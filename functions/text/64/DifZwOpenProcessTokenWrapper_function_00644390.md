# DifZwOpenProcessTokenWrapper

- RVA: `0x00644390`–`0x00644505` (길이 `373` bytes)
- VA: `0x0000000140644390`
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
- `0x006443CC` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006443F2` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00644426` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064444C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00644465` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00644473` → [ZwOpenProcessToken](../6A/ZwOpenProcessToken_function_006AF750.md) (function, `0x006AF750`)
- `0x0064449F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006444C5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006444DE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00644402` → RVA `0x00F048B8` (`.data`; read)
- `0x00644413` → RVA `0x00F04980` (`.data`; read)
- `0x0064441F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00644390  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00644395  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0064439A  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0064439F  55                              push rbp
006443A0  41 54                           push r12
006443A2  41 55                           push r13
006443A4  41 56                           push r14
006443A6  41 57                           push r15
006443A8  48 8B EC                        mov rbp, rsp
006443AB  48 83 EC 50                     sub rsp, 0x50
006443AF  33 C0                           xor eax, eax
006443B1  0F 57 C0                        xorps xmm0, xmm0
006443B4  4C 8B E9                        mov r13, rcx
006443B7  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
006443BB  4D 8B F8                        mov r15, r8
006443BE  44 8B E2                        mov r12d, edx
006443C1  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
006443C5  8D 48 4E                        lea ecx, [rax + 0x4e]
006443C8  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
006443CC  E8 63 16 E5 FF                  call 0x140495a34
006443D1  48 8B F0                        mov rsi, rax
006443D4  48 85 C0                        test rax, rax
006443D7  0F 84 8D 00 00 00               je 0x14064446a
006443DD  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006443E0  A8 18                           test al, 0x18
006443E2  74 0A                           je 0x1406443ee
006443E4  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
006443E8  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
006443EC  EB 0D                           jmp 0x1406443fb
006443EE  A8 04                           test al, 4
006443F0  74 09                           je 0x1406443fb
006443F2  E8 11 F8 E8 FF                  call 0x1404d3c08
006443F7  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
006443FB  45 32 F6                        xor r14b, r14b
006443FE  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
00644402  44 38 35 AF 04 8C 00            cmp byte ptr [rip + 0x8c04af], r14b
00644409  44 89 65 E0                     mov dword ptr [rbp - 0x20], r12d
0064440D  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
00644411  75 0C                           jne 0x14064441f
00644413  F7 05 63 05 8C 00 00 08 00 00   test dword ptr [rip + 0x8c0563], 0x800
0064441D  74 13                           je 0x140644432
0064441F  48 8D 0D 5A FA 8B 00            lea rcx, [rip + 0x8bfa5a]
00644426  E8 F5 21 BD FF                  call 0x140216620
0064442B  44 8A F0                        mov r14b, al
0064442E  84 C0                           test al, al
00644430  74 38                           je 0x14064446a
00644432  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00644436  48 8B 1F                        mov rbx, qword ptr [rdi]
00644439  EB 19                           jmp 0x140644454
0064443B  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064443F  48 85 C0                        test rax, rax
00644442  74 0D                           je 0x140644451
00644444  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00644448  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0064444C  E8 7F 66 07 00                  call 0x1406baad0
00644451  48 8B 1B                        mov rbx, qword ptr [rbx]
00644454  48 3B DF                        cmp rbx, rdi
00644457  75 E2                           jne 0x14064443b
00644459  45 84 F6                        test r14b, r14b
0064445C  74 0C                           je 0x14064446a
0064445E  48 8D 0D 1B FA 8B 00            lea rcx, [rip + 0x8bfa1b]
00644465  E8 16 5A D0 FF                  call 0x140349e80
0064446A  4D 8B C7                        mov r8, r15
0064446D  41 8B D4                        mov edx, r12d
00644470  49 8B CD                        mov rcx, r13
00644473  E8 D8 B2 06 00                  call 0x1406af750
00644478  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0064447B  48 85 F6                        test rsi, rsi
0064447E  74 63                           je 0x1406444e3
00644480  40 32 FF                        xor dil, dil
00644483  40 38 3D 2E 04 8C 00            cmp byte ptr [rip + 0x8c042e], dil
0064448A  75 0C                           jne 0x140644498
0064448C  F7 05 EA 04 8C 00 00 08 00 00   test dword ptr [rip + 0x8c04ea], 0x800
00644496  74 13                           je 0x1406444ab
00644498  48 8D 0D E1 F9 8B 00            lea rcx, [rip + 0x8bf9e1]
0064449F  E8 7C 21 BD FF                  call 0x140216620
006444A4  40 8A F8                        mov dil, al
006444A7  84 C0                           test al, al
006444A9  74 38                           je 0x1406444e3
006444AB  48 83 C6 30                     add rsi, 0x30
006444AF  48 8B 1E                        mov rbx, qword ptr [rsi]
006444B2  EB 19                           jmp 0x1406444cd
006444B4  48 8D 43 F0                     lea rax, [rbx - 0x10]
006444B8  48 85 C0                        test rax, rax
006444BB  74 0D                           je 0x1406444ca
006444BD  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006444C1  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006444C5  E8 06 66 07 00                  call 0x1406baad0
006444CA  48 8B 1B                        mov rbx, qword ptr [rbx]
006444CD  48 3B DE                        cmp rbx, rsi
006444D0  75 E2                           jne 0x1406444b4
006444D2  40 84 FF                        test dil, dil
006444D5  74 0C                           je 0x1406444e3
006444D7  48 8D 0D A2 F9 8B 00            lea rcx, [rip + 0x8bf9a2]
006444DE  E8 9D 59 D0 FF                  call 0x140349e80
006444E3  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
006444E6  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
006444EB  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
006444EF  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
006444F3  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
006444F7  49 8B E3                        mov rsp, r11
006444FA  41 5F                           pop r15
006444FC  41 5E                           pop r14
006444FE  41 5D                           pop r13
00644500  41 5C                           pop r12
00644502  5D                              pop rbp
00644503  C3                              ret
00644504  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwOpenProcessTokenWrapper(__int64 a1, int a2, __int64 a3)
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
    result = DifGetAPIThunkContextById(result + 78, a2, a3, a4);
    if (result == 0) goto loc_0064446A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006443EE;
    v_stack_m58 = v_stack_p0;
    goto loc_006443FB;
loc_006443EE:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9176239)) != 0) goto loc_0064441F;
    if (((*(unsigned int *)(v_rip + 9176419)) & (0x800ULL)) == 0) goto loc_00644432;
loc_0064441F:
    result = ExAcquireRundownProtection(v_rip + 9173594, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064446A;
loc_00644432:
    goto loc_00644454;
loc_0064443B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00644454:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0064443B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9173531;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwOpenProcessToken(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_006444E3;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9176110)) != 0) goto loc_00644498;
    if (((*(unsigned int *)(v_rip + 9176298)) & (0x800ULL)) == 0) goto loc_006444AB;
loc_00644498:
    result = ExAcquireRundownProtection(v_rip + 9173473, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006444E3;
loc_006444AB:
    v_rsi = (result) + (48);
    goto loc_006444CD;
loc_006444B4:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_006444CD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006444B4;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9173410;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwOpenProcessTokenWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3)
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
    result = DifGetAPIThunkContextById(result + 78, Arg2, Arg3, a4);
    if (result == 0) goto loc_0064446A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006443EE;
    v_stack_m58 = v_stack_p0;
    goto loc_006443FB;
loc_006443EE:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8C04AF)) != 0) goto loc_0064441F;
    if (((*(uint32_t *)(v_rip + 0x8C0563)) & (0x800ULL)) == 0) goto loc_00644432;
loc_0064441F:
    result = ExAcquireRundownProtection(v_rip + 9173594, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0064446A;
loc_00644432:
    goto loc_00644454;
loc_0064443B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00644454:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0064443B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9173531;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = ZwOpenProcessToken(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_006444E3;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C042E)) != 0) goto loc_00644498;
    if (((*(uint32_t *)(v_rip + 0x8C04EA)) & (0x800ULL)) == 0) goto loc_006444AB;
loc_00644498:
    result = ExAcquireRundownProtection(v_rip + 9173473, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_006444E3;
loc_006444AB:
    local_rsi = (result) + (48);
    goto loc_006444CD;
loc_006444B4:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
loc_006444CD:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006444B4;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9173410;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00644390&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00644390[BB_00644390]
  bb_006443DD[BB_006443DD]
  bb_006443E4[BB_006443E4]
  bb_006443EE[BB_006443EE]
  bb_006443F2[BB_006443F2]
  bb_006443FB[BB_006443FB]
  bb_00644413[BB_00644413]
  bb_0064441F[BB_0064441F]
  bb_00644432[BB_00644432]
  bb_0064443B[BB_0064443B]
  bb_00644444[BB_00644444]
  bb_00644451[BB_00644451]
  bb_00644454[BB_00644454]
  bb_00644459[BB_00644459]
  bb_0064445E[BB_0064445E]
  bb_0064446A[BB_0064446A]
  bb_00644480[BB_00644480]
  bb_0064448C[BB_0064448C]
  bb_00644498[BB_00644498]
  bb_006444AB[BB_006444AB]
  bb_006444B4[BB_006444B4]
  bb_006444BD[BB_006444BD]
  bb_006444CA[BB_006444CA]
  bb_006444CD[BB_006444CD]
  bb_006444D2[BB_006444D2]
  bb_006444D7[BB_006444D7]
  bb_006444E3[BB_006444E3]
  bb_00644504[BB_00644504]
  bb_00644390 -->|branch| bb_0064446A
  bb_00644390 -->|fallthrough| bb_006443DD
  bb_006443DD -->|branch| bb_006443EE
  bb_006443DD -->|fallthrough| bb_006443E4
  bb_006443E4 -->|branch| bb_006443FB
  bb_006443EE -->|branch| bb_006443FB
  bb_006443EE -->|fallthrough| bb_006443F2
  bb_006443F2 -->|flow| bb_006443FB
  bb_006443FB -->|branch| bb_0064441F
  bb_006443FB -->|fallthrough| bb_00644413
  bb_00644413 -->|branch| bb_00644432
  bb_00644413 -->|fallthrough| bb_0064441F
  bb_0064441F -->|branch| bb_0064446A
  bb_0064441F -->|fallthrough| bb_00644432
  bb_00644432 -->|branch| bb_00644454
  bb_0064443B -->|branch| bb_00644451
  bb_0064443B -->|fallthrough| bb_00644444
  bb_00644444 -->|flow| bb_00644451
  bb_00644451 -->|flow| bb_00644454
  bb_00644454 -->|branch| bb_0064443B
  bb_00644454 -->|fallthrough| bb_00644459
  bb_00644459 -->|branch| bb_0064446A
  bb_00644459 -->|fallthrough| bb_0064445E
  bb_0064445E -->|flow| bb_0064446A
  bb_0064446A -->|branch| bb_006444E3
  bb_0064446A -->|fallthrough| bb_00644480
  bb_00644480 -->|branch| bb_00644498
  bb_00644480 -->|fallthrough| bb_0064448C
  bb_0064448C -->|branch| bb_006444AB
  bb_0064448C -->|fallthrough| bb_00644498
  bb_00644498 -->|branch| bb_006444E3
  bb_00644498 -->|fallthrough| bb_006444AB
  bb_006444AB -->|branch| bb_006444CD
  bb_006444B4 -->|branch| bb_006444CA
  bb_006444B4 -->|fallthrough| bb_006444BD
  bb_006444BD -->|flow| bb_006444CA
  bb_006444CA -->|flow| bb_006444CD
  bb_006444CD -->|branch| bb_006444B4
  bb_006444CD -->|fallthrough| bb_006444D2
  bb_006444D2 -->|branch| bb_006444E3
  bb_006444D2 -->|fallthrough| bb_006444D7
  bb_006444D7 -->|flow| bb_006444E3
```
