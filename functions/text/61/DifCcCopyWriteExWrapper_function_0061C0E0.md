# DifCcCopyWriteExWrapper

- RVA: `0x0061C0E0`–`0x0061C28F` (길이 `431` bytes)
- VA: `0x000000014061C0E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD780`
- 디코드: `122`개 명령, `431/431` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0061C126` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0061C14E` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0061C19A` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061C1C0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061C1D9` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0061C1FD` → [CcCopyWriteEx](../3C/CcCopyWriteEx_function_003CA4F0.md) (function, `0x003CA4F0`)
- `0x0061C229` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061C24F` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061C268` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0061C15E` → RVA `0x00F048B8` (`.data`; read)
- `0x0061C187` → RVA `0x00F04980` (`.data`; read)
- `0x0061C193` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0061C0E0  48 8B C4                        mov rax, rsp
0061C0E3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0061C0E7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0061C0EB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0061C0EF  48 89 48 08                     mov qword ptr [rax + 8], rcx
0061C0F3  55                              push rbp
0061C0F4  41 54                           push r12
0061C0F6  41 55                           push r13
0061C0F8  41 56                           push r14
0061C0FA  41 57                           push r15
0061C0FC  48 8B EC                        mov rbp, rsp
0061C0FF  48 83 EC 70                     sub rsp, 0x70
0061C103  0F 57 C0                        xorps xmm0, xmm0
0061C106  33 C0                           xor eax, eax
0061C108  B9 B1 01 00 00                  mov ecx, 0x1b1
0061C10D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0061C111  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
0061C115  45 8A F9                        mov r15b, r9b
0061C118  45 8B E0                        mov r12d, r8d
0061C11B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0061C11F  4C 8B EA                        mov r13, rdx
0061C122  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0061C126  E8 09 99 E7 FF                  call 0x140495a34
0061C12B  4C 8B F0                        mov r14, rax
0061C12E  48 85 C0                        test rax, rax
0061C131  0F 84 A7 00 00 00               je 0x14061c1de
0061C137  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
0061C13A  F6 C1 18                        test cl, 0x18
0061C13D  74 0A                           je 0x14061c149
0061C13F  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0061C143  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
0061C147  EB 0E                           jmp 0x14061c157
0061C149  F6 C1 04                        test cl, 4
0061C14C  74 09                           je 0x14061c157
0061C14E  E8 B5 7A EB FF                  call 0x1404d3c08
0061C153  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0061C157  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0061C15B  40 32 F6                        xor sil, sil
0061C15E  40 38 35 53 87 8E 00            cmp byte ptr [rip + 0x8e8753], sil
0061C165  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0061C169  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0061C16D  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0061C171  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0061C175  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0061C179  4C 89 6D E0                     mov qword ptr [rbp - 0x20], r13
0061C17D  44 89 65 DC                     mov dword ptr [rbp - 0x24], r12d
0061C181  44 88 7D D8                     mov byte ptr [rbp - 0x28], r15b
0061C185  75 0C                           jne 0x14061c193
0061C187  F7 05 EF 87 8E 00 00 08 00 00   test dword ptr [rip + 0x8e87ef], 0x800
0061C191  74 13                           je 0x14061c1a6
0061C193  48 8D 0D E6 7C 8E 00            lea rcx, [rip + 0x8e7ce6]
0061C19A  E8 81 A4 BF FF                  call 0x140216620
0061C19F  40 8A F0                        mov sil, al
0061C1A2  84 C0                           test al, al
0061C1A4  74 38                           je 0x14061c1de
0061C1A6  49 8D 7E 20                     lea rdi, [r14 + 0x20]
0061C1AA  48 8B 1F                        mov rbx, qword ptr [rdi]
0061C1AD  EB 19                           jmp 0x14061c1c8
0061C1AF  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061C1B3  48 85 C0                        test rax, rax
0061C1B6  74 0D                           je 0x14061c1c5
0061C1B8  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061C1BC  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0061C1C0  E8 0B E9 09 00                  call 0x1406baad0
0061C1C5  48 8B 1B                        mov rbx, qword ptr [rbx]
0061C1C8  48 3B DF                        cmp rbx, rdi
0061C1CB  75 E2                           jne 0x14061c1af
0061C1CD  40 84 F6                        test sil, sil
0061C1D0  74 0C                           je 0x14061c1de
0061C1D2  48 8D 0D A7 7C 8E 00            lea rcx, [rip + 0x8e7ca7]
0061C1D9  E8 A2 DC D2 FF                  call 0x140349e80
0061C1DE  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0061C1E2  45 8A CF                        mov r9b, r15b
0061C1E5  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0061C1E9  45 8B C4                        mov r8d, r12d
0061C1EC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0061C1F1  49 8B D5                        mov rdx, r13
0061C1F4  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0061C1F8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0061C1FD  E8 EE E2 DA FF                  call 0x1403ca4f0
0061C202  88 45 F0                        mov byte ptr [rbp - 0x10], al
0061C205  4D 85 F6                        test r14, r14
0061C208  74 63                           je 0x14061c26d
0061C20A  40 32 FF                        xor dil, dil
0061C20D  40 38 3D A4 86 8E 00            cmp byte ptr [rip + 0x8e86a4], dil
0061C214  75 0C                           jne 0x14061c222
0061C216  F7 05 60 87 8E 00 00 08 00 00   test dword ptr [rip + 0x8e8760], 0x800
0061C220  74 13                           je 0x14061c235
0061C222  48 8D 0D 57 7C 8E 00            lea rcx, [rip + 0x8e7c57]
0061C229  E8 F2 A3 BF FF                  call 0x140216620
0061C22E  40 8A F8                        mov dil, al
0061C231  84 C0                           test al, al
0061C233  74 38                           je 0x14061c26d
0061C235  49 8D 76 30                     lea rsi, [r14 + 0x30]
0061C239  48 8B 1E                        mov rbx, qword ptr [rsi]
0061C23C  EB 19                           jmp 0x14061c257
0061C23E  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061C242  48 85 C0                        test rax, rax
0061C245  74 0D                           je 0x14061c254
0061C247  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061C24B  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0061C24F  E8 7C E8 09 00                  call 0x1406baad0
0061C254  48 8B 1B                        mov rbx, qword ptr [rbx]
0061C257  48 3B DE                        cmp rbx, rsi
0061C25A  75 E2                           jne 0x14061c23e
0061C25C  40 84 FF                        test dil, dil
0061C25F  74 0C                           je 0x14061c26d
0061C261  48 8D 0D 18 7C 8E 00            lea rcx, [rip + 0x8e7c18]
0061C268  E8 13 DC D2 FF                  call 0x140349e80
0061C26D  8A 45 F0                        mov al, byte ptr [rbp - 0x10]
0061C270  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
0061C275  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0061C279  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0061C27D  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0061C281  49 8B E3                        mov rsp, r11
0061C284  41 5F                           pop r15
0061C286  41 5E                           pop r14
0061C288  41 5D                           pop r13
0061C28A  41 5C                           pop r12
0061C28C  5D                              pop rbp
0061C28D  C3                              ret
0061C28E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifCcCopyWriteExWrapper(__int64 a1, __int64 a2, int a3, unsigned __int8 a4, __int64 a5, __int64 a6)
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
    unsigned __int8 v_stack_m50;
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
    result = 0;
    v_stack_m38 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(433, a2, a3, a4);
    if (result == 0) goto loc_0061C1DE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0061C149;
    v_stack_m68 = v_stack_p0;
    goto loc_0061C157;
loc_0061C149:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m68 = result;
    }
    v_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m58 = a5;
    v_stack_m60 = a6;
    v_stack_m48 = a2;
    v_stack_m4C = (unsigned int)((unsigned int)(a3));
    v_stack_m50 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9340755)) != 0) goto loc_0061C193;
    if (((*(unsigned int *)(v_rip + 9340911)) & (0x800ULL)) == 0) goto loc_0061C1A6;
loc_0061C193:
    result = ExAcquireRundownProtection(v_rip + 9338086, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061C1DE;
loc_0061C1A6:
    goto loc_0061C1C8;
loc_0061C1AF:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061C1C8:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0061C1AF;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9338023;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m70 = a6;
    v_stack_m78 = a5;
    result = CcCopyWriteEx(v_stack_p8, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    v_stack_m38 = (unsigned __int8)(result);
    if (result == 0) goto loc_0061C26D;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9340580)) != 0) goto loc_0061C222;
    if (((*(unsigned int *)(v_rip + 9340768)) & (0x800ULL)) == 0) goto loc_0061C235;
loc_0061C222:
    result = ExAcquireRundownProtection(v_rip + 9337943, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061C26D;
loc_0061C235:
    goto loc_0061C257;
loc_0061C23E:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_0061C257:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_0061C23E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9337880;
        result = ExReleaseRundownProtection(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    return v_stack_m38;
}
```

## 5. (Beta) C Style

```c
int64_t DifCcCopyWriteExWrapper(int64_t Arg1, int64_t Arg2, int32_t Arg3, uint8_t Arg4, int64_t Arg5, int64_t Arg6)
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
    uint8_t v_stack_m50;
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
    result = 0;
    v_stack_m38 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(433, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0061C1DE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0061C149;
    v_stack_m68 = v_stack_p0;
    goto loc_0061C157;
loc_0061C149:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m68 = result;
    }
    local_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m58 = Arg5;
    v_stack_m60 = Arg6;
    v_stack_m48 = Arg2;
    v_stack_m4C = (uint32_t)((uint32_t)(Arg3));
    v_stack_m50 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8E8753)) != 0) goto loc_0061C193;
    if (((*(uint32_t *)(v_rip + 0x8E87EF)) & (0x800ULL)) == 0) goto loc_0061C1A6;
loc_0061C193:
    result = ExAcquireRundownProtection(v_rip + 9338086, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0061C1DE;
loc_0061C1A6:
    goto loc_0061C1C8;
loc_0061C1AF:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0061C1C8:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0061C1AF;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9338023;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m70 = Arg6;
    v_stack_m78 = Arg5;
    result = CcCopyWriteEx(v_stack_p8, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    v_stack_m38 = (uint8_t)(result);
    if (result == 0) goto loc_0061C26D;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E86A4)) != 0) goto loc_0061C222;
    if (((*(uint32_t *)(v_rip + 0x8E8760)) & (0x800ULL)) == 0) goto loc_0061C235;
loc_0061C222:
    result = ExAcquireRundownProtection(v_rip + 9337943, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0061C26D;
loc_0061C235:
    goto loc_0061C257;
loc_0061C23E:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
loc_0061C257:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_0061C23E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9337880;
        result = ExReleaseRundownProtection(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
    return v_stack_m38;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0061C0E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0061C0E0[BB_0061C0E0]
  bb_0061C137[BB_0061C137]
  bb_0061C13F[BB_0061C13F]
  bb_0061C149[BB_0061C149]
  bb_0061C14E[BB_0061C14E]
  bb_0061C157[BB_0061C157]
  bb_0061C187[BB_0061C187]
  bb_0061C193[BB_0061C193]
  bb_0061C1A6[BB_0061C1A6]
  bb_0061C1AF[BB_0061C1AF]
  bb_0061C1B8[BB_0061C1B8]
  bb_0061C1C5[BB_0061C1C5]
  bb_0061C1C8[BB_0061C1C8]
  bb_0061C1CD[BB_0061C1CD]
  bb_0061C1D2[BB_0061C1D2]
  bb_0061C1DE[BB_0061C1DE]
  bb_0061C20A[BB_0061C20A]
  bb_0061C216[BB_0061C216]
  bb_0061C222[BB_0061C222]
  bb_0061C235[BB_0061C235]
  bb_0061C23E[BB_0061C23E]
  bb_0061C247[BB_0061C247]
  bb_0061C254[BB_0061C254]
  bb_0061C257[BB_0061C257]
  bb_0061C25C[BB_0061C25C]
  bb_0061C261[BB_0061C261]
  bb_0061C26D[BB_0061C26D]
  bb_0061C28E[BB_0061C28E]
  bb_0061C0E0 -->|branch| bb_0061C1DE
  bb_0061C0E0 -->|fallthrough| bb_0061C137
  bb_0061C137 -->|branch| bb_0061C149
  bb_0061C137 -->|fallthrough| bb_0061C13F
  bb_0061C13F -->|branch| bb_0061C157
  bb_0061C149 -->|branch| bb_0061C157
  bb_0061C149 -->|fallthrough| bb_0061C14E
  bb_0061C14E -->|flow| bb_0061C157
  bb_0061C157 -->|branch| bb_0061C193
  bb_0061C157 -->|fallthrough| bb_0061C187
  bb_0061C187 -->|branch| bb_0061C1A6
  bb_0061C187 -->|fallthrough| bb_0061C193
  bb_0061C193 -->|branch| bb_0061C1DE
  bb_0061C193 -->|fallthrough| bb_0061C1A6
  bb_0061C1A6 -->|branch| bb_0061C1C8
  bb_0061C1AF -->|branch| bb_0061C1C5
  bb_0061C1AF -->|fallthrough| bb_0061C1B8
  bb_0061C1B8 -->|flow| bb_0061C1C5
  bb_0061C1C5 -->|flow| bb_0061C1C8
  bb_0061C1C8 -->|branch| bb_0061C1AF
  bb_0061C1C8 -->|fallthrough| bb_0061C1CD
  bb_0061C1CD -->|branch| bb_0061C1DE
  bb_0061C1CD -->|fallthrough| bb_0061C1D2
  bb_0061C1D2 -->|flow| bb_0061C1DE
  bb_0061C1DE -->|branch| bb_0061C26D
  bb_0061C1DE -->|fallthrough| bb_0061C20A
  bb_0061C20A -->|branch| bb_0061C222
  bb_0061C20A -->|fallthrough| bb_0061C216
  bb_0061C216 -->|branch| bb_0061C235
  bb_0061C216 -->|fallthrough| bb_0061C222
  bb_0061C222 -->|branch| bb_0061C26D
  bb_0061C222 -->|fallthrough| bb_0061C235
  bb_0061C235 -->|branch| bb_0061C257
  bb_0061C23E -->|branch| bb_0061C254
  bb_0061C23E -->|fallthrough| bb_0061C247
  bb_0061C247 -->|flow| bb_0061C254
  bb_0061C254 -->|flow| bb_0061C257
  bb_0061C257 -->|branch| bb_0061C23E
  bb_0061C257 -->|fallthrough| bb_0061C25C
  bb_0061C25C -->|branch| bb_0061C26D
  bb_0061C25C -->|fallthrough| bb_0061C261
  bb_0061C261 -->|flow| bb_0061C26D
```
