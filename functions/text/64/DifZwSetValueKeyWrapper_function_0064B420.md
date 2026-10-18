# DifZwSetValueKeyWrapper

- RVA: `0x0064B420`–`0x0064B5C9` (길이 `425` bytes)
- VA: `0x000000014064B420`
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
- `0x0064B464` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0064B48C` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0064B4D6` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064B4FC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064B515` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0064B537` → [ZwSetValueKey](../6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x0064B563` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064B589` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064B5A2` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0064B49C` → RVA `0x00F048B8` (`.data`; read)
- `0x0064B4C3` → RVA `0x00F04980` (`.data`; read)
- `0x0064B4CF` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064B420  48 8B C4                        mov rax, rsp
0064B423  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0064B427  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064B42B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0064B42F  48 89 48 08                     mov qword ptr [rax + 8], rcx
0064B433  55                              push rbp
0064B434  41 54                           push r12
0064B436  41 55                           push r13
0064B438  41 56                           push r14
0064B43A  41 57                           push r15
0064B43C  48 8B EC                        mov rbp, rsp
0064B43F  48 83 EC 70                     sub rsp, 0x70
0064B443  33 C0                           xor eax, eax
0064B445  0F 57 C0                        xorps xmm0, xmm0
0064B448  45 8B F9                        mov r15d, r9d
0064B44B  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0064B44F  45 8B E0                        mov r12d, r8d
0064B452  4C 8B EA                        mov r13, rdx
0064B455  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
0064B459  8D 48 07                        lea ecx, [rax + 7]
0064B45C  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0064B460  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0064B464  E8 CB A5 E4 FF                  call 0x140495a34
0064B469  4C 8B F0                        mov r14, rax
0064B46C  48 85 C0                        test rax, rax
0064B46F  0F 84 A5 00 00 00               je 0x14064b51a
0064B475  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
0064B478  F6 C1 18                        test cl, 0x18
0064B47B  74 0A                           je 0x14064b487
0064B47D  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0064B481  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
0064B485  EB 0E                           jmp 0x14064b495
0064B487  F6 C1 04                        test cl, 4
0064B48A  74 09                           je 0x14064b495
0064B48C  E8 77 87 E8 FF                  call 0x1404d3c08
0064B491  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0064B495  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0064B499  40 32 F6                        xor sil, sil
0064B49C  40 38 35 15 94 8B 00            cmp byte ptr [rip + 0x8b9415], sil
0064B4A3  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0064B4A7  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0064B4AB  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0064B4AF  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
0064B4B2  89 45 C8                        mov dword ptr [rbp - 0x38], eax
0064B4B5  4C 89 6D E0                     mov qword ptr [rbp - 0x20], r13
0064B4B9  44 89 65 DC                     mov dword ptr [rbp - 0x24], r12d
0064B4BD  44 89 7D D8                     mov dword ptr [rbp - 0x28], r15d
0064B4C1  75 0C                           jne 0x14064b4cf
0064B4C3  F7 05 B3 94 8B 00 00 08 00 00   test dword ptr [rip + 0x8b94b3], 0x800
0064B4CD  74 13                           je 0x14064b4e2
0064B4CF  48 8D 0D AA 89 8B 00            lea rcx, [rip + 0x8b89aa]
0064B4D6  E8 45 B1 BC FF                  call 0x140216620
0064B4DB  40 8A F0                        mov sil, al
0064B4DE  84 C0                           test al, al
0064B4E0  74 38                           je 0x14064b51a
0064B4E2  49 8D 7E 20                     lea rdi, [r14 + 0x20]
0064B4E6  48 8B 1F                        mov rbx, qword ptr [rdi]
0064B4E9  EB 19                           jmp 0x14064b504
0064B4EB  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064B4EF  48 85 C0                        test rax, rax
0064B4F2  74 0D                           je 0x14064b501
0064B4F4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064B4F8  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0064B4FC  E8 CF F5 06 00                  call 0x1406baad0
0064B501  48 8B 1B                        mov rbx, qword ptr [rbx]
0064B504  48 3B DF                        cmp rbx, rdi
0064B507  75 E2                           jne 0x14064b4eb
0064B509  40 84 F6                        test sil, sil
0064B50C  74 0C                           je 0x14064b51a
0064B50E  48 8D 0D 6B 89 8B 00            lea rcx, [rip + 0x8b896b]
0064B515  E8 66 E9 CF FF                  call 0x140349e80
0064B51A  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
0064B51D  45 8B CF                        mov r9d, r15d
0064B520  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0064B524  45 8B C4                        mov r8d, r12d
0064B527  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0064B52B  49 8B D5                        mov rdx, r13
0064B52E  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0064B532  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0064B537  E8 94 27 06 00                  call 0x1406adcd0
0064B53C  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0064B53F  4D 85 F6                        test r14, r14
0064B542  74 63                           je 0x14064b5a7
0064B544  40 32 FF                        xor dil, dil
0064B547  40 38 3D 6A 93 8B 00            cmp byte ptr [rip + 0x8b936a], dil
0064B54E  75 0C                           jne 0x14064b55c
0064B550  F7 05 26 94 8B 00 00 08 00 00   test dword ptr [rip + 0x8b9426], 0x800
0064B55A  74 13                           je 0x14064b56f
0064B55C  48 8D 0D 1D 89 8B 00            lea rcx, [rip + 0x8b891d]
0064B563  E8 B8 B0 BC FF                  call 0x140216620
0064B568  40 8A F8                        mov dil, al
0064B56B  84 C0                           test al, al
0064B56D  74 38                           je 0x14064b5a7
0064B56F  49 8D 76 30                     lea rsi, [r14 + 0x30]
0064B573  48 8B 1E                        mov rbx, qword ptr [rsi]
0064B576  EB 19                           jmp 0x14064b591
0064B578  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064B57C  48 85 C0                        test rax, rax
0064B57F  74 0D                           je 0x14064b58e
0064B581  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064B585  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0064B589  E8 42 F5 06 00                  call 0x1406baad0
0064B58E  48 8B 1B                        mov rbx, qword ptr [rbx]
0064B591  48 3B DE                        cmp rbx, rsi
0064B594  75 E2                           jne 0x14064b578
0064B596  40 84 FF                        test dil, dil
0064B599  74 0C                           je 0x14064b5a7
0064B59B  48 8D 0D DE 88 8B 00            lea rcx, [rip + 0x8b88de]
0064B5A2  E8 D9 E8 CF FF                  call 0x140349e80
0064B5A7  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0064B5AA  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
0064B5AF  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0064B5B3  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0064B5B7  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0064B5BB  49 8B E3                        mov rsp, r11
0064B5BE  41 5F                           pop r15
0064B5C0  41 5E                           pop r14
0064B5C2  41 5D                           pop r13
0064B5C4  41 5C                           pop r12
0064B5C6  5D                              pop rbp
0064B5C7  C3                              ret
0064B5C8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwSetValueKeyWrapper(__int64 a1, __int64 a2, int a3, int a4, __int64 a5, unsigned int a6)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
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
    result = DifGetAPIThunkContextById(result + 7, a2, a3, a4);
    if (result == 0) goto loc_0064B51A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0064B487;
    v_stack_m68 = v_stack_p0;
    goto loc_0064B495;
loc_0064B487:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m68 = result;
    }
    v_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m58 = a5;
    v_stack_m60 = (unsigned int)((unsigned int)(a6));
    v_stack_m48 = a2;
    v_stack_m4C = (unsigned int)((unsigned int)(a3));
    v_stack_m50 = (unsigned int)((unsigned int)(a4));
    if ((*(unsigned __int8 *)(v_rip + 9147413)) != 0) goto loc_0064B4CF;
    if (((*(unsigned int *)(v_rip + 9147571)) & (0x800ULL)) == 0) goto loc_0064B4E2;
loc_0064B4CF:
    result = ExAcquireRundownProtection(v_rip + 9144746, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064B51A;
loc_0064B4E2:
    goto loc_0064B504;
loc_0064B4EB:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0064B504:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0064B4EB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9144683;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m70 = (unsigned int)((unsigned int)(a6));
    v_stack_m78 = a5;
    result = ZwSetValueKey(v_stack_p8, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0064B5A7;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9147242)) != 0) goto loc_0064B55C;
    if (((*(unsigned int *)(v_rip + 9147430)) & (0x800ULL)) == 0) goto loc_0064B56F;
loc_0064B55C:
    result = ExAcquireRundownProtection(v_rip + 9144605, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_0064B5A7;
loc_0064B56F:
    goto loc_0064B591;
loc_0064B578:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_0064B591:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_0064B578;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9144542;
        result = ExReleaseRundownProtection(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwSetValueKeyWrapper(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, int64_t Arg5, uint32_t Arg6)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
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
    result = DifGetAPIThunkContextById(result + 7, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0064B51A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0064B487;
    v_stack_m68 = v_stack_p0;
    goto loc_0064B495;
loc_0064B487:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m68 = result;
    }
    local_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m58 = Arg5;
    v_stack_m60 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m48 = Arg2;
    v_stack_m4C = (uint32_t)((uint32_t)(Arg3));
    v_stack_m50 = (uint32_t)((uint32_t)(Arg4));
    if ((*(uint8_t *)(v_rip + 0x8B9415)) != 0) goto loc_0064B4CF;
    if (((*(uint32_t *)(v_rip + 0x8B94B3)) & (0x800ULL)) == 0) goto loc_0064B4E2;
loc_0064B4CF:
    result = ExAcquireRundownProtection(v_rip + 9144746, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0064B51A;
loc_0064B4E2:
    goto loc_0064B504;
loc_0064B4EB:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0064B504:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0064B4EB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9144683;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m70 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m78 = Arg5;
    result = ZwSetValueKey(v_stack_p8, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0064B5A7;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8B936A)) != 0) goto loc_0064B55C;
    if (((*(uint32_t *)(v_rip + 0x8B9426)) & (0x800ULL)) == 0) goto loc_0064B56F;
loc_0064B55C:
    result = ExAcquireRundownProtection(v_rip + 9144605, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_0064B5A7;
loc_0064B56F:
    goto loc_0064B591;
loc_0064B578:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_0064B591:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_0064B578;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9144542;
        result = ExReleaseRundownProtection(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064B420&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0064B420[BB_0064B420]
  bb_0064B475[BB_0064B475]
  bb_0064B47D[BB_0064B47D]
  bb_0064B487[BB_0064B487]
  bb_0064B48C[BB_0064B48C]
  bb_0064B495[BB_0064B495]
  bb_0064B4C3[BB_0064B4C3]
  bb_0064B4CF[BB_0064B4CF]
  bb_0064B4E2[BB_0064B4E2]
  bb_0064B4EB[BB_0064B4EB]
  bb_0064B4F4[BB_0064B4F4]
  bb_0064B501[BB_0064B501]
  bb_0064B504[BB_0064B504]
  bb_0064B509[BB_0064B509]
  bb_0064B50E[BB_0064B50E]
  bb_0064B51A[BB_0064B51A]
  bb_0064B544[BB_0064B544]
  bb_0064B550[BB_0064B550]
  bb_0064B55C[BB_0064B55C]
  bb_0064B56F[BB_0064B56F]
  bb_0064B578[BB_0064B578]
  bb_0064B581[BB_0064B581]
  bb_0064B58E[BB_0064B58E]
  bb_0064B591[BB_0064B591]
  bb_0064B596[BB_0064B596]
  bb_0064B59B[BB_0064B59B]
  bb_0064B5A7[BB_0064B5A7]
  bb_0064B5C8[BB_0064B5C8]
  bb_0064B420 -->|branch| bb_0064B51A
  bb_0064B420 -->|fallthrough| bb_0064B475
  bb_0064B475 -->|branch| bb_0064B487
  bb_0064B475 -->|fallthrough| bb_0064B47D
  bb_0064B47D -->|branch| bb_0064B495
  bb_0064B487 -->|branch| bb_0064B495
  bb_0064B487 -->|fallthrough| bb_0064B48C
  bb_0064B48C -->|flow| bb_0064B495
  bb_0064B495 -->|branch| bb_0064B4CF
  bb_0064B495 -->|fallthrough| bb_0064B4C3
  bb_0064B4C3 -->|branch| bb_0064B4E2
  bb_0064B4C3 -->|fallthrough| bb_0064B4CF
  bb_0064B4CF -->|branch| bb_0064B51A
  bb_0064B4CF -->|fallthrough| bb_0064B4E2
  bb_0064B4E2 -->|branch| bb_0064B504
  bb_0064B4EB -->|branch| bb_0064B501
  bb_0064B4EB -->|fallthrough| bb_0064B4F4
  bb_0064B4F4 -->|flow| bb_0064B501
  bb_0064B501 -->|flow| bb_0064B504
  bb_0064B504 -->|branch| bb_0064B4EB
  bb_0064B504 -->|fallthrough| bb_0064B509
  bb_0064B509 -->|branch| bb_0064B51A
  bb_0064B509 -->|fallthrough| bb_0064B50E
  bb_0064B50E -->|flow| bb_0064B51A
  bb_0064B51A -->|branch| bb_0064B5A7
  bb_0064B51A -->|fallthrough| bb_0064B544
  bb_0064B544 -->|branch| bb_0064B55C
  bb_0064B544 -->|fallthrough| bb_0064B550
  bb_0064B550 -->|branch| bb_0064B56F
  bb_0064B550 -->|fallthrough| bb_0064B55C
  bb_0064B55C -->|branch| bb_0064B5A7
  bb_0064B55C -->|fallthrough| bb_0064B56F
  bb_0064B56F -->|branch| bb_0064B591
  bb_0064B578 -->|branch| bb_0064B58E
  bb_0064B578 -->|fallthrough| bb_0064B581
  bb_0064B581 -->|flow| bb_0064B58E
  bb_0064B58E -->|flow| bb_0064B591
  bb_0064B591 -->|branch| bb_0064B578
  bb_0064B591 -->|fallthrough| bb_0064B596
  bb_0064B596 -->|branch| bb_0064B5A7
  bb_0064B596 -->|fallthrough| bb_0064B59B
  bb_0064B59B -->|flow| bb_0064B5A7
```
