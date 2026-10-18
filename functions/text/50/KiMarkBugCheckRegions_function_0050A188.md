# KiMarkBugCheckRegions

- RVA: `0x0050A188`–`0x0050A553` (길이 `971` bytes)
- VA: `0x000000014050A188`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DA1E8`
- 디코드: `263`개 명령, `971/971` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x0050A1C8` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0050A1EC` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0050A234` → [MmIsAddressValid](../27/MmIsAddressValid_function_0027EC50.md) (function, `0x0027EC50`)
- `0x0050A2D1` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0050A314` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0050A345` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0050A357` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0050A362` → [MmIsAddressValid](../27/MmIsAddressValid_function_0027EC50.md) (function, `0x0027EC50`)
- `0x0050A404` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0050A414` → [MmIsAddressValid](../27/MmIsAddressValid_function_0027EC50.md) (function, `0x0027EC50`)
- `0x0050A4AD` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0050A4CC` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0050A4E6` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0050A4F3` → [MmQueryApiSetSchema](../4C/MmQueryApiSetSchema_function_004C013C.md) (function, `0x004C013C`)
- `0x0050A4FC` → [MmIsAddressValid](../27/MmIsAddressValid_function_0027EC50.md) (function, `0x0027EC50`)
- `0x0050A513` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x0050A526` → [sub_0051C6D8](../51/Unknown_function_0051C6D8.md) (function, `0x0051C6D8`)
- `0x0050A53C` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)

### Direct callers
- [KiCollectTriageDumpDataBlocks](../5B/KiCollectTriageDumpDataBlocks_function_005B43F8.md) at `0x005B45A9`

### Static image references
- `0x0050A1AE` → RVA `0x00F49620` (`.data`; read)
- `0x0050A1CD` → RVA `0x00E0F260` (`.data`; read)
- `0x0050A1DE` → RVA `0x00EF0E28` (`.data`; write)
- `0x0050A1E5` → RVA `0x00EF0E28` (`.data`; read)
- `0x0050A203` → RVA `0x00E0F258` (`.data`; read)
- `0x0050A211` → RVA `0x00E0F248` (`.data`; read)
- `0x0050A241` → RVA `0x00FC54C8` (`ALMOSTRO`; read)
- `0x0050A2ED` → RVA `0x00E0F258` (`.data`; write)
- `0x0050A4B7` → RVA `0x01201850` (`CFGRO`; read)
- `0x0050A4D1` → RVA `0x01201860` (`CFGRO`; read)
- `0x0050A52B` → RVA `0x00FC6A48` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0050A188  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0050A18D  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0050A192  55                              push rbp
0050A193  53                              push rbx
0050A194  56                              push rsi
0050A195  57                              push rdi
0050A196  41 54                           push r12
0050A198  41 55                           push r13
0050A19A  41 56                           push r14
0050A19C  41 57                           push r15
0050A19E  48 8B EC                        mov rbp, rsp
0050A1A1  48 83 EC 48                     sub rsp, 0x48
0050A1A5  4D 8B E9                        mov r13, r9
0050A1A8  4D 8B E0                        mov r12, r8
0050A1AB  0F AE E8                        lfence
0050A1AE  8B 05 6C F4 A3 00               mov eax, dword ptr [rip + 0xa3f46c]
0050A1B4  41 BF 04 00 00 00               mov r15d, 4
0050A1BA  85 C0                           test eax, eax
0050A1BC  74 0F                           je 0x14050a1cd
0050A1BE  41 8B D7                        mov edx, r15d
0050A1C1  48 8D 0D 58 F4 A3 00            lea rcx, [rip + 0xa3f458]
0050A1C8  E8 A7 E1 F1 FF                  call 0x140428374
0050A1CD  48 8B 05 8C 50 90 00            mov rax, qword ptr [rip + 0x90508c]
0050A1D4  48 85 C0                        test rax, rax
0050A1D7  74 18                           je 0x14050a1f1
0050A1D9  BA 08 00 00 00                  mov edx, 8
0050A1DE  48 89 05 43 6C 9E 00            mov qword ptr [rip + 0x9e6c43], rax
0050A1E5  48 8D 0D 3C 6C 9E 00            lea rcx, [rip + 0x9e6c3c]
0050A1EC  E8 83 E1 F1 FF                  call 0x140428374
0050A1F1  BE 03 00 00 00                  mov esi, 3
0050A1F6  41 81 FD 01 01 00 00            cmp r13d, 0x101
0050A1FD  0F 85 F4 00 00 00               jne 0x14050a2f7
0050A203  8B 05 4F 50 90 00               mov eax, dword ptr [rip + 0x90504f]
0050A209  85 C0                           test eax, eax
0050A20B  0F 84 E6 00 00 00               je 0x14050a2f7
0050A211  4C 8B 35 30 50 90 00            mov r14, qword ptr [rip + 0x905030]
0050A218  33 FF                           xor edi, edi
0050A21A  85 C0                           test eax, eax
0050A21C  0F 84 CB 00 00 00               je 0x14050a2ed
0050A222  0F AE E8                        lfence
0050A225  8B DF                           mov ebx, edi
0050A227  49 03 DE                        add rbx, r14
0050A22A  48 81 E3 00 F0 FF FF            and rbx, 0xfffffffffffff000
0050A231  48 8B CB                        mov rcx, rbx
0050A234  E8 17 4A D7 FF                  call 0x14027ec50
0050A239  84 C0                           test al, al
0050A23B  0F 84 9A 00 00 00               je 0x14050a2db
0050A241  48 8B 05 80 B2 AB 00            mov rax, qword ptr [rip + 0xabb280]
0050A248  48 C1 EB 09                     shr rbx, 9
0050A24C  48 8D 4D D8                     lea rcx, [rbp - 0x28]
0050A250  49 B8 F8 FF FF FF 7F 00 00 00   movabs r8, 0x7ffffffff8
0050A25A  49 8B D7                        mov rdx, r15
0050A25D  49 23 D8                        and rbx, r8
0050A260  48 03 D8                        add rbx, rax
0050A263  48 89 19                        mov qword ptr [rcx], rbx
0050A266  48 8B 05 5B B2 AB 00            mov rax, qword ptr [rip + 0xabb25b]
0050A26D  48 C1 EB 09                     shr rbx, 9
0050A271  48 8D 49 08                     lea rcx, [rcx + 8]
0050A275  49 23 D8                        and rbx, r8
0050A278  48 03 D8                        add rbx, rax
0050A27B  48 83 EA 01                     sub rdx, 1
0050A27F  75 E2                           jne 0x14050a263
0050A281  45 33 C9                        xor r9d, r9d
0050A284  8B D6                           mov edx, esi
0050A286  44 8B C2                        mov r8d, edx
0050A289  45 85 C9                        test r9d, r9d
0050A28C  75 1F                           jne 0x14050a2ad
0050A28E  85 D2                           test edx, edx
0050A290  74 2A                           je 0x14050a2bc
0050A292  8B C2                           mov eax, edx
0050A294  48 8B 4C C5 D8                  mov rcx, qword ptr [rbp + rax*8 - 0x28]
0050A299  8B 01                           mov eax, dword ptr [rcx]
0050A29B  C0 E8 07                        shr al, 7
0050A29E  A8 01                           test al, 1
0050A2A0  74 13                           je 0x14050a2b5
0050A2A2  FF CA                           dec edx
0050A2A4  41 B9 01 00 00 00               mov r9d, 1
0050A2AA  44 8B C2                        mov r8d, edx
0050A2AD  8B C2                           mov eax, edx
0050A2AF  48 83 64 C5 D8 00               and qword ptr [rbp + rax*8 - 0x28], 0
0050A2B5  FF CA                           dec edx
0050A2B7  45 85 C0                        test r8d, r8d
0050A2BA  75 CA                           jne 0x14050a286
0050A2BC  41 8B DF                        mov ebx, r15d
0050A2BF  8D 43 FF                        lea eax, [rbx - 1]
0050A2C2  48 8B 4C C5 D8                  mov rcx, qword ptr [rbp + rax*8 - 0x28]
0050A2C7  48 85 C9                        test rcx, rcx
0050A2CA  74 0F                           je 0x14050a2db
0050A2CC  BA 08 00 00 00                  mov edx, 8
0050A2D1  E8 9E E0 F1 FF                  call 0x140428374
0050A2D6  83 C3 FF                        add ebx, -1
0050A2D9  75 E4                           jne 0x14050a2bf
0050A2DB  81 C7 00 10 00 00               add edi, 0x1000
0050A2E1  3B 3D 71 4F 90 00               cmp edi, dword ptr [rip + 0x904f71]
0050A2E7  0F 82 35 FF FF FF               jb 0x14050a222
0050A2ED  C7 05 61 4F 90 00 00 10 00 00   mov dword ptr [rip + 0x904f61], 0x1000
0050A2F7  48 8D 3D 4A 4F 90 00            lea rdi, [rip + 0x904f4a]
0050A2FE  41 BE 02 00 00 00               mov r14d, 2
0050A304  48 8D 1D 4D 4F 90 00            lea rbx, [rip + 0x904f4d]
0050A30B  8B 13                           mov edx, dword ptr [rbx]
0050A30D  85 D2                           test edx, edx
0050A30F  74 08                           je 0x14050a319
0050A311  48 8B 0F                        mov rcx, qword ptr [rdi]
0050A314  E8 5B E0 F1 FF                  call 0x140428374
0050A319  49 03 DF                        add rbx, r15
0050A31C  48 83 C7 08                     add rdi, 8
0050A320  49 83 EE 01                     sub r14, 1
0050A324  75 E5                           jne 0x14050a30b
0050A326  4D 85 E4                        test r12, r12
0050A329  0F 84 E9 01 00 00               je 0x14050a518
0050A32F  49 8B DC                        mov rbx, r12
0050A332  41 BE 00 10 00 00               mov r14d, 0x1000
0050A338  48 81 E3 00 F0 FF FF            and rbx, 0xfffffffffffff000
0050A33F  41 8B D6                        mov edx, r14d
0050A342  48 8B CB                        mov rcx, rbx
0050A345  E8 2A E0 F1 FF                  call 0x140428374
0050A34A  48 8D BB 00 10 00 00            lea rdi, [rbx + 0x1000]
0050A351  41 8B D6                        mov edx, r14d
0050A354  48 8B CF                        mov rcx, rdi
0050A357  E8 18 E0 F1 FF                  call 0x140428374
0050A35C  0F AE E8                        lfence
0050A35F  48 8B CB                        mov rcx, rbx
0050A362  E8 E9 48 D7 FF                  call 0x14027ec50
0050A367  84 C0                           test al, al
0050A369  0F 84 9F 00 00 00               je 0x14050a40e
0050A36F  48 8B 05 52 B1 AB 00            mov rax, qword ptr [rip + 0xabb152]
0050A376  48 C1 EB 09                     shr rbx, 9
0050A37A  48 8D 4D D8                     lea rcx, [rbp - 0x28]
0050A37E  49 B8 F8 FF FF FF 7F 00 00 00   movabs r8, 0x7ffffffff8
0050A388  49 8B D7                        mov rdx, r15
0050A38B  49 23 D8                        and rbx, r8
0050A38E  48 03 D8                        add rbx, rax
0050A391  48 89 19                        mov qword ptr [rcx], rbx
0050A394  48 8B 05 2D B1 AB 00            mov rax, qword ptr [rip + 0xabb12d]
0050A39B  48 C1 EB 09                     shr rbx, 9
0050A39F  48 8D 49 08                     lea rcx, [rcx + 8]
0050A3A3  49 23 D8                        and rbx, r8
0050A3A6  48 03 D8                        add rbx, rax
0050A3A9  48 83 EA 01                     sub rdx, 1
0050A3AD  75 E2                           jne 0x14050a391
0050A3AF  45 33 C9                        xor r9d, r9d
0050A3B2  8B D6                           mov edx, esi
0050A3B4  41 83 CE FF                     or r14d, 0xffffffff
0050A3B8  44 8B C2                        mov r8d, edx
0050A3BB  45 85 C9                        test r9d, r9d
0050A3BE  75 1F                           jne 0x14050a3df
0050A3C0  85 D2                           test edx, edx
0050A3C2  74 2B                           je 0x14050a3ef
0050A3C4  8B C2                           mov eax, edx
0050A3C6  48 8B 4C C5 D8                  mov rcx, qword ptr [rbp + rax*8 - 0x28]
0050A3CB  8B 01                           mov eax, dword ptr [rcx]
0050A3CD  C0 E8 07                        shr al, 7
0050A3D0  A8 01                           test al, 1
0050A3D2  74 13                           je 0x14050a3e7
0050A3D4  FF CA                           dec edx
0050A3D6  41 B9 01 00 00 00               mov r9d, 1
0050A3DC  44 8B C2                        mov r8d, edx
0050A3DF  8B C2                           mov eax, edx
0050A3E1  48 83 64 C5 D8 00               and qword ptr [rbp + rax*8 - 0x28], 0
0050A3E7  41 03 D6                        add edx, r14d
0050A3EA  45 85 C0                        test r8d, r8d
0050A3ED  75 C9                           jne 0x14050a3b8
0050A3EF  41 8B DF                        mov ebx, r15d
0050A3F2  8D 43 FF                        lea eax, [rbx - 1]
0050A3F5  48 8B 4C C5 D8                  mov rcx, qword ptr [rbp + rax*8 - 0x28]
0050A3FA  48 85 C9                        test rcx, rcx
0050A3FD  74 0F                           je 0x14050a40e
0050A3FF  BA 08 00 00 00                  mov edx, 8
0050A404  E8 6B DF F1 FF                  call 0x140428374
0050A409  41 03 DE                        add ebx, r14d
0050A40C  75 E4                           jne 0x14050a3f2
0050A40E  0F AE E8                        lfence
0050A411  48 8B CF                        mov rcx, rdi
0050A414  E8 37 48 D7 FF                  call 0x14027ec50
0050A419  84 C0                           test al, al
0050A41B  0F 84 96 00 00 00               je 0x14050a4b7
0050A421  48 8B 05 A0 B0 AB 00            mov rax, qword ptr [rip + 0xabb0a0]
0050A428  48 C1 EF 09                     shr rdi, 9
0050A42C  48 8D 4D D8                     lea rcx, [rbp - 0x28]
0050A430  49 B8 F8 FF FF FF 7F 00 00 00   movabs r8, 0x7ffffffff8
0050A43A  49 8B D7                        mov rdx, r15
0050A43D  49 23 F8                        and rdi, r8
0050A440  48 03 F8                        add rdi, rax
0050A443  48 89 39                        mov qword ptr [rcx], rdi
0050A446  48 8B 05 7B B0 AB 00            mov rax, qword ptr [rip + 0xabb07b]
0050A44D  48 C1 EF 09                     shr rdi, 9
0050A451  48 8D 49 08                     lea rcx, [rcx + 8]
0050A455  49 23 F8                        and rdi, r8
0050A458  48 03 F8                        add rdi, rax
0050A45B  48 83 EA 01                     sub rdx, 1
0050A45F  75 E2                           jne 0x14050a443
0050A461  45 33 C0                        xor r8d, r8d
0050A464  83 CB FF                        or ebx, 0xffffffff
0050A467  8B D6                           mov edx, esi
0050A469  45 85 C0                        test r8d, r8d
0050A46C  75 1E                           jne 0x14050a48c
0050A46E  85 F6                           test esi, esi
0050A470  74 28                           je 0x14050a49a
0050A472  8B C6                           mov eax, esi
0050A474  48 8B 4C C5 D8                  mov rcx, qword ptr [rbp + rax*8 - 0x28]
0050A479  8B 01                           mov eax, dword ptr [rcx]
0050A47B  C0 E8 07                        shr al, 7
0050A47E  A8 01                           test al, 1
0050A480  74 12                           je 0x14050a494
0050A482  FF CE                           dec esi
0050A484  41 B8 01 00 00 00               mov r8d, 1
0050A48A  8B D6                           mov edx, esi
0050A48C  8B C6                           mov eax, esi
0050A48E  48 83 64 C5 D8 00               and qword ptr [rbp + rax*8 - 0x28], 0
0050A494  03 F3                           add esi, ebx
0050A496  85 D2                           test edx, edx
0050A498  75 CD                           jne 0x14050a467
0050A49A  41 8D 47 FF                     lea eax, [r15 - 1]
0050A49E  48 8B 4C C5 D8                  mov rcx, qword ptr [rbp + rax*8 - 0x28]
0050A4A3  48 85 C9                        test rcx, rcx
0050A4A6  74 0F                           je 0x14050a4b7
0050A4A8  BA 08 00 00 00                  mov edx, 8
0050A4AD  E8 C2 DE F1 FF                  call 0x140428374
0050A4B2  44 03 FB                        add r15d, ebx
0050A4B5  75 E3                           jne 0x14050a49a
0050A4B7  4C 3B 25 92 73 CF 00            cmp r12, qword ptr [rip + 0xcf7392]
0050A4BE  75 11                           jne 0x14050a4d1
0050A4C0  BA 08 00 00 00                  mov edx, 8
0050A4C5  48 8D 0D 84 73 CF 00            lea rcx, [rip + 0xcf7384]
0050A4CC  E8 A3 DE F1 FF                  call 0x140428374
0050A4D1  4C 3B 25 88 73 CF 00            cmp r12, qword ptr [rip + 0xcf7388]
0050A4D8  75 11                           jne 0x14050a4eb
0050A4DA  BA 08 00 00 00                  mov edx, 8
0050A4DF  48 8D 0D 7A 73 CF 00            lea rcx, [rip + 0xcf737a]
0050A4E6  E8 89 DE F1 FF                  call 0x140428374
0050A4EB  48 8D 55 60                     lea rdx, [rbp + 0x60]
0050A4EF  48 8D 4D 58                     lea rcx, [rbp + 0x58]
0050A4F3  E8 44 5C FB FF                  call 0x1404c013c
0050A4F8  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
0050A4FC  E8 4F 47 D7 FF                  call 0x14027ec50
0050A501  84 C0                           test al, al
0050A503  74 13                           je 0x14050a518
0050A505  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
0050A509  4C 3B 21                        cmp r12, qword ptr [rcx]
0050A50C  75 0A                           jne 0x14050a518
0050A50E  BA 08 00 00 00                  mov edx, 8
0050A513  E8 5C DE F1 FF                  call 0x140428374
0050A518  48 8B 55 50                     mov rdx, qword ptr [rbp + 0x50]
0050A51C  4D 8B CD                        mov r9, r13
0050A51F  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
0050A523  4D 8B C4                        mov r8, r12
0050A526  E8 AD 21 01 00                  call 0x14051c6d8
0050A52B  48 8B 0D 16 C5 AB 00            mov rcx, qword ptr [rip + 0xabc516]
0050A532  48 85 C9                        test rcx, rcx
0050A535  74 0A                           je 0x14050a541
0050A537  BA E8 0A 00 00                  mov edx, 0xae8
0050A53C  E8 33 DE F1 FF                  call 0x140428374
0050A541  48 83 C4 48                     add rsp, 0x48
0050A545  41 5F                           pop r15
0050A547  41 5E                           pop r14
0050A549  41 5D                           pop r13
0050A54B  41 5C                           pop r12
0050A54D  5F                              pop rdi
0050A54E  5E                              pop rsi
0050A54F  5B                              pop rbx
0050A550  5D                              pop rbp
0050A551  C3                              ret
0050A552  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiMarkBugCheckRegions(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (72);
    result = (unsigned int)(*(unsigned int *)(v_rip + 10744940));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10744940))) != 0) {
        a2 = 4;
        a1 = v_rip + 10744920;
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
    }
    result = *(unsigned __int64 *)(v_rip + 9457804);
    if (*(unsigned __int64 *)(v_rip + 9457804) != 0) {
        a2 = 8;
        *(unsigned __int64 *)(v_rip + 10382403) = *(unsigned __int64 *)(v_rip + 9457804);
        a1 = v_rip + 10382396;
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
    }
    if (((unsigned int)(a4)) != 257) goto loc_0050A2F7;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9457743))) == 0) goto loc_0050A2F7;
    v_rdi = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9457743))) == 0) goto loc_0050A2ED;
loc_0050A222:
    v_rbx = (0) + (*(unsigned __int64 *)(v_rip + 9457712));
    v_rbx = (v_rbx) & (0xFFFFFFFFFFFFF000ULL);
    result = MmIsAddressValid(v_rbx, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0050A2DB;
    v_rbx = (v_rbx) >> (9);
    v_rbx = (v_rbx) & (a3);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_rip + 11252352));
loc_0050A263:
    *(unsigned __int64 *)(v_stack_m68) = v_rbx;
    v_rbx = (v_rbx) >> (9);
    v_rbx = (v_rbx) & (a3);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_rip + 11252315));
    a2 = (4) - (1);
    if (condition_is_not_equal) goto loc_0050A263;
    a4 = 0;
loc_0050A286:
    if (0 != 0) goto loc_0050A2AD;
    if (3 == 0) goto loc_0050A2BC;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp + 3 * 8 - 40)))) >> (7));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_0050A2B5;
    a2 = (unsigned int)((3) - 1);
loc_0050A2AD:
loc_0050A2B5:
    a2 = (unsigned int)((a2) - 1);
    if ((unsigned int)((unsigned int)((unsigned int)(a2))) != 0) goto loc_0050A286;
loc_0050A2BC:
loc_0050A2BF:
    if (*(unsigned __int64 *)(v_rsp + 4 - 1 * 8 - 40) == 0) goto loc_0050A2DB;
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(v_rsp + 4 - 1 * 8 - 40), 8, (unsigned int)((unsigned int)(a2)), 1);
    v_rbx = (unsigned int)((4) + (-1));
    if (condition_is_not_equal) goto loc_0050A2BF;
loc_0050A2DB:
    v_rdi = (unsigned int)((v_rdi) + (0x1000ULL));
    if (((unsigned int)(v_rdi)) < (*(unsigned int *)(v_rip + 9457521))) goto loc_0050A222;
loc_0050A2ED:
    *(unsigned int *)(v_rip + 9457505) = 0x1000ULL;
loc_0050A2F7:
loc_0050A30B:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9457485))) != 0) {
        a1 = *(unsigned __int64 *)(v_rip + 9457482);
        result = IoAddTriageDumpDataBlock(a1, (unsigned int)(*(unsigned int *)(v_rip + 9457485)), (unsigned int)((unsigned int)(a2)), 1);
    }
    v_rbx = (v_rip + 9457485) + (4);
    v_rdi = (v_rip + 9457482) + (8);
    v_r14 = (2) - (1);
    if (condition_is_not_equal) goto loc_0050A30B;
    if (a3 == 0) goto loc_0050A518;
    v_rbx = (a3) & (0xFFFFFFFFFFFFF000ULL);
    result = IoAddTriageDumpDataBlock(v_rbx, (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))), (unsigned int)((unsigned int)(a2)), 1);
    result = IoAddTriageDumpDataBlock(v_rbx + 4096, (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))), (unsigned int)((unsigned int)(a2)), 1);
    result = MmIsAddressValid(v_rbx, (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))), (unsigned int)((unsigned int)(a2)), 1);
    if ((unsigned __int8)(result) == 0) goto loc_0050A40E;
    v_rbx = (v_rbx) >> (9);
    v_rbx = (v_rbx) & ((unsigned int)((unsigned int)(a2)));
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_rip + 11252050));
loc_0050A391:
    *(unsigned __int64 *)(v_stack_m68) = v_rbx;
    v_rbx = (v_rbx) >> (9);
    v_rbx = (v_rbx) & ((unsigned int)((unsigned int)(a2)));
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_rip + 11252013));
    a2 = (4) - (1);
    if (condition_is_not_equal) goto loc_0050A391;
    a4 = 0;
    v_r14 = (unsigned int)(((unsigned int)(0x1000ULL)) | (0xFFFFFFFFULL));
loc_0050A3B8:
    if (0 != 0) goto loc_0050A3DF;
    if (3 == 0) goto loc_0050A3EF;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp + 3 * 8 - 40)))) >> (7));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_0050A3E7;
    a2 = (unsigned int)((3) - 1);
loc_0050A3DF:
loc_0050A3E7:
    a2 = (unsigned int)((a2) + ((unsigned int)(v_r14)));
    if ((unsigned int)((unsigned int)((unsigned int)(a2))) != 0) goto loc_0050A3B8;
loc_0050A3EF:
loc_0050A3F2:
    if (*(unsigned __int64 *)(v_rsp + 4 - 1 * 8 - 40) == 0) goto loc_0050A40E;
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(v_rsp + 4 - 1 * 8 - 40), 8, (unsigned int)((unsigned int)(a2)), 1);
    v_rbx = (unsigned int)((4) + ((unsigned int)(v_r14)));
    if (condition_is_not_equal) goto loc_0050A3F2;
loc_0050A40E:
    result = MmIsAddressValid(v_rbx + 4096, 8, (unsigned int)((unsigned int)(a2)), 1);
    if ((unsigned __int8)(result) == 0) goto loc_0050A4B7;
    v_rdi = (v_rbx + 4096) >> (9);
    v_rdi = (v_rdi) & ((unsigned int)((unsigned int)(a2)));
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_rip + 11251872));
loc_0050A443:
    *(unsigned __int64 *)(v_stack_m68) = v_rdi;
    v_rdi = (v_rdi) >> (9);
    v_rdi = (v_rdi) & ((unsigned int)((unsigned int)(a2)));
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_rip + 11251835));
    a2 = (4) - (1);
    if (condition_is_not_equal) goto loc_0050A443;
    a3 = 0;
    v_rbx = (unsigned int)((v_rbx) | (0xFFFFFFFFULL));
loc_0050A467:
    if (0 != 0) goto loc_0050A48C;
    if (3 == 0) goto loc_0050A49A;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp + 3 * 8 - 40)))) >> (7));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_0050A494;
    v_rsi = (unsigned int)((3) - 1);
loc_0050A48C:
loc_0050A494:
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(v_rbx)));
    if ((unsigned int)((unsigned int)((unsigned int)(v_rsi))) != 0) goto loc_0050A467;
loc_0050A49A:
    if (*(unsigned __int64 *)(v_rsp + 4 - 1 * 8 - 40) == 0) goto loc_0050A4B7;
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(v_rsp + 4 - 1 * 8 - 40), 8, 1, 1);
    v_r15 = (unsigned int)((4) + ((unsigned int)(v_rbx)));
    if (condition_is_not_equal) goto loc_0050A49A;
loc_0050A4B7:
    if (0 == (*(unsigned __int64 *)(v_rip + 13595538))) {
        a2 = 8;
        a1 = v_rip + 13595524;
        result = IoAddTriageDumpDataBlock(a1, a2, 1, 1);
    }
    if (0 == (*(unsigned __int64 *)(v_rip + 13595528))) {
        a2 = 8;
        a1 = v_rip + 13595514;
        result = IoAddTriageDumpDataBlock(a1, a2, 1, 1);
    }
    result = MmQueryApiSetSchema(v_stack_p18, v_stack_p20, 1, 1);
    result = MmIsAddressValid(v_stack_p18, v_stack_p20, 1, 1);
    if ((unsigned __int8)(result) == 0) goto loc_0050A518;
    if (0 == (*(unsigned __int64 *)(v_stack_p18))) {
        a2 = 8;
        result = IoAddTriageDumpDataBlock(v_stack_p18, a2, 1, 1);
    }
    result = sub_0051C6D8(v_stack_p8, v_stack_p10, 0, 0);
    if (*(unsigned __int64 *)(v_rip + 11257110) != 0) {
        a2 = 0xAE8ULL;
        result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(v_rip + 11257110), a2, 0, 0);
    }
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiMarkBugCheckRegions(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (72);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xA3F46C));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA3F46C))) != 0) {
        Arg2 = 4;
        Arg1 = v_rip + 10744920;
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, Arg3, Arg4);
    }
    result = *(uint64_t *)(v_rip + 0x90508C);
    if (*(uint64_t *)(v_rip + 0x90508C) != 0) {
        Arg2 = 8;
        *(uint64_t *)(v_rip + 0x9E6C43) = *(uint64_t *)(v_rip + 0x90508C);
        Arg1 = v_rip + 10382396;
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, Arg3, Arg4);
    }
    if (((uint32_t)(Arg4)) != 257) goto loc_0050A2F7;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x90504F))) == 0) goto loc_0050A2F7;
    local_rdi = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x90504F))) == 0) goto loc_0050A2ED;
loc_0050A222:
    local_rbx = (0) + (*(uint64_t *)(v_rip + 0x905030));
    local_rbx = (local_rbx) & (0xFFFFFFFFFFFFF000ULL);
    result = MmIsAddressValid(local_rbx, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0050A2DB;
    local_rbx = (local_rbx) >> (9);
    local_rbx = (local_rbx) & (Arg3);
    local_rbx = (local_rbx) + (*(uint64_t *)(v_rip + 0xABB280));
loc_0050A263:
    *(uint64_t *)(v_stack_m68) = local_rbx;
    local_rbx = (local_rbx) >> (9);
    local_rbx = (local_rbx) & (Arg3);
    local_rbx = (local_rbx) + (*(uint64_t *)(v_rip + 0xABB25B));
    Arg2 = (4) - (1);
    if (condition_is_not_equal) goto loc_0050A263;
    Arg4 = 0;
loc_0050A286:
    if (0 != 0) goto loc_0050A2AD;
    if (3 == 0) goto loc_0050A2BC;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp + 0x3 * 8 - 0x28)))) >> (7));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_0050A2B5;
    Arg2 = (uint32_t)((3) - 1);
loc_0050A2AD:
loc_0050A2B5:
    Arg2 = (uint32_t)((Arg2) - 1);
    if ((uint32_t)((uint32_t)((uint32_t)(Arg2))) != 0) goto loc_0050A286;
loc_0050A2BC:
loc_0050A2BF:
    if (*(uint64_t *)(local_rsp + 0x4 - 0x1 * 8 - 0x28) == 0) goto loc_0050A2DB;
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(local_rsp + 0x4 - 0x1 * 8 - 0x28), 8, (uint32_t)((uint32_t)(Arg2)), 1);
    local_rbx = (uint32_t)((4) + (-1));
    if (condition_is_not_equal) goto loc_0050A2BF;
loc_0050A2DB:
    local_rdi = (uint32_t)((local_rdi) + (0x1000ULL));
    if (((uint32_t)(local_rdi)) < (*(uint32_t *)(v_rip + 0x904F71))) goto loc_0050A222;
loc_0050A2ED:
    *(uint32_t *)(v_rip + 0x904F61) = 0x1000ULL;
loc_0050A2F7:
loc_0050A30B:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x904F4D))) != 0) {
        Arg1 = *(uint64_t *)(v_rip + 0x904F4A);
        result = IoAddTriageDumpDataBlock(Arg1, (uint32_t)(*(uint32_t *)(v_rip + 0x904F4D)), (uint32_t)((uint32_t)(Arg2)), 1);
    }
    local_rbx = (v_rip + 9457485) + (4);
    local_rdi = (v_rip + 9457482) + (8);
    local_r14 = (2) - (1);
    if (condition_is_not_equal) goto loc_0050A30B;
    if (Arg3 == 0) goto loc_0050A518;
    local_rbx = (Arg3) & (0xFFFFFFFFFFFFF000ULL);
    result = IoAddTriageDumpDataBlock(local_rbx, (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))), (uint32_t)((uint32_t)(Arg2)), 1);
    result = IoAddTriageDumpDataBlock(local_rbx + 4096, (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))), (uint32_t)((uint32_t)(Arg2)), 1);
    result = MmIsAddressValid(local_rbx, (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))), (uint32_t)((uint32_t)(Arg2)), 1);
    if ((uint8_t)(result) == 0) goto loc_0050A40E;
    local_rbx = (local_rbx) >> (9);
    local_rbx = (local_rbx) & ((uint32_t)((uint32_t)(Arg2)));
    local_rbx = (local_rbx) + (*(uint64_t *)(v_rip + 0xABB152));
loc_0050A391:
    *(uint64_t *)(v_stack_m68) = local_rbx;
    local_rbx = (local_rbx) >> (9);
    local_rbx = (local_rbx) & ((uint32_t)((uint32_t)(Arg2)));
    local_rbx = (local_rbx) + (*(uint64_t *)(v_rip + 0xABB12D));
    Arg2 = (4) - (1);
    if (condition_is_not_equal) goto loc_0050A391;
    Arg4 = 0;
    local_r14 = (uint32_t)(((uint32_t)(0x1000ULL)) | (0xFFFFFFFFULL));
loc_0050A3B8:
    if (0 != 0) goto loc_0050A3DF;
    if (3 == 0) goto loc_0050A3EF;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp + 0x3 * 8 - 0x28)))) >> (7));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_0050A3E7;
    Arg2 = (uint32_t)((3) - 1);
loc_0050A3DF:
loc_0050A3E7:
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r14)));
    if ((uint32_t)((uint32_t)((uint32_t)(Arg2))) != 0) goto loc_0050A3B8;
loc_0050A3EF:
loc_0050A3F2:
    if (*(uint64_t *)(local_rsp + 0x4 - 0x1 * 8 - 0x28) == 0) goto loc_0050A40E;
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(local_rsp + 0x4 - 0x1 * 8 - 0x28), 8, (uint32_t)((uint32_t)(Arg2)), 1);
    local_rbx = (uint32_t)((4) + ((uint32_t)(local_r14)));
    if (condition_is_not_equal) goto loc_0050A3F2;
loc_0050A40E:
    result = MmIsAddressValid(local_rbx + 4096, 8, (uint32_t)((uint32_t)(Arg2)), 1);
    if ((uint8_t)(result) == 0) goto loc_0050A4B7;
    local_rdi = (local_rbx + 4096) >> (9);
    local_rdi = (local_rdi) & ((uint32_t)((uint32_t)(Arg2)));
    local_rdi = (local_rdi) + (*(uint64_t *)(v_rip + 0xABB0A0));
loc_0050A443:
    *(uint64_t *)(v_stack_m68) = local_rdi;
    local_rdi = (local_rdi) >> (9);
    local_rdi = (local_rdi) & ((uint32_t)((uint32_t)(Arg2)));
    local_rdi = (local_rdi) + (*(uint64_t *)(v_rip + 0xABB07B));
    Arg2 = (4) - (1);
    if (condition_is_not_equal) goto loc_0050A443;
    Arg3 = 0;
    local_rbx = (uint32_t)((local_rbx) | (0xFFFFFFFFULL));
loc_0050A467:
    if (0 != 0) goto loc_0050A48C;
    if (3 == 0) goto loc_0050A49A;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp + 0x3 * 8 - 0x28)))) >> (7));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_0050A494;
    local_rsi = (uint32_t)((3) - 1);
loc_0050A48C:
loc_0050A494:
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(local_rbx)));
    if ((uint32_t)((uint32_t)((uint32_t)(local_rsi))) != 0) goto loc_0050A467;
loc_0050A49A:
    if (*(uint64_t *)(local_rsp + 0x4 - 0x1 * 8 - 0x28) == 0) goto loc_0050A4B7;
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(local_rsp + 0x4 - 0x1 * 8 - 0x28), 8, 1, 1);
    local_r15 = (uint32_t)((4) + ((uint32_t)(local_rbx)));
    if (condition_is_not_equal) goto loc_0050A49A;
loc_0050A4B7:
    if (0 == (*(uint64_t *)(v_rip + 0xCF7392))) {
        Arg2 = 8;
        Arg1 = v_rip + 13595524;
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, 1, 1);
    }
    if (0 == (*(uint64_t *)(v_rip + 0xCF7388))) {
        Arg2 = 8;
        Arg1 = v_rip + 13595514;
        result = IoAddTriageDumpDataBlock(Arg1, Arg2, 1, 1);
    }
    result = MmQueryApiSetSchema(v_stack_p18, v_stack_p20, 1, 1);
    result = MmIsAddressValid(v_stack_p18, v_stack_p20, 1, 1);
    if ((uint8_t)(result) == 0) goto loc_0050A518;
    if (0 == (*(uint64_t *)(v_stack_p18))) {
        Arg2 = 8;
        result = IoAddTriageDumpDataBlock(v_stack_p18, Arg2, 1, 1);
    }
    result = sub_0051C6D8(v_stack_p8, v_stack_p10, 0, 0);
    if (*(uint64_t *)(v_rip + 0xABC516) != 0) {
        Arg2 = 0xAE8ULL;
        result = IoAddTriageDumpDataBlock(*(uint64_t *)(v_rip + 0xABC516), Arg2, 0, 0);
    }
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0050A188&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
