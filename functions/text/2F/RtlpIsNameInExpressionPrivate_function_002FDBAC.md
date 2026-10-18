# RtlpIsNameInExpressionPrivate

- RVA: `0x002FDBAC`–`0x002FE0A8` (길이 `1,276` bytes)
- VA: `0x00000001402FDBAC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00072CF0`
- 디코드: `319`개 명령, `1,276/1,276` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x002FDE74` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002FDF5A` → [RtlDoesNameContainWildCards](../41/RtlDoesNameContainWildCards_function_0041EC60.md) (function, `0x0041EC60`)
- `0x002FDFC1` → [memcmp](../6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x002FE07A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x002FE091` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [RtlIsNameInExpression](RtlIsNameInExpression_function_002FDA70.md) at `0x002FDAB3`
- [RtlIsNameInUnUpcasedExpression](RtlIsNameInUnUpcasedExpression_function_002FDAF0.md) at `0x002FDB67`

### Static image references
- `0x002FDBCB` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x002FE07A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x002FE091` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x002FDD23` → [sub_006DFD60 + 0x12](../6D/Unknown_function_006DFD60.md) (`tail-transfer`)
  - `0x002FE032` → [sub_006DFD60](../6D/Unknown_function_006DFD60.md) (`tail-transfer`)
  - `0x002FE03D` → [sub_006DFD60](../6D/Unknown_function_006DFD60.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002FDBAC  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
002FDBB1  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
002FDBB6  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
002FDBBB  57                              push rdi
002FDBBC  41 54                           push r12
002FDBBE  41 55                           push r13
002FDBC0  41 56                           push r14
002FDBC2  41 57                           push r15
002FDBC4  48 81 EC C0 00 00 00            sub rsp, 0xc0
002FDBCB  48 8B 05 6E CB B0 00            mov rax, qword ptr [rip + 0xb0cb6e]
002FDBD2  48 33 C4                        xor rax, rsp
002FDBD5  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
002FDBDD  0F B7 32                        movzx esi, word ptr [rdx]
002FDBE0  45 33 ED                        xor r13d, r13d
002FDBE3  44 88 4C 24 24                  mov byte ptr [rsp + 0x24], r9b
002FDBE8  45 8A E1                        mov r12b, r9b
002FDBEB  44 88 44 24 21                  mov byte ptr [rsp + 0x21], r8b
002FDBF0  45 8A F8                        mov r15b, r8b
002FDBF3  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
002FDBF8  4C 8B D2                        mov r10, rdx
002FDBFB  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
002FDC00  4C 8B C9                        mov r9, rcx
002FDC03  66 44 89 6C 24 22               mov word ptr [rsp + 0x22], r13w
002FDC09  45 8B C5                        mov r8d, r13d
002FDC0C  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
002FDC11  45 8A F5                        mov r14b, r13b
002FDC14  44 88 6C 24 20                  mov byte ptr [rsp + 0x20], r13b
002FDC19  66 85 F6                        test si, si
002FDC1C  0F 84 79 04 00 00               je 0x1402fe09b
002FDC22  0F B7 29                        movzx ebp, word ptr [rcx]
002FDC25  66 85 ED                        test bp, bp
002FDC28  0F 84 6D 04 00 00               je 0x1402fe09b
002FDC2E  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
002FDC32  41 8D 7D 01                     lea edi, [r13 + 1]
002FDC36  8D 4F 01                        lea ecx, [rdi + 1]
002FDC39  66 3B E9                        cmp bp, cx
002FDC3C  0F 84 65 03 00 00               je 0x1402fdfa7
002FDC42  66 83 38 2A                     cmp word ptr [rax], 0x2a
002FDC46  0F 84 D9 02 00 00               je 0x1402fdf25
002FDC4C  B8 FF 7F 00 00                  mov eax, 0x7fff
002FDC51  66 44 89 6C 24 70               mov word ptr [rsp + 0x70], r13w
002FDC57  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
002FDC5C  8B D7                           mov edx, edi
002FDC5E  4C 89 5C 24 38                  mov qword ptr [rsp + 0x38], r11
002FDC63  41 0F B7 DD                     movzx ebx, r13w
002FDC67  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
002FDC6B  4C 8D BC 24 90 00 00 00         lea r15, [rsp + 0x90]
002FDC73  66 89 5C 24 26                  mov word ptr [rsp + 0x26], bx
002FDC78  66 3B E8                        cmp bp, ax
002FDC7B  0F 87 6D 02 00 00               ja 0x1402fdeee
002FDC81  66 03 ED                        add bp, bp
002FDC84  45 84 F6                        test r14b, r14b
002FDC87  0F 85 F7 03 00 00               jne 0x1402fe084
002FDC8D  66 41 3B 1A                     cmp bx, word ptr [r10]
002FDC91  0F 83 A8 01 00 00               jae 0x1402fde3f
002FDC97  49 8B 42 08                     mov rax, qword ptr [r10 + 8]
002FDC9B  0F B7 CB                        movzx ecx, bx
002FDC9E  48 D1 E9                        shr rcx, 1
002FDCA1  66 83 C3 02                     add bx, 2
002FDCA5  66 89 5C 24 26                  mov word ptr [rsp + 0x26], bx
002FDCAA  0F B7 04 48                     movzx eax, word ptr [rax + rcx*2]
002FDCAE  66 89 44 24 22                  mov word ptr [rsp + 0x22], ax
002FDCB3  33 C9                           xor ecx, ecx
002FDCB5  8B D9                           mov ebx, ecx
002FDCB7  89 4C 24 2C                     mov dword ptr [rsp + 0x2c], ecx
002FDCBB  44 3B EA                        cmp r13d, edx
002FDCBE  0F 83 88 00 00 00               jae 0x1402fdd4c
002FDCC4  41 8B C5                        mov eax, r13d
002FDCC7  45 0F B7 24 43                  movzx r12d, word ptr [r11 + rax*2]
002FDCCC  0F B7 C1                        movzx eax, cx
002FDCCF  44 03 E7                        add r12d, edi
002FDCD2  41 D1 EC                        shr r12d, 1
002FDCD5  44 03 EF                        add r13d, edi
002FDCD8  41 0F B7 11                     movzx edx, word ptr [r9]
002FDCDC  66 44 3B E2                     cmp r12w, dx
002FDCE0  0F 84 E8 00 00 00               je 0x1402fddce
002FDCE6  BE 02 00 00 00                  mov esi, 2
002FDCEB  66 44 03 E0                     add r12w, ax
002FDCEF  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
002FDCF3  41 0F B7 F4                     movzx esi, r12w
002FDCF7  66 03 F6                        add si, si
002FDCFA  66 44 3B E2                     cmp r12w, dx
002FDCFE  0F 84 97 01 00 00               je 0x1402fde9b
002FDD04  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
002FDD08  41 0F B7 CC                     movzx ecx, r12w
002FDD0C  48 D1 E9                        shr rcx, 1
002FDD0F  44 0F B7 34 48                  movzx r14d, word ptr [rax + rcx*2]
002FDD14  33 C0                           xor eax, eax
002FDD16  38 44 24 21                     cmp byte ptr [rsp + 0x21], al
002FDD1A  0F 85 03 01 00 00               jne 0x1402fde23
002FDD20  83 FB 0E                        cmp ebx, 0xe
002FDD23  0F 83 49 20 3E 00               jae 0x1406dfd72
002FDD29  66 41 83 FE 2A                  cmp r14w, 0x2a
002FDD2E  75 45                           jne 0x1402fdd75
002FDD30  8B C3                           mov eax, ebx
002FDD32  03 DF                           add ebx, edi
002FDD34  66 41 89 34 47                  mov word ptr [r15 + rax*2], si
002FDD39  66 83 C6 03                     add si, 3
002FDD3D  66 41 89 34 5F                  mov word ptr [r15 + rbx*2], si
002FDD42  8B 44 24 28                     mov eax, dword ptr [rsp + 0x28]
002FDD46  03 DF                           add ebx, edi
002FDD48  33 C9                           xor ecx, ecx
002FDD4A  EB 8C                           jmp 0x1402fdcd8
002FDD4C  45 33 ED                        xor r13d, r13d
002FDD4F  85 DB                           test ebx, ebx
002FDD51  0F 84 8E 01 00 00               je 0x1402fdee5
002FDD57  49 8B C3                        mov rax, r11
002FDD5A  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
002FDD5F  4D 8B DF                        mov r11, r15
002FDD62  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
002FDD66  8B D3                           mov edx, ebx
002FDD68  4C 8B F8                        mov r15, rax
002FDD6B  0F B7 5C 24 26                  movzx ebx, word ptr [rsp + 0x26]
002FDD70  E9 0F FF FF FF                  jmp 0x1402fdc84
002FDD75  33 C9                           xor ecx, ecx
002FDD77  66 41 83 FE 3C                  cmp r14w, 0x3c
002FDD7C  0F 84 3B 01 00 00               je 0x1402fdebd
002FDD82  66 83 C6 04                     add si, 4
002FDD86  66 41 83 FE 3E                  cmp r14w, 0x3e
002FDD8B  0F 84 3C 02 00 00               je 0x1402fdfcd
002FDD91  66 41 83 FE 22                  cmp r14w, 0x22
002FDD96  0F 84 BB 02 00 00               je 0x1402fe057
002FDD9C  38 4C 24 20                     cmp byte ptr [rsp + 0x20], cl
002FDDA0  75 2C                           jne 0x1402fddce
002FDDA2  66 41 83 FE 3F                  cmp r14w, 0x3f
002FDDA7  0F 84 3A 02 00 00               je 0x1402fdfe7
002FDDAD  0F B7 4C 24 22                  movzx ecx, word ptr [rsp + 0x22]
002FDDB2  80 7C 24 21 00                  cmp byte ptr [rsp + 0x21], 0
002FDDB7  0F 85 EC 00 00 00               jne 0x1402fdea9
002FDDBD  66 44 3B F1                     cmp r14w, cx
002FDDC1  75 09                           jne 0x1402fddcc
002FDDC3  8B C3                           mov eax, ebx
002FDDC5  03 DF                           add ebx, edi
002FDDC7  66 41 89 34 47                  mov word ptr [r15 + rax*2], si
002FDDCC  33 C9                           xor ecx, ecx
002FDDCE  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
002FDDD2  44 8A 74 24 20                  mov r14b, byte ptr [rsp + 0x20]
002FDDD7  44 3B EA                        cmp r13d, edx
002FDDDA  0F 83 6C FF FF FF               jae 0x1402fdd4c
002FDDE0  8B 4C 24 2C                     mov ecx, dword ptr [rsp + 0x2c]
002FDDE4  44 8A 74 24 20                  mov r14b, byte ptr [rsp + 0x20]
002FDDE9  3B CB                           cmp ecx, ebx
002FDDEB  73 2F                           jae 0x1402fde1c
002FDDED  44 3B EA                        cmp r13d, edx
002FDDF0  73 1A                           jae 0x1402fde0c
002FDDF2  8B C1                           mov eax, ecx
002FDDF4  41 0F B7 0C 47                  movzx ecx, word ptr [r15 + rax*2]
002FDDF9  66 43 39 0C 6B                  cmp word ptr [r11 + r13*2], cx
002FDDFE  73 08                           jae 0x1402fde08
002FDE00  44 03 EF                        add r13d, edi
002FDE03  44 3B EA                        cmp r13d, edx
002FDE06  72 F1                           jb 0x1402fddf9
002FDE08  8B 4C 24 2C                     mov ecx, dword ptr [rsp + 0x2c]
002FDE0C  03 CF                           add ecx, edi
002FDE0E  89 4C 24 2C                     mov dword ptr [rsp + 0x2c], ecx
002FDE12  44 3B EA                        cmp r13d, edx
002FDE15  72 CD                           jb 0x1402fdde4
002FDE17  44 8A 74 24 20                  mov r14b, byte ptr [rsp + 0x20]
002FDE1C  33 C9                           xor ecx, ecx
002FDE1E  E9 98 FE FF FF                  jmp 0x1402fdcbb
002FDE23  38 44 24 24                     cmp byte ptr [rsp + 0x24], al
002FDE27  0F 84 F3 FE FF FF               je 0x1402fdd20
002FDE2D  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
002FDE35  46 0F B7 34 71                  movzx r14d, word ptr [rcx + r14*2]
002FDE3A  E9 E1 FE FF FF                  jmp 0x1402fdd20
002FDE3F  8D 4A FF                        lea ecx, [rdx - 1]
002FDE42  40 88 7C 24 20                  mov byte ptr [rsp + 0x20], dil
002FDE47  44 8A F7                        mov r14b, dil
002FDE4A  66 41 39 2C 4B                  cmp word ptr [r11 + rcx*2], bp
002FDE4F  0F 85 5E FE FF FF               jne 0x1402fdcb3
002FDE55  41 0F B7 1C 4B                  movzx ebx, word ptr [r11 + rcx*2]
002FDE5A  4D 85 C0                        test r8, r8
002FDE5D  0F 85 29 02 00 00               jne 0x1402fe08c
002FDE63  66 3B DD                        cmp bx, bp
002FDE66  0F 94 C0                        sete al
002FDE69  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
002FDE71  48 33 CC                        xor rcx, rsp
002FDE74  E8 C7 E7 3A 00                  call 0x1406ac640
002FDE79  4C 8D 9C 24 C0 00 00 00         lea r11, [rsp + 0xc0]
002FDE81  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
002FDE85  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
002FDE89  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
002FDE8D  49 8B E3                        mov rsp, r11
002FDE90  41 5F                           pop r15
002FDE92  41 5E                           pop r14
002FDE94  41 5D                           pop r13
002FDE96  41 5C                           pop r12
002FDE98  5F                              pop rdi
002FDE99  C3                              ret
002FDE9A  CC                              int3
002FDE9B  8B C3                           mov eax, ebx
002FDE9D  66 41 89 2C 47                  mov word ptr [r15 + rax*2], bp
002FDEA2  03 DF                           add ebx, edi
002FDEA4  E9 25 FF FF FF                  jmp 0x1402fddce
002FDEA9  0F B7 C1                        movzx eax, cx
002FDEAC  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
002FDEB4  0F B7 0C 41                     movzx ecx, word ptr [rcx + rax*2]
002FDEB8  E9 00 FF FF FF                  jmp 0x1402fddbd
002FDEBD  38 4C 24 20                     cmp byte ptr [rsp + 0x20], cl
002FDEC1  74 32                           je 0x1402fdef5
002FDEC3  4C 8B 4C 24 48                  mov r9, qword ptr [rsp + 0x48]
002FDEC8  8B C3                           mov eax, ebx
002FDECA  03 DF                           add ebx, edi
002FDECC  66 41 89 34 47                  mov word ptr [r15 + rax*2], si
002FDED1  66 83 C6 03                     add si, 3
002FDED5  66 41 89 34 5F                  mov word ptr [r15 + rbx*2], si
002FDEDA  03 DF                           add ebx, edi
002FDEDC  8B 44 24 28                     mov eax, dword ptr [rsp + 0x28]
002FDEE0  E9 F3 FD FF FF                  jmp 0x1402fdcd8
002FDEE5  4D 85 C0                        test r8, r8
002FDEE8  0F 85 87 01 00 00               jne 0x1402fe075
002FDEEE  32 C0                           xor al, al
002FDEF0  E9 74 FF FF FF                  jmp 0x1402fde69
002FDEF5  66 83 7C 24 22 2E               cmp word ptr [rsp + 0x22], 0x2e
002FDEFB  75 C6                           jne 0x1402fdec3
002FDEFD  0F B7 54 24 26                  movzx edx, word ptr [rsp + 0x26]
002FDF02  45 0F B7 0A                     movzx r9d, word ptr [r10]
002FDF06  66 41 3B D1                     cmp dx, r9w
002FDF0A  0F 82 E3 00 00 00               jb 0x1402fdff3
002FDF10  4C 8B 4C 24 48                  mov r9, qword ptr [rsp + 0x48]
002FDF15  66 83 C6 03                     add si, 3
002FDF19  8B C3                           mov eax, ebx
002FDF1B  66 41 89 34 47                  mov word ptr [r15 + rax*2], si
002FDF20  E9 1D FE FF FF                  jmp 0x1402fdd42
002FDF25  41 0F 10 01                     movups xmm0, xmmword ptr [r9]
002FDF29  4C 8D 70 02                     lea r14, [rax + 2]
002FDF2D  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
002FDF32  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
002FDF37  0F B7 5C 24 58                  movzx ebx, word ptr [rsp + 0x58]
002FDF3C  66 2B D9                        sub bx, cx
002FDF3F  48 C1 E8 10                     shr rax, 0x10
002FDF43  66 2B C1                        sub ax, cx
002FDF46  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
002FDF4B  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
002FDF50  66 89 44 24 5A                  mov word ptr [rsp + 0x5a], ax
002FDF55  66 89 5C 24 58                  mov word ptr [rsp + 0x58], bx
002FDF5A  E8 01 0D 12 00                  call 0x14041ec60
002FDF5F  84 C0                           test al, al
002FDF61  0F 85 DB 00 00 00               jne 0x1402fe042
002FDF67  66 83 ED 02                     sub bp, 2
002FDF6B  66 3B F5                        cmp si, bp
002FDF6E  0F 82 7A FF FF FF               jb 0x1402fdeee
002FDF74  4C 8B 5C 24 40                  mov r11, qword ptr [rsp + 0x40]
002FDF79  4C 8B CE                        mov r9, rsi
002FDF7C  44 0F B7 C3                     movzx r8d, bx
002FDF80  4D 2B C8                        sub r9, r8
002FDF83  49 D1 E9                        shr r9, 1
002FDF86  45 84 FF                        test r15b, r15b
002FDF89  74 28                           je 0x1402fdfb3
002FDF8B  4C 8B 84 24 10 01 00 00         mov r8, qword ptr [rsp + 0x110]
002FDF93  41 0F B7 D5                     movzx edx, r13w
002FDF97  66 D1 EB                        shr bx, 1
002FDF9A  66 3B D3                        cmp dx, bx
002FDF9D  72 75                           jb 0x1402fe014
002FDF9F  40 8A C7                        mov al, dil
002FDFA2  E9 C2 FE FF FF                  jmp 0x1402fde69
002FDFA7  66 83 38 2A                     cmp word ptr [rax], 0x2a
002FDFAB  0F 85 9B FC FF FF               jne 0x1402fdc4c
002FDFB1  EB EC                           jmp 0x1402fdf9f
002FDFB3  49 8B 53 08                     mov rdx, qword ptr [r11 + 8]
002FDFB7  49 8B CE                        mov rcx, r14
002FDFBA  41 8B C1                        mov eax, r9d
002FDFBD  48 8D 14 42                     lea rdx, [rdx + rax*2]
002FDFC1  E8 4A 8B 3C 00                  call 0x1406c6b10
002FDFC6  85 C0                           test eax, eax
002FDFC8  E9 99 FE FF FF                  jmp 0x1402fde66
002FDFCD  8B 44 24 28                     mov eax, dword ptr [rsp + 0x28]
002FDFD1  38 4C 24 20                     cmp byte ptr [rsp + 0x20], cl
002FDFD5  0F 85 FD FC FF FF               jne 0x1402fdcd8
002FDFDB  66 83 7C 24 22 2E               cmp word ptr [rsp + 0x22], 0x2e
002FDFE1  0F 84 F5 FE FF FF               je 0x1402fdedc
002FDFE7  8B C3                           mov eax, ebx
002FDFE9  66 41 89 34 47                  mov word ptr [r15 + rax*2], si
002FDFEE  E9 AF FE FF FF                  jmp 0x1402fdea2
002FDFF3  49 8B 42 08                     mov rax, qword ptr [r10 + 8]
002FDFF7  0F B7 CA                        movzx ecx, dx
002FDFFA  48 D1 E9                        shr rcx, 1
002FDFFD  66 83 3C 48 2E                  cmp word ptr [rax + rcx*2], 0x2e
002FE002  74 09                           je 0x1402fe00d
002FE004  66 83 C2 02                     add dx, 2
002FE008  E9 F9 FE FF FF                  jmp 0x1402fdf06
002FE00D  33 C9                           xor ecx, ecx
002FE00F  E9 AF FE FF FF                  jmp 0x1402fdec3
002FE014  49 8B 43 08                     mov rax, qword ptr [r11 + 8]
002FE018  0F B7 CA                        movzx ecx, dx
002FE01B  41 03 C9                        add ecx, r9d
002FE01E  0F B7 0C 48                     movzx ecx, word ptr [rax + rcx*2]
002FE022  0F B7 C2                        movzx eax, dx
002FE025  45 0F B7 14 48                  movzx r10d, word ptr [r8 + rcx*2]
002FE02A  41 0F B7 0C 46                  movzx ecx, word ptr [r14 + rax*2]
002FE02F  45 84 E4                        test r12b, r12b
002FE032  0F 84 28 1D 3E 00               je 0x1406dfd60
002FE038  41 0F B7 0C 48                  movzx ecx, word ptr [r8 + rcx*2]
002FE03D  E9 1E 1D 3E 00                  jmp 0x1406dfd60
002FE042  4C 8B 4C 24 48                  mov r9, qword ptr [rsp + 0x48]
002FE047  4D 8B C5                        mov r8, r13
002FE04A  4C 8B 54 24 40                  mov r10, qword ptr [rsp + 0x40]
002FE04F  45 8A F0                        mov r14b, r8b
002FE052  E9 F5 FB FF FF                  jmp 0x1402fdc4c
002FE057  38 4C 24 20                     cmp byte ptr [rsp + 0x20], cl
002FE05B  0F 85 7B FE FF FF               jne 0x1402fdedc
002FE061  0F B7 4C 24 22                  movzx ecx, word ptr [rsp + 0x22]
002FE066  66 83 F9 2E                     cmp cx, 0x2e
002FE06A  0F 85 42 FD FF FF               jne 0x1402fddb2
002FE070  E9 4E FD FF FF                  jmp 0x1402fddc3
002FE075  33 D2                           xor edx, edx
002FE077  49 8B C8                        mov rcx, r8
002FE07A  E8 F1 47 88 00                  call 0x140b82870
002FE07F  E9 6A FE FF FF                  jmp 0x1402fdeee
002FE084  8D 4A FF                        lea ecx, [rdx - 1]
002FE087  E9 C9 FD FF FF                  jmp 0x1402fde55
002FE08C  33 D2                           xor edx, edx
002FE08E  49 8B C8                        mov rcx, r8
002FE091  E8 DA 47 88 00                  call 0x140b82870
002FE096  E9 C8 FD FF FF                  jmp 0x1402fde63
002FE09B  41 0F B7 01                     movzx eax, word ptr [r9]
002FE09F  8B CE                           mov ecx, esi
002FE0A1  03 C8                           add ecx, eax
002FE0A3  E9 BE FD FF FF                  jmp 0x1402fde66
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpIsNameInExpressionPrivate(__int64 a1, __int64 a2, unsigned __int8 a3, unsigned __int8 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int16 v_stack_m66;
    unsigned __int64 v_stack_m68;
    unsigned __int16 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m98;
    unsigned __int16 v_stack_m9A;
    unsigned __int16 v_stack_m9E;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned __int16 v_stack_mC2;
    unsigned __int8 v_stack_mC4;
    unsigned __int16 v_stack_mC6;
    unsigned __int8 v_stack_mC7;
    unsigned __int8 v_stack_mC8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 11586414)) ^ (v_rsp);
    v_stack_m38 = result;
    v_r13 = 0;
    v_stack_mC4 = a4;
    v_stack_mC7 = a3;
    v_stack_mA8 = a2;
    v_stack_mA0 = a1;
    v_stack_mC6 = 0;
    v_stack_mB0 = 0;
    v_stack_mC8 = 0;
    if ((unsigned __int16)(*(unsigned __int16 *)(a2)) == 0) goto loc_002FE09B;
    if ((unsigned __int16)(*(unsigned __int16 *)(a1)) == 0) goto loc_002FE09B;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1))) == ((unsigned __int16)(v_r13 + 1 + 1))) goto loc_002FDFA7;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8))) == 42) goto loc_002FDF25;
loc_002FDC4C:
    v_stack_m78 = 0;
    v_stack_mB0 = v_stack_m78;
    v_stack_mB8 = (unsigned int)((unsigned int)((unsigned int)(v_r13 + 1)));
    v_stack_mC2 = 0;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1))) > ((unsigned __int16)((unsigned int)(0x7FFFULL)))) goto loc_002FDEEE;
    v_rbp = (unsigned __int16)((*(unsigned __int16 *)(a1)) + ((unsigned __int16)(*(unsigned __int16 *)(a1))));
loc_002FDC84:
    if (0 != 0) goto loc_002FE084;
    if (0 >= (*(unsigned __int16 *)(a2))) goto loc_002FDE3F;
    a1 = (0) >> (1);
    v_rbx = (unsigned __int16)((0) + (2));
    v_stack_mC2 = (unsigned __int16)(v_rbx);
    v_stack_mC6 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 8) + a1 * 2));
loc_002FDCB3:
    a1 = 0;
    v_stack_mBC = 0;
loc_002FDCBB:
    if (0 >= ((unsigned int)((unsigned int)((unsigned int)(v_r13 + 1))))) goto loc_002FDD4C;
    v_r12 = (unsigned int)((*(unsigned __int16 *)(v_stack_m78 + 0 * 2)) + ((unsigned int)(v_r13 + 1)));
    v_r12 = (unsigned int)((v_r12) >> (1));
    v_r13 = (unsigned int)((v_r13) + ((unsigned int)(v_r13 + 1)));
loc_002FDCD8:
    if (((unsigned __int16)(v_r12)) == ((unsigned __int16)(*(unsigned __int16 *)(a1)))) goto loc_002FDDCE;
    v_r12 = (unsigned __int16)((v_r12) + (0));
    v_stack_mC0 = 2;
    v_rsi = (unsigned __int16)(((unsigned __int16)(v_r12)) + ((unsigned __int16)((unsigned __int16)(v_r12))));
    if (((unsigned __int16)(v_r12)) == ((unsigned __int16)(*(unsigned __int16 *)(a1)))) goto loc_002FDE9B;
    a1 = ((unsigned __int16)(v_r12)) >> (1);
    result = 0;
    if (v_stack_mC7 != 0) goto loc_002FDE23;
loc_002FDD20:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + a1 * 2))) != 42) goto loc_002FDD75;
    v_rbx = (unsigned int)((0) + ((unsigned int)(v_r13 + 1)));
    *(unsigned __int16 *)(v_stack_m58 + 0 * 2) = (unsigned __int16)(v_rsi);
    v_rsi = (unsigned __int16)((v_rsi) + (3));
    *(unsigned __int16 *)(v_stack_m58 + v_rbx * 2) = (unsigned __int16)(v_rsi);
loc_002FDD42:
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(v_r13 + 1)));
    a1 = 0;
    goto loc_002FDCD8;
loc_002FDD4C:
    v_r13 = 0;
    if ((unsigned int)(v_rbx) == 0) goto loc_002FDEE5;
    v_stack_mB0 = v_stack_m58;
    v_stack_mB8 = (unsigned int)(v_rbx);
    goto loc_002FDC84;
loc_002FDD75:
    a1 = 0;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + a1 * 2))) == 60) goto loc_002FDEBD;
    v_rsi = (unsigned __int16)((v_rsi) + (4));
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + a1 * 2))) == 62) goto loc_002FDFCD;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + a1 * 2))) == 34) goto loc_002FE057;
    if (v_stack_mC8 != 0) goto loc_002FDDCE;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + a1 * 2))) == 63) goto loc_002FDFE7;
loc_002FDDB2:
    if (v_stack_mC7 != 0) goto loc_002FDEA9;
loc_002FDDBD:
    result = v_stack_m78;
    v_rbx = v_stack_mC2;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + a1 * 2))) == ((unsigned __int16)(v_stack_mC6))) {
        result = (unsigned int)(v_stack_mC2);
        v_rbx = (unsigned int)((v_stack_mC2) + ((unsigned int)(v_r13 + 1)));
        *(unsigned __int16 *)(v_stack_m78 + result * 2) = (unsigned __int16)(v_rsi);
    }
    a1 = 0;
loc_002FDDCE:
    if (0 >= ((unsigned int)((unsigned int)(v_stack_mB8)))) goto loc_002FDD4C;
loc_002FDDE4:
    if (((unsigned int)((unsigned int)(v_stack_mBC))) >= ((unsigned int)(v_rbx))) goto loc_002FDE1C;
    if (0 >= ((unsigned int)((unsigned int)(v_stack_mB8)))) goto loc_002FDE0C;
loc_002FDDF9:
    if ((*(unsigned __int16 *)(v_stack_m58 + v_r13 * 2)) >= ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m78 + (unsigned int)((unsigned int)((unsigned int)(v_stack_mBC))) * 2)))) goto loc_002FDE08;
    v_r13 = (unsigned int)((v_r13) + ((unsigned int)(v_r13 + 1)));
    if (((unsigned int)(v_r13)) < ((unsigned int)((unsigned int)(v_stack_mB8)))) goto loc_002FDDF9;
loc_002FDE08:
loc_002FDE0C:
    a1 = (unsigned int)(((unsigned int)(v_stack_mBC)) + ((unsigned int)(v_r13 + 1)));
    v_stack_mBC = (unsigned int)(a1);
    if (((unsigned int)(v_r13)) < ((unsigned int)((unsigned int)(v_stack_mB8)))) goto loc_002FDDE4;
loc_002FDE1C:
    a1 = 0;
    goto loc_002FDCBB;
loc_002FDE23:
    if (v_stack_mC4 == ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(v_stack_mBC)))))) goto loc_002FDD20;
    goto loc_002FDD20;
loc_002FDE3F:
    v_stack_mC8 = (unsigned __int8)(v_r13 + 1);
    if ((*(unsigned __int16 *)(v_stack_m58 + (unsigned int)(v_stack_mB8) - 1 * 2)) != ((unsigned __int16)(v_rbp))) goto loc_002FDCB3;
loc_002FDE55:
    if (0 != 0) goto loc_002FE08C;
loc_002FDE63:
loc_002FDE66:
    result = (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m58 + (unsigned int)(v_stack_mB8) - 1 * 2))) == ((unsigned __int16)(v_rbp))) ? 1 : 0;
loc_002FDE69:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(v_stack_mB8), 0, a1);
    return result;
loc_002FDE9B:
    *(unsigned __int16 *)(v_stack_m78 + (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56))) * 2) = (unsigned __int16)(*(unsigned __int64 *)(v_stack_m28 + 64));
loc_002FDEA2:
    v_rbx = (unsigned int)((*(unsigned __int64 *)(v_stack_m28 + 56)) + ((unsigned int)(v_r13 + 1)));
    goto loc_002FDDCE;
loc_002FDEA9:
    goto loc_002FDDBD;
loc_002FDEBD:
    if (v_stack_mA0 == ((unsigned __int8)(*(unsigned __int16 *)(a5 + (unsigned __int16)(a1) * 2)))) goto loc_002FDEF5;
loc_002FDEC3:
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(v_r13 + 1)));
    *(unsigned __int16 *)(v_stack_m78 + (unsigned int)((unsigned int)(v_rbx)) * 2) = (unsigned __int16)(*(unsigned __int64 *)(v_stack_m28 + 72));
    v_rsi = (unsigned __int16)((*(unsigned __int64 *)(v_stack_m28 + 72)) + (3));
    *(unsigned __int16 *)(v_stack_m78 + v_rbx * 2) = (unsigned __int16)(v_rsi);
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(v_r13 + 1)));
loc_002FDEDC:
    goto loc_002FDCD8;
loc_002FDEE5:
    if (0 != 0) goto loc_002FE075;
loc_002FDEEE:
    result = 0;
    goto loc_002FDE69;
loc_002FDEF5:
    if (v_stack_m9E != 46) goto loc_002FDEC3;
loc_002FDF06:
    if (((unsigned __int16)(v_stack_m9A)) < ((unsigned __int16)(*(unsigned __int16 *)(a2)))) goto loc_002FDFF3;
    v_rsi = (unsigned __int16)((v_rsi) + (3));
    *(unsigned __int16 *)(v_stack_m78 + (unsigned int)((unsigned int)(v_rbx)) * 2) = (unsigned __int16)(v_rsi);
    goto loc_002FDD42;
loc_002FDF25:
    v_stack_m68 = v_xmm0;
    v_rbx = (unsigned __int16)((v_stack_m68) - ((unsigned __int16)(*(unsigned __int16 *)(a5 + (unsigned __int16)(a1) * 2))));
    result = (v_stack_m68) >> (16);
    result = (unsigned __int16)((result) - ((unsigned __int16)(*(unsigned __int16 *)(a5 + (unsigned __int16)(a1) * 2))));
    v_stack_m60 = (unsigned int)((unsigned int)(v_rbx)) + 2;
    v_stack_m66 = (unsigned __int16)(result);
    v_stack_m68 = (unsigned __int16)(v_rbx);
    result = RtlDoesNameContainWildCards(v_stack_m68, v_stack_m9A, 0, v_stack_m78);
    if ((unsigned __int8)(result) != 0) goto loc_002FE042;
    v_rbp = (unsigned __int16)((*(unsigned __int64 *)(v_stack_m28 + 64)) - (2));
    if (((unsigned __int16)(v_rsi)) < ((unsigned __int16)(v_rbp))) goto loc_002FDEEE;
    a4 = (v_rsi) - ((unsigned __int16)(v_rbx));
    a4 = (a4) >> (1);
    if ((unsigned __int8)(v_stack_m78) == 0) goto loc_002FDFB3;
    v_rbx = (unsigned __int16)((v_rbx) >> (1));
    if (((unsigned __int16)((unsigned __int16)(v_r13))) < ((unsigned __int16)(v_rbx))) goto loc_002FE014;
loc_002FDF9F:
    goto loc_002FDE69;
loc_002FDFA7:
    if ((*(unsigned __int16 *)((unsigned __int8)(v_r13 + 1))) != 42) goto loc_002FDC4C;
    goto loc_002FDF9F;
loc_002FDFB3:
    result = memcmp((unsigned int)((unsigned int)(v_rbx)) + 2, *(unsigned __int64 *)(v_stack_m80 + 8) + (unsigned int)(a4) * 2, a5, a4);
    goto loc_002FDE66;
loc_002FDFCD:
    if (v_stack_mA0 != ((unsigned __int8)((unsigned int)((unsigned int)(v_rbx)) + 2))) goto loc_002FDCD8;
    if (v_stack_m9E == 46) goto loc_002FDEDC;
loc_002FDFE7:
    *(unsigned __int16 *)(v_stack_m78 + (unsigned int)((unsigned int)(v_rbx)) * 2) = (unsigned __int16)(v_rsi);
    goto loc_002FDEA2;
loc_002FDFF3:
    a1 = ((unsigned __int16)(*(unsigned __int64 *)(v_stack_m80 + 8) + (unsigned int)(a4) * 2)) >> (1);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 8) + a1 * 2)) == 46) goto loc_002FE00D;
    a2 = (unsigned __int16)((*(unsigned __int64 *)(v_stack_m80 + 8) + (unsigned int)(a4) * 2) + (2));
    goto loc_002FDF06;
loc_002FE00D:
    a1 = 0;
    goto loc_002FDEC3;
loc_002FE014:
    a1 = (unsigned int)(((unsigned __int16)(a2)) + (a4));
loc_002FE042:
    goto loc_002FDC4C;
loc_002FE057:
    if (v_stack_mA0 != ((unsigned __int8)(*(unsigned __int16 *)(a5 + *(unsigned __int16 *)((unsigned int)((unsigned int)(v_rbx)) + 2 + (unsigned __int16)(a2) * 2) * 2)))) goto loc_002FDEDC;
    if (((unsigned __int16)(v_stack_m9E)) != 46) goto loc_002FDDB2;
    goto loc_002FDDC3;
loc_002FE075:
    a2 = 0;
    result = ExFreePoolWithTag(v_r13, a2, v_r13, v_stack_m78);
    goto loc_002FDEEE;
loc_002FE084:
    goto loc_002FDE55;
loc_002FE08C:
    a2 = 0;
    result = ExFreePoolWithTag(v_r13, a2, v_r13, v_stack_m78);
    goto loc_002FDE63;
loc_002FE09B:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) + ((unsigned int)(*(unsigned __int16 *)(v_stack_m78))));
    goto loc_002FDE66;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpIsNameInExpressionPrivate(void *Arg1, void *Arg2, uint8_t Arg3, uint8_t Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint16_t v_stack_m66;
    uint64_t v_stack_m68;
    uint16_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m98;
    uint16_t v_stack_m9A;
    uint16_t v_stack_m9E;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint16_t v_stack_mC2;
    uint8_t v_stack_mC4;
    uint16_t v_stack_mC6;
    uint8_t v_stack_mC7;
    uint8_t v_stack_mC8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0xB0CB6E)) ^ (local_rsp);
    v_stack_m38 = result;
    local_r13 = 0;
    v_stack_mC4 = Arg4;
    v_stack_mC7 = Arg3;
    v_stack_mA8 = Arg2;
    v_stack_mA0 = Arg1;
    v_stack_mC6 = 0;
    v_stack_mB0 = 0;
    v_stack_mC8 = 0;
    if ((uint16_t)(*(uint16_t *)(arg2)) == 0) goto loc_002FE09B;
    if ((uint16_t)(*(uint16_t *)(arg1)) == 0) goto loc_002FE09B;
    if (((uint16_t)(*(uint16_t *)(arg1))) == ((uint16_t)(local_r13 + 1 + 1))) goto loc_002FDFA7;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8))) == 42) goto loc_002FDF25;
loc_002FDC4C:
    v_stack_m78 = 0;
    v_stack_mB0 = v_stack_m78;
    v_stack_mB8 = (uint32_t)((uint32_t)((uint32_t)(local_r13 + 1)));
    v_stack_mC2 = 0;
    if (((uint16_t)(*(uint16_t *)(arg1))) > ((uint16_t)((uint32_t)(0x7FFFULL)))) goto loc_002FDEEE;
    local_rbp = (uint16_t)((*(uint16_t *)(arg1)) + ((uint16_t)(*(uint16_t *)(arg1))));
loc_002FDC84:
    if (0 != 0) goto loc_002FE084;
    if (0 >= (*(uint16_t *)(arg2))) goto loc_002FDE3F;
    Arg1 = (0) >> (1);
    local_rbx = (uint16_t)((0) + (2));
    v_stack_mC2 = (uint16_t)(local_rbx);
    v_stack_mC6 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(arg2 + 0x8) + arg1 * 2));
loc_002FDCB3:
    Arg1 = 0;
    v_stack_mBC = 0;
loc_002FDCBB:
    if (0 >= ((uint32_t)((uint32_t)((uint32_t)(local_r13 + 1))))) goto loc_002FDD4C;
    local_r12 = (uint32_t)((*(uint16_t *)(v_stack_m78 + 0x0 * 2)) + ((uint32_t)(local_r13 + 1)));
    local_r12 = (uint32_t)((local_r12) >> (1));
    local_r13 = (uint32_t)((local_r13) + ((uint32_t)(local_r13 + 1)));
loc_002FDCD8:
    if (((uint16_t)(local_r12)) == ((uint16_t)(*(uint16_t *)(arg1)))) goto loc_002FDDCE;
    local_r12 = (uint16_t)((local_r12) + (0));
    v_stack_mC0 = 2;
    local_rsi = (uint16_t)(((uint16_t)(local_r12)) + ((uint16_t)((uint16_t)(local_r12))));
    if (((uint16_t)(local_r12)) == ((uint16_t)(*(uint16_t *)(arg1)))) goto loc_002FDE9B;
    Arg1 = ((uint16_t)(local_r12)) >> (1);
    result = 0;
    if (v_stack_mC7 != 0) goto loc_002FDE23;
loc_002FDD20:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + arg1 * 2))) != 42) goto loc_002FDD75;
    local_rbx = (uint32_t)((0) + ((uint32_t)(local_r13 + 1)));
    *(uint16_t *)(v_stack_m58 + 0x0 * 2) = (uint16_t)(local_rsi);
    local_rsi = (uint16_t)((local_rsi) + (3));
    *(uint16_t *)(v_stack_m58 + local_rbx * 2) = (uint16_t)(local_rsi);
loc_002FDD42:
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(local_r13 + 1)));
    Arg1 = 0;
    goto loc_002FDCD8;
loc_002FDD4C:
    local_r13 = 0;
    if ((uint32_t)(local_rbx) == 0) goto loc_002FDEE5;
    v_stack_mB0 = v_stack_m58;
    v_stack_mB8 = (uint32_t)(local_rbx);
    goto loc_002FDC84;
loc_002FDD75:
    Arg1 = 0;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + arg1 * 2))) == 60) goto loc_002FDEBD;
    local_rsi = (uint16_t)((local_rsi) + (4));
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + arg1 * 2))) == 62) goto loc_002FDFCD;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + arg1 * 2))) == 34) goto loc_002FE057;
    if (v_stack_mC8 != 0) goto loc_002FDDCE;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + arg1 * 2))) == 63) goto loc_002FDFE7;
loc_002FDDB2:
    if (v_stack_mC7 != 0) goto loc_002FDEA9;
loc_002FDDBD:
    result = v_stack_m78;
    local_rbx = v_stack_mC2;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + arg1 * 2))) == ((uint16_t)(v_stack_mC6))) {
        result = (uint32_t)(v_stack_mC2);
        local_rbx = (uint32_t)((v_stack_mC2) + ((uint32_t)(local_r13 + 1)));
        *(uint16_t *)(v_stack_m78 + result * 2) = (uint16_t)(local_rsi);
    }
    Arg1 = 0;
loc_002FDDCE:
    if (0 >= ((uint32_t)((uint32_t)(v_stack_mB8)))) goto loc_002FDD4C;
loc_002FDDE4:
    if (((uint32_t)((uint32_t)(v_stack_mBC))) >= ((uint32_t)(local_rbx))) goto loc_002FDE1C;
    if (0 >= ((uint32_t)((uint32_t)(v_stack_mB8)))) goto loc_002FDE0C;
loc_002FDDF9:
    if ((*(uint16_t *)(v_stack_m58 + local_r13 * 2)) >= ((uint16_t)(*(uint16_t *)(v_stack_m78 + (uint32_t)((uint32_t)((uint32_t)(v_stack_mBC))) * 2)))) goto loc_002FDE08;
    local_r13 = (uint32_t)((local_r13) + ((uint32_t)(local_r13 + 1)));
    if (((uint32_t)(local_r13)) < ((uint32_t)((uint32_t)(v_stack_mB8)))) goto loc_002FDDF9;
loc_002FDE08:
loc_002FDE0C:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_mBC)) + ((uint32_t)(local_r13 + 1)));
    v_stack_mBC = (uint32_t)(Arg1);
    if (((uint32_t)(local_r13)) < ((uint32_t)((uint32_t)(v_stack_mB8)))) goto loc_002FDDE4;
loc_002FDE1C:
    Arg1 = 0;
    goto loc_002FDCBB;
loc_002FDE23:
    if (v_stack_mC4 == ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mBC)))))) goto loc_002FDD20;
    goto loc_002FDD20;
loc_002FDE3F:
    v_stack_mC8 = (uint8_t)(local_r13 + 1);
    if ((*(uint16_t *)(v_stack_m58 + (uint32_t)(v_stack_mB8) - 0x1 * 2)) != ((uint16_t)(local_rbp))) goto loc_002FDCB3;
loc_002FDE55:
    if (0 != 0) goto loc_002FE08C;
loc_002FDE63:
loc_002FDE66:
    result = (((uint16_t)(*(uint16_t *)(v_stack_m58 + (uint32_t)(v_stack_mB8) - 0x1 * 2))) == ((uint16_t)(local_rbp))) ? 1 : 0;
loc_002FDE69:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(v_stack_mB8), 0, Arg1);
    return result;
loc_002FDE9B:
    *(uint16_t *)(v_stack_m78 + (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38))) * 2) = (uint16_t)(*(uint64_t *)(v_stack_m28 + 0x40));
loc_002FDEA2:
    local_rbx = (uint32_t)((*(uint64_t *)(v_stack_m28 + 0x38)) + ((uint32_t)(local_r13 + 1)));
    goto loc_002FDDCE;
loc_002FDEA9:
    goto loc_002FDDBD;
loc_002FDEBD:
    if (v_stack_mA0 == ((uint8_t)(*(uint16_t *)(arg5 + (uint16_t)(arg1) * 2)))) goto loc_002FDEF5;
loc_002FDEC3:
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(local_r13 + 1)));
    *(uint16_t *)(v_stack_m78 + (uint32_t)((uint32_t)(local_rbx)) * 2) = (uint16_t)(*(uint64_t *)(v_stack_m28 + 0x48));
    local_rsi = (uint16_t)((*(uint64_t *)(v_stack_m28 + 0x48)) + (3));
    *(uint16_t *)(v_stack_m78 + local_rbx * 2) = (uint16_t)(local_rsi);
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(local_r13 + 1)));
loc_002FDEDC:
    goto loc_002FDCD8;
loc_002FDEE5:
    if (0 != 0) goto loc_002FE075;
loc_002FDEEE:
    result = 0;
    goto loc_002FDE69;
loc_002FDEF5:
    if (v_stack_m9E != 46) goto loc_002FDEC3;
loc_002FDF06:
    if (((uint16_t)(v_stack_m9A)) < ((uint16_t)(*(uint16_t *)(arg2)))) goto loc_002FDFF3;
    local_rsi = (uint16_t)((local_rsi) + (3));
    *(uint16_t *)(v_stack_m78 + (uint32_t)((uint32_t)(local_rbx)) * 2) = (uint16_t)(local_rsi);
    goto loc_002FDD42;
loc_002FDF25:
    v_stack_m68 = v_xmm0;
    local_rbx = (uint16_t)((v_stack_m68) - ((uint16_t)(*(uint16_t *)(arg5 + (uint16_t)(arg1) * 2))));
    result = (v_stack_m68) >> (16);
    result = (uint16_t)((result) - ((uint16_t)(*(uint16_t *)(arg5 + (uint16_t)(arg1) * 2))));
    v_stack_m60 = (uint32_t)((uint32_t)(local_rbx)) + 2;
    v_stack_m66 = (uint16_t)(result);
    v_stack_m68 = (uint16_t)(local_rbx);
    result = RtlDoesNameContainWildCards(v_stack_m68, v_stack_m9A, 0, v_stack_m78);
    if ((uint8_t)(result) != 0) goto loc_002FE042;
    local_rbp = (uint16_t)((*(uint64_t *)(v_stack_m28 + 0x40)) - (2));
    if (((uint16_t)(local_rsi)) < ((uint16_t)(local_rbp))) goto loc_002FDEEE;
    Arg4 = (local_rsi) - ((uint16_t)(local_rbx));
    Arg4 = (Arg4) >> (1);
    if ((uint8_t)(v_stack_m78) == 0) goto loc_002FDFB3;
    local_rbx = (uint16_t)((local_rbx) >> (1));
    if (((uint16_t)((uint16_t)(local_r13))) < ((uint16_t)(local_rbx))) goto loc_002FE014;
loc_002FDF9F:
    goto loc_002FDE69;
loc_002FDFA7:
    if ((*(uint16_t *)((uint8_t)(local_r13 + 0x1))) != 42) goto loc_002FDC4C;
    goto loc_002FDF9F;
loc_002FDFB3:
    result = memcmp((uint32_t)((uint32_t)(local_rbx)) + 2, *(uint64_t *)(v_stack_m80 + 0x8) + (uint32_t)(Arg4) * 2, Arg5, Arg4);
    goto loc_002FDE66;
loc_002FDFCD:
    if (v_stack_mA0 != ((uint8_t)((uint32_t)((uint32_t)(local_rbx)) + 2))) goto loc_002FDCD8;
    if (v_stack_m9E == 46) goto loc_002FDEDC;
loc_002FDFE7:
    *(uint16_t *)(v_stack_m78 + (uint32_t)((uint32_t)(local_rbx)) * 2) = (uint16_t)(local_rsi);
    goto loc_002FDEA2;
loc_002FDFF3:
    Arg1 = ((uint16_t)(*(uint64_t *)(v_stack_m80 + 0x8) + (uint32_t)(Arg4) * 2)) >> (1);
    if ((*(uint16_t *)(*(uint64_t *)(arg2 + 0x8) + arg1 * 2)) == 46) goto loc_002FE00D;
    Arg2 = (uint16_t)((*(uint64_t *)(v_stack_m80 + 0x8) + (uint32_t)(Arg4) * 2) + (2));
    goto loc_002FDF06;
loc_002FE00D:
    Arg1 = 0;
    goto loc_002FDEC3;
loc_002FE014:
    Arg1 = (uint32_t)(((uint16_t)(Arg2)) + (Arg4));
loc_002FE042:
    goto loc_002FDC4C;
loc_002FE057:
    if (v_stack_mA0 != ((uint8_t)(*(uint16_t *)(arg5 + *(uint16_t *)((uint32_t)((uint32_t)(local_rbx)) + 0x2 + (uint16_t)(arg2) * 2) * 2)))) goto loc_002FDEDC;
    if (((uint16_t)(v_stack_m9E)) != 46) goto loc_002FDDB2;
    goto loc_002FDDC3;
loc_002FE075:
    Arg2 = 0;
    result = ExFreePoolWithTag(local_r13, Arg2, local_r13, v_stack_m78);
    goto loc_002FDEEE;
loc_002FE084:
    goto loc_002FDE55;
loc_002FE08C:
    Arg2 = 0;
    result = ExFreePoolWithTag(local_r13, Arg2, local_r13, v_stack_m78);
    goto loc_002FDE63;
loc_002FE09B:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) + ((uint32_t)(*(uint16_t *)(v_stack_m78))));
    goto loc_002FDE66;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg5` | `+ 0x0 + r14*2` | `16` | `R` |
| `Arg5` | `+ 0x0 + rax*2` | `16` | `R` |
| `Arg5` | `+ 0x0 + rcx*2` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002FDBAC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
