# sub_00ADBBE8

- RVA: `0x00ADBBE8`–`0x00ADBFEE` (길이 `1,030` bytes)
- VA: `0x0000000140ADBBE8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BF640`
- 디코드: `293`개 명령, `1,030/1,030` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00ADBD9D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00ADBDF8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ADBFD0` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_00968AF6](../96/Unknown_function_00968AF6.md) at `0x0096A8E0`

### Static image references
- `0x00ADBBFD` → RVA `0x00E0A740` (`.data`; read)
- `0x00ADBD60` → RVA `0x00FD83C0` (`PAGEDATA`; read)
- `0x00ADBD6E` → RVA `0x00FD8438` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00ADBD9D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00ADBDF8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ADBFD0` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ADBBE8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00ADBBED  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00ADBBF2  56                              push rsi
00ADBBF3  57                              push rdi
00ADBBF4  41 56                           push r14
00ADBBF6  48 81 EC 80 00 00 00            sub rsp, 0x80
00ADBBFD  48 8B 05 3C EB 32 00            mov rax, qword ptr [rip + 0x32eb3c]
00ADBC04  48 33 C4                        xor rax, rsp
00ADBC07  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00ADBC0C  49 8B F9                        mov rdi, r9
00ADBC0F  4C 8B F2                        mov r14, rdx
00ADBC12  4C 8B C1                        mov r8, rcx
00ADBC15  48 85 C9                        test rcx, rcx
00ADBC18  75 0B                           jne 0x140adbc25
00ADBC1A  41 B8 0D 00 00 C0               mov r8d, 0xc000000d
00ADBC20  E9 A0 03 00 00                  jmp 0x140adbfc5
00ADBC25  4D 85 F6                        test r14, r14
00ADBC28  74 F0                           je 0x140adbc1a
00ADBC2A  48 85 FF                        test rdi, rdi
00ADBC2D  74 EB                           je 0x140adbc1a
00ADBC2F  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
00ADBC33  48 85 D2                        test rdx, rdx
00ADBC36  74 E2                           je 0x140adbc1a
00ADBC38  83 39 03                        cmp dword ptr [rcx], 3
00ADBC3B  76 DD                           jbe 0x140adbc1a
00ADBC3D  48 8B C2                        mov rax, rdx
00ADBC40  45 33 C9                        xor r9d, r9d
00ADBC43  44 8B 10                        mov r10d, dword ptr [rax]
00ADBC46  48 8D 48 04                     lea rcx, [rax + 4]
00ADBC4A  41 83 F9 03                     cmp r9d, 3
00ADBC4E  73 1B                           jae 0x140adbc6b
00ADBC50  48 3B C8                        cmp rcx, rax
00ADBC53  0F 82 66 03 00 00               jb 0x140adbfbf
00ADBC59  4A 8D 04 11                     lea rax, [rcx + r10]
00ADBC5D  48 3B C1                        cmp rax, rcx
00ADBC60  0F 82 59 03 00 00               jb 0x140adbfbf
00ADBC66  41 FF C1                        inc r9d
00ADBC69  EB D8                           jmp 0x140adbc43
00ADBC6B  48 3B C8                        cmp rcx, rax
00ADBC6E  0F 82 4B 03 00 00               jb 0x140adbfbf
00ADBC74  33 F6                           xor esi, esi
00ADBC76  45 85 D2                        test r10d, r10d
00ADBC79  48 0F 45 F1                     cmovne rsi, rcx
00ADBC7D  41 83 FA 08                     cmp r10d, 8
00ADBC81  0F 85 7D 02 00 00               jne 0x140adbf04
00ADBC87  41 83 38 04                     cmp dword ptr [r8], 4
00ADBC8B  48 8B 36                        mov rsi, qword ptr [rsi]
00ADBC8E  76 8A                           jbe 0x140adbc1a
00ADBC90  48 8B C2                        mov rax, rdx
00ADBC93  45 33 C9                        xor r9d, r9d
00ADBC96  44 8B 10                        mov r10d, dword ptr [rax]
00ADBC99  48 8D 48 04                     lea rcx, [rax + 4]
00ADBC9D  41 83 F9 04                     cmp r9d, 4
00ADBCA1  73 1B                           jae 0x140adbcbe
00ADBCA3  48 3B C8                        cmp rcx, rax
00ADBCA6  0F 82 13 03 00 00               jb 0x140adbfbf
00ADBCAC  4A 8D 04 11                     lea rax, [rcx + r10]
00ADBCB0  48 3B C1                        cmp rax, rcx
00ADBCB3  0F 82 06 03 00 00               jb 0x140adbfbf
00ADBCB9  41 FF C1                        inc r9d
00ADBCBC  EB D8                           jmp 0x140adbc96
00ADBCBE  48 3B C8                        cmp rcx, rax
00ADBCC1  0F 82 F8 02 00 00               jb 0x140adbfbf
00ADBCC7  45 33 DB                        xor r11d, r11d
00ADBCCA  45 85 D2                        test r10d, r10d
00ADBCCD  4C 0F 45 D9                     cmovne r11, rcx
00ADBCD1  41 83 38 05                     cmp dword ptr [r8], 5
00ADBCD5  0F 86 3F FF FF FF               jbe 0x140adbc1a
00ADBCDB  48 8B C2                        mov rax, rdx
00ADBCDE  45 33 C9                        xor r9d, r9d
00ADBCE1  8B 28                           mov ebp, dword ptr [rax]
00ADBCE3  48 8D 48 04                     lea rcx, [rax + 4]
00ADBCE7  41 83 F9 05                     cmp r9d, 5
00ADBCEB  73 1B                           jae 0x140adbd08
00ADBCED  48 3B C8                        cmp rcx, rax
00ADBCF0  0F 82 C9 02 00 00               jb 0x140adbfbf
00ADBCF6  48 8D 04 29                     lea rax, [rcx + rbp]
00ADBCFA  48 3B C1                        cmp rax, rcx
00ADBCFD  0F 82 BC 02 00 00               jb 0x140adbfbf
00ADBD03  41 FF C1                        inc r9d
00ADBD06  EB D9                           jmp 0x140adbce1
00ADBD08  48 3B C8                        cmp rcx, rax
00ADBD0B  0F 82 AE 02 00 00               jb 0x140adbfbf
00ADBD11  33 DB                           xor ebx, ebx
00ADBD13  85 ED                           test ebp, ebp
00ADBD15  48 0F 45 D9                     cmovne rbx, rcx
00ADBD19  41 83 38 06                     cmp dword ptr [r8], 6
00ADBD1D  0F 86 F7 FE FF FF               jbe 0x140adbc1a
00ADBD23  45 33 C0                        xor r8d, r8d
00ADBD26  44 8B 0A                        mov r9d, dword ptr [rdx]
00ADBD29  48 8D 4A 04                     lea rcx, [rdx + 4]
00ADBD2D  41 83 F8 06                     cmp r8d, 6
00ADBD31  73 1B                           jae 0x140adbd4e
00ADBD33  48 3B CA                        cmp rcx, rdx
00ADBD36  0F 82 83 02 00 00               jb 0x140adbfbf
00ADBD3C  4A 8D 14 09                     lea rdx, [rcx + r9]
00ADBD40  48 3B D1                        cmp rdx, rcx
00ADBD43  0F 82 76 02 00 00               jb 0x140adbfbf
00ADBD49  41 FF C0                        inc r8d
00ADBD4C  EB D8                           jmp 0x140adbd26
00ADBD4E  48 3B CA                        cmp rcx, rdx
00ADBD51  0F 82 68 02 00 00               jb 0x140adbfbf
00ADBD57  33 D2                           xor edx, edx
00ADBD59  45 85 C9                        test r9d, r9d
00ADBD5C  48 0F 45 D1                     cmovne rdx, rcx
00ADBD60  48 83 3D 58 C6 4F 00 00         cmp qword ptr [rip + 0x4fc658], 0
00ADBD68  0F 84 49 02 00 00               je 0x140adbfb7
00ADBD6E  48 8B 05 C3 C6 4F 00            mov rax, qword ptr [rip + 0x4fc6c3]
00ADBD75  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00ADBD7A  C7 44 24 38 20 00 00 00         mov dword ptr [rsp + 0x38], 0x20
00ADBD82  4C 8B C3                        mov r8, rbx
00ADBD85  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00ADBD8A  49 8B CB                        mov rcx, r11
00ADBD8D  44 89 4C 24 28                  mov dword ptr [rsp + 0x28], r9d
00ADBD92  44 8B CD                        mov r9d, ebp
00ADBD95  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00ADBD9A  41 8B D2                        mov edx, r10d
00ADBD9D  E8 2E ED BD FF                  call 0x1406baad0
00ADBDA2  44 8B C0                        mov r8d, eax
00ADBDA5  85 C0                           test eax, eax
00ADBDA7  0F 88 18 02 00 00               js 0x140adbfc5
00ADBDAD  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
00ADBDB1  41 8B 56 20                     mov edx, dword ptr [r14 + 0x20]
00ADBDB5  83 C0 50                        add eax, 0x50
00ADBDB8  83 F8 50                        cmp eax, 0x50
00ADBDBB  0F 82 FE 01 00 00               jb 0x140adbfbf
00ADBDC1  8D 48 04                        lea ecx, [rax + 4]
00ADBDC4  41 8B E8                        mov ebp, r8d
00ADBDC7  3B C8                           cmp ecx, eax
00ADBDC9  0F 82 F0 01 00 00               jb 0x140adbfbf
00ADBDCF  8D 04 11                        lea eax, [rcx + rdx]
00ADBDD2  BB 95 00 00 C0                  mov ebx, 0xc0000095
00ADBDD7  3B C1                           cmp eax, ecx
00ADBDD9  45 1B C0                        sbb r8d, r8d
00ADBDDC  44 23 C3                        and r8d, ebx
00ADBDDF  0F 8C E0 01 00 00               jl 0x140adbfc5
00ADBDE5  BA 38 00 00 00                  mov edx, 0x38
00ADBDEA  B9 00 01 00 00                  mov ecx, 0x100
00ADBDEF  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00ADBDF5  89 57 04                        mov dword ptr [rdi + 4], edx
00ADBDF8  E8 F3 62 0A 00                  call 0x140b820f0
00ADBDFD  48 85 C0                        test rax, rax
00ADBE00  75 09                           jne 0x140adbe0b
00ADBE02  44 8D 43 82                     lea r8d, [rbx - 0x7e]
00ADBE06  E9 BA 01 00 00                  jmp 0x140adbfc5
00ADBE0B  48 89 47 08                     mov qword ptr [rdi + 8], rax
00ADBE0F  83 27 00                        and dword ptr [rdi], 0
00ADBE12  0F BA ED 1C                     bts ebp, 0x1c
00ADBE16  48 8B D0                        mov rdx, rax
00ADBE19  48 85 C0                        test rax, rax
00ADBE1C  75 1B                           jne 0x140adbe39
00ADBE1E  8B 47 04                        mov eax, dword ptr [rdi + 4]
00ADBE21  8D 48 08                        lea ecx, [rax + 8]
00ADBE24  3B C8                           cmp ecx, eax
00ADBE26  72 05                           jb 0x140adbe2d
00ADBE28  89 4F 04                        mov dword ptr [rdi + 4], ecx
00ADBE2B  EB 58                           jmp 0x140adbe85
00ADBE2D  83 4F 04 FF                     or dword ptr [rdi + 4], 0xffffffff
00ADBE31  44 8B C3                        mov r8d, ebx
00ADBE34  E9 8C 01 00 00                  jmp 0x140adbfc5
00ADBE39  44 8B 0F                        mov r9d, dword ptr [rdi]
00ADBE3C  33 C9                           xor ecx, ecx
00ADBE3E  41 3B C9                        cmp ecx, r9d
00ADBE41  73 1C                           jae 0x140adbe5f
00ADBE43  8B 02                           mov eax, dword ptr [rdx]
00ADBE45  83 C0 04                        add eax, 4
00ADBE48  83 F8 04                        cmp eax, 4
00ADBE4B  72 E4                           jb 0x140adbe31
00ADBE4D  44 8B C0                        mov r8d, eax
00ADBE50  4C 03 C2                        add r8, rdx
00ADBE53  4C 3B C2                        cmp r8, rdx
00ADBE56  72 D9                           jb 0x140adbe31
00ADBE58  49 8B D0                        mov rdx, r8
00ADBE5B  FF C1                           inc ecx
00ADBE5D  EB DF                           jmp 0x140adbe3e
00ADBE5F  4C 8D 42 04                     lea r8, [rdx + 4]
00ADBE63  4C 3B C2                        cmp r8, rdx
00ADBE66  72 C9                           jb 0x140adbe31
00ADBE68  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00ADBE6B  48 8D 42 08                     lea rax, [rdx + 8]
00ADBE6F  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
00ADBE73  48 3B C1                        cmp rax, rcx
00ADBE76  0F 87 88 00 00 00               ja 0x140adbf04
00ADBE7C  C7 02 04 00 00 00               mov dword ptr [rdx], 4
00ADBE82  41 89 28                        mov dword ptr [r8], ebp
00ADBE85  FF 07                           inc dword ptr [rdi]
00ADBE87  41 83 C9 FF                     or r9d, 0xffffffff
00ADBE8B  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00ADBE8F  48 85 D2                        test rdx, rdx
00ADBE92  75 25                           jne 0x140adbeb9
00ADBE94  8B 57 04                        mov edx, dword ptr [rdi + 4]
00ADBE97  41 8B C1                        mov eax, r9d
00ADBE9A  8D 4A 0C                        lea ecx, [rdx + 0xc]
00ADBE9D  3B CA                           cmp ecx, edx
00ADBE9F  0F 43 C1                        cmovae eax, ecx
00ADBEA2  45 1B C0                        sbb r8d, r8d
00ADBEA5  44 23 C3                        and r8d, ebx
00ADBEA8  89 47 04                        mov dword ptr [rdi + 4], eax
00ADBEAB  3B CA                           cmp ecx, edx
00ADBEAD  73 69                           jae 0x140adbf18
00ADBEAF  45 85 C0                        test r8d, r8d
00ADBEB2  79 66                           jns 0x140adbf1a
00ADBEB4  E9 0C 01 00 00                  jmp 0x140adbfc5
00ADBEB9  44 8B 17                        mov r10d, dword ptr [rdi]
00ADBEBC  33 C9                           xor ecx, ecx
00ADBEBE  41 3B CA                        cmp ecx, r10d
00ADBEC1  73 24                           jae 0x140adbee7
00ADBEC3  8B 02                           mov eax, dword ptr [rdx]
00ADBEC5  83 C0 04                        add eax, 4
00ADBEC8  83 F8 04                        cmp eax, 4
00ADBECB  0F 82 60 FF FF FF               jb 0x140adbe31
00ADBED1  44 8B C0                        mov r8d, eax
00ADBED4  4C 03 C2                        add r8, rdx
00ADBED7  4C 3B C2                        cmp r8, rdx
00ADBEDA  0F 82 51 FF FF FF               jb 0x140adbe31
00ADBEE0  49 8B D0                        mov rdx, r8
00ADBEE3  FF C1                           inc ecx
00ADBEE5  EB D7                           jmp 0x140adbebe
00ADBEE7  4C 8D 42 04                     lea r8, [rdx + 4]
00ADBEEB  4C 3B C2                        cmp r8, rdx
00ADBEEE  0F 82 3D FF FF FF               jb 0x140adbe31
00ADBEF4  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00ADBEF7  48 8D 42 0C                     lea rax, [rdx + 0xc]
00ADBEFB  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
00ADBEFF  48 3B C1                        cmp rax, rcx
00ADBF02  76 0B                           jbe 0x140adbf0f
00ADBF04  41 B8 23 00 00 C0               mov r8d, 0xc0000023
00ADBF0A  E9 B6 00 00 00                  jmp 0x140adbfc5
00ADBF0F  C7 02 08 00 00 00               mov dword ptr [rdx], 8
00ADBF15  49 89 30                        mov qword ptr [r8], rsi
00ADBF18  FF 07                           inc dword ptr [rdi]
00ADBF1A  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
00ADBF1E  48 85 D2                        test rdx, rdx
00ADBF21  75 25                           jne 0x140adbf48
00ADBF23  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00ADBF26  8D 41 24                        lea eax, [rcx + 0x24]
00ADBF29  3B C1                           cmp eax, ecx
00ADBF2B  44 0F 43 C8                     cmovae r9d, eax
00ADBF2F  45 1B C0                        sbb r8d, r8d
00ADBF32  44 23 C3                        and r8d, ebx
00ADBF35  44 89 4F 04                     mov dword ptr [rdi + 4], r9d
00ADBF39  3B C1                           cmp eax, ecx
00ADBF3B  0F 82 84 00 00 00               jb 0x140adbfc5
00ADBF41  FF 07                           inc dword ptr [rdi]
00ADBF43  45 33 C0                        xor r8d, r8d
00ADBF46  EB 7D                           jmp 0x140adbfc5
00ADBF48  44 8B 0F                        mov r9d, dword ptr [rdi]
00ADBF4B  33 C9                           xor ecx, ecx
00ADBF4D  41 3B C9                        cmp ecx, r9d
00ADBF50  73 24                           jae 0x140adbf76
00ADBF52  8B 02                           mov eax, dword ptr [rdx]
00ADBF54  83 C0 04                        add eax, 4
00ADBF57  83 F8 04                        cmp eax, 4
00ADBF5A  0F 82 D1 FE FF FF               jb 0x140adbe31
00ADBF60  44 8B C0                        mov r8d, eax
00ADBF63  4C 03 C2                        add r8, rdx
00ADBF66  4C 3B C2                        cmp r8, rdx
00ADBF69  0F 82 C2 FE FF FF               jb 0x140adbe31
00ADBF6F  49 8B D0                        mov rdx, r8
00ADBF72  FF C1                           inc ecx
00ADBF74  EB D7                           jmp 0x140adbf4d
00ADBF76  4C 8D 4A 04                     lea r9, [rdx + 4]
00ADBF7A  4C 3B CA                        cmp r9, rdx
00ADBF7D  0F 82 AE FE FF FF               jb 0x140adbe31
00ADBF83  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00ADBF86  48 8D 42 24                     lea rax, [rdx + 0x24]
00ADBF8A  48 03 4F 08                     add rcx, qword ptr [rdi + 8]
00ADBF8E  45 33 C0                        xor r8d, r8d
00ADBF91  48 3B C1                        cmp rax, rcx
00ADBF94  0F 87 6A FF FF FF               ja 0x140adbf04
00ADBF9A  C7 02 20 00 00 00               mov dword ptr [rdx], 0x20
00ADBFA0  0F 10 44 24 50                  movups xmm0, xmmword ptr [rsp + 0x50]
00ADBFA5  41 0F 11 01                     movups xmmword ptr [r9], xmm0
00ADBFA9  0F 10 4C 24 60                  movups xmm1, xmmword ptr [rsp + 0x60]
00ADBFAE  41 0F 11 49 10                  movups xmmword ptr [r9 + 0x10], xmm1
00ADBFB3  FF 07                           inc dword ptr [rdi]
00ADBFB5  EB 0E                           jmp 0x140adbfc5
00ADBFB7  41 B8 BB 00 00 C0               mov r8d, 0xc00000bb
00ADBFBD  EB 06                           jmp 0x140adbfc5
00ADBFBF  41 B8 95 00 00 C0               mov r8d, 0xc0000095
00ADBFC5  41 8B C0                        mov eax, r8d
00ADBFC8  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00ADBFCD  48 33 CC                        xor rcx, rsp
00ADBFD0  E8 6B 06 BD FF                  call 0x1406ac640
00ADBFD5  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
00ADBFDD  49 8B 5B 20                     mov rbx, qword ptr [r11 + 0x20]
00ADBFE1  49 8B 6B 28                     mov rbp, qword ptr [r11 + 0x28]
00ADBFE5  49 8B E3                        mov rsp, r11
00ADBFE8  41 5E                           pop r14
00ADBFEA  5F                              pop rdi
00ADBFEB  5E                              pop rsi
00ADBFEC  C3                              ret
00ADBFED  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00ADBBE8(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 3337020)) ^ (v_rsp);
    v_stack_m28 = result;
    if (a1 != 0) goto loc_00ADBC25;
loc_00ADBC1A:
    goto loc_00ADBFC5;
loc_00ADBC25:
    if (a2 == 0) goto loc_00ADBC1A;
    if (a4 == 0) goto loc_00ADBC1A;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00ADBC1A;
    if ((*(unsigned int *)(a1)) <= 3) goto loc_00ADBC1A;
    a4 = 0;
loc_00ADBC43:
    if (0 >= 3) goto loc_00ADBC6B;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00ADBFBF;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00ADBFBF;
    a4 = (unsigned int)((a4) + 1);
    goto loc_00ADBC43;
loc_00ADBC6B:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00ADBFBF;
    v_rsi = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rsi = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) != 8) goto loc_00ADBF04;
    if ((*(unsigned int *)((unsigned int)(0xC000000DULL))) <= 4) goto loc_00ADBC1A;
    a4 = 0;
loc_00ADBC96:
    if (0 >= 4) goto loc_00ADBCBE;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00ADBFBF;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00ADBFBF;
    a4 = (unsigned int)((a4) + 1);
    goto loc_00ADBC96;
loc_00ADBCBE:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00ADBFBF;
    v_r11 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_r11 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if ((*(unsigned int *)((unsigned int)(0xC000000DULL))) <= 5) goto loc_00ADBC1A;
    a4 = 0;
loc_00ADBCE1:
    if (0 >= 5) goto loc_00ADBD08;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00ADBFBF;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00ADBFBF;
    a4 = (unsigned int)((a4) + 1);
    goto loc_00ADBCE1;
loc_00ADBD08:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00ADBFBF;
    v_rbx = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rbx = *(unsigned __int64 *)(a1 + 8) + 4; }
    if ((*(unsigned int *)((unsigned int)(0xC000000DULL))) <= 6) goto loc_00ADBC1A;
    a3 = 0;
loc_00ADBD26:
    if (0 >= 6) goto loc_00ADBD4E;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00ADBFBF;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00ADBFBF;
    a3 = (unsigned int)((a3) + 1);
    goto loc_00ADBD26;
loc_00ADBD4E:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00ADBFBF;
    a2 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { a2 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if ((*(unsigned __int64 *)(v_rip + 5228120)) == 0) goto loc_00ADBFB7;
    v_stack_m60 = 32;
    v_stack_m68 = v_stack_m48;
    v_stack_m70 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))));
    v_stack_m78 = a2;
    result = guard_dispatch_icall(v_r11, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))), v_rbx, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))));
    if (sign_flag) goto loc_00ADBFC5;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16))) + (80));
    if (((unsigned int)(result)) < 80) goto loc_00ADBFBF;
    if (((unsigned int)(result + 4)) < ((unsigned int)(result))) goto loc_00ADBFBF;
    a3 = (unsigned int)(((unsigned int)((unsigned int)(result))) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    if (condition_is_less) goto loc_00ADBFC5;
    *(unsigned int *)(a4 + 4) = 56;
    result = ExAllocatePool2(256, 56, (unsigned int)(0x20534C53ULL), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))));
    if (result != 0) goto loc_00ADBE0B;
    goto loc_00ADBFC5;
loc_00ADBE0B:
    *(unsigned __int64 *)(a4 + 8) = result;
    if (result != 0) goto loc_00ADBE39;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00ADBE2D;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_00ADBE85;
loc_00ADBE2D:
loc_00ADBE31:
    goto loc_00ADBFC5;
loc_00ADBE39:
    a1 = 0;
loc_00ADBE3E:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00ADBE5F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00ADBE31;
    a3 = ((unsigned int)((unsigned int)(result))) + (result);
    if (a3 < result) goto loc_00ADBE31;
    a1 = (unsigned int)((a1) + 1);
    goto loc_00ADBE3E;
loc_00ADBE5F:
    if ((a3 + 4) < a3) goto loc_00ADBE31;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) > a1) goto loc_00ADBF04;
    *(unsigned int *)(a3) = 4;
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
loc_00ADBE85:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) | (0xFFFFFFFFULL));
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00ADBEB9;
    result = (unsigned int)((unsigned int)(a4));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { result = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12); }
    a3 = (unsigned int)((a3 + 4) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    *(unsigned int *)(a4 + 4) = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00ADBF18;
    if (!sign_flag) goto loc_00ADBF1A;
    goto loc_00ADBFC5;
loc_00ADBEB9:
    a1 = 0;
loc_00ADBEBE:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00ADBEE7;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(a4 + 4))))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00ADBE31;
    a3 = ((unsigned int)((unsigned int)(result))) + ((unsigned int)(*(unsigned int *)(a4 + 4)));
    if (a3 < ((unsigned int)(*(unsigned int *)(a4 + 4)))) goto loc_00ADBE31;
    a1 = (unsigned int)((a1) + 1);
    goto loc_00ADBEBE;
loc_00ADBEE7:
    if ((a3 + 4) < a3) goto loc_00ADBE31;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 12) <= a1) goto loc_00ADBF0F;
loc_00ADBF04:
    goto loc_00ADBFC5;
loc_00ADBF0F:
    *(unsigned int *)(a3) = 8;
    *(unsigned __int64 *)((unsigned int)(0xC0000023ULL)) = *(unsigned __int64 *)(v_rsi);
loc_00ADBF18:
loc_00ADBF1A:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00ADBF48;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 36)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { a4 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 36); }
    a3 = (unsigned int)(((unsigned int)(0xC0000023ULL)) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    *(unsigned int *)(a4 + 4) = (unsigned int)(a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 36)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00ADBFC5;
    a3 = 0;
    goto loc_00ADBFC5;
loc_00ADBF48:
    a1 = 0;
loc_00ADBF4D:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00ADBF76;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00ADBE31;
    a3 = ((unsigned int)((unsigned int)(result))) + (*(unsigned __int64 *)(a4 + 8));
    if (a3 < (*(unsigned __int64 *)(a4 + 8))) goto loc_00ADBE31;
    a1 = (unsigned int)((a1) + 1);
    goto loc_00ADBF4D;
loc_00ADBF76:
    if ((a3 + 4) < a3) goto loc_00ADBE31;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    a3 = 0;
    if ((a3 + 36) > a1) goto loc_00ADBF04;
    *(unsigned int *)(a3) = 32;
    *(unsigned __int64 *)(a3 + 4) = v_xmm0;
    *(unsigned __int64 *)(a3 + 4 + 16) = v_xmm1;
    goto loc_00ADBFC5;
loc_00ADBFB7:
    goto loc_00ADBFC5;
loc_00ADBFBF:
loc_00ADBFC5:
    a1 = (v_stack_m28) ^ (v_rsp);
    result = _security_check_cookie(a1, a3, (unsigned int)(0xC0000095ULL), a3 + 4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00ADBBE8(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0x32EB3C)) ^ (local_rsp);
    v_stack_m28 = result;
    if (Arg1 != NULL) goto loc_00ADBC25;
loc_00ADBC1A:
    goto loc_00ADBFC5;
loc_00ADBC25:
    if (Arg2 == 0) goto loc_00ADBC1A;
    if (Arg4 == 0) goto loc_00ADBC1A;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00ADBC1A;
    if ((*(uint32_t *)(arg1)) <= 3) goto loc_00ADBC1A;
    Arg4 = 0;
loc_00ADBC43:
    if (0 >= 3) goto loc_00ADBC6B;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00ADBFBF;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00ADBFBF;
    Arg4 = (uint32_t)((Arg4) + 1);
    goto loc_00ADBC43;
loc_00ADBC6B:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00ADBFBF;
    local_rsi = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rsi = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) != 8) goto loc_00ADBF04;
    if ((*(uint32_t *)((uint32_t)(0xC000000DULL))) <= 4) goto loc_00ADBC1A;
    Arg4 = 0;
loc_00ADBC96:
    if (0 >= 4) goto loc_00ADBCBE;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00ADBFBF;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00ADBFBF;
    Arg4 = (uint32_t)((Arg4) + 1);
    goto loc_00ADBC96;
loc_00ADBCBE:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00ADBFBF;
    local_r11 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_r11 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if ((*(uint32_t *)((uint32_t)(0xC000000DULL))) <= 5) goto loc_00ADBC1A;
    Arg4 = 0;
loc_00ADBCE1:
    if (0 >= 5) goto loc_00ADBD08;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00ADBFBF;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00ADBFBF;
    Arg4 = (uint32_t)((Arg4) + 1);
    goto loc_00ADBCE1;
loc_00ADBD08:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00ADBFBF;
    local_rbx = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rbx = *(uint64_t *)(arg1 + 0x8) + 4; }
    if ((*(uint32_t *)((uint32_t)(0xC000000DULL))) <= 6) goto loc_00ADBC1A;
    Arg3 = 0;
loc_00ADBD26:
    if (0 >= 6) goto loc_00ADBD4E;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00ADBFBF;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00ADBFBF;
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_00ADBD26;
loc_00ADBD4E:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00ADBFBF;
    Arg2 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { Arg2 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if ((*(uint64_t *)(v_rip + 0x4FC658)) == 0) goto loc_00ADBFB7;
    v_stack_m60 = 32;
    v_stack_m68 = v_stack_m48;
    v_stack_m70 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))));
    v_stack_m78 = Arg2;
    result = guard_dispatch_icall(local_r11, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))), local_rbx, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))));
    if (sign_flag) goto loc_00ADBFC5;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + 0x10))) + (80));
    if (((uint32_t)(result)) < 80) goto loc_00ADBFBF;
    if (((uint32_t)(result + 4)) < ((uint32_t)(result))) goto loc_00ADBFBF;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(result))) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    if (condition_is_less) goto loc_00ADBFC5;
    *(uint32_t *)(Arg4 + 0x4) = 56;
    result = ExAllocatePool2(256, 56, (uint32_t)(0x20534C53ULL), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))));
    if (result != 0) goto loc_00ADBE0B;
    goto loc_00ADBFC5;
loc_00ADBE0B:
    *(uint64_t *)(Arg4 + 0x8) = result;
    if (result != 0) goto loc_00ADBE39;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00ADBE2D;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_00ADBE85;
loc_00ADBE2D:
loc_00ADBE31:
    goto loc_00ADBFC5;
loc_00ADBE39:
    Arg1 = 0;
loc_00ADBE3E:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00ADBE5F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00ADBE31;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (result);
    if (Arg3 < result) goto loc_00ADBE31;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_00ADBE3E;
loc_00ADBE5F:
    if ((Arg3 + 4) < Arg3) goto loc_00ADBE31;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 8) > Arg1) goto loc_00ADBF04;
    *(uint32_t *)(Arg3) = 4;
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
loc_00ADBE85:
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg4))) | (0xFFFFFFFFULL));
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00ADBEB9;
    result = (uint32_t)((uint32_t)(Arg4));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) { result = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12); }
    Arg3 = (uint32_t)((Arg3 + 4) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00ADBF18;
    if (!sign_flag) goto loc_00ADBF1A;
    goto loc_00ADBFC5;
loc_00ADBEB9:
    Arg1 = 0;
loc_00ADBEBE:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00ADBEE7;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00ADBE31;
    Arg3 = ((uint32_t)((uint32_t)(result))) + ((uint32_t)(*(uint32_t *)(Arg4 + 0x4)));
    if (Arg3 < ((uint32_t)(*(uint32_t *)(Arg4 + 0x4)))) goto loc_00ADBE31;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_00ADBEBE;
loc_00ADBEE7:
    if ((Arg3 + 4) < Arg3) goto loc_00ADBE31;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 12) <= Arg1) goto loc_00ADBF0F;
loc_00ADBF04:
    goto loc_00ADBFC5;
loc_00ADBF0F:
    *(uint32_t *)(Arg3) = 8;
    *(uint64_t *)((uint32_t)(0xC0000023ULL)) = *(uint64_t *)(local_rsi);
loc_00ADBF18:
loc_00ADBF1A:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00ADBF48;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 36)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) { Arg4 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 36); }
    Arg3 = (uint32_t)(((uint32_t)(0xC0000023ULL)) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)(Arg4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 36)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00ADBFC5;
    Arg3 = 0;
    goto loc_00ADBFC5;
loc_00ADBF48:
    Arg1 = 0;
loc_00ADBF4D:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00ADBF76;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00ADBE31;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (*(uint64_t *)(Arg4 + 0x8));
    if (Arg3 < (*(uint64_t *)(Arg4 + 0x8))) goto loc_00ADBE31;
    Arg1 = (uint32_t)((Arg1) + 1);
    goto loc_00ADBF4D;
loc_00ADBF76:
    if ((Arg3 + 4) < Arg3) goto loc_00ADBE31;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    Arg3 = 0;
    if ((Arg3 + 36) > Arg1) goto loc_00ADBF04;
    *(uint32_t *)(Arg3) = 32;
    *(uint64_t *)(Arg3 + 0x4) = v_xmm0;
    *(uint64_t *)(Arg3 + 0x4 + 0x10) = v_xmm1;
    goto loc_00ADBFC5;
loc_00ADBFB7:
    goto loc_00ADBFC5;
loc_00ADBFBF:
loc_00ADBFC5:
    Arg1 = (v_stack_m28) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg3, (uint32_t)(0xC0000095ULL), Arg3 + 4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ADBBE8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
