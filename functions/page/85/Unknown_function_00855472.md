# sub_00855472

- RVA: `0x00855472`–`0x00855882` (길이 `1,040` bytes)
- VA: `0x0000000140855472`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006A0B4`
- 디코드: `256`개 명령, `1,040/1,040` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00855472` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00855480` → [CmpLockKcbStackShared](../94/CmpLockKcbStackShared_function_00948000.md) (function, `0x00948000`)
- `0x0085548A` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x0085549B` → [CmpUnlockKcbStack](../84/CmpUnlockKcbStack_function_00848460.md) (function, `0x00848460`)
- `0x008554A7` → [CmpTransSearchAddTransFromKeyBody](../87/CmpTransSearchAddTransFromKeyBody_function_008736B8.md) (function, `0x008736B8`)
- `0x00855509` → [HvpGetCellContextInitialize](HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x00855513` → [HvpGetCellContextInitialize](HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)
- `0x0085553E` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085557F` → [HvpGetCellFlat](HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x0085559E` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x0085567D` → [HvpReleaseCellPaged](HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x008556AC` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x008556B9` → [RtlUpcaseUnicodeChar](RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00855795` → [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x008557B5` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x008557FD` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00855807` → [HvpReleaseCellFlat](HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0085548A` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x0085559E` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **24**
  - `0x00855477` → [sub_008551B7 + 0x1A4](Unknown_function_008551B7.md) (`tail-transfer`)
  - `0x00855491` → [sub_008558BC + 0x41](Unknown_function_008558BC.md) (`tail-transfer`)
  - `0x008554B0` → [sub_008551B7 + 0x252](Unknown_function_008551B7.md) (`tail-transfer`)
  - `0x008554C0` → [sub_008551B7 + 0x57](Unknown_function_008551B7.md) (`tail-transfer`)
  - `0x008554CD` → [sub_008551B7 + 0x135](Unknown_function_008551B7.md) (`tail-transfer`)
  - `0x008554D9` → [sub_008558BC + 0x2D](Unknown_function_008558BC.md) (`tail-transfer`)
  - `0x008554E2` → [sub_008558BC + 0x12](Unknown_function_008558BC.md) (`tail-transfer`)
  - `0x0085551F` → [sub_008558BC + 0x36](Unknown_function_008558BC.md) (`tail-transfer`)
  - `0x00855636` → [sub_008558BC](Unknown_function_008558BC.md) (`tail-transfer`)
  - `0x0085568B` → [sub_008551B7 + 0x13A](Unknown_function_008551B7.md) (`tail-transfer`)
  - `0x008557B0` → [sub_008551B7 + 0x148](Unknown_function_008551B7.md) (`tail-transfer`)
  - `0x008557D1` → [sub_008551B7 + 0x23C](Unknown_function_008551B7.md) (`tail-transfer`)
  - `0x008557DA` → [sub_008551B7 + 0x86](Unknown_function_008551B7.md) (`tail-transfer`)
  - `0x008557EA` → [sub_008551B7 + 0x135](Unknown_function_008551B7.md) (`tail-transfer`)
  - `0x008557F8` → [sub_008551B7 + 0xBF](Unknown_function_008551B7.md) (`tail-transfer`)
  - `0x00855802` → [sub_008551B7 + 0x20E](Unknown_function_008551B7.md) (`tail-transfer`)
  - `0x0085580C` → [sub_008551B7 + 0x168](Unknown_function_008551B7.md) (`tail-transfer`)
  - `0x0085581B` → [sub_008551B7 + 0xDF](Unknown_function_008551B7.md) (`tail-transfer`)
  - `0x00855823` → [sub_008551B7 + 0x1EF](Unknown_function_008551B7.md) (`tail-transfer`)
  - `0x00855832` → [sub_008551B7 + 0x43](Unknown_function_008551B7.md) (`tail-transfer`)
  - `0x0085584D` → [sub_008558BC + 0x5E](Unknown_function_008558BC.md) (`tail-transfer`)
  - `0x00855869` → [sub_008551B7 + 0x33](Unknown_function_008551B7.md) (`tail-transfer`)
  - `0x00855872` → [sub_008551B7 + 0x1B7](Unknown_function_008551B7.md) (`tail-transfer`)
  - `0x0085587D` → [sub_008551B7 + 0x1EF](Unknown_function_008551B7.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00855472  E8 39 F8 FF FF                  call 0x140854cb0
00855477  E9 DF FE FF FF                  jmp 0x14085535b
0085547C  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00855480  E8 7B 2B 0F 00                  call 0x140948000
00855485  33 D2                           xor edx, edx
00855487  48 8B CF                        mov rcx, rdi
0085548A  E8 F1 3F 37 00                  call 0x140bc9480
0085548F  84 C0                           test al, al
00855491  0F 85 66 04 00 00               jne 0x1408558fd
00855497  48 8D 4D 80                     lea rcx, [rbp - 0x80]
0085549B  E8 C0 2F FF FF                  call 0x140848460
008554A0  48 8D 55 B0                     lea rdx, [rbp - 0x50]
008554A4  48 8B CF                        mov rcx, rdi
008554A7  E8 0C E2 01 00                  call 0x1408736b8
008554AC  8B F8                           mov edi, eax
008554AE  85 C0                           test eax, eax
008554B0  0F 88 53 FF FF FF               js 0x140855409
008554B6  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
008554BB  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
008554C0  E9 49 FD FF FF                  jmp 0x14085520e
008554C5  41 0F B6 44 24 41               movzx eax, byte ptr [r12 + 0x41]
008554CB  3C 01                           cmp al, 1
008554CD  0F 84 19 FE FF FF               je 0x1408552ec
008554D3  41 83 7C 24 28 FF               cmp dword ptr [r12 + 0x28], -1
008554D9  0F 84 0A 04 00 00               je 0x1408558e9
008554DF  48 85 DB                        test rbx, rbx
008554E2  0F 85 E6 03 00 00               jne 0x1408558ce
008554E8  49 8D 74 24 60                  lea rsi, [r12 + 0x60]
008554ED  44 8B 77 64                     mov r14d, dword ptr [rdi + 0x64]
008554F1  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
008554F6  4D 8B 6C 24 20                  mov r13, qword ptr [r12 + 0x20]
008554FB  48 89 75 C0                     mov qword ptr [rbp - 0x40], rsi
008554FF  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
00855504  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00855509  E8 02 0A 00 00                  call 0x140855f10
0085550E  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00855513  E8 F8 09 00 00                  call 0x140855f10
00855518  8B 1E                           mov ebx, dword ptr [rsi]
0085551A  89 5D A0                        mov dword ptr [rbp - 0x60], ebx
0085551D  85 DB                           test ebx, ebx
0085551F  0F 84 CD 03 00 00               je 0x1408558f2
00855525  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
0085552D  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00855532  8B 56 04                        mov edx, dword ptr [rsi + 4]
00855535  49 8B CD                        mov rcx, r13
00855538  0F 84 57 02 00 00               je 0x140855795
0085553E  E8 1D F7 FF FF                  call 0x140854c60
00855543  44 3B F3                        cmp r14d, ebx
00855546  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
0085554A  48 8B D0                        mov rdx, rax
0085554D  41 8B CF                        mov ecx, r15d
00855550  45 0F 43 F7                     cmovae r14d, r15d
00855554  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
00855558  44 89 74 24 44                  mov dword ptr [rsp + 0x44], r14d
0085555D  3B CB                           cmp ecx, ebx
0085555F  0F 83 3A 02 00 00               jae 0x14085579f
00855565  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
0085556D  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
00855572  42 8B 14 B2                     mov edx, dword ptr [rdx + r14*4]
00855576  49 8B CD                        mov rcx, r13
00855579  0F 84 2D 01 00 00               je 0x1408556ac
0085557F  E8 DC F6 FF FF                  call 0x140854c60
00855584  F6 40 10 01                     test byte ptr [rax + 0x10], 1
00855588  4C 8D 60 14                     lea r12, [rax + 0x14]
0085558C  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00855590  44 0F B7 78 02                  movzx r15d, word ptr [rax + 2]
00855595  48 8B 59 08                     mov rbx, qword ptr [rcx + 8]
00855599  0F B7 39                        movzx edi, word ptr [rcx]
0085559C  75 4F                           jne 0x1408555ed
0085559E  E8 4D 8C AA FF                  call 0x1402fe1f0
008555A3  8B F7                           mov esi, edi
008555A5  45 8B DF                        mov r11d, r15d
008555A8  48 D1 EE                        shr rsi, 1
008555AB  49 D1 EB                        shr r11, 1
008555AE  48 8B 88 B0 04 00 00            mov rcx, qword ptr [rax + 0x4b0]
008555B5  49 3B F3                        cmp rsi, r11
008555B8  48 8B C6                        mov rax, rsi
008555BB  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
008555C0  49 0F 47 C3                     cmova rax, r11
008555C4  4C 2B E3                        sub r12, rbx
008555C7  4C 8D 14 43                     lea r10, [rbx + rax*2]
008555CB  49 3B DA                        cmp rbx, r10
008555CE  0F 83 B9 01 00 00               jae 0x14085578d
008555D4  44 0F B7 03                     movzx r8d, word ptr [rbx]
008555D8  46 0F B7 0C 23                  movzx r9d, word ptr [rbx + r12]
008555DD  66 45 3B C1                     cmp r8w, r9w
008555E1  0F 85 E4 00 00 00               jne 0x1408556cb
008555E7  48 83 C3 02                     add rbx, 2
008555EB  EB DE                           jmp 0x1408555cb
008555ED  66 D1 EF                        shr di, 1
008555F0  66 85 FF                        test di, di
008555F3  74 64                           je 0x140855659
008555F5  66 45 85 FF                     test r15w, r15w
008555F9  74 5E                           je 0x140855659
008555FB  0F B7 33                        movzx esi, word ptr [rbx]
008555FE  48 83 C3 02                     add rbx, 2
00855602  45 0F B6 34 24                  movzx r14d, byte ptr [r12]
00855607  49 FF C4                        inc r12
0085560A  66 41 3B F6                     cmp si, r14w
0085560E  74 3B                           je 0x14085564b
00855610  66 83 FE 61                     cmp si, 0x61
00855614  0F 82 A7 00 00 00               jb 0x1408556c1
0085561A  66 83 FE 7A                     cmp si, 0x7a
0085561E  0F 87 92 00 00 00               ja 0x1408556b6
00855624  B8 E0 FF 00 00                  mov eax, 0xffe0
00855629  66 03 F0                        add si, ax
0085562C  41 83 FE 61                     cmp r14d, 0x61
00855630  72 0E                           jb 0x140855640
00855632  41 83 FE 7A                     cmp r14d, 0x7a
00855636  0F 87 80 02 00 00               ja 0x1408558bc
0085563C  66 44 03 F0                     add r14w, ax
00855640  41 0F B7 C6                     movzx eax, r14w
00855644  0F B7 F6                        movzx esi, si
00855647  2B F0                           sub esi, eax
00855649  75 17                           jne 0x140855662
0085564B  B8 FF FF 00 00                  mov eax, 0xffff
00855650  66 03 F8                        add di, ax
00855653  66 44 03 F8                     add r15w, ax
00855657  EB 97                           jmp 0x1408555f0
00855659  41 0F B7 C7                     movzx eax, r15w
0085565D  0F B7 F7                        movzx esi, di
00855660  2B F0                           sub esi, eax
00855662  44 8B 74 24 44                  mov r14d, dword ptr [rsp + 0x44]
00855667  41 F6 85 8C 00 00 00 01         test byte ptr [r13 + 0x8c], 1
0085566F  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00855674  49 8B CD                        mov rcx, r13
00855677  0F 85 38 01 00 00               jne 0x1408557b5
0085567D  E8 BE 08 00 00                  call 0x140855f40
00855682  48 8B 55 A8                     mov rdx, qword ptr [rbp - 0x58]
00855686  45 33 FF                        xor r15d, r15d
00855689  85 F6                           test esi, esi
0085568B  0F 84 60 FC FF FF               je 0x1408552f1
00855691  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
00855695  41 8D 46 01                     lea eax, [r14 + 1]
00855699  8B 5D A0                        mov ebx, dword ptr [rbp - 0x60]
0085569C  FF C1                           inc ecx
0085569E  3B C3                           cmp eax, ebx
008556A0  45 8B F7                        mov r14d, r15d
008556A3  44 0F 45 F0                     cmovne r14d, eax
008556A7  E9 A8 FE FF FF                  jmp 0x140855554
008556AC  E8 FF F5 FF FF                  call 0x140854cb0
008556B1  E9 CE FE FF FF                  jmp 0x140855584
008556B6  0F B7 CE                        movzx ecx, si
008556B9  E8 32 9A 00 00                  call 0x14085f0f0
008556BE  0F B7 F0                        movzx esi, ax
008556C1  B8 E0 FF 00 00                  mov eax, 0xffe0
008556C6  E9 61 FF FF FF                  jmp 0x14085562c
008556CB  41 83 F8 61                     cmp r8d, 0x61
008556CF  72 0F                           jb 0x1408556e0
008556D1  41 83 F8 7A                     cmp r8d, 0x7a
008556D5  77 37                           ja 0x14085570e
008556D7  B8 E0 FF 00 00                  mov eax, 0xffe0
008556DC  66 44 03 C0                     add r8w, ax
008556E0  41 83 F9 61                     cmp r9d, 0x61
008556E4  72 0F                           jb 0x1408556f5
008556E6  41 83 F9 7A                     cmp r9d, 0x7a
008556EA  77 60                           ja 0x14085574c
008556EC  B8 E0 FF 00 00                  mov eax, 0xffe0
008556F1  66 44 03 C8                     add r9w, ax
008556F5  66 45 3B C1                     cmp r8w, r9w
008556F9  0F 84 E8 FE FF FF               je 0x1408555e7
008556FF  41 0F B7 C1                     movzx eax, r9w
00855703  41 0F B7 F0                     movzx esi, r8w
00855707  2B F0                           sub esi, eax
00855709  E9 59 FF FF FF                  jmp 0x140855667
0085570E  48 85 C9                        test rcx, rcx
00855711  74 CD                           je 0x1408556e0
00855713  B8 C0 00 00 00                  mov eax, 0xc0
00855718  66 44 3B C0                     cmp r8w, ax
0085571C  72 C2                           jb 0x1408556e0
0085571E  49 8B C0                        mov rax, r8
00855721  41 8B D0                        mov edx, r8d
00855724  48 C1 E8 08                     shr rax, 8
00855728  83 E2 0F                        and edx, 0xf
0085572B  0F B7 0C 41                     movzx ecx, word ptr [rcx + rax*2]
0085572F  41 8B C0                        mov eax, r8d
00855732  C1 E8 04                        shr eax, 4
00855735  83 E0 0F                        and eax, 0xf
00855738  03 C1                           add eax, ecx
0085573A  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0085573F  0F B7 04 41                     movzx eax, word ptr [rcx + rax*2]
00855743  03 C2                           add eax, edx
00855745  66 44 03 04 41                  add r8w, word ptr [rcx + rax*2]
0085574A  EB 94                           jmp 0x1408556e0
0085574C  48 85 C9                        test rcx, rcx
0085574F  74 A4                           je 0x1408556f5
00855751  B8 C0 00 00 00                  mov eax, 0xc0
00855756  66 44 3B C8                     cmp r9w, ax
0085575A  72 99                           jb 0x1408556f5
0085575C  49 8B C1                        mov rax, r9
0085575F  41 8B D1                        mov edx, r9d
00855762  48 C1 E8 08                     shr rax, 8
00855766  83 E2 0F                        and edx, 0xf
00855769  0F B7 0C 41                     movzx ecx, word ptr [rcx + rax*2]
0085576D  41 8B C1                        mov eax, r9d
00855770  C1 E8 04                        shr eax, 4
00855773  83 E0 0F                        and eax, 0xf
00855776  03 C1                           add eax, ecx
00855778  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0085577D  0F B7 04 41                     movzx eax, word ptr [rcx + rax*2]
00855781  03 C2                           add eax, edx
00855783  66 44 03 0C 41                  add r9w, word ptr [rcx + rax*2]
00855788  E9 68 FF FF FF                  jmp 0x1408556f5
0085578D  41 2B F3                        sub esi, r11d
00855790  E9 D2 FE FF FF                  jmp 0x140855667
00855795  E8 16 F5 FF FF                  call 0x140854cb0
0085579A  E9 A4 FD FF FF                  jmp 0x140855543
0085579F  48 8B 5D C0                     mov rbx, qword ptr [rbp - 0x40]
008557A3  BF 34 00 00 C0                  mov edi, 0xc0000034
008557A8  41 BE FF FF FF FF               mov r14d, 0xffffffff
008557AE  8B 1B                           mov ebx, dword ptr [rbx]
008557B0  E9 4A FB FF FF                  jmp 0x1408552ff
008557B5  E8 66 74 00 00                  call 0x14085cc20
008557BA  E9 C3 FE FF FF                  jmp 0x140855682
008557BF  66 85 D2                        test dx, dx
008557C2  0F 85 FD FC FF FF               jne 0x1408554c5
008557C8  E9 06 FD FF FF                  jmp 0x1408554d3
008557CD  48 8D 0C 33                     lea rcx, [rbx + rsi]
008557D1  E9 1D FC FF FF                  jmp 0x1408553f3
008557D6  49 8D 0C 3C                     lea rcx, [r12 + rdi]
008557DA  E9 5E FA FF FF                  jmp 0x14085523d
008557DF  66 85 D2                        test dx, dx
008557E2  74 0C                           je 0x1408557f0
008557E4  41 80 7C 24 41 00               cmp byte ptr [r12 + 0x41], 0
008557EA  0F 85 FC FA FF FF               jne 0x1408552ec
008557F0  48 8B 5D B0                     mov rbx, qword ptr [rbp - 0x50]
008557F4  66 41 FF C8                     dec r8w
008557F8  E9 79 FA FF FF                  jmp 0x140855276
008557FD  E8 1E 74 00 00                  call 0x14085cc20
00855802  E9 BE FB FF FF                  jmp 0x1408553c5
00855807  E8 14 74 00 00                  call 0x14085cc20
0085580C  E9 0E FB FF FF                  jmp 0x14085531f
00855811  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00855816  4C 8B 64 C1 F0                  mov r12, qword ptr [rcx + rax*8 - 0x10]
0085581B  E9 76 FA FF FF                  jmp 0x140855296
00855820  41 8B FF                        mov edi, r15d
00855823  E9 7E FB FF FF                  jmp 0x1408553a6
00855828  48 8B 86 C0 00 00 00            mov rax, qword ptr [rsi + 0xc0]
0085582F  48 85 C0                        test rax, rax
00855832  0F 84 C2 F9 FF FF               je 0x1408551fa
00855838  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00855840  48 8B 48 10                     mov rcx, qword ptr [rax + 0x10]
00855844  49 0F BF D5                     movsx rdx, r13w
00855848  66 41 83 FD 02                  cmp r13w, 2
0085584D  0F 8D C7 00 00 00               jge 0x14085591a
00855853  48 89 4C D5 88                  mov qword ptr [rbp + rdx*8 - 0x78], rcx
00855858  4C 8B 45 98                     mov r8, qword ptr [rbp - 0x68]
0085585C  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
00855860  66 41 FF CD                     dec r13w
00855864  48 85 C0                        test rax, rax
00855867  75 D7                           jne 0x140855840
00855869  E9 7C F9 FF FF                  jmp 0x1408551ea
0085586E  F6 43 10 02                     test byte ptr [rbx + 0x10], 2
00855872  0F 84 F6 FA FF FF               je 0x14085536e
00855878  BF 34 00 00 C0                  mov edi, 0xc0000034
0085587D  E9 24 FB FF FF                  jmp 0x1408553a6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00855472(__int64 a1, int a2)
{
    __int64 result;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    result = HvpGetCellPaged(a1, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00855472(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    uint32_t v_stack_p44;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    result = HvpGetCellPaged(Arg1, Arg2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00855472&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
