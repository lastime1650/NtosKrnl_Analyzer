# PopPlCommitPowerPlaneRegistration

- RVA: `0x005DDA00`–`0x005DDA34` (길이 `52` bytes)
- VA: `0x00000001405DDA00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `15`개 명령, `52/52` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005DDA15` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005DDA26` → RVA `0x00F070C0` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005DDA00  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005DDA05  57                              push rdi
005DDA06  48 83 EC 20                     sub rsp, 0x20
005DDA0A  48 8B 59 08                     mov rbx, qword ptr [rcx + 8]
005DDA0E  48 8B F9                        mov rdi, rcx
005DDA11  48 8D 4B 10                     lea rcx, [rbx + 0x10]
005DDA15  E8 56 AA C2 FF                  call 0x140208470
005DDA1A  88 43 18                        mov byte ptr [rbx + 0x18], al
005DDA1D  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
005DDA21  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
005DDA26  48 89 05 93 96 92 00            mov qword ptr [rip + 0x929693], rax
005DDA2D  48 83 C4 20                     add rsp, 0x20
005DDA31  5F                              pop rdi
005DDA32  C3                              ret
005DDA33  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPlCommitPowerPlaneRegistration(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = KeAcquireSpinLockRaiseToDpc(*(unsigned __int64 *)(a1 + 8) + 16, a2, a3, a4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 24) = (unsigned __int8)(result);
    *(unsigned __int64 *)(v_rip + 9606803) = *(unsigned __int64 *)(a1 + 8);
    v_rsp = (v_rsp) + (32);
    return *(unsigned __int64 *)(a1 + 8);
}
```

## 5. (Beta) C Style

```c
int64_t PopPlCommitPowerPlaneRegistration(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = KeAcquireSpinLockRaiseToDpc(*(uint64_t *)(arg1 + 0x8) + 16, a2, a3, a4);
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x18) = (uint8_t)(result);
    *(uint64_t *)(v_rip + 0x929693) = *(uint64_t *)(arg1 + 0x8);
    local_rsp = (local_rsp) + (32);
    return *(uint64_t *)(arg1 + 0x8);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005DDA00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005DDA00[BB_005DDA00]
  bb_005DDA33[BB_005DDA33]
```
