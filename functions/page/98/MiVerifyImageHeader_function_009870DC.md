# MiVerifyImageHeader

- RVA: `0x009870DC`–`0x00987660` (길이 `1,412` bytes)
- VA: `0x00000001409870DC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00097CFC`
- 디코드: `301`개 명령, `1,412/1,412` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00987343` → [MiLegacyImageArchitecture](../../text/49/MiLegacyImageArchitecture_function_00494454.md) (function, `0x00494454`)
- `0x00987376` → [MiComputeBadImageHeaderType](MiComputeBadImageHeaderType_function_00987668.md) (function, `0x00987668`)

### Direct callers
- [MiCreateImageFileMap](MiCreateImageFileMap_function_00986830.md) at `0x00986A21`

### Static image references
- `0x0098727C` → RVA `0x00E2D878` (`.data`; read)
- `0x009874B9` → RVA `0x00E2D7F8` (`.data`; write)
- `0x0098759D` → RVA `0x00E2D87C` (`.data`; read)
- `0x009875AD` → RVA `0x00E2D880` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00987343` → [MiLegacyImageArchitecture](../../text/49/MiLegacyImageArchitecture_function_00494454.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00987589` → [sub_00B2B440 + 0xA](../B2/Unknown_function_00B2B440.md) (`tail-transfer`)
  - `0x00987598` → [sub_00B2B440](../B2/Unknown_function_00B2B440.md) (`tail-transfer`)
  - `0x0098764B` → [sub_00B2B440 + 0x14](../B2/Unknown_function_00B2B440.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009870DC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
009870E1  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
009870E6  57                              push rdi
009870E7  48 83 EC 20                     sub rsp, 0x20
009870EB  49 8B C0                        mov rax, r8
009870EE  4C 8B D2                        mov r10, rdx
009870F1  4C 8B D9                        mov r11, rcx
009870F4  F6 C2 03                        test dl, 3
009870F7  0F 85 82 04 00 00               jne 0x14098757f
009870FD  81 3A 50 45 00 00               cmp dword ptr [rdx], 0x4550
00987103  0F 85 64 02 00 00               jne 0x14098736d
00987109  33 DB                           xor ebx, ebx
0098710B  66 39 5A 04                     cmp word ptr [rdx + 4], bx
0098710F  0F 84 79 04 00 00               je 0x14098758e
00987115  F6 42 16 02                     test byte ptr [rdx + 0x16], 2
00987119  0F 84 36 04 00 00               je 0x140987555
0098711F  0F B7 4A 18                     movzx ecx, word ptr [rdx + 0x18]
00987123  BE 0B 02 00 00                  mov esi, 0x20b
00987128  66 41 89 4B 30                  mov word ptr [r11 + 0x30], cx
0098712D  8B 42 3C                        mov eax, dword ptr [rdx + 0x3c]
00987130  41 89 43 08                     mov dword ptr [r11 + 8], eax
00987134  8B 42 38                        mov eax, dword ptr [rdx + 0x38]
00987137  41 89 43 0C                     mov dword ptr [r11 + 0xc], eax
0098713B  8B 42 50                        mov eax, dword ptr [rdx + 0x50]
0098713E  41 89 43 10                     mov dword ptr [r11 + 0x10], eax
00987142  66 3B CE                        cmp cx, si
00987145  0F 85 3B 02 00 00               jne 0x140987386
0098714B  8B 8A 80 00 00 00               mov ecx, dword ptr [rdx + 0x80]
00987151  41 89 4B 14                     mov dword ptr [r11 + 0x14], ecx
00987155  48 8B 42 30                     mov rax, qword ptr [rdx + 0x30]
00987159  49 89 03                        mov qword ptr [r11], rax
0098715C  8B 42 54                        mov eax, dword ptr [rdx + 0x54]
0098715F  41 89 43 18                     mov dword ptr [r11 + 0x18], eax
00987163  8B 42 28                        mov eax, dword ptr [rdx + 0x28]
00987166  41 89 43 1C                     mov dword ptr [r11 + 0x1c], eax
0098716A  48 8B 42 60                     mov rax, qword ptr [rdx + 0x60]
0098716E  49 89 43 20                     mov qword ptr [r11 + 0x20], rax
00987172  48 8B 42 68                     mov rax, qword ptr [rdx + 0x68]
00987176  49 89 43 28                     mov qword ptr [r11 + 0x28], rax
0098717A  0F B7 42 5C                     movzx eax, word ptr [rdx + 0x5c]
0098717E  66 41 89 43 32                  mov word ptr [r11 + 0x32], ax
00987183  0F B7 42 48                     movzx eax, word ptr [rdx + 0x48]
00987187  66 41 89 43 34                  mov word ptr [r11 + 0x34], ax
0098718C  0F B7 42 4A                     movzx eax, word ptr [rdx + 0x4a]
00987190  66 41 89 43 36                  mov word ptr [r11 + 0x36], ax
00987195  0F B7 42 40                     movzx eax, word ptr [rdx + 0x40]
00987199  66 41 89 43 38                  mov word ptr [r11 + 0x38], ax
0098719E  0F B7 42 42                     movzx eax, word ptr [rdx + 0x42]
009871A2  66 41 89 43 3A                  mov word ptr [r11 + 0x3a], ax
009871A7  0F B7 42 5E                     movzx eax, word ptr [rdx + 0x5e]
009871AB  66 41 89 43 3C                  mov word ptr [r11 + 0x3c], ax
009871B0  8B 42 58                        mov eax, dword ptr [rdx + 0x58]
009871B3  41 89 43 40                     mov dword ptr [r11 + 0x40], eax
009871B7  8B 42 1C                        mov eax, dword ptr [rdx + 0x1c]
009871BA  41 89 43 44                     mov dword ptr [r11 + 0x44], eax
009871BE  49 89 5B 68                     mov qword ptr [r11 + 0x68], rbx
009871C2  83 BA 84 00 00 00 06            cmp dword ptr [rdx + 0x84], 6
009871C9  76 18                           jbe 0x1409871e3
009871CB  8B 82 B8 00 00 00               mov eax, dword ptr [rdx + 0xb8]
009871D1  85 C0                           test eax, eax
009871D3  74 0E                           je 0x1409871e3
009871D5  41 89 43 68                     mov dword ptr [r11 + 0x68], eax
009871D9  8B 82 BC 00 00 00               mov eax, dword ptr [rdx + 0xbc]
009871DF  41 89 43 6C                     mov dword ptr [r11 + 0x6c], eax
009871E3  83 BA 84 00 00 00 0C            cmp dword ptr [rdx + 0x84], 0xc
009871EA  76 14                           jbe 0x140987200
009871EC  8B 82 E8 00 00 00               mov eax, dword ptr [rdx + 0xe8]
009871F2  41 89 43 48                     mov dword ptr [r11 + 0x48], eax
009871F6  8B 82 EC 00 00 00               mov eax, dword ptr [rdx + 0xec]
009871FC  41 89 43 4C                     mov dword ptr [r11 + 0x4c], eax
00987200  83 BA 84 00 00 00 0E            cmp dword ptr [rdx + 0x84], 0xe
00987207  41 B9 01 00 00 00               mov r9d, 1
0098720D  0F 86 6A 01 00 00               jbe 0x14098737d
00987213  8B 82 F8 00 00 00               mov eax, dword ptr [rdx + 0xf8]
00987219  41 89 43 50                     mov dword ptr [r11 + 0x50], eax
0098721D  8B 82 FC 00 00 00               mov eax, dword ptr [rdx + 0xfc]
00987223  41 89 43 54                     mov dword ptr [r11 + 0x54], eax
00987227  39 9A F8 00 00 00               cmp dword ptr [rdx + 0xf8], ebx
0098722D  0F 85 92 02 00 00               jne 0x1409874c5
00987233  83 BA 84 00 00 00 05            cmp dword ptr [rdx + 0x84], 5
0098723A  0F 86 0A 03 00 00               jbe 0x14098754a
00987240  8B 82 B0 00 00 00               mov eax, dword ptr [rdx + 0xb0]
00987246  41 89 43 58                     mov dword ptr [r11 + 0x58], eax
0098724A  8B 82 B4 00 00 00               mov eax, dword ptr [rdx + 0xb4]
00987250  41 89 43 5C                     mov dword ptr [r11 + 0x5c], eax
00987254  83 BA 84 00 00 00 0A            cmp dword ptr [rdx + 0x84], 0xa
0098725B  0F 86 90 02 00 00               jbe 0x1409874f1
00987261  8B 82 D8 00 00 00               mov eax, dword ptr [rdx + 0xd8]
00987267  41 89 43 60                     mov dword ptr [r11 + 0x60], eax
0098726B  8B 8A DC 00 00 00               mov ecx, dword ptr [rdx + 0xdc]
00987271  B8 64 00 00 00                  mov eax, 0x64
00987276  49 8B D3                        mov rdx, r11
00987279  89 0C 02                        mov dword ptr [rdx + rax], ecx
0098727C  8B 05 F6 65 4A 00               mov eax, dword ptr [rip + 0x4a65f6]
00987282  85 C0                           test eax, eax
00987284  0F 85 13 03 00 00               jne 0x14098759d
0098728A  45 0F B7 43 30                  movzx r8d, word ptr [r11 + 0x30]
0098728F  BF 0B 01 00 00                  mov edi, 0x10b
00987294  41 0F B7 C0                     movzx eax, r8w
00987298  B9 FF FE 00 00                  mov ecx, 0xfeff
0098729D  66 2B C7                        sub ax, di
009872A0  66 85 C1                        test cx, ax
009872A3  0F 85 34 02 00 00               jne 0x1409874dd
009872A9  41 8B 4B 08                     mov ecx, dword ptr [r11 + 8]
009872AD  F7 C1 FF 01 00 00               test ecx, 0x1ff
009872B3  0F 85 7B 02 00 00               jne 0x140987534
009872B9  85 C9                           test ecx, ecx
009872BB  0F 84 02 03 00 00               je 0x1409875c3
009872C1  41 8B 53 0C                     mov edx, dword ptr [r11 + 0xc]
009872C5  8D 42 FF                        lea eax, [rdx - 1]
009872C8  85 C2                           test edx, eax
009872CA  0F 85 02 03 00 00               jne 0x1409875d2
009872D0  8D 41 FF                        lea eax, [rcx - 1]
009872D3  85 C1                           test ecx, eax
009872D5  0F 85 95 02 00 00               jne 0x140987570
009872DB  3B D1                           cmp edx, ecx
009872DD  0F 82 FE 02 00 00               jb 0x1409875e1
009872E3  41 8B 4B 10                     mov ecx, dword ptr [r11 + 0x10]
009872E7  81 F9 00 00 00 77               cmp ecx, 0x77000000
009872ED  0F 87 FD 02 00 00               ja 0x1409875f0
009872F3  66 44 3B C7                     cmp r8w, di
009872F7  0F 84 9B 01 00 00               je 0x140987498
009872FD  66 44 3B C6                     cmp r8w, si
00987301  75 13                           jne 0x140987316
00987303  41 0F B7 42 04                  movzx eax, word ptr [r10 + 4]
00987308  BA 64 86 00 00                  mov edx, 0x8664
0098730D  66 3B C2                        cmp ax, dx
00987310  0F 85 E9 02 00 00               jne 0x1409875ff
00987316  41 39 4B 18                     cmp dword ptr [r11 + 0x18], ecx
0098731A  0F 83 41 02 00 00               jae 0x140987561
00987320  66 41 39 1B                     cmp word ptr [r11], bx
00987324  0F 85 F2 02 00 00               jne 0x14098761c
0098732A  41 F6 42 14 07                  test byte ptr [r10 + 0x14], 7
0098732F  0F 85 F3 01 00 00               jne 0x140987528
00987335  45 0F B7 42 16                  movzx r8d, word ptr [r10 + 0x16]
0098733A  41 0F B7 4A 04                  movzx ecx, word ptr [r10 + 4]
0098733F  66 45 23 C1                     and r8w, r9w
00987343  E8 0C D1 B0 FF                  call 0x140494454
00987348  85 C0                           test eax, eax
0098734A  0F 84 F7 02 00 00               je 0x140987647
00987350  66 45 85 C0                     test r8w, r8w
00987354  0F 85 D1 02 00 00               jne 0x14098762b
0098735A  33 C0                           xor eax, eax
0098735C  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00987361  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00987366  48 83 C4 20                     add rsp, 0x20
0098736A  5F                              pop rdi
0098736B  C3                              ret
0098736C  CC                              int3
0098736D  4D 8B C1                        mov r8, r9
00987370  48 8B D0                        mov rdx, rax
00987373  49 8B CA                        mov rcx, r10
00987376  E8 ED 02 00 00                  call 0x140987668
0098737B  EB DF                           jmp 0x14098735c
0098737D  49 89 5B 50                     mov qword ptr [r11 + 0x50], rbx
00987381  E9 AD FE FF FF                  jmp 0x140987233
00987386  8B 4A 70                        mov ecx, dword ptr [rdx + 0x70]
00987389  41 89 4B 14                     mov dword ptr [r11 + 0x14], ecx
0098738D  8B 42 34                        mov eax, dword ptr [rdx + 0x34]
00987390  49 89 03                        mov qword ptr [r11], rax
00987393  8B 42 54                        mov eax, dword ptr [rdx + 0x54]
00987396  41 89 43 18                     mov dword ptr [r11 + 0x18], eax
0098739A  8B 42 28                        mov eax, dword ptr [rdx + 0x28]
0098739D  41 89 43 1C                     mov dword ptr [r11 + 0x1c], eax
009873A1  8B 42 60                        mov eax, dword ptr [rdx + 0x60]
009873A4  49 89 43 20                     mov qword ptr [r11 + 0x20], rax
009873A8  8B 42 64                        mov eax, dword ptr [rdx + 0x64]
009873AB  49 89 43 28                     mov qword ptr [r11 + 0x28], rax
009873AF  0F B7 42 5C                     movzx eax, word ptr [rdx + 0x5c]
009873B3  66 41 89 43 32                  mov word ptr [r11 + 0x32], ax
009873B8  0F B7 42 48                     movzx eax, word ptr [rdx + 0x48]
009873BC  66 41 89 43 34                  mov word ptr [r11 + 0x34], ax
009873C1  0F B7 42 4A                     movzx eax, word ptr [rdx + 0x4a]
009873C5  66 41 89 43 36                  mov word ptr [r11 + 0x36], ax
009873CA  0F B7 42 40                     movzx eax, word ptr [rdx + 0x40]
009873CE  66 41 89 43 38                  mov word ptr [r11 + 0x38], ax
009873D3  0F B7 42 42                     movzx eax, word ptr [rdx + 0x42]
009873D7  66 41 89 43 3A                  mov word ptr [r11 + 0x3a], ax
009873DC  0F B7 42 5E                     movzx eax, word ptr [rdx + 0x5e]
009873E0  66 41 89 43 3C                  mov word ptr [r11 + 0x3c], ax
009873E5  8B 42 58                        mov eax, dword ptr [rdx + 0x58]
009873E8  41 89 43 40                     mov dword ptr [r11 + 0x40], eax
009873EC  8B 42 1C                        mov eax, dword ptr [rdx + 0x1c]
009873EF  41 89 43 44                     mov dword ptr [r11 + 0x44], eax
009873F3  49 89 5B 68                     mov qword ptr [r11 + 0x68], rbx
009873F7  83 7A 74 06                     cmp dword ptr [rdx + 0x74], 6
009873FB  76 18                           jbe 0x140987415
009873FD  8B 82 A8 00 00 00               mov eax, dword ptr [rdx + 0xa8]
00987403  85 C0                           test eax, eax
00987405  74 0E                           je 0x140987415
00987407  41 89 43 68                     mov dword ptr [r11 + 0x68], eax
0098740B  8B 82 AC 00 00 00               mov eax, dword ptr [rdx + 0xac]
00987411  41 89 43 6C                     mov dword ptr [r11 + 0x6c], eax
00987415  83 7A 74 0C                     cmp dword ptr [rdx + 0x74], 0xc
00987419  76 14                           jbe 0x14098742f
0098741B  8B 82 D8 00 00 00               mov eax, dword ptr [rdx + 0xd8]
00987421  41 89 43 48                     mov dword ptr [r11 + 0x48], eax
00987425  8B 82 DC 00 00 00               mov eax, dword ptr [rdx + 0xdc]
0098742B  41 89 43 4C                     mov dword ptr [r11 + 0x4c], eax
0098742F  83 7A 74 0E                     cmp dword ptr [rdx + 0x74], 0xe
00987433  41 B9 01 00 00 00               mov r9d, 1
00987439  0F 86 D5 00 00 00               jbe 0x140987514
0098743F  8B 82 E8 00 00 00               mov eax, dword ptr [rdx + 0xe8]
00987445  41 89 43 50                     mov dword ptr [r11 + 0x50], eax
00987449  8B 82 EC 00 00 00               mov eax, dword ptr [rdx + 0xec]
0098744F  41 89 43 54                     mov dword ptr [r11 + 0x54], eax
00987453  39 9A E8 00 00 00               cmp dword ptr [rdx + 0xe8], ebx
00987459  0F 85 9D 00 00 00               jne 0x1409874fc
0098745F  83 7A 74 05                     cmp dword ptr [rdx + 0x74], 5
00987463  0F 86 B4 00 00 00               jbe 0x14098751d
00987469  8B 82 A0 00 00 00               mov eax, dword ptr [rdx + 0xa0]
0098746F  41 89 43 58                     mov dword ptr [r11 + 0x58], eax
00987473  8B 82 A4 00 00 00               mov eax, dword ptr [rdx + 0xa4]
00987479  41 89 43 5C                     mov dword ptr [r11 + 0x5c], eax
0098747D  83 7A 74 0A                     cmp dword ptr [rdx + 0x74], 0xa
00987481  76 6E                           jbe 0x1409874f1
00987483  8B 82 C8 00 00 00               mov eax, dword ptr [rdx + 0xc8]
00987489  41 89 43 60                     mov dword ptr [r11 + 0x60], eax
0098748D  8B 8A CC 00 00 00               mov ecx, dword ptr [rdx + 0xcc]
00987493  E9 D9 FD FF FF                  jmp 0x140987271
00987498  41 0F B7 42 04                  movzx eax, word ptr [r10 + 4]
0098749D  BA 4C 01 00 00                  mov edx, 0x14c
009874A2  66 3B C2                        cmp ax, dx
009874A5  0F 84 6B FE FF FF               je 0x140987316
009874AB  BA C4 01 00 00                  mov edx, 0x1c4
009874B0  66 3B C2                        cmp ax, dx
009874B3  0F 84 5D FE FF FF               je 0x140987316
009874B9  C7 05 35 63 4A 00 52 00 00 00   mov dword ptr [rip + 0x4a6335], 0x52
009874C3  EB 22                           jmp 0x1409874e7
009874C5  39 9A FC 00 00 00               cmp dword ptr [rdx + 0xfc], ebx
009874CB  0F 84 62 FD FF FF               je 0x140987233
009874D1  41 0B C9                        or ecx, r9d
009874D4  41 89 4B 14                     mov dword ptr [r11 + 0x14], ecx
009874D8  E9 56 FD FF FF                  jmp 0x140987233
009874DD  C7 05 11 63 4A 00 49 00 00 00   mov dword ptr [rip + 0x4a6311], 0x49
009874E7  B8 7B 00 00 C0                  mov eax, 0xc000007b
009874EC  E9 6B FE FF FF                  jmp 0x14098735c
009874F1  41 89 5B 60                     mov dword ptr [r11 + 0x60], ebx
009874F5  8B CB                           mov ecx, ebx
009874F7  E9 75 FD FF FF                  jmp 0x140987271
009874FC  39 9A EC 00 00 00               cmp dword ptr [rdx + 0xec], ebx
00987502  0F 84 57 FF FF FF               je 0x14098745f
00987508  41 0B C9                        or ecx, r9d
0098750B  41 89 4B 14                     mov dword ptr [r11 + 0x14], ecx
0098750F  E9 4B FF FF FF                  jmp 0x14098745f
00987514  49 89 5B 50                     mov qword ptr [r11 + 0x50], rbx
00987518  E9 42 FF FF FF                  jmp 0x14098745f
0098751D  41 89 5B 58                     mov dword ptr [r11 + 0x58], ebx
00987521  8B C3                           mov eax, ebx
00987523  E9 51 FF FF FF                  jmp 0x140987479
00987528  C7 05 C6 62 4A 00 56 00 00 00   mov dword ptr [rip + 0x4a62c6], 0x56
00987532  EB B3                           jmp 0x1409874e7
00987534  41 3B 4B 0C                     cmp ecx, dword ptr [r11 + 0xc]
00987538  0F 84 7B FD FF FF               je 0x1409872b9
0098753E  C7 05 B0 62 4A 00 4C 00 00 00   mov dword ptr [rip + 0x4a62b0], 0x4c
00987548  EB 9D                           jmp 0x1409874e7
0098754A  41 89 5B 58                     mov dword ptr [r11 + 0x58], ebx
0098754E  8B C3                           mov eax, ebx
00987550  E9 FB FC FF FF                  jmp 0x140987250
00987555  C7 05 99 62 4A 00 47 00 00 00   mov dword ptr [rip + 0x4a6299], 0x47
0098755F  EB 86                           jmp 0x1409874e7
00987561  C7 05 8D 62 4A 00 54 00 00 00   mov dword ptr [rip + 0x4a628d], 0x54
0098756B  E9 77 FF FF FF                  jmp 0x1409874e7
00987570  C7 05 7E 62 4A 00 4F 00 00 00   mov dword ptr [rip + 0x4a627e], 0x4f
0098757A  E9 68 FF FF FF                  jmp 0x1409874e7
0098757F  C7 05 6F 62 4A 00 3B 00 00 00   mov dword ptr [rip + 0x4a626f], 0x3b
00987589  E9 BC 3E 1A 00                  jmp 0x140b2b44a
0098758E  66 39 5A 14                     cmp word ptr [rdx + 0x14], bx
00987592  0F 85 7D FB FF FF               jne 0x140987115
00987598  E9 A3 3E 1A 00                  jmp 0x140b2b440
0098759D  8B 05 D9 62 4A 00               mov eax, dword ptr [rip + 0x4a62d9]
009875A3  41 3B 43 40                     cmp eax, dword ptr [r11 + 0x40]
009875A7  0F 85 DD FC FF FF               jne 0x14098728a
009875AD  8B 05 CD 62 4A 00               mov eax, dword ptr [rip + 0x4a62cd]
009875B3  41 3B 43 10                     cmp eax, dword ptr [r11 + 0x10]
009875B7  0F 85 CD FC FF FF               jne 0x14098728a
009875BD  CC                              int3
009875BE  E9 C7 FC FF FF                  jmp 0x14098728a
009875C3  C7 05 2B 62 4A 00 4D 00 00 00   mov dword ptr [rip + 0x4a622b], 0x4d
009875CD  E9 15 FF FF FF                  jmp 0x1409874e7
009875D2  C7 05 1C 62 4A 00 4E 00 00 00   mov dword ptr [rip + 0x4a621c], 0x4e
009875DC  E9 06 FF FF FF                  jmp 0x1409874e7
009875E1  C7 05 0D 62 4A 00 50 00 00 00   mov dword ptr [rip + 0x4a620d], 0x50
009875EB  E9 F7 FE FF FF                  jmp 0x1409874e7
009875F0  C7 05 FE 61 4A 00 51 00 00 00   mov dword ptr [rip + 0x4a61fe], 0x51
009875FA  E9 E8 FE FF FF                  jmp 0x1409874e7
009875FF  BA 64 AA 00 00                  mov edx, 0xaa64
00987604  66 3B C2                        cmp ax, dx
00987607  0F 84 09 FD FF FF               je 0x140987316
0098760D  C7 05 E1 61 4A 00 53 00 00 00   mov dword ptr [rip + 0x4a61e1], 0x53
00987617  E9 CB FE FF FF                  jmp 0x1409874e7
0098761C  C7 05 D2 61 4A 00 55 00 00 00   mov dword ptr [rip + 0x4a61d2], 0x55
00987626  E9 BC FE FF FF                  jmp 0x1409874e7
0098762B  66 41 0F BA 63 3C 0C            bt word ptr [r11 + 0x3c], 0xc
00987632  0F 83 22 FD FF FF               jae 0x14098735a
00987638  C7 05 B6 61 4A 00 57 00 00 00   mov dword ptr [rip + 0x4a61b6], 0x57
00987642  E9 A0 FE FF FF                  jmp 0x1409874e7
00987647  66 45 85 C0                     test r8w, r8w
0098764B  0F 84 03 3E 1A 00               je 0x140b2b454
00987651  C7 05 9D 61 4A 00 58 00 00 00   mov dword ptr [rip + 0x4a619d], 0x58
0098765B  E9 87 FE FF FF                  jmp 0x1409874e7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiVerifyImageHeader(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    if ((((unsigned __int8)(a2)) & (3)) != 0) goto loc_0098757F;
    if ((*(unsigned int *)(a2)) != 0x4550ULL) goto loc_0098736D;
    v_rbx = 0;
    if ((*(unsigned __int16 *)(a2 + 4)) == 0) goto loc_0098758E;
loc_00987115:
    if (((*(unsigned __int8 *)(a2 + 22)) & (2)) == 0) goto loc_00987555;
    *(unsigned __int16 *)(a1 + 48) = (unsigned __int16)(*(unsigned __int16 *)(a2 + 24));
    *(unsigned int *)(a1 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 60)));
    *(unsigned int *)(a1 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 56)));
    *(unsigned int *)(a1 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 80)));
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 24))) != 523) goto loc_00987386;
    *(unsigned int *)(a1 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 128)));
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(a2 + 48);
    *(unsigned int *)(a1 + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 84)));
    *(unsigned int *)(a1 + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 40)));
    *(unsigned __int64 *)(a1 + 32) = *(unsigned __int64 *)(a2 + 96);
    *(unsigned __int64 *)(a1 + 40) = *(unsigned __int64 *)(a2 + 104);
    *(unsigned __int16 *)(a1 + 50) = (unsigned __int16)(*(unsigned __int16 *)(a2 + 92));
    *(unsigned __int16 *)(a1 + 52) = (unsigned __int16)(*(unsigned __int16 *)(a2 + 72));
    *(unsigned __int16 *)(a1 + 54) = (unsigned __int16)(*(unsigned __int16 *)(a2 + 74));
    *(unsigned __int16 *)(a1 + 56) = (unsigned __int16)(*(unsigned __int16 *)(a2 + 64));
    *(unsigned __int16 *)(a1 + 58) = (unsigned __int16)(*(unsigned __int16 *)(a2 + 66));
    *(unsigned __int16 *)(a1 + 60) = (unsigned __int16)(*(unsigned __int16 *)(a2 + 94));
    *(unsigned int *)(a1 + 64) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 88)));
    *(unsigned int *)(a1 + 68) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 28)));
    *(unsigned __int64 *)(a1 + 104) = 0;
    if ((*(unsigned int *)(a2 + 132)) <= 6) goto loc_009871E3;
    result = (unsigned int)(*(unsigned int *)(a2 + 184));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 184))) != 0) {
        *(unsigned int *)(a1 + 104) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 184)));
        result = *(unsigned int *)(a2 + 188);
        *(unsigned int *)(a1 + 108) = (unsigned int)(result);
    }
    if ((*(unsigned int *)(a2 + 132)) >= = 12) {
        result = *(unsigned int *)(a2 + 232);
        *(unsigned int *)(a1 + 72) = (unsigned int)(result);
        result = *(unsigned int *)(a2 + 236);
        *(unsigned int *)(a1 + 76) = (unsigned int)(result);
    }
    if ((*(unsigned int *)(a2 + 132)) <= 14) goto loc_0098737D;
    *(unsigned int *)(a1 + 80) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 248)));
    *(unsigned int *)(a1 + 84) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 252)));
    if ((*(unsigned int *)(a2 + 248)) != 0) goto loc_009874C5;
loc_00987233:
    if ((*(unsigned int *)(a2 + 132)) <= 5) goto loc_0098754A;
    *(unsigned int *)(a1 + 88) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 176)));
loc_00987250:
    *(unsigned int *)(a1 + 92) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 180)));
    if ((*(unsigned int *)(a2 + 132)) <= 10) goto loc_009874F1;
    *(unsigned int *)(a1 + 96) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 216)));
loc_00987271:
    *(unsigned int *)(a1 + 100 * 1) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 220)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4875766))) != 0) goto loc_0098759D;
loc_0098728A:
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a1 + 48))) - (267));
    if ((((unsigned __int16)((unsigned int)(0xFEFFULL))) & ((unsigned __int16)(result))) != 0) goto loc_009874DD;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))) & (511)) != 0) goto loc_00987534;
loc_009872B9:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8))) == 0) goto loc_009875C3;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12)) - 1))) != 0) goto loc_009875D2;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)) - 1))) != 0) goto loc_00987570;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8))))) goto loc_009875E1;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)))) > 0x77000000ULL) goto loc_009875F0;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 48))) == 267) goto loc_00987498;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1 + 48))) != 523) goto loc_00987316;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 4))) != ((unsigned __int16)((unsigned int)(0x8664ULL)))) goto loc_009875FF;
loc_00987316:
    if ((*(unsigned int *)(a1 + 24)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))))) goto loc_00987561;
    if ((*(unsigned __int16 *)(a1)) != 0) goto loc_0098761C;
    if (((*(unsigned __int8 *)(a2 + 20)) & (7)) != 0) goto loc_00987528;
    a3 = (unsigned __int16)((*(unsigned __int16 *)(a2 + 22)) & (1));
    result = MiLegacyImageArchitecture(*(unsigned __int16 *)(a2 + 4), (unsigned int)(0x8664ULL), a3, 1);
    if ((unsigned int)(result) == 0) goto loc_00987647;
    if ((unsigned __int16)(a3) != 0) goto loc_0098762B;
loc_0098735A:
    result = 0;
loc_0098735C:
    v_rsp = (v_rsp) + (32);
    return result;
loc_0098736D:
    result = MiComputeBadImageHeaderType(a2, 0, 1, 1);
    goto loc_0098735C;
loc_0098737D:
    *(unsigned __int64 *)(a1 + 80) = v_stack_p8;
    goto loc_00987233;
loc_00987386:
    *(unsigned int *)(a1 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 112)));
    *(unsigned __int64 *)(a1) = (unsigned int)(*(unsigned int *)(0 + 52));
    *(unsigned int *)(a1 + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 84)));
    *(unsigned int *)(a1 + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 40)));
    *(unsigned __int64 *)(a1 + 32) = (unsigned int)(*(unsigned int *)(0 + 96));
    *(unsigned __int64 *)(a1 + 40) = (unsigned int)(*(unsigned int *)(0 + 100));
    *(unsigned __int16 *)(a1 + 50) = (unsigned __int16)(*(unsigned __int16 *)(0 + 92));
    *(unsigned __int16 *)(a1 + 52) = (unsigned __int16)(*(unsigned __int16 *)(0 + 72));
    *(unsigned __int16 *)(a1 + 54) = (unsigned __int16)(*(unsigned __int16 *)(0 + 74));
    *(unsigned __int16 *)(a1 + 56) = (unsigned __int16)(*(unsigned __int16 *)(0 + 64));
    *(unsigned __int16 *)(a1 + 58) = (unsigned __int16)(*(unsigned __int16 *)(0 + 66));
    *(unsigned __int16 *)(a1 + 60) = (unsigned __int16)(*(unsigned __int16 *)(0 + 94));
    *(unsigned int *)(a1 + 64) = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 88)));
    *(unsigned int *)(a1 + 68) = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 28)));
    *(unsigned __int64 *)(a1 + 104) = v_stack_p8;
    if ((*(unsigned int *)(0 + 116)) <= 6) goto loc_00987415;
    result = (unsigned int)(*(unsigned int *)(0 + 168));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(0 + 168))) != 0) {
        *(unsigned int *)(a1 + 104) = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 168)));
        result = *(unsigned int *)(0 + 172);
        *(unsigned int *)(a1 + 108) = (unsigned int)(result);
    }
    if ((*(unsigned int *)(0 + 116)) >= = 12) {
        result = *(unsigned int *)(0 + 216);
        *(unsigned int *)(a1 + 72) = (unsigned int)(result);
        result = *(unsigned int *)(0 + 220);
        *(unsigned int *)(a1 + 76) = (unsigned int)(result);
    }
    if ((*(unsigned int *)(0 + 116)) <= 14) goto loc_00987514;
    *(unsigned int *)(a1 + 80) = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 232)));
    *(unsigned int *)(a1 + 84) = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 236)));
    if ((*(unsigned int *)(0 + 232)) != ((unsigned int)(v_stack_p8))) goto loc_009874FC;
loc_0098745F:
    if ((*(unsigned int *)(0 + 116)) <= 5) goto loc_0098751D;
    *(unsigned int *)(a1 + 88) = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 160)));
loc_00987479:
    *(unsigned int *)(a1 + 92) = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 164)));
    if ((*(unsigned int *)(0 + 116)) <= 10) goto loc_009874F1;
    *(unsigned int *)(a1 + 96) = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 200)));
    goto loc_00987271;
loc_00987498:
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 4))) == 332) goto loc_00987316;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2 + 4))) == 452) goto loc_00987316;
    *(unsigned int *)(v_rip + 4875061) = 82;
    goto loc_009874E7;
loc_009874C5:
    if ((*(unsigned int *)(452 + 252)) == ((unsigned int)(v_stack_p8))) goto loc_00987233;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 204))) | (1));
    *(unsigned int *)(a1 + 20) = (unsigned int)(a1);
    goto loc_00987233;
loc_009874DD:
    *(unsigned int *)(v_rip + 4875025) = 73;
loc_009874E7:
    goto loc_0098735C;
loc_009874F1:
    *(unsigned int *)(a1 + 96) = (unsigned int)(v_stack_p8);
    goto loc_00987271;
loc_009874FC:
    if ((*(unsigned int *)(452 + 236)) == ((unsigned int)(v_stack_p8))) goto loc_0098745F;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p8))) | (1));
    *(unsigned int *)(a1 + 20) = (unsigned int)(a1);
    goto loc_0098745F;
loc_00987514:
    *(unsigned __int64 *)(a1 + 80) = v_stack_p8;
    goto loc_0098745F;
loc_0098751D:
    *(unsigned int *)(a1 + 88) = (unsigned int)(v_stack_p8);
    goto loc_00987479;
loc_00987528:
    *(unsigned int *)(v_rip + 4874950) = 86;
    goto loc_009874E7;
loc_00987534:
    if (((unsigned int)(a1)) == (*(unsigned int *)(a1 + 12))) goto loc_009872B9;
    *(unsigned int *)(v_rip + 4874928) = 76;
    goto loc_009874E7;
loc_0098754A:
    *(unsigned int *)(a1 + 88) = (unsigned int)(v_stack_p8);
    goto loc_00987250;
loc_00987555:
    *(unsigned int *)(v_rip + 4874905) = 71;
    goto loc_009874E7;
loc_00987561:
    *(unsigned int *)(v_rip + 4874893) = 84;
    goto loc_009874E7;
loc_00987570:
    *(unsigned int *)(v_rip + 4874878) = 79;
    goto loc_009874E7;
loc_0098757F:
    *(unsigned int *)(v_rip + 4874863) = 59;
loc_0098758E:
    if ((*(unsigned __int16 *)(452 + 20)) != ((unsigned __int16)(v_stack_p8))) goto loc_00987115;
loc_0098759D:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4874969)))) != (*(unsigned int *)(a1 + 64))) goto loc_0098728A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4874957)))) != (*(unsigned int *)(a1 + 16))) goto loc_0098728A;
    goto loc_0098728A;
loc_009875C3:
    *(unsigned int *)(v_rip + 4874795) = 77;
    goto loc_009874E7;
loc_009875D2:
    *(unsigned int *)(v_rip + 4874780) = 78;
    goto loc_009874E7;
loc_009875E1:
    *(unsigned int *)(v_rip + 4874765) = 80;
    goto loc_009874E7;
loc_009875F0:
    *(unsigned int *)(v_rip + 4874750) = 81;
    goto loc_009874E7;
loc_009875FF:
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rip + 4874957)))) == ((unsigned __int16)((unsigned int)(0xAA64ULL)))) goto loc_00987316;
    *(unsigned int *)(v_rip + 4874721) = 83;
    goto loc_009874E7;
loc_0098761C:
    *(unsigned int *)(v_rip + 4874706) = 85;
    goto loc_009874E7;
loc_0098762B:
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rip + 4874957)))) >= ((unsigned __int16)((unsigned int)(0xAA64ULL)))) goto loc_0098735A;
    *(unsigned int *)(v_rip + 4874678) = 87;
    goto loc_009874E7;
loc_00987647:
    *(unsigned int *)(v_rip + 4874653) = 88;
    goto loc_009874E7;
}
```

## 5. (Beta) C Style

```c
int64_t MiVerifyImageHeader(void *Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    if ((((uint8_t)(Arg2)) & (3)) != 0) goto loc_0098757F;
    if ((*(uint32_t *)(arg2)) != 0x4550ULL) goto loc_0098736D;
    local_rbx = 0;
    if ((*(uint16_t *)(arg2 + 0x4)) == 0) goto loc_0098758E;
loc_00987115:
    if (((*(uint8_t *)(arg2 + 0x16)) & (2)) == 0) goto loc_00987555;
    *(uint16_t *)(arg1 + 0x30) = (uint16_t)(*(uint16_t *)(arg2 + 0x18));
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x3C)));
    *(uint32_t *)(arg1 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x38)));
    *(uint32_t *)(arg1 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x50)));
    if (((uint16_t)(*(uint16_t *)(arg2 + 0x18))) != 523) goto loc_00987386;
    *(uint32_t *)(arg1 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x80)));
    *(uint64_t *)(arg1) = *(uint64_t *)(arg2 + 0x30);
    *(uint32_t *)(arg1 + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x54)));
    *(uint32_t *)(arg1 + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x28)));
    *(uint64_t *)(arg1 + 0x20) = *(uint64_t *)(arg2 + 0x60);
    *(uint64_t *)(arg1 + 0x28) = *(uint64_t *)(arg2 + 0x68);
    *(uint16_t *)(arg1 + 0x32) = (uint16_t)(*(uint16_t *)(arg2 + 0x5C));
    *(uint16_t *)(arg1 + 0x34) = (uint16_t)(*(uint16_t *)(arg2 + 0x48));
    *(uint16_t *)(arg1 + 0x36) = (uint16_t)(*(uint16_t *)(arg2 + 0x4A));
    *(uint16_t *)(arg1 + 0x38) = (uint16_t)(*(uint16_t *)(arg2 + 0x40));
    *(uint16_t *)(arg1 + 0x3A) = (uint16_t)(*(uint16_t *)(arg2 + 0x42));
    *(uint16_t *)(arg1 + 0x3C) = (uint16_t)(*(uint16_t *)(arg2 + 0x5E));
    *(uint32_t *)(arg1 + 0x40) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x58)));
    *(uint32_t *)(arg1 + 0x44) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x1C)));
    *(uint64_t *)(arg1 + 0x68) = 0;
    if ((*(uint32_t *)(arg2 + 0x84)) <= 6) goto loc_009871E3;
    result = (uint32_t)(*(uint32_t *)(arg2 + 0xB8));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xB8))) != 0) {
        *(uint32_t *)(arg1 + 0x68) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xB8)));
        result = *(uint32_t *)(arg2 + 0xBC);
        *(uint32_t *)(arg1 + 0x6C) = (uint32_t)(result);
    }
    if ((*(uint32_t *)(arg2 + 0x84)) >= = 12) {
        result = *(uint32_t *)(arg2 + 0xE8);
        *(uint32_t *)(arg1 + 0x48) = (uint32_t)(result);
        result = *(uint32_t *)(arg2 + 0xEC);
        *(uint32_t *)(arg1 + 0x4C) = (uint32_t)(result);
    }
    if ((*(uint32_t *)(arg2 + 0x84)) <= 14) goto loc_0098737D;
    *(uint32_t *)(arg1 + 0x50) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xF8)));
    *(uint32_t *)(arg1 + 0x54) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xFC)));
    if ((*(uint32_t *)(arg2 + 0xF8)) != 0) goto loc_009874C5;
loc_00987233:
    if ((*(uint32_t *)(arg2 + 0x84)) <= 5) goto loc_0098754A;
    *(uint32_t *)(arg1 + 0x58) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xB0)));
loc_00987250:
    *(uint32_t *)(arg1 + 0x5C) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xB4)));
    if ((*(uint32_t *)(arg2 + 0x84)) <= 10) goto loc_009874F1;
    *(uint32_t *)(arg1 + 0x60) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xD8)));
loc_00987271:
    *(uint32_t *)(arg1 + 0x64 * 1) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xDC)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4A65F6))) != 0) goto loc_0098759D;
loc_0098728A:
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(arg1 + 0x30))) - (267));
    if ((((uint16_t)((uint32_t)(0xFEFFULL))) & ((uint16_t)(result))) != 0) goto loc_009874DD;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))) & (511)) != 0) goto loc_00987534;
loc_009872B9:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8))) == 0) goto loc_009875C3;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC)) - 1))) != 0) goto loc_009875D2;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)) - 1))) != 0) goto loc_00987570;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8))))) goto loc_009875E1;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)))) > 0x77000000ULL) goto loc_009875F0;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x30))) == 267) goto loc_00987498;
    if (((uint16_t)(*(uint16_t *)(arg1 + 0x30))) != 523) goto loc_00987316;
    if (((uint16_t)(*(uint16_t *)(arg2 + 0x4))) != ((uint16_t)((uint32_t)(0x8664ULL)))) goto loc_009875FF;
loc_00987316:
    if ((*(uint32_t *)(arg1 + 0x18)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))))) goto loc_00987561;
    if ((*(uint16_t *)(arg1)) != 0) goto loc_0098761C;
    if (((*(uint8_t *)(arg2 + 0x14)) & (7)) != 0) goto loc_00987528;
    Arg3 = (uint16_t)((*(uint16_t *)(arg2 + 0x16)) & (1));
    result = MiLegacyImageArchitecture(*(uint16_t *)(arg2 + 0x4), (uint32_t)(0x8664ULL), Arg3, 1);
    if ((uint32_t)(result) == 0) goto loc_00987647;
    if ((uint16_t)(Arg3) != 0) goto loc_0098762B;
loc_0098735A:
    result = 0;
loc_0098735C:
    local_rsp = (local_rsp) + (32);
    return result;
loc_0098736D:
    result = MiComputeBadImageHeaderType(Arg2, 0, 1, 1);
    goto loc_0098735C;
loc_0098737D:
    *(uint64_t *)(arg1 + 0x50) = v_stack_p8;
    goto loc_00987233;
loc_00987386:
    *(uint32_t *)(arg1 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x70)));
    *(uint64_t *)(arg1) = (uint32_t)(*(uint32_t *)(0 + 0x34));
    *(uint32_t *)(arg1 + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x54)));
    *(uint32_t *)(arg1 + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x28)));
    *(uint64_t *)(arg1 + 0x20) = (uint32_t)(*(uint32_t *)(0 + 0x60));
    *(uint64_t *)(arg1 + 0x28) = (uint32_t)(*(uint32_t *)(0 + 0x64));
    *(uint16_t *)(arg1 + 0x32) = (uint16_t)(*(uint16_t *)(0 + 0x5C));
    *(uint16_t *)(arg1 + 0x34) = (uint16_t)(*(uint16_t *)(0 + 0x48));
    *(uint16_t *)(arg1 + 0x36) = (uint16_t)(*(uint16_t *)(0 + 0x4A));
    *(uint16_t *)(arg1 + 0x38) = (uint16_t)(*(uint16_t *)(0 + 0x40));
    *(uint16_t *)(arg1 + 0x3A) = (uint16_t)(*(uint16_t *)(0 + 0x42));
    *(uint16_t *)(arg1 + 0x3C) = (uint16_t)(*(uint16_t *)(0 + 0x5E));
    *(uint32_t *)(arg1 + 0x40) = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x58)));
    *(uint32_t *)(arg1 + 0x44) = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x1C)));
    *(uint64_t *)(arg1 + 0x68) = v_stack_p8;
    if ((*(uint32_t *)(0 + 0x74)) <= 6) goto loc_00987415;
    result = (uint32_t)(*(uint32_t *)(0 + 0xA8));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0xA8))) != 0) {
        *(uint32_t *)(arg1 + 0x68) = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0xA8)));
        result = *(uint32_t *)(0 + 0xAC);
        *(uint32_t *)(arg1 + 0x6C) = (uint32_t)(result);
    }
    if ((*(uint32_t *)(0 + 0x74)) >= = 12) {
        result = *(uint32_t *)(0 + 0xD8);
        *(uint32_t *)(arg1 + 0x48) = (uint32_t)(result);
        result = *(uint32_t *)(0 + 0xDC);
        *(uint32_t *)(arg1 + 0x4C) = (uint32_t)(result);
    }
    if ((*(uint32_t *)(0 + 0x74)) <= 14) goto loc_00987514;
    *(uint32_t *)(arg1 + 0x50) = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0xE8)));
    *(uint32_t *)(arg1 + 0x54) = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0xEC)));
    if ((*(uint32_t *)(0 + 0xE8)) != ((uint32_t)(v_stack_p8))) goto loc_009874FC;
loc_0098745F:
    if ((*(uint32_t *)(0 + 0x74)) <= 5) goto loc_0098751D;
    *(uint32_t *)(arg1 + 0x58) = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0xA0)));
loc_00987479:
    *(uint32_t *)(arg1 + 0x5C) = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0xA4)));
    if ((*(uint32_t *)(0 + 0x74)) <= 10) goto loc_009874F1;
    *(uint32_t *)(arg1 + 0x60) = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0xC8)));
    goto loc_00987271;
loc_00987498:
    if (((uint16_t)(*(uint16_t *)(arg2 + 0x4))) == 332) goto loc_00987316;
    if (((uint16_t)(*(uint16_t *)(arg2 + 0x4))) == 452) goto loc_00987316;
    *(uint32_t *)(v_rip + 0x4A6335) = 82;
    goto loc_009874E7;
loc_009874C5:
    if ((*(uint32_t *)(452 + 0xFC)) == ((uint32_t)(v_stack_p8))) goto loc_00987233;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0xCC))) | (1));
    *(uint32_t *)(arg1 + 0x14) = (uint32_t)(Arg1);
    goto loc_00987233;
loc_009874DD:
    *(uint32_t *)(v_rip + 0x4A6311) = 73;
loc_009874E7:
    goto loc_0098735C;
loc_009874F1:
    *(uint32_t *)(arg1 + 0x60) = (uint32_t)(v_stack_p8);
    goto loc_00987271;
loc_009874FC:
    if ((*(uint32_t *)(452 + 0xEC)) == ((uint32_t)(v_stack_p8))) goto loc_0098745F;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p8))) | (1));
    *(uint32_t *)(arg1 + 0x14) = (uint32_t)(Arg1);
    goto loc_0098745F;
loc_00987514:
    *(uint64_t *)(arg1 + 0x50) = v_stack_p8;
    goto loc_0098745F;
loc_0098751D:
    *(uint32_t *)(arg1 + 0x58) = (uint32_t)(v_stack_p8);
    goto loc_00987479;
loc_00987528:
    *(uint32_t *)(v_rip + 0x4A62C6) = 86;
    goto loc_009874E7;
loc_00987534:
    if (((uint32_t)(Arg1)) == (*(uint32_t *)(arg1 + 0xC))) goto loc_009872B9;
    *(uint32_t *)(v_rip + 0x4A62B0) = 76;
    goto loc_009874E7;
loc_0098754A:
    *(uint32_t *)(arg1 + 0x58) = (uint32_t)(v_stack_p8);
    goto loc_00987250;
loc_00987555:
    *(uint32_t *)(v_rip + 0x4A6299) = 71;
    goto loc_009874E7;
loc_00987561:
    *(uint32_t *)(v_rip + 0x4A628D) = 84;
    goto loc_009874E7;
loc_00987570:
    *(uint32_t *)(v_rip + 0x4A627E) = 79;
    goto loc_009874E7;
loc_0098757F:
    *(uint32_t *)(v_rip + 0x4A626F) = 59;
loc_0098758E:
    if ((*(uint16_t *)(452 + 0x14)) != ((uint16_t)(v_stack_p8))) goto loc_00987115;
loc_0098759D:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4A62D9)))) != (*(uint32_t *)(arg1 + 0x40))) goto loc_0098728A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4A62CD)))) != (*(uint32_t *)(arg1 + 0x10))) goto loc_0098728A;
    goto loc_0098728A;
loc_009875C3:
    *(uint32_t *)(v_rip + 0x4A622B) = 77;
    goto loc_009874E7;
loc_009875D2:
    *(uint32_t *)(v_rip + 0x4A621C) = 78;
    goto loc_009874E7;
loc_009875E1:
    *(uint32_t *)(v_rip + 0x4A620D) = 80;
    goto loc_009874E7;
loc_009875F0:
    *(uint32_t *)(v_rip + 0x4A61FE) = 81;
    goto loc_009874E7;
loc_009875FF:
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4A62CD)))) == ((uint16_t)((uint32_t)(0xAA64ULL)))) goto loc_00987316;
    *(uint32_t *)(v_rip + 0x4A61E1) = 83;
    goto loc_009874E7;
loc_0098761C:
    *(uint32_t *)(v_rip + 0x4A61D2) = 85;
    goto loc_009874E7;
loc_0098762B:
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_rip + 0x4A62CD)))) >= ((uint16_t)((uint32_t)(0xAA64ULL)))) goto loc_0098735A;
    *(uint32_t *)(v_rip + 0x4A61B6) = 87;
    goto loc_009874E7;
loc_00987647:
    *(uint32_t *)(v_rip + 0x4A619D) = 88;
    goto loc_009874E7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x0 + rax*1` | `32` | `W` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x8` | `32` | `W` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `W` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x10` | `32` | `W` |
| `Arg1` | `+ 0x14` | `32` | `W` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x18` | `32` | `W` |
| `Arg1` | `+ 0x1C` | `32` | `W` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x30` | `16` | `R` |
| `Arg1` | `+ 0x30` | `16` | `W` |
| `Arg1` | `+ 0x32` | `16` | `W` |
| `Arg1` | `+ 0x34` | `16` | `W` |
| `Arg1` | `+ 0x36` | `16` | `W` |
| `Arg1` | `+ 0x38` | `16` | `W` |
| `Arg1` | `+ 0x3A` | `16` | `W` |
| `Arg1` | `+ 0x3C` | `16` | `W` |
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg1` | `+ 0x40` | `32` | `W` |
| `Arg1` | `+ 0x44` | `32` | `W` |
| `Arg1` | `+ 0x48` | `32` | `W` |
| `Arg1` | `+ 0x4C` | `32` | `W` |
| `Arg1` | `+ 0x50` | `32` | `W` |
| `Arg1` | `+ 0x50` | `64` | `W` |
| `Arg1` | `+ 0x54` | `32` | `W` |
| `Arg1` | `+ 0x58` | `32` | `W` |

추가 오프셋 8개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009870DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
