# PpmEventTraceSoftCoreParkingSelectionEx

- RVA: `0x004F2424`–`0x004F2D52` (길이 `2,350` bytes)
- VA: `0x00000001404F2424`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B7E1C`
- 디코드: `581`개 명령, `2,350/2,350` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x004F2489` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004F249A` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004F24A9` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004F24C9` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x004F24F6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004F2512` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004F252A` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004F2542` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x004F2555` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x004F256B` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x004F2D22` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x004F2D31` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PpmParkCalculateCoreParkingMaskEx](../5D/PpmParkCalculateCoreParkingMaskEx_function_005DFBE0.md) at `0x005E0518`

### Static image references
- `0x004F244E` → RVA `0x00E0A740` (`.data`; read)
- `0x004F245F` → RVA `0x00E67A70` (`.data`; read)
- `0x004F24AE` → RVA `0x00E67A39` (`.data`; read)
- `0x004F24BB` → RVA `0x00F083E8` (`.data`; read)
- `0x004F24C2` → RVA `0x0001BDF8` (`.rdata`; read)
- `0x004F2609` → RVA `0x00E67A78` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F2424  48 8B C4                        mov rax, rsp
004F2427  48 89 58 08                     mov qword ptr [rax + 8], rbx
004F242B  66 44 89 48 20                  mov word ptr [rax + 0x20], r9w
004F2430  66 44 89 40 18                  mov word ptr [rax + 0x18], r8w
004F2435  55                              push rbp
004F2436  56                              push rsi
004F2437  57                              push rdi
004F2438  41 54                           push r12
004F243A  41 55                           push r13
004F243C  41 56                           push r14
004F243E  41 57                           push r15
004F2440  48 8D A8 28 FB FF FF            lea rbp, [rax - 0x4d8]
004F2447  48 81 EC A0 05 00 00            sub rsp, 0x5a0
004F244E  48 8B 05 EB 82 91 00            mov rax, qword ptr [rip + 0x9182eb]
004F2455  48 33 C4                        xor rax, rsp
004F2458  48 89 85 90 04 00 00            mov qword ptr [rbp + 0x490], rax
004F245F  48 8B 1D 0A 56 97 00            mov rbx, qword ptr [rip + 0x97560a]
004F2466  45 33 E4                        xor r12d, r12d
004F2469  44 8B FA                        mov r15d, edx
004F246C  4C 8B F1                        mov r14, rcx
004F246F  41 8B FC                        mov edi, r12d
004F2472  48 85 DB                        test rbx, rbx
004F2475  0F 84 AC 08 00 00               je 0x1404f2d27
004F247B  BE 00 01 00 00                  mov esi, 0x100
004F2480  48 8D 4D 68                     lea rcx, [rbp + 0x68]
004F2484  44 8B C6                        mov r8d, esi
004F2487  33 D2                           xor edx, edx
004F2489  E8 B2 47 1D 00                  call 0x1406c6c40
004F248E  44 8B C6                        mov r8d, esi
004F2491  48 8D 8D 78 01 00 00            lea rcx, [rbp + 0x178]
004F2498  33 D2                           xor edx, edx
004F249A  E8 A1 47 1D 00                  call 0x1406c6c40
004F249F  44 8B C6                        mov r8d, esi
004F24A2  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
004F24A7  33 D2                           xor edx, edx
004F24A9  E8 92 47 1D 00                  call 0x1406c6c40
004F24AE  44 38 25 84 55 97 00            cmp byte ptr [rip + 0x975584], r12b
004F24B5  0F 84 6C 08 00 00               je 0x1404f2d27
004F24BB  48 8B 0D 26 5F A1 00            mov rcx, qword ptr [rip + 0xa15f26]
004F24C2  48 8D 15 2F 99 B2 FF            lea rdx, [rip - 0x4d66d1]
004F24C9  E8 82 FF E9 FF                  call 0x140392450
004F24CE  84 C0                           test al, al
004F24D0  0F 84 51 08 00 00               je 0x1404f2d27
004F24D6  4F 8D 2C BF                     lea r13, [r15 + r15*4]
004F24DA  48 C7 45 60 01 00 20 00         mov qword ptr [rbp + 0x60], 0x200001
004F24E2  49 C1 E5 07                     shl r13, 7
004F24E6  48 8D 4D 68                     lea rcx, [rbp + 0x68]
004F24EA  4D 03 AE 08 05 00 00            add r13, qword ptr [r14 + 0x508]
004F24F1  33 D2                           xor edx, edx
004F24F3  44 8B C6                        mov r8d, esi
004F24F6  E8 45 47 1D 00                  call 0x1406c6c40
004F24FB  33 D2                           xor edx, edx
004F24FD  48 C7 85 70 01 00 00 01 00 20 00  mov qword ptr [rbp + 0x170], 0x200001
004F2508  44 8B C6                        mov r8d, esi
004F250B  48 8D 8D 78 01 00 00            lea rcx, [rbp + 0x178]
004F2512  E8 29 47 1D 00                  call 0x1406c6c40
004F2517  33 D2                           xor edx, edx
004F2519  48 C7 44 24 50 01 00 20 00      mov qword ptr [rsp + 0x50], 0x200001
004F2522  44 8B C6                        mov r8d, esi
004F2525  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
004F252A  E8 11 47 1D 00                  call 0x1406c6c40
004F252F  49 8D 75 28                     lea rsi, [r13 + 0x28]
004F2533  48 8B D6                        mov rdx, rsi
004F2536  49 8D 8E 40 02 00 00            lea rcx, [r14 + 0x240]
004F253D  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
004F2542  E8 F9 E1 EC FF                  call 0x1403c0740
004F2547  49 8D 8E 38 01 00 00            lea rcx, [r14 + 0x138]
004F254E  48 8B D6                        mov rdx, rsi
004F2551  4C 8D 45 60                     lea r8, [rbp + 0x60]
004F2555  E8 E6 E1 EC FF                  call 0x1403c0740
004F255A  49 8D 8E 48 03 00 00            lea rcx, [r14 + 0x348]
004F2561  48 8B D6                        mov rdx, rsi
004F2564  4C 8D 85 70 01 00 00            lea r8, [rbp + 0x170]
004F256B  E8 D0 E1 EC FF                  call 0x1403c0740
004F2570  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
004F2575  41 8D 44 24 20                  lea eax, [r12 + 0x20]
004F257A  45 0F B7 C4                     movzx r8d, r12w
004F257E  45 8D 7C 24 01                  lea r15d, [r12 + 1]
004F2583  41 8B D4                        mov edx, r12d
004F2586  66 3B 16                        cmp dx, word ptr [rsi]
004F2589  73 20                           jae 0x1404f25ab
004F258B  0F B7 C2                        movzx eax, dx
004F258E  4C 39 64 C6 08                  cmp qword ptr [rsi + rax*8 + 8], r12
004F2593  74 11                           je 0x1404f25a6
004F2595  8B C7                           mov eax, edi
004F2597  41 03 FF                        add edi, r15d
004F259A  66 45 03 C7                     add r8w, r15w
004F259E  66 89 94 45 90 02 00 00         mov word ptr [rbp + rax*2 + 0x290], dx
004F25A6  B8 20 00 00 00                  mov eax, 0x20
004F25AB  41 03 D7                        add edx, r15d
004F25AE  3B D0                           cmp edx, eax
004F25B0  72 D4                           jb 0x1404f2586
004F25B2  66 44 89 85 80 02 00 00         mov word ptr [rbp + 0x280], r8w
004F25BA  48 8D 85 80 02 00 00            lea rax, [rbp + 0x280]
004F25C1  48 89 03                        mov qword ptr [rbx], rax
004F25C4  41 BE 02 00 00 00               mov r14d, 2
004F25CA  4C 89 73 08                     mov qword ptr [rbx + 8], r14
004F25CE  41 8B D7                        mov edx, r15d
004F25D1  66 45 3B E0                     cmp r12w, r8w
004F25D5  73 51                           jae 0x1404f2628
004F25D7  4C 8D 8D 90 02 00 00            lea r9, [rbp + 0x290]
004F25DE  45 0F B7 D0                     movzx r10d, r8w
004F25E2  45 0F B7 01                     movzx r8d, word ptr [r9]
004F25E6  8D 4A 01                        lea ecx, [rdx + 1]
004F25E9  8B C2                           mov eax, edx
004F25EB  48 03 C9                        add rcx, rcx
004F25EE  48 03 C0                        add rax, rax
004F25F1  4C 89 0C C3                     mov qword ptr [rbx + rax*8], r9
004F25F5  4C 89 74 C3 08                  mov qword ptr [rbx + rax*8 + 8], r14
004F25FA  66 44 3B 06                     cmp r8w, word ptr [rsi]
004F25FE  73 09                           jae 0x1404f2609
004F2600  49 FF C0                        inc r8
004F2603  4E 8D 04 C6                     lea r8, [rsi + r8*8]
004F2607  EB 07                           jmp 0x1404f2610
004F2609  4C 8D 05 68 54 97 00            lea r8, [rip + 0x975468]
004F2610  41 03 D6                        add edx, r14d
004F2613  4C 89 04 CB                     mov qword ptr [rbx + rcx*8], r8
004F2617  4D 03 CE                        add r9, r14
004F261A  48 C7 44 CB 08 08 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 8
004F2623  4D 2B D7                        sub r10, r15
004F2626  75 BA                           jne 0x1404f25e2
004F2628  48 85 F6                        test rsi, rsi
004F262B  44 8B DF                        mov r11d, edi
004F262E  4C 8D 54 24 50                  lea r10, [rsp + 0x50]
004F2633  45 0F B7 CC                     movzx r9d, r12w
004F2637  4C 0F 45 D6                     cmovne r10, rsi
004F263B  45 8B C4                        mov r8d, r12d
004F263E  B8 20 00 00 00                  mov eax, 0x20
004F2643  66 45 3B 02                     cmp r8w, word ptr [r10]
004F2647  73 22                           jae 0x1404f266b
004F2649  41 0F B7 C0                     movzx eax, r8w
004F264D  4D 39 64 C2 08                  cmp qword ptr [r10 + rax*8 + 8], r12
004F2652  74 12                           je 0x1404f2666
004F2654  8B C7                           mov eax, edi
004F2656  41 03 FF                        add edi, r15d
004F2659  66 45 03 CF                     add r9w, r15w
004F265D  66 44 89 84 45 90 02 00 00      mov word ptr [rbp + rax*2 + 0x290], r8w
004F2666  B8 20 00 00 00                  mov eax, 0x20
004F266B  45 03 C7                        add r8d, r15d
004F266E  44 3B C0                        cmp r8d, eax
004F2671  72 D0                           jb 0x1404f2643
004F2673  66 44 89 8D 82 02 00 00         mov word ptr [rbp + 0x282], r9w
004F267B  48 85 F6                        test rsi, rsi
004F267E  75 18                           jne 0x1404f2698
004F2680  8B C2                           mov eax, edx
004F2682  48 8D 8D 82 02 00 00            lea rcx, [rbp + 0x282]
004F2689  48 03 C0                        add rax, rax
004F268C  41 03 D7                        add edx, r15d
004F268F  48 89 0C C3                     mov qword ptr [rbx + rax*8], rcx
004F2693  4C 89 74 C3 08                  mov qword ptr [rbx + rax*8 + 8], r14
004F2698  41 0F B7 C9                     movzx ecx, r9w
004F269C  41 8D 04 0B                     lea eax, [r11 + rcx]
004F26A0  44 3B D8                        cmp r11d, eax
004F26A3  73 5F                           jae 0x1404f2704
004F26A5  4C 8D 85 90 02 00 00            lea r8, [rbp + 0x290]
004F26AC  44 8B D1                        mov r10d, ecx
004F26AF  4F 8D 04 58                     lea r8, [r8 + r11*2]
004F26B3  44 0F B7 5C 24 50               movzx r11d, word ptr [rsp + 0x50]
004F26B9  45 0F B7 08                     movzx r9d, word ptr [r8]
004F26BD  8D 4A 01                        lea ecx, [rdx + 1]
004F26C0  8B C2                           mov eax, edx
004F26C2  48 03 C9                        add rcx, rcx
004F26C5  48 03 C0                        add rax, rax
004F26C8  4C 89 04 C3                     mov qword ptr [rbx + rax*8], r8
004F26CC  4C 89 74 C3 08                  mov qword ptr [rbx + rax*8 + 8], r14
004F26D1  66 45 3B CB                     cmp r9w, r11w
004F26D5  73 0E                           jae 0x1404f26e5
004F26D7  41 8B C1                        mov eax, r9d
004F26DA  4C 8D 4C 24 58                  lea r9, [rsp + 0x58]
004F26DF  4D 8D 0C C1                     lea r9, [r9 + rax*8]
004F26E3  EB 07                           jmp 0x1404f26ec
004F26E5  4C 8D 0D 8C 53 97 00            lea r9, [rip + 0x97538c]
004F26EC  41 03 D6                        add edx, r14d
004F26EF  4C 89 0C CB                     mov qword ptr [rbx + rcx*8], r9
004F26F3  4D 03 C6                        add r8, r14
004F26F6  48 C7 44 CB 08 08 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 8
004F26FF  4D 2B D7                        sub r10, r15
004F2702  75 B5                           jne 0x1404f26b9
004F2704  48 85 F6                        test rsi, rsi
004F2707  44 8B DF                        mov r11d, edi
004F270A  4C 8D 55 60                     lea r10, [rbp + 0x60]
004F270E  45 0F B7 CC                     movzx r9d, r12w
004F2712  4C 0F 45 D6                     cmovne r10, rsi
004F2716  45 8B C4                        mov r8d, r12d
004F2719  B8 20 00 00 00                  mov eax, 0x20
004F271E  66 45 3B 02                     cmp r8w, word ptr [r10]
004F2722  73 22                           jae 0x1404f2746
004F2724  41 0F B7 C0                     movzx eax, r8w
004F2728  4D 39 64 C2 08                  cmp qword ptr [r10 + rax*8 + 8], r12
004F272D  74 12                           je 0x1404f2741
004F272F  8B C7                           mov eax, edi
004F2731  41 03 FF                        add edi, r15d
004F2734  66 45 03 CF                     add r9w, r15w
004F2738  66 44 89 84 45 90 02 00 00      mov word ptr [rbp + rax*2 + 0x290], r8w
004F2741  B8 20 00 00 00                  mov eax, 0x20
004F2746  45 03 C7                        add r8d, r15d
004F2749  44 3B C0                        cmp r8d, eax
004F274C  72 D0                           jb 0x1404f271e
004F274E  66 44 89 8D 84 02 00 00         mov word ptr [rbp + 0x284], r9w
004F2756  48 85 F6                        test rsi, rsi
004F2759  75 18                           jne 0x1404f2773
004F275B  8B C2                           mov eax, edx
004F275D  48 8D 8D 84 02 00 00            lea rcx, [rbp + 0x284]
004F2764  48 03 C0                        add rax, rax
004F2767  41 03 D7                        add edx, r15d
004F276A  48 89 0C C3                     mov qword ptr [rbx + rax*8], rcx
004F276E  4C 89 74 C3 08                  mov qword ptr [rbx + rax*8 + 8], r14
004F2773  41 0F B7 C9                     movzx ecx, r9w
004F2777  41 8D 04 0B                     lea eax, [r11 + rcx]
004F277B  44 3B D8                        cmp r11d, eax
004F277E  73 5D                           jae 0x1404f27dd
004F2780  4C 8D 85 90 02 00 00            lea r8, [rbp + 0x290]
004F2787  44 8B D1                        mov r10d, ecx
004F278A  4F 8D 04 58                     lea r8, [r8 + r11*2]
004F278E  44 0F B7 5D 60                  movzx r11d, word ptr [rbp + 0x60]
004F2793  45 0F B7 08                     movzx r9d, word ptr [r8]
004F2797  8D 4A 01                        lea ecx, [rdx + 1]
004F279A  8B C2                           mov eax, edx
004F279C  48 03 C9                        add rcx, rcx
004F279F  48 03 C0                        add rax, rax
004F27A2  4C 89 04 C3                     mov qword ptr [rbx + rax*8], r8
004F27A6  4C 89 74 C3 08                  mov qword ptr [rbx + rax*8 + 8], r14
004F27AB  66 45 3B CB                     cmp r9w, r11w
004F27AF  73 0D                           jae 0x1404f27be
004F27B1  41 8B C1                        mov eax, r9d
004F27B4  4C 8D 4D 68                     lea r9, [rbp + 0x68]
004F27B8  4D 8D 0C C1                     lea r9, [r9 + rax*8]
004F27BC  EB 07                           jmp 0x1404f27c5
004F27BE  4C 8D 0D B3 52 97 00            lea r9, [rip + 0x9752b3]
004F27C5  41 03 D6                        add edx, r14d
004F27C8  4C 89 0C CB                     mov qword ptr [rbx + rcx*8], r9
004F27CC  4D 03 C6                        add r8, r14
004F27CF  48 C7 44 CB 08 08 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 8
004F27D8  4D 2B D7                        sub r10, r15
004F27DB  75 B6                           jne 0x1404f2793
004F27DD  48 85 F6                        test rsi, rsi
004F27E0  44 8B DF                        mov r11d, edi
004F27E3  4C 8D 95 70 01 00 00            lea r10, [rbp + 0x170]
004F27EA  45 0F B7 CC                     movzx r9d, r12w
004F27EE  4C 0F 45 D6                     cmovne r10, rsi
004F27F2  45 8B C4                        mov r8d, r12d
004F27F5  B8 20 00 00 00                  mov eax, 0x20
004F27FA  66 45 3B 02                     cmp r8w, word ptr [r10]
004F27FE  73 22                           jae 0x1404f2822
004F2800  41 0F B7 C0                     movzx eax, r8w
004F2804  4D 39 64 C2 08                  cmp qword ptr [r10 + rax*8 + 8], r12
004F2809  74 12                           je 0x1404f281d
004F280B  8B C7                           mov eax, edi
004F280D  41 03 FF                        add edi, r15d
004F2810  66 45 03 CF                     add r9w, r15w
004F2814  66 44 89 84 45 90 02 00 00      mov word ptr [rbp + rax*2 + 0x290], r8w
004F281D  B8 20 00 00 00                  mov eax, 0x20
004F2822  45 03 C7                        add r8d, r15d
004F2825  44 3B C0                        cmp r8d, eax
004F2828  72 D0                           jb 0x1404f27fa
004F282A  66 44 89 8D 86 02 00 00         mov word ptr [rbp + 0x286], r9w
004F2832  48 85 F6                        test rsi, rsi
004F2835  75 18                           jne 0x1404f284f
004F2837  8B C2                           mov eax, edx
004F2839  48 8D 8D 86 02 00 00            lea rcx, [rbp + 0x286]
004F2840  48 03 C0                        add rax, rax
004F2843  41 03 D7                        add edx, r15d
004F2846  48 89 0C C3                     mov qword ptr [rbx + rax*8], rcx
004F284A  4C 89 74 C3 08                  mov qword ptr [rbx + rax*8 + 8], r14
004F284F  41 0F B7 C9                     movzx ecx, r9w
004F2853  41 8D 04 0B                     lea eax, [r11 + rcx]
004F2857  44 3B D8                        cmp r11d, eax
004F285A  73 63                           jae 0x1404f28bf
004F285C  4C 8D 85 90 02 00 00            lea r8, [rbp + 0x290]
004F2863  44 8B D1                        mov r10d, ecx
004F2866  4F 8D 04 58                     lea r8, [r8 + r11*2]
004F286A  44 0F B7 9D 70 01 00 00         movzx r11d, word ptr [rbp + 0x170]
004F2872  45 0F B7 08                     movzx r9d, word ptr [r8]
004F2876  8D 4A 01                        lea ecx, [rdx + 1]
004F2879  8B C2                           mov eax, edx
004F287B  48 03 C9                        add rcx, rcx
004F287E  48 03 C0                        add rax, rax
004F2881  4C 89 04 C3                     mov qword ptr [rbx + rax*8], r8
004F2885  4C 89 74 C3 08                  mov qword ptr [rbx + rax*8 + 8], r14
004F288A  66 45 3B CB                     cmp r9w, r11w
004F288E  73 10                           jae 0x1404f28a0
004F2890  41 8B C1                        mov eax, r9d
004F2893  4C 8D 8D 78 01 00 00            lea r9, [rbp + 0x178]
004F289A  4D 8D 0C C1                     lea r9, [r9 + rax*8]
004F289E  EB 07                           jmp 0x1404f28a7
004F28A0  4C 8D 0D D1 51 97 00            lea r9, [rip + 0x9751d1]
004F28A7  41 03 D6                        add edx, r14d
004F28AA  4C 89 0C CB                     mov qword ptr [rbx + rcx*8], r9
004F28AE  4D 03 C6                        add r8, r14
004F28B1  48 C7 44 CB 08 08 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 8
004F28BA  4D 2B D7                        sub r10, r15
004F28BD  75 B3                           jne 0x1404f2872
004F28BF  48 8D 8D F8 04 00 00            lea rcx, [rbp + 0x4f8]
004F28C6  8B C2                           mov eax, edx
004F28C8  48 03 C0                        add rax, rax
004F28CB  44 8B DF                        mov r11d, edi
004F28CE  4C 8B D6                        mov r10, rsi
004F28D1  45 0F B7 CC                     movzx r9d, r12w
004F28D5  45 8B C4                        mov r8d, r12d
004F28D8  48 89 0C C3                     mov qword ptr [rbx + rax*8], rcx
004F28DC  8D 4A 01                        lea ecx, [rdx + 1]
004F28DF  4C 89 74 C3 08                  mov qword ptr [rbx + rax*8 + 8], r14
004F28E4  48 03 C9                        add rcx, rcx
004F28E7  41 03 D6                        add edx, r14d
004F28EA  48 8D 85 00 05 00 00            lea rax, [rbp + 0x500]
004F28F1  48 85 F6                        test rsi, rsi
004F28F4  4C 89 74 CB 08                  mov qword ptr [rbx + rcx*8 + 8], r14
004F28F9  4C 8B B5 08 05 00 00            mov r14, qword ptr [rbp + 0x508]
004F2900  48 89 04 CB                     mov qword ptr [rbx + rcx*8], rax
004F2904  4D 0F 44 D6                     cmove r10, r14
004F2908  B8 20 00 00 00                  mov eax, 0x20
004F290D  66 45 3B 02                     cmp r8w, word ptr [r10]
004F2911  73 22                           jae 0x1404f2935
004F2913  41 0F B7 C0                     movzx eax, r8w
004F2917  4D 39 64 C2 08                  cmp qword ptr [r10 + rax*8 + 8], r12
004F291C  74 12                           je 0x1404f2930
004F291E  8B C7                           mov eax, edi
004F2920  41 03 FF                        add edi, r15d
004F2923  66 45 03 CF                     add r9w, r15w
004F2927  66 44 89 84 45 90 02 00 00      mov word ptr [rbp + rax*2 + 0x290], r8w
004F2930  B8 20 00 00 00                  mov eax, 0x20
004F2935  45 03 C7                        add r8d, r15d
004F2938  44 3B C0                        cmp r8d, eax
004F293B  72 D0                           jb 0x1404f290d
004F293D  66 44 89 8D 88 02 00 00         mov word ptr [rbp + 0x288], r9w
004F2945  48 85 F6                        test rsi, rsi
004F2948  75 1C                           jne 0x1404f2966
004F294A  8B C2                           mov eax, edx
004F294C  48 8D 8D 88 02 00 00            lea rcx, [rbp + 0x288]
004F2953  48 03 C0                        add rax, rax
004F2956  41 03 D7                        add edx, r15d
004F2959  48 89 0C C3                     mov qword ptr [rbx + rax*8], rcx
004F295D  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F2966  41 0F B7 C9                     movzx ecx, r9w
004F296A  41 8D 04 0B                     lea eax, [r11 + rcx]
004F296E  44 3B D8                        cmp r11d, eax
004F2971  73 59                           jae 0x1404f29cc
004F2973  4C 8D 85 90 02 00 00            lea r8, [rbp + 0x290]
004F297A  44 8B D1                        mov r10d, ecx
004F297D  4F 8D 04 58                     lea r8, [r8 + r11*2]
004F2981  45 0F B7 08                     movzx r9d, word ptr [r8]
004F2985  8D 4A 01                        lea ecx, [rdx + 1]
004F2988  8B C2                           mov eax, edx
004F298A  48 03 C9                        add rcx, rcx
004F298D  48 03 C0                        add rax, rax
004F2990  4C 89 04 C3                     mov qword ptr [rbx + rax*8], r8
004F2994  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F299D  66 45 3B 0E                     cmp r9w, word ptr [r14]
004F29A1  73 09                           jae 0x1404f29ac
004F29A3  49 FF C1                        inc r9
004F29A6  4F 8D 0C CE                     lea r9, [r14 + r9*8]
004F29AA  EB 07                           jmp 0x1404f29b3
004F29AC  4C 8D 0D C5 50 97 00            lea r9, [rip + 0x9750c5]
004F29B3  83 C2 02                        add edx, 2
004F29B6  4C 89 0C CB                     mov qword ptr [rbx + rcx*8], r9
004F29BA  49 83 C0 02                     add r8, 2
004F29BE  48 C7 44 CB 08 08 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 8
004F29C7  4D 2B D7                        sub r10, r15
004F29CA  75 B5                           jne 0x1404f2981
004F29CC  4C 8B B5 10 05 00 00            mov r14, qword ptr [rbp + 0x510]
004F29D3  48 85 F6                        test rsi, rsi
004F29D6  4C 8B D6                        mov r10, rsi
004F29D9  44 8B DF                        mov r11d, edi
004F29DC  4D 0F 44 D6                     cmove r10, r14
004F29E0  45 0F B7 CC                     movzx r9d, r12w
004F29E4  45 8B C4                        mov r8d, r12d
004F29E7  B8 20 00 00 00                  mov eax, 0x20
004F29EC  66 45 3B 02                     cmp r8w, word ptr [r10]
004F29F0  73 22                           jae 0x1404f2a14
004F29F2  41 0F B7 C0                     movzx eax, r8w
004F29F6  4D 39 64 C2 08                  cmp qword ptr [r10 + rax*8 + 8], r12
004F29FB  74 12                           je 0x1404f2a0f
004F29FD  8B C7                           mov eax, edi
004F29FF  41 03 FF                        add edi, r15d
004F2A02  66 45 03 CF                     add r9w, r15w
004F2A06  66 44 89 84 45 90 02 00 00      mov word ptr [rbp + rax*2 + 0x290], r8w
004F2A0F  B8 20 00 00 00                  mov eax, 0x20
004F2A14  45 03 C7                        add r8d, r15d
004F2A17  44 3B C0                        cmp r8d, eax
004F2A1A  72 D0                           jb 0x1404f29ec
004F2A1C  66 44 89 8D 8A 02 00 00         mov word ptr [rbp + 0x28a], r9w
004F2A24  48 85 F6                        test rsi, rsi
004F2A27  75 1C                           jne 0x1404f2a45
004F2A29  8B C2                           mov eax, edx
004F2A2B  48 8D 8D 8A 02 00 00            lea rcx, [rbp + 0x28a]
004F2A32  48 03 C0                        add rax, rax
004F2A35  41 03 D7                        add edx, r15d
004F2A38  48 89 0C C3                     mov qword ptr [rbx + rax*8], rcx
004F2A3C  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F2A45  41 0F B7 C9                     movzx ecx, r9w
004F2A49  42 8D 04 19                     lea eax, [rcx + r11]
004F2A4D  44 3B D8                        cmp r11d, eax
004F2A50  73 59                           jae 0x1404f2aab
004F2A52  4C 8D 85 90 02 00 00            lea r8, [rbp + 0x290]
004F2A59  44 8B D1                        mov r10d, ecx
004F2A5C  4F 8D 04 58                     lea r8, [r8 + r11*2]
004F2A60  45 0F B7 08                     movzx r9d, word ptr [r8]
004F2A64  8D 4A 01                        lea ecx, [rdx + 1]
004F2A67  8B C2                           mov eax, edx
004F2A69  48 03 C9                        add rcx, rcx
004F2A6C  48 03 C0                        add rax, rax
004F2A6F  4C 89 04 C3                     mov qword ptr [rbx + rax*8], r8
004F2A73  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F2A7C  66 45 3B 0E                     cmp r9w, word ptr [r14]
004F2A80  73 09                           jae 0x1404f2a8b
004F2A82  49 FF C1                        inc r9
004F2A85  4F 8D 0C CE                     lea r9, [r14 + r9*8]
004F2A89  EB 07                           jmp 0x1404f2a92
004F2A8B  4C 8D 0D E6 4F 97 00            lea r9, [rip + 0x974fe6]
004F2A92  83 C2 02                        add edx, 2
004F2A95  4C 89 0C CB                     mov qword ptr [rbx + rcx*8], r9
004F2A99  49 83 C0 02                     add r8, 2
004F2A9D  48 C7 44 CB 08 08 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 8
004F2AA6  4D 2B D7                        sub r10, r15
004F2AA9  75 B5                           jne 0x1404f2a60
004F2AAB  4C 8B B5 18 05 00 00            mov r14, qword ptr [rbp + 0x518]
004F2AB2  48 85 F6                        test rsi, rsi
004F2AB5  4C 8B D6                        mov r10, rsi
004F2AB8  44 8B DF                        mov r11d, edi
004F2ABB  4D 0F 44 D6                     cmove r10, r14
004F2ABF  45 0F B7 CC                     movzx r9d, r12w
004F2AC3  45 8B C4                        mov r8d, r12d
004F2AC6  B8 20 00 00 00                  mov eax, 0x20
004F2ACB  66 45 3B 02                     cmp r8w, word ptr [r10]
004F2ACF  73 22                           jae 0x1404f2af3
004F2AD1  41 0F B7 C0                     movzx eax, r8w
004F2AD5  4D 39 64 C2 08                  cmp qword ptr [r10 + rax*8 + 8], r12
004F2ADA  74 12                           je 0x1404f2aee
004F2ADC  8B C7                           mov eax, edi
004F2ADE  41 03 FF                        add edi, r15d
004F2AE1  66 45 03 CF                     add r9w, r15w
004F2AE5  66 44 89 84 45 90 02 00 00      mov word ptr [rbp + rax*2 + 0x290], r8w
004F2AEE  B8 20 00 00 00                  mov eax, 0x20
004F2AF3  45 03 C7                        add r8d, r15d
004F2AF6  44 3B C0                        cmp r8d, eax
004F2AF9  72 D0                           jb 0x1404f2acb
004F2AFB  66 44 89 8D 8C 02 00 00         mov word ptr [rbp + 0x28c], r9w
004F2B03  48 85 F6                        test rsi, rsi
004F2B06  75 1C                           jne 0x1404f2b24
004F2B08  8B C2                           mov eax, edx
004F2B0A  48 8D 8D 8C 02 00 00            lea rcx, [rbp + 0x28c]
004F2B11  48 03 C0                        add rax, rax
004F2B14  41 03 D7                        add edx, r15d
004F2B17  48 89 0C C3                     mov qword ptr [rbx + rax*8], rcx
004F2B1B  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F2B24  41 0F B7 C9                     movzx ecx, r9w
004F2B28  42 8D 04 19                     lea eax, [rcx + r11]
004F2B2C  44 3B D8                        cmp r11d, eax
004F2B2F  73 59                           jae 0x1404f2b8a
004F2B31  4C 8D 85 90 02 00 00            lea r8, [rbp + 0x290]
004F2B38  44 8B D1                        mov r10d, ecx
004F2B3B  4F 8D 04 58                     lea r8, [r8 + r11*2]
004F2B3F  45 0F B7 08                     movzx r9d, word ptr [r8]
004F2B43  8D 4A 01                        lea ecx, [rdx + 1]
004F2B46  8B C2                           mov eax, edx
004F2B48  48 03 C9                        add rcx, rcx
004F2B4B  48 03 C0                        add rax, rax
004F2B4E  4C 89 04 C3                     mov qword ptr [rbx + rax*8], r8
004F2B52  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F2B5B  66 45 3B 0E                     cmp r9w, word ptr [r14]
004F2B5F  73 09                           jae 0x1404f2b6a
004F2B61  49 FF C1                        inc r9
004F2B64  4F 8D 0C CE                     lea r9, [r14 + r9*8]
004F2B68  EB 07                           jmp 0x1404f2b71
004F2B6A  4C 8D 0D 07 4F 97 00            lea r9, [rip + 0x974f07]
004F2B71  83 C2 02                        add edx, 2
004F2B74  4C 89 0C CB                     mov qword ptr [rbx + rcx*8], r9
004F2B78  49 83 C0 02                     add r8, 2
004F2B7C  48 C7 44 CB 08 08 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 8
004F2B85  4D 2B D7                        sub r10, r15
004F2B88  75 B5                           jne 0x1404f2b3f
004F2B8A  4C 8B B5 20 05 00 00            mov r14, qword ptr [rbp + 0x520]
004F2B91  48 85 F6                        test rsi, rsi
004F2B94  4C 8B D6                        mov r10, rsi
004F2B97  44 8B DF                        mov r11d, edi
004F2B9A  4D 0F 44 D6                     cmove r10, r14
004F2B9E  45 0F B7 CC                     movzx r9d, r12w
004F2BA2  45 8B C4                        mov r8d, r12d
004F2BA5  B8 20 00 00 00                  mov eax, 0x20
004F2BAA  66 45 3B 02                     cmp r8w, word ptr [r10]
004F2BAE  73 22                           jae 0x1404f2bd2
004F2BB0  41 0F B7 C0                     movzx eax, r8w
004F2BB4  4D 39 64 C2 08                  cmp qword ptr [r10 + rax*8 + 8], r12
004F2BB9  74 12                           je 0x1404f2bcd
004F2BBB  8B C7                           mov eax, edi
004F2BBD  41 03 FF                        add edi, r15d
004F2BC0  66 45 03 CF                     add r9w, r15w
004F2BC4  66 44 89 84 45 90 02 00 00      mov word ptr [rbp + rax*2 + 0x290], r8w
004F2BCD  B8 20 00 00 00                  mov eax, 0x20
004F2BD2  45 03 C7                        add r8d, r15d
004F2BD5  44 3B C0                        cmp r8d, eax
004F2BD8  72 D0                           jb 0x1404f2baa
004F2BDA  66 44 89 8D 8E 02 00 00         mov word ptr [rbp + 0x28e], r9w
004F2BE2  48 85 F6                        test rsi, rsi
004F2BE5  75 1C                           jne 0x1404f2c03
004F2BE7  8B C2                           mov eax, edx
004F2BE9  48 8D 8D 8E 02 00 00            lea rcx, [rbp + 0x28e]
004F2BF0  48 03 C0                        add rax, rax
004F2BF3  41 03 D7                        add edx, r15d
004F2BF6  48 89 0C C3                     mov qword ptr [rbx + rax*8], rcx
004F2BFA  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F2C03  41 0F B7 C9                     movzx ecx, r9w
004F2C07  42 8D 04 19                     lea eax, [rcx + r11]
004F2C0B  44 3B D8                        cmp r11d, eax
004F2C0E  73 59                           jae 0x1404f2c69
004F2C10  4C 8D 85 90 02 00 00            lea r8, [rbp + 0x290]
004F2C17  44 8B D1                        mov r10d, ecx
004F2C1A  4F 8D 04 58                     lea r8, [r8 + r11*2]
004F2C1E  45 0F B7 08                     movzx r9d, word ptr [r8]
004F2C22  8D 4A 01                        lea ecx, [rdx + 1]
004F2C25  8B C2                           mov eax, edx
004F2C27  48 03 C9                        add rcx, rcx
004F2C2A  48 03 C0                        add rax, rax
004F2C2D  4C 89 04 C3                     mov qword ptr [rbx + rax*8], r8
004F2C31  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F2C3A  66 45 3B 0E                     cmp r9w, word ptr [r14]
004F2C3E  73 09                           jae 0x1404f2c49
004F2C40  49 FF C1                        inc r9
004F2C43  4F 8D 0C CE                     lea r9, [r14 + r9*8]
004F2C47  EB 07                           jmp 0x1404f2c50
004F2C49  4C 8D 0D 28 4E 97 00            lea r9, [rip + 0x974e28]
004F2C50  83 C2 02                        add edx, 2
004F2C53  4C 89 0C CB                     mov qword ptr [rbx + rcx*8], r9
004F2C57  49 83 C0 02                     add r8, 2
004F2C5B  48 C7 44 CB 08 08 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 8
004F2C64  4D 2B D7                        sub r10, r15
004F2C67  75 B5                           jne 0x1404f2c1e
004F2C69  8B CA                           mov ecx, edx
004F2C6B  49 8D 45 08                     lea rax, [r13 + 8]
004F2C6F  48 03 C9                        add rcx, rcx
004F2C72  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
004F2C77  45 33 C9                        xor r9d, r9d
004F2C7A  45 33 C0                        xor r8d, r8d
004F2C7D  48 89 04 CB                     mov qword ptr [rbx + rcx*8], rax
004F2C81  48 8D 85 F0 04 00 00            lea rax, [rbp + 0x4f0]
004F2C88  48 C7 44 CB 08 02 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 2
004F2C91  8D 4A 01                        lea ecx, [rdx + 1]
004F2C94  48 03 C9                        add rcx, rcx
004F2C97  48 89 04 CB                     mov qword ptr [rbx + rcx*8], rax
004F2C9B  48 8D 85 28 05 00 00            lea rax, [rbp + 0x528]
004F2CA2  48 C7 44 CB 08 02 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 2
004F2CAB  8D 4A 02                        lea ecx, [rdx + 2]
004F2CAE  48 03 C9                        add rcx, rcx
004F2CB1  48 89 04 CB                     mov qword ptr [rbx + rcx*8], rax
004F2CB5  48 8D 85 30 05 00 00            lea rax, [rbp + 0x530]
004F2CBC  48 C7 44 CB 08 04 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 4
004F2CC5  8D 4A 03                        lea ecx, [rdx + 3]
004F2CC8  48 03 C9                        add rcx, rcx
004F2CCB  48 89 04 CB                     mov qword ptr [rbx + rcx*8], rax
004F2CCF  48 8D 44 24 40                  lea rax, [rsp + 0x40]
004F2CD4  48 C7 44 CB 08 04 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 4
004F2CDD  8D 4A 04                        lea ecx, [rdx + 4]
004F2CE0  48 03 C9                        add rcx, rcx
004F2CE3  48 89 04 CB                     mov qword ptr [rbx + rcx*8], rax
004F2CE7  49 8D 45 06                     lea rax, [r13 + 6]
004F2CEB  4C 89 7C CB 08                  mov qword ptr [rbx + rcx*8 + 8], r15
004F2CF0  8D 4A 05                        lea ecx, [rdx + 5]
004F2CF3  48 03 C9                        add rcx, rcx
004F2CF6  48 89 04 CB                     mov qword ptr [rbx + rcx*8], rax
004F2CFA  8D 42 06                        lea eax, [rdx + 6]
004F2CFD  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F2D01  48 8D 15 F0 90 B2 FF            lea rdx, [rip - 0x4d6f10]
004F2D08  48 C7 44 CB 08 02 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 2
004F2D11  48 8B 0D D0 56 A1 00            mov rcx, qword ptr [rip + 0xa156d0]
004F2D18  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
004F2D1D  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
004F2D22  E8 A9 C3 D6 FF                  call 0x14025f0d0
004F2D27  48 8B 8D 90 04 00 00            mov rcx, qword ptr [rbp + 0x490]
004F2D2E  48 33 CC                        xor rcx, rsp
004F2D31  E8 0A 99 1B 00                  call 0x1406ac640
004F2D36  48 8B 9C 24 E0 05 00 00         mov rbx, qword ptr [rsp + 0x5e0]
004F2D3E  48 81 C4 A0 05 00 00            add rsp, 0x5a0
004F2D45  41 5F                           pop r15
004F2D47  41 5E                           pop r14
004F2D49  41 5D                           pop r13
004F2D4B  41 5C                           pop r12
004F2D4D  5F                              pop rdi
004F2D4E  5E                              pop rsi
004F2D4F  5D                              pop rbp
004F2D50  C3                              ret
004F2D51  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmEventTraceSoftCoreParkingSelectionEx(__int64 a1, int a2, unsigned __int16 a3, unsigned __int16 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m580;
    unsigned __int64 v_stack_m588;
    unsigned __int8 v_stack_m598;
    unsigned __int64 v_stack_m5A0;
    unsigned int v_stack_m5A8;
    unsigned __int64 v_stack_m5B0;
    unsigned __int64 v_stack_m5B8;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int16 *)(v_rsp + 32) = a4;
    *(unsigned __int16 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (0x5A0ULL);
    result = (*(unsigned __int64 *)(v_rip + 9536235)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 1240 + 1168) = result;
    v_r12 = 0;
    if (*(unsigned __int64 *)(v_rip + 9917962) == 0) goto loc_004F2D27;
    a2 = 0;
    result = memset(v_rsp - 1240 + 104, a2, 256, a4);
    a2 = 0;
    result = memset(v_rsp - 1240 + 376, a2, 256, a4);
    a2 = 0;
    result = memset(v_stack_m580, a2, 256, a4);
    if ((*(unsigned __int8 *)(v_rip + 9917828)) == 0) goto loc_004F2D27;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 10575654), v_rip - 5072593, 256, a4);
    if ((unsigned __int8)(result) == 0) goto loc_004F2D27;
    *(unsigned __int64 *)(v_rsp - 1240 + 96) = 0x200001ULL;
    v_r13 = ((unsigned int)(a2) + (unsigned int)(a2) * 4) << (7);
    v_r13 = (v_r13) + (*(unsigned __int64 *)(a1 + 1288));
    a2 = 0;
    result = memset(v_rsp - 1240 + 104, a2, 256, a4);
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 1240 + 368) = 0x200001ULL;
    result = memset(v_rsp - 1240 + 376, a2, 256, a4);
    a2 = 0;
    v_stack_m588 = 0x200001ULL;
    result = memset(v_stack_m580, a2, 256, a4);
    result = KeAndAffinityEx2(a1 + 576, v_r13 + 40, v_stack_m588, a4);
    result = KeAndAffinityEx2(a1 + 312, v_r13 + 40, v_rsp - 1240 + 96, a4);
    result = KeAndAffinityEx2(a1 + 840, v_r13 + 40, v_rsp - 1240 + 368, a4);
    v_stack_m598 = (unsigned __int8)((unsigned int)(a2));
loc_004F2586:
    if (0 >= (*(unsigned __int16 *)(v_r13 + 40))) goto loc_004F25AB;
    result = 0;
    v_rdi = 0;
    if ((*(unsigned __int64 *)(v_r13 + 40 + 0 * 8 + 8)) != 0) {
        result = 0;
        v_rdi = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
        a3 = (unsigned __int16)((0) + ((unsigned __int16)(v_r12 + 1)));
        *(unsigned __int16 *)(v_rsp - 1240 + result * 2 + 656) = 0;
    }
loc_004F25AB:
    a2 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    if (a2 < 32) goto loc_004F2586;
    *(unsigned __int16 *)(v_rsp - 1240 + 640) = a3;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962)) = v_rsp - 1240 + 640;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + 8) = 2;
    if (0 >= a3) goto loc_004F2628;
loc_004F25E2:
    a1 = ((unsigned int)((unsigned int)(v_r12 + 1)) + 1) + ((unsigned int)((unsigned int)(v_r12 + 1)) + 1);
    result = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12 + 1))))) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12 + 1)))));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8) = v_rsp - 1240 + 656;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8 + 8) = 2;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 1240 + 656))) >= (*(unsigned __int16 *)(v_r13 + 40))) goto loc_004F2609;
    a3 = (*(unsigned __int16 *)(v_rsp - 1240 + 656)) + 1;
    goto loc_004F2610;
loc_004F2609:
loc_004F2610:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r12 + 1))) + (2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8) = v_rip + 9917544;
    a4 = (v_rsp - 1240 + 656) + (2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8 + 8) = 8;
    v_r10 = (a3) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_004F25E2;
loc_004F2628:
    v_r10 = v_stack_m588;
    if (v_r13 + 40 != 0) { v_r10 = v_r13 + 40; }
loc_004F2643:
    if (0 >= (*(unsigned __int16 *)(v_r10))) goto loc_004F266B;
    result = 0;
    if ((*(unsigned __int64 *)(v_r10 + 0 * 8 + 8)) != 0) {
        result = (unsigned int)(v_rdi);
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_r12 + 1)));
        a4 = (unsigned __int16)((0) + ((unsigned __int16)(v_r12 + 1)));
        *(unsigned __int16 *)(v_rsp - 1240 + result * 2 + 656) = 0;
    }
loc_004F266B:
    a3 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    if (a3 < 32) goto loc_004F2643;
    *(unsigned __int16 *)(v_rsp - 1240 + 642) = a4;
    result = 32;
    if (v_r13 + 40 == 0) {
        result = a2;
        a1 = v_rsp - 1240 + 642;
        result = (result) + (result);
        a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8) = a1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8 + 8) = 2;
    }
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= ((unsigned int)((unsigned int)((unsigned int)(v_rdi)) + a4 * 1))) goto loc_004F2704;
loc_004F26B9:
    a1 = (a2 + 1) + (a2 + 1);
    result = ((unsigned int)(a2)) + ((unsigned int)(a2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8) = v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8 + 8) = 2;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2))) >= ((unsigned __int16)(v_stack_m588))) goto loc_004F26E5;
    goto loc_004F26EC;
loc_004F26E5:
loc_004F26EC:
    a2 = (unsigned int)((a2) + (2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8) = v_rip + 9917324;
    a3 = (v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2) + (2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8 + 8) = 8;
    v_r10 = ((unsigned int)(a4)) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_004F26B9;
loc_004F2704:
    v_r10 = v_rsp - 1240 + 96;
    if (v_r13 + 40 != 0) { v_r10 = v_r13 + 40; }
loc_004F271E:
    if (0 >= (*(unsigned __int16 *)(v_r10))) goto loc_004F2746;
    result = 0;
    if ((*(unsigned __int64 *)(v_r10 + 0 * 8 + 8)) != 0) {
        result = (unsigned int)(v_rdi);
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_r12 + 1)));
        a4 = (unsigned __int16)((0) + ((unsigned __int16)(v_r12 + 1)));
        *(unsigned __int16 *)(v_rsp - 1240 + result * 2 + 656) = 0;
    }
loc_004F2746:
    a3 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    if (a3 < 32) goto loc_004F271E;
    *(unsigned __int16 *)(v_rsp - 1240 + 644) = a4;
    result = 32;
    if (v_r13 + 40 == 0) {
        result = a2;
        a1 = v_rsp - 1240 + 644;
        result = (result) + (result);
        a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8) = a1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8 + 8) = 2;
    }
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= ((unsigned int)((unsigned int)((unsigned int)(v_rdi)) + a4 * 1))) goto loc_004F27DD;
loc_004F2793:
    a1 = (a2 + 1) + (a2 + 1);
    result = ((unsigned int)(a2)) + ((unsigned int)(a2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8) = v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8 + 8) = 2;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2))) >= ((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 1240 + 96)))) goto loc_004F27BE;
    goto loc_004F27C5;
loc_004F27BE:
loc_004F27C5:
    a2 = (unsigned int)((a2) + (2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8) = v_rip + 9917107;
    a3 = (v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2) + (2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8 + 8) = 8;
    v_r10 = ((unsigned int)(a4)) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_004F2793;
loc_004F27DD:
    v_r10 = v_rsp - 1240 + 368;
    if (v_r13 + 40 != 0) { v_r10 = v_r13 + 40; }
loc_004F27FA:
    if (0 >= (*(unsigned __int16 *)(v_r10))) goto loc_004F2822;
    result = 0;
    if ((*(unsigned __int64 *)(v_r10 + 0 * 8 + 8)) != 0) {
        result = (unsigned int)(v_rdi);
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_r12 + 1)));
        a4 = (unsigned __int16)((0) + ((unsigned __int16)(v_r12 + 1)));
        *(unsigned __int16 *)(v_rsp - 1240 + result * 2 + 656) = 0;
    }
loc_004F2822:
    a3 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    if (a3 < 32) goto loc_004F27FA;
    *(unsigned __int16 *)(v_rsp - 1240 + 646) = a4;
    result = 32;
    if (v_r13 + 40 == 0) {
        result = a2;
        a1 = v_rsp - 1240 + 646;
        result = (result) + (result);
        a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8) = a1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8 + 8) = 2;
    }
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= ((unsigned int)((unsigned int)((unsigned int)(v_rdi)) + a4 * 1))) goto loc_004F28BF;
loc_004F2872:
    a1 = (a2 + 1) + (a2 + 1);
    result = ((unsigned int)(a2)) + ((unsigned int)(a2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8) = v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8 + 8) = 2;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2))) >= ((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 1240 + 368)))) goto loc_004F28A0;
    goto loc_004F28A7;
loc_004F28A0:
loc_004F28A7:
    a2 = (unsigned int)((a2) + (2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8) = v_rip + 9916881;
    a3 = (v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2) + (2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8 + 8) = 8;
    v_r10 = ((unsigned int)(a4)) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_004F2872;
loc_004F28BF:
    result = ((unsigned int)(a2)) + ((unsigned int)(a2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8) = v_rsp - 1240 + 1272;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8 + 8) = 2;
    a1 = (a2 + 1) + (a2 + 1);
    a2 = (unsigned int)((a2) + (2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8 + 8) = 2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8) = v_rsp - 1240 + 1280;
    v_r10 = v_r13 + 40;
    if (v_r13 + 40 == 0) { v_r10 = *(unsigned __int64 *)(v_rsp - 1240 + 1288); }
loc_004F290D:
    if (0 >= (*(unsigned __int16 *)(v_r10))) goto loc_004F2935;
    result = 0;
    if ((*(unsigned __int64 *)(v_r10 + 0 * 8 + 8)) != 0) {
        result = (unsigned int)(v_rdi);
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_r12 + 1)));
        a4 = (unsigned __int16)((0) + ((unsigned __int16)(v_r12 + 1)));
        *(unsigned __int16 *)(v_rsp - 1240 + result * 2 + 656) = 0;
    }
loc_004F2935:
    a3 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    if (a3 < 32) goto loc_004F290D;
    *(unsigned __int16 *)(v_rsp - 1240 + 648) = a4;
    result = 32;
    if (v_r13 + 40 == 0) {
        result = a2;
        a1 = v_rsp - 1240 + 648;
        result = (result) + (result);
        a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8) = a1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8 + 8) = 2;
    }
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= ((unsigned int)((unsigned int)((unsigned int)(v_rdi)) + a4 * 1))) goto loc_004F29CC;
loc_004F2981:
    a1 = (a2 + 1) + (a2 + 1);
    result = ((unsigned int)(a2)) + ((unsigned int)(a2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8) = v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8 + 8) = 2;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 1240 + 1288)))) goto loc_004F29AC;
    a4 = (*(unsigned __int16 *)(v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2)) + 1;
    goto loc_004F29B3;
loc_004F29AC:
loc_004F29B3:
    a2 = (unsigned int)((a2) + (2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8) = v_rip + 9916613;
    a3 = (v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2) + (2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8 + 8) = 8;
    v_r10 = ((unsigned int)(a4)) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_004F2981;
loc_004F29CC:
    v_r10 = v_r13 + 40;
    if (v_r13 + 40 == 0) { v_r10 = *(unsigned __int64 *)(v_rsp - 1240 + 1296); }
loc_004F29EC:
    if (0 >= (*(unsigned __int16 *)(v_r10))) goto loc_004F2A14;
    result = 0;
    if ((*(unsigned __int64 *)(v_r10 + 0 * 8 + 8)) != 0) {
        result = (unsigned int)(v_rdi);
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_r12 + 1)));
        a4 = (unsigned __int16)((0) + ((unsigned __int16)(v_r12 + 1)));
        *(unsigned __int16 *)(v_rsp - 1240 + result * 2 + 656) = 0;
    }
loc_004F2A14:
    a3 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    if (a3 < 32) goto loc_004F29EC;
    *(unsigned __int16 *)(v_rsp - 1240 + 650) = a4;
    result = 32;
    if (v_r13 + 40 == 0) {
        result = a2;
        a1 = v_rsp - 1240 + 650;
        result = (result) + (result);
        a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8) = a1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8 + 8) = 2;
    }
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= ((unsigned int)(a4 + (unsigned int)((unsigned int)(v_rdi)) * 1))) goto loc_004F2AAB;
loc_004F2A60:
    a1 = (a2 + 1) + (a2 + 1);
    result = ((unsigned int)(a2)) + ((unsigned int)(a2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8) = v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8 + 8) = 2;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 1240 + 1296)))) goto loc_004F2A8B;
    a4 = (*(unsigned __int16 *)(v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2)) + 1;
    goto loc_004F2A92;
loc_004F2A8B:
loc_004F2A92:
    a2 = (unsigned int)((a2) + (2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8) = v_rip + 9916390;
    a3 = (v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2) + (2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8 + 8) = 8;
    v_r10 = ((unsigned int)(a4)) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_004F2A60;
loc_004F2AAB:
    v_r10 = v_r13 + 40;
    if (v_r13 + 40 == 0) { v_r10 = *(unsigned __int64 *)(v_rsp - 1240 + 1304); }
loc_004F2ACB:
    if (0 >= (*(unsigned __int16 *)(v_r10))) goto loc_004F2AF3;
    result = 0;
    if ((*(unsigned __int64 *)(v_r10 + 0 * 8 + 8)) != 0) {
        result = (unsigned int)(v_rdi);
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_r12 + 1)));
        a4 = (unsigned __int16)((0) + ((unsigned __int16)(v_r12 + 1)));
        *(unsigned __int16 *)(v_rsp - 1240 + result * 2 + 656) = 0;
    }
loc_004F2AF3:
    a3 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    if (a3 < 32) goto loc_004F2ACB;
    *(unsigned __int16 *)(v_rsp - 1240 + 652) = a4;
    result = 32;
    if (v_r13 + 40 == 0) {
        result = a2;
        a1 = v_rsp - 1240 + 652;
        result = (result) + (result);
        a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8) = a1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8 + 8) = 2;
    }
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= ((unsigned int)(a4 + (unsigned int)((unsigned int)(v_rdi)) * 1))) goto loc_004F2B8A;
loc_004F2B3F:
    a1 = (a2 + 1) + (a2 + 1);
    result = ((unsigned int)(a2)) + ((unsigned int)(a2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8) = v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8 + 8) = 2;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 1240 + 1304)))) goto loc_004F2B6A;
    a4 = (*(unsigned __int16 *)(v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2)) + 1;
    goto loc_004F2B71;
loc_004F2B6A:
loc_004F2B71:
    a2 = (unsigned int)((a2) + (2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8) = v_rip + 9916167;
    a3 = (v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2) + (2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8 + 8) = 8;
    v_r10 = ((unsigned int)(a4)) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_004F2B3F;
loc_004F2B8A:
    v_r10 = v_r13 + 40;
    if (v_r13 + 40 == 0) { v_r10 = *(unsigned __int64 *)(v_rsp - 1240 + 1312); }
loc_004F2BAA:
    if (0 >= (*(unsigned __int16 *)(v_r10))) goto loc_004F2BD2;
    result = 0;
    if ((*(unsigned __int64 *)(v_r10 + 0 * 8 + 8)) != 0) {
        result = (unsigned int)(v_rdi);
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_r12 + 1)));
        a4 = (unsigned __int16)((0) + ((unsigned __int16)(v_r12 + 1)));
        *(unsigned __int16 *)(v_rsp - 1240 + result * 2 + 656) = 0;
    }
loc_004F2BD2:
    a3 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    if (a3 < 32) goto loc_004F2BAA;
    *(unsigned __int16 *)(v_rsp - 1240 + 654) = a4;
    result = 32;
    if (v_r13 + 40 == 0) {
        result = a2;
        a1 = v_rsp - 1240 + 654;
        result = (result) + (result);
        a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8) = a1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8 + 8) = 2;
    }
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= ((unsigned int)(a4 + (unsigned int)((unsigned int)(v_rdi)) * 1))) goto loc_004F2C69;
loc_004F2C1E:
    a1 = (a2 + 1) + (a2 + 1);
    result = ((unsigned int)(a2)) + ((unsigned int)(a2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8) = v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + result * 8 + 8) = 2;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 1240 + 1312)))) goto loc_004F2C49;
    a4 = (*(unsigned __int16 *)(v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2)) + 1;
    goto loc_004F2C50;
loc_004F2C49:
loc_004F2C50:
    a2 = (unsigned int)((a2) + (2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8) = v_rip + 9915944;
    a3 = (v_rsp - 1240 + 656 + (unsigned int)((unsigned int)(v_rdi)) * 2) + (2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8 + 8) = 8;
    v_r10 = ((unsigned int)(a4)) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_004F2C1E;
loc_004F2C69:
    a1 = ((unsigned int)(a2)) + ((unsigned int)(a2));
    v_stack_m5A0 = *(unsigned __int64 *)(v_rip + 9917962);
    a4 = 0;
    a3 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8) = v_r13 + 8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8 + 8) = 2;
    a1 = (a2 + 1) + (a2 + 1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8) = v_rsp - 1240 + 1264;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8 + 8) = 2;
    a1 = (a2 + 2) + (a2 + 2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8) = v_rsp - 1240 + 1320;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8 + 8) = 4;
    a1 = (a2 + 3) + (a2 + 3);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8) = v_rsp - 1240 + 1328;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8 + 8) = 4;
    a1 = (a2 + 4) + (a2 + 4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8) = v_stack_m598;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8 + 8) = v_r12 + 1;
    a1 = (a2 + 5) + (a2 + 5);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8) = v_r13 + 6;
    v_stack_m5A8 = (unsigned int)(a2 + 6);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9917962) + a1 * 8 + 8) = 2;
    v_stack_m5B0 = 0;
    v_stack_m5B8 = 0;
    result = EtwWriteEx(*(unsigned __int64 *)(v_rip + 10573520), v_rip - 5074704, a3, a4);
loc_004F2D27:
    a1 = (*(unsigned __int64 *)(v_rsp - 1240 + 1168)) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip - 5074704, a3, a4);
    v_rsp = (v_rsp) + (0x5A0ULL);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmEventTraceSoftCoreParkingSelectionEx(void *Arg1, void *Arg2, uint16_t Arg3, uint16_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m580;
    uint64_t v_stack_m588;
    uint8_t v_stack_m598;
    uint64_t v_stack_m5A0;
    uint32_t v_stack_m5A8;
    uint64_t v_stack_m5B0;
    uint64_t v_stack_m5B8;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint16_t *)(local_rsp + 0x20) = Arg4;
    *(uint16_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (0x5A0ULL);
    result = (*(uint64_t *)(v_rip + 0x9182EB)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x4D8 + 0x490) = result;
    local_r12 = 0;
    if (*(uint64_t *)(v_rip + 0x97560A) == 0) goto loc_004F2D27;
    Arg2 = 0;
    result = memset(local_rsp - 1240 + 104, Arg2, 256, Arg4);
    Arg2 = 0;
    result = memset(local_rsp - 1240 + 376, Arg2, 256, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m580, Arg2, 256, Arg4);
    if ((*(uint8_t *)(v_rip + 0x975584)) == 0) goto loc_004F2D27;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xA15F26), v_rip - 5072593, 256, Arg4);
    if ((uint8_t)(result) == 0) goto loc_004F2D27;
    *(uint64_t *)(local_rsp - 0x4D8 + 0x60) = 0x200001ULL;
    local_r13 = ((uint32_t)(Arg2) + (uint32_t)(Arg2) * 4) << (7);
    local_r13 = (local_r13) + (*(uint64_t *)(arg1 + 0x508));
    Arg2 = 0;
    result = memset(local_rsp - 1240 + 104, Arg2, 256, Arg4);
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0x4D8 + 0x170) = 0x200001ULL;
    result = memset(local_rsp - 1240 + 376, Arg2, 256, Arg4);
    Arg2 = 0;
    v_stack_m588 = 0x200001ULL;
    result = memset(v_stack_m580, Arg2, 256, Arg4);
    result = KeAndAffinityEx2(Arg1 + 576, local_r13 + 40, v_stack_m588, Arg4);
    result = KeAndAffinityEx2(Arg1 + 312, local_r13 + 40, local_rsp - 1240 + 96, Arg4);
    result = KeAndAffinityEx2(Arg1 + 840, local_r13 + 40, local_rsp - 1240 + 368, Arg4);
    v_stack_m598 = (uint8_t)((uint32_t)(Arg2));
loc_004F2586:
    if (0 >= (*(uint16_t *)(local_r13 + 0x28))) goto loc_004F25AB;
    result = 0;
    local_rdi = 0;
    if ((*(uint64_t *)(local_r13 + 0x28 + 0x0 * 8 + 0x8)) != 0) {
        result = 0;
        local_rdi = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
        Arg3 = (uint16_t)((0) + ((uint16_t)(local_r12 + 1)));
        *(uint16_t *)(local_rsp - 0x4D8 + result * 2 + 0x290) = 0;
    }
loc_004F25AB:
    Arg2 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    if (Arg2 < 32) goto loc_004F2586;
    *(uint16_t *)(local_rsp - 0x4D8 + 0x280) = Arg3;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A)) = local_rsp - 1240 + 640;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + 0x8) = 2;
    if (0 >= Arg3) goto loc_004F2628;
loc_004F25E2:
    Arg1 = ((uint32_t)((uint32_t)(local_r12 + 1)) + 1) + ((uint32_t)((uint32_t)(local_r12 + 1)) + 1);
    result = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12 + 1))))) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12 + 1)))));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8) = local_rsp - 1240 + 656;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8 + 0x8) = 2;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x4D8 + 0x290))) >= (*(uint16_t *)(local_r13 + 0x28))) goto loc_004F2609;
    Arg3 = (*(uint16_t *)(local_rsp - 0x4D8 + 0x290)) + 1;
    goto loc_004F2610;
loc_004F2609:
loc_004F2610:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r12 + 1))) + (2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8) = v_rip + 9917544;
    Arg4 = (local_rsp - 1240 + 656) + (2);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8 + 0x8) = 8;
    local_r10 = (Arg3) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_004F25E2;
loc_004F2628:
    local_r10 = v_stack_m588;
    if (local_r13 + 40 != 0) { local_r10 = local_r13 + 40; }
loc_004F2643:
    if (0 >= (*(uint16_t *)(local_r10))) goto loc_004F266B;
    result = 0;
    if ((*(uint64_t *)(local_r10 + 0x0 * 8 + 0x8)) != 0) {
        result = (uint32_t)(local_rdi);
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_r12 + 1)));
        Arg4 = (uint16_t)((0) + ((uint16_t)(local_r12 + 1)));
        *(uint16_t *)(local_rsp - 0x4D8 + result * 2 + 0x290) = 0;
    }
loc_004F266B:
    Arg3 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    if (Arg3 < 32) goto loc_004F2643;
    *(uint16_t *)(local_rsp - 0x4D8 + 0x282) = Arg4;
    result = 32;
    if (local_r13 + 40 == 0) {
        result = Arg2;
        Arg1 = local_rsp - 1240 + 642;
        result = (result) + (result);
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
        *(void **)(*(uint64_t *)(v_rip + 0x97560A) + result * 8) = Arg1;
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8 + 0x8) = 2;
    }
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= ((uint32_t)((uint32_t)((uint32_t)(local_rdi)) + Arg4 * 1))) goto loc_004F2704;
loc_004F26B9:
    Arg1 = (Arg2 + 1) + (Arg2 + 1);
    result = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8) = local_rsp - 1240 + 656 + (uint32_t)((uint32_t)(local_rdi)) * 2;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8 + 0x8) = 2;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x4D8 + 0x290 + (uint32_t)((uint32_t)(local_rdi)) * 2))) >= ((uint16_t)(v_stack_m588))) goto loc_004F26E5;
    goto loc_004F26EC;
loc_004F26E5:
loc_004F26EC:
    Arg2 = (uint32_t)((Arg2) + (2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8) = v_rip + 9917324;
    Arg3 = (local_rsp - 1240 + 656 + (uint32_t)((uint32_t)(local_rdi)) * 2) + (2);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8 + 0x8) = 8;
    local_r10 = ((uint32_t)(Arg4)) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_004F26B9;
loc_004F2704:
    local_r10 = local_rsp - 1240 + 96;
    if (local_r13 + 40 != 0) { local_r10 = local_r13 + 40; }
loc_004F271E:
    if (0 >= (*(uint16_t *)(local_r10))) goto loc_004F2746;
    result = 0;
    if ((*(uint64_t *)(local_r10 + 0x0 * 8 + 0x8)) != 0) {
        result = (uint32_t)(local_rdi);
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_r12 + 1)));
        Arg4 = (uint16_t)((0) + ((uint16_t)(local_r12 + 1)));
        *(uint16_t *)(local_rsp - 0x4D8 + result * 2 + 0x290) = 0;
    }
loc_004F2746:
    Arg3 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    if (Arg3 < 32) goto loc_004F271E;
    *(uint16_t *)(local_rsp - 0x4D8 + 0x284) = Arg4;
    result = 32;
    if (local_r13 + 40 == 0) {
        result = Arg2;
        Arg1 = local_rsp - 1240 + 644;
        result = (result) + (result);
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
        *(void **)(*(uint64_t *)(v_rip + 0x97560A) + result * 8) = Arg1;
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8 + 0x8) = 2;
    }
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= ((uint32_t)((uint32_t)((uint32_t)(local_rdi)) + Arg4 * 1))) goto loc_004F27DD;
loc_004F2793:
    Arg1 = (Arg2 + 1) + (Arg2 + 1);
    result = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8) = local_rsp - 1240 + 656 + (uint32_t)((uint32_t)(local_rdi)) * 2;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8 + 0x8) = 2;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x4D8 + 0x290 + (uint32_t)((uint32_t)(local_rdi)) * 2))) >= ((uint16_t)(*(uint16_t *)(local_rsp - 0x4D8 + 0x60)))) goto loc_004F27BE;
    goto loc_004F27C5;
loc_004F27BE:
loc_004F27C5:
    Arg2 = (uint32_t)((Arg2) + (2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8) = v_rip + 9917107;
    Arg3 = (local_rsp - 1240 + 656 + (uint32_t)((uint32_t)(local_rdi)) * 2) + (2);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8 + 0x8) = 8;
    local_r10 = ((uint32_t)(Arg4)) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_004F2793;
loc_004F27DD:
    local_r10 = local_rsp - 1240 + 368;
    if (local_r13 + 40 != 0) { local_r10 = local_r13 + 40; }
loc_004F27FA:
    if (0 >= (*(uint16_t *)(local_r10))) goto loc_004F2822;
    result = 0;
    if ((*(uint64_t *)(local_r10 + 0x0 * 8 + 0x8)) != 0) {
        result = (uint32_t)(local_rdi);
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_r12 + 1)));
        Arg4 = (uint16_t)((0) + ((uint16_t)(local_r12 + 1)));
        *(uint16_t *)(local_rsp - 0x4D8 + result * 2 + 0x290) = 0;
    }
loc_004F2822:
    Arg3 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    if (Arg3 < 32) goto loc_004F27FA;
    *(uint16_t *)(local_rsp - 0x4D8 + 0x286) = Arg4;
    result = 32;
    if (local_r13 + 40 == 0) {
        result = Arg2;
        Arg1 = local_rsp - 1240 + 646;
        result = (result) + (result);
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
        *(void **)(*(uint64_t *)(v_rip + 0x97560A) + result * 8) = Arg1;
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8 + 0x8) = 2;
    }
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= ((uint32_t)((uint32_t)((uint32_t)(local_rdi)) + Arg4 * 1))) goto loc_004F28BF;
loc_004F2872:
    Arg1 = (Arg2 + 1) + (Arg2 + 1);
    result = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8) = local_rsp - 1240 + 656 + (uint32_t)((uint32_t)(local_rdi)) * 2;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8 + 0x8) = 2;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x4D8 + 0x290 + (uint32_t)((uint32_t)(local_rdi)) * 2))) >= ((uint16_t)(*(uint16_t *)(local_rsp - 0x4D8 + 0x170)))) goto loc_004F28A0;
    goto loc_004F28A7;
loc_004F28A0:
loc_004F28A7:
    Arg2 = (uint32_t)((Arg2) + (2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8) = v_rip + 9916881;
    Arg3 = (local_rsp - 1240 + 656 + (uint32_t)((uint32_t)(local_rdi)) * 2) + (2);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8 + 0x8) = 8;
    local_r10 = ((uint32_t)(Arg4)) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_004F2872;
loc_004F28BF:
    result = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8) = local_rsp - 1240 + 1272;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8 + 0x8) = 2;
    Arg1 = (Arg2 + 1) + (Arg2 + 1);
    Arg2 = (uint32_t)((Arg2) + (2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8 + 0x8) = 2;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8) = local_rsp - 1240 + 1280;
    local_r10 = local_r13 + 40;
    if (local_r13 + 40 == 0) { local_r10 = *(uint64_t *)(local_rsp - 0x4D8 + 0x508); }
loc_004F290D:
    if (0 >= (*(uint16_t *)(local_r10))) goto loc_004F2935;
    result = 0;
    if ((*(uint64_t *)(local_r10 + 0x0 * 8 + 0x8)) != 0) {
        result = (uint32_t)(local_rdi);
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_r12 + 1)));
        Arg4 = (uint16_t)((0) + ((uint16_t)(local_r12 + 1)));
        *(uint16_t *)(local_rsp - 0x4D8 + result * 2 + 0x290) = 0;
    }
loc_004F2935:
    Arg3 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    if (Arg3 < 32) goto loc_004F290D;
    *(uint16_t *)(local_rsp - 0x4D8 + 0x288) = Arg4;
    result = 32;
    if (local_r13 + 40 == 0) {
        result = Arg2;
        Arg1 = local_rsp - 1240 + 648;
        result = (result) + (result);
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
        *(void **)(*(uint64_t *)(v_rip + 0x97560A) + result * 8) = Arg1;
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8 + 0x8) = 2;
    }
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= ((uint32_t)((uint32_t)((uint32_t)(local_rdi)) + Arg4 * 1))) goto loc_004F29CC;
loc_004F2981:
    Arg1 = (Arg2 + 1) + (Arg2 + 1);
    result = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8) = local_rsp - 1240 + 656 + (uint32_t)((uint32_t)(local_rdi)) * 2;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8 + 0x8) = 2;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x4D8 + 0x290 + (uint32_t)((uint32_t)(local_rdi)) * 2))) >= (*(uint16_t *)(*(uint64_t *)(local_rsp - 0x4D8 + 0x508)))) goto loc_004F29AC;
    Arg4 = (*(uint16_t *)(local_rsp - 0x4D8 + 0x290 + (uint32_t)((uint32_t)(local_rdi)) * 2)) + 1;
    goto loc_004F29B3;
loc_004F29AC:
loc_004F29B3:
    Arg2 = (uint32_t)((Arg2) + (2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8) = v_rip + 9916613;
    Arg3 = (local_rsp - 1240 + 656 + (uint32_t)((uint32_t)(local_rdi)) * 2) + (2);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8 + 0x8) = 8;
    local_r10 = ((uint32_t)(Arg4)) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_004F2981;
loc_004F29CC:
    local_r10 = local_r13 + 40;
    if (local_r13 + 40 == 0) { local_r10 = *(uint64_t *)(local_rsp - 0x4D8 + 0x510); }
loc_004F29EC:
    if (0 >= (*(uint16_t *)(local_r10))) goto loc_004F2A14;
    result = 0;
    if ((*(uint64_t *)(local_r10 + 0x0 * 8 + 0x8)) != 0) {
        result = (uint32_t)(local_rdi);
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_r12 + 1)));
        Arg4 = (uint16_t)((0) + ((uint16_t)(local_r12 + 1)));
        *(uint16_t *)(local_rsp - 0x4D8 + result * 2 + 0x290) = 0;
    }
loc_004F2A14:
    Arg3 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    if (Arg3 < 32) goto loc_004F29EC;
    *(uint16_t *)(local_rsp - 0x4D8 + 0x28A) = Arg4;
    result = 32;
    if (local_r13 + 40 == 0) {
        result = Arg2;
        Arg1 = local_rsp - 1240 + 650;
        result = (result) + (result);
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
        *(void **)(*(uint64_t *)(v_rip + 0x97560A) + result * 8) = Arg1;
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8 + 0x8) = 2;
    }
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= ((uint32_t)(Arg4 + (uint32_t)((uint32_t)(local_rdi)) * 1))) goto loc_004F2AAB;
loc_004F2A60:
    Arg1 = (Arg2 + 1) + (Arg2 + 1);
    result = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8) = local_rsp - 1240 + 656 + (uint32_t)((uint32_t)(local_rdi)) * 2;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8 + 0x8) = 2;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x4D8 + 0x290 + (uint32_t)((uint32_t)(local_rdi)) * 2))) >= (*(uint16_t *)(*(uint64_t *)(local_rsp - 0x4D8 + 0x510)))) goto loc_004F2A8B;
    Arg4 = (*(uint16_t *)(local_rsp - 0x4D8 + 0x290 + (uint32_t)((uint32_t)(local_rdi)) * 2)) + 1;
    goto loc_004F2A92;
loc_004F2A8B:
loc_004F2A92:
    Arg2 = (uint32_t)((Arg2) + (2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8) = v_rip + 9916390;
    Arg3 = (local_rsp - 1240 + 656 + (uint32_t)((uint32_t)(local_rdi)) * 2) + (2);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8 + 0x8) = 8;
    local_r10 = ((uint32_t)(Arg4)) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_004F2A60;
loc_004F2AAB:
    local_r10 = local_r13 + 40;
    if (local_r13 + 40 == 0) { local_r10 = *(uint64_t *)(local_rsp - 0x4D8 + 0x518); }
loc_004F2ACB:
    if (0 >= (*(uint16_t *)(local_r10))) goto loc_004F2AF3;
    result = 0;
    if ((*(uint64_t *)(local_r10 + 0x0 * 8 + 0x8)) != 0) {
        result = (uint32_t)(local_rdi);
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_r12 + 1)));
        Arg4 = (uint16_t)((0) + ((uint16_t)(local_r12 + 1)));
        *(uint16_t *)(local_rsp - 0x4D8 + result * 2 + 0x290) = 0;
    }
loc_004F2AF3:
    Arg3 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    if (Arg3 < 32) goto loc_004F2ACB;
    *(uint16_t *)(local_rsp - 0x4D8 + 0x28C) = Arg4;
    result = 32;
    if (local_r13 + 40 == 0) {
        result = Arg2;
        Arg1 = local_rsp - 1240 + 652;
        result = (result) + (result);
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
        *(void **)(*(uint64_t *)(v_rip + 0x97560A) + result * 8) = Arg1;
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8 + 0x8) = 2;
    }
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= ((uint32_t)(Arg4 + (uint32_t)((uint32_t)(local_rdi)) * 1))) goto loc_004F2B8A;
loc_004F2B3F:
    Arg1 = (Arg2 + 1) + (Arg2 + 1);
    result = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8) = local_rsp - 1240 + 656 + (uint32_t)((uint32_t)(local_rdi)) * 2;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8 + 0x8) = 2;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x4D8 + 0x290 + (uint32_t)((uint32_t)(local_rdi)) * 2))) >= (*(uint16_t *)(*(uint64_t *)(local_rsp - 0x4D8 + 0x518)))) goto loc_004F2B6A;
    Arg4 = (*(uint16_t *)(local_rsp - 0x4D8 + 0x290 + (uint32_t)((uint32_t)(local_rdi)) * 2)) + 1;
    goto loc_004F2B71;
loc_004F2B6A:
loc_004F2B71:
    Arg2 = (uint32_t)((Arg2) + (2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8) = v_rip + 9916167;
    Arg3 = (local_rsp - 1240 + 656 + (uint32_t)((uint32_t)(local_rdi)) * 2) + (2);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8 + 0x8) = 8;
    local_r10 = ((uint32_t)(Arg4)) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_004F2B3F;
loc_004F2B8A:
    local_r10 = local_r13 + 40;
    if (local_r13 + 40 == 0) { local_r10 = *(uint64_t *)(local_rsp - 0x4D8 + 0x520); }
loc_004F2BAA:
    if (0 >= (*(uint16_t *)(local_r10))) goto loc_004F2BD2;
    result = 0;
    if ((*(uint64_t *)(local_r10 + 0x0 * 8 + 0x8)) != 0) {
        result = (uint32_t)(local_rdi);
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_r12 + 1)));
        Arg4 = (uint16_t)((0) + ((uint16_t)(local_r12 + 1)));
        *(uint16_t *)(local_rsp - 0x4D8 + result * 2 + 0x290) = 0;
    }
loc_004F2BD2:
    Arg3 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    if (Arg3 < 32) goto loc_004F2BAA;
    *(uint16_t *)(local_rsp - 0x4D8 + 0x28E) = Arg4;
    result = 32;
    if (local_r13 + 40 == 0) {
        result = Arg2;
        Arg1 = local_rsp - 1240 + 654;
        result = (result) + (result);
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
        *(void **)(*(uint64_t *)(v_rip + 0x97560A) + result * 8) = Arg1;
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8 + 0x8) = 2;
    }
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= ((uint32_t)(Arg4 + (uint32_t)((uint32_t)(local_rdi)) * 1))) goto loc_004F2C69;
loc_004F2C1E:
    Arg1 = (Arg2 + 1) + (Arg2 + 1);
    result = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8) = local_rsp - 1240 + 656 + (uint32_t)((uint32_t)(local_rdi)) * 2;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + result * 8 + 0x8) = 2;
    if (((uint16_t)(*(uint16_t *)(local_rsp - 0x4D8 + 0x290 + (uint32_t)((uint32_t)(local_rdi)) * 2))) >= (*(uint16_t *)(*(uint64_t *)(local_rsp - 0x4D8 + 0x520)))) goto loc_004F2C49;
    Arg4 = (*(uint16_t *)(local_rsp - 0x4D8 + 0x290 + (uint32_t)((uint32_t)(local_rdi)) * 2)) + 1;
    goto loc_004F2C50;
loc_004F2C49:
loc_004F2C50:
    Arg2 = (uint32_t)((Arg2) + (2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8) = v_rip + 9915944;
    Arg3 = (local_rsp - 1240 + 656 + (uint32_t)((uint32_t)(local_rdi)) * 2) + (2);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8 + 0x8) = 8;
    local_r10 = ((uint32_t)(Arg4)) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_004F2C1E;
loc_004F2C69:
    Arg1 = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    v_stack_m5A0 = *(uint64_t *)(v_rip + 0x97560A);
    Arg4 = 0;
    Arg3 = 0;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8) = local_r13 + 8;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8 + 0x8) = 2;
    Arg1 = (Arg2 + 1) + (Arg2 + 1);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8) = local_rsp - 1240 + 1264;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8 + 0x8) = 2;
    Arg1 = (Arg2 + 2) + (Arg2 + 2);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8) = local_rsp - 1240 + 1320;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8 + 0x8) = 4;
    Arg1 = (Arg2 + 3) + (Arg2 + 3);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8) = local_rsp - 1240 + 1328;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8 + 0x8) = 4;
    Arg1 = (Arg2 + 4) + (Arg2 + 4);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8) = v_stack_m598;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8 + 0x8) = local_r12 + 1;
    Arg1 = (Arg2 + 5) + (Arg2 + 5);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8) = local_r13 + 6;
    v_stack_m5A8 = (uint32_t)(Arg2 + 6);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97560A) + arg1 * 8 + 0x8) = 2;
    v_stack_m5B0 = 0;
    v_stack_m5B8 = 0;
    result = EtwWriteEx(*(uint64_t *)(v_rip + 0xA156D0), v_rip - 5074704, Arg3, Arg4);
loc_004F2D27:
    Arg1 = (*(uint64_t *)(local_rsp - 0x4D8 + 0x490)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip - 5074704, Arg3, Arg4);
    local_rsp = (local_rsp) + (0x5A0ULL);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x138` | `64` | `R` |
| `Arg1` | `+ 0x240` | `64` | `R` |
| `Arg1` | `+ 0x348` | `64` | `R` |
| `Arg1` | `+ 0x508` | `64` | `R` |
| `Arg2` | `+ 0x0 + r15*4` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F2424&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
