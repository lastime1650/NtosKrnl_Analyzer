# sub_00241E90

- RVA: `0x00241E90`–`0x0024225B` (길이 `971` bytes)
- VA: `0x0000000140241E90`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00061978`
- 디코드: `219`개 명령, `971/971` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00241F3A` → [MiDecommitHandlePageFileFormatPte](MiDecommitHandlePageFileFormatPte_function_00242A5C.md) (function, `0x00242A5C`)
- `0x00241F85` → [MiIncreaseUsedPtes](MiIncreaseUsedPtes_function_00243630.md) (function, `0x00243630`)
- `0x00241FB3` → [MiGetProcessorFlushList](MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x00242054` → [MiDecommitHandleProtoFormatPte](MiDecommitHandleProtoFormatPte_function_00242D54.md) (function, `0x00242D54`)
- `0x002420F4` → [MiDecommitPagesTail](../27/MiDecommitPagesTail_function_002790FC.md) (function, `0x002790FC`)
- `0x002420FE` → [MiDecommitLockNewPageTable](MiDecommitLockNewPageTable_function_00243270.md) (function, `0x00243270`)
- `0x0024217B` → [MiDecommitPagesTail](../27/MiDecommitPagesTail_function_002790FC.md) (function, `0x002790FC`)
- `0x00242192` → [MiReturnPagedPoolLockCharge](MiReturnPagedPoolLockCharge_function_00240780.md) (function, `0x00240780`)
- `0x0024219C` → [MiDecommitHandleTransitionPte](MiDecommitHandleTransitionPte_function_0024037C.md) (function, `0x0024037C`)
- `0x002421CC` → [KiRemoveSystemWorkPriorityKick](../26/KiRemoveSystemWorkPriorityKick_function_002631D0.md) (function, `0x002631D0`)
- `0x0024221B` → [MiDecommitLargePte](../4D/MiDecommitLargePte_function_004D1ED4.md) (function, `0x004D1ED4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00241EB3` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00242140` → RVA `0x00E38840` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **38**
  - `0x00241E96` → [sub_00241C55 + 0x1A2](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00241EA5` → [sub_00241C55 + 0x1B0](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00241EAE` → [sub_00241C55 + 0x1C5](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00241EBE` → [sub_00241C55 + 0x96](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00241EDB` → [sub_00241C55 + 0x96](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00241EEB` → [sub_00241C55 + 0x96](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00241F17` → [sub_00241C55 + 0x96](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00241F3F` → [sub_00241C55 + 0x101](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00241F48` → [sub_00241C55 + 0x101](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00241F75` → [sub_00241C55 + 0x101](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00241F90` → [sub_00241C55 + 0x101](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00241FAB` → [sub_00241C55 + 0x101](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00242034` → [sub_00241C55 + 0xBD](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x0024203F` → [sub_00241C55 + 0xE0](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00242046` → [sub_00241C55 + 0xCC](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x0024204F` → [sub_00241C55 + 0xE0](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00242059` → [sub_00241C55 + 0x101](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00242062` → [sub_00241C55 + 0x1A2](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x0024206D` → [sub_00241C55 + 0x1C5](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00242078` → [sub_00241C55 + 0x1E5](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00242087` → [sub_00241C55 + 0x1B0](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00242092` → [sub_00241C55 + 0x1C5](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x0024209C` → [sub_00241C55 + 0x1C5](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x002420A4` → [sub_00241C55 + 0x1B0](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x002420D6` → [sub_00241C55 + 0x1C5](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x002420EA` → [sub_00241C55 + 0x1C5](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00242105` → [sub_00241C55 + 0x207](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x0024210F` → [sub_00241C55 + 0x66](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00242124` → [sub_00241C55 + 0x14D](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00242170` → [sub_00241C55 + 0x14D](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00242180` → [sub_00241C55 + 0x1E5](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00242197` → [sub_00241C55 + 0x101](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x002421A3` → [sub_00241C55 + 0x101](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x002421A9` → [sub_00241C55 + 0x1E5](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x002421F6` → [sub_00241C55 + 0x13D](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00242220` → [sub_00241C55 + 0x101](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00242229` → [sub_00241C55 + 0xF3](Unknown_function_00241C55.md) (`tail-transfer`)
  - `0x00242256` → [sub_00241C55 + 0xEA](Unknown_function_00241C55.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00241E90  45 8B C5                        mov r8d, r13d
00241E93  83 FE 07                        cmp esi, 7
00241E96  0F 86 5B FF FF FF               jbe 0x140241df7
00241E9C  0F B6 81 B9 38 00 00            movzx eax, byte ptr [rcx + 0x38b9]
00241EA3  84 C0                           test al, al
00241EA5  0F 84 5A FF FF FF               je 0x140241e05
00241EAB  41 8B DD                        mov ebx, r13d
00241EAE  E9 67 FF FF FF                  jmp 0x140241e1a
00241EB3  48 F7 05 CA 4B D8 00 00 00 60 00  test qword ptr [rip + 0xd84bca], 0x600000
00241EBE  0F 84 27 FE FF FF               je 0x140241ceb
00241EC4  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00241ECD  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00241ED4  44 38 A9 60 01 00 00            cmp byte ptr [rcx + 0x160], r13b
00241EDB  0F 84 0A FE FF FF               je 0x140241ceb
00241EE1  48 8B 91 08 05 00 00            mov rdx, qword ptr [rcx + 0x508]
00241EE8  48 85 D2                        test rdx, rdx
00241EEB  0F 84 FA FD FF FF               je 0x140241ceb
00241EF1  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
00241EF5  48 C1 E8 03                     shr rax, 3
00241EF9  25 FF 01 00 00                  and eax, 0x1ff
00241EFE  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
00241F02  A8 20                           test al, 0x20
00241F04  74 04                           je 0x140241f0a
00241F06  48 83 CB 20                     or rbx, 0x20
00241F0A  48 8B CB                        mov rcx, rbx
00241F0D  48 83 CB 42                     or rbx, 0x42
00241F11  A8 42                           test al, 0x42
00241F13  48 0F 44 D9                     cmove rbx, rcx
00241F17  E9 CF FD FF FF                  jmp 0x140241ceb
00241F1C  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00241F21  48 8B D3                        mov rdx, rbx
00241F24  48 0F BA E3 0A                  bt rbx, 0xa
00241F29  0F 82 25 01 00 00               jb 0x140242054
00241F2F  48 0F BA E3 0B                  bt rbx, 0xb
00241F34  0F 82 62 02 00 00               jb 0x14024219c
00241F3A  E8 1D 0B 00 00                  call 0x140242a5c
00241F3F  E9 12 FE FF FF                  jmp 0x140241d56
00241F44  44 39 75 88                     cmp dword ptr [rbp - 0x78], r14d
00241F48  0F 85 08 FE FF FF               jne 0x140241d56
00241F4E  44 39 75 C0                     cmp dword ptr [rbp - 0x40], r14d
00241F52  48 8B 5D 20                     mov rbx, qword ptr [rbp + 0x20]
00241F56  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
00241F5A  49 0F 45 DD                     cmovne rbx, r13
00241F5E  48 39 45 A8                     cmp qword ptr [rbp - 0x58], rax
00241F62  76 0D                           jbe 0x140241f71
00241F64  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00241F69  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00241F6D  48 01 41 18                     add qword ptr [rcx + 0x18], rax
00241F71  4C 39 75 10                     cmp qword ptr [rbp + 0x10], r14
00241F75  0F 84 DB FD FF FF               je 0x140241d56
00241F7B  48 8B 55 A0                     mov rdx, qword ptr [rbp - 0x60]
00241F7F  45 33 C9                        xor r9d, r9d
00241F82  44 8B C3                        mov r8d, ebx
00241F85  E8 A6 16 00 00                  call 0x140243630
00241F8A  49 8B D6                        mov rdx, r14
00241F8D  48 85 DB                        test rbx, rbx
00241F90  0F 84 C0 FD FF FF               je 0x140241d56
00241F96  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
00241F9A  48 8D 0C D0                     lea rcx, [rax + rdx*8]
00241F9E  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
00241FA2  48 FF C2                        inc rdx
00241FA5  48 89 01                        mov qword ptr [rcx], rax
00241FA8  48 3B D3                        cmp rdx, rbx
00241FAB  0F 83 A5 FD FF FF               jae 0x140241d56
00241FB1  EB E3                           jmp 0x140241f96
00241FB3  E8 D8 0C 00 00                  call 0x140242c90
00241FB8  4C 8B 45 80                     mov r8, qword ptr [rbp - 0x80]
00241FBC  48 8B D0                        mov rdx, rax
00241FBF  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00241FC4  44 89 70 10                     mov dword ptr [rax + 0x10], r14d
00241FC8  44 89 68 14                     mov dword ptr [rax + 0x14], r13d
00241FCC  4C 89 00                        mov qword ptr [rax], r8
00241FCF  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
00241FD6  C1 E8 08                        shr eax, 8
00241FD9  A8 08                           test al, 8
00241FDB  0F 95 C0                        setne al
00241FDE  88 42 18                        mov byte ptr [rdx + 0x18], al
00241FE1  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
00241FE8  A8 0F                           test al, 0xf
00241FEA  75 20                           jne 0x14024200c
00241FEC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00241FF5  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00241FFC  48 81 C1 00 04 00 00            add rcx, 0x400
00242003  4C 3B C1                        cmp r8, rcx
00242006  0F 85 EF 01 00 00               jne 0x1402421fb
0024200C  41 8B 80 B8 00 00 00            mov eax, dword ptr [r8 + 0xb8]
00242013  41 8B CE                        mov ecx, r14d
00242016  A8 0F                           test al, 0xf
00242018  41 0F 44 CD                     cmove ecx, r13d
0024201C  83 62 10 DB                     and dword ptr [rdx + 0x10], 0xffffffdb
00242020  89 4A 08                        mov dword ptr [rdx + 8], ecx
00242023  66 44 89 72 19                  mov word ptr [rdx + 0x19], r14w
00242028  44 89 72 1C                     mov dword ptr [rdx + 0x1c], r14d
0024202C  4C 89 72 20                     mov qword ptr [rdx + 0x20], r14
00242030  4C 89 72 28                     mov qword ptr [rdx + 0x28], r14
00242034  E9 D9 FC FF FF                  jmp 0x140241d12
00242039  41 B8 02 00 00 00               mov r8d, 2
0024203F  E9 F1 FC FF FF                  jmp 0x140241d35
00242044  85 C0                           test eax, eax
00242046  0F 84 D5 FC FF FF               je 0x140241d21
0024204C  45 8B C6                        mov r8d, r14d
0024204F  E9 E1 FC FF FF                  jmp 0x140241d35
00242054  E8 FB 0C 00 00                  call 0x140242d54
00242059  E9 F8 FC FF FF                  jmp 0x140241d56
0024205E  48 3B 41 08                     cmp rax, qword ptr [rcx + 8]
00242062  0F 84 8F FD FF FF               je 0x140241df7
00242068  BB 04 00 00 00                  mov ebx, 4
0024206D  E9 A8 FD FF FF                  jmp 0x140241e1a
00242072  45 8B CD                        mov r9d, r13d
00242075  83 FF 07                        cmp edi, 7
00242078  0F 86 BC FD FF FF               jbe 0x140241e3a
0024207E  0F B6 81 B9 38 00 00            movzx eax, byte ptr [rcx + 0x38b9]
00242085  84 C0                           test al, al
00242087  0F 84 78 FD FF FF               je 0x140241e05
0024208D  BB 07 00 00 00                  mov ebx, 7
00242092  E9 83 FD FF FF                  jmp 0x140241e1a
00242097  BB 03 00 00 00                  mov ebx, 3
0024209C  E9 79 FD FF FF                  jmp 0x140241e1a
002420A1  45 85 C9                        test r9d, r9d
002420A4  0F 85 5B FD FF FF               jne 0x140241e05
002420AA  FA                              cli
002420AB  44 89 B1 AC 83 00 00            mov dword ptr [rcx + 0x83ac], r14d
002420B2  44 89 B1 5C 86 00 00            mov dword ptr [rcx + 0x865c], r14d
002420B9  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
002420C2  4C 8B 81 B8 8E 00 00            mov r8, qword ptr [rcx + 0x8eb8]
002420C9  4D 85 C0                        test r8, r8
002420CC  0F 85 DC 00 00 00               jne 0x1402421ae
002420D2  FB                              sti
002420D3  41 8B DE                        mov ebx, r14d
002420D6  E9 3F FD FF FF                  jmp 0x140241e1a
002420DB  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
002420DF  48 39 41 08                     cmp qword ptr [rcx + 8], rax
002420E3  74 C5                           je 0x1402420aa
002420E5  BB 06 00 00 00                  mov ebx, 6
002420EA  E9 2B FD FF FF                  jmp 0x140241e1a
002420EF  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
002420F4  E8 03 70 03 00                  call 0x1402790fc
002420F9  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
002420FE  E8 6D 11 00 00                  call 0x140243270
00242103  85 C0                           test eax, eax
00242105  0F 84 51 FD FF FF               je 0x140241e5c
0024210B  48 8B 5D B8                     mov rbx, qword ptr [rbp - 0x48]
0024210F  E9 A7 FB FF FF                  jmp 0x140241cbb
00242114  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00242118  8B 88 B8 00 00 00               mov ecx, dword ptr [rax + 0xb8]
0024211E  80 E1 0F                        and cl, 0xf
00242121  80 F9 05                        cmp cl, 5
00242124  0F 87 78 FC FF FF               ja 0x140241da2
0024212A  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
0024212E  8B 88 B8 00 00 00               mov ecx, dword ptr [rax + 0xb8]
00242134  80 E1 0F                        and cl, 0xf
00242137  41 3A CD                        cmp cl, r13b
0024213A  0F 85 C7 00 00 00               jne 0x140242207
00242140  48 8D 05 F9 66 BF 00            lea rax, [rip + 0xbf66f9]
00242147  48 8B 08                        mov rcx, qword ptr [rax]
0024214A  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00242153  48 8B 80 38 88 00 00            mov rax, qword ptr [rax + 0x8838]
0024215A  48 85 C0                        test rax, rax
0024215D  74 26                           je 0x140242185
0024215F  8B 80 44 01 00 00               mov eax, dword ptr [rax + 0x144]
00242165  48 C1 E0 06                     shl rax, 6
00242169  8B 04 01                        mov eax, dword ptr [rcx + rax]
0024216C  0F BA E0 1E                     bt eax, 0x1e
00242170  0F 83 2C FC FF FF               jae 0x140241da2
00242176  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
0024217B  E8 7C 6F 03 00                  call 0x1402790fc
00242180  E9 B5 FC FF FF                  jmp 0x140241e3a
00242185  41 8B C6                        mov eax, r14d
00242188  EB DB                           jmp 0x140242165
0024218A  48 8B D3                        mov rdx, rbx
0024218D  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00242192  E8 E9 E5 FF FF                  call 0x140240780
00242197  E9 BA FB FF FF                  jmp 0x140241d56
0024219C  E8 DB E1 FF FF                  call 0x14024037c
002421A1  85 C0                           test eax, eax
002421A3  0F 85 AD FB FF FF               jne 0x140241d56
002421A9  E9 8C FC FF FF                  jmp 0x140241e3a
002421AE  41 0F 0D 08                     prefetchw byte ptr [r8]
002421B2  41 8B 00                        mov eax, dword ptr [r8]
002421B5  8B D0                           mov edx, eax
002421B7  0F BA F2 15                     btr edx, 0x15
002421BB  F0 41 0F B1 10                  lock cmpxchg dword ptr [r8], edx
002421C0  75 F3                           jne 0x1402421b5
002421C2  0F BA E0 15                     bt eax, 0x15
002421C6  0F 83 06 FF FF FF               jae 0x1402420d2
002421CC  E8 FF 0F 02 00                  call 0x1402631d0
002421D1  E9 FC FE FF FF                  jmp 0x1402420d2
002421D6  B9 02 00 00 00                  mov ecx, 2
002421DB  41 2B C9                        sub ecx, r9d
002421DE  44 8B C1                        mov r8d, ecx
002421E1  44 8B C9                        mov r9d, ecx
002421E4  48 C1 EA 09                     shr rdx, 9
002421E8  48 23 D6                        and rdx, rsi
002421EB  48 8B CF                        mov rcx, rdi
002421EE  48 03 D1                        add rdx, rcx
002421F1  4D 2B CD                        sub r9, r13
002421F4  75 EE                           jne 0x1402421e4
002421F6  E9 97 FB FF FF                  jmp 0x140241d92
002421FB  83 4A 10 09                     or dword ptr [rdx + 0x10], 9
002421FF  41 8B CE                        mov ecx, r14d
00242202  E9 15 FE FF FF                  jmp 0x14024201c
00242207  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
0024220B  48 05 C0 00 00 00               add rax, 0xc0
00242211  E9 31 FF FF FF                  jmp 0x140242147
00242216  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
0024221B  E8 B4 FC 28 00                  call 0x1404d1ed4
00242220  E9 31 FB FF FF                  jmp 0x140241d56
00242225  41 83 F8 02                     cmp r8d, 2
00242229  0F 84 19 FB FF FF               je 0x140241d48
0024222F  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00242233  4A 8D 04 CD 00 00 00 00         lea rax, [r9*8]
0024223B  48 85 C9                        test rcx, rcx
0024223E  48 0F 44 4D B8                  cmove rcx, qword ptr [rbp - 0x48]
00242243  48 2B C1                        sub rax, rcx
00242246  48 89 4D 30                     mov qword ptr [rbp + 0x30], rcx
0024224A  48 03 45 B8                     add rax, qword ptr [rbp - 0x48]
0024224E  48 C1 F8 03                     sar rax, 3
00242252  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
00242256  E9 E4 FA FF FF                  jmp 0x140241d3f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00241E90(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00241E90(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    uint64_t v_stack_p60;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x38B9` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00241E90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
