# DifZwEnumerateKeyWrapper

- RVA: `0x006419F0`–`0x00641B99` (길이 `425` bytes)
- VA: `0x00000001406419F0`
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
- `0x00641A34` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00641A5C` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00641AA6` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00641ACC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00641AE5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00641B07` → [ZwEnumerateKey](../6A/ZwEnumerateKey_function_006AD710.md) (function, `0x006AD710`)
- `0x00641B33` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00641B59` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00641B72` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00641A6C` → RVA `0x00F048B8` (`.data`; read)
- `0x00641A93` → RVA `0x00F04980` (`.data`; read)
- `0x00641A9F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006419F0  48 8B C4                        mov rax, rsp
006419F3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
006419F7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006419FB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
006419FF  48 89 48 08                     mov qword ptr [rax + 8], rcx
00641A03  55                              push rbp
00641A04  41 54                           push r12
00641A06  41 55                           push r13
00641A08  41 56                           push r14
00641A0A  41 57                           push r15
00641A0C  48 8B EC                        mov rbp, rsp
00641A0F  48 83 EC 70                     sub rsp, 0x70
00641A13  33 C0                           xor eax, eax
00641A15  0F 57 C0                        xorps xmm0, xmm0
00641A18  4D 8B F9                        mov r15, r9
00641A1B  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00641A1F  45 8B E0                        mov r12d, r8d
00641A22  44 8B EA                        mov r13d, edx
00641A25  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00641A29  8D 48 68                        lea ecx, [rax + 0x68]
00641A2C  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00641A30  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00641A34  E8 FB 3F E5 FF                  call 0x140495a34
00641A39  4C 8B F0                        mov r14, rax
00641A3C  48 85 C0                        test rax, rax
00641A3F  0F 84 A5 00 00 00               je 0x140641aea
00641A45  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00641A48  F6 C1 18                        test cl, 0x18
00641A4B  74 0A                           je 0x140641a57
00641A4D  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00641A51  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00641A55  EB 0E                           jmp 0x140641a65
00641A57  F6 C1 04                        test cl, 4
00641A5A  74 09                           je 0x140641a65
00641A5C  E8 A7 21 E9 FF                  call 0x1404d3c08
00641A61  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00641A65  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00641A69  40 32 F6                        xor sil, sil
00641A6C  40 38 35 45 2E 8C 00            cmp byte ptr [rip + 0x8c2e45], sil
00641A73  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00641A77  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00641A7A  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00641A7D  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00641A81  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00641A85  44 89 6D E4                     mov dword ptr [rbp - 0x1c], r13d
00641A89  44 89 65 E0                     mov dword ptr [rbp - 0x20], r12d
00641A8D  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
00641A91  75 0C                           jne 0x140641a9f
00641A93  F7 05 E3 2E 8C 00 00 08 00 00   test dword ptr [rip + 0x8c2ee3], 0x800
00641A9D  74 13                           je 0x140641ab2
00641A9F  48 8D 0D DA 23 8C 00            lea rcx, [rip + 0x8c23da]
00641AA6  E8 75 4B BD FF                  call 0x140216620
00641AAB  40 8A F0                        mov sil, al
00641AAE  84 C0                           test al, al
00641AB0  74 38                           je 0x140641aea
00641AB2  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00641AB6  48 8B 1F                        mov rbx, qword ptr [rdi]
00641AB9  EB 19                           jmp 0x140641ad4
00641ABB  48 8D 43 F0                     lea rax, [rbx - 0x10]
00641ABF  48 85 C0                        test rax, rax
00641AC2  74 0D                           je 0x140641ad1
00641AC4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00641AC8  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00641ACC  E8 FF 8F 07 00                  call 0x1406baad0
00641AD1  48 8B 1B                        mov rbx, qword ptr [rbx]
00641AD4  48 3B DF                        cmp rbx, rdi
00641AD7  75 E2                           jne 0x140641abb
00641AD9  40 84 F6                        test sil, sil
00641ADC  74 0C                           je 0x140641aea
00641ADE  48 8D 0D 9B 23 8C 00            lea rcx, [rip + 0x8c239b]
00641AE5  E8 96 83 D0 FF                  call 0x140349e80
00641AEA  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00641AEE  4D 8B CF                        mov r9, r15
00641AF1  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00641AF5  45 8B C4                        mov r8d, r12d
00641AF8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00641AFD  41 8B D5                        mov edx, r13d
00641B00  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00641B03  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00641B07  E8 04 BC 06 00                  call 0x1406ad710
00641B0C  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00641B0F  4D 85 F6                        test r14, r14
00641B12  74 63                           je 0x140641b77
00641B14  40 32 FF                        xor dil, dil
00641B17  40 38 3D 9A 2D 8C 00            cmp byte ptr [rip + 0x8c2d9a], dil
00641B1E  75 0C                           jne 0x140641b2c
00641B20  F7 05 56 2E 8C 00 00 08 00 00   test dword ptr [rip + 0x8c2e56], 0x800
00641B2A  74 13                           je 0x140641b3f
00641B2C  48 8D 0D 4D 23 8C 00            lea rcx, [rip + 0x8c234d]
00641B33  E8 E8 4A BD FF                  call 0x140216620
00641B38  40 8A F8                        mov dil, al
00641B3B  84 C0                           test al, al
00641B3D  74 38                           je 0x140641b77
00641B3F  49 8D 76 30                     lea rsi, [r14 + 0x30]
00641B43  48 8B 1E                        mov rbx, qword ptr [rsi]
00641B46  EB 19                           jmp 0x140641b61
00641B48  48 8D 43 F0                     lea rax, [rbx - 0x10]
00641B4C  48 85 C0                        test rax, rax
00641B4F  74 0D                           je 0x140641b5e
00641B51  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00641B55  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00641B59  E8 72 8F 07 00                  call 0x1406baad0
00641B5E  48 8B 1B                        mov rbx, qword ptr [rbx]
00641B61  48 3B DE                        cmp rbx, rsi
00641B64  75 E2                           jne 0x140641b48
00641B66  40 84 FF                        test dil, dil
00641B69  74 0C                           je 0x140641b77
00641B6B  48 8D 0D 0E 23 8C 00            lea rcx, [rip + 0x8c230e]
00641B72  E8 09 83 D0 FF                  call 0x140349e80
00641B77  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00641B7A  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00641B7F  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00641B83  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00641B87  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00641B8B  49 8B E3                        mov rsp, r11
00641B8E  41 5F                           pop r15
00641B90  41 5E                           pop r14
00641B92  41 5D                           pop r13
00641B94  41 5C                           pop r12
00641B96  5D                              pop rbp
00641B97  C3                              ret
00641B98  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwEnumerateKeyWrapper(__int64 a1, int a2, int a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m44;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
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
    result = DifGetAPIThunkContextById(result + 104, a2, a3, a4);
    if (result == 0) goto loc_00641AEA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00641A57;
    v_stack_m68 = v_stack_p0;
    goto loc_00641A65;
loc_00641A57:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m68 = result;
    }
    v_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m58 = (unsigned int)((unsigned int)(a5));
    v_stack_m60 = a6;
    v_stack_m44 = (unsigned int)((unsigned int)(a2));
    v_stack_m48 = (unsigned int)((unsigned int)(a3));
    v_stack_m50 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9186885)) != 0) goto loc_00641A9F;
    if (((*(unsigned int *)(v_rip + 9187043)) & (0x800ULL)) == 0) goto loc_00641AB2;
loc_00641A9F:
    result = ExAcquireRundownProtection(v_rip + 9184218, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00641AEA;
loc_00641AB2:
    goto loc_00641AD4;
loc_00641ABB:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00641AD4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00641ABB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9184155;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m70 = a6;
    v_stack_m78 = (unsigned int)((unsigned int)(a5));
    result = ZwEnumerateKey(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_00641B77;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9186714)) != 0) goto loc_00641B2C;
    if (((*(unsigned int *)(v_rip + 9186902)) & (0x800ULL)) == 0) goto loc_00641B3F;
loc_00641B2C:
    result = ExAcquireRundownProtection(v_rip + 9184077, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00641B77;
loc_00641B3F:
    goto loc_00641B61;
loc_00641B48:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_00641B61:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_00641B48;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9184014;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwEnumerateKeyWrapper(int64_t Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m44;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
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
    result = DifGetAPIThunkContextById(result + 104, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00641AEA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00641A57;
    v_stack_m68 = v_stack_p0;
    goto loc_00641A65;
loc_00641A57:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m68 = result;
    }
    local_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m58 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m60 = Arg6;
    v_stack_m44 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m48 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m50 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8C2E45)) != 0) goto loc_00641A9F;
    if (((*(uint32_t *)(v_rip + 0x8C2EE3)) & (0x800ULL)) == 0) goto loc_00641AB2;
loc_00641A9F:
    result = ExAcquireRundownProtection(v_rip + 9184218, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00641AEA;
loc_00641AB2:
    goto loc_00641AD4;
loc_00641ABB:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00641AD4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00641ABB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9184155;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m70 = Arg6;
    v_stack_m78 = (uint32_t)((uint32_t)(Arg5));
    result = ZwEnumerateKey(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_00641B77;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C2D9A)) != 0) goto loc_00641B2C;
    if (((*(uint32_t *)(v_rip + 0x8C2E56)) & (0x800ULL)) == 0) goto loc_00641B3F;
loc_00641B2C:
    result = ExAcquireRundownProtection(v_rip + 9184077, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00641B77;
loc_00641B3F:
    goto loc_00641B61;
loc_00641B48:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
loc_00641B61:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_00641B48;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9184014;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006419F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006419F0[BB_006419F0]
  bb_00641A45[BB_00641A45]
  bb_00641A4D[BB_00641A4D]
  bb_00641A57[BB_00641A57]
  bb_00641A5C[BB_00641A5C]
  bb_00641A65[BB_00641A65]
  bb_00641A93[BB_00641A93]
  bb_00641A9F[BB_00641A9F]
  bb_00641AB2[BB_00641AB2]
  bb_00641ABB[BB_00641ABB]
  bb_00641AC4[BB_00641AC4]
  bb_00641AD1[BB_00641AD1]
  bb_00641AD4[BB_00641AD4]
  bb_00641AD9[BB_00641AD9]
  bb_00641ADE[BB_00641ADE]
  bb_00641AEA[BB_00641AEA]
  bb_00641B14[BB_00641B14]
  bb_00641B20[BB_00641B20]
  bb_00641B2C[BB_00641B2C]
  bb_00641B3F[BB_00641B3F]
  bb_00641B48[BB_00641B48]
  bb_00641B51[BB_00641B51]
  bb_00641B5E[BB_00641B5E]
  bb_00641B61[BB_00641B61]
  bb_00641B66[BB_00641B66]
  bb_00641B6B[BB_00641B6B]
  bb_00641B77[BB_00641B77]
  bb_00641B98[BB_00641B98]
  bb_006419F0 -->|branch| bb_00641AEA
  bb_006419F0 -->|fallthrough| bb_00641A45
  bb_00641A45 -->|branch| bb_00641A57
  bb_00641A45 -->|fallthrough| bb_00641A4D
  bb_00641A4D -->|branch| bb_00641A65
  bb_00641A57 -->|branch| bb_00641A65
  bb_00641A57 -->|fallthrough| bb_00641A5C
  bb_00641A5C -->|flow| bb_00641A65
  bb_00641A65 -->|branch| bb_00641A9F
  bb_00641A65 -->|fallthrough| bb_00641A93
  bb_00641A93 -->|branch| bb_00641AB2
  bb_00641A93 -->|fallthrough| bb_00641A9F
  bb_00641A9F -->|branch| bb_00641AEA
  bb_00641A9F -->|fallthrough| bb_00641AB2
  bb_00641AB2 -->|branch| bb_00641AD4
  bb_00641ABB -->|branch| bb_00641AD1
  bb_00641ABB -->|fallthrough| bb_00641AC4
  bb_00641AC4 -->|flow| bb_00641AD1
  bb_00641AD1 -->|flow| bb_00641AD4
  bb_00641AD4 -->|branch| bb_00641ABB
  bb_00641AD4 -->|fallthrough| bb_00641AD9
  bb_00641AD9 -->|branch| bb_00641AEA
  bb_00641AD9 -->|fallthrough| bb_00641ADE
  bb_00641ADE -->|flow| bb_00641AEA
  bb_00641AEA -->|branch| bb_00641B77
  bb_00641AEA -->|fallthrough| bb_00641B14
  bb_00641B14 -->|branch| bb_00641B2C
  bb_00641B14 -->|fallthrough| bb_00641B20
  bb_00641B20 -->|branch| bb_00641B3F
  bb_00641B20 -->|fallthrough| bb_00641B2C
  bb_00641B2C -->|branch| bb_00641B77
  bb_00641B2C -->|fallthrough| bb_00641B3F
  bb_00641B3F -->|branch| bb_00641B61
  bb_00641B48 -->|branch| bb_00641B5E
  bb_00641B48 -->|fallthrough| bb_00641B51
  bb_00641B51 -->|flow| bb_00641B5E
  bb_00641B5E -->|flow| bb_00641B61
  bb_00641B61 -->|branch| bb_00641B48
  bb_00641B61 -->|fallthrough| bb_00641B66
  bb_00641B66 -->|branch| bb_00641B77
  bb_00641B66 -->|fallthrough| bb_00641B6B
  bb_00641B6B -->|flow| bb_00641B77
```
