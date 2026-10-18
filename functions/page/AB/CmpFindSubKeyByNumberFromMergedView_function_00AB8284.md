# CmpFindSubKeyByNumberFromMergedView

- RVA: `0x00AB8284`–`0x00AB87A0` (길이 `1,308` bytes)
- VA: `0x0000000140AB8284`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD1B0`
- 디코드: `361`개 명령, `1,308/1,308` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AB8341` → [CmpDelayDerefKeyControlBlock](../84/CmpDelayDerefKeyControlBlock_function_0084FA50.md) (function, `0x0084FA50`)
- `0x00AB835C` → [CmpDelayDerefKeyControlBlock](../84/CmpDelayDerefKeyControlBlock_function_0084FA50.md) (function, `0x0084FA50`)
- `0x00AB83DD` → [CmpFindSubKeyByNumberEx](../84/CmpFindSubKeyByNumberEx_function_0084F1A0.md) (function, `0x0084F1A0`)
- `0x00AB8489` → [CmpFindSubKeyByNumberEx](../84/CmpFindSubKeyByNumberEx_function_0084F1A0.md) (function, `0x0084F1A0`)
- `0x00AB84F5` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00AB84FC` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00AB8536` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00AB853D` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00AB8569` → [CmpDelayDerefKeyControlBlock](../84/CmpDelayDerefKeyControlBlock_function_0084FA50.md) (function, `0x0084FA50`)
- `0x00AB857D` → [CmpDelayDerefKeyControlBlock](../84/CmpDelayDerefKeyControlBlock_function_0084FA50.md) (function, `0x0084FA50`)
- `0x00AB85AA` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00AB8677` → [CmpCompareKeysByName](../94/CmpCompareKeysByName_function_00944950.md) (function, `0x00944950`)
- `0x00AB86EF` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00AB86F6` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00AB8729` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00AB8730` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00AB874B` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00AB876A` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00AB8771` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)

### Direct callers
- [sub_0084E7D5](../84/Unknown_function_0084E7D5.md) at `0x0084E981`
- [CmQueryKey](../85/CmQueryKey_function_00858240.md) at `0x00858476`
- [CmQueryKey](../85/CmQueryKey_function_00858240.md) at `0x008588D8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB8284  48 8B C4                        mov rax, rsp
00AB8287  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00AB828B  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00AB828F  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00AB8293  48 89 48 08                     mov qword ptr [rax + 8], rcx
00AB8297  55                              push rbp
00AB8298  53                              push rbx
00AB8299  56                              push rsi
00AB829A  57                              push rdi
00AB829B  41 54                           push r12
00AB829D  41 55                           push r13
00AB829F  41 56                           push r14
00AB82A1  41 57                           push r15
00AB82A3  48 8D 68 B9                     lea rbp, [rax - 0x47]
00AB82A7  48 81 EC B8 00 00 00            sub rsp, 0xb8
00AB82AE  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
00AB82B2  45 33 D2                        xor r10d, r10d
00AB82B5  45 8B C8                        mov r9d, r8d
00AB82B8  44 89 55 CB                     mov dword ptr [rbp - 0x35], r10d
00AB82BC  41 83 C8 FF                     or r8d, 0xffffffff
00AB82C0  44 89 55 CF                     mov dword ptr [rbp - 0x31], r10d
00AB82C4  48 85 D2                        test rdx, rdx
00AB82C7  44 88 55 9F                     mov byte ptr [rbp - 0x61], r10b
00AB82CB  4C 89 10                        mov qword ptr [rax], r10
00AB82CE  45 8D 5A 01                     lea r11d, [r10 + 1]
00AB82D2  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00AB82D6  BF 9A 00 00 C0                  mov edi, 0xc000009a
00AB82DB  45 8A F2                        mov r14b, r10b
00AB82DE  4C 89 55 D7                     mov qword ptr [rbp - 0x29], r10
00AB82E2  41 8B DA                        mov ebx, r10d
00AB82E5  44 89 45 B7                     mov dword ptr [rbp - 0x49], r8d
00AB82E9  44 89 55 BB                     mov dword ptr [rbp - 0x45], r10d
00AB82ED  45 8B E8                        mov r13d, r8d
00AB82F0  44 89 00                        mov dword ptr [rax], r8d
00AB82F3  45 8B E0                        mov r12d, r8d
00AB82F6  41 0F B6 C2                     movzx eax, r10b
00AB82FA  41 8B F2                        mov esi, r10d
00AB82FD  41 0F 44 C3                     cmove eax, r11d
00AB8301  44 89 45 AF                     mov dword ptr [rbp - 0x51], r8d
00AB8305  89 45 C3                        mov dword ptr [rbp - 0x3d], eax
00AB8308  45 8B FA                        mov r15d, r10d
00AB830B  44 89 55 B3                     mov dword ptr [rbp - 0x4d], r10d
00AB830F  44 89 45 C7                     mov dword ptr [rbp - 0x39], r8d
00AB8313  44 89 45 A3                     mov dword ptr [rbp - 0x5d], r8d
00AB8317  44 88 55 A7                     mov byte ptr [rbp - 0x59], r10b
00AB831B  4C 89 55 E7                     mov qword ptr [rbp - 0x19], r10
00AB831F  4C 89 55 EF                     mov qword ptr [rbp - 0x11], r10
00AB8323  4C 89 55 DF                     mov qword ptr [rbp - 0x21], r10
00AB8327  45 84 F6                        test r14b, r14b
00AB832A  74 09                           je 0x140ab8335
00AB832C  41 3B D9                        cmp ebx, r9d
00AB832F  0F 83 0C 04 00 00               jae 0x140ab8741
00AB8335  48 85 F6                        test rsi, rsi
00AB8338  74 16                           je 0x140ab8350
00AB833A  48 8B 55 6F                     mov rdx, qword ptr [rbp + 0x6f]
00AB833E  48 8B CE                        mov rcx, rsi
00AB8341  E8 0A 77 D9 FF                  call 0x14084fa50
00AB8346  45 33 D2                        xor r10d, r10d
00AB8349  41 8B F2                        mov esi, r10d
00AB834C  4C 89 55 E7                     mov qword ptr [rbp - 0x19], r10
00AB8350  4D 85 FF                        test r15, r15
00AB8353  74 16                           je 0x140ab836b
00AB8355  48 8B 55 6F                     mov rdx, qword ptr [rbp + 0x6f]
00AB8359  49 8B CF                        mov rcx, r15
00AB835C  E8 EF 76 D9 FF                  call 0x14084fa50
00AB8361  45 33 D2                        xor r10d, r10d
00AB8364  45 8B FA                        mov r15d, r10d
00AB8367  4C 89 55 EF                     mov qword ptr [rbp - 0x11], r10
00AB836B  44 38 55 A7                     cmp byte ptr [rbp - 0x59], r10b
00AB836F  0F 85 99 00 00 00               jne 0x140ab840e
00AB8375  41 83 FD FF                     cmp r13d, -1
00AB8379  0F 85 8F 00 00 00               jne 0x140ab840e
00AB837F  4C 8B 4D 67                     mov r9, qword ptr [rbp + 0x67]
00AB8383  4C 8B 6D 4F                     mov r13, qword ptr [rbp + 0x4f]
00AB8387  49 8B C1                        mov rax, r9
00AB838A  48 F7 D8                        neg rax
00AB838D  48 8D 45 E7                     lea rax, [rbp - 0x19]
00AB8391  4D 1B C0                        sbb r8, r8
00AB8394  4C 23 C0                        and r8, rax
00AB8397  49 8B C1                        mov rax, r9
00AB839A  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
00AB839F  48 F7 D8                        neg rax
00AB83A2  44 8B 45 CB                     mov r8d, dword ptr [rbp - 0x35]
00AB83A6  49 8B C1                        mov rax, r9
00AB83A9  48 1B D2                        sbb rdx, rdx
00AB83AC  48 23 55 57                     and rdx, qword ptr [rbp + 0x57]
00AB83B0  48 F7 D8                        neg rax
00AB83B3  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
00AB83B7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AB83BC  48 1B C9                        sbb rcx, rcx
00AB83BF  4C 89 4C 24 30                  mov qword ptr [rsp + 0x30], r9
00AB83C4  49 23 CD                        and rcx, r13
00AB83C7  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
00AB83CC  4C 8D 4D C7                     lea r9, [rbp - 0x39]
00AB83D0  41 8B 55 28                     mov edx, dword ptr [r13 + 0x28]
00AB83D4  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00AB83D9  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
00AB83DD  E8 BE 6D D9 FF                  call 0x14084f1a0
00AB83E2  48 8B 75 E7                     mov rsi, qword ptr [rbp - 0x19]
00AB83E6  45 33 D2                        xor r10d, r10d
00AB83E9  8B F8                           mov edi, eax
00AB83EB  85 C0                           test eax, eax
00AB83ED  0F 88 66 01 00 00               js 0x140ab8559
00AB83F3  8B 45 A7                        mov eax, dword ptr [rbp - 0x59]
00AB83F6  45 8D 5A 01                     lea r11d, [r10 + 1]
00AB83FA  44 8B 6D C7                     mov r13d, dword ptr [rbp - 0x39]
00AB83FE  41 83 FD FF                     cmp r13d, -1
00AB8402  0F B6 C0                        movzx eax, al
00AB8405  41 0F 44 C3                     cmove eax, r11d
00AB8409  89 45 A7                        mov dword ptr [rbp - 0x59], eax
00AB840C  EB 06                           jmp 0x140ab8414
00AB840E  41 BB 01 00 00 00               mov r11d, 1
00AB8414  8B 45 C3                        mov eax, dword ptr [rbp - 0x3d]
00AB8417  84 C0                           test al, al
00AB8419  0F 85 99 00 00 00               jne 0x140ab84b8
00AB841F  41 83 FC FF                     cmp r12d, -1
00AB8423  0F 85 8F 00 00 00               jne 0x140ab84b8
00AB8429  4C 8B 4D 67                     mov r9, qword ptr [rbp + 0x67]
00AB842D  4C 8B 65 57                     mov r12, qword ptr [rbp + 0x57]
00AB8431  49 8B C1                        mov rax, r9
00AB8434  48 F7 D8                        neg rax
00AB8437  48 8D 45 EF                     lea rax, [rbp - 0x11]
00AB843B  4D 1B C0                        sbb r8, r8
00AB843E  4C 23 C0                        and r8, rax
00AB8441  49 8B C1                        mov rax, r9
00AB8444  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
00AB8449  48 F7 D8                        neg rax
00AB844C  44 8B 45 CF                     mov r8d, dword ptr [rbp - 0x31]
00AB8450  49 8B C1                        mov rax, r9
00AB8453  48 1B D2                        sbb rdx, rdx
00AB8456  48 23 55 4F                     and rdx, qword ptr [rbp + 0x4f]
00AB845A  48 F7 D8                        neg rax
00AB845D  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
00AB8461  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AB8466  48 1B C9                        sbb rcx, rcx
00AB8469  4C 89 4C 24 30                  mov qword ptr [rsp + 0x30], r9
00AB846E  49 23 CC                        and rcx, r12
00AB8471  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
00AB8476  4C 8D 4D A3                     lea r9, [rbp - 0x5d]
00AB847A  41 8B 54 24 28                  mov edx, dword ptr [r12 + 0x28]
00AB847F  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00AB8484  49 8B 4C 24 20                  mov rcx, qword ptr [r12 + 0x20]
00AB8489  E8 12 6D D9 FF                  call 0x14084f1a0
00AB848E  4C 8B 7D EF                     mov r15, qword ptr [rbp - 0x11]
00AB8492  45 33 D2                        xor r10d, r10d
00AB8495  8B F8                           mov edi, eax
00AB8497  85 C0                           test eax, eax
00AB8499  0F 88 84 01 00 00               js 0x140ab8623
00AB849F  8B 45 C3                        mov eax, dword ptr [rbp - 0x3d]
00AB84A2  45 8D 5A 01                     lea r11d, [r10 + 1]
00AB84A6  44 8B 65 A3                     mov r12d, dword ptr [rbp - 0x5d]
00AB84AA  41 83 FC FF                     cmp r12d, -1
00AB84AE  0F B6 C0                        movzx eax, al
00AB84B1  41 0F 44 C3                     cmove eax, r11d
00AB84B5  89 45 C3                        mov dword ptr [rbp - 0x3d], eax
00AB84B8  44 38 55 A7                     cmp byte ptr [rbp - 0x59], r10b
00AB84BC  74 10                           je 0x140ab84ce
00AB84BE  84 C0                           test al, al
00AB84C0  0F 85 7B 02 00 00               jne 0x140ab8741
00AB84C6  41 BE 02 00 00 00               mov r14d, 2
00AB84CC  EB 09                           jmp 0x140ab84d7
00AB84CE  84 C0                           test al, al
00AB84D0  45 8B F2                        mov r14d, r10d
00AB84D3  41 0F 95 C6                     setne r14b
00AB84D7  41 83 FC FF                     cmp r12d, -1
00AB84DB  74 37                           je 0x140ab8514
00AB84DD  48 8B 45 57                     mov rax, qword ptr [rbp + 0x57]
00AB84E1  4C 8D 45 AF                     lea r8, [rbp - 0x51]
00AB84E5  41 8B D4                        mov edx, r12d
00AB84E8  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00AB84EC  44 84 99 8C 00 00 00            test byte ptr [rcx + 0x8c], r11b
00AB84F3  74 07                           je 0x140ab84fc
00AB84F5  E8 66 C7 D9 FF                  call 0x140854c60
00AB84FA  EB 05                           jmp 0x140ab8501
00AB84FC  E8 AF C7 D9 FF                  call 0x140854cb0
00AB8501  45 33 D2                        xor r10d, r10d
00AB8504  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
00AB8508  48 8B C8                        mov rcx, rax
00AB850B  48 85 C0                        test rax, rax
00AB850E  74 41                           je 0x140ab8551
00AB8510  45 8D 5A 01                     lea r11d, [r10 + 1]
00AB8514  41 83 FD FF                     cmp r13d, -1
00AB8518  0F 84 96 00 00 00               je 0x140ab85b4
00AB851E  48 8B 45 4F                     mov rax, qword ptr [rbp + 0x4f]
00AB8522  4C 8D 45 B7                     lea r8, [rbp - 0x49]
00AB8526  41 8B D5                        mov edx, r13d
00AB8529  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00AB852D  44 84 99 8C 00 00 00            test byte ptr [rcx + 0x8c], r11b
00AB8534  74 07                           je 0x140ab853d
00AB8536  E8 25 C7 D9 FF                  call 0x140854c60
00AB853B  EB 05                           jmp 0x140ab8542
00AB853D  E8 6E C7 D9 FF                  call 0x140854cb0
00AB8542  45 33 D2                        xor r10d, r10d
00AB8545  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
00AB8549  4C 8B C0                        mov r8, rax
00AB854C  48 85 C0                        test rax, rax
00AB854F  75 67                           jne 0x140ab85b8
00AB8551  44 8A 75 9F                     mov r14b, byte ptr [rbp - 0x61]
00AB8555  4C 8B 6D 4F                     mov r13, qword ptr [rbp + 0x4f]
00AB8559  4C 8B 65 57                     mov r12, qword ptr [rbp + 0x57]
00AB855D  48 85 F6                        test rsi, rsi
00AB8560  74 0F                           je 0x140ab8571
00AB8562  48 8B 55 6F                     mov rdx, qword ptr [rbp + 0x6f]
00AB8566  48 8B CE                        mov rcx, rsi
00AB8569  E8 E2 74 D9 FF                  call 0x14084fa50
00AB856E  45 33 D2                        xor r10d, r10d
00AB8571  4D 85 FF                        test r15, r15
00AB8574  74 0F                           je 0x140ab8585
00AB8576  48 8B 55 6F                     mov rdx, qword ptr [rbp + 0x6f]
00AB857A  49 8B CF                        mov rcx, r15
00AB857D  E8 CE 74 D9 FF                  call 0x14084fa50
00AB8582  45 33 D2                        xor r10d, r10d
00AB8585  BE 01 00 00 00                  mov esi, 1
00AB858A  4C 39 55 DF                     cmp qword ptr [rbp - 0x21], r10
00AB858E  0F 84 BF 01 00 00               je 0x140ab8753
00AB8594  49 8B 4C 24 20                  mov rcx, qword ptr [r12 + 0x20]
00AB8599  48 8D 55 AF                     lea rdx, [rbp - 0x51]
00AB859D  40 84 B1 8C 00 00 00            test byte ptr [rcx + 0x8c], sil
00AB85A4  0F 84 A1 01 00 00               je 0x140ab874b
00AB85AA  E8 71 46 DA FF                  call 0x14085cc20
00AB85AF  E9 9C 01 00 00                  jmp 0x140ab8750
00AB85B4  4C 8B 45 D7                     mov r8, qword ptr [rbp - 0x29]
00AB85B8  45 8A E2                        mov r12b, r10b
00AB85BB  45 85 F6                        test r14d, r14d
00AB85BE  0F 84 AC 00 00 00               je 0x140ab8670
00AB85C4  41 BB 01 00 00 00               mov r11d, 1
00AB85CA  41 83 EE 01                     sub r14d, 1
00AB85CE  74 5C                           je 0x140ab862c
00AB85D0  45 3B F3                        cmp r14d, r11d
00AB85D3  0F 85 EE 00 00 00               jne 0x140ab86c7
00AB85D9  8D 43 01                        lea eax, [rbx + 1]
00AB85DC  45 8A F3                        mov r14b, r11b
00AB85DF  44 38 55 9F                     cmp byte ptr [rbp - 0x61], r10b
00AB85E3  44 88 5D 9F                     mov byte ptr [rbp - 0x61], r11b
00AB85E7  0F 44 C3                        cmove eax, ebx
00AB85EA  8B D8                           mov ebx, eax
00AB85EC  3B 45 5F                        cmp eax, dword ptr [rbp + 0x5f]
00AB85EF  0F 85 C4 00 00 00               jne 0x140ab86b9
00AB85F5  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
00AB85F9  4C 8B 65 57                     mov r12, qword ptr [rbp + 0x57]
00AB85FD  49 8B 44 24 20                  mov rax, qword ptr [r12 + 0x20]
00AB8602  48 89 01                        mov qword ptr [rcx], rax
00AB8605  8B 45 A3                        mov eax, dword ptr [rbp - 0x5d]
00AB8608  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
00AB860C  89 01                           mov dword ptr [rcx], eax
00AB860E  48 8B 85 87 00 00 00            mov rax, qword ptr [rbp + 0x87]
00AB8615  48 85 C0                        test rax, rax
00AB8618  74 06                           je 0x140ab8620
00AB861A  4C 89 38                        mov qword ptr [rax], r15
00AB861D  4D 8B FA                        mov r15, r10
00AB8620  41 8B FA                        mov edi, r10d
00AB8623  4C 8B 6D 4F                     mov r13, qword ptr [rbp + 0x4f]
00AB8627  E9 31 FF FF FF                  jmp 0x140ab855d
00AB862C  8D 43 01                        lea eax, [rbx + 1]
00AB862F  45 8A F3                        mov r14b, r11b
00AB8632  44 38 55 9F                     cmp byte ptr [rbp - 0x61], r10b
00AB8636  0F 44 C3                        cmove eax, ebx
00AB8639  8B D8                           mov ebx, eax
00AB863B  3B 45 5F                        cmp eax, dword ptr [rbp + 0x5f]
00AB863E  75 64                           jne 0x140ab86a4
00AB8640  48 8B 45 4F                     mov rax, qword ptr [rbp + 0x4f]
00AB8644  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
00AB8648  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
00AB864C  48 89 01                        mov qword ptr [rcx], rax
00AB864F  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00AB8653  44 89 28                        mov dword ptr [rax], r13d
00AB8656  48 8B 85 87 00 00 00            mov rax, qword ptr [rbp + 0x87]
00AB865D  48 85 C0                        test rax, rax
00AB8660  74 06                           je 0x140ab8668
00AB8662  48 89 30                        mov qword ptr [rax], rsi
00AB8665  49 8B F2                        mov rsi, r10
00AB8668  41 8B FA                        mov edi, r10d
00AB866B  E9 E5 FE FF FF                  jmp 0x140ab8555
00AB8670  48 8B 55 DF                     mov rdx, qword ptr [rbp - 0x21]
00AB8674  49 8B C8                        mov rcx, r8
00AB8677  E8 D4 C2 E8 FF                  call 0x140944950
00AB867C  45 33 D2                        xor r10d, r10d
00AB867F  85 C0                           test eax, eax
00AB8681  8D 43 01                        lea eax, [rbx + 1]
00AB8684  45 8D 5A 01                     lea r11d, [r10 + 1]
00AB8688  45 8A F3                        mov r14b, r11b
00AB868B  78 A5                           js 0x140ab8632
00AB868D  0F 8F 4C FF FF FF               jg 0x140ab85df
00AB8693  44 38 55 9F                     cmp byte ptr [rbp - 0x61], r10b
00AB8697  0F 44 C3                        cmove eax, ebx
00AB869A  8B D8                           mov ebx, eax
00AB869C  3B 45 5F                        cmp eax, dword ptr [rbp + 0x5f]
00AB869F  74 9F                           je 0x140ab8640
00AB86A1  45 8A E3                        mov r12b, r11b
00AB86A4  44 01 5D CB                     add dword ptr [rbp - 0x35], r11d
00AB86A8  41 83 CD FF                     or r13d, 0xffffffff
00AB86AC  44 88 75 9F                     mov byte ptr [rbp - 0x61], r14b
00AB86B0  44 89 6D C7                     mov dword ptr [rbp - 0x39], r13d
00AB86B4  45 84 E4                        test r12b, r12b
00AB86B7  74 14                           je 0x140ab86cd
00AB86B9  41 83 CC FF                     or r12d, 0xffffffff
00AB86BD  44 01 5D CF                     add dword ptr [rbp - 0x31], r11d
00AB86C1  44 89 65 A3                     mov dword ptr [rbp - 0x5d], r12d
00AB86C5  EB 0A                           jmp 0x140ab86d1
00AB86C7  44 8B 65 A3                     mov r12d, dword ptr [rbp - 0x5d]
00AB86CB  EB 08                           jmp 0x140ab86d5
00AB86CD  44 8B 65 A3                     mov r12d, dword ptr [rbp - 0x5d]
00AB86D1  4C 8B 45 D7                     mov r8, qword ptr [rbp - 0x29]
00AB86D5  4D 85 C0                        test r8, r8
00AB86D8  74 28                           je 0x140ab8702
00AB86DA  48 8B 45 4F                     mov rax, qword ptr [rbp + 0x4f]
00AB86DE  48 8D 55 B7                     lea rdx, [rbp - 0x49]
00AB86E2  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00AB86E6  44 84 99 8C 00 00 00            test byte ptr [rcx + 0x8c], r11b
00AB86ED  74 07                           je 0x140ab86f6
00AB86EF  E8 2C 45 DA FF                  call 0x14085cc20
00AB86F4  EB 05                           jmp 0x140ab86fb
00AB86F6  E8 45 D8 D9 FF                  call 0x140855f40
00AB86FB  45 33 D2                        xor r10d, r10d
00AB86FE  4C 89 55 D7                     mov qword ptr [rbp - 0x29], r10
00AB8702  44 8A 75 9F                     mov r14b, byte ptr [rbp - 0x61]
00AB8706  44 8B 4D 5F                     mov r9d, dword ptr [rbp + 0x5f]
00AB870A  4C 39 55 DF                     cmp qword ptr [rbp - 0x21], r10
00AB870E  0F 84 13 FC FF FF               je 0x140ab8327
00AB8714  48 8B 45 57                     mov rax, qword ptr [rbp + 0x57]
00AB8718  48 8D 55 AF                     lea rdx, [rbp - 0x51]
00AB871C  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00AB8720  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
00AB8727  74 07                           je 0x140ab8730
00AB8729  E8 F2 44 DA FF                  call 0x14085cc20
00AB872E  EB 05                           jmp 0x140ab8735
00AB8730  E8 0B D8 D9 FF                  call 0x140855f40
00AB8735  44 8B 4D 5F                     mov r9d, dword ptr [rbp + 0x5f]
00AB8739  45 33 D2                        xor r10d, r10d
00AB873C  E9 E2 FB FF FF                  jmp 0x140ab8323
00AB8741  BF 1A 00 00 80                  mov edi, 0x8000001a
00AB8746  E9 0A FE FF FF                  jmp 0x140ab8555
00AB874B  E8 F0 D7 D9 FF                  call 0x140855f40
00AB8750  45 33 D2                        xor r10d, r10d
00AB8753  4C 39 55 D7                     cmp qword ptr [rbp - 0x29], r10
00AB8757  74 1D                           je 0x140ab8776
00AB8759  49 8B 4D 20                     mov rcx, qword ptr [r13 + 0x20]
00AB875D  48 8D 55 B7                     lea rdx, [rbp - 0x49]
00AB8761  40 84 B1 8C 00 00 00            test byte ptr [rcx + 0x8c], sil
00AB8768  74 07                           je 0x140ab8771
00AB876A  E8 B1 44 DA FF                  call 0x14085cc20
00AB876F  EB 05                           jmp 0x140ab8776
00AB8771  E8 CA D7 D9 FF                  call 0x140855f40
00AB8776  41 F6 DE                        neg r14b
00AB8779  8D 43 01                        lea eax, [rbx + 1]
00AB877C  1B C9                           sbb ecx, ecx
00AB877E  23 C8                           and ecx, eax
00AB8780  48 8B 85 8F 00 00 00            mov rax, qword ptr [rbp + 0x8f]
00AB8787  89 08                           mov dword ptr [rax], ecx
00AB8789  8B C7                           mov eax, edi
00AB878B  48 81 C4 B8 00 00 00            add rsp, 0xb8
00AB8792  41 5F                           pop r15
00AB8794  41 5E                           pop r14
00AB8796  41 5D                           pop r13
00AB8798  41 5C                           pop r12
00AB879A  5F                              pop rdi
00AB879B  5E                              pop rsi
00AB879C  5B                              pop rbx
00AB879D  5D                              pop rbp
00AB879E  C3                              ret
00AB879F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpFindSubKeyByNumberFromMergedView(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (184);
    v_r10 = 0;
    *(unsigned int *)(v_rsp - 71 - 53) = 0;
    a3 = (unsigned int)((a3) | (0xFFFFFFFFULL));
    *(unsigned int *)(v_rsp - 71 - 49) = 0;
    *(unsigned __int8 *)(v_rsp - 71 - 97) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 119)) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 41) = 0;
    *(unsigned int *)(v_rsp - 71 - 73) = a3;
    *(unsigned int *)(v_rsp - 71 - 69) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 127)) = a3;
    result = 0;
    if (a2 == 0) { result = (unsigned int)(v_r10 + 1); }
    *(unsigned int *)(v_rsp - 71 - 81) = a3;
    *(unsigned int *)(v_rsp - 71 - 61) = (unsigned int)(result);
    *(unsigned int *)(v_rsp - 71 - 77) = 0;
    *(unsigned int *)(v_rsp - 71 - 57) = a3;
    *(unsigned int *)(v_rsp - 71 - 93) = a3;
    *(unsigned __int8 *)(v_rsp - 71 - 89) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 25) = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 17) = 0;
loc_00AB8323:
    *(unsigned __int64 *)(v_rsp - 71 - 33) = 0;
loc_00AB8327:
    if (0 == 0) goto loc_00AB8335;
    if (0 >= ((unsigned int)((unsigned int)(a3)))) goto loc_00AB8741;
loc_00AB8335:
    v_rsi = 0;
    if (0 != 0) {
        a2 = *(unsigned __int64 *)(v_rsp - 71 + 111);
        a1 = 0;
        result = CmpDelayDerefKeyControlBlock(a1, a2, a3, (unsigned int)(a3));
        v_r10 = 0;
        v_rsi = 0;
        *(unsigned __int64 *)(v_rsp - 71 - 25) = 0;
    }
    v_r15 = 0;
    if (0 != 0) {
        a2 = *(unsigned __int64 *)(v_rsp - 71 + 111);
        a1 = 0;
        result = CmpDelayDerefKeyControlBlock(a1, a2, a3, (unsigned int)(a3));
        v_r10 = 0;
        v_r15 = 0;
        *(unsigned __int64 *)(v_rsp - 71 - 17) = 0;
    }
    if ((*(unsigned __int8 *)(v_rsp - 71 - 89)) != 0) goto loc_00AB840E;
    if (((unsigned int)((unsigned int)(a3))) != -1) goto loc_00AB840E;
    result = -(*(unsigned __int64 *)(v_rsp - 71 + 103));
    a3 = (a3) & (v_rsp - 71 - 25);
    v_stack_mB8 = a3;
    result = -(*(unsigned __int64 *)(v_rsp - 71 + 103));
    a2 = (a2) & (*(unsigned __int64 *)(v_rsp - 71 + 87));
    result = -(*(unsigned __int64 *)(v_rsp - 71 + 103));
    v_stack_mC0 = *(unsigned __int64 *)(v_rsp - 71 + 111);
    v_stack_mC8 = *(unsigned __int64 *)(v_rsp - 71 + 103);
    a1 = (a1) & (*(unsigned __int64 *)(v_rsp - 71 + 79));
    v_stack_mD0 = a2;
    v_stack_mD8 = a1;
    result = CmpFindSubKeyByNumberEx(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + 40)), (unsigned int)(*(unsigned int *)(v_rsp - 71 - 53)), v_rsp - 71 - 57);
    v_r10 = 0;
    if (sign_flag) goto loc_00AB8559;
    result = (unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 89)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)))) == -1) { result = (unsigned int)(v_r10 + 1); }
    *(unsigned int *)(v_rsp - 71 - 89) = (unsigned int)(result);
    goto loc_00AB8414;
loc_00AB840E:
loc_00AB8414:
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 61))) != 0) goto loc_00AB84B8;
    if (((unsigned int)((unsigned int)(a3))) != -1) goto loc_00AB84B8;
    result = -(*(unsigned __int64 *)(v_rsp - 71 + 103));
    a3 = ((unsigned int)(*(unsigned int *)(v_rsp - 71 - 53))) & (v_rsp - 71 - 17);
    v_stack_mB8 = a3;
    result = -(*(unsigned __int64 *)(v_rsp - 71 + 103));
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + 40))) & (*(unsigned __int64 *)(v_rsp - 71 + 79));
    result = -(*(unsigned __int64 *)(v_rsp - 71 + 103));
    v_stack_mC0 = *(unsigned __int64 *)(v_rsp - 71 + 111);
    v_stack_mC8 = *(unsigned __int64 *)(v_rsp - 71 + 103);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + 32)) & (*(unsigned __int64 *)(v_rsp - 71 + 87));
    v_stack_mD0 = a2;
    v_stack_mD8 = a1;
    result = CmpFindSubKeyByNumberEx(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 87) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 87) + 40)), (unsigned int)(*(unsigned int *)(v_rsp - 71 - 49)), v_rsp - 71 - 93);
    v_r10 = 0;
    if (sign_flag) goto loc_00AB8623;
    result = (unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 61)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 93)))) == -1) { result = (unsigned int)(v_r10 + 1); }
    *(unsigned int *)(v_rsp - 71 - 61) = (unsigned int)(result);
loc_00AB84B8:
    if ((*(unsigned __int8 *)(v_rsp - 71 - 89)) == 0) goto loc_00AB84CE;
    if ((unsigned __int8)(result) != 0) goto loc_00AB8741;
    goto loc_00AB84D7;
loc_00AB84CE:
    v_r14 = ((unsigned __int8)(result) != 0) ? 1 : 0;
loc_00AB84D7:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 93)))) == -1) goto loc_00AB8514;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 87) + 32) + 140)) & ((unsigned __int8)(v_r10 + 1))) == 0) goto loc_00AB84FC;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 87) + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 93)))), v_rsp - 71 - 81, v_rsp - 71 - 93);
    goto loc_00AB8501;
loc_00AB84FC:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 87) + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 93)))), v_rsp - 71 - 81, v_rsp - 71 - 93);
loc_00AB8501:
    v_r10 = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 33) = result;
    if (result == 0) goto loc_00AB8551;
loc_00AB8514:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)))) == -1) goto loc_00AB85B4;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + 32) + 140)) & ((unsigned __int8)(v_r10 + 1))) == 0) goto loc_00AB853D;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)))), v_rsp - 71 - 73, v_rsp - 71 - 93);
    goto loc_00AB8542;
loc_00AB853D:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 57)))), v_rsp - 71 - 73, v_rsp - 71 - 93);
loc_00AB8542:
    v_r10 = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 41) = result;
    if (result != 0) goto loc_00AB85B8;
loc_00AB8551:
loc_00AB8555:
loc_00AB8559:
loc_00AB855D:
    if (*(unsigned __int64 *)(v_rsp - 71 - 25) != 0) {
        a2 = *(unsigned __int64 *)(v_rsp - 71 + 111);
        a1 = *(unsigned __int64 *)(v_rsp - 71 - 25);
        result = CmpDelayDerefKeyControlBlock(a1, a2, result, v_rsp - 71 - 93);
        v_r10 = 0;
    }
    if (*(unsigned __int64 *)(v_rsp - 71 - 17) != 0) {
        a2 = *(unsigned __int64 *)(v_rsp - 71 + 111);
        a1 = *(unsigned __int64 *)(v_rsp - 71 - 17);
        result = CmpDelayDerefKeyControlBlock(a1, a2, result, v_rsp - 71 - 93);
        v_r10 = 0;
    }
    if ((*(unsigned __int64 *)(v_rsp - 71 - 33)) == 0) goto loc_00AB8753;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 87) + 32) + 140)) & (1)) == 0) goto loc_00AB874B;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 87) + 32), v_rsp - 71 - 81, result, v_rsp - 71 - 93);
    goto loc_00AB8750;
loc_00AB85B4:
loc_00AB85B8:
    if ((unsigned int)(*(unsigned __int8 *)(v_rsp - 71 - 97)) == 0) goto loc_00AB8670;
    v_r14 = (unsigned int)((*(unsigned __int8 *)(v_rsp - 71 - 97)) - (1));
    if (condition_is_equal) goto loc_00AB862C;
    if (((unsigned int)(v_r14)) != 1) goto loc_00AB86C7;
loc_00AB85DF:
    *(unsigned __int8 *)(v_rsp - 71 - 97) = 1;
    result = 0 + 1;
    if ((*(unsigned __int8 *)(v_rsp - 71 - 97)) == 0) { result = 0; }
    if (((unsigned int)(result)) != (*(unsigned int *)(v_rsp - 71 + 95))) goto loc_00AB86B9;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 119)) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 87) + 32);
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 127)) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 71 - 93)));
    v_r15 = *(unsigned __int64 *)(v_rsp - 71 - 17);
    if (*(unsigned __int64 *)(v_rsp - 71 + 135) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 135)) = *(unsigned __int64 *)(v_rsp - 71 - 17);
        v_r15 = 0;
    }
loc_00AB8623:
    goto loc_00AB855D;
loc_00AB862C:
loc_00AB8632:
    result = (unsigned int)((unsigned int)(result)) + 1;
    if ((*(unsigned __int8 *)(v_rsp - 71 - 97)) == 0) { result = (unsigned int)((unsigned int)((unsigned int)(result))); }
    if (((unsigned int)(result)) != (*(unsigned int *)(v_rsp - 71 + 95))) goto loc_00AB86A4;
loc_00AB8640:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 119)) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + 32);
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 127)) = (unsigned int)(*(unsigned __int64 *)(v_rsp - 71 + 79));
    v_rsi = 1;
    if (*(unsigned __int64 *)(v_rsp - 71 + 135) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 135)) = 1;
        v_rsi = 0;
    }
    goto loc_00AB8555;
loc_00AB8670:
    result = CmpCompareKeysByName(*(unsigned __int64 *)(v_rsp - 71 - 41), *(unsigned __int64 *)(v_rsp - 71 - 33), *(unsigned __int64 *)(v_rsp - 71 - 41), v_rsp - 71 - 93);
    v_r10 = 0;
    if (sign_flag) goto loc_00AB8632;
    if (condition_is_greater) goto loc_00AB85DF;
    result = (unsigned int)((unsigned int)(result)) + 1;
    if ((*(unsigned __int8 *)(v_rsp - 71 - 97)) == 0) { result = (unsigned int)((unsigned int)((unsigned int)(result))); }
    if (((unsigned int)(result)) == (*(unsigned int *)(v_rsp - 71 + 95))) goto loc_00AB8640;
loc_00AB86A4:
    v_r13 = (unsigned int)((*(unsigned __int64 *)(v_rsp - 71 + 79)) | (0xFFFFFFFFULL));
    *(unsigned __int8 *)(v_rsp - 71 - 97) = (unsigned __int8)((unsigned __int8)(v_r10 + 1));
    *(unsigned int *)(v_rsp - 71 - 57) = (unsigned int)(v_r13);
    if ((unsigned __int8)((unsigned __int8)(v_r10 + 1)) == 0) goto loc_00AB86CD;
loc_00AB86B9:
    v_r12 = (unsigned int)(((unsigned __int8)(v_r10 + 1)) | (0xFFFFFFFFULL));
    *(unsigned int *)(v_rsp - 71 - 93) = (unsigned int)(v_r12);
    goto loc_00AB86D1;
loc_00AB86C7:
    goto loc_00AB86D5;
loc_00AB86CD:
loc_00AB86D1:
loc_00AB86D5:
    if (*(unsigned __int64 *)(v_rsp - 71 - 41) == 0) goto loc_00AB8702;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + 32) + 140)) & ((unsigned __int8)(v_r10 + 1))) == 0) goto loc_00AB86F6;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + 32), v_rsp - 71 - 73, *(unsigned __int64 *)(v_rsp - 71 - 41), v_rsp - 71 - 93);
    goto loc_00AB86FB;
loc_00AB86F6:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 79) + 32), v_rsp - 71 - 73, *(unsigned __int64 *)(v_rsp - 71 - 41), v_rsp - 71 - 93);
loc_00AB86FB:
    v_r10 = 0;
    *(unsigned __int64 *)(v_rsp - 71 - 41) = 0;
loc_00AB8702:
    if ((*(unsigned __int64 *)(v_rsp - 71 - 33)) == 0) goto loc_00AB8327;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 87) + 32) + 140)) & (1)) == 0) goto loc_00AB8730;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 87) + 32), v_rsp - 71 - 81, *(unsigned __int64 *)(v_rsp - 71 - 41), (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)));
    goto loc_00AB8735;
loc_00AB8730:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 87) + 32), v_rsp - 71 - 81, *(unsigned __int64 *)(v_rsp - 71 - 41), (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)));
loc_00AB8735:
    v_r10 = 0;
    goto loc_00AB8323;
loc_00AB8741:
    goto loc_00AB8555;
loc_00AB874B:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 71 + 87) + 32), v_rsp - 71 - 81, *(unsigned __int64 *)(v_rsp - 71 - 41), (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)));
loc_00AB8750:
    v_r10 = 0;
loc_00AB8753:
    if ((*(unsigned __int64 *)(v_rsp - 71 - 41)) == 0) goto loc_00AB8776;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_r13 + 32) + 140)) & ((unsigned __int8)(v_rsi))) == 0) goto loc_00AB8771;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(v_r13 + 32), v_rsp - 71 - 73, *(unsigned __int64 *)(v_rsp - 71 - 41), (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)));
    goto loc_00AB8776;
loc_00AB8771:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_r13 + 32), v_rsp - 71 - 73, *(unsigned __int64 *)(v_rsp - 71 - 41), (unsigned int)(*(unsigned int *)(v_rsp - 71 + 95)));
loc_00AB8776:
    v_r14 = (unsigned __int8)(-(*(unsigned __int8 *)(v_rsp - 71 - 97)));
    a1 = (unsigned int)((*(unsigned __int64 *)(v_r13 + 32)) & ((unsigned int)((unsigned int)((unsigned int)(result)) + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 71 + 143)) = (unsigned int)(a1);
    v_rsp = (v_rsp) + (184);
    return (unsigned int)((unsigned int)((unsigned int)(0x8000001AULL)));
}
```

## 5. (Beta) C Style

```c
int64_t CmpFindSubKeyByNumberFromMergedView(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (184);
    local_r10 = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x35) = 0;
    Arg3 = (uint32_t)((Arg3) | (0xFFFFFFFFULL));
    *(uint32_t *)(local_rsp - 0x47 - 0x31) = 0;
    *(uint8_t *)(local_rsp - 0x47 - 0x61) = 0;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x77)) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x29) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x49) = Arg3;
    *(uint32_t *)(local_rsp - 0x47 - 0x45) = 0;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F)) = Arg3;
    result = 0;
    if (Arg2 == 0) { result = (uint32_t)(local_r10 + 1); }
    *(uint32_t *)(local_rsp - 0x47 - 0x51) = Arg3;
    *(uint32_t *)(local_rsp - 0x47 - 0x3D) = (uint32_t)(result);
    *(uint32_t *)(local_rsp - 0x47 - 0x4D) = 0;
    *(uint32_t *)(local_rsp - 0x47 - 0x39) = Arg3;
    *(uint32_t *)(local_rsp - 0x47 - 0x5D) = Arg3;
    *(uint8_t *)(local_rsp - 0x47 - 0x59) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x19) = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x11) = 0;
loc_00AB8323:
    *(uint64_t *)(local_rsp - 0x47 - 0x21) = 0;
loc_00AB8327:
    if (0 == 0) goto loc_00AB8335;
    if (0 >= ((uint32_t)((uint32_t)(Arg3)))) goto loc_00AB8741;
loc_00AB8335:
    local_rsi = 0;
    if (0 != 0) {
        Arg2 = *(uint64_t *)(local_rsp - 0x47 + 0x6F);
        Arg1 = 0;
        result = CmpDelayDerefKeyControlBlock(Arg1, Arg2, Arg3, (uint32_t)(Arg3));
        local_r10 = 0;
        local_rsi = 0;
        *(uint64_t *)(local_rsp - 0x47 - 0x19) = 0;
    }
    local_r15 = 0;
    if (0 != 0) {
        Arg2 = *(uint64_t *)(local_rsp - 0x47 + 0x6F);
        Arg1 = 0;
        result = CmpDelayDerefKeyControlBlock(Arg1, Arg2, Arg3, (uint32_t)(Arg3));
        local_r10 = 0;
        local_r15 = 0;
        *(uint64_t *)(local_rsp - 0x47 - 0x11) = 0;
    }
    if ((*(uint8_t *)(local_rsp - 0x47 - 0x59)) != 0) goto loc_00AB840E;
    if (((uint32_t)((uint32_t)(Arg3))) != -1) goto loc_00AB840E;
    result = -(*(uint64_t *)(local_rsp - 0x47 + 0x67));
    Arg3 = (Arg3) & (local_rsp - 71 - 25);
    v_stack_mB8 = Arg3;
    result = -(*(uint64_t *)(local_rsp - 0x47 + 0x67));
    Arg2 = (Arg2) & (*(uint64_t *)(local_rsp - 0x47 + 0x57));
    result = -(*(uint64_t *)(local_rsp - 0x47 + 0x67));
    v_stack_mC0 = *(uint64_t *)(local_rsp - 0x47 + 0x6F);
    v_stack_mC8 = *(uint64_t *)(local_rsp - 0x47 + 0x67);
    Arg1 = (Arg1) & (*(uint64_t *)(local_rsp - 0x47 + 0x4F));
    v_stack_mD0 = Arg2;
    v_stack_mD8 = Arg1;
    result = CmpFindSubKeyByNumberEx(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + 0x28)), (uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x35)), local_rsp - 71 - 57);
    local_r10 = 0;
    if (sign_flag) goto loc_00AB8559;
    result = (uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x59)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)))) == -1) { result = (uint32_t)(local_r10 + 1); }
    *(uint32_t *)(local_rsp - 0x47 - 0x59) = (uint32_t)(result);
    goto loc_00AB8414;
loc_00AB840E:
loc_00AB8414:
    if ((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x3D))) != 0) goto loc_00AB84B8;
    if (((uint32_t)((uint32_t)(Arg3))) != -1) goto loc_00AB84B8;
    result = -(*(uint64_t *)(local_rsp - 0x47 + 0x67));
    Arg3 = ((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x35))) & (local_rsp - 71 - 17);
    v_stack_mB8 = Arg3;
    result = -(*(uint64_t *)(local_rsp - 0x47 + 0x67));
    Arg2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + 0x28))) & (*(uint64_t *)(local_rsp - 0x47 + 0x4F));
    result = -(*(uint64_t *)(local_rsp - 0x47 + 0x67));
    v_stack_mC0 = *(uint64_t *)(local_rsp - 0x47 + 0x6F);
    v_stack_mC8 = *(uint64_t *)(local_rsp - 0x47 + 0x67);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + 0x20)) & (*(uint64_t *)(local_rsp - 0x47 + 0x57));
    v_stack_mD0 = Arg2;
    v_stack_mD8 = Arg1;
    result = CmpFindSubKeyByNumberEx(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x57) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x57) + 0x28)), (uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x31)), local_rsp - 71 - 93);
    local_r10 = 0;
    if (sign_flag) goto loc_00AB8623;
    result = (uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x3D)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x5D)))) == -1) { result = (uint32_t)(local_r10 + 1); }
    *(uint32_t *)(local_rsp - 0x47 - 0x3D) = (uint32_t)(result);
loc_00AB84B8:
    if ((*(uint8_t *)(local_rsp - 0x47 - 0x59)) == 0) goto loc_00AB84CE;
    if ((uint8_t)(result) != 0) goto loc_00AB8741;
    goto loc_00AB84D7;
loc_00AB84CE:
    local_r14 = ((uint8_t)(result) != 0) ? 1 : 0;
loc_00AB84D7:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x5D)))) == -1) goto loc_00AB8514;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x57) + 0x20) + 0x8C)) & ((uint8_t)(local_r10 + 1))) == 0) goto loc_00AB84FC;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x57) + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x5D)))), local_rsp - 71 - 81, local_rsp - 71 - 93);
    goto loc_00AB8501;
loc_00AB84FC:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x57) + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x5D)))), local_rsp - 71 - 81, local_rsp - 71 - 93);
loc_00AB8501:
    local_r10 = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x21) = result;
    if (result == 0) goto loc_00AB8551;
loc_00AB8514:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)))) == -1) goto loc_00AB85B4;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + 0x20) + 0x8C)) & ((uint8_t)(local_r10 + 1))) == 0) goto loc_00AB853D;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)))), local_rsp - 71 - 73, local_rsp - 71 - 93);
    goto loc_00AB8542;
loc_00AB853D:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x39)))), local_rsp - 71 - 73, local_rsp - 71 - 93);
loc_00AB8542:
    local_r10 = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x29) = result;
    if (result != 0) goto loc_00AB85B8;
loc_00AB8551:
loc_00AB8555:
loc_00AB8559:
loc_00AB855D:
    if (*(uint64_t *)(local_rsp - 0x47 - 0x19) != 0) {
        Arg2 = *(uint64_t *)(local_rsp - 0x47 + 0x6F);
        Arg1 = *(uint64_t *)(local_rsp - 0x47 - 0x19);
        result = CmpDelayDerefKeyControlBlock(Arg1, Arg2, result, local_rsp - 71 - 93);
        local_r10 = 0;
    }
    if (*(uint64_t *)(local_rsp - 0x47 - 0x11) != 0) {
        Arg2 = *(uint64_t *)(local_rsp - 0x47 + 0x6F);
        Arg1 = *(uint64_t *)(local_rsp - 0x47 - 0x11);
        result = CmpDelayDerefKeyControlBlock(Arg1, Arg2, result, local_rsp - 71 - 93);
        local_r10 = 0;
    }
    if ((*(uint64_t *)(local_rsp - 0x47 - 0x21)) == 0) goto loc_00AB8753;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x57) + 0x20) + 0x8C)) & (1)) == 0) goto loc_00AB874B;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x57) + 0x20), local_rsp - 71 - 81, result, local_rsp - 71 - 93);
    goto loc_00AB8750;
loc_00AB85B4:
loc_00AB85B8:
    if ((uint32_t)(*(uint8_t *)(local_rsp - 0x47 - 0x61)) == 0) goto loc_00AB8670;
    local_r14 = (uint32_t)((*(uint8_t *)(local_rsp - 0x47 - 0x61)) - (1));
    if (condition_is_equal) goto loc_00AB862C;
    if (((uint32_t)(local_r14)) != 1) goto loc_00AB86C7;
loc_00AB85DF:
    *(uint8_t *)(local_rsp - 0x47 - 0x61) = 1;
    result = 0 + 1;
    if ((*(uint8_t *)(local_rsp - 0x47 - 0x61)) == 0) { result = 0; }
    if (((uint32_t)(result)) != (*(uint32_t *)(local_rsp - 0x47 + 0x5F))) goto loc_00AB86B9;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x77)) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x57) + 0x20);
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F)) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x47 - 0x5D)));
    local_r15 = *(uint64_t *)(local_rsp - 0x47 - 0x11);
    if (*(uint64_t *)(local_rsp - 0x47 + 0x87) != 0) {
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x87)) = *(uint64_t *)(local_rsp - 0x47 - 0x11);
        local_r15 = 0;
    }
loc_00AB8623:
    goto loc_00AB855D;
loc_00AB862C:
loc_00AB8632:
    result = (uint32_t)((uint32_t)(result)) + 1;
    if ((*(uint8_t *)(local_rsp - 0x47 - 0x61)) == 0) { result = (uint32_t)((uint32_t)((uint32_t)(result))); }
    if (((uint32_t)(result)) != (*(uint32_t *)(local_rsp - 0x47 + 0x5F))) goto loc_00AB86A4;
loc_00AB8640:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x77)) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + 0x20);
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x7F)) = (uint32_t)(*(uint64_t *)(local_rsp - 0x47 + 0x4F));
    local_rsi = 1;
    if (*(uint64_t *)(local_rsp - 0x47 + 0x87) != 0) {
        *(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x87)) = 1;
        local_rsi = 0;
    }
    goto loc_00AB8555;
loc_00AB8670:
    result = CmpCompareKeysByName(*(uint64_t *)(local_rsp - 0x47 - 0x29), *(uint64_t *)(local_rsp - 0x47 - 0x21), *(uint64_t *)(local_rsp - 0x47 - 0x29), local_rsp - 71 - 93);
    local_r10 = 0;
    if (sign_flag) goto loc_00AB8632;
    if (condition_is_greater) goto loc_00AB85DF;
    result = (uint32_t)((uint32_t)(result)) + 1;
    if ((*(uint8_t *)(local_rsp - 0x47 - 0x61)) == 0) { result = (uint32_t)((uint32_t)((uint32_t)(result))); }
    if (((uint32_t)(result)) == (*(uint32_t *)(local_rsp - 0x47 + 0x5F))) goto loc_00AB8640;
loc_00AB86A4:
    local_r13 = (uint32_t)((*(uint64_t *)(local_rsp - 0x47 + 0x4F)) | (0xFFFFFFFFULL));
    *(uint8_t *)(local_rsp - 0x47 - 0x61) = (uint8_t)((uint8_t)(local_r10 + 1));
    *(uint32_t *)(local_rsp - 0x47 - 0x39) = (uint32_t)(local_r13);
    if ((uint8_t)((uint8_t)(local_r10 + 1)) == 0) goto loc_00AB86CD;
loc_00AB86B9:
    local_r12 = (uint32_t)(((uint8_t)(local_r10 + 1)) | (0xFFFFFFFFULL));
    *(uint32_t *)(local_rsp - 0x47 - 0x5D) = (uint32_t)(local_r12);
    goto loc_00AB86D1;
loc_00AB86C7:
    goto loc_00AB86D5;
loc_00AB86CD:
loc_00AB86D1:
loc_00AB86D5:
    if (*(uint64_t *)(local_rsp - 0x47 - 0x29) == 0) goto loc_00AB8702;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + 0x20) + 0x8C)) & ((uint8_t)(local_r10 + 1))) == 0) goto loc_00AB86F6;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + 0x20), local_rsp - 71 - 73, *(uint64_t *)(local_rsp - 0x47 - 0x29), local_rsp - 71 - 93);
    goto loc_00AB86FB;
loc_00AB86F6:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x4F) + 0x20), local_rsp - 71 - 73, *(uint64_t *)(local_rsp - 0x47 - 0x29), local_rsp - 71 - 93);
loc_00AB86FB:
    local_r10 = 0;
    *(uint64_t *)(local_rsp - 0x47 - 0x29) = 0;
loc_00AB8702:
    if ((*(uint64_t *)(local_rsp - 0x47 - 0x21)) == 0) goto loc_00AB8327;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x57) + 0x20) + 0x8C)) & (1)) == 0) goto loc_00AB8730;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x57) + 0x20), local_rsp - 71 - 81, *(uint64_t *)(local_rsp - 0x47 - 0x29), (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)));
    goto loc_00AB8735;
loc_00AB8730:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x57) + 0x20), local_rsp - 71 - 81, *(uint64_t *)(local_rsp - 0x47 - 0x29), (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)));
loc_00AB8735:
    local_r10 = 0;
    goto loc_00AB8323;
loc_00AB8741:
    goto loc_00AB8555;
loc_00AB874B:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x57) + 0x20), local_rsp - 71 - 81, *(uint64_t *)(local_rsp - 0x47 - 0x29), (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)));
loc_00AB8750:
    local_r10 = 0;
loc_00AB8753:
    if ((*(uint64_t *)(local_rsp - 0x47 - 0x29)) == 0) goto loc_00AB8776;
    if (((*(uint8_t *)(*(uint64_t *)(local_r13 + 0x20) + 0x8C)) & ((uint8_t)(local_rsi))) == 0) goto loc_00AB8771;
    result = HvpReleaseCellFlat(*(uint64_t *)(local_r13 + 0x20), local_rsp - 71 - 73, *(uint64_t *)(local_rsp - 0x47 - 0x29), (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)));
    goto loc_00AB8776;
loc_00AB8771:
    result = HvpReleaseCellPaged(*(uint64_t *)(local_r13 + 0x20), local_rsp - 71 - 73, *(uint64_t *)(local_rsp - 0x47 - 0x29), (uint32_t)(*(uint32_t *)(local_rsp - 0x47 + 0x5F)));
loc_00AB8776:
    local_r14 = (uint8_t)(-(*(uint8_t *)(local_rsp - 0x47 - 0x61)));
    Arg1 = (uint32_t)((*(uint64_t *)(local_r13 + 0x20)) & ((uint32_t)((uint32_t)((uint32_t)(result)) + 1)));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x47 + 0x8F)) = (uint32_t)(Arg1);
    local_rsp = (local_rsp) + (184);
    return (uint32_t)((uint32_t)((uint32_t)(0x8000001AULL)));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB8284&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
