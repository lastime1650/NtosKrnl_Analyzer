# DifMmAllocatePagesForMdlExWrapper

- RVA: `0x00634890`–`0x00634A39` (길이 `425` bytes)
- VA: `0x0000000140634890`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2D48`
- 디코드: `122`개 명령, `425/425` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006348D6` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006348FE` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00634946` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063496C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00634985` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006349A5` → [MmAllocatePagesForMdlEx](../3E/MmAllocatePagesForMdlEx_function_003EA8C0.md) (function, `0x003EA8C0`)
- `0x006349D2` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006349F8` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00634A11` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063490E` → RVA `0x00F048B8` (`.data`; read)
- `0x00634933` → RVA `0x00F04980` (`.data`; read)
- `0x0063493F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00634890  48 8B C4                        mov rax, rsp
00634893  48 89 58 08                     mov qword ptr [rax + 8], rbx
00634897  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
0063489B  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
0063489F  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
006348A3  55                              push rbp
006348A4  41 54                           push r12
006348A6  41 55                           push r13
006348A8  41 56                           push r14
006348AA  41 57                           push r15
006348AC  48 8B EC                        mov rbp, rsp
006348AF  48 83 EC 70                     sub rsp, 0x70
006348B3  0F 57 C0                        xorps xmm0, xmm0
006348B6  33 C0                           xor eax, eax
006348B8  48 8B F1                        mov rsi, rcx
006348BB  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
006348BF  B9 E5 00 00 00                  mov ecx, 0xe5
006348C4  49 8B D8                        mov rbx, r8
006348C7  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
006348CB  48 8B FA                        mov rdi, rdx
006348CE  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
006348D2  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
006348D6  E8 59 11 E6 FF                  call 0x140495a34
006348DB  4C 8B E8                        mov r13, rax
006348DE  48 85 C0                        test rax, rax
006348E1  0F 84 A3 00 00 00               je 0x14063498a
006348E7  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
006348EA  F6 C1 18                        test cl, 0x18
006348ED  74 0A                           je 0x1406348f9
006348EF  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
006348F3  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
006348F7  EB 0E                           jmp 0x140634907
006348F9  F6 C1 04                        test cl, 4
006348FC  74 09                           je 0x140634907
006348FE  E8 05 F3 E9 FF                  call 0x1404d3c08
00634903  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00634907  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0063490B  45 32 E4                        xor r12b, r12b
0063490E  44 38 25 A3 FF 8C 00            cmp byte ptr [rip + 0x8cffa3], r12b
00634915  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00634919  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
0063491C  89 45 CC                        mov dword ptr [rbp - 0x34], eax
0063491F  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
00634922  89 45 C8                        mov dword ptr [rbp - 0x38], eax
00634925  48 89 75 E8                     mov qword ptr [rbp - 0x18], rsi
00634929  48 89 7D E0                     mov qword ptr [rbp - 0x20], rdi
0063492D  48 89 5D D8                     mov qword ptr [rbp - 0x28], rbx
00634931  75 0C                           jne 0x14063493f
00634933  F7 05 43 00 8D 00 00 08 00 00   test dword ptr [rip + 0x8d0043], 0x800
0063493D  74 13                           je 0x140634952
0063493F  48 8D 0D 3A F5 8C 00            lea rcx, [rip + 0x8cf53a]
00634946  E8 D5 1C BE FF                  call 0x140216620
0063494B  44 8A E0                        mov r12b, al
0063494E  84 C0                           test al, al
00634950  74 38                           je 0x14063498a
00634952  4D 8D 7D 20                     lea r15, [r13 + 0x20]
00634956  4D 8B 37                        mov r14, qword ptr [r15]
00634959  EB 19                           jmp 0x140634974
0063495B  49 8D 46 F0                     lea rax, [r14 - 0x10]
0063495F  48 85 C0                        test rax, rax
00634962  74 0D                           je 0x140634971
00634964  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00634968  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0063496C  E8 5F 61 08 00                  call 0x1406baad0
00634971  4D 8B 36                        mov r14, qword ptr [r14]
00634974  4D 3B F7                        cmp r14, r15
00634977  75 E2                           jne 0x14063495b
00634979  45 84 E4                        test r12b, r12b
0063497C  74 0C                           je 0x14063498a
0063497E  48 8D 0D FB F4 8C 00            lea rcx, [rip + 0x8cf4fb]
00634985  E8 F6 54 D1 FF                  call 0x140349e80
0063498A  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
0063498D  4C 8B C3                        mov r8, rbx
00634990  4C 8B 4D 48                     mov r9, qword ptr [rbp + 0x48]
00634994  48 8B D7                        mov rdx, rdi
00634997  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0063499B  48 8B CE                        mov rcx, rsi
0063499E  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
006349A1  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
006349A5  E8 16 5F DB FF                  call 0x1403ea8c0
006349AA  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
006349AE  4D 85 ED                        test r13, r13
006349B1  74 63                           je 0x140634a16
006349B3  40 32 FF                        xor dil, dil
006349B6  40 38 3D FB FE 8C 00            cmp byte ptr [rip + 0x8cfefb], dil
006349BD  75 0C                           jne 0x1406349cb
006349BF  F7 05 B7 FF 8C 00 00 08 00 00   test dword ptr [rip + 0x8cffb7], 0x800
006349C9  74 13                           je 0x1406349de
006349CB  48 8D 0D AE F4 8C 00            lea rcx, [rip + 0x8cf4ae]
006349D2  E8 49 1C BE FF                  call 0x140216620
006349D7  40 8A F8                        mov dil, al
006349DA  84 C0                           test al, al
006349DC  74 38                           je 0x140634a16
006349DE  49 8D 75 30                     lea rsi, [r13 + 0x30]
006349E2  48 8B 1E                        mov rbx, qword ptr [rsi]
006349E5  EB 19                           jmp 0x140634a00
006349E7  48 8D 43 F0                     lea rax, [rbx - 0x10]
006349EB  48 85 C0                        test rax, rax
006349EE  74 0D                           je 0x1406349fd
006349F0  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006349F4  48 8D 4D C0                     lea rcx, [rbp - 0x40]
006349F8  E8 D3 60 08 00                  call 0x1406baad0
006349FD  48 8B 1B                        mov rbx, qword ptr [rbx]
00634A00  48 3B DE                        cmp rbx, rsi
00634A03  75 E2                           jne 0x1406349e7
00634A05  40 84 FF                        test dil, dil
00634A08  74 0C                           je 0x140634a16
00634A0A  48 8D 0D 6F F4 8C 00            lea rcx, [rip + 0x8cf46f]
00634A11  E8 6A 54 D1 FF                  call 0x140349e80
00634A16  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00634A1A  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00634A1F  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00634A23  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00634A27  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00634A2B  49 8B E3                        mov rsp, r11
00634A2E  41 5F                           pop r15
00634A30  41 5E                           pop r14
00634A32  41 5D                           pop r13
00634A34  41 5C                           pop r12
00634A36  5D                              pop rbp
00634A37  C3                              ret
00634A38  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmAllocatePagesForMdlExWrapper(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6)
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
    unsigned __int64 v_stack_p20;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    v_rsp = (v_rsp) - (112);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(229, a2, a3, a4);
    if (result == 0) goto loc_0063498A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006348F9;
    v_stack_m68 = v_stack_p0;
    goto loc_00634907;
loc_006348F9:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m68 = result;
    }
    v_r12 = 0;
    v_stack_m58 = v_stack_p20;
    v_stack_m5C = (unsigned int)((unsigned int)(a5));
    v_stack_m60 = (unsigned int)((unsigned int)(a6));
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9240483)) != 0) goto loc_0063493F;
    if (((*(unsigned int *)(v_rip + 9240643)) & (0x800ULL)) == 0) goto loc_00634952;
loc_0063493F:
    result = ExAcquireRundownProtection(v_rip + 9237818, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063498A;
loc_00634952:
    goto loc_00634974;
loc_0063495B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00634974:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063495B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9237755;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m70 = (unsigned int)((unsigned int)(a6));
    v_stack_m78 = (unsigned int)((unsigned int)(a5));
    result = MmAllocatePagesForMdlEx(a1, a2, a3, v_stack_p20);
    v_stack_m38 = result;
    if (result == 0) goto loc_00634A16;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9240315)) != 0) goto loc_006349CB;
    if (((*(unsigned int *)(v_rip + 9240503)) & (0x800ULL)) == 0) goto loc_006349DE;
loc_006349CB:
    result = ExAcquireRundownProtection(v_rip + 9237678, a2, a3, v_stack_p20);
    if ((unsigned __int8)(result) == 0) goto loc_00634A16;
loc_006349DE:
    goto loc_00634A00;
loc_006349E7:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, v_stack_p20);
    }
loc_00634A00:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_006349E7;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9237615;
        result = ExReleaseRundownProtection(a1, a2, a3, v_stack_p20);
    }
    return v_stack_m38;
}
```

## 5. (Beta) C Style

```c
int64_t DifMmAllocatePagesForMdlExWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6)
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
    uint64_t v_stack_p20;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    local_rsp = (local_rsp) - (112);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(229, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0063498A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006348F9;
    v_stack_m68 = v_stack_p0;
    goto loc_00634907;
loc_006348F9:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m68 = result;
    }
    local_r12 = 0;
    v_stack_m58 = v_stack_p20;
    v_stack_m5C = (uint32_t)((uint32_t)(Arg5));
    v_stack_m60 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8CFFA3)) != 0) goto loc_0063493F;
    if (((*(uint32_t *)(v_rip + 0x8D0043)) & (0x800ULL)) == 0) goto loc_00634952;
loc_0063493F:
    result = ExAcquireRundownProtection(v_rip + 9237818, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0063498A;
loc_00634952:
    goto loc_00634974;
loc_0063495B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00634974:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063495B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9237755;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m70 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m78 = (uint32_t)((uint32_t)(Arg5));
    result = MmAllocatePagesForMdlEx(Arg1, Arg2, Arg3, v_stack_p20);
    v_stack_m38 = result;
    if (result == 0) goto loc_00634A16;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CFEFB)) != 0) goto loc_006349CB;
    if (((*(uint32_t *)(v_rip + 0x8CFFB7)) & (0x800ULL)) == 0) goto loc_006349DE;
loc_006349CB:
    result = ExAcquireRundownProtection(v_rip + 9237678, Arg2, Arg3, v_stack_p20);
    if ((uint8_t)(result) == 0) goto loc_00634A16;
loc_006349DE:
    goto loc_00634A00;
loc_006349E7:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, v_stack_p20);
    }
loc_00634A00:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_006349E7;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9237615;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, v_stack_p20);
    }
    return v_stack_m38;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00634890&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00634890[BB_00634890]
  bb_006348E7[BB_006348E7]
  bb_006348EF[BB_006348EF]
  bb_006348F9[BB_006348F9]
  bb_006348FE[BB_006348FE]
  bb_00634907[BB_00634907]
  bb_00634933[BB_00634933]
  bb_0063493F[BB_0063493F]
  bb_00634952[BB_00634952]
  bb_0063495B[BB_0063495B]
  bb_00634964[BB_00634964]
  bb_00634971[BB_00634971]
  bb_00634974[BB_00634974]
  bb_00634979[BB_00634979]
  bb_0063497E[BB_0063497E]
  bb_0063498A[BB_0063498A]
  bb_006349B3[BB_006349B3]
  bb_006349BF[BB_006349BF]
  bb_006349CB[BB_006349CB]
  bb_006349DE[BB_006349DE]
  bb_006349E7[BB_006349E7]
  bb_006349F0[BB_006349F0]
  bb_006349FD[BB_006349FD]
  bb_00634A00[BB_00634A00]
  bb_00634A05[BB_00634A05]
  bb_00634A0A[BB_00634A0A]
  bb_00634A16[BB_00634A16]
  bb_00634A38[BB_00634A38]
  bb_00634890 -->|branch| bb_0063498A
  bb_00634890 -->|fallthrough| bb_006348E7
  bb_006348E7 -->|branch| bb_006348F9
  bb_006348E7 -->|fallthrough| bb_006348EF
  bb_006348EF -->|branch| bb_00634907
  bb_006348F9 -->|branch| bb_00634907
  bb_006348F9 -->|fallthrough| bb_006348FE
  bb_006348FE -->|flow| bb_00634907
  bb_00634907 -->|branch| bb_0063493F
  bb_00634907 -->|fallthrough| bb_00634933
  bb_00634933 -->|branch| bb_00634952
  bb_00634933 -->|fallthrough| bb_0063493F
  bb_0063493F -->|branch| bb_0063498A
  bb_0063493F -->|fallthrough| bb_00634952
  bb_00634952 -->|branch| bb_00634974
  bb_0063495B -->|branch| bb_00634971
  bb_0063495B -->|fallthrough| bb_00634964
  bb_00634964 -->|flow| bb_00634971
  bb_00634971 -->|flow| bb_00634974
  bb_00634974 -->|branch| bb_0063495B
  bb_00634974 -->|fallthrough| bb_00634979
  bb_00634979 -->|branch| bb_0063498A
  bb_00634979 -->|fallthrough| bb_0063497E
  bb_0063497E -->|flow| bb_0063498A
  bb_0063498A -->|branch| bb_00634A16
  bb_0063498A -->|fallthrough| bb_006349B3
  bb_006349B3 -->|branch| bb_006349CB
  bb_006349B3 -->|fallthrough| bb_006349BF
  bb_006349BF -->|branch| bb_006349DE
  bb_006349BF -->|fallthrough| bb_006349CB
  bb_006349CB -->|branch| bb_00634A16
  bb_006349CB -->|fallthrough| bb_006349DE
  bb_006349DE -->|branch| bb_00634A00
  bb_006349E7 -->|branch| bb_006349FD
  bb_006349E7 -->|fallthrough| bb_006349F0
  bb_006349F0 -->|flow| bb_006349FD
  bb_006349FD -->|flow| bb_00634A00
  bb_00634A00 -->|branch| bb_006349E7
  bb_00634A00 -->|fallthrough| bb_00634A05
  bb_00634A05 -->|branch| bb_00634A16
  bb_00634A05 -->|fallthrough| bb_00634A0A
  bb_00634A0A -->|flow| bb_00634A16
```
