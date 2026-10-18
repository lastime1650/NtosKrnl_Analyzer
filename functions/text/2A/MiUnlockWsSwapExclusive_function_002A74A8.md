# MiUnlockWsSwapExclusive

- RVA: `0x002A74A8`–`0x002A7504` (길이 `92` bytes)
- VA: `0x00000001402A74A8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `27`개 명령, `92/92` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002A74CE` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x002A74D6` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x002A74F3` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)

### Direct callers
- [MmOutSwapWorkingSet](MmOutSwapWorkingSet_function_002A6BC8.md) at `0x002A6CDC`
- [MmOutSwapVirtualAddresses](MmOutSwapVirtualAddresses_function_002A8C30.md) at `0x002A8D69`
- [MiTrimUnusedPageFileRegionsWorker](MiTrimUnusedPageFileRegionsWorker_function_002AA320.md) at `0x002AA439`
- [MiContractWsSwapPageFileWorker](../68/MiContractWsSwapPageFileWorker_function_0068B860.md) at `0x0068B911`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002A74A8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002A74AD  57                              push rdi
002A74AE  48 83 EC 20                     sub rsp, 0x20
002A74B2  48 8B F9                        mov rdi, rcx
002A74B5  48 8D 9A 98 04 00 00            lea rbx, [rdx + 0x498]
002A74BC  48 83 C8 FF                     or rax, 0xffffffffffffffff
002A74C0  F0 48 0F C1 03                  lock xadd qword ptr [rbx], rax
002A74C5  24 06                           and al, 6
002A74C7  3C 02                           cmp al, 2
002A74C9  75 08                           jne 0x1402a74d3
002A74CB  48 8B CB                        mov rcx, rbx
002A74CE  E8 FD E8 FB FF                  call 0x140265dd0
002A74D3  48 8B CB                        mov rcx, rbx
002A74D6  E8 25 A1 03 00                  call 0x1402e1600
002A74DB  90                              nop
002A74DC  66 83 87 E6 01 00 00 01         add word ptr [rdi + 0x1e6], 1
002A74E4  75 12                           jne 0x1402a74f8
002A74E6  48 8D 87 98 00 00 00            lea rax, [rdi + 0x98]
002A74ED  90                              nop
002A74EE  48 39 00                        cmp qword ptr [rax], rax
002A74F1  74 05                           je 0x1402a74f8
002A74F3  E8 88 B7 03 00                  call 0x1402e2c80
002A74F8  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
002A74FD  48 83 C4 20                     add rsp, 0x20
002A7501  5F                              pop rdi
002A7502  C3                              ret
002A7503  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUnlockWsSwapExclusive(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = a2 + 1176;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a2 + 1176, a2, a3, a4);
    if (((unsigned __int8)(result)) != 2) goto loc_002A74F8;
    result = a1 + 152;
    if ((*(unsigned __int64 *)(a1 + 152)) != (a1 + 152)) {
        result = KiCheckForKernelApcDelivery(a2 + 1176, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiUnlockWsSwapExclusive(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = (result) | (-1);
    result = (uint8_t)((result) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = Arg2 + 1176;
        result = ExfTryToWakePushLock(Arg1, Arg2, a3, a4);
    }
    result = KeAbPostRelease(Arg2 + 1176, Arg2, a3, a4);
    if (((uint8_t)(result)) != 2) goto loc_002A74F8;
    result = Arg1 + 152;
    if ((*(uint64_t *)(arg1 + 0x98)) != (Arg1 + 152)) {
        result = KiCheckForKernelApcDelivery(Arg2 + 1176, Arg2, a3, a4);
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
| `Arg2` | `+ 0x0` | `64` | `R/W` |
| `Arg2` | `+ 0x498` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002A74A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002A74A8[BB_002A74A8]
  bb_002A74CB[BB_002A74CB]
  bb_002A74D3[BB_002A74D3]
  bb_002A74E6[BB_002A74E6]
  bb_002A74F3[BB_002A74F3]
  bb_002A74F8[BB_002A74F8]
  bb_002A7503[BB_002A7503]
  bb_002A74A8 -->|branch| bb_002A74D3
  bb_002A74A8 -->|fallthrough| bb_002A74CB
  bb_002A74CB -->|flow| bb_002A74D3
  bb_002A74D3 -->|branch| bb_002A74F8
  bb_002A74D3 -->|fallthrough| bb_002A74E6
  bb_002A74E6 -->|branch| bb_002A74F8
  bb_002A74E6 -->|fallthrough| bb_002A74F3
  bb_002A74F3 -->|flow| bb_002A74F8
```
