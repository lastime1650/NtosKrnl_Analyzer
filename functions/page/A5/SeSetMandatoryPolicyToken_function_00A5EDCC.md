# SeSetMandatoryPolicyToken

- RVA: `0x00A5EDCC`–`0x00A5EE55` (길이 `137` bytes)
- VA: `0x0000000140A5EDCC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006CF28`
- 디코드: `35`개 명령, `137/137` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A5EDFB` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00A5EE36` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A5EE3B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [SepCreateAppContainerToken](../../text/4F/SepCreateAppContainerToken_function_004F43AC.md) at `0x004F481D`
- [NtCreateLowBoxToken](../AB/NtCreateLowBoxToken_function_00AB9880.md) at `0x00ABA081`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF1803`
- [SeMakeAnonymousLogonToken](../../init/C4/SeMakeAnonymousLogonToken_function_00C4A8D8.md) at `0x00C4AB07`
- [SeMakeAnonymousLogonTokenNoEveryone](../../init/C4/SeMakeAnonymousLogonTokenNoEveryone_function_00C4AB5C.md) at `0x00C4AD65`
- [SeMakeSystemToken](../../init/C4/SeMakeSystemToken_function_00C4ADBC.md) at `0x00C4B2ED`

### Static image references
- `0x00A5EE07` → RVA `0x00012D08` (`.rdata`; read)
- `0x00A5EE17` → RVA `0x00E0EBF0` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A5EDFB` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00A5EE36` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A5EE3B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A5EDCC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A5EDD1  57                              push rdi
00A5EDD2  48 83 EC 20                     sub rsp, 0x20
00A5EDD6  F7 02 FC FF FF FF               test dword ptr [rdx], 0xfffffffc
00A5EDDC  48 8B DA                        mov rbx, rdx
00A5EDDF  48 8B F9                        mov rdi, rcx
00A5EDE2  75 6A                           jne 0x140a5ee4e
00A5EDE4  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A5EDED  B2 01                           mov dl, 1
00A5EDEF  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00A5EDF6  90                              nop
00A5EDF7  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
00A5EDFB  E8 20 60 7B FF                  call 0x140214e20
00A5EE00  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
00A5EE05  8B 03                           mov eax, dword ptr [rbx]
00A5EE07  48 8B 0D FA 3E 5B FF            mov rcx, qword ptr [rip - 0xa4c106]
00A5EE0E  89 87 D4 00 00 00               mov dword ptr [rdi + 0xd4], eax
00A5EE14  48 8B C1                        mov rax, rcx
00A5EE17  F0 48 0F C1 05 D0 FD 3A 00      lock xadd qword ptr [rip + 0x3afdd0], rax
00A5EE20  48 03 C1                        add rax, rcx
00A5EE23  89 47 38                        mov dword ptr [rdi + 0x38], eax
00A5EE26  48 C1 E8 20                     shr rax, 0x20
00A5EE2A  89 47 3C                        mov dword ptr [rdi + 0x3c], eax
00A5EE2D  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
00A5EE32  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00A5EE36  E8 D5 0B 80 FF                  call 0x14025fa10
00A5EE3B  E8 70 EA 7F FF                  call 0x14025d8b0
00A5EE40  33 C0                           xor eax, eax
00A5EE42  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A5EE47  48 83 C4 20                     add rsp, 0x20
00A5EE4B  5F                              pop rdi
00A5EE4C  C3                              ret
00A5EE4D  CC                              int3
00A5EE4E  B8 0D 00 00 C0                  mov eax, 0xc000000d
00A5EE53  EB ED                           jmp 0x140a5ee42
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeSetMandatoryPolicyToken(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if (((*(unsigned int *)(a2)) & (0xFFFFFFFCULL)) != 0) goto loc_00A5EE4E;
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(a1 + 48), 1, a3, a4);
    *(unsigned int *)(a1 + 212) = (unsigned int)((unsigned int)(*(unsigned int *)(a2)));
    result = (*(unsigned __int64 *)(v_rip - 10797318)) + (*(unsigned __int64 *)(v_rip - 10797318));
    *(unsigned int *)(a1 + 56) = (unsigned int)(result);
    result = (result) >> (32);
    *(unsigned int *)(a1 + 60) = (unsigned int)(result);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(a1 + 48), 1, a3, a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(a1 + 48), 1, a3, a4);
    result = 0;
loc_00A5EE42:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00A5EE4E:
    goto loc_00A5EE42;
}
```

## 5. (Beta) C Style

```c
int64_t SeSetMandatoryPolicyToken(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m28;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if (((*(uint32_t *)(arg2)) & (0xFFFFFFFCULL)) != 0) goto loc_00A5EE4E;
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(arg1 + 0x30), 1, a3, a4);
    *(uint32_t *)(arg1 + 0xD4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2)));
    result = (*(uint64_t *)(v_rip - 0xA4C106)) + (*(uint64_t *)(v_rip - 0xA4C106));
    *(uint32_t *)(arg1 + 0x38) = (uint32_t)(result);
    result = (result) >> (32);
    *(uint32_t *)(arg1 + 0x3C) = (uint32_t)(result);
    result = ExReleaseResourceLite(*(uint64_t *)(arg1 + 0x30), 1, a3, a4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(arg1 + 0x30), 1, a3, a4);
    result = 0;
loc_00A5EE42:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00A5EE4E:
    goto loc_00A5EE42;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `32` | `W` |
| `Arg1` | `+ 0x3C` | `32` | `W` |
| `Arg1` | `+ 0xD4` | `32` | `W` |
| `Arg2` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A5EDCC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A5EDCC[BB_00A5EDCC]
  bb_00A5EDE4[BB_00A5EDE4]
  bb_00A5EE42[BB_00A5EE42]
  bb_00A5EE4D[BB_00A5EE4D]
  bb_00A5EE4E[BB_00A5EE4E]
  bb_00A5EDCC -->|branch| bb_00A5EE4E
  bb_00A5EDCC -->|fallthrough| bb_00A5EDE4
  bb_00A5EDE4 -->|flow| bb_00A5EE42
  bb_00A5EE4D -->|flow| bb_00A5EE4E
  bb_00A5EE4E -->|branch| bb_00A5EE42
```
