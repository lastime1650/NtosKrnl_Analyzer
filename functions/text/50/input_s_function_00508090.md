# input_s

- RVA: `0x00508090`–`0x0050892F` (길이 `2,207` bytes)
- VA: `0x0000000140508090`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C29B0`
- 디코드: `678`개 명령, `2,207/2,207` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0050811C` → [_inc](_inc_function_00508060.md) (function, `0x00508060`)
- `0x00508144` → [ungetc_nolock](ungetc_nolock_function_00509824.md) (function, `0x00509824`)
- `0x0050831E` → [_inc](_inc_function_00508060.md) (function, `0x00508060`)
- `0x0050834E` → [_inc](_inc_function_00508060.md) (function, `0x00508060`)
- `0x005084BF` → [_inc](_inc_function_00508060.md) (function, `0x00508060`)
- `0x005084DA` → [_inc](_inc_function_00508060.md) (function, `0x00508060`)
- `0x00508529` → [ungetc_nolock](ungetc_nolock_function_00509824.md) (function, `0x00509824`)
- `0x00508544` → [_inc](_inc_function_00508060.md) (function, `0x00508060`)
- `0x00508596` → [_inc](_inc_function_00508060.md) (function, `0x00508060`)
- `0x0050864D` → [_inc](_inc_function_00508060.md) (function, `0x00508060`)
- `0x00508673` → [ungetc_nolock](ungetc_nolock_function_00509824.md) (function, `0x00509824`)
- `0x00508721` → [_inc](_inc_function_00508060.md) (function, `0x00508060`)
- `0x00508747` → [ungetc_nolock](ungetc_nolock_function_00509824.md) (function, `0x00509824`)
- `0x005087FA` → [ReadStringDelimited](ReadStringDelimited_function_00507F00.md) (function, `0x00507F00`)
- `0x00508807` → [ReadString](ReadString_function_00507D40.md) (function, `0x00507D40`)
- `0x00508833` → [_inc](_inc_function_00508060.md) (function, `0x00508060`)
- `0x0050887D` → [ungetc_nolock](ungetc_nolock_function_00509824.md) (function, `0x00509824`)
- `0x005088C9` → [ungetc_nolock](ungetc_nolock_function_00509824.md) (function, `0x00509824`)
- `0x005088FE` → [EmpCheckErrataList](../49/EmpCheckErrataList_function_0049E550.md) (function, `0x0049E550`)
- `0x00508912` → [EmpCheckErrataList](../49/EmpCheckErrataList_function_0049E550.md) (function, `0x0049E550`)

### Direct callers
- [sinput_s](sinput_s_function_00508938.md) at `0x00508987`

### Static image references
- `0x00508101` → RVA `0x00E00000` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00508090  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00508095  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0050809A  55                              push rbp
0050809B  53                              push rbx
0050809C  56                              push rsi
0050809D  57                              push rdi
0050809E  41 54                           push r12
005080A0  41 55                           push r13
005080A2  41 56                           push r14
005080A4  41 57                           push r15
005080A6  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
005080AB  48 81 EC B8 00 00 00            sub rsp, 0xb8
005080B2  45 33 C9                        xor r9d, r9d
005080B5  4C 8B F2                        mov r14, rdx
005080B8  4C 89 4D DF                     mov qword ptr [rbp - 0x21], r9
005080BC  41 8B D9                        mov ebx, r9d
005080BF  89 5D C3                        mov dword ptr [rbp - 0x3d], ebx
005080C2  41 8B D1                        mov edx, r9d
005080C5  89 55 D3                        mov dword ptr [rbp - 0x2d], edx
005080C8  4C 8B D9                        mov r11, rcx
005080CB  4C 89 4D EF                     mov qword ptr [rbp - 0x11], r9
005080CF  4D 85 F6                        test r14, r14
005080D2  0F 84 30 08 00 00               je 0x140508908
005080D8  48 85 C9                        test rcx, rcx
005080DB  0F 84 27 08 00 00               je 0x140508908
005080E1  41 8A 0E                        mov cl, byte ptr [r14]
005080E4  41 83 CD FF                     or r13d, 0xffffffff
005080E8  44 88 4D B8                     mov byte ptr [rbp - 0x48], r9b
005080EC  41 8B C1                        mov eax, r9d
005080EF  44 89 4D BF                     mov dword ptr [rbp - 0x41], r9d
005080F3  41 8B F1                        mov esi, r9d
005080F6  89 45 BB                        mov dword ptr [rbp - 0x45], eax
005080F9  84 C9                           test cl, cl
005080FB  0F 84 8A 07 00 00               je 0x14050888b
00508101  4C 8B 05 F8 7E 8F 00            mov r8, qword ptr [rip + 0x8f7ef8]
00508108  0F B6 C1                        movzx eax, cl
0050810B  41 F6 04 40 08                  test byte ptr [r8 + rax*2], 8
00508110  74 50                           je 0x140508162
00508112  FF CE                           dec esi
00508114  FF C6                           inc esi
00508116  49 8B CB                        mov rcx, r11
00508119  89 75 BF                        mov dword ptr [rbp - 0x41], esi
0050811C  E8 3F FF FF FF                  call 0x140508060
00508121  44 8B C0                        mov r8d, eax
00508124  41 3B C5                        cmp eax, r13d
00508127  74 20                           je 0x140508149
00508129  48 8B 05 D0 7E 8F 00            mov rax, qword ptr [rip + 0x8f7ed0]
00508130  4C 8B 5D 67                     mov r11, qword ptr [rbp + 0x67]
00508134  41 0F B6 C8                     movzx ecx, r8b
00508138  F6 04 48 08                     test byte ptr [rax + rcx*2], 8
0050813C  75 D6                           jne 0x140508114
0050813E  49 8B D3                        mov rdx, r11
00508141  41 8B C8                        mov ecx, r8d
00508144  E8 DB 16 00 00                  call 0x140509824
00508149  48 8B 05 B0 7E 8F 00            mov rax, qword ptr [rip + 0x8f7eb0]
00508150  49 FF C6                        inc r14
00508153  41 0F B6 0E                     movzx ecx, byte ptr [r14]
00508157  F6 04 48 08                     test byte ptr [rax + rcx*2], 8
0050815B  75 EC                           jne 0x140508149
0050815D  E9 FE 06 00 00                  jmp 0x140508860
00508162  80 F9 25                        cmp cl, 0x25
00508165  0F 85 C0 06 00 00               jne 0x14050882b
0050816B  41 38 4E 01                     cmp byte ptr [r14 + 1], cl
0050816F  0F 84 B3 06 00 00               je 0x140508828
00508175  33 C0                           xor eax, eax
00508177  44 89 4D CB                     mov dword ptr [rbp - 0x35], r9d
0050817B  44 89 4D E7                     mov dword ptr [rbp - 0x19], r9d
0050817F  41 8B F9                        mov edi, r9d
00508182  45 8B D1                        mov r10d, r9d
00508185  4C 89 4D 07                     mov qword ptr [rbp + 7], r9
00508189  88 45 B9                        mov byte ptr [rbp - 0x47], al
0050818C  44 8A C8                        mov r9b, al
0050818F  8A D0                           mov dl, al
00508191  44 8A F8                        mov r15b, al
00508194  44 8B E0                        mov r12d, eax
00508197  41 B3 01                        mov r11b, 1
0050819A  49 FF C6                        inc r14
0050819D  4C 89 75 6F                     mov qword ptr [rbp + 0x6f], r14
005081A1  41 0F B6 0E                     movzx ecx, byte ptr [r14]
005081A5  41 F6 04 48 04                  test byte ptr [r8 + rcx*2], 4
005081AA  74 10                           je 0x1405081bc
005081AC  47 8D 14 92                     lea r10d, [r10 + r10*4]
005081B0  FF C7                           inc edi
005081B2  45 8D 52 E8                     lea r10d, [r10 - 0x18]
005081B6  46 8D 14 51                     lea r10d, [rcx + r10*2]
005081BA  EB 5A                           jmp 0x140508216
005081BC  83 F9 68                        cmp ecx, 0x68
005081BF  0F 87 BA 00 00 00               ja 0x14050827f
005081C5  0F 84 AC 00 00 00               je 0x140508277
005081CB  83 F9 2A                        cmp ecx, 0x2a
005081CE  0F 84 9E 00 00 00               je 0x140508272
005081D4  83 F9 46                        cmp ecx, 0x46
005081D7  74 3D                           je 0x140508216
005081D9  83 F9 49                        cmp ecx, 0x49
005081DC  74 14                           je 0x1405081f2
005081DE  83 F9 4C                        cmp ecx, 0x4c
005081E1  74 0A                           je 0x1405081ed
005081E3  83 F9 4E                        cmp ecx, 0x4e
005081E6  74 2E                           je 0x140508216
005081E8  E9 D1 00 00 00                  jmp 0x1405082be
005081ED  41 FE C3                        inc r11b
005081F0  EB 24                           jmp 0x140508216
005081F2  41 8A 46 01                     mov al, byte ptr [r14 + 1]
005081F6  3C 36                           cmp al, 0x36
005081F8  75 62                           jne 0x14050825c
005081FA  49 8D 46 02                     lea rax, [r14 + 2]
005081FE  80 38 34                        cmp byte ptr [rax], 0x34
00508201  0F 85 91 00 00 00               jne 0x140508298
00508207  4C 8B F0                        mov r14, rax
0050820A  48 89 45 6F                     mov qword ptr [rbp + 0x6f], rax
0050820E  41 FF C4                        inc r12d
00508211  48 83 65 DF 00                  and qword ptr [rbp - 0x21], 0
00508216  84 D2                           test dl, dl
00508218  74 80                           je 0x14050819a
0050821A  44 88 4D 7F                     mov byte ptr [rbp + 0x7f], r9b
0050821E  45 33 C0                        xor r8d, r8d
00508221  8A 4D 7F                        mov cl, byte ptr [rbp + 0x7f]
00508224  4C 8B 4D 07                     mov r9, qword ptr [rbp + 7]
00508228  44 88 5D B7                     mov byte ptr [rbp - 0x49], r11b
0050822C  4C 8B 5D 67                     mov r11, qword ptr [rbp + 0x67]
00508230  44 89 65 D7                     mov dword ptr [rbp - 0x29], r12d
00508234  89 7D CF                        mov dword ptr [rbp - 0x31], edi
00508237  44 89 55 C7                     mov dword ptr [rbp - 0x39], r10d
0050823B  84 C9                           test cl, cl
0050823D  0F 85 9A 00 00 00               jne 0x1405082dd
00508243  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
00508247  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
0050824B  48 83 C0 08                     add rax, 8
0050824F  48 89 45 77                     mov qword ptr [rbp + 0x77], rax
00508253  48 8B 50 F8                     mov rdx, qword ptr [rax - 8]
00508257  E9 84 00 00 00                  jmp 0x1405082e0
0050825C  3C 33                           cmp al, 0x33
0050825E  75 38                           jne 0x140508298
00508260  49 8D 46 02                     lea rax, [r14 + 2]
00508264  80 38 32                        cmp byte ptr [rax], 0x32
00508267  75 2F                           jne 0x140508298
00508269  4C 8B F0                        mov r14, rax
0050826C  48 89 45 6F                     mov qword ptr [rbp + 0x6f], rax
00508270  EB A4                           jmp 0x140508216
00508272  41 FE C1                        inc r9b
00508275  EB 9F                           jmp 0x140508216
00508277  45 02 DD                        add r11b, r13b
0050827A  45 02 FD                        add r15b, r13b
0050827D  EB 97                           jmp 0x140508216
0050827F  83 F9 6A                        cmp ecx, 0x6a
00508282  74 8A                           je 0x14050820e
00508284  83 F9 6C                        cmp ecx, 0x6c
00508287  74 3C                           je 0x1405082c5
00508289  83 F9 74                        cmp ecx, 0x74
0050828C  74 0A                           je 0x140508298
0050828E  83 F9 77                        cmp ecx, 0x77
00508291  74 42                           je 0x1405082d5
00508293  83 F9 7A                        cmp ecx, 0x7a
00508296  75 26                           jne 0x1405082be
00508298  41 8A 46 01                     mov al, byte ptr [r14 + 1]
0050829C  2C 58                           sub al, 0x58
0050829E  3C 20                           cmp al, 0x20
005082A0  77 14                           ja 0x1405082b6
005082A2  48 B9 01 10 82 20 01 00 00 00   movabs rcx, 0x120821001
005082AC  48 0F A3 C1                     bt rcx, rax
005082B0  0F 82 58 FF FF FF               jb 0x14050820e
005082B6  41 FF C4                        inc r12d
005082B9  48 83 65 DF 00                  and qword ptr [rbp - 0x21], 0
005082BE  FE C2                           inc dl
005082C0  E9 51 FF FF FF                  jmp 0x140508216
005082C5  49 8D 46 01                     lea rax, [r14 + 1]
005082C9  80 38 6C                        cmp byte ptr [rax], 0x6c
005082CC  0F 84 35 FF FF FF               je 0x140508207
005082D2  41 FE C3                        inc r11b
005082D5  41 FE C7                        inc r15b
005082D8  E9 39 FF FF FF                  jmp 0x140508216
005082DD  49 8B D0                        mov rdx, r8
005082E0  48 89 55 F7                     mov qword ptr [rbp - 9], rdx
005082E4  45 8A E0                        mov r12b, r8b
005082E7  48 89 55 FF                     mov qword ptr [rbp - 1], rdx
005082EB  45 84 FF                        test r15b, r15b
005082EE  75 13                           jne 0x140508303
005082F0  41 8A 06                        mov al, byte ptr [r14]
005082F3  2C 43                           sub al, 0x43
005082F5  24 EF                           and al, 0xef
005082F7  F6 D8                           neg al
005082F9  45 1A FF                        sbb r15b, r15b
005082FC  41 80 E7 FE                     and r15b, 0xfe
00508300  41 FE C7                        inc r15b
00508303  41 0F B6 3E                     movzx edi, byte ptr [r14]
00508307  83 CF 20                        or edi, 0x20
0050830A  83 FF 6E                        cmp edi, 0x6e
0050830D  74 65                           je 0x140508374
0050830F  83 FF 63                        cmp edi, 0x63
00508312  74 32                           je 0x140508346
00508314  83 FF 7B                        cmp edi, 0x7b
00508317  74 2D                           je 0x140508346
00508319  49 8B CB                        mov rcx, r11
0050831C  FF C6                           inc esi
0050831E  E8 3D FD FF FF                  call 0x140508060
00508323  8B D8                           mov ebx, eax
00508325  41 3B C5                        cmp eax, r13d
00508328  74 14                           je 0x14050833e
0050832A  48 8B 05 CF 7C 8F 00            mov rax, qword ptr [rip + 0x8f7ccf]
00508331  4C 8B 5D 67                     mov r11, qword ptr [rbp + 0x67]
00508335  0F B6 CB                        movzx ecx, bl
00508338  F6 04 48 08                     test byte ptr [rax + rcx*2], 8
0050833C  75 DB                           jne 0x140508319
0050833E  89 75 BF                        mov dword ptr [rbp - 0x41], esi
00508341  89 5D C3                        mov dword ptr [rbp - 0x3d], ebx
00508344  EB 12                           jmp 0x140508358
00508346  FF C6                           inc esi
00508348  49 8B CB                        mov rcx, r11
0050834B  89 75 BF                        mov dword ptr [rbp - 0x41], esi
0050834E  E8 0D FD FF FF                  call 0x140508060
00508353  8B D8                           mov ebx, eax
00508355  89 45 C3                        mov dword ptr [rbp - 0x3d], eax
00508358  41 3B DD                        cmp ebx, r13d
0050835B  0F 84 2F 05 00 00               je 0x140508890
00508361  48 8B 55 F7                     mov rdx, qword ptr [rbp - 9]
00508365  4C 8B 4D 07                     mov r9, qword ptr [rbp + 7]
00508369  44 8B 55 C7                     mov r10d, dword ptr [rbp - 0x39]
0050836D  4C 8B 5D 67                     mov r11, qword ptr [rbp + 0x67]
00508371  8A 4D 7F                        mov cl, byte ptr [rbp + 0x7f]
00508374  44 8B 45 CF                     mov r8d, dword ptr [rbp - 0x31]
00508378  33 C0                           xor eax, eax
0050837A  45 85 C0                        test r8d, r8d
0050837D  74 09                           je 0x140508388
0050837F  45 85 D2                        test r10d, r10d
00508382  0F 84 EB 04 00 00               je 0x140508873
00508388  84 C9                           test cl, cl
0050838A  75 3E                           jne 0x1405083ca
0050838C  83 FF 63                        cmp edi, 0x63
0050838F  74 0A                           je 0x14050839b
00508391  83 FF 73                        cmp edi, 0x73
00508394  74 05                           je 0x14050839b
00508396  83 FF 7B                        cmp edi, 0x7b
00508399  75 2F                           jne 0x1405083ca
0050839B  48 8B 45 EF                     mov rax, qword ptr [rbp - 0x11]
0050839F  48 8B 10                        mov rdx, qword ptr [rax]
005083A2  4C 8D 48 08                     lea r9, [rax + 8]
005083A6  4C 89 4D EF                     mov qword ptr [rbp - 0x11], r9
005083AA  49 83 C1 08                     add r9, 8
005083AE  4C 89 4D 77                     mov qword ptr [rbp + 0x77], r9
005083B2  44 8B 48 08                     mov r9d, dword ptr [rax + 8]
005083B6  48 89 55 F7                     mov qword ptr [rbp - 9], rdx
005083BA  48 89 55 FF                     mov qword ptr [rbp - 1], rdx
005083BE  49 83 F9 01                     cmp r9, 1
005083C2  0F 82 DE 04 00 00               jb 0x1405088a6
005083C8  33 C0                           xor eax, eax
005083CA  83 FF 70                        cmp edi, 0x70
005083CD  0F 87 84 00 00 00               ja 0x140508457
005083D3  74 65                           je 0x14050843a
005083D5  8B CF                           mov ecx, edi
005083D7  83 E9 63                        sub ecx, 0x63
005083DA  74 44                           je 0x140508420
005083DC  83 E9 01                        sub ecx, 1
005083DF  74 64                           je 0x140508445
005083E1  83 E9 05                        sub ecx, 5
005083E4  74 23                           je 0x140508409
005083E6  83 E9 05                        sub ecx, 5
005083E9  74 0A                           je 0x1405083f5
005083EB  83 F9 01                        cmp ecx, 1
005083EE  74 55                           je 0x140508445
005083F0  8A 4D 7F                        mov cl, byte ptr [rbp + 0x7f]
005083F3  EB 7A                           jmp 0x14050846f
005083F5  45 33 C9                        xor r9d, r9d
005083F8  8B C6                           mov eax, esi
005083FA  44 38 4D 7F                     cmp byte ptr [rbp + 0x7f], r9b
005083FE  0F 84 77 03 00 00               je 0x14050877b
00508404  E9 14 04 00 00                  jmp 0x14050881d
00508409  BF 64 00 00 00                  mov edi, 0x64
0050840E  83 FB 2D                        cmp ebx, 0x2d
00508411  0F 85 87 00 00 00               jne 0x14050849e
00508417  C6 45 B9 01                     mov byte ptr [rbp - 0x47], 1
0050841B  E9 83 00 00 00                  jmp 0x1405084a3
00508420  B9 10 00 00 00                  mov ecx, 0x10
00508425  45 85 C0                        test r8d, r8d
00508428  0F 85 76 03 00 00               jne 0x1405087a4
0050842E  44 8D 41 F1                     lea r8d, [rcx - 0xf]
00508432  41 FF C2                        inc r10d
00508435  E9 6A 03 00 00                  jmp 0x1405087a4
0050843A  FF 45 D7                        inc dword ptr [rbp - 0x29]
0050843D  C6 45 B7 01                     mov byte ptr [rbp - 0x49], 1
00508441  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
00508445  83 FB 2D                        cmp ebx, 0x2d
00508448  0F 85 24 01 00 00               jne 0x140508572
0050844E  C6 45 B9 01                     mov byte ptr [rbp - 0x47], 1
00508452  E9 20 01 00 00                  jmp 0x140508577
00508457  83 FF 73                        cmp edi, 0x73
0050845A  0F 84 3F 03 00 00               je 0x14050879f
00508460  83 FF 75                        cmp edi, 0x75
00508463  74 E0                           je 0x140508445
00508465  83 FF 78                        cmp edi, 0x78
00508468  74 A4                           je 0x14050840e
0050846A  83 FF 7B                        cmp edi, 0x7b
0050846D  74 25                           je 0x140508494
0050846F  41 0F B6 06                     movzx eax, byte ptr [r14]
00508473  3B C3                           cmp eax, ebx
00508475  0F 85 44 04 00 00               jne 0x1405088bf
0050847B  44 00 6D B8                     add byte ptr [rbp - 0x48], r13b
0050847F  84 C9                           test cl, cl
00508481  0F 85 96 03 00 00               jne 0x14050881d
00508487  4C 8B 45 EF                     mov r8, qword ptr [rbp - 0x11]
0050848B  4C 89 45 77                     mov qword ptr [rbp + 0x77], r8
0050848F  E9 89 03 00 00                  jmp 0x14050881d
00508494  B9 40 00 00 00                  mov ecx, 0x40
00508499  E9 06 03 00 00                  jmp 0x1405087a4
0050849E  83 FB 2B                        cmp ebx, 0x2b
005084A1  75 26                           jne 0x1405084c9
005084A3  41 83 EA 01                     sub r10d, 1
005084A7  44 89 55 C7                     mov dword ptr [rbp - 0x39], r10d
005084AB  75 0A                           jne 0x1405084b7
005084AD  45 85 C0                        test r8d, r8d
005084B0  74 05                           je 0x1405084b7
005084B2  41 B4 01                        mov r12b, 1
005084B5  EB 12                           jmp 0x1405084c9
005084B7  FF C6                           inc esi
005084B9  49 8B CB                        mov rcx, r11
005084BC  89 75 BF                        mov dword ptr [rbp - 0x41], esi
005084BF  E8 9C FB FF FF                  call 0x140508060
005084C4  8B D8                           mov ebx, eax
005084C6  89 45 C3                        mov dword ptr [rbp - 0x3d], eax
005084C9  83 FB 30                        cmp ebx, 0x30
005084CC  75 68                           jne 0x140508536
005084CE  4C 8B 7D 67                     mov r15, qword ptr [rbp + 0x67]
005084D2  FF C6                           inc esi
005084D4  49 8B CF                        mov rcx, r15
005084D7  89 75 BF                        mov dword ptr [rbp - 0x41], esi
005084DA  E8 81 FB FF FF                  call 0x140508060
005084DF  8B D8                           mov ebx, eax
005084E1  89 45 C3                        mov dword ptr [rbp - 0x3d], eax
005084E4  83 C0 A8                        add eax, -0x58
005084E7  A8 DF                           test al, 0xdf
005084E9  74 51                           je 0x14050853c
005084EB  C7 45 E7 01 00 00 00            mov dword ptr [rbp - 0x19], 1
005084F2  83 FF 78                        cmp edi, 0x78
005084F5  74 23                           je 0x14050851a
005084F7  44 8B 45 CF                     mov r8d, dword ptr [rbp - 0x31]
005084FB  45 33 C9                        xor r9d, r9d
005084FE  44 8B 7D C7                     mov r15d, dword ptr [rbp - 0x39]
00508502  45 85 C0                        test r8d, r8d
00508505  74 09                           je 0x140508510
00508507  41 83 EF 01                     sub r15d, 1
0050850B  75 03                           jne 0x140508510
0050850D  41 FE C4                        inc r12b
00508510  BF 6F 00 00 00                  mov edi, 0x6f
00508515  E9 8F 00 00 00                  jmp 0x1405085a9
0050851A  FF CE                           dec esi
0050851C  89 75 BF                        mov dword ptr [rbp - 0x41], esi
0050851F  41 3B DD                        cmp ebx, r13d
00508522  74 0A                           je 0x14050852e
00508524  49 8B D7                        mov rdx, r15
00508527  8B CB                           mov ecx, ebx
00508529  E8 F6 12 00 00                  call 0x140509824
0050852E  BB 30 00 00 00                  mov ebx, 0x30
00508533  89 5D C3                        mov dword ptr [rbp - 0x3d], ebx
00508536  44 8B 45 CF                     mov r8d, dword ptr [rbp - 0x31]
0050853A  EB 66                           jmp 0x1405085a2
0050853C  FF C6                           inc esi
0050853E  49 8B CF                        mov rcx, r15
00508541  89 75 BF                        mov dword ptr [rbp - 0x41], esi
00508544  E8 17 FB FF FF                  call 0x140508060
00508549  44 8B 45 CF                     mov r8d, dword ptr [rbp - 0x31]
0050854D  45 33 C9                        xor r9d, r9d
00508550  44 8B 7D C7                     mov r15d, dword ptr [rbp - 0x39]
00508554  8B D8                           mov ebx, eax
00508556  89 45 C3                        mov dword ptr [rbp - 0x3d], eax
00508559  45 85 C0                        test r8d, r8d
0050855C  74 0D                           je 0x14050856b
0050855E  41 83 EF 02                     sub r15d, 2
00508562  41 83 FF 01                     cmp r15d, 1
00508566  7D 03                           jge 0x14050856b
00508568  41 FE C4                        inc r12b
0050856B  BF 78 00 00 00                  mov edi, 0x78
00508570  EB 37                           jmp 0x1405085a9
00508572  83 FB 2B                        cmp ebx, 0x2b
00508575  75 2B                           jne 0x1405085a2
00508577  41 83 EA 01                     sub r10d, 1
0050857B  44 89 55 C7                     mov dword ptr [rbp - 0x39], r10d
0050857F  75 0D                           jne 0x14050858e
00508581  45 85 C0                        test r8d, r8d
00508584  74 08                           je 0x14050858e
00508586  41 B4 01                        mov r12b, 1
00508589  45 8B FA                        mov r15d, r10d
0050858C  EB 18                           jmp 0x1405085a6
0050858E  FF C6                           inc esi
00508590  49 8B CB                        mov rcx, r11
00508593  89 75 BF                        mov dword ptr [rbp - 0x41], esi
00508596  E8 C5 FA FF FF                  call 0x140508060
0050859B  8B D8                           mov ebx, eax
0050859D  89 45 C3                        mov dword ptr [rbp - 0x3d], eax
005085A0  EB 94                           jmp 0x140508536
005085A2  44 8B 7D C7                     mov r15d, dword ptr [rbp - 0x39]
005085A6  45 33 C9                        xor r9d, r9d
005085A9  44 39 4D D7                     cmp dword ptr [rbp - 0x29], r9d
005085AD  0F 84 E3 00 00 00               je 0x140508696
005085B3  45 84 E4                        test r12b, r12b
005085B6  0F 85 BF 00 00 00               jne 0x14050867b
005085BC  48 8B 0D 3D 7A 8F 00            mov rcx, qword ptr [rip + 0x8f7a3d]
005085C3  8D 47 90                        lea eax, [rdi - 0x70]
005085C6  A9 F7 FF FF FF                  test eax, 0xfffffff7
005085CB  0F B6 C3                        movzx eax, bl
005085CE  74 2C                           je 0x1405085fc
005085D0  F6 04 41 04                     test byte ptr [rcx + rax*2], 4
005085D4  0F 84 89 00 00 00               je 0x140508663
005085DA  48 8B 55 DF                     mov rdx, qword ptr [rbp - 0x21]
005085DE  83 FF 6F                        cmp edi, 0x6f
005085E1  75 10                           jne 0x1405085f3
005085E3  83 FB 38                        cmp ebx, 0x38
005085E6  7D 06                           jge 0x1405085ee
005085E8  48 C1 E2 03                     shl rdx, 3
005085EC  EB 32                           jmp 0x140508620
005085EE  41 B4 01                        mov r12b, 1
005085F1  EB 31                           jmp 0x140508624
005085F3  48 8D 14 92                     lea rdx, [rdx + rdx*4]
005085F7  48 03 D2                        add rdx, rdx
005085FA  EB 24                           jmp 0x140508620
005085FC  0F B7 0C 41                     movzx ecx, word ptr [rcx + rax*2]
00508600  84 C9                           test cl, cl
00508602  79 5F                           jns 0x140508663
00508604  48 8B 55 DF                     mov rdx, qword ptr [rbp - 0x21]
00508608  0F BE C3                        movsx eax, bl
0050860B  8B D8                           mov ebx, eax
0050860D  48 C1 E2 04                     shl rdx, 4
00508611  83 E3 DF                        and ebx, 0xffffffdf
00508614  83 EB 07                        sub ebx, 7
00508617  F6 C1 04                        test cl, 4
0050861A  0F 45 D8                        cmovne ebx, eax
0050861D  89 5D C3                        mov dword ptr [rbp - 0x3d], ebx
00508620  48 89 55 DF                     mov qword ptr [rbp - 0x21], rdx
00508624  45 84 E4                        test r12b, r12b
00508627  75 3A                           jne 0x140508663
00508629  FF 45 E7                        inc dword ptr [rbp - 0x19]
0050862C  8D 43 D0                        lea eax, [rbx - 0x30]
0050862F  48 63 C8                        movsxd rcx, eax
00508632  48 03 D1                        add rdx, rcx
00508635  48 89 55 DF                     mov qword ptr [rbp - 0x21], rdx
00508639  45 85 C0                        test r8d, r8d
0050863C  74 06                           je 0x140508644
0050863E  41 83 EF 01                     sub r15d, 1
00508642  74 3B                           je 0x14050867f
00508644  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
00508648  FF C6                           inc esi
0050864A  89 75 BF                        mov dword ptr [rbp - 0x41], esi
0050864D  E8 0E FA FF FF                  call 0x140508060
00508652  44 8B 45 CF                     mov r8d, dword ptr [rbp - 0x31]
00508656  8B D8                           mov ebx, eax
00508658  89 45 C3                        mov dword ptr [rbp - 0x3d], eax
0050865B  45 33 C9                        xor r9d, r9d
0050865E  E9 59 FF FF FF                  jmp 0x1405085bc
00508663  FF CE                           dec esi
00508665  89 75 BF                        mov dword ptr [rbp - 0x41], esi
00508668  41 3B DD                        cmp ebx, r13d
0050866B  74 0E                           je 0x14050867b
0050866D  48 8B 55 67                     mov rdx, qword ptr [rbp + 0x67]
00508671  8B CB                           mov ecx, ebx
00508673  E8 AC 11 00 00                  call 0x140509824
00508678  45 33 C9                        xor r9d, r9d
0050867B  48 8B 55 DF                     mov rdx, qword ptr [rbp - 0x21]
0050867F  48 8B C2                        mov rax, rdx
00508682  48 F7 D8                        neg rax
00508685  44 38 4D B9                     cmp byte ptr [rbp - 0x47], r9b
00508689  48 0F 44 C2                     cmove rax, rdx
0050868D  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
00508691  E9 C7 00 00 00                  jmp 0x14050875d
00508696  45 84 E4                        test r12b, r12b
00508699  0F 85 B0 00 00 00               jne 0x14050874f
0050869F  48 8B 0D 5A 79 8F 00            mov rcx, qword ptr [rip + 0x8f795a]
005086A6  8D 47 90                        lea eax, [rdi - 0x70]
005086A9  A9 F7 FF FF FF                  test eax, 0xfffffff7
005086AE  0F B6 C3                        movzx eax, bl
005086B1  74 25                           je 0x1405086d8
005086B3  F6 04 41 04                     test byte ptr [rcx + rax*2], 4
005086B7  74 7E                           je 0x140508737
005086B9  8B 55 CB                        mov edx, dword ptr [rbp - 0x35]
005086BC  83 FF 6F                        cmp edi, 0x6f
005086BF  75 0F                           jne 0x1405086d0
005086C1  83 FB 38                        cmp ebx, 0x38
005086C4  7D 05                           jge 0x1405086cb
005086C6  C1 E2 03                        shl edx, 3
005086C9  EB 2F                           jmp 0x1405086fa
005086CB  41 B4 01                        mov r12b, 1
005086CE  EB 2D                           jmp 0x1405086fd
005086D0  8D 04 92                        lea eax, [rdx + rdx*4]
005086D3  8D 14 00                        lea edx, [rax + rax]
005086D6  EB 22                           jmp 0x1405086fa
005086D8  0F B7 0C 41                     movzx ecx, word ptr [rcx + rax*2]
005086DC  84 C9                           test cl, cl
005086DE  79 57                           jns 0x140508737
005086E0  8B 55 CB                        mov edx, dword ptr [rbp - 0x35]
005086E3  0F BE C3                        movsx eax, bl
005086E6  8B D8                           mov ebx, eax
005086E8  C1 E2 04                        shl edx, 4
005086EB  83 E3 DF                        and ebx, 0xffffffdf
005086EE  83 EB 07                        sub ebx, 7
005086F1  F6 C1 04                        test cl, 4
005086F4  0F 45 D8                        cmovne ebx, eax
005086F7  89 5D C3                        mov dword ptr [rbp - 0x3d], ebx
005086FA  89 55 CB                        mov dword ptr [rbp - 0x35], edx
005086FD  45 84 E4                        test r12b, r12b
00508700  75 35                           jne 0x140508737
00508702  FF 45 E7                        inc dword ptr [rbp - 0x19]
00508705  83 C2 D0                        add edx, -0x30
00508708  03 D3                           add edx, ebx
0050870A  89 55 CB                        mov dword ptr [rbp - 0x35], edx
0050870D  45 85 C0                        test r8d, r8d
00508710  74 06                           je 0x140508718
00508712  41 83 EF 01                     sub r15d, 1
00508716  74 3A                           je 0x140508752
00508718  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
0050871C  FF C6                           inc esi
0050871E  89 75 BF                        mov dword ptr [rbp - 0x41], esi
00508721  E8 3A F9 FF FF                  call 0x140508060
00508726  44 8B 45 CF                     mov r8d, dword ptr [rbp - 0x31]
0050872A  8B D8                           mov ebx, eax
0050872C  89 45 C3                        mov dword ptr [rbp - 0x3d], eax
0050872F  45 33 C9                        xor r9d, r9d
00508732  E9 68 FF FF FF                  jmp 0x14050869f
00508737  FF CE                           dec esi
00508739  89 75 BF                        mov dword ptr [rbp - 0x41], esi
0050873C  41 3B DD                        cmp ebx, r13d
0050873F  74 0E                           je 0x14050874f
00508741  48 8B 55 67                     mov rdx, qword ptr [rbp + 0x67]
00508745  8B CB                           mov ecx, ebx
00508747  E8 D8 10 00 00                  call 0x140509824
0050874C  45 33 C9                        xor r9d, r9d
0050874F  8B 55 CB                        mov edx, dword ptr [rbp - 0x35]
00508752  44 38 4D B9                     cmp byte ptr [rbp - 0x47], r9b
00508756  74 05                           je 0x14050875d
00508758  F7 DA                           neg edx
0050875A  89 55 CB                        mov dword ptr [rbp - 0x35], edx
0050875D  44 39 4D E7                     cmp dword ptr [rbp - 0x19], r9d
00508761  0F 84 7E 01 00 00               je 0x1405088e5
00508767  44 38 4D 7F                     cmp byte ptr [rbp + 0x7f], r9b
0050876B  0F 85 AC 00 00 00               jne 0x14050881d
00508771  FF 45 BB                        inc dword ptr [rbp - 0x45]
00508774  48 8B 55 F7                     mov rdx, qword ptr [rbp - 9]
00508778  8B 45 CB                        mov eax, dword ptr [rbp - 0x35]
0050877B  44 39 4D D7                     cmp dword ptr [rbp - 0x29], r9d
0050877F  74 0C                           je 0x14050878d
00508781  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
00508785  48 89 02                        mov qword ptr [rdx], rax
00508788  E9 90 00 00 00                  jmp 0x14050881d
0050878D  44 38 4D B7                     cmp byte ptr [rbp - 0x49], r9b
00508791  74 07                           je 0x14050879a
00508793  89 02                           mov dword ptr [rdx], eax
00508795  E9 83 00 00 00                  jmp 0x14050881d
0050879A  66 89 02                        mov word ptr [rdx], ax
0050879D  EB 7E                           jmp 0x14050881d
0050879F  B9 20 00 00 00                  mov ecx, 0x20
005087A4  8B C1                           mov eax, ecx
005087A6  83 C8 01                        or eax, 1
005087A9  45 85 C0                        test r8d, r8d
005087AC  4C 8D 45 C3                     lea r8, [rbp - 0x3d]
005087B0  0F 44 C1                        cmove eax, ecx
005087B3  8B C8                           mov ecx, eax
005087B5  83 C9 02                        or ecx, 2
005087B8  45 84 FF                        test r15b, r15b
005087BB  0F 4E C8                        cmovle ecx, eax
005087BE  8B C1                           mov eax, ecx
005087C0  83 C8 04                        or eax, 4
005087C3  44 38 65 7F                     cmp byte ptr [rbp + 0x7f], r12b
005087C7  0F 44 C1                        cmove eax, ecx
005087CA  48 8D 4D BB                     lea rcx, [rbp - 0x45]
005087CE  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
005087D3  48 8D 4D FF                     lea rcx, [rbp - 1]
005087D7  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
005087DC  4C 8D 4D BF                     lea r9, [rbp - 0x41]
005087E0  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
005087E5  44 89 54 24 28                  mov dword ptr [rsp + 0x28], r10d
005087EA  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
005087EF  8B C8                           mov ecx, eax
005087F1  83 FF 7B                        cmp edi, 0x7b
005087F4  75 0F                           jne 0x140508805
005087F6  48 8D 55 6F                     lea rdx, [rbp + 0x6f]
005087FA  E8 01 F7 FF FF                  call 0x140507f00
005087FF  4C 8B 75 6F                     mov r14, qword ptr [rbp + 0x6f]
00508803  EB 07                           jmp 0x14050880c
00508805  33 D2                           xor edx, edx
00508807  E8 34 F5 FF FF                  call 0x140507d40
0050880C  8B 5D C3                        mov ebx, dword ptr [rbp - 0x3d]
0050880F  45 33 C9                        xor r9d, r9d
00508812  85 C0                           test eax, eax
00508814  0F 85 BB 00 00 00               jne 0x1405088d5
0050881A  8B 75 BF                        mov esi, dword ptr [rbp - 0x41]
0050881D  FE 45 B8                        inc byte ptr [rbp - 0x48]
00508820  49 FF C6                        inc r14
00508823  49 8B CE                        mov rcx, r14
00508826  EB 27                           jmp 0x14050884f
00508828  49 FF C6                        inc r14
0050882B  FF C6                           inc esi
0050882D  49 8B CB                        mov rcx, r11
00508830  89 75 BF                        mov dword ptr [rbp - 0x41], esi
00508833  E8 28 F8 FF FF                  call 0x140508060
00508838  8B D8                           mov ebx, eax
0050883A  89 45 C3                        mov dword ptr [rbp - 0x3d], eax
0050883D  41 0F B6 06                     movzx eax, byte ptr [r14]
00508841  49 FF C6                        inc r14
00508844  49 8B CE                        mov rcx, r14
00508847  3B C3                           cmp eax, ebx
00508849  0F 85 8B 00 00 00               jne 0x1405088da
0050884F  41 3B DD                        cmp ebx, r13d
00508852  75 0C                           jne 0x140508860
00508854  41 80 3E 25                     cmp byte ptr [r14], 0x25
00508858  75 28                           jne 0x140508882
0050885A  80 79 01 6E                     cmp byte ptr [rcx + 1], 0x6e
0050885E  75 22                           jne 0x140508882
00508860  41 8A 0E                        mov cl, byte ptr [r14]
00508863  45 33 C9                        xor r9d, r9d
00508866  84 C9                           test cl, cl
00508868  74 6B                           je 0x1405088d5
0050886A  4C 8B 5D 67                     mov r11, qword ptr [rbp + 0x67]
0050886E  E9 8E F8 FF FF                  jmp 0x140508101
00508873  41 3B DD                        cmp ebx, r13d
00508876  74 0A                           je 0x140508882
00508878  49 8B D3                        mov rdx, r11
0050887B  8B CB                           mov ecx, ebx
0050887D  E8 A2 0F 00 00                  call 0x140509824
00508882  8B 55 D3                        mov edx, dword ptr [rbp - 0x2d]
00508885  45 33 C9                        xor r9d, r9d
00508888  8B 45 BB                        mov eax, dword ptr [rbp - 0x45]
0050888B  41 3B DD                        cmp ebx, r13d
0050888E  75 5A                           jne 0x1405088ea
00508890  8B 45 BB                        mov eax, dword ptr [rbp - 0x45]
00508893  33 C9                           xor ecx, ecx
00508895  85 C0                           test eax, eax
00508897  75 05                           jne 0x14050889e
00508899  38 4D B8                        cmp byte ptr [rbp - 0x48], cl
0050889C  74 03                           je 0x1405088a1
0050889E  44 8B E8                        mov r13d, eax
005088A1  41 8B C5                        mov eax, r13d
005088A4  EB 74                           jmp 0x14050891a
005088A6  8B 45 BB                        mov eax, dword ptr [rbp - 0x45]
005088A9  45 33 C9                        xor r9d, r9d
005088AC  45 84 FF                        test r15b, r15b
005088AF  7E 06                           jle 0x1405088b7
005088B1  66 44 89 0A                     mov word ptr [rdx], r9w
005088B5  EB 03                           jmp 0x1405088ba
005088B7  44 88 0A                        mov byte ptr [rdx], r9b
005088BA  41 8B D1                        mov edx, r9d
005088BD  EB CC                           jmp 0x14050888b
005088BF  41 3B DD                        cmp ebx, r13d
005088C2  74 0A                           je 0x1405088ce
005088C4  49 8B D3                        mov rdx, r11
005088C7  8B CB                           mov ecx, ebx
005088C9  E8 56 0F 00 00                  call 0x140509824
005088CE  BA 01 00 00 00                  mov edx, 1
005088D3  EB B0                           jmp 0x140508885
005088D5  41 8B D1                        mov edx, r9d
005088D8  EB AE                           jmp 0x140508888
005088DA  41 3B DD                        cmp ebx, r13d
005088DD  74 A3                           je 0x140508882
005088DF  48 8B 55 67                     mov rdx, qword ptr [rbp + 0x67]
005088E3  EB 96                           jmp 0x14050887b
005088E5  8B 55 D3                        mov edx, dword ptr [rbp - 0x2d]
005088E8  EB 9E                           jmp 0x140508888
005088EA  83 FA 01                        cmp edx, 1
005088ED  75 2B                           jne 0x14050891a
005088EF  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
005088F4  45 33 C0                        xor r8d, r8d
005088F7  45 33 C9                        xor r9d, r9d
005088FA  33 D2                           xor edx, edx
005088FC  33 C9                           xor ecx, ecx
005088FE  E8 4D 5C F9 FF                  call 0x14049e550
00508903  8B 45 BB                        mov eax, dword ptr [rbp - 0x45]
00508906  EB 12                           jmp 0x14050891a
00508908  45 33 C0                        xor r8d, r8d
0050890B  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00508910  33 C9                           xor ecx, ecx
00508912  E8 39 5C F9 FF                  call 0x14049e550
00508917  83 C8 FF                        or eax, 0xffffffff
0050891A  48 81 C4 B8 00 00 00            add rsp, 0xb8
00508921  41 5F                           pop r15
00508923  41 5E                           pop r14
00508925  41 5D                           pop r13
00508927  41 5C                           pop r12
00508929  5F                              pop rdi
0050892A  5E                              pop rsi
0050892B  5B                              pop rbx
0050892C  5D                              pop rbp
0050892D  C3                              ret
0050892E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall input_s(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned int v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned __int8 v_stack_mA6;
    unsigned __int8 v_stack_mA7;
    unsigned __int8 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (184);
    a4 = 0;
    v_stack_m80 = 0;
    v_stack_m9C = 0;
    v_stack_m8C = 0;
    v_stack_m70 = 0;
    if (a2 == 0) goto loc_00508908;
    if (a1 == 0) goto loc_00508908;
    v_r13 = (unsigned int)((v_r13) | (0xFFFFFFFFULL));
    v_stack_mA7 = 0;
    v_stack_mA0 = 0;
    v_stack_mA4 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(a2)) == 0) goto loc_0050888B;
loc_00508101:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9404152) + (unsigned __int8)(*(unsigned __int8 *)(a2)) * 2)) & (8)) == 0) goto loc_00508162;
    v_rsi = (unsigned int)((0) - 1);
loc_00508114:
    v_rsi = (unsigned int)((v_rsi) + 1);
    v_stack_mA0 = (unsigned int)(v_rsi);
    result = _inc(a1, 0, *(unsigned __int64 *)(v_rip + 9404152), a4);
    if (((unsigned int)(result)) == ((unsigned int)(v_r13))) goto loc_00508149;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9404112) + (unsigned __int8)((unsigned int)((unsigned int)(result))) * 2)) & (8)) != 0) goto loc_00508114;
    result = ungetc_nolock((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_p8, (unsigned int)((unsigned int)(result)), a4);
loc_00508149:
    v_r14 = (a2) + 1;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9404080) + *(unsigned __int8 *)(v_r14) * 2)) & (8)) != 0) goto loc_00508149;
    goto loc_00508860;
loc_00508162:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r14))) != 37) goto loc_0050882B;
    if ((*(unsigned __int8 *)(v_r14 + 1)) == ((unsigned __int8)(*(unsigned __int8 *)(v_r14)))) goto loc_00508828;
    result = 0;
    v_stack_m94 = 0;
    v_stack_m78 = 0;
    v_stack_m58 = 0;
    v_stack_mA6 = 0;
loc_0050819A:
    v_r14 = (v_r14) + 1;
    v_stack_p10 = v_r14;
    if (((*(unsigned __int8 *)((unsigned int)((unsigned int)(result)) + *(unsigned __int8 *)(v_r14) * 2)) & (4)) == 0) goto loc_005081BC;
    v_rdi = (unsigned int)((0) + 1);
    goto loc_00508216;
loc_005081BC:
    if (((unsigned int)(*(unsigned __int8 *)(v_r14))) > 104) goto loc_0050827F;
    if (((unsigned int)(*(unsigned __int8 *)(v_r14))) == 104) goto loc_00508277;
    if (((unsigned int)(*(unsigned __int8 *)(v_r14))) == 42) goto loc_00508272;
    if (((unsigned int)(*(unsigned __int8 *)(v_r14))) == 70) goto loc_00508216;
    if (((unsigned int)(*(unsigned __int8 *)(v_r14))) == 73) goto loc_005081F2;
    if (((unsigned int)(*(unsigned __int8 *)(v_r14))) == 76) goto loc_005081ED;
    if (((unsigned int)(*(unsigned __int8 *)(v_r14))) == 78) goto loc_00508216;
    goto loc_005082BE;
loc_005081ED:
    v_r11 = (unsigned __int8)((1) + 1);
    goto loc_00508216;
loc_005081F2:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r14 + 1))) != 54) goto loc_0050825C;
    if ((*(unsigned __int8 *)(v_r14 + 2)) != 52) goto loc_00508298;
loc_00508207:
    v_stack_p10 = v_r14 + 2;
loc_0050820E:
    v_r12 = (unsigned int)((0) + 1);
loc_00508216:
    if (0 == 0) goto loc_0050819A;
    v_stack_p20 = 0;
    a3 = 0;
    v_stack_mA8 = (unsigned __int8)(v_r11);
    v_stack_m88 = (unsigned int)(v_r12);
    v_stack_m90 = (unsigned int)(v_rdi);
    v_stack_m98 = (unsigned int)(*(unsigned __int8 *)(v_r14) + 0 + 0 * 4 - 24 * 2);
    if ((unsigned __int8)(v_stack_p20) != 0) goto loc_005082DD;
    v_stack_m70 = v_stack_p18;
    result = (v_stack_p18) + (8);
    v_stack_p18 = result;
    goto loc_005082E0;
loc_0050825C:
    if (((unsigned __int8)(result)) != 51) goto loc_00508298;
    if ((*(unsigned __int8 *)(v_r14 + 2 + 2)) != 50) goto loc_00508298;
    v_stack_p10 = v_r14 + 2 + 2;
    goto loc_00508216;
loc_00508272:
    a4 = (unsigned __int8)((v_stack_m58) + 1);
    goto loc_00508216;
loc_00508277:
    v_r11 = (unsigned __int8)((v_stack_p8) + ((unsigned __int8)(v_r13)));
    v_r15 = (unsigned __int8)((0) + ((unsigned __int8)(v_r13)));
    goto loc_00508216;
loc_0050827F:
    if (((unsigned int)(v_stack_p20)) == 106) goto loc_0050820E;
    if (((unsigned int)(v_stack_p20)) == 108) goto loc_005082C5;
    if (((unsigned int)(v_stack_p20)) == 116) goto loc_00508298;
    if (((unsigned int)(v_stack_p20)) == 119) goto loc_005082D5;
    if (((unsigned int)(v_stack_p20)) != 122) goto loc_005082BE;
loc_00508298:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_r14 + 2 + 2 + 1)) - (88));
    if (((unsigned __int8)(result)) > 32) goto loc_005082B6;
    if (((unsigned __int8)(result)) < 32) goto loc_0050820E;
loc_005082B6:
    v_r12 = (unsigned int)((v_r12) + 1);
loc_005082BE:
    a2 = (unsigned __int8)((*(unsigned __int64 *)(result - 8)) + 1);
    goto loc_00508216;
loc_005082C5:
    if ((*(unsigned __int8 *)(v_r14 + 2 + 2 + 1)) == 108) goto loc_00508207;
    v_r11 = (unsigned __int8)((v_r11) + 1);
loc_005082D5:
    v_r15 = (unsigned __int8)((v_r15) + 1);
    goto loc_00508216;
loc_005082DD:
loc_005082E0:
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    result = v_r14 + 2 + 2 + 1;
    if ((unsigned __int8)(v_r15) == 0) {
        result = *(unsigned __int8 *)(v_r14 + 2 + 2);
        result = (unsigned __int8)((result) - (67));
        result = (unsigned __int8)((result) & (239));
        result = (unsigned __int8)(-(result));
        v_r15 = (unsigned __int8)((v_r15) & (254));
        v_r15 = (unsigned __int8)((v_r15) + 1);
    }
    v_rdi = (unsigned int)((*(unsigned __int8 *)(v_r14 + 2 + 2)) | (32));
    if (((unsigned int)(v_rdi)) == 110) goto loc_00508374;
    if (((unsigned int)(v_rdi)) == 99) goto loc_00508346;
    if (((unsigned int)(v_rdi)) == 123) goto loc_00508346;
loc_00508319:
    v_rsi = (unsigned int)((v_rsi) + 1);
    result = _inc(v_r11, 0, a3, a4);
    if (((unsigned int)(result)) == ((unsigned int)(v_r13))) goto loc_0050833E;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9403599) + (unsigned __int8)((unsigned int)((unsigned int)(result))) * 2)) & (8)) != 0) goto loc_00508319;
loc_0050833E:
    v_stack_mA0 = (unsigned int)(v_rsi);
    v_stack_m9C = (unsigned int)((unsigned int)((unsigned int)(result)));
    goto loc_00508358;
loc_00508346:
    v_rsi = (unsigned int)((v_rsi) + 1);
    v_stack_mA0 = (unsigned int)(v_rsi);
    result = _inc(v_stack_p8, 0, a3, a4);
    v_stack_m9C = (unsigned int)(result);
loc_00508358:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)(v_r13))) goto loc_00508890;
loc_00508374:
    result = 0;
    if ((unsigned int)((unsigned int)(v_stack_m90)) == 0) goto loc_00508388;
    if ((unsigned int)((unsigned int)(v_stack_m98)) == 0) goto loc_00508873;
loc_00508388:
    if ((unsigned __int8)(v_stack_p20) != 0) goto loc_005083CA;
    if (((unsigned int)(v_rdi)) == 99) goto loc_0050839B;
    if (((unsigned int)(v_rdi)) == 115) goto loc_0050839B;
    if (((unsigned int)(v_rdi)) != 123) goto loc_005083CA;
loc_0050839B:
    v_stack_m70 = v_stack_m70 + 8;
    a4 = (v_stack_m70 + 8) + (8);
    v_stack_p18 = a4;
    v_stack_m68 = *(unsigned __int64 *)(v_stack_m70);
    v_stack_m60 = *(unsigned __int64 *)(v_stack_m70);
    if (((unsigned int)(*(unsigned int *)(v_stack_m70 + 8))) < 1) goto loc_005088A6;
    result = 0;
loc_005083CA:
    if (((unsigned int)(v_rdi)) > 112) goto loc_00508457;
    if (((unsigned int)(v_rdi)) == 112) goto loc_0050843A;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - (99));
    if (condition_is_equal) goto loc_00508420;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00508445;
    a1 = (unsigned int)((a1) - (5));
    if (condition_is_equal) goto loc_00508409;
    a1 = (unsigned int)((a1) - (5));
    if (condition_is_equal) goto loc_005083F5;
    if (((unsigned int)(a1)) == 1) goto loc_00508445;
    goto loc_0050846F;
loc_005083F5:
    a4 = 0;
    if (v_stack_p20 == 0) goto loc_0050877B;
    goto loc_0050881D;
loc_00508409:
loc_0050840E:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 45) goto loc_0050849E;
    v_stack_mA6 = 1;
    goto loc_005084A3;
loc_00508420:
    if ((unsigned int)((unsigned int)(v_stack_m90)) != 0) goto loc_005087A4;
    v_r10 = (unsigned int)(((unsigned int)(v_stack_m98)) + 1);
    goto loc_005087A4;
loc_0050843A:
    v_stack_mA8 = 1;
    v_stack_m80 = (unsigned int)((unsigned int)(v_rsi));
loc_00508445:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 45) goto loc_00508572;
    v_stack_mA6 = 1;
    goto loc_00508577;
loc_00508457:
    if (100 == 115) goto loc_0050879F;
    if (100 == 117) goto loc_00508445;
    if (100 == 120) goto loc_0050840E;
    if (100 == 123) goto loc_00508494;
loc_0050846F:
    if (((unsigned int)(*(unsigned __int8 *)(v_r14 + 2 + 2))) != ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_005088BF;
    if (16 != 0) goto loc_0050881D;
    v_stack_p18 = v_stack_m70;
    goto loc_0050881D;
loc_00508494:
    goto loc_005087A4;
loc_0050849E:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 43) goto loc_005084C9;
loc_005084A3:
    v_r10 = (unsigned int)((v_r10) - (1));
    v_stack_m98 = (unsigned int)(v_r10);
    if (condition_is_not_equal) goto loc_005084B7;
    if ((unsigned int)(v_stack_m70) == 0) goto loc_005084B7;
    goto loc_005084C9;
loc_005084B7:
    v_rsi = (unsigned int)((v_rsi) + 1);
    v_stack_mA0 = (unsigned int)(v_rsi);
    result = _inc(v_stack_p8, *(unsigned __int64 *)(v_stack_m70), v_stack_m70, a4);
    v_stack_m9C = (unsigned int)(result);
loc_005084C9:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 48) goto loc_00508536;
    v_rsi = (unsigned int)((v_rsi) + 1);
    v_stack_mA0 = (unsigned int)(v_rsi);
    result = _inc(v_stack_p8, *(unsigned __int64 *)(v_stack_m70), v_stack_m70, a4);
    v_stack_m9C = (unsigned int)(result);
    result = (unsigned int)((result) + (-88));
    if ((((unsigned __int8)(result)) & (223)) == 0) goto loc_0050853C;
    v_stack_m78 = 1;
    if (100 == 120) goto loc_0050851A;
    a4 = 0;
    if ((unsigned int)((unsigned int)(v_stack_m90)) == 0) goto loc_00508510;
    v_r15 = (unsigned int)(((unsigned int)(v_stack_m98)) - (1));
    v_r12 = 1;
    if (!(condition_is_not_equal)) {
        v_r12 = (unsigned __int8)((1) + 1);
    }
    goto loc_005085A9;
loc_0050851A:
    v_rsi = (unsigned int)((v_rsi) - 1);
    v_stack_mA0 = (unsigned int)(v_rsi);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)(v_r13))) {
        a2 = v_r15;
        a1 = (unsigned int)((unsigned int)((unsigned int)(result)));
        result = ungetc_nolock(a1, a2, (unsigned int)(v_stack_m90), a4);
    }
    v_stack_m9C = 48;
loc_00508536:
    goto loc_005085A2;
loc_0050853C:
    v_rsi = (unsigned int)((v_rsi) + 1);
    v_stack_mA0 = (unsigned int)(v_rsi);
    result = _inc(v_r15, a2, (unsigned int)(v_stack_m90), a4);
    a4 = 0;
    v_stack_m9C = (unsigned int)(result);
    if ((unsigned int)((unsigned int)(v_stack_m90)) == 0) goto loc_0050856B;
    v_r15 = (unsigned int)(((unsigned int)(v_stack_m98)) - (2));
    if (((unsigned int)(v_r15)) < 1) {
        v_r12 = (unsigned __int8)((v_r12) + 1);
    }
    goto loc_005085A9;
loc_00508572:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 43) goto loc_005085A2;
loc_00508577:
    v_r10 = (unsigned int)((v_r10) - (1));
    v_stack_m98 = (unsigned int)(v_r10);
    if (condition_is_not_equal) goto loc_0050858E;
    if ((unsigned int)((unsigned int)(v_stack_m90)) == 0) goto loc_0050858E;
    goto loc_005085A6;
loc_0050858E:
    v_rsi = (unsigned int)((v_rsi) + 1);
    v_stack_mA0 = (unsigned int)(v_rsi);
    result = _inc(v_stack_p8, a2, (unsigned int)(v_stack_m90), a4);
    v_stack_m9C = (unsigned int)(result);
    goto loc_00508536;
loc_005085A2:
loc_005085A6:
    a4 = 0;
loc_005085A9:
    if (v_stack_m88 == 0) goto loc_00508696;
    if (1 != 0) goto loc_0050867B;
loc_005085BC:
    if ((((unsigned int)(120 - 112)) & (0xFFFFFFF7ULL)) == 0) goto loc_005085FC;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9402941) + (unsigned __int8)((unsigned int)((unsigned int)(result))) * 2)) & (4)) == 0) goto loc_00508663;
    if (120 != 111) goto loc_005085F3;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) >= 56) goto loc_005085EE;
    a2 = (v_stack_m80) << (3);
    goto loc_00508620;
loc_005085EE:
    goto loc_00508624;
loc_005085F3:
    a2 = (a2 + a2 * 4) + (a2 + a2 * 4);
    goto loc_00508620;
loc_005085FC:
    if (!sign_flag) goto loc_00508663;
    a2 = (v_stack_m80) << (4);
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((__int8)((unsigned __int8)((unsigned int)((unsigned int)(result))))))) & (0xFFFFFFDFULL));
    v_rbx = (unsigned int)((v_rbx) - (7));
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 9402941) + (unsigned __int8)((unsigned int)((unsigned int)(result))) * 2))) & (4)) != 0) { v_rbx = (unsigned int)((__int8)((unsigned __int8)((unsigned int)((unsigned int)(result))))); }
    v_stack_m9C = (unsigned int)(v_rbx);
loc_00508620:
    v_stack_m80 = a2;
loc_00508624:
    if (1 != 0) goto loc_00508663;
    a2 = (a2) + ((int)((unsigned int)(v_rbx - 48)));
    v_stack_m80 = a2;
    if ((unsigned int)((unsigned int)(v_stack_m90)) == 0) goto loc_00508644;
    v_r15 = (unsigned int)(((unsigned int)(v_stack_m98)) - (1));
    if (condition_is_equal) goto loc_0050867F;
loc_00508644:
    v_rsi = (unsigned int)((v_rsi) + 1);
    v_stack_mA0 = (unsigned int)(v_rsi);
    result = _inc(v_stack_p8, a2, (unsigned int)(v_stack_m90), a4);
    v_stack_m9C = (unsigned int)(result);
    a4 = 0;
    goto loc_005085BC;
loc_00508663:
    v_rsi = (unsigned int)((v_rsi) - 1);
    v_stack_mA0 = (unsigned int)(v_rsi);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)(v_r13))) {
        a2 = v_stack_p8;
        a1 = (unsigned int)((unsigned int)((unsigned int)(result)));
        result = ungetc_nolock(a1, a2, (unsigned int)(v_stack_m90), a4);
        a4 = 0;
    }
loc_0050867F:
    result = -(v_stack_m80);
    if (v_stack_mA6 == 0) { result = v_stack_m80; }
    v_stack_m80 = result;
    goto loc_0050875D;
loc_00508696:
    if (1 != 0) goto loc_0050874F;
loc_0050869F:
    if ((((unsigned int)(120 - 112)) & (0xFFFFFFF7ULL)) == 0) goto loc_005086D8;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9402714) + (unsigned __int8)((unsigned int)((unsigned int)(result))) * 2)) & (4)) == 0) goto loc_00508737;
    if (120 != 111) goto loc_005086D0;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) >= 56) goto loc_005086CB;
    a2 = (unsigned int)(((unsigned int)(v_stack_m94)) << (3));
    goto loc_005086FA;
loc_005086CB:
    goto loc_005086FD;
loc_005086D0:
    goto loc_005086FA;
loc_005086D8:
    if (!sign_flag) goto loc_00508737;
    a2 = (unsigned int)(((unsigned int)(v_stack_m94)) << (4));
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((__int8)((unsigned __int8)((unsigned int)((unsigned int)(result))))))) & (0xFFFFFFDFULL));
    v_rbx = (unsigned int)((v_rbx) - (7));
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 9402714) + a2 + a2 * 4 * 2))) & (4)) != 0) { v_rbx = (unsigned int)((__int8)((unsigned __int8)((unsigned int)((unsigned int)(result))))); }
    v_stack_m9C = (unsigned int)(v_rbx);
loc_005086FA:
    v_stack_m94 = (unsigned int)(a2);
loc_005086FD:
    if (1 != 0) goto loc_00508737;
    a2 = (unsigned int)((a2) + (-48));
    a2 = (unsigned int)((a2) + ((unsigned int)(v_rbx)));
    v_stack_m94 = (unsigned int)(a2);
    if ((unsigned int)((unsigned int)(v_stack_m90)) == 0) goto loc_00508718;
    v_r15 = (unsigned int)((v_r15) - (1));
    if (condition_is_equal) goto loc_00508752;
loc_00508718:
    v_rsi = (unsigned int)((v_rsi) + 1);
    v_stack_mA0 = (unsigned int)(v_rsi);
    result = _inc(v_stack_p8, a2, (unsigned int)(v_stack_m90), a4);
    v_stack_m9C = (unsigned int)(result);
    a4 = 0;
    goto loc_0050869F;
loc_00508737:
    v_rsi = (unsigned int)((v_rsi) - 1);
    v_stack_mA0 = (unsigned int)(v_rsi);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)(v_r13))) {
        a2 = v_stack_p8;
        a1 = (unsigned int)((unsigned int)((unsigned int)(result)));
        result = ungetc_nolock(a1, a2, (unsigned int)(v_stack_m90), a4);
        a4 = 0;
    }
loc_00508752:
    if (v_stack_mA6 != 0) {
        a2 = (unsigned int)(-((unsigned int)(v_stack_m94)));
        v_stack_m94 = (unsigned int)(a2);
    }
    if (v_stack_m78 == 0) goto loc_005088E5;
    if (v_stack_p20 != 0) goto loc_0050881D;
loc_0050877B:
    if (v_stack_m88 == 0) goto loc_0050878D;
    *(unsigned __int64 *)(v_stack_m68) = v_stack_m80;
    goto loc_0050881D;
loc_0050878D:
    if (v_stack_mA8 == 0) goto loc_0050879A;
    *(unsigned int *)(v_stack_m68) = (unsigned int)(v_stack_m80);
    goto loc_0050881D;
loc_0050879A:
    *(unsigned __int16 *)(v_stack_m68) = (unsigned __int16)(v_stack_m80);
    goto loc_0050881D;
loc_0050879F:
loc_005087A4:
    result = (unsigned int)((32) | (1));
    if ((unsigned int)((unsigned int)(v_stack_m90)) == 0) { result = 32; }
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) | (2));
    if (condition_is_less_or_equal) { a1 = (unsigned int)(result); }
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (4));
    if (v_stack_p20 == 1) { result = (unsigned int)(a1); }
    v_stack_mB8 = v_stack_mA4;
    v_stack_mC0 = 0;
    v_stack_mC8 = v_stack_p8;
    v_stack_mD0 = (unsigned int)(v_r10);
    v_stack_mD8 = v_stack_m60;
    if (120 != 123) goto loc_00508805;
    result = ReadStringDelimited((unsigned int)((unsigned int)(result)), v_stack_p10, v_stack_m9C, v_stack_mA0);
    goto loc_0050880C;
loc_00508805:
    a2 = 0;
    result = ReadString((unsigned int)((unsigned int)(result)), a2, v_stack_m9C, v_stack_mA0);
loc_0050880C:
    a4 = 0;
    if ((unsigned int)(result) != 0) goto loc_005088D5;
loc_0050881D:
    v_r14 = (v_stack_p10) + 1;
    goto loc_0050884F;
loc_00508828:
    v_r14 = (v_r14) + 1;
loc_0050882B:
    v_rsi = (unsigned int)(((unsigned int)(v_stack_mA0)) + 1);
    v_stack_mA0 = (unsigned int)(v_rsi);
    result = _inc(v_stack_p8, a2, v_stack_m9C, a4);
    v_stack_m9C = (unsigned int)(result);
    v_r14 = (v_r14) + 1;
    if (((unsigned int)(*(unsigned __int8 *)(v_r14))) != ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_005088DA;
loc_0050884F:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)(v_r13))) goto loc_00508860;
    if ((*(unsigned __int8 *)(v_r14)) != 37) goto loc_00508882;
    if ((*(unsigned __int8 *)(v_r14 + 1)) != 110) goto loc_00508882;
loc_00508860:
    a4 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_r14)) == 0) goto loc_005088D5;
    goto loc_00508101;
loc_00508873:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)(v_r13))) goto loc_00508882;
loc_0050887B:
    result = ungetc_nolock((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_p8, v_stack_m9C, a4);
loc_00508882:
loc_00508885:
    a4 = 0;
loc_00508888:
loc_0050888B:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)(v_r13))) goto loc_005088EA;
loc_00508890:
    a1 = 0;
    if ((unsigned int)((unsigned int)(v_stack_mA4)) != 0) goto loc_0050889E;
    if (v_stack_mA7 != 0) {
        v_r13 = (unsigned int)((unsigned int)(v_stack_mA4));
    }
    goto loc_0050891A;
loc_005088A6:
    a4 = 0;
    if (condition_is_less_or_equal) goto loc_005088B7;
    *(unsigned __int16 *)((unsigned int)(v_stack_m8C)) = 0;
    goto loc_005088BA;
loc_005088B7:
    *(unsigned __int8 *)((unsigned int)(v_stack_m8C)) = 0;
loc_005088BA:
    goto loc_0050888B;
loc_005088BF:
    result = (unsigned int)(v_stack_mA4);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)(v_r13))) {
        a2 = v_stack_p8;
        a1 = (unsigned int)((unsigned int)((unsigned int)(result)));
        result = ungetc_nolock(a1, a2, v_stack_m9C, a4);
    }
    goto loc_00508885;
loc_005088D5:
    goto loc_00508888;
loc_005088DA:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)(v_r13))) goto loc_00508882;
    goto loc_0050887B;
loc_005088E5:
    goto loc_00508888;
loc_005088EA:
    if (((unsigned int)((unsigned int)(v_stack_m8C))) != 1) goto loc_0050891A;
    v_stack_mD8 = 0;
    a3 = 0;
    a4 = 0;
    a2 = 0;
    a1 = 0;
    result = EmpCheckErrataList(a1, a2, a3, a4);
    goto loc_0050891A;
loc_00508908:
    a3 = 0;
    v_stack_mD8 = 0;
    a1 = 0;
    result = EmpCheckErrataList(a1, a2, a3, a4);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
loc_0050891A:
    v_rsp = (v_rsp) + (184);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t input_s(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint32_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint8_t v_stack_mA6;
    uint8_t v_stack_mA7;
    uint8_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (184);
    Arg4 = 0;
    v_stack_m80 = 0;
    v_stack_m9C = 0;
    v_stack_m8C = 0;
    v_stack_m70 = 0;
    if (Arg2 == 0) goto loc_00508908;
    if (Arg1 == 0) goto loc_00508908;
    local_r13 = (uint32_t)((local_r13) | (0xFFFFFFFFULL));
    v_stack_mA7 = 0;
    v_stack_mA0 = 0;
    v_stack_mA4 = 0;
    if ((uint8_t)(*(uint8_t *)(Arg2)) == 0) goto loc_0050888B;
loc_00508101:
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0x8F7EF8) + (uint8_t)(*(uint8_t *)(Arg2)) * 2)) & (8)) == 0) goto loc_00508162;
    local_rsi = (uint32_t)((0) - 1);
loc_00508114:
    local_rsi = (uint32_t)((local_rsi) + 1);
    v_stack_mA0 = (uint32_t)(local_rsi);
    result = _inc(Arg1, 0, *(uint64_t *)(v_rip + 0x8F7EF8), Arg4);
    if (((uint32_t)(result)) == ((uint32_t)(local_r13))) goto loc_00508149;
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0x8F7ED0) + (uint8_t)((uint32_t)((uint32_t)(result))) * 2)) & (8)) != 0) goto loc_00508114;
    result = ungetc_nolock((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_p8, (uint32_t)((uint32_t)(result)), Arg4);
loc_00508149:
    local_r14 = (Arg2) + 1;
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0x8F7EB0) + *(uint8_t *)(local_r14) * 2)) & (8)) != 0) goto loc_00508149;
    goto loc_00508860;
loc_00508162:
    if (((uint8_t)(*(uint8_t *)(local_r14))) != 37) goto loc_0050882B;
    if ((*(uint8_t *)(local_r14 + 0x1)) == ((uint8_t)(*(uint8_t *)(local_r14)))) goto loc_00508828;
    result = 0;
    v_stack_m94 = 0;
    v_stack_m78 = 0;
    v_stack_m58 = 0;
    v_stack_mA6 = 0;
loc_0050819A:
    local_r14 = (local_r14) + 1;
    v_stack_p10 = local_r14;
    if (((*(uint8_t *)((uint32_t)((uint32_t)(result)) + *(uint8_t *)(local_r14) * 2)) & (4)) == 0) goto loc_005081BC;
    local_rdi = (uint32_t)((0) + 1);
    goto loc_00508216;
loc_005081BC:
    if (((uint32_t)(*(uint8_t *)(local_r14))) > 104) goto loc_0050827F;
    if (((uint32_t)(*(uint8_t *)(local_r14))) == 104) goto loc_00508277;
    if (((uint32_t)(*(uint8_t *)(local_r14))) == 42) goto loc_00508272;
    if (((uint32_t)(*(uint8_t *)(local_r14))) == 70) goto loc_00508216;
    if (((uint32_t)(*(uint8_t *)(local_r14))) == 73) goto loc_005081F2;
    if (((uint32_t)(*(uint8_t *)(local_r14))) == 76) goto loc_005081ED;
    if (((uint32_t)(*(uint8_t *)(local_r14))) == 78) goto loc_00508216;
    goto loc_005082BE;
loc_005081ED:
    local_r11 = (uint8_t)((1) + 1);
    goto loc_00508216;
loc_005081F2:
    if (((uint8_t)(*(uint8_t *)(local_r14 + 0x1))) != 54) goto loc_0050825C;
    if ((*(uint8_t *)(local_r14 + 0x2)) != 52) goto loc_00508298;
loc_00508207:
    v_stack_p10 = local_r14 + 2;
loc_0050820E:
    local_r12 = (uint32_t)((0) + 1);
loc_00508216:
    if (0 == 0) goto loc_0050819A;
    v_stack_p20 = 0;
    Arg3 = 0;
    v_stack_mA8 = (uint8_t)(local_r11);
    v_stack_m88 = (uint32_t)(local_r12);
    v_stack_m90 = (uint32_t)(local_rdi);
    v_stack_m98 = (uint32_t)(*(uint8_t *)(local_r14) + 0 + 0 * 4 - 24 * 2);
    if ((uint8_t)(v_stack_p20) != 0) goto loc_005082DD;
    v_stack_m70 = v_stack_p18;
    result = (v_stack_p18) + (8);
    v_stack_p18 = result;
    goto loc_005082E0;
loc_0050825C:
    if (((uint8_t)(result)) != 51) goto loc_00508298;
    if ((*(uint8_t *)(local_r14 + 0x2 + 0x2)) != 50) goto loc_00508298;
    v_stack_p10 = local_r14 + 2 + 2;
    goto loc_00508216;
loc_00508272:
    Arg4 = (uint8_t)((v_stack_m58) + 1);
    goto loc_00508216;
loc_00508277:
    local_r11 = (uint8_t)((v_stack_p8) + ((uint8_t)(local_r13)));
    local_r15 = (uint8_t)((0) + ((uint8_t)(local_r13)));
    goto loc_00508216;
loc_0050827F:
    if (((uint32_t)(v_stack_p20)) == 106) goto loc_0050820E;
    if (((uint32_t)(v_stack_p20)) == 108) goto loc_005082C5;
    if (((uint32_t)(v_stack_p20)) == 116) goto loc_00508298;
    if (((uint32_t)(v_stack_p20)) == 119) goto loc_005082D5;
    if (((uint32_t)(v_stack_p20)) != 122) goto loc_005082BE;
loc_00508298:
    result = (uint8_t)((*(uint8_t *)(local_r14 + 0x2 + 0x2 + 0x1)) - (88));
    if (((uint8_t)(result)) > 32) goto loc_005082B6;
    if (((uint8_t)(result)) < 32) goto loc_0050820E;
loc_005082B6:
    local_r12 = (uint32_t)((local_r12) + 1);
loc_005082BE:
    Arg2 = (uint8_t)((*(uint64_t *)(result - 0x8)) + 1);
    goto loc_00508216;
loc_005082C5:
    if ((*(uint8_t *)(local_r14 + 0x2 + 0x2 + 0x1)) == 108) goto loc_00508207;
    local_r11 = (uint8_t)((local_r11) + 1);
loc_005082D5:
    local_r15 = (uint8_t)((local_r15) + 1);
    goto loc_00508216;
loc_005082DD:
loc_005082E0:
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    result = local_r14 + 2 + 2 + 1;
    if ((uint8_t)(local_r15) == 0) {
        result = *(uint8_t *)(local_r14 + 0x2 + 0x2);
        result = (uint8_t)((result) - (67));
        result = (uint8_t)((result) & (239));
        result = (uint8_t)(-(result));
        local_r15 = (uint8_t)((local_r15) & (254));
        local_r15 = (uint8_t)((local_r15) + 1);
    }
    local_rdi = (uint32_t)((*(uint8_t *)(local_r14 + 0x2 + 0x2)) | (32));
    if (((uint32_t)(local_rdi)) == 110) goto loc_00508374;
    if (((uint32_t)(local_rdi)) == 99) goto loc_00508346;
    if (((uint32_t)(local_rdi)) == 123) goto loc_00508346;
loc_00508319:
    local_rsi = (uint32_t)((local_rsi) + 1);
    result = _inc(local_r11, 0, Arg3, Arg4);
    if (((uint32_t)(result)) == ((uint32_t)(local_r13))) goto loc_0050833E;
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0x8F7CCF) + (uint8_t)((uint32_t)((uint32_t)(result))) * 2)) & (8)) != 0) goto loc_00508319;
loc_0050833E:
    v_stack_mA0 = (uint32_t)(local_rsi);
    v_stack_m9C = (uint32_t)((uint32_t)((uint32_t)(result)));
    goto loc_00508358;
loc_00508346:
    local_rsi = (uint32_t)((local_rsi) + 1);
    v_stack_mA0 = (uint32_t)(local_rsi);
    result = _inc(v_stack_p8, 0, Arg3, Arg4);
    v_stack_m9C = (uint32_t)(result);
loc_00508358:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)(local_r13))) goto loc_00508890;
loc_00508374:
    result = 0;
    if ((uint32_t)((uint32_t)(v_stack_m90)) == 0) goto loc_00508388;
    if ((uint32_t)((uint32_t)(v_stack_m98)) == 0) goto loc_00508873;
loc_00508388:
    if ((uint8_t)(v_stack_p20) != 0) goto loc_005083CA;
    if (((uint32_t)(local_rdi)) == 99) goto loc_0050839B;
    if (((uint32_t)(local_rdi)) == 115) goto loc_0050839B;
    if (((uint32_t)(local_rdi)) != 123) goto loc_005083CA;
loc_0050839B:
    v_stack_m70 = v_stack_m70 + 8;
    Arg4 = (v_stack_m70 + 8) + (8);
    v_stack_p18 = Arg4;
    v_stack_m68 = *(uint64_t *)(v_stack_m70);
    v_stack_m60 = *(uint64_t *)(v_stack_m70);
    if (((uint32_t)(*(uint32_t *)(v_stack_m70 + 0x8))) < 1) goto loc_005088A6;
    result = 0;
loc_005083CA:
    if (((uint32_t)(local_rdi)) > 112) goto loc_00508457;
    if (((uint32_t)(local_rdi)) == 112) goto loc_0050843A;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - (99));
    if (condition_is_equal) goto loc_00508420;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00508445;
    Arg1 = (uint32_t)((Arg1) - (5));
    if (condition_is_equal) goto loc_00508409;
    Arg1 = (uint32_t)((Arg1) - (5));
    if (condition_is_equal) goto loc_005083F5;
    if (((uint32_t)(Arg1)) == 1) goto loc_00508445;
    goto loc_0050846F;
loc_005083F5:
    Arg4 = 0;
    if (v_stack_p20 == 0) goto loc_0050877B;
    goto loc_0050881D;
loc_00508409:
loc_0050840E:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 45) goto loc_0050849E;
    v_stack_mA6 = 1;
    goto loc_005084A3;
loc_00508420:
    if ((uint32_t)((uint32_t)(v_stack_m90)) != 0) goto loc_005087A4;
    local_r10 = (uint32_t)(((uint32_t)(v_stack_m98)) + 1);
    goto loc_005087A4;
loc_0050843A:
    v_stack_mA8 = 1;
    v_stack_m80 = (uint32_t)((uint32_t)(local_rsi));
loc_00508445:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 45) goto loc_00508572;
    v_stack_mA6 = 1;
    goto loc_00508577;
loc_00508457:
    if (100 == 115) goto loc_0050879F;
    if (100 == 117) goto loc_00508445;
    if (100 == 120) goto loc_0050840E;
    if (100 == 123) goto loc_00508494;
loc_0050846F:
    if (((uint32_t)(*(uint8_t *)(local_r14 + 0x2 + 0x2))) != ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_005088BF;
    if (16 != 0) goto loc_0050881D;
    v_stack_p18 = v_stack_m70;
    goto loc_0050881D;
loc_00508494:
    goto loc_005087A4;
loc_0050849E:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 43) goto loc_005084C9;
loc_005084A3:
    local_r10 = (uint32_t)((local_r10) - (1));
    v_stack_m98 = (uint32_t)(local_r10);
    if (condition_is_not_equal) goto loc_005084B7;
    if ((uint32_t)(v_stack_m70) == 0) goto loc_005084B7;
    goto loc_005084C9;
loc_005084B7:
    local_rsi = (uint32_t)((local_rsi) + 1);
    v_stack_mA0 = (uint32_t)(local_rsi);
    result = _inc(v_stack_p8, *(uint64_t *)(v_stack_m70), v_stack_m70, Arg4);
    v_stack_m9C = (uint32_t)(result);
loc_005084C9:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 48) goto loc_00508536;
    local_rsi = (uint32_t)((local_rsi) + 1);
    v_stack_mA0 = (uint32_t)(local_rsi);
    result = _inc(v_stack_p8, *(uint64_t *)(v_stack_m70), v_stack_m70, Arg4);
    v_stack_m9C = (uint32_t)(result);
    result = (uint32_t)((result) + (-88));
    if ((((uint8_t)(result)) & (223)) == 0) goto loc_0050853C;
    v_stack_m78 = 1;
    if (100 == 120) goto loc_0050851A;
    Arg4 = 0;
    if ((uint32_t)((uint32_t)(v_stack_m90)) == 0) goto loc_00508510;
    local_r15 = (uint32_t)(((uint32_t)(v_stack_m98)) - (1));
    local_r12 = 1;
    if (!(condition_is_not_equal)) {
        local_r12 = (uint8_t)((1) + 1);
    }
    goto loc_005085A9;
loc_0050851A:
    local_rsi = (uint32_t)((local_rsi) - 1);
    v_stack_mA0 = (uint32_t)(local_rsi);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)(local_r13))) {
        Arg2 = local_r15;
        Arg1 = (uint32_t)((uint32_t)((uint32_t)(result)));
        result = ungetc_nolock(Arg1, Arg2, (uint32_t)(v_stack_m90), Arg4);
    }
    v_stack_m9C = 48;
loc_00508536:
    goto loc_005085A2;
loc_0050853C:
    local_rsi = (uint32_t)((local_rsi) + 1);
    v_stack_mA0 = (uint32_t)(local_rsi);
    result = _inc(local_r15, Arg2, (uint32_t)(v_stack_m90), Arg4);
    Arg4 = 0;
    v_stack_m9C = (uint32_t)(result);
    if ((uint32_t)((uint32_t)(v_stack_m90)) == 0) goto loc_0050856B;
    local_r15 = (uint32_t)(((uint32_t)(v_stack_m98)) - (2));
    if (((uint32_t)(local_r15)) < 1) {
        local_r12 = (uint8_t)((local_r12) + 1);
    }
    goto loc_005085A9;
loc_00508572:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 43) goto loc_005085A2;
loc_00508577:
    local_r10 = (uint32_t)((local_r10) - (1));
    v_stack_m98 = (uint32_t)(local_r10);
    if (condition_is_not_equal) goto loc_0050858E;
    if ((uint32_t)((uint32_t)(v_stack_m90)) == 0) goto loc_0050858E;
    goto loc_005085A6;
loc_0050858E:
    local_rsi = (uint32_t)((local_rsi) + 1);
    v_stack_mA0 = (uint32_t)(local_rsi);
    result = _inc(v_stack_p8, Arg2, (uint32_t)(v_stack_m90), Arg4);
    v_stack_m9C = (uint32_t)(result);
    goto loc_00508536;
loc_005085A2:
loc_005085A6:
    Arg4 = 0;
loc_005085A9:
    if (v_stack_m88 == 0) goto loc_00508696;
    if (1 != 0) goto loc_0050867B;
loc_005085BC:
    if ((((uint32_t)(120 - 112)) & (0xFFFFFFF7ULL)) == 0) goto loc_005085FC;
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0x8F7A3D) + (uint8_t)((uint32_t)((uint32_t)(result))) * 2)) & (4)) == 0) goto loc_00508663;
    if (120 != 111) goto loc_005085F3;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) >= 56) goto loc_005085EE;
    Arg2 = (v_stack_m80) << (3);
    goto loc_00508620;
loc_005085EE:
    goto loc_00508624;
loc_005085F3:
    Arg2 = (Arg2 + Arg2 * 4) + (Arg2 + Arg2 * 4);
    goto loc_00508620;
loc_005085FC:
    if (!sign_flag) goto loc_00508663;
    Arg2 = (v_stack_m80) << (4);
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((int8_t)((uint8_t)((uint32_t)((uint32_t)(result))))))) & (0xFFFFFFDFULL));
    local_rbx = (uint32_t)((local_rbx) - (7));
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x8F7A3D) + (uint8_t)((uint32_t)((uint32_t)(result))) * 2))) & (4)) != 0) { local_rbx = (uint32_t)((int8_t)((uint8_t)((uint32_t)((uint32_t)(result))))); }
    v_stack_m9C = (uint32_t)(local_rbx);
loc_00508620:
    v_stack_m80 = Arg2;
loc_00508624:
    if (1 != 0) goto loc_00508663;
    Arg2 = (Arg2) + ((int32_t)((uint32_t)(local_rbx - 48)));
    v_stack_m80 = Arg2;
    if ((uint32_t)((uint32_t)(v_stack_m90)) == 0) goto loc_00508644;
    local_r15 = (uint32_t)(((uint32_t)(v_stack_m98)) - (1));
    if (condition_is_equal) goto loc_0050867F;
loc_00508644:
    local_rsi = (uint32_t)((local_rsi) + 1);
    v_stack_mA0 = (uint32_t)(local_rsi);
    result = _inc(v_stack_p8, Arg2, (uint32_t)(v_stack_m90), Arg4);
    v_stack_m9C = (uint32_t)(result);
    Arg4 = 0;
    goto loc_005085BC;
loc_00508663:
    local_rsi = (uint32_t)((local_rsi) - 1);
    v_stack_mA0 = (uint32_t)(local_rsi);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)(local_r13))) {
        Arg2 = v_stack_p8;
        Arg1 = (uint32_t)((uint32_t)((uint32_t)(result)));
        result = ungetc_nolock(Arg1, Arg2, (uint32_t)(v_stack_m90), Arg4);
        Arg4 = 0;
    }
loc_0050867F:
    result = -(v_stack_m80);
    if (v_stack_mA6 == 0) { result = v_stack_m80; }
    v_stack_m80 = result;
    goto loc_0050875D;
loc_00508696:
    if (1 != 0) goto loc_0050874F;
loc_0050869F:
    if ((((uint32_t)(120 - 112)) & (0xFFFFFFF7ULL)) == 0) goto loc_005086D8;
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0x8F795A) + (uint8_t)((uint32_t)((uint32_t)(result))) * 2)) & (4)) == 0) goto loc_00508737;
    if (120 != 111) goto loc_005086D0;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) >= 56) goto loc_005086CB;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m94)) << (3));
    goto loc_005086FA;
loc_005086CB:
    goto loc_005086FD;
loc_005086D0:
    goto loc_005086FA;
loc_005086D8:
    if (!sign_flag) goto loc_00508737;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m94)) << (4));
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((int8_t)((uint8_t)((uint32_t)((uint32_t)(result))))))) & (0xFFFFFFDFULL));
    local_rbx = (uint32_t)((local_rbx) - (7));
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x8F795A) + Arg2 + Arg2 * 4 * 2))) & (4)) != 0) { local_rbx = (uint32_t)((int8_t)((uint8_t)((uint32_t)((uint32_t)(result))))); }
    v_stack_m9C = (uint32_t)(local_rbx);
loc_005086FA:
    v_stack_m94 = (uint32_t)(Arg2);
loc_005086FD:
    if (1 != 0) goto loc_00508737;
    Arg2 = (uint32_t)((Arg2) + (-48));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_rbx)));
    v_stack_m94 = (uint32_t)(Arg2);
    if ((uint32_t)((uint32_t)(v_stack_m90)) == 0) goto loc_00508718;
    local_r15 = (uint32_t)((local_r15) - (1));
    if (condition_is_equal) goto loc_00508752;
loc_00508718:
    local_rsi = (uint32_t)((local_rsi) + 1);
    v_stack_mA0 = (uint32_t)(local_rsi);
    result = _inc(v_stack_p8, Arg2, (uint32_t)(v_stack_m90), Arg4);
    v_stack_m9C = (uint32_t)(result);
    Arg4 = 0;
    goto loc_0050869F;
loc_00508737:
    local_rsi = (uint32_t)((local_rsi) - 1);
    v_stack_mA0 = (uint32_t)(local_rsi);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)(local_r13))) {
        Arg2 = v_stack_p8;
        Arg1 = (uint32_t)((uint32_t)((uint32_t)(result)));
        result = ungetc_nolock(Arg1, Arg2, (uint32_t)(v_stack_m90), Arg4);
        Arg4 = 0;
    }
loc_00508752:
    if (v_stack_mA6 != 0) {
        Arg2 = (uint32_t)(-((uint32_t)(v_stack_m94)));
        v_stack_m94 = (uint32_t)(Arg2);
    }
    if (v_stack_m78 == 0) goto loc_005088E5;
    if (v_stack_p20 != 0) goto loc_0050881D;
loc_0050877B:
    if (v_stack_m88 == 0) goto loc_0050878D;
    *(uint64_t *)(v_stack_m68) = v_stack_m80;
    goto loc_0050881D;
loc_0050878D:
    if (v_stack_mA8 == 0) goto loc_0050879A;
    *(uint32_t *)(v_stack_m68) = (uint32_t)(v_stack_m80);
    goto loc_0050881D;
loc_0050879A:
    *(uint16_t *)(v_stack_m68) = (uint16_t)(v_stack_m80);
    goto loc_0050881D;
loc_0050879F:
loc_005087A4:
    result = (uint32_t)((32) | (1));
    if ((uint32_t)((uint32_t)(v_stack_m90)) == 0) { result = 32; }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) | (2));
    if (condition_is_less_or_equal) { Arg1 = (uint32_t)(result); }
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (4));
    if (v_stack_p20 == 1) { result = (uint32_t)(Arg1); }
    v_stack_mB8 = v_stack_mA4;
    v_stack_mC0 = 0;
    v_stack_mC8 = v_stack_p8;
    v_stack_mD0 = (uint32_t)(local_r10);
    v_stack_mD8 = v_stack_m60;
    if (120 != 123) goto loc_00508805;
    result = ReadStringDelimited((uint32_t)((uint32_t)(result)), v_stack_p10, v_stack_m9C, v_stack_mA0);
    goto loc_0050880C;
loc_00508805:
    Arg2 = 0;
    result = ReadString((uint32_t)((uint32_t)(result)), Arg2, v_stack_m9C, v_stack_mA0);
loc_0050880C:
    Arg4 = 0;
    if ((uint32_t)(result) != 0) goto loc_005088D5;
loc_0050881D:
    local_r14 = (v_stack_p10) + 1;
    goto loc_0050884F;
loc_00508828:
    local_r14 = (local_r14) + 1;
loc_0050882B:
    local_rsi = (uint32_t)(((uint32_t)(v_stack_mA0)) + 1);
    v_stack_mA0 = (uint32_t)(local_rsi);
    result = _inc(v_stack_p8, Arg2, v_stack_m9C, Arg4);
    v_stack_m9C = (uint32_t)(result);
    local_r14 = (local_r14) + 1;
    if (((uint32_t)(*(uint8_t *)(local_r14))) != ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_005088DA;
loc_0050884F:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)(local_r13))) goto loc_00508860;
    if ((*(uint8_t *)(local_r14)) != 37) goto loc_00508882;
    if ((*(uint8_t *)(local_r14 + 0x1)) != 110) goto loc_00508882;
loc_00508860:
    Arg4 = 0;
    if ((uint8_t)(*(uint8_t *)(local_r14)) == 0) goto loc_005088D5;
    goto loc_00508101;
loc_00508873:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)(local_r13))) goto loc_00508882;
loc_0050887B:
    result = ungetc_nolock((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_p8, v_stack_m9C, Arg4);
loc_00508882:
loc_00508885:
    Arg4 = 0;
loc_00508888:
loc_0050888B:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)(local_r13))) goto loc_005088EA;
loc_00508890:
    Arg1 = 0;
    if ((uint32_t)((uint32_t)(v_stack_mA4)) != 0) goto loc_0050889E;
    if (v_stack_mA7 != 0) {
        local_r13 = (uint32_t)((uint32_t)(v_stack_mA4));
    }
    goto loc_0050891A;
loc_005088A6:
    Arg4 = 0;
    if (condition_is_less_or_equal) goto loc_005088B7;
    *(uint16_t *)((uint32_t)(v_stack_m8C)) = 0;
    goto loc_005088BA;
loc_005088B7:
    *(uint8_t *)((uint32_t)(v_stack_m8C)) = 0;
loc_005088BA:
    goto loc_0050888B;
loc_005088BF:
    result = (uint32_t)(v_stack_mA4);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)(local_r13))) {
        Arg2 = v_stack_p8;
        Arg1 = (uint32_t)((uint32_t)((uint32_t)(result)));
        result = ungetc_nolock(Arg1, Arg2, v_stack_m9C, Arg4);
    }
    goto loc_00508885;
loc_005088D5:
    goto loc_00508888;
loc_005088DA:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)(local_r13))) goto loc_00508882;
    goto loc_0050887B;
loc_005088E5:
    goto loc_00508888;
loc_005088EA:
    if (((uint32_t)((uint32_t)(v_stack_m8C))) != 1) goto loc_0050891A;
    v_stack_mD8 = 0;
    Arg3 = 0;
    Arg4 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = EmpCheckErrataList(Arg1, Arg2, Arg3, Arg4);
    goto loc_0050891A;
loc_00508908:
    Arg3 = 0;
    v_stack_mD8 = 0;
    Arg1 = 0;
    result = EmpCheckErrataList(Arg1, Arg2, Arg3, Arg4);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
loc_0050891A:
    local_rsp = (local_rsp) + (184);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00508090&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
