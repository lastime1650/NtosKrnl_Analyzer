# RtlDecompressBufferLz4

- RVA: `0x003A4D20`–`0x003A5312` (길이 `1,522` bytes)
- VA: `0x00000001403A4D20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00089A24`
- 디코드: `403`개 명령, `1,522/1,522` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x003A5174` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [SmStoreDecompressBuffer](SmStoreDecompressBuffer_function_003A4B6C.md) at `0x003A4C00`
- [RtlDecompressBufferEx](RtlDecompressBufferEx_function_003A4C60.md) at `0x003A4CCE`

### Static image references
- `0x003A504C` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x003A530D` → [sub_006E6B00](../6E/Unknown_function_006E6B00.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003A4D20  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003A4D25  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
003A4D2A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
003A4D2F  57                              push rdi
003A4D30  41 54                           push r12
003A4D32  41 55                           push r13
003A4D34  41 56                           push r14
003A4D36  41 57                           push r15
003A4D38  48 83 EC 20                     sub rsp, 0x20
003A4D3C  48 63 C2                        movsxd rax, edx
003A4D3F  49 8B D8                        mov rbx, r8
003A4D42  4C 8B F1                        mov r14, rcx
003A4D45  4D 85 C0                        test r8, r8
003A4D48  74 3A                           je 0x1403a4d84
003A4D4A  85 D2                           test edx, edx
003A4D4C  78 36                           js 0x1403a4d84
003A4D4E  49 63 F1                        movsxd rsi, r9d
003A4D51  48 8D 2C 08                     lea rbp, [rax + rcx]
003A4D55  48 03 F3                        add rsi, rbx
003A4D58  4C 8D 65 E0                     lea r12, [rbp - 0x20]
003A4D5C  48 8B D3                        mov rdx, rbx
003A4D5F  4C 8D 6E F0                     lea r13, [rsi - 0x10]
003A4D63  85 C0                           test eax, eax
003A4D65  75 18                           jne 0x1403a4d7f
003A4D67  41 83 F9 01                     cmp r9d, 1
003A4D6B  0F 85 7A 05 00 00               jne 0x1403a52eb
003A4D71  41 38 00                        cmp byte ptr [r8], al
003A4D74  0F 85 71 05 00 00               jne 0x1403a52eb
003A4D7A  45 33 FF                        xor r15d, r15d
003A4D7D  EB 17                           jmp 0x1403a4d96
003A4D7F  45 85 C9                        test r9d, r9d
003A4D82  75 3A                           jne 0x1403a4dbe
003A4D84  B8 23 00 00 C0                  mov eax, 0xc0000023
003A4D89  EB 15                           jmp 0x1403a4da0
003A4D8B  2B DA                           sub ebx, edx
003A4D8D  44 8D 7B FF                     lea r15d, [rbx - 1]
003A4D91  45 85 FF                        test r15d, r15d
003A4D94  78 EE                           js 0x1403a4d84
003A4D96  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
003A4D9B  44 89 38                        mov dword ptr [rax], r15d
003A4D9E  33 C0                           xor eax, eax
003A4DA0  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
003A4DA5  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
003A4DAA  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
003A4DAF  48 83 C4 20                     add rsp, 0x20
003A4DB3  41 5F                           pop r15
003A4DB5  41 5E                           pop r14
003A4DB7  41 5D                           pop r13
003A4DB9  41 5C                           pop r12
003A4DBB  5F                              pop rdi
003A4DBC  C3                              ret
003A4DBD  CC                              int3
003A4DBE  45 33 FF                        xor r15d, r15d
003A4DC1  48 83 F8 40                     cmp rax, 0x40
003A4DC5  0F 82 12 03 00 00               jb 0x1403a50dd
003A4DCB  0F 1F 44 00 00                  nop dword ptr [rax + rax]
003A4DD0  44 0F B6 12                     movzx r10d, byte ptr [rdx]
003A4DD4  48 FF C2                        inc rdx
003A4DD7  45 8B C2                        mov r8d, r10d
003A4DDA  45 8B CA                        mov r9d, r10d
003A4DDD  49 C1 E8 04                     shr r8, 4
003A4DE1  49 83 F8 0F                     cmp r8, 0xf
003A4DE5  0F 84 41 01 00 00               je 0x1403a4f2c
003A4DEB  48 8D 46 EF                     lea rax, [rsi - 0x11]
003A4DEF  48 3B D0                        cmp rdx, rax
003A4DF2  0F 87 55 03 00 00               ja 0x1403a514d
003A4DF8  0F 10 02                        movups xmm0, xmmword ptr [rdx]
003A4DFB  49 03 D0                        add rdx, r8
003A4DFE  0F 11 01                        movups xmmword ptr [rcx], xmm0
003A4E01  49 03 C8                        add rcx, r8
003A4E04  44 0F B7 02                     movzx r8d, word ptr [rdx]
003A4E08  48 8B F9                        mov rdi, rcx
003A4E0B  49 2B F8                        sub rdi, r8
003A4E0E  48 83 C2 02                     add rdx, 2
003A4E12  41 83 E1 0F                     and r9d, 0xf
003A4E16  49 83 F9 0F                     cmp r9, 0xf
003A4E1A  74 42                           je 0x1403a4e5e
003A4E1C  49 83 C1 04                     add r9, 4
003A4E20  48 8D 45 C0                     lea rax, [rbp - 0x40]
003A4E24  4D 8D 14 09                     lea r10, [r9 + rcx]
003A4E28  4C 3B D0                        cmp r10, rax
003A4E2B  0F 83 01 02 00 00               jae 0x1403a5032
003A4E31  49 3B FE                        cmp rdi, r14
003A4E34  0F 82 51 FF FF FF               jb 0x1403a4d8b
003A4E3A  49 83 F8 08                     cmp r8, 8
003A4E3E  72 70                           jb 0x1403a4eb0
003A4E40  48 8B 07                        mov rax, qword ptr [rdi]
003A4E43  48 89 01                        mov qword ptr [rcx], rax
003A4E46  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
003A4E4A  48 89 41 08                     mov qword ptr [rcx + 8], rax
003A4E4E  0F B7 47 10                     movzx eax, word ptr [rdi + 0x10]
003A4E52  66 89 41 10                     mov word ptr [rcx + 0x10], ax
003A4E56  49 8B CA                        mov rcx, r10
003A4E59  E9 72 FF FF FF                  jmp 0x1403a4dd0
003A4E5E  4C 8D 56 FC                     lea r10, [rsi - 4]
003A4E62  4D 8B CF                        mov r9, r15
003A4E65  0F B6 02                        movzx eax, byte ptr [rdx]
003A4E68  48 FF C2                        inc rdx
003A4E6B  4C 03 C8                        add r9, rax
003A4E6E  49 3B D2                        cmp rdx, r10
003A4E71  0F 87 14 FF FF FF               ja 0x1403a4d8b
003A4E77  48 3D FF 00 00 00               cmp rax, 0xff
003A4E7D  74 E6                           je 0x1403a4e65
003A4E7F  49 83 F9 FF                     cmp r9, -1
003A4E83  0F 84 02 FF FF FF               je 0x1403a4d8b
003A4E89  49 83 C1 13                     add r9, 0x13
003A4E8D  4D 8D 14 09                     lea r10, [r9 + rcx]
003A4E91  4C 3B D1                        cmp r10, rcx
003A4E94  0F 82 F1 FE FF FF               jb 0x1403a4d8b
003A4E9A  48 8D 45 C0                     lea rax, [rbp - 0x40]
003A4E9E  4C 3B D0                        cmp r10, rax
003A4EA1  0F 83 8B 01 00 00               jae 0x1403a5032
003A4EA7  49 3B FE                        cmp rdi, r14
003A4EAA  0F 82 DB FE FF FF               jb 0x1403a4d8b
003A4EB0  4D 8D 14 09                     lea r10, [r9 + rcx]
003A4EB4  49 83 F8 10                     cmp r8, 0x10
003A4EB8  73 4A                           jae 0x1403a4f04
003A4EBA  49 83 F8 02                     cmp r8, 2
003A4EBE  0F 85 05 01 00 00               jne 0x1403a4fc9
003A4EC4  0F B7 07                        movzx eax, word ptr [rdi]
003A4EC7  66 89 44 24 60                  mov word ptr [rsp + 0x60], ax
003A4ECC  66 89 44 24 62                  mov word ptr [rsp + 0x62], ax
003A4ED1  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
003A4ED5  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
003A4ED9  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
003A4EDE  48 8D 79 08                     lea rdi, [rcx + 8]
003A4EE2  48 89 01                        mov qword ptr [rcx], rax
003A4EE5  49 8B CA                        mov rcx, r10
003A4EE8  48 2B CF                        sub rcx, rdi
003A4EEB  48 83 C1 07                     add rcx, 7
003A4EEF  48 C1 E9 03                     shr rcx, 3
003A4EF3  49 3B FA                        cmp rdi, r10
003A4EF6  49 0F 47 CF                     cmova rcx, r15
003A4EFA  48 85 C9                        test rcx, rcx
003A4EFD  74 25                           je 0x1403a4f24
003A4EFF  F3 48 AB                        rep stosq qword ptr [rdi], rax
003A4F02  EB 20                           jmp 0x1403a4f24
003A4F04  0F 10 07                        movups xmm0, xmmword ptr [rdi]
003A4F07  48 8D 7F 20                     lea rdi, [rdi + 0x20]
003A4F0B  49 8D 04 38                     lea rax, [r8 + rdi]
003A4F0F  41 0F 11 44 38 E0               movups xmmword ptr [r8 + rdi - 0x20], xmm0
003A4F15  0F 10 47 F0                     movups xmm0, xmmword ptr [rdi - 0x10]
003A4F19  41 0F 11 44 38 F0               movups xmmword ptr [r8 + rdi - 0x10], xmm0
003A4F1F  49 3B C2                        cmp rax, r10
003A4F22  72 E0                           jb 0x1403a4f04
003A4F24  49 8B CA                        mov rcx, r10
003A4F27  E9 A4 FE FF FF                  jmp 0x1403a4dd0
003A4F2C  48 8D 7E F1                     lea rdi, [rsi - 0xf]
003A4F30  4D 8B C7                        mov r8, r15
003A4F33  48 3B D7                        cmp rdx, rdi
003A4F36  0F 83 4F FE FF FF               jae 0x1403a4d8b
003A4F3C  0F 1F 40 00                     nop dword ptr [rax]
003A4F40  0F B6 02                        movzx eax, byte ptr [rdx]
003A4F43  48 FF C2                        inc rdx
003A4F46  4C 03 C0                        add r8, rax
003A4F49  48 3B D7                        cmp rdx, rdi
003A4F4C  0F 87 39 FE FF FF               ja 0x1403a4d8b
003A4F52  48 3D FF 00 00 00               cmp rax, 0xff
003A4F58  74 E6                           je 0x1403a4f40
003A4F5A  49 83 F8 FF                     cmp r8, -1
003A4F5E  0F 84 27 FE FF FF               je 0x1403a4d8b
003A4F64  49 83 C0 0F                     add r8, 0xf
003A4F68  49 8D 3C 08                     lea rdi, [r8 + rcx]
003A4F6C  48 3B F9                        cmp rdi, rcx
003A4F6F  0F 82 16 FE FF FF               jb 0x1403a4d8b
003A4F75  4D 8D 1C 10                     lea r11, [r8 + rdx]
003A4F79  4C 3B DA                        cmp r11, rdx
003A4F7C  0F 82 09 FE FF FF               jb 0x1403a4d8b
003A4F82  49 3B FC                        cmp rdi, r12
003A4F85  0F 87 C2 01 00 00               ja 0x1403a514d
003A4F8B  48 8D 46 E0                     lea rax, [rsi - 0x20]
003A4F8F  4C 3B D8                        cmp r11, rax
003A4F92  0F 87 B5 01 00 00               ja 0x1403a514d
003A4F98  48 2B CA                        sub rcx, rdx
003A4F9B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
003A4FA0  0F 10 02                        movups xmm0, xmmword ptr [rdx]
003A4FA3  48 8D 52 20                     lea rdx, [rdx + 0x20]
003A4FA7  48 8D 04 11                     lea rax, [rcx + rdx]
003A4FAB  0F 11 44 11 E0                  movups xmmword ptr [rcx + rdx - 0x20], xmm0
003A4FB0  0F 10 42 F0                     movups xmm0, xmmword ptr [rdx - 0x10]
003A4FB4  0F 11 44 11 F0                  movups xmmword ptr [rcx + rdx - 0x10], xmm0
003A4FB9  48 3B C7                        cmp rax, rdi
003A4FBC  72 E2                           jb 0x1403a4fa0
003A4FBE  49 8B D3                        mov rdx, r11
003A4FC1  48 8B CF                        mov rcx, rdi
003A4FC4  E9 3B FE FF FF                  jmp 0x1403a4e04
003A4FC9  49 8B C0                        mov rax, r8
003A4FCC  48 83 E8 01                     sub rax, 1
003A4FD0  0F 84 DE 02 00 00               je 0x1403a52b4
003A4FD6  48 83 F8 03                     cmp rax, 3
003A4FDA  0F 85 38 02 00 00               jne 0x1403a5218
003A4FE0  8B 07                           mov eax, dword ptr [rdi]
003A4FE2  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
003A4FE6  E9 EA FE FF FF                  jmp 0x1403a4ed5
003A4FEB  4D 8D 0C 10                     lea r9, [r8 + rdx]
003A4FEF  48 8D 46 F8                     lea rax, [rsi - 8]
003A4FF3  4C 3B C8                        cmp r9, rax
003A4FF6  0F 87 62 01 00 00               ja 0x1403a515e
003A4FFC  48 2B D1                        sub rdx, rcx
003A4FFF  48 8B 04 11                     mov rax, qword ptr [rcx + rdx]
003A5003  48 89 01                        mov qword ptr [rcx], rax
003A5006  48 83 C1 08                     add rcx, 8
003A500A  48 3B CF                        cmp rcx, rdi
003A500D  72 F0                           jb 0x1403a4fff
003A500F  45 0F B7 01                     movzx r8d, word ptr [r9]
003A5013  49 8D 51 02                     lea rdx, [r9 + 2]
003A5017  48 8B CF                        mov rcx, rdi
003A501A  45 8B CA                        mov r9d, r10d
003A501D  49 2B F8                        sub rdi, r8
003A5020  41 83 E1 0F                     and r9d, 0xf
003A5024  49 83 F9 0F                     cmp r9, 0xf
003A5028  0F 84 92 01 00 00               je 0x1403a51c0
003A502E  49 83 C1 04                     add r9, 4
003A5032  49 3B FE                        cmp rdi, r14
003A5035  0F 82 50 FD FF FF               jb 0x1403a4d8b
003A503B  4D 8D 14 09                     lea r10, [r9 + rcx]
003A503F  49 83 F8 08                     cmp r8, 8
003A5043  0F 83 3B 01 00 00               jae 0x1403a5184
003A5049  0F B6 07                        movzx eax, byte ptr [rdi]
003A504C  4C 8D 1D AD AF C5 FF            lea r11, [rip - 0x3a5053]
003A5053  88 01                           mov byte ptr [rcx], al
003A5055  0F B6 47 01                     movzx eax, byte ptr [rdi + 1]
003A5059  88 41 01                        mov byte ptr [rcx + 1], al
003A505C  0F B6 47 02                     movzx eax, byte ptr [rdi + 2]
003A5060  88 41 02                        mov byte ptr [rcx + 2], al
003A5063  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
003A5067  88 41 03                        mov byte ptr [rcx + 3], al
003A506A  43 8B 84 83 60 63 03 00         mov eax, dword ptr [r11 + r8*4 + 0x36360]
003A5072  48 03 F8                        add rdi, rax
003A5075  8B 07                           mov eax, dword ptr [rdi]
003A5077  89 41 04                        mov dword ptr [rcx + 4], eax
003A507A  4B 63 84 83 40 63 03 00         movsxd rax, dword ptr [r11 + r8*4 + 0x36340]
003A5082  48 2B F8                        sub rdi, rax
003A5085  48 83 C1 08                     add rcx, 8
003A5089  48 8D 45 F4                     lea rax, [rbp - 0xc]
003A508D  4C 3B D0                        cmp r10, rax
003A5090  0F 86 60 02 00 00               jbe 0x1403a52f6
003A5096  48 8D 45 FB                     lea rax, [rbp - 5]
003A509A  4C 8D 4D F9                     lea r9, [rbp - 7]
003A509E  4C 3B D0                        cmp r10, rax
003A50A1  0F 87 E4 FC FF FF               ja 0x1403a4d8b
003A50A7  49 3B C9                        cmp rcx, r9
003A50AA  73 25                           jae 0x1403a50d1
003A50AC  4C 8B DF                        mov r11, rdi
003A50AF  4C 8B C1                        mov r8, rcx
003A50B2  4C 2B D9                        sub r11, rcx
003A50B5  4B 8B 04 18                     mov rax, qword ptr [r8 + r11]
003A50B9  49 89 00                        mov qword ptr [r8], rax
003A50BC  49 83 C0 08                     add r8, 8
003A50C0  4D 3B C1                        cmp r8, r9
003A50C3  72 F0                           jb 0x1403a50b5
003A50C5  49 8B C1                        mov rax, r9
003A50C8  48 2B C1                        sub rax, rcx
003A50CB  49 8B C9                        mov rcx, r9
003A50CE  48 03 F8                        add rdi, rax
003A50D1  49 3B CA                        cmp rcx, r10
003A50D4  0F 82 27 01 00 00               jb 0x1403a5201
003A50DA  49 8B CA                        mov rcx, r10
003A50DD  44 0F B6 12                     movzx r10d, byte ptr [rdx]
003A50E1  48 FF C2                        inc rdx
003A50E4  45 8B C2                        mov r8d, r10d
003A50E7  45 8B CA                        mov r9d, r10d
003A50EA  49 C1 E8 04                     shr r8, 4
003A50EE  49 83 F8 0F                     cmp r8, 0xf
003A50F2  75 54                           jne 0x1403a5148
003A50F4  4C 8D 4E F1                     lea r9, [rsi - 0xf]
003A50F8  49 8B C7                        mov rax, r15
003A50FB  49 3B D1                        cmp rdx, r9
003A50FE  0F 83 87 FC FF FF               jae 0x1403a4d8b
003A5104  0F B6 3A                        movzx edi, byte ptr [rdx]
003A5107  48 FF C2                        inc rdx
003A510A  48 03 C7                        add rax, rdi
003A510D  49 3B D1                        cmp rdx, r9
003A5110  0F 87 75 FC FF FF               ja 0x1403a4d8b
003A5116  48 81 FF FF 00 00 00            cmp rdi, 0xff
003A511D  74 E5                           je 0x1403a5104
003A511F  48 83 F8 FF                     cmp rax, -1
003A5123  0F 84 62 FC FF FF               je 0x1403a4d8b
003A5129  4C 03 C0                        add r8, rax
003A512C  49 8D 04 08                     lea rax, [r8 + rcx]
003A5130  48 3B C1                        cmp rax, rcx
003A5133  0F 82 52 FC FF FF               jb 0x1403a4d8b
003A5139  49 8D 04 10                     lea rax, [r8 + rdx]
003A513D  48 3B C2                        cmp rax, rdx
003A5140  0F 82 45 FC FF FF               jb 0x1403a4d8b
003A5146  EB 05                           jmp 0x1403a514d
003A5148  49 3B CC                        cmp rcx, r12
003A514B  76 46                           jbe 0x1403a5193
003A514D  49 8D 3C 08                     lea rdi, [r8 + rcx]
003A5151  48 8D 45 F4                     lea rax, [rbp - 0xc]
003A5155  48 3B F8                        cmp rdi, rax
003A5158  0F 86 8D FE FF FF               jbe 0x1403a4feb
003A515E  49 8D 04 10                     lea rax, [r8 + rdx]
003A5162  48 3B C6                        cmp rax, rsi
003A5165  0F 85 20 FC FF FF               jne 0x1403a4d8b
003A516B  48 3B FD                        cmp rdi, rbp
003A516E  0F 87 17 FC FF FF               ja 0x1403a4d8b
003A5174  E8 C7 16 32 00                  call 0x1406c6840
003A5179  41 2B FE                        sub edi, r14d
003A517C  44 8B FF                        mov r15d, edi
003A517F  E9 0D FC FF FF                  jmp 0x1403a4d91
003A5184  48 8B 07                        mov rax, qword ptr [rdi]
003A5187  48 83 C7 08                     add rdi, 8
003A518B  48 89 01                        mov qword ptr [rcx], rax
003A518E  E9 F2 FE FF FF                  jmp 0x1403a5085
003A5193  49 3B D5                        cmp rdx, r13
003A5196  73 B5                           jae 0x1403a514d
003A5198  0F 10 02                        movups xmm0, xmmword ptr [rdx]
003A519B  49 03 D0                        add rdx, r8
003A519E  41 83 E1 0F                     and r9d, 0xf
003A51A2  0F 11 01                        movups xmmword ptr [rcx], xmm0
003A51A5  49 03 C8                        add rcx, r8
003A51A8  44 0F B7 02                     movzx r8d, word ptr [rdx]
003A51AC  48 8B F9                        mov rdi, rcx
003A51AF  49 2B F8                        sub rdi, r8
003A51B2  48 83 C2 02                     add rdx, 2
003A51B6  49 83 F9 0F                     cmp r9, 0xf
003A51BA  0F 85 BF 00 00 00               jne 0x1403a527f
003A51C0  4C 8D 56 FC                     lea r10, [rsi - 4]
003A51C4  4D 8B CF                        mov r9, r15
003A51C7  0F B6 02                        movzx eax, byte ptr [rdx]
003A51CA  48 FF C2                        inc rdx
003A51CD  4C 03 C8                        add r9, rax
003A51D0  49 3B D2                        cmp rdx, r10
003A51D3  0F 87 B2 FB FF FF               ja 0x1403a4d8b
003A51D9  48 3D FF 00 00 00               cmp rax, 0xff
003A51DF  74 E6                           je 0x1403a51c7
003A51E1  49 83 F9 FF                     cmp r9, -1
003A51E5  0F 84 A0 FB FF FF               je 0x1403a4d8b
003A51EB  49 83 C1 0F                     add r9, 0xf
003A51EF  49 8D 04 09                     lea rax, [r9 + rcx]
003A51F3  48 3B C1                        cmp rax, rcx
003A51F6  0F 82 8F FB FF FF               jb 0x1403a4d8b
003A51FC  E9 2D FE FF FF                  jmp 0x1403a502e
003A5201  0F B6 07                        movzx eax, byte ptr [rdi]
003A5204  48 8D 7F 01                     lea rdi, [rdi + 1]
003A5208  88 01                           mov byte ptr [rcx], al
003A520A  48 FF C1                        inc rcx
003A520D  49 3B CA                        cmp rcx, r10
003A5210  0F 83 C4 FE FF FF               jae 0x1403a50da
003A5216  EB E9                           jmp 0x1403a5201
003A5218  49 83 F8 08                     cmp r8, 8
003A521C  0F 83 BA 00 00 00               jae 0x1403a52dc
003A5222  0F AE E8                        lfence
003A5225  0F B6 07                        movzx eax, byte ptr [rdi]
003A5228  4C 8D 1D D1 AD C5 FF            lea r11, [rip - 0x3a522f]
003A522F  47 8B 8C 83 60 63 03 00         mov r9d, dword ptr [r11 + r8*4 + 0x36360]
003A5237  88 01                           mov byte ptr [rcx], al
003A5239  4C 03 CF                        add r9, rdi
003A523C  0F B6 47 01                     movzx eax, byte ptr [rdi + 1]
003A5240  88 41 01                        mov byte ptr [rcx + 1], al
003A5243  0F B6 47 02                     movzx eax, byte ptr [rdi + 2]
003A5247  88 41 02                        mov byte ptr [rcx + 2], al
003A524A  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
003A524E  88 41 03                        mov byte ptr [rcx + 3], al
003A5251  41 8B 01                        mov eax, dword ptr [r9]
003A5254  89 41 04                        mov dword ptr [rcx + 4], eax
003A5257  4B 63 84 83 40 63 03 00         movsxd rax, dword ptr [r11 + r8*4 + 0x36340]
003A525F  4C 2B C8                        sub r9, rax
003A5262  48 83 C1 08                     add rcx, 8
003A5266  4C 2B C9                        sub r9, rcx
003A5269  4A 8B 04 09                     mov rax, qword ptr [rcx + r9]
003A526D  48 89 01                        mov qword ptr [rcx], rax
003A5270  48 83 C1 08                     add rcx, 8
003A5274  49 3B CA                        cmp rcx, r10
003A5277  0F 83 A7 FC FF FF               jae 0x1403a4f24
003A527D  EB EA                           jmp 0x1403a5269
003A527F  49 83 F8 08                     cmp r8, 8
003A5283  0F 82 9B FD FF FF               jb 0x1403a5024
003A5289  49 3B FE                        cmp rdi, r14
003A528C  0F 82 92 FD FF FF               jb 0x1403a5024
003A5292  48 8B 07                        mov rax, qword ptr [rdi]
003A5295  48 89 01                        mov qword ptr [rcx], rax
003A5298  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
003A529C  48 89 41 08                     mov qword ptr [rcx + 8], rax
003A52A0  0F B7 47 10                     movzx eax, word ptr [rdi + 0x10]
003A52A4  66 89 41 10                     mov word ptr [rcx + 0x10], ax
003A52A8  48 83 C1 04                     add rcx, 4
003A52AC  49 03 C9                        add rcx, r9
003A52AF  E9 29 FE FF FF                  jmp 0x1403a50dd
003A52B4  0F B6 07                        movzx eax, byte ptr [rdi]
003A52B7  88 44 24 60                     mov byte ptr [rsp + 0x60], al
003A52BB  88 44 24 61                     mov byte ptr [rsp + 0x61], al
003A52BF  88 44 24 62                     mov byte ptr [rsp + 0x62], al
003A52C3  88 44 24 63                     mov byte ptr [rsp + 0x63], al
003A52C7  88 44 24 64                     mov byte ptr [rsp + 0x64], al
003A52CB  88 44 24 65                     mov byte ptr [rsp + 0x65], al
003A52CF  88 44 24 66                     mov byte ptr [rsp + 0x66], al
003A52D3  88 44 24 67                     mov byte ptr [rsp + 0x67], al
003A52D7  E9 FD FB FF FF                  jmp 0x1403a4ed9
003A52DC  48 8B 07                        mov rax, qword ptr [rdi]
003A52DF  4C 8D 4F 08                     lea r9, [rdi + 8]
003A52E3  48 89 01                        mov qword ptr [rcx], rax
003A52E6  E9 77 FF FF FF                  jmp 0x1403a5262
003A52EB  41 BF FF FF FF FF               mov r15d, 0xffffffff
003A52F1  E9 9B FA FF FF                  jmp 0x1403a4d91
003A52F6  48 8B 07                        mov rax, qword ptr [rdi]
003A52F9  48 89 01                        mov qword ptr [rcx], rax
003A52FC  49 83 F9 10                     cmp r9, 0x10
003A5300  0F 86 D4 FD FF FF               jbe 0x1403a50da
003A5306  48 83 C1 08                     add rcx, 8
003A530A  48 2B F9                        sub rdi, rcx
003A530D  E9 EE 17 34 00                  jmp 0x1406e6b00
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlDecompressBufferLz4(__int64 a1, int a2, __int64 a3, int a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int16 v_stack_p60;
    unsigned __int8 v_stack_p61;
    unsigned __int16 v_stack_p62;
    unsigned __int8 v_stack_p63;
    unsigned int v_stack_p64;
    unsigned __int8 v_stack_p65;
    unsigned __int8 v_stack_p66;
    unsigned __int8 v_stack_p67;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (32);
    if (a3 == 0) goto loc_003A4D84;
    if (sign_flag) goto loc_003A4D84;
    v_rsi = ((int)(a4)) + (a3);
    if ((unsigned int)((int)(a2)) != 0) goto loc_003A4D7F;
    if (a4 != 1) goto loc_003A52EB;
    if ((*(unsigned __int8 *)(a3)) != ((unsigned __int8)((int)(a2)))) goto loc_003A52EB;
    v_r15 = 0;
    goto loc_003A4D96;
loc_003A4D7F:
    if (a4 != 0) goto loc_003A4DBE;
loc_003A4D84:
    goto loc_003A4DA0;
loc_003A4D8B:
    v_rbx = (unsigned int)((a3) - ((unsigned int)(a3)));
loc_003A4D91:
    if (sign_flag) goto loc_003A4D84;
loc_003A4D96:
    *(unsigned int *)(a6) = (unsigned int)(v_rbx - 1);
    result = 0;
loc_003A4DA0:
    v_rsp = (v_rsp) + (32);
    return result;
loc_003A4DBE:
    v_r15 = 0;
    if (0 < 64) goto loc_003A50DD;
loc_003A4DD0:
    a2 = (a3) + 1;
    a3 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(a3)))) >> (4);
    if (a3 == 15) goto loc_003A4F2C;
    if (a2 > (v_stack_p20 - 17)) goto loc_003A514D;
    a2 = (a2) + (a3);
    *(unsigned __int64 *)(a1) = v_xmm0;
    a1 = (a1) + (a3);
loc_003A4E04:
    v_rdi = (a1) - (*(unsigned __int16 *)(a2));
    a2 = (a2) + (2);
    a4 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a3)))) & (15));
    if (a4 == 15) goto loc_003A4E5E;
    a4 = (a4) + (4);
    if ((a4 + a1 * 1) >= (v_stack_p10 - 64)) goto loc_003A5032;
    if (v_rdi < a1) goto loc_003A4D8B;
    if ((*(unsigned __int16 *)(a2)) < 8) goto loc_003A4EB0;
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(v_rdi);
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(v_rdi + 8);
    *(unsigned __int16 *)(a1 + 16) = (unsigned __int16)(*(unsigned __int16 *)(v_rdi + 16));
    goto loc_003A4DD0;
loc_003A4E5E:
loc_003A4E65:
    a2 = (a2) + 1;
    a4 = (0) + (*(unsigned __int8 *)(a2));
    if (a2 > (v_stack_p20 - 4)) goto loc_003A4D8B;
    if ((*(unsigned __int8 *)(a2)) == 255) goto loc_003A4E65;
    if (a4 == -1) goto loc_003A4D8B;
    a4 = (a4) + (19);
    if ((a4 + a4 + a1 * 1 * 1) < (a4 + a1 * 1)) goto loc_003A4D8B;
    if ((a4 + a4 + a1 * 1 * 1) >= (v_stack_p10 - 64)) goto loc_003A5032;
    if (v_rdi < a1) goto loc_003A4D8B;
loc_003A4EB0:
    if ((*(unsigned __int16 *)(a2)) >= 16) goto loc_003A4F04;
    if ((*(unsigned __int16 *)(a2)) != 2) goto loc_003A4FC9;
    v_stack_p60 = (unsigned __int16)(*(unsigned __int16 *)(v_rdi));
    v_stack_p62 = (unsigned __int16)(*(unsigned __int16 *)(v_rdi));
loc_003A4ED5:
    v_stack_p64 = (unsigned int)((unsigned int)(v_stack_p60));
loc_003A4ED9:
    *(unsigned __int64 *)(a4 + a1 * 1) = v_stack_p60;
    a1 = (a4 + a4 + a1 * 1 * 1) - (a4 + a1 * 1 + 8);
    a1 = (a1) + (7);
    a1 = (a1) >> (3);
    if ((a4 + a1 * 1 + 8) > (a4 + a4 + a1 * 1 * 1)) { a1 = 0; }
    if (a1 == 0) goto loc_003A4F24;
    goto loc_003A4F24;
loc_003A4F04:
    *(unsigned __int64 *)(*(unsigned __int16 *)(a2) + a4 + a1 * 1 + 8 + 32 * 1 - 32) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int16 *)(a2) + a4 + a1 * 1 + 8 + 32 * 1 - 16) = v_xmm0;
    if ((*(unsigned __int16 *)(a2) + a4 + a1 * 1 + 8 + 32 * 1) < (a4 + a4 + a1 * 1 * 1)) goto loc_003A4F04;
loc_003A4F24:
    goto loc_003A4DD0;
loc_003A4F2C:
    if (a2 >= (v_stack_p20 - 15)) goto loc_003A4D8B;
loc_003A4F40:
    a2 = (a2) + 1;
    a3 = (0) + (*(unsigned __int8 *)(a2));
    if (a2 > (v_stack_p20 - 15)) goto loc_003A4D8B;
    if ((*(unsigned __int8 *)(a2)) == 255) goto loc_003A4F40;
    if (a3 == -1) goto loc_003A4D8B;
    a3 = (a3) + (15);
    if ((a3 + a4 + a4 + a1 * 1 * 1 * 1) < (a4 + a4 + a1 * 1 * 1)) goto loc_003A4D8B;
    if ((a3 + a2 * 1) < a2) goto loc_003A4D8B;
    if ((a3 + a4 + a4 + a1 * 1 * 1 * 1) > ((int)(a2) + a1 * 1 - 32)) goto loc_003A514D;
    if ((a3 + a2 * 1) > (v_stack_p20 - 32)) goto loc_003A514D;
    a1 = (a4 + a4 + a1 * 1 * 1) - (a2);
loc_003A4FA0:
    *(unsigned __int64 *)(a1 + a2 + 32 * 1 - 32) = v_xmm0;
    *(unsigned __int64 *)(a1 + a2 + 32 * 1 - 16) = v_xmm0;
    if ((a1 + a2 + 32 * 1) < (a3 + a4 + a4 + a1 * 1 * 1 * 1)) goto loc_003A4FA0;
    goto loc_003A4E04;
loc_003A4FC9:
    result = (a3) - (1);
    if (condition_is_equal) goto loc_003A52B4;
    if (result != 3) goto loc_003A5218;
    v_stack_p60 = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + a4 + a4 + a1 * 1 * 1 * 1)));
    goto loc_003A4ED5;
loc_003A4FEB:
    if ((a3 + a3 + a2 * 1 * 1) > (v_stack_p20 - 8)) goto loc_003A515E;
    a2 = (a3 + a2 * 1) - (a3 + a4 + a4 + a1 * 1 * 1 * 1);
loc_003A4FFF:
    *(unsigned __int64 *)(a3 + a4 + a4 + a1 * 1 * 1 * 1) = *(unsigned __int64 *)(a3 + a4 + a4 + a1 * 1 * 1 * 1 + a2 * 1);
    a1 = (a3 + a4 + a4 + a1 * 1 * 1 * 1) + (8);
    if (a1 < (a3 + a4 + a4 + a1 * 1 * 1 * 1)) goto loc_003A4FFF;
    v_rdi = (a3 + a4 + a4 + a1 * 1 * 1 * 1) - (*(unsigned __int16 *)(a3 + a3 + a2 * 1 * 1));
    a4 = (unsigned int)(((unsigned int)((unsigned int)(a4 + a4 + a1 * 1 * 1))) & (15));
loc_003A5024:
    if (a4 == 15) goto loc_003A51C0;
loc_003A502E:
    a4 = (a4) + (4);
loc_003A5032:
    if (v_rdi < a1) goto loc_003A4D8B;
    if ((*(unsigned __int16 *)(a3 + a3 + a2 * 1 * 1)) >= 8) goto loc_003A5184;
    *(unsigned __int8 *)(a3 + a4 + a4 + a1 * 1 * 1 * 1) = (unsigned __int8)(*(unsigned __int8 *)(v_rdi));
    *(unsigned __int8 *)(a3 + a4 + a4 + a1 * 1 * 1 * 1 + 1) = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1));
    *(unsigned __int8 *)(a3 + a4 + a4 + a1 * 1 * 1 * 1 + 2) = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 2));
    *(unsigned __int8 *)(a3 + a4 + a4 + a1 * 1 * 1 * 1 + 3) = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 3));
    v_rdi = (v_rdi) + ((unsigned int)(*(unsigned int *)(v_rip - 3821651 + *(unsigned __int16 *)(a3 + a3 + a2 * 1 * 1) * 4 + 222048)));
    *(unsigned int *)(a3 + a4 + a4 + a1 * 1 * 1 * 1 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi)));
    v_rdi = (v_rdi) - ((int)(*(unsigned int *)(v_rip - 3821651 + *(unsigned __int16 *)(a3 + a3 + a2 * 1 * 1) * 4 + 222016)));
loc_003A5085:
    a1 = (a3 + a4 + a4 + a1 * 1 * 1 * 1) + (8);
    if ((a4 + a3 + a4 + a4 + a1 * 1 * 1 * 1 * 1) <= (v_stack_p10 - 12)) goto loc_003A52F6;
    if ((a4 + a3 + a4 + a4 + a1 * 1 * 1 * 1 * 1) > (v_stack_p10 - 5)) goto loc_003A4D8B;
    if (a1 >= (v_stack_p10 - 7)) goto loc_003A50D1;
    v_r11 = (v_rdi) - (a1);
loc_003A50B5:
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(a1 + v_r11 * 1);
    a3 = (a1) + (8);
    if (a3 < (v_stack_p10 - 7)) goto loc_003A50B5;
    result = (v_stack_p10 - 7) - (a1);
    v_rdi = (v_rdi) + (result);
loc_003A50D1:
    if ((v_stack_p10 - 7) < (a4 + a3 + a4 + a4 + a1 * 1 * 1 * 1 * 1)) goto loc_003A5201;
loc_003A50DA:
loc_003A50DD:
    a2 = (a3 + a3 + a2 * 1 * 1 + 2) + 1;
    a3 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(a3 + a3 + a2 * 1 * 1 + 2)))) >> (4);
    if (a3 != 15) goto loc_003A5148;
    if (a2 >= (v_stack_p20 - 15)) goto loc_003A4D8B;
loc_003A5104:
    a2 = (a2) + 1;
    result = (0) + (*(unsigned __int8 *)(a2));
    if (a2 > (v_stack_p20 - 15)) goto loc_003A4D8B;
    if ((*(unsigned __int8 *)(a2)) == 255) goto loc_003A5104;
    if (result == -1) goto loc_003A4D8B;
    a3 = (a3) + (result);
    if ((a3 + a4 + a3 + a4 + a4 + a1 * 1 * 1 * 1 * 1 * 1) < (a4 + a3 + a4 + a4 + a1 * 1 * 1 * 1 * 1)) goto loc_003A4D8B;
    if ((a3 + a2 * 1) < a2) goto loc_003A4D8B;
    goto loc_003A514D;
loc_003A5148:
    if ((a4 + a3 + a4 + a4 + a1 * 1 * 1 * 1 * 1) <= ((int)(a2) + a1 * 1 - 32)) goto loc_003A5193;
loc_003A514D:
    if ((a3 + a4 + a3 + a4 + a4 + a1 * 1 * 1 * 1 * 1 * 1) <= (v_stack_p10 - 12)) goto loc_003A4FEB;
loc_003A515E:
    if ((a3 + a2 * 1) != v_stack_p20) goto loc_003A4D8B;
    if ((a3 + a4 + a3 + a4 + a4 + a1 * 1 * 1 * 1 * 1 * 1) > v_stack_p10) goto loc_003A4D8B;
    result = memcpy(a4 + a3 + a4 + a4 + a1 * 1 * 1 * 1 * 1, a2, a3, v_stack_p20 - 15);
    v_rdi = (unsigned int)((a3 + a4 + a3 + a4 + a4 + a1 * 1 * 1 * 1 * 1 * 1) - ((unsigned int)(a1)));
    goto loc_003A4D91;
loc_003A5184:
    v_rdi = (v_rdi) + (8);
    *(unsigned __int64 *)(a4 + a3 + a4 + a4 + a1 * 1 * 1 * 1 * 1) = *(unsigned __int64 *)(v_rdi);
    goto loc_003A5085;
loc_003A5193:
    if (a2 >= (v_rsi - 16)) goto loc_003A514D;
    a2 = (a2) + (a3);
    a4 = (unsigned int)((v_stack_p20 - 15) & (15));
    *(unsigned __int64 *)(a4 + a3 + a4 + a4 + a1 * 1 * 1 * 1 * 1) = v_xmm0;
    a1 = (a4 + a3 + a4 + a4 + a1 * 1 * 1 * 1 * 1) + (a3);
    v_rdi = (a1) - (*(unsigned __int16 *)(a2));
    a2 = (a2) + (2);
    if (a4 != 15) goto loc_003A527F;
loc_003A51C0:
loc_003A51C7:
    a2 = (a2) + 1;
    a4 = ((unsigned int)((unsigned int)(v_rdi))) + (*(unsigned __int8 *)(a2));
    if (a2 > (v_stack_p20 - 4)) goto loc_003A4D8B;
    if ((*(unsigned __int8 *)(a2)) == 255) goto loc_003A51C7;
    if (a4 == -1) goto loc_003A4D8B;
    a4 = (a4) + (15);
    if ((a4 + a1 * 1) < a1) goto loc_003A4D8B;
    goto loc_003A502E;
loc_003A5201:
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(v_rdi));
    a1 = (a1) + 1;
    if (a1 >= (v_stack_p20 - 4)) goto loc_003A50DA;
    goto loc_003A5201;
loc_003A5218:
    if ((*(unsigned __int16 *)(a2)) >= 8) goto loc_003A52DC;
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1));
    a4 = ((unsigned int)(*(unsigned int *)(v_rip - 3822127 + *(unsigned __int16 *)(a2) * 4 + 222048))) + (v_rdi + 1);
    *(unsigned __int8 *)(a1 + 1) = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1 + 1));
    *(unsigned __int8 *)(a1 + 2) = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1 + 2));
    *(unsigned __int8 *)(a1 + 3) = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1 + 3));
    *(unsigned int *)(a1 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4)));
    a4 = (a4) - ((int)(*(unsigned int *)(v_rip - 3822127 + *(unsigned __int16 *)(a2) * 4 + 222016)));
loc_003A5262:
    a1 = (a1) + (8);
    a4 = (a4) - (a1);
loc_003A5269:
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(a1 + a4 * 1);
    a1 = (a1) + (8);
    if (a1 >= (v_stack_p20 - 4)) goto loc_003A4F24;
    goto loc_003A5269;
loc_003A527F:
    if ((*(unsigned __int16 *)(a2)) < 8) goto loc_003A5024;
    if ((v_rdi + 1) < a1) goto loc_003A5024;
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(v_rdi + 1);
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(v_rdi + 1 + 8);
    *(unsigned __int16 *)(a1 + 16) = (unsigned __int16)(*(unsigned __int16 *)(v_rdi + 1 + 16));
    a1 = (a1) + (4);
    a1 = (a1) + (a4);
    goto loc_003A50DD;
loc_003A52B4:
    v_stack_p60 = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1));
    v_stack_p61 = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1));
    v_stack_p62 = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1));
    v_stack_p63 = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1));
    v_stack_p64 = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1));
    v_stack_p65 = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1));
    v_stack_p66 = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1));
    v_stack_p67 = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1));
    goto loc_003A4ED9;
loc_003A52DC:
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(v_rdi + 1);
    goto loc_003A5262;
loc_003A52EB:
    goto loc_003A4D91;
loc_003A52F6:
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(v_rdi + 1);
    if ((v_rdi + 1 + 8) <= 16) goto loc_003A50DA;
    a1 = (a1) + (8);
    v_rdi = (v_rdi + 1) - (a1);
}
```

## 5. (Beta) C Style

```c
int64_t RtlDecompressBufferLz4(int64_t Arg1, void *Arg2, void *Arg3, void *Arg4, uint64_t Arg5, void *Arg6)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r11;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint16_t v_stack_p60;
    uint8_t v_stack_p61;
    uint16_t v_stack_p62;
    uint8_t v_stack_p63;
    uint32_t v_stack_p64;
    uint8_t v_stack_p65;
    uint8_t v_stack_p66;
    uint8_t v_stack_p67;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (32);
    if (Arg3 == NULL) goto loc_003A4D84;
    if (sign_flag) goto loc_003A4D84;
    local_rsi = ((int32_t)(Arg4)) + (Arg3);
    if ((uint32_t)((int32_t)(Arg2)) != 0) goto loc_003A4D7F;
    if (Arg4 != 1) goto loc_003A52EB;
    if ((*(uint8_t *)(arg3)) != ((uint8_t)((int32_t)(Arg2)))) goto loc_003A52EB;
    local_r15 = 0;
    goto loc_003A4D96;
loc_003A4D7F:
    if (Arg4 != NULL) goto loc_003A4DBE;
loc_003A4D84:
    goto loc_003A4DA0;
loc_003A4D8B:
    local_rbx = (uint32_t)((Arg3) - ((uint32_t)(Arg3)));
loc_003A4D91:
    if (sign_flag) goto loc_003A4D84;
loc_003A4D96:
    *(uint32_t *)(arg6) = (uint32_t)(local_rbx - 1);
    result = 0;
loc_003A4DA0:
    local_rsp = (local_rsp) + (32);
    return result;
loc_003A4DBE:
    local_r15 = 0;
    if (0 < 64) goto loc_003A50DD;
loc_003A4DD0:
    Arg2 = (Arg3) + 1;
    Arg3 = ((uint32_t)((uint32_t)(*(uint8_t *)(arg3)))) >> (4);
    if (Arg3 == 15) goto loc_003A4F2C;
    if (Arg2 > (v_stack_p20 - 17)) goto loc_003A514D;
    Arg2 = (Arg2) + (Arg3);
    *(uint64_t *)(Arg1) = v_xmm0;
    Arg1 = (Arg1) + (Arg3);
loc_003A4E04:
    local_rdi = (Arg1) - (*(uint16_t *)(arg2));
    Arg2 = (Arg2) + (2);
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(arg3)))) & (15));
    if (Arg4 == 15) goto loc_003A4E5E;
    Arg4 = (Arg4) + (4);
    if ((Arg4 + Arg1 * 1) >= (v_stack_p10 - 64)) goto loc_003A5032;
    if (local_rdi < Arg1) goto loc_003A4D8B;
    if ((*(uint16_t *)(arg2)) < 8) goto loc_003A4EB0;
    *(uint64_t *)(Arg1) = *(uint64_t *)(local_rdi);
    *(uint64_t *)(Arg1 + 0x8) = *(uint64_t *)(local_rdi + 0x8);
    *(uint16_t *)(Arg1 + 0x10) = (uint16_t)(*(uint16_t *)(local_rdi + 0x10));
    goto loc_003A4DD0;
loc_003A4E5E:
loc_003A4E65:
    Arg2 = (Arg2) + 1;
    Arg4 = (0) + (*(uint8_t *)(arg2));
    if (Arg2 > (v_stack_p20 - 4)) goto loc_003A4D8B;
    if ((*(uint8_t *)(arg2)) == 255) goto loc_003A4E65;
    if (Arg4 == -1) goto loc_003A4D8B;
    Arg4 = (Arg4) + (19);
    if ((Arg4 + Arg4 + Arg1 * 1 * 1) < (Arg4 + Arg1 * 1)) goto loc_003A4D8B;
    if ((Arg4 + Arg4 + Arg1 * 1 * 1) >= (v_stack_p10 - 64)) goto loc_003A5032;
    if (local_rdi < Arg1) goto loc_003A4D8B;
loc_003A4EB0:
    if ((*(uint16_t *)(arg2)) >= 16) goto loc_003A4F04;
    if ((*(uint16_t *)(arg2)) != 2) goto loc_003A4FC9;
    v_stack_p60 = (uint16_t)(*(uint16_t *)(local_rdi));
    v_stack_p62 = (uint16_t)(*(uint16_t *)(local_rdi));
loc_003A4ED5:
    v_stack_p64 = (uint32_t)((uint32_t)(v_stack_p60));
loc_003A4ED9:
    *(uint64_t *)(arg4 + Arg1 * 1) = v_stack_p60;
    Arg1 = (Arg4 + Arg4 + Arg1 * 1 * 1) - (Arg4 + Arg1 * 1 + 8);
    Arg1 = (Arg1) + (7);
    Arg1 = (Arg1) >> (3);
    if ((Arg4 + Arg1 * 1 + 8) > (Arg4 + Arg4 + Arg1 * 1 * 1)) { Arg1 = 0; }
    if (Arg1 == 0) goto loc_003A4F24;
    goto loc_003A4F24;
loc_003A4F04:
    *(uint64_t *)(*(uint16_t *)(arg2) + arg4 + Arg1 * 1 + 0x8 + 0x20 * 1 - 0x20) = v_xmm0;
    *(uint64_t *)(*(uint16_t *)(arg2) + arg4 + Arg1 * 1 + 0x8 + 0x20 * 1 - 0x10) = v_xmm0;
    if ((*(uint16_t *)(arg2) + Arg4 + Arg1 * 1 + 8 + 32 * 1) < (Arg4 + Arg4 + Arg1 * 1 * 1)) goto loc_003A4F04;
loc_003A4F24:
    goto loc_003A4DD0;
loc_003A4F2C:
    if (Arg2 >= (v_stack_p20 - 15)) goto loc_003A4D8B;
loc_003A4F40:
    Arg2 = (Arg2) + 1;
    Arg3 = (0) + (*(uint8_t *)(arg2));
    if (Arg2 > (v_stack_p20 - 15)) goto loc_003A4D8B;
    if ((*(uint8_t *)(arg2)) == 255) goto loc_003A4F40;
    if (Arg3 == -1) goto loc_003A4D8B;
    Arg3 = (Arg3) + (15);
    if ((Arg3 + Arg4 + Arg4 + Arg1 * 1 * 1 * 1) < (Arg4 + Arg4 + Arg1 * 1 * 1)) goto loc_003A4D8B;
    if ((Arg3 + Arg2 * 1) < Arg2) goto loc_003A4D8B;
    if ((Arg3 + Arg4 + Arg4 + Arg1 * 1 * 1 * 1) > ((int32_t)(Arg2) + Arg1 * 1 - 32)) goto loc_003A514D;
    if ((Arg3 + Arg2 * 1) > (v_stack_p20 - 32)) goto loc_003A514D;
    Arg1 = (Arg4 + Arg4 + Arg1 * 1 * 1) - (Arg2);
loc_003A4FA0:
    *(uint64_t *)(Arg1 + arg2 + 0x20 * 1 - 0x20) = v_xmm0;
    *(uint64_t *)(Arg1 + arg2 + 0x20 * 1 - 0x10) = v_xmm0;
    if ((Arg1 + Arg2 + 32 * 1) < (Arg3 + Arg4 + Arg4 + Arg1 * 1 * 1 * 1)) goto loc_003A4FA0;
    goto loc_003A4E04;
loc_003A4FC9:
    result = (Arg3) - (1);
    if (condition_is_equal) goto loc_003A52B4;
    if (result != 3) goto loc_003A5218;
    v_stack_p60 = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + arg4 + arg4 + Arg1 * 1 * 1 * 1)));
    goto loc_003A4ED5;
loc_003A4FEB:
    if ((Arg3 + Arg3 + Arg2 * 1 * 1) > (v_stack_p20 - 8)) goto loc_003A515E;
    Arg2 = (Arg3 + Arg2 * 1) - (Arg3 + Arg4 + Arg4 + Arg1 * 1 * 1 * 1);
loc_003A4FFF:
    *(uint64_t *)(arg3 + arg4 + arg4 + Arg1 * 1 * 1 * 1) = *(uint64_t *)(arg3 + arg4 + arg4 + Arg1 * 1 * 1 * 1 + arg2 * 1);
    Arg1 = (Arg3 + Arg4 + Arg4 + Arg1 * 1 * 1 * 1) + (8);
    if (Arg1 < (Arg3 + Arg4 + Arg4 + Arg1 * 1 * 1 * 1)) goto loc_003A4FFF;
    local_rdi = (Arg3 + Arg4 + Arg4 + Arg1 * 1 * 1 * 1) - (*(uint16_t *)(arg3 + arg3 + arg2 * 1 * 1));
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(Arg4 + Arg4 + Arg1 * 1 * 1))) & (15));
loc_003A5024:
    if (Arg4 == 15) goto loc_003A51C0;
loc_003A502E:
    Arg4 = (Arg4) + (4);
loc_003A5032:
    if (local_rdi < Arg1) goto loc_003A4D8B;
    if ((*(uint16_t *)(arg3 + arg3 + arg2 * 1 * 1)) >= 8) goto loc_003A5184;
    *(uint8_t *)(arg3 + arg4 + arg4 + Arg1 * 1 * 1 * 1) = (uint8_t)(*(uint8_t *)(local_rdi));
    *(uint8_t *)(arg3 + arg4 + arg4 + Arg1 * 1 * 1 * 1 + 0x1) = (uint8_t)(*(uint8_t *)(local_rdi + 0x1));
    *(uint8_t *)(arg3 + arg4 + arg4 + Arg1 * 1 * 1 * 1 + 0x2) = (uint8_t)(*(uint8_t *)(local_rdi + 0x2));
    *(uint8_t *)(arg3 + arg4 + arg4 + Arg1 * 1 * 1 * 1 + 0x3) = (uint8_t)(*(uint8_t *)(local_rdi + 0x3));
    local_rdi = (local_rdi) + ((uint32_t)(*(uint32_t *)(v_rip - 0x3A5053 + *(uint16_t *)(arg3 + arg3 + arg2 * 1 * 1) * 4 + 0x36360)));
    *(uint32_t *)(arg3 + arg4 + arg4 + Arg1 * 1 * 1 * 1 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi)));
    local_rdi = (local_rdi) - ((int32_t)(*(uint32_t *)(v_rip - 0x3A5053 + *(uint16_t *)(arg3 + arg3 + arg2 * 1 * 1) * 4 + 0x36340)));
loc_003A5085:
    Arg1 = (Arg3 + Arg4 + Arg4 + Arg1 * 1 * 1 * 1) + (8);
    if ((Arg4 + Arg3 + Arg4 + Arg4 + Arg1 * 1 * 1 * 1 * 1) <= (v_stack_p10 - 12)) goto loc_003A52F6;
    if ((Arg4 + Arg3 + Arg4 + Arg4 + Arg1 * 1 * 1 * 1 * 1) > (v_stack_p10 - 5)) goto loc_003A4D8B;
    if (Arg1 >= (v_stack_p10 - 7)) goto loc_003A50D1;
    local_r11 = (local_rdi) - (Arg1);
loc_003A50B5:
    *(uint64_t *)(Arg1) = *(uint64_t *)(Arg1 + local_r11 * 1);
    Arg3 = (Arg1) + (8);
    if (Arg3 < (v_stack_p10 - 7)) goto loc_003A50B5;
    result = (v_stack_p10 - 7) - (Arg1);
    local_rdi = (local_rdi) + (result);
loc_003A50D1:
    if ((v_stack_p10 - 7) < (Arg4 + Arg3 + Arg4 + Arg4 + Arg1 * 1 * 1 * 1 * 1)) goto loc_003A5201;
loc_003A50DA:
loc_003A50DD:
    Arg2 = (Arg3 + Arg3 + Arg2 * 1 * 1 + 2) + 1;
    Arg3 = ((uint32_t)((uint32_t)(*(uint8_t *)(arg3 + arg3 + arg2 * 1 * 1 + 0x2)))) >> (4);
    if (Arg3 != 15) goto loc_003A5148;
    if (Arg2 >= (v_stack_p20 - 15)) goto loc_003A4D8B;
loc_003A5104:
    Arg2 = (Arg2) + 1;
    result = (0) + (*(uint8_t *)(arg2));
    if (Arg2 > (v_stack_p20 - 15)) goto loc_003A4D8B;
    if ((*(uint8_t *)(arg2)) == 255) goto loc_003A5104;
    if (result == -1) goto loc_003A4D8B;
    Arg3 = (Arg3) + (result);
    if ((Arg3 + Arg4 + Arg3 + Arg4 + Arg4 + Arg1 * 1 * 1 * 1 * 1 * 1) < (Arg4 + Arg3 + Arg4 + Arg4 + Arg1 * 1 * 1 * 1 * 1)) goto loc_003A4D8B;
    if ((Arg3 + Arg2 * 1) < Arg2) goto loc_003A4D8B;
    goto loc_003A514D;
loc_003A5148:
    if ((Arg4 + Arg3 + Arg4 + Arg4 + Arg1 * 1 * 1 * 1 * 1) <= ((int32_t)(Arg2) + Arg1 * 1 - 32)) goto loc_003A5193;
loc_003A514D:
    if ((Arg3 + Arg4 + Arg3 + Arg4 + Arg4 + Arg1 * 1 * 1 * 1 * 1 * 1) <= (v_stack_p10 - 12)) goto loc_003A4FEB;
loc_003A515E:
    if ((Arg3 + Arg2 * 1) != v_stack_p20) goto loc_003A4D8B;
    if ((Arg3 + Arg4 + Arg3 + Arg4 + Arg4 + Arg1 * 1 * 1 * 1 * 1 * 1) > v_stack_p10) goto loc_003A4D8B;
    result = memcpy(Arg4 + Arg3 + Arg4 + Arg4 + Arg1 * 1 * 1 * 1 * 1, Arg2, Arg3, v_stack_p20 - 15);
    local_rdi = (uint32_t)((Arg3 + Arg4 + Arg3 + Arg4 + Arg4 + Arg1 * 1 * 1 * 1 * 1 * 1) - ((uint32_t)(Arg1)));
    goto loc_003A4D91;
loc_003A5184:
    local_rdi = (local_rdi) + (8);
    *(uint64_t *)(arg4 + arg3 + arg4 + arg4 + Arg1 * 1 * 1 * 1 * 1) = *(uint64_t *)(local_rdi);
    goto loc_003A5085;
loc_003A5193:
    if (Arg2 >= (local_rsi - 16)) goto loc_003A514D;
    Arg2 = (Arg2) + (Arg3);
    Arg4 = (uint32_t)((v_stack_p20 - 15) & (15));
    *(uint64_t *)(arg4 + arg3 + arg4 + arg4 + Arg1 * 1 * 1 * 1 * 1) = v_xmm0;
    Arg1 = (Arg4 + Arg3 + Arg4 + Arg4 + Arg1 * 1 * 1 * 1 * 1) + (Arg3);
    local_rdi = (Arg1) - (*(uint16_t *)(arg2));
    Arg2 = (Arg2) + (2);
    if (Arg4 != 15) goto loc_003A527F;
loc_003A51C0:
loc_003A51C7:
    Arg2 = (Arg2) + 1;
    Arg4 = ((uint32_t)((uint32_t)(local_rdi))) + (*(uint8_t *)(arg2));
    if (Arg2 > (v_stack_p20 - 4)) goto loc_003A4D8B;
    if ((*(uint8_t *)(arg2)) == 255) goto loc_003A51C7;
    if (Arg4 == -1) goto loc_003A4D8B;
    Arg4 = (Arg4) + (15);
    if ((Arg4 + Arg1 * 1) < Arg1) goto loc_003A4D8B;
    goto loc_003A502E;
loc_003A5201:
    *(uint8_t *)(Arg1) = (uint8_t)(*(uint8_t *)(local_rdi));
    Arg1 = (Arg1) + 1;
    if (Arg1 >= (v_stack_p20 - 4)) goto loc_003A50DA;
    goto loc_003A5201;
loc_003A5218:
    if ((*(uint16_t *)(arg2)) >= 8) goto loc_003A52DC;
    *(uint8_t *)(Arg1) = (uint8_t)(*(uint8_t *)(local_rdi + 0x1));
    Arg4 = ((uint32_t)(*(uint32_t *)(v_rip - 0x3A522F + *(uint16_t *)(arg2) * 4 + 0x36360))) + (local_rdi + 1);
    *(uint8_t *)(Arg1 + 0x1) = (uint8_t)(*(uint8_t *)(local_rdi + 0x1 + 0x1));
    *(uint8_t *)(Arg1 + 0x2) = (uint8_t)(*(uint8_t *)(local_rdi + 0x1 + 0x2));
    *(uint8_t *)(Arg1 + 0x3) = (uint8_t)(*(uint8_t *)(local_rdi + 0x1 + 0x3));
    *(uint32_t *)(Arg1 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg4)));
    Arg4 = (Arg4) - ((int32_t)(*(uint32_t *)(v_rip - 0x3A522F + *(uint16_t *)(arg2) * 4 + 0x36340)));
loc_003A5262:
    Arg1 = (Arg1) + (8);
    Arg4 = (Arg4) - (Arg1);
loc_003A5269:
    *(uint64_t *)(Arg1) = *(uint64_t *)(Arg1 + arg4 * 1);
    Arg1 = (Arg1) + (8);
    if (Arg1 >= (v_stack_p20 - 4)) goto loc_003A4F24;
    goto loc_003A5269;
loc_003A527F:
    if ((*(uint16_t *)(arg2)) < 8) goto loc_003A5024;
    if ((local_rdi + 1) < Arg1) goto loc_003A5024;
    *(uint64_t *)(Arg1) = *(uint64_t *)(local_rdi + 0x1);
    *(uint64_t *)(Arg1 + 0x8) = *(uint64_t *)(local_rdi + 0x1 + 0x8);
    *(uint16_t *)(Arg1 + 0x10) = (uint16_t)(*(uint16_t *)(local_rdi + 0x1 + 0x10));
    Arg1 = (Arg1) + (4);
    Arg1 = (Arg1) + (Arg4);
    goto loc_003A50DD;
loc_003A52B4:
    v_stack_p60 = (uint8_t)(*(uint8_t *)(local_rdi + 0x1));
    v_stack_p61 = (uint8_t)(*(uint8_t *)(local_rdi + 0x1));
    v_stack_p62 = (uint8_t)(*(uint8_t *)(local_rdi + 0x1));
    v_stack_p63 = (uint8_t)(*(uint8_t *)(local_rdi + 0x1));
    v_stack_p64 = (uint8_t)(*(uint8_t *)(local_rdi + 0x1));
    v_stack_p65 = (uint8_t)(*(uint8_t *)(local_rdi + 0x1));
    v_stack_p66 = (uint8_t)(*(uint8_t *)(local_rdi + 0x1));
    v_stack_p67 = (uint8_t)(*(uint8_t *)(local_rdi + 0x1));
    goto loc_003A4ED9;
loc_003A52DC:
    *(uint64_t *)(Arg1) = *(uint64_t *)(local_rdi + 0x1);
    goto loc_003A5262;
loc_003A52EB:
    goto loc_003A4D91;
loc_003A52F6:
    *(uint64_t *)(Arg1) = *(uint64_t *)(local_rdi + 0x1);
    if ((local_rdi + 1 + 8) <= 16) goto loc_003A50DA;
    Arg1 = (Arg1) + (8);
    local_rdi = (local_rdi + 1) - (Arg1);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `- 0x40` | `64` | `R` |
| `Arg2` | `- 0x20` | `64` | `R` |
| `Arg2` | `- 0xC` | `64` | `R` |
| `Arg2` | `- 0x7` | `64` | `R` |
| `Arg2` | `- 0x5` | `64` | `R` |
| `Arg2` | `+ 0x0 + rcx*1` | `64` | `R` |
| `Arg3` | `- 0x1` | `32` | `R` |
| `Arg4` | `- 0x20` | `64` | `R` |
| `Arg4` | `- 0x11` | `64` | `R` |
| `Arg4` | `- 0x10` | `64` | `R` |
| `Arg4` | `- 0xF` | `64` | `R` |
| `Arg4` | `- 0x8` | `64` | `R` |
| `Arg4` | `- 0x4` | `64` | `R` |
| `Arg4` | `+ 0x0 + rax*1` | `32` | `R` |
| `Arg6` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003A4D20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
