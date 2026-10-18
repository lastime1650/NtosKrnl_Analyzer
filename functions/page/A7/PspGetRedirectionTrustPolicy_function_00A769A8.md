# PspGetRedirectionTrustPolicy

- RVA: `0x00A769A8`–`0x00A76A18` (길이 `112` bytes)
- VA: `0x0000000140A769A8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B5CE0`
- 디코드: `30`개 명령, `112/112` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A769C4` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (function, `0x0020FF80`)
- `0x00A769D9` → [SeTokenGetRedirectionTrustPolicy](../../text/49/SeTokenGetRedirectionTrustPolicy_function_00498C30.md) (function, `0x00498C30`)
- `0x00A769EE` → [ObFastDereferenceObject](../../text/3E/ObFastDereferenceObject_function_003ED5F0.md) (function, `0x003ED5F0`)

### Direct callers
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AC9FB`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE85C7`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A769C4` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (`PAGE` → `.text`)
  - `0x00A769D9` → [SeTokenGetRedirectionTrustPolicy](../../text/49/SeTokenGetRedirectionTrustPolicy_function_00498C30.md) (`PAGE` → `.text`)
  - `0x00A769EE` → [ObFastDereferenceObject](../../text/3E/ObFastDereferenceObject_function_003ED5F0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A769A8  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00A769AD  57                              push rdi
00A769AE  48 83 EC 20                     sub rsp, 0x20
00A769B2  BA 50 73 51 79                  mov edx, 0x79517350
00A769B7  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
00A769BC  48 8B F9                        mov rdi, rcx
00A769BF  C6 44 24 38 00                  mov byte ptr [rsp + 0x38], 0
00A769C4  E8 B7 95 79 FF                  call 0x14020ff80
00A769C9  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
00A769CE  48 8B C8                        mov rcx, rax
00A769D1  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00A769D6  48 8B D8                        mov rbx, rax
00A769D9  E8 52 22 A2 FF                  call 0x140498c30
00A769DE  48 8D 8F 48 02 00 00            lea rcx, [rdi + 0x248]
00A769E5  41 B8 50 73 51 79               mov r8d, 0x79517350
00A769EB  48 8B D3                        mov rdx, rbx
00A769EE  E8 FD 6B 97 FF                  call 0x1403ed5f0
00A769F3  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
00A769F8  75 17                           jne 0x140a76a11
00A769FA  8A 44 24 38                     mov al, byte ptr [rsp + 0x38]
00A769FE  F6 D8                           neg al
00A76A00  1B C0                           sbb eax, eax
00A76A02  83 E0 02                        and eax, 2
00A76A05  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00A76A0A  48 83 C4 20                     add rsp, 0x20
00A76A0E  5F                              pop rdi
00A76A0F  C3                              ret
00A76A10  CC                              int3
00A76A11  B8 01 00 00 00                  mov eax, 1
00A76A16  EB ED                           jmp 0x140a76a05
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspGetRedirectionTrustPolicy(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p8;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (32);
    v_stack_p8 = 0;
    v_stack_p10 = 0;
    result = PsReferencePrimaryTokenWithTag(a1, (unsigned int)(0x79517350ULL), a3, a4);
    result = SeTokenGetRedirectionTrustPolicy(result, v_stack_p8, v_stack_p10, a4);
    result = ObFastDereferenceObject(a1 + 584, result, (unsigned int)(0x79517350ULL), a4);
    if (v_stack_p8 != 0) goto loc_00A76A11;
    result = (unsigned __int8)(-(v_stack_p10));
    result = (unsigned int)((result) & (2));
loc_00A76A05:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00A76A11:
    goto loc_00A76A05;
}
```

## 5. (Beta) C Style

```c
int64_t PspGetRedirectionTrustPolicy(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_p10;
    uint64_t v_stack_p18;
    uint8_t v_stack_p8;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (32);
    v_stack_p8 = 0;
    v_stack_p10 = 0;
    result = PsReferencePrimaryTokenWithTag(Arg1, (uint32_t)(0x79517350ULL), a3, a4);
    result = SeTokenGetRedirectionTrustPolicy(result, v_stack_p8, v_stack_p10, a4);
    result = ObFastDereferenceObject(Arg1 + 584, result, (uint32_t)(0x79517350ULL), a4);
    if (v_stack_p8 != 0) goto loc_00A76A11;
    result = (uint8_t)(-(v_stack_p10));
    result = (uint32_t)((result) & (2));
loc_00A76A05:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00A76A11:
    goto loc_00A76A05;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x248` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A769A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A769A8[BB_00A769A8]
  bb_00A769FA[BB_00A769FA]
  bb_00A76A05[BB_00A76A05]
  bb_00A76A10[BB_00A76A10]
  bb_00A76A11[BB_00A76A11]
  bb_00A769A8 -->|branch| bb_00A76A11
  bb_00A769A8 -->|fallthrough| bb_00A769FA
  bb_00A769FA -->|flow| bb_00A76A05
  bb_00A76A10 -->|flow| bb_00A76A11
  bb_00A76A11 -->|branch| bb_00A76A05
```
