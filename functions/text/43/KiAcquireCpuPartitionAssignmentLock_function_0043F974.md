# KiAcquireCpuPartitionAssignmentLock

- RVA: `0x0043F974`–`0x0043F9BA` (길이 `70` bytes)
- VA: `0x000000014043F974`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BE4`
- 디코드: `20`개 명령, `70/70` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0043F9A0` → [KeAcquireSpinLockAtDpcLevel](../20/KeAcquireSpinLockAtDpcLevel_function_00208430.md) (function, `0x00208430`)
- `0x0043F9B3` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)

### Direct callers
- [KiQueryCpuPartitionAffinityProcess](../3C/KiQueryCpuPartitionAffinityProcess_function_003C01A0.md) at `0x003C01EB`
- [KiRemoveAndFreeCpuPartitionAssignmentProcess](KiRemoveAndFreeCpuPartitionAssignmentProcess_function_0043F8C0.md) at `0x0043F8E8`
- [KiAvailableCpusPartitionWorkItemCallback](../5B/KiAvailableCpusPartitionWorkItemCallback_function_005B9990.md) at `0x005B9A50`
- [KeAssignCpuPartitionsToProcess](../5C/KeAssignCpuPartitionsToProcess_function_005C08D0.md) at `0x005C09DC`

### Static image references
- `0x0043F98E` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0043F997` → RVA `0x00F23448` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0043F974  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0043F979  57                              push rdi
0043F97A  48 83 EC 20                     sub rsp, 0x20
0043F97E  48 8B F9                        mov rdi, rcx
0043F981  44 0F 20 C3                     mov rbx, cr8
0043F985  BA 02 00 00 00                  mov edx, 2
0043F98A  44 0F 22 C2                     mov cr8, rdx
0043F98E  83 3D 8B 73 B8 00 00            cmp dword ptr [rip + 0xb8738b], 0
0043F995  75 1A                           jne 0x14043f9b1
0043F997  48 8D 0D AA 3A AE 00            lea rcx, [rip + 0xae3aaa]
0043F99E  88 1F                           mov byte ptr [rdi], bl
0043F9A0  E8 8B 8A DC FF                  call 0x140208430
0043F9A5  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0043F9AA  48 83 C4 20                     add rsp, 0x20
0043F9AE  5F                              pop rdi
0043F9AF  C3                              ret
0043F9B0  CC                              int3
0043F9B1  8A CB                           mov cl, bl
0043F9B3  E8 44 5D 0B 00                  call 0x1404f56fc
0043F9B8  EB DD                           jmp 0x14043f997
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiAcquireCpuPartitionAssignmentLock(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(v_rip + 12088203)) != 0) goto loc_0043F9B1;
loc_0043F997:
    *(unsigned __int8 *)(a1) = (unsigned __int8)(v_cr8);
    result = KeAcquireSpinLockAtDpcLevel(v_rip + 11418282, 2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_0043F9B1:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_p8), 2, a3, a4);
    goto loc_0043F997;
}
```

## 5. (Beta) C Style

```c
int64_t KiAcquireCpuPartitionAssignmentLock(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(v_rip + 0xB8738B)) != 0) goto loc_0043F9B1;
loc_0043F997:
    *(uint8_t *)(arg1) = (uint8_t)(v_cr8);
    result = KeAcquireSpinLockAtDpcLevel(v_rip + 11418282, 2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_0043F9B1:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_p8), 2, a3, a4);
    goto loc_0043F997;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043F974&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043F974[BB_0043F974]
  bb_0043F997[BB_0043F997]
  bb_0043F9B0[BB_0043F9B0]
  bb_0043F9B1[BB_0043F9B1]
  bb_0043F974 -->|branch| bb_0043F9B1
  bb_0043F974 -->|fallthrough| bb_0043F997
  bb_0043F9B0 -->|flow| bb_0043F9B1
  bb_0043F9B1 -->|branch| bb_0043F997
```
