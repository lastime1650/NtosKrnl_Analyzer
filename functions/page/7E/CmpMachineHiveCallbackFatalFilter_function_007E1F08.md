# CmpMachineHiveCallbackFatalFilter

- RVA: `0x007E1F08`–`0x007E1F2D` (길이 `37` bytes)
- VA: `0x00000001407E1F08`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000622F0`
- 디코드: `10`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007E1F27` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [CmpMachineHiveLoadedWorkItem$filt$0](../B1/CmpMachineHiveLoadedWorkItem_filt_0_function_00B15771.md) at `0x00B1577E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007E1F27` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007E1F08  48 83 EC 38                     sub rsp, 0x38
007E1F0C  48 8B 01                        mov rax, qword ptr [rcx]
007E1F0F  4C 8B CA                        mov r9, rdx
007E1F12  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
007E1F16  B9 3F 01 00 00                  mov ecx, 0x13f
007E1F1B  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
007E1F20  48 63 10                        movsxd rdx, dword ptr [rax]
007E1F23  4D 8B 49 50                     mov r9, qword ptr [r9 + 0x50]
007E1F27  E8 34 B7 D1 FF                  call 0x1404fd660
007E1F2C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpMachineHiveCallbackFatalFilter(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    v_stack_m18 = a2;
    result = KeBugCheckEx(319, (int)(*(unsigned int *)(*(unsigned __int64 *)(a1))), *(unsigned __int64 *)(a1 + 8), *(unsigned __int64 *)(a2 + 80));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpMachineHiveCallbackFatalFilter(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    v_stack_m18 = Arg2;
    result = KeBugCheckEx(319, (int32_t)(*(uint32_t *)(*(uint64_t *)(arg1))), *(uint64_t *)(arg1 + 0x8), *(uint64_t *)(arg2 + 0x50));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x50` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007E1F08&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007E1F08[BB_007E1F08]
```
