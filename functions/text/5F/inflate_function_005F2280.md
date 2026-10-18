# inflate

- RVA: `0x005F2280`–`0x005F3314` (길이 `4,244` bytes)
- VA: `0x00000001405F2280`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D0438`
- 디코드: `1,114`개 명령, `4,244/4,244` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **18**

### Outgoing calls
- `0x005F229B` → [inflateStateCheck](inflateStateCheck_function_005F3478.md) (function, `0x005F3478`)
- `0x005F23EF` → [adler32_z](../60/adler32_z_function_00600344.md) (function, `0x00600344`)
- `0x005F25A2` → [adler32_z](../60/adler32_z_function_00600344.md) (function, `0x00600344`)
- `0x005F2681` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x005F2825` → [inflate_table](../60/inflate_table_function_00600664.md) (function, `0x00600664`)
- `0x005F2AD3` → [inflate_table](../60/inflate_table_function_00600664.md) (function, `0x00600664`)
- `0x005F2B3F` → [inflate_table](../60/inflate_table_function_00600664.md) (function, `0x00600664`)
- `0x005F2BC9` → [inflate_fast_chunk_](inflate_fast_chunk__function_005FFE4C.md) (function, `0x005FFE4C`)
- `0x005F309E` → [chunkset_core](chunkset_core_function_005F2120.md) (function, `0x005F2120`)
- `0x005F30B1` → [chunkcopy_core](chunkcopy_core_function_005F20DC.md) (function, `0x005F20DC`)
- `0x005F317C` → [adler32_z](../60/adler32_z_function_00600344.md) (function, `0x00600344`)
- `0x005F327C` → [updatewindow](updatewindow_function_005F34B8.md) (function, `0x005F34B8`)
- `0x005F32B9` → [adler32_z](../60/adler32_z_function_00600344.md) (function, `0x00600344`)

### Direct callers
- [RtlDecompressBufferDeflateInternal](RtlDecompressBufferDeflateInternal_function_005F0858.md) at `0x005F0900`

### Static image references
- `0x005F2487` → RVA `0x006CD410` (` ?? ::FNODOBFM::`string'`; read)
- `0x005F24A4` → RVA `0x00035B40` (`.rdata`; read)
- `0x005F24B6` → RVA `0x00035A90` (`.rdata`; read)
- `0x005F2545` → RVA `0x006CD4A0` (` ?? ::FNODOBFM::`string'`; read)
- `0x005F255F` → RVA `0x006CD4C0` (` ?? ::FNODOBFM::`string'`; read)
- `0x005F25E8` → RVA `0x006CD4E0` (` ?? ::FNODOBFM::`string'`; read)
- `0x005F2637` → RVA `0x006CD430` (` ?? ::FNODOBFM::`string'`; read)
- `0x005F276B` → RVA `0x00035B10` (`.rdata`; read)
- `0x005F2846` → RVA `0x006CD480` (` ?? ::FNODOBFM::`string'`; read)
- `0x005F2A4A` → RVA `0x006CD580` (` ?? ::FNODOBFM::`string'`; read)
- `0x005F2A83` → RVA `0x006CD5A0` (` ?? ::FNODOBFM::`string'`; read)
- `0x005F2AE8` → RVA `0x006CD5D0` (` ?? ::FNODOBFM::`string'`; read)
- `0x005F2B66` → RVA `0x006CD5F0` (` ?? ::FNODOBFM::`string'`; read)
- `0x005F2B72` → RVA `0x006CD450` (` ?? ::FNODOBFM::`string'`; read)
- `0x005F2DA6` → RVA `0x006CD500` (` ?? ::FNODOBFM::`string'`; read)
- `0x005F2F26` → RVA `0x006CD520` (` ?? ::FNODOBFM::`string'`; read)
- `0x005F2FCA` → RVA `0x006CD540` (` ?? ::FNODOBFM::`string'`; read)
- `0x005F31B9` → RVA `0x006CD560` (` ?? ::FNODOBFM::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005F2280  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005F2285  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
005F2289  55                              push rbp
005F228A  56                              push rsi
005F228B  57                              push rdi
005F228C  41 54                           push r12
005F228E  41 55                           push r13
005F2290  41 56                           push r14
005F2292  41 57                           push r15
005F2294  48 83 EC 50                     sub rsp, 0x50
005F2298  48 8B F1                        mov rsi, rcx
005F229B  E8 D8 11 00 00                  call 0x1405f3478
005F22A0  33 ED                           xor ebp, ebp
005F22A2  85 C0                           test eax, eax
005F22A4  0F 85 D7 00 00 00               jne 0x1405f2381
005F22AA  48 8D 41 10                     lea rax, [rcx + 0x10]
005F22AE  48 39 28                        cmp qword ptr [rax], rbp
005F22B1  0F 84 CA 00 00 00               je 0x1405f2381
005F22B7  48 39 29                        cmp qword ptr [rcx], rbp
005F22BA  75 0F                           jne 0x1405f22cb
005F22BC  39 69 08                        cmp dword ptr [rcx + 8], ebp
005F22BF  0F 85 BC 00 00 00               jne 0x1405f2381
005F22C5  48 83 C1 10                     add rcx, 0x10
005F22C9  EB 03                           jmp 0x1405f22ce
005F22CB  48 8B C8                        mov rcx, rax
005F22CE  48 8B 7E 28                     mov rdi, qword ptr [rsi + 0x28]
005F22D2  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
005F22D7  81 7F 08 3F 3F 00 00            cmp dword ptr [rdi + 8], 0x3f3f
005F22DE  75 0C                           jne 0x1405f22ec
005F22E0  C7 47 08 40 3F 00 00            mov dword ptr [rdi + 8], 0x3f40
005F22E7  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
005F22EC  4C 8B 08                        mov r9, qword ptr [rax]
005F22EF  B8 07 00 00 00                  mov eax, 7
005F22F4  44 8B 5E 18                     mov r11d, dword ptr [rsi + 0x18]
005F22F8  41 8B DB                        mov ebx, r11d
005F22FB  44 8B 66 08                     mov r12d, dword ptr [rsi + 8]
005F22FF  4C 8B 2E                        mov r13, qword ptr [rsi]
005F2302  44 8B 7F 48                     mov r15d, dword ptr [rdi + 0x48]
005F2306  8D 50 09                        lea edx, [rax + 9]
005F2309  44 8B 77 4C                     mov r14d, dword ptr [rdi + 0x4c]
005F230D  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
005F2312  44 89 9C 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r11d
005F231A  44 89 64 24 34                  mov dword ptr [rsp + 0x34], r12d
005F231F  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
005F2323  89 AC 24 98 00 00 00            mov dword ptr [rsp + 0x98], ebp
005F232A  4C 8D 47 74                     lea r8, [rdi + 0x74]
005F232E  4C 8D 57 70                     lea r10, [rdi + 0x70]
005F2332  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
005F2335  81 F9 47 3F 00 00               cmp ecx, 0x3f47
005F233B  0F 8F DD 08 00 00               jg 0x1405f2c1e
005F2341  0F 84 43 08 00 00               je 0x1405f2b8a
005F2347  81 F9 41 3F 00 00               cmp ecx, 0x3f41
005F234D  0F 8F 67 03 00 00               jg 0x1405f26ba
005F2353  0F 84 9B 02 00 00               je 0x1405f25f4
005F2359  81 E9 34 3F 00 00               sub ecx, 0x3f34
005F235F  0F 84 80 01 00 00               je 0x1405f24e5
005F2365  83 E9 09                        sub ecx, 9
005F2368  74 35                           je 0x1405f239f
005F236A  83 E9 01                        sub ecx, 1
005F236D  74 70                           je 0x1405f23df
005F236F  83 E9 01                        sub ecx, 1
005F2372  0F 84 A3 00 00 00               je 0x1405f241b
005F2378  83 F9 01                        cmp ecx, 1
005F237B  0F 84 9A 00 00 00               je 0x1405f241b
005F2381  B8 FE FF FF FF                  mov eax, 0xfffffffe
005F2386  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
005F238E  48 83 C4 50                     add rsp, 0x50
005F2392  41 5F                           pop r15
005F2394  41 5E                           pop r14
005F2396  41 5D                           pop r13
005F2398  41 5C                           pop r12
005F239A  5F                              pop rdi
005F239B  5E                              pop rsi
005F239C  5D                              pop rbp
005F239D  C3                              ret
005F239E  CC                              int3
005F239F  41 83 FE 20                     cmp r14d, 0x20
005F23A3  73 22                           jae 0x1405f23c7
005F23A5  45 85 E4                        test r12d, r12d
005F23A8  0F 84 80 0E 00 00               je 0x1405f322e
005F23AE  41 0F B6 45 00                  movzx eax, byte ptr [r13]
005F23B3  41 8B CE                        mov ecx, r14d
005F23B6  D3 E0                           shl eax, cl
005F23B8  41 FF CC                        dec r12d
005F23BB  44 03 F8                        add r15d, eax
005F23BE  49 FF C5                        inc r13
005F23C1  41 83 C6 08                     add r14d, 8
005F23C5  EB D8                           jmp 0x1405f239f
005F23C7  41 0F CF                        bswap r15d
005F23CA  44 89 7F 20                     mov dword ptr [rdi + 0x20], r15d
005F23CE  44 8B F5                        mov r14d, ebp
005F23D1  44 89 7E 4C                     mov dword ptr [rsi + 0x4c], r15d
005F23D5  44 8B FD                        mov r15d, ebp
005F23D8  C7 47 08 3E 3F 00 00            mov dword ptr [rdi + 8], 0x3f3e
005F23DF  39 6F 14                        cmp dword ptr [rdi + 0x14], ebp
005F23E2  0F 84 ED 0D 00 00               je 0x1405f31d5
005F23E8  45 33 C0                        xor r8d, r8d
005F23EB  33 D2                           xor edx, edx
005F23ED  33 C9                           xor ecx, ecx
005F23EF  E8 50 DF 00 00                  call 0x140600344
005F23F4  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
005F23F9  4C 8D 57 70                     lea r10, [rdi + 0x70]
005F23FD  44 8B 9C 24 A0 00 00 00         mov r11d, dword ptr [rsp + 0xa0]
005F2405  4C 8D 47 74                     lea r8, [rdi + 0x74]
005F2409  89 47 20                        mov dword ptr [rdi + 0x20], eax
005F240C  BA 10 00 00 00                  mov edx, 0x10
005F2411  89 46 4C                        mov dword ptr [rsi + 0x4c], eax
005F2414  C7 47 08 3F 3F 00 00            mov dword ptr [rdi + 8], 0x3f3f
005F241B  39 6F 0C                        cmp dword ptr [rdi + 0xc], ebp
005F241E  74 1C                           je 0x1405f243c
005F2420  41 8B CE                        mov ecx, r14d
005F2423  C7 47 08 4E 3F 00 00            mov dword ptr [rdi + 8], 0x3f4e
005F242A  B8 07 00 00 00                  mov eax, 7
005F242F  23 C8                           and ecx, eax
005F2431  41 D3 EF                        shr r15d, cl
005F2434  44 2B F1                        sub r14d, ecx
005F2437  E9 F6 FE FF FF                  jmp 0x1405f2332
005F243C  41 83 FE 03                     cmp r14d, 3
005F2440  73 22                           jae 0x1405f2464
005F2442  45 85 E4                        test r12d, r12d
005F2445  0F 84 E3 0D 00 00               je 0x1405f322e
005F244B  41 0F B6 45 00                  movzx eax, byte ptr [r13]
005F2450  41 8B CE                        mov ecx, r14d
005F2453  D3 E0                           shl eax, cl
005F2455  41 FF CC                        dec r12d
005F2458  44 03 F8                        add r15d, eax
005F245B  49 FF C5                        inc r13
005F245E  41 83 C6 08                     add r14d, 8
005F2462  EB D8                           jmp 0x1405f243c
005F2464  41 8B C7                        mov eax, r15d
005F2467  41 D1 EF                        shr r15d, 1
005F246A  83 E0 01                        and eax, 1
005F246D  89 47 0C                        mov dword ptr [rdi + 0xc], eax
005F2470  41 8B C7                        mov eax, r15d
005F2473  83 E0 03                        and eax, 3
005F2476  74 59                           je 0x1405f24d1
005F2478  83 E8 01                        sub eax, 1
005F247B  74 27                           je 0x1405f24a4
005F247D  83 E8 01                        sub eax, 1
005F2480  74 19                           je 0x1405f249b
005F2482  83 F8 01                        cmp eax, 1
005F2485  75 51                           jne 0x1405f24d8
005F2487  48 8D 05 82 AF 0D 00            lea rax, [rip + 0xdaf82]
005F248E  48 89 46 20                     mov qword ptr [rsi + 0x20], rax
005F2492  C7 47 08 51 3F 00 00            mov dword ptr [rdi + 8], 0x3f51
005F2499  EB 3D                           jmp 0x1405f24d8
005F249B  C7 47 08 44 3F 00 00            mov dword ptr [rdi + 8], 0x3f44
005F24A2  EB 34                           jmp 0x1405f24d8
005F24A4  48 8D 05 95 36 A4 FF            lea rax, [rip - 0x5bc96b]
005F24AB  41 C7 02 09 00 00 00            mov dword ptr [r10], 9
005F24B2  48 89 47 60                     mov qword ptr [rdi + 0x60], rax
005F24B6  48 8D 05 D3 35 A4 FF            lea rax, [rip - 0x5bca2d]
005F24BD  48 89 47 68                     mov qword ptr [rdi + 0x68], rax
005F24C1  41 C7 00 05 00 00 00            mov dword ptr [r8], 5
005F24C8  C7 47 08 47 3F 00 00            mov dword ptr [rdi + 8], 0x3f47
005F24CF  EB 07                           jmp 0x1405f24d8
005F24D1  C7 47 08 41 3F 00 00            mov dword ptr [rdi + 8], 0x3f41
005F24D8  41 C1 EF 02                     shr r15d, 2
005F24DC  41 83 C6 FD                     add r14d, -3
005F24E0  E9 E6 0C 00 00                  jmp 0x1405f31cb
005F24E5  39 6F 10                        cmp dword ptr [rdi + 0x10], ebp
005F24E8  75 0C                           jne 0x1405f24f6
005F24EA  C7 47 08 40 3F 00 00            mov dword ptr [rdi + 8], 0x3f40
005F24F1  E9 D5 0C 00 00                  jmp 0x1405f31cb
005F24F6  44 3B F2                        cmp r14d, edx
005F24F9  73 22                           jae 0x1405f251d
005F24FB  45 85 E4                        test r12d, r12d
005F24FE  0F 84 2A 0D 00 00               je 0x1405f322e
005F2504  41 0F B6 45 00                  movzx eax, byte ptr [r13]
005F2509  41 8B CE                        mov ecx, r14d
005F250C  D3 E0                           shl eax, cl
005F250E  41 FF CC                        dec r12d
005F2511  44 03 F8                        add r15d, eax
005F2514  49 FF C5                        inc r13
005F2517  41 83 C6 08                     add r14d, 8
005F251B  EB D9                           jmp 0x1405f24f6
005F251D  41 0F B6 CF                     movzx ecx, r15b
005F2521  41 8B C7                        mov eax, r15d
005F2524  C1 E8 08                        shr eax, 8
005F2527  C1 E1 08                        shl ecx, 8
005F252A  03 C8                           add ecx, eax
005F252C  B8 85 10 42 08                  mov eax, 0x8421085
005F2531  F7 E1                           mul ecx
005F2533  8B C1                           mov eax, ecx
005F2535  2B C2                           sub eax, edx
005F2537  D1 E8                           shr eax, 1
005F2539  03 C2                           add eax, edx
005F253B  C1 E8 04                        shr eax, 4
005F253E  6B C0 1F                        imul eax, eax, 0x1f
005F2541  3B C8                           cmp ecx, eax
005F2543  74 11                           je 0x1405f2556
005F2545  48 8D 05 54 AF 0D 00            lea rax, [rip + 0xdaf54]
005F254C  BA 10 00 00 00                  mov edx, 0x10
005F2551  E9 6A 0C 00 00                  jmp 0x1405f31c0
005F2556  41 8B C7                        mov eax, r15d
005F2559  24 0F                           and al, 0xf
005F255B  3C 08                           cmp al, 8
005F255D  74 09                           je 0x1405f2568
005F255F  48 8D 05 5A AF 0D 00            lea rax, [rip + 0xdaf5a]
005F2566  EB E4                           jmp 0x1405f254c
005F2568  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
005F256B  41 83 C6 FC                     add r14d, -4
005F256F  41 C1 EF 04                     shr r15d, 4
005F2573  41 8B CF                        mov ecx, r15d
005F2576  83 E1 0F                        and ecx, 0xf
005F2579  83 C1 08                        add ecx, 8
005F257C  85 C0                           test eax, eax
005F257E  75 05                           jne 0x1405f2585
005F2580  89 4F 30                        mov dword ptr [rdi + 0x30], ecx
005F2583  8B C1                           mov eax, ecx
005F2585  83 F9 0F                        cmp ecx, 0xf
005F2588  77 5E                           ja 0x1405f25e8
005F258A  3B C8                           cmp ecx, eax
005F258C  77 5A                           ja 0x1405f25e8
005F258E  B8 01 00 00 00                  mov eax, 1
005F2593  89 6F 18                        mov dword ptr [rdi + 0x18], ebp
005F2596  D3 E0                           shl eax, cl
005F2598  45 33 C0                        xor r8d, r8d
005F259B  33 C9                           xor ecx, ecx
005F259D  89 47 1C                        mov dword ptr [rdi + 0x1c], eax
005F25A0  33 D2                           xor edx, edx
005F25A2  E8 9D DD 00 00                  call 0x140600344
005F25A7  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
005F25AC  44 8B F5                        mov r14d, ebp
005F25AF  44 8B 9C 24 A0 00 00 00         mov r11d, dword ptr [rsp + 0xa0]
005F25B7  41 C1 EF 08                     shr r15d, 8
005F25BB  41 F7 D7                        not r15d
005F25BE  89 47 20                        mov dword ptr [rdi + 0x20], eax
005F25C1  41 83 E7 02                     and r15d, 2
005F25C5  89 46 4C                        mov dword ptr [rsi + 0x4c], eax
005F25C8  41 81 CF 3D 3F 00 00            or r15d, 0x3f3d
005F25CF  44 89 7F 08                     mov dword ptr [rdi + 8], r15d
005F25D3  44 8B FD                        mov r15d, ebp
005F25D6  4C 8D 57 70                     lea r10, [rdi + 0x70]
005F25DA  4C 8D 47 74                     lea r8, [rdi + 0x74]
005F25DE  BA 10 00 00 00                  mov edx, 0x10
005F25E3  E9 E3 0B 00 00                  jmp 0x1405f31cb
005F25E8  48 8D 05 F1 AE 0D 00            lea rax, [rip + 0xdaef1]
005F25EF  E9 58 FF FF FF                  jmp 0x1405f254c
005F25F4  41 8B CE                        mov ecx, r14d
005F25F7  23 C8                           and ecx, eax
005F25F9  41 D3 EF                        shr r15d, cl
005F25FC  44 2B F1                        sub r14d, ecx
005F25FF  41 83 FE 20                     cmp r14d, 0x20
005F2603  73 22                           jae 0x1405f2627
005F2605  45 85 E4                        test r12d, r12d
005F2608  0F 84 20 0C 00 00               je 0x1405f322e
005F260E  41 0F B6 45 00                  movzx eax, byte ptr [r13]
005F2613  41 8B CE                        mov ecx, r14d
005F2616  D3 E0                           shl eax, cl
005F2618  41 FF CC                        dec r12d
005F261B  44 03 F8                        add r15d, eax
005F261E  49 FF C5                        inc r13
005F2621  41 83 C6 08                     add r14d, 8
005F2625  EB D8                           jmp 0x1405f25ff
005F2627  41 8B C7                        mov eax, r15d
005F262A  41 0F B7 CF                     movzx ecx, r15w
005F262E  F7 D0                           not eax
005F2630  C1 E8 10                        shr eax, 0x10
005F2633  3B C8                           cmp ecx, eax
005F2635  74 0C                           je 0x1405f2643
005F2637  48 8D 05 F2 AD 0D 00            lea rax, [rip + 0xdadf2]
005F263E  E9 7D 0B 00 00                  jmp 0x1405f31c0
005F2643  89 4F 50                        mov dword ptr [rdi + 0x50], ecx
005F2646  44 8B FD                        mov r15d, ebp
005F2649  44 8B F5                        mov r14d, ebp
005F264C  C7 47 08 43 3F 00 00            mov dword ptr [rdi + 8], 0x3f43
005F2653  8B 47 50                        mov eax, dword ptr [rdi + 0x50]
005F2656  85 C0                           test eax, eax
005F2658  0F 84 20 05 00 00               je 0x1405f2b7e
005F265E  41 3B C4                        cmp eax, r12d
005F2661  41 8B EC                        mov ebp, r12d
005F2664  0F 46 E8                        cmovbe ebp, eax
005F2667  41 3B EB                        cmp ebp, r11d
005F266A  41 0F 47 EB                     cmova ebp, r11d
005F266E  85 ED                           test ebp, ebp
005F2670  0F 84 B8 0B 00 00               je 0x1405f322e
005F2676  44 8B C5                        mov r8d, ebp
005F2679  49 8B D5                        mov rdx, r13
005F267C  49 8B C9                        mov rcx, r9
005F267F  8B DD                           mov ebx, ebp
005F2681  E8 BA 41 0D 00                  call 0x1406c6840
005F2686  44 8B 9C 24 A0 00 00 00         mov r11d, dword ptr [rsp + 0xa0]
005F268E  4C 03 EB                        add r13, rbx
005F2691  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
005F2696  44 2B DD                        sub r11d, ebp
005F2699  29 6F 50                        sub dword ptr [rdi + 0x50], ebp
005F269C  4C 03 CB                        add r9, rbx
005F269F  8B 5C 24 30                     mov ebx, dword ptr [rsp + 0x30]
005F26A3  44 2B E5                        sub r12d, ebp
005F26A6  44 89 9C 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r11d
005F26AE  33 ED                           xor ebp, ebp
005F26B0  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
005F26B5  E9 1C FF FF FF                  jmp 0x1405f25d6
005F26BA  81 E9 42 3F 00 00               sub ecx, 0x3f42
005F26C0  74 8A                           je 0x1405f264c
005F26C2  83 E9 01                        sub ecx, 1
005F26C5  74 8C                           je 0x1405f2653
005F26C7  83 E9 01                        sub ecx, 1
005F26CA  74 17                           je 0x1405f26e3
005F26CC  83 E9 01                        sub ecx, 1
005F26CF  0F 84 91 00 00 00               je 0x1405f2766
005F26D5  83 F9 01                        cmp ecx, 1
005F26D8  0F 85 A3 FC FF FF               jne 0x1405f2381
005F26DE  E9 80 01 00 00                  jmp 0x1405f2863
005F26E3  41 83 FE 0E                     cmp r14d, 0xe
005F26E7  73 22                           jae 0x1405f270b
005F26E9  45 85 E4                        test r12d, r12d
005F26EC  0F 84 3C 0B 00 00               je 0x1405f322e
005F26F2  41 0F B6 45 00                  movzx eax, byte ptr [r13]
005F26F7  41 8B CE                        mov ecx, r14d
005F26FA  D3 E0                           shl eax, cl
005F26FC  41 FF CC                        dec r12d
005F26FF  44 03 F8                        add r15d, eax
005F2702  49 FF C5                        inc r13
005F2705  41 83 C6 08                     add r14d, 8
005F2709  EB D8                           jmp 0x1405f26e3
005F270B  41 8B CF                        mov ecx, r15d
005F270E  41 83 C6 F2                     add r14d, -0xe
005F2712  41 C1 EF 05                     shr r15d, 5
005F2716  83 E1 1F                        and ecx, 0x1f
005F2719  41 8B D7                        mov edx, r15d
005F271C  81 C1 01 01 00 00               add ecx, 0x101
005F2722  41 C1 EF 05                     shr r15d, 5
005F2726  83 E2 1F                        and edx, 0x1f
005F2729  41 8B C7                        mov eax, r15d
005F272C  89 4F 7C                        mov dword ptr [rdi + 0x7c], ecx
005F272F  83 E0 0F                        and eax, 0xf
005F2732  41 C1 EF 04                     shr r15d, 4
005F2736  83 C0 04                        add eax, 4
005F2739  FF C2                           inc edx
005F273B  89 97 80 00 00 00               mov dword ptr [rdi + 0x80], edx
005F2741  89 47 78                        mov dword ptr [rdi + 0x78], eax
005F2744  81 F9 1E 01 00 00               cmp ecx, 0x11e
005F274A  0F 87 22 04 00 00               ja 0x1405f2b72
005F2750  83 FA 1E                        cmp edx, 0x1e
005F2753  0F 87 19 04 00 00               ja 0x1405f2b72
005F2759  89 AF 84 00 00 00               mov dword ptr [rdi + 0x84], ebp
005F275F  C7 47 08 45 3F 00 00            mov dword ptr [rdi + 8], 0x3f45
005F2766  BA 07 00 00 00                  mov edx, 7
005F276B  4C 8D 05 9E 33 A4 FF            lea r8, [rip - 0x5bcc62]
005F2772  8B 87 84 00 00 00               mov eax, dword ptr [rdi + 0x84]
005F2778  3B 47 78                        cmp eax, dword ptr [rdi + 0x78]
005F277B  73 6D                           jae 0x1405f27ea
005F277D  41 83 FE 03                     cmp r14d, 3
005F2781  73 22                           jae 0x1405f27a5
005F2783  45 85 E4                        test r12d, r12d
005F2786  0F 84 A2 0A 00 00               je 0x1405f322e
005F278C  41 0F B6 45 00                  movzx eax, byte ptr [r13]
005F2791  41 8B CE                        mov ecx, r14d
005F2794  D3 E0                           shl eax, cl
005F2796  41 FF CC                        dec r12d
005F2799  44 03 F8                        add r15d, eax
005F279C  49 FF C5                        inc r13
005F279F  41 83 C6 08                     add r14d, 8
005F27A3  EB D8                           jmp 0x1405f277d
005F27A5  8B 87 84 00 00 00               mov eax, dword ptr [rdi + 0x84]
005F27AB  41 0F B7 CF                     movzx ecx, r15w
005F27AF  66 23 CA                        and cx, dx
005F27B2  41 C1 EF 03                     shr r15d, 3
005F27B6  41 0F B7 04 40                  movzx eax, word ptr [r8 + rax*2]
005F27BB  66 89 8C 47 90 00 00 00         mov word ptr [rdi + rax*2 + 0x90], cx
005F27C3  FF 87 84 00 00 00               inc dword ptr [rdi + 0x84]
005F27C9  41 83 C6 FD                     add r14d, -3
005F27CD  EB A3                           jmp 0x1405f2772
005F27CF  41 0F B7 0C 40                  movzx ecx, word ptr [r8 + rax*2]
005F27D4  66 89 AC 4F 90 00 00 00         mov word ptr [rdi + rcx*2 + 0x90], bp
005F27DC  8B 87 84 00 00 00               mov eax, dword ptr [rdi + 0x84]
005F27E2  FF C0                           inc eax
005F27E4  89 87 84 00 00 00               mov dword ptr [rdi + 0x84], eax
005F27EA  83 F8 13                        cmp eax, 0x13
005F27ED  72 E0                           jb 0x1405f27cf
005F27EF  48 8D 87 50 05 00 00            lea rax, [rdi + 0x550]
005F27F6  41 89 12                        mov dword ptr [r10], edx
005F27F9  4C 8D 8F 88 00 00 00            lea r9, [rdi + 0x88]
005F2800  48 89 47 60                     mov qword ptr [rdi + 0x60], rax
005F2804  33 C9                           xor ecx, ecx
005F2806  49 89 01                        mov qword ptr [r9], rax
005F2809  48 8D 87 10 03 00 00            lea rax, [rdi + 0x310]
005F2810  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005F2815  48 8D 97 90 00 00 00            lea rdx, [rdi + 0x90]
005F281C  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
005F2821  44 8D 41 13                     lea r8d, [rcx + 0x13]
005F2825  E8 3A DE 00 00                  call 0x140600664
005F282A  44 8B 9C 24 A0 00 00 00         mov r11d, dword ptr [rsp + 0xa0]
005F2832  4C 8D 57 70                     lea r10, [rdi + 0x70]
005F2836  89 84 24 98 00 00 00            mov dword ptr [rsp + 0x98], eax
005F283D  85 C0                           test eax, eax
005F283F  74 15                           je 0x1405f2856
005F2841  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
005F2846  48 8D 05 33 AC 0D 00            lea rax, [rip + 0xdac33]
005F284D  4C 8D 47 74                     lea r8, [rdi + 0x74]
005F2851  E9 F6 FC FF FF                  jmp 0x1405f254c
005F2856  89 AF 84 00 00 00               mov dword ptr [rdi + 0x84], ebp
005F285C  C7 47 08 46 3F 00 00            mov dword ptr [rdi + 8], 0x3f46
005F2863  8B 87 80 00 00 00               mov eax, dword ptr [rdi + 0x80]
005F2869  03 47 7C                        add eax, dword ptr [rdi + 0x7c]
005F286C  39 87 84 00 00 00               cmp dword ptr [rdi + 0x84], eax
005F2872  0F 83 E4 01 00 00               jae 0x1405f2a5c
005F2878  41 8B 0A                        mov ecx, dword ptr [r10]
005F287B  41 B9 01 00 00 00               mov r9d, 1
005F2881  4C 8B 47 60                     mov r8, qword ptr [rdi + 0x60]
005F2885  41 D3 E1                        shl r9d, cl
005F2888  41 FF C9                        dec r9d
005F288B  41 8B C7                        mov eax, r15d
005F288E  41 8B C9                        mov ecx, r9d
005F2891  48 23 C8                        and rcx, rax
005F2894  41 8B 14 88                     mov edx, dword ptr [r8 + rcx*4]
005F2898  8B C2                           mov eax, edx
005F289A  C1 E8 08                        shr eax, 8
005F289D  0F B6 C8                        movzx ecx, al
005F28A0  89 94 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], edx
005F28A7  41 3B CE                        cmp ecx, r14d
005F28AA  76 22                           jbe 0x1405f28ce
005F28AC  45 85 E4                        test r12d, r12d
005F28AF  0F 84 79 09 00 00               je 0x1405f322e
005F28B5  41 0F B6 45 00                  movzx eax, byte ptr [r13]
005F28BA  41 8B CE                        mov ecx, r14d
005F28BD  D3 E0                           shl eax, cl
005F28BF  41 FF CC                        dec r12d
005F28C2  44 03 F8                        add r15d, eax
005F28C5  49 FF C5                        inc r13
005F28C8  41 83 C6 08                     add r14d, 8
005F28CC  EB BD                           jmp 0x1405f288b
005F28CE  C1 EA 10                        shr edx, 0x10
005F28D1  B8 10 00 00 00                  mov eax, 0x10
005F28D6  66 3B D0                        cmp dx, ax
005F28D9  73 1F                           jae 0x1405f28fa
005F28DB  8B 87 84 00 00 00               mov eax, dword ptr [rdi + 0x84]
005F28E1  44 2B F1                        sub r14d, ecx
005F28E4  41 D3 EF                        shr r15d, cl
005F28E7  66 89 94 47 90 00 00 00         mov word ptr [rdi + rax*2 + 0x90], dx
005F28EF  FF 87 84 00 00 00               inc dword ptr [rdi + 0x84]
005F28F5  E9 69 FF FF FF                  jmp 0x1405f2863
005F28FA  75 6A                           jne 0x1405f2966
005F28FC  0F B6 94 24 A9 00 00 00         movzx edx, byte ptr [rsp + 0xa9]
005F2904  44 8D 42 02                     lea r8d, [rdx + 2]
005F2908  45 3B F0                        cmp r14d, r8d
005F290B  73 22                           jae 0x1405f292f
005F290D  45 85 E4                        test r12d, r12d
005F2910  0F 84 18 09 00 00               je 0x1405f322e
005F2916  41 0F B6 45 00                  movzx eax, byte ptr [r13]
005F291B  41 8B CE                        mov ecx, r14d
005F291E  D3 E0                           shl eax, cl
005F2920  41 FF CC                        dec r12d
005F2923  44 03 F8                        add r15d, eax
005F2926  49 FF C5                        inc r13
005F2929  41 83 C6 08                     add r14d, 8
005F292D  EB D9                           jmp 0x1405f2908
005F292F  8B 87 84 00 00 00               mov eax, dword ptr [rdi + 0x84]
005F2935  8B CA                           mov ecx, edx
005F2937  41 D3 EF                        shr r15d, cl
005F293A  44 2B F2                        sub r14d, edx
005F293D  85 C0                           test eax, eax
005F293F  0F 84 05 01 00 00               je 0x1405f2a4a
005F2945  41 8B D7                        mov edx, r15d
005F2948  41 83 C6 FE                     add r14d, -2
005F294C  83 E2 03                        and edx, 3
005F294F  41 C1 EF 02                     shr r15d, 2
005F2953  83 C2 03                        add edx, 3
005F2956  FF C8                           dec eax
005F2958  44 0F B7 8C 47 90 00 00 00      movzx r9d, word ptr [rdi + rax*2 + 0x90]
005F2961  E9 A9 00 00 00                  jmp 0x1405f2a0f
005F2966  66 83 BC 24 AA 00 00 00 11      cmp word ptr [rsp + 0xaa], 0x11
005F296F  44 0F B6 84 24 A9 00 00 00      movzx r8d, byte ptr [rsp + 0xa9]
005F2978  75 48                           jne 0x1405f29c2
005F297A  41 8D 50 03                     lea edx, [r8 + 3]
005F297E  44 3B F2                        cmp r14d, edx
005F2981  73 22                           jae 0x1405f29a5
005F2983  45 85 E4                        test r12d, r12d
005F2986  0F 84 A2 08 00 00               je 0x1405f322e
005F298C  41 0F B6 45 00                  movzx eax, byte ptr [r13]
005F2991  41 8B CE                        mov ecx, r14d
005F2994  D3 E0                           shl eax, cl
005F2996  41 FF CC                        dec r12d
005F2999  44 03 F8                        add r15d, eax
005F299C  49 FF C5                        inc r13
005F299F  41 83 C6 08                     add r14d, 8
005F29A3  EB D9                           jmp 0x1405f297e
005F29A5  41 8B C8                        mov ecx, r8d
005F29A8  44 8B CD                        mov r9d, ebp
005F29AB  41 D3 EF                        shr r15d, cl
005F29AE  B9 FD FF FF FF                  mov ecx, 0xfffffffd
005F29B3  41 8B D7                        mov edx, r15d
005F29B6  83 E2 07                        and edx, 7
005F29B9  83 C2 03                        add edx, 3
005F29BC  41 C1 EF 03                     shr r15d, 3
005F29C0  EB 47                           jmp 0x1405f2a09
005F29C2  41 8D 50 07                     lea edx, [r8 + 7]
005F29C6  44 3B F2                        cmp r14d, edx
005F29C9  73 22                           jae 0x1405f29ed
005F29CB  45 85 E4                        test r12d, r12d
005F29CE  0F 84 5A 08 00 00               je 0x1405f322e
005F29D4  41 0F B6 45 00                  movzx eax, byte ptr [r13]
005F29D9  41 8B CE                        mov ecx, r14d
005F29DC  D3 E0                           shl eax, cl
005F29DE  41 FF CC                        dec r12d
005F29E1  44 03 F8                        add r15d, eax
005F29E4  49 FF C5                        inc r13
005F29E7  41 83 C6 08                     add r14d, 8
005F29EB  EB D9                           jmp 0x1405f29c6
005F29ED  41 8B C8                        mov ecx, r8d
005F29F0  44 0F B7 CD                     movzx r9d, bp
005F29F4  41 D3 EF                        shr r15d, cl
005F29F7  B9 F9 FF FF FF                  mov ecx, 0xfffffff9
005F29FC  41 8B D7                        mov edx, r15d
005F29FF  83 E2 7F                        and edx, 0x7f
005F2A02  83 C2 0B                        add edx, 0xb
005F2A05  41 C1 EF 07                     shr r15d, 7
005F2A09  41 2B C8                        sub ecx, r8d
005F2A0C  44 03 F1                        add r14d, ecx
005F2A0F  44 8B 87 84 00 00 00            mov r8d, dword ptr [rdi + 0x84]
005F2A16  8B 87 80 00 00 00               mov eax, dword ptr [rdi + 0x80]
005F2A1C  03 47 7C                        add eax, dword ptr [rdi + 0x7c]
005F2A1F  41 8D 0C 10                     lea ecx, [r8 + rdx]
005F2A23  3B C8                           cmp ecx, eax
005F2A25  77 23                           ja 0x1405f2a4a
005F2A27  41 8B C0                        mov eax, r8d
005F2A2A  66 44 89 8C 47 90 00 00 00      mov word ptr [rdi + rax*2 + 0x90], r9w
005F2A33  FF 87 84 00 00 00               inc dword ptr [rdi + 0x84]
005F2A39  44 8B 87 84 00 00 00            mov r8d, dword ptr [rdi + 0x84]
005F2A40  83 C2 FF                        add edx, -1
005F2A43  75 E2                           jne 0x1405f2a27
005F2A45  E9 19 FE FF FF                  jmp 0x1405f2863
005F2A4A  48 8D 05 2F AB 0D 00            lea rax, [rip + 0xdab2f]
005F2A51  48 89 46 20                     mov qword ptr [rsi + 0x20], rax
005F2A55  C7 47 08 51 3F 00 00            mov dword ptr [rdi + 8], 0x3f51
005F2A5C  81 7F 08 51 3F 00 00            cmp dword ptr [rdi + 8], 0x3f51
005F2A63  4C 8D 47 74                     lea r8, [rdi + 0x74]
005F2A67  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
005F2A6C  BA 10 00 00 00                  mov edx, 0x10
005F2A71  8D 42 F7                        lea eax, [rdx - 9]
005F2A74  0F 84 B8 F8 FF FF               je 0x1405f2332
005F2A7A  66 39 AF 90 02 00 00            cmp word ptr [rdi + 0x290], bp
005F2A81  75 10                           jne 0x1405f2a93
005F2A83  48 8D 05 16 AB 0D 00            lea rax, [rip + 0xdab16]
005F2A8A  4C 8D 47 74                     lea r8, [rdi + 0x74]
005F2A8E  E9 2D 07 00 00                  jmp 0x1405f31c0
005F2A93  44 8B 47 7C                     mov r8d, dword ptr [rdi + 0x7c]
005F2A97  48 8D 87 50 05 00 00            lea rax, [rdi + 0x550]
005F2A9E  48 8D 9F 88 00 00 00            lea rbx, [rdi + 0x88]
005F2AA5  48 89 47 60                     mov qword ptr [rdi + 0x60], rax
005F2AA9  48 8D AF 10 03 00 00            lea rbp, [rdi + 0x310]
005F2AB0  48 89 03                        mov qword ptr [rbx], rax
005F2AB3  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
005F2AB8  48 8D 97 90 00 00 00            lea rdx, [rdi + 0x90]
005F2ABF  4C 8B CB                        mov r9, rbx
005F2AC2  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
005F2AC7  B9 01 00 00 00                  mov ecx, 1
005F2ACC  41 C7 02 0A 00 00 00            mov dword ptr [r10], 0xa
005F2AD3  E8 8C DB 00 00                  call 0x140600664
005F2AD8  89 84 24 98 00 00 00            mov dword ptr [rsp + 0x98], eax
005F2ADF  85 C0                           test eax, eax
005F2AE1  74 27                           je 0x1405f2b0a
005F2AE3  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
005F2AE8  48 8D 05 E1 AA 0D 00            lea rax, [rip + 0xdaae1]
005F2AEF  8B 5C 24 30                     mov ebx, dword ptr [rsp + 0x30]
005F2AF3  4C 8D 57 70                     lea r10, [rdi + 0x70]
005F2AF7  44 8B 9C 24 A0 00 00 00         mov r11d, dword ptr [rsp + 0xa0]
005F2AFF  4C 8D 47 74                     lea r8, [rdi + 0x74]
005F2B03  33 ED                           xor ebp, ebp
005F2B05  E9 42 FA FF FF                  jmp 0x1405f254c
005F2B0A  48 8B 03                        mov rax, qword ptr [rbx]
005F2B0D  48 8D 4F 74                     lea rcx, [rdi + 0x74]
005F2B11  44 8B 87 80 00 00 00            mov r8d, dword ptr [rdi + 0x80]
005F2B18  4C 8B CB                        mov r9, rbx
005F2B1B  48 89 47 68                     mov qword ptr [rdi + 0x68], rax
005F2B1F  8B 47 7C                        mov eax, dword ptr [rdi + 0x7c]
005F2B22  48 83 C0 48                     add rax, 0x48
005F2B26  C7 01 09 00 00 00               mov dword ptr [rcx], 9
005F2B2C  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
005F2B31  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
005F2B36  B9 02 00 00 00                  mov ecx, 2
005F2B3B  48 8D 14 47                     lea rdx, [rdi + rax*2]
005F2B3F  E8 20 DB 00 00                  call 0x140600664
005F2B44  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
005F2B49  4C 8D 57 70                     lea r10, [rdi + 0x70]
005F2B4D  8B 5C 24 30                     mov ebx, dword ptr [rsp + 0x30]
005F2B51  33 ED                           xor ebp, ebp
005F2B53  44 8B 9C 24 A0 00 00 00         mov r11d, dword ptr [rsp + 0xa0]
005F2B5B  89 84 24 98 00 00 00            mov dword ptr [rsp + 0x98], eax
005F2B62  85 C0                           test eax, eax
005F2B64  74 24                           je 0x1405f2b8a
005F2B66  48 8D 05 83 AA 0D 00            lea rax, [rip + 0xdaa83]
005F2B6D  E9 DB FC FF FF                  jmp 0x1405f284d
005F2B72  48 8D 05 D7 A8 0D 00            lea rax, [rip + 0xda8d7]
005F2B79  E9 CE F9 FF FF                  jmp 0x1405f254c
005F2B7E  C7 47 08 3F 3F 00 00            mov dword ptr [rdi + 8], 0x3f3f
005F2B85  E9 41 06 00 00                  jmp 0x1405f31cb
005F2B8A  C7 47 08 48 3F 00 00            mov dword ptr [rdi + 8], 0x3f48
005F2B91  41 83 FC 0F                     cmp r12d, 0xf
005F2B95  0F 82 CA 00 00 00               jb 0x1405f2c65
005F2B9B  41 81 FB 04 01 00 00            cmp r11d, 0x104
005F2BA2  0F 82 BD 00 00 00               jb 0x1405f2c65
005F2BA8  48 8B 6C 24 40                  mov rbp, qword ptr [rsp + 0x40]
005F2BAD  8B D3                           mov edx, ebx
005F2BAF  44 89 5E 18                     mov dword ptr [rsi + 0x18], r11d
005F2BB3  48 8B CE                        mov rcx, rsi
005F2BB6  4C 89 2E                        mov qword ptr [rsi], r13
005F2BB9  44 89 66 08                     mov dword ptr [rsi + 8], r12d
005F2BBD  4C 89 4D 00                     mov qword ptr [rbp], r9
005F2BC1  44 89 7F 48                     mov dword ptr [rdi + 0x48], r15d
005F2BC5  44 89 77 4C                     mov dword ptr [rdi + 0x4c], r14d
005F2BC9  E8 7E D2 00 00                  call 0x1405ffe4c
005F2BCE  81 7F 08 3F 3F 00 00            cmp dword ptr [rdi + 8], 0x3f3f
005F2BD5  4C 8D 57 70                     lea r10, [rdi + 0x70]
005F2BD9  4C 8B 4D 00                     mov r9, qword ptr [rbp]
005F2BDD  4C 8D 47 74                     lea r8, [rdi + 0x74]
005F2BE1  44 8B 5E 18                     mov r11d, dword ptr [rsi + 0x18]
005F2BE5  BD 00 00 00 00                  mov ebp, 0
005F2BEA  4C 8B 2E                        mov r13, qword ptr [rsi]
005F2BED  44 8B 66 08                     mov r12d, dword ptr [rsi + 8]
005F2BF1  44 8B 7F 48                     mov r15d, dword ptr [rdi + 0x48]
005F2BF5  44 8B 77 4C                     mov r14d, dword ptr [rdi + 0x4c]
005F2BF9  8D 55 10                        lea edx, [rbp + 0x10]
005F2BFC  8D 45 07                        lea eax, [rbp + 7]
005F2BFF  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
005F2C04  44 89 9C 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r11d
005F2C0C  0F 85 20 F7 FF FF               jne 0x1405f2332
005F2C12  83 8F 64 23 00 00 FF            or dword ptr [rdi + 0x2364], 0xffffffff
005F2C19  E9 0C F7 FF FF                  jmp 0x1405f232a
005F2C1E  81 F9 4D 3F 00 00               cmp ecx, 0x3f4d
005F2C24  0F 8F F5 04 00 00               jg 0x1405f311f
005F2C2A  0F 84 C1 04 00 00               je 0x1405f30f1
005F2C30  81 E9 48 3F 00 00               sub ecx, 0x3f48
005F2C36  0F 84 55 FF FF FF               je 0x1405f2b91
005F2C3C  83 E9 01                        sub ecx, 1
005F2C3F  0F 84 85 01 00 00               je 0x1405f2dca
005F2C45  83 E9 01                        sub ecx, 1
005F2C48  0F 84 D8 01 00 00               je 0x1405f2e26
005F2C4E  83 E9 01                        sub ecx, 1
005F2C51  0F 84 F3 02 00 00               je 0x1405f2f4a
005F2C57  83 F9 01                        cmp ecx, 1
005F2C5A  0F 85 21 F7 FF FF               jne 0x1405f2381
005F2C60  E9 3D 03 00 00                  jmp 0x1405f2fa2
005F2C65  41 8B 0A                        mov ecx, dword ptr [r10]
005F2C68  41 B8 01 00 00 00               mov r8d, 1
005F2C6E  48 8B 57 60                     mov rdx, qword ptr [rdi + 0x60]
005F2C72  41 D3 E0                        shl r8d, cl
005F2C75  41 FF C8                        dec r8d
005F2C78  89 AF 64 23 00 00               mov dword ptr [rdi + 0x2364], ebp
005F2C7E  41 8B C7                        mov eax, r15d
005F2C81  41 8B C8                        mov ecx, r8d
005F2C84  48 23 C8                        and rcx, rax
005F2C87  8B 04 8A                        mov eax, dword ptr [rdx + rcx*4]
005F2C8A  8B C8                           mov ecx, eax
005F2C8C  C1 E9 08                        shr ecx, 8
005F2C8F  0F B6 C9                        movzx ecx, cl
005F2C92  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
005F2C99  41 3B CE                        cmp ecx, r14d
005F2C9C  76 22                           jbe 0x1405f2cc0
005F2C9E  45 85 E4                        test r12d, r12d
005F2CA1  0F 84 87 05 00 00               je 0x1405f322e
005F2CA7  41 0F B6 45 00                  movzx eax, byte ptr [r13]
005F2CAC  41 8B CE                        mov ecx, r14d
005F2CAF  D3 E0                           shl eax, cl
005F2CB1  41 FF CC                        dec r12d
005F2CB4  44 03 F8                        add r15d, eax
005F2CB7  49 FF C5                        inc r13
005F2CBA  41 83 C6 08                     add r14d, 8
005F2CBE  EB BE                           jmp 0x1405f2c7e
005F2CC0  84 C0                           test al, al
005F2CC2  0F 84 82 00 00 00               je 0x1405f2d4a
005F2CC8  A8 F0                           test al, 0xf0
005F2CCA  75 7E                           jne 0x1405f2d4a
005F2CCC  44 0F B6 84 24 A9 00 00 00      movzx r8d, byte ptr [rsp + 0xa9]
005F2CD5  41 B9 01 00 00 00               mov r9d, 1
005F2CDB  4C 8B 57 60                     mov r10, qword ptr [rdi + 0x60]
005F2CDF  44 0F B7 9C 24 AA 00 00 00      movzx r11d, word ptr [rsp + 0xaa]
005F2CE8  0F B6 C8                        movzx ecx, al
005F2CEB  41 03 C8                        add ecx, r8d
005F2CEE  41 D3 E1                        shl r9d, cl
005F2CF1  41 8D 41 FF                     lea eax, [r9 - 1]
005F2CF5  41 8B C8                        mov ecx, r8d
005F2CF8  41 23 C7                        and eax, r15d
005F2CFB  D3 E8                           shr eax, cl
005F2CFD  41 03 C3                        add eax, r11d
005F2D00  41 8B 04 82                     mov eax, dword ptr [r10 + rax*4]
005F2D04  8B C8                           mov ecx, eax
005F2D06  C1 E9 08                        shr ecx, 8
005F2D09  0F B6 D1                        movzx edx, cl
005F2D0C  41 03 D0                        add edx, r8d
005F2D0F  41 3B D6                        cmp edx, r14d
005F2D12  76 22                           jbe 0x1405f2d36
005F2D14  45 85 E4                        test r12d, r12d
005F2D17  0F 84 11 05 00 00               je 0x1405f322e
005F2D1D  41 0F B6 45 00                  movzx eax, byte ptr [r13]
005F2D22  41 8B CE                        mov ecx, r14d
005F2D25  D3 E0                           shl eax, cl
005F2D27  41 FF CC                        dec r12d
005F2D2A  44 03 F8                        add r15d, eax
005F2D2D  49 FF C5                        inc r13
005F2D30  41 83 C6 08                     add r14d, 8
005F2D34  EB BB                           jmp 0x1405f2cf1
005F2D36  41 8B C8                        mov ecx, r8d
005F2D39  44 89 87 64 23 00 00            mov dword ptr [rdi + 0x2364], r8d
005F2D40  41 D3 EF                        shr r15d, cl
005F2D43  4C 8D 57 70                     lea r10, [rdi + 0x70]
005F2D47  45 2B F0                        sub r14d, r8d
005F2D4A  8B C8                           mov ecx, eax
005F2D4C  C1 E9 08                        shr ecx, 8
005F2D4F  0F B6 D1                        movzx edx, cl
005F2D52  01 97 64 23 00 00               add dword ptr [rdi + 0x2364], edx
005F2D58  8B CA                           mov ecx, edx
005F2D5A  41 D3 EF                        shr r15d, cl
005F2D5D  44 2B F2                        sub r14d, edx
005F2D60  8B C8                           mov ecx, eax
005F2D62  C1 E9 10                        shr ecx, 0x10
005F2D65  89 4F 50                        mov dword ptr [rdi + 0x50], ecx
005F2D68  84 C0                           test al, al
005F2D6A  75 19                           jne 0x1405f2d85
005F2D6C  C7 47 08 4D 3F 00 00            mov dword ptr [rdi + 8], 0x3f4d
005F2D73  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
005F2D78  44 8B 9C 24 A0 00 00 00         mov r11d, dword ptr [rsp + 0xa0]
005F2D80  E9 55 F8 FF FF                  jmp 0x1405f25da
005F2D85  A8 20                           test al, 0x20
005F2D87  74 10                           je 0x1405f2d99
005F2D89  83 8F 64 23 00 00 FF            or dword ptr [rdi + 0x2364], 0xffffffff
005F2D90  C7 47 08 3F 3F 00 00            mov dword ptr [rdi + 8], 0x3f3f
005F2D97  EB DA                           jmp 0x1405f2d73
005F2D99  4C 8D 47 74                     lea r8, [rdi + 0x74]
005F2D9D  A8 40                           test al, 0x40
005F2D9F  74 19                           je 0x1405f2dba
005F2DA1  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
005F2DA6  48 8D 05 53 A7 0D 00            lea rax, [rip + 0xda753]
005F2DAD  44 8B 9C 24 A0 00 00 00         mov r11d, dword ptr [rsp + 0xa0]
005F2DB5  E9 92 F7 FF FF                  jmp 0x1405f254c
005F2DBA  0F B6 C8                        movzx ecx, al
005F2DBD  83 E1 0F                        and ecx, 0xf
005F2DC0  C7 47 08 49 3F 00 00            mov dword ptr [rdi + 8], 0x3f49
005F2DC7  89 4F 58                        mov dword ptr [rdi + 0x58], ecx
005F2DCA  8B 57 58                        mov edx, dword ptr [rdi + 0x58]
005F2DCD  85 D2                           test edx, edx
005F2DCF  74 45                           je 0x1405f2e16
005F2DD1  44 3B F2                        cmp r14d, edx
005F2DD4  73 22                           jae 0x1405f2df8
005F2DD6  45 85 E4                        test r12d, r12d
005F2DD9  0F 84 4F 04 00 00               je 0x1405f322e
005F2DDF  41 0F B6 45 00                  movzx eax, byte ptr [r13]
005F2DE4  41 8B CE                        mov ecx, r14d
005F2DE7  D3 E0                           shl eax, cl
005F2DE9  41 FF CC                        dec r12d
005F2DEC  44 03 F8                        add r15d, eax
005F2DEF  49 FF C5                        inc r13
005F2DF2  41 83 C6 08                     add r14d, 8
005F2DF6  EB D9                           jmp 0x1405f2dd1
005F2DF8  8B 4F 58                        mov ecx, dword ptr [rdi + 0x58]
005F2DFB  B8 01 00 00 00                  mov eax, 1
005F2E00  D3 E0                           shl eax, cl
005F2E02  44 2B F1                        sub r14d, ecx
005F2E05  FF C8                           dec eax
005F2E07  41 23 C7                        and eax, r15d
005F2E0A  41 D3 EF                        shr r15d, cl
005F2E0D  01 47 50                        add dword ptr [rdi + 0x50], eax
005F2E10  01 8F 64 23 00 00               add dword ptr [rdi + 0x2364], ecx
005F2E16  8B 47 50                        mov eax, dword ptr [rdi + 0x50]
005F2E19  89 87 68 23 00 00               mov dword ptr [rdi + 0x2368], eax
005F2E1F  C7 47 08 4A 3F 00 00            mov dword ptr [rdi + 8], 0x3f4a
005F2E26  41 8B 08                        mov ecx, dword ptr [r8]
005F2E29  41 B8 01 00 00 00               mov r8d, 1
005F2E2F  48 8B 57 68                     mov rdx, qword ptr [rdi + 0x68]
005F2E33  41 D3 E0                        shl r8d, cl
005F2E36  41 FF C8                        dec r8d
005F2E39  41 8B C7                        mov eax, r15d
005F2E3C  41 8B C8                        mov ecx, r8d
005F2E3F  48 23 C8                        and rcx, rax
005F2E42  8B 04 8A                        mov eax, dword ptr [rdx + rcx*4]
005F2E45  8B C8                           mov ecx, eax
005F2E47  C1 E9 08                        shr ecx, 8
005F2E4A  0F B6 C9                        movzx ecx, cl
005F2E4D  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
005F2E54  41 3B CE                        cmp ecx, r14d
005F2E57  76 22                           jbe 0x1405f2e7b
005F2E59  45 85 E4                        test r12d, r12d
005F2E5C  0F 84 CC 03 00 00               je 0x1405f322e
005F2E62  41 0F B6 45 00                  movzx eax, byte ptr [r13]
005F2E67  41 8B CE                        mov ecx, r14d
005F2E6A  D3 E0                           shl eax, cl
005F2E6C  41 FF CC                        dec r12d
005F2E6F  44 03 F8                        add r15d, eax
005F2E72  49 FF C5                        inc r13
005F2E75  41 83 C6 08                     add r14d, 8
005F2E79  EB BE                           jmp 0x1405f2e39
005F2E7B  A8 F0                           test al, 0xf0
005F2E7D  75 7A                           jne 0x1405f2ef9
005F2E7F  44 0F B6 84 24 A9 00 00 00      movzx r8d, byte ptr [rsp + 0xa9]
005F2E88  41 B9 01 00 00 00               mov r9d, 1
005F2E8E  4C 8B 57 68                     mov r10, qword ptr [rdi + 0x68]
005F2E92  44 0F B7 9C 24 AA 00 00 00      movzx r11d, word ptr [rsp + 0xaa]
005F2E9B  0F B6 C8                        movzx ecx, al
005F2E9E  41 03 C8                        add ecx, r8d
005F2EA1  41 D3 E1                        shl r9d, cl
005F2EA4  41 8D 41 FF                     lea eax, [r9 - 1]
005F2EA8  41 8B C8                        mov ecx, r8d
005F2EAB  41 23 C7                        and eax, r15d
005F2EAE  D3 E8                           shr eax, cl
005F2EB0  41 03 C3                        add eax, r11d
005F2EB3  41 8B 04 82                     mov eax, dword ptr [r10 + rax*4]
005F2EB7  8B C8                           mov ecx, eax
005F2EB9  C1 E9 08                        shr ecx, 8
005F2EBC  0F B6 D1                        movzx edx, cl
005F2EBF  41 03 D0                        add edx, r8d
005F2EC2  41 3B D6                        cmp edx, r14d
005F2EC5  76 22                           jbe 0x1405f2ee9
005F2EC7  45 85 E4                        test r12d, r12d
005F2ECA  0F 84 5E 03 00 00               je 0x1405f322e
005F2ED0  41 0F B6 45 00                  movzx eax, byte ptr [r13]
005F2ED5  41 8B CE                        mov ecx, r14d
005F2ED8  D3 E0                           shl eax, cl
005F2EDA  41 FF CC                        dec r12d
005F2EDD  44 03 F8                        add r15d, eax
005F2EE0  49 FF C5                        inc r13
005F2EE3  41 83 C6 08                     add r14d, 8
005F2EE7  EB BB                           jmp 0x1405f2ea4
005F2EE9  41 8B C8                        mov ecx, r8d
005F2EEC  45 2B F0                        sub r14d, r8d
005F2EEF  41 D3 EF                        shr r15d, cl
005F2EF2  44 01 87 64 23 00 00            add dword ptr [rdi + 0x2364], r8d
005F2EF9  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
005F2EFE  4C 8D 57 70                     lea r10, [rdi + 0x70]
005F2F02  44 8B 9C 24 A0 00 00 00         mov r11d, dword ptr [rsp + 0xa0]
005F2F0A  4C 8D 47 74                     lea r8, [rdi + 0x74]
005F2F0E  8B C8                           mov ecx, eax
005F2F10  C1 E9 08                        shr ecx, 8
005F2F13  0F B6 C9                        movzx ecx, cl
005F2F16  01 8F 64 23 00 00               add dword ptr [rdi + 0x2364], ecx
005F2F1C  44 2B F1                        sub r14d, ecx
005F2F1F  41 D3 EF                        shr r15d, cl
005F2F22  A8 40                           test al, 0x40
005F2F24  74 0C                           je 0x1405f2f32
005F2F26  48 8D 05 F3 A5 0D 00            lea rax, [rip + 0xda5f3]
005F2F2D  E9 1A F6 FF FF                  jmp 0x1405f254c
005F2F32  8B C8                           mov ecx, eax
005F2F34  C7 47 08 4B 3F 00 00            mov dword ptr [rdi + 8], 0x3f4b
005F2F3B  C1 E9 10                        shr ecx, 0x10
005F2F3E  89 4F 54                        mov dword ptr [rdi + 0x54], ecx
005F2F41  0F B6 C8                        movzx ecx, al
005F2F44  83 E1 0F                        and ecx, 0xf
005F2F47  89 4F 58                        mov dword ptr [rdi + 0x58], ecx
005F2F4A  8B 57 58                        mov edx, dword ptr [rdi + 0x58]
005F2F4D  85 D2                           test edx, edx
005F2F4F  74 45                           je 0x1405f2f96
005F2F51  44 3B F2                        cmp r14d, edx
005F2F54  73 22                           jae 0x1405f2f78
005F2F56  45 85 E4                        test r12d, r12d
005F2F59  0F 84 CF 02 00 00               je 0x1405f322e
005F2F5F  41 0F B6 45 00                  movzx eax, byte ptr [r13]
005F2F64  41 8B CE                        mov ecx, r14d
005F2F67  D3 E0                           shl eax, cl
005F2F69  41 FF CC                        dec r12d
005F2F6C  44 03 F8                        add r15d, eax
005F2F6F  49 FF C5                        inc r13
005F2F72  41 83 C6 08                     add r14d, 8
005F2F76  EB D9                           jmp 0x1405f2f51
005F2F78  8B 4F 58                        mov ecx, dword ptr [rdi + 0x58]
005F2F7B  B8 01 00 00 00                  mov eax, 1
005F2F80  D3 E0                           shl eax, cl
005F2F82  44 2B F1                        sub r14d, ecx
005F2F85  FF C8                           dec eax
005F2F87  41 23 C7                        and eax, r15d
005F2F8A  41 D3 EF                        shr r15d, cl
005F2F8D  01 47 54                        add dword ptr [rdi + 0x54], eax
005F2F90  01 8F 64 23 00 00               add dword ptr [rdi + 0x2364], ecx
005F2F96  C7 47 08 4C 3F 00 00            mov dword ptr [rdi + 8], 0x3f4c
005F2F9D  BA 10 00 00 00                  mov edx, 0x10
005F2FA2  45 85 DB                        test r11d, r11d
005F2FA5  0F 84 83 02 00 00               je 0x1405f322e
005F2FAB  8B 4F 54                        mov ecx, dword ptr [rdi + 0x54]
005F2FAE  8B C3                           mov eax, ebx
005F2FB0  41 2B C3                        sub eax, r11d
005F2FB3  3B C8                           cmp ecx, eax
005F2FB5  0F 86 9E 00 00 00               jbe 0x1405f3059
005F2FBB  2B C8                           sub ecx, eax
005F2FBD  3B 4F 38                        cmp ecx, dword ptr [rdi + 0x38]
005F2FC0  76 14                           jbe 0x1405f2fd6
005F2FC2  39 AF 60 23 00 00               cmp dword ptr [rdi + 0x2360], ebp
005F2FC8  74 0C                           je 0x1405f2fd6
005F2FCA  48 8D 05 6F A5 0D 00            lea rax, [rip + 0xda56f]
005F2FD1  E9 EA 01 00 00                  jmp 0x1405f31c0
005F2FD6  8B 47 3C                        mov eax, dword ptr [rdi + 0x3c]
005F2FD9  4C 8B 47 40                     mov r8, qword ptr [rdi + 0x40]
005F2FDD  3B C8                           cmp ecx, eax
005F2FDF  76 09                           jbe 0x1405f2fea
005F2FE1  8B 57 34                        mov edx, dword ptr [rdi + 0x34]
005F2FE4  2B C8                           sub ecx, eax
005F2FE6  2B D1                           sub edx, ecx
005F2FE8  EB 04                           jmp 0x1405f2fee
005F2FEA  2B C1                           sub eax, ecx
005F2FEC  8B D0                           mov edx, eax
005F2FEE  44 8B 57 50                     mov r10d, dword ptr [rdi + 0x50]
005F2FF2  49 03 D0                        add rdx, r8
005F2FF5  41 3B CA                        cmp ecx, r10d
005F2FF8  44 0F 46 D1                     cmovbe r10d, ecx
005F2FFC  45 3B D3                        cmp r10d, r11d
005F2FFF  45 0F 47 D3                     cmova r10d, r11d
005F3003  41 83 FB 10                     cmp r11d, 0x10
005F3007  0F 83 9E 00 00 00               jae 0x1405f30ab
005F300D  41 F6 C2 08                     test r10b, 8
005F3011  74 0E                           je 0x1405f3021
005F3013  48 8B 02                        mov rax, qword ptr [rdx]
005F3016  49 89 01                        mov qword ptr [r9], rax
005F3019  49 83 C1 08                     add r9, 8
005F301D  48 83 C2 08                     add rdx, 8
005F3021  41 F6 C2 04                     test r10b, 4
005F3025  74 0D                           je 0x1405f3034
005F3027  8B 02                           mov eax, dword ptr [rdx]
005F3029  41 89 01                        mov dword ptr [r9], eax
005F302C  49 83 C1 04                     add r9, 4
005F3030  48 83 C2 04                     add rdx, 4
005F3034  41 F6 C2 02                     test r10b, 2
005F3038  74 0F                           je 0x1405f3049
005F303A  0F B7 02                        movzx eax, word ptr [rdx]
005F303D  66 41 89 01                     mov word ptr [r9], ax
005F3041  49 83 C1 02                     add r9, 2
005F3045  48 83 C2 02                     add rdx, 2
005F3049  41 F6 C2 01                     test r10b, 1
005F304D  74 36                           je 0x1405f3085
005F304F  8A 02                           mov al, byte ptr [rdx]
005F3051  41 88 01                        mov byte ptr [r9], al
005F3054  49 FF C1                        inc r9
005F3057  EB 2C                           jmp 0x1405f3085
005F3059  44 8B 57 50                     mov r10d, dword ptr [rdi + 0x50]
005F305D  45 3B D3                        cmp r10d, r11d
005F3060  45 0F 47 D3                     cmova r10d, r11d
005F3064  41 8B D2                        mov edx, r10d
005F3067  41 83 FB 30                     cmp r11d, 0x30
005F306B  73 1F                           jae 0x1405f308c
005F306D  45 85 D2                        test r10d, r10d
005F3070  74 13                           je 0x1405f3085
005F3072  49 8B C1                        mov rax, r9
005F3075  48 2B C1                        sub rax, rcx
005F3078  8A 00                           mov al, byte ptr [rax]
005F307A  41 88 01                        mov byte ptr [r9], al
005F307D  49 FF C1                        inc r9
005F3080  83 C2 FF                        add edx, -1
005F3083  75 ED                           jne 0x1405f3072
005F3085  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
005F308A  EB 2F                           jmp 0x1405f30bb
005F308C  41 3B CA                        cmp ecx, r10d
005F308F  73 14                           jae 0x1405f30a5
005F3091  83 F9 10                        cmp ecx, 0x10
005F3094  73 0F                           jae 0x1405f30a5
005F3096  8B D1                           mov edx, ecx
005F3098  45 8B C2                        mov r8d, r10d
005F309B  49 8B C9                        mov rcx, r9
005F309E  E8 7D F0 FF FF                  call 0x1405f2120
005F30A3  EB 11                           jmp 0x1405f30b6
005F30A5  49 8B D1                        mov rdx, r9
005F30A8  48 2B D1                        sub rdx, rcx
005F30AB  45 8B C2                        mov r8d, r10d
005F30AE  49 8B C9                        mov rcx, r9
005F30B1  E8 26 F0 FF FF                  call 0x1405f20dc
005F30B6  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005F30BB  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
005F30C0  4C 8D 47 74                     lea r8, [rdi + 0x74]
005F30C4  45 2B DA                        sub r11d, r10d
005F30C7  BA 10 00 00 00                  mov edx, 0x10
005F30CC  44 29 57 50                     sub dword ptr [rdi + 0x50], r10d
005F30D0  4C 8D 57 70                     lea r10, [rdi + 0x70]
005F30D4  44 89 9C 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r11d
005F30DC  8D 42 F7                        lea eax, [rdx - 9]
005F30DF  0F 85 4D F2 FF FF               jne 0x1405f2332
005F30E5  C7 47 08 48 3F 00 00            mov dword ptr [rdi + 8], 0x3f48
005F30EC  E9 39 F2 FF FF                  jmp 0x1405f232a
005F30F1  45 85 DB                        test r11d, r11d
005F30F4  0F 84 34 01 00 00               je 0x1405f322e
005F30FA  8A 47 50                        mov al, byte ptr [rdi + 0x50]
005F30FD  41 88 01                        mov byte ptr [r9], al
005F3100  49 FF C1                        inc r9
005F3103  41 FF CB                        dec r11d
005F3106  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
005F310B  44 89 9C 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r11d
005F3113  C7 47 08 48 3F 00 00            mov dword ptr [rdi + 8], 0x3f48
005F311A  E9 AC 00 00 00                  jmp 0x1405f31cb
005F311F  81 E9 4E 3F 00 00               sub ecx, 0x3f4e
005F3125  0F 85 DF 00 00 00               jne 0x1405f320a
005F312B  39 6F 10                        cmp dword ptr [rdi + 0x10], ebp
005F312E  0F 84 C8 00 00 00               je 0x1405f31fc
005F3134  41 83 FE 20                     cmp r14d, 0x20
005F3138  73 22                           jae 0x1405f315c
005F313A  45 85 E4                        test r12d, r12d
005F313D  0F 84 EB 00 00 00               je 0x1405f322e
005F3143  41 0F B6 45 00                  movzx eax, byte ptr [r13]
005F3148  41 8B CE                        mov ecx, r14d
005F314B  D3 E0                           shl eax, cl
005F314D  41 FF CC                        dec r12d
005F3150  44 03 F8                        add r15d, eax
005F3153  49 FF C5                        inc r13
005F3156  41 83 C6 08                     add r14d, 8
005F315A  EB D8                           jmp 0x1405f3134
005F315C  41 2B DB                        sub ebx, r11d
005F315F  01 5E 1C                        add dword ptr [rsi + 0x1c], ebx
005F3162  01 5F 24                        add dword ptr [rdi + 0x24], ebx
005F3165  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
005F3168  A8 04                           test al, 4
005F316A  74 35                           je 0x1405f31a1
005F316C  85 DB                           test ebx, ebx
005F316E  74 31                           je 0x1405f31a1
005F3170  8B 4F 20                        mov ecx, dword ptr [rdi + 0x20]
005F3173  49 8B D1                        mov rdx, r9
005F3176  44 8B C3                        mov r8d, ebx
005F3179  49 2B D0                        sub rdx, r8
005F317C  E8 C3 D1 00 00                  call 0x140600344
005F3181  4C 8B 4C 24 38                  mov r9, qword ptr [rsp + 0x38]
005F3186  4C 8D 57 70                     lea r10, [rdi + 0x70]
005F318A  44 8B 9C 24 A0 00 00 00         mov r11d, dword ptr [rsp + 0xa0]
005F3192  4C 8D 47 74                     lea r8, [rdi + 0x74]
005F3196  89 47 20                        mov dword ptr [rdi + 0x20], eax
005F3199  BA 10 00 00 00                  mov edx, 0x10
005F319E  89 46 4C                        mov dword ptr [rsi + 0x4c], eax
005F31A1  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
005F31A4  41 8B DB                        mov ebx, r11d
005F31A7  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
005F31AB  A8 04                           test al, 4
005F31AD  74 47                           je 0x1405f31f6
005F31AF  41 8B C7                        mov eax, r15d
005F31B2  0F C8                           bswap eax
005F31B4  3B 47 20                        cmp eax, dword ptr [rdi + 0x20]
005F31B7  74 3D                           je 0x1405f31f6
005F31B9  48 8D 05 A0 A3 0D 00            lea rax, [rip + 0xda3a0]
005F31C0  48 89 46 20                     mov qword ptr [rsi + 0x20], rax
005F31C4  C7 47 08 51 3F 00 00            mov dword ptr [rdi + 8], 0x3f51
005F31CB  B8 07 00 00 00                  mov eax, 7
005F31D0  E9 5D F1 FF FF                  jmp 0x1405f2332
005F31D5  4C 89 4E 10                     mov qword ptr [rsi + 0x10], r9
005F31D9  B8 02 00 00 00                  mov eax, 2
005F31DE  44 89 5E 18                     mov dword ptr [rsi + 0x18], r11d
005F31E2  4C 89 2E                        mov qword ptr [rsi], r13
005F31E5  44 89 66 08                     mov dword ptr [rsi + 8], r12d
005F31E9  44 89 7F 48                     mov dword ptr [rdi + 0x48], r15d
005F31ED  44 89 77 4C                     mov dword ptr [rdi + 0x4c], r14d
005F31F1  E9 90 F1 FF FF                  jmp 0x1405f2386
005F31F6  44 8B FD                        mov r15d, ebp
005F31F9  44 8B F5                        mov r14d, ebp
005F31FC  C7 47 08 50 3F 00 00            mov dword ptr [rdi + 8], 0x3f50
005F3203  BD 01 00 00 00                  mov ebp, 1
005F3208  EB 2B                           jmp 0x1405f3235
005F320A  83 E9 02                        sub ecx, 2
005F320D  74 F4                           je 0x1405f3203
005F320F  83 E9 01                        sub ecx, 1
005F3212  74 13                           je 0x1405f3227
005F3214  83 F9 01                        cmp ecx, 1
005F3217  0F 85 64 F1 FF FF               jne 0x1405f2381
005F321D  B8 FC FF FF FF                  mov eax, 0xfffffffc
005F3222  E9 5F F1 FF FF                  jmp 0x1405f2386
005F3227  BD FD FF FF FF                  mov ebp, 0xfffffffd
005F322C  EB 07                           jmp 0x1405f3235
005F322E  8B AC 24 98 00 00 00            mov ebp, dword ptr [rsp + 0x98]
005F3235  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
005F323A  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
005F323E  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
005F3245  89 46 18                        mov dword ptr [rsi + 0x18], eax
005F3248  4C 89 2E                        mov qword ptr [rsi], r13
005F324B  44 89 66 08                     mov dword ptr [rsi + 8], r12d
005F324F  44 89 77 4C                     mov dword ptr [rdi + 0x4c], r14d
005F3253  45 33 F6                        xor r14d, r14d
005F3256  44 89 7F 48                     mov dword ptr [rdi + 0x48], r15d
005F325A  44 39 77 34                     cmp dword ptr [rdi + 0x34], r14d
005F325E  75 0E                           jne 0x1405f326e
005F3260  3B 5E 18                        cmp ebx, dword ptr [rsi + 0x18]
005F3263  74 29                           je 0x1405f328e
005F3265  81 7F 08 4D 3F 00 00            cmp dword ptr [rdi + 8], 0x3f4d
005F326C  7F 20                           jg 0x1405f328e
005F326E  48 8B 56 10                     mov rdx, qword ptr [rsi + 0x10]
005F3272  44 8B C3                        mov r8d, ebx
005F3275  44 2B 46 18                     sub r8d, dword ptr [rsi + 0x18]
005F3279  48 8B CE                        mov rcx, rsi
005F327C  E8 37 02 00 00                  call 0x1405f34b8
005F3281  85 C0                           test eax, eax
005F3283  74 09                           je 0x1405f328e
005F3285  C7 47 08 52 3F 00 00            mov dword ptr [rdi + 8], 0x3f52
005F328C  EB 8F                           jmp 0x1405f321d
005F328E  2B 5E 18                        sub ebx, dword ptr [rsi + 0x18]
005F3291  01 5E 1C                        add dword ptr [rsi + 0x1c], ebx
005F3294  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
005F3298  2B 46 08                        sub eax, dword ptr [rsi + 8]
005F329B  01 46 0C                        add dword ptr [rsi + 0xc], eax
005F329E  01 5F 24                        add dword ptr [rdi + 0x24], ebx
005F32A1  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
005F32A4  A8 04                           test al, 4
005F32A6  74 1C                           je 0x1405f32c4
005F32A8  85 DB                           test ebx, ebx
005F32AA  74 18                           je 0x1405f32c4
005F32AC  48 8B 56 10                     mov rdx, qword ptr [rsi + 0x10]
005F32B0  8B 4F 20                        mov ecx, dword ptr [rdi + 0x20]
005F32B3  44 8B C3                        mov r8d, ebx
005F32B6  49 2B D0                        sub rdx, r8
005F32B9  E8 86 D0 00 00                  call 0x140600344
005F32BE  89 47 20                        mov dword ptr [rdi + 0x20], eax
005F32C1  89 46 4C                        mov dword ptr [rsi + 0x4c], eax
005F32C4  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
005F32C7  41 B8 80 00 00 00               mov r8d, 0x80
005F32CD  F7 D8                           neg eax
005F32CF  8B 47 08                        mov eax, dword ptr [rdi + 8]
005F32D2  1B D2                           sbb edx, edx
005F32D4  83 E2 40                        and edx, 0x40
005F32D7  3D 3F 3F 00 00                  cmp eax, 0x3f3f
005F32DC  45 0F 45 C6                     cmovne r8d, r14d
005F32E0  3D 47 3F 00 00                  cmp eax, 0x3f47
005F32E5  74 0A                           je 0x1405f32f1
005F32E7  3D 42 3F 00 00                  cmp eax, 0x3f42
005F32EC  41 8B C6                        mov eax, r14d
005F32EF  75 05                           jne 0x1405f32f6
005F32F1  B8 00 01 00 00                  mov eax, 0x100
005F32F6  8B 4F 4C                        mov ecx, dword ptr [rdi + 0x4c]
005F32F9  41 03 C8                        add ecx, r8d
005F32FC  03 CA                           add ecx, edx
005F32FE  03 C8                           add ecx, eax
005F3300  B8 FB FF FF FF                  mov eax, 0xfffffffb
005F3305  85 ED                           test ebp, ebp
005F3307  89 4E 48                        mov dword ptr [rsi + 0x48], ecx
005F330A  0F 44 E8                        cmove ebp, eax
005F330D  8B C5                           mov eax, ebp
005F330F  E9 72 F0 FF FF                  jmp 0x1405f2386
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall inflate(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p8;
    unsigned int v_stack_p98;
    unsigned int v_stack_pA0;
    unsigned int v_stack_pA8;
    unsigned __int8 v_stack_pA9;
    unsigned __int16 v_stack_pAA;

    v_stack_p8 = v_rbx;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (80);
    result = inflateStateCheck(a1, a2, a3, a4);
    v_rbp = 0;
    if ((unsigned int)(result) != 0) goto loc_005F2381;
    if ((*(unsigned __int64 *)(a1 + 16)) == 0) goto loc_005F2381;
    if ((*(unsigned __int64 *)(a1)) != 0) goto loc_005F22CB;
    if ((*(unsigned int *)(a1 + 8)) != 0) goto loc_005F2381;
    a1 = (a1) + (16);
    goto loc_005F22CE;
loc_005F22CB:
loc_005F22CE:
    v_stack_m48 = a1 + 16;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8)) == 0x3F3FULL) {
        *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F40ULL;
        v_stack_m48 = a1 + 16;
    }
    v_stack_m50 = *(unsigned __int64 *)(a1 + 16);
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)));
    v_stack_m54 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)));
    v_stack_m58 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    v_stack_p10 = 0;
loc_005F232A:
loc_005F2332:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8)))) > 0x3F47ULL) goto loc_005F2C1E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8)))) == 0x3F47ULL) goto loc_005F2B8A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8)))) > 0x3F41ULL) goto loc_005F26BA;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8)))) == 0x3F41ULL) goto loc_005F25F4;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8))) - (0x3F34ULL));
    if (condition_is_equal) goto loc_005F24E5;
    a1 = (unsigned int)((a1) - (9));
    if (condition_is_equal) goto loc_005F239F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_005F23DF;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_005F241B;
    if (((unsigned int)(a1)) == 1) goto loc_005F241B;
loc_005F2381:
loc_005F2386:
    v_rsp = (v_rsp) + (80);
    return (unsigned int)(0xFFFFFFFEULL);
loc_005F239F:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 76)))) >= 32) goto loc_005F23C7;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8))) == 0) goto loc_005F322E;
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1))) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 76)))))));
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8))) - 1);
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 72))) + ((unsigned int)(result)));
    v_r13 = (*(unsigned __int64 *)(a1)) + 1;
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 76))) + (8));
    goto loc_005F239F;
loc_005F23C7:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 32) = (unsigned int)(v_r15);
    *(unsigned int *)(a1 + 76) = (unsigned int)(v_r15);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F3EULL;
loc_005F23DF:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 20)) == 0) goto loc_005F31D5;
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = adler32_z(a1, a2, a3, *(unsigned __int64 *)(a1 + 16));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 32) = (unsigned int)(result);
    *(unsigned int *)(a1 + 76) = (unsigned int)(result);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F3FULL;
loc_005F241B:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 12)) == 0) goto loc_005F243C;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F4EULL;
    a1 = (unsigned int)((0) & (7));
    v_r15 = (unsigned int)((0) >> ((unsigned __int8)(a1)));
    v_r14 = (unsigned int)((0) - ((unsigned int)(a1)));
    goto loc_005F2332;
loc_005F243C:
    if (((unsigned int)(v_r14)) >= 3) goto loc_005F2464;
    if ((unsigned int)(v_r12) == 0) goto loc_005F322E;
    result = (unsigned int)((*(unsigned __int8 *)(v_r13)) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))));
    v_r12 = (unsigned int)((v_r12) - 1);
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(result)));
    v_r13 = (v_r13) + 1;
    v_r14 = (unsigned int)((v_r14) + (8));
    goto loc_005F243C;
loc_005F2464:
    v_r15 = (unsigned int)((v_r15) >> (1));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (1));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 12) = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (3));
    if (condition_is_equal) goto loc_005F24D1;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_005F24A4;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_005F249B;
    if (((unsigned int)(result)) != 1) goto loc_005F24D8;
    *(unsigned __int64 *)(a1 + 32) = v_rip + 896898;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F51ULL;
    goto loc_005F24D8;
loc_005F249B:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F44ULL;
    goto loc_005F24D8;
loc_005F24A4:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 112) = 9;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 96) = v_rip - 6015339;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 104) = v_rip - 6015533;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 116) = 5;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F47ULL;
    goto loc_005F24D8;
loc_005F24D1:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F41ULL;
loc_005F24D8:
    v_r15 = (unsigned int)((v_r15) >> (2));
    v_r14 = (unsigned int)((v_r14) + (-3));
    goto loc_005F31CB;
loc_005F24E5:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 16)) != 0) goto loc_005F24F6;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F40ULL;
    goto loc_005F31CB;
loc_005F24F6:
    if (((unsigned int)(v_r14)) >= 16) goto loc_005F251D;
    if ((unsigned int)(v_r12) == 0) goto loc_005F322E;
    result = (unsigned int)((*(unsigned __int8 *)(v_r13)) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))));
    v_r12 = (unsigned int)((v_r12) - 1);
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(result)));
    v_r13 = (v_r13) + 1;
    v_r14 = (unsigned int)((v_r14) + (8));
    goto loc_005F24F6;
loc_005F251D:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) >> (8));
    a1 = (unsigned int)(((unsigned __int8)(v_r15)) << (8));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) - (16));
    result = (unsigned int)((result) >> (1));
    result = (unsigned int)((result) + (16));
    result = (unsigned int)((result) >> (4));
    result = (unsigned int)((result) * ((unsigned int)(result)));
    if (((unsigned int)(a1)) == ((unsigned int)(result))) goto loc_005F2556;
loc_005F254C:
    goto loc_005F31C0;
loc_005F2556:
    result = (unsigned __int8)(((unsigned int)((unsigned int)(v_r15))) & (15));
    if (((unsigned __int8)(result)) == 8) goto loc_005F2568;
    goto loc_005F254C;
loc_005F2568:
    v_r14 = (unsigned int)((v_r14) + (-4));
    v_r15 = (unsigned int)((v_r15) >> (4));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (15));
    a1 = (unsigned int)((a1) + (8));
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 48));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 48))) == 0) {
        *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 48) = (unsigned int)(a1);
        result = (unsigned int)(a1);
    }
    if (((unsigned int)(a1)) > 15) goto loc_005F25E8;
    if (((unsigned int)(a1)) > ((unsigned int)(result))) goto loc_005F25E8;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 24) = 0;
    result = (unsigned int)((1) << ((unsigned __int8)(a1)));
    a3 = 0;
    a1 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 28) = (unsigned int)(result);
    a2 = 0;
    result = adler32_z(a1, a2, a3, v_stack_p38);
    v_r15 = (unsigned int)((v_r15) >> (8));
    v_r15 = (unsigned int)(~(v_r15));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 32) = (unsigned int)(result);
    v_r15 = (unsigned int)((v_r15) & (2));
    *(unsigned int *)(a1 + 76) = (unsigned int)(result);
    v_r15 = (unsigned int)((v_r15) | (0x3F3DULL));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = (unsigned int)(v_r15);
loc_005F25D6:
loc_005F25DA:
    goto loc_005F31CB;
loc_005F25E8:
    goto loc_005F254C;
loc_005F25F4:
    a1 = (unsigned int)((0) & ((unsigned int)(v_rip + 896753)));
    v_r15 = (unsigned int)((0) >> ((unsigned __int8)(a1)));
    v_r14 = (unsigned int)((0) - ((unsigned int)(a1)));
loc_005F25FF:
    if (((unsigned int)(v_r14)) >= 32) goto loc_005F2627;
    if ((unsigned int)(v_r12) == 0) goto loc_005F322E;
    result = (unsigned int)((*(unsigned __int8 *)(v_r13)) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))));
    v_r12 = (unsigned int)((v_r12) - 1);
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(result)));
    v_r13 = (v_r13) + 1;
    v_r14 = (unsigned int)((v_r14) + (8));
    goto loc_005F25FF;
loc_005F2627:
    result = (unsigned int)(~((unsigned int)((unsigned int)(v_r15))));
    result = (unsigned int)((result) >> (16));
    if (((unsigned int)((unsigned __int16)(v_r15))) == ((unsigned int)(result))) goto loc_005F2643;
    goto loc_005F31C0;
loc_005F2643:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 80) = (unsigned int)((unsigned __int16)(v_r15));
loc_005F264C:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F43ULL;
loc_005F2653:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 80))) == 0) goto loc_005F2B7E;
    v_rbp = (unsigned int)((unsigned int)(v_r12));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 80)))) <= ((unsigned int)(v_r12))) { v_rbp = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 80))); }
    if (((unsigned int)(v_rbp)) > ((unsigned int)((unsigned int)(v_stack_pA0)))) { v_rbp = (unsigned int)((unsigned int)(v_stack_pA0)); }
    if ((unsigned int)(v_rbp) == 0) goto loc_005F322E;
    result = memcpy(v_stack_p38, v_r13, (unsigned int)((unsigned int)(v_rbp)), v_stack_p38);
    v_r13 = (v_r13) + ((unsigned int)((unsigned int)(v_rbp)));
    v_r11 = (unsigned int)(((unsigned int)(v_stack_pA0)) - ((unsigned int)(v_rbp)));
    a4 = (v_stack_p38) + ((unsigned int)((unsigned int)(v_rbp)));
    v_r12 = (unsigned int)((v_r12) - ((unsigned int)(v_rbp)));
    v_stack_pA0 = (unsigned int)(v_r11);
    v_rbp = 0;
    v_stack_p38 = a4;
    goto loc_005F25D6;
loc_005F26BA:
    a1 = (unsigned int)((v_stack_p38) - (0x3F42ULL));
    if (condition_is_equal) goto loc_005F264C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_005F2653;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_005F26E3;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_005F2766;
    if (((unsigned int)(a1)) != 1) goto loc_005F2381;
    goto loc_005F2863;
loc_005F26E3:
    if (0 >= 14) goto loc_005F270B;
    if ((unsigned int)(v_r12) == 0) goto loc_005F322E;
    result = (unsigned int)((*(unsigned __int8 *)(v_r13)) << (0));
    v_r12 = (unsigned int)((v_r12) - 1);
    v_r15 = (unsigned int)((0) + ((unsigned int)(result)));
    v_r13 = (v_r13) + 1;
    v_r14 = (unsigned int)((0) + (8));
    goto loc_005F26E3;
loc_005F270B:
    v_r14 = (unsigned int)((v_r14) + (-14));
    v_r15 = (unsigned int)((v_r15) >> (5));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (31));
    a1 = (unsigned int)((a1) + (257));
    v_r15 = (unsigned int)((v_r15) >> (5));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (31));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 124) = (unsigned int)(a1);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (15));
    v_r15 = (unsigned int)((v_r15) >> (4));
    result = (unsigned int)((result) + (4));
    a2 = (unsigned int)((a2) + 1);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 128) = a2;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 120) = (unsigned int)(result);
    if (((unsigned int)(a1)) > 286) goto loc_005F2B72;
    if (a2 > 30) goto loc_005F2B72;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 132) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F45ULL;
loc_005F2766:
loc_005F2772:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 132)))) >= (*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 120))) goto loc_005F27EA;
loc_005F277D:
    if (((unsigned int)(v_r14)) >= 3) goto loc_005F27A5;
    if ((unsigned int)(v_r12) == 0) goto loc_005F322E;
    result = (unsigned int)((*(unsigned __int8 *)(v_r13)) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))));
    v_r12 = (unsigned int)((v_r12) - 1);
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(result)));
    v_r13 = (v_r13) + 1;
    v_r14 = (unsigned int)((v_r14) + (8));
    goto loc_005F277D;
loc_005F27A5:
    a1 = (unsigned __int16)(((unsigned __int16)(v_r15)) & (7));
    v_r15 = (unsigned int)((v_r15) >> (3));
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 40) + *(unsigned __int16 *)(v_rip - 6016098 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 132)) * 2) * 2 + 144) = (unsigned __int16)(a1);
    v_r14 = (unsigned int)((v_r14) + (-3));
    goto loc_005F2772;
loc_005F27CF:
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 40) + *(unsigned __int16 *)(v_rip - 6016098 + *(unsigned __int16 *)(v_rip - 6016098 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 132)) * 2) * 2) * 2 + 144) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 132))) + 1);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 132) = (unsigned int)(result);
loc_005F27EA:
    if (((unsigned int)(result)) < 19) goto loc_005F27CF;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 112) = 7;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 96) = *(unsigned __int64 *)(a1 + 40) + 1360;
    a1 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 136) = *(unsigned __int64 *)(a1 + 40) + 1360;
    v_stack_p28 = *(unsigned __int64 *)(a1 + 40) + 784;
    v_stack_p20 = *(unsigned __int64 *)(a1 + 40) + 112;
    result = inflate_table(a1, *(unsigned __int64 *)(a1 + 40) + 144, a1 + 19, *(unsigned __int64 *)(a1 + 40) + 136);
    v_stack_p98 = (unsigned int)(result);
    if ((unsigned int)(result) == 0) goto loc_005F2856;
loc_005F284D:
    goto loc_005F254C;
loc_005F2856:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 132) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F46ULL;
loc_005F2863:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 128))) + (*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 124)));
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 132)) >= ((unsigned int)(result))) goto loc_005F2A5C;
    a4 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 112)))));
    a4 = (unsigned int)((a4) - 1);
loc_005F288B:
    a1 = ((unsigned int)((unsigned int)(a4))) & ((unsigned int)((unsigned int)(v_r15)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 96) + a1 * 4))))) >> (8));
    v_stack_pA8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 96) + a1 * 4)));
    if (((unsigned int)((unsigned __int8)(result))) <= ((unsigned int)(v_r14))) goto loc_005F28CE;
    if ((unsigned int)(v_r12) == 0) goto loc_005F322E;
    result = (unsigned int)((*(unsigned __int8 *)(v_r13)) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))));
    v_r12 = (unsigned int)((v_r12) - 1);
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(result)));
    v_r13 = (v_r13) + 1;
    v_r14 = (unsigned int)((v_r14) + (8));
    goto loc_005F288B;
loc_005F28CE:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 96) + a1 * 4))) >> (16));
    if (((unsigned __int16)(a2)) >= 16) goto loc_005F28FA;
    v_r14 = (unsigned int)((v_r14) - ((unsigned int)((unsigned int)((unsigned int)(v_r14)))));
    v_r15 = (unsigned int)((v_r15) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))));
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 40) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 132)) * 2 + 144) = (unsigned __int16)(a2);
    goto loc_005F2863;
loc_005F28FA:
    if (condition_is_not_equal) goto loc_005F2966;
loc_005F2908:
    if (((unsigned int)(v_r14)) >= ((unsigned int)(v_stack_pA9 + 2))) goto loc_005F292F;
    if ((unsigned int)(v_r12) == 0) goto loc_005F322E;
    result = (unsigned int)((*(unsigned __int8 *)(v_r13)) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))));
    v_r12 = (unsigned int)((v_r12) - 1);
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(result)));
    v_r13 = (v_r13) + 1;
    v_r14 = (unsigned int)((v_r14) + (8));
    goto loc_005F2908;
loc_005F292F:
    v_r15 = (unsigned int)((v_r15) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_stack_pA9)))));
    v_r14 = (unsigned int)((v_r14) - ((unsigned int)(v_stack_pA9)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 132))) == 0) goto loc_005F2A4A;
    v_r14 = (unsigned int)((v_r14) + (-2));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (3));
    v_r15 = (unsigned int)((v_r15) >> (2));
    a2 = (unsigned int)((a2) + (3));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 132))) - 1);
    goto loc_005F2A0F;
loc_005F2966:
    if (v_stack_pAA != 17) goto loc_005F29C2;
loc_005F297E:
    if (((unsigned int)(v_r14)) >= ((unsigned int)(v_stack_pA9 + 3))) goto loc_005F29A5;
    if ((unsigned int)(v_r12) == 0) goto loc_005F322E;
    result = (unsigned int)((*(unsigned __int8 *)(v_r13)) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))));
    v_r12 = (unsigned int)((v_r12) - 1);
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(result)));
    v_r13 = (v_r13) + 1;
    v_r14 = (unsigned int)((v_r14) + (8));
    goto loc_005F297E;
loc_005F29A5:
    v_r15 = (unsigned int)((v_r15) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_stack_pA9)))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (7));
    a2 = (unsigned int)((a2) + (3));
    v_r15 = (unsigned int)((v_r15) >> (3));
    goto loc_005F2A09;
loc_005F29C2:
loc_005F29C6:
    if (((unsigned int)(v_r14)) >= ((unsigned int)(v_stack_pA9 + 7))) goto loc_005F29ED;
    if ((unsigned int)(v_r12) == 0) goto loc_005F322E;
    result = (unsigned int)((*(unsigned __int8 *)(v_r13)) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))));
    v_r12 = (unsigned int)((v_r12) - 1);
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(result)));
    v_r13 = (v_r13) + 1;
    v_r14 = (unsigned int)((v_r14) + (8));
    goto loc_005F29C6;
loc_005F29ED:
    v_r15 = (unsigned int)((v_r15) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_stack_pA9)))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (127));
    a2 = (unsigned int)((a2) + (11));
    v_r15 = (unsigned int)((v_r15) >> (7));
loc_005F2A09:
    a1 = (unsigned int)(((unsigned int)(0xFFFFFFF9ULL)) - ((unsigned int)(v_stack_pA9)));
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(a1)));
loc_005F2A0F:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 128))) + (*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 124)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 132)) + a2 * 1)) > ((unsigned int)(result))) goto loc_005F2A4A;
loc_005F2A27:
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 40) + (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 132)))) * 2 + 144) = 0;
    a2 = (unsigned int)((a2) + (-1));
    if (condition_is_not_equal) goto loc_005F2A27;
    goto loc_005F2863;
loc_005F2A4A:
    *(unsigned __int64 *)(a1 + 32) = v_rip + 895791;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F51ULL;
loc_005F2A5C:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8)) == 0x3F51ULL) goto loc_005F2332;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 40) + 656)) != 0) goto loc_005F2A93;
    goto loc_005F31C0;
loc_005F2A93:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 96) = *(unsigned __int64 *)(a1 + 40) + 1360;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 136) = *(unsigned __int64 *)(a1 + 40) + 1360;
    v_stack_p28 = *(unsigned __int64 *)(a1 + 40) + 784;
    v_stack_p20 = *(unsigned __int64 *)(a1 + 40) + 112;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 112) = 10;
    result = inflate_table(1, *(unsigned __int64 *)(a1 + 40) + 144, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 124)), *(unsigned __int64 *)(a1 + 40) + 136);
    v_stack_p98 = (unsigned int)(result);
    if ((unsigned int)(result) == 0) goto loc_005F2B0A;
    v_rbp = 0;
    goto loc_005F254C;
loc_005F2B0A:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 104) = *(unsigned __int64 *)((unsigned int)(v_stack_p30));
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 124))) + (72);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 116) = 9;
    v_stack_p28 = 0;
    v_stack_p20 = *(unsigned __int64 *)(a1 + 40) + 116;
    result = inflate_table(2, *(unsigned __int64 *)(a1 + 40) + result * 2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 128)), (unsigned int)(v_stack_p30));
    v_rbp = 0;
    v_stack_p98 = (unsigned int)(result);
    if ((unsigned int)(result) == 0) goto loc_005F2B8A;
    goto loc_005F284D;
loc_005F2B72:
    goto loc_005F254C;
loc_005F2B7E:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F3FULL;
    goto loc_005F31CB;
loc_005F2B8A:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F48ULL;
loc_005F2B91:
    if (((unsigned int)(v_r12)) < 15) goto loc_005F2C65;
    if (((unsigned int)((unsigned int)(v_stack_pA0))) < 260) goto loc_005F2C65;
    *(unsigned int *)(a1 + 24) = (unsigned int)((unsigned int)(v_stack_pA0));
    *(unsigned __int64 *)(a1) = v_r13;
    *(unsigned int *)(a1 + 8) = (unsigned int)(v_r12);
    *(unsigned __int64 *)(v_stack_p40) = v_stack_p38;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 72) = (unsigned int)(v_r15);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 76) = (unsigned int)(v_r14);
    result = inflate_fast_chunk_(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p30))), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 128)), v_stack_p38);
    v_stack_p38 = *(unsigned __int64 *)(v_stack_p40);
    v_stack_pA0 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)));
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8)) != 0x3F3FULL) goto loc_005F2332;
    goto loc_005F232A;
loc_005F2C1E:
    if (((unsigned int)(a1)) > 0x3F4DULL) goto loc_005F311F;
    if (((unsigned int)(a1)) == 0x3F4DULL) goto loc_005F30F1;
    a1 = (unsigned int)((a1) - (0x3F48ULL));
    if (condition_is_equal) goto loc_005F2B91;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_005F2DCA;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_005F2E26;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_005F2F4A;
    if (((unsigned int)(a1)) != 1) goto loc_005F2381;
    goto loc_005F2FA2;
loc_005F2C65:
    a3 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 112)))));
    a3 = (unsigned int)((a3) - 1);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 9060) = 0;
loc_005F2C7E:
    a1 = ((unsigned int)((unsigned int)(a3))) & ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 72)))));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 96) + a1 * 4))))) >> (8));
    v_stack_pA8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 96) + a1 * 4)));
    if (((unsigned int)((unsigned __int8)(a1))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 76))))) goto loc_005F2CC0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8))) == 0) goto loc_005F322E;
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1))) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 76)))))));
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8))) - 1);
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 72))) + ((unsigned int)(result)));
    v_r13 = (*(unsigned __int64 *)(a1)) + 1;
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 76))) + (8));
    goto loc_005F2C7E;
loc_005F2CC0:
    if ((unsigned __int8)(result) == 0) goto loc_005F2D4A;
    if ((((unsigned __int8)(result)) & (240)) != 0) goto loc_005F2D4A;
    a1 = (unsigned int)(((unsigned __int8)(result)) + ((unsigned int)(v_stack_pA9)));
    a4 = (unsigned int)((1) << ((unsigned __int8)(a1)));
loc_005F2CF1:
    result = (unsigned int)((a4 - 1) & ((unsigned int)(v_r15)));
    result = (unsigned int)((result) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_stack_pA9)))));
    result = (unsigned int)((result) + ((unsigned int)(v_stack_pAA)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 96) + result * 4))))) >> (8));
    a2 = (unsigned int)(((unsigned __int8)(a1)) + ((unsigned int)(v_stack_pA9)));
    if (a2 <= ((unsigned int)(v_r14))) goto loc_005F2D36;
    if ((unsigned int)(v_r12) == 0) goto loc_005F322E;
    result = (unsigned int)((*(unsigned __int8 *)(v_r13)) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))));
    v_r12 = (unsigned int)((v_r12) - 1);
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(result)));
    v_r13 = (v_r13) + 1;
    v_r14 = (unsigned int)((v_r14) + (8));
    goto loc_005F2CF1;
loc_005F2D36:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 9060) = (unsigned int)(v_stack_pA9);
    v_r15 = (unsigned int)((v_r15) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_stack_pA9)))));
    v_r14 = (unsigned int)((v_r14) - ((unsigned int)(v_stack_pA9)));
loc_005F2D4A:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (8));
    v_r15 = (unsigned int)((v_r15) >> ((unsigned __int8)((unsigned int)((unsigned int)((unsigned __int8)(a1))))));
    v_r14 = (unsigned int)((v_r14) - ((unsigned int)((unsigned __int8)(a1))));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (16));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 80) = (unsigned int)(a1);
    if ((unsigned __int8)(result) != 0) goto loc_005F2D85;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F4DULL;
loc_005F2D73:
    goto loc_005F25DA;
loc_005F2D85:
    if ((((unsigned __int8)(result)) & (32)) == 0) goto loc_005F2D99;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F3FULL;
    goto loc_005F2D73;
loc_005F2D99:
    if ((((unsigned __int8)(result)) & (64)) == 0) goto loc_005F2DBA;
    goto loc_005F254C;
loc_005F2DBA:
    a1 = (unsigned int)(((unsigned __int8)(v_rip + 894803)) & (15));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F49ULL;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 88) = (unsigned int)(a1);
loc_005F2DCA:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 88))) == 0) goto loc_005F2E16;
loc_005F2DD1:
    if (((unsigned int)(v_r14)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 88))))) goto loc_005F2DF8;
    if ((unsigned int)(v_r12) == 0) goto loc_005F322E;
    result = (unsigned int)((*(unsigned __int8 *)(v_r13)) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))));
    v_r12 = (unsigned int)((v_r12) - 1);
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(result)));
    v_r13 = (v_r13) + 1;
    v_r14 = (unsigned int)((v_r14) + (8));
    goto loc_005F2DD1;
loc_005F2DF8:
    result = (unsigned int)((1) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 88)))));
    v_r14 = (unsigned int)((v_r14) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 88)))));
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) & ((unsigned int)(v_r15)));
    v_r15 = (unsigned int)((v_r15) >> ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 88)))));
loc_005F2E16:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 9064) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 80)));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F4AULL;
loc_005F2E26:
    a3 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 116)))));
    a3 = (unsigned int)((a3) - 1);
loc_005F2E39:
    a1 = ((unsigned int)((unsigned int)(a3))) & ((unsigned int)((unsigned int)(v_r15)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 104) + a1 * 4))))) >> (8));
    v_stack_pA8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 104) + a1 * 4)));
    if (((unsigned int)((unsigned __int8)(a1))) <= ((unsigned int)(v_r14))) goto loc_005F2E7B;
    if ((unsigned int)(v_r12) == 0) goto loc_005F322E;
    result = (unsigned int)((*(unsigned __int8 *)(v_r13)) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))));
    v_r12 = (unsigned int)((v_r12) - 1);
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(result)));
    v_r13 = (v_r13) + 1;
    v_r14 = (unsigned int)((v_r14) + (8));
    goto loc_005F2E39;
loc_005F2E7B:
    if ((((unsigned __int8)(result)) & (240)) != 0) goto loc_005F2EF9;
    a1 = (unsigned int)(((unsigned __int8)(result)) + ((unsigned int)(v_stack_pA9)));
    a4 = (unsigned int)((1) << ((unsigned __int8)(a1)));
loc_005F2EA4:
    result = (unsigned int)((a4 - 1) & ((unsigned int)(v_r15)));
    result = (unsigned int)((result) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_stack_pA9)))));
    result = (unsigned int)((result) + ((unsigned int)(v_stack_pAA)));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 104) + result * 4))))) >> (8));
    a2 = (unsigned int)(((unsigned __int8)(a1)) + ((unsigned int)(v_stack_pA9)));
    if (a2 <= ((unsigned int)(v_r14))) goto loc_005F2EE9;
    if ((unsigned int)(v_r12) == 0) goto loc_005F322E;
    result = (unsigned int)((*(unsigned __int8 *)(v_r13)) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))));
    v_r12 = (unsigned int)((v_r12) - 1);
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(result)));
    v_r13 = (v_r13) + 1;
    v_r14 = (unsigned int)((v_r14) + (8));
    goto loc_005F2EA4;
loc_005F2EE9:
    v_r14 = (unsigned int)((v_r14) - ((unsigned int)(v_stack_pA9)));
    v_r15 = (unsigned int)((v_r15) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_stack_pA9)))));
loc_005F2EF9:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) >> (8));
    v_r14 = (unsigned int)((v_r14) - ((unsigned int)((unsigned __int8)(a1))));
    v_r15 = (unsigned int)((v_r15) >> ((unsigned __int8)((unsigned __int8)(a1))));
    if ((((unsigned __int8)(result)) & (64)) == 0) goto loc_005F2F32;
    goto loc_005F254C;
loc_005F2F32:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F4BULL;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rip + 894451))) >> (16));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 84) = (unsigned int)(a1);
    a1 = (unsigned int)(((unsigned __int8)(v_rip + 894451)) & (15));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 88) = (unsigned int)(a1);
loc_005F2F4A:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 88))) == 0) goto loc_005F2F96;
loc_005F2F51:
    if (((unsigned int)(v_r14)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 88))))) goto loc_005F2F78;
    if ((unsigned int)(v_r12) == 0) goto loc_005F322E;
    result = (unsigned int)((*(unsigned __int8 *)(v_r13)) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))));
    v_r12 = (unsigned int)((v_r12) - 1);
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(result)));
    v_r13 = (v_r13) + 1;
    v_r14 = (unsigned int)((v_r14) + (8));
    goto loc_005F2F51;
loc_005F2F78:
    result = (unsigned int)((1) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 88)))));
    v_r14 = (unsigned int)((v_r14) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 88)))));
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) & ((unsigned int)(v_r15)));
    v_r15 = (unsigned int)((v_r15) >> ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 88)))));
loc_005F2F96:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F4CULL;
loc_005F2FA2:
    if ((unsigned int)((unsigned int)(v_stack_pA0)) == 0) goto loc_005F322E;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p30)))) - ((unsigned int)((unsigned int)(v_stack_pA0))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 84)))) <= ((unsigned int)(result))) goto loc_005F3059;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 84))) - ((unsigned int)(result)));
    if (((unsigned int)(a1)) <= (*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 56))) goto loc_005F2FD6;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 9056)) == 0) goto loc_005F2FD6;
    goto loc_005F31C0;
loc_005F2FD6:
    if (((unsigned int)(a1)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 60))))) goto loc_005F2FEA;
    a1 = (unsigned int)((a1) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 60)))));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 52))) - ((unsigned int)(a1)));
    goto loc_005F2FEE;
loc_005F2FEA:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 60))) - ((unsigned int)(a1)));
loc_005F2FEE:
    a2 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 64));
    v_r10 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 80));
    if (((unsigned int)(a1)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 80))))) { v_r10 = (unsigned int)(a1); }
    if (((unsigned int)(v_r10)) > ((unsigned int)((unsigned int)(v_stack_pA0)))) { v_r10 = (unsigned int)((unsigned int)(v_stack_pA0)); }
    if (((unsigned int)((unsigned int)(v_stack_pA0))) >= 16) goto loc_005F30AB;
    if ((((unsigned __int8)(v_r10)) & (8)) != 0) {
        result = *(unsigned __int64 *)(a2);
        *(unsigned __int64 *)(v_stack_p38) = result;
        a4 = (v_stack_p38) + (8);
        a2 = (a2) + (8);
    }
    if ((((unsigned __int8)(v_r10)) & (4)) != 0) {
        result = *(unsigned int *)(a2);
        *(unsigned int *)(a4) = (unsigned int)(result);
        a4 = (a4) + (4);
        a2 = (a2) + (4);
    }
    if ((((unsigned __int8)(v_r10)) & (2)) != 0) {
        result = *(unsigned __int16 *)(a2);
        *(unsigned __int16 *)(a4) = (unsigned __int16)(result);
        a4 = (a4) + (2);
        a2 = (a2) + (2);
    }
    if ((((unsigned __int8)(v_r10)) & (1)) == 0) goto loc_005F3085;
    *(unsigned __int8 *)(a4) = (unsigned __int8)(*(unsigned __int8 *)(a2));
    a4 = (a4) + 1;
    goto loc_005F3085;
loc_005F3059:
    v_r10 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 80));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 80)))) > ((unsigned int)((unsigned int)(v_stack_pA0)))) { v_r10 = (unsigned int)((unsigned int)(v_stack_pA0)); }
    if (((unsigned int)((unsigned int)(v_stack_pA0))) >= 48) goto loc_005F308C;
    if ((unsigned int)(v_r10) == 0) goto loc_005F3085;
loc_005F3072:
    result = (a4) - (a1);
    *(unsigned __int8 *)(a4) = (unsigned __int8)(*(unsigned __int8 *)(result));
    a4 = (a4) + 1;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) + (-1));
    if (condition_is_not_equal) goto loc_005F3072;
loc_005F3085:
    v_stack_p38 = a4;
    goto loc_005F30BB;
loc_005F308C:
    if (((unsigned int)(a1)) >= ((unsigned int)(v_r10))) goto loc_005F30A5;
    if (((unsigned int)(a1)) >= 16) goto loc_005F30A5;
    result = chunkset_core(a4, (unsigned int)((unsigned int)(a1)), (unsigned int)((unsigned int)(v_r10)), a4);
    goto loc_005F30B6;
loc_005F30A5:
    a2 = (a4) - (a4);
loc_005F30AB:
    result = chunkcopy_core(a4, a2, (unsigned int)((unsigned int)(v_r10)), a4);
loc_005F30B6:
    v_stack_p38 = result;
loc_005F30BB:
    v_r11 = (unsigned int)(((unsigned int)(v_stack_pA0)) - ((unsigned int)(v_r10)));
    v_stack_pA0 = (unsigned int)(v_r11);
    if (condition_is_not_equal) goto loc_005F2332;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F48ULL;
    goto loc_005F232A;
loc_005F30F1:
    if ((unsigned int)(v_r11) == 0) goto loc_005F322E;
    *(unsigned __int8 *)(v_stack_p38) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 40) + 80));
    a4 = (v_stack_p38) + 1;
    v_r11 = (unsigned int)((v_r11) - 1);
    v_stack_p38 = a4;
    v_stack_pA0 = (unsigned int)(v_r11);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F48ULL;
    goto loc_005F31CB;
loc_005F311F:
    a1 = (unsigned int)((a4) - (0x3F4EULL));
    if (condition_is_not_equal) goto loc_005F320A;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 16)) == 0) goto loc_005F31FC;
loc_005F3134:
    if (((unsigned int)(v_r14)) >= 32) goto loc_005F315C;
    if ((unsigned int)(v_r12) == 0) goto loc_005F322E;
    result = (unsigned int)((*(unsigned __int8 *)(v_r13)) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))));
    v_r12 = (unsigned int)((v_r12) - 1);
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(result)));
    v_r13 = (v_r13) + 1;
    v_r14 = (unsigned int)((v_r14) + (8));
    goto loc_005F3134;
loc_005F315C:
    v_rbx = (unsigned int)(((unsigned int)(v_stack_p30)) - ((unsigned int)(v_r11)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 16)))) & (4)) == 0) goto loc_005F31A1;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 16));
    v_r10 = *(unsigned __int64 *)(a1 + 40) + 112;
    if ((unsigned int)(v_rbx) != 0) {
        a1 = *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 32);
        a2 = a4;
        a3 = (unsigned int)(v_rbx);
        a2 = (a2) - (a3);
        result = adler32_z(a1, a2, a3, a4);
        a4 = v_stack_p38;
        v_r10 = *(unsigned __int64 *)(a1 + 40) + 112;
        v_r11 = v_stack_pA0;
        a3 = *(unsigned __int64 *)(a1 + 40) + 116;
        *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 32) = (unsigned int)(result);
        a2 = 16;
        *(unsigned int *)(a1 + 76) = (unsigned int)(result);
    }
    v_stack_p30 = (unsigned int)((unsigned int)((unsigned int)(v_r11)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 16)))) & (4)) == 0) goto loc_005F31F6;
    if (((unsigned int)((unsigned int)((unsigned int)(v_r15)))) == (*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 32))) goto loc_005F31F6;
loc_005F31C0:
    *(unsigned __int64 *)(a1 + 32) = v_rip + 893856;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F51ULL;
loc_005F31CB:
    goto loc_005F2332;
loc_005F31D5:
    *(unsigned __int64 *)(a1 + 16) = a4;
    *(unsigned int *)(a1 + 24) = (unsigned int)(v_r11);
    *(unsigned __int64 *)(a1) = v_r13;
    *(unsigned int *)(a1 + 8) = (unsigned int)(v_r12);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 72) = (unsigned int)(v_r15);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 76) = (unsigned int)(v_r14);
    goto loc_005F2386;
loc_005F31F6:
loc_005F31FC:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F50ULL;
loc_005F3203:
    goto loc_005F3235;
loc_005F320A:
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_005F3203;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_005F3227;
    if (((unsigned int)(a1)) != 1) goto loc_005F2381;
loc_005F321D:
    goto loc_005F2386;
loc_005F3227:
    goto loc_005F3235;
loc_005F322E:
loc_005F3235:
    *(unsigned __int64 *)(a1 + 16) = v_stack_p38;
    *(unsigned int *)(a1 + 24) = (unsigned int)((unsigned int)(v_stack_pA0));
    *(unsigned __int64 *)(a1) = v_r13;
    *(unsigned int *)(a1 + 8) = (unsigned int)(v_r12);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 76) = 0;
    v_r14 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 72) = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 52)) != 0) goto loc_005F326E;
    if (((unsigned int)((unsigned int)((unsigned int)(v_r11)))) == (*(unsigned int *)(a1 + 24))) goto loc_005F328E;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8)) > 0x3F4DULL) goto loc_005F328E;
loc_005F326E:
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r11))))) - (*(unsigned int *)(a1 + 24)));
    result = updatewindow(a1, *(unsigned __int64 *)(a1 + 16), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_005F328E;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F52ULL;
    goto loc_005F321D;
loc_005F328E:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_r11))) - (*(unsigned int *)(a1 + 24)));
    result = (unsigned int)(((unsigned int)(v_stack_p34)) - (*(unsigned int *)(a1 + 8)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 16)))) & (4)) == 0) goto loc_005F32C4;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 16));
    if ((unsigned int)(v_rbx) != 0) {
        a2 = *(unsigned __int64 *)(a1 + 16);
        a1 = *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 32);
        a3 = (unsigned int)(v_rbx);
        a2 = (a2) - (a3);
        result = adler32_z(a1, a2, a3, a4);
        *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 32) = (unsigned int)(result);
        *(unsigned int *)(a1 + 76) = (unsigned int)(result);
    }
    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 12))));
    a2 = (unsigned int)((a2) & (64));
    a3 = 128;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8)))) != 0x3F3FULL) { a3 = 0; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8)))) == 0x3F47ULL) goto loc_005F32F1;
    result = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8)))) == 0x3F42ULL) {
        result = 256;
    }
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 76))) + ((unsigned int)(a3)));
    a1 = (unsigned int)((a1) + (a2));
    a1 = (unsigned int)((a1) + ((unsigned int)(result)));
    *(unsigned int *)(a1 + 72) = (unsigned int)(a1);
    v_rbp = (unsigned int)(v_stack_p98);
    if ((unsigned int)((unsigned int)(v_stack_p98)) == 0) { v_rbp = (unsigned int)((unsigned int)(0xFFFFFFFBULL)); }
    goto loc_005F2386;
}
```

## 5. (Beta) C Style

```c
int64_t inflate(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p8;
    uint32_t v_stack_p98;
    uint32_t v_stack_pA0;
    uint32_t v_stack_pA8;
    uint8_t v_stack_pA9;
    uint16_t v_stack_pAA;

    v_stack_p8 = local_rbx;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (80);
    result = inflateStateCheck(Arg1, Arg2, a3, a4);
    local_rbp = 0;
    if ((uint32_t)(result) != 0) goto loc_005F2381;
    if ((*(uint64_t *)(arg1 + 0x10)) == 0) goto loc_005F2381;
    if ((*(uint64_t *)(arg1)) != 0) goto loc_005F22CB;
    if ((*(uint32_t *)(arg1 + 0x8)) != 0) goto loc_005F2381;
    Arg1 = (Arg1) + (16);
    goto loc_005F22CE;
loc_005F22CB:
loc_005F22CE:
    v_stack_m48 = Arg1 + 16;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8)) == 0x3F3FULL) {
        *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F40ULL;
        v_stack_m48 = Arg1 + 16;
    }
    v_stack_m50 = *(uint64_t *)(arg1 + 0x10);
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)));
    v_stack_m54 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    v_stack_m58 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    v_stack_p10 = 0;
loc_005F232A:
loc_005F2332:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8)))) > 0x3F47ULL) goto loc_005F2C1E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8)))) == 0x3F47ULL) goto loc_005F2B8A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8)))) > 0x3F41ULL) goto loc_005F26BA;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8)))) == 0x3F41ULL) goto loc_005F25F4;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8))) - (0x3F34ULL));
    if (condition_is_equal) goto loc_005F24E5;
    Arg1 = (uint32_t)((Arg1) - (9));
    if (condition_is_equal) goto loc_005F239F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_005F23DF;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_005F241B;
    if (((uint32_t)(Arg1)) == 1) goto loc_005F241B;
loc_005F2381:
loc_005F2386:
    local_rsp = (local_rsp) + (80);
    return (uint32_t)(0xFFFFFFFEULL);
loc_005F239F:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x4C)))) >= 32) goto loc_005F23C7;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8))) == 0) goto loc_005F322E;
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(arg1))) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x4C)))))));
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8))) - 1);
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x48))) + ((uint32_t)(result)));
    local_r13 = (*(uint64_t *)(arg1)) + 1;
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x4C))) + (8));
    goto loc_005F239F;
loc_005F23C7:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x20) = (uint32_t)(local_r15);
    *(uint32_t *)(arg1 + 0x4C) = (uint32_t)(local_r15);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F3EULL;
loc_005F23DF:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x14)) == 0) goto loc_005F31D5;
    a3 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = adler32_z(Arg1, Arg2, a3, *(uint64_t *)(arg1 + 0x10));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x20) = (uint32_t)(result);
    *(uint32_t *)(arg1 + 0x4C) = (uint32_t)(result);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F3FULL;
loc_005F241B:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0xC)) == 0) goto loc_005F243C;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F4EULL;
    Arg1 = (uint32_t)((0) & (7));
    local_r15 = (uint32_t)((0) >> ((uint8_t)(Arg1)));
    local_r14 = (uint32_t)((0) - ((uint32_t)(Arg1)));
    goto loc_005F2332;
loc_005F243C:
    if (((uint32_t)(local_r14)) >= 3) goto loc_005F2464;
    if ((uint32_t)(local_r12) == 0) goto loc_005F322E;
    result = (uint32_t)((*(uint8_t *)(local_r13)) << ((uint8_t)((uint32_t)((uint32_t)(local_r14)))));
    local_r12 = (uint32_t)((local_r12) - 1);
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(result)));
    local_r13 = (local_r13) + 1;
    local_r14 = (uint32_t)((local_r14) + (8));
    goto loc_005F243C;
loc_005F2464:
    local_r15 = (uint32_t)((local_r15) >> (1));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (1));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0xC) = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (3));
    if (condition_is_equal) goto loc_005F24D1;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_005F24A4;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_005F249B;
    if (((uint32_t)(result)) != 1) goto loc_005F24D8;
    *(uint64_t *)(arg1 + 0x20) = v_rip + 896898;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F51ULL;
    goto loc_005F24D8;
loc_005F249B:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F44ULL;
    goto loc_005F24D8;
loc_005F24A4:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x70) = 9;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x60) = v_rip - 6015339;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x68) = v_rip - 6015533;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x74) = 5;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F47ULL;
    goto loc_005F24D8;
loc_005F24D1:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F41ULL;
loc_005F24D8:
    local_r15 = (uint32_t)((local_r15) >> (2));
    local_r14 = (uint32_t)((local_r14) + (-3));
    goto loc_005F31CB;
loc_005F24E5:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x10)) != 0) goto loc_005F24F6;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F40ULL;
    goto loc_005F31CB;
loc_005F24F6:
    if (((uint32_t)(local_r14)) >= 16) goto loc_005F251D;
    if ((uint32_t)(local_r12) == 0) goto loc_005F322E;
    result = (uint32_t)((*(uint8_t *)(local_r13)) << ((uint8_t)((uint32_t)((uint32_t)(local_r14)))));
    local_r12 = (uint32_t)((local_r12) - 1);
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(result)));
    local_r13 = (local_r13) + 1;
    local_r14 = (uint32_t)((local_r14) + (8));
    goto loc_005F24F6;
loc_005F251D:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) >> (8));
    Arg1 = (uint32_t)(((uint8_t)(local_r15)) << (8));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) - (16));
    result = (uint32_t)((result) >> (1));
    result = (uint32_t)((result) + (16));
    result = (uint32_t)((result) >> (4));
    result = (uint32_t)((result) * ((uint32_t)(result)));
    if (((uint32_t)(Arg1)) == ((uint32_t)(result))) goto loc_005F2556;
loc_005F254C:
    goto loc_005F31C0;
loc_005F2556:
    result = (uint8_t)(((uint32_t)((uint32_t)(local_r15))) & (15));
    if (((uint8_t)(result)) == 8) goto loc_005F2568;
    goto loc_005F254C;
loc_005F2568:
    local_r14 = (uint32_t)((local_r14) + (-4));
    local_r15 = (uint32_t)((local_r15) >> (4));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (15));
    Arg1 = (uint32_t)((Arg1) + (8));
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x30));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x30))) == 0) {
        *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x30) = (uint32_t)(Arg1);
        result = (uint32_t)(Arg1);
    }
    if (((uint32_t)(Arg1)) > 15) goto loc_005F25E8;
    if (((uint32_t)(Arg1)) > ((uint32_t)(result))) goto loc_005F25E8;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x18) = 0;
    result = (uint32_t)((1) << ((uint8_t)(Arg1)));
    a3 = 0;
    Arg1 = 0;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x1C) = (uint32_t)(result);
    Arg2 = 0;
    result = adler32_z(Arg1, Arg2, a3, v_stack_p38);
    local_r15 = (uint32_t)((local_r15) >> (8));
    local_r15 = (uint32_t)(~(local_r15));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x20) = (uint32_t)(result);
    local_r15 = (uint32_t)((local_r15) & (2));
    *(uint32_t *)(arg1 + 0x4C) = (uint32_t)(result);
    local_r15 = (uint32_t)((local_r15) | (0x3F3DULL));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = (uint32_t)(local_r15);
loc_005F25D6:
loc_005F25DA:
    goto loc_005F31CB;
loc_005F25E8:
    goto loc_005F254C;
loc_005F25F4:
    Arg1 = (uint32_t)((0) & ((uint32_t)(v_rip + 896753)));
    local_r15 = (uint32_t)((0) >> ((uint8_t)(Arg1)));
    local_r14 = (uint32_t)((0) - ((uint32_t)(Arg1)));
loc_005F25FF:
    if (((uint32_t)(local_r14)) >= 32) goto loc_005F2627;
    if ((uint32_t)(local_r12) == 0) goto loc_005F322E;
    result = (uint32_t)((*(uint8_t *)(local_r13)) << ((uint8_t)((uint32_t)((uint32_t)(local_r14)))));
    local_r12 = (uint32_t)((local_r12) - 1);
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(result)));
    local_r13 = (local_r13) + 1;
    local_r14 = (uint32_t)((local_r14) + (8));
    goto loc_005F25FF;
loc_005F2627:
    result = (uint32_t)(~((uint32_t)((uint32_t)(local_r15))));
    result = (uint32_t)((result) >> (16));
    if (((uint32_t)((uint16_t)(local_r15))) == ((uint32_t)(result))) goto loc_005F2643;
    goto loc_005F31C0;
loc_005F2643:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x50) = (uint32_t)((uint16_t)(local_r15));
loc_005F264C:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F43ULL;
loc_005F2653:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x50))) == 0) goto loc_005F2B7E;
    local_rbp = (uint32_t)((uint32_t)(local_r12));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x50)))) <= ((uint32_t)(local_r12))) { local_rbp = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x50))); }
    if (((uint32_t)(local_rbp)) > ((uint32_t)((uint32_t)(v_stack_pA0)))) { local_rbp = (uint32_t)((uint32_t)(v_stack_pA0)); }
    if ((uint32_t)(local_rbp) == 0) goto loc_005F322E;
    result = memcpy(v_stack_p38, local_r13, (uint32_t)((uint32_t)(local_rbp)), v_stack_p38);
    local_r13 = (local_r13) + ((uint32_t)((uint32_t)(local_rbp)));
    local_r11 = (uint32_t)(((uint32_t)(v_stack_pA0)) - ((uint32_t)(local_rbp)));
    a4 = (v_stack_p38) + ((uint32_t)((uint32_t)(local_rbp)));
    local_r12 = (uint32_t)((local_r12) - ((uint32_t)(local_rbp)));
    v_stack_pA0 = (uint32_t)(local_r11);
    local_rbp = 0;
    v_stack_p38 = a4;
    goto loc_005F25D6;
loc_005F26BA:
    Arg1 = (uint32_t)((v_stack_p38) - (0x3F42ULL));
    if (condition_is_equal) goto loc_005F264C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_005F2653;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_005F26E3;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_005F2766;
    if (((uint32_t)(Arg1)) != 1) goto loc_005F2381;
    goto loc_005F2863;
loc_005F26E3:
    if (0 >= 14) goto loc_005F270B;
    if ((uint32_t)(local_r12) == 0) goto loc_005F322E;
    result = (uint32_t)((*(uint8_t *)(local_r13)) << (0));
    local_r12 = (uint32_t)((local_r12) - 1);
    local_r15 = (uint32_t)((0) + ((uint32_t)(result)));
    local_r13 = (local_r13) + 1;
    local_r14 = (uint32_t)((0) + (8));
    goto loc_005F26E3;
loc_005F270B:
    local_r14 = (uint32_t)((local_r14) + (-14));
    local_r15 = (uint32_t)((local_r15) >> (5));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (31));
    Arg1 = (uint32_t)((Arg1) + (257));
    local_r15 = (uint32_t)((local_r15) >> (5));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (31));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x7C) = (uint32_t)(Arg1);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (15));
    local_r15 = (uint32_t)((local_r15) >> (4));
    result = (uint32_t)((result) + (4));
    Arg2 = (uint32_t)((Arg2) + 1);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x80) = Arg2;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x78) = (uint32_t)(result);
    if (((uint32_t)(Arg1)) > 286) goto loc_005F2B72;
    if (Arg2 > 30) goto loc_005F2B72;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x84) = 0;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F45ULL;
loc_005F2766:
loc_005F2772:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x84)))) >= (*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x78))) goto loc_005F27EA;
loc_005F277D:
    if (((uint32_t)(local_r14)) >= 3) goto loc_005F27A5;
    if ((uint32_t)(local_r12) == 0) goto loc_005F322E;
    result = (uint32_t)((*(uint8_t *)(local_r13)) << ((uint8_t)((uint32_t)((uint32_t)(local_r14)))));
    local_r12 = (uint32_t)((local_r12) - 1);
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(result)));
    local_r13 = (local_r13) + 1;
    local_r14 = (uint32_t)((local_r14) + (8));
    goto loc_005F277D;
loc_005F27A5:
    Arg1 = (uint16_t)(((uint16_t)(local_r15)) & (7));
    local_r15 = (uint32_t)((local_r15) >> (3));
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x28) + *(uint16_t *)(v_rip - 0x5BCC62 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x84)) * 2) * 2 + 0x90) = (uint16_t)(Arg1);
    local_r14 = (uint32_t)((local_r14) + (-3));
    goto loc_005F2772;
loc_005F27CF:
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x28) + *(uint16_t *)(v_rip - 0x5BCC62 + *(uint16_t *)(v_rip - 0x5BCC62 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x84)) * 2) * 2) * 2 + 0x90) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x84))) + 1);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x84) = (uint32_t)(result);
loc_005F27EA:
    if (((uint32_t)(result)) < 19) goto loc_005F27CF;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x70) = 7;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x60) = *(uint64_t *)(arg1 + 0x28) + 1360;
    Arg1 = 0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x88) = *(uint64_t *)(arg1 + 0x28) + 1360;
    v_stack_p28 = *(uint64_t *)(arg1 + 0x28) + 784;
    v_stack_p20 = *(uint64_t *)(arg1 + 0x28) + 112;
    result = inflate_table(Arg1, *(uint64_t *)(arg1 + 0x28) + 144, Arg1 + 19, *(uint64_t *)(arg1 + 0x28) + 136);
    v_stack_p98 = (uint32_t)(result);
    if ((uint32_t)(result) == 0) goto loc_005F2856;
loc_005F284D:
    goto loc_005F254C;
loc_005F2856:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x84) = 0;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F46ULL;
loc_005F2863:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x80))) + (*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x7C)));
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x84)) >= ((uint32_t)(result))) goto loc_005F2A5C;
    a4 = (uint32_t)((1) << ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x70)))));
    a4 = (uint32_t)((a4) - 1);
loc_005F288B:
    Arg1 = ((uint32_t)((uint32_t)(a4))) & ((uint32_t)((uint32_t)(local_r15)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x60) + arg1 * 4))))) >> (8));
    v_stack_pA8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x60) + arg1 * 4)));
    if (((uint32_t)((uint8_t)(result))) <= ((uint32_t)(local_r14))) goto loc_005F28CE;
    if ((uint32_t)(local_r12) == 0) goto loc_005F322E;
    result = (uint32_t)((*(uint8_t *)(local_r13)) << ((uint8_t)((uint32_t)((uint32_t)(local_r14)))));
    local_r12 = (uint32_t)((local_r12) - 1);
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(result)));
    local_r13 = (local_r13) + 1;
    local_r14 = (uint32_t)((local_r14) + (8));
    goto loc_005F288B;
loc_005F28CE:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x60) + arg1 * 4))) >> (16));
    if (((uint16_t)(Arg2)) >= 16) goto loc_005F28FA;
    local_r14 = (uint32_t)((local_r14) - ((uint32_t)((uint32_t)((uint32_t)(local_r14)))));
    local_r15 = (uint32_t)((local_r15) >> ((uint8_t)((uint32_t)((uint32_t)(local_r14)))));
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x28) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x84)) * 2 + 0x90) = (uint16_t)(Arg2);
    goto loc_005F2863;
loc_005F28FA:
    if (condition_is_not_equal) goto loc_005F2966;
loc_005F2908:
    if (((uint32_t)(local_r14)) >= ((uint32_t)(v_stack_pA9 + 2))) goto loc_005F292F;
    if ((uint32_t)(local_r12) == 0) goto loc_005F322E;
    result = (uint32_t)((*(uint8_t *)(local_r13)) << ((uint8_t)((uint32_t)((uint32_t)(local_r14)))));
    local_r12 = (uint32_t)((local_r12) - 1);
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(result)));
    local_r13 = (local_r13) + 1;
    local_r14 = (uint32_t)((local_r14) + (8));
    goto loc_005F2908;
loc_005F292F:
    local_r15 = (uint32_t)((local_r15) >> ((uint8_t)((uint32_t)((uint32_t)(v_stack_pA9)))));
    local_r14 = (uint32_t)((local_r14) - ((uint32_t)(v_stack_pA9)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x84))) == 0) goto loc_005F2A4A;
    local_r14 = (uint32_t)((local_r14) + (-2));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (3));
    local_r15 = (uint32_t)((local_r15) >> (2));
    Arg2 = (uint32_t)((Arg2) + (3));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x84))) - 1);
    goto loc_005F2A0F;
loc_005F2966:
    if (v_stack_pAA != 17) goto loc_005F29C2;
loc_005F297E:
    if (((uint32_t)(local_r14)) >= ((uint32_t)(v_stack_pA9 + 3))) goto loc_005F29A5;
    if ((uint32_t)(local_r12) == 0) goto loc_005F322E;
    result = (uint32_t)((*(uint8_t *)(local_r13)) << ((uint8_t)((uint32_t)((uint32_t)(local_r14)))));
    local_r12 = (uint32_t)((local_r12) - 1);
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(result)));
    local_r13 = (local_r13) + 1;
    local_r14 = (uint32_t)((local_r14) + (8));
    goto loc_005F297E;
loc_005F29A5:
    local_r15 = (uint32_t)((local_r15) >> ((uint8_t)((uint32_t)((uint32_t)(v_stack_pA9)))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (7));
    Arg2 = (uint32_t)((Arg2) + (3));
    local_r15 = (uint32_t)((local_r15) >> (3));
    goto loc_005F2A09;
loc_005F29C2:
loc_005F29C6:
    if (((uint32_t)(local_r14)) >= ((uint32_t)(v_stack_pA9 + 7))) goto loc_005F29ED;
    if ((uint32_t)(local_r12) == 0) goto loc_005F322E;
    result = (uint32_t)((*(uint8_t *)(local_r13)) << ((uint8_t)((uint32_t)((uint32_t)(local_r14)))));
    local_r12 = (uint32_t)((local_r12) - 1);
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(result)));
    local_r13 = (local_r13) + 1;
    local_r14 = (uint32_t)((local_r14) + (8));
    goto loc_005F29C6;
loc_005F29ED:
    local_r15 = (uint32_t)((local_r15) >> ((uint8_t)((uint32_t)((uint32_t)(v_stack_pA9)))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (127));
    Arg2 = (uint32_t)((Arg2) + (11));
    local_r15 = (uint32_t)((local_r15) >> (7));
loc_005F2A09:
    Arg1 = (uint32_t)(((uint32_t)(0xFFFFFFF9ULL)) - ((uint32_t)(v_stack_pA9)));
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(Arg1)));
loc_005F2A0F:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x80))) + (*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x7C)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x84)) + Arg2 * 1)) > ((uint32_t)(result))) goto loc_005F2A4A;
loc_005F2A27:
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x28) + (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x84)))) * 2 + 0x90) = 0;
    Arg2 = (uint32_t)((Arg2) + (-1));
    if (condition_is_not_equal) goto loc_005F2A27;
    goto loc_005F2863;
loc_005F2A4A:
    *(uint64_t *)(arg1 + 0x20) = v_rip + 895791;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F51ULL;
loc_005F2A5C:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8)) == 0x3F51ULL) goto loc_005F2332;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x28) + 0x290)) != 0) goto loc_005F2A93;
    goto loc_005F31C0;
loc_005F2A93:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x60) = *(uint64_t *)(arg1 + 0x28) + 1360;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x88) = *(uint64_t *)(arg1 + 0x28) + 1360;
    v_stack_p28 = *(uint64_t *)(arg1 + 0x28) + 784;
    v_stack_p20 = *(uint64_t *)(arg1 + 0x28) + 112;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x70) = 10;
    result = inflate_table(1, *(uint64_t *)(arg1 + 0x28) + 144, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x7C)), *(uint64_t *)(arg1 + 0x28) + 136);
    v_stack_p98 = (uint32_t)(result);
    if ((uint32_t)(result) == 0) goto loc_005F2B0A;
    local_rbp = 0;
    goto loc_005F254C;
loc_005F2B0A:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x68) = *(uint64_t *)((uint32_t)(v_stack_p30));
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x7C))) + (72);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x74) = 9;
    v_stack_p28 = 0;
    v_stack_p20 = *(uint64_t *)(arg1 + 0x28) + 116;
    result = inflate_table(2, *(uint64_t *)(arg1 + 0x28) + result * 2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x80)), (uint32_t)(v_stack_p30));
    local_rbp = 0;
    v_stack_p98 = (uint32_t)(result);
    if ((uint32_t)(result) == 0) goto loc_005F2B8A;
    goto loc_005F284D;
loc_005F2B72:
    goto loc_005F254C;
loc_005F2B7E:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F3FULL;
    goto loc_005F31CB;
loc_005F2B8A:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F48ULL;
loc_005F2B91:
    if (((uint32_t)(local_r12)) < 15) goto loc_005F2C65;
    if (((uint32_t)((uint32_t)(v_stack_pA0))) < 260) goto loc_005F2C65;
    *(uint32_t *)(arg1 + 0x18) = (uint32_t)((uint32_t)(v_stack_pA0));
    *(uint64_t *)(arg1) = local_r13;
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)(local_r12);
    *(uint64_t *)(v_stack_p40) = v_stack_p38;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x48) = (uint32_t)(local_r15);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x4C) = (uint32_t)(local_r14);
    result = inflate_fast_chunk_(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p30))), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x80)), v_stack_p38);
    v_stack_p38 = *(uint64_t *)(v_stack_p40);
    v_stack_pA0 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)));
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8)) != 0x3F3FULL) goto loc_005F2332;
    goto loc_005F232A;
loc_005F2C1E:
    if (((uint32_t)(Arg1)) > 0x3F4DULL) goto loc_005F311F;
    if (((uint32_t)(Arg1)) == 0x3F4DULL) goto loc_005F30F1;
    Arg1 = (uint32_t)((Arg1) - (0x3F48ULL));
    if (condition_is_equal) goto loc_005F2B91;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_005F2DCA;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_005F2E26;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_005F2F4A;
    if (((uint32_t)(Arg1)) != 1) goto loc_005F2381;
    goto loc_005F2FA2;
loc_005F2C65:
    a3 = (uint32_t)((1) << ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x70)))));
    a3 = (uint32_t)((a3) - 1);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x2364) = 0;
loc_005F2C7E:
    Arg1 = ((uint32_t)((uint32_t)(a3))) & ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x48)))));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x60) + arg1 * 4))))) >> (8));
    v_stack_pA8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x60) + arg1 * 4)));
    if (((uint32_t)((uint8_t)(Arg1))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x4C))))) goto loc_005F2CC0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8))) == 0) goto loc_005F322E;
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(arg1))) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x4C)))))));
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8))) - 1);
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x48))) + ((uint32_t)(result)));
    local_r13 = (*(uint64_t *)(arg1)) + 1;
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x4C))) + (8));
    goto loc_005F2C7E;
loc_005F2CC0:
    if ((uint8_t)(result) == 0) goto loc_005F2D4A;
    if ((((uint8_t)(result)) & (240)) != 0) goto loc_005F2D4A;
    Arg1 = (uint32_t)(((uint8_t)(result)) + ((uint32_t)(v_stack_pA9)));
    a4 = (uint32_t)((1) << ((uint8_t)(Arg1)));
loc_005F2CF1:
    result = (uint32_t)((a4 - 1) & ((uint32_t)(local_r15)));
    result = (uint32_t)((result) >> ((uint8_t)((uint32_t)((uint32_t)(v_stack_pA9)))));
    result = (uint32_t)((result) + ((uint32_t)(v_stack_pAA)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x60) + result * 4))))) >> (8));
    Arg2 = (uint32_t)(((uint8_t)(Arg1)) + ((uint32_t)(v_stack_pA9)));
    if (Arg2 <= ((uint32_t)(local_r14))) goto loc_005F2D36;
    if ((uint32_t)(local_r12) == 0) goto loc_005F322E;
    result = (uint32_t)((*(uint8_t *)(local_r13)) << ((uint8_t)((uint32_t)((uint32_t)(local_r14)))));
    local_r12 = (uint32_t)((local_r12) - 1);
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(result)));
    local_r13 = (local_r13) + 1;
    local_r14 = (uint32_t)((local_r14) + (8));
    goto loc_005F2CF1;
loc_005F2D36:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x2364) = (uint32_t)(v_stack_pA9);
    local_r15 = (uint32_t)((local_r15) >> ((uint8_t)((uint32_t)((uint32_t)(v_stack_pA9)))));
    local_r14 = (uint32_t)((local_r14) - ((uint32_t)(v_stack_pA9)));
loc_005F2D4A:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (8));
    local_r15 = (uint32_t)((local_r15) >> ((uint8_t)((uint32_t)((uint32_t)((uint8_t)(Arg1))))));
    local_r14 = (uint32_t)((local_r14) - ((uint32_t)((uint8_t)(Arg1))));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (16));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x50) = (uint32_t)(Arg1);
    if ((uint8_t)(result) != 0) goto loc_005F2D85;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F4DULL;
loc_005F2D73:
    goto loc_005F25DA;
loc_005F2D85:
    if ((((uint8_t)(result)) & (32)) == 0) goto loc_005F2D99;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F3FULL;
    goto loc_005F2D73;
loc_005F2D99:
    if ((((uint8_t)(result)) & (64)) == 0) goto loc_005F2DBA;
    goto loc_005F254C;
loc_005F2DBA:
    Arg1 = (uint32_t)(((uint8_t)(v_rip + 894803)) & (15));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F49ULL;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x58) = (uint32_t)(Arg1);
loc_005F2DCA:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x58))) == 0) goto loc_005F2E16;
loc_005F2DD1:
    if (((uint32_t)(local_r14)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x58))))) goto loc_005F2DF8;
    if ((uint32_t)(local_r12) == 0) goto loc_005F322E;
    result = (uint32_t)((*(uint8_t *)(local_r13)) << ((uint8_t)((uint32_t)((uint32_t)(local_r14)))));
    local_r12 = (uint32_t)((local_r12) - 1);
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(result)));
    local_r13 = (local_r13) + 1;
    local_r14 = (uint32_t)((local_r14) + (8));
    goto loc_005F2DD1;
loc_005F2DF8:
    result = (uint32_t)((1) << ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x58)))));
    local_r14 = (uint32_t)((local_r14) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x58)))));
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) & ((uint32_t)(local_r15)));
    local_r15 = (uint32_t)((local_r15) >> ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x58)))));
loc_005F2E16:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x2368) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x50)));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F4AULL;
loc_005F2E26:
    a3 = (uint32_t)((1) << ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x74)))));
    a3 = (uint32_t)((a3) - 1);
loc_005F2E39:
    Arg1 = ((uint32_t)((uint32_t)(a3))) & ((uint32_t)((uint32_t)(local_r15)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x68) + arg1 * 4))))) >> (8));
    v_stack_pA8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x68) + arg1 * 4)));
    if (((uint32_t)((uint8_t)(Arg1))) <= ((uint32_t)(local_r14))) goto loc_005F2E7B;
    if ((uint32_t)(local_r12) == 0) goto loc_005F322E;
    result = (uint32_t)((*(uint8_t *)(local_r13)) << ((uint8_t)((uint32_t)((uint32_t)(local_r14)))));
    local_r12 = (uint32_t)((local_r12) - 1);
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(result)));
    local_r13 = (local_r13) + 1;
    local_r14 = (uint32_t)((local_r14) + (8));
    goto loc_005F2E39;
loc_005F2E7B:
    if ((((uint8_t)(result)) & (240)) != 0) goto loc_005F2EF9;
    Arg1 = (uint32_t)(((uint8_t)(result)) + ((uint32_t)(v_stack_pA9)));
    a4 = (uint32_t)((1) << ((uint8_t)(Arg1)));
loc_005F2EA4:
    result = (uint32_t)((a4 - 1) & ((uint32_t)(local_r15)));
    result = (uint32_t)((result) >> ((uint8_t)((uint32_t)((uint32_t)(v_stack_pA9)))));
    result = (uint32_t)((result) + ((uint32_t)(v_stack_pAA)));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x68) + result * 4))))) >> (8));
    Arg2 = (uint32_t)(((uint8_t)(Arg1)) + ((uint32_t)(v_stack_pA9)));
    if (Arg2 <= ((uint32_t)(local_r14))) goto loc_005F2EE9;
    if ((uint32_t)(local_r12) == 0) goto loc_005F322E;
    result = (uint32_t)((*(uint8_t *)(local_r13)) << ((uint8_t)((uint32_t)((uint32_t)(local_r14)))));
    local_r12 = (uint32_t)((local_r12) - 1);
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(result)));
    local_r13 = (local_r13) + 1;
    local_r14 = (uint32_t)((local_r14) + (8));
    goto loc_005F2EA4;
loc_005F2EE9:
    local_r14 = (uint32_t)((local_r14) - ((uint32_t)(v_stack_pA9)));
    local_r15 = (uint32_t)((local_r15) >> ((uint8_t)((uint32_t)((uint32_t)(v_stack_pA9)))));
loc_005F2EF9:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) >> (8));
    local_r14 = (uint32_t)((local_r14) - ((uint32_t)((uint8_t)(Arg1))));
    local_r15 = (uint32_t)((local_r15) >> ((uint8_t)((uint8_t)(Arg1))));
    if ((((uint8_t)(result)) & (64)) == 0) goto loc_005F2F32;
    goto loc_005F254C;
loc_005F2F32:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F4BULL;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_rip + 894451))) >> (16));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x54) = (uint32_t)(Arg1);
    Arg1 = (uint32_t)(((uint8_t)(v_rip + 894451)) & (15));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x58) = (uint32_t)(Arg1);
loc_005F2F4A:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x58))) == 0) goto loc_005F2F96;
loc_005F2F51:
    if (((uint32_t)(local_r14)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x58))))) goto loc_005F2F78;
    if ((uint32_t)(local_r12) == 0) goto loc_005F322E;
    result = (uint32_t)((*(uint8_t *)(local_r13)) << ((uint8_t)((uint32_t)((uint32_t)(local_r14)))));
    local_r12 = (uint32_t)((local_r12) - 1);
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(result)));
    local_r13 = (local_r13) + 1;
    local_r14 = (uint32_t)((local_r14) + (8));
    goto loc_005F2F51;
loc_005F2F78:
    result = (uint32_t)((1) << ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x58)))));
    local_r14 = (uint32_t)((local_r14) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x58)))));
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) & ((uint32_t)(local_r15)));
    local_r15 = (uint32_t)((local_r15) >> ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x58)))));
loc_005F2F96:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F4CULL;
loc_005F2FA2:
    if ((uint32_t)((uint32_t)(v_stack_pA0)) == 0) goto loc_005F322E;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p30)))) - ((uint32_t)((uint32_t)(v_stack_pA0))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x54)))) <= ((uint32_t)(result))) goto loc_005F3059;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x54))) - ((uint32_t)(result)));
    if (((uint32_t)(Arg1)) <= (*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x38))) goto loc_005F2FD6;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x2360)) == 0) goto loc_005F2FD6;
    goto loc_005F31C0;
loc_005F2FD6:
    if (((uint32_t)(Arg1)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x3C))))) goto loc_005F2FEA;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x3C)))));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x34))) - ((uint32_t)(Arg1)));
    goto loc_005F2FEE;
loc_005F2FEA:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x3C))) - ((uint32_t)(Arg1)));
loc_005F2FEE:
    Arg2 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x40));
    local_r10 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x50));
    if (((uint32_t)(Arg1)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x50))))) { local_r10 = (uint32_t)(Arg1); }
    if (((uint32_t)(local_r10)) > ((uint32_t)((uint32_t)(v_stack_pA0)))) { local_r10 = (uint32_t)((uint32_t)(v_stack_pA0)); }
    if (((uint32_t)((uint32_t)(v_stack_pA0))) >= 16) goto loc_005F30AB;
    if ((((uint8_t)(local_r10)) & (8)) != 0) {
        result = *(uint64_t *)(Arg2);
        *(uint64_t *)(v_stack_p38) = result;
        a4 = (v_stack_p38) + (8);
        Arg2 = (Arg2) + (8);
    }
    if ((((uint8_t)(local_r10)) & (4)) != 0) {
        result = *(uint32_t *)(Arg2);
        *(uint32_t *)(a4) = (uint32_t)(result);
        a4 = (a4) + (4);
        Arg2 = (Arg2) + (4);
    }
    if ((((uint8_t)(local_r10)) & (2)) != 0) {
        result = *(uint16_t *)(Arg2);
        *(uint16_t *)(a4) = (uint16_t)(result);
        a4 = (a4) + (2);
        Arg2 = (Arg2) + (2);
    }
    if ((((uint8_t)(local_r10)) & (1)) == 0) goto loc_005F3085;
    *(uint8_t *)(a4) = (uint8_t)(*(uint8_t *)(Arg2));
    a4 = (a4) + 1;
    goto loc_005F3085;
loc_005F3059:
    local_r10 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x50));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x50)))) > ((uint32_t)((uint32_t)(v_stack_pA0)))) { local_r10 = (uint32_t)((uint32_t)(v_stack_pA0)); }
    if (((uint32_t)((uint32_t)(v_stack_pA0))) >= 48) goto loc_005F308C;
    if ((uint32_t)(local_r10) == 0) goto loc_005F3085;
loc_005F3072:
    result = (a4) - (Arg1);
    *(uint8_t *)(a4) = (uint8_t)(*(uint8_t *)(result));
    a4 = (a4) + 1;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) + (-1));
    if (condition_is_not_equal) goto loc_005F3072;
loc_005F3085:
    v_stack_p38 = a4;
    goto loc_005F30BB;
loc_005F308C:
    if (((uint32_t)(Arg1)) >= ((uint32_t)(local_r10))) goto loc_005F30A5;
    if (((uint32_t)(Arg1)) >= 16) goto loc_005F30A5;
    result = chunkset_core(a4, (uint32_t)((uint32_t)(Arg1)), (uint32_t)((uint32_t)(local_r10)), a4);
    goto loc_005F30B6;
loc_005F30A5:
    Arg2 = (a4) - (a4);
loc_005F30AB:
    result = chunkcopy_core(a4, Arg2, (uint32_t)((uint32_t)(local_r10)), a4);
loc_005F30B6:
    v_stack_p38 = result;
loc_005F30BB:
    local_r11 = (uint32_t)(((uint32_t)(v_stack_pA0)) - ((uint32_t)(local_r10)));
    v_stack_pA0 = (uint32_t)(local_r11);
    if (condition_is_not_equal) goto loc_005F2332;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F48ULL;
    goto loc_005F232A;
loc_005F30F1:
    if ((uint32_t)(local_r11) == 0) goto loc_005F322E;
    *(uint8_t *)(v_stack_p38) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x28) + 0x50));
    a4 = (v_stack_p38) + 1;
    local_r11 = (uint32_t)((local_r11) - 1);
    v_stack_p38 = a4;
    v_stack_pA0 = (uint32_t)(local_r11);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F48ULL;
    goto loc_005F31CB;
loc_005F311F:
    Arg1 = (uint32_t)((a4) - (0x3F4EULL));
    if (condition_is_not_equal) goto loc_005F320A;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x10)) == 0) goto loc_005F31FC;
loc_005F3134:
    if (((uint32_t)(local_r14)) >= 32) goto loc_005F315C;
    if ((uint32_t)(local_r12) == 0) goto loc_005F322E;
    result = (uint32_t)((*(uint8_t *)(local_r13)) << ((uint8_t)((uint32_t)((uint32_t)(local_r14)))));
    local_r12 = (uint32_t)((local_r12) - 1);
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(result)));
    local_r13 = (local_r13) + 1;
    local_r14 = (uint32_t)((local_r14) + (8));
    goto loc_005F3134;
loc_005F315C:
    local_rbx = (uint32_t)(((uint32_t)(v_stack_p30)) - ((uint32_t)(local_r11)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x10)))) & (4)) == 0) goto loc_005F31A1;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x10));
    local_r10 = *(uint64_t *)(arg1 + 0x28) + 112;
    if ((uint32_t)(local_rbx) != 0) {
        Arg1 = *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x20);
        Arg2 = a4;
        a3 = (uint32_t)(local_rbx);
        Arg2 = (Arg2) - (a3);
        result = adler32_z(Arg1, Arg2, a3, a4);
        a4 = v_stack_p38;
        local_r10 = *(uint64_t *)(arg1 + 0x28) + 112;
        local_r11 = v_stack_pA0;
        a3 = *(uint64_t *)(arg1 + 0x28) + 116;
        *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x20) = (uint32_t)(result);
        Arg2 = 16;
        *(uint32_t *)(arg1 + 0x4C) = (uint32_t)(result);
    }
    v_stack_p30 = (uint32_t)((uint32_t)((uint32_t)(local_r11)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x10)))) & (4)) == 0) goto loc_005F31F6;
    if (((uint32_t)((uint32_t)((uint32_t)(local_r15)))) == (*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x20))) goto loc_005F31F6;
loc_005F31C0:
    *(uint64_t *)(arg1 + 0x20) = v_rip + 893856;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F51ULL;
loc_005F31CB:
    goto loc_005F2332;
loc_005F31D5:
    *(uint64_t *)(arg1 + 0x10) = a4;
    *(uint32_t *)(arg1 + 0x18) = (uint32_t)(local_r11);
    *(uint64_t *)(arg1) = local_r13;
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)(local_r12);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x48) = (uint32_t)(local_r15);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x4C) = (uint32_t)(local_r14);
    goto loc_005F2386;
loc_005F31F6:
loc_005F31FC:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F50ULL;
loc_005F3203:
    goto loc_005F3235;
loc_005F320A:
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_005F3203;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_005F3227;
    if (((uint32_t)(Arg1)) != 1) goto loc_005F2381;
loc_005F321D:
    goto loc_005F2386;
loc_005F3227:
    goto loc_005F3235;
loc_005F322E:
loc_005F3235:
    *(uint64_t *)(arg1 + 0x10) = v_stack_p38;
    *(uint32_t *)(arg1 + 0x18) = (uint32_t)((uint32_t)(v_stack_pA0));
    *(uint64_t *)(arg1) = local_r13;
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)(local_r12);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x4C) = 0;
    local_r14 = 0;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x48) = 0;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x34)) != 0) goto loc_005F326E;
    if (((uint32_t)((uint32_t)((uint32_t)(local_r11)))) == (*(uint32_t *)(arg1 + 0x18))) goto loc_005F328E;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8)) > 0x3F4DULL) goto loc_005F328E;
loc_005F326E:
    a3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r11))))) - (*(uint32_t *)(arg1 + 0x18)));
    result = updatewindow(Arg1, *(uint64_t *)(arg1 + 0x10), a3, a4);
    if ((uint32_t)(result) == 0) goto loc_005F328E;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F52ULL;
    goto loc_005F321D;
loc_005F328E:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(local_r11))) - (*(uint32_t *)(arg1 + 0x18)));
    result = (uint32_t)(((uint32_t)(v_stack_p34)) - (*(uint32_t *)(arg1 + 0x8)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x10)))) & (4)) == 0) goto loc_005F32C4;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x10));
    if ((uint32_t)(local_rbx) != 0) {
        Arg2 = *(uint64_t *)(arg1 + 0x10);
        Arg1 = *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x20);
        a3 = (uint32_t)(local_rbx);
        Arg2 = (Arg2) - (a3);
        result = adler32_z(Arg1, Arg2, a3, a4);
        *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x20) = (uint32_t)(result);
        *(uint32_t *)(arg1 + 0x4C) = (uint32_t)(result);
    }
    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0xC))));
    Arg2 = (uint32_t)((Arg2) & (64));
    a3 = 128;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8)))) != 0x3F3FULL) { a3 = 0; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8)))) == 0x3F47ULL) goto loc_005F32F1;
    result = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8)))) == 0x3F42ULL) {
        result = 256;
    }
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x4C))) + ((uint32_t)(a3)));
    Arg1 = (uint32_t)((Arg1) + (Arg2));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(result)));
    *(uint32_t *)(arg1 + 0x48) = (uint32_t)(Arg1);
    local_rbp = (uint32_t)(v_stack_p98);
    if ((uint32_t)((uint32_t)(v_stack_p98)) == 0) { local_rbp = (uint32_t)((uint32_t)(0xFFFFFFFBULL)); }
    goto loc_005F2386;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x8` | `32` | `W` |
| `Arg1` | `+ 0xC` | `32` | `R/W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x18` | `32` | `W` |
| `Arg1` | `+ 0x1C` | `32` | `R/W` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x48` | `32` | `W` |
| `Arg1` | `+ 0x4C` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005F2280&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
