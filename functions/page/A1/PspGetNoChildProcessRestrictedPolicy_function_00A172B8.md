# PspGetNoChildProcessRestrictedPolicy

- RVA: `0x00A172B8`–`0x00A17338` (길이 `128` bytes)
- VA: `0x0000000140A172B8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9E38`
- 디코드: `37`개 명령, `128/128` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A172D8` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (function, `0x0020FF80`)
- `0x00A172F2` → [SeTokenGetNoChildProcessRestricted](../../text/45/SeTokenGetNoChildProcessRestricted_function_004584DC.md) (function, `0x004584DC`)
- `0x00A17307` → [ObFastDereferenceObject](../../text/3E/ObFastDereferenceObject_function_003ED5F0.md) (function, `0x003ED5F0`)

### Direct callers
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AAE82`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AC62C`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE84E1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A172D8` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (`PAGE` → `.text`)
  - `0x00A172F2` → [SeTokenGetNoChildProcessRestricted](../../text/45/SeTokenGetNoChildProcessRestricted_function_004584DC.md) (`PAGE` → `.text`)
  - `0x00A17307` → [ObFastDereferenceObject](../../text/3E/ObFastDereferenceObject_function_003ED5F0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A172B8  48 8B C4                        mov rax, rsp
00A172BB  48 89 58 20                     mov qword ptr [rax + 0x20], rbx
00A172BF  57                              push rdi
00A172C0  48 83 EC 20                     sub rsp, 0x20
00A172C4  BA 50 73 51 79                  mov edx, 0x79517350
00A172C9  C6 40 08 00                     mov byte ptr [rax + 8], 0
00A172CD  48 8B F9                        mov rdi, rcx
00A172D0  C6 40 10 00                     mov byte ptr [rax + 0x10], 0
00A172D4  C6 40 18 00                     mov byte ptr [rax + 0x18], 0
00A172D8  E8 A3 8C 7F FF                  call 0x14020ff80
00A172DD  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
00A172E2  48 8B C8                        mov rcx, rax
00A172E5  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
00A172EA  48 8B D8                        mov rbx, rax
00A172ED  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00A172F2  E8 E5 11 A4 FF                  call 0x1404584dc
00A172F7  48 8D 8F 48 02 00 00            lea rcx, [rdi + 0x248]
00A172FE  41 B8 50 73 51 79               mov r8d, 0x79517350
00A17304  48 8B D3                        mov rdx, rbx
00A17307  E8 E4 62 9D FF                  call 0x1403ed5f0
00A1730C  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
00A17311  75 17                           jne 0x140a1732a
00A17313  8A 44 24 40                     mov al, byte ptr [rsp + 0x40]
00A17317  F6 D8                           neg al
00A17319  1B C0                           sbb eax, eax
00A1731B  83 E0 03                        and eax, 3
00A1731E  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00A17323  48 83 C4 20                     add rsp, 0x20
00A17327  5F                              pop rdi
00A17328  C3                              ret
00A17329  CC                              int3
00A1732A  8A 44 24 38                     mov al, byte ptr [rsp + 0x38]
00A1732E  F6 D8                           neg al
00A17330  1B C0                           sbb eax, eax
00A17332  F7 D8                           neg eax
00A17334  FF C0                           inc eax
00A17336  EB E6                           jmp 0x140a1731e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspGetNoChildProcessRestrictedPolicy(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p38;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 32) = v_rbx;
    v_rsp = (v_rsp) - (32);
    *(unsigned __int8 *)(v_rsp + 8) = 0;
    *(unsigned __int8 *)(v_rsp + 16) = 0;
    *(unsigned __int8 *)(v_rsp + 24) = 0;
    result = PsReferencePrimaryTokenWithTag(a1, (unsigned int)(0x79517350ULL), a3, a4);
    result = SeTokenGetNoChildProcessRestricted(result, v_stack_p8, v_stack_p10, v_stack_p18);
    result = ObFastDereferenceObject(a1 + 584, result, (unsigned int)(0x79517350ULL), v_stack_p18);
    if (v_stack_p8 != 0) goto loc_00A1732A;
    result = (unsigned __int8)(-(v_stack_p18));
    result = (unsigned int)((result) & (3));
loc_00A1731E:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00A1732A:
    result = (unsigned __int8)(-(v_stack_p38));
    result = (unsigned int)(-(result));
    result = (unsigned int)((result) + 1);
    goto loc_00A1731E;
}
```

## 5. (Beta) C Style

```c
int64_t PspGetNoChildProcessRestrictedPolicy(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p38;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x20) = local_rbx;
    local_rsp = (local_rsp) - (32);
    *(uint8_t *)(local_rsp + 0x8) = 0;
    *(uint8_t *)(local_rsp + 0x10) = 0;
    *(uint8_t *)(local_rsp + 0x18) = 0;
    result = PsReferencePrimaryTokenWithTag(Arg1, (uint32_t)(0x79517350ULL), a3, a4);
    result = SeTokenGetNoChildProcessRestricted(result, v_stack_p8, v_stack_p10, v_stack_p18);
    result = ObFastDereferenceObject(Arg1 + 584, result, (uint32_t)(0x79517350ULL), v_stack_p18);
    if (v_stack_p8 != 0) goto loc_00A1732A;
    result = (uint8_t)(-(v_stack_p18));
    result = (uint32_t)((result) & (3));
loc_00A1731E:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00A1732A:
    result = (uint8_t)(-(v_stack_p38));
    result = (uint32_t)(-(result));
    result = (uint32_t)((result) + 1);
    goto loc_00A1731E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x248` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A172B8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A172B8[BB_00A172B8]
  bb_00A17313[BB_00A17313]
  bb_00A1731E[BB_00A1731E]
  bb_00A17329[BB_00A17329]
  bb_00A1732A[BB_00A1732A]
  bb_00A172B8 -->|branch| bb_00A1732A
  bb_00A172B8 -->|fallthrough| bb_00A17313
  bb_00A17313 -->|flow| bb_00A1731E
  bb_00A17329 -->|flow| bb_00A1732A
  bb_00A1732A -->|branch| bb_00A1731E
```
