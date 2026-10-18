# DifZwEnumerateValueKeyWrapper

- RVA: `0x00641BA0`–`0x00641D49` (길이 `425` bytes)
- VA: `0x0000000140641BA0`
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
- `0x00641BE4` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00641C0C` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00641C56` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00641C7C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00641C95` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00641CB7` → [ZwEnumerateValueKey](../6A/ZwEnumerateValueKey_function_006AD330.md) (function, `0x006AD330`)
- `0x00641CE3` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00641D09` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00641D22` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00641C1C` → RVA `0x00F048B8` (`.data`; read)
- `0x00641C43` → RVA `0x00F04980` (`.data`; read)
- `0x00641C4F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00641BA0  48 8B C4                        mov rax, rsp
00641BA3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00641BA7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00641BAB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00641BAF  48 89 48 08                     mov qword ptr [rax + 8], rcx
00641BB3  55                              push rbp
00641BB4  41 54                           push r12
00641BB6  41 55                           push r13
00641BB8  41 56                           push r14
00641BBA  41 57                           push r15
00641BBC  48 8B EC                        mov rbp, rsp
00641BBF  48 83 EC 70                     sub rsp, 0x70
00641BC3  33 C0                           xor eax, eax
00641BC5  0F 57 C0                        xorps xmm0, xmm0
00641BC8  4D 8B F9                        mov r15, r9
00641BCB  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00641BCF  45 8B E0                        mov r12d, r8d
00641BD2  44 8B EA                        mov r13d, edx
00641BD5  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00641BD9  8D 48 67                        lea ecx, [rax + 0x67]
00641BDC  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00641BE0  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00641BE4  E8 4B 3E E5 FF                  call 0x140495a34
00641BE9  4C 8B F0                        mov r14, rax
00641BEC  48 85 C0                        test rax, rax
00641BEF  0F 84 A5 00 00 00               je 0x140641c9a
00641BF5  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00641BF8  F6 C1 18                        test cl, 0x18
00641BFB  74 0A                           je 0x140641c07
00641BFD  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00641C01  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00641C05  EB 0E                           jmp 0x140641c15
00641C07  F6 C1 04                        test cl, 4
00641C0A  74 09                           je 0x140641c15
00641C0C  E8 F7 1F E9 FF                  call 0x1404d3c08
00641C11  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00641C15  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00641C19  40 32 F6                        xor sil, sil
00641C1C  40 38 35 95 2C 8C 00            cmp byte ptr [rip + 0x8c2c95], sil
00641C23  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00641C27  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00641C2A  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00641C2D  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00641C31  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00641C35  44 89 6D E4                     mov dword ptr [rbp - 0x1c], r13d
00641C39  44 89 65 E0                     mov dword ptr [rbp - 0x20], r12d
00641C3D  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
00641C41  75 0C                           jne 0x140641c4f
00641C43  F7 05 33 2D 8C 00 00 08 00 00   test dword ptr [rip + 0x8c2d33], 0x800
00641C4D  74 13                           je 0x140641c62
00641C4F  48 8D 0D 2A 22 8C 00            lea rcx, [rip + 0x8c222a]
00641C56  E8 C5 49 BD FF                  call 0x140216620
00641C5B  40 8A F0                        mov sil, al
00641C5E  84 C0                           test al, al
00641C60  74 38                           je 0x140641c9a
00641C62  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00641C66  48 8B 1F                        mov rbx, qword ptr [rdi]
00641C69  EB 19                           jmp 0x140641c84
00641C6B  48 8D 43 F0                     lea rax, [rbx - 0x10]
00641C6F  48 85 C0                        test rax, rax
00641C72  74 0D                           je 0x140641c81
00641C74  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00641C78  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00641C7C  E8 4F 8E 07 00                  call 0x1406baad0
00641C81  48 8B 1B                        mov rbx, qword ptr [rbx]
00641C84  48 3B DF                        cmp rbx, rdi
00641C87  75 E2                           jne 0x140641c6b
00641C89  40 84 F6                        test sil, sil
00641C8C  74 0C                           je 0x140641c9a
00641C8E  48 8D 0D EB 21 8C 00            lea rcx, [rip + 0x8c21eb]
00641C95  E8 E6 81 D0 FF                  call 0x140349e80
00641C9A  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00641C9E  4D 8B CF                        mov r9, r15
00641CA1  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00641CA5  45 8B C4                        mov r8d, r12d
00641CA8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00641CAD  41 8B D5                        mov edx, r13d
00641CB0  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00641CB3  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00641CB7  E8 74 B6 06 00                  call 0x1406ad330
00641CBC  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00641CBF  4D 85 F6                        test r14, r14
00641CC2  74 63                           je 0x140641d27
00641CC4  40 32 FF                        xor dil, dil
00641CC7  40 38 3D EA 2B 8C 00            cmp byte ptr [rip + 0x8c2bea], dil
00641CCE  75 0C                           jne 0x140641cdc
00641CD0  F7 05 A6 2C 8C 00 00 08 00 00   test dword ptr [rip + 0x8c2ca6], 0x800
00641CDA  74 13                           je 0x140641cef
00641CDC  48 8D 0D 9D 21 8C 00            lea rcx, [rip + 0x8c219d]
00641CE3  E8 38 49 BD FF                  call 0x140216620
00641CE8  40 8A F8                        mov dil, al
00641CEB  84 C0                           test al, al
00641CED  74 38                           je 0x140641d27
00641CEF  49 8D 76 30                     lea rsi, [r14 + 0x30]
00641CF3  48 8B 1E                        mov rbx, qword ptr [rsi]
00641CF6  EB 19                           jmp 0x140641d11
00641CF8  48 8D 43 F0                     lea rax, [rbx - 0x10]
00641CFC  48 85 C0                        test rax, rax
00641CFF  74 0D                           je 0x140641d0e
00641D01  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00641D05  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00641D09  E8 C2 8D 07 00                  call 0x1406baad0
00641D0E  48 8B 1B                        mov rbx, qword ptr [rbx]
00641D11  48 3B DE                        cmp rbx, rsi
00641D14  75 E2                           jne 0x140641cf8
00641D16  40 84 FF                        test dil, dil
00641D19  74 0C                           je 0x140641d27
00641D1B  48 8D 0D 5E 21 8C 00            lea rcx, [rip + 0x8c215e]
00641D22  E8 59 81 D0 FF                  call 0x140349e80
00641D27  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00641D2A  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00641D2F  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00641D33  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00641D37  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00641D3B  49 8B E3                        mov rsp, r11
00641D3E  41 5F                           pop r15
00641D40  41 5E                           pop r14
00641D42  41 5D                           pop r13
00641D44  41 5C                           pop r12
00641D46  5D                              pop rbp
00641D47  C3                              ret
00641D48  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwEnumerateValueKeyWrapper(__int64 a1, int a2, int a3, __int64 a4, unsigned int a5, __int64 a6)
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
    result = DifGetAPIThunkContextById(result + 103, a2, a3, a4);
    if (result == 0) goto loc_00641C9A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00641C07;
    v_stack_m68 = v_stack_p0;
    goto loc_00641C15;
loc_00641C07:
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
    if ((*(unsigned __int8 *)(v_rip + 9186453)) != 0) goto loc_00641C4F;
    if (((*(unsigned int *)(v_rip + 9186611)) & (0x800ULL)) == 0) goto loc_00641C62;
loc_00641C4F:
    result = ExAcquireRundownProtection(v_rip + 9183786, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00641C9A;
loc_00641C62:
    goto loc_00641C84;
loc_00641C6B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00641C84:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00641C6B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9183723;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m70 = a6;
    v_stack_m78 = (unsigned int)((unsigned int)(a5));
    result = ZwEnumerateValueKey(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_00641D27;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9186282)) != 0) goto loc_00641CDC;
    if (((*(unsigned int *)(v_rip + 9186470)) & (0x800ULL)) == 0) goto loc_00641CEF;
loc_00641CDC:
    result = ExAcquireRundownProtection(v_rip + 9183645, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00641D27;
loc_00641CEF:
    goto loc_00641D11;
loc_00641CF8:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_00641D11:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_00641CF8;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9183582;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwEnumerateValueKeyWrapper(int64_t Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6)
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
    result = DifGetAPIThunkContextById(result + 103, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00641C9A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00641C07;
    v_stack_m68 = v_stack_p0;
    goto loc_00641C15;
loc_00641C07:
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
    if ((*(uint8_t *)(v_rip + 0x8C2C95)) != 0) goto loc_00641C4F;
    if (((*(uint32_t *)(v_rip + 0x8C2D33)) & (0x800ULL)) == 0) goto loc_00641C62;
loc_00641C4F:
    result = ExAcquireRundownProtection(v_rip + 9183786, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00641C9A;
loc_00641C62:
    goto loc_00641C84;
loc_00641C6B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00641C84:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00641C6B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9183723;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m70 = Arg6;
    v_stack_m78 = (uint32_t)((uint32_t)(Arg5));
    result = ZwEnumerateValueKey(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_00641D27;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C2BEA)) != 0) goto loc_00641CDC;
    if (((*(uint32_t *)(v_rip + 0x8C2CA6)) & (0x800ULL)) == 0) goto loc_00641CEF;
loc_00641CDC:
    result = ExAcquireRundownProtection(v_rip + 9183645, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00641D27;
loc_00641CEF:
    goto loc_00641D11;
loc_00641CF8:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
loc_00641D11:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_00641CF8;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9183582;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00641BA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00641BA0[BB_00641BA0]
  bb_00641BF5[BB_00641BF5]
  bb_00641BFD[BB_00641BFD]
  bb_00641C07[BB_00641C07]
  bb_00641C0C[BB_00641C0C]
  bb_00641C15[BB_00641C15]
  bb_00641C43[BB_00641C43]
  bb_00641C4F[BB_00641C4F]
  bb_00641C62[BB_00641C62]
  bb_00641C6B[BB_00641C6B]
  bb_00641C74[BB_00641C74]
  bb_00641C81[BB_00641C81]
  bb_00641C84[BB_00641C84]
  bb_00641C89[BB_00641C89]
  bb_00641C8E[BB_00641C8E]
  bb_00641C9A[BB_00641C9A]
  bb_00641CC4[BB_00641CC4]
  bb_00641CD0[BB_00641CD0]
  bb_00641CDC[BB_00641CDC]
  bb_00641CEF[BB_00641CEF]
  bb_00641CF8[BB_00641CF8]
  bb_00641D01[BB_00641D01]
  bb_00641D0E[BB_00641D0E]
  bb_00641D11[BB_00641D11]
  bb_00641D16[BB_00641D16]
  bb_00641D1B[BB_00641D1B]
  bb_00641D27[BB_00641D27]
  bb_00641D48[BB_00641D48]
  bb_00641BA0 -->|branch| bb_00641C9A
  bb_00641BA0 -->|fallthrough| bb_00641BF5
  bb_00641BF5 -->|branch| bb_00641C07
  bb_00641BF5 -->|fallthrough| bb_00641BFD
  bb_00641BFD -->|branch| bb_00641C15
  bb_00641C07 -->|branch| bb_00641C15
  bb_00641C07 -->|fallthrough| bb_00641C0C
  bb_00641C0C -->|flow| bb_00641C15
  bb_00641C15 -->|branch| bb_00641C4F
  bb_00641C15 -->|fallthrough| bb_00641C43
  bb_00641C43 -->|branch| bb_00641C62
  bb_00641C43 -->|fallthrough| bb_00641C4F
  bb_00641C4F -->|branch| bb_00641C9A
  bb_00641C4F -->|fallthrough| bb_00641C62
  bb_00641C62 -->|branch| bb_00641C84
  bb_00641C6B -->|branch| bb_00641C81
  bb_00641C6B -->|fallthrough| bb_00641C74
  bb_00641C74 -->|flow| bb_00641C81
  bb_00641C81 -->|flow| bb_00641C84
  bb_00641C84 -->|branch| bb_00641C6B
  bb_00641C84 -->|fallthrough| bb_00641C89
  bb_00641C89 -->|branch| bb_00641C9A
  bb_00641C89 -->|fallthrough| bb_00641C8E
  bb_00641C8E -->|flow| bb_00641C9A
  bb_00641C9A -->|branch| bb_00641D27
  bb_00641C9A -->|fallthrough| bb_00641CC4
  bb_00641CC4 -->|branch| bb_00641CDC
  bb_00641CC4 -->|fallthrough| bb_00641CD0
  bb_00641CD0 -->|branch| bb_00641CEF
  bb_00641CD0 -->|fallthrough| bb_00641CDC
  bb_00641CDC -->|branch| bb_00641D27
  bb_00641CDC -->|fallthrough| bb_00641CEF
  bb_00641CEF -->|branch| bb_00641D11
  bb_00641CF8 -->|branch| bb_00641D0E
  bb_00641CF8 -->|fallthrough| bb_00641D01
  bb_00641D01 -->|flow| bb_00641D0E
  bb_00641D0E -->|flow| bb_00641D11
  bb_00641D11 -->|branch| bb_00641CF8
  bb_00641D11 -->|fallthrough| bb_00641D16
  bb_00641D16 -->|branch| bb_00641D27
  bb_00641D16 -->|fallthrough| bb_00641D1B
  bb_00641D1B -->|flow| bb_00641D27
```
