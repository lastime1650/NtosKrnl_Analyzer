# sub_00338E63

- RVA: `0x00338E63`–`0x00339712` (길이 `2,223` bytes)
- VA: `0x0000000140338E63`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076B14`
- 디코드: `470`개 명령, `2,223/2,223` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x00338F53` → [MiAcquirePageListLock](../27/MiAcquirePageListLock_function_0027C450.md) (function, `0x0027C450`)
- `0x003391F1` → [MiFindSuitableLookasideReplacement](MiFindSuitableLookasideReplacement_function_0033A0C0.md) (function, `0x0033A0C0`)
- `0x003392A1` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x003392E2` → [MiPageToNode](MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)
- `0x00339429` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003394A5` → [MiPageToChannel](../2B/MiPageToChannel_function_002B9B48.md) (function, `0x002B9B48`)
- `0x003394BE` → [MiPageToChannel](../2B/MiPageToChannel_function_002B9B48.md) (function, `0x002B9B48`)
- `0x0033950F` → [MiIsDecayPfn](../2B/MiIsDecayPfn_function_002B9240.md) (function, `0x002B9240`)
- `0x00339531` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x00339577` → [MiIsDecayPfn](../2B/MiIsDecayPfn_function_002B9240.md) (function, `0x002B9240`)
- `0x00339599` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x003395CD` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003396F8` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00339708` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00338EEA` → RVA `0x00E3CBE6` (`.data`; read)
- `0x00338F0C` → RVA `0x00E3D240` (`.data`; read)
- `0x00338F71` → RVA `0x00E35C00` (`.data`; read)
- `0x00338FE5` → RVA `0x00E30088` (`.data`; read)
- `0x00339003` → RVA `0x00E2DBC0` (`.data`; read)
- `0x0033900A` → RVA `0x00E2DBC4` (`.data`; read)
- `0x0033901B` → RVA `0x00E2DC20` (`.data`; read)
- `0x0033906A` → RVA `0x00E2DBC0` (`.data`; write)
- `0x003390BC` → RVA `0x00E2DC28` (`.data`; read)
- `0x003393E3` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x003394CC` → RVA `0x00E2DCE0` (`.data`; read)
- `0x003396EA` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x00338EF1` → [sub_0033971A + 0x7E](Unknown_function_0033971A.md) (`tail-transfer`)
  - `0x00338F92` → [sub_0033971A + 0x89](Unknown_function_0033971A.md) (`tail-transfer`)
  - `0x00339298` → [sub_0033971A](Unknown_function_0033971A.md) (`tail-transfer`)
  - `0x003395B2` → [sub_0033971A + 0x98](Unknown_function_0033971A.md) (`tail-transfer`)
  - `0x00339676` → [sub_0033971A + 0xB](Unknown_function_0033971A.md) (`tail-transfer`)
  - `0x003396B6` → [sub_0033971A + 0x51](Unknown_function_0033971A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00338E63  48 89 B4 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rsi
00338E6B  41 8B F9                        mov edi, r9d
00338E6E  4C 89 B4 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r14
00338E76  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
00338E80  83 FF 40                        cmp edi, 0x40
00338E83  0F 83 4A 07 00 00               jae 0x1403395d3
00338E89  8B C3                           mov eax, ebx
00338E8B  4C 8D 34 C5 00 00 00 00         lea r14, [rax*8]
00338E93  4B 8B B4 3E 40 1E 00 00         mov rsi, qword ptr [r14 + r15 + 0x1e40]
00338E9B  48 83 FE FF                     cmp rsi, -1
00338E9F  75 09                           jne 0x140338eaa
00338EA1  FF C7                           inc edi
00338EA3  FF C3                           inc ebx
00338EA5  83 E3 3F                        and ebx, 0x3f
00338EA8  EB D6                           jmp 0x140338e80
00338EAA  4C 8D 24 76                     lea r12, [rsi + rsi*2]
00338EAE  49 C1 E4 04                     shl r12, 4
00338EB2  4C 89 A4 24 00 01 00 00         mov qword ptr [rsp + 0x100], r12
00338EBA  48 8B C1                        mov rax, rcx
00338EBD  4D 8D 2C 04                     lea r13, [r12 + rax]
00338EC1  45 8B E1                        mov r12d, r9d
00338EC4  F0 49 0F BA 6D 18 3F            lock bts qword ptr [r13 + 0x18], 0x3f
00338ECB  0F 82 0F 05 00 00               jb 0x1403393e0
00338ED1  4B 8B 84 3E 40 1E 00 00         mov rax, qword ptr [r14 + r15 + 0x1e40]
00338ED9  4C 8B A4 24 00 01 00 00         mov r12, qword ptr [rsp + 0x100]
00338EE1  48 3B C6                        cmp rax, rsi
00338EE4  0F 85 1E 07 00 00               jne 0x140339608
00338EEA  80 3D F5 3C B0 00 00            cmp byte ptr [rip + 0xb03cf5], 0
00338EF1  0F 84 A1 08 00 00               je 0x140339798
00338EF7  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00338F01  49 8B CC                        mov rcx, r12
00338F04  48 C1 F9 04                     sar rcx, 4
00338F08  48 0F AF C8                     imul rcx, rax
00338F0C  48 8B 05 2D 43 B0 00            mov rax, qword ptr [rip + 0xb0432d]
00338F13  48 C1 E9 09                     shr rcx, 9
00338F17  0F B6 14 48                     movzx edx, byte ptr [rax + rcx*2]
00338F1B  85 D2                           test edx, edx
00338F1D  0F 85 3E 07 00 00               jne 0x140339661
00338F23  C7 84 24 00 01 00 00 09 00 00 00  mov dword ptr [rsp + 0x100], 9
00338F2E  44 8B 84 24 00 01 00 00         mov r8d, dword ptr [rsp + 0x100]
00338F36  4C 8B B4 24 08 01 00 00         mov r14, qword ptr [rsp + 0x108]
00338F3E  49 8B D5                        mov rdx, r13
00338F41  44 8B 8C 24 10 01 00 00         mov r9d, dword ptr [rsp + 0x110]
00338F49  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00338F4E  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00338F53  E8 F8 34 F4 FF                  call 0x14027c450
00338F58  85 C0                           test eax, eax
00338F5A  0F 84 7F 06 00 00               je 0x1403395df
00338F60  41 0F B6 06                     movzx eax, byte ptr [r14]
00338F64  0F 57 C0                        xorps xmm0, xmm0
00338F67  89 84 24 18 01 00 00            mov dword ptr [rsp + 0x118], eax
00338F6E  0F 57 C9                        xorps xmm1, xmm1
00338F71  48 8B 05 88 CC AF 00            mov rax, qword ptr [rip + 0xafcc88]
00338F78  F3 0F 7F 44 24 60               movdqu xmmword ptr [rsp + 0x60], xmm0
00338F7E  F3 0F 7F 4C 24 70               movdqu xmmword ptr [rsp + 0x70], xmm1
00338F84  48 3B F0                        cmp rsi, rax
00338F87  72 0F                           jb 0x140338f98
00338F89  48 05 00 08 00 00               add rax, 0x800
00338F8F  48 3B F0                        cmp rsi, rax
00338F92  0F 82 0B 08 00 00               jb 0x1403397a3
00338F98  49 BF 10 00 00 00 00 DE FF FF   movabs r15, 0xffffde0000000010
00338FA2  49 8B C7                        mov rax, r15
00338FA5  49 8B 0C 04                     mov rcx, qword ptr [r12 + rax]
00338FA9  48 0F BA E1 0A                  bt rcx, 0xa
00338FAE  0F 83 7B 04 00 00               jae 0x14033942f
00338FB4  F6 C1 08                        test cl, 8
00338FB7  75 24                           jne 0x140338fdd
00338FB9  48 8B C6                        mov rax, rsi
00338FBC  4C 8B B4 24 C0 00 00 00         mov r14, qword ptr [rsp + 0xc0]
00338FC4  48 8B B4 24 C8 00 00 00         mov rsi, qword ptr [rsp + 0xc8]
00338FCC  48 81 C4 D0 00 00 00            add rsp, 0xd0
00338FD3  41 5F                           pop r15
00338FD5  41 5D                           pop r13
00338FD7  41 5C                           pop r12
00338FD9  5F                              pop rdi
00338FDA  5B                              pop rbx
00338FDB  C3                              ret
00338FDC  CC                              int3
00338FDD  49 8B 45 28                     mov rax, qword ptr [r13 + 0x28]
00338FE1  49 8B 45 28                     mov rax, qword ptr [r13 + 0x28]
00338FE5  48 8B 0D 9C 70 AF 00            mov rcx, qword ptr [rip + 0xaf709c]
00338FEC  48 C1 E8 2B                     shr rax, 0x2b
00338FF0  25 FF 03 00 00                  and eax, 0x3ff
00338FF5  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
00338FFA  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
00338FFE  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
00339003  48 63 15 B6 4B AF 00            movsxd rdx, dword ptr [rip + 0xaf4bb6]
0033900A  8B 0D B4 4B AF 00               mov ecx, dword ptr [rip + 0xaf4bb4]
00339010  3B D1                           cmp edx, ecx
00339012  77 1D                           ja 0x140339031
00339014  48 8B C2                        mov rax, rdx
00339017  48 C1 E0 04                     shl rax, 4
0033901B  48 03 05 FE 4B AF 00            add rax, qword ptr [rip + 0xaf4bfe]
00339022  48 3B 30                        cmp rsi, qword ptr [rax]
00339025  72 0A                           jb 0x140339031
00339027  3B D1                           cmp edx, ecx
00339029  74 46                           je 0x140339071
0033902B  48 3B 70 10                     cmp rsi, qword ptr [rax + 0x10]
0033902F  72 40                           jb 0x140339071
00339031  45 33 C9                        xor r9d, r9d
00339034  41 8B D1                        mov edx, r9d
00339037  3B CA                           cmp ecx, edx
00339039  0F 8C D8 03 00 00               jl 0x140339417
0033903F  44 8D 04 0A                     lea r8d, [rdx + rcx]
00339043  41 D1 F8                        sar r8d, 1
00339046  49 63 C0                        movsxd rax, r8d
00339049  48 C1 E0 04                     shl rax, 4
0033904D  48 03 05 CC 4B AF 00            add rax, qword ptr [rip + 0xaf4bcc]
00339054  48 3B 30                        cmp rsi, qword ptr [rax]
00339057  0F 82 52 05 00 00               jb 0x1403395af
0033905D  44 3B 05 60 4B AF 00            cmp r8d, dword ptr [rip + 0xaf4b60]
00339064  0F 85 0B 04 00 00               jne 0x140339475
0033906A  44 89 05 4F 4B AF 00            mov dword ptr [rip + 0xaf4b4f], r8d
00339071  8B 40 08                        mov eax, dword ptr [rax + 8]
00339074  45 8B 45 20                     mov r8d, dword ptr [r13 + 0x20]
00339078  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
0033907C  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
00339080  C1 E8 18                        shr eax, 0x18
00339083  44 89 84 24 10 01 00 00         mov dword ptr [rsp + 0x110], r8d
0033908B  48 BA 30 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000030
00339095  48 BF 00 00 00 00 00 DE FF FF   movabs rdi, 0xffffde0000000000
0033909F  A8 08                           test al, 8
003390A1  0F 85 AE 03 00 00               jne 0x140339455
003390A7  49 BE AB AA AA AA AA AA AA AA   movabs r14, 0xaaaaaaaaaaaaaaab
003390B1  0F B6 9C 24 13 01 00 00         movzx ebx, byte ptr [rsp + 0x113]
003390B9  83 E3 07                        and ebx, 7
003390BC  48 83 3D 64 4B AF 00 00         cmp qword ptr [rip + 0xaf4b64], 0
003390C4  89 5C 24 6C                     mov dword ptr [rsp + 0x6c], ebx
003390C8  0F 85 E5 03 00 00               jne 0x1403394b3
003390CE  45 32 DB                        xor r11b, r11b
003390D1  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
003390D5  4C 63 8C 24 00 01 00 00         movsxd r9, dword ptr [rsp + 0x100]
003390DD  4C 69 C0 80 DF 00 00            imul r8, rax, 0xdf80
003390E4  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
003390E9  44 88 9C 24 10 01 00 00         mov byte ptr [rsp + 0x110], r11b
003390F1  44 88 5C 24 70                  mov byte ptr [rsp + 0x70], r11b
003390F6  44 89 4C 24 74                  mov dword ptr [rsp + 0x74], r9d
003390FB  4C 03 40 10                     add r8, qword ptr [rax + 0x10]
003390FF  41 83 F9 09                     cmp r9d, 9
00339103  0F 8C A9 05 00 00               jl 0x1403396b2
00339109  41 0F B6 C3                     movzx eax, r11b
0033910D  44 8B D3                        mov r10d, ebx
00339110  48 8D 0C C5 3B 00 00 00         lea rcx, [rax*8 + 0x3b]
00339118  49 03 CA                        add rcx, r10
0033911B  48 6B C1 58                     imul rax, rcx, 0x58
0033911F  49 03 C0                        add rax, r8
00339122  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00339127  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
0033912B  45 33 E4                        xor r12d, r12d
0033912E  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
00339132  41 8B FC                        mov edi, r12d
00339135  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
00339139  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0033913E  4C 69 C0 80 DF 00 00            imul r8, rax, 0xdf80
00339145  48 8D 51 10                     lea rdx, [rcx + 0x10]
00339149  4C 89 54 24 30                  mov qword ptr [rsp + 0x30], r10
0033914E  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
00339153  48 89 94 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdx
0033915B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00339160  85 FF                           test edi, edi
00339162  0F 84 99 02 00 00               je 0x140339401
00339168  83 FF 01                        cmp edi, 1
0033916B  0F 84 58 02 00 00               je 0x1403393c9
00339171  48 8B 12                        mov rdx, qword ptr [rdx]
00339174  41 83 F9 09                     cmp r9d, 9
00339178  0F 8C AF 04 00 00               jl 0x14033962d
0033917E  41 0F B6 C3                     movzx eax, r11b
00339182  4C 8D 34 C5 0D 00 00 00         lea r14, [rax*8 + 0xd]
0033918A  4D 03 F2                        add r14, r10
0033918D  49 C1 E6 09                     shl r14, 9
00339191  4D 03 F0                        add r14, r8
00339194  4C 03 F2                        add r14, rdx
00339197  41 8B DC                        mov ebx, r12d
0033919A  49 8B CE                        mov rcx, r14
0033919D  48 8B 01                        mov rax, qword ptr [rcx]
003391A0  48 3B C6                        cmp rax, rsi
003391A3  74 36                           je 0x1403391db
003391A5  FF C3                           inc ebx
003391A7  48 83 C1 08                     add rcx, 8
003391AB  8B C3                           mov eax, ebx
003391AD  83 FB 40                        cmp ebx, 0x40
003391B0  72 EB                           jb 0x14033919d
003391B2  83 F8 40                        cmp eax, 0x40
003391B5  75 24                           jne 0x1403391db
003391B7  FF C7                           inc edi
003391B9  83 FF 03                        cmp edi, 3
003391BC  0F 8D F7 FD FF FF               jge 0x140338fb9
003391C2  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
003391C7  48 8B 94 24 B0 00 00 00         mov rdx, qword ptr [rsp + 0xb0]
003391CF  49 BF 10 00 00 00 00 DE FF FF   movabs r15, 0xffffde0000000010
003391D9  EB 85                           jmp 0x140339160
003391DB  8B 84 24 18 01 00 00            mov eax, dword ptr [rsp + 0x118]
003391E2  4D 8B CD                        mov r9, r13
003391E5  44 8B C3                        mov r8d, ebx
003391E8  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
003391EC  49 8B D6                        mov rdx, r14
003391EF  8B CF                           mov ecx, edi
003391F1  E8 CA 0E 00 00                  call 0x14033a0c0
003391F6  85 C0                           test eax, eax
003391F8  0F 85 AB 01 00 00               jne 0x1403393a9
003391FE  8B C3                           mov eax, ebx
00339200  4D 8B 14 C6                     mov r10, qword ptr [r14 + rax*8]
00339204  49 C7 04 C6 FF FF FF FF         mov qword ptr [r14 + rax*8], 0xffffffffffffffff
0033920C  49 83 FA FF                     cmp r10, -1
00339210  0F 84 93 01 00 00               je 0x1403393a9
00339216  48 8B 15 E3 C9 AF 00            mov rdx, qword ptr [rip + 0xafc9e3]
0033921D  4C 3B D2                        cmp r10, rdx
00339220  72 10                           jb 0x140339232
00339222  48 8D 82 00 08 00 00            lea rax, [rdx + 0x800]
00339229  4C 3B D0                        cmp r10, rax
0033922C  0F 82 77 01 00 00               jb 0x1403393a9
00339232  4F 8D 34 52                     lea r14, [r10 + r10*2]
00339236  66 44 89 A4 24 A1 00 00 00      mov word ptr [rsp + 0xa1], r12w
0033923F  4D 03 F6                        add r14, r14
00339242  C6 84 24 A3 00 00 00 00         mov byte ptr [rsp + 0xa3], 0
0033924A  4C 89 A4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r12
00339252  49 8B C7                        mov rax, r15
00339255  4A 8B 0C F0                     mov rcx, qword ptr [rax + r14*8]
00339259  49 C7 C7 F7 FF FF FF            mov r15, 0xfffffffffffffff7
00339260  48 C7 C0 FF FF FF F7            mov rax, 0xfffffffff7ffffff
00339267  48 0F BA E1 0A                  bt rcx, 0xa
0033926C  4C 0F 43 F8                     cmovae r15, rax
00339270  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0033927A  4C 23 F9                        and r15, rcx
0033927D  48 8B C0                        mov rax, rax
00339280  4A 8D 1C F0                     lea rbx, [rax + r14*8]
00339284  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00339289  4C 3B D2                        cmp r10, rdx
0033928C  72 10                           jb 0x14033929e
0033928E  48 8D 82 00 08 00 00            lea rax, [rdx + 0x800]
00339295  4C 3B D0                        cmp r10, rax
00339298  0F 82 7C 04 00 00               jb 0x14033971a
0033929E  48 8B CB                        mov rcx, rbx
003392A1  E8 2A 50 F5 FF                  call 0x14028e2d0
003392A6  44 8B E0                        mov r12d, eax
003392A9  48 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rbx
003392B1  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
003392BB  48 8B D0                        mov rdx, rax
003392BE  4A 8B 14 F2                     mov rdx, qword ptr [rdx + r14*8]
003392C2  49 8B CA                        mov rcx, r10
003392C5  4C 8B 05 BC 6D AF 00            mov r8, qword ptr [rip + 0xaf6dbc]
003392CC  48 C1 EA 2B                     shr rdx, 0x2b
003392D0  81 E2 FF 03 00 00               and edx, 0x3ff
003392D6  4D 8B 0C D0                     mov r9, qword ptr [r8 + rdx*8]
003392DA  4C 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], r9
003392E2  E8 E9 F9 FF FF                  call 0x140338cd0
003392E7  89 84 24 98 00 00 00            mov dword ptr [rsp + 0x98], eax
003392EE  48 B9 20 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000020
003392F8  48 8B C1                        mov rax, rcx
003392FB  46 8B 04 F0                     mov r8d, dword ptr [rax + r14*8]
003392FF  44 89 44 24 48                  mov dword ptr [rsp + 0x48], r8d
00339304  48 8B C1                        mov rax, rcx
00339307  42 8B 0C F0                     mov ecx, dword ptr [rax + r14*8]
0033930B  C1 E9 18                        shr ecx, 0x18
0033930E  49 B9 00 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000000
00339318  F6 C1 08                        test cl, 8
0033931B  0F 85 1E 01 00 00               jne 0x14033943f
00339321  0F B6 5C 24 4B                  movzx ebx, byte ptr [rsp + 0x4b]
00339326  83 E3 07                        and ebx, 7
00339329  48 83 3D F7 48 AF 00 00         cmp qword ptr [rip + 0xaf48f7], 0
00339331  89 9C 24 9C 00 00 00            mov dword ptr [rsp + 0x9c], ebx
00339338  0F 85 4A 01 00 00               jne 0x140339488
0033933E  45 32 C0                        xor r8b, r8b
00339341  8B 84 24 98 00 00 00            mov eax, dword ptr [rsp + 0x98]
00339348  4C 69 C8 80 DF 00 00            imul r9, rax, 0xdf80
0033934F  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
00339357  44 88 84 24 A0 00 00 00         mov byte ptr [rsp + 0xa0], r8b
0033935F  44 89 A4 24 A4 00 00 00         mov dword ptr [rsp + 0xa4], r12d
00339367  4C 03 48 10                     add r9, qword ptr [rax + 0x10]
0033936B  41 83 FC 09                     cmp r12d, 9
0033936F  0F 8C FD 02 00 00               jl 0x140339672
00339375  8B C3                           mov eax, ebx
00339377  41 0F B6 C8                     movzx ecx, r8b
0033937B  48 8D 0C CD 3B 00 00 00         lea rcx, [rcx*8 + 0x3b]
00339383  48 03 C8                        add rcx, rax
00339386  48 6B C1 58                     imul rax, rcx, 0x58
0033938A  49 03 C1                        add rax, r9
0033938D  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00339395  48 B8 10 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000010
0033939F  48 8B C0                        mov rax, rax
003393A2  4E 89 3C F0                     mov qword ptr [rax + r14*8], r15
003393A6  45 33 E4                        xor r12d, r12d
003393A9  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
003393AE  44 0F B6 9C 24 10 01 00 00      movzx r11d, byte ptr [rsp + 0x110]
003393B7  4C 8B 54 24 30                  mov r10, qword ptr [rsp + 0x30]
003393BC  44 8B 8C 24 00 01 00 00         mov r9d, dword ptr [rsp + 0x100]
003393C4  E9 EE FD FF FF                  jmp 0x1403391b7
003393C9  4D 8B F2                        mov r14, r10
003393CC  49 C1 E6 09                     shl r14, 9
003393D0  49 81 C6 40 2E 00 00            add r14, 0x2e40
003393D7  4C 03 F1                        add r14, rcx
003393DA  E9 B8 FD FF FF                  jmp 0x140339197
003393DF  90                              nop
003393E0  41 FF C4                        inc r12d
003393E3  44 85 25 C2 BE C8 00            test dword ptr [rip + 0xc8bec2], r12d
003393EA  0F 84 FA 02 00 00               je 0x1403396ea
003393F0  F3 90                           pause
003393F2  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
003393F6  48 85 C0                        test rax, rax
003393F9  0F 89 C5 FA FF FF               jns 0x140338ec4
003393FF  EB DF                           jmp 0x1403393e0
00339401  4D 8B F2                        mov r14, r10
00339404  49 C1 E6 09                     shl r14, 9
00339408  49 81 C6 40 1E 00 00            add r14, 0x1e40
0033940F  4C 03 F1                        add r14, rcx
00339412  E9 80 FD FF FF                  jmp 0x140339197
00339417  4C 8B C6                        mov r8, rsi
0033941A  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0033941F  BA 80 51 00 00                  mov edx, 0x5180
00339424  B9 1A 00 00 00                  mov ecx, 0x1a
00339429  E8 32 42 1C 00                  call 0x1404fd660
0033942E  CC                              int3
0033942F  48 0F BA E1 1B                  bt rcx, 0x1b
00339434  0F 82 A3 FB FF FF               jb 0x140338fdd
0033943A  E9 7A FB FF FF                  jmp 0x140338fb9
0033943F  49 8B C1                        mov rax, r9
00339442  48 3B D8                        cmp rbx, rax
00339445  0F 83 81 00 00 00               jae 0x1403394cc
0033944B  BB 05 00 00 00                  mov ebx, 5
00339450  E9 D4 FE FF FF                  jmp 0x140339329
00339455  48 8B C7                        mov rax, rdi
00339458  4C 3B E8                        cmp r13, rax
0033945B  0F 83 E3 00 00 00               jae 0x140339544
00339461  49 BE AB AA AA AA AA AA AA AA   movabs r14, 0xaaaaaaaaaaaaaaab
0033946B  BB 05 00 00 00                  mov ebx, 5
00339470  E9 47 FC FF FF                  jmp 0x1403390bc
00339475  48 3B 70 10                     cmp rsi, qword ptr [rax + 0x10]
00339479  0F 82 EB FB FF FF               jb 0x14033906a
0033947F  41 8D 50 01                     lea edx, [r8 + 1]
00339483  E9 AF FB FF FF                  jmp 0x140339037
00339488  49 8B C1                        mov rax, r9
0033948B  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00339490  48 2B C8                        sub rcx, rax
00339493  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
0033949D  48 C1 F9 04                     sar rcx, 4
003394A1  48 0F AF C8                     imul rcx, rax
003394A5  E8 9E 06 F8 FF                  call 0x1402b9b48
003394AA  44 0F B6 C0                     movzx r8d, al
003394AE  E9 8E FE FF FF                  jmp 0x140339341
003394B3  49 C1 FC 04                     sar r12, 4
003394B7  4D 0F AF E6                     imul r12, r14
003394BB  49 8B CC                        mov rcx, r12
003394BE  E8 85 06 F8 FF                  call 0x1402b9b48
003394C3  44 0F B6 D8                     movzx r11d, al
003394C7  E9 05 FC FF FF                  jmp 0x1403390d1
003394CC  48 8B 05 0D 48 AF 00            mov rax, qword ptr [rip + 0xaf480d]
003394D3  48 8D 0C 40                     lea rcx, [rax + rax*2]
003394D7  48 B8 30 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000030
003394E1  48 C1 E1 04                     shl rcx, 4
003394E5  48 8B C0                        mov rax, rax
003394E8  48 03 C8                        add rcx, rax
003394EB  48 3B D9                        cmp rbx, rcx
003394EE  0F 83 57 FF FF FF               jae 0x14033944b
003394F4  49 8B C1                        mov rax, r9
003394F7  48 8B CB                        mov rcx, rbx
003394FA  48 2B C8                        sub rcx, rax
003394FD  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00339507  48 C1 F9 04                     sar rcx, 4
0033950B  48 0F AF C8                     imul rcx, rax
0033950F  E8 2C FD F7 FF                  call 0x1402b9240
00339514  85 C0                           test eax, eax
00339516  0F 85 2F FF FF FF               jne 0x14033944b
0033951C  41 C1 E8 10                     shr r8d, 0x10
00339520  41 80 E0 07                     and r8b, 7
00339524  41 80 F8 06                     cmp r8b, 6
00339528  0F 84 F3 FD FF FF               je 0x140339321
0033952E  48 8B CB                        mov rcx, rbx
00339531  E8 9A 4D F5 FF                  call 0x14028e2d0
00339536  83 F8 09                        cmp eax, 9
00339539  0F 85 E2 FD FF FF               jne 0x140339321
0033953F  E9 07 FF FF FF                  jmp 0x14033944b
00339544  48 8B 05 95 47 AF 00            mov rax, qword ptr [rip + 0xaf4795]
0033954B  48 8D 0C 40                     lea rcx, [rax + rax*2]
0033954F  48 C1 E1 04                     shl rcx, 4
00339553  48 8B C2                        mov rax, rdx
00339556  48 03 C8                        add rcx, rax
00339559  49 BE AB AA AA AA AA AA AA AA   movabs r14, 0xaaaaaaaaaaaaaaab
00339563  4C 3B E9                        cmp r13, rcx
00339566  0F 83 FF FE FF FF               jae 0x14033946b
0033956C  49 8B CC                        mov rcx, r12
0033956F  48 C1 F9 04                     sar rcx, 4
00339573  49 0F AF CE                     imul rcx, r14
00339577  E8 C4 FC F7 FF                  call 0x1402b9240
0033957C  85 C0                           test eax, eax
0033957E  0F 85 E7 FE FF FF               jne 0x14033946b
00339584  41 C1 E8 10                     shr r8d, 0x10
00339588  41 80 E0 07                     and r8b, 7
0033958C  41 80 F8 06                     cmp r8b, 6
00339590  0F 84 1B FB FF FF               je 0x1403390b1
00339596  49 8B CD                        mov rcx, r13
00339599  E8 32 4D F5 FF                  call 0x14028e2d0
0033959E  83 F8 09                        cmp eax, 9
003395A1  0F 85 0A FB FF FF               jne 0x1403390b1
003395A7  8D 58 FC                        lea ebx, [rax - 4]
003395AA  E9 0D FB FF FF                  jmp 0x1403390bc
003395AF  45 85 C0                        test r8d, r8d
003395B2  0F 85 FA 01 00 00               jne 0x1403397b2
003395B8  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
003395BD  4C 8B C6                        mov r8, rsi
003395C0  4C 8B C8                        mov r9, rax
003395C3  BA 80 51 00 00                  mov edx, 0x5180
003395C8  B9 1A 00 00 00                  mov ecx, 0x1a
003395CD  E8 8E 40 1C 00                  call 0x1404fd660
003395D2  CC                              int3
003395D3  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
003395DA  E9 DD F9 FF FF                  jmp 0x140338fbc
003395DF  8B 8C 24 18 01 00 00            mov ecx, dword ptr [rsp + 0x118]
003395E6  8B 84 24 10 01 00 00            mov eax, dword ptr [rsp + 0x110]
003395ED  FF C1                           inc ecx
003395EF  83 F9 08                        cmp ecx, 8
003395F2  89 8C 24 18 01 00 00            mov dword ptr [rsp + 0x118], ecx
003395F9  B9 01 00 00 00                  mov ecx, 1
003395FE  0F 44 C1                        cmove eax, ecx
00339601  89 84 24 10 01 00 00            mov dword ptr [rsp + 0x110], eax
00339608  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00339612  F0 49 21 45 18                  lock and qword ptr [r13 + 0x18], rax
00339617  FF CF                           dec edi
00339619  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
00339623  FF CB                           dec ebx
00339625  45 33 C9                        xor r9d, r9d
00339628  E9 74 F8 FF FF                  jmp 0x140338ea1
0033962D  0F B6 44 24 78                  movzx eax, byte ptr [rsp + 0x78]
00339632  41 83 F9 08                     cmp r9d, 8
00339636  41 8B CC                        mov ecx, r12d
00339639  0F 44 C8                        cmove ecx, eax
0033963C  0F B6 C1                        movzx eax, cl
0033963F  4D 8D 34 C2                     lea r14, [r10 + rax*8]
00339643  49 63 C1                        movsxd rax, r9d
00339646  48 69 C8 E8 00 00 00            imul rcx, rax, 0xe8
0033964D  49 C1 E6 09                     shl r14, 9
00339651  49 03 C8                        add rcx, r8
00339654  4C 03 B4 11 90 3D 00 00         add r14, qword ptr [rcx + rdx + 0x3d90]
0033965C  E9 36 FB FF FF                  jmp 0x140339197
00339661  44 8D 42 FF                     lea r8d, [rdx - 1]
00339665  44 89 84 24 00 01 00 00         mov dword ptr [rsp + 0x100], r8d
0033966D  E9 C4 F8 FF FF                  jmp 0x140338f36
00339672  41 83 FC 08                     cmp r12d, 8
00339676  0F 84 A9 00 00 00               je 0x140339725
0033967C  C6 84 24 A8 00 00 00 00         mov byte ptr [rsp + 0xa8], 0
00339684  32 D2                           xor dl, dl
00339686  0F B6 CA                        movzx ecx, dl
00339689  8B C3                           mov eax, ebx
0033968B  48 8D 0C C8                     lea rcx, [rax + rcx*8]
0033968F  49 63 C4                        movsxd rax, r12d
00339692  48 6B D1 58                     imul rdx, rcx, 0x58
00339696  48 69 C8 E8 00 00 00            imul rcx, rax, 0xe8
0033969D  4A 03 94 09 98 3D 00 00         add rdx, qword ptr [rcx + r9 + 0x3d98]
003396A5  48 89 94 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdx
003396AD  E9 E3 FC FF FF                  jmp 0x140339395
003396B2  41 83 F9 08                     cmp r9d, 8
003396B6  0F 84 AF 00 00 00               je 0x14033976b
003396BC  C6 44 24 78 00                  mov byte ptr [rsp + 0x78], 0
003396C1  32 D2                           xor dl, dl
003396C3  0F B6 C2                        movzx eax, dl
003396C6  44 8B D3                        mov r10d, ebx
003396C9  49 8D 0C C2                     lea rcx, [r10 + rax*8]
003396CD  48 6B D1 58                     imul rdx, rcx, 0x58
003396D1  49 69 C9 E8 00 00 00            imul rcx, r9, 0xe8
003396D8  4A 03 94 01 98 3D 00 00         add rdx, qword ptr [rcx + r8 + 0x3d98]
003396E0  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
003396E5  E9 3D FA FF FF                  jmp 0x140339127
003396EA  8B 05 C8 D3 C8 00               mov eax, dword ptr [rip + 0xc8d3c8]
003396F0  A8 40                           test al, 0x40
003396F2  0F 84 F8 FC FF FF               je 0x1403393f0
003396F8  E8 93 5D FD FF                  call 0x14030f490
003396FD  84 C0                           test al, al
003396FF  0F 84 EB FC FF FF               je 0x1403393f0
00339705  41 8B CC                        mov ecx, r12d
00339708  E8 53 5D FD FF                  call 0x14030f460
0033970D  E9 E0 FC FF FF                  jmp 0x1403393f2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00338E63(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, unsigned int a13, __int64 a14, unsigned __int8 a15, __int64 a16, __int64 a17, __int64 a18, unsigned int a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28, __int64 a29, __int64 a30, __int64 a31, unsigned int a32, __int64 a33, unsigned __int8 a34, unsigned int a35)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p100;
    unsigned int v_stack_p118;
    unsigned __int64 v_stack_p128;
    unsigned __int64 v_stack_p130;
    unsigned __int64 v_stack_p138;
    unsigned int v_stack_p140;
    unsigned __int8 v_stack_p143;
    unsigned __int64 v_stack_p148;
    unsigned __int64 v_stack_p150;
    unsigned __int64 v_stack_p158;
    unsigned int v_stack_p160;
    unsigned int v_stack_p164;
    unsigned __int8 v_stack_p168;
    unsigned int v_stack_p16C;
    unsigned __int8 v_stack_p170;
    unsigned __int64 v_stack_p178;
    unsigned __int64 v_stack_p180;
    unsigned __int64 v_stack_p188;
    unsigned int v_stack_p190;
    unsigned int v_stack_p194;
    unsigned __int8 v_stack_p198;
    unsigned __int16 v_stack_p199;
    unsigned __int8 v_stack_p19B;
    unsigned int v_stack_p19C;
    unsigned __int64 v_stack_p1A0;
    unsigned __int64 v_stack_p1A8;
    unsigned int v_stack_p1F8;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p208;
    unsigned __int8 v_stack_p20B;
    unsigned int v_stack_p210;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pC8;

    v_stack_pC8 = v_rsi;
    v_stack_pC0 = v_r14;
loc_00338E80:
    if (((unsigned int)((unsigned int)(a4))) >= 64) goto loc_003395D3;
    if ((*(unsigned __int64 *)((unsigned int)((unsigned int)(v_rbx)) * 8 + v_r15 * 1 + 7744)) != -1) goto loc_00338EAA;
loc_00338EA1:
    v_rdi = (unsigned int)(((unsigned int)(a4)) + 1);
    v_rbx = (unsigned int)((v_rbx) + 1);
    v_rbx = (unsigned int)((v_rbx) & (63));
    goto loc_00338E80;
loc_00338EAA:
    v_r12 = (*(unsigned __int64 *)((unsigned int)((unsigned int)(v_rbx)) * 8 + v_r15 * 1 + 7744) + *(unsigned __int64 *)((unsigned int)((unsigned int)(v_rbx)) * 8 + v_r15 * 1 + 7744) * 2) << (4);
    v_stack_p100 = v_r12;
loc_00338EC4:
    if (condition_is_below) goto loc_003393E0;
    if ((*(unsigned __int64 *)((unsigned int)((unsigned int)(v_rbx)) * 8 + v_r15 * 1 + 7744)) != (*(unsigned __int64 *)((unsigned int)((unsigned int)(v_rbx)) * 8 + v_r15 * 1 + 7744))) goto loc_00339608;
    a1 = (a32) >> (4);
    a1 = (a1) * (*(unsigned __int64 *)((unsigned int)((unsigned int)(v_rbx)) * 8 + v_r15 * 1 + 7744));
    a1 = (a1) >> (9);
    if ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 11551533) + a1 * 2)) != 0) goto loc_00339661;
    v_stack_p100 = 9;
loc_00338F36:
    v_stack_p20 = a33;
    result = MiAcquirePageListLock(a8, v_r12 + a1 * 1, (unsigned int)(a32), (unsigned int)(a34));
    if ((unsigned int)(result) == 0) goto loc_003395DF;
    v_stack_p118 = (unsigned int)(*(unsigned __int8 *)(a33));
    v_stack_p60 = v_xmm0;
    v_stack_p70 = v_xmm1;
    if ((*(unsigned __int64 *)((unsigned int)((unsigned int)(v_rbx)) * 8 + v_r15 * 1 + 7744)) < (*(unsigned __int64 *)(v_rip + 11521160))) goto loc_00338F98;
    result = (*(unsigned __int64 *)(v_rip + 11521160)) + (0x800ULL);
loc_00338F98:
    if ((*(unsigned __int64 *)((unsigned int)((unsigned int)(v_rbx)) * 8 + v_r15 * 1 + 7744)) >= result) goto loc_0033942F;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a32 + v_r15 * 1))) & (8)) != 0) goto loc_00338FDD;
loc_00338FB9:
loc_00338FBC:
    v_rsp = (v_rsp) + (208);
    return *(unsigned __int64 *)((unsigned int)((unsigned int)(v_rbx)) * 8 + v_r15 * 1 + 7744);
loc_00338FDD:
    result = (*(unsigned __int64 *)(v_r12 + a1 * 1 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_p150 = v_r12 + a1 * 1;
    v_stack_p148 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11497628) + result * 8);
    if (((unsigned int)((int)(*(unsigned int *)(v_rip + 11488182)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11488180))))) goto loc_00339031;
    result = ((int)(*(unsigned int *)(v_rip + 11488182))) << (4);
    result = (result) + (*(unsigned __int64 *)(v_rip + 11488254));
    if (a25 < (*(unsigned __int64 *)(result))) goto loc_00339031;
    if (((unsigned int)((int)(*(unsigned int *)(v_rip + 11488182)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11488180))))) goto loc_00339071;
    if (a25 < (*(unsigned __int64 *)(result + 16))) goto loc_00339071;
loc_00339031:
    a4 = 0;
loc_00339037:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11488180)))) < 0) goto loc_00339417;
    a3 = (unsigned int)((0 + (unsigned int)(*(unsigned int *)(v_rip + 11488180)) * 1) >> (1));
    result = ((int)((unsigned int)(a3))) << (4);
    result = (result) + (*(unsigned __int64 *)(v_rip + 11488204));
    if (a25 < (*(unsigned __int64 *)(result))) goto loc_003395AF;
    if (((unsigned int)(a3)) != (*(unsigned int *)(v_rip + 11488096))) goto loc_00339475;
loc_0033906A:
    *(unsigned int *)(v_rip + 11488079) = (unsigned int)(a3);
loc_00339071:
    v_stack_p160 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 8)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r12 + a1 * 1 + 32))) >> (24));
    v_stack_p208 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + a1 * 1 + 32)));
    if ((((unsigned __int8)(result)) & (8)) != 0) goto loc_00339455;
loc_003390B1:
    v_rbx = (unsigned int)((v_stack_p20B) & (7));
loc_003390BC:
    v_stack_p164 = (unsigned int)(v_rbx);
    if ((*(unsigned __int64 *)(v_rip + 11488100)) != 0) goto loc_003394B3;
    v_r11 = 0;
loc_003390D1:
    a3 = ((unsigned int)(*(unsigned int *)(v_r12 + a1 * 1 + 32))) * ((unsigned int)(a13));
    v_stack_p208 = 0;
    v_stack_p168 = 0;
    v_stack_p16C = (unsigned int)((int)(a32));
    a3 = (a3) + (*(unsigned __int64 *)(a10 + 16));
    if (((unsigned int)((int)(a32))) < 9) goto loc_003396B2;
    a1 = (0 * 8 + 59) + ((unsigned int)((unsigned int)(v_rbx)));
    result = (0) * (a1);
    result = (result) + (a3);
    v_stack_p158 = result;
loc_00339127:
    v_r12 = 0;
    a3 = (a3) * ((unsigned int)(a13));
    v_stack_p128 = (unsigned int)((unsigned int)(v_rbx));
    v_stack_p130 = a3;
    v_stack_p1A8 = a10 + 16;
loc_00339160:
    if (0 == 0) goto loc_00339401;
    if (0 == 1) goto loc_003393C9;
    if (((unsigned int)((int)(a32))) < 9) goto loc_0033962D;
    v_r14 = (0 * 8 + 13) + ((unsigned int)((unsigned int)(v_rbx)));
    v_r14 = (v_r14) << (9);
    v_r14 = (v_r14) + (a3);
    v_r14 = (v_r14) + (*(unsigned __int64 *)(a10 + 16));
loc_00339197:
loc_0033919D:
    if ((*(unsigned __int64 *)(v_r14)) == a25) goto loc_003391DB;
    v_rbx = (unsigned int)((0) + 1);
    a1 = (v_r14) + (8);
    if (((unsigned int)(v_rbx)) < 64) goto loc_0033919D;
    if (((unsigned int)((unsigned int)((unsigned int)(v_rbx)))) != 64) goto loc_003391DB;
loc_003391B7:
    v_rdi = (unsigned int)((0) + 1);
    if (((unsigned int)(v_rdi)) >= 3) goto loc_00338FB9;
    goto loc_00339160;
loc_003391DB:
    v_stack_p118 = (unsigned int)((unsigned int)(a35));
    result = MiFindSuitableLookasideReplacement((unsigned int)((unsigned int)(v_rdi)), v_r14, (unsigned int)((unsigned int)(v_rbx)), v_r12 + a1 * 1);
    if ((unsigned int)(result) != 0) goto loc_003393A9;
    *(unsigned __int64 *)(v_r14 + (unsigned int)((unsigned int)(v_rbx)) * 8) = -1;
    if ((*(unsigned __int64 *)(v_r14 + (unsigned int)((unsigned int)(v_rbx)) * 8)) == -1) goto loc_003393A9;
    if ((*(unsigned __int64 *)(v_r14 + (unsigned int)((unsigned int)(v_rbx)) * 8)) < (*(unsigned __int64 *)(v_rip + 11520483))) goto loc_00339232;
    if ((*(unsigned __int64 *)(v_r14 + (unsigned int)((unsigned int)(v_rbx)) * 8)) < (*(unsigned __int64 *)(v_rip + 11520483) + 2048)) goto loc_003393A9;
loc_00339232:
    v_stack_p199 = 0;
    v_r14 = (*(unsigned __int64 *)(v_r14 + (unsigned int)((unsigned int)(v_rbx)) * 8) + *(unsigned __int64 *)(v_r14 + (unsigned int)((unsigned int)(v_rbx)) * 8) * 2) + (*(unsigned __int64 *)(v_r14 + (unsigned int)((unsigned int)(v_rbx)) * 8) + *(unsigned __int64 *)(v_r14 + (unsigned int)((unsigned int)(v_rbx)) * 8) * 2);
    v_stack_p19B = 0;
    v_stack_p1A0 = 0;
    v_r15 = -9;
    if (condition_is_above_or_equal) { v_r15 = 0xFFFFFFFFF7FFFFFFULL; }
    v_r15 = (v_r15) & (*(unsigned __int64 *)(v_r15 + v_r14 * 8));
    v_stack_p138 = 0xFFFFFFFFF7FFFFFFULL + v_r14 * 8;
    if ((*(unsigned __int64 *)(v_r14 + (unsigned int)((unsigned int)(v_rbx)) * 8)) < (*(unsigned __int64 *)(v_rip + 11520483))) goto loc_0033929E;
loc_0033929E:
    result = MiGetPfnSlabType(0xFFFFFFFFF7FFFFFFULL + v_r14 * 8, *(unsigned __int64 *)(v_rip + 11520483), (unsigned int)((unsigned int)(v_rbx)), v_r12 + a1 * 1);
    v_stack_p180 = 0xFFFFFFFFF7FFFFFFULL + v_r14 * 8;
    a2 = (*(unsigned __int64 *)(result + v_r14 * 8)) >> (43);
    a2 = (unsigned int)((a2) & (0x3FFULL));
    v_stack_p178 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11496892) + a2 * 8);
    result = MiPageToNode(*(unsigned __int64 *)(v_r14 + (unsigned int)((unsigned int)(v_rbx)) * 8), a2, *(unsigned __int64 *)(v_rip + 11496892), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11496892) + a2 * 8));
    v_stack_p190 = (unsigned int)(result);
    v_stack_p140 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r14 + (unsigned int)((unsigned int)(v_rbx)) * 8) + v_r14 * 8)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r14 + (unsigned int)((unsigned int)(v_rbx)) * 8) + v_r14 * 8))) >> (24));
    if ((((unsigned __int8)(a1)) & (8)) != 0) goto loc_0033943F;
loc_00339321:
    v_rbx = (unsigned int)((v_stack_p143) & (7));
loc_00339329:
    v_stack_p194 = (unsigned int)(v_rbx);
    if ((*(unsigned __int64 *)(v_rip + 11487479)) != 0) goto loc_00339488;
    a3 = 0;
loc_00339341:
    a4 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11496892) + a2 * 8)) * ((unsigned int)(a19));
    v_stack_p198 = 0;
    v_stack_p19C = (unsigned int)((unsigned int)((unsigned int)(result)));
    a4 = (a4) + (*(unsigned __int64 *)(a16 + 16));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) < 9) goto loc_00339672;
    a1 = (0 * 8 + 59) + ((unsigned int)((unsigned int)(v_rbx)));
    result = ((unsigned int)((unsigned int)(v_rbx))) * (a1);
    result = (result) + (a4);
    v_stack_p188 = result;
loc_00339395:
    *(unsigned __int64 *)(result + v_r14 * 8) = v_r15;
    v_r12 = 0;
loc_003393A9:
    goto loc_003391B7;
loc_003393C9:
    v_r14 = (a6) << (9);
    v_r14 = (v_r14) + (0x2E40ULL);
    v_r14 = (v_r14) + (a1);
    goto loc_00339197;
loc_003393E0:
    v_r12 = (unsigned int)((v_r12) + 1);
    if (((*(unsigned int *)(v_rip + 13156034)) & ((unsigned int)(v_r12))) == 0) goto loc_003396EA;
loc_003393F0:
loc_003393F2:
    if (!sign_flag) goto loc_00338EC4;
    goto loc_003393E0;
loc_00339401:
    v_r14 = (a6) << (9);
    v_r14 = (v_r14) + (0x1E40ULL);
    v_r14 = (v_r14) + (a1);
    goto loc_00339197;
loc_00339417:
    v_stack_p118 = (unsigned int)(a32);
    result = KeBugCheckEx(26, (unsigned int)(0x5180ULL), a25, (unsigned int)(a32));
loc_0033942F:
    if (condition_is_below) goto loc_00338FDD;
    goto loc_00338FB9;
loc_0033943F:
    if (v_rbx >= ((unsigned int)(a32))) goto loc_003394CC;
loc_0033944B:
    goto loc_00339329;
loc_00339455:
    if ((v_r12 + a1 * 1) >= v_rdi) goto loc_00339544;
loc_0033946B:
    goto loc_003390BC;
loc_00339475:
    if (a25 < (*(unsigned __int64 *)(v_rdi + 16))) goto loc_0033906A;
    goto loc_00339037;
loc_00339488:
    a1 = (a8) - ((unsigned int)(a32));
    a1 = (a1) >> (4);
    a1 = (a1) * ((unsigned int)(a32));
    result = MiPageToChannel(a1, a25 + 1, a25, (unsigned int)(a32));
    goto loc_00339341;
loc_003394B3:
    v_r12 = (v_r12) >> (4);
    v_r12 = (v_r12) * (v_r14);
    result = MiPageToChannel(v_r12, a25 + 1, (unsigned __int8)(result), (unsigned int)(a32));
    goto loc_003390D1;
loc_003394CC:
    a1 = (*(unsigned __int64 *)(v_rip + 11487245) + *(unsigned __int64 *)(v_rip + 11487245) * 2) << (4);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 11487245));
    if (5 >= a1) goto loc_0033944B;
    a1 = (5) - ((unsigned int)(a32));
    a1 = (a1) >> (4);
    a1 = (a1) * ((unsigned int)(a32));
    result = MiIsDecayPfn(a1, a25 + 1, (unsigned __int8)(result), (unsigned int)(a32));
    if ((unsigned int)(result) != 0) goto loc_0033944B;
    a3 = (unsigned int)(((unsigned __int8)(result)) >> (16));
    a3 = (unsigned __int8)((a3) & (7));
    if (((unsigned __int8)(a3)) == 6) goto loc_00339321;
    result = MiGetPfnSlabType(5, a25 + 1, a3, (unsigned int)(a32));
    if (((unsigned int)(result)) != 9) goto loc_00339321;
    goto loc_0033944B;
loc_00339544:
    a1 = (*(unsigned __int64 *)(v_rip + 11487125) + *(unsigned __int64 *)(v_rip + 11487125) * 2) << (4);
    a1 = (a1) + (a25 + 1);
    if ((v_r12 + a1 * 1) >= a1) goto loc_0033946B;
    a1 = (v_r12) >> (4);
    a1 = (a1) * (v_r14);
    result = MiIsDecayPfn(a1, a25 + 1, a3, (unsigned int)(a32));
    if ((unsigned int)(result) != 0) goto loc_0033946B;
    a3 = (unsigned int)((a3) >> (16));
    a3 = (unsigned __int8)((a3) & (7));
    if (((unsigned __int8)(a3)) == 6) goto loc_003390B1;
    result = MiGetPfnSlabType(v_r12 + a1 * 1, a25 + 1, a3, (unsigned int)(a32));
    if (((unsigned int)(result)) != 9) goto loc_003390B1;
    goto loc_003390BC;
loc_003395AF:
    v_stack_p118 = (unsigned int)(a32);
    result = KeBugCheckEx(26, (unsigned int)(0x5180ULL), a25, result);
loc_003395D3:
    goto loc_00338FBC;
loc_003395DF:
    a1 = (unsigned int)(((unsigned int)(a35)) + 1);
    v_stack_p210 = (unsigned int)(a1);
    result = (unsigned int)(a34);
    if (((unsigned int)(a1)) == 8) { result = 1; }
    v_stack_p208 = (unsigned int)(result);
loc_00339608:
    v_rdi = (unsigned int)((v_rdi) - 1);
    v_rbx = (unsigned int)((result - 4) - 1);
    a4 = 0;
    goto loc_00338EA1;
loc_0033962D:
    a1 = (unsigned int)((unsigned int)(v_r12));
    if (0 == 8) { a1 = a15; }
    a1 = (a1) * ((int)(0));
    v_r14 = (a6 + (unsigned __int8)(a1) * 8) << (9);
    a1 = (a1) + (a25);
    v_r14 = (v_r14) + (*(unsigned __int64 *)(a1 + (unsigned int)(0x5180ULL) * 1 + 15760));
    goto loc_00339197;
loc_00339661:
    v_stack_p1F8 = (unsigned int)((unsigned int)(0x5180ULL) - 1);
    goto loc_00338F36;
loc_00339672:
    v_stack_p1A0 = 0;
    a2 = 0;
    a2 = (a2) * ((unsigned int)((unsigned int)(v_rbx)) + 0 * 8);
    a1 = ((unsigned int)((unsigned int)(v_rbx)) + 0 * 8) * ((int)((unsigned int)(v_r12)));
    a2 = (a2) + (*(unsigned __int64 *)(a1 + a4 * 1 + 15768));
    v_stack_p188 = a2;
    goto loc_00339395;
loc_003396B2:
    v_stack_p170 = 0;
    a2 = 0;
    a2 = (a2) * ((unsigned int)((unsigned int)(v_rbx)) + 0 * 8);
    a1 = ((unsigned int)((unsigned int)(v_rbx)) + 0 * 8) * (0);
    a2 = (a2) + (*(unsigned __int64 *)(a1 + (unsigned int)(0x5180ULL) - 1 * 1 + 15768));
    v_stack_p158 = a2;
    goto loc_00339127;
loc_003396EA:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13161416)))) & (64)) == 0) goto loc_003393F0;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, a2, (unsigned int)(0x5180ULL) - 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_003393F0;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r12)), a2, (unsigned int)(0x5180ULL) - 1, a4);
    goto loc_003393F2;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00338E63(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, uint64_t Arg9, void *Arg10, uint64_t Arg11, uint64_t Arg12, void *Arg13, uint64_t Arg14, uint8_t Arg15, void *Arg16, uint64_t Arg17, uint64_t Arg18, uint32_t Arg19, uint64_t Arg20, uint64_t Arg21, int64_t Arg22, uint64_t Arg23, int64_t Arg24, int64_t Arg25, uint64_t Arg26, uint64_t Arg27, uint64_t Arg28, uint64_t Arg29, uint64_t Arg30, uint64_t Arg31, void *Arg32, void *Arg33, uint8_t Arg34, uint32_t Arg35)
{
    uint8_t *arg10 = (uint8_t *)Arg10;
    uint8_t *arg13 = (uint8_t *)Arg13;
    uint8_t *arg16 = (uint8_t *)Arg16;
    uint8_t *arg32 = (uint8_t *)Arg32;
    uint8_t *arg33 = (uint8_t *)Arg33;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p100;
    uint32_t v_stack_p118;
    uint64_t v_stack_p128;
    uint64_t v_stack_p130;
    uint64_t v_stack_p138;
    uint32_t v_stack_p140;
    uint8_t v_stack_p143;
    uint64_t v_stack_p148;
    uint64_t v_stack_p150;
    uint64_t v_stack_p158;
    uint32_t v_stack_p160;
    uint32_t v_stack_p164;
    uint8_t v_stack_p168;
    uint32_t v_stack_p16C;
    uint8_t v_stack_p170;
    uint64_t v_stack_p178;
    uint64_t v_stack_p180;
    uint64_t v_stack_p188;
    uint32_t v_stack_p190;
    uint32_t v_stack_p194;
    uint8_t v_stack_p198;
    uint16_t v_stack_p199;
    uint8_t v_stack_p19B;
    uint32_t v_stack_p19C;
    uint64_t v_stack_p1A0;
    uint64_t v_stack_p1A8;
    uint32_t v_stack_p1F8;
    uint64_t v_stack_p20;
    uint32_t v_stack_p208;
    uint8_t v_stack_p20B;
    uint32_t v_stack_p210;
    uint64_t v_stack_p60;
    uint64_t v_stack_p70;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pC8;

    v_stack_pC8 = local_rsi;
    v_stack_pC0 = local_r14;
loc_00338E80:
    if (((uint32_t)((uint32_t)(Arg4))) >= 64) goto loc_003395D3;
    if ((*(uint64_t *)((uint32_t)((uint32_t)(local_rbx)) * 8 + local_r15 * 1 + 0x1E40)) != -1) goto loc_00338EAA;
loc_00338EA1:
    local_rdi = (uint32_t)(((uint32_t)(Arg4)) + 1);
    local_rbx = (uint32_t)((local_rbx) + 1);
    local_rbx = (uint32_t)((local_rbx) & (63));
    goto loc_00338E80;
loc_00338EAA:
    local_r12 = (*(uint64_t *)((uint32_t)((uint32_t)(local_rbx)) * 8 + local_r15 * 1 + 0x1E40) + *(uint64_t *)((uint32_t)((uint32_t)(local_rbx)) * 8 + local_r15 * 1 + 0x1E40) * 2) << (4);
    v_stack_p100 = local_r12;
loc_00338EC4:
    if (condition_is_below) goto loc_003393E0;
    if ((*(uint64_t *)((uint32_t)((uint32_t)(local_rbx)) * 8 + local_r15 * 1 + 0x1E40)) != (*(uint64_t *)((uint32_t)((uint32_t)(local_rbx)) * 8 + local_r15 * 1 + 0x1E40))) goto loc_00339608;
    Arg1 = (Arg32) >> (4);
    Arg1 = (Arg1) * (*(uint64_t *)((uint32_t)((uint32_t)(local_rbx)) * 8 + local_r15 * 1 + 0x1E40));
    Arg1 = (Arg1) >> (9);
    if ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xB0432D) + Arg1 * 2)) != 0) goto loc_00339661;
    v_stack_p100 = 9;
loc_00338F36:
    v_stack_p20 = Arg33;
    result = MiAcquirePageListLock(Arg8, local_r12 + Arg1 * 1, (uint32_t)(Arg32), (uint32_t)(Arg34));
    if ((uint32_t)(result) == 0) goto loc_003395DF;
    v_stack_p118 = (uint32_t)(*(uint8_t *)(arg33));
    v_stack_p60 = v_xmm0;
    v_stack_p70 = v_xmm1;
    if ((*(uint64_t *)((uint32_t)((uint32_t)(local_rbx)) * 8 + local_r15 * 1 + 0x1E40)) < (*(uint64_t *)(v_rip + 0xAFCC88))) goto loc_00338F98;
    result = (*(uint64_t *)(v_rip + 0xAFCC88)) + (0x800ULL);
loc_00338F98:
    if ((*(uint64_t *)((uint32_t)((uint32_t)(local_rbx)) * 8 + local_r15 * 1 + 0x1E40)) >= result) goto loc_0033942F;
    if ((((uint8_t)(*(uint64_t *)(arg32 + local_r15 * 1))) & (8)) != 0) goto loc_00338FDD;
loc_00338FB9:
loc_00338FBC:
    local_rsp = (local_rsp) + (208);
    return *(uint64_t *)((uint32_t)((uint32_t)(local_rbx)) * 8 + local_r15 * 1 + 0x1E40);
loc_00338FDD:
    result = (*(uint64_t *)(local_r12 + Arg1 * 1 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_p150 = local_r12 + Arg1 * 1;
    v_stack_p148 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xAF709C) + result * 8);
    if (((uint32_t)((int32_t)(*(uint32_t *)(v_rip + 0xAF4BB6)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAF4BB4))))) goto loc_00339031;
    result = ((int32_t)(*(uint32_t *)(v_rip + 0xAF4BB6))) << (4);
    result = (result) + (*(uint64_t *)(v_rip + 0xAF4BFE));
    if (Arg25 < (*(uint64_t *)(result))) goto loc_00339031;
    if (((uint32_t)((int32_t)(*(uint32_t *)(v_rip + 0xAF4BB6)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAF4BB4))))) goto loc_00339071;
    if (Arg25 < (*(uint64_t *)(result + 0x10))) goto loc_00339071;
loc_00339031:
    Arg4 = 0;
loc_00339037:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAF4BB4)))) < 0) goto loc_00339417;
    Arg3 = (uint32_t)((0 + (uint32_t)(*(uint32_t *)(v_rip + 0xAF4BB4)) * 1) >> (1));
    result = ((int32_t)((uint32_t)(Arg3))) << (4);
    result = (result) + (*(uint64_t *)(v_rip + 0xAF4BCC));
    if (Arg25 < (*(uint64_t *)(result))) goto loc_003395AF;
    if (((uint32_t)(Arg3)) != (*(uint32_t *)(v_rip + 0xAF4B60))) goto loc_00339475;
loc_0033906A:
    *(uint32_t *)(v_rip + 0xAF4B4F) = (uint32_t)(Arg3);
loc_00339071:
    v_stack_p160 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r12 + Arg1 * 1 + 0x20))) >> (24));
    v_stack_p208 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + Arg1 * 1 + 0x20)));
    if ((((uint8_t)(result)) & (8)) != 0) goto loc_00339455;
loc_003390B1:
    local_rbx = (uint32_t)((v_stack_p20B) & (7));
loc_003390BC:
    v_stack_p164 = (uint32_t)(local_rbx);
    if ((*(uint64_t *)(v_rip + 0xAF4B64)) != 0) goto loc_003394B3;
    local_r11 = 0;
loc_003390D1:
    Arg3 = ((uint32_t)(*(uint32_t *)(local_r12 + Arg1 * 1 + 0x20))) * ((uint32_t)(Arg13));
    v_stack_p208 = 0;
    v_stack_p168 = 0;
    v_stack_p16C = (uint32_t)((int32_t)(Arg32));
    Arg3 = (Arg3) + (*(uint64_t *)(arg10 + 0x10));
    if (((uint32_t)((int32_t)(Arg32))) < 9) goto loc_003396B2;
    Arg1 = (0 * 8 + 59) + ((uint32_t)((uint32_t)(local_rbx)));
    result = (0) * (Arg1);
    result = (result) + (Arg3);
    v_stack_p158 = result;
loc_00339127:
    local_r12 = 0;
    Arg3 = (Arg3) * ((uint32_t)(Arg13));
    v_stack_p128 = (uint32_t)((uint32_t)(local_rbx));
    v_stack_p130 = Arg3;
    v_stack_p1A8 = Arg10 + 16;
loc_00339160:
    if (0 == 0) goto loc_00339401;
    if (0 == 1) goto loc_003393C9;
    if (((uint32_t)((int32_t)(Arg32))) < 9) goto loc_0033962D;
    local_r14 = (0 * 8 + 13) + ((uint32_t)((uint32_t)(local_rbx)));
    local_r14 = (local_r14) << (9);
    local_r14 = (local_r14) + (Arg3);
    local_r14 = (local_r14) + (*(uint64_t *)(arg10 + 0x10));
loc_00339197:
loc_0033919D:
    if ((*(uint64_t *)(local_r14)) == Arg25) goto loc_003391DB;
    local_rbx = (uint32_t)((0) + 1);
    Arg1 = (local_r14) + (8);
    if (((uint32_t)(local_rbx)) < 64) goto loc_0033919D;
    if (((uint32_t)((uint32_t)((uint32_t)(local_rbx)))) != 64) goto loc_003391DB;
loc_003391B7:
    local_rdi = (uint32_t)((0) + 1);
    if (((uint32_t)(local_rdi)) >= 3) goto loc_00338FB9;
    goto loc_00339160;
loc_003391DB:
    v_stack_p118 = (uint32_t)((uint32_t)(Arg35));
    result = MiFindSuitableLookasideReplacement((uint32_t)((uint32_t)(local_rdi)), local_r14, (uint32_t)((uint32_t)(local_rbx)), local_r12 + Arg1 * 1);
    if ((uint32_t)(result) != 0) goto loc_003393A9;
    *(uint64_t *)(local_r14 + (uint32_t)((uint32_t)(local_rbx)) * 8) = -1;
    if ((*(uint64_t *)(local_r14 + (uint32_t)((uint32_t)(local_rbx)) * 8)) == -1) goto loc_003393A9;
    if ((*(uint64_t *)(local_r14 + (uint32_t)((uint32_t)(local_rbx)) * 8)) < (*(uint64_t *)(v_rip + 0xAFC9E3))) goto loc_00339232;
    if ((*(uint64_t *)(local_r14 + (uint32_t)((uint32_t)(local_rbx)) * 8)) < (*(uint64_t *)(v_rip + 0xAFC9E3) + 2048)) goto loc_003393A9;
loc_00339232:
    v_stack_p199 = 0;
    local_r14 = (*(uint64_t *)(local_r14 + (uint32_t)((uint32_t)(local_rbx)) * 8) + *(uint64_t *)(local_r14 + (uint32_t)((uint32_t)(local_rbx)) * 8) * 2) + (*(uint64_t *)(local_r14 + (uint32_t)((uint32_t)(local_rbx)) * 8) + *(uint64_t *)(local_r14 + (uint32_t)((uint32_t)(local_rbx)) * 8) * 2);
    v_stack_p19B = 0;
    v_stack_p1A0 = 0;
    local_r15 = -9;
    if (condition_is_above_or_equal) { local_r15 = 0xFFFFFFFFF7FFFFFFULL; }
    local_r15 = (local_r15) & (*(uint64_t *)(local_r15 + local_r14 * 8));
    v_stack_p138 = 0xFFFFFFFFF7FFFFFFULL + local_r14 * 8;
    if ((*(uint64_t *)(local_r14 + (uint32_t)((uint32_t)(local_rbx)) * 8)) < (*(uint64_t *)(v_rip + 0xAFC9E3))) goto loc_0033929E;
loc_0033929E:
    result = MiGetPfnSlabType(0xFFFFFFFFF7FFFFFFULL + local_r14 * 8, *(uint64_t *)(v_rip + 0xAFC9E3), (uint32_t)((uint32_t)(local_rbx)), local_r12 + Arg1 * 1);
    v_stack_p180 = 0xFFFFFFFFF7FFFFFFULL + local_r14 * 8;
    Arg2 = (*(uint64_t *)(result + local_r14 * 8)) >> (43);
    Arg2 = (uint32_t)((Arg2) & (0x3FFULL));
    v_stack_p178 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xAF6DBC) + Arg2 * 8);
    result = MiPageToNode(*(uint64_t *)(local_r14 + (uint32_t)((uint32_t)(local_rbx)) * 8), Arg2, *(uint64_t *)(v_rip + 0xAF6DBC), *(uint64_t *)(*(uint64_t *)(v_rip + 0xAF6DBC) + Arg2 * 8));
    v_stack_p190 = (uint32_t)(result);
    v_stack_p140 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r14 + (uint32_t)((uint32_t)(local_rbx)) * 8) + local_r14 * 8)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r14 + (uint32_t)((uint32_t)(local_rbx)) * 8) + local_r14 * 8))) >> (24));
    if ((((uint8_t)(Arg1)) & (8)) != 0) goto loc_0033943F;
loc_00339321:
    local_rbx = (uint32_t)((v_stack_p143) & (7));
loc_00339329:
    v_stack_p194 = (uint32_t)(local_rbx);
    if ((*(uint64_t *)(v_rip + 0xAF48F7)) != 0) goto loc_00339488;
    Arg3 = 0;
loc_00339341:
    Arg4 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xAF6DBC) + Arg2 * 8)) * ((uint32_t)(Arg19));
    v_stack_p198 = 0;
    v_stack_p19C = (uint32_t)((uint32_t)((uint32_t)(result)));
    Arg4 = (Arg4) + (*(uint64_t *)(arg16 + 0x10));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) < 9) goto loc_00339672;
    Arg1 = (0 * 8 + 59) + ((uint32_t)((uint32_t)(local_rbx)));
    result = ((uint32_t)((uint32_t)(local_rbx))) * (Arg1);
    result = (result) + (Arg4);
    v_stack_p188 = result;
loc_00339395:
    *(uint64_t *)(result + local_r14 * 8) = local_r15;
    local_r12 = 0;
loc_003393A9:
    goto loc_003391B7;
loc_003393C9:
    local_r14 = (Arg6) << (9);
    local_r14 = (local_r14) + (0x2E40ULL);
    local_r14 = (local_r14) + (Arg1);
    goto loc_00339197;
loc_003393E0:
    local_r12 = (uint32_t)((local_r12) + 1);
    if (((*(uint32_t *)(v_rip + 0xC8BEC2)) & ((uint32_t)(local_r12))) == 0) goto loc_003396EA;
loc_003393F0:
loc_003393F2:
    if (!sign_flag) goto loc_00338EC4;
    goto loc_003393E0;
loc_00339401:
    local_r14 = (Arg6) << (9);
    local_r14 = (local_r14) + (0x1E40ULL);
    local_r14 = (local_r14) + (Arg1);
    goto loc_00339197;
loc_00339417:
    v_stack_p118 = (uint32_t)(Arg32);
    result = KeBugCheckEx(26, (uint32_t)(0x5180ULL), Arg25, (uint32_t)(Arg32));
loc_0033942F:
    if (condition_is_below) goto loc_00338FDD;
    goto loc_00338FB9;
loc_0033943F:
    if (local_rbx >= ((uint32_t)(Arg32))) goto loc_003394CC;
loc_0033944B:
    goto loc_00339329;
loc_00339455:
    if ((local_r12 + Arg1 * 1) >= local_rdi) goto loc_00339544;
loc_0033946B:
    goto loc_003390BC;
loc_00339475:
    if (Arg25 < (*(uint64_t *)(local_rdi + 0x10))) goto loc_0033906A;
    goto loc_00339037;
loc_00339488:
    Arg1 = (Arg8) - ((uint32_t)(Arg32));
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * ((uint32_t)(Arg32));
    result = MiPageToChannel(Arg1, Arg25 + 1, Arg25, (uint32_t)(Arg32));
    goto loc_00339341;
loc_003394B3:
    local_r12 = (local_r12) >> (4);
    local_r12 = (local_r12) * (local_r14);
    result = MiPageToChannel(local_r12, Arg25 + 1, (uint8_t)(result), (uint32_t)(Arg32));
    goto loc_003390D1;
loc_003394CC:
    Arg1 = (*(uint64_t *)(v_rip + 0xAF480D) + *(uint64_t *)(v_rip + 0xAF480D) * 2) << (4);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xAF480D));
    if (5 >= Arg1) goto loc_0033944B;
    Arg1 = (5) - ((uint32_t)(Arg32));
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * ((uint32_t)(Arg32));
    result = MiIsDecayPfn(Arg1, Arg25 + 1, (uint8_t)(result), (uint32_t)(Arg32));
    if ((uint32_t)(result) != 0) goto loc_0033944B;
    Arg3 = (uint32_t)(((uint8_t)(result)) >> (16));
    Arg3 = (uint8_t)((Arg3) & (7));
    if (((uint8_t)(Arg3)) == 6) goto loc_00339321;
    result = MiGetPfnSlabType(5, Arg25 + 1, Arg3, (uint32_t)(Arg32));
    if (((uint32_t)(result)) != 9) goto loc_00339321;
    goto loc_0033944B;
loc_00339544:
    Arg1 = (*(uint64_t *)(v_rip + 0xAF4795) + *(uint64_t *)(v_rip + 0xAF4795) * 2) << (4);
    Arg1 = (Arg1) + (Arg25 + 1);
    if ((local_r12 + Arg1 * 1) >= Arg1) goto loc_0033946B;
    Arg1 = (local_r12) >> (4);
    Arg1 = (Arg1) * (local_r14);
    result = MiIsDecayPfn(Arg1, Arg25 + 1, Arg3, (uint32_t)(Arg32));
    if ((uint32_t)(result) != 0) goto loc_0033946B;
    Arg3 = (uint32_t)((Arg3) >> (16));
    Arg3 = (uint8_t)((Arg3) & (7));
    if (((uint8_t)(Arg3)) == 6) goto loc_003390B1;
    result = MiGetPfnSlabType(local_r12 + Arg1 * 1, Arg25 + 1, Arg3, (uint32_t)(Arg32));
    if (((uint32_t)(result)) != 9) goto loc_003390B1;
    goto loc_003390BC;
loc_003395AF:
    v_stack_p118 = (uint32_t)(Arg32);
    result = KeBugCheckEx(26, (uint32_t)(0x5180ULL), Arg25, result);
loc_003395D3:
    goto loc_00338FBC;
loc_003395DF:
    Arg1 = (uint32_t)(((uint32_t)(Arg35)) + 1);
    v_stack_p210 = (uint32_t)(Arg1);
    result = (uint32_t)(Arg34);
    if (((uint32_t)(Arg1)) == 8) { result = 1; }
    v_stack_p208 = (uint32_t)(result);
loc_00339608:
    local_rdi = (uint32_t)((local_rdi) - 1);
    local_rbx = (uint32_t)((result - 4) - 1);
    Arg4 = 0;
    goto loc_00338EA1;
loc_0033962D:
    Arg1 = (uint32_t)((uint32_t)(local_r12));
    if (0 == 8) { Arg1 = Arg15; }
    Arg1 = (Arg1) * ((int32_t)(0));
    local_r14 = (Arg6 + (uint8_t)(Arg1) * 8) << (9);
    Arg1 = (Arg1) + (Arg25);
    local_r14 = (local_r14) + (*(uint64_t *)(Arg1 + (uint32_t)(0x5180ULL) * 1 + 0x3D90));
    goto loc_00339197;
loc_00339661:
    v_stack_p1F8 = (uint32_t)((uint32_t)(0x5180ULL) - 1);
    goto loc_00338F36;
loc_00339672:
    v_stack_p1A0 = 0;
    Arg2 = 0;
    Arg2 = (Arg2) * ((uint32_t)((uint32_t)(local_rbx)) + 0 * 8);
    Arg1 = ((uint32_t)((uint32_t)(local_rbx)) + 0 * 8) * ((int32_t)((uint32_t)(local_r12)));
    Arg2 = (Arg2) + (*(uint64_t *)(Arg1 + Arg4 * 1 + 0x3D98));
    v_stack_p188 = Arg2;
    goto loc_00339395;
loc_003396B2:
    v_stack_p170 = 0;
    Arg2 = 0;
    Arg2 = (Arg2) * ((uint32_t)((uint32_t)(local_rbx)) + 0 * 8);
    Arg1 = ((uint32_t)((uint32_t)(local_rbx)) + 0 * 8) * (0);
    Arg2 = (Arg2) + (*(uint64_t *)(Arg1 + (uint32_t)(0x5180ULL) - 0x1 * 1 + 0x3D98));
    v_stack_p158 = Arg2;
    goto loc_00339127;
loc_003396EA:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC8D3C8)))) & (64)) == 0) goto loc_003393F0;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, Arg2, (uint32_t)(0x5180ULL) - 1, Arg4);
    if ((uint8_t)(result) == 0) goto loc_003393F0;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r12)), Arg2, (uint32_t)(0x5180ULL) - 1, Arg4);
    goto loc_003393F2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg10` | `+ 0x10` | `64` | `R` |
| `Arg13` | `+ 0x0 + rax*1` | `32` | `R` |
| `Arg16` | `+ 0x10` | `64` | `R` |
| `Arg32` | `+ 0x0 + rax*1` | `64` | `R` |
| `Arg33` | `+ 0x0` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00338E63&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
