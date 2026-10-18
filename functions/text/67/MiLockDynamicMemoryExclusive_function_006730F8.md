# MiLockDynamicMemoryExclusive

- RVA: `0x006730F8`–`0x0067314C` (길이 `84` bytes)
- VA: `0x00000001406730F8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `25`개 명령, `84/84` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00673119` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00673132` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [MiFreeUnusedPfnPages](MiFreeUnusedPfnPages_function_006720C0.md) at `0x006720F7`
- [MiClearPartitionPageBitMap](../69/MiClearPartitionPageBitMap_function_00690614.md) at `0x0069066E`
- [MiInsertPartitionPageNodes](../69/MiInsertPartitionPageNodes_function_00690F94.md) at `0x0069107F`
- [MiRebuildPartitionMemoryBlock](../69/MiRebuildPartitionMemoryBlock_function_00691AE8.md) at `0x00691B06`
- [MiReturnPartitionPagesToParent](../69/MiReturnPartitionPagesToParent_function_00691B5C.md) at `0x00691BC9`
- [MiAcquireAddMemoryLocks](../../page/7F/MiAcquireAddMemoryLocks_function_007F94F8.md) at `0x007F9512`
- [MiUpdatePartitionLargePfnBitMap](../../page/80/MiUpdatePartitionLargePfnBitMap_function_0080DB50.md) at `0x0080DB94`
- [MiNodeZeroConductor](../../page/81/MiNodeZeroConductor_function_00810AC0.md) at `0x00810B03`
- [MiInitializeMirroring](../../init/C6/MiInitializeMirroring_function_00C64730.md) at `0x00C64829`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006730F8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
006730FD  57                              push rdi
006730FE  48 83 EC 20                     sub rsp, 0x20
00673102  66 FF 8A E6 01 00 00            dec word ptr [rdx + 0x1e6]
00673109  48 8D B9 C0 00 00 00            lea rdi, [rcx + 0xc0]
00673110  48 8B CF                        mov rcx, rdi
00673113  45 33 C0                        xor r8d, r8d
00673116  33 D2                           xor edx, edx
00673118  90                              nop
00673119  E8 12 D1 B9 FF                  call 0x140210230
0067311E  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
00673124  48 8B D8                        mov rbx, rax
00673127  73 0E                           jae 0x140673137
00673129  4C 8B C7                        mov r8, rdi
0067312C  48 8B D0                        mov rdx, rax
0067312F  48 8B CF                        mov rcx, rdi
00673132  E8 59 CB B9 FF                  call 0x14020fc90
00673137  48 85 DB                        test rbx, rbx
0067313A  74 04                           je 0x140673140
0067313C  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
00673140  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00673145  48 83 C4 20                     add rsp, 0x20
00673149  5F                              pop rdi
0067314A  C3                              ret
0067314B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLockDynamicMemoryExclusive(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 192, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 192;
        a2 = result;
        a1 = a1 + 192;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiLockDynamicMemoryExclusive(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 192, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 192;
        Arg2 = result;
        Arg1 = Arg1 + 192;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
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
| `Arg2` | `+ 0x1E6` | `16` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006730F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006730F8[BB_006730F8]
  bb_00673129[BB_00673129]
  bb_00673137[BB_00673137]
  bb_0067313C[BB_0067313C]
  bb_00673140[BB_00673140]
  bb_0067314B[BB_0067314B]
  bb_006730F8 -->|branch| bb_00673137
  bb_006730F8 -->|fallthrough| bb_00673129
  bb_00673129 -->|flow| bb_00673137
  bb_00673137 -->|branch| bb_00673140
  bb_00673137 -->|fallthrough| bb_0067313C
  bb_0067313C -->|flow| bb_00673140
```
