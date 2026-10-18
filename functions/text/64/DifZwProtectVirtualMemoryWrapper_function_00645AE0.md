# DifZwProtectVirtualMemoryWrapper

- RVA: `0x00645AE0`–`0x00645C7C` (길이 `412` bytes)
- VA: `0x0000000140645AE0`
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
- `0x00645B24` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00645B4C` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00645B90` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00645BB6` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00645BCF` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00645BEA` → [ZwProtectVirtualMemory](../6A/ZwProtectVirtualMemory_function_006ADAD0.md) (function, `0x006ADAD0`)
- `0x00645C16` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00645C3C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00645C55` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00645B5C` → RVA `0x00F048B8` (`.data`; read)
- `0x00645B7D` → RVA `0x00F04980` (`.data`; read)
- `0x00645B89` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00645AE0  48 8B C4                        mov rax, rsp
00645AE3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00645AE7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00645AEB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00645AEF  48 89 48 08                     mov qword ptr [rax + 8], rcx
00645AF3  55                              push rbp
00645AF4  41 54                           push r12
00645AF6  41 55                           push r13
00645AF8  41 56                           push r14
00645AFA  41 57                           push r15
00645AFC  48 8B EC                        mov rbp, rsp
00645AFF  48 83 EC 70                     sub rsp, 0x70
00645B03  33 C0                           xor eax, eax
00645B05  0F 57 C0                        xorps xmm0, xmm0
00645B08  45 8B F9                        mov r15d, r9d
00645B0B  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00645B0F  4D 8B E0                        mov r12, r8
00645B12  4C 8B EA                        mov r13, rdx
00645B15  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00645B19  8D 48 3F                        lea ecx, [rax + 0x3f]
00645B1C  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00645B20  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00645B24  E8 0B FF E4 FF                  call 0x140495a34
00645B29  4C 8B F0                        mov r14, rax
00645B2C  48 85 C0                        test rax, rax
00645B2F  0F 84 9F 00 00 00               je 0x140645bd4
00645B35  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00645B38  F6 C1 18                        test cl, 0x18
00645B3B  74 0A                           je 0x140645b47
00645B3D  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00645B41  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00645B45  EB 0E                           jmp 0x140645b55
00645B47  F6 C1 04                        test cl, 4
00645B4A  74 09                           je 0x140645b55
00645B4C  E8 B7 E0 E8 FF                  call 0x1404d3c08
00645B51  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00645B55  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00645B59  40 32 F6                        xor sil, sil
00645B5C  40 38 35 55 ED 8B 00            cmp byte ptr [rip + 0x8bed55], sil
00645B63  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00645B67  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00645B6B  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00645B6F  4C 89 6D E0                     mov qword ptr [rbp - 0x20], r13
00645B73  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
00645B77  44 89 7D D0                     mov dword ptr [rbp - 0x30], r15d
00645B7B  75 0C                           jne 0x140645b89
00645B7D  F7 05 F9 ED 8B 00 00 08 00 00   test dword ptr [rip + 0x8bedf9], 0x800
00645B87  74 13                           je 0x140645b9c
00645B89  48 8D 0D F0 E2 8B 00            lea rcx, [rip + 0x8be2f0]
00645B90  E8 8B 0A BD FF                  call 0x140216620
00645B95  40 8A F0                        mov sil, al
00645B98  84 C0                           test al, al
00645B9A  74 38                           je 0x140645bd4
00645B9C  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00645BA0  48 8B 1F                        mov rbx, qword ptr [rdi]
00645BA3  EB 19                           jmp 0x140645bbe
00645BA5  48 8D 43 F0                     lea rax, [rbx - 0x10]
00645BA9  48 85 C0                        test rax, rax
00645BAC  74 0D                           je 0x140645bbb
00645BAE  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00645BB2  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00645BB6  E8 15 4F 07 00                  call 0x1406baad0
00645BBB  48 8B 1B                        mov rbx, qword ptr [rbx]
00645BBE  48 3B DF                        cmp rbx, rdi
00645BC1  75 E2                           jne 0x140645ba5
00645BC3  40 84 F6                        test sil, sil
00645BC6  74 0C                           je 0x140645bd4
00645BC8  48 8D 0D B1 E2 8B 00            lea rcx, [rip + 0x8be2b1]
00645BCF  E8 AC 42 D0 FF                  call 0x140349e80
00645BD4  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00645BD8  45 8B CF                        mov r9d, r15d
00645BDB  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00645BDF  4D 8B C4                        mov r8, r12
00645BE2  49 8B D5                        mov rdx, r13
00645BE5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00645BEA  E8 E1 7E 06 00                  call 0x1406adad0
00645BEF  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00645BF2  4D 85 F6                        test r14, r14
00645BF5  74 63                           je 0x140645c5a
00645BF7  40 32 FF                        xor dil, dil
00645BFA  40 38 3D B7 EC 8B 00            cmp byte ptr [rip + 0x8becb7], dil
00645C01  75 0C                           jne 0x140645c0f
00645C03  F7 05 73 ED 8B 00 00 08 00 00   test dword ptr [rip + 0x8bed73], 0x800
00645C0D  74 13                           je 0x140645c22
00645C0F  48 8D 0D 6A E2 8B 00            lea rcx, [rip + 0x8be26a]
00645C16  E8 05 0A BD FF                  call 0x140216620
00645C1B  40 8A F8                        mov dil, al
00645C1E  84 C0                           test al, al
00645C20  74 38                           je 0x140645c5a
00645C22  49 8D 76 30                     lea rsi, [r14 + 0x30]
00645C26  48 8B 1E                        mov rbx, qword ptr [rsi]
00645C29  EB 19                           jmp 0x140645c44
00645C2B  48 8D 43 F0                     lea rax, [rbx - 0x10]
00645C2F  48 85 C0                        test rax, rax
00645C32  74 0D                           je 0x140645c41
00645C34  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00645C38  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00645C3C  E8 8F 4E 07 00                  call 0x1406baad0
00645C41  48 8B 1B                        mov rbx, qword ptr [rbx]
00645C44  48 3B DE                        cmp rbx, rsi
00645C47  75 E2                           jne 0x140645c2b
00645C49  40 84 FF                        test dil, dil
00645C4C  74 0C                           je 0x140645c5a
00645C4E  48 8D 0D 2B E2 8B 00            lea rcx, [rip + 0x8be22b]
00645C55  E8 26 42 D0 FF                  call 0x140349e80
00645C5A  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00645C5D  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00645C62  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00645C66  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00645C6A  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00645C6E  49 8B E3                        mov rsp, r11
00645C71  41 5F                           pop r15
00645C73  41 5E                           pop r14
00645C75  41 5D                           pop r13
00645C77  41 5C                           pop r12
00645C79  5D                              pop rbp
00645C7A  C3                              ret
00645C7B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwProtectVirtualMemoryWrapper(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5)
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
    result = DifGetAPIThunkContextById(result + 63, a2, a3, a4);
    if (result == 0) goto loc_00645BD4;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00645B47;
    v_stack_m68 = v_stack_p0;
    goto loc_00645B55;
loc_00645B47:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m68 = result;
    }
    v_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m60 = a5;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    v_stack_m58 = (unsigned int)((unsigned int)(a4));
    if ((*(unsigned __int8 *)(v_rip + 9170261)) != 0) goto loc_00645B89;
    if (((*(unsigned int *)(v_rip + 9170425)) & (0x800ULL)) == 0) goto loc_00645B9C;
loc_00645B89:
    result = ExAcquireRundownProtection(v_rip + 9167600, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00645BD4;
loc_00645B9C:
    goto loc_00645BBE;
loc_00645BA5:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00645BBE:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00645BA5;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9167537;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m78 = a5;
    result = ZwProtectVirtualMemory(v_stack_p8, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_00645C5A;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9170103)) != 0) goto loc_00645C0F;
    if (((*(unsigned int *)(v_rip + 9170291)) & (0x800ULL)) == 0) goto loc_00645C22;
loc_00645C0F:
    result = ExAcquireRundownProtection(v_rip + 9167466, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_00645C5A;
loc_00645C22:
    goto loc_00645C44;
loc_00645C2B:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_00645C44:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_00645C2B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9167403;
        result = ExReleaseRundownProtection(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwProtectVirtualMemoryWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
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
    result = DifGetAPIThunkContextById(result + 63, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00645BD4;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00645B47;
    v_stack_m68 = v_stack_p0;
    goto loc_00645B55;
loc_00645B47:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m68 = result;
    }
    local_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m60 = Arg5;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    v_stack_m58 = (uint32_t)((uint32_t)(Arg4));
    if ((*(uint8_t *)(v_rip + 0x8BED55)) != 0) goto loc_00645B89;
    if (((*(uint32_t *)(v_rip + 0x8BEDF9)) & (0x800ULL)) == 0) goto loc_00645B9C;
loc_00645B89:
    result = ExAcquireRundownProtection(v_rip + 9167600, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00645BD4;
loc_00645B9C:
    goto loc_00645BBE;
loc_00645BA5:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00645BBE:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00645BA5;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9167537;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m78 = Arg5;
    result = ZwProtectVirtualMemory(v_stack_p8, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_00645C5A;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BECB7)) != 0) goto loc_00645C0F;
    if (((*(uint32_t *)(v_rip + 0x8BED73)) & (0x800ULL)) == 0) goto loc_00645C22;
loc_00645C0F:
    result = ExAcquireRundownProtection(v_rip + 9167466, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_00645C5A;
loc_00645C22:
    goto loc_00645C44;
loc_00645C2B:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_00645C44:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_00645C2B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9167403;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00645AE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00645AE0[BB_00645AE0]
  bb_00645B35[BB_00645B35]
  bb_00645B3D[BB_00645B3D]
  bb_00645B47[BB_00645B47]
  bb_00645B4C[BB_00645B4C]
  bb_00645B55[BB_00645B55]
  bb_00645B7D[BB_00645B7D]
  bb_00645B89[BB_00645B89]
  bb_00645B9C[BB_00645B9C]
  bb_00645BA5[BB_00645BA5]
  bb_00645BAE[BB_00645BAE]
  bb_00645BBB[BB_00645BBB]
  bb_00645BBE[BB_00645BBE]
  bb_00645BC3[BB_00645BC3]
  bb_00645BC8[BB_00645BC8]
  bb_00645BD4[BB_00645BD4]
  bb_00645BF7[BB_00645BF7]
  bb_00645C03[BB_00645C03]
  bb_00645C0F[BB_00645C0F]
  bb_00645C22[BB_00645C22]
  bb_00645C2B[BB_00645C2B]
  bb_00645C34[BB_00645C34]
  bb_00645C41[BB_00645C41]
  bb_00645C44[BB_00645C44]
  bb_00645C49[BB_00645C49]
  bb_00645C4E[BB_00645C4E]
  bb_00645C5A[BB_00645C5A]
  bb_00645C7B[BB_00645C7B]
  bb_00645AE0 -->|branch| bb_00645BD4
  bb_00645AE0 -->|fallthrough| bb_00645B35
  bb_00645B35 -->|branch| bb_00645B47
  bb_00645B35 -->|fallthrough| bb_00645B3D
  bb_00645B3D -->|branch| bb_00645B55
  bb_00645B47 -->|branch| bb_00645B55
  bb_00645B47 -->|fallthrough| bb_00645B4C
  bb_00645B4C -->|flow| bb_00645B55
  bb_00645B55 -->|branch| bb_00645B89
  bb_00645B55 -->|fallthrough| bb_00645B7D
  bb_00645B7D -->|branch| bb_00645B9C
  bb_00645B7D -->|fallthrough| bb_00645B89
  bb_00645B89 -->|branch| bb_00645BD4
  bb_00645B89 -->|fallthrough| bb_00645B9C
  bb_00645B9C -->|branch| bb_00645BBE
  bb_00645BA5 -->|branch| bb_00645BBB
  bb_00645BA5 -->|fallthrough| bb_00645BAE
  bb_00645BAE -->|flow| bb_00645BBB
  bb_00645BBB -->|flow| bb_00645BBE
  bb_00645BBE -->|branch| bb_00645BA5
  bb_00645BBE -->|fallthrough| bb_00645BC3
  bb_00645BC3 -->|branch| bb_00645BD4
  bb_00645BC3 -->|fallthrough| bb_00645BC8
  bb_00645BC8 -->|flow| bb_00645BD4
  bb_00645BD4 -->|branch| bb_00645C5A
  bb_00645BD4 -->|fallthrough| bb_00645BF7
  bb_00645BF7 -->|branch| bb_00645C0F
  bb_00645BF7 -->|fallthrough| bb_00645C03
  bb_00645C03 -->|branch| bb_00645C22
  bb_00645C03 -->|fallthrough| bb_00645C0F
  bb_00645C0F -->|branch| bb_00645C5A
  bb_00645C0F -->|fallthrough| bb_00645C22
  bb_00645C22 -->|branch| bb_00645C44
  bb_00645C2B -->|branch| bb_00645C41
  bb_00645C2B -->|fallthrough| bb_00645C34
  bb_00645C34 -->|flow| bb_00645C41
  bb_00645C41 -->|flow| bb_00645C44
  bb_00645C44 -->|branch| bb_00645C2B
  bb_00645C44 -->|fallthrough| bb_00645C49
  bb_00645C49 -->|branch| bb_00645C5A
  bb_00645C49 -->|fallthrough| bb_00645C4E
  bb_00645C4E -->|flow| bb_00645C5A
```
