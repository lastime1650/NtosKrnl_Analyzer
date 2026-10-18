# woutput_s

- RVA: `0x005073AC`–`0x00507CF1` (길이 `2,373` bytes)
- VA: `0x00000001405073AC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2988`
- 디코드: `648`개 명령, `2,373/2,373` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00507418` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005076B8` → [mbtowc](mbtowc_function_005008E0.md) (function, `0x005008E0`)
- `0x00507905` → [write_char](write_char_function_00507CF8.md) (function, `0x00507CF8`)
- `0x0050794E` → [write_char](write_char_function_00507CF8.md) (function, `0x00507CF8`)
- `0x00507984` → [write_char](write_char_function_00507CF8.md) (function, `0x00507CF8`)
- `0x005079C1` → [mbtowc](mbtowc_function_005008E0.md) (function, `0x005008E0`)
- `0x005079EE` → [write_char](write_char_function_00507CF8.md) (function, `0x00507CF8`)
- `0x00507A3A` → [write_char](write_char_function_00507CF8.md) (function, `0x00507CF8`)
- `0x00507A6C` → [write_char](write_char_function_00507CF8.md) (function, `0x00507CF8`)
- `0x00507B83` → [write_char](write_char_function_00507CF8.md) (function, `0x00507CF8`)
- `0x00507CBE` → [EmpCheckErrataList](../49/EmpCheckErrataList_function_0049E550.md) (function, `0x0049E550`)
- `0x00507CD0` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [swoutput_s](swoutput_s_function_00507278.md) at `0x005072F3`

### Static image references
- `0x005073CB` → RVA `0x00E0A740` (`.data`; read)
- `0x0050747D` → RVA `0x0001F830` (`.rdata`; read)
- `0x005075DE` → RVA `0x0001EF98` (`.rdata`; read)
- `0x0050769F` → RVA `0x00E0A700` (`.data`; read)
- `0x00507723` → RVA `0x0002AEF8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005073AC  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
005073B1  55                              push rbp
005073B2  56                              push rsi
005073B3  57                              push rdi
005073B4  41 54                           push r12
005073B6  41 55                           push r13
005073B8  41 56                           push r14
005073BA  41 57                           push r15
005073BC  48 8D AC 24 70 FC FF FF         lea rbp, [rsp - 0x390]
005073C4  48 81 EC 90 04 00 00            sub rsp, 0x490
005073CB  48 8B 05 6E 33 90 00            mov rax, qword ptr [rip + 0x90336e]
005073D2  48 33 C4                        xor rax, rsp
005073D5  48 89 85 80 03 00 00            mov qword ptr [rbp + 0x380], rax
005073DC  48 8B F9                        mov rdi, rcx
005073DF  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
005073E4  33 C9                           xor ecx, ecx
005073E6  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
005073EB  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
005073EF  44 8B F1                        mov r14d, ecx
005073F2  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
005073F6  8B F1                           mov esi, ecx
005073F8  89 4C 24 3C                     mov dword ptr [rsp + 0x3c], ecx
005073FC  8B D9                           mov ebx, ecx
005073FE  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
00507402  4D 8B F8                        mov r15, r8
00507405  89 4C 24 64                     mov dword ptr [rsp + 0x64], ecx
00507409  4C 8B EA                        mov r13, rdx
0050740C  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00507410  33 D2                           xor edx, edx
00507412  41 B8 00 04 00 00               mov r8d, 0x400
00507418  E8 23 F8 1B 00                  call 0x1406c6c40
0050741D  45 33 DB                        xor r11d, r11d
00507420  66 44 89 5C 24 40               mov word ptr [rsp + 0x40], r11w
00507426  44 89 5C 24 44                  mov dword ptr [rsp + 0x44], r11d
0050742B  48 85 FF                        test rdi, rdi
0050742E  0F 84 7B 08 00 00               je 0x140507caf
00507434  4D 85 ED                        test r13, r13
00507437  0F 84 72 08 00 00               je 0x140507caf
0050743D  45 0F B7 4D 00                  movzx r9d, word ptr [r13]
00507442  41 8B FB                        mov edi, r11d
00507445  44 89 5C 24 34                  mov dword ptr [rsp + 0x34], r11d
0050744A  45 8B E3                        mov r12d, r11d
0050744D  45 8B D3                        mov r10d, r11d
00507450  66 45 85 C9                     test r9w, r9w
00507454  0F 84 51 08 00 00               je 0x140507cab
0050745A  8D 4B 20                        lea ecx, [rbx + 0x20]
0050745D  49 83 C5 02                     add r13, 2
00507461  4D 8B C7                        mov r8, r15
00507464  85 FF                           test edi, edi
00507466  0F 88 34 08 00 00               js 0x140507ca0
0050746C  41 0F B7 C1                     movzx eax, r9w
00507470  66 2B C1                        sub ax, cx
00507473  66 83 F8 5A                     cmp ax, 0x5a
00507477  77 15                           ja 0x14050748e
00507479  41 0F B7 C1                     movzx eax, r9w
0050747D  48 8D 0D AC 83 B1 FF            lea rcx, [rip - 0x4e7c54]
00507484  0F B6 54 08 E0                  movzx edx, byte ptr [rax + rcx - 0x20]
00507489  83 E2 0F                        and edx, 0xf
0050748C  EB 03                           jmp 0x140507491
0050748E  41 8B D3                        mov edx, r11d
00507491  41 8D 04 D2                     lea eax, [r10 + rdx*8]
00507495  41 0F B7 C9                     movzx ecx, r9w
00507499  03 C2                           add eax, edx
0050749B  48 8D 15 8E 83 B1 FF            lea rdx, [rip - 0x4e7c72]
005074A2  44 0F B6 14 10                  movzx r10d, byte ptr [rax + rdx]
005074A7  41 C1 EA 04                     shr r10d, 4
005074AB  44 89 54 24 30                  mov dword ptr [rsp + 0x30], r10d
005074B0  41 83 FA 08                     cmp r10d, 8
005074B4  0F 84 F5 07 00 00               je 0x140507caf
005074BA  41 8B D2                        mov edx, r10d
005074BD  45 85 D2                        test r10d, r10d
005074C0  0F 84 A7 06 00 00               je 0x140507b6d
005074C6  83 EA 01                        sub edx, 1
005074C9  0F 84 8E 07 00 00               je 0x140507c5d
005074CF  83 EA 01                        sub edx, 1
005074D2  0F 84 3F 07 00 00               je 0x140507c17
005074D8  83 EA 01                        sub edx, 1
005074DB  0F 84 FB 06 00 00               je 0x140507bdc
005074E1  83 EA 01                        sub edx, 1
005074E4  0F 84 E5 06 00 00               je 0x140507bcf
005074EA  83 EA 01                        sub edx, 1
005074ED  0F 84 9E 06 00 00               je 0x140507b91
005074F3  83 EA 01                        sub edx, 1
005074F6  0F 84 8C 05 00 00               je 0x140507a88
005074FC  83 FA 01                        cmp edx, 1
005074FF  0F 85 76 07 00 00               jne 0x140507c7b
00507505  83 F9 69                        cmp ecx, 0x69
00507508  0F 87 D3 01 00 00               ja 0x1405076e1
0050750E  74 31                           je 0x140507541
00507510  83 E9 43                        sub ecx, 0x43
00507513  0F 84 4F 01 00 00               je 0x140507668
00507519  83 E9 10                        sub ecx, 0x10
0050751C  0F 84 D8 00 00 00               je 0x1405075fa
00507522  83 E9 05                        sub ecx, 5
00507525  0F 84 30 02 00 00               je 0x14050775b
0050752B  83 E9 02                        sub ecx, 2
0050752E  74 4D                           je 0x14050757d
00507530  83 E9 09                        sub ecx, 9
00507533  0F 84 42 01 00 00               je 0x14050767b
00507539  3B CA                           cmp ecx, edx
0050753B  0F 85 42 03 00 00               jne 0x140507883
00507541  41 83 CE 40                     or r14d, 0x40
00507545  41 B9 0A 00 00 00               mov r9d, 0xa
0050754B  B9 00 02 00 00                  mov ecx, 0x200
00507550  49 83 C7 08                     add r15, 8
00507554  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00507559  41 0F BA E6 0F                  bt r14d, 0xf
0050755E  72 0B                           jb 0x14050756b
00507560  41 0F BA E6 0C                  bt r14d, 0xc
00507565  0F 83 42 02 00 00               jae 0x1405077ad
0050756B  49 8B 00                        mov rax, qword ptr [r8]
0050756E  41 F6 C6 40                     test r14b, 0x40
00507572  0F 84 6E 02 00 00               je 0x1405077e6
00507578  E9 57 02 00 00                  jmp 0x1405077d4
0050757D  49 8B 08                        mov rcx, qword ptr [r8]
00507580  49 83 C7 08                     add r15, 8
00507584  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00507589  48 85 C9                        test rcx, rcx
0050758C  74 50                           je 0x1405075de
0050758E  48 8B 59 08                     mov rbx, qword ptr [rcx + 8]
00507592  48 85 DB                        test rbx, rbx
00507595  74 47                           je 0x1405075de
00507597  0F B7 01                        movzx eax, word ptr [rcx]
0050759A  66 39 41 02                     cmp word ptr [rcx + 2], ax
0050759E  0F 82 0B 07 00 00               jb 0x140507caf
005075A4  44 8B E0                        mov r12d, eax
005075A7  41 0F BA E6 0B                  bt r14d, 0xb
005075AC  73 26                           jae 0x1405075d4
005075AE  F7 D0                           not eax
005075B0  A8 01                           test al, 1
005075B2  0F 84 F7 06 00 00               je 0x140507caf
005075B8  8B C3                           mov eax, ebx
005075BA  F7 D0                           not eax
005075BC  A8 01                           test al, 1
005075BE  0F 84 EB 06 00 00               je 0x140507caf
005075C4  41 D1 EC                        shr r12d, 1
005075C7  C7 44 24 44 01 00 00 00         mov dword ptr [rsp + 0x44], 1
005075CF  E9 AF 02 00 00                  jmp 0x140507883
005075D4  44 89 5C 24 44                  mov dword ptr [rsp + 0x44], r11d
005075D9  E9 A5 02 00 00                  jmp 0x140507883
005075DE  48 8D 15 B3 79 B1 FF            lea rdx, [rip - 0x4e864d]
005075E5  49 83 CC FF                     or r12, 0xffffffffffffffff
005075E9  48 8B DA                        mov rbx, rdx
005075EC  49 FF C4                        inc r12
005075EF  46 38 1C 22                     cmp byte ptr [rdx + r12], r11b
005075F3  75 F7                           jne 0x1405075ec
005075F5  E9 89 02 00 00                  jmp 0x140507883
005075FA  41 F7 C6 30 08 00 00            test r14d, 0x830
00507601  75 04                           jne 0x140507607
00507603  41 83 CE 20                     or r14d, 0x20
00507607  49 8B 18                        mov rbx, qword ptr [r8]
0050760A  83 FE FF                        cmp esi, -1
0050760D  8B CE                           mov ecx, esi
0050760F  B8 FF FF FF 7F                  mov eax, 0x7fffffff
00507614  0F 44 C8                        cmove ecx, eax
00507617  41 B8 20 00 00 00               mov r8d, 0x20
0050761D  49 83 C7 08                     add r15, 8
00507621  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00507626  45 84 F0                        test r8b, r14b
00507629  0F 84 E9 00 00 00               je 0x140507718
0050762F  48 8B C3                        mov rax, rbx
00507632  48 85 DB                        test rbx, rbx
00507635  75 0D                           jne 0x140507644
00507637  48 8D 15 5A 79 B1 FF            lea rdx, [rip - 0x4e86a6]
0050763E  48 8B DA                        mov rbx, rdx
00507641  48 8B C2                        mov rax, rdx
00507644  45 8B E3                        mov r12d, r11d
00507647  85 C9                           test ecx, ecx
00507649  0F 8E 3A 02 00 00               jle 0x140507889
0050764F  44 38 18                        cmp byte ptr [rax], r11b
00507652  0F 84 31 02 00 00               je 0x140507889
00507658  48 FF C0                        inc rax
0050765B  41 FF C4                        inc r12d
0050765E  44 3B E1                        cmp r12d, ecx
00507661  7C EC                           jl 0x14050764f
00507663  E9 21 02 00 00                  jmp 0x140507889
00507668  BA 20 00 00 00                  mov edx, 0x20
0050766D  41 F7 C6 30 08 00 00            test r14d, 0x830
00507674  75 0A                           jne 0x140507680
00507676  44 0B F2                        or r14d, edx
00507679  EB 05                           jmp 0x140507680
0050767B  BA 20 00 00 00                  mov edx, 0x20
00507680  41 0F B7 00                     movzx eax, word ptr [r8]
00507684  49 83 C7 08                     add r15, 8
00507688  C7 44 24 44 01 00 00 00         mov dword ptr [rsp + 0x44], 1
00507690  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00507695  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
0050769A  44 84 F2                        test dl, r14b
0050769D  74 2F                           je 0x1405076ce
0050769F  4C 63 05 5A 30 90 00            movsxd r8, dword ptr [rip + 0x90305a]
005076A6  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
005076AB  48 8D 4D 80                     lea rcx, [rbp - 0x80]
005076AF  88 44 24 48                     mov byte ptr [rsp + 0x48], al
005076B3  44 88 5C 24 49                  mov byte ptr [rsp + 0x49], r11b
005076B8  E8 23 92 FF FF                  call 0x1405008e0
005076BD  45 33 DB                        xor r11d, r11d
005076C0  85 C0                           test eax, eax
005076C2  79 0E                           jns 0x1405076d2
005076C4  C7 44 24 64 01 00 00 00         mov dword ptr [rsp + 0x64], 1
005076CC  EB 04                           jmp 0x1405076d2
005076CE  66 89 45 80                     mov word ptr [rbp - 0x80], ax
005076D2  48 8D 5D 80                     lea rbx, [rbp - 0x80]
005076D6  41 BC 01 00 00 00               mov r12d, 1
005076DC  E9 A2 01 00 00                  jmp 0x140507883
005076E1  83 E9 6E                        sub ecx, 0x6e
005076E4  0F 84 C5 05 00 00               je 0x140507caf
005076EA  83 E9 01                        sub ecx, 1
005076ED  0F 84 9C 00 00 00               je 0x14050778f
005076F3  83 E9 01                        sub ecx, 1
005076F6  74 59                           je 0x140507751
005076F8  83 E9 03                        sub ecx, 3
005076FB  0F 84 06 FF FF FF               je 0x140507607
00507701  83 E9 02                        sub ecx, 2
00507704  0F 84 3B FE FF FF               je 0x140507545
0050770A  83 F9 03                        cmp ecx, 3
0050770D  0F 85 70 01 00 00               jne 0x140507883
00507713  8D 41 24                        lea eax, [rcx + 0x24]
00507716  EB 48                           jmp 0x140507760
00507718  48 85 DB                        test rbx, rbx
0050771B  C7 44 24 44 01 00 00 00         mov dword ptr [rsp + 0x44], 1
00507723  48 8D 05 CE 37 B2 FF            lea rax, [rip - 0x4dc832]
0050772A  48 0F 45 C3                     cmovne rax, rbx
0050772E  48 8B D8                        mov rbx, rax
00507731  EB 0C                           jmp 0x14050773f
00507733  FF C9                           dec ecx
00507735  66 44 39 18                     cmp word ptr [rax], r11w
00507739  74 08                           je 0x140507743
0050773B  48 83 C0 02                     add rax, 2
0050773F  85 C9                           test ecx, ecx
00507741  75 F0                           jne 0x140507733
00507743  48 2B C3                        sub rax, rbx
00507746  48 D1 F8                        sar rax, 1
00507749  44 8B E0                        mov r12d, eax
0050774C  E9 38 01 00 00                  jmp 0x140507889
00507751  BE 10 00 00 00                  mov esi, 0x10
00507756  41 0F BA EE 0F                  bts r14d, 0xf
0050775B  B8 07 00 00 00                  mov eax, 7
00507760  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00507764  45 84 F6                        test r14b, r14b
00507767  79 1B                           jns 0x140507784
00507769  B9 30 00 00 00                  mov ecx, 0x30
0050776E  C7 44 24 38 02 00 00 00         mov dword ptr [rsp + 0x38], 2
00507776  66 83 C0 51                     add ax, 0x51
0050777A  66 89 4C 24 4C                  mov word ptr [rsp + 0x4c], cx
0050777F  66 89 44 24 4E                  mov word ptr [rsp + 0x4e], ax
00507784  41 B9 10 00 00 00               mov r9d, 0x10
0050778A  E9 BC FD FF FF                  jmp 0x14050754b
0050778F  B8 08 00 00 00                  mov eax, 8
00507794  44 8B C8                        mov r9d, eax
00507797  45 84 F6                        test r14b, r14b
0050779A  0F 89 AB FD FF FF               jns 0x14050754b
005077A0  B9 00 02 00 00                  mov ecx, 0x200
005077A5  44 0B F1                        or r14d, ecx
005077A8  E9 A3 FD FF FF                  jmp 0x140507550
005077AD  41 8B C6                        mov eax, r14d
005077B0  BA 20 00 00 00                  mov edx, 0x20
005077B5  83 E0 40                        and eax, 0x40
005077B8  44 84 F2                        test dl, r14b
005077BB  74 10                           je 0x1405077cd
005077BD  85 C0                           test eax, eax
005077BF  74 06                           je 0x1405077c7
005077C1  49 0F BF 00                     movsx rax, word ptr [r8]
005077C5  EB 0D                           jmp 0x1405077d4
005077C7  41 0F B7 00                     movzx eax, word ptr [r8]
005077CB  EB 19                           jmp 0x1405077e6
005077CD  85 C0                           test eax, eax
005077CF  74 12                           je 0x1405077e3
005077D1  49 63 00                        movsxd rax, dword ptr [r8]
005077D4  48 85 C0                        test rax, rax
005077D7  79 0D                           jns 0x1405077e6
005077D9  48 F7 D8                        neg rax
005077DC  41 0F BA EE 08                  bts r14d, 8
005077E1  EB 03                           jmp 0x1405077e6
005077E3  41 8B 00                        mov eax, dword ptr [r8]
005077E6  41 F7 C6 00 90 00 00            test r14d, 0x9000
005077ED  44 8B C0                        mov r8d, eax
005077F0  4C 0F 45 C0                     cmovne r8, rax
005077F4  85 F6                           test esi, esi
005077F6  79 07                           jns 0x1405077ff
005077F8  BE 01 00 00 00                  mov esi, 1
005077FD  EB 09                           jmp 0x140507808
005077FF  41 83 E6 F7                     and r14d, 0xfffffff7
00507803  3B F1                           cmp esi, ecx
00507805  0F 4F F1                        cmovg esi, ecx
00507808  44 8B 54 24 60                  mov r10d, dword ptr [rsp + 0x60]
0050780D  49 8B C0                        mov rax, r8
00507810  48 F7 D8                        neg rax
00507813  1B C9                           sbb ecx, ecx
00507815  21 4C 24 38                     and dword ptr [rsp + 0x38], ecx
00507819  48 8D 8D 7F 01 00 00            lea rcx, [rbp + 0x17f]
00507820  8B C6                           mov eax, esi
00507822  FF CE                           dec esi
00507824  85 C0                           test eax, eax
00507826  7F 05                           jg 0x14050782d
00507828  4D 85 C0                        test r8, r8
0050782B  74 1D                           je 0x14050784a
0050782D  33 D2                           xor edx, edx
0050782F  49 8B C0                        mov rax, r8
00507832  49 F7 F1                        div r9
00507835  83 C2 30                        add edx, 0x30
00507838  4C 8B C0                        mov r8, rax
0050783B  83 FA 39                        cmp edx, 0x39
0050783E  7E 03                           jle 0x140507843
00507840  41 03 D2                        add edx, r10d
00507843  88 11                           mov byte ptr [rcx], dl
00507845  48 FF C9                        dec rcx
00507848  EB D6                           jmp 0x140507820
0050784A  4C 8D A5 7F 01 00 00            lea r12, [rbp + 0x17f]
00507851  89 74 24 3C                     mov dword ptr [rsp + 0x3c], esi
00507855  44 2B E1                        sub r12d, ecx
00507858  48 8D 59 01                     lea rbx, [rcx + 1]
0050785C  41 0F BA E6 09                  bt r14d, 9
00507861  73 20                           jae 0x140507883
00507863  B8 30 00 00 00                  mov eax, 0x30
00507868  45 85 E4                        test r12d, r12d
0050786B  74 09                           je 0x140507876
0050786D  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00507872  38 03                           cmp byte ptr [rbx], al
00507874  74 0D                           je 0x140507883
00507876  48 FF CB                        dec rbx
00507879  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
0050787E  41 FF C4                        inc r12d
00507881  88 03                           mov byte ptr [rbx], al
00507883  41 B8 20 00 00 00               mov r8d, 0x20
00507889  44 39 5C 24 64                  cmp dword ptr [rsp + 0x64], r11d
0050788E  0F 85 EE 03 00 00               jne 0x140507c82
00507894  41 F6 C6 40                     test r14b, 0x40
00507898  74 37                           je 0x1405078d1
0050789A  41 0F BA E6 08                  bt r14d, 8
0050789F  73 07                           jae 0x1405078a8
005078A1  B8 2D 00 00 00                  mov eax, 0x2d
005078A6  EB 0B                           jmp 0x1405078b3
005078A8  41 F6 C6 01                     test r14b, 1
005078AC  74 15                           je 0x1405078c3
005078AE  B8 2B 00 00 00                  mov eax, 0x2b
005078B3  66 89 44 24 4C                  mov word ptr [rsp + 0x4c], ax
005078B8  B9 01 00 00 00                  mov ecx, 1
005078BD  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
005078C1  EB 12                           jmp 0x1405078d5
005078C3  41 F6 C6 02                     test r14b, 2
005078C7  74 08                           je 0x1405078d1
005078C9  66 44 89 44 24 4C               mov word ptr [rsp + 0x4c], r8w
005078CF  EB E7                           jmp 0x1405078b8
005078D1  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
005078D5  44 8B 7C 24 50                  mov r15d, dword ptr [rsp + 0x50]
005078DA  45 8B DE                        mov r11d, r14d
005078DD  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
005078E2  45 2B FC                        sub r15d, r12d
005078E5  44 2B F9                        sub r15d, ecx
005078E8  41 83 E3 0C                     and r11d, 0xc
005078EC  75 32                           jne 0x140507920
005078EE  45 8B CF                        mov r9d, r15d
005078F1  45 85 FF                        test r15d, r15d
005078F4  7E 2A                           jle 0x140507920
005078F6  BE 20 00 00 00                  mov esi, 0x20
005078FB  8B CE                           mov ecx, esi
005078FD  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00507902  41 FF C9                        dec r9d
00507905  E8 EE 03 00 00                  call 0x140507cf8
0050790A  8B 7C 24 34                     mov edi, dword ptr [rsp + 0x34]
0050790E  83 FF FF                        cmp edi, -1
00507911  74 05                           je 0x140507918
00507913  45 85 C9                        test r9d, r9d
00507916  7F E3                           jg 0x1405078fb
00507918  8B 74 24 3C                     mov esi, dword ptr [rsp + 0x3c]
0050791C  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
00507920  8B 42 18                        mov eax, dword ptr [rdx + 0x18]
00507923  4C 8D 54 24 4C                  lea r10, [rsp + 0x4c]
00507928  44 8B C9                        mov r9d, ecx
0050792B  A8 40                           test al, 0x40
0050792D  74 0F                           je 0x14050793e
0050792F  48 83 7A 10 00                  cmp qword ptr [rdx + 0x10], 0
00507934  75 08                           jne 0x14050793e
00507936  03 F9                           add edi, ecx
00507938  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
0050793C  EB 27                           jmp 0x140507965
0050793E  85 C9                           test ecx, ecx
00507940  7E 23                           jle 0x140507965
00507942  41 0F B7 0A                     movzx ecx, word ptr [r10]
00507946  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
0050794B  41 FF C9                        dec r9d
0050794E  E8 A5 03 00 00                  call 0x140507cf8
00507953  8B 7C 24 34                     mov edi, dword ptr [rsp + 0x34]
00507957  4D 8D 52 02                     lea r10, [r10 + 2]
0050795B  83 FF FF                        cmp edi, -1
0050795E  74 05                           je 0x140507965
00507960  45 85 C9                        test r9d, r9d
00507963  7F DD                           jg 0x140507942
00507965  41 83 FB 08                     cmp r11d, 8
00507969  75 32                           jne 0x14050799d
0050796B  45 33 DB                        xor r11d, r11d
0050796E  45 8B CF                        mov r9d, r15d
00507971  45 85 FF                        test r15d, r15d
00507974  7E 2A                           jle 0x1405079a0
00507976  41 8D 73 30                     lea esi, [r11 + 0x30]
0050797A  8B CE                           mov ecx, esi
0050797C  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00507981  41 FF C9                        dec r9d
00507984  E8 6F 03 00 00                  call 0x140507cf8
00507989  8B 7C 24 34                     mov edi, dword ptr [rsp + 0x34]
0050798D  83 FF FF                        cmp edi, -1
00507990  74 05                           je 0x140507997
00507992  45 85 C9                        test r9d, r9d
00507995  7F E3                           jg 0x14050797a
00507997  8B 74 24 3C                     mov esi, dword ptr [rsp + 0x3c]
0050799B  EB 03                           jmp 0x1405079a0
0050799D  45 33 DB                        xor r11d, r11d
005079A0  44 39 5C 24 44                  cmp dword ptr [rsp + 0x44], r11d
005079A5  75 66                           jne 0x140507a0d
005079A7  45 85 E4                        test r12d, r12d
005079AA  7E 61                           jle 0x140507a0d
005079AC  48 8B F3                        mov rsi, rbx
005079AF  41 8B FC                        mov edi, r12d
005079B2  4C 63 05 47 2D 90 00            movsxd r8, dword ptr [rip + 0x902d47]
005079B9  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
005079BE  48 8B D6                        mov rdx, rsi
005079C1  E8 1A 8F FF FF                  call 0x1405008e0
005079C6  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
005079CB  45 33 DB                        xor r11d, r11d
005079CE  4C 63 C8                        movsxd r9, eax
005079D1  41 8B C3                        mov eax, r11d
005079D4  41 83 F9 02                     cmp r9d, 2
005079D8  0F 94 C0                        sete al
005079DB  FF C0                           inc eax
005079DD  2B F8                           sub edi, eax
005079DF  45 85 C9                        test r9d, r9d
005079E2  7E 1C                           jle 0x140507a00
005079E4  0F B7 4C 24 40                  movzx ecx, word ptr [rsp + 0x40]
005079E9  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
005079EE  E8 05 03 00 00                  call 0x140507cf8
005079F3  49 03 F1                        add rsi, r9
005079F6  85 FF                           test edi, edi
005079F8  7F B8                           jg 0x1405079b2
005079FA  8B 7C 24 34                     mov edi, dword ptr [rsp + 0x34]
005079FE  EB 07                           jmp 0x140507a07
00507A00  83 CF FF                        or edi, 0xffffffff
00507A03  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
00507A07  8B 74 24 3C                     mov esi, dword ptr [rsp + 0x3c]
00507A0B  EB 44                           jmp 0x140507a51
00507A0D  8B 42 18                        mov eax, dword ptr [rdx + 0x18]
00507A10  45 8B CC                        mov r9d, r12d
00507A13  4C 8B D3                        mov r10, rbx
00507A16  A8 40                           test al, 0x40
00507A18  74 0F                           je 0x140507a29
00507A1A  4C 39 5A 10                     cmp qword ptr [rdx + 0x10], r11
00507A1E  75 09                           jne 0x140507a29
00507A20  41 03 FC                        add edi, r12d
00507A23  89 7C 24 34                     mov dword ptr [rsp + 0x34], edi
00507A27  EB 28                           jmp 0x140507a51
00507A29  45 85 E4                        test r12d, r12d
00507A2C  7E 23                           jle 0x140507a51
00507A2E  41 0F B7 0A                     movzx ecx, word ptr [r10]
00507A32  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00507A37  41 FF C9                        dec r9d
00507A3A  E8 B9 02 00 00                  call 0x140507cf8
00507A3F  8B 7C 24 34                     mov edi, dword ptr [rsp + 0x34]
00507A43  4D 8D 52 02                     lea r10, [r10 + 2]
00507A47  83 FF FF                        cmp edi, -1
00507A4A  74 05                           je 0x140507a51
00507A4C  45 85 C9                        test r9d, r9d
00507A4F  7F DD                           jg 0x140507a2e
00507A51  B9 20 00 00 00                  mov ecx, 0x20
00507A56  85 FF                           test edi, edi
00507A58  0F 88 29 02 00 00               js 0x140507c87
00507A5E  41 F6 C6 04                     test r14b, 4
00507A62  EB 14                           jmp 0x140507a78
00507A64  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00507A69  41 FF CF                        dec r15d
00507A6C  E8 87 02 00 00                  call 0x140507cf8
00507A71  8B 7C 24 34                     mov edi, dword ptr [rsp + 0x34]
00507A75  83 FF FF                        cmp edi, -1
00507A78  0F 84 09 02 00 00               je 0x140507c87
00507A7E  45 85 FF                        test r15d, r15d
00507A81  7F E1                           jg 0x140507a64
00507A83  E9 FF 01 00 00                  jmp 0x140507c87
00507A88  BA 49 00 00 00                  mov edx, 0x49
00507A8D  3B CA                           cmp ecx, edx
00507A8F  74 26                           je 0x140507ab7
00507A91  83 F9 68                        cmp ecx, 0x68
00507A94  74 7A                           je 0x140507b10
00507A96  8D 42 21                        lea eax, [rdx + 0x21]
00507A99  3B C8                           cmp ecx, eax
00507A9B  74 1F                           je 0x140507abc
00507A9D  8D 42 23                        lea eax, [rdx + 0x23]
00507AA0  3B C8                           cmp ecx, eax
00507AA2  74 49                           je 0x140507aed
00507AA4  83 F9 74                        cmp ecx, 0x74
00507AA7  74 0E                           je 0x140507ab7
00507AA9  83 F9 77                        cmp ecx, 0x77
00507AAC  74 35                           je 0x140507ae3
00507AAE  83 F9 7A                        cmp ecx, 0x7a
00507AB1  0F 85 C4 01 00 00               jne 0x140507c7b
00507AB7  B8 6A 00 00 00                  mov eax, 0x6a
00507ABC  41 0F BA EE 0F                  bts r14d, 0xf
00507AC1  66 44 3B CA                     cmp r9w, dx
00507AC5  75 72                           jne 0x140507b39
00507AC7  41 0F B7 45 00                  movzx eax, word ptr [r13]
00507ACC  66 83 F8 36                     cmp ax, 0x36
00507AD0  75 4B                           jne 0x140507b1d
00507AD2  66 41 83 7D 02 34               cmp word ptr [r13 + 2], 0x34
00507AD8  75 69                           jne 0x140507b43
00507ADA  49 83 C5 04                     add r13, 4
00507ADE  E9 98 01 00 00                  jmp 0x140507c7b
00507AE3  41 0F BA EE 0B                  bts r14d, 0xb
00507AE8  E9 8E 01 00 00                  jmp 0x140507c7b
00507AED  B9 20 00 00 00                  mov ecx, 0x20
00507AF2  66 41 39 45 00                  cmp word ptr [r13], ax
00507AF7  75 0E                           jne 0x140507b07
00507AF9  49 83 C5 02                     add r13, 2
00507AFD  41 0F BA EE 0C                  bts r14d, 0xc
00507B02  E9 85 01 00 00                  jmp 0x140507c8c
00507B07  41 83 CE 10                     or r14d, 0x10
00507B0B  E9 7C 01 00 00                  jmp 0x140507c8c
00507B10  B9 20 00 00 00                  mov ecx, 0x20
00507B15  44 0B F1                        or r14d, ecx
00507B18  E9 6F 01 00 00                  jmp 0x140507c8c
00507B1D  66 83 F8 33                     cmp ax, 0x33
00507B21  75 20                           jne 0x140507b43
00507B23  66 41 83 7D 02 32               cmp word ptr [r13 + 2], 0x32
00507B29  75 18                           jne 0x140507b43
00507B2B  49 83 C5 04                     add r13, 4
00507B2F  41 0F BA F6 0F                  btr r14d, 0xf
00507B34  E9 42 01 00 00                  jmp 0x140507c7b
00507B39  66 44 3B C8                     cmp r9w, ax
00507B3D  0F 84 38 01 00 00               je 0x140507c7b
00507B43  41 0F B7 45 00                  movzx eax, word ptr [r13]
00507B48  BA 20 00 00 00                  mov edx, 0x20
00507B4D  66 83 E8 58                     sub ax, 0x58
00507B51  66 3B C2                        cmp ax, dx
00507B54  77 14                           ja 0x140507b6a
00507B56  48 B9 01 10 82 20 01 00 00 00   movabs rcx, 0x120821001
00507B60  48 0F A3 C1                     bt rcx, rax
00507B64  0F 82 EF 00 00 00               jb 0x140507c59
00507B6A  45 8B D3                        mov r10d, r11d
00507B6D  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
00507B72  4C 8D 44 24 34                  lea r8, [rsp + 0x34]
00507B77  41 0F B7 C9                     movzx ecx, r9w
00507B7B  C7 44 24 44 01 00 00 00         mov dword ptr [rsp + 0x44], 1
00507B83  E8 70 01 00 00                  call 0x140507cf8
00507B88  8B 7C 24 34                     mov edi, dword ptr [rsp + 0x34]
00507B8C  E9 EA 00 00 00                  jmp 0x140507c7b
00507B91  66 41 83 F9 2A                  cmp r9w, 0x2a
00507B96  75 29                           jne 0x140507bc1
00507B98  41 8B 30                        mov esi, dword ptr [r8]
00507B9B  49 83 C7 08                     add r15, 8
00507B9F  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00507BA4  B9 20 00 00 00                  mov ecx, 0x20
00507BA9  89 74 24 3C                     mov dword ptr [rsp + 0x3c], esi
00507BAD  85 F6                           test esi, esi
00507BAF  0F 89 D7 00 00 00               jns 0x140507c8c
00507BB5  83 CE FF                        or esi, 0xffffffff
00507BB8  89 74 24 3C                     mov dword ptr [rsp + 0x3c], esi
00507BBC  E9 CB 00 00 00                  jmp 0x140507c8c
00507BC1  8D 34 B6                        lea esi, [rsi + rsi*4]
00507BC4  8D 76 E8                        lea esi, [rsi - 0x18]
00507BC7  8D 34 71                        lea esi, [rcx + rsi*2]
00507BCA  E9 A8 00 00 00                  jmp 0x140507c77
00507BCF  41 8B F3                        mov esi, r11d
00507BD2  44 89 5C 24 3C                  mov dword ptr [rsp + 0x3c], r11d
00507BD7  E9 9F 00 00 00                  jmp 0x140507c7b
00507BDC  66 41 83 F9 2A                  cmp r9w, 0x2a
00507BE1  75 21                           jne 0x140507c04
00507BE3  41 8B 10                        mov edx, dword ptr [r8]
00507BE6  49 83 C7 08                     add r15, 8
00507BEA  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
00507BEF  8B CA                           mov ecx, edx
00507BF1  85 D2                           test edx, edx
00507BF3  79 04                           jns 0x140507bf9
00507BF5  41 83 CE 04                     or r14d, 4
00507BF9  8B C2                           mov eax, edx
00507BFB  F7 DA                           neg edx
00507BFD  85 C0                           test eax, eax
00507BFF  0F 49 D1                        cmovns edx, ecx
00507C02  EB 0D                           jmp 0x140507c11
00507C04  8B 54 24 50                     mov edx, dword ptr [rsp + 0x50]
00507C08  8D 14 92                        lea edx, [rdx + rdx*4]
00507C0B  8D 52 E8                        lea edx, [rdx - 0x18]
00507C0E  8D 14 51                        lea edx, [rcx + rdx*2]
00507C11  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
00507C15  EB 64                           jmp 0x140507c7b
00507C17  BA 20 00 00 00                  mov edx, 0x20
00507C1C  3B CA                           cmp ecx, edx
00507C1E  74 35                           je 0x140507c55
00507C20  83 F9 23                        cmp ecx, 0x23
00507C23  74 29                           je 0x140507c4e
00507C25  8D 42 0B                        lea eax, [rdx + 0xb]
00507C28  3B C8                           cmp ecx, eax
00507C2A  74 1C                           je 0x140507c48
00507C2C  8D 42 0D                        lea eax, [rdx + 0xd]
00507C2F  3B C8                           cmp ecx, eax
00507C31  74 0F                           je 0x140507c42
00507C33  8D 42 10                        lea eax, [rdx + 0x10]
00507C36  3B C8                           cmp ecx, eax
00507C38  8B CA                           mov ecx, edx
00507C3A  75 50                           jne 0x140507c8c
00507C3C  41 83 CE 08                     or r14d, 8
00507C40  EB 4A                           jmp 0x140507c8c
00507C42  41 83 CE 04                     or r14d, 4
00507C46  EB 11                           jmp 0x140507c59
00507C48  41 83 CE 01                     or r14d, 1
00507C4C  EB 0B                           jmp 0x140507c59
00507C4E  41 0F BA EE 07                  bts r14d, 7
00507C53  EB 04                           jmp 0x140507c59
00507C55  41 83 CE 02                     or r14d, 2
00507C59  8B CA                           mov ecx, edx
00507C5B  EB 2F                           jmp 0x140507c8c
00507C5D  44 89 5C 24 64                  mov dword ptr [rsp + 0x64], r11d
00507C62  45 8B F3                        mov r14d, r11d
00507C65  44 89 5C 24 50                  mov dword ptr [rsp + 0x50], r11d
00507C6A  83 CE FF                        or esi, 0xffffffff
00507C6D  44 89 5C 24 38                  mov dword ptr [rsp + 0x38], r11d
00507C72  44 89 5C 24 44                  mov dword ptr [rsp + 0x44], r11d
00507C77  89 74 24 3C                     mov dword ptr [rsp + 0x3c], esi
00507C7B  B9 20 00 00 00                  mov ecx, 0x20
00507C80  EB 0A                           jmp 0x140507c8c
00507C82  B9 20 00 00 00                  mov ecx, 0x20
00507C87  44 8B 54 24 30                  mov r10d, dword ptr [rsp + 0x30]
00507C8C  45 0F B7 4D 00                  movzx r9d, word ptr [r13]
00507C91  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00507C96  66 45 85 C9                     test r9w, r9w
00507C9A  0F 85 BD F7 FF FF               jne 0x14050745d
00507CA0  45 85 D2                        test r10d, r10d
00507CA3  74 06                           je 0x140507cab
00507CA5  41 83 FA 07                     cmp r10d, 7
00507CA9  75 04                           jne 0x140507caf
00507CAB  8B C7                           mov eax, edi
00507CAD  EB 17                           jmp 0x140507cc6
00507CAF  45 33 C9                        xor r9d, r9d
00507CB2  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
00507CB7  45 33 C0                        xor r8d, r8d
00507CBA  33 D2                           xor edx, edx
00507CBC  33 C9                           xor ecx, ecx
00507CBE  E8 8D 68 F9 FF                  call 0x14049e550
00507CC3  83 C8 FF                        or eax, 0xffffffff
00507CC6  48 8B 8D 80 03 00 00            mov rcx, qword ptr [rbp + 0x380]
00507CCD  48 33 CC                        xor rcx, rsp
00507CD0  E8 6B 49 1A 00                  call 0x1406ac640
00507CD5  48 8B 9C 24 D8 04 00 00         mov rbx, qword ptr [rsp + 0x4d8]
00507CDD  48 81 C4 90 04 00 00            add rsp, 0x490
00507CE4  41 5F                           pop r15
00507CE6  41 5E                           pop r14
00507CE8  41 5D                           pop r13
00507CEA  41 5C                           pop r12
00507CEC  5F                              pop rdi
00507CED  5E                              pop rsi
00507CEE  5D                              pop rbp
00507CEF  C3                              ret
00507CF0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall woutput_s(__int64 a1, __int64 a2, __int64 a3)
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
    unsigned __int64 v_stack_m3C8;
    unsigned __int64 v_stack_m448;
    unsigned __int64 v_stack_m460;
    unsigned int v_stack_m464;
    unsigned int v_stack_m468;
    unsigned __int64 v_stack_m470;
    unsigned int v_stack_m478;
    unsigned __int16 v_stack_m47A;
    unsigned __int16 v_stack_m47C;
    unsigned __int8 v_stack_m47F;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m480;
    unsigned int v_stack_m484;
    unsigned __int16 v_stack_m488;
    unsigned int v_stack_m48C;
    unsigned int v_stack_m490;
    unsigned int v_stack_m494;
    unsigned int v_stack_m498;
    unsigned __int64 v_stack_m4A8;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (0x490ULL);
    result = (*(unsigned __int64 *)(v_rip + 9450350)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m460 = a1;
    a1 = 0;
    v_stack_m470 = a3;
    v_stack_m468 = 0;
    v_stack_m478 = 0;
    v_stack_m48C = 0;
    v_stack_m490 = 0;
    v_stack_m464 = 0;
    a2 = 0;
    result = memset(v_stack_m448, a2, (unsigned int)(0x400ULL), a4);
    v_r11 = 0;
    v_stack_m488 = 0;
    v_stack_m484 = 0;
    if (0 == 0) goto loc_00507CAF;
    if (0 == 0) goto loc_00507CAF;
    v_stack_m494 = 0;
    if ((unsigned __int16)(*(unsigned __int16 *)(a2)) == 0) goto loc_00507CAB;
loc_0050745D:
    v_r13 = (a2) + (2);
    if (sign_flag) goto loc_00507CA0;
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a2))) - ((unsigned __int16)(0 + 32)));
    if (((unsigned __int16)(result)) > 90) goto loc_0050748E;
    a2 = (unsigned int)((*(unsigned __int8 *)((unsigned __int16)(*(unsigned __int16 *)(a2)) + v_rip - 5143636 * 1 - 32)) & (15));
    goto loc_00507491;
loc_0050748E:
loc_00507491:
    result = (unsigned int)((0 + 0 * 8) + (0));
    v_r10 = (unsigned int)((*(unsigned __int8 *)(result + v_rip - 5143666 * 1)) >> (4));
    v_stack_m498 = (unsigned int)(v_r10);
    if (((unsigned int)(v_r10)) == 8) goto loc_00507CAF;
    if ((unsigned int)(v_r10) == 0) goto loc_00507B6D;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) - (1));
    if (condition_is_equal) goto loc_00507C5D;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00507C17;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00507BDC;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00507BCF;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00507B91;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00507A88;
    if (((unsigned int)(a2)) != 1) goto loc_00507C7B;
    if (((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(a2)))) > 105) goto loc_005076E1;
    if (((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(a2)))) == 105) goto loc_00507541;
    a1 = (unsigned int)(((unsigned __int16)(*(unsigned __int16 *)(a2))) - (67));
    if (condition_is_equal) goto loc_00507668;
    a1 = (unsigned int)((a1) - (16));
    if (condition_is_equal) goto loc_005075FA;
    a1 = (unsigned int)((a1) - (5));
    if (condition_is_equal) goto loc_0050775B;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_0050757D;
    a1 = (unsigned int)((a1) - (9));
    if (condition_is_equal) goto loc_0050767B;
    if (((unsigned int)(a1)) != ((unsigned int)(a2))) goto loc_00507883;
loc_00507541:
    v_r14 = (unsigned int)((0) | (64));
loc_00507545:
loc_0050754B:
loc_00507550:
    v_r15 = (a3) + (8);
    v_stack_m470 = v_r15;
    if (condition_is_below) goto loc_0050756B;
    if (condition_is_above_or_equal) goto loc_005077AD;
loc_0050756B:
    if ((((unsigned __int8)(v_r14)) & (64)) == 0) goto loc_005077E6;
    goto loc_005077D4;
loc_0050757D:
    v_r15 = (v_r15) + (8);
    v_stack_m470 = v_r15;
    if (*(unsigned __int64 *)(a3) == 0) goto loc_005075DE;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3) + 8) == 0) goto loc_005075DE;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a3) + 2)) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a3))))) goto loc_00507CAF;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a3) + 2)) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a3))))) goto loc_005075D4;
    result = (unsigned int)(~(*(unsigned __int16 *)(*(unsigned __int64 *)(a3))));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_00507CAF;
    result = (unsigned int)(~((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) + 8)))));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_00507CAF;
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a3))))) >> (1));
    v_stack_m484 = 1;
    goto loc_00507883;
loc_005075D4:
    v_stack_m484 = 0;
    goto loc_00507883;
loc_005075DE:
    v_r12 = (v_r12) | (-1);
loc_005075EC:
    v_r12 = (v_r12) + 1;
    if ((*(unsigned __int8 *)(v_rip - 5146189 + v_r12 * 1)) != 0) goto loc_005075EC;
    goto loc_00507883;
loc_005075FA:
    if ((((unsigned int)(v_r14)) & (0x830ULL)) == 0) {
        v_r14 = (unsigned int)((v_r14) | (32));
    }
    a1 = 0;
    if (0 == -1) { a1 = (unsigned int)((unsigned int)(0x7FFFFFFFULL)); }
    v_r15 = (v_r15) + (8);
    v_stack_m470 = v_r15;
    if (((32) & ((unsigned __int8)(v_r14))) == 0) goto loc_00507718;
    result = *(unsigned __int64 *)(a3);
    v_rbx = *(unsigned __int64 *)(a3);
    if (*(unsigned __int64 *)(a3) == 0) {
        a2 = v_rip - 5146278;
        v_rbx = a2;
        result = a2;
    }
    if (condition_is_less_or_equal) goto loc_00507889;
loc_0050764F:
    if ((*(unsigned __int8 *)(result)) == 0) goto loc_00507889;
    result = (result) + 1;
    v_r12 = (unsigned int)((0) + 1);
    if (((unsigned int)(v_r12)) < ((unsigned int)(a1))) goto loc_0050764F;
    goto loc_00507889;
loc_00507668:
    if ((((unsigned int)(v_r14)) & (0x830ULL)) != 0) goto loc_00507680;
    v_r14 = (unsigned int)((v_r14) | (32));
    goto loc_00507680;
loc_0050767B:
loc_00507680:
    v_r15 = (v_r15) + (8);
    v_stack_m484 = 1;
    v_stack_m470 = v_r15;
    v_stack_m488 = (unsigned __int16)(*(unsigned __int16 *)(32));
    if (((32) & ((unsigned __int8)(v_r14))) == 0) goto loc_005076CE;
    v_stack_m480 = (unsigned __int8)(*(unsigned __int16 *)(32));
    v_stack_m47F = 0;
    result = mbtowc(v_stack_m448, v_stack_m480, (int)(*(unsigned int *)(v_rip + 9449562)), 10);
    v_r11 = 0;
    if (!sign_flag) goto loc_005076D2;
    v_stack_m464 = 1;
    goto loc_005076D2;
loc_005076CE:
    v_stack_m448 = (unsigned __int16)(result);
loc_005076D2:
    goto loc_00507883;
loc_005076E1:
    a1 = (unsigned int)((v_stack_m448) - (110));
    if (condition_is_equal) goto loc_00507CAF;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0050778F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00507751;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00507607;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00507545;
    if (((unsigned int)(a1)) != 3) goto loc_00507883;
    goto loc_00507760;
loc_00507718:
    v_stack_m484 = 1;
    result = v_rip - 5097522;
    if (v_stack_m448 != 0) { result = v_stack_m448; }
    goto loc_0050773F;
loc_00507733:
    a1 = (unsigned int)((a1) - 1);
    if ((*(unsigned __int16 *)(result)) == 0) goto loc_00507743;
    result = (result) + (2);
loc_0050773F:
    if ((unsigned int)(a1) != 0) goto loc_00507733;
loc_00507743:
    result = (result) - (result);
    result = (result) >> (1);
    goto loc_00507889;
loc_00507751:
loc_0050775B:
loc_00507760:
    v_stack_m468 = 7;
    result = 7;
    if (sign_flag) {
        a1 = 48;
        v_stack_m490 = 2;
        result = (unsigned __int16)((7) + (81));
        v_stack_m47C = (unsigned __int16)(a1);
        v_stack_m47A = (unsigned __int16)(result);
    }
    goto loc_0050754B;
loc_0050778F:
    if (!sign_flag) goto loc_0050754B;
    v_r14 = (unsigned int)((v_r14) | (512));
    goto loc_00507550;
loc_005077AD:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (64));
    if (((32) & ((unsigned __int8)(v_r14))) == 0) goto loc_005077CD;
    if ((unsigned int)(result) == 0) goto loc_005077C7;
    goto loc_005077D4;
loc_005077C7:
    goto loc_005077E6;
loc_005077CD:
    if ((unsigned int)(*(unsigned __int16 *)((int)(*(unsigned int *)(v_rip + 9449562)))) == 0) goto loc_005077E3;
loc_005077D4:
    if (!sign_flag) goto loc_005077E6;
    result = -((int)(*(unsigned int *)((int)(*(unsigned int *)(v_rip + 9449562)))));
    goto loc_005077E6;
loc_005077E3:
loc_005077E6:
    a3 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((int)(*(unsigned int *)(v_rip + 9449562))))));
    if ((((unsigned int)(v_r14)) & (0x9000ULL)) != 0) { a3 = (unsigned int)(*(unsigned int *)((int)(*(unsigned int *)(v_rip + 9449562)))); }
    if (!sign_flag) goto loc_005077FF;
    goto loc_00507808;
loc_005077FF:
    v_r14 = (unsigned int)((v_r14) & (0xFFFFFFF7ULL));
    v_rsi = 1;
    if (1 > 512) { v_rsi = 512; }
loc_00507808:
    result = -(a3);
loc_00507820:
    v_rsi = (unsigned int)((v_rsi) - 1);
    if (condition_is_greater) goto loc_0050782D;
    if (a3 == 0) goto loc_0050784A;
loc_0050782D:
    a2 = 0;
    a2 = (unsigned int)((a2) + (48));
    if (((unsigned int)(a2)) >= = 57) {
        a2 = (unsigned int)((a2) + ((unsigned int)((unsigned int)(v_stack_m468))));
    }
    *(unsigned __int8 *)(v_stack_m249) = (unsigned __int8)(a2);
    a1 = (v_stack_m249) - 1;
    goto loc_00507820;
loc_0050784A:
    v_stack_m48C = (unsigned int)(v_rsi);
    v_r12 = (unsigned int)((v_stack_m249) - ((unsigned int)(a1)));
    if (condition_is_above_or_equal) goto loc_00507883;
    if ((unsigned int)(v_r12) == 0) goto loc_00507876;
    v_stack_m470 = v_r15;
    v_rbx = a1 + 1;
    if ((*(unsigned __int8 *)(a1 + 1)) != 48) {
        v_rbx = (a1 + 1) - 1;
        v_stack_m470 = v_r15;
        v_r12 = (unsigned int)((v_r12) + 1);
        *(unsigned __int8 *)(v_rbx) = 48;
    }
loc_00507889:
    if (v_stack_m464 != 0) goto loc_00507C82;
    if ((((unsigned __int8)(v_r14)) & (64)) == 0) goto loc_005078D1;
    if (condition_is_above_or_equal) goto loc_005078A8;
    goto loc_005078B3;
loc_005078A8:
    if ((((unsigned __int8)(v_r14)) & (1)) == 0) goto loc_005078C3;
loc_005078B3:
    v_stack_m47C = 43;
loc_005078B8:
    v_stack_m490 = 1;
    goto loc_005078D5;
loc_005078C3:
    if ((((unsigned __int8)(v_r14)) & (2)) == 0) goto loc_005078D1;
    v_stack_m47C = 32;
    goto loc_005078B8;
loc_005078D1:
loc_005078D5:
    v_r15 = (unsigned int)(((unsigned int)(v_stack_m478)) - ((unsigned int)(v_r12)));
    v_r15 = (unsigned int)((v_r15) - ((unsigned int)((unsigned int)(v_stack_m490))));
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (12));
    if (condition_is_not_equal) goto loc_00507920;
    if (condition_is_less_or_equal) goto loc_00507920;
loc_005078FB:
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) - 1);
    result = write_char(32, v_stack_m460, v_stack_m494, a4);
    if (((unsigned int)((unsigned int)(v_stack_m494))) == -1) goto loc_00507918;
    if (condition_is_greater) goto loc_005078FB;
loc_00507918:
loc_00507920:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m460 + 24)))) & (64)) == 0) goto loc_0050793E;
    if ((*(unsigned __int64 *)(v_stack_m460 + 16)) != 0) goto loc_0050793E;
    v_rdi = (unsigned int)(((unsigned int)(v_stack_m494)) + ((unsigned int)((unsigned int)(v_stack_m490))));
    v_stack_m494 = (unsigned int)(v_rdi);
    goto loc_00507965;
loc_0050793E:
    if (condition_is_less_or_equal) goto loc_00507965;
loc_00507942:
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m490)))) - 1);
    result = write_char(*(unsigned __int16 *)(v_stack_m47C), v_stack_m460, v_stack_m494, a4);
    if (((unsigned int)((unsigned int)(v_stack_m494))) == -1) goto loc_00507965;
    if (condition_is_greater) goto loc_00507942;
loc_00507965:
    if (((unsigned int)(v_r11)) != 8) goto loc_0050799D;
    v_r11 = 0;
    if (condition_is_less_or_equal) goto loc_005079A0;
loc_0050797A:
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) - 1);
    result = write_char((unsigned int)((unsigned int)(v_r11 + 48)), v_stack_m460, v_stack_m494, a4);
    if (((unsigned int)((unsigned int)(v_stack_m494))) == -1) goto loc_00507997;
    if (condition_is_greater) goto loc_0050797A;
loc_00507997:
    goto loc_005079A0;
loc_0050799D:
    v_r11 = 0;
loc_005079A0:
    if (v_stack_m484 != 0) goto loc_00507A0D;
    if (condition_is_less_or_equal) goto loc_00507A0D;
loc_005079B2:
    result = mbtowc(v_stack_m488, v_rbx, (int)(*(unsigned int *)(v_rip + 9448775)), a4);
    v_r11 = 0;
    result = (((unsigned int)((int)((unsigned int)(result)))) == 2) ? 1 : 0;
    result = (unsigned int)((result) + 1);
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) - ((unsigned int)(result)));
    if (condition_is_less_or_equal) goto loc_00507A00;
    result = write_char(v_stack_m488, v_stack_m460, v_stack_m494, (int)((unsigned int)(result)));
    v_rsi = (v_rbx) + ((int)((unsigned int)(result)));
    if (condition_is_greater) goto loc_005079B2;
    goto loc_00507A07;
loc_00507A00:
    v_rdi = (unsigned int)(((unsigned int)(v_stack_m494)) | (0xFFFFFFFFULL));
    v_stack_m494 = (unsigned int)(v_rdi);
loc_00507A07:
    goto loc_00507A51;
loc_00507A0D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m460 + 24)))) & (64)) == 0) goto loc_00507A29;
    if ((*(unsigned __int64 *)(v_stack_m460 + 16)) != 0) goto loc_00507A29;
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_r12)));
    v_stack_m494 = (unsigned int)(v_rdi);
    goto loc_00507A51;
loc_00507A29:
    if (condition_is_less_or_equal) goto loc_00507A51;
loc_00507A2E:
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) - 1);
    result = write_char(*(unsigned __int16 *)(v_rbx), v_stack_m460, v_stack_m494, a4);
    if (((unsigned int)((unsigned int)(v_stack_m494))) == -1) goto loc_00507A51;
    if (condition_is_greater) goto loc_00507A2E;
loc_00507A51:
    if (sign_flag) goto loc_00507C87;
    goto loc_00507A78;
loc_00507A64:
    v_r15 = (unsigned int)((v_r15) - 1);
    result = write_char(32, v_stack_m460, v_stack_m494, a4);
loc_00507A78:
    if (((unsigned int)((unsigned int)(v_stack_m494))) == -1) goto loc_00507C87;
    if (condition_is_greater) goto loc_00507A64;
    goto loc_00507C87;
loc_00507A88:
    if (32 == 73) goto loc_00507AB7;
    if (32 == 104) goto loc_00507B10;
    if (32 == ((unsigned int)(73 + 33))) goto loc_00507ABC;
    if (32 == ((unsigned int)(73 + 35))) goto loc_00507AED;
    if (32 == 116) goto loc_00507AB7;
    if (32 == 119) goto loc_00507AE3;
    if (32 != 122) goto loc_00507C7B;
loc_00507AB7:
loc_00507ABC:
    if (((unsigned __int16)(a4)) != 73) goto loc_00507B39;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r13))) != 54) goto loc_00507B1D;
    if ((*(unsigned __int16 *)(v_r13 + 2)) != 52) goto loc_00507B43;
    v_r13 = (v_r13) + (4);
    goto loc_00507C7B;
loc_00507AE3:
    goto loc_00507C7B;
loc_00507AED:
    if ((*(unsigned __int16 *)(v_r13)) != ((unsigned __int16)(*(unsigned __int16 *)(v_r13)))) goto loc_00507B07;
    v_r13 = (v_r13) + (2);
    goto loc_00507C8C;
loc_00507B07:
    v_r14 = (unsigned int)((v_r14) | (16));
    goto loc_00507C8C;
loc_00507B10:
    v_r14 = (unsigned int)((v_r14) | (32));
    goto loc_00507C8C;
loc_00507B1D:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r13))) != 51) goto loc_00507B43;
    if ((*(unsigned __int16 *)(v_r13 + 2)) != 50) goto loc_00507B43;
    v_r13 = (v_r13) + (4);
    goto loc_00507C7B;
loc_00507B39:
    if (((unsigned __int16)(a4)) == ((unsigned __int16)(*(unsigned __int16 *)(v_r13)))) goto loc_00507C7B;
loc_00507B43:
    result = (unsigned __int16)((*(unsigned __int16 *)(v_r13)) - (88));
    if (((unsigned __int16)(result)) > 32) goto loc_00507B6A;
    if (((unsigned __int16)(result)) < 32) goto loc_00507C59;
loc_00507B6A:
loc_00507B6D:
    v_stack_m484 = 1;
    result = write_char((unsigned __int16)(a4), v_stack_m460, v_stack_m494, a4);
    goto loc_00507C7B;
loc_00507B91:
    if (((unsigned __int16)(a4)) != 42) goto loc_00507BC1;
    v_r15 = (v_r15) + (8);
    v_stack_m470 = v_r15;
    v_stack_m48C = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m494)));
    if (!sign_flag) goto loc_00507C8C;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m494))) | (0xFFFFFFFFULL));
    v_stack_m48C = (unsigned int)(v_rsi);
    goto loc_00507C8C;
loc_00507BC1:
    goto loc_00507C77;
loc_00507BCF:
    v_stack_m48C = 0;
    goto loc_00507C7B;
loc_00507BDC:
    if (((unsigned __int16)(a4)) != 42) goto loc_00507C04;
    v_r15 = (v_r15) + (8);
    v_stack_m470 = v_r15;
    if (sign_flag) {
        v_r14 = (unsigned int)((v_r14) | (4));
    }
    a2 = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_stack_m494))));
    if (!sign_flag) { a2 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m494))))); }
    goto loc_00507C11;
loc_00507C04:
loc_00507C11:
    v_stack_m478 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m494)))) + (unsigned int)(v_stack_m478) + (unsigned int)(v_stack_m478) * 4 - 24 * 2);
    goto loc_00507C7B;
loc_00507C17:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m494)))))) == 32) goto loc_00507C55;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m494)))))) == 35) goto loc_00507C4E;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m494)))))) == ((unsigned int)(32 + 11))) goto loc_00507C48;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m494)))))) == ((unsigned int)(32 + 13))) goto loc_00507C42;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m494)))))) != ((unsigned int)(32 + 16))) goto loc_00507C8C;
    v_r14 = (unsigned int)((v_r14) | (8));
    goto loc_00507C8C;
loc_00507C42:
    v_r14 = (unsigned int)((v_r14) | (4));
    goto loc_00507C59;
loc_00507C48:
    v_r14 = (unsigned int)((v_r14) | (1));
    goto loc_00507C59;
loc_00507C4E:
    goto loc_00507C59;
loc_00507C55:
    v_r14 = (unsigned int)((v_r14) | (2));
loc_00507C59:
    goto loc_00507C8C;
loc_00507C5D:
    v_stack_m464 = 0;
    v_stack_m478 = 0;
    v_rsi = (unsigned int)((0) | (0xFFFFFFFFULL));
    v_stack_m490 = 0;
    v_stack_m484 = 0;
loc_00507C77:
    v_stack_m48C = (unsigned int)(v_rsi);
loc_00507C7B:
    goto loc_00507C8C;
loc_00507C82:
loc_00507C87:
loc_00507C8C:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_r13)) != 0) goto loc_0050745D;
loc_00507CA0:
    if ((unsigned int)((unsigned int)(v_stack_m498)) == 0) goto loc_00507CAB;
    if (((unsigned int)((unsigned int)(v_stack_m498))) != 7) goto loc_00507CAF;
loc_00507CAB:
    goto loc_00507CC6;
loc_00507CAF:
    a4 = 0;
    v_stack_m4A8 = 0;
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = EmpCheckErrataList(a1, a2, a3, a4);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
loc_00507CC6:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (0x490ULL);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t woutput_s(int64_t Arg1, int64_t Arg2, int64_t Arg3)
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
    uint64_t v_stack_m3C8;
    uint64_t v_stack_m448;
    uint64_t v_stack_m460;
    uint32_t v_stack_m464;
    uint32_t v_stack_m468;
    uint64_t v_stack_m470;
    uint32_t v_stack_m478;
    uint16_t v_stack_m47A;
    uint16_t v_stack_m47C;
    uint8_t v_stack_m47F;
    uint64_t v_stack_m48;
    uint64_t v_stack_m480;
    uint32_t v_stack_m484;
    uint16_t v_stack_m488;
    uint32_t v_stack_m48C;
    uint32_t v_stack_m490;
    uint32_t v_stack_m494;
    uint32_t v_stack_m498;
    uint64_t v_stack_m4A8;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (0x490ULL);
    result = (*(uint64_t *)(v_rip + 0x90336E)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m460 = Arg1;
    Arg1 = 0;
    v_stack_m470 = Arg3;
    v_stack_m468 = 0;
    v_stack_m478 = 0;
    v_stack_m48C = 0;
    v_stack_m490 = 0;
    v_stack_m464 = 0;
    Arg2 = 0;
    result = memset(v_stack_m448, Arg2, (uint32_t)(0x400ULL), a4);
    local_r11 = 0;
    v_stack_m488 = 0;
    v_stack_m484 = 0;
    if (0 == 0) goto loc_00507CAF;
    if (0 == 0) goto loc_00507CAF;
    v_stack_m494 = 0;
    if ((uint16_t)(*(uint16_t *)(Arg2)) == 0) goto loc_00507CAB;
loc_0050745D:
    local_r13 = (Arg2) + (2);
    if (sign_flag) goto loc_00507CA0;
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(Arg2))) - ((uint16_t)(0 + 32)));
    if (((uint16_t)(result)) > 90) goto loc_0050748E;
    Arg2 = (uint32_t)((*(uint8_t *)((uint16_t)(*(uint16_t *)(Arg2)) + v_rip - 0x4E7C54 * 1 - 0x20)) & (15));
    goto loc_00507491;
loc_0050748E:
loc_00507491:
    result = (uint32_t)((0 + 0 * 8) + (0));
    local_r10 = (uint32_t)((*(uint8_t *)(result + v_rip - 0x4E7C72 * 1)) >> (4));
    v_stack_m498 = (uint32_t)(local_r10);
    if (((uint32_t)(local_r10)) == 8) goto loc_00507CAF;
    if ((uint32_t)(local_r10) == 0) goto loc_00507B6D;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) - (1));
    if (condition_is_equal) goto loc_00507C5D;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00507C17;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00507BDC;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00507BCF;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00507B91;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00507A88;
    if (((uint32_t)(Arg2)) != 1) goto loc_00507C7B;
    if (((uint32_t)((uint16_t)(*(uint16_t *)(Arg2)))) > 105) goto loc_005076E1;
    if (((uint32_t)((uint16_t)(*(uint16_t *)(Arg2)))) == 105) goto loc_00507541;
    Arg1 = (uint32_t)(((uint16_t)(*(uint16_t *)(Arg2))) - (67));
    if (condition_is_equal) goto loc_00507668;
    Arg1 = (uint32_t)((Arg1) - (16));
    if (condition_is_equal) goto loc_005075FA;
    Arg1 = (uint32_t)((Arg1) - (5));
    if (condition_is_equal) goto loc_0050775B;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_0050757D;
    Arg1 = (uint32_t)((Arg1) - (9));
    if (condition_is_equal) goto loc_0050767B;
    if (((uint32_t)(Arg1)) != ((uint32_t)(Arg2))) goto loc_00507883;
loc_00507541:
    local_r14 = (uint32_t)((0) | (64));
loc_00507545:
loc_0050754B:
loc_00507550:
    local_r15 = (Arg3) + (8);
    v_stack_m470 = local_r15;
    if (condition_is_below) goto loc_0050756B;
    if (condition_is_above_or_equal) goto loc_005077AD;
loc_0050756B:
    if ((((uint8_t)(local_r14)) & (64)) == 0) goto loc_005077E6;
    goto loc_005077D4;
loc_0050757D:
    local_r15 = (local_r15) + (8);
    v_stack_m470 = local_r15;
    if (*(uint64_t *)(Arg3) == 0) goto loc_005075DE;
    if (*(uint64_t *)(*(uint64_t *)(Arg3) + 0x8) == 0) goto loc_005075DE;
    if ((*(uint16_t *)(*(uint64_t *)(Arg3) + 0x2)) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg3))))) goto loc_00507CAF;
    if ((*(uint16_t *)(*(uint64_t *)(Arg3) + 0x2)) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg3))))) goto loc_005075D4;
    result = (uint32_t)(~(*(uint16_t *)(*(uint64_t *)(Arg3))));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_00507CAF;
    result = (uint32_t)(~((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(Arg3) + 0x8)))));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_00507CAF;
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(Arg3))))) >> (1));
    v_stack_m484 = 1;
    goto loc_00507883;
loc_005075D4:
    v_stack_m484 = 0;
    goto loc_00507883;
loc_005075DE:
    local_r12 = (local_r12) | (-1);
loc_005075EC:
    local_r12 = (local_r12) + 1;
    if ((*(uint8_t *)(v_rip - 0x4E864D + local_r12 * 1)) != 0) goto loc_005075EC;
    goto loc_00507883;
loc_005075FA:
    if ((((uint32_t)(local_r14)) & (0x830ULL)) == 0) {
        local_r14 = (uint32_t)((local_r14) | (32));
    }
    Arg1 = 0;
    if (0 == -1) { Arg1 = (uint32_t)((uint32_t)(0x7FFFFFFFULL)); }
    local_r15 = (local_r15) + (8);
    v_stack_m470 = local_r15;
    if (((32) & ((uint8_t)(local_r14))) == 0) goto loc_00507718;
    result = *(uint64_t *)(Arg3);
    local_rbx = *(uint64_t *)(Arg3);
    if (*(uint64_t *)(Arg3) == 0) {
        Arg2 = v_rip - 5146278;
        local_rbx = Arg2;
        result = Arg2;
    }
    if (condition_is_less_or_equal) goto loc_00507889;
loc_0050764F:
    if ((*(uint8_t *)(result)) == 0) goto loc_00507889;
    result = (result) + 1;
    local_r12 = (uint32_t)((0) + 1);
    if (((uint32_t)(local_r12)) < ((uint32_t)(Arg1))) goto loc_0050764F;
    goto loc_00507889;
loc_00507668:
    if ((((uint32_t)(local_r14)) & (0x830ULL)) != 0) goto loc_00507680;
    local_r14 = (uint32_t)((local_r14) | (32));
    goto loc_00507680;
loc_0050767B:
loc_00507680:
    local_r15 = (local_r15) + (8);
    v_stack_m484 = 1;
    v_stack_m470 = local_r15;
    v_stack_m488 = (uint16_t)(*(uint16_t *)(32));
    if (((32) & ((uint8_t)(local_r14))) == 0) goto loc_005076CE;
    v_stack_m480 = (uint8_t)(*(uint16_t *)(32));
    v_stack_m47F = 0;
    result = mbtowc(v_stack_m448, v_stack_m480, (int32_t)(*(uint32_t *)(v_rip + 0x90305A)), 10);
    local_r11 = 0;
    if (!sign_flag) goto loc_005076D2;
    v_stack_m464 = 1;
    goto loc_005076D2;
loc_005076CE:
    v_stack_m448 = (uint16_t)(result);
loc_005076D2:
    goto loc_00507883;
loc_005076E1:
    Arg1 = (uint32_t)((v_stack_m448) - (110));
    if (condition_is_equal) goto loc_00507CAF;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0050778F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00507751;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00507607;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00507545;
    if (((uint32_t)(Arg1)) != 3) goto loc_00507883;
    goto loc_00507760;
loc_00507718:
    v_stack_m484 = 1;
    result = v_rip - 5097522;
    if (v_stack_m448 != 0) { result = v_stack_m448; }
    goto loc_0050773F;
loc_00507733:
    Arg1 = (uint32_t)((Arg1) - 1);
    if ((*(uint16_t *)(result)) == 0) goto loc_00507743;
    result = (result) + (2);
loc_0050773F:
    if ((uint32_t)(Arg1) != 0) goto loc_00507733;
loc_00507743:
    result = (result) - (result);
    result = (result) >> (1);
    goto loc_00507889;
loc_00507751:
loc_0050775B:
loc_00507760:
    v_stack_m468 = 7;
    result = 7;
    if (sign_flag) {
        Arg1 = 48;
        v_stack_m490 = 2;
        result = (uint16_t)((7) + (81));
        v_stack_m47C = (uint16_t)(Arg1);
        v_stack_m47A = (uint16_t)(result);
    }
    goto loc_0050754B;
loc_0050778F:
    if (!sign_flag) goto loc_0050754B;
    local_r14 = (uint32_t)((local_r14) | (512));
    goto loc_00507550;
loc_005077AD:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (64));
    if (((32) & ((uint8_t)(local_r14))) == 0) goto loc_005077CD;
    if ((uint32_t)(result) == 0) goto loc_005077C7;
    goto loc_005077D4;
loc_005077C7:
    goto loc_005077E6;
loc_005077CD:
    if ((uint32_t)(*(uint16_t *)((int32_t)(*(uint32_t *)(v_rip + 0x90305A)))) == 0) goto loc_005077E3;
loc_005077D4:
    if (!sign_flag) goto loc_005077E6;
    result = -((int32_t)(*(uint32_t *)((int32_t)(*(uint32_t *)(v_rip + 0x90305A)))));
    goto loc_005077E6;
loc_005077E3:
loc_005077E6:
    Arg3 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((int32_t)(*(uint32_t *)(v_rip + 0x90305A))))));
    if ((((uint32_t)(local_r14)) & (0x9000ULL)) != 0) { Arg3 = (uint32_t)(*(uint32_t *)((int32_t)(*(uint32_t *)(v_rip + 0x90305A)))); }
    if (!sign_flag) goto loc_005077FF;
    goto loc_00507808;
loc_005077FF:
    local_r14 = (uint32_t)((local_r14) & (0xFFFFFFF7ULL));
    local_rsi = 1;
    if (1 > 512) { local_rsi = 512; }
loc_00507808:
    result = -(Arg3);
loc_00507820:
    local_rsi = (uint32_t)((local_rsi) - 1);
    if (condition_is_greater) goto loc_0050782D;
    if (Arg3 == 0) goto loc_0050784A;
loc_0050782D:
    Arg2 = 0;
    Arg2 = (uint32_t)((Arg2) + (48));
    if (((uint32_t)(Arg2)) >= = 57) {
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)((uint32_t)(v_stack_m468))));
    }
    *(uint8_t *)(v_stack_m249) = (uint8_t)(Arg2);
    Arg1 = (v_stack_m249) - 1;
    goto loc_00507820;
loc_0050784A:
    v_stack_m48C = (uint32_t)(local_rsi);
    local_r12 = (uint32_t)((v_stack_m249) - ((uint32_t)(Arg1)));
    if (condition_is_above_or_equal) goto loc_00507883;
    if ((uint32_t)(local_r12) == 0) goto loc_00507876;
    v_stack_m470 = local_r15;
    local_rbx = Arg1 + 1;
    if ((*(uint8_t *)(Arg1 + 0x1)) != 48) {
        local_rbx = (Arg1 + 1) - 1;
        v_stack_m470 = local_r15;
        local_r12 = (uint32_t)((local_r12) + 1);
        *(uint8_t *)(local_rbx) = 48;
    }
loc_00507889:
    if (v_stack_m464 != 0) goto loc_00507C82;
    if ((((uint8_t)(local_r14)) & (64)) == 0) goto loc_005078D1;
    if (condition_is_above_or_equal) goto loc_005078A8;
    goto loc_005078B3;
loc_005078A8:
    if ((((uint8_t)(local_r14)) & (1)) == 0) goto loc_005078C3;
loc_005078B3:
    v_stack_m47C = 43;
loc_005078B8:
    v_stack_m490 = 1;
    goto loc_005078D5;
loc_005078C3:
    if ((((uint8_t)(local_r14)) & (2)) == 0) goto loc_005078D1;
    v_stack_m47C = 32;
    goto loc_005078B8;
loc_005078D1:
loc_005078D5:
    local_r15 = (uint32_t)(((uint32_t)(v_stack_m478)) - ((uint32_t)(local_r12)));
    local_r15 = (uint32_t)((local_r15) - ((uint32_t)((uint32_t)(v_stack_m490))));
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (12));
    if (condition_is_not_equal) goto loc_00507920;
    if (condition_is_less_or_equal) goto loc_00507920;
loc_005078FB:
    a4 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) - 1);
    result = write_char(32, v_stack_m460, v_stack_m494, a4);
    if (((uint32_t)((uint32_t)(v_stack_m494))) == -1) goto loc_00507918;
    if (condition_is_greater) goto loc_005078FB;
loc_00507918:
loc_00507920:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m460 + 0x18)))) & (64)) == 0) goto loc_0050793E;
    if ((*(uint64_t *)(v_stack_m460 + 0x10)) != 0) goto loc_0050793E;
    local_rdi = (uint32_t)(((uint32_t)(v_stack_m494)) + ((uint32_t)((uint32_t)(v_stack_m490))));
    v_stack_m494 = (uint32_t)(local_rdi);
    goto loc_00507965;
loc_0050793E:
    if (condition_is_less_or_equal) goto loc_00507965;
loc_00507942:
    a4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m490)))) - 1);
    result = write_char(*(uint16_t *)(v_stack_m47C), v_stack_m460, v_stack_m494, a4);
    if (((uint32_t)((uint32_t)(v_stack_m494))) == -1) goto loc_00507965;
    if (condition_is_greater) goto loc_00507942;
loc_00507965:
    if (((uint32_t)(local_r11)) != 8) goto loc_0050799D;
    local_r11 = 0;
    if (condition_is_less_or_equal) goto loc_005079A0;
loc_0050797A:
    a4 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) - 1);
    result = write_char((uint32_t)((uint32_t)(local_r11 + 48)), v_stack_m460, v_stack_m494, a4);
    if (((uint32_t)((uint32_t)(v_stack_m494))) == -1) goto loc_00507997;
    if (condition_is_greater) goto loc_0050797A;
loc_00507997:
    goto loc_005079A0;
loc_0050799D:
    local_r11 = 0;
loc_005079A0:
    if (v_stack_m484 != 0) goto loc_00507A0D;
    if (condition_is_less_or_equal) goto loc_00507A0D;
loc_005079B2:
    result = mbtowc(v_stack_m488, local_rbx, (int32_t)(*(uint32_t *)(v_rip + 0x902D47)), a4);
    local_r11 = 0;
    result = (((uint32_t)((int32_t)((uint32_t)(result)))) == 2) ? 1 : 0;
    result = (uint32_t)((result) + 1);
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) - ((uint32_t)(result)));
    if (condition_is_less_or_equal) goto loc_00507A00;
    result = write_char(v_stack_m488, v_stack_m460, v_stack_m494, (int32_t)((uint32_t)(result)));
    local_rsi = (local_rbx) + ((int32_t)((uint32_t)(result)));
    if (condition_is_greater) goto loc_005079B2;
    goto loc_00507A07;
loc_00507A00:
    local_rdi = (uint32_t)(((uint32_t)(v_stack_m494)) | (0xFFFFFFFFULL));
    v_stack_m494 = (uint32_t)(local_rdi);
loc_00507A07:
    goto loc_00507A51;
loc_00507A0D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m460 + 0x18)))) & (64)) == 0) goto loc_00507A29;
    if ((*(uint64_t *)(v_stack_m460 + 0x10)) != 0) goto loc_00507A29;
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_r12)));
    v_stack_m494 = (uint32_t)(local_rdi);
    goto loc_00507A51;
loc_00507A29:
    if (condition_is_less_or_equal) goto loc_00507A51;
loc_00507A2E:
    a4 = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) - 1);
    result = write_char(*(uint16_t *)(local_rbx), v_stack_m460, v_stack_m494, a4);
    if (((uint32_t)((uint32_t)(v_stack_m494))) == -1) goto loc_00507A51;
    if (condition_is_greater) goto loc_00507A2E;
loc_00507A51:
    if (sign_flag) goto loc_00507C87;
    goto loc_00507A78;
loc_00507A64:
    local_r15 = (uint32_t)((local_r15) - 1);
    result = write_char(32, v_stack_m460, v_stack_m494, a4);
loc_00507A78:
    if (((uint32_t)((uint32_t)(v_stack_m494))) == -1) goto loc_00507C87;
    if (condition_is_greater) goto loc_00507A64;
    goto loc_00507C87;
loc_00507A88:
    if (32 == 73) goto loc_00507AB7;
    if (32 == 104) goto loc_00507B10;
    if (32 == ((uint32_t)(73 + 33))) goto loc_00507ABC;
    if (32 == ((uint32_t)(73 + 35))) goto loc_00507AED;
    if (32 == 116) goto loc_00507AB7;
    if (32 == 119) goto loc_00507AE3;
    if (32 != 122) goto loc_00507C7B;
loc_00507AB7:
loc_00507ABC:
    if (((uint16_t)(a4)) != 73) goto loc_00507B39;
    if (((uint16_t)(*(uint16_t *)(local_r13))) != 54) goto loc_00507B1D;
    if ((*(uint16_t *)(local_r13 + 0x2)) != 52) goto loc_00507B43;
    local_r13 = (local_r13) + (4);
    goto loc_00507C7B;
loc_00507AE3:
    goto loc_00507C7B;
loc_00507AED:
    if ((*(uint16_t *)(local_r13)) != ((uint16_t)(*(uint16_t *)(local_r13)))) goto loc_00507B07;
    local_r13 = (local_r13) + (2);
    goto loc_00507C8C;
loc_00507B07:
    local_r14 = (uint32_t)((local_r14) | (16));
    goto loc_00507C8C;
loc_00507B10:
    local_r14 = (uint32_t)((local_r14) | (32));
    goto loc_00507C8C;
loc_00507B1D:
    if (((uint16_t)(*(uint16_t *)(local_r13))) != 51) goto loc_00507B43;
    if ((*(uint16_t *)(local_r13 + 0x2)) != 50) goto loc_00507B43;
    local_r13 = (local_r13) + (4);
    goto loc_00507C7B;
loc_00507B39:
    if (((uint16_t)(a4)) == ((uint16_t)(*(uint16_t *)(local_r13)))) goto loc_00507C7B;
loc_00507B43:
    result = (uint16_t)((*(uint16_t *)(local_r13)) - (88));
    if (((uint16_t)(result)) > 32) goto loc_00507B6A;
    if (((uint16_t)(result)) < 32) goto loc_00507C59;
loc_00507B6A:
loc_00507B6D:
    v_stack_m484 = 1;
    result = write_char((uint16_t)(a4), v_stack_m460, v_stack_m494, a4);
    goto loc_00507C7B;
loc_00507B91:
    if (((uint16_t)(a4)) != 42) goto loc_00507BC1;
    local_r15 = (local_r15) + (8);
    v_stack_m470 = local_r15;
    v_stack_m48C = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m494)));
    if (!sign_flag) goto loc_00507C8C;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m494))) | (0xFFFFFFFFULL));
    v_stack_m48C = (uint32_t)(local_rsi);
    goto loc_00507C8C;
loc_00507BC1:
    goto loc_00507C77;
loc_00507BCF:
    v_stack_m48C = 0;
    goto loc_00507C7B;
loc_00507BDC:
    if (((uint16_t)(a4)) != 42) goto loc_00507C04;
    local_r15 = (local_r15) + (8);
    v_stack_m470 = local_r15;
    if (sign_flag) {
        local_r14 = (uint32_t)((local_r14) | (4));
    }
    Arg2 = (uint32_t)(-((uint32_t)(*(uint32_t *)(v_stack_m494))));
    if (!sign_flag) { Arg2 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m494))))); }
    goto loc_00507C11;
loc_00507C04:
loc_00507C11:
    v_stack_m478 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m494)))) + (uint32_t)(v_stack_m478) + (uint32_t)(v_stack_m478) * 4 - 24 * 2);
    goto loc_00507C7B;
loc_00507C17:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m494)))))) == 32) goto loc_00507C55;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m494)))))) == 35) goto loc_00507C4E;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m494)))))) == ((uint32_t)(32 + 11))) goto loc_00507C48;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m494)))))) == ((uint32_t)(32 + 13))) goto loc_00507C42;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m494)))))) != ((uint32_t)(32 + 16))) goto loc_00507C8C;
    local_r14 = (uint32_t)((local_r14) | (8));
    goto loc_00507C8C;
loc_00507C42:
    local_r14 = (uint32_t)((local_r14) | (4));
    goto loc_00507C59;
loc_00507C48:
    local_r14 = (uint32_t)((local_r14) | (1));
    goto loc_00507C59;
loc_00507C4E:
    goto loc_00507C59;
loc_00507C55:
    local_r14 = (uint32_t)((local_r14) | (2));
loc_00507C59:
    goto loc_00507C8C;
loc_00507C5D:
    v_stack_m464 = 0;
    v_stack_m478 = 0;
    local_rsi = (uint32_t)((0) | (0xFFFFFFFFULL));
    v_stack_m490 = 0;
    v_stack_m484 = 0;
loc_00507C77:
    v_stack_m48C = (uint32_t)(local_rsi);
loc_00507C7B:
    goto loc_00507C8C;
loc_00507C82:
loc_00507C87:
loc_00507C8C:
    if ((uint16_t)(*(uint16_t *)(local_r13)) != 0) goto loc_0050745D;
loc_00507CA0:
    if ((uint32_t)((uint32_t)(v_stack_m498)) == 0) goto loc_00507CAB;
    if (((uint32_t)((uint32_t)(v_stack_m498))) != 7) goto loc_00507CAF;
loc_00507CAB:
    goto loc_00507CC6;
loc_00507CAF:
    a4 = 0;
    v_stack_m4A8 = 0;
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = EmpCheckErrataList(Arg1, Arg2, Arg3, a4);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
loc_00507CC6:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (0x490ULL);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005073AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
