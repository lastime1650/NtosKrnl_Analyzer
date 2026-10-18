# DifZwOpenSectionWrapper

- RVA: `0x00644850`–`0x006449C5` (길이 `373` bytes)
- VA: `0x0000000140644850`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9A64`
- 디코드: `108`개 명령, `373/373` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0064488C` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006448B2` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006448E6` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064490C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00644925` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00644933` → [ZwOpenSection](../6A/ZwOpenSection_function_006AD7B0.md) (function, `0x006AD7B0`)
- `0x0064495F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00644985` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064499E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006448C2` → RVA `0x00F048B8` (`.data`; read)
- `0x006448D3` → RVA `0x00F04980` (`.data`; read)
- `0x006448DF` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00644850  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00644855  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0064485A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0064485F  55                              push rbp
00644860  41 54                           push r12
00644862  41 55                           push r13
00644864  41 56                           push r14
00644866  41 57                           push r15
00644868  48 8B EC                        mov rbp, rsp
0064486B  48 83 EC 50                     sub rsp, 0x50
0064486F  33 C0                           xor eax, eax
00644871  0F 57 C0                        xorps xmm0, xmm0
00644874  4C 8B E9                        mov r13, rcx
00644877  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0064487B  4D 8B F8                        mov r15, r8
0064487E  44 8B E2                        mov r12d, edx
00644881  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00644885  8D 48 4B                        lea ecx, [rax + 0x4b]
00644888  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0064488C  E8 A3 11 E5 FF                  call 0x140495a34
00644891  48 8B F0                        mov rsi, rax
00644894  48 85 C0                        test rax, rax
00644897  0F 84 8D 00 00 00               je 0x14064492a
0064489D  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006448A0  A8 18                           test al, 0x18
006448A2  74 0A                           je 0x1406448ae
006448A4  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
006448A8  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
006448AC  EB 0D                           jmp 0x1406448bb
006448AE  A8 04                           test al, 4
006448B0  74 09                           je 0x1406448bb
006448B2  E8 51 F3 E8 FF                  call 0x1404d3c08
006448B7  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
006448BB  45 32 F6                        xor r14b, r14b
006448BE  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
006448C2  44 38 35 EF FF 8B 00            cmp byte ptr [rip + 0x8bffef], r14b
006448C9  44 89 65 E0                     mov dword ptr [rbp - 0x20], r12d
006448CD  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
006448D1  75 0C                           jne 0x1406448df
006448D3  F7 05 A3 00 8C 00 00 08 00 00   test dword ptr [rip + 0x8c00a3], 0x800
006448DD  74 13                           je 0x1406448f2
006448DF  48 8D 0D 9A F5 8B 00            lea rcx, [rip + 0x8bf59a]
006448E6  E8 35 1D BD FF                  call 0x140216620
006448EB  44 8A F0                        mov r14b, al
006448EE  84 C0                           test al, al
006448F0  74 38                           je 0x14064492a
006448F2  48 8D 7E 20                     lea rdi, [rsi + 0x20]
006448F6  48 8B 1F                        mov rbx, qword ptr [rdi]
006448F9  EB 19                           jmp 0x140644914
006448FB  48 8D 43 F0                     lea rax, [rbx - 0x10]
006448FF  48 85 C0                        test rax, rax
00644902  74 0D                           je 0x140644911
00644904  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00644908  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0064490C  E8 BF 61 07 00                  call 0x1406baad0
00644911  48 8B 1B                        mov rbx, qword ptr [rbx]
00644914  48 3B DF                        cmp rbx, rdi
00644917  75 E2                           jne 0x1406448fb
00644919  45 84 F6                        test r14b, r14b
0064491C  74 0C                           je 0x14064492a
0064491E  48 8D 0D 5B F5 8B 00            lea rcx, [rip + 0x8bf55b]
00644925  E8 56 55 D0 FF                  call 0x140349e80
0064492A  4D 8B C7                        mov r8, r15
0064492D  41 8B D4                        mov edx, r12d
00644930  49 8B CD                        mov rcx, r13
00644933  E8 78 8E 06 00                  call 0x1406ad7b0
00644938  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0064493B  48 85 F6                        test rsi, rsi
0064493E  74 63                           je 0x1406449a3
00644940  40 32 FF                        xor dil, dil
00644943  40 38 3D 6E FF 8B 00            cmp byte ptr [rip + 0x8bff6e], dil
0064494A  75 0C                           jne 0x140644958
0064494C  F7 05 2A 00 8C 00 00 08 00 00   test dword ptr [rip + 0x8c002a], 0x800
00644956  74 13                           je 0x14064496b
00644958  48 8D 0D 21 F5 8B 00            lea rcx, [rip + 0x8bf521]
0064495F  E8 BC 1C BD FF                  call 0x140216620
00644964  40 8A F8                        mov dil, al
00644967  84 C0                           test al, al
00644969  74 38                           je 0x1406449a3
0064496B  48 83 C6 30                     add rsi, 0x30
0064496F  48 8B 1E                        mov rbx, qword ptr [rsi]
00644972  EB 19                           jmp 0x14064498d
00644974  48 8D 43 F0                     lea rax, [rbx - 0x10]
00644978  48 85 C0                        test rax, rax
0064497B  74 0D                           je 0x14064498a
0064497D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00644981  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00644985  E8 46 61 07 00                  call 0x1406baad0
0064498A  48 8B 1B                        mov rbx, qword ptr [rbx]
0064498D  48 3B DE                        cmp rbx, rsi
00644990  75 E2                           jne 0x140644974
00644992  40 84 FF                        test dil, dil
00644995  74 0C                           je 0x1406449a3
00644997  48 8D 0D E2 F4 8B 00            lea rcx, [rip + 0x8bf4e2]
0064499E  E8 DD 54 D0 FF                  call 0x140349e80
006449A3  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
006449A6  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
006449AB  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
006449AF  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
006449B3  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
006449B7  49 8B E3                        mov rsp, r11
006449BA  41 5F                           pop r15
006449BC  41 5E                           pop r14
006449BE  41 5D                           pop r13
006449C0  41 5C                           pop r12
006449C2  5D                              pop rbp
006449C3  C3                              ret
006449C4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwOpenSectionWrapper(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(result + 75, a2, a3, a4);
    if (result == 0) goto loc_0064492A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006448AE;
    v_stack_m58 = v_stack_p0;
    goto loc_006448BB;
loc_006448AE:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9175023)) != 0) goto loc_006448DF;
    if (((*(unsigned int *)(v_rip + 9175203)) & (0x800ULL)) == 0) goto loc_006448F2;
loc_006448DF:
    result = ExAcquireRundownProtection(v_rip + 9172378, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064492A;
loc_006448F2:
    goto loc_00644914;
loc_006448FB:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00644914:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006448FB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9172315;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwOpenSection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_006449A3;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9174894)) != 0) goto loc_00644958;
    if (((*(unsigned int *)(v_rip + 9175082)) & (0x800ULL)) == 0) goto loc_0064496B;
loc_00644958:
    result = ExAcquireRundownProtection(v_rip + 9172257, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006449A3;
loc_0064496B:
    v_rsi = (result) + (48);
    goto loc_0064498D;
loc_00644974:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_0064498D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00644974;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9172194;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwOpenSectionWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(result + 75, Arg2, Arg3, a4);
    if (result == 0) goto loc_0064492A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006448AE;
    v_stack_m58 = v_stack_p0;
    goto loc_006448BB;
loc_006448AE:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8BFFEF)) != 0) goto loc_006448DF;
    if (((*(uint32_t *)(v_rip + 0x8C00A3)) & (0x800ULL)) == 0) goto loc_006448F2;
loc_006448DF:
    result = ExAcquireRundownProtection(v_rip + 9172378, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0064492A;
loc_006448F2:
    goto loc_00644914;
loc_006448FB:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00644914:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006448FB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9172315;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = ZwOpenSection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_006449A3;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BFF6E)) != 0) goto loc_00644958;
    if (((*(uint32_t *)(v_rip + 0x8C002A)) & (0x800ULL)) == 0) goto loc_0064496B;
loc_00644958:
    result = ExAcquireRundownProtection(v_rip + 9172257, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_006449A3;
loc_0064496B:
    local_rsi = (result) + (48);
    goto loc_0064498D;
loc_00644974:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
loc_0064498D:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00644974;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9172194;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00644850&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00644850[BB_00644850]
  bb_0064489D[BB_0064489D]
  bb_006448A4[BB_006448A4]
  bb_006448AE[BB_006448AE]
  bb_006448B2[BB_006448B2]
  bb_006448BB[BB_006448BB]
  bb_006448D3[BB_006448D3]
  bb_006448DF[BB_006448DF]
  bb_006448F2[BB_006448F2]
  bb_006448FB[BB_006448FB]
  bb_00644904[BB_00644904]
  bb_00644911[BB_00644911]
  bb_00644914[BB_00644914]
  bb_00644919[BB_00644919]
  bb_0064491E[BB_0064491E]
  bb_0064492A[BB_0064492A]
  bb_00644940[BB_00644940]
  bb_0064494C[BB_0064494C]
  bb_00644958[BB_00644958]
  bb_0064496B[BB_0064496B]
  bb_00644974[BB_00644974]
  bb_0064497D[BB_0064497D]
  bb_0064498A[BB_0064498A]
  bb_0064498D[BB_0064498D]
  bb_00644992[BB_00644992]
  bb_00644997[BB_00644997]
  bb_006449A3[BB_006449A3]
  bb_006449C4[BB_006449C4]
  bb_00644850 -->|branch| bb_0064492A
  bb_00644850 -->|fallthrough| bb_0064489D
  bb_0064489D -->|branch| bb_006448AE
  bb_0064489D -->|fallthrough| bb_006448A4
  bb_006448A4 -->|branch| bb_006448BB
  bb_006448AE -->|branch| bb_006448BB
  bb_006448AE -->|fallthrough| bb_006448B2
  bb_006448B2 -->|flow| bb_006448BB
  bb_006448BB -->|branch| bb_006448DF
  bb_006448BB -->|fallthrough| bb_006448D3
  bb_006448D3 -->|branch| bb_006448F2
  bb_006448D3 -->|fallthrough| bb_006448DF
  bb_006448DF -->|branch| bb_0064492A
  bb_006448DF -->|fallthrough| bb_006448F2
  bb_006448F2 -->|branch| bb_00644914
  bb_006448FB -->|branch| bb_00644911
  bb_006448FB -->|fallthrough| bb_00644904
  bb_00644904 -->|flow| bb_00644911
  bb_00644911 -->|flow| bb_00644914
  bb_00644914 -->|branch| bb_006448FB
  bb_00644914 -->|fallthrough| bb_00644919
  bb_00644919 -->|branch| bb_0064492A
  bb_00644919 -->|fallthrough| bb_0064491E
  bb_0064491E -->|flow| bb_0064492A
  bb_0064492A -->|branch| bb_006449A3
  bb_0064492A -->|fallthrough| bb_00644940
  bb_00644940 -->|branch| bb_00644958
  bb_00644940 -->|fallthrough| bb_0064494C
  bb_0064494C -->|branch| bb_0064496B
  bb_0064494C -->|fallthrough| bb_00644958
  bb_00644958 -->|branch| bb_006449A3
  bb_00644958 -->|fallthrough| bb_0064496B
  bb_0064496B -->|branch| bb_0064498D
  bb_00644974 -->|branch| bb_0064498A
  bb_00644974 -->|fallthrough| bb_0064497D
  bb_0064497D -->|flow| bb_0064498A
  bb_0064498A -->|flow| bb_0064498D
  bb_0064498D -->|branch| bb_00644974
  bb_0064498D -->|fallthrough| bb_00644992
  bb_00644992 -->|branch| bb_006449A3
  bb_00644992 -->|fallthrough| bb_00644997
  bb_00644997 -->|flow| bb_006449A3
```
