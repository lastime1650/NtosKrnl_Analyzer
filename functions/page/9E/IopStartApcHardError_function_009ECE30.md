# IopStartApcHardError

- RVA: `0x009ECE30`–`0x009ECE9B` (길이 `107` bytes)
- VA: `0x00000001409ECE30`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A5B78`
- 디코드: `31`개 명령, `107/107` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x009ECE6A` → [PsCreateSystemThreadEx](PsCreateSystemThreadEx_function_009ED120.md) (function, `0x009ED120`)
- `0x009ECE78` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x009ECE8A` → [IofCompleteRequest](../../text/29/IofCompleteRequest_function_0029B5C0.md) (function, `0x0029B5C0`)
- `0x009ECE94` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x009ECE3D` → RVA `0x00A64220` (`IopApcHardError`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x009ECE78` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x009ECE8A` → [IofCompleteRequest](../../text/29/IofCompleteRequest_function_0029B5C0.md) (`PAGE` → `.text`)
  - `0x009ECE94` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009ECE30  4C 8B DC                        mov r11, rsp
009ECE33  53                              push rbx
009ECE34  48 83 EC 50                     sub rsp, 0x50
009ECE38  49 83 63 E8 00                  and qword ptr [r11 - 0x18], 0
009ECE3D  48 8D 05 DC 73 07 00            lea rax, [rip + 0x773dc]
009ECE44  49 83 63 E0 00                  and qword ptr [r11 - 0x20], 0
009ECE49  48 8B D9                        mov rbx, rcx
009ECE4C  49 83 63 10 00                  and qword ptr [r11 + 0x10], 0
009ECE51  45 33 C9                        xor r9d, r9d
009ECE54  49 89 4B D8                     mov qword ptr [r11 - 0x28], rcx
009ECE58  45 33 C0                        xor r8d, r8d
009ECE5B  49 89 43 D0                     mov qword ptr [r11 - 0x30], rax
009ECE5F  49 8D 4B 10                     lea rcx, [r11 + 0x10]
009ECE63  49 83 63 C8 00                  and qword ptr [r11 - 0x38], 0
009ECE68  33 D2                           xor edx, edx
009ECE6A  E8 B1 02 00 00                  call 0x1409ed120
009ECE6F  85 C0                           test eax, eax
009ECE71  78 11                           js 0x1409ece84
009ECE73  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
009ECE78  E8 33 04 CC FF                  call 0x1406ad2b0
009ECE7D  48 83 C4 50                     add rsp, 0x50
009ECE81  5B                              pop rbx
009ECE82  C3                              ret
009ECE83  CC                              int3
009ECE84  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
009ECE88  B2 01                           mov dl, 1
009ECE8A  E8 31 E7 8A FF                  call 0x14029b5c0
009ECE8F  33 D2                           xor edx, edx
009ECE91  48 8B CB                        mov rcx, rbx
009ECE94  E8 D7 59 19 00                  call 0x140b82870
009ECE99  EB E2                           jmp 0x1409ece7d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopStartApcHardError(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_rsp = (v_rsp) - (80);
    a4 = 0;
    *(unsigned __int64 *)(v_rsp - 40) = a1;
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 48) = v_rip + 488412;
    a2 = 0;
    result = PsCreateSystemThreadEx(v_rsp + 16, a2, a3, a4);
    if (sign_flag) goto loc_009ECE84;
    result = ZwClose(v_stack_p10, a2, a3, a4);
loc_009ECE7D:
    v_rsp = (v_rsp) + (80);
    return result;
loc_009ECE84:
    result = IofCompleteRequest(*(unsigned __int64 *)(a1 + 32), 1, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, a3, a4);
    goto loc_009ECE7D;
}
```

## 5. (Beta) C Style

```c
int64_t IopStartApcHardError(void *Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    local_rsp = (local_rsp) - (80);
    Arg4 = 0;
    *(void **)(local_rsp - 0x28) = Arg1;
    Arg3 = 0;
    *(uint64_t *)(local_rsp - 0x30) = v_rip + 488412;
    Arg2 = 0;
    result = PsCreateSystemThreadEx(local_rsp + 16, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_009ECE84;
    result = ZwClose(v_stack_p10, Arg2, Arg3, Arg4);
loc_009ECE7D:
    local_rsp = (local_rsp) + (80);
    return result;
loc_009ECE84:
    result = IofCompleteRequest(*(uint64_t *)(arg1 + 0x20), 1, Arg3, Arg4);
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    goto loc_009ECE7D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009ECE30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009ECE30[BB_009ECE30]
  bb_009ECE73[BB_009ECE73]
  bb_009ECE7D[BB_009ECE7D]
  bb_009ECE83[BB_009ECE83]
  bb_009ECE84[BB_009ECE84]
  bb_009ECE30 -->|branch| bb_009ECE84
  bb_009ECE30 -->|fallthrough| bb_009ECE73
  bb_009ECE73 -->|flow| bb_009ECE7D
  bb_009ECE83 -->|flow| bb_009ECE84
  bb_009ECE84 -->|branch| bb_009ECE7D
```
