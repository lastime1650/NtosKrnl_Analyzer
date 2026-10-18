# DifZwCreateEventWrapper

- RVA: `0x0063F7A0`–`0x0063F932` (길이 `402` bytes)
- VA: `0x000000014063F7A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2BBC`
- 디코드: `116`개 명령, `402/402` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063F7E0` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063F806` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063F848` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063F86E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063F887` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063F8A0` → [ZwCreateEvent](../6A/ZwCreateEvent_function_006AD9D0.md) (function, `0x006AD9D0`)
- `0x0063F8CC` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063F8F2` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063F90B` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063F816` → RVA `0x00F048B8` (`.data`; read)
- `0x0063F835` → RVA `0x00F04980` (`.data`; read)
- `0x0063F841` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063F7A0  48 8B C4                        mov rax, rsp
0063F7A3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0063F7A7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063F7AB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0063F7AF  48 89 48 08                     mov qword ptr [rax + 8], rcx
0063F7B3  55                              push rbp
0063F7B4  41 54                           push r12
0063F7B6  41 55                           push r13
0063F7B8  41 56                           push r14
0063F7BA  41 57                           push r15
0063F7BC  48 8B EC                        mov rbp, rsp
0063F7BF  48 83 EC 60                     sub rsp, 0x60
0063F7C3  0F 57 C0                        xorps xmm0, xmm0
0063F7C6  B9 7D 00 00 00                  mov ecx, 0x7d
0063F7CB  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0063F7CF  45 8B F9                        mov r15d, r9d
0063F7D2  4D 8B E0                        mov r12, r8
0063F7D5  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0063F7D9  44 8B EA                        mov r13d, edx
0063F7DC  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0063F7E0  E8 4F 62 E5 FF                  call 0x140495a34
0063F7E5  48 8B F0                        mov rsi, rax
0063F7E8  48 85 C0                        test rax, rax
0063F7EB  0F 84 9B 00 00 00               je 0x14063f88c
0063F7F1  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063F7F4  A8 18                           test al, 0x18
0063F7F6  74 0A                           je 0x14063f802
0063F7F8  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063F7FC  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0063F800  EB 0D                           jmp 0x14063f80f
0063F802  A8 04                           test al, 4
0063F804  74 09                           je 0x14063f80f
0063F806  E8 FD 43 E9 FF                  call 0x1404d3c08
0063F80B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063F80F  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0063F813  45 32 F6                        xor r14b, r14b
0063F816  44 38 35 9B 50 8C 00            cmp byte ptr [rip + 0x8c509b], r14b
0063F81D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0063F821  8A 45 50                        mov al, byte ptr [rbp + 0x50]
0063F824  88 45 D8                        mov byte ptr [rbp - 0x28], al
0063F827  44 89 6D E8                     mov dword ptr [rbp - 0x18], r13d
0063F82B  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0063F82F  44 89 7D DC                     mov dword ptr [rbp - 0x24], r15d
0063F833  75 0C                           jne 0x14063f841
0063F835  F7 05 41 51 8C 00 00 08 00 00   test dword ptr [rip + 0x8c5141], 0x800
0063F83F  74 13                           je 0x14063f854
0063F841  48 8D 0D 38 46 8C 00            lea rcx, [rip + 0x8c4638]
0063F848  E8 D3 6D BD FF                  call 0x140216620
0063F84D  44 8A F0                        mov r14b, al
0063F850  84 C0                           test al, al
0063F852  74 38                           je 0x14063f88c
0063F854  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063F858  48 8B 1F                        mov rbx, qword ptr [rdi]
0063F85B  EB 19                           jmp 0x14063f876
0063F85D  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063F861  48 85 C0                        test rax, rax
0063F864  74 0D                           je 0x14063f873
0063F866  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063F86A  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063F86E  E8 5D B2 07 00                  call 0x1406baad0
0063F873  48 8B 1B                        mov rbx, qword ptr [rbx]
0063F876  48 3B DF                        cmp rbx, rdi
0063F879  75 E2                           jne 0x14063f85d
0063F87B  45 84 F6                        test r14b, r14b
0063F87E  74 0C                           je 0x14063f88c
0063F880  48 8D 0D F9 45 8C 00            lea rcx, [rip + 0x8c45f9]
0063F887  E8 F4 A5 D0 FF                  call 0x140349e80
0063F88C  8A 45 50                        mov al, byte ptr [rbp + 0x50]
0063F88F  45 8B CF                        mov r9d, r15d
0063F892  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0063F896  4D 8B C4                        mov r8, r12
0063F899  41 8B D5                        mov edx, r13d
0063F89C  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0063F8A0  E8 2B E1 06 00                  call 0x1406ad9d0
0063F8A5  89 45 F8                        mov dword ptr [rbp - 8], eax
0063F8A8  48 85 F6                        test rsi, rsi
0063F8AB  74 63                           je 0x14063f910
0063F8AD  40 32 FF                        xor dil, dil
0063F8B0  40 38 3D 01 50 8C 00            cmp byte ptr [rip + 0x8c5001], dil
0063F8B7  75 0C                           jne 0x14063f8c5
0063F8B9  F7 05 BD 50 8C 00 00 08 00 00   test dword ptr [rip + 0x8c50bd], 0x800
0063F8C3  74 13                           je 0x14063f8d8
0063F8C5  48 8D 0D B4 45 8C 00            lea rcx, [rip + 0x8c45b4]
0063F8CC  E8 4F 6D BD FF                  call 0x140216620
0063F8D1  40 8A F8                        mov dil, al
0063F8D4  84 C0                           test al, al
0063F8D6  74 38                           je 0x14063f910
0063F8D8  48 83 C6 30                     add rsi, 0x30
0063F8DC  48 8B 1E                        mov rbx, qword ptr [rsi]
0063F8DF  EB 19                           jmp 0x14063f8fa
0063F8E1  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063F8E5  48 85 C0                        test rax, rax
0063F8E8  74 0D                           je 0x14063f8f7
0063F8EA  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063F8EE  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063F8F2  E8 D9 B1 07 00                  call 0x1406baad0
0063F8F7  48 8B 1B                        mov rbx, qword ptr [rbx]
0063F8FA  48 3B DE                        cmp rbx, rsi
0063F8FD  75 E2                           jne 0x14063f8e1
0063F8FF  40 84 FF                        test dil, dil
0063F902  74 0C                           je 0x14063f910
0063F904  48 8D 0D 75 45 8C 00            lea rcx, [rip + 0x8c4575]
0063F90B  E8 70 A5 D0 FF                  call 0x140349e80
0063F910  8B 45 F8                        mov eax, dword ptr [rbp - 8]
0063F913  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
0063F918  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0063F91C  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0063F920  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0063F924  49 8B E3                        mov rsp, r11
0063F927  41 5F                           pop r15
0063F929  41 5E                           pop r14
0063F92B  41 5D                           pop r13
0063F92D  41 5C                           pop r12
0063F92F  5D                              pop rbp
0063F930  C3                              ret
0063F931  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwCreateEventWrapper(__int64 a1, int a2, __int64 a3, int a4, unsigned __int8 a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned __int8 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int8 v_stack_m68;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(125, a2, a3, a4);
    if (result == 0) goto loc_0063F88C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063F802;
    v_stack_m58 = v_stack_p0;
    goto loc_0063F80F;
loc_0063F802:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m50 = a5;
    v_stack_m40 = (unsigned int)((unsigned int)(a2));
    v_stack_m48 = a3;
    v_stack_m4C = (unsigned int)((unsigned int)(a4));
    if ((*(unsigned __int8 *)(v_rip + 9195675)) != 0) goto loc_0063F841;
    if (((*(unsigned int *)(v_rip + 9195841)) & (0x800ULL)) == 0) goto loc_0063F854;
loc_0063F841:
    result = ExAcquireRundownProtection(v_rip + 9193016, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063F88C;
loc_0063F854:
    goto loc_0063F876;
loc_0063F85D:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063F876:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063F85D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9192953;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m68 = a5;
    result = ZwCreateEvent(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_0063F910;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9195521)) != 0) goto loc_0063F8C5;
    if (((*(unsigned int *)(v_rip + 9195709)) & (0x800ULL)) == 0) goto loc_0063F8D8;
loc_0063F8C5:
    result = ExAcquireRundownProtection(v_rip + 9192884, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_0063F910;
loc_0063F8D8:
    v_rsi = (result) + (48);
    goto loc_0063F8FA;
loc_0063F8E1:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_0063F8FA:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063F8E1;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9192821;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwCreateEventWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, uint8_t Arg5)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint8_t v_stack_m50;
    uint64_t v_stack_m58;
    uint8_t v_stack_m68;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(125, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0063F88C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063F802;
    v_stack_m58 = v_stack_p0;
    goto loc_0063F80F;
loc_0063F802:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m50 = Arg5;
    v_stack_m40 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m48 = Arg3;
    v_stack_m4C = (uint32_t)((uint32_t)(Arg4));
    if ((*(uint8_t *)(v_rip + 0x8C509B)) != 0) goto loc_0063F841;
    if (((*(uint32_t *)(v_rip + 0x8C5141)) & (0x800ULL)) == 0) goto loc_0063F854;
loc_0063F841:
    result = ExAcquireRundownProtection(v_rip + 9193016, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0063F88C;
loc_0063F854:
    goto loc_0063F876;
loc_0063F85D:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0063F876:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063F85D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9192953;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m68 = Arg5;
    result = ZwCreateEvent(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_0063F910;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C5001)) != 0) goto loc_0063F8C5;
    if (((*(uint32_t *)(v_rip + 0x8C50BD)) & (0x800ULL)) == 0) goto loc_0063F8D8;
loc_0063F8C5:
    result = ExAcquireRundownProtection(v_rip + 9192884, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_0063F910;
loc_0063F8D8:
    local_rsi = (result) + (48);
    goto loc_0063F8FA;
loc_0063F8E1:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_0063F8FA:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063F8E1;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9192821;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063F7A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063F7A0[BB_0063F7A0]
  bb_0063F7F1[BB_0063F7F1]
  bb_0063F7F8[BB_0063F7F8]
  bb_0063F802[BB_0063F802]
  bb_0063F806[BB_0063F806]
  bb_0063F80F[BB_0063F80F]
  bb_0063F835[BB_0063F835]
  bb_0063F841[BB_0063F841]
  bb_0063F854[BB_0063F854]
  bb_0063F85D[BB_0063F85D]
  bb_0063F866[BB_0063F866]
  bb_0063F873[BB_0063F873]
  bb_0063F876[BB_0063F876]
  bb_0063F87B[BB_0063F87B]
  bb_0063F880[BB_0063F880]
  bb_0063F88C[BB_0063F88C]
  bb_0063F8AD[BB_0063F8AD]
  bb_0063F8B9[BB_0063F8B9]
  bb_0063F8C5[BB_0063F8C5]
  bb_0063F8D8[BB_0063F8D8]
  bb_0063F8E1[BB_0063F8E1]
  bb_0063F8EA[BB_0063F8EA]
  bb_0063F8F7[BB_0063F8F7]
  bb_0063F8FA[BB_0063F8FA]
  bb_0063F8FF[BB_0063F8FF]
  bb_0063F904[BB_0063F904]
  bb_0063F910[BB_0063F910]
  bb_0063F931[BB_0063F931]
  bb_0063F7A0 -->|branch| bb_0063F88C
  bb_0063F7A0 -->|fallthrough| bb_0063F7F1
  bb_0063F7F1 -->|branch| bb_0063F802
  bb_0063F7F1 -->|fallthrough| bb_0063F7F8
  bb_0063F7F8 -->|branch| bb_0063F80F
  bb_0063F802 -->|branch| bb_0063F80F
  bb_0063F802 -->|fallthrough| bb_0063F806
  bb_0063F806 -->|flow| bb_0063F80F
  bb_0063F80F -->|branch| bb_0063F841
  bb_0063F80F -->|fallthrough| bb_0063F835
  bb_0063F835 -->|branch| bb_0063F854
  bb_0063F835 -->|fallthrough| bb_0063F841
  bb_0063F841 -->|branch| bb_0063F88C
  bb_0063F841 -->|fallthrough| bb_0063F854
  bb_0063F854 -->|branch| bb_0063F876
  bb_0063F85D -->|branch| bb_0063F873
  bb_0063F85D -->|fallthrough| bb_0063F866
  bb_0063F866 -->|flow| bb_0063F873
  bb_0063F873 -->|flow| bb_0063F876
  bb_0063F876 -->|branch| bb_0063F85D
  bb_0063F876 -->|fallthrough| bb_0063F87B
  bb_0063F87B -->|branch| bb_0063F88C
  bb_0063F87B -->|fallthrough| bb_0063F880
  bb_0063F880 -->|flow| bb_0063F88C
  bb_0063F88C -->|branch| bb_0063F910
  bb_0063F88C -->|fallthrough| bb_0063F8AD
  bb_0063F8AD -->|branch| bb_0063F8C5
  bb_0063F8AD -->|fallthrough| bb_0063F8B9
  bb_0063F8B9 -->|branch| bb_0063F8D8
  bb_0063F8B9 -->|fallthrough| bb_0063F8C5
  bb_0063F8C5 -->|branch| bb_0063F910
  bb_0063F8C5 -->|fallthrough| bb_0063F8D8
  bb_0063F8D8 -->|branch| bb_0063F8FA
  bb_0063F8E1 -->|branch| bb_0063F8F7
  bb_0063F8E1 -->|fallthrough| bb_0063F8EA
  bb_0063F8EA -->|flow| bb_0063F8F7
  bb_0063F8F7 -->|flow| bb_0063F8FA
  bb_0063F8FA -->|branch| bb_0063F8E1
  bb_0063F8FA -->|fallthrough| bb_0063F8FF
  bb_0063F8FF -->|branch| bb_0063F910
  bb_0063F8FF -->|fallthrough| bb_0063F904
  bb_0063F904 -->|flow| bb_0063F910
```
