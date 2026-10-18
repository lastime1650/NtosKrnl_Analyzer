# DifZwDuplicateTokenWrapper

- RVA: `0x00641560`–`0x00641709` (길이 `425` bytes)
- VA: `0x0000000140641560`
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
- `0x006415A4` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006415CC` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00641616` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064163C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00641655` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00641677` → [ZwDuplicateToken](../6A/ZwDuplicateToken_function_006AD910.md) (function, `0x006AD910`)
- `0x006416A3` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006416C9` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006416E2` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006415DC` → RVA `0x00F048B8` (`.data`; read)
- `0x00641603` → RVA `0x00F04980` (`.data`; read)
- `0x0064160F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00641560  48 8B C4                        mov rax, rsp
00641563  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00641567  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064156B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0064156F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00641573  55                              push rbp
00641574  41 54                           push r12
00641576  41 55                           push r13
00641578  41 56                           push r14
0064157A  41 57                           push r15
0064157C  48 8B EC                        mov rbp, rsp
0064157F  48 83 EC 70                     sub rsp, 0x70
00641583  33 C0                           xor eax, eax
00641585  0F 57 C0                        xorps xmm0, xmm0
00641588  45 8A F9                        mov r15b, r9b
0064158B  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0064158F  4D 8B E0                        mov r12, r8
00641592  44 8B EA                        mov r13d, edx
00641595  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00641599  8D 48 6B                        lea ecx, [rax + 0x6b]
0064159C  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
006415A0  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
006415A4  E8 8B 44 E5 FF                  call 0x140495a34
006415A9  4C 8B F0                        mov r14, rax
006415AC  48 85 C0                        test rax, rax
006415AF  0F 84 A5 00 00 00               je 0x14064165a
006415B5  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
006415B8  F6 C1 18                        test cl, 0x18
006415BB  74 0A                           je 0x1406415c7
006415BD  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
006415C1  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
006415C5  EB 0E                           jmp 0x1406415d5
006415C7  F6 C1 04                        test cl, 4
006415CA  74 09                           je 0x1406415d5
006415CC  E8 37 26 E9 FF                  call 0x1404d3c08
006415D1  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
006415D5  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
006415D9  40 32 F6                        xor sil, sil
006415DC  40 38 35 D5 32 8C 00            cmp byte ptr [rip + 0x8c32d5], sil
006415E3  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
006415E7  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
006415EA  89 45 D0                        mov dword ptr [rbp - 0x30], eax
006415ED  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
006415F1  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
006415F5  44 89 6D E0                     mov dword ptr [rbp - 0x20], r13d
006415F9  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
006415FD  44 88 7D D4                     mov byte ptr [rbp - 0x2c], r15b
00641601  75 0C                           jne 0x14064160f
00641603  F7 05 73 33 8C 00 00 08 00 00   test dword ptr [rip + 0x8c3373], 0x800
0064160D  74 13                           je 0x140641622
0064160F  48 8D 0D 6A 28 8C 00            lea rcx, [rip + 0x8c286a]
00641616  E8 05 50 BD FF                  call 0x140216620
0064161B  40 8A F0                        mov sil, al
0064161E  84 C0                           test al, al
00641620  74 38                           je 0x14064165a
00641622  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00641626  48 8B 1F                        mov rbx, qword ptr [rdi]
00641629  EB 19                           jmp 0x140641644
0064162B  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064162F  48 85 C0                        test rax, rax
00641632  74 0D                           je 0x140641641
00641634  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00641638  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0064163C  E8 8F 94 07 00                  call 0x1406baad0
00641641  48 8B 1B                        mov rbx, qword ptr [rbx]
00641644  48 3B DF                        cmp rbx, rdi
00641647  75 E2                           jne 0x14064162b
00641649  40 84 F6                        test sil, sil
0064164C  74 0C                           je 0x14064165a
0064164E  48 8D 0D 2B 28 8C 00            lea rcx, [rip + 0x8c282b]
00641655  E8 26 88 D0 FF                  call 0x140349e80
0064165A  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0064165E  45 8A CF                        mov r9b, r15b
00641661  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00641665  4D 8B C4                        mov r8, r12
00641668  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0064166D  41 8B D5                        mov edx, r13d
00641670  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00641673  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00641677  E8 94 C2 06 00                  call 0x1406ad910
0064167C  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0064167F  4D 85 F6                        test r14, r14
00641682  74 63                           je 0x1406416e7
00641684  40 32 FF                        xor dil, dil
00641687  40 38 3D 2A 32 8C 00            cmp byte ptr [rip + 0x8c322a], dil
0064168E  75 0C                           jne 0x14064169c
00641690  F7 05 E6 32 8C 00 00 08 00 00   test dword ptr [rip + 0x8c32e6], 0x800
0064169A  74 13                           je 0x1406416af
0064169C  48 8D 0D DD 27 8C 00            lea rcx, [rip + 0x8c27dd]
006416A3  E8 78 4F BD FF                  call 0x140216620
006416A8  40 8A F8                        mov dil, al
006416AB  84 C0                           test al, al
006416AD  74 38                           je 0x1406416e7
006416AF  49 8D 76 30                     lea rsi, [r14 + 0x30]
006416B3  48 8B 1E                        mov rbx, qword ptr [rsi]
006416B6  EB 19                           jmp 0x1406416d1
006416B8  48 8D 43 F0                     lea rax, [rbx - 0x10]
006416BC  48 85 C0                        test rax, rax
006416BF  74 0D                           je 0x1406416ce
006416C1  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006416C5  48 8D 4D C0                     lea rcx, [rbp - 0x40]
006416C9  E8 02 94 07 00                  call 0x1406baad0
006416CE  48 8B 1B                        mov rbx, qword ptr [rbx]
006416D1  48 3B DE                        cmp rbx, rsi
006416D4  75 E2                           jne 0x1406416b8
006416D6  40 84 FF                        test dil, dil
006416D9  74 0C                           je 0x1406416e7
006416DB  48 8D 0D 9E 27 8C 00            lea rcx, [rip + 0x8c279e]
006416E2  E8 99 87 D0 FF                  call 0x140349e80
006416E7  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
006416EA  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
006416EF  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
006416F3  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
006416F7  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
006416FB  49 8B E3                        mov rsp, r11
006416FE  41 5F                           pop r15
00641700  41 5E                           pop r14
00641702  41 5D                           pop r13
00641704  41 5C                           pop r12
00641706  5D                              pop rbp
00641707  C3                              ret
00641708  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwDuplicateTokenWrapper(__int64 a1, int a2, __int64 a3, unsigned __int8 a4, unsigned int a5, __int64 a6)
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
    unsigned __int8 v_stack_m54;
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
    result = DifGetAPIThunkContextById(result + 107, a2, a3, a4);
    if (result == 0) goto loc_0064165A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006415C7;
    v_stack_m68 = v_stack_p0;
    goto loc_006415D5;
loc_006415C7:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m68 = result;
    }
    v_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m58 = (unsigned int)((unsigned int)(a5));
    v_stack_m60 = a6;
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    v_stack_m50 = a3;
    v_stack_m54 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9188053)) != 0) goto loc_0064160F;
    if (((*(unsigned int *)(v_rip + 9188211)) & (0x800ULL)) == 0) goto loc_00641622;
loc_0064160F:
    result = ExAcquireRundownProtection(v_rip + 9185386, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064165A;
loc_00641622:
    goto loc_00641644;
loc_0064162B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00641644:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0064162B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9185323;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m70 = a6;
    v_stack_m78 = (unsigned int)((unsigned int)(a5));
    result = ZwDuplicateToken(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_006416E7;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9187882)) != 0) goto loc_0064169C;
    if (((*(unsigned int *)(v_rip + 9188070)) & (0x800ULL)) == 0) goto loc_006416AF;
loc_0064169C:
    result = ExAcquireRundownProtection(v_rip + 9185245, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006416E7;
loc_006416AF:
    goto loc_006416D1;
loc_006416B8:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_006416D1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_006416B8;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9185182;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwDuplicateTokenWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, uint8_t Arg4, uint32_t Arg5, int64_t Arg6)
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
    uint8_t v_stack_m54;
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
    result = DifGetAPIThunkContextById(result + 107, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0064165A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006415C7;
    v_stack_m68 = v_stack_p0;
    goto loc_006415D5;
loc_006415C7:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m68 = result;
    }
    local_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m58 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m60 = Arg6;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m50 = Arg3;
    v_stack_m54 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8C32D5)) != 0) goto loc_0064160F;
    if (((*(uint32_t *)(v_rip + 0x8C3373)) & (0x800ULL)) == 0) goto loc_00641622;
loc_0064160F:
    result = ExAcquireRundownProtection(v_rip + 9185386, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0064165A;
loc_00641622:
    goto loc_00641644;
loc_0064162B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00641644:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0064162B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9185323;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m70 = Arg6;
    v_stack_m78 = (uint32_t)((uint32_t)(Arg5));
    result = ZwDuplicateToken(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_006416E7;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C322A)) != 0) goto loc_0064169C;
    if (((*(uint32_t *)(v_rip + 0x8C32E6)) & (0x800ULL)) == 0) goto loc_006416AF;
loc_0064169C:
    result = ExAcquireRundownProtection(v_rip + 9185245, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_006416E7;
loc_006416AF:
    goto loc_006416D1;
loc_006416B8:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
loc_006416D1:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_006416B8;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9185182;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00641560&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00641560[BB_00641560]
  bb_006415B5[BB_006415B5]
  bb_006415BD[BB_006415BD]
  bb_006415C7[BB_006415C7]
  bb_006415CC[BB_006415CC]
  bb_006415D5[BB_006415D5]
  bb_00641603[BB_00641603]
  bb_0064160F[BB_0064160F]
  bb_00641622[BB_00641622]
  bb_0064162B[BB_0064162B]
  bb_00641634[BB_00641634]
  bb_00641641[BB_00641641]
  bb_00641644[BB_00641644]
  bb_00641649[BB_00641649]
  bb_0064164E[BB_0064164E]
  bb_0064165A[BB_0064165A]
  bb_00641684[BB_00641684]
  bb_00641690[BB_00641690]
  bb_0064169C[BB_0064169C]
  bb_006416AF[BB_006416AF]
  bb_006416B8[BB_006416B8]
  bb_006416C1[BB_006416C1]
  bb_006416CE[BB_006416CE]
  bb_006416D1[BB_006416D1]
  bb_006416D6[BB_006416D6]
  bb_006416DB[BB_006416DB]
  bb_006416E7[BB_006416E7]
  bb_00641708[BB_00641708]
  bb_00641560 -->|branch| bb_0064165A
  bb_00641560 -->|fallthrough| bb_006415B5
  bb_006415B5 -->|branch| bb_006415C7
  bb_006415B5 -->|fallthrough| bb_006415BD
  bb_006415BD -->|branch| bb_006415D5
  bb_006415C7 -->|branch| bb_006415D5
  bb_006415C7 -->|fallthrough| bb_006415CC
  bb_006415CC -->|flow| bb_006415D5
  bb_006415D5 -->|branch| bb_0064160F
  bb_006415D5 -->|fallthrough| bb_00641603
  bb_00641603 -->|branch| bb_00641622
  bb_00641603 -->|fallthrough| bb_0064160F
  bb_0064160F -->|branch| bb_0064165A
  bb_0064160F -->|fallthrough| bb_00641622
  bb_00641622 -->|branch| bb_00641644
  bb_0064162B -->|branch| bb_00641641
  bb_0064162B -->|fallthrough| bb_00641634
  bb_00641634 -->|flow| bb_00641641
  bb_00641641 -->|flow| bb_00641644
  bb_00641644 -->|branch| bb_0064162B
  bb_00641644 -->|fallthrough| bb_00641649
  bb_00641649 -->|branch| bb_0064165A
  bb_00641649 -->|fallthrough| bb_0064164E
  bb_0064164E -->|flow| bb_0064165A
  bb_0064165A -->|branch| bb_006416E7
  bb_0064165A -->|fallthrough| bb_00641684
  bb_00641684 -->|branch| bb_0064169C
  bb_00641684 -->|fallthrough| bb_00641690
  bb_00641690 -->|branch| bb_006416AF
  bb_00641690 -->|fallthrough| bb_0064169C
  bb_0064169C -->|branch| bb_006416E7
  bb_0064169C -->|fallthrough| bb_006416AF
  bb_006416AF -->|branch| bb_006416D1
  bb_006416B8 -->|branch| bb_006416CE
  bb_006416B8 -->|fallthrough| bb_006416C1
  bb_006416C1 -->|flow| bb_006416CE
  bb_006416CE -->|flow| bb_006416D1
  bb_006416D1 -->|branch| bb_006416B8
  bb_006416D1 -->|fallthrough| bb_006416D6
  bb_006416D6 -->|branch| bb_006416E7
  bb_006416D6 -->|fallthrough| bb_006416DB
  bb_006416DB -->|flow| bb_006416E7
```
