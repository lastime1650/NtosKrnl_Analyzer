# PerfInfoLogVirtualAlloc

- RVA: `0x00A45754`–`0x00A45856` (길이 `258` bytes)
- VA: `0x0000000140A45754`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AF4E0`
- 디코드: `62`개 명령, `258/258` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A457B2` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (function, `0x0044BEE0`)
- `0x00A457DB` → [EtwTraceSiloKernelEvent](../../text/22/EtwTraceSiloKernelEvent_function_002242A0.md) (function, `0x002242A0`)
- `0x00A457F1` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A4582B` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (function, `0x0044BEE0`)
- `0x00A4584F` → [EtwTraceSiloKernelEvent](../../text/22/EtwTraceSiloKernelEvent_function_002242A0.md) (function, `0x002242A0`)

### Direct callers
- [MiAllocateVirtualMemory](../88/MiAllocateVirtualMemory_function_00883B40.md) at `0x00884217`
- [sub_00B44B9C](../B4/Unknown_function_00B44B9C.md) at `0x00B44C07`

### Static image references
- `0x00A4576B` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x00A457B2` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (`PAGE` → `.text`)
  - `0x00A457DB` → [EtwTraceSiloKernelEvent](../../text/22/EtwTraceSiloKernelEvent_function_002242A0.md) (`PAGE` → `.text`)
  - `0x00A457F1` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A4582B` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (`PAGE` → `.text`)
  - `0x00A4584F` → [EtwTraceSiloKernelEvent](../../text/22/EtwTraceSiloKernelEvent_function_002242A0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A45754  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A45759  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00A4575E  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00A45763  55                              push rbp
00A45764  48 8B EC                        mov rbp, rsp
00A45767  48 83 EC 70                     sub rsp, 0x70
00A4576B  48 8B 05 CE 4F 3C 00            mov rax, qword ptr [rip + 0x3c4fce]
00A45772  48 33 C4                        xor rax, rsp
00A45775  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00A45779  41 8B 80 D0 01 00 00            mov eax, dword ptr [r8 + 0x1d0]
00A45780  48 8B F9                        mov rdi, rcx
00A45783  83 65 F4 00                     and dword ptr [rbp - 0xc], 0
00A45787  0F 57 C0                        xorps xmm0, xmm0
00A4578A  89 45 E0                        mov dword ptr [rbp - 0x20], eax
00A4578D  49 8B D8                        mov rbx, r8
00A45790  48 8D 45 D0                     lea rax, [rbp - 0x30]
00A45794  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00A45798  49 8B C8                        mov rcx, r8
00A4579B  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00A4579F  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00A457A3  48 89 55 D8                     mov qword ptr [rbp - 0x28], rdx
00A457A7  44 89 4D E4                     mov dword ptr [rbp - 0x1c], r9d
00A457AB  C7 45 F0 18 00 00 00            mov dword ptr [rbp - 0x10], 0x18
00A457B2  E8 29 67 A0 FF                  call 0x14044bee0
00A457B7  BE 00 80 00 20                  mov esi, 0x20008000
00A457BC  C7 44 24 28 02 19 60 00         mov dword ptr [rsp + 0x28], 0x601902
00A457C4  44 8B CE                        mov r9d, esi
00A457C7  66 C7 44 24 20 62 02            mov word ptr [rsp + 0x20], 0x262
00A457CE  48 8B C8                        mov rcx, rax
00A457D1  48 8D 55 E8                     lea rdx, [rbp - 0x18]
00A457D5  41 B8 01 00 00 00               mov r8d, 1
00A457DB  E8 C0 EA 7D FF                  call 0x1402242a0
00A457E0  0F B7 45 38                     movzx eax, word ptr [rbp + 0x38]
00A457E4  66 39 45 30                     cmp word ptr [rbp + 0x30], ax
00A457E8  75 23                           jne 0x140a4580d
00A457EA  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
00A457EE  48 33 CC                        xor rcx, rsp
00A457F1  E8 4A 6E C6 FF                  call 0x1406ac640
00A457F6  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00A457FB  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
00A457FF  49 8B 73 18                     mov rsi, qword ptr [r11 + 0x18]
00A45803  49 8B 7B 28                     mov rdi, qword ptr [r11 + 0x28]
00A45807  49 8B E3                        mov rsp, r11
00A4580A  5D                              pop rbp
00A4580B  C3                              ret
00A4580C  CC                              int3
00A4580D  83 65 F4 00                     and dword ptr [rbp - 0xc], 0
00A45811  48 8B CB                        mov rcx, rbx
00A45814  66 89 45 C8                     mov word ptr [rbp - 0x38], ax
00A45818  48 8D 45 C0                     lea rax, [rbp - 0x40]
00A4581C  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00A45820  48 89 7D C0                     mov qword ptr [rbp - 0x40], rdi
00A45824  C7 45 F0 10 00 00 00            mov dword ptr [rbp - 0x10], 0x10
00A4582B  E8 B0 66 A0 FF                  call 0x14044bee0
00A45830  48 8B C8                        mov rcx, rax
00A45833  C7 44 24 28 02 19 60 00         mov dword ptr [rsp + 0x28], 0x601902
00A4583B  44 8B CE                        mov r9d, esi
00A4583E  66 C7 44 24 20 89 02            mov word ptr [rsp + 0x20], 0x289
00A45845  41 B8 01 00 00 00               mov r8d, 1
00A4584B  48 8D 55 E8                     lea rdx, [rbp - 0x18]
00A4584F  E8 4C EA 7D FF                  call 0x1402242a0
00A45854  EB 94                           jmp 0x140a457ea
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PerfInfoLogVirtualAlloc(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned __int16 a5, unsigned __int16 a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m24;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int16 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int16 v_stack_m58;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (112);
    result = (*(unsigned __int64 *)(v_rip + 3952590)) ^ (v_rsp);
    v_stack_m10 = result;
    v_stack_m28 = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 464)));
    v_stack_m38 = a1;
    v_stack_m20 = v_stack_m38;
    v_stack_m48 = v_xmm0;
    v_stack_m30 = a2;
    v_stack_m24 = a4;
    v_stack_m18 = 24;
    result = PsGetProcessServerSilo(a3, a2, a3, a4);
    v_stack_m50 = 0x601902ULL;
    v_stack_m58 = 610;
    result = EtwTraceSiloKernelEvent(result, v_stack_m20, 1, (unsigned int)((unsigned int)((unsigned int)(0x20008000ULL))));
    if (a5 != a6) goto loc_00A4580D;
loc_00A457EA:
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m20, 1, (unsigned int)((unsigned int)((unsigned int)(0x20008000ULL))));
    return result;
loc_00A4580D:
    v_stack_m40 = (unsigned __int16)(result);
    v_stack_m20 = v_stack_m48;
    v_stack_m48 = *(unsigned __int64 *)(v_stack_m8 + 40);
    v_stack_m18 = 16;
    result = PsGetProcessServerSilo(*(unsigned __int64 *)(v_stack_m8 + 16), v_stack_m20, 1, (unsigned int)((unsigned int)((unsigned int)(0x20008000ULL))));
    v_stack_m48 = 0x601902ULL;
    v_stack_m50 = 649;
    result = EtwTraceSiloKernelEvent(result, v_stack_m20, 1, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m8 + 24))));
    goto loc_00A457EA;
}
```

## 5. (Beta) C Style

```c
int64_t PerfInfoLogVirtualAlloc(int64_t Arg1, int64_t Arg2, void *Arg3, int32_t Arg4, uint16_t Arg5, uint16_t Arg6)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m24;
    uint32_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint16_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint16_t v_stack_m58;
    uint64_t v_stack_m8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (112);
    result = (*(uint64_t *)(v_rip + 0x3C4FCE)) ^ (local_rsp);
    v_stack_m10 = result;
    v_stack_m28 = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x1D0)));
    v_stack_m38 = Arg1;
    v_stack_m20 = v_stack_m38;
    v_stack_m48 = v_xmm0;
    v_stack_m30 = Arg2;
    v_stack_m24 = Arg4;
    v_stack_m18 = 24;
    result = PsGetProcessServerSilo(Arg3, Arg2, Arg3, Arg4);
    v_stack_m50 = 0x601902ULL;
    v_stack_m58 = 610;
    result = EtwTraceSiloKernelEvent(result, v_stack_m20, 1, (uint32_t)((uint32_t)((uint32_t)(0x20008000ULL))));
    if (Arg5 != Arg6) goto loc_00A4580D;
loc_00A457EA:
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m20, 1, (uint32_t)((uint32_t)((uint32_t)(0x20008000ULL))));
    return result;
loc_00A4580D:
    v_stack_m40 = (uint16_t)(result);
    v_stack_m20 = v_stack_m48;
    v_stack_m48 = *(uint64_t *)(v_stack_m8 + 0x28);
    v_stack_m18 = 16;
    result = PsGetProcessServerSilo(*(uint64_t *)(v_stack_m8 + 0x10), v_stack_m20, 1, (uint32_t)((uint32_t)((uint32_t)(0x20008000ULL))));
    v_stack_m48 = 0x601902ULL;
    v_stack_m50 = 649;
    result = EtwTraceSiloKernelEvent(result, v_stack_m20, 1, (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m8 + 0x18))));
    goto loc_00A457EA;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x1D0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A45754&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A45754[BB_00A45754]
  bb_00A457EA[BB_00A457EA]
  bb_00A4580C[BB_00A4580C]
  bb_00A4580D[BB_00A4580D]
  bb_00A45754 -->|branch| bb_00A4580D
  bb_00A45754 -->|fallthrough| bb_00A457EA
  bb_00A4580C -->|flow| bb_00A4580D
  bb_00A4580D -->|branch| bb_00A457EA
```
