# MiSharedInsertPfnChainInList

- RVA: `0x0033CA70`–`0x0033D324` (길이 `2,228` bytes)
- VA: `0x000000014033CA70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007709C`
- 디코드: `535`개 명령, `2,228/2,228` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x0033D10C` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0033D1D5` → [MiPageToChannel](../2B/MiPageToChannel_function_002B9B48.md) (function, `0x002B9B48`)
- `0x0033D215` → [MiIsDecayPfn](../2B/MiIsDecayPfn_function_002B9240.md) (function, `0x002B9240`)
- `0x0033D230` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x0033D260` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0033D2A7` → [MiGetPfnPriority](../32/MiGetPfnPriority_function_003226F0.md) (function, `0x003226F0`)
- `0x0033D2F1` → [MiGetPfnPriority](../32/MiGetPfnPriority_function_003226F0.md) (function, `0x003226F0`)

### Direct callers
- [sub_0033E2D1](Unknown_function_0033E2D1.md) at `0x0033E6E3`

### Static image references
- `0x0033CB65` → RVA `0x00E2DC80` (`.data`; read)
- `0x0033CCFC` → RVA `0x00E30088` (`.data`; read)
- `0x0033CD15` → RVA `0x00E2DBC0` (`.data`; read)
- `0x0033CD21` → RVA `0x00E2DBC4` (`.data`; read)
- `0x0033CD32` → RVA `0x00E2DC20` (`.data`; read)
- `0x0033CD7D` → RVA `0x00E2DBC0` (`.data`; write)
- `0x0033CDC0` → RVA `0x00E2DC28` (`.data`; read)
- `0x0033D1DF` → RVA `0x00E2DCE0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0033CA70  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0033CA75  55                              push rbp
0033CA76  53                              push rbx
0033CA77  57                              push rdi
0033CA78  41 54                           push r12
0033CA7A  41 56                           push r14
0033CA7C  41 57                           push r15
0033CA7E  48 8D 6C 24 C8                  lea rbp, [rsp - 0x38]
0033CA83  48 81 EC 38 01 00 00            sub rsp, 0x138
0033CA8A  4C 8B 79 58                     mov r15, qword ptr [rcx + 0x58]
0033CA8E  4C 8B C2                        mov r8, rdx
0033CA91  4C 89 BD 80 00 00 00            mov qword ptr [rbp + 0x80], r15
0033CA98  4C 8B F1                        mov r14, rcx
0033CA9B  49 BA 00 00 00 00 00 DE FF FF   movabs r10, 0xffffde0000000000
0033CAA5  49 BB FF FF FF FF FF 00 00 00   movabs r11, 0xffffffffff
0033CAAF  49 B9 FF FF FF FF 3F 00 00 00   movabs r9, 0x3fffffffff
0033CAB9  4D 85 FF                        test r15, r15
0033CABC  74 40                           je 0x14033cafe
0033CABE  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
0033CAC2  49 3B C1                        cmp rax, r9
0033CAC5  74 37                           je 0x14033cafe
0033CAC7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
0033CAD0  48 8D 14 40                     lea rdx, [rax + rax*2]
0033CAD4  48 C1 E2 04                     shl rdx, 4
0033CAD8  49 8B C2                        mov rax, r10
0033CADB  48 03 D0                        add rdx, rax
0033CADE  8B 4A 20                        mov ecx, dword ptr [rdx + 0x20]
0033CAE1  48 8B 02                        mov rax, qword ptr [rdx]
0033CAE4  89 4D 70                        mov dword ptr [rbp + 0x70], ecx
0033CAE7  49 23 C3                        and rax, r11
0033CAEA  C1 E9 18                        shr ecx, 0x18
0033CAED  80 C9 08                        or cl, 8
0033CAF0  88 4D 73                        mov byte ptr [rbp + 0x73], cl
0033CAF3  8B 4D 70                        mov ecx, dword ptr [rbp + 0x70]
0033CAF6  89 4A 20                        mov dword ptr [rdx + 0x20], ecx
0033CAF9  49 3B C1                        cmp rax, r9
0033CAFC  75 D2                           jne 0x14033cad0
0033CAFE  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0033CB02  48 89 B4 24 30 01 00 00         mov qword ptr [rsp + 0x130], rsi
0033CB0A  4C 89 AC 24 28 01 00 00         mov qword ptr [rsp + 0x128], r13
0033CB12  48 8D 3C 40                     lea rdi, [rax + rax*2]
0033CB16  48 C1 E7 04                     shl rdi, 4
0033CB1A  49 8B C2                        mov rax, r10
0033CB1D  48 03 F8                        add rdi, rax
0033CB20  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
0033CB24  48 8D 1C 40                     lea rbx, [rax + rax*2]
0033CB28  48 C1 E3 04                     shl rbx, 4
0033CB2C  49 8B C2                        mov rax, r10
0033CB2F  4D 8B 60 08                     mov r12, qword ptr [r8 + 8]
0033CB33  48 03 D8                        add rbx, rax
0033CB36  4D 8B 40 20                     mov r8, qword ptr [r8 + 0x20]
0033CB3A  48 B9 AB AA AA AA AA AA AA AA   movabs rcx, 0xaaaaaaaaaaaaaaab
0033CB44  4C 89 45 70                     mov qword ptr [rbp + 0x70], r8
0033CB48  4C 89 A5 88 00 00 00            mov qword ptr [rbp + 0x88], r12
0033CB4F  4D 85 FF                        test r15, r15
0033CB52  0F 84 FB 00 00 00               je 0x14033cc53
0033CB58  49 8B C2                        mov rax, r10
0033CB5B  4D 8B 47 10                     mov r8, qword ptr [r15 + 0x10]
0033CB5F  49 8B D7                        mov rdx, r15
0033CB62  48 2B D0                        sub rdx, rax
0033CB65  48 8B 05 14 11 AF 00            mov rax, qword ptr [rip + 0xaf1114]
0033CB6C  48 C1 FA 04                     sar rdx, 4
0033CB70  48 0F AF D1                     imul rdx, rcx
0033CB74  48 85 C0                        test rax, rax
0033CB77  74 0C                           je 0x14033cb85
0033CB79  41 F6 C0 10                     test r8b, 0x10
0033CB7D  75 06                           jne 0x14033cb85
0033CB7F  48 F7 D0                        not rax
0033CB82  4C 23 C0                        and r8, rax
0033CB85  49 8B 4F 28                     mov rcx, qword ptr [r15 + 0x28]
0033CB89  49 BD 00 00 00 00 00 FF FF FF   movabs r13, 0xffffff0000000000
0033CB93  48 8B 03                        mov rax, qword ptr [rbx]
0033CB96  4C 8B C9                        mov r9, rcx
0033CB99  48 33 C2                        xor rax, rdx
0033CB9C  49 C1 E8 0C                     shr r8, 0xc
0033CBA0  49 23 C5                        and rax, r13
0033CBA3  4D 23 C3                        and r8, r11
0033CBA6  48 33 C2                        xor rax, rdx
0033CBA9  4D 23 CB                        and r9, r11
0033CBAC  48 89 03                        mov qword ptr [rbx], rax
0033CBAF  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0033CBB3  48 33 C1                        xor rax, rcx
0033CBB6  49 23 C5                        and rax, r13
0033CBB9  48 33 C1                        xor rax, rcx
0033CBBC  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
0033CBC0  4C 3B C2                        cmp r8, rdx
0033CBC3  0F 85 AC 05 00 00               jne 0x14033d175
0033CBC9  49 8B 56 10                     mov rdx, qword ptr [r14 + 0x10]
0033CBCD  4C 8B 05 AC 10 AF 00            mov r8, qword ptr [rip + 0xaf10ac]
0033CBD4  49 23 D3                        and rdx, r11
0033CBD7  48 C1 E2 0C                     shl rdx, 0xc
0033CBDB  48 8B C2                        mov rax, rdx
0033CBDE  48 0D 80 08 00 00               or rax, 0x880
0033CBE4  4D 85 C0                        test r8, r8
0033CBE7  74 1E                           je 0x14033cc07
0033CBE9  48 8B CA                        mov rcx, rdx
0033CBEC  48 81 CA 90 08 00 00            or rdx, 0x890
0033CBF3  49 0B C8                        or rcx, r8
0033CBF6  48 81 C9 80 08 00 00            or rcx, 0x880
0033CBFD  4C 85 C0                        test rax, r8
0033CC00  48 0F 44 D1                     cmove rdx, rcx
0033CC04  48 8B C2                        mov rax, rdx
0033CC07  49 89 47 10                     mov qword ptr [r15 + 0x10], rax
0033CC0B  4D 8B 4E 18                     mov r9, qword ptr [r14 + 0x18]
0033CC0F  49 8B 57 28                     mov rdx, qword ptr [r15 + 0x28]
0033CC13  48 8B CA                        mov rcx, rdx
0033CC16  48 8B C2                        mov rax, rdx
0033CC19  49 33 C9                        xor rcx, r9
0033CC1C  49 23 CD                        and rcx, r13
0033CC1F  49 33 C9                        xor rcx, r9
0033CC22  F0 49 0F B1 4F 28               lock cmpxchg qword ptr [r15 + 0x28], rcx
0033CC28  4C 8B C0                        mov r8, rax
0033CC2B  48 3B D0                        cmp rdx, rax
0033CC2E  0F 84 88 00 00 00               je 0x14033ccbc
0033CC34  49 8B C8                        mov rcx, r8
0033CC37  4D 33 C1                        xor r8, r9
0033CC3A  4D 23 C5                        and r8, r13
0033CC3D  48 8B C1                        mov rax, rcx
0033CC40  4D 33 C1                        xor r8, r9
0033CC43  F0 4D 0F B1 47 28               lock cmpxchg qword ptr [r15 + 0x28], r8
0033CC49  4C 8B C0                        mov r8, rax
0033CC4C  48 3B C8                        cmp rcx, rax
0033CC4F  75 E3                           jne 0x14033cc34
0033CC51  EB 69                           jmp 0x14033ccbc
0033CC53  49 BD 00 00 00 00 00 FF FF FF   movabs r13, 0xffffff0000000000
0033CC5D  4D 3B E1                        cmp r12, r9
0033CC60  0F 84 70 06 00 00               je 0x14033d2d6
0033CC66  4B 8D 14 64                     lea rdx, [r12 + r12*2]
0033CC6A  48 C1 E2 04                     shl rdx, 4
0033CC6E  49 8B C2                        mov rax, r10
0033CC71  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
0033CC75  48 03 D0                        add rdx, rax
0033CC78  48 8B 02                        mov rax, qword ptr [rdx]
0033CC7B  48 33 C1                        xor rax, rcx
0033CC7E  49 23 C5                        and rax, r13
0033CC81  48 33 C1                        xor rax, rcx
0033CC84  48 89 02                        mov qword ptr [rdx], rax
0033CC87  4D 3B C1                        cmp r8, r9
0033CC8A  0F 84 FC 05 00 00               je 0x14033d28c
0033CC90  49 8B 4E 18                     mov rcx, qword ptr [r14 + 0x18]
0033CC94  4B 8D 14 40                     lea rdx, [r8 + r8*2]
0033CC98  48 03 D2                        add rdx, rdx
0033CC9B  49 B8 18 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000018
0033CCA5  49 8B C0                        mov rax, r8
0033CCA8  48 8B 04 D0                     mov rax, qword ptr [rax + rdx*8]
0033CCAC  48 33 C1                        xor rax, rcx
0033CCAF  49 23 C5                        and rax, r13
0033CCB2  48 33 C1                        xor rax, rcx
0033CCB5  49 8B C8                        mov rcx, r8
0033CCB8  48 89 04 D1                     mov qword ptr [rcx + rdx*8], rax
0033CCBC  41 83 7E 0C 02                  cmp dword ptr [r14 + 0xc], 2
0033CCC1  0F 85 EB 03 00 00               jne 0x14033d0b2
0033CCC7  4D 8B 46 10                     mov r8, qword ptr [r14 + 0x10]
0033CCCB  0F 57 C0                        xorps xmm0, xmm0
0033CCCE  0F 57 C9                        xorps xmm1, xmm1
0033CCD1  49 BA 00 00 00 00 00 DE FF FF   movabs r10, 0xffffde0000000000
0033CCDB  F3 0F 7F 44 24 40               movdqu xmmword ptr [rsp + 0x40], xmm0
0033CCE1  4F 8D 1C 40                     lea r11, [r8 + r8*2]
0033CCE5  49 C1 E3 04                     shl r11, 4
0033CCE9  F3 0F 7F 4C 24 50               movdqu xmmword ptr [rsp + 0x50], xmm1
0033CCEF  49 8B C2                        mov rax, r10
0033CCF2  4D 8D 0C 03                     lea r9, [r11 + rax]
0033CCF6  33 F6                           xor esi, esi
0033CCF8  49 8B 41 28                     mov rax, qword ptr [r9 + 0x28]
0033CCFC  48 8B 0D 85 33 AF 00            mov rcx, qword ptr [rip + 0xaf3385]
0033CD03  48 C1 E8 2B                     shr rax, 0x2b
0033CD07  25 FF 03 00 00                  and eax, 0x3ff
0033CD0C  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
0033CD11  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
0033CD15  48 63 0D A4 0E AF 00            movsxd rcx, dword ptr [rip + 0xaf0ea4]
0033CD1C  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
0033CD21  8B 15 9D 0E AF 00               mov edx, dword ptr [rip + 0xaf0e9d]
0033CD27  3B CA                           cmp ecx, edx
0033CD29  77 1D                           ja 0x14033cd48
0033CD2B  48 8B C1                        mov rax, rcx
0033CD2E  48 C1 E0 04                     shl rax, 4
0033CD32  48 03 05 E7 0E AF 00            add rax, qword ptr [rip + 0xaf0ee7]
0033CD39  4C 3B 00                        cmp r8, qword ptr [rax]
0033CD3C  72 0A                           jb 0x14033cd48
0033CD3E  3B CA                           cmp ecx, edx
0033CD40  74 4B                           je 0x14033cd8d
0033CD42  4C 3B 40 10                     cmp r8, qword ptr [rax + 0x10]
0033CD46  72 45                           jb 0x14033cd8d
0033CD48  44 8B D6                        mov r10d, esi
0033CD4B  41 3B D2                        cmp edx, r10d
0033CD4E  0F 8C A7 03 00 00               jl 0x14033d0fb
0033CD54  41 8D 0C 12                     lea ecx, [r10 + rdx]
0033CD58  D1 F9                           sar ecx, 1
0033CD5A  48 63 C1                        movsxd rax, ecx
0033CD5D  48 C1 E0 04                     shl rax, 4
0033CD61  48 03 05 B8 0E AF 00            add rax, qword ptr [rip + 0xaf0eb8]
0033CD68  4C 3B 00                        cmp r8, qword ptr [rax]
0033CD6B  0F 82 D5 04 00 00               jb 0x14033d246
0033CD71  3B 0D 4D 0E AF 00               cmp ecx, dword ptr [rip + 0xaf0e4d]
0033CD77  0F 85 3A 04 00 00               jne 0x14033d1b7
0033CD7D  89 0D 3D 0E AF 00               mov dword ptr [rip + 0xaf0e3d], ecx
0033CD83  49 BA 00 00 00 00 00 DE FF FF   movabs r10, 0xffffde0000000000
0033CD8D  8B 40 08                        mov eax, dword ptr [rax + 8]
0033CD90  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0033CD94  4D 85 FF                        test r15, r15
0033CD97  0F 85 C9 04 00 00               jne 0x14033d266
0033CD9D  41 8B 71 20                     mov esi, dword ptr [r9 + 0x20]
0033CDA1  41 8B 41 20                     mov eax, dword ptr [r9 + 0x20]
0033CDA5  C1 E8 18                        shr eax, 0x18
0033CDA8  A8 08                           test al, 8
0033CDAA  0F 85 EB 03 00 00               jne 0x14033d19b
0033CDB0  49 B8 AB AA AA AA AA AA AA AA   movabs r8, 0xaaaaaaaaaaaaaaab
0033CDBA  C1 EE 18                        shr esi, 0x18
0033CDBD  83 E6 07                        and esi, 7
0033CDC0  48 83 3D 60 0E AF 00 00         cmp qword ptr [rip + 0xaf0e60], 0
0033CDC8  89 74 24 4C                     mov dword ptr [rsp + 0x4c], esi
0033CDCC  0F 85 F8 03 00 00               jne 0x14033d1ca
0033CDD2  32 C0                           xor al, al
0033CDD4  4C 8B 4D 78                     mov r9, qword ptr [rbp + 0x78]
0033CDD8  49 B8 FF FF FF FF FF FF 7F F0   movabs r8, 0xf07fffffffffffff
0033CDE2  0F B6 C8                        movzx ecx, al
0033CDE5  88 44 24 50                     mov byte ptr [rsp + 0x50], al
0033CDE9  8B C6                           mov eax, esi
0033CDEB  48 BE FF FF FF FF 3F 00 00 00   movabs rsi, 0x3fffffffff
0033CDF5  4D 8B 51 38                     mov r10, qword ptr [r9 + 0x38]
0033CDF9  4D 8B 49 50                     mov r9, qword ptr [r9 + 0x50]
0033CDFD  48 8D 0C CD 3B 00 00 00         lea rcx, [rcx*8 + 0x3b]
0033CE05  48 03 C8                        add rcx, rax
0033CE08  C7 44 24 54 09 00 00 00         mov dword ptr [rsp + 0x54], 9
0033CE10  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
0033CE14  48 6B D1 58                     imul rdx, rcx, 0x58
0033CE18  48 69 C8 80 DF 00 00            imul rcx, rax, 0xdf80
0033CE1F  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0033CE24  4C 89 45 78                     mov qword ptr [rbp + 0x78], r8
0033CE28  48 03 D1                        add rdx, rcx
0033CE2B  48 03 50 10                     add rdx, qword ptr [rax + 0x10]
0033CE2F  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0033CE34  4C 3B D6                        cmp r10, rsi
0033CE37  0F 84 87 04 00 00               je 0x14033d2c4
0033CE3D  4F 8D 04 52                     lea r8, [r10 + r10*2]
0033CE41  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0033CE4B  49 C1 E0 04                     shl r8, 4
0033CE4F  48 8B C0                        mov rax, rax
0033CE52  4D 8B 5E 10                     mov r11, qword ptr [r14 + 0x10]
0033CE56  4C 03 C0                        add r8, rax
0033CE59  0F 57 C0                        xorps xmm0, xmm0
0033CE5C  48 C7 44 24 60 00 00 00 00      mov qword ptr [rsp + 0x60], 0
0033CE65  49 8B CB                        mov rcx, r11
0033CE68  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
0033CE72  48 C1 E1 28                     shl rcx, 0x28
0033CE76  0F 57 C9                        xorps xmm1, xmm1
0033CE79  49 8B 00                        mov rax, qword ptr [r8]
0033CE7C  48 23 C2                        and rax, rdx
0033CE7F  48 0B C8                        or rcx, rax
0033CE82  41 8B 40 24                     mov eax, dword ptr [r8 + 0x24]
0033CE86  49 89 08                        mov qword ptr [r8], rcx
0033CE89  25 FF FF 1F 00                  and eax, 0x1fffff
0033CE8E  49 8B CB                        mov rcx, r11
0033CE91  49 C1 E3 14                     shl r11, 0x14
0033CE95  48 C1 E9 18                     shr rcx, 0x18
0033CE99  C1 E1 15                        shl ecx, 0x15
0033CE9C  0B C8                           or ecx, eax
0033CE9E  48 B8 FF FF FF FF FF FF 7F F0   movabs rax, 0xf07fffffffffffff
0033CEA8  41 89 48 24                     mov dword ptr [r8 + 0x24], ecx
0033CEAC  49 8B 50 28                     mov rdx, qword ptr [r8 + 0x28]
0033CEB0  48 8B CA                        mov rcx, rdx
0033CEB3  48 89 55 88                     mov qword ptr [rbp - 0x78], rdx
0033CEB7  49 33 CB                        xor rcx, r11
0033CEBA  48 23 C8                        and rcx, rax
0033CEBD  48 8B C2                        mov rax, rdx
0033CEC0  49 33 CB                        xor rcx, r11
0033CEC3  F3 0F 7F 44 24 68               movdqu xmmword ptr [rsp + 0x68], xmm0
0033CEC9  F3 0F 7F 4C 24 78               movdqu xmmword ptr [rsp + 0x78], xmm1
0033CECF  0F 11 45 90                     movups xmmword ptr [rbp - 0x70], xmm0
0033CED3  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
0033CED7  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
0033CEDB  F0 49 0F B1 48 28               lock cmpxchg qword ptr [r8 + 0x28], rcx
0033CEE1  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
0033CEE5  48 3B D0                        cmp rdx, rax
0033CEE8  74 29                           je 0x14033cf13
0033CEEA  66 0F 1F 44 00 00               nop word ptr [rax + rax]
0033CEF0  48 8B C8                        mov rcx, rax
0033CEF3  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0033CEF7  49 33 CB                        xor rcx, r11
0033CEFA  48 8B D0                        mov rdx, rax
0033CEFD  48 23 4D 78                     and rcx, qword ptr [rbp + 0x78]
0033CF01  49 33 CB                        xor rcx, r11
0033CF04  F0 49 0F B1 48 28               lock cmpxchg qword ptr [r8 + 0x28], rcx
0033CF0A  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
0033CF0E  48 3B D0                        cmp rdx, rax
0033CF11  75 DD                           jne 0x14033cef0
0033CF13  49 B8 FF FF FF FF FF FF 7F F0   movabs r8, 0xf07fffffffffffff
0033CF1D  49 BB FF FF FF FF FF 00 00 F8   movabs r11, 0xf80000ffffffffff
0033CF27  4C 3B CE                        cmp r9, rsi
0033CF2A  0F 84 4A 03 00 00               je 0x14033d27a
0033CF30  4B 8D 34 49                     lea rsi, [r9 + r9*2]
0033CF34  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0033CF3E  48 C1 E6 04                     shl rsi, 4
0033CF42  48 8B C0                        mov rax, rax
0033CF45  4D 8B 5E 18                     mov r11, qword ptr [r14 + 0x18]
0033CF49  48 03 F0                        add rsi, rax
0033CF4C  48 B8 FF FF FF FF FF 00 00 F8   movabs rax, 0xf80000ffffffffff
0033CF56  4D 8B E3                        mov r12, r11
0033CF59  49 C1 E4 28                     shl r12, 0x28
0033CF5D  49 8B CC                        mov rcx, r12
0033CF60  48 8B 56 18                     mov rdx, qword ptr [rsi + 0x18]
0033CF64  48 33 CA                        xor rcx, rdx
0033CF67  48 23 C8                        and rcx, rax
0033CF6A  48 8B C2                        mov rax, rdx
0033CF6D  49 33 CC                        xor rcx, r12
0033CF70  F0 48 0F B1 4E 18               lock cmpxchg qword ptr [rsi + 0x18], rcx
0033CF76  4C 8B C0                        mov r8, rax
0033CF79  48 3B D0                        cmp rdx, rax
0033CF7C  0F 85 C0 01 00 00               jne 0x14033d142
0033CF82  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
0033CF85  49 B8 FF FF FF FF FF FF 7F F0   movabs r8, 0xf07fffffffffffff
0033CF8F  4C 8B A5 88 00 00 00            mov r12, qword ptr [rbp + 0x88]
0033CF96  49 C1 EB 13                     shr r11, 0x13
0033CF9A  44 33 D8                        xor r11d, eax
0033CF9D  41 81 E3 FF FF 1F 00            and r11d, 0x1fffff
0033CFA4  44 33 D8                        xor r11d, eax
0033CFA7  44 89 5E 24                     mov dword ptr [rsi + 0x24], r11d
0033CFAB  49 BB FF FF FF FF FF 00 00 F8   movabs r11, 0xf80000ffffffffff
0033CFB5  48 8B 0B                        mov rcx, qword ptr [rbx]
0033CFB8  0F 57 C0                        xorps xmm0, xmm0
0033CFBB  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
0033CFC5  48 C7 45 C0 00 00 00 00         mov qword ptr [rbp - 0x40], 0
0033CFCD  48 23 C8                        and rcx, rax
0033CFD0  0F 57 C9                        xorps xmm1, xmm1
0033CFD3  49 8B C1                        mov rax, r9
0033CFD6  48 C1 E0 28                     shl rax, 0x28
0033CFDA  48 0B C8                        or rcx, rax
0033CFDD  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
0033CFE0  48 89 0B                        mov qword ptr [rbx], rcx
0033CFE3  25 FF FF 1F 00                  and eax, 0x1fffff
0033CFE8  49 8B C9                        mov rcx, r9
0033CFEB  49 C1 E1 14                     shl r9, 0x14
0033CFEF  48 C1 E9 18                     shr rcx, 0x18
0033CFF3  C1 E1 15                        shl ecx, 0x15
0033CFF6  0B C8                           or ecx, eax
0033CFF8  89 4B 24                        mov dword ptr [rbx + 0x24], ecx
0033CFFB  48 8B 53 28                     mov rdx, qword ptr [rbx + 0x28]
0033CFFF  48 8B CA                        mov rcx, rdx
0033D002  48 89 55 E8                     mov qword ptr [rbp - 0x18], rdx
0033D006  49 33 C9                        xor rcx, r9
0033D009  48 8B C2                        mov rax, rdx
0033D00C  49 23 C8                        and rcx, r8
0033D00F  49 33 C9                        xor rcx, r9
0033D012  F3 0F 7F 45 C8                  movdqu xmmword ptr [rbp - 0x38], xmm0
0033D017  F3 0F 7F 4D D8                  movdqu xmmword ptr [rbp - 0x28], xmm1
0033D01C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0033D020  0F 11 45 00                     movups xmmword ptr [rbp], xmm0
0033D024  0F 11 45 10                     movups xmmword ptr [rbp + 0x10], xmm0
0033D028  F0 48 0F B1 4B 28               lock cmpxchg qword ptr [rbx + 0x28], rcx
0033D02E  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
0033D032  48 3B D0                        cmp rdx, rax
0033D035  74 2B                           je 0x14033d062
0033D037  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
0033D040  48 8B C8                        mov rcx, rax
0033D043  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0033D047  49 33 C9                        xor rcx, r9
0033D04A  48 8B D0                        mov rdx, rax
0033D04D  49 23 C8                        and rcx, r8
0033D050  49 33 C9                        xor rcx, r9
0033D053  F0 48 0F B1 4B 28               lock cmpxchg qword ptr [rbx + 0x28], rcx
0033D059  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
0033D05D  48 3B D0                        cmp rdx, rax
0033D060  75 DE                           jne 0x14033d040
0033D062  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
0033D066  4D 8B CA                        mov r9, r10
0033D069  49 C1 E1 28                     shl r9, 0x28
0033D06D  48 8B C2                        mov rax, rdx
0033D070  49 8B C9                        mov rcx, r9
0033D073  48 33 CA                        xor rcx, rdx
0033D076  49 23 CB                        and rcx, r11
0033D079  49 33 C9                        xor rcx, r9
0033D07C  F0 48 0F B1 4F 18               lock cmpxchg qword ptr [rdi + 0x18], rcx
0033D082  4C 8B C0                        mov r8, rax
0033D085  48 3B D0                        cmp rdx, rax
0033D088  0F 85 92 00 00 00               jne 0x14033d120
0033D08E  8B 47 24                        mov eax, dword ptr [rdi + 0x24]
0033D091  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0033D096  49 C1 EA 13                     shr r10, 0x13
0033D09A  44 33 D0                        xor r10d, eax
0033D09D  41 81 E2 FF FF 1F 00            and r10d, 0x1fffff
0033D0A4  44 33 D0                        xor r10d, eax
0033D0A7  44 89 57 24                     mov dword ptr [rdi + 0x24], r10d
0033D0AB  49 8B 06                        mov rax, qword ptr [r14]
0033D0AE  F0 48 01 01                     lock add qword ptr [rcx], rax
0033D0B2  4D 85 FF                        test r15, r15
0033D0B5  75 22                           jne 0x14033d0d9
0033D0B7  48 8B 03                        mov rax, qword ptr [rbx]
0033D0BA  48 33 45 70                     xor rax, qword ptr [rbp + 0x70]
0033D0BE  49 23 C5                        and rax, r13
0033D0C1  48 33 45 70                     xor rax, qword ptr [rbp + 0x70]
0033D0C5  48 89 03                        mov qword ptr [rbx], rax
0033D0C8  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0033D0CC  49 33 C4                        xor rax, r12
0033D0CF  49 23 C5                        and rax, r13
0033D0D2  49 33 C4                        xor rax, r12
0033D0D5  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
0033D0D9  4C 8B AC 24 28 01 00 00         mov r13, qword ptr [rsp + 0x128]
0033D0E1  48 8B B4 24 30 01 00 00         mov rsi, qword ptr [rsp + 0x130]
0033D0E9  48 81 C4 38 01 00 00            add rsp, 0x138
0033D0F0  41 5F                           pop r15
0033D0F2  41 5E                           pop r14
0033D0F4  41 5C                           pop r12
0033D0F6  5F                              pop rdi
0033D0F7  5B                              pop rbx
0033D0F8  5D                              pop rbp
0033D0F9  C3                              ret
0033D0FA  CC                              int3
0033D0FB  45 33 C9                        xor r9d, r9d
0033D0FE  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0033D103  BA 80 51 00 00                  mov edx, 0x5180
0033D108  41 8D 49 1A                     lea ecx, [r9 + 0x1a]
0033D10C  E8 4F 05 1C 00                  call 0x1404fd660
0033D111  CC                              int3
0033D112  0F 1F 40 00                     nop dword ptr [rax]
0033D116  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
0033D120  49 8B C8                        mov rcx, r8
0033D123  4D 33 C1                        xor r8, r9
0033D126  4D 23 C3                        and r8, r11
0033D129  48 8B C1                        mov rax, rcx
0033D12C  4D 33 C1                        xor r8, r9
0033D12F  F0 4C 0F B1 47 18               lock cmpxchg qword ptr [rdi + 0x18], r8
0033D135  4C 8B C0                        mov r8, rax
0033D138  48 3B C8                        cmp rcx, rax
0033D13B  75 E3                           jne 0x14033d120
0033D13D  E9 4C FF FF FF                  jmp 0x14033d08e
0033D142  49 BF FF FF FF FF FF 00 00 F8   movabs r15, 0xf80000ffffffffff
0033D14C  49 8B C8                        mov rcx, r8
0033D14F  4D 33 C4                        xor r8, r12
0033D152  4D 23 C7                        and r8, r15
0033D155  48 8B C1                        mov rax, rcx
0033D158  4D 33 C4                        xor r8, r12
0033D15B  F0 4C 0F B1 46 18               lock cmpxchg qword ptr [rsi + 0x18], r8
0033D161  4C 8B C0                        mov r8, rax
0033D164  48 3B C8                        cmp rcx, rax
0033D167  75 E3                           jne 0x14033d14c
0033D169  4C 8B BD 80 00 00 00            mov r15, qword ptr [rbp + 0x80]
0033D170  E9 0D FE FF FF                  jmp 0x14033cf82
0033D175  4B 8D 14 49                     lea rdx, [r9 + r9*2]
0033D179  48 C1 E2 04                     shl rdx, 4
0033D17D  49 8B C2                        mov rax, r10
0033D180  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
0033D184  48 03 D0                        add rdx, rax
0033D187  48 8B 02                        mov rax, qword ptr [rdx]
0033D18A  48 33 C1                        xor rax, rcx
0033D18D  49 23 C5                        and rax, r13
0033D190  48 33 C1                        xor rax, rcx
0033D193  48 89 02                        mov qword ptr [rdx], rax
0033D196  E9 70 FA FF FF                  jmp 0x14033cc0b
0033D19B  49 8B C2                        mov rax, r10
0033D19E  4C 3B C8                        cmp r9, rax
0033D1A1  73 3C                           jae 0x14033d1df
0033D1A3  49 B8 AB AA AA AA AA AA AA AA   movabs r8, 0xaaaaaaaaaaaaaaab
0033D1AD  BE 05 00 00 00                  mov esi, 5
0033D1B2  E9 09 FC FF FF                  jmp 0x14033cdc0
0033D1B7  4C 3B 40 10                     cmp r8, qword ptr [rax + 0x10]
0033D1BB  0F 82 BC FB FF FF               jb 0x14033cd7d
0033D1C1  44 8D 51 01                     lea r10d, [rcx + 1]
0033D1C5  E9 81 FB FF FF                  jmp 0x14033cd4b
0033D1CA  49 C1 FB 04                     sar r11, 4
0033D1CE  4D 0F AF D8                     imul r11, r8
0033D1D2  49 8B CB                        mov rcx, r11
0033D1D5  E8 6E C9 F7 FF                  call 0x1402b9b48
0033D1DA  E9 F5 FB FF FF                  jmp 0x14033cdd4
0033D1DF  48 8B 05 FA 0A AF 00            mov rax, qword ptr [rip + 0xaf0afa]
0033D1E6  48 8D 0C 40                     lea rcx, [rax + rax*2]
0033D1EA  48 C1 E1 04                     shl rcx, 4
0033D1EE  48 B8 30 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000030
0033D1F8  48 03 C8                        add rcx, rax
0033D1FB  49 B8 AB AA AA AA AA AA AA AA   movabs r8, 0xaaaaaaaaaaaaaaab
0033D205  4C 3B C9                        cmp r9, rcx
0033D208  73 A3                           jae 0x14033d1ad
0033D20A  49 8B CB                        mov rcx, r11
0033D20D  48 C1 F9 04                     sar rcx, 4
0033D211  49 0F AF C8                     imul rcx, r8
0033D215  E8 26 C0 F7 FF                  call 0x1402b9240
0033D21A  85 C0                           test eax, eax
0033D21C  75 8F                           jne 0x14033d1ad
0033D21E  8B C6                           mov eax, esi
0033D220  C1 E8 10                        shr eax, 0x10
0033D223  24 07                           and al, 7
0033D225  3C 06                           cmp al, 6
0033D227  0F 84 8D FB FF FF               je 0x14033cdba
0033D22D  49 8B C9                        mov rcx, r9
0033D230  E8 9B 10 F5 FF                  call 0x14028e2d0
0033D235  83 F8 09                        cmp eax, 9
0033D238  0F 85 7C FB FF FF               jne 0x14033cdba
0033D23E  8D 70 FC                        lea esi, [rax - 4]
0033D241  E9 7A FB FF FF                  jmp 0x14033cdc0
0033D246  85 C9                           test ecx, ecx
0033D248  0F 85 CE 00 00 00               jne 0x14033d31c
0033D24E  4C 8B C8                        mov r9, rax
0033D251  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0033D256  BA 80 51 00 00                  mov edx, 0x5180
0033D25B  B9 1A 00 00 00                  mov ecx, 0x1a
0033D260  E8 FB 03 1C 00                  call 0x1404fd660
0033D265  CC                              int3
0033D266  BE 05 00 00 00                  mov esi, 5
0033D26B  49 B8 AB AA AA AA AA AA AA AA   movabs r8, 0xaaaaaaaaaaaaaaab
0033D275  E9 46 FB FF FF                  jmp 0x14033cdc0
0033D27A  49 8B 4E 18                     mov rcx, qword ptr [r14 + 0x18]
0033D27E  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0033D283  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0033D287  E9 29 FD FF FF                  jmp 0x14033cfb5
0033D28C  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
0033D290  48 8B 0D F1 2D AF 00            mov rcx, qword ptr [rip + 0xaf2df1]
0033D297  48 C1 E8 2B                     shr rax, 0x2b
0033D29B  25 FF 03 00 00                  and eax, 0x3ff
0033D2A0  4C 8B 1C C1                     mov r11, qword ptr [rcx + rax*8]
0033D2A4  48 8B CF                        mov rcx, rdi
0033D2A7  E8 44 54 FE FF                  call 0x1403226f0
0033D2AC  44 8B D0                        mov r10d, eax
0033D2AF  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
0033D2B3  49 6B CA 58                     imul rcx, r10, 0x58
0033D2B7  4A 89 84 19 D8 0C 00 00         mov qword ptr [rcx + r11 + 0xcd8], rax
0033D2BF  E9 F8 F9 FF FF                  jmp 0x14033ccbc
0033D2C4  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
0033D2C8  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0033D2CD  48 89 48 10                     mov qword ptr [rax + 0x10], rcx
0033D2D1  E9 47 FC FF FF                  jmp 0x14033cf1d
0033D2D6  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
0033D2DA  48 8B 0D A7 2D AF 00            mov rcx, qword ptr [rip + 0xaf2da7]
0033D2E1  48 C1 E8 2B                     shr rax, 0x2b
0033D2E5  25 FF 03 00 00                  and eax, 0x3ff
0033D2EA  4C 8B 1C C1                     mov r11, qword ptr [rcx + rax*8]
0033D2EE  48 8B CF                        mov rcx, rdi
0033D2F1  E8 FA 53 FE FF                  call 0x1403226f0
0033D2F6  4C 8B 45 70                     mov r8, qword ptr [rbp + 0x70]
0033D2FA  49 B9 FF FF FF FF 3F 00 00 00   movabs r9, 0x3fffffffff
0033D304  44 8B D0                        mov r10d, eax
0033D307  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0033D30B  49 6B CA 58                     imul rcx, r10, 0x58
0033D30F  4A 89 84 19 D0 0C 00 00         mov qword ptr [rcx + r11 + 0xcd0], rax
0033D317  E9 6B F9 FF FF                  jmp 0x14033cc87
0033D31C  8D 51 FF                        lea edx, [rcx - 1]
0033D31F  E9 27 FA FF FF                  jmp 0x14033cd4b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiSharedInsertPfnChainInList(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m114;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m11C;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p8;
    unsigned __int8 v_stack_pB;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (312);
    v_stack_p18 = *(unsigned __int64 *)(a1 + 88);
    if (*(unsigned __int64 *)(a1 + 88) == 0) goto loc_0033CAFE;
    if ((*(unsigned __int64 *)(a1 + 16)) == a4) goto loc_0033CAFE;
loc_0033CAD0:
    a2 = (*(unsigned __int64 *)(a1 + 16) + *(unsigned __int64 *)(a1 + 16) * 2) << (4);
    a2 = (a2) + (v_r10);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32)));
    result = (*(unsigned __int64 *)(a2)) & (v_r11);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 32))) >> (24));
    a1 = (unsigned __int8)((a1) | (8));
    v_stack_pB = (unsigned __int8)(a1);
    *(unsigned int *)(a2 + 32) = (unsigned int)((unsigned int)(v_stack_p8));
    if (result != a4) goto loc_0033CAD0;
loc_0033CAFE:
    v_stack_m38 = v_rsi;
    v_stack_m40 = v_r13;
    v_rdi = (*(unsigned __int64 *)(a1 + 16) + *(unsigned __int64 *)(a1 + 16) * 2) << (4);
    v_rdi = (v_rdi) + (v_r10);
    v_rbx = (*(unsigned __int64 *)(a1 + 24) + *(unsigned __int64 *)(a1 + 24) * 2) << (4);
    v_rbx = (v_rbx) + (v_r10);
    v_stack_p8 = *(unsigned __int64 *)(a2 + 32);
    v_stack_p20 = *(unsigned __int64 *)(a2 + 8);
    if (*(unsigned __int64 *)(a1 + 88) == 0) goto loc_0033CC53;
    a2 = (*(unsigned __int64 *)(a1 + 88)) - (v_r10);
    a2 = (a2) >> (4);
    a2 = (a2) * ((unsigned int)(v_stack_p8));
    if (*(unsigned __int64 *)(v_rip + 11473172) == 0) goto loc_0033CB85;
    result = *(unsigned __int64 *)(v_rip + 11473172);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 16))) & (16)) == 0) {
        result = ~(*(unsigned __int64 *)(v_rip + 11473172));
        a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 16)) & (result);
    }
    result = (*(unsigned __int64 *)(v_rbx)) ^ (a2);
    a3 = (a3) >> (12);
    result = (result) & (v_r13);
    a3 = (a3) & (v_r11);
    result = (result) ^ (a2);
    a4 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 40)) & (v_r11);
    *(unsigned __int64 *)(v_rbx) = result;
    result = (*(unsigned __int64 *)(v_rdi + 24)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 40));
    result = (result) & (v_r13);
    result = (result) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 40));
    *(unsigned __int64 *)(v_rdi + 24) = result;
    if (a3 != a2) goto loc_0033D175;
    a2 = (*(unsigned __int64 *)(a1 + 16)) & (v_r11);
    a2 = (a2) << (12);
    result = (a2) | (0x880ULL);
    if (*(unsigned __int64 *)(v_rip + 11473068) != 0) {
        a1 = a2;
        a2 = (a2) | (0x890ULL);
        a1 = (a1) | (*(unsigned __int64 *)(v_rip + 11473068));
        a1 = (a1) | (0x880ULL);
        if (((result) & (*(unsigned __int64 *)(v_rip + 11473068))) == 0) { a2 = a1; }
        result = a2;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 16) = result;
loc_0033CC0B:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 40)) ^ (*(unsigned __int64 *)(a1 + 24));
    a1 = (a1) & (v_r13);
    a1 = (a1) ^ (*(unsigned __int64 *)(a1 + 24));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 40)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 40))) goto loc_0033CCBC;
loc_0033CC34:
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 40)) ^ (*(unsigned __int64 *)(a1 + 24));
    a3 = (a3) & (v_r13);
    a3 = (a3) ^ (*(unsigned __int64 *)(a1 + 24));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 40)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 40))) goto loc_0033CC34;
    goto loc_0033CCBC;
loc_0033CC53:
    if ((*(unsigned __int64 *)(a2 + 8)) == (*(unsigned __int64 *)(a1 + 24))) goto loc_0033D2D6;
    a2 = (*(unsigned __int64 *)(a2 + 8) + *(unsigned __int64 *)(a2 + 8) * 2) << (4);
    a2 = (a2) + (v_r10);
    result = (*(unsigned __int64 *)(a2)) ^ (*(unsigned __int64 *)(a1 + 16));
    result = (result) & (v_r13);
    result = (result) ^ (*(unsigned __int64 *)(a1 + 16));
    *(unsigned __int64 *)(a2) = result;
loc_0033CC87:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 40)) == (*(unsigned __int64 *)(a1 + 24))) goto loc_0033D28C;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 40) + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 40) * 2) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 40) + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 40) * 2);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 40) + a2 * 8)) ^ (*(unsigned __int64 *)(a1 + 24));
    result = (result) & (v_r13);
    result = (result) ^ (*(unsigned __int64 *)(a1 + 24));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 88) + 40) + a2 * 8) = result;
loc_0033CCBC:
    if ((*(unsigned int *)(a1 + 12)) != 2) goto loc_0033D0B2;
    v_stack_m128 = v_xmm0;
    v_r11 = (*(unsigned __int64 *)(a1 + 16) + *(unsigned __int64 *)(a1 + 16) * 2) << (4);
    v_stack_m118 = v_xmm1;
    v_rsi = 0;
    result = (*(unsigned __int64 *)(v_r11 + v_r10 * 1 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_m130 = v_r11 + v_r10 * 1;
    v_stack_m138 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11481989) + result * 8);
    if (((unsigned int)((int)(*(unsigned int *)(v_rip + 11472548)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11472541))))) goto loc_0033CD48;
    result = ((int)(*(unsigned int *)(v_rip + 11472548))) << (4);
    result = (result) + (*(unsigned __int64 *)(v_rip + 11472615));
    if ((*(unsigned __int64 *)(a1 + 16)) < (*(unsigned __int64 *)(result))) goto loc_0033CD48;
    if (((unsigned int)((int)(*(unsigned int *)(v_rip + 11472548)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11472541))))) goto loc_0033CD8D;
    if ((*(unsigned __int64 *)(a1 + 16)) < (*(unsigned __int64 *)(result + 16))) goto loc_0033CD8D;
loc_0033CD48:
loc_0033CD4B:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11472541)))) < 0) goto loc_0033D0FB;
    a1 = (unsigned int)((0 + (unsigned int)(*(unsigned int *)(v_rip + 11472541)) * 1) >> (1));
    result = ((int)((unsigned int)(a1))) << (4);
    result = (result) + (*(unsigned __int64 *)(v_rip + 11472568));
    if ((*(unsigned __int64 *)(a1 + 16)) < (*(unsigned __int64 *)(result))) goto loc_0033D246;
    if (((unsigned int)(a1)) != (*(unsigned int *)(v_rip + 11472461))) goto loc_0033D1B7;
loc_0033CD7D:
    *(unsigned int *)(v_rip + 11472445) = (unsigned int)(a1);
loc_0033CD8D:
    v_stack_m120 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 8)));
    if (*(unsigned __int64 *)(a1 + 88) != 0) goto loc_0033D266;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r11 + v_r10 * 1 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (8)) != 0) goto loc_0033D19B;
loc_0033CDBA:
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r11 + v_r10 * 1 + 32))) >> (24));
    v_rsi = (unsigned int)((v_rsi) & (7));
loc_0033CDC0:
    v_stack_m11C = (unsigned int)(v_rsi);
    if ((*(unsigned __int64 *)(v_rip + 11472480)) != 0) goto loc_0033D1CA;
    result = 0;
loc_0033CDD4:
    v_stack_m118 = 0;
    a1 = (0 * 8 + 59) + ((unsigned int)((unsigned int)(v_rsi)));
    v_stack_m114 = 9;
    a2 = ((unsigned int)(*(unsigned int *)(v_rip + 11472541))) * (a1);
    a1 = (a1) * ((unsigned int)(v_stack_m120));
    v_stack_p10 = *(unsigned __int64 *)(a1 + 16);
    a2 = (a2) + (a1);
    a2 = (a2) + (*(unsigned __int64 *)(v_stack_m138 + 16));
    v_stack_m128 = a2;
    if ((*(unsigned __int64 *)(v_stack_p10 + 56)) == v_rsi) goto loc_0033D2C4;
    a3 = (*(unsigned __int64 *)(v_stack_p10 + 56) + *(unsigned __int64 *)(v_stack_p10 + 56) * 2) << (4);
    a3 = (a3) + (v_stack_m138);
    v_stack_m108 = 0;
    a1 = (*(unsigned __int64 *)(a1 + 16)) << (40);
    result = (*(unsigned __int64 *)(a3)) & (a2);
    a1 = (a1) | (result);
    *(unsigned __int64 *)(a3) = a1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 36))) & (0x1FFFFFULL));
    v_r11 = (*(unsigned __int64 *)(a1 + 16)) << (20);
    a1 = (*(unsigned __int64 *)(a1 + 16)) >> (24);
    a1 = (unsigned int)((a1) << (21));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    *(unsigned int *)(a3 + 36) = (unsigned int)(a1);
    v_stack_mE0 = *(unsigned __int64 *)(a3 + 40);
    a1 = (*(unsigned __int64 *)(a3 + 40)) ^ (v_r11);
    a1 = (a1) & (result);
    a1 = (a1) ^ (v_r11);
    v_stack_m100 = v_xmm0;
    v_stack_mF0 = v_xmm1;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = v_xmm0;
    v_stack_mB0 = *(unsigned __int64 *)(a3 + 40);
    if ((*(unsigned __int64 *)(a3 + 40)) == (*(unsigned __int64 *)(a3 + 40))) goto loc_0033CF13;
loc_0033CEF0:
    v_stack_mE0 = *(unsigned __int64 *)(a3 + 40);
    a1 = (*(unsigned __int64 *)(a3 + 40)) ^ (v_r11);
    a1 = (a1) & (v_stack_p10);
    a1 = (a1) ^ (v_r11);
    v_stack_mB0 = *(unsigned __int64 *)(a3 + 40);
    if ((*(unsigned __int64 *)(a3 + 40)) != (*(unsigned __int64 *)(a3 + 40))) goto loc_0033CEF0;
loc_0033CF13:
loc_0033CF1D:
    if ((*(unsigned __int64 *)(v_stack_p10 + 80)) == v_rsi) goto loc_0033D27A;
    v_rsi = (*(unsigned __int64 *)(v_stack_p10 + 80) + *(unsigned __int64 *)(v_stack_p10 + 80) * 2) << (4);
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(a3 + 40));
    v_r12 = (*(unsigned __int64 *)(a1 + 24)) << (40);
    a1 = (v_r12) ^ (*(unsigned __int64 *)(v_rsi + 24));
    a1 = (a1) & (*(unsigned __int64 *)(a3 + 40));
    a1 = (a1) ^ (v_r12);
    if ((*(unsigned __int64 *)(v_rsi + 24)) != (*(unsigned __int64 *)(v_rsi + 24))) goto loc_0033D142;
loc_0033CF82:
    v_r11 = (*(unsigned __int64 *)(a1 + 24)) >> (19);
    v_r11 = (unsigned int)((v_r11) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 36)))));
    v_r11 = (unsigned int)((v_r11) & (0x1FFFFFULL));
    v_r11 = (unsigned int)((v_r11) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 36)))));
    *(unsigned int *)(v_rsi + 36) = (unsigned int)(v_r11);
loc_0033CFB5:
    v_stack_mA8 = 0;
    a1 = (*(unsigned __int64 *)(v_rbx)) & ((unsigned int)(*(unsigned int *)(v_rsi + 36)));
    result = (*(unsigned __int64 *)(v_stack_p10 + 80)) << (40);
    a1 = (a1) | (result);
    *(unsigned __int64 *)(v_rbx) = a1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 36))) & (0x1FFFFFULL));
    a4 = (*(unsigned __int64 *)(v_stack_p10 + 80)) << (20);
    a1 = (*(unsigned __int64 *)(v_stack_p10 + 80)) >> (24);
    a1 = (unsigned int)((a1) << (21));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    *(unsigned int *)(v_rbx + 36) = (unsigned int)(a1);
    v_stack_m80 = *(unsigned __int64 *)(v_rbx + 40);
    a1 = (*(unsigned __int64 *)(v_rbx + 40)) ^ (a4);
    a1 = (a1) & (*(unsigned __int64 *)(v_rsi + 24));
    a1 = (a1) ^ (a4);
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm1;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m50 = *(unsigned __int64 *)(v_rbx + 40);
    if ((*(unsigned __int64 *)(v_rbx + 40)) == (*(unsigned __int64 *)(v_rbx + 40))) goto loc_0033D062;
loc_0033D040:
    v_stack_m80 = *(unsigned __int64 *)(v_rbx + 40);
    a1 = (*(unsigned __int64 *)(v_rbx + 40)) ^ (a4);
    a1 = (a1) & (*(unsigned __int64 *)(v_rsi + 24));
    a1 = (a1) ^ (a4);
    v_stack_m50 = *(unsigned __int64 *)(v_rbx + 40);
    if ((*(unsigned __int64 *)(v_rbx + 40)) != (*(unsigned __int64 *)(v_rbx + 40))) goto loc_0033D040;
loc_0033D062:
    a4 = (*(unsigned __int64 *)(v_stack_p10 + 56)) << (40);
    a1 = (a4) ^ (*(unsigned __int64 *)(v_rdi + 24));
    a1 = (a1) & (v_r11);
    a1 = (a1) ^ (a4);
    if ((*(unsigned __int64 *)(v_rdi + 24)) != (*(unsigned __int64 *)(v_rdi + 24))) goto loc_0033D120;
loc_0033D08E:
    v_r10 = (*(unsigned __int64 *)(v_stack_p10 + 56)) >> (19);
    v_r10 = (unsigned int)((v_r10) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 36)))));
    v_r10 = (unsigned int)((v_r10) & (0x1FFFFFULL));
    v_r10 = (unsigned int)((v_r10) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 36)))));
    *(unsigned int *)(v_rdi + 36) = (unsigned int)(v_r10);
loc_0033D0B2:
    result = *(unsigned __int64 *)(a1);
    if (*(unsigned __int64 *)(a1 + 88) == 0) {
        result = *(unsigned __int64 *)(v_rbx);
        result = (result) ^ (v_stack_p8);
        result = (result) & (v_r13);
        result = (result) ^ (v_stack_p8);
        *(unsigned __int64 *)(v_rbx) = result;
        result = *(unsigned __int64 *)(v_rdi + 24);
        result = (result) ^ (v_stack_p20);
        result = (result) & (v_r13);
        result = (result) ^ (v_stack_p20);
        *(unsigned __int64 *)(v_rdi + 24) = result;
    }
    v_rsp = (v_rsp) + (312);
    return result;
loc_0033D0FB:
    a4 = 0;
    v_stack_p20 = v_stack_m38;
    result = KeBugCheckEx(a4 + 26, (unsigned int)(0x5180ULL), *(unsigned __int64 *)(v_rdi + 24), a4);
loc_0033D120:
    a3 = (*(unsigned __int64 *)(v_rdi + 24)) ^ (0);
    a3 = (a3) & (v_r11);
    a3 = (a3) ^ (0);
    if ((*(unsigned __int64 *)(v_rdi + 24)) != (*(unsigned __int64 *)(v_rdi + 24))) goto loc_0033D120;
    goto loc_0033D08E;
loc_0033D142:
loc_0033D14C:
    a3 = (*(unsigned __int64 *)(v_rdi + 24)) ^ (v_stack_p20);
    a3 = (a3) & (*(unsigned __int64 *)(a1 + 88));
    a3 = (a3) ^ (v_stack_p20);
    if ((*(unsigned __int64 *)(v_rdi + 24)) != (*(unsigned __int64 *)(v_rdi + 24))) goto loc_0033D14C;
    goto loc_0033CF82;
loc_0033D175:
    a2 = (a4 + a4 * 2) << (4);
    a2 = (a2) + (v_r10);
    result = (*(unsigned __int64 *)(a2)) ^ (*(unsigned __int64 *)(a1 + 16));
    result = (result) & (v_stack_m40);
    result = (result) ^ (*(unsigned __int64 *)(a1 + 16));
    *(unsigned __int64 *)(a2) = result;
    goto loc_0033CC0B;
loc_0033D19B:
    if (0 >= v_r10) goto loc_0033D1DF;
loc_0033D1AD:
    goto loc_0033CDC0;
loc_0033D1B7:
    if ((*(unsigned __int64 *)(v_rdi + 24)) < (*(unsigned __int64 *)(v_r10 + 16))) goto loc_0033CD7D;
    goto loc_0033CD4B;
loc_0033D1CA:
    v_r11 = (v_r11) >> (4);
    v_r11 = (v_r11) * (*(unsigned __int64 *)(v_rdi + 24));
    result = MiPageToChannel(v_r11, a2, *(unsigned __int64 *)(v_rdi + 24), a4);
    goto loc_0033CDD4;
loc_0033D1DF:
    a1 = (*(unsigned __int64 *)(v_rip + 11471610) + *(unsigned __int64 *)(v_rip + 11471610) * 2) << (4);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 11471610));
    if (0 >= a1) goto loc_0033D1AD;
    a1 = (v_r11) >> (4);
    a1 = (a1) * (*(unsigned __int64 *)(v_rdi + 24));
    result = MiIsDecayPfn(a1, a2, *(unsigned __int64 *)(v_rdi + 24), a4);
    if ((unsigned int)(result) != 0) goto loc_0033D1AD;
    result = (unsigned int)((5) >> (16));
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) == 6) goto loc_0033CDBA;
    result = MiGetPfnSlabType(0, a2, *(unsigned __int64 *)(v_rdi + 24), a4);
    if (((unsigned int)(result)) != 9) goto loc_0033CDBA;
    goto loc_0033CDC0;
loc_0033D246:
    if (0 != 0) goto loc_0033D31C;
    v_stack_p20 = result - 4;
    result = KeBugCheckEx(26, (unsigned int)(0x5180ULL), *(unsigned __int64 *)(v_rdi + 24), result);
loc_0033D266:
    goto loc_0033CDC0;
loc_0033D27A:
    *(unsigned __int64 *)(v_stack_p40 + 24) = *(unsigned __int64 *)(a1 + 24);
    goto loc_0033CFB5;
loc_0033D28C:
    result = (*(unsigned __int64 *)(v_rdi + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    result = MiGetPfnPriority(v_rdi, (unsigned int)(0x5180ULL), *(unsigned __int64 *)(v_rdi + 24), result);
    a1 = (v_rdi) * ((unsigned int)((unsigned int)(result)));
    *(unsigned __int64 *)(a1 + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11480561) + result * 8) * 1 + 3288) = *(unsigned __int64 *)(a1 + 24);
    goto loc_0033CCBC;
loc_0033D2C4:
    *(unsigned __int64 *)(v_stack_p40 + 16) = *(unsigned __int64 *)(a1 + 16);
    goto loc_0033CF1D;
loc_0033D2D6:
    result = (*(unsigned __int64 *)(v_rdi + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    result = MiGetPfnPriority(v_rdi, (unsigned int)(0x5180ULL), *(unsigned __int64 *)(v_rdi + 24), result);
    a1 = (v_rdi) * ((unsigned int)((unsigned int)(result)));
    *(unsigned __int64 *)(a1 + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11480487) + result * 8) * 1 + 3280) = *(unsigned __int64 *)(a1 + 16);
    goto loc_0033CC87;
loc_0033D31C:
    goto loc_0033CD4B;
}
```

## 5. (Beta) C Style

```c
int64_t MiSharedInsertPfnChainInList(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint32_t v_stack_m114;
    uint64_t v_stack_m118;
    uint32_t v_stack_m11C;
    uint32_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mF0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p40;
    uint32_t v_stack_p8;
    uint8_t v_stack_pB;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (312);
    v_stack_p18 = *(uint64_t *)(arg1 + 0x58);
    if (*(uint64_t *)(arg1 + 0x58) == 0) goto loc_0033CAFE;
    if ((*(uint64_t *)(arg1 + 0x10)) == a4) goto loc_0033CAFE;
loc_0033CAD0:
    Arg2 = (*(uint64_t *)(arg1 + 0x10) + *(uint64_t *)(arg1 + 0x10) * 2) << (4);
    Arg2 = (Arg2) + (local_r10);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20)));
    result = (*(uint64_t *)(arg2)) & (local_r11);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x20))) >> (24));
    Arg1 = (uint8_t)((Arg1) | (8));
    v_stack_pB = (uint8_t)(Arg1);
    *(uint32_t *)(arg2 + 0x20) = (uint32_t)((uint32_t)(v_stack_p8));
    if (result != a4) goto loc_0033CAD0;
loc_0033CAFE:
    v_stack_m38 = local_rsi;
    v_stack_m40 = local_r13;
    local_rdi = (*(uint64_t *)(arg1 + 0x10) + *(uint64_t *)(arg1 + 0x10) * 2) << (4);
    local_rdi = (local_rdi) + (local_r10);
    local_rbx = (*(uint64_t *)(arg1 + 0x18) + *(uint64_t *)(arg1 + 0x18) * 2) << (4);
    local_rbx = (local_rbx) + (local_r10);
    v_stack_p8 = *(uint64_t *)(arg2 + 0x20);
    v_stack_p20 = *(uint64_t *)(arg2 + 0x8);
    if (*(uint64_t *)(arg1 + 0x58) == 0) goto loc_0033CC53;
    Arg2 = (*(uint64_t *)(arg1 + 0x58)) - (local_r10);
    Arg2 = (Arg2) >> (4);
    Arg2 = (Arg2) * ((uint32_t)(v_stack_p8));
    if (*(uint64_t *)(v_rip + 0xAF1114) == 0) goto loc_0033CB85;
    result = *(uint64_t *)(v_rip + 0xAF1114);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x10))) & (16)) == 0) {
        result = ~(*(uint64_t *)(v_rip + 0xAF1114));
        a3 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x10)) & (result);
    }
    result = (*(uint64_t *)(local_rbx)) ^ (Arg2);
    a3 = (a3) >> (12);
    result = (result) & (local_r13);
    a3 = (a3) & (local_r11);
    result = (result) ^ (Arg2);
    a4 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x28)) & (local_r11);
    *(uint64_t *)(local_rbx) = result;
    result = (*(uint64_t *)(local_rdi + 0x18)) ^ (*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x28));
    result = (result) & (local_r13);
    result = (result) ^ (*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x28));
    *(uint64_t *)(local_rdi + 0x18) = result;
    if (a3 != Arg2) goto loc_0033D175;
    Arg2 = (*(uint64_t *)(arg1 + 0x10)) & (local_r11);
    Arg2 = (Arg2) << (12);
    result = (Arg2) | (0x880ULL);
    if (*(uint64_t *)(v_rip + 0xAF10AC) != 0) {
        Arg1 = Arg2;
        Arg2 = (Arg2) | (0x890ULL);
        Arg1 = (Arg1) | (*(uint64_t *)(v_rip + 0xAF10AC));
        Arg1 = (Arg1) | (0x880ULL);
        if (((result) & (*(uint64_t *)(v_rip + 0xAF10AC))) == 0) { Arg2 = Arg1; }
        result = Arg2;
    }
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x10) = result;
loc_0033CC0B:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x28)) ^ (*(uint64_t *)(arg1 + 0x18));
    Arg1 = (Arg1) & (local_r13);
    Arg1 = (Arg1) ^ (*(uint64_t *)(arg1 + 0x18));
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x28)) == (*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x28))) goto loc_0033CCBC;
loc_0033CC34:
    a3 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x28)) ^ (*(uint64_t *)(arg1 + 0x18));
    a3 = (a3) & (local_r13);
    a3 = (a3) ^ (*(uint64_t *)(arg1 + 0x18));
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x28)) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x28))) goto loc_0033CC34;
    goto loc_0033CCBC;
loc_0033CC53:
    if ((*(uint64_t *)(arg2 + 0x8)) == (*(uint64_t *)(arg1 + 0x18))) goto loc_0033D2D6;
    Arg2 = (*(uint64_t *)(arg2 + 0x8) + *(uint64_t *)(arg2 + 0x8) * 2) << (4);
    Arg2 = (Arg2) + (local_r10);
    result = (*(uint64_t *)(arg2)) ^ (*(uint64_t *)(arg1 + 0x10));
    result = (result) & (local_r13);
    result = (result) ^ (*(uint64_t *)(arg1 + 0x10));
    *(uint64_t *)(arg2) = result;
loc_0033CC87:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x28)) == (*(uint64_t *)(arg1 + 0x18))) goto loc_0033D28C;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x28) + *(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x28) * 2) + (*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x28) + *(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x28) * 2);
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x28) + arg2 * 8)) ^ (*(uint64_t *)(arg1 + 0x18));
    result = (result) & (local_r13);
    result = (result) ^ (*(uint64_t *)(arg1 + 0x18));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x58) + 0x28) + arg2 * 8) = result;
loc_0033CCBC:
    if ((*(uint32_t *)(arg1 + 0xC)) != 2) goto loc_0033D0B2;
    v_stack_m128 = v_xmm0;
    local_r11 = (*(uint64_t *)(arg1 + 0x10) + *(uint64_t *)(arg1 + 0x10) * 2) << (4);
    v_stack_m118 = v_xmm1;
    local_rsi = 0;
    result = (*(uint64_t *)(local_r11 + local_r10 * 1 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_m130 = local_r11 + local_r10 * 1;
    v_stack_m138 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xAF3385) + result * 8);
    if (((uint32_t)((int32_t)(*(uint32_t *)(v_rip + 0xAF0EA4)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAF0E9D))))) goto loc_0033CD48;
    result = ((int32_t)(*(uint32_t *)(v_rip + 0xAF0EA4))) << (4);
    result = (result) + (*(uint64_t *)(v_rip + 0xAF0EE7));
    if ((*(uint64_t *)(arg1 + 0x10)) < (*(uint64_t *)(result))) goto loc_0033CD48;
    if (((uint32_t)((int32_t)(*(uint32_t *)(v_rip + 0xAF0EA4)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAF0E9D))))) goto loc_0033CD8D;
    if ((*(uint64_t *)(arg1 + 0x10)) < (*(uint64_t *)(result + 0x10))) goto loc_0033CD8D;
loc_0033CD48:
loc_0033CD4B:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAF0E9D)))) < 0) goto loc_0033D0FB;
    Arg1 = (uint32_t)((0 + (uint32_t)(*(uint32_t *)(v_rip + 0xAF0E9D)) * 1) >> (1));
    result = ((int32_t)((uint32_t)(Arg1))) << (4);
    result = (result) + (*(uint64_t *)(v_rip + 0xAF0EB8));
    if ((*(uint64_t *)(arg1 + 0x10)) < (*(uint64_t *)(result))) goto loc_0033D246;
    if (((uint32_t)(Arg1)) != (*(uint32_t *)(v_rip + 0xAF0E4D))) goto loc_0033D1B7;
loc_0033CD7D:
    *(uint32_t *)(v_rip + 0xAF0E3D) = (uint32_t)(Arg1);
loc_0033CD8D:
    v_stack_m120 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)));
    if (*(uint64_t *)(arg1 + 0x58) != 0) goto loc_0033D266;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r11 + local_r10 * 1 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (8)) != 0) goto loc_0033D19B;
loc_0033CDBA:
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r11 + local_r10 * 1 + 0x20))) >> (24));
    local_rsi = (uint32_t)((local_rsi) & (7));
loc_0033CDC0:
    v_stack_m11C = (uint32_t)(local_rsi);
    if ((*(uint64_t *)(v_rip + 0xAF0E60)) != 0) goto loc_0033D1CA;
    result = 0;
loc_0033CDD4:
    v_stack_m118 = 0;
    Arg1 = (0 * 8 + 59) + ((uint32_t)((uint32_t)(local_rsi)));
    v_stack_m114 = 9;
    Arg2 = ((uint32_t)(*(uint32_t *)(v_rip + 0xAF0E9D))) * (Arg1);
    Arg1 = (Arg1) * ((uint32_t)(v_stack_m120));
    v_stack_p10 = *(uint64_t *)(arg1 + 0x10);
    Arg2 = (Arg2) + (Arg1);
    Arg2 = (Arg2) + (*(uint64_t *)(v_stack_m138 + 0x10));
    v_stack_m128 = Arg2;
    if ((*(uint64_t *)(v_stack_p10 + 0x38)) == local_rsi) goto loc_0033D2C4;
    a3 = (*(uint64_t *)(v_stack_p10 + 0x38) + *(uint64_t *)(v_stack_p10 + 0x38) * 2) << (4);
    a3 = (a3) + (v_stack_m138);
    v_stack_m108 = 0;
    Arg1 = (*(uint64_t *)(arg1 + 0x10)) << (40);
    result = (*(uint64_t *)(a3)) & (Arg2);
    Arg1 = (Arg1) | (result);
    *(void **)(a3) = Arg1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(a3 + 0x24))) & (0x1FFFFFULL));
    local_r11 = (*(uint64_t *)(arg1 + 0x10)) << (20);
    Arg1 = (*(uint64_t *)(arg1 + 0x10)) >> (24);
    Arg1 = (uint32_t)((Arg1) << (21));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    *(uint32_t *)(a3 + 0x24) = (uint32_t)(Arg1);
    v_stack_mE0 = *(uint64_t *)(a3 + 0x28);
    Arg1 = (*(uint64_t *)(a3 + 0x28)) ^ (local_r11);
    Arg1 = (Arg1) & (result);
    Arg1 = (Arg1) ^ (local_r11);
    v_stack_m100 = v_xmm0;
    v_stack_mF0 = v_xmm1;
    v_stack_mD8 = v_xmm0;
    v_stack_mC8 = v_xmm0;
    v_stack_mB8 = v_xmm0;
    v_stack_mB0 = *(uint64_t *)(a3 + 0x28);
    if ((*(uint64_t *)(a3 + 0x28)) == (*(uint64_t *)(a3 + 0x28))) goto loc_0033CF13;
loc_0033CEF0:
    v_stack_mE0 = *(uint64_t *)(a3 + 0x28);
    Arg1 = (*(uint64_t *)(a3 + 0x28)) ^ (local_r11);
    Arg1 = (Arg1) & (v_stack_p10);
    Arg1 = (Arg1) ^ (local_r11);
    v_stack_mB0 = *(uint64_t *)(a3 + 0x28);
    if ((*(uint64_t *)(a3 + 0x28)) != (*(uint64_t *)(a3 + 0x28))) goto loc_0033CEF0;
loc_0033CF13:
loc_0033CF1D:
    if ((*(uint64_t *)(v_stack_p10 + 0x50)) == local_rsi) goto loc_0033D27A;
    local_rsi = (*(uint64_t *)(v_stack_p10 + 0x50) + *(uint64_t *)(v_stack_p10 + 0x50) * 2) << (4);
    local_rsi = (local_rsi) + (*(uint64_t *)(a3 + 0x28));
    local_r12 = (*(uint64_t *)(arg1 + 0x18)) << (40);
    Arg1 = (local_r12) ^ (*(uint64_t *)(local_rsi + 0x18));
    Arg1 = (Arg1) & (*(uint64_t *)(a3 + 0x28));
    Arg1 = (Arg1) ^ (local_r12);
    if ((*(uint64_t *)(local_rsi + 0x18)) != (*(uint64_t *)(local_rsi + 0x18))) goto loc_0033D142;
loc_0033CF82:
    local_r11 = (*(uint64_t *)(arg1 + 0x18)) >> (19);
    local_r11 = (uint32_t)((local_r11) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x24)))));
    local_r11 = (uint32_t)((local_r11) & (0x1FFFFFULL));
    local_r11 = (uint32_t)((local_r11) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x24)))));
    *(uint32_t *)(local_rsi + 0x24) = (uint32_t)(local_r11);
loc_0033CFB5:
    v_stack_mA8 = 0;
    Arg1 = (*(uint64_t *)(local_rbx)) & ((uint32_t)(*(uint32_t *)(local_rsi + 0x24)));
    result = (*(uint64_t *)(v_stack_p10 + 0x50)) << (40);
    Arg1 = (Arg1) | (result);
    *(void **)(local_rbx) = Arg1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x24))) & (0x1FFFFFULL));
    a4 = (*(uint64_t *)(v_stack_p10 + 0x50)) << (20);
    Arg1 = (*(uint64_t *)(v_stack_p10 + 0x50)) >> (24);
    Arg1 = (uint32_t)((Arg1) << (21));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    *(uint32_t *)(local_rbx + 0x24) = (uint32_t)(Arg1);
    v_stack_m80 = *(uint64_t *)(local_rbx + 0x28);
    Arg1 = (*(uint64_t *)(local_rbx + 0x28)) ^ (a4);
    Arg1 = (Arg1) & (*(uint64_t *)(local_rsi + 0x18));
    Arg1 = (Arg1) ^ (a4);
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm1;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m50 = *(uint64_t *)(local_rbx + 0x28);
    if ((*(uint64_t *)(local_rbx + 0x28)) == (*(uint64_t *)(local_rbx + 0x28))) goto loc_0033D062;
loc_0033D040:
    v_stack_m80 = *(uint64_t *)(local_rbx + 0x28);
    Arg1 = (*(uint64_t *)(local_rbx + 0x28)) ^ (a4);
    Arg1 = (Arg1) & (*(uint64_t *)(local_rsi + 0x18));
    Arg1 = (Arg1) ^ (a4);
    v_stack_m50 = *(uint64_t *)(local_rbx + 0x28);
    if ((*(uint64_t *)(local_rbx + 0x28)) != (*(uint64_t *)(local_rbx + 0x28))) goto loc_0033D040;
loc_0033D062:
    a4 = (*(uint64_t *)(v_stack_p10 + 0x38)) << (40);
    Arg1 = (a4) ^ (*(uint64_t *)(local_rdi + 0x18));
    Arg1 = (Arg1) & (local_r11);
    Arg1 = (Arg1) ^ (a4);
    if ((*(uint64_t *)(local_rdi + 0x18)) != (*(uint64_t *)(local_rdi + 0x18))) goto loc_0033D120;
loc_0033D08E:
    local_r10 = (*(uint64_t *)(v_stack_p10 + 0x38)) >> (19);
    local_r10 = (uint32_t)((local_r10) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x24)))));
    local_r10 = (uint32_t)((local_r10) & (0x1FFFFFULL));
    local_r10 = (uint32_t)((local_r10) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x24)))));
    *(uint32_t *)(local_rdi + 0x24) = (uint32_t)(local_r10);
loc_0033D0B2:
    result = *(uint64_t *)(arg1);
    if (*(uint64_t *)(arg1 + 0x58) == 0) {
        result = *(uint64_t *)(local_rbx);
        result = (result) ^ (v_stack_p8);
        result = (result) & (local_r13);
        result = (result) ^ (v_stack_p8);
        *(uint64_t *)(local_rbx) = result;
        result = *(uint64_t *)(local_rdi + 0x18);
        result = (result) ^ (v_stack_p20);
        result = (result) & (local_r13);
        result = (result) ^ (v_stack_p20);
        *(uint64_t *)(local_rdi + 0x18) = result;
    }
    local_rsp = (local_rsp) + (312);
    return result;
loc_0033D0FB:
    a4 = 0;
    v_stack_p20 = v_stack_m38;
    result = KeBugCheckEx(a4 + 26, (uint32_t)(0x5180ULL), *(uint64_t *)(local_rdi + 0x18), a4);
loc_0033D120:
    a3 = (*(uint64_t *)(local_rdi + 0x18)) ^ (0);
    a3 = (a3) & (local_r11);
    a3 = (a3) ^ (0);
    if ((*(uint64_t *)(local_rdi + 0x18)) != (*(uint64_t *)(local_rdi + 0x18))) goto loc_0033D120;
    goto loc_0033D08E;
loc_0033D142:
loc_0033D14C:
    a3 = (*(uint64_t *)(local_rdi + 0x18)) ^ (v_stack_p20);
    a3 = (a3) & (*(uint64_t *)(arg1 + 0x58));
    a3 = (a3) ^ (v_stack_p20);
    if ((*(uint64_t *)(local_rdi + 0x18)) != (*(uint64_t *)(local_rdi + 0x18))) goto loc_0033D14C;
    goto loc_0033CF82;
loc_0033D175:
    Arg2 = (a4 + a4 * 2) << (4);
    Arg2 = (Arg2) + (local_r10);
    result = (*(uint64_t *)(arg2)) ^ (*(uint64_t *)(arg1 + 0x10));
    result = (result) & (v_stack_m40);
    result = (result) ^ (*(uint64_t *)(arg1 + 0x10));
    *(uint64_t *)(arg2) = result;
    goto loc_0033CC0B;
loc_0033D19B:
    if (0 >= local_r10) goto loc_0033D1DF;
loc_0033D1AD:
    goto loc_0033CDC0;
loc_0033D1B7:
    if ((*(uint64_t *)(local_rdi + 0x18)) < (*(uint64_t *)(local_r10 + 0x10))) goto loc_0033CD7D;
    goto loc_0033CD4B;
loc_0033D1CA:
    local_r11 = (local_r11) >> (4);
    local_r11 = (local_r11) * (*(uint64_t *)(local_rdi + 0x18));
    result = MiPageToChannel(local_r11, Arg2, *(uint64_t *)(local_rdi + 0x18), a4);
    goto loc_0033CDD4;
loc_0033D1DF:
    Arg1 = (*(uint64_t *)(v_rip + 0xAF0AFA) + *(uint64_t *)(v_rip + 0xAF0AFA) * 2) << (4);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xAF0AFA));
    if (0 >= Arg1) goto loc_0033D1AD;
    Arg1 = (local_r11) >> (4);
    Arg1 = (Arg1) * (*(uint64_t *)(local_rdi + 0x18));
    result = MiIsDecayPfn(Arg1, Arg2, *(uint64_t *)(local_rdi + 0x18), a4);
    if ((uint32_t)(result) != 0) goto loc_0033D1AD;
    result = (uint32_t)((5) >> (16));
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) == 6) goto loc_0033CDBA;
    result = MiGetPfnSlabType(0, Arg2, *(uint64_t *)(local_rdi + 0x18), a4);
    if (((uint32_t)(result)) != 9) goto loc_0033CDBA;
    goto loc_0033CDC0;
loc_0033D246:
    if (0 != 0) goto loc_0033D31C;
    v_stack_p20 = result - 4;
    result = KeBugCheckEx(26, (uint32_t)(0x5180ULL), *(uint64_t *)(local_rdi + 0x18), result);
loc_0033D266:
    goto loc_0033CDC0;
loc_0033D27A:
    *(uint64_t *)(v_stack_p40 + 0x18) = *(uint64_t *)(arg1 + 0x18);
    goto loc_0033CFB5;
loc_0033D28C:
    result = (*(uint64_t *)(local_rdi + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    result = MiGetPfnPriority(local_rdi, (uint32_t)(0x5180ULL), *(uint64_t *)(local_rdi + 0x18), result);
    Arg1 = (local_rdi) * ((uint32_t)((uint32_t)(result)));
    *(uint64_t *)(arg1 + *(uint64_t *)(*(uint64_t *)(v_rip + 0xAF2DF1) + result * 8) * 1 + 0xCD8) = *(uint64_t *)(arg1 + 0x18);
    goto loc_0033CCBC;
loc_0033D2C4:
    *(uint64_t *)(v_stack_p40 + 0x10) = *(uint64_t *)(arg1 + 0x10);
    goto loc_0033CF1D;
loc_0033D2D6:
    result = (*(uint64_t *)(local_rdi + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    result = MiGetPfnPriority(local_rdi, (uint32_t)(0x5180ULL), *(uint64_t *)(local_rdi + 0x18), result);
    Arg1 = (local_rdi) * ((uint32_t)((uint32_t)(result)));
    *(uint64_t *)(arg1 + *(uint64_t *)(*(uint64_t *)(v_rip + 0xAF2DA7) + result * 8) * 1 + 0xCD0) = *(uint64_t *)(arg1 + 0x10);
    goto loc_0033CC87;
loc_0033D31C:
    goto loc_0033CD4B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0033CA70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
