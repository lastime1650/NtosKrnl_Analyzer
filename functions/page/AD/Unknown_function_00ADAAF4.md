# sub_00ADAAF4

- RVA: `0x00ADAAF4`–`0x00ADAED2` (길이 `990` bytes)
- VA: `0x0000000140ADAAF4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AA18C`
- 디코드: `290`개 명령, `990/990` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00ADAC0B` → [StringCbLengthW](../../text/45/StringCbLengthW_function_00458B60.md) (function, `0x00458B60`)
- `0x00ADAC40` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ADAC60` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00ADAD21` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00ADAD68` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ADADB3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [sub_00968AF6](../96/Unknown_function_00968AF6.md) at `0x0096A739`

### Static image references
- `0x00ADACF8` → RVA `0x00FD83B0` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00ADAC0B` → [StringCbLengthW](../../text/45/StringCbLengthW_function_00458B60.md) (`PAGE` → `.text`)
  - `0x00ADAC40` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ADAC60` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00ADAD21` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00ADAD68` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ADADB3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ADAAF4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00ADAAF9  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
00ADAAFE  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00ADAB03  57                              push rdi
00ADAB04  41 54                           push r12
00ADAB06  41 55                           push r13
00ADAB08  41 56                           push r14
00ADAB0A  41 57                           push r15
00ADAB0C  48 83 EC 30                     sub rsp, 0x30
00ADAB10  45 33 E4                        xor r12d, r12d
00ADAB13  49 8B F1                        mov rsi, r9
00ADAB16  4C 8B EA                        mov r13, rdx
00ADAB19  4C 8B F1                        mov r14, rcx
00ADAB1C  48 85 D2                        test rdx, rdx
00ADAB1F  75 0A                           jne 0x140adab2b
00ADAB21  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00ADAB26  E9 87 03 00 00                  jmp 0x140adaeb2
00ADAB2B  48 85 F6                        test rsi, rsi
00ADAB2E  74 F1                           je 0x140adab21
00ADAB30  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00ADAB34  48 85 C9                        test rcx, rcx
00ADAB37  74 E8                           je 0x140adab21
00ADAB39  41 83 3E 03                     cmp dword ptr [r14], 3
00ADAB3D  76 E2                           jbe 0x140adab21
00ADAB3F  48 8B C1                        mov rax, rcx
00ADAB42  45 8B C4                        mov r8d, r12d
00ADAB45  44 8B 08                        mov r9d, dword ptr [rax]
00ADAB48  48 8D 50 04                     lea rdx, [rax + 4]
00ADAB4C  41 83 F8 03                     cmp r8d, 3
00ADAB50  73 1B                           jae 0x140adab6d
00ADAB52  48 3B D0                        cmp rdx, rax
00ADAB55  0F 82 52 03 00 00               jb 0x140adaead
00ADAB5B  4A 8D 04 0A                     lea rax, [rdx + r9]
00ADAB5F  48 3B C2                        cmp rax, rdx
00ADAB62  0F 82 45 03 00 00               jb 0x140adaead
00ADAB68  41 FF C0                        inc r8d
00ADAB6B  EB D8                           jmp 0x140adab45
00ADAB6D  48 3B D0                        cmp rdx, rax
00ADAB70  0F 82 37 03 00 00               jb 0x140adaead
00ADAB76  45 85 C9                        test r9d, r9d
00ADAB79  49 8B EC                        mov rbp, r12
00ADAB7C  48 0F 45 EA                     cmovne rbp, rdx
00ADAB80  41 83 F9 08                     cmp r9d, 8
00ADAB84  74 0A                           je 0x140adab90
00ADAB86  BB 23 00 00 C0                  mov ebx, 0xc0000023
00ADAB8B  E9 22 03 00 00                  jmp 0x140adaeb2
00ADAB90  41 83 3E 04                     cmp dword ptr [r14], 4
00ADAB94  48 8B 6D 00                     mov rbp, qword ptr [rbp]
00ADAB98  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
00ADAB9D  76 82                           jbe 0x140adab21
00ADAB9F  45 8B CC                        mov r9d, r12d
00ADABA2  44 8B 01                        mov r8d, dword ptr [rcx]
00ADABA5  48 8D 51 04                     lea rdx, [rcx + 4]
00ADABA9  41 83 F9 04                     cmp r9d, 4
00ADABAD  73 1B                           jae 0x140adabca
00ADABAF  48 3B D1                        cmp rdx, rcx
00ADABB2  0F 82 F5 02 00 00               jb 0x140adaead
00ADABB8  4A 8D 0C 02                     lea rcx, [rdx + r8]
00ADABBC  48 3B CA                        cmp rcx, rdx
00ADABBF  0F 82 E8 02 00 00               jb 0x140adaead
00ADABC5  41 FF C1                        inc r9d
00ADABC8  EB D8                           jmp 0x140adaba2
00ADABCA  48 3B D1                        cmp rdx, rcx
00ADABCD  0F 82 DA 02 00 00               jb 0x140adaead
00ADABD3  45 85 C0                        test r8d, r8d
00ADABD6  49 8B DC                        mov rbx, r12
00ADABD9  48 0F 45 DA                     cmovne rbx, rdx
00ADABDD  75 0A                           jne 0x140adabe9
00ADABDF  BB 3E 00 00 C0                  mov ebx, 0xc000003e
00ADABE4  E9 C9 02 00 00                  jmp 0x140adaeb2
00ADABE9  41 F6 C0 01                     test r8b, 1
00ADABED  75 F0                           jne 0x140adabdf
00ADABEF  49 8B C0                        mov rax, r8
00ADABF2  4D 8B D8                        mov r11, r8
00ADABF5  48 D1 E8                        shr rax, 1
00ADABF8  66 44 3B 64 43 FE               cmp r12w, word ptr [rbx + rax*2 - 2]
00ADABFE  75 DF                           jne 0x140adabdf
00ADAC00  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00ADAC05  49 8B D3                        mov rdx, r11
00ADAC08  48 8B CB                        mov rcx, rbx
00ADAC0B  E8 50 DF 97 FF                  call 0x140458b60
00ADAC10  85 C0                           test eax, eax
00ADAC12  78 CB                           js 0x140adabdf
00ADAC14  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00ADAC19  48 8D 41 02                     lea rax, [rcx + 2]
00ADAC1D  49 3B C3                        cmp rax, r11
00ADAC20  75 BD                           jne 0x140adabdf
00ADAC22  48 D1 E9                        shr rcx, 1
00ADAC25  8D 0C 4D 02 00 00 00            lea ecx, [rcx*2 + 2]
00ADAC2C  85 C9                           test ecx, ecx
00ADAC2E  74 AF                           je 0x140adabdf
00ADAC30  44 8B F9                        mov r15d, ecx
00ADAC33  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00ADAC39  8B D1                           mov edx, ecx
00ADAC3B  B9 00 01 00 00                  mov ecx, 0x100
00ADAC40  E8 AB 74 0A 00                  call 0x140b820f0
00ADAC45  48 8B F8                        mov rdi, rax
00ADAC48  48 85 C0                        test rax, rax
00ADAC4B  75 0A                           jne 0x140adac57
00ADAC4D  BB 17 00 00 C0                  mov ebx, 0xc0000017
00ADAC52  E9 5B 02 00 00                  jmp 0x140adaeb2
00ADAC57  4D 8B C7                        mov r8, r15
00ADAC5A  48 8B D3                        mov rdx, rbx
00ADAC5D  48 8B C8                        mov rcx, rax
00ADAC60  E8 DB BB BE FF                  call 0x1406c6840
00ADAC65  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00ADAC69  48 85 D2                        test rdx, rdx
00ADAC6C  74 4D                           je 0x140adacbb
00ADAC6E  41 83 3E 05                     cmp dword ptr [r14], 5
00ADAC72  76 47                           jbe 0x140adacbb
00ADAC74  48 8B C2                        mov rax, rdx
00ADAC77  45 8B C4                        mov r8d, r12d
00ADAC7A  44 8B 18                        mov r11d, dword ptr [rax]
00ADAC7D  48 8D 48 04                     lea rcx, [rax + 4]
00ADAC81  41 83 F8 05                     cmp r8d, 5
00ADAC85  73 1B                           jae 0x140adaca2
00ADAC87  48 3B C8                        cmp rcx, rax
00ADAC8A  0F 82 10 01 00 00               jb 0x140adada0
00ADAC90  4A 8D 04 19                     lea rax, [rcx + r11]
00ADAC94  48 3B C1                        cmp rax, rcx
00ADAC97  0F 82 03 01 00 00               jb 0x140adada0
00ADAC9D  41 FF C0                        inc r8d
00ADACA0  EB D8                           jmp 0x140adac7a
00ADACA2  48 3B C8                        cmp rcx, rax
00ADACA5  0F 82 F5 00 00 00               jb 0x140adada0
00ADACAB  45 85 DB                        test r11d, r11d
00ADACAE  4D 8B D4                        mov r10, r12
00ADACB1  4C 0F 45 D1                     cmovne r10, rcx
00ADACB5  41 83 3E 06                     cmp dword ptr [r14], 6
00ADACB9  77 0A                           ja 0x140adacc5
00ADACBB  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00ADACC0  E9 E0 00 00 00                  jmp 0x140adada5
00ADACC5  45 8B CC                        mov r9d, r12d
00ADACC8  8B 02                           mov eax, dword ptr [rdx]
00ADACCA  48 8D 4A 04                     lea rcx, [rdx + 4]
00ADACCE  41 83 F9 06                     cmp r9d, 6
00ADACD2  73 1B                           jae 0x140adacef
00ADACD4  48 3B CA                        cmp rcx, rdx
00ADACD7  0F 82 C3 00 00 00               jb 0x140adada0
00ADACDD  48 8D 14 01                     lea rdx, [rcx + rax]
00ADACE1  48 3B D1                        cmp rdx, rcx
00ADACE4  0F 82 B6 00 00 00               jb 0x140adada0
00ADACEA  41 FF C1                        inc r9d
00ADACED  EB D9                           jmp 0x140adacc8
00ADACEF  48 3B CA                        cmp rcx, rdx
00ADACF2  0F 82 A8 00 00 00               jb 0x140adada0
00ADACF8  48 8B 1D B1 D6 4F 00            mov rbx, qword ptr [rip + 0x4fd6b1]
00ADACFF  85 C0                           test eax, eax
00ADAD01  4D 8B CC                        mov r9, r12
00ADAD04  4C 0F 45 C9                     cmovne r9, rcx
00ADAD08  48 85 DB                        test rbx, rbx
00ADAD0B  0F 84 92 01 00 00               je 0x140adaea3
00ADAD11  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00ADAD15  45 8B C3                        mov r8d, r11d
00ADAD18  48 8B C3                        mov rax, rbx
00ADAD1B  49 8B D2                        mov rdx, r10
00ADAD1E  48 8B CF                        mov rcx, rdi
00ADAD21  E8 AA FD BD FF                  call 0x1406baad0
00ADAD26  8B D8                           mov ebx, eax
00ADAD28  85 C0                           test eax, eax
00ADAD2A  78 79                           js 0x140adada5
00ADAD2C  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
00ADAD30  41 8B 55 20                     mov edx, dword ptr [r13 + 0x20]
00ADAD34  83 C0 30                        add eax, 0x30
00ADAD37  83 F8 30                        cmp eax, 0x30
00ADAD3A  72 64                           jb 0x140adada0
00ADAD3C  8D 48 04                        lea ecx, [rax + 4]
00ADAD3F  44 8B FB                        mov r15d, ebx
00ADAD42  3B C8                           cmp ecx, eax
00ADAD44  72 5A                           jb 0x140adada0
00ADAD46  8D 04 11                        lea eax, [rcx + rdx]
00ADAD49  3B C1                           cmp eax, ecx
00ADAD4B  1B DB                           sbb ebx, ebx
00ADAD4D  81 E3 95 00 00 C0               and ebx, 0xc0000095
00ADAD53  78 50                           js 0x140adada5
00ADAD55  BA 14 00 00 00                  mov edx, 0x14
00ADAD5A  B9 00 01 00 00                  mov ecx, 0x100
00ADAD5F  41 B8 53 4C 53 20               mov r8d, 0x20534c53
00ADAD65  89 56 04                        mov dword ptr [rsi + 4], edx
00ADAD68  E8 83 73 0A 00                  call 0x140b820f0
00ADAD6D  48 85 C0                        test rax, rax
00ADAD70  75 07                           jne 0x140adad79
00ADAD72  BB 17 00 00 C0                  mov ebx, 0xc0000017
00ADAD77  EB 2C                           jmp 0x140adada5
00ADAD79  48 89 46 08                     mov qword ptr [rsi + 8], rax
00ADAD7D  41 0F BA EF 1C                  bts r15d, 0x1c
00ADAD82  44 89 26                        mov dword ptr [rsi], r12d
00ADAD85  48 8B D0                        mov rdx, rax
00ADAD88  48 85 C0                        test rax, rax
00ADAD8B  75 30                           jne 0x140adadbd
00ADAD8D  8B 46 04                        mov eax, dword ptr [rsi + 4]
00ADAD90  8D 48 08                        lea ecx, [rax + 8]
00ADAD93  3B C8                           cmp ecx, eax
00ADAD95  72 05                           jb 0x140adad9c
00ADAD97  89 4E 04                        mov dword ptr [rsi + 4], ecx
00ADAD9A  EB 6E                           jmp 0x140adae0a
00ADAD9C  83 4E 04 FF                     or dword ptr [rsi + 4], 0xffffffff
00ADADA0  BB 95 00 00 C0                  mov ebx, 0xc0000095
00ADADA5  48 85 FF                        test rdi, rdi
00ADADA8  0F 84 04 01 00 00               je 0x140adaeb2
00ADADAE  33 D2                           xor edx, edx
00ADADB0  48 8B CF                        mov rcx, rdi
00ADADB3  E8 B8 7A 0A 00                  call 0x140b82870
00ADADB8  E9 F5 00 00 00                  jmp 0x140adaeb2
00ADADBD  41 8B CC                        mov ecx, r12d
00ADADC0  41 3B CC                        cmp ecx, r12d
00ADADC3  73 1C                           jae 0x140adade1
00ADADC5  8B 02                           mov eax, dword ptr [rdx]
00ADADC7  83 C0 04                        add eax, 4
00ADADCA  83 F8 04                        cmp eax, 4
00ADADCD  72 D1                           jb 0x140adada0
00ADADCF  44 8B C0                        mov r8d, eax
00ADADD2  4C 03 C2                        add r8, rdx
00ADADD5  4C 3B C2                        cmp r8, rdx
00ADADD8  72 C6                           jb 0x140adada0
00ADADDA  49 8B D0                        mov rdx, r8
00ADADDD  FF C1                           inc ecx
00ADADDF  EB DF                           jmp 0x140adadc0
00ADADE1  4C 8D 42 04                     lea r8, [rdx + 4]
00ADADE5  4C 3B C2                        cmp r8, rdx
00ADADE8  72 B6                           jb 0x140adada0
00ADADEA  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
00ADADED  48 8D 42 08                     lea rax, [rdx + 8]
00ADADF1  48 03 4E 08                     add rcx, qword ptr [rsi + 8]
00ADADF5  48 3B C1                        cmp rax, rcx
00ADADF8  76 07                           jbe 0x140adae01
00ADADFA  BB 23 00 00 C0                  mov ebx, 0xc0000023
00ADADFF  EB A4                           jmp 0x140adada5
00ADAE01  C7 02 04 00 00 00               mov dword ptr [rdx], 4
00ADAE07  45 89 38                        mov dword ptr [r8], r15d
00ADAE0A  FF 06                           inc dword ptr [rsi]
00ADAE0C  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00ADAE10  48 85 D2                        test rdx, rdx
00ADAE13  75 2B                           jne 0x140adae40
00ADAE15  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
00ADAE18  83 CA FF                        or edx, 0xffffffff
00ADAE1B  8D 41 0C                        lea eax, [rcx + 0xc]
00ADAE1E  3B C1                           cmp eax, ecx
00ADAE20  0F 43 D0                        cmovae edx, eax
00ADAE23  1B DB                           sbb ebx, ebx
00ADAE25  81 E3 95 00 00 C0               and ebx, 0xc0000095
00ADAE2B  89 56 04                        mov dword ptr [rsi + 4], edx
00ADAE2E  3B C1                           cmp eax, ecx
00ADAE30  0F 82 6F FF FF FF               jb 0x140adada5
00ADAE36  FF 06                           inc dword ptr [rsi]
00ADAE38  41 8B DC                        mov ebx, r12d
00ADAE3B  E9 65 FF FF FF                  jmp 0x140adada5
00ADAE40  44 8B 0E                        mov r9d, dword ptr [rsi]
00ADAE43  41 8B CC                        mov ecx, r12d
00ADAE46  41 3B C9                        cmp ecx, r9d
00ADAE49  73 24                           jae 0x140adae6f
00ADAE4B  8B 02                           mov eax, dword ptr [rdx]
00ADAE4D  83 C0 04                        add eax, 4
00ADAE50  83 F8 04                        cmp eax, 4
00ADAE53  0F 82 47 FF FF FF               jb 0x140adada0
00ADAE59  44 8B C0                        mov r8d, eax
00ADAE5C  4C 03 C2                        add r8, rdx
00ADAE5F  4C 3B C2                        cmp r8, rdx
00ADAE62  0F 82 38 FF FF FF               jb 0x140adada0
00ADAE68  49 8B D0                        mov rdx, r8
00ADAE6B  FF C1                           inc ecx
00ADAE6D  EB D7                           jmp 0x140adae46
00ADAE6F  4C 8D 42 04                     lea r8, [rdx + 4]
00ADAE73  4C 3B C2                        cmp r8, rdx
00ADAE76  0F 82 24 FF FF FF               jb 0x140adada0
00ADAE7C  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
00ADAE7F  48 8D 42 0C                     lea rax, [rdx + 0xc]
00ADAE83  48 03 4E 08                     add rcx, qword ptr [rsi + 8]
00ADAE87  41 8B DC                        mov ebx, r12d
00ADAE8A  48 3B C1                        cmp rax, rcx
00ADAE8D  0F 87 67 FF FF FF               ja 0x140adadfa
00ADAE93  C7 02 08 00 00 00               mov dword ptr [rdx], 8
00ADAE99  49 89 28                        mov qword ptr [r8], rbp
00ADAE9C  FF 06                           inc dword ptr [rsi]
00ADAE9E  E9 02 FF FF FF                  jmp 0x140adada5
00ADAEA3  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00ADAEA8  E9 F8 FE FF FF                  jmp 0x140adada5
00ADAEAD  BB 95 00 00 C0                  mov ebx, 0xc0000095
00ADAEB2  48 8B 6C 24 70                  mov rbp, qword ptr [rsp + 0x70]
00ADAEB7  8B C3                           mov eax, ebx
00ADAEB9  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00ADAEBE  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
00ADAEC3  48 83 C4 30                     add rsp, 0x30
00ADAEC7  41 5F                           pop r15
00ADAEC9  41 5E                           pop r14
00ADAECB  41 5D                           pop r13
00ADAECD  41 5C                           pop r12
00ADAECF  5F                              pop rdi
00ADAED0  C3                              ret
00ADAED1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00ADAAF4(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (48);
    v_r12 = 0;
    if (a2 != 0) goto loc_00ADAB2B;
loc_00ADAB21:
    goto loc_00ADAEB2;
loc_00ADAB2B:
    if (a4 == 0) goto loc_00ADAB21;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00ADAB21;
    if ((*(unsigned int *)(a1)) <= 3) goto loc_00ADAB21;
loc_00ADAB45:
    if (0 >= 3) goto loc_00ADAB6D;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00ADAEAD;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00ADAEAD;
    a3 = (unsigned int)((0) + 1);
    goto loc_00ADAB45;
loc_00ADAB6D:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00ADAEAD;
    v_rbp = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rbp = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) == 8) goto loc_00ADAB90;
    goto loc_00ADAEB2;
loc_00ADAB90:
    v_stack_p10 = 0;
    if ((*(unsigned int *)(a1)) <= 4) goto loc_00ADAB21;
loc_00ADABA2:
    if (0 >= 4) goto loc_00ADABCA;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00ADAEAD;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00ADAEAD;
    a4 = (unsigned int)((0) + 1);
    goto loc_00ADABA2;
loc_00ADABCA:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00ADAEAD;
    v_rbx = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_rbx = *(unsigned __int64 *)(a1 + 8) + 4; }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) goto loc_00ADABE9;
loc_00ADABDF:
    goto loc_00ADAEB2;
loc_00ADABE9:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) & (1)) != 0) goto loc_00ADABDF;
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) >> (1);
    if (0 != (*(unsigned __int16 *)((unsigned int)(0xC000003EULL) + result * 2 - 2))) goto loc_00ADABDF;
    result = StringCbLengthW((unsigned int)(0xC000003EULL), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))), v_stack_p10, a4);
    if (sign_flag) goto loc_00ADABDF;
    if ((v_stack_p10 + 2) != ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))) goto loc_00ADABDF;
    a1 = (v_stack_p10) >> (1);
    if ((unsigned int)(a1 * 2 + 2) == 0) goto loc_00ADABDF;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(a1 * 2 + 2)), (unsigned int)(0x20534C53ULL), a4);
    if (result != 0) goto loc_00ADAC57;
    goto loc_00ADAEB2;
loc_00ADAC57:
    result = memcpy(result, (unsigned int)(0xC0000017ULL), (unsigned int)((unsigned int)(a1 * 2 + 2)), a4);
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_00ADACBB;
    if ((*(unsigned int *)(a1)) <= 5) goto loc_00ADACBB;
loc_00ADAC7A:
    if (0 >= 5) goto loc_00ADACA2;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00ADADA0;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00ADADA0;
    a3 = (unsigned int)((0) + 1);
    goto loc_00ADAC7A;
loc_00ADACA2:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00ADADA0;
    v_r10 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { v_r10 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if ((*(unsigned int *)(a1)) > 6) goto loc_00ADACC5;
loc_00ADACBB:
    goto loc_00ADADA5;
loc_00ADACC5:
loc_00ADACC8:
    if (0 >= 6) goto loc_00ADACEF;
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8))) goto loc_00ADADA0;
    if ((*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1) < (*(unsigned __int64 *)(a1 + 8) + 4)) goto loc_00ADADA0;
    a4 = (unsigned int)((0) + 1);
    goto loc_00ADACC8;
loc_00ADACEF:
    if ((*(unsigned __int64 *)(a1 + 8) + 4) < (*(unsigned __int64 *)(a1 + 8) + 4 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))) * 1)) goto loc_00ADADA0;
    a4 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8)))) != 0) { a4 = *(unsigned __int64 *)(a1 + 8) + 4; }
    if (*(unsigned __int64 *)(v_rip + 5232305) == 0) goto loc_00ADAEA3;
    v_stack_m38 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))));
    result = guard_dispatch_icall(result, v_r10, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8))))), a4);
    if (sign_flag) goto loc_00ADADA5;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 16))) + (48));
    if (((unsigned int)(result)) < 48) goto loc_00ADADA0;
    if (((unsigned int)(result + 4)) < ((unsigned int)(result))) goto loc_00ADADA0;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result))) & (0xC0000095ULL));
    if (sign_flag) goto loc_00ADADA5;
    *(unsigned int *)(a4 + 4) = 20;
    result = ExAllocatePool2(256, 20, (unsigned int)(0x20534C53ULL), a4);
    if (result != 0) goto loc_00ADAD79;
    goto loc_00ADADA5;
loc_00ADAD79:
    *(unsigned __int64 *)(a4 + 8) = result;
    *(unsigned int *)(a4) = 0;
    if (result != 0) goto loc_00ADADBD;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00ADAD9C;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 8);
    goto loc_00ADAE0A;
loc_00ADAD9C:
loc_00ADADA0:
loc_00ADADA5:
    if (result == 0) goto loc_00ADAEB2;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x20534C53ULL), a4);
    goto loc_00ADAEB2;
loc_00ADADBD:
loc_00ADADC0:
    if (0 >= 0) goto loc_00ADADE1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00ADADA0;
    a3 = ((unsigned int)((unsigned int)(result))) + (0);
    if (a3 < 0) goto loc_00ADADA0;
    a1 = (unsigned int)((0) + 1);
    goto loc_00ADADC0;
loc_00ADADE1:
    if ((a3 + 4) < a3) goto loc_00ADADA0;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 8) <= a1) goto loc_00ADAE01;
loc_00ADADFA:
    goto loc_00ADADA5;
loc_00ADAE01:
    *(unsigned int *)(a3) = 4;
    *(unsigned int *)(a3 + 4) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
loc_00ADAE0A:
    if (*(unsigned __int64 *)(a4 + 8) != 0) goto loc_00ADAE40;
    a2 = (unsigned int)((*(unsigned __int64 *)(a4 + 8)) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) { a2 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12); }
    v_rbx = (unsigned int)(((unsigned int)(0xC0000023ULL)) & (0xC0000095ULL));
    *(unsigned int *)(a4 + 4) = (unsigned int)(a2);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)) + 12)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_00ADADA5;
    goto loc_00ADADA5;
loc_00ADAE40:
loc_00ADAE46:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_00ADAE6F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) + (4));
    if (((unsigned int)(result)) < 4) goto loc_00ADADA0;
    a3 = ((unsigned int)((unsigned int)(result))) + (a2);
    if (a3 < a2) goto loc_00ADADA0;
    a1 = (unsigned int)((0) + 1);
    goto loc_00ADAE46;
loc_00ADAE6F:
    if ((a3 + 4) < a3) goto loc_00ADADA0;
    a1 = ((unsigned int)(*(unsigned int *)(a4 + 4))) + (*(unsigned __int64 *)(a4 + 8));
    if ((a3 + 12) > a1) goto loc_00ADADFA;
    *(unsigned int *)(a3) = 8;
    *(unsigned __int64 *)(a3 + 4) = *(unsigned __int64 *)(v_rbp);
    goto loc_00ADADA5;
loc_00ADAEA3:
    goto loc_00ADADA5;
loc_00ADAEAD:
loc_00ADAEB2:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t sub_00ADAAF4(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint32_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (48);
    local_r12 = 0;
    if (Arg2 != NULL) goto loc_00ADAB2B;
loc_00ADAB21:
    goto loc_00ADAEB2;
loc_00ADAB2B:
    if (Arg4 == 0) goto loc_00ADAB21;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00ADAB21;
    if ((*(uint32_t *)(arg1)) <= 3) goto loc_00ADAB21;
loc_00ADAB45:
    if (0 >= 3) goto loc_00ADAB6D;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00ADAEAD;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00ADAEAD;
    Arg3 = (uint32_t)((0) + 1);
    goto loc_00ADAB45;
loc_00ADAB6D:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00ADAEAD;
    local_rbp = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rbp = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) == 8) goto loc_00ADAB90;
    goto loc_00ADAEB2;
loc_00ADAB90:
    v_stack_p10 = 0;
    if ((*(uint32_t *)(arg1)) <= 4) goto loc_00ADAB21;
loc_00ADABA2:
    if (0 >= 4) goto loc_00ADABCA;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00ADAEAD;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00ADAEAD;
    Arg4 = (uint32_t)((0) + 1);
    goto loc_00ADABA2;
loc_00ADABCA:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00ADAEAD;
    local_rbx = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_rbx = *(uint64_t *)(arg1 + 0x8) + 4; }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) goto loc_00ADABE9;
loc_00ADABDF:
    goto loc_00ADAEB2;
loc_00ADABE9:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) & (1)) != 0) goto loc_00ADABDF;
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) >> (1);
    if (0 != (*(uint16_t *)((uint32_t)(0xC000003EULL) + result * 2 - 0x2))) goto loc_00ADABDF;
    result = StringCbLengthW((uint32_t)(0xC000003EULL), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))), v_stack_p10, Arg4);
    if (sign_flag) goto loc_00ADABDF;
    if ((v_stack_p10 + 2) != ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))) goto loc_00ADABDF;
    Arg1 = (v_stack_p10) >> (1);
    if ((uint32_t)(Arg1 * 2 + 2) == 0) goto loc_00ADABDF;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(Arg1 * 2 + 2)), (uint32_t)(0x20534C53ULL), Arg4);
    if (result != 0) goto loc_00ADAC57;
    goto loc_00ADAEB2;
loc_00ADAC57:
    result = memcpy(result, (uint32_t)(0xC0000017ULL), (uint32_t)((uint32_t)(Arg1 * 2 + 2)), Arg4);
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_00ADACBB;
    if ((*(uint32_t *)(arg1)) <= 5) goto loc_00ADACBB;
loc_00ADAC7A:
    if (0 >= 5) goto loc_00ADACA2;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00ADADA0;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00ADADA0;
    Arg3 = (uint32_t)((0) + 1);
    goto loc_00ADAC7A;
loc_00ADACA2:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00ADADA0;
    local_r10 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { local_r10 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if ((*(uint32_t *)(arg1)) > 6) goto loc_00ADACC5;
loc_00ADACBB:
    goto loc_00ADADA5;
loc_00ADACC5:
loc_00ADACC8:
    if (0 >= 6) goto loc_00ADACEF;
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8))) goto loc_00ADADA0;
    if ((*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1) < (*(uint64_t *)(arg1 + 0x8) + 4)) goto loc_00ADADA0;
    Arg4 = (uint32_t)((0) + 1);
    goto loc_00ADACC8;
loc_00ADACEF:
    if ((*(uint64_t *)(arg1 + 0x8) + 4) < (*(uint64_t *)(arg1 + 0x8) + 4 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))) * 1)) goto loc_00ADADA0;
    Arg4 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8)))) != 0) { Arg4 = *(uint64_t *)(arg1 + 0x8) + 4; }
    if (*(uint64_t *)(v_rip + 0x4FD6B1) == 0) goto loc_00ADAEA3;
    v_stack_m38 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))));
    result = guard_dispatch_icall(result, local_r10, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8))))), Arg4);
    if (sign_flag) goto loc_00ADADA5;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x10))) + (48));
    if (((uint32_t)(result)) < 48) goto loc_00ADADA0;
    if (((uint32_t)(result + 4)) < ((uint32_t)(result))) goto loc_00ADADA0;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result))) & (0xC0000095ULL));
    if (sign_flag) goto loc_00ADADA5;
    *(uint32_t *)(Arg4 + 0x4) = 20;
    result = ExAllocatePool2(256, 20, (uint32_t)(0x20534C53ULL), Arg4);
    if (result != 0) goto loc_00ADAD79;
    goto loc_00ADADA5;
loc_00ADAD79:
    *(uint64_t *)(Arg4 + 0x8) = result;
    *(uint32_t *)(Arg4) = 0;
    if (result != 0) goto loc_00ADADBD;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00ADAD9C;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 8);
    goto loc_00ADAE0A;
loc_00ADAD9C:
loc_00ADADA0:
loc_00ADADA5:
    if (result == 0) goto loc_00ADAEB2;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x20534C53ULL), Arg4);
    goto loc_00ADAEB2;
loc_00ADADBD:
loc_00ADADC0:
    if (0 >= 0) goto loc_00ADADE1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00ADADA0;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (0);
    if (Arg3 < 0) goto loc_00ADADA0;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_00ADADC0;
loc_00ADADE1:
    if ((Arg3 + 4) < Arg3) goto loc_00ADADA0;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 8) <= Arg1) goto loc_00ADAE01;
loc_00ADADFA:
    goto loc_00ADADA5;
loc_00ADAE01:
    *(uint32_t *)(Arg3) = 4;
    *(uint32_t *)(Arg3 + 0x4) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
loc_00ADAE0A:
    if (*(uint64_t *)(Arg4 + 0x8) != 0) goto loc_00ADAE40;
    Arg2 = (uint32_t)((*(uint64_t *)(Arg4 + 0x8)) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) { Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12); }
    local_rbx = (uint32_t)(((uint32_t)(0xC0000023ULL)) & (0xC0000095ULL));
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)(Arg2);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)) + 12)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_00ADADA5;
    goto loc_00ADADA5;
loc_00ADAE40:
loc_00ADAE46:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_00ADAE6F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) + (4));
    if (((uint32_t)(result)) < 4) goto loc_00ADADA0;
    Arg3 = ((uint32_t)((uint32_t)(result))) + (Arg2);
    if (Arg3 < Arg2) goto loc_00ADADA0;
    Arg1 = (uint32_t)((0) + 1);
    goto loc_00ADAE46;
loc_00ADAE6F:
    if ((Arg3 + 4) < Arg3) goto loc_00ADADA0;
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) + (*(uint64_t *)(Arg4 + 0x8));
    if ((Arg3 + 12) > Arg1) goto loc_00ADADFA;
    *(uint32_t *)(Arg3) = 8;
    *(uint64_t *)(Arg3 + 0x4) = *(uint64_t *)(local_rbp);
    goto loc_00ADADA5;
loc_00ADAEA3:
    goto loc_00ADADA5;
loc_00ADAEAD:
loc_00ADAEB2:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x20` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ADAAF4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
