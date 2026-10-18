# sub_00241476

- RVA: `0x00241476`–`0x002419FE` (길이 `1,416` bytes)
- VA: `0x0000000140241476`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00061830`
- 디코드: `327`개 명령, `1,416/1,416` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x002414A4` → [MiGetProcessorFlushList](MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x00241634` → [MiGetVaAge](MiGetVaAge_function_00240AC0.md) (function, `0x00240AC0`)
- `0x00241644` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00241677` → [MiLogPageAccess](MiLogPageAccess_function_00240870.md) (function, `0x00240870`)
- `0x0024170D` → [MiPteHasShadow](../32/MiPteHasShadow_function_0032B998.md) (function, `0x0032B998`)
- `0x00241836` → [MiDemoteCombinedPte](../22/MiDemoteCombinedPte_function_0022ABAC.md) (function, `0x0022ABAC`)
- `0x002418A6` → [MiIsPageTableLocked](../22/MiIsPageTableLocked_function_0022A5B0.md) (function, `0x0022A5B0`)
- `0x00241960` → [qsort](../50/qsort_function_005009F0.md) (function, `0x005009F0`)
- `0x00241968` → [MiCompressTbFlushList](../2A/MiCompressTbFlushList_function_002A93A8.md) (function, `0x002A93A8`)
- `0x002419E4` → [MiGetPagePrivilege](../28/MiGetPagePrivilege_function_00285420.md) (function, `0x00285420`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0024160B` → RVA `0x00E30088` (`.data`; read)
- `0x0024184B` → RVA `0x00E38D00` (`.data`; read)
- `0x00241907` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00241953` → RVA `0x00695890` (`MiTbFlushSort`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **10**
  - `0x002416F2` → [sub_00241A0C + 0x15](Unknown_function_00241A0C.md) (`tail-transfer`)
  - `0x002417A7` → [sub_00241415 + 0x1A](Unknown_function_00241415.md) (`tail-transfer`)
  - `0x0024187A` → [sub_00241415 + 0x30](Unknown_function_00241415.md) (`tail-transfer`)
  - `0x0024189A` → [sub_00241415 + 0x30](Unknown_function_00241415.md) (`tail-transfer`)
  - `0x002418B3` → [sub_00241415 + 0x30](Unknown_function_00241415.md) (`tail-transfer`)
  - `0x00241933` → [sub_00241415 + 0x1A](Unknown_function_00241415.md) (`tail-transfer`)
  - `0x0024193D` → [sub_00241415 + 0x1A](Unknown_function_00241415.md) (`tail-transfer`)
  - `0x00241946` → [sub_00241415 + 0x1A](Unknown_function_00241415.md) (`tail-transfer`)
  - `0x002419A4` → [sub_00241415](Unknown_function_00241415.md) (`tail-transfer`)
  - `0x002419B2` → [sub_00241A0C](Unknown_function_00241A0C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00241476  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
0024147B  48 8B 5E 08                     mov rbx, qword ptr [rsi + 8]
0024147F  48 89 6C 24 60                  mov qword ptr [rsp + 0x60], rbp
00241484  BD 01 00 00 00                  mov ebp, 1
00241489  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
0024148E  45 33 E4                        xor r12d, r12d
00241491  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00241496  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0024149B  48 85 DB                        test rbx, rbx
0024149E  0F 85 93 00 00 00               jne 0x140241537
002414A4  E8 E7 17 00 00                  call 0x140242c90
002414A9  48 8D 98 28 10 00 00            lea rbx, [rax + 0x1028]
002414B0  C7 43 10 02 00 00 00            mov dword ptr [rbx + 0x10], 2
002414B7  89 6B 14                        mov dword ptr [rbx + 0x14], ebp
002414BA  48 89 3B                        mov qword ptr [rbx], rdi
002414BD  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
002414C3  C1 E8 08                        shr eax, 8
002414C6  C0 E8 03                        shr al, 3
002414C9  40 22 C5                        and al, bpl
002414CC  88 43 18                        mov byte ptr [rbx + 0x18], al
002414CF  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
002414D5  A8 0F                           test al, 0xf
002414D7  75 20                           jne 0x1402414f9
002414D9  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002414E2  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
002414E9  48 81 C1 00 04 00 00            add rcx, 0x400
002414F0  48 3B F9                        cmp rdi, rcx
002414F3  0F 85 7F 04 00 00               jne 0x140241978
002414F9  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
002414FF  41 8B CC                        mov ecx, r12d
00241502  A8 0F                           test al, 0xf
00241504  0F 44 CD                        cmove ecx, ebp
00241507  83 63 10 DB                     and dword ptr [rbx + 0x10], 0xffffffdb
0024150B  49 BA FF FF FF FF FF 00 00 00   movabs r10, 0xffffffffff
00241515  89 4B 08                        mov dword ptr [rbx + 8], ecx
00241518  66 44 89 63 19                  mov word ptr [rbx + 0x19], r12w
0024151D  44 89 63 1C                     mov dword ptr [rbx + 0x1c], r12d
00241521  4C 89 63 20                     mov qword ptr [rbx + 0x20], r12
00241525  4C 89 63 28                     mov qword ptr [rbx + 0x28], r12
00241529  48 89 5E 08                     mov qword ptr [rsi + 8], rbx
0024152D  49 B9 00 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000000
00241537  44 8B 3E                        mov r15d, dword ptr [rsi]
0024153A  49 8B F6                        mov rsi, r14
0024153D  48 C1 E6 19                     shl rsi, 0x19
00241541  41 83 E7 04                     and r15d, 4
00241545  49 BD 00 00 00 00 80 F6 FF FF   movabs r13, 0xfffff68000000000
0024154F  49 8B C5                        mov rax, r13
00241552  4D 8B 06                        mov r8, qword ptr [r14]
00241555  48 C1 E0 19                     shl rax, 0x19
00241559  48 2B F0                        sub rsi, rax
0024155C  48 C1 FE 10                     sar rsi, 0x10
00241560  48 B8 00 D0 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed000
0024156A  4C 3B F0                        cmp r14, rax
0024156D  72 2D                           jb 0x14024159c
0024156F  48 B8 F8 D7 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed7f8
00241579  4C 3B F0                        cmp r14, rax
0024157C  77 1E                           ja 0x14024159c
0024157E  49 8B D0                        mov rdx, r8
00241581  44 84 C5                        test bpl, r8b
00241584  74 16                           je 0x14024159c
00241586  41 F6 C0 42                     test r8b, 0x42
0024158A  0F 95 C1                        setne cl
0024158D  41 F6 C0 20                     test r8b, 0x20
00241591  0F 95 C0                        setne al
00241594  84 C8                           test al, cl
00241596  0F 84 71 01 00 00               je 0x14024170d
0024159C  49 C1 E8 0C                     shr r8, 0xc
002415A0  4D 23 C2                        and r8, r10
002415A3  4B 8D 2C 40                     lea rbp, [r8 + r8*2]
002415A7  48 C1 E5 04                     shl rbp, 4
002415AB  49 8B C1                        mov rax, r9
002415AE  48 03 E8                        add rbp, rax
002415B1  49 8B C5                        mov rax, r13
002415B4  48 B9 FF FF FF FF FF F6 FF FF   movabs rcx, 0xfffff6ffffffffff
002415BE  48 3B F0                        cmp rsi, rax
002415C1  0F 83 F1 02 00 00               jae 0x1402418b8
002415C7  41 8B CC                        mov ecx, r12d
002415CA  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
002415D0  85 C9                           test ecx, ecx
002415D2  0F 85 AD 02 00 00               jne 0x140241885
002415D8  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
002415DC  48 0F BA E0 28                  bt rax, 0x28
002415E1  0F 83 1E 02 00 00               jae 0x140241805
002415E7  8B 45 20                        mov eax, dword ptr [rbp + 0x20]
002415EA  66 83 F8 01                     cmp ax, 1
002415EE  0F 87 7E 02 00 00               ja 0x140241872
002415F4  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
002415FA  24 0F                           and al, 0xf
002415FC  3C 01                           cmp al, 1
002415FE  0F 84 47 02 00 00               je 0x14024184b
00241604  0F B7 8F AE 00 00 00            movzx ecx, word ptr [rdi + 0xae]
0024160B  48 8B 05 76 EA BE 00            mov rax, qword ptr [rip + 0xbeea76]
00241612  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
00241616  8B 80 2C 44 00 00               mov eax, dword ptr [rax + 0x442c]
0024161C  85 C0                           test eax, eax
0024161E  74 5C                           je 0x14024167c
00241620  BD FF FF FF FF                  mov ebp, 0xffffffff
00241625  49 8B C5                        mov rax, r13
00241628  48 3B F0                        cmp rsi, rax
0024162B  0F 83 26 02 00 00               jae 0x140241857
00241631  48 8B D6                        mov rdx, rsi
00241634  E8 87 F4 FF FF                  call 0x140240ac0
00241639  0F B6 E8                        movzx ebp, al
0024163C  83 FD 07                        cmp ebp, 7
0024163F  74 3B                           je 0x14024167c
00241641  49 8B CE                        mov rcx, r14
00241644  E8 57 12 04 00                  call 0x1402828a0
00241649  A8 20                           test al, 0x20
0024164B  74 2F                           je 0x14024167c
0024164D  8B 8F B8 00 00 00               mov ecx, dword ptr [rdi + 0xb8]
00241653  F6 C1 0F                        test cl, 0xf
00241656  0F 85 AB 02 00 00               jne 0x140241907
0024165C  41 8B CC                        mov ecx, r12d
0024165F  48 39 8F 70 02 00 00            cmp qword ptr [rdi + 0x270], rcx
00241666  0F 95 C1                        setne cl
00241669  85 C9                           test ecx, ecx
0024166B  0F 85 38 03 00 00               jne 0x1402419a9
00241671  49 8B D6                        mov rdx, r14
00241674  48 8B CF                        mov rcx, rdi
00241677  E8 F4 F1 FF FF                  call 0x140240870
0024167C  BD 01 00 00 00                  mov ebp, 1
00241681  39 6B 08                        cmp dword ptr [rbx + 8], ebp
00241684  0F 85 44 02 00 00               jne 0x1402418ce
0024168A  45 8B F4                        mov r14d, r12d
0024168D  44 8B 4B 1C                     mov r9d, dword ptr [rbx + 0x1c]
00241691  45 85 C9                        test r9d, r9d
00241694  0F 84 00 01 00 00               je 0x14024179a
0024169A  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
0024169D  A8 02                           test al, 2
0024169F  0F 85 B0 00 00 00               jne 0x140241755
002416A5  41 8D 41 FF                     lea eax, [r9 - 1]
002416A9  4C 8D 14 C3                     lea r10, [rbx + rax*8]
002416AD  48 8B 44 C3 28                  mov rax, qword ptr [rbx + rax*8 + 0x28]
002416B2  48 A9 00 0C 00 00               test rax, 0xc00
002416B8  0F 85 DC 00 00 00               jne 0x14024179a
002416BE  4C 8B C0                        mov r8, rax
002416C1  48 8B C8                        mov rcx, rax
002416C4  41 81 E0 FF 03 00 00            and r8d, 0x3ff
002416CB  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
002416D2  49 8D 50 01                     lea rdx, [r8 + 1]
002416D6  48 C1 E2 0C                     shl rdx, 0xc
002416DA  48 03 D1                        add rdx, rcx
002416DD  48 3B D6                        cmp rdx, rsi
002416E0  75 16                           jne 0x1402416f8
002416E2  49 8D 0C 28                     lea rcx, [r8 + rbp]
002416E6  49 3B C8                        cmp rcx, r8
002416E9  76 0D                           jbe 0x1402416f8
002416EB  48 81 F9 FF 03 00 00            cmp rcx, 0x3ff
002416F2  0F 86 29 03 00 00               jbe 0x140241a21
002416F8  41 8D 49 FF                     lea ecx, [r9 - 1]
002416FC  48 8D 49 05                     lea rcx, [rcx + 5]
00241700  48 8B 04 CB                     mov rax, qword ptr [rbx + rcx*8]
00241704  4C 8D 14 CB                     lea r10, [rbx + rcx*8]
00241708  48 8B C8                        mov rcx, rax
0024170B  EB 6F                           jmp 0x14024177c
0024170D  E8 86 A2 0E 00                  call 0x14032b998
00241712  48 85 C0                        test rax, rax
00241715  0F 84 81 FE FF FF               je 0x14024159c
0024171B  48 8B 88 08 05 00 00            mov rcx, qword ptr [rax + 0x508]
00241722  48 85 C9                        test rcx, rcx
00241725  0F 84 71 FE FF FF               je 0x14024159c
0024172B  49 8B C6                        mov rax, r14
0024172E  48 C1 E8 03                     shr rax, 3
00241732  25 FF 01 00 00                  and eax, 0x1ff
00241737  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
0024173B  A8 20                           test al, 0x20
0024173D  74 04                           je 0x140241743
0024173F  48 83 CA 20                     or rdx, 0x20
00241743  4C 8B C2                        mov r8, rdx
00241746  49 83 C8 42                     or r8, 0x42
0024174A  A8 42                           test al, 0x42
0024174C  4C 0F 44 C2                     cmove r8, rdx
00241750  E9 47 FE FF FF                  jmp 0x14024159c
00241755  45 85 C9                        test r9d, r9d
00241758  74 40                           je 0x14024179a
0024175A  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
0024175D  A8 02                           test al, 2
0024175F  75 39                           jne 0x14024179a
00241761  41 8D 49 FF                     lea ecx, [r9 - 1]
00241765  48 8D 49 05                     lea rcx, [rcx + 5]
00241769  48 8B 04 CB                     mov rax, qword ptr [rbx + rcx*8]
0024176D  4C 8D 14 CB                     lea r10, [rbx + rcx*8]
00241771  48 8B C8                        mov rcx, rax
00241774  48 A9 00 0C 00 00               test rax, 0xc00
0024177A  75 1E                           jne 0x14024179a
0024177C  4C 8B DD                        mov r11, rbp
0024177F  48 8B D1                        mov rdx, rcx
00241782  49 C1 E3 0C                     shl r11, 0xc
00241786  48 81 E2 00 F0 FF FF            and rdx, 0xfffffffffffff000
0024178D  4E 8D 04 1E                     lea r8, [rsi + r11]
00241791  49 3B D0                        cmp rdx, r8
00241794  0F 84 EA 01 00 00               je 0x140241984
0024179A  44 3B 4B 0C                     cmp r9d, dword ptr [rbx + 0xc]
0024179E  0F 84 86 01 00 00               je 0x14024192a
002417A4  48 85 ED                        test rbp, rbp
002417A7  0F 84 82 FC FF FF               je 0x14024142f
002417AD  48 8D 45 FF                     lea rax, [rbp - 1]
002417B1  48 8B CE                        mov rcx, rsi
002417B4  48 3D FF 03 00 00               cmp rax, 0x3ff
002417BA  BA 00 04 00 00                  mov edx, 0x400
002417BF  48 0F 46 D5                     cmovbe rdx, rbp
002417C3  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
002417CA  48 8D 42 FF                     lea rax, [rdx - 1]
002417CE  25 FF 03 00 00                  and eax, 0x3ff
002417D3  48 0B C1                        or rax, rcx
002417D6  48 8B CA                        mov rcx, rdx
002417D9  4A 89 44 CB 28                  mov qword ptr [rbx + r9*8 + 0x28], rax
002417DE  44 8B 4B 1C                     mov r9d, dword ptr [rbx + 0x1c]
002417E2  48 01 53 20                     add qword ptr [rbx + 0x20], rdx
002417E6  41 FF C1                        inc r9d
002417E9  48 C1 E1 0C                     shl rcx, 0xc
002417ED  48 03 F1                        add rsi, rcx
002417F0  44 89 4B 1C                     mov dword ptr [rbx + 0x1c], r9d
002417F4  48 2B EA                        sub rbp, rdx
002417F7  74 AB                           je 0x1402417a4
002417F9  44 3B 4B 0C                     cmp r9d, dword ptr [rbx + 0xc]
002417FD  0F 84 87 FE FF FF               je 0x14024168a
00241803  EB 9F                           jmp 0x1402417a4
00241805  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
00241809  48 85 C0                        test rax, rax
0024180C  0F 88 D5 FD FF FF               js 0x1402415e7
00241812  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
00241816  48 85 C0                        test rax, rax
00241819  0F 84 C8 FD FF FF               je 0x1402415e7
0024181F  4C 8B 45 08                     mov r8, qword ptr [rbp + 8]
00241823  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
0024182D  4C 0B C0                        or r8, rax
00241830  49 8B D6                        mov rdx, r14
00241833  48 8B CF                        mov rcx, rdi
00241836  E8 71 93 FE FF                  call 0x14022abac
0024183B  85 C0                           test eax, eax
0024183D  0F 84 A4 FD FF FF               je 0x1402415e7
00241843  49 8B 06                        mov rax, qword ptr [r14]
00241846  E9 9C FD FF FF                  jmp 0x1402415e7
0024184B  48 8D 05 AE 74 BF 00            lea rax, [rip + 0xbf74ae]
00241852  E9 BF FD FF FF                  jmp 0x140241616
00241857  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
00241861  48 8B C0                        mov rax, rax
00241864  48 3B F0                        cmp rsi, rax
00241867  0F 86 D4 FD FF FF               jbe 0x140241641
0024186D  E9 BF FD FF FF                  jmp 0x140241631
00241872  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
00241878  A8 0F                           test al, 0xf
0024187A  0F 85 C5 FB FF FF               jne 0x140241445
00241880  E9 6F FD FF FF                  jmp 0x1402415f4
00241885  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
00241889  48 B9 FF FF FF FF FF FF FF 3F   movabs rcx, 0x3fffffffffffffff
00241893  48 23 C1                        and rax, rcx
00241896  48 83 F8 01                     cmp rax, 1
0024189A  0F 85 A5 FB FF FF               jne 0x140241445
002418A0  49 8B D6                        mov rdx, r14
002418A3  48 8B CF                        mov rcx, rdi
002418A6  E8 05 8D FE FF                  call 0x14022a5b0
002418AB  85 C0                           test eax, eax
002418AD  0F 84 25 FD FF FF               je 0x1402415d8
002418B3  E9 8D FB FF FF                  jmp 0x140241445
002418B8  48 8B C1                        mov rax, rcx
002418BB  B9 01 00 00 00                  mov ecx, 1
002418C0  48 3B F0                        cmp rsi, rax
002418C3  0F 87 FE FC FF FF               ja 0x1402415c7
002418C9  E9 FC FC FF FF                  jmp 0x1402415ca
002418CE  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
002418D1  F6 C1 04                        test cl, 4
002418D4  0F 85 B0 FD FF FF               jne 0x14024168a
002418DA  49 8B C5                        mov rax, r13
002418DD  48 3B F0                        cmp rsi, rax
002418E0  0F 82 A4 FD FF FF               jb 0x14024168a
002418E6  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
002418F0  48 8B C0                        mov rax, rax
002418F3  48 3B F0                        cmp rsi, rax
002418F6  0F 87 8E FD FF FF               ja 0x14024168a
002418FC  83 C9 04                        or ecx, 4
002418FF  89 4B 10                        mov dword ptr [rbx + 0x10], ecx
00241902  E9 83 FD FF FF                  jmp 0x14024168a
00241907  48 0F BA 25 78 51 D8 00 24      bt qword ptr [rip + 0xd85178], 0x24
00241910  0F 83 5B FD FF FF               jae 0x140241671
00241916  8B 8F B8 00 00 00               mov ecx, dword ptr [rdi + 0xb8]
0024191C  C1 E9 08                        shr ecx, 8
0024191F  C1 E9 03                        shr ecx, 3
00241922  83 E1 01                        and ecx, 1
00241925  E9 3F FD FF FF                  jmp 0x140241669
0024192A  45 85 F6                        test r14d, r14d
0024192D  74 13                           je 0x140241942
0024192F  44 38 63 19                     cmp byte ptr [rbx + 0x19], r12b
00241933  0F 85 F6 FA FF FF               jne 0x14024142f
00241939  C6 43 19 01                     mov byte ptr [rbx + 0x19], 1
0024193D  E9 ED FA FF FF                  jmp 0x14024142f
00241942  44 38 63 19                     cmp byte ptr [rbx + 0x19], r12b
00241946  0F 85 E3 FA FF FF               jne 0x14024142f
0024194C  49 8B D1                        mov rdx, r9
0024194F  48 8D 4B 28                     lea rcx, [rbx + 0x28]
00241953  4C 8D 0D 36 3F 45 00            lea r9, [rip + 0x453f36]
0024195A  41 B8 08 00 00 00               mov r8d, 8
00241960  E8 8B F0 2B 00                  call 0x1405009f0
00241965  48 8B CB                        mov rcx, rbx
00241968  E8 3B 7A 06 00                  call 0x1402a93a8
0024196D  41 BE 01 00 00 00               mov r14d, 1
00241973  E9 15 FD FF FF                  jmp 0x14024168d
00241978  83 4B 10 09                     or dword ptr [rbx + 0x10], 9
0024197C  41 8B CC                        mov ecx, r12d
0024197F  E9 83 FB FF FF                  jmp 0x140241507
00241984  81 E1 FF 03 00 00               and ecx, 0x3ff
0024198A  48 8D 14 29                     lea rdx, [rcx + rbp]
0024198E  48 81 FA FF 03 00 00            cmp rdx, 0x3ff
00241995  0F 87 FF FD FF FF               ja 0x14024179a
0024199B  48 3B D1                        cmp rdx, rcx
0024199E  0F 86 F6 FD FF FF               jbe 0x14024179a
002419A4  E9 6C FA FF FF                  jmp 0x140241415
002419A9  8B 8F B8 00 00 00               mov ecx, dword ptr [rdi + 0xb8]
002419AF  F6 C1 0F                        test cl, 0xf
002419B2  74 58                           je 0x140241a0c
002419B4  48 C1 E8 0C                     shr rax, 0xc
002419B8  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
002419C2  48 23 C1                        and rax, rcx
002419C5  48 8D 0C 40                     lea rcx, [rax + rax*2]
002419C9  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002419D3  48 C1 E1 04                     shl rcx, 4
002419D7  48 8B C0                        mov rax, rax
002419DA  45 33 C0                        xor r8d, r8d
002419DD  48 03 C8                        add rcx, rax
002419E0  41 8D 50 02                     lea edx, [r8 + 2]
002419E4  E8 37 3A 04 00                  call 0x140285420
002419E9  A8 41                           test al, 0x41
002419EB  0F 84 80 FC FF FF               je 0x140241671
002419F1  85 ED                           test ebp, ebp
002419F3  0F 85 83 FC FF FF               jne 0x14024167c
002419F9  E9 73 FC FF FF                  jmp 0x140241671
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00241476(void)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rsi;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;

    v_stack_p58 = v_rbx;
    v_stack_p60 = v_rbp;
    v_stack_p68 = v_r12;
    v_r12 = 0;
    v_stack_p28 = v_r13;
    v_stack_p20 = v_r15;
    if (*(unsigned __int64 *)(v_rsi + 8) != 0) goto loc_00241537;
    result = MiGetProcessorFlushList(a1, a2, a3, a4);
    *(unsigned int *)(result + 4136 + 16) = 2;
    *(unsigned int *)(result + 4136 + 20) = 1;
    *(unsigned __int64 *)(result + 4136) = v_rdi;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 184))) >> (8));
    result = (unsigned __int8)((result) >> (3));
    result = (unsigned __int8)((result) & (1));
    *(unsigned __int8 *)(result + 4136 + 24) = (unsigned __int8)(result);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 184)))) & (15)) != 0) goto loc_002414F9;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    if (v_rdi != a1) goto loc_00241978;
loc_002414F9:
    a1 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 184)))) & (15)) == 0) { a1 = 1; }
loc_00241507:
    *(unsigned int *)(result + 4136 + 8) = (unsigned int)(a1);
    *(unsigned __int16 *)(result + 4136 + 25) = 0;
    *(unsigned int *)(result + 4136 + 28) = 0;
    *(unsigned __int64 *)(result + 4136 + 32) = 0;
    *(unsigned __int64 *)(result + 4136 + 40) = 0;
    *(unsigned __int64 *)(v_rsi + 8) = result + 4136;
loc_00241537:
    v_rsi = (v_r14) << (25);
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi))) & (4));
    result = (v_r13) << (25);
    v_rsi = (v_rsi) - (result);
    v_rsi = (v_rsi) >> (16);
    if (v_r14 < result) goto loc_0024159C;
    if (v_r14 > result) goto loc_0024159C;
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(v_r14)))) == 0) goto loc_0024159C;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(v_r14))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(v_r14))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0024170D;
loc_0024159C:
    a3 = (*(unsigned __int64 *)(v_r14)) >> (12);
    a3 = (a3) & (v_r10);
    v_rbp = (a3 + a3 * 2) << (4);
    v_rbp = (v_rbp) + (a4);
    if (v_rsi >= v_r13) goto loc_002418B8;
loc_002415C7:
loc_002415CA:
    if (0 != 0) goto loc_00241885;
loc_002415D8:
    if (condition_is_above_or_equal) goto loc_00241805;
loc_002415E7:
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rbp + 32)))) > 1) goto loc_00241872;
loc_002415F4:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_rdi + 184))) & (15));
    if (((unsigned __int8)(result)) == 1) goto loc_0024184B;
loc_00241616:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12511862) + *(unsigned __int16 *)(v_rdi + 174) * 8) + 17452))) == 0) goto loc_0024167C;
    if (v_rsi >= v_r13) goto loc_00241857;
loc_00241631:
    result = MiGetVaAge(*(unsigned __int16 *)(v_rdi + 174), v_rsi, a3, a4);
    if (((unsigned int)((unsigned __int8)(result))) == 7) goto loc_0024167C;
loc_00241641:
    result = MI_READ_PTE_LOCK_FREE(v_r14, v_rsi, a3, a4);
    if ((((unsigned __int8)(result)) & (32)) == 0) goto loc_0024167C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 184)))) & (15)) != 0) goto loc_00241907;
    a1 = ((*(unsigned __int64 *)(v_rdi + 624)) != 0) ? 1 : 0;
loc_00241669:
    if ((unsigned int)(a1) != 0) goto loc_002419A9;
loc_00241671:
    result = MiLogPageAccess(v_rdi, v_r14, a3, a4);
loc_0024167C:
    if ((*(unsigned int *)(result + 4136 + 8)) != 1) goto loc_002418CE;
loc_0024168A:
loc_0024168D:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 4136 + 28))) == 0) goto loc_0024179A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 4136 + 16)))) & (2)) != 0) goto loc_00241755;
    if (((*(unsigned __int64 *)(result + 4136 + (unsigned int)(*(unsigned int *)(result + 4136 + 28)) - 1 * 8 + 40)) & (0xC00ULL)) != 0) goto loc_0024179A;
    a3 = (unsigned int)((*(unsigned __int64 *)(result + 4136 + (unsigned int)(*(unsigned int *)(result + 4136 + 28)) - 1 * 8 + 40)) & (0x3FFULL));
    a1 = (*(unsigned __int64 *)(result + 4136 + (unsigned int)(*(unsigned int *)(result + 4136 + 28)) - 1 * 8 + 40)) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (a3 + 1) << (12);
    a2 = (a2) + (a1);
    if (a2 != v_rsi) goto loc_002416F8;
    if ((a3 + 1 * 1) <= a3) goto loc_002416F8;
loc_002416F8:
    goto loc_0024177C;
loc_0024170D:
    result = MiPteHasShadow(*(unsigned __int64 *)(result + 4136 + (unsigned int)(*(unsigned int *)(result + 4136 + 28)) - 1 + 5 * 8), a2, a3, (unsigned int)(*(unsigned int *)(result + 4136 + 28)));
    if (result == 0) goto loc_0024159C;
    if (*(unsigned __int64 *)(result + 1288) == 0) goto loc_0024159C;
    result = (0) >> (3);
    result = (unsigned int)((result) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (32)) != 0) {
        a2 = (a2) | (32);
    }
    a3 = (a2) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (66)) == 0) { a3 = a2; }
    goto loc_0024159C;
loc_00241755:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 4136 + 28))) == 0) goto loc_0024179A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 4136 + 16)))) & (2)) != 0) goto loc_0024179A;
    if (((*(unsigned __int64 *)(result + 4136 + (unsigned int)(*(unsigned int *)(result + 4136 + 28)) - 1 + 5 * 8)) & (0xC00ULL)) != 0) goto loc_0024179A;
loc_0024177C:
    v_r11 = (1) << (12);
    a2 = (*(unsigned __int64 *)(result + 4136 + (unsigned int)(*(unsigned int *)(result + 4136 + 28)) - 1 + 5 * 8)) & (0xFFFFFFFFFFFFF000ULL);
    if (a2 == (v_rsi + v_r11 * 1)) goto loc_00241984;
loc_0024179A:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 4136 + 28)))) == (*(unsigned int *)(result + 4136 + 12))) goto loc_0024192A;
loc_002417A4:
    a2 = (unsigned int)(0x400ULL);
    if ((1 - 1) <= 0x3FFULL) { a2 = 1; }
    a1 = (v_rsi) & (0xFFFFFFFFFFFFF000ULL);
    result = (unsigned int)((a2 - 1) & (0x3FFULL));
    result = (result) | (a1);
    *(unsigned __int64 *)(result + 4136 + (unsigned int)(*(unsigned int *)(result + 4136 + 28)) * 8 + 40) = result;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 4136 + 28))) + 1);
    a1 = (a2) << (12);
    v_rsi = (v_rsi) + (a1);
    *(unsigned int *)(result + 4136 + 28) = (unsigned int)(a4);
    v_rbp = (1) - (a2);
    if (condition_is_equal) goto loc_002417A4;
    if (((unsigned int)(a4)) == (*(unsigned int *)(result + 4136 + 12))) goto loc_0024168A;
    goto loc_002417A4;
loc_00241805:
    if (sign_flag) goto loc_002415E7;
    if (*(unsigned __int64 *)(v_rbp + 8) == 0) goto loc_002415E7;
    a3 = (*(unsigned __int64 *)(v_rbp + 8)) | (*(unsigned __int64 *)(v_rbp + 8));
    result = MiDemoteCombinedPte(v_rdi, 0, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_002415E7;
    goto loc_002415E7;
loc_0024184B:
    goto loc_00241616;
loc_00241857:
    if (v_rsi <= (v_rip + 12547246)) goto loc_00241641;
    goto loc_00241631;
loc_00241872:
    goto loc_002415F4;
loc_00241885:
    result = (*(unsigned __int64 *)(v_rbp + 24)) & (v_rdi);
    result = MiIsPageTableLocked(v_rdi, 0, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_002415D8;
loc_002418B8:
    if (v_rsi > v_rdi) goto loc_002415C7;
    goto loc_002415CA;
loc_002418CE:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 4136 + 16)))) & (4)) != 0) goto loc_0024168A;
    if (v_rsi < v_r13) goto loc_0024168A;
    if (v_rsi > v_r13) goto loc_0024168A;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 4136 + 16))) | (4));
    *(unsigned int *)(result + 4136 + 16) = (unsigned int)(a1);
    goto loc_0024168A;
loc_00241907:
    if (condition_is_above_or_equal) goto loc_00241671;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 184))) >> (8));
    a1 = (unsigned int)((a1) >> (3));
    a1 = (unsigned int)((a1) & (1));
    goto loc_00241669;
loc_0024192A:
    if (0 == 0) goto loc_00241942;
    *(unsigned __int8 *)(result + 4136 + 25) = 1;
loc_00241942:
    result = qsort(result + 4136 + 40, a4, 8, v_rip + 4538166);
    result = MiCompressTbFlushList(result + 4136, a4, 8, v_rip + 4538166);
    goto loc_0024168D;
loc_00241978:
    goto loc_00241507;
loc_00241984:
    a1 = (unsigned int)((0) & (0x3FFULL));
    if ((a1 + v_rbp * 1) > 0x3FFULL) goto loc_0024179A;
    if ((a1 + v_rbp * 1) <= a1) goto loc_0024179A;
loc_002419A9:
    result = (result) >> (12);
    result = (result) & ((unsigned int)(*(unsigned int *)(v_rdi + 184)));
    a1 = (result + result * 2) << (4);
    a3 = 0;
    a1 = (a1) + (result);
    result = MiGetPagePrivilege(a1, a3 + 2, a3, v_rip + 4538166);
    if ((((unsigned __int8)(result)) & (65)) == 0) goto loc_00241671;
    if ((unsigned int)(v_rbp) != 0) goto loc_0024167C;
    goto loc_00241671;
}
```

## 5. (Beta) C Style

```c
void sub_00241476(void)
{
    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rsi;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;

    v_stack_p58 = local_rbx;
    v_stack_p60 = local_rbp;
    v_stack_p68 = local_r12;
    local_r12 = 0;
    v_stack_p28 = local_r13;
    v_stack_p20 = local_r15;
    if (*(uint64_t *)(local_rsi + 0x8) != 0) goto loc_00241537;
    result = MiGetProcessorFlushList(a1, a2, a3, a4);
    *(uint32_t *)(result + 0x1028 + 0x10) = 2;
    *(uint32_t *)(result + 0x1028 + 0x14) = 1;
    *(uint64_t *)(result + 0x1028) = local_rdi;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0xB8))) >> (8));
    result = (uint8_t)((result) >> (3));
    result = (uint8_t)((result) & (1));
    *(uint8_t *)(result + 0x1028 + 0x18) = (uint8_t)(result);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0xB8)))) & (15)) != 0) goto loc_002414F9;
    a1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    if (local_rdi != a1) goto loc_00241978;
loc_002414F9:
    a1 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0xB8)))) & (15)) == 0) { a1 = 1; }
loc_00241507:
    *(uint32_t *)(result + 0x1028 + 0x8) = (uint32_t)(a1);
    *(uint16_t *)(result + 0x1028 + 0x19) = 0;
    *(uint32_t *)(result + 0x1028 + 0x1C) = 0;
    *(uint64_t *)(result + 0x1028 + 0x20) = 0;
    *(uint64_t *)(result + 0x1028 + 0x28) = 0;
    *(uint64_t *)(local_rsi + 0x8) = result + 4136;
loc_00241537:
    local_rsi = (local_r14) << (25);
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi))) & (4));
    result = (local_r13) << (25);
    local_rsi = (local_rsi) - (result);
    local_rsi = (local_rsi) >> (16);
    if (local_r14 < result) goto loc_0024159C;
    if (local_r14 > result) goto loc_0024159C;
    if (((1) & ((uint8_t)(*(uint64_t *)(local_r14)))) == 0) goto loc_0024159C;
    a1 = ((((uint8_t)(*(uint64_t *)(local_r14))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(local_r14))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(a1))) == 0) goto loc_0024170D;
loc_0024159C:
    a3 = (*(uint64_t *)(local_r14)) >> (12);
    a3 = (a3) & (local_r10);
    local_rbp = (a3 + a3 * 2) << (4);
    local_rbp = (local_rbp) + (a4);
    if (local_rsi >= local_r13) goto loc_002418B8;
loc_002415C7:
loc_002415CA:
    if (0 != 0) goto loc_00241885;
loc_002415D8:
    if (condition_is_above_or_equal) goto loc_00241805;
loc_002415E7:
    if (((uint16_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x20)))) > 1) goto loc_00241872;
loc_002415F4:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0xB8))) & (15));
    if (((uint8_t)(result)) == 1) goto loc_0024184B;
loc_00241616:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xBEEA76) + *(uint16_t *)(local_rdi + 0xAE) * 8) + 0x442C))) == 0) goto loc_0024167C;
    if (local_rsi >= local_r13) goto loc_00241857;
loc_00241631:
    result = MiGetVaAge(*(uint16_t *)(local_rdi + 0xAE), local_rsi, a3, a4);
    if (((uint32_t)((uint8_t)(result))) == 7) goto loc_0024167C;
loc_00241641:
    result = MI_READ_PTE_LOCK_FREE(local_r14, local_rsi, a3, a4);
    if ((((uint8_t)(result)) & (32)) == 0) goto loc_0024167C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0xB8)))) & (15)) != 0) goto loc_00241907;
    a1 = ((*(uint64_t *)(local_rdi + 0x270)) != 0) ? 1 : 0;
loc_00241669:
    if ((uint32_t)(a1) != 0) goto loc_002419A9;
loc_00241671:
    result = MiLogPageAccess(local_rdi, local_r14, a3, a4);
loc_0024167C:
    if ((*(uint32_t *)(result + 0x1028 + 0x8)) != 1) goto loc_002418CE;
loc_0024168A:
loc_0024168D:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1028 + 0x1C))) == 0) goto loc_0024179A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x1028 + 0x10)))) & (2)) != 0) goto loc_00241755;
    if (((*(uint64_t *)(result + 0x1028 + (uint32_t)(*(uint32_t *)(result + 0x1028 + 0x1C)) - 0x1 * 8 + 0x28)) & (0xC00ULL)) != 0) goto loc_0024179A;
    a3 = (uint32_t)((*(uint64_t *)(result + 0x1028 + (uint32_t)(*(uint32_t *)(result + 0x1028 + 0x1C)) - 0x1 * 8 + 0x28)) & (0x3FFULL));
    a1 = (*(uint64_t *)(result + 0x1028 + (uint32_t)(*(uint32_t *)(result + 0x1028 + 0x1C)) - 0x1 * 8 + 0x28)) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (a3 + 1) << (12);
    a2 = (a2) + (a1);
    if (a2 != local_rsi) goto loc_002416F8;
    if ((a3 + 1 * 1) <= a3) goto loc_002416F8;
loc_002416F8:
    goto loc_0024177C;
loc_0024170D:
    result = MiPteHasShadow(*(uint64_t *)(result + 0x1028 + (uint32_t)(*(uint32_t *)(result + 0x1028 + 0x1C)) - 0x1 + 0x5 * 8), a2, a3, (uint32_t)(*(uint32_t *)(result + 0x1028 + 0x1C)));
    if (result == 0) goto loc_0024159C;
    if (*(uint64_t *)(result + 0x508) == 0) goto loc_0024159C;
    result = (0) >> (3);
    result = (uint32_t)((result) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (32)) != 0) {
        a2 = (a2) | (32);
    }
    a3 = (a2) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (66)) == 0) { a3 = a2; }
    goto loc_0024159C;
loc_00241755:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1028 + 0x1C))) == 0) goto loc_0024179A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x1028 + 0x10)))) & (2)) != 0) goto loc_0024179A;
    if (((*(uint64_t *)(result + 0x1028 + (uint32_t)(*(uint32_t *)(result + 0x1028 + 0x1C)) - 0x1 + 0x5 * 8)) & (0xC00ULL)) != 0) goto loc_0024179A;
loc_0024177C:
    local_r11 = (1) << (12);
    a2 = (*(uint64_t *)(result + 0x1028 + (uint32_t)(*(uint32_t *)(result + 0x1028 + 0x1C)) - 0x1 + 0x5 * 8)) & (0xFFFFFFFFFFFFF000ULL);
    if (a2 == (local_rsi + local_r11 * 1)) goto loc_00241984;
loc_0024179A:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x1028 + 0x1C)))) == (*(uint32_t *)(result + 0x1028 + 0xC))) goto loc_0024192A;
loc_002417A4:
    a2 = (uint32_t)(0x400ULL);
    if ((1 - 1) <= 0x3FFULL) { a2 = 1; }
    a1 = (local_rsi) & (0xFFFFFFFFFFFFF000ULL);
    result = (uint32_t)((a2 - 1) & (0x3FFULL));
    result = (result) | (a1);
    *(uint64_t *)(result + 0x1028 + (uint32_t)(*(uint32_t *)(result + 0x1028 + 0x1C)) * 8 + 0x28) = result;
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x1028 + 0x1C))) + 1);
    a1 = (a2) << (12);
    local_rsi = (local_rsi) + (a1);
    *(uint32_t *)(result + 0x1028 + 0x1C) = (uint32_t)(a4);
    local_rbp = (1) - (a2);
    if (condition_is_equal) goto loc_002417A4;
    if (((uint32_t)(a4)) == (*(uint32_t *)(result + 0x1028 + 0xC))) goto loc_0024168A;
    goto loc_002417A4;
loc_00241805:
    if (sign_flag) goto loc_002415E7;
    if (*(uint64_t *)(local_rbp + 0x8) == 0) goto loc_002415E7;
    a3 = (*(uint64_t *)(local_rbp + 0x8)) | (*(uint64_t *)(local_rbp + 0x8));
    result = MiDemoteCombinedPte(local_rdi, 0, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_002415E7;
    goto loc_002415E7;
loc_0024184B:
    goto loc_00241616;
loc_00241857:
    if (local_rsi <= (v_rip + 12547246)) goto loc_00241641;
    goto loc_00241631;
loc_00241872:
    goto loc_002415F4;
loc_00241885:
    result = (*(uint64_t *)(local_rbp + 0x18)) & (local_rdi);
    result = MiIsPageTableLocked(local_rdi, 0, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_002415D8;
loc_002418B8:
    if (local_rsi > local_rdi) goto loc_002415C7;
    goto loc_002415CA;
loc_002418CE:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x1028 + 0x10)))) & (4)) != 0) goto loc_0024168A;
    if (local_rsi < local_r13) goto loc_0024168A;
    if (local_rsi > local_r13) goto loc_0024168A;
    a1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x1028 + 0x10))) | (4));
    *(uint32_t *)(result + 0x1028 + 0x10) = (uint32_t)(a1);
    goto loc_0024168A;
loc_00241907:
    if (condition_is_above_or_equal) goto loc_00241671;
    a1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0xB8))) >> (8));
    a1 = (uint32_t)((a1) >> (3));
    a1 = (uint32_t)((a1) & (1));
    goto loc_00241669;
loc_0024192A:
    if (0 == 0) goto loc_00241942;
    *(uint8_t *)(result + 0x1028 + 0x19) = 1;
loc_00241942:
    result = qsort(result + 4136 + 40, a4, 8, v_rip + 4538166);
    result = MiCompressTbFlushList(result + 4136, a4, 8, v_rip + 4538166);
    goto loc_0024168D;
loc_00241978:
    goto loc_00241507;
loc_00241984:
    a1 = (uint32_t)((0) & (0x3FFULL));
    if ((a1 + local_rbp * 1) > 0x3FFULL) goto loc_0024179A;
    if ((a1 + local_rbp * 1) <= a1) goto loc_0024179A;
loc_002419A9:
    result = (result) >> (12);
    result = (result) & ((uint32_t)(*(uint32_t *)(local_rdi + 0xB8)));
    a1 = (result + result * 2) << (4);
    a3 = 0;
    a1 = (a1) + (result);
    result = MiGetPagePrivilege(a1, a3 + 2, a3, v_rip + 4538166);
    if ((((uint8_t)(result)) & (65)) == 0) goto loc_00241671;
    if ((uint32_t)(local_rbp) != 0) goto loc_0024167C;
    goto loc_00241671;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00241476&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
