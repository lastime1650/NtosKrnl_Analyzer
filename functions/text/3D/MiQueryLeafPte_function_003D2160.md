# MiQueryLeafPte

- RVA: `0x003D2160`–`0x003D26AE` (길이 `1,358` bytes)
- VA: `0x00000001403D2160`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000913A8`
- 디코드: `316`개 명령, `1,358/1,358` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x003D2337` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003D244D` → [MiLocateCloneAddress](MiLocateCloneAddress_function_003D26B4.md) (function, `0x003D26B4`)
- `0x003D25A8` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003D2671` → [MiIdentifyPfnWrapper](../31/MiIdentifyPfnWrapper_function_0031C8F0.md) (function, `0x0031C8F0`)

### Direct callers
- [MiWalkPageTablesRecursively](../27/MiWalkPageTablesRecursively_function_002796C0.md) at `0x0027A414`

### Static image references
- `0x003D2197` → RVA `0x00E2F388` (`.data`; read)
- `0x003D2236` → RVA `0x00E2DBC0` (`.data`; read)
- `0x003D223D` → RVA `0x00E2DBC4` (`.data`; read)
- `0x003D2252` → RVA `0x00E2DC20` (`.data`; read)
- `0x003D229F` → RVA `0x00E2DBC0` (`.data`; write)
- `0x003D247C` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x003D2556` → RVA `0x00E2F3A0` (`.data`; read)
- `0x003D25F4` → RVA `0x00011070` (`.rdata`; read)
- `0x003D2684` → RVA `0x00E2F3B0` (`.data`; write)
- `0x003D268F` → RVA `0x00E2F3A0` (`.data`; write)
- `0x003D2696` → RVA `0x00E2F3A8` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003D2160  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
003D2165  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
003D216A  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
003D216F  41 56                           push r14
003D2171  48 83 EC 30                     sub rsp, 0x30
003D2175  4C 8B 89 B8 00 00 00            mov r9, qword ptr [rcx + 0xb8]
003D217C  48 8B FA                        mov rdi, rdx
003D217F  48 C1 E7 19                     shl rdi, 0x19
003D2183  49 BE 00 00 00 00 80 F6 FF FF   movabs r14, 0xfffff68000000000
003D218D  49 8B C6                        mov rax, r14
003D2190  48 C1 E0 19                     shl rax, 0x19
003D2194  48 2B F8                        sub rdi, rax
003D2197  48 8B 05 EA D1 A5 00            mov rax, qword ptr [rip + 0xa5d1ea]
003D219E  48 C1 FF 10                     sar rdi, 0x10
003D21A2  48 3B F8                        cmp rdi, rax
003D21A5  0F 83 AB 03 00 00               jae 0x1403d2556
003D21AB  41 83 F8 01                     cmp r8d, 1
003D21AF  0F 8D 58 01 00 00               jge 0x1403d230d
003D21B5  48 8B 02                        mov rax, qword ptr [rdx]
003D21B8  A8 01                           test al, 1
003D21BA  0F 84 4D 01 00 00               je 0x1403d230d
003D21C0  48 C1 E8 0C                     shr rax, 0xc
003D21C4  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
003D21CE  48 23 C1                        and rax, rcx
003D21D1  4C 8D 04 40                     lea r8, [rax + rax*2]
003D21D5  49 C1 E0 04                     shl r8, 4
003D21D9  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
003D21E3  49 8D 34 00                     lea rsi, [r8 + rax]
003D21E7  41 8B 01                        mov eax, dword ptr [r9]
003D21EA  A8 01                           test al, 1
003D21EC  0F 84 45 04 00 00               je 0x1403d2637
003D21F2  49 8B 49 10                     mov rcx, qword ptr [r9 + 0x10]
003D21F6  48 FF C1                        inc rcx
003D21F9  49 89 49 10                     mov qword ptr [r9 + 0x10], rcx
003D21FD  49 3B 49 18                     cmp rcx, qword ptr [r9 + 0x18]
003D2201  0F 83 4E 04 00 00               jae 0x1403d2655
003D2207  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
003D220B  49 C1 F8 04                     sar r8, 4
003D220F  4C 8D 1C C8                     lea r11, [rax + rcx*8]
003D2213  48 8B 44 C8 F8                  mov rax, qword ptr [rax + rcx*8 - 8]
003D2218  48 8B C8                        mov rcx, rax
003D221B  48 33 CF                        xor rcx, rdi
003D221E  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
003D2225  48 33 C8                        xor rcx, rax
003D2228  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
003D2232  49 89 4B F8                     mov qword ptr [r11 - 8], rcx
003D2236  48 63 0D 83 B9 A5 00            movsxd rcx, dword ptr [rip + 0xa5b983]
003D223D  8B 15 81 B9 A5 00               mov edx, dword ptr [rip + 0xa5b981]
003D2243  4C 0F AF C0                     imul r8, rax
003D2247  3B CA                           cmp ecx, edx
003D2249  77 1D                           ja 0x1403d2268
003D224B  48 8B C1                        mov rax, rcx
003D224E  48 C1 E0 04                     shl rax, 4
003D2252  48 03 05 C7 B9 A5 00            add rax, qword ptr [rip + 0xa5b9c7]
003D2259  4C 3B 00                        cmp r8, qword ptr [rax]
003D225C  72 0A                           jb 0x1403d2268
003D225E  3B CA                           cmp ecx, edx
003D2260  74 43                           je 0x1403d22a5
003D2262  4C 3B 40 10                     cmp r8, qword ptr [rax + 0x10]
003D2266  72 3D                           jb 0x1403d22a5
003D2268  33 DB                           xor ebx, ebx
003D226A  44 8B D3                        mov r10d, ebx
003D226D  41 3B D2                        cmp edx, r10d
003D2270  0F 8C B0 00 00 00               jl 0x1403d2326
003D2276  41 8D 0C 12                     lea ecx, [r10 + rdx]
003D227A  D1 F9                           sar ecx, 1
003D227C  48 63 C1                        movsxd rax, ecx
003D227F  48 C1 E0 04                     shl rax, 4
003D2283  48 03 05 96 B9 A5 00            add rax, qword ptr [rip + 0xa5b996]
003D228A  4C 3B 00                        cmp r8, qword ptr [rax]
003D228D  0F 82 FB 02 00 00               jb 0x1403d258e
003D2293  3B 0D 2B B9 A5 00               cmp ecx, dword ptr [rip + 0xa5b92b]
003D2299  0F 85 CA 01 00 00               jne 0x1403d2469
003D229F  89 0D 1B B9 A5 00               mov dword ptr [rip + 0xa5b91b], ecx
003D22A5  8B 48 08                        mov ecx, dword ptr [rax + 8]
003D22A8  48 C1 E1 09                     shl rcx, 9
003D22AC  48 8B C1                        mov rax, rcx
003D22AF  49 33 43 F8                     xor rax, qword ptr [r11 - 8]
003D22B3  48 25 FF F1 FF FF               and rax, 0xfffffffffffff1ff
003D22B9  48 33 C1                        xor rax, rcx
003D22BC  49 89 43 F8                     mov qword ptr [r11 - 8], rax
003D22C0  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
003D22C4  48 C1 E9 37                     shr rcx, 0x37
003D22C8  48 8B C1                        mov rax, rcx
003D22CB  49 33 43 F8                     xor rax, qword ptr [r11 - 8]
003D22CF  48 0F BA F0 08                  btr rax, 8
003D22D4  48 33 C1                        xor rax, rcx
003D22D7  49 89 43 F8                     mov qword ptr [r11 - 8], rax
003D22DB  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
003D22DF  48 85 C0                        test rax, rax
003D22E2  78 59                           js 0x1403d233d
003D22E4  49 8B 53 F8                     mov rdx, qword ptr [r11 - 8]
003D22E8  48 81 E2 1F FF FF FF            and rdx, 0xffffffffffffff1f
003D22EF  49 89 53 F8                     mov qword ptr [r11 - 8], rdx
003D22F3  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
003D22F7  48 C1 E8 05                     shr rax, 5
003D22FB  8B C8                           mov ecx, eax
003D22FD  8B C0                           mov eax, eax
003D22FF  48 33 C2                        xor rax, rdx
003D2302  48 83 E0 E0                     and rax, 0xffffffffffffffe0
003D2306  48 33 C1                        xor rax, rcx
003D2309  49 89 43 F8                     mov qword ptr [r11 - 8], rax
003D230D  33 C0                           xor eax, eax
003D230F  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
003D2314  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
003D2319  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
003D231E  48 83 C4 30                     add rsp, 0x30
003D2322  41 5E                           pop r14
003D2324  C3                              ret
003D2325  CC                              int3
003D2326  45 33 C9                        xor r9d, r9d
003D2329  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
003D232E  BA 80 51 00 00                  mov edx, 0x5180
003D2333  41 8D 49 1A                     lea ecx, [r9 + 0x1a]
003D2337  E8 24 B3 12 00                  call 0x1404fd660
003D233C  CC                              int3
003D233D  41 8B 01                        mov eax, dword ptr [r9]
003D2340  A8 02                           test al, 2
003D2342  0F 84 66 02 00 00               je 0x1403d25ae
003D2348  49 8B 4B F8                     mov rcx, qword ptr [r11 - 8]
003D234C  48 81 C9 E0 00 00 00            or rcx, 0xe0
003D2353  48 81 E1 FF F1 FF FF            and rcx, 0xfffffffffffff1ff
003D235A  48 C1 EF 09                     shr rdi, 9
003D235E  49 BA F8 FF FF FF 7F 00 00 00   movabs r10, 0x7ffffffff8
003D2368  4C 23 D7                        and r10, rdi
003D236B  49 89 4B F8                     mov qword ptr [r11 - 8], rcx
003D236F  49 8B C6                        mov rax, r14
003D2372  4C 03 D0                        add r10, rax
003D2375  48 BA 00 D0 BE 7D FB F6 FF FF   movabs rdx, 0xfffff6fb7dbed000
003D237F  49 8B 02                        mov rax, qword ptr [r10]
003D2382  48 8B CA                        mov rcx, rdx
003D2385  49 B8 F8 D7 BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbed7f8
003D238F  4C 3B D1                        cmp r10, rcx
003D2392  72 27                           jb 0x1403d23bb
003D2394  49 8B C8                        mov rcx, r8
003D2397  4C 3B D1                        cmp r10, rcx
003D239A  77 1F                           ja 0x1403d23bb
003D239C  A8 01                           test al, 1
003D239E  74 12                           je 0x1403d23b2
003D23A0  A8 42                           test al, 0x42
003D23A2  0F 95 C2                        setne dl
003D23A5  A8 20                           test al, 0x20
003D23A7  0F 95 C1                        setne cl
003D23AA  84 D1                           test cl, dl
003D23AC  0F 84 CA 00 00 00               je 0x1403d247c
003D23B2  49 8B 0A                        mov rcx, qword ptr [r10]
003D23B5  48 C1 E8 3C                     shr rax, 0x3c
003D23B9  EB 17                           jmp 0x1403d23d2
003D23BB  49 8B 0A                        mov rcx, qword ptr [r10]
003D23BE  48 C1 E8 3C                     shr rax, 0x3c
003D23C2  48 8B D2                        mov rdx, rdx
003D23C5  4C 3B D2                        cmp r10, rdx
003D23C8  72 27                           jb 0x1403d23f1
003D23CA  49 8B D0                        mov rdx, r8
003D23CD  4C 3B D2                        cmp r10, rdx
003D23D0  77 1F                           ja 0x1403d23f1
003D23D2  48 8B D1                        mov rdx, rcx
003D23D5  F6 C1 01                        test cl, 1
003D23D8  74 17                           je 0x1403d23f1
003D23DA  F6 C1 42                        test cl, 0x42
003D23DD  41 0F 95 C1                     setne r9b
003D23E1  F6 C1 20                        test cl, 0x20
003D23E4  41 0F 95 C0                     setne r8b
003D23E8  45 84 C8                        test r8b, r9b
003D23EB  0F 84 F9 00 00 00               je 0x1403d24ea
003D23F1  83 E0 07                        and eax, 7
003D23F4  0F 85 7D 01 00 00               jne 0x1403d2577
003D23FA  85 C0                           test eax, eax
003D23FC  75 60                           jne 0x1403d245e
003D23FE  44 8B 46 10                     mov r8d, dword ptr [rsi + 0x10]
003D2402  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
003D2406  49 C1 E8 05                     shr r8, 5
003D240A  41 83 E0 1F                     and r8d, 0x1f
003D240E  48 0F BA E0 28                  bt rax, 0x28
003D2413  72 0D                           jb 0x1403d2422
003D2415  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
003D2419  48 85 C0                        test rax, rax
003D241C  0F 89 C2 01 00 00               jns 0x1403d25e4
003D2422  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003D242B  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
003D2432  48 83 B9 80 02 00 00 00         cmp qword ptr [rcx + 0x280], 0
003D243A  74 1F                           je 0x1403d245b
003D243C  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
003D2440  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
003D244A  48 0B D0                        or rdx, rax
003D244D  E8 62 02 00 00                  call 0x1403d26b4
003D2452  48 85 C0                        test rax, rax
003D2455  0F 85 C9 01 00 00               jne 0x1403d2624
003D245B  41 8B C0                        mov eax, r8d
003D245E  8B C8                           mov ecx, eax
003D2460  49 33 43 F8                     xor rax, qword ptr [r11 - 8]
003D2464  E9 99 FE FF FF                  jmp 0x1403d2302
003D2469  4C 3B 40 10                     cmp r8, qword ptr [rax + 0x10]
003D246D  0F 82 2C FE FF FF               jb 0x1403d229f
003D2473  44 8D 51 01                     lea r10d, [rcx + 1]
003D2477  E9 F1 FD FF FF                  jmp 0x1403d226d
003D247C  48 F7 05 01 46 BF 00 00 00 60 00  test qword ptr [rip + 0xbf4601], 0x600000
003D2487  0F 84 25 FF FF FF               je 0x1403d23b2
003D248D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
003D2496  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
003D249D  80 BA 60 01 00 00 01            cmp byte ptr [rdx + 0x160], 1
003D24A4  0F 84 08 FF FF FF               je 0x1403d23b2
003D24AA  4C 8B 82 08 05 00 00            mov r8, qword ptr [rdx + 0x508]
003D24B1  4D 85 C0                        test r8, r8
003D24B4  0F 84 F8 FE FF FF               je 0x1403d23b2
003D24BA  49 8B CA                        mov rcx, r10
003D24BD  48 C1 E9 03                     shr rcx, 3
003D24C1  81 E1 FF 01 00 00               and ecx, 0x1ff
003D24C7  49 8B 0C C8                     mov rcx, qword ptr [r8 + rcx*8]
003D24CB  F6 C1 20                        test cl, 0x20
003D24CE  74 04                           je 0x1403d24d4
003D24D0  48 83 C8 20                     or rax, 0x20
003D24D4  48 8B D0                        mov rdx, rax
003D24D7  48 83 CA 42                     or rdx, 0x42
003D24DB  F6 C1 42                        test cl, 0x42
003D24DE  48 0F 44 D0                     cmove rdx, rax
003D24E2  48 8B C2                        mov rax, rdx
003D24E5  E9 C8 FE FF FF                  jmp 0x1403d23b2
003D24EA  48 F7 05 93 45 BF 00 00 00 60 00  test qword ptr [rip + 0xbf4593], 0x600000
003D24F5  0F 84 F6 FE FF FF               je 0x1403d23f1
003D24FB  65 4C 8B 04 25 88 01 00 00      mov r8, qword ptr gs:[0x188]
003D2504  4D 8B 88 B8 00 00 00            mov r9, qword ptr [r8 + 0xb8]
003D250B  41 80 B9 60 01 00 00 01         cmp byte ptr [r9 + 0x160], 1
003D2513  0F 84 D8 FE FF FF               je 0x1403d23f1
003D2519  4D 8B 81 08 05 00 00            mov r8, qword ptr [r9 + 0x508]
003D2520  4D 85 C0                        test r8, r8
003D2523  0F 84 C8 FE FF FF               je 0x1403d23f1
003D2529  49 C1 EA 03                     shr r10, 3
003D252D  41 81 E2 FF 01 00 00            and r10d, 0x1ff
003D2534  4F 8B 04 D0                     mov r8, qword ptr [r8 + r10*8]
003D2538  41 F6 C0 20                     test r8b, 0x20
003D253C  74 04                           je 0x1403d2542
003D253E  48 83 CA 20                     or rdx, 0x20
003D2542  48 8B CA                        mov rcx, rdx
003D2545  48 83 C9 42                     or rcx, 0x42
003D2549  41 F6 C0 42                     test r8b, 0x42
003D254D  48 0F 44 CA                     cmove rcx, rdx
003D2551  E9 9B FE FF FF                  jmp 0x1403d23f1
003D2556  48 8B 0D 43 CE A5 00            mov rcx, qword ptr [rip + 0xa5ce43]
003D255D  48 85 C9                        test rcx, rcx
003D2560  0F 84 19 01 00 00               je 0x1403d267f
003D2566  48 03 C1                        add rax, rcx
003D2569  48 3B F8                        cmp rdi, rax
003D256C  0F 82 9B FD FF FF               jb 0x1403d230d
003D2572  E9 34 FC FF FF                  jmp 0x1403d21ab
003D2577  0F B6 D1                        movzx edx, cl
003D257A  80 E2 18                        and dl, 0x18
003D257D  80 FA 08                        cmp dl, 8
003D2580  0F 85 84 00 00 00               jne 0x1403d260a
003D2586  83 C8 18                        or eax, 0x18
003D2589  E9 6C FE FF FF                  jmp 0x1403d23fa
003D258E  85 C9                           test ecx, ecx
003D2590  0F 85 10 01 00 00               jne 0x1403d26a6
003D2596  4C 8B C8                        mov r9, rax
003D2599  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
003D259E  BA 80 51 00 00                  mov edx, 0x5180
003D25A3  B9 1A 00 00 00                  mov ecx, 0x1a
003D25A8  E8 B3 B0 12 00                  call 0x1404fd660
003D25AD  CC                              int3
003D25AE  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
003D25B2  48 B9 FF FF FF FF FF FF FF 3F   movabs rcx, 0x3fffffffffffffff
003D25BC  48 23 C1                        and rax, rcx
003D25BF  48 83 F8 07                     cmp rax, 7
003D25C3  72 56                           jb 0x1403d261b
003D25C5  B8 07 00 00 00                  mov eax, 7
003D25CA  48 C1 E0 05                     shl rax, 5
003D25CE  48 8B C8                        mov rcx, rax
003D25D1  49 33 4B F8                     xor rcx, qword ptr [r11 - 8]
003D25D5  48 81 E1 1F FF FF FF            and rcx, 0xffffffffffffff1f
003D25DC  48 33 C8                        xor rcx, rax
003D25DF  E9 76 FD FF FF                  jmp 0x1403d235a
003D25E4  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
003D25E8  48 85 C0                        test rax, rax
003D25EB  0F 84 31 FE FF FF               je 0x1403d2422
003D25F1  41 8B C0                        mov eax, r8d
003D25F4  4C 8D 05 75 EA C3 FF            lea r8, [rip - 0x3c158b]
003D25FB  41 8B 04 80                     mov eax, dword ptr [r8 + rax*4]
003D25FF  8B C8                           mov ecx, eax
003D2601  49 33 43 F8                     xor rax, qword ptr [r11 - 8]
003D2605  E9 F8 FC FF FF                  jmp 0x1403d2302
003D260A  F6 C1 10                        test cl, 0x10
003D260D  0F 84 4B FE FF FF               je 0x1403d245e
003D2613  83 C8 08                        or eax, 8
003D2616  E9 DF FD FF FF                  jmp 0x1403d23fa
003D261B  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
003D261F  48 23 C1                        and rax, rcx
003D2622  EB A6                           jmp 0x1403d25ca
003D2624  41 8B C0                        mov eax, r8d
003D2627  4C 8D 05 42 EA C3 FF            lea r8, [rip - 0x3c15be]
003D262E  45 8B 04 80                     mov r8d, dword ptr [r8 + rax*4]
003D2632  E9 24 FE FF FF                  jmp 0x1403d245b
003D2637  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
003D263B  48 85 C0                        test rax, rax
003D263E  0F 89 C9 FC FF FF               jns 0x1403d230d
003D2644  49 8B 49 10                     mov rcx, qword ptr [r9 + 0x10]
003D2648  48 FF C1                        inc rcx
003D264B  49 89 49 10                     mov qword ptr [r9 + 0x10], rcx
003D264F  49 3B 49 18                     cmp rcx, qword ptr [r9 + 0x18]
003D2653  72 0A                           jb 0x1403d265f
003D2655  B8 05 00 00 00                  mov eax, 5
003D265A  E9 B0 FC FF FF                  jmp 0x1403d230f
003D265F  49 8B 59 08                     mov rbx, qword ptr [r9 + 8]
003D2663  48 C1 E1 05                     shl rcx, 5
003D2667  48 03 D9                        add rbx, rcx
003D266A  48 8B CE                        mov rcx, rsi
003D266D  48 8D 53 E0                     lea rdx, [rbx - 0x20]
003D2671  E8 7A A2 F4 FF                  call 0x14031c8f0
003D2676  48 89 7B F8                     mov qword ptr [rbx - 8], rdi
003D267A  E9 8E FC FF FF                  jmp 0x1403d230d
003D267F  B9 00 40 80 10                  mov ecx, 0x10804000
003D2684  48 C7 05 21 CD A5 00 00 00 00 10  mov qword ptr [rip + 0xa5cd21], 0x10000000
003D268F  48 89 0D 0A CD A5 00            mov qword ptr [rip + 0xa5cd0a], rcx
003D2696  48 C7 05 07 CD A5 00 00 00 80 10  mov qword ptr [rip + 0xa5cd07], 0x10800000
003D26A1  E9 C0 FE FF FF                  jmp 0x1403d2566
003D26A6  8D 51 FF                        lea edx, [rcx - 1]
003D26A9  E9 BF FB FF FF                  jmp 0x1403d226d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiQueryLeafPte(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (48);
    v_rdi = (a2) << (25);
    result = (v_r14) << (25);
    v_rdi = (v_rdi) - (result);
    v_rdi = (v_rdi) >> (16);
    if (v_rdi >= (*(unsigned __int64 *)(v_rip + 10867178))) goto loc_003D2556;
loc_003D21AB:
    if (a3 >= 1) goto loc_003D230D;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (1)) == 0) goto loc_003D230D;
    result = (*(unsigned __int64 *)(a2)) >> (12);
    result = (result) & (a1);
    a3 = (result + result * 2) << (4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 184))))) & (1)) == 0) goto loc_003D2637;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 16)) + 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 16) = a1;
    if (a1 >= (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 24))) goto loc_003D2655;
    a3 = (a3) >> (4);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 8) + a1 * 8 - 8)) ^ (v_rdi);
    a1 = (a1) & (0xFFFFFFFFFFFFF000ULL);
    a1 = (a1) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 8) + a1 * 8 - 8));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 8) + a1 * 8 - 8) = a1;
    a3 = (a3) * (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 8) + a1 * 8 - 8));
    if (((unsigned int)((int)(*(unsigned int *)(v_rip + 10860931)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10860929))))) goto loc_003D2268;
    result = ((int)(*(unsigned int *)(v_rip + 10860931))) << (4);
    result = (result) + (*(unsigned __int64 *)(v_rip + 10860999));
    if (a3 < (*(unsigned __int64 *)(result))) goto loc_003D2268;
    if (((unsigned int)((int)(*(unsigned int *)(v_rip + 10860931)))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10860929))))) goto loc_003D22A5;
    if (a3 < (*(unsigned __int64 *)(result + 16))) goto loc_003D22A5;
loc_003D2268:
    v_rbx = 0;
loc_003D226D:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10860929)))) < 0) goto loc_003D2326;
    a1 = (unsigned int)((0 + (unsigned int)(*(unsigned int *)(v_rip + 10860929)) * 1) >> (1));
    result = ((int)((unsigned int)(a1))) << (4);
    result = (result) + (*(unsigned __int64 *)(v_rip + 10860950));
    if (a3 < (*(unsigned __int64 *)(result))) goto loc_003D258E;
    if (((unsigned int)(a1)) != (*(unsigned int *)(v_rip + 10860843))) goto loc_003D2469;
loc_003D229F:
    *(unsigned int *)(v_rip + 10860827) = (unsigned int)(a1);
loc_003D22A5:
    a1 = ((unsigned int)(*(unsigned int *)(result + 8))) << (9);
    result = (a1) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 8) + a1 * 8 - 8));
    result = (result) & (0xFFFFFFFFFFFFF1FFULL);
    result = (result) ^ (a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 8) + a1 * 8 - 8) = result;
    a1 = (*(unsigned __int64 *)(a3 + result * 1 + 40)) >> (55);
    result = (a1) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 8) + a1 * 8 - 8));
    result = (result) ^ (a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 8) + a1 * 8 - 8) = result;
    if (sign_flag) goto loc_003D233D;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 8) + a1 * 8 - 8)) & (-225);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 8) + a1 * 8 - 8) = a2;
    result = (*(unsigned __int64 *)(a3 + result * 1 + 16)) >> (5);
    result = ((unsigned int)((unsigned int)(result))) ^ (a2);
loc_003D2302:
    result = (result) & (-32);
    result = (result) ^ ((unsigned int)((unsigned int)(result)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 8) + a1 * 8 - 8) = result;
loc_003D230D:
    result = 0;
loc_003D230F:
    v_rsp = (v_rsp) + (48);
    return result;
loc_003D2326:
    a4 = 0;
    v_stack_p20 = v_stack_p10;
    result = KeBugCheckEx(a4 + 26, (unsigned int)(0x5180ULL), a3, a4);
loc_003D233D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a4)))) & (2)) == 0) goto loc_003D25AE;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 8) + a1 * 8 - 8)) | (224);
    a1 = (a1) & (0xFFFFFFFFFFFFF1FFULL);
loc_003D235A:
    v_rdi = (v_stack_p20) >> (9);
    v_r10 = (0) & (v_rdi);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 8) + a1 * 8 - 8) = a1;
    v_r10 = (v_r10) + (v_r14);
    if (v_r10 < ((unsigned int)(0x5180ULL))) goto loc_003D23BB;
    if (v_r10 > a3) goto loc_003D23BB;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r10))) & (1)) == 0) goto loc_003D23B2;
    a2 = ((((unsigned __int8)(*(unsigned __int64 *)(v_r10))) & (66)) != 0) ? 1 : 0;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(v_r10))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a1)) & ((unsigned __int8)(a2))) == 0) goto loc_003D247C;
loc_003D23B2:
    result = (*(unsigned __int64 *)(v_r10)) >> (60);
    goto loc_003D23D2;
loc_003D23BB:
    result = (result) >> (60);
    if (v_r10 < a2) goto loc_003D23F1;
    if (v_r10 > a3) goto loc_003D23F1;
loc_003D23D2:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r10))) & (1)) == 0) goto loc_003D23F1;
    a4 = ((((unsigned __int8)(*(unsigned __int64 *)(v_r10))) & (66)) != 0) ? 1 : 0;
    a3 = ((((unsigned __int8)(*(unsigned __int64 *)(v_r10))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(a3)) & ((unsigned __int8)(a4))) == 0) goto loc_003D24EA;
loc_003D23F1:
    result = (unsigned int)((result) & (7));
    if (condition_is_not_equal) goto loc_003D2577;
loc_003D23FA:
    if ((unsigned int)(result) != 0) goto loc_003D245E;
    a3 = ((unsigned int)(*(unsigned int *)(v_stack_p18 + 16))) >> (5);
    a3 = (unsigned int)((a3) & (31));
    if (condition_is_below) goto loc_003D2422;
    if (!sign_flag) goto loc_003D25E4;
loc_003D2422:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 640)) == 0) goto loc_003D245B;
    a2 = (*(unsigned __int64 *)(v_stack_p18 + 8)) | (*(unsigned __int64 *)(gs_base + (0 + 392)));
    result = MiLocateCloneAddress(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a2, a3, a4);
    if (result != 0) goto loc_003D2624;
loc_003D245B:
loc_003D245E:
    result = ((unsigned int)(a3)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 8) + a1 * 8 - 8));
    goto loc_003D2302;
loc_003D2469:
    if (a3 < (*(unsigned __int64 *)(result + 16))) goto loc_003D229F;
    goto loc_003D226D;
loc_003D247C:
    if (((*(unsigned __int64 *)(v_rip + 12535297)) & (0x600000ULL)) == 0) goto loc_003D23B2;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_003D23B2;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_003D23B2;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(a3))) + 1) >> (3);
    a1 = (unsigned int)((a1) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    a2 = (result) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (66)) == 0) { a2 = result; }
    goto loc_003D23B2;
loc_003D24EA:
    if (((*(unsigned __int64 *)(v_rip + 12535187)) & (0x600000ULL)) == 0) goto loc_003D23F1;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_003D23F1;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_003D23F1;
    v_r10 = ((unsigned int)((unsigned int)((unsigned int)(a3))) + 1) >> (3);
    v_r10 = (unsigned int)((v_r10) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + v_r10 * 8))) & (32)) != 0) {
        a2 = (a2) | (32);
    }
    a1 = (a2) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + v_r10 * 8))) & (66)) == 0) { a1 = a2; }
    goto loc_003D23F1;
loc_003D2556:
    if (*(unsigned __int64 *)(v_rip + 10866243) == 0) goto loc_003D267F;
loc_003D2566:
    result = (a2) + (*(unsigned __int64 *)(v_rip + 10866243));
    if (v_rdi < result) goto loc_003D230D;
    goto loc_003D21AB;
loc_003D2577:
    a2 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10866243))) & (24));
    if (((unsigned __int8)(a2)) != 8) goto loc_003D260A;
    result = (unsigned int)((result) | (24));
    goto loc_003D23FA;
loc_003D258E:
    if ((unsigned int)(*(unsigned __int64 *)(v_rip + 10866243)) != 0) goto loc_003D26A6;
    v_stack_p20 = v_stack_p10;
    result = KeBugCheckEx(26, (unsigned int)(0x5180ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + v_r10 * 8), result);
loc_003D25AE:
    result = (*(unsigned __int64 *)(v_stack_p18 + 24)) & (26);
    if (result < 7) goto loc_003D261B;
loc_003D25CA:
    result = (7) << (5);
    a1 = (result) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 8) + a1 * 8 - 8));
    a1 = (a1) & (-225);
    a1 = (a1) ^ (result);
    goto loc_003D235A;
loc_003D25E4:
    if (*(unsigned __int64 *)(v_stack_p18 + 8) == 0) goto loc_003D2422;
    result = ((unsigned int)(*(unsigned int *)(v_rip - 3937675 + (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + v_r10 * 8))) * 4))) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 8) + a1 * 8 - 8));
    goto loc_003D2302;
loc_003D260A:
    if ((((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 3937675 + (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + v_r10 * 8))) * 4)))))) & (16)) == 0) goto loc_003D245E;
    result = (unsigned int)((result) | (8));
    goto loc_003D23FA;
loc_003D261B:
    result = (*(unsigned __int64 *)(v_stack_p18 + 24)) & ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 3937675 + (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + v_r10 * 8))) * 4)))));
    goto loc_003D25CA;
loc_003D2624:
    goto loc_003D245B;
loc_003D2637:
    if (!sign_flag) goto loc_003D230D;
    a1 = (*(unsigned __int64 *)(result + 16)) + 1;
    *(unsigned __int64 *)(result + 16) = a1;
    if (a1 < (*(unsigned __int64 *)(result + 24))) goto loc_003D265F;
loc_003D2655:
    goto loc_003D230F;
loc_003D265F:
    a1 = (a1) << (5);
    v_rbx = (*(unsigned __int64 *)(result + 8)) + (a1);
    result = MiIdentifyPfnWrapper(v_stack_p18, v_rbx - 32, (unsigned int)(*(unsigned int *)(v_rip - 3937726 + (unsigned int)((unsigned int)(v_rip - 3937675)) * 4)), result);
    *(unsigned __int64 *)(v_rbx - 8) = v_rdi;
    goto loc_003D230D;
loc_003D267F:
    *(unsigned __int64 *)(v_rip + 10865953) = 0x10000000ULL;
    *(unsigned __int64 *)(v_rip + 10865930) = (unsigned int)(0x10804000ULL);
    *(unsigned __int64 *)(v_rip + 10865927) = 0x10800000ULL;
    goto loc_003D2566;
loc_003D26A6:
    goto loc_003D226D;
}
```

## 5. (Beta) C Style

```c
int64_t MiQueryLeafPte(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (48);
    local_rdi = (Arg2) << (25);
    result = (local_r14) << (25);
    local_rdi = (local_rdi) - (result);
    local_rdi = (local_rdi) >> (16);
    if (local_rdi >= (*(uint64_t *)(v_rip + 0xA5D1EA))) goto loc_003D2556;
loc_003D21AB:
    if (Arg3 >= 1) goto loc_003D230D;
    if ((((uint8_t)(*(uint64_t *)(arg2))) & (1)) == 0) goto loc_003D230D;
    result = (*(uint64_t *)(arg2)) >> (12);
    result = (result) & (Arg1);
    Arg3 = (result + result * 2) << (4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xB8))))) & (1)) == 0) goto loc_003D2637;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x10)) + 1;
    *(void **)(*(uint64_t *)(arg1 + 0xB8) + 0x10) = Arg1;
    if (Arg1 >= (*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x18))) goto loc_003D2655;
    Arg3 = (Arg3) >> (4);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8) + arg1 * 8 - 0x8)) ^ (local_rdi);
    Arg1 = (Arg1) & (0xFFFFFFFFFFFFF000ULL);
    Arg1 = (Arg1) ^ (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8) + arg1 * 8 - 0x8));
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8) + arg1 * 8 - 0x8) = Arg1;
    Arg3 = (Arg3) * (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8) + arg1 * 8 - 0x8));
    if (((uint32_t)((int32_t)(*(uint32_t *)(v_rip + 0xA5B983)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA5B981))))) goto loc_003D2268;
    result = ((int32_t)(*(uint32_t *)(v_rip + 0xA5B983))) << (4);
    result = (result) + (*(uint64_t *)(v_rip + 0xA5B9C7));
    if (Arg3 < (*(uint64_t *)(result))) goto loc_003D2268;
    if (((uint32_t)((int32_t)(*(uint32_t *)(v_rip + 0xA5B983)))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA5B981))))) goto loc_003D22A5;
    if (Arg3 < (*(uint64_t *)(result + 0x10))) goto loc_003D22A5;
loc_003D2268:
    local_rbx = 0;
loc_003D226D:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA5B981)))) < 0) goto loc_003D2326;
    Arg1 = (uint32_t)((0 + (uint32_t)(*(uint32_t *)(v_rip + 0xA5B981)) * 1) >> (1));
    result = ((int32_t)((uint32_t)(Arg1))) << (4);
    result = (result) + (*(uint64_t *)(v_rip + 0xA5B996));
    if (Arg3 < (*(uint64_t *)(result))) goto loc_003D258E;
    if (((uint32_t)(Arg1)) != (*(uint32_t *)(v_rip + 0xA5B92B))) goto loc_003D2469;
loc_003D229F:
    *(uint32_t *)(v_rip + 0xA5B91B) = (uint32_t)(Arg1);
loc_003D22A5:
    Arg1 = ((uint32_t)(*(uint32_t *)(result + 0x8))) << (9);
    result = (Arg1) ^ (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8) + arg1 * 8 - 0x8));
    result = (result) & (0xFFFFFFFFFFFFF1FFULL);
    result = (result) ^ (Arg1);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8) + arg1 * 8 - 0x8) = result;
    Arg1 = (*(uint64_t *)(Arg3 + result * 1 + 0x28)) >> (55);
    result = (Arg1) ^ (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8) + arg1 * 8 - 0x8));
    result = (result) ^ (Arg1);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8) + arg1 * 8 - 0x8) = result;
    if (sign_flag) goto loc_003D233D;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8) + arg1 * 8 - 0x8)) & (-225);
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8) + arg1 * 8 - 0x8) = Arg2;
    result = (*(uint64_t *)(Arg3 + result * 1 + 0x10)) >> (5);
    result = ((uint32_t)((uint32_t)(result))) ^ (Arg2);
loc_003D2302:
    result = (result) & (-32);
    result = (result) ^ ((uint32_t)((uint32_t)(result)));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8) + arg1 * 8 - 0x8) = result;
loc_003D230D:
    result = 0;
loc_003D230F:
    local_rsp = (local_rsp) + (48);
    return result;
loc_003D2326:
    a4 = 0;
    v_stack_p20 = v_stack_p10;
    result = KeBugCheckEx(a4 + 26, (uint32_t)(0x5180ULL), Arg3, a4);
loc_003D233D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(a4)))) & (2)) == 0) goto loc_003D25AE;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8) + arg1 * 8 - 0x8)) | (224);
    Arg1 = (Arg1) & (0xFFFFFFFFFFFFF1FFULL);
loc_003D235A:
    local_rdi = (v_stack_p20) >> (9);
    local_r10 = (0) & (local_rdi);
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8) + arg1 * 8 - 0x8) = Arg1;
    local_r10 = (local_r10) + (local_r14);
    if (local_r10 < ((uint32_t)(0x5180ULL))) goto loc_003D23BB;
    if (local_r10 > Arg3) goto loc_003D23BB;
    if ((((uint8_t)(*(uint64_t *)(local_r10))) & (1)) == 0) goto loc_003D23B2;
    Arg2 = ((((uint8_t)(*(uint64_t *)(local_r10))) & (66)) != 0) ? 1 : 0;
    Arg1 = ((((uint8_t)(*(uint64_t *)(local_r10))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(Arg1)) & ((uint8_t)(Arg2))) == 0) goto loc_003D247C;
loc_003D23B2:
    result = (*(uint64_t *)(local_r10)) >> (60);
    goto loc_003D23D2;
loc_003D23BB:
    result = (result) >> (60);
    if (local_r10 < Arg2) goto loc_003D23F1;
    if (local_r10 > Arg3) goto loc_003D23F1;
loc_003D23D2:
    if ((((uint8_t)(*(uint64_t *)(local_r10))) & (1)) == 0) goto loc_003D23F1;
    a4 = ((((uint8_t)(*(uint64_t *)(local_r10))) & (66)) != 0) ? 1 : 0;
    Arg3 = ((((uint8_t)(*(uint64_t *)(local_r10))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(Arg3)) & ((uint8_t)(a4))) == 0) goto loc_003D24EA;
loc_003D23F1:
    result = (uint32_t)((result) & (7));
    if (condition_is_not_equal) goto loc_003D2577;
loc_003D23FA:
    if ((uint32_t)(result) != 0) goto loc_003D245E;
    Arg3 = ((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x10))) >> (5);
    Arg3 = (uint32_t)((Arg3) & (31));
    if (condition_is_below) goto loc_003D2422;
    if (!sign_flag) goto loc_003D25E4;
loc_003D2422:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x280)) == 0) goto loc_003D245B;
    Arg2 = (*(uint64_t *)(v_stack_p18 + 0x8)) | (*(uint64_t *)(gs_base + (0 + 0x188)));
    result = MiLocateCloneAddress(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg2, Arg3, a4);
    if (result != 0) goto loc_003D2624;
loc_003D245B:
loc_003D245E:
    result = ((uint32_t)(Arg3)) ^ (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8) + arg1 * 8 - 0x8));
    goto loc_003D2302;
loc_003D2469:
    if (Arg3 < (*(uint64_t *)(result + 0x10))) goto loc_003D229F;
    goto loc_003D226D;
loc_003D247C:
    if (((*(uint64_t *)(v_rip + 0xBF4601)) & (0x600000ULL)) == 0) goto loc_003D23B2;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_003D23B2;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_003D23B2;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(Arg3))) + 1) >> (3);
    Arg1 = (uint32_t)((Arg1) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + arg1 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    Arg2 = (result) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + arg1 * 8))) & (66)) == 0) { Arg2 = result; }
    goto loc_003D23B2;
loc_003D24EA:
    if (((*(uint64_t *)(v_rip + 0xBF4593)) & (0x600000ULL)) == 0) goto loc_003D23F1;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_003D23F1;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_003D23F1;
    local_r10 = ((uint32_t)((uint32_t)((uint32_t)(Arg3))) + 1) >> (3);
    local_r10 = (uint32_t)((local_r10) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + local_r10 * 8))) & (32)) != 0) {
        Arg2 = (Arg2) | (32);
    }
    Arg1 = (Arg2) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + local_r10 * 8))) & (66)) == 0) { Arg1 = Arg2; }
    goto loc_003D23F1;
loc_003D2556:
    if (*(uint64_t *)(v_rip + 0xA5CE43) == 0) goto loc_003D267F;
loc_003D2566:
    result = (Arg2) + (*(uint64_t *)(v_rip + 0xA5CE43));
    if (local_rdi < result) goto loc_003D230D;
    goto loc_003D21AB;
loc_003D2577:
    Arg2 = (uint8_t)(((uint8_t)(*(uint64_t *)(v_rip + 0xA5CE43))) & (24));
    if (((uint8_t)(Arg2)) != 8) goto loc_003D260A;
    result = (uint32_t)((result) | (24));
    goto loc_003D23FA;
loc_003D258E:
    if ((uint32_t)(*(uint64_t *)(v_rip + 0xA5CE43)) != 0) goto loc_003D26A6;
    v_stack_p20 = v_stack_p10;
    result = KeBugCheckEx(26, (uint32_t)(0x5180ULL), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + local_r10 * 8), result);
loc_003D25AE:
    result = (*(uint64_t *)(v_stack_p18 + 0x18)) & (26);
    if (result < 7) goto loc_003D261B;
loc_003D25CA:
    result = (7) << (5);
    Arg1 = (result) ^ (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8) + arg1 * 8 - 0x8));
    Arg1 = (Arg1) & (-225);
    Arg1 = (Arg1) ^ (result);
    goto loc_003D235A;
loc_003D25E4:
    if (*(uint64_t *)(v_stack_p18 + 0x8) == 0) goto loc_003D2422;
    result = ((uint32_t)(*(uint32_t *)(v_rip - 0x3C158B + (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + local_r10 * 8))) * 4))) ^ (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x8) + arg1 * 8 - 0x8));
    goto loc_003D2302;
loc_003D260A:
    if ((((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x3C158B + (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + local_r10 * 8))) * 4)))))) & (16)) == 0) goto loc_003D245E;
    result = (uint32_t)((result) | (8));
    goto loc_003D23FA;
loc_003D261B:
    result = (*(uint64_t *)(v_stack_p18 + 0x18)) & ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x3C158B + (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + local_r10 * 8))) * 4)))));
    goto loc_003D25CA;
loc_003D2624:
    goto loc_003D245B;
loc_003D2637:
    if (!sign_flag) goto loc_003D230D;
    Arg1 = (*(uint64_t *)(result + 0x10)) + 1;
    *(void **)(result + 0x10) = Arg1;
    if (Arg1 < (*(uint64_t *)(result + 0x18))) goto loc_003D265F;
loc_003D2655:
    goto loc_003D230F;
loc_003D265F:
    Arg1 = (Arg1) << (5);
    local_rbx = (*(uint64_t *)(result + 0x8)) + (Arg1);
    result = MiIdentifyPfnWrapper(v_stack_p18, local_rbx - 32, (uint32_t)(*(uint32_t *)(v_rip - 0x3C15BE + (uint32_t)((uint32_t)(v_rip - 0x3C158B)) * 4)), result);
    *(uint64_t *)(local_rbx - 0x8) = local_rdi;
    goto loc_003D230D;
loc_003D267F:
    *(uint64_t *)(v_rip + 0xA5CD21) = 0x10000000ULL;
    *(uint64_t *)(v_rip + 0xA5CD0A) = (uint32_t)(0x10804000ULL);
    *(uint64_t *)(v_rip + 0xA5CD07) = 0x10800000ULL;
    goto loc_003D2566;
loc_003D26A6:
    goto loc_003D226D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003D2160&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
