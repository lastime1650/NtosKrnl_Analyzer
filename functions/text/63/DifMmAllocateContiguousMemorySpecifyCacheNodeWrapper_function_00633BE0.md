# DifMmAllocateContiguousMemorySpecifyCacheNodeWrapper

- RVA: `0x00633BE0`–`0x00633D89` (길이 `425` bytes)
- VA: `0x0000000140633BE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD780`
- 디코드: `122`개 명령, `425/425` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00633C26` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00633C4E` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00633C96` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00633CBC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00633CD5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00633CF5` → [MmAllocateContiguousMemorySpecifyCacheNode](../3E/MmAllocateContiguousMemorySpecifyCacheNode_function_003E9D30.md) (function, `0x003E9D30`)
- `0x00633D22` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00633D48` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00633D61` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00633C5E` → RVA `0x00F048B8` (`.data`; read)
- `0x00633C83` → RVA `0x00F04980` (`.data`; read)
- `0x00633C8F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00633BE0  48 8B C4                        mov rax, rsp
00633BE3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00633BE7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00633BEB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00633BEF  48 89 48 08                     mov qword ptr [rax + 8], rcx
00633BF3  55                              push rbp
00633BF4  41 54                           push r12
00633BF6  41 55                           push r13
00633BF8  41 56                           push r14
00633BFA  41 57                           push r15
00633BFC  48 8B EC                        mov rbp, rsp
00633BFF  48 83 EC 70                     sub rsp, 0x70
00633C03  0F 57 C0                        xorps xmm0, xmm0
00633C06  33 C0                           xor eax, eax
00633C08  B9 EB 00 00 00                  mov ecx, 0xeb
00633C0D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00633C11  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00633C15  49 8B D9                        mov rbx, r9
00633C18  49 8B F8                        mov rdi, r8
00633C1B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00633C1F  48 8B F2                        mov rsi, rdx
00633C22  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00633C26  E8 09 1E E6 FF                  call 0x140495a34
00633C2B  4C 8B E8                        mov r13, rax
00633C2E  48 85 C0                        test rax, rax
00633C31  0F 84 A3 00 00 00               je 0x140633cda
00633C37  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00633C3A  F6 C1 18                        test cl, 0x18
00633C3D  74 0A                           je 0x140633c49
00633C3F  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00633C43  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00633C47  EB 0E                           jmp 0x140633c57
00633C49  F6 C1 04                        test cl, 4
00633C4C  74 09                           je 0x140633c57
00633C4E  E8 B5 FF E9 FF                  call 0x1404d3c08
00633C53  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00633C57  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00633C5B  45 32 E4                        xor r12b, r12b
00633C5E  44 38 25 53 0C 8D 00            cmp byte ptr [rip + 0x8d0c53], r12b
00633C65  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00633C69  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00633C6C  89 45 CC                        mov dword ptr [rbp - 0x34], eax
00633C6F  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
00633C72  89 45 C8                        mov dword ptr [rbp - 0x38], eax
00633C75  48 89 75 E0                     mov qword ptr [rbp - 0x20], rsi
00633C79  48 89 7D D8                     mov qword ptr [rbp - 0x28], rdi
00633C7D  48 89 5D D0                     mov qword ptr [rbp - 0x30], rbx
00633C81  75 0C                           jne 0x140633c8f
00633C83  F7 05 F3 0C 8D 00 00 08 00 00   test dword ptr [rip + 0x8d0cf3], 0x800
00633C8D  74 13                           je 0x140633ca2
00633C8F  48 8D 0D EA 01 8D 00            lea rcx, [rip + 0x8d01ea]
00633C96  E8 85 29 BE FF                  call 0x140216620
00633C9B  44 8A E0                        mov r12b, al
00633C9E  84 C0                           test al, al
00633CA0  74 38                           je 0x140633cda
00633CA2  4D 8D 7D 20                     lea r15, [r13 + 0x20]
00633CA6  4D 8B 37                        mov r14, qword ptr [r15]
00633CA9  EB 19                           jmp 0x140633cc4
00633CAB  49 8D 46 F0                     lea rax, [r14 - 0x10]
00633CAF  48 85 C0                        test rax, rax
00633CB2  74 0D                           je 0x140633cc1
00633CB4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00633CB8  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00633CBC  E8 0F 6E 08 00                  call 0x1406baad0
00633CC1  4D 8B 36                        mov r14, qword ptr [r14]
00633CC4  4D 3B F7                        cmp r14, r15
00633CC7  75 E2                           jne 0x140633cab
00633CC9  45 84 E4                        test r12b, r12b
00633CCC  74 0C                           je 0x140633cda
00633CCE  48 8D 0D AB 01 8D 00            lea rcx, [rip + 0x8d01ab]
00633CD5  E8 A6 61 D1 FF                  call 0x140349e80
00633CDA  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
00633CDD  4C 8B CB                        mov r9, rbx
00633CE0  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00633CE4  4C 8B C7                        mov r8, rdi
00633CE7  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00633CEB  48 8B D6                        mov rdx, rsi
00633CEE  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00633CF1  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00633CF5  E8 36 60 DB FF                  call 0x1403e9d30
00633CFA  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00633CFE  4D 85 ED                        test r13, r13
00633D01  74 63                           je 0x140633d66
00633D03  40 32 FF                        xor dil, dil
00633D06  40 38 3D AB 0B 8D 00            cmp byte ptr [rip + 0x8d0bab], dil
00633D0D  75 0C                           jne 0x140633d1b
00633D0F  F7 05 67 0C 8D 00 00 08 00 00   test dword ptr [rip + 0x8d0c67], 0x800
00633D19  74 13                           je 0x140633d2e
00633D1B  48 8D 0D 5E 01 8D 00            lea rcx, [rip + 0x8d015e]
00633D22  E8 F9 28 BE FF                  call 0x140216620
00633D27  40 8A F8                        mov dil, al
00633D2A  84 C0                           test al, al
00633D2C  74 38                           je 0x140633d66
00633D2E  49 8D 75 30                     lea rsi, [r13 + 0x30]
00633D32  48 8B 1E                        mov rbx, qword ptr [rsi]
00633D35  EB 19                           jmp 0x140633d50
00633D37  48 8D 43 F0                     lea rax, [rbx - 0x10]
00633D3B  48 85 C0                        test rax, rax
00633D3E  74 0D                           je 0x140633d4d
00633D40  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00633D44  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00633D48  E8 83 6D 08 00                  call 0x1406baad0
00633D4D  48 8B 1B                        mov rbx, qword ptr [rbx]
00633D50  48 3B DE                        cmp rbx, rsi
00633D53  75 E2                           jne 0x140633d37
00633D55  40 84 FF                        test dil, dil
00633D58  74 0C                           je 0x140633d66
00633D5A  48 8D 0D 1F 01 8D 00            lea rcx, [rip + 0x8d011f]
00633D61  E8 1A 61 D1 FF                  call 0x140349e80
00633D66  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00633D6A  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00633D6F  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00633D73  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00633D77  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00633D7B  49 8B E3                        mov rsp, r11
00633D7E  41 5F                           pop r15
00633D80  41 5E                           pop r14
00633D82  41 5D                           pop r13
00633D84  41 5C                           pop r12
00633D86  5D                              pop rbp
00633D87  C3                              ret
00633D88  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmAllocateContiguousMemorySpecifyCacheNodeWrapper(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (112);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(235, a2, a3, a4);
    if (result == 0) goto loc_00633CDA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00633C49;
    v_stack_m68 = v_stack_p0;
    goto loc_00633C57;
loc_00633C49:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m68 = result;
    }
    v_r12 = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m5C = (unsigned int)((unsigned int)(a5));
    v_stack_m60 = (unsigned int)((unsigned int)(a6));
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    v_stack_m58 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9243731)) != 0) goto loc_00633C8F;
    if (((*(unsigned int *)(v_rip + 9243891)) & (0x800ULL)) == 0) goto loc_00633CA2;
loc_00633C8F:
    result = ExAcquireRundownProtection(v_rip + 9241066, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00633CDA;
loc_00633CA2:
    goto loc_00633CC4;
loc_00633CAB:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00633CC4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00633CAB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9241003;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m70 = (unsigned int)((unsigned int)(a6));
    v_stack_m78 = (unsigned int)((unsigned int)(a5));
    result = MmAllocateContiguousMemorySpecifyCacheNode(v_stack_p8, a2, a3, a4);
    v_stack_m38 = result;
    if (result == 0) goto loc_00633D66;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9243563)) != 0) goto loc_00633D1B;
    if (((*(unsigned int *)(v_rip + 9243751)) & (0x800ULL)) == 0) goto loc_00633D2E;
loc_00633D1B:
    result = ExAcquireRundownProtection(v_rip + 9240926, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00633D66;
loc_00633D2E:
    goto loc_00633D50;
loc_00633D37:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00633D50:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_00633D37;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9240863;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return v_stack_m38;
}
```

## 5. (Beta) C Style

```c
int64_t DifMmAllocateContiguousMemorySpecifyCacheNodeWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (112);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(235, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00633CDA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00633C49;
    v_stack_m68 = v_stack_p0;
    goto loc_00633C57;
loc_00633C49:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m68 = result;
    }
    local_r12 = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m5C = (uint32_t)((uint32_t)(Arg5));
    v_stack_m60 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    v_stack_m58 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8D0C53)) != 0) goto loc_00633C8F;
    if (((*(uint32_t *)(v_rip + 0x8D0CF3)) & (0x800ULL)) == 0) goto loc_00633CA2;
loc_00633C8F:
    result = ExAcquireRundownProtection(v_rip + 9241066, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00633CDA;
loc_00633CA2:
    goto loc_00633CC4;
loc_00633CAB:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00633CC4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00633CAB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9241003;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m70 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m78 = (uint32_t)((uint32_t)(Arg5));
    result = MmAllocateContiguousMemorySpecifyCacheNode(v_stack_p8, Arg2, Arg3, Arg4);
    v_stack_m38 = result;
    if (result == 0) goto loc_00633D66;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D0BAB)) != 0) goto loc_00633D1B;
    if (((*(uint32_t *)(v_rip + 0x8D0C67)) & (0x800ULL)) == 0) goto loc_00633D2E;
loc_00633D1B:
    result = ExAcquireRundownProtection(v_rip + 9240926, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00633D66;
loc_00633D2E:
    goto loc_00633D50;
loc_00633D37:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00633D50:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_00633D37;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9240863;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    return v_stack_m38;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00633BE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00633BE0[BB_00633BE0]
  bb_00633C37[BB_00633C37]
  bb_00633C3F[BB_00633C3F]
  bb_00633C49[BB_00633C49]
  bb_00633C4E[BB_00633C4E]
  bb_00633C57[BB_00633C57]
  bb_00633C83[BB_00633C83]
  bb_00633C8F[BB_00633C8F]
  bb_00633CA2[BB_00633CA2]
  bb_00633CAB[BB_00633CAB]
  bb_00633CB4[BB_00633CB4]
  bb_00633CC1[BB_00633CC1]
  bb_00633CC4[BB_00633CC4]
  bb_00633CC9[BB_00633CC9]
  bb_00633CCE[BB_00633CCE]
  bb_00633CDA[BB_00633CDA]
  bb_00633D03[BB_00633D03]
  bb_00633D0F[BB_00633D0F]
  bb_00633D1B[BB_00633D1B]
  bb_00633D2E[BB_00633D2E]
  bb_00633D37[BB_00633D37]
  bb_00633D40[BB_00633D40]
  bb_00633D4D[BB_00633D4D]
  bb_00633D50[BB_00633D50]
  bb_00633D55[BB_00633D55]
  bb_00633D5A[BB_00633D5A]
  bb_00633D66[BB_00633D66]
  bb_00633D88[BB_00633D88]
  bb_00633BE0 -->|branch| bb_00633CDA
  bb_00633BE0 -->|fallthrough| bb_00633C37
  bb_00633C37 -->|branch| bb_00633C49
  bb_00633C37 -->|fallthrough| bb_00633C3F
  bb_00633C3F -->|branch| bb_00633C57
  bb_00633C49 -->|branch| bb_00633C57
  bb_00633C49 -->|fallthrough| bb_00633C4E
  bb_00633C4E -->|flow| bb_00633C57
  bb_00633C57 -->|branch| bb_00633C8F
  bb_00633C57 -->|fallthrough| bb_00633C83
  bb_00633C83 -->|branch| bb_00633CA2
  bb_00633C83 -->|fallthrough| bb_00633C8F
  bb_00633C8F -->|branch| bb_00633CDA
  bb_00633C8F -->|fallthrough| bb_00633CA2
  bb_00633CA2 -->|branch| bb_00633CC4
  bb_00633CAB -->|branch| bb_00633CC1
  bb_00633CAB -->|fallthrough| bb_00633CB4
  bb_00633CB4 -->|flow| bb_00633CC1
  bb_00633CC1 -->|flow| bb_00633CC4
  bb_00633CC4 -->|branch| bb_00633CAB
  bb_00633CC4 -->|fallthrough| bb_00633CC9
  bb_00633CC9 -->|branch| bb_00633CDA
  bb_00633CC9 -->|fallthrough| bb_00633CCE
  bb_00633CCE -->|flow| bb_00633CDA
  bb_00633CDA -->|branch| bb_00633D66
  bb_00633CDA -->|fallthrough| bb_00633D03
  bb_00633D03 -->|branch| bb_00633D1B
  bb_00633D03 -->|fallthrough| bb_00633D0F
  bb_00633D0F -->|branch| bb_00633D2E
  bb_00633D0F -->|fallthrough| bb_00633D1B
  bb_00633D1B -->|branch| bb_00633D66
  bb_00633D1B -->|fallthrough| bb_00633D2E
  bb_00633D2E -->|branch| bb_00633D50
  bb_00633D37 -->|branch| bb_00633D4D
  bb_00633D37 -->|fallthrough| bb_00633D40
  bb_00633D40 -->|flow| bb_00633D4D
  bb_00633D4D -->|flow| bb_00633D50
  bb_00633D50 -->|branch| bb_00633D37
  bb_00633D50 -->|fallthrough| bb_00633D55
  bb_00633D55 -->|branch| bb_00633D66
  bb_00633D55 -->|fallthrough| bb_00633D5A
  bb_00633D5A -->|flow| bb_00633D66
```
