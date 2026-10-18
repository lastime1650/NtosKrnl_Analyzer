# HalpInterruptParseMadt

- RVA: `0x00557E74`–`0x00558687` (길이 `2,067` bytes)
- VA: `0x0000000140557E74`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060284`
- 디코드: `584`개 명령, `2,067/2,067` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **20**

### Outgoing calls
- `0x00557F42` → [HalpMmAllocateMemoryInternal](../54/HalpMmAllocateMemoryInternal_function_00544990.md) (function, `0x00544990`)
- `0x00557F6A` → [HalpInterruptSetProblemEx](../48/HalpInterruptSetProblemEx_function_0048AC8C.md) (function, `0x0048AC8C`)
- `0x00558141` → [HalpMap](../3F/HalpMap_function_003F88F4.md) (function, `0x003F88F4`)
- `0x00558200` → [HalpMmAllocateMemoryInternal](../54/HalpMmAllocateMemoryInternal_function_00544990.md) (function, `0x00544990`)
- `0x0055825A` → [HalpMmAllocateMemoryInternal](../54/HalpMmAllocateMemoryInternal_function_00544990.md) (function, `0x00544990`)
- `0x005582EA` → [HalpInterruptGsiToLine](../2D/HalpInterruptGsiToLine_function_002D2DD0.md) (function, `0x002D2DD0`)
- `0x005582FE` → [HalpMmAllocateMemoryInternal](../54/HalpMmAllocateMemoryInternal_function_00544990.md) (function, `0x00544990`)
- `0x00558572` → [HalpInterruptSortProcessorTable](HalpInterruptSortProcessorTable_function_00558864.md) (function, `0x00558864`)
- `0x00558634` → [HalpInterruptSortProcessorTable](HalpInterruptSortProcessorTable_function_00558864.md) (function, `0x00558864`)
- `0x0055864E` → [HalpInterruptSortProcessorTable](HalpInterruptSortProcessorTable_function_00558864.md) (function, `0x00558864`)
- `0x00558665` → [HalpInterruptBlockSmtSiblings](HalpInterruptBlockSmtSiblings_function_00557670.md) (function, `0x00557670`)

### Direct callers
- [HalpInterruptParseAcpiTables](HalpInterruptParseAcpiTables_function_00557DD4.md) at `0x00557DFC`

### Static image references
- `0x00557EFF` → RVA `0x00F906C4` (`.data`; read/write)
- `0x00557F15` → RVA `0x00E10200` (`.data`; read/write)
- `0x00557F1E` → RVA `0x00E1020C` (`.data`; read)
- `0x00557F27` → RVA `0x00E1020C` (`.data`; write)
- `0x00557F37` → RVA `0x00F906C4` (`.data`; read)
- `0x00557F47` → RVA `0x00F906A8` (`.data`; write)
- `0x00557F53` → RVA `0x000250A0` (`.rdata`; read)
- `0x00557FAF` → RVA `0x00F906A8` (`.data`; read)
- `0x00558081` → RVA `0x00FC3E30` (`.data`; read)
- `0x005580EE` → RVA `0x00FC3E50` (`.data`; read)
- `0x00558222` → RVA `0x00F90700` (`.data`; read)
- `0x0055822C` → RVA `0x00F90700` (`.data`; write)
- `0x0055838E` → RVA `0x00F906E0` (`.data`; read)
- `0x00558399` → RVA `0x00F906E8` (`.data`; read)
- `0x005583AF` → RVA `0x00F906E8` (`.data`; write)
- `0x005583D5` → RVA `0x00E10200` (`.data`; read)
- `0x005583E5` → RVA `0x00E101F8` (`.data`; read)
- `0x0055855E` → RVA `0x00F906F8` (`.data`; write)
- `0x00558653` → RVA `0x00F906F8` (`.data`; read)
- `0x0055865C` → RVA `0x00F9070A` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00557E74  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00557E79  55                              push rbp
00557E7A  56                              push rsi
00557E7B  57                              push rdi
00557E7C  41 54                           push r12
00557E7E  41 55                           push r13
00557E80  41 56                           push r14
00557E82  41 57                           push r15
00557E84  48 83 EC 30                     sub rsp, 0x30
00557E88  44 8B 61 04                     mov r12d, dword ptr [rcx + 4]
00557E8C  48 8D 79 2C                     lea rdi, [rcx + 0x2c]
00557E90  48 83 64 24 70 00               and qword ptr [rsp + 0x70], 0
00557E96  33 ED                           xor ebp, ebp
00557E98  21 6C 24 78                     and dword ptr [rsp + 0x78], ebp
00557E9C  4C 03 E1                        add r12, rcx
00557E9F  45 33 ED                        xor r13d, r13d
00557EA2  45 33 C0                        xor r8d, r8d
00557EA5  48 8B F1                        mov rsi, rcx
00557EA8  4C 8B FF                        mov r15, rdi
00557EAB  8D 5D 01                        lea ebx, [rbp + 1]
00557EAE  85 D2                           test edx, edx
00557EB0  0F 85 7C 01 00 00               jne 0x140558032
00557EB6  48 8D 6F 02                     lea rbp, [rdi + 2]
00557EBA  49 3B EC                        cmp rbp, r12
00557EBD  77 78                           ja 0x140557f37
00557EBF  41 0F B6 4F 01                  movzx ecx, byte ptr [r15 + 1]
00557EC4  80 F9 02                        cmp cl, 2
00557EC7  72 6E                           jb 0x140557f37
00557EC9  4D 8D 0C 0F                     lea r9, [r15 + rcx]
00557ECD  4D 3B CC                        cmp r9, r12
00557ED0  77 65                           ja 0x140557f37
00557ED2  49 8B D7                        mov rdx, r15
00557ED5  4D 8B F9                        mov r15, r9
00557ED8  8A 02                           mov al, byte ptr [rdx]
00557EDA  84 C0                           test al, al
00557EDC  75 0A                           jne 0x140557ee8
00557EDE  80 F9 08                        cmp cl, 8
00557EE1  75 4B                           jne 0x140557f2e
00557EE3  84 5A 04                        test byte ptr [rdx + 4], bl
00557EE6  EB 2B                           jmp 0x140557f13
00557EE8  3C 09                           cmp al, 9
00557EEA  75 0A                           jne 0x140557ef6
00557EEC  80 F9 10                        cmp cl, 0x10
00557EEF  75 3D                           jne 0x140557f2e
00557EF1  84 5A 08                        test byte ptr [rdx + 8], bl
00557EF4  EB 1D                           jmp 0x140557f13
00557EF6  3A C3                           cmp al, bl
00557EF8  75 0D                           jne 0x140557f07
00557EFA  80 F9 0C                        cmp cl, 0xc
00557EFD  75 2F                           jne 0x140557f2e
00557EFF  01 1D BF 87 A3 00               add dword ptr [rip + 0xa387bf], ebx
00557F05  EB 27                           jmp 0x140557f2e
00557F07  3C 0B                           cmp al, 0xb
00557F09  75 23                           jne 0x140557f2e
00557F0B  80 F9 28                        cmp cl, 0x28
00557F0E  72 1E                           jb 0x140557f2e
00557F10  84 5A 0C                        test byte ptr [rdx + 0xc], bl
00557F13  74 06                           je 0x140557f1b
00557F15  01 1D E5 82 8B 00               add dword ptr [rip + 0x8b82e5], ebx
00557F1B  44 03 C3                        add r8d, ebx
00557F1E  44 3B 05 E7 82 8B 00            cmp r8d, dword ptr [rip + 0x8b82e7]
00557F25  76 07                           jbe 0x140557f2e
00557F27  44 89 05 DE 82 8B 00            mov dword ptr [rip + 0x8b82de], r8d
00557F2E  49 8D 41 02                     lea rax, [r9 + 2]
00557F32  49 3B C4                        cmp rax, r12
00557F35  76 88                           jbe 0x140557ebf
00557F37  8B 0D 87 87 A3 00               mov ecx, dword ptr [rip + 0xa38787]
00557F3D  8B D3                           mov edx, ebx
00557F3F  C1 E1 04                        shl ecx, 4
00557F42  E8 49 CA FE FF                  call 0x140544990
00557F47  48 89 05 5A 87 A3 00            mov qword ptr [rip + 0xa3875a], rax
00557F4E  48 85 C0                        test rax, rax
00557F51  75 26                           jne 0x140557f79
00557F53  4C 8D 0D 46 D1 AC FF            lea r9, [rip - 0x532eba]
00557F5A  C7 44 24 20 B8 06 00 00         mov dword ptr [rsp + 0x20], 0x6b8
00557F62  45 33 C0                        xor r8d, r8d
00557F65  8D 50 1E                        lea edx, [rax + 0x1e]
00557F68  33 C9                           xor ecx, ecx
00557F6A  E8 1D 2D F3 FF                  call 0x14048ac8c
00557F6F  B8 17 00 00 C0                  mov eax, 0xc0000017
00557F74  E9 F5 06 00 00                  jmp 0x14055866e
00557F79  44 8B 46 04                     mov r8d, dword ptr [rsi + 4]
00557F7D  45 33 D2                        xor r10d, r10d
00557F80  4C 03 C6                        add r8, rsi
00557F83  49 3B E8                        cmp rbp, r8
00557F86  77 53                           ja 0x140557fdb
00557F88  0F B6 4F 01                     movzx ecx, byte ptr [rdi + 1]
00557F8C  80 F9 02                        cmp cl, 2
00557F8F  72 4A                           jb 0x140557fdb
00557F91  48 8D 14 0F                     lea rdx, [rdi + rcx]
00557F95  49 3B D0                        cmp rdx, r8
00557F98  77 41                           ja 0x140557fdb
00557F9A  4C 8B CF                        mov r9, rdi
00557F9D  48 8B FA                        mov rdi, rdx
00557FA0  41 38 19                        cmp byte ptr [r9], bl
00557FA3  75 2D                           jne 0x140557fd2
00557FA5  80 F9 0C                        cmp cl, 0xc
00557FA8  75 28                           jne 0x140557fd2
00557FAA  41 0F B6 41 02                  movzx eax, byte ptr [r9 + 2]
00557FAF  48 8B 0D F2 86 A3 00            mov rcx, qword ptr [rip + 0xa386f2]
00557FB6  41 8B D2                        mov edx, r10d
00557FB9  48 03 D2                        add rdx, rdx
00557FBC  44 03 D3                        add r10d, ebx
00557FBF  89 04 D1                        mov dword ptr [rcx + rdx*8], eax
00557FC2  41 8B 41 04                     mov eax, dword ptr [r9 + 4]
00557FC6  89 44 D1 04                     mov dword ptr [rcx + rdx*8 + 4], eax
00557FCA  41 8B 41 08                     mov eax, dword ptr [r9 + 8]
00557FCE  89 44 D1 08                     mov dword ptr [rcx + rdx*8 + 8], eax
00557FD2  48 8D 47 02                     lea rax, [rdi + 2]
00557FD6  49 3B C0                        cmp rax, r8
00557FD9  76 AD                           jbe 0x140557f88
00557FDB  8B 0D E3 86 A3 00               mov ecx, dword ptr [rip + 0xa386e3]
00557FE1  85 C9                           test ecx, ecx
00557FE3  0F 84 81 06 00 00               je 0x14055866a
00557FE9  48 8B 05 B8 86 A3 00            mov rax, qword ptr [rip + 0xa386b8]
00557FF0  44 8B D1                        mov r10d, ecx
00557FF3  44 8B C1                        mov r8d, ecx
00557FF6  48 8D 78 08                     lea rdi, [rax + 8]
00557FFA  48 83 C0 0C                     add rax, 0xc
00557FFE  83 08 FF                        or dword ptr [rax], 0xffffffff
00558001  48 8B D7                        mov rdx, rdi
00558004  44 8B 58 FC                     mov r11d, dword ptr [rax - 4]
00558008  4D 8B CA                        mov r9, r10
0055800B  8B 0A                           mov ecx, dword ptr [rdx]
0055800D  41 3B CB                        cmp ecx, r11d
00558010  76 09                           jbe 0x14055801b
00558012  41 2B CB                        sub ecx, r11d
00558015  3B 08                           cmp ecx, dword ptr [rax]
00558017  73 02                           jae 0x14055801b
00558019  89 08                           mov dword ptr [rax], ecx
0055801B  48 83 C2 10                     add rdx, 0x10
0055801F  4C 2B CB                        sub r9, rbx
00558022  75 E7                           jne 0x14055800b
00558024  48 83 C0 10                     add rax, 0x10
00558028  4C 2B C3                        sub r8, rbx
0055802B  75 D1                           jne 0x140557ffe
0055802D  E9 38 06 00 00                  jmp 0x14055866a
00558032  41 B9 04 00 00 00               mov r9d, 4
00558038  BE 03 00 00 00                  mov esi, 3
0055803D  4D 8D 47 02                     lea r8, [r15 + 2]
00558041  4D 3B C4                        cmp r8, r12
00558044  0F 87 8B 03 00 00               ja 0x1405583d5
0055804A  4D 8D 77 01                     lea r14, [r15 + 1]
0055804E  41 0F B6 0E                     movzx ecx, byte ptr [r14]
00558052  80 F9 02                        cmp cl, 2
00558055  0F 82 7A 03 00 00               jb 0x1405583d5
0055805B  49 8D 14 0F                     lea rdx, [r15 + rcx]
0055805F  49 3B D4                        cmp rdx, r12
00558062  0F 87 6D 03 00 00               ja 0x1405583d5
00558068  49 8B FF                        mov rdi, r15
0055806B  8A C1                           mov al, cl
0055806D  4C 8B FA                        mov r15, rdx
00558070  8A 17                           mov dl, byte ptr [rdi]
00558072  84 D2                           test dl, dl
00558074  75 2A                           jne 0x1405580a0
00558076  80 F9 08                        cmp cl, 8
00558079  75 25                           jne 0x1405580a0
0055807B  8B CD                           mov ecx, ebp
0055807D  48 C1 E1 06                     shl rcx, 6
00558081  48 03 0D A8 BD A6 00            add rcx, qword ptr [rip + 0xa6bda8]
00558088  84 5F 04                        test byte ptr [rdi + 4], bl
0055808B  74 B0                           je 0x14055803d
0055808D  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
00558091  89 01                           mov dword ptr [rcx], eax
00558093  41 0F B6 00                     movzx eax, byte ptr [r8]
00558097  89 41 04                        mov dword ptr [rcx + 4], eax
0055809A  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
0055809E  EB 30                           jmp 0x1405580d0
005580A0  80 FA 09                        cmp dl, 9
005580A3  75 35                           jne 0x1405580da
005580A5  8A C1                           mov al, cl
005580A7  80 F9 10                        cmp cl, 0x10
005580AA  75 2E                           jne 0x1405580da
005580AC  8B CD                           mov ecx, ebp
005580AE  48 C1 E1 06                     shl rcx, 6
005580B2  48 03 0D 77 BD A6 00            add rcx, qword ptr [rip + 0xa6bd77]
005580B9  84 5F 08                        test byte ptr [rdi + 8], bl
005580BC  0F 84 7B FF FF FF               je 0x14055803d
005580C2  8B 47 04                        mov eax, dword ptr [rdi + 4]
005580C5  89 01                           mov dword ptr [rcx], eax
005580C7  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
005580CA  89 41 04                        mov dword ptr [rcx + 4], eax
005580CD  8B 47 04                        mov eax, dword ptr [rdi + 4]
005580D0  89 41 08                        mov dword ptr [rcx + 8], eax
005580D3  03 EB                           add ebp, ebx
005580D5  E9 63 FF FF FF                  jmp 0x14055803d
005580DA  80 FA 0B                        cmp dl, 0xb
005580DD  0F 85 0B 01 00 00               jne 0x1405581ee
005580E3  8A C1                           mov al, cl
005580E5  80 F9 28                        cmp cl, 0x28
005580E8  0F 82 00 01 00 00               jb 0x1405581ee
005580EE  39 35 5C BD A6 00               cmp dword ptr [rip + 0xa6bd5c], esi
005580F4  72 09                           jb 0x1405580ff
005580F6  80 F9 4C                        cmp cl, 0x4c
005580F9  0F 82 EF 00 00 00               jb 0x1405581ee
005580FF  8B F5                           mov esi, ebp
00558101  48 C1 E6 06                     shl rsi, 6
00558105  48 03 35 24 BD A6 00            add rsi, qword ptr [rip + 0xa6bd24]
0055810C  84 5F 0C                        test byte ptr [rdi + 0xc], bl
0055810F  0F 84 23 FF FF FF               je 0x140558038
00558115  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
00558119  39 5F 10                        cmp dword ptr [rdi + 0x10], ebx
0055811C  0F 85 BF 00 00 00               jne 0x1405581e1
00558122  48 85 C9                        test rcx, rcx
00558125  0F 84 B6 00 00 00               je 0x1405581e1
0055812B  4C 21 6C 24 28                  and qword ptr [rsp + 0x28], r13
00558130  45 33 C0                        xor r8d, r8d
00558133  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
00558138  8B D3                           mov edx, ebx
0055813A  45 33 C9                        xor r9d, r9d
0055813D  48 89 4E 18                     mov qword ptr [rsi + 0x18], rcx
00558141  E8 AE 07 EA FF                  call 0x1403f88f4
00558146  48 8B C8                        mov rcx, rax
00558149  48 89 46 20                     mov qword ptr [rsi + 0x20], rax
0055814D  48 F7 D8                        neg rax
00558150  45 1B C9                        sbb r9d, r9d
00558153  41 F7 D1                        not r9d
00558156  41 81 E1 9A 00 00 C0            and r9d, 0xc000009a
0055815D  44 89 4C 24 78                  mov dword ptr [rsp + 0x78], r9d
00558162  48 85 C9                        test rcx, rcx
00558165  0F 84 60 02 00 00               je 0x1405583cb
0055816B  83 3D DE BC A6 00 03            cmp dword ptr [rip + 0xa6bcde], 3
00558172  72 1A                           jb 0x14055818e
00558174  48 8B 4F 44                     mov rcx, qword ptr [rdi + 0x44]
00558178  48 C1 E9 08                     shr rcx, 8
0055817C  8B C1                           mov eax, ecx
0055817E  33 47 44                        xor eax, dword ptr [rdi + 0x44]
00558181  25 FF FF FF 00                  and eax, 0xffffff
00558186  33 C1                           xor eax, ecx
00558188  89 06                           mov dword ptr [rsi], eax
0055818A  33 C0                           xor eax, eax
0055818C  EB 08                           jmp 0x140558196
0055818E  8B 47 04                        mov eax, dword ptr [rdi + 4]
00558191  89 06                           mov dword ptr [rsi], eax
00558193  8B 47 04                        mov eax, dword ptr [rdi + 4]
00558196  89 46 08                        mov dword ptr [rsi + 8], eax
00558199  8B 47 08                        mov eax, dword ptr [rdi + 8]
0055819C  89 46 04                        mov dword ptr [rsi + 4], eax
0055819F  8B 47 14                        mov eax, dword ptr [rdi + 0x14]
005581A2  89 46 28                        mov dword ptr [rsi + 0x28], eax
005581A5  41 80 3E 4C                     cmp byte ptr [r14], 0x4c
005581A9  72 19                           jb 0x1405581c4
005581AB  48 8B 47 44                     mov rax, qword ptr [rdi + 0x44]
005581AF  48 89 46 30                     mov qword ptr [rsi + 0x30], rax
005581B3  88 5E 2D                        mov byte ptr [rsi + 0x2d], bl
005581B6  80 7F 01 4D                     cmp byte ptr [rdi + 1], 0x4d
005581BA  72 10                           jb 0x1405581cc
005581BC  8A 47 4C                        mov al, byte ptr [rdi + 0x4c]
005581BF  88 46 2C                        mov byte ptr [rsi + 0x2c], al
005581C2  EB 08                           jmp 0x1405581cc
005581C4  4C 21 6E 30                     and qword ptr [rsi + 0x30], r13
005581C8  44 88 6E 2D                     mov byte ptr [rsi + 0x2d], r13b
005581CC  F6 47 0C 02                     test byte ptr [rdi + 0xc], 2
005581D0  74 03                           je 0x1405581d5
005581D2  88 5E 0E                        mov byte ptr [rsi + 0xe], bl
005581D5  03 EB                           add ebp, ebx
005581D7  BE 03 00 00 00                  mov esi, 3
005581DC  E9 DA 01 00 00                  jmp 0x1405583bb
005581E1  C7 44 24 78 0D 00 00 C0         mov dword ptr [rsp + 0x78], 0xc000000d
005581E9  E9 4A FE FF FF                  jmp 0x140558038
005581EE  8A C8                           mov cl, al
005581F0  40 3A D6                        cmp dl, sil
005581F3  75 43                           jne 0x140558238
005581F5  3C 08                           cmp al, 8
005581F7  75 3F                           jne 0x140558238
005581F9  8B D3                           mov edx, ebx
005581FB  B9 18 00 00 00                  mov ecx, 0x18
00558200  E8 8B C7 FE FF                  call 0x140544990
00558205  48 8B C8                        mov rcx, rax
00558208  48 85 C0                        test rax, rax
0055820B  0F 84 BA 01 00 00               je 0x1405583cb
00558211  44 88 68 08                     mov byte ptr [rax + 8], r13b
00558215  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
00558219  89 41 10                        mov dword ptr [rcx + 0x10], eax
0055821C  8B 47 04                        mov eax, dword ptr [rdi + 4]
0055821F  89 41 14                        mov dword ptr [rcx + 0x14], eax
00558222  48 8B 05 D7 84 A3 00            mov rax, qword ptr [rip + 0xa384d7]
00558229  48 89 01                        mov qword ptr [rcx], rax
0055822C  48 89 0D CD 84 A3 00            mov qword ptr [rip + 0xa384cd], rcx
00558233  E9 83 01 00 00                  jmp 0x1405583bb
00558238  8A C1                           mov al, cl
0055823A  41 3A D1                        cmp dl, r9b
0055823D  75 05                           jne 0x140558244
0055823F  80 F9 06                        cmp cl, 6
00558242  74 0F                           je 0x140558253
00558244  8A C8                           mov cl, al
00558246  80 FA 0A                        cmp dl, 0xa
00558249  0F 85 81 00 00 00               jne 0x1405582d0
0055824F  3C 0C                           cmp al, 0xc
00558251  75 7D                           jne 0x1405582d0
00558253  8B D3                           mov edx, ebx
00558255  B9 18 00 00 00                  mov ecx, 0x18
0055825A  E8 31 C7 FE FF                  call 0x140544990
0055825F  48 8B C8                        mov rcx, rax
00558262  48 85 C0                        test rax, rax
00558265  0F 84 60 01 00 00               je 0x1405583cb
0055826B  33 C0                           xor eax, eax
0055826D  0F 57 C0                        xorps xmm0, xmm0
00558270  0F 11 01                        movups xmmword ptr [rcx], xmm0
00558273  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
00558277  88 59 08                        mov byte ptr [rcx + 8], bl
0055827A  44 8D 48 04                     lea r9d, [rax + 4]
0055827E  44 38 0F                        cmp byte ptr [rdi], r9b
00558281  75 1D                           jne 0x1405582a0
00558283  0F B6 47 02                     movzx eax, byte ptr [rdi + 2]
00558287  89 41 0C                        mov dword ptr [rcx + 0xc], eax
0055828A  80 7F 02 FF                     cmp byte ptr [rdi + 2], 0xff
0055828E  75 04                           jne 0x140558294
00558290  83 49 0C FF                     or dword ptr [rcx + 0xc], 0xffffffff
00558294  0F B7 47 03                     movzx eax, word ptr [rdi + 3]
00558298  89 41 10                        mov dword ptr [rcx + 0x10], eax
0055829B  8A 47 05                        mov al, byte ptr [rdi + 5]
0055829E  EB 10                           jmp 0x1405582b0
005582A0  8B 47 04                        mov eax, dword ptr [rdi + 4]
005582A3  89 41 0C                        mov dword ptr [rcx + 0xc], eax
005582A6  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
005582AA  89 41 10                        mov dword ptr [rcx + 0x10], eax
005582AD  8A 47 08                        mov al, byte ptr [rdi + 8]
005582B0  F6 D8                           neg al
005582B2  1B C0                           sbb eax, eax
005582B4  83 C0 FC                        add eax, -4
005582B7  89 41 14                        mov dword ptr [rcx + 0x14], eax
005582BA  48 8B 05 3F 84 A3 00            mov rax, qword ptr [rip + 0xa3843f]
005582C1  48 89 01                        mov qword ptr [rcx], rax
005582C4  48 89 0D 35 84 A3 00            mov qword ptr [rip + 0xa38435], rcx
005582CB  E9 6D FD FF FF                  jmp 0x14055803d
005582D0  80 FA 02                        cmp dl, 2
005582D3  0F 85 64 FD FF FF               jne 0x14055803d
005582D9  80 F9 0A                        cmp cl, 0xa
005582DC  0F 85 5B FD FF FF               jne 0x14055803d
005582E2  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
005582E5  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
005582EA  E8 E1 AA D7 FF                  call 0x1402d2dd0
005582EF  85 C0                           test eax, eax
005582F1  0F 88 BF 00 00 00               js 0x1405583b6
005582F7  8B D3                           mov edx, ebx
005582F9  B9 28 00 00 00                  mov ecx, 0x28
005582FE  E8 8D C6 FE FF                  call 0x140544990
00558303  48 8B C8                        mov rcx, rax
00558306  48 85 C0                        test rax, rax
00558309  0F 84 BC 00 00 00               je 0x1405583cb
0055830F  33 C0                           xor eax, eax
00558311  0F 57 C0                        xorps xmm0, xmm0
00558314  0F 11 01                        movups xmmword ptr [rcx], xmm0
00558317  4C 8B C1                        mov r8, rcx
0055831A  0F 11 41 10                     movups xmmword ptr [rcx + 0x10], xmm0
0055831E  48 89 41 20                     mov qword ptr [rcx + 0x20], rax
00558322  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
00558326  83 F8 08                        cmp eax, 8
00558329  73 07                           jae 0x140558332
0055832B  BA 00 B0 00 00                  mov edx, 0xb000
00558330  EB 08                           jmp 0x14055833a
00558332  83 C0 F8                        add eax, -8
00558335  BA 01 B0 00 00                  mov edx, 0xb001
0055833A  41 89 50 10                     mov dword ptr [r8 + 0x10], edx
0055833E  89 41 14                        mov dword ptr [rcx + 0x14], eax
00558341  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00558346  48 89 41 18                     mov qword ptr [rcx + 0x18], rax
0055834A  0F B7 47 08                     movzx eax, word ptr [rdi + 8]
0055834E  66 23 C6                        and ax, si
00558351  74 0A                           je 0x14055835d
00558353  66 3B C3                        cmp ax, bx
00558356  B8 02 00 00 00                  mov eax, 2
0055835B  75 02                           jne 0x14055835f
0055835D  8B C3                           mov eax, ebx
0055835F  41 B8 24 00 00 00               mov r8d, 0x24
00558365  48 8B D1                        mov rdx, rcx
00558368  41 89 04 08                     mov dword ptr [r8 + rcx], eax
0055836C  0F B7 47 08                     movzx eax, word ptr [rdi + 8]
00558370  66 83 E0 0C                     and ax, 0xc
00558374  74 0D                           je 0x140558383
00558376  41 8D 50 E0                     lea edx, [r8 - 0x20]
0055837A  66 3B C2                        cmp ax, dx
0055837D  74 04                           je 0x140558383
0055837F  33 C0                           xor eax, eax
00558381  EB 02                           jmp 0x140558385
00558383  8B C3                           mov eax, ebx
00558385  41 B8 20 00 00 00               mov r8d, 0x20
0055838B  48 8B D1                        mov rdx, rcx
0055838E  48 8D 15 4B 83 A3 00            lea rdx, [rip + 0xa3834b]
00558395  41 89 04 08                     mov dword ptr [r8 + rcx], eax
00558399  48 8B 05 48 83 A3 00            mov rax, qword ptr [rip + 0xa38348]
005583A0  48 39 10                        cmp qword ptr [rax], rdx
005583A3  75 21                           jne 0x1405583c6
005583A5  48 89 11                        mov qword ptr [rcx], rdx
005583A8  48 89 41 08                     mov qword ptr [rcx + 8], rax
005583AC  48 89 08                        mov qword ptr [rax], rcx
005583AF  48 89 0D 32 83 A3 00            mov qword ptr [rip + 0xa38332], rcx
005583B6  44 21 6C 24 78                  and dword ptr [rsp + 0x78], r13d
005583BB  41 B9 04 00 00 00               mov r9d, 4
005583C1  E9 77 FC FF FF                  jmp 0x14055803d
005583C6  48 8B CE                        mov rcx, rsi
005583C9  CD 29                           int 0x29
005583CB  B8 9A 00 00 C0                  mov eax, 0xc000009a
005583D0  E9 99 02 00 00                  jmp 0x14055866e
005583D5  44 8B 0D 24 7E 8B 00            mov r9d, dword ptr [rip + 0x8b7e24]
005583DC  44 3B CB                        cmp r9d, ebx
005583DF  0F 86 85 02 00 00               jbe 0x14055866a
005583E5  4C 8B 15 0C 7E 8B 00            mov r10, qword ptr [rip + 0x8b7e0c]
005583EC  45 33 C0                        xor r8d, r8d
005583EF  45 3B C1                        cmp r8d, r9d
005583F2  73 1F                           jae 0x140558413
005583F4  48 8B 05 35 BA A6 00            mov rax, qword ptr [rip + 0xa6ba35]
005583FB  41 8B 0A                        mov ecx, dword ptr [r10]
005583FE  41 8B D0                        mov edx, r8d
00558401  48 C1 E2 06                     shl rdx, 6
00558405  39 4C 02 08                     cmp dword ptr [rdx + rax + 8], ecx
00558409  74 05                           je 0x140558410
0055840B  44 03 C3                        add r8d, ebx
0055840E  EB DF                           jmp 0x1405583ef
00558410  45 8B E8                        mov r13d, r8d
00558413  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0055841C  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00558425  44 8B 80 A4 00 00 00            mov r8d, dword ptr [rax + 0xa4]
0055842C  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00558435  44 2B C3                        sub r8d, ebx
00558438  41 F7 D0                        not r8d
0055843B  8B B0 A0 00 00 00               mov esi, dword ptr [rax + 0xa0]
00558441  0F AF B1 A4 00 00 00            imul esi, dword ptr [rcx + 0xa4]
00558448  48 8B 05 A9 7D 8B 00            mov rax, qword ptr [rip + 0x8b7da9]
0055844F  8B 28                           mov ebp, dword ptr [rax]
00558451  2B F3                           sub esi, ebx
00558453  44 8B CD                        mov r9d, ebp
00558456  F7 D6                           not esi
00558458  23 EE                           and ebp, esi
0055845A  45 23 C8                        and r9d, r8d
0055845D  45 85 ED                        test r13d, r13d
00558460  74 4D                           je 0x1405584af
00558462  48 8B 0D C7 B9 A6 00            mov rcx, qword ptr [rip + 0xa6b9c7]
00558469  41 8B C5                        mov eax, r13d
0055846C  48 C1 E0 06                     shl rax, 6
00558470  48 03 C1                        add rax, rcx
00558473  0F 10 11                        movups xmm2, xmmword ptr [rcx]
00558476  0F 10 59 10                     movups xmm3, xmmword ptr [rcx + 0x10]
0055847A  0F 10 00                        movups xmm0, xmmword ptr [rax]
0055847D  0F 10 61 20                     movups xmm4, xmmword ptr [rcx + 0x20]
00558481  0F 10 69 30                     movups xmm5, xmmword ptr [rcx + 0x30]
00558485  0F 11 01                        movups xmmword ptr [rcx], xmm0
00558488  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
0055848C  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00558490  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
00558494  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
00558498  0F 10 48 30                     movups xmm1, xmmword ptr [rax + 0x30]
0055849C  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
005584A0  0F 11 10                        movups xmmword ptr [rax], xmm2
005584A3  0F 11 58 10                     movups xmmword ptr [rax + 0x10], xmm3
005584A7  0F 11 60 20                     movups xmmword ptr [rax + 0x20], xmm4
005584AB  0F 11 68 30                     movups xmmword ptr [rax + 0x30], xmm5
005584AF  8B 0D 4B 7D 8B 00               mov ecx, dword ptr [rip + 0x8b7d4b]
005584B5  8B FB                           mov edi, ebx
005584B7  3B CB                           cmp ecx, ebx
005584B9  76 1F                           jbe 0x1405584da
005584BB  48 8B 15 6E B9 A6 00            mov rdx, qword ptr [rip + 0xa6b96e]
005584C2  48 83 C2 48                     add rdx, 0x48
005584C6  8B 02                           mov eax, dword ptr [rdx]
005584C8  41 23 C0                        and eax, r8d
005584CB  41 3B C1                        cmp eax, r9d
005584CE  75 0A                           jne 0x1405584da
005584D0  03 FB                           add edi, ebx
005584D2  48 83 C2 40                     add rdx, 0x40
005584D6  3B F9                           cmp edi, ecx
005584D8  72 EC                           jb 0x1405584c6
005584DA  8D 47 01                        lea eax, [rdi + 1]
005584DD  3B C1                           cmp eax, ecx
005584DF  73 79                           jae 0x14055855a
005584E1  8B D0                           mov edx, eax
005584E3  48 C1 E2 06                     shl rdx, 6
005584E7  48 03 15 42 B9 A6 00            add rdx, qword ptr [rip + 0xa6b942]
005584EE  2B C8                           sub ecx, eax
005584F0  44 8B D1                        mov r10d, ecx
005584F3  8B 42 08                        mov eax, dword ptr [rdx + 8]
005584F6  41 23 C0                        and eax, r8d
005584F9  41 3B C1                        cmp eax, r9d
005584FC  75 53                           jne 0x140558551
005584FE  0F 10 02                        movups xmm0, xmmword ptr [rdx]
00558501  48 8B 05 28 B9 A6 00            mov rax, qword ptr [rip + 0xa6b928]
00558508  8B CF                           mov ecx, edi
0055850A  48 C1 E1 06                     shl rcx, 6
0055850E  03 FB                           add edi, ebx
00558510  0F 10 14 01                     movups xmm2, xmmword ptr [rcx + rax]
00558514  0F 10 5C 01 10                  movups xmm3, xmmword ptr [rcx + rax + 0x10]
00558519  0F 10 64 01 20                  movups xmm4, xmmword ptr [rcx + rax + 0x20]
0055851E  0F 10 6C 01 30                  movups xmm5, xmmword ptr [rcx + rax + 0x30]
00558523  0F 11 04 01                     movups xmmword ptr [rcx + rax], xmm0
00558527  0F 10 4A 10                     movups xmm1, xmmword ptr [rdx + 0x10]
0055852B  0F 11 4C 01 10                  movups xmmword ptr [rcx + rax + 0x10], xmm1
00558530  0F 10 42 20                     movups xmm0, xmmword ptr [rdx + 0x20]
00558534  0F 11 44 01 20                  movups xmmword ptr [rcx + rax + 0x20], xmm0
00558539  0F 10 4A 30                     movups xmm1, xmmword ptr [rdx + 0x30]
0055853D  0F 11 4C 01 30                  movups xmmword ptr [rcx + rax + 0x30], xmm1
00558542  0F 11 12                        movups xmmword ptr [rdx], xmm2
00558545  0F 11 5A 10                     movups xmmword ptr [rdx + 0x10], xmm3
00558549  0F 11 62 20                     movups xmmword ptr [rdx + 0x20], xmm4
0055854D  0F 11 6A 30                     movups xmmword ptr [rdx + 0x30], xmm5
00558551  48 83 C2 40                     add rdx, 0x40
00558555  4C 2B D3                        sub r10, rbx
00558558  75 99                           jne 0x1405584f3
0055855A  3B FB                           cmp edi, ebx
0055855C  76 06                           jbe 0x140558564
0055855E  88 1D 94 81 A3 00               mov byte ptr [rip + 0xa38194], bl
00558564  4C 8B 35 C5 B8 A6 00            mov r14, qword ptr [rip + 0xa6b8c5]
0055856B  8D 57 FF                        lea edx, [rdi - 1]
0055856E  49 8D 4E 40                     lea rcx, [r14 + 0x40]
00558572  E8 ED 02 00 00                  call 0x140558864
00558577  8B 0D 83 7C 8B 00               mov ecx, dword ptr [rip + 0x8b7c83]
0055857D  44 8B CF                        mov r9d, edi
00558580  3B F9                           cmp edi, ecx
00558582  73 1F                           jae 0x1405585a3
00558584  8B D7                           mov edx, edi
00558586  48 C1 E2 06                     shl rdx, 6
0055858A  48 83 C2 08                     add rdx, 8
0055858E  49 03 D6                        add rdx, r14
00558591  8B C6                           mov eax, esi
00558593  23 02                           and eax, dword ptr [rdx]
00558595  3B C5                           cmp eax, ebp
00558597  75 0A                           jne 0x1405585a3
00558599  03 FB                           add edi, ebx
0055859B  48 83 C2 40                     add rdx, 0x40
0055859F  3B F9                           cmp edi, ecx
005585A1  72 EE                           jb 0x140558591
005585A3  8D 47 01                        lea eax, [rdi + 1]
005585A6  3B C1                           cmp eax, ecx
005585A8  73 77                           jae 0x140558621
005585AA  8B D0                           mov edx, eax
005585AC  48 C1 E2 06                     shl rdx, 6
005585B0  48 03 15 79 B8 A6 00            add rdx, qword ptr [rip + 0xa6b879]
005585B7  2B C8                           sub ecx, eax
005585B9  44 8B C1                        mov r8d, ecx
005585BC  8B 42 08                        mov eax, dword ptr [rdx + 8]
005585BF  23 C6                           and eax, esi
005585C1  3B C5                           cmp eax, ebp
005585C3  75 53                           jne 0x140558618
005585C5  0F 10 02                        movups xmm0, xmmword ptr [rdx]
005585C8  48 8B 05 61 B8 A6 00            mov rax, qword ptr [rip + 0xa6b861]
005585CF  8B CF                           mov ecx, edi
005585D1  48 C1 E1 06                     shl rcx, 6
005585D5  03 FB                           add edi, ebx
005585D7  0F 10 14 01                     movups xmm2, xmmword ptr [rcx + rax]
005585DB  0F 10 5C 01 10                  movups xmm3, xmmword ptr [rcx + rax + 0x10]
005585E0  0F 10 64 01 20                  movups xmm4, xmmword ptr [rcx + rax + 0x20]
005585E5  0F 10 6C 01 30                  movups xmm5, xmmword ptr [rcx + rax + 0x30]
005585EA  0F 11 04 01                     movups xmmword ptr [rcx + rax], xmm0
005585EE  0F 10 4A 10                     movups xmm1, xmmword ptr [rdx + 0x10]
005585F2  0F 11 4C 01 10                  movups xmmword ptr [rcx + rax + 0x10], xmm1
005585F7  0F 10 42 20                     movups xmm0, xmmword ptr [rdx + 0x20]
005585FB  0F 11 44 01 20                  movups xmmword ptr [rcx + rax + 0x20], xmm0
00558600  0F 10 4A 30                     movups xmm1, xmmword ptr [rdx + 0x30]
00558604  0F 11 4C 01 30                  movups xmmword ptr [rcx + rax + 0x30], xmm1
00558609  0F 11 12                        movups xmmword ptr [rdx], xmm2
0055860C  0F 11 5A 10                     movups xmmword ptr [rdx + 0x10], xmm3
00558610  0F 11 62 20                     movups xmmword ptr [rdx + 0x20], xmm4
00558614  0F 11 6A 30                     movups xmmword ptr [rdx + 0x30], xmm5
00558618  48 83 C2 40                     add rdx, 0x40
0055861C  4C 2B C3                        sub r8, rbx
0055861F  75 9B                           jne 0x1405585bc
00558621  49 8B C9                        mov rcx, r9
00558624  8B D7                           mov edx, edi
00558626  48 C1 E1 06                     shl rcx, 6
0055862A  41 2B D1                        sub edx, r9d
0055862D  48 03 0D FC B7 A6 00            add rcx, qword ptr [rip + 0xa6b7fc]
00558634  E8 2B 02 00 00                  call 0x140558864
00558639  8B 15 C1 7B 8B 00               mov edx, dword ptr [rip + 0x8b7bc1]
0055863F  8B CF                           mov ecx, edi
00558641  2B D7                           sub edx, edi
00558643  48 C1 E1 06                     shl rcx, 6
00558647  48 03 0D E2 B7 A6 00            add rcx, qword ptr [rip + 0xa6b7e2]
0055864E  E8 11 02 00 00                  call 0x140558864
00558653  80 3D 9E 80 A3 00 00            cmp byte ptr [rip + 0xa3809e], 0
0055865A  74 0E                           je 0x14055866a
0055865C  80 3D A7 80 A3 00 00            cmp byte ptr [rip + 0xa380a7], 0
00558663  74 05                           je 0x14055866a
00558665  E8 06 F0 FF FF                  call 0x140557670
0055866A  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
0055866E  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
00558676  48 83 C4 30                     add rsp, 0x30
0055867A  41 5F                           pop r15
0055867C  41 5E                           pop r14
0055867E  41 5D                           pop r13
00558680  41 5C                           pop r12
00558682  5F                              pop rdi
00558683  5E                              pop rsi
00558684  5D                              pop rbp
00558685  C3                              ret
00558686  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpInterruptParseMadt(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (48);
    v_rbp = 0;
    v_r12 = ((unsigned int)(*(unsigned int *)(a1 + 4))) + (a1);
    v_r13 = 0;
    a3 = 0;
    if (a2 != 0) goto loc_00558032;
    if ((a1 + 44 + 2) > v_r12) goto loc_00557F37;
loc_00557EBF:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 44 + 1))) < 2) goto loc_00557F37;
    if ((a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1) > v_r12) goto loc_00557F37;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 44)) != 0) goto loc_00557EE8;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 44 + 1))) != 8) goto loc_00557F2E;
    goto loc_00557F13;
loc_00557EE8:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 44))) != 9) goto loc_00557EF6;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 44 + 1))) != 16) goto loc_00557F2E;
    goto loc_00557F13;
loc_00557EF6:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 44))) != ((unsigned __int8)(v_rbp + 1))) goto loc_00557F07;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 44 + 1))) != 12) goto loc_00557F2E;
    goto loc_00557F2E;
loc_00557F07:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 44))) != 11) goto loc_00557F2E;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 44 + 1))) < 40) goto loc_00557F2E;
loc_00557F13:
    if (((*(unsigned __int8 *)(a1 + 44 + 12)) & ((unsigned __int8)(v_rbp + 1))) != 0) {
    }
    a3 = (unsigned int)((a3) + ((unsigned int)(v_rbp + 1)));
    if (a3 >= = (*(unsigned int *)(v_rip + 9143015))) {
        *(unsigned int *)(v_rip + 9143006) = a3;
    }
    if ((a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 2) <= v_r12) goto loc_00557EBF;
loc_00557F37:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10717063))) << (4));
    result = HalpMmAllocateMemoryInternal(a1, (unsigned int)((unsigned int)(v_rbp + 1)), a3, a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1);
    *(unsigned __int64 *)(v_rip + 10717018) = result;
    if (result != 0) goto loc_00557F79;
    v_stack_m48 = 0x6B8ULL;
    a3 = 0;
    a1 = 0;
    result = HalpInterruptSetProblemEx(a1, result + 30, a3, v_rip - 5451450);
    goto loc_0055866E;
loc_00557F79:
    v_r10 = 0;
    a3 = ((unsigned int)(*(unsigned int *)(a1 + 4))) + (0);
    if ((a1 + 44 + 2) > a3) goto loc_00557FDB;
loc_00557F88:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 44 + 1))) < 2) goto loc_00557FDB;
    if ((a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1) > a3) goto loc_00557FDB;
    if ((*(unsigned __int8 *)(a1 + 44)) != ((unsigned __int8)(v_rbp + 1))) goto loc_00557FD2;
    result = (unsigned int)(0xC0000017ULL);
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 44 + 1))) == 12) {
        result = *(unsigned __int8 *)(a1 + 44 + 2);
        a1 = *(unsigned __int64 *)(v_rip + 10716914);
        a2 = 0;
        a2 = (a2) + (a2);
        v_r10 = (unsigned int)((v_r10) + ((unsigned int)(v_rbp + 1)));
        *(unsigned int *)(a1 + a2 * 8) = (unsigned int)(result);
        result = *(unsigned int *)(a1 + 44 + 4);
        *(unsigned int *)(a1 + a2 * 8 + 4) = (unsigned int)(result);
        result = *(unsigned int *)(a1 + 44 + 8);
        *(unsigned int *)(a1 + a2 * 8 + 8) = (unsigned int)(result);
    }
    if ((a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 2) <= a3) goto loc_00557F88;
loc_00557FDB:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10716899))) == 0) goto loc_0055866A;
    result = (*(unsigned __int64 *)(v_rip + 10716856)) + (12);
loc_00557FFE:
loc_0055800B:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10716856) + 8)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(result - 4))))) goto loc_0055801B;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10716856) + 8))) - ((unsigned int)((unsigned int)(*(unsigned int *)(result - 4)))));
    if (((unsigned int)(a1)) < (*(unsigned int *)(result))) {
        *(unsigned int *)(result) = (unsigned int)(a1);
    }
    a2 = (*(unsigned __int64 *)(v_rip + 10716856) + 8) + (16);
    a4 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10716899))))) - (v_rbp + 1);
    if (condition_is_not_equal) goto loc_0055800B;
    result = (result) + (16);
    a3 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10716899))))) - (v_rbp + 1);
    if (condition_is_not_equal) goto loc_00557FFE;
    goto loc_0055866A;
loc_00558032:
loc_00558038:
loc_0055803D:
    if ((a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 2) > v_r12) goto loc_005583D5;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 1))) < 2) goto loc_005583D5;
    if ((a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + *(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 1) * 1) > v_r12) goto loc_005583D5;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1)) != 0) goto loc_005580A0;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 1))) != 8) goto loc_005580A0;
    a1 = ((unsigned int)((unsigned int)(a1 + 44 + 2))) << (6);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 10927528));
    if (((*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 4)) & ((unsigned __int8)(v_rbp + 1))) == 0) goto loc_0055803D;
    *(unsigned int *)(a1) = (unsigned int)(*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 3));
    *(unsigned int *)(a1 + 4) = (unsigned int)(*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 2));
    goto loc_005580D0;
loc_005580A0:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1))) != 9) goto loc_005580DA;
    if (((unsigned __int8)(a1)) != 16) goto loc_005580DA;
    a1 = ((unsigned int)((unsigned int)(a1 + 44 + 2))) << (6);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 10927479));
    if (((*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 8)) & ((unsigned __int8)(v_rbp + 1))) == 0) goto loc_0055803D;
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 4)));
    *(unsigned int *)(a1 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 12)));
loc_005580D0:
    *(unsigned int *)(a1 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 4)));
    v_rbp = (unsigned int)((a1 + 44 + 2) + ((unsigned int)(v_rbp + 1)));
    goto loc_0055803D;
loc_005580DA:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1))) != 11) goto loc_005581EE;
    if (((unsigned __int8)(a1)) < 40) goto loc_005581EE;
    if ((*(unsigned int *)(v_rip + 10927452)) < 3) goto loc_005580FF;
    if (((unsigned __int8)(a1)) < 76) goto loc_005581EE;
loc_005580FF:
    v_rsi = ((unsigned int)((unsigned int)(v_rbp))) << (6);
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(v_rip + 10927396));
    if (((*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 12)) & ((unsigned __int8)(v_rbp + 1))) == 0) goto loc_00558038;
    if ((*(unsigned int *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 16)) != ((unsigned int)(v_rbp + 1))) goto loc_005581E1;
    if (*(unsigned __int64 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 24) == 0) goto loc_005581E1;
    a3 = 0;
    v_stack_m48 = 4;
    a4 = 0;
    *(unsigned __int64 *)(v_rsi + 24) = *(unsigned __int64 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 24);
    result = HalpMap(*(unsigned __int64 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 24), (unsigned int)((unsigned int)(v_rbp + 1)), a3, a4);
    *(unsigned __int64 *)(v_rsi + 32) = result;
    result = -(result);
    a4 = (unsigned int)(~(a4));
    a4 = (unsigned int)((a4) & (0xC000009AULL));
    v_stack_p10 = (unsigned int)(a4);
    if (result == 0) goto loc_005583CB;
    if ((*(unsigned int *)(v_rip + 10927326)) < 3) goto loc_0055818E;
    a1 = (*(unsigned __int64 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 68)) >> (8);
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) ^ (*(unsigned int *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 68)));
    result = (unsigned int)((result) & (0xFFFFFFULL));
    result = (unsigned int)((result) ^ ((unsigned int)(a1)));
    *(unsigned int *)(v_rsi) = (unsigned int)(result);
    result = 0;
    goto loc_00558196;
loc_0055818E:
    *(unsigned int *)(v_rsi) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 4)));
loc_00558196:
    *(unsigned int *)(v_rsi + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 4)));
    *(unsigned int *)(v_rsi + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 8)));
    *(unsigned int *)(v_rsi + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 20)));
    if ((*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 1)) < 76) goto loc_005581C4;
    *(unsigned __int64 *)(v_rsi + 48) = *(unsigned __int64 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 68);
    *(unsigned __int8 *)(v_rsi + 45) = (unsigned __int8)(v_rbp + 1);
    if ((*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 1)) < 77) goto loc_005581CC;
    *(unsigned __int8 *)(v_rsi + 44) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 76));
    goto loc_005581CC;
loc_005581C4:
    *(unsigned __int8 *)(v_rsi + 45) = 0;
loc_005581CC:
    if (((*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 12)) & (2)) != 0) {
        *(unsigned __int8 *)(v_rsi + 14) = (unsigned __int8)(v_rbp + 1);
    }
    v_rbp = (unsigned int)((v_rbp) + ((unsigned int)(v_rbp + 1)));
    goto loc_005583BB;
loc_005581E1:
    v_stack_p10 = 0xC000000DULL;
    goto loc_00558038;
loc_005581EE:
    if (((unsigned __int8)((unsigned int)((unsigned int)(v_rbp + 1)))) != 3) goto loc_00558238;
    if (((unsigned __int8)(*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 76))) != 8) goto loc_00558238;
    result = HalpMmAllocateMemoryInternal(24, (unsigned int)((unsigned int)(v_rbp + 1)), a3, a4);
    if (result == 0) goto loc_005583CB;
    *(unsigned __int8 *)(result + 8) = 0;
    *(unsigned int *)(result + 16) = (unsigned int)(*(unsigned __int16 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 2));
    *(unsigned int *)(result + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 4)));
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(v_rip + 10716375);
    *(unsigned __int64 *)(v_rip + 10716365) = result;
    goto loc_005583BB;
loc_00558238:
    if (((unsigned __int8)((unsigned int)((unsigned int)(v_rbp + 1)))) != ((unsigned __int8)(a4))) goto loc_00558244;
    if (((unsigned __int8)(result)) == 6) goto loc_00558253;
loc_00558244:
    if (((unsigned __int8)((unsigned int)((unsigned int)(v_rbp + 1)))) != 10) goto loc_005582D0;
    if (((unsigned __int8)((unsigned __int8)(result))) != 12) goto loc_005582D0;
loc_00558253:
    result = HalpMmAllocateMemoryInternal(24, (unsigned int)((unsigned int)(v_rbp + 1)), a3, a4);
    if (result == 0) goto loc_005583CB;
    result = 0;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = 0;
    *(unsigned __int8 *)(result + 8) = (unsigned __int8)(v_rbp + 1);
    if ((*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1)) != ((unsigned __int8)(result + 4))) goto loc_005582A0;
    *(unsigned int *)(result + 12) = (unsigned int)(*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 2));
    if ((*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 2)) == 255) {
    }
    *(unsigned int *)(result + 16) = (unsigned int)(*(unsigned __int16 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 3));
    goto loc_005582B0;
loc_005582A0:
    *(unsigned int *)(result + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 4)));
    *(unsigned int *)(result + 16) = (unsigned int)(*(unsigned __int16 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 2));
loc_005582B0:
    result = (unsigned __int8)(-(*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 8)));
    result = (unsigned int)((result) + (-4));
    *(unsigned int *)(result + 20) = (unsigned int)(result);
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(v_rip + 10716223);
    *(unsigned __int64 *)(v_rip + 10716213) = result;
    goto loc_0055803D;
loc_005582D0:
    if (((unsigned __int8)((unsigned int)((unsigned int)(v_rbp + 1)))) != 2) goto loc_0055803D;
    if (((unsigned __int8)(result)) != 10) goto loc_0055803D;
    result = HalpInterruptGsiToLine((unsigned int)(*(unsigned int *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 4)), v_stack_p8, a3, result + 4);
    if (sign_flag) goto loc_005583B6;
    result = HalpMmAllocateMemoryInternal(40, (unsigned int)((unsigned int)(v_rbp + 1)), a3, result + 4);
    if (result == 0) goto loc_005583CB;
    result = 0;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    *(unsigned __int64 *)(result + 32) = 0;
    if (((unsigned int)(*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 3))) >= 8) goto loc_00558332;
    goto loc_0055833A;
loc_00558332:
    result = (unsigned int)((*(unsigned __int8 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 3)) + (-8));
loc_0055833A:
    *(unsigned int *)(0 + 16) = (unsigned int)((unsigned int)(0xB001ULL));
    *(unsigned int *)(result + 20) = (unsigned int)(result);
    *(unsigned __int64 *)(result + 24) = v_stack_p8;
    result = (unsigned __int16)((*(unsigned __int16 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 8)) & (3));
    if (condition_is_equal) goto loc_0055835D;
    result = 2;
    if (((unsigned __int16)(result)) == ((unsigned __int16)(v_rbp + 1))) {
        result = (unsigned int)(v_rbp + 1);
    }
    *(unsigned int *)(36 + result * 1) = (unsigned int)(result);
    result = (unsigned __int16)((*(unsigned __int16 *)(a1 + 44 + *(unsigned __int8 *)(a1 + 44 + 1) * 1 + 8)) & (12));
    if (condition_is_equal) goto loc_00558383;
    if (((unsigned __int16)(result)) == ((unsigned __int16)(36 - 32))) goto loc_00558383;
    result = 0;
    goto loc_00558385;
loc_00558383:
loc_00558385:
    *(unsigned int *)(32 + result * 1) = (unsigned int)((unsigned int)((unsigned int)(v_rbp + 1)));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10715976))) != (v_rip + 10715979)) goto loc_005583C6;
    *(unsigned __int64 *)(result) = v_rip + 10715979;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(v_rip + 10715976);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10715976)) = 0;
    *(unsigned __int64 *)(v_rip + 10715954) = 0;
loc_005583B6:
loc_005583BB:
    goto loc_0055803D;
loc_005583C6:
loc_005583CB:
    goto loc_0055866E;
loc_005583D5:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9141796)))) <= ((unsigned int)(v_rbp + 1))) goto loc_0055866A;
    a3 = 0;
loc_005583EF:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9141796))))) goto loc_00558413;
    a2 = (0) << (6);
    if ((*(unsigned int *)(a2 + *(unsigned __int64 *)(v_rip + 10926645) * 1 + 8)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9141772)))))) goto loc_00558410;
    a3 = (unsigned int)((a3) + ((unsigned int)(v_rbp + 1)));
    goto loc_005583EF;
loc_00558410:
loc_00558413:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 164))) - ((unsigned int)(v_rbp + 1)));
    a3 = (unsigned int)(~(a3));
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 160))) * (*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 164)));
    v_rsi = (unsigned int)((v_rsi) - ((unsigned int)(v_rbp + 1)));
    v_rsi = (unsigned int)(~(v_rsi));
    v_rbp = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9141673)))) & ((unsigned int)(v_rsi)));
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9141673)))))) & (a3));
    result = *(unsigned __int64 *)(v_rip + 9141673);
    if ((unsigned int)((unsigned int)(a3)) != 0) {
        a1 = *(unsigned __int64 *)(v_rip + 10926535);
        result = (unsigned int)((unsigned int)(a3));
        result = (result) << (6);
        result = (result) + (a1);
        *(unsigned __int64 *)(a1) = v_xmm0;
        *(unsigned __int64 *)(a1 + 16) = v_xmm1;
        *(unsigned __int64 *)(a1 + 32) = v_xmm0;
        *(unsigned __int64 *)(a1 + 48) = v_xmm1;
        *(unsigned __int64 *)(result) = v_xmm2;
        *(unsigned __int64 *)(result + 16) = v_xmm3;
        *(unsigned __int64 *)(result + 32) = v_xmm4;
        *(unsigned __int64 *)(result + 48) = v_xmm5;
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9141579)))) <= ((unsigned int)(v_rbp + 1))) goto loc_005584DA;
    a2 = (*(unsigned __int64 *)(v_rip + 10926446)) + (72);
loc_005584C6:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) & (a3));
    if (((unsigned int)(result)) != ((unsigned int)(a4))) goto loc_005584DA;
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(v_rbp + 1))) + ((unsigned int)(v_rbp + 1)));
    a2 = (a2) + (64);
    if (((unsigned int)(v_rdi)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9141579))))) goto loc_005584C6;
loc_005584DA:
    if (((unsigned int)(v_rdi + 1)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9141579))))) goto loc_0055855A;
    a2 = ((unsigned int)((unsigned int)(v_rdi + 1))) << (6);
    a2 = (a2) + (*(unsigned __int64 *)(v_rip + 10926402));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9141579))) - ((unsigned int)(v_rdi + 1)));
loc_005584F3:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 8))) & (a3));
    if (((unsigned int)(result)) == ((unsigned int)(a4))) {
        result = *(unsigned __int64 *)(v_rip + 10926376);
        a1 = (unsigned int)(v_rdi);
        a1 = (a1) << (6);
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_rbp + 1)));
        *(unsigned __int64 *)(a1 + result * 1) = v_xmm0;
        *(unsigned __int64 *)(a1 + result * 1 + 16) = v_xmm1;
        *(unsigned __int64 *)(a1 + result * 1 + 32) = v_xmm0;
        *(unsigned __int64 *)(a1 + result * 1 + 48) = v_xmm1;
        *(unsigned __int64 *)(a2) = v_xmm2;
        *(unsigned __int64 *)(a2 + 16) = v_xmm3;
        *(unsigned __int64 *)(a2 + 32) = v_xmm4;
        *(unsigned __int64 *)(a2 + 48) = v_xmm5;
    }
    a2 = (a2) + (64);
    v_r10 = ((unsigned int)((unsigned int)(a1))) - (v_rbp + 1);
    if (condition_is_not_equal) goto loc_005584F3;
loc_0055855A:
    if (((unsigned int)(v_rdi)) >= = ((unsigned int)(v_rbp + 1))) {
        *(unsigned __int8 *)(v_rip + 10715540) = (unsigned __int8)(v_rbp + 1);
    }
    result = HalpInterruptSortProcessorTable(*(unsigned __int64 *)(v_rip + 10926277) + 64, v_rdi - 1, a3, a4);
    if (((unsigned int)(v_rdi)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9141379))))) goto loc_005585A3;
    a2 = ((unsigned int)((unsigned int)(v_rdi))) << (6);
    a2 = (a2) + (8);
    a2 = (a2) + (*(unsigned __int64 *)(v_rip + 10926277));
loc_00558591:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & (*(unsigned int *)(a2)));
    if (((unsigned int)(result)) != ((unsigned int)(v_rbp))) goto loc_005585A3;
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_rbp + 1)));
    a2 = (a2) + (64);
    if (((unsigned int)(v_rdi)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9141379))))) goto loc_00558591;
loc_005585A3:
    if (((unsigned int)(v_rdi + 1)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9141379))))) goto loc_00558621;
    a2 = ((unsigned int)((unsigned int)(v_rdi + 1))) << (6);
    a2 = (a2) + (*(unsigned __int64 *)(v_rip + 10926201));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9141379))) - ((unsigned int)(v_rdi + 1)));
loc_005585BC:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 8))) & ((unsigned int)(v_rsi)));
    if (((unsigned int)(result)) == ((unsigned int)(v_rbp))) {
        result = *(unsigned __int64 *)(v_rip + 10926177);
        a1 = (unsigned int)(v_rdi);
        a1 = (a1) << (6);
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_rbp + 1)));
        *(unsigned __int64 *)(a1 + result * 1) = v_xmm0;
        *(unsigned __int64 *)(a1 + result * 1 + 16) = v_xmm1;
        *(unsigned __int64 *)(a1 + result * 1 + 32) = v_xmm0;
        *(unsigned __int64 *)(a1 + result * 1 + 48) = v_xmm1;
        *(unsigned __int64 *)(a2) = v_xmm2;
        *(unsigned __int64 *)(a2 + 16) = v_xmm3;
        *(unsigned __int64 *)(a2 + 32) = v_xmm4;
        *(unsigned __int64 *)(a2 + 48) = v_xmm5;
    }
    a2 = (a2) + (64);
    a3 = ((unsigned int)((unsigned int)(a1))) - (v_rbp + 1);
    if (condition_is_not_equal) goto loc_005585BC;
loc_00558621:
    a1 = ((unsigned int)((unsigned int)(v_rdi))) << (6);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - ((unsigned int)((unsigned int)((unsigned int)(v_rdi)))));
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 10926076));
    result = HalpInterruptSortProcessorTable(a1, a2, a3, (unsigned int)((unsigned int)(v_rdi)));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9141185))) - ((unsigned int)(v_rdi)));
    a1 = ((unsigned int)((unsigned int)(v_rdi))) << (6);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip + 10926050));
    result = HalpInterruptSortProcessorTable(a1, a2, a3, (unsigned int)((unsigned int)(v_rdi)));
    if ((*(unsigned __int8 *)(v_rip + 10715294)) == 0) goto loc_0055866A;
    if ((*(unsigned __int8 *)(v_rip + 10715303)) != 0) {
        result = HalpInterruptBlockSmtSiblings(a1, a2, a3, (unsigned int)((unsigned int)(v_rdi)));
    }
loc_0055866E:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)(v_stack_p10);
}
```

## 5. (Beta) C Style

```c
int64_t HalpInterruptParseMadt(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (48);
    local_rbp = 0;
    local_r12 = ((uint32_t)(*(uint32_t *)(arg1 + 0x4))) + (Arg1);
    local_r13 = 0;
    Arg3 = 0;
    if (Arg2 != 0) goto loc_00558032;
    if ((Arg1 + 44 + 2) > local_r12) goto loc_00557F37;
loc_00557EBF:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x2C + 0x1))) < 2) goto loc_00557F37;
    if ((Arg1 + 44 + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1) > local_r12) goto loc_00557F37;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x2C)) != 0) goto loc_00557EE8;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x2C + 0x1))) != 8) goto loc_00557F2E;
    goto loc_00557F13;
loc_00557EE8:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x2C))) != 9) goto loc_00557EF6;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x2C + 0x1))) != 16) goto loc_00557F2E;
    goto loc_00557F13;
loc_00557EF6:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x2C))) != ((uint8_t)(local_rbp + 1))) goto loc_00557F07;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x2C + 0x1))) != 12) goto loc_00557F2E;
    goto loc_00557F2E;
loc_00557F07:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x2C))) != 11) goto loc_00557F2E;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x2C + 0x1))) < 40) goto loc_00557F2E;
loc_00557F13:
    if (((*(uint8_t *)(arg1 + 0x2C + 0xC)) & ((uint8_t)(local_rbp + 1))) != 0) {
    }
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(local_rbp + 1)));
    if (Arg3 >= = (*(uint32_t *)(v_rip + 0x8B82E7))) {
        *(uint32_t *)(v_rip + 0x8B82DE) = Arg3;
    }
    if ((Arg1 + 44 + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 2) <= local_r12) goto loc_00557EBF;
loc_00557F37:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA38787))) << (4));
    result = HalpMmAllocateMemoryInternal(Arg1, (uint32_t)((uint32_t)(local_rbp + 1)), Arg3, Arg1 + 44 + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1);
    *(uint64_t *)(v_rip + 0xA3875A) = result;
    if (result != 0) goto loc_00557F79;
    v_stack_m48 = 0x6B8ULL;
    Arg3 = 0;
    Arg1 = 0;
    result = HalpInterruptSetProblemEx(Arg1, result + 30, Arg3, v_rip - 5451450);
    goto loc_0055866E;
loc_00557F79:
    local_r10 = 0;
    Arg3 = ((uint32_t)(*(uint32_t *)(arg1 + 0x4))) + (0);
    if ((Arg1 + 44 + 2) > Arg3) goto loc_00557FDB;
loc_00557F88:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x2C + 0x1))) < 2) goto loc_00557FDB;
    if ((Arg1 + 44 + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1) > Arg3) goto loc_00557FDB;
    if ((*(uint8_t *)(arg1 + 0x2C)) != ((uint8_t)(local_rbp + 1))) goto loc_00557FD2;
    result = (uint32_t)(0xC0000017ULL);
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x2C + 0x1))) == 12) {
        result = *(uint8_t *)(arg1 + 0x2C + 0x2);
        Arg1 = *(uint64_t *)(v_rip + 0xA386F2);
        Arg2 = 0;
        Arg2 = (Arg2) + (Arg2);
        local_r10 = (uint32_t)((local_r10) + ((uint32_t)(local_rbp + 1)));
        *(uint32_t *)(arg1 + Arg2 * 8) = (uint32_t)(result);
        result = *(uint32_t *)(arg1 + 0x2C + 0x4);
        *(uint32_t *)(arg1 + Arg2 * 8 + 0x4) = (uint32_t)(result);
        result = *(uint32_t *)(arg1 + 0x2C + 0x8);
        *(uint32_t *)(arg1 + Arg2 * 8 + 0x8) = (uint32_t)(result);
    }
    if ((Arg1 + 44 + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 2) <= Arg3) goto loc_00557F88;
loc_00557FDB:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA386E3))) == 0) goto loc_0055866A;
    result = (*(uint64_t *)(v_rip + 0xA386B8)) + (12);
loc_00557FFE:
loc_0055800B:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA386B8) + 0x8)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(result - 0x4))))) goto loc_0055801B;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA386B8) + 0x8))) - ((uint32_t)((uint32_t)(*(uint32_t *)(result - 0x4)))));
    if (((uint32_t)(Arg1)) < (*(uint32_t *)(result))) {
        *(uint32_t *)(result) = (uint32_t)(Arg1);
    }
    Arg2 = (*(uint64_t *)(v_rip + 0xA386B8) + 8) + (16);
    a4 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA386E3))))) - (local_rbp + 1);
    if (condition_is_not_equal) goto loc_0055800B;
    result = (result) + (16);
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA386E3))))) - (local_rbp + 1);
    if (condition_is_not_equal) goto loc_00557FFE;
    goto loc_0055866A;
loc_00558032:
loc_00558038:
loc_0055803D:
    if ((Arg1 + 44 + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 2) > local_r12) goto loc_005583D5;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x1))) < 2) goto loc_005583D5;
    if ((Arg1 + 44 + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + *(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x1) * 1) > local_r12) goto loc_005583D5;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1)) != 0) goto loc_005580A0;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x1))) != 8) goto loc_005580A0;
    Arg1 = ((uint32_t)((uint32_t)(Arg1 + 44 + 2))) << (6);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xA6BDA8));
    if (((*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x4)) & ((uint8_t)(local_rbp + 1))) == 0) goto loc_0055803D;
    *(uint32_t *)(arg1) = (uint32_t)(*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x3));
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)(*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x2));
    goto loc_005580D0;
loc_005580A0:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1))) != 9) goto loc_005580DA;
    if (((uint8_t)(Arg1)) != 16) goto loc_005580DA;
    Arg1 = ((uint32_t)((uint32_t)(Arg1 + 44 + 2))) << (6);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xA6BD77));
    if (((*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x8)) & ((uint8_t)(local_rbp + 1))) == 0) goto loc_0055803D;
    *(uint32_t *)(arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x4)));
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0xC)));
loc_005580D0:
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x4)));
    local_rbp = (uint32_t)((Arg1 + 44 + 2) + ((uint32_t)(local_rbp + 1)));
    goto loc_0055803D;
loc_005580DA:
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1))) != 11) goto loc_005581EE;
    if (((uint8_t)(Arg1)) < 40) goto loc_005581EE;
    if ((*(uint32_t *)(v_rip + 0xA6BD5C)) < 3) goto loc_005580FF;
    if (((uint8_t)(Arg1)) < 76) goto loc_005581EE;
loc_005580FF:
    local_rsi = ((uint32_t)((uint32_t)(local_rbp))) << (6);
    local_rsi = (local_rsi) + (*(uint64_t *)(v_rip + 0xA6BD24));
    if (((*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0xC)) & ((uint8_t)(local_rbp + 1))) == 0) goto loc_00558038;
    if ((*(uint32_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x10)) != ((uint32_t)(local_rbp + 1))) goto loc_005581E1;
    if (*(uint64_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x18) == 0) goto loc_005581E1;
    Arg3 = 0;
    v_stack_m48 = 4;
    a4 = 0;
    *(uint64_t *)(local_rsi + 0x18) = *(uint64_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x18);
    result = HalpMap(*(uint64_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x18), (uint32_t)((uint32_t)(local_rbp + 1)), Arg3, a4);
    *(uint64_t *)(local_rsi + 0x20) = result;
    result = -(result);
    a4 = (uint32_t)(~(a4));
    a4 = (uint32_t)((a4) & (0xC000009AULL));
    v_stack_p10 = (uint32_t)(a4);
    if (result == 0) goto loc_005583CB;
    if ((*(uint32_t *)(v_rip + 0xA6BCDE)) < 3) goto loc_0055818E;
    Arg1 = (*(uint64_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x44)) >> (8);
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) ^ (*(uint32_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x44)));
    result = (uint32_t)((result) & (0xFFFFFFULL));
    result = (uint32_t)((result) ^ ((uint32_t)(Arg1)));
    *(uint32_t *)(local_rsi) = (uint32_t)(result);
    result = 0;
    goto loc_00558196;
loc_0055818E:
    *(uint32_t *)(local_rsi) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x4)));
loc_00558196:
    *(uint32_t *)(local_rsi + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x4)));
    *(uint32_t *)(local_rsi + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x8)));
    *(uint32_t *)(local_rsi + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x14)));
    if ((*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x1)) < 76) goto loc_005581C4;
    *(uint64_t *)(local_rsi + 0x30) = *(uint64_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x44);
    *(uint8_t *)(local_rsi + 0x2D) = (uint8_t)(local_rbp + 1);
    if ((*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x1)) < 77) goto loc_005581CC;
    *(uint8_t *)(local_rsi + 0x2C) = (uint8_t)(*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x4C));
    goto loc_005581CC;
loc_005581C4:
    *(uint8_t *)(local_rsi + 0x2D) = 0;
loc_005581CC:
    if (((*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0xC)) & (2)) != 0) {
        *(uint8_t *)(local_rsi + 0xE) = (uint8_t)(local_rbp + 1);
    }
    local_rbp = (uint32_t)((local_rbp) + ((uint32_t)(local_rbp + 1)));
    goto loc_005583BB;
loc_005581E1:
    v_stack_p10 = 0xC000000DULL;
    goto loc_00558038;
loc_005581EE:
    if (((uint8_t)((uint32_t)((uint32_t)(local_rbp + 1)))) != 3) goto loc_00558238;
    if (((uint8_t)(*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x4C))) != 8) goto loc_00558238;
    result = HalpMmAllocateMemoryInternal(24, (uint32_t)((uint32_t)(local_rbp + 1)), Arg3, a4);
    if (result == 0) goto loc_005583CB;
    *(uint8_t *)(result + 0x8) = 0;
    *(uint32_t *)(result + 0x10) = (uint32_t)(*(uint16_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x2));
    *(uint32_t *)(result + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x4)));
    *(uint64_t *)(result) = *(uint64_t *)(v_rip + 0xA384D7);
    *(uint64_t *)(v_rip + 0xA384CD) = result;
    goto loc_005583BB;
loc_00558238:
    if (((uint8_t)((uint32_t)((uint32_t)(local_rbp + 1)))) != ((uint8_t)(a4))) goto loc_00558244;
    if (((uint8_t)(result)) == 6) goto loc_00558253;
loc_00558244:
    if (((uint8_t)((uint32_t)((uint32_t)(local_rbp + 1)))) != 10) goto loc_005582D0;
    if (((uint8_t)((uint8_t)(result))) != 12) goto loc_005582D0;
loc_00558253:
    result = HalpMmAllocateMemoryInternal(24, (uint32_t)((uint32_t)(local_rbp + 1)), Arg3, a4);
    if (result == 0) goto loc_005583CB;
    result = 0;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = 0;
    *(uint8_t *)(result + 0x8) = (uint8_t)(local_rbp + 1);
    if ((*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1)) != ((uint8_t)(result + 4))) goto loc_005582A0;
    *(uint32_t *)(result + 0xC) = (uint32_t)(*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x2));
    if ((*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x2)) == 255) {
    }
    *(uint32_t *)(result + 0x10) = (uint32_t)(*(uint16_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x3));
    goto loc_005582B0;
loc_005582A0:
    *(uint32_t *)(result + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x4)));
    *(uint32_t *)(result + 0x10) = (uint32_t)(*(uint16_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x2));
loc_005582B0:
    result = (uint8_t)(-(*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x8)));
    result = (uint32_t)((result) + (-4));
    *(uint32_t *)(result + 0x14) = (uint32_t)(result);
    *(uint64_t *)(result) = *(uint64_t *)(v_rip + 0xA3843F);
    *(uint64_t *)(v_rip + 0xA38435) = result;
    goto loc_0055803D;
loc_005582D0:
    if (((uint8_t)((uint32_t)((uint32_t)(local_rbp + 1)))) != 2) goto loc_0055803D;
    if (((uint8_t)(result)) != 10) goto loc_0055803D;
    result = HalpInterruptGsiToLine((uint32_t)(*(uint32_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x4)), v_stack_p8, Arg3, result + 4);
    if (sign_flag) goto loc_005583B6;
    result = HalpMmAllocateMemoryInternal(40, (uint32_t)((uint32_t)(local_rbp + 1)), Arg3, result + 4);
    if (result == 0) goto loc_005583CB;
    result = 0;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    *(uint64_t *)(result + 0x20) = 0;
    if (((uint32_t)(*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x3))) >= 8) goto loc_00558332;
    goto loc_0055833A;
loc_00558332:
    result = (uint32_t)((*(uint8_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x3)) + (-8));
loc_0055833A:
    *(uint32_t *)(0 + 0x10) = (uint32_t)((uint32_t)(0xB001ULL));
    *(uint32_t *)(result + 0x14) = (uint32_t)(result);
    *(uint64_t *)(result + 0x18) = v_stack_p8;
    result = (uint16_t)((*(uint16_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x8)) & (3));
    if (condition_is_equal) goto loc_0055835D;
    result = 2;
    if (((uint16_t)(result)) == ((uint16_t)(local_rbp + 1))) {
        result = (uint32_t)(local_rbp + 1);
    }
    *(uint32_t *)(36 + result * 1) = (uint32_t)(result);
    result = (uint16_t)((*(uint16_t *)(arg1 + 0x2C + *(uint8_t *)(arg1 + 0x2C + 0x1) * 1 + 0x8)) & (12));
    if (condition_is_equal) goto loc_00558383;
    if (((uint16_t)(result)) == ((uint16_t)(36 - 32))) goto loc_00558383;
    result = 0;
    goto loc_00558385;
loc_00558383:
loc_00558385:
    *(uint32_t *)(32 + result * 1) = (uint32_t)((uint32_t)((uint32_t)(local_rbp + 1)));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA38348))) != (v_rip + 10715979)) goto loc_005583C6;
    *(uint64_t *)(result) = v_rip + 10715979;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(v_rip + 0xA38348);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0xA38348)) = 0;
    *(uint64_t *)(v_rip + 0xA38332) = 0;
loc_005583B6:
loc_005583BB:
    goto loc_0055803D;
loc_005583C6:
loc_005583CB:
    goto loc_0055866E;
loc_005583D5:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8B7E24)))) <= ((uint32_t)(local_rbp + 1))) goto loc_0055866A;
    Arg3 = 0;
loc_005583EF:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8B7E24))))) goto loc_00558413;
    Arg2 = (0) << (6);
    if ((*(uint32_t *)(Arg2 + *(uint64_t *)(v_rip + 0xA6BA35) * 1 + 0x8)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8B7E0C)))))) goto loc_00558410;
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(local_rbp + 1)));
    goto loc_005583EF;
loc_00558410:
loc_00558413:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA4))) - ((uint32_t)(local_rbp + 1)));
    Arg3 = (uint32_t)(~(Arg3));
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA0))) * (*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xA4)));
    local_rsi = (uint32_t)((local_rsi) - ((uint32_t)(local_rbp + 1)));
    local_rsi = (uint32_t)(~(local_rsi));
    local_rbp = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8B7DA9)))) & ((uint32_t)(local_rsi)));
    a4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8B7DA9)))))) & (Arg3));
    result = *(uint64_t *)(v_rip + 0x8B7DA9);
    if ((uint32_t)((uint32_t)(Arg3)) != 0) {
        Arg1 = *(uint64_t *)(v_rip + 0xA6B9C7);
        result = (uint32_t)((uint32_t)(Arg3));
        result = (result) << (6);
        result = (result) + (Arg1);
        *(uint64_t *)(arg1) = v_xmm0;
        *(uint64_t *)(arg1 + 0x10) = v_xmm1;
        *(uint64_t *)(arg1 + 0x20) = v_xmm0;
        *(uint64_t *)(arg1 + 0x30) = v_xmm1;
        *(uint64_t *)(result) = v_xmm2;
        *(uint64_t *)(result + 0x10) = v_xmm3;
        *(uint64_t *)(result + 0x20) = v_xmm4;
        *(uint64_t *)(result + 0x30) = v_xmm5;
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8B7D4B)))) <= ((uint32_t)(local_rbp + 1))) goto loc_005584DA;
    Arg2 = (*(uint64_t *)(v_rip + 0xA6B96E)) + (72);
loc_005584C6:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2))) & (Arg3));
    if (((uint32_t)(result)) != ((uint32_t)(a4))) goto loc_005584DA;
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(local_rbp + 1))) + ((uint32_t)(local_rbp + 1)));
    Arg2 = (Arg2) + (64);
    if (((uint32_t)(local_rdi)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8B7D4B))))) goto loc_005584C6;
loc_005584DA:
    if (((uint32_t)(local_rdi + 1)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8B7D4B))))) goto loc_0055855A;
    Arg2 = ((uint32_t)((uint32_t)(local_rdi + 1))) << (6);
    Arg2 = (Arg2) + (*(uint64_t *)(v_rip + 0xA6B942));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x8B7D4B))) - ((uint32_t)(local_rdi + 1)));
loc_005584F3:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + 0x8))) & (Arg3));
    if (((uint32_t)(result)) == ((uint32_t)(a4))) {
        result = *(uint64_t *)(v_rip + 0xA6B928);
        Arg1 = (uint32_t)(local_rdi);
        Arg1 = (Arg1) << (6);
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_rbp + 1)));
        *(uint64_t *)(arg1 + result * 1) = v_xmm0;
        *(uint64_t *)(arg1 + result * 1 + 0x10) = v_xmm1;
        *(uint64_t *)(arg1 + result * 1 + 0x20) = v_xmm0;
        *(uint64_t *)(arg1 + result * 1 + 0x30) = v_xmm1;
        *(uint64_t *)(Arg2) = v_xmm2;
        *(uint64_t *)(Arg2 + 0x10) = v_xmm3;
        *(uint64_t *)(Arg2 + 0x20) = v_xmm4;
        *(uint64_t *)(Arg2 + 0x30) = v_xmm5;
    }
    Arg2 = (Arg2) + (64);
    local_r10 = ((uint32_t)((uint32_t)(Arg1))) - (local_rbp + 1);
    if (condition_is_not_equal) goto loc_005584F3;
loc_0055855A:
    if (((uint32_t)(local_rdi)) >= = ((uint32_t)(local_rbp + 1))) {
        *(uint8_t *)(v_rip + 0xA38194) = (uint8_t)(local_rbp + 1);
    }
    result = HalpInterruptSortProcessorTable(*(uint64_t *)(v_rip + 0xA6B8C5) + 64, local_rdi - 1, Arg3, a4);
    if (((uint32_t)(local_rdi)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8B7C83))))) goto loc_005585A3;
    Arg2 = ((uint32_t)((uint32_t)(local_rdi))) << (6);
    Arg2 = (Arg2) + (8);
    Arg2 = (Arg2) + (*(uint64_t *)(v_rip + 0xA6B8C5));
loc_00558591:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & (*(uint32_t *)(Arg2)));
    if (((uint32_t)(result)) != ((uint32_t)(local_rbp))) goto loc_005585A3;
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_rbp + 1)));
    Arg2 = (Arg2) + (64);
    if (((uint32_t)(local_rdi)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8B7C83))))) goto loc_00558591;
loc_005585A3:
    if (((uint32_t)(local_rdi + 1)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8B7C83))))) goto loc_00558621;
    Arg2 = ((uint32_t)((uint32_t)(local_rdi + 1))) << (6);
    Arg2 = (Arg2) + (*(uint64_t *)(v_rip + 0xA6B879));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x8B7C83))) - ((uint32_t)(local_rdi + 1)));
loc_005585BC:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + 0x8))) & ((uint32_t)(local_rsi)));
    if (((uint32_t)(result)) == ((uint32_t)(local_rbp))) {
        result = *(uint64_t *)(v_rip + 0xA6B861);
        Arg1 = (uint32_t)(local_rdi);
        Arg1 = (Arg1) << (6);
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_rbp + 1)));
        *(uint64_t *)(arg1 + result * 1) = v_xmm0;
        *(uint64_t *)(arg1 + result * 1 + 0x10) = v_xmm1;
        *(uint64_t *)(arg1 + result * 1 + 0x20) = v_xmm0;
        *(uint64_t *)(arg1 + result * 1 + 0x30) = v_xmm1;
        *(uint64_t *)(Arg2) = v_xmm2;
        *(uint64_t *)(Arg2 + 0x10) = v_xmm3;
        *(uint64_t *)(Arg2 + 0x20) = v_xmm4;
        *(uint64_t *)(Arg2 + 0x30) = v_xmm5;
    }
    Arg2 = (Arg2) + (64);
    Arg3 = ((uint32_t)((uint32_t)(Arg1))) - (local_rbp + 1);
    if (condition_is_not_equal) goto loc_005585BC;
loc_00558621:
    Arg1 = ((uint32_t)((uint32_t)(local_rdi))) << (6);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - ((uint32_t)((uint32_t)((uint32_t)(local_rdi)))));
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xA6B7FC));
    result = HalpInterruptSortProcessorTable(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)(local_rdi)));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x8B7BC1))) - ((uint32_t)(local_rdi)));
    Arg1 = ((uint32_t)((uint32_t)(local_rdi))) << (6);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip + 0xA6B7E2));
    result = HalpInterruptSortProcessorTable(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)(local_rdi)));
    if ((*(uint8_t *)(v_rip + 0xA3809E)) == 0) goto loc_0055866A;
    if ((*(uint8_t *)(v_rip + 0xA380A7)) != 0) {
        result = HalpInterruptBlockSmtSiblings(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)(local_rdi)));
    }
loc_0055866E:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)(v_stack_p10);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2` | `64` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x2C` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00557E74&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
