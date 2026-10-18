# IvtFlushTbInternal

- RVA: `0x002D2548`–`0x002D2C82` (길이 `1,850` bytes)
- VA: `0x00000001402D2548`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006F93C`
- 디코드: `455`개 명령, `1,850/1,850` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x002D26EA` → [IvtIommuSendCommand](../46/IvtIommuSendCommand_function_0046A6E4.md) (function, `0x0046A6E4`)
- `0x002D277E` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x002D27D4` → [IvtIommuWaitCommand](../46/IvtIommuWaitCommand_function_0046A594.md) (function, `0x0046A594`)
- `0x002D2811` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002D28A5` → [HalpIommuGetNextFlushDevice](../4F/HalpIommuGetNextFlushDevice_function_004FB8E8.md) (function, `0x004FB8E8`)
- `0x002D28F6` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x002D2A01` → [IvtIommuSendCommand](../46/IvtIommuSendCommand_function_0046A6E4.md) (function, `0x0046A6E4`)
- `0x002D2C30` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x002D2C64` → [HalpIommuGetNextFlushDevice](../4F/HalpIommuGetNextFlushDevice_function_004FB8E8.md) (function, `0x004FB8E8`)

### Direct callers
- [IvtFlushDomainTb](IvtFlushDomainTb_function_002D1BD0.md) at `0x002D1C29`
- [IvtAttachDeviceDomainInternal](../56/IvtAttachDeviceDomainInternal_function_0056ED90.md) at `0x0056F01A`
- [IvtAttachDeviceDomainInternal](../56/IvtAttachDeviceDomainInternal_function_0056ED90.md) at `0x0056F04B`
- [IvtFlushTb](../56/IvtFlushTb_function_0056F830.md) at `0x0056F8B4`
- [IvtInitializeIommu](../../pagelk/B6/IvtInitializeIommu_function_00B61FE0.md) at `0x00B62129`

### Static image references
- `0x002D256B` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **12**
  - `0x002D2A43` → [sub_006DD832 + 0x1A](../6D/Unknown_function_006DD832.md) (`tail-transfer`)
  - `0x002D2A5A` → [sub_006DD832](../6D/Unknown_function_006DD832.md) (`tail-transfer`)
  - `0x002D2A6A` → [sub_006DD832 + 0x5](../6D/Unknown_function_006DD832.md) (`tail-transfer`)
  - `0x002D2AFE` → [sub_006DD832 + 0x66](../6D/Unknown_function_006DD832.md) (`tail-transfer`)
  - `0x002D2B0B` → [sub_006DD832 + 0x69](../6D/Unknown_function_006DD832.md) (`tail-transfer`)
  - `0x002D2B1B` → [sub_006DD832 + 0x7A](../6D/Unknown_function_006DD832.md) (`tail-transfer`)
  - `0x002D2B46` → [sub_006DD832 + 0xC1](../6D/Unknown_function_006DD832.md) (`tail-transfer`)
  - `0x002D2B6E` → [sub_006DD832 + 0xA2](../6D/Unknown_function_006DD832.md) (`tail-transfer`)
  - `0x002D2B8C` → [sub_006DD832 + 0xA2](../6D/Unknown_function_006DD832.md) (`tail-transfer`)
  - `0x002D2BE4` → [sub_006DD832 + 0x152](../6D/Unknown_function_006DD832.md) (`tail-transfer`)
  - `0x002D2C01` → [sub_006DD832 + 0xCF](../6D/Unknown_function_006DD832.md) (`tail-transfer`)
  - `0x002D2C1F` → [sub_006DD832 + 0xCF](../6D/Unknown_function_006DD832.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002D2548  48 8B C4                        mov rax, rsp
002D254B  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
002D254F  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
002D2553  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
002D2557  55                              push rbp
002D2558  41 54                           push r12
002D255A  41 55                           push r13
002D255C  41 56                           push r14
002D255E  41 57                           push r15
002D2560  48 8D 68 C9                     lea rbp, [rax - 0x37]
002D2564  48 81 EC D0 00 00 00            sub rsp, 0xd0
002D256B  48 8B 05 CE 81 B3 00            mov rax, qword ptr [rip + 0xb381ce]
002D2572  48 33 C4                        xor rax, rsp
002D2575  48 89 45 07                     mov qword ptr [rbp + 7], rax
002D2579  4C 8B 55 67                     mov r10, qword ptr [rbp + 0x67]
002D257D  45 8B D8                        mov r11d, r8d
002D2580  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
002D2584  0F 57 C0                        xorps xmm0, xmm0
002D2587  4C 8B 65 6F                     mov r12, qword ptr [rbp + 0x6f]
002D258B  41 BF 00 00 01 00               mov r15d, 0x10000
002D2591  44 89 45 CF                     mov dword ptr [rbp - 0x31], r8d
002D2595  48 8B F1                        mov rsi, rcx
002D2598  45 33 C0                        xor r8d, r8d
002D259B  48 89 4D AF                     mov qword ptr [rbp - 0x51], rcx
002D259F  4C 89 55 DF                     mov qword ptr [rbp - 0x21], r10
002D25A3  41 8B CF                        mov ecx, r15d
002D25A6  48 89 55 D7                     mov qword ptr [rbp - 0x29], rdx
002D25AA  4C 89 45 9F                     mov qword ptr [rbp - 0x61], r8
002D25AE  4C 89 45 A7                     mov qword ptr [rbp - 0x59], r8
002D25B2  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
002D25B6  4D 85 C9                        test r9, r9
002D25B9  74 04                           je 0x1402d25bf
002D25BB  41 8B 49 30                     mov ecx, dword ptr [r9 + 0x30]
002D25BF  44 8A 75 5F                     mov r14b, byte ptr [rbp + 0x5f]
002D25C3  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
002D25C7  45 84 F6                        test r14b, r14b
002D25CA  0F 84 6F 04 00 00               je 0x1402d2a3f
002D25D0  49 3B CF                        cmp rcx, r15
002D25D3  0F 84 43 03 00 00               je 0x1402d291c
002D25D9  44 39 45 77                     cmp dword ptr [rbp + 0x77], r8d
002D25DD  0F 84 8C 04 00 00               je 0x1402d2a6f
002D25E3  48 0F BA A6 D8 00 00 00 27      bt qword ptr [rsi + 0xd8], 0x27
002D25EC  0F 83 7D 04 00 00               jae 0x1402d2a6f
002D25F2  40 B7 01                        mov dil, 1
002D25F5  B8 32 00 00 00                  mov eax, 0x32
002D25FA  48 C1 E1 10                     shl rcx, 0x10
002D25FE  48 8B D9                        mov rbx, rcx
002D2601  40 88 7C 24 40                  mov byte ptr [rsp + 0x40], dil
002D2606  48 33 D8                        xor rbx, rax
002D2609  48 BA FF FF 00 00 FF FF FF FF   movabs rdx, 0xffffffff0000ffff
002D2613  48 23 DA                        and rbx, rdx
002D2616  48 33 D9                        xor rbx, rcx
002D2619  48 8B 55 D7                     mov rdx, qword ptr [rbp - 0x29]
002D261D  48 81 CB C0 00 00 00            or rbx, 0xc0
002D2624  F6 86 E0 00 00 00 04            test byte ptr [rsi + 0xe0], 4
002D262B  48 89 5D BF                     mov qword ptr [rbp - 0x41], rbx
002D262F  48 89 5D F7                     mov qword ptr [rbp - 9], rbx
002D2633  0F 85 43 04 00 00               jne 0x1402d2a7c
002D2639  4D 85 E4                        test r12, r12
002D263C  0F 84 BE 02 00 00               je 0x1402d2900
002D2642  41 B7 01                        mov r15b, 1
002D2645  44 88 7D 81                     mov byte ptr [rbp - 0x7f], r15b
002D2649  44 39 45 77                     cmp dword ptr [rbp + 0x77], r8d
002D264D  0F 84 B4 02 00 00               je 0x1402d2907
002D2653  41 8A C7                        mov al, r15b
002D2656  88 45 82                        mov byte ptr [rbp - 0x7e], al
002D2659  45 8B C8                        mov r9d, r8d
002D265C  44 88 45 83                     mov byte ptr [rbp - 0x7d], r8b
002D2660  4C 89 45 B7                     mov qword ptr [rbp - 0x49], r8
002D2664  44 89 45 87                     mov dword ptr [rbp - 0x79], r8d
002D2668  44 89 45 8F                     mov dword ptr [rbp - 0x71], r8d
002D266C  40 84 FF                        test dil, dil
002D266F  0F 84 BD 03 00 00               je 0x1402d2a32
002D2675  41 8B C1                        mov eax, r9d
002D2678  48 8B 14 C2                     mov rdx, qword ptr [rdx + rax*8]
002D267C  48 8B C2                        mov rax, rdx
002D267F  4C 8B C2                        mov r8, rdx
002D2682  48 C1 E8 0A                     shr rax, 0xa
002D2686  83 E0 03                        and eax, 3
002D2689  49 C1 E8 0C                     shr r8, 0xc
002D268D  4C 89 45 B7                     mov qword ptr [rbp - 0x49], r8
002D2691  8D 0C C0                        lea ecx, [rax + rax*8]
002D2694  89 4D 87                        mov dword ptr [rbp - 0x79], ecx
002D2697  81 E2 FF 03 00 00               and edx, 0x3ff
002D269D  0F 85 F1 03 00 00               jne 0x1402d2a94
002D26A3  40 84 FF                        test dil, dil
002D26A6  0F 84 82 02 00 00               je 0x1402d292e
002D26AC  45 84 F6                        test r14b, r14b
002D26AF  74 12                           je 0x1402d26c3
002D26B1  0F B7 86 DE 00 00 00            movzx eax, word ptr [rsi + 0xde]
002D26B8  83 E0 3F                        and eax, 0x3f
002D26BB  3B C8                           cmp ecx, eax
002D26BD  0F 87 06 04 00 00               ja 0x1402d2ac9
002D26C3  48 8B 45 FF                     mov rax, qword ptr [rbp - 1]
002D26C7  83 E1 3F                        and ecx, 0x3f
002D26CA  25 C0 0F 00 00                  and eax, 0xfc0
002D26CF  48 0B C8                        or rcx, rax
002D26D2  49 8B C0                        mov rax, r8
002D26D5  48 C1 E0 0C                     shl rax, 0xc
002D26D9  48 0B C8                        or rcx, rax
002D26DC  48 89 4D FF                     mov qword ptr [rbp - 1], rcx
002D26E0  45 33 C0                        xor r8d, r8d
002D26E3  48 8D 55 F7                     lea rdx, [rbp - 9]
002D26E7  48 8B CE                        mov rcx, rsi
002D26EA  E8 F5 7F 19 00                  call 0x14046a6e4
002D26EF  48 8B 5D F7                     mov rbx, qword ptr [rbp - 9]
002D26F3  45 33 C0                        xor r8d, r8d
002D26F6  4C 8B 55 DF                     mov r10, qword ptr [rbp - 0x21]
002D26FA  44 8B 4D 8F                     mov r9d, dword ptr [rbp - 0x71]
002D26FE  48 89 5D BF                     mov qword ptr [rbp - 0x41], rbx
002D2702  45 84 FF                        test r15b, r15b
002D2705  0F 84 A0 00 00 00               je 0x1402d27ab
002D270B  4C 89 65 97                     mov qword ptr [rbp - 0x69], r12
002D270F  4D 8B EC                        mov r13, r12
002D2712  4D 85 D2                        test r10, r10
002D2715  0F 85 C4 03 00 00               jne 0x1402d2adf
002D271B  49 8B 0C 24                     mov rcx, qword ptr [r12]
002D271F  45 84 F6                        test r14b, r14b
002D2722  0F 84 E6 02 00 00               je 0x1402d2a0e
002D2728  48 89 4D 97                     mov qword ptr [rbp - 0x69], rcx
002D272C  4C 8B E9                        mov r13, rcx
002D272F  44 88 45 80                     mov byte ptr [rbp - 0x80], r8b
002D2733  41 8A F8                        mov dil, r8b
002D2736  49 3B CC                        cmp rcx, r12
002D2739  0F 84 EA 03 00 00               je 0x1402d2b29
002D273F  48 8B 41 D8                     mov rax, qword ptr [rcx - 0x28]
002D2743  4C 8D 71 2C                     lea r14, [rcx + 0x2c]
002D2747  B2 01                           mov dl, 1
002D2749  48 8B 70 30                     mov rsi, qword ptr [rax + 0x30]
002D274D  48 8D 48 40                     lea rcx, [rax + 0x40]
002D2751  44 8B 78 3C                     mov r15d, dword ptr [rax + 0x3c]
002D2755  44 89 7D 8B                     mov dword ptr [rbp - 0x75], r15d
002D2759  48 89 75 C7                     mov qword ptr [rbp - 0x39], rsi
002D275D  48 89 4D 9F                     mov qword ptr [rbp - 0x61], rcx
002D2761  4C 89 75 A7                     mov qword ptr [rbp - 0x59], r14
002D2765  84 D2                           test dl, dl
002D2767  0F 84 A2 01 00 00               je 0x1402d290f
002D276D  44 8B 4D 87                     mov r9d, dword ptr [rbp - 0x79]
002D2771  41 8D 59 FF                     lea ebx, [r9 - 1]
002D2775  45 38 06                        cmp byte ptr [r14], r8b
002D2778  0F 85 C1 01 00 00               jne 0x1402d293f
002D277E  E8 9D 3E F4 FF                  call 0x140216620
002D2783  45 33 C0                        xor r8d, r8d
002D2786  84 C0                           test al, al
002D2788  0F 85 A8 03 00 00               jne 0x1402d2b36
002D278E  44 8A 75 5F                     mov r14b, byte ptr [rbp + 0x5f]
002D2792  48 8B 75 AF                     mov rsi, qword ptr [rbp - 0x51]
002D2796  4D 85 E4                        test r12, r12
002D2799  0F 85 99 00 00 00               jne 0x1402d2838
002D279F  48 8B 5D BF                     mov rbx, qword ptr [rbp - 0x41]
002D27A3  44 8B 4D 8F                     mov r9d, dword ptr [rbp - 0x71]
002D27A7  44 8A 7D 81                     mov r15b, byte ptr [rbp - 0x7f]
002D27AB  40 8A 7C 24 40                  mov dil, byte ptr [rsp + 0x40]
002D27B0  41 FF C1                        inc r9d
002D27B3  4C 8B 55 DF                     mov r10, qword ptr [rbp - 0x21]
002D27B7  8A 45 82                        mov al, byte ptr [rbp - 0x7e]
002D27BA  48 8B 55 D7                     mov rdx, qword ptr [rbp - 0x29]
002D27BE  44 89 4D 8F                     mov dword ptr [rbp - 0x71], r9d
002D27C2  44 3B 4D 77                     cmp r9d, dword ptr [rbp + 0x77]
002D27C6  0F 82 A0 FE FF FF               jb 0x1402d266c
002D27CC  45 33 C0                        xor r8d, r8d
002D27CF  33 D2                           xor edx, edx
002D27D1  48 8B CE                        mov rcx, rsi
002D27D4  E8 BB 7D 19 00                  call 0x14046a594
002D27D9  33 FF                           xor edi, edi
002D27DB  40 38 7D 83                     cmp byte ptr [rbp - 0x7d], dil
002D27DF  0F 85 3F 04 00 00               jne 0x1402d2c24
002D27E5  4D 85 E4                        test r12, r12
002D27E8  74 20                           je 0x1402d280a
002D27EA  49 8B DC                        mov rbx, r12
002D27ED  48 89 5D 97                     mov qword ptr [rbp - 0x69], rbx
002D27F1  45 84 F6                        test r14b, r14b
002D27F4  0F 84 40 04 00 00               je 0x1402d2c3a
002D27FA  48 8B 1B                        mov rbx, qword ptr [rbx]
002D27FD  48 89 5D 97                     mov qword ptr [rbp - 0x69], rbx
002D2801  49 3B DC                        cmp rbx, r12
002D2804  0F 85 CC 00 00 00               jne 0x1402d28d6
002D280A  48 8B 4D 07                     mov rcx, qword ptr [rbp + 7]
002D280E  48 33 CC                        xor rcx, rsp
002D2811  E8 2A 9E 3D 00                  call 0x1406ac640
002D2816  4C 8D 9C 24 D0 00 00 00         lea r11, [rsp + 0xd0]
002D281E  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
002D2822  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
002D2826  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
002D282A  49 8B E3                        mov rsp, r11
002D282D  41 5F                           pop r15
002D282F  41 5E                           pop r14
002D2831  41 5D                           pop r13
002D2833  41 5C                           pop r12
002D2835  5D                              pop rbp
002D2836  C3                              ret
002D2837  CC                              int3
002D2838  45 84 F6                        test r14b, r14b
002D283B  74 3E                           je 0x1402d287b
002D283D  4D 8B 6D 00                     mov r13, qword ptr [r13]
002D2841  4C 89 6D 97                     mov qword ptr [rbp - 0x69], r13
002D2845  4D 3B EC                        cmp r13, r12
002D2848  0F 84 51 FF FF FF               je 0x1402d279f
002D284E  49 8B 45 D8                     mov rax, qword ptr [r13 - 0x28]
002D2852  4D 8D 75 2C                     lea r14, [r13 + 0x2c]
002D2856  41 8A F8                        mov dil, r8b
002D2859  44 88 45 80                     mov byte ptr [rbp - 0x80], r8b
002D285D  4C 89 75 A7                     mov qword ptr [rbp - 0x59], r14
002D2861  48 8B 70 30                     mov rsi, qword ptr [rax + 0x30]
002D2865  48 8D 48 40                     lea rcx, [rax + 0x40]
002D2869  44 8B 78 3C                     mov r15d, dword ptr [rax + 0x3c]
002D286D  48 89 75 C7                     mov qword ptr [rbp - 0x39], rsi
002D2871  48 89 4D 9F                     mov qword ptr [rbp - 0x61], rcx
002D2875  44 89 7D 8B                     mov dword ptr [rbp - 0x75], r15d
002D2879  EB 52                           jmp 0x1402d28cd
002D287B  48 8D 45 A7                     lea rax, [rbp - 0x59]
002D287F  49 8B CC                        mov rcx, r12
002D2882  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002D2887  4C 8D 4D 8B                     lea r9, [rbp - 0x75]
002D288B  48 8D 45 9F                     lea rax, [rbp - 0x61]
002D288F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002D2894  4C 8D 45 C7                     lea r8, [rbp - 0x39]
002D2898  48 8D 45 80                     lea rax, [rbp - 0x80]
002D289C  48 8D 55 97                     lea rdx, [rbp - 0x69]
002D28A0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002D28A5  E8 3E 90 22 00                  call 0x1404fb8e8
002D28AA  45 33 C0                        xor r8d, r8d
002D28AD  84 C0                           test al, al
002D28AF  0F 84 EA FE FF FF               je 0x1402d279f
002D28B5  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
002D28B9  4C 8B 75 A7                     mov r14, qword ptr [rbp - 0x59]
002D28BD  40 8A 7D 80                     mov dil, byte ptr [rbp - 0x80]
002D28C1  44 8B 7D 8B                     mov r15d, dword ptr [rbp - 0x75]
002D28C5  4C 8B 6D 97                     mov r13, qword ptr [rbp - 0x69]
002D28C9  48 8B 75 C7                     mov rsi, qword ptr [rbp - 0x39]
002D28CD  44 8B 4D 87                     mov r9d, dword ptr [rbp - 0x79]
002D28D1  E9 9F FE FF FF                  jmp 0x1402d2775
002D28D6  48 8B 4B D8                     mov rcx, qword ptr [rbx - 0x28]
002D28DA  48 8D 43 2C                     lea rax, [rbx + 0x2c]
002D28DE  48 83 C1 40                     add rcx, 0x40
002D28E2  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
002D28E6  48 89 4D 9F                     mov qword ptr [rbp - 0x61], rcx
002D28EA  40 38 38                        cmp byte ptr [rax], dil
002D28ED  0F 84 FE FE FF FF               je 0x1402d27f1
002D28F3  40 88 38                        mov byte ptr [rax], dil
002D28F6  E8 85 75 07 00                  call 0x140349e80
002D28FB  E9 F1 FE FF FF                  jmp 0x1402d27f1
002D2900  45 8A F8                        mov r15b, r8b
002D2903  44 88 45 81                     mov byte ptr [rbp - 0x7f], r8b
002D2907  41 8A C0                        mov al, r8b
002D290A  E9 47 FD FF FF                  jmp 0x1402d2656
002D290F  48 8B 75 AF                     mov rsi, qword ptr [rbp - 0x51]
002D2913  44 8A 75 5F                     mov r14b, byte ptr [rbp + 0x5f]
002D2917  E9 8B FE FF FF                  jmp 0x1402d27a7
002D291C  41 8A F8                        mov dil, r8b
002D291F  44 88 44 24 40                  mov byte ptr [rsp + 0x40], r8b
002D2924  BB 12 00 00 00                  mov ebx, 0x12
002D2929  E9 F6 FC FF FF                  jmp 0x1402d2624
002D292E  45 33 C0                        xor r8d, r8d
002D2931  45 85 C9                        test r9d, r9d
002D2934  0F 85 C8 FD FF FF               jne 0x1402d2702
002D293A  E9 A1 FD FF FF                  jmp 0x1402d26e0
002D293F  44 8A 75 5F                     mov r14b, byte ptr [rbp + 0x5f]
002D2943  0F 57 C0                        xorps xmm0, xmm0
002D2946  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
002D294A  45 84 F6                        test r14b, r14b
002D294D  0F 85 96 02 00 00               jne 0x1402d2be9
002D2953  44 8B 5D CF                     mov r11d, dword ptr [rbp - 0x31]
002D2957  41 83 FB FF                     cmp r11d, -1
002D295B  0F 84 E2 01 00 00               je 0x1402d2b43
002D2961  48 8B 55 EF                     mov rdx, qword ptr [rbp - 0x11]
002D2965  41 8B C3                        mov eax, r11d
002D2968  25 FF FF 0F 00                  and eax, 0xfffff
002D296D  48 C1 E0 20                     shl rax, 0x20
002D2971  44 0F B7 C6                     movzx r8d, si
002D2975  48 B9 F8 FF 00 00 FF FF FF FF   movabs rcx, 0xffffffff0000fff8
002D297F  49 C1 E0 10                     shl r8, 0x10
002D2983  48 23 C1                        and rax, rcx
002D2986  4C 0B C0                        or r8, rax
002D2989  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
002D298D  49 83 C8 08                     or r8, 8
002D2991  48 0F BA A0 E0 00 00 00 29      bt qword ptr [rax + 0xe0], 0x29
002D299A  0F 82 F1 01 00 00               jb 0x1402d2b91
002D29A0  41 8B CF                        mov ecx, r15d
002D29A3  48 C1 E1 04                     shl rcx, 4
002D29A7  48 8B C1                        mov rax, rcx
002D29AA  49 33 C0                        xor rax, r8
002D29AD  48 25 0F FE FF FF               and rax, 0xfffffffffffffe0f
002D29B3  48 33 C1                        xor rax, rcx
002D29B6  83 7D 77 00                     cmp dword ptr [rbp + 0x77], 0
002D29BA  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
002D29BE  0F 84 FD 01 00 00               je 0x1402d2bc1
002D29C4  45 85 C9                        test r9d, r9d
002D29C7  0F 84 06 02 00 00               je 0x1402d2bd3
002D29CD  81 E2 FE 0F 00 00               and edx, 0xffe
002D29D3  8B CB                           mov ecx, ebx
002D29D5  B8 01 00 00 00                  mov eax, 1
002D29DA  48 D3 E0                        shl rax, cl
002D29DD  48 FF C8                        dec rax
002D29E0  48 0B 45 B7                     or rax, qword ptr [rbp - 0x49]
002D29E4  48 C1 E0 0C                     shl rax, 0xc
002D29E8  48 0B C2                        or rax, rdx
002D29EB  48 83 C8 01                     or rax, 1
002D29EF  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
002D29F3  48 8B 75 AF                     mov rsi, qword ptr [rbp - 0x51]
002D29F7  48 8D 55 E7                     lea rdx, [rbp - 0x19]
002D29FB  48 8B CE                        mov rcx, rsi
002D29FE  45 33 C0                        xor r8d, r8d
002D2A01  E8 DE 7C 19 00                  call 0x14046a6e4
002D2A06  45 33 C0                        xor r8d, r8d
002D2A09  E9 88 FD FF FF                  jmp 0x1402d2796
002D2A0E  49 3B CC                        cmp rcx, r12
002D2A11  0F 85 F9 00 00 00               jne 0x1402d2b10
002D2A17  41 8A D0                        mov dl, r8b
002D2A1A  4D 8B F0                        mov r14, r8
002D2A1D  49 8B C8                        mov rcx, r8
002D2A20  41 8A F8                        mov dil, r8b
002D2A23  45 8B F8                        mov r15d, r8d
002D2A26  49 8B F0                        mov rsi, r8
002D2A29  40 88 7D 80                     mov byte ptr [rbp - 0x80], dil
002D2A2D  E9 23 FD FF FF                  jmp 0x1402d2755
002D2A32  84 C0                           test al, al
002D2A34  0F 84 F7 FE FF FF               je 0x1402d2931
002D2A3A  E9 36 FC FF FF                  jmp 0x1402d2675
002D2A3F  41 83 FB FF                     cmp r11d, -1
002D2A43  0F 85 03 AE 40 00               jne 0x1406dd84c
002D2A49  48 0F BA A6 D8 00 00 00 27      bt qword ptr [rsi + 0xd8], 0x27
002D2A52  44 88 44 24 40                  mov byte ptr [rsp + 0x40], r8b
002D2A57  41 8A F8                        mov dil, r8b
002D2A5A  0F 83 D2 AD 40 00               jae 0x1406dd832
002D2A60  48 83 4D FF 40                  or qword ptr [rbp - 1], 0x40
002D2A65  BB 32 00 00 00                  mov ebx, 0x32
002D2A6A  E9 C8 AD 40 00                  jmp 0x1406dd837
002D2A6F  41 8A F8                        mov dil, r8b
002D2A72  B8 22 00 00 00                  mov eax, 0x22
002D2A77  E9 7E FB FF FF                  jmp 0x1402d25fa
002D2A7C  4D 85 D2                        test r10, r10
002D2A7F  0F 84 B4 FB FF FF               je 0x1402d2639
002D2A85  4D 39 42 60                     cmp qword ptr [r10 + 0x60], r8
002D2A89  0F 85 B3 FB FF FF               jne 0x1402d2642
002D2A8F  E9 A5 FB FF FF                  jmp 0x1402d2639
002D2A94  B8 01 00 00 00                  mov eax, 1
002D2A99  48 D3 E0                        shl rax, cl
002D2A9C  48 0F AF C2                     imul rax, rdx
002D2AA0  49 03 C0                        add rax, r8
002D2AA3  49 33 C0                        xor rax, r8
002D2AA6  48 0F BD C8                     bsr rcx, rax
002D2AAA  B8 01 00 00 00                  mov eax, 1
002D2AAF  FF C1                           inc ecx
002D2AB1  48 D3 E0                        shl rax, cl
002D2AB4  48 FF C8                        dec rax
002D2AB7  89 4D 87                        mov dword ptr [rbp - 0x79], ecx
002D2ABA  48 F7 D0                        not rax
002D2ABD  4C 23 C0                        and r8, rax
002D2AC0  4C 89 45 B7                     mov qword ptr [rbp - 0x49], r8
002D2AC4  E9 DA FB FF FF                  jmp 0x1402d26a3
002D2AC9  48 83 E3 EF                     and rbx, 0xffffffffffffffef
002D2ACD  C6 44 24 40 00                  mov byte ptr [rsp + 0x40], 0
002D2AD2  48 83 CB 20                     or rbx, 0x20
002D2AD6  48 89 5D F7                     mov qword ptr [rbp - 9], rbx
002D2ADA  E9 01 FC FF FF                  jmp 0x1402d26e0
002D2ADF  49 8B 42 60                     mov rax, qword ptr [r10 + 0x60]
002D2AE3  49 8B 72 30                     mov rsi, qword ptr [r10 + 0x30]
002D2AE7  45 8B 7A 3C                     mov r15d, dword ptr [r10 + 0x3c]
002D2AEB  48 89 75 C7                     mov qword ptr [rbp - 0x39], rsi
002D2AEF  8B 78 30                        mov edi, dword ptr [rax + 0x30]
002D2AF2  8B D7                           mov edx, edi
002D2AF4  83 E2 01                        and edx, 1
002D2AF7  44 89 7D 8B                     mov dword ptr [rbp - 0x75], r15d
002D2AFB  45 84 F6                        test r14b, r14b
002D2AFE  0F 85 94 AD 40 00               jne 0x1406dd898
002D2B04  C1 EF 0B                        shr edi, 0xb
002D2B07  40 80 E7 01                     and dil, 1
002D2B0B  E9 8B AD 40 00                  jmp 0x1406dd89b
002D2B10  48 8B 71 28                     mov rsi, qword ptr [rcx + 0x28]
002D2B14  8B 7E 30                        mov edi, dword ptr [rsi + 0x30]
002D2B17  40 F6 C7 01                     test dil, 1
002D2B1B  0F 85 8B AD 40 00               jne 0x1406dd8ac
002D2B21  48 8B 09                        mov rcx, qword ptr [rcx]
002D2B24  E9 E5 FE FF FF                  jmp 0x1402d2a0e
002D2B29  4C 89 45 9F                     mov qword ptr [rbp - 0x61], r8
002D2B2D  4C 89 45 A7                     mov qword ptr [rbp - 0x59], r8
002D2B31  E9 75 FC FF FF                  jmp 0x1402d27ab
002D2B36  44 8B 4D 87                     mov r9d, dword ptr [rbp - 0x79]
002D2B3A  41 C6 06 01                     mov byte ptr [r14], 1
002D2B3E  E9 FC FD FF FF                  jmp 0x1402d293f
002D2B43  40 84 FF                        test dil, dil
002D2B46  0F 85 A7 AD 40 00               jne 0x1406dd8f3
002D2B4C  44 39 45 8F                     cmp dword ptr [rbp - 0x71], r8d
002D2B50  0F 85 3C FC FF FF               jne 0x1402d2792
002D2B56  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
002D2B5A  0F B7 D6                        movzx edx, si
002D2B5D  48 C1 E2 20                     shl rdx, 0x20
002D2B61  48 83 CA 03                     or rdx, 3
002D2B65  48 0F BA A0 E0 00 00 00 29      bt qword ptr [rax + 0xe0], 0x29
002D2B6E  0F 83 60 AD 40 00               jae 0x1406dd8d4
002D2B74  48 8B C6                        mov rax, rsi
002D2B77  83 E6 0F                        and esi, 0xf
002D2B7A  48 83 E0 F0                     and rax, 0xfffffffffffffff0
002D2B7E  48 C1 E0 24                     shl rax, 0x24
002D2B82  48 0B C6                        or rax, rsi
002D2B85  48 C1 E0 0C                     shl rax, 0xc
002D2B89  48 0B D0                        or rdx, rax
002D2B8C  E9 43 AD 40 00                  jmp 0x1406dd8d4
002D2B91  49 8B C0                        mov rax, r8
002D2B94  48 8B CE                        mov rcx, rsi
002D2B97  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
002D2B9B  83 E6 0F                        and esi, 0xf
002D2B9E  48 C1 E1 24                     shl rcx, 0x24
002D2BA2  49 B8 FF 0F FF FF FF FF 0F 00   movabs r8, 0xfffffffff0fff
002D2BAC  48 0B CE                        or rcx, rsi
002D2BAF  49 23 C0                        and rax, r8
002D2BB2  48 C1 E1 0C                     shl rcx, 0xc
002D2BB6  4C 8B C1                        mov r8, rcx
002D2BB9  4C 0B C0                        or r8, rax
002D2BBC  E9 DF FD FF FF                  jmp 0x1402d29a0
002D2BC1  81 E2 FF 07 00 00               and edx, 0x7ff
002D2BC7  48 B8 00 F8 FF FF FF FF FF 7F   movabs rax, 0x7ffffffffffff800
002D2BD1  EB 0E                           jmp 0x1402d2be1
002D2BD3  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
002D2BD7  81 E2 FF 0F 00 00               and edx, 0xfff
002D2BDD  48 C1 E0 0C                     shl rax, 0xc
002D2BE1  48 0B D0                        or rdx, rax
002D2BE4  E9 9B AD 40 00                  jmp 0x1406dd984
002D2BE9  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
002D2BED  0F B7 D6                        movzx edx, si
002D2BF0  48 C1 E2 20                     shl rdx, 0x20
002D2BF4  48 83 CA 03                     or rdx, 3
002D2BF8  48 0F BA A0 E0 00 00 00 29      bt qword ptr [rax + 0xe0], 0x29
002D2C01  0F 83 FA AC 40 00               jae 0x1406dd901
002D2C07  48 8B C6                        mov rax, rsi
002D2C0A  83 E6 0F                        and esi, 0xf
002D2C0D  48 83 E0 F0                     and rax, 0xfffffffffffffff0
002D2C11  48 C1 E0 24                     shl rax, 0x24
002D2C15  48 0B C6                        or rax, rsi
002D2C18  48 C1 E0 0C                     shl rax, 0xc
002D2C1C  48 0B D0                        or rdx, rax
002D2C1F  E9 DD AC 40 00                  jmp 0x1406dd901
002D2C24  48 8B 4D DF                     mov rcx, qword ptr [rbp - 0x21]
002D2C28  48 83 C1 40                     add rcx, 0x40
002D2C2C  48 89 4D 9F                     mov qword ptr [rbp - 0x61], rcx
002D2C30  E8 4B 72 07 00                  call 0x140349e80
002D2C35  E9 AB FB FF FF                  jmp 0x1402d27e5
002D2C3A  48 8D 45 A7                     lea rax, [rbp - 0x59]
002D2C3E  49 8B CC                        mov rcx, r12
002D2C41  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002D2C46  4C 8D 4D 8B                     lea r9, [rbp - 0x75]
002D2C4A  48 8D 45 9F                     lea rax, [rbp - 0x61]
002D2C4E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002D2C53  4C 8D 45 C7                     lea r8, [rbp - 0x39]
002D2C57  48 8D 45 80                     lea rax, [rbp - 0x80]
002D2C5B  48 8D 55 97                     lea rdx, [rbp - 0x69]
002D2C5F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002D2C64  E8 7F 8C 22 00                  call 0x1404fb8e8
002D2C69  84 C0                           test al, al
002D2C6B  0F 84 99 FB FF FF               je 0x1402d280a
002D2C71  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
002D2C75  48 8B 45 A7                     mov rax, qword ptr [rbp - 0x59]
002D2C79  48 8B 5D 97                     mov rbx, qword ptr [rbp - 0x69]
002D2C7D  E9 68 FC FF FF                  jmp 0x1402d28ea
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IvtFlushTbInternal(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int8 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int8 v_stack_mB8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (208);
    result = (*(unsigned __int64 *)(v_rip + 11764174)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 55 + 7) = result;
    *(unsigned int *)(v_rsp - 55 - 49) = a3;
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 55 - 81) = a1;
    *(unsigned __int64 *)(v_rsp - 55 - 33) = *(unsigned __int64 *)(v_rsp - 55 + 103);
    *(unsigned __int64 *)(v_rsp - 55 - 41) = *(unsigned __int64 *)(v_rsp - 55 + 127);
    *(unsigned __int64 *)(v_rsp - 55 - 97) = 0;
    *(unsigned __int64 *)(v_rsp - 55 - 89) = 0;
    *(unsigned __int64 *)(v_rsp - 55 - 25) = v_xmm0;
    if (a4 != 0) {
        a1 = *(unsigned int *)(a4 + 48);
    }
    *(unsigned __int64 *)(v_rsp - 55 - 9) = v_xmm0;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 55 + 95)) == 0) goto loc_002D2A3F;
    if (a1 == ((unsigned int)(0x10000ULL))) goto loc_002D291C;
    if ((*(unsigned int *)(v_rsp - 55 + 119)) == 0) goto loc_002D2A6F;
    if ((*(unsigned int *)(v_rsp - 55 + 119)) >= 0) goto loc_002D2A6F;
loc_002D25FA:
    a1 = (a1) << (16);
    v_stack_mB8 = 1;
    v_rbx = (a1) ^ (50);
    v_rbx = (v_rbx) & (*(unsigned __int64 *)(v_rsp - 55 + 127));
    v_rbx = (v_rbx) ^ (a1);
    v_rbx = (v_rbx) | (192);
loc_002D2624:
    *(unsigned __int64 *)(v_rsp - 55 - 65) = v_rbx;
    *(unsigned __int64 *)(v_rsp - 55 - 9) = v_rbx;
    if (((*(unsigned __int8 *)(a1 + 224)) & (4)) != 0) goto loc_002D2A7C;
loc_002D2639:
    if (*(unsigned __int64 *)(v_rsp - 55 + 111) == 0) goto loc_002D2900;
loc_002D2642:
    *(unsigned __int8 *)(v_rsp - 55 - 127) = 1;
    if ((*(unsigned int *)(v_rsp - 55 + 119)) == 0) goto loc_002D2907;
loc_002D2656:
    *(unsigned __int8 *)(v_rsp - 55 - 126) = 1;
    *(unsigned __int8 *)(v_rsp - 55 - 125) = 0;
    *(unsigned __int64 *)(v_rsp - 55 - 73) = 0;
    *(unsigned int *)(v_rsp - 55 - 121) = 0;
    *(unsigned int *)(v_rsp - 55 - 113) = 0;
loc_002D266C:
    if (1 == 0) goto loc_002D2A32;
loc_002D2675:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 - 41) + 0 * 8)) >> (10);
    result = (unsigned int)((result) & (3));
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 - 41) + 0 * 8)) >> (12);
    *(unsigned __int64 *)(v_rsp - 55 - 73) = a3;
    *(unsigned int *)(v_rsp - 55 - 121) = (unsigned int)(result + result * 8);
    a2 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 - 41) + 0 * 8)) & (0x3FFULL));
    if (condition_is_not_equal) goto loc_002D2A94;
loc_002D26A3:
    if (1 == 0) goto loc_002D292E;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 55 + 95)) == 0) goto loc_002D26C3;
    result = (unsigned int)((*(unsigned __int16 *)(a1 + 222)) & (63));
    if (((unsigned int)(result + result * 8)) > ((unsigned int)(result))) goto loc_002D2AC9;
loc_002D26C3:
    a1 = (unsigned int)((result + result * 8) & (63));
    result = (unsigned int)((*(unsigned __int64 *)(v_rsp - 55 - 1)) & (0xFC0ULL));
    a1 = (a1) | (result);
    result = (a3) << (12);
    a1 = (a1) | (result);
    *(unsigned __int64 *)(v_rsp - 55 - 1) = a1;
loc_002D26E0:
    a3 = 0;
    result = IvtIommuSendCommand(a1, v_rsp - 55 - 9, a3, 0);
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 55 - 65) = *(unsigned __int64 *)(v_rsp - 55 - 9);
loc_002D2702:
    if (1 == 0) goto loc_002D27AB;
    *(unsigned __int64 *)(v_rsp - 55 - 105) = *(unsigned __int64 *)(v_rsp - 55 + 111);
    if (*(unsigned __int64 *)(v_rsp - 55 - 33) != 0) goto loc_002D2ADF;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 55 + 95)) == 0) goto loc_002D2A0E;
    *(unsigned __int64 *)(v_rsp - 55 - 105) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 + 111));
    *(unsigned __int8 *)(v_rsp - 55 - 128) = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 + 111))) == (*(unsigned __int64 *)(v_rsp - 55 + 111))) goto loc_002D2B29;
loc_002D2755:
    *(unsigned int *)(v_rsp - 55 - 117) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 + 111)) - 40) + 60)));
    *(unsigned __int64 *)(v_rsp - 55 - 57) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 + 111)) - 40) + 48);
    *(unsigned __int64 *)(v_rsp - 55 - 97) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 + 111)) - 40) + 64;
    *(unsigned __int64 *)(v_rsp - 55 - 89) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 + 111)) + 44;
    if (1 == 0) goto loc_002D290F;
loc_002D2775:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 + 111)) + 44)) != 0) goto loc_002D293F;
    result = ExAcquireRundownProtection(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 + 111)) - 40) + 64, 1, a3, (unsigned int)(*(unsigned int *)(v_rsp - 55 - 121)));
    a3 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_002D2B36;
loc_002D2792:
loc_002D2796:
    if (*(unsigned __int64 *)(v_rsp - 55 + 111) != 0) goto loc_002D2838;
loc_002D279F:
loc_002D27A7:
loc_002D27AB:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 55 - 113))) + 1);
    *(unsigned int *)(v_rsp - 55 - 113) = (unsigned int)(a4);
    if (((unsigned int)(a4)) < (*(unsigned int *)(v_rsp - 55 + 119))) goto loc_002D266C;
    a3 = 0;
    a2 = 0;
    result = IvtIommuWaitCommand(*(unsigned __int64 *)(v_rsp - 55 - 81), a2, a3, a4);
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rsp - 55 - 125)) != 0) goto loc_002D2C24;
loc_002D27E5:
    if (*(unsigned __int64 *)(v_rsp - 55 + 111) == 0) goto loc_002D280A;
    *(unsigned __int64 *)(v_rsp - 55 - 105) = *(unsigned __int64 *)(v_rsp - 55 + 111);
loc_002D27F1:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 55 + 95)) == 0) goto loc_002D2C3A;
    *(unsigned __int64 *)(v_rsp - 55 - 105) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 + 111));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 + 111))) != (*(unsigned __int64 *)(v_rsp - 55 + 111))) goto loc_002D28D6;
loc_002D280A:
    a1 = (*(unsigned __int64 *)(v_rsp - 55 + 7)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
loc_002D2838:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 55 + 95)) == 0) goto loc_002D287B;
    *(unsigned __int64 *)(v_rsp - 55 - 105) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 + 111)));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 + 111)))) == (*(unsigned __int64 *)(v_rsp - 55 + 111))) goto loc_002D279F;
    *(unsigned __int8 *)(v_rsp - 55 - 128) = 0;
    *(unsigned __int64 *)(v_rsp - 55 - 89) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 + 111))) + 44;
    *(unsigned __int64 *)(v_rsp - 55 - 57) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 + 111))) - 40) + 48);
    *(unsigned __int64 *)(v_rsp - 55 - 97) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 + 111))) - 40) + 64;
    *(unsigned int *)(v_rsp - 55 - 117) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 + 111))) - 40) + 60)));
    goto loc_002D28CD;
loc_002D287B:
    v_stack_mA0 = v_rsp - 55 - 89;
    v_stack_mA8 = v_rsp - 55 - 97;
    v_stack_mB0 = v_rsp - 55 - 128;
    result = HalpIommuGetNextFlushDevice(*(unsigned __int64 *)(v_rsp - 55 + 111), v_rsp - 55 - 105, v_rsp - 55 - 57, v_rsp - 55 - 117);
    a3 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_002D279F;
loc_002D28CD:
    goto loc_002D2775;
loc_002D28D6:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) - 40)) + (64);
    *(unsigned __int64 *)(v_rsp - 55 - 89) = *(unsigned __int64 *)(v_stack_m28 + 56) + 44;
    *(unsigned __int64 *)(v_rsp - 55 - 97) = a1;
loc_002D28EA:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 44)) == ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 55 - 128)))) goto loc_002D27F1;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 44) = (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 55 - 128));
    result = ExReleaseRundownProtection(a1, v_rsp - 55 - 105, a3, (unsigned int)(*(unsigned int *)(v_rsp - 55 - 121)));
    goto loc_002D27F1;
loc_002D2900:
    *(unsigned __int8 *)(v_rsp - 55 - 127) = 0;
loc_002D2907:
    goto loc_002D2656;
loc_002D290F:
    goto loc_002D27A7;
loc_002D291C:
    v_stack_m90 = 0;
    goto loc_002D2624;
loc_002D292E:
    a3 = 0;
loc_002D2931:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 55 - 121))) != 0) goto loc_002D2702;
    goto loc_002D26E0;
loc_002D293F:
    *(unsigned __int64 *)(v_rsp - 55 - 25) = v_xmm0;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 55 + 95)) != 0) goto loc_002D2BE9;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 55 - 49)))) == -1) goto loc_002D2B43;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 55 - 49))))) & (0xFFFFFULL));
    result = (result) << (32);
    a3 = ((unsigned __int16)(*(unsigned __int64 *)(v_rsp - 55 - 81))) << (16);
    result = (result) & (a1);
    a3 = (a3) | (result);
    a3 = (a3) | (8);
    if (condition_is_below) goto loc_002D2B91;
loc_002D29A0:
    a1 = (0) << (4);
    result = (a1) ^ (a3);
    result = (result) & (-497);
    result = (result) ^ (a1);
    *(unsigned __int64 *)(v_rsp - 55 - 25) = result;
    if ((*(unsigned int *)(v_rsp - 55 + 119)) == 0) goto loc_002D2BC1;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 55 - 121))) == 0) goto loc_002D2BD3;
    a2 = (unsigned int)((*(unsigned __int64 *)(v_rsp - 55 - 17)) & (0xFFEULL));
    result = (1) << (18);
    result = (result) - 1;
    result = (result) | (*(unsigned __int64 *)(v_rsp - 55 - 73));
    result = (result) << (12);
    result = (result) | (a2);
    result = (result) | (1);
    *(unsigned __int64 *)(v_rsp - 55 - 17) = result;
    a3 = 0;
    result = IvtIommuSendCommand(*(unsigned __int64 *)(v_rsp - 55 - 81), v_rsp - 55 - 25, a3, (unsigned int)(*(unsigned int *)(v_rsp - 55 - 121)));
    a3 = 0;
    goto loc_002D2796;
loc_002D2A0E:
    if ((*(unsigned __int64 *)(v_rsp - 55 - 81)) != (*(unsigned __int64 *)(v_rsp - 55 + 111))) goto loc_002D2B10;
    *(unsigned __int8 *)(v_rsp - 55 - 128) = 0;
    goto loc_002D2755;
loc_002D2A32:
    if ((unsigned __int8)(result) == 0) goto loc_002D2931;
    goto loc_002D2675;
loc_002D2A3F:
    v_stack_m90 = 0;
loc_002D2A6F:
    goto loc_002D25FA;
loc_002D2A7C:
    if (*(unsigned __int64 *)(v_rsp - 55 - 33) == 0) goto loc_002D2639;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 - 33) + 96)) != 0) goto loc_002D2642;
    goto loc_002D2639;
loc_002D2A94:
    result = (1) << (0);
    result = (result) * (0);
    result = (result) + (0);
    result = (result) ^ (0);
    a1 = (unsigned int)((0) + 1);
    result = (1) << ((unsigned __int8)(a1));
    result = (result) - 1;
    *(unsigned int *)(v_rsp - 55 - 121) = (unsigned int)(a1);
    result = ~(result);
    a3 = (a3) & (result);
    *(unsigned __int64 *)(v_rsp - 55 - 73) = a3;
    goto loc_002D26A3;
loc_002D2AC9:
    v_rbx = (50) & (-17);
    v_stack_m90 = 0;
    v_rbx = (v_rbx) | (32);
    *(unsigned __int64 *)(v_rsp - 55 - 9) = v_rbx;
    goto loc_002D26E0;
loc_002D2ADF:
    *(unsigned __int64 *)(v_rsp - 55 - 57) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 - 33) + 48);
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 - 33) + 96) + 48))))) & (1));
    *(unsigned int *)(v_rsp - 55 - 117) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 55 - 33) + 60)));
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 55 - 33) + 96) + 48))) >> (11));
    v_rdi = (unsigned __int8)((v_rdi) & (1));
loc_002D2B10:
    goto loc_002D2A0E;
loc_002D2B29:
    *(unsigned __int64 *)(v_rsp - 55 - 97) = a3;
    *(unsigned __int64 *)(v_rsp - 55 - 89) = a3;
    goto loc_002D27AB;
loc_002D2B36:
    *(unsigned __int8 *)(0) = 1;
    goto loc_002D293F;
loc_002D2B43:
    if ((*(unsigned int *)(v_rsp - 55 - 113)) != a3) goto loc_002D2792;
    a2 = ((unsigned __int16)(*(unsigned __int64 *)(a1 + 40))) << (32);
    a2 = (a2) | (3);
    v_rsi = (unsigned int)((*(unsigned __int64 *)(a1 + 40)) & (15));
    result = (*(unsigned __int64 *)(a1 + 40)) & (-16);
    result = (result) << (36);
    result = (result) | (v_rsi);
    result = (result) << (12);
    a2 = (a2) | (result);
loc_002D2B91:
    a1 = (v_rsi) & (-16);
    v_rsi = (unsigned int)((v_rsi) & (15));
    a1 = (a1) << (36);
    a1 = (a1) | (v_rsi);
    result = (a3) & (a3);
    a1 = (a1) << (12);
    a3 = (a1) | (result);
    goto loc_002D29A0;
loc_002D2BC1:
    a2 = (unsigned int)((a2) & (0x7FFULL));
    goto loc_002D2BE1;
loc_002D2BD3:
    a2 = (unsigned int)((a2) & (0xFFFULL));
    result = (*(unsigned __int64 *)(v_rsp - 55 - 73)) << (12);
loc_002D2BE1:
    a2 = (a2) | (result);
loc_002D2BE9:
    a2 = ((unsigned __int16)(v_rsi)) << (32);
    a2 = (a2) | (3);
    v_rsi = (unsigned int)((v_rsi) & (15));
    result = (v_rsi) & (-16);
    result = (result) << (36);
    result = (result) | (v_rsi);
    result = (result) << (12);
    a2 = (a2) | (result);
loc_002D2C24:
    a1 = (*(unsigned __int64 *)(v_rsp - 55 - 33)) + (64);
    *(unsigned __int64 *)(v_rsp - 55 - 97) = a1;
    result = ExReleaseRundownProtection(a1, a2, a3, (unsigned int)(*(unsigned int *)(v_rsp - 55 - 121)));
    goto loc_002D27E5;
loc_002D2C3A:
    v_stack_mA0 = v_rsp - 55 - 89;
    v_stack_mA8 = v_rsp - 55 - 97;
    v_stack_mB0 = v_rsp - 55 - 128;
    result = HalpIommuGetNextFlushDevice(*(unsigned __int64 *)(v_rsp - 55 + 111), v_rsp - 55 - 105, v_rsp - 55 - 57, v_rsp - 55 - 117);
    if ((unsigned __int8)(result) == 0) goto loc_002D280A;
    goto loc_002D28EA;
}
```

## 5. (Beta) C Style

```c
int64_t IvtFlushTbInternal(void *Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint8_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint8_t v_stack_mB8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (208);
    result = (*(uint64_t *)(v_rip + 0xB381CE)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x37 + 0x7) = result;
    *(uint32_t *)(local_rsp - 0x37 - 0x31) = Arg3;
    Arg3 = 0;
    *(void **)(local_rsp - 0x37 - 0x51) = Arg1;
    *(uint64_t *)(local_rsp - 0x37 - 0x21) = *(uint64_t *)(local_rsp - 0x37 + 0x67);
    *(uint64_t *)(local_rsp - 0x37 - 0x29) = *(uint64_t *)(local_rsp - 0x37 + 0x7F);
    *(uint64_t *)(local_rsp - 0x37 - 0x61) = 0;
    *(uint64_t *)(local_rsp - 0x37 - 0x59) = 0;
    *(uint64_t *)(local_rsp - 0x37 - 0x19) = v_xmm0;
    if (Arg4 != 0) {
        Arg1 = *(uint32_t *)(Arg4 + 0x30);
    }
    *(uint64_t *)(local_rsp - 0x37 - 0x9) = v_xmm0;
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x37 + 0x5F)) == 0) goto loc_002D2A3F;
    if (Arg1 == ((uint32_t)(0x10000ULL))) goto loc_002D291C;
    if ((*(uint32_t *)(local_rsp - 0x37 + 0x77)) == 0) goto loc_002D2A6F;
    if ((*(uint32_t *)(local_rsp - 0x37 + 0x77)) >= 0) goto loc_002D2A6F;
loc_002D25FA:
    Arg1 = (Arg1) << (16);
    v_stack_mB8 = 1;
    local_rbx = (Arg1) ^ (50);
    local_rbx = (local_rbx) & (*(uint64_t *)(local_rsp - 0x37 + 0x7F));
    local_rbx = (local_rbx) ^ (Arg1);
    local_rbx = (local_rbx) | (192);
loc_002D2624:
    *(uint64_t *)(local_rsp - 0x37 - 0x41) = local_rbx;
    *(uint64_t *)(local_rsp - 0x37 - 0x9) = local_rbx;
    if (((*(uint8_t *)(arg1 + 0xE0)) & (4)) != 0) goto loc_002D2A7C;
loc_002D2639:
    if (*(uint64_t *)(local_rsp - 0x37 + 0x6F) == 0) goto loc_002D2900;
loc_002D2642:
    *(uint8_t *)(local_rsp - 0x37 - 0x7F) = 1;
    if ((*(uint32_t *)(local_rsp - 0x37 + 0x77)) == 0) goto loc_002D2907;
loc_002D2656:
    *(uint8_t *)(local_rsp - 0x37 - 0x7E) = 1;
    *(uint8_t *)(local_rsp - 0x37 - 0x7D) = 0;
    *(uint64_t *)(local_rsp - 0x37 - 0x49) = 0;
    *(uint32_t *)(local_rsp - 0x37 - 0x79) = 0;
    *(uint32_t *)(local_rsp - 0x37 - 0x71) = 0;
loc_002D266C:
    if (1 == 0) goto loc_002D2A32;
loc_002D2675:
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 - 0x29) + 0x0 * 8)) >> (10);
    result = (uint32_t)((result) & (3));
    Arg3 = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 - 0x29) + 0x0 * 8)) >> (12);
    *(uint64_t *)(local_rsp - 0x37 - 0x49) = Arg3;
    *(uint32_t *)(local_rsp - 0x37 - 0x79) = (uint32_t)(result + result * 8);
    Arg2 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 - 0x29) + 0x0 * 8)) & (0x3FFULL));
    if (condition_is_not_equal) goto loc_002D2A94;
loc_002D26A3:
    if (1 == 0) goto loc_002D292E;
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x37 + 0x5F)) == 0) goto loc_002D26C3;
    result = (uint32_t)((*(uint16_t *)(arg1 + 0xDE)) & (63));
    if (((uint32_t)(result + result * 8)) > ((uint32_t)(result))) goto loc_002D2AC9;
loc_002D26C3:
    Arg1 = (uint32_t)((result + result * 8) & (63));
    result = (uint32_t)((*(uint64_t *)(local_rsp - 0x37 - 0x1)) & (0xFC0ULL));
    Arg1 = (Arg1) | (result);
    result = (Arg3) << (12);
    Arg1 = (Arg1) | (result);
    *(void **)(local_rsp - 0x37 - 0x1) = Arg1;
loc_002D26E0:
    Arg3 = 0;
    result = IvtIommuSendCommand(Arg1, local_rsp - 55 - 9, Arg3, 0);
    Arg3 = 0;
    *(uint64_t *)(local_rsp - 0x37 - 0x41) = *(uint64_t *)(local_rsp - 0x37 - 0x9);
loc_002D2702:
    if (1 == 0) goto loc_002D27AB;
    *(uint64_t *)(local_rsp - 0x37 - 0x69) = *(uint64_t *)(local_rsp - 0x37 + 0x6F);
    if (*(uint64_t *)(local_rsp - 0x37 - 0x21) != 0) goto loc_002D2ADF;
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x37 + 0x5F)) == 0) goto loc_002D2A0E;
    *(uint64_t *)(local_rsp - 0x37 - 0x69) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x6F));
    *(uint8_t *)(local_rsp - 0x37 - 0x80) = 0;
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x6F))) == (*(uint64_t *)(local_rsp - 0x37 + 0x6F))) goto loc_002D2B29;
loc_002D2755:
    *(uint32_t *)(local_rsp - 0x37 - 0x75) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x6F)) - 0x28) + 0x3C)));
    *(uint64_t *)(local_rsp - 0x37 - 0x39) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x6F)) - 0x28) + 0x30);
    *(uint64_t *)(local_rsp - 0x37 - 0x61) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x6F)) - 0x28) + 64;
    *(uint64_t *)(local_rsp - 0x37 - 0x59) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x6F)) + 44;
    if (1 == 0) goto loc_002D290F;
loc_002D2775:
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x6F)) + 0x2C)) != 0) goto loc_002D293F;
    result = ExAcquireRundownProtection(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x6F)) - 0x28) + 64, 1, Arg3, (uint32_t)(*(uint32_t *)(local_rsp - 0x37 - 0x79)));
    Arg3 = 0;
    if ((uint8_t)(result) != 0) goto loc_002D2B36;
loc_002D2792:
loc_002D2796:
    if (*(uint64_t *)(local_rsp - 0x37 + 0x6F) != 0) goto loc_002D2838;
loc_002D279F:
loc_002D27A7:
loc_002D27AB:
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x37 - 0x71))) + 1);
    *(uint32_t *)(local_rsp - 0x37 - 0x71) = (uint32_t)(Arg4);
    if (((uint32_t)(Arg4)) < (*(uint32_t *)(local_rsp - 0x37 + 0x77))) goto loc_002D266C;
    Arg3 = 0;
    Arg2 = 0;
    result = IvtIommuWaitCommand(*(uint64_t *)(local_rsp - 0x37 - 0x51), Arg2, Arg3, Arg4);
    local_rdi = 0;
    if ((*(uint8_t *)(local_rsp - 0x37 - 0x7D)) != 0) goto loc_002D2C24;
loc_002D27E5:
    if (*(uint64_t *)(local_rsp - 0x37 + 0x6F) == 0) goto loc_002D280A;
    *(uint64_t *)(local_rsp - 0x37 - 0x69) = *(uint64_t *)(local_rsp - 0x37 + 0x6F);
loc_002D27F1:
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x37 + 0x5F)) == 0) goto loc_002D2C3A;
    *(uint64_t *)(local_rsp - 0x37 - 0x69) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x6F));
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x6F))) != (*(uint64_t *)(local_rsp - 0x37 + 0x6F))) goto loc_002D28D6;
loc_002D280A:
    Arg1 = (*(uint64_t *)(local_rsp - 0x37 + 0x7)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
loc_002D2838:
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x37 + 0x5F)) == 0) goto loc_002D287B;
    *(uint64_t *)(local_rsp - 0x37 - 0x69) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x6F)));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x6F)))) == (*(uint64_t *)(local_rsp - 0x37 + 0x6F))) goto loc_002D279F;
    *(uint8_t *)(local_rsp - 0x37 - 0x80) = 0;
    *(uint64_t *)(local_rsp - 0x37 - 0x59) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x6F))) + 44;
    *(uint64_t *)(local_rsp - 0x37 - 0x39) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x6F))) - 0x28) + 0x30);
    *(uint64_t *)(local_rsp - 0x37 - 0x61) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x6F))) - 0x28) + 64;
    *(uint32_t *)(local_rsp - 0x37 - 0x75) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 + 0x6F))) - 0x28) + 0x3C)));
    goto loc_002D28CD;
loc_002D287B:
    v_stack_mA0 = local_rsp - 55 - 89;
    v_stack_mA8 = local_rsp - 55 - 97;
    v_stack_mB0 = local_rsp - 55 - 128;
    result = HalpIommuGetNextFlushDevice(*(uint64_t *)(local_rsp - 0x37 + 0x6F), local_rsp - 55 - 105, local_rsp - 55 - 57, local_rsp - 55 - 117);
    Arg3 = 0;
    if ((uint8_t)(result) == 0) goto loc_002D279F;
loc_002D28CD:
    goto loc_002D2775;
loc_002D28D6:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) - 0x28)) + (64);
    *(uint64_t *)(local_rsp - 0x37 - 0x59) = *(uint64_t *)(v_stack_m28 + 0x38) + 44;
    *(void **)(local_rsp - 0x37 - 0x61) = Arg1;
loc_002D28EA:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x2C)) == ((uint8_t)(*(uint8_t *)(local_rsp - 0x37 - 0x80)))) goto loc_002D27F1;
    *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x2C) = (uint8_t)(*(uint8_t *)(local_rsp - 0x37 - 0x80));
    result = ExReleaseRundownProtection(Arg1, local_rsp - 55 - 105, Arg3, (uint32_t)(*(uint32_t *)(local_rsp - 0x37 - 0x79)));
    goto loc_002D27F1;
loc_002D2900:
    *(uint8_t *)(local_rsp - 0x37 - 0x7F) = 0;
loc_002D2907:
    goto loc_002D2656;
loc_002D290F:
    goto loc_002D27A7;
loc_002D291C:
    v_stack_m90 = 0;
    goto loc_002D2624;
loc_002D292E:
    Arg3 = 0;
loc_002D2931:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x37 - 0x79))) != 0) goto loc_002D2702;
    goto loc_002D26E0;
loc_002D293F:
    *(uint64_t *)(local_rsp - 0x37 - 0x19) = v_xmm0;
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x37 + 0x5F)) != 0) goto loc_002D2BE9;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x37 - 0x31)))) == -1) goto loc_002D2B43;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x37 - 0x31))))) & (0xFFFFFULL));
    result = (result) << (32);
    Arg3 = ((uint16_t)(*(uint64_t *)(local_rsp - 0x37 - 0x51))) << (16);
    result = (result) & (Arg1);
    Arg3 = (Arg3) | (result);
    Arg3 = (Arg3) | (8);
    if (condition_is_below) goto loc_002D2B91;
loc_002D29A0:
    Arg1 = (0) << (4);
    result = (Arg1) ^ (Arg3);
    result = (result) & (-497);
    result = (result) ^ (Arg1);
    *(uint64_t *)(local_rsp - 0x37 - 0x19) = result;
    if ((*(uint32_t *)(local_rsp - 0x37 + 0x77)) == 0) goto loc_002D2BC1;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x37 - 0x79))) == 0) goto loc_002D2BD3;
    Arg2 = (uint32_t)((*(uint64_t *)(local_rsp - 0x37 - 0x11)) & (0xFFEULL));
    result = (1) << (18);
    result = (result) - 1;
    result = (result) | (*(uint64_t *)(local_rsp - 0x37 - 0x49));
    result = (result) << (12);
    result = (result) | (Arg2);
    result = (result) | (1);
    *(uint64_t *)(local_rsp - 0x37 - 0x11) = result;
    Arg3 = 0;
    result = IvtIommuSendCommand(*(uint64_t *)(local_rsp - 0x37 - 0x51), local_rsp - 55 - 25, Arg3, (uint32_t)(*(uint32_t *)(local_rsp - 0x37 - 0x79)));
    Arg3 = 0;
    goto loc_002D2796;
loc_002D2A0E:
    if ((*(uint64_t *)(local_rsp - 0x37 - 0x51)) != (*(uint64_t *)(local_rsp - 0x37 + 0x6F))) goto loc_002D2B10;
    *(uint8_t *)(local_rsp - 0x37 - 0x80) = 0;
    goto loc_002D2755;
loc_002D2A32:
    if ((uint8_t)(result) == 0) goto loc_002D2931;
    goto loc_002D2675;
loc_002D2A3F:
    v_stack_m90 = 0;
loc_002D2A6F:
    goto loc_002D25FA;
loc_002D2A7C:
    if (*(uint64_t *)(local_rsp - 0x37 - 0x21) == 0) goto loc_002D2639;
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 - 0x21) + 0x60)) != 0) goto loc_002D2642;
    goto loc_002D2639;
loc_002D2A94:
    result = (1) << (0);
    result = (result) * (0);
    result = (result) + (0);
    result = (result) ^ (0);
    Arg1 = (uint32_t)((0) + 1);
    result = (1) << ((uint8_t)(Arg1));
    result = (result) - 1;
    *(uint32_t *)(local_rsp - 0x37 - 0x79) = (uint32_t)(Arg1);
    result = ~(result);
    Arg3 = (Arg3) & (result);
    *(uint64_t *)(local_rsp - 0x37 - 0x49) = Arg3;
    goto loc_002D26A3;
loc_002D2AC9:
    local_rbx = (50) & (-17);
    v_stack_m90 = 0;
    local_rbx = (local_rbx) | (32);
    *(uint64_t *)(local_rsp - 0x37 - 0x9) = local_rbx;
    goto loc_002D26E0;
loc_002D2ADF:
    *(uint64_t *)(local_rsp - 0x37 - 0x39) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 - 0x21) + 0x30);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 - 0x21) + 0x60) + 0x30))))) & (1));
    *(uint32_t *)(local_rsp - 0x37 - 0x75) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x37 - 0x21) + 0x3C)));
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x37 - 0x21) + 0x60) + 0x30))) >> (11));
    local_rdi = (uint8_t)((local_rdi) & (1));
loc_002D2B10:
    goto loc_002D2A0E;
loc_002D2B29:
    *(uint64_t *)(local_rsp - 0x37 - 0x61) = Arg3;
    *(uint64_t *)(local_rsp - 0x37 - 0x59) = Arg3;
    goto loc_002D27AB;
loc_002D2B36:
    *(uint8_t *)(0) = 1;
    goto loc_002D293F;
loc_002D2B43:
    if ((*(uint32_t *)(local_rsp - 0x37 - 0x71)) != Arg3) goto loc_002D2792;
    Arg2 = ((uint16_t)(*(uint64_t *)(arg1 + 0x28))) << (32);
    Arg2 = (Arg2) | (3);
    local_rsi = (uint32_t)((*(uint64_t *)(arg1 + 0x28)) & (15));
    result = (*(uint64_t *)(arg1 + 0x28)) & (-16);
    result = (result) << (36);
    result = (result) | (local_rsi);
    result = (result) << (12);
    Arg2 = (Arg2) | (result);
loc_002D2B91:
    Arg1 = (local_rsi) & (-16);
    local_rsi = (uint32_t)((local_rsi) & (15));
    Arg1 = (Arg1) << (36);
    Arg1 = (Arg1) | (local_rsi);
    result = (Arg3) & (Arg3);
    Arg1 = (Arg1) << (12);
    Arg3 = (Arg1) | (result);
    goto loc_002D29A0;
loc_002D2BC1:
    Arg2 = (uint32_t)((Arg2) & (0x7FFULL));
    goto loc_002D2BE1;
loc_002D2BD3:
    Arg2 = (uint32_t)((Arg2) & (0xFFFULL));
    result = (*(uint64_t *)(local_rsp - 0x37 - 0x49)) << (12);
loc_002D2BE1:
    Arg2 = (Arg2) | (result);
loc_002D2BE9:
    Arg2 = ((uint16_t)(local_rsi)) << (32);
    Arg2 = (Arg2) | (3);
    local_rsi = (uint32_t)((local_rsi) & (15));
    result = (local_rsi) & (-16);
    result = (result) << (36);
    result = (result) | (local_rsi);
    result = (result) << (12);
    Arg2 = (Arg2) | (result);
loc_002D2C24:
    Arg1 = (*(uint64_t *)(local_rsp - 0x37 - 0x21)) + (64);
    *(void **)(local_rsp - 0x37 - 0x61) = Arg1;
    result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(local_rsp - 0x37 - 0x79)));
    goto loc_002D27E5;
loc_002D2C3A:
    v_stack_mA0 = local_rsp - 55 - 89;
    v_stack_mA8 = local_rsp - 55 - 97;
    v_stack_mB0 = local_rsp - 55 - 128;
    result = HalpIommuGetNextFlushDevice(*(uint64_t *)(local_rsp - 0x37 + 0x6F), local_rsp - 55 - 105, local_rsp - 55 - 57, local_rsp - 55 - 117);
    if ((uint8_t)(result) == 0) goto loc_002D280A;
    goto loc_002D28EA;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xD8` | `64` | `R` |
| `Arg1` | `+ 0xE0` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002D2548&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
