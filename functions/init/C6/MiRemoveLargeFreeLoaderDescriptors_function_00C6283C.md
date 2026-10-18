# MiRemoveLargeFreeLoaderDescriptors

- RVA: `0x00C6283C`–`0x00C62C8A` (길이 `1,102` bytes)
- VA: `0x0000000140C6283C`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00075C18`
- 디코드: `296`개 명령, `1,102/1,102` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00C62949` → [MiFindDescriptorByPfn](../C5/MiFindDescriptorByPfn_function_00C5FBA0.md) (function, `0x00C5FBA0`)
- `0x00C6298A` → [MiRestrictRangeToNode](../../text/40/MiRestrictRangeToNode_function_0040199C.md) (function, `0x0040199C`)
- `0x00C62995` → [MiPageToNode](../../text/33/MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)
- `0x00C62B07` → [MiFindDescriptorByPfn](../C5/MiFindDescriptorByPfn_function_00C5FBA0.md) (function, `0x00C5FBA0`)
- `0x00C62B7F` → [RtlRbRemoveNode](../../text/2E/RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)
- `0x00C62C48` → [RtlRbInsertNodeEx](../../text/2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)

### Direct callers
- [MiInitNucleus](../C5/MiInitNucleus_function_00C5FD38.md) at `0x00C5FF06`

### Static image references
- `0x00C62858` → RVA `0x00FC6B30` (`ALMOSTRO`; read)
- `0x00C62876` → RVA `0x0100A1D0` (`INITDATA`; read)
- `0x00C62A29` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x00C62A8F` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00C6298A` → [MiRestrictRangeToNode](../../text/40/MiRestrictRangeToNode_function_0040199C.md) (`INIT` → `.text`)
  - `0x00C62995` → [MiPageToNode](../../text/33/MiPageToNode_function_00338CD0.md) (`INIT` → `.text`)
  - `0x00C62B7F` → [RtlRbRemoveNode](../../text/2E/RtlRbRemoveNode_function_002E4C10.md) (`INIT` → `.text`)
  - `0x00C62C48` → [RtlRbInsertNodeEx](../../text/2E/RtlRbInsertNodeEx_function_002E4570.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C6283C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00C62841  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00C62846  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00C6284B  57                              push rdi
00C6284C  41 54                           push r12
00C6284E  41 55                           push r13
00C62850  41 56                           push r14
00C62852  41 57                           push r15
00C62854  48 83 EC 20                     sub rsp, 0x20
00C62858  48 0F BA 25 CF 42 36 00 25      bt qword ptr [rip + 0x3642cf], 0x25
00C62861  4C 8B E1                        mov r12, rcx
00C62864  0F 83 02 04 00 00               jae 0x140c62c6c
00C6286A  33 ED                           xor ebp, ebp
00C6286C  4C 8D B1 60 01 00 00            lea r14, [rcx + 0x160]
00C62873  49 8B 06                        mov rax, qword ptr [r14]
00C62876  4C 8D 15 53 79 3A 00            lea r10, [rip + 0x3a7953]
00C6287D  44 8B FD                        mov r15d, ebp
00C62880  8B DD                           mov ebx, ebp
00C62882  41 B8 00 00 10 00               mov r8d, 0x100000
00C62888  44 8D 6D 01                     lea r13d, [rbp + 1]
00C6288C  45 84 6E 08                     test byte ptr [r14 + 8], r13b
00C62890  74 0C                           je 0x140c6289e
00C62892  48 85 C0                        test rax, rax
00C62895  0F 84 E5 01 00 00               je 0x140c62a80
00C6289B  49 33 C6                        xor rax, r14
00C6289E  48 85 C0                        test rax, rax
00C628A1  74 24                           je 0x140c628c7
00C628A3  41 8A 56 08                     mov dl, byte ptr [r14 + 8]
00C628A7  41 22 D5                        and dl, r13b
00C628AA  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00C628AE  48 8B D8                        mov rbx, rax
00C628B1  84 D2                           test dl, dl
00C628B3  74 0A                           je 0x140c628bf
00C628B5  48 85 C9                        test rcx, rcx
00C628B8  74 05                           je 0x140c628bf
00C628BA  48 33 C1                        xor rax, rcx
00C628BD  EB 03                           jmp 0x140c628c2
00C628BF  48 8B C1                        mov rax, rcx
00C628C2  48 85 C0                        test rax, rax
00C628C5  75 E3                           jne 0x140c628aa
00C628C7  48 85 DB                        test rbx, rbx
00C628CA  0F 84 B0 01 00 00               je 0x140c62a80
00C628D0  45 8B F5                        mov r14d, r13d
00C628D3  48 8B 03                        mov rax, qword ptr [rbx]
00C628D6  4C 8B EB                        mov r13, rbx
00C628D9  48 8B CB                        mov rcx, rbx
00C628DC  48 85 C0                        test rax, rax
00C628DF  74 1A                           je 0x140c628fb
00C628E1  EB 04                           jmp 0x140c628e7
00C628E3  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00C628E7  48 8B D8                        mov rbx, rax
00C628EA  48 39 68 08                     cmp qword ptr [rax + 8], rbp
00C628EE  75 F3                           jne 0x140c628e3
00C628F0  EB 13                           jmp 0x140c62905
00C628F2  48 39 4B 08                     cmp qword ptr [rbx + 8], rcx
00C628F6  74 0D                           je 0x140c62905
00C628F8  48 8B CB                        mov rcx, rbx
00C628FB  48 8B 5B 10                     mov rbx, qword ptr [rbx + 0x10]
00C628FF  48 83 E3 FC                     and rbx, 0xfffffffffffffffc
00C62903  75 ED                           jne 0x140c628f2
00C62905  49 8B 75 28                     mov rsi, qword ptr [r13 + 0x28]
00C62909  49 8B 7D 20                     mov rdi, qword ptr [r13 + 0x20]
00C6290D  48 81 FE 00 00 20 00            cmp rsi, 0x200000
00C62914  73 4F                           jae 0x140c62965
00C62916  48 8D 04 3E                     lea rax, [rsi + rdi]
00C6291A  48 3D 00 00 30 00               cmp rax, 0x300000
00C62920  0F 82 3F 01 00 00               jb 0x140c62a65
00C62926  49 3B C7                        cmp rax, r15
00C62929  0F 82 36 01 00 00               jb 0x140c62a65
00C6292F  48 81 E7 00 00 FC FF            and rdi, 0xfffffffffffc0000
00C62936  49 3B F8                        cmp rdi, r8
00C62939  0F 82 26 01 00 00               jb 0x140c62a65
00C6293F  48 8D 97 00 00 FC FF            lea rdx, [rdi - 0x40000]
00C62946  49 8B CC                        mov rcx, r12
00C62949  E8 52 D2 FF FF                  call 0x140c5fba0
00C6294E  48 8B D8                        mov rbx, rax
00C62951  48 85 C0                        test rax, rax
00C62954  0F 84 0B 01 00 00               je 0x140c62a65
00C6295A  41 B8 00 00 10 00               mov r8d, 0x100000
00C62960  E9 6E FF FF FF                  jmp 0x140c628d3
00C62965  49 3B F8                        cmp rdi, r8
00C62968  73 0D                           jae 0x140c62977
00C6296A  48 81 C7 00 00 F0 FF            add rdi, -0x100000
00C62971  48 03 F7                        add rsi, rdi
00C62974  49 8B F8                        mov rdi, r8
00C62977  4D 63 6D 18                     movsxd r13, dword ptr [r13 + 0x18]
00C6297B  48 85 F6                        test rsi, rsi
00C6297E  0F 84 D8 00 00 00               je 0x140c62a5c
00C62984  48 8B D6                        mov rdx, rsi
00C62987  48 8B CF                        mov rcx, rdi
00C6298A  E8 0D F0 79 FF                  call 0x14040199c
00C6298F  48 8B CF                        mov rcx, rdi
00C62992  48 8B E8                        mov rbp, rax
00C62995  E8 36 63 6D FF                  call 0x140338cd0
00C6299A  8B D0                           mov edx, eax
00C6299C  4C 8D 15 2D 78 3A 00            lea r10, [rip + 0x3a782d]
00C629A3  48 C1 E2 05                     shl rdx, 5
00C629A7  49 03 D2                        add rdx, r10
00C629AA  41 83 FD 06                     cmp r13d, 6
00C629AE  74 29                           je 0x140c629d9
00C629B0  41 8D 4D E2                     lea ecx, [r13 - 0x1e]
00C629B4  83 F9 02                        cmp ecx, 2
00C629B7  76 20                           jbe 0x140c629d9
00C629B9  41 83 FD 2C                     cmp r13d, 0x2c
00C629BD  77 10                           ja 0x140c629cf
00C629BF  48 B9 08 00 C0 00 C4 15 00 00   movabs rcx, 0x15c400c00008
00C629C9  4C 0F A3 E9                     bt rcx, r13
00C629CD  72 76                           jb 0x140c62a45
00C629CF  48 01 6A 10                     add qword ptr [rdx + 0x10], rbp
00C629D3  41 83 FD 02                     cmp r13d, 2
00C629D7  74 06                           je 0x140c629df
00C629D9  41 83 FD 18                     cmp r13d, 0x18
00C629DD  75 66                           jne 0x140c62a45
00C629DF  48 01 6A 18                     add qword ptr [rdx + 0x18], rbp
00C629E3  48 81 FD 00 00 20 00            cmp rbp, 0x200000
00C629EA  72 59                           jb 0x140c62a45
00C629EC  48 3B 6A 08                     cmp rbp, qword ptr [rdx + 8]
00C629F0  76 53                           jbe 0x140c62a45
00C629F2  49 83 CF FF                     or r15, 0xffffffffffffffff
00C629F6  48 89 3A                        mov qword ptr [rdx], rdi
00C629F9  45 33 C9                        xor r9d, r9d
00C629FC  48 89 6A 08                     mov qword ptr [rdx + 8], rbp
00C62A00  41 0F B7 D1                     movzx edx, r9w
00C62A04  0F B7 C2                        movzx eax, dx
00C62A07  4D 8B C7                        mov r8, r15
00C62A0A  48 C1 E0 05                     shl rax, 5
00C62A0E  4A 8B 4C 10 08                  mov rcx, qword ptr [rax + r10 + 8]
00C62A13  49 3B CF                        cmp rcx, r15
00C62A16  73 08                           jae 0x140c62a20
00C62A18  4C 8B F9                        mov r15, rcx
00C62A1B  48 85 C9                        test rcx, rcx
00C62A1E  74 25                           je 0x140c62a45
00C62A20  49 3B C8                        cmp rcx, r8
00C62A23  0F B7 C2                        movzx eax, dx
00C62A26  4C 8B F9                        mov r15, rcx
00C62A29  0F B7 0D D0 25 36 00            movzx ecx, word ptr [rip + 0x3625d0]
00C62A30  4D 0F 43 F8                     cmovae r15, r8
00C62A34  41 2B CE                        sub ecx, r14d
00C62A37  3B C1                           cmp eax, ecx
00C62A39  74 0A                           je 0x140c62a45
00C62A3B  66 41 03 D6                     add dx, r14w
00C62A3F  66 83 FA 40                     cmp dx, 0x40
00C62A43  72 BF                           jb 0x140c62a04
00C62A45  48 2B F5                        sub rsi, rbp
00C62A48  48 03 FD                        add rdi, rbp
00C62A4B  33 ED                           xor ebp, ebp
00C62A4D  48 85 F6                        test rsi, rsi
00C62A50  0F 85 2E FF FF FF               jne 0x140c62984
00C62A56  41 B8 00 00 10 00               mov r8d, 0x100000
00C62A5C  48 85 DB                        test rbx, rbx
00C62A5F  0F 85 6E FE FF FF               jne 0x140c628d3
00C62A65  4D 8D B4 24 60 01 00 00         lea r14, [r12 + 0x160]
00C62A6D  41 BD 01 00 00 00               mov r13d, 1
00C62A73  41 B8 00 00 10 00               mov r8d, 0x100000
00C62A79  4C 8D 15 50 77 3A 00            lea r10, [rip + 0x3a7750]
00C62A80  66 3B 2D 79 25 36 00            cmp bp, word ptr [rip + 0x362579]
00C62A87  8B DD                           mov ebx, ebp
00C62A89  0F 83 DD 01 00 00               jae 0x140c62c6c
00C62A8F  4C 8D 3D 6A D5 39 FF            lea r15, [rip - 0xc62a96]
00C62A96  44 8B DB                        mov r11d, ebx
00C62A99  49 C1 E3 05                     shl r11, 5
00C62A9D  4D 03 DA                        add r11, r10
00C62AA0  8B F3                           mov esi, ebx
00C62AA2  49 8B 7B 08                     mov rdi, qword ptr [r11 + 8]
00C62AA6  48 85 FF                        test rdi, rdi
00C62AA9  0F 84 A5 01 00 00               je 0x140c62c54
00C62AAF  49 8B 53 18                     mov rdx, qword ptr [r11 + 0x18]
00C62AB3  48 81 FA 00 00 30 00            cmp rdx, 0x300000
00C62ABA  0F 82 94 01 00 00               jb 0x140c62c54
00C62AC0  49 8B 43 10                     mov rax, qword ptr [r11 + 0x10]
00C62AC4  48 8D 0C 40                     lea rcx, [rax + rax*2]
00C62AC8  48 B8 FC FF FF FF FF FF 3F 00   movabs rax, 0x3ffffffffffffc
00C62AD2  48 C1 E1 04                     shl rcx, 4
00C62AD6  48 C1 E9 0A                     shr rcx, 0xa
00C62ADA  48 23 C8                        and rcx, rax
00C62ADD  48 8B C2                        mov rax, rdx
00C62AE0  49 3B C8                        cmp rcx, r8
00C62AE3  49 0F 42 C8                     cmovb rcx, r8
00C62AE7  48 2B C7                        sub rax, rdi
00C62AEA  48 3B C1                        cmp rax, rcx
00C62AED  73 0F                           jae 0x140c62afe
00C62AEF  48 3B D1                        cmp rdx, rcx
00C62AF2  0F 86 5C 01 00 00               jbe 0x140c62c54
00C62AF8  48 8B FA                        mov rdi, rdx
00C62AFB  48 2B F9                        sub rdi, rcx
00C62AFE  4D 8B 1B                        mov r11, qword ptr [r11]
00C62B01  49 8B CC                        mov rcx, r12
00C62B04  49 8B D3                        mov rdx, r11
00C62B07  E8 94 D0 FF FF                  call 0x140c5fba0
00C62B0C  48 8B D0                        mov rdx, rax
00C62B0F  4D 8D 8B FF FF 03 00            lea r9, [r11 + 0x3ffff]
00C62B16  48 C7 C0 00 00 FC FF            mov rax, 0xfffffffffffc0000
00C62B1D  49 8D 0C 3B                     lea rcx, [r11 + rdi]
00C62B21  48 23 C8                        and rcx, rax
00C62B24  4C 23 C8                        and r9, rax
00C62B27  4C 8B D1                        mov r10, rcx
00C62B2A  49 3B C9                        cmp rcx, r9
00C62B2D  0F 82 1A 01 00 00               jb 0x140c62c4d
00C62B33  49 2B C9                        sub rcx, r9
00C62B36  48 81 F9 00 00 04 00            cmp rcx, 0x40000
00C62B3D  0F 82 0A 01 00 00               jb 0x140c62c4d
00C62B43  8B 42 18                        mov eax, dword ptr [rdx + 0x18]
00C62B46  48 8D 3C 76                     lea rdi, [rsi + rsi*2]
00C62B4A  48 C1 E7 04                     shl rdi, 4
00C62B4E  42 89 84 3F E8 C9 00 01         mov dword ptr [rdi + r15 + 0x100c9e8], eax
00C62B56  4E 89 8C 3F F0 C9 00 01         mov qword ptr [rdi + r15 + 0x100c9f0], r9
00C62B5E  4A 89 8C 3F F8 C9 00 01         mov qword ptr [rdi + r15 + 0x100c9f8], rcx
00C62B66  4C 8B 5A 20                     mov r11, qword ptr [rdx + 0x20]
00C62B6A  4C 8B 42 28                     mov r8, qword ptr [rdx + 0x28]
00C62B6E  4B 8D 04 03                     lea rax, [r11 + r8]
00C62B72  4D 3B CB                        cmp r9, r11
00C62B75  75 26                           jne 0x140c62b9d
00C62B77  4C 3B D0                        cmp r10, rax
00C62B7A  75 0D                           jne 0x140c62b89
00C62B7C  49 8B CE                        mov rcx, r14
00C62B7F  E8 8C 20 68 FF                  call 0x1402e4c10
00C62B84  E9 C4 00 00 00                  jmp 0x140c62c4d
00C62B89  49 8D 04 0B                     lea rax, [r11 + rcx]
00C62B8D  48 89 42 20                     mov qword ptr [rdx + 0x20], rax
00C62B91  4C 2B C1                        sub r8, rcx
00C62B94  4C 89 42 28                     mov qword ptr [rdx + 0x28], r8
00C62B98  E9 B0 00 00 00                  jmp 0x140c62c4d
00C62B9D  4C 3B D0                        cmp r10, rax
00C62BA0  74 EF                           je 0x140c62b91
00C62BA2  8B 42 18                        mov eax, dword ptr [rdx + 0x18]
00C62BA5  4D 8D 9F B0 E8 00 01            lea r11, [r15 + 0x100e8b0]
00C62BAC  4C 03 DF                        add r11, rdi
00C62BAF  41 89 43 18                     mov dword ptr [r11 + 0x18], eax
00C62BB3  48 8B 42 20                     mov rax, qword ptr [rdx + 0x20]
00C62BB7  49 89 43 20                     mov qword ptr [r11 + 0x20], rax
00C62BBB  49 8B C1                        mov rax, r9
00C62BBE  48 2B 42 20                     sub rax, qword ptr [rdx + 0x20]
00C62BC2  49 89 43 28                     mov qword ptr [r11 + 0x28], rax
00C62BC6  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
00C62BCA  49 2B C1                        sub rax, r9
00C62BCD  48 2B C1                        sub rax, rcx
00C62BD0  48 03 42 20                     add rax, qword ptr [rdx + 0x20]
00C62BD4  48 89 42 28                     mov qword ptr [rdx + 0x28], rax
00C62BD8  4C 89 52 20                     mov qword ptr [rdx + 0x20], r10
00C62BDC  49 8B 16                        mov rdx, qword ptr [r14]
00C62BDF  45 84 6E 08                     test byte ptr [r14 + 8], r13b
00C62BE3  74 0D                           je 0x140c62bf2
00C62BE5  48 85 D2                        test rdx, rdx
00C62BE8  74 05                           je 0x140c62bef
00C62BEA  49 33 D6                        xor rdx, r14
00C62BED  EB 03                           jmp 0x140c62bf2
00C62BEF  48 8B D5                        mov rdx, rbp
00C62BF2  41 0F B6 4E 08                  movzx ecx, byte ptr [r14 + 8]
00C62BF7  44 8A C5                        mov r8b, bpl
00C62BFA  41 23 CD                        and ecx, r13d
00C62BFD  48 85 D2                        test rdx, rdx
00C62C00  74 40                           je 0x140c62c42
00C62C02  4D 8B 43 20                     mov r8, qword ptr [r11 + 0x20]
00C62C06  4C 3B 42 20                     cmp r8, qword ptr [rdx + 0x20]
00C62C0A  73 19                           jae 0x140c62c25
00C62C0C  48 8B 02                        mov rax, qword ptr [rdx]
00C62C0F  85 C9                           test ecx, ecx
00C62C11  74 08                           je 0x140c62c1b
00C62C13  48 85 C0                        test rax, rax
00C62C16  74 08                           je 0x140c62c20
00C62C18  48 33 C2                        xor rax, rdx
00C62C1B  48 85 C0                        test rax, rax
00C62C1E  75 1A                           jne 0x140c62c3a
00C62C20  44 8A C5                        mov r8b, bpl
00C62C23  EB 1D                           jmp 0x140c62c42
00C62C25  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00C62C29  85 C9                           test ecx, ecx
00C62C2B  74 08                           je 0x140c62c35
00C62C2D  48 85 C0                        test rax, rax
00C62C30  74 0D                           je 0x140c62c3f
00C62C32  48 33 C2                        xor rax, rdx
00C62C35  48 85 C0                        test rax, rax
00C62C38  74 05                           je 0x140c62c3f
00C62C3A  48 8B D0                        mov rdx, rax
00C62C3D  EB C7                           jmp 0x140c62c06
00C62C3F  45 8A C5                        mov r8b, r13b
00C62C42  4D 8B CB                        mov r9, r11
00C62C45  49 8B CE                        mov rcx, r14
00C62C48  E8 23 19 68 FF                  call 0x1402e4570
00C62C4D  4C 8D 15 7C 75 3A 00            lea r10, [rip + 0x3a757c]
00C62C54  0F B7 05 A5 23 36 00            movzx eax, word ptr [rip + 0x3623a5]
00C62C5B  41 03 DD                        add ebx, r13d
00C62C5E  41 B8 00 00 10 00               mov r8d, 0x100000
00C62C64  3B D8                           cmp ebx, eax
00C62C66  0F 82 2A FE FF FF               jb 0x140c62a96
00C62C6C  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00C62C71  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
00C62C76  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00C62C7B  48 83 C4 20                     add rsp, 0x20
00C62C7F  41 5F                           pop r15
00C62C81  41 5E                           pop r14
00C62C83  41 5D                           pop r13
00C62C85  41 5C                           pop r12
00C62C87  5F                              pop rdi
00C62C88  C3                              ret
00C62C89  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiRemoveLargeFreeLoaderDescriptors(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    if (condition_is_above_or_equal) goto loc_00C62C6C;
    v_rbp = 0;
    if (((*(unsigned __int8 *)(a1 + 352 + 8)) & ((unsigned __int8)(v_rbp + 1))) == 0) goto loc_00C6289E;
    if (*(unsigned __int64 *)(a1 + 352) == 0) goto loc_00C62A80;
    result = (*(unsigned __int64 *)(a1 + 352)) ^ (a1 + 352);
loc_00C6289E:
    if (result == 0) goto loc_00C628C7;
    a2 = (unsigned __int8)((*(unsigned __int8 *)(a1 + 352 + 8)) & ((unsigned __int8)(v_rbp + 1)));
loc_00C628AA:
    if ((unsigned __int8)(a2) == 0) goto loc_00C628BF;
    if (*(unsigned __int64 *)(result + 8) == 0) goto loc_00C628BF;
    result = (result) ^ (*(unsigned __int64 *)(result + 8));
    goto loc_00C628C2;
loc_00C628BF:
loc_00C628C2:
    if (*(unsigned __int64 *)(result + 8) != 0) goto loc_00C628AA;
loc_00C628C7:
    if (result == 0) goto loc_00C62A80;
loc_00C628D3:
    if (*(unsigned __int64 *)(result) == 0) goto loc_00C628FB;
    goto loc_00C628E7;
loc_00C628E3:
loc_00C628E7:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 8)) != 0) goto loc_00C628E3;
    goto loc_00C62905;
loc_00C628F2:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 8)) == result) goto loc_00C62905;
loc_00C628FB:
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 16)) & (-4);
    if (condition_is_not_equal) goto loc_00C628F2;
loc_00C62905:
    if ((*(unsigned __int64 *)(result + 40)) >= 0x200000ULL) goto loc_00C62965;
    if ((*(unsigned __int64 *)(result + 40) + *(unsigned __int64 *)(result + 32) * 1) < 0x300000ULL) goto loc_00C62A65;
    if ((*(unsigned __int64 *)(result + 40) + *(unsigned __int64 *)(result + 32) * 1) < 0) goto loc_00C62A65;
    v_rdi = (*(unsigned __int64 *)(result + 32)) & (0xFFFFFFFFFFFC0000ULL);
    if (v_rdi < ((unsigned int)(0x100000ULL))) goto loc_00C62A65;
    result = MiFindDescriptorByPfn(a1, v_rdi - 262144, (unsigned int)(0x100000ULL), a4);
    if (result == 0) goto loc_00C62A65;
    goto loc_00C628D3;
loc_00C62965:
    v_rsi = *(unsigned __int64 *)(result + 40);
    if (v_rdi < ((unsigned int)(0x100000ULL))) {
        v_rdi = (v_rdi) + (0xFFFFFFFFFFF00000ULL);
        v_rsi = (*(unsigned __int64 *)(result + 40)) + (v_rdi);
        v_rdi = (unsigned int)(0x100000ULL);
    }
    if (v_rsi == 0) goto loc_00C62A5C;
loc_00C62984:
    result = MiRestrictRangeToNode(v_rdi, v_rsi, (unsigned int)(0x100000ULL), a4);
    result = MiPageToNode(v_rdi, v_rsi, (unsigned int)(0x100000ULL), a4);
    a2 = ((unsigned int)((unsigned int)(result))) << (5);
    a2 = (a2) + (v_rip + 3831853);
    if (((unsigned int)((int)(*(unsigned int *)(result + 24)))) == 6) goto loc_00C629D9;
    if (((unsigned int)((int)(*(unsigned int *)(result + 24)) - 30)) <= 2) goto loc_00C629D9;
    if (((unsigned int)((int)(*(unsigned int *)(result + 24)))) > 44) goto loc_00C629CF;
    if (((unsigned int)((int)(*(unsigned int *)(result + 24)))) < 44) goto loc_00C62A45;
loc_00C629CF:
    if (((unsigned int)((int)(*(unsigned int *)(result + 24)))) == 2) goto loc_00C629DF;
loc_00C629D9:
    if (((unsigned int)((int)(*(unsigned int *)(result + 24)))) != 24) goto loc_00C62A45;
loc_00C629DF:
    if (result < 0x200000ULL) goto loc_00C62A45;
    if (result <= (*(unsigned __int64 *)(a2 + 8))) goto loc_00C62A45;
    v_r15 = (0) | (-1);
    *(unsigned __int64 *)(a2) = v_rdi;
    a4 = 0;
    *(unsigned __int64 *)(a2 + 8) = result;
loc_00C62A04:
    result = (0) << (5);
    if ((*(unsigned __int64 *)(result + v_rip + 3831853 * 1 + 8)) >= v_r15) goto loc_00C62A20;
    if (*(unsigned __int64 *)(result + v_rip + 3831853 * 1 + 8) == 0) goto loc_00C62A45;
loc_00C62A20:
    v_r15 = *(unsigned __int64 *)(result + v_rip + 3831853 * 1 + 8);
    if ((*(unsigned __int64 *)(result + v_rip + 3831853 * 1 + 8)) >= v_r15) { v_r15 = v_r15; }
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rip + 3548624)) - ((unsigned int)((unsigned int)((unsigned int)(v_rbp + 1)))));
    if (0 == ((unsigned int)(a1))) goto loc_00C62A45;
    a2 = (unsigned __int16)((0) + ((unsigned __int16)((unsigned int)((unsigned int)(v_rbp + 1)))));
    if (((unsigned __int16)(a2)) < 64) goto loc_00C62A04;
loc_00C62A45:
    v_rsi = (v_rsi) - (result);
    v_rdi = (v_rdi) + (result);
    v_rbp = 0;
    if (v_rsi != 0) goto loc_00C62984;
loc_00C62A5C:
    if (result != 0) goto loc_00C628D3;
loc_00C62A65:
loc_00C62A80:
    if (0 >= (*(unsigned __int16 *)(v_rip + 3548537))) goto loc_00C62C6C;
loc_00C62A96:
    v_r11 = (0) << (5);
    v_r11 = (v_r11) + (v_rip + 3831632);
    if (*(unsigned __int64 *)(v_r11 + 8) == 0) goto loc_00C62C54;
    if ((*(unsigned __int64 *)(v_r11 + 24)) < 0x300000ULL) goto loc_00C62C54;
    a1 = (*(unsigned __int64 *)(v_r11 + 16) + *(unsigned __int64 *)(v_r11 + 16) * 2) << (4);
    a1 = (a1) >> (10);
    a1 = (a1) & (*(unsigned __int64 *)(v_r11 + 16));
    if (a1 < ((unsigned int)(0x100000ULL))) { a1 = (unsigned int)(0x100000ULL); }
    result = (*(unsigned __int64 *)(v_r11 + 24)) - (*(unsigned __int64 *)(v_r11 + 8));
    if (result >= a1) goto loc_00C62AFE;
    if ((*(unsigned __int64 *)(v_r11 + 24)) <= a1) goto loc_00C62C54;
    v_rdi = (*(unsigned __int64 *)(v_r11 + 24)) - (a1);
loc_00C62AFE:
    result = MiFindDescriptorByPfn(a1, *(unsigned __int64 *)(v_r11), (unsigned int)(0x100000ULL), a4);
    a1 = (*(unsigned __int64 *)(v_r11) + v_rdi * 1) & (0xFFFFFFFFFFFC0000ULL);
    a4 = (*(unsigned __int64 *)(v_r11) + 262143) & (0xFFFFFFFFFFFC0000ULL);
    if (a1 < a4) goto loc_00C62C4D;
    a1 = (a1) - (a4);
    if (a1 < 0x40000ULL) goto loc_00C62C4D;
    v_rdi = (0 + 0 * 2) << (4);
    *(unsigned int *)(v_rdi + v_rip - 12987030 * 1 + 16828904) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 24)));
    *(unsigned __int64 *)(v_rdi + v_rip - 12987030 * 1 + 16828912) = a4;
    *(unsigned __int64 *)(v_rdi + v_rip - 12987030 * 1 + 16828920) = a1;
    if (a4 != (*(unsigned __int64 *)(result + 32))) goto loc_00C62B9D;
    if (a1 != (*(unsigned __int64 *)(result + 32) + *(unsigned __int64 *)(result + 40) * 1)) goto loc_00C62B89;
    result = RtlRbRemoveNode(a1 + 352, result, *(unsigned __int64 *)(result + 40), a4);
    goto loc_00C62C4D;
loc_00C62B89:
    *(unsigned __int64 *)(result + 32) = *(unsigned __int64 *)(result + 32) + a1 + 352 * 1;
loc_00C62B91:
    a3 = (*(unsigned __int64 *)(result + 40)) - (a1 + 352);
    *(unsigned __int64 *)(result + 40) = a3;
    goto loc_00C62C4D;
loc_00C62B9D:
    if (a1 == (*(unsigned __int64 *)(result + 32) + a1 + 352 * 1)) goto loc_00C62B91;
    v_r11 = (v_rip - 12987030 + 16836784) + (v_rdi);
    *(unsigned int *)(v_r11 + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 24)));
    *(unsigned __int64 *)(v_r11 + 32) = *(unsigned __int64 *)(result + 32);
    result = (a4) - (*(unsigned __int64 *)(result + 32));
    *(unsigned __int64 *)(v_r11 + 40) = result;
    result = (*(unsigned __int64 *)(result + 40)) - (a4);
    result = (result) - (a1 + 352);
    result = (result) + (*(unsigned __int64 *)(result + 32));
    *(unsigned __int64 *)(result + 40) = result;
    *(unsigned __int64 *)(result + 32) = a1;
    if (((*(unsigned __int8 *)(a1 + 352 + 8)) & (1)) == 0) goto loc_00C62BF2;
    if (*(unsigned __int64 *)(a1 + 352) == 0) goto loc_00C62BEF;
    a2 = (*(unsigned __int64 *)(a1 + 352)) ^ (a1 + 352);
    goto loc_00C62BF2;
loc_00C62BEF:
loc_00C62BF2:
    a1 = (unsigned int)((*(unsigned __int8 *)(a1 + 352 + 8)) & (1));
    if (0 == 0) goto loc_00C62C42;
loc_00C62C06:
    if ((*(unsigned __int64 *)(v_r11 + 32)) >= (*(unsigned __int64 *)(0 + 32))) goto loc_00C62C25;
    if ((unsigned int)(a1) == 0) goto loc_00C62C1B;
    if (*(unsigned __int64 *)(0) == 0) goto loc_00C62C20;
    result = (*(unsigned __int64 *)(0)) ^ (0);
loc_00C62C1B:
    if (result != 0) goto loc_00C62C3A;
loc_00C62C20:
    goto loc_00C62C42;
loc_00C62C25:
    if ((unsigned int)(a1) == 0) goto loc_00C62C35;
    if (*(unsigned __int64 *)(0 + 8) == 0) goto loc_00C62C3F;
    result = (*(unsigned __int64 *)(0 + 8)) ^ (0);
loc_00C62C35:
    if (result == 0) goto loc_00C62C3F;
loc_00C62C3A:
    goto loc_00C62C06;
loc_00C62C3F:
loc_00C62C42:
    result = RtlRbInsertNodeEx(a1 + 352, result, 1, v_r11);
loc_00C62C4D:
loc_00C62C54:
    v_rbx = (unsigned int)((0) + (1));
    if (((unsigned int)(v_rbx)) < ((unsigned int)(*(unsigned __int16 *)(v_rip + 3548069)))) goto loc_00C62A96;
loc_00C62C6C:
    v_rsp = (v_rsp) + (32);
    return *(unsigned __int16 *)(v_rip + 3548069);
}
```

## 5. (Beta) C Style

```c
int64_t MiRemoveLargeFreeLoaderDescriptors(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    if (condition_is_above_or_equal) goto loc_00C62C6C;
    local_rbp = 0;
    if (((*(uint8_t *)(arg1 + 0x160 + 0x8)) & ((uint8_t)(local_rbp + 1))) == 0) goto loc_00C6289E;
    if (*(uint64_t *)(arg1 + 0x160) == 0) goto loc_00C62A80;
    result = (*(uint64_t *)(arg1 + 0x160)) ^ (Arg1 + 352);
loc_00C6289E:
    if (result == 0) goto loc_00C628C7;
    Arg2 = (uint8_t)((*(uint8_t *)(arg1 + 0x160 + 0x8)) & ((uint8_t)(local_rbp + 1)));
loc_00C628AA:
    if ((uint8_t)(Arg2) == 0) goto loc_00C628BF;
    if (*(uint64_t *)(result + 0x8) == 0) goto loc_00C628BF;
    result = (result) ^ (*(uint64_t *)(result + 0x8));
    goto loc_00C628C2;
loc_00C628BF:
loc_00C628C2:
    if (*(uint64_t *)(result + 0x8) != 0) goto loc_00C628AA;
loc_00C628C7:
    if (result == 0) goto loc_00C62A80;
loc_00C628D3:
    if (*(uint64_t *)(result) == 0) goto loc_00C628FB;
    goto loc_00C628E7;
loc_00C628E3:
loc_00C628E7:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x8)) != 0) goto loc_00C628E3;
    goto loc_00C62905;
loc_00C628F2:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x8)) == result) goto loc_00C62905;
loc_00C628FB:
    local_rbx = (*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x10)) & (-4);
    if (condition_is_not_equal) goto loc_00C628F2;
loc_00C62905:
    if ((*(uint64_t *)(result + 0x28)) >= 0x200000ULL) goto loc_00C62965;
    if ((*(uint64_t *)(result + 0x28) + *(uint64_t *)(result + 0x20) * 1) < 0x300000ULL) goto loc_00C62A65;
    if ((*(uint64_t *)(result + 0x28) + *(uint64_t *)(result + 0x20) * 1) < 0) goto loc_00C62A65;
    local_rdi = (*(uint64_t *)(result + 0x20)) & (0xFFFFFFFFFFFC0000ULL);
    if (local_rdi < ((uint32_t)(0x100000ULL))) goto loc_00C62A65;
    result = MiFindDescriptorByPfn(Arg1, local_rdi - 262144, (uint32_t)(0x100000ULL), Arg4);
    if (result == 0) goto loc_00C62A65;
    goto loc_00C628D3;
loc_00C62965:
    local_rsi = *(uint64_t *)(result + 0x28);
    if (local_rdi < ((uint32_t)(0x100000ULL))) {
        local_rdi = (local_rdi) + (0xFFFFFFFFFFF00000ULL);
        local_rsi = (*(uint64_t *)(result + 0x28)) + (local_rdi);
        local_rdi = (uint32_t)(0x100000ULL);
    }
    if (local_rsi == 0) goto loc_00C62A5C;
loc_00C62984:
    result = MiRestrictRangeToNode(local_rdi, local_rsi, (uint32_t)(0x100000ULL), Arg4);
    result = MiPageToNode(local_rdi, local_rsi, (uint32_t)(0x100000ULL), Arg4);
    Arg2 = ((uint32_t)((uint32_t)(result))) << (5);
    Arg2 = (Arg2) + (v_rip + 3831853);
    if (((uint32_t)((int32_t)(*(uint32_t *)(result + 0x18)))) == 6) goto loc_00C629D9;
    if (((uint32_t)((int32_t)(*(uint32_t *)(result + 0x18)) - 30)) <= 2) goto loc_00C629D9;
    if (((uint32_t)((int32_t)(*(uint32_t *)(result + 0x18)))) > 44) goto loc_00C629CF;
    if (((uint32_t)((int32_t)(*(uint32_t *)(result + 0x18)))) < 44) goto loc_00C62A45;
loc_00C629CF:
    if (((uint32_t)((int32_t)(*(uint32_t *)(result + 0x18)))) == 2) goto loc_00C629DF;
loc_00C629D9:
    if (((uint32_t)((int32_t)(*(uint32_t *)(result + 0x18)))) != 24) goto loc_00C62A45;
loc_00C629DF:
    if (result < 0x200000ULL) goto loc_00C62A45;
    if (result <= (*(uint64_t *)(Arg2 + 0x8))) goto loc_00C62A45;
    local_r15 = (0) | (-1);
    *(uint64_t *)(Arg2) = local_rdi;
    Arg4 = 0;
    *(uint64_t *)(Arg2 + 0x8) = result;
loc_00C62A04:
    result = (0) << (5);
    if ((*(uint64_t *)(result + v_rip + 0x3A782D * 1 + 0x8)) >= local_r15) goto loc_00C62A20;
    if (*(uint64_t *)(result + v_rip + 0x3A782D * 1 + 0x8) == 0) goto loc_00C62A45;
loc_00C62A20:
    local_r15 = *(uint64_t *)(result + v_rip + 0x3A782D * 1 + 0x8);
    if ((*(uint64_t *)(result + v_rip + 0x3A782D * 1 + 0x8)) >= local_r15) { local_r15 = local_r15; }
    Arg1 = (uint32_t)((*(uint16_t *)(v_rip + 0x3625D0)) - ((uint32_t)((uint32_t)((uint32_t)(local_rbp + 1)))));
    if (0 == ((uint32_t)(Arg1))) goto loc_00C62A45;
    Arg2 = (uint16_t)((0) + ((uint16_t)((uint32_t)((uint32_t)(local_rbp + 1)))));
    if (((uint16_t)(Arg2)) < 64) goto loc_00C62A04;
loc_00C62A45:
    local_rsi = (local_rsi) - (result);
    local_rdi = (local_rdi) + (result);
    local_rbp = 0;
    if (local_rsi != 0) goto loc_00C62984;
loc_00C62A5C:
    if (result != 0) goto loc_00C628D3;
loc_00C62A65:
loc_00C62A80:
    if (0 >= (*(uint16_t *)(v_rip + 0x362579))) goto loc_00C62C6C;
loc_00C62A96:
    local_r11 = (0) << (5);
    local_r11 = (local_r11) + (v_rip + 3831632);
    if (*(uint64_t *)(local_r11 + 0x8) == 0) goto loc_00C62C54;
    if ((*(uint64_t *)(local_r11 + 0x18)) < 0x300000ULL) goto loc_00C62C54;
    Arg1 = (*(uint64_t *)(local_r11 + 0x10) + *(uint64_t *)(local_r11 + 0x10) * 2) << (4);
    Arg1 = (Arg1) >> (10);
    Arg1 = (Arg1) & (*(uint64_t *)(local_r11 + 0x10));
    if (Arg1 < ((uint32_t)(0x100000ULL))) { Arg1 = (uint32_t)(0x100000ULL); }
    result = (*(uint64_t *)(local_r11 + 0x18)) - (*(uint64_t *)(local_r11 + 0x8));
    if (result >= Arg1) goto loc_00C62AFE;
    if ((*(uint64_t *)(local_r11 + 0x18)) <= Arg1) goto loc_00C62C54;
    local_rdi = (*(uint64_t *)(local_r11 + 0x18)) - (Arg1);
loc_00C62AFE:
    result = MiFindDescriptorByPfn(Arg1, *(uint64_t *)(local_r11), (uint32_t)(0x100000ULL), Arg4);
    Arg1 = (*(uint64_t *)(local_r11) + local_rdi * 1) & (0xFFFFFFFFFFFC0000ULL);
    Arg4 = (*(uint64_t *)(local_r11) + 262143) & (0xFFFFFFFFFFFC0000ULL);
    if (Arg1 < Arg4) goto loc_00C62C4D;
    Arg1 = (Arg1) - (Arg4);
    if (Arg1 < 0x40000ULL) goto loc_00C62C4D;
    local_rdi = (0 + 0 * 2) << (4);
    *(uint32_t *)(local_rdi + v_rip - 0xC62A96 * 1 + 0x100C9E8) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x18)));
    *(uint64_t *)(local_rdi + v_rip - 0xC62A96 * 1 + 0x100C9F0) = Arg4;
    *(void **)(local_rdi + v_rip - 0xC62A96 * 1 + 0x100C9F8) = Arg1;
    if (Arg4 != (*(uint64_t *)(result + 0x20))) goto loc_00C62B9D;
    if (Arg1 != (*(uint64_t *)(result + 0x20) + *(uint64_t *)(result + 0x28) * 1)) goto loc_00C62B89;
    result = RtlRbRemoveNode(Arg1 + 352, result, *(uint64_t *)(result + 0x28), Arg4);
    goto loc_00C62C4D;
loc_00C62B89:
    *(uint64_t *)(result + 0x20) = *(uint64_t *)(result + 0x20) + Arg1 + 352 * 1;
loc_00C62B91:
    Arg3 = (*(uint64_t *)(result + 0x28)) - (Arg1 + 352);
    *(uint64_t *)(result + 0x28) = Arg3;
    goto loc_00C62C4D;
loc_00C62B9D:
    if (Arg1 == (*(uint64_t *)(result + 0x20) + Arg1 + 352 * 1)) goto loc_00C62B91;
    local_r11 = (v_rip - 12987030 + 16836784) + (local_rdi);
    *(uint32_t *)(local_r11 + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x18)));
    *(uint64_t *)(local_r11 + 0x20) = *(uint64_t *)(result + 0x20);
    result = (Arg4) - (*(uint64_t *)(result + 0x20));
    *(uint64_t *)(local_r11 + 0x28) = result;
    result = (*(uint64_t *)(result + 0x28)) - (Arg4);
    result = (result) - (Arg1 + 352);
    result = (result) + (*(uint64_t *)(result + 0x20));
    *(uint64_t *)(result + 0x28) = result;
    *(void **)(result + 0x20) = Arg1;
    if (((*(uint8_t *)(arg1 + 0x160 + 0x8)) & (1)) == 0) goto loc_00C62BF2;
    if (*(uint64_t *)(arg1 + 0x160) == 0) goto loc_00C62BEF;
    Arg2 = (*(uint64_t *)(arg1 + 0x160)) ^ (Arg1 + 352);
    goto loc_00C62BF2;
loc_00C62BEF:
loc_00C62BF2:
    Arg1 = (uint32_t)((*(uint8_t *)(arg1 + 0x160 + 0x8)) & (1));
    if (0 == 0) goto loc_00C62C42;
loc_00C62C06:
    if ((*(uint64_t *)(local_r11 + 0x20)) >= (*(uint64_t *)(0 + 0x20))) goto loc_00C62C25;
    if ((uint32_t)(Arg1) == 0) goto loc_00C62C1B;
    if (*(uint64_t *)(0) == 0) goto loc_00C62C20;
    result = (*(uint64_t *)(0)) ^ (0);
loc_00C62C1B:
    if (result != 0) goto loc_00C62C3A;
loc_00C62C20:
    goto loc_00C62C42;
loc_00C62C25:
    if ((uint32_t)(Arg1) == 0) goto loc_00C62C35;
    if (*(uint64_t *)(0 + 0x8) == 0) goto loc_00C62C3F;
    result = (*(uint64_t *)(0 + 0x8)) ^ (0);
loc_00C62C35:
    if (result == 0) goto loc_00C62C3F;
loc_00C62C3A:
    goto loc_00C62C06;
loc_00C62C3F:
loc_00C62C42:
    result = RtlRbInsertNodeEx(Arg1 + 352, result, 1, local_r11);
loc_00C62C4D:
loc_00C62C54:
    local_rbx = (uint32_t)((0) + (1));
    if (((uint32_t)(local_rbx)) < ((uint32_t)(*(uint16_t *)(v_rip + 0x3623A5)))) goto loc_00C62A96;
loc_00C62C6C:
    local_rsp = (local_rsp) + (32);
    return *(uint16_t *)(v_rip + 0x3623A5);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x160` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C6283C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
