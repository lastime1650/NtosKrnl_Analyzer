# MiCloneDiscardVadCommit

- RVA: `0x00AB0CD8`–`0x00AB0D13` (길이 `59` bytes)
- VA: `0x0000000140AB0CD8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A2244`
- 디코드: `20`개 명령, `59/59` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AB0D04` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MiCloneCaptureVadCommit](../../text/4B/MiCloneCaptureVadCommit_function_004B4554.md) at `0x004B4759`
- [MiDeletePartialCloneVads](../81/MiDeletePartialCloneVads_function_008116E4.md) at `0x00811873`
- [sub_00B2A0A2](../B2/Unknown_function_00B2A0A2.md) at `0x00B2A108`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00AB0D04` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB0CD8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00AB0CDD  57                              push rdi
00AB0CDE  48 83 EC 20                     sub rsp, 0x20
00AB0CE2  48 8B F9                        mov rdi, rcx
00AB0CE5  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00AB0CE9  48 85 C9                        test rcx, rcx
00AB0CEC  75 11                           jne 0x140ab0cff
00AB0CEE  48 83 67 08 00                  and qword ptr [rdi + 8], 0
00AB0CF3  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00AB0CF8  48 83 C4 20                     add rsp, 0x20
00AB0CFC  5F                              pop rdi
00AB0CFD  C3                              ret
00AB0CFE  CC                              int3
00AB0CFF  48 8B 19                        mov rbx, qword ptr [rcx]
00AB0D02  33 D2                           xor edx, edx
00AB0D04  E8 67 1B 0D 00                  call 0x140b82870
00AB0D09  48 8B CB                        mov rcx, rbx
00AB0D0C  48 85 DB                        test rbx, rbx
00AB0D0F  75 EE                           jne 0x140ab0cff
00AB0D11  EB DB                           jmp 0x140ab0cee
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCloneDiscardVadCommit(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 8) != 0) goto loc_00AB0CFF;
loc_00AB0CEE:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00AB0CFF:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) != 0) goto loc_00AB0CFF;
    goto loc_00AB0CEE;
}
```

## 5. (Beta) C Style

```c
int64_t MiCloneDiscardVadCommit(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0x8) != 0) goto loc_00AB0CFF;
loc_00AB0CEE:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00AB0CFF:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x8), Arg2, a3, a4);
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8)) != 0) goto loc_00AB0CFF;
    goto loc_00AB0CEE;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB0CD8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AB0CD8[BB_00AB0CD8]
  bb_00AB0CEE[BB_00AB0CEE]
  bb_00AB0CFE[BB_00AB0CFE]
  bb_00AB0CFF[BB_00AB0CFF]
  bb_00AB0D11[BB_00AB0D11]
  bb_00AB0CD8 -->|branch| bb_00AB0CFF
  bb_00AB0CD8 -->|fallthrough| bb_00AB0CEE
  bb_00AB0CFE -->|flow| bb_00AB0CFF
  bb_00AB0CFF -->|branch| bb_00AB0CFF
  bb_00AB0CFF -->|fallthrough| bb_00AB0D11
  bb_00AB0D11 -->|branch| bb_00AB0CEE
```
