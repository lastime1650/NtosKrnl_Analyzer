# DifMmProbeAndLockProcessPagesWrapper

- RVA: `0x00636580`–`0x006366FB` (길이 `379` bytes)
- VA: `0x0000000140636580`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AC264`
- 디코드: `107`개 명령, `379/379` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006365B8` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006365E0` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063661D` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00636644` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063665D` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063666E` → [MmProbeAndLockProcessPages](../../page/9F/MmProbeAndLockProcessPages_function_009FE840.md) (function, `0x009FE840`)
- `0x00636697` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006366BE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006366D7` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006365F2` → RVA `0x00F048B8` (`.data`; read)
- `0x0063660A` → RVA `0x00F04980` (`.data`; read)
- `0x00636616` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0063666E` → [MmProbeAndLockProcessPages](../../page/9F/MmProbeAndLockProcessPages_function_009FE840.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00636580  48 8B C4                        mov rax, rsp
00636583  48 89 58 08                     mov qword ptr [rax + 8], rbx
00636587  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0063658B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063658F  57                              push rdi
00636590  41 54                           push r12
00636592  41 55                           push r13
00636594  41 56                           push r14
00636596  41 57                           push r15
00636598  48 83 EC 40                     sub rsp, 0x40
0063659C  0F 57 C0                        xorps xmm0, xmm0
0063659F  4C 8B E9                        mov r13, rcx
006365A2  B9 D8 00 00 00                  mov ecx, 0xd8
006365A7  45 8B F1                        mov r14d, r9d
006365AA  0F 11 40 B8                     movups xmmword ptr [rax - 0x48], xmm0
006365AE  45 8A F8                        mov r15b, r8b
006365B1  4C 8B E2                        mov r12, rdx
006365B4  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
006365B8  E8 77 F4 E5 FF                  call 0x140495a34
006365BD  48 8B F0                        mov rsi, rax
006365C0  48 85 C0                        test rax, rax
006365C3  0F 84 99 00 00 00               je 0x140636662
006365C9  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006365CC  A8 18                           test al, 0x18
006365CE  74 0C                           je 0x1406365dc
006365D0  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
006365D5  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006365DA  EB 0E                           jmp 0x1406365ea
006365DC  A8 04                           test al, 4
006365DE  74 0A                           je 0x1406365ea
006365E0  E8 23 D6 E9 FF                  call 0x1404d3c08
006365E5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006365EA  40 32 ED                        xor bpl, bpl
006365ED  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
006365F2  40 38 2D BF E2 8C 00            cmp byte ptr [rip + 0x8ce2bf], bpl
006365F9  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
006365FE  44 88 7C 24 2C                  mov byte ptr [rsp + 0x2c], r15b
00636603  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00636608  75 0C                           jne 0x140636616
0063660A  F7 05 6C E3 8C 00 00 08 00 00   test dword ptr [rip + 0x8ce36c], 0x800
00636614  74 13                           je 0x140636629
00636616  48 8D 0D 63 D8 8C 00            lea rcx, [rip + 0x8cd863]
0063661D  E8 FE FF BD FF                  call 0x140216620
00636622  40 8A E8                        mov bpl, al
00636625  84 C0                           test al, al
00636627  74 39                           je 0x140636662
00636629  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063662D  48 8B 1F                        mov rbx, qword ptr [rdi]
00636630  EB 1A                           jmp 0x14063664c
00636632  48 8D 43 F0                     lea rax, [rbx - 0x10]
00636636  48 85 C0                        test rax, rax
00636639  74 0E                           je 0x140636649
0063663B  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063663F  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00636644  E8 87 44 08 00                  call 0x1406baad0
00636649  48 8B 1B                        mov rbx, qword ptr [rbx]
0063664C  48 3B DF                        cmp rbx, rdi
0063664F  75 E1                           jne 0x140636632
00636651  40 84 ED                        test bpl, bpl
00636654  74 0C                           je 0x140636662
00636656  48 8D 0D 23 D8 8C 00            lea rcx, [rip + 0x8cd823]
0063665D  E8 1E 38 D1 FF                  call 0x140349e80
00636662  45 8B CE                        mov r9d, r14d
00636665  45 8A C7                        mov r8b, r15b
00636668  49 8B D4                        mov rdx, r12
0063666B  49 8B CD                        mov rcx, r13
0063666E  E8 CD 81 3C 00                  call 0x1409fe840
00636673  48 85 F6                        test rsi, rsi
00636676  74 64                           je 0x1406366dc
00636678  40 32 FF                        xor dil, dil
0063667B  40 38 3D 36 E2 8C 00            cmp byte ptr [rip + 0x8ce236], dil
00636682  75 0C                           jne 0x140636690
00636684  F7 05 F2 E2 8C 00 00 08 00 00   test dword ptr [rip + 0x8ce2f2], 0x800
0063668E  74 13                           je 0x1406366a3
00636690  48 8D 0D E9 D7 8C 00            lea rcx, [rip + 0x8cd7e9]
00636697  E8 84 FF BD FF                  call 0x140216620
0063669C  40 8A F8                        mov dil, al
0063669F  84 C0                           test al, al
006366A1  74 39                           je 0x1406366dc
006366A3  48 83 C6 30                     add rsi, 0x30
006366A7  48 8B 1E                        mov rbx, qword ptr [rsi]
006366AA  EB 1A                           jmp 0x1406366c6
006366AC  48 8D 43 F0                     lea rax, [rbx - 0x10]
006366B0  48 85 C0                        test rax, rax
006366B3  74 0E                           je 0x1406366c3
006366B5  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006366B9  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006366BE  E8 0D 44 08 00                  call 0x1406baad0
006366C3  48 8B 1B                        mov rbx, qword ptr [rbx]
006366C6  48 3B DE                        cmp rbx, rsi
006366C9  75 E1                           jne 0x1406366ac
006366CB  40 84 FF                        test dil, dil
006366CE  74 0C                           je 0x1406366dc
006366D0  48 8D 0D A9 D7 8C 00            lea rcx, [rip + 0x8cd7a9]
006366D7  E8 A4 37 D1 FF                  call 0x140349e80
006366DC  4C 8D 5C 24 40                  lea r11, [rsp + 0x40]
006366E1  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
006366E5  49 8B 6B 38                     mov rbp, qword ptr [r11 + 0x38]
006366E9  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
006366ED  49 8B E3                        mov rsp, r11
006366F0  41 5F                           pop r15
006366F2  41 5E                           pop r14
006366F4  41 5D                           pop r13
006366F6  41 5C                           pop r12
006366F8  5F                              pop rdi
006366F9  C3                              ret
006366FA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmProbeAndLockProcessPagesWrapper(__int64 a1, __int64 a2, unsigned __int8 a3, int a4)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int8 v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p0;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 72) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    result = DifGetAPIThunkContextById(216, a2, a3, a4);
    if (result == 0) goto loc_00636662;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006365DC;
    v_stack_m48 = v_stack_p0;
    goto loc_006365EA;
loc_006365DC:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m48 = result;
    }
    v_rbp = 0;
    v_stack_m30 = a1;
    v_stack_m38 = a2;
    v_stack_m3C = a3;
    v_stack_m40 = (unsigned int)((unsigned int)(a4));
    if ((*(unsigned __int8 *)(v_rip + 9233087)) != 0) goto loc_00636616;
    if (((*(unsigned int *)(v_rip + 9233260)) & (0x800ULL)) == 0) goto loc_00636629;
loc_00636616:
    result = ExAcquireRundownProtection(v_rip + 9230435, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00636662;
loc_00636629:
    goto loc_0063664C;
loc_00636632:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m48;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063664C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00636632;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9230371;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = MmProbeAndLockProcessPages(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if (result == 0) goto loc_006366DC;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9232950)) != 0) goto loc_00636690;
    if (((*(unsigned int *)(v_rip + 9233138)) & (0x800ULL)) == 0) goto loc_006366A3;
loc_00636690:
    result = ExAcquireRundownProtection(v_rip + 9230313, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_006366DC;
loc_006366A3:
    v_rsi = (result) + (48);
    goto loc_006366C6;
loc_006366AC:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m48;
        result = guard_dispatch_icall(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_006366C6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006366AC;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9230249;
        result = ExReleaseRundownProtection(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifMmProbeAndLockProcessPagesWrapper(int64_t Arg1, int64_t Arg2, uint8_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint8_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p0;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x48) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    result = DifGetAPIThunkContextById(216, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00636662;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006365DC;
    v_stack_m48 = v_stack_p0;
    goto loc_006365EA;
loc_006365DC:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m48 = result;
    }
    local_rbp = 0;
    v_stack_m30 = Arg1;
    v_stack_m38 = Arg2;
    v_stack_m3C = Arg3;
    v_stack_m40 = (uint32_t)((uint32_t)(Arg4));
    if ((*(uint8_t *)(v_rip + 0x8CE2BF)) != 0) goto loc_00636616;
    if (((*(uint32_t *)(v_rip + 0x8CE36C)) & (0x800ULL)) == 0) goto loc_00636629;
loc_00636616:
    result = ExAcquireRundownProtection(v_rip + 9230435, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00636662;
loc_00636629:
    goto loc_0063664C;
loc_00636632:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m48;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0063664C:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00636632;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9230371;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = MmProbeAndLockProcessPages(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if (result == 0) goto loc_006366DC;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CE236)) != 0) goto loc_00636690;
    if (((*(uint32_t *)(v_rip + 0x8CE2F2)) & (0x800ULL)) == 0) goto loc_006366A3;
loc_00636690:
    result = ExAcquireRundownProtection(v_rip + 9230313, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_006366DC;
loc_006366A3:
    local_rsi = (result) + (48);
    goto loc_006366C6;
loc_006366AC:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m48;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_006366C6:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006366AC;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9230249;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00636580&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00636580[BB_00636580]
  bb_006365C9[BB_006365C9]
  bb_006365D0[BB_006365D0]
  bb_006365DC[BB_006365DC]
  bb_006365E0[BB_006365E0]
  bb_006365EA[BB_006365EA]
  bb_0063660A[BB_0063660A]
  bb_00636616[BB_00636616]
  bb_00636629[BB_00636629]
  bb_00636632[BB_00636632]
  bb_0063663B[BB_0063663B]
  bb_00636649[BB_00636649]
  bb_0063664C[BB_0063664C]
  bb_00636651[BB_00636651]
  bb_00636656[BB_00636656]
  bb_00636662[BB_00636662]
  bb_00636678[BB_00636678]
  bb_00636684[BB_00636684]
  bb_00636690[BB_00636690]
  bb_006366A3[BB_006366A3]
  bb_006366AC[BB_006366AC]
  bb_006366B5[BB_006366B5]
  bb_006366C3[BB_006366C3]
  bb_006366C6[BB_006366C6]
  bb_006366CB[BB_006366CB]
  bb_006366D0[BB_006366D0]
  bb_006366DC[BB_006366DC]
  bb_006366FA[BB_006366FA]
  bb_00636580 -->|branch| bb_00636662
  bb_00636580 -->|fallthrough| bb_006365C9
  bb_006365C9 -->|branch| bb_006365DC
  bb_006365C9 -->|fallthrough| bb_006365D0
  bb_006365D0 -->|branch| bb_006365EA
  bb_006365DC -->|branch| bb_006365EA
  bb_006365DC -->|fallthrough| bb_006365E0
  bb_006365E0 -->|flow| bb_006365EA
  bb_006365EA -->|branch| bb_00636616
  bb_006365EA -->|fallthrough| bb_0063660A
  bb_0063660A -->|branch| bb_00636629
  bb_0063660A -->|fallthrough| bb_00636616
  bb_00636616 -->|branch| bb_00636662
  bb_00636616 -->|fallthrough| bb_00636629
  bb_00636629 -->|branch| bb_0063664C
  bb_00636632 -->|branch| bb_00636649
  bb_00636632 -->|fallthrough| bb_0063663B
  bb_0063663B -->|flow| bb_00636649
  bb_00636649 -->|flow| bb_0063664C
  bb_0063664C -->|branch| bb_00636632
  bb_0063664C -->|fallthrough| bb_00636651
  bb_00636651 -->|branch| bb_00636662
  bb_00636651 -->|fallthrough| bb_00636656
  bb_00636656 -->|flow| bb_00636662
  bb_00636662 -->|branch| bb_006366DC
  bb_00636662 -->|fallthrough| bb_00636678
  bb_00636678 -->|branch| bb_00636690
  bb_00636678 -->|fallthrough| bb_00636684
  bb_00636684 -->|branch| bb_006366A3
  bb_00636684 -->|fallthrough| bb_00636690
  bb_00636690 -->|branch| bb_006366DC
  bb_00636690 -->|fallthrough| bb_006366A3
  bb_006366A3 -->|branch| bb_006366C6
  bb_006366AC -->|branch| bb_006366C3
  bb_006366AC -->|fallthrough| bb_006366B5
  bb_006366B5 -->|flow| bb_006366C3
  bb_006366C3 -->|flow| bb_006366C6
  bb_006366C6 -->|branch| bb_006366AC
  bb_006366C6 -->|fallthrough| bb_006366CB
  bb_006366CB -->|branch| bb_006366DC
  bb_006366CB -->|fallthrough| bb_006366D0
  bb_006366D0 -->|flow| bb_006366DC
```
