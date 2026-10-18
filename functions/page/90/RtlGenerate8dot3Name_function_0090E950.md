# RtlGenerate8dot3Name

- RVA: `0x0090E950`–`0x0090EFD8` (길이 `1,672` bytes)
- VA: `0x000000014090E950`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000897E8`
- 디코드: `448`개 명령, `1,672/1,672` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0090E99B` → [RtlpIsUtf8Process](RtlpIsUtf8Process_function_0090DB60.md) (function, `0x0090DB60`)
- `0x0090E9A8` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x0090EC3C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0090EC61` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0090EC91` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0090ECB5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0090ECFC` → [RtlIsValidOemCharacter](RtlIsValidOemCharacter_function_0090F5C0.md) (function, `0x0090F5C0`)
- `0x0090EDDE` → [RtlIsValidOemCharacter](RtlIsValidOemCharacter_function_0090F5C0.md) (function, `0x0090F5C0`)
- `0x0090EE50` → [RtlIsValidOemCharacter](RtlIsValidOemCharacter_function_0090F5C0.md) (function, `0x0090F5C0`)
- `0x0090EE82` → [RtlComputeLfnChecksum](RtlComputeLfnChecksum_function_0090F4B8.md) (function, `0x0090F4B8`)
- `0x0090EF5A` → [RtlComputeLfnChecksum](RtlComputeLfnChecksum_function_0090F4B8.md) (function, `0x0090F4B8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0090E964` → RVA `0x00E0A740` (`.data`; read)
- `0x0090EA54` → RVA `0x00B4B560` (`RtlFatIllegalTable`; read)
- `0x0090EE21` → RVA `0x00FD803F` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x0090E9A8` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x0090EC3C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0090EC61` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0090EC91` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0090ECB5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x0090EF71` → [sub_00B21392](../B2/Unknown_function_00B21392.md) (`tail-transfer`)
  - `0x0090EFBC` → [sub_00B21392 + 0x78](../B2/Unknown_function_00B21392.md) (`tail-transfer`)
  - `0x0090EFCB` → [sub_00B21392 + 0x7B](../B2/Unknown_function_00B21392.md) (`tail-transfer`)
  - `0x0090EFD3` → [sub_00B21392 + 0x42](../B2/Unknown_function_00B21392.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0090E950  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0090E955  55                              push rbp
0090E956  56                              push rsi
0090E957  57                              push rdi
0090E958  41 54                           push r12
0090E95A  41 55                           push r13
0090E95C  41 56                           push r14
0090E95E  41 57                           push r15
0090E960  48 83 EC 50                     sub rsp, 0x50
0090E964  48 8B 05 D5 BD 4F 00            mov rax, qword ptr [rip + 0x4fbdd5]
0090E96B  48 33 C4                        xor rax, rsp
0090E96E  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0090E973  41 B6 01                        mov r14b, 1
0090E976  4C 89 4C 24 30                  mov qword ptr [rsp + 0x30], r9
0090E97B  4C 8B F9                        mov r15, rcx
0090E97E  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
0090E983  33 DB                           xor ebx, ebx
0090E985  44 88 74 24 21                  mov byte ptr [rsp + 0x21], r14b
0090E98A  41 8A CE                        mov cl, r14b
0090E98D  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
0090E992  49 8B F8                        mov rdi, r8
0090E995  44 8A EA                        mov r13b, dl
0090E998  40 8A F3                        mov sil, bl
0090E99B  E8 C0 F1 FF FF                  call 0x14090db60
0090E9A0  84 C0                           test al, al
0090E9A2  75 20                           jne 0x14090e9c4
0090E9A4  F0 09 1C 24                     lock or dword ptr [rsp], ebx
0090E9A8  E8 43 F8 9E FF                  call 0x1402fe1f0
0090E9AD  66 39 98 54 04 00 00            cmp word ptr [rax + 0x454], bx
0090E9B4  48 8B 88 70 04 00 00            mov rcx, qword ptr [rax + 0x470]
0090E9BB  40 0F 95 C6                     setne sil
0090E9BF  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
0090E9C4  45 84 ED                        test r13b, r13b
0090E9C7  0F 85 2B 04 00 00               jne 0x14090edf8
0090E9CD  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
0090E9D1  BE 30 00 00 00                  mov esi, 0x30
0090E9D6  8D 6E 07                        lea ebp, [rsi + 7]
0090E9D9  44 8D 66 D6                     lea r12d, [rsi - 0x2a]
0090E9DD  38 5F 03                        cmp byte ptr [rdi + 3], bl
0090E9E0  0F 85 A9 01 00 00               jne 0x14090eb8f
0090E9E6  41 83 CE FF                     or r14d, 0xffffffff
0090E9EA  44 8D 4E FE                     lea r9d, [rsi - 2]
0090E9EE  8B EB                           mov ebp, ebx
0090E9F0  66 41 39 1F                     cmp word ptr [r15], bx
0090E9F4  76 0D                           jbe 0x14090ea03
0090E9F6  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
0090E9FA  40 B6 01                        mov sil, 1
0090E9FD  66 44 39 08                     cmp word ptr [rax], r9w
0090EA01  74 03                           je 0x14090ea06
0090EA03  40 8A F3                        mov sil, bl
0090EA06  BF 5F 00 00 00                  mov edi, 0x5f
0090EA0B  44 8D 67 21                     lea r12d, [rdi + 0x21]
0090EA0F  0F B7 D3                        movzx edx, bx
0090EA12  41 0F B7 07                     movzx eax, word ptr [r15]
0090EA16  D1 E8                           shr eax, 1
0090EA18  3B E8                           cmp ebp, eax
0090EA1A  73 5E                           jae 0x14090ea7a
0090EA1C  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
0090EA20  8B CD                           mov ecx, ebp
0090EA22  FF C5                           inc ebp
0090EA24  0F B7 14 48                     movzx edx, word ptr [rax + rcx*2]
0090EA28  66 89 54 24 24                  mov word ptr [rsp + 0x24], dx
0090EA2D  66 83 FA 20                     cmp dx, 0x20
0090EA31  0F 86 D8 02 00 00               jbe 0x14090ed0f
0090EA37  66 83 FA 7F                     cmp dx, 0x7f
0090EA3B  0F 83 B1 02 00 00               jae 0x14090ecf2
0090EA41  66 41 3B D1                     cmp dx, r9w
0090EA45  0F 84 CB 02 00 00               je 0x14090ed16
0090EA4B  66 41 3B D4                     cmp dx, r12w
0090EA4F  73 20                           jae 0x14090ea71
0090EA51  0F B7 C2                        movzx eax, dx
0090EA54  4C 8D 05 05 CB 23 00            lea r8, [rip + 0x23cb05]
0090EA5B  48 C1 E8 05                     shr rax, 5
0090EA5F  0F B7 CA                        movzx ecx, dx
0090EA62  83 E1 1F                        and ecx, 0x1f
0090EA65  41 8B 04 80                     mov eax, dword ptr [r8 + rax*4]
0090EA69  0F A3 C8                        bt eax, ecx
0090EA6C  73 03                           jae 0x14090ea71
0090EA6E  0F B7 D7                        movzx edx, di
0090EA71  8D 42 9F                        lea eax, [rdx - 0x61]
0090EA74  66 83 F8 19                     cmp ax, 0x19
0090EA78  76 13                           jbe 0x14090ea8d
0090EA7A  66 85 D2                        test dx, dx
0090EA7D  74 18                           je 0x14090ea97
0090EA7F  40 8A F3                        mov sil, bl
0090EA82  66 41 3B D1                     cmp dx, r9w
0090EA86  75 87                           jne 0x14090ea0f
0090EA88  44 8B F5                        mov r14d, ebp
0090EA8B  EB 82                           jmp 0x14090ea0f
0090EA8D  B8 E0 FF 00 00                  mov eax, 0xffe0
0090EA92  66 03 D0                        add dx, ax
0090EA95  EB E3                           jmp 0x14090ea7a
0090EA97  41 0F B7 07                     movzx eax, word ptr [r15]
0090EA9B  8B F3                           mov esi, ebx
0090EA9D  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0090EAA2  8B EB                           mov ebp, ebx
0090EAA4  D1 E8                           shr eax, 1
0090EAA6  41 BC 06 00 00 00               mov r12d, 6
0090EAAC  44 3B F0                        cmp r14d, eax
0090EAAF  B8 FF FF FF FF                  mov eax, 0xffffffff
0090EAB4  44 0F 44 F0                     cmove r14d, eax
0090EAB8  88 5F 03                        mov byte ptr [rdi + 3], bl
0090EABB  0F B7 D3                        movzx edx, bx
0090EABE  41 0F B7 07                     movzx eax, word ptr [r15]
0090EAC2  D1 E8                           shr eax, 1
0090EAC4  3B F0                           cmp esi, eax
0090EAC6  73 64                           jae 0x14090eb2c
0090EAC8  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
0090EACC  8B CE                           mov ecx, esi
0090EACE  FF C6                           inc esi
0090EAD0  0F B7 14 48                     movzx edx, word ptr [rax + rcx*2]
0090EAD4  66 89 54 24 24                  mov word ptr [rsp + 0x24], dx
0090EAD9  66 83 FA 20                     cmp dx, 0x20
0090EADD  0F 86 0E 03 00 00               jbe 0x14090edf1
0090EAE3  66 83 FA 7F                     cmp dx, 0x7f
0090EAE7  0F 83 E7 02 00 00               jae 0x14090edd4
0090EAED  66 41 3B D1                     cmp dx, r9w
0090EAF1  0F 84 FA 02 00 00               je 0x14090edf1
0090EAF7  B8 80 00 00 00                  mov eax, 0x80
0090EAFC  66 3B D0                        cmp dx, ax
0090EAFF  73 22                           jae 0x14090eb23
0090EB01  0F B7 C2                        movzx eax, dx
0090EB04  4C 8D 05 55 CA 23 00            lea r8, [rip + 0x23ca55]
0090EB0B  48 C1 E8 05                     shr rax, 5
0090EB0F  0F B7 CA                        movzx ecx, dx
0090EB12  83 E1 1F                        and ecx, 0x1f
0090EB15  41 8B 04 80                     mov eax, dword ptr [r8 + rax*4]
0090EB19  0F A3 C8                        bt eax, ecx
0090EB1C  73 05                           jae 0x14090eb23
0090EB1E  BA 5F 00 00 00                  mov edx, 0x5f
0090EB23  8D 42 9F                        lea eax, [rdx - 0x61]
0090EB26  66 83 F8 19                     cmp ax, 0x19
0090EB2A  76 2A                           jbe 0x14090eb56
0090EB2C  66 85 D2                        test dx, dx
0090EB2F  74 2F                           je 0x14090eb60
0090EB31  41 3B F6                        cmp esi, r14d
0090EB34  73 2A                           jae 0x14090eb60
0090EB36  0F B6 4F 03                     movzx ecx, byte ptr [rdi + 3]
0090EB3A  41 3A CC                        cmp cl, r12b
0090EB3D  73 21                           jae 0x14090eb60
0090EB3F  38 5C 24 20                     cmp byte ptr [rsp + 0x20], bl
0090EB43  0F 85 8A 01 00 00               jne 0x14090ecd3
0090EB49  66 89 54 4F 04                  mov word ptr [rdi + rcx*2 + 4], dx
0090EB4E  FE 47 03                        inc byte ptr [rdi + 3]
0090EB51  E9 65 FF FF FF                  jmp 0x14090eabb
0090EB56  B8 E0 FF 00 00                  mov eax, 0xffe0
0090EB5B  66 03 D0                        add dx, ax
0090EB5E  EB CC                           jmp 0x14090eb2c
0090EB60  38 5C 24 20                     cmp byte ptr [rsp + 0x20], bl
0090EB64  75 04                           jne 0x14090eb6a
0090EB66  0F B6 6F 03                     movzx ebp, byte ptr [rdi + 3]
0090EB6A  83 FD 02                        cmp ebp, 2
0090EB6D  0F 86 E4 03 00 00               jbe 0x14090ef57
0090EB73  BE 30 00 00 00                  mov esi, 0x30
0090EB78  8D 6E 07                        lea ebp, [rsi + 7]
0090EB7B  83 C8 FF                        or eax, 0xffffffff
0090EB7E  44 3B F0                        cmp r14d, eax
0090EB81  0F 85 9A 01 00 00               jne 0x14090ed21
0090EB87  89 5F 14                        mov dword ptr [rdi + 0x14], ebx
0090EB8A  44 8A 74 24 21                  mov r14b, byte ptr [rsp + 0x21]
0090EB8F  44 8B 4F 20                     mov r9d, dword ptr [rdi + 0x20]
0090EB93  44 8A 6C 24 20                  mov r13b, byte ptr [rsp + 0x20]
0090EB98  41 FF C1                        inc r9d
0090EB9B  44 89 4F 20                     mov dword ptr [rdi + 0x20], r9d
0090EB9F  41 83 F9 04                     cmp r9d, 4
0090EBA3  0F 87 C1 02 00 00               ja 0x14090ee6a
0090EBA9  BE 01 00 00 00                  mov esi, 1
0090EBAE  8D 6E 06                        lea ebp, [rsi + 6]
0090EBB1  44 8D 56 07                     lea r10d, [rsi + 7]
0090EBB5  44 8D 5E 2F                     lea r11d, [rsi + 0x2f]
0090EBB9  45 85 C9                        test r9d, r9d
0090EBBC  74 45                           je 0x14090ec03
0090EBBE  B8 CD CC CC CC                  mov eax, 0xcccccccd
0090EBC3  41 F7 E1                        mul r9d
0090EBC6  C1 EA 03                        shr edx, 3
0090EBC9  0F B7 C2                        movzx eax, dx
0090EBCC  66 C1 E0 02                     shl ax, 2
0090EBD0  8D 0C 10                        lea ecx, [rax + rdx]
0090EBD3  41 8B C2                        mov eax, r10d
0090EBD6  66 03 C9                        add cx, cx
0090EBD9  2B C6                           sub eax, esi
0090EBDB  66 44 2B C9                     sub r9w, cx
0090EBDF  FF C6                           inc esi
0090EBE1  8B CB                           mov ecx, ebx
0090EBE3  47 8D 04 0B                     lea r8d, [r11 + r9]
0090EBE7  44 8B CA                        mov r9d, edx
0090EBEA  66 41 83 F8 39                  cmp r8w, 0x39
0090EBEF  66 44 89 44 44 38               mov word ptr [rsp + rax*2 + 0x38], r8w
0090EBF5  41 0F B6 C6                     movzx eax, r14b
0090EBF9  0F 44 C8                        cmove ecx, eax
0090EBFC  44 8A F1                        mov r14b, cl
0090EBFF  3B F5                           cmp esi, ebp
0090EC01  76 B6                           jbe 0x14090ebb9
0090EC03  0F B6 4F 03                     movzx ecx, byte ptr [rdi + 3]
0090EC07  44 2B D6                        sub r10d, esi
0090EC0A  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
0090EC0F  44 88 74 24 21                  mov byte ptr [rsp + 0x21], r14b
0090EC14  4C 8D 74 24 38                  lea r14, [rsp + 0x38]
0090EC19  8D 41 FF                        lea eax, [rcx - 1]
0090EC1C  4F 8D 34 56                     lea r14, [r14 + r10*2]
0090EC20  66 41 C7 06 7E 00               mov word ptr [r14], 0x7e
0090EC26  3C 0B                           cmp al, 0xb
0090EC28  0F 87 80 03 00 00               ja 0x14090efae
0090EC2E  44 8B C1                        mov r8d, ecx
0090EC31  48 8D 57 04                     lea rdx, [rdi + 4]
0090EC35  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
0090EC39  4D 03 C0                        add r8, r8
0090EC3C  E8 FF 7B DB FF                  call 0x1406c6840
0090EC41  0F B6 4F 03                     movzx ecx, byte ptr [rdi + 3]
0090EC45  66 03 C9                        add cx, cx
0090EC48  66 41 89 0F                     mov word ptr [r15], cx
0090EC4C  44 8D 04 36                     lea r8d, [rsi + rsi]
0090EC50  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
0090EC54  49 8B D6                        mov rdx, r14
0090EC57  0F B7 C9                        movzx ecx, cx
0090EC5A  48 D1 E9                        shr rcx, 1
0090EC5D  48 8D 0C 48                     lea rcx, [rax + rcx*2]
0090EC61  E8 DA 7B DB FF                  call 0x1406c6840
0090EC66  0F B7 CE                        movzx ecx, si
0090EC69  66 03 C9                        add cx, cx
0090EC6C  66 41 03 0F                     add cx, word ptr [r15]
0090EC70  66 41 89 0F                     mov word ptr [r15], cx
0090EC74  8B 47 14                        mov eax, dword ptr [rdi + 0x14]
0090EC77  85 C0                           test eax, eax
0090EC79  74 26                           je 0x14090eca1
0090EC7B  0F B7 C9                        movzx ecx, cx
0090EC7E  44 8D 04 00                     lea r8d, [rax + rax]
0090EC82  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
0090EC86  48 8D 57 18                     lea rdx, [rdi + 0x18]
0090EC8A  48 D1 E9                        shr rcx, 1
0090EC8D  48 8D 0C 48                     lea rcx, [rax + rcx*2]
0090EC91  E8 AA 7B DB FF                  call 0x1406c6840
0090EC96  0F B7 47 14                     movzx eax, word ptr [rdi + 0x14]
0090EC9A  66 03 C0                        add ax, ax
0090EC9D  66 41 01 07                     add word ptr [r15], ax
0090ECA1  38 5C 24 21                     cmp byte ptr [rsp + 0x21], bl
0090ECA5  0F 85 0A 03 00 00               jne 0x14090efb5
0090ECAB  33 C0                           xor eax, eax
0090ECAD  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0090ECB2  48 33 CC                        xor rcx, rsp
0090ECB5  E8 86 D9 D9 FF                  call 0x1406ac640
0090ECBA  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
0090ECC2  48 83 C4 50                     add rsp, 0x50
0090ECC6  41 5F                           pop r15
0090ECC8  41 5E                           pop r14
0090ECCA  41 5D                           pop r13
0090ECCC  41 5C                           pop r12
0090ECCE  5F                              pop rdi
0090ECCF  5E                              pop rsi
0090ECD0  5D                              pop rbp
0090ECD1  C3                              ret
0090ECD2  CC                              int3
0090ECD3  66 83 FA 7F                     cmp dx, 0x7f
0090ECD7  0F 87 1B 02 00 00               ja 0x14090eef8
0090ECDD  B8 01 00 00 00                  mov eax, 1
0090ECE2  03 E8                           add ebp, eax
0090ECE4  41 3B EC                        cmp ebp, r12d
0090ECE7  0F 86 5C FE FF FF               jbe 0x14090eb49
0090ECED  E9 78 FE FF FF                  jmp 0x14090eb6a
0090ECF2  45 84 ED                        test r13b, r13b
0090ECF5  74 18                           je 0x14090ed0f
0090ECF7  48 8D 4C 24 24                  lea rcx, [rsp + 0x24]
0090ECFC  E8 BF 08 00 00                  call 0x14090f5c0
0090ED01  41 B9 2E 00 00 00               mov r9d, 0x2e
0090ED07  84 C0                           test al, al
0090ED09  0F 85 2A 02 00 00               jne 0x14090ef39
0090ED0F  8B D3                           mov edx, ebx
0090ED11  E9 FC FC FF FF                  jmp 0x14090ea12
0090ED16  40 84 F6                        test sil, sil
0090ED19  0F 84 32 FD FF FF               je 0x14090ea51
0090ED1F  EB EE                           jmp 0x14090ed0f
0090ED21  BE 01 00 00 00                  mov esi, 1
0090ED26  66 44 89 4F 18                  mov word ptr [rdi + 0x18], r9w
0090ED2B  89 77 14                        mov dword ptr [rdi + 0x14], esi
0090ED2E  0F B7 D3                        movzx edx, bx
0090ED31  41 0F B7 07                     movzx eax, word ptr [r15]
0090ED35  D1 E8                           shr eax, 1
0090ED37  44 3B F0                        cmp r14d, eax
0090ED3A  73 64                           jae 0x14090eda0
0090ED3C  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
0090ED40  42 0F B7 14 70                  movzx edx, word ptr [rax + r14*2]
0090ED45  41 FF C6                        inc r14d
0090ED48  66 89 54 24 24                  mov word ptr [rsp + 0x24], dx
0090ED4D  66 83 FA 20                     cmp dx, 0x20
0090ED51  0F 86 0C 01 00 00               jbe 0x14090ee63
0090ED57  66 83 FA 7F                     cmp dx, 0x7f
0090ED5B  0F 83 E5 00 00 00               jae 0x14090ee46
0090ED61  66 41 3B D1                     cmp dx, r9w
0090ED65  0F 84 F8 00 00 00               je 0x14090ee63
0090ED6B  B8 80 00 00 00                  mov eax, 0x80
0090ED70  66 3B D0                        cmp dx, ax
0090ED73  73 22                           jae 0x14090ed97
0090ED75  0F B7 C2                        movzx eax, dx
0090ED78  4C 8D 05 E1 C7 23 00            lea r8, [rip + 0x23c7e1]
0090ED7F  48 C1 E8 05                     shr rax, 5
0090ED83  0F B7 CA                        movzx ecx, dx
0090ED86  83 E1 1F                        and ecx, 0x1f
0090ED89  41 8B 04 80                     mov eax, dword ptr [r8 + rax*4]
0090ED8D  0F A3 C8                        bt eax, ecx
0090ED90  73 05                           jae 0x14090ed97
0090ED92  BA 5F 00 00 00                  mov edx, 0x5f
0090ED97  8D 42 9F                        lea eax, [rdx - 0x61]
0090ED9A  66 83 F8 19                     cmp ax, 0x19
0090ED9E  76 20                           jbe 0x14090edc0
0090EDA0  66 85 D2                        test dx, dx
0090EDA3  74 25                           je 0x14090edca
0090EDA5  8B 4F 14                        mov ecx, dword ptr [rdi + 0x14]
0090EDA8  83 F9 04                        cmp ecx, 4
0090EDAB  73 74                           jae 0x14090ee21
0090EDAD  38 5C 24 20                     cmp byte ptr [rsp + 0x20], bl
0090EDB1  75 58                           jne 0x14090ee0b
0090EDB3  66 89 54 4F 18                  mov word ptr [rdi + rcx*2 + 0x18], dx
0090EDB8  FF 47 14                        inc dword ptr [rdi + 0x14]
0090EDBB  E9 6E FF FF FF                  jmp 0x14090ed2e
0090EDC0  B8 E0 FF 00 00                  mov eax, 0xffe0
0090EDC5  66 03 D0                        add dx, ax
0090EDC8  EB D6                           jmp 0x14090eda0
0090EDCA  BE 30 00 00 00                  mov esi, 0x30
0090EDCF  E9 B6 FD FF FF                  jmp 0x14090eb8a
0090EDD4  45 84 ED                        test r13b, r13b
0090EDD7  74 18                           je 0x14090edf1
0090EDD9  48 8D 4C 24 24                  lea rcx, [rsp + 0x24]
0090EDDE  E8 DD 07 00 00                  call 0x14090f5c0
0090EDE3  41 B9 2E 00 00 00               mov r9d, 0x2e
0090EDE9  84 C0                           test al, al
0090EDEB  0F 85 52 01 00 00               jne 0x14090ef43
0090EDF1  8B D3                           mov edx, ebx
0090EDF3  E9 C6 FC FF FF                  jmp 0x14090eabe
0090EDF8  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
0090EDFD  40 84 F6                        test sil, sil
0090EE00  0F 85 CB FB FF FF               jne 0x14090e9d1
0090EE06  E9 C2 FB FF FF                  jmp 0x14090e9cd
0090EE0B  66 83 FA 7F                     cmp dx, 0x7f
0090EE0F  0F 87 61 01 00 00               ja 0x14090ef76
0090EE15  B8 01 00 00 00                  mov eax, 1
0090EE1A  03 F0                           add esi, eax
0090EE1C  83 FE 04                        cmp esi, 4
0090EE1F  76 92                           jbe 0x14090edb3
0090EE21  38 1D 18 92 6C 00               cmp byte ptr [rip + 0x6c9218], bl
0090EE27  BE 30 00 00 00                  mov esi, 0x30
0090EE2C  44 8A 74 24 21                  mov r14b, byte ptr [rsp + 0x21]
0090EE31  0F 84 58 FD FF FF               je 0x14090eb8f
0090EE37  8D 41 FF                        lea eax, [rcx - 1]
0090EE3A  66 C7 44 47 18 7E 00            mov word ptr [rdi + rax*2 + 0x18], 0x7e
0090EE41  E9 49 FD FF FF                  jmp 0x14090eb8f
0090EE46  45 84 ED                        test r13b, r13b
0090EE49  74 18                           je 0x14090ee63
0090EE4B  48 8D 4C 24 24                  lea rcx, [rsp + 0x24]
0090EE50  E8 6B 07 00 00                  call 0x14090f5c0
0090EE55  41 B9 2E 00 00 00               mov r9d, 0x2e
0090EE5B  84 C0                           test al, al
0090EE5D  0F 85 EA 00 00 00               jne 0x14090ef4d
0090EE63  8B D3                           mov edx, ebx
0090EE65  E9 C7 FE FF FF                  jmp 0x14090ed31
0090EE6A  38 5F 02                        cmp byte ptr [rdi + 2], bl
0090EE6D  0F 85 36 FD FF FF               jne 0x14090eba9
0090EE73  45 84 ED                        test r13b, r13b
0090EE76  0F 85 99 00 00 00               jne 0x14090ef15
0090EE7C  44 8B D3                        mov r10d, ebx
0090EE7F  49 8B CF                        mov rcx, r15
0090EE82  E8 31 06 00 00                  call 0x14090f4b8
0090EE87  41 B8 02 00 00 00               mov r8d, 2
0090EE8D  66 89 07                        mov word ptr [rdi], ax
0090EE90  41 8B D4                        mov edx, r12d
0090EE93  45 2B C2                        sub r8d, r10d
0090EE96  41 2B D2                        sub edx, r10d
0090EE99  44 0F B7 D8                     movzx r11d, ax
0090EE9D  44 3B C2                        cmp r8d, edx
0090EEA0  73 39                           jae 0x14090eedb
0090EEA2  45 8B C8                        mov r9d, r8d
0090EEA5  49 83 C1 02                     add r9, 2
0090EEA9  41 2B D0                        sub edx, r8d
0090EEAC  44 8B C2                        mov r8d, edx
0090EEAF  4E 8D 0C 4F                     lea r9, [rdi + r9*2]
0090EEB3  41 0F B7 CB                     movzx ecx, r11w
0090EEB7  8B C6                           mov eax, esi
0090EEB9  66 83 E1 0F                     and cx, 0xf
0090EEBD  66 83 F9 09                     cmp cx, 9
0090EEC1  66 0F 47 C5                     cmova ax, bp
0090EEC5  66 41 C1 EB 04                  shr r11w, 4
0090EECA  66 03 C1                        add ax, cx
0090EECD  66 41 89 01                     mov word ptr [r9], ax
0090EED1  4D 8D 49 02                     lea r9, [r9 + 2]
0090EED5  49 83 E8 01                     sub r8, 1
0090EED9  75 D8                           jne 0x14090eeb3
0090EEDB  45 2A E2                        sub r12b, r10b
0090EEDE  C7 47 20 01 00 00 00            mov dword ptr [rdi + 0x20], 1
0090EEE5  44 88 67 03                     mov byte ptr [rdi + 3], r12b
0090EEE9  41 B9 01 00 00 00               mov r9d, 1
0090EEEF  C6 47 02 01                     mov byte ptr [rdi + 2], 1
0090EEF3  E9 B1 FC FF FF                  jmp 0x14090eba9
0090EEF8  4C 8B 44 24 28                  mov r8, qword ptr [rsp + 0x28]
0090EEFD  0F B7 C2                        movzx eax, dx
0090EF00  41 38 5C 40 01                  cmp byte ptr [r8 + rax*2 + 1], bl
0090EF05  B8 02 00 00 00                  mov eax, 2
0090EF0A  0F 85 D2 FD FF FF               jne 0x14090ece2
0090EF10  E9 C8 FD FF FF                  jmp 0x14090ecdd
0090EF15  0F B7 47 04                     movzx eax, word ptr [rdi + 4]
0090EF19  48 8B 54 24 28                  mov rdx, qword ptr [rsp + 0x28]
0090EF1E  83 F8 7F                        cmp eax, 0x7f
0090EF21  77 70                           ja 0x14090ef93
0090EF23  8B CB                           mov ecx, ebx
0090EF25  0F B7 47 06                     movzx eax, word ptr [rdi + 6]
0090EF29  83 F8 7F                        cmp eax, 0x7f
0090EF2C  77 72                           ja 0x14090efa0
0090EF2E  44 8B D3                        mov r10d, ebx
0090EF31  44 0B D1                        or r10d, ecx
0090EF34  E9 46 FF FF FF                  jmp 0x14090ee7f
0090EF39  0F B7 54 24 24                  movzx edx, word ptr [rsp + 0x24]
0090EF3E  E9 FE FA FF FF                  jmp 0x14090ea41
0090EF43  0F B7 54 24 24                  movzx edx, word ptr [rsp + 0x24]
0090EF48  E9 A0 FB FF FF                  jmp 0x14090eaed
0090EF4D  0F B7 54 24 24                  movzx edx, word ptr [rsp + 0x24]
0090EF52  E9 0A FE FF FF                  jmp 0x14090ed61
0090EF57  49 8B CF                        mov rcx, r15
0090EF5A  E8 59 05 00 00                  call 0x14090f4b8
0090EF5F  BE 30 00 00 00                  mov esi, 0x30
0090EF64  66 89 07                        mov word ptr [rdi], ax
0090EF67  44 0F B7 D0                     movzx r10d, ax
0090EF6B  44 8B C3                        mov r8d, ebx
0090EF6E  8D 6E 07                        lea ebp, [rsi + 7]
0090EF71  E9 1C 24 21 00                  jmp 0x140b21392
0090EF76  4C 8B 44 24 28                  mov r8, qword ptr [rsp + 0x28]
0090EF7B  0F B7 C2                        movzx eax, dx
0090EF7E  41 38 5C 40 01                  cmp byte ptr [r8 + rax*2 + 1], bl
0090EF83  B8 02 00 00 00                  mov eax, 2
0090EF88  0F 85 8C FE FF FF               jne 0x14090ee1a
0090EF8E  E9 82 FE FF FF                  jmp 0x14090ee15
0090EF93  B9 01 00 00 00                  mov ecx, 1
0090EF98  38 5C 42 01                     cmp byte ptr [rdx + rax*2 + 1], bl
0090EF9C  75 87                           jne 0x14090ef25
0090EF9E  EB 83                           jmp 0x14090ef23
0090EFA0  41 BA 01 00 00 00               mov r10d, 1
0090EFA6  38 5C 42 01                     cmp byte ptr [rdx + rax*2 + 1], bl
0090EFAA  75 85                           jne 0x14090ef31
0090EFAC  EB 80                           jmp 0x14090ef2e
0090EFAE  8B CB                           mov ecx, ebx
0090EFB0  E9 93 FC FF FF                  jmp 0x14090ec48
0090EFB5  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
0090EFB9  45 84 ED                        test r13b, r13b
0090EFBC  0F 84 48 24 21 00               je 0x140b2140a
0090EFC2  8B CB                           mov ecx, ebx
0090EFC4  8B D3                           mov edx, ebx
0090EFC6  44 8B C8                        mov r9d, eax
0090EFC9  84 C0                           test al, al
0090EFCB  0F 84 3C 24 21 00               je 0x140b2140d
0090EFD1  2B EE                           sub ebp, esi
0090EFD3  E9 FC 23 21 00                  jmp 0x140b213d4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlGenerate8dot3Name(__int64 a1, unsigned __int8 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int16 v_stack_m64;
    unsigned __int8 v_stack_m67;
    unsigned __int8 v_stack_m68;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p21;
    unsigned __int64 v_stack_p24;
    unsigned __int64 v_stack_p28;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (80);
    result = (*(unsigned __int64 *)(v_rip + 5225941)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m58 = a4;
    v_stack_m50 = a3;
    v_rbx = 0;
    v_stack_m67 = 1;
    v_stack_m60 = 0;
    result = RtlpIsUtf8Process(1, a2, a3, a4);
    v_rsi = 0;
    if ((unsigned __int8)(result) == 0) {
        result = PsGetCurrentServerSiloGlobals(1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(result + 1136);
        v_rsi = ((*(unsigned __int16 *)(result + 1108)) != 0) ? 1 : 0;
        v_stack_m60 = a1;
    }
    if (a2 != 0) goto loc_0090EDF8;
loc_0090E9CD:
    v_stack_m68 = 0;
loc_0090E9D1:
    if ((*(unsigned __int8 *)(a3 + 3)) != 0) goto loc_0090EB8F;
    v_r14 = (unsigned int)((1) | (0xFFFFFFFFULL));
    if ((*(unsigned __int16 *)(a1)) <= 0) goto loc_0090EA03;
    v_rsi = 1;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8))) != ((unsigned __int16)(48 - 2))) {
        v_rsi = 0;
    }
loc_0090EA0F:
loc_0090EA12:
    result = (unsigned int)((*(unsigned __int16 *)(a1)) >> (1));
    if (0 >= ((unsigned int)(result))) goto loc_0090EA7A;
    v_rbp = (unsigned int)((0) + 1);
    v_stack_m64 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 * 2));
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 * 2))) <= 32) goto loc_0090ED0F;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 * 2))) >= 127) goto loc_0090ECF2;
loc_0090EA41:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 * 2))) == ((unsigned __int16)(48 - 2))) goto loc_0090ED16;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 * 2))) >= ((unsigned __int16)(95 + 33))) goto loc_0090EA71;
loc_0090EA51:
    result = ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 * 2))) >> (5);
    a1 = (unsigned int)(((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 * 2))) & (31));
    if (!(condition_is_above_or_equal)) {
        a2 = 95;
    }
    if (((unsigned __int16)(a2 - 97)) <= 25) goto loc_0090EA8D;
loc_0090EA7A:
    if (a2 == 0) goto loc_0090EA97;
    if (a2 != ((unsigned __int16)(48 - 2))) goto loc_0090EA0F;
    goto loc_0090EA0F;
loc_0090EA8D:
    a2 = (unsigned __int16)((a2) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
    goto loc_0090EA7A;
loc_0090EA97:
    result = (unsigned int)((*(unsigned __int16 *)(a1)) >> (1));
    v_r14 = (unsigned int)((unsigned int)(v_rbp));
    if (((unsigned int)((unsigned int)((unsigned int)(v_rbp)))) == ((unsigned int)(result))) { v_r14 = (unsigned int)((unsigned int)(0xFFFFFFFFULL)); }
    *(unsigned __int8 *)(v_stack_m50 + 3) = 0;
loc_0090EABB:
loc_0090EABE:
    result = (unsigned int)((*(unsigned __int16 *)(a1)) >> (1));
    if (0 >= ((unsigned int)(result))) goto loc_0090EB2C;
    v_rsi = (unsigned int)((0) + 1);
    v_stack_m64 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 * 2));
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 * 2))) <= 32) goto loc_0090EDF1;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 * 2))) >= 127) goto loc_0090EDD4;
loc_0090EAED:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 * 2))) == ((unsigned __int16)(48 - 2))) goto loc_0090EDF1;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 * 2))) >= 128) goto loc_0090EB23;
    result = ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 * 2))) >> (5);
    a1 = (unsigned int)(((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 0 * 2))) & (31));
    if (!(condition_is_above_or_equal)) {
        a2 = 95;
    }
    if (((unsigned __int16)(a2 - 97)) <= 25) goto loc_0090EB56;
loc_0090EB2C:
    if (a2 == 0) goto loc_0090EB60;
    if (((unsigned int)(v_rsi)) >= ((unsigned int)(v_r14))) goto loc_0090EB60;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_m50 + 3))) >= 6) goto loc_0090EB60;
    if (v_stack_m68 != 0) goto loc_0090ECD3;
loc_0090EB49:
    *(unsigned __int16 *)(v_stack_m50 + *(unsigned __int8 *)(v_stack_m50 + 3) * 2 + 4) = a2;
    goto loc_0090EABB;
loc_0090EB56:
    a2 = (unsigned __int16)((a2) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
    goto loc_0090EB2C;
loc_0090EB60:
    v_rbp = 0;
    if (v_stack_m68 == 0) {
        v_rbp = *(unsigned __int8 *)(v_stack_m50 + 3);
    }
    if (((unsigned int)(v_rbp)) <= 2) goto loc_0090EF57;
    result = (unsigned int)(((unsigned int)(0xFFE0ULL)) | (0xFFFFFFFFULL));
    if (((unsigned int)(v_r14)) != ((unsigned int)(result))) goto loc_0090ED21;
    *(unsigned int *)(v_stack_m50 + 20) = 0;
loc_0090EB8A:
loc_0090EB8F:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m50 + 32))) + 1);
    *(unsigned int *)(v_stack_m50 + 32) = (unsigned int)(a4);
    if (((unsigned int)(a4)) > 4) goto loc_0090EE6A;
loc_0090EBA9:
loc_0090EBB9:
    if ((unsigned int)(a4) == 0) goto loc_0090EC03;
    a2 = (unsigned int)((a2) >> (3));
    result = (unsigned __int16)((a2) << (2));
    a1 = (unsigned __int16)((result + a2 * 1) + ((unsigned __int16)(result + a2 * 1)));
    result = (unsigned int)(((unsigned int)((unsigned int)(1 + 7))) - (1));
    a4 = (unsigned __int16)((a4) - ((unsigned __int16)(a1)));
    v_rsi = (unsigned int)((1) + 1);
    *(unsigned __int16 *)(v_rsp + result * 2 + 56) = (unsigned __int16)(1 + 47 + a4 * 1);
    a1 = 0;
    if (((unsigned __int16)(1 + 47 + a4 * 1)) == 57) { a1 = (unsigned int)((unsigned __int8)(v_stack_m67)); }
    if (((unsigned int)(v_rsi)) <= ((unsigned int)(1 + 6))) goto loc_0090EBB9;
loc_0090EC03:
    v_r10 = (unsigned int)((1 + 7) - ((unsigned int)(v_rsi)));
    v_stack_m67 = (unsigned __int8)((unsigned __int8)(a1));
    *(unsigned __int16 *)(v_stack_m50 + v_r10 * 2) = 126;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_m50 + 3) - 1)) > 11) goto loc_0090EFAE;
    a3 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_stack_m50 + 3)))) + ((unsigned int)((unsigned int)(*(unsigned __int8 *)(v_stack_m50 + 3))));
    result = memcpy(*(unsigned __int64 *)(v_stack_m58 + 8), v_stack_m50 + 4, a3, (unsigned int)(a2));
    a1 = (unsigned __int16)((*(unsigned __int8 *)(v_stack_m50 + 3)) + ((unsigned __int16)(*(unsigned __int8 *)(v_stack_m50 + 3))));
loc_0090EC48:
    *(unsigned __int16 *)(v_stack_m58) = (unsigned __int16)(a1);
    a1 = ((unsigned __int16)(a1)) >> (1);
    result = memcpy(*(unsigned __int64 *)(v_stack_m58 + 8) + a1 * 2, v_stack_m50 + v_r10 * 2, v_rsi + v_rsi * 1, (unsigned int)(a2));
    a1 = (unsigned __int16)(((unsigned __int16)(v_rsi)) + ((unsigned __int16)((unsigned __int16)(v_rsi))));
    a1 = (unsigned __int16)((a1) + (*(unsigned __int16 *)(v_stack_m58)));
    *(unsigned __int16 *)(v_stack_m58) = (unsigned __int16)(a1);
    result = (unsigned int)(*(unsigned int *)(v_stack_m50 + 20));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m50 + 20))) != 0) {
        a1 = (unsigned __int16)(a1);
        a3 = (unsigned int)(*(unsigned int *)(v_stack_m50 + 20)) + (unsigned int)(*(unsigned int *)(v_stack_m50 + 20)) * 1;
        result = *(unsigned __int64 *)(v_stack_m58 + 8);
        a2 = v_stack_m50 + 24;
        a1 = (a1) >> (1);
        a1 = result + a1 * 2;
        result = memcpy(a1, a2, a3, (unsigned int)(a2));
        result = *(unsigned __int16 *)(v_stack_m50 + 20);
        result = (unsigned __int16)((result) + ((unsigned __int16)(result)));
    }
    if (v_stack_m67 != 0) goto loc_0090EFB5;
    result = 0;
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, (unsigned int)(a2));
    v_rsp = (v_rsp) + (80);
    return result;
loc_0090ECD3:
    if (a2 > 127) goto loc_0090EEF8;
loc_0090ECDD:
loc_0090ECE2:
    v_rbp = (unsigned int)((1 + 6) + (1));
    if (((unsigned int)(v_rbp)) <= 6) goto loc_0090EB49;
    goto loc_0090EB6A;
loc_0090ECF2:
    if ((unsigned __int8)(v_stack_m68) == 0) goto loc_0090ED0F;
    result = RtlIsValidOemCharacter(v_stack_p24, a2, a3, (unsigned int)(a2));
    if ((unsigned __int8)(result) != 0) goto loc_0090EF39;
loc_0090ED0F:
    goto loc_0090EA12;
loc_0090ED16:
    if ((unsigned __int8)(v_rsi) == 0) goto loc_0090EA51;
    goto loc_0090ED0F;
loc_0090ED21:
    *(unsigned __int16 *)(v_stack_m50 + 24) = 46;
    *(unsigned int *)(v_stack_m50 + 20) = 1;
loc_0090ED2E:
loc_0090ED31:
    result = (unsigned int)((*(unsigned __int16 *)(v_stack_m58)) >> (1));
    if (((unsigned int)(v_stack_m50 + v_r10 * 2)) >= ((unsigned int)(result))) goto loc_0090EDA0;
    v_r14 = (unsigned int)((v_stack_m50 + v_r10 * 2) + 1);
    v_stack_p24 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m58 + 8) + v_stack_m50 + v_r10 * 2 * 2));
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m58 + 8) + v_stack_m50 + v_r10 * 2 * 2))) <= 32) goto loc_0090EE63;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m58 + 8) + v_stack_m50 + v_r10 * 2 * 2))) >= 127) goto loc_0090EE46;
loc_0090ED61:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m58 + 8) + v_stack_m50 + v_r10 * 2 * 2))) == 46) goto loc_0090EE63;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m58 + 8) + v_stack_m50 + v_r10 * 2 * 2))) >= 128) goto loc_0090ED97;
    result = ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m58 + 8) + v_stack_m50 + v_r10 * 2 * 2))) >> (5);
    a1 = (unsigned int)(((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m58 + 8) + v_stack_m50 + v_r10 * 2 * 2))) & (31));
    if (!(condition_is_above_or_equal)) {
        a2 = 95;
    }
    if (((unsigned __int16)(a2 - 97)) <= 25) goto loc_0090EDC0;
loc_0090EDA0:
    if (a2 == 0) goto loc_0090EDCA;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m50 + 20)))) >= 4) goto loc_0090EE21;
    if (v_stack_p20 != ((unsigned __int8)(v_stack_p10))) goto loc_0090EE0B;
loc_0090EDB3:
    *(unsigned __int16 *)(v_stack_m50 + (unsigned int)(*(unsigned int *)(v_stack_m50 + 20)) * 2 + 24) = a2;
    goto loc_0090ED2E;
loc_0090EDC0:
    a2 = (unsigned __int16)((a2) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
    goto loc_0090EDA0;
loc_0090EDCA:
    goto loc_0090EB8A;
loc_0090EDD4:
    if ((unsigned __int8)(v_stack_m68) == 0) goto loc_0090EDF1;
    result = RtlIsValidOemCharacter(v_stack_p24, a2, v_rip + 2344929, 46);
    if ((unsigned __int8)(result) != 0) goto loc_0090EF43;
loc_0090EDF1:
    goto loc_0090EABE;
loc_0090EDF8:
    v_stack_p20 = (unsigned __int8)(v_r14);
    if (48 != 0) goto loc_0090E9D1;
    goto loc_0090E9CD;
loc_0090EE0B:
    if (((unsigned __int16)((unsigned int)((unsigned int)(v_stack_p10)))) > 127) goto loc_0090EF76;
loc_0090EE15:
loc_0090EE1A:
    v_rsi = (unsigned int)((48) + (1));
    if (((unsigned int)(v_rsi)) <= 4) goto loc_0090EDB3;
loc_0090EE21:
    if ((*(unsigned __int8 *)(v_rip + 7115288)) == ((unsigned __int8)(v_stack_p10))) goto loc_0090EB8F;
    *(unsigned __int16 *)(v_stack_m50 + v_stack_p24 - 1 * 2 + 24) = 126;
    goto loc_0090EB8F;
loc_0090EE46:
    if ((unsigned __int8)(v_stack_m68) == 0) goto loc_0090EE63;
    result = RtlIsValidOemCharacter(v_stack_p24, (unsigned int)((unsigned int)(v_stack_p10)), v_rip + 2344929, 46);
    if ((unsigned __int8)(result) != 0) goto loc_0090EF4D;
loc_0090EE63:
    goto loc_0090ED31;
loc_0090EE6A:
    if ((*(unsigned __int8 *)(v_stack_m50 + 2)) != ((unsigned __int8)(v_stack_p10))) goto loc_0090EBA9;
    if ((unsigned __int8)(v_stack_m68) != 0) goto loc_0090EF15;
loc_0090EE7F:
    result = RtlComputeLfnChecksum(v_stack_m58, (unsigned int)((unsigned int)(v_stack_p10)), v_rip + 2344929, 46);
    *(unsigned __int16 *)(v_stack_m50) = (unsigned __int16)(result);
    a3 = (unsigned int)((2) - ((unsigned int)((unsigned int)((unsigned int)(v_stack_p10)))));
    a2 = (unsigned int)((6) - ((unsigned int)((unsigned int)((unsigned int)(v_stack_p10)))));
    if (((unsigned int)(a3)) >= a2) goto loc_0090EEDB;
    a4 = ((unsigned int)((unsigned int)(a3))) + (2);
    a2 = (unsigned int)((a2) - ((unsigned int)(a3)));
loc_0090EEB3:
    a1 = (unsigned __int16)(((unsigned __int16)((unsigned __int16)(result))) & (15));
    result = 48;
    if (((unsigned __int16)(a1)) > 9) { result = (unsigned __int16)(v_rbp); }
    v_r11 = (unsigned __int16)(((unsigned __int16)(result)) >> (4));
    result = (unsigned __int16)((result) + ((unsigned __int16)(a1)));
    *(unsigned __int16 *)(v_stack_m50 + a4 * 2) = (unsigned __int16)(result);
    a3 = ((unsigned int)(a2)) - (1);
    if (condition_is_not_equal) goto loc_0090EEB3;
loc_0090EEDB:
    v_r12 = (unsigned __int8)((6) - ((unsigned __int8)((unsigned int)((unsigned int)(v_stack_p10)))));
    *(unsigned int *)(v_stack_m50 + 32) = 1;
    *(unsigned __int8 *)(v_stack_m50 + 3) = (unsigned __int8)(v_r12);
    *(unsigned __int8 *)(v_stack_m50 + 2) = 1;
    goto loc_0090EBA9;
loc_0090EEF8:
    if ((*(unsigned __int8 *)(v_stack_p28 + a2 * 2 + 1)) != ((unsigned __int8)(v_stack_p10))) goto loc_0090ECE2;
    goto loc_0090ECDD;
loc_0090EF15:
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_m50 + 4))) > 127) goto loc_0090EF93;
loc_0090EF23:
loc_0090EF25:
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_m50 + 6))) > 127) goto loc_0090EFA0;
loc_0090EF2E:
loc_0090EF31:
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p10))) | ((unsigned int)((unsigned int)((unsigned int)(v_stack_p10)))));
    goto loc_0090EE7F;
loc_0090EF39:
    goto loc_0090EA41;
loc_0090EF43:
    goto loc_0090EAED;
loc_0090EF4D:
    goto loc_0090ED61;
loc_0090EF57:
    result = RtlComputeLfnChecksum(v_stack_m58, v_stack_p24, v_stack_p28, 1);
    *(unsigned __int16 *)(v_stack_m50) = (unsigned __int16)(result);
loc_0090EF76:
    if ((*(unsigned __int8 *)(v_stack_p28 + (unsigned __int16)(v_stack_p24) * 2 + 1)) != ((unsigned __int8)(v_stack_p10))) goto loc_0090EE1A;
    goto loc_0090EE15;
loc_0090EF93:
    if ((*(unsigned __int8 *)(v_stack_p24 + 2 * 2 + 1)) != ((unsigned __int8)(v_stack_p10))) goto loc_0090EF25;
    goto loc_0090EF23;
loc_0090EFA0:
    if ((*(unsigned __int8 *)(v_stack_p24 + 2 * 2 + 1)) != ((unsigned __int8)(v_stack_p10))) goto loc_0090EF31;
    goto loc_0090EF2E;
loc_0090EFAE:
    goto loc_0090EC48;
loc_0090EFB5:
    v_rbp = (unsigned int)((48 + 7) - (48));
}
```

## 5. (Beta) C Style

```c
int64_t RtlGenerate8dot3Name(void *Arg1, uint8_t Arg2, void *Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint16_t v_stack_m64;
    uint8_t v_stack_m67;
    uint8_t v_stack_m68;
    uint32_t v_stack_m88;
    uint64_t v_stack_p10;
    uint8_t v_stack_p20;
    uint8_t v_stack_p21;
    uint64_t v_stack_p24;
    uint64_t v_stack_p28;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (80);
    result = (*(uint64_t *)(v_rip + 0x4FBDD5)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m58 = Arg4;
    v_stack_m50 = Arg3;
    local_rbx = 0;
    v_stack_m67 = 1;
    v_stack_m60 = 0;
    result = RtlpIsUtf8Process(1, Arg2, Arg3, Arg4);
    local_rsi = 0;
    if ((uint8_t)(result) == 0) {
        result = PsGetCurrentServerSiloGlobals(1, Arg2, Arg3, Arg4);
        Arg1 = *(uint64_t *)(result + 0x470);
        local_rsi = ((*(uint16_t *)(result + 0x454)) != 0) ? 1 : 0;
        v_stack_m60 = Arg1;
    }
    if (Arg2 != 0) goto loc_0090EDF8;
loc_0090E9CD:
    v_stack_m68 = 0;
loc_0090E9D1:
    if ((*(uint8_t *)(arg3 + 0x3)) != 0) goto loc_0090EB8F;
    local_r14 = (uint32_t)((1) | (0xFFFFFFFFULL));
    if ((*(uint16_t *)(arg1)) <= 0) goto loc_0090EA03;
    local_rsi = 1;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8))) != ((uint16_t)(48 - 2))) {
        local_rsi = 0;
    }
loc_0090EA0F:
loc_0090EA12:
    result = (uint32_t)((*(uint16_t *)(arg1)) >> (1));
    if (0 >= ((uint32_t)(result))) goto loc_0090EA7A;
    local_rbp = (uint32_t)((0) + 1);
    v_stack_m64 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 * 2));
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 * 2))) <= 32) goto loc_0090ED0F;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 * 2))) >= 127) goto loc_0090ECF2;
loc_0090EA41:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 * 2))) == ((uint16_t)(48 - 2))) goto loc_0090ED16;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 * 2))) >= ((uint16_t)(95 + 33))) goto loc_0090EA71;
loc_0090EA51:
    result = ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 * 2))) >> (5);
    Arg1 = (uint32_t)(((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 * 2))) & (31));
    if (!(condition_is_above_or_equal)) {
        Arg2 = 95;
    }
    if (((uint16_t)(Arg2 - 97)) <= 25) goto loc_0090EA8D;
loc_0090EA7A:
    if (Arg2 == 0) goto loc_0090EA97;
    if (Arg2 != ((uint16_t)(48 - 2))) goto loc_0090EA0F;
    goto loc_0090EA0F;
loc_0090EA8D:
    Arg2 = (uint16_t)((Arg2) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
    goto loc_0090EA7A;
loc_0090EA97:
    result = (uint32_t)((*(uint16_t *)(arg1)) >> (1));
    local_r14 = (uint32_t)((uint32_t)(local_rbp));
    if (((uint32_t)((uint32_t)((uint32_t)(local_rbp)))) == ((uint32_t)(result))) { local_r14 = (uint32_t)((uint32_t)(0xFFFFFFFFULL)); }
    *(uint8_t *)(v_stack_m50 + 0x3) = 0;
loc_0090EABB:
loc_0090EABE:
    result = (uint32_t)((*(uint16_t *)(arg1)) >> (1));
    if (0 >= ((uint32_t)(result))) goto loc_0090EB2C;
    local_rsi = (uint32_t)((0) + 1);
    v_stack_m64 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 * 2));
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 * 2))) <= 32) goto loc_0090EDF1;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 * 2))) >= 127) goto loc_0090EDD4;
loc_0090EAED:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 * 2))) == ((uint16_t)(48 - 2))) goto loc_0090EDF1;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 * 2))) >= 128) goto loc_0090EB23;
    result = ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 * 2))) >> (5);
    Arg1 = (uint32_t)(((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x0 * 2))) & (31));
    if (!(condition_is_above_or_equal)) {
        Arg2 = 95;
    }
    if (((uint16_t)(Arg2 - 97)) <= 25) goto loc_0090EB56;
loc_0090EB2C:
    if (Arg2 == 0) goto loc_0090EB60;
    if (((uint32_t)(local_rsi)) >= ((uint32_t)(local_r14))) goto loc_0090EB60;
    if (((uint8_t)(*(uint8_t *)(v_stack_m50 + 0x3))) >= 6) goto loc_0090EB60;
    if (v_stack_m68 != 0) goto loc_0090ECD3;
loc_0090EB49:
    *(uint16_t *)(v_stack_m50 + *(uint8_t *)(v_stack_m50 + 0x3) * 2 + 0x4) = Arg2;
    goto loc_0090EABB;
loc_0090EB56:
    Arg2 = (uint16_t)((Arg2) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
    goto loc_0090EB2C;
loc_0090EB60:
    local_rbp = 0;
    if (v_stack_m68 == 0) {
        local_rbp = *(uint8_t *)(v_stack_m50 + 0x3);
    }
    if (((uint32_t)(local_rbp)) <= 2) goto loc_0090EF57;
    result = (uint32_t)(((uint32_t)(0xFFE0ULL)) | (0xFFFFFFFFULL));
    if (((uint32_t)(local_r14)) != ((uint32_t)(result))) goto loc_0090ED21;
    *(uint32_t *)(v_stack_m50 + 0x14) = 0;
loc_0090EB8A:
loc_0090EB8F:
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m50 + 0x20))) + 1);
    *(uint32_t *)(v_stack_m50 + 0x20) = (uint32_t)(Arg4);
    if (((uint32_t)(Arg4)) > 4) goto loc_0090EE6A;
loc_0090EBA9:
loc_0090EBB9:
    if ((uint32_t)(Arg4) == 0) goto loc_0090EC03;
    Arg2 = (uint32_t)((Arg2) >> (3));
    result = (uint16_t)((Arg2) << (2));
    Arg1 = (uint16_t)((result + Arg2 * 1) + ((uint16_t)(result + Arg2 * 1)));
    result = (uint32_t)(((uint32_t)((uint32_t)(1 + 7))) - (1));
    Arg4 = (uint16_t)((Arg4) - ((uint16_t)(Arg1)));
    local_rsi = (uint32_t)((1) + 1);
    *(uint16_t *)(local_rsp + result * 2 + 0x38) = (uint16_t)(1 + 47 + Arg4 * 1);
    Arg1 = 0;
    if (((uint16_t)(1 + 47 + Arg4 * 1)) == 57) { Arg1 = (uint32_t)((uint8_t)(v_stack_m67)); }
    if (((uint32_t)(local_rsi)) <= ((uint32_t)(1 + 6))) goto loc_0090EBB9;
loc_0090EC03:
    local_r10 = (uint32_t)((1 + 7) - ((uint32_t)(local_rsi)));
    v_stack_m67 = (uint8_t)((uint8_t)(Arg1));
    *(uint16_t *)(v_stack_m50 + local_r10 * 2) = 126;
    if (((uint8_t)(*(uint8_t *)(v_stack_m50 + 0x3) - 1)) > 11) goto loc_0090EFAE;
    Arg3 = ((uint32_t)((uint32_t)(*(uint8_t *)(v_stack_m50 + 0x3)))) + ((uint32_t)((uint32_t)(*(uint8_t *)(v_stack_m50 + 0x3))));
    result = memcpy(*(uint64_t *)(v_stack_m58 + 0x8), v_stack_m50 + 4, Arg3, (uint32_t)(Arg2));
    Arg1 = (uint16_t)((*(uint8_t *)(v_stack_m50 + 0x3)) + ((uint16_t)(*(uint8_t *)(v_stack_m50 + 0x3))));
loc_0090EC48:
    *(uint16_t *)(v_stack_m58) = (uint16_t)(Arg1);
    Arg1 = ((uint16_t)(Arg1)) >> (1);
    result = memcpy(*(uint64_t *)(v_stack_m58 + 0x8) + Arg1 * 2, v_stack_m50 + local_r10 * 2, local_rsi + local_rsi * 1, (uint32_t)(Arg2));
    Arg1 = (uint16_t)(((uint16_t)(local_rsi)) + ((uint16_t)((uint16_t)(local_rsi))));
    Arg1 = (uint16_t)((Arg1) + (*(uint16_t *)(v_stack_m58)));
    *(uint16_t *)(v_stack_m58) = (uint16_t)(Arg1);
    result = (uint32_t)(*(uint32_t *)(v_stack_m50 + 0x14));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m50 + 0x14))) != 0) {
        Arg1 = (uint16_t)(Arg1);
        Arg3 = (uint32_t)(*(uint32_t *)(v_stack_m50 + 0x14)) + (uint32_t)(*(uint32_t *)(v_stack_m50 + 0x14)) * 1;
        result = *(uint64_t *)(v_stack_m58 + 0x8);
        Arg2 = v_stack_m50 + 24;
        Arg1 = (Arg1) >> (1);
        Arg1 = result + Arg1 * 2;
        result = memcpy(Arg1, Arg2, Arg3, (uint32_t)(Arg2));
        result = *(uint16_t *)(v_stack_m50 + 0x14);
        result = (uint16_t)((result) + ((uint16_t)(result)));
    }
    if (v_stack_m67 != 0) goto loc_0090EFB5;
    result = 0;
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, (uint32_t)(Arg2));
    local_rsp = (local_rsp) + (80);
    return result;
loc_0090ECD3:
    if (Arg2 > 127) goto loc_0090EEF8;
loc_0090ECDD:
loc_0090ECE2:
    local_rbp = (uint32_t)((1 + 6) + (1));
    if (((uint32_t)(local_rbp)) <= 6) goto loc_0090EB49;
    goto loc_0090EB6A;
loc_0090ECF2:
    if ((uint8_t)(v_stack_m68) == 0) goto loc_0090ED0F;
    result = RtlIsValidOemCharacter(v_stack_p24, Arg2, Arg3, (uint32_t)(Arg2));
    if ((uint8_t)(result) != 0) goto loc_0090EF39;
loc_0090ED0F:
    goto loc_0090EA12;
loc_0090ED16:
    if ((uint8_t)(local_rsi) == 0) goto loc_0090EA51;
    goto loc_0090ED0F;
loc_0090ED21:
    *(uint16_t *)(v_stack_m50 + 0x18) = 46;
    *(uint32_t *)(v_stack_m50 + 0x14) = 1;
loc_0090ED2E:
loc_0090ED31:
    result = (uint32_t)((*(uint16_t *)(v_stack_m58)) >> (1));
    if (((uint32_t)(v_stack_m50 + local_r10 * 2)) >= ((uint32_t)(result))) goto loc_0090EDA0;
    local_r14 = (uint32_t)((v_stack_m50 + local_r10 * 2) + 1);
    v_stack_p24 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m58 + 0x8) + v_stack_m50 + local_r10 * 2 * 2));
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m58 + 0x8) + v_stack_m50 + local_r10 * 2 * 2))) <= 32) goto loc_0090EE63;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m58 + 0x8) + v_stack_m50 + local_r10 * 2 * 2))) >= 127) goto loc_0090EE46;
loc_0090ED61:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m58 + 0x8) + v_stack_m50 + local_r10 * 2 * 2))) == 46) goto loc_0090EE63;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m58 + 0x8) + v_stack_m50 + local_r10 * 2 * 2))) >= 128) goto loc_0090ED97;
    result = ((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m58 + 0x8) + v_stack_m50 + local_r10 * 2 * 2))) >> (5);
    Arg1 = (uint32_t)(((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_m58 + 0x8) + v_stack_m50 + local_r10 * 2 * 2))) & (31));
    if (!(condition_is_above_or_equal)) {
        Arg2 = 95;
    }
    if (((uint16_t)(Arg2 - 97)) <= 25) goto loc_0090EDC0;
loc_0090EDA0:
    if (Arg2 == 0) goto loc_0090EDCA;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m50 + 0x14)))) >= 4) goto loc_0090EE21;
    if (v_stack_p20 != ((uint8_t)(v_stack_p10))) goto loc_0090EE0B;
loc_0090EDB3:
    *(uint16_t *)(v_stack_m50 + (uint32_t)(*(uint32_t *)(v_stack_m50 + 0x14)) * 2 + 0x18) = Arg2;
    goto loc_0090ED2E;
loc_0090EDC0:
    Arg2 = (uint16_t)((Arg2) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
    goto loc_0090EDA0;
loc_0090EDCA:
    goto loc_0090EB8A;
loc_0090EDD4:
    if ((uint8_t)(v_stack_m68) == 0) goto loc_0090EDF1;
    result = RtlIsValidOemCharacter(v_stack_p24, Arg2, v_rip + 2344929, 46);
    if ((uint8_t)(result) != 0) goto loc_0090EF43;
loc_0090EDF1:
    goto loc_0090EABE;
loc_0090EDF8:
    v_stack_p20 = (uint8_t)(local_r14);
    if (48 != 0) goto loc_0090E9D1;
    goto loc_0090E9CD;
loc_0090EE0B:
    if (((uint16_t)((uint32_t)((uint32_t)(v_stack_p10)))) > 127) goto loc_0090EF76;
loc_0090EE15:
loc_0090EE1A:
    local_rsi = (uint32_t)((48) + (1));
    if (((uint32_t)(local_rsi)) <= 4) goto loc_0090EDB3;
loc_0090EE21:
    if ((*(uint8_t *)(v_rip + 0x6C9218)) == ((uint8_t)(v_stack_p10))) goto loc_0090EB8F;
    *(uint16_t *)(v_stack_m50 + v_stack_p24 - 0x1 * 2 + 0x18) = 126;
    goto loc_0090EB8F;
loc_0090EE46:
    if ((uint8_t)(v_stack_m68) == 0) goto loc_0090EE63;
    result = RtlIsValidOemCharacter(v_stack_p24, (uint32_t)((uint32_t)(v_stack_p10)), v_rip + 2344929, 46);
    if ((uint8_t)(result) != 0) goto loc_0090EF4D;
loc_0090EE63:
    goto loc_0090ED31;
loc_0090EE6A:
    if ((*(uint8_t *)(v_stack_m50 + 0x2)) != ((uint8_t)(v_stack_p10))) goto loc_0090EBA9;
    if ((uint8_t)(v_stack_m68) != 0) goto loc_0090EF15;
loc_0090EE7F:
    result = RtlComputeLfnChecksum(v_stack_m58, (uint32_t)((uint32_t)(v_stack_p10)), v_rip + 2344929, 46);
    *(uint16_t *)(v_stack_m50) = (uint16_t)(result);
    Arg3 = (uint32_t)((2) - ((uint32_t)((uint32_t)((uint32_t)(v_stack_p10)))));
    Arg2 = (uint32_t)((6) - ((uint32_t)((uint32_t)((uint32_t)(v_stack_p10)))));
    if (((uint32_t)(Arg3)) >= Arg2) goto loc_0090EEDB;
    Arg4 = ((uint32_t)((uint32_t)(Arg3))) + (2);
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(Arg3)));
loc_0090EEB3:
    Arg1 = (uint16_t)(((uint16_t)((uint16_t)(result))) & (15));
    result = 48;
    if (((uint16_t)(Arg1)) > 9) { result = (uint16_t)(local_rbp); }
    local_r11 = (uint16_t)(((uint16_t)(result)) >> (4));
    result = (uint16_t)((result) + ((uint16_t)(Arg1)));
    *(uint16_t *)(v_stack_m50 + Arg4 * 2) = (uint16_t)(result);
    Arg3 = ((uint32_t)(Arg2)) - (1);
    if (condition_is_not_equal) goto loc_0090EEB3;
loc_0090EEDB:
    local_r12 = (uint8_t)((6) - ((uint8_t)((uint32_t)((uint32_t)(v_stack_p10)))));
    *(uint32_t *)(v_stack_m50 + 0x20) = 1;
    *(uint8_t *)(v_stack_m50 + 0x3) = (uint8_t)(local_r12);
    *(uint8_t *)(v_stack_m50 + 0x2) = 1;
    goto loc_0090EBA9;
loc_0090EEF8:
    if ((*(uint8_t *)(v_stack_p28 + Arg2 * 2 + 0x1)) != ((uint8_t)(v_stack_p10))) goto loc_0090ECE2;
    goto loc_0090ECDD;
loc_0090EF15:
    if (((uint32_t)(*(uint16_t *)(v_stack_m50 + 0x4))) > 127) goto loc_0090EF93;
loc_0090EF23:
loc_0090EF25:
    if (((uint32_t)(*(uint16_t *)(v_stack_m50 + 0x6))) > 127) goto loc_0090EFA0;
loc_0090EF2E:
loc_0090EF31:
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p10))) | ((uint32_t)((uint32_t)((uint32_t)(v_stack_p10)))));
    goto loc_0090EE7F;
loc_0090EF39:
    goto loc_0090EA41;
loc_0090EF43:
    goto loc_0090EAED;
loc_0090EF4D:
    goto loc_0090ED61;
loc_0090EF57:
    result = RtlComputeLfnChecksum(v_stack_m58, v_stack_p24, v_stack_p28, 1);
    *(uint16_t *)(v_stack_m50) = (uint16_t)(result);
loc_0090EF76:
    if ((*(uint8_t *)(v_stack_p28 + (uint16_t)(v_stack_p24) * 2 + 0x1)) != ((uint8_t)(v_stack_p10))) goto loc_0090EE1A;
    goto loc_0090EE15;
loc_0090EF93:
    if ((*(uint8_t *)(v_stack_p24 + 0x2 * 2 + 0x1)) != ((uint8_t)(v_stack_p10))) goto loc_0090EF25;
    goto loc_0090EF23;
loc_0090EFA0:
    if ((*(uint8_t *)(v_stack_p24 + 0x2 * 2 + 0x1)) != ((uint8_t)(v_stack_p10))) goto loc_0090EF31;
    goto loc_0090EF2E;
loc_0090EFAE:
    goto loc_0090EC48;
loc_0090EFB5:
    local_rbp = (uint32_t)((48 + 7) - (48));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x3` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0090E950&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
