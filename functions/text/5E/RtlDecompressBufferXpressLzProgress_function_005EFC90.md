# RtlDecompressBufferXpressLzProgress

- RVA: `0x005EFC90`–`0x005F03CB` (길이 `1,851` bytes)
- VA: `0x00000001405EFC90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D011C`
- 디코드: `524`개 명령, `1,851/1,851` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005EFD56` → [RtlpMakeXpressCallback](../41/RtlpMakeXpressCallback_function_0041A7F0.md) (function, `0x0041A7F0`)
- `0x005EFEFD` → [RtlpMakeXpressCallback](../41/RtlpMakeXpressCallback_function_0041A7F0.md) (function, `0x0041A7F0`)
- `0x005EFF6D` → [RtlpMakeXpressCallback](../41/RtlpMakeXpressCallback_function_0041A7F0.md) (function, `0x0041A7F0`)
- `0x005F00F9` → [RtlpMakeXpressCallback](../41/RtlpMakeXpressCallback_function_0041A7F0.md) (function, `0x0041A7F0`)

### Direct callers
- [RtlDecompressBufferProgress](RtlDecompressBufferProgress_function_005EF580.md) at `0x005EF5DD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005EFC90  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
005EFC95  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
005EFC9A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
005EFC9F  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
005EFCA4  57                              push rdi
005EFCA5  41 54                           push r12
005EFCA7  41 55                           push r13
005EFCA9  41 56                           push r14
005EFCAB  41 57                           push r15
005EFCAD  48 83 EC 50                     sub rsp, 0x50
005EFCB1  C7 44 24 44 00 00 00 00         mov dword ptr [rsp + 0x44], 0
005EFCB9  49 8B D8                        mov rbx, r8
005EFCBC  4C 8B D9                        mov r11, rcx
005EFCBF  BE 00 10 00 00                  mov esi, 0x1000
005EFCC4  41 83 F9 05                     cmp r9d, 5
005EFCC8  0F 82 42 05 00 00               jb 0x1405f0210
005EFCCE  41 8B E9                        mov ebp, r9d
005EFCD1  48 8B F9                        mov rdi, rcx
005EFCD4  48 03 EB                        add rbp, rbx
005EFCD7  44 8B D2                        mov r10d, edx
005EFCDA  4C 03 D1                        add r10, rcx
005EFCDD  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
005EFCE5  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
005EFCEA  4C 8D 65 AA                     lea r12, [rbp - 0x56]
005EFCEE  4D 8D AA 90 FE FF FF            lea r13, [r10 - 0x170]
005EFCF5  48 85 C9                        test rcx, rcx
005EFCF8  74 04                           je 0x1405efcfe
005EFCFA  3B D6                           cmp edx, esi
005EFCFC  73 02                           jae 0x1405efd00
005EFCFE  8B F2                           mov esi, edx
005EFD00  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
005EFD08  44 8B C6                        mov r8d, esi
005EFD0B  4D 03 C3                        add r8, r11
005EFD0E  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
005EFD13  4D 3B E8                        cmp r13, r8
005EFD16  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005EFD1B  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
005EFD1F  4D 0F 42 C5                     cmovb r8, r13
005EFD23  45 33 C9                        xor r9d, r9d
005EFD26  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
005EFD2B  8B 33                           mov esi, dword ptr [rbx]
005EFD2D  48 8B CB                        mov rcx, rbx
005EFD30  48 83 C3 04                     add rbx, 4
005EFD34  49 3B DC                        cmp rbx, r12
005EFD37  0F 83 13 02 00 00               jae 0x1405eff50
005EFD3D  49 3B F8                        cmp rdi, r8
005EFD40  72 29                           jb 0x1405efd6b
005EFD42  49 3B FD                        cmp rdi, r13
005EFD45  0F 83 0E 05 00 00               jae 0x1405f0259
005EFD4B  4C 8B C7                        mov r8, rdi
005EFD4E  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
005EFD53  49 8B D5                        mov rdx, r13
005EFD56  E8 95 AA E2 FF                  call 0x14041a7f0
005EFD5B  4C 8B 4C 24 20                  mov r9, qword ptr [rsp + 0x20]
005EFD60  4C 8B C0                        mov r8, rax
005EFD63  4C 8B 9C 24 80 00 00 00         mov r11, qword ptr [rsp + 0x80]
005EFD6B  44 8D 34 75 01 00 00 00         lea r14d, [rsi*2 + 1]
005EFD73  85 F6                           test esi, esi
005EFD75  78 54                           js 0x1405efdcb
005EFD77  45 85 F6                        test r14d, r14d
005EFD7A  79 0D                           jns 0x1405efd89
005EFD7C  0F B6 03                        movzx eax, byte ptr [rbx]
005EFD7F  88 07                           mov byte ptr [rdi], al
005EFD81  48 FF C7                        inc rdi
005EFD84  48 FF C3                        inc rbx
005EFD87  EB 39                           jmp 0x1405efdc2
005EFD89  45 03 F6                        add r14d, r14d
005EFD8C  79 10                           jns 0x1405efd9e
005EFD8E  0F B7 03                        movzx eax, word ptr [rbx]
005EFD91  66 89 07                        mov word ptr [rdi], ax
005EFD94  48 83 C7 02                     add rdi, 2
005EFD98  48 83 C3 02                     add rbx, 2
005EFD9C  EB 24                           jmp 0x1405efdc2
005EFD9E  45 03 F6                        add r14d, r14d
005EFDA1  8B 03                           mov eax, dword ptr [rbx]
005EFDA3  89 07                           mov dword ptr [rdi], eax
005EFDA5  79 0A                           jns 0x1405efdb1
005EFDA7  48 83 C7 03                     add rdi, 3
005EFDAB  48 83 C3 03                     add rbx, 3
005EFDAF  EB 11                           jmp 0x1405efdc2
005EFDB1  48 83 C7 04                     add rdi, 4
005EFDB5  48 83 C3 04                     add rbx, 4
005EFDB9  45 03 F6                        add r14d, r14d
005EFDBC  0F 89 86 01 00 00               jns 0x1405eff48
005EFDC2  45 03 F6                        add r14d, r14d
005EFDC5  0F 84 60 FF FF FF               je 0x1405efd2b
005EFDCB  0F B7 0B                        movzx ecx, word ptr [rbx]
005EFDCE  48 83 C3 02                     add rbx, 2
005EFDD2  44 8B F9                        mov r15d, ecx
005EFDD5  48 C1 E9 03                     shr rcx, 3
005EFDD9  48 FF C1                        inc rcx
005EFDDC  41 83 E7 07                     and r15d, 7
005EFDE0  49 83 FF 07                     cmp r15, 7
005EFDE4  0F 85 82 00 00 00               jne 0x1405efe6c
005EFDEA  4D 85 C9                        test r9, r9
005EFDED  75 10                           jne 0x1405efdff
005EFDEF  4C 8B CB                        mov r9, rbx
005EFDF2  48 FF C3                        inc rbx
005EFDF5  45 0F B6 39                     movzx r15d, byte ptr [r9]
005EFDF9  41 83 E7 0F                     and r15d, 0xf
005EFDFD  EB 0B                           jmp 0x1405efe0a
005EFDFF  45 0F B6 39                     movzx r15d, byte ptr [r9]
005EFE03  49 C1 EF 04                     shr r15, 4
005EFE07  45 33 C9                        xor r9d, r9d
005EFE0A  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
005EFE0F  49 83 FF 0F                     cmp r15, 0xf
005EFE13  75 53                           jne 0x1405efe68
005EFE15  48 8D 43 07                     lea rax, [rbx + 7]
005EFE19  49 3B C4                        cmp rax, r12
005EFE1C  0F 83 D9 01 00 00               jae 0x1405efffb
005EFE22  44 0F B6 3B                     movzx r15d, byte ptr [rbx]
005EFE26  48 FF C3                        inc rbx
005EFE29  49 81 FF FF 00 00 00            cmp r15, 0xff
005EFE30  75 32                           jne 0x1405efe64
005EFE32  44 0F B7 3B                     movzx r15d, word ptr [rbx]
005EFE36  48 83 C3 02                     add rbx, 2
005EFE3A  4D 85 FF                        test r15, r15
005EFE3D  75 07                           jne 0x1405efe46
005EFE3F  44 8B 3B                        mov r15d, dword ptr [rbx]
005EFE42  48 83 C3 04                     add rbx, 4
005EFE46  49 83 FF 16                     cmp r15, 0x16
005EFE4A  0F 82 C0 03 00 00               jb 0x1405f0210
005EFE50  48 8D 47 03                     lea rax, [rdi + 3]
005EFE54  49 03 C7                        add rax, r15
005EFE57  48 3B C7                        cmp rax, rdi
005EFE5A  0F 82 B0 03 00 00               jb 0x1405f0210
005EFE60  49 83 EF 16                     sub r15, 0x16
005EFE64  49 83 C7 0F                     add r15, 0xf
005EFE68  49 83 C7 07                     add r15, 7
005EFE6C  48 8B F7                        mov rsi, rdi
005EFE6F  49 8B D7                        mov rdx, r15
005EFE72  48 2B F1                        sub rsi, rcx
005EFE75  49 83 C7 03                     add r15, 3
005EFE79  49 3B F3                        cmp rsi, r11
005EFE7C  0F 82 8E 03 00 00               jb 0x1405f0210
005EFE82  48 83 F9 04                     cmp rcx, 4
005EFE86  73 40                           jae 0x1405efec8
005EFE88  0F B6 06                        movzx eax, byte ptr [rsi]
005EFE8B  88 07                           mov byte ptr [rdi], al
005EFE8D  48 83 E9 01                     sub rcx, 1
005EFE91  74 1D                           je 0x1405efeb0
005EFE93  0F B6 46 01                     movzx eax, byte ptr [rsi + 1]
005EFE97  88 47 01                        mov byte ptr [rdi + 1], al
005EFE9A  48 83 F9 01                     cmp rcx, 1
005EFE9E  74 06                           je 0x1405efea6
005EFEA0  0F B6 46 02                     movzx eax, byte ptr [rsi + 2]
005EFEA4  EB 13                           jmp 0x1405efeb9
005EFEA6  49 83 EF 02                     sub r15, 2
005EFEAA  48 83 C7 02                     add rdi, 2
005EFEAE  EB 13                           jmp 0x1405efec3
005EFEB0  0F B6 06                        movzx eax, byte ptr [rsi]
005EFEB3  88 47 01                        mov byte ptr [rdi + 1], al
005EFEB6  0F B6 06                        movzx eax, byte ptr [rsi]
005EFEB9  88 47 02                        mov byte ptr [rdi + 2], al
005EFEBC  4C 8B FA                        mov r15, rdx
005EFEBF  48 83 C7 03                     add rdi, 3
005EFEC3  4D 85 FF                        test r15, r15
005EFEC6  74 77                           je 0x1405eff3f
005EFEC8  8B 06                           mov eax, dword ptr [rsi]
005EFECA  89 07                           mov dword ptr [rdi], eax
005EFECC  8B 46 04                        mov eax, dword ptr [rsi + 4]
005EFECF  89 47 04                        mov dword ptr [rdi + 4], eax
005EFED2  49 83 FF 09                     cmp r15, 9
005EFED6  7C 64                           jl 0x1405eff3c
005EFED8  48 83 C7 08                     add rdi, 8
005EFEDC  48 83 C6 08                     add rsi, 8
005EFEE0  49 83 EF 08                     sub r15, 8
005EFEE4  49 3B F8                        cmp rdi, r8
005EFEE7  72 1C                           jb 0x1405eff05
005EFEE9  49 3B FD                        cmp rdi, r13
005EFEEC  0F 83 EF 02 00 00               jae 0x1405f01e1
005EFEF2  4C 8B C7                        mov r8, rdi
005EFEF5  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
005EFEFA  49 8B D5                        mov rdx, r13
005EFEFD  E8 EE A8 E2 FF                  call 0x14041a7f0
005EFF02  4C 8B C0                        mov r8, rax
005EFF05  8B 06                           mov eax, dword ptr [rsi]
005EFF07  89 07                           mov dword ptr [rdi], eax
005EFF09  8B 46 04                        mov eax, dword ptr [rsi + 4]
005EFF0C  89 47 04                        mov dword ptr [rdi + 4], eax
005EFF0F  8B 46 08                        mov eax, dword ptr [rsi + 8]
005EFF12  89 47 08                        mov dword ptr [rdi + 8], eax
005EFF15  8B 46 0C                        mov eax, dword ptr [rsi + 0xc]
005EFF18  89 47 0C                        mov dword ptr [rdi + 0xc], eax
005EFF1B  49 83 FF 11                     cmp r15, 0x11
005EFF1F  7C 0E                           jl 0x1405eff2f
005EFF21  48 83 C7 10                     add rdi, 0x10
005EFF25  48 83 C6 10                     add rsi, 0x10
005EFF29  49 83 EF 10                     sub r15, 0x10
005EFF2D  EB B5                           jmp 0x1405efee4
005EFF2F  4C 8B 4C 24 20                  mov r9, qword ptr [rsp + 0x20]
005EFF34  4C 8B 9C 24 80 00 00 00         mov r11, qword ptr [rsp + 0x80]
005EFF3C  49 03 FF                        add rdi, r15
005EFF3F  45 85 F6                        test r14d, r14d
005EFF42  0F 88 7A FE FF FF               js 0x1405efdc2
005EFF48  45 03 F6                        add r14d, r14d
005EFF4B  E9 27 FE FF FF                  jmp 0x1405efd77
005EFF50  48 8D 59 04                     lea rbx, [rcx + 4]
005EFF54  49 3B F8                        cmp rdi, r8
005EFF57  72 29                           jb 0x1405eff82
005EFF59  49 3B FD                        cmp rdi, r13
005EFF5C  0F 83 F7 02 00 00               jae 0x1405f0259
005EFF62  4C 8B C7                        mov r8, rdi
005EFF65  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
005EFF6A  49 8B D5                        mov rdx, r13
005EFF6D  E8 7E A8 E2 FF                  call 0x14041a7f0
005EFF72  4C 8B 4C 24 20                  mov r9, qword ptr [rsp + 0x20]
005EFF77  4C 8B C0                        mov r8, rax
005EFF7A  4C 8B 9C 24 80 00 00 00         mov r11, qword ptr [rsp + 0x80]
005EFF82  44 8D 34 75 01 00 00 00         lea r14d, [rsi*2 + 1]
005EFF8A  85 F6                           test esi, esi
005EFF8C  0F 89 B5 01 00 00               jns 0x1405f0147
005EFF92  48 3B DD                        cmp rbx, rbp
005EFF95  0F 84 99 02 00 00               je 0x1405f0234
005EFF9B  48 8D 43 01                     lea rax, [rbx + 1]
005EFF9F  48 3B C5                        cmp rax, rbp
005EFFA2  0F 83 5E 02 00 00               jae 0x1405f0206
005EFFA8  0F B7 0B                        movzx ecx, word ptr [rbx]
005EFFAB  48 83 C3 02                     add rbx, 2
005EFFAF  44 8B F9                        mov r15d, ecx
005EFFB2  48 C1 E9 03                     shr rcx, 3
005EFFB6  48 FF C1                        inc rcx
005EFFB9  41 83 E7 07                     and r15d, 7
005EFFBD  49 83 FF 07                     cmp r15, 7
005EFFC1  0F 85 A1 00 00 00               jne 0x1405f0068
005EFFC7  4D 85 C9                        test r9, r9
005EFFCA  75 19                           jne 0x1405effe5
005EFFCC  48 3B DD                        cmp rbx, rbp
005EFFCF  0F 83 3B 02 00 00               jae 0x1405f0210
005EFFD5  4C 8B CB                        mov r9, rbx
005EFFD8  48 FF C3                        inc rbx
005EFFDB  45 0F B6 39                     movzx r15d, byte ptr [r9]
005EFFDF  41 83 E7 0F                     and r15d, 0xf
005EFFE3  EB 0B                           jmp 0x1405efff0
005EFFE5  45 0F B6 39                     movzx r15d, byte ptr [r9]
005EFFE9  49 C1 EF 04                     shr r15, 4
005EFFED  45 33 C9                        xor r9d, r9d
005EFFF0  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
005EFFF5  49 83 FF 0F                     cmp r15, 0xf
005EFFF9  75 69                           jne 0x1405f0064
005EFFFB  48 3B DD                        cmp rbx, rbp
005EFFFE  0F 83 0C 02 00 00               jae 0x1405f0210
005F0004  44 0F B6 3B                     movzx r15d, byte ptr [rbx]
005F0008  48 FF C3                        inc rbx
005F000B  49 81 FF FF 00 00 00            cmp r15, 0xff
005F0012  75 4C                           jne 0x1405f0060
005F0014  48 8D 43 01                     lea rax, [rbx + 1]
005F0018  48 3B C5                        cmp rax, rbp
005F001B  0F 83 EF 01 00 00               jae 0x1405f0210
005F0021  44 0F B7 3B                     movzx r15d, word ptr [rbx]
005F0025  48 83 C3 02                     add rbx, 2
005F0029  4D 85 FF                        test r15, r15
005F002C  75 14                           jne 0x1405f0042
005F002E  48 8D 43 03                     lea rax, [rbx + 3]
005F0032  48 3B C5                        cmp rax, rbp
005F0035  0F 83 D5 01 00 00               jae 0x1405f0210
005F003B  44 8B 3B                        mov r15d, dword ptr [rbx]
005F003E  48 83 C3 04                     add rbx, 4
005F0042  49 83 FF 16                     cmp r15, 0x16
005F0046  0F 82 C4 01 00 00               jb 0x1405f0210
005F004C  48 8D 47 03                     lea rax, [rdi + 3]
005F0050  49 03 C7                        add rax, r15
005F0053  48 3B C7                        cmp rax, rdi
005F0056  0F 82 B4 01 00 00               jb 0x1405f0210
005F005C  49 83 EF 16                     sub r15, 0x16
005F0060  49 83 C7 0F                     add r15, 0xf
005F0064  49 83 C7 07                     add r15, 7
005F0068  48 8B F7                        mov rsi, rdi
005F006B  49 8B D7                        mov rdx, r15
005F006E  48 2B F1                        sub rsi, rcx
005F0071  49 83 C7 03                     add r15, 3
005F0075  49 3B F3                        cmp rsi, r11
005F0078  0F 82 92 01 00 00               jb 0x1405f0210
005F007E  48 83 F9 04                     cmp rcx, 4
005F0082  73 40                           jae 0x1405f00c4
005F0084  0F B6 06                        movzx eax, byte ptr [rsi]
005F0087  88 07                           mov byte ptr [rdi], al
005F0089  48 83 E9 01                     sub rcx, 1
005F008D  74 1D                           je 0x1405f00ac
005F008F  0F B6 46 01                     movzx eax, byte ptr [rsi + 1]
005F0093  88 47 01                        mov byte ptr [rdi + 1], al
005F0096  48 83 F9 01                     cmp rcx, 1
005F009A  74 06                           je 0x1405f00a2
005F009C  0F B6 46 02                     movzx eax, byte ptr [rsi + 2]
005F00A0  EB 13                           jmp 0x1405f00b5
005F00A2  49 83 EF 02                     sub r15, 2
005F00A6  48 83 C7 02                     add rdi, 2
005F00AA  EB 13                           jmp 0x1405f00bf
005F00AC  0F B6 06                        movzx eax, byte ptr [rsi]
005F00AF  88 47 01                        mov byte ptr [rdi + 1], al
005F00B2  0F B6 06                        movzx eax, byte ptr [rsi]
005F00B5  88 47 02                        mov byte ptr [rdi + 2], al
005F00B8  4C 8B FA                        mov r15, rdx
005F00BB  48 83 C7 03                     add rdi, 3
005F00BF  4D 85 FF                        test r15, r15
005F00C2  74 77                           je 0x1405f013b
005F00C4  8B 06                           mov eax, dword ptr [rsi]
005F00C6  89 07                           mov dword ptr [rdi], eax
005F00C8  8B 46 04                        mov eax, dword ptr [rsi + 4]
005F00CB  89 47 04                        mov dword ptr [rdi + 4], eax
005F00CE  49 83 FF 09                     cmp r15, 9
005F00D2  7C 64                           jl 0x1405f0138
005F00D4  48 83 C7 08                     add rdi, 8
005F00D8  48 83 C6 08                     add rsi, 8
005F00DC  49 83 EF 08                     sub r15, 8
005F00E0  49 3B F8                        cmp rdi, r8
005F00E3  72 1C                           jb 0x1405f0101
005F00E5  49 3B FD                        cmp rdi, r13
005F00E8  0F 83 F3 00 00 00               jae 0x1405f01e1
005F00EE  4C 8B C7                        mov r8, rdi
005F00F1  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
005F00F6  49 8B D5                        mov rdx, r13
005F00F9  E8 F2 A6 E2 FF                  call 0x14041a7f0
005F00FE  4C 8B C0                        mov r8, rax
005F0101  8B 06                           mov eax, dword ptr [rsi]
005F0103  89 07                           mov dword ptr [rdi], eax
005F0105  8B 46 04                        mov eax, dword ptr [rsi + 4]
005F0108  89 47 04                        mov dword ptr [rdi + 4], eax
005F010B  8B 46 08                        mov eax, dword ptr [rsi + 8]
005F010E  89 47 08                        mov dword ptr [rdi + 8], eax
005F0111  8B 46 0C                        mov eax, dword ptr [rsi + 0xc]
005F0114  89 47 0C                        mov dword ptr [rdi + 0xc], eax
005F0117  49 83 FF 11                     cmp r15, 0x11
005F011B  7C 0E                           jl 0x1405f012b
005F011D  48 83 C7 10                     add rdi, 0x10
005F0121  48 83 C6 10                     add rsi, 0x10
005F0125  49 83 EF 10                     sub r15, 0x10
005F0129  EB B5                           jmp 0x1405f00e0
005F012B  4C 8B 4C 24 20                  mov r9, qword ptr [rsp + 0x20]
005F0130  4C 8B 9C 24 80 00 00 00         mov r11, qword ptr [rsp + 0x80]
005F0138  49 03 FF                        add rdi, r15
005F013B  45 85 F6                        test r14d, r14d
005F013E  0F 88 81 00 00 00               js 0x1405f01c5
005F0144  45 03 F6                        add r14d, r14d
005F0147  45 85 F6                        test r14d, r14d
005F014A  78 69                           js 0x1405f01b5
005F014C  45 03 F6                        add r14d, r14d
005F014F  78 4B                           js 0x1405f019c
005F0151  45 03 F6                        add r14d, r14d
005F0154  78 23                           js 0x1405f0179
005F0156  45 03 F6                        add r14d, r14d
005F0159  48 8D 43 03                     lea rax, [rbx + 3]
005F015D  48 3B C5                        cmp rax, rbp
005F0160  0F 83 AA 00 00 00               jae 0x1405f0210
005F0166  8B 03                           mov eax, dword ptr [rbx]
005F0168  48 83 C3 04                     add rbx, 4
005F016C  89 07                           mov dword ptr [rdi], eax
005F016E  48 83 C7 04                     add rdi, 4
005F0172  45 85 F6                        test r14d, r14d
005F0175  78 4E                           js 0x1405f01c5
005F0177  EB CB                           jmp 0x1405f0144
005F0179  48 8D 4B 02                     lea rcx, [rbx + 2]
005F017D  48 3B CD                        cmp rcx, rbp
005F0180  0F 83 8A 00 00 00               jae 0x1405f0210
005F0186  0F B7 03                        movzx eax, word ptr [rbx]
005F0189  66 89 07                        mov word ptr [rdi], ax
005F018C  0F B6 01                        movzx eax, byte ptr [rcx]
005F018F  88 47 02                        mov byte ptr [rdi + 2], al
005F0192  48 83 C7 03                     add rdi, 3
005F0196  48 83 C3 03                     add rbx, 3
005F019A  EB 29                           jmp 0x1405f01c5
005F019C  48 8D 43 01                     lea rax, [rbx + 1]
005F01A0  48 3B C5                        cmp rax, rbp
005F01A3  73 6B                           jae 0x1405f0210
005F01A5  0F B7 03                        movzx eax, word ptr [rbx]
005F01A8  66 89 07                        mov word ptr [rdi], ax
005F01AB  48 83 C7 02                     add rdi, 2
005F01AF  48 83 C3 02                     add rbx, 2
005F01B3  EB 10                           jmp 0x1405f01c5
005F01B5  48 3B DD                        cmp rbx, rbp
005F01B8  73 56                           jae 0x1405f0210
005F01BA  0F B6 03                        movzx eax, byte ptr [rbx]
005F01BD  88 07                           mov byte ptr [rdi], al
005F01BF  48 FF C7                        inc rdi
005F01C2  48 FF C3                        inc rbx
005F01C5  48 8B CB                        mov rcx, rbx
005F01C8  45 03 F6                        add r14d, r14d
005F01CB  0F 85 C1 FD FF FF               jne 0x1405eff92
005F01D1  48 8D 43 03                     lea rax, [rbx + 3]
005F01D5  48 3B C5                        cmp rax, rbp
005F01D8  73 36                           jae 0x1405f0210
005F01DA  8B 33                           mov esi, dword ptr [rbx]
005F01DC  E9 6F FD FF FF                  jmp 0x1405eff50
005F01E1  4C 8B 54 24 28                  mov r10, qword ptr [rsp + 0x28]
005F01E6  49 8D 04 3F                     lea rax, [r15 + rdi]
005F01EA  49 3B C2                        cmp rax, r10
005F01ED  77 21                           ja 0x1405f0210
005F01EF  4C 8B 4C 24 20                  mov r9, qword ptr [rsp + 0x20]
005F01F4  49 8B CF                        mov rcx, r15
005F01F7  4C 8B 9C 24 80 00 00 00         mov r11, qword ptr [rsp + 0x80]
005F01FF  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
005F0201  48 8B F8                        mov rdi, rax
005F0204  EB 33                           jmp 0x1405f0239
005F0206  4C 8B 54 24 28                  mov r10, qword ptr [rsp + 0x28]
005F020B  49 3B FA                        cmp rdi, r10
005F020E  73 29                           jae 0x1405f0239
005F0210  B8 42 02 00 C0                  mov eax, 0xc0000242
005F0215  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
005F021A  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
005F021E  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
005F0222  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
005F0226  49 8B E3                        mov rsp, r11
005F0229  41 5F                           pop r15
005F022B  41 5E                           pop r14
005F022D  41 5D                           pop r13
005F022F  41 5C                           pop r12
005F0231  5F                              pop rdi
005F0232  C3                              ret
005F0233  CC                              int3
005F0234  4C 8B 54 24 28                  mov r10, qword ptr [rsp + 0x28]
005F0239  45 85 F6                        test r14d, r14d
005F023C  78 05                           js 0x1405f0243
005F023E  45 03 F6                        add r14d, r14d
005F0241  EB 27                           jmp 0x1405f026a
005F0243  45 03 F6                        add r14d, r14d
005F0246  75 71                           jne 0x1405f02b9
005F0248  48 8D 43 03                     lea rax, [rbx + 3]
005F024C  48 3B C5                        cmp rax, rbp
005F024F  73 BF                           jae 0x1405f0210
005F0251  8B 33                           mov esi, dword ptr [rbx]
005F0253  48 83 C3 04                     add rbx, 4
005F0257  EB 05                           jmp 0x1405f025e
005F0259  4C 8B 54 24 28                  mov r10, qword ptr [rsp + 0x28]
005F025E  44 8D 34 75 01 00 00 00         lea r14d, [rsi*2 + 1]
005F0266  85 F6                           test esi, esi
005F0268  78 4F                           js 0x1405f02b9
005F026A  45 85 F6                        test r14d, r14d
005F026D  78 2B                           js 0x1405f029a
005F026F  45 03 F6                        add r14d, r14d
005F0272  48 8D 53 02                     lea rdx, [rbx + 2]
005F0276  48 3B D5                        cmp rdx, rbp
005F0279  77 95                           ja 0x1405f0210
005F027B  48 8D 4F 02                     lea rcx, [rdi + 2]
005F027F  49 3B CA                        cmp rcx, r10
005F0282  77 8C                           ja 0x1405f0210
005F0284  0F B7 03                        movzx eax, word ptr [rbx]
005F0287  48 8B DA                        mov rbx, rdx
005F028A  66 89 07                        mov word ptr [rdi], ax
005F028D  48 8B F9                        mov rdi, rcx
005F0290  45 85 F6                        test r14d, r14d
005F0293  78 AE                           js 0x1405f0243
005F0295  45 03 F6                        add r14d, r14d
005F0298  EB D0                           jmp 0x1405f026a
005F029A  48 3B DD                        cmp rbx, rbp
005F029D  0F 83 6D FF FF FF               jae 0x1405f0210
005F02A3  49 3B FA                        cmp rdi, r10
005F02A6  0F 83 64 FF FF FF               jae 0x1405f0210
005F02AC  0F B6 03                        movzx eax, byte ptr [rbx]
005F02AF  88 07                           mov byte ptr [rdi], al
005F02B1  48 FF C7                        inc rdi
005F02B4  48 FF C3                        inc rbx
005F02B7  EB 8A                           jmp 0x1405f0243
005F02B9  48 3B DD                        cmp rbx, rbp
005F02BC  0F 84 F5 00 00 00               je 0x1405f03b7
005F02C2  48 8D 43 01                     lea rax, [rbx + 1]
005F02C6  48 3B C5                        cmp rax, rbp
005F02C9  0F 83 DF 00 00 00               jae 0x1405f03ae
005F02CF  0F B7 13                        movzx edx, word ptr [rbx]
005F02D2  48 83 C3 02                     add rbx, 2
005F02D6  8B CA                           mov ecx, edx
005F02D8  48 C1 EA 03                     shr rdx, 3
005F02DC  48 FF C2                        inc rdx
005F02DF  83 E1 07                        and ecx, 7
005F02E2  48 83 F9 07                     cmp rcx, 7
005F02E6  0F 85 98 00 00 00               jne 0x1405f0384
005F02EC  4D 85 C9                        test r9, r9
005F02EF  75 18                           jne 0x1405f0309
005F02F1  48 3B DD                        cmp rbx, rbp
005F02F4  0F 83 16 FF FF FF               jae 0x1405f0210
005F02FA  4C 8B CB                        mov r9, rbx
005F02FD  48 FF C3                        inc rbx
005F0300  41 0F B6 09                     movzx ecx, byte ptr [r9]
005F0304  83 E1 0F                        and ecx, 0xf
005F0307  EB 0B                           jmp 0x1405f0314
005F0309  41 0F B6 09                     movzx ecx, byte ptr [r9]
005F030D  48 C1 E9 04                     shr rcx, 4
005F0311  45 33 C9                        xor r9d, r9d
005F0314  48 83 F9 0F                     cmp rcx, 0xf
005F0318  75 66                           jne 0x1405f0380
005F031A  48 3B DD                        cmp rbx, rbp
005F031D  0F 83 ED FE FF FF               jae 0x1405f0210
005F0323  0F B6 0B                        movzx ecx, byte ptr [rbx]
005F0326  48 FF C3                        inc rbx
005F0329  48 81 F9 FF 00 00 00            cmp rcx, 0xff
005F0330  75 4A                           jne 0x1405f037c
005F0332  48 8D 43 01                     lea rax, [rbx + 1]
005F0336  48 3B C5                        cmp rax, rbp
005F0339  0F 83 D1 FE FF FF               jae 0x1405f0210
005F033F  0F B7 0B                        movzx ecx, word ptr [rbx]
005F0342  48 83 C3 02                     add rbx, 2
005F0346  48 85 C9                        test rcx, rcx
005F0349  75 13                           jne 0x1405f035e
005F034B  48 8D 43 03                     lea rax, [rbx + 3]
005F034F  48 3B C5                        cmp rax, rbp
005F0352  0F 83 B8 FE FF FF               jae 0x1405f0210
005F0358  8B 0B                           mov ecx, dword ptr [rbx]
005F035A  48 83 C3 04                     add rbx, 4
005F035E  48 83 F9 16                     cmp rcx, 0x16
005F0362  0F 82 A8 FE FF FF               jb 0x1405f0210
005F0368  48 8D 47 03                     lea rax, [rdi + 3]
005F036C  48 03 C1                        add rax, rcx
005F036F  48 3B C7                        cmp rax, rdi
005F0372  0F 82 98 FE FF FF               jb 0x1405f0210
005F0378  48 83 E9 16                     sub rcx, 0x16
005F037C  48 83 C1 0F                     add rcx, 0xf
005F0380  48 83 C1 07                     add rcx, 7
005F0384  48 8B F7                        mov rsi, rdi
005F0387  48 83 C1 03                     add rcx, 3
005F038B  48 2B F2                        sub rsi, rdx
005F038E  49 3B F3                        cmp rsi, r11
005F0391  0F 82 79 FE FF FF               jb 0x1405f0210
005F0397  48 8D 04 39                     lea rax, [rcx + rdi]
005F039B  49 3B C2                        cmp rax, r10
005F039E  0F 87 6C FE FF FF               ja 0x1405f0210
005F03A4  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
005F03A6  48 8B F8                        mov rdi, rax
005F03A9  E9 8B FE FF FF                  jmp 0x1405f0239
005F03AE  49 3B FA                        cmp rdi, r10
005F03B1  0F 82 59 FE FF FF               jb 0x1405f0210
005F03B7  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
005F03BF  41 2B FB                        sub edi, r11d
005F03C2  89 38                           mov dword ptr [rax], edi
005F03C4  33 C0                           xor eax, eax
005F03C6  E9 4A FE FF FF                  jmp 0x1405f0215
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlDecompressBufferXpressLzProgress(__int64 a1, int a2, __int64 a3, int a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m34;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (80);
    v_stack_m34 = 0;
    if (a4 < 5) goto loc_005F0210;
    v_rbp = ((unsigned int)(a4)) + (a3);
    v_r10 = ((unsigned int)(a2)) + (a1);
    v_stack_m50 = v_r10;
    if (a6 == 0) goto loc_005EFCFE;
    v_rsi = (unsigned int)(0x1000ULL);
    if (a2 < ((unsigned int)((unsigned int)(0x1000ULL)))) {
        v_rsi = a2;
    }
    a3 = ((unsigned int)((unsigned int)(v_rsi))) + (a1);
    v_stack_m48 = a6;
    v_stack_m40 = a7;
    v_stack_m38 = (unsigned int)(v_rsi);
    if ((v_r10 - 368) < a3) { a3 = v_r10 - 368; }
    a4 = 0;
    v_stack_m58 = 0;
loc_005EFD2B:
    v_rbx = (a3) + (4);
    if (v_rbx >= (v_rbp - 86)) goto loc_005EFF50;
    if (a1 < a3) goto loc_005EFD6B;
    if (a1 >= (v_r10 - 368)) goto loc_005F0259;
    result = RtlpMakeXpressCallback(v_stack_m48, v_r10 - 368, a1, a4);
loc_005EFD6B:
    if (sign_flag) goto loc_005EFDCB;
loc_005EFD77:
    if (!sign_flag) goto loc_005EFD89;
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(v_rbx));
    v_rdi = (a1) + 1;
    v_rbx = (v_rbx) + 1;
    goto loc_005EFDC2;
loc_005EFD89:
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(a3)) * 2 + 1) + ((unsigned int)((unsigned int)(*(unsigned int *)(a3)) * 2 + 1)));
    if (!sign_flag) goto loc_005EFD9E;
    *(unsigned __int16 *)(v_rdi) = (unsigned __int16)(*(unsigned __int16 *)(v_rbx));
    v_rdi = (v_rdi) + (2);
    v_rbx = (v_rbx) + (2);
    goto loc_005EFDC2;
loc_005EFD9E:
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_r14)));
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx)));
    if (!sign_flag) goto loc_005EFDB1;
    v_rdi = (v_rdi) + (3);
    v_rbx = (v_rbx) + (3);
    goto loc_005EFDC2;
loc_005EFDB1:
    v_rdi = (v_rdi) + (4);
    v_rbx = (v_rbx) + (4);
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_r14)));
    if (!sign_flag) goto loc_005EFF48;
loc_005EFDC2:
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_r14)));
    if (condition_is_equal) goto loc_005EFD2B;
loc_005EFDCB:
    v_rbx = (v_rbx) + (2);
    a1 = (*(unsigned __int16 *)(v_rbx)) >> (3);
    a1 = (a1) + 1;
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx)))) & (7));
    if (v_r15 != 7) goto loc_005EFE6C;
    if (v_stack_m58 != 0) goto loc_005EFDFF;
    v_rbx = (v_rbx) + 1;
    v_r15 = (unsigned int)((*(unsigned __int8 *)(v_rbx)) & (15));
    goto loc_005EFE0A;
loc_005EFDFF:
    v_r15 = (*(unsigned __int8 *)(v_rbx)) >> (4);
    a4 = 0;
loc_005EFE0A:
    v_stack_m58 = 0;
    if (v_r15 != 15) goto loc_005EFE68;
    if ((v_rbx + 7) >= (v_rbp - 86)) goto loc_005EFFFB;
    v_rbx = (v_rbx) + 1;
    if ((*(unsigned __int8 *)(v_rbx)) != 255) goto loc_005EFE64;
    v_rbx = (v_rbx) + (2);
    v_r15 = *(unsigned __int16 *)(v_rbx);
    if (*(unsigned __int16 *)(v_rbx) == 0) {
        v_r15 = *(unsigned int *)(v_rbx);
        v_rbx = (v_rbx) + (4);
    }
    if (v_r15 < 22) goto loc_005F0210;
    result = (v_rdi + 3) + (v_r15);
    if (result < v_rdi) goto loc_005F0210;
    v_r15 = (v_r15) - (22);
loc_005EFE64:
    v_r15 = (v_r15) + (15);
loc_005EFE68:
    v_r15 = (v_r15) + (7);
loc_005EFE6C:
    v_rsi = (v_rdi) - (a1);
    v_r15 = (v_r15) + (3);
    if (v_rsi < v_stack_p8) goto loc_005F0210;
    if (a1 >= 4) goto loc_005EFEC8;
    *(unsigned __int8 *)(v_rdi) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi));
    a1 = (a1) - (1);
    if (condition_is_equal) goto loc_005EFEB0;
    *(unsigned __int8 *)(v_rdi + 1) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1));
    if (a1 == 1) goto loc_005EFEA6;
    goto loc_005EFEB9;
loc_005EFEA6:
    v_r15 = (v_r15) - (2);
    v_rdi = (v_rdi) + (2);
    goto loc_005EFEC3;
loc_005EFEB0:
    *(unsigned __int8 *)(v_rdi + 1) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi));
loc_005EFEB9:
    *(unsigned __int8 *)(v_rdi + 2) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi));
    v_rdi = (v_rdi) + (3);
loc_005EFEC3:
    if (v_r15 == 0) goto loc_005EFF3F;
loc_005EFEC8:
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)));
    *(unsigned int *)(v_rdi + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 4)));
    if (v_r15 < 9) goto loc_005EFF3C;
    v_rdi = (v_rdi) + (8);
    v_rsi = (v_rsi) + (8);
    v_r15 = (v_r15) - (8);
loc_005EFEE4:
    if (v_rdi < result) goto loc_005EFF05;
    if (v_rdi >= (v_r10 - 368)) goto loc_005F01E1;
    result = RtlpMakeXpressCallback(v_stack_m48, v_r10 - 368, v_rdi, a4);
loc_005EFF05:
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)));
    *(unsigned int *)(v_rdi + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 4)));
    *(unsigned int *)(v_rdi + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 8)));
    *(unsigned int *)(v_rdi + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 12)));
    if (v_r15 < 17) goto loc_005EFF2F;
    v_rdi = (v_rdi) + (16);
    v_rsi = (v_rsi) + (16);
    v_r15 = (v_r15) - (16);
    goto loc_005EFEE4;
loc_005EFF2F:
loc_005EFF3C:
    v_rdi = (v_rdi) + (v_r15);
loc_005EFF3F:
    if (sign_flag) goto loc_005EFDC2;
loc_005EFF48:
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_r14)));
    goto loc_005EFD77;
loc_005EFF50:
    if (v_rdi < result) goto loc_005EFF82;
    if (v_rdi >= (v_r10 - 368)) goto loc_005F0259;
    result = RtlpMakeXpressCallback(v_stack_m48, v_r10 - 368, v_rdi, v_stack_m58);
loc_005EFF82:
    if (!sign_flag) goto loc_005F0147;
loc_005EFF92:
    if ((v_stack_m48 + 4) == v_rbp) goto loc_005F0234;
    if ((v_stack_m48 + 4 + 1) >= v_rbp) goto loc_005F0206;
    v_rbx = (v_stack_m48 + 4) + (2);
    a1 = (*(unsigned __int16 *)(v_stack_m48 + 4)) >> (3);
    a1 = (a1) + 1;
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m48 + 4)))) & (7));
    if (v_r15 != 7) goto loc_005F0068;
    if (v_stack_m58 != 0) goto loc_005EFFE5;
    if (v_rbx >= v_rbp) goto loc_005F0210;
    v_rbx = (v_rbx) + 1;
    v_r15 = (unsigned int)((*(unsigned __int8 *)(v_rbx)) & (15));
    goto loc_005EFFF0;
loc_005EFFE5:
    v_r15 = (*(unsigned __int8 *)(v_rbx)) >> (4);
    a4 = 0;
loc_005EFFF0:
    v_stack_m58 = 0;
    if (v_r15 != 15) goto loc_005F0064;
loc_005EFFFB:
    if (v_rbx >= v_rbp) goto loc_005F0210;
    v_rbx = (v_rbx) + 1;
    if ((*(unsigned __int8 *)(v_rbx)) != 255) goto loc_005F0060;
    if ((v_rbx + 1) >= v_rbp) goto loc_005F0210;
    v_rbx = (v_rbx) + (2);
    if (*(unsigned __int16 *)(v_rbx) != 0) goto loc_005F0042;
    if ((v_rbx + 3) >= v_rbp) goto loc_005F0210;
    v_rbx = (v_rbx) + (4);
loc_005F0042:
    if (((unsigned int)(*(unsigned int *)(v_rbx))) < 22) goto loc_005F0210;
    result = (v_rdi + 3) + ((unsigned int)(*(unsigned int *)(v_rbx)));
    if (result < v_rdi) goto loc_005F0210;
    v_r15 = ((unsigned int)(*(unsigned int *)(v_rbx))) - (22);
loc_005F0060:
    v_r15 = (v_r15) + (15);
loc_005F0064:
    v_r15 = (v_r15) + (7);
loc_005F0068:
    v_rsi = (v_rdi) - (a1);
    v_r15 = (v_r15) + (3);
    if (v_rsi < v_stack_p8) goto loc_005F0210;
    if (a1 >= 4) goto loc_005F00C4;
    *(unsigned __int8 *)(v_rdi) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi));
    a1 = (a1) - (1);
    if (condition_is_equal) goto loc_005F00AC;
    *(unsigned __int8 *)(v_rdi + 1) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1));
    if (a1 == 1) goto loc_005F00A2;
    goto loc_005F00B5;
loc_005F00A2:
    v_r15 = (v_r15) - (2);
    v_rdi = (v_rdi) + (2);
    goto loc_005F00BF;
loc_005F00AC:
    *(unsigned __int8 *)(v_rdi + 1) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi));
loc_005F00B5:
    *(unsigned __int8 *)(v_rdi + 2) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi));
    v_rdi = (v_rdi) + (3);
loc_005F00BF:
    if (v_r15 == 0) goto loc_005F013B;
loc_005F00C4:
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)));
    *(unsigned int *)(v_rdi + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 4)));
    if (v_r15 < 9) goto loc_005F0138;
    v_rdi = (v_rdi) + (8);
    v_rsi = (v_rsi) + (8);
    v_r15 = (v_r15) - (8);
loc_005F00E0:
    if (v_rdi < result) goto loc_005F0101;
    if (v_rdi >= (v_r10 - 368)) goto loc_005F01E1;
    result = RtlpMakeXpressCallback(v_stack_m48, v_r10 - 368, v_rdi, a4);
loc_005F0101:
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi)));
    *(unsigned int *)(v_rdi + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 4)));
    *(unsigned int *)(v_rdi + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 8)));
    *(unsigned int *)(v_rdi + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 12)));
    if (v_r15 < 17) goto loc_005F012B;
    v_rdi = (v_rdi) + (16);
    v_rsi = (v_rsi) + (16);
    v_r15 = (v_r15) - (16);
    goto loc_005F00E0;
loc_005F012B:
loc_005F0138:
    v_rdi = (v_rdi) + (v_r15);
loc_005F013B:
    if (sign_flag) goto loc_005F01C5;
loc_005F0144:
    v_r14 = (unsigned int)((v_rsi * 2 + 1) + ((unsigned int)(v_rsi * 2 + 1)));
loc_005F0147:
    if (sign_flag) goto loc_005F01B5;
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_r14)));
    if (sign_flag) goto loc_005F019C;
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_r14)));
    if (sign_flag) goto loc_005F0179;
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_r14)));
    if ((v_rbx + 3) >= v_rbp) goto loc_005F0210;
    v_rbx = (v_rbx) + (4);
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx)));
    v_rdi = (v_rdi) + (4);
    if (sign_flag) goto loc_005F01C5;
    goto loc_005F0144;
loc_005F0179:
    if ((v_rbx + 2) >= v_rbp) goto loc_005F0210;
    *(unsigned __int16 *)(v_rdi) = (unsigned __int16)(*(unsigned __int16 *)(v_rbx));
    *(unsigned __int8 *)(v_rdi + 2) = (unsigned __int8)(*(unsigned __int8 *)(v_rbx + 2));
    v_rdi = (v_rdi) + (3);
    v_rbx = (v_rbx) + (3);
    goto loc_005F01C5;
loc_005F019C:
    if ((v_rbx + 1) >= v_rbp) goto loc_005F0210;
    *(unsigned __int16 *)(v_rdi) = (unsigned __int16)(*(unsigned __int16 *)(v_rbx));
    v_rdi = (v_rdi) + (2);
    v_rbx = (v_rbx) + (2);
    goto loc_005F01C5;
loc_005F01B5:
    if (v_rbx >= v_rbp) goto loc_005F0210;
    *(unsigned __int8 *)(v_rdi) = (unsigned __int8)(*(unsigned __int8 *)(v_rbx));
    v_rdi = (v_rdi) + 1;
    v_rbx = (v_rbx) + 1;
loc_005F01C5:
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_r14)));
    if (condition_is_not_equal) goto loc_005EFF92;
    if ((v_rbx + 3) >= v_rbp) goto loc_005F0210;
    goto loc_005EFF50;
loc_005F01E1:
    if ((v_r15 + v_rdi * 1) > v_stack_m50) goto loc_005F0210;
    goto loc_005F0239;
loc_005F0206:
    if ((v_r15 + v_rdi * 1) >= v_stack_m50) goto loc_005F0239;
loc_005F0210:
loc_005F0215:
    return (unsigned int)(0xC0000242ULL);
loc_005F0234:
loc_005F0239:
    if (sign_flag) goto loc_005F0243;
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_r14)));
    goto loc_005F026A;
loc_005F0243:
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_r14)));
    if (condition_is_not_equal) goto loc_005F02B9;
    if ((*(unsigned __int64 *)(v_stack_m28 + 56) + 3) >= (*(unsigned __int64 *)(v_stack_m28 + 64))) goto loc_005F0210;
    v_rbx = (*(unsigned __int64 *)(v_stack_m28 + 56)) + (4);
    goto loc_005F025E;
loc_005F0259:
loc_005F025E:
    if (sign_flag) goto loc_005F02B9;
loc_005F026A:
    if (sign_flag) goto loc_005F029A;
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56))) * 2 + 1) + ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56))) * 2 + 1)));
    if ((v_rbx + 2) > (*(unsigned __int64 *)(v_stack_m28 + 64))) goto loc_005F0210;
    if ((v_r15 + v_rdi * 1 + 2) > v_stack_m28) goto loc_005F0210;
    *(unsigned __int16 *)(v_r15 + v_rdi * 1) = (unsigned __int16)(*(unsigned __int16 *)(v_rbx));
    if (sign_flag) goto loc_005F0243;
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_r14)));
    goto loc_005F026A;
loc_005F029A:
    if ((v_rbx + 2) >= (*(unsigned __int64 *)(v_stack_m28 + 64))) goto loc_005F0210;
    if ((v_r15 + v_rdi * 1 + 2) >= v_stack_m28) goto loc_005F0210;
    *(unsigned __int8 *)(v_r15 + v_rdi * 1 + 2) = (unsigned __int8)(*(unsigned __int8 *)(v_rbx + 2));
    v_rdi = (v_r15 + v_rdi * 1 + 2) + 1;
    v_rbx = (v_rbx + 2) + 1;
    goto loc_005F0243;
loc_005F02B9:
    if (v_rbx == (*(unsigned __int64 *)(v_stack_m28 + 64))) goto loc_005F03B7;
    if ((v_rbx + 1) >= (*(unsigned __int64 *)(v_stack_m28 + 64))) goto loc_005F03AE;
    v_rbx = (v_rbx) + (2);
    a2 = (*(unsigned __int16 *)(v_rbx)) >> (3);
    a2 = (a2) + 1;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx)))) & (7));
    if (a1 != 7) goto loc_005F0384;
    if (v_stack_m58 != 0) goto loc_005F0309;
    if (v_rbx >= (*(unsigned __int64 *)(v_stack_m28 + 64))) goto loc_005F0210;
    v_rbx = (v_rbx) + 1;
    a1 = (unsigned int)((*(unsigned __int8 *)(v_rbx)) & (15));
    goto loc_005F0314;
loc_005F0309:
    a1 = (*(unsigned __int8 *)(v_rbx)) >> (4);
    a4 = 0;
loc_005F0314:
    if (a1 != 15) goto loc_005F0380;
    if (v_rbx >= (*(unsigned __int64 *)(v_stack_m28 + 64))) goto loc_005F0210;
    v_rbx = (v_rbx) + 1;
    if ((*(unsigned __int8 *)(v_rbx)) != 255) goto loc_005F037C;
    if ((v_rbx + 1) >= (*(unsigned __int64 *)(v_stack_m28 + 64))) goto loc_005F0210;
    v_rbx = (v_rbx) + (2);
    if (*(unsigned __int16 *)(v_rbx) != 0) goto loc_005F035E;
    if ((v_rbx + 3) >= (*(unsigned __int64 *)(v_stack_m28 + 64))) goto loc_005F0210;
    v_rbx = (v_rbx) + (4);
loc_005F035E:
    if (((unsigned int)(*(unsigned int *)(v_rbx))) < 22) goto loc_005F0210;
    result = (v_rdi + 3) + ((unsigned int)(*(unsigned int *)(v_rbx)));
    if (result < v_rdi) goto loc_005F0210;
    a1 = ((unsigned int)(*(unsigned int *)(v_rbx))) - (22);
loc_005F037C:
    a1 = (a1) + (15);
loc_005F0380:
    a1 = (a1) + (7);
loc_005F0384:
    a1 = (a1) + (3);
    v_rsi = (v_rdi) - (a2);
    if (v_rsi < v_stack_m28) goto loc_005F0210;
    if ((a1 + v_rdi * 1) > v_stack_m28) goto loc_005F0210;
    goto loc_005F0239;
loc_005F03AE:
    if ((a1 + v_rdi * 1) < v_stack_m28) goto loc_005F0210;
loc_005F03B7:
    v_rdi = (unsigned int)((a1 + v_rdi * 1) - ((unsigned int)(v_stack_m28)));
    *(unsigned int *)(a5) = (unsigned int)(v_rdi);
    result = 0;
    goto loc_005F0215;
}
```

## 5. (Beta) C Style

```c
int64_t RtlDecompressBufferXpressLzProgress(int64_t Arg1, void *Arg2, int64_t Arg3, int32_t Arg4, void *Arg5, int64_t Arg6, int64_t Arg7)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m34;
    uint32_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (80);
    v_stack_m34 = 0;
    if (Arg4 < 5) goto loc_005F0210;
    local_rbp = ((uint32_t)(Arg4)) + (Arg3);
    local_r10 = ((uint32_t)(Arg2)) + (Arg1);
    v_stack_m50 = local_r10;
    if (Arg6 == 0) goto loc_005EFCFE;
    local_rsi = (uint32_t)(0x1000ULL);
    if (Arg2 < ((uint32_t)((uint32_t)(0x1000ULL)))) {
        local_rsi = Arg2;
    }
    Arg3 = ((uint32_t)((uint32_t)(local_rsi))) + (Arg1);
    v_stack_m48 = Arg6;
    v_stack_m40 = Arg7;
    v_stack_m38 = (uint32_t)(local_rsi);
    if ((local_r10 - 368) < Arg3) { Arg3 = local_r10 - 368; }
    Arg4 = 0;
    v_stack_m58 = 0;
loc_005EFD2B:
    local_rbx = (Arg3) + (4);
    if (local_rbx >= (local_rbp - 86)) goto loc_005EFF50;
    if (Arg1 < Arg3) goto loc_005EFD6B;
    if (Arg1 >= (local_r10 - 368)) goto loc_005F0259;
    result = RtlpMakeXpressCallback(v_stack_m48, local_r10 - 368, Arg1, Arg4);
loc_005EFD6B:
    if (sign_flag) goto loc_005EFDCB;
loc_005EFD77:
    if (!sign_flag) goto loc_005EFD89;
    *(uint8_t *)(Arg1) = (uint8_t)(*(uint8_t *)(local_rbx));
    local_rdi = (Arg1) + 1;
    local_rbx = (local_rbx) + 1;
    goto loc_005EFDC2;
loc_005EFD89:
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3)) * 2 + 1) + ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)) * 2 + 1)));
    if (!sign_flag) goto loc_005EFD9E;
    *(uint16_t *)(local_rdi) = (uint16_t)(*(uint16_t *)(local_rbx));
    local_rdi = (local_rdi) + (2);
    local_rbx = (local_rbx) + (2);
    goto loc_005EFDC2;
loc_005EFD9E:
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(local_r14)));
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx)));
    if (!sign_flag) goto loc_005EFDB1;
    local_rdi = (local_rdi) + (3);
    local_rbx = (local_rbx) + (3);
    goto loc_005EFDC2;
loc_005EFDB1:
    local_rdi = (local_rdi) + (4);
    local_rbx = (local_rbx) + (4);
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(local_r14)));
    if (!sign_flag) goto loc_005EFF48;
loc_005EFDC2:
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(local_r14)));
    if (condition_is_equal) goto loc_005EFD2B;
loc_005EFDCB:
    local_rbx = (local_rbx) + (2);
    Arg1 = (*(uint16_t *)(local_rbx)) >> (3);
    Arg1 = (Arg1) + 1;
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rbx)))) & (7));
    if (local_r15 != 7) goto loc_005EFE6C;
    if (v_stack_m58 != 0) goto loc_005EFDFF;
    local_rbx = (local_rbx) + 1;
    local_r15 = (uint32_t)((*(uint8_t *)(local_rbx)) & (15));
    goto loc_005EFE0A;
loc_005EFDFF:
    local_r15 = (*(uint8_t *)(local_rbx)) >> (4);
    Arg4 = 0;
loc_005EFE0A:
    v_stack_m58 = 0;
    if (local_r15 != 15) goto loc_005EFE68;
    if ((local_rbx + 7) >= (local_rbp - 86)) goto loc_005EFFFB;
    local_rbx = (local_rbx) + 1;
    if ((*(uint8_t *)(local_rbx)) != 255) goto loc_005EFE64;
    local_rbx = (local_rbx) + (2);
    local_r15 = *(uint16_t *)(local_rbx);
    if (*(uint16_t *)(local_rbx) == 0) {
        local_r15 = *(uint32_t *)(local_rbx);
        local_rbx = (local_rbx) + (4);
    }
    if (local_r15 < 22) goto loc_005F0210;
    result = (local_rdi + 3) + (local_r15);
    if (result < local_rdi) goto loc_005F0210;
    local_r15 = (local_r15) - (22);
loc_005EFE64:
    local_r15 = (local_r15) + (15);
loc_005EFE68:
    local_r15 = (local_r15) + (7);
loc_005EFE6C:
    local_rsi = (local_rdi) - (Arg1);
    local_r15 = (local_r15) + (3);
    if (local_rsi < v_stack_p8) goto loc_005F0210;
    if (Arg1 >= 4) goto loc_005EFEC8;
    *(uint8_t *)(local_rdi) = (uint8_t)(*(uint8_t *)(local_rsi));
    Arg1 = (Arg1) - (1);
    if (condition_is_equal) goto loc_005EFEB0;
    *(uint8_t *)(local_rdi + 0x1) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1));
    if (Arg1 == 1) goto loc_005EFEA6;
    goto loc_005EFEB9;
loc_005EFEA6:
    local_r15 = (local_r15) - (2);
    local_rdi = (local_rdi) + (2);
    goto loc_005EFEC3;
loc_005EFEB0:
    *(uint8_t *)(local_rdi + 0x1) = (uint8_t)(*(uint8_t *)(local_rsi));
loc_005EFEB9:
    *(uint8_t *)(local_rdi + 0x2) = (uint8_t)(*(uint8_t *)(local_rsi));
    local_rdi = (local_rdi) + (3);
loc_005EFEC3:
    if (local_r15 == 0) goto loc_005EFF3F;
loc_005EFEC8:
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)));
    *(uint32_t *)(local_rdi + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x4)));
    if (local_r15 < 9) goto loc_005EFF3C;
    local_rdi = (local_rdi) + (8);
    local_rsi = (local_rsi) + (8);
    local_r15 = (local_r15) - (8);
loc_005EFEE4:
    if (local_rdi < result) goto loc_005EFF05;
    if (local_rdi >= (local_r10 - 368)) goto loc_005F01E1;
    result = RtlpMakeXpressCallback(v_stack_m48, local_r10 - 368, local_rdi, Arg4);
loc_005EFF05:
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)));
    *(uint32_t *)(local_rdi + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x4)));
    *(uint32_t *)(local_rdi + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x8)));
    *(uint32_t *)(local_rdi + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0xC)));
    if (local_r15 < 17) goto loc_005EFF2F;
    local_rdi = (local_rdi) + (16);
    local_rsi = (local_rsi) + (16);
    local_r15 = (local_r15) - (16);
    goto loc_005EFEE4;
loc_005EFF2F:
loc_005EFF3C:
    local_rdi = (local_rdi) + (local_r15);
loc_005EFF3F:
    if (sign_flag) goto loc_005EFDC2;
loc_005EFF48:
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(local_r14)));
    goto loc_005EFD77;
loc_005EFF50:
    if (local_rdi < result) goto loc_005EFF82;
    if (local_rdi >= (local_r10 - 368)) goto loc_005F0259;
    result = RtlpMakeXpressCallback(v_stack_m48, local_r10 - 368, local_rdi, v_stack_m58);
loc_005EFF82:
    if (!sign_flag) goto loc_005F0147;
loc_005EFF92:
    if ((v_stack_m48 + 4) == local_rbp) goto loc_005F0234;
    if ((v_stack_m48 + 4 + 1) >= local_rbp) goto loc_005F0206;
    local_rbx = (v_stack_m48 + 4) + (2);
    Arg1 = (*(uint16_t *)(v_stack_m48 + 0x4)) >> (3);
    Arg1 = (Arg1) + 1;
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m48 + 0x4)))) & (7));
    if (local_r15 != 7) goto loc_005F0068;
    if (v_stack_m58 != 0) goto loc_005EFFE5;
    if (local_rbx >= local_rbp) goto loc_005F0210;
    local_rbx = (local_rbx) + 1;
    local_r15 = (uint32_t)((*(uint8_t *)(local_rbx)) & (15));
    goto loc_005EFFF0;
loc_005EFFE5:
    local_r15 = (*(uint8_t *)(local_rbx)) >> (4);
    Arg4 = 0;
loc_005EFFF0:
    v_stack_m58 = 0;
    if (local_r15 != 15) goto loc_005F0064;
loc_005EFFFB:
    if (local_rbx >= local_rbp) goto loc_005F0210;
    local_rbx = (local_rbx) + 1;
    if ((*(uint8_t *)(local_rbx)) != 255) goto loc_005F0060;
    if ((local_rbx + 1) >= local_rbp) goto loc_005F0210;
    local_rbx = (local_rbx) + (2);
    if (*(uint16_t *)(local_rbx) != 0) goto loc_005F0042;
    if ((local_rbx + 3) >= local_rbp) goto loc_005F0210;
    local_rbx = (local_rbx) + (4);
loc_005F0042:
    if (((uint32_t)(*(uint32_t *)(local_rbx))) < 22) goto loc_005F0210;
    result = (local_rdi + 3) + ((uint32_t)(*(uint32_t *)(local_rbx)));
    if (result < local_rdi) goto loc_005F0210;
    local_r15 = ((uint32_t)(*(uint32_t *)(local_rbx))) - (22);
loc_005F0060:
    local_r15 = (local_r15) + (15);
loc_005F0064:
    local_r15 = (local_r15) + (7);
loc_005F0068:
    local_rsi = (local_rdi) - (Arg1);
    local_r15 = (local_r15) + (3);
    if (local_rsi < v_stack_p8) goto loc_005F0210;
    if (Arg1 >= 4) goto loc_005F00C4;
    *(uint8_t *)(local_rdi) = (uint8_t)(*(uint8_t *)(local_rsi));
    Arg1 = (Arg1) - (1);
    if (condition_is_equal) goto loc_005F00AC;
    *(uint8_t *)(local_rdi + 0x1) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1));
    if (Arg1 == 1) goto loc_005F00A2;
    goto loc_005F00B5;
loc_005F00A2:
    local_r15 = (local_r15) - (2);
    local_rdi = (local_rdi) + (2);
    goto loc_005F00BF;
loc_005F00AC:
    *(uint8_t *)(local_rdi + 0x1) = (uint8_t)(*(uint8_t *)(local_rsi));
loc_005F00B5:
    *(uint8_t *)(local_rdi + 0x2) = (uint8_t)(*(uint8_t *)(local_rsi));
    local_rdi = (local_rdi) + (3);
loc_005F00BF:
    if (local_r15 == 0) goto loc_005F013B;
loc_005F00C4:
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)));
    *(uint32_t *)(local_rdi + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x4)));
    if (local_r15 < 9) goto loc_005F0138;
    local_rdi = (local_rdi) + (8);
    local_rsi = (local_rsi) + (8);
    local_r15 = (local_r15) - (8);
loc_005F00E0:
    if (local_rdi < result) goto loc_005F0101;
    if (local_rdi >= (local_r10 - 368)) goto loc_005F01E1;
    result = RtlpMakeXpressCallback(v_stack_m48, local_r10 - 368, local_rdi, Arg4);
loc_005F0101:
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi)));
    *(uint32_t *)(local_rdi + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x4)));
    *(uint32_t *)(local_rdi + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x8)));
    *(uint32_t *)(local_rdi + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0xC)));
    if (local_r15 < 17) goto loc_005F012B;
    local_rdi = (local_rdi) + (16);
    local_rsi = (local_rsi) + (16);
    local_r15 = (local_r15) - (16);
    goto loc_005F00E0;
loc_005F012B:
loc_005F0138:
    local_rdi = (local_rdi) + (local_r15);
loc_005F013B:
    if (sign_flag) goto loc_005F01C5;
loc_005F0144:
    local_r14 = (uint32_t)((local_rsi * 2 + 1) + ((uint32_t)(local_rsi * 2 + 1)));
loc_005F0147:
    if (sign_flag) goto loc_005F01B5;
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(local_r14)));
    if (sign_flag) goto loc_005F019C;
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(local_r14)));
    if (sign_flag) goto loc_005F0179;
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(local_r14)));
    if ((local_rbx + 3) >= local_rbp) goto loc_005F0210;
    local_rbx = (local_rbx) + (4);
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx)));
    local_rdi = (local_rdi) + (4);
    if (sign_flag) goto loc_005F01C5;
    goto loc_005F0144;
loc_005F0179:
    if ((local_rbx + 2) >= local_rbp) goto loc_005F0210;
    *(uint16_t *)(local_rdi) = (uint16_t)(*(uint16_t *)(local_rbx));
    *(uint8_t *)(local_rdi + 0x2) = (uint8_t)(*(uint8_t *)(local_rbx + 0x2));
    local_rdi = (local_rdi) + (3);
    local_rbx = (local_rbx) + (3);
    goto loc_005F01C5;
loc_005F019C:
    if ((local_rbx + 1) >= local_rbp) goto loc_005F0210;
    *(uint16_t *)(local_rdi) = (uint16_t)(*(uint16_t *)(local_rbx));
    local_rdi = (local_rdi) + (2);
    local_rbx = (local_rbx) + (2);
    goto loc_005F01C5;
loc_005F01B5:
    if (local_rbx >= local_rbp) goto loc_005F0210;
    *(uint8_t *)(local_rdi) = (uint8_t)(*(uint8_t *)(local_rbx));
    local_rdi = (local_rdi) + 1;
    local_rbx = (local_rbx) + 1;
loc_005F01C5:
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(local_r14)));
    if (condition_is_not_equal) goto loc_005EFF92;
    if ((local_rbx + 3) >= local_rbp) goto loc_005F0210;
    goto loc_005EFF50;
loc_005F01E1:
    if ((local_r15 + local_rdi * 1) > v_stack_m50) goto loc_005F0210;
    goto loc_005F0239;
loc_005F0206:
    if ((local_r15 + local_rdi * 1) >= v_stack_m50) goto loc_005F0239;
loc_005F0210:
loc_005F0215:
    return (uint32_t)(0xC0000242ULL);
loc_005F0234:
loc_005F0239:
    if (sign_flag) goto loc_005F0243;
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(local_r14)));
    goto loc_005F026A;
loc_005F0243:
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(local_r14)));
    if (condition_is_not_equal) goto loc_005F02B9;
    if ((*(uint64_t *)(v_stack_m28 + 0x38) + 3) >= (*(uint64_t *)(v_stack_m28 + 0x40))) goto loc_005F0210;
    local_rbx = (*(uint64_t *)(v_stack_m28 + 0x38)) + (4);
    goto loc_005F025E;
loc_005F0259:
loc_005F025E:
    if (sign_flag) goto loc_005F02B9;
loc_005F026A:
    if (sign_flag) goto loc_005F029A;
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38))) * 2 + 1) + ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38))) * 2 + 1)));
    if ((local_rbx + 2) > (*(uint64_t *)(v_stack_m28 + 0x40))) goto loc_005F0210;
    if ((local_r15 + local_rdi * 1 + 2) > v_stack_m28) goto loc_005F0210;
    *(uint16_t *)(local_r15 + local_rdi * 1) = (uint16_t)(*(uint16_t *)(local_rbx));
    if (sign_flag) goto loc_005F0243;
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(local_r14)));
    goto loc_005F026A;
loc_005F029A:
    if ((local_rbx + 2) >= (*(uint64_t *)(v_stack_m28 + 0x40))) goto loc_005F0210;
    if ((local_r15 + local_rdi * 1 + 2) >= v_stack_m28) goto loc_005F0210;
    *(uint8_t *)(local_r15 + local_rdi * 1 + 0x2) = (uint8_t)(*(uint8_t *)(local_rbx + 0x2));
    local_rdi = (local_r15 + local_rdi * 1 + 2) + 1;
    local_rbx = (local_rbx + 2) + 1;
    goto loc_005F0243;
loc_005F02B9:
    if (local_rbx == (*(uint64_t *)(v_stack_m28 + 0x40))) goto loc_005F03B7;
    if ((local_rbx + 1) >= (*(uint64_t *)(v_stack_m28 + 0x40))) goto loc_005F03AE;
    local_rbx = (local_rbx) + (2);
    Arg2 = (*(uint16_t *)(local_rbx)) >> (3);
    Arg2 = (Arg2) + 1;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rbx)))) & (7));
    if (Arg1 != 7) goto loc_005F0384;
    if (v_stack_m58 != 0) goto loc_005F0309;
    if (local_rbx >= (*(uint64_t *)(v_stack_m28 + 0x40))) goto loc_005F0210;
    local_rbx = (local_rbx) + 1;
    Arg1 = (uint32_t)((*(uint8_t *)(local_rbx)) & (15));
    goto loc_005F0314;
loc_005F0309:
    Arg1 = (*(uint8_t *)(local_rbx)) >> (4);
    Arg4 = 0;
loc_005F0314:
    if (Arg1 != 15) goto loc_005F0380;
    if (local_rbx >= (*(uint64_t *)(v_stack_m28 + 0x40))) goto loc_005F0210;
    local_rbx = (local_rbx) + 1;
    if ((*(uint8_t *)(local_rbx)) != 255) goto loc_005F037C;
    if ((local_rbx + 1) >= (*(uint64_t *)(v_stack_m28 + 0x40))) goto loc_005F0210;
    local_rbx = (local_rbx) + (2);
    if (*(uint16_t *)(local_rbx) != 0) goto loc_005F035E;
    if ((local_rbx + 3) >= (*(uint64_t *)(v_stack_m28 + 0x40))) goto loc_005F0210;
    local_rbx = (local_rbx) + (4);
loc_005F035E:
    if (((uint32_t)(*(uint32_t *)(local_rbx))) < 22) goto loc_005F0210;
    result = (local_rdi + 3) + ((uint32_t)(*(uint32_t *)(local_rbx)));
    if (result < local_rdi) goto loc_005F0210;
    Arg1 = ((uint32_t)(*(uint32_t *)(local_rbx))) - (22);
loc_005F037C:
    Arg1 = (Arg1) + (15);
loc_005F0380:
    Arg1 = (Arg1) + (7);
loc_005F0384:
    Arg1 = (Arg1) + (3);
    local_rsi = (local_rdi) - (Arg2);
    if (local_rsi < v_stack_m28) goto loc_005F0210;
    if ((Arg1 + local_rdi * 1) > v_stack_m28) goto loc_005F0210;
    goto loc_005F0239;
loc_005F03AE:
    if ((Arg1 + local_rdi * 1) < v_stack_m28) goto loc_005F0210;
loc_005F03B7:
    local_rdi = (uint32_t)((Arg1 + local_rdi * 1) - ((uint32_t)(v_stack_m28)));
    *(uint32_t *)(arg5) = (uint32_t)(local_rdi);
    result = 0;
    goto loc_005F0215;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `- 0x170` | `64` | `R` |
| `Arg5` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005EFC90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
