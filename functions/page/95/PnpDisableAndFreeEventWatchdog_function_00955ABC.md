# PnpDisableAndFreeEventWatchdog

- RVA: `0x00955ABC`–`0x00955AF8` (길이 `60` bytes)
- VA: `0x0000000140955ABC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000682BC`
- 디코드: `19`개 명령, `60/60` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00955AE2` → [PnpDisableWatchdog](PnpDisableWatchdog_function_00955B00.md) (function, `0x00955B00`)
- `0x00955AF1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PnpProcessCompletedEject](../72/PnpProcessCompletedEject_function_0072D090.md) at `0x0072D1BF`
- [PnpDeviceEventWorker](PnpDeviceEventWorker_function_009556B0.md) at `0x009557E1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00955AF1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00955ABC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00955AC1  57                              push rdi
00955AC2  48 83 EC 20                     sub rsp, 0x20
00955AC6  48 8B F9                        mov rdi, rcx
00955AC9  48 8B 49 68                     mov rcx, qword ptr [rcx + 0x68]
00955ACD  48 85 C9                        test rcx, rcx
00955AD0  75 0C                           jne 0x140955ade
00955AD2  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00955AD7  48 83 C4 20                     add rsp, 0x20
00955ADB  5F                              pop rdi
00955ADC  C3                              ret
00955ADD  CC                              int3
00955ADE  48 8B 59 18                     mov rbx, qword ptr [rcx + 0x18]
00955AE2  E8 19 00 00 00                  call 0x140955b00
00955AE7  48 83 67 68 00                  and qword ptr [rdi + 0x68], 0
00955AEC  33 D2                           xor edx, edx
00955AEE  48 8B CB                        mov rcx, rbx
00955AF1  E8 7A CD 22 00                  call 0x140b82870
00955AF6  EB DA                           jmp 0x140955ad2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpDisableAndFreeEventWatchdog(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 104) != 0) goto loc_00955ADE;
loc_00955AD2:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00955ADE:
    result = PnpDisableWatchdog(*(unsigned __int64 *)(a1 + 104), a2, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104) + 24), a2, a3, a4);
    goto loc_00955AD2;
}
```

## 5. (Beta) C Style

```c
int64_t PnpDisableAndFreeEventWatchdog(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0x68) != 0) goto loc_00955ADE;
loc_00955AD2:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00955ADE:
    result = PnpDisableWatchdog(*(uint64_t *)(arg1 + 0x68), Arg2, a3, a4);
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68) + 0x18), Arg2, a3, a4);
    goto loc_00955AD2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00955ABC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00955ABC[BB_00955ABC]
  bb_00955AD2[BB_00955AD2]
  bb_00955ADD[BB_00955ADD]
  bb_00955ADE[BB_00955ADE]
  bb_00955ABC -->|branch| bb_00955ADE
  bb_00955ABC -->|fallthrough| bb_00955AD2
  bb_00955ADD -->|flow| bb_00955ADE
  bb_00955ADE -->|branch| bb_00955AD2
```
