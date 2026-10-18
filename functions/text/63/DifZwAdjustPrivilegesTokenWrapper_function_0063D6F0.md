# DifZwAdjustPrivilegesTokenWrapper

- RVA: `0x0063D6F0`–`0x0063D899` (길이 `425` bytes)
- VA: `0x000000014063D6F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD780`
- 디코드: `120`개 명령, `425/425` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063D726` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0063D730` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063D758` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063D7A4` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063D7CA` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063D7E3` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063D807` → [ZwAdjustPrivilegesToken](../6A/ZwAdjustPrivilegesToken_function_006AD8F0.md) (function, `0x006AD8F0`)
- `0x0063D833` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063D859` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063D872` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063D768` → RVA `0x00F048B8` (`.data`; read)
- `0x0063D791` → RVA `0x00F04980` (`.data`; read)
- `0x0063D79D` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063D6F0  48 8B C4                        mov rax, rsp
0063D6F3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0063D6F7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063D6FB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0063D6FF  48 89 48 08                     mov qword ptr [rax + 8], rcx
0063D703  55                              push rbp
0063D704  41 54                           push r12
0063D706  41 55                           push r13
0063D708  41 56                           push r14
0063D70A  41 57                           push r15
0063D70C  48 8B EC                        mov rbp, rsp
0063D70F  48 83 EC 70                     sub rsp, 0x70
0063D713  44 8A EA                        mov r13b, dl
0063D716  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0063D71A  33 D2                           xor edx, edx
0063D71C  4D 8B E0                        mov r12, r8
0063D71F  45 8B F9                        mov r15d, r9d
0063D722  44 8D 42 40                     lea r8d, [rdx + 0x40]
0063D726  E8 15 95 08 00                  call 0x1406c6c40
0063D72B  B9 91 00 00 00                  mov ecx, 0x91
0063D730  E8 FF 82 E5 FF                  call 0x140495a34
0063D735  4C 8B F0                        mov r14, rax
0063D738  48 85 C0                        test rax, rax
0063D73B  0F 84 A7 00 00 00               je 0x14063d7e8
0063D741  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
0063D744  F6 C1 18                        test cl, 0x18
0063D747  74 0A                           je 0x14063d753
0063D749  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063D74D  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
0063D751  EB 0E                           jmp 0x14063d761
0063D753  F6 C1 04                        test cl, 4
0063D756  74 09                           je 0x14063d761
0063D758  E8 AB 64 E9 FF                  call 0x1404d3c08
0063D75D  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0063D761  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0063D765  40 32 F6                        xor sil, sil
0063D768  40 38 35 49 71 8C 00            cmp byte ptr [rip + 0x8c7149], sil
0063D76F  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0063D773  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0063D777  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063D77B  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0063D77F  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0063D783  44 88 6D E8                     mov byte ptr [rbp - 0x18], r13b
0063D787  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0063D78B  44 89 7D D8                     mov dword ptr [rbp - 0x28], r15d
0063D78F  75 0C                           jne 0x14063d79d
0063D791  F7 05 E5 71 8C 00 00 08 00 00   test dword ptr [rip + 0x8c71e5], 0x800
0063D79B  74 13                           je 0x14063d7b0
0063D79D  48 8D 0D DC 66 8C 00            lea rcx, [rip + 0x8c66dc]
0063D7A4  E8 77 8E BD FF                  call 0x140216620
0063D7A9  40 8A F0                        mov sil, al
0063D7AC  84 C0                           test al, al
0063D7AE  74 38                           je 0x14063d7e8
0063D7B0  49 8D 7E 20                     lea rdi, [r14 + 0x20]
0063D7B4  48 8B 1F                        mov rbx, qword ptr [rdi]
0063D7B7  EB 19                           jmp 0x14063d7d2
0063D7B9  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063D7BD  48 85 C0                        test rax, rax
0063D7C0  74 0D                           je 0x14063d7cf
0063D7C2  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063D7C6  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0063D7CA  E8 01 D3 07 00                  call 0x1406baad0
0063D7CF  48 8B 1B                        mov rbx, qword ptr [rbx]
0063D7D2  48 3B DF                        cmp rbx, rdi
0063D7D5  75 E2                           jne 0x14063d7b9
0063D7D7  40 84 F6                        test sil, sil
0063D7DA  74 0C                           je 0x14063d7e8
0063D7DC  48 8D 0D 9D 66 8C 00            lea rcx, [rip + 0x8c669d]
0063D7E3  E8 98 C6 D0 FF                  call 0x140349e80
0063D7E8  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0063D7EC  45 8B CF                        mov r9d, r15d
0063D7EF  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0063D7F3  4D 8B C4                        mov r8, r12
0063D7F6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0063D7FB  41 8A D5                        mov dl, r13b
0063D7FE  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0063D802  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0063D807  E8 E4 00 07 00                  call 0x1406ad8f0
0063D80C  89 45 F8                        mov dword ptr [rbp - 8], eax
0063D80F  4D 85 F6                        test r14, r14
0063D812  74 63                           je 0x14063d877
0063D814  40 32 FF                        xor dil, dil
0063D817  40 38 3D 9A 70 8C 00            cmp byte ptr [rip + 0x8c709a], dil
0063D81E  75 0C                           jne 0x14063d82c
0063D820  F7 05 56 71 8C 00 00 08 00 00   test dword ptr [rip + 0x8c7156], 0x800
0063D82A  74 13                           je 0x14063d83f
0063D82C  48 8D 0D 4D 66 8C 00            lea rcx, [rip + 0x8c664d]
0063D833  E8 E8 8D BD FF                  call 0x140216620
0063D838  40 8A F8                        mov dil, al
0063D83B  84 C0                           test al, al
0063D83D  74 38                           je 0x14063d877
0063D83F  49 8D 76 30                     lea rsi, [r14 + 0x30]
0063D843  48 8B 1E                        mov rbx, qword ptr [rsi]
0063D846  EB 19                           jmp 0x14063d861
0063D848  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063D84C  48 85 C0                        test rax, rax
0063D84F  74 0D                           je 0x14063d85e
0063D851  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063D855  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0063D859  E8 72 D2 07 00                  call 0x1406baad0
0063D85E  48 8B 1B                        mov rbx, qword ptr [rbx]
0063D861  48 3B DE                        cmp rbx, rsi
0063D864  75 E2                           jne 0x14063d848
0063D866  40 84 FF                        test dil, dil
0063D869  74 0C                           je 0x14063d877
0063D86B  48 8D 0D 0E 66 8C 00            lea rcx, [rip + 0x8c660e]
0063D872  E8 09 C6 D0 FF                  call 0x140349e80
0063D877  8B 45 F8                        mov eax, dword ptr [rbp - 8]
0063D87A  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
0063D87F  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0063D883  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0063D887  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0063D88B  49 8B E3                        mov rsp, r11
0063D88E  41 5F                           pop r15
0063D890  41 5E                           pop r14
0063D892  41 5D                           pop r13
0063D894  41 5C                           pop r12
0063D896  5D                              pop rbp
0063D897  C3                              ret
0063D898  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwAdjustPrivilegesTokenWrapper(__int64 a1, int a2, __int64 a3, int a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int8 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (112);
    a2 = 0;
    result = memset(v_stack_m68, a2, a2 + 64, a4);
    result = DifGetAPIThunkContextById(145, a2, a2 + 64, a4);
    if (result == 0) goto loc_0063D7E8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063D753;
    v_stack_m68 = v_stack_p0;
    goto loc_0063D761;
loc_0063D753:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a2 + 64, a4);
        v_stack_m68 = result;
    }
    v_rsi = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m58 = a5;
    v_stack_m60 = a6;
    v_stack_m40 = (unsigned __int8)((unsigned __int8)(a2));
    v_stack_m48 = a3;
    v_stack_m50 = (unsigned int)((unsigned int)(a4));
    if ((*(unsigned __int8 *)(v_rip + 9204041)) != 0) goto loc_0063D79D;
    if (((*(unsigned int *)(v_rip + 9204197)) & (0x800ULL)) == 0) goto loc_0063D7B0;
loc_0063D79D:
    result = ExAcquireRundownProtection(v_rip + 9201372, a2, a2 + 64, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063D7E8;
loc_0063D7B0:
    goto loc_0063D7D2;
loc_0063D7B9:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a2 + 64, a4);
    }
loc_0063D7D2:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063D7B9;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9201309;
        result = ExReleaseRundownProtection(a1, a2, a2 + 64, a4);
    }
    v_stack_m70 = a6;
    v_stack_m78 = a5;
    result = ZwAdjustPrivilegesToken(v_stack_p8, (unsigned __int8)((unsigned __int8)(a2)), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_0063D877;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9203866)) != 0) goto loc_0063D82C;
    if (((*(unsigned int *)(v_rip + 9204054)) & (0x800ULL)) == 0) goto loc_0063D83F;
loc_0063D82C:
    result = ExAcquireRundownProtection(v_rip + 9201229, (unsigned __int8)((unsigned __int8)(a2)), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_0063D877;
loc_0063D83F:
    goto loc_0063D861;
loc_0063D848:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, (unsigned __int8)((unsigned __int8)(a2)), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_0063D861:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_0063D848;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9201166;
        result = ExReleaseRundownProtection(a1, (unsigned __int8)((unsigned __int8)(a2)), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwAdjustPrivilegesTokenWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint8_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (112);
    Arg2 = 0;
    result = memset(v_stack_m68, Arg2, Arg2 + 64, Arg4);
    result = DifGetAPIThunkContextById(145, Arg2, Arg2 + 64, Arg4);
    if (result == 0) goto loc_0063D7E8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063D753;
    v_stack_m68 = v_stack_p0;
    goto loc_0063D761;
loc_0063D753:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg2 + 64, Arg4);
        v_stack_m68 = result;
    }
    local_rsi = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m58 = Arg5;
    v_stack_m60 = Arg6;
    v_stack_m40 = (uint8_t)((uint8_t)(Arg2));
    v_stack_m48 = Arg3;
    v_stack_m50 = (uint32_t)((uint32_t)(Arg4));
    if ((*(uint8_t *)(v_rip + 0x8C7149)) != 0) goto loc_0063D79D;
    if (((*(uint32_t *)(v_rip + 0x8C71E5)) & (0x800ULL)) == 0) goto loc_0063D7B0;
loc_0063D79D:
    result = ExAcquireRundownProtection(v_rip + 9201372, Arg2, Arg2 + 64, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0063D7E8;
loc_0063D7B0:
    goto loc_0063D7D2;
loc_0063D7B9:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg2 + 64, Arg4);
    }
loc_0063D7D2:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063D7B9;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9201309;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg2 + 64, Arg4);
    }
    v_stack_m70 = Arg6;
    v_stack_m78 = Arg5;
    result = ZwAdjustPrivilegesToken(v_stack_p8, (uint8_t)((uint8_t)(Arg2)), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_0063D877;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C709A)) != 0) goto loc_0063D82C;
    if (((*(uint32_t *)(v_rip + 0x8C7156)) & (0x800ULL)) == 0) goto loc_0063D83F;
loc_0063D82C:
    result = ExAcquireRundownProtection(v_rip + 9201229, (uint8_t)((uint8_t)(Arg2)), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_0063D877;
loc_0063D83F:
    goto loc_0063D861;
loc_0063D848:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, (uint8_t)((uint8_t)(Arg2)), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_0063D861:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_0063D848;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9201166;
        result = ExReleaseRundownProtection(Arg1, (uint8_t)((uint8_t)(Arg2)), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063D6F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063D6F0[BB_0063D6F0]
  bb_0063D741[BB_0063D741]
  bb_0063D749[BB_0063D749]
  bb_0063D753[BB_0063D753]
  bb_0063D758[BB_0063D758]
  bb_0063D761[BB_0063D761]
  bb_0063D791[BB_0063D791]
  bb_0063D79D[BB_0063D79D]
  bb_0063D7B0[BB_0063D7B0]
  bb_0063D7B9[BB_0063D7B9]
  bb_0063D7C2[BB_0063D7C2]
  bb_0063D7CF[BB_0063D7CF]
  bb_0063D7D2[BB_0063D7D2]
  bb_0063D7D7[BB_0063D7D7]
  bb_0063D7DC[BB_0063D7DC]
  bb_0063D7E8[BB_0063D7E8]
  bb_0063D814[BB_0063D814]
  bb_0063D820[BB_0063D820]
  bb_0063D82C[BB_0063D82C]
  bb_0063D83F[BB_0063D83F]
  bb_0063D848[BB_0063D848]
  bb_0063D851[BB_0063D851]
  bb_0063D85E[BB_0063D85E]
  bb_0063D861[BB_0063D861]
  bb_0063D866[BB_0063D866]
  bb_0063D86B[BB_0063D86B]
  bb_0063D877[BB_0063D877]
  bb_0063D898[BB_0063D898]
  bb_0063D6F0 -->|branch| bb_0063D7E8
  bb_0063D6F0 -->|fallthrough| bb_0063D741
  bb_0063D741 -->|branch| bb_0063D753
  bb_0063D741 -->|fallthrough| bb_0063D749
  bb_0063D749 -->|branch| bb_0063D761
  bb_0063D753 -->|branch| bb_0063D761
  bb_0063D753 -->|fallthrough| bb_0063D758
  bb_0063D758 -->|flow| bb_0063D761
  bb_0063D761 -->|branch| bb_0063D79D
  bb_0063D761 -->|fallthrough| bb_0063D791
  bb_0063D791 -->|branch| bb_0063D7B0
  bb_0063D791 -->|fallthrough| bb_0063D79D
  bb_0063D79D -->|branch| bb_0063D7E8
  bb_0063D79D -->|fallthrough| bb_0063D7B0
  bb_0063D7B0 -->|branch| bb_0063D7D2
  bb_0063D7B9 -->|branch| bb_0063D7CF
  bb_0063D7B9 -->|fallthrough| bb_0063D7C2
  bb_0063D7C2 -->|flow| bb_0063D7CF
  bb_0063D7CF -->|flow| bb_0063D7D2
  bb_0063D7D2 -->|branch| bb_0063D7B9
  bb_0063D7D2 -->|fallthrough| bb_0063D7D7
  bb_0063D7D7 -->|branch| bb_0063D7E8
  bb_0063D7D7 -->|fallthrough| bb_0063D7DC
  bb_0063D7DC -->|flow| bb_0063D7E8
  bb_0063D7E8 -->|branch| bb_0063D877
  bb_0063D7E8 -->|fallthrough| bb_0063D814
  bb_0063D814 -->|branch| bb_0063D82C
  bb_0063D814 -->|fallthrough| bb_0063D820
  bb_0063D820 -->|branch| bb_0063D83F
  bb_0063D820 -->|fallthrough| bb_0063D82C
  bb_0063D82C -->|branch| bb_0063D877
  bb_0063D82C -->|fallthrough| bb_0063D83F
  bb_0063D83F -->|branch| bb_0063D861
  bb_0063D848 -->|branch| bb_0063D85E
  bb_0063D848 -->|fallthrough| bb_0063D851
  bb_0063D851 -->|flow| bb_0063D85E
  bb_0063D85E -->|flow| bb_0063D861
  bb_0063D861 -->|branch| bb_0063D848
  bb_0063D861 -->|fallthrough| bb_0063D866
  bb_0063D866 -->|branch| bb_0063D877
  bb_0063D866 -->|fallthrough| bb_0063D86B
  bb_0063D86B -->|flow| bb_0063D877
```
