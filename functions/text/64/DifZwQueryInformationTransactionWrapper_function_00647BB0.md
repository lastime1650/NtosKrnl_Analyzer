# DifZwQueryInformationTransactionWrapper

- RVA: `0x00647BB0`–`0x00647D4C` (길이 `412` bytes)
- VA: `0x0000000140647BB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD780`
- 디코드: `118`개 명령, `412/412` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00647BF4` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00647C1C` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00647C60` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00647C86` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00647C9F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00647CBA` → [ZwQueryInformationTransaction](../6A/ZwQueryInformationTransaction_function_006AFC10.md) (function, `0x006AFC10`)
- `0x00647CE6` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00647D0C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00647D25` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00647C2C` → RVA `0x00F048B8` (`.data`; read)
- `0x00647C4D` → RVA `0x00F04980` (`.data`; read)
- `0x00647C59` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00647BB0  48 8B C4                        mov rax, rsp
00647BB3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00647BB7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00647BBB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00647BBF  48 89 48 08                     mov qword ptr [rax + 8], rcx
00647BC3  55                              push rbp
00647BC4  41 54                           push r12
00647BC6  41 55                           push r13
00647BC8  41 56                           push r14
00647BCA  41 57                           push r15
00647BCC  48 8B EC                        mov rbp, rsp
00647BCF  48 83 EC 70                     sub rsp, 0x70
00647BD3  33 C0                           xor eax, eax
00647BD5  0F 57 C0                        xorps xmm0, xmm0
00647BD8  45 8B F9                        mov r15d, r9d
00647BDB  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00647BDF  4D 8B E0                        mov r12, r8
00647BE2  44 8B EA                        mov r13d, edx
00647BE5  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00647BE9  8D 48 2C                        lea ecx, [rax + 0x2c]
00647BEC  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00647BF0  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00647BF4  E8 3B DE E4 FF                  call 0x140495a34
00647BF9  4C 8B F0                        mov r14, rax
00647BFC  48 85 C0                        test rax, rax
00647BFF  0F 84 9F 00 00 00               je 0x140647ca4
00647C05  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00647C08  F6 C1 18                        test cl, 0x18
00647C0B  74 0A                           je 0x140647c17
00647C0D  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00647C11  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00647C15  EB 0E                           jmp 0x140647c25
00647C17  F6 C1 04                        test cl, 4
00647C1A  74 09                           je 0x140647c25
00647C1C  E8 E7 BF E8 FF                  call 0x1404d3c08
00647C21  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00647C25  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00647C29  40 32 F6                        xor sil, sil
00647C2C  40 38 35 85 CC 8B 00            cmp byte ptr [rip + 0x8bcc85], sil
00647C33  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00647C37  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00647C3B  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00647C3F  44 89 6D E0                     mov dword ptr [rbp - 0x20], r13d
00647C43  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
00647C47  44 89 7D D0                     mov dword ptr [rbp - 0x30], r15d
00647C4B  75 0C                           jne 0x140647c59
00647C4D  F7 05 29 CD 8B 00 00 08 00 00   test dword ptr [rip + 0x8bcd29], 0x800
00647C57  74 13                           je 0x140647c6c
00647C59  48 8D 0D 20 C2 8B 00            lea rcx, [rip + 0x8bc220]
00647C60  E8 BB E9 BC FF                  call 0x140216620
00647C65  40 8A F0                        mov sil, al
00647C68  84 C0                           test al, al
00647C6A  74 38                           je 0x140647ca4
00647C6C  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00647C70  48 8B 1F                        mov rbx, qword ptr [rdi]
00647C73  EB 19                           jmp 0x140647c8e
00647C75  48 8D 43 F0                     lea rax, [rbx - 0x10]
00647C79  48 85 C0                        test rax, rax
00647C7C  74 0D                           je 0x140647c8b
00647C7E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00647C82  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00647C86  E8 45 2E 07 00                  call 0x1406baad0
00647C8B  48 8B 1B                        mov rbx, qword ptr [rbx]
00647C8E  48 3B DF                        cmp rbx, rdi
00647C91  75 E2                           jne 0x140647c75
00647C93  40 84 F6                        test sil, sil
00647C96  74 0C                           je 0x140647ca4
00647C98  48 8D 0D E1 C1 8B 00            lea rcx, [rip + 0x8bc1e1]
00647C9F  E8 DC 21 D0 FF                  call 0x140349e80
00647CA4  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00647CA8  45 8B CF                        mov r9d, r15d
00647CAB  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00647CAF  4D 8B C4                        mov r8, r12
00647CB2  41 8B D5                        mov edx, r13d
00647CB5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00647CBA  E8 51 7F 06 00                  call 0x1406afc10
00647CBF  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00647CC2  4D 85 F6                        test r14, r14
00647CC5  74 63                           je 0x140647d2a
00647CC7  40 32 FF                        xor dil, dil
00647CCA  40 38 3D E7 CB 8B 00            cmp byte ptr [rip + 0x8bcbe7], dil
00647CD1  75 0C                           jne 0x140647cdf
00647CD3  F7 05 A3 CC 8B 00 00 08 00 00   test dword ptr [rip + 0x8bcca3], 0x800
00647CDD  74 13                           je 0x140647cf2
00647CDF  48 8D 0D 9A C1 8B 00            lea rcx, [rip + 0x8bc19a]
00647CE6  E8 35 E9 BC FF                  call 0x140216620
00647CEB  40 8A F8                        mov dil, al
00647CEE  84 C0                           test al, al
00647CF0  74 38                           je 0x140647d2a
00647CF2  49 8D 76 30                     lea rsi, [r14 + 0x30]
00647CF6  48 8B 1E                        mov rbx, qword ptr [rsi]
00647CF9  EB 19                           jmp 0x140647d14
00647CFB  48 8D 43 F0                     lea rax, [rbx - 0x10]
00647CFF  48 85 C0                        test rax, rax
00647D02  74 0D                           je 0x140647d11
00647D04  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00647D08  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00647D0C  E8 BF 2D 07 00                  call 0x1406baad0
00647D11  48 8B 1B                        mov rbx, qword ptr [rbx]
00647D14  48 3B DE                        cmp rbx, rsi
00647D17  75 E2                           jne 0x140647cfb
00647D19  40 84 FF                        test dil, dil
00647D1C  74 0C                           je 0x140647d2a
00647D1E  48 8D 0D 5B C1 8B 00            lea rcx, [rip + 0x8bc15b]
00647D25  E8 56 21 D0 FF                  call 0x140349e80
00647D2A  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00647D2D  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00647D32  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00647D36  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00647D3A  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00647D3E  49 8B E3                        mov rsp, r11
00647D41  41 5F                           pop r15
00647D43  41 5E                           pop r14
00647D45  41 5D                           pop r13
00647D47  41 5C                           pop r12
00647D49  5D                              pop rbp
00647D4A  C3                              ret
00647D4B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwQueryInformationTransactionWrapper(__int64 a1, int a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
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
    result = DifGetAPIThunkContextById(result + 44, a2, a3, a4);
    if (result == 0) goto loc_00647CA4;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00647C17;
    v_stack_m68 = v_stack_p0;
    goto loc_00647C25;
loc_00647C17:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m68 = result;
    }
    v_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m60 = a5;
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    v_stack_m50 = a3;
    v_stack_m58 = (unsigned int)((unsigned int)(a4));
    if ((*(unsigned __int8 *)(v_rip + 9161861)) != 0) goto loc_00647C59;
    if (((*(unsigned int *)(v_rip + 9162025)) & (0x800ULL)) == 0) goto loc_00647C6C;
loc_00647C59:
    result = ExAcquireRundownProtection(v_rip + 9159200, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00647CA4;
loc_00647C6C:
    goto loc_00647C8E;
loc_00647C75:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00647C8E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00647C75;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9159137;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m78 = a5;
    result = ZwQueryInformationTransaction(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_00647D2A;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9161703)) != 0) goto loc_00647CDF;
    if (((*(unsigned int *)(v_rip + 9161891)) & (0x800ULL)) == 0) goto loc_00647CF2;
loc_00647CDF:
    result = ExAcquireRundownProtection(v_rip + 9159066, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_00647D2A;
loc_00647CF2:
    goto loc_00647D14;
loc_00647CFB:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_00647D14:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_00647CFB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9159003;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwQueryInformationTransactionWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
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
    result = DifGetAPIThunkContextById(result + 44, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00647CA4;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00647C17;
    v_stack_m68 = v_stack_p0;
    goto loc_00647C25;
loc_00647C17:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m68 = result;
    }
    local_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m60 = Arg5;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m50 = Arg3;
    v_stack_m58 = (uint32_t)((uint32_t)(Arg4));
    if ((*(uint8_t *)(v_rip + 0x8BCC85)) != 0) goto loc_00647C59;
    if (((*(uint32_t *)(v_rip + 0x8BCD29)) & (0x800ULL)) == 0) goto loc_00647C6C;
loc_00647C59:
    result = ExAcquireRundownProtection(v_rip + 9159200, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00647CA4;
loc_00647C6C:
    goto loc_00647C8E;
loc_00647C75:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00647C8E:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00647C75;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9159137;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m78 = Arg5;
    result = ZwQueryInformationTransaction(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_00647D2A;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BCBE7)) != 0) goto loc_00647CDF;
    if (((*(uint32_t *)(v_rip + 0x8BCCA3)) & (0x800ULL)) == 0) goto loc_00647CF2;
loc_00647CDF:
    result = ExAcquireRundownProtection(v_rip + 9159066, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_00647D2A;
loc_00647CF2:
    goto loc_00647D14;
loc_00647CFB:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_00647D14:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_00647CFB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9159003;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00647BB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00647BB0[BB_00647BB0]
  bb_00647C05[BB_00647C05]
  bb_00647C0D[BB_00647C0D]
  bb_00647C17[BB_00647C17]
  bb_00647C1C[BB_00647C1C]
  bb_00647C25[BB_00647C25]
  bb_00647C4D[BB_00647C4D]
  bb_00647C59[BB_00647C59]
  bb_00647C6C[BB_00647C6C]
  bb_00647C75[BB_00647C75]
  bb_00647C7E[BB_00647C7E]
  bb_00647C8B[BB_00647C8B]
  bb_00647C8E[BB_00647C8E]
  bb_00647C93[BB_00647C93]
  bb_00647C98[BB_00647C98]
  bb_00647CA4[BB_00647CA4]
  bb_00647CC7[BB_00647CC7]
  bb_00647CD3[BB_00647CD3]
  bb_00647CDF[BB_00647CDF]
  bb_00647CF2[BB_00647CF2]
  bb_00647CFB[BB_00647CFB]
  bb_00647D04[BB_00647D04]
  bb_00647D11[BB_00647D11]
  bb_00647D14[BB_00647D14]
  bb_00647D19[BB_00647D19]
  bb_00647D1E[BB_00647D1E]
  bb_00647D2A[BB_00647D2A]
  bb_00647D4B[BB_00647D4B]
  bb_00647BB0 -->|branch| bb_00647CA4
  bb_00647BB0 -->|fallthrough| bb_00647C05
  bb_00647C05 -->|branch| bb_00647C17
  bb_00647C05 -->|fallthrough| bb_00647C0D
  bb_00647C0D -->|branch| bb_00647C25
  bb_00647C17 -->|branch| bb_00647C25
  bb_00647C17 -->|fallthrough| bb_00647C1C
  bb_00647C1C -->|flow| bb_00647C25
  bb_00647C25 -->|branch| bb_00647C59
  bb_00647C25 -->|fallthrough| bb_00647C4D
  bb_00647C4D -->|branch| bb_00647C6C
  bb_00647C4D -->|fallthrough| bb_00647C59
  bb_00647C59 -->|branch| bb_00647CA4
  bb_00647C59 -->|fallthrough| bb_00647C6C
  bb_00647C6C -->|branch| bb_00647C8E
  bb_00647C75 -->|branch| bb_00647C8B
  bb_00647C75 -->|fallthrough| bb_00647C7E
  bb_00647C7E -->|flow| bb_00647C8B
  bb_00647C8B -->|flow| bb_00647C8E
  bb_00647C8E -->|branch| bb_00647C75
  bb_00647C8E -->|fallthrough| bb_00647C93
  bb_00647C93 -->|branch| bb_00647CA4
  bb_00647C93 -->|fallthrough| bb_00647C98
  bb_00647C98 -->|flow| bb_00647CA4
  bb_00647CA4 -->|branch| bb_00647D2A
  bb_00647CA4 -->|fallthrough| bb_00647CC7
  bb_00647CC7 -->|branch| bb_00647CDF
  bb_00647CC7 -->|fallthrough| bb_00647CD3
  bb_00647CD3 -->|branch| bb_00647CF2
  bb_00647CD3 -->|fallthrough| bb_00647CDF
  bb_00647CDF -->|branch| bb_00647D2A
  bb_00647CDF -->|fallthrough| bb_00647CF2
  bb_00647CF2 -->|branch| bb_00647D14
  bb_00647CFB -->|branch| bb_00647D11
  bb_00647CFB -->|fallthrough| bb_00647D04
  bb_00647D04 -->|flow| bb_00647D11
  bb_00647D11 -->|flow| bb_00647D14
  bb_00647D14 -->|branch| bb_00647CFB
  bb_00647D14 -->|fallthrough| bb_00647D19
  bb_00647D19 -->|branch| bb_00647D2A
  bb_00647D19 -->|fallthrough| bb_00647D1E
  bb_00647D1E -->|flow| bb_00647D2A
```
