# LdrpResSearchResourceInsideDirectory

- RVA: `0x009F22F0`–`0x009F2EC3` (길이 `3,027` bytes)
- VA: `0x00000001409F22F0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A619C`
- 디코드: `699`개 명령, `3,027/3,027` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009F269C` → [LdrpResCompareResourceNames](LdrpResCompareResourceNames_function_009F2ECC.md) (function, `0x009F2ECC`)
- `0x009F2B9F` → [LdrpSectionTableFromVirtualAddress](LdrpSectionTableFromVirtualAddress_function_009F33A0.md) (function, `0x009F33A0`)
- `0x009F2BD5` → [LdrpSectionTableFromVirtualAddress](LdrpSectionTableFromVirtualAddress_function_009F33A0.md) (function, `0x009F33A0`)
- `0x009F2C05` → [LdrpSectionTableFromVirtualAddress](LdrpSectionTableFromVirtualAddress_function_009F33A0.md) (function, `0x009F33A0`)
- `0x009F2D26` → [wcsncmp](../../text/50/wcsncmp_function_00501CA0.md) (function, `0x00501CA0`)

### Direct callers
- [LdrpResSearchResourceMappedFile](../../text/45/LdrpResSearchResourceMappedFile_function_00454C98.md) at `0x0045503F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009F2D26` → [wcsncmp](../../text/50/wcsncmp_function_00501CA0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009F22F0  48 8B C4                        mov rax, rsp
009F22F3  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
009F22F7  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
009F22FB  53                              push rbx
009F22FC  56                              push rsi
009F22FD  57                              push rdi
009F22FE  41 54                           push r12
009F2300  41 55                           push r13
009F2302  41 56                           push r14
009F2304  41 57                           push r15
009F2306  48 81 EC F0 00 00 00            sub rsp, 0xf0
009F230D  4D 8B E1                        mov r12, r9
009F2310  4D 8B D0                        mov r10, r8
009F2313  48 8B F1                        mov rsi, rcx
009F2316  33 DB                           xor ebx, ebx
009F2318  89 5C 24 44                     mov dword ptr [rsp + 0x44], ebx
009F231C  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
009F2320  66 89 58 30                     mov word ptr [rax + 0x30], bx
009F2324  8B D3                           mov edx, ebx
009F2326  0F B7 C3                        movzx eax, bx
009F2329  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
009F232D  4D 85 C9                        test r9, r9
009F2330  74 74                           je 0x1409f23a6
009F2332  48 39 9C 24 50 01 00 00         cmp qword ptr [rsp + 0x150], rbx
009F233A  74 6A                           je 0x1409f23a6
009F233C  4C 8B 9C 24 60 01 00 00         mov r11, qword ptr [rsp + 0x160]
009F2344  4D 85 DB                        test r11, r11
009F2347  74 5D                           je 0x1409f23a6
009F2349  44 8B 84 24 68 01 00 00         mov r8d, dword ptr [rsp + 0x168]
009F2351  41 8D 40 FF                     lea eax, [r8 - 1]
009F2355  83 F8 03                        cmp eax, 3
009F2358  77 4C                           ja 0x1409f23a6
009F235A  44 8B 8C 24 88 01 00 00         mov r9d, dword ptr [rsp + 0x188]
009F2362  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
009F2367  41 0F BA E1 0F                  bt r9d, 0xf
009F236C  72 38                           jb 0x1409f23a6
009F236E  45 8B F9                        mov r15d, r9d
009F2371  41 81 E7 00 10 00 00            and r15d, 0x1000
009F2378  44 89 7C 24 48                  mov dword ptr [rsp + 0x48], r15d
009F237D  0F 95 84 24 38 01 00 00         setne byte ptr [rsp + 0x138]
009F2385  41 8B C1                        mov eax, r9d
009F2388  B9 00 88 00 00                  mov ecx, 0x8800
009F238D  23 C1                           and eax, ecx
009F238F  45 85 FF                        test r15d, r15d
009F2392  74 05                           je 0x1409f2399
009F2394  4D 85 D2                        test r10, r10
009F2397  74 0D                           je 0x1409f23a6
009F2399  3B C1                           cmp eax, ecx
009F239B  74 09                           je 0x1409f23a6
009F239D  48 85 F6                        test rsi, rsi
009F23A0  74 04                           je 0x1409f23a6
009F23A2  3B C1                           cmp eax, ecx
009F23A4  75 0A                           jne 0x1409f23b0
009F23A6  B8 0D 00 00 C0                  mov eax, 0xc000000d
009F23AB  E9 FF 0A 00 00                  jmp 0x1409f2eaf
009F23B0  41 8B C8                        mov ecx, r8d
009F23B3  89 4C 24 7C                     mov dword ptr [rsp + 0x7c], ecx
009F23B7  49 8B FC                        mov rdi, r12
009F23BA  4C 8B EB                        mov r13, rbx
009F23BD  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
009F23C2  48 89 9C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rbx
009F23CA  4C 8B B4 24 90 01 00 00         mov r14, qword ptr [rsp + 0x190]
009F23D2  4D 85 F6                        test r14, r14
009F23D5  74 04                           je 0x1409f23db
009F23D7  66 41 89 1E                     mov word ptr [r14], bx
009F23DB  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009F23E0  48 85 FF                        test rdi, rdi
009F23E3  0F 84 17 04 00 00               je 0x1409f2800
009F23E9  8B C1                           mov eax, ecx
009F23EB  FF C9                           dec ecx
009F23ED  89 4C 24 7C                     mov dword ptr [rsp + 0x7c], ecx
009F23F1  89 8C 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], ecx
009F23F8  85 C0                           test eax, eax
009F23FA  0F 84 00 04 00 00               je 0x1409f2800
009F2400  4D 8B 33                        mov r14, qword ptr [r11]
009F2403  4C 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r14
009F240B  4C 89 B4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r14
009F2413  33 D2                           xor edx, edx
009F2415  85 C9                           test ecx, ecx
009F2417  0F 84 32 03 00 00               je 0x1409f274f
009F241D  45 85 FF                        test r15d, r15d
009F2420  74 20                           je 0x1409f2442
009F2422  48 8D 4F 18                     lea rcx, [rdi + 0x18]
009F2426  48 3B CF                        cmp rcx, rdi
009F2429  0F 82 B1 01 00 00               jb 0x1409f25e0
009F242F  48 8B C6                        mov rax, rsi
009F2432  48 83 E0 FC                     and rax, 0xfffffffffffffffc
009F2436  49 03 C2                        add rax, r10
009F2439  48 3B C8                        cmp rcx, rax
009F243C  0F 87 9E 01 00 00               ja 0x1409f25e0
009F2442  44 0F B7 6F 0C                  movzx r13d, word ptr [rdi + 0xc]
009F2447  44 89 6C 24 78                  mov dword ptr [rsp + 0x78], r13d
009F244C  44 89 AC 24 48 01 00 00         mov dword ptr [rsp + 0x148], r13d
009F2454  45 85 ED                        test r13d, r13d
009F2457  0F 85 A7 02 00 00               jne 0x1409f2704
009F245D  4C 8D 5F 10                     lea r11, [rdi + 0x10]
009F2461  4C 89 9C 24 98 00 00 00         mov qword ptr [rsp + 0x98], r11
009F2469  4C 89 9C 24 90 00 00 00         mov qword ptr [rsp + 0x90], r11
009F2471  49 F7 C6 00 00 FF FF            test r14, -0x10000
009F2478  75 5E                           jne 0x1409f24d8
009F247A  45 85 ED                        test r13d, r13d
009F247D  0F 85 B2 04 00 00               jne 0x1409f2935
009F2483  44 0F B7 6F 0E                  movzx r13d, word ptr [rdi + 0xe]
009F2488  44 89 6C 24 78                  mov dword ptr [rsp + 0x78], r13d
009F248D  44 89 AC 24 48 01 00 00         mov dword ptr [rsp + 0x148], r13d
009F2495  45 85 FF                        test r15d, r15d
009F2498  74 3E                           je 0x1409f24d8
009F249A  41 8B C5                        mov eax, r13d
009F249D  48 C1 E0 03                     shl rax, 3
009F24A1  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
009F24A9  B9 FF FF FF FF                  mov ecx, 0xffffffff
009F24AE  48 3B C1                        cmp rax, rcx
009F24B1  0F 87 29 01 00 00               ja 0x1409f25e0
009F24B7  8B C8                           mov ecx, eax
009F24B9  49 03 CB                        add rcx, r11
009F24BC  49 3B CB                        cmp rcx, r11
009F24BF  0F 82 1B 01 00 00               jb 0x1409f25e0
009F24C5  48 8B C6                        mov rax, rsi
009F24C8  48 83 E0 FC                     and rax, 0xfffffffffffffffc
009F24CC  49 03 C2                        add rax, r10
009F24CF  48 3B C8                        cmp rcx, rax
009F24D2  0F 87 08 01 00 00               ja 0x1409f25e0
009F24D8  45 85 ED                        test r13d, r13d
009F24DB  0F 84 A1 08 00 00               je 0x1409f2d82
009F24E1  48 39 94 24 80 00 00 00         cmp qword ptr [rsp + 0x80], rdx
009F24E9  0F 85 D1 02 00 00               jne 0x1409f27c0
009F24EF  4C 8B 84 24 88 00 00 00         mov r8, qword ptr [rsp + 0x88]
009F24F7  48 8B FA                        mov rdi, rdx
009F24FA  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
009F24FF  49 8B D3                        mov rdx, r11
009F2502  48 89 94 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdx
009F250A  49 63 C5                        movsxd rax, r13d
009F250D  49 83 EB 08                     sub r11, 8
009F2511  49 8D 04 C3                     lea rax, [r11 + rax*8]
009F2515  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
009F251D  45 8B F5                        mov r14d, r13d
009F2520  44 89 AC 24 48 01 00 00         mov dword ptr [rsp + 0x148], r13d
009F2528  45 33 DB                        xor r11d, r11d
009F252B  48 3B D0                        cmp rdx, rax
009F252E  0F 87 C5 00 00 00               ja 0x1409f25f9
009F2534  41 D1 FD                        sar r13d, 1
009F2537  0F 85 11 01 00 00               jne 0x1409f264e
009F253D  45 85 F6                        test r14d, r14d
009F2540  0F 84 B3 00 00 00               je 0x1409f25f9
009F2546  44 89 5C 24 4C                  mov dword ptr [rsp + 0x4c], r11d
009F254B  41 8B C9                        mov ecx, r9d
009F254E  81 E1 00 10 00 00               and ecx, 0x1000
009F2554  48 85 D2                        test rdx, rdx
009F2557  0F 84 BD 08 00 00               je 0x1409f2e1a
009F255D  45 8B F3                        mov r14d, r11d
009F2560  44 89 5C 24 4C                  mov dword ptr [rsp + 0x4c], r11d
009F2565  8B 02                           mov eax, dword ptr [rdx]
009F2567  49 C7 C5 00 00 FF FF            mov r13, 0xffffffffffff0000
009F256E  4D 85 C5                        test r13, r8
009F2571  0F 85 68 07 00 00               jne 0x1409f2cdf
009F2577  85 C0                           test eax, eax
009F2579  0F 88 9F 05 00 00               js 0x1409f2b1e
009F257F  85 C9                           test ecx, ecx
009F2581  74 0B                           je 0x1409f258e
009F2583  8B C0                           mov eax, eax
009F2585  49 85 C5                        test r13, rax
009F2588  0F 85 7C 08 00 00               jne 0x1409f2e0a
009F258E  44 2B 02                        sub r8d, dword ptr [rdx]
009F2591  44 89 44 24 44                  mov dword ptr [rsp + 0x44], r8d
009F2596  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
009F259B  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
009F259F  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
009F25A4  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
009F25AC  45 85 F6                        test r14d, r14d
009F25AF  0F 88 E5 04 00 00               js 0x1409f2a9a
009F25B5  85 C0                           test eax, eax
009F25B7  75 40                           jne 0x1409f25f9
009F25B9  8B 42 04                        mov eax, dword ptr [rdx + 4]
009F25BC  85 C0                           test eax, eax
009F25BE  0F 89 2A 04 00 00               jns 0x1409f29ee
009F25C4  45 85 FF                        test r15d, r15d
009F25C7  74 21                           je 0x1409f25ea
009F25C9  4C 39 9C 24 80 00 00 00         cmp qword ptr [rsp + 0x80], r11
009F25D1  75 0D                           jne 0x1409f25e0
009F25D3  0F BA F0 1F                     btr eax, 0x1f
009F25D7  4A 8D 3C 20                     lea rdi, [rax + r12]
009F25DB  49 3B FC                        cmp rdi, r12
009F25DE  73 14                           jae 0x1409f25f4
009F25E0  BB 7B 00 00 C0                  mov ebx, 0xc000007b
009F25E5  E9 B7 08 00 00                  jmp 0x1409f2ea1
009F25EA  48 8B F8                        mov rdi, rax
009F25ED  0F BA F7 1F                     btr edi, 0x1f
009F25F1  49 03 FC                        add rdi, r12
009F25F4  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
009F25F9  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
009F25FE  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
009F2603  4C 39 9C 24 80 00 00 00         cmp qword ptr [rsp + 0x80], r11
009F260B  0F 85 51 03 00 00               jne 0x1409f2962
009F2611  4C 8B 9C 24 60 01 00 00         mov r11, qword ptr [rsp + 0x160]
009F2619  49 83 C3 08                     add r11, 8
009F261D  4C 89 9C 24 60 01 00 00         mov qword ptr [rsp + 0x160], r11
009F2625  4C 89 9C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r11
009F262D  44 8B 84 24 68 01 00 00         mov r8d, dword ptr [rsp + 0x168]
009F2635  4C 8B 94 24 40 01 00 00         mov r10, qword ptr [rsp + 0x140]
009F263D  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
009F2645  8B 4C 24 7C                     mov ecx, dword ptr [rsp + 0x7c]
009F2649  E9 92 FD FF FF                  jmp 0x1409f23e0
009F264E  48 89 94 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdx
009F2656  41 80 E6 01                     and r14b, 1
009F265A  44 88 B4 24 48 01 00 00         mov byte ptr [rsp + 0x148], r14b
009F2662  45 8D 75 FF                     lea r14d, [r13 - 1]
009F2666  49 63 C5                        movsxd rax, r13d
009F2669  75 03                           jne 0x1409f266e
009F266B  49 63 C6                        movsxd rax, r14d
009F266E  4C 8D 3C C2                     lea r15, [rdx + rax*8]
009F2672  4C 89 BC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r15
009F267A  48 8D 44 24 50                  lea rax, [rsp + 0x50]
009F267F  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009F2684  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
009F2689  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
009F268E  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
009F2693  4D 8B C8                        mov r9, r8
009F2696  4D 8B C2                        mov r8, r10
009F2699  48 8B CE                        mov rcx, rsi
009F269C  E8 2B 08 00 00                  call 0x1409f2ecc
009F26A1  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
009F26A5  45 33 DB                        xor r11d, r11d
009F26A8  85 C0                           test eax, eax
009F26AA  0F 88 D2 03 00 00               js 0x1409f2a82
009F26B0  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
009F26B4  89 4C 24 44                     mov dword ptr [rsp + 0x44], ecx
009F26B8  85 C9                           test ecx, ecx
009F26BA  0F 84 15 03 00 00               je 0x1409f29d5
009F26C0  0F 88 26 04 00 00               js 0x1409f2aec
009F26C6  49 8D 57 08                     lea rdx, [r15 + 8]
009F26CA  48 89 94 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdx
009F26D2  45 8B F5                        mov r14d, r13d
009F26D5  44 89 AC 24 48 01 00 00         mov dword ptr [rsp + 0x148], r13d
009F26DD  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
009F26E5  44 8B 7C 24 48                  mov r15d, dword ptr [rsp + 0x48]
009F26EA  4C 8B 94 24 40 01 00 00         mov r10, qword ptr [rsp + 0x140]
009F26F2  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
009F26F7  4C 8B 84 24 88 00 00 00         mov r8, qword ptr [rsp + 0x88]
009F26FF  E9 27 FE FF FF                  jmp 0x1409f252b
009F2704  45 85 FF                        test r15d, r15d
009F2707  0F 84 50 FD FF FF               je 0x1409f245d
009F270D  49 8B C5                        mov rax, r13
009F2710  48 C1 E0 03                     shl rax, 3
009F2714  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
009F271C  8B D0                           mov edx, eax
009F271E  48 8D 42 10                     lea rax, [rdx + 0x10]
009F2722  48 03 C7                        add rax, rdi
009F2725  48 3B C7                        cmp rax, rdi
009F2728  0F 82 B2 FE FF FF               jb 0x1409f25e0
009F272E  48 8B CE                        mov rcx, rsi
009F2731  48 83 E1 FC                     and rcx, 0xfffffffffffffffc
009F2735  49 03 CA                        add rcx, r10
009F2738  48 8D 47 10                     lea rax, [rdi + 0x10]
009F273C  48 03 C2                        add rax, rdx
009F273F  48 3B C1                        cmp rax, rcx
009F2742  0F 87 98 FE FF FF               ja 0x1409f25e0
009F2748  33 D2                           xor edx, edx
009F274A  E9 0E FD FF FF                  jmp 0x1409f245d
009F274F  41 83 F8 03                     cmp r8d, 3
009F2753  0F 85 C4 FC FF FF               jne 0x1409f241d
009F2759  48 8B C7                        mov rax, rdi
009F275C  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
009F2764  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
009F276C  48 8B 8C 24 70 01 00 00         mov rcx, qword ptr [rsp + 0x170]
009F2774  48 85 C9                        test rcx, rcx
009F2777  0F 84 24 07 00 00               je 0x1409f2ea1
009F277D  0F B7 01                        movzx eax, word ptr [rcx]
009F2780  66 89 84 24 58 01 00 00         mov word ptr [rsp + 0x158], ax
009F2788  66 89 84 24 A0 00 00 00         mov word ptr [rsp + 0xa0], ax
009F2790  89 54 24 74                     mov dword ptr [rsp + 0x74], edx
009F2794  66 89 54 24 70                  mov word ptr [rsp + 0x70], dx
009F2799  41 8B C1                        mov eax, r9d
009F279C  F7 D0                           not eax
009F279E  A8 04                           test al, 4
009F27A0  0F 84 77 FC FF FF               je 0x1409f241d
009F27A6  44 0F B7 71 04                  movzx r14d, word ptr [rcx + 4]
009F27AB  4C 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r14
009F27B3  4C 89 B4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r14
009F27BB  E9 5D FC FF FF                  jmp 0x1409f241d
009F27C0  41 F6 C1 20                     test r9b, 0x20
009F27C4  0F 84 25 FD FF FF               je 0x1409f24ef
009F27CA  48 8B FA                        mov rdi, rdx
009F27CD  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
009F27D2  41 8B 43 04                     mov eax, dword ptr [r11 + 4]
009F27D6  4E 8D 2C 20                     lea r13, [rax + r12]
009F27DA  45 85 FF                        test r15d, r15d
009F27DD  74 09                           je 0x1409f27e8
009F27DF  4D 3B EC                        cmp r13, r12
009F27E2  0F 82 F8 FD FF FF               jb 0x1409f25e0
009F27E8  4C 89 6C 24 60                  mov qword ptr [rsp + 0x60], r13
009F27ED  41 8B 13                        mov edx, dword ptr [r11]
009F27F0  48 89 94 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdx
009F27F8  44 8B 84 24 68 01 00 00         mov r8d, dword ptr [rsp + 0x168]
009F2800  45 33 DB                        xor r11d, r11d
009F2803  41 83 E1 02                     and r9d, 2
009F2807  4D 85 ED                        test r13, r13
009F280A  0F 84 15 02 00 00               je 0x1409f2a25
009F2810  45 85 C9                        test r9d, r9d
009F2813  0F 85 0C 02 00 00               jne 0x1409f2a25
009F2819  45 85 FF                        test r15d, r15d
009F281C  0F 84 F7 01 00 00               je 0x1409f2a19
009F2822  4D 3B EC                        cmp r13, r12
009F2825  0F 86 4D 02 00 00               jbe 0x1409f2a78
009F282B  48 8B DE                        mov rbx, rsi
009F282E  48 83 E3 FC                     and rbx, 0xfffffffffffffffc
009F2832  4A 8D 0C 13                     lea rcx, [rbx + r10]
009F2836  49 8D 45 10                     lea rax, [r13 + 0x10]
009F283A  48 3B C1                        cmp rax, rcx
009F283D  0F 87 35 02 00 00               ja 0x1409f2a78
009F2843  4C 8B B4 24 90 01 00 00         mov r14, qword ptr [rsp + 0x190]
009F284B  4D 85 F6                        test r14, r14
009F284E  74 04                           je 0x1409f2854
009F2850  66 41 89 16                     mov word ptr [r14], dx
009F2854  B8 01 00 00 00                  mov eax, 1
009F2859  40 84 F0                        test al, sil
009F285C  0F 85 D6 02 00 00               jne 0x1409f2b38
009F2862  49 8B FB                        mov rdi, r11
009F2865  45 8B 45 04                     mov r8d, dword ptr [r13 + 4]
009F2869  45 85 FF                        test r15d, r15d
009F286C  0F 84 30 02 00 00               je 0x1409f2aa2
009F2872  41 8B 4D 00                     mov ecx, dword ptr [r13]
009F2876  48 3B CF                        cmp rcx, rdi
009F2879  0F 82 61 FD FF FF               jb 0x1409f25e0
009F287F  48 2B CF                        sub rcx, rdi
009F2882  4C 2B E6                        sub r12, rsi
009F2885  49 3B CC                        cmp rcx, r12
009F2888  0F 82 EA 01 00 00               jb 0x1409f2a78
009F288E  4C 8B 94 24 40 01 00 00         mov r10, qword ptr [rsp + 0x140]
009F2896  49 3B CA                        cmp rcx, r10
009F2899  0F 87 D9 01 00 00               ja 0x1409f2a78
009F289F  45 85 C0                        test r8d, r8d
009F28A2  0F 84 D0 01 00 00               je 0x1409f2a78
009F28A8  41 8B C0                        mov eax, r8d
009F28AB  4D 3B C2                        cmp r8, r10
009F28AE  0F 87 C4 01 00 00               ja 0x1409f2a78
009F28B4  48 03 C1                        add rax, rcx
009F28B7  49 3B C2                        cmp rax, r10
009F28BA  0F 87 B8 01 00 00               ja 0x1409f2a78
009F28C0  48 8B 94 24 78 01 00 00         mov rdx, qword ptr [rsp + 0x178]
009F28C8  48 85 D2                        test rdx, rdx
009F28CB  74 26                           je 0x1409f28f3
009F28CD  45 85 FF                        test r15d, r15d
009F28D0  0F 84 9A 04 00 00               je 0x1409f2d70
009F28D6  4C 8D 0C 0B                     lea r9, [rbx + rcx]
009F28DA  4C 3B CB                        cmp r9, rbx
009F28DD  0F 82 FD FC FF FF               jb 0x1409f25e0
009F28E3  4A 8D 04 13                     lea rax, [rbx + r10]
009F28E7  4C 3B C8                        cmp r9, rax
009F28EA  0F 87 F0 FC FF FF               ja 0x1409f25e0
009F28F0  4C 89 0A                        mov qword ptr [rdx], r9
009F28F3  4C 8B 8C 24 80 01 00 00         mov r9, qword ptr [rsp + 0x180]
009F28FB  4D 85 C9                        test r9, r9
009F28FE  74 2D                           je 0x1409f292d
009F2900  45 85 FF                        test r15d, r15d
009F2903  74 25                           je 0x1409f292a
009F2905  48 85 D2                        test rdx, rdx
009F2908  74 20                           je 0x1409f292a
009F290A  48 8B 0A                        mov rcx, qword ptr [rdx]
009F290D  4A 8D 14 01                     lea rdx, [rcx + r8]
009F2911  48 3B D1                        cmp rdx, rcx
009F2914  0F 82 C6 FC FF FF               jb 0x1409f25e0
009F291A  48 83 E6 FC                     and rsi, 0xfffffffffffffffc
009F291E  49 03 F2                        add rsi, r10
009F2921  48 3B D6                        cmp rdx, rsi
009F2924  0F 87 B6 FC FF FF               ja 0x1409f25e0
009F292A  4D 89 01                        mov qword ptr [r9], r8
009F292D  41 8B DB                        mov ebx, r11d
009F2930  E9 6C 05 00 00                  jmp 0x1409f2ea1
009F2935  45 85 FF                        test r15d, r15d
009F2938  74 0F                           je 0x1409f2949
009F293A  49 63 CD                        movsxd rcx, r13d
009F293D  49 03 CB                        add rcx, r11
009F2940  49 3B CB                        cmp rcx, r11
009F2943  0F 82 97 FC FF FF               jb 0x1409f25e0
009F2949  4F 8D 1C EB                     lea r11, [r11 + r13*8]
009F294D  4C 89 9C 24 98 00 00 00         mov qword ptr [rsp + 0x98], r11
009F2955  4C 89 9C 24 90 00 00 00         mov qword ptr [rsp + 0x90], r11
009F295D  E9 21 FB FF FF                  jmp 0x1409f2483
009F2962  4D 85 ED                        test r13, r13
009F2965  0F 85 A6 FC FF FF               jne 0x1409f2611
009F296B  41 F6 C1 04                     test r9b, 4
009F296F  0F 85 E6 00 00 00               jne 0x1409f2a5b
009F2975  8B 54 24 74                     mov edx, dword ptr [rsp + 0x74]
009F2979  66 FF C2                        inc dx
009F297C  89 54 24 74                     mov dword ptr [rsp + 0x74], edx
009F2980  66 89 54 24 70                  mov word ptr [rsp + 0x70], dx
009F2985  0F B7 CA                        movzx ecx, dx
009F2988  0F BF 84 24 58 01 00 00         movsx eax, word ptr [rsp + 0x158]
009F2990  3B C8                           cmp ecx, eax
009F2992  48 8B 8C 24 70 01 00 00         mov rcx, qword ptr [rsp + 0x170]
009F299A  0F 8D 12 01 00 00               jge 0x1409f2ab2
009F29A0  0F B7 C2                        movzx eax, dx
009F29A3  44 0F B7 44 C1 04               movzx r8d, word ptr [rcx + rax*8 + 4]
009F29A9  4C 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], r8
009F29B1  4C 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r8
009F29B9  4C 8B 94 24 40 01 00 00         mov r10, qword ptr [rsp + 0x140]
009F29C1  4C 8B 9C 24 98 00 00 00         mov r11, qword ptr [rsp + 0x98]
009F29C9  44 8B 6C 24 78                  mov r13d, dword ptr [rsp + 0x78]
009F29CE  33 D2                           xor edx, edx
009F29D0  E9 22 FB FF FF                  jmp 0x1409f24f7
009F29D5  41 8B 47 04                     mov eax, dword ptr [r15 + 4]
009F29D9  44 8B 7C 24 48                  mov r15d, dword ptr [rsp + 0x48]
009F29DE  85 C0                           test eax, eax
009F29E0  0F 88 DE FB FF FF               js 0x1409f25c4
009F29E6  49 8B FB                        mov rdi, r11
009F29E9  4C 89 5C 24 68                  mov qword ptr [rsp + 0x68], r11
009F29EE  45 85 FF                        test r15d, r15d
009F29F1  0F 84 90 00 00 00               je 0x1409f2a87
009F29F7  4C 39 9C 24 80 00 00 00         cmp qword ptr [rsp + 0x80], r11
009F29FF  0F 84 DB FB FF FF               je 0x1409f25e0
009F2A05  4D 8D 2C 04                     lea r13, [r12 + rax]
009F2A09  4D 3B EC                        cmp r13, r12
009F2A0C  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
009F2A11  0F 82 C9 FB FF FF               jb 0x1409f25e0
009F2A17  EB 77                           jmp 0x1409f2a90
009F2A19  48 8B DE                        mov rbx, rsi
009F2A1C  48 83 E3 FC                     and rbx, 0xfffffffffffffffc
009F2A20  E9 1E FE FF FF                  jmp 0x1409f2843
009F2A25  48 85 FF                        test rdi, rdi
009F2A28  0F 85 08 04 00 00               jne 0x1409f2e36
009F2A2E  44 2B 44 24 7C                  sub r8d, dword ptr [rsp + 0x7c]
009F2A33  41 83 E8 01                     sub r8d, 1
009F2A37  0F 84 71 02 00 00               je 0x1409f2cae
009F2A3D  41 83 E8 01                     sub r8d, 1
009F2A41  0F 84 55 04 00 00               je 0x1409f2e9c
009F2A47  41 83 F8 01                     cmp r8d, 1
009F2A4B  0F 85 50 04 00 00               jne 0x1409f2ea1
009F2A51  BB 04 02 00 C0                  mov ebx, 0xc0000204
009F2A56  E9 46 04 00 00                  jmp 0x1409f2ea1
009F2A5B  44 8B 84 24 68 01 00 00         mov r8d, dword ptr [rsp + 0x168]
009F2A63  4C 8B 94 24 40 01 00 00         mov r10, qword ptr [rsp + 0x140]
009F2A6B  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
009F2A73  E9 8B FD FF FF                  jmp 0x1409f2803
009F2A78  4C 89 5C 24 60                  mov qword ptr [rsp + 0x60], r11
009F2A7D  E9 5E FB FF FF                  jmp 0x1409f25e0
009F2A82  E9 28 04 00 00                  jmp 0x1409f2eaf
009F2A87  4D 8D 2C 04                     lea r13, [r12 + rax]
009F2A8B  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
009F2A90  4C 89 6C 24 60                  mov qword ptr [rsp + 0x60], r13
009F2A95  E9 64 FB FF FF                  jmp 0x1409f25fe
009F2A9A  41 8B C6                        mov eax, r14d
009F2A9D  E9 0D 04 00 00                  jmp 0x1409f2eaf
009F2AA2  49 8B CB                        mov rcx, r11
009F2AA5  4C 8B 94 24 40 01 00 00         mov r10, qword ptr [rsp + 0x140]
009F2AAD  E9 0E FE FF FF                  jmp 0x1409f28c0
009F2AB2  44 38 99 04 02 00 00            cmp byte ptr [rcx + 0x204], r11b
009F2AB9  0F 85 52 FB FF FF               jne 0x1409f2611
009F2ABF  41 83 C9 20                     or r9d, 0x20
009F2AC3  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
009F2AC8  44 89 8C 24 88 01 00 00         mov dword ptr [rsp + 0x188], r9d
009F2AD0  4C 8B 94 24 40 01 00 00         mov r10, qword ptr [rsp + 0x140]
009F2AD8  4C 8B 9C 24 98 00 00 00         mov r11, qword ptr [rsp + 0x98]
009F2AE0  44 8B 6C 24 78                  mov r13d, dword ptr [rsp + 0x78]
009F2AE5  33 D2                           xor edx, edx
009F2AE7  E9 F5 F9 FF FF                  jmp 0x1409f24e1
009F2AEC  49 8D 47 F8                     lea rax, [r15 - 8]
009F2AF0  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
009F2AF8  44 38 9C 24 48 01 00 00         cmp byte ptr [rsp + 0x148], r11b
009F2B00  0F 84 C9 01 00 00               je 0x1409f2ccf
009F2B06  45 8B F5                        mov r14d, r13d
009F2B09  44 89 AC 24 48 01 00 00         mov dword ptr [rsp + 0x148], r13d
009F2B11  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
009F2B19  E9 C7 FB FF FF                  jmp 0x1409f26e5
009F2B1E  85 C9                           test ecx, ecx
009F2B20  0F 85 D9 02 00 00               jne 0x1409f2dff
009F2B26  B8 01 00 00 00                  mov eax, 1
009F2B2B  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
009F2B2F  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009F2B33  E9 67 FA FF FF                  jmp 0x1409f259f
009F2B38  4C 8B 84 24 50 01 00 00         mov r8, qword ptr [rsp + 0x150]
009F2B40  41 0F B7 40 18                  movzx eax, word ptr [r8 + 0x18]
009F2B45  B9 0B 01 00 00                  mov ecx, 0x10b
009F2B4A  66 3B C1                        cmp ax, cx
009F2B4D  0F 85 45 01 00 00               jne 0x1409f2c98
009F2B53  41 8B 80 88 00 00 00            mov eax, dword ptr [r8 + 0x88]
009F2B5A  85 C0                           test eax, eax
009F2B5C  0F 84 C8 02 00 00               je 0x1409f2e2a
009F2B62  8B C8                           mov ecx, eax
009F2B64  45 85 FF                        test r15d, r15d
009F2B67  74 16                           je 0x1409f2b7f
009F2B69  48 8D 14 19                     lea rdx, [rcx + rbx]
009F2B6D  48 3B D3                        cmp rdx, rbx
009F2B70  0F 82 6A FA FF FF               jb 0x1409f25e0
009F2B76  49 3B D4                        cmp rdx, r12
009F2B79  0F 82 61 FA FF FF               jb 0x1409f25e0
009F2B7F  48 8B FB                        mov rdi, rbx
009F2B82  49 2B FC                        sub rdi, r12
009F2B85  48 03 F9                        add rdi, rcx
009F2B88  44 8A B4 24 38 01 00 00         mov r14b, byte ptr [rsp + 0x138]
009F2B90  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
009F2B95  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009F2B99  49 8B D2                        mov rdx, r10
009F2B9C  48 8B CB                        mov rcx, rbx
009F2B9F  E8 FC 07 00 00                  call 0x1409f33a0
009F2BA4  45 33 DB                        xor r11d, r11d
009F2BA7  48 85 C0                        test rax, rax
009F2BAA  0F 84 C8 FE FF FF               je 0x1409f2a78
009F2BB0  41 8B 4D 00                     mov ecx, dword ptr [r13]
009F2BB4  3B 48 08                        cmp ecx, dword ptr [rax + 8]
009F2BB7  0F 86 A8 FC FF FF               jbe 0x1409f2865
009F2BBD  44 8B 78 0C                     mov r15d, dword ptr [rax + 0xc]
009F2BC1  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
009F2BC6  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
009F2BCA  48 8B 94 24 40 01 00 00         mov rdx, qword ptr [rsp + 0x140]
009F2BD2  48 8B CB                        mov rcx, rbx
009F2BD5  E8 C6 07 00 00                  call 0x1409f33a0
009F2BDA  45 33 F6                        xor r14d, r14d
009F2BDD  48 85 C0                        test rax, rax
009F2BE0  0F 84 D2 00 00 00               je 0x1409f2cb8
009F2BE6  44 8B 70 0C                     mov r14d, dword ptr [rax + 0xc]
009F2BEA  8A 84 24 38 01 00 00            mov al, byte ptr [rsp + 0x138]
009F2BF1  88 44 24 28                     mov byte ptr [rsp + 0x28], al
009F2BF5  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
009F2BFA  48 8B 94 24 40 01 00 00         mov rdx, qword ptr [rsp + 0x140]
009F2C02  48 8B CB                        mov rcx, rbx
009F2C05  E8 96 07 00 00                  call 0x1409f33a0
009F2C0A  4C 8B C0                        mov r8, rax
009F2C0D  45 33 DB                        xor r11d, r11d
009F2C10  44 8B 54 24 48                  mov r10d, dword ptr [rsp + 0x48]
009F2C15  48 85 C0                        test rax, rax
009F2C18  0F 84 AC 00 00 00               je 0x1409f2cca
009F2C1E  45 85 D2                        test r10d, r10d
009F2C21  74 24                           je 0x1409f2c47
009F2C23  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
009F2C26  45 8B CE                        mov r9d, r14d
009F2C29  4C 2B C9                        sub r9, rcx
009F2C2C  4C 03 CB                        add r9, rbx
009F2C2F  4C 3B CB                        cmp r9, rbx
009F2C32  0F 82 A8 F9 FF FF               jb 0x1409f25e0
009F2C38  8B 48 14                        mov ecx, dword ptr [rax + 0x14]
009F2C3B  49 03 C9                        add rcx, r9
009F2C3E  49 3B C9                        cmp rcx, r9
009F2C41  0F 82 99 F9 FF FF               jb 0x1409f25e0
009F2C47  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
009F2C4A  41 8B 50 14                     mov edx, dword ptr [r8 + 0x14]
009F2C4E  48 2B D0                        sub rdx, rax
009F2C51  48 03 D3                        add rdx, rbx
009F2C54  49 03 D6                        add rdx, r14
009F2C57  45 85 D2                        test r10d, r10d
009F2C5A  74 22                           je 0x1409f2c7e
009F2C5C  49 8B C7                        mov rax, r15
009F2C5F  41 8B 48 0C                     mov ecx, dword ptr [r8 + 0xc]
009F2C63  49 3B CF                        cmp rcx, r15
009F2C66  0F 82 74 F9 FF FF               jb 0x1409f25e0
009F2C6C  48 2B C8                        sub rcx, rax
009F2C6F  48 8B C2                        mov rax, rdx
009F2C72  49 2B C4                        sub rax, r12
009F2C75  48 3B C8                        cmp rcx, rax
009F2C78  0F 82 62 F9 FF FF               jb 0x1409f25e0
009F2C7E  41 8B 48 0C                     mov ecx, dword ptr [r8 + 0xc]
009F2C82  49 2B CF                        sub rcx, r15
009F2C85  48 2B CA                        sub rcx, rdx
009F2C88  49 03 CC                        add rcx, r12
009F2C8B  48 03 F9                        add rdi, rcx
009F2C8E  44 8B 7C 24 48                  mov r15d, dword ptr [rsp + 0x48]
009F2C93  E9 CD FB FF FF                  jmp 0x1409f2865
009F2C98  B9 0B 02 00 00                  mov ecx, 0x20b
009F2C9D  66 3B C1                        cmp ax, cx
009F2CA0  75 20                           jne 0x1409f2cc2
009F2CA2  41 8B 80 98 00 00 00            mov eax, dword ptr [r8 + 0x98]
009F2CA9  E9 AC FE FF FF                  jmp 0x1409f2b5a
009F2CAE  BB 8A 00 00 C0                  mov ebx, 0xc000008a
009F2CB3  E9 E9 01 00 00                  jmp 0x1409f2ea1
009F2CB8  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
009F2CBD  E9 1E F9 FF FF                  jmp 0x1409f25e0
009F2CC2  41 8B C3                        mov eax, r11d
009F2CC5  E9 90 FE FF FF                  jmp 0x1409f2b5a
009F2CCA  49 8B D3                        mov rdx, r11
009F2CCD  EB 88                           jmp 0x1409f2c57
009F2CCF  44 89 B4 24 48 01 00 00         mov dword ptr [rsp + 0x148], r14d
009F2CD7  45 8B EE                        mov r13d, r14d
009F2CDA  E9 32 FE FF FF                  jmp 0x1409f2b11
009F2CDF  85 C0                           test eax, eax
009F2CE1  0F 89 A5 00 00 00               jns 0x1409f2d8c
009F2CE7  44 8B C8                        mov r9d, eax
009F2CEA  41 0F BA F1 1F                  btr r9d, 0x1f
009F2CEF  4F 8D 3C 21                     lea r15, [r9 + r12]
009F2CF3  85 C9                           test ecx, ecx
009F2CF5  0F 85 A1 00 00 00               jne 0x1409f2d9c
009F2CFB  48 8B D6                        mov rdx, rsi
009F2CFE  48 83 E2 FC                     and rdx, 0xfffffffffffffffc
009F2D02  85 C9                           test ecx, ecx
009F2D04  0F 85 C9 00 00 00               jne 0x1409f2dd3
009F2D0A  49 8D 57 02                     lea rdx, [r15 + 2]
009F2D0E  49 85 D5                        test r13, rdx
009F2D11  0F 84 A7 00 00 00               je 0x1409f2dbe
009F2D17  45 0F B7 07                     movzx r8d, word ptr [r15]
009F2D1B  4C 8B AC 24 88 00 00 00         mov r13, qword ptr [rsp + 0x88]
009F2D23  49 8B CD                        mov rcx, r13
009F2D26  E8 75 EF B0 FF                  call 0x140501ca0
009F2D2B  44 8B C0                        mov r8d, eax
009F2D2E  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
009F2D32  45 33 DB                        xor r11d, r11d
009F2D35  85 C0                           test eax, eax
009F2D37  0F 85 B8 00 00 00               jne 0x1409f2df5
009F2D3D  48 83 C9 FF                     or rcx, 0xffffffffffffffff
009F2D41  48 FF C1                        inc rcx
009F2D44  66 45 39 5C 4D 00               cmp word ptr [r13 + rcx*2], r11w
009F2D4A  75 F5                           jne 0x1409f2d41
009F2D4C  41 0F B7 07                     movzx eax, word ptr [r15]
009F2D50  48 3B C8                        cmp rcx, rax
009F2D53  0F 84 9C 00 00 00               je 0x1409f2df5
009F2D59  B8 01 00 00 00                  mov eax, 1
009F2D5E  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
009F2D62  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009F2D66  44 8B 7C 24 48                  mov r15d, dword ptr [rsp + 0x48]
009F2D6B  E9 2F F8 FF FF                  jmp 0x1409f259f
009F2D70  41 8B 45 00                     mov eax, dword ptr [r13]
009F2D74  48 2B C7                        sub rax, rdi
009F2D77  48 03 C3                        add rax, rbx
009F2D7A  48 89 02                        mov qword ptr [rdx], rax
009F2D7D  E9 71 FB FF FF                  jmp 0x1409f28f3
009F2D82  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
009F2D87  E9 A2 FC FF FF                  jmp 0x1409f2a2e
009F2D8C  83 C8 FF                        or eax, 0xffffffff
009F2D8F  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
009F2D93  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009F2D97  E9 FF F7 FF FF                  jmp 0x1409f259b
009F2D9C  4D 3B FC                        cmp r15, r12
009F2D9F  72 1D                           jb 0x1409f2dbe
009F2DA1  4D 8D 47 04                     lea r8, [r15 + 4]
009F2DA5  4D 3B C4                        cmp r8, r12
009F2DA8  72 14                           jb 0x1409f2dbe
009F2DAA  48 8B D6                        mov rdx, rsi
009F2DAD  48 83 E2 FC                     and rdx, 0xfffffffffffffffc
009F2DB1  4A 8D 04 12                     lea rax, [rdx + r10]
009F2DB5  4C 3B C0                        cmp r8, rax
009F2DB8  0F 86 44 FF FF FF               jbe 0x1409f2d02
009F2DBE  41 BE 7B 00 00 C0               mov r14d, 0xc000007b
009F2DC4  44 89 74 24 4C                  mov dword ptr [rsp + 0x4c], r14d
009F2DC9  44 8B 7C 24 48                  mov r15d, dword ptr [rsp + 0x48]
009F2DCE  E9 C8 F7 FF FF                  jmp 0x1409f259b
009F2DD3  41 0F B7 0F                     movzx ecx, word ptr [r15]
009F2DD7  48 83 C1 02                     add rcx, 2
009F2DDB  49 8D 0C 4C                     lea rcx, [r12 + rcx*2]
009F2DDF  49 03 C9                        add rcx, r9
009F2DE2  49 3B CC                        cmp rcx, r12
009F2DE5  72 D7                           jb 0x1409f2dbe
009F2DE7  4A 8D 04 12                     lea rax, [rdx + r10]
009F2DEB  48 3B C8                        cmp rcx, rax
009F2DEE  77 CE                           ja 0x1409f2dbe
009F2DF0  E9 15 FF FF FF                  jmp 0x1409f2d0a
009F2DF5  44 8B 7C 24 48                  mov r15d, dword ptr [rsp + 0x48]
009F2DFA  E9 97 F7 FF FF                  jmp 0x1409f2596
009F2DFF  8B 02                           mov eax, dword ptr [rdx]
009F2E01  49 85 C5                        test r13, rax
009F2E04  0F 85 1C FD FF FF               jne 0x1409f2b26
009F2E0A  41 BE 7B 00 00 C0               mov r14d, 0xc000007b
009F2E10  44 89 74 24 4C                  mov dword ptr [rsp + 0x4c], r14d
009F2E15  E9 81 F7 FF FF                  jmp 0x1409f259b
009F2E1A  44 8B F3                        mov r14d, ebx
009F2E1D  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
009F2E21  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
009F2E25  E9 82 F7 FF FF                  jmp 0x1409f25ac
009F2E2A  4C 89 5C 24 60                  mov qword ptr [rsp + 0x60], r11
009F2E2F  BB 89 00 00 C0                  mov ebx, 0xc0000089
009F2E34  EB 6B                           jmp 0x1409f2ea1
009F2E36  45 85 C9                        test r9d, r9d
009F2E39  0F 84 EF FB FF FF               je 0x1409f2a2e
009F2E3F  45 85 FF                        test r15d, r15d
009F2E42  74 20                           je 0x1409f2e64
009F2E44  48 8D 4F 18                     lea rcx, [rdi + 0x18]
009F2E48  48 3B CF                        cmp rcx, rdi
009F2E4B  72 0D                           jb 0x1409f2e5a
009F2E4D  48 83 E6 FC                     and rsi, 0xfffffffffffffffc
009F2E51  4A 8D 04 16                     lea rax, [rsi + r10]
009F2E55  48 3B C8                        cmp rcx, rax
009F2E58  76 0E                           jbe 0x1409f2e68
009F2E5A  4C 89 5C 24 68                  mov qword ptr [rsp + 0x68], r11
009F2E5F  E9 7C F7 FF FF                  jmp 0x1409f25e0
009F2E64  48 83 E6 FC                     and rsi, 0xfffffffffffffffc
009F2E68  48 8B 8C 24 78 01 00 00         mov rcx, qword ptr [rsp + 0x178]
009F2E70  48 85 C9                        test rcx, rcx
009F2E73  0F 84 B4 FA FF FF               je 0x1409f292d
009F2E79  45 85 FF                        test r15d, r15d
009F2E7C  74 16                           je 0x1409f2e94
009F2E7E  48 3B FE                        cmp rdi, rsi
009F2E81  0F 82 59 F7 FF FF               jb 0x1409f25e0
009F2E87  4A 8D 04 16                     lea rax, [rsi + r10]
009F2E8B  48 3B F8                        cmp rdi, rax
009F2E8E  0F 87 4C F7 FF FF               ja 0x1409f25e0
009F2E94  48 89 39                        mov qword ptr [rcx], rdi
009F2E97  E9 91 FA FF FF                  jmp 0x1409f292d
009F2E9C  BB 8B 00 00 C0                  mov ebx, 0xc000008b
009F2EA1  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
009F2EA5  EB 06                           jmp 0x1409f2ead
009F2EA7  8B D8                           mov ebx, eax
009F2EA9  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
009F2EAD  8B C3                           mov eax, ebx
009F2EAF  48 81 C4 F0 00 00 00            add rsp, 0xf0
009F2EB6  41 5F                           pop r15
009F2EB8  41 5E                           pop r14
009F2EBA  41 5D                           pop r13
009F2EBC  41 5C                           pop r12
009F2EBE  5F                              pop rdi
009F2EBF  5E                              pop rsi
009F2EC0  5B                              pop rbx
009F2EC1  C3                              ret
009F2EC2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LdrpResSearchResourceInsideDirectory(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned __int16 a6, __int64 a7, unsigned int a8, __int64 a9, __int64 a10, __int64 a11, unsigned int a12, __int64 a13)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int16 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned __int16 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;
    unsigned __int8 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int16 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p60;

    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (240);
    v_rbx = 0;
    v_stack_mE4 = 0;
    v_stack_mD8 = 0;
    *(unsigned __int16 *)(v_rsp + 48) = 0;
    v_stack_mB4 = 0;
    if (a4 == 0) goto loc_009F23A6;
    if (a5 == 0) goto loc_009F23A6;
    if (a7 == 0) goto loc_009F23A6;
    if (((unsigned int)((unsigned int)(a8) - 1)) > 3) goto loc_009F23A6;
    v_stack_mD4 = (unsigned int)((unsigned int)(a12));
    if (((unsigned int)((unsigned int)(a8) - 1)) < 3) goto loc_009F23A6;
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a12)))) & (0x1000ULL));
    v_stack_mE0 = (unsigned int)(v_r15);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a12)))) & ((unsigned int)((unsigned int)(0x8800ULL))));
    if ((unsigned int)(v_r15) == 0) goto loc_009F2399;
    if (a3 == 0) goto loc_009F23A6;
loc_009F2399:
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x8800ULL)))) goto loc_009F23A6;
    if (a1 == 0) goto loc_009F23A6;
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x8800ULL)))) goto loc_009F23B0;
loc_009F23A6:
    goto loc_009F2EAF;
loc_009F23B0:
    v_stack_mAC = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a8))));
    v_stack_mD0 = 0;
    v_stack_mA8 = 0;
    if (a13 != 0) {
        *(unsigned __int16 *)(a13) = 0;
    }
loc_009F23E0:
    if (a4 == 0) goto loc_009F2800;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a8)))) - 1);
    v_stack_mAC = (unsigned int)(a1);
    v_stack_m68 = (unsigned int)(a1);
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a8)))))) == 0) goto loc_009F2800;
    v_stack_mA0 = *(unsigned __int64 *)(a7);
    v_stack_m80 = *(unsigned __int64 *)(a7);
    a2 = 0;
    if ((unsigned int)(a1) == 0) goto loc_009F274F;
loc_009F241D:
    if ((unsigned int)(v_r15) == 0) goto loc_009F2442;
    if ((a4 + 24) < a4) goto loc_009F25E0;
    result = (a1) & (-4);
    result = (result) + (a3);
    if ((a4 + 24) > result) goto loc_009F25E0;
loc_009F2442:
    v_stack_mB0 = (unsigned int)(*(unsigned __int16 *)(a4 + 12));
    v_stack_p20 = (unsigned int)(*(unsigned __int16 *)(a4 + 12));
    if ((unsigned int)(*(unsigned __int16 *)(a4 + 12)) != 0) goto loc_009F2704;
loc_009F245D:
    v_stack_m90 = a4 + 16;
    v_stack_m98 = a4 + 16;
    if (((*(unsigned __int64 *)(a7)) & (0xFFFFFFFFFFFF0000ULL)) != 0) goto loc_009F24D8;
    if ((unsigned int)(*(unsigned __int16 *)(a4 + 12)) != 0) goto loc_009F2935;
loc_009F2483:
    v_stack_mB0 = (unsigned int)(*(unsigned __int16 *)(a4 + 14));
    v_stack_p20 = (unsigned int)(*(unsigned __int16 *)(a4 + 14));
    if ((unsigned int)(v_r15) == 0) goto loc_009F24D8;
    result = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(a4 + 14)))) << (3);
    v_stack_m58 = result;
    if (result > ((unsigned int)(0xFFFFFFFFULL))) goto loc_009F25E0;
    a1 = ((unsigned int)((unsigned int)(result))) + (a4 + 16);
    if (a1 < (a4 + 16)) goto loc_009F25E0;
    result = (a1) & (-4);
    result = (result) + (a3);
    if (a1 > result) goto loc_009F25E0;
loc_009F24D8:
    if ((unsigned int)(*(unsigned __int16 *)(a4 + 14)) == 0) goto loc_009F2D82;
loc_009F24E1:
    if (v_stack_mA8 != 0) goto loc_009F27C0;
loc_009F24EF:
loc_009F24F7:
    v_stack_mC0 = 0;
    v_stack_m98 = a4 + 16;
    v_r11 = (a4 + 16) - (8);
    v_stack_m70 = v_r11 + (int)((unsigned int)(*(unsigned __int16 *)(a4 + 14))) * 8;
    v_stack_p20 = (unsigned int)(*(unsigned __int16 *)(a4 + 14));
    v_r11 = 0;
loc_009F252B:
    if ((a4 + 16) > (v_r11 + (int)((unsigned int)(*(unsigned __int16 *)(a4 + 14))) * 8)) goto loc_009F25F9;
    v_r13 = (unsigned int)((*(unsigned __int16 *)(a4 + 14)) >> (1));
    if (condition_is_not_equal) goto loc_009F264E;
    if ((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int16 *)(a4 + 14)))) == 0) goto loc_009F25F9;
    v_stack_mDC = 0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a12)))) & (0x1000ULL));
    if (a4 + 16 == 0) goto loc_009F2E1A;
    v_stack_mDC = 0;
    if (((0xFFFFFFFFFFFF0000ULL) & (v_stack_mA0)) != 0) goto loc_009F2CDF;
    if (sign_flag) goto loc_009F2B1E;
    if ((unsigned int)(a1) == 0) goto loc_009F258E;
    if (((0xFFFFFFFFFFFF0000ULL) & ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))))) != 0) goto loc_009F2E0A;
loc_009F258E:
    a3 = (unsigned int)((v_stack_mA0) - (*(unsigned int *)(a4 + 16)));
    v_stack_mE4 = (unsigned int)(a3);
loc_009F2596:
    v_stack_mD8 = (unsigned int)(a3);
loc_009F259B:
loc_009F259F:
    v_stack_mE8 = 0;
loc_009F25AC:
    if (sign_flag) goto loc_009F2A9A;
    if ((unsigned int)((unsigned int)(v_stack_mE4)) != 0) goto loc_009F25F9;
    if (!sign_flag) goto loc_009F29EE;
loc_009F25C4:
    if ((unsigned int)(v_r15) == 0) goto loc_009F25EA;
    if (v_stack_mA8 != 0) goto loc_009F25E0;
    if (((unsigned int)(*(unsigned int *)(v_stack_m98 + 4)) + a4 * 1) >= a4) goto loc_009F25F4;
loc_009F25E0:
    goto loc_009F2EA1;
loc_009F25EA:
    v_rdi = ((unsigned int)(*(unsigned int *)(v_stack_m98 + 4))) + (a4);
loc_009F25F4:
    v_stack_mC0 = v_rdi;
loc_009F25F9:
loc_009F25FE:
    if (v_stack_mA8 != 0) goto loc_009F2962;
loc_009F2611:
    v_r11 = (a7) + (8);
    v_stack_p38 = v_r11;
    v_stack_m48 = v_r11;
    goto loc_009F23E0;
loc_009F264E:
    v_stack_m78 = v_stack_mA0;
    v_r14 = (unsigned __int8)((0) & (1));
    v_stack_p20 = (unsigned __int8)(v_r14);
    result = (int)((unsigned int)(v_stack_mD0));
    if (!(condition_is_not_equal)) {
        result = (int)((unsigned int)(v_stack_mD0 - 1));
    }
    v_stack_m78 = v_stack_mA0 + result * 8;
    v_stack_mF0 = v_stack_mD8;
    v_stack_mF8 = (unsigned int)((unsigned int)(v_stack_mD4));
    v_stack_m100 = v_stack_mA0 + result * 8;
    v_stack_m108 = a4;
    result = LdrpResCompareResourceNames(a1, v_stack_mA0, v_stack_p18, (unsigned int)(a8));
    v_stack_mE8 = (unsigned int)(result);
    v_r11 = 0;
    if (sign_flag) goto loc_009F2A82;
    v_stack_mE4 = (unsigned int)((unsigned int)(v_stack_mD8));
    if ((unsigned int)((unsigned int)(v_stack_mD8)) == 0) goto loc_009F29D5;
    if (sign_flag) goto loc_009F2AEC;
    v_stack_m98 = v_stack_mA0 + result * 8 + 8;
    v_stack_p20 = (unsigned int)(v_stack_mD0);
loc_009F26E5:
    goto loc_009F252B;
loc_009F2704:
    if ((unsigned int)((unsigned int)(v_stack_mE0)) == 0) goto loc_009F245D;
    result = (v_stack_mD0) << (3);
    v_stack_m90 = result;
    result = ((unsigned int)((unsigned int)(result)) + 16) + (v_rdi);
    if (result < v_rdi) goto loc_009F25E0;
    a1 = (a1) & (-4);
    a1 = (a1) + (v_stack_p18);
    result = (v_rdi + 16) + ((unsigned int)((unsigned int)(result)));
    if (result > a1) goto loc_009F25E0;
    a2 = 0;
    goto loc_009F245D;
loc_009F274F:
    if (((unsigned int)(v_stack_mA0)) != 3) goto loc_009F241D;
    v_stack_mA8 = v_rdi;
    v_stack_m60 = v_rdi;
    if (a9 == 0) goto loc_009F2EA1;
    v_stack_p30 = (unsigned __int16)(*(unsigned __int16 *)(a9));
    v_stack_m88 = (unsigned __int16)(*(unsigned __int16 *)(a9));
    v_stack_mB4 = 0;
    v_stack_mB8 = 0;
    result = (unsigned int)(~((unsigned int)((unsigned int)((unsigned int)(v_stack_mD4)))));
    if ((((unsigned __int8)(result)) & (4)) == 0) goto loc_009F241D;
    v_stack_mA0 = *(unsigned __int16 *)(a9 + 4);
    v_stack_m80 = *(unsigned __int16 *)(a9 + 4);
    goto loc_009F241D;
loc_009F27C0:
    if ((((unsigned __int8)((unsigned int)(v_stack_mD4))) & (32)) == 0) goto loc_009F24EF;
    v_stack_mC0 = 0;
    if ((unsigned int)((unsigned int)(v_stack_mE0)) == 0) goto loc_009F27E8;
    if (((unsigned int)(*(unsigned int *)(v_r11 + 4)) + a4 * 1) < a4) goto loc_009F25E0;
loc_009F27E8:
    v_stack_mC8 = (unsigned int)(*(unsigned int *)(v_r11 + 4)) + a4 * 1;
    v_stack_m80 = (unsigned int)(*(unsigned int *)(v_r11));
loc_009F2800:
    v_r11 = 0;
loc_009F2803:
    a4 = (unsigned int)(((unsigned int)(v_stack_mD4)) & (2));
    if ((unsigned int)(*(unsigned int *)(v_r11 + 4)) + a4 * 1 == 0) goto loc_009F2A25;
    if ((unsigned int)(a4) != 0) goto loc_009F2A25;
    if ((unsigned int)((unsigned int)(v_stack_mE0)) == 0) goto loc_009F2A19;
    if (((unsigned int)(*(unsigned int *)(v_r11 + 4)) + a4 * 1) <= a4) goto loc_009F2A78;
    v_rbx = (a1) & (-4);
    if (((unsigned int)(*(unsigned int *)(v_r11 + 4)) + a4 * 1 + 16) > (v_rbx + v_stack_p18 * 1)) goto loc_009F2A78;
loc_009F2843:
    if (a13 != 0) {
        *(unsigned __int16 *)(a13) = (unsigned __int16)((unsigned int)(*(unsigned int *)(v_r11)));
    }
    if (((1) & ((unsigned __int8)(a1))) != 0) goto loc_009F2B38;
loc_009F2865:
    if ((unsigned int)((unsigned int)(v_stack_mE0)) == 0) goto loc_009F2AA2;
    if (((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_r11 + 4)) + a4 * 1))) < 0) goto loc_009F25E0;
    a1 = ((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_r11 + 4)) + a4 * 1))) - (0);
    v_r12 = (a4) - (a1);
    if (a1 < v_r12) goto loc_009F2A78;
    if (a1 > v_stack_p18) goto loc_009F2A78;
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_r11 + 4)) + a4 * 1 + 4))) == 0) goto loc_009F2A78;
    if (((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_r11 + 4)) + a4 * 1 + 4))) > v_stack_p18) goto loc_009F2A78;
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_r11 + 4)) + a4 * 1 + 4))))) + (a1);
    if (result > v_stack_p18) goto loc_009F2A78;
loc_009F28C0:
    if (a10 == 0) goto loc_009F28F3;
    if ((unsigned int)((unsigned int)(v_stack_mE0)) == 0) goto loc_009F2D70;
    if ((v_rbx + a1 * 1) < v_rbx) goto loc_009F25E0;
    if ((v_rbx + a1 * 1) > (v_rbx + v_stack_p18 * 1)) goto loc_009F25E0;
    *(unsigned __int64 *)(a10) = v_rbx + a1 * 1;
loc_009F28F3:
    if (a11 == 0) goto loc_009F292D;
    if ((unsigned int)((unsigned int)(v_stack_mE0)) == 0) goto loc_009F292A;
    if (a10 == 0) goto loc_009F292A;
    if ((*(unsigned __int64 *)(a10) + (unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_r11 + 4)) + a4 * 1 + 4)) * 1) < (*(unsigned __int64 *)(a10))) goto loc_009F25E0;
    v_rsi = (a1) & (-4);
    v_rsi = (v_rsi) + (v_stack_p18);
    if ((*(unsigned __int64 *)(a10) + (unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_r11 + 4)) + a4 * 1 + 4)) * 1) > v_rsi) goto loc_009F25E0;
loc_009F292A:
    *(unsigned __int64 *)(a11) = (unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_r11 + 4)) + a4 * 1 + 4));
loc_009F292D:
    goto loc_009F2EA1;
loc_009F2935:
    if ((unsigned int)((unsigned int)(v_stack_mE0)) == 0) goto loc_009F2949;
    a1 = ((int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 4)) + a4 * 1))) + (0);
    if (a1 < 0) goto loc_009F25E0;
loc_009F2949:
    v_stack_m90 = v_r11 + (unsigned int)(*(unsigned int *)(v_r11 + 4)) + a4 * 1 * 8;
    v_stack_m98 = v_r11 + (unsigned int)(*(unsigned int *)(v_r11 + 4)) + a4 * 1 * 8;
    goto loc_009F2483;
loc_009F2962:
    if ((unsigned int)(*(unsigned int *)(v_r11 + 4)) + a4 * 1 != 0) goto loc_009F2611;
    if ((((unsigned __int8)(a11)) & (4)) != 0) goto loc_009F2A5B;
    a2 = (unsigned __int16)(((unsigned int)(v_stack_mB4)) + 1);
    v_stack_mB4 = (unsigned int)(a2);
    v_stack_mB8 = (unsigned __int16)(a2);
    if (((unsigned int)((unsigned __int16)(a2))) >= ((unsigned int)((__int16)(a6)))) goto loc_009F2AB2;
    v_stack_mA0 = *(unsigned __int16 *)(a9 + (unsigned __int16)(a2) * 8 + 4);
    v_stack_m80 = *(unsigned __int16 *)(a9 + (unsigned __int16)(a2) * 8 + 4);
    a2 = 0;
    goto loc_009F24F7;
loc_009F29D5:
    if (sign_flag) goto loc_009F25C4;
    v_stack_mC0 = v_stack_m90;
loc_009F29EE:
    if ((unsigned int)((unsigned int)(v_stack_mE0)) == 0) goto loc_009F2A87;
    if (v_stack_mA8 == v_stack_m90) goto loc_009F25E0;
    v_stack_mD0 = v_r12 + (unsigned int)(*(unsigned int *)((unsigned int)(v_stack_mE0) + 4)) * 1;
    if ((v_r12 + (unsigned int)(*(unsigned int *)((unsigned int)(v_stack_mE0) + 4)) * 1) < v_r12) goto loc_009F25E0;
    goto loc_009F2A90;
loc_009F2A19:
    v_rbx = (v_rsi) & (-4);
    goto loc_009F2843;
loc_009F2A25:
    if (v_stack_m90 != 0) goto loc_009F2E36;
loc_009F2A2E:
    a3 = (unsigned int)((*(unsigned __int16 *)(a9 + (unsigned __int16)(a2) * 8 + 4)) - (v_stack_mAC));
    a3 = (unsigned int)((a3) - (1));
    if (condition_is_equal) goto loc_009F2CAE;
    a3 = (unsigned int)((a3) - (1));
    if (condition_is_equal) goto loc_009F2E9C;
    if (((unsigned int)(a3)) != 1) goto loc_009F2EA1;
    goto loc_009F2EA1;
loc_009F2A5B:
    goto loc_009F2803;
loc_009F2A78:
    v_stack_mC8 = v_stack_m90;
    goto loc_009F25E0;
loc_009F2A82:
    goto loc_009F2EAF;
loc_009F2A87:
    v_stack_mD0 = v_r12 + (unsigned int)(*(unsigned int *)((unsigned int)(v_stack_mE0) + 4)) * 1;
loc_009F2A90:
    v_stack_mC8 = v_r12 + (unsigned int)(*(unsigned int *)((unsigned int)(v_stack_mE0) + 4)) * 1;
    goto loc_009F25FE;
loc_009F2A9A:
    goto loc_009F2EAF;
loc_009F2AA2:
    goto loc_009F28C0;
loc_009F2AB2:
    if ((*(unsigned __int8 *)(v_stack_m90 + 516)) != ((unsigned __int8)(v_stack_m90))) goto loc_009F2611;
    a4 = (unsigned int)((a11) | (32));
    v_stack_mD4 = (unsigned int)(a4);
    v_stack_p60 = (unsigned int)(a4);
    a2 = 0;
    goto loc_009F24E1;
loc_009F2AEC:
    v_stack_m70 = (unsigned int)(v_stack_mE0) - 8;
    if (v_stack_p20 == ((unsigned __int8)(v_stack_m90))) goto loc_009F2CCF;
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_mB0));
loc_009F2B11:
    goto loc_009F26E5;
loc_009F2B1E:
    if ((unsigned int)(v_stack_m90) != 0) goto loc_009F2DFF;
loc_009F2B26:
    v_stack_mE4 = 1;
    v_stack_mD8 = 1;
    goto loc_009F259F;
loc_009F2B38:
    if (((unsigned __int16)(*(unsigned __int16 *)(a5 + 24))) != 267) goto loc_009F2C98;
loc_009F2B5A:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 136))) == 0) goto loc_009F2E2A;
    if ((unsigned int)((unsigned int)(v_stack_mE0)) == 0) goto loc_009F2B7F;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 136)))) + (unsigned int)(0xC0000204ULL) * 1) < ((unsigned int)(0xC0000204ULL))) goto loc_009F25E0;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 136)))) + (unsigned int)(0xC0000204ULL) * 1) < v_r12) goto loc_009F25E0;
loc_009F2B7F:
    v_rdi = ((unsigned int)(0xC0000204ULL)) - (v_r12);
    v_rdi = (v_rdi) + ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 136)))));
    v_stack_m100 = (unsigned __int8)(v_stack_p10);
    v_stack_m108 = (unsigned int)((unsigned int)(*(unsigned int *)(a5 + 136)));
    result = LdrpSectionTableFromVirtualAddress((unsigned int)(0xC0000204ULL), v_stack_p18, a5, a4);
    v_r11 = 0;
    if (result == 0) goto loc_009F2A78;
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_mB0))))) <= (*(unsigned int *)(result + 8))) goto loc_009F2865;
    v_stack_m100 = (unsigned __int8)(v_stack_p10);
    v_stack_m108 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_mB0))));
    result = LdrpSectionTableFromVirtualAddress((unsigned int)(0xC0000204ULL), v_stack_p18, a5, a4);
    v_r14 = 0;
    if (result == 0) goto loc_009F2CB8;
    v_stack_m100 = (unsigned __int8)(v_stack_p10);
    v_stack_m108 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 12)));
    result = LdrpSectionTableFromVirtualAddress((unsigned int)(0xC0000204ULL), v_stack_p18, a5, a4);
    v_r11 = 0;
    if (result == 0) goto loc_009F2CCA;
    if ((unsigned int)((unsigned int)(v_stack_mE0)) == 0) goto loc_009F2C47;
    a4 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 12))))) - ((unsigned int)(*(unsigned int *)(result + 12)));
    a4 = (a4) + ((unsigned int)(0xC0000204ULL));
    if (a4 < ((unsigned int)(0xC0000204ULL))) goto loc_009F25E0;
    a1 = ((unsigned int)(*(unsigned int *)(result + 20))) + (a4);
    if (a1 < a4) goto loc_009F25E0;
loc_009F2C47:
    a2 = ((unsigned int)(*(unsigned int *)(result + 20))) - ((unsigned int)(*(unsigned int *)(result + 12)));
    a2 = (a2) + ((unsigned int)(0xC0000204ULL));
    a2 = (a2) + ((unsigned int)(*(unsigned int *)(result + 12)));
loc_009F2C57:
    if ((unsigned int)((unsigned int)(v_stack_mE0)) == 0) goto loc_009F2C7E;
    if (((unsigned int)(*(unsigned int *)(result + 12))) < ((unsigned int)(*(unsigned int *)(result + 12)))) goto loc_009F25E0;
    a1 = ((unsigned int)(*(unsigned int *)(result + 12))) - ((unsigned int)(*(unsigned int *)(result + 12)));
    result = (a2) - (v_r12);
    if (a1 < result) goto loc_009F25E0;
loc_009F2C7E:
    a1 = ((unsigned int)(*(unsigned int *)(result + 12))) - ((unsigned int)(*(unsigned int *)(result + 12)));
    a1 = (a1) - (a2);
    a1 = (a1) + (v_r12);
    v_rdi = (v_rdi) + (a1);
    goto loc_009F2865;
loc_009F2C98:
    if (((unsigned __int16)(result)) != 523) goto loc_009F2CC2;
    goto loc_009F2B5A;
loc_009F2CAE:
    goto loc_009F2EA1;
loc_009F2CB8:
    v_stack_mC8 = (unsigned int)(*(unsigned int *)(result + 12));
    goto loc_009F25E0;
loc_009F2CC2:
    goto loc_009F2B5A;
loc_009F2CCA:
    goto loc_009F2C57;
loc_009F2CCF:
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 12)));
    goto loc_009F2B11;
loc_009F2CDF:
    if (!sign_flag) goto loc_009F2D8C;
    if (523 != 0) goto loc_009F2D9C;
    a2 = (v_rsi) & (-4);
loc_009F2D02:
    if (523 != 0) goto loc_009F2DD3;
loc_009F2D0A:
    if ((((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 12))))) & (0 + v_r12 * 1 + 2)) == 0) goto loc_009F2DBE;
    result = wcsncmp(v_stack_mA0, 0 + v_r12 * 1 + 2, *(unsigned __int16 *)(0 + v_r12 * 1), 0);
    v_stack_mE4 = (unsigned int)(result);
    v_r11 = 0;
    if ((unsigned int)(result) != 0) goto loc_009F2DF5;
    a1 = (v_stack_mA0) | (-1);
loc_009F2D41:
    a1 = (a1) + 1;
    if ((*(unsigned __int16 *)(v_stack_mA0 + a1 * 2)) != 0) goto loc_009F2D41;
    if (a1 == (*(unsigned __int16 *)(0 + v_r12 * 1))) goto loc_009F2DF5;
    v_stack_mE4 = 1;
    v_stack_mD8 = 1;
    goto loc_009F259F;
loc_009F2D70:
    result = ((unsigned int)(*(unsigned int *)(v_stack_mA0))) - (v_rdi);
    result = (result) + ((unsigned int)(0xC000008AULL));
    *(unsigned __int64 *)(0 + v_r12 * 1 + 2) = result;
    goto loc_009F28F3;
loc_009F2D82:
    v_stack_mC0 = 0 + v_r12 * 1 + 2;
    goto loc_009F2A2E;
loc_009F2D8C:
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    v_stack_mE4 = (unsigned int)(result);
    v_stack_mD8 = (unsigned int)(result);
    goto loc_009F259B;
loc_009F2D9C:
    if (((unsigned int)(v_stack_mE0)) < v_r12) goto loc_009F2DBE;
    if (((unsigned int)(v_stack_mE0) + 4) < v_r12) goto loc_009F2DBE;
    a2 = (v_rsi) & (-4);
    if (((unsigned int)(v_stack_mE0) + 4) <= (a2 + (unsigned int)(v_stack_mE0) * 1)) goto loc_009F2D02;
loc_009F2DBE:
    v_stack_mDC = (unsigned int)((unsigned int)(0xC000007BULL));
    goto loc_009F259B;
loc_009F2DD3:
    a1 = (*(unsigned __int16 *)((unsigned int)(v_stack_mE0))) + (2);
    a1 = (v_r12 + a1 * 2) + (0);
    if (a1 < v_r12) goto loc_009F2DBE;
    if (a1 > (a2 + (unsigned int)(v_stack_mE0) * 1)) goto loc_009F2DBE;
    goto loc_009F2D0A;
loc_009F2DF5:
    goto loc_009F2596;
loc_009F2DFF:
    if (((v_stack_mA0) & ((unsigned int)(*(unsigned int *)(a2)))) != 0) goto loc_009F2B26;
loc_009F2E0A:
    v_stack_mDC = (unsigned int)((unsigned int)(0xC000007BULL));
    goto loc_009F259B;
loc_009F2E1A:
    v_stack_mE8 = (unsigned int)((unsigned int)(0xC000008AULL));
    goto loc_009F25AC;
loc_009F2E2A:
    v_stack_mC8 = 0;
    goto loc_009F2EA1;
loc_009F2E36:
    if (0 == 0) goto loc_009F2A2E;
    if ((unsigned int)((unsigned int)(v_stack_mE0)) == 0) goto loc_009F2E64;
    if ((v_rdi + 24) < v_rdi) goto loc_009F2E5A;
    v_rsi = (v_rsi) & (-4);
    if ((v_rdi + 24) <= (v_rsi + (unsigned int)(v_stack_mE0) * 1)) goto loc_009F2E68;
loc_009F2E5A:
    v_stack_mC0 = 0;
    goto loc_009F25E0;
loc_009F2E64:
    v_rsi = (v_rsi) & (-4);
loc_009F2E68:
    if (a10 == 0) goto loc_009F292D;
    if ((unsigned int)((unsigned int)(v_stack_mE0)) == 0) goto loc_009F2E94;
    if (v_rdi < v_rsi) goto loc_009F25E0;
    if (v_rdi > (v_rsi + (unsigned int)(v_stack_mE0) * 1)) goto loc_009F25E0;
loc_009F2E94:
    *(unsigned __int64 *)(a10) = v_rdi;
    goto loc_009F292D;
loc_009F2E9C:
loc_009F2EA1:
    v_stack_mE8 = (unsigned int)((unsigned int)(0xC000008BULL));
    goto loc_009F2EAD;
loc_009F2EAD:
loc_009F2EAF:
    v_rsp = (v_rsp) + (240);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000008BULL)));
}
```

## 5. (Beta) C Style

```c
int64_t LdrpResSearchResourceInsideDirectory(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, void *Arg5, uint16_t Arg6, int64_t Arg7, void *Arg8, void *Arg9, int64_t Arg10, int64_t Arg11, uint32_t Arg12, int64_t Arg13)
{
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg8 = (uint8_t *)Arg8;
    uint8_t *arg9 = (uint8_t *)Arg9;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint16_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint16_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;
    uint8_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint16_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p60;

    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (240);
    local_rbx = 0;
    v_stack_mE4 = 0;
    v_stack_mD8 = 0;
    *(uint16_t *)(local_rsp + 0x30) = 0;
    v_stack_mB4 = 0;
    if (Arg4 == NULL) goto loc_009F23A6;
    if (Arg5 == NULL) goto loc_009F23A6;
    if (Arg7 == 0) goto loc_009F23A6;
    if (((uint32_t)((uint32_t)(Arg8) - 1)) > 3) goto loc_009F23A6;
    v_stack_mD4 = (uint32_t)((uint32_t)(Arg12));
    if (((uint32_t)((uint32_t)(Arg8) - 1)) < 3) goto loc_009F23A6;
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg12)))) & (0x1000ULL));
    v_stack_mE0 = (uint32_t)(local_r15);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg12)))) & ((uint32_t)((uint32_t)(0x8800ULL))));
    if ((uint32_t)(local_r15) == 0) goto loc_009F2399;
    if (Arg3 == 0) goto loc_009F23A6;
loc_009F2399:
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x8800ULL)))) goto loc_009F23A6;
    if (Arg1 == 0) goto loc_009F23A6;
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x8800ULL)))) goto loc_009F23B0;
loc_009F23A6:
    goto loc_009F2EAF;
loc_009F23B0:
    v_stack_mAC = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg8))));
    v_stack_mD0 = 0;
    v_stack_mA8 = 0;
    if (Arg13 != 0) {
        *(uint16_t *)(Arg13) = 0;
    }
loc_009F23E0:
    if (Arg4 == NULL) goto loc_009F2800;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg8)))) - 1);
    v_stack_mAC = (uint32_t)(Arg1);
    v_stack_m68 = (uint32_t)(Arg1);
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg8)))))) == 0) goto loc_009F2800;
    v_stack_mA0 = *(uint64_t *)(Arg7);
    v_stack_m80 = *(uint64_t *)(Arg7);
    Arg2 = 0;
    if ((uint32_t)(Arg1) == 0) goto loc_009F274F;
loc_009F241D:
    if ((uint32_t)(local_r15) == 0) goto loc_009F2442;
    if ((Arg4 + 24) < Arg4) goto loc_009F25E0;
    result = (Arg1) & (-4);
    result = (result) + (Arg3);
    if ((Arg4 + 24) > result) goto loc_009F25E0;
loc_009F2442:
    v_stack_mB0 = (uint32_t)(*(uint16_t *)(arg4 + 0xC));
    v_stack_p20 = (uint32_t)(*(uint16_t *)(arg4 + 0xC));
    if ((uint32_t)(*(uint16_t *)(arg4 + 0xC)) != 0) goto loc_009F2704;
loc_009F245D:
    v_stack_m90 = Arg4 + 16;
    v_stack_m98 = Arg4 + 16;
    if (((*(uint64_t *)(Arg7)) & (0xFFFFFFFFFFFF0000ULL)) != 0) goto loc_009F24D8;
    if ((uint32_t)(*(uint16_t *)(arg4 + 0xC)) != 0) goto loc_009F2935;
loc_009F2483:
    v_stack_mB0 = (uint32_t)(*(uint16_t *)(arg4 + 0xE));
    v_stack_p20 = (uint32_t)(*(uint16_t *)(arg4 + 0xE));
    if ((uint32_t)(local_r15) == 0) goto loc_009F24D8;
    result = ((uint32_t)((uint32_t)(*(uint16_t *)(arg4 + 0xE)))) << (3);
    v_stack_m58 = result;
    if (result > ((uint32_t)(0xFFFFFFFFULL))) goto loc_009F25E0;
    Arg1 = ((uint32_t)((uint32_t)(result))) + (Arg4 + 16);
    if (Arg1 < (Arg4 + 16)) goto loc_009F25E0;
    result = (Arg1) & (-4);
    result = (result) + (Arg3);
    if (Arg1 > result) goto loc_009F25E0;
loc_009F24D8:
    if ((uint32_t)(*(uint16_t *)(arg4 + 0xE)) == 0) goto loc_009F2D82;
loc_009F24E1:
    if (v_stack_mA8 != 0) goto loc_009F27C0;
loc_009F24EF:
loc_009F24F7:
    v_stack_mC0 = 0;
    v_stack_m98 = Arg4 + 16;
    local_r11 = (Arg4 + 16) - (8);
    v_stack_m70 = local_r11 + (int32_t)((uint32_t)(*(uint16_t *)(arg4 + 0xE))) * 8;
    v_stack_p20 = (uint32_t)(*(uint16_t *)(arg4 + 0xE));
    local_r11 = 0;
loc_009F252B:
    if ((Arg4 + 16) > (local_r11 + (int32_t)((uint32_t)(*(uint16_t *)(arg4 + 0xE))) * 8)) goto loc_009F25F9;
    local_r13 = (uint32_t)((*(uint16_t *)(arg4 + 0xE)) >> (1));
    if (condition_is_not_equal) goto loc_009F264E;
    if ((uint32_t)((uint32_t)((uint32_t)(*(uint16_t *)(arg4 + 0xE)))) == 0) goto loc_009F25F9;
    v_stack_mDC = 0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg12)))) & (0x1000ULL));
    if (Arg4 + 16 == 0) goto loc_009F2E1A;
    v_stack_mDC = 0;
    if (((0xFFFFFFFFFFFF0000ULL) & (v_stack_mA0)) != 0) goto loc_009F2CDF;
    if (sign_flag) goto loc_009F2B1E;
    if ((uint32_t)(Arg1) == 0) goto loc_009F258E;
    if (((0xFFFFFFFFFFFF0000ULL) & ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x10)))))) != 0) goto loc_009F2E0A;
loc_009F258E:
    Arg3 = (uint32_t)((v_stack_mA0) - (*(uint32_t *)(arg4 + 0x10)));
    v_stack_mE4 = (uint32_t)(Arg3);
loc_009F2596:
    v_stack_mD8 = (uint32_t)(Arg3);
loc_009F259B:
loc_009F259F:
    v_stack_mE8 = 0;
loc_009F25AC:
    if (sign_flag) goto loc_009F2A9A;
    if ((uint32_t)((uint32_t)(v_stack_mE4)) != 0) goto loc_009F25F9;
    if (!sign_flag) goto loc_009F29EE;
loc_009F25C4:
    if ((uint32_t)(local_r15) == 0) goto loc_009F25EA;
    if (v_stack_mA8 != 0) goto loc_009F25E0;
    if (((uint32_t)(*(uint32_t *)(v_stack_m98 + 0x4)) + Arg4 * 1) >= Arg4) goto loc_009F25F4;
loc_009F25E0:
    goto loc_009F2EA1;
loc_009F25EA:
    local_rdi = ((uint32_t)(*(uint32_t *)(v_stack_m98 + 0x4))) + (Arg4);
loc_009F25F4:
    v_stack_mC0 = local_rdi;
loc_009F25F9:
loc_009F25FE:
    if (v_stack_mA8 != 0) goto loc_009F2962;
loc_009F2611:
    local_r11 = (Arg7) + (8);
    v_stack_p38 = local_r11;
    v_stack_m48 = local_r11;
    goto loc_009F23E0;
loc_009F264E:
    v_stack_m78 = v_stack_mA0;
    local_r14 = (uint8_t)((0) & (1));
    v_stack_p20 = (uint8_t)(local_r14);
    result = (int32_t)((uint32_t)(v_stack_mD0));
    if (!(condition_is_not_equal)) {
        result = (int32_t)((uint32_t)(v_stack_mD0 - 1));
    }
    v_stack_m78 = v_stack_mA0 + result * 8;
    v_stack_mF0 = v_stack_mD8;
    v_stack_mF8 = (uint32_t)((uint32_t)(v_stack_mD4));
    v_stack_m100 = v_stack_mA0 + result * 8;
    v_stack_m108 = Arg4;
    result = LdrpResCompareResourceNames(Arg1, v_stack_mA0, v_stack_p18, (uint32_t)(Arg8));
    v_stack_mE8 = (uint32_t)(result);
    local_r11 = 0;
    if (sign_flag) goto loc_009F2A82;
    v_stack_mE4 = (uint32_t)((uint32_t)(v_stack_mD8));
    if ((uint32_t)((uint32_t)(v_stack_mD8)) == 0) goto loc_009F29D5;
    if (sign_flag) goto loc_009F2AEC;
    v_stack_m98 = v_stack_mA0 + result * 8 + 8;
    v_stack_p20 = (uint32_t)(v_stack_mD0);
loc_009F26E5:
    goto loc_009F252B;
loc_009F2704:
    if ((uint32_t)((uint32_t)(v_stack_mE0)) == 0) goto loc_009F245D;
    result = (v_stack_mD0) << (3);
    v_stack_m90 = result;
    result = ((uint32_t)((uint32_t)(result)) + 16) + (local_rdi);
    if (result < local_rdi) goto loc_009F25E0;
    Arg1 = (Arg1) & (-4);
    Arg1 = (Arg1) + (v_stack_p18);
    result = (local_rdi + 16) + ((uint32_t)((uint32_t)(result)));
    if (result > Arg1) goto loc_009F25E0;
    Arg2 = 0;
    goto loc_009F245D;
loc_009F274F:
    if (((uint32_t)(v_stack_mA0)) != 3) goto loc_009F241D;
    v_stack_mA8 = local_rdi;
    v_stack_m60 = local_rdi;
    if (Arg9 == NULL) goto loc_009F2EA1;
    v_stack_p30 = (uint16_t)(*(uint16_t *)(arg9));
    v_stack_m88 = (uint16_t)(*(uint16_t *)(arg9));
    v_stack_mB4 = 0;
    v_stack_mB8 = 0;
    result = (uint32_t)(~((uint32_t)((uint32_t)((uint32_t)(v_stack_mD4)))));
    if ((((uint8_t)(result)) & (4)) == 0) goto loc_009F241D;
    v_stack_mA0 = *(uint16_t *)(arg9 + 0x4);
    v_stack_m80 = *(uint16_t *)(arg9 + 0x4);
    goto loc_009F241D;
loc_009F27C0:
    if ((((uint8_t)((uint32_t)(v_stack_mD4))) & (32)) == 0) goto loc_009F24EF;
    v_stack_mC0 = 0;
    if ((uint32_t)((uint32_t)(v_stack_mE0)) == 0) goto loc_009F27E8;
    if (((uint32_t)(*(uint32_t *)(local_r11 + 0x4)) + Arg4 * 1) < Arg4) goto loc_009F25E0;
loc_009F27E8:
    v_stack_mC8 = (uint32_t)(*(uint32_t *)(local_r11 + 0x4)) + Arg4 * 1;
    v_stack_m80 = (uint32_t)(*(uint32_t *)(local_r11));
loc_009F2800:
    local_r11 = 0;
loc_009F2803:
    Arg4 = (uint32_t)(((uint32_t)(v_stack_mD4)) & (2));
    if ((uint32_t)(*(uint32_t *)(local_r11 + 0x4)) + Arg4 * 1 == 0) goto loc_009F2A25;
    if ((uint32_t)(Arg4) != 0) goto loc_009F2A25;
    if ((uint32_t)((uint32_t)(v_stack_mE0)) == 0) goto loc_009F2A19;
    if (((uint32_t)(*(uint32_t *)(local_r11 + 0x4)) + Arg4 * 1) <= Arg4) goto loc_009F2A78;
    local_rbx = (Arg1) & (-4);
    if (((uint32_t)(*(uint32_t *)(local_r11 + 0x4)) + Arg4 * 1 + 16) > (local_rbx + v_stack_p18 * 1)) goto loc_009F2A78;
loc_009F2843:
    if (Arg13 != 0) {
        *(uint16_t *)(Arg13) = (uint16_t)((uint32_t)(*(uint32_t *)(local_r11)));
    }
    if (((1) & ((uint8_t)(Arg1))) != 0) goto loc_009F2B38;
loc_009F2865:
    if ((uint32_t)((uint32_t)(v_stack_mE0)) == 0) goto loc_009F2AA2;
    if (((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_r11 + 0x4)) + arg4 * 1))) < 0) goto loc_009F25E0;
    Arg1 = ((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_r11 + 0x4)) + arg4 * 1))) - (0);
    local_r12 = (Arg4) - (Arg1);
    if (Arg1 < local_r12) goto loc_009F2A78;
    if (Arg1 > v_stack_p18) goto loc_009F2A78;
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_r11 + 0x4)) + arg4 * 1 + 0x4))) == 0) goto loc_009F2A78;
    if (((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_r11 + 0x4)) + arg4 * 1 + 0x4))) > v_stack_p18) goto loc_009F2A78;
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_r11 + 0x4)) + arg4 * 1 + 0x4))))) + (Arg1);
    if (result > v_stack_p18) goto loc_009F2A78;
loc_009F28C0:
    if (Arg10 == 0) goto loc_009F28F3;
    if ((uint32_t)((uint32_t)(v_stack_mE0)) == 0) goto loc_009F2D70;
    if ((local_rbx + Arg1 * 1) < local_rbx) goto loc_009F25E0;
    if ((local_rbx + Arg1 * 1) > (local_rbx + v_stack_p18 * 1)) goto loc_009F25E0;
    *(uint64_t *)(Arg10) = local_rbx + Arg1 * 1;
loc_009F28F3:
    if (Arg11 == 0) goto loc_009F292D;
    if ((uint32_t)((uint32_t)(v_stack_mE0)) == 0) goto loc_009F292A;
    if (Arg10 == 0) goto loc_009F292A;
    if ((*(uint64_t *)(Arg10) + (uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_r11 + 0x4)) + arg4 * 1 + 0x4)) * 1) < (*(uint64_t *)(Arg10))) goto loc_009F25E0;
    local_rsi = (Arg1) & (-4);
    local_rsi = (local_rsi) + (v_stack_p18);
    if ((*(uint64_t *)(Arg10) + (uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_r11 + 0x4)) + arg4 * 1 + 0x4)) * 1) > local_rsi) goto loc_009F25E0;
loc_009F292A:
    *(uint64_t *)(Arg11) = (uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_r11 + 0x4)) + arg4 * 1 + 0x4));
loc_009F292D:
    goto loc_009F2EA1;
loc_009F2935:
    if ((uint32_t)((uint32_t)(v_stack_mE0)) == 0) goto loc_009F2949;
    Arg1 = ((int32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0x4)) + Arg4 * 1))) + (0);
    if (Arg1 < 0) goto loc_009F25E0;
loc_009F2949:
    v_stack_m90 = local_r11 + (uint32_t)(*(uint32_t *)(local_r11 + 0x4)) + Arg4 * 1 * 8;
    v_stack_m98 = local_r11 + (uint32_t)(*(uint32_t *)(local_r11 + 0x4)) + Arg4 * 1 * 8;
    goto loc_009F2483;
loc_009F2962:
    if ((uint32_t)(*(uint32_t *)(local_r11 + 0x4)) + Arg4 * 1 != 0) goto loc_009F2611;
    if ((((uint8_t)(Arg11)) & (4)) != 0) goto loc_009F2A5B;
    Arg2 = (uint16_t)(((uint32_t)(v_stack_mB4)) + 1);
    v_stack_mB4 = (uint32_t)(Arg2);
    v_stack_mB8 = (uint16_t)(Arg2);
    if (((uint32_t)((uint16_t)(Arg2))) >= ((uint32_t)((int16_t)(Arg6)))) goto loc_009F2AB2;
    v_stack_mA0 = *(uint16_t *)(arg9 + (uint16_t)(Arg2) * 8 + 0x4);
    v_stack_m80 = *(uint16_t *)(arg9 + (uint16_t)(Arg2) * 8 + 0x4);
    Arg2 = 0;
    goto loc_009F24F7;
loc_009F29D5:
    if (sign_flag) goto loc_009F25C4;
    v_stack_mC0 = v_stack_m90;
loc_009F29EE:
    if ((uint32_t)((uint32_t)(v_stack_mE0)) == 0) goto loc_009F2A87;
    if (v_stack_mA8 == v_stack_m90) goto loc_009F25E0;
    v_stack_mD0 = local_r12 + (uint32_t)(*(uint32_t *)((uint32_t)(v_stack_mE0) + 0x4)) * 1;
    if ((local_r12 + (uint32_t)(*(uint32_t *)((uint32_t)(v_stack_mE0) + 0x4)) * 1) < local_r12) goto loc_009F25E0;
    goto loc_009F2A90;
loc_009F2A19:
    local_rbx = (local_rsi) & (-4);
    goto loc_009F2843;
loc_009F2A25:
    if (v_stack_m90 != 0) goto loc_009F2E36;
loc_009F2A2E:
    Arg3 = (uint32_t)((*(uint16_t *)(arg9 + (uint16_t)(Arg2) * 8 + 0x4)) - (v_stack_mAC));
    Arg3 = (uint32_t)((Arg3) - (1));
    if (condition_is_equal) goto loc_009F2CAE;
    Arg3 = (uint32_t)((Arg3) - (1));
    if (condition_is_equal) goto loc_009F2E9C;
    if (((uint32_t)(Arg3)) != 1) goto loc_009F2EA1;
    goto loc_009F2EA1;
loc_009F2A5B:
    goto loc_009F2803;
loc_009F2A78:
    v_stack_mC8 = v_stack_m90;
    goto loc_009F25E0;
loc_009F2A82:
    goto loc_009F2EAF;
loc_009F2A87:
    v_stack_mD0 = local_r12 + (uint32_t)(*(uint32_t *)((uint32_t)(v_stack_mE0) + 0x4)) * 1;
loc_009F2A90:
    v_stack_mC8 = local_r12 + (uint32_t)(*(uint32_t *)((uint32_t)(v_stack_mE0) + 0x4)) * 1;
    goto loc_009F25FE;
loc_009F2A9A:
    goto loc_009F2EAF;
loc_009F2AA2:
    goto loc_009F28C0;
loc_009F2AB2:
    if ((*(uint8_t *)(v_stack_m90 + 0x204)) != ((uint8_t)(v_stack_m90))) goto loc_009F2611;
    Arg4 = (uint32_t)((Arg11) | (32));
    v_stack_mD4 = (uint32_t)(Arg4);
    v_stack_p60 = (uint32_t)(Arg4);
    Arg2 = 0;
    goto loc_009F24E1;
loc_009F2AEC:
    v_stack_m70 = (uint32_t)(v_stack_mE0) - 8;
    if (v_stack_p20 == ((uint8_t)(v_stack_m90))) goto loc_009F2CCF;
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_mB0));
loc_009F2B11:
    goto loc_009F26E5;
loc_009F2B1E:
    if ((uint32_t)(v_stack_m90) != 0) goto loc_009F2DFF;
loc_009F2B26:
    v_stack_mE4 = 1;
    v_stack_mD8 = 1;
    goto loc_009F259F;
loc_009F2B38:
    if (((uint16_t)(*(uint16_t *)(arg5 + 0x18))) != 267) goto loc_009F2C98;
loc_009F2B5A:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x88))) == 0) goto loc_009F2E2A;
    if ((uint32_t)((uint32_t)(v_stack_mE0)) == 0) goto loc_009F2B7F;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x88)))) + (uint32_t)(0xC0000204ULL) * 1) < ((uint32_t)(0xC0000204ULL))) goto loc_009F25E0;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x88)))) + (uint32_t)(0xC0000204ULL) * 1) < local_r12) goto loc_009F25E0;
loc_009F2B7F:
    local_rdi = ((uint32_t)(0xC0000204ULL)) - (local_r12);
    local_rdi = (local_rdi) + ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x88)))));
    v_stack_m100 = (uint8_t)(v_stack_p10);
    v_stack_m108 = (uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x88)));
    result = LdrpSectionTableFromVirtualAddress((uint32_t)(0xC0000204ULL), v_stack_p18, Arg5, Arg4);
    local_r11 = 0;
    if (result == 0) goto loc_009F2A78;
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_mB0))))) <= (*(uint32_t *)(result + 0x8))) goto loc_009F2865;
    v_stack_m100 = (uint8_t)(v_stack_p10);
    v_stack_m108 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_mB0))));
    result = LdrpSectionTableFromVirtualAddress((uint32_t)(0xC0000204ULL), v_stack_p18, Arg5, Arg4);
    local_r14 = 0;
    if (result == 0) goto loc_009F2CB8;
    v_stack_m100 = (uint8_t)(v_stack_p10);
    v_stack_m108 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC)));
    result = LdrpSectionTableFromVirtualAddress((uint32_t)(0xC0000204ULL), v_stack_p18, Arg5, Arg4);
    local_r11 = 0;
    if (result == 0) goto loc_009F2CCA;
    if ((uint32_t)((uint32_t)(v_stack_mE0)) == 0) goto loc_009F2C47;
    Arg4 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC))))) - ((uint32_t)(*(uint32_t *)(result + 0xC)));
    Arg4 = (Arg4) + ((uint32_t)(0xC0000204ULL));
    if (Arg4 < ((uint32_t)(0xC0000204ULL))) goto loc_009F25E0;
    Arg1 = ((uint32_t)(*(uint32_t *)(result + 0x14))) + (Arg4);
    if (Arg1 < Arg4) goto loc_009F25E0;
loc_009F2C47:
    Arg2 = ((uint32_t)(*(uint32_t *)(result + 0x14))) - ((uint32_t)(*(uint32_t *)(result + 0xC)));
    Arg2 = (Arg2) + ((uint32_t)(0xC0000204ULL));
    Arg2 = (Arg2) + ((uint32_t)(*(uint32_t *)(result + 0xC)));
loc_009F2C57:
    if ((uint32_t)((uint32_t)(v_stack_mE0)) == 0) goto loc_009F2C7E;
    if (((uint32_t)(*(uint32_t *)(result + 0xC))) < ((uint32_t)(*(uint32_t *)(result + 0xC)))) goto loc_009F25E0;
    Arg1 = ((uint32_t)(*(uint32_t *)(result + 0xC))) - ((uint32_t)(*(uint32_t *)(result + 0xC)));
    result = (Arg2) - (local_r12);
    if (Arg1 < result) goto loc_009F25E0;
loc_009F2C7E:
    Arg1 = ((uint32_t)(*(uint32_t *)(result + 0xC))) - ((uint32_t)(*(uint32_t *)(result + 0xC)));
    Arg1 = (Arg1) - (Arg2);
    Arg1 = (Arg1) + (local_r12);
    local_rdi = (local_rdi) + (Arg1);
    goto loc_009F2865;
loc_009F2C98:
    if (((uint16_t)(result)) != 523) goto loc_009F2CC2;
    goto loc_009F2B5A;
loc_009F2CAE:
    goto loc_009F2EA1;
loc_009F2CB8:
    v_stack_mC8 = (uint32_t)(*(uint32_t *)(result + 0xC));
    goto loc_009F25E0;
loc_009F2CC2:
    goto loc_009F2B5A;
loc_009F2CCA:
    goto loc_009F2C57;
loc_009F2CCF:
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC)));
    goto loc_009F2B11;
loc_009F2CDF:
    if (!sign_flag) goto loc_009F2D8C;
    if (523 != 0) goto loc_009F2D9C;
    Arg2 = (local_rsi) & (-4);
loc_009F2D02:
    if (523 != 0) goto loc_009F2DD3;
loc_009F2D0A:
    if ((((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0xC))))) & (0 + local_r12 * 1 + 2)) == 0) goto loc_009F2DBE;
    result = wcsncmp(v_stack_mA0, 0 + local_r12 * 1 + 2, *(uint16_t *)(0 + local_r12 * 1), 0);
    v_stack_mE4 = (uint32_t)(result);
    local_r11 = 0;
    if ((uint32_t)(result) != 0) goto loc_009F2DF5;
    Arg1 = (v_stack_mA0) | (-1);
loc_009F2D41:
    Arg1 = (Arg1) + 1;
    if ((*(uint16_t *)(v_stack_mA0 + Arg1 * 2)) != 0) goto loc_009F2D41;
    if (Arg1 == (*(uint16_t *)(0 + local_r12 * 1))) goto loc_009F2DF5;
    v_stack_mE4 = 1;
    v_stack_mD8 = 1;
    goto loc_009F259F;
loc_009F2D70:
    result = ((uint32_t)(*(uint32_t *)(v_stack_mA0))) - (local_rdi);
    result = (result) + ((uint32_t)(0xC000008AULL));
    *(uint64_t *)(0 + local_r12 * 1 + 0x2) = result;
    goto loc_009F28F3;
loc_009F2D82:
    v_stack_mC0 = 0 + local_r12 * 1 + 2;
    goto loc_009F2A2E;
loc_009F2D8C:
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    v_stack_mE4 = (uint32_t)(result);
    v_stack_mD8 = (uint32_t)(result);
    goto loc_009F259B;
loc_009F2D9C:
    if (((uint32_t)(v_stack_mE0)) < local_r12) goto loc_009F2DBE;
    if (((uint32_t)(v_stack_mE0) + 4) < local_r12) goto loc_009F2DBE;
    Arg2 = (local_rsi) & (-4);
    if (((uint32_t)(v_stack_mE0) + 4) <= (Arg2 + (uint32_t)(v_stack_mE0) * 1)) goto loc_009F2D02;
loc_009F2DBE:
    v_stack_mDC = (uint32_t)((uint32_t)(0xC000007BULL));
    goto loc_009F259B;
loc_009F2DD3:
    Arg1 = (*(uint16_t *)((uint32_t)(v_stack_mE0))) + (2);
    Arg1 = (local_r12 + Arg1 * 2) + (0);
    if (Arg1 < local_r12) goto loc_009F2DBE;
    if (Arg1 > (Arg2 + (uint32_t)(v_stack_mE0) * 1)) goto loc_009F2DBE;
    goto loc_009F2D0A;
loc_009F2DF5:
    goto loc_009F2596;
loc_009F2DFF:
    if (((v_stack_mA0) & ((uint32_t)(*(uint32_t *)(Arg2)))) != 0) goto loc_009F2B26;
loc_009F2E0A:
    v_stack_mDC = (uint32_t)((uint32_t)(0xC000007BULL));
    goto loc_009F259B;
loc_009F2E1A:
    v_stack_mE8 = (uint32_t)((uint32_t)(0xC000008AULL));
    goto loc_009F25AC;
loc_009F2E2A:
    v_stack_mC8 = 0;
    goto loc_009F2EA1;
loc_009F2E36:
    if (0 == 0) goto loc_009F2A2E;
    if ((uint32_t)((uint32_t)(v_stack_mE0)) == 0) goto loc_009F2E64;
    if ((local_rdi + 24) < local_rdi) goto loc_009F2E5A;
    local_rsi = (local_rsi) & (-4);
    if ((local_rdi + 24) <= (local_rsi + (uint32_t)(v_stack_mE0) * 1)) goto loc_009F2E68;
loc_009F2E5A:
    v_stack_mC0 = 0;
    goto loc_009F25E0;
loc_009F2E64:
    local_rsi = (local_rsi) & (-4);
loc_009F2E68:
    if (Arg10 == 0) goto loc_009F292D;
    if ((uint32_t)((uint32_t)(v_stack_mE0)) == 0) goto loc_009F2E94;
    if (local_rdi < local_rsi) goto loc_009F25E0;
    if (local_rdi > (local_rsi + (uint32_t)(v_stack_mE0) * 1)) goto loc_009F25E0;
loc_009F2E94:
    *(uint64_t *)(Arg10) = local_rdi;
    goto loc_009F292D;
loc_009F2E9C:
loc_009F2EA1:
    v_stack_mE8 = (uint32_t)((uint32_t)(0xC000008BULL));
    goto loc_009F2EAD;
loc_009F2EAD:
loc_009F2EAF:
    local_rsp = (local_rsp) + (240);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000008BULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0 + rax*1` | `64` | `R` |
| `Arg4` | `+ 0x0 + rcx*2` | `64` | `R` |
| `Arg5` | `+ 0x18` | `16` | `R` |
| `Arg5` | `+ 0x88` | `32` | `R` |
| `Arg5` | `+ 0x98` | `32` | `R` |
| `Arg8` | `- 0x1` | `32` | `R` |
| `Arg9` | `+ 0x4 + rax*8` | `16` | `R` |
| `Arg9` | `+ 0x204` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009F22F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
