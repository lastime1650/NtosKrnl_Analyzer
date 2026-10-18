# DifZwOpenTransactionManagerWrapper

- RVA: `0x00645190`–`0x00645335` (길이 `421` bytes)
- VA: `0x0000000140645190`
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
- `0x006451C6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x006451D0` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006451F8` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00645242` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00645268` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00645281` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006452A3` → [ZwOpenTransactionManager](../6A/ZwOpenTransactionManager_function_006AF870.md) (function, `0x006AF870`)
- `0x006452CF` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006452F5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064530E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00645208` → RVA `0x00F048B8` (`.data`; read)
- `0x0064522F` → RVA `0x00F04980` (`.data`; read)
- `0x0064523B` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00645190  48 8B C4                        mov rax, rsp
00645193  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00645197  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064519B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0064519F  48 89 48 08                     mov qword ptr [rax + 8], rcx
006451A3  55                              push rbp
006451A4  41 54                           push r12
006451A6  41 55                           push r13
006451A8  41 56                           push r14
006451AA  41 57                           push r15
006451AC  48 8B EC                        mov rbp, rsp
006451AF  48 83 EC 70                     sub rsp, 0x70
006451B3  44 8B EA                        mov r13d, edx
006451B6  48 8D 4D C0                     lea rcx, [rbp - 0x40]
006451BA  33 D2                           xor edx, edx
006451BC  4D 8B E0                        mov r12, r8
006451BF  4D 8B F9                        mov r15, r9
006451C2  44 8D 42 40                     lea r8d, [rdx + 0x40]
006451C6  E8 75 1A 08 00                  call 0x1406c6c40
006451CB  B9 44 00 00 00                  mov ecx, 0x44
006451D0  E8 5F 08 E5 FF                  call 0x140495a34
006451D5  4C 8B F0                        mov r14, rax
006451D8  48 85 C0                        test rax, rax
006451DB  0F 84 A5 00 00 00               je 0x140645286
006451E1  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
006451E4  F6 C1 18                        test cl, 0x18
006451E7  74 0A                           je 0x1406451f3
006451E9  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
006451ED  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
006451F1  EB 0E                           jmp 0x140645201
006451F3  F6 C1 04                        test cl, 4
006451F6  74 09                           je 0x140645201
006451F8  E8 0B EA E8 FF                  call 0x1404d3c08
006451FD  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00645201  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00645205  40 32 F6                        xor sil, sil
00645208  40 38 35 A9 F6 8B 00            cmp byte ptr [rip + 0x8bf6a9], sil
0064520F  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00645213  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00645217  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0064521B  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
0064521E  89 45 C8                        mov dword ptr [rbp - 0x38], eax
00645221  44 89 6D E8                     mov dword ptr [rbp - 0x18], r13d
00645225  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
00645229  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
0064522D  75 0C                           jne 0x14064523b
0064522F  F7 05 47 F7 8B 00 00 08 00 00   test dword ptr [rip + 0x8bf747], 0x800
00645239  74 13                           je 0x14064524e
0064523B  48 8D 0D 3E EC 8B 00            lea rcx, [rip + 0x8bec3e]
00645242  E8 D9 13 BD FF                  call 0x140216620
00645247  40 8A F0                        mov sil, al
0064524A  84 C0                           test al, al
0064524C  74 38                           je 0x140645286
0064524E  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00645252  48 8B 1F                        mov rbx, qword ptr [rdi]
00645255  EB 19                           jmp 0x140645270
00645257  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064525B  48 85 C0                        test rax, rax
0064525E  74 0D                           je 0x14064526d
00645260  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00645264  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00645268  E8 63 58 07 00                  call 0x1406baad0
0064526D  48 8B 1B                        mov rbx, qword ptr [rbx]
00645270  48 3B DF                        cmp rbx, rdi
00645273  75 E2                           jne 0x140645257
00645275  40 84 F6                        test sil, sil
00645278  74 0C                           je 0x140645286
0064527A  48 8D 0D FF EB 8B 00            lea rcx, [rip + 0x8bebff]
00645281  E8 FA 4B D0 FF                  call 0x140349e80
00645286  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
00645289  4D 8B CF                        mov r9, r15
0064528C  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00645290  4D 8B C4                        mov r8, r12
00645293  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00645297  41 8B D5                        mov edx, r13d
0064529A  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0064529E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006452A3  E8 C8 A5 06 00                  call 0x1406af870
006452A8  89 45 F8                        mov dword ptr [rbp - 8], eax
006452AB  4D 85 F6                        test r14, r14
006452AE  74 63                           je 0x140645313
006452B0  40 32 FF                        xor dil, dil
006452B3  40 38 3D FE F5 8B 00            cmp byte ptr [rip + 0x8bf5fe], dil
006452BA  75 0C                           jne 0x1406452c8
006452BC  F7 05 BA F6 8B 00 00 08 00 00   test dword ptr [rip + 0x8bf6ba], 0x800
006452C6  74 13                           je 0x1406452db
006452C8  48 8D 0D B1 EB 8B 00            lea rcx, [rip + 0x8bebb1]
006452CF  E8 4C 13 BD FF                  call 0x140216620
006452D4  40 8A F8                        mov dil, al
006452D7  84 C0                           test al, al
006452D9  74 38                           je 0x140645313
006452DB  49 8D 76 30                     lea rsi, [r14 + 0x30]
006452DF  48 8B 1E                        mov rbx, qword ptr [rsi]
006452E2  EB 19                           jmp 0x1406452fd
006452E4  48 8D 43 F0                     lea rax, [rbx - 0x10]
006452E8  48 85 C0                        test rax, rax
006452EB  74 0D                           je 0x1406452fa
006452ED  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006452F1  48 8D 4D C0                     lea rcx, [rbp - 0x40]
006452F5  E8 D6 57 07 00                  call 0x1406baad0
006452FA  48 8B 1B                        mov rbx, qword ptr [rbx]
006452FD  48 3B DE                        cmp rbx, rsi
00645300  75 E2                           jne 0x1406452e4
00645302  40 84 FF                        test dil, dil
00645305  74 0C                           je 0x140645313
00645307  48 8D 0D 72 EB 8B 00            lea rcx, [rip + 0x8beb72]
0064530E  E8 6D 4B D0 FF                  call 0x140349e80
00645313  8B 45 F8                        mov eax, dword ptr [rbp - 8]
00645316  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
0064531B  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0064531F  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00645323  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00645327  49 8B E3                        mov rsp, r11
0064532A  41 5F                           pop r15
0064532C  41 5E                           pop r14
0064532E  41 5D                           pop r13
00645330  41 5C                           pop r12
00645332  5D                              pop rbp
00645333  C3                              ret
00645334  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwOpenTransactionManagerWrapper(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (112);
    a2 = 0;
    result = memset(v_stack_m68, a2, a2 + 64, a4);
    result = DifGetAPIThunkContextById(68, a2, a2 + 64, a4);
    if (result == 0) goto loc_00645286;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006451F3;
    v_stack_m68 = v_stack_p0;
    goto loc_00645201;
loc_006451F3:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a2 + 64, a4);
        v_stack_m68 = result;
    }
    v_rsi = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m58 = a5;
    v_stack_m60 = (unsigned int)((unsigned int)(a6));
    v_stack_m40 = (unsigned int)((unsigned int)(a2));
    v_stack_m48 = a3;
    v_stack_m50 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9172649)) != 0) goto loc_0064523B;
    if (((*(unsigned int *)(v_rip + 9172807)) & (0x800ULL)) == 0) goto loc_0064524E;
loc_0064523B:
    result = ExAcquireRundownProtection(v_rip + 9169982, a2, a2 + 64, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00645286;
loc_0064524E:
    goto loc_00645270;
loc_00645257:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a2 + 64, a4);
    }
loc_00645270:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00645257;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9169919;
        result = ExReleaseRundownProtection(a1, a2, a2 + 64, a4);
    }
    v_stack_m70 = (unsigned int)((unsigned int)(a6));
    v_stack_m78 = a5;
    result = ZwOpenTransactionManager(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_00645313;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9172478)) != 0) goto loc_006452C8;
    if (((*(unsigned int *)(v_rip + 9172666)) & (0x800ULL)) == 0) goto loc_006452DB;
loc_006452C8:
    result = ExAcquireRundownProtection(v_rip + 9169841, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00645313;
loc_006452DB:
    goto loc_006452FD;
loc_006452E4:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_006452FD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_006452E4;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9169778;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwOpenTransactionManagerWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (112);
    Arg2 = 0;
    result = memset(v_stack_m68, Arg2, Arg2 + 64, Arg4);
    result = DifGetAPIThunkContextById(68, Arg2, Arg2 + 64, Arg4);
    if (result == 0) goto loc_00645286;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006451F3;
    v_stack_m68 = v_stack_p0;
    goto loc_00645201;
loc_006451F3:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg2 + 64, Arg4);
        v_stack_m68 = result;
    }
    local_rsi = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m58 = Arg5;
    v_stack_m60 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m40 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m48 = Arg3;
    v_stack_m50 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8BF6A9)) != 0) goto loc_0064523B;
    if (((*(uint32_t *)(v_rip + 0x8BF747)) & (0x800ULL)) == 0) goto loc_0064524E;
loc_0064523B:
    result = ExAcquireRundownProtection(v_rip + 9169982, Arg2, Arg2 + 64, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00645286;
loc_0064524E:
    goto loc_00645270;
loc_00645257:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg2 + 64, Arg4);
    }
loc_00645270:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00645257;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9169919;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg2 + 64, Arg4);
    }
    v_stack_m70 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m78 = Arg5;
    result = ZwOpenTransactionManager(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_00645313;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BF5FE)) != 0) goto loc_006452C8;
    if (((*(uint32_t *)(v_rip + 0x8BF6BA)) & (0x800ULL)) == 0) goto loc_006452DB;
loc_006452C8:
    result = ExAcquireRundownProtection(v_rip + 9169841, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00645313;
loc_006452DB:
    goto loc_006452FD;
loc_006452E4:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
loc_006452FD:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_006452E4;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9169778;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00645190&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00645190[BB_00645190]
  bb_006451E1[BB_006451E1]
  bb_006451E9[BB_006451E9]
  bb_006451F3[BB_006451F3]
  bb_006451F8[BB_006451F8]
  bb_00645201[BB_00645201]
  bb_0064522F[BB_0064522F]
  bb_0064523B[BB_0064523B]
  bb_0064524E[BB_0064524E]
  bb_00645257[BB_00645257]
  bb_00645260[BB_00645260]
  bb_0064526D[BB_0064526D]
  bb_00645270[BB_00645270]
  bb_00645275[BB_00645275]
  bb_0064527A[BB_0064527A]
  bb_00645286[BB_00645286]
  bb_006452B0[BB_006452B0]
  bb_006452BC[BB_006452BC]
  bb_006452C8[BB_006452C8]
  bb_006452DB[BB_006452DB]
  bb_006452E4[BB_006452E4]
  bb_006452ED[BB_006452ED]
  bb_006452FA[BB_006452FA]
  bb_006452FD[BB_006452FD]
  bb_00645302[BB_00645302]
  bb_00645307[BB_00645307]
  bb_00645313[BB_00645313]
  bb_00645334[BB_00645334]
  bb_00645190 -->|branch| bb_00645286
  bb_00645190 -->|fallthrough| bb_006451E1
  bb_006451E1 -->|branch| bb_006451F3
  bb_006451E1 -->|fallthrough| bb_006451E9
  bb_006451E9 -->|branch| bb_00645201
  bb_006451F3 -->|branch| bb_00645201
  bb_006451F3 -->|fallthrough| bb_006451F8
  bb_006451F8 -->|flow| bb_00645201
  bb_00645201 -->|branch| bb_0064523B
  bb_00645201 -->|fallthrough| bb_0064522F
  bb_0064522F -->|branch| bb_0064524E
  bb_0064522F -->|fallthrough| bb_0064523B
  bb_0064523B -->|branch| bb_00645286
  bb_0064523B -->|fallthrough| bb_0064524E
  bb_0064524E -->|branch| bb_00645270
  bb_00645257 -->|branch| bb_0064526D
  bb_00645257 -->|fallthrough| bb_00645260
  bb_00645260 -->|flow| bb_0064526D
  bb_0064526D -->|flow| bb_00645270
  bb_00645270 -->|branch| bb_00645257
  bb_00645270 -->|fallthrough| bb_00645275
  bb_00645275 -->|branch| bb_00645286
  bb_00645275 -->|fallthrough| bb_0064527A
  bb_0064527A -->|flow| bb_00645286
  bb_00645286 -->|branch| bb_00645313
  bb_00645286 -->|fallthrough| bb_006452B0
  bb_006452B0 -->|branch| bb_006452C8
  bb_006452B0 -->|fallthrough| bb_006452BC
  bb_006452BC -->|branch| bb_006452DB
  bb_006452BC -->|fallthrough| bb_006452C8
  bb_006452C8 -->|branch| bb_00645313
  bb_006452C8 -->|fallthrough| bb_006452DB
  bb_006452DB -->|branch| bb_006452FD
  bb_006452E4 -->|branch| bb_006452FA
  bb_006452E4 -->|fallthrough| bb_006452ED
  bb_006452ED -->|flow| bb_006452FA
  bb_006452FA -->|flow| bb_006452FD
  bb_006452FD -->|branch| bb_006452E4
  bb_006452FD -->|fallthrough| bb_00645302
  bb_00645302 -->|branch| bb_00645313
  bb_00645302 -->|fallthrough| bb_00645307
  bb_00645307 -->|flow| bb_00645313
```
