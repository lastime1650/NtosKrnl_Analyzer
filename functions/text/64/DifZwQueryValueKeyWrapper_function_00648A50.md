# DifZwQueryValueKeyWrapper

- RVA: `0x00648A50`–`0x00648BF5` (길이 `421` bytes)
- VA: `0x0000000140648A50`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD780`
- 디코드: `120`개 명령, `421/421` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00648A86` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00648A90` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00648AB8` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00648B02` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00648B28` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00648B41` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00648B63` → [ZwQueryValueKey](../6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x00648B8F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00648BB5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00648BCE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00648AC8` → RVA `0x00F048B8` (`.data`; read)
- `0x00648AEF` → RVA `0x00F04980` (`.data`; read)
- `0x00648AFB` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00648A50  48 8B C4                        mov rax, rsp
00648A53  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00648A57  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00648A5B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00648A5F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00648A63  55                              push rbp
00648A64  41 54                           push r12
00648A66  41 55                           push r13
00648A68  41 56                           push r14
00648A6A  41 57                           push r15
00648A6C  48 8B EC                        mov rbp, rsp
00648A6F  48 83 EC 70                     sub rsp, 0x70
00648A73  4C 8B EA                        mov r13, rdx
00648A76  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00648A7A  33 D2                           xor edx, edx
00648A7C  45 8B E0                        mov r12d, r8d
00648A7F  4D 8B F9                        mov r15, r9
00648A82  44 8D 42 40                     lea r8d, [rdx + 0x40]
00648A86  E8 B5 E1 07 00                  call 0x1406c6c40
00648A8B  B9 22 00 00 00                  mov ecx, 0x22
00648A90  E8 9F CF E4 FF                  call 0x140495a34
00648A95  4C 8B F0                        mov r14, rax
00648A98  48 85 C0                        test rax, rax
00648A9B  0F 84 A5 00 00 00               je 0x140648b46
00648AA1  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00648AA4  F6 C1 18                        test cl, 0x18
00648AA7  74 0A                           je 0x140648ab3
00648AA9  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00648AAD  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00648AB1  EB 0E                           jmp 0x140648ac1
00648AB3  F6 C1 04                        test cl, 4
00648AB6  74 09                           je 0x140648ac1
00648AB8  E8 4B B1 E8 FF                  call 0x1404d3c08
00648ABD  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00648AC1  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00648AC5  40 32 F6                        xor sil, sil
00648AC8  40 38 35 E9 BD 8B 00            cmp byte ptr [rip + 0x8bbde9], sil
00648ACF  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00648AD3  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00648AD6  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00648AD9  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00648ADD  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00648AE1  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
00648AE5  44 89 65 E0                     mov dword ptr [rbp - 0x20], r12d
00648AE9  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
00648AED  75 0C                           jne 0x140648afb
00648AEF  F7 05 87 BE 8B 00 00 08 00 00   test dword ptr [rip + 0x8bbe87], 0x800
00648AF9  74 13                           je 0x140648b0e
00648AFB  48 8D 0D 7E B3 8B 00            lea rcx, [rip + 0x8bb37e]
00648B02  E8 19 DB BC FF                  call 0x140216620
00648B07  40 8A F0                        mov sil, al
00648B0A  84 C0                           test al, al
00648B0C  74 38                           je 0x140648b46
00648B0E  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00648B12  48 8B 1F                        mov rbx, qword ptr [rdi]
00648B15  EB 19                           jmp 0x140648b30
00648B17  48 8D 43 F0                     lea rax, [rbx - 0x10]
00648B1B  48 85 C0                        test rax, rax
00648B1E  74 0D                           je 0x140648b2d
00648B20  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00648B24  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00648B28  E8 A3 1F 07 00                  call 0x1406baad0
00648B2D  48 8B 1B                        mov rbx, qword ptr [rbx]
00648B30  48 3B DF                        cmp rbx, rdi
00648B33  75 E2                           jne 0x140648b17
00648B35  40 84 F6                        test sil, sil
00648B38  74 0C                           je 0x140648b46
00648B3A  48 8D 0D 3F B3 8B 00            lea rcx, [rip + 0x8bb33f]
00648B41  E8 3A 13 D0 FF                  call 0x140349e80
00648B46  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00648B4A  4D 8B CF                        mov r9, r15
00648B4D  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00648B51  45 8B C4                        mov r8d, r12d
00648B54  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00648B59  49 8B D5                        mov rdx, r13
00648B5C  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00648B5F  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00648B63  E8 48 48 06 00                  call 0x1406ad3b0
00648B68  89 45 F8                        mov dword ptr [rbp - 8], eax
00648B6B  4D 85 F6                        test r14, r14
00648B6E  74 63                           je 0x140648bd3
00648B70  40 32 FF                        xor dil, dil
00648B73  40 38 3D 3E BD 8B 00            cmp byte ptr [rip + 0x8bbd3e], dil
00648B7A  75 0C                           jne 0x140648b88
00648B7C  F7 05 FA BD 8B 00 00 08 00 00   test dword ptr [rip + 0x8bbdfa], 0x800
00648B86  74 13                           je 0x140648b9b
00648B88  48 8D 0D F1 B2 8B 00            lea rcx, [rip + 0x8bb2f1]
00648B8F  E8 8C DA BC FF                  call 0x140216620
00648B94  40 8A F8                        mov dil, al
00648B97  84 C0                           test al, al
00648B99  74 38                           je 0x140648bd3
00648B9B  49 8D 76 30                     lea rsi, [r14 + 0x30]
00648B9F  48 8B 1E                        mov rbx, qword ptr [rsi]
00648BA2  EB 19                           jmp 0x140648bbd
00648BA4  48 8D 43 F0                     lea rax, [rbx - 0x10]
00648BA8  48 85 C0                        test rax, rax
00648BAB  74 0D                           je 0x140648bba
00648BAD  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00648BB1  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00648BB5  E8 16 1F 07 00                  call 0x1406baad0
00648BBA  48 8B 1B                        mov rbx, qword ptr [rbx]
00648BBD  48 3B DE                        cmp rbx, rsi
00648BC0  75 E2                           jne 0x140648ba4
00648BC2  40 84 FF                        test dil, dil
00648BC5  74 0C                           je 0x140648bd3
00648BC7  48 8D 0D B2 B2 8B 00            lea rcx, [rip + 0x8bb2b2]
00648BCE  E8 AD 12 D0 FF                  call 0x140349e80
00648BD3  8B 45 F8                        mov eax, dword ptr [rbp - 8]
00648BD6  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00648BDB  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00648BDF  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00648BE3  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00648BE7  49 8B E3                        mov rsp, r11
00648BEA  41 5F                           pop r15
00648BEC  41 5E                           pop r14
00648BEE  41 5D                           pop r13
00648BF0  41 5C                           pop r12
00648BF2  5D                              pop rbp
00648BF3  C3                              ret
00648BF4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwQueryValueKeyWrapper(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
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
    a2 = 0;
    result = memset(v_stack_m68, a2, a2 + 64, a4);
    result = DifGetAPIThunkContextById(34, a2, a2 + 64, a4);
    if (result == 0) goto loc_00648B46;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00648AB3;
    v_stack_m68 = v_stack_p0;
    goto loc_00648AC1;
loc_00648AB3:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a2 + 64, a4);
        v_stack_m68 = result;
    }
    v_rsi = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m58 = (unsigned int)((unsigned int)(a5));
    v_stack_m60 = a6;
    v_stack_m40 = 0;
    v_stack_m48 = (unsigned int)((unsigned int)(a3));
    v_stack_m50 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9158121)) != 0) goto loc_00648AFB;
    if (((*(unsigned int *)(v_rip + 9158279)) & (0x800ULL)) == 0) goto loc_00648B0E;
loc_00648AFB:
    result = ExAcquireRundownProtection(v_rip + 9155454, a2, a2 + 64, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00648B46;
loc_00648B0E:
    goto loc_00648B30;
loc_00648B17:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a2 + 64, a4);
    }
loc_00648B30:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00648B17;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9155391;
        result = ExReleaseRundownProtection(a1, a2, a2 + 64, a4);
    }
    v_stack_m70 = a6;
    v_stack_m78 = (unsigned int)((unsigned int)(a5));
    result = ZwQueryValueKey(v_stack_p8, 0, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_00648BD3;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9157950)) != 0) goto loc_00648B88;
    if (((*(unsigned int *)(v_rip + 9158138)) & (0x800ULL)) == 0) goto loc_00648B9B;
loc_00648B88:
    result = ExAcquireRundownProtection(v_rip + 9155313, 0, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00648BD3;
loc_00648B9B:
    goto loc_00648BBD;
loc_00648BA4:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, 0, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_00648BBD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_00648BA4;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9155250;
        result = ExReleaseRundownProtection(a1, 0, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwQueryValueKeyWrapper(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
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
    Arg2 = 0;
    result = memset(v_stack_m68, Arg2, Arg2 + 64, Arg4);
    result = DifGetAPIThunkContextById(34, Arg2, Arg2 + 64, Arg4);
    if (result == 0) goto loc_00648B46;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00648AB3;
    v_stack_m68 = v_stack_p0;
    goto loc_00648AC1;
loc_00648AB3:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg2 + 64, Arg4);
        v_stack_m68 = result;
    }
    local_rsi = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m58 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m60 = Arg6;
    v_stack_m40 = 0;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m50 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8BBDE9)) != 0) goto loc_00648AFB;
    if (((*(uint32_t *)(v_rip + 0x8BBE87)) & (0x800ULL)) == 0) goto loc_00648B0E;
loc_00648AFB:
    result = ExAcquireRundownProtection(v_rip + 9155454, Arg2, Arg2 + 64, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00648B46;
loc_00648B0E:
    goto loc_00648B30;
loc_00648B17:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg2 + 64, Arg4);
    }
loc_00648B30:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00648B17;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9155391;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg2 + 64, Arg4);
    }
    v_stack_m70 = Arg6;
    v_stack_m78 = (uint32_t)((uint32_t)(Arg5));
    result = ZwQueryValueKey(v_stack_p8, 0, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_00648BD3;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BBD3E)) != 0) goto loc_00648B88;
    if (((*(uint32_t *)(v_rip + 0x8BBDFA)) & (0x800ULL)) == 0) goto loc_00648B9B;
loc_00648B88:
    result = ExAcquireRundownProtection(v_rip + 9155313, 0, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00648BD3;
loc_00648B9B:
    goto loc_00648BBD;
loc_00648BA4:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, 0, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
loc_00648BBD:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_00648BA4;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9155250;
        result = ExReleaseRundownProtection(Arg1, 0, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00648A50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00648A50[BB_00648A50]
  bb_00648AA1[BB_00648AA1]
  bb_00648AA9[BB_00648AA9]
  bb_00648AB3[BB_00648AB3]
  bb_00648AB8[BB_00648AB8]
  bb_00648AC1[BB_00648AC1]
  bb_00648AEF[BB_00648AEF]
  bb_00648AFB[BB_00648AFB]
  bb_00648B0E[BB_00648B0E]
  bb_00648B17[BB_00648B17]
  bb_00648B20[BB_00648B20]
  bb_00648B2D[BB_00648B2D]
  bb_00648B30[BB_00648B30]
  bb_00648B35[BB_00648B35]
  bb_00648B3A[BB_00648B3A]
  bb_00648B46[BB_00648B46]
  bb_00648B70[BB_00648B70]
  bb_00648B7C[BB_00648B7C]
  bb_00648B88[BB_00648B88]
  bb_00648B9B[BB_00648B9B]
  bb_00648BA4[BB_00648BA4]
  bb_00648BAD[BB_00648BAD]
  bb_00648BBA[BB_00648BBA]
  bb_00648BBD[BB_00648BBD]
  bb_00648BC2[BB_00648BC2]
  bb_00648BC7[BB_00648BC7]
  bb_00648BD3[BB_00648BD3]
  bb_00648BF4[BB_00648BF4]
  bb_00648A50 -->|branch| bb_00648B46
  bb_00648A50 -->|fallthrough| bb_00648AA1
  bb_00648AA1 -->|branch| bb_00648AB3
  bb_00648AA1 -->|fallthrough| bb_00648AA9
  bb_00648AA9 -->|branch| bb_00648AC1
  bb_00648AB3 -->|branch| bb_00648AC1
  bb_00648AB3 -->|fallthrough| bb_00648AB8
  bb_00648AB8 -->|flow| bb_00648AC1
  bb_00648AC1 -->|branch| bb_00648AFB
  bb_00648AC1 -->|fallthrough| bb_00648AEF
  bb_00648AEF -->|branch| bb_00648B0E
  bb_00648AEF -->|fallthrough| bb_00648AFB
  bb_00648AFB -->|branch| bb_00648B46
  bb_00648AFB -->|fallthrough| bb_00648B0E
  bb_00648B0E -->|branch| bb_00648B30
  bb_00648B17 -->|branch| bb_00648B2D
  bb_00648B17 -->|fallthrough| bb_00648B20
  bb_00648B20 -->|flow| bb_00648B2D
  bb_00648B2D -->|flow| bb_00648B30
  bb_00648B30 -->|branch| bb_00648B17
  bb_00648B30 -->|fallthrough| bb_00648B35
  bb_00648B35 -->|branch| bb_00648B46
  bb_00648B35 -->|fallthrough| bb_00648B3A
  bb_00648B3A -->|flow| bb_00648B46
  bb_00648B46 -->|branch| bb_00648BD3
  bb_00648B46 -->|fallthrough| bb_00648B70
  bb_00648B70 -->|branch| bb_00648B88
  bb_00648B70 -->|fallthrough| bb_00648B7C
  bb_00648B7C -->|branch| bb_00648B9B
  bb_00648B7C -->|fallthrough| bb_00648B88
  bb_00648B88 -->|branch| bb_00648BD3
  bb_00648B88 -->|fallthrough| bb_00648B9B
  bb_00648B9B -->|branch| bb_00648BBD
  bb_00648BA4 -->|branch| bb_00648BBA
  bb_00648BA4 -->|fallthrough| bb_00648BAD
  bb_00648BAD -->|flow| bb_00648BBA
  bb_00648BBA -->|flow| bb_00648BBD
  bb_00648BBD -->|branch| bb_00648BA4
  bb_00648BBD -->|fallthrough| bb_00648BC2
  bb_00648BC2 -->|branch| bb_00648BD3
  bb_00648BC2 -->|fallthrough| bb_00648BC7
  bb_00648BC7 -->|flow| bb_00648BD3
```
