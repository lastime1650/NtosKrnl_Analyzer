# sub_00BE8DF0

- RVA: `0x00BE8DF0`–`0x00BE9DE6` (길이 `4,086` bytes)
- VA: `0x0000000140BE8DF0`
- 실행 섹션: `INITKDBG`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2CBC`
- 디코드: `1,021`개 명령, `4,086/4,086` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00BE9110` → [sub_00BE8384](Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x00BE9415` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE95C2` → [sub_00BE8384](Unknown_function_00BE8384.md) (function, `0x00BE8384`)
- `0x00BE9BBC` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE9BCD` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE9DAE` → [KeGuardCheckICall](KeGuardCheckICall_function_00BEAA70.md) (function, `0x00BEAA70`)
- `0x00BE9DE0` → [SdbpCheckDll](SdbpCheckDll_function_00BEA7B0.md) (function, `0x00BEA7B0`)

### Direct callers
- [RtlpComputeEpilogueOffset](../../text/51/RtlpComputeEpilogueOffset_function_0051C81C.md) at `0x0051C8A1`

### Static image references
- `0x00BE9B25` → RVA `0x006BC8C0` (`$$10`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BE8DF0  48 8B C4                        mov rax, rsp
00BE8DF3  48 89 58 08                     mov qword ptr [rax + 8], rbx
00BE8DF7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00BE8DFB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00BE8DFF  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
00BE8E03  55                              push rbp
00BE8E04  41 54                           push r12
00BE8E06  41 55                           push r13
00BE8E08  41 56                           push r14
00BE8E0A  41 57                           push r15
00BE8E0C  48 8D 68 98                     lea rbp, [rax - 0x68]
00BE8E10  48 81 EC 40 01 00 00            sub rsp, 0x140
00BE8E17  8B 82 D8 09 00 00               mov eax, dword ptr [rdx + 0x9d8]
00BE8E1D  45 33 FF                        xor r15d, r15d
00BE8E20  B9 00 80 08 00                  mov ecx, 0x88000
00BE8E25  48 8B FA                        mov rdi, rdx
00BE8E28  23 C1                           and eax, ecx
00BE8E2A  45 8D 77 08                     lea r14d, [r15 + 8]
00BE8E2E  45 8D 67 01                     lea r12d, [r15 + 1]
00BE8E32  3B C1                           cmp eax, ecx
00BE8E34  0F 84 A5 00 00 00               je 0x140be8edf
00BE8E3A  48 8B 92 00 09 00 00            mov rdx, qword ptr [rdx + 0x900]
00BE8E41  45 8D 47 26                     lea r8d, [r15 + 0x26]
00BE8E45  48 8B C2                        mov rax, rdx
00BE8E48  B9 30 01 00 00                  mov ecx, 0x130
00BE8E4D  4C 89 38                        mov qword ptr [rax], r15
00BE8E50  83 C1 F8                        add ecx, -8
00BE8E53  49 03 C6                        add rax, r14
00BE8E56  4D 2B C4                        sub r8, r12
00BE8E59  75 F2                           jne 0x140be8e4d
00BE8E5B  85 C9                           test ecx, ecx
00BE8E5D  74 0B                           je 0x140be8e6a
00BE8E5F  44 88 38                        mov byte ptr [rax], r15b
00BE8E62  49 03 C4                        add rax, r12
00BE8E65  83 C1 FF                        add ecx, -1
00BE8E68  75 F5                           jne 0x140be8e5f
00BE8E6A  0F 10 87 68 08 00 00            movups xmm0, xmmword ptr [rdi + 0x868]
00BE8E71  B8 2F 01 00 00                  mov eax, 0x12f
00BE8E76  F3 0F 7F 42 10                  movdqu xmmword ptr [rdx + 0x10], xmm0
00BE8E7B  0F 10 8F 78 08 00 00            movups xmm1, xmmword ptr [rdi + 0x878]
00BE8E82  F3 0F 7F 4A 20                  movdqu xmmword ptr [rdx + 0x20], xmm1
00BE8E87  0F 10 87 88 08 00 00            movups xmm0, xmmword ptr [rdi + 0x888]
00BE8E8E  F3 0F 7F 82 20 01 00 00         movdqu xmmword ptr [rdx + 0x120], xmm0
00BE8E96  66 89 45 A0                     mov word ptr [rbp - 0x60], ax
00BE8E9A  48 8D 87 98 08 00 00            lea rax, [rdi + 0x898]
00BE8EA1  48 89 55 A2                     mov qword ptr [rbp - 0x5e], rdx
00BE8EA5  48 8B C8                        mov rcx, rax
00BE8EA8  48 C1 E9 10                     shr rcx, 0x10
00BE8EAC  66 89 42 10                     mov word ptr [rdx + 0x10], ax
00BE8EB0  48 C1 E8 20                     shr rax, 0x20
00BE8EB4  89 42 18                        mov dword ptr [rdx + 0x18], eax
00BE8EB7  66 89 4A 16                     mov word ptr [rdx + 0x16], cx
00BE8EBB  FA                              cli
00BE8EBC  F7 87 D8 09 00 00 00 00 00 40   test dword ptr [rdi + 0x9d8], 0x40000000
00BE8EC6  74 06                           je 0x140be8ece
00BE8EC8  41 0F 23 FF                     mov dr7, r15
00BE8ECC  EB 10                           jmp 0x140be8ede
00BE8ECE  0F 01 4D C8                     sidt [rbp - 0x38]
00BE8ED2  0F 01 5D A0                     lidt [rbp - 0x60]
00BE8ED6  41 0F 23 FF                     mov dr7, r15
00BE8EDA  0F 01 5D C8                     lidt [rbp - 0x38]
00BE8EDE  FB                              sti
00BE8EDF  81 87 48 08 00 00 30 06 00 00   add dword ptr [rdi + 0x848], 0x630
00BE8EE9  48 8D 8F 30 06 00 00            lea rcx, [rdi + 0x630]
00BE8EF0  8B B7 C4 00 00 00               mov esi, dword ptr [rdi + 0xc4]
00BE8EF6  4C 8B CF                        mov r9, rdi
00BE8EF9  44 8B 97 34 08 00 00            mov r10d, dword ptr [rdi + 0x834]
00BE8F00  48 8B C7                        mov rax, rdi
00BE8F03  4C 8B 9F 38 08 00 00            mov r11, qword ptr [rdi + 0x838]
00BE8F0A  41 BD 40 00 00 00               mov r13d, 0x40
00BE8F10  44 89 BF C4 00 00 00            mov dword ptr [rdi + 0xc4], r15d
00BE8F17  48 3B F9                        cmp rdi, rcx
00BE8F1A  73 0B                           jae 0x140be8f27
00BE8F1C  0F 18 00                        prefetchnta byte ptr [rax]
00BE8F1F  49 03 C5                        add rax, r13
00BE8F22  48 3B C1                        cmp rax, rcx
00BE8F25  72 F5                           jb 0x140be8f1c
00BE8F27  4D 8B C3                        mov r8, r11
00BE8F2A  BB 0C 00 00 00                  mov ebx, 0xc
00BE8F2F  49 BD 01 20 00 04 80 00 10 70   movabs r13, 0x7010008004002001
00BE8F39  49 8B C6                        mov rax, r14
00BE8F3C  4D 33 01                        xor r8, qword ptr [r9]
00BE8F3F  41 8B CA                        mov ecx, r10d
00BE8F42  4D 03 CE                        add r9, r14
00BE8F45  49 D3 C0                        rol r8, cl
00BE8F48  4D 33 01                        xor r8, qword ptr [r9]
00BE8F4B  4D 03 CE                        add r9, r14
00BE8F4E  49 D3 C0                        rol r8, cl
00BE8F51  49 2B C4                        sub rax, r12
00BE8F54  75 E6                           jne 0x140be8f3c
00BE8F56  49 8B C9                        mov rcx, r9
00BE8F59  48 2B CF                        sub rcx, rdi
00BE8F5C  49 33 CB                        xor rcx, r11
00BE8F5F  48 8B C1                        mov rax, rcx
00BE8F62  48 C1 C0 11                     rol rax, 0x11
00BE8F66  48 33 C8                        xor rcx, rax
00BE8F69  49 8B C5                        mov rax, r13
00BE8F6C  48 F7 E1                        mul rcx
00BE8F6F  48 89 55 D8                     mov qword ptr [rbp - 0x28], rdx
00BE8F73  33 D0                           xor edx, eax
00BE8F75  44 33 D2                        xor r10d, edx
00BE8F78  41 83 E2 3F                     and r10d, 0x3f
00BE8F7C  45 0F 44 D4                     cmove r10d, r12d
00BE8F80  83 C3 FF                        add ebx, -1
00BE8F83  75 B4                           jne 0x140be8f39
00BE8F85  8D 53 30                        lea edx, [rbx + 0x30]
00BE8F88  8D 43 06                        lea eax, [rbx + 6]
00BE8F8B  44 8D 6B 40                     lea r13d, [rbx + 0x40]
00BE8F8F  4D 33 01                        xor r8, qword ptr [r9]
00BE8F92  41 8B CA                        mov ecx, r10d
00BE8F95  49 D3 C0                        rol r8, cl
00BE8F98  4D 03 CE                        add r9, r14
00BE8F9B  83 C2 F8                        add edx, -8
00BE8F9E  49 2B C4                        sub rax, r12
00BE8FA1  75 EC                           jne 0x140be8f8f
00BE8FA3  85 D2                           test edx, edx
00BE8FA5  74 15                           je 0x140be8fbc
00BE8FA7  41 0F B6 01                     movzx eax, byte ptr [r9]
00BE8FAB  41 8B CA                        mov ecx, r10d
00BE8FAE  4C 33 C0                        xor r8, rax
00BE8FB1  4D 03 CC                        add r9, r12
00BE8FB4  49 D3 C0                        rol r8, cl
00BE8FB7  83 C2 FF                        add edx, -1
00BE8FBA  75 EB                           jne 0x140be8fa7
00BE8FBC  48 BA E8 B4 C8 91 58 3F A0 A3   movabs rdx, 0xa3a03f5891c8b4e8
00BE8FC6  89 B7 C4 00 00 00               mov dword ptr [rdi + 0xc4], esi
00BE8FCC  4C 39 87 68 0A 00 00            cmp qword ptr [rdi + 0xa68], r8
00BE8FD3  0F 84 3C 01 00 00               je 0x140be9115
00BE8FD9  48 8B 87 88 05 00 00            mov rax, qword ptr [rdi + 0x588]
00BE8FE0  8B 8F 04 08 00 00               mov ecx, dword ptr [rdi + 0x804]
00BE8FE6  48 89 38                        mov qword ptr [rax], rdi
00BE8FE9  89 48 10                        mov dword ptr [rax + 0x10], ecx
00BE8FEC  48 8B 87 68 0A 00 00            mov rax, qword ptr [rdi + 0xa68]
00BE8FF3  44 39 BF 18 09 00 00            cmp dword ptr [rdi + 0x918], r15d
00BE8FFA  0F 85 15 01 00 00               jne 0x140be9115
00BE9000  49 8B C8                        mov rcx, r8
00BE9003  48 33 C8                        xor rcx, rax
00BE9006  48 8B 87 88 05 00 00            mov rax, qword ptr [rdi + 0x588]
00BE900D  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
00BE9011  44 39 BF 18 09 00 00            cmp dword ptr [rdi + 0x918], r15d
00BE9018  0F 85 F7 00 00 00               jne 0x140be9115
00BE901E  8B 8F D8 09 00 00               mov ecx, dword ptr [rdi + 0x9d8]
00BE9024  48 8D 04 17                     lea rax, [rdi + rdx]
00BE9028  48 89 87 20 09 00 00            mov qword ptr [rdi + 0x920], rax
00BE902F  4C 89 BF 28 09 00 00            mov qword ptr [rdi + 0x928], r15
00BE9036  48 C7 87 30 09 00 00 09 01 00 00  mov qword ptr [rdi + 0x930], 0x109
00BE9041  4C 89 87 38 09 00 00            mov qword ptr [rdi + 0x938], r8
00BE9048  44 89 A7 18 09 00 00            mov dword ptr [rdi + 0x918], r12d
00BE904F  0F BA E1 1D                     bt ecx, 0x1d
00BE9053  0F 82 BC 00 00 00               jb 0x140be9115
00BE9059  F7 87 DC 09 00 00 00 00 20 00   test dword ptr [rdi + 0x9dc], 0x200000
00BE9063  0F 84 AC 00 00 00               je 0x140be9115
00BE9069  41 84 CC                        test r12b, cl
00BE906C  0F 84 A3 00 00 00               je 0x140be9115
00BE9072  8B 8F 74 0A 00 00               mov ecx, dword ptr [rdi + 0xa74]
00BE9078  8B 87 04 08 00 00               mov eax, dword ptr [rdi + 0x804]
00BE907E  4C 8B 97 38 08 00 00            mov r10, qword ptr [rdi + 0x838]
00BE9085  2B C1                           sub eax, ecx
00BE9087  4C 8B 87 78 0A 00 00            mov r8, qword ptr [rdi + 0xa78]
00BE908E  48 8D 14 39                     lea rdx, [rcx + rdi]
00BE9092  8B C8                           mov ecx, eax
00BE9094  48 C1 E9 03                     shr rcx, 3
00BE9098  4C 8D 0C CA                     lea r9, [rdx + rcx*8]
00BE909C  EB 20                           jmp 0x140be90be
00BE909E  4C 31 02                        xor qword ptr [rdx], r8
00BE90A1  48 8B 02                        mov rax, qword ptr [rdx]
00BE90A4  41 0F B6 C8                     movzx ecx, r8b
00BE90A8  49 33 C2                        xor rax, r10
00BE90AB  83 E1 3F                        and ecx, 0x3f
00BE90AE  49 D3 C8                        ror r8, cl
00BE90B1  4C 03 C0                        add r8, rax
00BE90B4  49 81 F0 FA 0E 00 00            xor r8, 0xefa
00BE90BB  49 03 D6                        add rdx, r14
00BE90BE  49 3B D1                        cmp rdx, r9
00BE90C1  75 DB                           jne 0x140be909e
00BE90C3  0F BA B7 DC 09 00 00 15         btr dword ptr [rdi + 0x9dc], 0x15
00BE90CB  4C 3B 87 80 0A 00 00            cmp r8, qword ptr [rdi + 0xa80]
00BE90D2  74 41                           je 0x140be9115
00BE90D4  8B 8F 04 08 00 00               mov ecx, dword ptr [rdi + 0x804]
00BE90DA  48 8B 87 88 05 00 00            mov rax, qword ptr [rdi + 0x588]
00BE90E1  48 89 38                        mov qword ptr [rax], rdi
00BE90E4  89 48 10                        mov dword ptr [rax + 0x10], ecx
00BE90E7  48 8B 8F 80 0A 00 00            mov rcx, qword ptr [rdi + 0xa80]
00BE90EE  44 39 BF 18 09 00 00            cmp dword ptr [rdi + 0x918], r15d
00BE90F5  75 0E                           jne 0x140be9105
00BE90F7  48 8B 87 88 05 00 00            mov rax, qword ptr [rdi + 0x588]
00BE90FE  49 33 C8                        xor rcx, r8
00BE9101  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
00BE9105  33 D2                           xor edx, edx
00BE9107  41 B9 00 01 00 00               mov r9d, 0x100
00BE910D  48 8B CF                        mov rcx, rdi
00BE9110  E8 6F F2 FF FF                  call 0x140be8384
00BE9115  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
00BE911A  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00BE911F  B9 04 00 00 00                  mov ecx, 4
00BE9124  44 88 38                        mov byte ptr [rax], r15b
00BE9127  49 03 C4                        add rax, r12
00BE912A  83 C1 FF                        add ecx, -1
00BE912D  75 F5                           jne 0x140be9124
00BE912F  41 8B CF                        mov ecx, r15d
00BE9132  BA 02 00 00 00                  mov edx, 2
00BE9137  41 BB 00 10 00 00               mov r11d, 0x1000
00BE913D  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00BE9141  44 39 BF 00 08 00 00            cmp dword ptr [rdi + 0x800], r15d
00BE9148  0F 86 AB 04 00 00               jbe 0x140be95f9
00BE914E  48 8B 87 C0 0A 00 00            mov rax, qword ptr [rdi + 0xac0]
00BE9155  4C 8B C7                        mov r8, rdi
00BE9158  48 85 C0                        test rax, rax
00BE915B  45 8B CF                        mov r9d, r15d
00BE915E  4C 0F 45 C0                     cmovne r8, rax
00BE9162  41 8B 98 28 08 00 00            mov ebx, dword ptr [r8 + 0x828]
00BE9169  49 03 D8                        add rbx, r8
00BE916C  44 39 7C 24 50                  cmp dword ptr [rsp + 0x50], r15d
00BE9171  74 12                           je 0x140be9185
00BE9173  39 4C 24 54                     cmp dword ptr [rsp + 0x54], ecx
00BE9177  77 0C                           ja 0x140be9185
00BE9179  8B 5C 24 58                     mov ebx, dword ptr [rsp + 0x58]
00BE917D  44 8B 4C 24 54                  mov r9d, dword ptr [rsp + 0x54]
00BE9182  49 03 D8                        add rbx, r8
00BE9185  44 3B C9                        cmp r9d, ecx
00BE9188  0F 84 F9 00 00 00               je 0x140be9287
00BE918E  44 8B D1                        mov r10d, ecx
00BE9191  49 BD AB AA AA AA AA AA AA AA   movabs r13, 0xaaaaaaaaaaaaaaab
00BE919B  45 2B D1                        sub r10d, r9d
00BE919E  44 8B C9                        mov r9d, ecx
00BE91A1  8B 0B                           mov ecx, dword ptr [rbx]
00BE91A3  83 E9 01                        sub ecx, 1
00BE91A6  0F 84 B2 00 00 00               je 0x140be925e
00BE91AC  83 E9 06                        sub ecx, 6
00BE91AF  0F 84 9C 00 00 00               je 0x140be9251
00BE91B5  83 E9 01                        sub ecx, 1
00BE91B8  0F 84 87 00 00 00               je 0x140be9245
00BE91BE  2B CA                           sub ecx, edx
00BE91C0  74 78                           je 0x140be923a
00BE91C2  83 E9 12                        sub ecx, 0x12
00BE91C5  74 6D                           je 0x140be9234
00BE91C7  2B CA                           sub ecx, edx
00BE91C9  74 3E                           je 0x140be9209
00BE91CB  83 E9 03                        sub ecx, 3
00BE91CE  74 13                           je 0x140be91e3
00BE91D0  83 F9 0A                        cmp ecx, 0xa
00BE91D3  0F 84 85 00 00 00               je 0x140be925e
00BE91D9  B8 30 00 00 00                  mov eax, 0x30
00BE91DE  E9 94 00 00 00                  jmp 0x140be9277
00BE91E3  8B 4B 20                        mov ecx, dword ptr [rbx + 0x20]
00BE91E6  8B 53 28                        mov edx, dword ptr [rbx + 0x28]
00BE91E9  81 E1 FF 0F 00 00               and ecx, 0xfff
00BE91EF  48 81 C2 FF 0F 00 00            add rdx, 0xfff
00BE91F6  48 03 D1                        add rdx, rcx
00BE91F9  48 C1 EA 0C                     shr rdx, 0xc
00BE91FD  8D 04 92                        lea eax, [rdx + rdx*4]
00BE9200  8D 04 85 30 00 00 00            lea eax, [rax*4 + 0x30]
00BE9207  EB 69                           jmp 0x140be9272
00BE9209  8B 43 24                        mov eax, dword ptr [rbx + 0x24]
00BE920C  8D 48 FF                        lea ecx, [rax - 1]
00BE920F  F7 D8                           neg eax
00BE9211  1B C0                           sbb eax, eax
00BE9213  23 C8                           and ecx, eax
00BE9215  49 8B C5                        mov rax, r13
00BE9218  48 F7 E1                        mul rcx
00BE921B  0F B7 43 28                     movzx eax, word ptr [rbx + 0x28]
00BE921F  48 C1 EA 03                     shr rdx, 3
00BE9223  83 C2 07                        add edx, 7
00BE9226  83 E2 F8                        and edx, 0xfffffff8
00BE9229  83 C0 02                        add eax, 2
00BE922C  8D 04 40                        lea eax, [rax + rax*2]
00BE922F  8D 04 C2                        lea eax, [rdx + rax*8]
00BE9232  EB 3E                           jmp 0x140be9272
00BE9234  0F B7 43 28                     movzx eax, word ptr [rbx + 0x28]
00BE9238  EB 0F                           jmp 0x140be9249
00BE923A  8B 43 1C                        mov eax, dword ptr [rbx + 0x1c]
00BE923D  83 C0 03                        add eax, 3
00BE9240  C1 E0 04                        shl eax, 4
00BE9243  EB 32                           jmp 0x140be9277
00BE9245  0F B7 43 20                     movzx eax, word ptr [rbx + 0x20]
00BE9249  83 C0 37                        add eax, 0x37
00BE924C  83 E0 F8                        and eax, 0xfffffff8
00BE924F  EB 26                           jmp 0x140be9277
00BE9251  8B 43 18                        mov eax, dword ptr [rbx + 0x18]
00BE9254  03 C2                           add eax, edx
00BE9256  8D 04 40                        lea eax, [rax + rax*2]
00BE9259  C1 E0 03                        shl eax, 3
00BE925C  EB 19                           jmp 0x140be9277
00BE925E  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
00BE9261  49 8B C5                        mov rax, r13
00BE9264  48 F7 E1                        mul rcx
00BE9267  48 C1 EA 03                     shr rdx, 3
00BE926B  8D 04 95 30 00 00 00            lea eax, [rdx*4 + 0x30]
00BE9272  BA 02 00 00 00                  mov edx, 2
00BE9277  48 03 D8                        add rbx, rax
00BE927A  4D 2B D4                        sub r10, r12
00BE927D  0F 85 1E FF FF FF               jne 0x140be91a1
00BE9283  45 8D 6A 40                     lea r13d, [r10 + 0x40]
00BE9287  4C 8B 5B 08                     mov r11, qword ptr [rbx + 8]
00BE928B  8B C3                           mov eax, ebx
00BE928D  44 8B B7 34 08 00 00            mov r14d, dword ptr [rdi + 0x834]
00BE9294  41 2B C0                        sub eax, r8d
00BE9297  44 8B 43 10                     mov r8d, dword ptr [rbx + 0x10]
00BE929B  44 01 87 48 08 00 00            add dword ptr [rdi + 0x848], r8d
00BE92A2  4C 8B BF 38 08 00 00            mov r15, qword ptr [rdi + 0x838]
00BE92A9  44 89 4C 24 54                  mov dword ptr [rsp + 0x54], r9d
00BE92AE  4D 8B CB                        mov r9, r11
00BE92B1  4B 8D 0C 03                     lea rcx, [r11 + r8]
00BE92B5  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00BE92B9  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
00BE92BE  49 8B C3                        mov rax, r11
00BE92C1  4C 3B D9                        cmp r11, rcx
00BE92C4  73 0B                           jae 0x140be92d1
00BE92C6  0F 18 00                        prefetchnta byte ptr [rax]
00BE92C9  49 03 C5                        add rax, r13
00BE92CC  48 3B C1                        cmp rax, rcx
00BE92CF  72 F5                           jb 0x140be92c6
00BE92D1  45 8B D0                        mov r10d, r8d
00BE92D4  49 8B F7                        mov rsi, r15
00BE92D7  41 C1 EA 07                     shr r10d, 7
00BE92DB  45 85 D2                        test r10d, r10d
00BE92DE  74 5C                           je 0x140be933c
00BE92E0  48 BF 01 20 00 04 80 00 10 70   movabs rdi, 0x7010008004002001
00BE92EA  B8 08 00 00 00                  mov eax, 8
00BE92EF  49 33 31                        xor rsi, qword ptr [r9]
00BE92F2  41 8B CE                        mov ecx, r14d
00BE92F5  48 D3 C6                        rol rsi, cl
00BE92F8  49 33 71 08                     xor rsi, qword ptr [r9 + 8]
00BE92FC  49 83 C1 10                     add r9, 0x10
00BE9300  48 D3 C6                        rol rsi, cl
00BE9303  49 2B C4                        sub rax, r12
00BE9306  75 E7                           jne 0x140be92ef
00BE9308  49 8B C9                        mov rcx, r9
00BE930B  49 2B CB                        sub rcx, r11
00BE930E  49 33 CF                        xor rcx, r15
00BE9311  48 8B C1                        mov rax, rcx
00BE9314  48 C1 C0 11                     rol rax, 0x11
00BE9318  48 33 C8                        xor rcx, rax
00BE931B  48 8B C7                        mov rax, rdi
00BE931E  48 F7 E1                        mul rcx
00BE9321  48 89 55 E0                     mov qword ptr [rbp - 0x20], rdx
00BE9325  33 D0                           xor edx, eax
00BE9327  44 33 F2                        xor r14d, edx
00BE932A  41 83 E6 3F                     and r14d, 0x3f
00BE932E  45 0F 44 F4                     cmove r14d, r12d
00BE9332  41 83 C2 FF                     add r10d, -1
00BE9336  75 B2                           jne 0x140be92ea
00BE9338  48 8B 7D 78                     mov rdi, qword ptr [rbp + 0x78]
00BE933C  41 83 E0 7F                     and r8d, 0x7f
00BE9340  41 83 F8 08                     cmp r8d, 8
00BE9344  72 1D                           jb 0x140be9363
00BE9346  41 8B C0                        mov eax, r8d
00BE9349  48 C1 E8 03                     shr rax, 3
00BE934D  49 33 31                        xor rsi, qword ptr [r9]
00BE9350  41 8B CE                        mov ecx, r14d
00BE9353  48 D3 C6                        rol rsi, cl
00BE9356  49 83 C1 08                     add r9, 8
00BE935A  41 83 C0 F8                     add r8d, -8
00BE935E  49 2B C4                        sub rax, r12
00BE9361  75 EA                           jne 0x140be934d
00BE9363  45 33 FF                        xor r15d, r15d
00BE9366  45 85 C0                        test r8d, r8d
00BE9369  74 16                           je 0x140be9381
00BE936B  41 0F B6 01                     movzx eax, byte ptr [r9]
00BE936F  41 8B CE                        mov ecx, r14d
00BE9372  48 33 F0                        xor rsi, rax
00BE9375  4D 03 CC                        add r9, r12
00BE9378  48 D3 C6                        rol rsi, cl
00BE937B  41 83 C0 FF                     add r8d, -1
00BE937F  75 EA                           jne 0x140be936b
00BE9381  48 8B C6                        mov rax, rsi
00BE9384  EB 02                           jmp 0x140be9388
00BE9386  33 F0                           xor esi, eax
00BE9388  48 C1 E8 1F                     shr rax, 0x1f
00BE938C  48 85 C0                        test rax, rax
00BE938F  75 F5                           jne 0x140be9386
00BE9391  0F BA F6 1F                     btr esi, 0x1f
00BE9395  45 8B E7                        mov r12d, r15d
00BE9398  3B 73 14                        cmp esi, dword ptr [rbx + 0x14]
00BE939B  0F 84 28 02 00 00               je 0x140be95c9
00BE93A1  44 39 3B                        cmp dword ptr [rbx], r15d
00BE93A4  75 0D                           jne 0x140be93b3
00BE93A6  44 39 7B 18                     cmp dword ptr [rbx + 0x18], r15d
00BE93AA  B8 01 00 00 00                  mov eax, 1
00BE93AF  44 0F 45 E0                     cmovne r12d, eax
00BE93B3  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
00BE93B6  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00BE93BA  48 85 C9                        test rcx, rcx
00BE93BD  0F 84 BF 00 00 00               je 0x140be9482
00BE93C3  8B 87 DC 09 00 00               mov eax, dword ptr [rdi + 0x9dc]
00BE93C9  41 84 C5                        test r13b, al
00BE93CC  0F 84 B0 00 00 00               je 0x140be9482
00BE93D2  45 0F 20 C5                     mov r13, cr8
00BE93D6  41 BB 02 00 00 00               mov r11d, 2
00BE93DC  45 0F 22 C3                     mov cr8, r11
00BE93E0  4C 8B FA                        mov r15, rdx
00BE93E3  48 8D 41 FF                     lea rax, [rcx - 1]
00BE93E7  49 81 E7 00 F0 FF FF            and r15, 0xfffffffffffff000
00BE93EE  48 03 C2                        add rax, rdx
00BE93F1  48 0D FF 0F 00 00               or rax, 0xfff
00BE93F7  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00BE93FC  49 8D 47 FF                     lea rax, [r15 - 1]
00BE9400  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00BE9405  45 0F B6 F5                     movzx r14d, r13b
00BE9409  48 8B 87 68 04 00 00            mov rax, qword ptr [rdi + 0x468]
00BE9410  33 D2                           xor edx, edx
00BE9412  49 8B CF                        mov rcx, r15
00BE9415  E8 46 16 00 00                  call 0x140beaa60
00BE941A  3D 2D 02 00 C0                  cmp eax, 0xc000022d
00BE941F  75 29                           jne 0x140be944a
00BE9421  45 85 E4                        test r12d, r12d
00BE9424  75 55                           jne 0x140be947b
00BE9426  41 8D 44 24 01                  lea eax, [r12 + 1]
00BE942B  44 3A E8                        cmp r13b, al
00BE942E  77 1E                           ja 0x140be944e
00BE9430  45 0F B6 F5                     movzx r14d, r13b
00BE9434  45 0F 22 C6                     mov cr8, r14
00BE9438  41 8A 07                        mov al, byte ptr [r15]
00BE943B  44 0F 20 C0                     mov rax, cr8
00BE943F  41 8D 44 24 02                  lea eax, [r12 + 2]
00BE9444  44 0F 22 C0                     mov cr8, rax
00BE9448  EB BF                           jmp 0x140be9409
00BE944A  85 C0                           test eax, eax
00BE944C  78 2D                           js 0x140be947b
00BE944E  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00BE9453  41 BB 00 10 00 00               mov r11d, 0x1000
00BE9459  49 03 C3                        add rax, r11
00BE945C  4D 03 FB                        add r15, r11
00BE945F  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00BE9464  48 3B 44 24 60                  cmp rax, qword ptr [rsp + 0x60]
00BE9469  75 9A                           jne 0x140be9405
00BE946B  45 0F 22 C6                     mov cr8, r14
00BE946F  45 33 FF                        xor r15d, r15d
00BE9472  45 8D 67 01                     lea r12d, [r15 + 1]
00BE9476  E9 5A 01 00 00                  jmp 0x140be95d5
00BE947B  45 33 FF                        xor r15d, r15d
00BE947E  45 0F 22 C6                     mov cr8, r14
00BE9482  4C 8B CF                        mov r9, rdi
00BE9485  8B 43 14                        mov eax, dword ptr [rbx + 0x14]
00BE9488  41 BA DC 09 00 00               mov r10d, 0x9dc
00BE948E  44 39 BF 18 09 00 00            cmp dword ptr [rdi + 0x918], r15d
00BE9495  75 10                           jne 0x140be94a7
00BE9497  8B CE                           mov ecx, esi
00BE9499  48 33 C8                        xor rcx, rax
00BE949C  48 8B 87 88 05 00 00            mov rax, qword ptr [rdi + 0x588]
00BE94A3  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
00BE94A7  41 BC 01 00 00 00               mov r12d, 1
00BE94AD  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00BE94B1  44 39 BF 18 09 00 00            cmp dword ptr [rdi + 0x918], r15d
00BE94B8  0F 85 11 01 00 00               jne 0x140be95cf
00BE94BE  48 B8 E8 B4 C8 91 58 3F A0 A3   movabs rax, 0xa3a03f5891c8b4e8
00BE94C8  48 03 C7                        add rax, rdi
00BE94CB  48 89 87 20 09 00 00            mov qword ptr [rdi + 0x920], rax
00BE94D2  48 B8 15 34 45 E4 DE 4B B7 B3   movabs rax, 0xb3b74bdee4453415
00BE94DC  48 03 C3                        add rax, rbx
00BE94DF  48 89 87 28 09 00 00            mov qword ptr [rdi + 0x928], rax
00BE94E6  48 63 03                        movsxd rax, dword ptr [rbx]
00BE94E9  48 89 8F 38 09 00 00            mov qword ptr [rdi + 0x938], rcx
00BE94F0  8B 8F D8 09 00 00               mov ecx, dword ptr [rdi + 0x9d8]
00BE94F6  48 89 87 30 09 00 00            mov qword ptr [rdi + 0x930], rax
00BE94FD  44 89 A7 18 09 00 00            mov dword ptr [rdi + 0x918], r12d
00BE9504  0F BA E1 1D                     bt ecx, 0x1d
00BE9508  0F 82 C1 00 00 00               jb 0x140be95cf
00BE950E  43 F7 04 11 00 00 20 00         test dword ptr [r9 + r10], 0x200000
00BE9516  0F 84 B3 00 00 00               je 0x140be95cf
00BE951C  41 84 CC                        test r12b, cl
00BE951F  0F 84 AA 00 00 00               je 0x140be95cf
00BE9525  8B 8F 74 0A 00 00               mov ecx, dword ptr [rdi + 0xa74]
00BE952B  8B 87 04 08 00 00               mov eax, dword ptr [rdi + 0x804]
00BE9531  48 8B 9F 38 08 00 00            mov rbx, qword ptr [rdi + 0x838]
00BE9538  2B C1                           sub eax, ecx
00BE953A  4C 8B 87 78 0A 00 00            mov r8, qword ptr [rdi + 0xa78]
00BE9541  48 8D 14 39                     lea rdx, [rcx + rdi]
00BE9545  8B C8                           mov ecx, eax
00BE9547  48 C1 E9 03                     shr rcx, 3
00BE954B  4C 8D 1C CA                     lea r11, [rdx + rcx*8]
00BE954F  EB 21                           jmp 0x140be9572
00BE9551  4C 31 02                        xor qword ptr [rdx], r8
00BE9554  48 8B 02                        mov rax, qword ptr [rdx]
00BE9557  41 0F B6 C8                     movzx ecx, r8b
00BE955B  48 33 C3                        xor rax, rbx
00BE955E  83 E1 3F                        and ecx, 0x3f
00BE9561  49 D3 C8                        ror r8, cl
00BE9564  4C 03 C0                        add r8, rax
00BE9567  49 81 F0 FA 0E 00 00            xor r8, 0xefa
00BE956E  48 83 C2 08                     add rdx, 8
00BE9572  49 3B D3                        cmp rdx, r11
00BE9575  75 DA                           jne 0x140be9551
00BE9577  43 0F BA 34 11 15               btr dword ptr [r9 + r10], 0x15
00BE957D  4C 3B 87 80 0A 00 00            cmp r8, qword ptr [rdi + 0xa80]
00BE9584  74 49                           je 0x140be95cf
00BE9586  8B 8F 04 08 00 00               mov ecx, dword ptr [rdi + 0x804]
00BE958C  48 8B 87 88 05 00 00            mov rax, qword ptr [rdi + 0x588]
00BE9593  48 89 38                        mov qword ptr [rax], rdi
00BE9596  89 48 10                        mov dword ptr [rax + 0x10], ecx
00BE9599  48 8B 8F 80 0A 00 00            mov rcx, qword ptr [rdi + 0xa80]
00BE95A0  44 39 BF 18 09 00 00            cmp dword ptr [rdi + 0x918], r15d
00BE95A7  75 0E                           jne 0x140be95b7
00BE95A9  48 8B 87 88 05 00 00            mov rax, qword ptr [rdi + 0x588]
00BE95B0  49 33 C8                        xor rcx, r8
00BE95B3  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
00BE95B7  33 D2                           xor edx, edx
00BE95B9  41 B9 00 01 00 00               mov r9d, 0x100
00BE95BF  48 8B CF                        mov rcx, rdi
00BE95C2  E8 BD ED FF FF                  call 0x140be8384
00BE95C7  EB 06                           jmp 0x140be95cf
00BE95C9  41 BC 01 00 00 00               mov r12d, 1
00BE95CF  41 BB 00 10 00 00               mov r11d, 0x1000
00BE95D5  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
00BE95D9  BA 02 00 00 00                  mov edx, 2
00BE95DE  41 03 CC                        add ecx, r12d
00BE95E1  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00BE95E5  44 8D 6A 3E                     lea r13d, [rdx + 0x3e]
00BE95E9  3B 8F 00 08 00 00               cmp ecx, dword ptr [rdi + 0x800]
00BE95EF  0F 82 59 FB FF FF               jb 0x140be914e
00BE95F5  44 8D 72 06                     lea r14d, [rdx + 6]
00BE95F9  44 39 BF 18 09 00 00            cmp dword ptr [rdi + 0x918], r15d
00BE9600  0F 84 D9 04 00 00               je 0x140be9adf
00BE9606  48 8B B7 30 09 00 00            mov rsi, qword ptr [rdi + 0x930]
00BE960D  4C 8B B7 38 09 00 00            mov r14, qword ptr [rdi + 0x938]
00BE9614  4C 8B BF 28 09 00 00            mov r15, qword ptr [rdi + 0x928]
00BE961B  4C 8B A7 20 09 00 00            mov r12, qword ptr [rdi + 0x920]
00BE9622  48 89 75 90                     mov qword ptr [rbp - 0x70], rsi
00BE9626  4C 89 75 98                     mov qword ptr [rbp - 0x68], r14
00BE962A  4C 89 7D C0                     mov qword ptr [rbp - 0x40], r15
00BE962E  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
00BE9633  44 0F 20 C0                     mov rax, cr8
00BE9637  3A C2                           cmp al, dl
00BE9639  73 08                           jae 0x140be9643
00BE963B  44 0F 20 C0                     mov rax, cr8
00BE963F  44 0F 22 C2                     mov cr8, rdx
00BE9643  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
00BE964C  48 8B 87 40 06 00 00            mov rax, qword ptr [rdi + 0x640]
00BE9653  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00BE965C  4D 8B 0C 00                     mov r9, qword ptr [r8 + rax]
00BE9660  48 8B 87 48 06 00 00            mov rax, qword ptr [rdi + 0x648]
00BE9667  4C 89 4C 24 48                  mov qword ptr [rsp + 0x48], r9
00BE966C  4A 8B 14 00                     mov rdx, qword ptr [rax + r8]
00BE9670  48 8B 87 58 06 00 00            mov rax, qword ptr [rdi + 0x658]
00BE9677  48 03 97 88 07 00 00            add rdx, qword ptr [rdi + 0x788]
00BE967E  48 8B 1C 01                     mov rbx, qword ptr [rcx + rax]
00BE9682  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00BE9687  48 89 5D B8                     mov qword ptr [rbp - 0x48], rbx
00BE968B  49 3B C1                        cmp rax, r9
00BE968E  77 16                           ja 0x140be96a6
00BE9690  8B 87 FC 05 00 00               mov eax, dword ptr [rdi + 0x5fc]
00BE9696  49 8B C9                        mov rcx, r9
00BE9699  48 2B C8                        sub rcx, rax
00BE969C  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00BE96A1  48 3B C1                        cmp rax, rcx
00BE96A4  73 45                           jae 0x140be96eb
00BE96A6  48 8B 87 50 06 00 00            mov rax, qword ptr [rdi + 0x650]
00BE96AD  41 80 3C 00 00                  cmp byte ptr [r8 + rax], 0
00BE96B2  74 27                           je 0x140be96db
00BE96B4  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00BE96B9  48 3B C2                        cmp rax, rdx
00BE96BC  77 1D                           ja 0x140be96db
00BE96BE  8B 87 F8 05 00 00               mov eax, dword ptr [rdi + 0x5f8]
00BE96C4  48 8B CA                        mov rcx, rdx
00BE96C7  48 2B C8                        sub rcx, rax
00BE96CA  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00BE96CF  48 3B C1                        cmp rax, rcx
00BE96D2  72 07                           jb 0x140be96db
00BE96D4  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
00BE96D9  EB 10                           jmp 0x140be96eb
00BE96DB  48 8B 87 88 06 00 00            mov rax, qword ptr [rdi + 0x688]
00BE96E2  48 8B 04 03                     mov rax, qword ptr [rbx + rax]
00BE96E6  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00BE96EB  F7 87 D8 09 00 00 00 00 00 04   test dword ptr [rdi + 0x9d8], 0x4000000
00BE96F5  0F 85 A8 05 00 00               jne 0x140be9ca3
00BE96FB  48 83 65 88 00                  and qword ptr [rbp - 0x78], 0
00BE9700  F7 87 DC 09 00 00 00 00 40 00   test dword ptr [rdi + 0x9dc], 0x400000
00BE970A  75 12                           jne 0x140be971e
00BE970C  0F 20 C1                        mov rcx, cr0
00BE970F  48 8B C1                        mov rax, rcx
00BE9712  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
00BE9716  48 0F BA F0 10                  btr rax, 0x10
00BE971B  0F 22 C0                        mov cr0, rax
00BE971E  44 8B A7 E8 0A 00 00            mov r12d, dword ptr [rdi + 0xae8]
00BE9725  4C 8D B7 F0 0A 00 00            lea r14, [rdi + 0xaf0]
00BE972C  49 C1 E4 04                     shl r12, 4
00BE9730  33 D2                           xor edx, edx
00BE9732  4D 03 E6                        add r12, r14
00BE9735  49 8B F4                        mov rsi, r12
00BE9738  4C 89 65 B0                     mov qword ptr [rbp - 0x50], r12
00BE973C  44 8D 52 01                     lea r10d, [rdx + 1]
00BE9740  39 97 EC 0A 00 00               cmp dword ptr [rdi + 0xaec], edx
00BE9746  76 3B                           jbe 0x140be9783
00BE9748  48 8B 0E                        mov rcx, qword ptr [rsi]
00BE974B  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00BE974F  48 89 01                        mov qword ptr [rcx], rax
00BE9752  0F 20 E1                        mov rcx, cr4
00BE9755  48 F7 C1 80 00 02 00            test rcx, 0x20080
00BE975C  74 10                           je 0x140be976e
00BE975E  48 8B C1                        mov rax, rcx
00BE9761  48 0F BA F8 07                  btc rax, 7
00BE9766  0F 22 E0                        mov cr4, rax
00BE9769  0F 22 E1                        mov cr4, rcx
00BE976C  EB 06                           jmp 0x140be9774
00BE976E  0F 20 D8                        mov rax, cr3
00BE9771  0F 22 D8                        mov cr3, rax
00BE9774  48 83 C6 10                     add rsi, 0x10
00BE9778  41 03 D2                        add edx, r10d
00BE977B  3B 97 EC 0A 00 00               cmp edx, dword ptr [rdi + 0xaec]
00BE9781  72 C5                           jb 0x140be9748
00BE9783  48 B9 F8 FF FF FF 7F 00 00 00   movabs rcx, 0x7ffffffff8
00BE978D  4D 3B F4                        cmp r14, r12
00BE9790  0F 83 03 02 00 00               jae 0x140be9999
00BE9796  F7 87 DC 09 00 00 00 00 40 00   test dword ptr [rdi + 0x9dc], 0x400000
00BE97A0  45 8B 6E 08                     mov r13d, dword ptr [r14 + 8]
00BE97A4  4D 8B 06                        mov r8, qword ptr [r14]
00BE97A7  44 89 6C 24 68                  mov dword ptr [rsp + 0x68], r13d
00BE97AC  75 47                           jne 0x140be97f5
00BE97AE  41 8B D5                        mov edx, r13d
00BE97B1  48 8B CE                        mov rcx, rsi
00BE97B4  41 83 FD 08                     cmp r13d, 8
00BE97B8  72 1D                           jb 0x140be97d7
00BE97BA  45 8B CD                        mov r9d, r13d
00BE97BD  49 C1 E9 03                     shr r9, 3
00BE97C1  48 8B 01                        mov rax, qword ptr [rcx]
00BE97C4  83 C2 F8                        add edx, -8
00BE97C7  49 89 00                        mov qword ptr [r8], rax
00BE97CA  48 83 C1 08                     add rcx, 8
00BE97CE  49 83 C0 08                     add r8, 8
00BE97D2  4D 2B CA                        sub r9, r10
00BE97D5  75 EA                           jne 0x140be97c1
00BE97D7  85 D2                           test edx, edx
00BE97D9  0F 84 8F 01 00 00               je 0x140be996e
00BE97DF  4C 2B C1                        sub r8, rcx
00BE97E2  8A 01                           mov al, byte ptr [rcx]
00BE97E4  42 88 04 01                     mov byte ptr [rcx + r8], al
00BE97E8  49 03 CA                        add rcx, r10
00BE97EB  83 C2 FF                        add edx, -1
00BE97EE  75 F2                           jne 0x140be97e2
00BE97F0  E9 79 01 00 00                  jmp 0x140be996e
00BE97F5  49 8B C8                        mov rcx, r8
00BE97F8  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
00BE97FD  81 E1 FF 0F 00 00               and ecx, 0xfff
00BE9803  49 8D 95 FF 0F 00 00            lea rdx, [r13 + 0xfff]
00BE980A  48 03 D1                        add rdx, rcx
00BE980D  41 8B DD                        mov ebx, r13d
00BE9810  48 C1 EA 0C                     shr rdx, 0xc
00BE9814  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00BE9818  85 D2                           test edx, edx
00BE981A  0F 84 4E 01 00 00               je 0x140be996e
00BE9820  8B C2                           mov eax, edx
00BE9822  41 BC 04 00 00 00               mov r12d, 4
00BE9828  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00BE982C  49 BD F8 FF FF FF 7F 00 00 00   movabs r13, 0x7ffffffff8
00BE9836  4C 8B 97 D8 05 00 00            mov r10, qword ptr [rdi + 0x5d8]
00BE983D  48 8D 4D F8                     lea rcx, [rbp - 8]
00BE9841  49 8B C0                        mov rax, r8
00BE9844  49 8B D4                        mov rdx, r12
00BE9847  48 C1 E8 09                     shr rax, 9
00BE984B  45 8B CC                        mov r9d, r12d
00BE984E  49 23 C5                        and rax, r13
00BE9851  41 BF 01 00 00 00               mov r15d, 1
00BE9857  49 03 C2                        add rax, r10
00BE985A  48 89 01                        mov qword ptr [rcx], rax
00BE985D  48 8D 49 08                     lea rcx, [rcx + 8]
00BE9861  48 C1 E8 09                     shr rax, 9
00BE9865  49 23 C5                        and rax, r13
00BE9868  49 03 C2                        add rax, r10
00BE986B  49 2B D7                        sub rdx, r15
00BE986E  75 EA                           jne 0x140be985a
00BE9870  41 83 C1 FF                     add r9d, -1
00BE9874  74 0F                           je 0x140be9885
00BE9876  4A 8B 44 CD F8                  mov rax, qword ptr [rbp + r9*8 - 8]
00BE987B  8B 08                           mov ecx, dword ptr [rax]
00BE987D  C0 E9 07                        shr cl, 7
00BE9880  41 84 CF                        test r15b, cl
00BE9883  74 EB                           je 0x140be9870
00BE9885  4E 8B 7C CD F8                  mov r15, qword ptr [rbp + r9*8 - 8]
00BE988A  49 8B 07                        mov rax, qword ptr [r15]
00BE988D  48 83 C8 62                     or rax, 0x62
00BE9891  49 89 07                        mov qword ptr [r15], rax
00BE9894  0F 20 E2                        mov rdx, cr4
00BE9897  48 F7 C2 80 00 02 00            test rdx, 0x20080
00BE989E  74 10                           je 0x140be98b0
00BE98A0  48 8B CA                        mov rcx, rdx
00BE98A3  48 0F BA F9 07                  btc rcx, 7
00BE98A8  0F 22 E1                        mov cr4, rcx
00BE98AB  0F 22 E2                        mov cr4, rdx
00BE98AE  EB 06                           jmp 0x140be98b6
00BE98B0  0F 20 D9                        mov rcx, cr3
00BE98B3  0F 22 D9                        mov cr3, rcx
00BE98B6  41 8B D3                        mov edx, r11d
00BE98B9  41 8B C8                        mov ecx, r8d
00BE98BC  81 E1 FF 0F 00 00               and ecx, 0xfff
00BE98C2  44 8B D3                        mov r10d, ebx
00BE98C5  2B D1                           sub edx, ecx
00BE98C7  4D 8B C8                        mov r9, r8
00BE98CA  3B D3                           cmp edx, ebx
00BE98CC  44 0F 42 D2                     cmovb r10d, edx
00BE98D0  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
00BE98D5  45 8B DA                        mov r11d, r10d
00BE98D8  41 83 FA 08                     cmp r10d, 8
00BE98DC  72 23                           jb 0x140be9901
00BE98DE  41 8B DA                        mov ebx, r10d
00BE98E1  48 C1 EB 03                     shr rbx, 3
00BE98E5  48 8B 0A                        mov rcx, qword ptr [rdx]
00BE98E8  41 83 C3 F8                     add r11d, -8
00BE98EC  49 89 09                        mov qword ptr [r9], rcx
00BE98EF  48 83 C2 08                     add rdx, 8
00BE98F3  49 83 C1 08                     add r9, 8
00BE98F7  48 83 EB 01                     sub rbx, 1
00BE98FB  75 E8                           jne 0x140be98e5
00BE98FD  8B 5C 24 40                     mov ebx, dword ptr [rsp + 0x40]
00BE9901  45 85 DB                        test r11d, r11d
00BE9904  74 12                           je 0x140be9918
00BE9906  4C 2B CA                        sub r9, rdx
00BE9909  8A 0A                           mov cl, byte ptr [rdx]
00BE990B  42 88 0C 0A                     mov byte ptr [rdx + r9], cl
00BE990F  48 FF C2                        inc rdx
00BE9912  41 83 C3 FF                     add r11d, -1
00BE9916  75 F1                           jne 0x140be9909
00BE9918  41 8B CA                        mov ecx, r10d
00BE991B  48 01 4C 24 78                  add qword ptr [rsp + 0x78], rcx
00BE9920  4C 03 C1                        add r8, rcx
00BE9923  41 2B DA                        sub ebx, r10d
00BE9926  49 89 07                        mov qword ptr [r15], rax
00BE9929  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00BE992D  0F 20 E1                        mov rcx, cr4
00BE9930  48 F7 C1 80 00 02 00            test rcx, 0x20080
00BE9937  74 10                           je 0x140be9949
00BE9939  48 8B C1                        mov rax, rcx
00BE993C  48 0F BA F8 07                  btc rax, 7
00BE9941  0F 22 E0                        mov cr4, rax
00BE9944  0F 22 E1                        mov cr4, rcx
00BE9947  EB 06                           jmp 0x140be994f
00BE9949  0F 20 D8                        mov rax, cr3
00BE994C  0F 22 D8                        mov cr3, rax
00BE994F  41 BA 01 00 00 00               mov r10d, 1
00BE9955  41 BB 00 10 00 00               mov r11d, 0x1000
00BE995B  4C 29 55 80                     sub qword ptr [rbp - 0x80], r10
00BE995F  0F 85 D1 FE FF FF               jne 0x140be9836
00BE9965  4C 8B 65 B0                     mov r12, qword ptr [rbp - 0x50]
00BE9969  44 8B 6C 24 68                  mov r13d, dword ptr [rsp + 0x68]
00BE996E  41 8B C5                        mov eax, r13d
00BE9971  49 83 C6 10                     add r14, 0x10
00BE9975  48 03 F0                        add rsi, rax
00BE9978  41 BB 00 10 00 00               mov r11d, 0x1000
00BE997E  4D 3B F4                        cmp r14, r12
00BE9981  0F 82 0F FE FF FF               jb 0x140be9796
00BE9987  48 8B 5D B8                     mov rbx, qword ptr [rbp - 0x48]
00BE998B  48 B9 F8 FF FF FF 7F 00 00 00   movabs rcx, 0x7ffffffff8
00BE9995  4C 8B 7D C0                     mov r15, qword ptr [rbp - 0x40]
00BE9999  F7 87 DC 09 00 00 00 00 40 00   test dword ptr [rdi + 0x9dc], 0x400000
00BE99A3  41 BD 01 00 00 00               mov r13d, 1
00BE99A9  4C 8B 87 28 02 00 00            mov r8, qword ptr [rdi + 0x228]
00BE99B0  75 1D                           jne 0x140be99cf
00BE99B2  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
00BE99B6  41 C6 00 C3                     mov byte ptr [r8], 0xc3
00BE99BA  0F 22 C0                        mov cr0, rax
00BE99BD  48 8B 75 90                     mov rsi, qword ptr [rbp - 0x70]
00BE99C1  4C 8B 75 98                     mov r14, qword ptr [rbp - 0x68]
00BE99C5  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
00BE99CA  E9 DA 02 00 00                  jmp 0x140be9ca9
00BE99CF  48 8B 97 D8 05 00 00            mov rdx, qword ptr [rdi + 0x5d8]
00BE99D6  4C 8D 4D 78                     lea r9, [rbp + 0x78]
00BE99DA  49 8B C0                        mov rax, r8
00BE99DD  C6 45 78 C3                     mov byte ptr [rbp + 0x78], 0xc3
00BE99E1  48 C1 E8 09                     shr rax, 9
00BE99E5  41 BB 04 00 00 00               mov r11d, 4
00BE99EB  48 23 C1                        and rax, rcx
00BE99EE  45 8B D3                        mov r10d, r11d
00BE99F1  48 03 C2                        add rax, rdx
00BE99F4  48 8D 4D 18                     lea rcx, [rbp + 0x18]
00BE99F8  48 BE F8 FF FF FF 7F 00 00 00   movabs rsi, 0x7ffffffff8
00BE9A02  48 89 01                        mov qword ptr [rcx], rax
00BE9A05  48 8D 49 08                     lea rcx, [rcx + 8]
00BE9A09  48 C1 E8 09                     shr rax, 9
00BE9A0D  48 23 C6                        and rax, rsi
00BE9A10  48 03 C2                        add rax, rdx
00BE9A13  4D 2B DD                        sub r11, r13
00BE9A16  75 EA                           jne 0x140be9a02
00BE9A18  41 83 CE FF                     or r14d, 0xffffffff
00BE9A1C  45 03 D6                        add r10d, r14d
00BE9A1F  74 0F                           je 0x140be9a30
00BE9A21  4A 8B 44 D5 18                  mov rax, qword ptr [rbp + r10*8 + 0x18]
00BE9A26  8B 08                           mov ecx, dword ptr [rax]
00BE9A28  C0 E9 07                        shr cl, 7
00BE9A2B  41 84 CD                        test r13b, cl
00BE9A2E  74 EC                           je 0x140be9a1c
00BE9A30  4E 8B 5C D5 18                  mov r11, qword ptr [rbp + r10*8 + 0x18]
00BE9A35  49 8B 03                        mov rax, qword ptr [r11]
00BE9A38  48 83 C8 62                     or rax, 0x62
00BE9A3C  49 89 03                        mov qword ptr [r11], rax
00BE9A3F  0F 20 E2                        mov rdx, cr4
00BE9A42  BE 80 00 02 00                  mov esi, 0x20080
00BE9A47  48 85 D6                        test rsi, rdx
00BE9A4A  74 10                           je 0x140be9a5c
00BE9A4C  48 8B CA                        mov rcx, rdx
00BE9A4F  48 0F BA F9 07                  btc rcx, 7
00BE9A54  0F 22 E1                        mov cr4, rcx
00BE9A57  0F 22 E2                        mov cr4, rdx
00BE9A5A  EB 06                           jmp 0x140be9a62
00BE9A5C  0F 20 D9                        mov rcx, cr3
00BE9A5F  0F 22 D9                        mov cr3, rcx
00BE9A62  41 8B C8                        mov ecx, r8d
00BE9A65  41 BA 00 10 00 00               mov r10d, 0x1000
00BE9A6B  81 E1 FF 0F 00 00               and ecx, 0xfff
00BE9A71  41 8B D5                        mov edx, r13d
00BE9A74  44 2B D1                        sub r10d, ecx
00BE9A77  45 3B D5                        cmp r10d, r13d
00BE9A7A  41 0F 42 D2                     cmovb edx, r10d
00BE9A7E  83 FA 08                        cmp edx, 8
00BE9A81  72 1D                           jb 0x140be9aa0
00BE9A83  44 8B D2                        mov r10d, edx
00BE9A86  49 C1 EA 03                     shr r10, 3
00BE9A8A  49 8B 09                        mov rcx, qword ptr [r9]
00BE9A8D  83 C2 F8                        add edx, -8
00BE9A90  49 89 08                        mov qword ptr [r8], rcx
00BE9A93  49 83 C1 08                     add r9, 8
00BE9A97  49 83 C0 08                     add r8, 8
00BE9A9B  4D 2B D5                        sub r10, r13
00BE9A9E  75 EA                           jne 0x140be9a8a
00BE9AA0  85 D2                           test edx, edx
00BE9AA2  74 12                           je 0x140be9ab6
00BE9AA4  4D 2B C1                        sub r8, r9
00BE9AA7  41 8A 09                        mov cl, byte ptr [r9]
00BE9AAA  43 88 0C 01                     mov byte ptr [r9 + r8], cl
00BE9AAE  4D 03 CD                        add r9, r13
00BE9AB1  41 03 D6                        add edx, r14d
00BE9AB4  75 F1                           jne 0x140be9aa7
00BE9AB6  49 89 03                        mov qword ptr [r11], rax
00BE9AB9  0F 20 E1                        mov rcx, cr4
00BE9ABC  48 85 CE                        test rsi, rcx
00BE9ABF  74 13                           je 0x140be9ad4
00BE9AC1  48 8B C1                        mov rax, rcx
00BE9AC4  48 0F BA F8 07                  btc rax, 7
00BE9AC9  0F 22 E0                        mov cr4, rax
00BE9ACC  0F 22 E1                        mov cr4, rcx
00BE9ACF  E9 E9 FE FF FF                  jmp 0x140be99bd
00BE9AD4  0F 20 D8                        mov rax, cr3
00BE9AD7  0F 22 D8                        mov cr3, rax
00BE9ADA  E9 DE FE FF FF                  jmp 0x140be99bd
00BE9ADF  44 8B 87 10 08 00 00            mov r8d, dword ptr [rdi + 0x810]
00BE9AE6  49 BA 01 20 00 04 80 00 10 70   movabs r10, 0x7010008004002001
00BE9AF0  4C 03 C7                        add r8, rdi
00BE9AF3  F7 87 D8 09 00 00 00 00 00 08   test dword ptr [rdi + 0x9d8], 0x8000000
00BE9AFD  74 38                           je 0x140be9b37
00BE9AFF  0F 31                           rdtsc
00BE9B01  48 C1 E2 20                     shl rdx, 0x20
00BE9B05  48 0B C2                        or rax, rdx
00BE9B08  48 8B C8                        mov rcx, rax
00BE9B0B  48 8B D0                        mov rdx, rax
00BE9B0E  48 C1 C9 03                     ror rcx, 3
00BE9B12  49 8B C2                        mov rax, r10
00BE9B15  48 33 D1                        xor rdx, rcx
00BE9B18  48 F7 E2                        mul rdx
00BE9B1B  4C 8B C2                        mov r8, rdx
00BE9B1E  48 89 55 E8                     mov qword ptr [rbp - 0x18], rdx
00BE9B22  4C 33 C0                        xor r8, rax
00BE9B25  48 8D 05 94 2D AD FF            lea rax, [rip - 0x52d26c]
00BE9B2C  41 83 E0 0F                     and r8d, 0xf
00BE9B30  49 C1 E0 04                     shl r8, 4
00BE9B34  4C 03 C0                        add r8, rax
00BE9B37  4C 8B 8F 50 0A 00 00            mov r9, qword ptr [rdi + 0xa50]
00BE9B3E  4D 85 C9                        test r9, r9
00BE9B41  75 05                           jne 0x140be9b48
00BE9B43  4C 8B CF                        mov r9, rdi
00BE9B46  EB 44                           jmp 0x140be9b8c
00BE9B48  0F 31                           rdtsc
00BE9B4A  48 C1 E2 20                     shl rdx, 0x20
00BE9B4E  48 0B C2                        or rax, rdx
00BE9B51  48 8B C8                        mov rcx, rax
00BE9B54  48 8B D0                        mov rdx, rax
00BE9B57  48 C1 C9 03                     ror rcx, 3
00BE9B5B  49 8B C2                        mov rax, r10
00BE9B5E  48 33 D1                        xor rdx, rcx
00BE9B61  48 F7 E2                        mul rdx
00BE9B64  48 89 55 F0                     mov qword ptr [rbp - 0x10], rdx
00BE9B68  48 33 D0                        xor rdx, rax
00BE9B6B  48 8B C2                        mov rax, rdx
00BE9B6E  49 89 51 10                     mov qword ptr [r9 + 0x10], rdx
00BE9B72  49 33 C0                        xor rax, r8
00BE9B75  48 33 D7                        xor rdx, rdi
00BE9B78  49 89 41 18                     mov qword ptr [r9 + 0x18], rax
00BE9B7C  49 89 51 08                     mov qword ptr [r9 + 8], rdx
00BE9B80  F0 44 09 3C 24                  lock or dword ptr [rsp], r15d
00BE9B85  4C 8B 87 F0 02 00 00            mov r8, qword ptr [rdi + 0x2f0]
00BE9B8C  4C 89 87 C8 07 00 00            mov qword ptr [rdi + 0x7c8], r8
00BE9B93  B8 B8 07 00 00                  mov eax, 0x7b8
00BE9B98  48 8B D7                        mov rdx, rdi
00BE9B9B  4C 89 8F D0 07 00 00            mov qword ptr [rdi + 0x7d0], r9
00BE9BA2  49 8B CF                        mov rcx, r15
00BE9BA5  48 89 0C 10                     mov qword ptr [rax + rdx], rcx
00BE9BA9  FA                              cli
00BE9BAA  FB                              sti
00BE9BAB  48 8B 87 78 02 00 00            mov rax, qword ptr [rdi + 0x278]
00BE9BB2  48 8D 9F 20 08 00 00            lea rbx, [rdi + 0x820]
00BE9BB9  48 8B CB                        mov rcx, rbx
00BE9BBC  E8 9F 0E 00 00                  call 0x140beaa60
00BE9BC1  8A D0                           mov dl, al
00BE9BC3  48 8B CB                        mov rcx, rbx
00BE9BC6  48 8B 87 80 02 00 00            mov rax, qword ptr [rdi + 0x280]
00BE9BCD  E8 8E 0E 00 00                  call 0x140beaa60
00BE9BD2  8B 8F 58 08 00 00               mov ecx, dword ptr [rdi + 0x858]
00BE9BD8  83 E9 03                        sub ecx, 3
00BE9BDB  74 7F                           je 0x140be9c5c
00BE9BDD  83 E9 01                        sub ecx, 1
00BE9BE0  74 49                           je 0x140be9c2b
00BE9BE2  83 F9 01                        cmp ecx, 1
00BE9BE5  0F 85 8E 00 00 00               jne 0x140be9c79
00BE9BEB  48 8B 8F E0 09 00 00            mov rcx, qword ptr [rdi + 0x9e0]
00BE9BF2  48 8D 97 E8 09 00 00            lea rdx, [rdi + 0x9e8]
00BE9BF9  49 03 CE                        add rcx, r14
00BE9BFC  4D 8B C6                        mov r8, r14
00BE9BFF  48 8B 02                        mov rax, qword ptr [rdx]
00BE9C02  41 83 C5 F8                     add r13d, -8
00BE9C06  48 89 01                        mov qword ptr [rcx], rax
00BE9C09  49 03 D6                        add rdx, r14
00BE9C0C  49 03 CE                        add rcx, r14
00BE9C0F  4D 2B C4                        sub r8, r12
00BE9C12  75 EB                           jne 0x140be9bff
00BE9C14  45 85 ED                        test r13d, r13d
00BE9C17  74 60                           je 0x140be9c79
00BE9C19  8A 02                           mov al, byte ptr [rdx]
00BE9C1B  49 03 D4                        add rdx, r12
00BE9C1E  88 01                           mov byte ptr [rcx], al
00BE9C20  49 03 CC                        add rcx, r12
00BE9C23  41 83 C5 FF                     add r13d, -1
00BE9C27  75 F0                           jne 0x140be9c19
00BE9C29  EB 4E                           jmp 0x140be9c79
00BE9C2B  8B 87 DC 09 00 00               mov eax, dword ptr [rdi + 0x9dc]
00BE9C31  4C 8B 8F 28 0A 00 00            mov r9, qword ptr [rdi + 0xa28]
00BE9C38  41 84 C4                        test r12b, al
00BE9C3B  75 15                           jne 0x140be9c52
00BE9C3D  49 8B 49 40                     mov rcx, qword ptr [r9 + 0x40]
00BE9C41  48 8B C1                        mov rax, rcx
00BE9C44  49 33 41 48                     xor rax, qword ptr [r9 + 0x48]
00BE9C48  49 33 C1                        xor rax, r9
00BE9C4B  49 33 49 38                     xor rcx, qword ptr [r9 + 0x38]
00BE9C4F  48 89 01                        mov qword ptr [rcx], rax
00BE9C52  4D 89 79 48                     mov qword ptr [r9 + 0x48], r15
00BE9C56  4D 89 79 38                     mov qword ptr [r9 + 0x38], r15
00BE9C5A  EB 1D                           jmp 0x140be9c79
00BE9C5C  FA                              cli
00BE9C5D  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00BE9C66  48 8B 87 58 06 00 00            mov rax, qword ptr [rdi + 0x658]
00BE9C6D  48 8B 0C 01                     mov rcx, qword ptr [rcx + rax]
00BE9C71  48 89 8F E0 09 00 00            mov qword ptr [rdi + 0x9e0], rcx
00BE9C78  FB                              sti
00BE9C79  F0 44 09 3C 24                  lock or dword ptr [rsp], r15d
00BE9C7E  4C 8D 9C 24 40 01 00 00         lea r11, [rsp + 0x140]
00BE9C86  48 8B C7                        mov rax, rdi
00BE9C89  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00BE9C8D  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00BE9C91  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00BE9C95  49 8B E3                        mov rsp, r11
00BE9C98  41 5F                           pop r15
00BE9C9A  41 5E                           pop r14
00BE9C9C  41 5D                           pop r13
00BE9C9E  41 5C                           pop r12
00BE9CA0  5D                              pop rbp
00BE9CA1  C3                              ret
00BE9CA2  CC                              int3
00BE9CA3  41 BD 01 00 00 00               mov r13d, 1
00BE9CA9  83 BF 48 09 00 00 00            cmp dword ptr [rdi + 0x948], 0
00BE9CB0  74 15                           je 0x140be9cc7
00BE9CB2  44 0F 20 C0                     mov rax, cr8
00BE9CB6  B9 02 00 00 00                  mov ecx, 2
00BE9CBB  3A C1                           cmp al, cl
00BE9CBD  73 08                           jae 0x140be9cc7
00BE9CBF  44 0F 20 C0                     mov rax, cr8
00BE9CC3  44 0F 22 C1                     mov cr8, rcx
00BE9CC7  8B 8F 48 09 00 00               mov ecx, dword ptr [rdi + 0x948]
00BE9CCD  85 C9                           test ecx, ecx
00BE9CCF  0F 84 BA 00 00 00               je 0x140be9d8f
00BE9CD5  83 E9 01                        sub ecx, 1
00BE9CD8  0F 84 A4 00 00 00               je 0x140be9d82
00BE9CDE  83 E9 01                        sub ecx, 1
00BE9CE1  0F 84 92 00 00 00               je 0x140be9d79
00BE9CE7  83 E9 01                        sub ecx, 1
00BE9CEA  0F 84 80 00 00 00               je 0x140be9d70
00BE9CF0  83 E9 01                        sub ecx, 1
00BE9CF3  74 3F                           je 0x140be9d34
00BE9CF5  83 F9 01                        cmp ecx, 1
00BE9CF8  74 14                           je 0x140be9d0e
00BE9CFA  48 8B 87 B0 05 00 00            mov rax, qword ptr [rdi + 0x5b0]
00BE9D01  F0 4C 09 A8 40 03 00 00         lock or qword ptr [rax + 0x340], r13
00BE9D09  E9 81 00 00 00                  jmp 0x140be9d8f
00BE9D0E  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00BE9D17  48 8B 87 58 06 00 00            mov rax, qword ptr [rdi + 0x658]
00BE9D1E  8B 97 D8 09 00 00               mov edx, dword ptr [rdi + 0x9d8]
00BE9D24  C1 EA 09                        shr edx, 9
00BE9D27  83 E2 1F                        and edx, 0x1f
00BE9D2A  48 8B 0C 08                     mov rcx, qword ptr [rax + rcx]
00BE9D2E  F0 0F AB 11                     lock bts dword ptr [rcx], edx
00BE9D32  EB 5B                           jmp 0x140be9d8f
00BE9D34  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
00BE9D3D  48 8B 87 58 06 00 00            mov rax, qword ptr [rdi + 0x658]
00BE9D44  44 8B 87 D8 09 00 00            mov r8d, dword ptr [rdi + 0x9d8]
00BE9D4B  41 C1 E8 09                     shr r8d, 9
00BE9D4F  41 83 E0 1F                     and r8d, 0x1f
00BE9D53  48 8B 0C 08                     mov rcx, qword ptr [rax + rcx]
00BE9D57  48 03 8F B8 06 00 00            add rcx, qword ptr [rdi + 0x6b8]
00BE9D5E  48 8B 87 98 06 00 00            mov rax, qword ptr [rdi + 0x698]
00BE9D65  48 8B 14 01                     mov rdx, qword ptr [rcx + rax]
00BE9D69  F0 44 0F AB 02                  lock bts dword ptr [rdx], r8d
00BE9D6E  EB 1F                           jmp 0x140be9d8f
00BE9D70  48 8B 87 58 05 00 00            mov rax, qword ptr [rdi + 0x558]
00BE9D77  EB 10                           jmp 0x140be9d89
00BE9D79  48 8B 87 50 05 00 00            mov rax, qword ptr [rdi + 0x550]
00BE9D80  EB 07                           jmp 0x140be9d89
00BE9D82  48 8B 87 40 05 00 00            mov rax, qword ptr [rdi + 0x540]
00BE9D89  F0 48 0F BA 28 00               lock bts qword ptr [rax], 0
00BE9D8F  48 8B 87 A0 06 00 00            mov rax, qword ptr [rdi + 0x6a0]
00BE9D96  48 83 24 03 00                  and qword ptr [rbx + rax], 0
00BE9D9B  48 8B 87 B0 06 00 00            mov rax, qword ptr [rdi + 0x6b0]
00BE9DA2  48 83 24 03 00                  and qword ptr [rbx + rax], 0
00BE9DA7  48 8B 8F 68 01 00 00            mov rcx, qword ptr [rdi + 0x168]
00BE9DAE  E8 BD 0C 00 00                  call 0x140beaa70
00BE9DB3  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00BE9DB8  4D 8B CE                        mov r9, r14
00BE9DBB  48 83 C0 F8                     add rax, -8
00BE9DBF  4D 8B C7                        mov r8, r15
00BE9DC2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00BE9DC7  49 8B D4                        mov rdx, r12
00BE9DCA  48 8B 87 68 01 00 00            mov rax, qword ptr [rdi + 0x168]
00BE9DD1  B9 09 01 00 00                  mov ecx, 0x109
00BE9DD6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00BE9DDB  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00BE9DE0  E8 CB 09 00 00                  call 0x140bea7b0
00BE9DE5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00BE8DF0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_cr0;
    __int64 v_cr8;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m114;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned int v_stack_m128;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (320);
    v_r15 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 2520))) & ((unsigned int)((unsigned int)(0x88000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x88000ULL)))) goto loc_00BE8EDF;
loc_00BE8E4D:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 2304)) = 0;
    a1 = (unsigned int)((304) + (-8));
    result = (*(unsigned __int64 *)(a2 + 2304)) + (v_r15 + 8);
    a3 = (v_r15 + 38) - (v_r15 + 1);
    if (condition_is_not_equal) goto loc_00BE8E4D;
    if ((unsigned int)(a1) == 0) goto loc_00BE8E6A;
loc_00BE8E5F:
    *(unsigned __int8 *)(result) = 0;
    result = (result) + (v_r15 + 1);
    a1 = (unsigned int)((a1) + (-1));
    if (condition_is_not_equal) goto loc_00BE8E5F;
loc_00BE8E6A:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 2304) + 16) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 2304) + 32) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 2304) + 288) = v_xmm0;
    *(unsigned __int16 *)(v_rsp - 104 - 96) = 303;
    *(unsigned __int64 *)(v_rsp - 104 - 94) = *(unsigned __int64 *)(a2 + 2304);
    a1 = (a2 + 2200) >> (16);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 2304) + 16) = (unsigned __int16)(a2 + 2200);
    result = (a2 + 2200) >> (32);
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 2304) + 24) = (unsigned int)(result);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 2304) + 22) = (unsigned __int16)(a1);
    if (((*(unsigned int *)(a2 + 2520)) & (0x40000000ULL)) == 0) goto loc_00BE8ECE;
    goto loc_00BE8EDE;
loc_00BE8ECE:
loc_00BE8EDE:
loc_00BE8EDF:
    *(unsigned int *)(a2 + 196) = 0;
    if (a2 >= (a2 + 1584)) goto loc_00BE8F27;
loc_00BE8F1C:
    result = (a2) + (64);
    if (result < (a2 + 1584)) goto loc_00BE8F1C;
loc_00BE8F27:
loc_00BE8F39:
loc_00BE8F3C:
    a3 = (*(unsigned __int64 *)(a2 + 2104)) ^ (*(unsigned __int64 *)(a2));
    a4 = (a2) + (v_r15 + 8);
    a3 = (a3) ^ (*(unsigned __int64 *)(a4));
    a4 = (a4) + (v_r15 + 8);
    result = (v_r15 + 8) - (v_r15 + 1);
    if (condition_is_not_equal) goto loc_00BE8F3C;
    a1 = (a4) - (a2);
    a1 = (a1) ^ (*(unsigned __int64 *)(a2 + 2104));
    a1 = (a1) ^ (a1);
    *(unsigned __int64 *)(v_rsp - 104 - 40) = *(unsigned __int64 *)(a2 + 2304);
    a2 = (unsigned int)((*(unsigned __int64 *)(a2 + 2304)) ^ (64));
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 2100))) ^ ((unsigned int)(a2)));
    v_r10 = (unsigned int)((v_r10) & (63));
    if (condition_is_equal) { v_r10 = (unsigned int)(v_r15 + 1); }
    v_rbx = (unsigned int)((12) + (-1));
    if (condition_is_not_equal) goto loc_00BE8F39;
loc_00BE8F8F:
    a3 = (a3) ^ (*(unsigned __int64 *)(a4));
    a4 = (a4) + (v_r15 + 8);
    a2 = (unsigned int)((v_rbx + 48) + (-8));
    result = (v_rbx + 6) - (v_r15 + 1);
    if (condition_is_not_equal) goto loc_00BE8F8F;
    if ((unsigned int)(a2) == 0) goto loc_00BE8FBC;
loc_00BE8FA7:
    a3 = (a3) ^ (*(unsigned __int8 *)(a4));
    a4 = (a4) + (v_r15 + 1);
    a2 = (unsigned int)((a2) + (-1));
    if (condition_is_not_equal) goto loc_00BE8FA7;
loc_00BE8FBC:
    *(unsigned int *)(a2 + 196) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 196)));
    if ((*(unsigned __int64 *)(a2 + 2664)) == a3) goto loc_00BE9115;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1416)) = a2;
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 2052)));
    if ((*(unsigned int *)(a2 + 2328)) != 0) goto loc_00BE9115;
    a1 = (a3) ^ (*(unsigned __int64 *)(a2 + 2664));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1416) + 24) = a1;
    if ((*(unsigned int *)(a2 + 2328)) != 0) goto loc_00BE9115;
    *(unsigned __int64 *)(a2 + 2336) = a2 + a2 * 1;
    *(unsigned __int64 *)(a2 + 2344) = 0;
    *(unsigned __int64 *)(a2 + 2352) = 265;
    *(unsigned __int64 *)(a2 + 2360) = a3;
    *(unsigned int *)(a2 + 2328) = (unsigned int)(v_r15 + 1);
    if ((*(unsigned int *)(a2 + 2328)) < 0) goto loc_00BE9115;
    if (((*(unsigned int *)(a2 + 2524)) & (0x200000ULL)) == 0) goto loc_00BE9115;
    if ((((unsigned __int8)(v_r15 + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 2520))))) == 0) goto loc_00BE9115;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_00BE90BE;
loc_00BE909E:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a2 + 2676)) + a2 * 1)) ^ (*(unsigned __int64 *)(a2 + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(a2 + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(a2 + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a2 = ((unsigned int)(*(unsigned int *)(a2 + 2676)) + a2 * 1) + (v_r15 + 8);
loc_00BE90BE:
    if (a2 != ((unsigned int)(*(unsigned int *)(a2 + 2676)) + a2 * 1 + a1 * 8)) goto loc_00BE909E;
    if (a3 == (*(unsigned __int64 *)(a2 + 2688))) goto loc_00BE9115;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 1416)) = a2;
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 2052)));
    result = *(unsigned __int64 *)(a2 + 1416);
    if ((*(unsigned int *)(a2 + 2328)) == 0) {
        result = *(unsigned __int64 *)(a2 + 1416);
        a1 = (*(unsigned __int64 *)(a2 + 2688)) ^ (a3);
        *(unsigned __int64 *)(result + 24) = a1;
    }
    a2 = 0;
    result = sub_00BE8384(0, a2, a3, 256);
loc_00BE9115:
    v_stack_m118 = 0;
loc_00BE9124:
    *(unsigned __int8 *)(v_stack_m110) = 0;
    result = (v_stack_m110) + (v_r15 + 1);
    a1 = (unsigned int)((4) + (-1));
    if (condition_is_not_equal) goto loc_00BE9124;
    v_stack_m128 = 0;
    if ((*(unsigned int *)(a2 + 2048)) <= 0) goto loc_00BE95F9;
loc_00BE914E:
    a3 = 0;
    if (*(unsigned __int64 *)(a2 + 2752) != 0) { a3 = *(unsigned __int64 *)(a2 + 2752); }
    v_rbx = ((unsigned int)(*(unsigned int *)(a3 + 2088))) + (a3);
    if (v_stack_m118 == 0) goto loc_00BE9185;
    if (v_stack_m114 <= 0) {
        v_rbx = v_stack_m110;
        a4 = v_stack_m114;
        v_rbx = (v_rbx) + (a3);
    }
    if (((unsigned int)(a4)) == 0) goto loc_00BE9287;
    v_r10 = (unsigned int)((0) - ((unsigned int)(a4)));
loc_00BE91A1:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx))) - (1));
    if (condition_is_equal) goto loc_00BE925E;
    a1 = (unsigned int)((a1) - (6));
    if (condition_is_equal) goto loc_00BE9251;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BE9245;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00BE923A;
    a1 = (unsigned int)((a1) - (18));
    if (condition_is_equal) goto loc_00BE9234;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00BE9209;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_00BE91E3;
    if (((unsigned int)(a1)) == 10) goto loc_00BE925E;
    goto loc_00BE9277;
loc_00BE91E3:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 32))) & (0xFFFULL));
    a2 = ((unsigned int)(*(unsigned int *)(v_rbx + 40))) + (0xFFFULL);
    a2 = (a2) + (a1);
    a2 = (a2) >> (12);
    goto loc_00BE9272;
loc_00BE9209:
    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_rbx + 36))));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 36)) - 1) & ((unsigned int)(result)));
    a2 = (a2) >> (3);
    a2 = (unsigned int)((a2) + (7));
    a2 = (unsigned int)((a2) & (0xFFFFFFF8ULL));
    result = (unsigned int)((*(unsigned __int16 *)(v_rbx + 40)) + (2));
    goto loc_00BE9272;
loc_00BE9234:
    goto loc_00BE9249;
loc_00BE923A:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 28))) + (3));
    result = (unsigned int)((result) << (4));
    goto loc_00BE9277;
loc_00BE9245:
loc_00BE9249:
    result = (unsigned int)((*(unsigned __int16 *)(v_rbx + 32)) + (55));
    result = (unsigned int)((result) & (0xFFFFFFF8ULL));
    goto loc_00BE9277;
loc_00BE9251:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 24))) + ((unsigned int)(a2)));
    result = (unsigned int)((result + result * 2) << (3));
    goto loc_00BE9277;
loc_00BE925E:
    a2 = (a2) >> (3);
loc_00BE9272:
loc_00BE9277:
    v_rbx = (v_rbx) + (a2 * 4 + 48);
    v_r10 = (v_r10) - (v_r15 + 1);
    if (condition_is_not_equal) goto loc_00BE91A1;
loc_00BE9287:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - ((unsigned int)(a3)));
    v_stack_m114 = 0;
    v_stack_m110 = (unsigned int)(result);
    v_stack_m118 = (unsigned int)(v_r15 + 1);
    if ((*(unsigned __int64 *)(v_rbx + 8)) >= (*(unsigned __int64 *)(v_rbx + 8) + (unsigned int)(*(unsigned int *)(v_rbx + 16)) * 1)) goto loc_00BE92D1;
loc_00BE92C6:
    result = (*(unsigned __int64 *)(v_rbx + 8)) + (v_r10 + 64);
    if (result < (*(unsigned __int64 *)(v_rbx + 8) + (unsigned int)(*(unsigned int *)(v_rbx + 16)) * 1)) goto loc_00BE92C6;
loc_00BE92D1:
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 16))))) >> (7));
    if ((unsigned int)(v_r10) == 0) goto loc_00BE933C;
loc_00BE92EA:
loc_00BE92EF:
    v_rsi = (*(unsigned __int64 *)(a2 + 2104)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8)));
    v_rsi = (v_rsi) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8) + 8));
    a4 = (*(unsigned __int64 *)(v_rbx + 8)) + (16);
    result = (8) - (v_r15 + 1);
    if (condition_is_not_equal) goto loc_00BE92EF;
    a1 = (a4) - (*(unsigned __int64 *)(v_rbx + 8));
    a1 = (a1) ^ (*(unsigned __int64 *)(a2 + 2104));
    a1 = (a1) ^ (a1);
    *(unsigned __int64 *)(v_rsp - 104 - 32) = 2;
    a2 = (unsigned int)((2) ^ ((unsigned int)(a2)));
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 2100))) ^ ((unsigned int)(a2)));
    v_r14 = (unsigned int)((v_r14) & (63));
    if (condition_is_equal) { v_r14 = (unsigned int)(v_r15 + 1); }
    v_r10 = (unsigned int)((v_r10) + (-1));
    if (condition_is_not_equal) goto loc_00BE92EA;
loc_00BE933C:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 16))) & (127));
    if (((unsigned int)(a3)) < 8) goto loc_00BE9363;
    result = ((unsigned int)((unsigned int)(a3))) >> (3);
loc_00BE934D:
    v_rsi = (v_rsi) ^ (*(unsigned __int64 *)(a4));
    a4 = (a4) + (8);
    a3 = (unsigned int)((a3) + (-8));
    result = (result) - (v_r15 + 1);
    if (condition_is_not_equal) goto loc_00BE934D;
loc_00BE9363:
    v_r15 = 0;
    if ((unsigned int)(a3) == 0) goto loc_00BE9381;
loc_00BE936B:
    v_rsi = (v_rsi) ^ (*(unsigned __int8 *)(a4));
    a4 = (a4) + (v_r15 + 1);
    a3 = (unsigned int)((a3) + (-1));
    if (condition_is_not_equal) goto loc_00BE936B;
loc_00BE9381:
    goto loc_00BE9388;
loc_00BE9386:
    v_rsi = (unsigned int)((v_rsi) ^ ((unsigned int)(v_rsi)));
loc_00BE9388:
    result = (v_rsi) >> (31);
    if (result != 0) goto loc_00BE9386;
    if (((unsigned int)(v_rsi)) == (*(unsigned int *)(v_rbx + 20))) goto loc_00BE95C9;
    v_r12 = 0;
    if ((*(unsigned int *)(v_rbx)) == 0) {
        result = 1;
        v_r12 = 0;
        if ((*(unsigned int *)(v_rbx + 24)) != 0) { v_r12 = (unsigned int)(result); }
    }
    if ((unsigned int)(*(unsigned int *)(v_rbx + 16)) == 0) goto loc_00BE9482;
    if ((((unsigned __int8)(v_r10 + 64)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2524))))) == 0) goto loc_00BE9482;
    v_r15 = (*(unsigned __int64 *)(v_rbx + 8)) & (0xFFFFFFFFFFFFF000ULL);
    result = ((unsigned int)(*(unsigned int *)(v_rbx + 16)) - 1) + (*(unsigned __int64 *)(v_rbx + 8));
    result = (result) | (0xFFFULL);
    v_stack_m108 = result;
    v_stack_m120 = v_r15 - 1;
loc_00BE9405:
loc_00BE9409:
    a2 = 0;
    result = KeGuardDispatchICall(v_r15, a2, a3, a4);
    if (((unsigned int)(result)) != 0xC000022DULL) goto loc_00BE944A;
    if ((unsigned int)(v_r12) != 0) goto loc_00BE947B;
    if (((unsigned __int8)(v_cr8)) > ((unsigned __int8)(v_r12 + 1))) goto loc_00BE944E;
    goto loc_00BE9409;
loc_00BE944A:
    if (sign_flag) goto loc_00BE947B;
loc_00BE944E:
    result = (v_stack_m120) + ((unsigned int)(0x1000ULL));
    v_r15 = (v_r15) + ((unsigned int)(0x1000ULL));
    v_stack_m120 = result;
    if (result != v_stack_m108) goto loc_00BE9405;
    v_r15 = 0;
    goto loc_00BE95D5;
loc_00BE947B:
    v_r15 = 0;
loc_00BE9482:
    result = (unsigned int)(*(unsigned int *)(v_rbx + 20));
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2328)) == 0) {
        a1 = (unsigned int)(v_rsi);
        a1 = (a1) ^ ((unsigned int)(*(unsigned int *)(v_rbx + 20)));
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1416);
        *(unsigned __int64 *)(result + 24) = a1;
    }
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2328)) != 0) goto loc_00BE95CF;
    result = (result) + (*(unsigned __int64 *)(v_rsp - 104 + 120));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2336) = result;
    result = (result) + (v_rbx);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2344) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2360) = *(unsigned __int64 *)(v_rbx + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2352) = (int)(*(unsigned int *)(v_rbx));
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2328) = 1;
    if (condition_is_below) goto loc_00BE95CF;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + (unsigned int)(0x9DCULL) * 1)) & (0x200000ULL)) == 0) goto loc_00BE95CF;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2520))))) == 0) goto loc_00BE95CF;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2052))) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2676)))));
    a1 = ((unsigned int)((unsigned int)(result))) >> (3);
    goto loc_00BE9572;
loc_00BE9551:
    result = (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2676)) + *(unsigned __int64 *)(v_rsp - 104 + 120) * 1)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2104));
    a1 = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2680))) & (63));
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2680)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2676)) + *(unsigned __int64 *)(v_rsp - 104 + 120) * 1) + (8);
loc_00BE9572:
    if (a2 != ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2676)) + *(unsigned __int64 *)(v_rsp - 104 + 120) * 1 + a1 * 8)) goto loc_00BE9551;
    if (a3 == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2688))) goto loc_00BE95CF;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1416)) = *(unsigned __int64 *)(v_rsp - 104 + 120);
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1416) + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2052)));
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1416);
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2328)) == 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1416);
        a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2688)) ^ (a3);
        *(unsigned __int64 *)(result + 24) = a1;
    }
    a2 = 0;
    result = sub_00BE8384(*(unsigned __int64 *)(v_rsp - 104 + 120), a2, a3, 256);
    goto loc_00BE95CF;
loc_00BE95C9:
loc_00BE95CF:
loc_00BE95D5:
    a1 = (unsigned int)(((unsigned int)(v_stack_m128)) + (1));
    v_stack_m128 = (unsigned int)(a1);
    if (((unsigned int)(a1)) < (*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2048))) goto loc_00BE914E;
loc_00BE95F9:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2328)) == 0) goto loc_00BE9ADF;
    *(unsigned __int64 *)(v_rsp - 104 - 112) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2352);
    *(unsigned __int64 *)(v_rsp - 104 - 104) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2360);
    *(unsigned __int64 *)(v_rsp - 104 - 64) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2344);
    v_stack_m108 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2336);
    result = (unsigned __int8)(v_cr8);
    v_cr8 = (unsigned __int8)(v_cr8);
    if (((unsigned __int8)((unsigned __int8)(v_cr8))) < 2) {
        result = (unsigned __int8)(v_cr8);
        v_cr8 = 2;
    }
    v_stack_m120 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1600) * 1);
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1608) + *(unsigned __int64 *)(gs_base + (0 + 32)) * 1)) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1928));
    *(unsigned __int64 *)(v_rsp - 104 - 72) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1624) * 1);
    if (v_stack_mF8 > (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1600) * 1))) goto loc_00BE96A6;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1600) * 1)) - ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1532)));
    if (v_stack_mF8 >= a1) goto loc_00BE96EB;
loc_00BE96A6:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1616) * 1)) == 0) goto loc_00BE96DB;
    if (v_stack_mF8 > a2) goto loc_00BE96DB;
    a1 = (a2) - ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1528)));
    if (v_stack_mF8 < a1) goto loc_00BE96DB;
    v_stack_m120 = a2;
    goto loc_00BE96EB;
loc_00BE96DB:
    v_stack_m120 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1624) * 1) + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1672) * 1);
loc_00BE96EB:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2520)) & (0x4000000ULL)) != 0) goto loc_00BE9CA3;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1624) * 1) + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1672) * 1);
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2524)) & (0x400000ULL)) == 0) {
        a1 = v_cr0;
        result = a1;
        *(unsigned __int64 *)(v_rsp - 104 - 120) = a1;
        v_cr0 = result;
    }
    v_r12 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2792))) << (4);
    a2 = 0;
    v_r12 = (v_r12) + (*(unsigned __int64 *)(v_rsp - 104 + 120) + 2800);
    *(unsigned __int64 *)(v_rsp - 104 - 80) = v_r12;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2796)) <= 0) goto loc_00BE9783;
loc_00BE9748:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r12)) = *(unsigned __int64 *)(v_r12 + 8);
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_00BE976E;
    goto loc_00BE9774;
loc_00BE976E:
loc_00BE9774:
    v_rsi = (v_r12) + (16);
    a2 = (unsigned int)((a2) + ((unsigned int)(a2 + 1)));
    if (((unsigned int)(a2)) < (*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2796))) goto loc_00BE9748;
loc_00BE9783:
    if ((*(unsigned __int64 *)(v_rsp - 104 + 120) + 2800) >= v_r12) goto loc_00BE9999;
loc_00BE9796:
    v_stack_m100 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2800 + 8)));
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2524)) & (0x400000ULL)) != 0) goto loc_00BE97F5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2800 + 8)))) < 8) goto loc_00BE97D7;
    a4 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2800 + 8))))) >> (3);
loc_00BE97C1:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2800 + 8))))) + (-8));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2800)) = *(unsigned __int64 *)(v_rsi);
    a1 = (v_rsi) + (8);
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2800)) + (8);
    a4 = (a4) - (a2 + 1);
    if (condition_is_not_equal) goto loc_00BE97C1;
loc_00BE97D7:
    if ((unsigned int)(a2) == 0) goto loc_00BE996E;
    a3 = (a3) - (a1);
loc_00BE97E2:
    *(unsigned __int8 *)(a1 + a3 * 1) = (unsigned __int8)(*(unsigned __int8 *)(a1));
    a1 = (a1) + (a2 + 1);
    a2 = (unsigned int)((a2) + (-1));
    if (condition_is_not_equal) goto loc_00BE97E2;
    goto loc_00BE996E;
loc_00BE97F5:
    v_stack_mF0 = v_rsi;
    a1 = (unsigned int)((a3) & (0xFFFULL));
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2800 + 8)) + 4095) + (a1);
    a2 = (a2) >> (12);
    v_stack_m128 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2800 + 8)))));
    if ((unsigned int)(a2) == 0) goto loc_00BE996E;
    *(unsigned __int64 *)(v_rsp - 104 - 128) = (unsigned int)((unsigned int)(a2));
loc_00BE9836:
    result = (a3) >> (9);
    result = (result) & ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2800 + 8)));
    result = (result) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1496));
loc_00BE985A:
    *(unsigned __int64 *)(v_rsp - 104 - 8) = result;
    result = (result) >> (9);
    result = (result) & ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2800 + 8)));
    result = (result) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1496));
    a2 = (4) - (1);
    if (condition_is_not_equal) goto loc_00BE985A;
loc_00BE9870:
    a4 = (unsigned int)((4) + (-1));
    if (condition_is_equal) goto loc_00BE9885;
    a1 = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + a4 * 8 - 8)))) >> (7));
    if (((1) & ((unsigned __int8)(a1))) == 0) goto loc_00BE9870;
loc_00BE9885:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + a4 * 8 - 8))) | (98);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + a4 * 8 - 8)) = result;
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_00BE98B0;
    goto loc_00BE98B6;
loc_00BE98B0:
loc_00BE98B6:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a3))) & (0xFFFULL));
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x1000ULL)))) - ((unsigned int)(a1)));
    v_r10 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2800 + 8))))));
    if (((unsigned int)(a2)) < ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2800 + 8))))))) { v_r10 = (unsigned int)(a2); }
    if (((unsigned int)(v_r10)) < 8) goto loc_00BE9901;
    v_rbx = ((unsigned int)((unsigned int)(v_r10))) >> (3);
loc_00BE98E5:
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) + (-8));
    *(unsigned __int64 *)(a3) = *(unsigned __int64 *)(v_stack_mF0);
    a2 = (v_stack_mF0) + (8);
    a4 = (a3) + (8);
    v_rbx = (v_rbx) - (1);
    if (condition_is_not_equal) goto loc_00BE98E5;
loc_00BE9901:
    if ((unsigned int)(v_r11) == 0) goto loc_00BE9918;
    a4 = (a4) - (a2);
loc_00BE9909:
    *(unsigned __int8 *)(a2 + a4 * 1) = (unsigned __int8)(*(unsigned __int8 *)(a2));
    a2 = (a2) + 1;
    v_r11 = (unsigned int)((v_r11) + (-1));
    if (condition_is_not_equal) goto loc_00BE9909;
loc_00BE9918:
    a3 = (a3) + ((unsigned int)((unsigned int)(v_r10)));
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m128)) - ((unsigned int)(v_r10)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + a4 * 8 - 8)) = result;
    v_stack_m128 = (unsigned int)(v_rbx);
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_00BE9949;
    goto loc_00BE994F;
loc_00BE9949:
loc_00BE994F:
    if (((v_cr4) & (0x20080ULL)) != 0) goto loc_00BE9836;
loc_00BE996E:
    v_r14 = (*(unsigned __int64 *)(v_rsp - 104 + 120) + 2800) + (16);
    v_rsi = (v_rsi) + ((unsigned int)((unsigned int)((unsigned int)(v_stack_m100))));
    if (v_r14 < (*(unsigned __int64 *)(v_rsp - 104 - 80))) goto loc_00BE9796;
loc_00BE9999:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2524)) & (0x400000ULL)) != 0) goto loc_00BE99CF;
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 552)) = 195;
loc_00BE99BD:
    goto loc_00BE9CA9;
loc_00BE99CF:
    *(unsigned __int8 *)(v_rsp - 104 + 120) = 195;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 552)) >> (9);
    result = (result) & (v_cr4);
    result = (result) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1496));
loc_00BE9A02:
    *(unsigned __int64 *)(v_rsp - 104 + 24) = result;
    result = (result) >> (9);
    result = (result) & (*(unsigned __int64 *)(v_rsp - 104 - 112));
    result = (result) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1496));
    v_r11 = (4) - (1);
    if (condition_is_not_equal) goto loc_00BE9A02;
    v_r14 = (unsigned int)((*(unsigned __int64 *)(v_rsp - 104 - 104)) | (0xFFFFFFFFULL));
loc_00BE9A1C:
    v_r10 = (unsigned int)((4) + ((unsigned int)(v_r14)));
    if (condition_is_equal) goto loc_00BE9A30;
    a1 = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + v_r10 * 8 + 24)))) >> (7));
    if (((1) & ((unsigned __int8)(a1))) == 0) goto loc_00BE9A1C;
loc_00BE9A30:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + v_r10 * 8 + 24))) | (98);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + v_r10 * 8 + 24)) = result;
    if ((((unsigned int)(0x20080ULL)) & (v_cr4)) == 0) goto loc_00BE9A5C;
    goto loc_00BE9A62;
loc_00BE9A5C:
loc_00BE9A62:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 552)))) & (0xFFFULL));
    v_r10 = (unsigned int)(((unsigned int)(0x1000ULL)) - ((unsigned int)(a1)));
    a2 = 1;
    if (((unsigned int)(v_r10)) < 1) { a2 = (unsigned int)(v_r10); }
    if (((unsigned int)(a2)) < 8) goto loc_00BE9AA0;
    v_r10 = ((unsigned int)((unsigned int)(a2))) >> (3);
loc_00BE9A8A:
    a2 = (unsigned int)((a2) + (-8));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 552)) = *(unsigned __int64 *)(v_rsp - 104 + 120);
    a4 = (v_rsp - 104 + 120) + (8);
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 552)) + (8);
    v_r10 = (v_r10) - (1);
    if (condition_is_not_equal) goto loc_00BE9A8A;
loc_00BE9AA0:
    if ((unsigned int)(a2) == 0) goto loc_00BE9AB6;
    a3 = (a3) - (a4);
loc_00BE9AA7:
    *(unsigned __int8 *)(a4 + a3 * 1) = (unsigned __int8)(*(unsigned __int8 *)(a4));
    a4 = (a4) + (1);
    a2 = (unsigned int)((a2) + ((unsigned int)(v_r14)));
    if (condition_is_not_equal) goto loc_00BE9AA7;
loc_00BE9AB6:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + v_r10 * 8 + 24)) = result;
    if ((((unsigned int)(0x20080ULL)) & (v_cr4)) == 0) goto loc_00BE9AD4;
    goto loc_00BE99BD;
loc_00BE9AD4:
    goto loc_00BE99BD;
loc_00BE9ADF:
    a3 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2064))) + (*(unsigned __int64 *)(v_rsp - 104 + 120));
    result = v_cr3;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2520)) & (0x8000000ULL)) != 0) {
        a2 = (a2) << (32);
        result = (v_cr3) | (a2);
        a1 = result;
        a2 = result;
        result = v_r10;
        a2 = (a2) ^ (a1);
        a3 = a2;
        *(unsigned __int64 *)(v_rsp - 104 - 24) = a2;
        a3 = (a3) ^ (result);
        result = v_rip - 5427820;
        a3 = (unsigned int)((a3) & (15));
        a3 = (a3) << (4);
        a3 = (a3) + (result);
    }
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2640) != 0) goto loc_00BE9B48;
    goto loc_00BE9B8C;
loc_00BE9B48:
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    *(unsigned __int64 *)(v_rsp - 104 - 16) = a2;
    a2 = (a2) ^ (v_r10);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 16) = a2;
    result = (a2) ^ (a3);
    a2 = (a2) ^ (*(unsigned __int64 *)(v_rsp - 104 + 120));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 24) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 8) = a2;
loc_00BE9B8C:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1992) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 752);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2000) = *(unsigned __int64 *)(v_rsp - 104 + 120);
    *(unsigned __int64 *)((unsigned int)(0x7B8ULL) + *(unsigned __int64 *)(v_rsp - 104 + 120) * 1) = *(unsigned __int64 *)(v_rsp - 104 - 64);
    result = KeGuardDispatchICall(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2080, *(unsigned __int64 *)(v_rsp - 104 + 120), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 752), *(unsigned __int64 *)(v_rsp - 104 + 120));
    result = KeGuardDispatchICall(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2080, (unsigned __int8)(result), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 752), *(unsigned __int64 *)(v_rsp - 104 + 120));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2136))) - (3));
    if (condition_is_equal) goto loc_00BE9C5C;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BE9C2B;
    if (((unsigned int)(a1)) != 1) goto loc_00BE9C79;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2528)) + (v_r14);
loc_00BE9BFF:
    v_r13 = (unsigned int)((1) + (-8));
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2536);
    a2 = (*(unsigned __int64 *)(v_rsp - 104 + 120) + 2536) + (v_r14);
    a1 = (a1) + (v_r14);
    a3 = (v_r14) - (v_stack_m108);
    if (condition_is_not_equal) goto loc_00BE9BFF;
    if ((unsigned int)(v_r13) == 0) goto loc_00BE9C79;
loc_00BE9C19:
    a2 = (a2) + (v_stack_m108);
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(a2));
    a1 = (a1) + (v_stack_m108);
    v_r13 = (unsigned int)((v_r13) + (-1));
    if (condition_is_not_equal) goto loc_00BE9C19;
    goto loc_00BE9C79;
loc_00BE9C2B:
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2524));
    if ((((unsigned __int8)(v_stack_m108)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2524))))) == 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2600) + 64);
        result = a1;
        result = (result) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2600) + 72));
        result = (result) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2600));
        a1 = (a1) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2600) + 56));
        *(unsigned __int64 *)(a1) = result;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2600) + 72) = *(unsigned __int64 *)(v_rsp - 104 - 64);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2600) + 56) = *(unsigned __int64 *)(v_rsp - 104 - 64);
    goto loc_00BE9C79;
loc_00BE9C5C:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2528) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 1624) * 1);
loc_00BE9C79:
    return *(unsigned __int64 *)(v_rsp - 104 + 120);
loc_00BE9CA3:
loc_00BE9CA9:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 2376)) == 0) goto loc_00BE9CC7;
    result = v_cr8;
    if (((unsigned __int8)(v_cr8)) < 2) {
        result = v_cr8;
        v_cr8 = 2;
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 2376))) == 0) goto loc_00BE9D8F;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 2376))) - (1));
    if (condition_is_equal) goto loc_00BE9D82;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BE9D79;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BE9D70;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00BE9D34;
    if (((unsigned int)(a1)) == 1) goto loc_00BE9D0E;
    goto loc_00BE9D8F;
loc_00BE9D0E:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 2520))) >> (9));
    a2 = (unsigned int)((a2) & (31));
    goto loc_00BE9D8F;
loc_00BE9D34:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 2520))) >> (9));
    a3 = (unsigned int)((a3) & (31));
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 1624) + *(unsigned __int64 *)(gs_base + (0 + 32)) * 1)) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 1720));
    goto loc_00BE9D8F;
loc_00BE9D70:
    goto loc_00BE9D89;
loc_00BE9D79:
    goto loc_00BE9D89;
loc_00BE9D82:
loc_00BE9D89:
loc_00BE9D8F:
    result = KeGuardCheckICall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 360), *(unsigned __int64 *)(a1 + *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 1688) * 1), a3, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 104 + 120) + 2600));
    result = (v_stack_mF8) + (-8);
    v_stack_m110 = result;
    v_stack_m118 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 360);
    v_stack_m120 = *(unsigned __int64 *)(v_stack_m28 + 64);
    result = SdbpCheckDll(265, v_stack_m108, *(unsigned __int64 *)(v_rsp - 104 - 64), v_r14);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00BE8DF0(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t v_cr0;
    int64_t v_cr8;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m114;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint32_t v_stack_m128;
    uint32_t v_stack_m168;
    uint64_t v_stack_m28;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(void **)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (320);
    local_r15 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x9D8))) & ((uint32_t)((uint32_t)(0x88000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x88000ULL)))) goto loc_00BE8EDF;
loc_00BE8E4D:
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x900)) = 0;
    Arg1 = (uint32_t)((304) + (-8));
    result = (*(uint64_t *)(arg2 + 0x900)) + (local_r15 + 8);
    a3 = (local_r15 + 38) - (local_r15 + 1);
    if (condition_is_not_equal) goto loc_00BE8E4D;
    if ((uint32_t)(Arg1) == 0) goto loc_00BE8E6A;
loc_00BE8E5F:
    *(uint8_t *)(result) = 0;
    result = (result) + (local_r15 + 1);
    Arg1 = (uint32_t)((Arg1) + (-1));
    if (condition_is_not_equal) goto loc_00BE8E5F;
loc_00BE8E6A:
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x900) + 0x10) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x900) + 0x20) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x900) + 0x120) = v_xmm0;
    *(uint16_t *)(local_rsp - 0x68 - 0x60) = 303;
    *(uint64_t *)(local_rsp - 0x68 - 0x5E) = *(uint64_t *)(arg2 + 0x900);
    Arg1 = (Arg2 + 2200) >> (16);
    *(uint16_t *)(*(uint64_t *)(arg2 + 0x900) + 0x10) = (uint16_t)(Arg2 + 2200);
    result = (Arg2 + 2200) >> (32);
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x900) + 0x18) = (uint32_t)(result);
    *(uint16_t *)(*(uint64_t *)(arg2 + 0x900) + 0x16) = (uint16_t)(Arg1);
    if (((*(uint32_t *)(arg2 + 0x9D8)) & (0x40000000ULL)) == 0) goto loc_00BE8ECE;
    goto loc_00BE8EDE;
loc_00BE8ECE:
loc_00BE8EDE:
loc_00BE8EDF:
    *(uint32_t *)(arg2 + 0xC4) = 0;
    if (Arg2 >= (Arg2 + 1584)) goto loc_00BE8F27;
loc_00BE8F1C:
    result = (Arg2) + (64);
    if (result < (Arg2 + 1584)) goto loc_00BE8F1C;
loc_00BE8F27:
loc_00BE8F39:
loc_00BE8F3C:
    a3 = (*(uint64_t *)(arg2 + 0x838)) ^ (*(uint64_t *)(arg2));
    a4 = (Arg2) + (local_r15 + 8);
    a3 = (a3) ^ (*(uint64_t *)(a4));
    a4 = (a4) + (local_r15 + 8);
    result = (local_r15 + 8) - (local_r15 + 1);
    if (condition_is_not_equal) goto loc_00BE8F3C;
    Arg1 = (a4) - (Arg2);
    Arg1 = (Arg1) ^ (*(uint64_t *)(arg2 + 0x838));
    Arg1 = (Arg1) ^ (Arg1);
    *(uint64_t *)(local_rsp - 0x68 - 0x28) = *(uint64_t *)(arg2 + 0x900);
    Arg2 = (uint32_t)((*(uint64_t *)(arg2 + 0x900)) ^ (64));
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x834))) ^ ((uint32_t)(Arg2)));
    local_r10 = (uint32_t)((local_r10) & (63));
    if (condition_is_equal) { local_r10 = (uint32_t)(local_r15 + 1); }
    local_rbx = (uint32_t)((12) + (-1));
    if (condition_is_not_equal) goto loc_00BE8F39;
loc_00BE8F8F:
    a3 = (a3) ^ (*(uint64_t *)(a4));
    a4 = (a4) + (local_r15 + 8);
    Arg2 = (uint32_t)((local_rbx + 48) + (-8));
    result = (local_rbx + 6) - (local_r15 + 1);
    if (condition_is_not_equal) goto loc_00BE8F8F;
    if ((uint32_t)(Arg2) == 0) goto loc_00BE8FBC;
loc_00BE8FA7:
    a3 = (a3) ^ (*(uint8_t *)(a4));
    a4 = (a4) + (local_r15 + 1);
    Arg2 = (uint32_t)((Arg2) + (-1));
    if (condition_is_not_equal) goto loc_00BE8FA7;
loc_00BE8FBC:
    *(uint32_t *)(arg2 + 0xC4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xC4)));
    if ((*(uint64_t *)(arg2 + 0xA68)) == a3) goto loc_00BE9115;
    *(void **)(*(uint64_t *)(arg2 + 0x588)) = Arg2;
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x804)));
    if ((*(uint32_t *)(arg2 + 0x918)) != 0) goto loc_00BE9115;
    Arg1 = (a3) ^ (*(uint64_t *)(arg2 + 0xA68));
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x588) + 0x18) = Arg1;
    if ((*(uint32_t *)(arg2 + 0x918)) != 0) goto loc_00BE9115;
    *(void **)(arg2 + 0x920) = Arg2 + Arg2 * 1;
    *(uint64_t *)(arg2 + 0x928) = 0;
    *(uint64_t *)(arg2 + 0x930) = 265;
    *(uint64_t *)(arg2 + 0x938) = a3;
    *(uint32_t *)(arg2 + 0x918) = (uint32_t)(local_r15 + 1);
    if ((*(uint32_t *)(arg2 + 0x918)) < 0) goto loc_00BE9115;
    if (((*(uint32_t *)(arg2 + 0x9DC)) & (0x200000ULL)) == 0) goto loc_00BE9115;
    if ((((uint8_t)(local_r15 + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x9D8))))) == 0) goto loc_00BE9115;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_00BE90BE;
loc_00BE909E:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(arg2 + 0xA74)) + arg2 * 1)) ^ (*(uint64_t *)(arg2 + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(arg2 + 0xA78))) & (63));
    a3 = (*(uint64_t *)(arg2 + 0xA78)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    Arg2 = ((uint32_t)(*(uint32_t *)(arg2 + 0xA74)) + Arg2 * 1) + (local_r15 + 8);
loc_00BE90BE:
    if (Arg2 != ((uint32_t)(*(uint32_t *)(arg2 + 0xA74)) + Arg2 * 1 + Arg1 * 8)) goto loc_00BE909E;
    if (a3 == (*(uint64_t *)(arg2 + 0xA80))) goto loc_00BE9115;
    *(void **)(*(uint64_t *)(arg2 + 0x588)) = Arg2;
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x804)));
    result = *(uint64_t *)(arg2 + 0x588);
    if ((*(uint32_t *)(arg2 + 0x918)) == 0) {
        result = *(uint64_t *)(arg2 + 0x588);
        Arg1 = (*(uint64_t *)(arg2 + 0xA80)) ^ (a3);
        *(uint64_t *)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384(0, Arg2, a3, 256);
loc_00BE9115:
    v_stack_m118 = 0;
loc_00BE9124:
    *(uint8_t *)(v_stack_m110) = 0;
    result = (v_stack_m110) + (local_r15 + 1);
    Arg1 = (uint32_t)((4) + (-1));
    if (condition_is_not_equal) goto loc_00BE9124;
    v_stack_m128 = 0;
    if ((*(uint32_t *)(arg2 + 0x800)) <= 0) goto loc_00BE95F9;
loc_00BE914E:
    a3 = 0;
    if (*(uint64_t *)(arg2 + 0xAC0) != 0) { a3 = *(uint64_t *)(arg2 + 0xAC0); }
    local_rbx = ((uint32_t)(*(uint32_t *)(a3 + 0x828))) + (a3);
    if (v_stack_m118 == 0) goto loc_00BE9185;
    if (v_stack_m114 <= 0) {
        local_rbx = v_stack_m110;
        a4 = v_stack_m114;
        local_rbx = (local_rbx) + (a3);
    }
    if (((uint32_t)(a4)) == 0) goto loc_00BE9287;
    local_r10 = (uint32_t)((0) - ((uint32_t)(a4)));
loc_00BE91A1:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx))) - (1));
    if (condition_is_equal) goto loc_00BE925E;
    Arg1 = (uint32_t)((Arg1) - (6));
    if (condition_is_equal) goto loc_00BE9251;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BE9245;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00BE923A;
    Arg1 = (uint32_t)((Arg1) - (18));
    if (condition_is_equal) goto loc_00BE9234;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00BE9209;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_00BE91E3;
    if (((uint32_t)(Arg1)) == 10) goto loc_00BE925E;
    goto loc_00BE9277;
loc_00BE91E3:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x20))) & (0xFFFULL));
    Arg2 = ((uint32_t)(*(uint32_t *)(local_rbx + 0x28))) + (0xFFFULL);
    Arg2 = (Arg2) + (Arg1);
    Arg2 = (Arg2) >> (12);
    goto loc_00BE9272;
loc_00BE9209:
    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(local_rbx + 0x24))));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x24)) - 1) & ((uint32_t)(result)));
    Arg2 = (Arg2) >> (3);
    Arg2 = (uint32_t)((Arg2) + (7));
    Arg2 = (uint32_t)((Arg2) & (0xFFFFFFF8ULL));
    result = (uint32_t)((*(uint16_t *)(local_rbx + 0x28)) + (2));
    goto loc_00BE9272;
loc_00BE9234:
    goto loc_00BE9249;
loc_00BE923A:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x1C))) + (3));
    result = (uint32_t)((result) << (4));
    goto loc_00BE9277;
loc_00BE9245:
loc_00BE9249:
    result = (uint32_t)((*(uint16_t *)(local_rbx + 0x20)) + (55));
    result = (uint32_t)((result) & (0xFFFFFFF8ULL));
    goto loc_00BE9277;
loc_00BE9251:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x18))) + ((uint32_t)(Arg2)));
    result = (uint32_t)((result + result * 2) << (3));
    goto loc_00BE9277;
loc_00BE925E:
    Arg2 = (Arg2) >> (3);
loc_00BE9272:
loc_00BE9277:
    local_rbx = (local_rbx) + (Arg2 * 4 + 48);
    local_r10 = (local_r10) - (local_r15 + 1);
    if (condition_is_not_equal) goto loc_00BE91A1;
loc_00BE9287:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - ((uint32_t)(a3)));
    v_stack_m114 = 0;
    v_stack_m110 = (uint32_t)(result);
    v_stack_m118 = (uint32_t)(local_r15 + 1);
    if ((*(uint64_t *)(local_rbx + 0x8)) >= (*(uint64_t *)(local_rbx + 0x8) + (uint32_t)(*(uint32_t *)(local_rbx + 0x10)) * 1)) goto loc_00BE92D1;
loc_00BE92C6:
    result = (*(uint64_t *)(local_rbx + 0x8)) + (local_r10 + 64);
    if (result < (*(uint64_t *)(local_rbx + 0x8) + (uint32_t)(*(uint32_t *)(local_rbx + 0x10)) * 1)) goto loc_00BE92C6;
loc_00BE92D1:
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x10))))) >> (7));
    if ((uint32_t)(local_r10) == 0) goto loc_00BE933C;
loc_00BE92EA:
loc_00BE92EF:
    local_rsi = (*(uint64_t *)(arg2 + 0x838)) ^ (*(uint64_t *)(*(uint64_t *)(local_rbx + 0x8)));
    local_rsi = (local_rsi) ^ (*(uint64_t *)(*(uint64_t *)(local_rbx + 0x8) + 0x8));
    a4 = (*(uint64_t *)(local_rbx + 0x8)) + (16);
    result = (8) - (local_r15 + 1);
    if (condition_is_not_equal) goto loc_00BE92EF;
    Arg1 = (a4) - (*(uint64_t *)(local_rbx + 0x8));
    Arg1 = (Arg1) ^ (*(uint64_t *)(arg2 + 0x838));
    Arg1 = (Arg1) ^ (Arg1);
    *(uint64_t *)(local_rsp - 0x68 - 0x20) = 2;
    Arg2 = (uint32_t)((2) ^ ((uint32_t)(Arg2)));
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x834))) ^ ((uint32_t)(Arg2)));
    local_r14 = (uint32_t)((local_r14) & (63));
    if (condition_is_equal) { local_r14 = (uint32_t)(local_r15 + 1); }
    local_r10 = (uint32_t)((local_r10) + (-1));
    if (condition_is_not_equal) goto loc_00BE92EA;
loc_00BE933C:
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x10))) & (127));
    if (((uint32_t)(a3)) < 8) goto loc_00BE9363;
    result = ((uint32_t)((uint32_t)(a3))) >> (3);
loc_00BE934D:
    local_rsi = (local_rsi) ^ (*(uint64_t *)(a4));
    a4 = (a4) + (8);
    a3 = (uint32_t)((a3) + (-8));
    result = (result) - (local_r15 + 1);
    if (condition_is_not_equal) goto loc_00BE934D;
loc_00BE9363:
    local_r15 = 0;
    if ((uint32_t)(a3) == 0) goto loc_00BE9381;
loc_00BE936B:
    local_rsi = (local_rsi) ^ (*(uint8_t *)(a4));
    a4 = (a4) + (local_r15 + 1);
    a3 = (uint32_t)((a3) + (-1));
    if (condition_is_not_equal) goto loc_00BE936B;
loc_00BE9381:
    goto loc_00BE9388;
loc_00BE9386:
    local_rsi = (uint32_t)((local_rsi) ^ ((uint32_t)(local_rsi)));
loc_00BE9388:
    result = (local_rsi) >> (31);
    if (result != 0) goto loc_00BE9386;
    if (((uint32_t)(local_rsi)) == (*(uint32_t *)(local_rbx + 0x14))) goto loc_00BE95C9;
    local_r12 = 0;
    if ((*(uint32_t *)(local_rbx)) == 0) {
        result = 1;
        local_r12 = 0;
        if ((*(uint32_t *)(local_rbx + 0x18)) != 0) { local_r12 = (uint32_t)(result); }
    }
    if ((uint32_t)(*(uint32_t *)(local_rbx + 0x10)) == 0) goto loc_00BE9482;
    if ((((uint8_t)(local_r10 + 64)) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x9DC))))) == 0) goto loc_00BE9482;
    local_r15 = (*(uint64_t *)(local_rbx + 0x8)) & (0xFFFFFFFFFFFFF000ULL);
    result = ((uint32_t)(*(uint32_t *)(local_rbx + 0x10)) - 1) + (*(uint64_t *)(local_rbx + 0x8));
    result = (result) | (0xFFFULL);
    v_stack_m108 = result;
    v_stack_m120 = local_r15 - 1;
loc_00BE9405:
loc_00BE9409:
    Arg2 = 0;
    result = KeGuardDispatchICall(local_r15, Arg2, a3, a4);
    if (((uint32_t)(result)) != 0xC000022DULL) goto loc_00BE944A;
    if ((uint32_t)(local_r12) != 0) goto loc_00BE947B;
    if (((uint8_t)(v_cr8)) > ((uint8_t)(local_r12 + 1))) goto loc_00BE944E;
    goto loc_00BE9409;
loc_00BE944A:
    if (sign_flag) goto loc_00BE947B;
loc_00BE944E:
    result = (v_stack_m120) + ((uint32_t)(0x1000ULL));
    local_r15 = (local_r15) + ((uint32_t)(0x1000ULL));
    v_stack_m120 = result;
    if (result != v_stack_m108) goto loc_00BE9405;
    local_r15 = 0;
    goto loc_00BE95D5;
loc_00BE947B:
    local_r15 = 0;
loc_00BE9482:
    result = (uint32_t)(*(uint32_t *)(local_rbx + 0x14));
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x918)) == 0) {
        Arg1 = (uint32_t)(local_rsi);
        Arg1 = (Arg1) ^ ((uint32_t)(*(uint32_t *)(local_rbx + 0x14)));
        result = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x588);
        *(uint64_t *)(result + 0x18) = Arg1;
    }
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x918)) != 0) goto loc_00BE95CF;
    result = (result) + (*(uint64_t *)(local_rsp - 0x68 + 0x78));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x920) = result;
    result = (result) + (local_rbx);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x928) = result;
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x938) = *(uint64_t *)(local_rbx + 0x8);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x930) = (int32_t)(*(uint32_t *)(local_rbx));
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x918) = 1;
    if (condition_is_below) goto loc_00BE95CF;
    if (((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + (uint32_t)(0x9DCULL) * 1)) & (0x200000ULL)) == 0) goto loc_00BE95CF;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x9D8))))) == 0) goto loc_00BE95CF;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x804))) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xA74)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) >> (3);
    goto loc_00BE9572;
loc_00BE9551:
    result = (*(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xA74)) + *(uint64_t *)(local_rsp - 0x68 + 0x78) * 1)) ^ (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x838));
    Arg1 = (uint32_t)(((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xA78))) & (63));
    a3 = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xA78)) + (result);
    a3 = (a3) ^ (0xEFAULL);
    Arg2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xA74)) + *(uint64_t *)(local_rsp - 0x68 + 0x78) * 1) + (8);
loc_00BE9572:
    if (Arg2 != ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xA74)) + *(uint64_t *)(local_rsp - 0x68 + 0x78) * 1 + Arg1 * 8)) goto loc_00BE9551;
    if (a3 == (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xA80))) goto loc_00BE95CF;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x588)) = *(uint64_t *)(local_rsp - 0x68 + 0x78);
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x588) + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x804)));
    result = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x588);
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x918)) == 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x588);
        Arg1 = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xA80)) ^ (a3);
        *(uint64_t *)(result + 0x18) = Arg1;
    }
    Arg2 = 0;
    result = sub_00BE8384(*(uint64_t *)(local_rsp - 0x68 + 0x78), Arg2, a3, 256);
    goto loc_00BE95CF;
loc_00BE95C9:
loc_00BE95CF:
loc_00BE95D5:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m128)) + (1));
    v_stack_m128 = (uint32_t)(Arg1);
    if (((uint32_t)(Arg1)) < (*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x800))) goto loc_00BE914E;
loc_00BE95F9:
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x918)) == 0) goto loc_00BE9ADF;
    *(uint64_t *)(local_rsp - 0x68 - 0x70) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x930);
    *(uint64_t *)(local_rsp - 0x68 - 0x68) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x938);
    *(uint64_t *)(local_rsp - 0x68 - 0x40) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x928);
    v_stack_m108 = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x920);
    result = (uint8_t)(v_cr8);
    v_cr8 = (uint8_t)(v_cr8);
    if (((uint8_t)((uint8_t)(v_cr8))) < 2) {
        result = (uint8_t)(v_cr8);
        v_cr8 = 2;
    }
    v_stack_m120 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x640) * 1);
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x648) + *(uint64_t *)(gs_base + (0 + 0x20)) * 1)) + (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x788));
    *(uint64_t *)(local_rsp - 0x68 - 0x48) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x658) * 1);
    if (v_stack_mF8 > (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x640) * 1))) goto loc_00BE96A6;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x640) * 1)) - ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x5FC)));
    if (v_stack_mF8 >= Arg1) goto loc_00BE96EB;
loc_00BE96A6:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x650) * 1)) == 0) goto loc_00BE96DB;
    if (v_stack_mF8 > Arg2) goto loc_00BE96DB;
    Arg1 = (Arg2) - ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x5F8)));
    if (v_stack_mF8 < Arg1) goto loc_00BE96DB;
    v_stack_m120 = Arg2;
    goto loc_00BE96EB;
loc_00BE96DB:
    v_stack_m120 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x658) * 1) + *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x688) * 1);
loc_00BE96EB:
    if (((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x9D8)) & (0x4000000ULL)) != 0) goto loc_00BE9CA3;
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x658) * 1) + *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x688) * 1);
    if (((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x9DC)) & (0x400000ULL)) == 0) {
        Arg1 = v_cr0;
        result = Arg1;
        *(uint64_t *)(local_rsp - 0x68 - 0x78) = Arg1;
        v_cr0 = result;
    }
    local_r12 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xAE8))) << (4);
    Arg2 = 0;
    local_r12 = (local_r12) + (*(uint64_t *)(local_rsp - 0x68 + 0x78) + 2800);
    *(uint64_t *)(local_rsp - 0x68 - 0x50) = local_r12;
    if ((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xAEC)) <= 0) goto loc_00BE9783;
loc_00BE9748:
    *(uint64_t *)(*(uint64_t *)(local_r12)) = *(uint64_t *)(local_r12 + 0x8);
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_00BE976E;
    goto loc_00BE9774;
loc_00BE976E:
loc_00BE9774:
    local_rsi = (local_r12) + (16);
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg2 + 1)));
    if (((uint32_t)(Arg2)) < (*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xAEC))) goto loc_00BE9748;
loc_00BE9783:
    if ((*(uint64_t *)(local_rsp - 0x68 + 0x78) + 2800) >= local_r12) goto loc_00BE9999;
loc_00BE9796:
    v_stack_m100 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xAF0 + 0x8)));
    if (((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x9DC)) & (0x400000ULL)) != 0) goto loc_00BE97F5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xAF0 + 0x8)))) < 8) goto loc_00BE97D7;
    a4 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xAF0 + 0x8))))) >> (3);
loc_00BE97C1:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xAF0 + 0x8))))) + (-8));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xAF0)) = *(uint64_t *)(local_rsi);
    Arg1 = (local_rsi) + (8);
    a3 = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xAF0)) + (8);
    a4 = (a4) - (Arg2 + 1);
    if (condition_is_not_equal) goto loc_00BE97C1;
loc_00BE97D7:
    if ((uint32_t)(Arg2) == 0) goto loc_00BE996E;
    a3 = (a3) - (Arg1);
loc_00BE97E2:
    *(uint8_t *)(Arg1 + a3 * 1) = (uint8_t)(*(uint8_t *)(Arg1));
    Arg1 = (Arg1) + (Arg2 + 1);
    Arg2 = (uint32_t)((Arg2) + (-1));
    if (condition_is_not_equal) goto loc_00BE97E2;
    goto loc_00BE996E;
loc_00BE97F5:
    v_stack_mF0 = local_rsi;
    Arg1 = (uint32_t)((a3) & (0xFFFULL));
    Arg2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xAF0 + 0x8)) + 4095) + (Arg1);
    Arg2 = (Arg2) >> (12);
    v_stack_m128 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xAF0 + 0x8)))));
    if ((uint32_t)(Arg2) == 0) goto loc_00BE996E;
    *(uint64_t *)(local_rsp - 0x68 - 0x80) = (uint32_t)((uint32_t)(Arg2));
loc_00BE9836:
    result = (a3) >> (9);
    result = (result) & ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xAF0 + 0x8)));
    result = (result) + (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x5D8));
loc_00BE985A:
    *(uint64_t *)(local_rsp - 0x68 - 0x8) = result;
    result = (result) >> (9);
    result = (result) & ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xAF0 + 0x8)));
    result = (result) + (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x5D8));
    Arg2 = (4) - (1);
    if (condition_is_not_equal) goto loc_00BE985A;
loc_00BE9870:
    a4 = (uint32_t)((4) + (-1));
    if (condition_is_equal) goto loc_00BE9885;
    Arg1 = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + a4 * 8 - 0x8)))) >> (7));
    if (((1) & ((uint8_t)(Arg1))) == 0) goto loc_00BE9870;
loc_00BE9885:
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + a4 * 8 - 0x8))) | (98);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + a4 * 8 - 0x8)) = result;
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_00BE98B0;
    goto loc_00BE98B6;
loc_00BE98B0:
loc_00BE98B6:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(a3))) & (0xFFFULL));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x1000ULL)))) - ((uint32_t)(Arg1)));
    local_r10 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xAF0 + 0x8))))));
    if (((uint32_t)(Arg2)) < ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xAF0 + 0x8))))))) { local_r10 = (uint32_t)(Arg2); }
    if (((uint32_t)(local_r10)) < 8) goto loc_00BE9901;
    local_rbx = ((uint32_t)((uint32_t)(local_r10))) >> (3);
loc_00BE98E5:
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) + (-8));
    *(uint64_t *)(a3) = *(uint64_t *)(v_stack_mF0);
    Arg2 = (v_stack_mF0) + (8);
    a4 = (a3) + (8);
    local_rbx = (local_rbx) - (1);
    if (condition_is_not_equal) goto loc_00BE98E5;
loc_00BE9901:
    if ((uint32_t)(local_r11) == 0) goto loc_00BE9918;
    a4 = (a4) - (Arg2);
loc_00BE9909:
    *(uint8_t *)(arg2 + a4 * 1) = (uint8_t)(*(uint8_t *)(arg2));
    Arg2 = (Arg2) + 1;
    local_r11 = (uint32_t)((local_r11) + (-1));
    if (condition_is_not_equal) goto loc_00BE9909;
loc_00BE9918:
    a3 = (a3) + ((uint32_t)((uint32_t)(local_r10)));
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m128)) - ((uint32_t)(local_r10)));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + a4 * 8 - 0x8)) = result;
    v_stack_m128 = (uint32_t)(local_rbx);
    if (((v_cr4) & (0x20080ULL)) == 0) goto loc_00BE9949;
    goto loc_00BE994F;
loc_00BE9949:
loc_00BE994F:
    if (((v_cr4) & (0x20080ULL)) != 0) goto loc_00BE9836;
loc_00BE996E:
    local_r14 = (*(uint64_t *)(local_rsp - 0x68 + 0x78) + 2800) + (16);
    local_rsi = (local_rsi) + ((uint32_t)((uint32_t)((uint32_t)(v_stack_m100))));
    if (local_r14 < (*(uint64_t *)(local_rsp - 0x68 - 0x50))) goto loc_00BE9796;
loc_00BE9999:
    if (((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x9DC)) & (0x400000ULL)) != 0) goto loc_00BE99CF;
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x228)) = 195;
loc_00BE99BD:
    goto loc_00BE9CA9;
loc_00BE99CF:
    *(uint8_t *)(local_rsp - 0x68 + 0x78) = 195;
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x228)) >> (9);
    result = (result) & (v_cr4);
    result = (result) + (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x5D8));
loc_00BE9A02:
    *(uint64_t *)(local_rsp - 0x68 + 0x18) = result;
    result = (result) >> (9);
    result = (result) & (*(uint64_t *)(local_rsp - 0x68 - 0x70));
    result = (result) + (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x5D8));
    local_r11 = (4) - (1);
    if (condition_is_not_equal) goto loc_00BE9A02;
    local_r14 = (uint32_t)((*(uint64_t *)(local_rsp - 0x68 - 0x68)) | (0xFFFFFFFFULL));
loc_00BE9A1C:
    local_r10 = (uint32_t)((4) + ((uint32_t)(local_r14)));
    if (condition_is_equal) goto loc_00BE9A30;
    Arg1 = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + local_r10 * 8 + 0x18)))) >> (7));
    if (((1) & ((uint8_t)(Arg1))) == 0) goto loc_00BE9A1C;
loc_00BE9A30:
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + local_r10 * 8 + 0x18))) | (98);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + local_r10 * 8 + 0x18)) = result;
    if ((((uint32_t)(0x20080ULL)) & (v_cr4)) == 0) goto loc_00BE9A5C;
    goto loc_00BE9A62;
loc_00BE9A5C:
loc_00BE9A62:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x228)))) & (0xFFFULL));
    local_r10 = (uint32_t)(((uint32_t)(0x1000ULL)) - ((uint32_t)(Arg1)));
    Arg2 = 1;
    if (((uint32_t)(local_r10)) < 1) { Arg2 = (uint32_t)(local_r10); }
    if (((uint32_t)(Arg2)) < 8) goto loc_00BE9AA0;
    local_r10 = ((uint32_t)((uint32_t)(Arg2))) >> (3);
loc_00BE9A8A:
    Arg2 = (uint32_t)((Arg2) + (-8));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x228)) = *(uint64_t *)(local_rsp - 0x68 + 0x78);
    a4 = (local_rsp - 104 + 120) + (8);
    a3 = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x228)) + (8);
    local_r10 = (local_r10) - (1);
    if (condition_is_not_equal) goto loc_00BE9A8A;
loc_00BE9AA0:
    if ((uint32_t)(Arg2) == 0) goto loc_00BE9AB6;
    a3 = (a3) - (a4);
loc_00BE9AA7:
    *(uint8_t *)(a4 + a3 * 1) = (uint8_t)(*(uint8_t *)(a4));
    a4 = (a4) + (1);
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r14)));
    if (condition_is_not_equal) goto loc_00BE9AA7;
loc_00BE9AB6:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + local_r10 * 8 + 0x18)) = result;
    if ((((uint32_t)(0x20080ULL)) & (v_cr4)) == 0) goto loc_00BE9AD4;
    goto loc_00BE99BD;
loc_00BE9AD4:
    goto loc_00BE99BD;
loc_00BE9ADF:
    a3 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x810))) + (*(uint64_t *)(local_rsp - 0x68 + 0x78));
    result = v_cr3;
    if (((*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x9D8)) & (0x8000000ULL)) != 0) {
        Arg2 = (Arg2) << (32);
        result = (v_cr3) | (Arg2);
        Arg1 = result;
        Arg2 = result;
        result = local_r10;
        Arg2 = (Arg2) ^ (Arg1);
        a3 = Arg2;
        *(void **)(local_rsp - 0x68 - 0x18) = Arg2;
        a3 = (a3) ^ (result);
        result = v_rip - 5427820;
        a3 = (uint32_t)((a3) & (15));
        a3 = (a3) << (4);
        a3 = (a3) + (result);
    }
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xA50) != 0) goto loc_00BE9B48;
    goto loc_00BE9B8C;
loc_00BE9B48:
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    *(void **)(local_rsp - 0x68 - 0x10) = Arg2;
    Arg2 = (Arg2) ^ (local_r10);
    *(void **)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x10) = Arg2;
    result = (Arg2) ^ (a3);
    Arg2 = (Arg2) ^ (*(uint64_t *)(local_rsp - 0x68 + 0x78));
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x18) = result;
    *(void **)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x8) = Arg2;
loc_00BE9B8C:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x7C8) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x2F0);
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x7D0) = *(uint64_t *)(local_rsp - 0x68 + 0x78);
    *(uint64_t *)((uint32_t)(0x7B8ULL) + *(uint64_t *)(local_rsp - 0x68 + 0x78) * 1) = *(uint64_t *)(local_rsp - 0x68 - 0x40);
    result = KeGuardDispatchICall(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 2080, *(uint64_t *)(local_rsp - 0x68 + 0x78), *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x2F0), *(uint64_t *)(local_rsp - 0x68 + 0x78));
    result = KeGuardDispatchICall(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 2080, (uint8_t)(result), *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x2F0), *(uint64_t *)(local_rsp - 0x68 + 0x78));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x858))) - (3));
    if (condition_is_equal) goto loc_00BE9C5C;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BE9C2B;
    if (((uint32_t)(Arg1)) != 1) goto loc_00BE9C79;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x9E0)) + (local_r14);
loc_00BE9BFF:
    local_r13 = (uint32_t)((1) + (-8));
    *(uint64_t *)(Arg1) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x9E8);
    Arg2 = (*(uint64_t *)(local_rsp - 0x68 + 0x78) + 2536) + (local_r14);
    Arg1 = (Arg1) + (local_r14);
    a3 = (local_r14) - (v_stack_m108);
    if (condition_is_not_equal) goto loc_00BE9BFF;
    if ((uint32_t)(local_r13) == 0) goto loc_00BE9C79;
loc_00BE9C19:
    Arg2 = (Arg2) + (v_stack_m108);
    *(uint8_t *)(Arg1) = (uint8_t)(*(uint8_t *)(arg2));
    Arg1 = (Arg1) + (v_stack_m108);
    local_r13 = (uint32_t)((local_r13) + (-1));
    if (condition_is_not_equal) goto loc_00BE9C19;
    goto loc_00BE9C79;
loc_00BE9C2B:
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x9DC));
    if ((((uint8_t)(v_stack_m108)) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x9DC))))) == 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xA28) + 0x40);
        result = Arg1;
        result = (result) ^ (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xA28) + 0x48));
        result = (result) ^ (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xA28));
        Arg1 = (Arg1) ^ (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xA28) + 0x38));
        *(uint64_t *)(Arg1) = result;
    }
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xA28) + 0x48) = *(uint64_t *)(local_rsp - 0x68 - 0x40);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xA28) + 0x38) = *(uint64_t *)(local_rsp - 0x68 - 0x40);
    goto loc_00BE9C79;
loc_00BE9C5C:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x9E0) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0x658) * 1);
loc_00BE9C79:
    return *(uint64_t *)(local_rsp - 0x68 + 0x78);
loc_00BE9CA3:
loc_00BE9CA9:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x948)) == 0) goto loc_00BE9CC7;
    result = v_cr8;
    if (((uint8_t)(v_cr8)) < 2) {
        result = v_cr8;
        v_cr8 = 2;
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x948))) == 0) goto loc_00BE9D8F;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x948))) - (1));
    if (condition_is_equal) goto loc_00BE9D82;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BE9D79;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BE9D70;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00BE9D34;
    if (((uint32_t)(Arg1)) == 1) goto loc_00BE9D0E;
    goto loc_00BE9D8F;
loc_00BE9D0E:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x9D8))) >> (9));
    Arg2 = (uint32_t)((Arg2) & (31));
    goto loc_00BE9D8F;
loc_00BE9D34:
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x9D8))) >> (9));
    a3 = (uint32_t)((a3) & (31));
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x658) + *(uint64_t *)(gs_base + (0 + 0x20)) * 1)) + (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x6B8));
    goto loc_00BE9D8F;
loc_00BE9D70:
    goto loc_00BE9D89;
loc_00BE9D79:
    goto loc_00BE9D89;
loc_00BE9D82:
loc_00BE9D89:
loc_00BE9D8F:
    result = KeGuardCheckICall(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x168), *(uint64_t *)(Arg1 + *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x698) * 1), a3, *(uint64_t *)(*(uint64_t *)(local_rsp - 0x68 + 0x78) + 0xA28));
    result = (v_stack_mF8) + (-8);
    v_stack_m110 = result;
    v_stack_m118 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x168);
    v_stack_m120 = *(uint64_t *)(v_stack_m28 + 0x40);
    result = SdbpCheckDll(265, v_stack_m108, *(uint64_t *)(local_rsp - 0x68 - 0x40), local_r14);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `8` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0xC4` | `32` | `R` |
| `Arg2` | `+ 0xC4` | `32` | `W` |
| `Arg2` | `+ 0x630` | `64` | `R` |
| `Arg2` | `+ 0x834` | `32` | `R` |
| `Arg2` | `+ 0x838` | `64` | `R` |
| `Arg2` | `+ 0x848` | `32` | `R/W` |
| `Arg2` | `+ 0x868` | `128` | `R` |
| `Arg2` | `+ 0x878` | `128` | `R` |
| `Arg2` | `+ 0x888` | `128` | `R` |
| `Arg2` | `+ 0x898` | `64` | `R` |
| `Arg2` | `+ 0x900` | `64` | `R` |
| `Arg2` | `+ 0x9D8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=initkdbg&rva=0x00BE8DF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
