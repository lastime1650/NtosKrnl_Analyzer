# woutput_l

- RVA: `0x0050293C`–`0x00503242` (길이 `2,310` bytes)
- VA: `0x000000014050293C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D6F18`
- 디코드: `610`개 명령, `2,310/2,310` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **8**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x005029A7` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00502C3C` → [mbtowc](mbtowc_function_005008E0.md) (function, `0x005008E0`)
- `0x00502E8A` → [write_multi_char](write_multi_char_function_0050329C.md) (function, `0x0050329C`)
- `0x00502EA1` → [write_string](write_string_function_005032F4.md) (function, `0x005032F4`)
- `0x00502EC0` → [write_multi_char](write_multi_char_function_0050329C.md) (function, `0x0050329C`)
- `0x00502EE6` → [mbtowc](mbtowc_function_005008E0.md) (function, `0x005008E0`)
- `0x00502F13` → [write_char](write_char_function_00503248.md) (function, `0x00503248`)
- `0x00502F51` → [write_string](write_string_function_005032F4.md) (function, `0x005032F4`)
- `0x00502F79` → [write_multi_char](write_multi_char_function_0050329C.md) (function, `0x0050329C`)
- `0x00502FBC` → [get_printf_count_output](get_printf_count_output_function_00504494.md) (function, `0x00504494`)
- `0x005030EA` → [write_char](write_char_function_00503248.md) (function, `0x00503248`)
- `0x0050320F` → [EmpCheckErrataList](../49/EmpCheckErrataList_function_0049E550.md) (function, `0x0049E550`)
- `0x00503221` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [vsnwprintf_l](../4F/vsnwprintf_l_function_004FEF50.md) at `0x004FEFC7`
- [snwprintf](../4F/snwprintf_function_004FFC40.md) at `0x004FFCB6`
- [swprintf](../4F/swprintf_function_004FFED0.md) at `0x004FFF23`
- [vswprintf_l](../4F/vswprintf_l_function_004FFFBC.md) at `0x004FFFFD`

### Static image references
- `0x0050295B` → RVA `0x00E0A740` (`.data`; read)
- `0x00502A12` → RVA `0x0001EFA0` (`.rdata`; read)
- `0x00502B66` → RVA `0x0001EF98` (`.rdata`; read)
- `0x00502C23` → RVA `0x00E0A700` (`.data`; read)
- `0x00502CA7` → RVA `0x0002AEF8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0050293C  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00502941  55                              push rbp
00502942  56                              push rsi
00502943  57                              push rdi
00502944  41 54                           push r12
00502946  41 55                           push r13
00502948  41 56                           push r14
0050294A  41 57                           push r15
0050294C  48 8D AC 24 60 FC FF FF         lea rbp, [rsp - 0x3a0]
00502954  48 81 EC A0 04 00 00            sub rsp, 0x4a0
0050295B  48 8B 05 DE 7D 90 00            mov rax, qword ptr [rip + 0x907dde]
00502962  48 33 C4                        xor rax, rsp
00502965  48 89 85 90 03 00 00            mov qword ptr [rbp + 0x390], rax
0050296C  4C 8B F1                        mov r14, rcx
0050296F  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
00502974  33 C9                           xor ecx, ecx
00502976  4C 89 4C 24 58                  mov qword ptr [rsp + 0x58], r9
0050297B  89 4C 24 70                     mov dword ptr [rsp + 0x70], ecx
0050297F  8B F9                           mov edi, ecx
00502981  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
00502985  8B F1                           mov esi, ecx
00502987  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
0050298B  8B D9                           mov ebx, ecx
0050298D  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
00502991  4C 8B E2                        mov r12, rdx
00502994  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00502998  33 D2                           xor edx, edx
0050299A  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0050299E  41 B8 00 04 00 00               mov r8d, 0x400
005029A4  4D 8B F9                        mov r15, r9
005029A7  E8 94 42 1C 00                  call 0x1406c6c40
005029AC  45 33 DB                        xor r11d, r11d
005029AF  66 44 89 5C 24 3C               mov word ptr [rsp + 0x3c], r11w
005029B5  44 89 5C 24 40                  mov dword ptr [rsp + 0x40], r11d
005029BA  4D 85 F6                        test r14, r14
005029BD  0F 84 3D 08 00 00               je 0x140503200
005029C3  4D 85 E4                        test r12, r12
005029C6  0F 84 34 08 00 00               je 0x140503200
005029CC  45 0F B7 0C 24                  movzx r9d, word ptr [r12]
005029D1  45 8B F3                        mov r14d, r11d
005029D4  44 89 5C 24 30                  mov dword ptr [rsp + 0x30], r11d
005029D9  45 8B EB                        mov r13d, r11d
005029DC  45 8B D3                        mov r10d, r11d
005029DF  66 45 85 C9                     test r9w, r9w
005029E3  0F 84 BF 05 00 00               je 0x140502fa8
005029E9  8D 4B 20                        lea ecx, [rbx + 0x20]
005029EC  49 83 C4 02                     add r12, 2
005029F0  4D 8B C7                        mov r8, r15
005029F3  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
005029F8  45 85 F6                        test r14d, r14d
005029FB  0F 88 A7 05 00 00               js 0x140502fa8
00502A01  41 0F B7 C1                     movzx eax, r9w
00502A05  66 2B C1                        sub ax, cx
00502A08  66 83 F8 5A                     cmp ax, 0x5a
00502A0C  77 15                           ja 0x140502a23
00502A0E  41 0F B7 C1                     movzx eax, r9w
00502A12  48 8D 0D 87 C5 B1 FF            lea rcx, [rip - 0x4e3a79]
00502A19  0F BE 4C 08 E0                  movsx ecx, byte ptr [rax + rcx - 0x20]
00502A1E  83 E1 0F                        and ecx, 0xf
00502A21  EB 03                           jmp 0x140502a26
00502A23  41 8B CB                        mov ecx, r11d
00502A26  41 8D 04 CA                     lea eax, [r10 + rcx*8]
00502A2A  41 0F B7 D1                     movzx edx, r9w
00502A2E  48 63 C8                        movsxd rcx, eax
00502A31  48 8D 05 68 C5 B1 FF            lea rax, [rip - 0x4e3a98]
00502A38  44 0F BE 14 01                  movsx r10d, byte ptr [rcx + rax]
00502A3D  41 C1 FA 04                     sar r10d, 4
00502A41  44 89 54 24 44                  mov dword ptr [rsp + 0x44], r10d
00502A46  41 8B CA                        mov ecx, r10d
00502A49  45 85 D2                        test r10d, r10d
00502A4C  0F 84 82 06 00 00               je 0x1405030d4
00502A52  83 E9 01                        sub ecx, 1
00502A55  0F 84 82 07 00 00               je 0x1405031dd
00502A5B  83 E9 01                        sub ecx, 1
00502A5E  0F 84 29 07 00 00               je 0x14050318d
00502A64  83 E9 01                        sub ecx, 1
00502A67  0F 84 D6 06 00 00               je 0x140503143
00502A6D  83 E9 01                        sub ecx, 1
00502A70  0F 84 C0 06 00 00               je 0x140503136
00502A76  83 E9 01                        sub ecx, 1
00502A79  0F 84 75 06 00 00               je 0x1405030f4
00502A7F  83 E9 01                        sub ecx, 1
00502A82  0F 84 69 05 00 00               je 0x140502ff1
00502A88  83 F9 01                        cmp ecx, 1
00502A8B  0F 85 FE 04 00 00               jne 0x140502f8f
00502A91  83 FA 69                        cmp edx, 0x69
00502A94  0F 87 CB 01 00 00               ja 0x140502c65
00502A9A  74 31                           je 0x140502acd
00502A9C  83 EA 43                        sub edx, 0x43
00502A9F  0F 84 49 01 00 00               je 0x140502bee
00502AA5  83 EA 10                        sub edx, 0x10
00502AA8  0F 84 D4 00 00 00               je 0x140502b82
00502AAE  83 EA 05                        sub edx, 5
00502AB1  0F 84 27 02 00 00               je 0x140502cde
00502AB7  83 EA 02                        sub edx, 2
00502ABA  74 4A                           je 0x140502b06
00502ABC  83 EA 09                        sub edx, 9
00502ABF  0F 84 3A 01 00 00               je 0x140502bff
00502AC5  3B D1                           cmp edx, ecx
00502AC7  0F 85 47 03 00 00               jne 0x140502e14
00502ACD  83 CF 40                        or edi, 0x40
00502AD0  41 BA 0A 00 00 00               mov r10d, 0xa
00502AD6  BA 00 02 00 00                  mov edx, 0x200
00502ADB  49 83 C7 08                     add r15, 8
00502ADF  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00502AE4  0F BA E7 0F                     bt edi, 0xf
00502AE8  72 0A                           jb 0x140502af4
00502AEA  0F BA E7 0C                     bt edi, 0xc
00502AEE  0F 83 3B 02 00 00               jae 0x140502d2f
00502AF4  49 8B 00                        mov rax, qword ptr [r8]
00502AF7  40 F6 C7 40                     test dil, 0x40
00502AFB  0F 84 65 02 00 00               je 0x140502d66
00502B01  E9 4F 02 00 00                  jmp 0x140502d55
00502B06  49 8B 08                        mov rcx, qword ptr [r8]
00502B09  49 83 C7 08                     add r15, 8
00502B0D  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00502B12  48 85 C9                        test rcx, rcx
00502B15  74 4F                           je 0x140502b66
00502B17  48 8B 59 08                     mov rbx, qword ptr [rcx + 8]
00502B1B  48 85 DB                        test rbx, rbx
00502B1E  74 46                           je 0x140502b66
00502B20  0F B7 01                        movzx eax, word ptr [rcx]
00502B23  66 39 41 02                     cmp word ptr [rcx + 2], ax
00502B27  0F 82 D3 06 00 00               jb 0x140503200
00502B2D  44 8B E8                        mov r13d, eax
00502B30  0F BA E7 0B                     bt edi, 0xb
00502B34  73 26                           jae 0x140502b5c
00502B36  F7 D0                           not eax
00502B38  A8 01                           test al, 1
00502B3A  0F 84 C0 06 00 00               je 0x140503200
00502B40  8B C3                           mov eax, ebx
00502B42  F7 D0                           not eax
00502B44  A8 01                           test al, 1
00502B46  0F 84 B4 06 00 00               je 0x140503200
00502B4C  41 D1 ED                        shr r13d, 1
00502B4F  C7 44 24 40 01 00 00 00         mov dword ptr [rsp + 0x40], 1
00502B57  E9 B8 02 00 00                  jmp 0x140502e14
00502B5C  44 89 5C 24 40                  mov dword ptr [rsp + 0x40], r11d
00502B61  E9 AE 02 00 00                  jmp 0x140502e14
00502B66  48 8D 15 2B C4 B1 FF            lea rdx, [rip - 0x4e3bd5]
00502B6D  49 83 CD FF                     or r13, 0xffffffffffffffff
00502B71  48 8B DA                        mov rbx, rdx
00502B74  49 FF C5                        inc r13
00502B77  46 38 1C 2A                     cmp byte ptr [rdx + r13], r11b
00502B7B  75 F7                           jne 0x140502b74
00502B7D  E9 92 02 00 00                  jmp 0x140502e14
00502B82  F7 C7 30 08 00 00               test edi, 0x830
00502B88  75 03                           jne 0x140502b8d
00502B8A  83 CF 20                        or edi, 0x20
00502B8D  49 8B 18                        mov rbx, qword ptr [r8]
00502B90  83 FE FF                        cmp esi, -1
00502B93  8B CE                           mov ecx, esi
00502B95  B8 FF FF FF 7F                  mov eax, 0x7fffffff
00502B9A  0F 44 C8                        cmove ecx, eax
00502B9D  41 B8 20 00 00 00               mov r8d, 0x20
00502BA3  49 83 C7 08                     add r15, 8
00502BA7  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00502BAC  41 84 F8                        test r8b, dil
00502BAF  0F 84 E7 00 00 00               je 0x140502c9c
00502BB5  48 8B C3                        mov rax, rbx
00502BB8  48 85 DB                        test rbx, rbx
00502BBB  75 0D                           jne 0x140502bca
00502BBD  48 8D 15 D4 C3 B1 FF            lea rdx, [rip - 0x4e3c2c]
00502BC4  48 8B DA                        mov rbx, rdx
00502BC7  48 8B C2                        mov rax, rdx
00502BCA  45 8B EB                        mov r13d, r11d
00502BCD  85 C9                           test ecx, ecx
00502BCF  0F 8E 45 02 00 00               jle 0x140502e1a
00502BD5  44 38 18                        cmp byte ptr [rax], r11b
00502BD8  0F 84 3C 02 00 00               je 0x140502e1a
00502BDE  48 FF C0                        inc rax
00502BE1  41 FF C5                        inc r13d
00502BE4  44 3B E9                        cmp r13d, ecx
00502BE7  7C EC                           jl 0x140502bd5
00502BE9  E9 2C 02 00 00                  jmp 0x140502e1a
00502BEE  B9 20 00 00 00                  mov ecx, 0x20
00502BF3  F7 C7 30 08 00 00               test edi, 0x830
00502BF9  75 09                           jne 0x140502c04
00502BFB  0B F9                           or edi, ecx
00502BFD  EB 05                           jmp 0x140502c04
00502BFF  B9 20 00 00 00                  mov ecx, 0x20
00502C04  41 0F B7 00                     movzx eax, word ptr [r8]
00502C08  49 83 C7 08                     add r15, 8
00502C0C  C7 44 24 40 01 00 00 00         mov dword ptr [rsp + 0x40], 1
00502C14  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00502C19  66 89 44 24 3C                  mov word ptr [rsp + 0x3c], ax
00502C1E  40 84 F9                        test cl, dil
00502C21  74 2F                           je 0x140502c52
00502C23  4C 63 05 D6 7A 90 00            movsxd r8, dword ptr [rip + 0x907ad6]
00502C2A  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00502C2F  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00502C33  88 44 24 48                     mov byte ptr [rsp + 0x48], al
00502C37  44 88 5C 24 49                  mov byte ptr [rsp + 0x49], r11b
00502C3C  E8 9F DC FF FF                  call 0x1405008e0
00502C41  45 33 DB                        xor r11d, r11d
00502C44  85 C0                           test eax, eax
00502C46  79 0E                           jns 0x140502c56
00502C48  C7 44 24 60 01 00 00 00         mov dword ptr [rsp + 0x60], 1
00502C50  EB 04                           jmp 0x140502c56
00502C52  66 89 45 90                     mov word ptr [rbp - 0x70], ax
00502C56  48 8D 5D 90                     lea rbx, [rbp - 0x70]
00502C5A  41 BD 01 00 00 00               mov r13d, 1
00502C60  E9 AF 01 00 00                  jmp 0x140502e14
00502C65  83 EA 6E                        sub edx, 0x6e
00502C68  0F 84 42 03 00 00               je 0x140502fb0
00502C6E  83 EA 01                        sub edx, 1
00502C71  0F 84 9B 00 00 00               je 0x140502d12
00502C77  83 EA 01                        sub edx, 1
00502C7A  74 59                           je 0x140502cd5
00502C7C  83 EA 03                        sub edx, 3
00502C7F  0F 84 08 FF FF FF               je 0x140502b8d
00502C85  83 EA 02                        sub edx, 2
00502C88  0F 84 42 FE FF FF               je 0x140502ad0
00502C8E  83 FA 03                        cmp edx, 3
00502C91  0F 85 7D 01 00 00               jne 0x140502e14
00502C97  8D 42 24                        lea eax, [rdx + 0x24]
00502C9A  EB 47                           jmp 0x140502ce3
00502C9C  48 85 DB                        test rbx, rbx
00502C9F  C7 44 24 40 01 00 00 00         mov dword ptr [rsp + 0x40], 1
00502CA7  48 8D 05 4A 82 B2 FF            lea rax, [rip - 0x4d7db6]
00502CAE  48 0F 45 C3                     cmovne rax, rbx
00502CB2  48 8B D8                        mov rbx, rax
00502CB5  EB 0C                           jmp 0x140502cc3
00502CB7  FF C9                           dec ecx
00502CB9  66 44 39 18                     cmp word ptr [rax], r11w
00502CBD  74 08                           je 0x140502cc7
00502CBF  48 83 C0 02                     add rax, 2
00502CC3  85 C9                           test ecx, ecx
00502CC5  75 F0                           jne 0x140502cb7
00502CC7  48 2B C3                        sub rax, rbx
00502CCA  48 D1 F8                        sar rax, 1
00502CCD  44 8B E8                        mov r13d, eax
00502CD0  E9 45 01 00 00                  jmp 0x140502e1a
00502CD5  BE 10 00 00 00                  mov esi, 0x10
00502CDA  0F BA EF 0F                     bts edi, 0xf
00502CDE  B8 07 00 00 00                  mov eax, 7
00502CE3  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00502CE7  40 84 FF                        test dil, dil
00502CEA  79 1B                           jns 0x140502d07
00502CEC  B9 30 00 00 00                  mov ecx, 0x30
00502CF1  C7 44 24 34 02 00 00 00         mov dword ptr [rsp + 0x34], 2
00502CF9  66 83 C0 51                     add ax, 0x51
00502CFD  66 89 4C 24 4C                  mov word ptr [rsp + 0x4c], cx
00502D02  66 89 44 24 4E                  mov word ptr [rsp + 0x4e], ax
00502D07  41 BA 10 00 00 00               mov r10d, 0x10
00502D0D  E9 C4 FD FF FF                  jmp 0x140502ad6
00502D12  B8 08 00 00 00                  mov eax, 8
00502D17  44 8B D0                        mov r10d, eax
00502D1A  40 84 FF                        test dil, dil
00502D1D  0F 89 B3 FD FF FF               jns 0x140502ad6
00502D23  BA 00 02 00 00                  mov edx, 0x200
00502D28  0B FA                           or edi, edx
00502D2A  E9 AC FD FF FF                  jmp 0x140502adb
00502D2F  8B C7                           mov eax, edi
00502D31  B9 20 00 00 00                  mov ecx, 0x20
00502D36  83 E0 40                        and eax, 0x40
00502D39  40 84 F9                        test cl, dil
00502D3C  74 10                           je 0x140502d4e
00502D3E  85 C0                           test eax, eax
00502D40  74 06                           je 0x140502d48
00502D42  49 0F BF 00                     movsx rax, word ptr [r8]
00502D46  EB 0D                           jmp 0x140502d55
00502D48  41 0F B7 00                     movzx eax, word ptr [r8]
00502D4C  EB 18                           jmp 0x140502d66
00502D4E  85 C0                           test eax, eax
00502D50  74 11                           je 0x140502d63
00502D52  49 63 00                        movsxd rax, dword ptr [r8]
00502D55  48 85 C0                        test rax, rax
00502D58  79 0C                           jns 0x140502d66
00502D5A  48 F7 D8                        neg rax
00502D5D  0F BA EF 08                     bts edi, 8
00502D61  EB 03                           jmp 0x140502d66
00502D63  41 8B 00                        mov eax, dword ptr [r8]
00502D66  F7 C7 00 90 00 00               test edi, 0x9000
00502D6C  44 8B C0                        mov r8d, eax
00502D6F  4C 0F 45 C0                     cmovne r8, rax
00502D73  85 F6                           test esi, esi
00502D75  79 07                           jns 0x140502d7e
00502D77  BE 01 00 00 00                  mov esi, 1
00502D7C  EB 08                           jmp 0x140502d86
00502D7E  83 E7 F7                        and edi, 0xfffffff7
00502D81  3B F2                           cmp esi, edx
00502D83  0F 4F F2                        cmovg esi, edx
00502D86  44 8B 5C 24 70                  mov r11d, dword ptr [rsp + 0x70]
00502D8B  49 8B C0                        mov rax, r8
00502D8E  48 F7 D8                        neg rax
00502D91  1B C9                           sbb ecx, ecx
00502D93  23 4C 24 34                     and ecx, dword ptr [rsp + 0x34]
00502D97  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
00502D9B  44 8B C9                        mov r9d, ecx
00502D9E  48 8D 8D 8F 01 00 00            lea rcx, [rbp + 0x18f]
00502DA5  8B C6                           mov eax, esi
00502DA7  FF CE                           dec esi
00502DA9  85 C0                           test eax, eax
00502DAB  7F 05                           jg 0x140502db2
00502DAD  4D 85 C0                        test r8, r8
00502DB0  74 1D                           je 0x140502dcf
00502DB2  33 D2                           xor edx, edx
00502DB4  49 8B C0                        mov rax, r8
00502DB7  49 F7 F2                        div r10
00502DBA  83 C2 30                        add edx, 0x30
00502DBD  4C 8B C0                        mov r8, rax
00502DC0  83 FA 39                        cmp edx, 0x39
00502DC3  7E 03                           jle 0x140502dc8
00502DC5  41 03 D3                        add edx, r11d
00502DC8  88 11                           mov byte ptr [rcx], dl
00502DCA  48 FF C9                        dec rcx
00502DCD  EB D6                           jmp 0x140502da5
00502DCF  4C 8D AD 8F 01 00 00            lea r13, [rbp + 0x18f]
00502DD6  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
00502DDA  44 2B E9                        sub r13d, ecx
00502DDD  48 8D 59 01                     lea rbx, [rcx + 1]
00502DE1  0F BA E7 09                     bt edi, 9
00502DE5  73 2A                           jae 0x140502e11
00502DE7  B8 30 00 00 00                  mov eax, 0x30
00502DEC  45 85 ED                        test r13d, r13d
00502DEF  74 0E                           je 0x140502dff
00502DF1  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00502DF6  44 89 4C 24 34                  mov dword ptr [rsp + 0x34], r9d
00502DFB  38 03                           cmp byte ptr [rbx], al
00502DFD  74 12                           je 0x140502e11
00502DFF  48 FF CB                        dec rbx
00502E02  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00502E07  41 FF C5                        inc r13d
00502E0A  44 89 4C 24 34                  mov dword ptr [rsp + 0x34], r9d
00502E0F  88 03                           mov byte ptr [rbx], al
00502E11  45 33 DB                        xor r11d, r11d
00502E14  41 B8 20 00 00 00               mov r8d, 0x20
00502E1A  44 39 5C 24 60                  cmp dword ptr [rsp + 0x60], r11d
00502E1F  0F 85 65 01 00 00               jne 0x140502f8a
00502E25  40 F6 C7 40                     test dil, 0x40
00502E29  74 38                           je 0x140502e63
00502E2B  0F BA E7 08                     bt edi, 8
00502E2F  73 07                           jae 0x140502e38
00502E31  B8 2D 00 00 00                  mov eax, 0x2d
00502E36  EB 0B                           jmp 0x140502e43
00502E38  40 F6 C7 01                     test dil, 1
00502E3C  74 17                           je 0x140502e55
00502E3E  B8 2B 00 00 00                  mov eax, 0x2b
00502E43  66 89 44 24 4C                  mov word ptr [rsp + 0x4c], ax
00502E48  41 BE 01 00 00 00               mov r14d, 1
00502E4E  44 89 74 24 34                  mov dword ptr [rsp + 0x34], r14d
00502E53  EB 13                           jmp 0x140502e68
00502E55  40 F6 C7 02                     test dil, 2
00502E59  74 08                           je 0x140502e63
00502E5B  66 44 89 44 24 4C               mov word ptr [rsp + 0x4c], r8w
00502E61  EB E5                           jmp 0x140502e48
00502E63  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
00502E68  44 8B 7C 24 50                  mov r15d, dword ptr [rsp + 0x50]
00502E6D  8B F7                           mov esi, edi
00502E6F  45 2B FD                        sub r15d, r13d
00502E72  45 2B FE                        sub r15d, r14d
00502E75  83 E6 0C                        and esi, 0xc
00502E78  75 15                           jne 0x140502e8f
00502E7A  41 8B C8                        mov ecx, r8d
00502E7D  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
00502E82  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00502E87  41 8B D7                        mov edx, r15d
00502E8A  E8 0D 04 00 00                  call 0x14050329c
00502E8F  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00502E94  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
00502E99  41 8B D6                        mov edx, r14d
00502E9C  48 8D 4C 24 4C                  lea rcx, [rsp + 0x4c]
00502EA1  E8 4E 04 00 00                  call 0x1405032f4
00502EA6  83 FE 08                        cmp esi, 8
00502EA9  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00502EAE  75 15                           jne 0x140502ec5
00502EB0  B9 30 00 00 00                  mov ecx, 0x30
00502EB5  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
00502EBA  4C 8B C6                        mov r8, rsi
00502EBD  41 8B D7                        mov edx, r15d
00502EC0  E8 D7 03 00 00                  call 0x14050329c
00502EC5  83 7C 24 40 00                  cmp dword ptr [rsp + 0x40], 0
00502ECA  75 77                           jne 0x140502f43
00502ECC  45 85 ED                        test r13d, r13d
00502ECF  7E 72                           jle 0x140502f43
00502ED1  4C 8B F3                        mov r14, rbx
00502ED4  41 8B F5                        mov esi, r13d
00502ED7  4C 63 05 22 78 90 00            movsxd r8, dword ptr [rip + 0x907822]
00502EDE  48 8D 4C 24 3C                  lea rcx, [rsp + 0x3c]
00502EE3  49 8B D6                        mov rdx, r14
00502EE6  E8 F5 D9 FF FF                  call 0x1405008e0
00502EEB  4C 63 E0                        movsxd r12, eax
00502EEE  45 33 DB                        xor r11d, r11d
00502EF1  41 83 FC 02                     cmp r12d, 2
00502EF5  41 8B C3                        mov eax, r11d
00502EF8  0F 94 C0                        sete al
00502EFB  FF C0                           inc eax
00502EFD  2B F0                           sub esi, eax
00502EFF  45 85 E4                        test r12d, r12d
00502F02  7E 2A                           jle 0x140502f2e
00502F04  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
00502F09  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
00502F0E  0F B7 4C 24 3C                  movzx ecx, word ptr [rsp + 0x3c]
00502F13  E8 30 03 00 00                  call 0x140503248
00502F18  45 33 DB                        xor r11d, r11d
00502F1B  4D 03 F4                        add r14, r12
00502F1E  85 F6                           test esi, esi
00502F20  7F B5                           jg 0x140502ed7
00502F22  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
00502F27  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00502F2C  EB 2B                           jmp 0x140502f59
00502F2E  4C 8B 64 24 78                  mov r12, qword ptr [rsp + 0x78]
00502F33  41 83 CE FF                     or r14d, 0xffffffff
00502F37  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00502F3C  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
00502F41  EB 1B                           jmp 0x140502f5e
00502F43  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
00502F48  4C 8B C6                        mov r8, rsi
00502F4B  41 8B D5                        mov edx, r13d
00502F4E  48 8B CB                        mov rcx, rbx
00502F51  E8 9E 03 00 00                  call 0x1405032f4
00502F56  45 33 DB                        xor r11d, r11d
00502F59  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
00502F5E  B9 20 00 00 00                  mov ecx, 0x20
00502F63  45 85 F6                        test r14d, r14d
00502F66  78 7E                           js 0x140502fe6
00502F68  40 F6 C7 04                     test dil, 4
00502F6C  74 78                           je 0x140502fe6
00502F6E  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
00502F73  4C 8B C6                        mov r8, rsi
00502F76  41 8B D7                        mov edx, r15d
00502F79  E8 1E 03 00 00                  call 0x14050329c
00502F7E  8B 74 24 38                     mov esi, dword ptr [rsp + 0x38]
00502F82  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
00502F87  45 33 DB                        xor r11d, r11d
00502F8A  44 8B 54 24 44                  mov r10d, dword ptr [rsp + 0x44]
00502F8F  B9 20 00 00 00                  mov ecx, 0x20
00502F94  45 0F B7 0C 24                  movzx r9d, word ptr [r12]
00502F99  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00502F9E  66 45 85 C9                     test r9w, r9w
00502FA2  0F 85 44 FA FF FF               jne 0x1405029ec
00502FA8  41 8B C6                        mov eax, r14d
00502FAB  E9 67 02 00 00                  jmp 0x140503217
00502FB0  49 8B 30                        mov rsi, qword ptr [r8]
00502FB3  49 83 C7 08                     add r15, 8
00502FB7  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00502FBC  E8 D3 14 00 00                  call 0x140504494
00502FC1  45 33 DB                        xor r11d, r11d
00502FC4  85 C0                           test eax, eax
00502FC6  0F 84 34 02 00 00               je 0x140503200
00502FCC  41 8D 4B 20                     lea ecx, [r11 + 0x20]
00502FD0  40 84 F9                        test cl, dil
00502FD3  74 06                           je 0x140502fdb
00502FD5  66 44 89 36                     mov word ptr [rsi], r14w
00502FD9  EB 03                           jmp 0x140502fde
00502FDB  44 89 36                        mov dword ptr [rsi], r14d
00502FDE  C7 44 24 60 01 00 00 00         mov dword ptr [rsp + 0x60], 1
00502FE6  8B 74 24 38                     mov esi, dword ptr [rsp + 0x38]
00502FEA  44 8B 54 24 44                  mov r10d, dword ptr [rsp + 0x44]
00502FEF  EB A3                           jmp 0x140502f94
00502FF1  B9 49 00 00 00                  mov ecx, 0x49
00502FF6  3B D1                           cmp edx, ecx
00502FF8  74 26                           je 0x140503020
00502FFA  83 FA 68                        cmp edx, 0x68
00502FFD  74 77                           je 0x140503076
00502FFF  8D 41 21                        lea eax, [rcx + 0x21]
00503002  3B D0                           cmp edx, eax
00503004  74 1F                           je 0x140503025
00503006  8D 41 23                        lea eax, [rcx + 0x23]
00503009  3B D0                           cmp edx, eax
0050300B  74 48                           je 0x140503055
0050300D  83 FA 74                        cmp edx, 0x74
00503010  74 0E                           je 0x140503020
00503012  83 FA 77                        cmp edx, 0x77
00503015  74 35                           je 0x14050304c
00503017  83 FA 7A                        cmp edx, 0x7a
0050301A  0F 85 6F FF FF FF               jne 0x140502f8f
00503020  B8 6A 00 00 00                  mov eax, 0x6a
00503025  0F BA EF 0F                     bts edi, 0xf
00503029  66 44 3B C9                     cmp r9w, cx
0050302D  75 6F                           jne 0x14050309e
0050302F  41 0F B7 04 24                  movzx eax, word ptr [r12]
00503034  66 83 F8 36                     cmp ax, 0x36
00503038  75 48                           jne 0x140503082
0050303A  66 41 83 7C 24 02 34            cmp word ptr [r12 + 2], 0x34
00503041  75 65                           jne 0x1405030a8
00503043  49 83 C4 04                     add r12, 4
00503047  E9 43 FF FF FF                  jmp 0x140502f8f
0050304C  0F BA EF 0B                     bts edi, 0xb
00503050  E9 3A FF FF FF                  jmp 0x140502f8f
00503055  B9 20 00 00 00                  mov ecx, 0x20
0050305A  66 41 39 04 24                  cmp word ptr [r12], ax
0050305F  75 0D                           jne 0x14050306e
00503061  49 83 C4 02                     add r12, 2
00503065  0F BA EF 0C                     bts edi, 0xc
00503069  E9 26 FF FF FF                  jmp 0x140502f94
0050306E  83 CF 10                        or edi, 0x10
00503071  E9 1E FF FF FF                  jmp 0x140502f94
00503076  B9 20 00 00 00                  mov ecx, 0x20
0050307B  0B F9                           or edi, ecx
0050307D  E9 12 FF FF FF                  jmp 0x140502f94
00503082  66 83 F8 33                     cmp ax, 0x33
00503086  75 20                           jne 0x1405030a8
00503088  66 41 83 7C 24 02 32            cmp word ptr [r12 + 2], 0x32
0050308F  75 17                           jne 0x1405030a8
00503091  49 83 C4 04                     add r12, 4
00503095  0F BA F7 0F                     btr edi, 0xf
00503099  E9 F1 FE FF FF                  jmp 0x140502f8f
0050309E  66 44 3B C8                     cmp r9w, ax
005030A2  0F 84 E7 FE FF FF               je 0x140502f8f
005030A8  41 0F B7 04 24                  movzx eax, word ptr [r12]
005030AD  B9 20 00 00 00                  mov ecx, 0x20
005030B2  66 83 E8 58                     sub ax, 0x58
005030B6  66 3B C1                        cmp ax, cx
005030B9  77 14                           ja 0x1405030cf
005030BB  48 B9 01 10 82 20 01 00 00 00   movabs rcx, 0x120821001
005030C5  48 0F A3 C1                     bt rcx, rax
005030C9  0F 82 C0 FE FF FF               jb 0x140502f8f
005030CF  44 89 5C 24 44                  mov dword ptr [rsp + 0x44], r11d
005030D4  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
005030D9  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
005030DE  41 0F B7 C9                     movzx ecx, r9w
005030E2  C7 44 24 40 01 00 00 00         mov dword ptr [rsp + 0x40], 1
005030EA  E8 59 01 00 00                  call 0x140503248
005030EF  E9 8E FE FF FF                  jmp 0x140502f82
005030F4  66 41 83 F9 2A                  cmp r9w, 0x2a
005030F9  75 29                           jne 0x140503124
005030FB  41 8B 30                        mov esi, dword ptr [r8]
005030FE  49 83 C7 08                     add r15, 8
00503102  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00503107  B9 20 00 00 00                  mov ecx, 0x20
0050310C  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
00503110  85 F6                           test esi, esi
00503112  0F 89 7C FE FF FF               jns 0x140502f94
00503118  83 CE FF                        or esi, 0xffffffff
0050311B  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
0050311F  E9 70 FE FF FF                  jmp 0x140502f94
00503124  8D 34 B6                        lea esi, [rsi + rsi*4]
00503127  8D 76 E8                        lea esi, [rsi - 0x18]
0050312A  8D 34 72                        lea esi, [rdx + rsi*2]
0050312D  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
00503131  E9 59 FE FF FF                  jmp 0x140502f8f
00503136  41 8B F3                        mov esi, r11d
00503139  44 89 5C 24 38                  mov dword ptr [rsp + 0x38], r11d
0050313E  E9 4C FE FF FF                  jmp 0x140502f8f
00503143  66 41 83 F9 2A                  cmp r9w, 0x2a
00503148  75 2D                           jne 0x140503177
0050314A  45 8B 00                        mov r8d, dword ptr [r8]
0050314D  49 83 C7 08                     add r15, 8
00503151  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00503156  41 8B C8                        mov ecx, r8d
00503159  45 85 C0                        test r8d, r8d
0050315C  79 03                           jns 0x140503161
0050315E  83 CF 04                        or edi, 4
00503161  41 8B C0                        mov eax, r8d
00503164  41 F7 D8                        neg r8d
00503167  85 C0                           test eax, eax
00503169  44 0F 49 C1                     cmovns r8d, ecx
0050316D  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
00503172  E9 18 FE FF FF                  jmp 0x140502f8f
00503177  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
0050317B  8D 0C 89                        lea ecx, [rcx + rcx*4]
0050317E  8D 49 E8                        lea ecx, [rcx - 0x18]
00503181  8D 0C 4A                        lea ecx, [rdx + rcx*2]
00503184  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
00503188  E9 02 FE FF FF                  jmp 0x140502f8f
0050318D  B9 20 00 00 00                  mov ecx, 0x20
00503192  3B D1                           cmp edx, ecx
00503194  74 3F                           je 0x1405031d5
00503196  83 FA 23                        cmp edx, 0x23
00503199  74 31                           je 0x1405031cc
0050319B  8D 41 0B                        lea eax, [rcx + 0xb]
0050319E  3B D0                           cmp edx, eax
005031A0  74 22                           je 0x1405031c4
005031A2  8D 41 0D                        lea eax, [rcx + 0xd]
005031A5  3B D0                           cmp edx, eax
005031A7  74 13                           je 0x1405031bc
005031A9  8D 41 10                        lea eax, [rcx + 0x10]
005031AC  3B D0                           cmp edx, eax
005031AE  0F 85 E0 FD FF FF               jne 0x140502f94
005031B4  83 CF 08                        or edi, 8
005031B7  E9 D8 FD FF FF                  jmp 0x140502f94
005031BC  83 CF 04                        or edi, 4
005031BF  E9 D0 FD FF FF                  jmp 0x140502f94
005031C4  83 CF 01                        or edi, 1
005031C7  E9 C8 FD FF FF                  jmp 0x140502f94
005031CC  0F BA EF 07                     bts edi, 7
005031D0  E9 BF FD FF FF                  jmp 0x140502f94
005031D5  83 CF 02                        or edi, 2
005031D8  E9 B7 FD FF FF                  jmp 0x140502f94
005031DD  83 CE FF                        or esi, 0xffffffff
005031E0  44 89 5C 24 60                  mov dword ptr [rsp + 0x60], r11d
005031E5  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
005031E9  41 8B FB                        mov edi, r11d
005031EC  44 89 5C 24 50                  mov dword ptr [rsp + 0x50], r11d
005031F1  44 89 5C 24 34                  mov dword ptr [rsp + 0x34], r11d
005031F6  44 89 5C 24 40                  mov dword ptr [rsp + 0x40], r11d
005031FB  E9 8F FD FF FF                  jmp 0x140502f8f
00503200  45 33 C9                        xor r9d, r9d
00503203  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
00503208  45 33 C0                        xor r8d, r8d
0050320B  33 D2                           xor edx, edx
0050320D  33 C9                           xor ecx, ecx
0050320F  E8 3C B3 F9 FF                  call 0x14049e550
00503214  83 C8 FF                        or eax, 0xffffffff
00503217  48 8B 8D 90 03 00 00            mov rcx, qword ptr [rbp + 0x390]
0050321E  48 33 CC                        xor rcx, rsp
00503221  E8 1A 94 1A 00                  call 0x1406ac640
00503226  48 8B 9C 24 F0 04 00 00         mov rbx, qword ptr [rsp + 0x4f0]
0050322E  48 81 C4 A0 04 00 00            add rsp, 0x4a0
00503235  41 5F                           pop r15
00503237  41 5E                           pop r14
00503239  41 5D                           pop r13
0050323B  41 5C                           pop r12
0050323D  5F                              pop rdi
0050323E  5E                              pop rsi
0050323F  5D                              pop rbp
00503240  C3                              ret
00503241  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall woutput_l(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
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
    unsigned __int64 v_stack_m249;
    unsigned __int64 v_stack_m3D8;
    unsigned __int64 v_stack_m448;
    unsigned __int64 v_stack_m460;
    unsigned int v_stack_m468;
    unsigned __int64 v_stack_m470;
    unsigned int v_stack_m478;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m480;
    unsigned int v_stack_m488;
    unsigned __int16 v_stack_m48A;
    unsigned __int16 v_stack_m48C;
    unsigned __int8 v_stack_m48F;
    unsigned __int64 v_stack_m490;
    unsigned int v_stack_m494;
    unsigned int v_stack_m498;
    unsigned __int16 v_stack_m49C;
    unsigned int v_stack_m4A0;
    unsigned int v_stack_m4A4;
    unsigned int v_stack_m4A8;
    unsigned __int64 v_stack_m4B8;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (0x4A0ULL);
    result = (*(unsigned __int64 *)(v_rip + 9469406)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m470 = a1;
    a1 = 0;
    v_stack_m480 = a4;
    v_stack_m468 = 0;
    v_stack_m488 = 0;
    v_stack_m4A0 = 0;
    v_stack_m4A4 = 0;
    v_stack_m478 = 0;
    a2 = 0;
    result = memset(v_stack_m448, a2, (unsigned int)(0x400ULL), a4);
    v_r11 = 0;
    v_stack_m49C = 0;
    v_stack_m498 = 0;
    if (0 == 0) goto loc_00503200;
    if (0 == 0) goto loc_00503200;
    v_stack_m4A8 = 0;
    if ((unsigned __int16)(*(unsigned __int16 *)(a2)) == 0) goto loc_00502FA8;
loc_005029EC:
    v_r12 = (a2) + (2);
    v_stack_m460 = v_r12;
    if (sign_flag) goto loc_00502FA8;
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a2))) - ((unsigned __int16)(0 + 32)));
    if (((unsigned __int16)(result)) > 90) goto loc_00502A23;
    a1 = (unsigned int)(((__int8)(*(unsigned __int8 *)((unsigned __int16)(*(unsigned __int16 *)(a2)) + v_rip - 5126777 * 1 - 32))) & (15));
    goto loc_00502A26;
loc_00502A23:
loc_00502A26:
    v_r10 = (unsigned int)(((__int8)(*(unsigned __int8 *)((int)((unsigned int)(0 + 0 * 8)) + v_rip - 5126808 * 1))) >> (4));
    v_stack_m494 = (unsigned int)(v_r10);
    if ((unsigned int)(v_r10) == 0) goto loc_005030D4;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) - (1));
    if (condition_is_equal) goto loc_005031DD;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0050318D;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00503143;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00503136;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_005030F4;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00502FF1;
    if (((unsigned int)(a1)) != 1) goto loc_00502F8F;
    if (((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(a2)))) > 105) goto loc_00502C65;
    if (((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(a2)))) == 105) goto loc_00502ACD;
    a2 = (unsigned int)(((unsigned __int16)(*(unsigned __int16 *)(a2))) - (67));
    if (condition_is_equal) goto loc_00502BEE;
    a2 = (unsigned int)((a2) - (16));
    if (condition_is_equal) goto loc_00502B82;
    a2 = (unsigned int)((a2) - (5));
    if (condition_is_equal) goto loc_00502CDE;
    a2 = (unsigned int)((a2) - (2));
    if (condition_is_equal) goto loc_00502B06;
    a2 = (unsigned int)((a2) - (9));
    if (condition_is_equal) goto loc_00502BFF;
    if (((unsigned int)(a2)) != ((unsigned int)(a1))) goto loc_00502E14;
loc_00502ACD:
    v_rdi = (unsigned int)((0) | (64));
loc_00502AD0:
loc_00502AD6:
loc_00502ADB:
    v_r15 = (a4) + (8);
    v_stack_m480 = v_r15;
    if (condition_is_below) goto loc_00502AF4;
    if (condition_is_above_or_equal) goto loc_00502D2F;
loc_00502AF4:
    if ((((unsigned __int8)(v_rdi)) & (64)) == 0) goto loc_00502D66;
    goto loc_00502D55;
loc_00502B06:
    v_r15 = (v_r15) + (8);
    v_stack_m480 = v_r15;
    if (*(unsigned __int64 *)(a4) == 0) goto loc_00502B66;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 8) == 0) goto loc_00502B66;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a4) + 2)) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a4))))) goto loc_00503200;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a4) + 2)) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a4))))) goto loc_00502B5C;
    result = (unsigned int)(~(*(unsigned __int16 *)(*(unsigned __int64 *)(a4))));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_00503200;
    result = (unsigned int)(~((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 8)))));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_00503200;
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a4))))) >> (1));
    v_stack_m498 = 1;
    goto loc_00502E14;
loc_00502B5C:
    v_stack_m498 = 0;
    goto loc_00502E14;
loc_00502B66:
    v_r13 = (v_r13) | (-1);
loc_00502B74:
    v_r13 = (v_r13) + 1;
    if ((*(unsigned __int8 *)(v_rip - 5127125 + v_r13 * 1)) != 0) goto loc_00502B74;
    goto loc_00502E14;
loc_00502B82:
    if ((((unsigned int)(v_rdi)) & (0x830ULL)) == 0) {
        v_rdi = (unsigned int)((v_rdi) | (32));
    }
    a1 = 0;
    if (0 == -1) { a1 = (unsigned int)((unsigned int)(0x7FFFFFFFULL)); }
    v_r15 = (v_r15) + (8);
    v_stack_m480 = v_r15;
    if (((32) & ((unsigned __int8)(v_rdi))) == 0) goto loc_00502C9C;
    result = *(unsigned __int64 *)(a4);
    v_rbx = *(unsigned __int64 *)(a4);
    if (*(unsigned __int64 *)(a4) == 0) {
        a2 = v_rip - 5127212;
        v_rbx = a2;
        result = a2;
    }
    if (condition_is_less_or_equal) goto loc_00502E1A;
loc_00502BD5:
    if ((*(unsigned __int8 *)(result)) == 0) goto loc_00502E1A;
    result = (result) + 1;
    v_r13 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r13)) < ((unsigned int)(a1))) goto loc_00502BD5;
    goto loc_00502E1A;
loc_00502BEE:
    if ((((unsigned int)(v_rdi)) & (0x830ULL)) != 0) goto loc_00502C04;
    v_rdi = (unsigned int)((v_rdi) | (32));
    goto loc_00502C04;
loc_00502BFF:
loc_00502C04:
    v_r15 = (v_r15) + (8);
    v_stack_m498 = 1;
    v_stack_m480 = v_r15;
    v_stack_m49C = (unsigned __int16)(*(unsigned __int16 *)(32));
    if (((32) & ((unsigned __int8)(v_rdi))) == 0) goto loc_00502C52;
    v_stack_m490 = (unsigned __int8)(*(unsigned __int16 *)(32));
    v_stack_m48F = 0;
    result = mbtowc(v_stack_m448, v_stack_m490, (int)(*(unsigned int *)(v_rip + 9468630)), *(unsigned __int16 *)(a2));
    v_r11 = 0;
    if (!sign_flag) goto loc_00502C56;
    v_stack_m478 = 1;
    goto loc_00502C56;
loc_00502C52:
    v_stack_m448 = (unsigned __int16)(result);
loc_00502C56:
    goto loc_00502E14;
loc_00502C65:
    a2 = (unsigned int)((v_stack_m490) - (110));
    if (condition_is_equal) goto loc_00502FB0;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00502D12;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00502CD5;
    a2 = (unsigned int)((a2) - (3));
    if (condition_is_equal) goto loc_00502B8D;
    a2 = (unsigned int)((a2) - (2));
    if (condition_is_equal) goto loc_00502AD0;
    if (((unsigned int)(a2)) != 3) goto loc_00502E14;
    goto loc_00502CE3;
loc_00502C9C:
    v_stack_m498 = 1;
    result = v_rip - 5078454;
    if (v_stack_m448 != 0) { result = v_stack_m448; }
    goto loc_00502CC3;
loc_00502CB7:
    a1 = (unsigned int)((v_stack_m448) - 1);
    if ((*(unsigned __int16 *)(result)) == 0) goto loc_00502CC7;
    result = (result) + (2);
loc_00502CC3:
    if ((unsigned int)(a1) != 0) goto loc_00502CB7;
loc_00502CC7:
    result = (result) - (result);
    result = (result) >> (1);
    goto loc_00502E1A;
loc_00502CD5:
loc_00502CDE:
loc_00502CE3:
    v_stack_m468 = 7;
    result = 7;
    if (sign_flag) {
        a1 = 48;
        v_stack_m4A4 = 2;
        result = (unsigned __int16)((7) + (81));
        v_stack_m48C = (unsigned __int16)(a1);
        v_stack_m48A = (unsigned __int16)(result);
    }
    goto loc_00502AD6;
loc_00502D12:
    if (!sign_flag) goto loc_00502AD6;
    v_rdi = (unsigned int)((v_rdi) | (512));
    goto loc_00502ADB;
loc_00502D2F:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (64));
    if (((32) & ((unsigned __int8)(v_rdi))) == 0) goto loc_00502D4E;
    if ((unsigned int)(result) == 0) goto loc_00502D48;
    goto loc_00502D55;
loc_00502D48:
    goto loc_00502D66;
loc_00502D4E:
    if ((unsigned int)(*(unsigned __int16 *)((int)(*(unsigned int *)(v_rip + 9468630)))) == 0) goto loc_00502D63;
loc_00502D55:
    if (!sign_flag) goto loc_00502D66;
    result = -((int)(*(unsigned int *)((int)(*(unsigned int *)(v_rip + 9468630)))));
    goto loc_00502D66;
loc_00502D63:
loc_00502D66:
    a3 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((int)(*(unsigned int *)(v_rip + 9468630))))));
    if ((((unsigned int)(v_rdi)) & (0x9000ULL)) != 0) { a3 = (unsigned int)(*(unsigned int *)((int)(*(unsigned int *)(v_rip + 9468630)))); }
    if (!sign_flag) goto loc_00502D7E;
    goto loc_00502D86;
loc_00502D7E:
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFF7ULL));
    v_rsi = 1;
    if (1 > 512) { v_rsi = 512; }
loc_00502D86:
    result = -(a3);
    a1 = (unsigned int)((32) & (v_stack_m4A4));
    v_stack_m4A4 = (unsigned int)(a1);
loc_00502DA5:
    v_rsi = (unsigned int)((v_rsi) - 1);
    if (condition_is_greater) goto loc_00502DB2;
    if (a3 == 0) goto loc_00502DCF;
loc_00502DB2:
    a2 = 0;
    a2 = (unsigned int)((a2) + (48));
    if (((unsigned int)(a2)) >= = 57) {
        a2 = (unsigned int)((a2) + ((unsigned int)((unsigned int)(v_stack_m468))));
    }
    *(unsigned __int8 *)(v_stack_m249) = (unsigned __int8)(a2);
    a1 = (v_stack_m249) - 1;
    goto loc_00502DA5;
loc_00502DCF:
    v_stack_m4A0 = (unsigned int)(v_rsi);
    v_r13 = (unsigned int)((v_stack_m249) - ((unsigned int)(a1)));
    if (condition_is_above_or_equal) goto loc_00502E11;
    if ((unsigned int)(v_r13) == 0) goto loc_00502DFF;
    v_stack_m480 = v_r15;
    v_stack_m4A4 = (unsigned int)((unsigned int)((unsigned int)(a1)));
    v_rbx = a1 + 1;
    if ((*(unsigned __int8 *)(a1 + 1)) != 48) {
        v_rbx = (a1 + 1) - 1;
        v_stack_m480 = v_r15;
        v_r13 = (unsigned int)((v_r13) + 1);
        v_stack_m4A4 = (unsigned int)((unsigned int)((unsigned int)(a1)));
        *(unsigned __int8 *)(v_rbx) = 48;
    }
    v_r11 = 0;
loc_00502E14:
loc_00502E1A:
    if (v_stack_m478 != 0) goto loc_00502F8A;
    if ((((unsigned __int8)(v_rdi)) & (64)) == 0) goto loc_00502E63;
    if (condition_is_above_or_equal) goto loc_00502E38;
    goto loc_00502E43;
loc_00502E38:
    if ((((unsigned __int8)(v_rdi)) & (1)) == 0) goto loc_00502E55;
loc_00502E43:
    v_stack_m48C = 43;
loc_00502E48:
    v_stack_m4A4 = 1;
    goto loc_00502E68;
loc_00502E55:
    if ((((unsigned __int8)(v_rdi)) & (2)) == 0) goto loc_00502E63;
    v_stack_m48C = 32;
    goto loc_00502E48;
loc_00502E63:
loc_00502E68:
    v_r15 = (unsigned int)(((unsigned int)(v_stack_m488)) - ((unsigned int)(v_r13)));
    v_r15 = (unsigned int)((v_r15) - ((unsigned int)((unsigned int)(v_stack_m4A4))));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (12));
    result = 43;
    if (!(condition_is_not_equal)) {
        a1 = 32;
        a4 = v_stack_m4A8;
        a3 = v_stack_m470;
        a2 = (unsigned int)(v_r15);
        result = write_multi_char(a1, a2, a3, a4);
    }
    result = write_string(v_stack_m48C, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4A4))), v_stack_m470, v_stack_m4A8);
    if (((unsigned int)(v_rsi)) == 8) {
        a1 = 48;
        a4 = v_stack_m4A8;
        a3 = v_stack_m470;
        a2 = (unsigned int)(v_r15);
        result = write_multi_char(a1, a2, a3, a4);
    }
    if (v_stack_m498 != 0) goto loc_00502F43;
    if (condition_is_less_or_equal) goto loc_00502F43;
loc_00502ED7:
    result = mbtowc(v_stack_m49C, v_rbx, (int)(*(unsigned int *)(v_rip + 9467938)), a4);
    v_r11 = 0;
    result = (((unsigned int)((int)((unsigned int)(result)))) == 2) ? 1 : 0;
    result = (unsigned int)((result) + 1);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) - ((unsigned int)(result)));
    if (condition_is_less_or_equal) goto loc_00502F2E;
    result = write_char(v_stack_m49C, v_stack_m470, v_stack_m4A8, a4);
    v_r11 = 0;
    v_r14 = (v_rbx) + ((int)((unsigned int)(result)));
    if (condition_is_greater) goto loc_00502ED7;
    goto loc_00502F59;
loc_00502F2E:
    v_r14 = (unsigned int)((v_r14) | (0xFFFFFFFFULL));
    v_stack_m4A8 = (unsigned int)(v_r14);
    goto loc_00502F5E;
loc_00502F43:
    result = write_string(v_rbx, (unsigned int)((unsigned int)(v_r13)), v_stack_m470, v_stack_m4A8);
    v_r11 = 0;
loc_00502F59:
loc_00502F5E:
    if (sign_flag) goto loc_00502FE6;
    if ((((unsigned __int8)(v_rdi)) & (4)) == 0) goto loc_00502FE6;
    result = write_multi_char(32, (unsigned int)((unsigned int)(v_r15)), v_stack_m470, v_stack_m4A8);
loc_00502F82:
    v_r11 = 0;
loc_00502F8A:
loc_00502F8F:
loc_00502F94:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m460)) != 0) goto loc_005029EC;
loc_00502FA8:
    goto loc_00503217;
loc_00502FB0:
    v_r15 = (v_stack_m480) + (8);
    v_stack_m480 = v_r15;
    result = get_printf_count_output(32, (unsigned int)((unsigned int)(v_r15)), v_stack_m470, *(unsigned __int16 *)(v_stack_m460));
    v_r11 = 0;
    if ((unsigned int)(result) == 0) goto loc_00503200;
    if ((((unsigned __int8)(v_r11 + 32)) & ((unsigned __int8)(v_rdi))) == 0) goto loc_00502FDB;
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m470)) = (unsigned __int16)((unsigned int)(v_stack_m4A8));
    goto loc_00502FDE;
loc_00502FDB:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m470)) = (unsigned int)((unsigned int)(v_stack_m4A8));
loc_00502FDE:
    v_stack_m478 = 1;
loc_00502FE6:
    goto loc_00502F94;
loc_00502FF1:
    if (((unsigned int)((unsigned int)((unsigned int)(v_r15)))) == 73) goto loc_00503020;
    if (((unsigned int)((unsigned int)((unsigned int)(v_r15)))) == 104) goto loc_00503076;
    if (((unsigned int)((unsigned int)((unsigned int)(v_r15)))) == ((unsigned int)(73 + 33))) goto loc_00503025;
    if (((unsigned int)((unsigned int)((unsigned int)(v_r15)))) == ((unsigned int)(73 + 35))) goto loc_00503055;
    if (((unsigned int)((unsigned int)((unsigned int)(v_r15)))) == 116) goto loc_00503020;
    if (((unsigned int)((unsigned int)((unsigned int)(v_r15)))) == 119) goto loc_0050304C;
    if (((unsigned int)((unsigned int)((unsigned int)(v_r15)))) != 122) goto loc_00502F8F;
loc_00503020:
loc_00503025:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m460))) != 73) goto loc_0050309E;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m460))) != 54) goto loc_00503082;
    if ((*(unsigned __int16 *)(v_stack_m460 + 2)) != 52) goto loc_005030A8;
    v_r12 = (v_stack_m460) + (4);
    goto loc_00502F8F;
loc_0050304C:
    goto loc_00502F8F;
loc_00503055:
    if ((*(unsigned __int16 *)(v_r12)) != ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m460)))) goto loc_0050306E;
    v_r12 = (v_r12) + (2);
    goto loc_00502F94;
loc_0050306E:
    v_rdi = (unsigned int)((v_rdi) | (16));
    goto loc_00502F94;
loc_00503076:
    v_rdi = (unsigned int)((v_rdi) | (32));
    goto loc_00502F94;
loc_00503082:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m460))) != 51) goto loc_005030A8;
    if ((*(unsigned __int16 *)(v_r12 + 2)) != 50) goto loc_005030A8;
    v_r12 = (v_r12) + (4);
    goto loc_00502F8F;
loc_0050309E:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m460))) == ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m460)))) goto loc_00502F8F;
loc_005030A8:
    result = (unsigned __int16)((*(unsigned __int16 *)(v_r12)) - (88));
    if (((unsigned __int16)(result)) > 32) goto loc_005030CF;
    if (((unsigned __int16)(result)) < 32) goto loc_00502F8F;
loc_005030CF:
    v_stack_m494 = 0;
loc_005030D4:
    v_stack_m498 = 1;
    result = write_char((unsigned __int16)(*(unsigned __int16 *)(v_stack_m460)), v_stack_m470, v_stack_m4A8, *(unsigned __int16 *)(v_stack_m460));
    goto loc_00502F82;
loc_005030F4:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m460))) != 42) goto loc_00503124;
    v_r15 = (v_r15) + (8);
    v_stack_m480 = v_r15;
    v_stack_m4A0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m4A8)));
    if (!sign_flag) goto loc_00502F94;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m4A8))) | (0xFFFFFFFFULL));
    v_stack_m4A0 = (unsigned int)(v_rsi);
    goto loc_00502F94;
loc_00503124:
    v_stack_m4A0 = (unsigned int)(v_stack_m470 + v_rsi + v_rsi * 4 - 24 * 2);
    goto loc_00502F8F;
loc_00503136:
    v_stack_m4A0 = 0;
    goto loc_00502F8F;
loc_00503143:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m460))) != 42) goto loc_00503177;
    v_r15 = (v_r15) + (8);
    v_stack_m480 = v_r15;
    if (sign_flag) {
        v_rdi = (unsigned int)((v_rdi) | (4));
    }
    a3 = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_stack_m4A8))));
    if (!sign_flag) { a3 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m4A8))))); }
    v_stack_m488 = (unsigned int)(a3);
    goto loc_00502F8F;
loc_00503177:
    v_stack_m488 = (unsigned int)(v_stack_m470 + (unsigned int)(v_stack_m488) + (unsigned int)(v_stack_m488) * 4 - 24 * 2);
    goto loc_00502F8F;
loc_0050318D:
    if (((unsigned int)(v_stack_m470)) == 32) goto loc_005031D5;
    if (((unsigned int)(v_stack_m470)) == 35) goto loc_005031CC;
    if (((unsigned int)(v_stack_m470)) == ((unsigned int)(32 + 11))) goto loc_005031C4;
    if (((unsigned int)(v_stack_m470)) == ((unsigned int)(32 + 13))) goto loc_005031BC;
    if (((unsigned int)(v_stack_m470)) != ((unsigned int)(32 + 16))) goto loc_00502F94;
    v_rdi = (unsigned int)((v_rdi) | (8));
    goto loc_00502F94;
loc_005031BC:
    v_rdi = (unsigned int)((v_rdi) | (4));
    goto loc_00502F94;
loc_005031C4:
    v_rdi = (unsigned int)((v_rdi) | (1));
    goto loc_00502F94;
loc_005031CC:
    goto loc_00502F94;
loc_005031D5:
    v_rdi = (unsigned int)((v_rdi) | (2));
    goto loc_00502F94;
loc_005031DD:
    v_rsi = (unsigned int)((0) | (0xFFFFFFFFULL));
    v_stack_m478 = 0;
    v_stack_m4A0 = (unsigned int)(v_rsi);
    v_stack_m488 = 0;
    v_stack_m4A4 = 0;
    v_stack_m498 = 0;
    goto loc_00502F8F;
loc_00503200:
    a4 = 0;
    v_stack_m4B8 = 0;
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = EmpCheckErrataList(a1, a2, a3, a4);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
loc_00503217:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (0x4A0ULL);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t woutput_l(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
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
    uint64_t v_stack_m249;
    uint64_t v_stack_m3D8;
    uint64_t v_stack_m448;
    uint64_t v_stack_m460;
    uint32_t v_stack_m468;
    uint64_t v_stack_m470;
    uint32_t v_stack_m478;
    uint64_t v_stack_m48;
    uint64_t v_stack_m480;
    uint32_t v_stack_m488;
    uint16_t v_stack_m48A;
    uint16_t v_stack_m48C;
    uint8_t v_stack_m48F;
    uint64_t v_stack_m490;
    uint32_t v_stack_m494;
    uint32_t v_stack_m498;
    uint16_t v_stack_m49C;
    uint32_t v_stack_m4A0;
    uint32_t v_stack_m4A4;
    uint32_t v_stack_m4A8;
    uint64_t v_stack_m4B8;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (0x4A0ULL);
    result = (*(uint64_t *)(v_rip + 0x907DDE)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m470 = Arg1;
    Arg1 = 0;
    v_stack_m480 = Arg4;
    v_stack_m468 = 0;
    v_stack_m488 = 0;
    v_stack_m4A0 = 0;
    v_stack_m4A4 = 0;
    v_stack_m478 = 0;
    Arg2 = 0;
    result = memset(v_stack_m448, Arg2, (uint32_t)(0x400ULL), Arg4);
    local_r11 = 0;
    v_stack_m49C = 0;
    v_stack_m498 = 0;
    if (0 == 0) goto loc_00503200;
    if (0 == 0) goto loc_00503200;
    v_stack_m4A8 = 0;
    if ((uint16_t)(*(uint16_t *)(Arg2)) == 0) goto loc_00502FA8;
loc_005029EC:
    local_r12 = (Arg2) + (2);
    v_stack_m460 = local_r12;
    if (sign_flag) goto loc_00502FA8;
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(Arg2))) - ((uint16_t)(0 + 32)));
    if (((uint16_t)(result)) > 90) goto loc_00502A23;
    Arg1 = (uint32_t)(((int8_t)(*(uint8_t *)((uint16_t)(*(uint16_t *)(Arg2)) + v_rip - 0x4E3A79 * 1 - 0x20))) & (15));
    goto loc_00502A26;
loc_00502A23:
loc_00502A26:
    local_r10 = (uint32_t)(((int8_t)(*(uint8_t *)((int32_t)((uint32_t)(0 + 0x0 * 8)) + v_rip - 0x4E3A98 * 1))) >> (4));
    v_stack_m494 = (uint32_t)(local_r10);
    if ((uint32_t)(local_r10) == 0) goto loc_005030D4;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) - (1));
    if (condition_is_equal) goto loc_005031DD;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0050318D;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00503143;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00503136;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_005030F4;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00502FF1;
    if (((uint32_t)(Arg1)) != 1) goto loc_00502F8F;
    if (((uint32_t)((uint16_t)(*(uint16_t *)(Arg2)))) > 105) goto loc_00502C65;
    if (((uint32_t)((uint16_t)(*(uint16_t *)(Arg2)))) == 105) goto loc_00502ACD;
    Arg2 = (uint32_t)(((uint16_t)(*(uint16_t *)(Arg2))) - (67));
    if (condition_is_equal) goto loc_00502BEE;
    Arg2 = (uint32_t)((Arg2) - (16));
    if (condition_is_equal) goto loc_00502B82;
    Arg2 = (uint32_t)((Arg2) - (5));
    if (condition_is_equal) goto loc_00502CDE;
    Arg2 = (uint32_t)((Arg2) - (2));
    if (condition_is_equal) goto loc_00502B06;
    Arg2 = (uint32_t)((Arg2) - (9));
    if (condition_is_equal) goto loc_00502BFF;
    if (((uint32_t)(Arg2)) != ((uint32_t)(Arg1))) goto loc_00502E14;
loc_00502ACD:
    local_rdi = (uint32_t)((0) | (64));
loc_00502AD0:
loc_00502AD6:
loc_00502ADB:
    local_r15 = (Arg4) + (8);
    v_stack_m480 = local_r15;
    if (condition_is_below) goto loc_00502AF4;
    if (condition_is_above_or_equal) goto loc_00502D2F;
loc_00502AF4:
    if ((((uint8_t)(local_rdi)) & (64)) == 0) goto loc_00502D66;
    goto loc_00502D55;
loc_00502B06:
    local_r15 = (local_r15) + (8);
    v_stack_m480 = local_r15;
    if (*(uint64_t *)(Arg4) == 0) goto loc_00502B66;
    if (*(uint64_t *)(*(uint64_t *)(Arg4) + 0x8) == 0) goto loc_00502B66;
    if ((*(uint16_t *)(*(uint64_t *)(Arg4) + 0x2)) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg4))))) goto loc_00503200;
    if ((*(uint16_t *)(*(uint64_t *)(Arg4) + 0x2)) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg4))))) goto loc_00502B5C;
    result = (uint32_t)(~(*(uint16_t *)(*(uint64_t *)(Arg4))));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_00503200;
    result = (uint32_t)(~((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(Arg4) + 0x8)))));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_00503200;
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(Arg4))))) >> (1));
    v_stack_m498 = 1;
    goto loc_00502E14;
loc_00502B5C:
    v_stack_m498 = 0;
    goto loc_00502E14;
loc_00502B66:
    local_r13 = (local_r13) | (-1);
loc_00502B74:
    local_r13 = (local_r13) + 1;
    if ((*(uint8_t *)(v_rip - 0x4E3BD5 + local_r13 * 1)) != 0) goto loc_00502B74;
    goto loc_00502E14;
loc_00502B82:
    if ((((uint32_t)(local_rdi)) & (0x830ULL)) == 0) {
        local_rdi = (uint32_t)((local_rdi) | (32));
    }
    Arg1 = 0;
    if (0 == -1) { Arg1 = (uint32_t)((uint32_t)(0x7FFFFFFFULL)); }
    local_r15 = (local_r15) + (8);
    v_stack_m480 = local_r15;
    if (((32) & ((uint8_t)(local_rdi))) == 0) goto loc_00502C9C;
    result = *(uint64_t *)(Arg4);
    local_rbx = *(uint64_t *)(Arg4);
    if (*(uint64_t *)(Arg4) == 0) {
        Arg2 = v_rip - 5127212;
        local_rbx = Arg2;
        result = Arg2;
    }
    if (condition_is_less_or_equal) goto loc_00502E1A;
loc_00502BD5:
    if ((*(uint8_t *)(result)) == 0) goto loc_00502E1A;
    result = (result) + 1;
    local_r13 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r13)) < ((uint32_t)(Arg1))) goto loc_00502BD5;
    goto loc_00502E1A;
loc_00502BEE:
    if ((((uint32_t)(local_rdi)) & (0x830ULL)) != 0) goto loc_00502C04;
    local_rdi = (uint32_t)((local_rdi) | (32));
    goto loc_00502C04;
loc_00502BFF:
loc_00502C04:
    local_r15 = (local_r15) + (8);
    v_stack_m498 = 1;
    v_stack_m480 = local_r15;
    v_stack_m49C = (uint16_t)(*(uint16_t *)(32));
    if (((32) & ((uint8_t)(local_rdi))) == 0) goto loc_00502C52;
    v_stack_m490 = (uint8_t)(*(uint16_t *)(32));
    v_stack_m48F = 0;
    result = mbtowc(v_stack_m448, v_stack_m490, (int32_t)(*(uint32_t *)(v_rip + 0x907AD6)), *(uint16_t *)(Arg2));
    local_r11 = 0;
    if (!sign_flag) goto loc_00502C56;
    v_stack_m478 = 1;
    goto loc_00502C56;
loc_00502C52:
    v_stack_m448 = (uint16_t)(result);
loc_00502C56:
    goto loc_00502E14;
loc_00502C65:
    Arg2 = (uint32_t)((v_stack_m490) - (110));
    if (condition_is_equal) goto loc_00502FB0;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00502D12;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00502CD5;
    Arg2 = (uint32_t)((Arg2) - (3));
    if (condition_is_equal) goto loc_00502B8D;
    Arg2 = (uint32_t)((Arg2) - (2));
    if (condition_is_equal) goto loc_00502AD0;
    if (((uint32_t)(Arg2)) != 3) goto loc_00502E14;
    goto loc_00502CE3;
loc_00502C9C:
    v_stack_m498 = 1;
    result = v_rip - 5078454;
    if (v_stack_m448 != 0) { result = v_stack_m448; }
    goto loc_00502CC3;
loc_00502CB7:
    Arg1 = (uint32_t)((v_stack_m448) - 1);
    if ((*(uint16_t *)(result)) == 0) goto loc_00502CC7;
    result = (result) + (2);
loc_00502CC3:
    if ((uint32_t)(Arg1) != 0) goto loc_00502CB7;
loc_00502CC7:
    result = (result) - (result);
    result = (result) >> (1);
    goto loc_00502E1A;
loc_00502CD5:
loc_00502CDE:
loc_00502CE3:
    v_stack_m468 = 7;
    result = 7;
    if (sign_flag) {
        Arg1 = 48;
        v_stack_m4A4 = 2;
        result = (uint16_t)((7) + (81));
        v_stack_m48C = (uint16_t)(Arg1);
        v_stack_m48A = (uint16_t)(result);
    }
    goto loc_00502AD6;
loc_00502D12:
    if (!sign_flag) goto loc_00502AD6;
    local_rdi = (uint32_t)((local_rdi) | (512));
    goto loc_00502ADB;
loc_00502D2F:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (64));
    if (((32) & ((uint8_t)(local_rdi))) == 0) goto loc_00502D4E;
    if ((uint32_t)(result) == 0) goto loc_00502D48;
    goto loc_00502D55;
loc_00502D48:
    goto loc_00502D66;
loc_00502D4E:
    if ((uint32_t)(*(uint16_t *)((int32_t)(*(uint32_t *)(v_rip + 0x907AD6)))) == 0) goto loc_00502D63;
loc_00502D55:
    if (!sign_flag) goto loc_00502D66;
    result = -((int32_t)(*(uint32_t *)((int32_t)(*(uint32_t *)(v_rip + 0x907AD6)))));
    goto loc_00502D66;
loc_00502D63:
loc_00502D66:
    Arg3 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((int32_t)(*(uint32_t *)(v_rip + 0x907AD6))))));
    if ((((uint32_t)(local_rdi)) & (0x9000ULL)) != 0) { Arg3 = (uint32_t)(*(uint32_t *)((int32_t)(*(uint32_t *)(v_rip + 0x907AD6)))); }
    if (!sign_flag) goto loc_00502D7E;
    goto loc_00502D86;
loc_00502D7E:
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFF7ULL));
    local_rsi = 1;
    if (1 > 512) { local_rsi = 512; }
loc_00502D86:
    result = -(Arg3);
    Arg1 = (uint32_t)((32) & (v_stack_m4A4));
    v_stack_m4A4 = (uint32_t)(Arg1);
loc_00502DA5:
    local_rsi = (uint32_t)((local_rsi) - 1);
    if (condition_is_greater) goto loc_00502DB2;
    if (Arg3 == 0) goto loc_00502DCF;
loc_00502DB2:
    Arg2 = 0;
    Arg2 = (uint32_t)((Arg2) + (48));
    if (((uint32_t)(Arg2)) >= = 57) {
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)((uint32_t)(v_stack_m468))));
    }
    *(uint8_t *)(v_stack_m249) = (uint8_t)(Arg2);
    Arg1 = (v_stack_m249) - 1;
    goto loc_00502DA5;
loc_00502DCF:
    v_stack_m4A0 = (uint32_t)(local_rsi);
    local_r13 = (uint32_t)((v_stack_m249) - ((uint32_t)(Arg1)));
    if (condition_is_above_or_equal) goto loc_00502E11;
    if ((uint32_t)(local_r13) == 0) goto loc_00502DFF;
    v_stack_m480 = local_r15;
    v_stack_m4A4 = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
    local_rbx = Arg1 + 1;
    if ((*(uint8_t *)(Arg1 + 0x1)) != 48) {
        local_rbx = (Arg1 + 1) - 1;
        v_stack_m480 = local_r15;
        local_r13 = (uint32_t)((local_r13) + 1);
        v_stack_m4A4 = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
        *(uint8_t *)(local_rbx) = 48;
    }
    local_r11 = 0;
loc_00502E14:
loc_00502E1A:
    if (v_stack_m478 != 0) goto loc_00502F8A;
    if ((((uint8_t)(local_rdi)) & (64)) == 0) goto loc_00502E63;
    if (condition_is_above_or_equal) goto loc_00502E38;
    goto loc_00502E43;
loc_00502E38:
    if ((((uint8_t)(local_rdi)) & (1)) == 0) goto loc_00502E55;
loc_00502E43:
    v_stack_m48C = 43;
loc_00502E48:
    v_stack_m4A4 = 1;
    goto loc_00502E68;
loc_00502E55:
    if ((((uint8_t)(local_rdi)) & (2)) == 0) goto loc_00502E63;
    v_stack_m48C = 32;
    goto loc_00502E48;
loc_00502E63:
loc_00502E68:
    local_r15 = (uint32_t)(((uint32_t)(v_stack_m488)) - ((uint32_t)(local_r13)));
    local_r15 = (uint32_t)((local_r15) - ((uint32_t)((uint32_t)(v_stack_m4A4))));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (12));
    result = 43;
    if (!(condition_is_not_equal)) {
        Arg1 = 32;
        Arg4 = v_stack_m4A8;
        Arg3 = v_stack_m470;
        Arg2 = (uint32_t)(local_r15);
        result = write_multi_char(Arg1, Arg2, Arg3, Arg4);
    }
    result = write_string(v_stack_m48C, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4A4))), v_stack_m470, v_stack_m4A8);
    if (((uint32_t)(local_rsi)) == 8) {
        Arg1 = 48;
        Arg4 = v_stack_m4A8;
        Arg3 = v_stack_m470;
        Arg2 = (uint32_t)(local_r15);
        result = write_multi_char(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m498 != 0) goto loc_00502F43;
    if (condition_is_less_or_equal) goto loc_00502F43;
loc_00502ED7:
    result = mbtowc(v_stack_m49C, local_rbx, (int32_t)(*(uint32_t *)(v_rip + 0x907822)), Arg4);
    local_r11 = 0;
    result = (((uint32_t)((int32_t)((uint32_t)(result)))) == 2) ? 1 : 0;
    result = (uint32_t)((result) + 1);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) - ((uint32_t)(result)));
    if (condition_is_less_or_equal) goto loc_00502F2E;
    result = write_char(v_stack_m49C, v_stack_m470, v_stack_m4A8, Arg4);
    local_r11 = 0;
    local_r14 = (local_rbx) + ((int32_t)((uint32_t)(result)));
    if (condition_is_greater) goto loc_00502ED7;
    goto loc_00502F59;
loc_00502F2E:
    local_r14 = (uint32_t)((local_r14) | (0xFFFFFFFFULL));
    v_stack_m4A8 = (uint32_t)(local_r14);
    goto loc_00502F5E;
loc_00502F43:
    result = write_string(local_rbx, (uint32_t)((uint32_t)(local_r13)), v_stack_m470, v_stack_m4A8);
    local_r11 = 0;
loc_00502F59:
loc_00502F5E:
    if (sign_flag) goto loc_00502FE6;
    if ((((uint8_t)(local_rdi)) & (4)) == 0) goto loc_00502FE6;
    result = write_multi_char(32, (uint32_t)((uint32_t)(local_r15)), v_stack_m470, v_stack_m4A8);
loc_00502F82:
    local_r11 = 0;
loc_00502F8A:
loc_00502F8F:
loc_00502F94:
    if ((uint16_t)(*(uint16_t *)(v_stack_m460)) != 0) goto loc_005029EC;
loc_00502FA8:
    goto loc_00503217;
loc_00502FB0:
    local_r15 = (v_stack_m480) + (8);
    v_stack_m480 = local_r15;
    result = get_printf_count_output(32, (uint32_t)((uint32_t)(local_r15)), v_stack_m470, *(uint16_t *)(v_stack_m460));
    local_r11 = 0;
    if ((uint32_t)(result) == 0) goto loc_00503200;
    if ((((uint8_t)(local_r11 + 32)) & ((uint8_t)(local_rdi))) == 0) goto loc_00502FDB;
    *(uint16_t *)(*(uint64_t *)(v_stack_m470)) = (uint16_t)((uint32_t)(v_stack_m4A8));
    goto loc_00502FDE;
loc_00502FDB:
    *(uint32_t *)(*(uint64_t *)(v_stack_m470)) = (uint32_t)((uint32_t)(v_stack_m4A8));
loc_00502FDE:
    v_stack_m478 = 1;
loc_00502FE6:
    goto loc_00502F94;
loc_00502FF1:
    if (((uint32_t)((uint32_t)((uint32_t)(local_r15)))) == 73) goto loc_00503020;
    if (((uint32_t)((uint32_t)((uint32_t)(local_r15)))) == 104) goto loc_00503076;
    if (((uint32_t)((uint32_t)((uint32_t)(local_r15)))) == ((uint32_t)(73 + 33))) goto loc_00503025;
    if (((uint32_t)((uint32_t)((uint32_t)(local_r15)))) == ((uint32_t)(73 + 35))) goto loc_00503055;
    if (((uint32_t)((uint32_t)((uint32_t)(local_r15)))) == 116) goto loc_00503020;
    if (((uint32_t)((uint32_t)((uint32_t)(local_r15)))) == 119) goto loc_0050304C;
    if (((uint32_t)((uint32_t)((uint32_t)(local_r15)))) != 122) goto loc_00502F8F;
loc_00503020:
loc_00503025:
    if (((uint16_t)(*(uint16_t *)(v_stack_m460))) != 73) goto loc_0050309E;
    if (((uint16_t)(*(uint16_t *)(v_stack_m460))) != 54) goto loc_00503082;
    if ((*(uint16_t *)(v_stack_m460 + 0x2)) != 52) goto loc_005030A8;
    local_r12 = (v_stack_m460) + (4);
    goto loc_00502F8F;
loc_0050304C:
    goto loc_00502F8F;
loc_00503055:
    if ((*(uint16_t *)(local_r12)) != ((uint16_t)(*(uint16_t *)(v_stack_m460)))) goto loc_0050306E;
    local_r12 = (local_r12) + (2);
    goto loc_00502F94;
loc_0050306E:
    local_rdi = (uint32_t)((local_rdi) | (16));
    goto loc_00502F94;
loc_00503076:
    local_rdi = (uint32_t)((local_rdi) | (32));
    goto loc_00502F94;
loc_00503082:
    if (((uint16_t)(*(uint16_t *)(v_stack_m460))) != 51) goto loc_005030A8;
    if ((*(uint16_t *)(local_r12 + 0x2)) != 50) goto loc_005030A8;
    local_r12 = (local_r12) + (4);
    goto loc_00502F8F;
loc_0050309E:
    if (((uint16_t)(*(uint16_t *)(v_stack_m460))) == ((uint16_t)(*(uint16_t *)(v_stack_m460)))) goto loc_00502F8F;
loc_005030A8:
    result = (uint16_t)((*(uint16_t *)(local_r12)) - (88));
    if (((uint16_t)(result)) > 32) goto loc_005030CF;
    if (((uint16_t)(result)) < 32) goto loc_00502F8F;
loc_005030CF:
    v_stack_m494 = 0;
loc_005030D4:
    v_stack_m498 = 1;
    result = write_char((uint16_t)(*(uint16_t *)(v_stack_m460)), v_stack_m470, v_stack_m4A8, *(uint16_t *)(v_stack_m460));
    goto loc_00502F82;
loc_005030F4:
    if (((uint16_t)(*(uint16_t *)(v_stack_m460))) != 42) goto loc_00503124;
    local_r15 = (local_r15) + (8);
    v_stack_m480 = local_r15;
    v_stack_m4A0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m4A8)));
    if (!sign_flag) goto loc_00502F94;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m4A8))) | (0xFFFFFFFFULL));
    v_stack_m4A0 = (uint32_t)(local_rsi);
    goto loc_00502F94;
loc_00503124:
    v_stack_m4A0 = (uint32_t)(v_stack_m470 + local_rsi + local_rsi * 4 - 24 * 2);
    goto loc_00502F8F;
loc_00503136:
    v_stack_m4A0 = 0;
    goto loc_00502F8F;
loc_00503143:
    if (((uint16_t)(*(uint16_t *)(v_stack_m460))) != 42) goto loc_00503177;
    local_r15 = (local_r15) + (8);
    v_stack_m480 = local_r15;
    if (sign_flag) {
        local_rdi = (uint32_t)((local_rdi) | (4));
    }
    Arg3 = (uint32_t)(-((uint32_t)(*(uint32_t *)(v_stack_m4A8))));
    if (!sign_flag) { Arg3 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m4A8))))); }
    v_stack_m488 = (uint32_t)(Arg3);
    goto loc_00502F8F;
loc_00503177:
    v_stack_m488 = (uint32_t)(v_stack_m470 + (uint32_t)(v_stack_m488) + (uint32_t)(v_stack_m488) * 4 - 24 * 2);
    goto loc_00502F8F;
loc_0050318D:
    if (((uint32_t)(v_stack_m470)) == 32) goto loc_005031D5;
    if (((uint32_t)(v_stack_m470)) == 35) goto loc_005031CC;
    if (((uint32_t)(v_stack_m470)) == ((uint32_t)(32 + 11))) goto loc_005031C4;
    if (((uint32_t)(v_stack_m470)) == ((uint32_t)(32 + 13))) goto loc_005031BC;
    if (((uint32_t)(v_stack_m470)) != ((uint32_t)(32 + 16))) goto loc_00502F94;
    local_rdi = (uint32_t)((local_rdi) | (8));
    goto loc_00502F94;
loc_005031BC:
    local_rdi = (uint32_t)((local_rdi) | (4));
    goto loc_00502F94;
loc_005031C4:
    local_rdi = (uint32_t)((local_rdi) | (1));
    goto loc_00502F94;
loc_005031CC:
    goto loc_00502F94;
loc_005031D5:
    local_rdi = (uint32_t)((local_rdi) | (2));
    goto loc_00502F94;
loc_005031DD:
    local_rsi = (uint32_t)((0) | (0xFFFFFFFFULL));
    v_stack_m478 = 0;
    v_stack_m4A0 = (uint32_t)(local_rsi);
    v_stack_m488 = 0;
    v_stack_m4A4 = 0;
    v_stack_m498 = 0;
    goto loc_00502F8F;
loc_00503200:
    Arg4 = 0;
    v_stack_m4B8 = 0;
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = EmpCheckErrataList(Arg1, Arg2, Arg3, Arg4);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
loc_00503217:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (0x4A0ULL);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0050293C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
