# PsGetThreadExitStatus

- RVA: `0x00A65500`–`0x00A65541` (길이 `65` bytes)
- VA: `0x0000000140A65500`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B38AC`
- 디코드: `19`개 명령, `65/65` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A65517` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00A65535` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- [MiInjectThreadForHotPatch](../80/MiInjectThreadForHotPatch_function_00803FD8.md) at `0x00804152`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE397B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A65517` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x00A65535` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A65500  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A65505  57                              push rdi
00A65506  48 83 EC 20                     sub rsp, 0x20
00A6550A  48 8D B9 88 05 00 00            lea rdi, [rcx + 0x588]
00A65511  48 8B D9                        mov rbx, rcx
00A65514  48 8B CF                        mov rcx, rdi
00A65517  E8 04 11 7B FF                  call 0x140216620
00A6551C  84 C0                           test al, al
00A6551E  75 12                           jne 0x140a65532
00A65520  8B 83 D8 05 00 00               mov eax, dword ptr [rbx + 0x5d8]
00A65526  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A6552B  48 83 C4 20                     add rsp, 0x20
00A6552F  5F                              pop rdi
00A65530  C3                              ret
00A65531  CC                              int3
00A65532  48 8B CF                        mov rcx, rdi
00A65535  E8 46 49 8E FF                  call 0x140349e80
00A6553A  B8 03 01 00 00                  mov eax, 0x103
00A6553F  EB E5                           jmp 0x140a65526
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsGetThreadExitStatus(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = ExAcquireRundownProtection(a1 + 1416, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00A65532;
loc_00A65526:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)(*(unsigned int *)(a1 + 1496));
loc_00A65532:
    result = ExReleaseRundownProtection(a1 + 1416, a2, a3, a4);
    goto loc_00A65526;
}
```

## 5. (Beta) C Style

```c
int64_t PsGetThreadExitStatus(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = ExAcquireRundownProtection(Arg1 + 1416, a2, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_00A65532;
loc_00A65526:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)(*(uint32_t *)(arg1 + 0x5D8));
loc_00A65532:
    result = ExReleaseRundownProtection(Arg1 + 1416, a2, a3, a4);
    goto loc_00A65526;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x588` | `64` | `R` |
| `Arg1` | `+ 0x5D8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A65500&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A65500[BB_00A65500]
  bb_00A65520[BB_00A65520]
  bb_00A65526[BB_00A65526]
  bb_00A65531[BB_00A65531]
  bb_00A65532[BB_00A65532]
  bb_00A65500 -->|branch| bb_00A65532
  bb_00A65500 -->|fallthrough| bb_00A65520
  bb_00A65520 -->|flow| bb_00A65526
  bb_00A65531 -->|flow| bb_00A65532
  bb_00A65532 -->|branch| bb_00A65526
```
