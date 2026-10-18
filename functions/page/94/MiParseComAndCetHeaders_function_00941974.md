# MiParseComAndCetHeaders

- RVA: `0x00941974`–`0x00941DD0` (길이 `1,116` bytes)
- VA: `0x0000000140941974`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000902AC`
- 디코드: `270`개 명령, `1,116/1,116` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x009419B5` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009419FF` → [MiMapImageInSystemSpace](MiMapImageInSystemSpace_function_00941DD8.md) (function, `0x00941DD8`)
- `0x00941A13` → [MiReferenceControlAreaFile](../../text/43/MiReferenceControlAreaFile_function_00431554.md) (function, `0x00431554`)
- `0x00941A9C` → [MiLogRelocationRva](MiLogRelocationRva_function_009420DC.md) (function, `0x009420DC`)
- `0x00941B4F` → [MiLogRelocationRva](MiLogRelocationRva_function_009420DC.md) (function, `0x009420DC`)
- `0x00941BCE` → [MiUnmapImageInSystemSpace](MiUnmapImageInSystemSpace_function_0094206C.md) (function, `0x0094206C`)
- `0x00941BDE` → [MiDereferenceControlAreaFile](../../text/43/MiDereferenceControlAreaFile_function_004345E0.md) (function, `0x004345E0`)
- `0x00941BF0` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00941D00` → [MiLogRelocationRva](MiLogRelocationRva_function_009420DC.md) (function, `0x009420DC`)

### Direct callers
- [MiCreateNewSection](../98/MiCreateNewSection_function_00985DB0.md) at `0x00986017`

### Static image references
- `0x00941987` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x009419B5` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00941A13` → [MiReferenceControlAreaFile](../../text/43/MiReferenceControlAreaFile_function_00431554.md) (`PAGE` → `.text`)
  - `0x00941BDE` → [MiDereferenceControlAreaFile](../../text/43/MiDereferenceControlAreaFile_function_004345E0.md) (`PAGE` → `.text`)
  - `0x00941BF0` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00941974  40 53                           push rbx
00941976  56                              push rsi
00941977  57                              push rdi
00941978  41 54                           push r12
0094197A  41 55                           push r13
0094197C  41 56                           push r14
0094197E  41 57                           push r15
00941980  48 81 EC 30 01 00 00            sub rsp, 0x130
00941987  48 8B 05 B2 8D 4C 00            mov rax, qword ptr [rip + 0x4c8db2]
0094198E  48 33 C4                        xor rax, rsp
00941991  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
00941999  49 8B F0                        mov rsi, r8
0094199C  4C 8B FA                        mov r15, rdx
0094199F  4C 8B E9                        mov r13, rcx
009419A2  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
009419A7  33 D2                           xor edx, edx
009419A9  44 8D 42 50                     lea r8d, [rdx + 0x50]
009419AD  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
009419B5  E8 86 52 D8 FF                  call 0x1406c6c40
009419BA  33 DB                           xor ebx, ebx
009419BC  48 21 5C 24 40                  and qword ptr [rsp + 0x40], rbx
009419C1  88 1E                           mov byte ptr [rsi], bl
009419C3  41 8B 4F 50                     mov ecx, dword ptr [r15 + 0x50]
009419C7  85 C9                           test ecx, ecx
009419C9  0F 85 8D 02 00 00               jne 0x140941c5c
009419CF  41 BE 01 00 00 00               mov r14d, 1
009419D5  41 8B 47 68                     mov eax, dword ptr [r15 + 0x68]
009419D9  85 C0                           test eax, eax
009419DB  0F 85 39 02 00 00               jne 0x140941c1a
009419E1  41 BC 02 00 00 00               mov r12d, 2
009419E7  85 DB                           test ebx, ebx
009419E9  0F 84 99 03 00 00               je 0x140941d88
009419EF  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
009419F7  BA 03 00 00 00                  mov edx, 3
009419FC  49 8B CD                        mov rcx, r13
009419FF  E8 D4 03 00 00                  call 0x140941dd8
00941A04  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
00941A08  85 C0                           test eax, eax
00941A0A  0F 88 42 02 00 00               js 0x140941c52
00941A10  49 8B CD                        mov rcx, r13
00941A13  E8 3C FB AE FF                  call 0x140431554
00941A18  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00941A1D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00941A22  83 CB 0C                        or ebx, 0xc
00941A25  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00941A29  49 8B 7D 00                     mov rdi, qword ptr [r13]
00941A2D  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
00941A35  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
00941A3A  41 84 DE                        test r14b, bl
00941A3D  0F 85 53 02 00 00               jne 0x140941c96
00941A43  41 84 DC                        test r12b, bl
00941A46  0F 84 06 02 00 00               je 0x140941c52
00941A4C  41 8B 77 68                     mov esi, dword ptr [r15 + 0x68]
00941A50  48 03 74 24 48                  add rsi, qword ptr [rsp + 0x48]
00941A55  45 33 C0                        xor r8d, r8d
00941A58  44 89 44 24 28                  mov dword ptr [rsp + 0x28], r8d
00941A5D  41 8B 4F 6C                     mov ecx, dword ptr [r15 + 0x6c]
00941A61  48 B8 93 24 49 92 24 49 92 24   movabs rax, 0x2492492492492493
00941A6B  48 F7 E1                        mul rcx
00941A6E  48 2B CA                        sub rcx, rdx
00941A71  48 D1 E9                        shr rcx, 1
00941A74  48 03 CA                        add rcx, rdx
00941A77  48 C1 E9 04                     shr rcx, 4
00941A7B  41 8B C0                        mov eax, r8d
00941A7E  48 3B C1                        cmp rax, rcx
00941A81  0F 83 CB 01 00 00               jae 0x140941c52
00941A87  41 6B C8 1C                     imul ecx, r8d, 0x1c
00941A8B  41 03 4F 68                     add ecx, dword ptr [r15 + 0x68]
00941A8F  4D 8B CD                        mov r9, r13
00941A92  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00941A97  BA 1C 00 00 00                  mov edx, 0x1c
00941A9C  E8 3B 06 00 00                  call 0x1409420dc
00941AA1  90                              nop
00941AA2  0F 10 06                        movups xmm0, xmmword ptr [rsi]
00941AA5  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
00941AAA  F2 0F 10 4E 10                  movsd xmm1, qword ptr [rsi + 0x10]
00941AAF  F2 0F 11 4C 24 68               movsd qword ptr [rsp + 0x68], xmm1
00941AB5  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
00941AB8  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00941ABC  EB 23                           jmp 0x140941ae1
00941ABE  8B F8                           mov edi, eax
00941AC0  48 8B 74 24 30                  mov rsi, qword ptr [rsp + 0x30]
00941AC5  8B 5C 24 20                     mov ebx, dword ptr [rsp + 0x20]
00941AC9  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
00941ACE  3D 05 00 00 C0                  cmp eax, 0xc0000005
00941AD3  75 07                           jne 0x140941adc
00941AD5  33 FF                           xor edi, edi
00941AD7  E9 E5 00 00 00                  jmp 0x140941bc1
00941ADC  E9 E0 00 00 00                  jmp 0x140941bc1
00941AE1  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00941AE6  48 C1 E8 20                     shr rax, 0x20
00941AEA  83 F8 14                        cmp eax, 0x14
00941AED  0F 85 16 01 00 00               jne 0x140941c09
00941AF3  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00941AF8  48 C1 E9 20                     shr rcx, 0x20
00941AFC  85 C9                           test ecx, ecx
00941AFE  0F 84 4E 01 00 00               je 0x140941c52
00941B04  F6 C1 03                        test cl, 3
00941B07  0F 85 45 01 00 00               jne 0x140941c52
00941B0D  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
00941B11  85 C0                           test eax, eax
00941B13  0F 84 39 01 00 00               je 0x140941c52
00941B19  A8 03                           test al, 3
00941B1B  0F 85 31 01 00 00               jne 0x140941c52
00941B21  41 8B 57 10                     mov edx, dword ptr [r15 + 0x10]
00941B25  3B C2                           cmp eax, edx
00941B27  0F 83 25 01 00 00               jae 0x140941c52
00941B2D  3B CA                           cmp ecx, edx
00941B2F  0F 83 1D 01 00 00               jae 0x140941c52
00941B35  03 C1                           add eax, ecx
00941B37  3B C2                           cmp eax, edx
00941B39  0F 83 13 01 00 00               jae 0x140941c52
00941B3F  4D 8B CD                        mov r9, r13
00941B42  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00941B47  4C 8B C6                        mov r8, rsi
00941B4A  BA 04 00 00 00                  mov edx, 4
00941B4F  E8 88 05 00 00                  call 0x1409420dc
00941B54  8B 4C 24 6C                     mov ecx, dword ptr [rsp + 0x6c]
00941B58  48 03 4C 24 48                  add rcx, qword ptr [rsp + 0x48]
00941B5D  8B 09                           mov ecx, dword ptr [rcx]
00941B5F  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
00941B63  EB 12                           jmp 0x140941b77
00941B65  8B F8                           mov edi, eax
00941B67  48 8B 74 24 30                  mov rsi, qword ptr [rsp + 0x30]
00941B6C  8B 5C 24 20                     mov ebx, dword ptr [rsp + 0x20]
00941B70  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
00941B75  EB 4A                           jmp 0x140941bc1
00941B77  41 84 CE                        test r14b, cl
00941B7A  74 08                           je 0x140941b84
00941B7C  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
00941B80  44 09 70 4C                     or dword ptr [rax + 0x4c], r14d
00941B84  41 84 CC                        test r12b, cl
00941B87  0F 85 02 02 00 00               jne 0x140941d8f
00941B8D  F6 C1 04                        test cl, 4
00941B90  0F 85 06 02 00 00               jne 0x140941d9c
00941B96  F6 C1 08                        test cl, 8
00941B99  0F 85 0A 02 00 00               jne 0x140941da9
00941B9F  F6 C1 10                        test cl, 0x10
00941BA2  0F 85 0E 02 00 00               jne 0x140941db6
00941BA8  F6 C1 20                        test cl, 0x20
00941BAB  0F 85 12 02 00 00               jne 0x140941dc3
00941BB1  84 C9                           test cl, cl
00941BB3  79 08                           jns 0x140941bbd
00941BB5  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
00941BB9  83 48 4C 40                     or dword ptr [rax + 0x4c], 0x40
00941BBD  8B 7C 24 24                     mov edi, dword ptr [rsp + 0x24]
00941BC1  F6 C3 04                        test bl, 4
00941BC4  74 0D                           je 0x140941bd3
00941BC6  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
00941BCE  E8 99 04 00 00                  call 0x14094206c
00941BD3  83 FB 08                        cmp ebx, 8
00941BD6  72 0B                           jb 0x140941be3
00941BD8  48 8B D6                        mov rdx, rsi
00941BDB  49 8B CD                        mov rcx, r13
00941BDE  E8 FD 29 AF FF                  call 0x1404345e0
00941BE3  8B C7                           mov eax, edi
00941BE5  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
00941BED  48 33 CC                        xor rcx, rsp
00941BF0  E8 4B AA D6 FF                  call 0x1406ac640
00941BF5  48 81 C4 30 01 00 00            add rsp, 0x130
00941BFC  41 5F                           pop r15
00941BFE  41 5E                           pop r14
00941C00  41 5D                           pop r13
00941C02  41 5C                           pop r12
00941C04  5F                              pop rdi
00941C05  5E                              pop rsi
00941C06  5B                              pop rbx
00941C07  C3                              ret
00941C08  CC                              int3
00941C09  48 83 C6 1C                     add rsi, 0x1c
00941C0D  44 8B 44 24 28                  mov r8d, dword ptr [rsp + 0x28]
00941C12  45 03 C6                        add r8d, r14d
00941C15  E9 3E FE FF FF                  jmp 0x140941a58
00941C1A  A8 03                           test al, 3
00941C1C  0F 85 BF FD FF FF               jne 0x1409419e1
00941C22  41 8B 4F 6C                     mov ecx, dword ptr [r15 + 0x6c]
00941C26  83 F9 1C                        cmp ecx, 0x1c
00941C29  0F 82 B2 FD FF FF               jb 0x1409419e1
00941C2F  8D 14 01                        lea edx, [rcx + rax]
00941C32  3B D0                           cmp edx, eax
00941C34  0F 86 A7 FD FF FF               jbe 0x1409419e1
00941C3A  41 3B 57 10                     cmp edx, dword ptr [r15 + 0x10]
00941C3E  0F 87 9D FD FF FF               ja 0x1409419e1
00941C44  41 BC 02 00 00 00               mov r12d, 2
00941C4A  41 0B DC                        or ebx, r12d
00941C4D  E9 95 FD FF FF                  jmp 0x1409419e7
00941C52  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00941C57  E9 61 FF FF FF                  jmp 0x140941bbd
00941C5C  F6 C1 03                        test cl, 3
00941C5F  0F 85 6A FD FF FF               jne 0x1409419cf
00941C65  41 8B 47 54                     mov eax, dword ptr [r15 + 0x54]
00941C69  83 F8 48                        cmp eax, 0x48
00941C6C  0F 82 5D FD FF FF               jb 0x1409419cf
00941C72  03 C1                           add eax, ecx
00941C74  3B C1                           cmp eax, ecx
00941C76  0F 86 53 FD FF FF               jbe 0x1409419cf
00941C7C  48 83 C1 48                     add rcx, 0x48
00941C80  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
00941C84  41 BE 01 00 00 00               mov r14d, 1
00941C8A  48 3B C8                        cmp rcx, rax
00941C8D  41 0F 46 DE                     cmovbe ebx, r14d
00941C91  E9 3F FD FF FF                  jmp 0x1409419d5
00941C96  45 8B 57 50                     mov r10d, dword ptr [r15 + 0x50]
00941C9A  4A 8D 0C 12                     lea rcx, [rdx + r10]
00941C9E  0F 10 01                        movups xmm0, xmmword ptr [rcx]
00941CA1  0F 29 84 24 D0 00 00 00         movaps xmmword ptr [rsp + 0xd0], xmm0
00941CA9  0F 10 49 10                     movups xmm1, xmmword ptr [rcx + 0x10]
00941CAD  0F 29 8C 24 E0 00 00 00         movaps xmmword ptr [rsp + 0xe0], xmm1
00941CB5  0F 10 41 20                     movups xmm0, xmmword ptr [rcx + 0x20]
00941CB9  0F 29 84 24 F0 00 00 00         movaps xmmword ptr [rsp + 0xf0], xmm0
00941CC1  0F 10 49 30                     movups xmm1, xmmword ptr [rcx + 0x30]
00941CC5  0F 29 8C 24 00 01 00 00         movaps xmmword ptr [rsp + 0x100], xmm1
00941CCD  F2 0F 10 41 40                  movsd xmm0, qword ptr [rcx + 0x40]
00941CD2  F2 0F 11 84 24 10 01 00 00      movsd qword ptr [rsp + 0x110], xmm0
00941CDB  EB 15                           jmp 0x140941cf2
00941CDD  8B F8                           mov edi, eax
00941CDF  48 8B 74 24 30                  mov rsi, qword ptr [rsp + 0x30]
00941CE4  8B 5C 24 20                     mov ebx, dword ptr [rsp + 0x20]
00941CE8  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
00941CED  E9 CF FE FF FF                  jmp 0x140941bc1
00941CF2  4D 8B CD                        mov r9, r13
00941CF5  4C 8B C0                        mov r8, rax
00941CF8  BA 48 00 00 00                  mov edx, 0x48
00941CFD  41 8B CA                        mov ecx, r10d
00941D00  E8 D7 03 00 00                  call 0x1409420dc
00941D05  44 8B 84 24 E0 00 00 00         mov r8d, dword ptr [rsp + 0xe0]
00941D0D  45 84 C6                        test r14b, r8b
00941D10  0F 84 2D FD FF FF               je 0x140941a43
00941D16  44 88 36                        mov byte ptr [rsi], r14b
00941D19  B8 00 40 00 00                  mov eax, 0x4000
00941D1E  66 09 47 0C                     or word ptr [rdi + 0xc], ax
00941D22  66 44 39 A4 24 D4 00 00 00      cmp word ptr [rsp + 0xd4], r12w
00941D2B  77 15                           ja 0x140941d42
00941D2D  0F 85 10 FD FF FF               jne 0x140941a43
00941D33  66 83 BC 24 D6 00 00 00 05      cmp word ptr [rsp + 0xd6], 5
00941D3C  0F 82 01 FD FF FF               jb 0x140941a43
00941D42  48 8B 57 38                     mov rdx, qword ptr [rdi + 0x38]
00941D46  8A 4A 33                        mov cl, byte ptr [rdx + 0x33]
00941D49  41 0A CC                        or cl, r12b
00941D4C  88 4A 33                        mov byte ptr [rdx + 0x33], cl
00941D4F  41 8B C0                        mov eax, r8d
00941D52  25 02 00 02 00                  and eax, 0x20002
00941D57  41 3B C4                        cmp eax, r12d
00941D5A  0F 84 E3 FC FF FF               je 0x140941a43
00941D60  66 0F BA 67 0C 0F               bt word ptr [rdi + 0xc], 0xf
00941D66  0F 83 D7 FC FF FF               jae 0x140941a43
00941D6C  41 0A CE                        or cl, r14b
00941D6F  88 4A 33                        mov byte ptr [rdx + 0x33], cl
00941D72  41 0F BA E0 11                  bt r8d, 0x11
00941D77  0F 83 C6 FC FF FF               jae 0x140941a43
00941D7D  80 C9 20                        or cl, 0x20
00941D80  88 4A 33                        mov byte ptr [rdx + 0x33], cl
00941D83  E9 BB FC FF FF                  jmp 0x140941a43
00941D88  33 C0                           xor eax, eax
00941D8A  E9 56 FE FF FF                  jmp 0x140941be5
00941D8F  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
00941D93  44 09 60 4C                     or dword ptr [rax + 0x4c], r12d
00941D97  E9 F1 FD FF FF                  jmp 0x140941b8d
00941D9C  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
00941DA0  83 48 4C 04                     or dword ptr [rax + 0x4c], 4
00941DA4  E9 ED FD FF FF                  jmp 0x140941b96
00941DA9  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
00941DAD  83 48 4C 08                     or dword ptr [rax + 0x4c], 8
00941DB1  E9 E9 FD FF FF                  jmp 0x140941b9f
00941DB6  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
00941DBA  83 48 4C 10                     or dword ptr [rax + 0x4c], 0x10
00941DBE  E9 E5 FD FF FF                  jmp 0x140941ba8
00941DC3  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
00941DC7  83 48 4C 20                     or dword ptr [rax + 0x4c], 0x20
00941DCB  E9 E1 FD FF FF                  jmp 0x140941bb1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiParseComAndCetHeaders(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m140;
    unsigned int v_stack_m144;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mF8;
    unsigned int v_stack_mFC;
    unsigned __int64 v_stack_p100;
    unsigned __int64 v_stack_p110;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_pD0;
    unsigned __int16 v_stack_pD4;
    unsigned __int16 v_stack_pD6;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pF0;

    v_rsp = (v_rsp) - (304);
    result = (*(unsigned __int64 *)(v_rip + 5017010)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m130 = a1;
    a2 = 0;
    result = memset(v_stack_mE8, a2, a2 + 80, a4);
    v_rbx = 0;
    *(unsigned __int8 *)(a3) = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 80))) != 0) goto loc_00941C5C;
loc_009419CF:
loc_009419D5:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 104))) != 0) goto loc_00941C1A;
loc_009419E1:
loc_009419E7:
    if (0 == 0) goto loc_00941D88;
    result = MiMapImageInSystemSpace(a1, 3, v_stack_mE8, a4);
    v_stack_m144 = (unsigned int)(result);
    if (sign_flag) goto loc_00941C52;
    result = MiReferenceControlAreaFile(a1, 3, v_stack_mE8, a4);
    v_stack_m128 = result;
    v_stack_m138 = result;
    v_rbx = (unsigned int)((v_rbx) | (12));
    v_stack_m148 = (unsigned int)(v_rbx);
    v_stack_m120 = v_stack_mE8;
    if (((1) & ((unsigned __int8)(v_rbx))) != 0) goto loc_00941C96;
loc_00941A43:
    if (((2) & ((unsigned __int8)(v_rbx))) == 0) goto loc_00941C52;
    v_rsi = ((unsigned int)(*(unsigned int *)(a2 + 104))) + (v_stack_m120);
    a3 = 0;
loc_00941A58:
    v_stack_m140 = 0;
    a1 = ((unsigned int)(*(unsigned int *)(a2 + 108))) - (v_stack_mE8);
    a1 = (a1) >> (1);
    a1 = (a1) + (v_stack_mE8);
    a1 = (a1) >> (4);
    if (0 >= a1) goto loc_00941C52;
    a1 = (unsigned int)((a1) * (0));
    a1 = (unsigned int)((a1) + (*(unsigned int *)(a2 + 104)));
    result = MiLogRelocationRva(a1, 28, v_stack_m128, a1);
    v_stack_m110 = v_xmm0;
    v_stack_m100 = v_xmm1;
    v_stack_mF8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 24)));
    goto loc_00941AE1;
loc_00941AE1:
    result = (v_stack_m108) >> (32);
    if (((unsigned int)(result)) != 20) goto loc_00941C09;
    a1 = (v_stack_m100) >> (32);
    if ((unsigned int)(a1) == 0) goto loc_00941C52;
    if ((((unsigned __int8)(a1)) & (3)) != 0) goto loc_00941C52;
    if ((unsigned int)((unsigned int)(v_stack_m100)) == 0) goto loc_00941C52;
    if ((((unsigned __int8)((unsigned int)(v_stack_m100))) & (3)) != 0) goto loc_00941C52;
    if (((unsigned int)((unsigned int)(v_stack_m100))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16))))) goto loc_00941C52;
    if (((unsigned int)(a1)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16))))) goto loc_00941C52;
    result = (unsigned int)(((unsigned int)(v_stack_m100)) + ((unsigned int)(a1)));
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16))))) goto loc_00941C52;
    result = MiLogRelocationRva(a1, 4, v_stack_m128, a1);
    a1 = ((unsigned int)(v_stack_mFC)) + (v_stack_m120);
    v_stack_m118 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    goto loc_00941B77;
loc_00941B77:
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1))))) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56);
    }
    if (((2) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1))))) != 0) goto loc_00941D8F;
loc_00941B8D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (4)) != 0) goto loc_00941D9C;
loc_00941B96:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (8)) != 0) goto loc_00941DA9;
loc_00941B9F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (16)) != 0) goto loc_00941DB6;
loc_00941BA8:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (32)) != 0) goto loc_00941DC3;
loc_00941BB1:
    if (sign_flag) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 56);
    }
loc_00941BC1:
    if ((((unsigned __int8)(v_rbx)) & (4)) != 0) {
        a1 = v_stack_mE8;
        result = MiUnmapImageInSystemSpace(a1, 4, v_stack_m128, a1);
    }
    if (((unsigned int)(v_rbx)) >= 8) {
        a2 = v_stack_m128;
        a1 = a1;
        result = MiDereferenceControlAreaFile(a1, a2, v_stack_m128, a1);
    }
loc_00941BE5:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m128, a1);
    v_rsp = (v_rsp) + (304);
    return result;
loc_00941C09:
    v_rsi = (v_stack_m128) + (28);
    a3 = (unsigned int)(((unsigned int)(v_stack_p28)) + (1));
    goto loc_00941A58;
loc_00941C1A:
    if ((((unsigned __int8)(result)) & (3)) != 0) goto loc_009419E1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 108)))) < 28) goto loc_009419E1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 108)) + result * 1)) <= ((unsigned int)(result))) goto loc_009419E1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 108)) + result * 1)) > (*(unsigned int *)(a2 + 16))) goto loc_009419E1;
    v_rbx = (unsigned int)((v_rbx) | (2));
    goto loc_009419E7;
loc_00941C52:
    goto loc_00941BBD;
loc_00941C5C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 108)))) & (3)) != 0) goto loc_009419CF;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 84)))) < 72) goto loc_009419CF;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 84))) + ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 108)))));
    if (((unsigned int)(result)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 108))))) goto loc_009419CF;
    a1 = ((unsigned int)(*(unsigned int *)(a2 + 108))) + (72);
    if (a1 <= ((unsigned int)(*(unsigned int *)(a2 + 16)))) { v_rbx = 1; }
    goto loc_009419D5;
loc_00941C96:
    v_stack_pD0 = v_xmm0;
    v_stack_pE0 = v_xmm1;
    v_stack_pF0 = v_xmm0;
    v_stack_p100 = v_xmm1;
    v_stack_p110 = v_xmm0;
    goto loc_00941CF2;
loc_00941CF2:
    result = MiLogRelocationRva((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 80)))), 72, (unsigned int)(*(unsigned int *)(a2 + 16)), a1);
    if (((1) & ((unsigned __int8)((unsigned int)(v_stack_pE0)))) == 0) goto loc_00941A43;
    *(unsigned __int8 *)(v_stack_p40) = 1;
    if (v_stack_pD4 > 2) goto loc_00941D42;
    if (v_stack_pD4 != 2) goto loc_00941A43;
    if (v_stack_pD6 < 5) goto loc_00941A43;
loc_00941D42:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m144) + 56) + 51)) | (2));
    *(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m144) + 56) + 51) = (unsigned __int8)(a1);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_pE0)))) & (0x20002ULL));
    if (((unsigned int)(result)) == 2) goto loc_00941A43;
    if (((unsigned int)(result)) >= 2) goto loc_00941A43;
    a1 = (unsigned __int8)((a1) | (1));
    *(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m144) + 56) + 51) = (unsigned __int8)(a1);
    if (condition_is_above_or_equal) goto loc_00941A43;
    a1 = (unsigned __int8)((a1) | (32));
    *(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m144) + 56) + 51) = (unsigned __int8)(a1);
    goto loc_00941A43;
loc_00941D88:
    result = 0;
    goto loc_00941BE5;
loc_00941D8F:
    goto loc_00941B8D;
loc_00941D9C:
    goto loc_00941B96;
loc_00941DA9:
    goto loc_00941B9F;
loc_00941DB6:
    goto loc_00941BA8;
loc_00941DC3:
    goto loc_00941BB1;
}
```

## 5. (Beta) C Style

```c
int64_t MiParseComAndCetHeaders(void *Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint32_t v_stack_m140;
    uint32_t v_stack_m144;
    uint32_t v_stack_m148;
    uint64_t v_stack_m48;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mF8;
    uint32_t v_stack_mFC;
    uint64_t v_stack_p100;
    uint64_t v_stack_p110;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_pD0;
    uint16_t v_stack_pD4;
    uint16_t v_stack_pD6;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pF0;

    local_rsp = (local_rsp) - (304);
    result = (*(uint64_t *)(v_rip + 0x4C8DB2)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m130 = Arg1;
    Arg2 = 0;
    result = memset(v_stack_mE8, Arg2, Arg2 + 80, a4);
    local_rbx = 0;
    *(uint8_t *)(arg3) = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x50))) != 0) goto loc_00941C5C;
loc_009419CF:
loc_009419D5:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x68))) != 0) goto loc_00941C1A;
loc_009419E1:
loc_009419E7:
    if (0 == 0) goto loc_00941D88;
    result = MiMapImageInSystemSpace(Arg1, 3, v_stack_mE8, a4);
    v_stack_m144 = (uint32_t)(result);
    if (sign_flag) goto loc_00941C52;
    result = MiReferenceControlAreaFile(Arg1, 3, v_stack_mE8, a4);
    v_stack_m128 = result;
    v_stack_m138 = result;
    local_rbx = (uint32_t)((local_rbx) | (12));
    v_stack_m148 = (uint32_t)(local_rbx);
    v_stack_m120 = v_stack_mE8;
    if (((1) & ((uint8_t)(local_rbx))) != 0) goto loc_00941C96;
loc_00941A43:
    if (((2) & ((uint8_t)(local_rbx))) == 0) goto loc_00941C52;
    local_rsi = ((uint32_t)(*(uint32_t *)(arg2 + 0x68))) + (v_stack_m120);
    Arg3 = 0;
loc_00941A58:
    v_stack_m140 = 0;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg2 + 0x6C))) - (v_stack_mE8);
    Arg1 = (Arg1) >> (1);
    Arg1 = (Arg1) + (v_stack_mE8);
    Arg1 = (Arg1) >> (4);
    if (0 >= Arg1) goto loc_00941C52;
    Arg1 = (uint32_t)((Arg1) * (0));
    Arg1 = (uint32_t)((Arg1) + (*(uint32_t *)(arg2 + 0x68)));
    result = MiLogRelocationRva(Arg1, 28, v_stack_m128, Arg1);
    v_stack_m110 = v_xmm0;
    v_stack_m100 = v_xmm1;
    v_stack_mF8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x18)));
    goto loc_00941AE1;
loc_00941AE1:
    result = (v_stack_m108) >> (32);
    if (((uint32_t)(result)) != 20) goto loc_00941C09;
    Arg1 = (v_stack_m100) >> (32);
    if ((uint32_t)(Arg1) == 0) goto loc_00941C52;
    if ((((uint8_t)(Arg1)) & (3)) != 0) goto loc_00941C52;
    if ((uint32_t)((uint32_t)(v_stack_m100)) == 0) goto loc_00941C52;
    if ((((uint8_t)((uint32_t)(v_stack_m100))) & (3)) != 0) goto loc_00941C52;
    if (((uint32_t)((uint32_t)(v_stack_m100))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10))))) goto loc_00941C52;
    if (((uint32_t)(Arg1)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10))))) goto loc_00941C52;
    result = (uint32_t)(((uint32_t)(v_stack_m100)) + ((uint32_t)(Arg1)));
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10))))) goto loc_00941C52;
    result = MiLogRelocationRva(Arg1, 4, v_stack_m128, Arg1);
    Arg1 = ((uint32_t)(v_stack_mFC)) + (v_stack_m120);
    v_stack_m118 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    goto loc_00941B77;
loc_00941B77:
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1))))) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(arg1) + 0x38);
    }
    if (((2) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1))))) != 0) goto loc_00941D8F;
loc_00941B8D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (4)) != 0) goto loc_00941D9C;
loc_00941B96:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (8)) != 0) goto loc_00941DA9;
loc_00941B9F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (16)) != 0) goto loc_00941DB6;
loc_00941BA8:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (32)) != 0) goto loc_00941DC3;
loc_00941BB1:
    if (sign_flag) {
        result = *(uint64_t *)(*(uint64_t *)(arg1) + 0x38);
    }
loc_00941BC1:
    if ((((uint8_t)(local_rbx)) & (4)) != 0) {
        Arg1 = v_stack_mE8;
        result = MiUnmapImageInSystemSpace(Arg1, 4, v_stack_m128, Arg1);
    }
    if (((uint32_t)(local_rbx)) >= 8) {
        Arg2 = v_stack_m128;
        Arg1 = Arg1;
        result = MiDereferenceControlAreaFile(Arg1, Arg2, v_stack_m128, Arg1);
    }
loc_00941BE5:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m128, Arg1);
    local_rsp = (local_rsp) + (304);
    return result;
loc_00941C09:
    local_rsi = (v_stack_m128) + (28);
    Arg3 = (uint32_t)(((uint32_t)(v_stack_p28)) + (1));
    goto loc_00941A58;
loc_00941C1A:
    if ((((uint8_t)(result)) & (3)) != 0) goto loc_009419E1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x6C)))) < 28) goto loc_009419E1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x6C)) + result * 1)) <= ((uint32_t)(result))) goto loc_009419E1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x6C)) + result * 1)) > (*(uint32_t *)(arg2 + 0x10))) goto loc_009419E1;
    local_rbx = (uint32_t)((local_rbx) | (2));
    goto loc_009419E7;
loc_00941C52:
    goto loc_00941BBD;
loc_00941C5C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x6C)))) & (3)) != 0) goto loc_009419CF;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x54)))) < 72) goto loc_009419CF;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x54))) + ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x6C)))));
    if (((uint32_t)(result)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x6C))))) goto loc_009419CF;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg2 + 0x6C))) + (72);
    if (Arg1 <= ((uint32_t)(*(uint32_t *)(arg2 + 0x10)))) { local_rbx = 1; }
    goto loc_009419D5;
loc_00941C96:
    v_stack_pD0 = v_xmm0;
    v_stack_pE0 = v_xmm1;
    v_stack_pF0 = v_xmm0;
    v_stack_p100 = v_xmm1;
    v_stack_p110 = v_xmm0;
    goto loc_00941CF2;
loc_00941CF2:
    result = MiLogRelocationRva((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x50)))), 72, (uint32_t)(*(uint32_t *)(arg2 + 0x10)), Arg1);
    if (((1) & ((uint8_t)((uint32_t)(v_stack_pE0)))) == 0) goto loc_00941A43;
    *(uint8_t *)(v_stack_p40) = 1;
    if (v_stack_pD4 > 2) goto loc_00941D42;
    if (v_stack_pD4 != 2) goto loc_00941A43;
    if (v_stack_pD6 < 5) goto loc_00941A43;
loc_00941D42:
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)((uint32_t)(v_stack_m144) + 0x38) + 0x33)) | (2));
    *(uint8_t *)(*(uint64_t *)((uint32_t)(v_stack_m144) + 0x38) + 0x33) = (uint8_t)(Arg1);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_pE0)))) & (0x20002ULL));
    if (((uint32_t)(result)) == 2) goto loc_00941A43;
    if (((uint32_t)(result)) >= 2) goto loc_00941A43;
    Arg1 = (uint8_t)((Arg1) | (1));
    *(uint8_t *)(*(uint64_t *)((uint32_t)(v_stack_m144) + 0x38) + 0x33) = (uint8_t)(Arg1);
    if (condition_is_above_or_equal) goto loc_00941A43;
    Arg1 = (uint8_t)((Arg1) | (32));
    *(uint8_t *)(*(uint64_t *)((uint32_t)(v_stack_m144) + 0x38) + 0x33) = (uint8_t)(Arg1);
    goto loc_00941A43;
loc_00941D88:
    result = 0;
    goto loc_00941BE5;
loc_00941D8F:
    goto loc_00941B8D;
loc_00941D9C:
    goto loc_00941B96;
loc_00941DA9:
    goto loc_00941B9F;
loc_00941DB6:
    goto loc_00941BA8;
loc_00941DC3:
    goto loc_00941BB1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x50` | `32` | `R` |
| `Arg2` | `+ 0x54` | `32` | `R` |
| `Arg2` | `+ 0x68` | `32` | `R` |
| `Arg2` | `+ 0x6C` | `32` | `R` |
| `Arg3` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00941974&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
