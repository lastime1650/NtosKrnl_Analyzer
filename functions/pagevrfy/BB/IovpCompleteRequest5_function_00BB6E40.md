# IovpCompleteRequest5

- RVA: `0x00BB6E40`–`0x00BB6E84` (길이 `68` bytes)
- VA: `0x0000000140BB6E40`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063C24`
- 디코드: `21`개 명령, `68/68` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BB6E66` → [KeAcquireSpinLockRaiseToDpc](../../text/20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x00BB6E71` → [IovpSessionDataDereference](../BA/IovpSessionDataDereference_function_00BAC808.md) (function, `0x00BAC808`)
- `0x00BB6E7D` → [VfIrpDatabaseEntryReleaseLock](VfIrpDatabaseEntryReleaseLock_function_00BB3FD4.md) (function, `0x00BB3FD4`)

### Direct callers
- [IovpLocalCompletionRoutine](IovpLocalCompletionRoutine_function_00BB6B60.md) at `0x00BB6C55`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BB6E66` → [KeAcquireSpinLockRaiseToDpc](../../text/20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BB6E40  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00BB6E45  57                              push rdi
00BB6E46  48 83 EC 20                     sub rsp, 0x20
00BB6E4A  48 8B 39                        mov rdi, qword ptr [rcx]
00BB6E4D  48 85 FF                        test rdi, rdi
00BB6E50  75 0C                           jne 0x140bb6e5e
00BB6E52  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00BB6E57  48 83 C4 20                     add rsp, 0x20
00BB6E5B  5F                              pop rdi
00BB6E5C  C3                              ret
00BB6E5D  CC                              int3
00BB6E5E  48 8B 59 08                     mov rbx, qword ptr [rcx + 8]
00BB6E62  48 8D 4B 08                     lea rcx, [rbx + 8]
00BB6E66  E8 05 16 65 FF                  call 0x140208470
00BB6E6B  48 8B CF                        mov rcx, rdi
00BB6E6E  88 43 10                        mov byte ptr [rbx + 0x10], al
00BB6E71  E8 92 59 FF FF                  call 0x140bac808
00BB6E76  F0 FF 4B 14                     lock dec dword ptr [rbx + 0x14]
00BB6E7A  48 8B CB                        mov rcx, rbx
00BB6E7D  E8 52 D1 FF FF                  call 0x140bb3fd4
00BB6E82  EB CE                           jmp 0x140bb6e52
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IovpCompleteRequest5(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1) != 0) goto loc_00BB6E5E;
loc_00BB6E52:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00BB6E5E:
    result = KeAcquireSpinLockRaiseToDpc(*(unsigned __int64 *)(a1 + 8) + 8, a2, a3, a4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 16) = (unsigned __int8)(result);
    result = IovpSessionDataDereference(*(unsigned __int64 *)(a1), a2, a3, a4);
    result = VfIrpDatabaseEntryReleaseLock(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
    goto loc_00BB6E52;
}
```

## 5. (Beta) C Style

```c
int64_t IovpCompleteRequest5(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1) != 0) goto loc_00BB6E5E;
loc_00BB6E52:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00BB6E5E:
    result = KeAcquireSpinLockRaiseToDpc(*(uint64_t *)(arg1 + 0x8) + 8, a2, a3, a4);
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x10) = (uint8_t)(result);
    result = IovpSessionDataDereference(*(uint64_t *)(arg1), a2, a3, a4);
    result = VfIrpDatabaseEntryReleaseLock(*(uint64_t *)(arg1 + 0x8), a2, a3, a4);
    goto loc_00BB6E52;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BB6E40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BB6E40[BB_00BB6E40]
  bb_00BB6E52[BB_00BB6E52]
  bb_00BB6E5D[BB_00BB6E5D]
  bb_00BB6E5E[BB_00BB6E5E]
  bb_00BB6E40 -->|branch| bb_00BB6E5E
  bb_00BB6E40 -->|fallthrough| bb_00BB6E52
  bb_00BB6E5D -->|flow| bb_00BB6E5E
  bb_00BB6E5E -->|branch| bb_00BB6E52
```
