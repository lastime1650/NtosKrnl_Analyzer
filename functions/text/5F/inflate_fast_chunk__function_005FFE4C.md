# inflate_fast_chunk_

- RVA: `0x005FFE4C`–`0x0060033C` (길이 `1,264` bytes)
- VA: `0x00000001405FFE4C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D04D0`
- 디코드: `371`개 명령, `1,264/1,264` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00600126` → [chunkcopy_core](chunkcopy_core_function_005F20DC.md) (function, `0x005F20DC`)
- `0x006001A2` → [chunkcopy_core](chunkcopy_core_function_005F20DC.md) (function, `0x005F20DC`)
- `0x006001C7` → [chunkunroll_relaxed](chunkunroll_relaxed_function_005FFE0C.md) (function, `0x005FFE0C`)
- `0x0060026F` → [chunkcopy_core](chunkcopy_core_function_005F20DC.md) (function, `0x005F20DC`)
- `0x00600294` → [chunkcopy_lapped_relaxed](chunkcopy_lapped_relaxed_function_005FFC8C.md) (function, `0x005FFC8C`)

### Direct callers
- [inflate](inflate_function_005F2280.md) at `0x005F2BC9`

### Static image references
- `0x006002C2` → RVA `0x006CD500` (` ?? ::FNODOBFM::`string'`; read)
- `0x006002CB` → RVA `0x006CD520` (` ?? ::FNODOBFM::`string'`; read)
- `0x006002D4` → RVA `0x006CD540` (` ?? ::FNODOBFM::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005FFE4C  40 53                           push rbx
005FFE4E  55                              push rbp
005FFE4F  56                              push rsi
005FFE50  57                              push rdi
005FFE51  41 54                           push r12
005FFE53  41 55                           push r13
005FFE55  41 56                           push r14
005FFE57  41 57                           push r15
005FFE59  48 83 EC 58                     sub rsp, 0x58
005FFE5D  44 8B 69 18                     mov r13d, dword ptr [rcx + 0x18]
005FFE61  48 8B F1                        mov rsi, rcx
005FFE64  4C 8B 49 10                     mov r9, qword ptr [rcx + 0x10]
005FFE68  41 2B D5                        sub edx, r13d
005FFE6B  48 8B 79 28                     mov rdi, qword ptr [rcx + 0x28]
005FFE6F  44 8B 79 08                     mov r15d, dword ptr [rcx + 8]
005FFE73  4C 8B 31                        mov r14, qword ptr [rcx]
005FFE76  45 8D A5 FD FE FF FF            lea r12d, [r13 - 0x103]
005FFE7D  8B C2                           mov eax, edx
005FFE7F  41 83 EF 0E                     sub r15d, 0xe
005FFE83  8B 57 3C                        mov edx, dword ptr [rdi + 0x3c]
005FFE86  49 8B C9                        mov rcx, r9
005FFE89  48 2B C8                        sub rcx, rax
005FFE8C  89 94 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], edx
005FFE93  8B 47 34                        mov eax, dword ptr [rdi + 0x34]
005FFE96  4D 03 E1                        add r12, r9
005FFE99  4D 03 FE                        add r15, r14
005FFE9C  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
005FFEA1  8B 4F 38                        mov ecx, dword ptr [rdi + 0x38]
005FFEA4  4D 03 E9                        add r13, r9
005FFEA7  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
005FFEAB  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
005FFEAF  85 D2                           test edx, edx
005FFEB1  75 0B                           jne 0x1405ffebe
005FFEB3  3B C8                           cmp ecx, eax
005FFEB5  72 07                           jb 0x1405ffebe
005FFEB7  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
005FFEBE  8B 4F 70                        mov ecx, dword ptr [rdi + 0x70]
005FFEC1  BB 01 00 00 00                  mov ebx, 1
005FFEC6  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
005FFECA  41 BA 01 00 00 00               mov r10d, 1
005FFED0  4C 8B 47 60                     mov r8, qword ptr [rdi + 0x60]
005FFED4  8B 6F 48                        mov ebp, dword ptr [rdi + 0x48]
005FFED7  44 8B 5F 4C                     mov r11d, dword ptr [rdi + 0x4c]
005FFEDB  D3 E3                           shl ebx, cl
005FFEDD  8B 4F 74                        mov ecx, dword ptr [rdi + 0x74]
005FFEE0  FF CB                           dec ebx
005FFEE2  41 D3 E2                        shl r10d, cl
005FFEE5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005FFEEA  41 FF CA                        dec r10d
005FFEED  48 8B 47 68                     mov rax, qword ptr [rdi + 0x68]
005FFEF1  44 89 94 24 B0 00 00 00         mov dword ptr [rsp + 0xb0], r10d
005FFEF9  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
005FFEFE  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
005FFF03  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
005FFF08  49 8B 06                        mov rax, qword ptr [r14]
005FFF0B  41 8B CB                        mov ecx, r11d
005FFF0E  48 D3 E0                        shl rax, cl
005FFF11  48 0B E8                        or rbp, rax
005FFF14  41 8B CB                        mov ecx, r11d
005FFF17  48 C1 E9 03                     shr rcx, 3
005FFF1B  B8 07 00 00 00                  mov eax, 7
005FFF20  48 2B C1                        sub rax, rcx
005FFF23  41 83 CB 38                     or r11d, 0x38
005FFF27  4C 03 F0                        add r14, rax
005FFF2A  48 8B C3                        mov rax, rbx
005FFF2D  48 23 C5                        and rax, rbp
005FFF30  49 8D 14 80                     lea rdx, [r8 + rax*4]
005FFF34  80 3A 00                        cmp byte ptr [rdx], 0
005FFF37  75 43                           jne 0x1405fff7c
005FFF39  8A 42 02                        mov al, byte ptr [rdx + 2]
005FFF3C  41 88 01                        mov byte ptr [r9], al
005FFF3F  49 FF C1                        inc r9
005FFF42  0F B6 42 01                     movzx eax, byte ptr [rdx + 1]
005FFF46  8A C8                           mov cl, al
005FFF48  44 2B D8                        sub r11d, eax
005FFF4B  48 D3 ED                        shr rbp, cl
005FFF4E  48 8B C3                        mov rax, rbx
005FFF51  48 23 C5                        and rax, rbp
005FFF54  49 8D 14 80                     lea rdx, [r8 + rax*4]
005FFF58  80 3A 00                        cmp byte ptr [rdx], 0
005FFF5B  75 1F                           jne 0x1405fff7c
005FFF5D  8A 42 02                        mov al, byte ptr [rdx + 2]
005FFF60  41 88 01                        mov byte ptr [r9], al
005FFF63  49 FF C1                        inc r9
005FFF66  0F B6 42 01                     movzx eax, byte ptr [rdx + 1]
005FFF6A  8A C8                           mov cl, al
005FFF6C  44 2B D8                        sub r11d, eax
005FFF6F  48 D3 ED                        shr rbp, cl
005FFF72  48 8B C3                        mov rax, rbx
005FFF75  48 23 C5                        and rax, rbp
005FFF78  49 8D 14 80                     lea rdx, [r8 + rax*4]
005FFF7C  0F B6 4A 01                     movzx ecx, byte ptr [rdx + 1]
005FFF80  48 D3 ED                        shr rbp, cl
005FFF83  44 2B D9                        sub r11d, ecx
005FFF86  0F B6 0A                        movzx ecx, byte ptr [rdx]
005FFF89  85 C9                           test ecx, ecx
005FFF8B  0F 84 0A 03 00 00               je 0x14060029b
005FFF91  F6 C1 10                        test cl, 0x10
005FFF94  75 23                           jne 0x1405fffb9
005FFF96  F6 C1 40                        test cl, 0x40
005FFF99  0F 85 15 03 00 00               jne 0x1406002b4
005FFF9F  B8 01 00 00 00                  mov eax, 1
005FFFA4  D3 E0                           shl eax, cl
005FFFA6  8D 48 FF                        lea ecx, [rax - 1]
005FFFA9  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
005FFFAD  48 23 CD                        and rcx, rbp
005FFFB0  48 03 C8                        add rcx, rax
005FFFB3  49 8D 14 88                     lea rdx, [r8 + rcx*4]
005FFFB7  EB C3                           jmp 0x1405fff7c
005FFFB9  0F B7 5A 02                     movzx ebx, word ptr [rdx + 2]
005FFFBD  83 E1 0F                        and ecx, 0xf
005FFFC0  74 13                           je 0x1405fffd5
005FFFC2  B8 01 00 00 00                  mov eax, 1
005FFFC7  D3 E0                           shl eax, cl
005FFFC9  FF C8                           dec eax
005FFFCB  23 C5                           and eax, ebp
005FFFCD  48 D3 ED                        shr rbp, cl
005FFFD0  03 D8                           add ebx, eax
005FFFD2  44 2B D9                        sub r11d, ecx
005FFFD5  41 8B C2                        mov eax, r10d
005FFFD8  4C 8B 54 24 40                  mov r10, qword ptr [rsp + 0x40]
005FFFDD  48 23 C5                        and rax, rbp
005FFFE0  4D 8D 04 82                     lea r8, [r10 + rax*4]
005FFFE4  41 0F B6 48 01                  movzx ecx, byte ptr [r8 + 1]
005FFFE9  41 0F B6 10                     movzx edx, byte ptr [r8]
005FFFED  44 2B D9                        sub r11d, ecx
005FFFF0  48 D3 ED                        shr rbp, cl
005FFFF3  F6 C2 10                        test dl, 0x10
005FFFF6  75 26                           jne 0x14060001e
005FFFF8  F6 C2 40                        test dl, 0x40
005FFFFB  0F 85 CA 02 00 00               jne 0x1406002cb
00600001  8B CA                           mov ecx, edx
00600003  B8 01 00 00 00                  mov eax, 1
00600008  D3 E0                           shl eax, cl
0060000A  8D 48 FF                        lea ecx, [rax - 1]
0060000D  41 0F B7 40 02                  movzx eax, word ptr [r8 + 2]
00600012  48 23 CD                        and rcx, rbp
00600015  48 03 C8                        add rcx, rax
00600018  4D 8D 04 8A                     lea r8, [r10 + rcx*4]
0060001C  EB C6                           jmp 0x1405fffe4
0060001E  45 0F B7 50 02                  movzx r10d, word ptr [r8 + 2]
00600023  83 E2 0F                        and edx, 0xf
00600026  44 3B DA                        cmp r11d, edx
00600029  73 22                           jae 0x14060004d
0060002B  49 8B 06                        mov rax, qword ptr [r14]
0060002E  41 8B CB                        mov ecx, r11d
00600031  48 D3 E0                        shl rax, cl
00600034  48 0B E8                        or rbp, rax
00600037  41 8B CB                        mov ecx, r11d
0060003A  48 C1 E9 03                     shr rcx, 3
0060003E  B8 07 00 00 00                  mov eax, 7
00600043  48 2B C1                        sub rax, rcx
00600046  4C 03 F0                        add r14, rax
00600049  41 83 CB 38                     or r11d, 0x38
0060004D  8B CA                           mov ecx, edx
0060004F  B8 01 00 00 00                  mov eax, 1
00600054  D3 E0                           shl eax, cl
00600056  44 2B DA                        sub r11d, edx
00600059  FF C8                           dec eax
0060005B  23 C5                           and eax, ebp
0060005D  48 D3 ED                        shr rbp, cl
00600060  44 03 D0                        add r10d, eax
00600063  41 8B C1                        mov eax, r9d
00600066  2B 44 24 48                     sub eax, dword ptr [rsp + 0x48]
0060006A  44 89 94 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r10d
00600072  44 3B D0                        cmp r10d, eax
00600075  0F 86 10 02 00 00               jbe 0x14060028b
0060007B  44 2B D0                        sub r10d, eax
0060007E  44 3B 54 24 20                  cmp r10d, dword ptr [rsp + 0x20]
00600083  76 0D                           jbe 0x140600092
00600085  83 BF 60 23 00 00 00            cmp dword ptr [rdi + 0x2360], 0
0060008C  0F 85 42 02 00 00               jne 0x1406002d4
00600092  8B 84 24 A8 00 00 00            mov eax, dword ptr [rsp + 0xa8]
00600099  41 3B C2                        cmp eax, r10d
0060009C  72 0F                           jb 0x1406000ad
0060009E  41 2B C2                        sub eax, r10d
006000A1  8B D0                           mov edx, eax
006000A3  48 03 54 24 28                  add rdx, qword ptr [rsp + 0x28]
006000A8  E9 8E 00 00 00                  jmp 0x14060013b
006000AD  8B 54 24 24                     mov edx, dword ptr [rsp + 0x24]
006000B1  44 2B D0                        sub r10d, eax
006000B4  41 2B D2                        sub edx, r10d
006000B7  48 03 54 24 28                  add rdx, qword ptr [rsp + 0x28]
006000BC  44 3B D3                        cmp r10d, ebx
006000BF  0F 83 50 01 00 00               jae 0x140600215
006000C5  49 8B C5                        mov rax, r13
006000C8  41 2B DA                        sub ebx, r10d
006000CB  49 2B C1                        sub rax, r9
006000CE  48 83 F8 10                     cmp rax, 0x10
006000D2  7D 4C                           jge 0x140600120
006000D4  41 F6 C2 08                     test r10b, 8
006000D8  74 0E                           je 0x1406000e8
006000DA  48 8B 02                        mov rax, qword ptr [rdx]
006000DD  49 89 01                        mov qword ptr [r9], rax
006000E0  49 83 C1 08                     add r9, 8
006000E4  48 83 C2 08                     add rdx, 8
006000E8  41 F6 C2 04                     test r10b, 4
006000EC  74 0D                           je 0x1406000fb
006000EE  8B 02                           mov eax, dword ptr [rdx]
006000F0  41 89 01                        mov dword ptr [r9], eax
006000F3  49 83 C1 04                     add r9, 4
006000F7  48 83 C2 04                     add rdx, 4
006000FB  41 F6 C2 02                     test r10b, 2
006000FF  74 0F                           je 0x140600110
00600101  0F B7 02                        movzx eax, word ptr [rdx]
00600104  66 41 89 01                     mov word ptr [r9], ax
00600108  49 83 C1 02                     add r9, 2
0060010C  48 83 C2 02                     add rdx, 2
00600110  41 F6 C2 01                     test r10b, 1
00600114  74 18                           je 0x14060012e
00600116  8A 02                           mov al, byte ptr [rdx]
00600118  41 88 01                        mov byte ptr [r9], al
0060011B  49 FF C1                        inc r9
0060011E  EB 0E                           jmp 0x14060012e
00600120  45 8B C2                        mov r8d, r10d
00600123  49 8B C9                        mov rcx, r9
00600126  E8 B1 1F FF FF                  call 0x1405f20dc
0060012B  4C 8B C8                        mov r9, rax
0060012E  48 8B 54 24 28                  mov rdx, qword ptr [rsp + 0x28]
00600133  44 8B 94 24 A8 00 00 00         mov r10d, dword ptr [rsp + 0xa8]
0060013B  44 3B D3                        cmp r10d, ebx
0060013E  0F 83 D1 00 00 00               jae 0x140600215
00600144  49 8B C5                        mov rax, r13
00600147  49 2B C1                        sub rax, r9
0060014A  48 83 F8 10                     cmp rax, 0x10
0060014E  7D 4C                           jge 0x14060019c
00600150  41 F6 C2 08                     test r10b, 8
00600154  74 0E                           je 0x140600164
00600156  48 8B 02                        mov rax, qword ptr [rdx]
00600159  49 89 01                        mov qword ptr [r9], rax
0060015C  49 83 C1 08                     add r9, 8
00600160  48 83 C2 08                     add rdx, 8
00600164  41 F6 C2 04                     test r10b, 4
00600168  74 0D                           je 0x140600177
0060016A  8B 02                           mov eax, dword ptr [rdx]
0060016C  41 89 01                        mov dword ptr [r9], eax
0060016F  49 83 C1 04                     add r9, 4
00600173  48 83 C2 04                     add rdx, 4
00600177  41 F6 C2 02                     test r10b, 2
0060017B  74 0F                           je 0x14060018c
0060017D  0F B7 02                        movzx eax, word ptr [rdx]
00600180  66 41 89 01                     mov word ptr [r9], ax
00600184  49 83 C1 02                     add r9, 2
00600188  48 83 C2 02                     add rdx, 2
0060018C  41 F6 C2 01                     test r10b, 1
00600190  74 18                           je 0x1406001aa
00600192  8A 02                           mov al, byte ptr [rdx]
00600194  41 88 01                        mov byte ptr [r9], al
00600197  49 FF C1                        inc r9
0060019A  EB 0E                           jmp 0x1406001aa
0060019C  45 8B C2                        mov r8d, r10d
0060019F  49 8B C9                        mov rcx, r9
006001A2  E8 35 1F FF FF                  call 0x1405f20dc
006001A7  4C 8B C8                        mov r9, rax
006001AA  41 2B DA                        sub ebx, r10d
006001AD  4C 8D 84 24 B8 00 00 00         lea r8, [rsp + 0xb8]
006001B5  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
006001BD  89 9C 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], ebx
006001C4  49 8B C9                        mov rcx, r9
006001C7  E8 40 FC FF FF                  call 0x1405ffe0c
006001CC  44 8B 84 24 B8 00 00 00         mov r8d, dword ptr [rsp + 0xb8]
006001D4  4C 8B C8                        mov r9, rax
006001D7  49 8B C5                        mov rax, r13
006001DA  49 2B C1                        sub rax, r9
006001DD  48 83 F8 30                     cmp rax, 0x30
006001E1  7D 29                           jge 0x14060020c
006001E3  45 85 C0                        test r8d, r8d
006001E6  0F 84 8B 00 00 00               je 0x140600277
006001EC  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
006001F3  49 8B C9                        mov rcx, r9
006001F6  48 2B C8                        sub rcx, rax
006001F9  8A 01                           mov al, byte ptr [rcx]
006001FB  48 FF C1                        inc rcx
006001FE  41 88 01                        mov byte ptr [r9], al
00600201  49 FF C1                        inc r9
00600204  41 83 C0 FF                     add r8d, -1
00600208  75 EF                           jne 0x1406001f9
0060020A  EB 6B                           jmp 0x140600277
0060020C  8B 94 24 A0 00 00 00            mov edx, dword ptr [rsp + 0xa0]
00600213  EB 7C                           jmp 0x140600291
00600215  49 8B C5                        mov rax, r13
00600218  49 2B C1                        sub rax, r9
0060021B  48 83 F8 10                     cmp rax, 0x10
0060021F  7D 48                           jge 0x140600269
00600221  F6 C3 08                        test bl, 8
00600224  74 0E                           je 0x140600234
00600226  48 8B 02                        mov rax, qword ptr [rdx]
00600229  49 89 01                        mov qword ptr [r9], rax
0060022C  49 83 C1 08                     add r9, 8
00600230  48 83 C2 08                     add rdx, 8
00600234  F6 C3 04                        test bl, 4
00600237  74 0D                           je 0x140600246
00600239  8B 02                           mov eax, dword ptr [rdx]
0060023B  41 89 01                        mov dword ptr [r9], eax
0060023E  49 83 C1 04                     add r9, 4
00600242  48 83 C2 04                     add rdx, 4
00600246  F6 C3 02                        test bl, 2
00600249  74 0F                           je 0x14060025a
0060024B  0F B7 02                        movzx eax, word ptr [rdx]
0060024E  66 41 89 01                     mov word ptr [r9], ax
00600252  49 83 C1 02                     add r9, 2
00600256  48 83 C2 02                     add rdx, 2
0060025A  F6 C3 01                        test bl, 1
0060025D  74 18                           je 0x140600277
0060025F  8A 02                           mov al, byte ptr [rdx]
00600261  41 88 01                        mov byte ptr [r9], al
00600264  49 FF C1                        inc r9
00600267  EB 0E                           jmp 0x140600277
00600269  44 8B C3                        mov r8d, ebx
0060026C  49 8B C9                        mov rcx, r9
0060026F  E8 68 1E FF FF                  call 0x1405f20dc
00600274  4C 8B C8                        mov r9, rax
00600277  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
0060027C  44 8B 94 24 B0 00 00 00         mov r10d, dword ptr [rsp + 0xb0]
00600284  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
00600289  EB 19                           jmp 0x1406002a4
0060028B  44 8B C3                        mov r8d, ebx
0060028E  41 8B D2                        mov edx, r10d
00600291  49 8B C9                        mov rcx, r9
00600294  E8 F3 F9 FF FF                  call 0x1405ffc8c
00600299  EB D9                           jmp 0x140600274
0060029B  8A 42 02                        mov al, byte ptr [rdx + 2]
0060029E  41 88 01                        mov byte ptr [r9], al
006002A1  49 FF C1                        inc r9
006002A4  4D 3B F7                        cmp r14, r15
006002A7  73 3D                           jae 0x1406002e6
006002A9  4D 3B CC                        cmp r9, r12
006002AC  0F 82 56 FC FF FF               jb 0x1405fff08
006002B2  EB 32                           jmp 0x1406002e6
006002B4  F6 C1 20                        test cl, 0x20
006002B7  74 09                           je 0x1406002c2
006002B9  C7 47 08 3F 3F 00 00            mov dword ptr [rdi + 8], 0x3f3f
006002C0  EB 24                           jmp 0x1406002e6
006002C2  48 8D 05 37 D2 0C 00            lea rax, [rip + 0xcd237]
006002C9  EB 10                           jmp 0x1406002db
006002CB  48 8D 05 4E D2 0C 00            lea rax, [rip + 0xcd24e]
006002D2  EB 07                           jmp 0x1406002db
006002D4  48 8D 05 65 D2 0C 00            lea rax, [rip + 0xcd265]
006002DB  48 89 46 20                     mov qword ptr [rsi + 0x20], rax
006002DF  C7 47 08 51 3F 00 00            mov dword ptr [rdi + 8], 0x3f51
006002E6  41 8B C3                        mov eax, r11d
006002E9  4C 89 4E 10                     mov qword ptr [rsi + 0x10], r9
006002ED  C1 E8 03                        shr eax, 3
006002F0  45 2B E1                        sub r12d, r9d
006002F3  4C 2B F0                        sub r14, rax
006002F6  41 81 C4 03 01 00 00            add r12d, 0x103
006002FD  C1 E0 03                        shl eax, 3
00600300  45 2B FE                        sub r15d, r14d
00600303  44 2B D8                        sub r11d, eax
00600306  4C 89 36                        mov qword ptr [rsi], r14
00600309  41 83 C7 0E                     add r15d, 0xe
0060030D  44 89 66 18                     mov dword ptr [rsi + 0x18], r12d
00600311  44 89 7E 08                     mov dword ptr [rsi + 8], r15d
00600315  41 8B CB                        mov ecx, r11d
00600318  B8 01 00 00 00                  mov eax, 1
0060031D  44 89 5F 4C                     mov dword ptr [rdi + 0x4c], r11d
00600321  D3 E0                           shl eax, cl
00600323  FF C8                           dec eax
00600325  23 C5                           and eax, ebp
00600327  89 47 48                        mov dword ptr [rdi + 0x48], eax
0060032A  48 83 C4 58                     add rsp, 0x58
0060032E  41 5F                           pop r15
00600330  41 5E                           pop r14
00600332  41 5D                           pop r13
00600334  41 5C                           pop r12
00600336  5F                              pop rdi
00600337  5E                              pop rsi
00600338  5D                              pop rbp
00600339  5B                              pop rbx
0060033A  C3                              ret
0060033B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall inflate_fast_chunk_(__int64 a1, int a2)
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
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_rsp = (v_rsp) - (88);
    a2 = (unsigned int)((a2) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8))) - (14));
    a1 = (*(unsigned __int64 *)(a1 + 16)) - ((unsigned int)(a2));
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 60)));
    v_r12 = ((unsigned int)(*(unsigned int *)(a1 + 24)) - 259) + (*(unsigned __int64 *)(a1 + 16));
    v_r15 = (v_r15) + (*(unsigned __int64 *)(a1));
    v_stack_m50 = a1;
    v_r13 = ((unsigned int)(*(unsigned int *)(a1 + 24))) + (*(unsigned __int64 *)(a1 + 16));
    v_stack_m78 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 56)));
    v_stack_m74 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 52)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 60))) != 0) goto loc_005FFEBE;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 56)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 52))))) {
        v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 52)));
    }
    v_rbx = (unsigned int)((1) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 112)))));
    v_rbx = (unsigned int)((v_rbx) - 1);
    v_r10 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 116)))));
    v_stack_m70 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 64);
    v_r10 = (unsigned int)((v_r10) - 1);
    v_stack_p18 = (unsigned int)(v_r10);
    v_stack_m68 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 96);
    v_stack_m58 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 104);
    v_stack_m60 = v_rbx;
loc_005FFF08:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1))) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 76))))));
    v_rbp = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 72))) | (result);
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 76))))) >> (3);
    result = (7) - (a1);
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 76))) | (56));
    v_r14 = (*(unsigned __int64 *)(a1)) + (result);
    result = (v_rbx) & (v_rbp);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 96) + result * 4)) != 0) goto loc_005FFF7C;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 16)) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 96) + result * 4 + 2));
    a4 = (*(unsigned __int64 *)(a1 + 16)) + 1;
    v_r11 = (unsigned int)((v_r11) - ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 96) + result * 4 + 1))));
    v_rbp = (v_rbp) >> ((unsigned __int8)((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 96) + result * 4 + 1))));
    result = (v_rbx) & (v_rbp);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 96) + result * 4)) == 0) {
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 96) + result * 4 + 2);
        *(unsigned __int8 *)(a4) = (unsigned __int8)(result);
        a4 = (a4) + 1;
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 96) + result * 4 + 1);
        a1 = (unsigned __int8)(result);
        v_r11 = (unsigned int)((v_r11) - ((unsigned int)(result)));
        v_rbp = (v_rbp) >> ((unsigned __int8)(a1));
        result = v_rbx;
        result = (result) & (v_rbp);
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 96) + result * 4;
    }
    v_rbp = (v_rbp) >> ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1)));
    v_r11 = (unsigned int)((v_r11) - ((unsigned int)(*(unsigned __int8 *)(a2 + 1))));
    if ((unsigned int)(*(unsigned __int8 *)(a2)) == 0) goto loc_0060029B;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a2))) & (16)) != 0) goto loc_005FFFB9;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a2))) & (64)) != 0) goto loc_006002B4;
    result = (unsigned int)((1) << ((unsigned __int8)(*(unsigned __int8 *)(a2))));
    a1 = (result - 1) & (v_rbp);
    a1 = (a1) + (*(unsigned __int16 *)(a2 + 2));
    goto loc_005FFF7C;
loc_005FFFB9:
    a1 = (unsigned int)((a1) & (15));
    result = *(unsigned __int16 *)(a2 + 2);
    v_rbx = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 96) + a1 * 4 + 2);
    if (!(condition_is_equal)) {
        result = 1;
        result = (unsigned int)((result) << ((unsigned __int8)(a1)));
        result = (unsigned int)((result) - 1);
        result = (unsigned int)((result) & ((unsigned int)(v_rbp)));
        v_rbp = (v_rbp) >> ((unsigned __int8)(a1));
        v_rbx = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 96) + a1 * 4 + 2)) + ((unsigned int)(result)));
        v_r11 = (unsigned int)((v_r11) - ((unsigned int)(a1)));
    }
    result = ((unsigned int)((unsigned int)(v_r10))) & (v_rbp);
loc_005FFFE4:
    v_r11 = (unsigned int)((v_r11) - ((unsigned int)(*(unsigned __int8 *)(v_stack_m58 + result * 4 + 1))));
    v_rbp = (v_rbp) >> ((unsigned __int8)(*(unsigned __int8 *)(v_stack_m58 + result * 4 + 1)));
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_m58 + result * 4))) & (16)) != 0) goto loc_0060001E;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_m58 + result * 4))) & (64)) != 0) goto loc_006002CB;
    result = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_stack_m58 + result * 4))))));
    a1 = (result - 1) & (v_rbp);
    a1 = (a1) + (*(unsigned __int16 *)(v_stack_m58 + result * 4 + 2));
    goto loc_005FFFE4;
loc_0060001E:
    a2 = (unsigned int)((*(unsigned __int8 *)(v_stack_m58 + result * 4)) & (15));
    result = *(unsigned __int16 *)(v_stack_m58 + result * 4 + 2);
    if (((unsigned int)(v_r11)) < a2) {
        result = *(unsigned __int64 *)(v_r14);
        a1 = (unsigned int)(v_r11);
        result = (result) << ((unsigned __int8)(a1));
        v_rbp = (v_rbp) | (result);
        a1 = (unsigned int)(v_r11);
        a1 = (a1) >> (3);
        result = 7;
        result = (result) - (a1);
        v_r14 = (v_r14) + (result);
        v_r11 = (unsigned int)((v_r11) | (56));
    }
    result = (unsigned int)((1) << ((unsigned __int8)((unsigned int)(a2))));
    v_r11 = (unsigned int)((v_r11) - (a2));
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) & ((unsigned int)(v_rbp)));
    v_rbp = (v_rbp) >> ((unsigned __int8)((unsigned int)(a2)));
    v_r10 = (unsigned int)((*(unsigned __int16 *)(v_stack_m58 + a1 * 4 + 2)) + ((unsigned int)(result)));
    result = (unsigned int)(((unsigned int)((unsigned int)(a4))) - (v_stack_m50));
    v_stack_p8 = (unsigned int)(v_r10);
    if (((unsigned int)(v_r10)) <= ((unsigned int)(result))) goto loc_0060028B;
    v_r10 = (unsigned int)((v_r10) - ((unsigned int)(result)));
    if (((unsigned int)(v_r10)) <= v_stack_m78) goto loc_00600092;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 9056)) != 0) goto loc_006002D4;
loc_00600092:
    if (((unsigned int)((unsigned int)(v_stack_p10))) < ((unsigned int)(v_r10))) goto loc_006000AD;
    result = (unsigned int)(((unsigned int)(v_stack_p10)) - ((unsigned int)(v_r10)));
    a2 = ((unsigned int)((unsigned int)(result))) + (v_stack_m70);
    goto loc_0060013B;
loc_006000AD:
    v_r10 = (unsigned int)((v_r10) - ((unsigned int)(result)));
    a2 = (unsigned int)(((unsigned int)(v_stack_m74)) - ((unsigned int)(v_r10)));
    a2 = (a2) + (v_stack_m70);
    if (((unsigned int)(v_r10)) >= ((unsigned int)(v_rbx))) goto loc_00600215;
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)(v_r10)));
    result = (v_r13) - (a4);
    if (result >= 16) goto loc_00600120;
    if ((((unsigned __int8)(v_r10)) & (8)) != 0) {
        result = *(unsigned __int64 *)(a2);
        *(unsigned __int64 *)(a4) = result;
        a4 = (a4) + (8);
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
    if ((((unsigned __int8)(v_r10)) & (1)) == 0) goto loc_0060012E;
    *(unsigned __int8 *)(a4) = (unsigned __int8)(*(unsigned __int8 *)(a2));
    a4 = (a4) + 1;
    goto loc_0060012E;
loc_00600120:
    result = chunkcopy_core(a4, a2, (unsigned int)((unsigned int)(v_r10)), a4);
loc_0060012E:
loc_0060013B:
    if (((unsigned int)((unsigned int)(v_stack_p10))) >= ((unsigned int)(v_rbx))) goto loc_00600215;
    result = (v_r13) - (result);
    if (result >= 16) goto loc_0060019C;
    if ((((unsigned __int8)((unsigned int)(v_stack_p10))) & (8)) != 0) {
        result = *(unsigned __int64 *)(v_stack_m70);
        *(unsigned __int64 *)(result) = result;
        a4 = (result) + (8);
        a2 = (v_stack_m70) + (8);
    }
    if ((((unsigned __int8)((unsigned int)(v_stack_p10))) & (4)) != 0) {
        result = *(unsigned int *)(a2);
        *(unsigned int *)(a4) = (unsigned int)(result);
        a4 = (a4) + (4);
        a2 = (a2) + (4);
    }
    if ((((unsigned __int8)((unsigned int)(v_stack_p10))) & (2)) != 0) {
        result = *(unsigned __int16 *)(a2);
        *(unsigned __int16 *)(a4) = (unsigned __int16)(result);
        a4 = (a4) + (2);
        a2 = (a2) + (2);
    }
    if ((((unsigned __int8)((unsigned int)(v_stack_p10))) & (1)) == 0) goto loc_006001AA;
    *(unsigned __int8 *)(a4) = (unsigned __int8)(*(unsigned __int8 *)(a2));
    a4 = (a4) + 1;
    goto loc_006001AA;
loc_0060019C:
    result = chunkcopy_core(a4, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_p10))), a4);
loc_006001AA:
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)((unsigned int)(v_stack_p10))));
    v_stack_p20 = (unsigned int)(v_rbx);
    result = chunkunroll_relaxed(result, v_stack_p8, v_stack_p20, result);
    result = (v_r13) - (result);
    if (result >= 48) goto loc_0060020C;
    if ((unsigned int)((unsigned int)(v_stack_p20)) == 0) goto loc_00600277;
    a1 = (result) - ((unsigned int)(v_stack_p8));
loc_006001F9:
    a1 = (a1) + 1;
    *(unsigned __int8 *)(result) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    a4 = (result) + 1;
    a3 = (unsigned int)(((unsigned int)(v_stack_p20)) + (-1));
    if (condition_is_not_equal) goto loc_006001F9;
    goto loc_00600277;
loc_0060020C:
    goto loc_00600291;
loc_00600215:
    result = (v_r13) - (a4);
    if (result >= 16) goto loc_00600269;
    if ((((unsigned __int8)(v_rbx)) & (8)) != 0) {
        result = *(unsigned __int64 *)((unsigned int)(v_stack_p8));
        *(unsigned __int64 *)(a4) = result;
        a4 = (a4) + (8);
        a2 = ((unsigned int)(v_stack_p8)) + (8);
    }
    if ((((unsigned __int8)(v_rbx)) & (4)) != 0) {
        result = *(unsigned int *)(a2);
        *(unsigned int *)(a4) = (unsigned int)(result);
        a4 = (a4) + (4);
        a2 = (a2) + (4);
    }
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) {
        result = *(unsigned __int16 *)(a2);
        *(unsigned __int16 *)(a4) = (unsigned __int16)(result);
        a4 = (a4) + (2);
        a2 = (a2) + (2);
    }
    if ((((unsigned __int8)(v_rbx)) & (1)) == 0) goto loc_00600277;
    *(unsigned __int8 *)(a4) = (unsigned __int8)(*(unsigned __int8 *)(a2));
    a4 = (a4) + 1;
    goto loc_00600277;
loc_00600269:
    result = chunkcopy_core(a4, a2, (unsigned int)((unsigned int)(v_rbx)), a4);
loc_00600274:
loc_00600277:
    goto loc_006002A4;
loc_0060028B:
loc_00600291:
    result = chunkcopy_lapped_relaxed(result, (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), (unsigned int)((unsigned int)(v_stack_m60)), result);
    goto loc_00600274;
loc_0060029B:
    *(unsigned __int8 *)(result) = (unsigned __int8)(*(unsigned __int8 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))) + 2));
    a4 = (result) + 1;
loc_006002A4:
    if (v_r14 >= v_r15) goto loc_006002E6;
    if (a4 < v_r12) goto loc_005FFF08;
    goto loc_006002E6;
loc_006002B4:
    if ((((unsigned __int8)(result)) & (32)) == 0) goto loc_006002C2;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F3FULL;
    goto loc_006002E6;
loc_006002C2:
    goto loc_006002DB;
loc_006002CB:
    goto loc_006002DB;
loc_006002D4:
loc_006002DB:
    *(unsigned __int64 *)(a1 + 32) = v_rip + 840293;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 8) = 0x3F51ULL;
loc_006002E6:
    *(unsigned __int64 *)(a1 + 16) = a4;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r11))) >> (3));
    v_r12 = (unsigned int)((v_r12) - ((unsigned int)(a4)));
    v_r14 = (v_r14) - (result);
    v_r12 = (unsigned int)((v_r12) + (259));
    result = (unsigned int)((result) << (3));
    v_r15 = (unsigned int)((v_r15) - ((unsigned int)(v_r14)));
    v_r11 = (unsigned int)((v_r11) - ((unsigned int)(result)));
    *(unsigned __int64 *)(a1) = v_r14;
    v_r15 = (unsigned int)((v_r15) + (14));
    *(unsigned int *)(a1 + 24) = (unsigned int)(v_r12);
    *(unsigned int *)(a1 + 8) = (unsigned int)(v_r15);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 76) = (unsigned int)(v_r11);
    result = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r11)))));
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) & ((unsigned int)(v_rbp)));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 72) = (unsigned int)(result);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t inflate_fast_chunk_(void *Arg1, int32_t Arg2)
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
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    local_rsp = (local_rsp) - (88);
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8))) - (14));
    Arg1 = (*(uint64_t *)(arg1 + 0x10)) - ((uint32_t)(Arg2));
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x3C)));
    local_r12 = ((uint32_t)(*(uint32_t *)(arg1 + 0x18)) - 259) + (*(uint64_t *)(arg1 + 0x10));
    local_r15 = (local_r15) + (*(uint64_t *)(arg1));
    v_stack_m50 = Arg1;
    local_r13 = ((uint32_t)(*(uint32_t *)(arg1 + 0x18))) + (*(uint64_t *)(arg1 + 0x10));
    v_stack_m78 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x38)));
    v_stack_m74 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x34)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x3C))) != 0) goto loc_005FFEBE;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x38)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x34))))) {
        v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x34)));
    }
    local_rbx = (uint32_t)((1) << ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x70)))));
    local_rbx = (uint32_t)((local_rbx) - 1);
    local_r10 = (uint32_t)((1) << ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x74)))));
    v_stack_m70 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x40);
    local_r10 = (uint32_t)((local_r10) - 1);
    v_stack_p18 = (uint32_t)(local_r10);
    v_stack_m68 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x60);
    v_stack_m58 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x68);
    v_stack_m60 = local_rbx;
loc_005FFF08:
    result = (*(uint64_t *)(*(uint64_t *)(arg1))) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x4C))))));
    local_rbp = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x48))) | (result);
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x4C))))) >> (3);
    result = (7) - (Arg1);
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x4C))) | (56));
    local_r14 = (*(uint64_t *)(arg1)) + (result);
    result = (local_rbx) & (local_rbp);
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x60) + result * 4)) != 0) goto loc_005FFF7C;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x10)) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x60) + result * 4 + 0x2));
    a4 = (*(uint64_t *)(arg1 + 0x10)) + 1;
    local_r11 = (uint32_t)((local_r11) - ((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x60) + result * 4 + 0x1))));
    local_rbp = (local_rbp) >> ((uint8_t)((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x60) + result * 4 + 0x1))));
    result = (local_rbx) & (local_rbp);
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x60) + result * 4)) == 0) {
        result = *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x60) + result * 4 + 0x2);
        *(uint8_t *)(a4) = (uint8_t)(result);
        a4 = (a4) + 1;
        result = *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x60) + result * 4 + 0x1);
        Arg1 = (uint8_t)(result);
        local_r11 = (uint32_t)((local_r11) - ((uint32_t)(result)));
        local_rbp = (local_rbp) >> ((uint8_t)(Arg1));
        result = local_rbx;
        result = (result) & (local_rbp);
        Arg2 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x60) + result * 4;
    }
    local_rbp = (local_rbp) >> ((uint8_t)(*(uint8_t *)(Arg2 + 0x1)));
    local_r11 = (uint32_t)((local_r11) - ((uint32_t)(*(uint8_t *)(Arg2 + 0x1))));
    if ((uint32_t)(*(uint8_t *)(Arg2)) == 0) goto loc_0060029B;
    if ((((uint8_t)(*(uint8_t *)(Arg2))) & (16)) != 0) goto loc_005FFFB9;
    if ((((uint8_t)(*(uint8_t *)(Arg2))) & (64)) != 0) goto loc_006002B4;
    result = (uint32_t)((1) << ((uint8_t)(*(uint8_t *)(Arg2))));
    Arg1 = (result - 1) & (local_rbp);
    Arg1 = (Arg1) + (*(uint16_t *)(Arg2 + 0x2));
    goto loc_005FFF7C;
loc_005FFFB9:
    Arg1 = (uint32_t)((Arg1) & (15));
    result = *(uint16_t *)(Arg2 + 0x2);
    local_rbx = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x60) + arg1 * 4 + 0x2);
    if (!(condition_is_equal)) {
        result = 1;
        result = (uint32_t)((result) << ((uint8_t)(Arg1)));
        result = (uint32_t)((result) - 1);
        result = (uint32_t)((result) & ((uint32_t)(local_rbp)));
        local_rbp = (local_rbp) >> ((uint8_t)(Arg1));
        local_rbx = (uint32_t)((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x60) + arg1 * 4 + 0x2)) + ((uint32_t)(result)));
        local_r11 = (uint32_t)((local_r11) - ((uint32_t)(Arg1)));
    }
    result = ((uint32_t)((uint32_t)(local_r10))) & (local_rbp);
loc_005FFFE4:
    local_r11 = (uint32_t)((local_r11) - ((uint32_t)(*(uint8_t *)(v_stack_m58 + result * 4 + 0x1))));
    local_rbp = (local_rbp) >> ((uint8_t)(*(uint8_t *)(v_stack_m58 + result * 4 + 0x1)));
    if ((((uint8_t)(*(uint8_t *)(v_stack_m58 + result * 4))) & (16)) != 0) goto loc_0060001E;
    if ((((uint8_t)(*(uint8_t *)(v_stack_m58 + result * 4))) & (64)) != 0) goto loc_006002CB;
    result = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(*(uint8_t *)(v_stack_m58 + result * 4))))));
    Arg1 = (result - 1) & (local_rbp);
    Arg1 = (Arg1) + (*(uint16_t *)(v_stack_m58 + result * 4 + 0x2));
    goto loc_005FFFE4;
loc_0060001E:
    Arg2 = (uint32_t)((*(uint8_t *)(v_stack_m58 + result * 4)) & (15));
    result = *(uint16_t *)(v_stack_m58 + result * 4 + 0x2);
    if (((uint32_t)(local_r11)) < Arg2) {
        result = *(uint64_t *)(local_r14);
        Arg1 = (uint32_t)(local_r11);
        result = (result) << ((uint8_t)(Arg1));
        local_rbp = (local_rbp) | (result);
        Arg1 = (uint32_t)(local_r11);
        Arg1 = (Arg1) >> (3);
        result = 7;
        result = (result) - (Arg1);
        local_r14 = (local_r14) + (result);
        local_r11 = (uint32_t)((local_r11) | (56));
    }
    result = (uint32_t)((1) << ((uint8_t)((uint32_t)(Arg2))));
    local_r11 = (uint32_t)((local_r11) - (Arg2));
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) & ((uint32_t)(local_rbp)));
    local_rbp = (local_rbp) >> ((uint8_t)((uint32_t)(Arg2)));
    local_r10 = (uint32_t)((*(uint16_t *)(v_stack_m58 + arg1 * 4 + 0x2)) + ((uint32_t)(result)));
    result = (uint32_t)(((uint32_t)((uint32_t)(a4))) - (v_stack_m50));
    v_stack_p8 = (uint32_t)(local_r10);
    if (((uint32_t)(local_r10)) <= ((uint32_t)(result))) goto loc_0060028B;
    local_r10 = (uint32_t)((local_r10) - ((uint32_t)(result)));
    if (((uint32_t)(local_r10)) <= v_stack_m78) goto loc_00600092;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x2360)) != 0) goto loc_006002D4;
loc_00600092:
    if (((uint32_t)((uint32_t)(v_stack_p10))) < ((uint32_t)(local_r10))) goto loc_006000AD;
    result = (uint32_t)(((uint32_t)(v_stack_p10)) - ((uint32_t)(local_r10)));
    Arg2 = ((uint32_t)((uint32_t)(result))) + (v_stack_m70);
    goto loc_0060013B;
loc_006000AD:
    local_r10 = (uint32_t)((local_r10) - ((uint32_t)(result)));
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m74)) - ((uint32_t)(local_r10)));
    Arg2 = (Arg2) + (v_stack_m70);
    if (((uint32_t)(local_r10)) >= ((uint32_t)(local_rbx))) goto loc_00600215;
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)(local_r10)));
    result = (local_r13) - (a4);
    if (result >= 16) goto loc_00600120;
    if ((((uint8_t)(local_r10)) & (8)) != 0) {
        result = *(uint64_t *)(Arg2);
        *(uint64_t *)(a4) = result;
        a4 = (a4) + (8);
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
    if ((((uint8_t)(local_r10)) & (1)) == 0) goto loc_0060012E;
    *(uint8_t *)(a4) = (uint8_t)(*(uint8_t *)(Arg2));
    a4 = (a4) + 1;
    goto loc_0060012E;
loc_00600120:
    result = chunkcopy_core(a4, Arg2, (uint32_t)((uint32_t)(local_r10)), a4);
loc_0060012E:
loc_0060013B:
    if (((uint32_t)((uint32_t)(v_stack_p10))) >= ((uint32_t)(local_rbx))) goto loc_00600215;
    result = (local_r13) - (result);
    if (result >= 16) goto loc_0060019C;
    if ((((uint8_t)((uint32_t)(v_stack_p10))) & (8)) != 0) {
        result = *(uint64_t *)(v_stack_m70);
        *(uint64_t *)(result) = result;
        a4 = (result) + (8);
        Arg2 = (v_stack_m70) + (8);
    }
    if ((((uint8_t)((uint32_t)(v_stack_p10))) & (4)) != 0) {
        result = *(uint32_t *)(Arg2);
        *(uint32_t *)(a4) = (uint32_t)(result);
        a4 = (a4) + (4);
        Arg2 = (Arg2) + (4);
    }
    if ((((uint8_t)((uint32_t)(v_stack_p10))) & (2)) != 0) {
        result = *(uint16_t *)(Arg2);
        *(uint16_t *)(a4) = (uint16_t)(result);
        a4 = (a4) + (2);
        Arg2 = (Arg2) + (2);
    }
    if ((((uint8_t)((uint32_t)(v_stack_p10))) & (1)) == 0) goto loc_006001AA;
    *(uint8_t *)(a4) = (uint8_t)(*(uint8_t *)(Arg2));
    a4 = (a4) + 1;
    goto loc_006001AA;
loc_0060019C:
    result = chunkcopy_core(a4, Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_p10))), a4);
loc_006001AA:
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)((uint32_t)(v_stack_p10))));
    v_stack_p20 = (uint32_t)(local_rbx);
    result = chunkunroll_relaxed(result, v_stack_p8, v_stack_p20, result);
    result = (local_r13) - (result);
    if (result >= 48) goto loc_0060020C;
    if ((uint32_t)((uint32_t)(v_stack_p20)) == 0) goto loc_00600277;
    Arg1 = (result) - ((uint32_t)(v_stack_p8));
loc_006001F9:
    Arg1 = (Arg1) + 1;
    *(uint8_t *)(result) = (uint8_t)(*(uint8_t *)(arg1));
    a4 = (result) + 1;
    a3 = (uint32_t)(((uint32_t)(v_stack_p20)) + (-1));
    if (condition_is_not_equal) goto loc_006001F9;
    goto loc_00600277;
loc_0060020C:
    goto loc_00600291;
loc_00600215:
    result = (local_r13) - (a4);
    if (result >= 16) goto loc_00600269;
    if ((((uint8_t)(local_rbx)) & (8)) != 0) {
        result = *(uint64_t *)((uint32_t)(v_stack_p8));
        *(uint64_t *)(a4) = result;
        a4 = (a4) + (8);
        Arg2 = ((uint32_t)(v_stack_p8)) + (8);
    }
    if ((((uint8_t)(local_rbx)) & (4)) != 0) {
        result = *(uint32_t *)(Arg2);
        *(uint32_t *)(a4) = (uint32_t)(result);
        a4 = (a4) + (4);
        Arg2 = (Arg2) + (4);
    }
    if ((((uint8_t)(local_rbx)) & (2)) != 0) {
        result = *(uint16_t *)(Arg2);
        *(uint16_t *)(a4) = (uint16_t)(result);
        a4 = (a4) + (2);
        Arg2 = (Arg2) + (2);
    }
    if ((((uint8_t)(local_rbx)) & (1)) == 0) goto loc_00600277;
    *(uint8_t *)(a4) = (uint8_t)(*(uint8_t *)(Arg2));
    a4 = (a4) + 1;
    goto loc_00600277;
loc_00600269:
    result = chunkcopy_core(a4, Arg2, (uint32_t)((uint32_t)(local_rbx)), a4);
loc_00600274:
loc_00600277:
    goto loc_006002A4;
loc_0060028B:
loc_00600291:
    result = chunkcopy_lapped_relaxed(result, (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), (uint32_t)((uint32_t)(v_stack_m60)), result);
    goto loc_00600274;
loc_0060029B:
    *(uint8_t *)(result) = (uint8_t)(*(uint8_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))) + 0x2));
    a4 = (result) + 1;
loc_006002A4:
    if (local_r14 >= local_r15) goto loc_006002E6;
    if (a4 < local_r12) goto loc_005FFF08;
    goto loc_006002E6;
loc_006002B4:
    if ((((uint8_t)(result)) & (32)) == 0) goto loc_006002C2;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F3FULL;
    goto loc_006002E6;
loc_006002C2:
    goto loc_006002DB;
loc_006002CB:
    goto loc_006002DB;
loc_006002D4:
loc_006002DB:
    *(uint64_t *)(arg1 + 0x20) = v_rip + 840293;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x8) = 0x3F51ULL;
loc_006002E6:
    *(uint64_t *)(arg1 + 0x10) = a4;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r11))) >> (3));
    local_r12 = (uint32_t)((local_r12) - ((uint32_t)(a4)));
    local_r14 = (local_r14) - (result);
    local_r12 = (uint32_t)((local_r12) + (259));
    result = (uint32_t)((result) << (3));
    local_r15 = (uint32_t)((local_r15) - ((uint32_t)(local_r14)));
    local_r11 = (uint32_t)((local_r11) - ((uint32_t)(result)));
    *(uint64_t *)(arg1) = local_r14;
    local_r15 = (uint32_t)((local_r15) + (14));
    *(uint32_t *)(arg1 + 0x18) = (uint32_t)(local_r12);
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)(local_r15);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x4C) = (uint32_t)(local_r11);
    result = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(local_r11)))));
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) & ((uint32_t)(local_rbp)));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x48) = (uint32_t)(result);
    local_rsp = (local_rsp) + (88);
    return result;
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
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x18` | `32` | `W` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005FFE4C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
