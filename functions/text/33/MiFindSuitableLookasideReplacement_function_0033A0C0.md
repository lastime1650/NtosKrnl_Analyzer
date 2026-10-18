# MiFindSuitableLookasideReplacement

- RVA: `0x0033A0C0`–`0x0033A956` (길이 `2,198` bytes)
- VA: `0x000000014033A0C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076C40`
- 디코드: `484`개 명령, `2,198/2,198` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x0033A577` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0033A632` → [MiGetStandbyPageType](../3D/MiGetStandbyPageType_function_003D55B0.md) (function, `0x003D55B0`)
- `0x0033A72D` → [MiSearchChannelTable](MiSearchChannelTable_function_0033BE24.md) (function, `0x0033BE24`)
- `0x0033A7AA` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x0033A7D7` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0033A8A2` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x0033A8CA` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)

### Direct callers
- [sub_00338E63](Unknown_function_00338E63.md) at `0x003391F1`
- [sub_00339916](Unknown_function_00339916.md) at `0x00339A71`

### Static image references
- `0x0033A11E` → RVA `0x00E35C00` (`.data`; read)
- `0x0033A3B7` → RVA `0x00E3CBE6` (`.data`; read)
- `0x0033A3CE` → RVA `0x00E3D240` (`.data`; read)
- `0x0033A3FC` → RVA `0x00E30088` (`.data`; read)
- `0x0033A415` → RVA `0x00E2DBC0` (`.data`; read)
- `0x0033A421` → RVA `0x00E2DBC4` (`.data`; read)
- `0x0033A432` → RVA `0x00E2DC20` (`.data`; read)
- `0x0033A47D` → RVA `0x00E2DBC0` (`.data`; write)
- `0x0033A4B8` → RVA `0x00E2DC28` (`.data`; read)
- `0x0033A74E` → RVA `0x00E2DCE0` (`.data`; read)
- `0x0033A845` → RVA `0x00E2DC80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0033A0C0  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
0033A0C5  53                              push rbx
0033A0C6  56                              push rsi
0033A0C7  57                              push rdi
0033A0C8  41 54                           push r12
0033A0CA  41 55                           push r13
0033A0CC  41 56                           push r14
0033A0CE  41 57                           push r15
0033A0D0  48 83 EC 60                     sub rsp, 0x60
0033A0D4  45 33 ED                        xor r13d, r13d
0033A0D7  4C 8B F2                        mov r14, rdx
0033A0DA  41 8B F5                        mov esi, r13d
0033A0DD  4C 89 AC 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r13
0033A0E5  41 8B FD                        mov edi, r13d
0033A0E8  48 BA 00 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000000
0033A0F2  44 8B D9                        mov r11d, ecx
0033A0F5  49 BC FF FF FF FF 3F 00 00 00   movabs r12, 0x3fffffffff
0033A0FF  48 8B C2                        mov rax, rdx
0033A102  4D 8B D1                        mov r10, r9
0033A105  4C 2B D0                        sub r10, rax
0033A108  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
0033A112  49 C1 FA 04                     sar r10, 4
0033A116  4C 0F AF D0                     imul r10, rax
0033A11A  85 C9                           test ecx, ecx
0033A11C  75 39                           jne 0x14033a157
0033A11E  48 8B 05 DB BA AF 00            mov rax, qword ptr [rip + 0xafbadb]
0033A125  4C 3B D0                        cmp r10, rax
0033A128  72 11                           jb 0x14033a13b
0033A12A  48 05 00 08 00 00               add rax, 0x800
0033A130  4C 3B D0                        cmp r10, rax
0033A133  73 06                           jae 0x14033a13b
0033A135  44 8D 79 01                     lea r15d, [rcx + 1]
0033A139  EB 1F                           jmp 0x14033a15a
0033A13B  4B 8D 0C 52                     lea rcx, [r10 + r10*2]
0033A13F  48 C1 E1 04                     shl rcx, 4
0033A143  48 8B C2                        mov rax, rdx
0033A146  48 03 C8                        add rcx, rax
0033A149  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
0033A14C  C1 E8 18                        shr eax, 0x18
0033A14F  A8 08                           test al, 8
0033A151  0F 85 73 07 00 00               jne 0x14033a8ca
0033A157  45 8B FD                        mov r15d, r13d
0033A15A  44 89 BC 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r15d
0033A162  4D 8B C5                        mov r8, r13
0033A165  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
0033A16F  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
0033A179  49 83 F8 10                     cmp r8, 0x10
0033A17D  0F 83 AA 03 00 00               jae 0x14033a52d
0033A183  45 85 DB                        test r11d, r11d
0033A186  0F 85 74 01 00 00               jne 0x14033a300
0033A18C  49 FF C0                        inc r8
0033A18F  85 FF                           test edi, edi
0033A191  0F 85 46 06 00 00               jne 0x14033a7dd
0033A197  49 8B 19                        mov rbx, qword ptr [r9]
0033A19A  48 23 DA                        and rbx, rdx
0033A19D  49 8B C4                        mov rax, r12
0033A1A0  48 3B D8                        cmp rbx, rax
0033A1A3  0F 84 F9 03 00 00               je 0x14033a5a2
0033A1A9  48 8D 0C 5B                     lea rcx, [rbx + rbx*2]
0033A1AD  49 B9 00 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000000
0033A1B7  48 03 C9                        add rcx, rcx
0033A1BA  49 8B C1                        mov rax, r9
0033A1BD  48 8D 14 C8                     lea rdx, [rax + rcx*8]
0033A1C1  48 8B 05 38 BA AF 00            mov rax, qword ptr [rip + 0xafba38]
0033A1C8  48 3B D8                        cmp rbx, rax
0033A1CB  72 0F                           jb 0x14033a1dc
0033A1CD  48 05 00 08 00 00               add rax, 0x800
0033A1D3  48 3B D8                        cmp rbx, rax
0033A1D6  0F 82 A1 03 00 00               jb 0x14033a57d
0033A1DC  48 8B 05 1D BA AF 00            mov rax, qword ptr [rip + 0xafba1d]
0033A1E3  48 3B D8                        cmp rbx, rax
0033A1E6  0F 82 F1 03 00 00               jb 0x14033a5dd
0033A1EC  48 05 00 08 00 00               add rax, 0x800
0033A1F2  48 3B D8                        cmp rbx, rax
0033A1F5  0F 83 E2 03 00 00               jae 0x14033a5dd
0033A1FB  C7 84 24 A0 00 00 00 01 00 00 00  mov dword ptr [rsp + 0xa0], 1
0033A206  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
0033A210  49 8B C4                        mov rax, r12
0033A213  48 3B D8                        cmp rbx, rax
0033A216  0F 84 86 03 00 00               je 0x14033a5a2
0033A21C  48 8D 0C 5B                     lea rcx, [rbx + rbx*2]
0033A220  49 B9 00 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000000
0033A22A  48 03 C9                        add rcx, rcx
0033A22D  49 8B C1                        mov rax, r9
0033A230  48 8D 14 C8                     lea rdx, [rax + rcx*8]
0033A234  44 39 AC 24 C0 00 00 00         cmp dword ptr [rsp + 0xc0], r13d
0033A23C  0F 84 8D 00 00 00               je 0x14033a2cf
0033A242  49 83 F8 01                     cmp r8, 1
0033A246  0F 87 83 00 00 00               ja 0x14033a2cf
0033A24C  45 85 DB                        test r11d, r11d
0033A24F  0F 84 BB 03 00 00               je 0x14033a610
0033A255  48 8B 05 A4 B9 AF 00            mov rax, qword ptr [rip + 0xafb9a4]
0033A25C  48 3B D8                        cmp rbx, rax
0033A25F  72 0B                           jb 0x14033a26c
0033A261  48 05 00 08 00 00               add rax, 0x800
0033A267  48 3B D8                        cmp rbx, rax
0033A26A  72 2B                           jb 0x14033a297
0033A26C  48 B8 10 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000010
0033A276  48 8B C0                        mov rax, rax
0033A279  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
0033A27D  48 0F BA E1 0A                  bt rcx, 0xa
0033A282  0F 83 33 04 00 00               jae 0x14033a6bb
0033A288  48 C1 E9 03                     shr rcx, 3
0033A28C  F7 D1                           not ecx
0033A28E  F6 C1 01                        test cl, 1
0033A291  0F 85 8A 00 00 00               jne 0x14033a321
0033A297  41 8B D5                        mov edx, r13d
0033A29A  49 8B CE                        mov rcx, r14
0033A29D  48 8B 01                        mov rax, qword ptr [rcx]
0033A2A0  48 3B C3                        cmp rax, rbx
0033A2A3  74 0D                           je 0x14033a2b2
0033A2A5  FF C2                           inc edx
0033A2A7  48 83 C1 08                     add rcx, 8
0033A2AB  83 FA 40                        cmp edx, 0x40
0033A2AE  74 71                           je 0x14033a321
0033A2B0  72 EB                           jb 0x14033a29d
0033A2B2  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
0033A2BC  4C 8D 0C 5B                     lea r9, [rbx + rbx*2]
0033A2C0  49 C1 E1 04                     shl r9, 4
0033A2C4  48 8B C1                        mov rax, rcx
0033A2C7  4C 03 C8                        add r9, rax
0033A2CA  E9 A0 FE FF FF                  jmp 0x14033a16f
0033A2CF  F0 48 0F BA 6A 18 3F            lock bts qword ptr [rdx + 0x18], 0x3f
0033A2D6  0F 82 BC 02 00 00               jb 0x14033a598
0033A2DC  48 85 F6                        test rsi, rsi
0033A2DF  74 0F                           je 0x14033a2f0
0033A2E1  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0033A2EB  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
0033A2F0  48 8B F2                        mov rsi, rdx
0033A2F3  48 89 94 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdx
0033A2FB  E9 4C FF FF FF                  jmp 0x14033a24c
0033A300  41 83 FB 01                     cmp r11d, 1
0033A304  0F 85 39 03 00 00               jne 0x14033a643
0033A30A  49 FF C0                        inc r8
0033A30D  85 FF                           test edi, edi
0033A30F  0F 85 31 04 00 00               jne 0x14033a746
0033A315  49 8B 59 18                     mov rbx, qword ptr [r9 + 0x18]
0033A319  48 23 DA                        and rbx, rdx
0033A31C  E9 EF FE FF FF                  jmp 0x14033a210
0033A321  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
0033A328  4D 8B 04 C6                     mov r8, qword ptr [r14 + rax*8]
0033A32C  49 89 1C C6                     mov qword ptr [r14 + rax*8], rbx
0033A330  49 83 F8 FF                     cmp r8, -1
0033A334  0F 84 FA 05 00 00               je 0x14033a934
0033A33A  48 8B 15 BF B8 AF 00            mov rdx, qword ptr [rip + 0xafb8bf]
0033A341  4C 3B C2                        cmp r8, rdx
0033A344  72 10                           jb 0x14033a356
0033A346  48 8D 82 00 08 00 00            lea rax, [rdx + 0x800]
0033A34D  4C 3B C0                        cmp r8, rax
0033A350  0F 82 DE 05 00 00               jb 0x14033a934
0033A356  0F 57 C0                        xorps xmm0, xmm0
0033A359  49 BA 10 00 00 00 00 DE FF FF   movabs r10, 0xffffde0000000010
0033A363  0F 57 C9                        xorps xmm1, xmm1
0033A366  4F 8D 34 40                     lea r14, [r8 + r8*2]
0033A36A  F3 0F 7F 44 24 40               movdqu xmmword ptr [rsp + 0x40], xmm0
0033A370  49 C1 E6 04                     shl r14, 4
0033A374  F3 0F 7F 4C 24 50               movdqu xmmword ptr [rsp + 0x50], xmm1
0033A37A  49 8B C2                        mov rax, r10
0033A37D  49 8B 0C 06                     mov rcx, qword ptr [r14 + rax]
0033A381  49 C7 C7 F7 FF FF FF            mov r15, 0xfffffffffffffff7
0033A388  48 0F BA E1 0A                  bt rcx, 0xa
0033A38D  48 C7 C0 FF FF FF F7            mov rax, 0xfffffffff7ffffff
0033A394  4C 0F 43 F8                     cmovae r15, rax
0033A398  4C 23 F9                        and r15, rcx
0033A39B  49 8B C1                        mov rax, r9
0033A39E  49 8D 34 06                     lea rsi, [r14 + rax]
0033A3A2  4C 3B C2                        cmp r8, rdx
0033A3A5  72 10                           jb 0x14033a3b7
0033A3A7  48 8D 82 00 08 00 00            lea rax, [rdx + 0x800]
0033A3AE  4C 3B C0                        cmp r8, rax
0033A3B1  0F 82 2A 05 00 00               jb 0x14033a8e1
0033A3B7  44 38 2D 28 28 B0 00            cmp byte ptr [rip + 0xb02828], r13b
0033A3BE  49 BB AB AA AA AA AA AA AA AA   movabs r11, 0xaaaaaaaaaaaaaaab
0033A3C8  0F 84 75 05 00 00               je 0x14033a943
0033A3CE  48 8B 05 6B 2E B0 00            mov rax, qword ptr [rip + 0xb02e6b]
0033A3D5  49 8B CE                        mov rcx, r14
0033A3D8  48 C1 F9 04                     sar rcx, 4
0033A3DC  49 0F AF CB                     imul rcx, r11
0033A3E0  48 C1 E9 09                     shr rcx, 9
0033A3E4  44 0F B6 24 48                  movzx r12d, byte ptr [rax + rcx*2]
0033A3E9  45 85 E4                        test r12d, r12d
0033A3EC  0F 85 A8 04 00 00               jne 0x14033a89a
0033A3F2  41 BC 09 00 00 00               mov r12d, 9
0033A3F8  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0033A3FC  48 8B 0D 85 5C AF 00            mov rcx, qword ptr [rip + 0xaf5c85]
0033A403  48 C1 E8 2B                     shr rax, 0x2b
0033A407  25 FF 03 00 00                  and eax, 0x3ff
0033A40C  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
0033A411  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
0033A415  48 63 0D A4 37 AF 00            movsxd rcx, dword ptr [rip + 0xaf37a4]
0033A41C  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
0033A421  8B 15 9D 37 AF 00               mov edx, dword ptr [rip + 0xaf379d]
0033A427  3B CA                           cmp ecx, edx
0033A429  77 1D                           ja 0x14033a448
0033A42B  48 8B C1                        mov rax, rcx
0033A42E  48 C1 E0 04                     shl rax, 4
0033A432  48 03 05 E7 37 AF 00            add rax, qword ptr [rip + 0xaf37e7]
0033A439  4C 3B 00                        cmp r8, qword ptr [rax]
0033A43C  72 0A                           jb 0x14033a448
0033A43E  3B CA                           cmp ecx, edx
0033A440  74 4B                           je 0x14033a48d
0033A442  4C 3B 40 10                     cmp r8, qword ptr [rax + 0x10]
0033A446  72 45                           jb 0x14033a48d
0033A448  45 8B CD                        mov r9d, r13d
0033A44B  41 3B D1                        cmp edx, r9d
0033A44E  0F 8C 12 01 00 00               jl 0x14033a566
0033A454  41 8D 0C 11                     lea ecx, [r9 + rdx]
0033A458  D1 F9                           sar ecx, 1
0033A45A  48 63 C1                        movsxd rax, ecx
0033A45D  48 C1 E0 04                     shl rax, 4
0033A461  48 03 05 B8 37 AF 00            add rax, qword ptr [rip + 0xaf37b8]
0033A468  4C 3B 00                        cmp r8, qword ptr [rax]
0033A46B  0F 82 4C 03 00 00               jb 0x14033a7bd
0033A471  3B 0D 4D 37 AF 00               cmp ecx, dword ptr [rip + 0xaf374d]
0033A477  0F 85 60 02 00 00               jne 0x14033a6dd
0033A47D  89 0D 3D 37 AF 00               mov dword ptr [rip + 0xaf373d], ecx
0033A483  49 B9 00 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000000
0033A48D  8B 40 08                        mov eax, dword ptr [rax + 8]
0033A490  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0033A494  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
0033A497  8B 4E 20                        mov ecx, dword ptr [rsi + 0x20]
0033A49A  C1 E9 18                        shr ecx, 0x18
0033A49D  89 84 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], eax
0033A4A4  F6 C1 08                        test cl, 8
0033A4A7  0F 85 1E 02 00 00               jne 0x14033a6cb
0033A4AD  0F B6 BC 24 C3 00 00 00         movzx edi, byte ptr [rsp + 0xc3]
0033A4B5  83 E7 07                        and edi, 7
0033A4B8  4C 39 2D 69 37 AF 00            cmp qword ptr [rip + 0xaf3769], r13
0033A4BF  89 7C 24 4C                     mov dword ptr [rsp + 0x4c], edi
0033A4C3  0F 85 59 02 00 00               jne 0x14033a722
0033A4C9  45 32 C0                        xor r8b, r8b
0033A4CC  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
0033A4D0  4C 69 C8 80 DF 00 00            imul r9, rax, 0xdf80
0033A4D7  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0033A4DC  44 88 44 24 50                  mov byte ptr [rsp + 0x50], r8b
0033A4E1  44 89 64 24 54                  mov dword ptr [rsp + 0x54], r12d
0033A4E6  4C 03 48 10                     add r9, qword ptr [rax + 0x10]
0033A4EA  41 83 FC 09                     cmp r12d, 9
0033A4EE  0F 8C F2 02 00 00               jl 0x14033a7e6
0033A4F4  8B C7                           mov eax, edi
0033A4F6  41 0F B6 C8                     movzx ecx, r8b
0033A4FA  48 8D 0C CD 3B 00 00 00         lea rcx, [rcx*8 + 0x3b]
0033A502  48 03 C8                        add rcx, rax
0033A505  48 6B C1 58                     imul rax, rcx, 0x58
0033A509  49 03 C1                        add rax, r9
0033A50C  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0033A511  49 8B C2                        mov rax, r10
0033A514  48 8B B4 24 B8 00 00 00         mov rsi, qword ptr [rsp + 0xb8]
0033A51C  4D 89 3C 06                     mov qword ptr [r14 + rax], r15
0033A520  4C 8B E3                        mov r12, rbx
0033A523  48 83 FB FF                     cmp rbx, -1
0033A527  0F 85 44 01 00 00               jne 0x14033a671
0033A52D  48 85 F6                        test rsi, rsi
0033A530  74 0F                           je 0x14033a541
0033A532  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0033A53C  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
0033A541  48 B8 FF FF FF FF 3F 00 00 00   movabs rax, 0x3fffffffff
0033A54B  4C 3B E0                        cmp r12, rax
0033A54E  41 0F 95 C5                     setne r13b
0033A552  41 8B C5                        mov eax, r13d
0033A555  48 83 C4 60                     add rsp, 0x60
0033A559  41 5F                           pop r15
0033A55B  41 5E                           pop r14
0033A55D  41 5D                           pop r13
0033A55F  41 5C                           pop r12
0033A561  5F                              pop rdi
0033A562  5E                              pop rsi
0033A563  5B                              pop rbx
0033A564  C3                              ret
0033A565  CC                              int3
0033A566  45 33 C9                        xor r9d, r9d
0033A569  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0033A56E  BA 80 51 00 00                  mov edx, 0x5180
0033A573  41 8D 49 1A                     lea ecx, [r9 + 0x1a]
0033A577  E8 E4 30 1C 00                  call 0x1404fd660
0033A57C  CC                              int3
0033A57D  44 39 AC 24 C0 00 00 00         cmp dword ptr [rsp + 0xc0], r13d
0033A585  0F 85 95 02 00 00               jne 0x14033a820
0033A58B  F0 48 0F BA 6A 18 3F            lock bts qword ptr [rdx + 0x18], 0x3f
0033A592  0F 83 E1 02 00 00               jae 0x14033a879
0033A598  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
0033A5A2  85 FF                           test edi, edi
0033A5A4  75 87                           jne 0x14033a52d
0033A5A6  48 85 F6                        test rsi, rsi
0033A5A9  74 1A                           je 0x14033a5c5
0033A5AB  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0033A5B5  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
0033A5BA  49 8B F5                        mov rsi, r13
0033A5BD  4C 89 AC 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r13
0033A5C5  BF 01 00 00 00                  mov edi, 1
0033A5CA  44 89 BC 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r15d
0033A5D2  49 8B DA                        mov rbx, r10
0033A5D5  4D 8B C5                        mov r8, r13
0033A5D8  E9 DF FC FF FF                  jmp 0x14033a2bc
0033A5DD  48 8D 0C 5B                     lea rcx, [rbx + rbx*2]
0033A5E1  48 C1 E1 04                     shl rcx, 4
0033A5E5  49 8B C1                        mov rax, r9
0033A5E8  48 03 C8                        add rcx, rax
0033A5EB  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
0033A5EE  C1 E8 18                        shr eax, 0x18
0033A5F1  A8 08                           test al, 8
0033A5F3  0F 85 A9 02 00 00               jne 0x14033a8a2
0033A5F9  44 89 AC 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r13d
0033A601  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
0033A60B  E9 00 FC FF FF                  jmp 0x14033a210
0033A610  48 8B 05 E9 B5 AF 00            mov rax, qword ptr [rip + 0xafb5e9]
0033A617  48 3B D8                        cmp rbx, rax
0033A61A  0F 82 35 FC FF FF               jb 0x14033a255
0033A620  48 05 00 08 00 00               add rax, 0x800
0033A626  48 3B D8                        cmp rbx, rax
0033A629  0F 83 26 FC FF FF               jae 0x14033a255
0033A62F  48 8B CB                        mov rcx, rbx
0033A632  E8 79 AF 09 00                  call 0x1403d55b0
0033A637  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
0033A63E  E9 6F FC FF FF                  jmp 0x14033a2b2
0033A643  85 FF                           test edi, edi
0033A645  0F 85 A5 00 00 00               jne 0x14033a6f0
0033A64B  49 8B 41 18                     mov rax, qword ptr [r9 + 0x18]
0033A64F  41 8B 59 24                     mov ebx, dword ptr [r9 + 0x24]
0033A653  81 E3 FF FF 1F 00               and ebx, 0x1fffff
0033A659  48 C1 E8 28                     shr rax, 0x28
0033A65D  48 C1 E3 13                     shl rbx, 0x13
0033A661  25 FF FF 07 00                  and eax, 0x7ffff
0033A666  48 0B D8                        or rbx, rax
0033A669  49 FF C0                        inc r8
0033A66C  E9 9F FB FF FF                  jmp 0x14033a210
0033A671  48 8B 05 88 B5 AF 00            mov rax, qword ptr [rip + 0xafb588]
0033A678  48 3B D8                        cmp rbx, rax
0033A67B  72 0F                           jb 0x14033a68c
0033A67D  48 05 00 08 00 00               add rax, 0x800
0033A683  48 3B D8                        cmp rbx, rax
0033A686  0F 82 A1 FE FF FF               jb 0x14033a52d
0033A68C  4C 8D 04 5B                     lea r8, [rbx + rbx*2]
0033A690  4D 03 C0                        add r8, r8
0033A693  49 8B C2                        mov rax, r10
0033A696  4A 8B 14 C0                     mov rdx, qword ptr [rax + r8*8]
0033A69A  B9 08 00 00 00                  mov ecx, 8
0033A69F  48 0F BA E2 0A                  bt rdx, 0xa
0033A6A4  B8 00 00 00 08                  mov eax, 0x8000000
0033A6A9  0F 43 C8                        cmovae ecx, eax
0033A6AC  48 0B CA                        or rcx, rdx
0033A6AF  49 8B C2                        mov rax, r10
0033A6B2  4A 89 0C C0                     mov qword ptr [rax + r8*8], rcx
0033A6B6  E9 72 FE FF FF                  jmp 0x14033a52d
0033A6BB  48 0F BA E1 1B                  bt rcx, 0x1b
0033A6C0  0F 83 5B FC FF FF               jae 0x14033a321
0033A6C6  E9 CC FB FF FF                  jmp 0x14033a297
0033A6CB  49 8B C9                        mov rcx, r9
0033A6CE  48 3B F1                        cmp rsi, rcx
0033A6D1  73 7B                           jae 0x14033a74e
0033A6D3  BF 05 00 00 00                  mov edi, 5
0033A6D8  E9 DB FD FF FF                  jmp 0x14033a4b8
0033A6DD  4C 3B 40 10                     cmp r8, qword ptr [rax + 0x10]
0033A6E1  0F 82 96 FD FF FF               jb 0x14033a47d
0033A6E7  44 8D 49 01                     lea r9d, [rcx + 1]
0033A6EB  E9 5B FD FF FF                  jmp 0x14033a44b
0033A6F0  49 8B 59 28                     mov rbx, qword ptr [r9 + 0x28]
0033A6F4  48 B8 00 00 00 00 00 00 80 0F   movabs rax, 0xf80000000000000
0033A6FE  48 23 D8                        and rbx, rax
0033A701  49 8B 01                        mov rax, qword ptr [r9]
0033A704  48 C1 E8 14                     shr rax, 0x14
0033A708  48 0B D8                        or rbx, rax
0033A70B  41 8B 41 24                     mov eax, dword ptr [r9 + 0x24]
0033A70F  48 25 00 00 E0 FF               and rax, 0xffffffffffe00000
0033A715  48 C1 EB 14                     shr rbx, 0x14
0033A719  48 C1 E0 03                     shl rax, 3
0033A71D  E9 44 FF FF FF                  jmp 0x14033a666
0033A722  49 8B CE                        mov rcx, r14
0033A725  48 C1 F9 04                     sar rcx, 4
0033A729  49 0F AF CB                     imul rcx, r11
0033A72D  E8 F2 16 00 00                  call 0x14033be24
0033A732  49 BA 10 00 00 00 00 DE FF FF   movabs r10, 0xffffde0000000010
0033A73C  44 0F B6 40 0C                  movzx r8d, byte ptr [rax + 0xc]
0033A741  E9 86 FD FF FF                  jmp 0x14033a4cc
0033A746  49 8B 19                        mov rbx, qword ptr [r9]
0033A749  E9 CB FB FF FF                  jmp 0x14033a319
0033A74E  48 8B 0D 8B 35 AF 00            mov rcx, qword ptr [rip + 0xaf358b]
0033A755  48 8D 14 49                     lea rdx, [rcx + rcx*2]
0033A759  48 C1 E2 04                     shl rdx, 4
0033A75D  48 B9 30 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000030
0033A767  48 03 D1                        add rdx, rcx
0033A76A  48 3B F2                        cmp rsi, rdx
0033A76D  0F 83 60 FF FF FF               jae 0x14033a6d3
0033A773  48 8B 0D 86 B4 AF 00            mov rcx, qword ptr [rip + 0xafb486]
0033A77A  49 8B D6                        mov rdx, r14
0033A77D  48 C1 FA 04                     sar rdx, 4
0033A781  49 0F AF D3                     imul rdx, r11
0033A785  48 3B D1                        cmp rdx, rcx
0033A788  72 10                           jb 0x14033a79a
0033A78A  48 81 C1 00 08 00 00            add rcx, 0x800
0033A791  48 3B D1                        cmp rdx, rcx
0033A794  0F 82 39 FF FF FF               jb 0x14033a6d3
0033A79A  C1 E8 10                        shr eax, 0x10
0033A79D  24 07                           and al, 7
0033A79F  3C 06                           cmp al, 6
0033A7A1  0F 84 06 FD FF FF               je 0x14033a4ad
0033A7A7  48 8B CE                        mov rcx, rsi
0033A7AA  E8 21 3B F5 FF                  call 0x14028e2d0
0033A7AF  83 F8 09                        cmp eax, 9
0033A7B2  0F 85 F5 FC FF FF               jne 0x14033a4ad
0033A7B8  E9 16 FF FF FF                  jmp 0x14033a6d3
0033A7BD  85 C9                           test ecx, ecx
0033A7BF  0F 85 89 01 00 00               jne 0x14033a94e
0033A7C5  4C 8B C8                        mov r9, rax
0033A7C8  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0033A7CD  BA 80 51 00 00                  mov edx, 0x5180
0033A7D2  B9 1A 00 00 00                  mov ecx, 0x1a
0033A7D7  E8 84 2E 1C 00                  call 0x1404fd660
0033A7DC  CC                              int3
0033A7DD  49 8B 59 18                     mov rbx, qword ptr [r9 + 0x18]
0033A7E1  E9 B4 F9 FF FF                  jmp 0x14033a19a
0033A7E6  41 83 FC 08                     cmp r12d, 8
0033A7EA  0F 84 06 01 00 00               je 0x14033a8f6
0033A7F0  44 88 6C 24 58                  mov byte ptr [rsp + 0x58], r13b
0033A7F5  32 C9                           xor cl, cl
0033A7F7  0F B6 C9                        movzx ecx, cl
0033A7FA  8B C7                           mov eax, edi
0033A7FC  48 8D 0C C8                     lea rcx, [rax + rcx*8]
0033A800  49 63 C4                        movsxd rax, r12d
0033A803  48 6B D1 58                     imul rdx, rcx, 0x58
0033A807  48 69 C8 E8 00 00 00            imul rcx, rax, 0xe8
0033A80E  4A 03 94 09 98 3D 00 00         add rdx, qword ptr [rcx + r9 + 0x3d98]
0033A816  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0033A81B  E9 F1 FC FF FF                  jmp 0x14033a511
0033A820  49 83 F8 01                     cmp r8, 1
0033A824  0F 87 61 FD FF FF               ja 0x14033a58b
0033A82A  83 BC 24 A0 00 00 00 02         cmp dword ptr [rsp + 0xa0], 2
0033A832  0F 84 F7 FD FF FF               je 0x14033a62f
0033A838  48 B8 10 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000010
0033A842  48 8B D8                        mov rbx, rax
0033A845  48 8B 05 34 34 AF 00            mov rax, qword ptr [rip + 0xaf3434]
0033A84C  48 8B 1C CB                     mov rbx, qword ptr [rbx + rcx*8]
0033A850  48 85 C0                        test rax, rax
0033A853  74 0B                           je 0x14033a860
0033A855  F6 C3 10                        test bl, 0x10
0033A858  75 06                           jne 0x14033a860
0033A85A  48 F7 D0                        not rax
0033A85D  48 23 D8                        and rbx, rax
0033A860  48 C1 EB 0C                     shr rbx, 0xc
0033A864  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
0033A86E  48 23 D8                        and rbx, rax
0033A871  49 FF C0                        inc r8
0033A874  E9 63 F9 FF FF                  jmp 0x14033a1dc
0033A879  48 85 F6                        test rsi, rsi
0033A87C  74 0F                           je 0x14033a88d
0033A87E  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0033A888  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
0033A88D  48 8B F2                        mov rsi, rdx
0033A890  48 89 94 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdx
0033A898  EB 90                           jmp 0x14033a82a
0033A89A  41 FF CC                        dec r12d
0033A89D  E9 56 FB FF FF                  jmp 0x14033a3f8
0033A8A2  E8 29 3A F5 FF                  call 0x14028e2d0
0033A8A7  83 F8 09                        cmp eax, 9
0033A8AA  0F 85 49 FD FF FF               jne 0x14033a5f9
0033A8B0  C7 84 24 A0 00 00 00 02 00 00 00  mov dword ptr [rsp + 0xa0], 2
0033A8BB  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
0033A8C5  E9 46 F9 FF FF                  jmp 0x14033a210
0033A8CA  E8 01 3A F5 FF                  call 0x14028e2d0
0033A8CF  83 F8 09                        cmp eax, 9
0033A8D2  0F 85 7F F8 FF FF               jne 0x14033a157
0033A8D8  44 8D 78 F9                     lea r15d, [rax - 7]
0033A8DC  E9 79 F8 FF FF                  jmp 0x14033a15a
0033A8E1  41 BC 09 00 00 00               mov r12d, 9
0033A8E7  49 BB AB AA AA AA AA AA AA AA   movabs r11, 0xaaaaaaaaaaaaaaab
0033A8F1  E9 02 FB FF FF                  jmp 0x14033a3f8
0033A8F6  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
0033A900  48 8B C1                        mov rax, rcx
0033A903  48 2B F0                        sub rsi, rax
0033A906  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
0033A910  48 C1 FE 04                     sar rsi, 4
0033A914  48 0F AF F0                     imul rsi, rax
0033A918  48 8B 05 21 29 B0 00            mov rax, qword ptr [rip + 0xb02921]
0033A91F  48 C1 EE 09                     shr rsi, 9
0033A923  0F B6 4C 70 01                  movzx ecx, byte ptr [rax + rsi*2 + 1]
0033A928  80 E1 7F                        and cl, 0x7f
0033A92B  88 4C 24 58                     mov byte ptr [rsp + 0x58], cl
0033A92F  E9 C3 FE FF FF                  jmp 0x14033a7f7
0033A934  49 BA 10 00 00 00 00 DE FF FF   movabs r10, 0xffffde0000000010
0033A93E  E9 DD FB FF FF                  jmp 0x14033a520
0033A943  41 BC 09 00 00 00               mov r12d, 9
0033A949  E9 AA FA FF FF                  jmp 0x14033a3f8
0033A94E  8D 51 FF                        lea edx, [rcx - 1]
0033A951  E9 F5 FA FF FF                  jmp 0x14033a44b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFindSuitableLookasideReplacement(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m44;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int8 v_stack_p2B;
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p58;
    unsigned int v_stack_p8;
    unsigned int v_stack_pA0;
    unsigned __int64 v_stack_pB8;

    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (96);
    v_r13 = 0;
    v_stack_p20 = 0;
    v_r10 = (a4) - (a2);
    v_r10 = (v_r10) >> (4);
    v_r10 = (v_r10) * (a2);
    if ((unsigned int)(a1) != 0) goto loc_0033A157;
    if (v_r10 < (*(unsigned __int64 *)(v_rip + 11516635))) goto loc_0033A13B;
    result = (*(unsigned __int64 *)(v_rip + 11516635)) + (0x800ULL);
    if (v_r10 >= result) goto loc_0033A13B;
    goto loc_0033A15A;
loc_0033A13B:
    a1 = (v_r10 + v_r10 * 2) << (4);
    a1 = (a1) + (a2);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (8)) != 0) goto loc_0033A8CA;
loc_0033A157:
loc_0033A15A:
    v_stack_p8 = 0;
loc_0033A16F:
    if (0 >= 16) goto loc_0033A52D;
    if ((unsigned int)((unsigned int)((unsigned int)(a1))) != 0) goto loc_0033A300;
    a3 = (0) + 1;
    if (0 != 0) goto loc_0033A7DD;
loc_0033A19A:
    v_rbx = (*(unsigned __int64 *)(a4)) & (a2);
    if (v_rbx == v_r12) goto loc_0033A5A2;
    a1 = (v_rbx + v_rbx * 2) + (v_rbx + v_rbx * 2);
    if (v_rbx < (*(unsigned __int64 *)(v_rip + 11516472))) goto loc_0033A1DC;
    result = (*(unsigned __int64 *)(v_rip + 11516472)) + (0x800ULL);
    if (v_rbx < result) goto loc_0033A57D;
loc_0033A1DC:
    if (v_rbx < (*(unsigned __int64 *)(v_rip + 11516445))) goto loc_0033A5DD;
    result = (*(unsigned __int64 *)(v_rip + 11516445)) + (0x800ULL);
    if (v_rbx >= result) goto loc_0033A5DD;
    v_stack_p8 = 1;
loc_0033A210:
    if (v_rbx == v_r12) goto loc_0033A5A2;
    a1 = (v_rbx + v_rbx * 2) + (v_rbx + v_rbx * 2);
    if (a5 == 0) goto loc_0033A2CF;
    if (a3 > 1) goto loc_0033A2CF;
loc_0033A24C:
    if ((unsigned int)((unsigned int)((unsigned int)(a1))) == 0) goto loc_0033A610;
loc_0033A255:
    if (v_rbx < (*(unsigned __int64 *)(v_rip + 11516324))) goto loc_0033A26C;
    result = (*(unsigned __int64 *)(v_rip + 11516324)) + (0x800ULL);
    if (v_rbx < result) goto loc_0033A297;
loc_0033A26C:
    if (v_rbx >= result) goto loc_0033A6BB;
    a1 = (*(unsigned __int64 *)(result + a1 * 8)) >> (3);
    a1 = (unsigned int)(~(a1));
    if ((((unsigned __int8)(a1)) & (1)) != 0) goto loc_0033A321;
loc_0033A297:
loc_0033A29D:
    if ((*(unsigned __int64 *)(a2)) == v_rbx) goto loc_0033A2B2;
    a2 = (unsigned int)((0) + 1);
    a1 = (a2) + (8);
    if (((unsigned int)(a2)) == 64) goto loc_0033A321;
    if (((unsigned int)(a2)) < 64) goto loc_0033A29D;
loc_0033A2B2:
loc_0033A2BC:
    a4 = (v_rbx + v_rbx * 2) << (4);
    a4 = (a4) + (a1);
    goto loc_0033A16F;
loc_0033A2CF:
    if (condition_is_below) goto loc_0033A598;
    if (0 != 0) {
    }
    v_stack_p20 = a2;
    goto loc_0033A24C;
loc_0033A300:
    if (((unsigned int)((unsigned int)((unsigned int)(a1)))) != 1) goto loc_0033A643;
    a3 = (a3) + 1;
    if (0 != 0) goto loc_0033A746;
loc_0033A319:
    v_rbx = (*(unsigned __int64 *)(a4 + 24)) & (a2);
    goto loc_0033A210;
loc_0033A321:
    *(unsigned __int64 *)(a2 + (unsigned int)(v_stack_p18) * 8) = v_rbx;
    if ((*(unsigned __int64 *)(a2 + (unsigned int)(v_stack_p18) * 8)) == -1) goto loc_0033A934;
    if ((*(unsigned __int64 *)(a2 + (unsigned int)(v_stack_p18) * 8)) < (*(unsigned __int64 *)(v_rip + 11516095))) goto loc_0033A356;
    if ((*(unsigned __int64 *)(a2 + (unsigned int)(v_stack_p18) * 8)) < (*(unsigned __int64 *)(v_rip + 11516095) + 2048)) goto loc_0033A934;
loc_0033A356:
    v_stack_m58 = v_xmm0;
    v_r14 = (*(unsigned __int64 *)(a2 + (unsigned int)(v_stack_p18) * 8) + *(unsigned __int64 *)(a2 + (unsigned int)(v_stack_p18) * 8) * 2) << (4);
    v_stack_m48 = v_xmm1;
    v_r15 = -9;
    if (condition_is_above_or_equal) { v_r15 = 0xFFFFFFFFF7FFFFFFULL; }
    v_r15 = (v_r15) & (*(unsigned __int64 *)(v_r14 + v_r10 * 1));
    if ((*(unsigned __int64 *)(a2 + (unsigned int)(v_stack_p18) * 8)) < (*(unsigned __int64 *)(v_rip + 11516095))) goto loc_0033A3B7;
    if ((*(unsigned __int64 *)(a2 + (unsigned int)(v_stack_p18) * 8)) < (*(unsigned __int64 *)(v_rip + 11516095) + 2048)) goto loc_0033A8E1;
loc_0033A3B7:
    if ((*(unsigned __int8 *)(v_rip + 11544616)) == 0) goto loc_0033A943;
    a1 = (v_r14) >> (4);
    a1 = (a1) * ((unsigned int)((unsigned int)(a1)));
    a1 = (a1) >> (9);
    if ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 11546219) + a1 * 2)) != 0) goto loc_0033A89A;
loc_0033A3F8:
    result = (*(unsigned __int64 *)(v_r14 + a4 * 1 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_m60 = v_r14 + a4 * 1;
    v_stack_m68 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11492485) + result * 8);
    if (((unsigned int)((int)(*(unsigned int *)(v_rip + 11483044)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11483037))))) goto loc_0033A448;
    result = ((int)(*(unsigned int *)(v_rip + 11483044))) << (4);
    result = (result) + (*(unsigned __int64 *)(v_rip + 11483111));
    if ((*(unsigned __int64 *)(a2 + (unsigned int)(v_stack_p18) * 8)) < (*(unsigned __int64 *)(result))) goto loc_0033A448;
    if (((unsigned int)((int)(*(unsigned int *)(v_rip + 11483044)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11483037))))) goto loc_0033A48D;
    if ((*(unsigned __int64 *)(a2 + (unsigned int)(v_stack_p18) * 8)) < (*(unsigned __int64 *)(result + 16))) goto loc_0033A48D;
loc_0033A448:
loc_0033A44B:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11483037)))) < 0) goto loc_0033A566;
    a1 = (unsigned int)((0 + (unsigned int)(*(unsigned int *)(v_rip + 11483037)) * 1) >> (1));
    result = ((int)((unsigned int)(a1))) << (4);
    result = (result) + (*(unsigned __int64 *)(v_rip + 11483064));
    if ((*(unsigned __int64 *)(a2 + (unsigned int)(v_stack_p18) * 8)) < (*(unsigned __int64 *)(result))) goto loc_0033A7BD;
    if (((unsigned int)(a1)) != (*(unsigned int *)(v_rip + 11482957))) goto loc_0033A6DD;
loc_0033A47D:
    *(unsigned int *)(v_rip + 11482941) = (unsigned int)(a1);
loc_0033A48D:
    v_stack_m50 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 8)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + a4 * 1 + 32))) >> (24));
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + a4 * 1 + 32)));
    if ((((unsigned __int8)(a1)) & (8)) != 0) goto loc_0033A6CB;
loc_0033A4AD:
    v_rdi = (unsigned int)((v_stack_p2B) & (7));
loc_0033A4B8:
    v_stack_m4C = (unsigned int)(v_rdi);
    if ((*(unsigned __int64 *)(v_rip + 11482985)) != 0) goto loc_0033A722;
    a3 = 0;
loc_0033A4CC:
    a4 = (0) * ((unsigned int)(v_stack_m50));
    v_stack_m48 = 0;
    v_stack_m44 = 9;
    a4 = (a4) + (*(unsigned __int64 *)(v_stack_m68 + 16));
    if (9 < 9) goto loc_0033A7E6;
    a1 = (0 * 8 + 59) + ((unsigned int)((unsigned int)(v_rdi)));
    result = ((unsigned int)((unsigned int)(v_rdi))) * (a1);
    result = (result) + (a4);
    v_stack_m58 = result;
loc_0033A511:
    *(unsigned __int64 *)(v_r14 + v_r10 * 1) = v_r15;
loc_0033A520:
    if (v_rbx != -1) goto loc_0033A671;
loc_0033A52D:
    if (v_stack_p20 != 0) {
    }
    v_r13 = (v_rbx != v_r10) ? 1 : 0;
    v_rsp = (v_rsp) + (96);
    return (unsigned int)((unsigned int)(v_r13));
loc_0033A566:
    a4 = 0;
    v_stack_p20 = v_r13;
    result = KeBugCheckEx(a4 + 26, (unsigned int)(0x5180ULL), a3, a4);
loc_0033A57D:
    if (a5 != ((unsigned int)(v_r13))) goto loc_0033A820;
loc_0033A58B:
    if (a5 >= ((unsigned int)(v_r13))) goto loc_0033A879;
loc_0033A598:
loc_0033A5A2:
    if ((unsigned int)(v_rdi) != 0) goto loc_0033A52D;
    v_rsi = v_stack_p20;
    if (v_stack_p20 != 0) {
        v_rsi = v_r13;
        v_stack_pB8 = v_r13;
    }
    v_stack_pA0 = (unsigned int)(v_r15);
    goto loc_0033A2BC;
loc_0033A5DD:
    a1 = (v_r10 + v_r10 * 2) << (4);
    a1 = (a1) + (0);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (8)) != 0) goto loc_0033A8A2;
loc_0033A5F9:
    v_stack_pA0 = (unsigned int)(v_r13);
    goto loc_0033A210;
loc_0033A610:
    if (v_r10 < (*(unsigned __int64 *)(v_rip + 11515369))) goto loc_0033A255;
    result = (*(unsigned __int64 *)(v_rip + 11515369)) + (0x800ULL);
    if (v_r10 >= result) goto loc_0033A255;
loc_0033A62F:
    result = MiGetStandbyPageType(v_r10, (unsigned int)(0x5180ULL), v_r13, a4);
    v_stack_pA0 = (unsigned int)(result);
    goto loc_0033A2B2;
loc_0033A643:
    if (1 != 0) goto loc_0033A6F0;
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 36))) & (0x1FFFFFULL));
    result = (*(unsigned __int64 *)(a4 + 24)) >> (40);
    v_rbx = (v_rbx) << (19);
    result = (unsigned int)((result) & (0x7FFFFULL));
loc_0033A666:
    v_rbx = (v_rbx) | (result);
    a3 = (v_r13) + 1;
    goto loc_0033A210;
loc_0033A671:
    if (v_rbx < (*(unsigned __int64 *)(v_rip + 11515272))) goto loc_0033A68C;
    result = (*(unsigned __int64 *)(v_rip + 11515272)) + (0x800ULL);
    if (v_rbx < result) goto loc_0033A52D;
loc_0033A68C:
    a3 = (v_rbx + v_rbx * 2) + (v_rbx + v_rbx * 2);
    a1 = 8;
    if (condition_is_above_or_equal) { a1 = (unsigned int)((unsigned int)(0x8000000ULL)); }
    a1 = (a1) | (*(unsigned __int64 *)(v_r10 + a3 * 8));
    *(unsigned __int64 *)(v_r10 + a3 * 8) = a1;
    goto loc_0033A52D;
loc_0033A6BB:
    if (condition_is_above_or_equal) goto loc_0033A321;
    goto loc_0033A297;
loc_0033A6CB:
    if (v_rsi >= 0) goto loc_0033A74E;
loc_0033A6D3:
    goto loc_0033A4B8;
loc_0033A6DD:
    if (a3 < (*(unsigned __int64 *)(v_r10 + 16))) goto loc_0033A47D;
    goto loc_0033A44B;
loc_0033A6F0:
    v_rbx = (*(unsigned __int64 *)(0 + 1 + 40)) & (v_r10);
    result = (*(unsigned __int64 *)(0 + 1)) >> (20);
    v_rbx = (v_rbx) | (result);
    result = ((unsigned int)(*(unsigned int *)(0 + 1 + 36))) & (0xFFFFFFFFFFE00000ULL);
    v_rbx = (v_rbx) >> (20);
    result = (result) << (3);
    goto loc_0033A666;
loc_0033A722:
    a1 = (v_r14) >> (4);
    a1 = (a1) * ((unsigned int)((unsigned int)(a1)));
    result = MiSearchChannelTable(a1, *(unsigned __int64 *)(v_r10 + a3 * 8), a3, 0 + 1);
    goto loc_0033A4CC;
loc_0033A746:
    goto loc_0033A319;
loc_0033A74E:
    a2 = (*(unsigned __int64 *)(v_rip + 11482507) + *(unsigned __int64 *)(v_rip + 11482507) * 2) << (4);
    a2 = (a2) + (*(unsigned __int64 *)(v_rip + 11482507));
    if (v_rsi >= a2) goto loc_0033A6D3;
    a2 = (v_r14) >> (4);
    a2 = (a2) * ((unsigned int)((unsigned int)(a1)));
    if (a2 < (*(unsigned __int64 *)(v_rip + 11515014))) goto loc_0033A79A;
    a1 = (*(unsigned __int64 *)(v_rip + 11515014)) + (0x800ULL);
    if (a2 < a1) goto loc_0033A6D3;
loc_0033A79A:
    result = (unsigned int)((result) >> (16));
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) == 6) goto loc_0033A4AD;
    result = MiGetPfnSlabType(v_rsi, a2, *(unsigned __int8 *)(result + 12), 0 + 1);
    if (((unsigned int)(result)) != 9) goto loc_0033A4AD;
    goto loc_0033A6D3;
loc_0033A7BD:
    if ((unsigned int)(v_rsi) != 0) goto loc_0033A94E;
    v_stack_p20 = v_r13;
    result = KeBugCheckEx(26, (unsigned int)(0x5180ULL), *(unsigned __int8 *)(result + 12), result);
loc_0033A7DD:
    goto loc_0033A19A;
loc_0033A7E6:
    if (((unsigned int)(v_rbx)) == 8) goto loc_0033A8F6;
    v_stack_p58 = (unsigned __int8)(v_r13);
    a1 = 0;
loc_0033A7F7:
    a2 = ((unsigned int)(0x5180ULL)) * (5 + 0 * 8);
    a1 = (5 + 0 * 8) * ((int)((unsigned int)(v_rbx)));
    a2 = (a2) + (*(unsigned __int64 *)(a1 + result * 1 + 15768));
    v_stack_p40 = a2;
    goto loc_0033A511;
loc_0033A820:
    if ((*(unsigned __int8 *)(result + 12)) > 1) goto loc_0033A58B;
loc_0033A82A:
    if (v_stack_pA0 == 2) goto loc_0033A62F;
    if (*(unsigned __int64 *)(v_rip + 11482164) == 0) goto loc_0033A860;
    result = *(unsigned __int64 *)(v_rip + 11482164);
    v_rbx = *(unsigned __int64 *)((int)((unsigned int)(v_rbx)) + a1 * 8);
    if ((((unsigned __int8)(*(unsigned __int64 *)((int)((unsigned int)(v_rbx)) + a1 * 8))) & (16)) == 0) {
        result = ~(*(unsigned __int64 *)(v_rip + 11482164));
        v_rbx = (*(unsigned __int64 *)((int)((unsigned int)(v_rbx)) + a1 * 8)) & (result);
    }
    v_rbx = (v_rbx) >> (12);
    v_rbx = (v_rbx) & (result);
    a3 = (*(unsigned __int8 *)(result + 12)) + 1;
    goto loc_0033A1DC;
loc_0033A879:
    if (v_rsi != 0) {
    }
    v_stack_pB8 = a2;
    goto loc_0033A82A;
loc_0033A89A:
    v_r12 = (unsigned int)((v_rbx) - 1);
    goto loc_0033A3F8;
loc_0033A8A2:
    result = MiGetPfnSlabType(a1, a2, a3, result);
    if (((unsigned int)(result)) != 9) goto loc_0033A5F9;
    v_stack_pA0 = 2;
    goto loc_0033A210;
loc_0033A8CA:
    result = MiGetPfnSlabType(a1, a2, a3, result);
    if (((unsigned int)(result)) != 9) goto loc_0033A157;
    goto loc_0033A15A;
loc_0033A8E1:
    goto loc_0033A3F8;
loc_0033A8F6:
    v_rsi = (a2) - (a1);
    v_rsi = (v_rsi) >> (4);
    v_rsi = (v_rsi) * (a1);
    v_rsi = (v_rsi) >> (9);
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 11544865) + v_rsi * 2 + 1)) & (127));
    v_stack_p58 = (unsigned __int8)(a1);
    goto loc_0033A7F7;
loc_0033A934:
    goto loc_0033A520;
loc_0033A943:
    goto loc_0033A3F8;
loc_0033A94E:
    goto loc_0033A44B;
}
```

## 5. (Beta) C Style

```c
int64_t MiFindSuitableLookasideReplacement(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m44;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint8_t v_stack_p2B;
    uint64_t v_stack_p40;
    uint8_t v_stack_p58;
    uint32_t v_stack_p8;
    uint32_t v_stack_pA0;
    uint64_t v_stack_pB8;

    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (96);
    local_r13 = 0;
    v_stack_p20 = 0;
    local_r10 = (Arg4) - (Arg2);
    local_r10 = (local_r10) >> (4);
    local_r10 = (local_r10) * (Arg2);
    if ((uint32_t)(Arg1) != 0) goto loc_0033A157;
    if (local_r10 < (*(uint64_t *)(v_rip + 0xAFBADB))) goto loc_0033A13B;
    result = (*(uint64_t *)(v_rip + 0xAFBADB)) + (0x800ULL);
    if (local_r10 >= result) goto loc_0033A13B;
    goto loc_0033A15A;
loc_0033A13B:
    Arg1 = (local_r10 + local_r10 * 2) << (4);
    Arg1 = (Arg1) + (Arg2);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (8)) != 0) goto loc_0033A8CA;
loc_0033A157:
loc_0033A15A:
    v_stack_p8 = 0;
loc_0033A16F:
    if (0 >= 16) goto loc_0033A52D;
    if ((uint32_t)((uint32_t)((uint32_t)(Arg1))) != 0) goto loc_0033A300;
    Arg3 = (0) + 1;
    if (0 != 0) goto loc_0033A7DD;
loc_0033A19A:
    local_rbx = (*(uint64_t *)(Arg4)) & (Arg2);
    if (local_rbx == local_r12) goto loc_0033A5A2;
    Arg1 = (local_rbx + local_rbx * 2) + (local_rbx + local_rbx * 2);
    if (local_rbx < (*(uint64_t *)(v_rip + 0xAFBA38))) goto loc_0033A1DC;
    result = (*(uint64_t *)(v_rip + 0xAFBA38)) + (0x800ULL);
    if (local_rbx < result) goto loc_0033A57D;
loc_0033A1DC:
    if (local_rbx < (*(uint64_t *)(v_rip + 0xAFBA1D))) goto loc_0033A5DD;
    result = (*(uint64_t *)(v_rip + 0xAFBA1D)) + (0x800ULL);
    if (local_rbx >= result) goto loc_0033A5DD;
    v_stack_p8 = 1;
loc_0033A210:
    if (local_rbx == local_r12) goto loc_0033A5A2;
    Arg1 = (local_rbx + local_rbx * 2) + (local_rbx + local_rbx * 2);
    if (Arg5 == 0) goto loc_0033A2CF;
    if (Arg3 > 1) goto loc_0033A2CF;
loc_0033A24C:
    if ((uint32_t)((uint32_t)((uint32_t)(Arg1))) == 0) goto loc_0033A610;
loc_0033A255:
    if (local_rbx < (*(uint64_t *)(v_rip + 0xAFB9A4))) goto loc_0033A26C;
    result = (*(uint64_t *)(v_rip + 0xAFB9A4)) + (0x800ULL);
    if (local_rbx < result) goto loc_0033A297;
loc_0033A26C:
    if (local_rbx >= result) goto loc_0033A6BB;
    Arg1 = (*(uint64_t *)(result + Arg1 * 8)) >> (3);
    Arg1 = (uint32_t)(~(Arg1));
    if ((((uint8_t)(Arg1)) & (1)) != 0) goto loc_0033A321;
loc_0033A297:
loc_0033A29D:
    if ((*(uint64_t *)(Arg2)) == local_rbx) goto loc_0033A2B2;
    Arg2 = (uint32_t)((0) + 1);
    Arg1 = (Arg2) + (8);
    if (((uint32_t)(Arg2)) == 64) goto loc_0033A321;
    if (((uint32_t)(Arg2)) < 64) goto loc_0033A29D;
loc_0033A2B2:
loc_0033A2BC:
    Arg4 = (local_rbx + local_rbx * 2) << (4);
    Arg4 = (Arg4) + (Arg1);
    goto loc_0033A16F;
loc_0033A2CF:
    if (condition_is_below) goto loc_0033A598;
    if (0 != 0) {
    }
    v_stack_p20 = Arg2;
    goto loc_0033A24C;
loc_0033A300:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg1)))) != 1) goto loc_0033A643;
    Arg3 = (Arg3) + 1;
    if (0 != 0) goto loc_0033A746;
loc_0033A319:
    local_rbx = (*(uint64_t *)(Arg4 + 0x18)) & (Arg2);
    goto loc_0033A210;
loc_0033A321:
    *(uint64_t *)(Arg2 + (uint32_t)(v_stack_p18) * 8) = local_rbx;
    if ((*(uint64_t *)(Arg2 + (uint32_t)(v_stack_p18) * 8)) == -1) goto loc_0033A934;
    if ((*(uint64_t *)(Arg2 + (uint32_t)(v_stack_p18) * 8)) < (*(uint64_t *)(v_rip + 0xAFB8BF))) goto loc_0033A356;
    if ((*(uint64_t *)(Arg2 + (uint32_t)(v_stack_p18) * 8)) < (*(uint64_t *)(v_rip + 0xAFB8BF) + 2048)) goto loc_0033A934;
loc_0033A356:
    v_stack_m58 = v_xmm0;
    local_r14 = (*(uint64_t *)(Arg2 + (uint32_t)(v_stack_p18) * 8) + *(uint64_t *)(Arg2 + (uint32_t)(v_stack_p18) * 8) * 2) << (4);
    v_stack_m48 = v_xmm1;
    local_r15 = -9;
    if (condition_is_above_or_equal) { local_r15 = 0xFFFFFFFFF7FFFFFFULL; }
    local_r15 = (local_r15) & (*(uint64_t *)(local_r14 + local_r10 * 1));
    if ((*(uint64_t *)(Arg2 + (uint32_t)(v_stack_p18) * 8)) < (*(uint64_t *)(v_rip + 0xAFB8BF))) goto loc_0033A3B7;
    if ((*(uint64_t *)(Arg2 + (uint32_t)(v_stack_p18) * 8)) < (*(uint64_t *)(v_rip + 0xAFB8BF) + 2048)) goto loc_0033A8E1;
loc_0033A3B7:
    if ((*(uint8_t *)(v_rip + 0xB02828)) == 0) goto loc_0033A943;
    Arg1 = (local_r14) >> (4);
    Arg1 = (Arg1) * ((uint32_t)((uint32_t)(Arg1)));
    Arg1 = (Arg1) >> (9);
    if ((uint32_t)(*(uint8_t *)(*(uint64_t *)(v_rip + 0xB02E6B) + Arg1 * 2)) != 0) goto loc_0033A89A;
loc_0033A3F8:
    result = (*(uint64_t *)(local_r14 + Arg4 * 1 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_m60 = local_r14 + Arg4 * 1;
    v_stack_m68 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xAF5C85) + result * 8);
    if (((uint32_t)((int32_t)(*(uint32_t *)(v_rip + 0xAF37A4)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAF379D))))) goto loc_0033A448;
    result = ((int32_t)(*(uint32_t *)(v_rip + 0xAF37A4))) << (4);
    result = (result) + (*(uint64_t *)(v_rip + 0xAF37E7));
    if ((*(uint64_t *)(Arg2 + (uint32_t)(v_stack_p18) * 8)) < (*(uint64_t *)(result))) goto loc_0033A448;
    if (((uint32_t)((int32_t)(*(uint32_t *)(v_rip + 0xAF37A4)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAF379D))))) goto loc_0033A48D;
    if ((*(uint64_t *)(Arg2 + (uint32_t)(v_stack_p18) * 8)) < (*(uint64_t *)(result + 0x10))) goto loc_0033A48D;
loc_0033A448:
loc_0033A44B:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAF379D)))) < 0) goto loc_0033A566;
    Arg1 = (uint32_t)((0 + (uint32_t)(*(uint32_t *)(v_rip + 0xAF379D)) * 1) >> (1));
    result = ((int32_t)((uint32_t)(Arg1))) << (4);
    result = (result) + (*(uint64_t *)(v_rip + 0xAF37B8));
    if ((*(uint64_t *)(Arg2 + (uint32_t)(v_stack_p18) * 8)) < (*(uint64_t *)(result))) goto loc_0033A7BD;
    if (((uint32_t)(Arg1)) != (*(uint32_t *)(v_rip + 0xAF374D))) goto loc_0033A6DD;
loc_0033A47D:
    *(uint32_t *)(v_rip + 0xAF373D) = (uint32_t)(Arg1);
loc_0033A48D:
    v_stack_m50 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + Arg4 * 1 + 0x20))) >> (24));
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + Arg4 * 1 + 0x20)));
    if ((((uint8_t)(Arg1)) & (8)) != 0) goto loc_0033A6CB;
loc_0033A4AD:
    local_rdi = (uint32_t)((v_stack_p2B) & (7));
loc_0033A4B8:
    v_stack_m4C = (uint32_t)(local_rdi);
    if ((*(uint64_t *)(v_rip + 0xAF3769)) != 0) goto loc_0033A722;
    Arg3 = 0;
loc_0033A4CC:
    Arg4 = (0) * ((uint32_t)(v_stack_m50));
    v_stack_m48 = 0;
    v_stack_m44 = 9;
    Arg4 = (Arg4) + (*(uint64_t *)(v_stack_m68 + 0x10));
    if (9 < 9) goto loc_0033A7E6;
    Arg1 = (0 * 8 + 59) + ((uint32_t)((uint32_t)(local_rdi)));
    result = ((uint32_t)((uint32_t)(local_rdi))) * (Arg1);
    result = (result) + (Arg4);
    v_stack_m58 = result;
loc_0033A511:
    *(uint64_t *)(local_r14 + local_r10 * 1) = local_r15;
loc_0033A520:
    if (local_rbx != -1) goto loc_0033A671;
loc_0033A52D:
    if (v_stack_p20 != 0) {
    }
    local_r13 = (local_rbx != local_r10) ? 1 : 0;
    local_rsp = (local_rsp) + (96);
    return (uint32_t)((uint32_t)(local_r13));
loc_0033A566:
    Arg4 = 0;
    v_stack_p20 = local_r13;
    result = KeBugCheckEx(Arg4 + 26, (uint32_t)(0x5180ULL), Arg3, Arg4);
loc_0033A57D:
    if (Arg5 != ((uint32_t)(local_r13))) goto loc_0033A820;
loc_0033A58B:
    if (Arg5 >= ((uint32_t)(local_r13))) goto loc_0033A879;
loc_0033A598:
loc_0033A5A2:
    if ((uint32_t)(local_rdi) != 0) goto loc_0033A52D;
    local_rsi = v_stack_p20;
    if (v_stack_p20 != 0) {
        local_rsi = local_r13;
        v_stack_pB8 = local_r13;
    }
    v_stack_pA0 = (uint32_t)(local_r15);
    goto loc_0033A2BC;
loc_0033A5DD:
    Arg1 = (local_r10 + local_r10 * 2) << (4);
    Arg1 = (Arg1) + (0);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (8)) != 0) goto loc_0033A8A2;
loc_0033A5F9:
    v_stack_pA0 = (uint32_t)(local_r13);
    goto loc_0033A210;
loc_0033A610:
    if (local_r10 < (*(uint64_t *)(v_rip + 0xAFB5E9))) goto loc_0033A255;
    result = (*(uint64_t *)(v_rip + 0xAFB5E9)) + (0x800ULL);
    if (local_r10 >= result) goto loc_0033A255;
loc_0033A62F:
    result = MiGetStandbyPageType(local_r10, (uint32_t)(0x5180ULL), local_r13, Arg4);
    v_stack_pA0 = (uint32_t)(result);
    goto loc_0033A2B2;
loc_0033A643:
    if (1 != 0) goto loc_0033A6F0;
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg4 + 0x24))) & (0x1FFFFFULL));
    result = (*(uint64_t *)(Arg4 + 0x18)) >> (40);
    local_rbx = (local_rbx) << (19);
    result = (uint32_t)((result) & (0x7FFFFULL));
loc_0033A666:
    local_rbx = (local_rbx) | (result);
    Arg3 = (local_r13) + 1;
    goto loc_0033A210;
loc_0033A671:
    if (local_rbx < (*(uint64_t *)(v_rip + 0xAFB588))) goto loc_0033A68C;
    result = (*(uint64_t *)(v_rip + 0xAFB588)) + (0x800ULL);
    if (local_rbx < result) goto loc_0033A52D;
loc_0033A68C:
    Arg3 = (local_rbx + local_rbx * 2) + (local_rbx + local_rbx * 2);
    Arg1 = 8;
    if (condition_is_above_or_equal) { Arg1 = (uint32_t)((uint32_t)(0x8000000ULL)); }
    Arg1 = (Arg1) | (*(uint64_t *)(local_r10 + Arg3 * 8));
    *(uint64_t *)(local_r10 + Arg3 * 8) = Arg1;
    goto loc_0033A52D;
loc_0033A6BB:
    if (condition_is_above_or_equal) goto loc_0033A321;
    goto loc_0033A297;
loc_0033A6CB:
    if (local_rsi >= 0) goto loc_0033A74E;
loc_0033A6D3:
    goto loc_0033A4B8;
loc_0033A6DD:
    if (Arg3 < (*(uint64_t *)(local_r10 + 0x10))) goto loc_0033A47D;
    goto loc_0033A44B;
loc_0033A6F0:
    local_rbx = (*(uint64_t *)(0 + 0x1 + 0x28)) & (local_r10);
    result = (*(uint64_t *)(0 + 0x1)) >> (20);
    local_rbx = (local_rbx) | (result);
    result = ((uint32_t)(*(uint32_t *)(0 + 0x1 + 0x24))) & (0xFFFFFFFFFFE00000ULL);
    local_rbx = (local_rbx) >> (20);
    result = (result) << (3);
    goto loc_0033A666;
loc_0033A722:
    Arg1 = (local_r14) >> (4);
    Arg1 = (Arg1) * ((uint32_t)((uint32_t)(Arg1)));
    result = MiSearchChannelTable(Arg1, *(uint64_t *)(local_r10 + Arg3 * 8), Arg3, 0 + 1);
    goto loc_0033A4CC;
loc_0033A746:
    goto loc_0033A319;
loc_0033A74E:
    Arg2 = (*(uint64_t *)(v_rip + 0xAF358B) + *(uint64_t *)(v_rip + 0xAF358B) * 2) << (4);
    Arg2 = (Arg2) + (*(uint64_t *)(v_rip + 0xAF358B));
    if (local_rsi >= Arg2) goto loc_0033A6D3;
    Arg2 = (local_r14) >> (4);
    Arg2 = (Arg2) * ((uint32_t)((uint32_t)(Arg1)));
    if (Arg2 < (*(uint64_t *)(v_rip + 0xAFB486))) goto loc_0033A79A;
    Arg1 = (*(uint64_t *)(v_rip + 0xAFB486)) + (0x800ULL);
    if (Arg2 < Arg1) goto loc_0033A6D3;
loc_0033A79A:
    result = (uint32_t)((result) >> (16));
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) == 6) goto loc_0033A4AD;
    result = MiGetPfnSlabType(local_rsi, Arg2, *(uint8_t *)(result + 0xC), 0 + 1);
    if (((uint32_t)(result)) != 9) goto loc_0033A4AD;
    goto loc_0033A6D3;
loc_0033A7BD:
    if ((uint32_t)(local_rsi) != 0) goto loc_0033A94E;
    v_stack_p20 = local_r13;
    result = KeBugCheckEx(26, (uint32_t)(0x5180ULL), *(uint8_t *)(result + 0xC), result);
loc_0033A7DD:
    goto loc_0033A19A;
loc_0033A7E6:
    if (((uint32_t)(local_rbx)) == 8) goto loc_0033A8F6;
    v_stack_p58 = (uint8_t)(local_r13);
    Arg1 = 0;
loc_0033A7F7:
    Arg2 = ((uint32_t)(0x5180ULL)) * (5 + 0 * 8);
    Arg1 = (5 + 0 * 8) * ((int32_t)((uint32_t)(local_rbx)));
    Arg2 = (Arg2) + (*(uint64_t *)(Arg1 + result * 1 + 0x3D98));
    v_stack_p40 = Arg2;
    goto loc_0033A511;
loc_0033A820:
    if ((*(uint8_t *)(result + 0xC)) > 1) goto loc_0033A58B;
loc_0033A82A:
    if (v_stack_pA0 == 2) goto loc_0033A62F;
    if (*(uint64_t *)(v_rip + 0xAF3434) == 0) goto loc_0033A860;
    result = *(uint64_t *)(v_rip + 0xAF3434);
    local_rbx = *(uint64_t *)((int32_t)((uint32_t)(local_rbx)) + Arg1 * 8);
    if ((((uint8_t)(*(uint64_t *)((int32_t)((uint32_t)(local_rbx)) + Arg1 * 8))) & (16)) == 0) {
        result = ~(*(uint64_t *)(v_rip + 0xAF3434));
        local_rbx = (*(uint64_t *)((int32_t)((uint32_t)(local_rbx)) + Arg1 * 8)) & (result);
    }
    local_rbx = (local_rbx) >> (12);
    local_rbx = (local_rbx) & (result);
    Arg3 = (*(uint8_t *)(result + 0xC)) + 1;
    goto loc_0033A1DC;
loc_0033A879:
    if (local_rsi != 0) {
    }
    v_stack_pB8 = Arg2;
    goto loc_0033A82A;
loc_0033A89A:
    local_r12 = (uint32_t)((local_rbx) - 1);
    goto loc_0033A3F8;
loc_0033A8A2:
    result = MiGetPfnSlabType(Arg1, Arg2, Arg3, result);
    if (((uint32_t)(result)) != 9) goto loc_0033A5F9;
    v_stack_pA0 = 2;
    goto loc_0033A210;
loc_0033A8CA:
    result = MiGetPfnSlabType(Arg1, Arg2, Arg3, result);
    if (((uint32_t)(result)) != 9) goto loc_0033A157;
    goto loc_0033A15A;
loc_0033A8E1:
    goto loc_0033A3F8;
loc_0033A8F6:
    local_rsi = (Arg2) - (Arg1);
    local_rsi = (local_rsi) >> (4);
    local_rsi = (local_rsi) * (Arg1);
    local_rsi = (local_rsi) >> (9);
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0xB02921) + local_rsi * 2 + 0x1)) & (127));
    v_stack_p58 = (uint8_t)(Arg1);
    goto loc_0033A7F7;
loc_0033A934:
    goto loc_0033A520;
loc_0033A943:
    goto loc_0033A3F8;
loc_0033A94E:
    goto loc_0033A44B;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0033A0C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
