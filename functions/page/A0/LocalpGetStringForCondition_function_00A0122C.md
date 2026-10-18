# LocalpGetStringForCondition

- RVA: `0x00A0122C`–`0x00A0175B` (길이 `1,327` bytes)
- VA: `0x0000000140A0122C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A7DDC`
- 디코드: `329`개 명령, `1,327/1,327` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00A012AD` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A01379` → [GetPrintableAttributeName](GetPrintableAttributeName_function_00A019D0.md) (function, `0x00A019D0`)
- `0x00A0141B` → [GetPrintableOperandValue](GetPrintableOperandValue_function_00A01764.md) (function, `0x00A01764`)
- `0x00A0149C` → [GetOperatorIndexByToken](GetOperatorIndexByToken_function_00A01BAC.md) (function, `0x00A01BAC`)
- `0x00A01520` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A0155D` → [EncloseSubCondition](EncloseSubCondition_function_00A01BD4.md) (function, `0x00A01BD4`)
- `0x00A015B5` → [SddlpAlloc](../92/SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x00A015EA` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (function, `0x00482D5C`)
- `0x00A015FA` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00A0160F` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00A01707` → [EncloseSubCondition](EncloseSubCondition_function_00A01BD4.md) (function, `0x00A01BD4`)

### Direct callers
- [LocalGetAceCondition](LocalGetAceCondition_function_00A010BC.md) at `0x00A01197`

### Static image references
- `0x00A0124B` → RVA `0x00E0A740` (`.data`; read)
- `0x00A012FC` → RVA `0x00002BB0` (`.rdata`; read)
- `0x00A015D0` → RVA `0x00014A80` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A012AD` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A01520` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A015EA` → [RtlStringCchPrintfW](../../text/48/RtlStringCchPrintfW_function_00482D5C.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **9**
  - `0x00A014D2` → [sub_00B32900 + 0x65](../B3/Unknown_function_00B32900.md) (`tail-transfer`)
  - `0x00A01571` → [sub_00B32900 + 0x17A](../B3/Unknown_function_00B32900.md) (`tail-transfer`)
  - `0x00A016BC` → [sub_00B32900 + 0x6](../B3/Unknown_function_00B32900.md) (`tail-transfer`)
  - `0x00A016C7` → [sub_00B32900](../B3/Unknown_function_00B32900.md) (`tail-transfer`)
  - `0x00A016CF` → [sub_00B32900 + 0x18](../B3/Unknown_function_00B32900.md) (`tail-transfer`)
  - `0x00A016E9` → [sub_00B32900 + 0x3E](../B3/Unknown_function_00B32900.md) (`tail-transfer`)
  - `0x00A01725` → [sub_00B32900 + 0x3E](../B3/Unknown_function_00B32900.md) (`tail-transfer`)
  - `0x00A0173E` → [sub_00B32900 + 0x163](../B3/Unknown_function_00B32900.md) (`tail-transfer`)
  - `0x00A0174C` → [sub_00B32900 + 0x17A](../B3/Unknown_function_00B32900.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A0122C  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00A01231  55                              push rbp
00A01232  56                              push rsi
00A01233  57                              push rdi
00A01234  41 54                           push r12
00A01236  41 55                           push r13
00A01238  41 56                           push r14
00A0123A  41 57                           push r15
00A0123C  48 8D AC 24 60 F8 FF FF         lea rbp, [rsp - 0x7a0]
00A01244  48 81 EC A0 08 00 00            sub rsp, 0x8a0
00A0124B  48 8B 05 EE 94 40 00            mov rax, qword ptr [rip + 0x4094ee]
00A01252  48 33 C4                        xor rax, rsp
00A01255  48 89 85 90 07 00 00            mov qword ptr [rbp + 0x790], rax
00A0125C  48 8B 85 00 08 00 00            mov rax, qword ptr [rbp + 0x800]
00A01263  49 8B F8                        mov rdi, r8
00A01266  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00A0126B  44 8B EA                        mov r13d, edx
00A0126E  48 8B 85 08 08 00 00            mov rax, qword ptr [rbp + 0x808]
00A01275  4C 8B F9                        mov r15, rcx
00A01278  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00A0127D  45 33 E4                        xor r12d, r12d
00A01280  48 8B 85 10 08 00 00            mov rax, qword ptr [rbp + 0x810]
00A01287  41 8B DC                        mov ebx, r12d
00A0128A  4C 89 45 80                     mov qword ptr [rbp - 0x80], r8
00A0128E  41 B8 00 08 00 00               mov r8d, 0x800
00A01294  89 54 24 58                     mov dword ptr [rsp + 0x58], edx
00A01298  33 D2                           xor edx, edx
00A0129A  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
00A0129F  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00A012A3  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00A012A8  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
00A012AD  E8 8E 59 CC FF                  call 0x1406c6c40
00A012B2  44 89 64 24 40                  mov dword ptr [rsp + 0x40], r12d
00A012B7  45 8B F4                        mov r14d, r12d
00A012BA  44 89 64 24 54                  mov dword ptr [rsp + 0x54], r12d
00A012BF  4D 85 FF                        test r15, r15
00A012C2  0F 84 AA 03 00 00               je 0x140a01672
00A012C8  48 85 FF                        test rdi, rdi
00A012CB  0F 84 A1 03 00 00               je 0x140a01672
00A012D1  45 85 ED                        test r13d, r13d
00A012D4  0F 84 98 03 00 00               je 0x140a01672
00A012DA  41 83 FD 06                     cmp r13d, 6
00A012DE  0F 82 6D 04 00 00               jb 0x140a01751
00A012E4  41 81 3F 61 72 74 78            cmp dword ptr [r15], 0x78747261
00A012EB  0F 85 60 04 00 00               jne 0x140a01751
00A012F1  41 8D 74 24 04                  lea esi, [r12 + 4]
00A012F6  41 BB FF FF FF FF               mov r11d, 0xffffffff
00A012FC  4C 8D 15 AD 18 60 FF            lea r10, [rip - 0x9fe753]
00A01303  89 74 24 50                     mov dword ptr [rsp + 0x50], esi
00A01307  41 B9 38 05 00 00               mov r9d, 0x538
00A0130D  41 3B F5                        cmp esi, r13d
00A01310  0F 83 2B 02 00 00               jae 0x140a01541
00A01316  49 81 FC FF 00 00 00            cmp r12, 0xff
00A0131D  0F 84 61 03 00 00               je 0x140a01684
00A01323  8B FE                           mov edi, esi
00A01325  49 03 FF                        add rdi, r15
00A01328  44 0F B6 3F                     movzx r15d, byte ptr [rdi]
00A0132C  41 8B CF                        mov ecx, r15d
00A0132F  41 81 FF 8A 00 00 00            cmp r15d, 0x8a
00A01336  76 61                           jbe 0x140a01399
00A01338  81 F9 F8 00 00 00               cmp ecx, 0xf8
00A0133E  0F 86 1D 01 00 00               jbe 0x140a01461
00A01344  81 E9 F9 00 00 00               sub ecx, 0xf9
00A0134A  74 13                           je 0x140a0135f
00A0134C  83 E9 01                        sub ecx, 1
00A0134F  74 0E                           je 0x140a0135f
00A01351  83 E9 01                        sub ecx, 1
00A01354  74 09                           je 0x140a0135f
00A01356  83 F9 01                        cmp ecx, 1
00A01359  0F 85 09 03 00 00               jne 0x140a01668
00A0135F  41 8B D5                        mov edx, r13d
00A01362  48 8D 44 24 54                  lea rax, [rsp + 0x54]
00A01367  2B D6                           sub edx, esi
00A01369  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A0136E  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
00A01373  45 8A C7                        mov r8b, r15b
00A01376  48 8B CF                        mov rcx, rdi
00A01379  E8 52 06 00 00                  call 0x140a019d0
00A0137E  33 FF                           xor edi, edi
00A01380  8B D8                           mov ebx, eax
00A01382  85 C0                           test eax, eax
00A01384  0F 85 AA 03 00 00               jne 0x140a01734
00A0138A  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00A0138F  4A 89 44 E5 90                  mov qword ptr [rbp + r12*8 - 0x70], rax
00A01394  E9 9D 00 00 00                  jmp 0x140a01436
00A01399  0F 84 E5 00 00 00               je 0x140a01484
00A0139F  81 F9 80 00 00 00               cmp ecx, 0x80
00A013A5  0F 87 F0 02 00 00               ja 0x140a0169b
00A013AB  0F 84 D3 00 00 00               je 0x140a01484
00A013B1  45 84 FF                        test r15b, r15b
00A013B4  0F 84 91 02 00 00               je 0x140a0164b
00A013BA  83 E9 01                        sub ecx, 1
00A013BD  74 22                           je 0x140a013e1
00A013BF  83 E9 01                        sub ecx, 1
00A013C2  74 1D                           je 0x140a013e1
00A013C4  83 E9 01                        sub ecx, 1
00A013C7  74 18                           je 0x140a013e1
00A013C9  83 E9 01                        sub ecx, 1
00A013CC  74 13                           je 0x140a013e1
00A013CE  83 E9 0C                        sub ecx, 0xc
00A013D1  74 0E                           je 0x140a013e1
00A013D3  83 E9 08                        sub ecx, 8
00A013D6  74 09                           je 0x140a013e1
00A013D8  83 E9 38                        sub ecx, 0x38
00A013DB  0F 85 B0 02 00 00               jne 0x140a01691
00A013E1  8A 85 18 08 00 00               mov al, byte ptr [rbp + 0x818]
00A013E7  4C 8D 4C 24 54                  lea r9, [rsp + 0x54]
00A013EC  88 44 24 38                     mov byte ptr [rsp + 0x38], al
00A013F0  4C 8D 44 24 48                  lea r8, [rsp + 0x48]
00A013F5  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00A013FA  41 8B D5                        mov edx, r13d
00A013FD  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A01402  2B D6                           sub edx, esi
00A01404  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00A01409  48 8B CF                        mov rcx, rdi
00A0140C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A01411  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00A01416  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A0141B  E8 44 03 00 00                  call 0x140a01764
00A01420  33 FF                           xor edi, edi
00A01422  8B D8                           mov ebx, eax
00A01424  85 C0                           test eax, eax
00A01426  0F 85 08 03 00 00               jne 0x140a01734
00A0142C  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A01431  4A 89 4C E5 90                  mov qword ptr [rbp + r12*8 - 0x70], rcx
00A01436  41 FF C6                        inc r14d
00A01439  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00A0143E  49 FF C4                        inc r12
00A01441  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
00A01446  4C 8D 15 63 17 60 FF            lea r10, [rip - 0x9fe89d]
00A0144D  41 BB FF FF FF FF               mov r11d, 0xffffffff
00A01453  03 74 24 54                     add esi, dword ptr [rsp + 0x54]
00A01457  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
00A0145C  E9 A2 FE FF FF                  jmp 0x140a01303
00A01461  0F 84 F8 FE FF FF               je 0x140a0135f
00A01467  81 F9 91 00 00 00               cmp ecx, 0x91
00A0146D  0F 86 4E 02 00 00               jbe 0x140a016c1
00A01473  81 E9 92 00 00 00               sub ecx, 0x92
00A01479  74 09                           je 0x140a01484
00A0147B  83 E9 01                        sub ecx, 1
00A0147E  0F 85 48 02 00 00               jne 0x140a016cc
00A01484  41 8D 47 60                     lea eax, [r15 + 0x60]
00A01488  3C 01                           cmp al, 1
00A0148A  0F 86 5E 02 00 00               jbe 0x140a016ee
00A01490  41 80 FF A2                     cmp r15b, 0xa2
00A01494  0F 84 3A 02 00 00               je 0x140a016d4
00A0149A  8A 0F                           mov cl, byte ptr [rdi]
00A0149C  E8 0B 07 00 00                  call 0x140a01bac
00A014A1  45 33 C0                        xor r8d, r8d
00A014A4  85 C0                           test eax, eax
00A014A6  0F 88 D0 01 00 00               js 0x140a0167c
00A014AC  48 98                           cdqe
00A014AE  4C 8D 2C 40                     lea r13, [rax + rax*2]
00A014B2  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A014B6  4B 8B 0C EA                     mov rcx, qword ptr [r10 + r13*8]
00A014BA  48 FF C0                        inc rax
00A014BD  66 44 39 04 41                  cmp word ptr [rcx + rax*2], r8w
00A014C2  75 F6                           jne 0x140a014ba
00A014C4  8D 0C 00                        lea ecx, [rax + rax]
00A014C7  33 C0                           xor eax, eax
00A014C9  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
00A014CD  43 38 44 EA 10                  cmp byte ptr [r10 + r13*8 + 0x10], al
00A014D2  0F 85 8D 14 13 00               jne 0x140b32965
00A014D8  49 83 FC 02                     cmp r12, 2
00A014DC  0F 8C 9A 01 00 00               jl 0x140a0167c
00A014E2  4E 8B 7C E5 88                  mov r15, qword ptr [rbp + r12*8 - 0x78]
00A014E7  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A014EB  48 FF C0                        inc rax
00A014EE  66 45 39 04 47                  cmp word ptr [r15 + rax*2], r8w
00A014F3  75 F6                           jne 0x140a014eb
00A014F5  8B C0                           mov eax, eax
00A014F7  48 03 C0                        add rax, rax
00A014FA  49 3B C3                        cmp rax, r11
00A014FD  76 77                           jbe 0x140a01576
00A014FF  BB 16 02 00 00                  mov ebx, 0x216
00A01504  BE 38 05 00 00                  mov esi, 0x538
00A01509  8B C3                           mov eax, ebx
00A0150B  45 85 F6                        test r14d, r14d
00A0150E  0F 85 2F 02 00 00               jne 0x140a01743
00A01514  8B C3                           mov eax, ebx
00A01516  48 8B 8D 90 07 00 00            mov rcx, qword ptr [rbp + 0x790]
00A0151D  48 33 CC                        xor rcx, rsp
00A01520  E8 1B B1 CA FF                  call 0x1406ac640
00A01525  48 8B 9C 24 F8 08 00 00         mov rbx, qword ptr [rsp + 0x8f8]
00A0152D  48 81 C4 A0 08 00 00            add rsp, 0x8a0
00A01534  41 5F                           pop r15
00A01536  41 5E                           pop r14
00A01538  41 5D                           pop r13
00A0153A  41 5C                           pop r12
00A0153C  5F                              pop rdi
00A0153D  5E                              pop rsi
00A0153E  5D                              pop rbp
00A0153F  C3                              ret
00A01540  CC                              int3
00A01541  41 83 FE 01                     cmp r14d, 1
00A01545  0F 85 3E 01 00 00               jne 0x140a01689
00A0154B  48 8B 7D 80                     mov rdi, qword ptr [rbp - 0x80]
00A0154F  49 63 C6                        movsxd rax, r14d
00A01552  48 8B 4C C5 88                  mov rcx, qword ptr [rbp + rax*8 - 0x78]
00A01557  48 89 0F                        mov qword ptr [rdi], rcx
00A0155A  48 8B CF                        mov rcx, rdi
00A0155D  E8 72 06 00 00                  call 0x140a01bd4
00A01562  8B D8                           mov ebx, eax
00A01564  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00A01568  33 C0                           xor eax, eax
00A0156A  85 DB                           test ebx, ebx
00A0156C  74 A6                           je 0x140a01514
00A0156E  48 89 07                        mov qword ptr [rdi], rax
00A01571  E9 04 15 13 00                  jmp 0x140b32a7a
00A01576  8D 14 01                        lea edx, [rcx + rax]
00A01579  3B D1                           cmp edx, ecx
00A0157B  72 82                           jb 0x140a014ff
00A0157D  4A 8B 74 E5 80                  mov rsi, qword ptr [rbp + r12*8 - 0x80]
00A01582  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A01586  48 FF C0                        inc rax
00A01589  66 44 39 04 46                  cmp word ptr [rsi + rax*2], r8w
00A0158E  75 F6                           jne 0x140a01586
00A01590  8B C0                           mov eax, eax
00A01592  48 03 C0                        add rax, rax
00A01595  49 3B C3                        cmp rax, r11
00A01598  0F 87 61 FF FF FF               ja 0x140a014ff
00A0159E  8D 0C 02                        lea ecx, [rdx + rax]
00A015A1  3B CA                           cmp ecx, edx
00A015A3  0F 82 56 FF FF FF               jb 0x140a014ff
00A015A9  44 8D 71 0A                     lea r14d, [rcx + 0xa]
00A015AD  41 8B CE                        mov ecx, r14d
00A015B0  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
00A015B5  E8 CE 49 F2 FF                  call 0x140925f88
00A015BA  48 8B F8                        mov rdi, rax
00A015BD  48 85 C0                        test rax, rax
00A015C0  74 7A                           je 0x140a0163c
00A015C2  48 8D 05 E7 15 60 FF            lea rax, [rip - 0x9fea19]
00A015C9  41 8B D6                        mov edx, r14d
00A015CC  4A 8B 04 E8                     mov rax, qword ptr [rax + r13*8]
00A015D0  4C 8D 05 A9 34 61 FF            lea r8, [rip - 0x9ecb57]
00A015D7  48 D1 EA                        shr rdx, 1
00A015DA  4C 8B CE                        mov r9, rsi
00A015DD  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
00A015E2  48 8B CF                        mov rcx, rdi
00A015E5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A015EA  E8 6D 17 A8 FF                  call 0x140482d5c
00A015EF  85 C0                           test eax, eax
00A015F1  0F 88 33 01 00 00               js 0x140a0172a
00A015F7  49 8B CF                        mov rcx, r15
00A015FA  E8 05 0E ED FF                  call 0x1408d2404
00A015FF  49 83 CE FF                     or r14, 0xffffffffffffffff
00A01603  4E 8D 7C E5 80                  lea r15, [rbp + r12*8 - 0x80]
00A01608  FF 4C 24 40                     dec dword ptr [rsp + 0x40]
00A0160C  48 8B CE                        mov rcx, rsi
00A0160F  E8 F0 0D ED FF                  call 0x1408d2404
00A01614  8B 74 24 50                     mov esi, dword ptr [rsp + 0x50]
00A01618  33 C0                           xor eax, eax
00A0161A  44 8B 6C 24 58                  mov r13d, dword ptr [rsp + 0x58]
00A0161F  4D 03 E6                        add r12, r14
00A01622  44 8B 74 24 40                  mov r14d, dword ptr [rsp + 0x40]
00A01627  49 89 3F                        mov qword ptr [r15], rdi
00A0162A  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A0162F  C7 44 24 54 01 00 00 00         mov dword ptr [rsp + 0x54], 1
00A01637  E9 0A FE FF FF                  jmp 0x140a01446
00A0163C  BB 08 00 00 00                  mov ebx, 8
00A01641  44 8B 74 24 40                  mov r14d, dword ptr [rsp + 0x40]
00A01646  E9 EE 00 00 00                  jmp 0x140a01739
00A0164B  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00A01650  33 FF                           xor edi, edi
00A01652  FF C6                           inc esi
00A01654  41 3B F5                        cmp esi, r13d
00A01657  73 09                           jae 0x140a01662
00A01659  40 38 3C 0E                     cmp byte ptr [rsi + rcx], dil
00A0165D  74 F3                           je 0x140a01652
00A0165F  41 3B F5                        cmp esi, r13d
00A01662  0F 84 EB FD FF FF               je 0x140a01453
00A01668  41 8B D9                        mov ebx, r9d
00A0166B  8B F3                           mov esi, ebx
00A0166D  E9 97 FE FF FF                  jmp 0x140a01509
00A01672  B8 57 00 00 00                  mov eax, 0x57
00A01677  E9 9A FE FF FF                  jmp 0x140a01516
00A0167C  41 8B D9                        mov ebx, r9d
00A0167F  E9 80 FE FF FF                  jmp 0x140a01504
00A01684  BB E9 03 00 00                  mov ebx, 0x3e9
00A01689  41 8B F1                        mov esi, r9d
00A0168C  E9 78 FE FF FF                  jmp 0x140a01509
00A01691  83 F9 01                        cmp ecx, 1
00A01694  75 D2                           jne 0x140a01668
00A01696  E9 46 FD FF FF                  jmp 0x140a013e1
00A0169B  81 E9 81 00 00 00               sub ecx, 0x81
00A016A1  0F 84 DD FD FF FF               je 0x140a01484
00A016A7  83 E9 01                        sub ecx, 1
00A016AA  0F 84 D4 FD FF FF               je 0x140a01484
00A016B0  83 E9 01                        sub ecx, 1
00A016B3  0F 84 CB FD FF FF               je 0x140a01484
00A016B9  83 E9 01                        sub ecx, 1
00A016BC  E9 45 12 13 00                  jmp 0x140b32906
00A016C1  0F 84 BD FD FF FF               je 0x140a01484
00A016C7  E9 34 12 13 00                  jmp 0x140b32900
00A016CC  83 E9 0D                        sub ecx, 0xd
00A016CF  E9 44 12 13 00                  jmp 0x140b32918
00A016D4  49 83 FC 01                     cmp r12, 1
00A016D8  7C 8E                           jl 0x140a01668
00A016DA  41 8D 46 FF                     lea eax, [r14 - 1]
00A016DE  48 63 C8                        movsxd rcx, eax
00A016E1  48 8D 45 90                     lea rax, [rbp - 0x70]
00A016E5  48 8D 0C C8                     lea rcx, [rax + rcx*8]
00A016E9  E9 50 12 13 00                  jmp 0x140b3293e
00A016EE  49 83 FC 02                     cmp r12, 2
00A016F2  0F 8C 70 FF FF FF               jl 0x140a01668
00A016F8  41 8D 46 FF                     lea eax, [r14 - 1]
00A016FC  48 63 C8                        movsxd rcx, eax
00A016FF  48 8D 45 90                     lea rax, [rbp - 0x70]
00A01703  48 8D 0C C8                     lea rcx, [rax + rcx*8]
00A01707  E8 C8 04 00 00                  call 0x140a01bd4
00A0170C  8B D8                           mov ebx, eax
00A0170E  85 C0                           test eax, eax
00A01710  0F 85 EE FD FF FF               jne 0x140a01504
00A01716  41 8D 46 FE                     lea eax, [r14 - 2]
00A0171A  48 63 D0                        movsxd rdx, eax
00A0171D  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00A01721  48 8D 0C D1                     lea rcx, [rcx + rdx*8]
00A01725  E9 14 12 13 00                  jmp 0x140b3293e
00A0172A  BB 32 00 00 00                  mov ebx, 0x32
00A0172F  E9 0D FF FF FF                  jmp 0x140a01641
00A01734  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
00A01739  BE 38 05 00 00                  mov esi, 0x538
00A0173E  E9 20 13 13 00                  jmp 0x140b32a63
00A01743  85 C0                           test eax, eax
00A01745  0F 44 DE                        cmove ebx, esi
00A01748  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00A0174C  E9 29 13 13 00                  jmp 0x140b32a7a
00A01751  B8 25 03 00 00                  mov eax, 0x325
00A01756  E9 BB FD FF FF                  jmp 0x140a01516
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LocalpGetStringForCondition(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, unsigned __int8 a8)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m7D8;
    unsigned __int64 v_stack_m848;
    unsigned __int64 v_stack_m858;
    unsigned __int64 v_stack_m860;
    unsigned __int64 v_stack_m868;
    unsigned __int64 v_stack_m870;
    unsigned __int64 v_stack_m878;
    unsigned int v_stack_m880;
    unsigned int v_stack_m884;
    unsigned int v_stack_m888;
    unsigned __int64 v_stack_m890;
    unsigned int v_stack_m898;
    unsigned __int8 v_stack_m8A0;
    unsigned __int64 v_stack_m8A8;
    unsigned __int64 v_stack_m8B0;
    unsigned __int64 v_stack_m8B8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p40;
    unsigned int v_stack_p48;
    unsigned int v_stack_p50;
    unsigned int v_stack_p54;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p60;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (0x8A0ULL);
    result = (*(unsigned __int64 *)(v_rip + 4232430)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m860 = a5;
    v_stack_m868 = a6;
    v_r12 = 0;
    v_stack_m858 = a3;
    v_stack_m880 = a2;
    a2 = 0;
    v_stack_m878 = a1;
    v_stack_m870 = a7;
    v_stack_m890 = 0;
    result = memset(v_stack_m848, a2, (unsigned int)(0x800ULL), a4);
    v_stack_m898 = 0;
    v_stack_m884 = 0;
    if (a1 == 0) goto loc_00A01672;
    if (a3 == 0) goto loc_00A01672;
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_00A01672;
    if (((unsigned int)((unsigned int)(a2))) < 6) goto loc_00A01751;
    if ((*(unsigned int *)(a1)) != 0x78747261ULL) goto loc_00A01751;
loc_00A01303:
    v_stack_m888 = (unsigned int)(v_r12 + 4);
    if (((unsigned int)(v_r12 + 4)) >= ((unsigned int)((unsigned int)(a2)))) goto loc_00A01541;
    if (0 == 255) goto loc_00A01684;
    v_rdi = ((unsigned int)((unsigned int)(v_r12 + 4))) + (a1);
    if (((unsigned int)(*(unsigned __int8 *)(v_rdi))) <= 138) goto loc_00A01399;
    if (((unsigned int)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rdi))))) <= 248) goto loc_00A01461;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_rdi)))) - (249));
    if (condition_is_equal) goto loc_00A0135F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A0135F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A0135F;
    if (((unsigned int)(a1)) != 1) goto loc_00A01668;
loc_00A0135F:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - ((unsigned int)(v_r12 + 4)));
    v_stack_m8B8 = v_stack_m884;
    result = GetPrintableAttributeName(v_rdi, a2, (unsigned __int8)(*(unsigned __int8 *)(v_rdi)), v_stack_m890);
    v_rdi = 0;
    if ((unsigned int)(result) != 0) goto loc_00A01734;
    *(unsigned __int64 *)(v_stack_m7D8 + v_r12 * 8 - 112) = v_stack_m890;
    goto loc_00A01436;
loc_00A01399:
    if ((unsigned int)(result) == 0) goto loc_00A01484;
    if (0 > 128) goto loc_00A0169B;
    if (0 == 128) goto loc_00A01484;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rdi)) == 0) goto loc_00A0164B;
    a1 = (unsigned int)((v_rdi) - (1));
    if (condition_is_equal) goto loc_00A013E1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A013E1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A013E1;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A013E1;
    a1 = (unsigned int)((a1) - (12));
    if (condition_is_equal) goto loc_00A013E1;
    a1 = (unsigned int)((a1) - (8));
    if (condition_is_equal) goto loc_00A013E1;
    a1 = (unsigned int)((a1) - (56));
    if (condition_is_not_equal) goto loc_00A01691;
loc_00A013E1:
    v_stack_m8A0 = a8;
    v_stack_m8A8 = v_stack_m870;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) - ((unsigned int)(v_r12 + 4)));
    v_stack_m8B0 = v_stack_m868;
    v_stack_m8B8 = v_stack_m860;
    result = GetPrintableOperandValue(0, a2, v_stack_m890, v_stack_m884);
    v_rdi = 0;
    if ((unsigned int)(result) != 0) goto loc_00A01734;
    *(unsigned __int64 *)(v_stack_m7D8 + v_r12 * 8 - 112) = v_stack_m890;
loc_00A01436:
    v_r14 = (unsigned int)((0) + 1);
    v_stack_m890 = 0;
    v_r12 = (v_r12) + 1;
    v_stack_m898 = (unsigned int)(v_r14);
loc_00A01446:
loc_00A01453:
    v_rsi = (unsigned int)((v_r12 + 4) + (v_stack_m884));
    goto loc_00A01303;
loc_00A01461:
    if (condition_is_equal) goto loc_00A0135F;
    if (((unsigned int)(v_stack_m890)) <= 145) goto loc_00A016C1;
    a1 = (unsigned int)((v_stack_m890) - (146));
    if (condition_is_equal) goto loc_00A01484;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_not_equal) goto loc_00A016CC;
loc_00A01484:
    if (((unsigned __int8)(v_stack_m878 + 96)) <= 1) goto loc_00A016EE;
    if (((unsigned __int8)(v_stack_m878)) == 162) goto loc_00A016D4;
    result = GetOperatorIndexByToken(*(unsigned __int8 *)(v_rdi), a2, v_stack_m890, v_stack_m884);
    a3 = 0;
    if (sign_flag) goto loc_00A0167C;
    result = (result) | (-1);
loc_00A014BA:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip - 10479773 + result + result * 2 * 8) + result * 2)) != 0) goto loc_00A014BA;
    result = 0;
    v_stack_m890 = (unsigned int)(result + result * 1);
    if (v_r12 < 2) goto loc_00A0167C;
    result = (result) | (-1);
loc_00A014EB:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m7D8 + v_r12 * 8 - 120) + result * 2)) != 0) goto loc_00A014EB;
    result = ((unsigned int)((unsigned int)(result))) + ((unsigned int)((unsigned int)(result)));
    if (result <= ((unsigned int)(0xFFFFFFFFULL))) goto loc_00A01576;
loc_00A014FF:
loc_00A01504:
loc_00A01509:
    if ((unsigned int)(v_r14) != 0) goto loc_00A01743;
loc_00A01514:
loc_00A01516:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, v_stack_m884);
    v_rsp = (v_rsp) + (0x8A0ULL);
    return result;
loc_00A01541:
    if (((unsigned int)(v_r14)) != 1) goto loc_00A01689;
    *(unsigned __int64 *)(v_stack_m858) = *(unsigned __int64 *)(v_stack_m7D8 + (int)((unsigned int)(v_r14)) * 8 - 120);
    result = EncloseSubCondition(v_stack_m858, a2, a3, v_stack_m884);
    v_stack_p50 = (unsigned int)(result);
    result = 0;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_00A01514;
    *(unsigned __int64 *)(v_stack_m858) = 0;
loc_00A01576:
    if (((unsigned int)(v_stack_m858 + result * 1)) < ((unsigned int)(v_stack_m858))) goto loc_00A014FF;
    result = (result) | (-1);
loc_00A01586:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m7D8 + v_r12 * 8 - 128) + result * 2)) != 0) goto loc_00A01586;
    result = ((unsigned int)((unsigned int)(result))) + ((unsigned int)((unsigned int)(result)));
    if (result > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00A014FF;
    if (((unsigned int)(v_stack_m858 + result * 1 + result * 1)) < ((unsigned int)(v_stack_m858 + result * 1))) goto loc_00A014FF;
    v_stack_p48 = (unsigned int)(v_stack_m858 + result * 1 + result * 1 + 10);
    result = SddlpAlloc((unsigned int)((unsigned int)(v_stack_m858 + result * 1 + result * 1 + 10)), v_stack_m858 + result * 1, a3, v_stack_m884);
    if (result == 0) goto loc_00A0163C;
    a2 = ((unsigned int)((unsigned int)(v_stack_m858 + result * 1 + result * 1 + 10))) >> (1);
    v_stack_p28 = *(unsigned __int64 *)(v_stack_m7D8 + v_r12 * 8 - 120);
    v_stack_p20 = *(unsigned __int64 *)(v_rip - 10480153 + result + result * 2 * 8);
    result = RtlStringCchPrintfW(result, a2, v_rip - 10406743, *(unsigned __int64 *)(v_stack_m7D8 + v_r12 * 8 - 128));
    if (sign_flag) goto loc_00A0172A;
    result = PdcCloseEvent(*(unsigned __int64 *)(v_stack_m7D8 + v_r12 * 8 - 120), a2, v_rip - 10406743, *(unsigned __int64 *)(v_stack_m7D8 + v_r12 * 8 - 128));
    v_r14 = (v_stack_m858 + result * 1 + result * 1 + 10) | (-1);
    result = PdcCloseEvent(*(unsigned __int64 *)(v_stack_m7D8 + v_r12 * 8 - 128), a2, v_rip - 10406743, *(unsigned __int64 *)(v_stack_m7D8 + v_r12 * 8 - 128));
    result = 0;
    v_r12 = (v_r12) + (v_r14);
    *(unsigned __int64 *)(v_stack_m7D8 + v_r12 * 8 - 128) = 0;
    v_stack_p48 = 0;
    v_stack_p54 = 1;
    goto loc_00A01446;
loc_00A0163C:
loc_00A01641:
    goto loc_00A01739;
loc_00A0164B:
    v_rdi = 0;
loc_00A01652:
    v_rsi = (unsigned int)(((unsigned int)(v_stack_p50)) + 1);
    if (((unsigned int)(v_rsi)) >= ((unsigned int)((unsigned int)(v_stack_p58)))) goto loc_00A01662;
    if ((*(unsigned __int8 *)(v_rsi + v_stack_p60 * 1)) == 0) goto loc_00A01652;
loc_00A01662:
    if (((unsigned int)(v_rsi)) == ((unsigned int)((unsigned int)(v_stack_p58)))) goto loc_00A01453;
loc_00A01668:
    goto loc_00A01509;
loc_00A01672:
    goto loc_00A01516;
loc_00A0167C:
    goto loc_00A01504;
loc_00A01684:
loc_00A01689:
    goto loc_00A01509;
loc_00A01691:
    if (((unsigned int)(v_stack_p60)) != 1) goto loc_00A01668;
    goto loc_00A013E1;
loc_00A0169B:
    a1 = (unsigned int)((v_stack_p60) - (129));
    if (condition_is_equal) goto loc_00A01484;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A01484;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00A01484;
    a1 = (unsigned int)((a1) - (1));
loc_00A016C1:
    if (condition_is_equal) goto loc_00A01484;
loc_00A016CC:
    a1 = (unsigned int)((a1) - (13));
loc_00A016D4:
    if (v_r12 < 1) goto loc_00A01668;
loc_00A016EE:
    if (v_r12 < 2) goto loc_00A01668;
    result = EncloseSubCondition(v_stack_m848 + (int)((unsigned int)((unsigned int)(v_stack_p40) - 1)) * 8, a2, v_rip - 10406743, *(unsigned __int64 *)(v_stack_m7D8 + v_r12 * 8 - 128));
    if ((unsigned int)(result) != 0) goto loc_00A01504;
loc_00A0172A:
    goto loc_00A01641;
loc_00A01734:
loc_00A01739:
loc_00A01743:
    v_rbx = 50;
    if ((unsigned int)((unsigned int)(v_stack_p40) - 2) == 0) { v_rbx = (unsigned int)((unsigned int)(0x538ULL)); }
    v_stack_p50 = (unsigned int)(v_rbx);
loc_00A01751:
    goto loc_00A01516;
}
```

## 5. (Beta) C Style

```c
int64_t LocalpGetStringForCondition(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, uint8_t Arg8)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m7D8;
    uint64_t v_stack_m848;
    uint64_t v_stack_m858;
    uint64_t v_stack_m860;
    uint64_t v_stack_m868;
    uint64_t v_stack_m870;
    uint64_t v_stack_m878;
    uint32_t v_stack_m880;
    uint32_t v_stack_m884;
    uint32_t v_stack_m888;
    uint64_t v_stack_m890;
    uint32_t v_stack_m898;
    uint8_t v_stack_m8A0;
    uint64_t v_stack_m8A8;
    uint64_t v_stack_m8B0;
    uint64_t v_stack_m8B8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p40;
    uint32_t v_stack_p48;
    uint32_t v_stack_p50;
    uint32_t v_stack_p54;
    uint32_t v_stack_p58;
    uint64_t v_stack_p60;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (0x8A0ULL);
    result = (*(uint64_t *)(v_rip + 0x4094EE)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m860 = Arg5;
    v_stack_m868 = Arg6;
    local_r12 = 0;
    v_stack_m858 = Arg3;
    v_stack_m880 = Arg2;
    Arg2 = 0;
    v_stack_m878 = Arg1;
    v_stack_m870 = Arg7;
    v_stack_m890 = 0;
    result = memset(v_stack_m848, Arg2, (uint32_t)(0x800ULL), Arg4);
    v_stack_m898 = 0;
    v_stack_m884 = 0;
    if (Arg1 == 0) goto loc_00A01672;
    if (Arg3 == 0) goto loc_00A01672;
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_00A01672;
    if (((uint32_t)((uint32_t)(Arg2))) < 6) goto loc_00A01751;
    if ((*(uint32_t *)(Arg1)) != 0x78747261ULL) goto loc_00A01751;
loc_00A01303:
    v_stack_m888 = (uint32_t)(local_r12 + 4);
    if (((uint32_t)(local_r12 + 4)) >= ((uint32_t)((uint32_t)(Arg2)))) goto loc_00A01541;
    if (0 == 255) goto loc_00A01684;
    local_rdi = ((uint32_t)((uint32_t)(local_r12 + 4))) + (Arg1);
    if (((uint32_t)(*(uint8_t *)(local_rdi))) <= 138) goto loc_00A01399;
    if (((uint32_t)((uint32_t)((uint32_t)(*(uint8_t *)(local_rdi))))) <= 248) goto loc_00A01461;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(local_rdi)))) - (249));
    if (condition_is_equal) goto loc_00A0135F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A0135F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A0135F;
    if (((uint32_t)(Arg1)) != 1) goto loc_00A01668;
loc_00A0135F:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - ((uint32_t)(local_r12 + 4)));
    v_stack_m8B8 = v_stack_m884;
    result = GetPrintableAttributeName(local_rdi, Arg2, (uint8_t)(*(uint8_t *)(local_rdi)), v_stack_m890);
    local_rdi = 0;
    if ((uint32_t)(result) != 0) goto loc_00A01734;
    *(uint64_t *)(v_stack_m7D8 + local_r12 * 8 - 0x70) = v_stack_m890;
    goto loc_00A01436;
loc_00A01399:
    if ((uint32_t)(result) == 0) goto loc_00A01484;
    if (0 > 128) goto loc_00A0169B;
    if (0 == 128) goto loc_00A01484;
    if ((uint8_t)(*(uint8_t *)(local_rdi)) == 0) goto loc_00A0164B;
    Arg1 = (uint32_t)((local_rdi) - (1));
    if (condition_is_equal) goto loc_00A013E1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A013E1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A013E1;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A013E1;
    Arg1 = (uint32_t)((Arg1) - (12));
    if (condition_is_equal) goto loc_00A013E1;
    Arg1 = (uint32_t)((Arg1) - (8));
    if (condition_is_equal) goto loc_00A013E1;
    Arg1 = (uint32_t)((Arg1) - (56));
    if (condition_is_not_equal) goto loc_00A01691;
loc_00A013E1:
    v_stack_m8A0 = Arg8;
    v_stack_m8A8 = v_stack_m870;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) - ((uint32_t)(local_r12 + 4)));
    v_stack_m8B0 = v_stack_m868;
    v_stack_m8B8 = v_stack_m860;
    result = GetPrintableOperandValue(0, Arg2, v_stack_m890, v_stack_m884);
    local_rdi = 0;
    if ((uint32_t)(result) != 0) goto loc_00A01734;
    *(uint64_t *)(v_stack_m7D8 + local_r12 * 8 - 0x70) = v_stack_m890;
loc_00A01436:
    local_r14 = (uint32_t)((0) + 1);
    v_stack_m890 = 0;
    local_r12 = (local_r12) + 1;
    v_stack_m898 = (uint32_t)(local_r14);
loc_00A01446:
loc_00A01453:
    local_rsi = (uint32_t)((local_r12 + 4) + (v_stack_m884));
    goto loc_00A01303;
loc_00A01461:
    if (condition_is_equal) goto loc_00A0135F;
    if (((uint32_t)(v_stack_m890)) <= 145) goto loc_00A016C1;
    Arg1 = (uint32_t)((v_stack_m890) - (146));
    if (condition_is_equal) goto loc_00A01484;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_not_equal) goto loc_00A016CC;
loc_00A01484:
    if (((uint8_t)(v_stack_m878 + 96)) <= 1) goto loc_00A016EE;
    if (((uint8_t)(v_stack_m878)) == 162) goto loc_00A016D4;
    result = GetOperatorIndexByToken(*(uint8_t *)(local_rdi), Arg2, v_stack_m890, v_stack_m884);
    Arg3 = 0;
    if (sign_flag) goto loc_00A0167C;
    result = (result) | (-1);
loc_00A014BA:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_rip - 0x9FE89D + result + result * 2 * 8) + result * 2)) != 0) goto loc_00A014BA;
    result = 0;
    v_stack_m890 = (uint32_t)(result + result * 1);
    if (local_r12 < 2) goto loc_00A0167C;
    result = (result) | (-1);
loc_00A014EB:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m7D8 + local_r12 * 8 - 0x78) + result * 2)) != 0) goto loc_00A014EB;
    result = ((uint32_t)((uint32_t)(result))) + ((uint32_t)((uint32_t)(result)));
    if (result <= ((uint32_t)(0xFFFFFFFFULL))) goto loc_00A01576;
loc_00A014FF:
loc_00A01504:
loc_00A01509:
    if ((uint32_t)(local_r14) != 0) goto loc_00A01743;
loc_00A01514:
loc_00A01516:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, v_stack_m884);
    local_rsp = (local_rsp) + (0x8A0ULL);
    return result;
loc_00A01541:
    if (((uint32_t)(local_r14)) != 1) goto loc_00A01689;
    *(uint64_t *)(v_stack_m858) = *(uint64_t *)(v_stack_m7D8 + (int32_t)((uint32_t)(local_r14)) * 8 - 0x78);
    result = EncloseSubCondition(v_stack_m858, Arg2, Arg3, v_stack_m884);
    v_stack_p50 = (uint32_t)(result);
    result = 0;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_00A01514;
    *(uint64_t *)(v_stack_m858) = 0;
loc_00A01576:
    if (((uint32_t)(v_stack_m858 + result * 1)) < ((uint32_t)(v_stack_m858))) goto loc_00A014FF;
    result = (result) | (-1);
loc_00A01586:
    result = (result) + 1;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m7D8 + local_r12 * 8 - 0x80) + result * 2)) != 0) goto loc_00A01586;
    result = ((uint32_t)((uint32_t)(result))) + ((uint32_t)((uint32_t)(result)));
    if (result > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00A014FF;
    if (((uint32_t)(v_stack_m858 + result * 1 + result * 1)) < ((uint32_t)(v_stack_m858 + result * 1))) goto loc_00A014FF;
    v_stack_p48 = (uint32_t)(v_stack_m858 + result * 1 + result * 1 + 10);
    result = SddlpAlloc((uint32_t)((uint32_t)(v_stack_m858 + result * 1 + result * 1 + 10)), v_stack_m858 + result * 1, Arg3, v_stack_m884);
    if (result == 0) goto loc_00A0163C;
    Arg2 = ((uint32_t)((uint32_t)(v_stack_m858 + result * 1 + result * 1 + 10))) >> (1);
    v_stack_p28 = *(uint64_t *)(v_stack_m7D8 + local_r12 * 8 - 0x78);
    v_stack_p20 = *(uint64_t *)(v_rip - 0x9FEA19 + result + result * 2 * 8);
    result = RtlStringCchPrintfW(result, Arg2, v_rip - 10406743, *(uint64_t *)(v_stack_m7D8 + local_r12 * 8 - 0x80));
    if (sign_flag) goto loc_00A0172A;
    result = PdcCloseEvent(*(uint64_t *)(v_stack_m7D8 + local_r12 * 8 - 0x78), Arg2, v_rip - 10406743, *(uint64_t *)(v_stack_m7D8 + local_r12 * 8 - 0x80));
    local_r14 = (v_stack_m858 + result * 1 + result * 1 + 10) | (-1);
    result = PdcCloseEvent(*(uint64_t *)(v_stack_m7D8 + local_r12 * 8 - 0x80), Arg2, v_rip - 10406743, *(uint64_t *)(v_stack_m7D8 + local_r12 * 8 - 0x80));
    result = 0;
    local_r12 = (local_r12) + (local_r14);
    *(uint64_t *)(v_stack_m7D8 + local_r12 * 8 - 0x80) = 0;
    v_stack_p48 = 0;
    v_stack_p54 = 1;
    goto loc_00A01446;
loc_00A0163C:
loc_00A01641:
    goto loc_00A01739;
loc_00A0164B:
    local_rdi = 0;
loc_00A01652:
    local_rsi = (uint32_t)(((uint32_t)(v_stack_p50)) + 1);
    if (((uint32_t)(local_rsi)) >= ((uint32_t)((uint32_t)(v_stack_p58)))) goto loc_00A01662;
    if ((*(uint8_t *)(local_rsi + v_stack_p60 * 1)) == 0) goto loc_00A01652;
loc_00A01662:
    if (((uint32_t)(local_rsi)) == ((uint32_t)((uint32_t)(v_stack_p58)))) goto loc_00A01453;
loc_00A01668:
    goto loc_00A01509;
loc_00A01672:
    goto loc_00A01516;
loc_00A0167C:
    goto loc_00A01504;
loc_00A01684:
loc_00A01689:
    goto loc_00A01509;
loc_00A01691:
    if (((uint32_t)(v_stack_p60)) != 1) goto loc_00A01668;
    goto loc_00A013E1;
loc_00A0169B:
    Arg1 = (uint32_t)((v_stack_p60) - (129));
    if (condition_is_equal) goto loc_00A01484;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A01484;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00A01484;
    Arg1 = (uint32_t)((Arg1) - (1));
loc_00A016C1:
    if (condition_is_equal) goto loc_00A01484;
loc_00A016CC:
    Arg1 = (uint32_t)((Arg1) - (13));
loc_00A016D4:
    if (local_r12 < 1) goto loc_00A01668;
loc_00A016EE:
    if (local_r12 < 2) goto loc_00A01668;
    result = EncloseSubCondition(v_stack_m848 + (int32_t)((uint32_t)((uint32_t)(v_stack_p40) - 1)) * 8, Arg2, v_rip - 10406743, *(uint64_t *)(v_stack_m7D8 + local_r12 * 8 - 0x80));
    if ((uint32_t)(result) != 0) goto loc_00A01504;
loc_00A0172A:
    goto loc_00A01641;
loc_00A01734:
loc_00A01739:
loc_00A01743:
    local_rbx = 50;
    if ((uint32_t)((uint32_t)(v_stack_p40) - 2) == 0) { local_rbx = (uint32_t)((uint32_t)(0x538ULL)); }
    v_stack_p50 = (uint32_t)(local_rbx);
loc_00A01751:
    goto loc_00A01516;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A0122C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
