# sub_00A4991C

- RVA: `0x00A4991C`–`0x00A49D4F` (길이 `1,075` bytes)
- VA: `0x0000000140A4991C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AFEE0`
- 디코드: `297`개 명령, `1,075/1,075` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A499A9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A49B03` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A49B5E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [sub_00968AF6](../96/Unknown_function_00968AF6.md) at `0x00969CA2`

### Static image references
- `0x00A49937` → RVA `0x00E0A740` (`.data`; read)
- `0x00A49AC1` → RVA `0x00FD83C0` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A499A9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A49B03` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A49B5E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A4991C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A49921  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00A49926  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00A4992B  57                              push rdi
00A4992C  41 56                           push r14
00A4992E  41 57                           push r15
00A49930  48 81 EC 80 00 00 00            sub rsp, 0x80
00A49937  48 8B 05 02 0E 3C 00            mov rax, qword ptr [rip + 0x3c0e02]
00A4993E  48 33 C4                        xor rax, rsp
00A49941  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00A49946  49 8B F9                        mov rdi, r9
00A49949  4C 8B FA                        mov r15, rdx
00A4994C  4C 8B C1                        mov r8, rcx
00A4994F  48 85 C9                        test rcx, rcx
00A49952  0F 84 E9 02 00 00               je 0x140a49c41
00A49958  48 85 D2                        test rdx, rdx
00A4995B  0F 84 E0 02 00 00               je 0x140a49c41
00A49961  4D 85 C9                        test r9, r9
00A49964  0F 84 D7 02 00 00               je 0x140a49c41
00A4996A  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
00A4996E  48 85 D2                        test rdx, rdx
00A49971  0F 84 CA 02 00 00               je 0x140a49c41
00A49977  83 39 03                        cmp dword ptr [rcx], 3
00A4997A  0F 86 C1 02 00 00               jbe 0x140a49c41
00A49980  48 8B C2                        mov rax, rdx
00A49983  45 33 C9                        xor r9d, r9d
00A49986  44 8B 10                        mov r10d, dword ptr [rax]
00A49989  48 8D 48 04                     lea rcx, [rax + 4]
00A4998D  41 83 F9 03                     cmp r9d, 3
00A49991  73 47                           jae 0x140a499da
00A49993  48 3B C8                        cmp rcx, rax
00A49996  73 34                           jae 0x140a499cc
00A49998  41 B8 95 00 00 C0               mov r8d, 0xc0000095
00A4999E  41 8B C0                        mov eax, r8d
00A499A1  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00A499A6  48 33 CC                        xor rcx, rsp
00A499A9  E8 92 2C C6 FF                  call 0x1406ac640
00A499AE  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
00A499B6  49 8B 5B 20                     mov rbx, qword ptr [r11 + 0x20]
00A499BA  49 8B 6B 28                     mov rbp, qword ptr [r11 + 0x28]
00A499BE  49 8B 73 30                     mov rsi, qword ptr [r11 + 0x30]
00A499C2  49 8B E3                        mov rsp, r11
00A499C5  41 5F                           pop r15
00A499C7  41 5E                           pop r14
00A499C9  5F                              pop rdi
00A499CA  C3                              ret
00A499CB  CC                              int3
00A499CC  4A 8D 04 11                     lea rax, [rcx + r10]
00A499D0  48 3B C1                        cmp rax, rcx
00A499D3  72 C3                           jb 0x140a49998
00A499D5  41 FF C1                        inc r9d
00A499D8  EB AC                           jmp 0x140a49986
00A499DA  48 3B C8                        cmp rcx, rax
00A499DD  72 B9                           jb 0x140a49998
00A499DF  33 F6                           xor esi, esi
00A499E1  45 85 D2                        test r10d, r10d
00A499E4  48 0F 45 F1                     cmovne rsi, rcx
00A499E8  41 83 FA 08                     cmp r10d, 8
00A499EC  0F 85 3F 03 00 00               jne 0x140a49d31
00A499F2  41 83 38 04                     cmp dword ptr [r8], 4
00A499F6  48 8B 36                        mov rsi, qword ptr [rsi]
00A499F9  0F 86 42 02 00 00               jbe 0x140a49c41
00A499FF  48 8B C2                        mov rax, rdx
00A49A02  45 33 C9                        xor r9d, r9d
00A49A05  44 8B 10                        mov r10d, dword ptr [rax]
00A49A08  48 8D 48 04                     lea rcx, [rax + 4]
00A49A0C  41 83 F9 04                     cmp r9d, 4
00A49A10  73 17                           jae 0x140a49a29
00A49A12  48 3B C8                        cmp rcx, rax
00A49A15  72 81                           jb 0x140a49998
00A49A17  4A 8D 04 11                     lea rax, [rcx + r10]
00A49A1B  48 3B C1                        cmp rax, rcx
00A49A1E  0F 82 74 FF FF FF               jb 0x140a49998
00A49A24  41 FF C1                        inc r9d
00A49A27  EB DC                           jmp 0x140a49a05
00A49A29  48 3B C8                        cmp rcx, rax
00A49A2C  0F 82 66 FF FF FF               jb 0x140a49998
00A49A32  45 33 DB                        xor r11d, r11d
00A49A35  45 85 D2                        test r10d, r10d
00A49A38  4C 0F 45 D9                     cmovne r11, rcx
00A49A3C  41 83 38 05                     cmp dword ptr [r8], 5
00A49A40  0F 86 FB 01 00 00               jbe 0x140a49c41
00A49A46  48 8B C2                        mov rax, rdx
00A49A49  45 33 C9                        xor r9d, r9d
00A49A4C  8B 28                           mov ebp, dword ptr [rax]
00A49A4E  48 8D 48 04                     lea rcx, [rax + 4]
00A49A52  41 83 F9 05                     cmp r9d, 5
00A49A56  73 1B                           jae 0x140a49a73
00A49A58  48 3B C8                        cmp rcx, rax
00A49A5B  0F 82 37 FF FF FF               jb 0x140a49998
00A49A61  48 8D 04 29                     lea rax, [rcx + rbp]
00A49A65  48 3B C1                        cmp rax, rcx
00A49A68  0F 82 2A FF FF FF               jb 0x140a49998
00A49A6E  41 FF C1                        inc r9d
00A49A71  EB D9                           jmp 0x140a49a4c
00A49A73  48 3B C8                        cmp rcx, rax
00A49A76  0F 82 1C FF FF FF               jb 0x140a49998
00A49A7C  33 DB                           xor ebx, ebx
00A49A7E  85 ED                           test ebp, ebp
00A49A80  48 0F 45 D9                     cmovne rbx, rcx
00A49A84  41 83 38 06                     cmp dword ptr [r8], 6
00A49A88  0F 86 B3 01 00 00               jbe 0x140a49c41
00A49A8E  45 33 C0                        xor r8d, r8d
00A49A91  8B 02                           mov eax, dword ptr [rdx]
00A49A93  48 8D 4A 04                     lea rcx, [rdx + 4]
00A49A97  41 83 F8 06                     cmp r8d, 6
00A49A9B  73 1B                           jae 0x140a49ab8
00A49A9D  48 3B CA                        cmp rcx, rdx
00A49AA0  0F 82 F2 FE FF FF               jb 0x140a49998
00A49AA6  48 8D 14 01                     lea rdx, [rcx + rax]
00A49AAA  48 3B D1                        cmp rdx, rcx
00A49AAD  0F 82 E5 FE FF FF               jb 0x140a49998
00A49AB3  41 FF C0                        inc r8d
00A49AB6  EB D9                           jmp 0x140a49a91
00A49AB8  48 3B CA                        cmp rcx, rdx
00A49ABB  0F 82 D7 FE FF FF               jb 0x140a49998
00A49AC1  4C 8B 35 F8 E8 58 00            mov r14, qword ptr [rip + 0x58e8f8]
00A49AC8  33 D2                           xor edx, edx
00A49ACA  85 C0                           test eax, eax
00A49ACC  48 0F 45 D1                     cmovne rdx, rcx
00A49AD0  4D 85 F6                        test r14, r14
00A49AD3  0F 84 73 01 00 00               je 0x140a49c4c
00A49AD9  C7 44 24 38 20 00 00 00         mov dword ptr [rsp + 0x38], 0x20
00A49AE1  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00A49AE6  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00A49AEB  44 8B CD                        mov r9d, ebp
00A49AEE  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00A49AF2  4C 8B C3                        mov r8, rbx
00A49AF5  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00A49AFA  49 8B CB                        mov rcx, r11
00A49AFD  41 8B D2                        mov edx, r10d
00A49B00  49 8B C6                        mov rax, r14
00A49B03  E8 C8 0F C7 FF                  call 0x1406baad0
00A49B08  44 8B C0                        mov r8d, eax
00A49B0B  85 C0                           test eax, eax
00A49B0D  0F 88 8B FE FF FF               js 0x140a4999e
00A49B13  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
00A49B17  41 8B 57 20                     mov edx, dword ptr [r15 + 0x20]
00A49B1B  83 C0 50                        add eax, 0x50
00A49B1E  83 F8 50                        cmp eax, 0x50
00A49B21  0F 82 71 FE FF FF               jb 0x140a49998
00A49B27  8D 48 04                        lea ecx, [rax + 4]
00A49B2A  41 8B E8                        mov ebp, r8d
00A49B2D  3B C8                           cmp ecx, eax
00A49B2F  0F 82 63 FE FF FF               jb 0x140a49998
00A49B35  8D 04 11                        lea eax, [rcx + rdx]
00A49B38  BB 95 00 00 C0                  mov ebx, 0xc0000095
00A49B3D  3B C1                           cmp eax, ecx
00A49B3F  45 1B C0                        sbb r8d, r8d
00A49B42  44 23 C3                        and r8d, ebx
00A49B45  0F 8C 53 FE FF FF               jl 0x140a4999e
00A49B4B  BA 38 00 00 00                  mov edx, 0x38
00A49B50  B9 00 01 00 00                  mov ecx, 0x100
00A49B55  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00A49B5B  89 57 04                        mov dword ptr [rdi + 4], edx
00A49B5E  E8 8D 85 13 00                  call 0x140b820f0
00A49B63  48 85 C0                        test rax, rax
00A49B66  0F 84 D8 01 00 00               je 0x140a49d44
00A49B6C  48 89 47 08                     mov qword ptr [rdi + 8], rax
00A49B70  83 27 00                        and dword ptr [rdi], 0
00A49B73  0F BA ED 1C                     bts ebp, 0x1c
00A49B77  48 8B D0                        mov rdx, rax
00A49B7A  48 85 C0                        test rax, rax
00A49B7D  0F 84 73 01 00 00               je 0x140a49cf6
00A49B83  44 8B 0F                        mov r9d, dword ptr [rdi]
00A49B86  33 C9                           xor ecx, ecx
00A49B88  41 3B C9                        cmp ecx, r9d
00A49B8B  73 16                           jae 0x140a49ba3
00A49B8D  8B 02                           mov eax, dword ptr [rdx]
00A49B8F  83 C0 04                        add eax, 4
00A49B92  83 F8 04                        cmp eax, 4
00A49B95  0F 83 8D 00 00 00               jae 0x140a49c28
00A49B9B  44 8B C3                        mov r8d, ebx
00A49B9E  E9 FB FD FF FF                  jmp 0x140a4999e
00A49BA3  4C 8D 42 04                     lea r8, [rdx + 4]
00A49BA7  4C 3B C2                        cmp r8, rdx
00A49BAA  72 EF                           jb 0x140a49b9b
00A49BAC  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00A49BAF  48 8D 42 08                     lea rax, [rdx + 8]
00A49BB3  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
00A49BB7  48 3B C1                        cmp rax, rcx
00A49BBA  0F 87 71 01 00 00               ja 0x140a49d31
00A49BC0  C7 02 04 00 00 00               mov dword ptr [rdx], 4
00A49BC6  41 89 28                        mov dword ptr [r8], ebp
00A49BC9  FF 07                           inc dword ptr [rdi]
00A49BCB  41 83 C9 FF                     or r9d, 0xffffffff
00A49BCF  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00A49BD3  48 85 D2                        test rdx, rdx
00A49BD6  74 7F                           je 0x140a49c57
00A49BD8  44 8B 17                        mov r10d, dword ptr [rdi]
00A49BDB  33 C9                           xor ecx, ecx
00A49BDD  41 3B CA                        cmp ecx, r10d
00A49BE0  73 1C                           jae 0x140a49bfe
00A49BE2  8B 02                           mov eax, dword ptr [rdx]
00A49BE4  83 C0 04                        add eax, 4
00A49BE7  83 F8 04                        cmp eax, 4
00A49BEA  72 AF                           jb 0x140a49b9b
00A49BEC  44 8B C0                        mov r8d, eax
00A49BEF  4C 03 C2                        add r8, rdx
00A49BF2  4C 3B C2                        cmp r8, rdx
00A49BF5  72 A4                           jb 0x140a49b9b
00A49BF7  49 8B D0                        mov rdx, r8
00A49BFA  FF C1                           inc ecx
00A49BFC  EB DF                           jmp 0x140a49bdd
00A49BFE  4C 8D 42 04                     lea r8, [rdx + 4]
00A49C02  4C 3B C2                        cmp r8, rdx
00A49C05  72 94                           jb 0x140a49b9b
00A49C07  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00A49C0A  48 8D 42 0C                     lea rax, [rdx + 0xc]
00A49C0E  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
00A49C12  48 3B C1                        cmp rax, rcx
00A49C15  0F 87 16 01 00 00               ja 0x140a49d31
00A49C1B  C7 02 08 00 00 00               mov dword ptr [rdx], 8
00A49C21  49 89 30                        mov qword ptr [r8], rsi
00A49C24  FF 07                           inc dword ptr [rdi]
00A49C26  EB 53                           jmp 0x140a49c7b
00A49C28  44 8B C0                        mov r8d, eax
00A49C2B  4C 03 C2                        add r8, rdx
00A49C2E  4C 3B C2                        cmp r8, rdx
00A49C31  0F 82 64 FF FF FF               jb 0x140a49b9b
00A49C37  49 8B D0                        mov rdx, r8
00A49C3A  FF C1                           inc ecx
00A49C3C  E9 47 FF FF FF                  jmp 0x140a49b88
00A49C41  41 B8 0D 00 00 C0               mov r8d, 0xc000000d
00A49C47  E9 52 FD FF FF                  jmp 0x140a4999e
00A49C4C  41 B8 BB 00 00 C0               mov r8d, 0xc00000bb
00A49C52  E9 47 FD FF FF                  jmp 0x140a4999e
00A49C57  8B 57 04                        mov edx, dword ptr [rdi + 4]
00A49C5A  41 8B C1                        mov eax, r9d
00A49C5D  8D 4A 0C                        lea ecx, [rdx + 0xc]
00A49C60  3B CA                           cmp ecx, edx
00A49C62  0F 43 C1                        cmovae eax, ecx
00A49C65  45 1B C0                        sbb r8d, r8d
00A49C68  44 23 C3                        and r8d, ebx
00A49C6B  89 47 04                        mov dword ptr [rdi + 4], eax
00A49C6E  3B CA                           cmp ecx, edx
00A49C70  73 B2                           jae 0x140a49c24
00A49C72  45 85 C0                        test r8d, r8d
00A49C75  0F 88 23 FD FF FF               js 0x140a4999e
00A49C7B  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00A49C7F  48 85 D2                        test rdx, rdx
00A49C82  0F 84 81 00 00 00               je 0x140a49d09
00A49C88  44 8B 0F                        mov r9d, dword ptr [rdi]
00A49C8B  33 C9                           xor ecx, ecx
00A49C8D  41 3B C9                        cmp ecx, r9d
00A49C90  73 24                           jae 0x140a49cb6
00A49C92  8B 02                           mov eax, dword ptr [rdx]
00A49C94  83 C0 04                        add eax, 4
00A49C97  83 F8 04                        cmp eax, 4
00A49C9A  0F 82 FB FE FF FF               jb 0x140a49b9b
00A49CA0  44 8B C0                        mov r8d, eax
00A49CA3  4C 03 C2                        add r8, rdx
00A49CA6  4C 3B C2                        cmp r8, rdx
00A49CA9  0F 82 EC FE FF FF               jb 0x140a49b9b
00A49CAF  49 8B D0                        mov rdx, r8
00A49CB2  FF C1                           inc ecx
00A49CB4  EB D7                           jmp 0x140a49c8d
00A49CB6  4C 8D 4A 04                     lea r9, [rdx + 4]
00A49CBA  4C 3B CA                        cmp r9, rdx
00A49CBD  0F 82 D8 FE FF FF               jb 0x140a49b9b
00A49CC3  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00A49CC6  48 8D 42 24                     lea rax, [rdx + 0x24]
00A49CCA  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
00A49CCE  45 33 C0                        xor r8d, r8d
00A49CD1  48 3B C1                        cmp rax, rcx
00A49CD4  77 5B                           ja 0x140a49d31
00A49CD6  C7 02 20 00 00 00               mov dword ptr [rdx], 0x20
00A49CDC  0F 10 44 24 50                  movups xmm0, xmmword ptr [rsp + 0x50]
00A49CE1  41 0F 11 01                     movups xmmword ptr [r9], xmm0
00A49CE5  0F 10 4C 24 60                  movups xmm1, xmmword ptr [rsp + 0x60]
00A49CEA  41 0F 11 49 10                  movups xmmword ptr [r9 + 0x10], xmm1
00A49CEF  FF 07                           inc dword ptr [rdi]
00A49CF1  E9 A8 FC FF FF                  jmp 0x140a4999e
00A49CF6  8B 47 04                        mov eax, dword ptr [rdi + 4]
00A49CF9  8D 48 08                        lea ecx, [rax + 8]
00A49CFC  3B C8                           cmp ecx, eax
00A49CFE  73 3C                           jae 0x140a49d3c
00A49D00  83 4F 04 FF                     or dword ptr [rdi + 4], 0xffffffff
00A49D04  E9 92 FE FF FF                  jmp 0x140a49b9b
00A49D09  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00A49D0C  8D 41 24                        lea eax, [rcx + 0x24]
00A49D0F  3B C1                           cmp eax, ecx
00A49D11  44 0F 43 C8                     cmovae r9d, eax
00A49D15  45 1B C0                        sbb r8d, r8d
00A49D18  44 23 C3                        and r8d, ebx
00A49D1B  44 89 4F 04                     mov dword ptr [rdi + 4], r9d
00A49D1F  3B C1                           cmp eax, ecx
00A49D21  0F 82 77 FC FF FF               jb 0x140a4999e
00A49D27  FF 07                           inc dword ptr [rdi]
00A49D29  45 33 C0                        xor r8d, r8d
00A49D2C  E9 6D FC FF FF                  jmp 0x140a4999e
00A49D31  41 B8 23 00 00 C0               mov r8d, 0xc0000023
00A49D37  E9 62 FC FF FF                  jmp 0x140a4999e
00A49D3C  89 4F 04                        mov dword ptr [rdi + 4], ecx
00A49D3F  E9 85 FE FF FF                  jmp 0x140a49bc9
00A49D44  41 B8 17 00 00 C0               mov r8d, 0xc0000017
00A49D4A  E9 4F FC FF FF                  jmp 0x140a4999e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00A4991C(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 3935746)) ^ (v_rsp);
    v_stack_m28 = result;
    if (a1 == 0) goto loc_00A49C41;
    if (a2 == 0) goto loc_00A49C41;
    if (a4 == 0) goto loc_00A49C41;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00A49C41;
    if ((*(unsigned int *)(a1)) <= 3) goto loc_00A49C41;
    a4 = 0;
loc_00A49986:
    if (0 >= 3) goto loc_00A499DA;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) >= (*(unsigned __int64 *)(a1 + 8))) goto loc_00A499CC;
loc_00A49998:
loc_00A4999E:
    a1 = (v_stack_m28) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(a1 + 8), (unsigned int)(0xC0000095ULL), a4);
    return result;
loc_00A499CC:
    if ((a1 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < a1) goto loc_00A49998;
    a4 = (unsigned int)((a4) + 1);
    goto loc_00A49986;
loc_00A499DA:
    if (a1 < (a1 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A49998;
    v_rsi = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rsi = a1; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_00A49D31;
    if ((*(unsigned int *)((unsigned int)(0xC0000095ULL))) <= 4) goto loc_00A49C41;
    a4 = 0;
loc_00A49A05:
    if (0 >= 4) goto loc_00A49A29;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00A49998;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00A49998;
    a4 = (unsigned int)((a4) + 1);
    goto loc_00A49A05;
loc_00A49A29:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A49998;
    v_r11 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_r11 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if ((*(unsigned int *)((unsigned int)(0xC0000095ULL))) <= 5) goto loc_00A49C41;
    a4 = 0;
loc_00A49A4C:
    if (0 >= 5) goto loc_00A49A73;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00A49998;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00A49998;
    a4 = (unsigned int)((a4) + 1);
    goto loc_00A49A4C;
loc_00A49A73:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A49998;
    v_rbx = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rbx = *(unsigned __int64 *)(a1 + 8) + 4; }
    if ((*(unsigned int *)((unsigned int)(0xC0000095ULL))) <= 6) goto loc_00A49C41;
    a3 = 0;
loc_00A49A91:
    if (0 >= 6) goto loc_00A49AB8;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00A49998;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00A49998;
    a3 = (unsigned int)((a3) + 1);
    goto loc_00A49A91;
loc_00A49AB8:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00A49998;
    a2 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { a2 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (*(unsigned __int64 *)(v_rip + 5826808) == 0) goto loc_00A49C4C;
    v_stack_m48 = 32;
    v_stack_m50 = v_stack_m30;
    v_stack_m58 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))));
    v_stack_m60 = a2;
    result = guard_dispatch_icall(v_r11, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))), v_rbx, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))));
    if (sign_flag) goto loc_00A4999E;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16))) + (80));
    if (((unsigned int)(result)) < 80) goto loc_00A49998;
    if (((unsigned int)(result + 4)) < ((unsigned int)(result))) goto loc_00A49998;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(result))) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    if (condition_is_less) goto loc_00A4999E;
    *(unsigned int *)(a4 + 4) = 56;
    result = ExAllocatePool2(256, 56, (unsigned int)(0x20534C53ULL), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))));
    if (result == 0) goto loc_00A49D44;
    *(unsigned __int64 *)(a4 + 8) = result;
    if (result == 0) goto loc_00A49CF6;
    a1 = 0;
loc_00A49B88:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00A49BA3;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result))) + (4));
    if (((unsigned int)(result)) >= 4) goto loc_00A49C28;
loc_00A49B9B:
    goto loc_00A4999E;
loc_00A49BA3:
    if ((result + 4) < result) goto loc_00A49B9B;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((result + 8) > a1) goto loc_00A49D31;
    *(unsigned int *)(result) = 4;
    *(unsigned int *)(result + 4) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
loc_00A49BC9:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) | (0xFFFFFFFFULL));
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_00A49C57;
    a1 = 0;
loc_00A49BDD:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00A49BFE;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00A49B9B;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00A49B9B;
    a1 = (unsigned int)((a1) + 1);
    goto loc_00A49BDD;
loc_00A49BFE:
    if ((a3 + 4) < a3) goto loc_00A49B9B;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 12) > a1) goto loc_00A49D31;
    *(unsigned int *)(a3) = 8;
    *(unsigned __int64 *)(a3 + 4) = *(unsigned __int64 *)(v_rsi);
loc_00A49C24:
    goto loc_00A49C7B;
loc_00A49C28:
    a3 = ((unsigned int)((unsigned int)(a3 + 12))) + (a3);
    if (a3 < a3) goto loc_00A49B9B;
    a1 = (unsigned int)((a1) + 1);
    goto loc_00A49B88;
loc_00A49C41:
    goto loc_00A4999E;
loc_00A49C4C:
    goto loc_00A4999E;
loc_00A49C57:
    result = (unsigned int)((unsigned int)(a4));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { result = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12); }
    a3 = (unsigned int)(((unsigned int)(0xC00000BBULL)) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    *(unsigned int *)(a4 + 4) = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00A49C24;
    if (sign_flag) goto loc_00A4999E;
loc_00A49C7B:
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_00A49D09;
    a1 = 0;
loc_00A49C8D:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00A49CB6;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00A49B9B;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00A49B9B;
    a1 = (unsigned int)((a1) + 1);
    goto loc_00A49C8D;
loc_00A49CB6:
    if ((a3 + 4) < a3) goto loc_00A49B9B;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    a3 = 0;
    if ((a3 + 36) > a1) goto loc_00A49D31;
    *(unsigned int *)(a3) = 32;
    *(unsigned __int64 *)(a3 + 4) = v_xmm0;
    *(unsigned __int64 *)(a3 + 4 + 16) = v_xmm1;
    goto loc_00A4999E;
loc_00A49CF6:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00A49D3C;
    goto loc_00A49B9B;
loc_00A49D09:
    a4 = a3 + 4;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 36)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { a4 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 36); }
    a3 = (unsigned int)((a3) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    *(unsigned int *)(a4 + 4) = (unsigned int)(a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 36)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00A4999E;
    a3 = 0;
    goto loc_00A4999E;
loc_00A49D31:
    goto loc_00A4999E;
loc_00A49D3C:
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)));
    goto loc_00A49BC9;
loc_00A49D44:
    goto loc_00A4999E;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00A4991C(void *Arg1, void *Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r11;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0x3C0E02)) ^ (local_rsp);
    v_stack_m28 = result;
    if (Arg1 == NULL) goto loc_00A49C41;
    if (Arg2 == NULL) goto loc_00A49C41;
    if (Arg4 == NULL) goto loc_00A49C41;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00A49C41;
    if ((*(uint32_t *)(arg1)) <= 3) goto loc_00A49C41;
    Arg4 = 0;
loc_00A49986:
    if (0 >= 3) goto loc_00A499DA;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) >= (*(uint64_t *)(arg1 + 0x8))) goto loc_00A499CC;
loc_00A49998:
loc_00A4999E:
    Arg1 = (v_stack_m28) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(arg1 + 0x8), (uint32_t)(0xC0000095ULL), Arg4);
    return result;
loc_00A499CC:
    if ((Arg1 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < Arg1) goto loc_00A49998;
    Arg4 = (uint32_t)((Arg4) + 1);
    goto loc_00A49986;
loc_00A499DA:
    if (Arg1 < (Arg1 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A49998;
    local_rsi = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rsi = Arg1; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 8) goto loc_00A49D31;
    if ((*(uint32_t *)((uint32_t)(0xC0000095ULL))) <= 4) goto loc_00A49C41;
    Arg4 = 0;
loc_00A49A05:
    if (0 >= 4) goto loc_00A49A29;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00A49998;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00A49998;
    Arg4 = (uint32_t)((Arg4) + 1);
    goto loc_00A49A05;
loc_00A49A29:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A49998;
    local_r11 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_r11 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if ((*(uint32_t *)((uint32_t)(0xC0000095ULL))) <= 5) goto loc_00A49C41;
    Arg4 = 0;
loc_00A49A4C:
    if (0 >= 5) goto loc_00A49A73;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00A49998;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00A49998;
    Arg4 = (uint32_t)((Arg4) + 1);
    goto loc_00A49A4C;
loc_00A49A73:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A49998;
    local_rbx = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rbx = *(uint64_t *)(arg1 + 0x8) + 4; }
    if ((*(uint32_t *)((uint32_t)(0xC0000095ULL))) <= 6) goto loc_00A49C41;
    Arg3 = 0;
loc_00A49A91:
    if (0 >= 6) goto loc_00A49AB8;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00A49998;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00A49998;
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_00A49A91;
loc_00A49AB8:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00A49998;
    Arg2 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { Arg2 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (*(uint64_t *)(v_rip + 0x58E8F8) == 0) goto loc_00A49C4C;
    v_stack_m48 = 32;
    v_stack_m50 = v_stack_m30;
    v_stack_m58 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))));
    v_stack_m60 = Arg2;
    result = guard_dispatch_icall(local_r11, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))), local_rbx, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))));
    if (sign_flag) goto loc_00A4999E;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x10))) + (80));
    if (((uint32_t)(result)) < 80) goto loc_00A49998;
    if (((uint32_t)(result + 4)) < ((uint32_t)(result))) goto loc_00A49998;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(result))) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    if (condition_is_less) goto loc_00A4999E;
    *(uint32_t *)(arg4 + 0x4) = 56;
    result = ExAllocatePool2(256, 56, (uint32_t)(0x20534C53ULL), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))));
    if (result == 0) goto loc_00A49D44;
    *(uint64_t *)(arg4 + 0x8) = result;
    if (result == 0) goto loc_00A49CF6;
    Arg1 = 0;
loc_00A49B88:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) goto loc_00A49BA3;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result))) + (4));
    if (((uint32_t)(result)) >= 4) goto loc_00A49C28;
loc_00A49B9B:
    goto loc_00A4999E;
loc_00A49BA3:
    if ((result + 4) < result) goto loc_00A49B9B;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg4 + 0x4))) + (*(uint64_t *)(arg4 + 0x8));
    if ((result + 8) > Arg1) goto loc_00A49D31;
    *(uint32_t *)(result) = 4;
    *(uint32_t *)(result + 0x4) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
loc_00A49BC9:
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4))) | (0xFFFFFFFFULL));
    if (*(uint64_t *)(arg4 + 0x8) == 0) goto loc_00A49C57;
    Arg1 = 0;
loc_00A49BDD:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) goto loc_00A49BFE;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00A49B9B;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(arg4 + 0x8))) goto loc_00A49B9B;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_00A49BDD;
loc_00A49BFE:
    if ((Arg3 + 4) < Arg3) goto loc_00A49B9B;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg4 + 0x4))) + (*(uint64_t *)(arg4 + 0x8));
    if ((Arg3 + 12) > Arg1) goto loc_00A49D31;
    *(uint32_t *)(Arg3) = 8;
    *(uint64_t *)(Arg3 + 0x4) = *(uint64_t *)(local_rsi);
loc_00A49C24:
    goto loc_00A49C7B;
loc_00A49C28:
    Arg3 = ((uint32_t)((uint32_t)(Arg3 + 12))) + (Arg3);
    if (Arg3 < Arg3) goto loc_00A49B9B;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_00A49B88;
loc_00A49C41:
    goto loc_00A4999E;
loc_00A49C4C:
    goto loc_00A4999E;
loc_00A49C57:
    result = (uint32_t)((uint32_t)(Arg4));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 12)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) { result = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 12); }
    Arg3 = (uint32_t)(((uint32_t)(0xC00000BBULL)) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 12)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) goto loc_00A49C24;
    if (sign_flag) goto loc_00A4999E;
loc_00A49C7B:
    if (*(uint64_t *)(arg4 + 0x8) == 0) goto loc_00A49D09;
    Arg1 = 0;
loc_00A49C8D:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) goto loc_00A49CB6;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00A49B9B;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(arg4 + 0x8))) goto loc_00A49B9B;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_00A49C8D;
loc_00A49CB6:
    if ((Arg3 + 4) < Arg3) goto loc_00A49B9B;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg4 + 0x4))) + (*(uint64_t *)(arg4 + 0x8));
    Arg3 = 0;
    if ((Arg3 + 36) > Arg1) goto loc_00A49D31;
    *(uint32_t *)(Arg3) = 32;
    *(uint64_t *)(Arg3 + 0x4) = v_xmm0;
    *(uint64_t *)(Arg3 + 0x4 + 0x10) = v_xmm1;
    goto loc_00A4999E;
loc_00A49CF6:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 8)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) goto loc_00A49D3C;
    goto loc_00A49B9B;
loc_00A49D09:
    Arg4 = Arg3 + 4;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 36)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) { Arg4 = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 36); }
    Arg3 = (uint32_t)((Arg3) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)(Arg4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)) + 36)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))))) goto loc_00A4999E;
    Arg3 = 0;
    goto loc_00A4999E;
loc_00A49D31:
    goto loc_00A4999E;
loc_00A49D3C:
    *(uint32_t *)(arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)));
    goto loc_00A49BC9;
loc_00A49D44:
    goto loc_00A4999E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x20` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R/W` |
| `Arg4` | `+ 0x4` | `32` | `R` |
| `Arg4` | `+ 0x4` | `32` | `R/W` |
| `Arg4` | `+ 0x4` | `32` | `W` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A4991C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
