# HalpInterruptDpReplaceBegin

- RVA: `0x005631CC`–`0x0056357E` (길이 `946` bytes)
- VA: `0x00000001405631CC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C4BC0`
- 디코드: `259`개 명령, `946/946` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00563263` → [HalpInterruptSetProblemEx](../48/HalpInterruptSetProblemEx_function_0048AC8C.md) (function, `0x0048AC8C`)
- `0x005632B1` → [KeGetProcessorIndexFromNumber](../2D/KeGetProcessorIndexFromNumber_function_002DD2D0.md) (function, `0x002DD2D0`)
- `0x0056333A` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00563359` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0056339C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005633E2` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0056340B` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0056346E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0056351D` → [HalpInterruptSetProblemEx](../48/HalpInterruptSetProblemEx_function_0048AC8C.md) (function, `0x0048AC8C`)

### Direct callers
- [HalpDpReplaceBegin](../../page/70/HalpDpReplaceBegin_function_0070C130.md) at `0x0070C246`

### Static image references
- `0x0056321F` → RVA `0x00E10200` (`.data`; read)
- `0x0056322D` → RVA `0x00FC3E30` (`.data`; read)
- `0x0056325C` → RVA `0x00025F20` (`.rdata`; read)
- `0x005632D7` → RVA `0x00E101F0` (`.data`; read)
- `0x005632FF` → RVA `0x00E10204` (`.data`; read)
- `0x00563427` → RVA `0x00E102D0` (`.data`; read)
- `0x0056342E` → RVA `0x00E102E0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005631CC  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
005631D1  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
005631D6  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
005631DB  55                              push rbp
005631DC  56                              push rsi
005631DD  57                              push rdi
005631DE  41 54                           push r12
005631E0  41 55                           push r13
005631E2  41 56                           push r14
005631E4  41 57                           push r15
005631E6  48 8B EC                        mov rbp, rsp
005631E9  48 83 EC 70                     sub rsp, 0x70
005631ED  33 C0                           xor eax, eax
005631EF  0F 57 C0                        xorps xmm0, xmm0
005631F2  21 45 58                        and dword ptr [rbp + 0x58], eax
005631F5  45 8B F1                        mov r14d, r9d
005631F8  4C 8B 4D 70                     mov r9, qword ptr [rbp + 0x70]
005631FC  33 DB                           xor ebx, ebx
005631FE  4D 8B E8                        mov r13, r8
00563201  89 45 D8                        mov dword ptr [rbp - 0x28], eax
00563204  4C 8B D2                        mov r10, rdx
00563207  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0056320A  0F 11 45 C8                     movups xmmword ptr [rbp - 0x38], xmm0
0056320E  41 21 01                        and dword ptr [r9], eax
00563211  45 33 C0                        xor r8d, r8d
00563214  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00563218  45 3B C6                        cmp r8d, r14d
0056321B  73 55                           jae 0x140563272
0056321D  33 D2                           xor edx, edx
0056321F  3B 15 DB CF 8A 00               cmp edx, dword ptr [rip + 0x8acfdb]
00563225  73 1E                           jae 0x140563245
00563227  8B CA                           mov ecx, edx
00563229  48 C1 E1 06                     shl rcx, 6
0056322D  48 03 0D FC 0B A6 00            add rcx, qword ptr [rip + 0xa60bfc]
00563234  38 59 0D                        cmp byte ptr [rcx + 0xd], bl
00563237  74 08                           je 0x140563241
00563239  43 8B 04 82                     mov eax, dword ptr [r10 + r8*4]
0056323D  39 01                           cmp dword ptr [rcx], eax
0056323F  74 09                           je 0x14056324a
00563241  FF C2                           inc edx
00563243  EB DA                           jmp 0x14056321f
00563245  41 FF C0                        inc r8d
00563248  EB CE                           jmp 0x140563218
0056324A  C7 44 24 20 97 00 00 00         mov dword ptr [rsp + 0x20], 0x97
00563252  BA 18 00 00 00                  mov edx, 0x18
00563257  45 33 C0                        xor r8d, r8d
0056325A  33 C9                           xor ecx, ecx
0056325C  4C 8D 0D BD 2C AC FF            lea r9, [rip - 0x53d343]
00563263  E8 24 7A F2 FF                  call 0x14048ac8c
00563268  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0056326D  E9 F1 02 00 00                  jmp 0x140563563
00563272  48 8B 55 40                     mov rdx, qword ptr [rbp + 0x40]
00563276  33 F6                           xor esi, esi
00563278  41 3B F6                        cmp esi, r14d
0056327B  73 5A                           jae 0x1405632d7
0056327D  33 FF                           xor edi, edi
0056327F  44 8B 3D 7A CF 8A 00            mov r15d, dword ptr [rip + 0x8acf7a]
00563286  41 3B FF                        cmp edi, r15d
00563289  73 37                           jae 0x1405632c2
0056328B  8B CF                           mov ecx, edi
0056328D  48 C1 E1 06                     shl rcx, 6
00563291  48 03 0D 98 0B A6 00            add rcx, qword ptr [rip + 0xa60b98]
00563298  38 59 0C                        cmp byte ptr [rcx + 0xc], bl
0056329B  74 0C                           je 0x1405632a9
0056329D  38 59 0D                        cmp byte ptr [rcx + 0xd], bl
005632A0  74 07                           je 0x1405632a9
005632A2  8B 04 B2                        mov eax, dword ptr [rdx + rsi*4]
005632A5  39 01                           cmp dword ptr [rcx], eax
005632A7  74 04                           je 0x1405632ad
005632A9  FF C7                           inc edi
005632AB  EB D2                           jmp 0x14056327f
005632AD  48 83 C1 10                     add rcx, 0x10
005632B1  E8 1A A0 D7 FF                  call 0x1402dd2d0
005632B6  48 8B 55 40                     mov rdx, qword ptr [rbp + 0x40]
005632BA  41 3B FF                        cmp edi, r15d
005632BD  41 89 44 B5 00                  mov dword ptr [r13 + rsi*4], eax
005632C2  74 04                           je 0x1405632c8
005632C4  FF C6                           inc esi
005632C6  EB B0                           jmp 0x140563278
005632C8  C7 44 24 20 BB 00 00 00         mov dword ptr [rsp + 0x20], 0xbb
005632D0  BA 15 00 00 00                  mov edx, 0x15
005632D5  EB 80                           jmp 0x140563257
005632D7  48 8B 05 12 CF 8A 00            mov rax, qword ptr [rip + 0x8acf12]
005632DE  4C 8B 68 10                     mov r13, qword ptr [rax + 0x10]
005632E2  4C 8B A0 90 00 00 00            mov r12, qword ptr [rax + 0x90]
005632E9  4C 89 6D C0                     mov qword ptr [rbp - 0x40], r13
005632ED  45 85 F6                        test r14d, r14d
005632F0  0F 84 2E 02 00 00               je 0x140563524
005632F6  4D 85 E4                        test r12, r12
005632F9  0F 84 25 02 00 00               je 0x140563524
005632FF  38 1D FF CE 8A 00               cmp byte ptr [rip + 0x8aceff], bl
00563305  0F 85 19 02 00 00               jne 0x140563524
0056330B  38 5D 60                        cmp byte ptr [rbp + 0x60], bl
0056330E  0F 85 10 02 00 00               jne 0x140563524
00563314  48 8B 7D 48                     mov rdi, qword ptr [rbp + 0x48]
00563318  33 F6                           xor esi, esi
0056331A  4C 8B FA                        mov r15, rdx
0056331D  4C 2B FF                        sub r15, rdi
00563320  41 3B F6                        cmp esi, r14d
00563323  0F 83 FB 01 00 00               jae 0x140563524
00563329  49 8D 14 3F                     lea rdx, [r15 + rdi]
0056332D  41 B1 01                        mov r9b, 1
00563330  4C 8D 45 E0                     lea r8, [rbp - 0x20]
00563334  49 8B CD                        mov rcx, r13
00563337  49 8B C4                        mov rax, r12
0056333A  E8 91 77 15 00                  call 0x1406baad0
0056333F  8B D8                           mov ebx, eax
00563341  85 C0                           test eax, eax
00563343  0F 88 B6 01 00 00               js 0x1405634ff
00563349  41 B1 01                        mov r9b, 1
0056334C  4C 8D 45 C8                     lea r8, [rbp - 0x38]
00563350  48 8B D7                        mov rdx, rdi
00563353  49 8B CD                        mov rcx, r13
00563356  49 8B C4                        mov rax, r12
00563359  E8 72 77 15 00                  call 0x1406baad0
0056335E  8B D8                           mov ebx, eax
00563360  85 C0                           test eax, eax
00563362  0F 88 8D 01 00 00               js 0x1405634f5
00563368  8B 45 D0                        mov eax, dword ptr [rbp - 0x30]
0056336B  39 45 E8                        cmp dword ptr [rbp - 0x18], eax
0056336E  75 08                           jne 0x140563378
00563370  48 83 C7 04                     add rdi, 4
00563374  FF C6                           inc esi
00563376  EB A8                           jmp 0x140563320
00563378  33 F6                           xor esi, esi
0056337A  41 3B F6                        cmp esi, r14d
0056337D  0F 83 A1 01 00 00               jae 0x140563524
00563383  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
00563387  33 FF                           xor edi, edi
00563389  48 8B D0                        mov rdx, rax
0056338C  44 8B FF                        mov r15d, edi
0056338F  49 8B C4                        mov rax, r12
00563392  4C 8D 45 E0                     lea r8, [rbp - 0x20]
00563396  41 B1 01                        mov r9b, 1
00563399  49 8B CD                        mov rcx, r13
0056339C  E8 2F 77 15 00                  call 0x1406baad0
005633A1  8B D8                           mov ebx, eax
005633A3  85 C0                           test eax, eax
005633A5  0F 88 40 01 00 00               js 0x1405634eb
005633AB  8B 4D 58                        mov ecx, dword ptr [rbp + 0x58]
005633AE  85 FF                           test edi, edi
005633B0  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
005633B4  0F 44 4D E8                     cmove ecx, dword ptr [rbp - 0x18]
005633B8  48 83 C0 04                     add rax, 4
005633BC  FF C6                           inc esi
005633BE  89 4D 58                        mov dword ptr [rbp + 0x58], ecx
005633C1  FF C7                           inc edi
005633C3  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
005633C7  41 3B F6                        cmp esi, r14d
005633CA  73 05                           jae 0x1405633d1
005633CC  39 4D E8                        cmp dword ptr [rbp - 0x18], ecx
005633CF  74 B8                           je 0x140563389
005633D1  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
005633D5  4C 8D 45 C8                     lea r8, [rbp - 0x38]
005633D9  41 B1 01                        mov r9b, 1
005633DC  49 8B CD                        mov rcx, r13
005633DF  49 8B C4                        mov rax, r12
005633E2  E8 E9 76 15 00                  call 0x1406baad0
005633E7  8B D8                           mov ebx, eax
005633E9  85 C0                           test eax, eax
005633EB  0F 88 F0 00 00 00               js 0x1405634e1
005633F1  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
005633F5  4C 8D 45 C8                     lea r8, [rbp - 0x38]
005633F9  44 8B 6D D0                     mov r13d, dword ptr [rbp - 0x30]
005633FD  41 B1 01                        mov r9b, 1
00563400  49 8B C4                        mov rax, r12
00563403  4A 8D 14 B9                     lea rdx, [rcx + r15*4]
00563407  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
0056340B  E8 C0 76 15 00                  call 0x1406baad0
00563410  8B D8                           mov ebx, eax
00563412  85 C0                           test eax, eax
00563414  0F 88 BD 00 00 00               js 0x1405634d7
0056341A  44 8B 7D D0                     mov r15d, dword ptr [rbp - 0x30]
0056341E  45 3B EF                        cmp r13d, r15d
00563421  0F 85 94 00 00 00               jne 0x1405634bb
00563427  48 8B 05 A2 CE 8A 00            mov rax, qword ptr [rip + 0x8acea2]
0056342E  48 3B 05 AB CE 8A 00            cmp rax, qword ptr [rip + 0x8aceab]
00563435  73 15                           jae 0x14056344c
00563437  44 39 28                        cmp dword ptr [rax], r13d
0056343A  74 06                           je 0x140563442
0056343C  48 83 C0 18                     add rax, 0x18
00563440  EB EC                           jmp 0x14056342e
00563442  F3 48 0F B8 40 08               popcnt rax, qword ptr [rax + 8]
00563448  85 C0                           test eax, eax
0056344A  75 44                           jne 0x140563490
0056344C  85 FF                           test edi, edi
0056344E  75 59                           jne 0x1405634a9
00563450  4C 8B 6D C0                     mov r13, qword ptr [rbp - 0x40]
00563454  41 3B F6                        cmp esi, r14d
00563457  0F 83 C7 00 00 00               jae 0x140563524
0056345D  48 8B 55 48                     mov rdx, qword ptr [rbp + 0x48]
00563461  4C 8D 45 C8                     lea r8, [rbp - 0x38]
00563465  41 B1 01                        mov r9b, 1
00563468  49 8B CD                        mov rcx, r13
0056346B  49 8B C4                        mov rax, r12
0056346E  E8 5D 76 15 00                  call 0x1406baad0
00563473  8B D8                           mov ebx, eax
00563475  85 C0                           test eax, eax
00563477  78 26                           js 0x14056349f
00563479  44 3B 7D D0                     cmp r15d, dword ptr [rbp - 0x30]
0056347D  0F 85 F7 FE FF FF               jne 0x14056337a
00563483  C7 44 24 20 C1 01 00 00         mov dword ptr [rsp + 0x20], 0x1c1
0056348B  8D 57 1B                        lea edx, [rdi + 0x1b]
0056348E  EB 38                           jmp 0x1405634c8
00563490  C7 44 24 20 8D 01 00 00         mov dword ptr [rsp + 0x20], 0x18d
00563498  BA 1A 00 00 00                  mov edx, 0x1a
0056349D  EB 29                           jmp 0x1405634c8
0056349F  C7 44 24 20 AC 01 00 00         mov dword ptr [rsp + 0x20], 0x1ac
005634A7  EB 5E                           jmp 0x140563507
005634A9  C7 44 24 20 9C 01 00 00         mov dword ptr [rsp + 0x20], 0x19c
005634B1  BA 19 00 00 00                  mov edx, 0x19
005634B6  E9 9C FD FF FF                  jmp 0x140563257
005634BB  C7 44 24 20 74 01 00 00         mov dword ptr [rsp + 0x20], 0x174
005634C3  BA 19 00 00 00                  mov edx, 0x19
005634C8  48 8B 0D 21 CD 8A 00            mov rcx, qword ptr [rip + 0x8acd21]
005634CF  45 33 C0                        xor r8d, r8d
005634D2  E9 85 FD FF FF                  jmp 0x14056325c
005634D7  C7 44 24 20 62 01 00 00         mov dword ptr [rsp + 0x20], 0x162
005634DF  EB 26                           jmp 0x140563507
005634E1  C7 44 24 20 51 01 00 00         mov dword ptr [rsp + 0x20], 0x151
005634E9  EB 1C                           jmp 0x140563507
005634EB  C7 44 24 20 29 01 00 00         mov dword ptr [rsp + 0x20], 0x129
005634F3  EB 12                           jmp 0x140563507
005634F5  C7 44 24 20 F9 00 00 00         mov dword ptr [rsp + 0x20], 0xf9
005634FD  EB 08                           jmp 0x140563507
005634FF  C7 44 24 20 EC 00 00 00         mov dword ptr [rsp + 0x20], 0xec
00563507  48 8B 0D E2 CC 8A 00            mov rcx, qword ptr [rip + 0x8acce2]
0056350E  4C 8D 0D 0B 2A AC FF            lea r9, [rip - 0x53d5f5]
00563515  44 8B C0                        mov r8d, eax
00563518  BA 09 00 00 00                  mov edx, 9
0056351D  E8 6A 77 F2 FF                  call 0x14048ac8c
00563522  EB 3F                           jmp 0x140563563
00563524  80 7D 68 00                     cmp byte ptr [rbp + 0x68], 0
00563528  74 39                           je 0x140563563
0056352A  45 85 F6                        test r14d, r14d
0056352D  74 34                           je 0x140563563
0056352F  80 7D 60 00                     cmp byte ptr [rbp + 0x60], 0
00563533  75 1B                           jne 0x140563550
00563535  80 3D C8 CC 8A 00 00            cmp byte ptr [rip + 0x8accc8], 0
0056353C  74 12                           je 0x140563550
0056353E  C7 44 24 20 DC 01 00 00         mov dword ptr [rsp + 0x20], 0x1dc
00563546  BA 1C 00 00 00                  mov edx, 0x1c
0056354B  E9 78 FF FF FF                  jmp 0x1405634c8
00563550  48 8B 05 99 CC 8A 00            mov rax, qword ptr [rip + 0x8acc99]
00563557  8B 88 38 01 00 00               mov ecx, dword ptr [rax + 0x138]
0056355D  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
00563561  89 08                           mov dword ptr [rax], ecx
00563563  8B C3                           mov eax, ebx
00563565  48 8B 9C 24 C0 00 00 00         mov rbx, qword ptr [rsp + 0xc0]
0056356D  48 83 C4 70                     add rsp, 0x70
00563571  41 5F                           pop r15
00563573  41 5E                           pop r14
00563575  41 5D                           pop r13
00563577  41 5C                           pop r12
00563579  5F                              pop rdi
0056357A  5E                              pop rsi
0056357B  5D                              pop rbp
0056357C  C3                              ret
0056357D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpInterruptDpReplaceBegin(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned __int8 a5, unsigned __int8 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = v_rbx;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (112);
    result = 0;
    v_rbx = 0;
    v_stack_m60 = 0;
    v_stack_m48 = 0;
    v_stack_m70 = v_xmm0;
    a3 = 0;
    v_stack_m58 = v_xmm0;
loc_00563218:
    if (0 >= ((unsigned int)((unsigned int)(a4)))) goto loc_00563272;
    a2 = 0;
loc_0056321F:
    if (0 >= (*(unsigned int *)(v_rip + 9097179))) goto loc_00563245;
    a1 = (0) << (6);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 10882044));
    if ((*(unsigned __int8 *)(a1 + 13)) == 0) goto loc_00563241;
    if ((*(unsigned int *)(a1)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + a3 * 4))))) goto loc_0056324A;
loc_00563241:
    a2 = (unsigned int)((a2) + 1);
    goto loc_0056321F;
loc_00563245:
    a3 = (unsigned int)((a3) + 1);
    goto loc_00563218;
loc_0056324A:
    v_stack_m88 = 151;
loc_00563257:
    a3 = 0;
    a1 = 0;
loc_0056325C:
    result = HalpInterruptSetProblemEx(a1, 24, a3, v_rip - 5493571);
    goto loc_00563563;
loc_00563272:
    v_rsi = 0;
loc_00563278:
    if (0 >= ((unsigned int)((unsigned int)(a4)))) goto loc_005632D7;
    v_rdi = 0;
loc_0056327F:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9097082))))) goto loc_005632C2;
    a1 = (0) << (6);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 10881944));
    if ((*(unsigned __int8 *)(a1 + 12)) == ((unsigned __int8)((unsigned int)(0xC000000DULL)))) goto loc_005632A9;
    if ((*(unsigned __int8 *)(a1 + 13)) == ((unsigned __int8)((unsigned int)(0xC000000DULL)))) goto loc_005632A9;
    if ((*(unsigned int *)(a1)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + v_rsi * 4))))) goto loc_005632AD;
loc_005632A9:
    v_rdi = (unsigned int)((v_rdi) + 1);
    goto loc_0056327F;
loc_005632AD:
    a1 = (a1) + (16);
    result = KeGetProcessorIndexFromNumber(a1, v_stack_p8, a3, v_rip - 5493571);
    *(unsigned int *)(a3 + v_rsi * 4) = (unsigned int)(result);
loc_005632C2:
    if (((unsigned int)(v_rdi)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9097082))))) goto loc_005632C8;
    v_rsi = (unsigned int)((v_rsi) + 1);
    goto loc_00563278;
loc_005632C8:
    v_stack_m88 = 187;
    goto loc_00563257;
loc_005632D7:
    v_stack_m78 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9096978) + 16);
    if ((unsigned int)((unsigned int)(a4)) == 0) goto loc_00563524;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9096978) + 144) == 0) goto loc_00563524;
    if ((*(unsigned __int8 *)(v_rip + 9096959)) != ((unsigned __int8)((unsigned int)(0xC000000DULL)))) goto loc_00563524;
    if (a5 != ((unsigned __int8)((unsigned int)(0xC000000DULL)))) goto loc_00563524;
    v_rsi = 0;
    v_r15 = (21) - (v_stack_p10);
loc_00563320:
    if (0 >= ((unsigned int)((unsigned int)(a4)))) goto loc_00563524;
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9096978) + 16), v_r15 + v_stack_p10 * 1, v_stack_m58, 1);
    if (sign_flag) goto loc_005634FF;
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9096978) + 16), v_stack_p10, v_stack_m70, 1);
    if (sign_flag) goto loc_005634F5;
    if (v_stack_m50 != ((unsigned int)((unsigned int)(v_stack_m68)))) goto loc_00563378;
    v_rdi = (v_stack_p10) + (4);
    v_rsi = (unsigned int)((v_rsi) + 1);
    goto loc_00563320;
loc_00563378:
    v_rsi = 0;
loc_0056337A:
    if (0 >= ((unsigned int)((unsigned int)(a4)))) goto loc_00563524;
    v_rdi = 0;
loc_00563389:
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9096978) + 16), v_stack_p8, v_stack_m58, 1);
    if (sign_flag) goto loc_005634EB;
    a1 = (unsigned int)(v_stack_p20);
    if (0 == 0) { a1 = v_stack_m50; }
    result = (v_stack_p8) + (4);
    v_rsi = (unsigned int)((v_rsi) + 1);
    v_stack_p20 = (unsigned int)(a1);
    v_rdi = (unsigned int)((v_rdi) + 1);
    v_stack_p8 = result;
    if (((unsigned int)(v_rsi)) >= ((unsigned int)((unsigned int)(a4)))) goto loc_005633D1;
    if (v_stack_m50 == ((unsigned int)(a1))) goto loc_00563389;
loc_005633D1:
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9096978) + 16), v_stack_p10, v_stack_m70, 1);
    if (sign_flag) goto loc_005634E1;
    result = guard_dispatch_icall(v_stack_m78, v_stack_p10 + 0 * 4, v_stack_m70, 1);
    if (sign_flag) goto loc_005634D7;
    if (((unsigned int)((unsigned int)(v_stack_m68))) != ((unsigned int)((unsigned int)(v_stack_m68)))) goto loc_005634BB;
loc_0056342E:
    if ((*(unsigned __int64 *)(v_rip + 9096866)) >= (*(unsigned __int64 *)(v_rip + 9096875))) goto loc_0056344C;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9096866))) == ((unsigned int)((unsigned int)(v_stack_m68)))) goto loc_00563442;
    result = (*(unsigned __int64 *)(v_rip + 9096866)) + (24);
    goto loc_0056342E;
loc_00563442:
    if ((unsigned int)(result) != 0) goto loc_00563490;
loc_0056344C:
    if ((unsigned int)(v_rdi) != 0) goto loc_005634A9;
    if (((unsigned int)(v_rsi)) >= ((unsigned int)((unsigned int)(a4)))) goto loc_00563524;
    result = guard_dispatch_icall(v_stack_m78, v_stack_p10, v_stack_m70, 1);
    if (sign_flag) goto loc_0056349F;
    if (((unsigned int)((unsigned int)(v_stack_m68))) != v_stack_m68) goto loc_0056337A;
    v_stack_m88 = 449;
    goto loc_005634C8;
loc_00563490:
    v_stack_m88 = 397;
    goto loc_005634C8;
loc_0056349F:
    v_stack_m88 = 428;
    goto loc_00563507;
loc_005634A9:
    v_stack_m88 = 412;
    goto loc_00563257;
loc_005634BB:
    v_stack_m88 = 372;
loc_005634C8:
    a3 = 0;
    goto loc_0056325C;
loc_005634D7:
    v_stack_m88 = 354;
    goto loc_00563507;
loc_005634E1:
    v_stack_m88 = 337;
    goto loc_00563507;
loc_005634EB:
    v_stack_m88 = 297;
    goto loc_00563507;
loc_005634F5:
    v_stack_m88 = 249;
    goto loc_00563507;
loc_005634FF:
    v_stack_m88 = 236;
loc_00563507:
    result = HalpInterruptSetProblemEx(*(unsigned __int64 *)(v_rip + 9096418), 9, (unsigned int)((unsigned int)(result)), v_rip - 5494261);
    goto loc_00563563;
loc_00563524:
    if (a6 == 0) goto loc_00563563;
    if ((unsigned int)((unsigned int)(a4)) == 0) goto loc_00563563;
    if (a5 != 0) goto loc_00563550;
    if ((*(unsigned __int8 *)(v_rip + 9096392)) == 0) goto loc_00563550;
    v_stack_m88 = 476;
    goto loc_005634C8;
loc_00563550:
    *(unsigned int *)(a7) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9096345) + 312)));
loc_00563563:
    v_rsp = (v_rsp) + (112);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t HalpInterruptDpReplaceBegin(int64_t Arg1, void *Arg2, void *Arg3, int32_t Arg4, uint8_t Arg5, uint8_t Arg6, void *Arg7)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m88;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p18 = local_rbx;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (112);
    result = 0;
    local_rbx = 0;
    v_stack_m60 = 0;
    v_stack_m48 = 0;
    v_stack_m70 = v_xmm0;
    Arg3 = 0;
    v_stack_m58 = v_xmm0;
loc_00563218:
    if (0 >= ((uint32_t)((uint32_t)(Arg4)))) goto loc_00563272;
    Arg2 = 0;
loc_0056321F:
    if (0 >= (*(uint32_t *)(v_rip + 0x8ACFDB))) goto loc_00563245;
    Arg1 = (0) << (6);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xA60BFC));
    if ((*(uint8_t *)(Arg1 + 0xD)) == 0) goto loc_00563241;
    if ((*(uint32_t *)(Arg1)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + arg3 * 4))))) goto loc_0056324A;
loc_00563241:
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_0056321F;
loc_00563245:
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_00563218;
loc_0056324A:
    v_stack_m88 = 151;
loc_00563257:
    Arg3 = 0;
    Arg1 = 0;
loc_0056325C:
    result = HalpInterruptSetProblemEx(Arg1, 24, Arg3, v_rip - 5493571);
    goto loc_00563563;
loc_00563272:
    local_rsi = 0;
loc_00563278:
    if (0 >= ((uint32_t)((uint32_t)(Arg4)))) goto loc_005632D7;
    local_rdi = 0;
loc_0056327F:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8ACF7A))))) goto loc_005632C2;
    Arg1 = (0) << (6);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xA60B98));
    if ((*(uint8_t *)(Arg1 + 0xC)) == ((uint8_t)((uint32_t)(0xC000000DULL)))) goto loc_005632A9;
    if ((*(uint8_t *)(Arg1 + 0xD)) == ((uint8_t)((uint32_t)(0xC000000DULL)))) goto loc_005632A9;
    if ((*(uint32_t *)(Arg1)) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + local_rsi * 4))))) goto loc_005632AD;
loc_005632A9:
    local_rdi = (uint32_t)((local_rdi) + 1);
    goto loc_0056327F;
loc_005632AD:
    Arg1 = (Arg1) + (16);
    result = KeGetProcessorIndexFromNumber(Arg1, v_stack_p8, Arg3, v_rip - 5493571);
    *(uint32_t *)(arg3 + local_rsi * 4) = (uint32_t)(result);
loc_005632C2:
    if (((uint32_t)(local_rdi)) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8ACF7A))))) goto loc_005632C8;
    local_rsi = (uint32_t)((local_rsi) + 1);
    goto loc_00563278;
loc_005632C8:
    v_stack_m88 = 187;
    goto loc_00563257;
loc_005632D7:
    v_stack_m78 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x8ACF12) + 0x10);
    if ((uint32_t)((uint32_t)(Arg4)) == 0) goto loc_00563524;
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x8ACF12) + 0x90) == 0) goto loc_00563524;
    if ((*(uint8_t *)(v_rip + 0x8ACEFF)) != ((uint8_t)((uint32_t)(0xC000000DULL)))) goto loc_00563524;
    if (Arg5 != ((uint8_t)((uint32_t)(0xC000000DULL)))) goto loc_00563524;
    local_rsi = 0;
    local_r15 = (21) - (v_stack_p10);
loc_00563320:
    if (0 >= ((uint32_t)((uint32_t)(Arg4)))) goto loc_00563524;
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(v_rip + 0x8ACF12) + 0x10), local_r15 + v_stack_p10 * 1, v_stack_m58, 1);
    if (sign_flag) goto loc_005634FF;
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(v_rip + 0x8ACF12) + 0x10), v_stack_p10, v_stack_m70, 1);
    if (sign_flag) goto loc_005634F5;
    if (v_stack_m50 != ((uint32_t)((uint32_t)(v_stack_m68)))) goto loc_00563378;
    local_rdi = (v_stack_p10) + (4);
    local_rsi = (uint32_t)((local_rsi) + 1);
    goto loc_00563320;
loc_00563378:
    local_rsi = 0;
loc_0056337A:
    if (0 >= ((uint32_t)((uint32_t)(Arg4)))) goto loc_00563524;
    local_rdi = 0;
loc_00563389:
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(v_rip + 0x8ACF12) + 0x10), v_stack_p8, v_stack_m58, 1);
    if (sign_flag) goto loc_005634EB;
    Arg1 = (uint32_t)(v_stack_p20);
    if (0 == 0) { Arg1 = v_stack_m50; }
    result = (v_stack_p8) + (4);
    local_rsi = (uint32_t)((local_rsi) + 1);
    v_stack_p20 = (uint32_t)(Arg1);
    local_rdi = (uint32_t)((local_rdi) + 1);
    v_stack_p8 = result;
    if (((uint32_t)(local_rsi)) >= ((uint32_t)((uint32_t)(Arg4)))) goto loc_005633D1;
    if (v_stack_m50 == ((uint32_t)(Arg1))) goto loc_00563389;
loc_005633D1:
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(v_rip + 0x8ACF12) + 0x10), v_stack_p10, v_stack_m70, 1);
    if (sign_flag) goto loc_005634E1;
    result = guard_dispatch_icall(v_stack_m78, v_stack_p10 + 0 * 4, v_stack_m70, 1);
    if (sign_flag) goto loc_005634D7;
    if (((uint32_t)((uint32_t)(v_stack_m68))) != ((uint32_t)((uint32_t)(v_stack_m68)))) goto loc_005634BB;
loc_0056342E:
    if ((*(uint64_t *)(v_rip + 0x8ACEA2)) >= (*(uint64_t *)(v_rip + 0x8ACEAB))) goto loc_0056344C;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x8ACEA2))) == ((uint32_t)((uint32_t)(v_stack_m68)))) goto loc_00563442;
    result = (*(uint64_t *)(v_rip + 0x8ACEA2)) + (24);
    goto loc_0056342E;
loc_00563442:
    if ((uint32_t)(result) != 0) goto loc_00563490;
loc_0056344C:
    if ((uint32_t)(local_rdi) != 0) goto loc_005634A9;
    if (((uint32_t)(local_rsi)) >= ((uint32_t)((uint32_t)(Arg4)))) goto loc_00563524;
    result = guard_dispatch_icall(v_stack_m78, v_stack_p10, v_stack_m70, 1);
    if (sign_flag) goto loc_0056349F;
    if (((uint32_t)((uint32_t)(v_stack_m68))) != v_stack_m68) goto loc_0056337A;
    v_stack_m88 = 449;
    goto loc_005634C8;
loc_00563490:
    v_stack_m88 = 397;
    goto loc_005634C8;
loc_0056349F:
    v_stack_m88 = 428;
    goto loc_00563507;
loc_005634A9:
    v_stack_m88 = 412;
    goto loc_00563257;
loc_005634BB:
    v_stack_m88 = 372;
loc_005634C8:
    Arg3 = 0;
    goto loc_0056325C;
loc_005634D7:
    v_stack_m88 = 354;
    goto loc_00563507;
loc_005634E1:
    v_stack_m88 = 337;
    goto loc_00563507;
loc_005634EB:
    v_stack_m88 = 297;
    goto loc_00563507;
loc_005634F5:
    v_stack_m88 = 249;
    goto loc_00563507;
loc_005634FF:
    v_stack_m88 = 236;
loc_00563507:
    result = HalpInterruptSetProblemEx(*(uint64_t *)(v_rip + 0x8ACCE2), 9, (uint32_t)((uint32_t)(result)), v_rip - 5494261);
    goto loc_00563563;
loc_00563524:
    if (Arg6 == 0) goto loc_00563563;
    if ((uint32_t)((uint32_t)(Arg4)) == 0) goto loc_00563563;
    if (Arg5 != 0) goto loc_00563550;
    if ((*(uint8_t *)(v_rip + 0x8ACCC8)) == 0) goto loc_00563550;
    v_stack_m88 = 476;
    goto loc_005634C8;
loc_00563550:
    *(uint32_t *)(arg7) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8ACC99) + 0x138)));
loc_00563563:
    local_rsp = (local_rsp) + (112);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0 + r8*4` | `32` | `R` |
| `Arg3` | `+ 0x0 + rsi*4` | `32` | `W` |
| `Arg7` | `+ 0x0` | `32` | `R/W` |
| `Arg7` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005631CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
