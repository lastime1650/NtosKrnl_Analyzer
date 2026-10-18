# output_s

- RVA: `0x00506854`–`0x005070A1` (길이 `2,125` bytes)
- VA: `0x0000000140506854`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C294C`
- 디코드: `580`개 명령, `2,125/2,125` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x005068C3` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00506B19` → [safecrt_wctomb_s](safecrt_wctomb_s_function_005070A8.md) (function, `0x005070A8`)
- `0x00506D75` → [write_multi_char](write_multi_char_function_00503C30.md) (function, `0x00503C30`)
- `0x00506D8C` → [write_string](write_string_function_00503C88.md) (function, `0x00503C88`)
- `0x00506DA8` → [write_multi_char](write_multi_char_function_00503C30.md) (function, `0x00503C30`)
- `0x00506DE0` → [safecrt_wctomb_s](safecrt_wctomb_s_function_005070A8.md) (function, `0x005070A8`)
- `0x00506E05` → [write_string](write_string_function_00503C88.md) (function, `0x00503C88`)
- `0x00506E2D` → [write_string](write_string_function_00503C88.md) (function, `0x00503C88`)
- `0x00506E57` → [write_multi_char](write_multi_char_function_00503C30.md) (function, `0x00503C30`)
- `0x00506F47` → [write_char](write_char_function_00503BE0.md) (function, `0x00503BE0`)
- `0x0050706E` → [EmpCheckErrataList](../49/EmpCheckErrataList_function_0049E550.md) (function, `0x0049E550`)
- `0x00507080` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [soutput_s](soutput_s_function_00507184.md) at `0x005071F1`

### Static image references
- `0x00506873` → RVA `0x00E0A740` (`.data`; read)
- `0x005068FF` → RVA `0x0001F830` (`.rdata`; read)
- `0x00506A73` → RVA `0x0001EF98` (`.rdata`; read)
- `0x00506ACD` → RVA `0x0002AEF8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00506854  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00506859  55                              push rbp
0050685A  56                              push rsi
0050685B  57                              push rdi
0050685C  41 54                           push r12
0050685E  41 55                           push r13
00506860  41 56                           push r14
00506862  41 57                           push r15
00506864  48 8D AC 24 80 FE FF FF         lea rbp, [rsp - 0x180]
0050686C  48 81 EC 80 02 00 00            sub rsp, 0x280
00506873  48 8B 05 C6 3E 90 00            mov rax, qword ptr [rip + 0x903ec6]
0050687A  48 33 C4                        xor rax, rsp
0050687D  48 89 85 78 01 00 00            mov qword ptr [rbp + 0x178], rax
00506884  4C 8B E1                        mov r12, rcx
00506887  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
0050688C  33 C9                           xor ecx, ecx
0050688E  4C 89 44 24 50                  mov qword ptr [rsp + 0x50], r8
00506893  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00506897  8B F1                           mov esi, ecx
00506899  89 4C 24 4C                     mov dword ptr [rsp + 0x4c], ecx
0050689D  8B F9                           mov edi, ecx
0050689F  89 4C 24 3C                     mov dword ptr [rsp + 0x3c], ecx
005068A3  44 8B F9                        mov r15d, ecx
005068A6  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
005068AA  8B D9                           mov ebx, ecx
005068AC  89 4C 24 64                     mov dword ptr [rsp + 0x64], ecx
005068B0  4D 8B F0                        mov r14, r8
005068B3  4C 8B EA                        mov r13, rdx
005068B6  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
005068BB  33 D2                           xor edx, edx
005068BD  41 B8 00 02 00 00               mov r8d, 0x200
005068C3  E8 78 03 1C 00                  call 0x1406c6c40
005068C8  45 33 DB                        xor r11d, r11d
005068CB  44 89 5C 24 44                  mov dword ptr [rsp + 0x44], r11d
005068D0  4D 85 E4                        test r12, r12
005068D3  0F 84 86 07 00 00               je 0x14050705f
005068D9  4D 85 ED                        test r13, r13
005068DC  0F 84 7D 07 00 00               je 0x14050705f
005068E2  45 8A 4D 00                     mov r9b, byte ptr [r13]
005068E6  45 8B E3                        mov r12d, r11d
005068E9  44 89 5C 24 38                  mov dword ptr [rsp + 0x38], r11d
005068EE  45 8B D3                        mov r10d, r11d
005068F1  44 89 5C 24 40                  mov dword ptr [rsp + 0x40], r11d
005068F6  45 84 C9                        test r9b, r9b
005068F9  0F 84 5A 07 00 00               je 0x140507059
005068FF  48 8D 0D 2A 8F B1 FF            lea rcx, [rip - 0x4e70d6]
00506906  49 FF C5                        inc r13
00506909  4D 8B C6                        mov r8, r14
0050690C  44 39 5C 24 38                  cmp dword ptr [rsp + 0x38], r11d
00506911  0F 8C 37 07 00 00               jl 0x14050704e
00506917  41 8D 41 E0                     lea eax, [r9 - 0x20]
0050691B  3C 5A                           cmp al, 0x5a
0050691D  77 0E                           ja 0x14050692d
0050691F  49 0F BE C1                     movsx rax, r9b
00506923  0F B6 54 08 E0                  movzx edx, byte ptr [rax + rcx - 0x20]
00506928  83 E2 0F                        and edx, 0xf
0050692B  EB 03                           jmp 0x140506930
0050692D  41 8B D3                        mov edx, r11d
00506930  41 8D 04 D2                     lea eax, [r10 + rdx*8]
00506934  41 0F BE C9                     movsx ecx, r9b
00506938  03 C2                           add eax, edx
0050693A  48 8D 15 EF 8E B1 FF            lea rdx, [rip - 0x4e7111]
00506941  44 0F B6 14 10                  movzx r10d, byte ptr [rax + rdx]
00506946  41 C1 EA 04                     shr r10d, 4
0050694A  44 89 54 24 48                  mov dword ptr [rsp + 0x48], r10d
0050694F  41 83 FA 08                     cmp r10d, 8
00506953  0F 84 06 07 00 00               je 0x14050705f
00506959  41 8B D2                        mov edx, r10d
0050695C  45 85 D2                        test r10d, r10d
0050695F  0F 84 D0 05 00 00               je 0x140506f35
00506965  83 EA 01                        sub edx, 1
00506968  0F 84 96 06 00 00               je 0x140507004
0050696E  83 EA 01                        sub edx, 1
00506971  0F 84 55 06 00 00               je 0x140506fcc
00506977  83 EA 01                        sub edx, 1
0050697A  0F 84 13 06 00 00               je 0x140506f93
00506980  83 EA 01                        sub edx, 1
00506983  0F 84 FD 05 00 00               je 0x140506f86
00506989  83 EA 01                        sub edx, 1
0050698C  0F 84 BF 05 00 00               je 0x140506f51
00506992  83 EA 01                        sub edx, 1
00506995  0F 84 D2 04 00 00               je 0x140506e6d
0050699B  83 FA 01                        cmp edx, 1
0050699E  0F 85 91 06 00 00               jne 0x140507035
005069A4  83 F9 69                        cmp ecx, 0x69
005069A7  0F 8F A3 01 00 00               jg 0x140506b50
005069AD  74 31                           je 0x1405069e0
005069AF  83 E9 43                        sub ecx, 0x43
005069B2  0F 84 30 01 00 00               je 0x140506ae8
005069B8  83 E9 10                        sub ecx, 0x10
005069BB  0F 84 D3 00 00 00               je 0x140506a94
005069C1  83 E9 05                        sub ecx, 5
005069C4  0F 84 0D 02 00 00               je 0x140506bd7
005069CA  83 E9 02                        sub ecx, 2
005069CD  74 4A                           je 0x140506a19
005069CF  83 E9 09                        sub ecx, 9
005069D2  0F 84 1C 01 00 00               je 0x140506af4
005069D8  3B CA                           cmp ecx, edx
005069DA  0F 85 2C 03 00 00               jne 0x140506d0c
005069E0  83 CE 40                        or esi, 0x40
005069E3  41 BA 0A 00 00 00               mov r10d, 0xa
005069E9  B9 00 02 00 00                  mov ecx, 0x200
005069EE  49 83 C6 08                     add r14, 8
005069F2  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
005069F7  0F BA E6 0F                     bt esi, 0xf
005069FB  72 0A                           jb 0x140506a07
005069FD  0F BA E6 0C                     bt esi, 0xc
00506A01  0F 83 17 02 00 00               jae 0x140506c1e
00506A07  49 8B 00                        mov rax, qword ptr [r8]
00506A0A  40 F6 C6 40                     test sil, 0x40
00506A0E  0F 84 3D 02 00 00               je 0x140506c51
00506A14  E9 27 02 00 00                  jmp 0x140506c40
00506A19  49 8B 08                        mov rcx, qword ptr [r8]
00506A1C  49 83 C6 08                     add r14, 8
00506A20  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
00506A25  48 85 C9                        test rcx, rcx
00506A28  74 49                           je 0x140506a73
00506A2A  48 8B 59 08                     mov rbx, qword ptr [rcx + 8]
00506A2E  48 85 DB                        test rbx, rbx
00506A31  74 40                           je 0x140506a73
00506A33  0F B7 01                        movzx eax, word ptr [rcx]
00506A36  66 39 41 02                     cmp word ptr [rcx + 2], ax
00506A3A  0F 82 1F 06 00 00               jb 0x14050705f
00506A40  44 8B E0                        mov r12d, eax
00506A43  0F BA E6 0B                     bt esi, 0xb
00506A47  73 23                           jae 0x140506a6c
00506A49  F7 D0                           not eax
00506A4B  A8 01                           test al, 1
00506A4D  0F 84 0C 06 00 00               je 0x14050705f
00506A53  8B C3                           mov eax, ebx
00506A55  F7 D0                           not eax
00506A57  A8 01                           test al, 1
00506A59  0F 84 00 06 00 00               je 0x14050705f
00506A5F  C7 44 24 44 01 00 00 00         mov dword ptr [rsp + 0x44], 1
00506A67  41 D1 EC                        shr r12d, 1
00506A6A  EB 1E                           jmp 0x140506a8a
00506A6C  44 89 5C 24 44                  mov dword ptr [rsp + 0x44], r11d
00506A71  EB 17                           jmp 0x140506a8a
00506A73  48 8D 05 1E 85 B1 FF            lea rax, [rip - 0x4e7ae2]
00506A7A  49 83 CC FF                     or r12, 0xffffffffffffffff
00506A7E  48 8B D8                        mov rbx, rax
00506A81  49 FF C4                        inc r12
00506A84  46 38 1C 20                     cmp byte ptr [rax + r12], r11b
00506A88  75 F7                           jne 0x140506a81
00506A8A  44 89 64 24 40                  mov dword ptr [rsp + 0x40], r12d
00506A8F  E9 78 02 00 00                  jmp 0x140506d0c
00506A94  F7 C6 30 08 00 00               test esi, 0x830
00506A9A  75 04                           jne 0x140506aa0
00506A9C  0F BA EE 0B                     bts esi, 0xb
00506AA0  49 8B 18                        mov rbx, qword ptr [r8]
00506AA3  83 FF FF                        cmp edi, -1
00506AA6  8B CF                           mov ecx, edi
00506AA8  B8 FF FF FF 7F                  mov eax, 0x7fffffff
00506AAD  0F 44 C8                        cmove ecx, eax
00506AB0  49 83 C6 08                     add r14, 8
00506AB4  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
00506AB9  F7 C6 10 08 00 00               test esi, 0x810
00506ABF  0F 84 DA 00 00 00               je 0x140506b9f
00506AC5  48 8B C3                        mov rax, rbx
00506AC8  48 85 DB                        test rbx, rbx
00506ACB  75 0E                           jne 0x140506adb
00506ACD  48 8D 1D 24 44 B2 FF            lea rbx, [rip - 0x4dbbdc]
00506AD4  48 8D 05 1D 44 B2 FF            lea rax, [rip - 0x4dbbe3]
00506ADB  C7 44 24 44 01 00 00 00         mov dword ptr [rsp + 0x44], 1
00506AE3  E9 AB 00 00 00                  jmp 0x140506b93
00506AE8  F7 C6 30 08 00 00               test esi, 0x830
00506AEE  75 04                           jne 0x140506af4
00506AF0  0F BA EE 0B                     bts esi, 0xb
00506AF4  49 83 C6 08                     add r14, 8
00506AF8  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
00506AFD  F7 C6 10 08 00 00               test esi, 0x810
00506B03  74 2F                           je 0x140506b34
00506B05  45 0F B7 08                     movzx r9d, word ptr [r8]
00506B09  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00506B0E  41 B8 00 02 00 00               mov r8d, 0x200
00506B14  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00506B19  E8 8A 05 00 00                  call 0x1405070a8
00506B1E  44 8B 64 24 40                  mov r12d, dword ptr [rsp + 0x40]
00506B23  45 33 DB                        xor r11d, r11d
00506B26  85 C0                           test eax, eax
00506B28  74 1C                           je 0x140506b46
00506B2A  C7 44 24 64 01 00 00 00         mov dword ptr [rsp + 0x64], 1
00506B32  EB 12                           jmp 0x140506b46
00506B34  41 8A 00                        mov al, byte ptr [r8]
00506B37  41 BC 01 00 00 00               mov r12d, 1
00506B3D  88 44 24 70                     mov byte ptr [rsp + 0x70], al
00506B41  44 89 64 24 40                  mov dword ptr [rsp + 0x40], r12d
00506B46  48 8D 5C 24 70                  lea rbx, [rsp + 0x70]
00506B4B  E9 BC 01 00 00                  jmp 0x140506d0c
00506B50  83 E9 6E                        sub ecx, 0x6e
00506B53  0F 84 06 05 00 00               je 0x14050705f
00506B59  83 E9 01                        sub ecx, 1
00506B5C  0F 84 9F 00 00 00               je 0x140506c01
00506B62  83 E9 01                        sub ecx, 1
00506B65  74 67                           je 0x140506bce
00506B67  83 E9 03                        sub ecx, 3
00506B6A  0F 84 30 FF FF FF               je 0x140506aa0
00506B70  83 E9 02                        sub ecx, 2
00506B73  0F 84 6A FE FF FF               je 0x1405069e3
00506B79  83 F9 03                        cmp ecx, 3
00506B7C  0F 85 8A 01 00 00               jne 0x140506d0c
00506B82  8D 41 24                        lea eax, [rcx + 0x24]
00506B85  EB 55                           jmp 0x140506bdc
00506B87  FF C9                           dec ecx
00506B89  66 44 39 18                     cmp word ptr [rax], r11w
00506B8D  74 08                           je 0x140506b97
00506B8F  48 83 C0 02                     add rax, 2
00506B93  85 C9                           test ecx, ecx
00506B95  75 F0                           jne 0x140506b87
00506B97  48 2B C3                        sub rax, rbx
00506B9A  48 D1 F8                        sar rax, 1
00506B9D  EB 23                           jmp 0x140506bc2
00506B9F  48 85 DB                        test rbx, rbx
00506BA2  48 8D 05 EF 83 B1 FF            lea rax, [rip - 0x4e7c11]
00506BA9  48 0F 45 C3                     cmovne rax, rbx
00506BAD  48 8B D8                        mov rbx, rax
00506BB0  EB 0A                           jmp 0x140506bbc
00506BB2  FF C9                           dec ecx
00506BB4  44 38 18                        cmp byte ptr [rax], r11b
00506BB7  74 07                           je 0x140506bc0
00506BB9  48 FF C0                        inc rax
00506BBC  85 C9                           test ecx, ecx
00506BBE  75 F2                           jne 0x140506bb2
00506BC0  2B C3                           sub eax, ebx
00506BC2  44 8B E0                        mov r12d, eax
00506BC5  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00506BC9  E9 3E 01 00 00                  jmp 0x140506d0c
00506BCE  BF 10 00 00 00                  mov edi, 0x10
00506BD3  0F BA EE 0F                     bts esi, 0xf
00506BD7  B8 07 00 00 00                  mov eax, 7
00506BDC  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00506BE0  40 84 F6                        test sil, sil
00506BE3  79 11                           jns 0x140506bf6
00506BE5  04 51                           add al, 0x51
00506BE7  C6 44 24 34 30                  mov byte ptr [rsp + 0x34], 0x30
00506BEC  88 44 24 35                     mov byte ptr [rsp + 0x35], al
00506BF0  41 BF 02 00 00 00               mov r15d, 2
00506BF6  41 BA 10 00 00 00               mov r10d, 0x10
00506BFC  E9 E8 FD FF FF                  jmp 0x1405069e9
00506C01  B8 08 00 00 00                  mov eax, 8
00506C06  44 8B D0                        mov r10d, eax
00506C09  40 84 F6                        test sil, sil
00506C0C  0F 89 D7 FD FF FF               jns 0x1405069e9
00506C12  B9 00 02 00 00                  mov ecx, 0x200
00506C17  0B F1                           or esi, ecx
00506C19  E9 D0 FD FF FF                  jmp 0x1405069ee
00506C1E  8B C6                           mov eax, esi
00506C20  83 E0 40                        and eax, 0x40
00506C23  40 F6 C6 20                     test sil, 0x20
00506C27  74 10                           je 0x140506c39
00506C29  85 C0                           test eax, eax
00506C2B  74 06                           je 0x140506c33
00506C2D  49 0F BF 00                     movsx rax, word ptr [r8]
00506C31  EB 0D                           jmp 0x140506c40
00506C33  41 0F B7 00                     movzx eax, word ptr [r8]
00506C37  EB 18                           jmp 0x140506c51
00506C39  85 C0                           test eax, eax
00506C3B  74 11                           je 0x140506c4e
00506C3D  49 63 00                        movsxd rax, dword ptr [r8]
00506C40  48 85 C0                        test rax, rax
00506C43  79 0C                           jns 0x140506c51
00506C45  48 F7 D8                        neg rax
00506C48  0F BA EE 08                     bts esi, 8
00506C4C  EB 03                           jmp 0x140506c51
00506C4E  41 8B 00                        mov eax, dword ptr [r8]
00506C51  F7 C6 00 90 00 00               test esi, 0x9000
00506C57  44 8B C0                        mov r8d, eax
00506C5A  4C 0F 45 C0                     cmovne r8, rax
00506C5E  85 FF                           test edi, edi
00506C60  79 07                           jns 0x140506c69
00506C62  BF 01 00 00 00                  mov edi, 1
00506C67  EB 08                           jmp 0x140506c71
00506C69  83 E6 F7                        and esi, 0xfffffff7
00506C6C  3B F9                           cmp edi, ecx
00506C6E  0F 4F F9                        cmovg edi, ecx
00506C71  49 8B C0                        mov rax, r8
00506C74  48 F7 D8                        neg rax
00506C77  1B C9                           sbb ecx, ecx
00506C79  41 23 CF                        and ecx, r15d
00506C7C  44 8B 7C 24 60                  mov r15d, dword ptr [rsp + 0x60]
00506C81  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00506C85  44 8B C9                        mov r9d, ecx
00506C88  48 8D 8D 6F 01 00 00            lea rcx, [rbp + 0x16f]
00506C8F  8B C7                           mov eax, edi
00506C91  FF CF                           dec edi
00506C93  85 C0                           test eax, eax
00506C95  7F 05                           jg 0x140506c9c
00506C97  4D 85 C0                        test r8, r8
00506C9A  74 1D                           je 0x140506cb9
00506C9C  33 D2                           xor edx, edx
00506C9E  49 8B C0                        mov rax, r8
00506CA1  49 F7 F2                        div r10
00506CA4  83 C2 30                        add edx, 0x30
00506CA7  4C 8B C0                        mov r8, rax
00506CAA  83 FA 39                        cmp edx, 0x39
00506CAD  7E 03                           jle 0x140506cb2
00506CAF  41 03 D7                        add edx, r15d
00506CB2  88 11                           mov byte ptr [rcx], dl
00506CB4  48 FF C9                        dec rcx
00506CB7  EB D6                           jmp 0x140506c8f
00506CB9  48 8D 85 6F 01 00 00            lea rax, [rbp + 0x16f]
00506CC0  89 7C 24 3C                     mov dword ptr [rsp + 0x3c], edi
00506CC4  2B C1                           sub eax, ecx
00506CC6  48 8D 59 01                     lea rbx, [rcx + 1]
00506CCA  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00506CCE  44 8B E0                        mov r12d, eax
00506CD1  45 8B F9                        mov r15d, r9d
00506CD4  0F BA E6 09                     bt esi, 9
00506CD8  73 2F                           jae 0x140506d09
00506CDA  85 C0                           test eax, eax
00506CDC  74 0F                           je 0x140506ced
00506CDE  80 3B 30                        cmp byte ptr [rbx], 0x30
00506CE1  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
00506CE6  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
00506CEB  74 1C                           je 0x140506d09
00506CED  48 FF CB                        dec rbx
00506CF0  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
00506CF5  44 8D 60 01                     lea r12d, [rax + 1]
00506CF9  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
00506CFE  44 89 64 24 40                  mov dword ptr [rsp + 0x40], r12d
00506D03  45 8B F9                        mov r15d, r9d
00506D06  C6 03 30                        mov byte ptr [rbx], 0x30
00506D09  45 33 DB                        xor r11d, r11d
00506D0C  44 39 5C 24 64                  cmp dword ptr [rsp + 0x64], r11d
00506D11  0F 85 19 03 00 00               jne 0x140507030
00506D17  40 F6 C6 40                     test sil, 0x40
00506D1B  74 32                           je 0x140506d4f
00506D1D  0F BA E6 08                     bt esi, 8
00506D21  73 07                           jae 0x140506d2a
00506D23  C6 44 24 34 2D                  mov byte ptr [rsp + 0x34], 0x2d
00506D28  EB 0B                           jmp 0x140506d35
00506D2A  40 F6 C6 01                     test sil, 1
00506D2E  74 12                           je 0x140506d42
00506D30  C6 44 24 34 2B                  mov byte ptr [rsp + 0x34], 0x2b
00506D35  41 BE 01 00 00 00               mov r14d, 1
00506D3B  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
00506D40  EB 12                           jmp 0x140506d54
00506D42  40 F6 C6 02                     test sil, 2
00506D46  74 07                           je 0x140506d4f
00506D48  C6 44 24 34 20                  mov byte ptr [rsp + 0x34], 0x20
00506D4D  EB E6                           jmp 0x140506d35
00506D4F  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
00506D54  44 8B 7C 24 4C                  mov r15d, dword ptr [rsp + 0x4c]
00506D59  8B FE                           mov edi, esi
00506D5B  45 2B FC                        sub r15d, r12d
00506D5E  45 2B FE                        sub r15d, r14d
00506D61  83 E7 0C                        and edi, 0xc
00506D64  75 14                           jne 0x140506d7a
00506D66  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00506D6B  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
00506D70  41 8B D7                        mov edx, r15d
00506D73  B1 20                           mov cl, 0x20
00506D75  E8 B6 CE FF FF                  call 0x140503c30
00506D7A  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00506D7F  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
00506D84  41 8B D6                        mov edx, r14d
00506D87  48 8D 4C 24 34                  lea rcx, [rsp + 0x34]
00506D8C  E8 F7 CE FF FF                  call 0x140503c88
00506D91  83 FF 08                        cmp edi, 8
00506D94  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00506D99  75 12                           jne 0x140506dad
00506D9B  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
00506DA0  4C 8B C7                        mov r8, rdi
00506DA3  41 8B D7                        mov edx, r15d
00506DA6  B1 30                           mov cl, 0x30
00506DA8  E8 83 CE FF FF                  call 0x140503c30
00506DAD  83 7C 24 44 00                  cmp dword ptr [rsp + 0x44], 0
00506DB2  74 6B                           je 0x140506e1f
00506DB4  45 85 E4                        test r12d, r12d
00506DB7  7E 66                           jle 0x140506e1f
00506DB9  83 64 24 68 00                  and dword ptr [rsp + 0x68], 0
00506DBE  4C 8B F3                        mov r14, rbx
00506DC1  41 8B FC                        mov edi, r12d
00506DC4  45 0F B7 0E                     movzx r9d, word ptr [r14]
00506DC8  48 8D 95 70 01 00 00            lea rdx, [rbp + 0x170]
00506DCF  41 B8 06 00 00 00               mov r8d, 6
00506DD5  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
00506DDA  4D 8D 76 02                     lea r14, [r14 + 2]
00506DDE  FF CF                           dec edi
00506DE0  E8 C3 02 00 00                  call 0x1405070a8
00506DE5  45 33 DB                        xor r11d, r11d
00506DE8  85 C0                           test eax, eax
00506DEA  75 27                           jne 0x140506e13
00506DEC  8B 54 24 68                     mov edx, dword ptr [rsp + 0x68]
00506DF0  85 D2                           test edx, edx
00506DF2  74 1F                           je 0x140506e13
00506DF4  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00506DF9  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
00506DFE  48 8D 8D 70 01 00 00            lea rcx, [rbp + 0x170]
00506E05  E8 7E CE FF FF                  call 0x140503c88
00506E0A  45 33 DB                        xor r11d, r11d
00506E0D  85 FF                           test edi, edi
00506E0F  75 B3                           jne 0x140506dc4
00506E11  EB 05                           jmp 0x140506e18
00506E13  83 4C 24 38 FF                  or dword ptr [rsp + 0x38], 0xffffffff
00506E18  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00506E1D  EB 16                           jmp 0x140506e35
00506E1F  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
00506E24  4C 8B C7                        mov r8, rdi
00506E27  41 8B D4                        mov edx, r12d
00506E2A  48 8B CB                        mov rcx, rbx
00506E2D  E8 56 CE FF FF                  call 0x140503c88
00506E32  45 33 DB                        xor r11d, r11d
00506E35  44 39 5C 24 38                  cmp dword ptr [rsp + 0x38], r11d
00506E3A  0F 8C E7 01 00 00               jl 0x140507027
00506E40  40 F6 C6 04                     test sil, 4
00506E44  0F 84 DD 01 00 00               je 0x140507027
00506E4A  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
00506E4F  4C 8B C7                        mov r8, rdi
00506E52  41 8B D7                        mov edx, r15d
00506E55  B1 20                           mov cl, 0x20
00506E57  E8 D4 CD FF FF                  call 0x140503c30
00506E5C  8B 7C 24 3C                     mov edi, dword ptr [rsp + 0x3c]
00506E60  44 8B 7C 24 30                  mov r15d, dword ptr [rsp + 0x30]
00506E65  45 33 DB                        xor r11d, r11d
00506E68  E9 C3 01 00 00                  jmp 0x140507030
00506E6D  41 80 F9 49                     cmp r9b, 0x49
00506E71  74 29                           je 0x140506e9c
00506E73  41 80 F9 68                     cmp r9b, 0x68
00506E77  74 6F                           je 0x140506ee8
00506E79  41 80 F9 6A                     cmp r9b, 0x6a
00506E7D  74 1D                           je 0x140506e9c
00506E7F  B2 6C                           mov dl, 0x6c
00506E81  44 3A CA                        cmp r9b, dl
00506E84  74 41                           je 0x140506ec7
00506E86  41 80 F9 74                     cmp r9b, 0x74
00506E8A  74 10                           je 0x140506e9c
00506E8C  41 80 F9 77                     cmp r9b, 0x77
00506E90  74 2C                           je 0x140506ebe
00506E92  41 80 F9 7A                     cmp r9b, 0x7a
00506E96  0F 85 99 01 00 00               jne 0x140507035
00506E9C  0F BA EE 0F                     bts esi, 0xf
00506EA0  41 80 F9 49                     cmp r9b, 0x49
00506EA4  75 62                           jne 0x140506f08
00506EA6  41 8A 45 00                     mov al, byte ptr [r13]
00506EAA  3C 36                           cmp al, 0x36
00506EAC  75 42                           jne 0x140506ef0
00506EAE  41 80 7D 01 34                  cmp byte ptr [r13 + 1], 0x34
00506EB3  75 5D                           jne 0x140506f12
00506EB5  49 83 C5 02                     add r13, 2
00506EB9  E9 77 01 00 00                  jmp 0x140507035
00506EBE  0F BA EE 0B                     bts esi, 0xb
00506EC2  E9 6E 01 00 00                  jmp 0x140507035
00506EC7  41 8A 4D 00                     mov cl, byte ptr [r13]
00506ECB  3A CA                           cmp cl, dl
00506ECD  75 03                           jne 0x140506ed2
00506ECF  49 FF C5                        inc r13
00506ED2  3A CA                           cmp cl, dl
00506ED4  B8 00 10 00 00                  mov eax, 0x1000
00506ED9  B9 10 00 00 00                  mov ecx, 0x10
00506EDE  0F 45 C1                        cmovne eax, ecx
00506EE1  0B F0                           or esi, eax
00506EE3  E9 4D 01 00 00                  jmp 0x140507035
00506EE8  83 CE 20                        or esi, 0x20
00506EEB  E9 45 01 00 00                  jmp 0x140507035
00506EF0  3C 33                           cmp al, 0x33
00506EF2  75 1E                           jne 0x140506f12
00506EF4  41 80 7D 01 32                  cmp byte ptr [r13 + 1], 0x32
00506EF9  75 17                           jne 0x140506f12
00506EFB  49 83 C5 02                     add r13, 2
00506EFF  0F BA F6 0F                     btr esi, 0xf
00506F03  E9 2D 01 00 00                  jmp 0x140507035
00506F08  41 80 F9 6A                     cmp r9b, 0x6a
00506F0C  0F 84 23 01 00 00               je 0x140507035
00506F12  41 8A 45 00                     mov al, byte ptr [r13]
00506F16  2C 58                           sub al, 0x58
00506F18  3C 20                           cmp al, 0x20
00506F1A  77 14                           ja 0x140506f30
00506F1C  48 B9 01 10 82 20 01 00 00 00   movabs rcx, 0x120821001
00506F26  48 0F A3 C1                     bt rcx, rax
00506F2A  0F 82 05 01 00 00               jb 0x140507035
00506F30  44 89 5C 24 48                  mov dword ptr [rsp + 0x48], r11d
00506F35  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00506F3A  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
00506F3F  41 8A C9                        mov cl, r9b
00506F42  44 89 5C 24 44                  mov dword ptr [rsp + 0x44], r11d
00506F47  E8 94 CC FF FF                  call 0x140503be0
00506F4C  E9 14 FF FF FF                  jmp 0x140506e65
00506F51  41 80 F9 2A                     cmp r9b, 0x2a
00506F55  75 1D                           jne 0x140506f74
00506F57  41 8B 38                        mov edi, dword ptr [r8]
00506F5A  49 83 C6 08                     add r14, 8
00506F5E  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
00506F63  89 7C 24 3C                     mov dword ptr [rsp + 0x3c], edi
00506F67  85 FF                           test edi, edi
00506F69  0F 89 C6 00 00 00               jns 0x140507035
00506F6F  83 CF FF                        or edi, 0xffffffff
00506F72  EB 09                           jmp 0x140506f7d
00506F74  8D 3C BF                        lea edi, [rdi + rdi*4]
00506F77  8D 7F E8                        lea edi, [rdi - 0x18]
00506F7A  8D 3C 79                        lea edi, [rcx + rdi*2]
00506F7D  89 7C 24 3C                     mov dword ptr [rsp + 0x3c], edi
00506F81  E9 AF 00 00 00                  jmp 0x140507035
00506F86  41 8B FB                        mov edi, r11d
00506F89  44 89 5C 24 3C                  mov dword ptr [rsp + 0x3c], r11d
00506F8E  E9 A2 00 00 00                  jmp 0x140507035
00506F93  41 80 F9 2A                     cmp r9b, 0x2a
00506F97  75 20                           jne 0x140506fb9
00506F99  41 8B 10                        mov edx, dword ptr [r8]
00506F9C  49 83 C6 08                     add r14, 8
00506FA0  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
00506FA5  8B CA                           mov ecx, edx
00506FA7  85 D2                           test edx, edx
00506FA9  79 03                           jns 0x140506fae
00506FAB  83 CE 04                        or esi, 4
00506FAE  8B C2                           mov eax, edx
00506FB0  F7 DA                           neg edx
00506FB2  85 C0                           test eax, eax
00506FB4  0F 49 D1                        cmovns edx, ecx
00506FB7  EB 0D                           jmp 0x140506fc6
00506FB9  8B 54 24 4C                     mov edx, dword ptr [rsp + 0x4c]
00506FBD  8D 14 92                        lea edx, [rdx + rdx*4]
00506FC0  8D 52 E8                        lea edx, [rdx - 0x18]
00506FC3  8D 14 51                        lea edx, [rcx + rdx*2]
00506FC6  89 54 24 4C                     mov dword ptr [rsp + 0x4c], edx
00506FCA  EB 69                           jmp 0x140507035
00506FCC  41 80 F9 20                     cmp r9b, 0x20
00506FD0  74 2D                           je 0x140506fff
00506FD2  41 80 F9 23                     cmp r9b, 0x23
00506FD6  74 21                           je 0x140506ff9
00506FD8  41 80 F9 2B                     cmp r9b, 0x2b
00506FDC  74 16                           je 0x140506ff4
00506FDE  41 80 F9 2D                     cmp r9b, 0x2d
00506FE2  74 0B                           je 0x140506fef
00506FE4  41 80 F9 30                     cmp r9b, 0x30
00506FE8  75 4B                           jne 0x140507035
00506FEA  83 CE 08                        or esi, 8
00506FED  EB 46                           jmp 0x140507035
00506FEF  83 CE 04                        or esi, 4
00506FF2  EB 41                           jmp 0x140507035
00506FF4  83 CE 01                        or esi, 1
00506FF7  EB 3C                           jmp 0x140507035
00506FF9  0F BA EE 07                     bts esi, 7
00506FFD  EB 36                           jmp 0x140507035
00506FFF  83 CE 02                        or esi, 2
00507002  EB 31                           jmp 0x140507035
00507004  83 CF FF                        or edi, 0xffffffff
00507007  44 89 5C 24 64                  mov dword ptr [rsp + 0x64], r11d
0050700C  89 7C 24 3C                     mov dword ptr [rsp + 0x3c], edi
00507010  45 8B FB                        mov r15d, r11d
00507013  44 89 5C 24 4C                  mov dword ptr [rsp + 0x4c], r11d
00507018  41 8B F3                        mov esi, r11d
0050701B  44 89 5C 24 30                  mov dword ptr [rsp + 0x30], r11d
00507020  44 89 5C 24 44                  mov dword ptr [rsp + 0x44], r11d
00507025  EB 0E                           jmp 0x140507035
00507027  44 8B 7C 24 30                  mov r15d, dword ptr [rsp + 0x30]
0050702C  8B 7C 24 3C                     mov edi, dword ptr [rsp + 0x3c]
00507030  44 8B 54 24 48                  mov r10d, dword ptr [rsp + 0x48]
00507035  45 8A 4D 00                     mov r9b, byte ptr [r13]
00507039  48 8D 0D F0 87 B1 FF            lea rcx, [rip - 0x4e7810]
00507040  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
00507045  45 84 C9                        test r9b, r9b
00507048  0F 85 B8 F8 FF FF               jne 0x140506906
0050704E  45 85 D2                        test r10d, r10d
00507051  74 06                           je 0x140507059
00507053  41 83 FA 07                     cmp r10d, 7
00507057  75 06                           jne 0x14050705f
00507059  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
0050705D  EB 17                           jmp 0x140507076
0050705F  45 33 C9                        xor r9d, r9d
00507062  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
00507067  45 33 C0                        xor r8d, r8d
0050706A  33 D2                           xor edx, edx
0050706C  33 C9                           xor ecx, ecx
0050706E  E8 DD 74 F9 FF                  call 0x14049e550
00507073  83 C8 FF                        or eax, 0xffffffff
00507076  48 8B 8D 78 01 00 00            mov rcx, qword ptr [rbp + 0x178]
0050707D  48 33 CC                        xor rcx, rsp
00507080  E8 BB 55 1A 00                  call 0x1406ac640
00507085  48 8B 9C 24 D8 02 00 00         mov rbx, qword ptr [rsp + 0x2d8]
0050708D  48 81 C4 80 02 00 00            add rsp, 0x280
00507094  41 5F                           pop r15
00507096  41 5E                           pop r14
00507098  41 5D                           pop r13
0050709A  41 5C                           pop r12
0050709C  5F                              pop rdi
0050709D  5E                              pop rsi
0050709E  5D                              pop rbp
0050709F  C3                              ret
005070A0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall output_s(__int64 a1, __int64 a2, __int64 a3)
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
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m248;
    unsigned int v_stack_m250;
    unsigned int v_stack_m254;
    unsigned int v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned int v_stack_m26C;
    unsigned int v_stack_m270;
    unsigned int v_stack_m274;
    unsigned int v_stack_m278;
    unsigned int v_stack_m27C;
    unsigned int v_stack_m280;
    unsigned __int8 v_stack_m283;
    unsigned __int8 v_stack_m284;
    unsigned int v_stack_m288;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m49;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (640);
    result = (*(unsigned __int64 *)(v_rip + 9453254)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m260 = a1;
    a1 = 0;
    v_stack_m268 = a3;
    v_stack_m258 = 0;
    v_stack_m26C = 0;
    v_stack_m27C = 0;
    v_stack_m288 = 0;
    v_stack_m254 = 0;
    a2 = 0;
    result = memset(v_stack_m248, a2, 512, a4);
    v_r11 = 0;
    v_stack_m274 = 0;
    if (0 == 0) goto loc_0050705F;
    if (0 == 0) goto loc_0050705F;
    v_stack_m280 = 0;
    v_stack_m278 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(a2)) == 0) goto loc_00507059;
loc_00506906:
    v_r13 = (a2) + 1;
    if (v_stack_m280 < 0) goto loc_0050704E;
    if (((unsigned __int8)(*(unsigned __int8 *)(a2) - 32)) > 90) goto loc_0050692D;
    a2 = (unsigned int)((*(unsigned __int8 *)((__int8)((unsigned __int8)(*(unsigned __int8 *)(a2))) + v_rip - 5140694 * 1 - 32)) & (15));
    goto loc_00506930;
loc_0050692D:
loc_00506930:
    result = (unsigned int)((0 + 0 * 8) + (0));
    v_r10 = (unsigned int)((*(unsigned __int8 *)(result + v_rip - 5140753 * 1)) >> (4));
    v_stack_m270 = (unsigned int)(v_r10);
    if (((unsigned int)(v_r10)) == 8) goto loc_0050705F;
    if ((unsigned int)(v_r10) == 0) goto loc_00506F35;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) - (1));
    if (condition_is_equal) goto loc_00507004;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00506FCC;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00506F93;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00506F86;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00506F51;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_00506E6D;
    if (((unsigned int)(a2)) != 1) goto loc_00507035;
    if (((unsigned int)((__int8)((unsigned __int8)(*(unsigned __int8 *)(a2))))) > 105) goto loc_00506B50;
    if (((unsigned int)((__int8)((unsigned __int8)(*(unsigned __int8 *)(a2))))) == 105) goto loc_005069E0;
    a1 = (unsigned int)(((__int8)((unsigned __int8)(*(unsigned __int8 *)(a2)))) - (67));
    if (condition_is_equal) goto loc_00506AE8;
    a1 = (unsigned int)((a1) - (16));
    if (condition_is_equal) goto loc_00506A94;
    a1 = (unsigned int)((a1) - (5));
    if (condition_is_equal) goto loc_00506BD7;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00506A19;
    a1 = (unsigned int)((a1) - (9));
    if (condition_is_equal) goto loc_00506AF4;
    if (((unsigned int)(a1)) != ((unsigned int)(a2))) goto loc_00506D0C;
loc_005069E0:
    v_rsi = (unsigned int)((0) | (64));
loc_005069E3:
loc_005069E9:
loc_005069EE:
    v_r14 = (a3) + (8);
    v_stack_m268 = v_r14;
    if (condition_is_below) goto loc_00506A07;
    if (condition_is_above_or_equal) goto loc_00506C1E;
loc_00506A07:
    if ((((unsigned __int8)(v_rsi)) & (64)) == 0) goto loc_00506C51;
    goto loc_00506C40;
loc_00506A19:
    v_r14 = (v_r14) + (8);
    v_stack_m268 = v_r14;
    if (*(unsigned __int64 *)(a3) == 0) goto loc_00506A73;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a3) + 8) == 0) goto loc_00506A73;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a3) + 2)) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a3))))) goto loc_0050705F;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a3) + 2)) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a3))))) goto loc_00506A6C;
    result = (unsigned int)(~(*(unsigned __int16 *)(*(unsigned __int64 *)(a3))));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_0050705F;
    result = (unsigned int)(~((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) + 8)))));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_0050705F;
    v_stack_m274 = 1;
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a3))))) >> (1));
    goto loc_00506A8A;
loc_00506A6C:
    v_stack_m274 = 0;
    goto loc_00506A8A;
loc_00506A73:
    v_r12 = (v_r12) | (-1);
loc_00506A81:
    v_r12 = (v_r12) + 1;
    if ((*(unsigned __int8 *)(v_rip - 5143266 + v_r12 * 1)) != 0) goto loc_00506A81;
loc_00506A8A:
    v_stack_m278 = (unsigned int)(v_r12);
    goto loc_00506D0C;
loc_00506A94:
    if ((((unsigned int)(v_rsi)) & (0x830ULL)) == 0) {
    }
    a1 = 0;
    if (0 == -1) { a1 = (unsigned int)((unsigned int)(0x7FFFFFFFULL)); }
    v_r14 = (v_r14) + (8);
    v_stack_m268 = v_r14;
    if ((((unsigned int)(v_rsi)) & (0x810ULL)) == 0) goto loc_00506B9F;
    result = *(unsigned __int64 *)(a3);
    v_rbx = *(unsigned __int64 *)(a3);
    if (*(unsigned __int64 *)(a3) == 0) {
        v_rbx = v_rip - 5094364;
        result = v_rip - 5094371;
    }
    v_stack_m274 = 1;
    goto loc_00506B93;
loc_00506AE8:
    if ((((unsigned int)(v_rsi)) & (0x830ULL)) == 0) {
    }
    v_r14 = (v_r14) + (8);
    v_stack_m268 = v_r14;
    if ((((unsigned int)(v_rsi)) & (0x810ULL)) == 0) goto loc_00506B34;
    result = safecrt_wctomb_s(v_stack_m278, v_stack_m248, 512, *(unsigned __int16 *)(a3));
    v_r11 = 0;
    if ((unsigned int)(result) == 0) goto loc_00506B46;
    v_stack_m254 = 1;
    goto loc_00506B46;
loc_00506B34:
    v_stack_m248 = (unsigned __int8)(*(unsigned __int8 *)(512));
    v_stack_m278 = 1;
loc_00506B46:
    goto loc_00506D0C;
loc_00506B50:
    a1 = (unsigned int)((v_stack_m278) - (110));
    if (condition_is_equal) goto loc_0050705F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00506C01;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00506BCE;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00506AA0;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_005069E3;
    if (((unsigned int)(a1)) != 3) goto loc_00506D0C;
    goto loc_00506BDC;
loc_00506B87:
    a1 = (unsigned int)((a1) - 1);
    if ((*(unsigned __int16 *)(a1 + 36)) == 0) goto loc_00506B97;
    result = (a1 + 36) + (2);
loc_00506B93:
    if ((unsigned int)(a1) != 0) goto loc_00506B87;
loc_00506B97:
    result = (result) - (v_stack_m248);
    result = (result) >> (1);
    goto loc_00506BC2;
loc_00506B9F:
    result = v_rip - 5143569;
    if (v_stack_m248 != 0) { result = v_stack_m248; }
    goto loc_00506BBC;
loc_00506BB2:
    a1 = (unsigned int)((a1) - 1);
    if ((*(unsigned __int8 *)(result)) == 0) goto loc_00506BC0;
    result = (result) + 1;
loc_00506BBC:
    if ((unsigned int)(a1) != 0) goto loc_00506BB2;
loc_00506BC0:
    result = (unsigned int)((result) - ((unsigned int)(result)));
loc_00506BC2:
    v_stack_m278 = (unsigned int)(result);
    goto loc_00506D0C;
loc_00506BCE:
loc_00506BD7:
loc_00506BDC:
    v_stack_m258 = 7;
    result = 7;
    v_r15 = 0;
    if (sign_flag) {
        result = (unsigned __int8)((7) + (81));
        v_stack_m284 = 48;
        v_stack_m283 = (unsigned __int8)(result);
        v_r15 = 2;
    }
    goto loc_005069E9;
loc_00506C01:
    if (!sign_flag) goto loc_005069E9;
    v_rsi = (unsigned int)((v_rsi) | (512));
    goto loc_005069EE;
loc_00506C1E:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & (64));
    if ((((unsigned __int8)(v_rsi)) & (32)) == 0) goto loc_00506C39;
    if ((unsigned int)(result) == 0) goto loc_00506C33;
    goto loc_00506C40;
loc_00506C33:
    goto loc_00506C51;
loc_00506C39:
    if ((unsigned int)(*(unsigned __int16 *)(512)) == 0) goto loc_00506C4E;
loc_00506C40:
    if (!sign_flag) goto loc_00506C51;
    result = -((int)(*(unsigned int *)(512)));
    goto loc_00506C51;
loc_00506C4E:
loc_00506C51:
    a3 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(512))));
    if ((((unsigned int)(v_rsi)) & (0x9000ULL)) != 0) { a3 = (unsigned int)(*(unsigned int *)(512)); }
    if (!sign_flag) goto loc_00506C69;
    goto loc_00506C71;
loc_00506C69:
    v_rsi = (unsigned int)((v_rsi) & (0xFFFFFFF7ULL));
    v_rdi = 1;
    if (1 > 512) { v_rdi = 512; }
loc_00506C71:
    result = -(a3);
    a1 = (unsigned int)((512) & ((unsigned int)(v_r15)));
    v_stack_m288 = (unsigned int)(a1);
loc_00506C8F:
    v_rdi = (unsigned int)((v_rdi) - 1);
    if (condition_is_greater) goto loc_00506C9C;
    if (a3 == 0) goto loc_00506CB9;
loc_00506C9C:
    a2 = 0;
    a2 = (unsigned int)((a2) + (48));
    if (((unsigned int)(a2)) >= = 57) {
        a2 = (unsigned int)((a2) + ((unsigned int)((unsigned int)(v_stack_m258))));
    }
    *(unsigned __int8 *)(v_stack_m49) = (unsigned __int8)(a2);
    a1 = (v_stack_m49) - 1;
    goto loc_00506C8F;
loc_00506CB9:
    v_stack_m27C = (unsigned int)(v_rdi);
    result = (unsigned int)((v_stack_m49) - ((unsigned int)(a1)));
    v_stack_m278 = (unsigned int)(result);
    if (condition_is_above_or_equal) goto loc_00506D09;
    if ((unsigned int)(result) == 0) goto loc_00506CED;
    v_stack_m268 = v_r14;
    v_stack_m288 = (unsigned int)((unsigned int)((unsigned int)(a1)));
    v_rbx = a1 + 1;
    v_r12 = (unsigned int)((unsigned int)(result));
    v_r15 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1))));
    if ((*(unsigned __int8 *)(a1 + 1)) != 48) {
        v_rbx = (a1 + 1) - 1;
        v_stack_m268 = v_r14;
        v_r12 = result + 1;
        v_stack_m288 = (unsigned int)((unsigned int)((unsigned int)(a1)));
        v_stack_m278 = (unsigned int)(v_r12);
        v_r15 = (unsigned int)((unsigned int)((unsigned int)(a1)));
        *(unsigned __int8 *)(v_rbx) = 48;
    }
    v_r11 = 0;
loc_00506D0C:
    if (v_stack_m254 != 0) goto loc_00507030;
    if ((((unsigned __int8)(v_rsi)) & (64)) == 0) goto loc_00506D4F;
    if (condition_is_above_or_equal) goto loc_00506D2A;
    v_stack_m284 = 45;
    goto loc_00506D35;
loc_00506D2A:
    if ((((unsigned __int8)(v_rsi)) & (1)) == 0) goto loc_00506D42;
    v_stack_m284 = 43;
loc_00506D35:
    v_stack_m288 = 1;
    goto loc_00506D54;
loc_00506D42:
    if ((((unsigned __int8)(v_rsi)) & (2)) == 0) goto loc_00506D4F;
    v_stack_m284 = 32;
    goto loc_00506D35;
loc_00506D4F:
loc_00506D54:
    v_r15 = (unsigned int)(((unsigned int)(v_stack_m26C)) - ((unsigned int)(v_r12)));
    v_r15 = (unsigned int)((v_r15) - ((unsigned int)((unsigned int)(v_stack_m288))));
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & (12));
    if (!(condition_is_not_equal)) {
        a3 = v_stack_m260;
        a4 = v_stack_m280;
        a2 = (unsigned int)(v_r15);
        a1 = 32;
        result = write_multi_char(a1, a2, a3, a4);
    }
    result = write_string(v_stack_m284, (unsigned int)((unsigned int)((unsigned int)(v_stack_m288))), v_stack_m260, v_stack_m280);
    if (((unsigned int)(v_rdi)) == 8) {
        a4 = v_stack_m280;
        a3 = v_stack_m260;
        a2 = (unsigned int)(v_r15);
        a1 = 48;
        result = write_multi_char(a1, a2, a3, a4);
    }
    if (v_stack_m274 == 0) goto loc_00506E1F;
    if (condition_is_less_or_equal) goto loc_00506E1F;
loc_00506DC4:
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) - 1);
    result = safecrt_wctomb_s(v_stack_m250, v_stack_m48, 6, *(unsigned __int16 *)(v_rbx));
    v_r11 = 0;
    if ((unsigned int)(result) != 0) goto loc_00506E13;
    if ((unsigned int)((unsigned int)(v_stack_m250)) == 0) goto loc_00506E13;
    result = write_string(v_stack_m48, (unsigned int)(v_stack_m250), v_stack_m260, v_stack_m280);
    v_r11 = 0;
    if ((unsigned int)(v_rdi) != 0) goto loc_00506DC4;
    goto loc_00506E18;
loc_00506E13:
loc_00506E18:
    goto loc_00506E35;
loc_00506E1F:
    result = write_string(v_rbx, (unsigned int)((unsigned int)(v_r12)), v_stack_m260, v_stack_m280);
    v_r11 = 0;
loc_00506E35:
    if (v_stack_m280 < 0) goto loc_00507027;
    if ((((unsigned __int8)(v_rsi)) & (4)) == 0) goto loc_00507027;
    result = write_multi_char(32, (unsigned int)((unsigned int)(v_r15)), v_stack_m260, v_stack_m280);
loc_00506E65:
    v_r11 = 0;
    goto loc_00507030;
loc_00506E6D:
    if (((unsigned __int8)(v_stack_m280)) == 73) goto loc_00506E9C;
    if (((unsigned __int8)(v_stack_m280)) == 104) goto loc_00506EE8;
    if (((unsigned __int8)(v_stack_m280)) == 106) goto loc_00506E9C;
    if (((unsigned __int8)(v_stack_m280)) == 108) goto loc_00506EC7;
    if (((unsigned __int8)(v_stack_m280)) == 116) goto loc_00506E9C;
    if (((unsigned __int8)(v_stack_m280)) == 119) goto loc_00506EBE;
    if (((unsigned __int8)(v_stack_m280)) != 122) goto loc_00507035;
loc_00506E9C:
    if (((unsigned __int8)(v_stack_m280)) != 73) goto loc_00506F08;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r13))) != 54) goto loc_00506EF0;
    if ((*(unsigned __int8 *)(v_r13 + 1)) != 52) goto loc_00506F12;
    v_r13 = (v_r13) + (2);
    goto loc_00507035;
loc_00506EBE:
    goto loc_00507035;
loc_00506EC7:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r13))) == 108) {
        v_r13 = (v_r13) + 1;
    }
    result = (unsigned int)(0x1000ULL);
    if (((unsigned __int8)(*(unsigned __int8 *)(v_r13))) != 108) { result = 16; }
    v_rsi = (unsigned int)((v_rsi) | ((unsigned int)(result)));
    goto loc_00507035;
loc_00506EE8:
    v_rsi = (unsigned int)((v_rsi) | (32));
    goto loc_00507035;
loc_00506EF0:
    if (((unsigned __int8)(result)) != 51) goto loc_00506F12;
    if ((*(unsigned __int8 *)(v_r13 + 1)) != 50) goto loc_00506F12;
    v_r13 = (v_r13) + (2);
    goto loc_00507035;
loc_00506F08:
    if (((unsigned __int8)(v_stack_m280)) == 106) goto loc_00507035;
loc_00506F12:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_r13)) - (88));
    if (((unsigned __int8)(result)) > 32) goto loc_00506F30;
    if (((unsigned __int8)(result)) < 32) goto loc_00507035;
loc_00506F30:
    v_stack_m270 = 0;
loc_00506F35:
    v_stack_m274 = 0;
    result = write_char((unsigned __int8)(v_stack_m280), v_stack_m260, v_stack_m280, v_stack_m280);
    goto loc_00506E65;
loc_00506F51:
    if (((unsigned __int8)(v_stack_m280)) != 42) goto loc_00506F74;
    v_r14 = (v_rbx + 2) + (8);
    v_stack_m268 = v_r14;
    v_stack_m27C = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m280)));
    if (!sign_flag) goto loc_00507035;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m280))) | (0xFFFFFFFFULL));
    goto loc_00506F7D;
loc_00506F74:
loc_00506F7D:
    v_stack_m27C = (unsigned int)((unsigned __int8)(v_stack_m280) + v_rdi + v_rdi * 4 - 24 * 2);
    goto loc_00507035;
loc_00506F86:
    v_stack_m27C = 0;
    goto loc_00507035;
loc_00506F93:
    if (((unsigned __int8)(v_stack_m280)) != 42) goto loc_00506FB9;
    v_r14 = (v_r14) + (8);
    v_stack_m268 = v_r14;
    if (sign_flag) {
        v_rsi = (unsigned int)((v_rsi) | (4));
    }
    a2 = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_stack_m280))));
    if (!sign_flag) { a2 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m280))))); }
    goto loc_00506FC6;
loc_00506FB9:
loc_00506FC6:
    v_stack_m26C = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m280)))) + (unsigned int)(v_stack_m26C) + (unsigned int)(v_stack_m26C) * 4 - 24 * 2);
    goto loc_00507035;
loc_00506FCC:
    if (((unsigned __int8)(v_stack_m280)) == 32) goto loc_00506FFF;
    if (((unsigned __int8)(v_stack_m280)) == 35) goto loc_00506FF9;
    if (((unsigned __int8)(v_stack_m280)) == 43) goto loc_00506FF4;
    if (((unsigned __int8)(v_stack_m280)) == 45) goto loc_00506FEF;
    if (((unsigned __int8)(v_stack_m280)) != 48) goto loc_00507035;
    v_rsi = (unsigned int)((v_rsi) | (8));
    goto loc_00507035;
loc_00506FEF:
    v_rsi = (unsigned int)((v_rsi) | (4));
    goto loc_00507035;
loc_00506FF4:
    v_rsi = (unsigned int)((v_rsi) | (1));
    goto loc_00507035;
loc_00506FF9:
    goto loc_00507035;
loc_00506FFF:
    v_rsi = (unsigned int)((v_rsi) | (2));
    goto loc_00507035;
loc_00507004:
    v_rdi = (unsigned int)((0) | (0xFFFFFFFFULL));
    v_stack_m254 = 0;
    v_stack_m27C = (unsigned int)(v_rdi);
    v_stack_m26C = 0;
    v_stack_m288 = 0;
    v_stack_m274 = 0;
    goto loc_00507035;
loc_00507027:
loc_00507030:
loc_00507035:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_r13)) != 0) goto loc_00506906;
loc_0050704E:
    if ((unsigned int)((unsigned int)(v_stack_m270)) == 0) goto loc_00507059;
    if (((unsigned int)((unsigned int)(v_stack_m270))) != 7) goto loc_0050705F;
loc_00507059:
    goto loc_00507076;
loc_0050705F:
    a4 = 0;
    v_stack_m298 = 0;
    a3 = 0;
    a2 = 0;
    a1 = 0;
    result = EmpCheckErrataList(a1, a2, a3, a4);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
loc_00507076:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (640);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t output_s(int64_t Arg1, int64_t Arg2, int64_t Arg3)
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
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m248;
    uint32_t v_stack_m250;
    uint32_t v_stack_m254;
    uint32_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint32_t v_stack_m26C;
    uint32_t v_stack_m270;
    uint32_t v_stack_m274;
    uint32_t v_stack_m278;
    uint32_t v_stack_m27C;
    uint32_t v_stack_m280;
    uint8_t v_stack_m283;
    uint8_t v_stack_m284;
    uint32_t v_stack_m288;
    uint64_t v_stack_m298;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m49;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (640);
    result = (*(uint64_t *)(v_rip + 0x903EC6)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m260 = Arg1;
    Arg1 = 0;
    v_stack_m268 = Arg3;
    v_stack_m258 = 0;
    v_stack_m26C = 0;
    v_stack_m27C = 0;
    v_stack_m288 = 0;
    v_stack_m254 = 0;
    Arg2 = 0;
    result = memset(v_stack_m248, Arg2, 512, a4);
    local_r11 = 0;
    v_stack_m274 = 0;
    if (0 == 0) goto loc_0050705F;
    if (0 == 0) goto loc_0050705F;
    v_stack_m280 = 0;
    v_stack_m278 = 0;
    if ((uint8_t)(*(uint8_t *)(Arg2)) == 0) goto loc_00507059;
loc_00506906:
    local_r13 = (Arg2) + 1;
    if (v_stack_m280 < 0) goto loc_0050704E;
    if (((uint8_t)(*(uint8_t *)(Arg2) - 32)) > 90) goto loc_0050692D;
    Arg2 = (uint32_t)((*(uint8_t *)((int8_t)((uint8_t)(*(uint8_t *)(Arg2))) + v_rip - 0x4E70D6 * 1 - 0x20)) & (15));
    goto loc_00506930;
loc_0050692D:
loc_00506930:
    result = (uint32_t)((0 + 0 * 8) + (0));
    local_r10 = (uint32_t)((*(uint8_t *)(result + v_rip - 0x4E7111 * 1)) >> (4));
    v_stack_m270 = (uint32_t)(local_r10);
    if (((uint32_t)(local_r10)) == 8) goto loc_0050705F;
    if ((uint32_t)(local_r10) == 0) goto loc_00506F35;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) - (1));
    if (condition_is_equal) goto loc_00507004;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00506FCC;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00506F93;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00506F86;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00506F51;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_00506E6D;
    if (((uint32_t)(Arg2)) != 1) goto loc_00507035;
    if (((uint32_t)((int8_t)((uint8_t)(*(uint8_t *)(Arg2))))) > 105) goto loc_00506B50;
    if (((uint32_t)((int8_t)((uint8_t)(*(uint8_t *)(Arg2))))) == 105) goto loc_005069E0;
    Arg1 = (uint32_t)(((int8_t)((uint8_t)(*(uint8_t *)(Arg2)))) - (67));
    if (condition_is_equal) goto loc_00506AE8;
    Arg1 = (uint32_t)((Arg1) - (16));
    if (condition_is_equal) goto loc_00506A94;
    Arg1 = (uint32_t)((Arg1) - (5));
    if (condition_is_equal) goto loc_00506BD7;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00506A19;
    Arg1 = (uint32_t)((Arg1) - (9));
    if (condition_is_equal) goto loc_00506AF4;
    if (((uint32_t)(Arg1)) != ((uint32_t)(Arg2))) goto loc_00506D0C;
loc_005069E0:
    local_rsi = (uint32_t)((0) | (64));
loc_005069E3:
loc_005069E9:
loc_005069EE:
    local_r14 = (Arg3) + (8);
    v_stack_m268 = local_r14;
    if (condition_is_below) goto loc_00506A07;
    if (condition_is_above_or_equal) goto loc_00506C1E;
loc_00506A07:
    if ((((uint8_t)(local_rsi)) & (64)) == 0) goto loc_00506C51;
    goto loc_00506C40;
loc_00506A19:
    local_r14 = (local_r14) + (8);
    v_stack_m268 = local_r14;
    if (*(uint64_t *)(Arg3) == 0) goto loc_00506A73;
    if (*(uint64_t *)(*(uint64_t *)(Arg3) + 0x8) == 0) goto loc_00506A73;
    if ((*(uint16_t *)(*(uint64_t *)(Arg3) + 0x2)) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg3))))) goto loc_0050705F;
    if ((*(uint16_t *)(*(uint64_t *)(Arg3) + 0x2)) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg3))))) goto loc_00506A6C;
    result = (uint32_t)(~(*(uint16_t *)(*(uint64_t *)(Arg3))));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_0050705F;
    result = (uint32_t)(~((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(Arg3) + 0x8)))));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_0050705F;
    v_stack_m274 = 1;
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(Arg3))))) >> (1));
    goto loc_00506A8A;
loc_00506A6C:
    v_stack_m274 = 0;
    goto loc_00506A8A;
loc_00506A73:
    local_r12 = (local_r12) | (-1);
loc_00506A81:
    local_r12 = (local_r12) + 1;
    if ((*(uint8_t *)(v_rip - 0x4E7AE2 + local_r12 * 1)) != 0) goto loc_00506A81;
loc_00506A8A:
    v_stack_m278 = (uint32_t)(local_r12);
    goto loc_00506D0C;
loc_00506A94:
    if ((((uint32_t)(local_rsi)) & (0x830ULL)) == 0) {
    }
    Arg1 = 0;
    if (0 == -1) { Arg1 = (uint32_t)((uint32_t)(0x7FFFFFFFULL)); }
    local_r14 = (local_r14) + (8);
    v_stack_m268 = local_r14;
    if ((((uint32_t)(local_rsi)) & (0x810ULL)) == 0) goto loc_00506B9F;
    result = *(uint64_t *)(Arg3);
    local_rbx = *(uint64_t *)(Arg3);
    if (*(uint64_t *)(Arg3) == 0) {
        local_rbx = v_rip - 5094364;
        result = v_rip - 5094371;
    }
    v_stack_m274 = 1;
    goto loc_00506B93;
loc_00506AE8:
    if ((((uint32_t)(local_rsi)) & (0x830ULL)) == 0) {
    }
    local_r14 = (local_r14) + (8);
    v_stack_m268 = local_r14;
    if ((((uint32_t)(local_rsi)) & (0x810ULL)) == 0) goto loc_00506B34;
    result = safecrt_wctomb_s(v_stack_m278, v_stack_m248, 512, *(uint16_t *)(Arg3));
    local_r11 = 0;
    if ((uint32_t)(result) == 0) goto loc_00506B46;
    v_stack_m254 = 1;
    goto loc_00506B46;
loc_00506B34:
    v_stack_m248 = (uint8_t)(*(uint8_t *)(512));
    v_stack_m278 = 1;
loc_00506B46:
    goto loc_00506D0C;
loc_00506B50:
    Arg1 = (uint32_t)((v_stack_m278) - (110));
    if (condition_is_equal) goto loc_0050705F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00506C01;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00506BCE;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00506AA0;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_005069E3;
    if (((uint32_t)(Arg1)) != 3) goto loc_00506D0C;
    goto loc_00506BDC;
loc_00506B87:
    Arg1 = (uint32_t)((Arg1) - 1);
    if ((*(uint16_t *)(Arg1 + 0x24)) == 0) goto loc_00506B97;
    result = (Arg1 + 36) + (2);
loc_00506B93:
    if ((uint32_t)(Arg1) != 0) goto loc_00506B87;
loc_00506B97:
    result = (result) - (v_stack_m248);
    result = (result) >> (1);
    goto loc_00506BC2;
loc_00506B9F:
    result = v_rip - 5143569;
    if (v_stack_m248 != 0) { result = v_stack_m248; }
    goto loc_00506BBC;
loc_00506BB2:
    Arg1 = (uint32_t)((Arg1) - 1);
    if ((*(uint8_t *)(result)) == 0) goto loc_00506BC0;
    result = (result) + 1;
loc_00506BBC:
    if ((uint32_t)(Arg1) != 0) goto loc_00506BB2;
loc_00506BC0:
    result = (uint32_t)((result) - ((uint32_t)(result)));
loc_00506BC2:
    v_stack_m278 = (uint32_t)(result);
    goto loc_00506D0C;
loc_00506BCE:
loc_00506BD7:
loc_00506BDC:
    v_stack_m258 = 7;
    result = 7;
    local_r15 = 0;
    if (sign_flag) {
        result = (uint8_t)((7) + (81));
        v_stack_m284 = 48;
        v_stack_m283 = (uint8_t)(result);
        local_r15 = 2;
    }
    goto loc_005069E9;
loc_00506C01:
    if (!sign_flag) goto loc_005069E9;
    local_rsi = (uint32_t)((local_rsi) | (512));
    goto loc_005069EE;
loc_00506C1E:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & (64));
    if ((((uint8_t)(local_rsi)) & (32)) == 0) goto loc_00506C39;
    if ((uint32_t)(result) == 0) goto loc_00506C33;
    goto loc_00506C40;
loc_00506C33:
    goto loc_00506C51;
loc_00506C39:
    if ((uint32_t)(*(uint16_t *)(512)) == 0) goto loc_00506C4E;
loc_00506C40:
    if (!sign_flag) goto loc_00506C51;
    result = -((int32_t)(*(uint32_t *)(512)));
    goto loc_00506C51;
loc_00506C4E:
loc_00506C51:
    Arg3 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(512))));
    if ((((uint32_t)(local_rsi)) & (0x9000ULL)) != 0) { Arg3 = (uint32_t)(*(uint32_t *)(512)); }
    if (!sign_flag) goto loc_00506C69;
    goto loc_00506C71;
loc_00506C69:
    local_rsi = (uint32_t)((local_rsi) & (0xFFFFFFF7ULL));
    local_rdi = 1;
    if (1 > 512) { local_rdi = 512; }
loc_00506C71:
    result = -(Arg3);
    Arg1 = (uint32_t)((512) & ((uint32_t)(local_r15)));
    v_stack_m288 = (uint32_t)(Arg1);
loc_00506C8F:
    local_rdi = (uint32_t)((local_rdi) - 1);
    if (condition_is_greater) goto loc_00506C9C;
    if (Arg3 == 0) goto loc_00506CB9;
loc_00506C9C:
    Arg2 = 0;
    Arg2 = (uint32_t)((Arg2) + (48));
    if (((uint32_t)(Arg2)) >= = 57) {
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)((uint32_t)(v_stack_m258))));
    }
    *(uint8_t *)(v_stack_m49) = (uint8_t)(Arg2);
    Arg1 = (v_stack_m49) - 1;
    goto loc_00506C8F;
loc_00506CB9:
    v_stack_m27C = (uint32_t)(local_rdi);
    result = (uint32_t)((v_stack_m49) - ((uint32_t)(Arg1)));
    v_stack_m278 = (uint32_t)(result);
    if (condition_is_above_or_equal) goto loc_00506D09;
    if ((uint32_t)(result) == 0) goto loc_00506CED;
    v_stack_m268 = local_r14;
    v_stack_m288 = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
    local_rbx = Arg1 + 1;
    local_r12 = (uint32_t)((uint32_t)(result));
    local_r15 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1))));
    if ((*(uint8_t *)(Arg1 + 0x1)) != 48) {
        local_rbx = (Arg1 + 1) - 1;
        v_stack_m268 = local_r14;
        local_r12 = result + 1;
        v_stack_m288 = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
        v_stack_m278 = (uint32_t)(local_r12);
        local_r15 = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
        *(uint8_t *)(local_rbx) = 48;
    }
    local_r11 = 0;
loc_00506D0C:
    if (v_stack_m254 != 0) goto loc_00507030;
    if ((((uint8_t)(local_rsi)) & (64)) == 0) goto loc_00506D4F;
    if (condition_is_above_or_equal) goto loc_00506D2A;
    v_stack_m284 = 45;
    goto loc_00506D35;
loc_00506D2A:
    if ((((uint8_t)(local_rsi)) & (1)) == 0) goto loc_00506D42;
    v_stack_m284 = 43;
loc_00506D35:
    v_stack_m288 = 1;
    goto loc_00506D54;
loc_00506D42:
    if ((((uint8_t)(local_rsi)) & (2)) == 0) goto loc_00506D4F;
    v_stack_m284 = 32;
    goto loc_00506D35;
loc_00506D4F:
loc_00506D54:
    local_r15 = (uint32_t)(((uint32_t)(v_stack_m26C)) - ((uint32_t)(local_r12)));
    local_r15 = (uint32_t)((local_r15) - ((uint32_t)((uint32_t)(v_stack_m288))));
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & (12));
    if (!(condition_is_not_equal)) {
        Arg3 = v_stack_m260;
        a4 = v_stack_m280;
        Arg2 = (uint32_t)(local_r15);
        Arg1 = 32;
        result = write_multi_char(Arg1, Arg2, Arg3, a4);
    }
    result = write_string(v_stack_m284, (uint32_t)((uint32_t)((uint32_t)(v_stack_m288))), v_stack_m260, v_stack_m280);
    if (((uint32_t)(local_rdi)) == 8) {
        a4 = v_stack_m280;
        Arg3 = v_stack_m260;
        Arg2 = (uint32_t)(local_r15);
        Arg1 = 48;
        result = write_multi_char(Arg1, Arg2, Arg3, a4);
    }
    if (v_stack_m274 == 0) goto loc_00506E1F;
    if (condition_is_less_or_equal) goto loc_00506E1F;
loc_00506DC4:
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) - 1);
    result = safecrt_wctomb_s(v_stack_m250, v_stack_m48, 6, *(uint16_t *)(local_rbx));
    local_r11 = 0;
    if ((uint32_t)(result) != 0) goto loc_00506E13;
    if ((uint32_t)((uint32_t)(v_stack_m250)) == 0) goto loc_00506E13;
    result = write_string(v_stack_m48, (uint32_t)(v_stack_m250), v_stack_m260, v_stack_m280);
    local_r11 = 0;
    if ((uint32_t)(local_rdi) != 0) goto loc_00506DC4;
    goto loc_00506E18;
loc_00506E13:
loc_00506E18:
    goto loc_00506E35;
loc_00506E1F:
    result = write_string(local_rbx, (uint32_t)((uint32_t)(local_r12)), v_stack_m260, v_stack_m280);
    local_r11 = 0;
loc_00506E35:
    if (v_stack_m280 < 0) goto loc_00507027;
    if ((((uint8_t)(local_rsi)) & (4)) == 0) goto loc_00507027;
    result = write_multi_char(32, (uint32_t)((uint32_t)(local_r15)), v_stack_m260, v_stack_m280);
loc_00506E65:
    local_r11 = 0;
    goto loc_00507030;
loc_00506E6D:
    if (((uint8_t)(v_stack_m280)) == 73) goto loc_00506E9C;
    if (((uint8_t)(v_stack_m280)) == 104) goto loc_00506EE8;
    if (((uint8_t)(v_stack_m280)) == 106) goto loc_00506E9C;
    if (((uint8_t)(v_stack_m280)) == 108) goto loc_00506EC7;
    if (((uint8_t)(v_stack_m280)) == 116) goto loc_00506E9C;
    if (((uint8_t)(v_stack_m280)) == 119) goto loc_00506EBE;
    if (((uint8_t)(v_stack_m280)) != 122) goto loc_00507035;
loc_00506E9C:
    if (((uint8_t)(v_stack_m280)) != 73) goto loc_00506F08;
    if (((uint8_t)(*(uint8_t *)(local_r13))) != 54) goto loc_00506EF0;
    if ((*(uint8_t *)(local_r13 + 0x1)) != 52) goto loc_00506F12;
    local_r13 = (local_r13) + (2);
    goto loc_00507035;
loc_00506EBE:
    goto loc_00507035;
loc_00506EC7:
    if (((uint8_t)(*(uint8_t *)(local_r13))) == 108) {
        local_r13 = (local_r13) + 1;
    }
    result = (uint32_t)(0x1000ULL);
    if (((uint8_t)(*(uint8_t *)(local_r13))) != 108) { result = 16; }
    local_rsi = (uint32_t)((local_rsi) | ((uint32_t)(result)));
    goto loc_00507035;
loc_00506EE8:
    local_rsi = (uint32_t)((local_rsi) | (32));
    goto loc_00507035;
loc_00506EF0:
    if (((uint8_t)(result)) != 51) goto loc_00506F12;
    if ((*(uint8_t *)(local_r13 + 0x1)) != 50) goto loc_00506F12;
    local_r13 = (local_r13) + (2);
    goto loc_00507035;
loc_00506F08:
    if (((uint8_t)(v_stack_m280)) == 106) goto loc_00507035;
loc_00506F12:
    result = (uint8_t)((*(uint8_t *)(local_r13)) - (88));
    if (((uint8_t)(result)) > 32) goto loc_00506F30;
    if (((uint8_t)(result)) < 32) goto loc_00507035;
loc_00506F30:
    v_stack_m270 = 0;
loc_00506F35:
    v_stack_m274 = 0;
    result = write_char((uint8_t)(v_stack_m280), v_stack_m260, v_stack_m280, v_stack_m280);
    goto loc_00506E65;
loc_00506F51:
    if (((uint8_t)(v_stack_m280)) != 42) goto loc_00506F74;
    local_r14 = (local_rbx + 2) + (8);
    v_stack_m268 = local_r14;
    v_stack_m27C = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m280)));
    if (!sign_flag) goto loc_00507035;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m280))) | (0xFFFFFFFFULL));
    goto loc_00506F7D;
loc_00506F74:
loc_00506F7D:
    v_stack_m27C = (uint32_t)((uint8_t)(v_stack_m280) + local_rdi + local_rdi * 4 - 24 * 2);
    goto loc_00507035;
loc_00506F86:
    v_stack_m27C = 0;
    goto loc_00507035;
loc_00506F93:
    if (((uint8_t)(v_stack_m280)) != 42) goto loc_00506FB9;
    local_r14 = (local_r14) + (8);
    v_stack_m268 = local_r14;
    if (sign_flag) {
        local_rsi = (uint32_t)((local_rsi) | (4));
    }
    Arg2 = (uint32_t)(-((uint32_t)(*(uint32_t *)(v_stack_m280))));
    if (!sign_flag) { Arg2 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m280))))); }
    goto loc_00506FC6;
loc_00506FB9:
loc_00506FC6:
    v_stack_m26C = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m280)))) + (uint32_t)(v_stack_m26C) + (uint32_t)(v_stack_m26C) * 4 - 24 * 2);
    goto loc_00507035;
loc_00506FCC:
    if (((uint8_t)(v_stack_m280)) == 32) goto loc_00506FFF;
    if (((uint8_t)(v_stack_m280)) == 35) goto loc_00506FF9;
    if (((uint8_t)(v_stack_m280)) == 43) goto loc_00506FF4;
    if (((uint8_t)(v_stack_m280)) == 45) goto loc_00506FEF;
    if (((uint8_t)(v_stack_m280)) != 48) goto loc_00507035;
    local_rsi = (uint32_t)((local_rsi) | (8));
    goto loc_00507035;
loc_00506FEF:
    local_rsi = (uint32_t)((local_rsi) | (4));
    goto loc_00507035;
loc_00506FF4:
    local_rsi = (uint32_t)((local_rsi) | (1));
    goto loc_00507035;
loc_00506FF9:
    goto loc_00507035;
loc_00506FFF:
    local_rsi = (uint32_t)((local_rsi) | (2));
    goto loc_00507035;
loc_00507004:
    local_rdi = (uint32_t)((0) | (0xFFFFFFFFULL));
    v_stack_m254 = 0;
    v_stack_m27C = (uint32_t)(local_rdi);
    v_stack_m26C = 0;
    v_stack_m288 = 0;
    v_stack_m274 = 0;
    goto loc_00507035;
loc_00507027:
loc_00507030:
loc_00507035:
    if ((uint8_t)(*(uint8_t *)(local_r13)) != 0) goto loc_00506906;
loc_0050704E:
    if ((uint32_t)((uint32_t)(v_stack_m270)) == 0) goto loc_00507059;
    if (((uint32_t)((uint32_t)(v_stack_m270))) != 7) goto loc_0050705F;
loc_00507059:
    goto loc_00507076;
loc_0050705F:
    a4 = 0;
    v_stack_m298 = 0;
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = EmpCheckErrataList(Arg1, Arg2, Arg3, a4);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
loc_00507076:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (640);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00506854&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
