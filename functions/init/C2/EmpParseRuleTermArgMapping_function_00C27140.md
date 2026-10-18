# EmpParseRuleTermArgMapping

- RVA: `0x00C27140`–`0x00C27454` (길이 `788` bytes)
- VA: `0x0000000140C27140`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C5BF4`
- 디코드: `210`개 명령, `788/788` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00C2721F` → [strtoul](../../text/4F/strtoul_function_004FF3B8.md) (function, `0x004FF3B8`)
- `0x00C272DF` → [strtoul](../../text/4F/strtoul_function_004FF3B8.md) (function, `0x004FF3B8`)
- `0x00C273CC` → [strtoul](../../text/4F/strtoul_function_004FF3B8.md) (function, `0x004FF3B8`)

### Direct callers
- [EmpParseRuleTerm](EmpParseRuleTerm_function_00C26FC0.md) at `0x00C270EE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00C2721F` → [strtoul](../../text/4F/strtoul_function_004FF3B8.md) (`INIT` → `.text`)
  - `0x00C272DF` → [strtoul](../../text/4F/strtoul_function_004FF3B8.md) (`INIT` → `.text`)
  - `0x00C273CC` → [strtoul](../../text/4F/strtoul_function_004FF3B8.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C27140  48 8B C4                        mov rax, rsp
00C27143  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
00C27147  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00C2714B  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00C2714F  53                              push rbx
00C27150  55                              push rbp
00C27151  56                              push rsi
00C27152  57                              push rdi
00C27153  41 54                           push r12
00C27155  41 55                           push r13
00C27157  41 56                           push r14
00C27159  41 57                           push r15
00C2715B  48 83 EC 38                     sub rsp, 0x38
00C2715F  48 8B FA                        mov rdi, rdx
00C27162  47 8D 2C 08                     lea r13d, [r8 + r9]
00C27166  44 03 AC 24 A0 00 00 00         add r13d, dword ptr [rsp + 0xa0]
00C2716E  33 D2                           xor edx, edx
00C27170  4C 8B F1                        mov r14, rcx
00C27173  89 94 24 80 00 00 00            mov dword ptr [rsp + 0x80], edx
00C2717A  33 C9                           xor ecx, ecx
00C2717C  45 32 FF                        xor r15b, r15b
00C2717F  32 DB                           xor bl, bl
00C27181  48 89 48 A8                     mov qword ptr [rax - 0x58], rcx
00C27185  33 ED                           xor ebp, ebp
00C27187  45 33 E4                        xor r12d, r12d
00C2718A  33 F6                           xor esi, esi
00C2718C  48 85 FF                        test rdi, rdi
00C2718F  75 04                           jne 0x140c27195
00C27191  32 C0                           xor al, al
00C27193  EB 6A                           jmp 0x140c271ff
00C27195  84 DB                           test bl, bl
00C27197  75 63                           jne 0x140c271fc
00C27199  83 FE 05                        cmp esi, 5
00C2719C  0F 87 9E 01 00 00               ja 0x140c27340
00C271A2  0F 84 80 01 00 00               je 0x140c27328
00C271A8  8B C6                           mov eax, esi
00C271AA  85 F6                           test esi, esi
00C271AC  0F 84 70 01 00 00               je 0x140c27322
00C271B2  83 E8 01                        sub eax, 1
00C271B5  0F 84 07 01 00 00               je 0x140c272c2
00C271BB  83 E8 01                        sub eax, 1
00C271BE  0F 84 DF 00 00 00               je 0x140c272a3
00C271C4  83 E8 01                        sub eax, 1
00C271C7  0F 84 9E 00 00 00               je 0x140c2726b
00C271CD  83 F8 01                        cmp eax, 1
00C271D0  75 18                           jne 0x140c271ea
00C271D2  41 80 3E 29                     cmp byte ptr [r14], 0x29
00C271D6  0F 84 85 00 00 00               je 0x140c27261
00C271DC  41 8D 3C 2C                     lea edi, [r12 + rbp]
00C271E0  41 3B FD                        cmp edi, r13d
00C271E3  72 2C                           jb 0x140c27211
00C271E5  B3 01                           mov bl, 1
00C271E7  44 8A FB                        mov r15b, bl
00C271EA  49 FF C6                        inc r14
00C271ED  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
00C271F5  45 84 FF                        test r15b, r15b
00C271F8  74 9B                           je 0x140c27195
00C271FA  84 DB                           test bl, bl
00C271FC  0F 94 C0                        sete al
00C271FF  48 83 C4 38                     add rsp, 0x38
00C27203  41 5F                           pop r15
00C27205  41 5E                           pop r14
00C27207  41 5D                           pop r13
00C27209  41 5C                           pop r12
00C2720B  5F                              pop rdi
00C2720C  5E                              pop rsi
00C2720D  5D                              pop rbp
00C2720E  5B                              pop rbx
00C2720F  C3                              ret
00C27210  CC                              int3
00C27211  41 B8 0A 00 00 00               mov r8d, 0xa
00C27217  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
00C2721C  49 8B CE                        mov rcx, r14
00C2721F  E8 94 81 8D FF                  call 0x1404ff3b8
00C27224  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
00C2722C  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
00C27231  44 8B 8C 24 98 00 00 00         mov r9d, dword ptr [rsp + 0x98]
00C27239  44 8B 84 24 90 00 00 00         mov r8d, dword ptr [rsp + 0x90]
00C27241  89 04 BA                        mov dword ptr [rdx + rdi*4], eax
00C27244  8B 94 24 80 00 00 00            mov edx, dword ptr [rsp + 0x80]
00C2724B  4C 3B F1                        cmp r14, rcx
00C2724E  0F 84 E6 01 00 00               je 0x140c2743a
00C27254  BE 05 00 00 00                  mov esi, 5
00C27259  41 FF C4                        inc r12d
00C2725C  E9 DB 01 00 00                  jmp 0x140c2743c
00C27261  BE 06 00 00 00                  mov esi, 6
00C27266  E9 D1 01 00 00                  jmp 0x140c2743c
00C2726B  41 8A 06                        mov al, byte ptr [r14]
00C2726E  84 C0                           test al, al
00C27270  74 15                           je 0x140c27287
00C27272  3C 28                           cmp al, 0x28
00C27274  74 07                           je 0x140c2727d
00C27276  B3 01                           mov bl, 1
00C27278  E9 6D FF FF FF                  jmp 0x140c271ea
00C2727D  BE 04 00 00 00                  mov esi, 4
00C27282  E9 63 FF FF FF                  jmp 0x140c271ea
00C27287  41 3B E8                        cmp ebp, r8d
00C2728A  75 EA                           jne 0x140c27276
00C2728C  45 85 C9                        test r9d, r9d
00C2728F  75 E5                           jne 0x140c27276
00C27291  44 39 8C 24 A0 00 00 00         cmp dword ptr [rsp + 0xa0], r9d
00C27299  75 DB                           jne 0x140c27276
00C2729B  41 B7 01                        mov r15b, 1
00C2729E  E9 47 FF FF FF                  jmp 0x140c271ea
00C272A3  41 8A 06                        mov al, byte ptr [r14]
00C272A6  3C 29                           cmp al, 0x29
00C272A8  74 0E                           je 0x140c272b8
00C272AA  3C 2E                           cmp al, 0x2e
00C272AC  75 C8                           jne 0x140c27276
00C272AE  BE 01 00 00 00                  mov esi, 1
00C272B3  E9 32 FF FF FF                  jmp 0x140c271ea
00C272B8  BE 03 00 00 00                  mov esi, 3
00C272BD  E9 28 FF FF FF                  jmp 0x140c271ea
00C272C2  41 80 3E 29                     cmp byte ptr [r14], 0x29
00C272C6  74 50                           je 0x140c27318
00C272C8  41 3B ED                        cmp ebp, r13d
00C272CB  0F 83 14 FF FF FF               jae 0x140c271e5
00C272D1  41 B8 0A 00 00 00               mov r8d, 0xa
00C272D7  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
00C272DC  49 8B CE                        mov rcx, r14
00C272DF  E8 D4 80 8D FF                  call 0x1404ff3b8
00C272E4  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
00C272E9  44 8B 8C 24 98 00 00 00         mov r9d, dword ptr [rsp + 0x98]
00C272F1  44 8B 84 24 90 00 00 00         mov r8d, dword ptr [rsp + 0x90]
00C272F9  8B 94 24 80 00 00 00            mov edx, dword ptr [rsp + 0x80]
00C27300  89 04 AF                        mov dword ptr [rdi + rbp*4], eax
00C27303  4C 3B F1                        cmp r14, rcx
00C27306  0F 84 2E 01 00 00               je 0x140c2743a
00C2730C  BE 02 00 00 00                  mov esi, 2
00C27311  FF C5                           inc ebp
00C27313  E9 24 01 00 00                  jmp 0x140c2743c
00C27318  BE 03 00 00 00                  mov esi, 3
00C2731D  E9 1A 01 00 00                  jmp 0x140c2743c
00C27322  41 80 3E 28                     cmp byte ptr [r14], 0x28
00C27326  EB 84                           jmp 0x140c272ac
00C27328  41 8A 06                        mov al, byte ptr [r14]
00C2732B  3C 29                           cmp al, 0x29
00C2732D  74 07                           je 0x140c27336
00C2732F  3C 2E                           cmp al, 0x2e
00C27331  E9 3E FF FF FF                  jmp 0x140c27274
00C27336  BE 06 00 00 00                  mov esi, 6
00C2733B  E9 AA FE FF FF                  jmp 0x140c271ea
00C27340  8B C6                           mov eax, esi
00C27342  83 E8 06                        sub eax, 6
00C27345  0F 84 C9 00 00 00               je 0x140c27414
00C2734B  83 E8 01                        sub eax, 1
00C2734E  74 59                           je 0x140c273a9
00C27350  83 E8 01                        sub eax, 1
00C27353  74 31                           je 0x140c27386
00C27355  83 F8 01                        cmp eax, 1
00C27358  0F 85 8C FE FF FF               jne 0x140c271ea
00C2735E  41 80 3E 00                     cmp byte ptr [r14], 0
00C27362  0F 85 0E FF FF FF               jne 0x140c27276
00C27368  41 3B E8                        cmp ebp, r8d
00C2736B  0F 85 05 FF FF FF               jne 0x140c27276
00C27371  45 3B E1                        cmp r12d, r9d
00C27374  0F 85 FC FE FF FF               jne 0x140c27276
00C2737A  3B 94 24 A0 00 00 00            cmp edx, dword ptr [rsp + 0xa0]
00C27381  E9 13 FF FF FF                  jmp 0x140c27299
00C27386  41 8A 06                        mov al, byte ptr [r14]
00C27389  3C 29                           cmp al, 0x29
00C2738B  74 12                           je 0x140c2739f
00C2738D  3C 2E                           cmp al, 0x2e
00C2738F  0F 85 E1 FE FF FF               jne 0x140c27276
00C27395  BE 07 00 00 00                  mov esi, 7
00C2739A  E9 4B FE FF FF                  jmp 0x140c271ea
00C2739F  BE 09 00 00 00                  mov esi, 9
00C273A4  E9 41 FE FF FF                  jmp 0x140c271ea
00C273A9  41 80 3E 29                     cmp byte ptr [r14], 0x29
00C273AD  74 5E                           je 0x140c2740d
00C273AF  41 8D 3C 14                     lea edi, [r12 + rdx]
00C273B3  03 FD                           add edi, ebp
00C273B5  41 3B FD                        cmp edi, r13d
00C273B8  0F 83 27 FE FF FF               jae 0x140c271e5
00C273BE  41 B8 0A 00 00 00               mov r8d, 0xa
00C273C4  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
00C273C9  49 8B CE                        mov rcx, r14
00C273CC  E8 E7 7F 8D FF                  call 0x1404ff3b8
00C273D1  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
00C273D9  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
00C273DE  44 8B 8C 24 98 00 00 00         mov r9d, dword ptr [rsp + 0x98]
00C273E6  44 8B 84 24 90 00 00 00         mov r8d, dword ptr [rsp + 0x90]
00C273EE  89 04 BA                        mov dword ptr [rdx + rdi*4], eax
00C273F1  8B 94 24 80 00 00 00            mov edx, dword ptr [rsp + 0x80]
00C273F8  4C 3B F1                        cmp r14, rcx
00C273FB  74 3D                           je 0x140c2743a
00C273FD  FF C2                           inc edx
00C273FF  BE 08 00 00 00                  mov esi, 8
00C27404  89 94 24 80 00 00 00            mov dword ptr [rsp + 0x80], edx
00C2740B  EB 2F                           jmp 0x140c2743c
00C2740D  BE 09 00 00 00                  mov esi, 9
00C27412  EB 28                           jmp 0x140c2743c
00C27414  41 8A 06                        mov al, byte ptr [r14]
00C27417  84 C0                           test al, al
00C27419  74 07                           je 0x140c27422
00C2741B  3C 28                           cmp al, 0x28
00C2741D  E9 6D FF FF FF                  jmp 0x140c2738f
00C27422  41 3B E8                        cmp ebp, r8d
00C27425  75 13                           jne 0x140c2743a
00C27427  45 3B E1                        cmp r12d, r9d
00C2742A  75 0E                           jne 0x140c2743a
00C2742C  83 BC 24 A0 00 00 00 00         cmp dword ptr [rsp + 0xa0], 0
00C27434  0F 84 61 FE FF FF               je 0x140c2729b
00C2743A  B3 01                           mov bl, 1
00C2743C  48 85 C9                        test rcx, rcx
00C2743F  0F 84 A5 FD FF FF               je 0x140c271ea
00C27445  4C 8B F1                        mov r14, rcx
00C27448  33 C9                           xor ecx, ecx
00C2744A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00C2744F  E9 99 FD FF FF                  jmp 0x140c271ed
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EmpParseRuleTermArgMapping(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;
    unsigned int v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned int v_stack_p90;
    unsigned int v_stack_p98;

    *(unsigned int *)(v_rsp + 32) = (unsigned int)(a4);
    *(unsigned int *)(v_rsp + 24) = (unsigned int)(a3);
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (56);
    v_r13 = (unsigned int)((a3 + a4 * 1) + (a5));
    a2 = 0;
    v_stack_p8 = 0;
    a1 = 0;
    v_r15 = 0;
    v_rbx = 0;
    *(unsigned __int64 *)(v_rsp - 88) = 0;
    v_rbp = 0;
    v_r12 = 0;
    v_rsi = 0;
    if (0 != 0) goto loc_00C27195;
    result = 0;
    goto loc_00C271FF;
loc_00C27195:
    if (0 != 0) goto loc_00C271FC;
    if (0 > 5) goto loc_00C27340;
    if (0 == 5) goto loc_00C27328;
    if (0 == 0) goto loc_00C27322;
    result = (unsigned int)((0) - (1));
    if (condition_is_equal) goto loc_00C272C2;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00C272A3;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00C2726B;
    if (((unsigned int)(result)) != 1) goto loc_00C271EA;
    if ((*(unsigned __int8 *)(a1)) == 41) goto loc_00C27261;
    if (((unsigned int)(v_r12 + v_rbp * 1)) < ((unsigned int)(v_r13))) goto loc_00C27211;
loc_00C271E5:
loc_00C271EA:
    v_r14 = (a1) + 1;
loc_00C271ED:
    if (1 == 0) goto loc_00C27195;
loc_00C271FC:
    result = (1 == 0) ? 1 : 0;
loc_00C271FF:
    v_rsp = (v_rsp) + (56);
    return result;
loc_00C27211:
    result = strtoul(v_r14, v_stack_p20, 10, a4);
    *(unsigned int *)(v_stack_p88 + v_stack_p10 * 4) = (unsigned int)(result);
    if (v_r14 == v_stack_p20) goto loc_00C2743A;
    v_r12 = (unsigned int)((v_r12) + 1);
    goto loc_00C2743C;
loc_00C27261:
    goto loc_00C2743C;
loc_00C2726B:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_r14)) == 0) goto loc_00C27287;
loc_00C27274:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r14))) == 40) goto loc_00C2727D;
loc_00C27276:
    goto loc_00C271EA;
loc_00C2727D:
    goto loc_00C271EA;
loc_00C27287:
    if (0 != ((unsigned int)((unsigned int)(v_stack_p90)))) goto loc_00C27276;
    if ((unsigned int)((unsigned int)(v_stack_p98)) != 0) goto loc_00C27276;
loc_00C27299:
    if (a5 != ((unsigned int)((unsigned int)(v_stack_p98)))) goto loc_00C27276;
loc_00C2729B:
    goto loc_00C271EA;
loc_00C272A3:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r14))) == 41) goto loc_00C272B8;
loc_00C272AC:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r14))) != 46) goto loc_00C27276;
    goto loc_00C271EA;
loc_00C272B8:
    goto loc_00C271EA;
loc_00C272C2:
    if ((*(unsigned __int8 *)(v_r14)) == 41) goto loc_00C27318;
    if (0 >= ((unsigned int)(v_r13))) goto loc_00C271E5;
    result = strtoul(v_r14, v_stack_p20, 10, (unsigned int)(v_stack_p98));
    *(unsigned int *)(v_stack_p10 + v_rbp * 4) = (unsigned int)(result);
    if (v_r14 == v_stack_p20) goto loc_00C2743A;
    v_rbp = (unsigned int)((v_rbp) + 1);
    goto loc_00C2743C;
loc_00C27318:
    goto loc_00C2743C;
loc_00C27322:
    goto loc_00C272AC;
loc_00C27328:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r14))) == 41) goto loc_00C27336;
    goto loc_00C27274;
loc_00C27336:
    goto loc_00C271EA;
loc_00C27340:
    result = (unsigned int)((6) - (6));
    if (condition_is_equal) goto loc_00C27414;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00C273A9;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00C27386;
    if (((unsigned int)(result)) != 1) goto loc_00C271EA;
    if ((*(unsigned __int8 *)(v_r14)) != 0) goto loc_00C27276;
    if (((unsigned int)(v_rbp)) != ((unsigned int)((unsigned int)(v_stack_p90)))) goto loc_00C27276;
    if (((unsigned int)(v_r12)) != ((unsigned int)((unsigned int)(v_stack_p98)))) goto loc_00C27276;
    goto loc_00C27299;
loc_00C27386:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r14))) == 41) goto loc_00C2739F;
loc_00C2738F:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r14))) != 46) goto loc_00C27276;
    goto loc_00C271EA;
loc_00C2739F:
    goto loc_00C271EA;
loc_00C273A9:
    if ((*(unsigned __int8 *)(v_r14)) == 41) goto loc_00C2740D;
    v_rdi = (unsigned int)((v_r12 + (unsigned int)(v_stack_p80) * 1) + ((unsigned int)(v_rbp)));
    if (((unsigned int)(v_rdi)) >= ((unsigned int)(v_r13))) goto loc_00C271E5;
    result = strtoul(v_r14, v_stack_p20, 10, (unsigned int)(v_stack_p98));
    *(unsigned int *)(v_stack_p88 + v_rdi * 4) = (unsigned int)(result);
    if (v_r14 == v_stack_p20) goto loc_00C2743A;
    a2 = (unsigned int)(((unsigned int)(v_stack_p80)) + 1);
    v_stack_p80 = (unsigned int)(a2);
    goto loc_00C2743C;
loc_00C2740D:
    goto loc_00C2743C;
loc_00C27414:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_r14)) == 0) goto loc_00C27422;
    goto loc_00C2738F;
loc_00C27422:
    if (((unsigned int)(v_rbp)) != ((unsigned int)((unsigned int)(v_stack_p90)))) goto loc_00C2743A;
    if (((unsigned int)(v_r12)) != ((unsigned int)((unsigned int)(v_stack_p98)))) goto loc_00C2743A;
    if (a5 == 0) goto loc_00C2729B;
loc_00C2743A:
loc_00C2743C:
    if (v_stack_p20 == 0) goto loc_00C271EA;
    a1 = 0;
    v_stack_p20 = 0;
    goto loc_00C271ED;
}
```

## 5. (Beta) C Style

```c
int64_t EmpParseRuleTermArgMapping(int64_t Arg1, int64_t Arg2, void *Arg3, int64_t Arg4, uint32_t Arg5)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;
    uint32_t v_stack_p80;
    uint64_t v_stack_p88;
    uint32_t v_stack_p90;
    uint32_t v_stack_p98;

    *(uint32_t *)(local_rsp + 0x20) = (uint32_t)(Arg4);
    *(uint32_t *)(local_rsp + 0x18) = (uint32_t)(Arg3);
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (56);
    local_r13 = (uint32_t)((Arg3 + Arg4 * 1) + (Arg5));
    Arg2 = 0;
    v_stack_p8 = 0;
    Arg1 = 0;
    local_r15 = 0;
    local_rbx = 0;
    *(uint64_t *)(local_rsp - 0x58) = 0;
    local_rbp = 0;
    local_r12 = 0;
    local_rsi = 0;
    if (0 != 0) goto loc_00C27195;
    result = 0;
    goto loc_00C271FF;
loc_00C27195:
    if (0 != 0) goto loc_00C271FC;
    if (0 > 5) goto loc_00C27340;
    if (0 == 5) goto loc_00C27328;
    if (0 == 0) goto loc_00C27322;
    result = (uint32_t)((0) - (1));
    if (condition_is_equal) goto loc_00C272C2;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00C272A3;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00C2726B;
    if (((uint32_t)(result)) != 1) goto loc_00C271EA;
    if ((*(uint8_t *)(Arg1)) == 41) goto loc_00C27261;
    if (((uint32_t)(local_r12 + local_rbp * 1)) < ((uint32_t)(local_r13))) goto loc_00C27211;
loc_00C271E5:
loc_00C271EA:
    local_r14 = (Arg1) + 1;
loc_00C271ED:
    if (1 == 0) goto loc_00C27195;
loc_00C271FC:
    result = (1 == 0) ? 1 : 0;
loc_00C271FF:
    local_rsp = (local_rsp) + (56);
    return result;
loc_00C27211:
    result = strtoul(local_r14, v_stack_p20, 10, Arg4);
    *(uint32_t *)(v_stack_p88 + v_stack_p10 * 4) = (uint32_t)(result);
    if (local_r14 == v_stack_p20) goto loc_00C2743A;
    local_r12 = (uint32_t)((local_r12) + 1);
    goto loc_00C2743C;
loc_00C27261:
    goto loc_00C2743C;
loc_00C2726B:
    if ((uint8_t)(*(uint8_t *)(local_r14)) == 0) goto loc_00C27287;
loc_00C27274:
    if (((uint8_t)(*(uint8_t *)(local_r14))) == 40) goto loc_00C2727D;
loc_00C27276:
    goto loc_00C271EA;
loc_00C2727D:
    goto loc_00C271EA;
loc_00C27287:
    if (0 != ((uint32_t)((uint32_t)(v_stack_p90)))) goto loc_00C27276;
    if ((uint32_t)((uint32_t)(v_stack_p98)) != 0) goto loc_00C27276;
loc_00C27299:
    if (Arg5 != ((uint32_t)((uint32_t)(v_stack_p98)))) goto loc_00C27276;
loc_00C2729B:
    goto loc_00C271EA;
loc_00C272A3:
    if (((uint8_t)(*(uint8_t *)(local_r14))) == 41) goto loc_00C272B8;
loc_00C272AC:
    if (((uint8_t)(*(uint8_t *)(local_r14))) != 46) goto loc_00C27276;
    goto loc_00C271EA;
loc_00C272B8:
    goto loc_00C271EA;
loc_00C272C2:
    if ((*(uint8_t *)(local_r14)) == 41) goto loc_00C27318;
    if (0 >= ((uint32_t)(local_r13))) goto loc_00C271E5;
    result = strtoul(local_r14, v_stack_p20, 10, (uint32_t)(v_stack_p98));
    *(uint32_t *)(v_stack_p10 + local_rbp * 4) = (uint32_t)(result);
    if (local_r14 == v_stack_p20) goto loc_00C2743A;
    local_rbp = (uint32_t)((local_rbp) + 1);
    goto loc_00C2743C;
loc_00C27318:
    goto loc_00C2743C;
loc_00C27322:
    goto loc_00C272AC;
loc_00C27328:
    if (((uint8_t)(*(uint8_t *)(local_r14))) == 41) goto loc_00C27336;
    goto loc_00C27274;
loc_00C27336:
    goto loc_00C271EA;
loc_00C27340:
    result = (uint32_t)((6) - (6));
    if (condition_is_equal) goto loc_00C27414;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00C273A9;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00C27386;
    if (((uint32_t)(result)) != 1) goto loc_00C271EA;
    if ((*(uint8_t *)(local_r14)) != 0) goto loc_00C27276;
    if (((uint32_t)(local_rbp)) != ((uint32_t)((uint32_t)(v_stack_p90)))) goto loc_00C27276;
    if (((uint32_t)(local_r12)) != ((uint32_t)((uint32_t)(v_stack_p98)))) goto loc_00C27276;
    goto loc_00C27299;
loc_00C27386:
    if (((uint8_t)(*(uint8_t *)(local_r14))) == 41) goto loc_00C2739F;
loc_00C2738F:
    if (((uint8_t)(*(uint8_t *)(local_r14))) != 46) goto loc_00C27276;
    goto loc_00C271EA;
loc_00C2739F:
    goto loc_00C271EA;
loc_00C273A9:
    if ((*(uint8_t *)(local_r14)) == 41) goto loc_00C2740D;
    local_rdi = (uint32_t)((local_r12 + (uint32_t)(v_stack_p80) * 1) + ((uint32_t)(local_rbp)));
    if (((uint32_t)(local_rdi)) >= ((uint32_t)(local_r13))) goto loc_00C271E5;
    result = strtoul(local_r14, v_stack_p20, 10, (uint32_t)(v_stack_p98));
    *(uint32_t *)(v_stack_p88 + local_rdi * 4) = (uint32_t)(result);
    if (local_r14 == v_stack_p20) goto loc_00C2743A;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_p80)) + 1);
    v_stack_p80 = (uint32_t)(Arg2);
    goto loc_00C2743C;
loc_00C2740D:
    goto loc_00C2743C;
loc_00C27414:
    if ((uint8_t)(*(uint8_t *)(local_r14)) == 0) goto loc_00C27422;
    goto loc_00C2738F;
loc_00C27422:
    if (((uint32_t)(local_rbp)) != ((uint32_t)((uint32_t)(v_stack_p90)))) goto loc_00C2743A;
    if (((uint32_t)(local_r12)) != ((uint32_t)((uint32_t)(v_stack_p98)))) goto loc_00C2743A;
    if (Arg5 == 0) goto loc_00C2729B;
loc_00C2743A:
loc_00C2743C:
    if (v_stack_p20 == 0) goto loc_00C271EA;
    Arg1 = 0;
    v_stack_p20 = 0;
    goto loc_00C271ED;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0 + r9*1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C27140&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
