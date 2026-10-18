# MiPreparePlaceholderVadReplacement

- RVA: `0x00A7E998`–`0x00A7EA48` (길이 `176` bytes)
- VA: `0x0000000140A7E998`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008E1C0`
- 디코드: `48`개 명령, `176/176` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A7E9B0` → [MiReferenceVad](../../text/29/MiReferenceVad_function_00295890.md) (function, `0x00295890`)
- `0x00A7E9BD` → [MiRemoveVad](../../text/29/MiRemoveVad_function_00295C78.md) (function, `0x00295C78`)
- `0x00A7EA41` → [PerfInfoLogVirtualFree](../88/PerfInfoLogVirtualFree_function_00880B98.md) (function, `0x00880B98`)

### Direct callers
- [MiReserveUserMemory](../88/MiReserveUserMemory_function_00884498.md) at `0x00884AD1`
- [sub_008857C1](../88/Unknown_function_008857C1.md) at `0x008858A1`

### Static image references
- `0x00A7E9FF` → RVA `0x00FC6B04` (`ALMOSTRO`; reference)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A7E9B0` → [MiReferenceVad](../../text/29/MiReferenceVad_function_00295890.md) (`PAGE` → `.text`)
  - `0x00A7E9BD` → [MiRemoveVad](../../text/29/MiRemoveVad_function_00295C78.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A7E998  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A7E99D  57                              push rdi
00A7E99E  48 83 EC 20                     sub rsp, 0x20
00A7E9A2  48 8B FA                        mov rdi, rdx
00A7E9A5  48 8B D9                        mov rbx, rcx
00A7E9A8  F0 41 FF 80 E8 00 00 00         lock inc dword ptr [r8 + 0xe8]
00A7E9B0  E8 DB 6E 81 FF                  call 0x140295890
00A7E9B5  48 8B CB                        mov rcx, rbx
00A7E9B8  45 33 C0                        xor r8d, r8d
00A7E9BB  33 D2                           xor edx, edx
00A7E9BD  E8 B6 72 81 FF                  call 0x140295c78
00A7E9C2  4C 8B 87 28 02 00 00            mov r8, qword ptr [rdi + 0x228]
00A7E9C9  41 B9 00 80 00 00               mov r9d, 0x8000
00A7E9CF  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
00A7E9D2  0F B6 4B 21                     movzx ecx, byte ptr [rbx + 0x21]
00A7E9D6  0F B6 53 20                     movzx edx, byte ptr [rbx + 0x20]
00A7E9DA  48 C1 E2 20                     shl rdx, 0x20
00A7E9DE  48 C1 E1 20                     shl rcx, 0x20
00A7E9E2  48 0B C8                        or rcx, rax
00A7E9E5  8B 43 18                        mov eax, dword ptr [rbx + 0x18]
00A7E9E8  48 0B D0                        or rdx, rax
00A7E9EB  48 2B D1                        sub rdx, rcx
00A7E9EE  48 FF CA                        dec rdx
00A7E9F1  48 C1 E2 0C                     shl rdx, 0xc
00A7E9F5  49 03 D0                        add rdx, r8
00A7E9F8  48 89 97 28 02 00 00            mov qword ptr [rdi + 0x228], rdx
00A7E9FF  44 85 0D FE 80 54 00            test dword ptr [rip + 0x5480fe], r9d
00A7EA06  75 0C                           jne 0x140a7ea14
00A7EA08  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A7EA0D  48 83 C4 20                     add rsp, 0x20
00A7EA11  5F                              pop rdi
00A7EA12  C3                              ret
00A7EA13  CC                              int3
00A7EA14  8B 43 18                        mov eax, dword ptr [rbx + 0x18]
00A7EA17  4C 8B C7                        mov r8, rdi
00A7EA1A  0F B6 4B 20                     movzx ecx, byte ptr [rbx + 0x20]
00A7EA1E  0F B6 53 21                     movzx edx, byte ptr [rbx + 0x21]
00A7EA22  48 C1 E2 20                     shl rdx, 0x20
00A7EA26  48 C1 E1 20                     shl rcx, 0x20
00A7EA2A  48 0B C8                        or rcx, rax
00A7EA2D  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
00A7EA30  48 0B D0                        or rdx, rax
00A7EA33  48 2B D1                        sub rdx, rcx
00A7EA36  48 C1 E1 0C                     shl rcx, 0xc
00A7EA3A  48 FF C2                        inc rdx
00A7EA3D  48 C1 E2 0C                     shl rdx, 0xc
00A7EA41  E8 52 21 E0 FF                  call 0x140880b98
00A7EA46  EB C0                           jmp 0x140a7ea08
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiPreparePlaceholderVadReplacement(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = MiReferenceVad(a1, a2, a3, a4);
    a3 = 0;
    a2 = 0;
    result = MiRemoveVad(a1, a2, a3, a4);
    a2 = (*(unsigned __int8 *)(a1 + 32)) << (32);
    a1 = (*(unsigned __int8 *)(a1 + 33)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(a1 + 28)));
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(a1 + 24)));
    a2 = (a2) - (a1);
    a2 = (a2) - 1;
    a2 = (a2) << (12);
    a2 = (a2) + (*(unsigned __int64 *)(a2 + 552));
    *(unsigned __int64 *)(a2 + 552) = a2;
    if (((*(unsigned int *)(v_rip + 5538046)) & ((unsigned int)((unsigned int)(0x8000ULL)))) != 0) goto loc_00A7EA14;
loc_00A7EA08:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)(*(unsigned int *)(a1 + 24));
loc_00A7EA14:
    a2 = (*(unsigned __int8 *)(v_stack_p8 + 33)) << (32);
    a1 = (*(unsigned __int8 *)(v_stack_p8 + 32)) << (32);
    a1 = (a1) | ((unsigned int)(*(unsigned int *)(v_stack_p8 + 24)));
    a2 = (a2) | ((unsigned int)(*(unsigned int *)(v_stack_p8 + 28)));
    a2 = (a2) - (a1);
    a1 = (a1) << (12);
    a2 = (a2) + 1;
    a2 = (a2) << (12);
    result = PerfInfoLogVirtualFree(a1, a2, a2, (unsigned int)(0x8000ULL));
    goto loc_00A7EA08;
}
```

## 5. (Beta) C Style

```c
int64_t MiPreparePlaceholderVadReplacement(void *Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = MiReferenceVad(Arg1, Arg2, Arg3, a4);
    Arg3 = 0;
    Arg2 = 0;
    result = MiRemoveVad(Arg1, Arg2, Arg3, a4);
    Arg2 = (*(uint8_t *)(arg1 + 0x20)) << (32);
    Arg1 = (*(uint8_t *)(arg1 + 0x21)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(arg1 + 0x1C)));
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(arg1 + 0x18)));
    Arg2 = (Arg2) - (Arg1);
    Arg2 = (Arg2) - 1;
    Arg2 = (Arg2) << (12);
    Arg2 = (Arg2) + (*(uint64_t *)(arg2 + 0x228));
    *(void **)(arg2 + 0x228) = Arg2;
    if (((*(uint32_t *)(v_rip + 0x5480FE)) & ((uint32_t)((uint32_t)(0x8000ULL)))) != 0) goto loc_00A7EA14;
loc_00A7EA08:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)(*(uint32_t *)(arg1 + 0x18));
loc_00A7EA14:
    Arg2 = (*(uint8_t *)(v_stack_p8 + 0x21)) << (32);
    Arg1 = (*(uint8_t *)(v_stack_p8 + 0x20)) << (32);
    Arg1 = (Arg1) | ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x18)));
    Arg2 = (Arg2) | ((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x1C)));
    Arg2 = (Arg2) - (Arg1);
    Arg1 = (Arg1) << (12);
    Arg2 = (Arg2) + 1;
    Arg2 = (Arg2) << (12);
    result = PerfInfoLogVirtualFree(Arg1, Arg2, Arg2, (uint32_t)(0x8000ULL));
    goto loc_00A7EA08;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x20` | `8` | `R` |
| `Arg1` | `+ 0x21` | `8` | `R` |
| `Arg2` | `+ 0x228` | `64` | `R` |
| `Arg2` | `+ 0x228` | `64` | `W` |
| `Arg3` | `+ 0xE8` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A7E998&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A7E998[BB_00A7E998]
  bb_00A7EA08[BB_00A7EA08]
  bb_00A7EA13[BB_00A7EA13]
  bb_00A7EA14[BB_00A7EA14]
  bb_00A7E998 -->|branch| bb_00A7EA14
  bb_00A7E998 -->|fallthrough| bb_00A7EA08
  bb_00A7EA13 -->|flow| bb_00A7EA14
  bb_00A7EA14 -->|branch| bb_00A7EA08
```
