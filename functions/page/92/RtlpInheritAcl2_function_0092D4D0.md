# RtlpInheritAcl2

- RVA: `0x0092D4D0`–`0x0092DB6F` (길이 `1,695` bytes)
- VA: `0x000000014092D4D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008DBB4`
- 디코드: `383`개 명령, `1,695/1,695` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0092D55D` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0092D760` → [RtlpCopyAces](RtlpCopyAces_function_0092E020.md) (function, `0x0092E020`)
- `0x0092D911` → [RtlpGenerateInheritedAce](RtlpGenerateInheritedAce_function_0092DB80.md) (function, `0x0092DB80`)
- `0x0092DA0D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092DA7B` → [RtlFindAceByType](../../text/41/RtlFindAceByType_function_00410AF0.md) (function, `0x00410AF0`)

### Direct callers
- [RtlpNewSecurityObject](RtlpNewSecurityObject_function_0092AB50.md) at `0x0092B3B6`
- [RtlpNewSecurityObject](RtlpNewSecurityObject_function_0092AB50.md) at `0x0092B647`
- [RtlpNewSecurityObject](RtlpNewSecurityObject_function_0092AB50.md) at `0x0092C0C9`
- [RtlpNewSecurityObject](RtlpNewSecurityObject_function_0092AB50.md) at `0x0092C1D3`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0092D55D` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0092DA0D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092DA7B` → [RtlFindAceByType](../../text/41/RtlFindAceByType_function_00410AF0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0092D4D0  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
0092D4D5  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0092D4DA  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0092D4DF  53                              push rbx
0092D4E0  55                              push rbp
0092D4E1  56                              push rsi
0092D4E2  57                              push rdi
0092D4E3  41 54                           push r12
0092D4E5  41 55                           push r13
0092D4E7  41 56                           push r14
0092D4E9  41 57                           push r15
0092D4EB  48 81 EC 98 00 00 00            sub rsp, 0x98
0092D4F2  48 8B BC 24 50 01 00 00         mov rdi, qword ptr [rsp + 0x150]
0092D4FA  45 33 F6                        xor r14d, r14d
0092D4FD  48 8B 9C 24 58 01 00 00         mov rbx, qword ptr [rsp + 0x158]
0092D505  41 BD 02 00 00 00               mov r13d, 2
0092D50B  45 32 FF                        xor r15b, r15b
0092D50E  44 89 74 24 74                  mov dword ptr [rsp + 0x74], r14d
0092D513  41 8B F6                        mov esi, r14d
0092D516  66 44 89 74 24 7C               mov word ptr [rsp + 0x7c], r14w
0092D51C  8B 3F                           mov edi, dword ptr [rdi]
0092D51E  45 0F B6 D9                     movzx r11d, r9b
0092D522  41 8B E8                        mov ebp, r8d
0092D525  4C 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r14
0092D52D  4C 8B D2                        mov r10, rdx
0092D530  40 88 B4 24 F0 00 00 00         mov byte ptr [rsp + 0xf0], sil
0092D538  45 8B C6                        mov r8d, r14d
0092D53B  C6 44 24 70 01                  mov byte ptr [rsp + 0x70], 1
0092D540  8D 47 F8                        lea eax, [rdi - 8]
0092D543  44 89 6C 24 78                  mov dword ptr [rsp + 0x78], r13d
0092D548  45 8B E6                        mov r12d, r14d
0092D54B  45 8B CD                        mov r9d, r13d
0092D54E  3D F4 FF 00 00                  cmp eax, 0xfff4
0092D553  77 38                           ja 0x14092d58d
0092D555  44 8B C7                        mov r8d, edi
0092D558  33 D2                           xor edx, edx
0092D55A  48 8B CB                        mov rcx, rbx
0092D55D  E8 DE 96 D9 FF                  call 0x1406c6c40
0092D562  4C 8B 94 24 E8 00 00 00         mov r10, qword ptr [rsp + 0xe8]
0092D56A  B8 FC FF 00 00                  mov eax, 0xfffc
0092D56F  44 0F B6 9C 24 F8 00 00 00      movzx r11d, byte ptr [rsp + 0xf8]
0092D578  66 23 F8                        and di, ax
0092D57B  66 89 7B 02                     mov word ptr [rbx + 2], di
0092D57F  45 8B C6                        mov r8d, r14d
0092D582  66 44 89 2B                     mov word ptr [rbx], r13w
0092D586  45 8B CD                        mov r9d, r13d
0092D589  44 89 73 04                     mov dword ptr [rbx + 4], r14d
0092D58D  48 8B 84 24 60 01 00 00         mov rax, qword ptr [rsp + 0x160]
0092D595  44 8B F5                        mov r14d, ebp
0092D598  0F B6 BC 24 00 01 00 00         movzx edi, byte ptr [rsp + 0x100]
0092D5A0  40 88 30                        mov byte ptr [rax], sil
0092D5A3  40 0F B6 C7                     movzx eax, dil
0092D5A7  F6 D8                           neg al
0092D5A9  48 8B 84 24 68 01 00 00         mov rax, qword ptr [rsp + 0x168]
0092D5B1  1B C9                           sbb ecx, ecx
0092D5B3  81 E1 00 04 00 00               and ecx, 0x400
0092D5B9  89 08                           mov dword ptr [rax], ecx
0092D5BB  41 83 E6 08                     and r14d, 8
0092D5BF  75 20                           jne 0x14092d5e1
0092D5C1  8B D5                           mov edx, ebp
0092D5C3  81 E2 00 10 00 00               and edx, 0x1000
0092D5C9  74 09                           je 0x14092d5d4
0092D5CB  0F BA E9 0C                     bts ecx, 0xc
0092D5CF  41 B7 01                        mov r15b, 1
0092D5D2  89 08                           mov dword ptr [rax], ecx
0092D5D4  8B C5                           mov eax, ebp
0092D5D6  25 04 10 00 00                  and eax, 0x1004
0092D5DB  0F 85 D9 00 00 00               jne 0x14092d6ba
0092D5E1  4C 8B AC 24 60 01 00 00         mov r13, qword ptr [rsp + 0x160]
0092D5E9  40 84 FF                        test dil, dil
0092D5EC  75 0A                           jne 0x14092d5f8
0092D5EE  40 F6 C5 04                     test bpl, 4
0092D5F2  0F 84 9B 00 00 00               je 0x14092d693
0092D5F8  45 85 F6                        test r14d, r14d
0092D5FB  0F 85 92 00 00 00               jne 0x14092d693
0092D601  40 84 FF                        test dil, dil
0092D604  74 09                           je 0x14092d60f
0092D606  45 84 FF                        test r15b, r15b
0092D609  0F 84 84 00 00 00               je 0x14092d693
0092D60F  0F B6 AC 24 F0 00 00 00         movzx ebp, byte ptr [rsp + 0xf0]
0092D617  45 33 D2                        xor r10d, r10d
0092D61A  8B 7C 24 74                     mov edi, dword ptr [rsp + 0x74]
0092D61E  42 8D 04 26                     lea eax, [rsi + r12]
0092D622  85 C0                           test eax, eax
0092D624  75 2F                           jne 0x14092d655
0092D626  41 38 45 00                     cmp byte ptr [r13], al
0092D62A  0F 85 FF 03 00 00               jne 0x14092da2f
0092D630  48 8B 84 24 50 01 00 00         mov rax, qword ptr [rsp + 0x150]
0092D638  44 89 10                        mov dword ptr [rax], r10d
0092D63B  B8 0B 00 00 80                  mov eax, 0x8000000b
0092D640  48 81 C4 98 00 00 00            add rsp, 0x98
0092D647  41 5F                           pop r15
0092D649  41 5E                           pop r14
0092D64B  41 5D                           pop r13
0092D64D  41 5C                           pop r12
0092D64F  5F                              pop rdi
0092D650  5E                              pop rsi
0092D651  5D                              pop rbp
0092D652  5B                              pop rbx
0092D653  C3                              ret
0092D654  CC                              int3
0092D655  48 83 C0 08                     add rax, 8
0092D659  48 3D FF FF 00 00               cmp rax, 0xffff
0092D65F  0F 87 E7 03 00 00               ja 0x14092da4c
0092D665  48 8B 84 24 50 01 00 00         mov rax, qword ptr [rsp + 0x150]
0092D66D  8D 4F 08                        lea ecx, [rdi + 8]
0092D670  03 CE                           add ecx, esi
0092D672  89 08                           mov dword ptr [rax], ecx
0092D674  40 84 ED                        test bpl, bpl
0092D677  0F 85 A8 03 00 00               jne 0x14092da25
0092D67D  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
0092D681  66 83 C6 08                     add si, 8
0092D685  66 41 03 F4                     add si, r12w
0092D689  88 03                           mov byte ptr [rbx], al
0092D68B  66 89 73 02                     mov word ptr [rbx + 2], si
0092D68F  33 C0                           xor eax, eax
0092D691  EB AD                           jmp 0x14092d640
0092D693  4C 8B 84 24 E0 00 00 00         mov r8, qword ptr [rsp + 0xe0]
0092D69B  4D 85 C0                        test r8, r8
0092D69E  0F 84 6B FF FF FF               je 0x14092d60f
0092D6A4  41 0F B6 08                     movzx ecx, byte ptr [r8]
0092D6A8  8D 41 FE                        lea eax, [rcx - 2]
0092D6AB  3C 02                           cmp al, 2
0092D6AD  0F 86 64 01 00 00               jbe 0x14092d817
0092D6B3  B8 58 00 00 C0                  mov eax, 0xc0000058
0092D6B8  EB 86                           jmp 0x14092d640
0092D6BA  4D 85 D2                        test r10, r10
0092D6BD  0F 84 CB 03 00 00               je 0x14092da8e
0092D6C3  41 0F B6 02                     movzx eax, byte ptr [r10]
0092D6C7  41 3B C5                        cmp eax, r13d
0092D6CA  40 88 74 24 70                  mov byte ptr [rsp + 0x70], sil
0092D6CF  44 0F 43 C8                     cmovae r9d, eax
0092D6D3  44 89 4C 24 78                  mov dword ptr [rsp + 0x78], r9d
0092D6D8  40 84 FF                        test dil, dil
0092D6DB  0F 84 E3 00 00 00               je 0x14092d7c4
0092D6E1  85 D2                           test edx, edx
0092D6E3  0F 85 D1 03 00 00               jne 0x14092daba
0092D6E9  41 BD 01 00 00 00               mov r13d, 1
0092D6EF  45 32 C9                        xor r9b, r9b
0092D6F2  41 0F B6 C5                     movzx eax, r13b
0092D6F6  48 8B 94 24 30 01 00 00         mov rdx, qword ptr [rsp + 0x130]
0092D6FE  48 8D 4C 24 74                  lea rcx, [rsp + 0x74]
0092D703  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
0092D708  45 8B C5                        mov r8d, r13d
0092D70B  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
0092D710  8B 8C 24 38 01 00 00            mov ecx, dword ptr [rsp + 0x138]
0092D717  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
0092D71B  48 8B 8C 24 28 01 00 00         mov rcx, qword ptr [rsp + 0x128]
0092D723  40 88 74 24 50                  mov byte ptr [rsp + 0x50], sil
0092D728  44 88 5C 24 48                  mov byte ptr [rsp + 0x48], r11b
0092D72D  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
0092D732  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
0092D73A  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0092D73F  48 8B 8C 24 18 01 00 00         mov rcx, qword ptr [rsp + 0x118]
0092D747  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0092D74C  48 8B 8C 24 10 01 00 00         mov rcx, qword ptr [rsp + 0x110]
0092D754  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
0092D759  49 8B CA                        mov rcx, r10
0092D75C  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0092D760  E8 BB 08 00 00                  call 0x14092e020
0092D765  44 8B 44 24 74                  mov r8d, dword ptr [rsp + 0x74]
0092D76A  3D 23 00 00 C0                  cmp eax, 0xc0000023
0092D76F  45 8B E0                        mov r12d, r8d
0092D772  0F 94 84 24 F0 00 00 00         sete byte ptr [rsp + 0xf0]
0092D77A  45 33 C9                        xor r9d, r9d
0092D77D  3D 23 00 00 C0                  cmp eax, 0xc0000023
0092D782  41 8B C9                        mov ecx, r9d
0092D785  0F 45 C8                        cmovne ecx, eax
0092D788  85 C9                           test ecx, ecx
0092D78A  0F 88 80 00 00 00               js 0x14092d810
0092D790  40 38 B4 24 08 01 00 00         cmp byte ptr [rsp + 0x108], sil
0092D798  0F 85 26 03 00 00               jne 0x14092dac4
0092D79E  4C 8B 94 24 E8 00 00 00         mov r10, qword ptr [rsp + 0xe8]
0092D7A6  8B 8C 24 38 01 00 00            mov ecx, dword ptr [rsp + 0x138]
0092D7AD  83 F9 01                        cmp ecx, 1
0092D7B0  75 1C                           jne 0x14092d7ce
0092D7B2  4C 8B AC 24 60 01 00 00         mov r13, qword ptr [rsp + 0x160]
0092D7BA  41 C6 45 00 01                  mov byte ptr [r13], 1
0092D7BF  E9 25 FE FF FF                  jmp 0x14092d5e9
0092D7C4  45 32 C9                        xor r9b, r9b
0092D7C7  32 C0                           xor al, al
0092D7C9  E9 28 FF FF FF                  jmp 0x14092d6f6
0092D7CE  83 F9 02                        cmp ecx, 2
0092D7D1  0F 85 0A FE FF FF               jne 0x14092d5e1
0092D7D7  45 85 C0                        test r8d, r8d
0092D7DA  75 D6                           jne 0x14092d7b2
0092D7DC  45 84 FF                        test r15b, r15b
0092D7DF  75 D1                           jne 0x14092d7b2
0092D7E1  45 85 C0                        test r8d, r8d
0092D7E4  0F 85 F7 FD FF FF               jne 0x14092d5e1
0092D7EA  4D 85 D2                        test r10, r10
0092D7ED  0F 84 EE FD FF FF               je 0x14092d5e1
0092D7F3  66 41 39 72 04                  cmp word ptr [r10 + 4], si
0092D7F8  0F 85 E3 FD FF FF               jne 0x14092d5e1
0092D7FE  4C 8B AC 24 60 01 00 00         mov r13, qword ptr [rsp + 0x160]
0092D806  41 C6 45 00 01                  mov byte ptr [r13], 1
0092D80B  E9 D9 FD FF FF                  jmp 0x14092d5e9
0092D810  8B C1                           mov eax, ecx
0092D812  E9 29 FE FF FF                  jmp 0x14092d640
0092D817  8B C1                           mov eax, ecx
0092D819  40 88 B4 24 00 01 00 00         mov byte ptr [rsp + 0x100], sil
0092D821  8B 4C 24 78                     mov ecx, dword ptr [rsp + 0x78]
0092D825  49 8D 68 08                     lea rbp, [r8 + 8]
0092D829  3B C8                           cmp ecx, eax
0092D82B  0F 46 C8                        cmovbe ecx, eax
0092D82E  45 33 D2                        xor r10d, r10d
0092D831  41 8B D2                        mov edx, r10d
0092D834  89 4C 24 78                     mov dword ptr [rsp + 0x78], ecx
0092D838  89 94 24 68 01 00 00            mov dword ptr [rsp + 0x168], edx
0092D83F  45 32 F6                        xor r14b, r14b
0092D842  88 94 24 60 01 00 00            mov byte ptr [rsp + 0x160], dl
0092D849  45 8B FA                        mov r15d, r10d
0092D84C  44 89 94 24 80 00 00 00         mov dword ptr [rsp + 0x80], r10d
0092D854  44 89 94 24 84 00 00 00         mov dword ptr [rsp + 0x84], r10d
0092D85C  41 0F B7 40 04                  movzx eax, word ptr [r8 + 4]
0092D861  44 3B F8                        cmp r15d, eax
0092D864  0F 83 17 01 00 00               jae 0x14092d981
0092D86A  80 7D 00 11                     cmp byte ptr [rbp], 0x11
0092D86E  0F 84 EF 01 00 00               je 0x14092da63
0092D874  83 BC 24 38 01 00 00 03         cmp dword ptr [rsp + 0x138], 3
0092D87C  0F 84 E9 00 00 00               je 0x14092d96b
0092D882  4C 8B 8C 24 10 01 00 00         mov r9, qword ptr [rsp + 0x110]
0092D88A  48 8D 84 24 00 01 00 00         lea rax, [rsp + 0x100]
0092D892  0F B6 94 24 F8 00 00 00         movzx edx, byte ptr [rsp + 0xf8]
0092D89A  44 0F B6 C7                     movzx r8d, dil
0092D89E  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0092D8A3  48 8B CD                        mov rcx, rbp
0092D8A6  48 8D 84 24 84 00 00 00         lea rax, [rsp + 0x84]
0092D8AE  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0092D8B3  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
0092D8BB  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
0092D8C0  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0092D8C5  8B 84 24 48 01 00 00            mov eax, dword ptr [rsp + 0x148]
0092D8CC  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0092D8D0  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
0092D8D8  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0092D8DD  48 8B 84 24 30 01 00 00         mov rax, qword ptr [rsp + 0x130]
0092D8E5  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0092D8EA  48 8B 84 24 28 01 00 00         mov rax, qword ptr [rsp + 0x128]
0092D8F2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0092D8F7  48 8B 84 24 20 01 00 00         mov rax, qword ptr [rsp + 0x120]
0092D8FF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0092D904  48 8B 84 24 18 01 00 00         mov rax, qword ptr [rsp + 0x118]
0092D90C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0092D911  E8 6A 02 00 00                  call 0x14092db80
0092D916  3D 23 00 00 C0                  cmp eax, 0xc0000023
0092D91B  0F 85 DA 01 00 00               jne 0x14092dafb
0092D921  41 B6 01                        mov r14b, 1
0092D924  80 BC 24 00 01 00 00 00         cmp byte ptr [rsp + 0x100], 0
0092D92C  0F 85 30 02 00 00               jne 0x14092db62
0092D932  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
0092D939  03 F0                           add esi, eax
0092D93B  8B 94 24 68 01 00 00            mov edx, dword ptr [rsp + 0x168]
0092D942  8B 8C 24 84 00 00 00            mov ecx, dword ptr [rsp + 0x84]
0092D949  3B C2                           cmp eax, edx
0092D94B  77 0D                           ja 0x14092d95a
0092D94D  2B D0                           sub edx, eax
0092D94F  89 94 24 68 01 00 00            mov dword ptr [rsp + 0x168], edx
0092D956  3B D1                           cmp edx, ecx
0092D958  77 09                           ja 0x14092d963
0092D95A  8B D1                           mov edx, ecx
0092D95C  89 8C 24 68 01 00 00            mov dword ptr [rsp + 0x168], ecx
0092D963  4C 8B 84 24 E0 00 00 00         mov r8, qword ptr [rsp + 0xe0]
0092D96B  0F B7 45 02                     movzx eax, word ptr [rbp + 2]
0092D96F  41 FF C7                        inc r15d
0092D972  48 03 E8                        add rbp, rax
0092D975  E9 E2 FE FF FF                  jmp 0x14092d85c
0092D97A  8B 94 24 68 01 00 00            mov edx, dword ptr [rsp + 0x168]
0092D981  45 84 F6                        test r14b, r14b
0092D984  0F 85 CC 00 00 00               jne 0x14092da56
0092D98A  0F B6 AC 24 F0 00 00 00         movzx ebp, byte ptr [rsp + 0xf0]
0092D992  40 84 ED                        test bpl, bpl
0092D995  0F 85 BB 00 00 00               jne 0x14092da56
0092D99B  45 33 D2                        xor r10d, r10d
0092D99E  80 BC 24 08 01 00 00 00         cmp byte ptr [rsp + 0x108], 0
0092D9A6  8B 7C 24 74                     mov edi, dword ptr [rsp + 0x74]
0092D9AA  0F 84 6E FC FF FF               je 0x14092d61e
0092D9B0  85 FF                           test edi, edi
0092D9B2  0F 84 66 FC FF FF               je 0x14092d61e
0092D9B8  80 BC 24 60 01 00 00 00         cmp byte ptr [rsp + 0x160], 0
0092D9C0  0F 84 58 FC FF FF               je 0x14092d61e
0092D9C6  40 84 ED                        test bpl, bpl
0092D9C9  0F 85 4F FC FF FF               jne 0x14092d61e
0092D9CF  44 0F B7 43 04                  movzx r8d, word ptr [rbx + 4]
0092D9D4  48 8D 4B 08                     lea rcx, [rbx + 8]
0092D9D8  41 8B D2                        mov edx, r10d
0092D9DB  41 3B D0                        cmp edx, r8d
0092D9DE  0F 82 60 01 00 00               jb 0x14092db44
0092D9E4  44 0F B7 43 02                  movzx r8d, word ptr [rbx + 2]
0092D9E9  4C 03 C3                        add r8, rbx
0092D9EC  49 3B C8                        cmp rcx, r8
0092D9EF  49 0F 47 CA                     cmova rcx, r10
0092D9F3  48 85 C9                        test rcx, rcx
0092D9F6  75 03                           jne 0x14092d9fb
0092D9F8  49 8B C8                        mov rcx, r8
0092D9FB  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
0092DA03  48 2B CA                        sub rcx, rdx
0092DA06  44 8B C1                        mov r8d, ecx
0092DA09  48 8D 4B 08                     lea rcx, [rbx + 8]
0092DA0D  E8 2E 8E D9 FF                  call 0x1406c6840
0092DA12  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
0092DA16  66 29 43 04                     sub word ptr [rbx + 4], ax
0092DA1A  45 33 D2                        xor r10d, r10d
0092DA1D  45 8B E2                        mov r12d, r10d
0092DA20  E9 F9 FB FF FF                  jmp 0x14092d61e
0092DA25  B8 23 00 00 C0                  mov eax, 0xc0000023
0092DA2A  E9 11 FC FF FF                  jmp 0x14092d640
0092DA2F  80 7C 24 70 00                  cmp byte ptr [rsp + 0x70], 0
0092DA34  0F 84 1B FC FF FF               je 0x14092d655
0092DA3A  48 8B 84 24 50 01 00 00         mov rax, qword ptr [rsp + 0x150]
0092DA42  44 89 10                        mov dword ptr [rax], r10d
0092DA45  33 C0                           xor eax, eax
0092DA47  E9 F4 FB FF FF                  jmp 0x14092d640
0092DA4C  B8 7D 00 00 C0                  mov eax, 0xc000007d
0092DA51  E9 EA FB FF FF                  jmp 0x14092d640
0092DA56  03 F2                           add esi, edx
0092DA58  40 B5 01                        mov bpl, 1
0092DA5B  45 33 D2                        xor r10d, r10d
0092DA5E  E9 3B FF FF FF                  jmp 0x14092d99e
0092DA63  83 BC 24 38 01 00 00 03         cmp dword ptr [rsp + 0x138], 3
0092DA6B  0F 85 FA FE FF FF               jne 0x14092d96b
0092DA71  45 33 C0                        xor r8d, r8d
0092DA74  48 8B CB                        mov rcx, rbx
0092DA77  41 8D 50 11                     lea edx, [r8 + 0x11]
0092DA7B  E8 70 30 AE FF                  call 0x140410af0
0092DA80  48 85 C0                        test rax, rax
0092DA83  0F 84 F9 FD FF FF               je 0x14092d882
0092DA89  E9 EC FE FF FF                  jmp 0x14092d97a
0092DA8E  40 84 FF                        test dil, dil
0092DA91  0F 84 0F FD FF FF               je 0x14092d7a6
0092DA97  8B 8C 24 38 01 00 00            mov ecx, dword ptr [rsp + 0x138]
0092DA9E  83 F9 01                        cmp ecx, 1
0092DAA1  0F 85 27 FD FF FF               jne 0x14092d7ce
0092DAA7  83 F8 04                        cmp eax, 4
0092DAAA  0F 85 02 FD FF FF               jne 0x14092d7b2
0092DAB0  B8 77 00 00 C0                  mov eax, 0xc0000077
0092DAB5  E9 86 FB FF FF                  jmp 0x14092d640
0092DABA  41 B1 10                        mov r9b, 0x10
0092DABD  B0 01                           mov al, 1
0092DABF  E9 32 FC FF FF                  jmp 0x14092d6f6
0092DAC4  45 85 C0                        test r8d, r8d
0092DAC7  0F 84 D1 FC FF FF               je 0x14092d79e
0092DACD  0F B7 43 04                     movzx eax, word ptr [rbx + 4]
0092DAD1  48 8D 53 08                     lea rdx, [rbx + 8]
0092DAD5  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
0092DAD9  41 8B C9                        mov ecx, r9d
0092DADC  3B C8                           cmp ecx, eax
0092DADE  0F B7 43 02                     movzx eax, word ptr [rbx + 2]
0092DAE2  72 45                           jb 0x14092db29
0092DAE4  48 03 C3                        add rax, rbx
0092DAE7  48 3B D0                        cmp rdx, rax
0092DAEA  49 0F 47 D1                     cmova rdx, r9
0092DAEE  48 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdx
0092DAF6  E9 A3 FC FF FF                  jmp 0x14092d79e
0092DAFB  85 C0                           test eax, eax
0092DAFD  0F 89 21 FE FF FF               jns 0x14092d924
0092DB03  45 33 D2                        xor r10d, r10d
0092DB06  3D 23 00 00 C0                  cmp eax, 0xc0000023
0092DB0B  41 8B CA                        mov ecx, r10d
0092DB0E  41 8B F2                        mov esi, r10d
0092DB11  0F 45 C8                        cmovne ecx, eax
0092DB14  85 C9                           test ecx, ecx
0092DB16  0F 88 F4 FC FF FF               js 0x14092d810
0092DB1C  0F B6 AC 24 F0 00 00 00         movzx ebp, byte ptr [rsp + 0xf0]
0092DB24  E9 75 FE FF FF                  jmp 0x14092d99e
0092DB29  48 03 C3                        add rax, rbx
0092DB2C  48 3B D0                        cmp rdx, rax
0092DB2F  0F 83 17 FF FF FF               jae 0x14092da4c
0092DB35  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
0092DB39  FF C1                           inc ecx
0092DB3B  48 03 D0                        add rdx, rax
0092DB3E  8B 44 24 7C                     mov eax, dword ptr [rsp + 0x7c]
0092DB42  EB 98                           jmp 0x14092dadc
0092DB44  0F B7 43 02                     movzx eax, word ptr [rbx + 2]
0092DB48  48 03 C3                        add rax, rbx
0092DB4B  48 3B C8                        cmp rcx, rax
0092DB4E  0F 83 F8 FE FF FF               jae 0x14092da4c
0092DB54  0F B7 41 02                     movzx eax, word ptr [rcx + 2]
0092DB58  FF C2                           inc edx
0092DB5A  48 03 C8                        add rcx, rax
0092DB5D  E9 79 FE FF FF                  jmp 0x14092d9db
0092DB62  C6 84 24 60 01 00 00 01         mov byte ptr [rsp + 0x160], 1
0092DB6A  E9 C3 FD FF FF                  jmp 0x14092d932
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpInheritAcl2(__int64 a1, __int64 a2, int a3, unsigned __int8 a4, unsigned __int8 a5, unsigned __int8 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, unsigned int a12, __int64 a13, unsigned int a14, __int64 a15, __int64 a16, unsigned __int8 a17, unsigned int a18)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int16 v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned __int8 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p100;
    unsigned __int8 v_stack_p160;
    unsigned int v_stack_p168;
    unsigned __int8 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p48;
    unsigned __int8 v_stack_p50;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int8 v_stack_p70;
    unsigned __int64 v_stack_p74;
    unsigned int v_stack_p78;
    unsigned int v_stack_p7C;
    unsigned __int64 v_stack_p8;
    unsigned int v_stack_p80;
    unsigned int v_stack_p84;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pE8;
    unsigned __int8 v_stack_pF0;
    unsigned __int8 v_stack_pF8;

    v_stack_p20 = a4;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (152);
    v_r14 = 0;
    v_r15 = 0;
    v_stack_m64 = 0;
    v_stack_m5C = 0;
    v_stack_m50 = 0;
    v_stack_p18 = 0;
    v_stack_m68 = 1;
    v_stack_m60 = 2;
    result = (unsigned int)(*(unsigned int *)(a15)) - 8;
    v_rdi = (unsigned int)(*(unsigned int *)(a15));
    v_r10 = a2;
    v_r11 = a4;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a15)) - 8)) <= 0xFFF4ULL) {
        a3 = (unsigned int)((unsigned int)(*(unsigned int *)(a15)));
        a2 = 0;
        a1 = a16;
        result = memset(a1, a2, a3, 2);
        v_r10 = v_stack_p10;
        result = 0xFFFCULL;
        v_r11 = v_stack_p20;
        v_rdi = (unsigned __int16)(((unsigned int)(*(unsigned int *)(a15))) & ((unsigned __int16)(result)));
        *(unsigned __int16 *)(a16 + 2) = (unsigned __int16)(v_rdi);
        a3 = 0;
        *(unsigned __int16 *)(a16) = 2;
        a4 = 2;
        *(unsigned int *)(a16 + 4) = 0;
    }
    *(unsigned __int8 *)(a17) = 0;
    result = (unsigned __int8)(-(a5));
    a1 = (unsigned int)((a1) & (0x400ULL));
    *(unsigned int *)(a18) = (unsigned int)(a1);
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (8));
    if (condition_is_not_equal) goto loc_0092D5E1;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (0x1000ULL));
    if (!(condition_is_equal)) {
        v_r15 = 1;
        *(unsigned int *)(a18) = (unsigned int)(a1);
    }
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) & (0x1004ULL));
    if (condition_is_not_equal) goto loc_0092D6BA;
loc_0092D5E1:
loc_0092D5E9:
    if (a5 != 0) goto loc_0092D5F8;
    if ((((unsigned __int8)((unsigned int)(a3))) & (4)) == 0) goto loc_0092D693;
loc_0092D5F8:
    if ((unsigned int)(v_r14) != 0) goto loc_0092D693;
    if (a5 == 0) goto loc_0092D60F;
    if ((unsigned __int8)(v_r15) == 0) goto loc_0092D693;
loc_0092D60F:
    v_r10 = 0;
loc_0092D61E:
    if ((unsigned int)(0 + 0 * 1) != 0) goto loc_0092D655;
    if ((*(unsigned __int8 *)(a17)) != ((unsigned __int8)(0 + 0 * 1))) goto loc_0092DA2F;
    *(unsigned int *)(a15) = 0;
loc_0092D640:
    v_rsp = (v_rsp) + (152);
    return (unsigned int)(0x8000000BULL);
loc_0092D655:
    result = ((unsigned int)(0x8000000BULL)) + (8);
    if (result > 0xFFFFULL) goto loc_0092DA4C;
    a1 = (unsigned int)(((unsigned int)(v_stack_m64) + 8) + (0));
    *(unsigned int *)(a15) = (unsigned int)(a1);
    if ((unsigned __int8)(v_stack_p18) != 0) goto loc_0092DA25;
    v_rsi = (unsigned __int16)((0) + (8));
    v_rsi = (unsigned __int16)((v_rsi) + (0));
    *(unsigned __int8 *)(a16) = (unsigned __int8)((unsigned int)(v_stack_p78));
    *(unsigned __int16 *)(a16 + 2) = (unsigned __int16)(v_rsi);
    result = 0;
    goto loc_0092D640;
loc_0092D693:
    if (v_stack_pE0 == 0) goto loc_0092D60F;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_pE0) - 2)) <= 2) goto loc_0092D817;
    goto loc_0092D640;
loc_0092D6BA:
    if (0 == 0) goto loc_0092DA8E;
    v_stack_p70 = (unsigned __int8)(v_rsi);
    if (((unsigned int)(*(unsigned __int8 *)(v_r10))) >= a17) { a4 = (unsigned int)(*(unsigned __int8 *)(v_r10)); }
    v_stack_p78 = a4;
    if ((unsigned __int8)((unsigned int)(v_stack_m64)) == 0) goto loc_0092D7C4;
    if ((unsigned int)(a2) != 0) goto loc_0092DABA;
    a4 = 0;
loc_0092D6F6:
    v_stack_p68 = a16;
    v_stack_p60 = v_stack_p74;
    v_stack_p58 = (unsigned int)((unsigned int)(a12));
    v_stack_p50 = (unsigned __int8)(v_rsi);
    v_stack_p48 = (unsigned __int8)(v_r11);
    v_stack_p40 = a10;
    v_stack_p38 = a9;
    v_stack_p30 = a8;
    v_stack_p28 = a7;
    v_stack_p20 = 1;
    result = RtlpCopyAces(0, a11, 1, a4);
    a4 = 0;
    a1 = 0;
    if (((unsigned int)(result)) != 0xC0000023ULL) { a1 = (unsigned int)(result); }
    if (sign_flag) goto loc_0092D810;
    if (a6 != ((unsigned __int8)(v_rsi))) goto loc_0092DAC4;
loc_0092D79E:
loc_0092D7A6:
    if (((unsigned int)((unsigned int)(a12))) != 1) goto loc_0092D7CE;
loc_0092D7B2:
    *(unsigned __int8 *)(a17) = 1;
    goto loc_0092D5E9;
loc_0092D7C4:
    a4 = 0;
    result = 0;
    goto loc_0092D6F6;
loc_0092D7CE:
    if (((unsigned int)((unsigned int)(a12))) != 2) goto loc_0092D5E1;
    if ((unsigned int)((unsigned int)(v_stack_p74)) != 0) goto loc_0092D7B2;
    if ((unsigned __int8)(v_r15) != 0) goto loc_0092D7B2;
    if ((unsigned int)((unsigned int)(v_stack_p74)) != 0) goto loc_0092D5E1;
    if (v_stack_pE8 == 0) goto loc_0092D5E1;
    if ((*(unsigned __int16 *)(v_stack_pE8 + 4)) != ((unsigned __int16)(v_rsi))) goto loc_0092D5E1;
    *(unsigned __int8 *)(a17) = 1;
    goto loc_0092D5E9;
loc_0092D810:
    goto loc_0092D640;
loc_0092D817:
    v_stack_p100 = (unsigned __int8)(v_rsi);
    a1 = (unsigned int)(v_stack_p78);
    if (((unsigned int)((unsigned int)(v_stack_p78))) <= ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a12)))))) { a1 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a12)))); }
    v_r10 = 0;
    v_stack_p78 = (unsigned int)(a1);
    v_stack_p168 = 0;
    v_r14 = 0;
    v_stack_p160 = 0;
    v_stack_p80 = 0;
    v_stack_p84 = 0;
loc_0092D85C:
    if (0 >= ((unsigned int)(*(unsigned __int16 *)((unsigned int)(v_stack_p74) + 4)))) goto loc_0092D981;
    if ((*(unsigned __int8 *)((unsigned int)(v_stack_p74) + 8)) == 17) goto loc_0092DA63;
    if (a12 == 3) goto loc_0092D96B;
loc_0092D882:
    v_stack_p68 = a5;
    v_stack_p60 = v_stack_p84;
    v_stack_p58 = a16;
    v_stack_p50 = v_stack_p80;
    v_stack_p48 = (unsigned int)((unsigned int)(a14));
    v_stack_p40 = a13;
    v_stack_p38 = a11;
    v_stack_p30 = a10;
    v_stack_p28 = a9;
    v_stack_p20 = a8;
    result = RtlpGenerateInheritedAce((unsigned int)(v_stack_p74) + 8, v_stack_pF8, (unsigned __int8)((unsigned int)(v_stack_m64)), a7);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_0092DAFB;
loc_0092D924:
    if (a5 != 0) goto loc_0092DB62;
loc_0092D932:
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)((unsigned int)(v_stack_p80))));
    if (((unsigned int)((unsigned int)(v_stack_p80))) > ((unsigned int)((unsigned int)(a18)))) goto loc_0092D95A;
    a2 = (unsigned int)(((unsigned int)(a18)) - ((unsigned int)((unsigned int)(v_stack_p80))));
    v_stack_p168 = (unsigned int)(a2);
    if (((unsigned int)(a2)) <= ((unsigned int)((unsigned int)(v_stack_p84)))) {
        a2 = (unsigned int)((unsigned int)(v_stack_p84));
        v_stack_p168 = (unsigned int)((unsigned int)(v_stack_p84));
    }
loc_0092D96B:
    v_r15 = (unsigned int)((0) + 1);
    v_rbp = ((unsigned int)(v_stack_p74) + 8) + (*(unsigned __int16 *)((unsigned int)(v_stack_p74) + 8 + 2));
    goto loc_0092D85C;
loc_0092D97A:
loc_0092D981:
    if (1 != 0) goto loc_0092DA56;
    if ((unsigned __int8)(v_stack_pF0) != 0) goto loc_0092DA56;
    v_r10 = 0;
loc_0092D99E:
    if (a6 == 0) goto loc_0092D61E;
    if ((unsigned int)((unsigned int)(v_stack_p74)) == 0) goto loc_0092D61E;
    if (a17 == 0) goto loc_0092D61E;
    if ((unsigned __int8)(v_stack_pF0) != 0) goto loc_0092D61E;
loc_0092D9DB:
    if (0 < ((unsigned int)(*(unsigned __int16 *)(a16 + 4)))) goto loc_0092DB44;
    a3 = (*(unsigned __int16 *)(a16 + 2)) + (a16);
    a1 = a16 + 8;
    if ((a16 + 8) > a3) { a1 = 0; }
    if (a1 == 0) {
        a1 = a3;
    }
    a1 = (a1) - (v_stack_p88);
    result = memcpy(a16 + 8, v_stack_p88, (unsigned int)((unsigned int)(a1)), a7);
    v_r10 = 0;
    goto loc_0092D61E;
loc_0092DA25:
    goto loc_0092D640;
loc_0092DA2F:
    if (v_stack_p70 == 0) goto loc_0092D655;
    *(unsigned int *)(a15) = 0;
    result = 0;
    goto loc_0092D640;
loc_0092DA4C:
    goto loc_0092D640;
loc_0092DA56:
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(v_stack_p88)));
    v_r10 = 0;
    goto loc_0092D99E;
loc_0092DA63:
    if (a12 != 3) goto loc_0092D96B;
    a3 = 0;
    result = RtlFindAceByType(a16, a3 + 17, a3, a7);
    if (result == 0) goto loc_0092D882;
    goto loc_0092D97A;
loc_0092DA8E:
    if ((unsigned __int8)((unsigned int)(v_stack_p74)) == 0) goto loc_0092D7A6;
    if (((unsigned int)((unsigned int)(a12))) != 1) goto loc_0092D7CE;
    if (((unsigned int)(result)) != 4) goto loc_0092D7B2;
    goto loc_0092D640;
loc_0092DABA:
    goto loc_0092D6F6;
loc_0092DAC4:
    if (0 == 0) goto loc_0092D79E;
    v_stack_p7C = (unsigned int)(*(unsigned __int16 *)(a16 + 4));
loc_0092DADC:
    if (16 < ((unsigned int)(*(unsigned __int16 *)(a16 + 4)))) goto loc_0092DB29;
    result = (*(unsigned __int16 *)(a16 + 2)) + (a16);
    a2 = a16 + 8;
    if ((a16 + 8) > result) { a2 = 16; }
    v_stack_p88 = a2;
    goto loc_0092D79E;
loc_0092DAFB:
    if (!sign_flag) goto loc_0092D924;
    v_r10 = 0;
    a1 = 0;
    if (((unsigned int)(result)) != 0xC0000023ULL) { a1 = (unsigned int)(result); }
    if (sign_flag) goto loc_0092D810;
    goto loc_0092D99E;
loc_0092DB29:
    result = (result) + (a16);
    if (a2 >= result) goto loc_0092DA4C;
    a1 = (unsigned int)((a1) + 1);
    a2 = (a2) + (*(unsigned __int16 *)(a2 + 2));
    goto loc_0092DADC;
loc_0092DB44:
    result = (*(unsigned __int16 *)(a16 + 2)) + (a16);
    if (a1 >= result) goto loc_0092DA4C;
    a2 = (unsigned int)((a2) + 1);
    a1 = (a1) + (*(unsigned __int16 *)(a1 + 2));
    goto loc_0092D9DB;
loc_0092DB62:
    v_stack_p160 = 1;
    goto loc_0092D932;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpInheritAcl2(int64_t Arg1, int64_t Arg2, int32_t Arg3, uint8_t Arg4, uint8_t Arg5, uint8_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11, uint32_t Arg12, int64_t Arg13, uint32_t Arg14, void *Arg15, void *Arg16, void *Arg17, void *Arg18)
{
    uint8_t *arg15 = (uint8_t *)Arg15;
    uint8_t *arg16 = (uint8_t *)Arg16;
    uint8_t *arg17 = (uint8_t *)Arg17;
    uint8_t *arg18 = (uint8_t *)Arg18;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint16_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint8_t v_stack_m68;
    uint64_t v_stack_p10;
    uint8_t v_stack_p100;
    uint8_t v_stack_p160;
    uint32_t v_stack_p168;
    uint8_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint8_t v_stack_p48;
    uint8_t v_stack_p50;
    uint32_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint8_t v_stack_p70;
    uint64_t v_stack_p74;
    uint32_t v_stack_p78;
    uint32_t v_stack_p7C;
    uint64_t v_stack_p8;
    uint32_t v_stack_p80;
    uint32_t v_stack_p84;
    uint64_t v_stack_p88;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pE8;
    uint8_t v_stack_pF0;
    uint8_t v_stack_pF8;

    v_stack_p20 = Arg4;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (152);
    local_r14 = 0;
    local_r15 = 0;
    v_stack_m64 = 0;
    v_stack_m5C = 0;
    v_stack_m50 = 0;
    v_stack_p18 = 0;
    v_stack_m68 = 1;
    v_stack_m60 = 2;
    result = (uint32_t)(*(uint32_t *)(arg15)) - 8;
    local_rdi = (uint32_t)(*(uint32_t *)(arg15));
    local_r10 = Arg2;
    local_r11 = Arg4;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg15)) - 8)) <= 0xFFF4ULL) {
        Arg3 = (uint32_t)((uint32_t)(*(uint32_t *)(arg15)));
        Arg2 = 0;
        Arg1 = Arg16;
        result = memset(Arg1, Arg2, Arg3, 2);
        local_r10 = v_stack_p10;
        result = 0xFFFCULL;
        local_r11 = v_stack_p20;
        local_rdi = (uint16_t)(((uint32_t)(*(uint32_t *)(arg15))) & ((uint16_t)(result)));
        *(uint16_t *)(arg16 + 0x2) = (uint16_t)(local_rdi);
        Arg3 = 0;
        *(uint16_t *)(arg16) = 2;
        Arg4 = 2;
        *(uint32_t *)(arg16 + 0x4) = 0;
    }
    *(uint8_t *)(arg17) = 0;
    result = (uint8_t)(-(Arg5));
    Arg1 = (uint32_t)((Arg1) & (0x400ULL));
    *(uint32_t *)(arg18) = (uint32_t)(Arg1);
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (8));
    if (condition_is_not_equal) goto loc_0092D5E1;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (0x1000ULL));
    if (!(condition_is_equal)) {
        local_r15 = 1;
        *(uint32_t *)(arg18) = (uint32_t)(Arg1);
    }
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) & (0x1004ULL));
    if (condition_is_not_equal) goto loc_0092D6BA;
loc_0092D5E1:
loc_0092D5E9:
    if (Arg5 != 0) goto loc_0092D5F8;
    if ((((uint8_t)((uint32_t)(Arg3))) & (4)) == 0) goto loc_0092D693;
loc_0092D5F8:
    if ((uint32_t)(local_r14) != 0) goto loc_0092D693;
    if (Arg5 == 0) goto loc_0092D60F;
    if ((uint8_t)(local_r15) == 0) goto loc_0092D693;
loc_0092D60F:
    local_r10 = 0;
loc_0092D61E:
    if ((uint32_t)(0 + 0 * 1) != 0) goto loc_0092D655;
    if ((*(uint8_t *)(arg17)) != ((uint8_t)(0 + 0 * 1))) goto loc_0092DA2F;
    *(uint32_t *)(arg15) = 0;
loc_0092D640:
    local_rsp = (local_rsp) + (152);
    return (uint32_t)(0x8000000BULL);
loc_0092D655:
    result = ((uint32_t)(0x8000000BULL)) + (8);
    if (result > 0xFFFFULL) goto loc_0092DA4C;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m64) + 8) + (0));
    *(uint32_t *)(arg15) = (uint32_t)(Arg1);
    if ((uint8_t)(v_stack_p18) != 0) goto loc_0092DA25;
    local_rsi = (uint16_t)((0) + (8));
    local_rsi = (uint16_t)((local_rsi) + (0));
    *(uint8_t *)(arg16) = (uint8_t)((uint32_t)(v_stack_p78));
    *(uint16_t *)(arg16 + 0x2) = (uint16_t)(local_rsi);
    result = 0;
    goto loc_0092D640;
loc_0092D693:
    if (v_stack_pE0 == 0) goto loc_0092D60F;
    if (((uint8_t)(*(uint8_t *)(v_stack_pE0) - 2)) <= 2) goto loc_0092D817;
    goto loc_0092D640;
loc_0092D6BA:
    if (0 == 0) goto loc_0092DA8E;
    v_stack_p70 = (uint8_t)(local_rsi);
    if (((uint32_t)(*(uint8_t *)(local_r10))) >= Arg17) { Arg4 = (uint32_t)(*(uint8_t *)(local_r10)); }
    v_stack_p78 = Arg4;
    if ((uint8_t)((uint32_t)(v_stack_m64)) == 0) goto loc_0092D7C4;
    if ((uint32_t)(Arg2) != 0) goto loc_0092DABA;
    Arg4 = 0;
loc_0092D6F6:
    v_stack_p68 = Arg16;
    v_stack_p60 = v_stack_p74;
    v_stack_p58 = (uint32_t)((uint32_t)(Arg12));
    v_stack_p50 = (uint8_t)(local_rsi);
    v_stack_p48 = (uint8_t)(local_r11);
    v_stack_p40 = Arg10;
    v_stack_p38 = Arg9;
    v_stack_p30 = Arg8;
    v_stack_p28 = Arg7;
    v_stack_p20 = 1;
    result = RtlpCopyAces(0, Arg11, 1, Arg4);
    Arg4 = 0;
    Arg1 = 0;
    if (((uint32_t)(result)) != 0xC0000023ULL) { Arg1 = (uint32_t)(result); }
    if (sign_flag) goto loc_0092D810;
    if (Arg6 != ((uint8_t)(local_rsi))) goto loc_0092DAC4;
loc_0092D79E:
loc_0092D7A6:
    if (((uint32_t)((uint32_t)(Arg12))) != 1) goto loc_0092D7CE;
loc_0092D7B2:
    *(uint8_t *)(arg17) = 1;
    goto loc_0092D5E9;
loc_0092D7C4:
    Arg4 = 0;
    result = 0;
    goto loc_0092D6F6;
loc_0092D7CE:
    if (((uint32_t)((uint32_t)(Arg12))) != 2) goto loc_0092D5E1;
    if ((uint32_t)((uint32_t)(v_stack_p74)) != 0) goto loc_0092D7B2;
    if ((uint8_t)(local_r15) != 0) goto loc_0092D7B2;
    if ((uint32_t)((uint32_t)(v_stack_p74)) != 0) goto loc_0092D5E1;
    if (v_stack_pE8 == 0) goto loc_0092D5E1;
    if ((*(uint16_t *)(v_stack_pE8 + 0x4)) != ((uint16_t)(local_rsi))) goto loc_0092D5E1;
    *(uint8_t *)(arg17) = 1;
    goto loc_0092D5E9;
loc_0092D810:
    goto loc_0092D640;
loc_0092D817:
    v_stack_p100 = (uint8_t)(local_rsi);
    Arg1 = (uint32_t)(v_stack_p78);
    if (((uint32_t)((uint32_t)(v_stack_p78))) <= ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg12)))))) { Arg1 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg12)))); }
    local_r10 = 0;
    v_stack_p78 = (uint32_t)(Arg1);
    v_stack_p168 = 0;
    local_r14 = 0;
    v_stack_p160 = 0;
    v_stack_p80 = 0;
    v_stack_p84 = 0;
loc_0092D85C:
    if (0 >= ((uint32_t)(*(uint16_t *)((uint32_t)(v_stack_p74) + 0x4)))) goto loc_0092D981;
    if ((*(uint8_t *)((uint32_t)(v_stack_p74) + 0x8)) == 17) goto loc_0092DA63;
    if (Arg12 == 3) goto loc_0092D96B;
loc_0092D882:
    v_stack_p68 = Arg5;
    v_stack_p60 = v_stack_p84;
    v_stack_p58 = Arg16;
    v_stack_p50 = v_stack_p80;
    v_stack_p48 = (uint32_t)((uint32_t)(Arg14));
    v_stack_p40 = Arg13;
    v_stack_p38 = Arg11;
    v_stack_p30 = Arg10;
    v_stack_p28 = Arg9;
    v_stack_p20 = Arg8;
    result = RtlpGenerateInheritedAce((uint32_t)(v_stack_p74) + 8, v_stack_pF8, (uint8_t)((uint32_t)(v_stack_m64)), Arg7);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_0092DAFB;
loc_0092D924:
    if (Arg5 != 0) goto loc_0092DB62;
loc_0092D932:
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)((uint32_t)(v_stack_p80))));
    if (((uint32_t)((uint32_t)(v_stack_p80))) > ((uint32_t)((uint32_t)(Arg18)))) goto loc_0092D95A;
    Arg2 = (uint32_t)(((uint32_t)(Arg18)) - ((uint32_t)((uint32_t)(v_stack_p80))));
    v_stack_p168 = (uint32_t)(Arg2);
    if (((uint32_t)(Arg2)) <= ((uint32_t)((uint32_t)(v_stack_p84)))) {
        Arg2 = (uint32_t)((uint32_t)(v_stack_p84));
        v_stack_p168 = (uint32_t)((uint32_t)(v_stack_p84));
    }
loc_0092D96B:
    local_r15 = (uint32_t)((0) + 1);
    local_rbp = ((uint32_t)(v_stack_p74) + 8) + (*(uint16_t *)((uint32_t)(v_stack_p74) + 0x8 + 0x2));
    goto loc_0092D85C;
loc_0092D97A:
loc_0092D981:
    if (1 != 0) goto loc_0092DA56;
    if ((uint8_t)(v_stack_pF0) != 0) goto loc_0092DA56;
    local_r10 = 0;
loc_0092D99E:
    if (Arg6 == 0) goto loc_0092D61E;
    if ((uint32_t)((uint32_t)(v_stack_p74)) == 0) goto loc_0092D61E;
    if (Arg17 == NULL) goto loc_0092D61E;
    if ((uint8_t)(v_stack_pF0) != 0) goto loc_0092D61E;
loc_0092D9DB:
    if (0 < ((uint32_t)(*(uint16_t *)(arg16 + 0x4)))) goto loc_0092DB44;
    Arg3 = (*(uint16_t *)(arg16 + 0x2)) + (Arg16);
    Arg1 = Arg16 + 8;
    if ((Arg16 + 8) > Arg3) { Arg1 = 0; }
    if (Arg1 == 0) {
        Arg1 = Arg3;
    }
    Arg1 = (Arg1) - (v_stack_p88);
    result = memcpy(Arg16 + 8, v_stack_p88, (uint32_t)((uint32_t)(Arg1)), Arg7);
    local_r10 = 0;
    goto loc_0092D61E;
loc_0092DA25:
    goto loc_0092D640;
loc_0092DA2F:
    if (v_stack_p70 == 0) goto loc_0092D655;
    *(uint32_t *)(arg15) = 0;
    result = 0;
    goto loc_0092D640;
loc_0092DA4C:
    goto loc_0092D640;
loc_0092DA56:
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(v_stack_p88)));
    local_r10 = 0;
    goto loc_0092D99E;
loc_0092DA63:
    if (Arg12 != 3) goto loc_0092D96B;
    Arg3 = 0;
    result = RtlFindAceByType(Arg16, Arg3 + 17, Arg3, Arg7);
    if (result == 0) goto loc_0092D882;
    goto loc_0092D97A;
loc_0092DA8E:
    if ((uint8_t)((uint32_t)(v_stack_p74)) == 0) goto loc_0092D7A6;
    if (((uint32_t)((uint32_t)(Arg12))) != 1) goto loc_0092D7CE;
    if (((uint32_t)(result)) != 4) goto loc_0092D7B2;
    goto loc_0092D640;
loc_0092DABA:
    goto loc_0092D6F6;
loc_0092DAC4:
    if (0 == 0) goto loc_0092D79E;
    v_stack_p7C = (uint32_t)(*(uint16_t *)(arg16 + 0x4));
loc_0092DADC:
    if (16 < ((uint32_t)(*(uint16_t *)(arg16 + 0x4)))) goto loc_0092DB29;
    result = (*(uint16_t *)(arg16 + 0x2)) + (Arg16);
    Arg2 = Arg16 + 8;
    if ((Arg16 + 8) > result) { Arg2 = 16; }
    v_stack_p88 = Arg2;
    goto loc_0092D79E;
loc_0092DAFB:
    if (!sign_flag) goto loc_0092D924;
    local_r10 = 0;
    Arg1 = 0;
    if (((uint32_t)(result)) != 0xC0000023ULL) { Arg1 = (uint32_t)(result); }
    if (sign_flag) goto loc_0092D810;
    goto loc_0092D99E;
loc_0092DB29:
    result = (result) + (Arg16);
    if (Arg2 >= result) goto loc_0092DA4C;
    Arg1 = (uint32_t)((Arg1) + 1);
    Arg2 = (Arg2) + (*(uint16_t *)(Arg2 + 0x2));
    goto loc_0092DADC;
loc_0092DB44:
    result = (*(uint16_t *)(arg16 + 0x2)) + (Arg16);
    if (Arg1 >= result) goto loc_0092DA4C;
    Arg2 = (uint32_t)((Arg2) + 1);
    Arg1 = (Arg1) + (*(uint16_t *)(Arg1 + 0x2));
    goto loc_0092D9DB;
loc_0092DB62:
    v_stack_p160 = 1;
    goto loc_0092D932;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg15` | `+ 0x0` | `32` | `R` |
| `Arg15` | `+ 0x0` | `32` | `W` |
| `Arg16` | `+ 0x0` | `8` | `W` |
| `Arg16` | `+ 0x0` | `16` | `W` |
| `Arg16` | `+ 0x2` | `16` | `R` |
| `Arg16` | `+ 0x2` | `16` | `W` |
| `Arg16` | `+ 0x4` | `16` | `R` |
| `Arg16` | `+ 0x4` | `16` | `R/W` |
| `Arg16` | `+ 0x4` | `32` | `W` |
| `Arg16` | `+ 0x8` | `64` | `R` |
| `Arg17` | `+ 0x0` | `8` | `R` |
| `Arg17` | `+ 0x0` | `8` | `W` |
| `Arg18` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0092D4D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
