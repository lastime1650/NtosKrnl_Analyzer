# do_decode

- RVA: `0x006A8ADC`–`0x006A8EDD` (길이 `1,025` bytes)
- VA: `0x00000001406A8ADC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A5A38`
- 디코드: `297`개 명령, `1,025/1,025` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [XpressDecode](XpressDecode_function_006A8960.md) at `0x006A8A48`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006A8ADC  48 8B C4                        mov rax, rsp
006A8ADF  48 89 58 08                     mov qword ptr [rax + 8], rbx
006A8AE3  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
006A8AE7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006A8AEB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
006A8AEF  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
006A8AF3  33 ED                           xor ebp, ebp
006A8AF5  4C 8B 41 30                     mov r8, qword ptr [rcx + 0x30]
006A8AF9  4C 8B C9                        mov r9, rcx
006A8AFC  44 8D 55 01                     lea r10d, [rbp + 1]
006A8B00  4D 3B 41 38                     cmp r8, qword ptr [r9 + 0x38]
006A8B04  0F 83 9C 01 00 00               jae 0x1406a8ca6
006A8B0A  49 3B 51 10                     cmp rdx, qword ptr [r9 + 0x10]
006A8B0E  0F 83 92 01 00 00               jae 0x1406a8ca6
006A8B14  41 8B 00                        mov eax, dword ptr [r8]
006A8B17  49 83 C0 04                     add r8, 4
006A8B1B  44 8D 1C 45 01 00 00 00         lea r11d, [rax*2 + 1]
006A8B23  85 C0                           test eax, eax
006A8B25  0F 89 54 01 00 00               jns 0x1406a8c7f
006A8B2B  41 0F B7 00                     movzx eax, word ptr [r8]
006A8B2F  49 83 C0 02                     add r8, 2
006A8B33  8B C8                           mov ecx, eax
006A8B35  C1 E8 03                        shr eax, 3
006A8B38  83 E1 07                        and ecx, 7
006A8B3B  F7 D0                           not eax
006A8B3D  83 F9 05                        cmp ecx, 5
006A8B40  77 49                           ja 0x1406a8b8b
006A8B42  48 63 D8                        movsxd rbx, eax
006A8B45  48 03 DA                        add rbx, rdx
006A8B48  49 3B 59 08                     cmp rbx, qword ptr [r9 + 8]
006A8B4C  0F 82 6E 03 00 00               jb 0x1406a8ec0
006A8B52  8A 03                           mov al, byte ptr [rbx]
006A8B54  83 C1 03                        add ecx, 3
006A8B57  88 02                           mov byte ptr [rdx], al
006A8B59  8A 43 01                        mov al, byte ptr [rbx + 1]
006A8B5C  88 42 01                        mov byte ptr [rdx + 1], al
006A8B5F  8A 43 02                        mov al, byte ptr [rbx + 2]
006A8B62  88 42 02                        mov byte ptr [rdx + 2], al
006A8B65  8A 43 03                        mov al, byte ptr [rbx + 3]
006A8B68  88 42 03                        mov byte ptr [rdx + 3], al
006A8B6B  8A 43 04                        mov al, byte ptr [rbx + 4]
006A8B6E  88 42 04                        mov byte ptr [rdx + 4], al
006A8B71  8A 43 05                        mov al, byte ptr [rbx + 5]
006A8B74  88 42 05                        mov byte ptr [rdx + 5], al
006A8B77  8A 43 06                        mov al, byte ptr [rbx + 6]
006A8B7A  88 42 06                        mov byte ptr [rdx + 6], al
006A8B7D  8A 43 07                        mov al, byte ptr [rbx + 7]
006A8B80  88 42 07                        mov byte ptr [rdx + 7], al
006A8B83  48 03 D1                        add rdx, rcx
006A8B86  E9 FF 00 00 00                  jmp 0x1406a8c8a
006A8B8B  83 F9 07                        cmp ecx, 7
006A8B8E  75 4D                           jne 0x1406a8bdd
006A8B90  48 85 ED                        test rbp, rbp
006A8B93  75 0F                           jne 0x1406a8ba4
006A8B95  41 0F B6 08                     movzx ecx, byte ptr [r8]
006A8B99  49 8B E8                        mov rbp, r8
006A8B9C  83 E1 0F                        and ecx, 0xf
006A8B9F  4D 03 C2                        add r8, r10
006A8BA2  EB 09                           jmp 0x1406a8bad
006A8BA4  0F B6 4D 00                     movzx ecx, byte ptr [rbp]
006A8BA8  C1 E9 04                        shr ecx, 4
006A8BAB  33 ED                           xor ebp, ebp
006A8BAD  83 F9 0F                        cmp ecx, 0xf
006A8BB0  0F 85 BE 00 00 00               jne 0x1406a8c74
006A8BB6  41 0F B6 08                     movzx ecx, byte ptr [r8]
006A8BBA  4D 03 C2                        add r8, r10
006A8BBD  81 F9 FF 00 00 00               cmp ecx, 0xff
006A8BC3  0F 85 A8 00 00 00               jne 0x1406a8c71
006A8BC9  41 0F B7 08                     movzx ecx, word ptr [r8]
006A8BCD  49 83 C0 02                     add r8, 2
006A8BD1  81 F9 15 01 00 00               cmp ecx, 0x115
006A8BD7  0F 82 E3 02 00 00               jb 0x1406a8ec0
006A8BDD  83 C1 03                        add ecx, 3
006A8BE0  4D 89 41 58                     mov qword ptr [r9 + 0x58], r8
006A8BE4  4C 63 C0                        movsxd r8, eax
006A8BE7  8B C1                           mov eax, ecx
006A8BE9  4C 03 C2                        add r8, rdx
006A8BEC  48 03 C2                        add rax, rdx
006A8BEF  49 3B 41 10                     cmp rax, qword ptr [r9 + 0x10]
006A8BF3  0F 83 A4 00 00 00               jae 0x1406a8c9d
006A8BF9  4D 3B 41 08                     cmp r8, qword ptr [r9 + 8]
006A8BFD  0F 82 BD 02 00 00               jb 0x1406a8ec0
006A8C03  83 F9 08                        cmp ecx, 8
006A8C06  76 52                           jbe 0x1406a8c5a
006A8C08  8D 41 F7                        lea eax, [rcx - 9]
006A8C0B  C1 E8 03                        shr eax, 3
006A8C0E  FF C0                           inc eax
006A8C10  8B D8                           mov ebx, eax
006A8C12  F7 D8                           neg eax
006A8C14  8D 0C C1                        lea ecx, [rcx + rax*8]
006A8C17  41 8A 00                        mov al, byte ptr [r8]
006A8C1A  88 02                           mov byte ptr [rdx], al
006A8C1C  41 8A 40 01                     mov al, byte ptr [r8 + 1]
006A8C20  88 42 01                        mov byte ptr [rdx + 1], al
006A8C23  41 8A 40 02                     mov al, byte ptr [r8 + 2]
006A8C27  88 42 02                        mov byte ptr [rdx + 2], al
006A8C2A  41 8A 40 03                     mov al, byte ptr [r8 + 3]
006A8C2E  88 42 03                        mov byte ptr [rdx + 3], al
006A8C31  41 8A 40 04                     mov al, byte ptr [r8 + 4]
006A8C35  88 42 04                        mov byte ptr [rdx + 4], al
006A8C38  41 8A 40 05                     mov al, byte ptr [r8 + 5]
006A8C3C  88 42 05                        mov byte ptr [rdx + 5], al
006A8C3F  41 8A 40 06                     mov al, byte ptr [r8 + 6]
006A8C43  88 42 06                        mov byte ptr [rdx + 6], al
006A8C46  41 8A 40 07                     mov al, byte ptr [r8 + 7]
006A8C4A  49 83 C0 08                     add r8, 8
006A8C4E  88 42 07                        mov byte ptr [rdx + 7], al
006A8C51  48 83 C2 08                     add rdx, 8
006A8C55  49 2B DA                        sub rbx, r10
006A8C58  75 BD                           jne 0x1406a8c17
006A8C5A  4C 2B C2                        sub r8, rdx
006A8C5D  41 8A 04 10                     mov al, byte ptr [r8 + rdx]
006A8C61  88 02                           mov byte ptr [rdx], al
006A8C63  49 03 D2                        add rdx, r10
006A8C66  41 2B CA                        sub ecx, r10d
006A8C69  75 F2                           jne 0x1406a8c5d
006A8C6B  4D 8B 41 58                     mov r8, qword ptr [r9 + 0x58]
006A8C6F  EB 19                           jmp 0x1406a8c8a
006A8C71  83 C1 0F                        add ecx, 0xf
006A8C74  83 C1 0A                        add ecx, 0xa
006A8C77  E9 64 FF FF FF                  jmp 0x1406a8be0
006A8C7C  45 03 DB                        add r11d, r11d
006A8C7F  41 8A 00                        mov al, byte ptr [r8]
006A8C82  88 02                           mov byte ptr [rdx], al
006A8C84  49 03 D2                        add rdx, r10
006A8C87  4D 03 C2                        add r8, r10
006A8C8A  45 85 DB                        test r11d, r11d
006A8C8D  79 ED                           jns 0x1406a8c7c
006A8C8F  45 03 DB                        add r11d, r11d
006A8C92  0F 85 93 FE FF FF               jne 0x1406a8b2b
006A8C98  E9 63 FE FF FF                  jmp 0x1406a8b00
006A8C9D  49 8D 79 18                     lea rdi, [r9 + 0x18]
006A8CA1  E9 C9 00 00 00                  jmp 0x1406a8d6f
006A8CA6  4D 3B 41 48                     cmp r8, qword ptr [r9 + 0x48]
006A8CAA  0F 83 10 02 00 00               jae 0x1406a8ec0
006A8CB0  41 8B 00                        mov eax, dword ptr [r8]
006A8CB3  49 83 C0 04                     add r8, 4
006A8CB7  44 8D 1C 45 01 00 00 00         lea r11d, [rax*2 + 1]
006A8CBF  85 C0                           test eax, eax
006A8CC1  0F 89 3F 01 00 00               jns 0x1406a8e06
006A8CC7  49 8D 79 18                     lea rdi, [r9 + 0x18]
006A8CCB  48 3B 17                        cmp rdx, qword ptr [rdi]
006A8CCE  0F 83 D9 01 00 00               jae 0x1406a8ead
006A8CD4  49 8B 59 40                     mov rbx, qword ptr [r9 + 0x40]
006A8CD8  4C 3B C3                        cmp r8, rbx
006A8CDB  0F 83 DF 01 00 00               jae 0x1406a8ec0
006A8CE1  41 0F B7 00                     movzx eax, word ptr [r8]
006A8CE5  49 83 C0 02                     add r8, 2
006A8CE9  8B C8                           mov ecx, eax
006A8CEB  C1 E8 03                        shr eax, 3
006A8CEE  83 E1 07                        and ecx, 7
006A8CF1  F7 D0                           not eax
006A8CF3  83 F9 07                        cmp ecx, 7
006A8CF6  75 6A                           jne 0x1406a8d62
006A8CF8  48 85 ED                        test rbp, rbp
006A8CFB  75 19                           jne 0x1406a8d16
006A8CFD  4D 3B 41 28                     cmp r8, qword ptr [r9 + 0x28]
006A8D01  0F 83 B9 01 00 00               jae 0x1406a8ec0
006A8D07  41 0F B6 08                     movzx ecx, byte ptr [r8]
006A8D0B  49 8B E8                        mov rbp, r8
006A8D0E  83 E1 0F                        and ecx, 0xf
006A8D11  4D 03 C2                        add r8, r10
006A8D14  EB 09                           jmp 0x1406a8d1f
006A8D16  0F B6 4D 00                     movzx ecx, byte ptr [rbp]
006A8D1A  C1 E9 04                        shr ecx, 4
006A8D1D  33 ED                           xor ebp, ebp
006A8D1F  83 F9 0F                        cmp ecx, 0xf
006A8D22  0F 85 D3 00 00 00               jne 0x1406a8dfb
006A8D28  4D 3B 41 28                     cmp r8, qword ptr [r9 + 0x28]
006A8D2C  0F 83 8E 01 00 00               jae 0x1406a8ec0
006A8D32  41 0F B6 08                     movzx ecx, byte ptr [r8]
006A8D36  4D 03 C2                        add r8, r10
006A8D39  81 F9 FF 00 00 00               cmp ecx, 0xff
006A8D3F  0F 85 B3 00 00 00               jne 0x1406a8df8
006A8D45  4C 3B C3                        cmp r8, rbx
006A8D48  0F 83 72 01 00 00               jae 0x1406a8ec0
006A8D4E  41 0F B7 08                     movzx ecx, word ptr [r8]
006A8D52  49 83 C0 02                     add r8, 2
006A8D56  81 F9 15 01 00 00               cmp ecx, 0x115
006A8D5C  0F 82 5E 01 00 00               jb 0x1406a8ec0
006A8D62  83 C1 03                        add ecx, 3
006A8D65  4D 89 41 58                     mov qword ptr [r9 + 0x58], r8
006A8D69  4C 63 C0                        movsxd r8, eax
006A8D6C  4C 03 C2                        add r8, rdx
006A8D6F  48 8B 37                        mov rsi, qword ptr [rdi]
006A8D72  48 63 C1                        movsxd rax, ecx
006A8D75  48 03 C2                        add rax, rdx
006A8D78  4D 3B 41 08                     cmp r8, qword ptr [r9 + 8]
006A8D7C  0F 82 3E 01 00 00               jb 0x1406a8ec0
006A8D82  48 3B C6                        cmp rax, rsi
006A8D85  0F 87 B0 00 00 00               ja 0x1406a8e3b
006A8D8B  83 F9 08                        cmp ecx, 8
006A8D8E  76 52                           jbe 0x1406a8de2
006A8D90  8D 41 F7                        lea eax, [rcx - 9]
006A8D93  C1 E8 03                        shr eax, 3
006A8D96  FF C0                           inc eax
006A8D98  8B D8                           mov ebx, eax
006A8D9A  F7 D8                           neg eax
006A8D9C  8D 0C C1                        lea ecx, [rcx + rax*8]
006A8D9F  41 8A 00                        mov al, byte ptr [r8]
006A8DA2  88 02                           mov byte ptr [rdx], al
006A8DA4  41 8A 40 01                     mov al, byte ptr [r8 + 1]
006A8DA8  88 42 01                        mov byte ptr [rdx + 1], al
006A8DAB  41 8A 40 02                     mov al, byte ptr [r8 + 2]
006A8DAF  88 42 02                        mov byte ptr [rdx + 2], al
006A8DB2  41 8A 40 03                     mov al, byte ptr [r8 + 3]
006A8DB6  88 42 03                        mov byte ptr [rdx + 3], al
006A8DB9  41 8A 40 04                     mov al, byte ptr [r8 + 4]
006A8DBD  88 42 04                        mov byte ptr [rdx + 4], al
006A8DC0  41 8A 40 05                     mov al, byte ptr [r8 + 5]
006A8DC4  88 42 05                        mov byte ptr [rdx + 5], al
006A8DC7  41 8A 40 06                     mov al, byte ptr [r8 + 6]
006A8DCB  88 42 06                        mov byte ptr [rdx + 6], al
006A8DCE  41 8A 40 07                     mov al, byte ptr [r8 + 7]
006A8DD2  49 83 C0 08                     add r8, 8
006A8DD6  88 42 07                        mov byte ptr [rdx + 7], al
006A8DD9  48 83 C2 08                     add rdx, 8
006A8DDD  49 2B DA                        sub rbx, r10
006A8DE0  75 BD                           jne 0x1406a8d9f
006A8DE2  41 8A 00                        mov al, byte ptr [r8]
006A8DE5  4D 03 C2                        add r8, r10
006A8DE8  88 02                           mov byte ptr [rdx], al
006A8DEA  49 03 D2                        add rdx, r10
006A8DED  41 2B CA                        sub ecx, r10d
006A8DF0  75 F0                           jne 0x1406a8de2
006A8DF2  4D 8B 41 58                     mov r8, qword ptr [r9 + 0x58]
006A8DF6  EB 30                           jmp 0x1406a8e28
006A8DF8  83 C1 0F                        add ecx, 0xf
006A8DFB  83 C1 0A                        add ecx, 0xa
006A8DFE  E9 62 FF FF FF                  jmp 0x1406a8d65
006A8E03  45 03 DB                        add r11d, r11d
006A8E06  49 8D 79 18                     lea rdi, [r9 + 0x18]
006A8E0A  48 3B 17                        cmp rdx, qword ptr [rdi]
006A8E0D  0F 83 A3 00 00 00               jae 0x1406a8eb6
006A8E13  4D 3B 41 28                     cmp r8, qword ptr [r9 + 0x28]
006A8E17  0F 83 A3 00 00 00               jae 0x1406a8ec0
006A8E1D  41 8A 00                        mov al, byte ptr [r8]
006A8E20  88 02                           mov byte ptr [rdx], al
006A8E22  49 03 D2                        add rdx, r10
006A8E25  4D 03 C2                        add r8, r10
006A8E28  45 85 DB                        test r11d, r11d
006A8E2B  79 D6                           jns 0x1406a8e03
006A8E2D  45 03 DB                        add r11d, r11d
006A8E30  0F 85 95 FE FF FF               jne 0x1406a8ccb
006A8E36  E9 6B FE FF FF                  jmp 0x1406a8ca6
006A8E3B  8B 0F                           mov ecx, dword ptr [rdi]
006A8E3D  2B CA                           sub ecx, edx
006A8E3F  83 F9 08                        cmp ecx, 8
006A8E42  7E 53                           jle 0x1406a8e97
006A8E44  8D 41 F7                        lea eax, [rcx - 9]
006A8E47  C1 E8 03                        shr eax, 3
006A8E4A  FF C0                           inc eax
006A8E4C  44 8B D8                        mov r11d, eax
006A8E4F  F7 D8                           neg eax
006A8E51  8D 0C C1                        lea ecx, [rcx + rax*8]
006A8E54  41 8A 00                        mov al, byte ptr [r8]
006A8E57  88 02                           mov byte ptr [rdx], al
006A8E59  41 8A 40 01                     mov al, byte ptr [r8 + 1]
006A8E5D  88 42 01                        mov byte ptr [rdx + 1], al
006A8E60  41 8A 40 02                     mov al, byte ptr [r8 + 2]
006A8E64  88 42 02                        mov byte ptr [rdx + 2], al
006A8E67  41 8A 40 03                     mov al, byte ptr [r8 + 3]
006A8E6B  88 42 03                        mov byte ptr [rdx + 3], al
006A8E6E  41 8A 40 04                     mov al, byte ptr [r8 + 4]
006A8E72  88 42 04                        mov byte ptr [rdx + 4], al
006A8E75  41 8A 40 05                     mov al, byte ptr [r8 + 5]
006A8E79  88 42 05                        mov byte ptr [rdx + 5], al
006A8E7C  41 8A 40 06                     mov al, byte ptr [r8 + 6]
006A8E80  88 42 06                        mov byte ptr [rdx + 6], al
006A8E83  41 8A 40 07                     mov al, byte ptr [r8 + 7]
006A8E87  49 83 C0 08                     add r8, 8
006A8E8B  88 42 07                        mov byte ptr [rdx + 7], al
006A8E8E  48 83 C2 08                     add rdx, 8
006A8E92  4D 2B DA                        sub r11, r10
006A8E95  75 BD                           jne 0x1406a8e54
006A8E97  41 8A 00                        mov al, byte ptr [r8]
006A8E9A  4D 03 C2                        add r8, r10
006A8E9D  88 02                           mov byte ptr [rdx], al
006A8E9F  49 03 D2                        add rdx, r10
006A8EA2  41 2B CA                        sub ecx, r10d
006A8EA5  75 F0                           jne 0x1406a8e97
006A8EA7  4D 8B 41 58                     mov r8, qword ptr [r9 + 0x58]
006A8EAB  EB 09                           jmp 0x1406a8eb6
006A8EAD  49 3B 11                        cmp rdx, qword ptr [r9]
006A8EB0  75 04                           jne 0x1406a8eb6
006A8EB2  45 89 51 64                     mov dword ptr [r9 + 0x64], r10d
006A8EB6  4D 89 41 58                     mov qword ptr [r9 + 0x58], r8
006A8EBA  49 89 51 20                     mov qword ptr [r9 + 0x20], rdx
006A8EBE  EB 03                           jmp 0x1406a8ec3
006A8EC0  45 33 D2                        xor r10d, r10d
006A8EC3  45 89 51 60                     mov dword ptr [r9 + 0x60], r10d
006A8EC7  48 8B 5C 24 08                  mov rbx, qword ptr [rsp + 8]
006A8ECC  48 8B 6C 24 10                  mov rbp, qword ptr [rsp + 0x10]
006A8ED1  48 8B 74 24 18                  mov rsi, qword ptr [rsp + 0x18]
006A8ED6  48 8B 7C 24 20                  mov rdi, qword ptr [rsp + 0x20]
006A8EDB  C3                              ret
006A8EDC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall do_decode(__int64 a1)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_rbp;
    __int64 v_rbx;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rbp = 0;
loc_006A8B00:
    if ((*(unsigned __int64 *)(a1 + 48)) >= (*(unsigned __int64 *)(a1 + 56))) goto loc_006A8CA6;
    if ((*(unsigned __int64 *)(a1 + 8)) >= (*(unsigned __int64 *)(a1 + 16))) goto loc_006A8CA6;
    a3 = (*(unsigned __int64 *)(a1 + 48)) + (4);
    if (!sign_flag) goto loc_006A8C7F;
loc_006A8B2B:
    a3 = (a3) + (2);
    result = (unsigned int)((*(unsigned __int16 *)(a3)) >> (3));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(a3)))) & (7));
    result = (unsigned int)(~(result));
    if (((unsigned int)(a1)) > 5) goto loc_006A8B8B;
    v_rbx = ((int)((unsigned int)(result))) + (*(unsigned __int64 *)(a1 + 8));
    if (v_rbx < (*(unsigned __int64 *)(a1 + 8))) goto loc_006A8EC0;
    a1 = (unsigned int)((a1) + (3));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8)) = (unsigned __int8)(*(unsigned __int8 *)(v_rbx));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 1) = (unsigned __int8)(*(unsigned __int8 *)(v_rbx + 1));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 2) = (unsigned __int8)(*(unsigned __int8 *)(v_rbx + 2));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 3) = (unsigned __int8)(*(unsigned __int8 *)(v_rbx + 3));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 4) = (unsigned __int8)(*(unsigned __int8 *)(v_rbx + 4));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 5) = (unsigned __int8)(*(unsigned __int8 *)(v_rbx + 5));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 6) = (unsigned __int8)(*(unsigned __int8 *)(v_rbx + 6));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 7) = (unsigned __int8)(*(unsigned __int8 *)(v_rbx + 7));
    a2 = (*(unsigned __int64 *)(a1 + 8)) + (a1);
    goto loc_006A8C8A;
loc_006A8B8B:
    if (((unsigned int)(a1)) != 7) goto loc_006A8BDD;
    if (0 != 0) goto loc_006A8BA4;
    a1 = (unsigned int)((*(unsigned __int8 *)(a3)) & (15));
    a3 = (a3) + (v_rbp + 1);
    goto loc_006A8BAD;
loc_006A8BA4:
    a1 = (unsigned int)((*(unsigned __int8 *)(a3)) >> (4));
    v_rbp = 0;
loc_006A8BAD:
    if (((unsigned int)(a1)) != 15) goto loc_006A8C74;
    a3 = (a3) + (v_rbp + 1);
    if (((unsigned int)(*(unsigned __int8 *)(a3))) != 255) goto loc_006A8C71;
    a3 = (a3) + (2);
    if (((unsigned int)(*(unsigned __int16 *)(a3))) < 277) goto loc_006A8EC0;
loc_006A8BDD:
    a1 = (unsigned int)((*(unsigned __int16 *)(a3)) + (3));
loc_006A8BE0:
    *(unsigned __int64 *)(a1 + 88) = a3;
    a3 = ((int)((unsigned int)(*(unsigned __int8 *)(v_rbx + 7)))) + (a2);
    result = ((unsigned int)((unsigned int)(a1))) + (a2);
    if (result >= (*(unsigned __int64 *)(a1 + 16))) goto loc_006A8C9D;
    if (a3 < (*(unsigned __int64 *)(a1 + 8))) goto loc_006A8EC0;
    if (((unsigned int)(a1)) <= 8) goto loc_006A8C5A;
    result = (unsigned int)((a1 - 9) >> (3));
    result = (unsigned int)((result) + 1);
    result = (unsigned int)(-(result));
loc_006A8C17:
    *(unsigned __int8 *)(a2) = (unsigned __int8)(*(unsigned __int8 *)(a3));
    *(unsigned __int8 *)(a2 + 1) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 1));
    *(unsigned __int8 *)(a2 + 2) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 2));
    *(unsigned __int8 *)(a2 + 3) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 3));
    *(unsigned __int8 *)(a2 + 4) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 4));
    *(unsigned __int8 *)(a2 + 5) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 5));
    *(unsigned __int8 *)(a2 + 6) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 6));
    a3 = (a3) + (8);
    *(unsigned __int8 *)(a2 + 7) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 7));
    a2 = (a2) + (8);
    v_rbx = ((unsigned int)((unsigned int)(result))) - (v_rbp + 1);
    if (condition_is_not_equal) goto loc_006A8C17;
loc_006A8C5A:
    a3 = (a3) - (a2);
loc_006A8C5D:
    *(unsigned __int8 *)(a2) = (unsigned __int8)(*(unsigned __int8 *)(a3 + a2 * 1));
    a2 = (a2) + (v_rbp + 1);
    a1 = (unsigned int)((a1 + result * 8) - ((unsigned int)(v_rbp + 1)));
    if (condition_is_not_equal) goto loc_006A8C5D;
    goto loc_006A8C8A;
loc_006A8C71:
    a1 = (unsigned int)((a1) + (15));
loc_006A8C74:
    a1 = (unsigned int)((a1) + (10));
    goto loc_006A8BE0;
loc_006A8C7C:
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 48))) * 2 + 1) + ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 48))) * 2 + 1)));
loc_006A8C7F:
    *(unsigned __int8 *)(a2) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 88)));
    a2 = (a2) + (v_rbp + 1);
    a3 = (*(unsigned __int64 *)(a1 + 88)) + (v_rbp + 1);
loc_006A8C8A:
    if (!sign_flag) goto loc_006A8C7C;
    v_r11 = (unsigned int)((v_r11) + ((unsigned int)(v_r11)));
    if (condition_is_not_equal) goto loc_006A8B2B;
    goto loc_006A8B00;
loc_006A8C9D:
    goto loc_006A8D6F;
loc_006A8CA6:
    if (a3 >= (*(unsigned __int64 *)(a1 + 72))) goto loc_006A8EC0;
    a3 = (a3) + (4);
    if (!sign_flag) goto loc_006A8E06;
loc_006A8CCB:
    if (a2 >= (*(unsigned __int64 *)(a1 + 24))) goto loc_006A8EAD;
    if (a3 >= (*(unsigned __int64 *)(a1 + 64))) goto loc_006A8EC0;
    a3 = (a3) + (2);
    result = (unsigned int)((*(unsigned __int16 *)(a3)) >> (3));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(a3)))) & (7));
    result = (unsigned int)(~(result));
    if (((unsigned int)(a1)) != 7) goto loc_006A8D62;
    if (0 != 0) goto loc_006A8D16;
    if (a3 >= (*(unsigned __int64 *)(a1 + 40))) goto loc_006A8EC0;
    a1 = (unsigned int)((*(unsigned __int8 *)(a3)) & (15));
    a3 = (a3) + (v_rbp + 1);
    goto loc_006A8D1F;
loc_006A8D16:
    a1 = (unsigned int)((*(unsigned __int8 *)(a3)) >> (4));
    v_rbp = 0;
loc_006A8D1F:
    if (((unsigned int)(a1)) != 15) goto loc_006A8DFB;
    if (a3 >= (*(unsigned __int64 *)(a1 + 40))) goto loc_006A8EC0;
    a3 = (a3) + (v_rbp + 1);
    if (((unsigned int)(*(unsigned __int8 *)(a3))) != 255) goto loc_006A8DF8;
    if (a3 >= (*(unsigned __int64 *)(a1 + 64))) goto loc_006A8EC0;
    a3 = (a3) + (2);
    if (((unsigned int)(*(unsigned __int16 *)(a3))) < 277) goto loc_006A8EC0;
loc_006A8D62:
    a1 = (unsigned int)((*(unsigned __int16 *)(a3)) + (3));
loc_006A8D65:
    *(unsigned __int64 *)(a1 + 88) = a3;
    a3 = ((int)((unsigned int)(result))) + (a2);
loc_006A8D6F:
    result = ((int)((unsigned int)(a1))) + (a2);
    if (a3 < (*(unsigned __int64 *)(a1 + 8))) goto loc_006A8EC0;
    if (result > (*(unsigned __int64 *)(a1 + 24))) goto loc_006A8E3B;
    if (((unsigned int)(a1)) <= 8) goto loc_006A8DE2;
    result = (unsigned int)((a1 - 9) >> (3));
    result = (unsigned int)((result) + 1);
    result = (unsigned int)(-(result));
loc_006A8D9F:
    *(unsigned __int8 *)(a2) = (unsigned __int8)(*(unsigned __int8 *)(a3));
    *(unsigned __int8 *)(a2 + 1) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 1));
    *(unsigned __int8 *)(a2 + 2) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 2));
    *(unsigned __int8 *)(a2 + 3) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 3));
    *(unsigned __int8 *)(a2 + 4) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 4));
    *(unsigned __int8 *)(a2 + 5) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 5));
    *(unsigned __int8 *)(a2 + 6) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 6));
    a3 = (a3) + (8);
    *(unsigned __int8 *)(a2 + 7) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 7));
    a2 = (a2) + (8);
    v_rbx = ((unsigned int)((unsigned int)(result))) - (v_rbp + 1);
    if (condition_is_not_equal) goto loc_006A8D9F;
loc_006A8DE2:
    a3 = (a3) + (v_rbp + 1);
    *(unsigned __int8 *)(a2) = (unsigned __int8)(*(unsigned __int8 *)(a3));
    a2 = (a2) + (v_rbp + 1);
    a1 = (unsigned int)((a1 + result * 8) - ((unsigned int)(v_rbp + 1)));
    if (condition_is_not_equal) goto loc_006A8DE2;
    goto loc_006A8E28;
loc_006A8DF8:
    a1 = (unsigned int)((a1) + (15));
loc_006A8DFB:
    a1 = (unsigned int)((a1) + (10));
    goto loc_006A8D65;
loc_006A8E03:
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3)) * 2 + 1) + ((unsigned int)((unsigned int)(*(unsigned int *)(a3)) * 2 + 1)));
loc_006A8E06:
    if (a2 >= (*(unsigned __int64 *)(a1 + 24))) goto loc_006A8EB6;
    if ((*(unsigned __int64 *)(a1 + 88)) >= (*(unsigned __int64 *)(a1 + 40))) goto loc_006A8EC0;
    *(unsigned __int8 *)(a2) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 88)));
    a2 = (a2) + (v_rbp + 1);
    a3 = (*(unsigned __int64 *)(a1 + 88)) + (v_rbp + 1);
loc_006A8E28:
    if (!sign_flag) goto loc_006A8E03;
    v_r11 = (unsigned int)((v_r11) + ((unsigned int)(v_r11)));
    if (condition_is_not_equal) goto loc_006A8CCB;
    goto loc_006A8CA6;
loc_006A8E3B:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 24))) - ((unsigned int)(a2)));
    if (((unsigned int)(a1)) <= 8) goto loc_006A8E97;
    result = (unsigned int)((a1 - 9) >> (3));
    result = (unsigned int)((result) + 1);
    result = (unsigned int)(-(result));
loc_006A8E54:
    *(unsigned __int8 *)(a2) = (unsigned __int8)(*(unsigned __int8 *)(a3));
    *(unsigned __int8 *)(a2 + 1) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 1));
    *(unsigned __int8 *)(a2 + 2) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 2));
    *(unsigned __int8 *)(a2 + 3) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 3));
    *(unsigned __int8 *)(a2 + 4) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 4));
    *(unsigned __int8 *)(a2 + 5) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 5));
    *(unsigned __int8 *)(a2 + 6) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 6));
    a3 = (a3) + (8);
    *(unsigned __int8 *)(a2 + 7) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 7));
    a2 = (a2) + (8);
    v_r11 = ((unsigned int)((unsigned int)(result))) - (v_rbp + 1);
    if (condition_is_not_equal) goto loc_006A8E54;
loc_006A8E97:
    a3 = (a3) + (v_rbp + 1);
    *(unsigned __int8 *)(a2) = (unsigned __int8)(*(unsigned __int8 *)(a3));
    a2 = (a2) + (v_rbp + 1);
    a1 = (unsigned int)((a1 + result * 8) - ((unsigned int)(v_rbp + 1)));
    if (condition_is_not_equal) goto loc_006A8E97;
    goto loc_006A8EB6;
loc_006A8EAD:
    if (a2 == (*(unsigned __int64 *)(a1))) {
        *(unsigned int *)(a1 + 100) = (unsigned int)(v_rbp + 1);
    }
    *(unsigned __int64 *)(a1 + 88) = *(unsigned __int64 *)(a1 + 88);
    *(unsigned __int64 *)(a1 + 32) = a2;
    goto loc_006A8EC3;
loc_006A8EC0:
    v_r10 = 0;
loc_006A8EC3:
    *(unsigned int *)(a1 + 96) = 0;
    return *(unsigned __int8 *)(a3);
}
```

## 5. (Beta) C Style

```c
int64_t do_decode(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_rbp;
    int64_t local_rbx;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rbp = 0;
loc_006A8B00:
    if ((*(uint64_t *)(arg1 + 0x30)) >= (*(uint64_t *)(arg1 + 0x38))) goto loc_006A8CA6;
    if ((*(uint64_t *)(arg1 + 0x8)) >= (*(uint64_t *)(arg1 + 0x10))) goto loc_006A8CA6;
    a3 = (*(uint64_t *)(arg1 + 0x30)) + (4);
    if (!sign_flag) goto loc_006A8C7F;
loc_006A8B2B:
    a3 = (a3) + (2);
    result = (uint32_t)((*(uint16_t *)(a3)) >> (3));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(a3)))) & (7));
    result = (uint32_t)(~(result));
    if (((uint32_t)(Arg1)) > 5) goto loc_006A8B8B;
    local_rbx = ((int32_t)((uint32_t)(result))) + (*(uint64_t *)(arg1 + 0x8));
    if (local_rbx < (*(uint64_t *)(arg1 + 0x8))) goto loc_006A8EC0;
    Arg1 = (uint32_t)((Arg1) + (3));
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8)) = (uint8_t)(*(uint8_t *)(local_rbx));
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x1) = (uint8_t)(*(uint8_t *)(local_rbx + 0x1));
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x2) = (uint8_t)(*(uint8_t *)(local_rbx + 0x2));
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x3) = (uint8_t)(*(uint8_t *)(local_rbx + 0x3));
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x4) = (uint8_t)(*(uint8_t *)(local_rbx + 0x4));
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x5) = (uint8_t)(*(uint8_t *)(local_rbx + 0x5));
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x6) = (uint8_t)(*(uint8_t *)(local_rbx + 0x6));
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x7) = (uint8_t)(*(uint8_t *)(local_rbx + 0x7));
    a2 = (*(uint64_t *)(arg1 + 0x8)) + (Arg1);
    goto loc_006A8C8A;
loc_006A8B8B:
    if (((uint32_t)(Arg1)) != 7) goto loc_006A8BDD;
    if (0 != 0) goto loc_006A8BA4;
    Arg1 = (uint32_t)((*(uint8_t *)(a3)) & (15));
    a3 = (a3) + (local_rbp + 1);
    goto loc_006A8BAD;
loc_006A8BA4:
    Arg1 = (uint32_t)((*(uint8_t *)(a3)) >> (4));
    local_rbp = 0;
loc_006A8BAD:
    if (((uint32_t)(Arg1)) != 15) goto loc_006A8C74;
    a3 = (a3) + (local_rbp + 1);
    if (((uint32_t)(*(uint8_t *)(a3))) != 255) goto loc_006A8C71;
    a3 = (a3) + (2);
    if (((uint32_t)(*(uint16_t *)(a3))) < 277) goto loc_006A8EC0;
loc_006A8BDD:
    Arg1 = (uint32_t)((*(uint16_t *)(a3)) + (3));
loc_006A8BE0:
    *(uint64_t *)(arg1 + 0x58) = a3;
    a3 = ((int32_t)((uint32_t)(*(uint8_t *)(local_rbx + 0x7)))) + (a2);
    result = ((uint32_t)((uint32_t)(Arg1))) + (a2);
    if (result >= (*(uint64_t *)(arg1 + 0x10))) goto loc_006A8C9D;
    if (a3 < (*(uint64_t *)(arg1 + 0x8))) goto loc_006A8EC0;
    if (((uint32_t)(Arg1)) <= 8) goto loc_006A8C5A;
    result = (uint32_t)((Arg1 - 9) >> (3));
    result = (uint32_t)((result) + 1);
    result = (uint32_t)(-(result));
loc_006A8C17:
    *(uint8_t *)(a2) = (uint8_t)(*(uint8_t *)(a3));
    *(uint8_t *)(a2 + 0x1) = (uint8_t)(*(uint8_t *)(a3 + 0x1));
    *(uint8_t *)(a2 + 0x2) = (uint8_t)(*(uint8_t *)(a3 + 0x2));
    *(uint8_t *)(a2 + 0x3) = (uint8_t)(*(uint8_t *)(a3 + 0x3));
    *(uint8_t *)(a2 + 0x4) = (uint8_t)(*(uint8_t *)(a3 + 0x4));
    *(uint8_t *)(a2 + 0x5) = (uint8_t)(*(uint8_t *)(a3 + 0x5));
    *(uint8_t *)(a2 + 0x6) = (uint8_t)(*(uint8_t *)(a3 + 0x6));
    a3 = (a3) + (8);
    *(uint8_t *)(a2 + 0x7) = (uint8_t)(*(uint8_t *)(a3 + 0x7));
    a2 = (a2) + (8);
    local_rbx = ((uint32_t)((uint32_t)(result))) - (local_rbp + 1);
    if (condition_is_not_equal) goto loc_006A8C17;
loc_006A8C5A:
    a3 = (a3) - (a2);
loc_006A8C5D:
    *(uint8_t *)(a2) = (uint8_t)(*(uint8_t *)(a3 + a2 * 1));
    a2 = (a2) + (local_rbp + 1);
    Arg1 = (uint32_t)((Arg1 + result * 8) - ((uint32_t)(local_rbp + 1)));
    if (condition_is_not_equal) goto loc_006A8C5D;
    goto loc_006A8C8A;
loc_006A8C71:
    Arg1 = (uint32_t)((Arg1) + (15));
loc_006A8C74:
    Arg1 = (uint32_t)((Arg1) + (10));
    goto loc_006A8BE0;
loc_006A8C7C:
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x30))) * 2 + 1) + ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x30))) * 2 + 1)));
loc_006A8C7F:
    *(uint8_t *)(a2) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x58)));
    a2 = (a2) + (local_rbp + 1);
    a3 = (*(uint64_t *)(arg1 + 0x58)) + (local_rbp + 1);
loc_006A8C8A:
    if (!sign_flag) goto loc_006A8C7C;
    local_r11 = (uint32_t)((local_r11) + ((uint32_t)(local_r11)));
    if (condition_is_not_equal) goto loc_006A8B2B;
    goto loc_006A8B00;
loc_006A8C9D:
    goto loc_006A8D6F;
loc_006A8CA6:
    if (a3 >= (*(uint64_t *)(arg1 + 0x48))) goto loc_006A8EC0;
    a3 = (a3) + (4);
    if (!sign_flag) goto loc_006A8E06;
loc_006A8CCB:
    if (a2 >= (*(uint64_t *)(arg1 + 0x18))) goto loc_006A8EAD;
    if (a3 >= (*(uint64_t *)(arg1 + 0x40))) goto loc_006A8EC0;
    a3 = (a3) + (2);
    result = (uint32_t)((*(uint16_t *)(a3)) >> (3));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(a3)))) & (7));
    result = (uint32_t)(~(result));
    if (((uint32_t)(Arg1)) != 7) goto loc_006A8D62;
    if (0 != 0) goto loc_006A8D16;
    if (a3 >= (*(uint64_t *)(arg1 + 0x28))) goto loc_006A8EC0;
    Arg1 = (uint32_t)((*(uint8_t *)(a3)) & (15));
    a3 = (a3) + (local_rbp + 1);
    goto loc_006A8D1F;
loc_006A8D16:
    Arg1 = (uint32_t)((*(uint8_t *)(a3)) >> (4));
    local_rbp = 0;
loc_006A8D1F:
    if (((uint32_t)(Arg1)) != 15) goto loc_006A8DFB;
    if (a3 >= (*(uint64_t *)(arg1 + 0x28))) goto loc_006A8EC0;
    a3 = (a3) + (local_rbp + 1);
    if (((uint32_t)(*(uint8_t *)(a3))) != 255) goto loc_006A8DF8;
    if (a3 >= (*(uint64_t *)(arg1 + 0x40))) goto loc_006A8EC0;
    a3 = (a3) + (2);
    if (((uint32_t)(*(uint16_t *)(a3))) < 277) goto loc_006A8EC0;
loc_006A8D62:
    Arg1 = (uint32_t)((*(uint16_t *)(a3)) + (3));
loc_006A8D65:
    *(uint64_t *)(arg1 + 0x58) = a3;
    a3 = ((int32_t)((uint32_t)(result))) + (a2);
loc_006A8D6F:
    result = ((int32_t)((uint32_t)(Arg1))) + (a2);
    if (a3 < (*(uint64_t *)(arg1 + 0x8))) goto loc_006A8EC0;
    if (result > (*(uint64_t *)(arg1 + 0x18))) goto loc_006A8E3B;
    if (((uint32_t)(Arg1)) <= 8) goto loc_006A8DE2;
    result = (uint32_t)((Arg1 - 9) >> (3));
    result = (uint32_t)((result) + 1);
    result = (uint32_t)(-(result));
loc_006A8D9F:
    *(uint8_t *)(a2) = (uint8_t)(*(uint8_t *)(a3));
    *(uint8_t *)(a2 + 0x1) = (uint8_t)(*(uint8_t *)(a3 + 0x1));
    *(uint8_t *)(a2 + 0x2) = (uint8_t)(*(uint8_t *)(a3 + 0x2));
    *(uint8_t *)(a2 + 0x3) = (uint8_t)(*(uint8_t *)(a3 + 0x3));
    *(uint8_t *)(a2 + 0x4) = (uint8_t)(*(uint8_t *)(a3 + 0x4));
    *(uint8_t *)(a2 + 0x5) = (uint8_t)(*(uint8_t *)(a3 + 0x5));
    *(uint8_t *)(a2 + 0x6) = (uint8_t)(*(uint8_t *)(a3 + 0x6));
    a3 = (a3) + (8);
    *(uint8_t *)(a2 + 0x7) = (uint8_t)(*(uint8_t *)(a3 + 0x7));
    a2 = (a2) + (8);
    local_rbx = ((uint32_t)((uint32_t)(result))) - (local_rbp + 1);
    if (condition_is_not_equal) goto loc_006A8D9F;
loc_006A8DE2:
    a3 = (a3) + (local_rbp + 1);
    *(uint8_t *)(a2) = (uint8_t)(*(uint8_t *)(a3));
    a2 = (a2) + (local_rbp + 1);
    Arg1 = (uint32_t)((Arg1 + result * 8) - ((uint32_t)(local_rbp + 1)));
    if (condition_is_not_equal) goto loc_006A8DE2;
    goto loc_006A8E28;
loc_006A8DF8:
    Arg1 = (uint32_t)((Arg1) + (15));
loc_006A8DFB:
    Arg1 = (uint32_t)((Arg1) + (10));
    goto loc_006A8D65;
loc_006A8E03:
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(a3)) * 2 + 1) + ((uint32_t)((uint32_t)(*(uint32_t *)(a3)) * 2 + 1)));
loc_006A8E06:
    if (a2 >= (*(uint64_t *)(arg1 + 0x18))) goto loc_006A8EB6;
    if ((*(uint64_t *)(arg1 + 0x58)) >= (*(uint64_t *)(arg1 + 0x28))) goto loc_006A8EC0;
    *(uint8_t *)(a2) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x58)));
    a2 = (a2) + (local_rbp + 1);
    a3 = (*(uint64_t *)(arg1 + 0x58)) + (local_rbp + 1);
loc_006A8E28:
    if (!sign_flag) goto loc_006A8E03;
    local_r11 = (uint32_t)((local_r11) + ((uint32_t)(local_r11)));
    if (condition_is_not_equal) goto loc_006A8CCB;
    goto loc_006A8CA6;
loc_006A8E3B:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x18))) - ((uint32_t)(a2)));
    if (((uint32_t)(Arg1)) <= 8) goto loc_006A8E97;
    result = (uint32_t)((Arg1 - 9) >> (3));
    result = (uint32_t)((result) + 1);
    result = (uint32_t)(-(result));
loc_006A8E54:
    *(uint8_t *)(a2) = (uint8_t)(*(uint8_t *)(a3));
    *(uint8_t *)(a2 + 0x1) = (uint8_t)(*(uint8_t *)(a3 + 0x1));
    *(uint8_t *)(a2 + 0x2) = (uint8_t)(*(uint8_t *)(a3 + 0x2));
    *(uint8_t *)(a2 + 0x3) = (uint8_t)(*(uint8_t *)(a3 + 0x3));
    *(uint8_t *)(a2 + 0x4) = (uint8_t)(*(uint8_t *)(a3 + 0x4));
    *(uint8_t *)(a2 + 0x5) = (uint8_t)(*(uint8_t *)(a3 + 0x5));
    *(uint8_t *)(a2 + 0x6) = (uint8_t)(*(uint8_t *)(a3 + 0x6));
    a3 = (a3) + (8);
    *(uint8_t *)(a2 + 0x7) = (uint8_t)(*(uint8_t *)(a3 + 0x7));
    a2 = (a2) + (8);
    local_r11 = ((uint32_t)((uint32_t)(result))) - (local_rbp + 1);
    if (condition_is_not_equal) goto loc_006A8E54;
loc_006A8E97:
    a3 = (a3) + (local_rbp + 1);
    *(uint8_t *)(a2) = (uint8_t)(*(uint8_t *)(a3));
    a2 = (a2) + (local_rbp + 1);
    Arg1 = (uint32_t)((Arg1 + result * 8) - ((uint32_t)(local_rbp + 1)));
    if (condition_is_not_equal) goto loc_006A8E97;
    goto loc_006A8EB6;
loc_006A8EAD:
    if (a2 == (*(uint64_t *)(arg1))) {
        *(uint32_t *)(arg1 + 0x64) = (uint32_t)(local_rbp + 1);
    }
    *(uint64_t *)(arg1 + 0x58) = *(uint64_t *)(arg1 + 0x58);
    *(uint64_t *)(arg1 + 0x20) = a2;
    goto loc_006A8EC3;
loc_006A8EC0:
    local_r10 = 0;
loc_006A8EC3:
    *(uint32_t *)(arg1 + 0x60) = 0;
    return *(uint8_t *)(a3);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `W` |
| `Arg1` | `+ 0x60` | `32` | `W` |
| `Arg1` | `+ 0x64` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006A8ADC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
