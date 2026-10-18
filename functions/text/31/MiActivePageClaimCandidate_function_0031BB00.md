# MiActivePageClaimCandidate

- RVA: `0x0031BB00`–`0x0031C673` (길이 `2,931` bytes)
- VA: `0x000000014031BB00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00074D80`
- 디코드: `591`개 명령, `2,931/2,931` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **71**

### Outgoing calls
- `0x0031BE8F` → [MiHyperPage](MiHyperPage_function_0031DCD4.md) (function, `0x0031DCD4`)
- `0x0031BF69` → [MiGetSystemRegionType](../28/MiGetSystemRegionType_function_0028EC80.md) (function, `0x0028EC80`)
- `0x0031BFAF` → [MiSafeLockPage](../32/MiSafeLockPage_function_00321620.md) (function, `0x00321620`)
- `0x0031C005` → [MiGetSystemRegionType](../28/MiGetSystemRegionType_function_0028EC80.md) (function, `0x0028EC80`)
- `0x0031C016` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0031C082` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0031C09C` → [MiRequestIoPageMdlCacheRelease](../44/MiRequestIoPageMdlCacheRelease_function_00442AD0.md) (function, `0x00442AD0`)
- `0x0031C131` → [MiGetSystemRegionType](../28/MiGetSystemRegionType_function_0028EC80.md) (function, `0x0028EC80`)
- `0x0031C225` → [MiHyperPage](MiHyperPage_function_0031DCD4.md) (function, `0x0031DCD4`)
- `0x0031C2F0` → [MiGetBaseResidentPage](MiGetBaseResidentPage_function_0031C750.md) (function, `0x0031C750`)
- `0x0031C2FB` → [MiGetPfnPageSizeIndex](MiGetPfnPageSizeIndex_function_0031C710.md) (function, `0x0031C710`)
- `0x0031C4F9` → [MiGetPfnPageSizeIndexUnsynchronized](../46/MiGetPfnPageSizeIndexUnsynchronized_function_0046C008.md) (function, `0x0046C008`)

### Direct callers
- [MiTradePage](../28/MiTradePage_function_0028D160.md) at `0x0028D2FD`
- [MiPfnsWorthTrying](MiPfnsWorthTrying_function_0031B0C0.md) at `0x0031B270`
- [MiCheckContiguityTradeEligible](../68/MiCheckContiguityTradeEligible_function_00687300.md) at `0x00687352`

### Static image references
- `0x0031BB98` → RVA `0x00E30088` (`.data`; read)
- `0x0031BBB9` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0031BC9D` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x0031BD8C` → RVA `0x00E2DB68` (`.data`; read)
- `0x0031BD99` → RVA `0x00E2DB70` (`.data`; read)
- `0x0031BE11` → RVA `0x00EF526C` (`.data`; read/write)
- `0x0031BE2A` → RVA `0x00EF52D4` (`.data`; read/write)
- `0x0031BECC` → RVA `0x00E3738C` (`.data`; read)
- `0x0031BEF8` → RVA `0x00EF52D0` (`.data`; read/write)
- `0x0031BF03` → RVA `0x00EF540C` (`.data`; read/write)
- `0x0031BF5B` → RVA `0x00EF52F8` (`.data`; read/write)
- `0x0031BF8F` → RVA `0x00E2DBC9` (`.data`; reference)
- `0x0031BFA6` → RVA `0x00EF5468` (`.data`; read/write)
- `0x0031C071` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0031C0CA` → RVA `0x00EF5318` (`.data`; read/write)
- `0x0031C0E3` → RVA `0x00EF5448` (`.data`; read/write)
- `0x0031C0EE` → RVA `0x00FC6C38` (`ALMOSTRO`; read)
- `0x0031C0FE` → RVA `0x00FC6DE0` (`ALMOSTRO`; read)
- `0x0031C123` → RVA `0x00EF52DC` (`.data`; read/write)
- `0x0031C16C` → RVA `0x00EF5304` (`.data`; read/write)
- `0x0031C191` → RVA `0x00EF52A0` (`.data`; read/write)
- `0x0031C1AA` → RVA `0x00EF52B0` (`.data`; read/write)
- `0x0031C1E4` → RVA `0x00EF5424` (`.data`; read/write)
- `0x0031C202` → RVA `0x00EF52AC` (`.data`; read/write)
- `0x0031C217` → RVA `0x00EF5444` (`.data`; read/write)
- `0x0031C24C` → RVA `0x00EF5308` (`.data`; read/write)
- `0x0031C265` → RVA `0x00EF5300` (`.data`; read/write)
- `0x0031C287` → RVA `0x00EF52E0` (`.data`; read/write)
- `0x0031C292` → RVA `0x00EF52C8` (`.data`; read/write)
- `0x0031C2C3` → RVA `0x00EF52B8` (`.data`; read/write)
- `0x0031C2CE` → RVA `0x00EF544C` (`.data`; read/write)
- `0x0031C2D9` → RVA `0x00EF52CC` (`.data`; read/write)
- `0x0031C348` → RVA `0x00EF5250` (`.data`; read/write)
- `0x0031C361` → RVA `0x00EF52C4` (`.data`; read/write)
- `0x0031C37A` → RVA `0x00EF52F0` (`.data`; read/write)
- `0x0031C393` → RVA `0x00EF52F4` (`.data`; read/write)
- `0x0031C3AB` → RVA `0x00EF5458` (`.data`; read/write)
- `0x0031C3C9` → RVA `0x00EF5310` (`.data`; read/write)
- `0x0031C3E2` → RVA `0x00EF5314` (`.data`; read/write)
- `0x0031C3FB` → RVA `0x00EF52C0` (`.data`; read/write)
- `0x0031C439` → RVA `0x00EF530C` (`.data`; read/write)
- `0x0031C444` → RVA `0x00EF545C` (`.data`; read/write)
- `0x0031C462` → RVA `0x00EF52E4` (`.data`; read/write)
- `0x0031C495` → RVA `0x00EF52E8` (`.data`; read/write)
- `0x0031C4BB` → RVA `0x00EF52EC` (`.data`; read/write)
- `0x0031C4D4` → RVA `0x00EF52B4` (`.data`; read/write)
- `0x0031C503` → RVA `0x00EF52FC` (`.data`; read/write)
- `0x0031C52F` → RVA `0x00EF5390` (`.data`; read/write)
- `0x0031C53A` → RVA `0x00EF5440` (`.data`; read/write)
- `0x0031C545` → RVA `0x00EF5454` (`.data`; read/write)
- `0x0031C550` → RVA `0x00EF53C8` (`.data`; read/write)
- `0x0031C55B` → RVA `0x00EF53CC` (`.data`; read/write)
- `0x0031C566` → RVA `0x00EF53D4` (`.data`; read/write)
- `0x0031C571` → RVA `0x00EF53D0` (`.data`; read/write)
- `0x0031C57C` → RVA `0x00EF53D8` (`.data`; read/write)
- `0x0031C587` → RVA `0x00EF5460` (`.data`; read/write)
- `0x0031C592` → RVA `0x00EF5428` (`.data`; read/write)
- `0x0031C59D` → RVA `0x00EF53F0` (`.data`; read/write)
- `0x0031C5A8` → RVA `0x00EF53DC` (`.data`; read/write)
- `0x0031C5E4` → RVA `0x00EF543C` (`.data`; read/write)
- `0x0031C5FA` → RVA `0x00EF5414` (`.data`; read/write)
- `0x0031C605` → RVA `0x00EF53E4` (`.data`; read/write)
- `0x0031C610` → RVA `0x00EF53E8` (`.data`; read/write)
- `0x0031C61B` → RVA `0x00EF53EC` (`.data`; read/write)
- `0x0031C626` → RVA `0x00EF53E0` (`.data`; read/write)
- `0x0031C631` → RVA `0x00EF53F4` (`.data`; read/write)
- `0x0031C63C` → RVA `0x00EF5400` (`.data`; read/write)
- `0x0031C647` → RVA `0x00EF5410` (`.data`; read/write)
- `0x0031C652` → RVA `0x00EF5404` (`.data`; read/write)
- `0x0031C65D` → RVA `0x00EF5408` (`.data`; read/write)
- `0x0031C668` → RVA `0x00EF53FC` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x0031C5C6` → [sub_006E1438](../6E/Unknown_function_006E1438.md) (`tail-transfer`)
  - `0x0031C5CC` → [sub_006E1438 + 0xB](../6E/Unknown_function_006E1438.md) (`tail-transfer`)
  - `0x0031C5D9` → [sub_006E1438](../6E/Unknown_function_006E1438.md) (`tail-transfer`)
  - `0x0031C5DF` → [sub_006E1438 + 0xB](../6E/Unknown_function_006E1438.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0031BB00  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0031BB05  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0031BB0A  55                              push rbp
0031BB0B  56                              push rsi
0031BB0C  57                              push rdi
0031BB0D  41 54                           push r12
0031BB0F  41 55                           push r13
0031BB11  41 56                           push r14
0031BB13  41 57                           push r15
0031BB15  48 83 EC 30                     sub rsp, 0x30
0031BB19  45 8B D0                        mov r10d, r8d
0031BB1C  45 8B F1                        mov r14d, r9d
0031BB1F  41 83 E2 01                     and r10d, 1
0031BB23  45 8B F8                        mov r15d, r8d
0031BB26  44 89 94 24 80 00 00 00         mov dword ptr [rsp + 0x80], r10d
0031BB2E  48 8B DA                        mov rbx, rdx
0031BB31  4C 8B E1                        mov r12, rcx
0031BB34  BE 01 00 00 00                  mov esi, 1
0031BB39  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0031BB43  48 8B 7A 08                     mov rdi, qword ptr [rdx + 8]
0031BB47  4C 8B EA                        mov r13, rdx
0031BB4A  4C 2B E8                        sub r13, rax
0031BB4D  40 B5 11                        mov bpl, 0x11
0031BB50  49 C1 FD 04                     sar r13, 4
0031BB54  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
0031BB5E  4C 0F AF E8                     imul r13, rax
0031BB62  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
0031BB6C  48 0B F8                        or rdi, rax
0031BB6F  8B 42 20                        mov eax, dword ptr [rdx + 0x20]
0031BB72  C1 E8 18                        shr eax, 0x18
0031BB75  A8 08                           test al, 8
0031BB77  0F 85 86 02 00 00               jne 0x14031be03
0031BB7D  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
0031BB81  49 BB 00 00 00 00 00 01 00 00   movabs r11, 0x10000000000
0031BB8B  49 85 C3                        test r11, rax
0031BB8E  0F 85 50 07 00 00               jne 0x14031c2e4
0031BB94  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0031BB98  48 8B 0D E9 44 B1 00            mov rcx, qword ptr [rip + 0xb144e9]
0031BB9F  48 C1 E8 2B                     shr rax, 0x2b
0031BBA3  25 FF 03 00 00                  and eax, 0x3ff
0031BBA8  4C 39 24 C1                     cmp qword ptr [rcx + rax*8], r12
0031BBAC  0F 85 88 07 00 00               jne 0x14031c33a
0031BBB2  41 81 E6 00 00 41 00            and r14d, 0x410000
0031BBB9  4C 8D 05 40 44 CE FF            lea r8, [rip - 0x31bbc0]
0031BBC0  41 81 FE 00 00 41 00            cmp r14d, 0x410000
0031BBC7  74 0A                           je 0x14031bbd3
0031BBC9  41 F6 C7 02                     test r15b, 2
0031BBCD  0F 84 62 02 00 00               je 0x14031be35
0031BBD3  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0031BBD7  48 85 C0                        test rax, rax
0031BBDA  0F 88 9D 01 00 00               js 0x14031bd7d
0031BBE0  48 83 FF F8                     cmp rdi, -8
0031BBE4  0F 84 69 07 00 00               je 0x14031c353
0031BBEA  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
0031BBF4  48 3B F8                        cmp rdi, rax
0031BBF7  72 20                           jb 0x14031bc19
0031BBF9  48 8B C7                        mov rax, rdi
0031BBFC  48 C1 E8 27                     shr rax, 0x27
0031BC00  25 FF 01 00 00                  and eax, 0x1ff
0031BC05  2D 00 01 00 00                  sub eax, 0x100
0031BC0A  42 80 BC 00 A8 8A E3 00 04      cmp byte ptr [rax + r8 + 0xe38aa8], 4
0031BC13  0F 84 D1 02 00 00               je 0x14031beea
0031BC19  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0031BC1D  48 C1 E8 3C                     shr rax, 0x3c
0031BC21  24 07                           and al, 7
0031BC23  40 3A C6                        cmp al, sil
0031BC26  0F 84 F0 01 00 00               je 0x14031be1c
0031BC2C  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0031BC30  49 B9 FF FF FF FF FF 00 00 00   movabs r9, 0xffffffffff
0031BC3A  49 23 C1                        and rax, r9
0031BC3D  48 B9 FE FF FF FF 3F 00 00 00   movabs rcx, 0x3ffffffffe
0031BC47  48 3B C1                        cmp rax, rcx
0031BC4A  0F 84 CC 01 00 00               je 0x14031be1c
0031BC50  49 BF 00 00 00 00 80 F6 FF FF   movabs r15, 0xfffff68000000000
0031BC5A  49 8B C7                        mov rax, r15
0031BC5D  48 3B F8                        cmp rdi, rax
0031BC60  0F 82 DE 07 00 00               jb 0x14031c444
0031BC66  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
0031BC70  48 8B C0                        mov rax, rax
0031BC73  48 3B F8                        cmp rdi, rax
0031BC76  0F 87 C8 07 00 00               ja 0x14031c444
0031BC7C  4C 8B F7                        mov r14, rdi
0031BC7F  49 C1 E6 19                     shl r14, 0x19
0031BC83  49 8B C7                        mov rax, r15
0031BC86  48 C1 E0 19                     shl rax, 0x19
0031BC8A  4C 2B F0                        sub r14, rax
0031BC8D  48 8B 03                        mov rax, qword ptr [rbx]
0031BC90  49 C1 FE 10                     sar r14, 0x10
0031BC94  40 84 C6                        test sil, al
0031BC97  0F 84 EF 01 00 00               je 0x14031be8c
0031BC9D  48 8B 05 0C AE CA 00            mov rax, qword ptr [rip + 0xcaae0c]
0031BCA4  48 85 C0                        test rax, rax
0031BCA7  74 11                           je 0x14031bcba
0031BCA9  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
0031BCAD  48 C1 E8 0C                     shr rax, 0xc
0031BCB1  4C 3B E8                        cmp r13, rax
0031BCB4  0F 84 B2 06 00 00               je 0x14031c36c
0031BCBA  48 B9 00 00 00 40 FB F6 FF FF   movabs rcx, 0xfffff6fb40000000
0031BCC4  48 BA F8 FF FF 5F FB F6 FF FF   movabs rdx, 0xfffff6fb5ffffff8
0031BCCE  45 33 C0                        xor r8d, r8d
0031BCD1  49 BB F8 FF FF FF 7F 00 00 00   movabs r11, 0x7ffffffff8
0031BCDB  41 83 F8 03                     cmp r8d, 3
0031BCDF  73 28                           jae 0x14031bd09
0031BCE1  48 3B F9                        cmp rdi, rcx
0031BCE4  0F 83 31 02 00 00               jae 0x14031bf1b
0031BCEA  48 C1 E9 09                     shr rcx, 9
0031BCEE  49 23 CB                        and rcx, r11
0031BCF1  49 8B C7                        mov rax, r15
0031BCF4  48 C1 EA 09                     shr rdx, 9
0031BCF8  48 03 C8                        add rcx, rax
0031BCFB  49 23 D3                        and rdx, r11
0031BCFE  49 8B C7                        mov rax, r15
0031BD01  48 03 D0                        add rdx, rax
0031BD04  41 FF C0                        inc r8d
0031BD07  EB D2                           jmp 0x14031bcdb
0031BD09  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0031BD0D  49 23 C1                        and rax, r9
0031BD10  49 3B C5                        cmp rax, r13
0031BD13  0F 84 9C 04 00 00               je 0x14031c1b5
0031BD19  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0031BD1D  48 BF FF FF FF FF FF FF FF 3F   movabs rdi, 0x3fffffffffffffff
0031BD27  48 23 C7                        and rax, rdi
0031BD2A  48 3B C6                        cmp rax, rsi
0031BD2D  0F 87 FB 03 00 00               ja 0x14031c12e
0031BD33  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0031BD37  49 85 C1                        test r9, rax
0031BD3A  0F 84 94 06 00 00               je 0x14031c3d4
0031BD40  8B 53 20                        mov edx, dword ptr [rbx + 0x20]
0031BD43  66 3B D6                        cmp dx, si
0031BD46  0F 87 48 03 00 00               ja 0x14031c094
0031BD4C  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0031BD50  48 23 C7                        and rax, rdi
0031BD53  0F B7 D2                        movzx edx, dx
0031BD56  48 3B D0                        cmp rdx, rax
0031BD59  0F 87 35 03 00 00               ja 0x14031c094
0031BD5F  33 F6                           xor esi, esi
0031BD61  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
0031BD69  48 8B C6                        mov rax, rsi
0031BD6C  48 83 C4 30                     add rsp, 0x30
0031BD70  41 5F                           pop r15
0031BD72  41 5E                           pop r14
0031BD74  41 5D                           pop r13
0031BD76  41 5C                           pop r12
0031BD78  5F                              pop rdi
0031BD79  5E                              pop rsi
0031BD7A  5D                              pop rbp
0031BD7B  C3                              ret
0031BD7C  CC                              int3
0031BD7D  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0031BD81  48 0F BA E0 3E                  bt rax, 0x3e
0031BD86  0F 82 68 04 00 00               jb 0x14031c1f4
0031BD8C  48 3B 3D D5 1D B1 00            cmp rdi, qword ptr [rip + 0xb11dd5]
0031BD93  0F 84 5B 04 00 00               je 0x14031c1f4
0031BD99  48 3B 3D D0 1D B1 00            cmp rdi, qword ptr [rip + 0xb11dd0]
0031BDA0  0F 84 4E 04 00 00               je 0x14031c1f4
0031BDA6  45 85 D2                        test r10d, r10d
0031BDA9  0F 85 C8 03 00 00               jne 0x14031c177
0031BDAF  8B 4B 20                        mov ecx, dword ptr [rbx + 0x20]
0031BDB2  66 3B CE                        cmp cx, si
0031BDB5  0F 87 E1 03 00 00               ja 0x14031c19c
0031BDBB  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0031BDBF  48 BF FF FF FF FF FF FF FF 3F   movabs rdi, 0x3fffffffffffffff
0031BDC9  48 23 C7                        and rax, rdi
0031BDCC  0F B7 C9                        movzx ecx, cx
0031BDCF  48 3B C8                        cmp rcx, rax
0031BDD2  0F 87 C4 03 00 00               ja 0x14031c19c
0031BDD8  48 8B 03                        mov rax, qword ptr [rbx]
0031BDDB  40 84 C6                        test sil, al
0031BDDE  0F 84 E2 06 00 00               je 0x14031c4c6
0031BDE4  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0031BDE8  49 85 C3                        test r11, rax
0031BDEB  75 0D                           jne 0x14031bdfa
0031BDED  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0031BDF1  48 85 C0                        test rax, rax
0031BDF4  0F 89 A3 04 00 00               jns 0x14031c29d
0031BDFA  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0031BDFE  E9 5C FF FF FF                  jmp 0x14031bd5f
0031BE03  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031BE0B  0F 84 F2 00 00 00               je 0x14031bf03
0031BE11  FF 05 55 94 BD 00               inc dword ptr [rip + 0xbd9455]
0031BE17  E9 45 FF FF FF                  jmp 0x14031bd61
0031BE1C  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031BE24  0F 84 07 08 00 00               je 0x14031c631
0031BE2A  FF 05 A4 94 BD 00               inc dword ptr [rip + 0xbd94a4]
0031BE30  E9 2C FF FF FF                  jmp 0x14031bd61
0031BE35  41 80 BC 24 E6 3E 00 00 00      cmp byte ptr [r12 + 0x3ee6], 0
0031BE3E  0F 84 8F FD FF FF               je 0x14031bbd3
0031BE44  45 33 C9                        xor r9d, r9d
0031BE47  41 83 F9 02                     cmp r9d, 2
0031BE4B  0F 83 BD 00 00 00               jae 0x14031bf0e
0031BE51  41 8B C1                        mov eax, r9d
0031BE54  48 03 C0                        add rax, rax
0031BE57  49 83 BC C4 C8 3F 00 00 00      cmp qword ptr [r12 + rax*8 + 0x3fc8], 0
0031BE60  74 25                           je 0x14031be87
0031BE62  49 8B 84 C4 D0 3F 00 00         mov rax, qword ptr [r12 + rax*8 + 0x3fd0]
0031BE6A  49 8B D5                        mov rdx, r13
0031BE6D  43 8B 8C 88 E8 35 01 00         mov ecx, dword ptr [r8 + r9*4 + 0x135e8]
0031BE75  48 D3 EA                        shr rdx, cl
0031BE78  48 0F A3 10                     bt qword ptr [rax], rdx
0031BE7C  0F 92 C0                        setb al
0031BE7F  84 C0                           test al, al
0031BE81  0F 85 19 06 00 00               jne 0x14031c4a0
0031BE87  41 FF C1                        inc r9d
0031BE8A  EB BB                           jmp 0x14031be47
0031BE8C  48 8B CB                        mov rcx, rbx
0031BE8F  E8 40 1E 00 00                  call 0x14031dcd4
0031BE94  85 C0                           test eax, eax
0031BE96  0F 85 6A 05 00 00               jne 0x14031c406
0031BE9C  45 8B 8C 24 58 48 00 00         mov r9d, dword ptr [r12 + 0x4858]
0031BEA4  33 D2                           xor edx, edx
0031BEA6  41 3B D1                        cmp edx, r9d
0031BEA9  0F 83 B7 00 00 00               jae 0x14031bf66
0031BEAF  4D 8B 84 D4 60 48 00 00         mov r8, qword ptr [r12 + rdx*8 + 0x4860]
0031BEB7  49 8B 80 B8 00 00 00            mov rax, qword ptr [r8 + 0xb8]
0031BEBE  48 85 C0                        test rax, rax
0031BEC1  74 23                           je 0x14031bee6
0031BEC3  4C 3B F0                        cmp r14, rax
0031BEC6  72 1E                           jb 0x14031bee6
0031BEC8  41 8B 48 04                     mov ecx, dword ptr [r8 + 4]
0031BECC  8B 05 BA B4 B1 00               mov eax, dword ptr [rip + 0xb1b4ba]
0031BED2  48 0F AF C8                     imul rcx, rax
0031BED6  49 03 88 B8 00 00 00            add rcx, qword ptr [r8 + 0xb8]
0031BEDD  4C 3B F1                        cmp r14, rcx
0031BEE0  0F 82 79 FE FF FF               jb 0x14031bd5f
0031BEE6  FF C2                           inc edx
0031BEE8  EB BC                           jmp 0x14031bea6
0031BEEA  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031BEF2  0F 84 4D 06 00 00               je 0x14031c545
0031BEF8  FF 05 D2 93 BD 00               inc dword ptr [rip + 0xbd93d2]
0031BEFE  E9 5E FE FF FF                  jmp 0x14031bd61
0031BF03  FF 05 03 95 BD 00               inc dword ptr [rip + 0xbd9503]
0031BF09  E9 53 FE FF FF                  jmp 0x14031bd61
0031BF0E  44 8B 94 24 80 00 00 00         mov r10d, dword ptr [rsp + 0x80]
0031BF16  E9 B8 FC FF FF                  jmp 0x14031bbd3
0031BF1B  48 3B FA                        cmp rdi, rdx
0031BF1E  0F 87 C6 FD FF FF               ja 0x14031bcea
0031BF24  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0031BF27  66 3B C6                        cmp ax, si
0031BF2A  0F 87 55 04 00 00               ja 0x14031c385
0031BF30  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0031BF34  48 BF FF FF FF FF FF FF FF 3F   movabs rdi, 0x3fffffffffffffff
0031BF3E  48 23 C7                        and rax, rdi
0031BF41  48 3D 00 00 01 00               cmp rax, 0x10000
0031BF47  0F 82 12 FE FF FF               jb 0x14031bd5f
0031BF4D  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031BF55  0F 84 0B 06 00 00               je 0x14031c566
0031BF5B  FF 05 97 93 BD 00               inc dword ptr [rip + 0xbd9397]
0031BF61  E9 FB FD FF FF                  jmp 0x14031bd61
0031BF66  49 8B CE                        mov rcx, r14
0031BF69  E8 12 2D F7 FF                  call 0x14028ec80
0031BF6E  8B C8                           mov ecx, eax
0031BF70  83 F8 04                        cmp eax, 4
0031BF73  0F 85 75 01 00 00               jne 0x14031c0ee
0031BF79  F6 43 23 10                     test byte ptr [rbx + 0x23], 0x10
0031BF7D  0F 85 3B 06 00 00               jne 0x14031c5be
0031BF83  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0031BF86  66 3B C6                        cmp ax, si
0031BF89  0F 87 42 06 00 00               ja 0x14031c5d1
0031BF8F  40 84 35 33 1C B1 00            test byte ptr [rip + 0xb11c33], sil
0031BF96  0F 84 51 04 00 00               je 0x14031c3ed
0031BF9C  83 BC 24 80 00 00 00 00         cmp dword ptr [rsp + 0x80], 0
0031BFA4  75 6D                           jne 0x14031c013
0031BFA6  FF 05 BC 94 BD 00               inc dword ptr [rip + 0xbd94bc]
0031BFAC  49 8B CD                        mov rcx, r13
0031BFAF  E8 6C 56 00 00                  call 0x140321620
0031BFB4  0F B6 E8                        movzx ebp, al
0031BFB7  3C 11                           cmp al, 0x11
0031BFB9  0F 84 30 06 00 00               je 0x14031c5ef
0031BFBF  0F B6 43 22                     movzx eax, byte ptr [rbx + 0x22]
0031BFC3  24 07                           and al, 7
0031BFC5  3C 06                           cmp al, 6
0031BFC7  0F 85 01 03 00 00               jne 0x14031c2ce
0031BFCD  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0031BFD0  66 3B C6                        cmp ax, si
0031BFD3  0F 87 F5 02 00 00               ja 0x14031c2ce
0031BFD9  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0031BFDD  48 0F BA E0 28                  bt rax, 0x28
0031BFE2  0F 82 E6 02 00 00               jb 0x14031c2ce
0031BFE8  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0031BFEC  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
0031BFF6  48 0B C1                        or rax, rcx
0031BFF9  48 3B C7                        cmp rax, rdi
0031BFFC  0F 85 CC 02 00 00               jne 0x14031c2ce
0031C002  49 8B CE                        mov rcx, r14
0031C005  E8 76 2C F7 FF                  call 0x14028ec80
0031C00A  83 F8 04                        cmp eax, 4
0031C00D  0F 85 BB 02 00 00               jne 0x14031c2ce
0031C013  48 8B CF                        mov rcx, rdi
0031C016  E8 85 68 F6 FF                  call 0x1402828a0
0031C01B  40 84 C6                        test sil, al
0031C01E  0F 84 E9 01 00 00               je 0x14031c20d
0031C024  48 8B C8                        mov rcx, rax
0031C027  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
0031C031  48 C1 E9 0C                     shr rcx, 0xc
0031C035  48 23 CA                        and rcx, rdx
0031C038  4C 3B E9                        cmp r13, rcx
0031C03B  0F 85 CC 01 00 00               jne 0x14031c20d
0031C041  48 0F BA E0 09                  bt rax, 9
0031C046  0F 82 89 00 00 00               jb 0x14031c0d5
0031C04C  33 F6                           xor esi, esi
0031C04E  40 80 FD 11                     cmp bpl, 0x11
0031C052  0F 84 09 FD FF FF               je 0x14031bd61
0031C058  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0031C062  F0 48 21 43 18                  lock and qword ptr [rbx + 0x18], rax
0031C067  40 80 FD 02                     cmp bpl, 2
0031C06B  0F 83 F0 FC FF FF               jae 0x14031bd61
0031C071  83 3D A8 AC CA 00 00            cmp dword ptr [rip + 0xcaaca8], 0
0031C078  74 0D                           je 0x14031c087
0031C07A  44 0F 20 C1                     mov rcx, cr8
0031C07E  40 0F B6 D5                     movzx edx, bpl
0031C082  E8 11 96 1D 00                  call 0x1404f5698
0031C087  40 0F B6 C5                     movzx eax, bpl
0031C08B  44 0F 22 C0                     mov cr8, rax
0031C08F  E9 CD FC FF FF                  jmp 0x14031bd61
0031C094  45 85 D2                        test r10d, r10d
0031C097  75 08                           jne 0x14031c0a1
0031C099  49 8B CD                        mov rcx, r13
0031C09C  E8 2F 6A 12 00                  call 0x140442ad0
0031C0A1  8B 4B 20                        mov ecx, dword ptr [rbx + 0x20]
0031C0A4  66 3B CE                        cmp cx, si
0031C0A7  77 13                           ja 0x14031c0bc
0031C0A9  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0031C0AD  48 23 C7                        and rax, rdi
0031C0B0  0F B7 C9                        movzx ecx, cx
0031C0B3  48 3B C8                        cmp rcx, rax
0031C0B6  0F 86 A3 FC FF FF               jbe 0x14031bd5f
0031C0BC  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C0C4  0F 84 DE 04 00 00               je 0x14031c5a8
0031C0CA  FF 05 48 92 BD 00               inc dword ptr [rip + 0xbd9248]
0031C0D0  E9 8C FC FF FF                  jmp 0x14031bd61
0031C0D5  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C0DD  0F 85 F6 01 00 00               jne 0x14031c2d9
0031C0E3  FF 05 5F 93 BD 00               inc dword ptr [rip + 0xbd935f]
0031C0E9  E9 60 FF FF FF                  jmp 0x14031c04e
0031C0EE  48 8B 15 43 AB CA 00            mov rdx, qword ptr [rip + 0xcaab43]
0031C0F5  4C 3B F2                        cmp r14, rdx
0031C0F8  0F 82 72 01 00 00               jb 0x14031c270
0031C0FE  48 8B 05 DB AC CA 00            mov rax, qword ptr [rip + 0xcaacdb]
0031C105  48 C1 E0 0C                     shl rax, 0xc
0031C109  48 03 C2                        add rax, rdx
0031C10C  4C 3B F0                        cmp r14, rax
0031C10F  0F 87 5B 01 00 00               ja 0x14031c270
0031C115  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C11D  0F 84 D7 04 00 00               je 0x14031c5fa
0031C123  FF 05 B3 91 BD 00               inc dword ptr [rip + 0xbd91b3]
0031C129  E9 33 FC FF FF                  jmp 0x14031bd61
0031C12E  49 8B CE                        mov rcx, r14
0031C131  E8 4A 2B F7 FF                  call 0x14028ec80
0031C136  83 F8 05                        cmp eax, 5
0031C139  0F 85 E3 00 00 00               jne 0x14031c222
0031C13F  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0031C142  66 3B C6                        cmp ax, si
0031C145  0F 87 0C 01 00 00               ja 0x14031c257
0031C14B  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0031C14F  48 23 C7                        and rax, rdi
0031C152  48 3D 00 00 01 00               cmp rax, 0x10000
0031C158  0F 82 01 FC FF FF               jb 0x14031bd5f
0031C15E  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C166  0F 84 10 04 00 00               je 0x14031c57c
0031C16C  FF 05 92 91 BD 00               inc dword ptr [rip + 0xbd9192]
0031C172  E9 EA FB FF FF                  jmp 0x14031bd61
0031C177  48 0F BA 63 28 35               bt qword ptr [rbx + 0x28], 0x35
0031C17D  0F 83 2C FC FF FF               jae 0x14031bdaf
0031C183  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C18B  0F 84 AB 04 00 00               je 0x14031c63c
0031C191  FF 05 09 91 BD 00               inc dword ptr [rip + 0xbd9109]
0031C197  E9 C5 FB FF FF                  jmp 0x14031bd61
0031C19C  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C1A4  0F 84 B3 04 00 00               je 0x14031c65d
0031C1AA  FF 05 00 91 BD 00               inc dword ptr [rip + 0xbd9100]
0031C1B0  E9 AC FB FF FF                  jmp 0x14031bd61
0031C1B5  33 F6                           xor esi, esi
0031C1B7  48 B8 68 DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedf68
0031C1C1  48 3B F8                        cmp rdi, rax
0031C1C4  0F 85 D4 01 00 00               jne 0x14031c39e
0031C1CA  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0031C1CD  66 83 F8 01                     cmp ax, 1
0031C1D1  0F 86 8A FB FF FF               jbe 0x14031bd61
0031C1D7  39 B4 24 90 00 00 00            cmp dword ptr [rsp + 0x90], esi
0031C1DE  0F 85 2A 03 00 00               jne 0x14031c50e
0031C1E4  FF 05 3A 92 BD 00               inc dword ptr [rip + 0xbd923a]
0031C1EA  BE 01 00 00 00                  mov esi, 1
0031C1EF  E9 6D FB FF FF                  jmp 0x14031bd61
0031C1F4  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C1FC  0F 84 66 04 00 00               je 0x14031c668
0031C202  FF 05 A4 90 BD 00               inc dword ptr [rip + 0xbd90a4]
0031C208  E9 54 FB FF FF                  jmp 0x14031bd61
0031C20D  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C215  75 7B                           jne 0x14031c292
0031C217  FF 05 27 92 BD 00               inc dword ptr [rip + 0xbd9227]
0031C21D  E9 2C FE FF FF                  jmp 0x14031c04e
0031C222  48 8B CB                        mov rcx, rbx
0031C225  E8 AA 1A 00 00                  call 0x14031dcd4
0031C22A  85 C0                           test eax, eax
0031C22C  0F 84 89 01 00 00               je 0x14031c3bb
0031C232  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
0031C235  66 3B C6                        cmp ax, si
0031C238  0F 86 21 FB FF FF               jbe 0x14031bd5f
0031C23E  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C246  0F 84 3B 03 00 00               je 0x14031c587
0031C24C  FF 05 B6 90 BD 00               inc dword ptr [rip + 0xbd90b6]
0031C252  E9 0A FB FF FF                  jmp 0x14031bd61
0031C257  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C25F  0F 84 0C 03 00 00               je 0x14031c571
0031C265  FF 05 95 90 BD 00               inc dword ptr [rip + 0xbd9095]
0031C26B  E9 F1 FA FF FF                  jmp 0x14031bd61
0031C270  83 F9 0B                        cmp ecx, 0xb
0031C273  0F 85 D6 01 00 00               jne 0x14031c44f
0031C279  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C281  0F 84 7E 03 00 00               je 0x14031c605
0031C287  FF 05 53 90 BD 00               inc dword ptr [rip + 0xbd9053]
0031C28D  E9 CF FA FF FF                  jmp 0x14031bd61
0031C292  FF 05 30 90 BD 00               inc dword ptr [rip + 0xbd9030]
0031C298  E9 B1 FD FF FF                  jmp 0x14031c04e
0031C29D  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0031C2A1  48 85 C0                        test rax, rax
0031C2A4  0F 84 50 FB FF FF               je 0x14031bdfa
0031C2AA  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
0031C2B2  83 08 02                        or dword ptr [rax], 2
0031C2B5  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C2BD  0F 84 84 03 00 00               je 0x14031c647
0031C2C3  FF 05 EF 8F BD 00               inc dword ptr [rip + 0xbd8fef]
0031C2C9  E9 93 FA FF FF                  jmp 0x14031bd61
0031C2CE  FF 05 78 91 BD 00               inc dword ptr [rip + 0xbd9178]
0031C2D4  E9 7F FD FF FF                  jmp 0x14031c058
0031C2D9  FF 05 ED 8F BD 00               inc dword ptr [rip + 0xbd8fed]
0031C2DF  E9 6A FD FF FF                  jmp 0x14031c04e
0031C2E4  48 8B CB                        mov rcx, rbx
0031C2E7  45 85 D2                        test r10d, r10d
0031C2EA  0F 84 EF 01 00 00               je 0x14031c4df
0031C2F0  E8 5B 04 00 00                  call 0x14031c750
0031C2F5  48 8B C8                        mov rcx, rax
0031C2F8  4C 8B E0                        mov r12, rax
0031C2FB  E8 10 04 00 00                  call 0x14031c710
0031C300  4C 3B E3                        cmp r12, rbx
0031C303  74 10                           je 0x14031c315
0031C305  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
0031C30F  F0 49 21 4C 24 18               lock and qword ptr [r12 + 0x18], rcx
0031C315  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
0031C31A  83 F8 03                        cmp eax, 3
0031C31D  0F 85 F6 01 00 00               jne 0x14031c519
0031C323  44 8B 94 24 80 00 00 00         mov r10d, dword ptr [rsp + 0x80]
0031C32B  49 BB 00 00 00 00 00 01 00 00   movabs r11, 0x10000000000
0031C335  E9 5A F8 FF FF                  jmp 0x14031bb94
0031C33A  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C342  0F 84 E7 01 00 00               je 0x14031c52f
0031C348  FF 05 02 8F BD 00               inc dword ptr [rip + 0xbd8f02]
0031C34E  E9 0E FA FF FF                  jmp 0x14031bd61
0031C353  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C35B  0F 84 D9 01 00 00               je 0x14031c53a
0031C361  FF 05 5D 8F BD 00               inc dword ptr [rip + 0xbd8f5d]
0031C367  E9 F5 F9 FF FF                  jmp 0x14031bd61
0031C36C  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C374  0F 84 D6 01 00 00               je 0x14031c550
0031C37A  FF 05 70 8F BD 00               inc dword ptr [rip + 0xbd8f70]
0031C380  E9 DC F9 FF FF                  jmp 0x14031bd61
0031C385  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C38D  0F 84 C8 01 00 00               je 0x14031c55b
0031C393  FF 05 5B 8F BD 00               inc dword ptr [rip + 0xbd8f5b]
0031C399  E9 C3 F9 FF FF                  jmp 0x14031bd61
0031C39E  39 B4 24 90 00 00 00            cmp dword ptr [rsp + 0x90], esi
0031C3A5  0F 85 58 01 00 00               jne 0x14031c503
0031C3AB  FF 05 A7 90 BD 00               inc dword ptr [rip + 0xbd90a7]
0031C3B1  BE 01 00 00 00                  mov esi, 1
0031C3B6  E9 A6 F9 FF FF                  jmp 0x14031bd61
0031C3BB  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C3C3  0F 84 C9 01 00 00               je 0x14031c592
0031C3C9  FF 05 41 8F BD 00               inc dword ptr [rip + 0xbd8f41]
0031C3CF  E9 8D F9 FF FF                  jmp 0x14031bd61
0031C3D4  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C3DC  0F 84 BB 01 00 00               je 0x14031c59d
0031C3E2  FF 05 2C 8F BD 00               inc dword ptr [rip + 0xbd8f2c]
0031C3E8  E9 74 F9 FF FF                  jmp 0x14031bd61
0031C3ED  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C3F5  0F 84 E9 01 00 00               je 0x14031c5e4
0031C3FB  FF 05 BF 8E BD 00               inc dword ptr [rip + 0xbd8ebf]
0031C401  E9 5B F9 FF FF                  jmp 0x14031bd61
0031C406  8B 4B 20                        mov ecx, dword ptr [rbx + 0x20]
0031C409  66 3B CE                        cmp cx, si
0031C40C  77 1D                           ja 0x14031c42b
0031C40E  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0031C412  48 BF FF FF FF FF FF FF FF 3F   movabs rdi, 0x3fffffffffffffff
0031C41C  48 23 C7                        and rax, rdi
0031C41F  0F B7 C9                        movzx ecx, cx
0031C422  48 3B C8                        cmp rcx, rax
0031C425  0F 86 34 F9 FF FF               jbe 0x14031bd5f
0031C42B  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C433  0F 84 7A 01 00 00               je 0x14031c5b3
0031C439  FF 05 CD 8E BD 00               inc dword ptr [rip + 0xbd8ecd]
0031C43F  E9 1D F9 FF FF                  jmp 0x14031bd61
0031C444  FF 05 12 90 BD 00               inc dword ptr [rip + 0xbd9012]
0031C44A  E9 12 F9 FF FF                  jmp 0x14031bd61
0031C44F  83 F9 08                        cmp ecx, 8
0031C452  75 19                           jne 0x14031c46d
0031C454  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C45C  0F 84 AE 01 00 00               je 0x14031c610
0031C462  FF 05 7C 8E BD 00               inc dword ptr [rip + 0xbd8e7c]
0031C468  E9 F4 F8 FF FF                  jmp 0x14031bd61
0031C46D  49 8B C7                        mov rax, r15
0031C470  4C 3B F0                        cmp r14, rax
0031C473  72 38                           jb 0x14031c4ad
0031C475  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
0031C47F  48 8B C0                        mov rax, rax
0031C482  4C 3B F0                        cmp r14, rax
0031C485  77 26                           ja 0x14031c4ad
0031C487  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C48F  0F 84 86 01 00 00               je 0x14031c61b
0031C495  FF 05 4D 8E BD 00               inc dword ptr [rip + 0xbd8e4d]
0031C49B  E9 C1 F8 FF FF                  jmp 0x14031bd61
0031C4A0  4B 8B B4 C8 60 1C 01 00         mov rsi, qword ptr [r8 + r9*8 + 0x11c60]
0031C4A8  E9 B4 F8 FF FF                  jmp 0x14031bd61
0031C4AD  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C4B5  0F 84 6B 01 00 00               je 0x14031c626
0031C4BB  FF 05 2B 8E BD 00               inc dword ptr [rip + 0xbd8e2b]
0031C4C1  E9 9B F8 FF FF                  jmp 0x14031bd61
0031C4C6  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C4CE  0F 84 7E 01 00 00               je 0x14031c652
0031C4D4  FF 05 DA 8D BD 00               inc dword ptr [rip + 0xbd8dda]
0031C4DA  E9 82 F8 FF FF                  jmp 0x14031bd61
0031C4DF  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
0031C4E4  C7 44 24 20 00 00 00 00         mov dword ptr [rsp + 0x20], 0
0031C4EC  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
0031C4F1  C7 44 24 78 00 00 00 00         mov dword ptr [rsp + 0x78], 0
0031C4F9  E8 0A FB 14 00                  call 0x14046c008
0031C4FE  E9 17 FE FF FF                  jmp 0x14031c31a
0031C503  FF 05 F3 8D BD 00               inc dword ptr [rip + 0xbd8df3]
0031C509  E9 A3 FE FF FF                  jmp 0x14031c3b1
0031C50E  FF 05 F8 8D BD 00               inc dword ptr [rip + 0xbd8df8]
0031C514  E9 D1 FC FF FF                  jmp 0x14031c1ea
0031C519  8B C0                           mov eax, eax
0031C51B  4C 8D 05 DE 3A CE FF            lea r8, [rip - 0x31c522]
0031C522  49 8B B4 C0 60 1C 01 00         mov rsi, qword ptr [r8 + rax*8 + 0x11c60]
0031C52A  E9 32 F8 FF FF                  jmp 0x14031bd61
0031C52F  FF 05 5B 8E BD 00               inc dword ptr [rip + 0xbd8e5b]
0031C535  E9 27 F8 FF FF                  jmp 0x14031bd61
0031C53A  FF 05 00 8F BD 00               inc dword ptr [rip + 0xbd8f00]
0031C540  E9 1C F8 FF FF                  jmp 0x14031bd61
0031C545  FF 05 09 8F BD 00               inc dword ptr [rip + 0xbd8f09]
0031C54B  E9 11 F8 FF FF                  jmp 0x14031bd61
0031C550  FF 05 72 8E BD 00               inc dword ptr [rip + 0xbd8e72]
0031C556  E9 06 F8 FF FF                  jmp 0x14031bd61
0031C55B  FF 05 6B 8E BD 00               inc dword ptr [rip + 0xbd8e6b]
0031C561  E9 FB F7 FF FF                  jmp 0x14031bd61
0031C566  FF 05 68 8E BD 00               inc dword ptr [rip + 0xbd8e68]
0031C56C  E9 F0 F7 FF FF                  jmp 0x14031bd61
0031C571  FF 05 59 8E BD 00               inc dword ptr [rip + 0xbd8e59]
0031C577  E9 E5 F7 FF FF                  jmp 0x14031bd61
0031C57C  FF 05 56 8E BD 00               inc dword ptr [rip + 0xbd8e56]
0031C582  E9 DA F7 FF FF                  jmp 0x14031bd61
0031C587  FF 05 D3 8E BD 00               inc dword ptr [rip + 0xbd8ed3]
0031C58D  E9 CF F7 FF FF                  jmp 0x14031bd61
0031C592  FF 05 90 8E BD 00               inc dword ptr [rip + 0xbd8e90]
0031C598  E9 C4 F7 FF FF                  jmp 0x14031bd61
0031C59D  FF 05 4D 8E BD 00               inc dword ptr [rip + 0xbd8e4d]
0031C5A3  E9 B9 F7 FF FF                  jmp 0x14031bd61
0031C5A8  FF 05 2E 8E BD 00               inc dword ptr [rip + 0xbd8e2e]
0031C5AE  E9 AE F7 FF FF                  jmp 0x14031bd61
0031C5B3  FF 05 6B 8E BD 00               inc dword ptr [rip + 0xbd8e6b]
0031C5B9  E9 A3 F7 FF FF                  jmp 0x14031bd61
0031C5BE  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C5C6  0F 84 6C 4E 3C 00               je 0x1406e1438
0031C5CC  E9 72 4E 3C 00                  jmp 0x1406e1443
0031C5D1  83 BC 24 90 00 00 00 00         cmp dword ptr [rsp + 0x90], 0
0031C5D9  0F 84 59 4E 3C 00               je 0x1406e1438
0031C5DF  E9 5F 4E 3C 00                  jmp 0x1406e1443
0031C5E4  FF 05 52 8E BD 00               inc dword ptr [rip + 0xbd8e52]
0031C5EA  E9 72 F7 FF FF                  jmp 0x14031bd61
0031C5EF  FF 05 57 8E BD 00               inc dword ptr [rip + 0xbd8e57]
0031C5F5  E9 67 F7 FF FF                  jmp 0x14031bd61
0031C5FA  FF 05 14 8E BD 00               inc dword ptr [rip + 0xbd8e14]
0031C600  E9 5C F7 FF FF                  jmp 0x14031bd61
0031C605  FF 05 D9 8D BD 00               inc dword ptr [rip + 0xbd8dd9]
0031C60B  E9 51 F7 FF FF                  jmp 0x14031bd61
0031C610  FF 05 D2 8D BD 00               inc dword ptr [rip + 0xbd8dd2]
0031C616  E9 46 F7 FF FF                  jmp 0x14031bd61
0031C61B  FF 05 CB 8D BD 00               inc dword ptr [rip + 0xbd8dcb]
0031C621  E9 3B F7 FF FF                  jmp 0x14031bd61
0031C626  FF 05 B4 8D BD 00               inc dword ptr [rip + 0xbd8db4]
0031C62C  E9 30 F7 FF FF                  jmp 0x14031bd61
0031C631  FF 05 BD 8D BD 00               inc dword ptr [rip + 0xbd8dbd]
0031C637  E9 25 F7 FF FF                  jmp 0x14031bd61
0031C63C  FF 05 BE 8D BD 00               inc dword ptr [rip + 0xbd8dbe]
0031C642  E9 1A F7 FF FF                  jmp 0x14031bd61
0031C647  FF 05 C3 8D BD 00               inc dword ptr [rip + 0xbd8dc3]
0031C64D  E9 0F F7 FF FF                  jmp 0x14031bd61
0031C652  FF 05 AC 8D BD 00               inc dword ptr [rip + 0xbd8dac]
0031C658  E9 04 F7 FF FF                  jmp 0x14031bd61
0031C65D  FF 05 A5 8D BD 00               inc dword ptr [rip + 0xbd8da5]
0031C663  E9 F9 F6 FF FF                  jmp 0x14031bd61
0031C668  FF 05 8E 8D BD 00               inc dword ptr [rip + 0xbd8d8e]
0031C66E  E9 EE F6 FF FF                  jmp 0x14031bd61
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiActivePageClaimCandidate(__int64 a1, __int64 a2, int a3, int a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned int v_stack_p80;

    v_stack_p20 = v_rbx;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (48);
    v_r10 = (unsigned int)(((unsigned int)(a3)) & (1));
    v_stack_p18 = (unsigned int)(v_r10);
    v_r13 = (a2) - (result);
    v_r13 = (v_r13) >> (4);
    v_r13 = (v_r13) * (result);
    v_rdi = (*(unsigned __int64 *)(a2 + 8)) | (result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (8)) != 0) goto loc_0031BE03;
    if (((v_r11) & (*(unsigned __int64 *)(a2 + 40))) != 0) goto loc_0031C2E4;
loc_0031BB94:
    result = (*(unsigned __int64 *)(a2 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11617513) + result * 8)) != a1) goto loc_0031C33A;
    v_r14 = (unsigned int)(((unsigned int)(a4)) & (0x410000ULL));
    if (((unsigned int)(v_r14)) == 0x410000ULL) goto loc_0031BBD3;
    if ((((unsigned __int8)((unsigned int)(a3))) & (2)) == 0) goto loc_0031BE35;
loc_0031BBD3:
    if (sign_flag) goto loc_0031BD7D;
    if (v_rdi == -8) goto loc_0031C353;
    if (v_rdi < (*(unsigned __int64 *)(a2 + 40))) goto loc_0031BC19;
    result = (v_rdi) >> (39);
    result = (unsigned int)((result) & (511));
    result = (unsigned int)((result) - (256));
    if ((*(unsigned __int8 *)(result + v_rip - 3259328 * 1 + 14912168)) == 4) goto loc_0031BEEA;
loc_0031BC19:
    result = (*(unsigned __int64 *)(a2 + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) == 1) goto loc_0031BE1C;
    result = (*(unsigned __int64 *)(a2 + 40)) & (a4);
    if (result == (*(unsigned __int64 *)(v_rip + 11617513))) goto loc_0031BE1C;
    if (v_rdi < ((unsigned int)(a3))) goto loc_0031C444;
    if (v_rdi > ((unsigned int)(a3))) goto loc_0031C444;
    v_r14 = (v_rdi) << (25);
    result = ((unsigned int)(a3)) << (25);
    v_r14 = (v_r14) - (result);
    v_r14 = (v_r14) >> (16);
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(a2)))) == 0) goto loc_0031BE8C;
    if (*(unsigned __int64 *)(v_rip + 13282828) == 0) goto loc_0031BCBA;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13282828) + 40)) >> (12);
    if (v_r13 == result) goto loc_0031C36C;
loc_0031BCBA:
    a3 = 0;
loc_0031BCDB:
    if (0 >= 3) goto loc_0031BD09;
    if (v_rdi >= (*(unsigned __int64 *)(v_rip + 11617513))) goto loc_0031BF1B;
loc_0031BCEA:
    a1 = (*(unsigned __int64 *)(v_rip + 11617513)) >> (9);
    a1 = (a1) & (v_r11);
    a2 = (a2) >> (9);
    a1 = (a1) + ((unsigned int)(a3));
    a2 = (a2) & (v_r11);
    a2 = (a2) + ((unsigned int)(a3));
    a3 = (unsigned int)((a3) + 1);
    goto loc_0031BCDB;
loc_0031BD09:
    result = (*(unsigned __int64 *)(a2 + 40)) & (a4);
    if (result == v_r13) goto loc_0031C1B5;
    result = (*(unsigned __int64 *)(a2 + 24)) & (v_rdi);
    if (result > 1) goto loc_0031C12E;
    if (((a4) & (*(unsigned __int64 *)(a2 + 24))) == 0) goto loc_0031C3D4;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(a2 + 32)))) > 1) goto loc_0031C094;
    result = (*(unsigned __int64 *)(a2 + 24)) & (v_rdi);
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(a2 + 32)))) > result) goto loc_0031C094;
loc_0031BD5F:
    v_rsi = 0;
loc_0031BD61:
    v_rsp = (v_rsp) + (48);
    return 0;
loc_0031BD7D:
    if (condition_is_below) goto loc_0031C1F4;
    if (v_rdi == (*(unsigned __int64 *)(v_rip + 11607509))) goto loc_0031C1F4;
    if (v_rdi == (*(unsigned __int64 *)(v_rip + 11607504))) goto loc_0031C1F4;
    if ((unsigned int)(v_r10) != 0) goto loc_0031C177;
loc_0031BDAF:
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p20 + 32)))) > 0) goto loc_0031C19C;
    result = (*(unsigned __int64 *)(v_stack_p20 + 24)) & (v_rdi);
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p20 + 32)))) > result) goto loc_0031C19C;
    if (((0) & ((unsigned __int8)(*(unsigned __int64 *)(v_stack_p20)))) == 0) goto loc_0031C4C6;
    if (((v_r11) & (*(unsigned __int64 *)(v_stack_p20 + 40))) != 0) goto loc_0031BDFA;
    if (!sign_flag) goto loc_0031C29D;
loc_0031BDFA:
    goto loc_0031BD5F;
loc_0031BE03:
    if (a5 == 0) goto loc_0031BF03;
    goto loc_0031BD61;
loc_0031BE1C:
    if (a5 == 0) goto loc_0031C631;
    goto loc_0031BD61;
loc_0031BE35:
    if ((*(unsigned __int8 *)(a1 + 16102)) == 0) goto loc_0031BBD3;
    a4 = 0;
loc_0031BE47:
    if (0 >= 2) goto loc_0031BF0E;
    result = (0) + (0);
    if ((*(unsigned __int64 *)(a1 + result * 8 + 16328)) == 0) goto loc_0031BE87;
    a2 = (v_r13) >> ((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + a4 * 4 + 79336))));
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) goto loc_0031C4A0;
loc_0031BE87:
    a4 = (unsigned int)((a4) + 1);
    goto loc_0031BE47;
loc_0031BE8C:
    result = MiHyperPage(v_stack_p20, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_0031C406;
    a2 = 0;
loc_0031BEA6:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 18520))))) goto loc_0031BF66;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + a2 * 8 + 18528) + 184) == 0) goto loc_0031BEE6;
    if (v_r14 < (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + a2 * 8 + 18528) + 184))) goto loc_0031BEE6;
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + a2 * 8 + 18528) + 4))) * ((unsigned int)(*(unsigned int *)(v_rip + 11646138)));
    a1 = (a1) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + a2 * 8 + 18528) + 184));
    if (v_r14 < a1) goto loc_0031BD5F;
loc_0031BEE6:
    a2 = (unsigned int)((a2) + 1);
    goto loc_0031BEA6;
loc_0031BEEA:
    if (a5 == 0) goto loc_0031C545;
    goto loc_0031BD61;
loc_0031BF03:
    goto loc_0031BD61;
loc_0031BF0E:
    goto loc_0031BBD3;
loc_0031BF1B:
    if (v_rdi > a2) goto loc_0031BCEA;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p20 + 32)))) > 0) goto loc_0031C385;
    result = (*(unsigned __int64 *)(v_stack_p20 + 24)) & (v_rdi);
    if (result < 0x10000ULL) goto loc_0031BD5F;
    if (a5 == 0) goto loc_0031C566;
    goto loc_0031BD61;
loc_0031BF66:
    result = MiGetSystemRegionType(v_r14, a2, *(unsigned __int64 *)(a1 + a2 * 8 + 18528), (unsigned int)(*(unsigned int *)(a1 + 18520)));
    if (((unsigned int)(result)) != 4) goto loc_0031C0EE;
    if (((*(unsigned __int8 *)(v_stack_p20 + 35)) & (16)) != 0) goto loc_0031C5BE;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p20 + 32)))) > 0) goto loc_0031C5D1;
    if (((*(unsigned __int8 *)(v_rip + 11607091)) & (0)) == 0) goto loc_0031C3ED;
    if (v_stack_p80 != 0) goto loc_0031C013;
    result = MiSafeLockPage(v_r13, a2, *(unsigned __int64 *)(a1 + a2 * 8 + 18528), (unsigned int)(*(unsigned int *)(a1 + 18520)));
    if (((unsigned __int8)(result)) == 17) goto loc_0031C5EF;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p20 + 34)) & (7));
    if (((unsigned __int8)(result)) != 6) goto loc_0031C2CE;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p20 + 32)))) > 0) goto loc_0031C2CE;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p20 + 32)))) < 0) goto loc_0031C2CE;
    result = (*(unsigned __int64 *)(v_stack_p20 + 8)) | (v_r13);
    if (result != v_rdi) goto loc_0031C2CE;
    result = MiGetSystemRegionType(v_r14, a2, *(unsigned __int64 *)(a1 + a2 * 8 + 18528), (unsigned int)(*(unsigned int *)(a1 + 18520)));
    if (((unsigned int)(result)) != 4) goto loc_0031C2CE;
loc_0031C013:
    result = MI_READ_PTE_LOCK_FREE(v_rdi, a2, *(unsigned __int64 *)(a1 + a2 * 8 + 18528), (unsigned int)(*(unsigned int *)(a1 + 18520)));
    if (((0) & ((unsigned __int8)(result))) == 0) goto loc_0031C20D;
    a1 = (result) >> (12);
    a1 = (a1) & (a2);
    if (v_r13 != a1) goto loc_0031C20D;
    if (v_r13 < a1) goto loc_0031C0D5;
    v_rsi = 0;
loc_0031C04E:
    if (((unsigned __int8)((unsigned __int8)(result))) == 17) goto loc_0031BD61;
loc_0031C058:
    if (((unsigned __int8)((unsigned __int8)(result))) >= 2) goto loc_0031BD61;
    if ((*(unsigned int *)(v_rip + 13282472)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)((unsigned __int8)(result));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(a1 + a2 * 8 + 18528), (unsigned int)(*(unsigned int *)(a1 + 18520)));
    }
    goto loc_0031BD61;
loc_0031C094:
    result = (unsigned __int8)((unsigned __int8)(result));
    if ((unsigned int)((unsigned int)(v_stack_p80)) == 0) {
        a1 = v_r13;
        result = MiRequestIoPageMdlCacheRelease(a1, a2, *(unsigned __int64 *)(a1 + a2 * 8 + 18528), (unsigned int)(*(unsigned int *)(a1 + 18520)));
    }
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p20 + 32)))) > 0) goto loc_0031C0BC;
    result = (*(unsigned __int64 *)(v_stack_p20 + 24)) & (v_rdi);
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p20 + 32)))) <= result) goto loc_0031BD5F;
loc_0031C0BC:
    if (a5 == 0) goto loc_0031C5A8;
    goto loc_0031BD61;
loc_0031C0D5:
    if (a5 != 0) goto loc_0031C2D9;
    goto loc_0031C04E;
loc_0031C0EE:
    if (v_r14 < (*(unsigned __int64 *)(v_rip + 13282115))) goto loc_0031C270;
    result = (*(unsigned __int64 *)(v_rip + 13282523)) << (12);
    result = (result) + (*(unsigned __int64 *)(v_rip + 13282115));
    if (v_r14 > result) goto loc_0031C270;
    if (a5 == 0) goto loc_0031C5FA;
    goto loc_0031BD61;
loc_0031C12E:
    result = MiGetSystemRegionType(v_r14, *(unsigned __int64 *)(v_rip + 13282115), *(unsigned __int64 *)(a1 + a2 * 8 + 18528), (unsigned int)(*(unsigned int *)(a1 + 18520)));
    if (((unsigned int)(result)) != 5) goto loc_0031C222;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p20 + 32)))) > 0) goto loc_0031C257;
    result = (*(unsigned __int64 *)(v_stack_p20 + 24)) & (v_rdi);
    if (result < 0x10000ULL) goto loc_0031BD5F;
    if (a5 == 0) goto loc_0031C57C;
    goto loc_0031BD61;
loc_0031C177:
    if (a5 >= 0) goto loc_0031BDAF;
    if (a5 == 0) goto loc_0031C63C;
    goto loc_0031BD61;
loc_0031C19C:
    if (a5 == 0) goto loc_0031C65D;
    goto loc_0031BD61;
loc_0031C1B5:
    v_rsi = 0;
    if (v_rdi != result) goto loc_0031C39E;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p20 + 32)))) <= 1) goto loc_0031BD61;
    if (a5 != 0) goto loc_0031C50E;
loc_0031C1EA:
    goto loc_0031BD61;
loc_0031C1F4:
    if (a5 == 0) goto loc_0031C668;
    goto loc_0031BD61;
loc_0031C20D:
    if (a5 != 0) goto loc_0031C292;
    goto loc_0031C04E;
loc_0031C222:
    result = MiHyperPage(v_stack_p20, *(unsigned __int64 *)(v_rip + 13282115), *(unsigned __int64 *)(a1 + a2 * 8 + 18528), (unsigned int)(*(unsigned int *)(a1 + 18520)));
    if ((unsigned int)(result) == 0) goto loc_0031C3BB;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p20 + 32)))) <= 1) goto loc_0031BD5F;
    if (a5 == 0) goto loc_0031C587;
    goto loc_0031BD61;
loc_0031C257:
    if (a5 == 0) goto loc_0031C571;
    goto loc_0031BD61;
loc_0031C270:
    if (((unsigned int)(v_stack_p20)) != 11) goto loc_0031C44F;
    if (a5 == 0) goto loc_0031C605;
    goto loc_0031BD61;
loc_0031C292:
    goto loc_0031C04E;
loc_0031C29D:
    if (*(unsigned __int64 *)(v_stack_p20 + 8) == 0) goto loc_0031BDFA;
    if (a5 == 0) goto loc_0031C647;
    goto loc_0031BD61;
loc_0031C2CE:
    goto loc_0031C058;
loc_0031C2D9:
    goto loc_0031C04E;
loc_0031C2E4:
    if ((unsigned int)((unsigned int)(v_stack_p80)) == 0) goto loc_0031C4DF;
    result = MiGetBaseResidentPage(v_stack_p20, *(unsigned __int64 *)(v_rip + 13282115), *(unsigned __int64 *)(a1 + a2 * 8 + 18528), (unsigned int)(*(unsigned int *)(a1 + 18520)));
    result = MiGetPfnPageSizeIndex(result, *(unsigned __int64 *)(v_rip + 13282115), *(unsigned __int64 *)(a1 + a2 * 8 + 18528), (unsigned int)(*(unsigned int *)(a1 + 18520)));
    if (result != v_stack_p20) {
    }
loc_0031C31A:
    if (((unsigned int)(result)) != 3) goto loc_0031C519;
    goto loc_0031BB94;
loc_0031C33A:
    if (a5 == 0) goto loc_0031C52F;
    goto loc_0031BD61;
loc_0031C353:
    if (a5 == 0) goto loc_0031C53A;
    goto loc_0031BD61;
loc_0031C36C:
    if (a5 == 0) goto loc_0031C550;
    goto loc_0031BD61;
loc_0031C385:
    if (a5 == 0) goto loc_0031C55B;
    goto loc_0031BD61;
loc_0031C39E:
    if (a5 != 1) goto loc_0031C503;
loc_0031C3B1:
    goto loc_0031BD61;
loc_0031C3BB:
    if (a5 == 0) goto loc_0031C592;
    goto loc_0031BD61;
loc_0031C3D4:
    if (a5 == 0) goto loc_0031C59D;
    goto loc_0031BD61;
loc_0031C3ED:
    if (a5 == 0) goto loc_0031C5E4;
    goto loc_0031BD61;
loc_0031C406:
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p20 + 32)))) > 1) goto loc_0031C42B;
    result = (*(unsigned __int64 *)(v_stack_p20 + 24)) & (v_rdi);
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p20 + 32)))) <= result) goto loc_0031BD5F;
loc_0031C42B:
    if (a5 == 0) goto loc_0031C5B3;
    goto loc_0031BD61;
loc_0031C444:
    goto loc_0031BD61;
loc_0031C44F:
    if (((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p20 + 32))))) != 8) goto loc_0031C46D;
    if (a5 == 0) goto loc_0031C610;
    goto loc_0031BD61;
loc_0031C46D:
    if (v_r14 < ((unsigned int)(a3))) goto loc_0031C4AD;
    if (v_r14 > ((unsigned int)(a3))) goto loc_0031C4AD;
    if (a5 == 0) goto loc_0031C61B;
    goto loc_0031BD61;
loc_0031C4A0:
    goto loc_0031BD61;
loc_0031C4AD:
    if (a5 == 0) goto loc_0031C626;
    goto loc_0031BD61;
loc_0031C4C6:
    if (a5 == 0) goto loc_0031C652;
    goto loc_0031BD61;
loc_0031C4DF:
    v_stack_p20 = 0;
    v_stack_p78 = 0;
    result = MiGetPfnPageSizeIndexUnsynchronized((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_p20 + 32))), v_stack_p20, v_stack_p78, (unsigned int)(*(unsigned int *)(a1 + 18520)));
    goto loc_0031C31A;
loc_0031C503:
    goto loc_0031C3B1;
loc_0031C50E:
    goto loc_0031C1EA;
loc_0031C519:
    goto loc_0031BD61;
loc_0031C52F:
    goto loc_0031BD61;
loc_0031C53A:
    goto loc_0031BD61;
loc_0031C545:
    goto loc_0031BD61;
loc_0031C550:
    goto loc_0031BD61;
loc_0031C55B:
    goto loc_0031BD61;
loc_0031C566:
    goto loc_0031BD61;
loc_0031C571:
    goto loc_0031BD61;
loc_0031C57C:
    goto loc_0031BD61;
loc_0031C587:
    goto loc_0031BD61;
loc_0031C592:
    goto loc_0031BD61;
loc_0031C59D:
    goto loc_0031BD61;
loc_0031C5A8:
    goto loc_0031BD61;
loc_0031C5B3:
    goto loc_0031BD61;
loc_0031C5BE:
loc_0031C5D1:
loc_0031C5E4:
    goto loc_0031BD61;
loc_0031C5EF:
    goto loc_0031BD61;
loc_0031C5FA:
    goto loc_0031BD61;
loc_0031C605:
    goto loc_0031BD61;
loc_0031C610:
    goto loc_0031BD61;
loc_0031C61B:
    goto loc_0031BD61;
loc_0031C626:
    goto loc_0031BD61;
loc_0031C631:
    goto loc_0031BD61;
loc_0031C63C:
    goto loc_0031BD61;
loc_0031C647:
    goto loc_0031BD61;
loc_0031C652:
    goto loc_0031BD61;
loc_0031C65D:
    goto loc_0031BD61;
loc_0031C668:
    goto loc_0031BD61;
}
```

## 5. (Beta) C Style

```c
int64_t MiActivePageClaimCandidate(int64_t Arg1, void *Arg2, int32_t Arg3, int32_t Arg4, uint32_t Arg5, void *Arg6)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;
    uint32_t v_stack_p80;

    v_stack_p20 = local_rbx;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (48);
    local_r10 = (uint32_t)(((uint32_t)(Arg3)) & (1));
    v_stack_p18 = (uint32_t)(local_r10);
    local_r13 = (Arg2) - (result);
    local_r13 = (local_r13) >> (4);
    local_r13 = (local_r13) * (result);
    local_rdi = (*(uint64_t *)(arg2 + 0x8)) | (result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (8)) != 0) goto loc_0031BE03;
    if (((local_r11) & (*(uint64_t *)(arg2 + 0x28))) != 0) goto loc_0031C2E4;
loc_0031BB94:
    result = (*(uint64_t *)(arg2 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xB144E9) + result * 8)) != Arg1) goto loc_0031C33A;
    local_r14 = (uint32_t)(((uint32_t)(Arg4)) & (0x410000ULL));
    if (((uint32_t)(local_r14)) == 0x410000ULL) goto loc_0031BBD3;
    if ((((uint8_t)((uint32_t)(Arg3))) & (2)) == 0) goto loc_0031BE35;
loc_0031BBD3:
    if (sign_flag) goto loc_0031BD7D;
    if (local_rdi == -8) goto loc_0031C353;
    if (local_rdi < (*(uint64_t *)(arg2 + 0x28))) goto loc_0031BC19;
    result = (local_rdi) >> (39);
    result = (uint32_t)((result) & (511));
    result = (uint32_t)((result) - (256));
    if ((*(uint8_t *)(result + v_rip - 0x31BBC0 * 1 + 0xE38AA8)) == 4) goto loc_0031BEEA;
loc_0031BC19:
    result = (*(uint64_t *)(arg2 + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) == 1) goto loc_0031BE1C;
    result = (*(uint64_t *)(arg2 + 0x28)) & (Arg4);
    if (result == (*(uint64_t *)(v_rip + 0xB144E9))) goto loc_0031BE1C;
    if (local_rdi < ((uint32_t)(Arg3))) goto loc_0031C444;
    if (local_rdi > ((uint32_t)(Arg3))) goto loc_0031C444;
    local_r14 = (local_rdi) << (25);
    result = ((uint32_t)(Arg3)) << (25);
    local_r14 = (local_r14) - (result);
    local_r14 = (local_r14) >> (16);
    if (((1) & ((uint8_t)(*(uint64_t *)(arg2)))) == 0) goto loc_0031BE8C;
    if (*(uint64_t *)(v_rip + 0xCAAE0C) == 0) goto loc_0031BCBA;
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xCAAE0C) + 0x28)) >> (12);
    if (local_r13 == result) goto loc_0031C36C;
loc_0031BCBA:
    Arg3 = 0;
loc_0031BCDB:
    if (0 >= 3) goto loc_0031BD09;
    if (local_rdi >= (*(uint64_t *)(v_rip + 0xB144E9))) goto loc_0031BF1B;
loc_0031BCEA:
    Arg1 = (*(uint64_t *)(v_rip + 0xB144E9)) >> (9);
    Arg1 = (Arg1) & (local_r11);
    Arg2 = (Arg2) >> (9);
    Arg1 = (Arg1) + ((uint32_t)(Arg3));
    Arg2 = (Arg2) & (local_r11);
    Arg2 = (Arg2) + ((uint32_t)(Arg3));
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_0031BCDB;
loc_0031BD09:
    result = (*(uint64_t *)(arg2 + 0x28)) & (Arg4);
    if (result == local_r13) goto loc_0031C1B5;
    result = (*(uint64_t *)(arg2 + 0x18)) & (local_rdi);
    if (result > 1) goto loc_0031C12E;
    if (((Arg4) & (*(uint64_t *)(arg2 + 0x18))) == 0) goto loc_0031C3D4;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20)))) > 1) goto loc_0031C094;
    result = (*(uint64_t *)(arg2 + 0x18)) & (local_rdi);
    if (((uint16_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20)))) > result) goto loc_0031C094;
loc_0031BD5F:
    local_rsi = 0;
loc_0031BD61:
    local_rsp = (local_rsp) + (48);
    return 0;
loc_0031BD7D:
    if (condition_is_below) goto loc_0031C1F4;
    if (local_rdi == (*(uint64_t *)(v_rip + 0xB11DD5))) goto loc_0031C1F4;
    if (local_rdi == (*(uint64_t *)(v_rip + 0xB11DD0))) goto loc_0031C1F4;
    if ((uint32_t)(local_r10) != 0) goto loc_0031C177;
loc_0031BDAF:
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x20)))) > 0) goto loc_0031C19C;
    result = (*(uint64_t *)(v_stack_p20 + 0x18)) & (local_rdi);
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x20)))) > result) goto loc_0031C19C;
    if (((0) & ((uint8_t)(*(uint64_t *)(v_stack_p20)))) == 0) goto loc_0031C4C6;
    if (((local_r11) & (*(uint64_t *)(v_stack_p20 + 0x28))) != 0) goto loc_0031BDFA;
    if (!sign_flag) goto loc_0031C29D;
loc_0031BDFA:
    goto loc_0031BD5F;
loc_0031BE03:
    if (Arg5 == 0) goto loc_0031BF03;
    goto loc_0031BD61;
loc_0031BE1C:
    if (Arg5 == 0) goto loc_0031C631;
    goto loc_0031BD61;
loc_0031BE35:
    if ((*(uint8_t *)(Arg1 + 0x3EE6)) == 0) goto loc_0031BBD3;
    Arg4 = 0;
loc_0031BE47:
    if (0 >= 2) goto loc_0031BF0E;
    result = (0) + (0);
    if ((*(uint64_t *)(Arg1 + result * 8 + 0x3FC8)) == 0) goto loc_0031BE87;
    Arg2 = (local_r13) >> ((uint8_t)((uint32_t)(*(uint32_t *)(Arg3 + Arg4 * 4 + 0x135E8))));
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) != 0) goto loc_0031C4A0;
loc_0031BE87:
    Arg4 = (uint32_t)((Arg4) + 1);
    goto loc_0031BE47;
loc_0031BE8C:
    result = MiHyperPage(v_stack_p20, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_0031C406;
    Arg2 = 0;
loc_0031BEA6:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x4858))))) goto loc_0031BF66;
    if (*(uint64_t *)(*(uint64_t *)(Arg1 + arg2 * 8 + 0x4860) + 0xB8) == 0) goto loc_0031BEE6;
    if (local_r14 < (*(uint64_t *)(*(uint64_t *)(Arg1 + arg2 * 8 + 0x4860) + 0xB8))) goto loc_0031BEE6;
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + arg2 * 8 + 0x4860) + 0x4))) * ((uint32_t)(*(uint32_t *)(v_rip + 0xB1B4BA)));
    Arg1 = (Arg1) + (*(uint64_t *)(*(uint64_t *)(Arg1 + arg2 * 8 + 0x4860) + 0xB8));
    if (local_r14 < Arg1) goto loc_0031BD5F;
loc_0031BEE6:
    Arg2 = (uint32_t)((Arg2) + 1);
    goto loc_0031BEA6;
loc_0031BEEA:
    if (Arg5 == 0) goto loc_0031C545;
    goto loc_0031BD61;
loc_0031BF03:
    goto loc_0031BD61;
loc_0031BF0E:
    goto loc_0031BBD3;
loc_0031BF1B:
    if (local_rdi > Arg2) goto loc_0031BCEA;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x20)))) > 0) goto loc_0031C385;
    result = (*(uint64_t *)(v_stack_p20 + 0x18)) & (local_rdi);
    if (result < 0x10000ULL) goto loc_0031BD5F;
    if (Arg5 == 0) goto loc_0031C566;
    goto loc_0031BD61;
loc_0031BF66:
    result = MiGetSystemRegionType(local_r14, Arg2, *(uint64_t *)(Arg1 + arg2 * 8 + 0x4860), (uint32_t)(*(uint32_t *)(Arg1 + 0x4858)));
    if (((uint32_t)(result)) != 4) goto loc_0031C0EE;
    if (((*(uint8_t *)(v_stack_p20 + 0x23)) & (16)) != 0) goto loc_0031C5BE;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x20)))) > 0) goto loc_0031C5D1;
    if (((*(uint8_t *)(v_rip + 0xB11C33)) & (0)) == 0) goto loc_0031C3ED;
    if (v_stack_p80 != 0) goto loc_0031C013;
    result = MiSafeLockPage(local_r13, Arg2, *(uint64_t *)(Arg1 + arg2 * 8 + 0x4860), (uint32_t)(*(uint32_t *)(Arg1 + 0x4858)));
    if (((uint8_t)(result)) == 17) goto loc_0031C5EF;
    result = (uint8_t)((*(uint8_t *)(v_stack_p20 + 0x22)) & (7));
    if (((uint8_t)(result)) != 6) goto loc_0031C2CE;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x20)))) > 0) goto loc_0031C2CE;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x20)))) < 0) goto loc_0031C2CE;
    result = (*(uint64_t *)(v_stack_p20 + 0x8)) | (local_r13);
    if (result != local_rdi) goto loc_0031C2CE;
    result = MiGetSystemRegionType(local_r14, Arg2, *(uint64_t *)(Arg1 + arg2 * 8 + 0x4860), (uint32_t)(*(uint32_t *)(Arg1 + 0x4858)));
    if (((uint32_t)(result)) != 4) goto loc_0031C2CE;
loc_0031C013:
    result = MI_READ_PTE_LOCK_FREE(local_rdi, Arg2, *(uint64_t *)(Arg1 + arg2 * 8 + 0x4860), (uint32_t)(*(uint32_t *)(Arg1 + 0x4858)));
    if (((0) & ((uint8_t)(result))) == 0) goto loc_0031C20D;
    Arg1 = (result) >> (12);
    Arg1 = (Arg1) & (Arg2);
    if (local_r13 != Arg1) goto loc_0031C20D;
    if (local_r13 < Arg1) goto loc_0031C0D5;
    local_rsi = 0;
loc_0031C04E:
    if (((uint8_t)((uint8_t)(result))) == 17) goto loc_0031BD61;
loc_0031C058:
    if (((uint8_t)((uint8_t)(result))) >= 2) goto loc_0031BD61;
    if ((*(uint32_t *)(v_rip + 0xCAACA8)) != 0) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)((uint8_t)(result));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(Arg1 + arg2 * 8 + 0x4860), (uint32_t)(*(uint32_t *)(Arg1 + 0x4858)));
    }
    goto loc_0031BD61;
loc_0031C094:
    result = (uint8_t)((uint8_t)(result));
    if ((uint32_t)((uint32_t)(v_stack_p80)) == 0) {
        Arg1 = local_r13;
        result = MiRequestIoPageMdlCacheRelease(Arg1, Arg2, *(uint64_t *)(Arg1 + arg2 * 8 + 0x4860), (uint32_t)(*(uint32_t *)(Arg1 + 0x4858)));
    }
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x20)))) > 0) goto loc_0031C0BC;
    result = (*(uint64_t *)(v_stack_p20 + 0x18)) & (local_rdi);
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x20)))) <= result) goto loc_0031BD5F;
loc_0031C0BC:
    if (Arg5 == 0) goto loc_0031C5A8;
    goto loc_0031BD61;
loc_0031C0D5:
    if (Arg5 != 0) goto loc_0031C2D9;
    goto loc_0031C04E;
loc_0031C0EE:
    if (local_r14 < (*(uint64_t *)(v_rip + 0xCAAB43))) goto loc_0031C270;
    result = (*(uint64_t *)(v_rip + 0xCAACDB)) << (12);
    result = (result) + (*(uint64_t *)(v_rip + 0xCAAB43));
    if (local_r14 > result) goto loc_0031C270;
    if (Arg5 == 0) goto loc_0031C5FA;
    goto loc_0031BD61;
loc_0031C12E:
    result = MiGetSystemRegionType(local_r14, *(uint64_t *)(v_rip + 0xCAAB43), *(uint64_t *)(Arg1 + arg2 * 8 + 0x4860), (uint32_t)(*(uint32_t *)(Arg1 + 0x4858)));
    if (((uint32_t)(result)) != 5) goto loc_0031C222;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x20)))) > 0) goto loc_0031C257;
    result = (*(uint64_t *)(v_stack_p20 + 0x18)) & (local_rdi);
    if (result < 0x10000ULL) goto loc_0031BD5F;
    if (Arg5 == 0) goto loc_0031C57C;
    goto loc_0031BD61;
loc_0031C177:
    if (Arg5 >= 0) goto loc_0031BDAF;
    if (Arg5 == 0) goto loc_0031C63C;
    goto loc_0031BD61;
loc_0031C19C:
    if (Arg5 == 0) goto loc_0031C65D;
    goto loc_0031BD61;
loc_0031C1B5:
    local_rsi = 0;
    if (local_rdi != result) goto loc_0031C39E;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x20)))) <= 1) goto loc_0031BD61;
    if (Arg5 != 0) goto loc_0031C50E;
loc_0031C1EA:
    goto loc_0031BD61;
loc_0031C1F4:
    if (Arg5 == 0) goto loc_0031C668;
    goto loc_0031BD61;
loc_0031C20D:
    if (Arg5 != 0) goto loc_0031C292;
    goto loc_0031C04E;
loc_0031C222:
    result = MiHyperPage(v_stack_p20, *(uint64_t *)(v_rip + 0xCAAB43), *(uint64_t *)(Arg1 + arg2 * 8 + 0x4860), (uint32_t)(*(uint32_t *)(Arg1 + 0x4858)));
    if ((uint32_t)(result) == 0) goto loc_0031C3BB;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x20)))) <= 1) goto loc_0031BD5F;
    if (Arg5 == 0) goto loc_0031C587;
    goto loc_0031BD61;
loc_0031C257:
    if (Arg5 == 0) goto loc_0031C571;
    goto loc_0031BD61;
loc_0031C270:
    if (((uint32_t)(v_stack_p20)) != 11) goto loc_0031C44F;
    if (Arg5 == 0) goto loc_0031C605;
    goto loc_0031BD61;
loc_0031C292:
    goto loc_0031C04E;
loc_0031C29D:
    if (*(uint64_t *)(v_stack_p20 + 0x8) == 0) goto loc_0031BDFA;
    if (Arg5 == 0) goto loc_0031C647;
    goto loc_0031BD61;
loc_0031C2CE:
    goto loc_0031C058;
loc_0031C2D9:
    goto loc_0031C04E;
loc_0031C2E4:
    if ((uint32_t)((uint32_t)(v_stack_p80)) == 0) goto loc_0031C4DF;
    result = MiGetBaseResidentPage(v_stack_p20, *(uint64_t *)(v_rip + 0xCAAB43), *(uint64_t *)(Arg1 + arg2 * 8 + 0x4860), (uint32_t)(*(uint32_t *)(Arg1 + 0x4858)));
    result = MiGetPfnPageSizeIndex(result, *(uint64_t *)(v_rip + 0xCAAB43), *(uint64_t *)(Arg1 + arg2 * 8 + 0x4860), (uint32_t)(*(uint32_t *)(Arg1 + 0x4858)));
    if (result != v_stack_p20) {
    }
loc_0031C31A:
    if (((uint32_t)(result)) != 3) goto loc_0031C519;
    goto loc_0031BB94;
loc_0031C33A:
    if (Arg5 == 0) goto loc_0031C52F;
    goto loc_0031BD61;
loc_0031C353:
    if (Arg5 == 0) goto loc_0031C53A;
    goto loc_0031BD61;
loc_0031C36C:
    if (Arg5 == 0) goto loc_0031C550;
    goto loc_0031BD61;
loc_0031C385:
    if (Arg5 == 0) goto loc_0031C55B;
    goto loc_0031BD61;
loc_0031C39E:
    if (Arg5 != 1) goto loc_0031C503;
loc_0031C3B1:
    goto loc_0031BD61;
loc_0031C3BB:
    if (Arg5 == 0) goto loc_0031C592;
    goto loc_0031BD61;
loc_0031C3D4:
    if (Arg5 == 0) goto loc_0031C59D;
    goto loc_0031BD61;
loc_0031C3ED:
    if (Arg5 == 0) goto loc_0031C5E4;
    goto loc_0031BD61;
loc_0031C406:
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x20)))) > 1) goto loc_0031C42B;
    result = (*(uint64_t *)(v_stack_p20 + 0x18)) & (local_rdi);
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x20)))) <= result) goto loc_0031BD5F;
loc_0031C42B:
    if (Arg5 == 0) goto loc_0031C5B3;
    goto loc_0031BD61;
loc_0031C444:
    goto loc_0031BD61;
loc_0031C44F:
    if (((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x20))))) != 8) goto loc_0031C46D;
    if (Arg5 == 0) goto loc_0031C610;
    goto loc_0031BD61;
loc_0031C46D:
    if (local_r14 < ((uint32_t)(Arg3))) goto loc_0031C4AD;
    if (local_r14 > ((uint32_t)(Arg3))) goto loc_0031C4AD;
    if (Arg5 == 0) goto loc_0031C61B;
    goto loc_0031BD61;
loc_0031C4A0:
    goto loc_0031BD61;
loc_0031C4AD:
    if (Arg5 == 0) goto loc_0031C626;
    goto loc_0031BD61;
loc_0031C4C6:
    if (Arg5 == 0) goto loc_0031C652;
    goto loc_0031BD61;
loc_0031C4DF:
    v_stack_p20 = 0;
    v_stack_p78 = 0;
    result = MiGetPfnPageSizeIndexUnsynchronized((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_p20 + 0x20))), v_stack_p20, v_stack_p78, (uint32_t)(*(uint32_t *)(Arg1 + 0x4858)));
    goto loc_0031C31A;
loc_0031C503:
    goto loc_0031C3B1;
loc_0031C50E:
    goto loc_0031C1EA;
loc_0031C519:
    goto loc_0031BD61;
loc_0031C52F:
    goto loc_0031BD61;
loc_0031C53A:
    goto loc_0031BD61;
loc_0031C545:
    goto loc_0031BD61;
loc_0031C550:
    goto loc_0031BD61;
loc_0031C55B:
    goto loc_0031BD61;
loc_0031C566:
    goto loc_0031BD61;
loc_0031C571:
    goto loc_0031BD61;
loc_0031C57C:
    goto loc_0031BD61;
loc_0031C587:
    goto loc_0031BD61;
loc_0031C592:
    goto loc_0031BD61;
loc_0031C59D:
    goto loc_0031BD61;
loc_0031C5A8:
    goto loc_0031BD61;
loc_0031C5B3:
    goto loc_0031BD61;
loc_0031C5BE:
loc_0031C5D1:
loc_0031C5E4:
    goto loc_0031BD61;
loc_0031C5EF:
    goto loc_0031BD61;
loc_0031C5FA:
    goto loc_0031BD61;
loc_0031C605:
    goto loc_0031BD61;
loc_0031C610:
    goto loc_0031BD61;
loc_0031C61B:
    goto loc_0031BD61;
loc_0031C626:
    goto loc_0031BD61;
loc_0031C631:
    goto loc_0031BD61;
loc_0031C63C:
    goto loc_0031BD61;
loc_0031C647:
    goto loc_0031BD61;
loc_0031C652:
    goto loc_0031BD61;
loc_0031C65D:
    goto loc_0031BD61;
loc_0031C668:
    goto loc_0031BD61;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R/W` |
| `Arg2` | `+ 0x20` | `32` | `R` |
| `Arg2` | `+ 0x22` | `8` | `R` |
| `Arg2` | `+ 0x23` | `8` | `R` |
| `Arg2` | `+ 0x28` | `64` | `R` |
| `Arg6` | `+ 0x0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0031BB00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
