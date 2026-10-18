# LdrpResSearchResourceMappedFile

- RVA: `0x00454C98`–`0x0045532C` (길이 `1,684` bytes)
- VA: `0x0000000140454C98`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A7A2C`
- 디코드: `375`개 명령, `1,684/1,684` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00454D59` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00454DCA` → [wcsicmp](../50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00454E85` → [LdrResFallbackLangList](../../page/A2/LdrResFallbackLangList_function_00A21F1C.md) (function, `0x00A21F1C`)
- `0x00454ED6` → [LdrpResGetResourceDirectory](../../page/9F/LdrpResGetResourceDirectory_function_009F3004.md) (function, `0x009F3004`)
- `0x0045503F` → [LdrpResSearchResourceInsideDirectory](../../page/9F/LdrpResSearchResourceInsideDirectory_function_009F22F0.md) (function, `0x009F22F0`)
- `0x00455079` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00455197` → [LdrLoadAlternateResourceModuleEx](LdrLoadAlternateResourceModuleEx_function_004557CC.md) (function, `0x004557CC`)
- `0x004551E0` → [LdrpResGetResourceDirectory](../../page/9F/LdrpResGetResourceDirectory_function_009F3004.md) (function, `0x009F3004`)
- `0x0045522B` → [LdrResGetRCConfig](../../page/A8/LdrResGetRCConfig_function_00A8035C.md) (function, `0x00A8035C`)
- `0x00455244` → [LdrIsResItemExist](LdrIsResItemExist_function_004554DC.md) (function, `0x004554DC`)
- `0x004552BB` → [LdrpResGetMappingSize](../../page/99/LdrpResGetMappingSize_function_00991614.md) (function, `0x00991614`)

### Direct callers
- [LdrResSearchResource](../../page/98/LdrResSearchResource_function_0098F7A0.md) at `0x0098F98F`
- [sub_00B2B9CE](../../page/B2/Unknown_function_00B2B9CE.md) at `0x00B2BA4E`
- [sub_00B42D56](../../page/B4/Unknown_function_00B42D56.md) at `0x00B42D91`

### Static image references
- `0x00454CAD` → RVA `0x00E0A740` (`.data`; read)
- `0x00454DC3` → RVA `0x006CC5E0` (` ?? ::FNODOBFM::`string'`; read)
- `0x0045515E` → RVA `0x00F8C5FA` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00454E85` → [LdrResFallbackLangList](../../page/A2/LdrResFallbackLangList_function_00A21F1C.md) (`.text` → `PAGE`)
  - `0x00454ED6` → [LdrpResGetResourceDirectory](../../page/9F/LdrpResGetResourceDirectory_function_009F3004.md) (`.text` → `PAGE`)
  - `0x0045503F` → [LdrpResSearchResourceInsideDirectory](../../page/9F/LdrpResSearchResourceInsideDirectory_function_009F22F0.md) (`.text` → `PAGE`)
  - `0x004551E0` → [LdrpResGetResourceDirectory](../../page/9F/LdrpResGetResourceDirectory_function_009F3004.md) (`.text` → `PAGE`)
  - `0x0045522B` → [LdrResGetRCConfig](../../page/A8/LdrResGetRCConfig_function_00A8035C.md) (`.text` → `PAGE`)
  - `0x004552BB` → [LdrpResGetMappingSize](../../page/99/LdrpResGetMappingSize_function_00991614.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x004552FF` → [sub_006F1854](../6F/Unknown_function_006F1854.md) (`tail-transfer`)
  - `0x00455308` → [sub_006F1854 + 0x8](../6F/Unknown_function_006F1854.md) (`tail-transfer`)
  - `0x00455315` → [sub_006F1854 + 0x52](../6F/Unknown_function_006F1854.md) (`tail-transfer`)
  - `0x00455327` → [sub_006F1854 + 0x90](../6F/Unknown_function_006F1854.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00454C98  4C 8B DC                        mov r11, rsp
00454C9B  53                              push rbx
00454C9C  56                              push rsi
00454C9D  57                              push rdi
00454C9E  41 54                           push r12
00454CA0  41 55                           push r13
00454CA2  41 56                           push r14
00454CA4  41 57                           push r15
00454CA6  48 81 EC D0 03 00 00            sub rsp, 0x3d0
00454CAD  48 8B 05 8C 5A 9B 00            mov rax, qword ptr [rip + 0x9b5a8c]
00454CB4  48 33 C4                        xor rax, rsp
00454CB7  48 89 84 24 C0 03 00 00         mov qword ptr [rsp + 0x3c0], rax
00454CBF  49 8B F1                        mov rsi, r9
00454CC2  4C 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], r9
00454CCA  41 8B D8                        mov ebx, r8d
00454CCD  48 89 94 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdx
00454CD5  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00454CDA  48 8B 84 24 40 04 00 00         mov rax, qword ptr [rsp + 0x440]
00454CE2  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
00454CEA  48 8B 84 24 38 04 00 00         mov rax, qword ptr [rsp + 0x438]
00454CF2  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
00454CFA  48 8B 84 24 48 04 00 00         mov rax, qword ptr [rsp + 0x448]
00454D02  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
00454D0A  48 8B 84 24 50 04 00 00         mov rax, qword ptr [rsp + 0x450]
00454D12  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
00454D1A  45 33 FF                        xor r15d, r15d
00454D1D  4D 89 BB 88 FC FF FF            mov qword ptr [r11 - 0x378], r15
00454D24  4D 89 BB C8 FC FF FF            mov qword ptr [r11 - 0x338], r15
00454D2B  4D 89 BB D0 FC FF FF            mov qword ptr [r11 - 0x330], r15
00454D32  4D 89 BB B8 FC FF FF            mov qword ptr [r11 - 0x348], r15
00454D39  4D 89 BB C0 FC FF FF            mov qword ptr [r11 - 0x340], r15
00454D40  33 C0                           xor eax, eax
00454D42  66 89 84 24 02 01 00 00         mov word ptr [rsp + 0x102], ax
00454D4A  33 D2                           xor edx, edx
00454D4C  41 B8 06 02 00 00               mov r8d, 0x206
00454D52  49 8D 8B F8 FC FF FF            lea rcx, [r11 - 0x308]
00454D59  E8 E2 1E 27 00                  call 0x1406c6c40
00454D5E  66 44 89 7C 24 70               mov word ptr [rsp + 0x70], r15w
00454D64  4C 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], r15
00454D6C  41 8A D7                        mov dl, r15b
00454D6F  8B C3                           mov eax, ebx
00454D71  83 E0 40                        and eax, 0x40
00454D74  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
00454D7B  4C 89 BC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r15
00454D83  45 8A EF                        mov r13b, r15b
00454D86  45 0F B7 E7                     movzx r12d, r15w
00454D8A  44 8B F3                        mov r14d, ebx
00454D8D  41 81 E6 80 00 00 00            and r14d, 0x80
00454D94  48 8D 7E 10                     lea rdi, [rsi + 0x10]
00454D98  8B 84 24 30 04 00 00            mov eax, dword ptr [rsp + 0x430]
00454D9F  83 F8 03                        cmp eax, 3
00454DA2  0F 85 96 03 00 00               jne 0x14045513e
00454DA8  44 0F B7 27                     movzx r12d, word ptr [rdi]
00454DAC  48 8B 0E                        mov rcx, qword ptr [rsi]
00454DAF  48 F7 C1 00 00 FF FF            test rcx, -0x10000
00454DB6  75 0B                           jne 0x140454dc3
00454DB8  41 8A D7                        mov dl, r15b
00454DBB  41 BF 01 00 00 00               mov r15d, 1
00454DC1  EB 17                           jmp 0x140454dda
00454DC3  48 8D 15 16 78 27 00            lea rdx, [rip + 0x277816]
00454DCA  E8 B1 B2 0A 00                  call 0x140500080
00454DCF  85 C0                           test eax, eax
00454DD1  75 E5                           jne 0x140454db8
00454DD3  44 8D 78 01                     lea r15d, [rax + 1]
00454DD7  41 8A D7                        mov dl, r15b
00454DDA  88 94 24 80 00 00 00            mov byte ptr [rsp + 0x80], dl
00454DE1  8B 84 24 30 04 00 00            mov eax, dword ptr [rsp + 0x430]
00454DE8  EB 07                           jmp 0x140454df1
00454DEA  8B F8                           mov edi, eax
00454DEC  E9 7B 02 00 00                  jmp 0x14045506c
00454DF1  41 8B F6                        mov esi, r14d
00454DF4  F6 C3 10                        test bl, 0x10
00454DF7  0F 84 C1 02 00 00               je 0x1404550be
00454DFD  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00454E02  45 33 C9                        xor r9d, r9d
00454E05  8B C6                           mov eax, esi
00454E07  B9 00 00 06 00                  mov ecx, 0x60000
00454E0C  23 C1                           and eax, ecx
00454E0E  3B C1                           cmp eax, ecx
00454E10  75 0A                           jne 0x140454e1c
00454E12  BF 8A 00 00 C0                  mov edi, 0xc000008a
00454E17  E9 50 02 00 00                  jmp 0x14045506c
00454E1C  41 0F B6 D1                     movzx edx, r9b
00454E20  44 8B C6                        mov r8d, esi
00454E23  41 F7 D0                        not r8d
00454E26  8B C3                           mov eax, ebx
00454E28  F7 D0                           not eax
00454E2A  A8 10                           test al, 0x10
00454E2C  0F 95 C1                        setne cl
00454E2F  41 0F BA E0 13                  bt r8d, 0x13
00454E34  0F 92 C0                        setb al
00454E37  84 C8                           test al, cl
00454E39  0F 85 F1 02 00 00               jne 0x140455130
00454E3F  66 44 89 BC 24 00 01 00 00      mov word ptr [rsp + 0x100], r15w
00454E48  66 44 89 8C 24 04 01 00 00      mov word ptr [rsp + 0x104], r9w
00454E51  84 D2                           test dl, dl
00454E53  75 0A                           jne 0x140454e5f
00454E55  83 BC 24 30 04 00 00 03         cmp dword ptr [rsp + 0x430], 3
00454E5D  75 36                           jne 0x140454e95
00454E5F  F6 C3 10                        test bl, 0x10
00454E62  74 05                           je 0x140454e69
00454E64  F6 C3 20                        test bl, 0x20
00454E67  75 2C                           jne 0x140454e95
00454E69  F6 C3 04                        test bl, 4
00454E6C  74 03                           je 0x140454e71
00454E6E  83 CE 04                        or esi, 4
00454E71  48 8D 84 24 00 01 00 00         lea rax, [rsp + 0x100]
00454E79  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00454E7E  44 8B CE                        mov r9d, esi
00454E81  45 0F B7 C4                     movzx r8d, r12w
00454E85  E8 92 D0 5C 00                  call 0x140a21f1c
00454E8A  45 33 C9                        xor r9d, r9d
00454E8D  85 C0                           test eax, eax
00454E8F  0F 88 BE 03 00 00               js 0x140455253
00454E95  8B C6                           mov eax, esi
00454E97  F7 D0                           not eax
00454E99  0F BA E0 12                     bt eax, 0x12
00454E9D  0F 93 C1                        setae cl
00454EA0  F6 C3 10                        test bl, 0x10
00454EA3  0F 94 C0                        sete al
00454EA6  22 C8                           and cl, al
00454EA8  0F BA E6 13                     bt esi, 0x13
00454EAC  0F 93 C0                        setae al
00454EAF  84 C8                           test al, cl
00454EB1  75 33                           jne 0x140454ee6
00454EB3  48 8D 84 24 C0 00 00 00         lea rax, [rsp + 0xc0]
00454EBB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00454EC0  4C 8D 8C 24 D0 00 00 00         lea r9, [rsp + 0xd0]
00454EC8  44 8B C3                        mov r8d, ebx
00454ECB  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
00454ED3  48 8B CF                        mov rcx, rdi
00454ED6  E8 29 E1 59 00                  call 0x1409f3004
00454EDB  45 33 C9                        xor r9d, r9d
00454EDE  85 C0                           test eax, eax
00454EE0  0F 88 88 01 00 00               js 0x14045506e
00454EE6  41 8B F9                        mov edi, r9d
00454EE9  45 8B E1                        mov r12d, r9d
00454EEC  0F B7 84 24 00 01 00 00         movzx eax, word ptr [rsp + 0x100]
00454EF4  44 3B E0                        cmp r12d, eax
00454EF7  0F 83 6F 01 00 00               jae 0x14045506c
00454EFD  4C 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], r9
00454F05  4C 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], r9
00454F0D  41 8B CC                        mov ecx, r12d
00454F10  0F B7 84 CC 04 01 00 00         movzx eax, word ptr [rsp + rcx*8 + 0x104]
00454F18  66 89 44 24 70                  mov word ptr [rsp + 0x70], ax
00454F1D  8B 8C CC 08 01 00 00            mov ecx, dword ptr [rsp + rcx*8 + 0x108]
00454F24  89 4C 24 74                     mov dword ptr [rsp + 0x74], ecx
00454F28  45 8B F1                        mov r14d, r9d
00454F2B  41 83 FE 02                     cmp r14d, 2
00454F2F  0F 83 CE 02 00 00               jae 0x140455203
00454F35  41 8B C6                        mov eax, r14d
00454F38  45 85 F6                        test r14d, r14d
00454F3B  0F 84 51 01 00 00               je 0x140455092
00454F41  83 F8 01                        cmp eax, 1
00454F44  75 03                           jne 0x140454f49
00454F46  45 8A E9                        mov r13b, r9b
00454F49  45 84 ED                        test r13b, r13b
00454F4C  0F 85 21 02 00 00               jne 0x140455173
00454F52  8B C3                           mov eax, ebx
00454F54  F7 D0                           not eax
00454F56  8B BC 24 30 04 00 00            mov edi, dword ptr [rsp + 0x430]
00454F5D  A8 02                           test al, 2
00454F5F  74 16                           je 0x140454f77
00454F61  83 FF 02                        cmp edi, 2
00454F64  7E 11                           jle 0x140454f77
00454F66  0F B7 44 24 70                  movzx eax, word ptr [rsp + 0x70]
00454F6B  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00454F73  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
00454F77  4C 89 8C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r9
00454F7F  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00454F84  45 84 ED                        test r13b, r13b
00454F87  4D 0F 45 D9                     cmovne r11, r9
00454F8B  44 8B D3                        mov r10d, ebx
00454F8E  0F 85 B5 01 00 00               jne 0x140455149
00454F94  F6 C3 20                        test bl, 0x20
00454F97  75 04                           jne 0x140454f9d
00454F99  41 83 CA 04                     or r10d, 4
00454F9D  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
00454FA5  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
00454FAD  48 85 C9                        test rcx, rcx
00454FB0  48 0F 45 C1                     cmovne rax, rcx
00454FB4  48 8B 94 24 C0 00 00 00         mov rdx, qword ptr [rsp + 0xc0]
00454FBC  45 84 ED                        test r13b, r13b
00454FBF  48 0F 45 94 24 C8 00 00 00      cmovne rdx, qword ptr [rsp + 0xc8]
00454FC8  4C 8B 8C 24 D0 00 00 00         mov r9, qword ptr [rsp + 0xd0]
00454FD0  4C 0F 45 8C 24 D8 00 00 00      cmovne r9, qword ptr [rsp + 0xd8]
00454FD9  4C 8B 84 24 A8 00 00 00         mov r8, qword ptr [rsp + 0xa8]
00454FE1  4C 0F 45 84 24 88 00 00 00      cmovne r8, qword ptr [rsp + 0x88]
00454FEA  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00454FEF  48 0F 45 8C 24 90 00 00 00      cmovne rcx, qword ptr [rsp + 0x90]
00454FF8  4C 89 5C 24 60                  mov qword ptr [rsp + 0x60], r11
00454FFD  44 89 54 24 58                  mov dword ptr [rsp + 0x58], r10d
00455002  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00455007  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
0045500F  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00455014  48 8D 84 24 00 01 00 00         lea rax, [rsp + 0x100]
0045501C  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00455021  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
00455025  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
0045502D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00455032  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00455038  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
0045503D  33 D2                           xor edx, edx
0045503F  E8 AC D2 59 00                  call 0x1409f22f0
00455044  8B F8                           mov edi, eax
00455046  45 33 C9                        xor r9d, r9d
00455049  44 39 8C 24 A0 00 00 00         cmp dword ptr [rsp + 0xa0], r9d
00455051  0F 85 7B 02 00 00               jne 0x1404552d2
00455057  85 FF                           test edi, edi
00455059  78 57                           js 0x1404550b2
0045505B  4C 8B B4 24 E8 00 00 00         mov r14, qword ptr [rsp + 0xe8]
00455063  4D 85 F6                        test r14, r14
00455066  0F 85 A1 02 00 00               jne 0x14045530d
0045506C  8B C7                           mov eax, edi
0045506E  48 8B 8C 24 C0 03 00 00         mov rcx, qword ptr [rsp + 0x3c0]
00455076  48 33 CC                        xor rcx, rsp
00455079  E8 C2 75 25 00                  call 0x1406ac640
0045507E  48 81 C4 D0 03 00 00            add rsp, 0x3d0
00455085  41 5F                           pop r15
00455087  41 5E                           pop r14
00455089  41 5D                           pop r13
0045508B  41 5C                           pop r12
0045508D  5F                              pop rdi
0045508E  5E                              pop rsi
0045508F  5B                              pop rbx
00455090  C3                              ret
00455091  CC                              int3
00455092  83 F9 09                        cmp ecx, 9
00455095  0F 84 5C 01 00 00               je 0x1404551f7
0045509B  F7 C6 00 00 0A 00               test esi, 0xa0000
004550A1  0F 94 C1                        sete cl
004550A4  F6 C3 10                        test bl, 0x10
004550A7  0F 94 C0                        sete al
004550AA  84 C8                           test al, cl
004550AC  0F 85 A0 00 00 00               jne 0x140455152
004550B2  8B 4C 24 74                     mov ecx, dword ptr [rsp + 0x74]
004550B6  45 03 F7                        add r14d, r15d
004550B9  E9 6D FE FF FF                  jmp 0x140454f2b
004550BE  41 8B F6                        mov esi, r14d
004550C1  41 3B C7                        cmp eax, r15d
004550C4  0F 8C 33 FD FF FF               jl 0x140454dfd
004550CA  83 F8 03                        cmp eax, 3
004550CD  0F 8F 2A FD FF FF               jg 0x140454dfd
004550D3  0F 85 C1 01 00 00               jne 0x14045529a
004550D9  0F B7 0F                        movzx ecx, word ptr [rdi]
004550DC  0F BA E3 18                     bt ebx, 0x18
004550E0  72 43                           jb 0x140455125
004550E2  48 8B B4 24 98 00 00 00         mov rsi, qword ptr [rsp + 0x98]
004550EA  48 8B 06                        mov rax, qword ptr [rsi]
004550ED  48 83 E8 10                     sub rax, 0x10
004550F1  48 A9 F7 FF FF FF               test rax, -9
004550F7  0F 85 0E 01 00 00               jne 0x14045520b
004550FD  8B C3                           mov eax, ebx
004550FF  F7 D0                           not eax
00455101  A8 08                           test al, 8
00455103  0F 84 0A 01 00 00               je 0x140455213
00455109  B8 FF F3 00 00                  mov eax, 0xf3ff
0045510E  66 85 C8                        test ax, cx
00455111  0F 85 FC 00 00 00               jne 0x140455213
00455117  B8 00 0C 00 00                  mov eax, 0xc00
0045511C  66 3B C8                        cmp cx, ax
0045511F  0F 84 EE 00 00 00               je 0x140455213
00455125  83 CB 10                        or ebx, 0x10
00455128  41 8B F6                        mov esi, r14d
0045512B  E9 CD FC FF FF                  jmp 0x140454dfd
00455130  41 0F BA E0 11                  bt r8d, 0x11
00455135  41 0F 42 D7                     cmovb edx, r15d
00455139  E9 01 FD FF FF                  jmp 0x140454e3f
0045513E  41 BF 01 00 00 00               mov r15d, 1
00455144  E9 A8 FC FF FF                  jmp 0x140454df1
00455149  41 83 CA 20                     or r10d, 0x20
0045514D  E9 4B FE FF FF                  jmp 0x140454f9d
00455152  66 44 39 4C 24 70               cmp word ptr [rsp + 0x70], r9w
00455158  0F 84 54 FF FF FF               je 0x1404550b2
0045515E  80 3D 95 74 B3 00 00            cmp byte ptr [rip + 0xb37495], 0
00455165  0F 84 47 FF FF FF               je 0x1404550b2
0045516B  45 8A EF                        mov r13b, r15b
0045516E  E9 D6 FD FF FF                  jmp 0x140454f49
00455173  8B C6                           mov eax, esi
00455175  0F BA E8 0C                     bts eax, 0xc
00455179  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0045517D  4C 8D 8C 24 88 00 00 00         lea r9, [rsp + 0x88]
00455185  4C 8D 84 24 90 00 00 00         lea r8, [rsp + 0x90]
0045518D  0F B7 54 24 70                  movzx edx, word ptr [rsp + 0x70]
00455192  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00455197  E8 30 06 00 00                  call 0x1404557cc
0045519C  8B F8                           mov edi, eax
0045519E  45 33 C9                        xor r9d, r9d
004551A1  85 C0                           test eax, eax
004551A3  0F 88 B9 00 00 00               js 0x140455262
004551A9  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
004551B1  48 85 D2                        test rdx, rdx
004551B4  0F 84 EB 00 00 00               je 0x1404552a5
004551BA  0F BA E3 0C                     bt ebx, 0xc
004551BE  72 3F                           jb 0x1404551ff
004551C0  48 8D 84 24 C8 00 00 00         lea rax, [rsp + 0xc8]
004551C8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004551CD  4C 8D 8C 24 D8 00 00 00         lea r9, [rsp + 0xd8]
004551D5  44 8B C3                        mov r8d, ebx
004551D8  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
004551E0  E8 1F DE 59 00                  call 0x1409f3004
004551E5  8B F8                           mov edi, eax
004551E7  45 33 C9                        xor r9d, r9d
004551EA  85 C0                           test eax, eax
004551EC  0F 89 60 FD FF FF               jns 0x140454f52
004551F2  E9 BB FE FF FF                  jmp 0x1404550b2
004551F7  83 CB 20                        or ebx, 0x20
004551FA  E9 B7 FE FF FF                  jmp 0x1404550b6
004551FF  85 FF                           test edi, edi
00455201  79 BD                           jns 0x1404551c0
00455203  45 03 E7                        add r12d, r15d
00455206  E9 E1 FC FF FF                  jmp 0x140454eec
0045520B  84 D2                           test dl, dl
0045520D  0F 85 EA FE FF FF               jne 0x1404550fd
00455213  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
00455218  44 8B CB                        mov r9d, ebx
0045521B  45 33 C0                        xor r8d, r8d
0045521E  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
00455226  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0045522B  E8 2C B1 62 00                  call 0x140a8035c
00455230  8B F8                           mov edi, eax
00455232  45 33 C9                        xor r9d, r9d
00455235  85 C0                           test eax, eax
00455237  78 45                           js 0x14045527e
00455239  48 8B D6                        mov rdx, rsi
0045523C  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00455241  48 8B CF                        mov rcx, rdi
00455244  E8 93 02 00 00                  call 0x1404554dc
00455249  8B F0                           mov esi, eax
0045524B  41 0B F6                        or esi, r14d
0045524E  E9 AF FB FF FF                  jmp 0x140454e02
00455253  0F BA E3 0C                     bt ebx, 0xc
00455257  0F 83 38 FC FF FF               jae 0x140454e95
0045525D  E9 0C FE FF FF                  jmp 0x14045506e
00455262  3D 34 00 00 C0                  cmp eax, 0xc0000034
00455267  74 0B                           je 0x140455274
00455269  3D 3A 00 00 C0                  cmp eax, 0xc000003a
0045526E  0F 85 3E FE FF FF               jne 0x1404550b2
00455274  BF 01 00 0B C0                  mov edi, 0xc00b0001
00455279  E9 34 FE FF FF                  jmp 0x1404550b2
0045527E  3D 8A 00 00 C0                  cmp eax, 0xc000008a
00455283  0F 85 E3 FD FF FF               jne 0x14045506c
00455289  41 8B F6                        mov esi, r14d
0045528C  0F BA EE 13                     bts esi, 0x13
00455290  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00455295  E9 6B FB FF FF                  jmp 0x140454e05
0045529A  45 33 C0                        xor r8d, r8d
0045529D  41 8B C8                        mov ecx, r8d
004552A0  E9 37 FE FF FF                  jmp 0x1404550dc
004552A5  41 B8 00 02 00 00               mov r8d, 0x200
004552AB  48 8D 94 24 88 00 00 00         lea rdx, [rsp + 0x88]
004552B3  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
004552BB  E8 54 C3 53 00                  call 0x140991614
004552C0  8B F8                           mov edi, eax
004552C2  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
004552CA  45 33 C9                        xor r9d, r9d
004552CD  E9 E8 FE FF FF                  jmp 0x1404551ba
004552D2  85 C0                           test eax, eax
004552D4  0F 88 7D FD FF FF               js 0x140455057
004552DA  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
004552E2  48 85 C9                        test rcx, rcx
004552E5  0F 84 6C FD FF FF               je 0x140455057
004552EB  45 84 ED                        test r13b, r13b
004552EE  0F 84 63 FD FF FF               je 0x140455057
004552F4  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
004552FC  48 85 C0                        test rax, rax
004552FF  0F 84 4F C5 29 00               je 0x1406f1854
00455305  4C 8B 00                        mov r8, qword ptr [rax]
00455308  E9 4F C5 29 00                  jmp 0x1406f185c
0045530D  0F B7 4C 24 70                  movzx ecx, word ptr [rsp + 0x70]
00455312  66 85 C9                        test cx, cx
00455315  0F 85 8B C5 29 00               jne 0x1406f18a6
0045531B  66 44 89 8C 24 10 03 00 00      mov word ptr [rsp + 0x310], r9w
00455324  41 8B F1                        mov esi, r9d
00455327  E9 B8 C5 29 00                  jmp 0x1406f18e4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LdrpResSearchResourceMappedFile(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int16 v_stack_m304;
    unsigned __int16 v_stack_m306;
    unsigned __int16 v_stack_m308;
    unsigned __int64 v_stack_m318;
    unsigned __int64 v_stack_m320;
    unsigned __int64 v_stack_m328;
    unsigned __int64 v_stack_m330;
    unsigned __int64 v_stack_m338;
    unsigned __int64 v_stack_m340;
    unsigned __int64 v_stack_m348;
    unsigned __int64 v_stack_m350;
    unsigned __int64 v_stack_m358;
    unsigned __int64 v_stack_m360;
    unsigned int v_stack_m368;
    unsigned __int64 v_stack_m370;
    unsigned __int64 v_stack_m378;
    unsigned __int64 v_stack_m380;
    unsigned __int8 v_stack_m388;
    unsigned __int64 v_stack_m390;
    unsigned int v_stack_m394;
    unsigned __int16 v_stack_m398;
    unsigned __int64 v_stack_m3A8;
    unsigned int v_stack_m3B0;
    unsigned __int64 v_stack_m3B8;
    unsigned __int64 v_stack_m3C0;
    unsigned __int64 v_stack_m3C8;
    unsigned int v_stack_m3D0;
    unsigned __int64 v_stack_m3D8;
    unsigned __int64 v_stack_m3E0;
    unsigned __int64 v_stack_m3E8;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_p20;
    unsigned __int16 v_stack_p310;
    unsigned __int16 v_stack_p70;
    unsigned int v_stack_p74;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;

    v_rsp = (v_rsp) - (976);
    result = (*(unsigned __int64 *)(v_rip + 10181260)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m370 = a4;
    v_stack_m360 = a2;
    v_stack_m390 = a1;
    v_stack_m328 = a7;
    v_stack_m350 = a6;
    v_stack_m318 = a8;
    v_stack_m320 = a9;
    v_r15 = 0;
    *(unsigned __int64 *)(v_rsp - 888) = 0;
    *(unsigned __int64 *)(v_rsp - 824) = 0;
    *(unsigned __int64 *)(v_rsp - 816) = 0;
    *(unsigned __int64 *)(v_rsp - 840) = 0;
    *(unsigned __int64 *)(v_rsp - 832) = 0;
    result = 0;
    v_stack_m306 = 0;
    a2 = 0;
    result = memset(v_rsp - 776, a2, 518, a4);
    v_stack_m398 = 0;
    v_stack_m380 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (64));
    v_stack_m368 = (unsigned int)(result);
    v_stack_m358 = 0;
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (128));
    if (((unsigned int)((unsigned int)(a5))) != 3) goto loc_0045513E;
    if (((*(unsigned __int64 *)(a4)) & (0xFFFFFFFFFFFF0000ULL)) != 0) goto loc_00454DC3;
loc_00454DB8:
    goto loc_00454DDA;
loc_00454DC3:
    result = wcsicmp(*(unsigned __int64 *)(a4), v_rip + 2586646, 518, a4);
    if ((unsigned int)(result) != 0) goto loc_00454DB8;
loc_00454DDA:
    v_stack_m388 = (unsigned __int8)((unsigned __int8)(result + 1));
    goto loc_00454DF1;
loc_00454DF1:
    if ((((unsigned __int8)((unsigned int)(a3))) & (16)) == 0) goto loc_004550BE;
loc_00454DFD:
loc_00454E02:
    a4 = 0;
loc_00454E05:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r14))))) & ((unsigned int)((unsigned int)(0x60000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x60000ULL)))) goto loc_00454E1C;
    goto loc_0045506C;
loc_00454E1C:
    a3 = (unsigned int)(~((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r14))))));
    result = (unsigned int)(~((unsigned int)((unsigned int)((unsigned int)(a3)))));
    a1 = ((((unsigned __int8)(result)) & (16)) != 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_00455130;
loc_00454E3F:
    v_stack_m308 = (unsigned __int16)(result + 1);
    v_stack_m304 = 0;
    if (0 != 0) goto loc_00454E5F;
    if (a5 != 3) goto loc_00454E95;
loc_00454E5F:
    if ((((unsigned __int8)((unsigned int)(a3))) & (16)) == 0) goto loc_00454E69;
    if ((((unsigned __int8)((unsigned int)(a3))) & (32)) != 0) goto loc_00454E95;
loc_00454E69:
    v_rsi = (unsigned int)((unsigned int)(v_r14));
    if ((((unsigned __int8)((unsigned int)(a3))) & (4)) != 0) {
        v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) | (4));
    }
    v_stack_m3E8 = v_stack_m308;
    result = LdrResFallbackLangList(a1, 0, (unsigned __int16)(*(unsigned __int16 *)(a4 + 16)), (unsigned int)((unsigned int)(v_rsi)));
    a4 = 0;
    if (sign_flag) goto loc_00455253;
loc_00454E95:
    result = (unsigned int)(~((unsigned int)((unsigned int)(v_rsi))));
    a1 = (condition_is_above_or_equal) ? 1 : 0;
    result = ((((unsigned __int8)((unsigned int)(a3))) & (16)) == 0) ? 1 : 0;
    a1 = (unsigned __int8)((a1) & ((unsigned __int8)(result)));
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_00454EE6;
    v_stack_m3E8 = v_stack_m348;
    result = LdrpResGetResourceDirectory((unsigned int)(0xC000008AULL), v_stack_m360, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_m338);
    a4 = 0;
    if (sign_flag) goto loc_0045506E;
loc_00454EE6:
loc_00454EEC:
    if (0 >= ((unsigned int)(v_stack_m308))) goto loc_0045506C;
    v_stack_m378 = 0;
    v_stack_m380 = 0;
    v_stack_m398 = (unsigned __int16)(*(unsigned __int16 *)(v_rsp + 0 * 8 + 260));
    v_stack_m394 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + 0 * 8 + 264)));
loc_00454F2B:
    if (0 >= 2) goto loc_00455203;
    if (0 == 0) goto loc_00455092;
    v_r13 = 0;
    if (0 == 1) {
        v_r13 = 0;
    }
    if ((unsigned __int8)(v_r13) != 0) goto loc_00455173;
loc_00454F52:
    result = (unsigned int)(~((unsigned int)((unsigned int)((unsigned int)(a3)))));
    if ((((unsigned __int8)(result)) & (2)) == 0) goto loc_00454F77;
    if (((unsigned int)((unsigned int)(a5))) >= = 2) {
        result = v_stack_m398;
        a1 = v_stack_m370;
        *(unsigned __int64 *)(a1 + 16) = result;
    }
    v_stack_m358 = 0;
    v_r11 = v_stack_m398;
    if ((unsigned __int8)(v_r13) != 0) { v_r11 = 0; }
    if ((unsigned __int8)(v_r13) != 0) goto loc_00455149;
    v_r10 = (unsigned int)((unsigned int)((unsigned int)(a3)));
    if ((((unsigned __int8)((unsigned int)(a3))) & (32)) == 0) {
        v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) | (4));
    }
    result = v_stack_m358;
    if (v_stack_m328 != 0) { result = v_stack_m328; }
    a2 = v_stack_m348;
    if ((unsigned __int8)(v_r13) != 0) { a2 = v_stack_m340; }
    a4 = v_stack_m338;
    if ((unsigned __int8)(v_r13) != 0) { a4 = v_stack_m330; }
    a3 = v_stack_m360;
    if ((unsigned __int8)(v_r13) != 0) { a3 = v_stack_m380; }
    a1 = v_stack_m390;
    if ((unsigned __int8)(v_r13) != 0) { a1 = v_stack_m378; }
    v_stack_m3A8 = v_r11;
    v_stack_m3B0 = (unsigned int)(v_r10);
    v_stack_m3B8 = result;
    v_stack_m3C0 = v_stack_m350;
    v_stack_m3C8 = v_stack_m308;
    v_stack_m3D0 = (unsigned int)((unsigned int)(a5));
    v_stack_m3D8 = v_stack_m370;
    v_stack_m3E8 = a2;
    a2 = 0;
    result = LdrpResSearchResourceInsideDirectory(a1, a2, a3, a4);
    a4 = 0;
    if (v_stack_m368 != 0) goto loc_004552D2;
loc_00455057:
    if (sign_flag) goto loc_004550B2;
    if (v_stack_m320 != 0) goto loc_0045530D;
loc_0045506C:
loc_0045506E:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (976);
    return result;
loc_00455092:
    if (((unsigned int)(a1)) == 9) goto loc_004551F7;
    a1 = ((((unsigned int)(v_rsi)) & (0xA0000ULL)) == 0) ? 1 : 0;
    result = ((((unsigned __int8)((unsigned int)(a3))) & (16)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_00455152;
loc_004550B2:
loc_004550B6:
    v_r14 = (unsigned int)((v_stack_m320) + ((unsigned int)(result + 1)));
    goto loc_00454F2B;
loc_004550BE:
    if (((unsigned int)(result)) < ((unsigned int)(result + 1))) goto loc_00454DFD;
    if (((unsigned int)(result)) > 3) goto loc_00454DFD;
    if (((unsigned int)(result)) != 3) goto loc_0045529A;
loc_004550DC:
    if (((unsigned int)(result)) < 3) goto loc_00455125;
    result = (*(unsigned __int64 *)(v_stack_p98)) - (16);
    if (((result) & (-9)) != 0) goto loc_0045520B;
loc_004550FD:
    result = (unsigned int)(~((unsigned int)((unsigned int)((unsigned int)(a3)))));
    if ((((unsigned __int8)(result)) & (8)) == 0) goto loc_00455213;
    if ((((unsigned __int16)((unsigned int)(0xF3FFULL))) & ((unsigned __int16)(*(unsigned __int16 *)((unsigned int)((unsigned int)(result)))))) != 0) goto loc_00455213;
    if (((unsigned __int16)(*(unsigned __int16 *)((unsigned int)((unsigned int)(result))))) == ((unsigned __int16)((unsigned int)(0xC00ULL)))) goto loc_00455213;
loc_00455125:
    v_rbx = (unsigned int)(((unsigned int)(a3)) | (16));
    goto loc_00454DFD;
loc_00455130:
    if (condition_is_below) { a2 = (unsigned int)(result + 1); }
    goto loc_00454E3F;
loc_0045513E:
    goto loc_00454DF1;
loc_00455149:
    v_r10 = (unsigned int)((v_r10) | (32));
    goto loc_00454F9D;
loc_00455152:
    if (v_stack_p70 == 0) goto loc_004550B2;
    if ((*(unsigned __int8 *)(v_rip + 11760789)) == 0) goto loc_004550B2;
    goto loc_00454F49;
loc_00455173:
    v_stack_p20 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r14)))));
    result = LdrLoadAlternateResourceModuleEx(v_stack_p78, v_stack_p70, v_stack_p90, v_stack_p88);
    a4 = 0;
    if (sign_flag) goto loc_00455262;
    if (v_stack_p88 == 0) goto loc_004552A5;
loc_004551BA:
    if (condition_is_below) goto loc_004551FF;
loc_004551C0:
    v_stack_p20 = v_stack_pC8;
    result = LdrpResGetResourceDirectory(v_stack_p90, v_stack_p88, (unsigned int)((unsigned int)(v_rbx)), v_stack_pD8);
    a4 = 0;
    if (!sign_flag) goto loc_00454F52;
    goto loc_004550B2;
loc_004551F7:
    v_rbx = (unsigned int)((v_rbx) | (32));
    goto loc_004550B6;
loc_004551FF:
    if (!sign_flag) goto loc_004551C0;
loc_00455203:
    v_r12 = (unsigned int)((0) + (1));
    goto loc_00454EEC;
loc_0045520B:
    if ((unsigned __int8)(v_stack_p88) != 0) goto loc_004550FD;
loc_00455213:
    v_stack_p20 = 1;
    a3 = 0;
    result = LdrResGetRCConfig(v_stack_p78, v_stack_pA8, a3, (unsigned int)((unsigned int)(v_rbx)));
    a4 = 0;
    if (sign_flag) goto loc_0045527E;
    result = LdrIsResItemExist(v_stack_p78, (unsigned int)((unsigned int)(v_r14)), a3, a4);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(result))) | ((unsigned int)(v_r14)));
    goto loc_00454E02;
loc_00455253:
    if (condition_is_above_or_equal) goto loc_00454E95;
    goto loc_0045506E;
loc_00455262:
    if (((unsigned int)(result)) == 0xC0000034ULL) goto loc_00455274;
    if (((unsigned int)(result)) != 0xC000003AULL) goto loc_004550B2;
loc_00455274:
    goto loc_004550B2;
loc_0045527E:
    if (((unsigned int)(result)) != 0xC000008AULL) goto loc_0045506C;
    goto loc_00454E05;
loc_0045529A:
    a3 = 0;
    goto loc_004550DC;
loc_004552A5:
    result = LdrpResGetMappingSize(v_stack_p90, v_stack_p88, 512, a4);
    a4 = 0;
    goto loc_004551BA;
loc_004552D2:
    if (sign_flag) goto loc_00455057;
    if (v_stack_pB8 == 0) goto loc_00455057;
    if (1 == 0) goto loc_00455057;
loc_0045530D:
    v_stack_p310 = 0;
}
```

## 5. (Beta) C Style

```c
int64_t LdrpResSearchResourceMappedFile(int64_t Arg1, int64_t Arg2, int32_t Arg3, void *Arg4, uint32_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint16_t v_stack_m304;
    uint16_t v_stack_m306;
    uint16_t v_stack_m308;
    uint64_t v_stack_m318;
    uint64_t v_stack_m320;
    uint64_t v_stack_m328;
    uint64_t v_stack_m330;
    uint64_t v_stack_m338;
    uint64_t v_stack_m340;
    uint64_t v_stack_m348;
    uint64_t v_stack_m350;
    uint64_t v_stack_m358;
    uint64_t v_stack_m360;
    uint32_t v_stack_m368;
    uint64_t v_stack_m370;
    uint64_t v_stack_m378;
    uint64_t v_stack_m380;
    uint8_t v_stack_m388;
    uint64_t v_stack_m390;
    uint32_t v_stack_m394;
    uint16_t v_stack_m398;
    uint64_t v_stack_m3A8;
    uint32_t v_stack_m3B0;
    uint64_t v_stack_m3B8;
    uint64_t v_stack_m3C0;
    uint64_t v_stack_m3C8;
    uint32_t v_stack_m3D0;
    uint64_t v_stack_m3D8;
    uint64_t v_stack_m3E0;
    uint64_t v_stack_m3E8;
    uint64_t v_stack_m48;
    uint32_t v_stack_p20;
    uint16_t v_stack_p310;
    uint16_t v_stack_p70;
    uint32_t v_stack_p74;
    uint64_t v_stack_p78;
    uint64_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;

    local_rsp = (local_rsp) - (976);
    result = (*(uint64_t *)(v_rip + 0x9B5A8C)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m370 = Arg4;
    v_stack_m360 = Arg2;
    v_stack_m390 = Arg1;
    v_stack_m328 = Arg7;
    v_stack_m350 = Arg6;
    v_stack_m318 = Arg8;
    v_stack_m320 = Arg9;
    local_r15 = 0;
    *(uint64_t *)(local_rsp - 0x378) = 0;
    *(uint64_t *)(local_rsp - 0x338) = 0;
    *(uint64_t *)(local_rsp - 0x330) = 0;
    *(uint64_t *)(local_rsp - 0x348) = 0;
    *(uint64_t *)(local_rsp - 0x340) = 0;
    result = 0;
    v_stack_m306 = 0;
    Arg2 = 0;
    result = memset(local_rsp - 776, Arg2, 518, Arg4);
    v_stack_m398 = 0;
    v_stack_m380 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (64));
    v_stack_m368 = (uint32_t)(result);
    v_stack_m358 = 0;
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (128));
    if (((uint32_t)((uint32_t)(Arg5))) != 3) goto loc_0045513E;
    if (((*(uint64_t *)(arg4)) & (0xFFFFFFFFFFFF0000ULL)) != 0) goto loc_00454DC3;
loc_00454DB8:
    goto loc_00454DDA;
loc_00454DC3:
    result = wcsicmp(*(uint64_t *)(arg4), v_rip + 2586646, 518, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00454DB8;
loc_00454DDA:
    v_stack_m388 = (uint8_t)((uint8_t)(result + 1));
    goto loc_00454DF1;
loc_00454DF1:
    if ((((uint8_t)((uint32_t)(Arg3))) & (16)) == 0) goto loc_004550BE;
loc_00454DFD:
loc_00454E02:
    Arg4 = 0;
loc_00454E05:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r14))))) & ((uint32_t)((uint32_t)(0x60000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x60000ULL)))) goto loc_00454E1C;
    goto loc_0045506C;
loc_00454E1C:
    Arg3 = (uint32_t)(~((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r14))))));
    result = (uint32_t)(~((uint32_t)((uint32_t)((uint32_t)(Arg3)))));
    Arg1 = ((((uint8_t)(result)) & (16)) != 0) ? 1 : 0;
    result = (condition_is_below) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_00455130;
loc_00454E3F:
    v_stack_m308 = (uint16_t)(result + 1);
    v_stack_m304 = 0;
    if (0 != 0) goto loc_00454E5F;
    if (Arg5 != 3) goto loc_00454E95;
loc_00454E5F:
    if ((((uint8_t)((uint32_t)(Arg3))) & (16)) == 0) goto loc_00454E69;
    if ((((uint8_t)((uint32_t)(Arg3))) & (32)) != 0) goto loc_00454E95;
loc_00454E69:
    local_rsi = (uint32_t)((uint32_t)(local_r14));
    if ((((uint8_t)((uint32_t)(Arg3))) & (4)) != 0) {
        local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) | (4));
    }
    v_stack_m3E8 = v_stack_m308;
    result = LdrResFallbackLangList(Arg1, 0, (uint16_t)(*(uint16_t *)(arg4 + 0x10)), (uint32_t)((uint32_t)(local_rsi)));
    Arg4 = 0;
    if (sign_flag) goto loc_00455253;
loc_00454E95:
    result = (uint32_t)(~((uint32_t)((uint32_t)(local_rsi))));
    Arg1 = (condition_is_above_or_equal) ? 1 : 0;
    result = ((((uint8_t)((uint32_t)(Arg3))) & (16)) == 0) ? 1 : 0;
    Arg1 = (uint8_t)((Arg1) & ((uint8_t)(result)));
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_00454EE6;
    v_stack_m3E8 = v_stack_m348;
    result = LdrpResGetResourceDirectory((uint32_t)(0xC000008AULL), v_stack_m360, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_m338);
    Arg4 = 0;
    if (sign_flag) goto loc_0045506E;
loc_00454EE6:
loc_00454EEC:
    if (0 >= ((uint32_t)(v_stack_m308))) goto loc_0045506C;
    v_stack_m378 = 0;
    v_stack_m380 = 0;
    v_stack_m398 = (uint16_t)(*(uint16_t *)(local_rsp + 0x0 * 8 + 0x104));
    v_stack_m394 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + 0x0 * 8 + 0x108)));
loc_00454F2B:
    if (0 >= 2) goto loc_00455203;
    if (0 == 0) goto loc_00455092;
    local_r13 = 0;
    if (0 == 1) {
        local_r13 = 0;
    }
    if ((uint8_t)(local_r13) != 0) goto loc_00455173;
loc_00454F52:
    result = (uint32_t)(~((uint32_t)((uint32_t)((uint32_t)(Arg3)))));
    if ((((uint8_t)(result)) & (2)) == 0) goto loc_00454F77;
    if (((uint32_t)((uint32_t)(Arg5))) >= = 2) {
        result = v_stack_m398;
        Arg1 = v_stack_m370;
        *(uint64_t *)(Arg1 + 0x10) = result;
    }
    v_stack_m358 = 0;
    local_r11 = v_stack_m398;
    if ((uint8_t)(local_r13) != 0) { local_r11 = 0; }
    if ((uint8_t)(local_r13) != 0) goto loc_00455149;
    local_r10 = (uint32_t)((uint32_t)((uint32_t)(Arg3)));
    if ((((uint8_t)((uint32_t)(Arg3))) & (32)) == 0) {
        local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) | (4));
    }
    result = v_stack_m358;
    if (v_stack_m328 != 0) { result = v_stack_m328; }
    Arg2 = v_stack_m348;
    if ((uint8_t)(local_r13) != 0) { Arg2 = v_stack_m340; }
    Arg4 = v_stack_m338;
    if ((uint8_t)(local_r13) != 0) { Arg4 = v_stack_m330; }
    Arg3 = v_stack_m360;
    if ((uint8_t)(local_r13) != 0) { Arg3 = v_stack_m380; }
    Arg1 = v_stack_m390;
    if ((uint8_t)(local_r13) != 0) { Arg1 = v_stack_m378; }
    v_stack_m3A8 = local_r11;
    v_stack_m3B0 = (uint32_t)(local_r10);
    v_stack_m3B8 = result;
    v_stack_m3C0 = v_stack_m350;
    v_stack_m3C8 = v_stack_m308;
    v_stack_m3D0 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m3D8 = v_stack_m370;
    v_stack_m3E8 = Arg2;
    Arg2 = 0;
    result = LdrpResSearchResourceInsideDirectory(Arg1, Arg2, Arg3, Arg4);
    Arg4 = 0;
    if (v_stack_m368 != 0) goto loc_004552D2;
loc_00455057:
    if (sign_flag) goto loc_004550B2;
    if (v_stack_m320 != 0) goto loc_0045530D;
loc_0045506C:
loc_0045506E:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (976);
    return result;
loc_00455092:
    if (((uint32_t)(Arg1)) == 9) goto loc_004551F7;
    Arg1 = ((((uint32_t)(local_rsi)) & (0xA0000ULL)) == 0) ? 1 : 0;
    result = ((((uint8_t)((uint32_t)(Arg3))) & (16)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_00455152;
loc_004550B2:
loc_004550B6:
    local_r14 = (uint32_t)((v_stack_m320) + ((uint32_t)(result + 1)));
    goto loc_00454F2B;
loc_004550BE:
    if (((uint32_t)(result)) < ((uint32_t)(result + 1))) goto loc_00454DFD;
    if (((uint32_t)(result)) > 3) goto loc_00454DFD;
    if (((uint32_t)(result)) != 3) goto loc_0045529A;
loc_004550DC:
    if (((uint32_t)(result)) < 3) goto loc_00455125;
    result = (*(uint64_t *)(v_stack_p98)) - (16);
    if (((result) & (-9)) != 0) goto loc_0045520B;
loc_004550FD:
    result = (uint32_t)(~((uint32_t)((uint32_t)((uint32_t)(Arg3)))));
    if ((((uint8_t)(result)) & (8)) == 0) goto loc_00455213;
    if ((((uint16_t)((uint32_t)(0xF3FFULL))) & ((uint16_t)(*(uint16_t *)((uint32_t)((uint32_t)(result)))))) != 0) goto loc_00455213;
    if (((uint16_t)(*(uint16_t *)((uint32_t)((uint32_t)(result))))) == ((uint16_t)((uint32_t)(0xC00ULL)))) goto loc_00455213;
loc_00455125:
    local_rbx = (uint32_t)(((uint32_t)(Arg3)) | (16));
    goto loc_00454DFD;
loc_00455130:
    if (condition_is_below) { Arg2 = (uint32_t)(result + 1); }
    goto loc_00454E3F;
loc_0045513E:
    goto loc_00454DF1;
loc_00455149:
    local_r10 = (uint32_t)((local_r10) | (32));
    goto loc_00454F9D;
loc_00455152:
    if (v_stack_p70 == 0) goto loc_004550B2;
    if ((*(uint8_t *)(v_rip + 0xB37495)) == 0) goto loc_004550B2;
    goto loc_00454F49;
loc_00455173:
    v_stack_p20 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r14)))));
    result = LdrLoadAlternateResourceModuleEx(v_stack_p78, v_stack_p70, v_stack_p90, v_stack_p88);
    Arg4 = 0;
    if (sign_flag) goto loc_00455262;
    if (v_stack_p88 == 0) goto loc_004552A5;
loc_004551BA:
    if (condition_is_below) goto loc_004551FF;
loc_004551C0:
    v_stack_p20 = v_stack_pC8;
    result = LdrpResGetResourceDirectory(v_stack_p90, v_stack_p88, (uint32_t)((uint32_t)(local_rbx)), v_stack_pD8);
    Arg4 = 0;
    if (!sign_flag) goto loc_00454F52;
    goto loc_004550B2;
loc_004551F7:
    local_rbx = (uint32_t)((local_rbx) | (32));
    goto loc_004550B6;
loc_004551FF:
    if (!sign_flag) goto loc_004551C0;
loc_00455203:
    local_r12 = (uint32_t)((0) + (1));
    goto loc_00454EEC;
loc_0045520B:
    if ((uint8_t)(v_stack_p88) != 0) goto loc_004550FD;
loc_00455213:
    v_stack_p20 = 1;
    Arg3 = 0;
    result = LdrResGetRCConfig(v_stack_p78, v_stack_pA8, Arg3, (uint32_t)((uint32_t)(local_rbx)));
    Arg4 = 0;
    if (sign_flag) goto loc_0045527E;
    result = LdrIsResItemExist(v_stack_p78, (uint32_t)((uint32_t)(local_r14)), Arg3, Arg4);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(result))) | ((uint32_t)(local_r14)));
    goto loc_00454E02;
loc_00455253:
    if (condition_is_above_or_equal) goto loc_00454E95;
    goto loc_0045506E;
loc_00455262:
    if (((uint32_t)(result)) == 0xC0000034ULL) goto loc_00455274;
    if (((uint32_t)(result)) != 0xC000003AULL) goto loc_004550B2;
loc_00455274:
    goto loc_004550B2;
loc_0045527E:
    if (((uint32_t)(result)) != 0xC000008AULL) goto loc_0045506C;
    goto loc_00454E05;
loc_0045529A:
    Arg3 = 0;
    goto loc_004550DC;
loc_004552A5:
    result = LdrpResGetMappingSize(v_stack_p90, v_stack_p88, 512, Arg4);
    Arg4 = 0;
    goto loc_004551BA;
loc_004552D2:
    if (sign_flag) goto loc_00455057;
    if (v_stack_pB8 == 0) goto loc_00455057;
    if (1 == 0) goto loc_00455057;
loc_0045530D:
    v_stack_p310 = 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `16` | `R` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00454C98&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
