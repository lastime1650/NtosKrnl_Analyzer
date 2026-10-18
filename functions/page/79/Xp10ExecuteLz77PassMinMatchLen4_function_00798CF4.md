# Xp10ExecuteLz77PassMinMatchLen4

- RVA: `0x00798CF4`–`0x007993CD` (길이 `1,753` bytes)
- VA: `0x0000000140798CF4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BECA4`
- 디코드: `461`개 명령, `1,753/1,753` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [Xp10CompressBuffer](Xp10CompressBuffer_function_007972F4.md) at `0x00797454`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00798CF4  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00798CF9  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00798CFE  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00798D03  53                              push rbx
00798D04  55                              push rbp
00798D05  56                              push rsi
00798D06  57                              push rdi
00798D07  41 54                           push r12
00798D09  41 55                           push r13
00798D0B  41 56                           push r14
00798D0D  41 57                           push r15
00798D0F  48 83 EC 58                     sub rsp, 0x58
00798D13  48 8B 01                        mov rax, qword ptr [rcx]
00798D16  4C 8B D1                        mov r10, rcx
00798D19  45 33 F6                        xor r14d, r14d
00798D1C  49 8B E8                        mov rbp, r8
00798D1F  4D 8B D9                        mov r11, r9
00798D22  44 89 74 24 04                  mov dword ptr [rsp + 4], r14d
00798D27  4C 8D 42 01                     lea r8, [rdx + 1]
00798D2B  0F B7 08                        movzx ecx, word ptr [rax]
00798D2E  49 8D BA 20 16 00 00            lea rdi, [r10 + 0x1620]
00798D35  83 E1 1F                        and ecx, 0x1f
00798D38  45 89 72 18                     mov dword ptr [r10 + 0x18], r14d
00798D3C  41 8D 46 01                     lea eax, [r14 + 1]
00798D40  D3 E0                           shl eax, cl
00798D42  B9 F2 0E 00 00                  mov ecx, 0xef2
00798D47  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
00798D4B  48 8B C2                        mov rax, rdx
00798D4E  F3 48 AB                        rep stosq qword ptr [rdi], rax
00798D51  49 8D BA B0 8D 00 00            lea rdi, [r10 + 0x8db0]
00798D58  B9 EE 12 00 00                  mov ecx, 0x12ee
00798D5D  F3 48 AB                        rep stosq qword ptr [rdi], rax
00798D60  0F B6 02                        movzx eax, byte ptr [rdx]
00798D63  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
00798D6B  66 41 89 01                     mov word ptr [r9], ax
00798D6F  48 83 C1 F1                     add rcx, -0xf
00798D73  49 83 C1 02                     add r9, 2
00798D77  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00798D7C  41 FF 44 82 1C                  inc dword ptr [r10 + rax*4 + 0x1c]
00798D81  48 8D 45 D8                     lea rax, [rbp - 0x28]
00798D85  4C 89 4C 24 10                  mov qword ptr [rsp + 0x10], r9
00798D8A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00798D8F  4C 3B C0                        cmp r8, rax
00798D92  0F 83 DA 05 00 00               jae 0x140799372
00798D98  4C 3B C9                        cmp r9, rcx
00798D9B  0F 83 C9 05 00 00               jae 0x14079936a
00798DA1  44 8B 4C 24 24                  mov r9d, dword ptr [rsp + 0x24]
00798DA6  4D 8D 7A 08                     lea r15, [r10 + 8]
00798DAA  49 8B D8                        mov rbx, r8
00798DAD  44 89 74 24 08                  mov dword ptr [rsp + 8], r14d
00798DB2  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00798DB7  4D 8B E8                        mov r13, r8
00798DBA  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
00798DBF  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
00798DC4  44 89 34 24                     mov dword ptr [rsp], r14d
00798DC8  41 0F B6 48 03                  movzx ecx, byte ptr [r8 + 3]
00798DCD  4D 8D 70 01                     lea r14, [r8 + 1]
00798DD1  41 0F B6 06                     movzx eax, byte ptr [r14]
00798DD5  C1 E0 03                        shl eax, 3
00798DD8  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00798DDD  8D 0C 88                        lea ecx, [rax + rcx*4]
00798DE0  41 0F B6 40 02                  movzx eax, byte ptr [r8 + 2]
00798DE5  8D 14 41                        lea edx, [rcx + rax*2]
00798DE8  41 0F B6 00                     movzx eax, byte ptr [r8]
00798DEC  03 D0                           add edx, eax
00798DEE  4D 8B 9C D2 20 16 00 00         mov r11, qword ptr [r10 + rdx*8 + 0x1620]
00798DF6  4D 89 84 D2 20 16 00 00         mov qword ptr [r10 + rdx*8 + 0x1620], r8
00798DFE  41 8A 00                        mov al, byte ptr [r8]
00798E01  41 38 03                        cmp byte ptr [r11], al
00798E04  0F 85 FB 02 00 00               jne 0x140799105
00798E0A  41 8A 06                        mov al, byte ptr [r14]
00798E0D  41 38 43 01                     cmp byte ptr [r11 + 1], al
00798E11  0F 85 EE 02 00 00               jne 0x140799105
00798E17  41 8A 40 02                     mov al, byte ptr [r8 + 2]
00798E1B  41 38 43 02                     cmp byte ptr [r11 + 2], al
00798E1F  0F 85 E0 02 00 00               jne 0x140799105
00798E25  41 8A 40 03                     mov al, byte ptr [r8 + 3]
00798E29  41 38 43 03                     cmp byte ptr [r11 + 3], al
00798E2D  0F 85 D2 02 00 00               jne 0x140799105
00798E33  41 8B C0                        mov eax, r8d
00798E36  41 2B C3                        sub eax, r11d
00798E39  41 3B C1                        cmp eax, r9d
00798E3C  0F 83 C3 02 00 00               jae 0x140799105
00798E42  4D 3B C3                        cmp r8, r11
00798E45  0F 84 BA 02 00 00               je 0x140799105
00798E4B  41 0F B6 7B 04                  movzx edi, byte ptr [r11 + 4]
00798E50  BB 01 00 00 00                  mov ebx, 1
00798E55  41 0F B6 40 04                  movzx eax, byte ptr [r8 + 4]
00798E5A  89 9C 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], ebx
00798E61  40 3A F8                        cmp dil, al
00798E64  74 54                           je 0x140798eba
00798E66  03 C2                           add eax, edx
00798E68  49 8B 8C C2 B0 8D 00 00         mov rcx, qword ptr [r10 + rax*8 + 0x8db0]
00798E70  8D 04 3A                        lea eax, [rdx + rdi]
00798E73  4D 89 9C C2 B0 8D 00 00         mov qword ptr [r10 + rax*8 + 0x8db0], r11
00798E7B  41 8B 00                        mov eax, dword ptr [r8]
00798E7E  39 01                           cmp dword ptr [rcx], eax
00798E80  0F 85 8B 01 00 00               jne 0x140799011
00798E86  41 0F B6 78 04                  movzx edi, byte ptr [r8 + 4]
00798E8B  40 38 79 04                     cmp byte ptr [rcx + 4], dil
00798E8F  0F 85 7C 01 00 00               jne 0x140799011
00798E95  41 8B C0                        mov eax, r8d
00798E98  2B C1                           sub eax, ecx
00798E9A  41 3B C1                        cmp eax, r9d
00798E9D  0F 83 6E 01 00 00               jae 0x140799011
00798EA3  4C 3B C1                        cmp r8, rcx
00798EA6  0F 84 65 01 00 00               je 0x140799011
00798EAC  8D 04 3A                        lea eax, [rdx + rdi]
00798EAF  4C 8B D9                        mov r11, rcx
00798EB2  4D 89 84 C2 B0 8D 00 00         mov qword ptr [r10 + rax*8 + 0x8db0], r8
00798EBA  41 0F B6 58 05                  movzx ebx, byte ptr [r8 + 5]
00798EBF  41 0F B6 73 05                  movzx esi, byte ptr [r11 + 5]
00798EC4  40 3A DE                        cmp bl, sil
00798EC7  0F 84 9B 00 00 00               je 0x140798f68
00798ECD  41 8A 48 04                     mov cl, byte ptr [r8 + 4]
00798ED1  41 8A 38                        mov dil, byte ptr [r8]
00798ED4  40 8A C7                        mov al, dil
00798ED7  40 D2 C7                        rol dil, cl
00798EDA  D0 C8                           ror al, 1
00798EDC  04 45                           add al, 0x45
00798EDE  32 C1                           xor al, cl
00798EE0  40 0F B6 CF                     movzx ecx, dil
00798EE4  C0 C0 03                        rol al, 3
00798EE7  0F B6 D0                        movzx edx, al
00798EEA  41 8A 40 03                     mov al, byte ptr [r8 + 3]
00798EEE  C0 C0 03                        rol al, 3
00798EF1  41 32 06                        xor al, byte ptr [r14]
00798EF4  D0 C8                           ror al, 1
00798EF6  0F B6 C0                        movzx eax, al
00798EF9  03 D0                           add edx, eax
00798EFB  41 0F B6 40 02                  movzx eax, byte ptr [r8 + 2]
00798F00  33 C8                           xor ecx, eax
00798F02  8D 3C 91                        lea edi, [rcx + rdx*4]
00798F05  03 FF                           add edi, edi
00798F07  8D 04 1F                        lea eax, [rdi + rbx]
00798F0A  49 8B 8C C2 B0 8D 00 00         mov rcx, qword ptr [r10 + rax*8 + 0x8db0]
00798F12  8D 04 37                        lea eax, [rdi + rsi]
00798F15  4D 89 9C C2 B0 8D 00 00         mov qword ptr [r10 + rax*8 + 0x8db0], r11
00798F1D  8B 01                           mov eax, dword ptr [rcx]
00798F1F  41 39 00                        cmp dword ptr [r8], eax
00798F22  0F 85 F0 00 00 00               jne 0x140799018
00798F28  8A 41 04                        mov al, byte ptr [rcx + 4]
00798F2B  41 38 40 04                     cmp byte ptr [r8 + 4], al
00798F2F  0F 85 E3 00 00 00               jne 0x140799018
00798F35  41 0F B6 50 05                  movzx edx, byte ptr [r8 + 5]
00798F3A  3A 51 05                        cmp dl, byte ptr [rcx + 5]
00798F3D  0F 85 D5 00 00 00               jne 0x140799018
00798F43  41 8B C0                        mov eax, r8d
00798F46  2B C1                           sub eax, ecx
00798F48  41 3B C1                        cmp eax, r9d
00798F4B  0F 83 C7 00 00 00               jae 0x140799018
00798F51  4C 3B C1                        cmp r8, rcx
00798F54  0F 84 BE 00 00 00               je 0x140799018
00798F5A  8D 04 17                        lea eax, [rdi + rdx]
00798F5D  4C 8B D9                        mov r11, rcx
00798F60  4D 89 84 C2 B0 8D 00 00         mov qword ptr [r10 + rax*8 + 0x8db0], r8
00798F68  49 8D 58 06                     lea rbx, [r8 + 6]
00798F6C  49 8B C3                        mov rax, r11
00798F6F  49 2B C0                        sub rax, r8
00798F72  48 8D 53 08                     lea rdx, [rbx + 8]
00798F76  48 03 D0                        add rdx, rax
00798F79  49 8B F8                        mov rdi, r8
00798F7C  49 2B FB                        sub rdi, r11
00798F7F  B9 06 00 00 00                  mov ecx, 6
00798F84  48 8D 45 D8                     lea rax, [rbp - 0x28]
00798F88  48 3B D8                        cmp rbx, rax
00798F8B  0F 83 4E 01 00 00               jae 0x1407990df
00798F91  41 8D 41 E0                     lea eax, [r9 - 0x20]
00798F95  3B C8                           cmp ecx, eax
00798F97  0F 83 42 01 00 00               jae 0x1407990df
00798F9D  8B 42 F8                        mov eax, dword ptr [rdx - 8]
00798FA0  39 03                           cmp dword ptr [rbx], eax
00798FA2  0F 85 37 01 00 00               jne 0x1407990df
00798FA8  8B 42 FC                        mov eax, dword ptr [rdx - 4]
00798FAB  39 44 17 FC                     cmp dword ptr [rdi + rdx - 4], eax
00798FAF  0F 85 27 01 00 00               jne 0x1407990dc
00798FB5  8B 02                           mov eax, dword ptr [rdx]
00798FB7  39 04 17                        cmp dword ptr [rdi + rdx], eax
00798FBA  0F 85 17 01 00 00               jne 0x1407990d7
00798FC0  8B 42 04                        mov eax, dword ptr [rdx + 4]
00798FC3  39 44 17 04                     cmp dword ptr [rdi + rdx + 4], eax
00798FC7  0F 85 05 01 00 00               jne 0x1407990d2
00798FCD  8B 42 08                        mov eax, dword ptr [rdx + 8]
00798FD0  39 44 17 08                     cmp dword ptr [rdi + rdx + 8], eax
00798FD4  0F 85 F3 00 00 00               jne 0x1407990cd
00798FDA  8B 42 0C                        mov eax, dword ptr [rdx + 0xc]
00798FDD  39 44 17 0C                     cmp dword ptr [rdi + rdx + 0xc], eax
00798FE1  0F 85 E1 00 00 00               jne 0x1407990c8
00798FE7  8B 42 10                        mov eax, dword ptr [rdx + 0x10]
00798FEA  39 44 17 10                     cmp dword ptr [rdi + rdx + 0x10], eax
00798FEE  0F 85 CF 00 00 00               jne 0x1407990c3
00798FF4  8B 42 14                        mov eax, dword ptr [rdx + 0x14]
00798FF7  39 44 17 14                     cmp dword ptr [rdi + rdx + 0x14], eax
00798FFB  0F 85 BD 00 00 00               jne 0x1407990be
00799001  83 C1 20                        add ecx, 0x20
00799004  48 83 C3 20                     add rbx, 0x20
00799008  48 83 C2 20                     add rdx, 0x20
0079900C  E9 73 FF FF FF                  jmp 0x140798f84
00799011  B9 04 00 00 00                  mov ecx, 4
00799016  EB 0C                           jmp 0x140799024
00799018  B9 05 00 00 00                  mov ecx, 5
0079901D  8B 9C 24 A8 00 00 00            mov ebx, dword ptr [rsp + 0xa8]
00799024  45 8A 30                        mov r14b, byte ptr [r8]
00799027  49 8B EF                        mov rbp, r15
0079902A  44 8B 7C 24 04                  mov r15d, dword ptr [rsp + 4]
0079902F  33 F6                           xor esi, esi
00799031  4C 8B 94 24 B0 00 00 00         mov r10, qword ptr [rsp + 0xb0]
00799039  4C 8B 64 24 28                  mov r12, qword ptr [rsp + 0x28]
0079903E  8B 45 00                        mov eax, dword ptr [rbp]
00799041  49 8B D0                        mov rdx, r8
00799044  48 2B D0                        sub rdx, rax
00799047  44 38 32                        cmp byte ptr [rdx], r14b
0079904A  0F 85 CD 00 00 00               jne 0x14079911d
00799050  41 8A 04 24                     mov al, byte ptr [r12]
00799054  38 42 01                        cmp byte ptr [rdx + 1], al
00799057  0F 85 C0 00 00 00               jne 0x14079911d
0079905D  41 8A 40 02                     mov al, byte ptr [r8 + 2]
00799061  38 42 02                        cmp byte ptr [rdx + 2], al
00799064  0F 85 B3 00 00 00               jne 0x14079911d
0079906A  41 8A 40 03                     mov al, byte ptr [r8 + 3]
0079906E  38 42 03                        cmp byte ptr [rdx + 3], al
00799071  0F 85 A6 00 00 00               jne 0x14079911d
00799077  49 3B D0                        cmp rdx, r8
0079907A  0F 84 9D 00 00 00               je 0x14079911d
00799080  49 8D 58 04                     lea rbx, [r8 + 4]
00799084  BF 04 00 00 00                  mov edi, 4
00799089  49 3B DA                        cmp rbx, r10
0079908C  73 16                           jae 0x1407990a4
0079908E  8B C7                           mov eax, edi
00799090  8A 04 10                        mov al, byte ptr [rax + rdx]
00799093  38 03                           cmp byte ptr [rbx], al
00799095  75 0D                           jne 0x1407990a4
00799097  FF C7                           inc edi
00799099  8B C7                           mov eax, edi
0079909B  4A 8D 1C 07                     lea rbx, [rdi + r8]
0079909F  49 3B DA                        cmp rbx, r10
007990A2  72 EC                           jb 0x140799090
007990A4  3B F9                           cmp edi, ecx
007990A6  72 6E                           jb 0x140799116
007990A8  BB 02 00 00 00                  mov ebx, 2
007990AD  4C 8B DA                        mov r11, rdx
007990B0  89 9C 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], ebx
007990B7  44 8B FE                        mov r15d, esi
007990BA  8B CF                           mov ecx, edi
007990BC  EB 5F                           jmp 0x14079911d
007990BE  83 C1 1C                        add ecx, 0x1c
007990C1  EB 1C                           jmp 0x1407990df
007990C3  83 C1 18                        add ecx, 0x18
007990C6  EB 17                           jmp 0x1407990df
007990C8  83 C1 14                        add ecx, 0x14
007990CB  EB 12                           jmp 0x1407990df
007990CD  83 C1 10                        add ecx, 0x10
007990D0  EB 0D                           jmp 0x1407990df
007990D2  83 C1 0C                        add ecx, 0xc
007990D5  EB 08                           jmp 0x1407990df
007990D7  83 C1 08                        add ecx, 8
007990DA  EB 03                           jmp 0x1407990df
007990DC  83 C1 04                        add ecx, 4
007990DF  8B C1                           mov eax, ecx
007990E1  4A 8D 14 00                     lea rdx, [rax + r8]
007990E5  EB 14                           jmp 0x1407990fb
007990E7  42 8A 04 18                     mov al, byte ptr [rax + r11]
007990EB  38 02                           cmp byte ptr [rdx], al
007990ED  0F 85 2A FF FF FF               jne 0x14079901d
007990F3  FF C1                           inc ecx
007990F5  8B C1                           mov eax, ecx
007990F7  4A 8D 14 01                     lea rdx, [rcx + r8]
007990FB  48 3B D5                        cmp rdx, rbp
007990FE  72 E7                           jb 0x1407990e7
00799100  E9 18 FF FF FF                  jmp 0x14079901d
00799105  33 DB                           xor ebx, ebx
00799107  89 9C 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], ebx
0079910E  8D 4B 01                        lea ecx, [rbx + 1]
00799111  E9 0E FF FF FF                  jmp 0x140799024
00799116  8B 9C 24 A8 00 00 00            mov ebx, dword ptr [rsp + 0xa8]
0079911D  FF C6                           inc esi
0079911F  48 83 C5 04                     add rbp, 4
00799123  83 FE 04                        cmp esi, 4
00799126  0F 82 12 FF FF FF               jb 0x14079903e
0079912C  3B 4C 24 20                     cmp ecx, dword ptr [rsp + 0x20]
00799130  41 8B C7                        mov eax, r15d
00799133  4C 8B 94 24 A0 00 00 00         mov r10, qword ptr [rsp + 0xa0]
0079913B  8B F1                           mov esi, ecx
0079913D  0F 42 5C 24 08                  cmovb ebx, dword ptr [rsp + 8]
00799142  4D 0F 42 C5                     cmovb r8, r13
00799146  0F 42 04 24                     cmovb eax, dword ptr [rsp]
0079914A  4D 8B E8                        mov r13, r8
0079914D  0F 42 74 24 20                  cmovb esi, dword ptr [rsp + 0x20]
00799152  4D 8B C4                        mov r8, r12
00799155  4C 0F 42 5C 24 18               cmovb r11, qword ptr [rsp + 0x18]
0079915B  4D 8B F0                        mov r14, r8
0079915E  4C 8B 64 24 30                  mov r12, qword ptr [rsp + 0x30]
00799163  8B FB                           mov edi, ebx
00799165  48 8B AC 24 B0 00 00 00         mov rbp, qword ptr [rsp + 0xb0]
0079916D  4D 2B F4                        sub r14, r12
00799170  44 89 7C 24 04                  mov dword ptr [rsp + 4], r15d
00799175  4D 8D 7A 08                     lea r15, [r10 + 8]
00799179  89 04 24                        mov dword ptr [rsp], eax
0079917C  89 5C 24 08                     mov dword ptr [rsp + 8], ebx
00799180  4C 89 5C 24 18                  mov qword ptr [rsp + 0x18], r11
00799185  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
00799189  49 83 FE 02                     cmp r14, 2
0079918D  0F 8E 35 FC FF FF               jle 0x140798dc8
00799193  4C 8B 4C 24 10                  mov r9, qword ptr [rsp + 0x10]
00799198  8B E8                           mov ebp, eax
0079919A  89 6C 24 04                     mov dword ptr [rsp + 4], ebp
0079919E  EB 1B                           jmp 0x1407991bb
007991A0  41 0F B6 04 24                  movzx eax, byte ptr [r12]
007991A5  49 8B C9                        mov rcx, r9
007991A8  66 41 89 01                     mov word ptr [r9], ax
007991AC  49 83 C1 02                     add r9, 2
007991B0  0F B7 01                        movzx eax, word ptr [rcx]
007991B3  41 FF 44 82 1C                  inc dword ptr [r10 + rax*4 + 0x1c]
007991B8  49 FF C4                        inc r12
007991BB  4D 3B E5                        cmp r12, r13
007991BE  72 E0                           jb 0x1407991a0
007991C0  45 33 F6                        xor r14d, r14d
007991C3  49 8B D9                        mov rbx, r9
007991C6  45 8B DE                        mov r11d, r14d
007991C9  8B CF                           mov ecx, edi
007991CB  85 FF                           test edi, edi
007991CD  0F 84 5C 01 00 00               je 0x14079932f
007991D3  83 E9 01                        sub ecx, 1
007991D6  0F 84 AA 00 00 00               je 0x140799286
007991DC  83 F9 01                        cmp ecx, 1
007991DF  75 3C                           jne 0x14079921d
007991E1  8D 41 0F                        lea eax, [rcx + 0xf]
007991E4  03 C5                           add eax, ebp
007991E6  66 C1 E0 04                     shl ax, 4
007991EA  66 41 89 01                     mov word ptr [r9], ax
007991EE  41 8B 54 AA 08                  mov edx, dword ptr [r10 + rbp*4 + 8]
007991F3  85 ED                           test ebp, ebp
007991F5  74 26                           je 0x14079921d
007991F7  49 8D 4F 08                     lea rcx, [r15 + 8]
007991FB  83 FD 03                        cmp ebp, 3
007991FE  72 08                           jb 0x140799208
00799200  8B 01                           mov eax, dword ptr [rcx]
00799202  41 89 47 0C                     mov dword ptr [r15 + 0xc], eax
00799206  EB 05                           jmp 0x14079920d
00799208  83 FD 02                        cmp ebp, 2
0079920B  72 06                           jb 0x140799213
0079920D  41 8B 47 04                     mov eax, dword ptr [r15 + 4]
00799211  89 01                           mov dword ptr [rcx], eax
00799213  41 8B 07                        mov eax, dword ptr [r15]
00799216  41 89 47 04                     mov dword ptr [r15 + 4], eax
0079921A  41 89 17                        mov dword ptr [r15], edx
0079921D  48 8B 6C 24 18                  mov rbp, qword ptr [rsp + 0x18]
00799222  41 0F B7 01                     movzx eax, word ptr [r9]
00799226  8D 7E FC                        lea edi, [rsi - 4]
00799229  41 BF 0F 00 00 00               mov r15d, 0xf
0079922F  41 3B FF                        cmp edi, r15d
00799232  0F 82 AE 00 00 00               jb 0x1407992e6
00799238  66 41 03 C7                     add ax, r15w
0079923C  4D 8D 41 02                     lea r8, [r9 + 2]
00799240  66 41 89 01                     mov word ptr [r9], ax
00799244  4D 8D 48 01                     lea r9, [r8 + 1]
00799248  4C 89 4C 24 10                  mov qword ptr [rsp + 0x10], r9
0079924D  81 FF F6 00 00 00               cmp edi, 0xf6
00799253  76 78                           jbe 0x1407992cd
00799255  81 C7 0A FF FF FF               add edi, 0xffffff0a
0079925B  44 89 B4 24 A8 00 00 00         mov dword ptr [rsp + 0xa8], r14d
00799263  0F BD CF                        bsr ecx, edi
00799266  8D 41 E8                        lea eax, [rcx - 0x18]
00799269  41 88 00                        mov byte ptr [r8], al
0079926C  83 FF 01                        cmp edi, 1
0079926F  76 67                           jbe 0x1407992d8
00799271  41 01 4A 18                     add dword ptr [r10 + 0x18], ecx
00799275  41 8D 47 F2                     lea eax, [r15 - 0xe]
00799279  D3 E0                           shl eax, cl
0079927B  2B F8                           sub edi, eax
0079927D  41 89 39                        mov dword ptr [r9], edi
00799280  49 83 C1 04                     add r9, 4
00799284  EB 4D                           jmp 0x1407992d3
00799286  48 8B 6C 24 18                  mov rbp, qword ptr [rsp + 0x18]
0079928B  41 8B CD                        mov ecx, r13d
0079928E  2B CD                           sub ecx, ebp
00799290  44 89 B4 24 A8 00 00 00         mov dword ptr [rsp + 0xa8], r14d
00799298  44 0F BD D9                     bsr r11d, ecx
0079929C  B8 14 00 00 00                  mov eax, 0x14
007992A1  41 03 C3                        add eax, r11d
007992A4  66 C1 E0 04                     shl ax, 4
007992A8  66 41 89 01                     mov word ptr [r9], ax
007992AC  41 8B 42 10                     mov eax, dword ptr [r10 + 0x10]
007992B0  41 89 42 14                     mov dword ptr [r10 + 0x14], eax
007992B4  41 8B 42 0C                     mov eax, dword ptr [r10 + 0xc]
007992B8  41 89 42 10                     mov dword ptr [r10 + 0x10], eax
007992BC  41 8B 42 08                     mov eax, dword ptr [r10 + 8]
007992C0  41 89 42 0C                     mov dword ptr [r10 + 0xc], eax
007992C4  41 89 4A 08                     mov dword ptr [r10 + 8], ecx
007992C8  E9 55 FF FF FF                  jmp 0x140799222
007992CD  41 2A FF                        sub dil, r15b
007992D0  41 88 38                        mov byte ptr [r8], dil
007992D3  4C 89 4C 24 10                  mov qword ptr [rsp + 0x10], r9
007992D8  41 0F B6 00                     movzx eax, byte ptr [r8]
007992DC  41 FF 84 82 1C 0B 00 00         inc dword ptr [r10 + rax*4 + 0xb1c]
007992E4  EB 10                           jmp 0x1407992f6
007992E6  66 03 F8                        add di, ax
007992E9  66 41 89 39                     mov word ptr [r9], di
007992ED  49 83 C1 02                     add r9, 2
007992F1  4C 89 4C 24 10                  mov qword ptr [rsp + 0x10], r9
007992F6  0F B7 03                        movzx eax, word ptr [rbx]
007992F9  41 FF 44 82 1C                  inc dword ptr [r10 + rax*4 + 0x1c]
007992FE  83 7C 24 08 01                  cmp dword ptr [rsp + 8], 1
00799303  75 26                           jne 0x14079932b
00799305  45 85 DB                        test r11d, r11d
00799308  74 21                           je 0x14079932b
0079930A  45 01 5A 18                     add dword ptr [r10 + 0x18], r11d
0079930E  41 8B CB                        mov ecx, r11d
00799311  B8 01 00 00 00                  mov eax, 1
00799316  D3 E0                           shl eax, cl
00799318  41 8B CD                        mov ecx, r13d
0079931B  2B C8                           sub ecx, eax
0079931D  2B CD                           sub ecx, ebp
0079931F  41 89 09                        mov dword ptr [r9], ecx
00799322  49 83 C1 04                     add r9, 4
00799326  4C 89 4C 24 10                  mov qword ptr [rsp + 0x10], r9
0079932B  8B C6                           mov eax, esi
0079932D  EB 1F                           jmp 0x14079934e
0079932F  41 0F B6 45 00                  movzx eax, byte ptr [r13]
00799334  66 41 89 01                     mov word ptr [r9], ax
00799338  49 83 C1 02                     add r9, 2
0079933C  0F B7 03                        movzx eax, word ptr [rbx]
0079933F  4C 89 4C 24 10                  mov qword ptr [rsp + 0x10], r9
00799344  41 FF 44 82 1C                  inc dword ptr [r10 + rax*4 + 0x1c]
00799349  B8 01 00 00 00                  mov eax, 1
0079934E  48 8B AC 24 B0 00 00 00         mov rbp, qword ptr [rsp + 0xb0]
00799356  4E 8D 04 28                     lea r8, [rax + r13]
0079935A  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0079935F  4C 3B 44 24 38                  cmp r8, qword ptr [rsp + 0x38]
00799364  0F 82 2E FA FF FF               jb 0x140798d98
0079936A  4C 8B 9C 24 B8 00 00 00         mov r11, qword ptr [rsp + 0xb8]
00799372  4C 3B C5                        cmp r8, rbp
00799375  73 34                           jae 0x1407993ab
00799377  4C 8B 9C 24 C0 00 00 00         mov r11, qword ptr [rsp + 0xc0]
0079937F  4D 3B CB                        cmp r9, r11
00799382  73 1F                           jae 0x1407993a3
00799384  41 0F B6 00                     movzx eax, byte ptr [r8]
00799388  49 8B C9                        mov rcx, r9
0079938B  66 41 89 01                     mov word ptr [r9], ax
0079938F  49 FF C0                        inc r8
00799392  49 83 C1 02                     add r9, 2
00799396  0F B7 01                        movzx eax, word ptr [rcx]
00799399  41 FF 44 82 1C                  inc dword ptr [r10 + rax*4 + 0x1c]
0079939E  4C 3B C5                        cmp r8, rbp
007993A1  72 DC                           jb 0x14079937f
007993A3  4C 8B 9C 24 B8 00 00 00         mov r11, qword ptr [rsp + 0xb8]
007993AB  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
007993B3  45 2B CB                        sub r9d, r11d
007993B6  44 89 08                        mov dword ptr [rax], r9d
007993B9  33 C0                           xor eax, eax
007993BB  48 83 C4 58                     add rsp, 0x58
007993BF  41 5F                           pop r15
007993C1  41 5E                           pop r14
007993C3  41 5D                           pop r13
007993C5  41 5C                           pop r12
007993C7  5F                              pop rdi
007993C8  5E                              pop rsi
007993C9  5D                              pop rbp
007993CA  5B                              pop rbx
007993CB  C3                              ret
007993CC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Xp10ExecuteLz77PassMinMatchLen4(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (88);
    v_r14 = 0;
    v_stack_m94 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1))) & (31));
    *(unsigned int *)(a1 + 24) = 0;
    result = (unsigned int)((v_r14 + 1) << ((unsigned __int8)(a1)));
    v_stack_m74 = (unsigned int)(result);
    *(unsigned __int16 *)(a4) = (unsigned __int16)(*(unsigned __int8 *)(a2));
    a1 = (a5) + (-15);
    a4 = (a4) + (2);
    v_stack_m58 = a1;
    v_stack_m88 = a4;
    v_stack_m60 = a3 - 40;
    if ((a2 + 1) >= (a3 - 40)) goto loc_00799372;
loc_00798D98:
    if (a4 >= a1) goto loc_0079936A;
    v_stack_m90 = 0;
    v_stack_m80 = a2 + 1;
    v_stack_m68 = a2 + 1;
    v_stack_m78 = 0;
    v_stack_m98 = 0;
loc_00798DC8:
    result = (unsigned int)((*(unsigned __int8 *)(a2 + 1 + 1)) << (3));
    v_stack_m70 = a2 + 1 + 1;
    a2 = (unsigned int)((result + *(unsigned __int8 *)(a2 + 1 + 3) * 4 + *(unsigned __int8 *)(a2 + 1 + 2) * 2) + ((unsigned int)(*(unsigned __int8 *)(a2 + 1))));
    *(unsigned __int64 *)(a1 + a2 * 8 + 5664) = a2 + 1;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + a2 * 8 + 5664))) != ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1)))) goto loc_00799105;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + a2 * 8 + 5664) + 1)) != ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 1)))) goto loc_00799105;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + a2 * 8 + 5664) + 2)) != ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 2)))) goto loc_00799105;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + a2 * 8 + 5664) + 3)) != ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 3)))) goto loc_00799105;
    result = (unsigned int)(((unsigned int)((unsigned int)(a2 + 1))) - ((unsigned int)(*(unsigned __int64 *)(a1 + a2 * 8 + 5664))));
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(v_stack_m74)))) goto loc_00799105;
    if ((a2 + 1) == (*(unsigned __int64 *)(a1 + a2 * 8 + 5664))) goto loc_00799105;
    v_stack_p10 = 1;
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + a2 * 8 + 5664) + 4))) == ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 4)))) goto loc_00798EBA;
    result = (unsigned int)((*(unsigned __int8 *)(a2 + 1 + 4)) + ((unsigned int)(a2)));
    *(unsigned __int64 *)(a1 + a2 + *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + a2 * 8 + 5664) + 4) * 1 * 8 + 36272) = *(unsigned __int64 *)(a1 + a2 * 8 + 5664);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + result * 8 + 36272))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 1))))) goto loc_00799011;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + result * 8 + 36272) + 4)) != ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 4)))) goto loc_00799011;
    result = (unsigned int)(((unsigned int)((unsigned int)(a2 + 1))) - ((unsigned int)(*(unsigned __int64 *)(a1 + result * 8 + 36272))));
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(v_stack_m74)))) goto loc_00799011;
    if ((a2 + 1) == (*(unsigned __int64 *)(a1 + result * 8 + 36272))) goto loc_00799011;
    *(unsigned __int64 *)(a1 + a2 + *(unsigned __int8 *)(a2 + 1 + 4) * 1 * 8 + 36272) = a2 + 1;
loc_00798EBA:
    if (((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 5))) == ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + result * 8 + 36272) + 5)))) goto loc_00798F68;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a2 + 1))) + (69));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 4))));
    result = (unsigned __int8)((*(unsigned __int8 *)(a2 + 1 + 3)) ^ (*(unsigned __int8 *)(a2 + 1 + 1)));
    a2 = (unsigned int)(((unsigned __int8)(result)) + ((unsigned int)((unsigned __int8)(result))));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int8 *)(a2 + 1))) ^ ((unsigned int)(*(unsigned __int8 *)(a2 + 1 + 2))));
    v_rdi = (unsigned int)((a1 + a2 * 4) + ((unsigned int)(a1 + a2 * 4)));
    *(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + result * 8 + 36272) + 5) * 1 * 8 + 36272) = *(unsigned __int64 *)(a1 + result * 8 + 36272);
    if ((*(unsigned int *)(a2 + 1)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 5) * 1 * 8 + 36272)))))) goto loc_00799018;
    if ((*(unsigned __int8 *)(a2 + 1 + 4)) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 5) * 1 * 8 + 36272) + 4)))) goto loc_00799018;
    if (((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 5))) != (*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 5) * 1 * 8 + 36272) + 5))) goto loc_00799018;
    result = (unsigned int)(((unsigned int)((unsigned int)(a2 + 1))) - ((unsigned int)(*(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 5) * 1 * 8 + 36272))));
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(v_stack_m74)))) goto loc_00799018;
    if ((a2 + 1) == (*(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 5) * 1 * 8 + 36272))) goto loc_00799018;
    *(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 5) * 1 * 8 + 36272) = a2 + 1;
loc_00798F68:
    result = (*(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 5) * 1 * 8 + 36272)) - (a2 + 1);
    a2 = (a2 + 1 + 6 + 8) + (result);
    v_rdi = (a2 + 1) - (*(unsigned __int64 *)(a1 + v_rdi + *(unsigned __int8 *)(a2 + 1 + 5) * 1 * 8 + 36272));
loc_00798F84:
    if ((a2 + 1 + 6) >= (a3 - 40)) goto loc_007990DF;
    if (6 >= ((unsigned int)((unsigned int)(v_stack_m74) - 32))) goto loc_007990DF;
    if ((*(unsigned int *)(a2 + 1 + 6)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2 - 8))))) goto loc_007990DF;
    if ((*(unsigned int *)(v_rdi + a2 * 1 - 4)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2 - 4))))) goto loc_007990DC;
    if ((*(unsigned int *)(v_rdi + a2 * 1)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) goto loc_007990D7;
    if ((*(unsigned int *)(v_rdi + a2 * 1 + 4)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4))))) goto loc_007990D2;
    if ((*(unsigned int *)(v_rdi + a2 * 1 + 8)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 8))))) goto loc_007990CD;
    if ((*(unsigned int *)(v_rdi + a2 * 1 + 12)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 12))))) goto loc_007990C8;
    if ((*(unsigned int *)(v_rdi + a2 * 1 + 16)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 16))))) goto loc_007990C3;
    if ((*(unsigned int *)(v_rdi + a2 * 1 + 20)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 20))))) goto loc_007990BE;
    a1 = (unsigned int)((6) + (32));
    v_rbx = (a2 + 1 + 6) + (32);
    a2 = (a2) + (32);
    goto loc_00798F84;
loc_00799011:
    goto loc_00799024;
loc_00799018:
loc_0079901D:
loc_00799024:
    v_rsi = 0;
loc_0079903E:
    a2 = (a2 + 1) - ((unsigned int)(*(unsigned int *)(a1 + 8)));
    if ((*(unsigned __int8 *)(a2)) != ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1)))) goto loc_0079911D;
    if ((*(unsigned __int8 *)(a2 + 1)) != ((unsigned __int8)(*(unsigned __int8 *)(v_stack_m70)))) goto loc_0079911D;
    if ((*(unsigned __int8 *)(a2 + 2)) != ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 2)))) goto loc_0079911D;
    if ((*(unsigned __int8 *)(a2 + 3)) != ((unsigned __int8)(*(unsigned __int8 *)(a2 + 1 + 3)))) goto loc_0079911D;
    if (a2 == (a2 + 1)) goto loc_0079911D;
    if ((a2 + 1 + 4) >= v_stack_p18) goto loc_007990A4;
loc_00799090:
    if ((*(unsigned __int8 *)(a2 + 1 + 4)) != ((unsigned __int8)(*(unsigned __int8 *)(4 + a2 * 1)))) goto loc_007990A4;
    v_rdi = (unsigned int)((4) + 1);
    if ((v_rdi + a2 + 1 * 1) < v_stack_p18) goto loc_00799090;
loc_007990A4:
    if (((unsigned int)(v_rdi)) < 5) goto loc_00799116;
    v_stack_p10 = 2;
    goto loc_0079911D;
loc_007990BE:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) + (28));
    goto loc_007990DF;
loc_007990C3:
    a1 = (unsigned int)((a1) + (24));
    goto loc_007990DF;
loc_007990C8:
    a1 = (unsigned int)((a1) + (20));
    goto loc_007990DF;
loc_007990CD:
    a1 = (unsigned int)((a1) + (16));
    goto loc_007990DF;
loc_007990D2:
    a1 = (unsigned int)((a1) + (12));
    goto loc_007990DF;
loc_007990D7:
    a1 = (unsigned int)((a1) + (8));
    goto loc_007990DF;
loc_007990DC:
    a1 = (unsigned int)((a1) + (4));
loc_007990DF:
    goto loc_007990FB;
loc_007990E7:
    if ((*(unsigned __int8 *)((unsigned int)((unsigned int)(a1)) + a2 + 1 * 1)) != ((unsigned __int8)(*(unsigned __int8 *)((unsigned int)((unsigned int)(a1)) + a2 * 1)))) goto loc_0079901D;
    a1 = (unsigned int)((a1) + 1);
loc_007990FB:
    if ((a1 + a2 + 1 * 1) < (a1 + 8)) goto loc_007990E7;
    goto loc_0079901D;
loc_00799105:
    v_rbx = 0;
    v_stack_p10 = 0;
    goto loc_00799024;
loc_00799116:
loc_0079911D:
    v_rsi = (unsigned int)((v_rsi) + 1);
    v_rbp = (a1 + 8) + (4);
    if (((unsigned int)(v_rsi)) < 4) goto loc_0079903E;
    v_rbx = (unsigned int)(v_stack_p10);
    if (((unsigned int)(v_rbx + 1)) < v_stack_m78) { v_rbx = v_stack_m90; }
    a3 = a2 + 1;
    if (((unsigned int)(v_rbx + 1)) < v_stack_m78) { a3 = a2 + 1; }
    result = 0;
    if (((unsigned int)(v_rbx + 1)) < v_stack_m78) { result = v_stack_m98; }
    v_rsi = (unsigned int)((unsigned int)(v_rbx + 1));
    if (((unsigned int)(v_rbx + 1)) < v_stack_m78) {
        v_rsi = v_stack_m78;
        a2 = v_stack_m80;
    }
    v_r14 = (v_stack_m70) - (v_stack_m68);
    v_stack_m94 = 0;
    v_stack_m98 = (unsigned int)(result);
    v_stack_m90 = (unsigned int)(v_rbx);
    v_stack_m80 = a2;
    v_stack_m78 = (unsigned int)(v_rsi);
    if (v_r14 <= 2) goto loc_00798DC8;
    v_stack_m94 = (unsigned int)((unsigned int)((unsigned int)(result)));
    goto loc_007991BB;
loc_007991A0:
    *(unsigned __int16 *)(v_stack_m88) = (unsigned __int16)(*(unsigned __int8 *)(v_stack_m68));
    a4 = (v_stack_m88) + (2);
    v_r12 = (v_stack_m68) + 1;
loc_007991BB:
    if (v_r12 < a3) goto loc_007991A0;
    v_r14 = 0;
    if ((unsigned int)((unsigned int)((unsigned int)(v_rbx))) == 0) goto loc_0079932F;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rbx))))) - (1));
    if (condition_is_equal) goto loc_00799286;
    if (((unsigned int)(a1)) != 1) goto loc_0079921D;
    result = (unsigned int)((a1 + 15) + ((unsigned int)((unsigned int)((unsigned int)(result)))));
    result = (unsigned __int16)((result) << (4));
    *(unsigned __int16 *)(a4) = (unsigned __int16)(result);
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_0079921D;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) < 3) goto loc_00799208;
    *(unsigned int *)(v_stack_p8 + 8 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 8 + 8)));
    goto loc_0079920D;
loc_00799208:
    result = (unsigned int)(*(unsigned int *)(v_stack_p8 + 8 + 8));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) >= 2) {
        result = *(unsigned int *)(v_stack_p8 + 8 + 4);
        *(unsigned int *)(v_stack_p8 + 8 + 8) = (unsigned int)(result);
    }
    *(unsigned int *)(v_stack_p8 + 8 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 8)));
    *(unsigned int *)(v_stack_p8 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + (unsigned int)((unsigned int)(result)) * 4 + 8)));
loc_0079921D:
loc_00799222:
    if (((unsigned int)(v_rsi - 4)) < 15) goto loc_007992E6;
    result = (unsigned __int16)((*(unsigned __int16 *)(a4)) + (15));
    *(unsigned __int16 *)(a4) = (unsigned __int16)(result);
    v_stack_m88 = a4 + 2 + 1;
    if (((unsigned int)(v_rsi - 4)) <= 246) goto loc_007992CD;
    v_rdi = (unsigned int)((v_rsi - 4) + (0xFFFFFF0AULL));
    v_stack_p10 = 0;
    *(unsigned __int8 *)(a4 + 2) = (unsigned __int8)(v_stack_p8 + 8 + 8 - 24);
    if (((unsigned int)(v_rdi)) <= 1) goto loc_007992D8;
    result = (unsigned int)((15 - 14) << ((unsigned __int8)(v_stack_p8 + 8 + 8)));
    v_rdi = (unsigned int)((v_rdi) - ((unsigned int)(result)));
    *(unsigned int *)(a4 + 2 + 1) = (unsigned int)(v_rdi);
    a4 = (a4 + 2 + 1) + (4);
    goto loc_007992D3;
loc_00799286:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a3))) - ((unsigned int)(v_stack_m80)));
    v_stack_p10 = 0;
    result = (unsigned int)((20) + (0));
    result = (unsigned __int16)((result) << (4));
    *(unsigned __int16 *)(a4) = (unsigned __int16)(result);
    *(unsigned int *)(v_stack_p8 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 16)));
    *(unsigned int *)(v_stack_p8 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 12)));
    *(unsigned int *)(v_stack_p8 + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p8 + 8)));
    *(unsigned int *)(v_stack_p8 + 8) = (unsigned int)(a1);
    goto loc_00799222;
loc_007992CD:
    v_rdi = (unsigned __int8)((v_rdi) - (15));
    *(unsigned __int8 *)(a4 + 2) = (unsigned __int8)(v_rdi);
loc_007992D3:
    v_stack_m88 = a4;
loc_007992D8:
    goto loc_007992F6;
loc_007992E6:
    v_rdi = (unsigned __int16)((v_rdi) + ((unsigned __int16)(*(unsigned __int8 *)(a4 + 2))));
    *(unsigned __int16 *)(a4) = (unsigned __int16)(v_rdi);
    a4 = (a4) + (2);
    v_stack_m88 = a4;
loc_007992F6:
    if (v_stack_m90 != 1) goto loc_0079932B;
    result = *(unsigned __int16 *)(a4);
    if (0 != 0) {
        a1 = 0;
        result = 1;
        result = (unsigned int)((result) << ((unsigned __int8)(a1)));
        a1 = (unsigned int)(a3);
        a1 = (unsigned int)((a1) - ((unsigned int)(result)));
        a1 = (unsigned int)((a1) - ((unsigned int)(v_stack_m80)));
        *(unsigned int *)(a4) = (unsigned int)(a1);
        a4 = (a4) + (4);
        v_stack_m88 = a4;
    }
    goto loc_0079934E;
loc_0079932F:
    *(unsigned __int16 *)(a4) = (unsigned __int16)(*(unsigned __int8 *)(a3));
    a4 = (a4) + (2);
    v_stack_m88 = a4;
loc_0079934E:
    if ((1 + a3 * 1) < v_stack_m60) goto loc_00798D98;
loc_0079936A:
loc_00799372:
    if ((1 + a3 * 1) >= v_stack_p18) goto loc_007993AB;
loc_0079937F:
    if (a4 >= a5) goto loc_007993A3;
    *(unsigned __int16 *)(a4) = (unsigned __int16)(*(unsigned __int8 *)(1 + a3 * 1));
    a3 = (1 + a3 * 1) + 1;
    a4 = (a4) + (2);
    if (a3 < v_stack_p18) goto loc_0079937F;
loc_007993A3:
loc_007993AB:
    a4 = (unsigned int)((a4) - ((unsigned int)(v_stack_p20)));
    *(unsigned int *)(a6) = (unsigned int)(a4);
    result = 0;
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Xp10ExecuteLz77PassMinMatchLen4(void *Arg1, void *Arg2, void *Arg3, void *Arg4, int64_t Arg5, void *Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (88);
    local_r14 = 0;
    v_stack_m94 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(arg1))) & (31));
    *(uint32_t *)(arg1 + 0x18) = 0;
    result = (uint32_t)((local_r14 + 1) << ((uint8_t)(Arg1)));
    v_stack_m74 = (uint32_t)(result);
    *(uint16_t *)(arg4) = (uint16_t)(*(uint8_t *)(arg2));
    Arg1 = (Arg5) + (-15);
    Arg4 = (Arg4) + (2);
    v_stack_m58 = Arg1;
    v_stack_m88 = Arg4;
    v_stack_m60 = Arg3 - 40;
    if ((Arg2 + 1) >= (Arg3 - 40)) goto loc_00799372;
loc_00798D98:
    if (Arg4 >= Arg1) goto loc_0079936A;
    v_stack_m90 = 0;
    v_stack_m80 = Arg2 + 1;
    v_stack_m68 = Arg2 + 1;
    v_stack_m78 = 0;
    v_stack_m98 = 0;
loc_00798DC8:
    result = (uint32_t)((*(uint8_t *)(arg2 + 0x1 + 0x1)) << (3));
    v_stack_m70 = Arg2 + 1 + 1;
    Arg2 = (uint32_t)((result + *(uint8_t *)(arg2 + 0x1 + 0x3) * 4 + *(uint8_t *)(arg2 + 0x1 + 0x2) * 2) + ((uint32_t)(*(uint8_t *)(arg2 + 0x1))));
    *(void **)(arg1 + arg2 * 8 + 0x1620) = Arg2 + 1;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + arg2 * 8 + 0x1620))) != ((uint8_t)(*(uint8_t *)(arg2 + 0x1)))) goto loc_00799105;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + arg2 * 8 + 0x1620) + 0x1)) != ((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x1)))) goto loc_00799105;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + arg2 * 8 + 0x1620) + 0x2)) != ((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x2)))) goto loc_00799105;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + arg2 * 8 + 0x1620) + 0x3)) != ((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x3)))) goto loc_00799105;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2 + 1))) - ((uint32_t)(*(uint64_t *)(arg1 + arg2 * 8 + 0x1620))));
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(v_stack_m74)))) goto loc_00799105;
    if ((Arg2 + 1) == (*(uint64_t *)(arg1 + arg2 * 8 + 0x1620))) goto loc_00799105;
    v_stack_p10 = 1;
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + arg2 * 8 + 0x1620) + 0x4))) == ((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x4)))) goto loc_00798EBA;
    result = (uint32_t)((*(uint8_t *)(arg2 + 0x1 + 0x4)) + ((uint32_t)(Arg2)));
    *(uint64_t *)(arg1 + arg2 + *(uint8_t *)(*(uint64_t *)(arg1 + arg2 * 8 + 0x1620) + 0x4) * 1 * 8 + 0x8DB0) = *(uint64_t *)(arg1 + arg2 * 8 + 0x1620);
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + result * 8 + 0x8DB0))) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x1))))) goto loc_00799011;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + result * 8 + 0x8DB0) + 0x4)) != ((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x4)))) goto loc_00799011;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2 + 1))) - ((uint32_t)(*(uint64_t *)(arg1 + result * 8 + 0x8DB0))));
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(v_stack_m74)))) goto loc_00799011;
    if ((Arg2 + 1) == (*(uint64_t *)(arg1 + result * 8 + 0x8DB0))) goto loc_00799011;
    *(void **)(arg1 + arg2 + *(uint8_t *)(arg2 + 0x1 + 0x4) * 1 * 8 + 0x8DB0) = Arg2 + 1;
loc_00798EBA:
    if (((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x5))) == ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + result * 8 + 0x8DB0) + 0x5)))) goto loc_00798F68;
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(arg2 + 0x1))) + (69));
    result = (uint8_t)((result) ^ ((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x4))));
    result = (uint8_t)((*(uint8_t *)(arg2 + 0x1 + 0x3)) ^ (*(uint8_t *)(arg2 + 0x1 + 0x1)));
    Arg2 = (uint32_t)(((uint8_t)(result)) + ((uint32_t)((uint8_t)(result))));
    Arg1 = (uint32_t)(((uint8_t)(*(uint8_t *)(arg2 + 0x1))) ^ ((uint32_t)(*(uint8_t *)(arg2 + 0x1 + 0x2))));
    local_rdi = (uint32_t)((Arg1 + Arg2 * 4) + ((uint32_t)(Arg1 + Arg2 * 4)));
    *(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(*(uint64_t *)(arg1 + result * 8 + 0x8DB0) + 0x5) * 1 * 8 + 0x8DB0) = *(uint64_t *)(arg1 + result * 8 + 0x8DB0);
    if ((*(uint32_t *)(arg2 + 0x1)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x5) * 1 * 8 + 0x8DB0)))))) goto loc_00799018;
    if ((*(uint8_t *)(arg2 + 0x1 + 0x4)) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x5) * 1 * 8 + 0x8DB0) + 0x4)))) goto loc_00799018;
    if (((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x5))) != (*(uint8_t *)(*(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x5) * 1 * 8 + 0x8DB0) + 0x5))) goto loc_00799018;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg2 + 1))) - ((uint32_t)(*(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x5) * 1 * 8 + 0x8DB0))));
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(v_stack_m74)))) goto loc_00799018;
    if ((Arg2 + 1) == (*(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x5) * 1 * 8 + 0x8DB0))) goto loc_00799018;
    *(void **)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x5) * 1 * 8 + 0x8DB0) = Arg2 + 1;
loc_00798F68:
    result = (*(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x5) * 1 * 8 + 0x8DB0)) - (Arg2 + 1);
    Arg2 = (Arg2 + 1 + 6 + 8) + (result);
    local_rdi = (Arg2 + 1) - (*(uint64_t *)(arg1 + local_rdi + *(uint8_t *)(arg2 + 0x1 + 0x5) * 1 * 8 + 0x8DB0));
loc_00798F84:
    if ((Arg2 + 1 + 6) >= (Arg3 - 40)) goto loc_007990DF;
    if (6 >= ((uint32_t)((uint32_t)(v_stack_m74) - 32))) goto loc_007990DF;
    if ((*(uint32_t *)(arg2 + 0x1 + 0x6)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 - 0x8))))) goto loc_007990DF;
    if ((*(uint32_t *)(local_rdi + arg2 * 1 - 0x4)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 - 0x4))))) goto loc_007990DC;
    if ((*(uint32_t *)(local_rdi + arg2 * 1)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) goto loc_007990D7;
    if ((*(uint32_t *)(local_rdi + arg2 * 1 + 0x4)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x4))))) goto loc_007990D2;
    if ((*(uint32_t *)(local_rdi + arg2 * 1 + 0x8)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x8))))) goto loc_007990CD;
    if ((*(uint32_t *)(local_rdi + arg2 * 1 + 0xC)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xC))))) goto loc_007990C8;
    if ((*(uint32_t *)(local_rdi + arg2 * 1 + 0x10)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x10))))) goto loc_007990C3;
    if ((*(uint32_t *)(local_rdi + arg2 * 1 + 0x14)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x14))))) goto loc_007990BE;
    Arg1 = (uint32_t)((6) + (32));
    local_rbx = (Arg2 + 1 + 6) + (32);
    Arg2 = (Arg2) + (32);
    goto loc_00798F84;
loc_00799011:
    goto loc_00799024;
loc_00799018:
loc_0079901D:
loc_00799024:
    local_rsi = 0;
loc_0079903E:
    Arg2 = (Arg2 + 1) - ((uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    if ((*(uint8_t *)(arg2)) != ((uint8_t)(*(uint8_t *)(arg2 + 0x1)))) goto loc_0079911D;
    if ((*(uint8_t *)(arg2 + 0x1)) != ((uint8_t)(*(uint8_t *)(v_stack_m70)))) goto loc_0079911D;
    if ((*(uint8_t *)(arg2 + 0x2)) != ((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x2)))) goto loc_0079911D;
    if ((*(uint8_t *)(arg2 + 0x3)) != ((uint8_t)(*(uint8_t *)(arg2 + 0x1 + 0x3)))) goto loc_0079911D;
    if (Arg2 == (Arg2 + 1)) goto loc_0079911D;
    if ((Arg2 + 1 + 4) >= v_stack_p18) goto loc_007990A4;
loc_00799090:
    if ((*(uint8_t *)(arg2 + 0x1 + 0x4)) != ((uint8_t)(*(uint8_t *)(4 + arg2 * 1)))) goto loc_007990A4;
    local_rdi = (uint32_t)((4) + 1);
    if ((local_rdi + Arg2 + 1 * 1) < v_stack_p18) goto loc_00799090;
loc_007990A4:
    if (((uint32_t)(local_rdi)) < 5) goto loc_00799116;
    v_stack_p10 = 2;
    goto loc_0079911D;
loc_007990BE:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) + (28));
    goto loc_007990DF;
loc_007990C3:
    Arg1 = (uint32_t)((Arg1) + (24));
    goto loc_007990DF;
loc_007990C8:
    Arg1 = (uint32_t)((Arg1) + (20));
    goto loc_007990DF;
loc_007990CD:
    Arg1 = (uint32_t)((Arg1) + (16));
    goto loc_007990DF;
loc_007990D2:
    Arg1 = (uint32_t)((Arg1) + (12));
    goto loc_007990DF;
loc_007990D7:
    Arg1 = (uint32_t)((Arg1) + (8));
    goto loc_007990DF;
loc_007990DC:
    Arg1 = (uint32_t)((Arg1) + (4));
loc_007990DF:
    goto loc_007990FB;
loc_007990E7:
    if ((*(uint8_t *)((uint32_t)((uint32_t)(arg1)) + arg2 + 0x1 * 1)) != ((uint8_t)(*(uint8_t *)((uint32_t)((uint32_t)(arg1)) + arg2 * 1)))) goto loc_0079901D;
    Arg1 = (uint32_t)((Arg1) + 1);
loc_007990FB:
    if ((Arg1 + Arg2 + 1 * 1) < (Arg1 + 8)) goto loc_007990E7;
    goto loc_0079901D;
loc_00799105:
    local_rbx = 0;
    v_stack_p10 = 0;
    goto loc_00799024;
loc_00799116:
loc_0079911D:
    local_rsi = (uint32_t)((local_rsi) + 1);
    local_rbp = (Arg1 + 8) + (4);
    if (((uint32_t)(local_rsi)) < 4) goto loc_0079903E;
    local_rbx = (uint32_t)(v_stack_p10);
    if (((uint32_t)(local_rbx + 1)) < v_stack_m78) { local_rbx = v_stack_m90; }
    Arg3 = Arg2 + 1;
    if (((uint32_t)(local_rbx + 1)) < v_stack_m78) { Arg3 = Arg2 + 1; }
    result = 0;
    if (((uint32_t)(local_rbx + 1)) < v_stack_m78) { result = v_stack_m98; }
    local_rsi = (uint32_t)((uint32_t)(local_rbx + 1));
    if (((uint32_t)(local_rbx + 1)) < v_stack_m78) {
        local_rsi = v_stack_m78;
        Arg2 = v_stack_m80;
    }
    local_r14 = (v_stack_m70) - (v_stack_m68);
    v_stack_m94 = 0;
    v_stack_m98 = (uint32_t)(result);
    v_stack_m90 = (uint32_t)(local_rbx);
    v_stack_m80 = Arg2;
    v_stack_m78 = (uint32_t)(local_rsi);
    if (local_r14 <= 2) goto loc_00798DC8;
    v_stack_m94 = (uint32_t)((uint32_t)((uint32_t)(result)));
    goto loc_007991BB;
loc_007991A0:
    *(uint16_t *)(v_stack_m88) = (uint16_t)(*(uint8_t *)(v_stack_m68));
    Arg4 = (v_stack_m88) + (2);
    local_r12 = (v_stack_m68) + 1;
loc_007991BB:
    if (local_r12 < Arg3) goto loc_007991A0;
    local_r14 = 0;
    if ((uint32_t)((uint32_t)((uint32_t)(local_rbx))) == 0) goto loc_0079932F;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rbx))))) - (1));
    if (condition_is_equal) goto loc_00799286;
    if (((uint32_t)(Arg1)) != 1) goto loc_0079921D;
    result = (uint32_t)((Arg1 + 15) + ((uint32_t)((uint32_t)((uint32_t)(result)))));
    result = (uint16_t)((result) << (4));
    *(uint16_t *)(arg4) = (uint16_t)(result);
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_0079921D;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) < 3) goto loc_00799208;
    *(uint32_t *)(v_stack_p8 + 0x8 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x8 + 0x8)));
    goto loc_0079920D;
loc_00799208:
    result = (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x8 + 0x8));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) >= 2) {
        result = *(uint32_t *)(v_stack_p8 + 0x8 + 0x4);
        *(uint32_t *)(v_stack_p8 + 0x8 + 0x8) = (uint32_t)(result);
    }
    *(uint32_t *)(v_stack_p8 + 0x8 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x8)));
    *(uint32_t *)(v_stack_p8 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + (uint32_t)((uint32_t)(result)) * 4 + 0x8)));
loc_0079921D:
loc_00799222:
    if (((uint32_t)(local_rsi - 4)) < 15) goto loc_007992E6;
    result = (uint16_t)((*(uint16_t *)(arg4)) + (15));
    *(uint16_t *)(arg4) = (uint16_t)(result);
    v_stack_m88 = Arg4 + 2 + 1;
    if (((uint32_t)(local_rsi - 4)) <= 246) goto loc_007992CD;
    local_rdi = (uint32_t)((local_rsi - 4) + (0xFFFFFF0AULL));
    v_stack_p10 = 0;
    *(uint8_t *)(arg4 + 0x2) = (uint8_t)(v_stack_p8 + 8 + 8 - 24);
    if (((uint32_t)(local_rdi)) <= 1) goto loc_007992D8;
    result = (uint32_t)((15 - 14) << ((uint8_t)(v_stack_p8 + 8 + 8)));
    local_rdi = (uint32_t)((local_rdi) - ((uint32_t)(result)));
    *(uint32_t *)(arg4 + 0x2 + 0x1) = (uint32_t)(local_rdi);
    Arg4 = (Arg4 + 2 + 1) + (4);
    goto loc_007992D3;
loc_00799286:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg3))) - ((uint32_t)(v_stack_m80)));
    v_stack_p10 = 0;
    result = (uint32_t)((20) + (0));
    result = (uint16_t)((result) << (4));
    *(uint16_t *)(arg4) = (uint16_t)(result);
    *(uint32_t *)(v_stack_p8 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x10)));
    *(uint32_t *)(v_stack_p8 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xC)));
    *(uint32_t *)(v_stack_p8 + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p8 + 0x8)));
    *(uint32_t *)(v_stack_p8 + 0x8) = (uint32_t)(Arg1);
    goto loc_00799222;
loc_007992CD:
    local_rdi = (uint8_t)((local_rdi) - (15));
    *(uint8_t *)(arg4 + 0x2) = (uint8_t)(local_rdi);
loc_007992D3:
    v_stack_m88 = Arg4;
loc_007992D8:
    goto loc_007992F6;
loc_007992E6:
    local_rdi = (uint16_t)((local_rdi) + ((uint16_t)(*(uint8_t *)(arg4 + 0x2))));
    *(uint16_t *)(arg4) = (uint16_t)(local_rdi);
    Arg4 = (Arg4) + (2);
    v_stack_m88 = Arg4;
loc_007992F6:
    if (v_stack_m90 != 1) goto loc_0079932B;
    result = *(uint16_t *)(arg4);
    if (0 != 0) {
        Arg1 = 0;
        result = 1;
        result = (uint32_t)((result) << ((uint8_t)(Arg1)));
        Arg1 = (uint32_t)(Arg3);
        Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result)));
        Arg1 = (uint32_t)((Arg1) - ((uint32_t)(v_stack_m80)));
        *(uint32_t *)(arg4) = (uint32_t)(Arg1);
        Arg4 = (Arg4) + (4);
        v_stack_m88 = Arg4;
    }
    goto loc_0079934E;
loc_0079932F:
    *(uint16_t *)(arg4) = (uint16_t)(*(uint8_t *)(arg3));
    Arg4 = (Arg4) + (2);
    v_stack_m88 = Arg4;
loc_0079934E:
    if ((1 + Arg3 * 1) < v_stack_m60) goto loc_00798D98;
loc_0079936A:
loc_00799372:
    if ((1 + Arg3 * 1) >= v_stack_p18) goto loc_007993AB;
loc_0079937F:
    if (Arg4 >= Arg5) goto loc_007993A3;
    *(uint16_t *)(arg4) = (uint16_t)(*(uint8_t *)(1 + arg3 * 1));
    Arg3 = (1 + Arg3 * 1) + 1;
    Arg4 = (Arg4) + (2);
    if (Arg3 < v_stack_p18) goto loc_0079937F;
loc_007993A3:
loc_007993AB:
    Arg4 = (uint32_t)((Arg4) - ((uint32_t)(v_stack_p20)));
    *(uint32_t *)(arg6) = (uint32_t)(Arg4);
    result = 0;
    local_rsp = (local_rsp) + (88);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x18` | `32` | `W` |
| `Arg1` | `+ 0x1C + rax*4` | `32` | `R/W` |
| `Arg1` | `+ 0x1620` | `64` | `R` |
| `Arg1` | `+ 0x8DB0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `8` | `R` |
| `Arg2` | `+ 0x1` | `64` | `R` |
| `Arg3` | `- 0x28` | `64` | `R` |
| `Arg4` | `+ 0x0` | `16` | `W` |
| `Arg6` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00798CF4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
