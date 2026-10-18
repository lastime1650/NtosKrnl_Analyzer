# RtlCompressBufferXpressHuffMax

- RVA: `0x0026CA10`–`0x0026CFC1` (길이 `1,457` bytes)
- VA: `0x000000014026CA10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000655F4`
- 디코드: `345`개 명령, `1,457/1,457` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0026CA80` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0026CAF6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0026CB7D` → [XpressBuildHuffmanEncodings](XpressBuildHuffmanEncodings_function_0026C2C0.md) (function, `0x0026C2C0`)
- `0x0026CC2A` → [XpressDoHuffmanPass](XpressDoHuffmanPass_function_0026C6E0.md) (function, `0x0026C6E0`)
- `0x0026CF39` → [RtlpMakeXpressCallback](../41/RtlpMakeXpressCallback_function_0041A7F0.md) (function, `0x0041A7F0`)

### Direct callers
- [RtlCompressBufferXpressHuff](RtlCompressBufferXpressHuff_function_0026B9A0.md) at `0x0026BA42`
- [RtlCompressBufferProgress](../5E/RtlCompressBufferProgress_function_005EF3C0.md) at `0x005EF558`

### Static image references
- `0x0026CBE1` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **8**
  - `0x0026CC04` → [sub_006D9ADA](../6D/Unknown_function_006D9ADA.md) (`tail-transfer`)
  - `0x0026CCD7` → [sub_006D9ADA + 0x5E](../6D/Unknown_function_006D9ADA.md) (`tail-transfer`)
  - `0x0026CDF7` → [sub_006D9ADA + 0x12D](../6D/Unknown_function_006D9ADA.md) (`tail-transfer`)
  - `0x0026CF52` → [sub_006D9ADA + 0x1C9](../6D/Unknown_function_006D9ADA.md) (`tail-transfer`)
  - `0x0026CF76` → [sub_006D9ADA + 0x1EC](../6D/Unknown_function_006D9ADA.md) (`tail-transfer`)
  - `0x0026CF84` → [sub_006D9ADA + 0x21A](../6D/Unknown_function_006D9ADA.md) (`tail-transfer`)
  - `0x0026CFA4` → [sub_006D9ADA + 0x224](../6D/Unknown_function_006D9ADA.md) (`tail-transfer`)
  - `0x0026CFAC` → [sub_006D9ADA + 0x232](../6D/Unknown_function_006D9ADA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0026CA10  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0026CA15  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0026CA1A  55                              push rbp
0026CA1B  56                              push rsi
0026CA1C  57                              push rdi
0026CA1D  41 54                           push r12
0026CA1F  41 55                           push r13
0026CA21  41 56                           push r14
0026CA23  41 57                           push r15
0026CA25  48 81 EC A0 00 00 00            sub rsp, 0xa0
0026CA2C  33 ED                           xor ebp, ebp
0026CA2E  44 8B EA                        mov r13d, edx
0026CA31  4C 03 E9                        add r13, rcx
0026CA34  45 8B E1                        mov r12d, r9d
0026CA37  4D 03 E0                        add r12, r8
0026CA3A  8B FA                           mov edi, edx
0026CA3C  89 AC 24 94 00 00 00            mov dword ptr [rsp + 0x94], ebp
0026CA43  49 8B F0                        mov rsi, r8
0026CA46  4C 89 6C 24 60                  mov qword ptr [rsp + 0x60], r13
0026CA4B  4C 8B F9                        mov r15, rcx
0026CA4E  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
0026CA53  41 81 F9 2C 01 00 00            cmp r9d, 0x12c
0026CA5A  0F 82 4F 01 00 00               jb 0x14026cbaf
0026CA60  48 81 F9 01 00 01 00            cmp rcx, 0x10001
0026CA67  0F 86 94 04 00 00               jbe 0x14026cf01
0026CA6D  4C 8B B4 24 08 01 00 00         mov r14, qword ptr [rsp + 0x108]
0026CA75  33 D2                           xor edx, edx
0026CA77  49 8B CE                        mov rcx, r14
0026CA7A  41 B8 00 00 04 00               mov r8d, 0x40000
0026CA80  E8 BB A1 45 00                  call 0x1406c6c40
0026CA85  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
0026CA8D  49 8B DF                        mov rbx, r15
0026CA90  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
0026CA95  49 89 AE 00 00 04 00            mov qword ptr [r14 + 0x40000], rbp
0026CA9C  48 85 C0                        test rax, rax
0026CA9F  0F 84 64 01 00 00               je 0x14026cc09
0026CAA5  39 BC 24 20 01 00 00            cmp dword ptr [rsp + 0x120], edi
0026CAAC  0F 87 57 01 00 00               ja 0x14026cc09
0026CAB2  8B BC 24 20 01 00 00            mov edi, dword ptr [rsp + 0x120]
0026CAB9  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0026CAC1  48 8B 84 24 18 01 00 00         mov rax, qword ptr [rsp + 0x118]
0026CAC9  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
0026CAD1  89 BC 24 90 00 00 00            mov dword ptr [rsp + 0x90], edi
0026CAD8  48 89 6C 24 40                  mov qword ptr [rsp + 0x40], rbp
0026CADD  49 8D 8E 20 72 14 00            lea rcx, [r14 + 0x147220]
0026CAE4  48 89 6C 24 50                  mov qword ptr [rsp + 0x50], rbp
0026CAE9  33 D2                           xor edx, edx
0026CAEB  48 89 6C 24 58                  mov qword ptr [rsp + 0x58], rbp
0026CAF0  41 B8 00 08 00 00               mov r8d, 0x800
0026CAF6  E8 45 A1 45 00                  call 0x1406c6c40
0026CAFB  48 8D 83 00 00 01 00            lea rax, [rbx + 0x10000]
0026CB02  8B EF                           mov ebp, edi
0026CB04  49 3B C5                        cmp rax, r13
0026CB07  49 8D B6 20 7B 14 00            lea rsi, [r14 + 0x147b20]
0026CB0E  48 8B CE                        mov rcx, rsi
0026CB11  4D 8B D5                        mov r10, r13
0026CB14  4C 0F 46 D0                     cmovbe r10, rax
0026CB18  48 89 8C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rcx
0026CB20  48 03 EB                        add rbp, rbx
0026CB23  4C 89 54 24 78                  mov qword ptr [rsp + 0x78], r10
0026CB28  BF 01 00 00 00                  mov edi, 1
0026CB2D  4D 8D 5A FB                     lea r11, [r10 - 5]
0026CB31  4C 3B DD                        cmp r11, rbp
0026CB34  4C 89 5C 24 48                  mov qword ptr [rsp + 0x48], r11
0026CB39  49 0F 42 EB                     cmovb rbp, r11
0026CB3D  48 83 C6 04                     add rsi, 4
0026CB41  49 3B DF                        cmp rbx, r15
0026CB44  0F 84 C1 03 00 00               je 0x14026cf0b
0026CB4A  49 3B DB                        cmp rbx, r11
0026CB4D  0F 82 8B 00 00 00               jb 0x14026cbde
0026CB53  49 3B DA                        cmp rbx, r10
0026CB56  0F 82 2D 04 00 00               jb 0x14026cf89
0026CB5C  85 FF                           test edi, edi
0026CB5E  0F 8F 4D 04 00 00               jg 0x14026cfb1
0026CB64  8D 04 7D 01 00 00 00            lea eax, [rdi*2 + 1]
0026CB6B  89 01                           mov dword ptr [rcx], eax
0026CB6D  49 3B DD                        cmp rbx, r13
0026CB70  73 5E                           jae 0x14026cbd0
0026CB72  33 C0                           xor eax, eax
0026CB74  8B F8                           mov edi, eax
0026CB76  49 8D 8E 00 00 14 00            lea rcx, [r14 + 0x140000]
0026CB7D  E8 3E F7 FF FF                  call 0x14026c2c0
0026CB82  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
0026CB87  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
0026CB8C  49 83 C2 1F                     add r10, 0x1f
0026CB90  4C 03 D0                        add r10, rax
0026CB93  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0026CB98  49 C1 EA 05                     shr r10, 5
0026CB9C  4A 8D 04 90                     lea rax, [rax + r10*4]
0026CBA0  4D 8D 91 02 01 00 00            lea r10, [r9 + 0x102]
0026CBA7  4C 03 D0                        add r10, rax
0026CBAA  4D 3B D4                        cmp r10, r12
0026CBAD  72 66                           jb 0x14026cc15
0026CBAF  B8 23 00 00 C0                  mov eax, 0xc0000023
0026CBB4  48 8B 9C 24 E8 00 00 00         mov rbx, qword ptr [rsp + 0xe8]
0026CBBC  48 81 C4 A0 00 00 00            add rsp, 0xa0
0026CBC3  41 5F                           pop r15
0026CBC5  41 5E                           pop r14
0026CBC7  41 5D                           pop r13
0026CBC9  41 5C                           pop r12
0026CBCB  5F                              pop rdi
0026CBCC  5E                              pop rsi
0026CBCD  5D                              pop rbp
0026CBCE  C3                              ret
0026CBCF  CC                              int3
0026CBD0  41 FF 86 20 76 14 00            inc dword ptr [r14 + 0x147620]
0026CBD7  BF 01 00 00 00                  mov edi, 1
0026CBDC  EB 98                           jmp 0x14026cb76
0026CBDE  48 8B C3                        mov rax, rbx
0026CBE1  4C 8D 15 18 34 D9 FF            lea r10, [rip - 0x26cbe8]
0026CBE8  49 2B C7                        sub rax, r15
0026CBEB  4C 8B C3                        mov r8, rbx
0026CBEE  48 99                           cqo
0026CBF0  81 E2 FF FF 01 00               and edx, 0x1ffff
0026CBF6  4C 8D 0C 02                     lea r9, [rdx + rax]
0026CBFA  41 81 E1 FF FF 01 00            and r9d, 0x1ffff
0026CC01  4C 2B CA                        sub r9, rdx
0026CC04  E9 D1 CE 46 00                  jmp 0x1406d9ada
0026CC09  89 BC 24 20 01 00 00            mov dword ptr [rsp + 0x120], edi
0026CC10  E9 A4 FE FF FF                  jmp 0x14026cab9
0026CC15  4C 8B C6                        mov r8, rsi
0026CC18  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
0026CC1C  49 8D 96 20 7B 14 00            lea rdx, [r14 + 0x147b20]
0026CC23  49 8D 8E 00 00 14 00            lea rcx, [r14 + 0x140000]
0026CC2A  E8 B1 FA FF FF                  call 0x14026c6e0
0026CC2F  85 FF                           test edi, edi
0026CC31  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0026CC36  8B BC 24 20 01 00 00            mov edi, dword ptr [rsp + 0x120]
0026CC3D  48 8B C8                        mov rcx, rax
0026CC40  BD 00 00 00 00                  mov ebp, 0
0026CC45  0F 84 92 FE FF FF               je 0x14026cadd
0026CC4B  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
0026CC53  2B 8C 24 F0 00 00 00            sub ecx, dword ptr [rsp + 0xf0]
0026CC5A  89 08                           mov dword ptr [rax], ecx
0026CC5C  33 C0                           xor eax, eax
0026CC5E  E9 51 FF FF FF                  jmp 0x14026cbb4
0026CC63  48 3B DD                        cmp rbx, rbp
0026CC66  0F 83 7C 02 00 00               jae 0x14026cee8
0026CC6C  44 8B 03                        mov r8d, dword ptr [rbx]
0026CC6F  48 8B C3                        mov rax, rbx
0026CC72  49 2B C7                        sub rax, r15
0026CC75  48 99                           cqo
0026CC77  81 E2 FF FF 01 00               and edx, 0x1ffff
0026CC7D  48 03 C2                        add rax, rdx
0026CC80  25 FF FF 01 00                  and eax, 0x1ffff
0026CC85  48 2B C2                        sub rax, rdx
0026CC88  49 8B 94 C6 00 00 04 00         mov rdx, qword ptr [r14 + rax*8 + 0x40000]
0026CC90  48 8D 8A 00 00 01 00            lea rcx, [rdx + 0x10000]
0026CC97  48 3B CB                        cmp rcx, rbx
0026CC9A  77 2B                           ja 0x14026ccc7
0026CC9C  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
0026CCA4  48 FF C3                        inc rbx
0026CCA7  41 0F B6 C0                     movzx eax, r8b
0026CCAB  41 FF 84 86 20 72 14 00         inc dword ptr [r14 + rax*4 + 0x147220]
0026CCB3  88 06                           mov byte ptr [rsi], al
0026CCB5  48 FF C6                        inc rsi
0026CCB8  8D 04 3F                        lea eax, [rdi + rdi]
0026CCBB  85 FF                           test edi, edi
0026CCBD  0F 8E CD 01 00 00               jle 0x14026ce90
0026CCC3  8B F8                           mov edi, eax
0026CCC5  EB 9C                           jmp 0x14026cc63
0026CCC7  41 8B C0                        mov eax, r8d
0026CCCA  33 02                           xor eax, dword ptr [rdx]
0026CCCC  0F 84 9C 01 00 00               je 0x14026ce6e
0026CCD2  A9 FF FF FF 00                  test eax, 0xffffff
0026CCD7  0F 85 5B CE 46 00               jne 0x1406d9b38
0026CCDD  48 8D 8B 00 00 FF FF            lea rcx, [rbx - 0x10000]
0026CCE4  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0026CCE9  33 C0                           xor eax, eax
0026CCEB  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0026CCF0  41 BC 03 00 00 00               mov r12d, 3
0026CCF6  44 8B C8                        mov r9d, eax
0026CCF9  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
0026CCFE  4C 8B EB                        mov r13, rbx
0026CD01  49 2B D7                        sub rdx, r15
0026CD04  48 8B C2                        mov rax, rdx
0026CD07  48 99                           cqo
0026CD09  81 E2 FF FF 01 00               and edx, 0x1ffff
0026CD0F  48 03 C2                        add rax, rdx
0026CD12  25 FF FF 01 00                  and eax, 0x1ffff
0026CD17  48 2B C2                        sub rax, rdx
0026CD1A  49 8B 94 C6 00 00 04 00         mov rdx, qword ptr [r14 + rax*8 + 0x40000]
0026CD22  48 3B D1                        cmp rdx, rcx
0026CD25  0F 87 9E 00 00 00               ja 0x14026cdc9
0026CD2B  4C 8B 54 24 40                  mov r10, qword ptr [rsp + 0x40]
0026CD30  49 8B D5                        mov rdx, r13
0026CD33  4B 8D 1C 2C                     lea rbx, [r12 + r13]
0026CD37  49 2B D2                        sub rdx, r10
0026CD3A  48 81 FA 00 10 00 00            cmp rdx, 0x1000
0026CD41  0F 87 10 01 00 00               ja 0x14026ce57
0026CD47  48 81 FA 00 01 00 00            cmp rdx, 0x100
0026CD4E  0F 83 57 01 00 00               jae 0x14026ceab
0026CD54  4C 8D 15 A5 32 D9 FF            lea r10, [rip - 0x26cd5b]
0026CD5B  42 0F B6 8C 12 50 06 01 00      movzx ecx, byte ptr [rdx + r10 + 0x10650]
0026CD64  48 01 4C 24 50                  add qword ptr [rsp + 0x50], rcx
0026CD69  4D 8D 4C 24 FD                  lea r9, [r12 - 3]
0026CD6E  B8 01 00 00 00                  mov eax, 1
0026CD73  4C 8D 46 01                     lea r8, [rsi + 1]
0026CD77  48 D3 E0                        shl rax, cl
0026CD7A  48 2B D0                        sub rdx, rax
0026CD7D  C0 E1 04                        shl cl, 4
0026CD80  49 8B C1                        mov rax, r9
0026CD83  49 83 F9 0F                     cmp r9, 0xf
0026CD87  0F 83 D6 01 00 00               jae 0x14026cf63
0026CD8D  02 C8                           add cl, al
0026CD8F  88 0E                           mov byte ptr [rsi], cl
0026CD91  49 8B F0                        mov rsi, r8
0026CD94  4C 8B 5C 24 48                  mov r11, qword ptr [rsp + 0x48]
0026CD99  0F B6 C1                        movzx eax, cl
0026CD9C  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
0026CDA4  41 FF 84 86 20 76 14 00         inc dword ptr [r14 + rax*4 + 0x147620]
0026CDAC  8D 04 7D 01 00 00 00            lea eax, [rdi*2 + 1]
0026CDB3  66 89 16                        mov word ptr [rsi], dx
0026CDB6  48 83 C6 02                     add rsi, 2
0026CDBA  85 FF                           test edi, edi
0026CDBC  0F 8E CE 00 00 00               jle 0x14026ce90
0026CDC2  8B F8                           mov edi, eax
0026CDC4  E9 9A FE FF FF                  jmp 0x14026cc63
0026CDC9  44 3B 02                        cmp r8d, dword ptr [rdx]
0026CDCC  75 5E                           jne 0x14026ce2c
0026CDCE  49 8B DD                        mov rbx, r13
0026CDD1  48 83 C3 04                     add rbx, 4
0026CDD5  48 83 C2 04                     add rdx, 4
0026CDD9  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
0026CDDE  4C 8D 63 20                     lea r12, [rbx + 0x20]
0026CDE2  4C 3B E1                        cmp r12, rcx
0026CDE5  73 57                           jae 0x14026ce3e
0026CDE7  8B 03                           mov eax, dword ptr [rbx]
0026CDE9  8B 0A                           mov ecx, dword ptr [rdx]
0026CDEB  3B C1                           cmp eax, ecx
0026CDED  75 16                           jne 0x14026ce05
0026CDEF  8B 43 04                        mov eax, dword ptr [rbx + 4]
0026CDF2  8B 4A 04                        mov ecx, dword ptr [rdx + 4]
0026CDF5  3B C1                           cmp eax, ecx
0026CDF7  0F 84 0A CE 46 00               je 0x1406d9c07
0026CDFD  48 83 C3 04                     add rbx, 4
0026CE01  48 83 C2 04                     add rdx, 4
0026CE05  3A C1                           cmp al, cl
0026CE07  0F 84 3E 01 00 00               je 0x14026cf4b
0026CE0D  4C 8B 64 24 30                  mov r12, qword ptr [rsp + 0x30]
0026CE12  49 2B DD                        sub rbx, r13
0026CE15  48 8B C2                        mov rax, rdx
0026CE18  48 2B D3                        sub rdx, rbx
0026CE1B  49 3B DC                        cmp rbx, r12
0026CE1E  0F 87 A6 00 00 00               ja 0x14026ceca
0026CE24  4C 03 CB                        add r9, rbx
0026CE27  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0026CE2C  49 FF C1                        inc r9
0026CE2F  49 83 F9 0C                     cmp r9, 0xc
0026CE33  0F 82 C8 FE FF FF               jb 0x14026cd01
0026CE39  E9 ED FE FF FF                  jmp 0x14026cd2b
0026CE3E  48 3B D9                        cmp rbx, rcx
0026CE41  73 CA                           jae 0x14026ce0d
0026CE43  0F B6 02                        movzx eax, byte ptr [rdx]
0026CE46  38 03                           cmp byte ptr [rbx], al
0026CE48  75 C3                           jne 0x14026ce0d
0026CE4A  48 FF C3                        inc rbx
0026CE4D  48 FF C2                        inc rdx
0026CE50  48 3B D9                        cmp rbx, rcx
0026CE53  72 EE                           jb 0x14026ce43
0026CE55  EB B6                           jmp 0x14026ce0d
0026CE57  49 83 FC 03                     cmp r12, 3
0026CE5B  0F 85 E6 FE FF FF               jne 0x14026cd47
0026CE61  4C 8B 5C 24 48                  mov r11, qword ptr [rsp + 0x48]
0026CE66  49 8B DD                        mov rbx, r13
0026CE69  E9 2E FE FF FF                  jmp 0x14026cc9c
0026CE6E  48 8D 83 00 00 FF FF            lea rax, [rbx - 0x10000]
0026CE75  48 C7 44 24 30 03 00 00 00      mov qword ptr [rsp + 0x30], 3
0026CE7E  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0026CE83  4C 8B EB                        mov r13, rbx
0026CE86  33 C0                           xor eax, eax
0026CE88  44 8B C8                        mov r9d, eax
0026CE8B  E9 41 FF FF FF                  jmp 0x14026cdd1
0026CE90  89 01                           mov dword ptr [rcx], eax
0026CE92  BF 01 00 00 00                  mov edi, 1
0026CE97  48 8B CE                        mov rcx, rsi
0026CE9A  48 83 C6 04                     add rsi, 4
0026CE9E  48 89 8C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rcx
0026CEA6  E9 B8 FD FF FF                  jmp 0x14026cc63
0026CEAB  48 8B C2                        mov rax, rdx
0026CEAE  48 8D 0D 4B 31 D9 FF            lea rcx, [rip - 0x26ceb5]
0026CEB5  48 C1 E8 08                     shr rax, 8
0026CEB9  0F B6 8C 08 50 06 01 00         movzx ecx, byte ptr [rax + rcx + 0x10650]
0026CEC1  48 83 C1 08                     add rcx, 8
0026CEC5  E9 9A FE FF FF                  jmp 0x14026cd64
0026CECA  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
0026CECF  4C 8B E3                        mov r12, rbx
0026CED2  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0026CED7  4C 8B D2                        mov r10, rdx
0026CEDA  49 3B C5                        cmp rax, r13
0026CEDD  0F 87 4D FE FF FF               ja 0x14026cd30
0026CEE3  E9 3F FF FF FF                  jmp 0x14026ce27
0026CEE8  49 3B DB                        cmp rbx, r11
0026CEEB  72 3E                           jb 0x14026cf2b
0026CEED  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
0026CEF2  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
0026CEF7  4C 8B 54 24 78                  mov r10, qword ptr [rsp + 0x78]
0026CEFC  E9 52 FC FF FF                  jmp 0x14026cb53
0026CF01  B8 BB 00 00 C0                  mov eax, 0xc00000bb
0026CF06  E9 A9 FC FF FF                  jmp 0x14026cbb4
0026CF0B  0F B6 03                        movzx eax, byte ptr [rbx]
0026CF0E  BF 02 00 00 00                  mov edi, 2
0026CF13  41 FF 84 86 20 72 14 00         inc dword ptr [r14 + rax*4 + 0x147220]
0026CF1B  0F B6 03                        movzx eax, byte ptr [rbx]
0026CF1E  48 FF C3                        inc rbx
0026CF21  88 06                           mov byte ptr [rsi], al
0026CF23  48 FF C6                        inc rsi
0026CF26  E9 1F FC FF FF                  jmp 0x14026cb4a
0026CF2B  4C 8B C3                        mov r8, rbx
0026CF2E  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
0026CF36  49 8B D3                        mov rdx, r11
0026CF39  E8 B2 D8 1A 00                  call 0x14041a7f0
0026CF3E  4C 8B 5C 24 48                  mov r11, qword ptr [rsp + 0x48]
0026CF43  48 8B E8                        mov rbp, rax
0026CF46  E9 21 FD FF FF                  jmp 0x14026cc6c
0026CF4B  0F B6 42 01                     movzx eax, byte ptr [rdx + 1]
0026CF4F  38 43 01                        cmp byte ptr [rbx + 1], al
0026CF52  0F 84 4B CD 46 00               je 0x1406d9ca3
0026CF58  48 FF C3                        inc rbx
0026CF5B  48 FF C2                        inc rdx
0026CF5E  E9 AA FE FF FF                  jmp 0x14026ce0d
0026CF63  80 C1 0F                        add cl, 0xf
0026CF66  48 83 E8 0F                     sub rax, 0xf
0026CF6A  88 0E                           mov byte ptr [rsi], cl
0026CF6C  49 8D 70 01                     lea rsi, [r8 + 1]
0026CF70  48 3D FF 00 00 00               cmp rax, 0xff
0026CF76  0F 83 4A CD 46 00               jae 0x1406d9cc6
0026CF7C  41 88 00                        mov byte ptr [r8], al
0026CF7F  B8 01 00 00 00                  mov eax, 1
0026CF84  E9 6B CD 46 00                  jmp 0x1406d9cf4
0026CF89  0F B6 03                        movzx eax, byte ptr [rbx]
0026CF8C  41 FF 84 86 20 72 14 00         inc dword ptr [r14 + rax*4 + 0x147220]
0026CF94  0F B6 03                        movzx eax, byte ptr [rbx]
0026CF97  48 FF C3                        inc rbx
0026CF9A  88 06                           mov byte ptr [rsi], al
0026CF9C  48 FF C6                        inc rsi
0026CF9F  8D 04 3F                        lea eax, [rdi + rdi]
0026CFA2  85 FF                           test edi, edi
0026CFA4  0F 8E 54 CD 46 00               jle 0x1406d9cfe
0026CFAA  8B F8                           mov edi, eax
0026CFAC  E9 5B CD 46 00                  jmp 0x1406d9d0c
0026CFB1  8D 3C 7D 01 00 00 00            lea edi, [rdi*2 + 1]
0026CFB8  85 FF                           test edi, edi
0026CFBA  7F F5                           jg 0x14026cfb1
0026CFBC  E9 A3 FB FF FF                  jmp 0x14026cb64
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlCompressBufferXpressHuffMax(__int64 a1, int a2, __int64 a3, int a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, unsigned int a9)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m44;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p120;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_pE0;
    unsigned int v_stack_pF0;

    v_stack_p10 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (160);
    v_rbp = 0;
    v_r13 = ((unsigned int)(a2)) + (a1);
    v_r12 = ((unsigned int)(a4)) + (a3);
    v_stack_m44 = 0;
    v_stack_m78 = v_r13;
    v_stack_m68 = v_r12;
    if (a4 < 300) goto loc_0026CBAF;
    if (a1 <= 0x10001ULL) goto loc_0026CF01;
    a2 = 0;
    result = memset(a6, a2, (unsigned int)(0x40000ULL), a4);
    v_stack_m70 = a3;
    *(unsigned __int64 *)(a6 + 262144) = 0;
    if (a7 == 0) goto loc_0026CC09;
    if (a9 > ((unsigned int)((unsigned int)(a2)))) goto loc_0026CC09;
loc_0026CAB9:
    v_stack_m58 = a7;
    v_stack_m50 = a8;
    v_stack_m48 = (unsigned int)((unsigned int)(a9));
    v_stack_m98 = 0;
loc_0026CADD:
    v_stack_m88 = 0;
    a2 = 0;
    v_stack_m80 = 0;
    result = memset(a6 + 1339936, a2, (unsigned int)(0x800ULL), a4);
    v_r10 = v_r13;
    if ((a1 + 65536) <= v_r13) { v_r10 = a1 + 65536; }
    v_stack_p8 = a6 + 1342240;
    v_rbp = ((unsigned int)((unsigned int)((unsigned int)(a9)))) + (a1);
    v_stack_m60 = v_r10;
    v_stack_m90 = v_r10 - 5;
    if ((v_r10 - 5) < v_rbp) { v_rbp = v_r10 - 5; }
    v_rsi = (a6 + 1342240) + (4);
    if (a1 == a1) goto loc_0026CF0B;
loc_0026CB4A:
    if (a1 < (v_r10 - 5)) goto loc_0026CBDE;
loc_0026CB53:
    if (a1 < v_r10) goto loc_0026CF89;
    if (condition_is_greater) goto loc_0026CFB1;
loc_0026CB64:
    *(unsigned int *)(a6 + 1342240) = (unsigned int)(1 * 2 + 1);
    if (a1 >= v_r13) goto loc_0026CBD0;
    result = 0;
loc_0026CB76:
    result = XpressBuildHuffmanEncodings(a6 + 1310720, a2, (unsigned int)(0x800ULL), a4);
    v_r10 = (v_stack_m88) + (31);
    v_r10 = (v_r10) + (result);
    v_r10 = (v_r10) >> (5);
    v_r10 = (v_stack_m70 + 258) + (v_stack_m80 + v_r10 * 4);
    if (v_r10 < v_r12) goto loc_0026CC15;
loc_0026CBAF:
loc_0026CBB4:
    v_rsp = (v_rsp) + (160);
    return (unsigned int)(0xC0000023ULL);
loc_0026CBD0:
    goto loc_0026CB76;
loc_0026CBDE:
    result = (v_stack_p10) - (a1);
    a2 = (unsigned int)((a2) & (0x1FFFFULL));
    a4 = (unsigned int)((a2 + result * 1) & (0x1FFFFULL));
    a4 = (a4) - (a2);
loc_0026CC09:
    v_stack_p120 = 1;
    goto loc_0026CAB9;
loc_0026CC15:
    v_stack_p20 = 1;
    result = XpressDoHuffmanPass(a6 + 1310720, a6 + 1342240, v_rsi, a4);
    v_stack_p68 = result;
    if (1 == 0) goto loc_0026CADD;
    a1 = (unsigned int)((result) - (v_stack_pF0));
    *(unsigned int *)(a5) = (unsigned int)(a1);
    result = 0;
    goto loc_0026CBB4;
loc_0026CF01:
    goto loc_0026CBB4;
loc_0026CF0B:
    v_rbx = (v_stack_p10) + 1;
    *(unsigned __int8 *)(v_rsi) = (unsigned __int8)(*(unsigned __int8 *)(v_stack_p10));
    v_rsi = (v_rsi) + 1;
    goto loc_0026CB4A;
loc_0026CF89:
    v_rbx = (v_rbx) + 1;
    *(unsigned __int8 *)(v_rsi) = (unsigned __int8)(*(unsigned __int8 *)(v_rbx));
    v_rsi = (v_rsi) + 1;
loc_0026CFB1:
    if (condition_is_greater) goto loc_0026CFB1;
    goto loc_0026CB64;
}
```

## 5. (Beta) C Style

```c
int64_t RtlCompressBufferXpressHuffMax(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, void *Arg5, void *Arg6, int64_t Arg7, int64_t Arg8, uint32_t Arg9)
{
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m44;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_p10;
    uint32_t v_stack_p120;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;
    uint64_t v_stack_p80;
    uint64_t v_stack_pE0;
    uint32_t v_stack_pF0;

    v_stack_p10 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (160);
    local_rbp = 0;
    local_r13 = ((uint32_t)(Arg2)) + (Arg1);
    local_r12 = ((uint32_t)(Arg4)) + (Arg3);
    v_stack_m44 = 0;
    v_stack_m78 = local_r13;
    v_stack_m68 = local_r12;
    if (Arg4 < 300) goto loc_0026CBAF;
    if (Arg1 <= 0x10001ULL) goto loc_0026CF01;
    Arg2 = 0;
    result = memset(Arg6, Arg2, (uint32_t)(0x40000ULL), Arg4);
    v_stack_m70 = Arg3;
    *(uint64_t *)(arg6 + 0x40000) = 0;
    if (Arg7 == 0) goto loc_0026CC09;
    if (Arg9 > ((uint32_t)((uint32_t)(Arg2)))) goto loc_0026CC09;
loc_0026CAB9:
    v_stack_m58 = Arg7;
    v_stack_m50 = Arg8;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg9));
    v_stack_m98 = 0;
loc_0026CADD:
    v_stack_m88 = 0;
    Arg2 = 0;
    v_stack_m80 = 0;
    result = memset(Arg6 + 1339936, Arg2, (uint32_t)(0x800ULL), Arg4);
    local_r10 = local_r13;
    if ((Arg1 + 65536) <= local_r13) { local_r10 = Arg1 + 65536; }
    v_stack_p8 = Arg6 + 1342240;
    local_rbp = ((uint32_t)((uint32_t)((uint32_t)(Arg9)))) + (Arg1);
    v_stack_m60 = local_r10;
    v_stack_m90 = local_r10 - 5;
    if ((local_r10 - 5) < local_rbp) { local_rbp = local_r10 - 5; }
    local_rsi = (Arg6 + 1342240) + (4);
    if (Arg1 == Arg1) goto loc_0026CF0B;
loc_0026CB4A:
    if (Arg1 < (local_r10 - 5)) goto loc_0026CBDE;
loc_0026CB53:
    if (Arg1 < local_r10) goto loc_0026CF89;
    if (condition_is_greater) goto loc_0026CFB1;
loc_0026CB64:
    *(uint32_t *)(arg6 + 0x147B20) = (uint32_t)(1 * 2 + 1);
    if (Arg1 >= local_r13) goto loc_0026CBD0;
    result = 0;
loc_0026CB76:
    result = XpressBuildHuffmanEncodings(Arg6 + 1310720, Arg2, (uint32_t)(0x800ULL), Arg4);
    local_r10 = (v_stack_m88) + (31);
    local_r10 = (local_r10) + (result);
    local_r10 = (local_r10) >> (5);
    local_r10 = (v_stack_m70 + 258) + (v_stack_m80 + local_r10 * 4);
    if (local_r10 < local_r12) goto loc_0026CC15;
loc_0026CBAF:
loc_0026CBB4:
    local_rsp = (local_rsp) + (160);
    return (uint32_t)(0xC0000023ULL);
loc_0026CBD0:
    goto loc_0026CB76;
loc_0026CBDE:
    result = (v_stack_p10) - (Arg1);
    Arg2 = (uint32_t)((Arg2) & (0x1FFFFULL));
    Arg4 = (uint32_t)((Arg2 + result * 1) & (0x1FFFFULL));
    Arg4 = (Arg4) - (Arg2);
loc_0026CC09:
    v_stack_p120 = 1;
    goto loc_0026CAB9;
loc_0026CC15:
    v_stack_p20 = 1;
    result = XpressDoHuffmanPass(Arg6 + 1310720, Arg6 + 1342240, local_rsi, Arg4);
    v_stack_p68 = result;
    if (1 == 0) goto loc_0026CADD;
    Arg1 = (uint32_t)((result) - (v_stack_pF0));
    *(uint32_t *)(arg5) = (uint32_t)(Arg1);
    result = 0;
    goto loc_0026CBB4;
loc_0026CF01:
    goto loc_0026CBB4;
loc_0026CF0B:
    local_rbx = (v_stack_p10) + 1;
    *(uint8_t *)(local_rsi) = (uint8_t)(*(uint8_t *)(v_stack_p10));
    local_rsi = (local_rsi) + 1;
    goto loc_0026CB4A;
loc_0026CF89:
    local_rbx = (local_rbx) + 1;
    *(uint8_t *)(local_rsi) = (uint8_t)(*(uint8_t *)(local_rbx));
    local_rsi = (local_rsi) + 1;
loc_0026CFB1:
    if (condition_is_greater) goto loc_0026CFB1;
    goto loc_0026CB64;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `32` | `W` |
| `Arg6` | `+ 0x0` | `8` | `W` |
| `Arg6` | `+ 0x0` | `32` | `W` |
| `Arg6` | `+ 0x40000` | `64` | `W` |
| `Arg6` | `+ 0x140000` | `64` | `R` |
| `Arg6` | `+ 0x147220` | `64` | `R` |
| `Arg6` | `+ 0x147220 + rax*4` | `32` | `R/W` |
| `Arg6` | `+ 0x147620` | `32` | `R/W` |
| `Arg6` | `+ 0x147B20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0026CA10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
