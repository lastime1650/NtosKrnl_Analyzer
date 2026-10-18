# sub_00853ABC

- RVA: `0x00853ABC`–`0x00854145` (길이 `1,673` bytes)
- VA: `0x0000000140853ABC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069EEC`
- 디코드: `429`개 명령, `1,673/1,673` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00853BAB` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x00853BDC` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x00853C85` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00853D5E` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00853DA3` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00853E89` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00853EF5` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00853F13` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00853F36` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00853F40` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00853FC5` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00853FD9` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x008540E3` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x008540F7` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00853BAB` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x00853BDC` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **34**
  - `0x00853B3B` → [sub_0085416A + 0x573](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853B66` → [sub_0085416A + 0x50D](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853BC5` → [sub_0085416A + 0x4B1](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853BF6` → [sub_0085416A + 0x4D4](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853C14` → [sub_0085416A + 0x410](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853C90` → [sub_0085416A + 0x45B](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853CA2` → [sub_0085416A + 0x620](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853CAB` → [sub_0085416A + 0x5B4](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853D09` → [sub_0085416A + 0x5FC](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853D1C` → [sub_0085416A + 0x470](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853D58` → [sub_0085416A + 0x503](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853DAE` → [sub_0085416A + 0x150](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853DC0` → [sub_0085416A + 0x655](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853DC9` → [sub_0085416A + 0x5D0](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853E27` → [sub_0085416A + 0x60E](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853E3A` → [sub_0085416A + 0x48D](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853E83` → [sub_0085416A + 0x51B](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853EC2` → [sub_0085416A](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853ECF` → [sub_0085416A + 0x176](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853F54` → [sub_0085416A + 0x5EC](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853F76` → [sub_0085416A + 0x431](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853F81` → [sub_0085416A + 0x590](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853FBC` → [sub_0085416A + 0x3B6](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00853FD3` → [sub_0085416A + 0xD5](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00854003` → [sub_0085416A + 0x525](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00854009` → [sub_0085416A + 0x49E](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00854038` → [sub_0085416A + 0x12B](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00854045` → [sub_0085416A + 0x296](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x0085406E` → [sub_0085416A + 0x5F4](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00854091` → [sub_0085416A + 0x43D](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x0085409C` → [sub_0085416A + 0x5A7](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x008540DA` → [sub_0085416A + 0x3E8](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x008540F1` → [sub_0085416A + 0x16B](Unknown_function_0085416A.md) (`tail-transfer`)
  - `0x00854113` → [sub_0085416A + 0x45B](Unknown_function_0085416A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00853ABC  49 89 73 D0                     mov qword ptr [r11 - 0x30], rsi
00853AC0  BA 6C 66 00 00                  mov edx, 0x666c
00853AC5  49 89 7B C8                     mov qword ptr [r11 - 0x38], rdi
00853AC9  41 B8 FF FD 00 00               mov r8d, 0xfdff
00853ACF  4D 89 73 C0                     mov qword ptr [r11 - 0x40], r14
00853AD3  0F 1F 40 00                     nop dword ptr [rax]
00853AD7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
00853AE0  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
00853AE5  4C 8B 75 50                     mov r14, qword ptr [rbp + 0x50]
00853AE9  0F B7 C1                        movzx eax, cx
00853AEC  66 2B C2                        sub ax, dx
00853AEF  41 C7 06 FF FF FF FF            mov dword ptr [r14], 0xffffffff
00853AF6  66 41 85 C0                     test r8w, ax
00853AFA  0F 85 7B 02 00 00               jne 0x140853d7b
00853B00  4C 8D 34 DD 04 00 00 00         lea r14, [rbx*8 + 4]
00853B08  4D 03 F4                        add r14, r12
00853B0B  4C 89 75 D8                     mov qword ptr [rbp - 0x28], r14
00853B0F  66 3B CA                        cmp cx, dx
00853B12  0F 85 41 01 00 00               jne 0x140853c59
00853B18  4C 8B 6D 30                     mov r13, qword ptr [rbp + 0x30]
00853B1C  BE 04 00 00 00                  mov esi, 4
00853B21  41 8B C2                        mov eax, r10d
00853B24  3B C6                           cmp eax, esi
00853B26  73 10                           jae 0x140853b38
00853B28  8B C8                           mov ecx, eax
00853B2A  42 80 7C 31 04 00               cmp byte ptr [rcx + r14 + 4], 0
00853B30  74 04                           je 0x140853b36
00853B32  FF C0                           inc eax
00853B34  EB EE                           jmp 0x140853b24
00853B36  8B F0                           mov esi, eax
00853B38  4D 85 C9                        test r9, r9
00853B3B  0F 85 9C 0B 00 00               jne 0x1408546dd
00853B41  41 0F B7 07                     movzx eax, word ptr [r15]
00853B45  D1 E8                           shr eax, 1
00853B47  3B C6                           cmp eax, esi
00853B49  48 8D 3C DD 00 00 00 00         lea rdi, [rbx*8]
00853B51  45 8B DA                        mov r11d, r10d
00853B54  0F 42 F0                        cmovb esi, eax
00853B57  44 3B DE                        cmp r11d, esi
00853B5A  0F 83 F9 00 00 00               jae 0x140853c59
00853B60  41 8B CB                        mov ecx, r11d
00853B63  4D 85 C9                        test r9, r9
00853B66  0F 85 0B 0B 00 00               jne 0x140854677
00853B6C  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
00853B70  44 0F B7 04 48                  movzx r8d, word ptr [rax + rcx*2]
00853B75  48 8D 04 39                     lea rax, [rcx + rdi]
00853B79  46 0F B6 4C 20 08               movzx r9d, byte ptr [rax + r12 + 8]
00853B7F  66 41 83 F8 61                  cmp r8w, 0x61
00853B84  73 4B                           jae 0x140853bd1
00853B86  45 0F B7 D0                     movzx r10d, r8w
00853B8A  41 83 F9 61                     cmp r9d, 0x61
00853B8E  73 11                           jae 0x140853ba1
00853B90  41 8B C1                        mov eax, r9d
00853B93  44 2B D0                        sub r10d, eax
00853B96  75 6A                           jne 0x140853c02
00853B98  4C 8B 4D 48                     mov r9, qword ptr [rbp + 0x48]
00853B9C  41 FF C3                        inc r11d
00853B9F  EB B6                           jmp 0x140853b57
00853BA1  41 83 F9 7A                     cmp r9d, 0x7a
00853BA5  0F 86 5C 03 00 00               jbe 0x140853f07
00853BAB  E8 40 A6 AA FF                  call 0x1402fe1f0
00853BB0  4C 8B 80 B0 04 00 00            mov r8, qword ptr [rax + 0x4b0]
00853BB7  4D 85 C0                        test r8, r8
00853BBA  74 0F                           je 0x140853bcb
00853BBC  B8 C0 00 00 00                  mov eax, 0xc0
00853BC1  66 44 3B C8                     cmp r9w, ax
00853BC5  0F 83 50 0A 00 00               jae 0x14085461b
00853BCB  41 0F B7 C1                     movzx eax, r9w
00853BCF  EB C2                           jmp 0x140853b93
00853BD1  66 41 83 F8 7A                  cmp r8w, 0x7a
00853BD6  0F 86 72 02 00 00               jbe 0x140853e4e
00853BDC  E8 0F A6 AA FF                  call 0x1402fe1f0
00853BE1  4C 8B 90 B0 04 00 00            mov r10, qword ptr [rax + 0x4b0]
00853BE8  4D 85 D2                        test r10, r10
00853BEB  74 0F                           je 0x140853bfc
00853BED  B8 C0 00 00 00                  mov eax, 0xc0
00853BF2  66 44 3B C0                     cmp r8w, ax
00853BF6  0F 83 42 0A 00 00               jae 0x14085463e
00853BFC  45 0F B7 D0                     movzx r10d, r8w
00853C00  EB 88                           jmp 0x140853b8a
00853C02  45 85 D2                        test r10d, r10d
00853C05  BA 01 00 00 00                  mov edx, 1
00853C0A  B8 FF FF FF FF                  mov eax, 0xffffffff
00853C0F  0F 4E D0                        cmovle edx, eax
00853C12  85 D2                           test edx, edx
00853C14  0F 84 60 09 00 00               je 0x14085457a
00853C1A  78 32                           js 0x140853c4e
00853C1C  44 8B 45 C4                     mov r8d, dword ptr [rbp - 0x3c]
00853C20  8B F3                           mov esi, ebx
00853C22  89 5D C0                        mov dword ptr [rbp - 0x40], ebx
00853C25  41 8B D8                        mov ebx, r8d
00853C28  BA 6C 66 00 00                  mov edx, 0x666c
00853C2D  2B DE                           sub ebx, esi
00853C2F  41 B8 FF FD 00 00               mov r8d, 0xfdff
00853C35  83 FB 01                        cmp ebx, 1
00853C38  0F 86 68 02 00 00               jbe 0x140853ea6
00853C3E  4C 8B 4D 48                     mov r9, qword ptr [rbp + 0x48]
00853C42  D1 EB                           shr ebx, 1
00853C44  03 DE                           add ebx, esi
00853C46  45 33 D2                        xor r10d, r10d
00853C49  E9 92 FE FF FF                  jmp 0x140853ae0
00853C4E  8B 75 C0                        mov esi, dword ptr [rbp - 0x40]
00853C51  44 8B C3                        mov r8d, ebx
00853C54  89 5D C4                        mov dword ptr [rbp - 0x3c], ebx
00853C57  EB CC                           jmp 0x140853c25
00853C59  4C 8B 6D 30                     mov r13, qword ptr [rbp + 0x30]
00853C5D  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00853C61  41 8B 54 DC 04                  mov edx, dword ptr [r12 + rbx*8 + 4]
00853C66  49 8B CD                        mov rcx, r13
00853C69  C7 45 D0 FF FF FF FF            mov dword ptr [rbp - 0x30], 0xffffffff
00853C70  C7 45 D4 00 00 00 00            mov dword ptr [rbp - 0x2c], 0
00853C77  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
00853C7F  0F 84 B1 02 00 00               je 0x140853f36
00853C85  E8 D6 0F 00 00                  call 0x140854c60
00853C8A  48 8B C8                        mov rcx, rax
00853C8D  48 85 C0                        test rax, rax
00853C90  0F 84 2F 09 00 00               je 0x1408545c5
00853C96  F6 40 02 20                     test byte ptr [rax + 2], 0x20
00853C9A  4C 8D 68 4C                     lea r13, [rax + 0x4c]
00853C9E  4C 8B 55 48                     mov r10, qword ptr [rbp + 0x48]
00853CA2  0F 84 E2 0A 00 00               je 0x14085478a
00853CA8  4D 85 D2                        test r10, r10
00853CAB  0F 85 6D 0A 00 00               jne 0x14085471e
00853CB1  41 0F B7 3F                     movzx edi, word ptr [r15]
00853CB5  4D 8B 67 08                     mov r12, qword ptr [r15 + 8]
00853CB9  44 0F B7 78 48                  movzx r15d, word ptr [rax + 0x48]
00853CBE  66 D1 EF                        shr di, 1
00853CC1  66 85 FF                        test di, di
00853CC4  74 6A                           je 0x140853d30
00853CC6  66 45 85 FF                     test r15w, r15w
00853CCA  74 64                           je 0x140853d30
00853CCC  41 0F B7 34 24                  movzx esi, word ptr [r12]
00853CD1  49 83 C4 02                     add r12, 2
00853CD5  45 0F B6 75 00                  movzx r14d, byte ptr [r13]
00853CDA  49 FF C5                        inc r13
00853CDD  66 41 3B F6                     cmp si, r14w
00853CE1  74 3F                           je 0x140853d22
00853CE3  66 83 FE 61                     cmp si, 0x61
00853CE7  0F 82 10 02 00 00               jb 0x140853efd
00853CED  66 83 FE 7A                     cmp si, 0x7a
00853CF1  0F 87 FB 01 00 00               ja 0x140853ef2
00853CF7  B8 E0 FF 00 00                  mov eax, 0xffe0
00853CFC  66 03 F0                        add si, ax
00853CFF  41 83 FE 61                     cmp r14d, 0x61
00853D03  72 0E                           jb 0x140853d13
00853D05  41 83 FE 7A                     cmp r14d, 0x7a
00853D09  0F 87 57 0A 00 00               ja 0x140854766
00853D0F  66 44 03 F0                     add r14w, ax
00853D13  41 0F B7 C6                     movzx eax, r14w
00853D17  0F B7 F6                        movzx esi, si
00853D1A  2B F0                           sub esi, eax
00853D1C  0F 85 B8 08 00 00               jne 0x1408545da
00853D22  BE FF FF 00 00                  mov esi, 0xffff
00853D27  66 03 FE                        add di, si
00853D2A  66 44 03 FE                     add r15w, si
00853D2E  EB 91                           jmp 0x140853cc1
00853D30  4C 8B 65 38                     mov r12, qword ptr [rbp + 0x38]
00853D34  4C 8B 75 D8                     mov r14, qword ptr [rbp - 0x28]
00853D38  41 0F B7 C7                     movzx eax, r15w
00853D3C  4C 8B 7D 40                     mov r15, qword ptr [rbp + 0x40]
00853D40  0F B7 F7                        movzx esi, di
00853D43  2B F0                           sub esi, eax
00853D45  4C 8B 6D 30                     mov r13, qword ptr [rbp + 0x30]
00853D49  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00853D4D  49 8B CD                        mov rcx, r13
00853D50  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
00853D58  0F 85 0F 09 00 00               jne 0x14085466d
00853D5E  E8 DD 21 00 00                  call 0x140855f40
00853D63  85 F6                           test esi, esi
00853D65  0F 84 BA 01 00 00               je 0x140853f25
00853D6B  0F 88 2B 01 00 00               js 0x140853e9c
00853D71  BA 01 00 00 00                  mov edx, 1
00853D76  E9 97 FE FF FF                  jmp 0x140853c12
00853D7B  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
00853D83  4C 8D 45 C8                     lea r8, [rbp - 0x38]
00853D87  41 8B 54 9C 04                  mov edx, dword ptr [r12 + rbx*4 + 4]
00853D8C  49 8B CD                        mov rcx, r13
00853D8F  C7 45 C8 FF FF FF FF            mov dword ptr [rbp - 0x38], 0xffffffff
00853D96  C7 45 CC 00 00 00 00            mov dword ptr [rbp - 0x34], 0
00853D9D  0F 84 9D 01 00 00               je 0x140853f40
00853DA3  E8 B8 0E 00 00                  call 0x140854c60
00853DA8  48 8B C8                        mov rcx, rax
00853DAB  48 85 C0                        test rax, rax
00853DAE  0F 84 06 05 00 00               je 0x1408542ba
00853DB4  F6 40 02 20                     test byte ptr [rax + 2], 0x20
00853DB8  4C 8D 68 4C                     lea r13, [rax + 0x4c]
00853DBC  4C 8B 55 48                     mov r10, qword ptr [rbp + 0x48]
00853DC0  0F 84 F9 09 00 00               je 0x1408547bf
00853DC6  4D 85 D2                        test r10, r10
00853DC9  0F 85 6B 09 00 00               jne 0x14085473a
00853DCF  41 0F B7 3F                     movzx edi, word ptr [r15]
00853DD3  4D 8B 67 08                     mov r12, qword ptr [r15 + 8]
00853DD7  44 0F B7 78 48                  movzx r15d, word ptr [rax + 0x48]
00853DDC  66 D1 EF                        shr di, 1
00853DDF  66 85 FF                        test di, di
00853DE2  74 77                           je 0x140853e5b
00853DE4  66 45 85 FF                     test r15w, r15w
00853DE8  74 71                           je 0x140853e5b
00853DEA  41 0F B7 34 24                  movzx esi, word ptr [r12]
00853DEF  49 83 C4 02                     add r12, 2
00853DF3  45 0F B6 75 00                  movzx r14d, byte ptr [r13]
00853DF8  49 FF C5                        inc r13
00853DFB  66 41 3B F6                     cmp si, r14w
00853DFF  74 3F                           je 0x140853e40
00853E01  66 83 FE 61                     cmp si, 0x61
00853E05  0F 82 10 01 00 00               jb 0x140853f1b
00853E0B  66 83 FE 7A                     cmp si, 0x7a
00853E0F  0F 87 FB 00 00 00               ja 0x140853f10
00853E15  B8 E0 FF 00 00                  mov eax, 0xffe0
00853E1A  66 03 F0                        add si, ax
00853E1D  41 83 FE 61                     cmp r14d, 0x61
00853E21  72 0E                           jb 0x140853e31
00853E23  41 83 FE 7A                     cmp r14d, 0x7a
00853E27  0F 87 4B 09 00 00               ja 0x140854778
00853E2D  66 44 03 F0                     add r14w, ax
00853E31  41 0F B7 C6                     movzx eax, r14w
00853E35  0F B7 F6                        movzx esi, si
00853E38  2B F0                           sub esi, eax
00853E3A  0F 85 B7 07 00 00               jne 0x1408545f7
00853E40  BE FF FF 00 00                  mov esi, 0xffff
00853E45  66 03 FE                        add di, si
00853E48  66 44 03 FE                     add r15w, si
00853E4C  EB 91                           jmp 0x140853ddf
00853E4E  45 0F B7 D0                     movzx r10d, r8w
00853E52  41 83 EA 20                     sub r10d, 0x20
00853E56  E9 2F FD FF FF                  jmp 0x140853b8a
00853E5B  4C 8B 65 38                     mov r12, qword ptr [rbp + 0x38]
00853E5F  4C 8B 75 50                     mov r14, qword ptr [rbp + 0x50]
00853E63  41 0F B7 C7                     movzx eax, r15w
00853E67  4C 8B 7D 40                     mov r15, qword ptr [rbp + 0x40]
00853E6B  0F B7 F7                        movzx esi, di
00853E6E  2B F0                           sub esi, eax
00853E70  4C 8B 6D 30                     mov r13, qword ptr [rbp + 0x30]
00853E74  48 8D 55 C8                     lea rdx, [rbp - 0x38]
00853E78  49 8B CD                        mov rcx, r13
00853E7B  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
00853E83  0F 85 FC 07 00 00               jne 0x140854685
00853E89  E8 B2 20 00 00                  call 0x140855f40
00853E8E  85 F6                           test esi, esi
00853E90  0F 84 4D 01 00 00               je 0x140853fe3
00853E96  0F 89 D5 FE FF FF               jns 0x140853d71
00853E9C  BA FF FF FF FF                  mov edx, 0xffffffff
00853EA1  E9 6C FD FF FF                  jmp 0x140853c12
00853EA6  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
00853EAB  4C 8B 75 50                     mov r14, qword ptr [rbp + 0x50]
00853EAF  0F B7 C1                        movzx eax, cx
00853EB2  66 2B C2                        sub ax, dx
00853EB5  66 41 85 C0                     test r8w, ax
00853EB9  8B C6                           mov eax, esi
00853EBB  41 C7 06 FF FF FF FF            mov dword ptr [r14], 0xffffffff
00853EC2  0F 85 A2 02 00 00               jne 0x14085416a
00853EC8  4D 8D 2C C4                     lea r13, [r12 + rax*8]
00853ECC  66 3B CA                        cmp cx, dx
00853ECF  0F 85 0B 04 00 00               jne 0x1408542e0
00853ED5  33 D2                           xor edx, edx
00853ED7  41 BE 04 00 00 00               mov r14d, 4
00853EDD  8B CA                           mov ecx, edx
00853EDF  90                              nop
00853EE0  41 3B CE                        cmp ecx, r14d
00853EE3  73 68                           jae 0x140853f4d
00853EE5  8B C1                           mov eax, ecx
00853EE7  42 38 54 28 08                  cmp byte ptr [rax + r13 + 8], dl
00853EEC  74 5C                           je 0x140853f4a
00853EEE  FF C1                           inc ecx
00853EF0  EB EE                           jmp 0x140853ee0
00853EF2  0F B7 CE                        movzx ecx, si
00853EF5  E8 F6 B1 00 00                  call 0x14085f0f0
00853EFA  0F B7 F0                        movzx esi, ax
00853EFD  B8 E0 FF 00 00                  mov eax, 0xffe0
00853F02  E9 F8 FD FF FF                  jmp 0x140853cff
00853F07  41 8D 41 E0                     lea eax, [r9 - 0x20]
00853F0B  E9 83 FC FF FF                  jmp 0x140853b93
00853F10  0F B7 CE                        movzx ecx, si
00853F13  E8 D8 B1 00 00                  call 0x14085f0f0
00853F18  0F B7 F0                        movzx esi, ax
00853F1B  B8 E0 FF 00 00                  mov eax, 0xffe0
00853F20  E9 F8 FE FF FF                  jmp 0x140853e1d
00853F25  4C 8B 45 50                     mov r8, qword ptr [rbp + 0x50]
00853F29  33 D2                           xor edx, edx
00853F2B  41 8B 06                        mov eax, dword ptr [r14]
00853F2E  41 89 00                        mov dword ptr [r8], eax
00853F31  E9 DC FC FF FF                  jmp 0x140853c12
00853F36  E8 75 0D 00 00                  call 0x140854cb0
00853F3B  E9 4A FD FF FF                  jmp 0x140853c8a
00853F40  E8 6B 0D 00 00                  call 0x140854cb0
00853F45  E9 5E FE FF FF                  jmp 0x140853da8
00853F4A  44 8B F1                        mov r14d, ecx
00853F4D  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
00853F51  48 85 DB                        test rbx, rbx
00853F54  0F 85 FC 07 00 00               jne 0x140854756
00853F5A  41 0F B7 07                     movzx eax, word ptr [r15]
00853F5E  D1 E8                           shr eax, 1
00853F60  41 3B C6                        cmp eax, r14d
00853F63  8B FA                           mov edi, edx
00853F65  44 0F 42 F0                     cmovb r14d, eax
00853F69  8B C6                           mov eax, esi
00853F6B  4C 8D 3C C5 00 00 00 00         lea r15, [rax*8]
00853F73  41 3B FE                        cmp edi, r14d
00853F76  0F 83 1F 06 00 00               jae 0x14085459b
00853F7C  8B D7                           mov edx, edi
00853F7E  48 85 DB                        test rbx, rbx
00853F81  0F 85 73 07 00 00               jne 0x1408546fa
00853F87  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
00853F8B  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00853F8F  0F B7 0C 50                     movzx ecx, word ptr [rax + rdx*2]
00853F93  4A 8D 04 3A                     lea rax, [rdx + r15]
00853F97  42 0F B6 74 20 08               movzx esi, byte ptr [rax + r12 + 8]
00853F9D  66 83 F9 61                     cmp cx, 0x61
00853FA1  73 2C                           jae 0x140853fcf
00853FA3  0F B7 D9                        movzx ebx, cx
00853FA6  83 FE 61                        cmp esi, 0x61
00853FA9  73 0E                           jae 0x140853fb9
00853FAB  8B C6                           mov eax, esi
00853FAD  2B D8                           sub ebx, eax
00853FAF  75 41                           jne 0x140853ff2
00853FB1  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
00853FB5  FF C7                           inc edi
00853FB7  EB BA                           jmp 0x140853f73
00853FB9  83 FE 7A                        cmp esi, 0x7a
00853FBC  0F 86 5E 05 00 00               jbe 0x140854520
00853FC2  0F B7 CE                        movzx ecx, si
00853FC5  E8 26 B1 00 00                  call 0x14085f0f0
00853FCA  0F B7 C0                        movzx eax, ax
00853FCD  EB DE                           jmp 0x140853fad
00853FCF  66 83 F9 7A                     cmp cx, 0x7a
00853FD3  0F 86 66 02 00 00               jbe 0x14085423f
00853FD9  E8 12 B1 00 00                  call 0x14085f0f0
00853FDE  0F B7 D8                        movzx ebx, ax
00853FE1  EB C3                           jmp 0x140853fa6
00853FE3  41 8B 4C 9C 04                  mov ecx, dword ptr [r12 + rbx*4 + 4]
00853FE8  33 D2                           xor edx, edx
00853FEA  41 89 0E                        mov dword ptr [r14], ecx
00853FED  E9 20 FC FF FF                  jmp 0x140853c12
00853FF2  85 DB                           test ebx, ebx
00853FF4  BA 01 00 00 00                  mov edx, 1
00853FF9  B8 FF FF FF FF                  mov eax, 0xffffffff
00853FFE  0F 4E D0                        cmovle edx, eax
00854001  85 D2                           test edx, edx
00854003  0F 84 86 06 00 00               je 0x14085468f
00854009  0F 88 F9 05 00 00               js 0x140854608
0085400F  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
00854014  BA 6C 66 00 00                  mov edx, 0x666c
00854019  4C 8B 75 50                     mov r14, qword ptr [rbp + 0x50]
0085401D  0F B7 C1                        movzx eax, cx
00854020  44 8B 7D C4                     mov r15d, dword ptr [rbp - 0x3c]
00854024  66 2B C2                        sub ax, dx
00854027  41 B8 FF FD 00 00               mov r8d, 0xfdff
0085402D  41 C7 06 FF FF FF FF            mov dword ptr [r14], 0xffffffff
00854034  66 41 85 C0                     test r8w, ax
00854038  0F 85 57 02 00 00               jne 0x140854295
0085403E  4F 8D 2C FC                     lea r13, [r12 + r15*8]
00854042  66 3B CA                        cmp cx, dx
00854045  0F 85 B5 03 00 00               jne 0x140854400
0085404B  33 F6                           xor esi, esi
0085404D  8B CE                           mov ecx, esi
0085404F  90                              nop
00854050  83 F9 04                        cmp ecx, 4
00854053  73 0D                           jae 0x140854062
00854055  8B C1                           mov eax, ecx
00854057  42 38 74 28 08                  cmp byte ptr [rax + r13 + 8], sil
0085405C  74 09                           je 0x140854067
0085405E  FF C1                           inc ecx
00854060  EB EE                           jmp 0x140854050
00854062  B9 04 00 00 00                  mov ecx, 4
00854067  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
0085406B  48 85 DB                        test rbx, rbx
0085406E  0F 85 EA 06 00 00               jne 0x14085475e
00854074  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
00854078  0F B7 00                        movzx eax, word ptr [rax]
0085407B  D1 E8                           shr eax, 1
0085407D  3B C1                           cmp eax, ecx
0085407F  4E 8D 34 FD 00 00 00 00         lea r14, [r15*8]
00854087  8B FE                           mov edi, esi
00854089  0F 42 C8                        cmovb ecx, eax
0085408C  89 4D 38                        mov dword ptr [rbp + 0x38], ecx
0085408F  3B F9                           cmp edi, ecx
00854091  0F 83 10 05 00 00               jae 0x1408545a7
00854097  8B D7                           mov edx, edi
00854099  48 85 DB                        test rbx, rbx
0085409C  0F 85 6F 06 00 00               jne 0x140854711
008540A2  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
008540A6  48 8B 40 08                     mov rax, qword ptr [rax + 8]
008540AA  0F B7 0C 50                     movzx ecx, word ptr [rax + rdx*2]
008540AE  4A 8D 04 32                     lea rax, [rdx + r14]
008540B2  42 0F B6 74 20 08               movzx esi, byte ptr [rax + r12 + 8]
008540B8  66 83 F9 61                     cmp cx, 0x61
008540BC  73 2F                           jae 0x1408540ed
008540BE  0F B7 D9                        movzx ebx, cx
008540C1  83 FE 61                        cmp esi, 0x61
008540C4  73 11                           jae 0x1408540d7
008540C6  8B C6                           mov eax, esi
008540C8  2B D8                           sub ebx, eax
008540CA  75 35                           jne 0x140854101
008540CC  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
008540D0  FF C7                           inc edi
008540D2  8B 4D 38                        mov ecx, dword ptr [rbp + 0x38]
008540D5  EB B8                           jmp 0x14085408f
008540D7  83 FE 7A                        cmp esi, 0x7a
008540DA  0F 86 72 04 00 00               jbe 0x140854552
008540E0  0F B7 CE                        movzx ecx, si
008540E3  E8 08 B0 00 00                  call 0x14085f0f0
008540E8  0F B7 C0                        movzx eax, ax
008540EB  EB DB                           jmp 0x1408540c8
008540ED  66 83 F9 7A                     cmp cx, 0x7a
008540F1  0F 86 DE 01 00 00               jbe 0x1408542d5
008540F7  E8 F4 AF 00 00                  call 0x14085f0f0
008540FC  0F B7 D8                        movzx ebx, ax
008540FF  EB C0                           jmp 0x1408540c1
00854101  85 DB                           test ebx, ebx
00854103  B9 01 00 00 00                  mov ecx, 1
00854108  B8 FF FF FF FF                  mov eax, 0xffffffff
0085410D  0F 4E C8                        cmovle ecx, eax
00854110  83 F9 02                        cmp ecx, 2
00854113  0F 84 AC 04 00 00               je 0x1408545c5
00854119  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0085411D  F7 D9                           neg ecx
0085411F  44 89 38                        mov dword ptr [rax], r15d
00854122  1B C0                           sbb eax, eax
00854124  25 34 00 00 C0                  and eax, 0xc0000034
00854129  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
0085412E  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00854133  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
00854138  48 83 C4 70                     add rsp, 0x70
0085413C  41 5F                           pop r15
0085413E  41 5D                           pop r13
00854140  41 5C                           pop r12
00854142  5B                              pop rbx
00854143  5D                              pop rbp
00854144  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00853ABC(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13)
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

    *(unsigned __int64 *)(v_r11 - 48) = v_rsi;
    *(unsigned __int64 *)(v_r11 - 56) = v_rdi;
    *(unsigned __int64 *)(v_r11 - 64) = v_r14;
loc_00853AE0:
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_r12))) - ((unsigned __int16)((unsigned int)(0x666CULL))));
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 80)) = 0xFFFFFFFFULL;
    if ((((unsigned __int16)((unsigned int)(0xFDFFULL))) & ((unsigned __int16)(result))) != 0) goto loc_00853D7B;
    v_r14 = (v_rbx * 8 + 4) + (v_r12);
    *(unsigned __int64 *)(v_rbp - 40) = v_r14;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r12))) != ((unsigned __int16)((unsigned int)(0x666CULL)))) goto loc_00853C59;
loc_00853B24:
    if (((unsigned int)((unsigned int)((unsigned int)(v_r10)))) >= 4) goto loc_00853B38;
    if ((*(unsigned __int8 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r10)))) + v_r14 * 1 + 4)) == 0) goto loc_00853B36;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) + 1);
    goto loc_00853B24;
loc_00853B36:
loc_00853B38:
    result = (unsigned int)((*(unsigned __int16 *)(v_r15)) >> (1));
    v_rsi = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)((unsigned int)(result))))) { v_rsi = (unsigned int)(result); }
loc_00853B57:
    if (((unsigned int)((unsigned int)((unsigned int)(v_r10)))) >= ((unsigned int)(v_rsi))) goto loc_00853C59;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r15 + 8) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r10)))) * 2))) >= 97) goto loc_00853BD1;
loc_00853B8A:
    if (((unsigned int)(*(unsigned __int8 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r10)))) + v_rbx * 8 * 1 + v_r12 * 1 + 8))) >= 97) goto loc_00853BA1;
loc_00853B93:
    v_r10 = (unsigned int)(((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r15 + 8) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r10)))) * 2))) - ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r10)))) + v_rbx * 8 * 1 + v_r12 * 1 + 8))))));
    if (condition_is_not_equal) goto loc_00853C02;
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) + 1);
    goto loc_00853B57;
loc_00853BA1:
    if (((unsigned int)(*(unsigned __int64 *)(v_rbp + 72))) <= 122) goto loc_00853F07;
    result = PsGetCurrentServerSiloGlobals((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r10)))), (unsigned int)(0x666CULL), *(unsigned __int16 *)(*(unsigned __int64 *)(v_r15 + 8) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r10)))) * 2), *(unsigned __int64 *)(v_rbp + 72));
    if (*(unsigned __int64 *)(result + 1200) == 0) goto loc_00853BCB;
loc_00853BCB:
    goto loc_00853B93;
loc_00853BD1:
    if (((unsigned __int16)(*(unsigned __int64 *)(result + 1200))) <= 122) goto loc_00853E4E;
    result = PsGetCurrentServerSiloGlobals((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r10)))), (unsigned int)(0x666CULL), *(unsigned __int64 *)(result + 1200), *(unsigned __int64 *)(v_rbp + 72));
    if (*(unsigned __int64 *)(result + 1200) == 0) goto loc_00853BFC;
loc_00853BFC:
    goto loc_00853B8A;
loc_00853C02:
    a2 = 1;
    if (condition_is_less_or_equal) { a2 = (unsigned int)((unsigned int)(0xFFFFFFFFULL)); }
loc_00853C12:
    if (sign_flag) goto loc_00853C4E;
    *(unsigned int *)(v_rbp - 64) = (unsigned int)(v_rbx);
loc_00853C25:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 60))))) - ((unsigned int)((unsigned int)((unsigned int)(v_rbx)))));
    if (((unsigned int)(v_rbx)) <= 1) goto loc_00853EA6;
    v_rbx = (unsigned int)((v_rbx) >> (1));
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)((unsigned int)((unsigned int)(v_rbx)))));
    v_r10 = 0;
    goto loc_00853AE0;
loc_00853C4E:
    *(unsigned int *)(v_rbp - 60) = (unsigned int)(v_rbx);
    goto loc_00853C25;
loc_00853C59:
    *(unsigned int *)(v_rbp - 48) = 0xFFFFFFFFULL;
    *(unsigned int *)(v_rbp - 44) = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 48) + 140)) & (1)) == 0) goto loc_00853F36;
    result = HvpGetCellFlat(*(unsigned __int64 *)(v_rbp + 48), (unsigned int)(*(unsigned int *)(v_r12 + v_rbx * 8 + 4)), v_rbp - 48, *(unsigned __int64 *)(v_rbp + 72));
loc_00853C8A:
    v_rdi = (unsigned __int16)((*(unsigned __int16 *)(v_r15)) >> (1));
loc_00853CC1:
    if ((unsigned __int16)(v_rdi) == 0) goto loc_00853D30;
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 72)) == 0) goto loc_00853D30;
    v_r12 = (*(unsigned __int64 *)(v_r15 + 8)) + (2);
    v_r13 = (result + 76) + 1;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r15 + 8)))) == ((unsigned __int16)(*(unsigned __int8 *)(result + 76)))) goto loc_00853D22;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r15 + 8)))) < 97) goto loc_00853EFD;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r15 + 8)))) > 122) goto loc_00853EF2;
    v_rsi = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_r15 + 8))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_00853CFF:
    if (((unsigned int)(*(unsigned __int8 *)(result + 76))) < 97) goto loc_00853D13;
    v_r14 = (unsigned __int16)((*(unsigned __int8 *)(result + 76)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_00853D13:
    v_rsi = (unsigned int)(((unsigned __int16)(v_rsi)) - ((unsigned int)((unsigned __int16)(v_r14))));
loc_00853D22:
    v_rdi = (unsigned __int16)((v_rdi) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    v_r15 = (unsigned __int16)((*(unsigned __int16 *)(result + 72)) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    goto loc_00853CC1;
loc_00853D30:
    v_rsi = (unsigned int)(((unsigned __int16)(v_rdi)) - ((unsigned int)((unsigned __int16)(v_r15))));
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_rbp + 48), v_rbp - 48, v_rbp - 48, *(unsigned __int64 *)(v_rbp + 72));
    if ((unsigned int)(v_rsi) == 0) goto loc_00853F25;
    if (sign_flag) goto loc_00853E9C;
loc_00853D71:
    goto loc_00853C12;
loc_00853D7B:
    *(unsigned int *)(v_rbp - 56) = 0xFFFFFFFFULL;
    *(unsigned int *)(v_rbp - 52) = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rbp + 48) + 140)) & (1)) == 0) goto loc_00853F40;
    result = HvpGetCellFlat(*(unsigned __int64 *)(v_rbp + 48), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp + 56) + v_rbx * 4 + 4)), v_rbp - 56, *(unsigned __int64 *)(v_rbp + 72));
loc_00853DA8:
    v_rdi = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp + 64))) >> (1));
loc_00853DDF:
    if ((unsigned __int16)(v_rdi) == 0) goto loc_00853E5B;
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 72)) == 0) goto loc_00853E5B;
    v_r12 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 64) + 8)) + (2);
    v_r13 = (result + 76) + 1;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 64) + 8)))) == ((unsigned __int16)(*(unsigned __int8 *)(result + 76)))) goto loc_00853E40;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 64) + 8)))) < 97) goto loc_00853F1B;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 64) + 8)))) > 122) goto loc_00853F10;
    v_rsi = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 64) + 8))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_00853E1D:
    if (((unsigned int)(*(unsigned __int8 *)(result + 76))) < 97) goto loc_00853E31;
    v_r14 = (unsigned __int16)((*(unsigned __int8 *)(result + 76)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_00853E31:
    v_rsi = (unsigned int)(((unsigned __int16)(v_rsi)) - ((unsigned int)((unsigned __int16)(v_r14))));
loc_00853E40:
    v_rdi = (unsigned __int16)((v_rdi) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    v_r15 = (unsigned __int16)((*(unsigned __int16 *)(result + 72)) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    goto loc_00853DDF;
loc_00853E4E:
    v_r10 = (unsigned int)(((unsigned __int16)(v_rbp - 56)) - (32));
    goto loc_00853B8A;
loc_00853E5B:
    v_rsi = (unsigned int)(((unsigned __int16)(v_rdi)) - ((unsigned int)((unsigned __int16)(v_r15))));
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_rbp + 48), v_rbp - 56, v_rbp - 56, *(unsigned __int64 *)(v_rbp + 72));
    if ((unsigned int)(v_rsi) == 0) goto loc_00853FE3;
    if (!sign_flag) goto loc_00853D71;
loc_00853E9C:
    goto loc_00853C12;
loc_00853EA6:
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp + 56)))) - ((unsigned __int16)((unsigned int)(0xFFFFFFFFULL))));
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 80)) = 0xFFFFFFFFULL;
    a2 = 0;
loc_00853EE0:
    if (0 >= 4) goto loc_00853F4D;
    if ((*(unsigned __int8 *)(0 + *(unsigned __int64 *)(v_rbp + 56) + (unsigned int)((unsigned int)(v_rsi)) * 8 * 1 + 8)) == 0) goto loc_00853F4A;
    a1 = (unsigned int)((0) + 1);
    goto loc_00853EE0;
loc_00853EF2:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(v_rsi), a2, v_rbp - 56, *(unsigned __int64 *)(v_rbp + 72));
loc_00853EFD:
    goto loc_00853CFF;
loc_00853F07:
    goto loc_00853B93;
loc_00853F10:
    result = RtlUpcaseUnicodeChar((unsigned __int16)((unsigned __int16)(result)), a2, v_rbp - 56, *(unsigned __int64 *)(v_rbp + 72));
loc_00853F1B:
    goto loc_00853E1D;
loc_00853F25:
    a2 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 80)) = (unsigned int)((unsigned int)(*(unsigned int *)(4)));
    goto loc_00853C12;
loc_00853F36:
    result = HvpGetCellPaged((unsigned __int16)((unsigned __int16)(result)), a2, *(unsigned __int64 *)(v_rbp + 80), *(unsigned __int64 *)(v_rbp + 72));
    goto loc_00853C8A;
loc_00853F40:
    result = HvpGetCellPaged((unsigned __int16)((unsigned __int16)(result)), a2, *(unsigned __int64 *)(v_rbp + 80), *(unsigned __int64 *)(v_rbp + 72));
    goto loc_00853DA8;
loc_00853F4A:
loc_00853F4D:
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp + 64))) >> (1));
    v_r14 = (unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result))));
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)((unsigned int)((unsigned __int16)((unsigned __int16)(result))))))) { v_r14 = (unsigned int)(result); }
loc_00853F73:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 64) + 8) + 0 * 2))) >= 97) goto loc_00853FCF;
loc_00853FA6:
    if (((unsigned int)(*(unsigned __int8 *)(0 + (unsigned int)((unsigned int)((unsigned __int16)(result))) * 8 * 1 + *(unsigned __int64 *)(v_rbp + 56) * 1 + 8))) >= 97) goto loc_00853FB9;
loc_00853FAD:
    v_rbx = (unsigned int)(((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 64) + 8) + 0 * 2))) - ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)(0 + (unsigned int)((unsigned int)((unsigned __int16)(result))) * 8 * 1 + *(unsigned __int64 *)(v_rbp + 56) * 1 + 8))))));
    if (condition_is_not_equal) goto loc_00853FF2;
    v_rdi = (unsigned int)((0) + 1);
    goto loc_00853F73;
loc_00853FB9:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(*(unsigned __int8 *)(0 + (unsigned int)((unsigned int)((unsigned __int16)(result))) * 8 * 1 + *(unsigned __int64 *)(v_rbp + 56) * 1 + 8)), 0, *(unsigned __int64 *)(v_rbp + 80), *(unsigned __int64 *)(v_rbp + 72));
    goto loc_00853FAD;
loc_00853FCF:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(*(unsigned __int8 *)(0 + (unsigned int)((unsigned int)((unsigned __int16)(result))) * 8 * 1 + *(unsigned __int64 *)(v_rbp + 56) * 1 + 8)), 0, *(unsigned __int64 *)(v_rbp + 80), *(unsigned __int64 *)(v_rbp + 72));
    goto loc_00853FA6;
loc_00853FE3:
    a2 = 0;
    *(unsigned int *)(v_r14) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp + 56) + (unsigned __int16)(result) * 4 + 4)));
    goto loc_00853C12;
loc_00853FF2:
    a2 = 1;
    if (condition_is_less_or_equal) { a2 = (unsigned int)((unsigned int)(0xFFFFFFFFULL)); }
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp + 56)))) - ((unsigned __int16)((unsigned int)(0x666CULL))));
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 80)) = 0xFFFFFFFFULL;
    v_rsi = 0;
loc_00854050:
    if (0 >= 4) goto loc_00854062;
    if ((*(unsigned __int8 *)(0 + *(unsigned __int64 *)(v_rbp + 56) + (unsigned int)(*(unsigned int *)(v_rbp - 60)) * 8 * 1 + 8)) == 0) goto loc_00854067;
    a1 = (unsigned int)((0) + 1);
    goto loc_00854050;
loc_00854062:
loc_00854067:
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp + 64))) >> (1));
    a1 = 4;
    if (((unsigned int)(result)) < 4) { a1 = (unsigned int)(result); }
    *(unsigned int *)(v_rbp + 56) = (unsigned int)(a1);
loc_0085408F:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 64) + 8) + 0 * 2))) >= 97) goto loc_008540ED;
loc_008540C1:
    if (((unsigned int)(*(unsigned __int8 *)(0 + (unsigned int)(*(unsigned int *)(v_rbp - 60)) * 8 * 1 + *(unsigned __int64 *)(v_rbp + 56) * 1 + 8))) >= 97) goto loc_008540D7;
loc_008540C8:
    v_rbx = (unsigned int)(((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 64) + 8) + 0 * 2))) - ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)(0 + (unsigned int)(*(unsigned int *)(v_rbp - 60)) * 8 * 1 + *(unsigned __int64 *)(v_rbp + 56) * 1 + 8))))));
    if (condition_is_not_equal) goto loc_00854101;
    v_rdi = (unsigned int)((0) + 1);
    goto loc_0085408F;
loc_008540D7:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(*(unsigned __int8 *)(0 + (unsigned int)(*(unsigned int *)(v_rbp - 60)) * 8 * 1 + *(unsigned __int64 *)(v_rbp + 56) * 1 + 8)), 0, (unsigned int)(0xFDFFULL), *(unsigned __int64 *)(v_rbp + 72));
    goto loc_008540C8;
loc_008540ED:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(*(unsigned __int8 *)(0 + (unsigned int)(*(unsigned int *)(v_rbp - 60)) * 8 * 1 + *(unsigned __int64 *)(v_rbp + 56) * 1 + 8)), 0, (unsigned int)(0xFDFFULL), *(unsigned __int64 *)(v_rbp + 72));
    goto loc_008540C1;
loc_00854101:
    a1 = 1;
    if (condition_is_less_or_equal) { a1 = (unsigned int)((unsigned int)(0xFFFFFFFFULL)); }
    a1 = (unsigned int)(-(a1));
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 88)) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 60)));
    result = (unsigned int)((*(unsigned __int64 *)(v_rbp + 88)) & (0xC0000034ULL));
    v_rsp = (v_rsp) + (112);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00853ABC(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, int64_t Arg11, int64_t Arg12, int64_t Arg13)
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

    *(uint64_t *)(local_r11 - 0x30) = local_rsi;
    *(uint64_t *)(local_r11 - 0x38) = local_rdi;
    *(uint64_t *)(local_r11 - 0x40) = local_r14;
loc_00853AE0:
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(local_r12))) - ((uint16_t)((uint32_t)(0x666CULL))));
    *(uint32_t *)(*(uint64_t *)(local_rbp + 0x50)) = 0xFFFFFFFFULL;
    if ((((uint16_t)((uint32_t)(0xFDFFULL))) & ((uint16_t)(result))) != 0) goto loc_00853D7B;
    local_r14 = (local_rbx * 8 + 4) + (local_r12);
    *(uint64_t *)(local_rbp - 0x28) = local_r14;
    if (((uint16_t)(*(uint16_t *)(local_r12))) != ((uint16_t)((uint32_t)(0x666CULL)))) goto loc_00853C59;
loc_00853B24:
    if (((uint32_t)((uint32_t)((uint32_t)(local_r10)))) >= 4) goto loc_00853B38;
    if ((*(uint8_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r10)))) + local_r14 * 1 + 0x4)) == 0) goto loc_00853B36;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) + 1);
    goto loc_00853B24;
loc_00853B36:
loc_00853B38:
    result = (uint32_t)((*(uint16_t *)(local_r15)) >> (1));
    local_rsi = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)((uint32_t)(result))))) { local_rsi = (uint32_t)(result); }
loc_00853B57:
    if (((uint32_t)((uint32_t)((uint32_t)(local_r10)))) >= ((uint32_t)(local_rsi))) goto loc_00853C59;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r15 + 0x8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r10)))) * 2))) >= 97) goto loc_00853BD1;
loc_00853B8A:
    if (((uint32_t)(*(uint8_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r10)))) + local_rbx * 8 * 1 + local_r12 * 1 + 0x8))) >= 97) goto loc_00853BA1;
loc_00853B93:
    local_r10 = (uint32_t)(((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r15 + 0x8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r10)))) * 2))) - ((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r10)))) + local_rbx * 8 * 1 + local_r12 * 1 + 0x8))))));
    if (condition_is_not_equal) goto loc_00853C02;
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) + 1);
    goto loc_00853B57;
loc_00853BA1:
    if (((uint32_t)(*(uint64_t *)(local_rbp + 0x48))) <= 122) goto loc_00853F07;
    result = PsGetCurrentServerSiloGlobals((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r10)))), (uint32_t)(0x666CULL), *(uint16_t *)(*(uint64_t *)(local_r15 + 0x8) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r10)))) * 2), *(uint64_t *)(local_rbp + 0x48));
    if (*(uint64_t *)(result + 0x4B0) == 0) goto loc_00853BCB;
loc_00853BCB:
    goto loc_00853B93;
loc_00853BD1:
    if (((uint16_t)(*(uint64_t *)(result + 0x4B0))) <= 122) goto loc_00853E4E;
    result = PsGetCurrentServerSiloGlobals((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r10)))), (uint32_t)(0x666CULL), *(uint64_t *)(result + 0x4B0), *(uint64_t *)(local_rbp + 0x48));
    if (*(uint64_t *)(result + 0x4B0) == 0) goto loc_00853BFC;
loc_00853BFC:
    goto loc_00853B8A;
loc_00853C02:
    Arg2 = 1;
    if (condition_is_less_or_equal) { Arg2 = (uint32_t)((uint32_t)(0xFFFFFFFFULL)); }
loc_00853C12:
    if (sign_flag) goto loc_00853C4E;
    *(uint32_t *)(local_rbp - 0x40) = (uint32_t)(local_rbx);
loc_00853C25:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x3C))))) - ((uint32_t)((uint32_t)((uint32_t)(local_rbx)))));
    if (((uint32_t)(local_rbx)) <= 1) goto loc_00853EA6;
    local_rbx = (uint32_t)((local_rbx) >> (1));
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)((uint32_t)((uint32_t)(local_rbx)))));
    local_r10 = 0;
    goto loc_00853AE0;
loc_00853C4E:
    *(uint32_t *)(local_rbp - 0x3C) = (uint32_t)(local_rbx);
    goto loc_00853C25;
loc_00853C59:
    *(uint32_t *)(local_rbp - 0x30) = 0xFFFFFFFFULL;
    *(uint32_t *)(local_rbp - 0x2C) = 0;
    if (((*(uint8_t *)(*(uint64_t *)(local_rbp + 0x30) + 0x8C)) & (1)) == 0) goto loc_00853F36;
    result = HvpGetCellFlat(*(uint64_t *)(local_rbp + 0x30), (uint32_t)(*(uint32_t *)(local_r12 + local_rbx * 8 + 0x4)), local_rbp - 48, *(uint64_t *)(local_rbp + 0x48));
loc_00853C8A:
    local_rdi = (uint16_t)((*(uint16_t *)(local_r15)) >> (1));
loc_00853CC1:
    if ((uint16_t)(local_rdi) == 0) goto loc_00853D30;
    if ((uint16_t)(*(uint16_t *)(result + 0x48)) == 0) goto loc_00853D30;
    local_r12 = (*(uint64_t *)(local_r15 + 0x8)) + (2);
    local_r13 = (result + 76) + 1;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r15 + 0x8)))) == ((uint16_t)(*(uint8_t *)(result + 0x4C)))) goto loc_00853D22;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r15 + 0x8)))) < 97) goto loc_00853EFD;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r15 + 0x8)))) > 122) goto loc_00853EF2;
    local_rsi = (uint16_t)((*(uint16_t *)(*(uint64_t *)(local_r15 + 0x8))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_00853CFF:
    if (((uint32_t)(*(uint8_t *)(result + 0x4C))) < 97) goto loc_00853D13;
    local_r14 = (uint16_t)((*(uint8_t *)(result + 0x4C)) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_00853D13:
    local_rsi = (uint32_t)(((uint16_t)(local_rsi)) - ((uint32_t)((uint16_t)(local_r14))));
loc_00853D22:
    local_rdi = (uint16_t)((local_rdi) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    local_r15 = (uint16_t)((*(uint16_t *)(result + 0x48)) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    goto loc_00853CC1;
loc_00853D30:
    local_rsi = (uint32_t)(((uint16_t)(local_rdi)) - ((uint32_t)((uint16_t)(local_r15))));
    result = HvpReleaseCellPaged(*(uint64_t *)(local_rbp + 0x30), local_rbp - 48, local_rbp - 48, *(uint64_t *)(local_rbp + 0x48));
    if ((uint32_t)(local_rsi) == 0) goto loc_00853F25;
    if (sign_flag) goto loc_00853E9C;
loc_00853D71:
    goto loc_00853C12;
loc_00853D7B:
    *(uint32_t *)(local_rbp - 0x38) = 0xFFFFFFFFULL;
    *(uint32_t *)(local_rbp - 0x34) = 0;
    if (((*(uint8_t *)(*(uint64_t *)(local_rbp + 0x30) + 0x8C)) & (1)) == 0) goto loc_00853F40;
    result = HvpGetCellFlat(*(uint64_t *)(local_rbp + 0x30), (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp + 0x38) + local_rbx * 4 + 0x4)), local_rbp - 56, *(uint64_t *)(local_rbp + 0x48));
loc_00853DA8:
    local_rdi = (uint16_t)((*(uint16_t *)(*(uint64_t *)(local_rbp + 0x40))) >> (1));
loc_00853DDF:
    if ((uint16_t)(local_rdi) == 0) goto loc_00853E5B;
    if ((uint16_t)(*(uint16_t *)(result + 0x48)) == 0) goto loc_00853E5B;
    local_r12 = (*(uint64_t *)(*(uint64_t *)(local_rbp + 0x40) + 0x8)) + (2);
    local_r13 = (result + 76) + 1;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x40) + 0x8)))) == ((uint16_t)(*(uint8_t *)(result + 0x4C)))) goto loc_00853E40;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x40) + 0x8)))) < 97) goto loc_00853F1B;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x40) + 0x8)))) > 122) goto loc_00853F10;
    local_rsi = (uint16_t)((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x40) + 0x8))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_00853E1D:
    if (((uint32_t)(*(uint8_t *)(result + 0x4C))) < 97) goto loc_00853E31;
    local_r14 = (uint16_t)((*(uint8_t *)(result + 0x4C)) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_00853E31:
    local_rsi = (uint32_t)(((uint16_t)(local_rsi)) - ((uint32_t)((uint16_t)(local_r14))));
loc_00853E40:
    local_rdi = (uint16_t)((local_rdi) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    local_r15 = (uint16_t)((*(uint16_t *)(result + 0x48)) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    goto loc_00853DDF;
loc_00853E4E:
    local_r10 = (uint32_t)(((uint16_t)(local_rbp - 56)) - (32));
    goto loc_00853B8A;
loc_00853E5B:
    local_rsi = (uint32_t)(((uint16_t)(local_rdi)) - ((uint32_t)((uint16_t)(local_r15))));
    result = HvpReleaseCellPaged(*(uint64_t *)(local_rbp + 0x30), local_rbp - 56, local_rbp - 56, *(uint64_t *)(local_rbp + 0x48));
    if ((uint32_t)(local_rsi) == 0) goto loc_00853FE3;
    if (!sign_flag) goto loc_00853D71;
loc_00853E9C:
    goto loc_00853C12;
loc_00853EA6:
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rbp + 0x38)))) - ((uint16_t)((uint32_t)(0xFFFFFFFFULL))));
    *(uint32_t *)(*(uint64_t *)(local_rbp + 0x50)) = 0xFFFFFFFFULL;
    Arg2 = 0;
loc_00853EE0:
    if (0 >= 4) goto loc_00853F4D;
    if ((*(uint8_t *)(0 + *(uint64_t *)(local_rbp + 0x38) + (uint32_t)((uint32_t)(local_rsi)) * 8 * 1 + 0x8)) == 0) goto loc_00853F4A;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_00853EE0;
loc_00853EF2:
    result = RtlUpcaseUnicodeChar((uint16_t)(local_rsi), Arg2, local_rbp - 56, *(uint64_t *)(local_rbp + 0x48));
loc_00853EFD:
    goto loc_00853CFF;
loc_00853F07:
    goto loc_00853B93;
loc_00853F10:
    result = RtlUpcaseUnicodeChar((uint16_t)((uint16_t)(result)), Arg2, local_rbp - 56, *(uint64_t *)(local_rbp + 0x48));
loc_00853F1B:
    goto loc_00853E1D;
loc_00853F25:
    Arg2 = 0;
    *(uint32_t *)(*(uint64_t *)(local_rbp + 0x50)) = (uint32_t)((uint32_t)(*(uint32_t *)(4)));
    goto loc_00853C12;
loc_00853F36:
    result = HvpGetCellPaged((uint16_t)((uint16_t)(result)), Arg2, *(uint64_t *)(local_rbp + 0x50), *(uint64_t *)(local_rbp + 0x48));
    goto loc_00853C8A;
loc_00853F40:
    result = HvpGetCellPaged((uint16_t)((uint16_t)(result)), Arg2, *(uint64_t *)(local_rbp + 0x50), *(uint64_t *)(local_rbp + 0x48));
    goto loc_00853DA8;
loc_00853F4A:
loc_00853F4D:
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(local_rbp + 0x40))) >> (1));
    local_r14 = (uint32_t)((uint32_t)((uint16_t)((uint16_t)(result))));
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)((uint32_t)((uint16_t)((uint16_t)(result))))))) { local_r14 = (uint32_t)(result); }
loc_00853F73:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x40) + 0x8) + 0x0 * 2))) >= 97) goto loc_00853FCF;
loc_00853FA6:
    if (((uint32_t)(*(uint8_t *)(0 + (uint32_t)((uint32_t)((uint16_t)(result))) * 8 * 1 + *(uint64_t *)(local_rbp + 0x38) * 1 + 0x8))) >= 97) goto loc_00853FB9;
loc_00853FAD:
    local_rbx = (uint32_t)(((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x40) + 0x8) + 0x0 * 2))) - ((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)(0 + (uint32_t)((uint32_t)((uint16_t)(result))) * 8 * 1 + *(uint64_t *)(local_rbp + 0x38) * 1 + 0x8))))));
    if (condition_is_not_equal) goto loc_00853FF2;
    local_rdi = (uint32_t)((0) + 1);
    goto loc_00853F73;
loc_00853FB9:
    result = RtlUpcaseUnicodeChar((uint16_t)(*(uint8_t *)(0 + (uint32_t)((uint32_t)((uint16_t)(result))) * 8 * 1 + *(uint64_t *)(local_rbp + 0x38) * 1 + 0x8)), 0, *(uint64_t *)(local_rbp + 0x50), *(uint64_t *)(local_rbp + 0x48));
    goto loc_00853FAD;
loc_00853FCF:
    result = RtlUpcaseUnicodeChar((uint16_t)(*(uint8_t *)(0 + (uint32_t)((uint32_t)((uint16_t)(result))) * 8 * 1 + *(uint64_t *)(local_rbp + 0x38) * 1 + 0x8)), 0, *(uint64_t *)(local_rbp + 0x50), *(uint64_t *)(local_rbp + 0x48));
    goto loc_00853FA6;
loc_00853FE3:
    Arg2 = 0;
    *(uint32_t *)(local_r14) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp + 0x38) + (uint16_t)(result) * 4 + 0x4)));
    goto loc_00853C12;
loc_00853FF2:
    Arg2 = 1;
    if (condition_is_less_or_equal) { Arg2 = (uint32_t)((uint32_t)(0xFFFFFFFFULL)); }
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rbp + 0x38)))) - ((uint16_t)((uint32_t)(0x666CULL))));
    *(uint32_t *)(*(uint64_t *)(local_rbp + 0x50)) = 0xFFFFFFFFULL;
    local_rsi = 0;
loc_00854050:
    if (0 >= 4) goto loc_00854062;
    if ((*(uint8_t *)(0 + *(uint64_t *)(local_rbp + 0x38) + (uint32_t)(*(uint32_t *)(local_rbp - 0x3C)) * 8 * 1 + 0x8)) == 0) goto loc_00854067;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_00854050;
loc_00854062:
loc_00854067:
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(local_rbp + 0x40))) >> (1));
    Arg1 = 4;
    if (((uint32_t)(result)) < 4) { Arg1 = (uint32_t)(result); }
    *(uint32_t *)(local_rbp + 0x38) = (uint32_t)(Arg1);
loc_0085408F:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x40) + 0x8) + 0x0 * 2))) >= 97) goto loc_008540ED;
loc_008540C1:
    if (((uint32_t)(*(uint8_t *)(0 + (uint32_t)(*(uint32_t *)(local_rbp - 0x3C)) * 8 * 1 + *(uint64_t *)(local_rbp + 0x38) * 1 + 0x8))) >= 97) goto loc_008540D7;
loc_008540C8:
    local_rbx = (uint32_t)(((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x40) + 0x8) + 0x0 * 2))) - ((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)(0 + (uint32_t)(*(uint32_t *)(local_rbp - 0x3C)) * 8 * 1 + *(uint64_t *)(local_rbp + 0x38) * 1 + 0x8))))));
    if (condition_is_not_equal) goto loc_00854101;
    local_rdi = (uint32_t)((0) + 1);
    goto loc_0085408F;
loc_008540D7:
    result = RtlUpcaseUnicodeChar((uint16_t)(*(uint8_t *)(0 + (uint32_t)(*(uint32_t *)(local_rbp - 0x3C)) * 8 * 1 + *(uint64_t *)(local_rbp + 0x38) * 1 + 0x8)), 0, (uint32_t)(0xFDFFULL), *(uint64_t *)(local_rbp + 0x48));
    goto loc_008540C8;
loc_008540ED:
    result = RtlUpcaseUnicodeChar((uint16_t)(*(uint8_t *)(0 + (uint32_t)(*(uint32_t *)(local_rbp - 0x3C)) * 8 * 1 + *(uint64_t *)(local_rbp + 0x38) * 1 + 0x8)), 0, (uint32_t)(0xFDFFULL), *(uint64_t *)(local_rbp + 0x48));
    goto loc_008540C1;
loc_00854101:
    Arg1 = 1;
    if (condition_is_less_or_equal) { Arg1 = (uint32_t)((uint32_t)(0xFFFFFFFFULL)); }
    Arg1 = (uint32_t)(-(Arg1));
    *(uint32_t *)(*(uint64_t *)(local_rbp + 0x58)) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x3C)));
    result = (uint32_t)((*(uint64_t *)(local_rbp + 0x58)) & (0xC0000034ULL));
    local_rsp = (local_rsp) + (112);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00853ABC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
