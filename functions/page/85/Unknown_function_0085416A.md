# sub_0085416A

- RVA: `0x0085416A`–`0x00854C50` (길이 `2,790` bytes)
- VA: `0x000000014085416A`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069F20`
- 디코드: `711`개 명령, `2,790/2,790` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **43**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00854192` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085426E` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x008542AA` → [CmpDoCompareKeyName](CmpDoCompareKeyName_function_00854E80.md) (function, `0x00854E80`)
- `0x0085430C` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x008543CD` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x008543F1` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085442A` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x008544F8` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x0085452B` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00854540` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00854570` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00854587` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00854591` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x0085466D` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00854685` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x008546E6` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x008546F0` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00854707` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x0085472E` → [CmpCompareTwoCompressedNames](../84/CmpCompareTwoCompressedNames_function_00847610.md) (function, `0x00847610`)
- `0x0085474A` → [CmpCompareTwoCompressedNames](../84/CmpCompareTwoCompressedNames_function_00847610.md) (function, `0x00847610`)
- `0x0085476A` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085477C` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x008547B1` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x008547E6` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00854803` → [CmpCompareTwoCompressedNames](../84/CmpCompareTwoCompressedNames_function_00847610.md) (function, `0x00847610`)
- `0x0085481E` → [CmpCompareTwoCompressedNames](../84/CmpCompareTwoCompressedNames_function_00847610.md) (function, `0x00847610`)
- `0x0085483A` → [CmpCompareTwoCompressedNames](../84/CmpCompareTwoCompressedNames_function_00847610.md) (function, `0x00847610`)
- `0x00854849` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085485A` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0085486B` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x008548A1` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x008548D6` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00854908` → [RtlCompareUnicodeStrings](../97/RtlCompareUnicodeStrings_function_009727E0.md) (function, `0x009727E0`)
- `0x00854A15` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00854A2A` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00854BB3` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00854BC8` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00854BDD` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00854BEF` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00854BFF` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00854C0F` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00854C1F` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00854C2F` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **30**
  - `0x00854245` → [sub_00853ABC + 0x4EA](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x00854290` → [sub_00853ABC + 0x545](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x008542D0` → [sub_00853ABC + 0x66D](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x008542DB` → [sub_00853ABC + 0x605](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x008543E9` → [sub_00853ABC + 0x545](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x0085451B` → [sub_00853ABC + 0x654](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x00854523` → [sub_00853ABC + 0x4F1](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x00854555` → [sub_00853ABC + 0x60C](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x0085456B` → [sub_00853ABC + 0x545](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x00854582` → [sub_00853ABC + 0x66D](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x008545C0` → [sub_00853ABC + 0x654](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x008545E6` → [sub_00853ABC + 0x289](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x00854603` → [sub_00853ABC + 0x3B4](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x00854616` → [sub_00853ABC + 0x66D](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x00854639` → [sub_00853ABC + 0x10F](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x00854668` → [sub_00853ABC + 0x140](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x00854672` → [sub_00853ABC + 0x2A7](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x00854680` → [sub_00853ABC + 0xB9](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x0085468A` → [sub_00853ABC + 0x3D2](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x0085469A` → [sub_00853ABC + 0x66D](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x008546E1` → [sub_00853ABC + 0x8B](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x00854702` → [sub_00853ABC + 0x4D7](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x00854719` → [sub_00853ABC + 0x5F2](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x00854735` → [sub_00853ABC + 0x289](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x00854751` → [sub_00853ABC + 0x3B4](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x00854759` → [sub_00853ABC + 0x4A4](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x00854761` → [sub_00853ABC + 0x5C1](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x00854773` → [sub_00853ABC + 0x257](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x00854785` → [sub_00853ABC + 0x375](Unknown_function_00853ABC.md) (`tail-transfer`)
  - `0x00854C41` → [sub_00853ABC + 0x545](Unknown_function_00853ABC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0085416A  41 8B 54 84 04                  mov edx, dword ptr [r12 + rax*4 + 4]
0085416F  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00854173  45 33 F6                        xor r14d, r14d
00854176  C7 45 D0 FF FF FF FF            mov dword ptr [rbp - 0x30], 0xffffffff
0085417D  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
00854185  49 8B CD                        mov rcx, r13
00854188  44 89 75 D4                     mov dword ptr [rbp - 0x2c], r14d
0085418C  0F 84 FF 03 00 00               je 0x140854591
00854192  E8 C9 0A 00 00                  call 0x140854c60
00854197  48 8B C8                        mov rcx, rax
0085419A  48 85 C0                        test rax, rax
0085419D  0F 84 22 04 00 00               je 0x1408545c5
008541A3  F6 40 02 20                     test byte ptr [rax + 2], 0x20
008541A7  4C 8D 60 4C                     lea r12, [rax + 0x4c]
008541AB  4C 8B 55 48                     mov r10, qword ptr [rbp + 0x48]
008541AF  0F 84 2D 07 00 00               je 0x1408548e2
008541B5  4D 85 D2                        test r10, r10
008541B8  0F 85 6C 06 00 00               jne 0x14085482a
008541BE  48 8B 7D 40                     mov rdi, qword ptr [rbp + 0x40]
008541C2  44 0F B7 70 48                  movzx r14d, word ptr [rax + 0x48]
008541C7  B8 FF FF 00 00                  mov eax, 0xffff
008541CC  4D 8B 7F 08                     mov r15, qword ptr [r15 + 8]
008541D0  0F B7 3F                        movzx edi, word ptr [rdi]
008541D3  66 D1 EF                        shr di, 1
008541D6  66 85 FF                        test di, di
008541D9  74 6F                           je 0x14085424a
008541DB  66 45 85 F6                     test r14w, r14w
008541DF  74 69                           je 0x14085424a
008541E1  41 0F B7 1F                     movzx ebx, word ptr [r15]
008541E5  49 83 C7 02                     add r15, 2
008541E9  41 0F B6 34 24                  movzx esi, byte ptr [r12]
008541EE  49 FF C4                        inc r12
008541F1  66 3B DE                        cmp bx, si
008541F4  74 40                           je 0x140854236
008541F6  66 83 FB 61                     cmp bx, 0x61
008541FA  0F 82 48 03 00 00               jb 0x140854548
00854200  66 83 FB 7A                     cmp bx, 0x7a
00854204  0F 87 33 03 00 00               ja 0x14085453d
0085420A  B8 E0 FF 00 00                  mov eax, 0xffe0
0085420F  66 03 D8                        add bx, ax
00854212  83 FE 61                        cmp esi, 0x61
00854215  72 0C                           jb 0x140854223
00854217  83 FE 7A                        cmp esi, 0x7a
0085421A  0F 87 48 06 00 00               ja 0x140854868
00854220  66 03 F0                        add si, ax
00854223  0F B7 C6                        movzx eax, si
00854226  0F B7 DB                        movzx ebx, bx
00854229  2B D8                           sub ebx, eax
0085422B  0F 85 A1 04 00 00               jne 0x1408546d2
00854231  B8 FF FF 00 00                  mov eax, 0xffff
00854236  66 03 F8                        add di, ax
00854239  66 44 03 F0                     add r14w, ax
0085423D  EB 97                           jmp 0x1408541d6
0085423F  0F B7 D9                        movzx ebx, cx
00854242  83 EB 20                        sub ebx, 0x20
00854245  E9 5C FD FF FF                  jmp 0x140853fa6
0085424A  8B 75 C0                        mov esi, dword ptr [rbp - 0x40]
0085424D  41 0F B7 C6                     movzx eax, r14w
00854251  0F B7 DF                        movzx ebx, di
00854254  2B D8                           sub ebx, eax
00854256  45 33 F6                        xor r14d, r14d
00854259  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
00854261  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00854265  49 8B CD                        mov rcx, r13
00854268  0F 85 99 04 00 00               jne 0x140854707
0085426E  E8 CD 1C 00 00                  call 0x140855f40
00854273  85 DB                           test ebx, ebx
00854275  0F 85 5F 01 00 00               jne 0x1408543da
0085427B  4C 8B 65 38                     mov r12, qword ptr [rbp + 0x38]
0085427F  41 8B D6                        mov edx, r14d
00854282  4C 8B 45 50                     mov r8, qword ptr [rbp + 0x50]
00854286  8B C6                           mov eax, esi
00854288  41 8B 4C 84 04                  mov ecx, dword ptr [r12 + rax*4 + 4]
0085428D  41 89 08                        mov dword ptr [r8], ecx
00854290  E9 6C FD FF FF                  jmp 0x140854001
00854295  47 8B 4C BC 04                  mov r9d, dword ptr [r12 + r15*4 + 4]
0085429A  4B 8D 1C BC                     lea rbx, [r12 + r15*4]
0085429E  4C 8B 45 48                     mov r8, qword ptr [rbp + 0x48]
008542A2  48 8B 55 40                     mov rdx, qword ptr [rbp + 0x40]
008542A6  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
008542AA  E8 D1 0B 00 00                  call 0x140854e80
008542AF  8B F0                           mov esi, eax
008542B1  83 F8 02                        cmp eax, 2
008542B4  0F 85 F6 02 00 00               jne 0x1408545b0
008542BA  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
008542BE  41 C7 06 FF FF FF FF            mov dword ptr [r14], 0xffffffff
008542C5  C7 00 00 00 00 80               mov dword ptr [rax], 0x80000000
008542CB  B8 9A 00 00 C0                  mov eax, 0xc000009a
008542D0  E9 54 FE FF FF                  jmp 0x140854129
008542D5  0F B7 D9                        movzx ebx, cx
008542D8  83 EB 20                        sub ebx, 0x20
008542DB  E9 E1 FD FF FF                  jmp 0x1408540c1
008542E0  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
008542E4  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
008542E8  4C 8D 45 D0                     lea r8, [rbp - 0x30]
008542EC  8B C6                           mov eax, esi
008542EE  33 F6                           xor esi, esi
008542F0  C7 45 D0 FF FF FF FF            mov dword ptr [rbp - 0x30], 0xffffffff
008542F7  89 75 D4                        mov dword ptr [rbp - 0x2c], esi
008542FA  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00854301  41 8B 54 C4 04                  mov edx, dword ptr [r12 + rax*8 + 4]
00854306  0F 84 64 02 00 00               je 0x140854570
0085430C  E8 4F 09 00 00                  call 0x140854c60
00854311  48 8B C8                        mov rcx, rax
00854314  48 85 C0                        test rax, rax
00854317  74 A1                           je 0x1408542ba
00854319  F6 40 02 20                     test byte ptr [rax + 2], 0x20
0085431D  4C 8D 60 4C                     lea r12, [rax + 0x4c]
00854321  0F 84 51 05 00 00               je 0x140854878
00854327  48 85 DB                        test rbx, rbx
0085432A  0F 85 C4 04 00 00               jne 0x1408547f4
00854330  48 8B 75 40                     mov rsi, qword ptr [rbp + 0x40]
00854334  44 0F B7 70 48                  movzx r14d, word ptr [rax + 0x48]
00854339  B8 FF FF 00 00                  mov eax, 0xffff
0085433E  0F B7 3E                        movzx edi, word ptr [rsi]
00854341  4C 8B 7E 08                     mov r15, qword ptr [rsi + 8]
00854345  66 D1 EF                        shr di, 1
00854348  66 85 FF                        test di, di
0085434B  74 60                           je 0x1408543ad
0085434D  66 45 85 F6                     test r14w, r14w
00854351  74 5A                           je 0x1408543ad
00854353  41 0F B7 1F                     movzx ebx, word ptr [r15]
00854357  49 83 C7 02                     add r15, 2
0085435B  41 0F B6 34 24                  movzx esi, byte ptr [r12]
00854360  49 FF C4                        inc r12
00854363  66 3B DE                        cmp bx, si
00854366  74 3C                           je 0x1408543a4
00854368  66 83 FB 61                     cmp bx, 0x61
0085436C  0F 82 87 00 00 00               jb 0x1408543f9
00854372  66 83 FB 7A                     cmp bx, 0x7a
00854376  77 76                           ja 0x1408543ee
00854378  B8 E0 FF 00 00                  mov eax, 0xffe0
0085437D  66 03 D8                        add bx, ax
00854380  83 FE 61                        cmp esi, 0x61
00854383  72 0C                           jb 0x140854391
00854385  83 FE 7A                        cmp esi, 0x7a
00854388  0F 87 B8 04 00 00               ja 0x140854846
0085438E  66 03 F0                        add si, ax
00854391  0F B7 C6                        movzx eax, si
00854394  0F B7 DB                        movzx ebx, bx
00854397  2B D8                           sub ebx, eax
00854399  0F 85 0B 03 00 00               jne 0x1408546aa
0085439F  B8 FF FF 00 00                  mov eax, 0xffff
008543A4  66 03 F8                        add di, ax
008543A7  66 44 03 F0                     add r14w, ax
008543AB  EB 9B                           jmp 0x140854348
008543AD  41 0F B7 C6                     movzx eax, r14w
008543B1  0F B7 DF                        movzx ebx, di
008543B4  2B D8                           sub ebx, eax
008543B6  33 F6                           xor esi, esi
008543B8  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
008543BC  48 8D 55 D0                     lea rdx, [rbp - 0x30]
008543C0  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
008543C7  0F 85 19 03 00 00               jne 0x1408546e6
008543CD  E8 6E 1B 00 00                  call 0x140855f40
008543D2  85 DB                           test ebx, ebx
008543D4  0F 84 80 01 00 00               je 0x14085455a
008543DA  4C 8B 65 38                     mov r12, qword ptr [rbp + 0x38]
008543DE  0F 88 58 08 00 00               js 0x140854c3c
008543E4  BA 01 00 00 00                  mov edx, 1
008543E9  E9 13 FC FF FF                  jmp 0x140854001
008543EE  0F B7 CB                        movzx ecx, bx
008543F1  E8 FA AC 00 00                  call 0x14085f0f0
008543F6  0F B7 D8                        movzx ebx, ax
008543F9  B8 E0 FF 00 00                  mov eax, 0xffe0
008543FE  EB 80                           jmp 0x140854380
00854400  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
00854404  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00854408  4C 8D 45 38                     lea r8, [rbp + 0x38]
0085440C  43 8B 54 FC 04                  mov edx, dword ptr [r12 + r15*8 + 4]
00854411  33 F6                           xor esi, esi
00854413  C7 45 38 FF FF FF FF            mov dword ptr [rbp + 0x38], 0xffffffff
0085441A  89 75 3C                        mov dword ptr [rbp + 0x3c], esi
0085441D  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00854424  0F 84 5D 01 00 00               je 0x140854587
0085442A  E8 31 08 00 00                  call 0x140854c60
0085442F  48 8B C8                        mov rcx, rax
00854432  48 85 C0                        test rax, rax
00854435  0F 84 7F FE FF FF               je 0x1408542ba
0085443B  F6 40 02 20                     test byte ptr [rax + 2], 0x20
0085443F  4C 8D 60 4C                     lea r12, [rax + 0x4c]
00854443  0F 84 64 04 00 00               je 0x1408548ad
00854449  48 85 DB                        test rbx, rbx
0085444C  0F 85 BD 03 00 00               jne 0x14085480f
00854452  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
00854456  0F B7 71 48                     movzx esi, word ptr [rcx + 0x48]
0085445A  0F B7 38                        movzx edi, word ptr [rax]
0085445D  4C 8B 78 08                     mov r15, qword ptr [rax + 8]
00854461  B8 FF FF 00 00                  mov eax, 0xffff
00854466  66 D1 EF                        shr di, 1
00854469  66 85 FF                        test di, di
0085446C  74 67                           je 0x1408544d5
0085446E  66 85 F6                        test si, si
00854471  74 62                           je 0x1408544d5
00854473  41 0F B7 1F                     movzx ebx, word ptr [r15]
00854477  49 83 C7 02                     add r15, 2
0085447B  45 0F B6 34 24                  movzx r14d, byte ptr [r12]
00854480  49 FF C4                        inc r12
00854483  66 41 3B DE                     cmp bx, r14w
00854487  74 44                           je 0x1408544cd
00854489  66 83 FB 61                     cmp bx, 0x61
0085448D  0F 82 A0 00 00 00               jb 0x140854533
00854493  66 83 FB 7A                     cmp bx, 0x7a
00854497  0F 87 8B 00 00 00               ja 0x140854528
0085449D  B8 E0 FF 00 00                  mov eax, 0xffe0
008544A2  66 03 D8                        add bx, ax
008544A5  41 83 FE 61                     cmp r14d, 0x61
008544A9  72 0E                           jb 0x1408544b9
008544AB  41 83 FE 7A                     cmp r14d, 0x7a
008544AF  0F 87 A1 03 00 00               ja 0x140854856
008544B5  66 44 03 F0                     add r14w, ax
008544B9  41 0F B7 C6                     movzx eax, r14w
008544BD  0F B7 DB                        movzx ebx, bx
008544C0  2B D8                           sub ebx, eax
008544C2  0F 85 F4 01 00 00               jne 0x1408546bc
008544C8  B8 FF FF 00 00                  mov eax, 0xffff
008544CD  66 03 F8                        add di, ax
008544D0  66 03 F0                        add si, ax
008544D3  EB 94                           jmp 0x140854469
008544D5  44 8B 7D C4                     mov r15d, dword ptr [rbp - 0x3c]
008544D9  0F B7 C6                        movzx eax, si
008544DC  0F B7 DF                        movzx ebx, di
008544DF  2B D8                           sub ebx, eax
008544E1  33 F6                           xor esi, esi
008544E3  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
008544E7  48 8D 55 38                     lea rdx, [rbp + 0x38]
008544EB  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
008544F2  0F 85 F8 01 00 00               jne 0x1408546f0
008544F8  E8 43 1A 00 00                  call 0x140855f40
008544FD  85 DB                           test ebx, ebx
008544FF  74 0D                           je 0x14085450e
00854501  0F 88 3F 07 00 00               js 0x140854c46
00854507  BE 01 00 00 00                  mov esi, 1
0085450C  EB 0B                           jmp 0x140854519
0085450E  4C 8B 45 50                     mov r8, qword ptr [rbp + 0x50]
00854512  41 8B 45 04                     mov eax, dword ptr [r13 + 4]
00854516  41 89 00                        mov dword ptr [r8], eax
00854519  8B CE                           mov ecx, esi
0085451B  E9 F0 FB FF FF                  jmp 0x140854110
00854520  8D 46 E0                        lea eax, [rsi - 0x20]
00854523  E9 85 FA FF FF                  jmp 0x140853fad
00854528  0F B7 CB                        movzx ecx, bx
0085452B  E8 C0 AB 00 00                  call 0x14085f0f0
00854530  0F B7 D8                        movzx ebx, ax
00854533  B8 E0 FF 00 00                  mov eax, 0xffe0
00854538  E9 68 FF FF FF                  jmp 0x1408544a5
0085453D  0F B7 CB                        movzx ecx, bx
00854540  E8 AB AB 00 00                  call 0x14085f0f0
00854545  0F B7 D8                        movzx ebx, ax
00854548  B8 E0 FF 00 00                  mov eax, 0xffe0
0085454D  E9 C0 FC FF FF                  jmp 0x140854212
00854552  8D 46 E0                        lea eax, [rsi - 0x20]
00854555  E9 6E FB FF FF                  jmp 0x1408540c8
0085455A  4C 8B 45 50                     mov r8, qword ptr [rbp + 0x50]
0085455E  8B D6                           mov edx, esi
00854560  41 8B 45 04                     mov eax, dword ptr [r13 + 4]
00854564  4C 8B 65 38                     mov r12, qword ptr [rbp + 0x38]
00854568  41 89 00                        mov dword ptr [r8], eax
0085456B  E9 91 FA FF FF                  jmp 0x140854001
00854570  E8 3B 07 00 00                  call 0x140854cb0
00854575  E9 97 FD FF FF                  jmp 0x140854311
0085457A  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0085457E  89 18                           mov dword ptr [rax], ebx
00854580  33 C0                           xor eax, eax
00854582  E9 A2 FB FF FF                  jmp 0x140854129
00854587  E8 24 07 00 00                  call 0x140854cb0
0085458C  E9 9E FE FF FF                  jmp 0x14085442f
00854591  E8 1A 07 00 00                  call 0x140854cb0
00854596  E9 FC FB FF FF                  jmp 0x140854197
0085459B  8B 75 C0                        mov esi, dword ptr [rbp - 0x40]
0085459E  4C 8B 75 50                     mov r14, qword ptr [rbp + 0x50]
008545A2  E9 3D FD FF FF                  jmp 0x1408542e4
008545A7  4C 8B 75 50                     mov r14, qword ptr [rbp + 0x50]
008545AB  E9 54 FE FF FF                  jmp 0x140854404
008545B0  85 C0                           test eax, eax
008545B2  0F 85 61 FF FF FF               jne 0x140854519
008545B8  8B 4B 04                        mov ecx, dword ptr [rbx + 4]
008545BB  41 89 0E                        mov dword ptr [r14], ecx
008545BE  8B CE                           mov ecx, esi
008545C0  E9 4B FB FF FF                  jmp 0x140854110
008545C5  4C 8B 75 50                     mov r14, qword ptr [rbp + 0x50]
008545C9  E9 EC FC FF FF                  jmp 0x1408542ba
008545CE  41 0F B7 C7                     movzx eax, r15w
008545D2  41 0F B7 F6                     movzx esi, r14w
008545D6  2B F0                           sub esi, eax
008545D8  F7 DE                           neg esi
008545DA  4C 8B 65 38                     mov r12, qword ptr [rbp + 0x38]
008545DE  4C 8B 75 D8                     mov r14, qword ptr [rbp - 0x28]
008545E2  4C 8B 7D 40                     mov r15, qword ptr [rbp + 0x40]
008545E6  E9 5A F7 FF FF                  jmp 0x140853d45
008545EB  41 0F B7 C7                     movzx eax, r15w
008545EF  41 0F B7 F6                     movzx esi, r14w
008545F3  2B F0                           sub esi, eax
008545F5  F7 DE                           neg esi
008545F7  4C 8B 65 38                     mov r12, qword ptr [rbp + 0x38]
008545FB  4C 8B 7D 40                     mov r15, qword ptr [rbp + 0x40]
008545FF  4C 8B 75 50                     mov r14, qword ptr [rbp + 0x50]
00854603  E9 68 F8 FF FF                  jmp 0x140853e70
00854608  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0085460C  8B 55 C0                        mov edx, dword ptr [rbp - 0x40]
0085460F  89 10                           mov dword ptr [rax], edx
00854611  B8 34 00 00 C0                  mov eax, 0xc0000034
00854616  E9 0E FB FF FF                  jmp 0x140854129
0085461B  41 0F B7 00                     movzx eax, word ptr [r8]
0085461F  41 8B C9                        mov ecx, r9d
00854622  C1 E9 04                        shr ecx, 4
00854625  41 8B D1                        mov edx, r9d
00854628  03 C8                           add ecx, eax
0085462A  83 E2 0F                        and edx, 0xf
0085462D  41 0F B7 0C 48                  movzx ecx, word ptr [r8 + rcx*2]
00854632  03 CA                           add ecx, edx
00854634  66 45 03 0C 48                  add r9w, word ptr [r8 + rcx*2]
00854639  E9 8D F5 FF FF                  jmp 0x140853bcb
0085463E  41 0F B7 D0                     movzx edx, r8w
00854642  41 0F B7 C0                     movzx eax, r8w
00854646  48 C1 E8 08                     shr rax, 8
0085464A  41 0F B7 0C 42                  movzx ecx, word ptr [r10 + rax*2]
0085464F  8B C2                           mov eax, edx
00854651  C1 E8 04                        shr eax, 4
00854654  83 E2 0F                        and edx, 0xf
00854657  83 E0 0F                        and eax, 0xf
0085465A  03 C8                           add ecx, eax
0085465C  41 0F B7 0C 4A                  movzx ecx, word ptr [r10 + rcx*2]
00854661  03 CA                           add ecx, edx
00854663  66 45 03 04 4A                  add r8w, word ptr [r10 + rcx*2]
00854668  E9 8F F5 FF FF                  jmp 0x140853bfc
0085466D  E8 AE 85 00 00                  call 0x14085cc20
00854672  E9 EC F6 FF FF                  jmp 0x140853d63
00854677  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
0085467B  44 0F B6 04 08                  movzx r8d, byte ptr [rax + rcx]
00854680  E9 F0 F4 FF FF                  jmp 0x140853b75
00854685  E8 96 85 00 00                  call 0x14085cc20
0085468A  E9 FF F7 FF FF                  jmp 0x140853e8e
0085468F  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00854693  8B 55 C0                        mov edx, dword ptr [rbp - 0x40]
00854696  89 10                           mov dword ptr [rax], edx
00854698  33 C0                           xor eax, eax
0085469A  E9 8A FA FF FF                  jmp 0x140854129
0085469F  41 0F B7 C6                     movzx eax, r14w
008546A3  0F B7 DE                        movzx ebx, si
008546A6  2B D8                           sub ebx, eax
008546A8  F7 DB                           neg ebx
008546AA  33 F6                           xor esi, esi
008546AC  E9 07 FD FF FF                  jmp 0x1408543b8
008546B1  41 0F B7 C6                     movzx eax, r14w
008546B5  0F B7 DE                        movzx ebx, si
008546B8  2B D8                           sub ebx, eax
008546BA  F7 DB                           neg ebx
008546BC  44 8B 7D C4                     mov r15d, dword ptr [rbp - 0x3c]
008546C0  33 F6                           xor esi, esi
008546C2  E9 1C FE FF FF                  jmp 0x1408544e3
008546C7  41 0F B7 C6                     movzx eax, r14w
008546CB  0F B7 DE                        movzx ebx, si
008546CE  2B D8                           sub ebx, eax
008546D0  F7 DB                           neg ebx
008546D2  8B 75 C0                        mov esi, dword ptr [rbp - 0x40]
008546D5  45 33 F6                        xor r14d, r14d
008546D8  E9 7C FB FF FF                  jmp 0x140854259
008546DD  41 0F B7 01                     movzx eax, word ptr [r9]
008546E1  E9 61 F4 FF FF                  jmp 0x140853b47
008546E6  E8 35 85 00 00                  call 0x14085cc20
008546EB  E9 E2 FC FF FF                  jmp 0x1408543d2
008546F0  E8 2B 85 00 00                  call 0x14085cc20
008546F5  E9 03 FE FF FF                  jmp 0x1408544fd
008546FA  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
008546FE  0F B6 0C 10                     movzx ecx, byte ptr [rax + rdx]
00854702  E9 8C F8 FF FF                  jmp 0x140853f93
00854707  E8 14 85 00 00                  call 0x14085cc20
0085470C  E9 62 FB FF FF                  jmp 0x140854273
00854711  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00854715  0F B6 0C 10                     movzx ecx, byte ptr [rax + rdx]
00854719  E9 90 F9 FF FF                  jmp 0x1408540ae
0085471E  44 0F B7 49 48                  movzx r9d, word ptr [rcx + 0x48]
00854723  4D 8B C5                        mov r8, r13
00854726  49 8B 4A 08                     mov rcx, qword ptr [r10 + 8]
0085472A  41 0F B7 12                     movzx edx, word ptr [r10]
0085472E  E8 DD 2E FF FF                  call 0x140847610
00854733  8B F0                           mov esi, eax
00854735  E9 0B F6 FF FF                  jmp 0x140853d45
0085473A  44 0F B7 49 48                  movzx r9d, word ptr [rcx + 0x48]
0085473F  4D 8B C5                        mov r8, r13
00854742  49 8B 4A 08                     mov rcx, qword ptr [r10 + 8]
00854746  41 0F B7 12                     movzx edx, word ptr [r10]
0085474A  E8 C1 2E FF FF                  call 0x140847610
0085474F  8B F0                           mov esi, eax
00854751  E9 1A F7 FF FF                  jmp 0x140853e70
00854756  0F B7 03                        movzx eax, word ptr [rbx]
00854759  E9 02 F8 FF FF                  jmp 0x140853f60
0085475E  0F B7 03                        movzx eax, word ptr [rbx]
00854761  E9 17 F9 FF FF                  jmp 0x14085407d
00854766  41 0F B7 CE                     movzx ecx, r14w
0085476A  E8 81 A9 00 00                  call 0x14085f0f0
0085476F  44 0F B7 F0                     movzx r14d, ax
00854773  E9 9B F5 FF FF                  jmp 0x140853d13
00854778  41 0F B7 CE                     movzx ecx, r14w
0085477C  E8 6F A9 00 00                  call 0x14085f0f0
00854781  44 0F B7 F0                     movzx r14d, ax
00854785  E9 A7 F6 FF FF                  jmp 0x140853e31
0085478A  44 0F B7 71 48                  movzx r14d, word ptr [rcx + 0x48]
0085478F  4D 85 D2                        test r10, r10
00854792  0F 85 7D 01 00 00               jne 0x140854915
00854798  41 0F B7 17                     movzx edx, word ptr [r15]
0085479C  45 8B CE                        mov r9d, r14d
0085479F  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
008547A3  4D 8B C5                        mov r8, r13
008547A6  49 D1 E9                        shr r9, 1
008547A9  48 D1 EA                        shr rdx, 1
008547AC  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
008547B1  E8 2A E0 11 00                  call 0x1409727e0
008547B6  4C 8B 75 D8                     mov r14, qword ptr [rbp - 0x28]
008547BA  E9 74 FF FF FF                  jmp 0x140854733
008547BF  44 0F B7 71 48                  movzx r14d, word ptr [rcx + 0x48]
008547C4  4D 85 D2                        test r10, r10
008547C7  0F 85 C8 01 00 00               jne 0x140854995
008547CD  41 0F B7 17                     movzx edx, word ptr [r15]
008547D1  45 8B CE                        mov r9d, r14d
008547D4  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
008547D8  4D 8B C5                        mov r8, r13
008547DB  49 D1 E9                        shr r9, 1
008547DE  48 D1 EA                        shr rdx, 1
008547E1  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
008547E6  E8 F5 DF 11 00                  call 0x1409727e0
008547EB  4C 8B 75 50                     mov r14, qword ptr [rbp + 0x50]
008547EF  E9 5B FF FF FF                  jmp 0x14085474f
008547F4  44 0F B7 49 48                  movzx r9d, word ptr [rcx + 0x48]
008547F9  4D 8B C4                        mov r8, r12
008547FC  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00854800  0F B7 13                        movzx edx, word ptr [rbx]
00854803  E8 08 2E FF FF                  call 0x140847610
00854808  8B D8                           mov ebx, eax
0085480A  E9 A9 FB FF FF                  jmp 0x1408543b8
0085480F  44 0F B7 49 48                  movzx r9d, word ptr [rcx + 0x48]
00854814  4D 8B C4                        mov r8, r12
00854817  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0085481B  0F B7 13                        movzx edx, word ptr [rbx]
0085481E  E8 ED 2D FF FF                  call 0x140847610
00854823  8B D8                           mov ebx, eax
00854825  E9 B9 FC FF FF                  jmp 0x1408544e3
0085482A  44 0F B7 49 48                  movzx r9d, word ptr [rcx + 0x48]
0085482F  4D 8B C4                        mov r8, r12
00854832  49 8B 4A 08                     mov rcx, qword ptr [r10 + 8]
00854836  41 0F B7 12                     movzx edx, word ptr [r10]
0085483A  E8 D1 2D FF FF                  call 0x140847610
0085483F  8B D8                           mov ebx, eax
00854841  E9 13 FA FF FF                  jmp 0x140854259
00854846  0F B7 CE                        movzx ecx, si
00854849  E8 A2 A8 00 00                  call 0x14085f0f0
0085484E  0F B7 F0                        movzx esi, ax
00854851  E9 3B FB FF FF                  jmp 0x140854391
00854856  41 0F B7 CE                     movzx ecx, r14w
0085485A  E8 91 A8 00 00                  call 0x14085f0f0
0085485F  44 0F B7 F0                     movzx r14d, ax
00854863  E9 51 FC FF FF                  jmp 0x1408544b9
00854868  0F B7 CE                        movzx ecx, si
0085486B  E8 80 A8 00 00                  call 0x14085f0f0
00854870  0F B7 F0                        movzx esi, ax
00854873  E9 AB F9 FF FF                  jmp 0x140854223
00854878  0F B7 71 48                     movzx esi, word ptr [rcx + 0x48]
0085487C  48 85 DB                        test rbx, rbx
0085487F  0F 85 B4 01 00 00               jne 0x140854a39
00854885  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
00854889  44 8B CE                        mov r9d, esi
0085488C  49 D1 E9                        shr r9, 1
0085488F  4D 8B C4                        mov r8, r12
00854892  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00854897  0F B7 10                        movzx edx, word ptr [rax]
0085489A  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0085489E  48 D1 EA                        shr rdx, 1
008548A1  E8 3A DF 11 00                  call 0x1409727e0
008548A6  33 F6                           xor esi, esi
008548A8  E9 5B FF FF FF                  jmp 0x140854808
008548AD  0F B7 71 48                     movzx esi, word ptr [rcx + 0x48]
008548B1  48 85 DB                        test rbx, rbx
008548B4  0F 85 00 02 00 00               jne 0x140854aba
008548BA  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
008548BE  44 8B CE                        mov r9d, esi
008548C1  49 D1 E9                        shr r9, 1
008548C4  4D 8B C4                        mov r8, r12
008548C7  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
008548CC  0F B7 10                        movzx edx, word ptr [rax]
008548CF  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
008548D3  48 D1 EA                        shr rdx, 1
008548D6  E8 05 DF 11 00                  call 0x1409727e0
008548DB  33 F6                           xor esi, esi
008548DD  E9 41 FF FF FF                  jmp 0x140854823
008548E2  0F B7 71 48                     movzx esi, word ptr [rcx + 0x48]
008548E6  4D 85 D2                        test r10, r10
008548E9  0F 85 4C 02 00 00               jne 0x140854b3b
008548EF  41 0F B7 17                     movzx edx, word ptr [r15]
008548F3  44 8B CE                        mov r9d, esi
008548F6  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
008548FA  4D 8B C4                        mov r8, r12
008548FD  49 D1 E9                        shr r9, 1
00854900  48 D1 EA                        shr rdx, 1
00854903  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
00854908  E8 D3 DE 11 00                  call 0x1409727e0
0085490D  8B 75 C0                        mov esi, dword ptr [rbp - 0x40]
00854910  E9 2A FF FF FF                  jmp 0x14085483f
00854915  4D 8B 62 08                     mov r12, qword ptr [r10 + 8]
00854919  45 0F B7 3A                     movzx r15d, word ptr [r10]
0085491D  66 41 D1 EE                     shr r14w, 1
00854921  66 45 85 F6                     test r14w, r14w
00854925  0F 84 A3 FC FF FF               je 0x1408545ce
0085492B  66 45 85 FF                     test r15w, r15w
0085492F  0F 84 99 FC FF FF               je 0x1408545ce
00854935  41 0F B7 7D 00                  movzx edi, word ptr [r13]
0085493A  49 83 C5 02                     add r13, 2
0085493E  41 0F B6 34 24                  movzx esi, byte ptr [r12]
00854943  49 FF C4                        inc r12
00854946  66 3B FE                        cmp di, si
00854949  74 3B                           je 0x140854986
0085494B  66 83 FF 61                     cmp di, 0x61
0085494F  0F 82 C8 00 00 00               jb 0x140854a1d
00854955  66 83 FF 7A                     cmp di, 0x7a
00854959  0F 87 B3 00 00 00               ja 0x140854a12
0085495F  B8 E0 FF 00 00                  mov eax, 0xffe0
00854964  66 03 F8                        add di, ax
00854967  83 FE 61                        cmp esi, 0x61
0085496A  72 0C                           jb 0x140854978
0085496C  83 FE 7A                        cmp esi, 0x7a
0085496F  0F 87 87 02 00 00               ja 0x140854bfc
00854975  66 03 F0                        add si, ax
00854978  0F B7 C6                        movzx eax, si
0085497B  0F B7 F7                        movzx esi, di
0085497E  2B F0                           sub esi, eax
00854980  0F 85 52 FC FF FF               jne 0x1408545d8
00854986  B8 FF FF 00 00                  mov eax, 0xffff
0085498B  66 44 03 F0                     add r14w, ax
0085498F  66 44 03 F8                     add r15w, ax
00854993  EB 8C                           jmp 0x140854921
00854995  4D 8B 62 08                     mov r12, qword ptr [r10 + 8]
00854999  B8 FF FF 00 00                  mov eax, 0xffff
0085499E  45 0F B7 3A                     movzx r15d, word ptr [r10]
008549A2  66 41 D1 EE                     shr r14w, 1
008549A6  66 45 85 F6                     test r14w, r14w
008549AA  0F 84 3B FC FF FF               je 0x1408545eb
008549B0  66 45 85 FF                     test r15w, r15w
008549B4  0F 84 31 FC FF FF               je 0x1408545eb
008549BA  41 0F B7 7D 00                  movzx edi, word ptr [r13]
008549BF  49 83 C5 02                     add r13, 2
008549C3  41 0F B6 34 24                  movzx esi, byte ptr [r12]
008549C8  49 FF C4                        inc r12
008549CB  66 3B FE                        cmp di, si
008549CE  74 38                           je 0x140854a08
008549D0  66 83 FF 61                     cmp di, 0x61
008549D4  72 5C                           jb 0x140854a32
008549D6  66 83 FF 7A                     cmp di, 0x7a
008549DA  77 4B                           ja 0x140854a27
008549DC  B8 E0 FF 00 00                  mov eax, 0xffe0
008549E1  66 03 F8                        add di, ax
008549E4  83 FE 61                        cmp esi, 0x61
008549E7  72 0C                           jb 0x1408549f5
008549E9  83 FE 7A                        cmp esi, 0x7a
008549EC  0F 87 FA 01 00 00               ja 0x140854bec
008549F2  66 03 F0                        add si, ax
008549F5  0F B7 C6                        movzx eax, si
008549F8  0F B7 F7                        movzx esi, di
008549FB  2B F0                           sub esi, eax
008549FD  0F 85 F2 FB FF FF               jne 0x1408545f5
00854A03  B8 FF FF 00 00                  mov eax, 0xffff
00854A08  66 44 03 F0                     add r14w, ax
00854A0C  66 44 03 F8                     add r15w, ax
00854A10  EB 94                           jmp 0x1408549a6
00854A12  0F B7 CF                        movzx ecx, di
00854A15  E8 D6 A6 00 00                  call 0x14085f0f0
00854A1A  0F B7 F8                        movzx edi, ax
00854A1D  B8 E0 FF 00 00                  mov eax, 0xffe0
00854A22  E9 40 FF FF FF                  jmp 0x140854967
00854A27  0F B7 CF                        movzx ecx, di
00854A2A  E8 C1 A6 00 00                  call 0x14085f0f0
00854A2F  0F B7 F8                        movzx edi, ax
00854A32  B8 E0 FF 00 00                  mov eax, 0xffe0
00854A37  EB AB                           jmp 0x1408549e4
00854A39  4C 8B 7B 08                     mov r15, qword ptr [rbx + 8]
00854A3D  B8 FF FF 00 00                  mov eax, 0xffff
00854A42  44 0F B7 33                     movzx r14d, word ptr [rbx]
00854A46  66 D1 EE                        shr si, 1
00854A49  66 85 F6                        test si, si
00854A4C  0F 84 4D FC FF FF               je 0x14085469f
00854A52  66 45 85 F6                     test r14w, r14w
00854A56  0F 84 43 FC FF FF               je 0x14085469f
00854A5C  41 0F B7 1C 24                  movzx ebx, word ptr [r12]
00854A61  49 83 C4 02                     add r12, 2
00854A65  41 0F B6 3F                     movzx edi, byte ptr [r15]
00854A69  49 FF C7                        inc r15
00854A6C  66 3B DF                        cmp bx, di
00854A6F  74 40                           je 0x140854ab1
00854A71  66 83 FB 61                     cmp bx, 0x61
00854A75  0F 82 40 01 00 00               jb 0x140854bbb
00854A7B  66 83 FB 7A                     cmp bx, 0x7a
00854A7F  0F 87 2B 01 00 00               ja 0x140854bb0
00854A85  B8 E0 FF 00 00                  mov eax, 0xffe0
00854A8A  66 03 D8                        add bx, ax
00854A8D  83 FF 61                        cmp edi, 0x61
00854A90  72 0C                           jb 0x140854a9e
00854A92  83 FF 7A                        cmp edi, 0x7a
00854A95  0F 87 81 01 00 00               ja 0x140854c1c
00854A9B  66 03 F8                        add di, ax
00854A9E  0F B7 C7                        movzx eax, di
00854AA1  0F B7 DB                        movzx ebx, bx
00854AA4  2B D8                           sub ebx, eax
00854AA6  0F 85 FC FB FF FF               jne 0x1408546a8
00854AAC  B8 FF FF 00 00                  mov eax, 0xffff
00854AB1  66 03 F0                        add si, ax
00854AB4  66 44 03 F0                     add r14w, ax
00854AB8  EB 8F                           jmp 0x140854a49
00854ABA  4C 8B 7B 08                     mov r15, qword ptr [rbx + 8]
00854ABE  B8 FF FF 00 00                  mov eax, 0xffff
00854AC3  44 0F B7 33                     movzx r14d, word ptr [rbx]
00854AC7  66 D1 EE                        shr si, 1
00854ACA  66 85 F6                        test si, si
00854ACD  0F 84 DE FB FF FF               je 0x1408546b1
00854AD3  66 45 85 F6                     test r14w, r14w
00854AD7  0F 84 D4 FB FF FF               je 0x1408546b1
00854ADD  41 0F B7 1C 24                  movzx ebx, word ptr [r12]
00854AE2  49 83 C4 02                     add r12, 2
00854AE6  41 0F B6 3F                     movzx edi, byte ptr [r15]
00854AEA  49 FF C7                        inc r15
00854AED  66 3B DF                        cmp bx, di
00854AF0  74 40                           je 0x140854b32
00854AF2  66 83 FB 61                     cmp bx, 0x61
00854AF6  0F 82 D4 00 00 00               jb 0x140854bd0
00854AFC  66 83 FB 7A                     cmp bx, 0x7a
00854B00  0F 87 BF 00 00 00               ja 0x140854bc5
00854B06  B8 E0 FF 00 00                  mov eax, 0xffe0
00854B0B  66 03 D8                        add bx, ax
00854B0E  83 FF 61                        cmp edi, 0x61
00854B11  72 0C                           jb 0x140854b1f
00854B13  83 FF 7A                        cmp edi, 0x7a
00854B16  0F 87 10 01 00 00               ja 0x140854c2c
00854B1C  66 03 F8                        add di, ax
00854B1F  0F B7 C7                        movzx eax, di
00854B22  0F B7 DB                        movzx ebx, bx
00854B25  2B D8                           sub ebx, eax
00854B27  0F 85 8D FB FF FF               jne 0x1408546ba
00854B2D  B8 FF FF 00 00                  mov eax, 0xffff
00854B32  66 03 F0                        add si, ax
00854B35  66 44 03 F0                     add r14w, ax
00854B39  EB 8F                           jmp 0x140854aca
00854B3B  4D 8B 7A 08                     mov r15, qword ptr [r10 + 8]
00854B3F  B8 FF FF 00 00                  mov eax, 0xffff
00854B44  45 0F B7 32                     movzx r14d, word ptr [r10]
00854B48  66 D1 EE                        shr si, 1
00854B4B  66 85 F6                        test si, si
00854B4E  0F 84 73 FB FF FF               je 0x1408546c7
00854B54  66 45 85 F6                     test r14w, r14w
00854B58  0F 84 69 FB FF FF               je 0x1408546c7
00854B5E  41 0F B7 1C 24                  movzx ebx, word ptr [r12]
00854B63  49 83 C4 02                     add r12, 2
00854B67  41 0F B6 3F                     movzx edi, byte ptr [r15]
00854B6B  49 FF C7                        inc r15
00854B6E  66 3B DF                        cmp bx, di
00854B71  74 34                           je 0x140854ba7
00854B73  66 83 FB 61                     cmp bx, 0x61
00854B77  72 6C                           jb 0x140854be5
00854B79  66 83 FB 7A                     cmp bx, 0x7a
00854B7D  77 5B                           ja 0x140854bda
00854B7F  B8 E0 FF 00 00                  mov eax, 0xffe0
00854B84  66 03 D8                        add bx, ax
00854B87  83 FF 61                        cmp edi, 0x61
00854B8A  72 08                           jb 0x140854b94
00854B8C  83 FF 7A                        cmp edi, 0x7a
00854B8F  77 7B                           ja 0x140854c0c
00854B91  66 03 F8                        add di, ax
00854B94  0F B7 C7                        movzx eax, di
00854B97  0F B7 DB                        movzx ebx, bx
00854B9A  2B D8                           sub ebx, eax
00854B9C  0F 85 2E FB FF FF               jne 0x1408546d0
00854BA2  B8 FF FF 00 00                  mov eax, 0xffff
00854BA7  66 03 F0                        add si, ax
00854BAA  66 44 03 F0                     add r14w, ax
00854BAE  EB 9B                           jmp 0x140854b4b
00854BB0  0F B7 CB                        movzx ecx, bx
00854BB3  E8 38 A5 00 00                  call 0x14085f0f0
00854BB8  0F B7 D8                        movzx ebx, ax
00854BBB  B8 E0 FF 00 00                  mov eax, 0xffe0
00854BC0  E9 C8 FE FF FF                  jmp 0x140854a8d
00854BC5  0F B7 CB                        movzx ecx, bx
00854BC8  E8 23 A5 00 00                  call 0x14085f0f0
00854BCD  0F B7 D8                        movzx ebx, ax
00854BD0  B8 E0 FF 00 00                  mov eax, 0xffe0
00854BD5  E9 34 FF FF FF                  jmp 0x140854b0e
00854BDA  0F B7 CB                        movzx ecx, bx
00854BDD  E8 0E A5 00 00                  call 0x14085f0f0
00854BE2  0F B7 D8                        movzx ebx, ax
00854BE5  B8 E0 FF 00 00                  mov eax, 0xffe0
00854BEA  EB 9B                           jmp 0x140854b87
00854BEC  0F B7 CE                        movzx ecx, si
00854BEF  E8 FC A4 00 00                  call 0x14085f0f0
00854BF4  0F B7 F0                        movzx esi, ax
00854BF7  E9 F9 FD FF FF                  jmp 0x1408549f5
00854BFC  0F B7 CE                        movzx ecx, si
00854BFF  E8 EC A4 00 00                  call 0x14085f0f0
00854C04  0F B7 F0                        movzx esi, ax
00854C07  E9 6C FD FF FF                  jmp 0x140854978
00854C0C  0F B7 CF                        movzx ecx, di
00854C0F  E8 DC A4 00 00                  call 0x14085f0f0
00854C14  0F B7 F8                        movzx edi, ax
00854C17  E9 78 FF FF FF                  jmp 0x140854b94
00854C1C  0F B7 CF                        movzx ecx, di
00854C1F  E8 CC A4 00 00                  call 0x14085f0f0
00854C24  0F B7 F8                        movzx edi, ax
00854C27  E9 72 FE FF FF                  jmp 0x140854a9e
00854C2C  0F B7 CF                        movzx ecx, di
00854C2F  E8 BC A4 00 00                  call 0x14085f0f0
00854C34  0F B7 F8                        movzx edi, ax
00854C37  E9 E3 FE FF FF                  jmp 0x140854b1f
00854C3C  BA FF FF FF FF                  mov edx, 0xffffffff
00854C41  E9 BB F3 FF FF                  jmp 0x140854001
00854C46  BE FF FF FF FF                  mov esi, 0xffffffff
00854C4B  E9 C9 F8 FF FF                  jmp 0x140854519
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0085416A(void)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    unsigned __int8 v_stack_p20;

    v_r14 = 0;
    *(unsigned int *)(v_rbp - 48) = 0xFFFFFFFFULL;
    *(unsigned int *)(v_rbp - 44) = 0;
    if (((*(unsigned __int8 *)(v_r13 + 140)) & (1)) == 0) goto loc_00854591;
    result = HvpGetCellFlat(v_r13, (unsigned int)(*(unsigned int *)(v_r12 + result * 4 + 4)), v_rbp - 48, a4);
loc_00854197:
    if (result == 0) goto loc_008545C5;
    if (((*(unsigned __int8 *)(result + 2)) & (32)) == 0) goto loc_008548E2;
    if (*(unsigned __int64 *)(v_rbp + 72) != 0) goto loc_0085482A;
    v_rdi = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp + 64))) >> (1));
loc_008541D6:
    if ((unsigned __int16)(v_rdi) == 0) goto loc_0085424A;
    if ((unsigned __int16)(*(unsigned __int16 *)(result + 72)) == 0) goto loc_0085424A;
    v_r15 = (*(unsigned __int64 *)(v_r15 + 8)) + (2);
    v_r12 = (result + 76) + 1;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r15 + 8)))) == ((unsigned __int16)(*(unsigned __int8 *)(result + 76)))) goto loc_00854236;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r15 + 8)))) < 97) goto loc_00854548;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r15 + 8)))) > 122) goto loc_0085453D;
    v_rbx = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_r15 + 8))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_00854212:
    if (((unsigned int)(*(unsigned __int8 *)(result + 76))) < 97) goto loc_00854223;
    if (((unsigned int)(*(unsigned __int8 *)(result + 76))) > 122) goto loc_00854868;
    v_rsi = (unsigned __int16)((*(unsigned __int8 *)(result + 76)) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_00854223:
    v_rbx = (unsigned int)(((unsigned __int16)(v_rbx)) - ((unsigned int)((unsigned __int16)(v_rsi))));
    if (condition_is_not_equal) goto loc_008546D2;
loc_00854236:
    v_rdi = (unsigned __int16)((v_rdi) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    v_r14 = (unsigned __int16)((*(unsigned __int16 *)(result + 72)) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    goto loc_008541D6;
loc_0085424A:
    v_rbx = (unsigned int)(((unsigned __int16)(v_rdi)) - ((unsigned int)((unsigned __int16)(v_r14))));
    v_r14 = 0;
loc_00854259:
    if (((*(unsigned __int8 *)(v_r13 + 140)) & (1)) != 0) goto loc_00854707;
    result = HvpReleaseCellPaged(v_r13, v_rbp - 48, v_rbp - 48, a4);
loc_00854273:
    if ((unsigned int)(v_rbx) != 0) goto loc_008543DA;
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 80)) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbp + 56) + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 64)))) * 4 + 4)));
loc_008542BA:
    *(unsigned int *)(v_r14) = 0xFFFFFFFFULL;
    *(unsigned int *)(*(unsigned __int64 *)(v_rbp + 88)) = 0x80000000ULL;
loc_008543DA:
    if (sign_flag) goto loc_00854C3C;
loc_0085453D:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(v_rbx), 1, *(unsigned __int64 *)(v_rbp + 80), a4);
loc_00854548:
    goto loc_00854212;
loc_00854591:
    result = HvpGetCellPaged((unsigned __int16)(v_rbx), 1, *(unsigned __int64 *)(v_rbp + 80), a4);
    goto loc_00854197;
loc_008545C5:
    goto loc_008542BA;
loc_008546C7:
    v_rbx = (unsigned int)(((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rbp - 64)))) - ((unsigned int)((unsigned __int16)(*(unsigned __int64 *)(v_rbp + 80)))));
loc_008546D0:
    v_rbx = (unsigned int)(-(v_rbx));
loc_008546D2:
    v_r14 = 0;
    goto loc_00854259;
loc_00854707:
    result = HvpReleaseCellFlat((unsigned __int16)(v_rbx), 1, *(unsigned __int64 *)(v_rbp + 80), a4);
    goto loc_00854273;
loc_0085482A:
    result = CmpCompareTwoCompressedNames(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 72) + 8), *(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp + 72)), *(unsigned __int64 *)(v_rbp + 56), *(unsigned __int16 *)((unsigned __int16)(v_rbx) + 72));
loc_0085483F:
    goto loc_00854259;
loc_00854868:
    result = RtlUpcaseUnicodeChar((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rbp - 64))), *(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp + 72)), *(unsigned __int64 *)(v_rbp + 56), *(unsigned __int16 *)((unsigned __int16)(v_rbx) + 72));
    goto loc_00854223;
loc_008548E2:
    if (*(unsigned __int64 *)(v_rbp + 72) != 0) goto loc_00854B3B;
    a4 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rbp - 64))) + 72)))) >> (1);
    a2 = (*(unsigned __int16 *)(v_r15)) >> (1);
    v_stack_p20 = 1;
    result = RtlCompareUnicodeStrings(*(unsigned __int64 *)(v_r15 + 8), a2, *(unsigned __int64 *)(v_rbp + 56), a4);
    goto loc_0085483F;
loc_00854B3B:
    v_rsi = (unsigned __int16)(((unsigned int)(*(unsigned int *)(v_rbp - 64))) >> (1));
loc_00854B4B:
    if ((unsigned __int16)(v_rsi) == 0) goto loc_008546C7;
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp + 72))) == 0) goto loc_008546C7;
    v_r12 = (*(unsigned __int64 *)(v_rbp + 56)) + (2);
    v_r15 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 72) + 8)) + 1;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp + 56)))) == ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 72) + 8))))) goto loc_00854BA7;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp + 56)))) < 97) goto loc_00854BE5;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp + 56)))) > 122) goto loc_00854BDA;
    v_rbx = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp + 56))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_00854B87:
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 72) + 8)))) < 97) goto loc_00854B94;
    if (((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 72) + 8)))) > 122) goto loc_00854C0C;
    v_rdi = (unsigned __int16)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbp + 72) + 8))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_00854B94:
    v_rbx = (unsigned int)(((unsigned __int16)(v_rbx)) - ((unsigned int)((unsigned __int16)(v_rdi))));
    if (condition_is_not_equal) goto loc_008546D0;
loc_00854BA7:
    v_rsi = (unsigned __int16)((v_rsi) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    v_r14 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rbp + 72))) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    goto loc_00854B4B;
loc_00854BDA:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(v_rbx), a2, *(unsigned __int64 *)(v_rbp + 56), a4);
loc_00854BE5:
    goto loc_00854B87;
loc_00854C0C:
    result = RtlUpcaseUnicodeChar((unsigned __int16)(v_rdi), a2, *(unsigned __int64 *)(v_rbp + 56), a4);
    goto loc_00854B94;
loc_00854C3C:
}
```

## 5. (Beta) C Style

```c
void sub_0085416A(void)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    uint8_t v_stack_p20;

    local_r14 = 0;
    *(uint32_t *)(local_rbp - 0x30) = 0xFFFFFFFFULL;
    *(uint32_t *)(local_rbp - 0x2C) = 0;
    if (((*(uint8_t *)(local_r13 + 0x8C)) & (1)) == 0) goto loc_00854591;
    result = HvpGetCellFlat(local_r13, (uint32_t)(*(uint32_t *)(local_r12 + result * 4 + 0x4)), local_rbp - 48, a4);
loc_00854197:
    if (result == 0) goto loc_008545C5;
    if (((*(uint8_t *)(result + 0x2)) & (32)) == 0) goto loc_008548E2;
    if (*(uint64_t *)(local_rbp + 0x48) != 0) goto loc_0085482A;
    local_rdi = (uint16_t)((*(uint16_t *)(*(uint64_t *)(local_rbp + 0x40))) >> (1));
loc_008541D6:
    if ((uint16_t)(local_rdi) == 0) goto loc_0085424A;
    if ((uint16_t)(*(uint16_t *)(result + 0x48)) == 0) goto loc_0085424A;
    local_r15 = (*(uint64_t *)(local_r15 + 0x8)) + (2);
    local_r12 = (result + 76) + 1;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r15 + 0x8)))) == ((uint16_t)(*(uint8_t *)(result + 0x4C)))) goto loc_00854236;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r15 + 0x8)))) < 97) goto loc_00854548;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r15 + 0x8)))) > 122) goto loc_0085453D;
    local_rbx = (uint16_t)((*(uint16_t *)(*(uint64_t *)(local_r15 + 0x8))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_00854212:
    if (((uint32_t)(*(uint8_t *)(result + 0x4C))) < 97) goto loc_00854223;
    if (((uint32_t)(*(uint8_t *)(result + 0x4C))) > 122) goto loc_00854868;
    local_rsi = (uint16_t)((*(uint8_t *)(result + 0x4C)) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_00854223:
    local_rbx = (uint32_t)(((uint16_t)(local_rbx)) - ((uint32_t)((uint16_t)(local_rsi))));
    if (condition_is_not_equal) goto loc_008546D2;
loc_00854236:
    local_rdi = (uint16_t)((local_rdi) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    local_r14 = (uint16_t)((*(uint16_t *)(result + 0x48)) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    goto loc_008541D6;
loc_0085424A:
    local_rbx = (uint32_t)(((uint16_t)(local_rdi)) - ((uint32_t)((uint16_t)(local_r14))));
    local_r14 = 0;
loc_00854259:
    if (((*(uint8_t *)(local_r13 + 0x8C)) & (1)) != 0) goto loc_00854707;
    result = HvpReleaseCellPaged(local_r13, local_rbp - 48, local_rbp - 48, a4);
loc_00854273:
    if ((uint32_t)(local_rbx) != 0) goto loc_008543DA;
    *(uint32_t *)(*(uint64_t *)(local_rbp + 0x50)) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbp + 0x38) + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x40)))) * 4 + 0x4)));
loc_008542BA:
    *(uint32_t *)(local_r14) = 0xFFFFFFFFULL;
    *(uint32_t *)(*(uint64_t *)(local_rbp + 0x58)) = 0x80000000ULL;
loc_008543DA:
    if (sign_flag) goto loc_00854C3C;
loc_0085453D:
    result = RtlUpcaseUnicodeChar((uint16_t)(local_rbx), 1, *(uint64_t *)(local_rbp + 0x50), a4);
loc_00854548:
    goto loc_00854212;
loc_00854591:
    result = HvpGetCellPaged((uint16_t)(local_rbx), 1, *(uint64_t *)(local_rbp + 0x50), a4);
    goto loc_00854197;
loc_008545C5:
    goto loc_008542BA;
loc_008546C7:
    local_rbx = (uint32_t)(((uint16_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x40)))) - ((uint32_t)((uint16_t)(*(uint64_t *)(local_rbp + 0x50)))));
loc_008546D0:
    local_rbx = (uint32_t)(-(local_rbx));
loc_008546D2:
    local_r14 = 0;
    goto loc_00854259;
loc_00854707:
    result = HvpReleaseCellFlat((uint16_t)(local_rbx), 1, *(uint64_t *)(local_rbp + 0x50), a4);
    goto loc_00854273;
loc_0085482A:
    result = CmpCompareTwoCompressedNames(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x48) + 0x8), *(uint16_t *)(*(uint64_t *)(local_rbp + 0x48)), *(uint64_t *)(local_rbp + 0x38), *(uint16_t *)((uint16_t)(local_rbx) + 0x48));
loc_0085483F:
    goto loc_00854259;
loc_00854868:
    result = RtlUpcaseUnicodeChar((uint16_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x40))), *(uint16_t *)(*(uint64_t *)(local_rbp + 0x48)), *(uint64_t *)(local_rbp + 0x38), *(uint16_t *)((uint16_t)(local_rbx) + 0x48));
    goto loc_00854223;
loc_008548E2:
    if (*(uint64_t *)(local_rbp + 0x48) != 0) goto loc_00854B3B;
    a4 = ((uint32_t)((uint32_t)(*(uint16_t *)((uint16_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x40))) + 0x48)))) >> (1);
    a2 = (*(uint16_t *)(local_r15)) >> (1);
    v_stack_p20 = 1;
    result = RtlCompareUnicodeStrings(*(uint64_t *)(local_r15 + 0x8), a2, *(uint64_t *)(local_rbp + 0x38), a4);
    goto loc_0085483F;
loc_00854B3B:
    local_rsi = (uint16_t)(((uint32_t)(*(uint32_t *)(local_rbp - 0x40))) >> (1));
loc_00854B4B:
    if ((uint16_t)(local_rsi) == 0) goto loc_008546C7;
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rbp + 0x48))) == 0) goto loc_008546C7;
    local_r12 = (*(uint64_t *)(local_rbp + 0x38)) + (2);
    local_r15 = (*(uint64_t *)(*(uint64_t *)(local_rbp + 0x48) + 0x8)) + 1;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rbp + 0x38)))) == ((uint16_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x48) + 0x8))))) goto loc_00854BA7;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rbp + 0x38)))) < 97) goto loc_00854BE5;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_rbp + 0x38)))) > 122) goto loc_00854BDA;
    local_rbx = (uint16_t)((*(uint16_t *)(*(uint64_t *)(local_rbp + 0x38))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_00854B87:
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x48) + 0x8)))) < 97) goto loc_00854B94;
    if (((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x48) + 0x8)))) > 122) goto loc_00854C0C;
    local_rdi = (uint16_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rbp + 0x48) + 0x8))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_00854B94:
    local_rbx = (uint32_t)(((uint16_t)(local_rbx)) - ((uint32_t)((uint16_t)(local_rdi))));
    if (condition_is_not_equal) goto loc_008546D0;
loc_00854BA7:
    local_rsi = (uint16_t)((local_rsi) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    local_r14 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(local_rbp + 0x48))) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    goto loc_00854B4B;
loc_00854BDA:
    result = RtlUpcaseUnicodeChar((uint16_t)(local_rbx), a2, *(uint64_t *)(local_rbp + 0x38), a4);
loc_00854BE5:
    goto loc_00854B87;
loc_00854C0C:
    result = RtlUpcaseUnicodeChar((uint16_t)(local_rdi), a2, *(uint64_t *)(local_rbp + 0x38), a4);
    goto loc_00854B94;
loc_00854C3C:
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0085416A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
