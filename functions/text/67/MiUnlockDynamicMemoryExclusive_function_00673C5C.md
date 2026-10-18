# MiUnlockDynamicMemoryExclusive

- RVA: `0x00673C5C`–`0x00673CB8` (길이 `92` bytes)
- VA: `0x0000000140673C5C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `27`개 명령, `92/92` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00673C82` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00673C8A` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00673CA7` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)

### Direct callers
- [MiFreeUnusedPfnPages](MiFreeUnusedPfnPages_function_006720C0.md) at `0x0067212B`
- [MiClearPartitionPageBitMap](../69/MiClearPartitionPageBitMap_function_00690614.md) at `0x00690701`
- [MiInsertPartitionPageNodes](../69/MiInsertPartitionPageNodes_function_00690F94.md) at `0x00691123`
- [MiRebuildPartitionMemoryBlock](../69/MiRebuildPartitionMemoryBlock_function_00691AE8.md) at `0x00691B3E`
- [MiReturnPartitionPagesToParent](../69/MiReturnPartitionPagesToParent_function_00691B5C.md) at `0x00691D30`
- [MiReleaseAddMemoryLocks](../../page/7F/MiReleaseAddMemoryLocks_function_007FACEC.md) at `0x007FAD21`
- [MiUpdatePartitionLargePfnBitMap](../../page/80/MiUpdatePartitionLargePfnBitMap_function_0080DB50.md) at `0x0080DC10`
- [MiNodeZeroConductor](../../page/81/MiNodeZeroConductor_function_00810AC0.md) at `0x00810B30`
- [MiInitializeMirroring](../../init/C6/MiInitializeMirroring_function_00C64730.md) at `0x00C6486B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00673C5C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00673C61  57                              push rdi
00673C62  48 83 EC 20                     sub rsp, 0x20
00673C66  48 8B FA                        mov rdi, rdx
00673C69  48 8D 99 C0 00 00 00            lea rbx, [rcx + 0xc0]
00673C70  48 83 C8 FF                     or rax, 0xffffffffffffffff
00673C74  F0 48 0F C1 03                  lock xadd qword ptr [rbx], rax
00673C79  24 06                           and al, 6
00673C7B  3C 02                           cmp al, 2
00673C7D  75 08                           jne 0x140673c87
00673C7F  48 8B CB                        mov rcx, rbx
00673C82  E8 49 21 BF FF                  call 0x140265dd0
00673C87  48 8B CB                        mov rcx, rbx
00673C8A  E8 71 D9 C6 FF                  call 0x1402e1600
00673C8F  90                              nop
00673C90  66 83 87 E6 01 00 00 01         add word ptr [rdi + 0x1e6], 1
00673C98  75 12                           jne 0x140673cac
00673C9A  48 8D 87 98 00 00 00            lea rax, [rdi + 0x98]
00673CA1  90                              nop
00673CA2  48 39 00                        cmp qword ptr [rax], rax
00673CA5  74 05                           je 0x140673cac
00673CA7  E8 D4 EF C6 FF                  call 0x1402e2c80
00673CAC  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00673CB1  48 83 C4 20                     add rsp, 0x20
00673CB5  5F                              pop rdi
00673CB6  C3                              ret
00673CB7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUnlockDynamicMemoryExclusive(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = (result) | (-1);
    result = (unsigned __int8)((result) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = a1 + 192;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a1 + 192, a2, a3, a4);
    if (((unsigned __int8)(result)) != 2) goto loc_00673CAC;
    result = a2 + 152;
    if ((*(unsigned __int64 *)(a2 + 152)) != (a2 + 152)) {
        result = KiCheckForKernelApcDelivery(a1 + 192, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiUnlockDynamicMemoryExclusive(void *Arg1, void *Arg2)
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
        Arg1 = Arg1 + 192;
        result = ExfTryToWakePushLock(Arg1, Arg2, a3, a4);
    }
    result = KeAbPostRelease(Arg1 + 192, Arg2, a3, a4);
    if (((uint8_t)(result)) != 2) goto loc_00673CAC;
    result = Arg2 + 152;
    if ((*(uint64_t *)(arg2 + 0x98)) != (Arg2 + 152)) {
        result = KiCheckForKernelApcDelivery(Arg1 + 192, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x98` | `64` | `R` |
| `Arg2` | `+ 0x1E6` | `16` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00673C5C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00673C5C[BB_00673C5C]
  bb_00673C7F[BB_00673C7F]
  bb_00673C87[BB_00673C87]
  bb_00673C9A[BB_00673C9A]
  bb_00673CA7[BB_00673CA7]
  bb_00673CAC[BB_00673CAC]
  bb_00673CB7[BB_00673CB7]
  bb_00673C5C -->|branch| bb_00673C87
  bb_00673C5C -->|fallthrough| bb_00673C7F
  bb_00673C7F -->|flow| bb_00673C87
  bb_00673C87 -->|branch| bb_00673CAC
  bb_00673C87 -->|fallthrough| bb_00673C9A
  bb_00673C9A -->|branch| bb_00673CAC
  bb_00673C9A -->|fallthrough| bb_00673CA7
  bb_00673CA7 -->|flow| bb_00673CAC
```
