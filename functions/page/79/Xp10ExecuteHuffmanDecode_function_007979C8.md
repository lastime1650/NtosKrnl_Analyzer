# Xp10ExecuteHuffmanDecode

- RVA: `0x007979C8`–`0x007980FA` (길이 `1,842` bytes)
- VA: `0x00000001407979C8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00081478`
- 디코드: `572`개 명령, `1,842/1,842` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00797A4E` → [Xp10ReadAndDecodeHuffmanTables](Xp10ReadAndDecodeHuffmanTables_function_007993D4.md) (function, `0x007993D4`)
- `0x00797A87` → [Xp10ReadAndDecodeHuffmanTables](Xp10ReadAndDecodeHuffmanTables_function_007993D4.md) (function, `0x007993D4`)
- `0x00797AEA` → [Xp10ScatteredReadBytes](Xp10ScatteredReadBytes_function_0079A220.md) (function, `0x0079A220`)
- `0x00797B75` → [Xp10ScatteredReadBytes](Xp10ScatteredReadBytes_function_0079A220.md) (function, `0x0079A220`)
- `0x00797BE0` → [Xp10ScatteredReadBytes](Xp10ScatteredReadBytes_function_0079A220.md) (function, `0x0079A220`)
- `0x00797C61` → [Xp10ScatteredReadBytes](Xp10ScatteredReadBytes_function_0079A220.md) (function, `0x0079A220`)
- `0x00797CC7` → [Xp10ScatteredNextBuffer](Xp10ScatteredNextBuffer_function_0079A1CC.md) (function, `0x0079A1CC`)
- `0x00797D20` → [Xp10ScatteredReadBytes](Xp10ScatteredReadBytes_function_0079A220.md) (function, `0x0079A220`)
- `0x00797D92` → [Xp10ScatteredReadBytes](Xp10ScatteredReadBytes_function_0079A220.md) (function, `0x0079A220`)
- `0x00797DEC` → [Xp10ScatteredReadBytes](Xp10ScatteredReadBytes_function_0079A220.md) (function, `0x0079A220`)
- `0x00797E63` → [Xp10ScatteredReadBytes](Xp10ScatteredReadBytes_function_0079A220.md) (function, `0x0079A220`)
- `0x00797EDA` → [Xp10ScatteredReadBytes](Xp10ScatteredReadBytes_function_0079A220.md) (function, `0x0079A220`)
- `0x00798016` → [Xp10ScatteredReadBytes](Xp10ScatteredReadBytes_function_0079A220.md) (function, `0x0079A220`)
- `0x007980B0` → [Xp10ScatteredCopyFromPrevious](Xp10ScatteredCopyFromPrevious_function_0079A174.md) (function, `0x0079A174`)
- `0x007980CF` → [Xp10ScatteredCopyFromPrevious](Xp10ScatteredCopyFromPrevious_function_0079A174.md) (function, `0x0079A174`)

### Direct callers
- [RtlDecompressBuffer2Xp10](RtlDecompressBuffer2Xp10_function_007959A0.md) at `0x00795B6B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007979C8  4C 8B DC                        mov r11, rsp
007979CB  49 89 5B 10                     mov qword ptr [r11 + 0x10], rbx
007979CF  4D 89 43 18                     mov qword ptr [r11 + 0x18], r8
007979D3  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
007979D7  55                              push rbp
007979D8  56                              push rsi
007979D9  57                              push rdi
007979DA  41 54                           push r12
007979DC  41 55                           push r13
007979DE  41 56                           push r14
007979E0  41 57                           push r15
007979E2  48 8B EC                        mov rbp, rsp
007979E5  48 83 EC 70                     sub rsp, 0x70
007979E9  48 8B 01                        mov rax, qword ptr [rcx]
007979EC  4C 8B E1                        mov r12, rcx
007979EF  45 33 ED                        xor r13d, r13d
007979F2  48 8B DA                        mov rbx, rdx
007979F5  4C 89 6D D8                     mov qword ptr [rbp - 0x28], r13
007979F9  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
007979FD  44 0F B7 08                     movzx r9d, word ptr [rax]
00797A01  41 8B C9                        mov ecx, r9d
00797A04  44 89 6D 58                     mov dword ptr [rbp + 0x58], r13d
00797A08  83 E1 1F                        and ecx, 0x1f
00797A0B  41 C1 E9 05                     shr r9d, 5
00797A0F  41 8D 45 01                     lea eax, [r13 + 1]
00797A13  41 83 E1 07                     and r9d, 7
00797A17  D3 E0                           shl eax, cl
00797A19  41 2B C1                        sub eax, r9d
00797A1C  2D F6 00 00 00                  sub eax, 0xf6
00797A21  8D 51 14                        lea edx, [rcx + 0x14]
00797A24  0F BD F0                        bsr esi, eax
00797A27  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00797A2B  C1 E2 04                        shl edx, 4
00797A2E  49 89 4B 90                     mov qword ptr [r11 - 0x70], rcx
00797A32  8D 78 FF                        lea edi, [rax - 1]
00797A35  23 F8                           and edi, eax
00797A37  89 55 D4                        mov dword ptr [rbp - 0x2c], edx
00797A3A  49 8D 84 24 58 12 00 00         lea rax, [r12 + 0x1258]
00797A42  49 8B CC                        mov rcx, r12
00797A45  49 89 43 80                     mov qword ptr [r11 - 0x80], rax
00797A49  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00797A4E  E8 81 19 00 00                  call 0x1407993d4
00797A53  85 C0                           test eax, eax
00797A55  0F 88 86 06 00 00               js 0x1407980e1
00797A5B  8D 56 01                        lea edx, [rsi + 1]
00797A5E  85 FF                           test edi, edi
00797A60  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00797A64  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00797A69  49 8D 84 24 58 52 00 00         lea rax, [r12 + 0x5258]
00797A71  0F 44 D6                        cmove edx, esi
00797A74  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00797A79  81 C2 E8 00 00 00               add edx, 0xe8
00797A7F  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00797A84  49 8B CC                        mov rcx, r12
00797A87  E8 48 19 00 00                  call 0x1407993d4
00797A8C  85 C0                           test eax, eax
00797A8E  0F 88 4D 06 00 00               js 0x1407980e1
00797A94  48 8D 4B 08                     lea rcx, [rbx + 8]
00797A98  4C 8B F1                        mov r14, rcx
00797A9B  48 8B 03                        mov rax, qword ptr [rbx]
00797A9E  4C 89 75 E0                     mov qword ptr [rbp - 0x20], r14
00797AA2  48 85 C0                        test rax, rax
00797AA5  0F 84 36 06 00 00               je 0x1407980e1
00797AAB  48 8B 75 E8                     mov rsi, qword ptr [rbp - 0x18]
00797AAF  BF 0C 00 00 00                  mov edi, 0xc
00797AB4  48 89 75 F0                     mov qword ptr [rbp - 0x10], rsi
00797AB8  44 89 6D 58                     mov dword ptr [rbp + 0x58], r13d
00797ABC  48 3B C7                        cmp rax, rdi
00797ABF  73 09                           jae 0x140797aca
00797AC1  8B F8                           mov edi, eax
00797AC3  48 89 4D E0                     mov qword ptr [rbp - 0x20], rcx
00797AC7  4C 8B F1                        mov r14, rcx
00797ACA  4C 8D 6B 10                     lea r13, [rbx + 0x10]
00797ACE  4D 8B FE                        mov r15, r14
00797AD1  41 8B 55 00                     mov edx, dword ptr [r13]
00797AD5  4D 8B C5                        mov r8, r13
00797AD8  3B D7                           cmp edx, edi
00797ADA  73 38                           jae 0x140797b14
00797ADC  48 8D 4B 18                     lea rcx, [rbx + 0x18]
00797AE0  41 B8 04 00 00 00               mov r8d, 4
00797AE6  48 8D 55 58                     lea rdx, [rbp + 0x58]
00797AEA  E8 31 27 00 00                  call 0x14079a220
00797AEF  41 8B 4D 00                     mov ecx, dword ptr [r13]
00797AF3  4D 8B C5                        mov r8, r13
00797AF6  8B 55 58                        mov edx, dword ptr [rbp + 0x58]
00797AF9  48 D3 E2                        shl rdx, cl
00797AFC  49 09 16                        or qword ptr [r14], rdx
00797AFF  8D 14 C1                        lea edx, [rcx + rax*8]
00797B02  41 89 55 00                     mov dword ptr [r13], edx
00797B06  3B D7                           cmp edx, edi
00797B08  73 0A                           jae 0x140797b14
00797B0A  8B FA                           mov edi, edx
00797B0C  4C 8D 43 10                     lea r8, [rbx + 0x10]
00797B10  4C 8D 7B 08                     lea r15, [rbx + 8]
00797B14  4C 8B 0B                        mov r9, qword ptr [rbx]
00797B17  8B CF                           mov ecx, edi
00797B19  83 65 D0 00                     and dword ptr [rbp - 0x30], 0
00797B1D  B8 01 00 00 00                  mov eax, 1
00797B22  48 D3 E0                        shl rax, cl
00797B25  49 8B F8                        mov rdi, r8
00797B28  FF C8                           dec eax
00797B2A  49 8B C9                        mov rcx, r9
00797B2D  41 23 06                        and eax, dword ptr [r14]
00797B30  4D 8B F7                        mov r14, r15
00797B33  44 0F BF 14 46                  movsx r10d, word ptr [rsi + rax*2]
00797B38  41 8B F2                        mov esi, r10d
00797B3B  66 44 89 55 58                  mov word ptr [rbp + 0x58], r10w
00797B40  83 E6 0F                        and esi, 0xf
00797B43  4D 85 C9                        test r9, r9
00797B46  74 5F                           je 0x140797ba7
00797B48  85 F6                           test esi, esi
00797B4A  74 5B                           je 0x140797ba7
00797B4C  8B C6                           mov eax, esi
00797B4E  49 8B FD                        mov rdi, r13
00797B51  4D 8B EF                        mov r13, r15
00797B54  49 3B C1                        cmp rax, r9
00797B57  76 0A                           jbe 0x140797b63
00797B59  41 8B F1                        mov esi, r9d
00797B5C  4C 8D 6B 08                     lea r13, [rbx + 8]
00797B60  49 8B F8                        mov rdi, r8
00797B63  3B D6                           cmp edx, esi
00797B65  73 31                           jae 0x140797b98
00797B67  48 8D 4B 18                     lea rcx, [rbx + 0x18]
00797B6B  41 B8 04 00 00 00               mov r8d, 4
00797B71  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00797B75  E8 A6 26 00 00                  call 0x14079a220
00797B7A  8B 0F                           mov ecx, dword ptr [rdi]
00797B7C  8B 55 D0                        mov edx, dword ptr [rbp - 0x30]
00797B7F  44 0F B7 55 58                  movzx r10d, word ptr [rbp + 0x58]
00797B84  48 D3 E2                        shl rdx, cl
00797B87  49 09 17                        or qword ptr [r15], rdx
00797B8A  8D 14 C1                        lea edx, [rcx + rax*8]
00797B8D  89 17                           mov dword ptr [rdi], edx
00797B8F  3B D6                           cmp edx, esi
00797B91  73 05                           jae 0x140797b98
00797B93  8B F2                           mov esi, edx
00797B95  4D 8B F5                        mov r14, r13
00797B98  8B CE                           mov ecx, esi
00797B9A  49 D3 2E                        shr qword ptr [r14], cl
00797B9D  48 29 0B                        sub qword ptr [rbx], rcx
00797BA0  48 8B 0B                        mov rcx, qword ptr [rbx]
00797BA3  2B D6                           sub edx, esi
00797BA5  89 17                           mov dword ptr [rdi], edx
00797BA7  45 33 ED                        xor r13d, r13d
00797BAA  45 8D 7D 04                     lea r15d, [r13 + 4]
00797BAE  66 45 85 D2                     test r10w, r10w
00797BB2  0F 89 EA 00 00 00               jns 0x140797ca2
00797BB8  4C 8B 65 F0                     mov r12, qword ptr [rbp - 0x10]
00797BBC  44 89 6D D0                     mov dword ptr [rbp - 0x30], r13d
00797BC0  BE 06 00 00 00                  mov esi, 6
00797BC5  48 85 C9                        test rcx, rcx
00797BC8  74 4C                           je 0x140797c16
00797BCA  48 3B CE                        cmp rcx, rsi
00797BCD  73 02                           jae 0x140797bd1
00797BCF  8B 33                           mov esi, dword ptr [rbx]
00797BD1  39 37                           cmp dword ptr [rdi], esi
00797BD3  73 2A                           jae 0x140797bff
00797BD5  48 8D 4B 18                     lea rcx, [rbx + 0x18]
00797BD9  45 8B C7                        mov r8d, r15d
00797BDC  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00797BE0  E8 3B 26 00 00                  call 0x14079a220
00797BE5  8B 0F                           mov ecx, dword ptr [rdi]
00797BE7  8B 55 D0                        mov edx, dword ptr [rbp - 0x30]
00797BEA  44 0F B7 55 58                  movzx r10d, word ptr [rbp + 0x58]
00797BEF  48 D3 E2                        shl rdx, cl
00797BF2  49 09 16                        or qword ptr [r14], rdx
00797BF5  8D 14 C1                        lea edx, [rcx + rax*8]
00797BF8  3B D6                           cmp edx, esi
00797BFA  89 17                           mov dword ptr [rdi], edx
00797BFC  0F 42 F2                        cmovb esi, edx
00797BFF  8B CE                           mov ecx, esi
00797C01  BA 01 00 00 00                  mov edx, 1
00797C06  48 D3 E2                        shl rdx, cl
00797C09  48 8B 0B                        mov rcx, qword ptr [rbx]
00797C0C  FF CA                           dec edx
00797C0E  41 23 16                        and edx, dword ptr [r14]
00797C11  4C 8B C1                        mov r8, rcx
00797C14  EB 06                           jmp 0x140797c1c
00797C16  41 8B D5                        mov edx, r13d
00797C19  4D 8B C5                        mov r8, r13
00797C1C  49 0F BF C2                     movsx rax, r10w
00797C20  48 83 E0 F0                     and rax, 0xfffffffffffffff0
00797C24  44 89 6D D0                     mov dword ptr [rbp - 0x30], r13d
00797C28  4D 8D 24 44                     lea r12, [r12 + rax*2]
00797C2C  8B C2                           mov eax, edx
00797C2E  45 0F BF 14 44                  movsx r10d, word ptr [r12 + rax*2]
00797C33  41 8B F2                        mov esi, r10d
00797C36  66 44 89 55 58                  mov word ptr [rbp + 0x58], r10w
00797C3B  83 E6 0F                        and esi, 0xf
00797C3E  4D 85 C0                        test r8, r8
00797C41  74 4D                           je 0x140797c90
00797C43  85 F6                           test esi, esi
00797C45  74 49                           je 0x140797c90
00797C47  8B C6                           mov eax, esi
00797C49  49 3B C0                        cmp rax, r8
00797C4C  76 02                           jbe 0x140797c50
00797C4E  8B 33                           mov esi, dword ptr [rbx]
00797C50  8B 07                           mov eax, dword ptr [rdi]
00797C52  3B C6                           cmp eax, esi
00797C54  73 2B                           jae 0x140797c81
00797C56  48 8D 4B 18                     lea rcx, [rbx + 0x18]
00797C5A  45 8B C7                        mov r8d, r15d
00797C5D  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00797C61  E8 BA 25 00 00                  call 0x14079a220
00797C66  8B 0F                           mov ecx, dword ptr [rdi]
00797C68  8B 55 D0                        mov edx, dword ptr [rbp - 0x30]
00797C6B  44 0F B7 55 58                  movzx r10d, word ptr [rbp + 0x58]
00797C70  48 D3 E2                        shl rdx, cl
00797C73  49 09 16                        or qword ptr [r14], rdx
00797C76  8D 04 C1                        lea eax, [rcx + rax*8]
00797C79  89 07                           mov dword ptr [rdi], eax
00797C7B  3B C6                           cmp eax, esi
00797C7D  73 02                           jae 0x140797c81
00797C7F  8B F0                           mov esi, eax
00797C81  8B CE                           mov ecx, esi
00797C83  49 D3 2E                        shr qword ptr [r14], cl
00797C86  48 29 0B                        sub qword ptr [rbx], rcx
00797C89  48 8B 0B                        mov rcx, qword ptr [rbx]
00797C8C  2B C6                           sub eax, esi
00797C8E  89 07                           mov dword ptr [rdi], eax
00797C90  66 45 85 D2                     test r10w, r10w
00797C94  0F 88 22 FF FF FF               js 0x140797bbc
00797C9A  4C 8B 65 40                     mov r12, qword ptr [rbp + 0x40]
00797C9E  48 8D 7B 10                     lea rdi, [rbx + 0x10]
00797CA2  66 41 C1 EA 04                  shr r10w, 4
00797CA7  B8 00 01 00 00                  mov eax, 0x100
00797CAC  66 44 89 55 58                  mov word ptr [rbp + 0x58], r10w
00797CB1  66 44 3B D0                     cmp r10w, ax
00797CB5  73 31                           jae 0x140797ce8
00797CB7  4C 8B 7D 50                     mov r15, qword ptr [rbp + 0x50]
00797CBB  49 8B 07                        mov rax, qword ptr [r15]
00797CBE  49 3B 47 08                     cmp rax, qword ptr [r15 + 8]
00797CC2  75 11                           jne 0x140797cd5
00797CC4  49 8B CF                        mov rcx, r15
00797CC7  E8 00 25 00 00                  call 0x14079a1cc
00797CCC  85 C0                           test eax, eax
00797CCE  75 EB                           jne 0x140797cbb
00797CD0  E9 07 04 00 00                  jmp 0x1407980dc
00797CD5  44 88 10                        mov byte ptr [rax], r10b
00797CD8  49 FF 07                        inc qword ptr [r15]
00797CDB  4C 8B 75 E0                     mov r14, qword ptr [rbp - 0x20]
00797CDF  48 8D 4B 08                     lea rcx, [rbx + 8]
00797CE3  E9 B3 FD FF FF                  jmp 0x140797a9b
00797CE8  41 8A C2                        mov al, r10b
00797CEB  24 0F                           and al, 0xf
00797CED  3C 0F                           cmp al, 0xf
00797CEF  0F 85 78 02 00 00               jne 0x140797f6d
00797CF5  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
00797CF9  BE 0C 00 00 00                  mov esi, 0xc
00797CFE  44 89 6D D0                     mov dword ptr [rbp - 0x30], r13d
00797D02  4C 8B F2                        mov r14, rdx
00797D05  48 85 C9                        test rcx, rcx
00797D08  74 49                           je 0x140797d53
00797D0A  48 3B CE                        cmp rcx, rsi
00797D0D  73 02                           jae 0x140797d11
00797D0F  8B 33                           mov esi, dword ptr [rbx]
00797D11  39 37                           cmp dword ptr [rdi], esi
00797D13  73 2A                           jae 0x140797d3f
00797D15  48 8D 4B 18                     lea rcx, [rbx + 0x18]
00797D19  45 8B C7                        mov r8d, r15d
00797D1C  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00797D20  E8 FB 24 00 00                  call 0x14079a220
00797D25  8B 0F                           mov ecx, dword ptr [rdi]
00797D27  8B 55 D0                        mov edx, dword ptr [rbp - 0x30]
00797D2A  48 D3 E2                        shl rdx, cl
00797D2D  48 09 53 08                     or qword ptr [rbx + 8], rdx
00797D31  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
00797D35  8D 04 C1                        lea eax, [rcx + rax*8]
00797D38  3B C6                           cmp eax, esi
00797D3A  89 07                           mov dword ptr [rdi], eax
00797D3C  0F 42 F0                        cmovb esi, eax
00797D3F  8B CE                           mov ecx, esi
00797D41  B8 01 00 00 00                  mov eax, 1
00797D46  48 D3 E0                        shl rax, cl
00797D49  48 8B 0B                        mov rcx, qword ptr [rbx]
00797D4C  FF C8                           dec eax
00797D4E  23 43 08                        and eax, dword ptr [rbx + 8]
00797D51  EB 03                           jmp 0x140797d56
00797D53  41 8B C5                        mov eax, r13d
00797D56  0F BF 34 42                     movsx esi, word ptr [rdx + rax*2]
00797D5A  4C 8B C9                        mov r9, rcx
00797D5D  8B FE                           mov edi, esi
00797D5F  44 89 6D D0                     mov dword ptr [rbp - 0x30], r13d
00797D63  83 E7 0F                        and edi, 0xf
00797D66  48 85 C9                        test rcx, rcx
00797D69  0F 84 20 01 00 00               je 0x140797e8f
00797D6F  85 FF                           test edi, edi
00797D71  0F 84 18 01 00 00               je 0x140797e8f
00797D77  8B C7                           mov eax, edi
00797D79  48 3B C1                        cmp rax, rcx
00797D7C  76 02                           jbe 0x140797d80
00797D7E  8B 3B                           mov edi, dword ptr [rbx]
00797D80  8B 53 10                        mov edx, dword ptr [rbx + 0x10]
00797D83  3B D7                           cmp edx, edi
00797D85  73 26                           jae 0x140797dad
00797D87  48 8D 4B 18                     lea rcx, [rbx + 0x18]
00797D8B  45 8B C7                        mov r8d, r15d
00797D8E  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00797D92  E8 89 24 00 00                  call 0x14079a220
00797D97  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
00797D9A  8B 55 D0                        mov edx, dword ptr [rbp - 0x30]
00797D9D  48 D3 E2                        shl rdx, cl
00797DA0  48 09 53 08                     or qword ptr [rbx + 8], rdx
00797DA4  8D 14 C1                        lea edx, [rcx + rax*8]
00797DA7  3B D7                           cmp edx, edi
00797DA9  73 02                           jae 0x140797dad
00797DAB  8B FA                           mov edi, edx
00797DAD  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00797DB1  8B CF                           mov ecx, edi
00797DB3  48 29 0B                        sub qword ptr [rbx], rcx
00797DB6  48 D3 E8                        shr rax, cl
00797DB9  2B D7                           sub edx, edi
00797DBB  48 89 43 08                     mov qword ptr [rbx + 8], rax
00797DBF  89 53 10                        mov dword ptr [rbx + 0x10], edx
00797DC2  E9 C5 00 00 00                  jmp 0x140797e8c
00797DC7  44 89 6D D0                     mov dword ptr [rbp - 0x30], r13d
00797DCB  BF 06 00 00 00                  mov edi, 6
00797DD0  4D 85 C9                        test r9, r9
00797DD3  74 45                           je 0x140797e1a
00797DD5  4C 3B CF                        cmp r9, rdi
00797DD8  73 02                           jae 0x140797ddc
00797DDA  8B 3B                           mov edi, dword ptr [rbx]
00797DDC  39 7B 10                        cmp dword ptr [rbx + 0x10], edi
00797DDF  73 28                           jae 0x140797e09
00797DE1  48 8D 4B 18                     lea rcx, [rbx + 0x18]
00797DE5  45 8B C7                        mov r8d, r15d
00797DE8  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00797DEC  E8 2F 24 00 00                  call 0x14079a220
00797DF1  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
00797DF4  8B 55 D0                        mov edx, dword ptr [rbp - 0x30]
00797DF7  48 D3 E2                        shl rdx, cl
00797DFA  48 09 53 08                     or qword ptr [rbx + 8], rdx
00797DFE  8D 14 C1                        lea edx, [rcx + rax*8]
00797E01  3B D7                           cmp edx, edi
00797E03  89 53 10                        mov dword ptr [rbx + 0x10], edx
00797E06  0F 42 FA                        cmovb edi, edx
00797E09  8B CF                           mov ecx, edi
00797E0B  BA 01 00 00 00                  mov edx, 1
00797E10  48 D3 E2                        shl rdx, cl
00797E13  FF CA                           dec edx
00797E15  23 53 08                        and edx, dword ptr [rbx + 8]
00797E18  EB 03                           jmp 0x140797e1d
00797E1A  41 8B D5                        mov edx, r13d
00797E1D  48 8B 0B                        mov rcx, qword ptr [rbx]
00797E20  48 0F BF C6                     movsx rax, si
00797E24  4C 8B C9                        mov r9, rcx
00797E27  48 83 E0 F0                     and rax, 0xfffffffffffffff0
00797E2B  44 89 6D D0                     mov dword ptr [rbp - 0x30], r13d
00797E2F  4D 8D 34 46                     lea r14, [r14 + rax*2]
00797E33  8B C2                           mov eax, edx
00797E35  41 0F BF 34 46                  movsx esi, word ptr [r14 + rax*2]
00797E3A  8B FE                           mov edi, esi
00797E3C  83 E7 0F                        and edi, 0xf
00797E3F  48 85 C9                        test rcx, rcx
00797E42  74 4B                           je 0x140797e8f
00797E44  85 FF                           test edi, edi
00797E46  74 47                           je 0x140797e8f
00797E48  8B C7                           mov eax, edi
00797E4A  48 3B C1                        cmp rax, rcx
00797E4D  76 02                           jbe 0x140797e51
00797E4F  8B F9                           mov edi, ecx
00797E51  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
00797E54  3B C7                           cmp eax, edi
00797E56  73 26                           jae 0x140797e7e
00797E58  48 8D 4B 18                     lea rcx, [rbx + 0x18]
00797E5C  45 8B C7                        mov r8d, r15d
00797E5F  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00797E63  E8 B8 23 00 00                  call 0x14079a220
00797E68  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
00797E6B  8B 55 D0                        mov edx, dword ptr [rbp - 0x30]
00797E6E  48 D3 E2                        shl rdx, cl
00797E71  48 09 53 08                     or qword ptr [rbx + 8], rdx
00797E75  8D 04 C1                        lea eax, [rcx + rax*8]
00797E78  3B C7                           cmp eax, edi
00797E7A  73 02                           jae 0x140797e7e
00797E7C  8B F8                           mov edi, eax
00797E7E  8B CF                           mov ecx, edi
00797E80  48 D3 6B 08                     shr qword ptr [rbx + 8], cl
00797E84  48 29 0B                        sub qword ptr [rbx], rcx
00797E87  2B C7                           sub eax, edi
00797E89  89 43 10                        mov dword ptr [rbx + 0x10], eax
00797E8C  4C 8B 0B                        mov r9, qword ptr [rbx]
00797E8F  66 85 F6                        test si, si
00797E92  0F 88 2F FF FF FF               js 0x140797dc7
00797E98  66 C1 EE 04                     shr si, 4
00797E9C  40 0F B6 D6                     movzx edx, sil
00797EA0  40 80 FE E8                     cmp sil, 0xe8
00797EA4  0F 86 AA 00 00 00               jbe 0x140797f54
00797EAA  44 89 6D D0                     mov dword ptr [rbp - 0x30], r13d
00797EAE  8D B2 18 FF FF FF               lea esi, [rdx - 0xe8]
00797EB4  8B FE                           mov edi, esi
00797EB6  4D 85 C9                        test r9, r9
00797EB9  74 66                           je 0x140797f21
00797EBB  85 F6                           test esi, esi
00797EBD  74 62                           je 0x140797f21
00797EBF  8B C6                           mov eax, esi
00797EC1  49 3B C1                        cmp rax, r9
00797EC4  76 02                           jbe 0x140797ec8
00797EC6  8B 3B                           mov edi, dword ptr [rbx]
00797EC8  8B 53 10                        mov edx, dword ptr [rbx + 0x10]
00797ECB  3B D7                           cmp edx, edi
00797ECD  73 26                           jae 0x140797ef5
00797ECF  48 8D 4B 18                     lea rcx, [rbx + 0x18]
00797ED3  45 8B C7                        mov r8d, r15d
00797ED6  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00797EDA  E8 41 23 00 00                  call 0x14079a220
00797EDF  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
00797EE2  8B 55 D0                        mov edx, dword ptr [rbp - 0x30]
00797EE5  48 D3 E2                        shl rdx, cl
00797EE8  48 09 53 08                     or qword ptr [rbx + 8], rdx
00797EEC  8D 14 C1                        lea edx, [rcx + rax*8]
00797EEF  3B D7                           cmp edx, edi
00797EF1  73 02                           jae 0x140797ef5
00797EF3  8B FA                           mov edi, edx
00797EF5  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00797EF9  8B CF                           mov ecx, edi
00797EFB  41 BA 01 00 00 00               mov r10d, 1
00797F01  49 D3 E2                        shl r10, cl
00797F04  41 FF CA                        dec r10d
00797F07  8B CF                           mov ecx, edi
00797F09  44 23 53 08                     and r10d, dword ptr [rbx + 8]
00797F0D  48 29 0B                        sub qword ptr [rbx], rcx
00797F10  4C 8B 0B                        mov r9, qword ptr [rbx]
00797F13  48 D3 E8                        shr rax, cl
00797F16  2B D7                           sub edx, edi
00797F18  48 89 43 08                     mov qword ptr [rbx + 8], rax
00797F1C  89 53 10                        mov dword ptr [rbx + 0x10], edx
00797F1F  EB 06                           jmp 0x140797f27
00797F21  45 8B D5                        mov r10d, r13d
00797F24  41 8B FD                        mov edi, r13d
00797F27  3B FE                           cmp edi, esi
00797F29  0F 82 AD 01 00 00               jb 0x1407980dc
00797F2F  49 8B 04 24                     mov rax, qword ptr [r12]
00797F33  8B CE                           mov ecx, esi
00797F35  BA 01 00 00 00                  mov edx, 1
00797F3A  D3 E2                           shl edx, cl
00797F3C  44 0F B7 00                     movzx r8d, word ptr [rax]
00797F40  41 C1 E8 05                     shr r8d, 5
00797F44  41 83 E0 07                     and r8d, 7
00797F48  41 8D B0 F6 00 00 00            lea esi, [r8 + 0xf6]
00797F4F  41 03 F2                        add esi, r10d
00797F52  EB 10                           jmp 0x140797f64
00797F54  49 8B 04 24                     mov rax, qword ptr [r12]
00797F58  0F B7 30                        movzx esi, word ptr [rax]
00797F5B  C1 EE 05                        shr esi, 5
00797F5E  83 E6 07                        and esi, 7
00797F61  83 C6 0F                        add esi, 0xf
00797F64  44 0F B7 55 58                  movzx r10d, word ptr [rbp + 0x58]
00797F69  03 F2                           add esi, edx
00797F6B  EB 19                           jmp 0x140797f86
00797F6D  49 8B 04 24                     mov rax, qword ptr [r12]
00797F71  4C 8B C9                        mov r9, rcx
00797F74  0F B7 30                        movzx esi, word ptr [rax]
00797F77  C1 EE 05                        shr esi, 5
00797F7A  41 0F B7 C2                     movzx eax, r10w
00797F7E  83 E6 07                        and esi, 7
00797F81  83 E0 0F                        and eax, 0xf
00797F84  03 F0                           add esi, eax
00797F86  B9 40 01 00 00                  mov ecx, 0x140
00797F8B  41 0F B7 C2                     movzx eax, r10w
00797F8F  66 44 3B D1                     cmp r10w, cx
00797F93  73 31                           jae 0x140797fc6
00797F95  05 00 FF FF FF                  add eax, 0xffffff00
00797F9A  B9 10 00 00 00                  mov ecx, 0x10
00797F9F  99                              cdq
00797FA0  F7 F9                           idiv ecx
00797FA2  41 8B 7C 84 08                  mov edi, dword ptr [r12 + rax*4 + 8]
00797FA7  85 C0                           test eax, eax
00797FA9  0F 84 ED 00 00 00               je 0x14079809c
00797FAF  83 F8 03                        cmp eax, 3
00797FB2  0F 83 C1 00 00 00               jae 0x140798079
00797FB8  83 F8 02                        cmp eax, 2
00797FBB  0F 82 CC 00 00 00               jb 0x14079808d
00797FC1  E9 BD 00 00 00                  jmp 0x140798083
00797FC6  3B 45 D4                        cmp eax, dword ptr [rbp - 0x2c]
00797FC9  0F 83 0D 01 00 00               jae 0x1407980dc
00797FCF  B9 4F 01 00 00                  mov ecx, 0x14f
00797FD4  66 44 3B D1                     cmp r10w, cx
00797FD8  0F 86 96 00 00 00               jbe 0x140798074
00797FDE  05 C0 FE FF FF                  add eax, 0xfffffec0
00797FE3  44 89 6D 58                     mov dword ptr [rbp + 0x58], r13d
00797FE7  99                              cdq
00797FE8  B9 10 00 00 00                  mov ecx, 0x10
00797FED  F7 F9                           idiv ecx
00797FEF  44 8B F0                        mov r14d, eax
00797FF2  8B F8                           mov edi, eax
00797FF4  4D 85 C9                        test r9, r9
00797FF7  74 61                           je 0x14079805a
00797FF9  85 C0                           test eax, eax
00797FFB  74 5D                           je 0x14079805a
00797FFD  4D 3B F1                        cmp r14, r9
00798000  76 02                           jbe 0x140798004
00798002  8B 3B                           mov edi, dword ptr [rbx]
00798004  8B 53 10                        mov edx, dword ptr [rbx + 0x10]
00798007  3B D7                           cmp edx, edi
00798009  73 26                           jae 0x140798031
0079800B  48 8D 4B 18                     lea rcx, [rbx + 0x18]
0079800F  45 8B C7                        mov r8d, r15d
00798012  48 8D 55 58                     lea rdx, [rbp + 0x58]
00798016  E8 05 22 00 00                  call 0x14079a220
0079801B  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
0079801E  8B 55 58                        mov edx, dword ptr [rbp + 0x58]
00798021  48 D3 E2                        shl rdx, cl
00798024  48 09 53 08                     or qword ptr [rbx + 8], rdx
00798028  8D 14 C1                        lea edx, [rcx + rax*8]
0079802B  3B D7                           cmp edx, edi
0079802D  73 02                           jae 0x140798031
0079802F  8B FA                           mov edi, edx
00798031  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00798035  8B CF                           mov ecx, edi
00798037  41 B8 01 00 00 00               mov r8d, 1
0079803D  49 D3 E0                        shl r8, cl
00798040  41 FF C8                        dec r8d
00798043  8B CF                           mov ecx, edi
00798045  44 23 43 08                     and r8d, dword ptr [rbx + 8]
00798049  48 29 0B                        sub qword ptr [rbx], rcx
0079804C  48 D3 E8                        shr rax, cl
0079804F  2B D7                           sub edx, edi
00798051  48 89 43 08                     mov qword ptr [rbx + 8], rax
00798055  89 53 10                        mov dword ptr [rbx + 0x10], edx
00798058  EB 06                           jmp 0x140798060
0079805A  45 8B C5                        mov r8d, r13d
0079805D  41 8B FD                        mov edi, r13d
00798060  41 3B FE                        cmp edi, r14d
00798063  72 77                           jb 0x1407980dc
00798065  41 8B CE                        mov ecx, r14d
00798068  BF 01 00 00 00                  mov edi, 1
0079806D  D3 E7                           shl edi, cl
0079806F  41 03 F8                        add edi, r8d
00798072  EB 05                           jmp 0x140798079
00798074  BF 01 00 00 00                  mov edi, 1
00798079  41 8B 44 24 10                  mov eax, dword ptr [r12 + 0x10]
0079807E  41 89 44 24 14                  mov dword ptr [r12 + 0x14], eax
00798083  41 8B 44 24 0C                  mov eax, dword ptr [r12 + 0xc]
00798088  41 89 44 24 10                  mov dword ptr [r12 + 0x10], eax
0079808D  41 8B 44 24 08                  mov eax, dword ptr [r12 + 8]
00798092  41 89 7C 24 08                  mov dword ptr [r12 + 8], edi
00798097  41 89 44 24 0C                  mov dword ptr [r12 + 0xc], eax
0079809C  85 FF                           test edi, edi
0079809E  74 3C                           je 0x1407980dc
007980A0  4C 8B 7D 50                     mov r15, qword ptr [rbp + 0x50]
007980A4  3B F7                           cmp esi, edi
007980A6  76 17                           jbe 0x1407980bf
007980A8  44 8B C7                        mov r8d, edi
007980AB  8B D7                           mov edx, edi
007980AD  49 8B CF                        mov rcx, r15
007980B0  E8 BF 20 00 00                  call 0x14079a174
007980B5  3B C7                           cmp eax, edi
007980B7  75 23                           jne 0x1407980dc
007980B9  2B F7                           sub esi, edi
007980BB  03 FF                           add edi, edi
007980BD  EB E5                           jmp 0x1407980a4
007980BF  85 F6                           test esi, esi
007980C1  0F 84 14 FC FF FF               je 0x140797cdb
007980C7  44 8B C6                        mov r8d, esi
007980CA  8B D7                           mov edx, edi
007980CC  49 8B CF                        mov rcx, r15
007980CF  E8 A0 20 00 00                  call 0x14079a174
007980D4  3B C6                           cmp eax, esi
007980D6  0F 84 FF FB FF FF               je 0x140797cdb
007980DC  B8 42 02 00 C0                  mov eax, 0xc0000242
007980E1  48 8B 9C 24 B8 00 00 00         mov rbx, qword ptr [rsp + 0xb8]
007980E9  48 83 C4 70                     add rsp, 0x70
007980ED  41 5F                           pop r15
007980EF  41 5E                           pop r14
007980F1  41 5D                           pop r13
007980F3  41 5C                           pop r12
007980F5  5F                              pop rdi
007980F6  5E                              pop rsi
007980F7  5D                              pop rbp
007980F8  C3                              ret
007980F9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Xp10ExecuteHuffmanDecode(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (112);
    v_r13 = 0;
    v_stack_m60 = 0;
    v_stack_m50 = 0;
    v_stack_p20 = 0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1))))) & (31));
    a4 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1))) >> (5));
    a4 = (unsigned int)((a4) & (7));
    result = (unsigned int)((v_r13 + 1) << ((unsigned __int8)(a1)));
    result = (unsigned int)((result) - ((unsigned int)(a4)));
    result = (unsigned int)((result) - (246));
    a2 = (unsigned int)((a1 + 20) << (4));
    *(unsigned __int64 *)(v_rsp - 112) = v_stack_m50;
    v_rdi = (unsigned int)((result - 1) & ((unsigned int)(result)));
    v_stack_m64 = (unsigned int)(a2);
    *(unsigned __int64 *)(v_rsp - 128) = a1 + 4696;
    v_stack_m88 = a2;
    result = Xp10ReadAndDecodeHuffmanTables(a1, a2, a3, a4);
    if (sign_flag) goto loc_007980E1;
    v_stack_m70 = v_stack_m60;
    a2 = v_rsi + 1;
    if ((unsigned int)(v_rdi) == 0) { a2 = (unsigned int)(v_rsi); }
    v_stack_m80 = a1 + 21080;
    a2 = (unsigned int)((a2) + (232));
    v_stack_m88 = a2;
    result = Xp10ReadAndDecodeHuffmanTables(a1, a2, a3, a4);
    if (sign_flag) goto loc_007980E1;
loc_00797A9B:
    v_stack_m58 = a2 + 8;
    if (*(unsigned __int64 *)(a2) == 0) goto loc_007980E1;
    v_stack_m48 = v_stack_m50;
    v_stack_p20 = 0;
    v_rdi = 12;
    v_r14 = a2 + 8;
    if ((*(unsigned __int64 *)(a2)) < 12) {
        v_rdi = (unsigned int)(*(unsigned __int64 *)(a2));
        v_stack_m58 = a2 + 8;
        v_r14 = a2 + 8;
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)))) >= ((unsigned int)(v_rdi))) goto loc_00797B14;
    result = Xp10ScatteredReadBytes(a2 + 24, v_stack_p20, 4, a4);
    a2 = ((unsigned int)(v_stack_p20)) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 16))));
    *(unsigned int *)(a2 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)) + result * 8);
    v_r15 = v_r14;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)) + result * 8)) < ((unsigned int)(v_rdi))) {
        v_rdi = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)) + result * 8);
        a3 = a2 + 16;
        v_r15 = a2 + 8;
    }
    result = (1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi))));
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) & (*(unsigned int *)(v_r14)));
    v_stack_p20 = (unsigned __int16)((__int16)(*(unsigned __int16 *)(v_stack_m50 + result * 2)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((__int16)(*(unsigned __int16 *)(v_stack_m50 + result * 2))))) & (15));
    if (*(unsigned __int64 *)(a2) == 0) goto loc_00797BA7;
    if ((unsigned int)(v_rsi) == 0) goto loc_00797BA7;
    v_rdi = a2 + 16;
    v_r13 = v_r15;
    if (((unsigned int)((unsigned int)(v_rsi))) >= = (*(unsigned __int64 *)(a2))) {
        v_rsi = (unsigned int)(*(unsigned __int64 *)(a2));
        v_r13 = a2 + 8;
        v_rdi = a3;
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)) + result * 8)) >= ((unsigned int)(v_rsi))) goto loc_00797B98;
    result = Xp10ScatteredReadBytes(a2 + 24, v_stack_m68, 4, *(unsigned __int64 *)(a2));
    a2 = ((unsigned int)(v_stack_m68)) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi))));
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi)) + result * 8);
    v_r14 = v_r15;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi)) + result * 8)) < ((unsigned int)(v_rsi))) {
        v_rsi = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi)) + result * 8);
        v_r14 = v_r13;
    }
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi)) + result * 8) - ((unsigned int)(v_rsi)));
    *(unsigned int *)(v_rdi) = (unsigned int)(a2);
loc_00797BA7:
    v_r13 = 0;
    if (!sign_flag) goto loc_00797CA2;
loc_00797BBC:
    v_stack_m68 = 0;
    if (*(unsigned __int64 *)(a2) == 0) goto loc_00797C16;
    v_rsi = 6;
    if ((*(unsigned __int64 *)(a2)) < 6) {
        v_rsi = *(unsigned int *)(a2);
    }
    v_r10 = v_stack_p20;
    if ((*(unsigned int *)(v_rdi)) < ((unsigned int)(v_rsi))) {
        a1 = a2 + 24;
        a3 = (unsigned int)(v_r13 + 4);
        a2 = v_stack_m68;
        result = Xp10ScatteredReadBytes(a1, a2, a3, *(unsigned __int64 *)(a2));
        a1 = *(unsigned int *)(v_rdi);
        a2 = v_stack_m68;
        v_r10 = v_stack_p20;
        a2 = (a2) << ((unsigned __int8)(a1));
        a2 = a1 + result * 8;
        *(unsigned int *)(v_rdi) = (unsigned int)(a2);
        if (((unsigned int)(a2)) < ((unsigned int)(v_rsi))) { v_rsi = (unsigned int)(a2); }
    }
    a2 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rsi))));
    a2 = (unsigned int)((a2) - 1);
    a2 = (unsigned int)((a2) & (*(unsigned int *)(v_r14)));
    goto loc_00797C1C;
loc_00797C16:
loc_00797C1C:
    result = ((__int16)((unsigned __int16)(v_r10))) & (-16);
    v_stack_m68 = 0;
    v_stack_p20 = (unsigned __int16)((__int16)(*(unsigned __int16 *)(v_stack_m48 + result * 2 + 0 * 2)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((__int16)(*(unsigned __int16 *)(v_stack_m48 + result * 2 + 0 * 2))))) & (15));
    if (0 == 0) goto loc_00797C90;
    if ((unsigned int)(v_rsi) == 0) goto loc_00797C90;
    if (((unsigned int)((unsigned int)(v_rsi))) >= = 0) {
        v_rsi = *(unsigned int *)(a2);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi)))) >= ((unsigned int)(v_rsi))) goto loc_00797C81;
    result = Xp10ScatteredReadBytes(a2 + 24, v_stack_m68, (unsigned int)((unsigned int)(v_r13 + 4)), *(unsigned __int64 *)(a2));
    a2 = ((unsigned int)(v_stack_m68)) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi))));
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi)) + result * 8);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi)) + result * 8)) < ((unsigned int)(v_rsi))) {
        v_rsi = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi)) + result * 8);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi)) + result * 8) - ((unsigned int)(v_rsi)));
    *(unsigned int *)(v_rdi) = (unsigned int)(result);
loc_00797C90:
    if (sign_flag) goto loc_00797BBC;
loc_00797CA2:
    v_r10 = (unsigned __int16)((v_stack_p20) >> (4));
    v_stack_p20 = (unsigned __int16)(v_r10);
    if (((unsigned __int16)(v_r10)) >= 256) goto loc_00797CE8;
loc_00797CBB:
    if ((*(unsigned __int64 *)(v_stack_p18)) != (*(unsigned __int64 *)(v_stack_p18 + 8))) goto loc_00797CD5;
    result = Xp10ScatteredNextBuffer(v_stack_p18, a2, (unsigned int)((unsigned int)(v_r13 + 4)), *(unsigned __int64 *)(a2));
    if ((unsigned int)(result) != 0) goto loc_00797CBB;
    goto loc_007980DC;
loc_00797CD5:
    *(unsigned __int8 *)(result) = (unsigned __int8)(v_r10);
loc_00797CDB:
    goto loc_00797A9B;
loc_00797CE8:
    result = (unsigned __int8)(((unsigned __int8)(v_r10)) & (15));
    if (((unsigned __int8)(result)) != 15) goto loc_00797F6D;
    v_stack_m68 = 0;
    if (a2 + 8 == 0) goto loc_00797D53;
    v_rsi = 12;
    if ((a2 + 8) < 12) {
        v_rsi = *(unsigned int *)(a2);
    }
    if ((*(unsigned int *)(a2 + 16)) < ((unsigned int)(v_rsi))) {
        a1 = a2 + 24;
        a3 = (unsigned int)(v_stack_p18);
        a2 = v_stack_m68;
        result = Xp10ScatteredReadBytes(a1, a2, a3, *(unsigned __int64 *)(a2));
        a1 = *(unsigned int *)(a2 + 16);
        a2 = v_stack_m68;
        a2 = (a2) << ((unsigned __int8)(a1));
        a2 = v_stack_m60;
        result = a1 + result * 8;
        *(unsigned int *)(a2 + 16) = (unsigned int)(result);
        if (((unsigned int)(result)) < ((unsigned int)(v_rsi))) { v_rsi = (unsigned int)(result); }
    }
    result = (1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rsi))));
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) & (*(unsigned int *)(a2 + 8)));
    goto loc_00797D56;
loc_00797D53:
loc_00797D56:
    v_stack_m68 = 0;
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)((__int16)(*(unsigned __int16 *)(a2 + 0 * 2))))) & (15));
    if (*(unsigned __int64 *)(a2) == 0) goto loc_00797E8F;
    if ((unsigned int)(v_rdi) == 0) goto loc_00797E8F;
    if (((unsigned int)((unsigned int)(v_rdi))) >= = (*(unsigned __int64 *)(a2))) {
        v_rdi = *(unsigned int *)(a2);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)))) >= ((unsigned int)(v_rdi))) goto loc_00797DAD;
    result = Xp10ScatteredReadBytes(a2 + 24, v_stack_m68, (unsigned int)((unsigned int)(v_stack_p18)), *(unsigned __int64 *)(a2));
    a2 = ((unsigned int)(v_stack_m68)) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 16))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)) + result * 8)) < ((unsigned int)(v_rdi))) {
        v_rdi = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)) + result * 8);
    }
    result = (*(unsigned __int64 *)(a2 + 8)) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi))));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16)) + result * 8) - ((unsigned int)(v_rdi)));
    *(unsigned __int64 *)(a2 + 8) = result;
    *(unsigned int *)(a2 + 16) = (unsigned int)(a2);
    goto loc_00797E8C;
loc_00797DC7:
    v_stack_m68 = 0;
    if (*(unsigned __int64 *)(a2) == 0) goto loc_00797E1A;
    v_rdi = 6;
    if ((*(unsigned __int64 *)(a2)) < 6) {
        v_rdi = *(unsigned int *)(a2);
    }
    if ((*(unsigned int *)(a2 + 16)) < ((unsigned int)(v_rdi))) {
        a1 = a2 + 24;
        a3 = (unsigned int)(v_stack_p18);
        a2 = v_stack_m68;
        result = Xp10ScatteredReadBytes(a1, a2, a3, *(unsigned __int64 *)(a2));
        a1 = *(unsigned int *)(a2 + 16);
        a2 = v_stack_m68;
        a2 = (a2) << ((unsigned __int8)(a1));
        a2 = a1 + result * 8;
        *(unsigned int *)(a2 + 16) = (unsigned int)(a2);
        if (((unsigned int)(a2)) < ((unsigned int)(v_rdi))) { v_rdi = (unsigned int)(a2); }
    }
    a2 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi))));
    a2 = (unsigned int)((a2) - 1);
    a2 = (unsigned int)((a2) & (*(unsigned int *)(a2 + 8)));
    goto loc_00797E1D;
loc_00797E1A:
loc_00797E1D:
    result = ((__int16)((unsigned __int16)((__int16)(*(unsigned __int16 *)(a2 + 0 * 2))))) & (-16);
    v_stack_m68 = 0;
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)((__int16)(*(unsigned __int16 *)(v_stack_m60 + result * 2 + 0 * 2))))) & (15));
    if (*(unsigned __int64 *)(a2) == 0) goto loc_00797E8F;
    if ((unsigned int)(v_rdi) == 0) goto loc_00797E8F;
    if (((unsigned int)((unsigned int)(v_rdi))) >= = (*(unsigned __int64 *)(a2))) {
        v_rdi = (unsigned int)(*(unsigned __int64 *)(a2));
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)))) >= ((unsigned int)(v_rdi))) goto loc_00797E7E;
    result = Xp10ScatteredReadBytes(a2 + 24, v_stack_m68, (unsigned int)((unsigned int)(v_stack_p18)), *(unsigned __int64 *)(a2));
    a2 = ((unsigned int)(v_stack_m68)) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 16))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)) + result * 8)) < ((unsigned int)(v_rdi))) {
        v_rdi = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)) + result * 8);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16)) + result * 8) - ((unsigned int)(v_rdi)));
    *(unsigned int *)(a2 + 16) = (unsigned int)(result);
loc_00797E8C:
loc_00797E8F:
    if (sign_flag) goto loc_00797DC7;
    v_rsi = (unsigned __int16)(((__int16)(*(unsigned __int16 *)(v_stack_m60 + result * 2 + 0 * 2))) >> (4));
    if (((unsigned __int8)(v_rsi)) <= 232) goto loc_00797F54;
    v_stack_m68 = 0;
    if (*(unsigned __int64 *)(a2) == 0) goto loc_00797F21;
    if ((unsigned int)((unsigned __int8)(v_rsi) - 232) == 0) goto loc_00797F21;
    v_rdi = (unsigned int)((unsigned int)((unsigned __int8)(v_rsi) - 232));
    if (((unsigned int)((unsigned int)((unsigned __int8)(v_rsi) - 232))) >= = (*(unsigned __int64 *)(a2))) {
        v_rdi = *(unsigned int *)(a2);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)))) >= ((unsigned int)(v_rdi))) goto loc_00797EF5;
    result = Xp10ScatteredReadBytes(a2 + 24, v_stack_m68, (unsigned int)((unsigned int)(v_stack_p18)), *(unsigned __int64 *)(a2));
    a2 = ((unsigned int)(v_stack_m68)) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 16))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)) + result * 8)) < ((unsigned int)(v_rdi))) {
        v_rdi = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)) + result * 8);
    }
    v_r10 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi))));
    v_r10 = (unsigned int)((v_r10) - 1);
    v_r10 = (unsigned int)((v_r10) & (*(unsigned int *)(a2 + 8)));
    result = (*(unsigned __int64 *)(a2 + 8)) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi))));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16)) + result * 8) - ((unsigned int)(v_rdi)));
    *(unsigned __int64 *)(a2 + 8) = result;
    *(unsigned int *)(a2 + 16) = (unsigned int)(a2);
    goto loc_00797F27;
loc_00797F21:
loc_00797F27:
    if (0 < ((unsigned int)((unsigned __int8)(v_rsi) - 232))) goto loc_007980DC;
    a2 = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned __int8)(v_rsi) - 232)))));
    a3 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8))) >> (5));
    a3 = (unsigned int)((a3) & (7));
    v_rsi = (unsigned int)((a3 + 246) + (0));
    goto loc_00797F64;
loc_00797F54:
    v_rsi = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8))) >> (5));
    v_rsi = (unsigned int)((v_rsi) & (7));
    v_rsi = (unsigned int)((v_rsi) + (15));
loc_00797F64:
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(a2)));
    goto loc_00797F86;
loc_00797F6D:
    v_rsi = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8))) >> (5));
    v_rsi = (unsigned int)((v_rsi) & (7));
    result = (unsigned int)(((unsigned __int16)(v_stack_p20)) & (15));
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(result)));
loc_00797F86:
    if (((unsigned __int16)(v_stack_p20)) >= 320) goto loc_00797FC6;
    result = (unsigned int)(((unsigned __int16)(v_stack_p20)) + (0xFFFFFF00ULL));
    if ((unsigned int)(result) == 0) goto loc_0079809C;
    if (((unsigned int)(result)) >= 3) goto loc_00798079;
    if (((unsigned int)(result)) < 2) goto loc_0079808D;
    goto loc_00798083;
loc_00797FC6:
    if (((unsigned int)(result)) >= v_stack_m64) goto loc_007980DC;
    if (((unsigned __int16)(v_stack_p20)) <= 335) goto loc_00798074;
    result = (unsigned int)((result) + (0xFFFFFEC0ULL));
    v_stack_p20 = 0;
    if ((unsigned int)((unsigned int)((unsigned __int8)(v_rsi) - 232)) == 0) goto loc_0079805A;
    if ((unsigned int)(result) == 0) goto loc_0079805A;
    v_rdi = (unsigned int)((unsigned int)(result));
    if (((unsigned int)((unsigned int)(result))) >= = ((unsigned int)((unsigned int)((unsigned __int8)(v_rsi) - 232)))) {
        v_rdi = *(unsigned int *)(a2);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)))) >= ((unsigned int)(v_rdi))) goto loc_00798031;
    result = Xp10ScatteredReadBytes(a2 + 24, v_stack_p20, (unsigned int)((unsigned int)(v_stack_p18)), (unsigned int)((unsigned int)((unsigned __int8)(v_rsi) - 232)));
    a2 = ((unsigned int)(v_stack_p20)) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 16))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)) + result * 8)) < ((unsigned int)(v_rdi))) {
        v_rdi = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16)) + result * 8);
    }
    a3 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi))));
    a3 = (unsigned int)((a3) - 1);
    a3 = (unsigned int)((a3) & (*(unsigned int *)(a2 + 8)));
    result = (*(unsigned __int64 *)(a2 + 8)) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi))));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16)) + result * 8) - ((unsigned int)(v_rdi)));
    *(unsigned __int64 *)(a2 + 8) = result;
    *(unsigned int *)(a2 + 16) = (unsigned int)(a2);
    goto loc_00798060;
loc_0079805A:
loc_00798060:
    if (0 < ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_007980DC;
    v_rdi = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))))));
    v_rdi = (unsigned int)((v_rdi) + (0));
    goto loc_00798079;
loc_00798074:
loc_00798079:
    *(unsigned int *)(v_stack_p8 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 16)));
loc_00798083:
    *(unsigned int *)(v_stack_p8 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 12)));
loc_0079808D:
    *(unsigned int *)(v_stack_p8 + 8) = 1;
    *(unsigned int *)(v_stack_p8 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 8)));
loc_0079809C:
    if (1 == 0) goto loc_007980DC;
loc_007980A4:
    if (((unsigned int)(v_rsi)) <= 1) goto loc_007980BF;
    result = Xp10ScatteredCopyFromPrevious(v_stack_p18, 1, 1, (unsigned int)((unsigned int)((unsigned __int8)(v_rsi) - 232)));
    if (((unsigned int)(result)) != 1) goto loc_007980DC;
    v_rsi = (unsigned int)((v_rsi) - (1));
    v_rdi = (unsigned int)((1) + (1));
    goto loc_007980A4;
loc_007980BF:
    if ((unsigned int)(v_rsi) == 0) goto loc_00797CDB;
    result = Xp10ScatteredCopyFromPrevious(v_stack_p18, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)(v_rsi)), (unsigned int)((unsigned int)((unsigned __int8)(v_rsi) - 232)));
    if (((unsigned int)(result)) == ((unsigned int)(v_rsi))) goto loc_00797CDB;
loc_007980DC:
loc_007980E1:
    v_rsp = (v_rsp) + (112);
    return (unsigned int)(0xC0000242ULL);
}
```

## 5. (Beta) C Style

```c
int64_t Xp10ExecuteHuffmanDecode(void *Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (112);
    local_r13 = 0;
    v_stack_m60 = 0;
    v_stack_m50 = 0;
    v_stack_p20 = 0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(arg1))))) & (31));
    a4 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(arg1))) >> (5));
    a4 = (uint32_t)((a4) & (7));
    result = (uint32_t)((local_r13 + 1) << ((uint8_t)(Arg1)));
    result = (uint32_t)((result) - ((uint32_t)(a4)));
    result = (uint32_t)((result) - (246));
    Arg2 = (uint32_t)((Arg1 + 20) << (4));
    *(uint64_t *)(local_rsp - 0x70) = v_stack_m50;
    local_rdi = (uint32_t)((result - 1) & ((uint32_t)(result)));
    v_stack_m64 = (uint32_t)(Arg2);
    *(void **)(local_rsp - 0x80) = Arg1 + 4696;
    v_stack_m88 = Arg2;
    result = Xp10ReadAndDecodeHuffmanTables(Arg1, Arg2, Arg3, a4);
    if (sign_flag) goto loc_007980E1;
    v_stack_m70 = v_stack_m60;
    Arg2 = local_rsi + 1;
    if ((uint32_t)(local_rdi) == 0) { Arg2 = (uint32_t)(local_rsi); }
    v_stack_m80 = Arg1 + 21080;
    Arg2 = (uint32_t)((Arg2) + (232));
    v_stack_m88 = Arg2;
    result = Xp10ReadAndDecodeHuffmanTables(Arg1, Arg2, Arg3, a4);
    if (sign_flag) goto loc_007980E1;
loc_00797A9B:
    v_stack_m58 = Arg2 + 8;
    if (*(uint64_t *)(arg2) == 0) goto loc_007980E1;
    v_stack_m48 = v_stack_m50;
    v_stack_p20 = 0;
    local_rdi = 12;
    local_r14 = Arg2 + 8;
    if ((*(uint64_t *)(arg2)) < 12) {
        local_rdi = (uint32_t)(*(uint64_t *)(arg2));
        v_stack_m58 = Arg2 + 8;
        local_r14 = Arg2 + 8;
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)))) >= ((uint32_t)(local_rdi))) goto loc_00797B14;
    result = Xp10ScatteredReadBytes(Arg2 + 24, v_stack_p20, 4, a4);
    Arg2 = ((uint32_t)(v_stack_p20)) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10))));
    *(uint32_t *)(arg2 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)) + result * 8);
    local_r15 = local_r14;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)) + result * 8)) < ((uint32_t)(local_rdi))) {
        local_rdi = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)) + result * 8);
        Arg3 = Arg2 + 16;
        local_r15 = Arg2 + 8;
    }
    result = (1) << ((uint8_t)((uint32_t)((uint32_t)(local_rdi))));
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) & (*(uint32_t *)(local_r14)));
    v_stack_p20 = (uint16_t)((int16_t)(*(uint16_t *)(v_stack_m50 + result * 2)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((int16_t)(*(uint16_t *)(v_stack_m50 + result * 2))))) & (15));
    if (*(uint64_t *)(arg2) == 0) goto loc_00797BA7;
    if ((uint32_t)(local_rsi) == 0) goto loc_00797BA7;
    local_rdi = Arg2 + 16;
    local_r13 = local_r15;
    if (((uint32_t)((uint32_t)(local_rsi))) >= = (*(uint64_t *)(arg2))) {
        local_rsi = (uint32_t)(*(uint64_t *)(arg2));
        local_r13 = Arg2 + 8;
        local_rdi = Arg3;
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)) + result * 8)) >= ((uint32_t)(local_rsi))) goto loc_00797B98;
    result = Xp10ScatteredReadBytes(Arg2 + 24, v_stack_m68, 4, *(uint64_t *)(arg2));
    Arg2 = ((uint32_t)(v_stack_m68)) << ((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi))));
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi)) + result * 8);
    local_r14 = local_r15;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi)) + result * 8)) < ((uint32_t)(local_rsi))) {
        local_rsi = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi)) + result * 8);
        local_r14 = local_r13;
    }
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi)) + result * 8) - ((uint32_t)(local_rsi)));
    *(uint32_t *)(local_rdi) = (uint32_t)(Arg2);
loc_00797BA7:
    local_r13 = 0;
    if (!sign_flag) goto loc_00797CA2;
loc_00797BBC:
    v_stack_m68 = 0;
    if (*(uint64_t *)(arg2) == 0) goto loc_00797C16;
    local_rsi = 6;
    if ((*(uint64_t *)(arg2)) < 6) {
        local_rsi = *(uint32_t *)(arg2);
    }
    local_r10 = v_stack_p20;
    if ((*(uint32_t *)(local_rdi)) < ((uint32_t)(local_rsi))) {
        Arg1 = Arg2 + 24;
        Arg3 = (uint32_t)(local_r13 + 4);
        Arg2 = v_stack_m68;
        result = Xp10ScatteredReadBytes(Arg1, Arg2, Arg3, *(uint64_t *)(arg2));
        Arg1 = *(uint32_t *)(local_rdi);
        Arg2 = v_stack_m68;
        local_r10 = v_stack_p20;
        Arg2 = (Arg2) << ((uint8_t)(Arg1));
        Arg2 = Arg1 + result * 8;
        *(uint32_t *)(local_rdi) = (uint32_t)(Arg2);
        if (((uint32_t)(Arg2)) < ((uint32_t)(local_rsi))) { local_rsi = (uint32_t)(Arg2); }
    }
    Arg2 = (1) << ((uint8_t)((uint32_t)((uint32_t)(local_rsi))));
    Arg2 = (uint32_t)((Arg2) - 1);
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(local_r14)));
    goto loc_00797C1C;
loc_00797C16:
loc_00797C1C:
    result = ((int16_t)((uint16_t)(local_r10))) & (-16);
    v_stack_m68 = 0;
    v_stack_p20 = (uint16_t)((int16_t)(*(uint16_t *)(v_stack_m48 + result * 2 + 0x0 * 2)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((int16_t)(*(uint16_t *)(v_stack_m48 + result * 2 + 0x0 * 2))))) & (15));
    if (0 == 0) goto loc_00797C90;
    if ((uint32_t)(local_rsi) == 0) goto loc_00797C90;
    if (((uint32_t)((uint32_t)(local_rsi))) >= = 0) {
        local_rsi = *(uint32_t *)(arg2);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi)))) >= ((uint32_t)(local_rsi))) goto loc_00797C81;
    result = Xp10ScatteredReadBytes(Arg2 + 24, v_stack_m68, (uint32_t)((uint32_t)(local_r13 + 4)), *(uint64_t *)(arg2));
    Arg2 = ((uint32_t)(v_stack_m68)) << ((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi))));
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi)) + result * 8);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi)) + result * 8)) < ((uint32_t)(local_rsi))) {
        local_rsi = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi)) + result * 8);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi)) + result * 8) - ((uint32_t)(local_rsi)));
    *(uint32_t *)(local_rdi) = (uint32_t)(result);
loc_00797C90:
    if (sign_flag) goto loc_00797BBC;
loc_00797CA2:
    local_r10 = (uint16_t)((v_stack_p20) >> (4));
    v_stack_p20 = (uint16_t)(local_r10);
    if (((uint16_t)(local_r10)) >= 256) goto loc_00797CE8;
loc_00797CBB:
    if ((*(uint64_t *)(v_stack_p18)) != (*(uint64_t *)(v_stack_p18 + 0x8))) goto loc_00797CD5;
    result = Xp10ScatteredNextBuffer(v_stack_p18, Arg2, (uint32_t)((uint32_t)(local_r13 + 4)), *(uint64_t *)(arg2));
    if ((uint32_t)(result) != 0) goto loc_00797CBB;
    goto loc_007980DC;
loc_00797CD5:
    *(uint8_t *)(result) = (uint8_t)(local_r10);
loc_00797CDB:
    goto loc_00797A9B;
loc_00797CE8:
    result = (uint8_t)(((uint8_t)(local_r10)) & (15));
    if (((uint8_t)(result)) != 15) goto loc_00797F6D;
    v_stack_m68 = 0;
    if (Arg2 + 8 == 0) goto loc_00797D53;
    local_rsi = 12;
    if ((Arg2 + 8) < 12) {
        local_rsi = *(uint32_t *)(arg2);
    }
    if ((*(uint32_t *)(arg2 + 0x10)) < ((uint32_t)(local_rsi))) {
        Arg1 = Arg2 + 24;
        Arg3 = (uint32_t)(v_stack_p18);
        Arg2 = v_stack_m68;
        result = Xp10ScatteredReadBytes(Arg1, Arg2, Arg3, *(uint64_t *)(arg2));
        Arg1 = *(uint32_t *)(arg2 + 0x10);
        Arg2 = v_stack_m68;
        Arg2 = (Arg2) << ((uint8_t)(Arg1));
        Arg2 = v_stack_m60;
        result = Arg1 + result * 8;
        *(uint32_t *)(arg2 + 0x10) = (uint32_t)(result);
        if (((uint32_t)(result)) < ((uint32_t)(local_rsi))) { local_rsi = (uint32_t)(result); }
    }
    result = (1) << ((uint8_t)((uint32_t)((uint32_t)(local_rsi))));
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) & (*(uint32_t *)(arg2 + 0x8)));
    goto loc_00797D56;
loc_00797D53:
loc_00797D56:
    v_stack_m68 = 0;
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)((int16_t)(*(uint16_t *)(arg2 + 0x0 * 2))))) & (15));
    if (*(uint64_t *)(arg2) == 0) goto loc_00797E8F;
    if ((uint32_t)(local_rdi) == 0) goto loc_00797E8F;
    if (((uint32_t)((uint32_t)(local_rdi))) >= = (*(uint64_t *)(arg2))) {
        local_rdi = *(uint32_t *)(arg2);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)))) >= ((uint32_t)(local_rdi))) goto loc_00797DAD;
    result = Xp10ScatteredReadBytes(Arg2 + 24, v_stack_m68, (uint32_t)((uint32_t)(v_stack_p18)), *(uint64_t *)(arg2));
    Arg2 = ((uint32_t)(v_stack_m68)) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)) + result * 8)) < ((uint32_t)(local_rdi))) {
        local_rdi = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)) + result * 8);
    }
    result = (*(uint64_t *)(arg2 + 0x8)) >> ((uint8_t)((uint32_t)((uint32_t)(local_rdi))));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x10)) + result * 8) - ((uint32_t)(local_rdi)));
    *(uint64_t *)(arg2 + 0x8) = result;
    *(uint32_t *)(arg2 + 0x10) = (uint32_t)(Arg2);
    goto loc_00797E8C;
loc_00797DC7:
    v_stack_m68 = 0;
    if (*(uint64_t *)(arg2) == 0) goto loc_00797E1A;
    local_rdi = 6;
    if ((*(uint64_t *)(arg2)) < 6) {
        local_rdi = *(uint32_t *)(arg2);
    }
    if ((*(uint32_t *)(arg2 + 0x10)) < ((uint32_t)(local_rdi))) {
        Arg1 = Arg2 + 24;
        Arg3 = (uint32_t)(v_stack_p18);
        Arg2 = v_stack_m68;
        result = Xp10ScatteredReadBytes(Arg1, Arg2, Arg3, *(uint64_t *)(arg2));
        Arg1 = *(uint32_t *)(arg2 + 0x10);
        Arg2 = v_stack_m68;
        Arg2 = (Arg2) << ((uint8_t)(Arg1));
        Arg2 = Arg1 + result * 8;
        *(uint32_t *)(arg2 + 0x10) = (uint32_t)(Arg2);
        if (((uint32_t)(Arg2)) < ((uint32_t)(local_rdi))) { local_rdi = (uint32_t)(Arg2); }
    }
    Arg2 = (1) << ((uint8_t)((uint32_t)((uint32_t)(local_rdi))));
    Arg2 = (uint32_t)((Arg2) - 1);
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(arg2 + 0x8)));
    goto loc_00797E1D;
loc_00797E1A:
loc_00797E1D:
    result = ((int16_t)((uint16_t)((int16_t)(*(uint16_t *)(arg2 + 0x0 * 2))))) & (-16);
    v_stack_m68 = 0;
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)((int16_t)(*(uint16_t *)(v_stack_m60 + result * 2 + 0x0 * 2))))) & (15));
    if (*(uint64_t *)(arg2) == 0) goto loc_00797E8F;
    if ((uint32_t)(local_rdi) == 0) goto loc_00797E8F;
    if (((uint32_t)((uint32_t)(local_rdi))) >= = (*(uint64_t *)(arg2))) {
        local_rdi = (uint32_t)(*(uint64_t *)(arg2));
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)))) >= ((uint32_t)(local_rdi))) goto loc_00797E7E;
    result = Xp10ScatteredReadBytes(Arg2 + 24, v_stack_m68, (uint32_t)((uint32_t)(v_stack_p18)), *(uint64_t *)(arg2));
    Arg2 = ((uint32_t)(v_stack_m68)) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)) + result * 8)) < ((uint32_t)(local_rdi))) {
        local_rdi = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)) + result * 8);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x10)) + result * 8) - ((uint32_t)(local_rdi)));
    *(uint32_t *)(arg2 + 0x10) = (uint32_t)(result);
loc_00797E8C:
loc_00797E8F:
    if (sign_flag) goto loc_00797DC7;
    local_rsi = (uint16_t)(((int16_t)(*(uint16_t *)(v_stack_m60 + result * 2 + 0x0 * 2))) >> (4));
    if (((uint8_t)(local_rsi)) <= 232) goto loc_00797F54;
    v_stack_m68 = 0;
    if (*(uint64_t *)(arg2) == 0) goto loc_00797F21;
    if ((uint32_t)((uint8_t)(local_rsi) - 232) == 0) goto loc_00797F21;
    local_rdi = (uint32_t)((uint32_t)((uint8_t)(local_rsi) - 232));
    if (((uint32_t)((uint32_t)((uint8_t)(local_rsi) - 232))) >= = (*(uint64_t *)(arg2))) {
        local_rdi = *(uint32_t *)(arg2);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)))) >= ((uint32_t)(local_rdi))) goto loc_00797EF5;
    result = Xp10ScatteredReadBytes(Arg2 + 24, v_stack_m68, (uint32_t)((uint32_t)(v_stack_p18)), *(uint64_t *)(arg2));
    Arg2 = ((uint32_t)(v_stack_m68)) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)) + result * 8)) < ((uint32_t)(local_rdi))) {
        local_rdi = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)) + result * 8);
    }
    local_r10 = (1) << ((uint8_t)((uint32_t)((uint32_t)(local_rdi))));
    local_r10 = (uint32_t)((local_r10) - 1);
    local_r10 = (uint32_t)((local_r10) & (*(uint32_t *)(arg2 + 0x8)));
    result = (*(uint64_t *)(arg2 + 0x8)) >> ((uint8_t)((uint32_t)((uint32_t)(local_rdi))));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x10)) + result * 8) - ((uint32_t)(local_rdi)));
    *(uint64_t *)(arg2 + 0x8) = result;
    *(uint32_t *)(arg2 + 0x10) = (uint32_t)(Arg2);
    goto loc_00797F27;
loc_00797F21:
loc_00797F27:
    if (0 < ((uint32_t)((uint8_t)(local_rsi) - 232))) goto loc_007980DC;
    Arg2 = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)((uint8_t)(local_rsi) - 232)))));
    Arg3 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_stack_p8))) >> (5));
    Arg3 = (uint32_t)((Arg3) & (7));
    local_rsi = (uint32_t)((Arg3 + 246) + (0));
    goto loc_00797F64;
loc_00797F54:
    local_rsi = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_stack_p8))) >> (5));
    local_rsi = (uint32_t)((local_rsi) & (7));
    local_rsi = (uint32_t)((local_rsi) + (15));
loc_00797F64:
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(Arg2)));
    goto loc_00797F86;
loc_00797F6D:
    local_rsi = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_stack_p8))) >> (5));
    local_rsi = (uint32_t)((local_rsi) & (7));
    result = (uint32_t)(((uint16_t)(v_stack_p20)) & (15));
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(result)));
loc_00797F86:
    if (((uint16_t)(v_stack_p20)) >= 320) goto loc_00797FC6;
    result = (uint32_t)(((uint16_t)(v_stack_p20)) + (0xFFFFFF00ULL));
    if ((uint32_t)(result) == 0) goto loc_0079809C;
    if (((uint32_t)(result)) >= 3) goto loc_00798079;
    if (((uint32_t)(result)) < 2) goto loc_0079808D;
    goto loc_00798083;
loc_00797FC6:
    if (((uint32_t)(result)) >= v_stack_m64) goto loc_007980DC;
    if (((uint16_t)(v_stack_p20)) <= 335) goto loc_00798074;
    result = (uint32_t)((result) + (0xFFFFFEC0ULL));
    v_stack_p20 = 0;
    if ((uint32_t)((uint32_t)((uint8_t)(local_rsi) - 232)) == 0) goto loc_0079805A;
    if ((uint32_t)(result) == 0) goto loc_0079805A;
    local_rdi = (uint32_t)((uint32_t)(result));
    if (((uint32_t)((uint32_t)(result))) >= = ((uint32_t)((uint32_t)((uint8_t)(local_rsi) - 232)))) {
        local_rdi = *(uint32_t *)(arg2);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)))) >= ((uint32_t)(local_rdi))) goto loc_00798031;
    result = Xp10ScatteredReadBytes(Arg2 + 24, v_stack_p20, (uint32_t)((uint32_t)(v_stack_p18)), (uint32_t)((uint32_t)((uint8_t)(local_rsi) - 232)));
    Arg2 = ((uint32_t)(v_stack_p20)) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)) + result * 8)) < ((uint32_t)(local_rdi))) {
        local_rdi = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10)) + result * 8);
    }
    Arg3 = (1) << ((uint8_t)((uint32_t)((uint32_t)(local_rdi))));
    Arg3 = (uint32_t)((Arg3) - 1);
    Arg3 = (uint32_t)((Arg3) & (*(uint32_t *)(arg2 + 0x8)));
    result = (*(uint64_t *)(arg2 + 0x8)) >> ((uint8_t)((uint32_t)((uint32_t)(local_rdi))));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x10)) + result * 8) - ((uint32_t)(local_rdi)));
    *(uint64_t *)(arg2 + 0x8) = result;
    *(uint32_t *)(arg2 + 0x10) = (uint32_t)(Arg2);
    goto loc_00798060;
loc_0079805A:
loc_00798060:
    if (0 < ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_007980DC;
    local_rdi = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))))));
    local_rdi = (uint32_t)((local_rdi) + (0));
    goto loc_00798079;
loc_00798074:
loc_00798079:
    *(uint32_t *)(v_stack_p8 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10)));
loc_00798083:
    *(uint32_t *)(v_stack_p8 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xC)));
loc_0079808D:
    *(uint32_t *)(v_stack_p8 + 0x8) = 1;
    *(uint32_t *)(v_stack_p8 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x8)));
loc_0079809C:
    if (1 == 0) goto loc_007980DC;
loc_007980A4:
    if (((uint32_t)(local_rsi)) <= 1) goto loc_007980BF;
    result = Xp10ScatteredCopyFromPrevious(v_stack_p18, 1, 1, (uint32_t)((uint32_t)((uint8_t)(local_rsi) - 232)));
    if (((uint32_t)(result)) != 1) goto loc_007980DC;
    local_rsi = (uint32_t)((local_rsi) - (1));
    local_rdi = (uint32_t)((1) + (1));
    goto loc_007980A4;
loc_007980BF:
    if ((uint32_t)(local_rsi) == 0) goto loc_00797CDB;
    result = Xp10ScatteredCopyFromPrevious(v_stack_p18, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)(local_rsi)), (uint32_t)((uint32_t)((uint8_t)(local_rsi) - 232)));
    if (((uint32_t)(result)) == ((uint32_t)(local_rsi))) goto loc_00797CDB;
loc_007980DC:
loc_007980E1:
    local_rsp = (local_rsp) + (112);
    return (uint32_t)(0xC0000242ULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x1258` | `64` | `R` |
| `Arg1` | `+ 0x5258` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R/W` |
| `Arg2` | `+ 0x8` | `32` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R/W` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x10` | `32` | `W` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007979C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
