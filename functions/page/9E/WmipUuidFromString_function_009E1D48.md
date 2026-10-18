# WmipUuidFromString

- RVA: `0x009E1D48`–`0x009E2184` (길이 `1,084` bytes)
- VA: `0x00000001409E1D48`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A3DF4`
- 디코드: `312`개 명령, `1,084/1,084` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009E1D6E` → [WmipHexStringToDword](WmipHexStringToDword_function_009E218C.md) (function, `0x009E218C`)

### Direct callers
- [WmipOpenGuidObject](WmipOpenGuidObject_function_009E02EC.md) at `0x009E0353`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009E1D48  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
009E1D4D  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
009E1D52  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
009E1D57  57                              push rdi
009E1D58  48 83 EC 20                     sub rsp, 0x20
009E1D5C  BD 2D 00 00 00                  mov ebp, 0x2d
009E1D61  48 8B FA                        mov rdi, rdx
009E1D64  44 8B CD                        mov r9d, ebp
009E1D67  48 8B D9                        mov rbx, rcx
009E1D6A  44 8D 45 DB                     lea r8d, [rbp - 0x25]
009E1D6E  E8 19 04 00 00                  call 0x1409e218c
009E1D73  45 33 C0                        xor r8d, r8d
009E1D76  84 C0                           test al, al
009E1D78  0F 84 FC 03 00 00               je 0x1409e217a
009E1D7E  4C 8D 4B 12                     lea r9, [rbx + 0x12]
009E1D82  41 8B C8                        mov ecx, r8d
009E1D85  4D 8B D1                        mov r10, r9
009E1D88  8D 5D D5                        lea ebx, [rbp - 0x2b]
009E1D8B  45 8B D8                        mov r11d, r8d
009E1D8E  66 BE 05 00                     mov si, 5
009E1D92  41 0F B7 12                     movzx edx, word ptr [r10]
009E1D96  41 83 FB 04                     cmp r11d, 4
009E1D9A  73 1D                           jae 0x1409e1db9
009E1D9C  8D 42 D0                        lea eax, [rdx - 0x30]
009E1D9F  66 83 F8 09                     cmp ax, 9
009E1DA3  0F 87 64 01 00 00               ja 0x1409e1f0d
009E1DA9  C1 E1 04                        shl ecx, 4
009E1DAC  83 C1 D0                        add ecx, -0x30
009E1DAF  03 CA                           add ecx, edx
009E1DB1  41 FF C3                        inc r11d
009E1DB4  4C 03 D3                        add r10, rbx
009E1DB7  EB D9                           jmp 0x1409e1d92
009E1DB9  66 3B D5                        cmp dx, bp
009E1DBC  0F 85 B8 03 00 00               jne 0x1409e217a
009E1DC2  66 89 4F 04                     mov word ptr [rdi + 4], cx
009E1DC6  4D 8D 51 0A                     lea r10, [r9 + 0xa]
009E1DCA  41 8B C8                        mov ecx, r8d
009E1DCD  45 8B D8                        mov r11d, r8d
009E1DD0  41 0F B7 12                     movzx edx, word ptr [r10]
009E1DD4  41 83 FB 04                     cmp r11d, 4
009E1DD8  73 1D                           jae 0x1409e1df7
009E1DDA  8D 42 D0                        lea eax, [rdx - 0x30]
009E1DDD  66 83 F8 09                     cmp ax, 9
009E1DE1  0F 87 49 01 00 00               ja 0x1409e1f30
009E1DE7  C1 E1 04                        shl ecx, 4
009E1DEA  83 C1 D0                        add ecx, -0x30
009E1DED  03 CA                           add ecx, edx
009E1DEF  41 FF C3                        inc r11d
009E1DF2  4C 03 D3                        add r10, rbx
009E1DF5  EB D9                           jmp 0x1409e1dd0
009E1DF7  66 3B D5                        cmp dx, bp
009E1DFA  0F 85 7A 03 00 00               jne 0x1409e217a
009E1E00  66 89 4F 06                     mov word ptr [rdi + 6], cx
009E1E04  4D 8D 59 14                     lea r11, [r9 + 0x14]
009E1E08  41 8B C8                        mov ecx, r8d
009E1E0B  45 8B D0                        mov r10d, r8d
009E1E0E  44 3B D3                        cmp r10d, ebx
009E1E11  73 21                           jae 0x1409e1e34
009E1E13  41 0F B7 13                     movzx edx, word ptr [r11]
009E1E17  8D 42 D0                        lea eax, [rdx - 0x30]
009E1E1A  66 83 F8 09                     cmp ax, 9
009E1E1E  0F 87 2F 01 00 00               ja 0x1409e1f53
009E1E24  C1 E1 04                        shl ecx, 4
009E1E27  83 C1 D0                        add ecx, -0x30
009E1E2A  03 CA                           add ecx, edx
009E1E2C  41 FF C2                        inc r10d
009E1E2F  4C 03 DB                        add r11, rbx
009E1E32  EB DA                           jmp 0x1409e1e0e
009E1E34  88 4F 08                        mov byte ptr [rdi + 8], cl
009E1E37  4D 8D 51 18                     lea r10, [r9 + 0x18]
009E1E3B  41 8B C8                        mov ecx, r8d
009E1E3E  45 8B D8                        mov r11d, r8d
009E1E41  41 0F B7 12                     movzx edx, word ptr [r10]
009E1E45  44 3B DB                        cmp r11d, ebx
009E1E48  73 1D                           jae 0x1409e1e67
009E1E4A  8D 42 D0                        lea eax, [rdx - 0x30]
009E1E4D  66 83 F8 09                     cmp ax, 9
009E1E51  0F 87 1F 01 00 00               ja 0x1409e1f76
009E1E57  C1 E1 04                        shl ecx, 4
009E1E5A  83 C1 D0                        add ecx, -0x30
009E1E5D  03 CA                           add ecx, edx
009E1E5F  41 FF C3                        inc r11d
009E1E62  4C 03 D3                        add r10, rbx
009E1E65  EB DA                           jmp 0x1409e1e41
009E1E67  66 3B D5                        cmp dx, bp
009E1E6A  0F 85 0A 03 00 00               jne 0x1409e217a
009E1E70  88 4F 09                        mov byte ptr [rdi + 9], cl
009E1E73  4D 8D 59 1E                     lea r11, [r9 + 0x1e]
009E1E77  41 8B C8                        mov ecx, r8d
009E1E7A  45 8B D0                        mov r10d, r8d
009E1E7D  44 3B D3                        cmp r10d, ebx
009E1E80  73 21                           jae 0x1409e1ea3
009E1E82  41 0F B7 13                     movzx edx, word ptr [r11]
009E1E86  8D 42 D0                        lea eax, [rdx - 0x30]
009E1E89  66 83 F8 09                     cmp ax, 9
009E1E8D  0F 87 06 01 00 00               ja 0x1409e1f99
009E1E93  C1 E1 04                        shl ecx, 4
009E1E96  83 C1 D0                        add ecx, -0x30
009E1E99  03 CA                           add ecx, edx
009E1E9B  41 FF C2                        inc r10d
009E1E9E  4C 03 DB                        add r11, rbx
009E1EA1  EB DA                           jmp 0x1409e1e7d
009E1EA3  88 4F 0A                        mov byte ptr [rdi + 0xa], cl
009E1EA6  4D 8D 59 22                     lea r11, [r9 + 0x22]
009E1EAA  41 8B C8                        mov ecx, r8d
009E1EAD  45 8B D0                        mov r10d, r8d
009E1EB0  44 3B D3                        cmp r10d, ebx
009E1EB3  73 21                           jae 0x1409e1ed6
009E1EB5  41 0F B7 13                     movzx edx, word ptr [r11]
009E1EB9  8D 42 D0                        lea eax, [rdx - 0x30]
009E1EBC  66 83 F8 09                     cmp ax, 9
009E1EC0  0F 87 F6 00 00 00               ja 0x1409e1fbc
009E1EC6  C1 E1 04                        shl ecx, 4
009E1EC9  83 C1 D0                        add ecx, -0x30
009E1ECC  03 CA                           add ecx, edx
009E1ECE  41 FF C2                        inc r10d
009E1ED1  4C 03 DB                        add r11, rbx
009E1ED4  EB DA                           jmp 0x1409e1eb0
009E1ED6  88 4F 0B                        mov byte ptr [rdi + 0xb], cl
009E1ED9  4D 8D 59 26                     lea r11, [r9 + 0x26]
009E1EDD  41 8B C8                        mov ecx, r8d
009E1EE0  45 8B D0                        mov r10d, r8d
009E1EE3  44 3B D3                        cmp r10d, ebx
009E1EE6  0F 83 F3 00 00 00               jae 0x1409e1fdf
009E1EEC  41 0F B7 13                     movzx edx, word ptr [r11]
009E1EF0  8D 42 D0                        lea eax, [rdx - 0x30]
009E1EF3  66 83 F8 09                     cmp ax, 9
009E1EF7  0F 87 44 01 00 00               ja 0x1409e2041
009E1EFD  C1 E1 04                        shl ecx, 4
009E1F00  83 C1 D0                        add ecx, -0x30
009E1F03  03 CA                           add ecx, edx
009E1F05  41 FF C2                        inc r10d
009E1F08  4C 03 DB                        add r11, rbx
009E1F0B  EB D6                           jmp 0x1409e1ee3
009E1F0D  8D 42 BF                        lea eax, [rdx - 0x41]
009E1F10  66 3B C6                        cmp ax, si
009E1F13  0F 86 F1 01 00 00               jbe 0x1409e210a
009E1F19  8D 42 9F                        lea eax, [rdx - 0x61]
009E1F1C  66 3B C6                        cmp ax, si
009E1F1F  0F 87 55 02 00 00               ja 0x1409e217a
009E1F25  C1 E1 04                        shl ecx, 4
009E1F28  83 C1 A9                        add ecx, -0x57
009E1F2B  E9 7F FE FF FF                  jmp 0x1409e1daf
009E1F30  8D 42 BF                        lea eax, [rdx - 0x41]
009E1F33  66 3B C6                        cmp ax, si
009E1F36  0F 86 D9 01 00 00               jbe 0x1409e2115
009E1F3C  8D 42 9F                        lea eax, [rdx - 0x61]
009E1F3F  66 3B C6                        cmp ax, si
009E1F42  0F 87 32 02 00 00               ja 0x1409e217a
009E1F48  C1 E1 04                        shl ecx, 4
009E1F4B  83 C1 A9                        add ecx, -0x57
009E1F4E  E9 9A FE FF FF                  jmp 0x1409e1ded
009E1F53  8D 42 BF                        lea eax, [rdx - 0x41]
009E1F56  66 3B C6                        cmp ax, si
009E1F59  0F 86 C1 01 00 00               jbe 0x1409e2120
009E1F5F  8D 42 9F                        lea eax, [rdx - 0x61]
009E1F62  66 3B C6                        cmp ax, si
009E1F65  0F 87 0F 02 00 00               ja 0x1409e217a
009E1F6B  C1 E1 04                        shl ecx, 4
009E1F6E  83 C1 A9                        add ecx, -0x57
009E1F71  E9 B4 FE FF FF                  jmp 0x1409e1e2a
009E1F76  8D 42 BF                        lea eax, [rdx - 0x41]
009E1F79  66 3B C6                        cmp ax, si
009E1F7C  0F 86 A9 01 00 00               jbe 0x1409e212b
009E1F82  8D 42 9F                        lea eax, [rdx - 0x61]
009E1F85  66 3B C6                        cmp ax, si
009E1F88  0F 87 EC 01 00 00               ja 0x1409e217a
009E1F8E  C1 E1 04                        shl ecx, 4
009E1F91  83 C1 A9                        add ecx, -0x57
009E1F94  E9 C4 FE FF FF                  jmp 0x1409e1e5d
009E1F99  8D 42 BF                        lea eax, [rdx - 0x41]
009E1F9C  66 3B C6                        cmp ax, si
009E1F9F  0F 86 91 01 00 00               jbe 0x1409e2136
009E1FA5  8D 42 9F                        lea eax, [rdx - 0x61]
009E1FA8  66 3B C6                        cmp ax, si
009E1FAB  0F 87 C9 01 00 00               ja 0x1409e217a
009E1FB1  C1 E1 04                        shl ecx, 4
009E1FB4  83 C1 A9                        add ecx, -0x57
009E1FB7  E9 DD FE FF FF                  jmp 0x1409e1e99
009E1FBC  8D 42 BF                        lea eax, [rdx - 0x41]
009E1FBF  66 3B C6                        cmp ax, si
009E1FC2  0F 86 79 01 00 00               jbe 0x1409e2141
009E1FC8  8D 42 9F                        lea eax, [rdx - 0x61]
009E1FCB  66 3B C6                        cmp ax, si
009E1FCE  0F 87 A6 01 00 00               ja 0x1409e217a
009E1FD4  C1 E1 04                        shl ecx, 4
009E1FD7  83 C1 A9                        add ecx, -0x57
009E1FDA  E9 ED FE FF FF                  jmp 0x1409e1ecc
009E1FDF  88 4F 0C                        mov byte ptr [rdi + 0xc], cl
009E1FE2  4D 8D 59 2A                     lea r11, [r9 + 0x2a]
009E1FE6  41 8B C8                        mov ecx, r8d
009E1FE9  45 8B D0                        mov r10d, r8d
009E1FEC  44 3B D3                        cmp r10d, ebx
009E1FEF  73 1D                           jae 0x1409e200e
009E1FF1  41 0F B7 13                     movzx edx, word ptr [r11]
009E1FF5  8D 42 D0                        lea eax, [rdx - 0x30]
009E1FF8  66 83 F8 09                     cmp ax, 9
009E1FFC  77 66                           ja 0x1409e2064
009E1FFE  C1 E1 04                        shl ecx, 4
009E2001  83 C1 D0                        add ecx, -0x30
009E2004  03 CA                           add ecx, edx
009E2006  41 FF C2                        inc r10d
009E2009  4C 03 DB                        add r11, rbx
009E200C  EB DE                           jmp 0x1409e1fec
009E200E  88 4F 0D                        mov byte ptr [rdi + 0xd], cl
009E2011  4D 8D 59 2E                     lea r11, [r9 + 0x2e]
009E2015  41 8B C8                        mov ecx, r8d
009E2018  45 8B D0                        mov r10d, r8d
009E201B  44 3B D3                        cmp r10d, ebx
009E201E  73 64                           jae 0x1409e2084
009E2020  41 0F B7 13                     movzx edx, word ptr [r11]
009E2024  8D 42 D0                        lea eax, [rdx - 0x30]
009E2027  66 83 F8 09                     cmp ax, 9
009E202B  0F 87 9C 00 00 00               ja 0x1409e20cd
009E2031  C1 E1 04                        shl ecx, 4
009E2034  83 C1 D0                        add ecx, -0x30
009E2037  03 CA                           add ecx, edx
009E2039  41 FF C2                        inc r10d
009E203C  4C 03 DB                        add r11, rbx
009E203F  EB DA                           jmp 0x1409e201b
009E2041  8D 42 BF                        lea eax, [rdx - 0x41]
009E2044  66 3B C6                        cmp ax, si
009E2047  0F 86 FF 00 00 00               jbe 0x1409e214c
009E204D  8D 42 9F                        lea eax, [rdx - 0x61]
009E2050  66 3B C6                        cmp ax, si
009E2053  0F 87 21 01 00 00               ja 0x1409e217a
009E2059  C1 E1 04                        shl ecx, 4
009E205C  83 C1 A9                        add ecx, -0x57
009E205F  E9 9F FE FF FF                  jmp 0x1409e1f03
009E2064  8D 42 BF                        lea eax, [rdx - 0x41]
009E2067  66 3B C6                        cmp ax, si
009E206A  0F 86 E7 00 00 00               jbe 0x1409e2157
009E2070  8D 42 9F                        lea eax, [rdx - 0x61]
009E2073  66 3B C6                        cmp ax, si
009E2076  0F 87 FE 00 00 00               ja 0x1409e217a
009E207C  C1 E1 04                        shl ecx, 4
009E207F  83 C1 A9                        add ecx, -0x57
009E2082  EB 80                           jmp 0x1409e2004
009E2084  88 4F 0E                        mov byte ptr [rdi + 0xe], cl
009E2087  49 83 C1 32                     add r9, 0x32
009E208B  41 8B D0                        mov edx, r8d
009E208E  3B D3                           cmp edx, ebx
009E2090  73 1F                           jae 0x1409e20b1
009E2092  41 0F B7 09                     movzx ecx, word ptr [r9]
009E2096  8D 41 D0                        lea eax, [rcx - 0x30]
009E2099  66 83 F8 09                     cmp ax, 9
009E209D  77 51                           ja 0x1409e20f0
009E209F  41 C1 E0 04                     shl r8d, 4
009E20A3  41 83 C0 D0                     add r8d, -0x30
009E20A7  44 03 C1                        add r8d, ecx
009E20AA  FF C2                           inc edx
009E20AC  4C 03 CB                        add r9, rbx
009E20AF  EB DD                           jmp 0x1409e208e
009E20B1  44 88 47 0F                     mov byte ptr [rdi + 0xf], r8b
009E20B5  33 C0                           xor eax, eax
009E20B7  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
009E20BC  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
009E20C1  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
009E20C6  48 83 C4 20                     add rsp, 0x20
009E20CA  5F                              pop rdi
009E20CB  C3                              ret
009E20CC  CC                              int3
009E20CD  8D 42 BF                        lea eax, [rdx - 0x41]
009E20D0  66 3B C6                        cmp ax, si
009E20D3  0F 86 89 00 00 00               jbe 0x1409e2162
009E20D9  8D 42 9F                        lea eax, [rdx - 0x61]
009E20DC  66 3B C6                        cmp ax, si
009E20DF  0F 87 95 00 00 00               ja 0x1409e217a
009E20E5  C1 E1 04                        shl ecx, 4
009E20E8  83 C1 A9                        add ecx, -0x57
009E20EB  E9 47 FF FF FF                  jmp 0x1409e2037
009E20F0  8D 41 BF                        lea eax, [rcx - 0x41]
009E20F3  66 3B C6                        cmp ax, si
009E20F6  76 75                           jbe 0x1409e216d
009E20F8  8D 41 9F                        lea eax, [rcx - 0x61]
009E20FB  66 3B C6                        cmp ax, si
009E20FE  77 7A                           ja 0x1409e217a
009E2100  41 C1 E0 04                     shl r8d, 4
009E2104  41 83 C0 A9                     add r8d, -0x57
009E2108  EB 9D                           jmp 0x1409e20a7
009E210A  C1 E1 04                        shl ecx, 4
009E210D  83 C1 C9                        add ecx, -0x37
009E2110  E9 9A FC FF FF                  jmp 0x1409e1daf
009E2115  C1 E1 04                        shl ecx, 4
009E2118  83 C1 C9                        add ecx, -0x37
009E211B  E9 CD FC FF FF                  jmp 0x1409e1ded
009E2120  C1 E1 04                        shl ecx, 4
009E2123  83 C1 C9                        add ecx, -0x37
009E2126  E9 FF FC FF FF                  jmp 0x1409e1e2a
009E212B  C1 E1 04                        shl ecx, 4
009E212E  83 C1 C9                        add ecx, -0x37
009E2131  E9 27 FD FF FF                  jmp 0x1409e1e5d
009E2136  C1 E1 04                        shl ecx, 4
009E2139  83 C1 C9                        add ecx, -0x37
009E213C  E9 58 FD FF FF                  jmp 0x1409e1e99
009E2141  C1 E1 04                        shl ecx, 4
009E2144  83 C1 C9                        add ecx, -0x37
009E2147  E9 80 FD FF FF                  jmp 0x1409e1ecc
009E214C  C1 E1 04                        shl ecx, 4
009E214F  83 C1 C9                        add ecx, -0x37
009E2152  E9 AC FD FF FF                  jmp 0x1409e1f03
009E2157  C1 E1 04                        shl ecx, 4
009E215A  83 C1 C9                        add ecx, -0x37
009E215D  E9 A2 FE FF FF                  jmp 0x1409e2004
009E2162  C1 E1 04                        shl ecx, 4
009E2165  83 C1 C9                        add ecx, -0x37
009E2168  E9 CA FE FF FF                  jmp 0x1409e2037
009E216D  41 C1 E0 04                     shl r8d, 4
009E2171  41 83 C0 C9                     add r8d, -0x37
009E2175  E9 2D FF FF FF                  jmp 0x1409e20a7
009E217A  B8 0D 00 00 C0                  mov eax, 0xc000000d
009E217F  E9 33 FF FF FF                  jmp 0x1409e20b7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WmipUuidFromString(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = WmipHexStringToDword(a1, a2, 45 - 37, 45);
    a3 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_009E217A;
loc_009E1D92:
    if (0 >= 4) goto loc_009E1DB9;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18) - 48)) > 9) goto loc_009E1F0D;
    a1 = (unsigned int)((0) << (4));
    a1 = (unsigned int)((a1) + (-48));
loc_009E1DAF:
    a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int16 *)(a1 + 18))));
    v_r11 = (unsigned int)((0) + 1);
    v_r10 = (a1 + 18) + (45 - 43);
    goto loc_009E1D92;
loc_009E1DB9:
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18))) != 45) goto loc_009E217A;
    *(unsigned __int16 *)(a2 + 4) = (unsigned __int16)(a1);
loc_009E1DD0:
    if (0 >= 4) goto loc_009E1DF7;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 10) - 48)) > 9) goto loc_009E1F30;
    a1 = (unsigned int)((0) << (4));
    a1 = (unsigned int)((a1) + (-48));
loc_009E1DED:
    a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int16 *)(a1 + 18 + 10))));
    v_r11 = (unsigned int)((0) + 1);
    v_r10 = (a1 + 18 + 10) + (45 - 43);
    goto loc_009E1DD0;
loc_009E1DF7:
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 10))) != 45) goto loc_009E217A;
    *(unsigned __int16 *)(a2 + 6) = (unsigned __int16)(a1);
loc_009E1E0E:
    if (0 >= ((unsigned int)(45 - 43))) goto loc_009E1E34;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 20) - 48)) > 9) goto loc_009E1F53;
    a1 = (unsigned int)((0) << (4));
    a1 = (unsigned int)((a1) + (-48));
loc_009E1E2A:
    a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int16 *)(a1 + 18 + 20))));
    v_r10 = (unsigned int)((0) + 1);
    v_r11 = (a1 + 18 + 20) + (45 - 43);
    goto loc_009E1E0E;
loc_009E1E34:
    *(unsigned __int8 *)(a2 + 8) = (unsigned __int8)(a1);
loc_009E1E41:
    if (0 >= ((unsigned int)(45 - 43))) goto loc_009E1E67;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 24) - 48)) > 9) goto loc_009E1F76;
    a1 = (unsigned int)((0) << (4));
    a1 = (unsigned int)((a1) + (-48));
loc_009E1E5D:
    a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int16 *)(a1 + 18 + 24))));
    v_r11 = (unsigned int)((0) + 1);
    v_r10 = (a1 + 18 + 24) + (45 - 43);
    goto loc_009E1E41;
loc_009E1E67:
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 24))) != 45) goto loc_009E217A;
    *(unsigned __int8 *)(a2 + 9) = (unsigned __int8)(a1);
loc_009E1E7D:
    if (0 >= ((unsigned int)(45 - 43))) goto loc_009E1EA3;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 30) - 48)) > 9) goto loc_009E1F99;
    a1 = (unsigned int)((0) << (4));
    a1 = (unsigned int)((a1) + (-48));
loc_009E1E99:
    a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int16 *)(a1 + 18 + 30))));
    v_r10 = (unsigned int)((0) + 1);
    v_r11 = (a1 + 18 + 30) + (45 - 43);
    goto loc_009E1E7D;
loc_009E1EA3:
    *(unsigned __int8 *)(a2 + 10) = (unsigned __int8)(a1);
loc_009E1EB0:
    if (0 >= ((unsigned int)(45 - 43))) goto loc_009E1ED6;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 34) - 48)) > 9) goto loc_009E1FBC;
    a1 = (unsigned int)((0) << (4));
    a1 = (unsigned int)((a1) + (-48));
loc_009E1ECC:
    a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int16 *)(a1 + 18 + 34))));
    v_r10 = (unsigned int)((0) + 1);
    v_r11 = (a1 + 18 + 34) + (45 - 43);
    goto loc_009E1EB0;
loc_009E1ED6:
    *(unsigned __int8 *)(a2 + 11) = (unsigned __int8)(a1);
loc_009E1EE3:
    if (0 >= ((unsigned int)(45 - 43))) goto loc_009E1FDF;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 38) - 48)) > 9) goto loc_009E2041;
    a1 = (unsigned int)((0) << (4));
    a1 = (unsigned int)((a1) + (-48));
loc_009E1F03:
    a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int16 *)(a1 + 18 + 38))));
    v_r10 = (unsigned int)((0) + 1);
    v_r11 = (a1 + 18 + 38) + (45 - 43);
    goto loc_009E1EE3;
loc_009E1F0D:
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 38) - 65)) <= 5) goto loc_009E210A;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 38) - 97)) > 5) goto loc_009E217A;
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) + (-87));
    goto loc_009E1DAF;
loc_009E1F30:
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 38) - 65)) <= 5) goto loc_009E2115;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 38) - 97)) > 5) goto loc_009E217A;
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) + (-87));
    goto loc_009E1DED;
loc_009E1F53:
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 38) - 65)) <= 5) goto loc_009E2120;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 38) - 97)) > 5) goto loc_009E217A;
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) + (-87));
    goto loc_009E1E2A;
loc_009E1F76:
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 38) - 65)) <= 5) goto loc_009E212B;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 38) - 97)) > 5) goto loc_009E217A;
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) + (-87));
    goto loc_009E1E5D;
loc_009E1F99:
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 38) - 65)) <= 5) goto loc_009E2136;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 38) - 97)) > 5) goto loc_009E217A;
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) + (-87));
    goto loc_009E1E99;
loc_009E1FBC:
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 38) - 65)) <= 5) goto loc_009E2141;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 38) - 97)) > 5) goto loc_009E217A;
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) + (-87));
    goto loc_009E1ECC;
loc_009E1FDF:
    *(unsigned __int8 *)(a2 + 12) = (unsigned __int8)(a1);
loc_009E1FEC:
    if (0 >= ((unsigned int)(45 - 43))) goto loc_009E200E;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 42) - 48)) > 9) goto loc_009E2064;
    a1 = (unsigned int)((0) << (4));
    a1 = (unsigned int)((a1) + (-48));
loc_009E2004:
    a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int16 *)(a1 + 18 + 42))));
    v_r10 = (unsigned int)((0) + 1);
    v_r11 = (a1 + 18 + 42) + (45 - 43);
    goto loc_009E1FEC;
loc_009E200E:
    *(unsigned __int8 *)(a2 + 13) = (unsigned __int8)(a1);
loc_009E201B:
    if (0 >= ((unsigned int)(45 - 43))) goto loc_009E2084;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 46) - 48)) > 9) goto loc_009E20CD;
    a1 = (unsigned int)((0) << (4));
    a1 = (unsigned int)((a1) + (-48));
loc_009E2037:
    a1 = (unsigned int)((a1) + ((unsigned int)(*(unsigned __int16 *)(a1 + 18 + 46))));
    v_r10 = (unsigned int)((0) + 1);
    v_r11 = (a1 + 18 + 46) + (45 - 43);
    goto loc_009E201B;
loc_009E2041:
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 46) - 65)) <= 5) goto loc_009E214C;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 46) - 97)) > 5) goto loc_009E217A;
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) + (-87));
    goto loc_009E1F03;
loc_009E2064:
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 46) - 65)) <= 5) goto loc_009E2157;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 18 + 46) - 97)) > 5) goto loc_009E217A;
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) + (-87));
    goto loc_009E2004;
loc_009E2084:
    *(unsigned __int8 *)(a2 + 14) = (unsigned __int8)(a1);
    a4 = (a1 + 18) + (50);
loc_009E208E:
    if (0 >= ((unsigned int)(45 - 43))) goto loc_009E20B1;
    if (((unsigned __int16)(*(unsigned __int16 *)(a4) - 48)) > 9) goto loc_009E20F0;
    a3 = (unsigned int)((a3) << (4));
    a3 = (unsigned int)((a3) + (-48));
loc_009E20A7:
    a3 = (unsigned int)((a3) + ((unsigned int)(*(unsigned __int16 *)(a4))));
    a2 = (unsigned int)((0) + 1);
    a4 = (a4) + (45 - 43);
    goto loc_009E208E;
loc_009E20B1:
    *(unsigned __int8 *)(a2 + 15) = (unsigned __int8)(a3);
    result = 0;
loc_009E20B7:
    v_rsp = (v_rsp) + (32);
    return result;
loc_009E20CD:
    if (((unsigned __int16)(a2 - 65)) <= ((unsigned __int16)(v_stack_p18))) goto loc_009E2162;
    if (((unsigned __int16)(a2 - 97)) > ((unsigned __int16)(v_stack_p18))) goto loc_009E217A;
    a1 = (unsigned int)((*(unsigned __int16 *)(a4)) << (4));
    a1 = (unsigned int)((a1) + (-87));
    goto loc_009E2037;
loc_009E20F0:
    if (((unsigned __int16)(a1 - 65)) <= ((unsigned __int16)(v_stack_p18))) goto loc_009E216D;
    if (((unsigned __int16)(a1 - 97)) > ((unsigned __int16)(v_stack_p18))) goto loc_009E217A;
    a3 = (unsigned int)((a3) << (4));
    a3 = (unsigned int)((a3) + (-87));
    goto loc_009E20A7;
loc_009E210A:
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) + (-55));
    goto loc_009E1DAF;
loc_009E2115:
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) + (-55));
    goto loc_009E1DED;
loc_009E2120:
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) + (-55));
    goto loc_009E1E2A;
loc_009E212B:
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) + (-55));
    goto loc_009E1E5D;
loc_009E2136:
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) + (-55));
    goto loc_009E1E99;
loc_009E2141:
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) + (-55));
    goto loc_009E1ECC;
loc_009E214C:
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) + (-55));
    goto loc_009E1F03;
loc_009E2157:
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) + (-55));
    goto loc_009E2004;
loc_009E2162:
    a1 = (unsigned int)((a1) << (4));
    a1 = (unsigned int)((a1) + (-55));
    goto loc_009E2037;
loc_009E216D:
    a3 = (unsigned int)((a3) << (4));
    a3 = (unsigned int)((a3) + (-55));
    goto loc_009E20A7;
loc_009E217A:
    goto loc_009E20B7;
}
```

## 5. (Beta) C Style

```c
int64_t WmipUuidFromString(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = WmipHexStringToDword(Arg1, Arg2, 45 - 37, 45);
    a3 = 0;
    if ((uint8_t)(result) == 0) goto loc_009E217A;
loc_009E1D92:
    if (0 >= 4) goto loc_009E1DB9;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12) - 48)) > 9) goto loc_009E1F0D;
    Arg1 = (uint32_t)((0) << (4));
    Arg1 = (uint32_t)((Arg1) + (-48));
loc_009E1DAF:
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(*(uint16_t *)(arg1 + 0x12))));
    local_r11 = (uint32_t)((0) + 1);
    local_r10 = (Arg1 + 18) + (45 - 43);
    goto loc_009E1D92;
loc_009E1DB9:
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12))) != 45) goto loc_009E217A;
    *(uint16_t *)(arg2 + 0x4) = (uint16_t)(Arg1);
loc_009E1DD0:
    if (0 >= 4) goto loc_009E1DF7;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0xA) - 48)) > 9) goto loc_009E1F30;
    Arg1 = (uint32_t)((0) << (4));
    Arg1 = (uint32_t)((Arg1) + (-48));
loc_009E1DED:
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(*(uint16_t *)(arg1 + 0x12 + 0xA))));
    local_r11 = (uint32_t)((0) + 1);
    local_r10 = (Arg1 + 18 + 10) + (45 - 43);
    goto loc_009E1DD0;
loc_009E1DF7:
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0xA))) != 45) goto loc_009E217A;
    *(uint16_t *)(arg2 + 0x6) = (uint16_t)(Arg1);
loc_009E1E0E:
    if (0 >= ((uint32_t)(45 - 43))) goto loc_009E1E34;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x14) - 48)) > 9) goto loc_009E1F53;
    Arg1 = (uint32_t)((0) << (4));
    Arg1 = (uint32_t)((Arg1) + (-48));
loc_009E1E2A:
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(*(uint16_t *)(arg1 + 0x12 + 0x14))));
    local_r10 = (uint32_t)((0) + 1);
    local_r11 = (Arg1 + 18 + 20) + (45 - 43);
    goto loc_009E1E0E;
loc_009E1E34:
    *(uint8_t *)(arg2 + 0x8) = (uint8_t)(Arg1);
loc_009E1E41:
    if (0 >= ((uint32_t)(45 - 43))) goto loc_009E1E67;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x18) - 48)) > 9) goto loc_009E1F76;
    Arg1 = (uint32_t)((0) << (4));
    Arg1 = (uint32_t)((Arg1) + (-48));
loc_009E1E5D:
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(*(uint16_t *)(arg1 + 0x12 + 0x18))));
    local_r11 = (uint32_t)((0) + 1);
    local_r10 = (Arg1 + 18 + 24) + (45 - 43);
    goto loc_009E1E41;
loc_009E1E67:
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x18))) != 45) goto loc_009E217A;
    *(uint8_t *)(arg2 + 0x9) = (uint8_t)(Arg1);
loc_009E1E7D:
    if (0 >= ((uint32_t)(45 - 43))) goto loc_009E1EA3;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x1E) - 48)) > 9) goto loc_009E1F99;
    Arg1 = (uint32_t)((0) << (4));
    Arg1 = (uint32_t)((Arg1) + (-48));
loc_009E1E99:
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(*(uint16_t *)(arg1 + 0x12 + 0x1E))));
    local_r10 = (uint32_t)((0) + 1);
    local_r11 = (Arg1 + 18 + 30) + (45 - 43);
    goto loc_009E1E7D;
loc_009E1EA3:
    *(uint8_t *)(arg2 + 0xA) = (uint8_t)(Arg1);
loc_009E1EB0:
    if (0 >= ((uint32_t)(45 - 43))) goto loc_009E1ED6;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x22) - 48)) > 9) goto loc_009E1FBC;
    Arg1 = (uint32_t)((0) << (4));
    Arg1 = (uint32_t)((Arg1) + (-48));
loc_009E1ECC:
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(*(uint16_t *)(arg1 + 0x12 + 0x22))));
    local_r10 = (uint32_t)((0) + 1);
    local_r11 = (Arg1 + 18 + 34) + (45 - 43);
    goto loc_009E1EB0;
loc_009E1ED6:
    *(uint8_t *)(arg2 + 0xB) = (uint8_t)(Arg1);
loc_009E1EE3:
    if (0 >= ((uint32_t)(45 - 43))) goto loc_009E1FDF;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x26) - 48)) > 9) goto loc_009E2041;
    Arg1 = (uint32_t)((0) << (4));
    Arg1 = (uint32_t)((Arg1) + (-48));
loc_009E1F03:
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(*(uint16_t *)(arg1 + 0x12 + 0x26))));
    local_r10 = (uint32_t)((0) + 1);
    local_r11 = (Arg1 + 18 + 38) + (45 - 43);
    goto loc_009E1EE3;
loc_009E1F0D:
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x26) - 65)) <= 5) goto loc_009E210A;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x26) - 97)) > 5) goto loc_009E217A;
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) + (-87));
    goto loc_009E1DAF;
loc_009E1F30:
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x26) - 65)) <= 5) goto loc_009E2115;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x26) - 97)) > 5) goto loc_009E217A;
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) + (-87));
    goto loc_009E1DED;
loc_009E1F53:
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x26) - 65)) <= 5) goto loc_009E2120;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x26) - 97)) > 5) goto loc_009E217A;
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) + (-87));
    goto loc_009E1E2A;
loc_009E1F76:
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x26) - 65)) <= 5) goto loc_009E212B;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x26) - 97)) > 5) goto loc_009E217A;
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) + (-87));
    goto loc_009E1E5D;
loc_009E1F99:
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x26) - 65)) <= 5) goto loc_009E2136;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x26) - 97)) > 5) goto loc_009E217A;
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) + (-87));
    goto loc_009E1E99;
loc_009E1FBC:
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x26) - 65)) <= 5) goto loc_009E2141;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x26) - 97)) > 5) goto loc_009E217A;
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) + (-87));
    goto loc_009E1ECC;
loc_009E1FDF:
    *(uint8_t *)(arg2 + 0xC) = (uint8_t)(Arg1);
loc_009E1FEC:
    if (0 >= ((uint32_t)(45 - 43))) goto loc_009E200E;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x2A) - 48)) > 9) goto loc_009E2064;
    Arg1 = (uint32_t)((0) << (4));
    Arg1 = (uint32_t)((Arg1) + (-48));
loc_009E2004:
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(*(uint16_t *)(arg1 + 0x12 + 0x2A))));
    local_r10 = (uint32_t)((0) + 1);
    local_r11 = (Arg1 + 18 + 42) + (45 - 43);
    goto loc_009E1FEC;
loc_009E200E:
    *(uint8_t *)(arg2 + 0xD) = (uint8_t)(Arg1);
loc_009E201B:
    if (0 >= ((uint32_t)(45 - 43))) goto loc_009E2084;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x2E) - 48)) > 9) goto loc_009E20CD;
    Arg1 = (uint32_t)((0) << (4));
    Arg1 = (uint32_t)((Arg1) + (-48));
loc_009E2037:
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(*(uint16_t *)(arg1 + 0x12 + 0x2E))));
    local_r10 = (uint32_t)((0) + 1);
    local_r11 = (Arg1 + 18 + 46) + (45 - 43);
    goto loc_009E201B;
loc_009E2041:
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x2E) - 65)) <= 5) goto loc_009E214C;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x2E) - 97)) > 5) goto loc_009E217A;
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) + (-87));
    goto loc_009E1F03;
loc_009E2064:
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x2E) - 65)) <= 5) goto loc_009E2157;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x12 + 0x2E) - 97)) > 5) goto loc_009E217A;
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) + (-87));
    goto loc_009E2004;
loc_009E2084:
    *(uint8_t *)(arg2 + 0xE) = (uint8_t)(Arg1);
    a4 = (Arg1 + 18) + (50);
loc_009E208E:
    if (0 >= ((uint32_t)(45 - 43))) goto loc_009E20B1;
    if (((uint16_t)(*(uint16_t *)(a4) - 48)) > 9) goto loc_009E20F0;
    a3 = (uint32_t)((a3) << (4));
    a3 = (uint32_t)((a3) + (-48));
loc_009E20A7:
    a3 = (uint32_t)((a3) + ((uint32_t)(*(uint16_t *)(a4))));
    Arg2 = (uint32_t)((0) + 1);
    a4 = (a4) + (45 - 43);
    goto loc_009E208E;
loc_009E20B1:
    *(uint8_t *)(arg2 + 0xF) = (uint8_t)(a3);
    result = 0;
loc_009E20B7:
    local_rsp = (local_rsp) + (32);
    return result;
loc_009E20CD:
    if (((uint16_t)(Arg2 - 65)) <= ((uint16_t)(v_stack_p18))) goto loc_009E2162;
    if (((uint16_t)(Arg2 - 97)) > ((uint16_t)(v_stack_p18))) goto loc_009E217A;
    Arg1 = (uint32_t)((*(uint16_t *)(a4)) << (4));
    Arg1 = (uint32_t)((Arg1) + (-87));
    goto loc_009E2037;
loc_009E20F0:
    if (((uint16_t)(Arg1 - 65)) <= ((uint16_t)(v_stack_p18))) goto loc_009E216D;
    if (((uint16_t)(Arg1 - 97)) > ((uint16_t)(v_stack_p18))) goto loc_009E217A;
    a3 = (uint32_t)((a3) << (4));
    a3 = (uint32_t)((a3) + (-87));
    goto loc_009E20A7;
loc_009E210A:
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) + (-55));
    goto loc_009E1DAF;
loc_009E2115:
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) + (-55));
    goto loc_009E1DED;
loc_009E2120:
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) + (-55));
    goto loc_009E1E2A;
loc_009E212B:
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) + (-55));
    goto loc_009E1E5D;
loc_009E2136:
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) + (-55));
    goto loc_009E1E99;
loc_009E2141:
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) + (-55));
    goto loc_009E1ECC;
loc_009E214C:
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) + (-55));
    goto loc_009E1F03;
loc_009E2157:
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) + (-55));
    goto loc_009E2004;
loc_009E2162:
    Arg1 = (uint32_t)((Arg1) << (4));
    Arg1 = (uint32_t)((Arg1) + (-55));
    goto loc_009E2037;
loc_009E216D:
    a3 = (uint32_t)((a3) << (4));
    a3 = (uint32_t)((a3) + (-55));
    goto loc_009E20A7;
loc_009E217A:
    goto loc_009E20B7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0xA` | `64` | `R` |
| `Arg1` | `+ 0x12` | `64` | `R` |
| `Arg1` | `+ 0x14` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x1E` | `64` | `R` |
| `Arg1` | `+ 0x22` | `64` | `R` |
| `Arg1` | `+ 0x26` | `64` | `R` |
| `Arg1` | `+ 0x2A` | `64` | `R` |
| `Arg1` | `+ 0x2E` | `64` | `R` |
| `Arg2` | `+ 0x4` | `16` | `W` |
| `Arg2` | `+ 0x6` | `16` | `W` |
| `Arg2` | `+ 0x8` | `8` | `W` |
| `Arg2` | `+ 0x9` | `8` | `W` |
| `Arg2` | `+ 0xA` | `8` | `W` |
| `Arg2` | `+ 0xB` | `8` | `W` |
| `Arg2` | `+ 0xC` | `8` | `W` |
| `Arg2` | `+ 0xD` | `8` | `W` |
| `Arg2` | `+ 0xE` | `8` | `W` |
| `Arg2` | `+ 0xF` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009E1D48&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
