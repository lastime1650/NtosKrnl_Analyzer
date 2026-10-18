# winput_s

- RVA: `0x00508E78`–`0x0050981D` (길이 `2,469` bytes)
- VA: `0x0000000140508E78`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C29B0`
- 디코드: `714`개 명령, `2,469/2,469` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **22**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00508EF8` → [iswctype](iswctype_function_00502900.md) (function, `0x00502900`)
- `0x00508F0F` → [_whiteout](_whiteout_function_00508E20.md) (function, `0x00508E20`)
- `0x00508F24` → [ungetwc_nolock](ungetwc_nolock_function_00509900.md) (function, `0x00509900`)
- `0x00508F36` → [iswctype](iswctype_function_00502900.md) (function, `0x00502900`)
- `0x0050914D` → [_whiteout](_whiteout_function_00508E20.md) (function, `0x00508E20`)
- `0x00509163` → [fgetwc_nolock](fgetwc_nolock_function_005098B4.md) (function, `0x005098B4`)
- `0x005092F9` → [fgetwc_nolock](fgetwc_nolock_function_005098B4.md) (function, `0x005098B4`)
- `0x0050934F` → [fgetwc_nolock](fgetwc_nolock_function_005098B4.md) (function, `0x005098B4`)
- `0x00509377` → [ungetwc_nolock](ungetwc_nolock_function_00509900.md) (function, `0x00509900`)
- `0x0050938D` → [fgetwc_nolock](fgetwc_nolock_function_005098B4.md) (function, `0x005098B4`)
- `0x005093E8` → [fgetwc_nolock](fgetwc_nolock_function_005098B4.md) (function, `0x005098B4`)
- `0x005094D0` → [fgetwc_nolock](fgetwc_nolock_function_005098B4.md) (function, `0x005098B4`)
- `0x00509500` → [ungetwc_nolock](ungetwc_nolock_function_00509900.md) (function, `0x00509900`)
- `0x005095DC` → [fgetwc_nolock](fgetwc_nolock_function_005098B4.md) (function, `0x005098B4`)
- `0x0050960C` → [ungetwc_nolock](ungetwc_nolock_function_00509900.md) (function, `0x00509900`)
- `0x005096BF` → [ReadStringDelimited](ReadStringDelimited_function_00508BF8.md) (function, `0x00508BF8`)
- `0x005096CC` → [ReadString](ReadString_function_005089B0.md) (function, `0x005089B0`)
- `0x0050970E` → [fgetwc_nolock](fgetwc_nolock_function_005098B4.md) (function, `0x005098B4`)
- `0x00509788` → [ungetwc_nolock](ungetwc_nolock_function_00509900.md) (function, `0x00509900`)
- `0x005097A5` → [ungetwc_nolock](ungetwc_nolock_function_00509900.md) (function, `0x00509900`)
- `0x005097D2` → [EmpCheckErrataList](../49/EmpCheckErrataList_function_0049E550.md) (function, `0x0049E550`)
- `0x00509800` → [EmpCheckErrataList](../49/EmpCheckErrataList_function_0049E550.md) (function, `0x0049E550`)

### Direct callers
- [swinput_s](swinput_s_function_00508DA4.md) at `0x00508DF5`

### Static image references
- `0x00508FA4` → RVA `0x00E00000` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00508E78  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00508E7D  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00508E82  55                              push rbp
00508E83  53                              push rbx
00508E84  56                              push rsi
00508E85  57                              push rdi
00508E86  41 54                           push r12
00508E88  41 55                           push r13
00508E8A  41 56                           push r14
00508E8C  41 57                           push r15
00508E8E  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
00508E93  48 81 EC B8 00 00 00            sub rsp, 0xb8
00508E9A  33 DB                           xor ebx, ebx
00508E9C  4C 8B F2                        mov r14, rdx
00508E9F  48 89 5D E7                     mov qword ptr [rbp - 0x19], rbx
00508EA3  0F B7 FB                        movzx edi, bx
00508EA6  89 7D CF                        mov dword ptr [rbp - 0x31], edi
00508EA9  48 8B F1                        mov rsi, rcx
00508EAC  66 89 5D B7                     mov word ptr [rbp - 0x49], bx
00508EB0  44 8B C3                        mov r8d, ebx
00508EB3  48 89 5D F7                     mov qword ptr [rbp - 9], rbx
00508EB7  48 85 D2                        test rdx, rdx
00508EBA  0F 84 34 09 00 00               je 0x1405097f4
00508EC0  48 85 C9                        test rcx, rcx
00508EC3  0F 84 2B 09 00 00               je 0x1405097f4
00508EC9  41 0F B7 06                     movzx eax, word ptr [r14]
00508ECD  8A D3                           mov dl, bl
00508ECF  88 5D 7F                        mov byte ptr [rbp + 0x7f], bl
00508ED2  44 8B FB                        mov r15d, ebx
00508ED5  89 5D BF                        mov dword ptr [rbp - 0x41], ebx
00508ED8  8B CB                           mov ecx, ebx
00508EDA  89 5D CB                        mov dword ptr [rbp - 0x35], ebx
00508EDD  41 BC FF FF 00 00               mov r12d, 0xffff
00508EE3  66 85 C0                        test ax, ax
00508EE6  0F 84 C7 08 00 00               je 0x1405097b3
00508EEC  44 8D 6B 25                     lea r13d, [rbx + 0x25]
00508EF0  BA 08 00 00 00                  mov edx, 8
00508EF5  0F B7 C8                        movzx ecx, ax
00508EF8  E8 03 9A FF FF                  call 0x140502900
00508EFD  85 C0                           test eax, eax
00508EFF  74 4D                           je 0x140508f4e
00508F01  41 FF CF                        dec r15d
00508F04  48 8D 4D BF                     lea rcx, [rbp - 0x41]
00508F08  48 8B D6                        mov rdx, rsi
00508F0B  44 89 7D BF                     mov dword ptr [rbp - 0x41], r15d
00508F0F  E8 0C FF FF FF                  call 0x140508e20
00508F14  B9 FF FF 00 00                  mov ecx, 0xffff
00508F19  66 3B C8                        cmp cx, ax
00508F1C  74 0B                           je 0x140508f29
00508F1E  48 8B D6                        mov rdx, rsi
00508F21  0F B7 C8                        movzx ecx, ax
00508F24  E8 D7 09 00 00                  call 0x140509900
00508F29  49 83 C6 02                     add r14, 2
00508F2D  BA 08 00 00 00                  mov edx, 8
00508F32  41 0F B7 0E                     movzx ecx, word ptr [r14]
00508F36  E8 C5 99 FF FF                  call 0x140502900
00508F3B  85 C0                           test eax, eax
00508F3D  75 EA                           jne 0x140508f29
00508F3F  44 8B 7D BF                     mov r15d, dword ptr [rbp - 0x41]
00508F43  41 BC FF FF 00 00               mov r12d, 0xffff
00508F49  E9 F6 07 00 00                  jmp 0x140509744
00508F4E  66 45 3B 2E                     cmp r13w, word ptr [r14]
00508F52  0F 85 AC 07 00 00               jne 0x140509704
00508F58  66 45 3B 6E 02                  cmp r13w, word ptr [r14 + 2]
00508F5D  0F 84 9D 07 00 00               je 0x140509700
00508F63  BF 6C 00 00 00                  mov edi, 0x6c
00508F68  89 5D D7                        mov dword ptr [rbp - 0x29], ebx
00508F6B  89 5D EF                        mov dword ptr [rbp - 0x11], ebx
00508F6E  8B CB                           mov ecx, ebx
00508F70  89 5D C7                        mov dword ptr [rbp - 0x39], ebx
00508F73  44 8B D3                        mov r10d, ebx
00508F76  88 5D C3                        mov byte ptr [rbp - 0x3d], bl
00508F79  44 8A EB                        mov r13b, bl
00508F7C  44 8D 7F B4                     lea r15d, [rdi - 0x4c]
00508F80  44 8A C3                        mov r8b, bl
00508F83  44 8A E3                        mov r12b, bl
00508F86  40 B6 01                        mov sil, 1
00508F89  44 8B DB                        mov r11d, ebx
00508F8C  41 B9 00 FF 00 00               mov r9d, 0xff00
00508F92  49 83 C6 02                     add r14, 2
00508F96  4C 89 75 6F                     mov qword ptr [rbp + 0x6f], r14
00508F9A  41 0F B7 16                     movzx edx, word ptr [r14]
00508F9E  66 41 85 D1                     test r9w, dx
00508FA2  75 26                           jne 0x140508fca
00508FA4  48 8B 05 55 70 8F 00            mov rax, qword ptr [rip + 0x8f7055]
00508FAB  0F B6 CA                        movzx ecx, dl
00508FAE  F6 04 48 04                     test byte ptr [rax + rcx*2], 4
00508FB2  8B 4D C7                        mov ecx, dword ptr [rbp - 0x39]
00508FB5  74 13                           je 0x140508fca
00508FB7  47 8D 14 92                     lea r10d, [r10 + r10*4]
00508FBB  FF C1                           inc ecx
00508FBD  45 8D 52 E8                     lea r10d, [r10 - 0x18]
00508FC1  89 4D C7                        mov dword ptr [rbp - 0x39], ecx
00508FC4  46 8D 14 52                     lea r10d, [rdx + r10*2]
00508FC8  EB 5D                           jmp 0x140509027
00508FCA  83 FA 68                        cmp edx, 0x68
00508FCD  0F 87 C6 00 00 00               ja 0x140509099
00508FD3  0F 84 B8 00 00 00               je 0x140509091
00508FD9  83 FA 2A                        cmp edx, 0x2a
00508FDC  0F 84 AA 00 00 00               je 0x14050908c
00508FE2  83 FA 46                        cmp edx, 0x46
00508FE5  74 40                           je 0x140509027
00508FE7  83 FA 49                        cmp edx, 0x49
00508FEA  74 14                           je 0x140509000
00508FEC  83 FA 4C                        cmp edx, 0x4c
00508FEF  74 0A                           je 0x140508ffb
00508FF1  83 FA 4E                        cmp edx, 0x4e
00508FF4  74 31                           je 0x140509027
00508FF6  E9 E0 00 00 00                  jmp 0x1405090db
00508FFB  40 FE C6                        inc sil
00508FFE  EB 27                           jmp 0x140509027
00509000  41 0F B7 46 02                  movzx eax, word ptr [r14 + 2]
00509005  66 83 F8 36                     cmp ax, 0x36
00509009  75 68                           jne 0x140509073
0050900B  49 8D 46 04                     lea rax, [r14 + 4]
0050900F  66 83 38 34                     cmp word ptr [rax], 0x34
00509013  0F 85 98 00 00 00               jne 0x1405090b1
00509019  4C 8B F0                        mov r14, rax
0050901C  48 89 45 6F                     mov qword ptr [rbp + 0x6f], rax
00509020  48 89 5D E7                     mov qword ptr [rbp - 0x19], rbx
00509024  41 FF C3                        inc r11d
00509027  45 84 C0                        test r8b, r8b
0050902A  0F 84 62 FF FF FF               je 0x140508f92
00509030  8B 7D CF                        mov edi, dword ptr [rbp - 0x31]
00509033  4C 8B CB                        mov r9, rbx
00509036  44 8B 7D BF                     mov r15d, dword ptr [rbp - 0x41]
0050903A  45 8A C5                        mov r8b, r13b
0050903D  44 88 6D C4                     mov byte ptr [rbp - 0x3c], r13b
00509041  40 88 75 BB                     mov byte ptr [rbp - 0x45], sil
00509045  44 89 5D DF                     mov dword ptr [rbp - 0x21], r11d
00509049  44 89 55 D3                     mov dword ptr [rbp - 0x2d], r10d
0050904D  45 84 ED                        test r13b, r13b
00509050  0F 85 A5 00 00 00               jne 0x1405090fb
00509056  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
0050905A  48 89 45 F7                     mov qword ptr [rbp - 9], rax
0050905E  48 83 C0 08                     add rax, 8
00509062  48 89 45 77                     mov qword ptr [rbp + 0x77], rax
00509066  48 8B 50 F8                     mov rdx, qword ptr [rax - 8]
0050906A  48 89 55 FF                     mov qword ptr [rbp - 1], rdx
0050906E  E9 8F 00 00 00                  jmp 0x140509102
00509073  66 83 F8 33                     cmp ax, 0x33
00509077  75 38                           jne 0x1405090b1
00509079  49 8D 46 04                     lea rax, [r14 + 4]
0050907D  66 83 38 32                     cmp word ptr [rax], 0x32
00509081  75 2E                           jne 0x1405090b1
00509083  4C 8B F0                        mov r14, rax
00509086  48 89 45 6F                     mov qword ptr [rbp + 0x6f], rax
0050908A  EB 9B                           jmp 0x140509027
0050908C  41 FE C5                        inc r13b
0050908F  EB 96                           jmp 0x140509027
00509091  40 FE CE                        dec sil
00509094  41 FE CC                        dec r12b
00509097  EB 8E                           jmp 0x140509027
00509099  83 FA 6A                        cmp edx, 0x6a
0050909C  74 82                           je 0x140509020
0050909E  3B D7                           cmp edx, edi
005090A0  74 41                           je 0x1405090e3
005090A2  83 FA 74                        cmp edx, 0x74
005090A5  74 0A                           je 0x1405090b1
005090A7  83 FA 77                        cmp edx, 0x77
005090AA  74 47                           je 0x1405090f3
005090AC  83 FA 7A                        cmp edx, 0x7a
005090AF  75 2A                           jne 0x1405090db
005090B1  41 0F B7 46 02                  movzx eax, word ptr [r14 + 2]
005090B6  66 83 E8 58                     sub ax, 0x58
005090BA  66 41 3B C7                     cmp ax, r15w
005090BE  77 14                           ja 0x1405090d4
005090C0  48 BA 01 10 82 20 01 00 00 00   movabs rdx, 0x120821001
005090CA  48 0F A3 C2                     bt rdx, rax
005090CE  0F 82 4C FF FF FF               jb 0x140509020
005090D4  41 FF C3                        inc r11d
005090D7  48 89 5D E7                     mov qword ptr [rbp - 0x19], rbx
005090DB  41 FE C0                        inc r8b
005090DE  E9 44 FF FF FF                  jmp 0x140509027
005090E3  49 8D 46 02                     lea rax, [r14 + 2]
005090E7  66 39 38                        cmp word ptr [rax], di
005090EA  0F 84 29 FF FF FF               je 0x140509019
005090F0  40 FE C6                        inc sil
005090F3  41 FE C4                        inc r12b
005090F6  E9 2C FF FF FF                  jmp 0x140509027
005090FB  48 8B D3                        mov rdx, rbx
005090FE  48 89 5D FF                     mov qword ptr [rbp - 1], rbx
00509102  48 89 55 07                     mov qword ptr [rbp + 7], rdx
00509106  44 8A EB                        mov r13b, bl
00509109  45 84 E4                        test r12b, r12b
0050910C  75 1D                           jne 0x14050912b
0050910E  41 0F B7 06                     movzx eax, word ptr [r14]
00509112  BE EF FF 00 00                  mov esi, 0xffef
00509117  66 83 E8 43                     sub ax, 0x43
0050911B  66 23 C6                        and ax, si
0050911E  66 F7 D8                        neg ax
00509121  45 1A E4                        sbb r12b, r12b
00509124  41 80 E4 02                     and r12b, 2
00509128  41 FE CC                        dec r12b
0050912B  41 0F B7 36                     movzx esi, word ptr [r14]
0050912F  B8 6E 00 00 00                  mov eax, 0x6e
00509134  83 CE 20                        or esi, 0x20
00509137  3B F0                           cmp esi, eax
00509139  74 5B                           je 0x140509196
0050913B  83 FE 63                        cmp esi, 0x63
0050913E  74 18                           je 0x140509158
00509140  83 FE 7B                        cmp esi, 0x7b
00509143  74 13                           je 0x140509158
00509145  48 8B 55 67                     mov rdx, qword ptr [rbp + 0x67]
00509149  48 8D 4D BF                     lea rcx, [rbp - 0x41]
0050914D  E8 CE FC FF FF                  call 0x140508e20
00509152  44 8B 7D BF                     mov r15d, dword ptr [rbp - 0x41]
00509156  EB 10                           jmp 0x140509168
00509158  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
0050915C  41 FF C7                        inc r15d
0050915F  44 89 7D BF                     mov dword ptr [rbp - 0x41], r15d
00509163  E8 4C 07 00 00                  call 0x1405098b4
00509168  0F B7 F8                        movzx edi, ax
0050916B  66 89 45 B7                     mov word ptr [rbp - 0x49], ax
0050916F  B8 FF FF 00 00                  mov eax, 0xffff
00509174  89 7D CF                        mov dword ptr [rbp - 0x31], edi
00509177  66 3B C7                        cmp ax, di
0050917A  0F 84 5C 06 00 00               je 0x1405097dc
00509180  48 8B 55 FF                     mov rdx, qword ptr [rbp - 1]
00509184  4C 8B CB                        mov r9, rbx
00509187  44 8B 55 D3                     mov r10d, dword ptr [rbp - 0x2d]
0050918B  44 8B 5D DF                     mov r11d, dword ptr [rbp - 0x21]
0050918F  8B 4D C7                        mov ecx, dword ptr [rbp - 0x39]
00509192  44 8A 45 C4                     mov r8b, byte ptr [rbp - 0x3c]
00509196  85 C9                           test ecx, ecx
00509198  74 09                           je 0x1405091a3
0050919A  45 85 D2                        test r10d, r10d
0050919D  0F 84 B0 05 00 00               je 0x140509753
005091A3  45 84 C0                        test r8b, r8b
005091A6  75 3C                           jne 0x1405091e4
005091A8  83 FE 63                        cmp esi, 0x63
005091AB  74 0A                           je 0x1405091b7
005091AD  83 FE 73                        cmp esi, 0x73
005091B0  74 05                           je 0x1405091b7
005091B2  83 FE 7B                        cmp esi, 0x7b
005091B5  75 2D                           jne 0x1405091e4
005091B7  48 8B 45 F7                     mov rax, qword ptr [rbp - 9]
005091BB  48 8B 10                        mov rdx, qword ptr [rax]
005091BE  4C 8D 48 08                     lea r9, [rax + 8]
005091C2  4C 89 4D F7                     mov qword ptr [rbp - 9], r9
005091C6  49 83 C1 08                     add r9, 8
005091CA  4C 89 4D 77                     mov qword ptr [rbp + 0x77], r9
005091CE  44 8B 48 08                     mov r9d, dword ptr [rax + 8]
005091D2  48 89 55 FF                     mov qword ptr [rbp - 1], rdx
005091D6  48 89 55 07                     mov qword ptr [rbp + 7], rdx
005091DA  49 83 F9 01                     cmp r9, 1
005091DE  0F 82 7F 05 00 00               jb 0x140509763
005091E4  83 FE 70                        cmp esi, 0x70
005091E7  0F 87 90 00 00 00               ja 0x14050927d
005091ED  74 7D                           je 0x14050926c
005091EF  8B CE                           mov ecx, esi
005091F1  83 E9 63                        sub ecx, 0x63
005091F4  74 5B                           je 0x140509251
005091F6  83 E9 01                        sub ecx, 1
005091F9  74 13                           je 0x14050920e
005091FB  83 E9 05                        sub ecx, 5
005091FE  74 39                           je 0x140509239
00509200  83 E9 05                        sub ecx, 5
00509203  74 23                           je 0x140509228
00509205  83 F9 01                        cmp ecx, 1
00509208  0F 85 87 00 00 00               jne 0x140509295
0050920E  8B 4D C7                        mov ecx, dword ptr [rbp - 0x39]
00509211  B8 2D 00 00 00                  mov eax, 0x2d
00509216  66 3B C7                        cmp ax, di
00509219  0F 85 9E 01 00 00               jne 0x1405093bd
0050921F  C6 45 C3 01                     mov byte ptr [rbp - 0x3d], 1
00509223  E9 9F 01 00 00                  jmp 0x1405093c7
00509228  41 8B C7                        mov eax, r15d
0050922B  45 84 C0                        test r8b, r8b
0050922E  0F 84 06 04 00 00               je 0x14050963a
00509234  E9 AB 04 00 00                  jmp 0x1405096e4
00509239  8B 4D C7                        mov ecx, dword ptr [rbp - 0x39]
0050923C  BE 64 00 00 00                  mov esi, 0x64
00509241  B8 2D 00 00 00                  mov eax, 0x2d
00509246  66 3B C7                        cmp ax, di
00509249  75 77                           jne 0x1405092c2
0050924B  C6 45 C3 01                     mov byte ptr [rbp - 0x3d], 1
0050924F  EB 7B                           jmp 0x1405092cc
00509251  8B 55 C7                        mov edx, dword ptr [rbp - 0x39]
00509254  B9 10 00 00 00                  mov ecx, 0x10
00509259  85 D2                           test edx, edx
0050925B  0F 85 06 04 00 00               jne 0x140509667
00509261  8D 51 F1                        lea edx, [rcx - 0xf]
00509264  41 FF C2                        inc r10d
00509267  E9 FB 03 00 00                  jmp 0x140509667
0050926C  41 FF C3                        inc r11d
0050926F  C6 45 BB 01                     mov byte ptr [rbp - 0x45], 1
00509273  44 89 5D DF                     mov dword ptr [rbp - 0x21], r11d
00509277  48 89 5D E7                     mov qword ptr [rbp - 0x19], rbx
0050927B  EB 94                           jmp 0x140509211
0050927D  83 FE 73                        cmp esi, 0x73
00509280  0F 84 D9 03 00 00               je 0x14050965f
00509286  83 FE 75                        cmp esi, 0x75
00509289  74 86                           je 0x140509211
0050928B  83 FE 78                        cmp esi, 0x78
0050928E  74 B1                           je 0x140509241
00509290  83 FE 7B                        cmp esi, 0x7b
00509293  74 23                           je 0x1405092b8
00509295  66 41 39 3E                     cmp word ptr [r14], di
00509299  0F 85 D8 04 00 00               jne 0x140509777
0050929F  FE 4D 7F                        dec byte ptr [rbp + 0x7f]
005092A2  45 84 C0                        test r8b, r8b
005092A5  0F 85 39 04 00 00               jne 0x1405096e4
005092AB  4C 8B 45 F7                     mov r8, qword ptr [rbp - 9]
005092AF  4C 89 45 77                     mov qword ptr [rbp + 0x77], r8
005092B3  E9 2C 04 00 00                  jmp 0x1405096e4
005092B8  B9 40 00 00 00                  mov ecx, 0x40
005092BD  E9 A2 03 00 00                  jmp 0x140509664
005092C2  B8 2B 00 00 00                  mov eax, 0x2b
005092C7  66 3B C7                        cmp ax, di
005092CA  75 11                           jne 0x1405092dd
005092CC  41 83 EA 01                     sub r10d, 1
005092D0  44 89 55 D3                     mov dword ptr [rbp - 0x2d], r10d
005092D4  75 6B                           jne 0x140509341
005092D6  85 C9                           test ecx, ecx
005092D8  74 67                           je 0x140509341
005092DA  41 B5 01                        mov r13b, 1
005092DD  4C 8B 65 67                     mov r12, qword ptr [rbp + 0x67]
005092E1  B8 30 00 00 00                  mov eax, 0x30
005092E6  66 3B C7                        cmp ax, di
005092E9  0F 85 08 01 00 00               jne 0x1405093f7
005092EF  41 FF C7                        inc r15d
005092F2  49 8B CC                        mov rcx, r12
005092F5  44 89 7D BF                     mov dword ptr [rbp - 0x41], r15d
005092F9  E8 B6 05 00 00                  call 0x1405098b4
005092FE  0F B7 F8                        movzx edi, ax
00509301  66 89 45 B7                     mov word ptr [rbp - 0x49], ax
00509305  B9 DF FF 00 00                  mov ecx, 0xffdf
0050930A  89 7D CF                        mov dword ptr [rbp - 0x31], edi
0050930D  8D 47 A8                        lea eax, [rdi - 0x58]
00509310  66 85 C1                        test cx, ax
00509313  74 6E                           je 0x140509383
00509315  C7 45 EF 01 00 00 00            mov dword ptr [rbp - 0x11], 1
0050931C  83 FE 78                        cmp esi, 0x78
0050931F  74 3F                           je 0x140509360
00509321  44 8B 45 C7                     mov r8d, dword ptr [rbp - 0x39]
00509325  44 8B 65 D3                     mov r12d, dword ptr [rbp - 0x2d]
00509329  45 85 C0                        test r8d, r8d
0050932C  74 09                           je 0x140509337
0050932E  41 83 EC 01                     sub r12d, 1
00509332  75 03                           jne 0x140509337
00509334  41 FE C5                        inc r13b
00509337  BE 6F 00 00 00                  mov esi, 0x6f
0050933C  E9 BE 00 00 00                  jmp 0x1405093ff
00509341  4C 8B 65 67                     mov r12, qword ptr [rbp + 0x67]
00509345  41 FF C7                        inc r15d
00509348  49 8B CC                        mov rcx, r12
0050934B  44 89 7D BF                     mov dword ptr [rbp - 0x41], r15d
0050934F  E8 60 05 00 00                  call 0x1405098b4
00509354  0F B7 F8                        movzx edi, ax
00509357  66 89 45 B7                     mov word ptr [rbp - 0x49], ax
0050935B  89 7D CF                        mov dword ptr [rbp - 0x31], edi
0050935E  EB 81                           jmp 0x1405092e1
00509360  41 FF CF                        dec r15d
00509363  B8 FF FF 00 00                  mov eax, 0xffff
00509368  44 89 7D BF                     mov dword ptr [rbp - 0x41], r15d
0050936C  66 3B C7                        cmp ax, di
0050936F  74 0B                           je 0x14050937c
00509371  49 8B D4                        mov rdx, r12
00509374  0F B7 CF                        movzx ecx, di
00509377  E8 84 05 00 00                  call 0x140509900
0050937C  BF 30 00 00 00                  mov edi, 0x30
00509381  EB 6D                           jmp 0x1405093f0
00509383  41 FF C7                        inc r15d
00509386  49 8B CC                        mov rcx, r12
00509389  44 89 7D BF                     mov dword ptr [rbp - 0x41], r15d
0050938D  E8 22 05 00 00                  call 0x1405098b4
00509392  44 8B 45 C7                     mov r8d, dword ptr [rbp - 0x39]
00509396  0F B7 F8                        movzx edi, ax
00509399  44 8B 65 D3                     mov r12d, dword ptr [rbp - 0x2d]
0050939D  89 7D CF                        mov dword ptr [rbp - 0x31], edi
005093A0  66 89 45 B7                     mov word ptr [rbp - 0x49], ax
005093A4  45 85 C0                        test r8d, r8d
005093A7  74 0D                           je 0x1405093b6
005093A9  41 83 EC 02                     sub r12d, 2
005093AD  41 83 FC 01                     cmp r12d, 1
005093B1  7D 03                           jge 0x1405093b6
005093B3  41 FE C5                        inc r13b
005093B6  BE 78 00 00 00                  mov esi, 0x78
005093BB  EB 42                           jmp 0x1405093ff
005093BD  B8 2B 00 00 00                  mov eax, 0x2b
005093C2  66 3B C7                        cmp ax, di
005093C5  75 30                           jne 0x1405093f7
005093C7  41 83 EA 01                     sub r10d, 1
005093CB  44 89 55 D3                     mov dword ptr [rbp - 0x2d], r10d
005093CF  75 0C                           jne 0x1405093dd
005093D1  85 C9                           test ecx, ecx
005093D3  74 08                           je 0x1405093dd
005093D5  41 B5 01                        mov r13b, 1
005093D8  45 8B E2                        mov r12d, r10d
005093DB  EB 1E                           jmp 0x1405093fb
005093DD  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
005093E1  41 FF C7                        inc r15d
005093E4  44 89 7D BF                     mov dword ptr [rbp - 0x41], r15d
005093E8  E8 C7 04 00 00                  call 0x1405098b4
005093ED  0F B7 F8                        movzx edi, ax
005093F0  66 89 7D B7                     mov word ptr [rbp - 0x49], di
005093F4  89 7D CF                        mov dword ptr [rbp - 0x31], edi
005093F7  44 8B 65 D3                     mov r12d, dword ptr [rbp - 0x2d]
005093FB  44 8B 45 C7                     mov r8d, dword ptr [rbp - 0x39]
005093FF  39 5D DF                        cmp dword ptr [rbp - 0x21], ebx
00509402  0F 84 17 01 00 00               je 0x14050951f
00509408  45 84 ED                        test r13b, r13b
0050940B  0F 85 F4 00 00 00               jne 0x140509505
00509411  8D 46 90                        lea eax, [rsi - 0x70]
00509414  A9 F7 FF FF FF                  test eax, 0xfffffff7
00509419  B8 00 FF 00 00                  mov eax, 0xff00
0050941E  74 48                           je 0x140509468
00509420  66 85 F8                        test ax, di
00509423  0F 85 BF 00 00 00               jne 0x1405094e8
00509429  48 8B 05 D0 6B 8F 00            mov rax, qword ptr [rip + 0x8f6bd0]
00509430  40 0F B6 CF                     movzx ecx, dil
00509434  F6 04 48 04                     test byte ptr [rax + rcx*2], 4
00509438  0F 84 AA 00 00 00               je 0x1405094e8
0050943E  48 8B 4D E7                     mov rcx, qword ptr [rbp - 0x19]
00509442  83 FE 6F                        cmp esi, 0x6f
00509445  75 13                           jne 0x14050945a
00509447  8D 46 C9                        lea eax, [rsi - 0x37]
0050944A  66 3B C7                        cmp ax, di
0050944D  76 06                           jbe 0x140509455
0050944F  48 C1 E1 03                     shl rcx, 3
00509453  EB 0D                           jmp 0x140509462
00509455  41 B5 01                        mov r13b, 1
00509458  EB 4A                           jmp 0x1405094a4
0050945A  48 8D 04 89                     lea rax, [rcx + rcx*4]
0050945E  48 8D 0C 00                     lea rcx, [rax + rax]
00509462  48 89 4D E7                     mov qword ptr [rbp - 0x19], rcx
00509466  EB 3C                           jmp 0x1405094a4
00509468  66 85 F8                        test ax, di
0050946B  75 7B                           jne 0x1405094e8
0050946D  48 8B 05 8C 6B 8F 00            mov rax, qword ptr [rip + 0x8f6b8c]
00509474  40 0F B6 CF                     movzx ecx, dil
00509478  0F B7 14 48                     movzx edx, word ptr [rax + rcx*2]
0050947C  84 D2                           test dl, dl
0050947E  79 68                           jns 0x1405094e8
00509480  48 8B 4D E7                     mov rcx, qword ptr [rbp - 0x19]
00509484  48 C1 E1 04                     shl rcx, 4
00509488  48 89 4D E7                     mov qword ptr [rbp - 0x19], rcx
0050948C  F6 C2 04                        test dl, 4
0050948F  75 13                           jne 0x1405094a4
00509491  B8 DF FF 00 00                  mov eax, 0xffdf
00509496  66 23 F8                        and di, ax
00509499  66 83 EF 07                     sub di, 7
0050949D  89 7D CF                        mov dword ptr [rbp - 0x31], edi
005094A0  66 89 7D B7                     mov word ptr [rbp - 0x49], di
005094A4  45 84 ED                        test r13b, r13b
005094A7  75 3F                           jne 0x1405094e8
005094A9  FF 45 EF                        inc dword ptr [rbp - 0x11]
005094AC  48 83 C1 D0                     add rcx, -0x30
005094B0  0F B7 C7                        movzx eax, di
005094B3  48 03 C8                        add rcx, rax
005094B6  48 89 4D E7                     mov qword ptr [rbp - 0x19], rcx
005094BA  45 85 C0                        test r8d, r8d
005094BD  74 06                           je 0x1405094c5
005094BF  41 83 EC 01                     sub r12d, 1
005094C3  74 44                           je 0x140509509
005094C5  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
005094C9  41 FF C7                        inc r15d
005094CC  44 89 7D BF                     mov dword ptr [rbp - 0x41], r15d
005094D0  E8 DF 03 00 00                  call 0x1405098b4
005094D5  44 8B 45 C7                     mov r8d, dword ptr [rbp - 0x39]
005094D9  0F B7 F8                        movzx edi, ax
005094DC  89 7D CF                        mov dword ptr [rbp - 0x31], edi
005094DF  66 89 45 B7                     mov word ptr [rbp - 0x49], ax
005094E3  E9 29 FF FF FF                  jmp 0x140509411
005094E8  41 FF CF                        dec r15d
005094EB  B8 FF FF 00 00                  mov eax, 0xffff
005094F0  44 89 7D BF                     mov dword ptr [rbp - 0x41], r15d
005094F4  66 3B C7                        cmp ax, di
005094F7  74 0C                           je 0x140509505
005094F9  48 8B 55 67                     mov rdx, qword ptr [rbp + 0x67]
005094FD  0F B7 CF                        movzx ecx, di
00509500  E8 FB 03 00 00                  call 0x140509900
00509505  48 8B 4D E7                     mov rcx, qword ptr [rbp - 0x19]
00509509  48 8B C1                        mov rax, rcx
0050950C  48 F7 D8                        neg rax
0050950F  38 5D C3                        cmp byte ptr [rbp - 0x3d], bl
00509512  48 0F 44 C1                     cmove rax, rcx
00509516  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
0050951A  E9 FF 00 00 00                  jmp 0x14050961e
0050951F  45 84 ED                        test r13b, r13b
00509522  0F 85 E9 00 00 00               jne 0x140509611
00509528  8D 46 90                        lea eax, [rsi - 0x70]
0050952B  A9 F7 FF FF FF                  test eax, 0xfffffff7
00509530  B8 00 FF 00 00                  mov eax, 0xff00
00509535  74 43                           je 0x14050957a
00509537  66 85 F8                        test ax, di
0050953A  0F 85 B4 00 00 00               jne 0x1405095f4
00509540  48 8B 05 B9 6A 8F 00            mov rax, qword ptr [rip + 0x8f6ab9]
00509547  40 0F B6 CF                     movzx ecx, dil
0050954B  F6 04 48 04                     test byte ptr [rax + rcx*2], 4
0050954F  0F 84 9F 00 00 00               je 0x1405095f4
00509555  8B 4D D7                        mov ecx, dword ptr [rbp - 0x29]
00509558  83 FE 6F                        cmp esi, 0x6f
0050955B  75 12                           jne 0x14050956f
0050955D  8D 46 C9                        lea eax, [rsi - 0x37]
00509560  66 3B C7                        cmp ax, di
00509563  76 05                           jbe 0x14050956a
00509565  C1 E1 03                        shl ecx, 3
00509568  EB 0B                           jmp 0x140509575
0050956A  41 B5 01                        mov r13b, 1
0050956D  EB 44                           jmp 0x1405095b3
0050956F  8D 04 89                        lea eax, [rcx + rcx*4]
00509572  8D 0C 00                        lea ecx, [rax + rax]
00509575  89 4D D7                        mov dword ptr [rbp - 0x29], ecx
00509578  EB 39                           jmp 0x1405095b3
0050957A  66 85 F8                        test ax, di
0050957D  75 75                           jne 0x1405095f4
0050957F  48 8B 05 7A 6A 8F 00            mov rax, qword ptr [rip + 0x8f6a7a]
00509586  40 0F B6 CF                     movzx ecx, dil
0050958A  0F B7 14 48                     movzx edx, word ptr [rax + rcx*2]
0050958E  84 D2                           test dl, dl
00509590  79 62                           jns 0x1405095f4
00509592  8B 4D D7                        mov ecx, dword ptr [rbp - 0x29]
00509595  C1 E1 04                        shl ecx, 4
00509598  89 4D D7                        mov dword ptr [rbp - 0x29], ecx
0050959B  F6 C2 04                        test dl, 4
0050959E  75 13                           jne 0x1405095b3
005095A0  B8 DF FF 00 00                  mov eax, 0xffdf
005095A5  66 23 F8                        and di, ax
005095A8  66 83 EF 07                     sub di, 7
005095AC  89 7D CF                        mov dword ptr [rbp - 0x31], edi
005095AF  66 89 7D B7                     mov word ptr [rbp - 0x49], di
005095B3  45 84 ED                        test r13b, r13b
005095B6  75 3C                           jne 0x1405095f4
005095B8  FF 45 EF                        inc dword ptr [rbp - 0x11]
005095BB  83 C1 D0                        add ecx, -0x30
005095BE  0F B7 C7                        movzx eax, di
005095C1  03 C8                           add ecx, eax
005095C3  89 4D D7                        mov dword ptr [rbp - 0x29], ecx
005095C6  45 85 C0                        test r8d, r8d
005095C9  74 06                           je 0x1405095d1
005095CB  41 83 EC 01                     sub r12d, 1
005095CF  74 43                           je 0x140509614
005095D1  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
005095D5  41 FF C7                        inc r15d
005095D8  44 89 7D BF                     mov dword ptr [rbp - 0x41], r15d
005095DC  E8 D3 02 00 00                  call 0x1405098b4
005095E1  44 8B 45 C7                     mov r8d, dword ptr [rbp - 0x39]
005095E5  0F B7 F8                        movzx edi, ax
005095E8  89 7D CF                        mov dword ptr [rbp - 0x31], edi
005095EB  66 89 45 B7                     mov word ptr [rbp - 0x49], ax
005095EF  E9 34 FF FF FF                  jmp 0x140509528
005095F4  41 FF CF                        dec r15d
005095F7  B8 FF FF 00 00                  mov eax, 0xffff
005095FC  44 89 7D BF                     mov dword ptr [rbp - 0x41], r15d
00509600  66 3B C7                        cmp ax, di
00509603  74 0C                           je 0x140509611
00509605  48 8B 55 67                     mov rdx, qword ptr [rbp + 0x67]
00509609  0F B7 CF                        movzx ecx, di
0050960C  E8 EF 02 00 00                  call 0x140509900
00509611  8B 4D D7                        mov ecx, dword ptr [rbp - 0x29]
00509614  38 5D C3                        cmp byte ptr [rbp - 0x3d], bl
00509617  74 05                           je 0x14050961e
00509619  F7 D9                           neg ecx
0050961B  89 4D D7                        mov dword ptr [rbp - 0x29], ecx
0050961E  39 5D EF                        cmp dword ptr [rbp - 0x11], ebx
00509621  0F 84 83 01 00 00               je 0x1405097aa
00509627  38 5D C4                        cmp byte ptr [rbp - 0x3c], bl
0050962A  0F 85 B4 00 00 00               jne 0x1405096e4
00509630  FF 45 CB                        inc dword ptr [rbp - 0x35]
00509633  48 8B 55 FF                     mov rdx, qword ptr [rbp - 1]
00509637  8B 45 D7                        mov eax, dword ptr [rbp - 0x29]
0050963A  39 5D DF                        cmp dword ptr [rbp - 0x21], ebx
0050963D  74 0C                           je 0x14050964b
0050963F  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
00509643  48 89 02                        mov qword ptr [rdx], rax
00509646  E9 99 00 00 00                  jmp 0x1405096e4
0050964B  38 5D BB                        cmp byte ptr [rbp - 0x45], bl
0050964E  74 07                           je 0x140509657
00509650  89 02                           mov dword ptr [rdx], eax
00509652  E9 8D 00 00 00                  jmp 0x1405096e4
00509657  66 89 02                        mov word ptr [rdx], ax
0050965A  E9 85 00 00 00                  jmp 0x1405096e4
0050965F  B9 20 00 00 00                  mov ecx, 0x20
00509664  8B 55 C7                        mov edx, dword ptr [rbp - 0x39]
00509667  8B C1                           mov eax, ecx
00509669  83 C8 01                        or eax, 1
0050966C  85 D2                           test edx, edx
0050966E  0F 44 C1                        cmove eax, ecx
00509671  8B C8                           mov ecx, eax
00509673  83 C9 02                        or ecx, 2
00509676  45 84 E4                        test r12b, r12b
00509679  0F 4E C8                        cmovle ecx, eax
0050967C  8B C1                           mov eax, ecx
0050967E  83 C8 04                        or eax, 4
00509681  45 84 C0                        test r8b, r8b
00509684  4C 8D 45 B7                     lea r8, [rbp - 0x49]
00509688  0F 44 C1                        cmove eax, ecx
0050968B  48 8D 4D CB                     lea rcx, [rbp - 0x35]
0050968F  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00509694  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
00509698  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
0050969D  4C 8D 4D BF                     lea r9, [rbp - 0x41]
005096A1  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
005096A6  48 8D 4D 07                     lea rcx, [rbp + 7]
005096AA  44 89 54 24 28                  mov dword ptr [rsp + 0x28], r10d
005096AF  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
005096B4  8B C8                           mov ecx, eax
005096B6  83 FE 7B                        cmp esi, 0x7b
005096B9  75 0F                           jne 0x1405096ca
005096BB  48 8D 55 6F                     lea rdx, [rbp + 0x6f]
005096BF  E8 34 F5 FF FF                  call 0x140508bf8
005096C4  4C 8B 75 6F                     mov r14, qword ptr [rbp + 0x6f]
005096C8  EB 07                           jmp 0x1405096d1
005096CA  33 D2                           xor edx, edx
005096CC  E8 DF F2 FF FF                  call 0x1405089b0
005096D1  0F B7 7D B7                     movzx edi, word ptr [rbp - 0x49]
005096D5  85 C0                           test eax, eax
005096D7  0F 85 CD 00 00 00               jne 0x1405097aa
005096DD  44 8B 7D BF                     mov r15d, dword ptr [rbp - 0x41]
005096E1  89 7D CF                        mov dword ptr [rbp - 0x31], edi
005096E4  FE 45 7F                        inc byte ptr [rbp + 0x7f]
005096E7  41 BC FF FF 00 00               mov r12d, 0xffff
005096ED  48 8B 75 67                     mov rsi, qword ptr [rbp + 0x67]
005096F1  49 83 C6 02                     add r14, 2
005096F5  49 8B CE                        mov rcx, r14
005096F8  41 BD 25 00 00 00               mov r13d, 0x25
005096FE  EB 2D                           jmp 0x14050972d
00509700  49 83 C6 02                     add r14, 2
00509704  41 FF C7                        inc r15d
00509707  48 8B CE                        mov rcx, rsi
0050970A  44 89 7D BF                     mov dword ptr [rbp - 0x41], r15d
0050970E  E8 A1 01 00 00                  call 0x1405098b4
00509713  0F B7 F8                        movzx edi, ax
00509716  66 89 45 B7                     mov word ptr [rbp - 0x49], ax
0050971A  41 0F B7 06                     movzx eax, word ptr [r14]
0050971E  49 83 C6 02                     add r14, 2
00509722  89 7D CF                        mov dword ptr [rbp - 0x31], edi
00509725  49 8B CE                        mov rcx, r14
00509728  66 3B C7                        cmp ax, di
0050972B  75 68                           jne 0x140509795
0050972D  66 44 3B E7                     cmp r12w, di
00509731  75 11                           jne 0x140509744
00509733  66 45 39 2E                     cmp word ptr [r14], r13w
00509737  75 71                           jne 0x1405097aa
00509739  B8 6E 00 00 00                  mov eax, 0x6e
0050973E  66 39 41 02                     cmp word ptr [rcx + 2], ax
00509742  75 66                           jne 0x1405097aa
00509744  41 0F B7 06                     movzx eax, word ptr [r14]
00509748  66 85 C0                        test ax, ax
0050974B  0F 85 9F F7 FF FF               jne 0x140508ef0
00509751  EB 57                           jmp 0x1405097aa
00509753  B9 FF FF 00 00                  mov ecx, 0xffff
00509758  66 3B CF                        cmp cx, di
0050975B  74 4D                           je 0x1405097aa
0050975D  48 8B 55 67                     mov rdx, qword ptr [rbp + 0x67]
00509761  EB 3F                           jmp 0x1405097a2
00509763  8B 4D CB                        mov ecx, dword ptr [rbp - 0x35]
00509766  44 8B C3                        mov r8d, ebx
00509769  45 84 E4                        test r12b, r12b
0050976C  7E 05                           jle 0x140509773
0050976E  66 89 1A                        mov word ptr [rdx], bx
00509771  EB 3D                           jmp 0x1405097b0
00509773  88 1A                           mov byte ptr [rdx], bl
00509775  EB 39                           jmp 0x1405097b0
00509777  B9 FF FF 00 00                  mov ecx, 0xffff
0050977C  66 3B CF                        cmp cx, di
0050977F  74 0C                           je 0x14050978d
00509781  48 8B 55 67                     mov rdx, qword ptr [rbp + 0x67]
00509785  0F B7 CF                        movzx ecx, di
00509788  E8 73 01 00 00                  call 0x140509900
0050978D  41 B8 01 00 00 00               mov r8d, 1
00509793  EB 18                           jmp 0x1405097ad
00509795  B9 FF FF 00 00                  mov ecx, 0xffff
0050979A  66 3B CF                        cmp cx, di
0050979D  74 0B                           je 0x1405097aa
0050979F  48 8B D6                        mov rdx, rsi
005097A2  0F B7 CF                        movzx ecx, di
005097A5  E8 56 01 00 00                  call 0x140509900
005097AA  44 8B C3                        mov r8d, ebx
005097AD  8B 4D CB                        mov ecx, dword ptr [rbp - 0x35]
005097B0  8A 55 7F                        mov dl, byte ptr [rbp + 0x7f]
005097B3  B8 FF FF 00 00                  mov eax, 0xffff
005097B8  66 3B C7                        cmp ax, di
005097BB  74 22                           je 0x1405097df
005097BD  41 83 F8 01                     cmp r8d, 1
005097C1  75 2D                           jne 0x1405097f0
005097C3  45 33 C9                        xor r9d, r9d
005097C6  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
005097CB  45 33 C0                        xor r8d, r8d
005097CE  33 D2                           xor edx, edx
005097D0  33 C9                           xor ecx, ecx
005097D2  E8 79 4D F9 FF                  call 0x14049e550
005097D7  8B 45 CB                        mov eax, dword ptr [rbp - 0x35]
005097DA  EB 2C                           jmp 0x140509808
005097DC  8A 55 7F                        mov dl, byte ptr [rbp + 0x7f]
005097DF  8B 45 CB                        mov eax, dword ptr [rbp - 0x35]
005097E2  85 C0                           test eax, eax
005097E4  75 04                           jne 0x1405097ea
005097E6  84 D2                           test dl, dl
005097E8  74 02                           je 0x1405097ec
005097EA  8B D8                           mov ebx, eax
005097EC  8B C3                           mov eax, ebx
005097EE  EB 18                           jmp 0x140509808
005097F0  8B C1                           mov eax, ecx
005097F2  EB 14                           jmp 0x140509808
005097F4  45 33 C9                        xor r9d, r9d
005097F7  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
005097FC  33 D2                           xor edx, edx
005097FE  33 C9                           xor ecx, ecx
00509800  E8 4B 4D F9 FF                  call 0x14049e550
00509805  83 C8 FF                        or eax, 0xffffffff
00509808  48 81 C4 B8 00 00 00            add rsp, 0xb8
0050980F  41 5F                           pop r15
00509811  41 5E                           pop r14
00509813  41 5D                           pop r13
00509815  41 5C                           pop r12
00509817  5F                              pop rdi
00509818  5E                              pop rsi
00509819  5B                              pop rbx
0050981A  5D                              pop rbp
0050981B  C3                              ret
0050981C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall winput_s(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned int v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned __int8 v_stack_m9B;
    unsigned __int8 v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned __int8 v_stack_mA4;
    unsigned __int16 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (184);
    v_rbx = 0;
    v_stack_m78 = 0;
    v_stack_m90 = 0;
    v_stack_mA8 = 0;
    v_stack_m68 = 0;
    if (a2 == 0) goto loc_005097F4;
    if (a1 == 0) goto loc_005097F4;
    v_stack_p20 = 0;
    v_stack_mA0 = 0;
    v_stack_m94 = 0;
    if ((unsigned __int16)(*(unsigned __int16 *)(a2)) == 0) goto loc_005097B3;
loc_00508EF0:
    result = iswctype((unsigned __int16)(*(unsigned __int16 *)(a2)), 8, 0, a4);
    if ((unsigned int)(result) == 0) goto loc_00508F4E;
    v_r15 = (unsigned int)((0) - 1);
    v_stack_mA0 = (unsigned int)(v_r15);
    result = _whiteout(v_stack_mA0, a1, 0, a4);
    if (((unsigned __int16)((unsigned int)(0xFFFFULL))) != ((unsigned __int16)(result))) {
        a2 = a1;
        a1 = (unsigned __int16)(result);
        result = ungetwc_nolock(a1, a2, 0, a4);
    }
    v_r14 = (a2) + (2);
    result = iswctype(*(unsigned __int16 *)(v_r14), 8, 0, a4);
    if ((unsigned int)(result) != 0) goto loc_00508F29;
    goto loc_00509744;
loc_00508F4E:
    if (((unsigned __int16)(v_rbx + 37)) != (*(unsigned __int16 *)(v_r14))) goto loc_00509704;
    if (((unsigned __int16)(v_rbx + 37)) == (*(unsigned __int16 *)(v_r14 + 2))) goto loc_00509700;
    v_stack_m88 = 0;
    v_stack_m70 = 0;
    v_stack_m98 = 0;
    v_stack_m9C = 0;
loc_00508F92:
    v_r14 = (v_r14) + (2);
    v_stack_p10 = v_r14;
    if ((((unsigned __int16)((unsigned int)(0xFF00ULL))) & ((unsigned __int16)(*(unsigned __int16 *)(v_r14)))) != 0) goto loc_00508FCA;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9400405) + (unsigned __int8)(*(unsigned __int16 *)(v_r14)) * 2)) & (4)) == 0) goto loc_00508FCA;
    a1 = (unsigned int)(((unsigned int)(v_stack_m98)) + 1);
    v_stack_m98 = (unsigned int)(a1);
    goto loc_00509027;
loc_00508FCA:
    if (((unsigned int)(*(unsigned __int16 *)(v_r14))) > 104) goto loc_00509099;
    if (((unsigned int)(*(unsigned __int16 *)(v_r14))) == 104) goto loc_00509091;
    if (((unsigned int)(*(unsigned __int16 *)(v_r14))) == 42) goto loc_0050908C;
    if (((unsigned int)(*(unsigned __int16 *)(v_r14))) == 70) goto loc_00509027;
    if (((unsigned int)(*(unsigned __int16 *)(v_r14))) == 73) goto loc_00509000;
    if (((unsigned int)(*(unsigned __int16 *)(v_r14))) == 76) goto loc_00508FFB;
    if (((unsigned int)(*(unsigned __int16 *)(v_r14))) == 78) goto loc_00509027;
    goto loc_005090DB;
loc_00508FFB:
    v_rsi = (unsigned __int8)((1) + 1);
    goto loc_00509027;
loc_00509000:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r14 + 2))) != 54) goto loc_00509073;
    if ((*(unsigned __int16 *)(v_r14 + 4)) != 52) goto loc_005090B1;
loc_00509019:
    v_stack_p10 = v_r14 + 4;
loc_00509020:
    v_stack_m78 = 0;
    v_r11 = (unsigned int)((0) + 1);
loc_00509027:
    if (0 == 0) goto loc_00508F92;
    v_stack_m9B = 0;
    v_stack_mA4 = (unsigned __int8)(v_rsi);
    v_stack_m80 = (unsigned int)(v_r11);
    v_stack_m8C = (unsigned int)(*(unsigned __int16 *)(v_r14) + 0 + 0 * 4 - 24 * 2);
    if (0 != 0) goto loc_005090FB;
    v_stack_m68 = v_stack_p18;
    result = (v_stack_p18) + (8);
    v_stack_p18 = result;
    v_stack_m60 = *(unsigned __int64 *)(result - 8);
    goto loc_00509102;
loc_00509073:
    if (((unsigned __int16)(result)) != 51) goto loc_005090B1;
    if ((*(unsigned __int16 *)(v_r14 + 4 + 4)) != 50) goto loc_005090B1;
    v_stack_p10 = v_r14 + 4 + 4;
    goto loc_00509027;
loc_0050908C:
    v_r13 = (unsigned __int8)((0) + 1);
    goto loc_00509027;
loc_00509091:
    v_rsi = (unsigned __int8)((v_rsi) - 1);
    v_r12 = (unsigned __int8)((0) - 1);
    goto loc_00509027;
loc_00509099:
    if (((unsigned int)(*(unsigned __int64 *)(result - 8))) == 106) goto loc_00509020;
    if (((unsigned int)(*(unsigned __int64 *)(result - 8))) == ((unsigned int)((unsigned int)(v_stack_m90)))) goto loc_005090E3;
    if (((unsigned int)(*(unsigned __int64 *)(result - 8))) == 116) goto loc_005090B1;
    if (((unsigned int)(*(unsigned __int64 *)(result - 8))) == 119) goto loc_005090F3;
    if (((unsigned int)(*(unsigned __int64 *)(result - 8))) != 122) goto loc_005090DB;
loc_005090B1:
    result = (unsigned __int16)((*(unsigned __int16 *)(v_r14 + 4 + 4 + 2)) - (88));
    if (((unsigned __int16)(result)) > ((unsigned __int16)((unsigned int)(v_stack_mA0)))) goto loc_005090D4;
    if (((unsigned __int16)(result)) < ((unsigned __int16)((unsigned int)(v_stack_mA0)))) goto loc_00509020;
loc_005090D4:
    v_r11 = (unsigned int)((v_r11) + 1);
    v_stack_m78 = 0;
loc_005090DB:
    a3 = (unsigned __int8)((0) + 1);
    goto loc_00509027;
loc_005090E3:
    if ((*(unsigned __int16 *)(v_r14 + 4 + 4 + 2)) == ((unsigned __int16)((unsigned int)(v_stack_m90)))) goto loc_00509019;
    v_rsi = (unsigned __int8)((v_rsi) + 1);
loc_005090F3:
    v_r12 = (unsigned __int8)((v_r12) + 1);
    goto loc_00509027;
loc_005090FB:
    v_stack_m60 = 0;
loc_00509102:
    v_stack_m58 = 0;
    result = v_r14 + 4 + 4 + 2;
    if ((unsigned __int8)(v_r12) == 0) {
        result = *(unsigned __int16 *)(v_r14 + 4 + 4);
        v_rsi = 0xFFEFULL;
        result = (unsigned __int16)((result) - (67));
        result = (unsigned __int16)((result) & ((unsigned __int16)(v_rsi)));
        result = (unsigned __int16)(-(result));
        v_r12 = (unsigned __int8)((v_r12) & (2));
        v_r12 = (unsigned __int8)((v_r12) - 1);
    }
    v_rsi = (unsigned int)((*(unsigned __int16 *)(v_r14 + 4 + 4)) | (32));
    if (((unsigned int)(v_rsi)) == 110) goto loc_00509196;
    if (((unsigned int)(v_rsi)) == 99) goto loc_00509158;
    if (((unsigned int)(v_rsi)) == 123) goto loc_00509158;
    result = _whiteout(v_stack_mA0, v_stack_p8, a3, 0);
    goto loc_00509168;
loc_00509158:
    v_r15 = (unsigned int)(((unsigned int)(v_stack_mA0)) + 1);
    v_stack_mA0 = (unsigned int)(v_r15);
    result = fgetwc_nolock(v_stack_p8, v_stack_p8, a3, 0);
loc_00509168:
    v_stack_mA8 = (unsigned __int16)(result);
    v_stack_m90 = (unsigned int)((unsigned __int16)(result));
    if (((unsigned __int16)((unsigned int)(0xFFFFULL))) == ((unsigned __int16)((unsigned __int16)(result)))) goto loc_005097DC;
loc_00509196:
    if ((unsigned int)((unsigned int)(v_stack_m98)) == 0) goto loc_005091A3;
    if ((unsigned int)((unsigned int)(v_stack_m8C)) == 0) goto loc_00509753;
loc_005091A3:
    if ((unsigned __int8)(v_stack_m9B) != 0) goto loc_005091E4;
    if (((unsigned int)(v_rsi)) == 99) goto loc_005091B7;
    if (((unsigned int)(v_rsi)) == 115) goto loc_005091B7;
    if (((unsigned int)(v_rsi)) != 123) goto loc_005091E4;
loc_005091B7:
    v_stack_m68 = v_stack_m68 + 8;
    a4 = (v_stack_m68 + 8) + (8);
    v_stack_p18 = a4;
    v_stack_m60 = *(unsigned __int64 *)(v_stack_m68);
    v_stack_m58 = *(unsigned __int64 *)(v_stack_m68);
    if (((unsigned int)(*(unsigned int *)(v_stack_m68 + 8))) < 1) goto loc_00509763;
loc_005091E4:
    if (((unsigned int)(v_rsi)) > 112) goto loc_0050927D;
    if (((unsigned int)(v_rsi)) == 112) goto loc_0050926C;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) - (99));
    if (condition_is_equal) goto loc_00509251;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0050920E;
    a1 = (unsigned int)((a1) - (5));
    if (condition_is_equal) goto loc_00509239;
    a1 = (unsigned int)((a1) - (5));
    if (condition_is_equal) goto loc_00509228;
    if (((unsigned int)(a1)) != 1) goto loc_00509295;
loc_0050920E:
loc_00509211:
    if (45 != ((unsigned __int16)((unsigned __int16)(result)))) goto loc_005093BD;
    v_stack_m9C = 1;
    goto loc_005093C7;
loc_00509228:
    if ((unsigned __int8)(v_stack_m9B) == 0) goto loc_0050963A;
    goto loc_005096E4;
loc_00509239:
loc_00509241:
    if (45 != ((unsigned __int16)((unsigned __int16)(result)))) goto loc_005092C2;
    v_stack_m9C = 1;
    goto loc_005092CC;
loc_00509251:
    if ((unsigned int)((unsigned int)(v_stack_m98)) != 0) goto loc_00509667;
    v_r10 = (unsigned int)(((unsigned int)(v_stack_m8C)) + 1);
    goto loc_00509667;
loc_0050926C:
    v_r11 = (unsigned int)(((unsigned int)(v_stack_m80)) + 1);
    v_stack_mA4 = 1;
    v_stack_m80 = (unsigned int)(v_r11);
    v_stack_m78 = 0;
    goto loc_00509211;
loc_0050927D:
    if (100 == 115) goto loc_0050965F;
    if (100 == 117) goto loc_00509211;
    if (100 == 120) goto loc_00509241;
    if (100 == 123) goto loc_005092B8;
loc_00509295:
    if ((*(unsigned __int16 *)(v_r14 + 4 + 4)) != ((unsigned __int16)((unsigned __int16)(result)))) goto loc_00509777;
    if ((unsigned __int8)(v_stack_m9B) != 0) goto loc_005096E4;
    v_stack_p18 = v_stack_m68;
    goto loc_005096E4;
loc_005092B8:
    goto loc_00509664;
loc_005092C2:
    if (43 != ((unsigned __int16)((unsigned __int16)(result)))) goto loc_005092DD;
loc_005092CC:
    v_r10 = (unsigned int)((v_r10) - (1));
    v_stack_m8C = (unsigned int)(v_r10);
    if (condition_is_not_equal) goto loc_00509341;
    if (64 == 0) goto loc_00509341;
loc_005092DD:
loc_005092E1:
    if (48 != ((unsigned __int16)((unsigned __int16)(result)))) goto loc_005093F7;
    v_r15 = (unsigned int)((v_r15) + 1);
    v_stack_mA0 = (unsigned int)(v_r15);
    result = fgetwc_nolock(v_stack_p8, 16 - 15, v_stack_m68, (unsigned int)(*(unsigned int *)(v_stack_m68 + 8)));
    v_stack_mA8 = (unsigned __int16)(result);
    v_stack_m90 = (unsigned int)((unsigned __int16)(result));
    if ((((unsigned __int16)((unsigned int)(0xFFDFULL))) & ((unsigned __int16)((unsigned __int16)(result) - 88))) == 0) goto loc_00509383;
    v_stack_m70 = 1;
    if (100 == 120) goto loc_00509360;
    if ((unsigned int)((unsigned int)(v_stack_m98)) == 0) goto loc_00509337;
    v_r12 = (unsigned int)(((unsigned int)(v_stack_m8C)) - (1));
    v_r13 = 1;
    if (!(condition_is_not_equal)) {
        v_r13 = (unsigned __int8)((1) + 1);
    }
    goto loc_005093FF;
loc_00509341:
    v_r15 = (unsigned int)((v_r15) + 1);
    v_stack_mA0 = (unsigned int)(v_r15);
    result = fgetwc_nolock(v_stack_p8, 16 - 15, (unsigned int)(v_stack_m98), (unsigned int)(*(unsigned int *)(v_stack_m68 + 8)));
    v_stack_mA8 = (unsigned __int16)(result);
    v_stack_m90 = (unsigned int)((unsigned __int16)(result));
    goto loc_005092E1;
loc_00509360:
    v_r15 = (unsigned int)((v_r15) - 1);
    v_stack_mA0 = (unsigned int)(v_r15);
    result = (unsigned int)(0xFFFFULL);
    if (((unsigned __int16)((unsigned int)(0xFFFFULL))) != ((unsigned __int16)((unsigned __int16)(result)))) {
        a2 = v_stack_p8;
        a1 = (unsigned __int16)((unsigned __int16)(result));
        result = ungetwc_nolock(a1, a2, (unsigned int)(v_stack_m98), (unsigned int)(*(unsigned int *)(v_stack_m68 + 8)));
    }
    goto loc_005093F0;
loc_00509383:
    v_r15 = (unsigned int)((v_r15) + 1);
    v_stack_mA0 = (unsigned int)(v_r15);
    result = fgetwc_nolock(v_stack_p8, a2, (unsigned int)(v_stack_m98), (unsigned int)(*(unsigned int *)(v_stack_m68 + 8)));
    v_stack_m90 = (unsigned int)((unsigned __int16)(result));
    v_stack_mA8 = (unsigned __int16)(result);
    if ((unsigned int)((unsigned int)(v_stack_m98)) == 0) goto loc_005093B6;
    v_r12 = (unsigned int)(((unsigned int)(v_stack_m8C)) - (2));
    if (((unsigned int)(v_r12)) < 1) {
        v_r13 = (unsigned __int8)((v_r13) + 1);
    }
    goto loc_005093FF;
loc_005093BD:
    if (43 != ((unsigned __int16)((unsigned __int16)(result)))) goto loc_005093F7;
loc_005093C7:
    v_r10 = (unsigned int)((v_r10) - (1));
    v_stack_m8C = (unsigned int)(v_r10);
    if (condition_is_not_equal) goto loc_005093DD;
    if ((unsigned int)(v_stack_p8) == 0) goto loc_005093DD;
    goto loc_005093FB;
loc_005093DD:
    v_r15 = (unsigned int)((v_r15) + 1);
    v_stack_mA0 = (unsigned int)(v_r15);
    result = fgetwc_nolock(v_stack_p8, a2, (unsigned int)(v_stack_m98), (unsigned int)(*(unsigned int *)(v_stack_m68 + 8)));
loc_005093F0:
    v_stack_mA8 = (unsigned __int16)((unsigned __int16)(result));
    v_stack_m90 = (unsigned int)((unsigned __int16)(result));
loc_005093F7:
loc_005093FB:
loc_005093FF:
    if (v_stack_m80 == 0) goto loc_0050951F;
    if (1 != 0) goto loc_00509505;
loc_00509411:
    if ((((unsigned int)(120 - 112)) & (0xFFFFFFF7ULL)) == 0) goto loc_00509468;
    if ((((unsigned __int16)((unsigned int)(0xFF00ULL))) & ((unsigned __int16)((unsigned __int16)(result)))) != 0) goto loc_005094E8;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9399248) + (unsigned __int8)((unsigned __int16)(result)) * 2)) & (4)) == 0) goto loc_005094E8;
    if (120 != 111) goto loc_0050945A;
    if (((unsigned __int16)(120 - 55)) <= ((unsigned __int16)((unsigned __int16)(result)))) goto loc_00509455;
    a1 = (v_stack_m78) << (3);
    goto loc_00509462;
loc_00509455:
    goto loc_005094A4;
loc_0050945A:
loc_00509462:
    v_stack_m78 = a1 + a1 * 4 + a1 + a1 * 4 * 1;
    goto loc_005094A4;
loc_00509468:
    if ((((unsigned __int16)(a1 + a1 * 4)) & ((unsigned __int16)((unsigned __int16)(result)))) != 0) goto loc_005094E8;
    if (!sign_flag) goto loc_005094E8;
    a1 = (v_stack_m78) << (4);
    v_stack_m78 = a1;
    result = *(unsigned __int64 *)(v_rip + 9399180);
    v_rdi = (unsigned __int16)(result);
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 9399180) + (unsigned __int8)((unsigned __int16)(result)) * 2))) & (4)) == 0) {
        result = 0xFFDFULL;
        v_rdi = (unsigned __int16)(((unsigned __int16)(result)) & ((unsigned __int16)(result)));
        v_rdi = (unsigned __int16)((v_rdi) - (7));
        v_stack_m90 = (unsigned int)(v_rdi);
        v_stack_mA8 = (unsigned __int16)(v_rdi);
    }
    if (1 != 0) goto loc_005094E8;
    a1 = (a1) + (-48);
    a1 = (a1) + ((unsigned __int16)(v_rdi));
    v_stack_m78 = a1;
    if ((unsigned int)((unsigned int)(v_stack_m98)) == 0) goto loc_005094C5;
    v_r12 = (unsigned int)(((unsigned int)(v_stack_m8C)) - (1));
    if (condition_is_equal) goto loc_00509509;
loc_005094C5:
    v_r15 = (unsigned int)((v_r15) + 1);
    v_stack_mA0 = (unsigned int)(v_r15);
    result = fgetwc_nolock(v_stack_p8, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 9399180) + (unsigned __int8)((unsigned __int16)(result)) * 2), (unsigned int)(v_stack_m98), (unsigned int)(*(unsigned int *)(v_stack_m68 + 8)));
    v_stack_m90 = (unsigned int)((unsigned __int16)(result));
    v_stack_mA8 = (unsigned __int16)(result);
    goto loc_00509411;
loc_005094E8:
    v_r15 = (unsigned int)((v_r15) - 1);
    v_stack_mA0 = (unsigned int)(v_r15);
    result = (unsigned int)(0xFFFFULL);
    if (((unsigned __int16)((unsigned int)(0xFFFFULL))) != ((unsigned __int16)((unsigned __int16)(result)))) {
        a2 = v_stack_p8;
        a1 = (unsigned __int16)((unsigned __int16)(result));
        result = ungetwc_nolock(a1, a2, (unsigned int)(v_stack_m98), (unsigned int)(*(unsigned int *)(v_stack_m68 + 8)));
    }
loc_00509509:
    result = -(v_stack_m78);
    if (v_stack_m9C == 0) { result = v_stack_m78; }
    v_stack_m78 = result;
    goto loc_0050961E;
loc_0050951F:
    if (1 != 0) goto loc_00509611;
loc_00509528:
    if ((((unsigned int)(120 - 112)) & (0xFFFFFFF7ULL)) == 0) goto loc_0050957A;
    if ((((unsigned __int16)((unsigned int)(0xFF00ULL))) & ((unsigned __int16)((unsigned __int16)(result)))) != 0) goto loc_005095F4;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9398969) + (unsigned __int8)((unsigned __int16)(result)) * 2)) & (4)) == 0) goto loc_005095F4;
    if (120 != 111) goto loc_0050956F;
    if (((unsigned __int16)(120 - 55)) <= ((unsigned __int16)((unsigned __int16)(result)))) goto loc_0050956A;
    a1 = (unsigned int)(((unsigned int)(v_stack_m88)) << (3));
    goto loc_00509575;
loc_0050956A:
    goto loc_005095B3;
loc_0050956F:
loc_00509575:
    v_stack_m88 = (unsigned int)(a1 + a1 * 4 + a1 + a1 * 4 * 1);
    goto loc_005095B3;
loc_0050957A:
    if ((((unsigned __int16)(a1 + a1 * 4)) & ((unsigned __int16)((unsigned __int16)(result)))) != 0) goto loc_005095F4;
    if (!sign_flag) goto loc_005095F4;
    a1 = (unsigned int)(((unsigned int)(v_stack_m88)) << (4));
    v_stack_m88 = (unsigned int)(a1);
    result = *(unsigned __int64 *)(v_rip + 9398906);
    v_rdi = (unsigned __int16)(result);
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 9398906) + (unsigned __int8)((unsigned __int16)(result)) * 2))) & (4)) == 0) {
        result = 0xFFDFULL;
        v_rdi = (unsigned __int16)(((unsigned __int16)(result)) & ((unsigned __int16)(result)));
        v_rdi = (unsigned __int16)((v_rdi) - (7));
        v_stack_m90 = (unsigned int)(v_rdi);
        v_stack_mA8 = (unsigned __int16)(v_rdi);
    }
    if (1 != 0) goto loc_005095F4;
    a1 = (unsigned int)((a1) + (-48));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned __int16)(v_rdi))));
    v_stack_m88 = (unsigned int)(a1);
    if ((unsigned int)((unsigned int)(v_stack_m98)) == 0) goto loc_005095D1;
    v_r12 = (unsigned int)((v_r12) - (1));
    if (condition_is_equal) goto loc_00509614;
loc_005095D1:
    v_r15 = (unsigned int)((v_r15) + 1);
    v_stack_mA0 = (unsigned int)(v_r15);
    result = fgetwc_nolock(v_stack_p8, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 9398906) + (unsigned __int8)((unsigned __int16)(result)) * 2), (unsigned int)(v_stack_m98), (unsigned int)(*(unsigned int *)(v_stack_m68 + 8)));
    v_stack_m90 = (unsigned int)((unsigned __int16)(result));
    v_stack_mA8 = (unsigned __int16)(result);
    goto loc_00509528;
loc_005095F4:
    v_r15 = (unsigned int)((v_r15) - 1);
    v_stack_mA0 = (unsigned int)(v_r15);
    result = (unsigned int)(0xFFFFULL);
    if (((unsigned __int16)((unsigned int)(0xFFFFULL))) != ((unsigned __int16)((unsigned __int16)(result)))) {
        a2 = v_stack_p8;
        a1 = (unsigned __int16)((unsigned __int16)(result));
        result = ungetwc_nolock(a1, a2, (unsigned int)(v_stack_m98), (unsigned int)(*(unsigned int *)(v_stack_m68 + 8)));
    }
loc_00509614:
    if (v_stack_m9C != 0) {
        a1 = (unsigned int)(-((unsigned int)(v_stack_m88)));
        v_stack_m88 = (unsigned int)(a1);
    }
    if (v_stack_m70 == 0) goto loc_005097AA;
    if (v_stack_m9B != 0) goto loc_005096E4;
loc_0050963A:
    if (v_stack_m80 == 0) goto loc_0050964B;
    *(unsigned __int64 *)(v_stack_m60) = v_stack_m78;
    goto loc_005096E4;
loc_0050964B:
    if (v_stack_mA4 == 0) goto loc_00509657;
    *(unsigned int *)(v_stack_m60) = (unsigned int)(v_stack_m78);
    goto loc_005096E4;
loc_00509657:
    *(unsigned __int16 *)(v_stack_m60) = (unsigned __int16)(v_stack_m78);
    goto loc_005096E4;
loc_0050965F:
loc_00509664:
loc_00509667:
    result = (unsigned int)((32) | (1));
    if ((unsigned int)((unsigned int)(v_stack_m98)) == 0) { result = 32; }
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) | (2));
    if (condition_is_less_or_equal) { a1 = (unsigned int)(result); }
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (4));
    if ((unsigned __int8)((unsigned int)(v_stack_m98)) == 0) { result = (unsigned int)(a1); }
    v_stack_mB8 = v_stack_m94;
    v_stack_mC0 = (unsigned int)(*(unsigned int *)(v_stack_m68 + 8));
    v_stack_mC8 = v_stack_p8;
    v_stack_mD0 = (unsigned int)(v_r10);
    v_stack_mD8 = v_stack_m58;
    if (120 != 123) goto loc_005096CA;
    result = ReadStringDelimited((unsigned int)((unsigned int)(result)), v_stack_p10, v_stack_mA8, v_stack_mA0);
    goto loc_005096D1;
loc_005096CA:
    a2 = 0;
    result = ReadString((unsigned int)((unsigned int)(result)), a2, v_stack_mA8, v_stack_mA0);
loc_005096D1:
    if ((unsigned int)(result) != 0) goto loc_005097AA;
    v_stack_m90 = (unsigned int)(v_stack_mA8);
loc_005096E4:
    v_r14 = (v_stack_p10) + (2);
    goto loc_0050972D;
loc_00509700:
    v_r14 = (v_r14) + (2);
loc_00509704:
    v_r15 = (unsigned int)(((unsigned int)(v_stack_mA0)) + 1);
    v_stack_mA0 = (unsigned int)(v_r15);
    result = fgetwc_nolock(v_stack_p8, a2, v_stack_mA8, v_stack_mA0);
    v_stack_mA8 = (unsigned __int16)(result);
    v_r14 = (v_r14) + (2);
    v_stack_m90 = (unsigned int)((unsigned __int16)(result));
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r14))) != ((unsigned __int16)((unsigned __int16)(result)))) goto loc_00509795;
loc_0050972D:
    if (((unsigned __int16)((unsigned int)(0xFFFFULL))) != ((unsigned __int16)((unsigned __int16)(result)))) goto loc_00509744;
    if ((*(unsigned __int16 *)(v_r14)) != 37) goto loc_005097AA;
    if ((*(unsigned __int16 *)(v_r14 + 2)) != 110) goto loc_005097AA;
loc_00509744:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_r14)) != 0) goto loc_00508EF0;
    goto loc_005097AA;
loc_00509753:
    if (((unsigned __int16)((unsigned int)(0xFFFFULL))) == ((unsigned __int16)((unsigned __int16)(result)))) goto loc_005097AA;
    goto loc_005097A2;
loc_00509763:
    if (condition_is_less_or_equal) goto loc_00509773;
    *(unsigned __int16 *)(v_stack_p8) = 0;
    goto loc_005097B0;
loc_00509773:
    *(unsigned __int8 *)(v_stack_p8) = 0;
    goto loc_005097B0;
loc_00509777:
    result = *(unsigned __int16 *)(v_r14);
    if (((unsigned __int16)((unsigned int)(0xFFFFULL))) != ((unsigned __int16)((unsigned __int16)(result)))) {
        a2 = v_stack_p8;
        a1 = (unsigned __int16)((unsigned __int16)(result));
        result = ungetwc_nolock(a1, a2, 0, v_stack_mA0);
    }
    goto loc_005097AD;
loc_00509795:
    if (((unsigned __int16)((unsigned int)(0xFFFFULL))) == ((unsigned __int16)((unsigned __int16)(result)))) goto loc_005097AA;
loc_005097A2:
    result = ungetwc_nolock((unsigned __int16)((unsigned __int16)(result)), v_stack_p8, 1, v_stack_mA0);
loc_005097AA:
loc_005097AD:
loc_005097B0:
loc_005097B3:
    if (((unsigned __int16)((unsigned int)(0xFFFFULL))) == ((unsigned __int16)((unsigned __int16)(result)))) goto loc_005097DF;
    if (0 != 1) goto loc_005097F0;
    a4 = 0;
    v_stack_mD8 = 0;
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = EmpCheckErrataList(a1, a2, a3, a4);
    goto loc_00509808;
loc_005097DC:
loc_005097DF:
    if ((unsigned int)((unsigned int)(v_stack_m94)) != 0) goto loc_005097EA;
    if ((unsigned __int8)(v_stack_p20) != 0) {
        v_rbx = (unsigned int)((unsigned int)(v_stack_m94));
    }
    goto loc_00509808;
loc_005097F0:
    goto loc_00509808;
loc_005097F4:
    a4 = 0;
    v_stack_mD8 = v_rbx;
    a2 = 0;
    a1 = 0;
    result = EmpCheckErrataList(a1, a2, a3, a4);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
loc_00509808:
    v_rsp = (v_rsp) + (184);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t winput_s(int64_t Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint32_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint8_t v_stack_m9B;
    uint8_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint8_t v_stack_mA4;
    uint16_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (184);
    local_rbx = 0;
    v_stack_m78 = 0;
    v_stack_m90 = 0;
    v_stack_mA8 = 0;
    v_stack_m68 = 0;
    if (Arg2 == NULL) goto loc_005097F4;
    if (Arg1 == 0) goto loc_005097F4;
    v_stack_p20 = 0;
    v_stack_mA0 = 0;
    v_stack_m94 = 0;
    if ((uint16_t)(*(uint16_t *)(arg2)) == 0) goto loc_005097B3;
loc_00508EF0:
    result = iswctype((uint16_t)(*(uint16_t *)(arg2)), 8, 0, a4);
    if ((uint32_t)(result) == 0) goto loc_00508F4E;
    local_r15 = (uint32_t)((0) - 1);
    v_stack_mA0 = (uint32_t)(local_r15);
    result = _whiteout(v_stack_mA0, Arg1, 0, a4);
    if (((uint16_t)((uint32_t)(0xFFFFULL))) != ((uint16_t)(result))) {
        Arg2 = Arg1;
        Arg1 = (uint16_t)(result);
        result = ungetwc_nolock(Arg1, Arg2, 0, a4);
    }
    local_r14 = (Arg2) + (2);
    result = iswctype(*(uint16_t *)(local_r14), 8, 0, a4);
    if ((uint32_t)(result) != 0) goto loc_00508F29;
    goto loc_00509744;
loc_00508F4E:
    if (((uint16_t)(local_rbx + 37)) != (*(uint16_t *)(local_r14))) goto loc_00509704;
    if (((uint16_t)(local_rbx + 37)) == (*(uint16_t *)(local_r14 + 0x2))) goto loc_00509700;
    v_stack_m88 = 0;
    v_stack_m70 = 0;
    v_stack_m98 = 0;
    v_stack_m9C = 0;
loc_00508F92:
    local_r14 = (local_r14) + (2);
    v_stack_p10 = local_r14;
    if ((((uint16_t)((uint32_t)(0xFF00ULL))) & ((uint16_t)(*(uint16_t *)(local_r14)))) != 0) goto loc_00508FCA;
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0x8F7055) + (uint8_t)(*(uint16_t *)(local_r14)) * 2)) & (4)) == 0) goto loc_00508FCA;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m98)) + 1);
    v_stack_m98 = (uint32_t)(Arg1);
    goto loc_00509027;
loc_00508FCA:
    if (((uint32_t)(*(uint16_t *)(local_r14))) > 104) goto loc_00509099;
    if (((uint32_t)(*(uint16_t *)(local_r14))) == 104) goto loc_00509091;
    if (((uint32_t)(*(uint16_t *)(local_r14))) == 42) goto loc_0050908C;
    if (((uint32_t)(*(uint16_t *)(local_r14))) == 70) goto loc_00509027;
    if (((uint32_t)(*(uint16_t *)(local_r14))) == 73) goto loc_00509000;
    if (((uint32_t)(*(uint16_t *)(local_r14))) == 76) goto loc_00508FFB;
    if (((uint32_t)(*(uint16_t *)(local_r14))) == 78) goto loc_00509027;
    goto loc_005090DB;
loc_00508FFB:
    local_rsi = (uint8_t)((1) + 1);
    goto loc_00509027;
loc_00509000:
    if (((uint16_t)(*(uint16_t *)(local_r14 + 0x2))) != 54) goto loc_00509073;
    if ((*(uint16_t *)(local_r14 + 0x4)) != 52) goto loc_005090B1;
loc_00509019:
    v_stack_p10 = local_r14 + 4;
loc_00509020:
    v_stack_m78 = 0;
    local_r11 = (uint32_t)((0) + 1);
loc_00509027:
    if (0 == 0) goto loc_00508F92;
    v_stack_m9B = 0;
    v_stack_mA4 = (uint8_t)(local_rsi);
    v_stack_m80 = (uint32_t)(local_r11);
    v_stack_m8C = (uint32_t)(*(uint16_t *)(local_r14) + 0 + 0 * 4 - 24 * 2);
    if (0 != 0) goto loc_005090FB;
    v_stack_m68 = v_stack_p18;
    result = (v_stack_p18) + (8);
    v_stack_p18 = result;
    v_stack_m60 = *(uint64_t *)(result - 0x8);
    goto loc_00509102;
loc_00509073:
    if (((uint16_t)(result)) != 51) goto loc_005090B1;
    if ((*(uint16_t *)(local_r14 + 0x4 + 0x4)) != 50) goto loc_005090B1;
    v_stack_p10 = local_r14 + 4 + 4;
    goto loc_00509027;
loc_0050908C:
    local_r13 = (uint8_t)((0) + 1);
    goto loc_00509027;
loc_00509091:
    local_rsi = (uint8_t)((local_rsi) - 1);
    local_r12 = (uint8_t)((0) - 1);
    goto loc_00509027;
loc_00509099:
    if (((uint32_t)(*(uint64_t *)(result - 0x8))) == 106) goto loc_00509020;
    if (((uint32_t)(*(uint64_t *)(result - 0x8))) == ((uint32_t)((uint32_t)(v_stack_m90)))) goto loc_005090E3;
    if (((uint32_t)(*(uint64_t *)(result - 0x8))) == 116) goto loc_005090B1;
    if (((uint32_t)(*(uint64_t *)(result - 0x8))) == 119) goto loc_005090F3;
    if (((uint32_t)(*(uint64_t *)(result - 0x8))) != 122) goto loc_005090DB;
loc_005090B1:
    result = (uint16_t)((*(uint16_t *)(local_r14 + 0x4 + 0x4 + 0x2)) - (88));
    if (((uint16_t)(result)) > ((uint16_t)((uint32_t)(v_stack_mA0)))) goto loc_005090D4;
    if (((uint16_t)(result)) < ((uint16_t)((uint32_t)(v_stack_mA0)))) goto loc_00509020;
loc_005090D4:
    local_r11 = (uint32_t)((local_r11) + 1);
    v_stack_m78 = 0;
loc_005090DB:
    Arg3 = (uint8_t)((0) + 1);
    goto loc_00509027;
loc_005090E3:
    if ((*(uint16_t *)(local_r14 + 0x4 + 0x4 + 0x2)) == ((uint16_t)((uint32_t)(v_stack_m90)))) goto loc_00509019;
    local_rsi = (uint8_t)((local_rsi) + 1);
loc_005090F3:
    local_r12 = (uint8_t)((local_r12) + 1);
    goto loc_00509027;
loc_005090FB:
    v_stack_m60 = 0;
loc_00509102:
    v_stack_m58 = 0;
    result = local_r14 + 4 + 4 + 2;
    if ((uint8_t)(local_r12) == 0) {
        result = *(uint16_t *)(local_r14 + 0x4 + 0x4);
        local_rsi = 0xFFEFULL;
        result = (uint16_t)((result) - (67));
        result = (uint16_t)((result) & ((uint16_t)(local_rsi)));
        result = (uint16_t)(-(result));
        local_r12 = (uint8_t)((local_r12) & (2));
        local_r12 = (uint8_t)((local_r12) - 1);
    }
    local_rsi = (uint32_t)((*(uint16_t *)(local_r14 + 0x4 + 0x4)) | (32));
    if (((uint32_t)(local_rsi)) == 110) goto loc_00509196;
    if (((uint32_t)(local_rsi)) == 99) goto loc_00509158;
    if (((uint32_t)(local_rsi)) == 123) goto loc_00509158;
    result = _whiteout(v_stack_mA0, v_stack_p8, Arg3, 0);
    goto loc_00509168;
loc_00509158:
    local_r15 = (uint32_t)(((uint32_t)(v_stack_mA0)) + 1);
    v_stack_mA0 = (uint32_t)(local_r15);
    result = fgetwc_nolock(v_stack_p8, v_stack_p8, Arg3, 0);
loc_00509168:
    v_stack_mA8 = (uint16_t)(result);
    v_stack_m90 = (uint32_t)((uint16_t)(result));
    if (((uint16_t)((uint32_t)(0xFFFFULL))) == ((uint16_t)((uint16_t)(result)))) goto loc_005097DC;
loc_00509196:
    if ((uint32_t)((uint32_t)(v_stack_m98)) == 0) goto loc_005091A3;
    if ((uint32_t)((uint32_t)(v_stack_m8C)) == 0) goto loc_00509753;
loc_005091A3:
    if ((uint8_t)(v_stack_m9B) != 0) goto loc_005091E4;
    if (((uint32_t)(local_rsi)) == 99) goto loc_005091B7;
    if (((uint32_t)(local_rsi)) == 115) goto loc_005091B7;
    if (((uint32_t)(local_rsi)) != 123) goto loc_005091E4;
loc_005091B7:
    v_stack_m68 = v_stack_m68 + 8;
    a4 = (v_stack_m68 + 8) + (8);
    v_stack_p18 = a4;
    v_stack_m60 = *(uint64_t *)(v_stack_m68);
    v_stack_m58 = *(uint64_t *)(v_stack_m68);
    if (((uint32_t)(*(uint32_t *)(v_stack_m68 + 0x8))) < 1) goto loc_00509763;
loc_005091E4:
    if (((uint32_t)(local_rsi)) > 112) goto loc_0050927D;
    if (((uint32_t)(local_rsi)) == 112) goto loc_0050926C;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) - (99));
    if (condition_is_equal) goto loc_00509251;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0050920E;
    Arg1 = (uint32_t)((Arg1) - (5));
    if (condition_is_equal) goto loc_00509239;
    Arg1 = (uint32_t)((Arg1) - (5));
    if (condition_is_equal) goto loc_00509228;
    if (((uint32_t)(Arg1)) != 1) goto loc_00509295;
loc_0050920E:
loc_00509211:
    if (45 != ((uint16_t)((uint16_t)(result)))) goto loc_005093BD;
    v_stack_m9C = 1;
    goto loc_005093C7;
loc_00509228:
    if ((uint8_t)(v_stack_m9B) == 0) goto loc_0050963A;
    goto loc_005096E4;
loc_00509239:
loc_00509241:
    if (45 != ((uint16_t)((uint16_t)(result)))) goto loc_005092C2;
    v_stack_m9C = 1;
    goto loc_005092CC;
loc_00509251:
    if ((uint32_t)((uint32_t)(v_stack_m98)) != 0) goto loc_00509667;
    local_r10 = (uint32_t)(((uint32_t)(v_stack_m8C)) + 1);
    goto loc_00509667;
loc_0050926C:
    local_r11 = (uint32_t)(((uint32_t)(v_stack_m80)) + 1);
    v_stack_mA4 = 1;
    v_stack_m80 = (uint32_t)(local_r11);
    v_stack_m78 = 0;
    goto loc_00509211;
loc_0050927D:
    if (100 == 115) goto loc_0050965F;
    if (100 == 117) goto loc_00509211;
    if (100 == 120) goto loc_00509241;
    if (100 == 123) goto loc_005092B8;
loc_00509295:
    if ((*(uint16_t *)(local_r14 + 0x4 + 0x4)) != ((uint16_t)((uint16_t)(result)))) goto loc_00509777;
    if ((uint8_t)(v_stack_m9B) != 0) goto loc_005096E4;
    v_stack_p18 = v_stack_m68;
    goto loc_005096E4;
loc_005092B8:
    goto loc_00509664;
loc_005092C2:
    if (43 != ((uint16_t)((uint16_t)(result)))) goto loc_005092DD;
loc_005092CC:
    local_r10 = (uint32_t)((local_r10) - (1));
    v_stack_m8C = (uint32_t)(local_r10);
    if (condition_is_not_equal) goto loc_00509341;
    if (64 == 0) goto loc_00509341;
loc_005092DD:
loc_005092E1:
    if (48 != ((uint16_t)((uint16_t)(result)))) goto loc_005093F7;
    local_r15 = (uint32_t)((local_r15) + 1);
    v_stack_mA0 = (uint32_t)(local_r15);
    result = fgetwc_nolock(v_stack_p8, 16 - 15, v_stack_m68, (uint32_t)(*(uint32_t *)(v_stack_m68 + 0x8)));
    v_stack_mA8 = (uint16_t)(result);
    v_stack_m90 = (uint32_t)((uint16_t)(result));
    if ((((uint16_t)((uint32_t)(0xFFDFULL))) & ((uint16_t)((uint16_t)(result) - 88))) == 0) goto loc_00509383;
    v_stack_m70 = 1;
    if (100 == 120) goto loc_00509360;
    if ((uint32_t)((uint32_t)(v_stack_m98)) == 0) goto loc_00509337;
    local_r12 = (uint32_t)(((uint32_t)(v_stack_m8C)) - (1));
    local_r13 = 1;
    if (!(condition_is_not_equal)) {
        local_r13 = (uint8_t)((1) + 1);
    }
    goto loc_005093FF;
loc_00509341:
    local_r15 = (uint32_t)((local_r15) + 1);
    v_stack_mA0 = (uint32_t)(local_r15);
    result = fgetwc_nolock(v_stack_p8, 16 - 15, (uint32_t)(v_stack_m98), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0x8)));
    v_stack_mA8 = (uint16_t)(result);
    v_stack_m90 = (uint32_t)((uint16_t)(result));
    goto loc_005092E1;
loc_00509360:
    local_r15 = (uint32_t)((local_r15) - 1);
    v_stack_mA0 = (uint32_t)(local_r15);
    result = (uint32_t)(0xFFFFULL);
    if (((uint16_t)((uint32_t)(0xFFFFULL))) != ((uint16_t)((uint16_t)(result)))) {
        Arg2 = v_stack_p8;
        Arg1 = (uint16_t)((uint16_t)(result));
        result = ungetwc_nolock(Arg1, Arg2, (uint32_t)(v_stack_m98), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0x8)));
    }
    goto loc_005093F0;
loc_00509383:
    local_r15 = (uint32_t)((local_r15) + 1);
    v_stack_mA0 = (uint32_t)(local_r15);
    result = fgetwc_nolock(v_stack_p8, Arg2, (uint32_t)(v_stack_m98), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0x8)));
    v_stack_m90 = (uint32_t)((uint16_t)(result));
    v_stack_mA8 = (uint16_t)(result);
    if ((uint32_t)((uint32_t)(v_stack_m98)) == 0) goto loc_005093B6;
    local_r12 = (uint32_t)(((uint32_t)(v_stack_m8C)) - (2));
    if (((uint32_t)(local_r12)) < 1) {
        local_r13 = (uint8_t)((local_r13) + 1);
    }
    goto loc_005093FF;
loc_005093BD:
    if (43 != ((uint16_t)((uint16_t)(result)))) goto loc_005093F7;
loc_005093C7:
    local_r10 = (uint32_t)((local_r10) - (1));
    v_stack_m8C = (uint32_t)(local_r10);
    if (condition_is_not_equal) goto loc_005093DD;
    if ((uint32_t)(v_stack_p8) == 0) goto loc_005093DD;
    goto loc_005093FB;
loc_005093DD:
    local_r15 = (uint32_t)((local_r15) + 1);
    v_stack_mA0 = (uint32_t)(local_r15);
    result = fgetwc_nolock(v_stack_p8, Arg2, (uint32_t)(v_stack_m98), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0x8)));
loc_005093F0:
    v_stack_mA8 = (uint16_t)((uint16_t)(result));
    v_stack_m90 = (uint32_t)((uint16_t)(result));
loc_005093F7:
loc_005093FB:
loc_005093FF:
    if (v_stack_m80 == 0) goto loc_0050951F;
    if (1 != 0) goto loc_00509505;
loc_00509411:
    if ((((uint32_t)(120 - 112)) & (0xFFFFFFF7ULL)) == 0) goto loc_00509468;
    if ((((uint16_t)((uint32_t)(0xFF00ULL))) & ((uint16_t)((uint16_t)(result)))) != 0) goto loc_005094E8;
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0x8F6BD0) + (uint8_t)((uint16_t)(result)) * 2)) & (4)) == 0) goto loc_005094E8;
    if (120 != 111) goto loc_0050945A;
    if (((uint16_t)(120 - 55)) <= ((uint16_t)((uint16_t)(result)))) goto loc_00509455;
    Arg1 = (v_stack_m78) << (3);
    goto loc_00509462;
loc_00509455:
    goto loc_005094A4;
loc_0050945A:
loc_00509462:
    v_stack_m78 = Arg1 + Arg1 * 4 + Arg1 + Arg1 * 4 * 1;
    goto loc_005094A4;
loc_00509468:
    if ((((uint16_t)(Arg1 + Arg1 * 4)) & ((uint16_t)((uint16_t)(result)))) != 0) goto loc_005094E8;
    if (!sign_flag) goto loc_005094E8;
    Arg1 = (v_stack_m78) << (4);
    v_stack_m78 = Arg1;
    result = *(uint64_t *)(v_rip + 0x8F6B8C);
    local_rdi = (uint16_t)(result);
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x8F6B8C) + (uint8_t)((uint16_t)(result)) * 2))) & (4)) == 0) {
        result = 0xFFDFULL;
        local_rdi = (uint16_t)(((uint16_t)(result)) & ((uint16_t)(result)));
        local_rdi = (uint16_t)((local_rdi) - (7));
        v_stack_m90 = (uint32_t)(local_rdi);
        v_stack_mA8 = (uint16_t)(local_rdi);
    }
    if (1 != 0) goto loc_005094E8;
    Arg1 = (Arg1) + (-48);
    Arg1 = (Arg1) + ((uint16_t)(local_rdi));
    v_stack_m78 = Arg1;
    if ((uint32_t)((uint32_t)(v_stack_m98)) == 0) goto loc_005094C5;
    local_r12 = (uint32_t)(((uint32_t)(v_stack_m8C)) - (1));
    if (condition_is_equal) goto loc_00509509;
loc_005094C5:
    local_r15 = (uint32_t)((local_r15) + 1);
    v_stack_mA0 = (uint32_t)(local_r15);
    result = fgetwc_nolock(v_stack_p8, *(uint16_t *)(*(uint64_t *)(v_rip + 0x8F6B8C) + (uint8_t)((uint16_t)(result)) * 2), (uint32_t)(v_stack_m98), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0x8)));
    v_stack_m90 = (uint32_t)((uint16_t)(result));
    v_stack_mA8 = (uint16_t)(result);
    goto loc_00509411;
loc_005094E8:
    local_r15 = (uint32_t)((local_r15) - 1);
    v_stack_mA0 = (uint32_t)(local_r15);
    result = (uint32_t)(0xFFFFULL);
    if (((uint16_t)((uint32_t)(0xFFFFULL))) != ((uint16_t)((uint16_t)(result)))) {
        Arg2 = v_stack_p8;
        Arg1 = (uint16_t)((uint16_t)(result));
        result = ungetwc_nolock(Arg1, Arg2, (uint32_t)(v_stack_m98), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0x8)));
    }
loc_00509509:
    result = -(v_stack_m78);
    if (v_stack_m9C == 0) { result = v_stack_m78; }
    v_stack_m78 = result;
    goto loc_0050961E;
loc_0050951F:
    if (1 != 0) goto loc_00509611;
loc_00509528:
    if ((((uint32_t)(120 - 112)) & (0xFFFFFFF7ULL)) == 0) goto loc_0050957A;
    if ((((uint16_t)((uint32_t)(0xFF00ULL))) & ((uint16_t)((uint16_t)(result)))) != 0) goto loc_005095F4;
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0x8F6AB9) + (uint8_t)((uint16_t)(result)) * 2)) & (4)) == 0) goto loc_005095F4;
    if (120 != 111) goto loc_0050956F;
    if (((uint16_t)(120 - 55)) <= ((uint16_t)((uint16_t)(result)))) goto loc_0050956A;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m88)) << (3));
    goto loc_00509575;
loc_0050956A:
    goto loc_005095B3;
loc_0050956F:
loc_00509575:
    v_stack_m88 = (uint32_t)(Arg1 + Arg1 * 4 + Arg1 + Arg1 * 4 * 1);
    goto loc_005095B3;
loc_0050957A:
    if ((((uint16_t)(Arg1 + Arg1 * 4)) & ((uint16_t)((uint16_t)(result)))) != 0) goto loc_005095F4;
    if (!sign_flag) goto loc_005095F4;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m88)) << (4));
    v_stack_m88 = (uint32_t)(Arg1);
    result = *(uint64_t *)(v_rip + 0x8F6A7A);
    local_rdi = (uint16_t)(result);
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x8F6A7A) + (uint8_t)((uint16_t)(result)) * 2))) & (4)) == 0) {
        result = 0xFFDFULL;
        local_rdi = (uint16_t)(((uint16_t)(result)) & ((uint16_t)(result)));
        local_rdi = (uint16_t)((local_rdi) - (7));
        v_stack_m90 = (uint32_t)(local_rdi);
        v_stack_mA8 = (uint16_t)(local_rdi);
    }
    if (1 != 0) goto loc_005095F4;
    Arg1 = (uint32_t)((Arg1) + (-48));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint16_t)(local_rdi))));
    v_stack_m88 = (uint32_t)(Arg1);
    if ((uint32_t)((uint32_t)(v_stack_m98)) == 0) goto loc_005095D1;
    local_r12 = (uint32_t)((local_r12) - (1));
    if (condition_is_equal) goto loc_00509614;
loc_005095D1:
    local_r15 = (uint32_t)((local_r15) + 1);
    v_stack_mA0 = (uint32_t)(local_r15);
    result = fgetwc_nolock(v_stack_p8, *(uint16_t *)(*(uint64_t *)(v_rip + 0x8F6A7A) + (uint8_t)((uint16_t)(result)) * 2), (uint32_t)(v_stack_m98), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0x8)));
    v_stack_m90 = (uint32_t)((uint16_t)(result));
    v_stack_mA8 = (uint16_t)(result);
    goto loc_00509528;
loc_005095F4:
    local_r15 = (uint32_t)((local_r15) - 1);
    v_stack_mA0 = (uint32_t)(local_r15);
    result = (uint32_t)(0xFFFFULL);
    if (((uint16_t)((uint32_t)(0xFFFFULL))) != ((uint16_t)((uint16_t)(result)))) {
        Arg2 = v_stack_p8;
        Arg1 = (uint16_t)((uint16_t)(result));
        result = ungetwc_nolock(Arg1, Arg2, (uint32_t)(v_stack_m98), (uint32_t)(*(uint32_t *)(v_stack_m68 + 0x8)));
    }
loc_00509614:
    if (v_stack_m9C != 0) {
        Arg1 = (uint32_t)(-((uint32_t)(v_stack_m88)));
        v_stack_m88 = (uint32_t)(Arg1);
    }
    if (v_stack_m70 == 0) goto loc_005097AA;
    if (v_stack_m9B != 0) goto loc_005096E4;
loc_0050963A:
    if (v_stack_m80 == 0) goto loc_0050964B;
    *(uint64_t *)(v_stack_m60) = v_stack_m78;
    goto loc_005096E4;
loc_0050964B:
    if (v_stack_mA4 == 0) goto loc_00509657;
    *(uint32_t *)(v_stack_m60) = (uint32_t)(v_stack_m78);
    goto loc_005096E4;
loc_00509657:
    *(uint16_t *)(v_stack_m60) = (uint16_t)(v_stack_m78);
    goto loc_005096E4;
loc_0050965F:
loc_00509664:
loc_00509667:
    result = (uint32_t)((32) | (1));
    if ((uint32_t)((uint32_t)(v_stack_m98)) == 0) { result = 32; }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) | (2));
    if (condition_is_less_or_equal) { Arg1 = (uint32_t)(result); }
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (4));
    if ((uint8_t)((uint32_t)(v_stack_m98)) == 0) { result = (uint32_t)(Arg1); }
    v_stack_mB8 = v_stack_m94;
    v_stack_mC0 = (uint32_t)(*(uint32_t *)(v_stack_m68 + 0x8));
    v_stack_mC8 = v_stack_p8;
    v_stack_mD0 = (uint32_t)(local_r10);
    v_stack_mD8 = v_stack_m58;
    if (120 != 123) goto loc_005096CA;
    result = ReadStringDelimited((uint32_t)((uint32_t)(result)), v_stack_p10, v_stack_mA8, v_stack_mA0);
    goto loc_005096D1;
loc_005096CA:
    Arg2 = 0;
    result = ReadString((uint32_t)((uint32_t)(result)), Arg2, v_stack_mA8, v_stack_mA0);
loc_005096D1:
    if ((uint32_t)(result) != 0) goto loc_005097AA;
    v_stack_m90 = (uint32_t)(v_stack_mA8);
loc_005096E4:
    local_r14 = (v_stack_p10) + (2);
    goto loc_0050972D;
loc_00509700:
    local_r14 = (local_r14) + (2);
loc_00509704:
    local_r15 = (uint32_t)(((uint32_t)(v_stack_mA0)) + 1);
    v_stack_mA0 = (uint32_t)(local_r15);
    result = fgetwc_nolock(v_stack_p8, Arg2, v_stack_mA8, v_stack_mA0);
    v_stack_mA8 = (uint16_t)(result);
    local_r14 = (local_r14) + (2);
    v_stack_m90 = (uint32_t)((uint16_t)(result));
    if (((uint16_t)(*(uint16_t *)(local_r14))) != ((uint16_t)((uint16_t)(result)))) goto loc_00509795;
loc_0050972D:
    if (((uint16_t)((uint32_t)(0xFFFFULL))) != ((uint16_t)((uint16_t)(result)))) goto loc_00509744;
    if ((*(uint16_t *)(local_r14)) != 37) goto loc_005097AA;
    if ((*(uint16_t *)(local_r14 + 0x2)) != 110) goto loc_005097AA;
loc_00509744:
    if ((uint16_t)(*(uint16_t *)(local_r14)) != 0) goto loc_00508EF0;
    goto loc_005097AA;
loc_00509753:
    if (((uint16_t)((uint32_t)(0xFFFFULL))) == ((uint16_t)((uint16_t)(result)))) goto loc_005097AA;
    goto loc_005097A2;
loc_00509763:
    if (condition_is_less_or_equal) goto loc_00509773;
    *(uint16_t *)(v_stack_p8) = 0;
    goto loc_005097B0;
loc_00509773:
    *(uint8_t *)(v_stack_p8) = 0;
    goto loc_005097B0;
loc_00509777:
    result = *(uint16_t *)(local_r14);
    if (((uint16_t)((uint32_t)(0xFFFFULL))) != ((uint16_t)((uint16_t)(result)))) {
        Arg2 = v_stack_p8;
        Arg1 = (uint16_t)((uint16_t)(result));
        result = ungetwc_nolock(Arg1, Arg2, 0, v_stack_mA0);
    }
    goto loc_005097AD;
loc_00509795:
    if (((uint16_t)((uint32_t)(0xFFFFULL))) == ((uint16_t)((uint16_t)(result)))) goto loc_005097AA;
loc_005097A2:
    result = ungetwc_nolock((uint16_t)((uint16_t)(result)), v_stack_p8, 1, v_stack_mA0);
loc_005097AA:
loc_005097AD:
loc_005097B0:
loc_005097B3:
    if (((uint16_t)((uint32_t)(0xFFFFULL))) == ((uint16_t)((uint16_t)(result)))) goto loc_005097DF;
    if (0 != 1) goto loc_005097F0;
    a4 = 0;
    v_stack_mD8 = 0;
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = EmpCheckErrataList(Arg1, Arg2, Arg3, a4);
    goto loc_00509808;
loc_005097DC:
loc_005097DF:
    if ((uint32_t)((uint32_t)(v_stack_m94)) != 0) goto loc_005097EA;
    if ((uint8_t)(v_stack_p20) != 0) {
        local_rbx = (uint32_t)((uint32_t)(v_stack_m94));
    }
    goto loc_00509808;
loc_005097F0:
    goto loc_00509808;
loc_005097F4:
    a4 = 0;
    v_stack_mD8 = local_rbx;
    Arg2 = 0;
    Arg1 = 0;
    result = EmpCheckErrataList(Arg1, Arg2, Arg3, a4);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
loc_00509808:
    local_rsp = (local_rsp) + (184);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00508E78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
