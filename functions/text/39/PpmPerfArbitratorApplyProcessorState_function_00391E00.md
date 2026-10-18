# PpmPerfArbitratorApplyProcessorState

- RVA: `0x00391E00`–`0x00392427` (길이 `1,575` bytes)
- VA: `0x0000000140391E00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00080CA8`
- 디코드: `331`개 명령, `1,575/1,575` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00391F23` → [EtwEventEnabled](EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00391F39` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00391FD0` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00392188` → [KiIsQosGroupingClass](KiIsQosGroupingClass_function_00392430.md) (function, `0x00392430`)
- `0x003923B7` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)

### Direct callers
- [PpmPerfSetProcessorIdle](../2C/PpmPerfSetProcessorIdle_function_002CFD7C.md) at `0x002CFE72`
- [PpmPerfApplyProcessorState](../2D/PpmPerfApplyProcessorState_function_002DA4BC.md) at `0x002DA59C`
- [sub_00391990](Unknown_function_00391990.md) at `0x003919DB`
- [sub_00391C8E](Unknown_function_00391C8E.md) at `0x00391CD5`

### Static image references
- `0x00391E1C` → RVA `0x00E0A740` (`.data`; read)
- `0x00391E3E` → RVA `0x00FC6AA6` (`ALMOSTRO`; read)
- `0x00391EE8` → RVA `0x00011290` (`.rdata`; read)
- `0x00391F07` → RVA `0x00E67A39` (`.data`; read)
- `0x00391F19` → RVA `0x00F083E8` (`.data`; read)
- `0x00391FD5` → RVA `0x00FC6B40` (`ALMOSTRO`; read)
- `0x00392405` → RVA `0x00011340` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00391E00  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00391E05  55                              push rbp
00391E06  56                              push rsi
00391E07  57                              push rdi
00391E08  41 54                           push r12
00391E0A  41 55                           push r13
00391E0C  41 56                           push r14
00391E0E  41 57                           push r15
00391E10  48 8D 6C 24 90                  lea rbp, [rsp - 0x70]
00391E15  48 81 EC 70 01 00 00            sub rsp, 0x170
00391E1C  48 8B 05 1D 89 A7 00            mov rax, qword ptr [rip + 0xa7891d]
00391E23  48 33 C4                        xor rax, rsp
00391E26  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
00391E2A  4C 8B 91 B8 89 00 00            mov r10, qword ptr [rcx + 0x89b8]
00391E31  45 32 FF                        xor r15b, r15b
00391E34  48 8B 99 B0 89 00 00            mov rbx, qword ptr [rcx + 0x89b0]
00391E3B  45 33 F6                        xor r14d, r14d
00391E3E  44 38 35 61 4C C3 00            cmp byte ptr [rip + 0xc34c61], r14b
00391E45  48 8B F9                        mov rdi, rcx
00391E48  45 0F B6 E8                     movzx r13d, r8b
00391E4C  44 0F B6 E2                     movzx r12d, dl
00391E50  41 0F B6 C8                     movzx ecx, r8b
00391E54  0F 84 38 04 00 00               je 0x140392292
00391E5A  8B B7 40 8A 00 00               mov esi, dword ptr [rdi + 0x8a40]
00391E60  8B 93 24 03 00 00               mov edx, dword ptr [rbx + 0x324]
00391E66  3B B7 44 8A 00 00               cmp esi, dword ptr [rdi + 0x8a44]
00391E6C  0F 84 4F 05 00 00               je 0x1403923c1
00391E72  44 38 B3 EB 01 00 00            cmp byte ptr [rbx + 0x1eb], r14b
00391E79  74 12                           je 0x140391e8d
00391E7B  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00391E84  48 3B F8                        cmp rdi, rax
00391E87  0F 85 93 05 00 00               jne 0x140392420
00391E8D  0F B7 87 48 8A 00 00            movzx eax, word ptr [rdi + 0x8a48]
00391E94  0F A3 F0                        bt eax, esi
00391E97  0F 82 33 05 00 00               jb 0x1403923d0
00391E9D  B1 01                           mov cl, 1
00391E9F  41 89 52 78                     mov dword ptr [r10 + 0x78], edx
00391EA3  44 0F B6 E1                     movzx r12d, cl
00391EA7  89 B7 44 8A 00 00               mov dword ptr [rdi + 0x8a44], esi
00391EAD  41 B7 01                        mov r15b, 1
00391EB0  84 C9                           test cl, cl
00391EB2  0F 85 AE 00 00 00               jne 0x140391f66
00391EB8  45 84 FF                        test r15b, r15b
00391EBB  74 73                           je 0x140391f30
00391EBD  80 BF F4 89 00 00 00            cmp byte ptr [rdi + 0x89f4], 0
00391EC4  8B 87 44 8A 00 00               mov eax, dword ptr [rdi + 0x8a44]
00391ECA  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00391ECE  41 0F B6 C4                     movzx eax, r12b
00391ED2  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00391ED6  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
00391EDB  0F 84 1D 05 00 00               je 0x1403923fe
00391EE1  0F B6 87 D0 00 00 00            movzx eax, byte ptr [rdi + 0xd0]
00391EE8  48 8D 1D A1 F3 C7 FF            lea rbx, [rip - 0x380c5f]
00391EEF  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
00391EF4  0F B6 87 D1 00 00 00            movzx eax, byte ptr [rdi + 0xd1]
00391EFB  88 44 24 42                     mov byte ptr [rsp + 0x42], al
00391EFF  48 C7 45 A8 03 00 00 00         mov qword ptr [rbp - 0x58], 3
00391F07  80 3D 2B 5B AD 00 00            cmp byte ptr [rip + 0xad5b2b], 0
00391F0E  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00391F13  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00391F17  74 17                           je 0x140391f30
00391F19  48 8B 0D C8 64 B7 00            mov rcx, qword ptr [rip + 0xb764c8]
00391F20  48 8B D3                        mov rdx, rbx
00391F23  E8 28 05 00 00                  call 0x140392450
00391F28  84 C0                           test al, al
00391F2A  0F 85 6A 03 00 00               jne 0x14039229a
00391F30  B0 01                           mov al, 1
00391F32  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
00391F36  48 33 CC                        xor rcx, rsp
00391F39  E8 02 A7 31 00                  call 0x1406ac640
00391F3E  48 8B 9C 24 C8 01 00 00         mov rbx, qword ptr [rsp + 0x1c8]
00391F46  48 81 C4 70 01 00 00            add rsp, 0x170
00391F4D  41 5F                           pop r15
00391F4F  41 5E                           pop r14
00391F51  41 5D                           pop r13
00391F53  41 5C                           pop r12
00391F55  5F                              pop rdi
00391F56  5E                              pop rsi
00391F57  5D                              pop rbp
00391F58  C3                              ret
00391F59  CC                              int3
00391F5A  85 F6                           test esi, esi
00391F5C  0F 85 7D 04 00 00               jne 0x1403923df
00391F62  41 89 52 78                     mov dword ptr [r10 + 0x78], edx
00391F66  45 84 ED                        test r13b, r13b
00391F69  74 04                           je 0x140391f6f
00391F6B  45 89 72 78                     mov dword ptr [r10 + 0x78], r14d
00391F6F  41 8B 42 50                     mov eax, dword ptr [r10 + 0x50]
00391F73  49 8D 52 40                     lea rdx, [r10 + 0x40]
00391F77  41 89 82 80 00 00 00            mov dword ptr [r10 + 0x80], eax
00391F7E  45 0F B6 CD                     movzx r9d, r13b
00391F82  8B 42 14                        mov eax, dword ptr [rdx + 0x14]
00391F85  45 0F B6 C4                     movzx r8d, r12b
00391F89  41 89 42 7C                     mov dword ptr [r10 + 0x7c], eax
00391F8D  4C 63 F6                        movsxd r14, esi
00391F90  49 6B C6 38                     imul rax, r14, 0x38
00391F94  0F 10 84 18 28 03 00 00         movups xmm0, xmmword ptr [rax + rbx + 0x328]
00391F9C  0F 11 02                        movups xmmword ptr [rdx], xmm0
00391F9F  0F 10 8C 18 38 03 00 00         movups xmm1, xmmword ptr [rax + rbx + 0x338]
00391FA7  0F 11 4A 10                     movups xmmword ptr [rdx + 0x10], xmm1
00391FAB  0F 10 84 18 48 03 00 00         movups xmm0, xmmword ptr [rax + rbx + 0x348]
00391FB3  0F 11 42 20                     movups xmmword ptr [rdx + 0x20], xmm0
00391FB7  F2 0F 10 8C 18 58 03 00 00      movsd xmm1, qword ptr [rax + rbx + 0x358]
00391FC0  F2 0F 11 4A 30                  movsd qword ptr [rdx + 0x30], xmm1
00391FC5  48 8B 83 88 01 00 00            mov rax, qword ptr [rbx + 0x188]
00391FCC  49 8B 4A 08                     mov rcx, qword ptr [r10 + 8]
00391FD0  E8 FB 8A 32 00                  call 0x1406baad0
00391FD5  83 3D 64 4B C3 00 00            cmp dword ptr [rip + 0xc34b64], 0
00391FDC  0F 84 91 01 00 00               je 0x140392173
00391FE2  42 0F B7 84 73 14 03 00 00      movzx eax, word ptr [rbx + r14*2 + 0x314]
00391FEB  0F B7 97 48 8A 00 00            movzx edx, word ptr [rdi + 0x8a48]
00391FF2  66 3B C2                        cmp ax, dx
00391FF5  0F 84 78 01 00 00               je 0x140392173
00391FFB  44 0F B7 C0                     movzx r8d, ax
00391FFF  66 89 87 48 8A 00 00            mov word ptr [rdi + 0x8a48], ax
00392006  48 8B 9F C0 00 00 00            mov rbx, qword ptr [rdi + 0xc0]
0039200D  0F B7 CA                        movzx ecx, dx
00392010  66 41 83 E0 01                  and r8w, 1
00392015  66 83 E1 01                     and cx, 1
00392019  66 44 3B C1                     cmp r8w, cx
0039201D  74 1A                           je 0x140392039
0039201F  0F B6 8F D1 00 00 00            movzx ecx, byte ptr [rdi + 0xd1]
00392026  66 45 85 C0                     test r8w, r8w
0039202A  0F 85 D5 01 00 00               jne 0x140392205
00392030  F0 48 0F B3 8B 00 01 00 00      lock btr qword ptr [rbx + 0x100], rcx
00392039  66 D1 E8                        shr ax, 1
0039203C  66 D1 EA                        shr dx, 1
0039203F  44 0F B7 C0                     movzx r8d, ax
00392043  0F B7 CA                        movzx ecx, dx
00392046  66 41 83 E0 01                  and r8w, 1
0039204B  66 83 E1 01                     and cx, 1
0039204F  66 44 3B C1                     cmp r8w, cx
00392053  74 1A                           je 0x14039206f
00392055  0F B6 8F D1 00 00 00            movzx ecx, byte ptr [rdi + 0xd1]
0039205C  66 45 85 C0                     test r8w, r8w
00392060  0F 85 AD 01 00 00               jne 0x140392213
00392066  F0 48 0F B3 8B 08 01 00 00      lock btr qword ptr [rbx + 0x108], rcx
0039206F  66 D1 E8                        shr ax, 1
00392072  66 D1 EA                        shr dx, 1
00392075  44 0F B7 C0                     movzx r8d, ax
00392079  0F B7 CA                        movzx ecx, dx
0039207C  66 41 83 E0 01                  and r8w, 1
00392081  66 83 E1 01                     and cx, 1
00392085  66 44 3B C1                     cmp r8w, cx
00392089  74 1A                           je 0x1403920a5
0039208B  0F B6 8F D1 00 00 00            movzx ecx, byte ptr [rdi + 0xd1]
00392092  66 45 85 C0                     test r8w, r8w
00392096  0F 85 85 01 00 00               jne 0x140392221
0039209C  F0 48 0F B3 8B 10 01 00 00      lock btr qword ptr [rbx + 0x110], rcx
003920A5  66 D1 E8                        shr ax, 1
003920A8  66 D1 EA                        shr dx, 1
003920AB  44 0F B7 C0                     movzx r8d, ax
003920AF  0F B7 CA                        movzx ecx, dx
003920B2  66 41 83 E0 01                  and r8w, 1
003920B7  66 83 E1 01                     and cx, 1
003920BB  66 44 3B C1                     cmp r8w, cx
003920BF  74 1A                           je 0x1403920db
003920C1  0F B6 8F D1 00 00 00            movzx ecx, byte ptr [rdi + 0xd1]
003920C8  66 45 85 C0                     test r8w, r8w
003920CC  0F 85 5D 01 00 00               jne 0x14039222f
003920D2  F0 48 0F B3 8B 18 01 00 00      lock btr qword ptr [rbx + 0x118], rcx
003920DB  66 D1 E8                        shr ax, 1
003920DE  66 D1 EA                        shr dx, 1
003920E1  44 0F B7 C0                     movzx r8d, ax
003920E5  0F B7 CA                        movzx ecx, dx
003920E8  66 41 83 E0 01                  and r8w, 1
003920ED  66 83 E1 01                     and cx, 1
003920F1  66 44 3B C1                     cmp r8w, cx
003920F5  74 1A                           je 0x140392111
003920F7  0F B6 8F D1 00 00 00            movzx ecx, byte ptr [rdi + 0xd1]
003920FE  66 45 85 C0                     test r8w, r8w
00392102  0F 85 35 01 00 00               jne 0x14039223d
00392108  F0 48 0F B3 8B 20 01 00 00      lock btr qword ptr [rbx + 0x120], rcx
00392111  66 D1 E8                        shr ax, 1
00392114  66 D1 EA                        shr dx, 1
00392117  44 0F B7 C0                     movzx r8d, ax
0039211B  0F B7 CA                        movzx ecx, dx
0039211E  66 41 83 E0 01                  and r8w, 1
00392123  66 83 E1 01                     and cx, 1
00392127  66 44 3B C1                     cmp r8w, cx
0039212B  74 1A                           je 0x140392147
0039212D  0F B6 8F D1 00 00 00            movzx ecx, byte ptr [rdi + 0xd1]
00392134  66 45 85 C0                     test r8w, r8w
00392138  0F 85 0D 01 00 00               jne 0x14039224b
0039213E  F0 48 0F B3 8B 28 01 00 00      lock btr qword ptr [rbx + 0x128], rcx
00392147  66 D1 E8                        shr ax, 1
0039214A  66 D1 EA                        shr dx, 1
0039214D  66 83 E0 01                     and ax, 1
00392151  66 83 E2 01                     and dx, 1
00392155  66 3B C2                        cmp ax, dx
00392158  74 19                           je 0x140392173
0039215A  0F B6 8F D1 00 00 00            movzx ecx, byte ptr [rdi + 0xd1]
00392161  66 85 C0                        test ax, ax
00392164  0F 85 EF 00 00 00               jne 0x140392259
0039216A  F0 48 0F B3 8B 30 01 00 00      lock btr qword ptr [rbx + 0x130], rcx
00392173  48 8B 87 C0 00 00 00            mov rax, qword ptr [rdi + 0xc0]
0039217A  8B CE                           mov ecx, esi
0039217C  0F 10 88 40 01 00 00            movups xmm1, xmmword ptr [rax + 0x140]
00392183  0F 29 4C 24 70                  movaps xmmword ptr [rsp + 0x70], xmm1
00392188  E8 A3 02 00 00                  call 0x140392430
0039218D  66 0F 6F C1                     movdqa xmm0, xmm1
00392191  44 0F B6 D8                     movzx r11d, al
00392195  66 0F 73 D8 08                  psrldq xmm0, 8
0039219A  66 49 0F 7E C9                  movq r9, xmm1
0039219F  66 49 0F 7E C2                  movq r10, xmm0
003921A4  48 8B 9F C8 00 00 00            mov rbx, qword ptr [rdi + 0xc8]
003921AB  48 8B 97 60 8E 00 00            mov rdx, qword ptr [rdi + 0x8e60]
003921B2  66 0F 7F 4C 24 60               movdqa xmmword ptr [rsp + 0x60], xmm1
003921B8  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
003921BD  45 84 DB                        test r11b, r11b
003921C0  0F 85 A1 00 00 00               jne 0x140392267
003921C6  48 F7 D3                        not rbx
003921C9  48 F7 D2                        not rdx
003921CC  49 23 D9                        and rbx, r9
003921CF  48 23 CA                        and rcx, rdx
003921D2  4C 8B 87 C0 00 00 00            mov r8, qword ptr [rdi + 0xc0]
003921D9  49 8B C1                        mov rax, r9
003921DC  49 8B D2                        mov rdx, r10
003921DF  F0 49 0F C7 88 40 01 00 00      lock cmpxchg16b xmmword ptr [r8 + 0x140]
003921E8  4C 8B C8                        mov r9, rax
003921EB  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
003921F0  4C 8B D2                        mov r10, rdx
003921F3  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
003921F8  0F 84 83 00 00 00               je 0x140392281
003921FE  0F 28 4C 24 70                  movaps xmm1, xmmword ptr [rsp + 0x70]
00392203  EB 9F                           jmp 0x1403921a4
00392205  F0 48 0F AB 8B 00 01 00 00      lock bts qword ptr [rbx + 0x100], rcx
0039220E  E9 26 FE FF FF                  jmp 0x140392039
00392213  F0 48 0F AB 8B 08 01 00 00      lock bts qword ptr [rbx + 0x108], rcx
0039221C  E9 4E FE FF FF                  jmp 0x14039206f
00392221  F0 48 0F AB 8B 10 01 00 00      lock bts qword ptr [rbx + 0x110], rcx
0039222A  E9 76 FE FF FF                  jmp 0x1403920a5
0039222F  F0 48 0F AB 8B 18 01 00 00      lock bts qword ptr [rbx + 0x118], rcx
00392238  E9 9E FE FF FF                  jmp 0x1403920db
0039223D  F0 48 0F AB 8B 20 01 00 00      lock bts qword ptr [rbx + 0x120], rcx
00392246  E9 C6 FE FF FF                  jmp 0x140392111
0039224B  F0 48 0F AB 8B 28 01 00 00      lock bts qword ptr [rbx + 0x128], rcx
00392254  E9 EE FE FF FF                  jmp 0x140392147
00392259  F0 48 0F AB 8B 30 01 00 00      lock bts qword ptr [rbx + 0x130], rcx
00392262  E9 0C FF FF FF                  jmp 0x140392173
00392267  49 0B D9                        or rbx, r9
0039226A  48 8B C2                        mov rax, rdx
0039226D  48 23 C3                        and rax, rbx
00392270  48 3B C2                        cmp rax, rdx
00392273  0F 85 59 FF FF FF               jne 0x1403921d2
00392279  48 0B CA                        or rcx, rdx
0039227C  E9 51 FF FF FF                  jmp 0x1403921d2
00392281  45 33 F6                        xor r14d, r14d
00392284  45 84 ED                        test r13b, r13b
00392287  0F 85 2B FC FF FF               jne 0x140391eb8
0039228D  E9 2B FC FF FF                  jmp 0x140391ebd
00392292  41 8B F6                        mov esi, r14d
00392295  E9 C6 FB FF FF                  jmp 0x140391e60
0039229A  48 8B 8F B8 89 00 00            mov rcx, qword ptr [rdi + 0x89b8]
003922A1  45 33 C9                        xor r9d, r9d
003922A4  45 33 C0                        xor r8d, r8d
003922A7  48 8B D3                        mov rdx, rbx
003922AA  8B 41 40                        mov eax, dword ptr [rcx + 0x40]
003922AD  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
003922B1  8B 41 54                        mov eax, dword ptr [rcx + 0x54]
003922B4  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
003922B8  48 8D 44 24 44                  lea rax, [rsp + 0x44]
003922BD  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
003922C1  48 8D 44 24 48                  lea rax, [rsp + 0x48]
003922C6  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
003922CA  48 8D 41 50                     lea rax, [rcx + 0x50]
003922CE  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
003922D2  48 8D 41 60                     lea rax, [rcx + 0x60]
003922D6  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
003922DA  48 8D 41 58                     lea rax, [rcx + 0x58]
003922DE  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
003922E2  48 8D 41 5C                     lea rax, [rcx + 0x5c]
003922E6  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
003922EA  48 8D 41 64                     lea rax, [rcx + 0x64]
003922EE  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
003922F2  48 8D 41 68                     lea rax, [rcx + 0x68]
003922F6  48 89 45 00                     mov qword ptr [rbp], rax
003922FA  48 C7 45 88 04 00 00 00         mov qword ptr [rbp - 0x78], 4
00392302  48 C7 45 98 04 00 00 00         mov qword ptr [rbp - 0x68], 4
0039230A  48 C7 45 B8 04 00 00 00         mov qword ptr [rbp - 0x48], 4
00392312  48 C7 45 C8 04 00 00 00         mov qword ptr [rbp - 0x38], 4
0039231A  48 C7 45 D8 04 00 00 00         mov qword ptr [rbp - 0x28], 4
00392322  48 C7 45 E8 04 00 00 00         mov qword ptr [rbp - 0x18], 4
0039232A  48 C7 45 F8 04 00 00 00         mov qword ptr [rbp - 8], 4
00392332  48 C7 45 08 04 00 00 00         mov qword ptr [rbp + 8], 4
0039233A  0F B6 41 70                     movzx eax, byte ptr [rcx + 0x70]
0039233E  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
00392342  48 8D 44 24 4C                  lea rax, [rsp + 0x4c]
00392347  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
0039234B  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00392350  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
00392354  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00392359  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
0039235D  48 8D 41 48                     lea rax, [rcx + 0x48]
00392361  48 83 C1 6C                     add rcx, 0x6c
00392365  48 C7 45 18 04 00 00 00         mov qword ptr [rbp + 0x18], 4
0039236D  48 89 4D 50                     mov qword ptr [rbp + 0x50], rcx
00392371  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00392375  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0039237A  48 8B 0D 67 60 B7 00            mov rcx, qword ptr [rip + 0xb76067]
00392381  C7 44 24 30 0E 00 00 00         mov dword ptr [rsp + 0x30], 0xe
00392389  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
0039238E  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00392393  48 C7 45 28 04 00 00 00         mov qword ptr [rbp + 0x28], 4
0039239B  48 C7 45 38 04 00 00 00         mov qword ptr [rbp + 0x38], 4
003923A3  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
003923A7  48 C7 45 48 08 00 00 00         mov qword ptr [rbp + 0x48], 8
003923AF  48 C7 45 58 04 00 00 00         mov qword ptr [rbp + 0x58], 4
003923B7  E8 14 CD EC FF                  call 0x14025f0d0
003923BC  E9 6F FB FF FF                  jmp 0x140391f30
003923C1  41 39 52 78                     cmp dword ptr [r10 + 0x78], edx
003923C5  0F 84 E5 FA FF FF               je 0x140391eb0
003923CB  E9 8A FB FF FF                  jmp 0x140391f5a
003923D0  41 39 52 78                     cmp dword ptr [r10 + 0x78], edx
003923D4  0F 84 CD FA FF FF               je 0x140391ea7
003923DA  E9 BE FA FF FF                  jmp 0x140391e9d
003923DF  44 38 B3 EB 01 00 00            cmp byte ptr [rbx + 0x1eb], r14b
003923E6  74 0E                           je 0x1403923f6
003923E8  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
003923F1  48 3B F8                        cmp rdi, rax
003923F4  75 2A                           jne 0x140392420
003923F6  41 B4 01                        mov r12b, 1
003923F9  E9 64 FB FF FF                  jmp 0x140391f62
003923FE  48 8B 87 B8 89 00 00            mov rax, qword ptr [rdi + 0x89b8]
00392405  48 8D 1D 34 EF C7 FF            lea rbx, [rip - 0x3810cc]
0039240C  8B 48 14                        mov ecx, dword ptr [rax + 0x14]
0039240F  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00392413  48 C7 45 A8 04 00 00 00         mov qword ptr [rbp - 0x58], 4
0039241B  E9 E7 FA FF FF                  jmp 0x140391f07
00392420  32 C0                           xor al, al
00392422  E9 0B FB FF FF                  jmp 0x140391f32
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmPerfArbitratorApplyProcessorState(__int64 a1, unsigned __int8 a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m150;
    unsigned int v_stack_m158;
    unsigned __int8 v_stack_m166;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned int v_stack_p44;
    unsigned int v_stack_p48;
    unsigned int v_stack_p4C;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (368);
    result = (*(unsigned __int64 *)(v_rip + 10979613)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r15 = 0;
    v_r14 = 0;
    if ((*(unsigned __int8 *)(v_rip + 12799073)) == 0) goto loc_00392292;
loc_00391E60:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 35392)))) == (*(unsigned int *)(a1 + 35396))) goto loc_003923C1;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 35248) + 491)) == 0) goto loc_00391E8D;
    if (a1 != (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_00392420;
loc_00391E8D:
    if (a1 < (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_003923D0;
loc_00391E9D:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 35256) + 120) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35248) + 804)));
loc_00391EA7:
    *(unsigned int *)(a1 + 35396) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 35392)));
loc_00391EB0:
    if (1 != 0) goto loc_00391F66;
loc_00391EB8:
    if (1 == 0) goto loc_00391F30;
loc_00391EBD:
    v_stack_m150 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 35396)));
    v_stack_m158 = 1;
    v_stack_m168 = 0;
    if ((*(unsigned __int8 *)(a1 + 35316)) == 0) goto loc_003923FE;
    v_stack_m168 = (unsigned __int16)(*(unsigned __int8 *)(a1 + 208));
    v_stack_m166 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 209));
    v_stack_m100 = 3;
loc_00391F07:
    v_stack_m108 = v_stack_m168;
    if ((*(unsigned __int8 *)(v_rip + 11361067)) == 0) goto loc_00391F30;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 12018888), v_rip - 3673183, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0039229A;
loc_00391F30:
loc_00391F32:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip - 3673183, a3, a4);
    v_rsp = (v_rsp) + (368);
    return result;
loc_00391F5A:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 35392))) != 0) goto loc_003923DF;
loc_00391F62:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 35256) + 120) = (unsigned int)(v_rip - 3673183);
loc_00391F66:
    if (a3 != 0) {
        *(unsigned int *)(*(unsigned __int64 *)(a1 + 35256) + 120) = 0;
    }
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 35256) + 128) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35256) + 80)));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 35256) + 124) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35256) + 64 + 20)));
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35256) + 64 + 20))) * ((int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 35392)))));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35256) + 64) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35256) + 64 + 16) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35256) + 64 + 32) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35256) + 64 + 48) = v_xmm1;
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 35256) + 8), *(unsigned __int64 *)(a1 + 35256) + 64, 1, a3);
    if ((*(unsigned int *)(v_rip + 12798820)) == 0) goto loc_00392173;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_p20 + (int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 35392)))) * 2 + 788))) == ((unsigned __int16)(*(unsigned __int16 *)(a1 + 35400)))) goto loc_00392173;
    *(unsigned __int16 *)(a1 + 35400) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_p20 + (int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 35392)))) * 2 + 788));
    a3 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_stack_p20 + (int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 35392)))) * 2 + 788))) & (1));
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a1 + 35400))) & (1));
    if (a3 == ((unsigned __int16)(a1))) goto loc_00392039;
    if (a3 != 0) goto loc_00392205;
loc_00392039:
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_p20 + (int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 35392)))) * 2 + 788)) >> (1));
    a2 = (unsigned __int16)((*(unsigned __int16 *)(a1 + 35400)) >> (1));
    a3 = (unsigned __int16)(((unsigned __int16)(result)) & (1));
    a1 = (unsigned __int16)((a2) & (1));
    if (a3 == ((unsigned __int16)(a1))) goto loc_0039206F;
    if (a3 != 0) goto loc_00392213;
loc_0039206F:
    result = (unsigned __int16)((result) >> (1));
    a2 = (unsigned __int16)((a2) >> (1));
    a3 = (unsigned __int16)(((unsigned __int16)(result)) & (1));
    a1 = (unsigned __int16)((a2) & (1));
    if (a3 == ((unsigned __int16)(a1))) goto loc_003920A5;
    if (a3 != 0) goto loc_00392221;
loc_003920A5:
    result = (unsigned __int16)((result) >> (1));
    a2 = (unsigned __int16)((a2) >> (1));
    a3 = (unsigned __int16)(((unsigned __int16)(result)) & (1));
    a1 = (unsigned __int16)((a2) & (1));
    if (a3 == ((unsigned __int16)(a1))) goto loc_003920DB;
    if (a3 != 0) goto loc_0039222F;
loc_003920DB:
    result = (unsigned __int16)((result) >> (1));
    a2 = (unsigned __int16)((a2) >> (1));
    a3 = (unsigned __int16)(((unsigned __int16)(result)) & (1));
    a1 = (unsigned __int16)((a2) & (1));
    if (a3 == ((unsigned __int16)(a1))) goto loc_00392111;
    if (a3 != 0) goto loc_0039223D;
loc_00392111:
    result = (unsigned __int16)((result) >> (1));
    a2 = (unsigned __int16)((a2) >> (1));
    a3 = (unsigned __int16)(((unsigned __int16)(result)) & (1));
    a1 = (unsigned __int16)((a2) & (1));
    if (a3 == ((unsigned __int16)(a1))) goto loc_00392147;
    if (a3 != 0) goto loc_0039224B;
loc_00392147:
    result = (unsigned __int16)((result) >> (1));
    a2 = (unsigned __int16)((a2) >> (1));
    result = (unsigned __int16)((result) & (1));
    a2 = (unsigned __int16)((a2) & (1));
    if (((unsigned __int16)(result)) == a2) goto loc_00392173;
    if ((unsigned __int16)(result) != 0) goto loc_00392259;
loc_00392173:
    v_stack_p70 = v_xmm1;
    result = KiIsQosGroupingClass((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 35392)))), a2, a3, a3);
loc_003921A4:
    v_stack_p60 = v_xmm1;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_00392267;
    v_rbx = ~(*(unsigned __int64 *)(a1 + 200));
    a2 = ~(*(unsigned __int64 *)(a1 + 36448));
    v_rbx = (v_rbx) & (a3);
    a1 = (v_stack_p68) & (a2);
loc_003921D2:
    v_stack_p70 = a3;
    v_stack_p78 = *(unsigned __int64 *)(a1 + 35256);
    if (condition_is_equal) goto loc_00392281;
    goto loc_003921A4;
loc_00392205:
    goto loc_00392039;
loc_00392213:
    goto loc_0039206F;
loc_00392221:
    goto loc_003920A5;
loc_0039222F:
    goto loc_003920DB;
loc_0039223D:
    goto loc_00392111;
loc_0039224B:
    goto loc_00392147;
loc_00392259:
    goto loc_00392173;
loc_00392267:
    v_rbx = (v_rbx) | (a3);
    result = (*(unsigned __int64 *)(a1 + 35256)) & (v_rbx);
    if (result != (*(unsigned __int64 *)(a1 + 35256))) goto loc_003921D2;
    a1 = (a1) | (*(unsigned __int64 *)(a1 + 35256));
    goto loc_003921D2;
loc_00392281:
    v_r14 = 0;
    if (a3 != 0) goto loc_00391EB8;
    goto loc_00391EBD;
loc_00392292:
    goto loc_00391E60;
loc_0039229A:
    a4 = 0;
    a3 = 0;
    v_stack_p44 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35256) + 64)));
    v_stack_p48 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35256) + 84)));
    v_stack_m128 = v_stack_p44;
    v_stack_m118 = v_stack_p48;
    v_stack_mF8 = *(unsigned __int64 *)(a1 + 35256) + 80;
    v_stack_mE8 = *(unsigned __int64 *)(a1 + 35256) + 96;
    v_stack_mD8 = *(unsigned __int64 *)(a1 + 35256) + 88;
    v_stack_mC8 = *(unsigned __int64 *)(a1 + 35256) + 92;
    v_stack_mB8 = *(unsigned __int64 *)(a1 + 35256) + 100;
    v_stack_mA8 = *(unsigned __int64 *)(a1 + 35256) + 104;
    v_stack_m120 = 4;
    v_stack_m110 = 4;
    v_stack_mF0 = 4;
    v_stack_mE0 = 4;
    v_stack_mD0 = 4;
    v_stack_mC0 = 4;
    v_stack_mB0 = 4;
    v_stack_mA0 = 4;
    v_stack_p4C = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 35256) + 112));
    v_stack_m98 = v_stack_p4C;
    v_stack_m88 = v_stack_p50;
    v_stack_m78 = v_stack_p58;
    a1 = (*(unsigned __int64 *)(a1 + 35256)) + (108);
    v_stack_m90 = 4;
    v_stack_m58 = a1;
    v_stack_p38 = v_stack_m128;
    v_stack_p30 = 14;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    v_stack_m80 = 4;
    v_stack_m70 = 4;
    v_stack_m68 = *(unsigned __int64 *)(a1 + 35256) + 72;
    v_stack_m60 = 8;
    v_stack_m50 = 4;
    result = EtwWriteEx(*(unsigned __int64 *)(v_rip + 12017767), v_rbx, a3, a4);
    goto loc_00391F30;
loc_003923C1:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 35256) + 120)) == ((unsigned int)(v_rbx))) goto loc_00391EB0;
    goto loc_00391F5A;
loc_003923D0:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 35256) + 120)) == ((unsigned int)(v_rbx))) goto loc_00391EA7;
    goto loc_00391E9D;
loc_003923DF:
    if ((*(unsigned __int8 *)(v_rbx + 491)) == 0) goto loc_003923F6;
    if (a1 != (*(unsigned __int64 *)(gs_base + (0 + 32)))) goto loc_00392420;
loc_003923F6:
    goto loc_00391F62;
loc_003923FE:
    v_stack_p40 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 35256) + 20)));
    v_stack_m100 = 4;
    goto loc_00391F07;
loc_00392420:
    result = 0;
    goto loc_00391F32;
}
```

## 5. (Beta) C Style

```c
int64_t PpmPerfArbitratorApplyProcessorState(void *Arg1, uint8_t Arg2, uint8_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m150;
    uint32_t v_stack_m158;
    uint8_t v_stack_m166;
    uint32_t v_stack_m168;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint32_t v_stack_p44;
    uint32_t v_stack_p48;
    uint32_t v_stack_p4C;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (368);
    result = (*(uint64_t *)(v_rip + 0xA7891D)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r15 = 0;
    local_r14 = 0;
    if ((*(uint8_t *)(v_rip + 0xC34C61)) == 0) goto loc_00392292;
loc_00391E60:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8A40)))) == (*(uint32_t *)(arg1 + 0x8A44))) goto loc_003923C1;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x89B0) + 0x1EB)) == 0) goto loc_00391E8D;
    if (Arg1 != (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_00392420;
loc_00391E8D:
    if (Arg1 < (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_003923D0;
loc_00391E9D:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x78) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B0) + 0x324)));
loc_00391EA7:
    *(uint32_t *)(arg1 + 0x8A44) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8A40)));
loc_00391EB0:
    if (1 != 0) goto loc_00391F66;
loc_00391EB8:
    if (1 == 0) goto loc_00391F30;
loc_00391EBD:
    v_stack_m150 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8A44)));
    v_stack_m158 = 1;
    v_stack_m168 = 0;
    if ((*(uint8_t *)(arg1 + 0x89F4)) == 0) goto loc_003923FE;
    v_stack_m168 = (uint16_t)(*(uint8_t *)(arg1 + 0xD0));
    v_stack_m166 = (uint8_t)(*(uint8_t *)(arg1 + 0xD1));
    v_stack_m100 = 3;
loc_00391F07:
    v_stack_m108 = v_stack_m168;
    if ((*(uint8_t *)(v_rip + 0xAD5B2B)) == 0) goto loc_00391F30;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xB764C8), v_rip - 3673183, Arg3, a4);
    if ((uint8_t)(result) != 0) goto loc_0039229A;
loc_00391F30:
loc_00391F32:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip - 3673183, Arg3, a4);
    local_rsp = (local_rsp) + (368);
    return result;
loc_00391F5A:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8A40))) != 0) goto loc_003923DF;
loc_00391F62:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x78) = (uint32_t)(v_rip - 3673183);
loc_00391F66:
    if (Arg3 != 0) {
        *(uint32_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x78) = 0;
    }
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x80) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x50)));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x7C) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x40 + 0x14)));
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x40 + 0x14))) * ((int32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8A40)))));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x40) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x40 + 0x10) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x40 + 0x20) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x40 + 0x30) = v_xmm1;
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x8), *(uint64_t *)(arg1 + 0x89B8) + 64, 1, Arg3);
    if ((*(uint32_t *)(v_rip + 0xC34B64)) == 0) goto loc_00392173;
    if (((uint16_t)(*(uint16_t *)(v_stack_p20 + (int32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8A40)))) * 2 + 0x314))) == ((uint16_t)(*(uint16_t *)(arg1 + 0x8A48)))) goto loc_00392173;
    *(uint16_t *)(arg1 + 0x8A48) = (uint16_t)(*(uint16_t *)(v_stack_p20 + (int32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8A40)))) * 2 + 0x314));
    Arg3 = (uint16_t)(((uint16_t)(*(uint16_t *)(v_stack_p20 + (int32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8A40)))) * 2 + 0x314))) & (1));
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(arg1 + 0x8A48))) & (1));
    if (Arg3 == ((uint16_t)(Arg1))) goto loc_00392039;
    if (Arg3 != 0) goto loc_00392205;
loc_00392039:
    result = (uint16_t)((*(uint16_t *)(v_stack_p20 + (int32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8A40)))) * 2 + 0x314)) >> (1));
    Arg2 = (uint16_t)((*(uint16_t *)(arg1 + 0x8A48)) >> (1));
    Arg3 = (uint16_t)(((uint16_t)(result)) & (1));
    Arg1 = (uint16_t)((Arg2) & (1));
    if (Arg3 == ((uint16_t)(Arg1))) goto loc_0039206F;
    if (Arg3 != 0) goto loc_00392213;
loc_0039206F:
    result = (uint16_t)((result) >> (1));
    Arg2 = (uint16_t)((Arg2) >> (1));
    Arg3 = (uint16_t)(((uint16_t)(result)) & (1));
    Arg1 = (uint16_t)((Arg2) & (1));
    if (Arg3 == ((uint16_t)(Arg1))) goto loc_003920A5;
    if (Arg3 != 0) goto loc_00392221;
loc_003920A5:
    result = (uint16_t)((result) >> (1));
    Arg2 = (uint16_t)((Arg2) >> (1));
    Arg3 = (uint16_t)(((uint16_t)(result)) & (1));
    Arg1 = (uint16_t)((Arg2) & (1));
    if (Arg3 == ((uint16_t)(Arg1))) goto loc_003920DB;
    if (Arg3 != 0) goto loc_0039222F;
loc_003920DB:
    result = (uint16_t)((result) >> (1));
    Arg2 = (uint16_t)((Arg2) >> (1));
    Arg3 = (uint16_t)(((uint16_t)(result)) & (1));
    Arg1 = (uint16_t)((Arg2) & (1));
    if (Arg3 == ((uint16_t)(Arg1))) goto loc_00392111;
    if (Arg3 != 0) goto loc_0039223D;
loc_00392111:
    result = (uint16_t)((result) >> (1));
    Arg2 = (uint16_t)((Arg2) >> (1));
    Arg3 = (uint16_t)(((uint16_t)(result)) & (1));
    Arg1 = (uint16_t)((Arg2) & (1));
    if (Arg3 == ((uint16_t)(Arg1))) goto loc_00392147;
    if (Arg3 != 0) goto loc_0039224B;
loc_00392147:
    result = (uint16_t)((result) >> (1));
    Arg2 = (uint16_t)((Arg2) >> (1));
    result = (uint16_t)((result) & (1));
    Arg2 = (uint16_t)((Arg2) & (1));
    if (((uint16_t)(result)) == Arg2) goto loc_00392173;
    if ((uint16_t)(result) != 0) goto loc_00392259;
loc_00392173:
    v_stack_p70 = v_xmm1;
    result = KiIsQosGroupingClass((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8A40)))), Arg2, Arg3, Arg3);
loc_003921A4:
    v_stack_p60 = v_xmm1;
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_00392267;
    local_rbx = ~(*(uint64_t *)(arg1 + 0xC8));
    Arg2 = ~(*(uint64_t *)(arg1 + 0x8E60));
    local_rbx = (local_rbx) & (Arg3);
    Arg1 = (v_stack_p68) & (Arg2);
loc_003921D2:
    v_stack_p70 = Arg3;
    v_stack_p78 = *(uint64_t *)(arg1 + 0x89B8);
    if (condition_is_equal) goto loc_00392281;
    goto loc_003921A4;
loc_00392205:
    goto loc_00392039;
loc_00392213:
    goto loc_0039206F;
loc_00392221:
    goto loc_003920A5;
loc_0039222F:
    goto loc_003920DB;
loc_0039223D:
    goto loc_00392111;
loc_0039224B:
    goto loc_00392147;
loc_00392259:
    goto loc_00392173;
loc_00392267:
    local_rbx = (local_rbx) | (Arg3);
    result = (*(uint64_t *)(arg1 + 0x89B8)) & (local_rbx);
    if (result != (*(uint64_t *)(arg1 + 0x89B8))) goto loc_003921D2;
    Arg1 = (Arg1) | (*(uint64_t *)(arg1 + 0x89B8));
    goto loc_003921D2;
loc_00392281:
    local_r14 = 0;
    if (Arg3 != 0) goto loc_00391EB8;
    goto loc_00391EBD;
loc_00392292:
    goto loc_00391E60;
loc_0039229A:
    a4 = 0;
    Arg3 = 0;
    v_stack_p44 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x40)));
    v_stack_p48 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x54)));
    v_stack_m128 = v_stack_p44;
    v_stack_m118 = v_stack_p48;
    v_stack_mF8 = *(uint64_t *)(arg1 + 0x89B8) + 80;
    v_stack_mE8 = *(uint64_t *)(arg1 + 0x89B8) + 96;
    v_stack_mD8 = *(uint64_t *)(arg1 + 0x89B8) + 88;
    v_stack_mC8 = *(uint64_t *)(arg1 + 0x89B8) + 92;
    v_stack_mB8 = *(uint64_t *)(arg1 + 0x89B8) + 100;
    v_stack_mA8 = *(uint64_t *)(arg1 + 0x89B8) + 104;
    v_stack_m120 = 4;
    v_stack_m110 = 4;
    v_stack_mF0 = 4;
    v_stack_mE0 = 4;
    v_stack_mD0 = 4;
    v_stack_mC0 = 4;
    v_stack_mB0 = 4;
    v_stack_mA0 = 4;
    v_stack_p4C = (uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x70));
    v_stack_m98 = v_stack_p4C;
    v_stack_m88 = v_stack_p50;
    v_stack_m78 = v_stack_p58;
    Arg1 = (*(uint64_t *)(arg1 + 0x89B8)) + (108);
    v_stack_m90 = 4;
    v_stack_m58 = Arg1;
    v_stack_p38 = v_stack_m128;
    v_stack_p30 = 14;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    v_stack_m80 = 4;
    v_stack_m70 = 4;
    v_stack_m68 = *(uint64_t *)(arg1 + 0x89B8) + 72;
    v_stack_m60 = 8;
    v_stack_m50 = 4;
    result = EtwWriteEx(*(uint64_t *)(v_rip + 0xB76067), local_rbx, Arg3, a4);
    goto loc_00391F30;
loc_003923C1:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x78)) == ((uint32_t)(local_rbx))) goto loc_00391EB0;
    goto loc_00391F5A;
loc_003923D0:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x78)) == ((uint32_t)(local_rbx))) goto loc_00391EA7;
    goto loc_00391E9D;
loc_003923DF:
    if ((*(uint8_t *)(local_rbx + 0x1EB)) == 0) goto loc_003923F6;
    if (Arg1 != (*(uint64_t *)(gs_base + (0 + 0x20)))) goto loc_00392420;
loc_003923F6:
    goto loc_00391F62;
loc_003923FE:
    v_stack_p40 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x89B8) + 0x14)));
    v_stack_m100 = 4;
    goto loc_00391F07;
loc_00392420:
    result = 0;
    goto loc_00391F32;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x89B0` | `64` | `R` |
| `Arg1` | `+ 0x89B8` | `64` | `R` |
| `Arg1` | `+ 0x8A40` | `32` | `R` |
| `Arg1` | `+ 0x8A44` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00391E00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
