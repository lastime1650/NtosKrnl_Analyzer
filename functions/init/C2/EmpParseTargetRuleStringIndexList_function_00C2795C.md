# EmpParseTargetRuleStringIndexList

- RVA: `0x00C2795C`–`0x00C27C71` (길이 `789` bytes)
- VA: `0x0000000140C2795C`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00089D74`
- 디코드: `213`개 명령, `789/789` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00C27A61` → [strchr](../../text/50/strchr_function_005014F0.md) (function, `0x005014F0`)
- `0x00C27AA9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C27B4B` → [EmpInfParseGetValueFromSectionAndKeyName](EmpInfParseGetValueFromSectionAndKeyName_function_00C264B4.md) (function, `0x00C264B4`)
- `0x00C27BD6` → [RtlCharToInteger](../../page/A6/RtlCharToInteger_function_00A6C4E0.md) (function, `0x00A6C4E0`)
- `0x00C27C1B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [EmpParseTargetRules](EmpParseTargetRules_function_00C27C78.md) at `0x00C27E2B`

### Static image references
- `0x00C27A5A` → RVA `0x00C79690` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C27B3B` → RVA `0x00C79680` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C27B5B` → RVA `0x00E65BDC` (`.data`; read)
- `0x00C27B64` → RVA `0x00E65BE0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00C27A61` → [strchr](../../text/50/strchr_function_005014F0.md) (`INIT` → `.text`)
  - `0x00C27AA9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C27BD6` → [RtlCharToInteger](../../page/A6/RtlCharToInteger_function_00A6C4E0.md) (`INIT` → `PAGE`)
  - `0x00C27C1B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C2795C  48 8B C4                        mov rax, rsp
00C2795F  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
00C27963  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00C27967  48 89 48 08                     mov qword ptr [rax + 8], rcx
00C2796B  53                              push rbx
00C2796C  55                              push rbp
00C2796D  56                              push rsi
00C2796E  57                              push rdi
00C2796F  41 54                           push r12
00C27971  41 55                           push r13
00C27973  41 56                           push r14
00C27975  41 57                           push r15
00C27977  48 83 EC 48                     sub rsp, 0x48
00C2797B  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
00C27983  33 F6                           xor esi, esi
00C27985  21 70 B0                        and dword ptr [rax - 0x50], esi
00C27988  45 33 F6                        xor r14d, r14d
00C2798B  32 DB                           xor bl, bl
00C2798D  89 B4 24 98 00 00 00            mov dword ptr [rsp + 0x98], esi
00C27994  45 33 ED                        xor r13d, r13d
00C27997  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
00C2799C  48 8B FA                        mov rdi, rdx
00C2799F  8B 11                           mov edx, dword ptr [rcx]
00C279A1  89 54 24 34                     mov dword ptr [rsp + 0x34], edx
00C279A5  48 39 B4 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], rsi
00C279AD  75 07                           jne 0x140c279b6
00C279AF  32 C0                           xor al, al
00C279B1  E9 A9 02 00 00                  jmp 0x140c27c5f
00C279B6  84 DB                           test bl, bl
00C279B8  0F 85 9E 02 00 00               jne 0x140c27c5c
00C279BE  8B C6                           mov eax, esi
00C279C0  85 F6                           test esi, esi
00C279C2  0F 84 70 02 00 00               je 0x140c27c38
00C279C8  83 E8 01                        sub eax, 1
00C279CB  74 55                           je 0x140c27a22
00C279CD  83 E8 01                        sub eax, 1
00C279D0  74 34                           je 0x140c27a06
00C279D2  83 F8 01                        cmp eax, 1
00C279D5  75 DF                           jne 0x140c279b6
00C279D7  38 1F                           cmp byte ptr [rdi], bl
00C279D9  0F 85 5E 02 00 00               jne 0x140c27c3d
00C279DF  45 3B E8                        cmp r13d, r8d
00C279E2  0F 85 55 02 00 00               jne 0x140c27c3d
00C279E8  45 3B F1                        cmp r14d, r9d
00C279EB  0F 85 4C 02 00 00               jne 0x140c27c3d
00C279F1  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
00C279F9  43 8D 04 2E                     lea eax, [r14 + r13]
00C279FD  03 C2                           add eax, edx
00C279FF  89 01                           mov dword ptr [rcx], eax
00C27A01  E9 54 02 00 00                  jmp 0x140c27c5a
00C27A06  8A 07                           mov al, byte ptr [rdi]
00C27A08  3C 2E                           cmp al, 0x2e
00C27A0A  0F 84 34 02 00 00               je 0x140c27c44
00C27A10  3C 7D                           cmp al, 0x7d
00C27A12  0F 85 25 02 00 00               jne 0x140c27c3d
00C27A18  BE 03 00 00 00                  mov esi, 3
00C27A1D  E9 27 02 00 00                  jmp 0x140c27c49
00C27A22  8A 0F                           mov cl, byte ptr [rdi]
00C27A24  80 F9 7D                        cmp cl, 0x7d
00C27A27  74 EF                           je 0x140c27a18
00C27A29  45 3B E8                        cmp r13d, r8d
00C27A2C  0F 87 26 02 00 00               ja 0x140c27c58
00C27A32  45 3B F1                        cmp r14d, r9d
00C27A35  0F 87 1D 02 00 00               ja 0x140c27c58
00C27A3B  47 8D 24 2E                     lea r12d, [r14 + r13]
00C27A3F  44 03 E2                        add r12d, edx
00C27A42  44 3B A4 24 B8 00 00 00         cmp r12d, dword ptr [rsp + 0xb8]
00C27A4A  0F 83 08 02 00 00               jae 0x140c27c58
00C27A50  4C 8B F7                        mov r14, rdi
00C27A53  84 C9                           test cl, cl
00C27A55  74 31                           je 0x140c27a88
00C27A57  0F BE D1                        movsx edx, cl
00C27A5A  48 8D 0D 2F 1C 05 00            lea rcx, [rip + 0x51c2f]
00C27A61  E8 8A 9A 8D FF                  call 0x1405014f0
00C27A66  48 85 C0                        test rax, rax
00C27A69  75 09                           jne 0x140c27a74
00C27A6B  48 FF C7                        inc rdi
00C27A6E  8A 0F                           mov cl, byte ptr [rdi]
00C27A70  84 C9                           test cl, cl
00C27A72  75 E3                           jne 0x140c27a57
00C27A74  8B 54 24 34                     mov edx, dword ptr [rsp + 0x34]
00C27A78  44 8B 84 24 A0 00 00 00         mov r8d, dword ptr [rsp + 0xa0]
00C27A80  44 8B 8C 24 A8 00 00 00         mov r9d, dword ptr [rsp + 0xa8]
00C27A88  48 8B EF                        mov rbp, rdi
00C27A8B  49 2B EE                        sub rbp, r14
00C27A8E  48 8D 75 01                     lea rsi, [rbp + 1]
00C27A92  48 85 F6                        test rsi, rsi
00C27A95  0F 84 8A 01 00 00               je 0x140c27c25
00C27A9B  41 B8 45 4D 69 74               mov r8d, 0x74694d45
00C27AA1  48 8B D6                        mov rdx, rsi
00C27AA4  B9 00 01 00 00                  mov ecx, 0x100
00C27AA9  E8 42 A6 F5 FF                  call 0x140b820f0
00C27AAE  4C 8B F8                        mov r15, rax
00C27AB1  48 85 C0                        test rax, rax
00C27AB4  75 27                           jne 0x140c27add
00C27AB6  8B B4 24 98 00 00 00            mov esi, dword ptr [rsp + 0x98]
00C27ABD  B3 01                           mov bl, 1
00C27ABF  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
00C27AC4  8B 54 24 34                     mov edx, dword ptr [rsp + 0x34]
00C27AC8  44 8B 84 24 A0 00 00 00         mov r8d, dword ptr [rsp + 0xa0]
00C27AD0  44 8B 8C 24 A8 00 00 00         mov r9d, dword ptr [rsp + 0xa8]
00C27AD8  E9 D9 FE FF FF                  jmp 0x140c279b6
00C27ADD  48 81 FE FF FF FF 7F            cmp rsi, 0x7fffffff
00C27AE4  77 D0                           ja 0x140c27ab6
00C27AE6  48 81 FD FE FF FF 7F            cmp rbp, 0x7ffffffe
00C27AED  76 05                           jbe 0x140c27af4
00C27AEF  C6 00 00                        mov byte ptr [rax], 0
00C27AF2  EB C2                           jmp 0x140c27ab6
00C27AF4  49 8B CF                        mov rcx, r15
00C27AF7  4D 2B F7                        sub r14, r15
00C27AFA  48 8D 56 FF                     lea rdx, [rsi - 1]
00C27AFE  48 85 D2                        test rdx, rdx
00C27B01  74 12                           je 0x140c27b15
00C27B03  41 8A 04 0E                     mov al, byte ptr [r14 + rcx]
00C27B07  84 C0                           test al, al
00C27B09  74 0A                           je 0x140c27b15
00C27B0B  88 01                           mov byte ptr [rcx], al
00C27B0D  48 8B F2                        mov rsi, rdx
00C27B10  48 FF C1                        inc rcx
00C27B13  EB E5                           jmp 0x140c27afa
00C27B15  48 85 F6                        test rsi, rsi
00C27B18  48 8D 41 FF                     lea rax, [rcx - 1]
00C27B1C  48 0F 45 C1                     cmovne rax, rcx
00C27B20  C6 00 00                        mov byte ptr [rax], 0
00C27B23  74 91                           je 0x140c27ab6
00C27B25  44 3B AC 24 A0 00 00 00         cmp r13d, dword ptr [rsp + 0xa0]
00C27B2D  0F 83 96 00 00 00               jae 0x140c27bc9
00C27B33  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00C27B3B  48 8D 15 3E 1B 05 00            lea rdx, [rip + 0x51b3e]
00C27B42  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00C27B48  4D 8B C7                        mov r8, r15
00C27B4B  E8 64 E9 FF FF                  call 0x140c264b4
00C27B50  4C 8B D0                        mov r10, rax
00C27B53  48 85 C0                        test rax, rax
00C27B56  74 61                           je 0x140c27bb9
00C27B58  45 33 C0                        xor r8d, r8d
00C27B5B  44 3B 05 7A E0 23 00            cmp r8d, dword ptr [rip + 0x23e07a]
00C27B62  73 50                           jae 0x140c27bb4
00C27B64  48 8B 0D 75 E0 23 00            mov rcx, qword ptr [rip + 0x23e075]
00C27B6B  49 8B D2                        mov rdx, r10
00C27B6E  4E 8B 0C C1                     mov r9, qword ptr [rcx + r8*8]
00C27B72  49 2B D1                        sub rdx, r9
00C27B75  41 0F B6 09                     movzx ecx, byte ptr [r9]
00C27B79  41 0F B6 04 11                  movzx eax, byte ptr [r9 + rdx]
00C27B7E  2B C8                           sub ecx, eax
00C27B80  75 07                           jne 0x140c27b89
00C27B82  49 FF C1                        inc r9
00C27B85  85 C0                           test eax, eax
00C27B87  75 EC                           jne 0x140c27b75
00C27B89  85 C9                           test ecx, ecx
00C27B8B  74 05                           je 0x140c27b92
00C27B8D  41 FF C0                        inc r8d
00C27B90  EB C9                           jmp 0x140c27b5b
00C27B92  8B 4C 24 34                     mov ecx, dword ptr [rsp + 0x34]
00C27B96  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
00C27B9E  41 03 CD                        add ecx, r13d
00C27BA1  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
00C27BA6  41 FF C5                        inc r13d
00C27BA9  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
00C27BAE  44 89 04 88                     mov dword ptr [rax + rcx*4], r8d
00C27BB2  EB 53                           jmp 0x140c27c07
00C27BB4  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
00C27BB9  8B B4 24 98 00 00 00            mov esi, dword ptr [rsp + 0x98]
00C27BC0  B3 01                           mov bl, 1
00C27BC2  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
00C27BC7  EB 4A                           jmp 0x140c27c13
00C27BC9  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
00C27BCE  BA 10 00 00 00                  mov edx, 0x10
00C27BD3  49 8B CF                        mov rcx, r15
00C27BD6  E8 05 49 E4 FF                  call 0x140a6c4e0
00C27BDB  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
00C27BE0  85 C0                           test eax, eax
00C27BE2  79 0B                           jns 0x140c27bef
00C27BE4  8B B4 24 98 00 00 00            mov esi, dword ptr [rsp + 0x98]
00C27BEB  B3 01                           mov bl, 1
00C27BED  EB 24                           jmp 0x140c27c13
00C27BEF  48 8B 94 24 B0 00 00 00         mov rdx, qword ptr [rsp + 0xb0]
00C27BF7  41 FF C6                        inc r14d
00C27BFA  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
00C27BFE  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
00C27C03  42 89 04 A2                     mov dword ptr [rdx + r12*4], eax
00C27C07  BE 02 00 00 00                  mov esi, 2
00C27C0C  89 B4 24 98 00 00 00            mov dword ptr [rsp + 0x98], esi
00C27C13  BA 45 4D 69 74                  mov edx, 0x74694d45
00C27C18  49 8B CF                        mov rcx, r15
00C27C1B  E8 50 AC F5 FF                  call 0x140b82870
00C27C20  E9 9F FE FF FF                  jmp 0x140c27ac4
00C27C25  8B B4 24 98 00 00 00            mov esi, dword ptr [rsp + 0x98]
00C27C2C  B3 01                           mov bl, 1
00C27C2E  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
00C27C33  E9 7E FD FF FF                  jmp 0x140c279b6
00C27C38  80 3F 7B                        cmp byte ptr [rdi], 0x7b
00C27C3B  74 07                           je 0x140c27c44
00C27C3D  B3 01                           mov bl, 1
00C27C3F  E9 72 FD FF FF                  jmp 0x140c279b6
00C27C44  BE 01 00 00 00                  mov esi, 1
00C27C49  48 FF C7                        inc rdi
00C27C4C  89 B4 24 98 00 00 00            mov dword ptr [rsp + 0x98], esi
00C27C53  E9 5E FD FF FF                  jmp 0x140c279b6
00C27C58  B3 01                           mov bl, 1
00C27C5A  84 DB                           test bl, bl
00C27C5C  0F 94 C0                        sete al
00C27C5F  48 83 C4 48                     add rsp, 0x48
00C27C63  41 5F                           pop r15
00C27C65  41 5E                           pop r14
00C27C67  41 5D                           pop r13
00C27C69  41 5C                           pop r12
00C27C6B  5F                              pop rdi
00C27C6C  5E                              pop rsi
00C27C6D  5D                              pop rbp
00C27C6E  5B                              pop rbx
00C27C6F  C3                              ret
00C27C70  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EmpParseTargetRuleStringIndexList(__int64 a1, __int64 a2, int a3, int a4, __int64 a5, unsigned int a6, __int64 a7)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (72);
    v_rsi = 0;
    v_r14 = 0;
    v_rbx = 0;
    v_stack_p10 = 0;
    v_r13 = 0;
    v_stack_m58 = 0;
    v_stack_m54 = (unsigned int)((unsigned int)(*(unsigned int *)(a7)));
    if (a5 != 0) goto loc_00C279B6;
    result = 0;
    goto loc_00C27C5F;
loc_00C279B6:
    if (0 != 0) goto loc_00C27C5C;
    if (0 == 0) goto loc_00C27C38;
    result = (unsigned int)((0) - (1));
    if (condition_is_equal) goto loc_00C27A22;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00C27A06;
    if (((unsigned int)(result)) != 1) goto loc_00C279B6;
    if ((*(unsigned __int8 *)(a2)) != 0) goto loc_00C27C3D;
    if (0 != a3) goto loc_00C27C3D;
    if (0 != a4) goto loc_00C27C3D;
    result = (unsigned int)((v_r14 + v_r13 * 1) + ((unsigned int)((unsigned int)(*(unsigned int *)(a7)))));
    *(unsigned int *)(a7) = (unsigned int)(result);
    goto loc_00C27C5A;
loc_00C27A06:
    if (((unsigned __int8)(*(unsigned __int8 *)(a2))) == 46) goto loc_00C27C44;
    if (((unsigned __int8)(*(unsigned __int8 *)(a2))) != 125) goto loc_00C27C3D;
loc_00C27A18:
    goto loc_00C27C49;
loc_00C27A22:
    if (((unsigned __int8)(*(unsigned __int8 *)(a2))) == 125) goto loc_00C27A18;
    if (0 > a3) goto loc_00C27C58;
    if (0 > a4) goto loc_00C27C58;
    v_r12 = (unsigned int)((v_r14 + v_r13 * 1) + ((unsigned int)((unsigned int)(*(unsigned int *)(a7)))));
    if (((unsigned int)(v_r12)) >= a6) goto loc_00C27C58;
    if ((unsigned __int8)(*(unsigned __int8 *)(a2)) == 0) goto loc_00C27A88;
loc_00C27A57:
    result = strchr(v_rip + 334895, (__int8)((unsigned __int8)(*(unsigned __int8 *)(a2))), a3, a4);
    if (result != 0) goto loc_00C27A74;
    v_rdi = (a2) + 1;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rdi)) != 0) goto loc_00C27A57;
loc_00C27A74:
loc_00C27A88:
    v_rbp = (v_rdi) - (a2);
    if (v_rbp + 1 == 0) goto loc_00C27C25;
    result = ExAllocatePool2(256, v_rbp + 1, (unsigned int)(0x74694D45ULL), (unsigned int)(v_stack_p20));
    if (result != 0) goto loc_00C27ADD;
loc_00C27AB6:
loc_00C27AC4:
    goto loc_00C279B6;
loc_00C27ADD:
    if (((unsigned int)(v_stack_p10)) > 0x7FFFFFFFULL) goto loc_00C27AB6;
    if (v_rbp <= 0x7FFFFFFEULL) goto loc_00C27AF4;
    *(unsigned __int8 *)(result) = 0;
    goto loc_00C27AB6;
loc_00C27AF4:
    v_r14 = ((unsigned int)(v_stack_m58)) - (result);
loc_00C27AFA:
    if ((unsigned int)(v_stack_p10) - 1 == 0) goto loc_00C27B15;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_r14 + result * 1)) == 0) goto loc_00C27B15;
    *(unsigned __int8 *)(result) = (unsigned __int8)(*(unsigned __int8 *)(v_r14 + result * 1));
    a1 = (result) + 1;
    goto loc_00C27AFA;
loc_00C27B15:
    result = a1 - 1;
    if ((unsigned int)(v_stack_p10) - 1 != 0) { result = a1; }
    *(unsigned __int8 *)(result) = 0;
    if ((unsigned int)(v_stack_p10) - 1 == 0) goto loc_00C27AB6;
    if (0 >= v_stack_p18) goto loc_00C27BC9;
    result = EmpInfParseGetValueFromSectionAndKeyName(v_stack_p8, v_rip + 334654, result, (unsigned int)(v_stack_p20));
    if (result == 0) goto loc_00C27BB9;
    a3 = 0;
loc_00C27B5B:
    if (0 >= (*(unsigned int *)(v_rip + 2351226))) goto loc_00C27BB4;
    a2 = (result) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 2351221) + a3 * 8));
loc_00C27B75:
    a1 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 2351221) + a3 * 8))) - ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 2351221) + a3 * 8) + a2 * 1))));
    if (condition_is_not_equal) goto loc_00C27B89;
    a4 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 2351221) + a3 * 8)) + 1;
    if ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 2351221) + a3 * 8) + a2 * 1)) != 0) goto loc_00C27B75;
loc_00C27B89:
    if ((unsigned int)(a1) == 0) goto loc_00C27B92;
    a3 = (unsigned int)((a3) + 1);
    goto loc_00C27B5B;
loc_00C27B92:
    a1 = (unsigned int)(((unsigned int)(v_stack_m54)) + (0));
    v_r13 = (unsigned int)((v_r13) + 1);
    v_stack_m50 = a3;
    *(unsigned int *)(a5 + a1 * 4) = a3;
    goto loc_00C27C07;
loc_00C27BB4:
    v_stack_m50 = a3;
loc_00C27BB9:
    goto loc_00C27C13;
loc_00C27BC9:
    result = RtlCharToInteger(result, 16, v_stack_m50, a4);
    if (!sign_flag) goto loc_00C27BEF;
    goto loc_00C27C13;
loc_00C27BEF:
    v_r14 = (unsigned int)(((unsigned int)(v_stack_m58)) + 1);
    v_stack_m58 = (unsigned int)(v_r14);
    *(unsigned int *)(a5 + v_r12 * 4) = (unsigned int)((unsigned int)(v_stack_m50));
loc_00C27C07:
    v_stack_p10 = 2;
loc_00C27C13:
    result = ExFreePoolWithTag(result, (unsigned int)(0x74694D45ULL), v_stack_m50, a4);
    goto loc_00C27AC4;
loc_00C27C25:
    goto loc_00C279B6;
loc_00C27C38:
    if ((*(unsigned __int8 *)(v_rdi)) == 123) goto loc_00C27C44;
loc_00C27C3D:
    goto loc_00C279B6;
loc_00C27C44:
loc_00C27C49:
    v_rdi = (v_rdi) + 1;
    v_stack_p10 = 1;
    goto loc_00C279B6;
loc_00C27C58:
loc_00C27C5A:
loc_00C27C5C:
    result = (1 == 0) ? 1 : 0;
loc_00C27C5F:
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EmpParseTargetRuleStringIndexList(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, void *Arg5, uint32_t Arg6, void *Arg7)
{
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_m68;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (72);
    local_rsi = 0;
    local_r14 = 0;
    local_rbx = 0;
    v_stack_p10 = 0;
    local_r13 = 0;
    v_stack_m58 = 0;
    v_stack_m54 = (uint32_t)((uint32_t)(*(uint32_t *)(arg7)));
    if (Arg5 != NULL) goto loc_00C279B6;
    result = 0;
    goto loc_00C27C5F;
loc_00C279B6:
    if (0 != 0) goto loc_00C27C5C;
    if (0 == 0) goto loc_00C27C38;
    result = (uint32_t)((0) - (1));
    if (condition_is_equal) goto loc_00C27A22;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00C27A06;
    if (((uint32_t)(result)) != 1) goto loc_00C279B6;
    if ((*(uint8_t *)(Arg2)) != 0) goto loc_00C27C3D;
    if (0 != Arg3) goto loc_00C27C3D;
    if (0 != Arg4) goto loc_00C27C3D;
    result = (uint32_t)((local_r14 + local_r13 * 1) + ((uint32_t)((uint32_t)(*(uint32_t *)(arg7)))));
    *(uint32_t *)(arg7) = (uint32_t)(result);
    goto loc_00C27C5A;
loc_00C27A06:
    if (((uint8_t)(*(uint8_t *)(Arg2))) == 46) goto loc_00C27C44;
    if (((uint8_t)(*(uint8_t *)(Arg2))) != 125) goto loc_00C27C3D;
loc_00C27A18:
    goto loc_00C27C49;
loc_00C27A22:
    if (((uint8_t)(*(uint8_t *)(Arg2))) == 125) goto loc_00C27A18;
    if (0 > Arg3) goto loc_00C27C58;
    if (0 > Arg4) goto loc_00C27C58;
    local_r12 = (uint32_t)((local_r14 + local_r13 * 1) + ((uint32_t)((uint32_t)(*(uint32_t *)(arg7)))));
    if (((uint32_t)(local_r12)) >= Arg6) goto loc_00C27C58;
    if ((uint8_t)(*(uint8_t *)(Arg2)) == 0) goto loc_00C27A88;
loc_00C27A57:
    result = strchr(v_rip + 334895, (int8_t)((uint8_t)(*(uint8_t *)(Arg2))), Arg3, Arg4);
    if (result != 0) goto loc_00C27A74;
    local_rdi = (Arg2) + 1;
    if ((uint8_t)(*(uint8_t *)(local_rdi)) != 0) goto loc_00C27A57;
loc_00C27A74:
loc_00C27A88:
    local_rbp = (local_rdi) - (Arg2);
    if (local_rbp + 1 == 0) goto loc_00C27C25;
    result = ExAllocatePool2(256, local_rbp + 1, (uint32_t)(0x74694D45ULL), (uint32_t)(v_stack_p20));
    if (result != 0) goto loc_00C27ADD;
loc_00C27AB6:
loc_00C27AC4:
    goto loc_00C279B6;
loc_00C27ADD:
    if (((uint32_t)(v_stack_p10)) > 0x7FFFFFFFULL) goto loc_00C27AB6;
    if (local_rbp <= 0x7FFFFFFEULL) goto loc_00C27AF4;
    *(uint8_t *)(result) = 0;
    goto loc_00C27AB6;
loc_00C27AF4:
    local_r14 = ((uint32_t)(v_stack_m58)) - (result);
loc_00C27AFA:
    if ((uint32_t)(v_stack_p10) - 1 == 0) goto loc_00C27B15;
    if ((uint8_t)(*(uint8_t *)(local_r14 + result * 1)) == 0) goto loc_00C27B15;
    *(uint8_t *)(result) = (uint8_t)(*(uint8_t *)(local_r14 + result * 1));
    Arg1 = (result) + 1;
    goto loc_00C27AFA;
loc_00C27B15:
    result = Arg1 - 1;
    if ((uint32_t)(v_stack_p10) - 1 != 0) { result = Arg1; }
    *(uint8_t *)(result) = 0;
    if ((uint32_t)(v_stack_p10) - 1 == 0) goto loc_00C27AB6;
    if (0 >= v_stack_p18) goto loc_00C27BC9;
    result = EmpInfParseGetValueFromSectionAndKeyName(v_stack_p8, v_rip + 334654, result, (uint32_t)(v_stack_p20));
    if (result == 0) goto loc_00C27BB9;
    Arg3 = 0;
loc_00C27B5B:
    if (0 >= (*(uint32_t *)(v_rip + 0x23E07A))) goto loc_00C27BB4;
    Arg2 = (result) - (*(uint64_t *)(*(uint64_t *)(v_rip + 0x23E075) + Arg3 * 8));
loc_00C27B75:
    Arg1 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x23E075) + Arg3 * 8))) - ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x23E075) + Arg3 * 8) + Arg2 * 1))));
    if (condition_is_not_equal) goto loc_00C27B89;
    Arg4 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x23E075) + Arg3 * 8)) + 1;
    if ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x23E075) + Arg3 * 8) + Arg2 * 1)) != 0) goto loc_00C27B75;
loc_00C27B89:
    if ((uint32_t)(Arg1) == 0) goto loc_00C27B92;
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_00C27B5B;
loc_00C27B92:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m54)) + (0));
    local_r13 = (uint32_t)((local_r13) + 1);
    v_stack_m50 = Arg3;
    *(uint32_t *)(arg5 + Arg1 * 4) = Arg3;
    goto loc_00C27C07;
loc_00C27BB4:
    v_stack_m50 = Arg3;
loc_00C27BB9:
    goto loc_00C27C13;
loc_00C27BC9:
    result = RtlCharToInteger(result, 16, v_stack_m50, Arg4);
    if (!sign_flag) goto loc_00C27BEF;
    goto loc_00C27C13;
loc_00C27BEF:
    local_r14 = (uint32_t)(((uint32_t)(v_stack_m58)) + 1);
    v_stack_m58 = (uint32_t)(local_r14);
    *(uint32_t *)(arg5 + local_r12 * 4) = (uint32_t)((uint32_t)(v_stack_m50));
loc_00C27C07:
    v_stack_p10 = 2;
loc_00C27C13:
    result = ExFreePoolWithTag(result, (uint32_t)(0x74694D45ULL), v_stack_m50, Arg4);
    goto loc_00C27AC4;
loc_00C27C25:
    goto loc_00C279B6;
loc_00C27C38:
    if ((*(uint8_t *)(local_rdi)) == 123) goto loc_00C27C44;
loc_00C27C3D:
    goto loc_00C279B6;
loc_00C27C44:
loc_00C27C49:
    local_rdi = (local_rdi) + 1;
    v_stack_p10 = 1;
    goto loc_00C279B6;
loc_00C27C58:
loc_00C27C5A:
loc_00C27C5C:
    result = (1 == 0) ? 1 : 0;
loc_00C27C5F:
    local_rsp = (local_rsp) + (72);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0 + r12*4` | `32` | `W` |
| `Arg5` | `+ 0x0 + rcx*4` | `32` | `W` |
| `Arg7` | `+ 0x0` | `32` | `R` |
| `Arg7` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C2795C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
