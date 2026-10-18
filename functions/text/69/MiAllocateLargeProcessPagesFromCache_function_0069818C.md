# MiAllocateLargeProcessPagesFromCache

- RVA: `0x0069818C`–`0x006987BA` (길이 `1,582` bytes)
- VA: `0x000000014069818C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CC7C4`
- 디코드: `410`개 명령, `1,582/1,582` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006981DD` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x006981F9` → [MiGetVadCacheAttribute](../4A/MiGetVadCacheAttribute_function_004AF624.md) (function, `0x004AF624`)
- `0x00698290` → [MiCreateProcessLargePageCacheAnchor](MiCreateProcessLargePageCacheAnchor_function_00698A44.md) (function, `0x00698A44`)
- `0x006982BF` → [MiComputePreferredNode](../3D/MiComputePreferredNode_function_003D3438.md) (function, `0x003D3438`)
- `0x00698333` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x006984D1` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x00698512` → [MiZeroLargePage](../2C/MiZeroLargePage_function_002C6914.md) (function, `0x002C6914`)
- `0x006985E8` → [MiCreateLargePfnList](../3D/MiCreateLargePfnList_function_003D2DA8.md) (function, `0x003D2DA8`)
- `0x00698606` → [MiReturnResident](../28/MiReturnResident_function_00286890.md) (function, `0x00286890`)
- `0x00698625` → [MiPopLargePfnList](../49/MiPopLargePfnList_function_0049C460.md) (function, `0x0049C460`)
- `0x00698676` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x00698729` → [RtlSetBits](../3E/RtlSetBits_function_003E1610.md) (function, `0x003E1610`)
- `0x00698756` → [MiSetOriginalPtePfnFromFreeList](../28/MiSetOriginalPtePfnFromFreeList_function_0028A99C.md) (function, `0x0028A99C`)
- `0x00698777` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x0069878B` → [MiFreeLargeZeroPages](../3B/MiFreeLargeZeroPages_function_003B5F0C.md) (function, `0x003B5F0C`)
- `0x00698799` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_006E962C](../6E/Unknown_function_006E962C.md) at `0x006E967F`

### Static image references
- `0x006981A8` → RVA `0x00E0A740` (`.data`; read)
- `0x00698258` → RVA `0x00E30088` (`.data`; read)
- `0x00698550` → RVA `0x00FC5000` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0069818C  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00698191  55                              push rbp
00698192  56                              push rsi
00698193  57                              push rdi
00698194  41 54                           push r12
00698196  41 55                           push r13
00698198  41 56                           push r14
0069819A  41 57                           push r15
0069819C  48 8D 6C 24 E0                  lea rbp, [rsp - 0x20]
006981A1  48 81 EC 20 01 00 00            sub rsp, 0x120
006981A8  48 8B 05 91 25 77 00            mov rax, qword ptr [rip + 0x772591]
006981AF  48 33 C4                        xor rax, rsp
006981B2  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
006981B6  4C 8B AD 88 00 00 00            mov r13, qword ptr [rbp + 0x88]
006981BD  41 8B D9                        mov ebx, r9d
006981C0  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
006981C5  49 8B F0                        mov rsi, r8
006981C8  33 D2                           xor edx, edx
006981CA  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
006981CE  4C 8B F1                        mov r14, rcx
006981D1  89 5C 24 54                     mov dword ptr [rsp + 0x54], ebx
006981D5  48 8D 4D B0                     lea rcx, [rbp - 0x50]
006981D9  44 8D 42 60                     lea r8d, [rdx + 0x60]
006981DD  E8 5E EA 02 00                  call 0x1406c6c40
006981E2  4D 8B 06                        mov r8, qword ptr [r14]
006981E5  45 33 C9                        xor r9d, r9d
006981E8  BA 01 00 00 00                  mov edx, 1
006981ED  48 89 55 88                     mov qword ptr [rbp - 0x78], rdx
006981F1  4D 85 C0                        test r8, r8
006981F4  74 21                           je 0x140698217
006981F6  49 8B C8                        mov rcx, r8
006981F9  E8 26 74 E1 FF                  call 0x1404af624
006981FE  41 8B 48 30                     mov ecx, dword ptr [r8 + 0x30]
00698202  44 8B E0                        mov r12d, eax
00698205  B8 00 00 A0 01                  mov eax, 0x1a00000
0069820A  45 8B F9                        mov r15d, r9d
0069820D  23 C8                           and ecx, eax
0069820F  3B C8                           cmp ecx, eax
00698211  41 0F 94 C7                     sete r15b
00698215  EB 2E                           jmp 0x140698245
00698217  41 8B 4E 14                     mov ecx, dword ptr [r14 + 0x14]
0069821B  8B C1                           mov eax, ecx
0069821D  C1 E8 03                        shr eax, 3
00698220  83 F8 03                        cmp eax, 3
00698223  75 0B                           jne 0x140698230
00698225  F6 C1 07                        test cl, 7
00698228  74 0D                           je 0x140698237
0069822A  44 8D 60 FF                     lea r12d, [rax - 1]
0069822E  EB 0A                           jmp 0x14069823a
00698230  45 8B E1                        mov r12d, r9d
00698233  3B C2                           cmp eax, edx
00698235  74 03                           je 0x14069823a
00698237  44 8B E2                        mov r12d, edx
0069823A  45 39 4E 10                     cmp dword ptr [r14 + 0x10], r9d
0069823E  45 8B F9                        mov r15d, r9d
00698241  41 0F 95 C7                     setne r15b
00698245  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0069824E  45 33 C0                        xor r8d, r8d
00698251  48 8B B8 B8 00 00 00            mov rdi, qword ptr [rax + 0xb8]
00698258  48 8B 05 29 7E 79 00            mov rax, qword ptr [rip + 0x797e29]
0069825F  4C 8B 97 10 04 00 00            mov r10, qword ptr [rdi + 0x410]
00698266  0F B7 8F AE 04 00 00            movzx ecx, word ptr [rdi + 0x4ae]
0069826D  49 81 C2 00 03 00 00            add r10, 0x300
00698274  4C 89 55 80                     mov qword ptr [rbp - 0x80], r10
00698278  4D 8B 8A 18 01 00 00            mov r9, qword ptr [r10 + 0x118]
0069827F  4C 8B 1C C8                     mov r11, qword ptr [rax + rcx*8]
00698283  4C 89 5C 24 78                  mov qword ptr [rsp + 0x78], r11
00698288  4D 85 C9                        test r9, r9
0069828B  75 20                           jne 0x1406982ad
0069828D  49 8B CB                        mov rcx, r11
00698290  E8 AF 07 00 00                  call 0x140698a44
00698295  45 33 C0                        xor r8d, r8d
00698298  4C 8B C8                        mov r9, rax
0069829B  48 85 C0                        test rax, rax
0069829E  0F 84 4D 03 00 00               je 0x1406985f1
006982A4  4C 8B 55 80                     mov r10, qword ptr [rbp - 0x80]
006982A8  4C 8B 5C 24 78                  mov r11, qword ptr [rsp + 0x78]
006982AD  85 DB                           test ebx, ebx
006982AF  0F 85 9B 02 00 00               jne 0x140698550
006982B5  49 8B 16                        mov rdx, qword ptr [r14]
006982B8  48 8D 8F 00 04 00 00            lea rcx, [rdi + 0x400]
006982BF  E8 74 B1 D3 FF                  call 0x1403d3438
006982C4  45 33 C0                        xor r8d, r8d
006982C7  41 8B 8B 58 40 00 00            mov ecx, dword ptr [r11 + 0x4058]
006982CE  41 BB 3F 00 00 00               mov r11d, 0x3f
006982D4  41 89 49 18                     mov dword ptr [r9 + 0x18], ecx
006982D8  49 83 C1 20                     add r9, 0x20
006982DC  8B C8                           mov ecx, eax
006982DE  49 63 C4                        movsxd rax, r12d
006982E1  48 C1 EE 04                     shr rsi, 4
006982E5  44 89 5C 24 64                  mov dword ptr [rsp + 0x64], r11d
006982EA  48 8D 14 49                     lea rdx, [rcx + rcx*2]
006982EE  41 8B C8                        mov ecx, r8d
006982F1  48 03 C2                        add rax, rdx
006982F4  48 C1 E0 06                     shl rax, 6
006982F8  49 03 C1                        add rax, r9
006982FB  45 8D 4B C2                     lea r9d, [r11 - 0x3e]
006982FF  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00698304  48 8D 50 0C                     lea rdx, [rax + 0xc]
00698308  44 84 1A                        test byte ptr [rdx], r11b
0069830B  75 12                           jne 0x14069831f
0069830D  41 03 C9                        add ecx, r9d
00698310  48 83 C2 10                     add rdx, 0x10
00698314  83 F9 04                        cmp ecx, 4
00698317  72 EF                           jb 0x140698308
00698319  0F 84 6B 02 00 00               je 0x14069858a
0069831F  49 8D 82 20 01 00 00            lea rax, [r10 + 0x120]
00698326  45 8B F0                        mov r14d, r8d
00698329  48 8B C8                        mov rcx, rax
0069832C  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
00698330  41 8B F8                        mov edi, r8d
00698333  E8 58 03 BB FF                  call 0x140248690
00698338  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0069833D  BB 3F 00 00 00                  mov ebx, 0x3f
00698342  88 44 24 50                     mov byte ptr [rsp + 0x50], al
00698346  48 83 C2 0C                     add rdx, 0xc
0069834A  41 BA FF FF 00 00               mov r10d, 0xffff
00698350  44 8D 4B C5                     lea r9d, [rbx - 0x3b]
00698354  44 8D 5B C2                     lea r11d, [rbx - 0x3e]
00698358  0F B7 4A 02                     movzx ecx, word ptr [rdx + 2]
0069835C  66 41 3B CA                     cmp cx, r10w
00698360  74 08                           je 0x14069836a
00698362  66 41 03 CB                     add cx, r11w
00698366  66 89 4A 02                     mov word ptr [rdx + 2], cx
0069836A  0F B7 0A                        movzx ecx, word ptr [rdx]
0069836D  44 0F B7 C1                     movzx r8d, cx
00698371  66 44 23 C3                     and r8w, bx
00698375  75 03                           jne 0x14069837a
00698377  45 03 F3                        add r14d, r11d
0069837A  0F B7 C1                        movzx eax, cx
0069837D  41 BB BF FF 00 00               mov r11d, 0xffbf
00698383  66 41 23 C3                     and ax, r11w
00698387  66 83 C9 40                     or cx, 0x40
0069838B  66 45 85 C0                     test r8w, r8w
0069838F  41 BB 01 00 00 00               mov r11d, 1
00698395  66 0F 45 C8                     cmovne cx, ax
00698399  66 89 0A                        mov word ptr [rdx], cx
0069839C  48 83 C2 10                     add rdx, 0x10
006983A0  4D 2B CB                        sub r9, r11
006983A3  75 B3                           jne 0x140698358
006983A5  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
006983A9  4C 8B 54 24 58                  mov r10, qword ptr [rsp + 0x58]
006983AE  41 83 FE 04                     cmp r14d, 4
006983B2  0F 84 11 01 00 00               je 0x1406984c9
006983B8  49 8D 42 0E                     lea rax, [r10 + 0xe]
006983BC  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
006983C0  41 83 C9 FF                     or r9d, 0xffffffff
006983C4  41 B8 FF FF 00 00               mov r8d, 0xffff
006983CA  33 C9                           xor ecx, ecx
006983CC  8B D1                           mov edx, ecx
006983CE  48 8B C8                        mov rcx, rax
006983D1  F6 41 FE 40                     test byte ptr [rcx - 2], 0x40
006983D5  75 10                           jne 0x1406983e7
006983D7  0F B7 01                        movzx eax, word ptr [rcx]
006983DA  66 41 3B C0                     cmp ax, r8w
006983DE  77 07                           ja 0x1406983e7
006983E0  44 0F B7 C0                     movzx r8d, ax
006983E4  44 8B CA                        mov r9d, edx
006983E7  41 03 D3                        add edx, r11d
006983EA  48 83 C1 10                     add rcx, 0x10
006983EE  83 FA 04                        cmp edx, 4
006983F1  72 DE                           jb 0x1406983d1
006983F3  41 8B D1                        mov edx, r9d
006983F6  45 03 F3                        add r14d, r11d
006983F9  48 C1 E2 04                     shl rdx, 4
006983FD  49 03 D2                        add rdx, r10
00698400  48 8B 02                        mov rax, qword ptr [rdx]
00698403  66 83 4A 0C 40                  or word ptr [rdx + 0xc], 0x40
00698408  44 8B 4A 08                     mov r9d, dword ptr [rdx + 8]
0069840C  4C 8D 1C 40                     lea r11, [rax + rax*2]
00698410  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0069841A  49 C1 E3 04                     shl r11, 4
0069841E  48 8B C0                        mov rax, rax
00698421  4C 03 D8                        add r11, rax
00698424  45 33 C0                        xor r8d, r8d
00698427  66 44 89 42 0E                  mov word ptr [rdx + 0xe], r8w
0069842C  4D 85 C9                        test r9, r9
0069842F  0F 84 37 01 00 00               je 0x14069856c
00698435  49 0F BC C1                     bsf rax, r9
00698439  41 BA FF FF FF FF               mov r10d, 0xffffffff
0069843F  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00698443  0F B6 C0                        movzx eax, al
00698446  44 0F 45 D0                     cmovne r10d, eax
0069844A  49 0F BE C2                     movsx rax, r10b
0069844E  4C 8D 04 40                     lea r8, [rax + rax*2]
00698452  0F B7 42 0C                     movzx eax, word ptr [rdx + 0xc]
00698456  0F B7 C8                        movzx ecx, ax
00698459  49 C1 E0 08                     shl r8, 8
0069845D  66 2B 4D 88                     sub cx, word ptr [rbp - 0x78]
00698461  4D 03 C3                        add r8, r11
00698464  66 33 C8                        xor cx, ax
00698467  66 23 4C 24 64                  and cx, word ptr [rsp + 0x64]
0069846C  66 33 C8                        xor cx, ax
0069846F  49 8D 45 30                     lea rax, [r13 + 0x30]
00698473  66 89 4A 0C                     mov word ptr [rdx + 0xc], cx
00698477  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0069847B  48 39 01                        cmp qword ptr [rcx], rax
0069847E  0F 85 CB 02 00 00               jne 0x14069874f
00698484  49 89 48 08                     mov qword ptr [r8 + 8], rcx
00698488  49 89 00                        mov qword ptr [r8], rax
0069848B  4C 89 01                        mov qword ptr [rcx], r8
0069848E  B9 01 00 00 00                  mov ecx, 1
00698493  4C 89 40 08                     mov qword ptr [rax + 8], r8
00698497  49 01 4D 40                     add qword ptr [r13 + 0x40], rcx
0069849B  49 8B 40 10                     mov rax, qword ptr [r8 + 0x10]
0069849F  48 A9 E0 03 00 00               test rax, 0x3e0
006984A5  74 02                           je 0x1406984a9
006984A7  03 F9                           add edi, ecx
006984A9  41 B8 01 00 00 00               mov r8d, 1
006984AF  41 8A CA                        mov cl, r10b
006984B2  41 8B C0                        mov eax, r8d
006984B5  D3 E0                           shl eax, cl
006984B7  F7 D0                           not eax
006984B9  4C 23 C8                        and r9, rax
006984BC  44 89 4A 08                     mov dword ptr [rdx + 8], r9d
006984C0  49 2B F0                        sub rsi, r8
006984C3  0F 85 63 FF FF FF               jne 0x14069842c
006984C9  8A 54 24 50                     mov dl, byte ptr [rsp + 0x50]
006984CD  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
006984D1  E8 EA FD BA FF                  call 0x1402482c0
006984D6  33 C0                           xor eax, eax
006984D8  44 8D 48 01                     lea r9d, [rax + 1]
006984DC  45 85 FF                        test r15d, r15d
006984DF  75 5D                           jne 0x14069853e
006984E1  85 FF                           test edi, edi
006984E3  74 59                           je 0x14069853e
006984E5  44 8B F0                        mov r14d, eax
006984E8  49 8B 7D 30                     mov rdi, qword ptr [r13 + 0x30]
006984EC  49 39 45 40                     cmp qword ptr [r13 + 0x40], rax
006984F0  76 4C                           jbe 0x14069853e
006984F2  33 DB                           xor ebx, ebx
006984F4  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
006984F8  48 A9 E0 03 00 00               test rax, 0x3e0
006984FE  74 2B                           je 0x14069852b
00698500  45 8B CC                        mov r9d, r12d
00698503  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00698507  41 B8 02 00 00 00               mov r8d, 2
0069850D  48 8B D7                        mov rdx, rdi
00698510  33 C9                           xor ecx, ecx
00698512  E8 FD E3 C2 FF                  call 0x1402c6914
00698517  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0069851B  41 B9 01 00 00 00               mov r9d, 1
00698521  48 25 1F FC FF FF               and rax, 0xfffffffffffffc1f
00698527  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
0069852B  48 8B 3F                        mov rdi, qword ptr [rdi]
0069852E  45 03 F1                        add r14d, r9d
00698531  41 8B C6                        mov eax, r14d
00698534  49 3B 45 40                     cmp rax, qword ptr [r13 + 0x40]
00698538  72 BA                           jb 0x1406984f4
0069853A  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
0069853E  45 33 E4                        xor r12d, r12d
00698541  48 85 F6                        test rsi, rsi
00698544  0F 84 46 02 00 00               je 0x140698790
0069854A  4C 8B 75 A0                     mov r14, qword ptr [rbp - 0x60]
0069854E  EB 3D                           jmp 0x14069858d
00698550  0F B7 0D A9 CA 92 00            movzx ecx, word ptr [rip + 0x92caa9]
00698557  8D 43 FF                        lea eax, [rbx - 1]
0069855A  3B C1                           cmp eax, ecx
0069855C  0F 82 65 FD FF FF               jb 0x1406982c7
00698562  B8 0D 00 00 C0                  mov eax, 0xc000000d
00698567  E9 26 02 00 00                  jmp 0x140698792
0069856C  41 83 FE 04                     cmp r14d, 4
00698570  0F 84 53 FF FF FF               je 0x1406984c9
00698576  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
0069857A  41 BB 01 00 00 00               mov r11d, 1
00698580  4C 8B 54 24 58                  mov r10, qword ptr [rsp + 0x58]
00698585  E9 36 FE FF FF                  jmp 0x1406983c0
0069858A  45 33 E4                        xor r12d, r12d
0069858D  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
00698592  48 8D 45 B0                     lea rax, [rbp - 0x50]
00698596  48 81 E2 00 00 E0 FF            and rdx, 0xffffffffffe00000
0069859D  B9 04 00 00 00                  mov ecx, 4
006985A2  4C 89 60 10                     mov qword ptr [rax + 0x10], r12
006985A6  48 89 40 08                     mov qword ptr [rax + 8], rax
006985AA  48 89 00                        mov qword ptr [rax], rax
006985AD  48 83 C0 18                     add rax, 0x18
006985B1  49 2B C9                        sub rcx, r9
006985B4  75 EC                           jne 0x1406985a2
006985B6  48 8D 45 B0                     lea rax, [rbp - 0x50]
006985BA  49 8B CE                        mov rcx, r14
006985BD  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
006985C2  8A 85 80 00 00 00               mov al, byte ptr [rbp + 0x80]
006985C8  C7 44 24 38 08 00 00 00         mov dword ptr [rsp + 0x38], 8
006985D0  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
006985D5  88 44 24 28                     mov byte ptr [rsp + 0x28], al
006985D9  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
006985DD  BB 00 02 00 00                  mov ebx, 0x200
006985E2  44 8B CB                        mov r9d, ebx
006985E5  44 8B C3                        mov r8d, ebx
006985E8  E8 BB A7 D3 FF                  call 0x1403d2da8
006985ED  85 C0                           test eax, eax
006985EF  79 0A                           jns 0x1406985fb
006985F1  B8 9A 00 00 C0                  mov eax, 0xc000009a
006985F6  E9 97 01 00 00                  jmp 0x140698792
006985FB  4C 8B 74 24 78                  mov r14, qword ptr [rsp + 0x78]
00698600  48 8B D3                        mov rdx, rbx
00698603  49 8B CE                        mov rcx, r14
00698606  E8 85 E2 BE FF                  call 0x140286890
0069860B  BB 20 00 00 00                  mov ebx, 0x20
00698610  48 2B DE                        sub rbx, rsi
00698613  48 85 F6                        test rsi, rsi
00698616  74 53                           je 0x14069866b
00698618  49 8D 7D 30                     lea rdi, [r13 + 0x30]
0069861C  BA 02 00 00 00                  mov edx, 2
00698621  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00698625  E8 36 3E E0 FF                  call 0x14049c460
0069862A  48 8D 0C 40                     lea rcx, [rax + rax*2]
0069862E  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00698638  48 C1 E1 04                     shl rcx, 4
0069863C  48 8B C0                        mov rax, rax
0069863F  48 03 C8                        add rcx, rax
00698642  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00698646  48 39 38                        cmp qword ptr [rax], rdi
00698649  0F 85 00 01 00 00               jne 0x14069874f
0069864F  48 89 41 08                     mov qword ptr [rcx + 8], rax
00698653  48 89 39                        mov qword ptr [rcx], rdi
00698656  48 89 08                        mov qword ptr [rax], rcx
00698659  B8 01 00 00 00                  mov eax, 1
0069865E  48 89 4F 08                     mov qword ptr [rdi + 8], rcx
00698662  49 01 45 40                     add qword ptr [r13 + 0x40], rax
00698666  48 2B F0                        sub rsi, rax
00698669  75 B1                           jne 0x14069861c
0069866B  48 8B 7D 80                     mov rdi, qword ptr [rbp - 0x80]
0069866F  48 8D 8F 20 01 00 00            lea rcx, [rdi + 0x120]
00698676  E8 15 00 BB FF                  call 0x140248690
0069867B  4C 8B 54 24 58                  mov r10, qword ptr [rsp + 0x58]
00698680  41 BD 01 00 00 00               mov r13d, 1
00698686  40 8A F0                        mov sil, al
00698689  41 8B D4                        mov edx, r12d
0069868C  4D 8D 4A 0C                     lea r9, [r10 + 0xc]
00698690  4D 8B C1                        mov r8, r9
00698693  45 8D 5D 3E                     lea r11d, [r13 + 0x3e]
00698697  41 8A 08                        mov cl, byte ptr [r8]
0069869A  41 84 CB                        test r11b, cl
0069869D  0F 85 CA 00 00 00               jne 0x14069876d
006986A3  41 03 D5                        add edx, r13d
006986A6  49 83 C0 10                     add r8, 0x10
006986AA  83 FA 04                        cmp edx, 4
006986AD  72 E8                           jb 0x140698697
006986AF  0F 85 B8 00 00 00               jne 0x14069876d
006986B5  48 8B 5D E0                     mov rbx, qword ptr [rbp - 0x20]
006986B9  49 8D 42 08                     lea rax, [r10 + 8]
006986BD  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
006986C2  41 0F B7 01                     movzx eax, word ptr [r9]
006986C6  0F B7 C8                        movzx ecx, ax
006986C9  48 C7 44 24 68 20 00 00 00      mov qword ptr [rsp + 0x68], 0x20
006986D2  66 33 4D F0                     xor cx, word ptr [rbp - 0x10]
006986D6  66 41 23 CB                     and cx, r11w
006986DA  66 33 C8                        xor cx, ax
006986DD  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
006986E7  66 41 89 09                     mov word ptr [r9], cx
006986EB  48 8B C0                        mov rax, rax
006986EE  41 23 CB                        and ecx, r11d
006986F1  66 45 89 62 0E                  mov word ptr [r10 + 0xe], r12w
006986F6  44 8B C1                        mov r8d, ecx
006986F9  48 8B D3                        mov rdx, rbx
006986FC  48 2B D0                        sub rdx, rax
006986FF  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00698704  48 C1 FA 04                     sar rdx, 4
00698708  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00698712  48 0F AF D0                     imul rdx, rax
00698716  48 8B C2                        mov rax, rdx
00698719  48 25 00 FE FF FF               and rax, 0xfffffffffffffe00
0069871F  48 2B D0                        sub rdx, rax
00698722  49 89 02                        mov qword ptr [r10], rax
00698725  48 C1 EA 04                     shr rdx, 4
00698729  E8 E2 8E D4 FF                  call 0x1403e1610
0069872E  45 8B C4                        mov r8d, r12d
00698731  4C 39 65 F0                     cmp qword ptr [rbp - 0x10], r12
00698735  76 33                           jbe 0x14069876a
00698737  48 8D 4B 10                     lea rcx, [rbx + 0x10]
0069873B  45 85 FF                        test r15d, r15d
0069873E  75 16                           jne 0x140698756
00698740  48 8B 01                        mov rax, qword ptr [rcx]
00698743  48 25 1F FC FF FF               and rax, 0xfffffffffffffc1f
00698749  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
0069874D  EB 0C                           jmp 0x14069875b
0069874F  B9 03 00 00 00                  mov ecx, 3
00698754  CD 29                           int 0x29
00698756  E8 41 22 BF FF                  call 0x14028a99c
0069875B  48 8B 1B                        mov rbx, qword ptr [rbx]
0069875E  45 03 C5                        add r8d, r13d
00698761  41 8B C0                        mov eax, r8d
00698764  48 3B 45 F0                     cmp rax, qword ptr [rbp - 0x10]
00698768  72 CD                           jb 0x140698737
0069876A  49 8B DC                        mov rbx, r12
0069876D  40 8A D6                        mov dl, sil
00698770  48 8D 8F 20 01 00 00            lea rcx, [rdi + 0x120]
00698777  E8 44 FB BA FF                  call 0x1402482c0
0069877C  48 85 DB                        test rbx, rbx
0069877F  74 0F                           je 0x140698790
00698781  45 8B C7                        mov r8d, r15d
00698784  48 8D 55 B0                     lea rdx, [rbp - 0x50]
00698788  49 8B CE                        mov rcx, r14
0069878B  E8 7C D7 D1 FF                  call 0x1403b5f0c
00698790  33 C0                           xor eax, eax
00698792  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00698796  48 33 CC                        xor rcx, rsp
00698799  E8 A2 3E 01 00                  call 0x1406ac640
0069879E  48 8B 9C 24 70 01 00 00         mov rbx, qword ptr [rsp + 0x170]
006987A6  48 81 C4 20 01 00 00            add rsp, 0x120
006987AD  41 5F                           pop r15
006987AF  41 5E                           pop r14
006987B1  41 5D                           pop r13
006987B3  41 5C                           pop r12
006987B5  5F                              pop rdi
006987B6  5E                              pop rsi
006987B7  5D                              pop rbp
006987B8  C3                              ret
006987B9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAllocateLargeProcessPagesFromCache(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned __int8 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m104;
    unsigned __int8 v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int8 v_stack_m130;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int16 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned int v_stack_mF8;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (288);
    result = (*(unsigned __int64 *)(v_rip + 7808401)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_mF0 = a2;
    a2 = 0;
    v_stack_mB8 = a1;
    v_stack_m104 = (unsigned int)((unsigned int)(a4));
    result = memset(v_stack_mA8, a2, a2 + 96, a4);
    a4 = 0;
    v_stack_mD0 = 1;
    if (*(unsigned __int64 *)(a1) == 0) goto loc_00698217;
    result = MiGetVadCacheAttribute(*(unsigned __int64 *)(a1), 1, *(unsigned __int64 *)(a1), a4);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 48))) & ((unsigned int)((unsigned int)(0x1A00000ULL))));
    v_r15 = (((unsigned int)(a1)) == ((unsigned int)((unsigned int)(0x1A00000ULL)))) ? 1 : 0;
    goto loc_00698245;
loc_00698217:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20))))) >> (3));
    if (((unsigned int)(result)) != 3) goto loc_00698230;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 20)))) & (7)) == 0) goto loc_00698237;
    goto loc_0069823A;
loc_00698230:
    v_r12 = 0;
    if (((unsigned int)(result)) != 1) {
        v_r12 = 1;
    }
    v_r15 = ((*(unsigned int *)(a1 + 16)) != 0) ? 1 : 0;
loc_00698245:
    a3 = 0;
    v_r10 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1040)) + (768);
    v_stack_mD8 = v_r10;
    v_stack_mE0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7962153) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8);
    if (*(unsigned __int64 *)(v_r10 + 280) != 0) goto loc_006982AD;
    result = MiCreateProcessLargePageCacheAnchor(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7962153) + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1198) * 8), 1, a3, *(unsigned __int64 *)(v_r10 + 280));
    a3 = 0;
    if (result == 0) goto loc_006985F1;
loc_006982AD:
    if ((unsigned int)((unsigned int)(a4)) != 0) goto loc_00698550;
    result = MiComputePreferredNode(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024, *(unsigned __int64 *)(a1), a3, result);
    a3 = 0;
loc_006982C7:
    *(unsigned int *)(result + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mE0 + 16472)));
    a4 = (result) + (32);
    v_rsi = (a3) >> (4);
    v_stack_mF4 = 63;
    result = ((int)((unsigned int)(v_r12))) + ((unsigned int)((unsigned int)(result)) + (unsigned int)((unsigned int)(result)) * 2);
    result = (result) << (6);
    result = (result) + (a4);
    v_stack_m100 = result;
loc_00698308:
    if (((*(unsigned __int8 *)(result + 12)) & (63)) != 0) goto loc_0069831F;
    a1 = (unsigned int)((0) + ((unsigned int)(63 - 62)));
    a2 = (result + 12) + (16);
    if (((unsigned int)(a1)) < 4) goto loc_00698308;
    if (((unsigned int)(a1)) == 4) goto loc_0069858A;
loc_0069831F:
    v_stack_mC0 = v_stack_mD8 + 288;
    result = ExAcquireSpinLockExclusive(v_stack_mD8 + 288, a2, a3, 63 - 62);
    v_stack_m108 = (unsigned __int8)(result);
    a2 = (v_stack_m100) + (12);
loc_00698358:
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 2))) != ((unsigned __int16)((unsigned int)(0xFFFFULL)))) {
        a1 = (unsigned __int16)((*(unsigned __int16 *)(a2 + 2)) + ((unsigned __int16)(63 - 62)));
        *(unsigned __int16 *)(a2 + 2) = (unsigned __int16)(a1);
    }
    a3 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a2))) & (63));
    v_r14 = 0;
    if (!(condition_is_not_equal)) {
        v_r14 = (unsigned int)((0) + ((unsigned int)(63 - 62)));
    }
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a2))) & ((unsigned __int16)((unsigned int)(0xFFBFULL))));
    a1 = (unsigned __int16)((*(unsigned __int16 *)(a2)) | (64));
    if ((unsigned __int16)(a3) != 0) { a1 = (unsigned __int16)(result); }
    *(unsigned __int16 *)(a2) = (unsigned __int16)(a1);
    a2 = (a2) + (16);
    a4 = (63 - 59) - (1);
    if (condition_is_not_equal) goto loc_00698358;
    if (((unsigned int)(v_r14)) == 4) goto loc_006984C9;
    v_stack_mC8 = v_stack_m100 + 14;
loc_006983C0:
    a4 = (unsigned int)((a4) | (0xFFFFFFFFULL));
    a1 = 0;
loc_006983D1:
    if (((*(unsigned __int8 *)(v_stack_m100 + 14 - 2)) & (64)) != 0) goto loc_006983E7;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m100 + 14))) <= ((unsigned __int16)((unsigned int)(0xFFFFULL)))) {
        a3 = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m100 + 14));
        a4 = 0;
    }
    a2 = (unsigned int)((0) + (1));
    a1 = (v_stack_m100 + 14) + (16);
    if (((unsigned int)(a2)) < 4) goto loc_006983D1;
    v_r14 = (unsigned int)((v_r14) + (1));
    a2 = ((unsigned int)(a4)) << (4);
    a2 = (a2) + (v_stack_m100);
    v_r11 = (*(unsigned __int64 *)(a2) + *(unsigned __int64 *)(a2) * 2) << (4);
    v_r11 = (v_r11) + (*(unsigned __int64 *)(a2));
    a3 = 0;
    *(unsigned __int16 *)(a2 + 14) = 0;
loc_0069842C:
    if ((unsigned int)(*(unsigned int *)(a2 + 8)) == 0) goto loc_0069856C;
    v_stack_mF8 = (unsigned int)(*(unsigned __int64 *)(a2));
    v_r10 = (unsigned int)(0xFFFFFFFFULL);
    if ((unsigned int)(*(unsigned int *)(a2 + 8)) != 0) { v_r10 = (unsigned int)((unsigned __int8)(*(unsigned __int64 *)(a2))); }
    a3 = ((__int8)((unsigned __int8)(v_r10)) + (__int8)((unsigned __int8)(v_r10)) * 2) << (8);
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a2 + 12))) - (v_stack_mD0));
    a3 = (a3) + (v_r11);
    a1 = (unsigned __int16)((a1) ^ ((unsigned __int16)(*(unsigned __int16 *)(a2 + 12))));
    a1 = (unsigned __int16)((a1) & (v_stack_mF4));
    a1 = (unsigned __int16)((a1) ^ ((unsigned __int16)(*(unsigned __int16 *)(a2 + 12))));
    *(unsigned __int16 *)(a2 + 12) = (unsigned __int16)(a1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 48 + 8))) != (a6 + 48)) goto loc_0069874F;
    *(unsigned __int64 *)(a3 + 8) = *(unsigned __int64 *)(a6 + 48 + 8);
    *(unsigned __int64 *)(a3) = a6 + 48;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 48 + 8)) = a3;
    *(unsigned __int64 *)(a6 + 48 + 8) = a3;
    v_rdi = 0;
    if (((*(unsigned __int64 *)(a3 + 16)) & (992)) != 0) {
        v_rdi = (unsigned int)((0) + (1));
    }
    result = (unsigned int)((1) << ((unsigned __int8)((unsigned __int8)(v_r10))));
    result = (unsigned int)(~(result));
    a4 = ((unsigned int)(*(unsigned int *)(a2 + 8))) & (result);
    *(unsigned int *)(a2 + 8) = a4;
    v_rsi = (v_rsi) - (1);
    if (condition_is_not_equal) goto loc_0069842C;
loc_006984C9:
    result = MiReleaseSpinLockExclusive(v_stack_mC0, v_stack_m108, 1, a4);
    result = 0;
    if ((unsigned int)(v_r15) != 0) goto loc_0069853E;
    if ((unsigned int)(v_rdi) == 0) goto loc_0069853E;
    if ((*(unsigned __int64 *)(a6 + 64)) <= 0) goto loc_0069853E;
    v_rbx = 0;
loc_006984F4:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 48) + 16);
    if (((*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 48) + 16)) & (992)) != 0) {
        a4 = (unsigned int)(v_r12);
        v_stack_m138 = 0;
        a3 = 2;
        a2 = *(unsigned __int64 *)(a6 + 48);
        a1 = 0;
        result = MiZeroLargePage(a1, a2, a3, a4);
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 48) + 16);
        a4 = 1;
        result = (result) & (-993);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 48) + 16) = result;
    }
    v_r14 = (unsigned int)((0) + (a4));
    if (((unsigned int)((unsigned int)(v_r14))) < (*(unsigned __int64 *)(a6 + 64))) goto loc_006984F4;
loc_0069853E:
    v_r12 = 0;
    if (v_rsi == 0) goto loc_00698790;
    goto loc_0069858D;
loc_00698550:
    if (((unsigned int)((unsigned int)(v_stack_m104) - 1)) < ((unsigned int)(*(unsigned __int16 *)(v_rip + 9620137)))) goto loc_006982C7;
    goto loc_00698792;
loc_0069856C:
    if (((unsigned int)(v_stack_mB8)) == 4) goto loc_006984C9;
    goto loc_006983C0;
loc_0069858A:
    v_r12 = 0;
loc_0069858D:
    a2 = (v_stack_mF0) & (0xFFFFFFFFFFE00000ULL);
loc_006985A2:
    *(unsigned __int64 *)(v_stack_mA8 + 16) = 0;
    *(unsigned __int64 *)(v_stack_mA8 + 8) = v_stack_mA8;
    *(unsigned __int64 *)(v_stack_mA8) = v_stack_mA8;
    result = (v_stack_mA8) + (24);
    a1 = (4) - (a4);
    if (condition_is_not_equal) goto loc_006985A2;
    v_stack_m118 = v_stack_mA8;
    v_stack_m120 = 8;
    v_stack_m128 = 0;
    v_stack_m130 = a5;
    v_stack_m138 = (unsigned int)((unsigned int)(v_stack_m104));
    result = MiCreateLargePfnList(v_stack_mB8, a2, 512, 512);
    if (!sign_flag) goto loc_006985FB;
loc_006985F1:
    goto loc_00698792;
loc_006985FB:
    result = MiReturnResident(v_stack_mE0, 512, 512, 512);
    v_rbx = (32) - (v_rsi);
    if (v_rsi == 0) goto loc_0069866B;
loc_0069861C:
    result = MiPopLargePfnList(v_stack_mA8, 2, 512, 512);
    a1 = (result + result * 2) << (4);
    a1 = (a1) + (result);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 48 + 8))) != (a6 + 48)) goto loc_0069874F;
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(a6 + 48 + 8);
    *(unsigned __int64 *)(a1) = a6 + 48;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 48 + 8)) = a1;
    *(unsigned __int64 *)(a6 + 48 + 8) = a1;
    v_rsi = (v_rsi) - (1);
    if (condition_is_not_equal) goto loc_0069861C;
loc_0069866B:
    result = ExAcquireSpinLockExclusive(v_stack_mD8 + 288, 2, 512, 512);
loc_00698697:
    if ((((unsigned __int8)(1 + 62)) & ((unsigned __int8)(*(unsigned __int8 *)(v_stack_m100 + 12)))) != 0) goto loc_0069876D;
    a2 = (unsigned int)((0) + (1));
    a3 = (v_stack_m100 + 12) + (16);
    if (((unsigned int)(a2)) < 4) goto loc_00698697;
    if (((unsigned int)(a2)) != 4) goto loc_0069876D;
    v_stack_mE8 = v_stack_m100 + 8;
    v_stack_mF0 = 32;
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_stack_m100 + 12))) ^ (v_stack_m68));
    a1 = (unsigned __int16)((a1) & ((unsigned __int16)(1 + 62)));
    a1 = (unsigned __int16)((a1) ^ ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m100 + 12))));
    *(unsigned __int16 *)(v_stack_m100 + 12) = (unsigned __int16)(a1);
    a1 = (unsigned int)((a1) & ((unsigned int)(1 + 62)));
    *(unsigned __int16 *)(v_stack_m100 + 14) = 0;
    a2 = (v_stack_m78) - (*(unsigned __int16 *)(v_stack_m100 + 12));
    a2 = (a2) >> (4);
    a2 = (a2) * (*(unsigned __int16 *)(v_stack_m100 + 12));
    result = (a2) & (-512);
    a2 = (a2) - (result);
    *(unsigned __int64 *)(v_stack_m100) = result;
    a2 = (a2) >> (4);
    result = RtlSetBits(v_stack_mF0, a2, (unsigned int)((unsigned int)(a1)), v_stack_m100 + 12);
    if (v_stack_m68 <= 0) goto loc_0069876A;
loc_00698737:
    if ((unsigned int)(v_r15) != 0) goto loc_00698756;
    result = (*(unsigned __int64 *)(v_stack_m78 + 16)) & (-993);
    *(unsigned __int64 *)(v_stack_m78 + 16) = result;
    goto loc_0069875B;
loc_0069874F:
loc_00698756:
    result = MiSetOriginalPtePfnFromFreeList(3, a2, 0, v_stack_m100 + 12);
loc_0069875B:
    a3 = (unsigned int)((0) + (1));
    if (((unsigned int)((unsigned int)(a3))) < v_stack_m68) goto loc_00698737;
loc_0069876A:
loc_0069876D:
    result = MiReleaseSpinLockExclusive(v_stack_mD8 + 288, (unsigned __int8)((unsigned __int8)(result)), a3, v_stack_m100 + 12);
    if (0 != 0) {
        a3 = (unsigned int)(v_r15);
        a2 = v_stack_mA8;
        a1 = v_stack_mE0;
        result = MiFreeLargeZeroPages(a1, a2, a3, v_stack_m100 + 12);
    }
    result = 0;
loc_00698792:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, v_stack_m100 + 12);
    v_rsp = (v_rsp) + (288);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiAllocateLargeProcessPagesFromCache(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint8_t Arg5, void *Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m104;
    uint8_t v_stack_m108;
    uint64_t v_stack_m118;
    uint32_t v_stack_m120;
    uint64_t v_stack_m128;
    uint8_t v_stack_m130;
    uint32_t v_stack_m138;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint16_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint32_t v_stack_mF8;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (288);
    result = (*(uint64_t *)(v_rip + 0x772591)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_mF0 = Arg2;
    Arg2 = 0;
    v_stack_mB8 = Arg1;
    v_stack_m104 = (uint32_t)((uint32_t)(Arg4));
    result = memset(v_stack_mA8, Arg2, Arg2 + 96, Arg4);
    Arg4 = 0;
    v_stack_mD0 = 1;
    if (*(uint64_t *)(arg1) == 0) goto loc_00698217;
    result = MiGetVadCacheAttribute(*(uint64_t *)(arg1), 1, *(uint64_t *)(arg1), Arg4);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x30))) & ((uint32_t)((uint32_t)(0x1A00000ULL))));
    local_r15 = (((uint32_t)(Arg1)) == ((uint32_t)((uint32_t)(0x1A00000ULL)))) ? 1 : 0;
    goto loc_00698245;
loc_00698217:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14))))) >> (3));
    if (((uint32_t)(result)) != 3) goto loc_00698230;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14)))) & (7)) == 0) goto loc_00698237;
    goto loc_0069823A;
loc_00698230:
    local_r12 = 0;
    if (((uint32_t)(result)) != 1) {
        local_r12 = 1;
    }
    local_r15 = ((*(uint32_t *)(arg1 + 0x10)) != 0) ? 1 : 0;
loc_00698245:
    Arg3 = 0;
    local_r10 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x410)) + (768);
    v_stack_mD8 = local_r10;
    v_stack_mE0 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x797E29) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8);
    if (*(uint64_t *)(local_r10 + 0x118) != 0) goto loc_006982AD;
    result = MiCreateProcessLargePageCacheAnchor(*(uint64_t *)(*(uint64_t *)(v_rip + 0x797E29) + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x4AE) * 8), 1, Arg3, *(uint64_t *)(local_r10 + 0x118));
    Arg3 = 0;
    if (result == 0) goto loc_006985F1;
loc_006982AD:
    if ((uint32_t)((uint32_t)(Arg4)) != 0) goto loc_00698550;
    result = MiComputePreferredNode(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024, *(uint64_t *)(arg1), Arg3, result);
    Arg3 = 0;
loc_006982C7:
    *(uint32_t *)(result + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mE0 + 0x4058)));
    Arg4 = (result) + (32);
    local_rsi = (Arg3) >> (4);
    v_stack_mF4 = 63;
    result = ((int32_t)((uint32_t)(local_r12))) + ((uint32_t)((uint32_t)(result)) + (uint32_t)((uint32_t)(result)) * 2);
    result = (result) << (6);
    result = (result) + (Arg4);
    v_stack_m100 = result;
loc_00698308:
    if (((*(uint8_t *)(result + 0xC)) & (63)) != 0) goto loc_0069831F;
    Arg1 = (uint32_t)((0) + ((uint32_t)(63 - 62)));
    Arg2 = (result + 12) + (16);
    if (((uint32_t)(Arg1)) < 4) goto loc_00698308;
    if (((uint32_t)(Arg1)) == 4) goto loc_0069858A;
loc_0069831F:
    v_stack_mC0 = v_stack_mD8 + 288;
    result = ExAcquireSpinLockExclusive(v_stack_mD8 + 288, Arg2, Arg3, 63 - 62);
    v_stack_m108 = (uint8_t)(result);
    Arg2 = (v_stack_m100) + (12);
loc_00698358:
    if (((uint16_t)(*(uint16_t *)(Arg2 + 0x2))) != ((uint16_t)((uint32_t)(0xFFFFULL)))) {
        Arg1 = (uint16_t)((*(uint16_t *)(Arg2 + 0x2)) + ((uint16_t)(63 - 62)));
        *(uint16_t *)(Arg2 + 0x2) = (uint16_t)(Arg1);
    }
    Arg3 = (uint16_t)(((uint16_t)(*(uint16_t *)(Arg2))) & (63));
    local_r14 = 0;
    if (!(condition_is_not_equal)) {
        local_r14 = (uint32_t)((0) + ((uint32_t)(63 - 62)));
    }
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(Arg2))) & ((uint16_t)((uint32_t)(0xFFBFULL))));
    Arg1 = (uint16_t)((*(uint16_t *)(Arg2)) | (64));
    if ((uint16_t)(Arg3) != 0) { Arg1 = (uint16_t)(result); }
    *(uint16_t *)(Arg2) = (uint16_t)(Arg1);
    Arg2 = (Arg2) + (16);
    Arg4 = (63 - 59) - (1);
    if (condition_is_not_equal) goto loc_00698358;
    if (((uint32_t)(local_r14)) == 4) goto loc_006984C9;
    v_stack_mC8 = v_stack_m100 + 14;
loc_006983C0:
    Arg4 = (uint32_t)((Arg4) | (0xFFFFFFFFULL));
    Arg1 = 0;
loc_006983D1:
    if (((*(uint8_t *)(v_stack_m100 + 0xE - 0x2)) & (64)) != 0) goto loc_006983E7;
    if (((uint16_t)(*(uint16_t *)(v_stack_m100 + 0xE))) <= ((uint16_t)((uint32_t)(0xFFFFULL)))) {
        Arg3 = (uint16_t)(*(uint16_t *)(v_stack_m100 + 0xE));
        Arg4 = 0;
    }
    Arg2 = (uint32_t)((0) + (1));
    Arg1 = (v_stack_m100 + 14) + (16);
    if (((uint32_t)(Arg2)) < 4) goto loc_006983D1;
    local_r14 = (uint32_t)((local_r14) + (1));
    Arg2 = ((uint32_t)(Arg4)) << (4);
    Arg2 = (Arg2) + (v_stack_m100);
    local_r11 = (*(uint64_t *)(Arg2) + *(uint64_t *)(Arg2) * 2) << (4);
    local_r11 = (local_r11) + (*(uint64_t *)(Arg2));
    Arg3 = 0;
    *(uint16_t *)(Arg2 + 0xE) = 0;
loc_0069842C:
    if ((uint32_t)(*(uint32_t *)(Arg2 + 0x8)) == 0) goto loc_0069856C;
    v_stack_mF8 = (uint32_t)(*(uint64_t *)(Arg2));
    local_r10 = (uint32_t)(0xFFFFFFFFULL);
    if ((uint32_t)(*(uint32_t *)(Arg2 + 0x8)) != 0) { local_r10 = (uint32_t)((uint8_t)(*(uint64_t *)(Arg2))); }
    Arg3 = ((int8_t)((uint8_t)(local_r10)) + (int8_t)((uint8_t)(local_r10)) * 2) << (8);
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(Arg2 + 0xC))) - (v_stack_mD0));
    Arg3 = (Arg3) + (local_r11);
    Arg1 = (uint16_t)((Arg1) ^ ((uint16_t)(*(uint16_t *)(Arg2 + 0xC))));
    Arg1 = (uint16_t)((Arg1) & (v_stack_mF4));
    Arg1 = (uint16_t)((Arg1) ^ ((uint16_t)(*(uint16_t *)(Arg2 + 0xC))));
    *(uint16_t *)(Arg2 + 0xC) = (uint16_t)(Arg1);
    if ((*(uint64_t *)(*(uint64_t *)(arg6 + 0x30 + 0x8))) != (Arg6 + 48)) goto loc_0069874F;
    *(uint64_t *)(Arg3 + 0x8) = *(uint64_t *)(arg6 + 0x30 + 0x8);
    *(void **)(Arg3) = Arg6 + 48;
    *(uint64_t *)(*(uint64_t *)(arg6 + 0x30 + 0x8)) = Arg3;
    *(uint64_t *)(arg6 + 0x30 + 0x8) = Arg3;
    local_rdi = 0;
    if (((*(uint64_t *)(Arg3 + 0x10)) & (992)) != 0) {
        local_rdi = (uint32_t)((0) + (1));
    }
    result = (uint32_t)((1) << ((uint8_t)((uint8_t)(local_r10))));
    result = (uint32_t)(~(result));
    Arg4 = ((uint32_t)(*(uint32_t *)(Arg2 + 0x8))) & (result);
    *(uint32_t *)(Arg2 + 0x8) = Arg4;
    local_rsi = (local_rsi) - (1);
    if (condition_is_not_equal) goto loc_0069842C;
loc_006984C9:
    result = MiReleaseSpinLockExclusive(v_stack_mC0, v_stack_m108, 1, Arg4);
    result = 0;
    if ((uint32_t)(local_r15) != 0) goto loc_0069853E;
    if ((uint32_t)(local_rdi) == 0) goto loc_0069853E;
    if ((*(uint64_t *)(arg6 + 0x40)) <= 0) goto loc_0069853E;
    local_rbx = 0;
loc_006984F4:
    result = *(uint64_t *)(*(uint64_t *)(arg6 + 0x30) + 0x10);
    if (((*(uint64_t *)(*(uint64_t *)(arg6 + 0x30) + 0x10)) & (992)) != 0) {
        Arg4 = (uint32_t)(local_r12);
        v_stack_m138 = 0;
        Arg3 = 2;
        Arg2 = *(uint64_t *)(arg6 + 0x30);
        Arg1 = 0;
        result = MiZeroLargePage(Arg1, Arg2, Arg3, Arg4);
        result = *(uint64_t *)(*(uint64_t *)(arg6 + 0x30) + 0x10);
        Arg4 = 1;
        result = (result) & (-993);
        *(uint64_t *)(*(uint64_t *)(arg6 + 0x30) + 0x10) = result;
    }
    local_r14 = (uint32_t)((0) + (Arg4));
    if (((uint32_t)((uint32_t)(local_r14))) < (*(uint64_t *)(arg6 + 0x40))) goto loc_006984F4;
loc_0069853E:
    local_r12 = 0;
    if (local_rsi == 0) goto loc_00698790;
    goto loc_0069858D;
loc_00698550:
    if (((uint32_t)((uint32_t)(v_stack_m104) - 1)) < ((uint32_t)(*(uint16_t *)(v_rip + 0x92CAA9)))) goto loc_006982C7;
    goto loc_00698792;
loc_0069856C:
    if (((uint32_t)(v_stack_mB8)) == 4) goto loc_006984C9;
    goto loc_006983C0;
loc_0069858A:
    local_r12 = 0;
loc_0069858D:
    Arg2 = (v_stack_mF0) & (0xFFFFFFFFFFE00000ULL);
loc_006985A2:
    *(uint64_t *)(v_stack_mA8 + 0x10) = 0;
    *(uint64_t *)(v_stack_mA8 + 0x8) = v_stack_mA8;
    *(uint64_t *)(v_stack_mA8) = v_stack_mA8;
    result = (v_stack_mA8) + (24);
    Arg1 = (4) - (Arg4);
    if (condition_is_not_equal) goto loc_006985A2;
    v_stack_m118 = v_stack_mA8;
    v_stack_m120 = 8;
    v_stack_m128 = 0;
    v_stack_m130 = Arg5;
    v_stack_m138 = (uint32_t)((uint32_t)(v_stack_m104));
    result = MiCreateLargePfnList(v_stack_mB8, Arg2, 512, 512);
    if (!sign_flag) goto loc_006985FB;
loc_006985F1:
    goto loc_00698792;
loc_006985FB:
    result = MiReturnResident(v_stack_mE0, 512, 512, 512);
    local_rbx = (32) - (local_rsi);
    if (local_rsi == 0) goto loc_0069866B;
loc_0069861C:
    result = MiPopLargePfnList(v_stack_mA8, 2, 512, 512);
    Arg1 = (result + result * 2) << (4);
    Arg1 = (Arg1) + (result);
    if ((*(uint64_t *)(*(uint64_t *)(arg6 + 0x30 + 0x8))) != (Arg6 + 48)) goto loc_0069874F;
    *(uint64_t *)(arg1 + 0x8) = *(uint64_t *)(arg6 + 0x30 + 0x8);
    *(void **)(arg1) = Arg6 + 48;
    *(void **)(*(uint64_t *)(arg6 + 0x30 + 0x8)) = Arg1;
    *(void **)(arg6 + 0x30 + 0x8) = Arg1;
    local_rsi = (local_rsi) - (1);
    if (condition_is_not_equal) goto loc_0069861C;
loc_0069866B:
    result = ExAcquireSpinLockExclusive(v_stack_mD8 + 288, 2, 512, 512);
loc_00698697:
    if ((((uint8_t)(1 + 62)) & ((uint8_t)(*(uint8_t *)(v_stack_m100 + 0xC)))) != 0) goto loc_0069876D;
    Arg2 = (uint32_t)((0) + (1));
    Arg3 = (v_stack_m100 + 12) + (16);
    if (((uint32_t)(Arg2)) < 4) goto loc_00698697;
    if (((uint32_t)(Arg2)) != 4) goto loc_0069876D;
    v_stack_mE8 = v_stack_m100 + 8;
    v_stack_mF0 = 32;
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(v_stack_m100 + 0xC))) ^ (v_stack_m68));
    Arg1 = (uint16_t)((Arg1) & ((uint16_t)(1 + 62)));
    Arg1 = (uint16_t)((Arg1) ^ ((uint16_t)(*(uint16_t *)(v_stack_m100 + 0xC))));
    *(uint16_t *)(v_stack_m100 + 0xC) = (uint16_t)(Arg1);
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)(1 + 62)));
    *(uint16_t *)(v_stack_m100 + 0xE) = 0;
    Arg2 = (v_stack_m78) - (*(uint16_t *)(v_stack_m100 + 0xC));
    Arg2 = (Arg2) >> (4);
    Arg2 = (Arg2) * (*(uint16_t *)(v_stack_m100 + 0xC));
    result = (Arg2) & (-512);
    Arg2 = (Arg2) - (result);
    *(uint64_t *)(v_stack_m100) = result;
    Arg2 = (Arg2) >> (4);
    result = RtlSetBits(v_stack_mF0, Arg2, (uint32_t)((uint32_t)(Arg1)), v_stack_m100 + 12);
    if (v_stack_m68 <= 0) goto loc_0069876A;
loc_00698737:
    if ((uint32_t)(local_r15) != 0) goto loc_00698756;
    result = (*(uint64_t *)(v_stack_m78 + 0x10)) & (-993);
    *(uint64_t *)(v_stack_m78 + 0x10) = result;
    goto loc_0069875B;
loc_0069874F:
loc_00698756:
    result = MiSetOriginalPtePfnFromFreeList(3, Arg2, 0, v_stack_m100 + 12);
loc_0069875B:
    Arg3 = (uint32_t)((0) + (1));
    if (((uint32_t)((uint32_t)(Arg3))) < v_stack_m68) goto loc_00698737;
loc_0069876A:
loc_0069876D:
    result = MiReleaseSpinLockExclusive(v_stack_mD8 + 288, (uint8_t)((uint8_t)(result)), Arg3, v_stack_m100 + 12);
    if (0 != 0) {
        Arg3 = (uint32_t)(local_r15);
        Arg2 = v_stack_mA8;
        Arg1 = v_stack_mE0;
        result = MiFreeLargeZeroPages(Arg1, Arg2, Arg3, v_stack_m100 + 12);
    }
    result = 0;
loc_00698792:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, v_stack_m100 + 12);
    local_rsp = (local_rsp) + (288);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x14` | `32` | `R` |
| `Arg6` | `+ 0x8` | `64` | `R` |
| `Arg6` | `+ 0x8` | `64` | `W` |
| `Arg6` | `+ 0x30` | `64` | `R` |
| `Arg6` | `+ 0x40` | `64` | `R` |
| `Arg6` | `+ 0x40` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0069818C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
