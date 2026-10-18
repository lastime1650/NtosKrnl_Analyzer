# RtlpGenerateInheritedAce

- RVA: `0x0092DB80`–`0x0092E010` (길이 `1,168` bytes)
- VA: `0x000000014092DB80`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008DBD0`
- 디코드: `304`개 명령, `1,168/1,168` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0092DCF6` → [RtlpCopyEffectiveAce](RtlpCopyEffectiveAce_function_0092E530.md) (function, `0x0092E530`)
- `0x0092DDD6` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)
- `0x0092DEDB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092DF04` → [RtlpIsDuplicateAce](RtlpIsDuplicateAce_function_0092EA70.md) (function, `0x0092EA70`)
- `0x0092DF7B` → [RtlpCompareKnownObjectAces](../70/RtlpCompareKnownObjectAces_function_00704670.md) (function, `0x00704670`)

### Direct callers
- [RtlpInheritAcl2](RtlpInheritAcl2_function_0092D4D0.md) at `0x0092D911`

### Static image references
- `0x0092DD48` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0092DDD6` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (`PAGE` → `.text`)
  - `0x0092DEDB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0092DB80  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0092DB85  55                              push rbp
0092DB86  56                              push rsi
0092DB87  57                              push rdi
0092DB88  41 54                           push r12
0092DB8A  41 55                           push r13
0092DB8C  41 56                           push r14
0092DB8E  41 57                           push r15
0092DB90  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
0092DB95  48 81 EC F0 00 00 00            sub rsp, 0xf0
0092DB9C  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
0092DBA0  33 DB                           xor ebx, ebx
0092DBA2  48 8B BD 9F 00 00 00            mov rdi, qword ptr [rbp + 0x9f]
0092DBA9  45 32 E4                        xor r12b, r12b
0092DBAC  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
0092DBB0  44 0F B6 DA                     movzx r11d, dl
0092DBB4  48 8B 45 6F                     mov rax, qword ptr [rbp + 0x6f]
0092DBB8  8B F3                           mov esi, ebx
0092DBBA  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
0092DBBE  44 8B FB                        mov r15d, ebx
0092DBC1  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
0092DBC5  44 8B D3                        mov r10d, ebx
0092DBC8  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
0092DBCC  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
0092DBD0  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
0092DBD4  48 8B 85 87 00 00 00            mov rax, qword ptr [rbp + 0x87]
0092DBDB  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
0092DBDF  48 8B 85 97 00 00 00            mov rax, qword ptr [rbp + 0x97]
0092DBE6  48 89 45 F7                     mov qword ptr [rbp - 9], rax
0092DBEA  48 8B 85 A7 00 00 00            mov rax, qword ptr [rbp + 0xa7]
0092DBF1  48 89 45 FF                     mov qword ptr [rbp - 1], rax
0092DBF5  48 8B 85 AF 00 00 00            mov rax, qword ptr [rbp + 0xaf]
0092DBFC  4C 89 4D EF                     mov qword ptr [rbp - 0x11], r9
0092DC00  44 88 45 99                     mov byte ptr [rbp - 0x67], r8b
0092DC04  48 89 4D B7                     mov qword ptr [rbp - 0x49], rcx
0092DC08  88 18                           mov byte ptr [rax], bl
0092DC0A  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
0092DC0E  89 5D 9B                        mov dword ptr [rbp - 0x65], ebx
0092DC11  44 88 65 9A                     mov byte ptr [rbp - 0x66], r12b
0092DC15  88 5D 97                        mov byte ptr [rbp - 0x69], bl
0092DC18  84 D2                           test dl, dl
0092DC1A  0F 85 50 02 00 00               jne 0x14092de70
0092DC20  45 32 F6                        xor r14b, r14b
0092DC23  44 0F B7 47 04                  movzx r8d, word ptr [rdi + 4]
0092DC28  4C 8D 6F 08                     lea r13, [rdi + 8]
0092DC2C  49 8B D5                        mov rdx, r13
0092DC2F  44 88 75 98                     mov byte ptr [rbp - 0x68], r14b
0092DC33  4C 8B CB                        mov r9, rbx
0092DC36  48 89 5D A7                     mov qword ptr [rbp - 0x59], rbx
0092DC3A  8B CB                           mov ecx, ebx
0092DC3C  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
0092DC40  48 03 C7                        add rax, rdi
0092DC43  41 3B C8                        cmp ecx, r8d
0092DC46  0F 82 AD 01 00 00               jb 0x14092ddf9
0092DC4C  48 3B D0                        cmp rdx, rax
0092DC4F  77 07                           ja 0x14092dc58
0092DC51  4C 8B CA                        mov r9, rdx
0092DC54  48 89 55 A7                     mov qword ptr [rbp - 0x59], rdx
0092DC58  4D 85 C9                        test r9, r9
0092DC5B  0F 84 85 03 00 00               je 0x14092dfe6
0092DC61  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
0092DC65  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
0092DC69  45 84 DB                        test r11b, r11b
0092DC6C  0F 85 91 03 00 00               jne 0x14092e003
0092DC72  A8 01                           test al, 1
0092DC74  0F 84 96 01 00 00               je 0x14092de10
0092DC7A  0F B6 55 99                     movzx edx, byte ptr [rbp - 0x67]
0092DC7E  48 8D 45 97                     lea rax, [rbp - 0x69]
0092DC82  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0092DC87  4D 8B F9                        mov r15, r9
0092DC8A  48 8D 45 9A                     lea rax, [rbp - 0x66]
0092DC8E  4C 89 4D AF                     mov qword ptr [rbp - 0x51], r9
0092DC92  4C 8B 4D EF                     mov r9, qword ptr [rbp - 0x11]
0092DC96  45 0F B6 C6                     movzx r8d, r14b
0092DC9A  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0092DC9F  48 8B 45 BF                     mov rax, qword ptr [rbp - 0x41]
0092DCA3  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0092DCA8  48 8D 45 9B                     lea rax, [rbp - 0x65]
0092DCAC  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
0092DCB1  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0092DCB6  48 8D 45 A7                     lea rax, [rbp - 0x59]
0092DCBA  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0092DCBF  8B 85 8F 00 00 00               mov eax, dword ptr [rbp + 0x8f]
0092DCC5  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0092DCC9  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
0092DCCD  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0092DCD2  48 8B 45 CF                     mov rax, qword ptr [rbp - 0x31]
0092DCD6  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0092DCDB  48 8B 45 D7                     mov rax, qword ptr [rbp - 0x29]
0092DCDF  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0092DCE4  48 8B 45 DF                     mov rax, qword ptr [rbp - 0x21]
0092DCE8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0092DCED  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
0092DCF1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0092DCF6  E8 35 08 00 00                  call 0x14092e530
0092DCFB  84 C0                           test al, al
0092DCFD  0F 84 E3 02 00 00               je 0x14092dfe6
0092DD03  44 8B 55 9B                     mov r10d, dword ptr [rbp - 0x65]
0092DD07  38 5D 97                        cmp byte ptr [rbp - 0x69], bl
0092DD0A  0F 85 12 01 00 00               jne 0x14092de22
0092DD10  45 85 D2                        test r10d, r10d
0092DD13  0F 84 09 01 00 00               je 0x14092de22
0092DD19  4D 85 FF                        test r15, r15
0092DD1C  0F 84 00 01 00 00               je 0x14092de22
0092DD22  41 0F B6 07                     movzx eax, byte ptr [r15]
0092DD26  3C 04                           cmp al, 4
0092DD28  0F 84 F4 00 00 00               je 0x14092de22
0092DD2E  3C 08                           cmp al, 8
0092DD30  0F 87 EC 00 00 00               ja 0x14092de22
0092DD36  41 0F B6 4F 01                  movzx ecx, byte ptr [r15 + 1]
0092DD3B  F6 C1 10                        test cl, 0x10
0092DD3E  0F 84 DE 00 00 00               je 0x14092de22
0092DD44  41 8B 47 04                     mov eax, dword ptr [r15 + 4]
0092DD48  4C 8D 1D B1 22 6D FF            lea r11, [rip - 0x92dd4f]
0092DD4F  F6 C1 02                        test cl, 2
0092DD52  44 8B F8                        mov r15d, eax
0092DD55  44 8B E0                        mov r12d, eax
0092DD58  44 8B F3                        mov r14d, ebx
0092DD5B  44 0F 44 FB                     cmove r15d, ebx
0092DD5F  F6 C1 01                        test cl, 1
0092DD62  44 0F 44 E3                     cmove r12d, ebx
0092DD66  F6 C1 08                        test cl, 8
0092DD69  44 0F 44 F0                     cmove r14d, eax
0092DD6D  0F B7 47 04                     movzx eax, word ptr [rdi + 4]
0092DD71  FF C8                           dec eax
0092DD73  3B F0                           cmp esi, eax
0092DD75  0F 8D 9A 00 00 00               jge 0x14092de15
0092DD7B  41 0F B6 4D 00                  movzx ecx, byte ptr [r13]
0092DD80  80 F9 08                        cmp cl, 8
0092DD83  77 65                           ja 0x14092ddea
0092DD85  80 F9 04                        cmp cl, 4
0092DD88  74 60                           je 0x14092ddea
0092DD8A  45 0F B6 4D 01                  movzx r9d, byte ptr [r13 + 1]
0092DD8F  41 F6 C1 10                     test r9b, 0x10
0092DD93  74 55                           je 0x14092ddea
0092DD95  80 F9 05                        cmp cl, 5
0092DD98  0F 83 C6 01 00 00               jae 0x14092df64
0092DD9E  4C 8B 55 AF                     mov r10, qword ptr [rbp - 0x51]
0092DDA2  41 0F B6 12                     movzx edx, byte ptr [r10]
0092DDA6  8D 42 FB                        lea eax, [rdx - 5]
0092DDA9  3C 03                           cmp al, 3
0092DDAB  76 3D                           jbe 0x14092ddea
0092DDAD  42 0F B6 84 19 38 AD B4 00      movzx eax, byte ptr [rcx + r11 + 0xb4ad38]
0092DDB6  42 38 84 1A 38 AD B4 00         cmp byte ptr [rdx + r11 + 0xb4ad38], al
0092DDBE  75 2A                           jne 0x14092ddea
0092DDC0  42 38 9C 1A 08 B0 B4 00         cmp byte ptr [rdx + r11 + 0xb4b008], bl
0092DDC8  0F 85 22 02 00 00               jne 0x14092dff0
0092DDCE  49 8D 55 08                     lea rdx, [r13 + 8]
0092DDD2  49 8D 4A 08                     lea rcx, [r10 + 8]
0092DDD6  E8 F5 2C AD FF                  call 0x140400ad0
0092DDDB  84 C0                           test al, al
0092DDDD  0F 85 A5 01 00 00               jne 0x14092df88
0092DDE3  4C 8D 1D 16 22 6D FF            lea r11, [rip - 0x92ddea]
0092DDEA  41 0F B7 45 02                  movzx eax, word ptr [r13 + 2]
0092DDEF  FF C6                           inc esi
0092DDF1  4C 03 E8                        add r13, rax
0092DDF4  E9 74 FF FF FF                  jmp 0x14092dd6d
0092DDF9  48 3B D0                        cmp rdx, rax
0092DDFC  0F 83 E4 01 00 00               jae 0x14092dfe6
0092DE02  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
0092DE06  FF C1                           inc ecx
0092DE08  48 03 D0                        add rdx, rax
0092DE0B  E9 2C FE FF FF                  jmp 0x14092dc3c
0092DE10  44 8B EB                        mov r13d, ebx
0092DE13  EB 20                           jmp 0x14092de35
0092DE15  44 8B 55 9B                     mov r10d, dword ptr [rbp - 0x65]
0092DE19  44 0F B6 75 98                  movzx r14d, byte ptr [rbp - 0x68]
0092DE1E  4C 8B 7D AF                     mov r15, qword ptr [rbp - 0x51]
0092DE22  4C 8B 4D A7                     mov r9, qword ptr [rbp - 0x59]
0092DE26  44 8B EB                        mov r13d, ebx
0092DE29  44 0F B6 65 9A                  movzx r12d, byte ptr [rbp - 0x66]
0092DE2E  41 8B F2                        mov esi, r10d
0092DE31  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
0092DE35  45 84 F6                        test r14b, r14b
0092DE38  75 52                           jne 0x14092de8c
0092DE3A  48 8B 45 F7                     mov rax, qword ptr [rbp - 9]
0092DE3E  38 5D 97                        cmp byte ptr [rbp - 0x69], bl
0092DE41  89 30                           mov dword ptr [rax], esi
0092DE43  48 8B 45 FF                     mov rax, qword ptr [rbp - 1]
0092DE47  44 89 28                        mov dword ptr [rax], r13d
0092DE4A  B8 23 00 00 C0                  mov eax, 0xc0000023
0092DE4F  0F 45 D8                        cmovne ebx, eax
0092DE52  8B C3                           mov eax, ebx
0092DE54  48 8B 9C 24 38 01 00 00         mov rbx, qword ptr [rsp + 0x138]
0092DE5C  48 81 C4 F0 00 00 00            add rsp, 0xf0
0092DE63  41 5F                           pop r15
0092DE65  41 5E                           pop r14
0092DE67  41 5D                           pop r13
0092DE69  41 5C                           pop r12
0092DE6B  5F                              pop rdi
0092DE6C  5E                              pop rsi
0092DE6D  5D                              pop rbp
0092DE6E  C3                              ret
0092DE6F  CC                              int3
0092DE70  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
0092DE74  A8 04                           test al, 4
0092DE76  0F 85 A4 FD FF FF               jne 0x14092dc20
0092DE7C  A8 01                           test al, 1
0092DE7E  0F 84 A8 00 00 00               je 0x14092df2c
0092DE84  41 B6 01                        mov r14b, 1
0092DE87  E9 97 FD FF FF                  jmp 0x14092dc23
0092DE8C  45 85 D2                        test r10d, r10d
0092DE8F  74 09                           je 0x14092de9a
0092DE91  45 84 E4                        test r12b, r12b
0092DE94  0F 84 9F 00 00 00               je 0x14092df39
0092DE9A  80 39 08                        cmp byte ptr [rcx], 8
0092DE9D  77 05                           ja 0x14092dea4
0092DE9F  39 59 04                        cmp dword ptr [rcx + 4], ebx
0092DEA2  74 96                           je 0x14092de3a
0092DEA4  0F B7 41 02                     movzx eax, word ptr [rcx + 2]
0092DEA8  03 F0                           add esi, eax
0092DEAA  81 FE FF FF 00 00               cmp esi, 0xffff
0092DEB0  0F 87 30 01 00 00               ja 0x14092dfe6
0092DEB6  44 8B C0                        mov r8d, eax
0092DEB9  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
0092DEBD  49 2B C1                        sub rax, r9
0092DEC0  48 03 C7                        add rax, rdi
0092DEC3  4C 3B C0                        cmp r8, rax
0092DEC6  0F 8F 11 01 00 00               jg 0x14092dfdd
0092DECC  38 5D 97                        cmp byte ptr [rbp - 0x69], bl
0092DECF  0F 85 65 FF FF FF               jne 0x14092de3a
0092DED5  48 8B D1                        mov rdx, rcx
0092DED8  49 8B C9                        mov rcx, r9
0092DEDB  E8 60 89 D9 FF                  call 0x1406c6840
0092DEE0  48 8B 45 A7                     mov rax, qword ptr [rbp - 0x59]
0092DEE4  80 48 01 08                     or byte ptr [rax + 1], 8
0092DEE8  66 FF 47 04                     inc word ptr [rdi + 4]
0092DEEC  38 5D 99                        cmp byte ptr [rbp - 0x67], bl
0092DEEF  0F 84 45 FF FF FF               je 0x14092de3a
0092DEF5  48 8B 45 A7                     mov rax, qword ptr [rbp - 0x59]
0092DEF9  48 8B CF                        mov rcx, rdi
0092DEFC  80 48 01 10                     or byte ptr [rax + 1], 0x10
0092DF00  48 8B 55 A7                     mov rdx, qword ptr [rbp - 0x59]
0092DF04  E8 67 0B 00 00                  call 0x14092ea70
0092DF09  84 C0                           test al, al
0092DF0B  0F 84 29 FF FF FF               je 0x14092de3a
0092DF11  66 FF 4F 04                     dec word ptr [rdi + 4]
0092DF15  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
0092DF19  0F B7 40 02                     movzx eax, word ptr [rax + 2]
0092DF1D  44 3B E8                        cmp r13d, eax
0092DF20  77 03                           ja 0x14092df25
0092DF22  44 8B E8                        mov r13d, eax
0092DF25  2B F0                           sub esi, eax
0092DF27  E9 0E FF FF FF                  jmp 0x14092de3a
0092DF2C  A8 02                           test al, 2
0092DF2E  0F 85 50 FF FF FF               jne 0x14092de84
0092DF34  E9 E7 FC FF FF                  jmp 0x14092dc20
0092DF39  38 5D 97                        cmp byte ptr [rbp - 0x69], bl
0092DF3C  0F 85 F8 FE FF FF               jne 0x14092de3a
0092DF42  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
0092DF46  24 03                           and al, 3
0092DF48  41 0A 47 01                     or al, byte ptr [r15 + 1]
0092DF4C  41 88 47 01                     mov byte ptr [r15 + 1], al
0092DF50  38 5D 99                        cmp byte ptr [rbp - 0x67], bl
0092DF53  0F 84 E1 FE FF FF               je 0x14092de3a
0092DF59  0C 10                           or al, 0x10
0092DF5B  41 88 47 01                     mov byte ptr [r15 + 1], al
0092DF5F  E9 D6 FE FF FF                  jmp 0x14092de3a
0092DF64  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
0092DF68  0F B6 01                        movzx eax, byte ptr [rcx]
0092DF6B  2C 05                           sub al, 5
0092DF6D  3C 03                           cmp al, 3
0092DF6F  0F 87 75 FE FF FF               ja 0x14092ddea
0092DF75  48 8B D1                        mov rdx, rcx
0092DF78  49 8B CD                        mov rcx, r13
0092DF7B  E8 F0 66 DD FF                  call 0x140704670
0092DF80  84 C0                           test al, al
0092DF82  0F 84 5B FE FF FF               je 0x14092dde3
0092DF88  41 0F B6 4D 01                  movzx ecx, byte ptr [r13 + 1]
0092DF8D  41 8B 45 04                     mov eax, dword ptr [r13 + 4]
0092DF91  F7 D0                           not eax
0092DF93  F6 C1 02                        test cl, 2
0092DF96  74 03                           je 0x14092df9b
0092DF98  44 23 F8                        and r15d, eax
0092DF9B  F6 C1 01                        test cl, 1
0092DF9E  74 03                           je 0x14092dfa3
0092DFA0  44 23 E0                        and r12d, eax
0092DFA3  F6 C1 08                        test cl, 8
0092DFA6  75 03                           jne 0x14092dfab
0092DFA8  44 23 F0                        and r14d, eax
0092DFAB  41 8B C6                        mov eax, r14d
0092DFAE  41 0B C4                        or eax, r12d
0092DFB1  41 0B C7                        or eax, r15d
0092DFB4  0F 85 29 FE FF FF               jne 0x14092dde3
0092DFBA  4C 8B 7D AF                     mov r15, qword ptr [rbp - 0x51]
0092DFBE  44 8B D3                        mov r10d, ebx
0092DFC1  44 8B 6D 9B                     mov r13d, dword ptr [rbp - 0x65]
0092DFC5  4D 8B CF                        mov r9, r15
0092DFC8  66 FF 4F 04                     dec word ptr [rdi + 4]
0092DFCC  44 0F B6 75 98                  movzx r14d, byte ptr [rbp - 0x68]
0092DFD1  4C 89 7D A7                     mov qword ptr [rbp - 0x59], r15
0092DFD5  89 5D 9B                        mov dword ptr [rbp - 0x65], ebx
0092DFD8  E9 4C FE FF FF                  jmp 0x14092de29
0092DFDD  C6 45 97 01                     mov byte ptr [rbp - 0x69], 1
0092DFE1  E9 54 FE FF FF                  jmp 0x14092de3a
0092DFE6  B8 7D 00 00 C0                  mov eax, 0xc000007d
0092DFEB  E9 64 FE FF FF                  jmp 0x14092de54
0092DFF0  45 32 4A 01                     xor r9b, byte ptr [r10 + 1]
0092DFF4  41 F6 C1 C0                     test r9b, 0xc0
0092DFF8  0F 84 D0 FD FF FF               je 0x14092ddce
0092DFFE  E9 E7 FD FF FF                  jmp 0x14092ddea
0092E003  A8 02                           test al, 2
0092E005  0F 84 05 FE FF FF               je 0x14092de10
0092E00B  E9 6A FC FF FF                  jmp 0x14092dc7a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpGenerateInheritedAce(__int64 a1, unsigned __int8 a2, unsigned __int8 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, unsigned int a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m3F;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
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
    unsigned int v_stack_mA4;
    unsigned __int8 v_stack_mA5;
    unsigned __int8 v_stack_mA6;
    unsigned __int8 v_stack_mA7;
    unsigned __int8 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (240);
    v_rbx = 0;
    v_r12 = 0;
    v_stack_m58 = a5;
    v_stack_m60 = a6;
    v_stack_m68 = a7;
    v_stack_m70 = a8;
    v_stack_m78 = a9;
    v_stack_m48 = a11;
    v_stack_m40 = a13;
    v_stack_m50 = a4;
    v_stack_mA6 = a3;
    v_stack_m88 = a1;
    *(unsigned __int8 *)(a14) = 0;
    v_stack_m80 = a14;
    v_stack_mA4 = 0;
    v_stack_mA5 = 0;
    v_stack_mA8 = 0;
    if (a2 != 0) goto loc_0092DE70;
loc_0092DC20:
    v_r14 = 0;
loc_0092DC23:
    v_stack_mA7 = 0;
    v_stack_m98 = 0;
loc_0092DC3C:
    result = (*(unsigned __int16 *)(a12 + 2)) + (a12);
    if (0 < ((unsigned int)(*(unsigned __int16 *)(a12 + 4)))) goto loc_0092DDF9;
    if ((a12 + 8) <= result) {
        a4 = a12 + 8;
        v_stack_m98 = a12 + 8;
    }
    if (a4 == 0) goto loc_0092DFE6;
    if (a2 != 0) goto loc_0092E003;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_m88 + 1))) & (1)) == 0) goto loc_0092DE10;
loc_0092DC7A:
    v_stack_mB0 = v_stack_mA8;
    v_stack_m90 = a4;
    v_stack_mB8 = v_stack_mA5;
    v_stack_mC0 = v_stack_m80;
    v_stack_mC8 = a12;
    v_stack_mD0 = v_stack_mA4;
    v_stack_mD8 = v_stack_m98;
    v_stack_mE0 = (unsigned int)((unsigned int)(a10));
    v_stack_mE8 = v_stack_m78;
    v_stack_mF0 = v_stack_m70;
    v_stack_mF8 = v_stack_m68;
    v_stack_m100 = v_stack_m60;
    v_stack_m108 = v_stack_m58;
    result = RtlpCopyEffectiveAce(v_stack_m88, v_stack_mA6, 0, v_stack_m50);
    if ((unsigned __int8)(result) == 0) goto loc_0092DFE6;
    if (v_stack_mA8 != 0) goto loc_0092DE22;
    if ((unsigned int)((unsigned int)(v_stack_mA4)) == 0) goto loc_0092DE22;
    if (a4 == 0) goto loc_0092DE22;
    if (((unsigned __int8)(*(unsigned __int8 *)(a4))) == 4) goto loc_0092DE22;
    if (((unsigned __int8)(*(unsigned __int8 *)(a4))) > 8) goto loc_0092DE22;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a4 + 1))) & (16)) == 0) goto loc_0092DE22;
    v_r15 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a4 + 1))) & (2)) == 0) { v_r15 = 0; }
    v_r12 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a4 + 1))) & (1)) == 0) { v_r12 = 0; }
    v_r14 = 0;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a4 + 1))) & (8)) == 0) { v_r14 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))); }
loc_0092DD6D:
    result = (unsigned int)((*(unsigned __int16 *)(a12 + 4)) - 1);
    if (0 >= ((unsigned int)(result))) goto loc_0092DE15;
    if (((unsigned __int8)(*(unsigned __int8 *)(a12 + 8))) > 8) goto loc_0092DDEA;
    if (((unsigned __int8)(*(unsigned __int8 *)(a12 + 8))) == 4) goto loc_0092DDEA;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a12 + 8 + 1))) & (16)) == 0) goto loc_0092DDEA;
    if (((unsigned __int8)(*(unsigned __int8 *)(a12 + 8))) >= 5) goto loc_0092DF64;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_m90) - 5)) <= 3) goto loc_0092DDEA;
    if ((*(unsigned __int8 *)(*(unsigned __int8 *)(v_stack_m90) + v_rip - 9624911 * 1 + 11840824)) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int8 *)(a12 + 8) + v_rip - 9624911 * 1 + 11840824)))) goto loc_0092DDEA;
    if ((*(unsigned __int8 *)(*(unsigned __int8 *)(v_stack_m90) + v_rip - 9624911 * 1 + 11841544)) != 0) goto loc_0092DFF0;
loc_0092DDCE:
    result = RtlEqualSid(v_stack_m90 + 8, a12 + 8 + 8, 0, *(unsigned __int8 *)(a12 + 8 + 1));
    if ((unsigned __int8)(result) != 0) goto loc_0092DF88;
loc_0092DDE3:
loc_0092DDEA:
    v_rsi = (unsigned int)((0) + 1);
    v_r13 = (a12 + 8) + (*(unsigned __int16 *)(a12 + 8 + 2));
    goto loc_0092DD6D;
loc_0092DDF9:
    if ((a12 + 8 + 8) >= (*(unsigned __int16 *)(a12 + 8 + 2))) goto loc_0092DFE6;
    a1 = (unsigned int)((v_stack_m90 + 8) + 1);
    a2 = (a12 + 8 + 8) + (*(unsigned __int16 *)(a12 + 8 + 8 + 2));
    goto loc_0092DC3C;
loc_0092DE10:
    goto loc_0092DE35;
loc_0092DE15:
loc_0092DE22:
loc_0092DE29:
loc_0092DE35:
    if ((unsigned __int8)(v_stack_mA7) != 0) goto loc_0092DE8C;
loc_0092DE3A:
    *(unsigned int *)(v_stack_m48) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_mA4))));
    *(unsigned int *)(v_stack_m40) = 0;
    if (v_stack_mA8 != 0) { v_rbx = (unsigned int)((unsigned int)(0xC0000023ULL)); }
loc_0092DE54:
    v_rsp = (v_rsp) + (240);
    return (unsigned int)((unsigned int)(v_rbx));
loc_0092DE70:
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_m88 + 1))) & (4)) != 0) goto loc_0092DC20;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_m88 + 1))) & (1)) == 0) goto loc_0092DF2C;
loc_0092DE84:
    goto loc_0092DC23;
loc_0092DE8C:
    if ((unsigned int)((unsigned int)(v_stack_mA4)) == 0) goto loc_0092DE9A;
    if ((unsigned __int8)(v_stack_mA5) == 0) goto loc_0092DF39;
loc_0092DE9A:
    if ((*(unsigned __int8 *)(v_stack_m88)) > 8) goto loc_0092DEA4;
    if ((*(unsigned int *)(v_stack_m88 + 4)) == ((unsigned int)(v_stack_p10))) goto loc_0092DE3A;
loc_0092DEA4:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mA4)))) + ((unsigned int)(*(unsigned __int16 *)(v_stack_m88 + 2))));
    if (((unsigned int)(v_rsi)) > 0xFFFFULL) goto loc_0092DFE6;
    result = (*(unsigned __int16 *)(a12 + 2)) - (v_stack_m98);
    result = (result) + (a12);
    if (((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m88 + 2)))) > result) goto loc_0092DFDD;
    if (v_stack_mA8 != ((unsigned __int8)(v_stack_p10))) goto loc_0092DE3A;
    result = memcpy(v_stack_m98, v_stack_m88, (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m88 + 2))), v_stack_m98);
    if (v_stack_mA6 == ((unsigned __int8)(v_stack_p10))) goto loc_0092DE3A;
    result = RtlpIsDuplicateAce(a12, v_stack_m98, (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m88 + 2))), v_stack_m98);
    if ((unsigned __int8)(result) == 0) goto loc_0092DE3A;
    v_r13 = 0;
    if (0 <= ((unsigned int)(*(unsigned __int16 *)(v_stack_m88 + 2)))) {
        v_r13 = (unsigned int)(*(unsigned __int16 *)(v_stack_m88 + 2));
    }
    v_rsi = (unsigned int)((v_rsi) - ((unsigned int)(*(unsigned __int16 *)(v_stack_m88 + 2))));
    goto loc_0092DE3A;
loc_0092DF2C:
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_m88 + 2))) & (2)) != 0) goto loc_0092DE84;
    goto loc_0092DC20;
loc_0092DF39:
    if (v_stack_mA8 != ((unsigned __int8)(v_stack_p10))) goto loc_0092DE3A;
    result = (unsigned __int8)((*(unsigned __int8 *)(a12 + 1)) & (3));
    result = (unsigned __int8)((result) | (*(unsigned __int8 *)(v_stack_m90 + 1)));
    *(unsigned __int8 *)(v_stack_m90 + 1) = (unsigned __int8)(result);
    if (v_stack_mA6 == ((unsigned __int8)(v_stack_p10))) goto loc_0092DE3A;
    result = (unsigned __int8)((result) | (16));
    *(unsigned __int8 *)(v_stack_m90 + 1) = (unsigned __int8)(result);
    goto loc_0092DE3A;
loc_0092DF64:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_m90)) - (5));
    if (((unsigned __int8)(result)) > 3) goto loc_0092DDEA;
    result = RtlpCompareKnownObjectAces(v_r13, v_stack_m90, (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m88 + 2))), v_stack_m98);
    if ((unsigned __int8)(result) == 0) goto loc_0092DDE3;
loc_0092DF88:
    result = (unsigned int)(~((unsigned int)(*(unsigned int *)(v_r13 + 4))));
    v_r15 = v_stack_m90;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r13 + 1))) & (2)) != 0) {
        v_r15 = (unsigned int)((v_stack_m90) & ((unsigned int)(result)));
    }
    v_r12 = v_stack_mA5;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r13 + 1))) & (1)) != 0) {
        v_r12 = (unsigned int)((v_stack_mA5) & ((unsigned int)(result)));
    }
    v_r14 = 1;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_r13 + 1))) & (8)) == 0) {
        v_r14 = (unsigned int)((1) & ((unsigned int)(result)));
    }
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) | ((unsigned int)(v_r12)));
    result = (unsigned int)((result) | ((unsigned int)(v_r15)));
    if (condition_is_not_equal) goto loc_0092DDE3;
    v_stack_m98 = v_stack_m90;
    v_stack_mA4 = (unsigned int)(v_stack_p10);
    goto loc_0092DE29;
loc_0092DFDD:
    v_stack_mA8 = 1;
    goto loc_0092DE3A;
loc_0092DFE6:
    goto loc_0092DE54;
loc_0092DFF0:
    a4 = (unsigned __int8)((v_stack_m90) ^ (*(unsigned __int8 *)((unsigned int)((unsigned int)(v_stack_p10)) + 1)));
    if ((((unsigned __int8)(a4)) & (192)) == 0) goto loc_0092DDCE;
    goto loc_0092DDEA;
loc_0092E003:
    if ((((unsigned __int8)((unsigned int)(0xC000007DULL))) & (2)) == 0) goto loc_0092DE10;
    goto loc_0092DC7A;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpGenerateInheritedAce(void *Arg1, uint8_t Arg2, uint8_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9, uint32_t Arg10, int64_t Arg11, void *Arg12, int64_t Arg13, void *Arg14)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg12 = (uint8_t *)Arg12;
    uint8_t *arg14 = (uint8_t *)Arg14;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m3F;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
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
    uint32_t v_stack_mA4;
    uint8_t v_stack_mA5;
    uint8_t v_stack_mA6;
    uint8_t v_stack_mA7;
    uint8_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (240);
    local_rbx = 0;
    local_r12 = 0;
    v_stack_m58 = Arg5;
    v_stack_m60 = Arg6;
    v_stack_m68 = Arg7;
    v_stack_m70 = Arg8;
    v_stack_m78 = Arg9;
    v_stack_m48 = Arg11;
    v_stack_m40 = Arg13;
    v_stack_m50 = Arg4;
    v_stack_mA6 = Arg3;
    v_stack_m88 = Arg1;
    *(uint8_t *)(arg14) = 0;
    v_stack_m80 = Arg14;
    v_stack_mA4 = 0;
    v_stack_mA5 = 0;
    v_stack_mA8 = 0;
    if (Arg2 != 0) goto loc_0092DE70;
loc_0092DC20:
    local_r14 = 0;
loc_0092DC23:
    v_stack_mA7 = 0;
    v_stack_m98 = 0;
loc_0092DC3C:
    result = (*(uint16_t *)(arg12 + 0x2)) + (Arg12);
    if (0 < ((uint32_t)(*(uint16_t *)(arg12 + 0x4)))) goto loc_0092DDF9;
    if ((Arg12 + 8) <= result) {
        Arg4 = Arg12 + 8;
        v_stack_m98 = Arg12 + 8;
    }
    if (Arg4 == 0) goto loc_0092DFE6;
    if (Arg2 != 0) goto loc_0092E003;
    if ((((uint8_t)(*(uint8_t *)(v_stack_m88 + 0x1))) & (1)) == 0) goto loc_0092DE10;
loc_0092DC7A:
    v_stack_mB0 = v_stack_mA8;
    v_stack_m90 = Arg4;
    v_stack_mB8 = v_stack_mA5;
    v_stack_mC0 = v_stack_m80;
    v_stack_mC8 = Arg12;
    v_stack_mD0 = v_stack_mA4;
    v_stack_mD8 = v_stack_m98;
    v_stack_mE0 = (uint32_t)((uint32_t)(Arg10));
    v_stack_mE8 = v_stack_m78;
    v_stack_mF0 = v_stack_m70;
    v_stack_mF8 = v_stack_m68;
    v_stack_m100 = v_stack_m60;
    v_stack_m108 = v_stack_m58;
    result = RtlpCopyEffectiveAce(v_stack_m88, v_stack_mA6, 0, v_stack_m50);
    if ((uint8_t)(result) == 0) goto loc_0092DFE6;
    if (v_stack_mA8 != 0) goto loc_0092DE22;
    if ((uint32_t)((uint32_t)(v_stack_mA4)) == 0) goto loc_0092DE22;
    if (Arg4 == 0) goto loc_0092DE22;
    if (((uint8_t)(*(uint8_t *)(Arg4))) == 4) goto loc_0092DE22;
    if (((uint8_t)(*(uint8_t *)(Arg4))) > 8) goto loc_0092DE22;
    if ((((uint8_t)(*(uint8_t *)(Arg4 + 0x1))) & (16)) == 0) goto loc_0092DE22;
    local_r15 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))));
    if ((((uint8_t)(*(uint8_t *)(Arg4 + 0x1))) & (2)) == 0) { local_r15 = 0; }
    local_r12 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))));
    if ((((uint8_t)(*(uint8_t *)(Arg4 + 0x1))) & (1)) == 0) { local_r12 = 0; }
    local_r14 = 0;
    if ((((uint8_t)(*(uint8_t *)(Arg4 + 0x1))) & (8)) == 0) { local_r14 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))); }
loc_0092DD6D:
    result = (uint32_t)((*(uint16_t *)(arg12 + 0x4)) - 1);
    if (0 >= ((uint32_t)(result))) goto loc_0092DE15;
    if (((uint8_t)(*(uint8_t *)(arg12 + 0x8))) > 8) goto loc_0092DDEA;
    if (((uint8_t)(*(uint8_t *)(arg12 + 0x8))) == 4) goto loc_0092DDEA;
    if ((((uint8_t)(*(uint8_t *)(arg12 + 0x8 + 0x1))) & (16)) == 0) goto loc_0092DDEA;
    if (((uint8_t)(*(uint8_t *)(arg12 + 0x8))) >= 5) goto loc_0092DF64;
    if (((uint8_t)(*(uint8_t *)(v_stack_m90) - 5)) <= 3) goto loc_0092DDEA;
    if ((*(uint8_t *)(*(uint8_t *)(v_stack_m90) + v_rip - 0x92DD4F * 1 + 0xB4AD38)) != ((uint8_t)(*(uint8_t *)(*(uint8_t *)(arg12 + 0x8) + v_rip - 0x92DD4F * 1 + 0xB4AD38)))) goto loc_0092DDEA;
    if ((*(uint8_t *)(*(uint8_t *)(v_stack_m90) + v_rip - 0x92DD4F * 1 + 0xB4B008)) != 0) goto loc_0092DFF0;
loc_0092DDCE:
    result = RtlEqualSid(v_stack_m90 + 8, Arg12 + 8 + 8, 0, *(uint8_t *)(arg12 + 0x8 + 0x1));
    if ((uint8_t)(result) != 0) goto loc_0092DF88;
loc_0092DDE3:
loc_0092DDEA:
    local_rsi = (uint32_t)((0) + 1);
    local_r13 = (Arg12 + 8) + (*(uint16_t *)(arg12 + 0x8 + 0x2));
    goto loc_0092DD6D;
loc_0092DDF9:
    if ((Arg12 + 8 + 8) >= (*(uint16_t *)(arg12 + 0x8 + 0x2))) goto loc_0092DFE6;
    Arg1 = (uint32_t)((v_stack_m90 + 8) + 1);
    Arg2 = (Arg12 + 8 + 8) + (*(uint16_t *)(arg12 + 0x8 + 0x8 + 0x2));
    goto loc_0092DC3C;
loc_0092DE10:
    goto loc_0092DE35;
loc_0092DE15:
loc_0092DE22:
loc_0092DE29:
loc_0092DE35:
    if ((uint8_t)(v_stack_mA7) != 0) goto loc_0092DE8C;
loc_0092DE3A:
    *(uint32_t *)(v_stack_m48) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mA4))));
    *(uint32_t *)(v_stack_m40) = 0;
    if (v_stack_mA8 != 0) { local_rbx = (uint32_t)((uint32_t)(0xC0000023ULL)); }
loc_0092DE54:
    local_rsp = (local_rsp) + (240);
    return (uint32_t)((uint32_t)(local_rbx));
loc_0092DE70:
    if ((((uint8_t)(*(uint8_t *)(v_stack_m88 + 0x1))) & (4)) != 0) goto loc_0092DC20;
    if ((((uint8_t)(*(uint8_t *)(v_stack_m88 + 0x1))) & (1)) == 0) goto loc_0092DF2C;
loc_0092DE84:
    goto loc_0092DC23;
loc_0092DE8C:
    if ((uint32_t)((uint32_t)(v_stack_mA4)) == 0) goto loc_0092DE9A;
    if ((uint8_t)(v_stack_mA5) == 0) goto loc_0092DF39;
loc_0092DE9A:
    if ((*(uint8_t *)(v_stack_m88)) > 8) goto loc_0092DEA4;
    if ((*(uint32_t *)(v_stack_m88 + 0x4)) == ((uint32_t)(v_stack_p10))) goto loc_0092DE3A;
loc_0092DEA4:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mA4)))) + ((uint32_t)(*(uint16_t *)(v_stack_m88 + 0x2))));
    if (((uint32_t)(local_rsi)) > 0xFFFFULL) goto loc_0092DFE6;
    result = (*(uint16_t *)(arg12 + 0x2)) - (v_stack_m98);
    result = (result) + (Arg12);
    if (((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m88 + 0x2)))) > result) goto loc_0092DFDD;
    if (v_stack_mA8 != ((uint8_t)(v_stack_p10))) goto loc_0092DE3A;
    result = memcpy(v_stack_m98, v_stack_m88, (uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m88 + 0x2))), v_stack_m98);
    if (v_stack_mA6 == ((uint8_t)(v_stack_p10))) goto loc_0092DE3A;
    result = RtlpIsDuplicateAce(Arg12, v_stack_m98, (uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m88 + 0x2))), v_stack_m98);
    if ((uint8_t)(result) == 0) goto loc_0092DE3A;
    local_r13 = 0;
    if (0 <= ((uint32_t)(*(uint16_t *)(v_stack_m88 + 0x2)))) {
        local_r13 = (uint32_t)(*(uint16_t *)(v_stack_m88 + 0x2));
    }
    local_rsi = (uint32_t)((local_rsi) - ((uint32_t)(*(uint16_t *)(v_stack_m88 + 0x2))));
    goto loc_0092DE3A;
loc_0092DF2C:
    if ((((uint8_t)(*(uint16_t *)(v_stack_m88 + 0x2))) & (2)) != 0) goto loc_0092DE84;
    goto loc_0092DC20;
loc_0092DF39:
    if (v_stack_mA8 != ((uint8_t)(v_stack_p10))) goto loc_0092DE3A;
    result = (uint8_t)((*(uint8_t *)(arg12 + 0x1)) & (3));
    result = (uint8_t)((result) | (*(uint8_t *)(v_stack_m90 + 0x1)));
    *(uint8_t *)(v_stack_m90 + 0x1) = (uint8_t)(result);
    if (v_stack_mA6 == ((uint8_t)(v_stack_p10))) goto loc_0092DE3A;
    result = (uint8_t)((result) | (16));
    *(uint8_t *)(v_stack_m90 + 0x1) = (uint8_t)(result);
    goto loc_0092DE3A;
loc_0092DF64:
    result = (uint8_t)((*(uint8_t *)(v_stack_m90)) - (5));
    if (((uint8_t)(result)) > 3) goto loc_0092DDEA;
    result = RtlpCompareKnownObjectAces(local_r13, v_stack_m90, (uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m88 + 0x2))), v_stack_m98);
    if ((uint8_t)(result) == 0) goto loc_0092DDE3;
loc_0092DF88:
    result = (uint32_t)(~((uint32_t)(*(uint32_t *)(local_r13 + 0x4))));
    local_r15 = v_stack_m90;
    if ((((uint8_t)(*(uint8_t *)(local_r13 + 0x1))) & (2)) != 0) {
        local_r15 = (uint32_t)((v_stack_m90) & ((uint32_t)(result)));
    }
    local_r12 = v_stack_mA5;
    if ((((uint8_t)(*(uint8_t *)(local_r13 + 0x1))) & (1)) != 0) {
        local_r12 = (uint32_t)((v_stack_mA5) & ((uint32_t)(result)));
    }
    local_r14 = 1;
    if ((((uint8_t)(*(uint8_t *)(local_r13 + 0x1))) & (8)) == 0) {
        local_r14 = (uint32_t)((1) & ((uint32_t)(result)));
    }
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) | ((uint32_t)(local_r12)));
    result = (uint32_t)((result) | ((uint32_t)(local_r15)));
    if (condition_is_not_equal) goto loc_0092DDE3;
    v_stack_m98 = v_stack_m90;
    v_stack_mA4 = (uint32_t)(v_stack_p10);
    goto loc_0092DE29;
loc_0092DFDD:
    v_stack_mA8 = 1;
    goto loc_0092DE3A;
loc_0092DFE6:
    goto loc_0092DE54;
loc_0092DFF0:
    Arg4 = (uint8_t)((v_stack_m90) ^ (*(uint8_t *)((uint32_t)((uint32_t)(v_stack_p10)) + 0x1)));
    if ((((uint8_t)(Arg4)) & (192)) == 0) goto loc_0092DDCE;
    goto loc_0092DDEA;
loc_0092E003:
    if ((((uint8_t)((uint32_t)(0xC000007DULL))) & (2)) == 0) goto loc_0092DE10;
    goto loc_0092DC7A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1` | `8` | `R` |
| `Arg12` | `+ 0x0` | `8` | `R` |
| `Arg12` | `+ 0x1` | `8` | `R` |
| `Arg12` | `+ 0x2` | `16` | `R` |
| `Arg12` | `+ 0x4` | `16` | `R` |
| `Arg12` | `+ 0x4` | `16` | `R/W` |
| `Arg12` | `+ 0x4` | `32` | `R` |
| `Arg12` | `+ 0x8` | `64` | `R` |
| `Arg14` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0092DB80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
