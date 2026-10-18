# PpmEventTraceCoreParkingSelectionEx

- RVA: `0x004F09D0`–`0x004F132A` (길이 `2,394` bytes)
- VA: `0x00000001404F09D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B5EDC`
- 디코드: `618`개 명령, `2,394/2,394` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x004F0A40` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x004F12FA` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x004F1309` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PpmParkComputeUnparkMaskEx](../5E/PpmParkComputeUnparkMaskEx_function_005E05E0.md) at `0x005E112C`

### Static image references
- `0x004F09FB` → RVA `0x00E0A740` (`.data`; read)
- `0x004F0A0C` → RVA `0x00E67A70` (`.data`; read)
- `0x004F0A25` → RVA `0x00E67A39` (`.data`; read)
- `0x004F0A32` → RVA `0x00F083E8` (`.data`; read)
- `0x004F0A39` → RVA `0x0001BAA0` (`.rdata`; read)
- `0x004F0AD6` → RVA `0x00E67A78` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F09D0  48 8B C4                        mov rax, rsp
004F09D3  48 89 58 08                     mov qword ptr [rax + 8], rbx
004F09D7  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
004F09DB  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
004F09DF  89 50 10                        mov dword ptr [rax + 0x10], edx
004F09E2  55                              push rbp
004F09E3  56                              push rsi
004F09E4  57                              push rdi
004F09E5  41 54                           push r12
004F09E7  41 55                           push r13
004F09E9  41 56                           push r14
004F09EB  41 57                           push r15
004F09ED  48 8D A8 D8 FD FF FF            lea rbp, [rax - 0x228]
004F09F4  48 81 EC F0 02 00 00            sub rsp, 0x2f0
004F09FB  48 8B 05 3E 9D 91 00            mov rax, qword ptr [rip + 0x919d3e]
004F0A02  48 33 C4                        xor rax, rsp
004F0A05  48 89 85 E0 01 00 00            mov qword ptr [rbp + 0x1e0], rax
004F0A0C  48 8B 1D 5D 70 97 00            mov rbx, qword ptr [rip + 0x97705d]
004F0A13  45 33 E4                        xor r12d, r12d
004F0A16  48 8B F1                        mov rsi, rcx
004F0A19  41 8B FC                        mov edi, r12d
004F0A1C  48 85 DB                        test rbx, rbx
004F0A1F  0F 84 DA 08 00 00               je 0x1404f12ff
004F0A25  44 38 25 0D 70 97 00            cmp byte ptr [rip + 0x97700d], r12b
004F0A2C  0F 84 CD 08 00 00               je 0x1404f12ff
004F0A32  48 8B 0D AF 79 A1 00            mov rcx, qword ptr [rip + 0xa179af]
004F0A39  48 8D 15 60 B0 B2 FF            lea rdx, [rip - 0x4d4fa0]
004F0A40  E8 0B 1A EA FF                  call 0x140392450
004F0A45  84 C0                           test al, al
004F0A47  0F 84 B2 08 00 00               je 0x1404f12ff
004F0A4D  44 0F B7 0E                     movzx r9d, word ptr [rsi]
004F0A51  45 8D 6C 24 01                  lea r13d, [r12 + 1]
004F0A56  45 0F B7 C4                     movzx r8d, r12w
004F0A5A  41 8B D4                        mov edx, r12d
004F0A5D  66 41 3B D1                     cmp dx, r9w
004F0A61  73 18                           jae 0x1404f0a7b
004F0A63  0F B7 C2                        movzx eax, dx
004F0A66  4C 39 64 C6 08                  cmp qword ptr [rsi + rax*8 + 8], r12
004F0A6B  74 0E                           je 0x1404f0a7b
004F0A6D  8B C7                           mov eax, edi
004F0A6F  41 03 FD                        add edi, r13d
004F0A72  66 45 03 C5                     add r8w, r13w
004F0A76  66 89 54 44 60                  mov word ptr [rsp + rax*2 + 0x60], dx
004F0A7B  41 03 D5                        add edx, r13d
004F0A7E  83 FA 20                        cmp edx, 0x20
004F0A81  72 DA                           jb 0x1404f0a5d
004F0A83  66 44 89 44 24 40               mov word ptr [rsp + 0x40], r8w
004F0A89  48 8D 44 24 40                  lea rax, [rsp + 0x40]
004F0A8E  48 89 03                        mov qword ptr [rbx], rax
004F0A91  41 8B D5                        mov edx, r13d
004F0A94  48 C7 43 08 02 00 00 00         mov qword ptr [rbx + 8], 2
004F0A9C  66 45 3B E0                     cmp r12w, r8w
004F0AA0  73 54                           jae 0x1404f0af6
004F0AA2  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
004F0AA7  45 0F B7 D0                     movzx r10d, r8w
004F0AAB  45 0F B7 01                     movzx r8d, word ptr [r9]
004F0AAF  8D 4A 01                        lea ecx, [rdx + 1]
004F0AB2  8B C2                           mov eax, edx
004F0AB4  48 03 C9                        add rcx, rcx
004F0AB7  48 03 C0                        add rax, rax
004F0ABA  4C 89 0C C3                     mov qword ptr [rbx + rax*8], r9
004F0ABE  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F0AC7  66 44 3B 06                     cmp r8w, word ptr [rsi]
004F0ACB  73 09                           jae 0x1404f0ad6
004F0ACD  49 FF C0                        inc r8
004F0AD0  4E 8D 04 C6                     lea r8, [rsi + r8*8]
004F0AD4  EB 07                           jmp 0x1404f0add
004F0AD6  4C 8D 05 9B 6F 97 00            lea r8, [rip + 0x976f9b]
004F0ADD  83 C2 02                        add edx, 2
004F0AE0  4C 89 04 CB                     mov qword ptr [rbx + rcx*8], r8
004F0AE4  49 83 C1 02                     add r9, 2
004F0AE8  48 C7 44 CB 08 08 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 8
004F0AF1  4D 2B D5                        sub r10, r13
004F0AF4  75 B5                           jne 0x1404f0aab
004F0AF6  4C 8B 9D 60 02 00 00            mov r11, qword ptr [rbp + 0x260]
004F0AFD  48 8D 8D 38 02 00 00            lea rcx, [rbp + 0x238]
004F0B04  8B C2                           mov eax, edx
004F0B06  4D 8B F3                        mov r14, r11
004F0B09  48 03 C0                        add rax, rax
004F0B0C  44 8B D7                        mov r10d, edi
004F0B0F  45 0F B7 CC                     movzx r9d, r12w
004F0B13  45 8B C4                        mov r8d, r12d
004F0B16  48 89 0C C3                     mov qword ptr [rbx + rax*8], rcx
004F0B1A  8D 4A 01                        lea ecx, [rdx + 1]
004F0B1D  48 C7 44 C3 08 04 00 00 00      mov qword ptr [rbx + rax*8 + 8], 4
004F0B26  48 03 C9                        add rcx, rcx
004F0B29  48 8D 85 40 02 00 00            lea rax, [rbp + 0x240]
004F0B30  48 89 04 CB                     mov qword ptr [rbx + rcx*8], rax
004F0B34  48 8D 85 48 02 00 00            lea rax, [rbp + 0x248]
004F0B3B  48 C7 44 CB 08 04 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 4
004F0B44  8D 4A 02                        lea ecx, [rdx + 2]
004F0B47  48 03 C9                        add rcx, rcx
004F0B4A  48 89 04 CB                     mov qword ptr [rbx + rcx*8], rax
004F0B4E  48 8D 85 50 02 00 00            lea rax, [rbp + 0x250]
004F0B55  48 C7 44 CB 08 04 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 4
004F0B5E  8D 4A 03                        lea ecx, [rdx + 3]
004F0B61  48 03 C9                        add rcx, rcx
004F0B64  48 89 04 CB                     mov qword ptr [rbx + rcx*8], rax
004F0B68  48 8D 85 58 02 00 00            lea rax, [rbp + 0x258]
004F0B6F  48 C7 44 CB 08 04 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 4
004F0B78  8D 4A 04                        lea ecx, [rdx + 4]
004F0B7B  48 03 C9                        add rcx, rcx
004F0B7E  83 C2 05                        add edx, 5
004F0B81  48 85 F6                        test rsi, rsi
004F0B84  4C 0F 45 F6                     cmovne r14, rsi
004F0B88  48 89 04 CB                     mov qword ptr [rbx + rcx*8], rax
004F0B8C  48 C7 44 CB 08 04 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 4
004F0B95  45 0F B7 3E                     movzx r15d, word ptr [r14]
004F0B99  66 45 3B C7                     cmp r8w, r15w
004F0B9D  73 1A                           jae 0x1404f0bb9
004F0B9F  41 0F B7 C0                     movzx eax, r8w
004F0BA3  4D 39 64 C6 08                  cmp qword ptr [r14 + rax*8 + 8], r12
004F0BA8  74 0F                           je 0x1404f0bb9
004F0BAA  8B C7                           mov eax, edi
004F0BAC  41 03 FD                        add edi, r13d
004F0BAF  66 45 03 CD                     add r9w, r13w
004F0BB3  66 44 89 44 44 60               mov word ptr [rsp + rax*2 + 0x60], r8w
004F0BB9  45 03 C5                        add r8d, r13d
004F0BBC  41 83 F8 20                     cmp r8d, 0x20
004F0BC0  72 D7                           jb 0x1404f0b99
004F0BC2  66 44 89 4C 24 42               mov word ptr [rsp + 0x42], r9w
004F0BC8  48 85 F6                        test rsi, rsi
004F0BCB  75 1A                           jne 0x1404f0be7
004F0BCD  8B C2                           mov eax, edx
004F0BCF  48 8D 4C 24 42                  lea rcx, [rsp + 0x42]
004F0BD4  48 03 C0                        add rax, rax
004F0BD7  41 03 D5                        add edx, r13d
004F0BDA  48 89 0C C3                     mov qword ptr [rbx + rax*8], rcx
004F0BDE  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F0BE7  41 0F B7 C9                     movzx ecx, r9w
004F0BEB  42 8D 04 11                     lea eax, [rcx + r10]
004F0BEF  44 3B D0                        cmp r10d, eax
004F0BF2  73 57                           jae 0x1404f0c4b
004F0BF4  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
004F0BF9  4F 8D 04 50                     lea r8, [r8 + r10*2]
004F0BFD  44 8B D1                        mov r10d, ecx
004F0C00  45 0F B7 08                     movzx r9d, word ptr [r8]
004F0C04  8D 4A 01                        lea ecx, [rdx + 1]
004F0C07  8B C2                           mov eax, edx
004F0C09  48 03 C9                        add rcx, rcx
004F0C0C  48 03 C0                        add rax, rax
004F0C0F  4C 89 04 C3                     mov qword ptr [rbx + rax*8], r8
004F0C13  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F0C1C  66 45 3B 0B                     cmp r9w, word ptr [r11]
004F0C20  73 09                           jae 0x1404f0c2b
004F0C22  49 FF C1                        inc r9
004F0C25  4F 8D 0C CB                     lea r9, [r11 + r9*8]
004F0C29  EB 07                           jmp 0x1404f0c32
004F0C2B  4C 8D 0D 46 6E 97 00            lea r9, [rip + 0x976e46]
004F0C32  83 C2 02                        add edx, 2
004F0C35  4C 89 0C CB                     mov qword ptr [rbx + rcx*8], r9
004F0C39  49 83 C0 02                     add r8, 2
004F0C3D  48 C7 44 CB 08 08 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 8
004F0C46  4D 2B D5                        sub r10, r13
004F0C49  75 B5                           jne 0x1404f0c00
004F0C4B  4C 8B B5 68 02 00 00            mov r14, qword ptr [rbp + 0x268]
004F0C52  48 85 F6                        test rsi, rsi
004F0C55  4D 8B D6                        mov r10, r14
004F0C58  44 8B DF                        mov r11d, edi
004F0C5B  4C 0F 45 D6                     cmovne r10, rsi
004F0C5F  45 0F B7 CC                     movzx r9d, r12w
004F0C63  45 8B C4                        mov r8d, r12d
004F0C66  45 0F B7 3A                     movzx r15d, word ptr [r10]
004F0C6A  66 45 3B C7                     cmp r8w, r15w
004F0C6E  73 1A                           jae 0x1404f0c8a
004F0C70  41 0F B7 C0                     movzx eax, r8w
004F0C74  4D 39 64 C2 08                  cmp qword ptr [r10 + rax*8 + 8], r12
004F0C79  74 0F                           je 0x1404f0c8a
004F0C7B  8B C7                           mov eax, edi
004F0C7D  41 03 FD                        add edi, r13d
004F0C80  66 45 03 CD                     add r9w, r13w
004F0C84  66 44 89 44 44 60               mov word ptr [rsp + rax*2 + 0x60], r8w
004F0C8A  45 03 C5                        add r8d, r13d
004F0C8D  41 83 F8 20                     cmp r8d, 0x20
004F0C91  72 D7                           jb 0x1404f0c6a
004F0C93  66 44 89 4C 24 44               mov word ptr [rsp + 0x44], r9w
004F0C99  48 85 F6                        test rsi, rsi
004F0C9C  75 1A                           jne 0x1404f0cb8
004F0C9E  8B C2                           mov eax, edx
004F0CA0  48 8D 4C 24 44                  lea rcx, [rsp + 0x44]
004F0CA5  48 03 C0                        add rax, rax
004F0CA8  41 03 D5                        add edx, r13d
004F0CAB  48 89 0C C3                     mov qword ptr [rbx + rax*8], rcx
004F0CAF  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F0CB8  41 0F B7 C9                     movzx ecx, r9w
004F0CBC  42 8D 04 19                     lea eax, [rcx + r11]
004F0CC0  44 3B D8                        cmp r11d, eax
004F0CC3  73 57                           jae 0x1404f0d1c
004F0CC5  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
004F0CCA  44 8B D1                        mov r10d, ecx
004F0CCD  4F 8D 04 58                     lea r8, [r8 + r11*2]
004F0CD1  45 0F B7 08                     movzx r9d, word ptr [r8]
004F0CD5  8D 4A 01                        lea ecx, [rdx + 1]
004F0CD8  8B C2                           mov eax, edx
004F0CDA  48 03 C9                        add rcx, rcx
004F0CDD  48 03 C0                        add rax, rax
004F0CE0  4C 89 04 C3                     mov qword ptr [rbx + rax*8], r8
004F0CE4  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F0CED  66 45 3B 0E                     cmp r9w, word ptr [r14]
004F0CF1  73 09                           jae 0x1404f0cfc
004F0CF3  49 FF C1                        inc r9
004F0CF6  4F 8D 0C CE                     lea r9, [r14 + r9*8]
004F0CFA  EB 07                           jmp 0x1404f0d03
004F0CFC  4C 8D 0D 75 6D 97 00            lea r9, [rip + 0x976d75]
004F0D03  83 C2 02                        add edx, 2
004F0D06  4C 89 0C CB                     mov qword ptr [rbx + rcx*8], r9
004F0D0A  49 83 C0 02                     add r8, 2
004F0D0E  48 C7 44 CB 08 08 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 8
004F0D17  4D 2B D5                        sub r10, r13
004F0D1A  75 B5                           jne 0x1404f0cd1
004F0D1C  4C 8B B5 70 02 00 00            mov r14, qword ptr [rbp + 0x270]
004F0D23  48 85 F6                        test rsi, rsi
004F0D26  4D 8B D6                        mov r10, r14
004F0D29  44 8B DF                        mov r11d, edi
004F0D2C  4C 0F 45 D6                     cmovne r10, rsi
004F0D30  45 0F B7 CC                     movzx r9d, r12w
004F0D34  45 8B C4                        mov r8d, r12d
004F0D37  45 0F B7 3A                     movzx r15d, word ptr [r10]
004F0D3B  66 45 3B C7                     cmp r8w, r15w
004F0D3F  73 1A                           jae 0x1404f0d5b
004F0D41  41 0F B7 C0                     movzx eax, r8w
004F0D45  4D 39 64 C2 08                  cmp qword ptr [r10 + rax*8 + 8], r12
004F0D4A  74 0F                           je 0x1404f0d5b
004F0D4C  8B C7                           mov eax, edi
004F0D4E  41 03 FD                        add edi, r13d
004F0D51  66 45 03 CD                     add r9w, r13w
004F0D55  66 44 89 44 44 60               mov word ptr [rsp + rax*2 + 0x60], r8w
004F0D5B  45 03 C5                        add r8d, r13d
004F0D5E  41 83 F8 20                     cmp r8d, 0x20
004F0D62  72 D7                           jb 0x1404f0d3b
004F0D64  66 44 89 4C 24 46               mov word ptr [rsp + 0x46], r9w
004F0D6A  48 85 F6                        test rsi, rsi
004F0D6D  75 1A                           jne 0x1404f0d89
004F0D6F  8B C2                           mov eax, edx
004F0D71  48 8D 4C 24 46                  lea rcx, [rsp + 0x46]
004F0D76  48 03 C0                        add rax, rax
004F0D79  41 03 D5                        add edx, r13d
004F0D7C  48 89 0C C3                     mov qword ptr [rbx + rax*8], rcx
004F0D80  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F0D89  41 0F B7 C9                     movzx ecx, r9w
004F0D8D  42 8D 04 19                     lea eax, [rcx + r11]
004F0D91  44 3B D8                        cmp r11d, eax
004F0D94  73 57                           jae 0x1404f0ded
004F0D96  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
004F0D9B  44 8B D1                        mov r10d, ecx
004F0D9E  4F 8D 04 58                     lea r8, [r8 + r11*2]
004F0DA2  45 0F B7 08                     movzx r9d, word ptr [r8]
004F0DA6  8D 4A 01                        lea ecx, [rdx + 1]
004F0DA9  8B C2                           mov eax, edx
004F0DAB  48 03 C9                        add rcx, rcx
004F0DAE  48 03 C0                        add rax, rax
004F0DB1  4C 89 04 C3                     mov qword ptr [rbx + rax*8], r8
004F0DB5  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F0DBE  66 45 3B 0E                     cmp r9w, word ptr [r14]
004F0DC2  73 09                           jae 0x1404f0dcd
004F0DC4  49 FF C1                        inc r9
004F0DC7  4F 8D 0C CE                     lea r9, [r14 + r9*8]
004F0DCB  EB 07                           jmp 0x1404f0dd4
004F0DCD  4C 8D 0D A4 6C 97 00            lea r9, [rip + 0x976ca4]
004F0DD4  83 C2 02                        add edx, 2
004F0DD7  4C 89 0C CB                     mov qword ptr [rbx + rcx*8], r9
004F0DDB  49 83 C0 02                     add r8, 2
004F0DDF  48 C7 44 CB 08 08 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 8
004F0DE8  4D 2B D5                        sub r10, r13
004F0DEB  75 B5                           jne 0x1404f0da2
004F0DED  4C 8B B5 78 02 00 00            mov r14, qword ptr [rbp + 0x278]
004F0DF4  48 85 F6                        test rsi, rsi
004F0DF7  4D 8B D6                        mov r10, r14
004F0DFA  44 8B DF                        mov r11d, edi
004F0DFD  4C 0F 45 D6                     cmovne r10, rsi
004F0E01  45 0F B7 CC                     movzx r9d, r12w
004F0E05  45 8B C4                        mov r8d, r12d
004F0E08  45 0F B7 3A                     movzx r15d, word ptr [r10]
004F0E0C  66 45 3B C7                     cmp r8w, r15w
004F0E10  73 1A                           jae 0x1404f0e2c
004F0E12  41 0F B7 C0                     movzx eax, r8w
004F0E16  4D 39 64 C2 08                  cmp qword ptr [r10 + rax*8 + 8], r12
004F0E1B  74 0F                           je 0x1404f0e2c
004F0E1D  8B C7                           mov eax, edi
004F0E1F  41 03 FD                        add edi, r13d
004F0E22  66 45 03 CD                     add r9w, r13w
004F0E26  66 44 89 44 44 60               mov word ptr [rsp + rax*2 + 0x60], r8w
004F0E2C  45 03 C5                        add r8d, r13d
004F0E2F  41 83 F8 20                     cmp r8d, 0x20
004F0E33  72 D7                           jb 0x1404f0e0c
004F0E35  66 44 89 4C 24 48               mov word ptr [rsp + 0x48], r9w
004F0E3B  48 85 F6                        test rsi, rsi
004F0E3E  75 1A                           jne 0x1404f0e5a
004F0E40  8B C2                           mov eax, edx
004F0E42  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
004F0E47  48 03 C0                        add rax, rax
004F0E4A  41 03 D5                        add edx, r13d
004F0E4D  48 89 0C C3                     mov qword ptr [rbx + rax*8], rcx
004F0E51  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F0E5A  41 0F B7 C9                     movzx ecx, r9w
004F0E5E  42 8D 04 19                     lea eax, [rcx + r11]
004F0E62  44 3B D8                        cmp r11d, eax
004F0E65  73 57                           jae 0x1404f0ebe
004F0E67  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
004F0E6C  44 8B D1                        mov r10d, ecx
004F0E6F  4F 8D 04 58                     lea r8, [r8 + r11*2]
004F0E73  45 0F B7 08                     movzx r9d, word ptr [r8]
004F0E77  8D 4A 01                        lea ecx, [rdx + 1]
004F0E7A  8B C2                           mov eax, edx
004F0E7C  48 03 C9                        add rcx, rcx
004F0E7F  48 03 C0                        add rax, rax
004F0E82  4C 89 04 C3                     mov qword ptr [rbx + rax*8], r8
004F0E86  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F0E8F  66 45 3B 0E                     cmp r9w, word ptr [r14]
004F0E93  73 09                           jae 0x1404f0e9e
004F0E95  49 FF C1                        inc r9
004F0E98  4F 8D 0C CE                     lea r9, [r14 + r9*8]
004F0E9C  EB 07                           jmp 0x1404f0ea5
004F0E9E  4C 8D 0D D3 6B 97 00            lea r9, [rip + 0x976bd3]
004F0EA5  83 C2 02                        add edx, 2
004F0EA8  4C 89 0C CB                     mov qword ptr [rbx + rcx*8], r9
004F0EAC  49 83 C0 02                     add r8, 2
004F0EB0  48 C7 44 CB 08 08 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 8
004F0EB9  4D 2B D5                        sub r10, r13
004F0EBC  75 B5                           jne 0x1404f0e73
004F0EBE  4C 8B B5 80 02 00 00            mov r14, qword ptr [rbp + 0x280]
004F0EC5  48 85 F6                        test rsi, rsi
004F0EC8  4D 8B D6                        mov r10, r14
004F0ECB  44 8B DF                        mov r11d, edi
004F0ECE  4C 0F 45 D6                     cmovne r10, rsi
004F0ED2  45 0F B7 CC                     movzx r9d, r12w
004F0ED6  45 8B C4                        mov r8d, r12d
004F0ED9  45 0F B7 3A                     movzx r15d, word ptr [r10]
004F0EDD  66 45 3B C7                     cmp r8w, r15w
004F0EE1  73 1A                           jae 0x1404f0efd
004F0EE3  41 0F B7 C0                     movzx eax, r8w
004F0EE7  4D 39 64 C2 08                  cmp qword ptr [r10 + rax*8 + 8], r12
004F0EEC  74 0F                           je 0x1404f0efd
004F0EEE  8B C7                           mov eax, edi
004F0EF0  41 03 FD                        add edi, r13d
004F0EF3  66 45 03 CD                     add r9w, r13w
004F0EF7  66 44 89 44 44 60               mov word ptr [rsp + rax*2 + 0x60], r8w
004F0EFD  45 03 C5                        add r8d, r13d
004F0F00  41 83 F8 20                     cmp r8d, 0x20
004F0F04  72 D7                           jb 0x1404f0edd
004F0F06  66 44 89 4C 24 4A               mov word ptr [rsp + 0x4a], r9w
004F0F0C  48 85 F6                        test rsi, rsi
004F0F0F  75 1A                           jne 0x1404f0f2b
004F0F11  8B C2                           mov eax, edx
004F0F13  48 8D 4C 24 4A                  lea rcx, [rsp + 0x4a]
004F0F18  48 03 C0                        add rax, rax
004F0F1B  41 03 D5                        add edx, r13d
004F0F1E  48 89 0C C3                     mov qword ptr [rbx + rax*8], rcx
004F0F22  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F0F2B  41 0F B7 C9                     movzx ecx, r9w
004F0F2F  42 8D 04 19                     lea eax, [rcx + r11]
004F0F33  44 3B D8                        cmp r11d, eax
004F0F36  73 57                           jae 0x1404f0f8f
004F0F38  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
004F0F3D  44 8B D1                        mov r10d, ecx
004F0F40  4F 8D 04 58                     lea r8, [r8 + r11*2]
004F0F44  45 0F B7 08                     movzx r9d, word ptr [r8]
004F0F48  8D 4A 01                        lea ecx, [rdx + 1]
004F0F4B  8B C2                           mov eax, edx
004F0F4D  48 03 C9                        add rcx, rcx
004F0F50  48 03 C0                        add rax, rax
004F0F53  4C 89 04 C3                     mov qword ptr [rbx + rax*8], r8
004F0F57  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F0F60  66 45 3B 0E                     cmp r9w, word ptr [r14]
004F0F64  73 09                           jae 0x1404f0f6f
004F0F66  49 FF C1                        inc r9
004F0F69  4F 8D 0C CE                     lea r9, [r14 + r9*8]
004F0F6D  EB 07                           jmp 0x1404f0f76
004F0F6F  4C 8D 0D 02 6B 97 00            lea r9, [rip + 0x976b02]
004F0F76  83 C2 02                        add edx, 2
004F0F79  4C 89 0C CB                     mov qword ptr [rbx + rcx*8], r9
004F0F7D  49 83 C0 02                     add r8, 2
004F0F81  48 C7 44 CB 08 08 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 8
004F0F8A  4D 2B D5                        sub r10, r13
004F0F8D  75 B5                           jne 0x1404f0f44
004F0F8F  4C 8B B5 88 02 00 00            mov r14, qword ptr [rbp + 0x288]
004F0F96  48 85 F6                        test rsi, rsi
004F0F99  4D 8B D6                        mov r10, r14
004F0F9C  44 8B DF                        mov r11d, edi
004F0F9F  4C 0F 45 D6                     cmovne r10, rsi
004F0FA3  45 0F B7 CC                     movzx r9d, r12w
004F0FA7  45 8B C4                        mov r8d, r12d
004F0FAA  45 0F B7 3A                     movzx r15d, word ptr [r10]
004F0FAE  66 45 3B C7                     cmp r8w, r15w
004F0FB2  73 1A                           jae 0x1404f0fce
004F0FB4  41 0F B7 C0                     movzx eax, r8w
004F0FB8  4D 39 64 C2 08                  cmp qword ptr [r10 + rax*8 + 8], r12
004F0FBD  74 0F                           je 0x1404f0fce
004F0FBF  8B C7                           mov eax, edi
004F0FC1  41 03 FD                        add edi, r13d
004F0FC4  66 45 03 CD                     add r9w, r13w
004F0FC8  66 44 89 44 44 60               mov word ptr [rsp + rax*2 + 0x60], r8w
004F0FCE  45 03 C5                        add r8d, r13d
004F0FD1  41 83 F8 20                     cmp r8d, 0x20
004F0FD5  72 D7                           jb 0x1404f0fae
004F0FD7  66 44 89 4C 24 4C               mov word ptr [rsp + 0x4c], r9w
004F0FDD  48 85 F6                        test rsi, rsi
004F0FE0  75 1A                           jne 0x1404f0ffc
004F0FE2  8B C2                           mov eax, edx
004F0FE4  48 8D 4C 24 4C                  lea rcx, [rsp + 0x4c]
004F0FE9  48 03 C0                        add rax, rax
004F0FEC  41 03 D5                        add edx, r13d
004F0FEF  48 89 0C C3                     mov qword ptr [rbx + rax*8], rcx
004F0FF3  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F0FFC  41 0F B7 C9                     movzx ecx, r9w
004F1000  42 8D 04 19                     lea eax, [rcx + r11]
004F1004  44 3B D8                        cmp r11d, eax
004F1007  73 57                           jae 0x1404f1060
004F1009  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
004F100E  44 8B D1                        mov r10d, ecx
004F1011  4F 8D 04 58                     lea r8, [r8 + r11*2]
004F1015  45 0F B7 08                     movzx r9d, word ptr [r8]
004F1019  8D 4A 01                        lea ecx, [rdx + 1]
004F101C  8B C2                           mov eax, edx
004F101E  48 03 C9                        add rcx, rcx
004F1021  48 03 C0                        add rax, rax
004F1024  4C 89 04 C3                     mov qword ptr [rbx + rax*8], r8
004F1028  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F1031  66 45 3B 0E                     cmp r9w, word ptr [r14]
004F1035  73 09                           jae 0x1404f1040
004F1037  49 FF C1                        inc r9
004F103A  4F 8D 0C CE                     lea r9, [r14 + r9*8]
004F103E  EB 07                           jmp 0x1404f1047
004F1040  4C 8D 0D 31 6A 97 00            lea r9, [rip + 0x976a31]
004F1047  83 C2 02                        add edx, 2
004F104A  4C 89 0C CB                     mov qword ptr [rbx + rcx*8], r9
004F104E  49 83 C0 02                     add r8, 2
004F1052  48 C7 44 CB 08 08 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 8
004F105B  4D 2B D5                        sub r10, r13
004F105E  75 B5                           jne 0x1404f1015
004F1060  4C 8B B5 90 02 00 00            mov r14, qword ptr [rbp + 0x290]
004F1067  48 85 F6                        test rsi, rsi
004F106A  4D 8B D6                        mov r10, r14
004F106D  44 8B DF                        mov r11d, edi
004F1070  4C 0F 45 D6                     cmovne r10, rsi
004F1074  45 0F B7 CC                     movzx r9d, r12w
004F1078  45 8B C4                        mov r8d, r12d
004F107B  45 0F B7 3A                     movzx r15d, word ptr [r10]
004F107F  66 45 3B C7                     cmp r8w, r15w
004F1083  73 1A                           jae 0x1404f109f
004F1085  41 0F B7 C0                     movzx eax, r8w
004F1089  4D 39 64 C2 08                  cmp qword ptr [r10 + rax*8 + 8], r12
004F108E  74 0F                           je 0x1404f109f
004F1090  8B C7                           mov eax, edi
004F1092  41 03 FD                        add edi, r13d
004F1095  66 45 03 CD                     add r9w, r13w
004F1099  66 44 89 44 44 60               mov word ptr [rsp + rax*2 + 0x60], r8w
004F109F  45 03 C5                        add r8d, r13d
004F10A2  41 83 F8 20                     cmp r8d, 0x20
004F10A6  72 D7                           jb 0x1404f107f
004F10A8  66 44 89 4C 24 4E               mov word ptr [rsp + 0x4e], r9w
004F10AE  48 85 F6                        test rsi, rsi
004F10B1  75 1A                           jne 0x1404f10cd
004F10B3  8B C2                           mov eax, edx
004F10B5  48 8D 4C 24 4E                  lea rcx, [rsp + 0x4e]
004F10BA  48 03 C0                        add rax, rax
004F10BD  41 03 D5                        add edx, r13d
004F10C0  48 89 0C C3                     mov qword ptr [rbx + rax*8], rcx
004F10C4  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F10CD  41 0F B7 C9                     movzx ecx, r9w
004F10D1  42 8D 04 19                     lea eax, [rcx + r11]
004F10D5  44 3B D8                        cmp r11d, eax
004F10D8  73 57                           jae 0x1404f1131
004F10DA  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
004F10DF  44 8B D1                        mov r10d, ecx
004F10E2  4F 8D 04 58                     lea r8, [r8 + r11*2]
004F10E6  45 0F B7 08                     movzx r9d, word ptr [r8]
004F10EA  8D 4A 01                        lea ecx, [rdx + 1]
004F10ED  8B C2                           mov eax, edx
004F10EF  48 03 C9                        add rcx, rcx
004F10F2  48 03 C0                        add rax, rax
004F10F5  4C 89 04 C3                     mov qword ptr [rbx + rax*8], r8
004F10F9  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F1102  66 45 3B 0E                     cmp r9w, word ptr [r14]
004F1106  73 09                           jae 0x1404f1111
004F1108  49 FF C1                        inc r9
004F110B  4F 8D 0C CE                     lea r9, [r14 + r9*8]
004F110F  EB 07                           jmp 0x1404f1118
004F1111  4C 8D 0D 60 69 97 00            lea r9, [rip + 0x976960]
004F1118  83 C2 02                        add edx, 2
004F111B  4C 89 0C CB                     mov qword ptr [rbx + rcx*8], r9
004F111F  49 83 C0 02                     add r8, 2
004F1123  48 C7 44 CB 08 08 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 8
004F112C  4D 2B D5                        sub r10, r13
004F112F  75 B5                           jne 0x1404f10e6
004F1131  4C 8B B5 98 02 00 00            mov r14, qword ptr [rbp + 0x298]
004F1138  48 85 F6                        test rsi, rsi
004F113B  4D 8B D6                        mov r10, r14
004F113E  44 8B DF                        mov r11d, edi
004F1141  4C 0F 45 D6                     cmovne r10, rsi
004F1145  45 0F B7 CC                     movzx r9d, r12w
004F1149  45 8B C4                        mov r8d, r12d
004F114C  45 0F B7 3A                     movzx r15d, word ptr [r10]
004F1150  66 45 3B C7                     cmp r8w, r15w
004F1154  73 1A                           jae 0x1404f1170
004F1156  41 0F B7 C0                     movzx eax, r8w
004F115A  4D 39 64 C2 08                  cmp qword ptr [r10 + rax*8 + 8], r12
004F115F  74 0F                           je 0x1404f1170
004F1161  8B C7                           mov eax, edi
004F1163  41 03 FD                        add edi, r13d
004F1166  66 45 03 CD                     add r9w, r13w
004F116A  66 44 89 44 44 60               mov word ptr [rsp + rax*2 + 0x60], r8w
004F1170  45 03 C5                        add r8d, r13d
004F1173  41 83 F8 20                     cmp r8d, 0x20
004F1177  72 D7                           jb 0x1404f1150
004F1179  66 44 89 4C 24 50               mov word ptr [rsp + 0x50], r9w
004F117F  48 85 F6                        test rsi, rsi
004F1182  75 1A                           jne 0x1404f119e
004F1184  8B C2                           mov eax, edx
004F1186  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
004F118B  48 03 C0                        add rax, rax
004F118E  41 03 D5                        add edx, r13d
004F1191  48 89 0C C3                     mov qword ptr [rbx + rax*8], rcx
004F1195  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F119E  41 0F B7 C9                     movzx ecx, r9w
004F11A2  42 8D 04 19                     lea eax, [rcx + r11]
004F11A6  44 3B D8                        cmp r11d, eax
004F11A9  73 57                           jae 0x1404f1202
004F11AB  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
004F11B0  44 8B D1                        mov r10d, ecx
004F11B3  4F 8D 04 58                     lea r8, [r8 + r11*2]
004F11B7  45 0F B7 08                     movzx r9d, word ptr [r8]
004F11BB  8D 4A 01                        lea ecx, [rdx + 1]
004F11BE  8B C2                           mov eax, edx
004F11C0  48 03 C9                        add rcx, rcx
004F11C3  48 03 C0                        add rax, rax
004F11C6  4C 89 04 C3                     mov qword ptr [rbx + rax*8], r8
004F11CA  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F11D3  66 45 3B 0E                     cmp r9w, word ptr [r14]
004F11D7  73 09                           jae 0x1404f11e2
004F11D9  49 FF C1                        inc r9
004F11DC  4F 8D 0C CE                     lea r9, [r14 + r9*8]
004F11E0  EB 07                           jmp 0x1404f11e9
004F11E2  4C 8D 0D 8F 68 97 00            lea r9, [rip + 0x97688f]
004F11E9  83 C2 02                        add edx, 2
004F11EC  4C 89 0C CB                     mov qword ptr [rbx + rcx*8], r9
004F11F0  49 83 C0 02                     add r8, 2
004F11F4  48 C7 44 CB 08 08 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 8
004F11FD  4D 2B D5                        sub r10, r13
004F1200  75 B5                           jne 0x1404f11b7
004F1202  4C 8B B5 A0 02 00 00            mov r14, qword ptr [rbp + 0x2a0]
004F1209  48 85 F6                        test rsi, rsi
004F120C  4D 8B D6                        mov r10, r14
004F120F  44 8B DF                        mov r11d, edi
004F1212  4C 0F 45 D6                     cmovne r10, rsi
004F1216  45 0F B7 CC                     movzx r9d, r12w
004F121A  45 8B C4                        mov r8d, r12d
004F121D  45 0F B7 3A                     movzx r15d, word ptr [r10]
004F1221  66 45 3B C7                     cmp r8w, r15w
004F1225  73 1A                           jae 0x1404f1241
004F1227  41 0F B7 C0                     movzx eax, r8w
004F122B  4D 39 64 C2 08                  cmp qword ptr [r10 + rax*8 + 8], r12
004F1230  74 0F                           je 0x1404f1241
004F1232  8B C7                           mov eax, edi
004F1234  41 03 FD                        add edi, r13d
004F1237  66 45 03 CD                     add r9w, r13w
004F123B  66 44 89 44 44 60               mov word ptr [rsp + rax*2 + 0x60], r8w
004F1241  45 03 C5                        add r8d, r13d
004F1244  41 83 F8 20                     cmp r8d, 0x20
004F1248  72 D7                           jb 0x1404f1221
004F124A  66 44 89 4C 24 52               mov word ptr [rsp + 0x52], r9w
004F1250  48 85 F6                        test rsi, rsi
004F1253  75 1A                           jne 0x1404f126f
004F1255  8B C2                           mov eax, edx
004F1257  48 8D 4C 24 52                  lea rcx, [rsp + 0x52]
004F125C  48 03 C0                        add rax, rax
004F125F  41 03 D5                        add edx, r13d
004F1262  48 89 0C C3                     mov qword ptr [rbx + rax*8], rcx
004F1266  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F126F  41 0F B7 C9                     movzx ecx, r9w
004F1273  41 8D 04 0B                     lea eax, [r11 + rcx]
004F1277  44 3B D8                        cmp r11d, eax
004F127A  73 57                           jae 0x1404f12d3
004F127C  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
004F1281  44 8B D1                        mov r10d, ecx
004F1284  4F 8D 04 58                     lea r8, [r8 + r11*2]
004F1288  45 0F B7 08                     movzx r9d, word ptr [r8]
004F128C  8D 4A 01                        lea ecx, [rdx + 1]
004F128F  8B C2                           mov eax, edx
004F1291  48 03 C9                        add rcx, rcx
004F1294  48 03 C0                        add rax, rax
004F1297  4C 89 04 C3                     mov qword ptr [rbx + rax*8], r8
004F129B  48 C7 44 C3 08 02 00 00 00      mov qword ptr [rbx + rax*8 + 8], 2
004F12A4  66 45 3B 0E                     cmp r9w, word ptr [r14]
004F12A8  73 09                           jae 0x1404f12b3
004F12AA  49 FF C1                        inc r9
004F12AD  4F 8D 0C CE                     lea r9, [r14 + r9*8]
004F12B1  EB 07                           jmp 0x1404f12ba
004F12B3  4C 8D 0D BE 67 97 00            lea r9, [rip + 0x9767be]
004F12BA  83 C2 02                        add edx, 2
004F12BD  4C 89 0C CB                     mov qword ptr [rbx + rcx*8], r9
004F12C1  49 83 C0 02                     add r8, 2
004F12C5  48 C7 44 CB 08 08 00 00 00      mov qword ptr [rbx + rcx*8 + 8], 8
004F12CE  4D 2B D5                        sub r10, r13
004F12D1  75 B5                           jne 0x1404f1288
004F12D3  48 8B 0D 0E 71 A1 00            mov rcx, qword ptr [rip + 0xa1710e]
004F12DA  45 33 C9                        xor r9d, r9d
004F12DD  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
004F12E2  45 33 C0                        xor r8d, r8d
004F12E5  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
004F12E9  48 8D 15 B0 A7 B2 FF            lea rdx, [rip - 0x4d5850]
004F12F0  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
004F12F5  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
004F12FA  E8 D1 DD D6 FF                  call 0x14025f0d0
004F12FF  48 8B 8D E0 01 00 00            mov rcx, qword ptr [rbp + 0x1e0]
004F1306  48 33 CC                        xor rcx, rsp
004F1309  E8 32 B3 1B 00                  call 0x1406ac640
004F130E  48 8B 9C 24 30 03 00 00         mov rbx, qword ptr [rsp + 0x330]
004F1316  48 81 C4 F0 02 00 00            add rsp, 0x2f0
004F131D  41 5F                           pop r15
004F131F  41 5E                           pop r14
004F1321  41 5D                           pop r13
004F1323  41 5C                           pop r12
004F1325  5F                              pop rdi
004F1326  5E                              pop rsi
004F1327  5D                              pop rbp
004F1328  C3                              ret
004F1329  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmEventTraceCoreParkingSelectionEx(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m2C8;
    unsigned __int16 v_stack_m2D6;
    unsigned __int16 v_stack_m2D8;
    unsigned __int16 v_stack_m2DA;
    unsigned __int16 v_stack_m2DC;
    unsigned __int16 v_stack_m2DE;
    unsigned __int16 v_stack_m2E0;
    unsigned __int16 v_stack_m2E2;
    unsigned __int16 v_stack_m2E4;
    unsigned __int16 v_stack_m2E6;
    unsigned __int16 v_stack_m2E8;
    unsigned __int64 v_stack_m2F0;
    unsigned int v_stack_m2F8;
    unsigned __int64 v_stack_m300;
    unsigned __int64 v_stack_m308;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (752);
    result = (*(unsigned __int64 *)(v_rip + 9542974)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 552 + 480) = result;
    v_r12 = 0;
    if (*(unsigned __int64 *)(v_rip + 9924701) == 0) goto loc_004F12FF;
    if ((*(unsigned __int8 *)(v_rip + 9924621)) == 0) goto loc_004F12FF;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 10582447), v_rip - 5066656, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_004F12FF;
loc_004F0A5D:
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(a1)))) goto loc_004F0A7B;
    result = 0;
    v_rdi = 0;
    if ((*(unsigned __int64 *)(a1 + 0 * 8 + 8)) != 0) {
        result = 0;
        v_rdi = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
        a3 = (unsigned __int16)((0) + ((unsigned __int16)(v_r12 + 1)));
        *(unsigned __int16 *)(v_rsp + result * 2 + 96) = 0;
    }
    a2 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    if (a2 < 32) goto loc_004F0A5D;
    v_stack_m2E8 = (unsigned __int16)(a3);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701)) = v_stack_m2E8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + 8) = 2;
    if (0 >= ((unsigned __int16)(a3))) goto loc_004F0AF6;
loc_004F0AAB:
    a1 = ((unsigned int)((unsigned int)(v_r12 + 1)) + 1) + ((unsigned int)((unsigned int)(v_r12 + 1)) + 1);
    result = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12 + 1))))) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12 + 1)))));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8) = v_stack_m2C8;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8 + 8) = 2;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m2C8))) >= (*(unsigned __int16 *)(a1))) goto loc_004F0AD6;
    a3 = (*(unsigned __int16 *)(v_stack_m2C8)) + 1;
    goto loc_004F0ADD;
loc_004F0AD6:
loc_004F0ADD:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r12 + 1))) + (2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8) = v_rip + 9924507;
    a4 = (v_stack_m2C8) + (2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8 + 8) = 8;
    v_r10 = ((unsigned __int16)(a3)) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_004F0AAB;
loc_004F0AF6:
    result = ((unsigned int)(a2)) + ((unsigned int)(a2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8) = v_rsp - 552 + 568;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8 + 8) = 4;
    a1 = (a2 + 1) + (a2 + 1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8) = v_rsp - 552 + 576;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8 + 8) = 4;
    a1 = (a2 + 2) + (a2 + 2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8) = v_rsp - 552 + 584;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8 + 8) = 4;
    a1 = (a2 + 3) + (a2 + 3);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8) = v_rsp - 552 + 592;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8 + 8) = 4;
    a1 = (a2 + 4) + (a2 + 4);
    a2 = (unsigned int)((a2) + (5));
    v_r14 = *(unsigned __int64 *)(v_rsp - 552 + 608);
    if (a1 != 0) { v_r14 = a1; }
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8) = v_rsp - 552 + 600;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8 + 8) = 4;
loc_004F0B99:
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_r14)))) goto loc_004F0BB9;
    result = 0;
    if ((*(unsigned __int64 *)(v_r14 + 0 * 8 + 8)) != 0) {
        result = (unsigned int)(v_rdi);
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_r12 + 1)));
        a4 = (unsigned __int16)((0) + ((unsigned __int16)(v_r12 + 1)));
        *(unsigned __int16 *)(v_rsp + result * 2 + 96) = 0;
    }
    a3 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    if (a3 < 32) goto loc_004F0B99;
    v_stack_m2E6 = (unsigned __int16)(a4);
    if (a1 == 0) {
        result = a2;
        a1 = v_stack_m2E6;
        result = (result) + (result);
        a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8) = a1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8 + 8) = 2;
    }
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= ((unsigned int)((unsigned __int16)(a4) + (unsigned int)((unsigned int)(v_rdi)) * 1))) goto loc_004F0C4B;
loc_004F0C00:
    a1 = (a2 + 1) + (a2 + 1);
    result = ((unsigned int)(a2)) + ((unsigned int)(a2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8) = v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8 + 8) = 2;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 552 + 608)))) goto loc_004F0C2B;
    a4 = (*(unsigned __int16 *)(v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2)) + 1;
    goto loc_004F0C32;
loc_004F0C2B:
loc_004F0C32:
    a2 = (unsigned int)((a2) + (2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8) = v_rip + 9924166;
    a3 = (v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2) + (2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8 + 8) = 8;
    v_r10 = ((unsigned int)((unsigned int)((unsigned __int16)(a4)))) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_004F0C00;
loc_004F0C4B:
    v_r10 = *(unsigned __int64 *)(v_rsp - 552 + 616);
    if (a1 != 0) { v_r10 = a1; }
loc_004F0C6A:
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_r10)))) goto loc_004F0C8A;
    result = 0;
    if ((*(unsigned __int64 *)(v_r10 + 0 * 8 + 8)) != 0) {
        result = (unsigned int)(v_rdi);
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_r12 + 1)));
        a4 = (unsigned __int16)((0) + ((unsigned __int16)(v_r12 + 1)));
        *(unsigned __int16 *)(v_rsp + result * 2 + 96) = 0;
    }
    a3 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    if (a3 < 32) goto loc_004F0C6A;
    v_stack_m2E4 = (unsigned __int16)(a4);
    if (a1 == 0) {
        result = a2;
        a1 = v_stack_m2E4;
        result = (result) + (result);
        a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8) = a1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8 + 8) = 2;
    }
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= ((unsigned int)((unsigned __int16)(a4) + (unsigned int)((unsigned int)(v_rdi)) * 1))) goto loc_004F0D1C;
loc_004F0CD1:
    a1 = (a2 + 1) + (a2 + 1);
    result = ((unsigned int)(a2)) + ((unsigned int)(a2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8) = v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8 + 8) = 2;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 552 + 616)))) goto loc_004F0CFC;
    a4 = (*(unsigned __int16 *)(v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2)) + 1;
    goto loc_004F0D03;
loc_004F0CFC:
loc_004F0D03:
    a2 = (unsigned int)((a2) + (2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8) = v_rip + 9923957;
    a3 = (v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2) + (2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8 + 8) = 8;
    v_r10 = ((unsigned int)((unsigned int)((unsigned __int16)(a4)))) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_004F0CD1;
loc_004F0D1C:
    v_r10 = *(unsigned __int64 *)(v_rsp - 552 + 624);
    if (a1 != 0) { v_r10 = a1; }
loc_004F0D3B:
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_r10)))) goto loc_004F0D5B;
    result = 0;
    if ((*(unsigned __int64 *)(v_r10 + 0 * 8 + 8)) != 0) {
        result = (unsigned int)(v_rdi);
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_r12 + 1)));
        a4 = (unsigned __int16)((0) + ((unsigned __int16)(v_r12 + 1)));
        *(unsigned __int16 *)(v_rsp + result * 2 + 96) = 0;
    }
    a3 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    if (a3 < 32) goto loc_004F0D3B;
    v_stack_m2E2 = (unsigned __int16)(a4);
    if (a1 == 0) {
        result = a2;
        a1 = v_stack_m2E2;
        result = (result) + (result);
        a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8) = a1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8 + 8) = 2;
    }
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= ((unsigned int)((unsigned __int16)(a4) + (unsigned int)((unsigned int)(v_rdi)) * 1))) goto loc_004F0DED;
loc_004F0DA2:
    a1 = (a2 + 1) + (a2 + 1);
    result = ((unsigned int)(a2)) + ((unsigned int)(a2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8) = v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8 + 8) = 2;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 552 + 624)))) goto loc_004F0DCD;
    a4 = (*(unsigned __int16 *)(v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2)) + 1;
    goto loc_004F0DD4;
loc_004F0DCD:
loc_004F0DD4:
    a2 = (unsigned int)((a2) + (2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8) = v_rip + 9923748;
    a3 = (v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2) + (2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8 + 8) = 8;
    v_r10 = ((unsigned int)((unsigned int)((unsigned __int16)(a4)))) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_004F0DA2;
loc_004F0DED:
    v_r10 = *(unsigned __int64 *)(v_rsp - 552 + 632);
    if (a1 != 0) { v_r10 = a1; }
loc_004F0E0C:
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_r10)))) goto loc_004F0E2C;
    result = 0;
    if ((*(unsigned __int64 *)(v_r10 + 0 * 8 + 8)) != 0) {
        result = (unsigned int)(v_rdi);
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_r12 + 1)));
        a4 = (unsigned __int16)((0) + ((unsigned __int16)(v_r12 + 1)));
        *(unsigned __int16 *)(v_rsp + result * 2 + 96) = 0;
    }
    a3 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    if (a3 < 32) goto loc_004F0E0C;
    v_stack_m2E0 = (unsigned __int16)(a4);
    if (a1 == 0) {
        result = a2;
        a1 = v_stack_m2E0;
        result = (result) + (result);
        a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8) = a1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8 + 8) = 2;
    }
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= ((unsigned int)((unsigned __int16)(a4) + (unsigned int)((unsigned int)(v_rdi)) * 1))) goto loc_004F0EBE;
loc_004F0E73:
    a1 = (a2 + 1) + (a2 + 1);
    result = ((unsigned int)(a2)) + ((unsigned int)(a2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8) = v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8 + 8) = 2;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 552 + 632)))) goto loc_004F0E9E;
    a4 = (*(unsigned __int16 *)(v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2)) + 1;
    goto loc_004F0EA5;
loc_004F0E9E:
loc_004F0EA5:
    a2 = (unsigned int)((a2) + (2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8) = v_rip + 9923539;
    a3 = (v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2) + (2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8 + 8) = 8;
    v_r10 = ((unsigned int)((unsigned int)((unsigned __int16)(a4)))) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_004F0E73;
loc_004F0EBE:
    v_r10 = *(unsigned __int64 *)(v_rsp - 552 + 640);
    if (a1 != 0) { v_r10 = a1; }
loc_004F0EDD:
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_r10)))) goto loc_004F0EFD;
    result = 0;
    if ((*(unsigned __int64 *)(v_r10 + 0 * 8 + 8)) != 0) {
        result = (unsigned int)(v_rdi);
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_r12 + 1)));
        a4 = (unsigned __int16)((0) + ((unsigned __int16)(v_r12 + 1)));
        *(unsigned __int16 *)(v_rsp + result * 2 + 96) = 0;
    }
    a3 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    if (a3 < 32) goto loc_004F0EDD;
    v_stack_m2DE = (unsigned __int16)(a4);
    if (a1 == 0) {
        result = a2;
        a1 = v_stack_m2DE;
        result = (result) + (result);
        a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8) = a1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8 + 8) = 2;
    }
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= ((unsigned int)((unsigned __int16)(a4) + (unsigned int)((unsigned int)(v_rdi)) * 1))) goto loc_004F0F8F;
loc_004F0F44:
    a1 = (a2 + 1) + (a2 + 1);
    result = ((unsigned int)(a2)) + ((unsigned int)(a2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8) = v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8 + 8) = 2;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 552 + 640)))) goto loc_004F0F6F;
    a4 = (*(unsigned __int16 *)(v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2)) + 1;
    goto loc_004F0F76;
loc_004F0F6F:
loc_004F0F76:
    a2 = (unsigned int)((a2) + (2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8) = v_rip + 9923330;
    a3 = (v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2) + (2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8 + 8) = 8;
    v_r10 = ((unsigned int)((unsigned int)((unsigned __int16)(a4)))) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_004F0F44;
loc_004F0F8F:
    v_r10 = *(unsigned __int64 *)(v_rsp - 552 + 648);
    if (a1 != 0) { v_r10 = a1; }
loc_004F0FAE:
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_r10)))) goto loc_004F0FCE;
    result = 0;
    if ((*(unsigned __int64 *)(v_r10 + 0 * 8 + 8)) != 0) {
        result = (unsigned int)(v_rdi);
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_r12 + 1)));
        a4 = (unsigned __int16)((0) + ((unsigned __int16)(v_r12 + 1)));
        *(unsigned __int16 *)(v_rsp + result * 2 + 96) = 0;
    }
    a3 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    if (a3 < 32) goto loc_004F0FAE;
    v_stack_m2DC = (unsigned __int16)(a4);
    if (a1 == 0) {
        result = a2;
        a1 = v_stack_m2DC;
        result = (result) + (result);
        a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8) = a1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8 + 8) = 2;
    }
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= ((unsigned int)((unsigned __int16)(a4) + (unsigned int)((unsigned int)(v_rdi)) * 1))) goto loc_004F1060;
loc_004F1015:
    a1 = (a2 + 1) + (a2 + 1);
    result = ((unsigned int)(a2)) + ((unsigned int)(a2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8) = v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8 + 8) = 2;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 552 + 648)))) goto loc_004F1040;
    a4 = (*(unsigned __int16 *)(v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2)) + 1;
    goto loc_004F1047;
loc_004F1040:
loc_004F1047:
    a2 = (unsigned int)((a2) + (2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8) = v_rip + 9923121;
    a3 = (v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2) + (2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8 + 8) = 8;
    v_r10 = ((unsigned int)((unsigned int)((unsigned __int16)(a4)))) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_004F1015;
loc_004F1060:
    v_r10 = *(unsigned __int64 *)(v_rsp - 552 + 656);
    if (a1 != 0) { v_r10 = a1; }
loc_004F107F:
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_r10)))) goto loc_004F109F;
    result = 0;
    if ((*(unsigned __int64 *)(v_r10 + 0 * 8 + 8)) != 0) {
        result = (unsigned int)(v_rdi);
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_r12 + 1)));
        a4 = (unsigned __int16)((0) + ((unsigned __int16)(v_r12 + 1)));
        *(unsigned __int16 *)(v_rsp + result * 2 + 96) = 0;
    }
    a3 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    if (a3 < 32) goto loc_004F107F;
    v_stack_m2DA = (unsigned __int16)(a4);
    if (a1 == 0) {
        result = a2;
        a1 = v_stack_m2DA;
        result = (result) + (result);
        a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8) = a1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8 + 8) = 2;
    }
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= ((unsigned int)((unsigned __int16)(a4) + (unsigned int)((unsigned int)(v_rdi)) * 1))) goto loc_004F1131;
loc_004F10E6:
    a1 = (a2 + 1) + (a2 + 1);
    result = ((unsigned int)(a2)) + ((unsigned int)(a2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8) = v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8 + 8) = 2;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 552 + 656)))) goto loc_004F1111;
    a4 = (*(unsigned __int16 *)(v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2)) + 1;
    goto loc_004F1118;
loc_004F1111:
loc_004F1118:
    a2 = (unsigned int)((a2) + (2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8) = v_rip + 9922912;
    a3 = (v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2) + (2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8 + 8) = 8;
    v_r10 = ((unsigned int)((unsigned int)((unsigned __int16)(a4)))) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_004F10E6;
loc_004F1131:
    v_r10 = *(unsigned __int64 *)(v_rsp - 552 + 664);
    if (a1 != 0) { v_r10 = a1; }
loc_004F1150:
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_r10)))) goto loc_004F1170;
    result = 0;
    if ((*(unsigned __int64 *)(v_r10 + 0 * 8 + 8)) != 0) {
        result = (unsigned int)(v_rdi);
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_r12 + 1)));
        a4 = (unsigned __int16)((0) + ((unsigned __int16)(v_r12 + 1)));
        *(unsigned __int16 *)(v_rsp + result * 2 + 96) = 0;
    }
    a3 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    if (a3 < 32) goto loc_004F1150;
    v_stack_m2D8 = (unsigned __int16)(a4);
    if (a1 == 0) {
        result = a2;
        a1 = v_stack_m2D8;
        result = (result) + (result);
        a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8) = a1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8 + 8) = 2;
    }
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= ((unsigned int)((unsigned __int16)(a4) + (unsigned int)((unsigned int)(v_rdi)) * 1))) goto loc_004F1202;
loc_004F11B7:
    a1 = (a2 + 1) + (a2 + 1);
    result = ((unsigned int)(a2)) + ((unsigned int)(a2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8) = v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8 + 8) = 2;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 552 + 664)))) goto loc_004F11E2;
    a4 = (*(unsigned __int16 *)(v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2)) + 1;
    goto loc_004F11E9;
loc_004F11E2:
loc_004F11E9:
    a2 = (unsigned int)((a2) + (2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8) = v_rip + 9922703;
    a3 = (v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2) + (2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8 + 8) = 8;
    v_r10 = ((unsigned int)((unsigned int)((unsigned __int16)(a4)))) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_004F11B7;
loc_004F1202:
    v_r10 = *(unsigned __int64 *)(v_rsp - 552 + 672);
    if (a1 != 0) { v_r10 = a1; }
loc_004F1221:
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(v_r10)))) goto loc_004F1241;
    result = 0;
    if ((*(unsigned __int64 *)(v_r10 + 0 * 8 + 8)) != 0) {
        result = (unsigned int)(v_rdi);
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_r12 + 1)));
        a4 = (unsigned __int16)((0) + ((unsigned __int16)(v_r12 + 1)));
        *(unsigned __int16 *)(v_rsp + result * 2 + 96) = 0;
    }
    a3 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    if (a3 < 32) goto loc_004F1221;
    v_stack_m2D6 = (unsigned __int16)(a4);
    if (a1 == 0) {
        result = a2;
        a1 = v_stack_m2D6;
        result = (result) + (result);
        a2 = (unsigned int)((a2) + ((unsigned int)(v_r12 + 1)));
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8) = a1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8 + 8) = 2;
    }
    if (((unsigned int)((unsigned int)((unsigned int)(v_rdi)))) >= ((unsigned int)((unsigned int)((unsigned int)(v_rdi)) + (unsigned __int16)(a4) * 1))) goto loc_004F12D3;
loc_004F1288:
    a1 = (a2 + 1) + (a2 + 1);
    result = ((unsigned int)(a2)) + ((unsigned int)(a2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8) = v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + result * 8 + 8) = 2;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2))) >= (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rsp - 552 + 672)))) goto loc_004F12B3;
    a4 = (*(unsigned __int16 *)(v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2)) + 1;
    goto loc_004F12BA;
loc_004F12B3:
loc_004F12BA:
    a2 = (unsigned int)((a2) + (2));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8) = v_rip + 9922494;
    a3 = (v_stack_m2C8 + (unsigned int)((unsigned int)(v_rdi)) * 2) + (2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9924701) + a1 * 8 + 8) = 8;
    v_r10 = ((unsigned int)((unsigned int)((unsigned __int16)(a4)))) - (v_r12 + 1);
    if (condition_is_not_equal) goto loc_004F1288;
loc_004F12D3:
    a4 = 0;
    v_stack_m2F0 = *(unsigned __int64 *)(v_rip + 9924701);
    a3 = 0;
    v_stack_m2F8 = a2;
    v_stack_m300 = 0;
    v_stack_m308 = 0;
    result = EtwWriteEx(*(unsigned __int64 *)(v_rip + 10580238), v_rip - 5068880, a3, a4);
loc_004F12FF:
    a1 = (*(unsigned __int64 *)(v_rsp - 552 + 480)) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip - 5068880, a3, a4);
    v_rsp = (v_rsp) + (752);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmEventTraceCoreParkingSelectionEx(void *Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m2C8;
    uint16_t v_stack_m2D6;
    uint16_t v_stack_m2D8;
    uint16_t v_stack_m2DA;
    uint16_t v_stack_m2DC;
    uint16_t v_stack_m2DE;
    uint16_t v_stack_m2E0;
    uint16_t v_stack_m2E2;
    uint16_t v_stack_m2E4;
    uint16_t v_stack_m2E6;
    uint16_t v_stack_m2E8;
    uint64_t v_stack_m2F0;
    uint32_t v_stack_m2F8;
    uint64_t v_stack_m300;
    uint64_t v_stack_m308;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (752);
    result = (*(uint64_t *)(v_rip + 0x919D3E)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x228 + 0x1E0) = result;
    local_r12 = 0;
    if (*(uint64_t *)(v_rip + 0x97705D) == 0) goto loc_004F12FF;
    if ((*(uint8_t *)(v_rip + 0x97700D)) == 0) goto loc_004F12FF;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xA179AF), v_rip - 5066656, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_004F12FF;
loc_004F0A5D:
    if (0 >= ((uint16_t)(*(uint16_t *)(arg1)))) goto loc_004F0A7B;
    result = 0;
    local_rdi = 0;
    if ((*(uint64_t *)(arg1 + 0x0 * 8 + 0x8)) != 0) {
        result = 0;
        local_rdi = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
        Arg3 = (uint16_t)((0) + ((uint16_t)(local_r12 + 1)));
        *(uint16_t *)(local_rsp + result * 2 + 0x60) = 0;
    }
    Arg2 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    if (Arg2 < 32) goto loc_004F0A5D;
    v_stack_m2E8 = (uint16_t)(Arg3);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D)) = v_stack_m2E8;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + 0x8) = 2;
    if (0 >= ((uint16_t)(Arg3))) goto loc_004F0AF6;
loc_004F0AAB:
    Arg1 = ((uint32_t)((uint32_t)(local_r12 + 1)) + 1) + ((uint32_t)((uint32_t)(local_r12 + 1)) + 1);
    result = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12 + 1))))) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12 + 1)))));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8) = v_stack_m2C8;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8 + 0x8) = 2;
    if (((uint16_t)(*(uint16_t *)(v_stack_m2C8))) >= (*(uint16_t *)(arg1))) goto loc_004F0AD6;
    Arg3 = (*(uint16_t *)(v_stack_m2C8)) + 1;
    goto loc_004F0ADD;
loc_004F0AD6:
loc_004F0ADD:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r12 + 1))) + (2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8) = v_rip + 9924507;
    Arg4 = (v_stack_m2C8) + (2);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8 + 0x8) = 8;
    local_r10 = ((uint16_t)(Arg3)) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_004F0AAB;
loc_004F0AF6:
    result = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8) = local_rsp - 552 + 568;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8 + 0x8) = 4;
    Arg1 = (Arg2 + 1) + (Arg2 + 1);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8) = local_rsp - 552 + 576;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8 + 0x8) = 4;
    Arg1 = (Arg2 + 2) + (Arg2 + 2);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8) = local_rsp - 552 + 584;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8 + 0x8) = 4;
    Arg1 = (Arg2 + 3) + (Arg2 + 3);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8) = local_rsp - 552 + 592;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8 + 0x8) = 4;
    Arg1 = (Arg2 + 4) + (Arg2 + 4);
    Arg2 = (uint32_t)((Arg2) + (5));
    local_r14 = *(uint64_t *)(local_rsp - 0x228 + 0x260);
    if (Arg1 != NULL) { local_r14 = Arg1; }
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8) = local_rsp - 552 + 600;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8 + 0x8) = 4;
loc_004F0B99:
    if (0 >= ((uint16_t)(*(uint16_t *)(local_r14)))) goto loc_004F0BB9;
    result = 0;
    if ((*(uint64_t *)(local_r14 + 0x0 * 8 + 0x8)) != 0) {
        result = (uint32_t)(local_rdi);
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_r12 + 1)));
        Arg4 = (uint16_t)((0) + ((uint16_t)(local_r12 + 1)));
        *(uint16_t *)(local_rsp + result * 2 + 0x60) = 0;
    }
    Arg3 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    if (Arg3 < 32) goto loc_004F0B99;
    v_stack_m2E6 = (uint16_t)(Arg4);
    if (Arg1 == NULL) {
        result = Arg2;
        Arg1 = v_stack_m2E6;
        result = (result) + (result);
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
        *(void **)(*(uint64_t *)(v_rip + 0x97705D) + result * 8) = Arg1;
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8 + 0x8) = 2;
    }
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= ((uint32_t)((uint16_t)(Arg4) + (uint32_t)((uint32_t)(local_rdi)) * 1))) goto loc_004F0C4B;
loc_004F0C00:
    Arg1 = (Arg2 + 1) + (Arg2 + 1);
    result = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8) = v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8 + 0x8) = 2;
    if (((uint16_t)(*(uint16_t *)(v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2))) >= (*(uint16_t *)(*(uint64_t *)(local_rsp - 0x228 + 0x260)))) goto loc_004F0C2B;
    Arg4 = (*(uint16_t *)(v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2)) + 1;
    goto loc_004F0C32;
loc_004F0C2B:
loc_004F0C32:
    Arg2 = (uint32_t)((Arg2) + (2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8) = v_rip + 9924166;
    Arg3 = (v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2) + (2);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8 + 0x8) = 8;
    local_r10 = ((uint32_t)((uint32_t)((uint16_t)(Arg4)))) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_004F0C00;
loc_004F0C4B:
    local_r10 = *(uint64_t *)(local_rsp - 0x228 + 0x268);
    if (Arg1 != NULL) { local_r10 = Arg1; }
loc_004F0C6A:
    if (0 >= ((uint16_t)(*(uint16_t *)(local_r10)))) goto loc_004F0C8A;
    result = 0;
    if ((*(uint64_t *)(local_r10 + 0x0 * 8 + 0x8)) != 0) {
        result = (uint32_t)(local_rdi);
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_r12 + 1)));
        Arg4 = (uint16_t)((0) + ((uint16_t)(local_r12 + 1)));
        *(uint16_t *)(local_rsp + result * 2 + 0x60) = 0;
    }
    Arg3 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    if (Arg3 < 32) goto loc_004F0C6A;
    v_stack_m2E4 = (uint16_t)(Arg4);
    if (Arg1 == NULL) {
        result = Arg2;
        Arg1 = v_stack_m2E4;
        result = (result) + (result);
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
        *(void **)(*(uint64_t *)(v_rip + 0x97705D) + result * 8) = Arg1;
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8 + 0x8) = 2;
    }
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= ((uint32_t)((uint16_t)(Arg4) + (uint32_t)((uint32_t)(local_rdi)) * 1))) goto loc_004F0D1C;
loc_004F0CD1:
    Arg1 = (Arg2 + 1) + (Arg2 + 1);
    result = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8) = v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8 + 0x8) = 2;
    if (((uint16_t)(*(uint16_t *)(v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2))) >= (*(uint16_t *)(*(uint64_t *)(local_rsp - 0x228 + 0x268)))) goto loc_004F0CFC;
    Arg4 = (*(uint16_t *)(v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2)) + 1;
    goto loc_004F0D03;
loc_004F0CFC:
loc_004F0D03:
    Arg2 = (uint32_t)((Arg2) + (2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8) = v_rip + 9923957;
    Arg3 = (v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2) + (2);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8 + 0x8) = 8;
    local_r10 = ((uint32_t)((uint32_t)((uint16_t)(Arg4)))) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_004F0CD1;
loc_004F0D1C:
    local_r10 = *(uint64_t *)(local_rsp - 0x228 + 0x270);
    if (Arg1 != NULL) { local_r10 = Arg1; }
loc_004F0D3B:
    if (0 >= ((uint16_t)(*(uint16_t *)(local_r10)))) goto loc_004F0D5B;
    result = 0;
    if ((*(uint64_t *)(local_r10 + 0x0 * 8 + 0x8)) != 0) {
        result = (uint32_t)(local_rdi);
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_r12 + 1)));
        Arg4 = (uint16_t)((0) + ((uint16_t)(local_r12 + 1)));
        *(uint16_t *)(local_rsp + result * 2 + 0x60) = 0;
    }
    Arg3 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    if (Arg3 < 32) goto loc_004F0D3B;
    v_stack_m2E2 = (uint16_t)(Arg4);
    if (Arg1 == NULL) {
        result = Arg2;
        Arg1 = v_stack_m2E2;
        result = (result) + (result);
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
        *(void **)(*(uint64_t *)(v_rip + 0x97705D) + result * 8) = Arg1;
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8 + 0x8) = 2;
    }
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= ((uint32_t)((uint16_t)(Arg4) + (uint32_t)((uint32_t)(local_rdi)) * 1))) goto loc_004F0DED;
loc_004F0DA2:
    Arg1 = (Arg2 + 1) + (Arg2 + 1);
    result = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8) = v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8 + 0x8) = 2;
    if (((uint16_t)(*(uint16_t *)(v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2))) >= (*(uint16_t *)(*(uint64_t *)(local_rsp - 0x228 + 0x270)))) goto loc_004F0DCD;
    Arg4 = (*(uint16_t *)(v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2)) + 1;
    goto loc_004F0DD4;
loc_004F0DCD:
loc_004F0DD4:
    Arg2 = (uint32_t)((Arg2) + (2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8) = v_rip + 9923748;
    Arg3 = (v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2) + (2);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8 + 0x8) = 8;
    local_r10 = ((uint32_t)((uint32_t)((uint16_t)(Arg4)))) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_004F0DA2;
loc_004F0DED:
    local_r10 = *(uint64_t *)(local_rsp - 0x228 + 0x278);
    if (Arg1 != NULL) { local_r10 = Arg1; }
loc_004F0E0C:
    if (0 >= ((uint16_t)(*(uint16_t *)(local_r10)))) goto loc_004F0E2C;
    result = 0;
    if ((*(uint64_t *)(local_r10 + 0x0 * 8 + 0x8)) != 0) {
        result = (uint32_t)(local_rdi);
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_r12 + 1)));
        Arg4 = (uint16_t)((0) + ((uint16_t)(local_r12 + 1)));
        *(uint16_t *)(local_rsp + result * 2 + 0x60) = 0;
    }
    Arg3 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    if (Arg3 < 32) goto loc_004F0E0C;
    v_stack_m2E0 = (uint16_t)(Arg4);
    if (Arg1 == NULL) {
        result = Arg2;
        Arg1 = v_stack_m2E0;
        result = (result) + (result);
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
        *(void **)(*(uint64_t *)(v_rip + 0x97705D) + result * 8) = Arg1;
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8 + 0x8) = 2;
    }
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= ((uint32_t)((uint16_t)(Arg4) + (uint32_t)((uint32_t)(local_rdi)) * 1))) goto loc_004F0EBE;
loc_004F0E73:
    Arg1 = (Arg2 + 1) + (Arg2 + 1);
    result = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8) = v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8 + 0x8) = 2;
    if (((uint16_t)(*(uint16_t *)(v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2))) >= (*(uint16_t *)(*(uint64_t *)(local_rsp - 0x228 + 0x278)))) goto loc_004F0E9E;
    Arg4 = (*(uint16_t *)(v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2)) + 1;
    goto loc_004F0EA5;
loc_004F0E9E:
loc_004F0EA5:
    Arg2 = (uint32_t)((Arg2) + (2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8) = v_rip + 9923539;
    Arg3 = (v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2) + (2);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8 + 0x8) = 8;
    local_r10 = ((uint32_t)((uint32_t)((uint16_t)(Arg4)))) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_004F0E73;
loc_004F0EBE:
    local_r10 = *(uint64_t *)(local_rsp - 0x228 + 0x280);
    if (Arg1 != NULL) { local_r10 = Arg1; }
loc_004F0EDD:
    if (0 >= ((uint16_t)(*(uint16_t *)(local_r10)))) goto loc_004F0EFD;
    result = 0;
    if ((*(uint64_t *)(local_r10 + 0x0 * 8 + 0x8)) != 0) {
        result = (uint32_t)(local_rdi);
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_r12 + 1)));
        Arg4 = (uint16_t)((0) + ((uint16_t)(local_r12 + 1)));
        *(uint16_t *)(local_rsp + result * 2 + 0x60) = 0;
    }
    Arg3 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    if (Arg3 < 32) goto loc_004F0EDD;
    v_stack_m2DE = (uint16_t)(Arg4);
    if (Arg1 == NULL) {
        result = Arg2;
        Arg1 = v_stack_m2DE;
        result = (result) + (result);
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
        *(void **)(*(uint64_t *)(v_rip + 0x97705D) + result * 8) = Arg1;
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8 + 0x8) = 2;
    }
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= ((uint32_t)((uint16_t)(Arg4) + (uint32_t)((uint32_t)(local_rdi)) * 1))) goto loc_004F0F8F;
loc_004F0F44:
    Arg1 = (Arg2 + 1) + (Arg2 + 1);
    result = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8) = v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8 + 0x8) = 2;
    if (((uint16_t)(*(uint16_t *)(v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2))) >= (*(uint16_t *)(*(uint64_t *)(local_rsp - 0x228 + 0x280)))) goto loc_004F0F6F;
    Arg4 = (*(uint16_t *)(v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2)) + 1;
    goto loc_004F0F76;
loc_004F0F6F:
loc_004F0F76:
    Arg2 = (uint32_t)((Arg2) + (2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8) = v_rip + 9923330;
    Arg3 = (v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2) + (2);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8 + 0x8) = 8;
    local_r10 = ((uint32_t)((uint32_t)((uint16_t)(Arg4)))) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_004F0F44;
loc_004F0F8F:
    local_r10 = *(uint64_t *)(local_rsp - 0x228 + 0x288);
    if (Arg1 != NULL) { local_r10 = Arg1; }
loc_004F0FAE:
    if (0 >= ((uint16_t)(*(uint16_t *)(local_r10)))) goto loc_004F0FCE;
    result = 0;
    if ((*(uint64_t *)(local_r10 + 0x0 * 8 + 0x8)) != 0) {
        result = (uint32_t)(local_rdi);
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_r12 + 1)));
        Arg4 = (uint16_t)((0) + ((uint16_t)(local_r12 + 1)));
        *(uint16_t *)(local_rsp + result * 2 + 0x60) = 0;
    }
    Arg3 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    if (Arg3 < 32) goto loc_004F0FAE;
    v_stack_m2DC = (uint16_t)(Arg4);
    if (Arg1 == NULL) {
        result = Arg2;
        Arg1 = v_stack_m2DC;
        result = (result) + (result);
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
        *(void **)(*(uint64_t *)(v_rip + 0x97705D) + result * 8) = Arg1;
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8 + 0x8) = 2;
    }
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= ((uint32_t)((uint16_t)(Arg4) + (uint32_t)((uint32_t)(local_rdi)) * 1))) goto loc_004F1060;
loc_004F1015:
    Arg1 = (Arg2 + 1) + (Arg2 + 1);
    result = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8) = v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8 + 0x8) = 2;
    if (((uint16_t)(*(uint16_t *)(v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2))) >= (*(uint16_t *)(*(uint64_t *)(local_rsp - 0x228 + 0x288)))) goto loc_004F1040;
    Arg4 = (*(uint16_t *)(v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2)) + 1;
    goto loc_004F1047;
loc_004F1040:
loc_004F1047:
    Arg2 = (uint32_t)((Arg2) + (2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8) = v_rip + 9923121;
    Arg3 = (v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2) + (2);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8 + 0x8) = 8;
    local_r10 = ((uint32_t)((uint32_t)((uint16_t)(Arg4)))) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_004F1015;
loc_004F1060:
    local_r10 = *(uint64_t *)(local_rsp - 0x228 + 0x290);
    if (Arg1 != NULL) { local_r10 = Arg1; }
loc_004F107F:
    if (0 >= ((uint16_t)(*(uint16_t *)(local_r10)))) goto loc_004F109F;
    result = 0;
    if ((*(uint64_t *)(local_r10 + 0x0 * 8 + 0x8)) != 0) {
        result = (uint32_t)(local_rdi);
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_r12 + 1)));
        Arg4 = (uint16_t)((0) + ((uint16_t)(local_r12 + 1)));
        *(uint16_t *)(local_rsp + result * 2 + 0x60) = 0;
    }
    Arg3 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    if (Arg3 < 32) goto loc_004F107F;
    v_stack_m2DA = (uint16_t)(Arg4);
    if (Arg1 == NULL) {
        result = Arg2;
        Arg1 = v_stack_m2DA;
        result = (result) + (result);
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
        *(void **)(*(uint64_t *)(v_rip + 0x97705D) + result * 8) = Arg1;
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8 + 0x8) = 2;
    }
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= ((uint32_t)((uint16_t)(Arg4) + (uint32_t)((uint32_t)(local_rdi)) * 1))) goto loc_004F1131;
loc_004F10E6:
    Arg1 = (Arg2 + 1) + (Arg2 + 1);
    result = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8) = v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8 + 0x8) = 2;
    if (((uint16_t)(*(uint16_t *)(v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2))) >= (*(uint16_t *)(*(uint64_t *)(local_rsp - 0x228 + 0x290)))) goto loc_004F1111;
    Arg4 = (*(uint16_t *)(v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2)) + 1;
    goto loc_004F1118;
loc_004F1111:
loc_004F1118:
    Arg2 = (uint32_t)((Arg2) + (2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8) = v_rip + 9922912;
    Arg3 = (v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2) + (2);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8 + 0x8) = 8;
    local_r10 = ((uint32_t)((uint32_t)((uint16_t)(Arg4)))) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_004F10E6;
loc_004F1131:
    local_r10 = *(uint64_t *)(local_rsp - 0x228 + 0x298);
    if (Arg1 != NULL) { local_r10 = Arg1; }
loc_004F1150:
    if (0 >= ((uint16_t)(*(uint16_t *)(local_r10)))) goto loc_004F1170;
    result = 0;
    if ((*(uint64_t *)(local_r10 + 0x0 * 8 + 0x8)) != 0) {
        result = (uint32_t)(local_rdi);
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_r12 + 1)));
        Arg4 = (uint16_t)((0) + ((uint16_t)(local_r12 + 1)));
        *(uint16_t *)(local_rsp + result * 2 + 0x60) = 0;
    }
    Arg3 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    if (Arg3 < 32) goto loc_004F1150;
    v_stack_m2D8 = (uint16_t)(Arg4);
    if (Arg1 == NULL) {
        result = Arg2;
        Arg1 = v_stack_m2D8;
        result = (result) + (result);
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
        *(void **)(*(uint64_t *)(v_rip + 0x97705D) + result * 8) = Arg1;
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8 + 0x8) = 2;
    }
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= ((uint32_t)((uint16_t)(Arg4) + (uint32_t)((uint32_t)(local_rdi)) * 1))) goto loc_004F1202;
loc_004F11B7:
    Arg1 = (Arg2 + 1) + (Arg2 + 1);
    result = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8) = v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8 + 0x8) = 2;
    if (((uint16_t)(*(uint16_t *)(v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2))) >= (*(uint16_t *)(*(uint64_t *)(local_rsp - 0x228 + 0x298)))) goto loc_004F11E2;
    Arg4 = (*(uint16_t *)(v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2)) + 1;
    goto loc_004F11E9;
loc_004F11E2:
loc_004F11E9:
    Arg2 = (uint32_t)((Arg2) + (2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8) = v_rip + 9922703;
    Arg3 = (v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2) + (2);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8 + 0x8) = 8;
    local_r10 = ((uint32_t)((uint32_t)((uint16_t)(Arg4)))) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_004F11B7;
loc_004F1202:
    local_r10 = *(uint64_t *)(local_rsp - 0x228 + 0x2A0);
    if (Arg1 != NULL) { local_r10 = Arg1; }
loc_004F1221:
    if (0 >= ((uint16_t)(*(uint16_t *)(local_r10)))) goto loc_004F1241;
    result = 0;
    if ((*(uint64_t *)(local_r10 + 0x0 * 8 + 0x8)) != 0) {
        result = (uint32_t)(local_rdi);
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_r12 + 1)));
        Arg4 = (uint16_t)((0) + ((uint16_t)(local_r12 + 1)));
        *(uint16_t *)(local_rsp + result * 2 + 0x60) = 0;
    }
    Arg3 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    if (Arg3 < 32) goto loc_004F1221;
    v_stack_m2D6 = (uint16_t)(Arg4);
    if (Arg1 == NULL) {
        result = Arg2;
        Arg1 = v_stack_m2D6;
        result = (result) + (result);
        Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r12 + 1)));
        *(void **)(*(uint64_t *)(v_rip + 0x97705D) + result * 8) = Arg1;
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8 + 0x8) = 2;
    }
    if (((uint32_t)((uint32_t)((uint32_t)(local_rdi)))) >= ((uint32_t)((uint32_t)((uint32_t)(local_rdi)) + (uint16_t)(Arg4) * 1))) goto loc_004F12D3;
loc_004F1288:
    Arg1 = (Arg2 + 1) + (Arg2 + 1);
    result = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8) = v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + result * 8 + 0x8) = 2;
    if (((uint16_t)(*(uint16_t *)(v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2))) >= (*(uint16_t *)(*(uint64_t *)(local_rsp - 0x228 + 0x2A0)))) goto loc_004F12B3;
    Arg4 = (*(uint16_t *)(v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2)) + 1;
    goto loc_004F12BA;
loc_004F12B3:
loc_004F12BA:
    Arg2 = (uint32_t)((Arg2) + (2));
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8) = v_rip + 9922494;
    Arg3 = (v_stack_m2C8 + (uint32_t)((uint32_t)(local_rdi)) * 2) + (2);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x97705D) + arg1 * 8 + 0x8) = 8;
    local_r10 = ((uint32_t)((uint32_t)((uint16_t)(Arg4)))) - (local_r12 + 1);
    if (condition_is_not_equal) goto loc_004F1288;
loc_004F12D3:
    Arg4 = 0;
    v_stack_m2F0 = *(uint64_t *)(v_rip + 0x97705D);
    Arg3 = 0;
    v_stack_m2F8 = Arg2;
    v_stack_m300 = 0;
    v_stack_m308 = 0;
    result = EtwWriteEx(*(uint64_t *)(v_rip + 0xA1710E), v_rip - 5068880, Arg3, Arg4);
loc_004F12FF:
    Arg1 = (*(uint64_t *)(local_rsp - 0x228 + 0x1E0)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip - 5068880, Arg3, Arg4);
    local_rsp = (local_rsp) + (752);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x0 + r8*8` | `64` | `R` |
| `Arg1` | `+ 0x8 + rax*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F09D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
