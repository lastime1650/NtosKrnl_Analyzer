# sub_0041A1D1

- RVA: `0x0041A1D1`–`0x0041A754` (길이 `1,411` bytes)
- VA: `0x000000014041A1D1`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009D378`
- 디코드: `344`개 명령, `1,411/1,411` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0041A707` → [RtlpMakeXpressCallback](RtlpMakeXpressCallback_function_0041A7F0.md) (function, `0x0041A7F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x0041A2CF` → [sub_0041A75E + 0x12](Unknown_function_0041A75E.md) (`tail-transfer`)
  - `0x0041A726` → [sub_0041A75E](Unknown_function_0041A75E.md) (`tail-transfer`)
  - `0x0041A73B` → [sub_0041A7B1](Unknown_function_0041A7B1.md) (`tail-transfer`)
  - `0x0041A74F` → [sub_0041A0A8 + 0x96](Unknown_function_0041A0A8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0041A1D1  4C 8B BC 24 D8 00 00 00         mov r15, qword ptr [rsp + 0xd8]
0041A1D9  49 8B C2                        mov rax, r10
0041A1DC  4C 8B 94 24 C0 00 00 00         mov r10, qword ptr [rsp + 0xc0]
0041A1E4  49 8B FF                        mov rdi, r15
0041A1E7  B9 F6 0A 00 00                  mov ecx, 0xaf6
0041A1EC  4C 89 54 24 38                  mov qword ptr [rsp + 0x38], r10
0041A1F1  F3 48 AB                        rep stosq qword ptr [rdi], rax
0041A1F4  49 8D BF B0 57 00 00            lea rdi, [r15 + 0x57b0]
0041A1FB  B9 EE 12 00 00                  mov ecx, 0x12ee
0041A200  F3 48 AB                        rep stosq qword ptr [rdi], rax
0041A203  EB 10                           jmp 0x14041a215
0041A205  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
0041A210  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
0041A215  0F B6 03                        movzx eax, byte ptr [rbx]
0041A218  0F B6 4B 01                     movzx ecx, byte ptr [rbx + 1]
0041A21C  49 8D 14 C7                     lea rdx, [r15 + rax*8]
0041A220  0F B6 43 02                     movzx eax, byte ptr [rbx + 2]
0041A224  48 8D 3C 88                     lea rdi, [rax + rcx*4]
0041A228  48 8B C7                        mov rax, rdi
0041A22B  48 03 C0                        add rax, rax
0041A22E  4C 8B 04 C2                     mov r8, qword ptr [rdx + rax*8]
0041A232  48 89 1C C2                     mov qword ptr [rdx + rax*8], rbx
0041A236  0F B6 0B                        movzx ecx, byte ptr [rbx]
0041A239  41 38 08                        cmp byte ptr [r8], cl
0041A23C  74 1D                           je 0x14041a25b
0041A23E  88 0E                           mov byte ptr [rsi], cl
0041A240  43 8D 04 36                     lea eax, [r14 + r14]
0041A244  48 FF C6                        inc rsi
0041A247  48 FF C3                        inc rbx
0041A24A  48 8B FE                        mov rdi, rsi
0041A24D  45 85 F6                        test r14d, r14d
0041A250  0F 8E 5C 03 00 00               jle 0x14041a5b2
0041A256  44 8B F0                        mov r14d, eax
0041A259  EB BA                           jmp 0x14041a215
0041A25B  0F B6 43 01                     movzx eax, byte ptr [rbx + 1]
0041A25F  41 38 40 01                     cmp byte ptr [r8 + 1], al
0041A263  75 D9                           jne 0x14041a23e
0041A265  0F B6 43 02                     movzx eax, byte ptr [rbx + 2]
0041A269  41 38 40 02                     cmp byte ptr [r8 + 2], al
0041A26D  75 CF                           jne 0x14041a23e
0041A26F  48 8B C3                        mov rax, rbx
0041A272  49 2B C0                        sub rax, r8
0041A275  48 3D 00 20 00 00               cmp rax, 0x2000
0041A27B  7D C1                           jge 0x14041a23e
0041A27D  45 0F B6 50 03                  movzx r10d, byte ptr [r8 + 3]
0041A282  48 8B EB                        mov rbp, rbx
0041A285  44 0F B6 5B 03                  movzx r11d, byte ptr [rbx + 3]
0041A28A  45 3A DA                        cmp r11b, r10b
0041A28D  0F 85 C5 00 00 00               jne 0x14041a358
0041A293  45 0F B6 50 04                  movzx r10d, byte ptr [r8 + 4]
0041A298  44 0F B6 5B 04                  movzx r11d, byte ptr [rbx + 4]
0041A29D  45 3A DA                        cmp r11b, r10b
0041A2A0  0F 85 EF 00 00 00               jne 0x14041a395
0041A2A6  0F B6 43 05                     movzx eax, byte ptr [rbx + 5]
0041A2AA  45 0F B6 68 05                  movzx r13d, byte ptr [r8 + 5]
0041A2AF  88 84 24 B8 00 00 00            mov byte ptr [rsp + 0xb8], al
0041A2B6  41 3A C5                        cmp al, r13b
0041A2B9  0F 85 72 02 00 00               jne 0x14041a531
0041A2BF  4C 8B 4C 24 28                  mov r9, qword ptr [rsp + 0x28]
0041A2C4  48 83 C3 06                     add rbx, 6
0041A2C8  49 83 C0 06                     add r8, 6
0041A2CC  49 3B D9                        cmp rbx, r9
0041A2CF  0F 83 9B 04 00 00               jae 0x14041a770
0041A2D5  8B 03                           mov eax, dword ptr [rbx]
0041A2D7  41 8B 08                        mov ecx, dword ptr [r8]
0041A2DA  3B C1                           cmp eax, ecx
0041A2DC  0F 85 94 01 00 00               jne 0x14041a476
0041A2E2  41 8B 48 04                     mov ecx, dword ptr [r8 + 4]
0041A2E6  8B 43 04                        mov eax, dword ptr [rbx + 4]
0041A2E9  3B C1                           cmp eax, ecx
0041A2EB  0F 85 7D 01 00 00               jne 0x14041a46e
0041A2F1  41 8B 48 08                     mov ecx, dword ptr [r8 + 8]
0041A2F5  8B 43 08                        mov eax, dword ptr [rbx + 8]
0041A2F8  3B C1                           cmp eax, ecx
0041A2FA  0F 85 21 03 00 00               jne 0x14041a621
0041A300  41 8B 48 0C                     mov ecx, dword ptr [r8 + 0xc]
0041A304  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
0041A307  3B C1                           cmp eax, ecx
0041A309  0F 85 B4 03 00 00               jne 0x14041a6c3
0041A30F  41 8B 48 10                     mov ecx, dword ptr [r8 + 0x10]
0041A313  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
0041A316  3B C1                           cmp eax, ecx
0041A318  0F 85 98 03 00 00               jne 0x14041a6b6
0041A31E  41 8B 48 14                     mov ecx, dword ptr [r8 + 0x14]
0041A322  8B 43 14                        mov eax, dword ptr [rbx + 0x14]
0041A325  3B C1                           cmp eax, ecx
0041A327  0F 85 B0 03 00 00               jne 0x14041a6dd
0041A32D  41 8B 48 18                     mov ecx, dword ptr [r8 + 0x18]
0041A331  8B 43 18                        mov eax, dword ptr [rbx + 0x18]
0041A334  3B C1                           cmp eax, ecx
0041A336  0F 85 94 03 00 00               jne 0x14041a6d0
0041A33C  41 8B 48 1C                     mov ecx, dword ptr [r8 + 0x1c]
0041A340  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
0041A343  3B C1                           cmp eax, ecx
0041A345  0F 85 9F 03 00 00               jne 0x14041a6ea
0041A34B  48 83 C3 20                     add rbx, 0x20
0041A34F  49 83 C0 20                     add r8, 0x20
0041A353  E9 74 FF FF FF                  jmp 0x14041a2cc
0041A358  48 8D 0C 79                     lea rcx, [rcx + rdi*2]
0041A35C  4A 8D 04 19                     lea rax, [rcx + r11]
0041A360  49 8B BC C7 B0 57 00 00         mov rdi, qword ptr [r15 + rax*8 + 0x57b0]
0041A368  4A 8D 04 11                     lea rax, [rcx + r10]
0041A36C  4D 89 84 C7 B0 57 00 00         mov qword ptr [r15 + rax*8 + 0x57b0], r8
0041A374  48 8B C3                        mov rax, rbx
0041A377  48 2B C7                        sub rax, rdi
0041A37A  48 3D 00 20 00 00               cmp rax, 0x2000
0041A380  0F 8C 66 01 00 00               jl 0x14041a4ec
0041A386  4C 8B 4C 24 28                  mov r9, qword ptr [rsp + 0x28]
0041A38B  48 83 C3 03                     add rbx, 3
0041A38F  49 83 C0 03                     add r8, 3
0041A393  EB 75                           jmp 0x14041a40a
0041A395  0F B6 53 01                     movzx edx, byte ptr [rbx + 1]
0041A399  0F B6 3B                        movzx edi, byte ptr [rbx]
0041A39C  8D 42 61                        lea eax, [rdx + 0x61]
0041A39F  02 43 02                        add al, byte ptr [rbx + 2]
0041A3A2  D0 C8                           ror al, 1
0041A3A4  40 32 C7                        xor al, dil
0041A3A7  40 02 7B 03                     add dil, byte ptr [rbx + 3]
0041A3AB  C0 C0 03                        rol al, 3
0041A3AE  0F B6 C8                        movzx ecx, al
0041A3B1  40 C0 C7 03                     rol dil, 3
0041A3B5  40 32 FA                        xor dil, dl
0041A3B8  40 D0 CF                        ror dil, 1
0041A3BB  40 0F B6 C7                     movzx eax, dil
0041A3BF  48 8D 14 88                     lea rdx, [rax + rcx*4]
0041A3C3  48 03 D2                        add rdx, rdx
0041A3C6  4A 8D 04 1A                     lea rax, [rdx + r11]
0041A3CA  49 8B 8C C7 B0 57 00 00         mov rcx, qword ptr [r15 + rax*8 + 0x57b0]
0041A3D2  4A 8D 04 12                     lea rax, [rdx + r10]
0041A3D6  4D 89 84 C7 B0 57 00 00         mov qword ptr [r15 + rax*8 + 0x57b0], r8
0041A3DE  48 8B C3                        mov rax, rbx
0041A3E1  48 2B C1                        sub rax, rcx
0041A3E4  48 3D 00 20 00 00               cmp rax, 0x2000
0041A3EA  0F 8C F1 01 00 00               jl 0x14041a5e1
0041A3F0  4C 8B 4C 24 28                  mov r9, qword ptr [rsp + 0x28]
0041A3F5  48 83 C3 04                     add rbx, 4
0041A3F9  49 83 C0 04                     add r8, 4
0041A3FD  4C 8B 6C 24 20                  mov r13, qword ptr [rsp + 0x20]
0041A402  4C 8B A4 24 B0 00 00 00         mov r12, qword ptr [rsp + 0xb0]
0041A40A  48 8B D3                        mov rdx, rbx
0041A40D  48 8B C3                        mov rax, rbx
0041A410  48 2B D5                        sub rdx, rbp
0041A413  49 2B C0                        sub rax, r8
0041A416  48 83 C2 FD                     add rdx, -3
0041A41A  48 8B CA                        mov rcx, rdx
0041A41D  48 8D 04 C5 F8 FF FF FF         lea rax, [rax*8 - 8]
0041A425  48 83 FA 07                     cmp rdx, 7
0041A429  0F 83 81 00 00 00               jae 0x14041a4b0
0041A42F  66 03 C1                        add ax, cx
0041A432  66 89 06                        mov word ptr [rsi], ax
0041A435  48 83 C6 02                     add rsi, 2
0041A439  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
0041A43E  42 8D 04 75 01 00 00 00         lea eax, [r14*2 + 1]
0041A446  45 85 F6                        test r14d, r14d
0041A449  0F 8E DF 01 00 00               jle 0x14041a62e
0041A44F  44 8B F0                        mov r14d, eax
0041A452  49 3B DC                        cmp rbx, r12
0041A455  0F 83 9C 02 00 00               jae 0x14041a6f7
0041A45B  4C 8B 4C 24 28                  mov r9, qword ptr [rsp + 0x28]
0041A460  49 3B F5                        cmp rsi, r13
0041A463  0F 82 A7 FD FF FF               jb 0x14041a210
0041A469  E9 CF 02 00 00                  jmp 0x14041a73d
0041A46E  48 83 C3 04                     add rbx, 4
0041A472  49 83 C0 04                     add r8, 4
0041A476  3A C1                           cmp al, cl
0041A478  75 83                           jne 0x14041a3fd
0041A47A  41 0F B6 40 01                  movzx eax, byte ptr [r8 + 1]
0041A47F  38 43 01                        cmp byte ptr [rbx + 1], al
0041A482  0F 85 85 00 00 00               jne 0x14041a50d
0041A488  41 0F B6 40 02                  movzx eax, byte ptr [r8 + 2]
0041A48D  4C 8B A4 24 B0 00 00 00         mov r12, qword ptr [rsp + 0xb0]
0041A495  4C 8B 6C 24 20                  mov r13, qword ptr [rsp + 0x20]
0041A49A  38 43 02                        cmp byte ptr [rbx + 2], al
0041A49D  0F 84 71 01 00 00               je 0x14041a614
0041A4A3  48 83 C3 02                     add rbx, 2
0041A4A7  49 83 C0 02                     add r8, 2
0041A4AB  E9 5A FF FF FF                  jmp 0x14041a40a
0041A4B0  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
0041A4B5  66 83 C8 07                     or ax, 7
0041A4B9  66 89 06                        mov word ptr [rsi], ax
0041A4BC  48 83 E9 07                     sub rcx, 7
0041A4C0  48 83 C6 02                     add rsi, 2
0041A4C4  48 8B C6                        mov rax, rsi
0041A4C7  48 85 FF                        test rdi, rdi
0041A4CA  74 4C                           je 0x14041a518
0041A4CC  0F B6 07                        movzx eax, byte ptr [rdi]
0041A4CF  48 83 F9 0F                     cmp rcx, 0xf
0041A4D3  0F 83 90 01 00 00               jae 0x14041a669
0041A4D9  C0 E1 04                        shl cl, 4
0041A4DC  0A C8                           or cl, al
0041A4DE  33 C0                           xor eax, eax
0041A4E0  88 0F                           mov byte ptr [rdi], cl
0041A4E2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0041A4E7  E9 4D FF FF FF                  jmp 0x14041a439
0041A4EC  8B 03                           mov eax, dword ptr [rbx]
0041A4EE  3B 07                           cmp eax, dword ptr [rdi]
0041A4F0  0F 85 90 FE FF FF               jne 0x14041a386
0041A4F6  48 C1 E8 18                     shr rax, 0x18
0041A4FA  4C 8B C7                        mov r8, rdi
0041A4FD  48 03 C1                        add rax, rcx
0041A500  49 89 9C C7 B0 57 00 00         mov qword ptr [r15 + rax*8 + 0x57b0], rbx
0041A508  E9 86 FD FF FF                  jmp 0x14041a293
0041A50D  48 FF C3                        inc rbx
0041A510  49 FF C0                        inc r8
0041A513  E9 E5 FE FF FF                  jmp 0x14041a3fd
0041A518  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0041A51D  48 83 F9 0F                     cmp rcx, 0xf
0041A521  0F 83 21 01 00 00               jae 0x14041a648
0041A527  88 0E                           mov byte ptr [rsi], cl
0041A529  48 FF C6                        inc rsi
0041A52C  E9 08 FF FF FF                  jmp 0x14041a439
0041A531  0F B6 4B 04                     movzx ecx, byte ptr [rbx + 4]
0041A535  0F B6 3B                        movzx edi, byte ptr [rbx]
0041A538  40 0F B6 C7                     movzx eax, dil
0041A53C  40 D2 C7                        rol dil, cl
0041A53F  D0 C8                           ror al, 1
0041A541  04 45                           add al, 0x45
0041A543  32 C1                           xor al, cl
0041A545  40 0F B6 CF                     movzx ecx, dil
0041A549  C0 C0 03                        rol al, 3
0041A54C  0F B6 D0                        movzx edx, al
0041A54F  0F B6 43 03                     movzx eax, byte ptr [rbx + 3]
0041A553  C0 C0 03                        rol al, 3
0041A556  32 43 01                        xor al, byte ptr [rbx + 1]
0041A559  D0 C8                           ror al, 1
0041A55B  0F B6 C0                        movzx eax, al
0041A55E  48 03 D0                        add rdx, rax
0041A561  0F B6 43 02                     movzx eax, byte ptr [rbx + 2]
0041A565  48 33 C8                        xor rcx, rax
0041A568  0F B6 84 24 B8 00 00 00         movzx eax, byte ptr [rsp + 0xb8]
0041A570  48 8D 14 91                     lea rdx, [rcx + rdx*4]
0041A574  48 03 D2                        add rdx, rdx
0041A577  48 03 C2                        add rax, rdx
0041A57A  49 8B 8C C7 B0 57 00 00         mov rcx, qword ptr [r15 + rax*8 + 0x57b0]
0041A582  4A 8D 04 2A                     lea rax, [rdx + r13]
0041A586  4D 89 84 C7 B0 57 00 00         mov qword ptr [r15 + rax*8 + 0x57b0], r8
0041A58E  48 8B C3                        mov rax, rbx
0041A591  48 2B C1                        sub rax, rcx
0041A594  48 3D 00 20 00 00               cmp rax, 0x2000
0041A59A  0F 8C D6 00 00 00               jl 0x14041a676
0041A5A0  4C 8B 4C 24 28                  mov r9, qword ptr [rsp + 0x28]
0041A5A5  48 83 C3 05                     add rbx, 5
0041A5A9  49 83 C0 05                     add r8, 5
0041A5AD  E9 4B FE FF FF                  jmp 0x14041a3fd
0041A5B2  48 83 C6 04                     add rsi, 4
0041A5B6  41 89 02                        mov dword ptr [r10], eax
0041A5B9  41 BE 01 00 00 00               mov r14d, 1
0041A5BF  49 3B DC                        cmp rbx, r12
0041A5C2  0F 83 6D 01 00 00               jae 0x14041a735
0041A5C8  48 8B EF                        mov rbp, rdi
0041A5CB  49 3B F5                        cmp rsi, r13
0041A5CE  0F 83 69 01 00 00               jae 0x14041a73d
0041A5D4  4C 8B D7                        mov r10, rdi
0041A5D7  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
0041A5DC  E9 34 FC FF FF                  jmp 0x14041a215
0041A5E1  8B 01                           mov eax, dword ptr [rcx]
0041A5E3  39 03                           cmp dword ptr [rbx], eax
0041A5E5  0F 85 05 FE FF FF               jne 0x14041a3f0
0041A5EB  0F B6 43 04                     movzx eax, byte ptr [rbx + 4]
0041A5EF  3A 41 04                        cmp al, byte ptr [rcx + 4]
0041A5F2  0F 85 F8 FD FF FF               jne 0x14041a3f0
0041A5F8  48 3B D9                        cmp rbx, rcx
0041A5FB  0F 84 EF FD FF FF               je 0x14041a3f0
0041A601  48 03 C2                        add rax, rdx
0041A604  4C 8B C1                        mov r8, rcx
0041A607  49 89 9C C7 B0 57 00 00         mov qword ptr [r15 + rax*8 + 0x57b0], rbx
0041A60F  E9 92 FC FF FF                  jmp 0x14041a2a6
0041A614  48 83 C3 03                     add rbx, 3
0041A618  49 83 C0 03                     add r8, 3
0041A61C  E9 E9 FD FF FF                  jmp 0x14041a40a
0041A621  48 83 C3 08                     add rbx, 8
0041A625  49 83 C0 08                     add r8, 8
0041A629  E9 48 FE FF FF                  jmp 0x14041a476
0041A62E  89 45 00                        mov dword ptr [rbp], eax
0041A631  41 BE 01 00 00 00               mov r14d, 1
0041A637  48 8B EE                        mov rbp, rsi
0041A63A  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
0041A63F  48 83 C6 04                     add rsi, 4
0041A643  E9 0A FE FF FF                  jmp 0x14041a452
0041A648  C6 06 0F                        mov byte ptr [rsi], 0xf
0041A64B  48 FF C6                        inc rsi
0041A64E  48 83 E9 0F                     sub rcx, 0xf
0041A652  48 81 F9 FF 00 00 00            cmp rcx, 0xff
0041A659  0F 83 BD 00 00 00               jae 0x14041a71c
0041A65F  88 0E                           mov byte ptr [rsi], cl
0041A661  48 FF C6                        inc rsi
0041A664  E9 D0 FD FF FF                  jmp 0x14041a439
0041A669  0C F0                           or al, 0xf0
0041A66B  88 07                           mov byte ptr [rdi], al
0041A66D  33 C0                           xor eax, eax
0041A66F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0041A674  EB D8                           jmp 0x14041a64e
0041A676  8B 01                           mov eax, dword ptr [rcx]
0041A678  39 03                           cmp dword ptr [rbx], eax
0041A67A  0F 85 20 FF FF FF               jne 0x14041a5a0
0041A680  0F B6 41 04                     movzx eax, byte ptr [rcx + 4]
0041A684  38 43 04                        cmp byte ptr [rbx + 4], al
0041A687  0F 85 13 FF FF FF               jne 0x14041a5a0
0041A68D  0F B6 43 05                     movzx eax, byte ptr [rbx + 5]
0041A691  48 3B D9                        cmp rbx, rcx
0041A694  0F 84 06 FF FF FF               je 0x14041a5a0
0041A69A  3A 41 05                        cmp al, byte ptr [rcx + 5]
0041A69D  0F 85 FD FE FF FF               jne 0x14041a5a0
0041A6A3  48 03 C2                        add rax, rdx
0041A6A6  4C 8B C1                        mov r8, rcx
0041A6A9  49 89 9C C7 B0 57 00 00         mov qword ptr [r15 + rax*8 + 0x57b0], rbx
0041A6B1  E9 09 FC FF FF                  jmp 0x14041a2bf
0041A6B6  48 83 C3 10                     add rbx, 0x10
0041A6BA  49 83 C0 10                     add r8, 0x10
0041A6BE  E9 B3 FD FF FF                  jmp 0x14041a476
0041A6C3  48 83 C3 0C                     add rbx, 0xc
0041A6C7  49 83 C0 0C                     add r8, 0xc
0041A6CB  E9 A6 FD FF FF                  jmp 0x14041a476
0041A6D0  48 83 C3 18                     add rbx, 0x18
0041A6D4  49 83 C0 18                     add r8, 0x18
0041A6D8  E9 99 FD FF FF                  jmp 0x14041a476
0041A6DD  48 83 C3 14                     add rbx, 0x14
0041A6E1  49 83 C0 14                     add r8, 0x14
0041A6E5  E9 8C FD FF FF                  jmp 0x14041a476
0041A6EA  48 83 C3 1C                     add rbx, 0x1c
0041A6EE  49 83 C0 1C                     add r8, 0x1c
0041A6F2  E9 7F FD FF FF                  jmp 0x14041a476
0041A6F7  49 3B D9                        cmp rbx, r9
0041A6FA  73 41                           jae 0x14041a73d
0041A6FC  4C 8B C3                        mov r8, rbx
0041A6FF  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0041A704  49 8B D1                        mov rdx, r9
0041A707  E8 E4 00 00 00                  call 0x14041a7f0
0041A70C  4C 8B E0                        mov r12, rax
0041A70F  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
0041A717  E9 3F FD FF FF                  jmp 0x14041a45b
0041A71C  C6 06 FF                        mov byte ptr [rsi], 0xff
0041A71F  48 81 FA 00 00 01 00            cmp rdx, 0x10000
0041A726  73 36                           jae 0x14041a75e
0041A728  66 89 56 01                     mov word ptr [rsi + 1], dx
0041A72C  48 83 C6 03                     add rsi, 3
0041A730  E9 04 FD FF FF                  jmp 0x14041a439
0041A735  48 8B EF                        mov rbp, rdi
0041A738  49 3B D9                        cmp rbx, r9
0041A73B  72 74                           jb 0x14041a7b1
0041A73D  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
0041A742  4C 8B 5C 24 48                  mov r11, qword ptr [rsp + 0x48]
0041A747  4C 8B BC 24 C0 00 00 00         mov r15, qword ptr [rsp + 0xc0]
0041A74F  E9 EA F9 FF FF                  jmp 0x14041a13e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0041A1D1(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, unsigned __int8 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_pB0;
    unsigned __int8 v_stack_pB8;

    v_stack_p38 = a24;
    goto loc_0041A215;
loc_0041A210:
loc_0041A215:
    result = (*(unsigned __int8 *)(v_rbx + 2) + *(unsigned __int8 *)(v_rbx + 1) * 4) + (*(unsigned __int8 *)(v_rbx + 2) + *(unsigned __int8 *)(v_rbx + 1) * 4);
    *(unsigned __int64 *)(a27 + *(unsigned __int8 *)(v_rbx) * 8 + result * 8) = v_rbx;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a27 + *(unsigned __int8 *)(v_rbx) * 8 + result * 8))) == ((unsigned __int8)(*(unsigned __int8 *)(v_rbx)))) goto loc_0041A25B;
loc_0041A23E:
    *(unsigned __int8 *)(v_rsi) = (unsigned __int8)(*(unsigned __int8 *)(v_rbx));
    v_rsi = (v_rsi) + 1;
    v_rbx = (v_rbx) + 1;
    if (condition_is_less_or_equal) goto loc_0041A5B2;
    goto loc_0041A215;
loc_0041A25B:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a27 + *(unsigned __int8 *)(v_rbx) * 8 + result * 8) + 1)) != ((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 1)))) goto loc_0041A23E;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a27 + *(unsigned __int8 *)(v_rbx) * 8 + result * 8) + 2)) != ((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 2)))) goto loc_0041A23E;
    result = (v_rbx) - (*(unsigned __int64 *)(a27 + *(unsigned __int8 *)(v_rbx) * 8 + result * 8));
    if (result >= 0x2000ULL) goto loc_0041A23E;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 3))) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a27 + *(unsigned __int8 *)(v_rbx) * 8 + result * 8) + 3)))) goto loc_0041A358;
loc_0041A293:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 4))) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a27 + *(unsigned __int8 *)(v_rbx) * 8 + result * 8) + 4)))) goto loc_0041A395;
loc_0041A2A6:
    v_stack_pB8 = (unsigned __int8)(*(unsigned __int8 *)(v_rbx + 5));
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 5))) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a27 + *(unsigned __int8 *)(v_rbx) * 8 + result * 8) + 5)))) goto loc_0041A531;
loc_0041A2BF:
    v_rbx = (v_rbx) + (6);
    a3 = (*(unsigned __int64 *)(a27 + *(unsigned __int8 *)(v_rbx) * 8 + result * 8)) + (6);
loc_0041A2CC:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a3))))) goto loc_0041A476;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 4)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4))))) goto loc_0041A46E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 8)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 8))))) goto loc_0041A621;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 12)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12))))) goto loc_0041A6C3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 16)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 16))))) goto loc_0041A6B6;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 20)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 20))))) goto loc_0041A6DD;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 24)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 24))))) goto loc_0041A6D0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 28)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 28))))) goto loc_0041A6EA;
    v_rbx = (v_rbx) + (32);
    a3 = (a3) + (32);
    goto loc_0041A2CC;
loc_0041A358:
    *(unsigned __int64 *)(a27 + (unsigned int)(*(unsigned int *)(a3 + 28)) + v_rsi * 2 + *(unsigned __int8 *)(*(unsigned __int64 *)(a27 + *(unsigned __int8 *)(v_rbx) * 8 + result * 8) + 4) * 1 * 8 + 22448) = a3;
    result = (v_rbx) - (*(unsigned __int64 *)(a27 + (unsigned int)(*(unsigned int *)(a3 + 28)) + v_rsi * 2 + *(unsigned __int8 *)(v_rbx + 4) * 1 * 8 + 22448));
    if (result < 0x2000ULL) goto loc_0041A4EC;
loc_0041A386:
    v_rbx = (v_rbx) + (3);
    a3 = (a3) + (3);
    goto loc_0041A40A;
loc_0041A395:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rbx + 1) + 97) + (*(unsigned __int8 *)(v_rbx + 2)));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(*(unsigned __int8 *)(v_rbx))));
    v_rdi = (unsigned __int8)((*(unsigned __int8 *)(v_rbx)) + (*(unsigned __int8 *)(v_rbx + 3)));
    v_rdi = (unsigned __int8)((v_rdi) ^ ((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 1))));
    a2 = ((unsigned __int8)(v_rdi) + (unsigned __int8)(result) * 4) + ((unsigned __int8)(v_rdi) + (unsigned __int8)(result) * 4);
    *(unsigned __int64 *)(a27 + a2 + *(unsigned __int8 *)(*(unsigned __int64 *)(a27 + *(unsigned __int8 *)(v_rbx) * 8 + result * 8) + 4) * 1 * 8 + 22448) = a3;
    result = (v_rbx) - (*(unsigned __int64 *)(a27 + a2 + *(unsigned __int8 *)(v_rbx + 4) * 1 * 8 + 22448));
    if (result < 0x2000ULL) goto loc_0041A5E1;
loc_0041A3F0:
    v_rbx = (v_rbx) + (4);
    a3 = (a3) + (4);
loc_0041A3FD:
loc_0041A40A:
    a2 = (v_rbx) - (v_rbx);
    result = (v_rbx) - (a3);
    a2 = (a2) + (-3);
    if (a2 >= 7) goto loc_0041A4B0;
    result = (unsigned __int16)((result * 8 - 8) + ((unsigned __int16)(a2)));
    *(unsigned __int16 *)(v_rsi) = (unsigned __int16)(result);
    v_rsi = (v_rsi) + (2);
loc_0041A439:
    if (condition_is_less_or_equal) goto loc_0041A62E;
loc_0041A452:
    if (v_rbx >= a22) goto loc_0041A6F7;
loc_0041A45B:
    if (v_rsi < v_stack_p20) goto loc_0041A210;
    goto loc_0041A73D;
loc_0041A46E:
    v_rbx = (v_rbx) + (4);
    a3 = (a3) + (4);
loc_0041A476:
    if (((unsigned __int8)((unsigned int)((unsigned int)(v_r14 + v_r14 * 1)) * 2 + 1)) != ((unsigned __int8)(a2))) goto loc_0041A3FD;
    if ((*(unsigned __int8 *)(v_rbx + 1)) != ((unsigned __int8)(*(unsigned __int8 *)(a3 + 1)))) goto loc_0041A50D;
    if ((*(unsigned __int8 *)(v_rbx + 2)) == ((unsigned __int8)(*(unsigned __int8 *)(a3 + 2)))) goto loc_0041A614;
    v_rbx = (v_rbx) + (2);
    a3 = (a3) + (2);
    goto loc_0041A40A;
loc_0041A4B0:
    result = (unsigned __int16)((*(unsigned __int8 *)(a3 + 2)) | (7));
    *(unsigned __int16 *)(v_rsi) = (unsigned __int16)(result);
    a1 = (a2) - (7);
    v_rsi = (v_rsi) + (2);
    if (a6 == 0) goto loc_0041A518;
    if (a1 >= 15) goto loc_0041A669;
    a1 = (unsigned __int8)((a1) << (4));
    a1 = (unsigned __int8)((a1) | ((unsigned __int8)(*(unsigned __int8 *)(a6))));
    result = 0;
    *(unsigned __int8 *)(a6) = (unsigned __int8)(a1);
    v_stack_p30 = 0;
    goto loc_0041A439;
loc_0041A4EC:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx)))) != (*(unsigned int *)(a6))) goto loc_0041A386;
    result = ((unsigned int)(*(unsigned int *)(v_rbx))) >> (24);
    result = (result) + (a1);
    *(unsigned __int64 *)(a27 + result * 8 + 22448) = v_rbx;
    goto loc_0041A293;
loc_0041A50D:
    v_rbx = (v_rbx) + 1;
    a3 = (a6) + 1;
    goto loc_0041A3FD;
loc_0041A518:
    v_stack_p30 = result;
    if (a1 >= 15) goto loc_0041A648;
    *(unsigned __int8 *)(v_rsi) = (unsigned __int8)(a1);
    v_rsi = (v_rsi) + 1;
    goto loc_0041A439;
loc_0041A531:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_rbx))) + (69));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 4))));
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rbx + 3)) ^ (*(unsigned __int8 *)(v_rbx + 1)));
    a2 = ((unsigned __int8)(result)) + ((unsigned __int8)(result));
    a1 = ((unsigned __int8)(*(unsigned __int8 *)(v_rbx))) ^ (*(unsigned __int8 *)(v_rbx + 2));
    a2 = (a1 + a2 * 4) + (a1 + a2 * 4);
    result = (a23) + (a2);
    *(unsigned __int64 *)(a27 + a2 + v_stack_p20 * 1 * 8 + 22448) = a3;
    result = (v_rbx) - (*(unsigned __int64 *)(a27 + result * 8 + 22448));
    if (result < 0x2000ULL) goto loc_0041A676;
loc_0041A5A0:
    v_rbx = (v_rbx) + (5);
    a3 = (a3) + (5);
    goto loc_0041A3FD;
loc_0041A5B2:
    v_rsi = (v_rsi) + (4);
    *(unsigned int *)(*(unsigned __int8 *)(*(unsigned __int64 *)(a27 + *(unsigned __int8 *)(v_rbx) * 8 + result * 8) + 4)) = (unsigned int)(result);
    if (v_rbx >= a22) goto loc_0041A735;
    if (v_rsi >= v_stack_p20) goto loc_0041A73D;
    v_stack_p38 = *(unsigned __int8 *)(v_rbx);
    goto loc_0041A215;
loc_0041A5E1:
    if ((*(unsigned int *)(v_rbx)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a27 + result * 8 + 22448)))))) goto loc_0041A3F0;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 4))) != (*(unsigned __int8 *)(*(unsigned __int64 *)(a27 + result * 8 + 22448) + 4))) goto loc_0041A3F0;
    if (v_rbx == (*(unsigned __int64 *)(a27 + result * 8 + 22448))) goto loc_0041A3F0;
    result = (*(unsigned __int8 *)(v_rbx + 4)) + (a2);
    *(unsigned __int64 *)(a27 + result * 8 + 22448) = v_rbx;
    goto loc_0041A2A6;
loc_0041A614:
    v_rbx = (v_rbx) + (3);
    a3 = (*(unsigned __int64 *)(a27 + result * 8 + 22448)) + (3);
    goto loc_0041A40A;
loc_0041A621:
    v_rbx = (v_rbx) + (8);
    a3 = (a3) + (8);
    goto loc_0041A476;
loc_0041A62E:
    *(unsigned int *)(*(unsigned __int8 *)(v_rbx)) = (unsigned int)(result);
    v_stack_p38 = v_rsi;
    v_rsi = (v_rsi) + (4);
    goto loc_0041A452;
loc_0041A648:
    *(unsigned __int8 *)(v_rsi) = 15;
    v_rsi = (v_rsi) + 1;
loc_0041A64E:
    a1 = (*(unsigned __int64 *)(a27 + result * 8 + 22448)) - (15);
    if (a1 >= 255) goto loc_0041A71C;
    *(unsigned __int8 *)(v_rsi) = (unsigned __int8)(a1);
    v_rsi = (v_rsi) + 1;
    goto loc_0041A439;
loc_0041A669:
    result = (unsigned __int8)((result) | (240));
    *(unsigned __int8 *)(*(unsigned __int8 *)(v_rbx)) = (unsigned __int8)(result);
    result = 0;
    v_stack_p30 = 0;
    goto loc_0041A64E;
loc_0041A676:
    if ((*(unsigned int *)(v_rbx)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) goto loc_0041A5A0;
    if ((*(unsigned __int8 *)(v_rbx + 4)) != ((unsigned __int8)(*(unsigned __int8 *)(a1 + 4)))) goto loc_0041A5A0;
    if (v_rbx == a1) goto loc_0041A5A0;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 5))) != (*(unsigned __int8 *)(a1 + 5))) goto loc_0041A5A0;
    result = (*(unsigned __int8 *)(v_rbx + 5)) + (a2);
    *(unsigned __int64 *)(a27 + result * 8 + 22448) = v_rbx;
    goto loc_0041A2BF;
loc_0041A6B6:
    v_rbx = (v_rbx) + (16);
    a3 = (a1) + (16);
    goto loc_0041A476;
loc_0041A6C3:
    v_rbx = (v_rbx) + (12);
    a3 = (a3) + (12);
    goto loc_0041A476;
loc_0041A6D0:
    v_rbx = (v_rbx) + (24);
    a3 = (a3) + (24);
    goto loc_0041A476;
loc_0041A6DD:
    v_rbx = (v_rbx) + (20);
    a3 = (a3) + (20);
    goto loc_0041A476;
loc_0041A6EA:
    v_rbx = (v_rbx) + (28);
    a3 = (a3) + (28);
    goto loc_0041A476;
loc_0041A6F7:
    if (v_rbx >= a5) goto loc_0041A73D;
    result = RtlpMakeXpressCallback(a10, a5, v_rbx, a5);
    v_stack_pB0 = result;
    goto loc_0041A45B;
loc_0041A71C:
    *(unsigned __int8 *)(v_rsi) = 255;
    *(unsigned __int16 *)(v_rsi + 1) = (unsigned __int16)(a5);
    v_rsi = (v_rsi) + (3);
    goto loc_0041A439;
loc_0041A735:
loc_0041A73D:
}
```

## 5. (Beta) C Style

```c
int64_t sub_0041A1D1(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, void *Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, int64_t Arg22, uint8_t Arg23, int64_t Arg24, uint64_t Arg25, uint64_t Arg26, void *Arg27)
{
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg27 = (uint8_t *)Arg27;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_pB0;
    uint8_t v_stack_pB8;

    v_stack_p38 = Arg24;
    goto loc_0041A215;
loc_0041A210:
loc_0041A215:
    result = (*(uint8_t *)(local_rbx + 0x2) + *(uint8_t *)(local_rbx + 0x1) * 4) + (*(uint8_t *)(local_rbx + 0x2) + *(uint8_t *)(local_rbx + 0x1) * 4);
    *(uint64_t *)(arg27 + *(uint8_t *)(local_rbx) * 8 + result * 8) = local_rbx;
    if ((*(uint8_t *)(*(uint64_t *)(arg27 + *(uint8_t *)(local_rbx) * 8 + result * 8))) == ((uint8_t)(*(uint8_t *)(local_rbx)))) goto loc_0041A25B;
loc_0041A23E:
    *(uint8_t *)(local_rsi) = (uint8_t)(*(uint8_t *)(local_rbx));
    local_rsi = (local_rsi) + 1;
    local_rbx = (local_rbx) + 1;
    if (condition_is_less_or_equal) goto loc_0041A5B2;
    goto loc_0041A215;
loc_0041A25B:
    if ((*(uint8_t *)(*(uint64_t *)(arg27 + *(uint8_t *)(local_rbx) * 8 + result * 8) + 0x1)) != ((uint8_t)(*(uint8_t *)(local_rbx + 0x1)))) goto loc_0041A23E;
    if ((*(uint8_t *)(*(uint64_t *)(arg27 + *(uint8_t *)(local_rbx) * 8 + result * 8) + 0x2)) != ((uint8_t)(*(uint8_t *)(local_rbx + 0x2)))) goto loc_0041A23E;
    result = (local_rbx) - (*(uint64_t *)(arg27 + *(uint8_t *)(local_rbx) * 8 + result * 8));
    if (result >= 0x2000ULL) goto loc_0041A23E;
    if (((uint8_t)(*(uint8_t *)(local_rbx + 0x3))) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg27 + *(uint8_t *)(local_rbx) * 8 + result * 8) + 0x3)))) goto loc_0041A358;
loc_0041A293:
    if (((uint8_t)(*(uint8_t *)(local_rbx + 0x4))) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg27 + *(uint8_t *)(local_rbx) * 8 + result * 8) + 0x4)))) goto loc_0041A395;
loc_0041A2A6:
    v_stack_pB8 = (uint8_t)(*(uint8_t *)(local_rbx + 0x5));
    if (((uint8_t)(*(uint8_t *)(local_rbx + 0x5))) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg27 + *(uint8_t *)(local_rbx) * 8 + result * 8) + 0x5)))) goto loc_0041A531;
loc_0041A2BF:
    local_rbx = (local_rbx) + (6);
    Arg3 = (*(uint64_t *)(arg27 + *(uint8_t *)(local_rbx) * 8 + result * 8)) + (6);
loc_0041A2CC:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3))))) goto loc_0041A476;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x4)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x4))))) goto loc_0041A46E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x8)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x8))))) goto loc_0041A621;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0xC)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0xC))))) goto loc_0041A6C3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x10)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x10))))) goto loc_0041A6B6;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x14)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x14))))) goto loc_0041A6DD;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x18)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x18))))) goto loc_0041A6D0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x1C)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x1C))))) goto loc_0041A6EA;
    local_rbx = (local_rbx) + (32);
    Arg3 = (Arg3) + (32);
    goto loc_0041A2CC;
loc_0041A358:
    *(uint64_t *)(arg27 + (uint32_t)(*(uint32_t *)(Arg3 + 0x1C)) + local_rsi * 2 + *(uint8_t *)(*(uint64_t *)(arg27 + *(uint8_t *)(local_rbx) * 8 + result * 8) + 0x4) * 1 * 8 + 0x57B0) = Arg3;
    result = (local_rbx) - (*(uint64_t *)(arg27 + (uint32_t)(*(uint32_t *)(Arg3 + 0x1C)) + local_rsi * 2 + *(uint8_t *)(local_rbx + 0x4) * 1 * 8 + 0x57B0));
    if (result < 0x2000ULL) goto loc_0041A4EC;
loc_0041A386:
    local_rbx = (local_rbx) + (3);
    Arg3 = (Arg3) + (3);
    goto loc_0041A40A;
loc_0041A395:
    result = (uint8_t)((*(uint8_t *)(local_rbx + 0x1) + 97) + (*(uint8_t *)(local_rbx + 0x2)));
    result = (uint8_t)((result) ^ ((uint8_t)(*(uint8_t *)(local_rbx))));
    local_rdi = (uint8_t)((*(uint8_t *)(local_rbx)) + (*(uint8_t *)(local_rbx + 0x3)));
    local_rdi = (uint8_t)((local_rdi) ^ ((uint8_t)(*(uint8_t *)(local_rbx + 0x1))));
    Arg2 = ((uint8_t)(local_rdi) + (uint8_t)(result) * 4) + ((uint8_t)(local_rdi) + (uint8_t)(result) * 4);
    *(uint64_t *)(arg27 + Arg2 + *(uint8_t *)(*(uint64_t *)(arg27 + *(uint8_t *)(local_rbx) * 8 + result * 8) + 0x4) * 1 * 8 + 0x57B0) = Arg3;
    result = (local_rbx) - (*(uint64_t *)(arg27 + Arg2 + *(uint8_t *)(local_rbx + 0x4) * 1 * 8 + 0x57B0));
    if (result < 0x2000ULL) goto loc_0041A5E1;
loc_0041A3F0:
    local_rbx = (local_rbx) + (4);
    Arg3 = (Arg3) + (4);
loc_0041A3FD:
loc_0041A40A:
    Arg2 = (local_rbx) - (local_rbx);
    result = (local_rbx) - (Arg3);
    Arg2 = (Arg2) + (-3);
    if (Arg2 >= 7) goto loc_0041A4B0;
    result = (uint16_t)((result * 8 - 8) + ((uint16_t)(Arg2)));
    *(uint16_t *)(local_rsi) = (uint16_t)(result);
    local_rsi = (local_rsi) + (2);
loc_0041A439:
    if (condition_is_less_or_equal) goto loc_0041A62E;
loc_0041A452:
    if (local_rbx >= Arg22) goto loc_0041A6F7;
loc_0041A45B:
    if (local_rsi < v_stack_p20) goto loc_0041A210;
    goto loc_0041A73D;
loc_0041A46E:
    local_rbx = (local_rbx) + (4);
    Arg3 = (Arg3) + (4);
loc_0041A476:
    if (((uint8_t)((uint32_t)((uint32_t)(local_r14 + local_r14 * 1)) * 2 + 1)) != ((uint8_t)(Arg2))) goto loc_0041A3FD;
    if ((*(uint8_t *)(local_rbx + 0x1)) != ((uint8_t)(*(uint8_t *)(Arg3 + 0x1)))) goto loc_0041A50D;
    if ((*(uint8_t *)(local_rbx + 0x2)) == ((uint8_t)(*(uint8_t *)(Arg3 + 0x2)))) goto loc_0041A614;
    local_rbx = (local_rbx) + (2);
    Arg3 = (Arg3) + (2);
    goto loc_0041A40A;
loc_0041A4B0:
    result = (uint16_t)((*(uint8_t *)(Arg3 + 0x2)) | (7));
    *(uint16_t *)(local_rsi) = (uint16_t)(result);
    Arg1 = (Arg2) - (7);
    local_rsi = (local_rsi) + (2);
    if (Arg6 == 0) goto loc_0041A518;
    if (Arg1 >= 15) goto loc_0041A669;
    Arg1 = (uint8_t)((Arg1) << (4));
    Arg1 = (uint8_t)((Arg1) | ((uint8_t)(*(uint8_t *)(Arg6))));
    result = 0;
    *(uint8_t *)(Arg6) = (uint8_t)(Arg1);
    v_stack_p30 = 0;
    goto loc_0041A439;
loc_0041A4EC:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx)))) != (*(uint32_t *)(Arg6))) goto loc_0041A386;
    result = ((uint32_t)(*(uint32_t *)(local_rbx))) >> (24);
    result = (result) + (Arg1);
    *(uint64_t *)(arg27 + result * 8 + 0x57B0) = local_rbx;
    goto loc_0041A293;
loc_0041A50D:
    local_rbx = (local_rbx) + 1;
    Arg3 = (Arg6) + 1;
    goto loc_0041A3FD;
loc_0041A518:
    v_stack_p30 = result;
    if (Arg1 >= 15) goto loc_0041A648;
    *(uint8_t *)(local_rsi) = (uint8_t)(Arg1);
    local_rsi = (local_rsi) + 1;
    goto loc_0041A439;
loc_0041A531:
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(local_rbx))) + (69));
    result = (uint8_t)((result) ^ ((uint8_t)(*(uint8_t *)(local_rbx + 0x4))));
    result = (uint8_t)((*(uint8_t *)(local_rbx + 0x3)) ^ (*(uint8_t *)(local_rbx + 0x1)));
    Arg2 = ((uint8_t)(result)) + ((uint8_t)(result));
    Arg1 = ((uint8_t)(*(uint8_t *)(local_rbx))) ^ (*(uint8_t *)(local_rbx + 0x2));
    Arg2 = (Arg1 + Arg2 * 4) + (Arg1 + Arg2 * 4);
    result = (Arg23) + (Arg2);
    *(uint64_t *)(arg27 + Arg2 + v_stack_p20 * 1 * 8 + 0x57B0) = Arg3;
    result = (local_rbx) - (*(uint64_t *)(arg27 + result * 8 + 0x57B0));
    if (result < 0x2000ULL) goto loc_0041A676;
loc_0041A5A0:
    local_rbx = (local_rbx) + (5);
    Arg3 = (Arg3) + (5);
    goto loc_0041A3FD;
loc_0041A5B2:
    local_rsi = (local_rsi) + (4);
    *(uint32_t *)(*(uint8_t *)(*(uint64_t *)(arg27 + *(uint8_t *)(local_rbx) * 8 + result * 8) + 0x4)) = (uint32_t)(result);
    if (local_rbx >= Arg22) goto loc_0041A735;
    if (local_rsi >= v_stack_p20) goto loc_0041A73D;
    v_stack_p38 = *(uint8_t *)(local_rbx);
    goto loc_0041A215;
loc_0041A5E1:
    if ((*(uint32_t *)(local_rbx)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg27 + result * 8 + 0x57B0)))))) goto loc_0041A3F0;
    if (((uint8_t)(*(uint8_t *)(local_rbx + 0x4))) != (*(uint8_t *)(*(uint64_t *)(arg27 + result * 8 + 0x57B0) + 0x4))) goto loc_0041A3F0;
    if (local_rbx == (*(uint64_t *)(arg27 + result * 8 + 0x57B0))) goto loc_0041A3F0;
    result = (*(uint8_t *)(local_rbx + 0x4)) + (Arg2);
    *(uint64_t *)(arg27 + result * 8 + 0x57B0) = local_rbx;
    goto loc_0041A2A6;
loc_0041A614:
    local_rbx = (local_rbx) + (3);
    Arg3 = (*(uint64_t *)(arg27 + result * 8 + 0x57B0)) + (3);
    goto loc_0041A40A;
loc_0041A621:
    local_rbx = (local_rbx) + (8);
    Arg3 = (Arg3) + (8);
    goto loc_0041A476;
loc_0041A62E:
    *(uint32_t *)(*(uint8_t *)(local_rbx)) = (uint32_t)(result);
    v_stack_p38 = local_rsi;
    local_rsi = (local_rsi) + (4);
    goto loc_0041A452;
loc_0041A648:
    *(uint8_t *)(local_rsi) = 15;
    local_rsi = (local_rsi) + 1;
loc_0041A64E:
    Arg1 = (*(uint64_t *)(arg27 + result * 8 + 0x57B0)) - (15);
    if (Arg1 >= 255) goto loc_0041A71C;
    *(uint8_t *)(local_rsi) = (uint8_t)(Arg1);
    local_rsi = (local_rsi) + 1;
    goto loc_0041A439;
loc_0041A669:
    result = (uint8_t)((result) | (240));
    *(uint8_t *)(*(uint8_t *)(local_rbx)) = (uint8_t)(result);
    result = 0;
    v_stack_p30 = 0;
    goto loc_0041A64E;
loc_0041A676:
    if ((*(uint32_t *)(local_rbx)) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1))))) goto loc_0041A5A0;
    if ((*(uint8_t *)(local_rbx + 0x4)) != ((uint8_t)(*(uint8_t *)(Arg1 + 0x4)))) goto loc_0041A5A0;
    if (local_rbx == Arg1) goto loc_0041A5A0;
    if (((uint8_t)(*(uint8_t *)(local_rbx + 0x5))) != (*(uint8_t *)(Arg1 + 0x5))) goto loc_0041A5A0;
    result = (*(uint8_t *)(local_rbx + 0x5)) + (Arg2);
    *(uint64_t *)(arg27 + result * 8 + 0x57B0) = local_rbx;
    goto loc_0041A2BF;
loc_0041A6B6:
    local_rbx = (local_rbx) + (16);
    Arg3 = (Arg1) + (16);
    goto loc_0041A476;
loc_0041A6C3:
    local_rbx = (local_rbx) + (12);
    Arg3 = (Arg3) + (12);
    goto loc_0041A476;
loc_0041A6D0:
    local_rbx = (local_rbx) + (24);
    Arg3 = (Arg3) + (24);
    goto loc_0041A476;
loc_0041A6DD:
    local_rbx = (local_rbx) + (20);
    Arg3 = (Arg3) + (20);
    goto loc_0041A476;
loc_0041A6EA:
    local_rbx = (local_rbx) + (28);
    Arg3 = (Arg3) + (28);
    goto loc_0041A476;
loc_0041A6F7:
    if (local_rbx >= Arg5) goto loc_0041A73D;
    result = RtlpMakeXpressCallback(Arg10, Arg5, local_rbx, Arg5);
    v_stack_pB0 = result;
    goto loc_0041A45B;
loc_0041A71C:
    *(uint8_t *)(local_rsi) = 255;
    *(uint16_t *)(local_rsi + 0x1) = (uint16_t)(Arg5);
    local_rsi = (local_rsi) + (3);
    goto loc_0041A439;
loc_0041A735:
loc_0041A73D:
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg7` | `+ 0x0` | `32` | `W` |
| `Arg27` | `+ 0x0` | `64` | `W` |
| `Arg27` | `+ 0x0 + rax*8` | `64` | `R` |
| `Arg27` | `+ 0x0 + rax*8` | `64` | `W` |
| `Arg27` | `+ 0x57B0` | `64` | `R` |
| `Arg27` | `+ 0x57B0 + rax*8` | `64` | `R` |
| `Arg27` | `+ 0x57B0 + rax*8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0041A1D1&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
