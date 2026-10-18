# XpressBuildHuffmanDecodingTable

- RVA: `0x003C8DA0`–`0x003C928C` (길이 `1,260` bytes)
- VA: `0x00000001403C8DA0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008F534`
- 디코드: `319`개 명령, `1,260/1,260` bytes 표시
- 미해석 바이트: `1` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_003C8840](Unknown_function_003C8840.md) at `0x003C888F`
- [sub_005EF68C](../5E/Unknown_function_005EF68C.md) at `0x005EF71F`

### Static image references
- `0x003C8F75` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003C8DA0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003C8DA5  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
003C8DAA  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
003C8DAF  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
003C8DB4  41 54                           push r12
003C8DB6  41 56                           push r14
003C8DB8  41 57                           push r15
003C8DBA  45 33 DB                        xor r11d, r11d
003C8DBD  41 BC 00 02 00 00               mov r12d, 0x200
003C8DC3  41 8B FC                        mov edi, r12d
003C8DC6  4C 8B FA                        mov r15, rdx
003C8DC9  C1 E7 10                        shl edi, 0x10
003C8DCC  4C 8B C1                        mov r8, rcx
003C8DCF  41 0B FC                        or edi, r12d
003C8DD2  45 8B D3                        mov r10d, r11d
003C8DD5  41 8B C3                        mov eax, r11d
003C8DD8  41 8B F3                        mov esi, r11d
003C8DDB  41 8B D3                        mov edx, r11d
003C8DDE  45 8B CB                        mov r9d, r11d
003C8DE1  41 8B EB                        mov ebp, r11d
003C8DE4  45 8B F3                        mov r14d, r11d
003C8DE7  66 0F 6E C7                     movd xmm0, edi
003C8DEB  66 0F 70 C0 00                  pshufd xmm0, xmm0, 0
003C8DF0  0F 11 81 00 04 00 00            movups xmmword ptr [rcx + 0x400], xmm0
003C8DF7  0F 11 81 10 04 00 00            movups xmmword ptr [rcx + 0x410], xmm0
003C8DFE  41 8B CB                        mov ecx, r11d
003C8E01  41 0F B6 3C 07                  movzx edi, byte ptr [r15 + rax]
003C8E06  49 8D 1C 07                     lea rbx, [r15 + rax]
003C8E0A  83 E7 0F                        and edi, 0xf
003C8E0D  74 20                           je 0x1403c8e2f
003C8E0F  41 0F B7 84 78 00 04 00 00      movzx eax, word ptr [r8 + rdi*2 + 0x400]
003C8E18  66 03 D2                        add dx, dx
003C8E1B  66 41 89 04 B0                  mov word ptr [r8 + rsi*4], ax
003C8E20  4C 8B CD                        mov r9, rbp
003C8E23  66 41 89 94 78 00 04 00 00      mov word ptr [r8 + rdi*2 + 0x400], dx
003C8E2C  49 8B CE                        mov rcx, r14
003C8E2F  0F B6 13                        movzx edx, byte ptr [rbx]
003C8E32  48 C1 EA 04                     shr rdx, 4
003C8E36  48 85 D2                        test rdx, rdx
003C8E39  74 1E                           je 0x1403c8e59
003C8E3B  41 0F B7 84 50 00 04 00 00      movzx eax, word ptr [r8 + rdx*2 + 0x400]
003C8E44  66 03 C9                        add cx, cx
003C8E47  66 FF C1                        inc cx
003C8E4A  66 43 89 44 88 02               mov word ptr [r8 + r9*4 + 2], ax
003C8E50  66 41 89 8C 50 00 04 00 00      mov word ptr [r8 + rdx*2 + 0x400], cx
003C8E59  49 FF C2                        inc r10
003C8E5C  49 8B C2                        mov rax, r10
003C8E5F  49 8B F2                        mov rsi, r10
003C8E62  49 8B D2                        mov rdx, r10
003C8E65  4D 8B CA                        mov r9, r10
003C8E68  49 8B EA                        mov rbp, r10
003C8E6B  49 8B CA                        mov rcx, r10
003C8E6E  4D 8B F2                        mov r14, r10
003C8E71  49 81 FA 00 01 00 00            cmp r10, 0x100
003C8E78  72 87                           jb 0x1403c8e01
003C8E7A  BF 00 FC FF FF                  mov edi, 0xfffffc00
003C8E7F  49 8D 98 1E 04 00 00            lea rbx, [r8 + 0x41e]
003C8E86  41 B9 00 04 00 00               mov r9d, 0x400
003C8E8C  41 BA 0F 00 00 00               mov r10d, 0xf
003C8E92  8D 4F 01                        lea ecx, [rdi + 1]
003C8E95  49 83 FA 0A                     cmp r10, 0xa
003C8E99  0F 86 84 00 00 00               jbe 0x1403c8f23
003C8E9F  66 3B CF                        cmp cx, di
003C8EA2  7D 30                           jge 0x1403c8ed4
003C8EA4  0F B7 C7                        movzx eax, di
003C8EA7  49 8D 90 20 0C 00 00            lea rdx, [r8 + 0xc20]
003C8EAE  66 2B C1                        sub ax, cx
003C8EB1  4A 8D 14 4A                     lea rdx, [rdx + r9*2]
003C8EB5  66 FF C8                        dec ax
003C8EB8  66 D1 E8                        shr ax, 1
003C8EBB  66 FF C0                        inc ax
003C8EBE  0F B7 C0                        movzx eax, ax
003C8EC1  4C 2B C8                        sub r9, rax
003C8EC4  66 89 0A                        mov word ptr [rdx], cx
003C8EC7  48 8D 52 FE                     lea rdx, [rdx - 2]
003C8ECB  66 83 C1 02                     add cx, 2
003C8ECF  66 3B CF                        cmp cx, di
003C8ED2  7C F0                           jl 0x1403c8ec4
003C8ED4  0F 84 FB 01 00 00               je 0x1403c90d5
003C8EDA  0F B7 13                        movzx edx, word ptr [rbx]
003C8EDD  8D 4F 01                        lea ecx, [rdi + 1]
003C8EE0  49 3B D4                        cmp rdx, r12
003C8EE3  74 2B                           je 0x1403c8f10
003C8EE5  49 8D B8 20 0C 00 00            lea rdi, [r8 + 0xc20]
003C8EEC  4A 8D 3C 4F                     lea rdi, [rdi + r9*2]
003C8EF0  0F B7 C2                        movzx eax, dx
003C8EF3  48 8D 7F FE                     lea rdi, [rdi - 2]
003C8EF7  66 C1 E0 04                     shl ax, 4
003C8EFB  49 FF C9                        dec r9
003C8EFE  66 41 03 C2                     add ax, r10w
003C8F02  66 89 47 02                     mov word ptr [rdi + 2], ax
003C8F06  41 0F B7 14 50                  movzx edx, word ptr [r8 + rdx*2]
003C8F0B  49 3B D4                        cmp rdx, r12
003C8F0E  75 E0                           jne 0x1403c8ef0
003C8F10  41 0F B7 F9                     movzx edi, r9w
003C8F14  49 FF CA                        dec r10
003C8F17  66 F7 DF                        neg di
003C8F1A  48 83 EB 02                     sub rbx, 2
003C8F1E  E9 72 FF FF FF                  jmp 0x1403c8e95
003C8F23  41 B9 FF 03 00 00               mov r9d, 0x3ff
003C8F29  66 3B CF                        cmp cx, di
003C8F2C  7D 32                           jge 0x1403c8f60
003C8F2E  0F B7 C7                        movzx eax, di
003C8F31  49 8D 90 1E 0C 00 00            lea rdx, [r8 + 0xc1e]
003C8F38  66 2B C1                        sub ax, cx
003C8F3B  66 FF C8                        dec ax
003C8F3E  66 D1 E8                        shr ax, 1
003C8F41  66 FF C0                        inc ax
003C8F44  0F B7 C0                        movzx eax, ax
003C8F47  4C 2B C8                        sub r9, rax
003C8F4A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
003C8F50  66 89 0A                        mov word ptr [rdx], cx
003C8F53  48 8D 52 FE                     lea rdx, [rdx - 2]
003C8F57  66 83 C1 02                     add cx, 2
003C8F5B  66 3B CF                        cmp cx, di
003C8F5E  7C F0                           jl 0x1403c8f50
003C8F60  0F 84 6F 01 00 00               je 0x1403c90d5
003C8F66  BB 0A 00 00 00                  mov ebx, 0xa
003C8F6B  49 8D B0 14 04 00 00            lea rsi, [r8 + 0x414]
003C8F72  41 8B FB                        mov edi, r11d
003C8F75  4C 8D 35 84 70 C3 FF            lea r14, [rip - 0x3c8f7c]
003C8F7C  8D 6B F7                        lea ebp, [rbx - 9]
003C8F7F  90                              nop
003C8F80  48 85 DB                        test rbx, rbx
003C8F83  0F 84 26 01 00 00               je 0x1403c90af
003C8F89  44 0F B7 16                     movzx r10d, word ptr [rsi]
003C8F8D  B9 0A 00 00 00                  mov ecx, 0xa
003C8F92  48 2B CB                        sub rcx, rbx
003C8F95  4D 3B D4                        cmp r10, r12
003C8F98  0F 84 BC 00 00 00               je 0x1403c905a
003C8F9E  45 0F B7 DA                     movzx r11d, r10w
003C8FA2  66 41 C1 E3 04                  shl r11w, 4
003C8FA7  66 44 03 DB                     add r11w, bx
003C8FAB  85 FF                           test edi, edi
003C8FAD  0F 85 22 01 00 00               jne 0x1403c90d5
003C8FB3  49 8D 41 01                     lea rax, [r9 + 1]
003C8FB7  48 D3 E0                        shl rax, cl
003C8FBA  48 3D 00 04 00 00               cmp rax, 0x400
003C8FC0  0F 87 0F 01 00 00               ja 0x1403c90d5
003C8FC6  49 8B D1                        mov rdx, r9
003C8FC9  48 8B C1                        mov rax, rcx
003C8FCC  48 D3 E2                        shl rdx, cl
003C8FCF  48 85 C9                        test rcx, rcx
003C8FD2  74 0E                           je 0x1403c8fe2
003C8FD4  48 3B CD                        cmp rcx, rbp
003C8FD7  75 22                           jne 0x1403c8ffb
003C8FD9  66 45 89 9C 50 22 04 00 00      mov word ptr [r8 + rdx*2 + 0x422], r11w
003C8FE2  4D 85 C9                        test r9, r9
003C8FE5  66 45 89 9C 50 20 04 00 00      mov word ptr [r8 + rdx*2 + 0x420], r11w
003C8FEE  47 0F B7 14 50                  movzx r10d, word ptr [r8 + r10*2]
003C8FF3  0F 44 FD                        cmove edi, ebp
003C8FF6  49 FF C9                        dec r9
003C8FF9  EB 9A                           jmp 0x1403c8f95
003C8FFB  48 83 F8 02                     cmp rax, 2
003C8FFF  75 14                           jne 0x1403c9015
003C9001  66 45 89 9C 50 26 04 00 00      mov word ptr [r8 + rdx*2 + 0x426], r11w
003C900A  66 45 89 9C 50 24 04 00 00      mov word ptr [r8 + rdx*2 + 0x424], r11w
003C9013  EB C4                           jmp 0x1403c8fd9
003C9015  48 83 E8 03                     sub rax, 3
003C9019  48 83 F8 06                     cmp rax, 6
003C901D  0F 87 32 02 00 00               ja 0x1403c9255
003C9023  41 8B 84 86 70 92 3C 00         mov eax, dword ptr [r14 + rax*4 + 0x3c9270]
003C902B  49 03 C6                        add rax, r14
003C902E  FF E0                           jmp rax
003C9030  CC                              int3
003C9031  CC                              int3
003C9032  CC                              int3
003C9033  CC                              int3
003C9034  66 45 89 9C 50 2E 04 00 00      mov word ptr [r8 + rdx*2 + 0x42e], r11w
003C903D  66 45 89 9C 50 2C 04 00 00      mov word ptr [r8 + rdx*2 + 0x42c], r11w
003C9046  66 45 89 9C 50 2A 04 00 00      mov word ptr [r8 + rdx*2 + 0x42a], r11w
003C904F  66 45 89 9C 50 28 04 00 00      mov word ptr [r8 + rdx*2 + 0x428], r11w
003C9058  EB A7                           jmp 0x1403c9001
003C905A  49 D1 E9                        shr r9, 1
003C905D  48 FF CB                        dec rbx
003C9060  48 83 EE 02                     sub rsi, 2
003C9064  E9 17 FF FF FF                  jmp 0x1403c8f80
003C9069  48 81 C2 11 02 00 00            add rdx, 0x211
003C9070  49 8D 04 50                     lea rax, [r8 + rdx*2]
003C9074  BA 04 00 00 00                  mov edx, 4
003C9079  0F 1F 80 00 00 00 00            nop dword ptr [rax]
003C9080  66 44 89 58 FE                  mov word ptr [rax - 2], r11w
003C9085  66 44 89 18                     mov word ptr [rax], r11w
003C9089  66 44 89 58 02                  mov word ptr [rax + 2], r11w
003C908E  66 44 89 58 04                  mov word ptr [rax + 4], r11w
003C9093  48 8D 40 08                     lea rax, [rax + 8]
003C9097  48 2B D5                        sub rdx, rbp
003C909A  75 E4                           jne 0x1403c9080
003C909C  47 0F B7 14 50                  movzx r10d, word ptr [r8 + r10*2]
003C90A1  4D 85 C9                        test r9, r9
003C90A4  0F 44 FD                        cmove edi, ebp
003C90A7  49 FF C9                        dec r9
003C90AA  E9 E6 FE FF FF                  jmp 0x1403c8f95
003C90AF  85 FF                           test edi, edi
003C90B1  0F 84 68 01 00 00               je 0x1403c921f
003C90B7  33 C0                           xor eax, eax
003C90B9  48 8B 5C 24 20                  mov rbx, qword ptr [rsp + 0x20]
003C90BE  48 8B 6C 24 28                  mov rbp, qword ptr [rsp + 0x28]
003C90C3  48 8B 74 24 30                  mov rsi, qword ptr [rsp + 0x30]
003C90C8  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
003C90CD  41 5F                           pop r15
003C90CF  41 5E                           pop r14
003C90D1  41 5C                           pop r12
003C90D3  C3                              ret
003C90D4  CC                              int3
003C90D5  B8 42 02 00 C0                  mov eax, 0xc0000242
003C90DA  EB DD                           jmp 0x1403c90b9
003C90DC  48 81 C2 11 02 00 00            add rdx, 0x211
003C90E3  49 8D 04 50                     lea rax, [r8 + rdx*2]
003C90E7  BA 08 00 00 00                  mov edx, 8
003C90EC  0F 1F 40 00                     nop dword ptr [rax]
003C90F0  66 44 89 58 FE                  mov word ptr [rax - 2], r11w
003C90F5  66 44 89 18                     mov word ptr [rax], r11w
003C90F9  66 44 89 58 02                  mov word ptr [rax + 2], r11w
003C90FE  66 44 89 58 04                  mov word ptr [rax + 4], r11w
003C9103  48 8D 40 08                     lea rax, [rax + 8]
003C9107  48 2B D5                        sub rdx, rbp
003C910A  75 E4                           jne 0x1403c90f0
003C910C  47 0F B7 14 50                  movzx r10d, word ptr [r8 + r10*2]
003C9111  4D 85 C9                        test r9, r9
003C9114  0F 44 FD                        cmove edi, ebp
003C9117  49 FF C9                        dec r9
003C911A  E9 76 FE FF FF                  jmp 0x1403c8f95
003C911F  48 81 C2 11 02 00 00            add rdx, 0x211
003C9126  49 8D 04 50                     lea rax, [r8 + rdx*2]
003C912A  BA 10 00 00 00                  mov edx, 0x10
003C912F  90                              nop
003C9130  66 44 89 58 FE                  mov word ptr [rax - 2], r11w
003C9135  66 44 89 18                     mov word ptr [rax], r11w
003C9139  66 44 89 58 02                  mov word ptr [rax + 2], r11w
003C913E  66 44 89 58 04                  mov word ptr [rax + 4], r11w
003C9143  48 8D 40 08                     lea rax, [rax + 8]
003C9147  48 2B D5                        sub rdx, rbp
003C914A  75 E4                           jne 0x1403c9130
003C914C  47 0F B7 14 50                  movzx r10d, word ptr [r8 + r10*2]
003C9151  4D 85 C9                        test r9, r9
003C9154  0F 44 FD                        cmove edi, ebp
003C9157  49 FF C9                        dec r9
003C915A  E9 36 FE FF FF                  jmp 0x1403c8f95
003C915F  48 81 C2 11 02 00 00            add rdx, 0x211
003C9166  49 8D 04 50                     lea rax, [r8 + rdx*2]
003C916A  BA 20 00 00 00                  mov edx, 0x20
003C916F  90                              nop
003C9170  66 44 89 58 FE                  mov word ptr [rax - 2], r11w
003C9175  66 44 89 18                     mov word ptr [rax], r11w
003C9179  66 44 89 58 02                  mov word ptr [rax + 2], r11w
003C917E  66 44 89 58 04                  mov word ptr [rax + 4], r11w
003C9183  48 8D 40 08                     lea rax, [rax + 8]
003C9187  48 2B D5                        sub rdx, rbp
003C918A  75 E4                           jne 0x1403c9170
003C918C  47 0F B7 14 50                  movzx r10d, word ptr [r8 + r10*2]
003C9191  4D 85 C9                        test r9, r9
003C9194  0F 44 FD                        cmove edi, ebp
003C9197  49 FF C9                        dec r9
003C919A  E9 F6 FD FF FF                  jmp 0x1403c8f95
003C919F  48 81 C2 11 02 00 00            add rdx, 0x211
003C91A6  49 8D 04 50                     lea rax, [r8 + rdx*2]
003C91AA  BA 40 00 00 00                  mov edx, 0x40
003C91AF  90                              nop
003C91B0  66 44 89 58 FE                  mov word ptr [rax - 2], r11w
003C91B5  66 44 89 18                     mov word ptr [rax], r11w
003C91B9  66 44 89 58 02                  mov word ptr [rax + 2], r11w
003C91BE  66 44 89 58 04                  mov word ptr [rax + 4], r11w
003C91C3  48 8D 40 08                     lea rax, [rax + 8]
003C91C7  48 2B D5                        sub rdx, rbp
003C91CA  75 E4                           jne 0x1403c91b0
003C91CC  47 0F B7 14 50                  movzx r10d, word ptr [r8 + r10*2]
003C91D1  4D 85 C9                        test r9, r9
003C91D4  0F 44 FD                        cmove edi, ebp
003C91D7  49 FF C9                        dec r9
003C91DA  E9 B6 FD FF FF                  jmp 0x1403c8f95
003C91DF  48 81 C2 11 02 00 00            add rdx, 0x211
003C91E6  49 8D 04 50                     lea rax, [r8 + rdx*2]
003C91EA  BA 80 00 00 00                  mov edx, 0x80
003C91EF  90                              nop
003C91F0  66 44 89 58 FE                  mov word ptr [rax - 2], r11w
003C91F5  66 44 89 18                     mov word ptr [rax], r11w
003C91F9  66 44 89 58 02                  mov word ptr [rax + 2], r11w
003C91FE  66 44 89 58 04                  mov word ptr [rax + 4], r11w
003C9203  48 8D 40 08                     lea rax, [rax + 8]
003C9207  48 2B D5                        sub rdx, rbp
003C920A  75 E4                           jne 0x1403c91f0
003C920C  47 0F B7 14 50                  movzx r10d, word ptr [r8 + r10*2]
003C9211  4D 85 C9                        test r9, r9
003C9214  0F 44 FD                        cmove edi, ebp
003C9217  49 FF C9                        dec r9
003C921A  E9 76 FD FF FF                  jmp 0x1403c8f95
003C921F  B8 02 00 00 00                  mov eax, 2
003C9224  49 8D 88 04 04 00 00            lea rcx, [r8 + 0x404]
003C922B  48 83 F8 0F                     cmp rax, 0xf
003C922F  76 2B                           jbe 0x1403c925c
003C9231  66 45 39 A0 02 04 00 00         cmp word ptr [r8 + 0x402], r12w
003C9239  0F 84 96 FE FF FF               je 0x1403c90d5
003C923F  49 8D B8 20 04 00 00            lea rdi, [r8 + 0x420]
003C9246  49 0F BF C3                     movsx rax, r11w
003C924A  49 8B CC                        mov rcx, r12
003C924D  66 F3 AB                        rep stosw word ptr [rdi], ax
003C9250  E9 62 FE FF FF                  jmp 0x1403c90b7
003C9255  B9 25 00 00 00                  mov ecx, 0x25
003C925A  CD 29                           int 0x29
003C925C  66 44 39 21                     cmp word ptr [rcx], r12w
003C9260  0F 85 6F FE FF FF               jne 0x1403c90d5
003C9266  48 FF C0                        inc rax
003C9269  48 83 C1 02                     add rcx, 2
003C926D  EB BC                           jmp 0x1403c922b
003C926F  90                              nop
003C9270  34 90                           xor al, 0x90
003C9272  3C 00                           cmp al, 0
003C9274  69 90 3C 00 DC 90 3C 00 1F 91   imul edx, dword ptr [rax - 0x6f23ffc4], 0x911f003c
003C927E  3C 00                           cmp al, 0
003C9280  5F                              pop rdi
003C9281  91                              xchg ecx, eax
003C9282  3C 00                           cmp al, 0
003C9284  9F                              lahf
003C9285  91                              xchg ecx, eax
003C9286  3C 00                           cmp al, 0
003C9288  DF                              .byte 0xdf
003C9289  91                              xchg ecx, eax
003C928A  3C 00                           cmp al, 0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall XpressBuildHuffmanDecodingTable(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_r11 = 0;
    v_rdi = (unsigned int)((512) << (16));
    v_rdi = (unsigned int)((v_rdi) | (512));
    *(unsigned __int64 *)(a1 + 1024) = v_xmm0;
    *(unsigned __int64 *)(a1 + 1040) = v_xmm0;
loc_003C8E01:
    v_rdi = (unsigned int)((*(unsigned __int8 *)(a2 + 0 * 1)) & (15));
    result = 0;
    if (!(condition_is_equal)) {
        result = *(unsigned __int16 *)(a1 + v_rdi * 2 + 1024);
        a2 = (unsigned __int16)((0) + (0));
        *(unsigned __int16 *)(a1 + 0 * 4) = (unsigned __int16)(result);
        a4 = 0;
        *(unsigned __int16 *)(a1 + v_rdi * 2 + 1024) = (unsigned __int16)(a2);
        a1 = 0;
    }
    a2 = (*(unsigned __int8 *)(a2 + 0 * 1)) >> (4);
    if (a2 != 0) {
        result = *(unsigned __int16 *)(a1 + a2 * 2 + 1024);
        a1 = (unsigned __int16)((a1) + ((unsigned __int16)(a1)));
        a1 = (unsigned __int16)((a1) + 1);
        *(unsigned __int16 *)(a1 + a4 * 4 + 2) = (unsigned __int16)(result);
        *(unsigned __int16 *)(a1 + a2 * 2 + 1024) = (unsigned __int16)(a1);
    }
    v_r10 = (0) + 1;
    if (v_r10 < 256) goto loc_003C8E01;
loc_003C8E95:
    if (15 <= 10) goto loc_003C8F23;
    if (((unsigned __int16)((unsigned int)(0xFFFFFC00ULL) + 1)) >= ((unsigned __int16)((unsigned int)(0xFFFFFC00ULL)))) goto loc_003C8ED4;
    result = (unsigned __int16)(((unsigned __int16)((unsigned int)(0xFFFFFC00ULL))) - ((unsigned __int16)((unsigned int)(0xFFFFFC00ULL) + 1)));
    result = (unsigned __int16)((result) - 1);
    result = (unsigned __int16)((result) >> (1));
    result = (unsigned __int16)((result) + 1);
    a4 = ((unsigned int)(0x400ULL)) - ((unsigned __int16)(result));
loc_003C8EC4:
    *(unsigned __int16 *)(a1 + 3104 + (unsigned int)(0x400ULL) * 2) = (unsigned __int16)((unsigned int)(0xFFFFFC00ULL) + 1);
    a1 = (unsigned __int16)(((unsigned int)(0xFFFFFC00ULL) + 1) + (2));
    if (((unsigned __int16)(a1)) < ((unsigned __int16)((unsigned int)(0xFFFFFC00ULL)))) goto loc_003C8EC4;
loc_003C8ED4:
    if (((unsigned __int16)(a1)) == ((unsigned __int16)((unsigned int)(0xFFFFFC00ULL)))) goto loc_003C90D5;
    if ((*(unsigned __int16 *)(a1 + 1054)) == 512) goto loc_003C8F10;
loc_003C8EF0:
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a1 + 1054))) << (4));
    a4 = (a4) - 1;
    result = (unsigned __int16)((result) + (15));
    *(unsigned __int16 *)(a1 + 3104 + a4 * 2 - 2 + 2) = (unsigned __int16)(result);
    if ((*(unsigned __int16 *)(a1 + *(unsigned __int16 *)(a1 + 1054) * 2)) != 512) goto loc_003C8EF0;
loc_003C8F10:
    v_r10 = (15) - 1;
    v_rdi = (unsigned __int16)(-((unsigned __int16)(a4)));
    v_rbx = (a1 + 1054) - (2);
    goto loc_003C8E95;
loc_003C8F23:
    if (((unsigned __int16)((unsigned int)(0xFFFFFC00ULL) + 1)) >= ((unsigned __int16)(v_rdi))) goto loc_003C8F60;
    result = (unsigned __int16)(((unsigned __int16)(v_rdi)) - ((unsigned __int16)((unsigned int)(0xFFFFFC00ULL) + 1)));
    result = (unsigned __int16)((result) - 1);
    result = (unsigned __int16)((result) >> (1));
    result = (unsigned __int16)((result) + 1);
    a4 = ((unsigned int)(0x3FFULL)) - ((unsigned __int16)(result));
loc_003C8F50:
    *(unsigned __int16 *)(a1 + 3102) = (unsigned __int16)((unsigned int)(0xFFFFFC00ULL) + 1);
    a1 = (unsigned __int16)(((unsigned int)(0xFFFFFC00ULL) + 1) + (2));
    if (((unsigned __int16)(a1)) < ((unsigned __int16)(v_rdi))) goto loc_003C8F50;
loc_003C8F60:
    if (((unsigned __int16)(a1)) == ((unsigned __int16)(v_rdi))) goto loc_003C90D5;
loc_003C8F80:
    if (10 == 0) goto loc_003C90AF;
    a1 = (10) - (10);
loc_003C8F95:
    if ((*(unsigned __int16 *)(a1 + 1044)) == 512) goto loc_003C905A;
    v_r11 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a1 + 1044))) << (4));
    v_r11 = (unsigned __int16)((v_r11) + (10));
    if (0 != 0) goto loc_003C90D5;
    result = (a4 + 1) << ((unsigned __int8)(a1));
    if (result > 0x400ULL) goto loc_003C90D5;
    a2 = (a4) << ((unsigned __int8)(a1));
    if (a1 == 0) goto loc_003C8FE2;
    if (a1 != (10 - 9)) goto loc_003C8FFB;
loc_003C8FD9:
    *(unsigned __int16 *)(a1 + a2 * 2 + 1058) = (unsigned __int16)(v_r11);
loc_003C8FE2:
    *(unsigned __int16 *)(a1 + a2 * 2 + 1056) = (unsigned __int16)(v_r11);
    v_rdi = 0;
    if (a4 == 0) { v_rdi = (unsigned int)(10 - 9); }
    a4 = (a4) - 1;
    goto loc_003C8F95;
loc_003C8FFB:
    if (a1 != 2) goto loc_003C9015;
loc_003C9001:
    *(unsigned __int16 *)(a1 + a2 * 2 + 1062) = (unsigned __int16)(v_r11);
    *(unsigned __int16 *)(a1 + a2 * 2 + 1060) = (unsigned __int16)(v_r11);
    goto loc_003C8FD9;
loc_003C9015:
    result = (a1) - (3);
    if (result > 6) goto loc_003C9255;
    result = ((unsigned int)(*(unsigned int *)(v_rip - 3968892 + result * 4 + 3969648))) + (v_rip - 3968892);
loc_003C905A:
    a4 = (a4) >> (1);
    v_rbx = (10) - 1;
    v_rsi = (a1 + 1044) - (2);
    goto loc_003C8F80;
loc_003C90AF:
    if ((unsigned int)(v_rdi) == 0) goto loc_003C921F;
loc_003C90B7:
    result = 0;
loc_003C90B9:
    return result;
loc_003C90D5:
    goto loc_003C90B9;
loc_003C921F:
loc_003C922B:
    if (2 <= 15) goto loc_003C925C;
    if ((*(unsigned __int16 *)(a1 + 1026)) == 512) goto loc_003C90D5;
    goto loc_003C90B7;
loc_003C9255:
loc_003C925C:
    if ((*(unsigned __int16 *)(37)) != 512) goto loc_003C90D5;
    result = ((__int16)((unsigned __int16)(v_r11))) + 1;
    a1 = (37) + (2);
    goto loc_003C922B;
}
```

## 5. (Beta) C Style

```c
int64_t XpressBuildHuffmanDecodingTable(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_r11 = 0;
    local_rdi = (uint32_t)((512) << (16));
    local_rdi = (uint32_t)((local_rdi) | (512));
    *(uint64_t *)(arg1 + 0x400) = v_xmm0;
    *(uint64_t *)(arg1 + 0x410) = v_xmm0;
loc_003C8E01:
    local_rdi = (uint32_t)((*(uint8_t *)(arg2 + 0x0 * 1)) & (15));
    result = 0;
    if (!(condition_is_equal)) {
        result = *(uint16_t *)(arg1 + local_rdi * 2 + 0x400);
        Arg2 = (uint16_t)((0) + (0));
        *(uint16_t *)(arg1 + 0x0 * 4) = (uint16_t)(result);
        a4 = 0;
        *(uint16_t *)(arg1 + local_rdi * 2 + 0x400) = (uint16_t)(Arg2);
        Arg1 = 0;
    }
    Arg2 = (*(uint8_t *)(arg2 + 0x0 * 1)) >> (4);
    if (Arg2 != NULL) {
        result = *(uint16_t *)(arg1 + arg2 * 2 + 0x400);
        Arg1 = (uint16_t)((Arg1) + ((uint16_t)(Arg1)));
        Arg1 = (uint16_t)((Arg1) + 1);
        *(uint16_t *)(arg1 + a4 * 4 + 0x2) = (uint16_t)(result);
        *(uint16_t *)(arg1 + arg2 * 2 + 0x400) = (uint16_t)(Arg1);
    }
    local_r10 = (0) + 1;
    if (local_r10 < 256) goto loc_003C8E01;
loc_003C8E95:
    if (15 <= 10) goto loc_003C8F23;
    if (((uint16_t)((uint32_t)(0xFFFFFC00ULL) + 1)) >= ((uint16_t)((uint32_t)(0xFFFFFC00ULL)))) goto loc_003C8ED4;
    result = (uint16_t)(((uint16_t)((uint32_t)(0xFFFFFC00ULL))) - ((uint16_t)((uint32_t)(0xFFFFFC00ULL) + 1)));
    result = (uint16_t)((result) - 1);
    result = (uint16_t)((result) >> (1));
    result = (uint16_t)((result) + 1);
    a4 = ((uint32_t)(0x400ULL)) - ((uint16_t)(result));
loc_003C8EC4:
    *(uint16_t *)(arg1 + 0xC20 + (uint32_t)(0x400ULL) * 2) = (uint16_t)((uint32_t)(0xFFFFFC00ULL) + 1);
    Arg1 = (uint16_t)(((uint32_t)(0xFFFFFC00ULL) + 1) + (2));
    if (((uint16_t)(Arg1)) < ((uint16_t)((uint32_t)(0xFFFFFC00ULL)))) goto loc_003C8EC4;
loc_003C8ED4:
    if (((uint16_t)(Arg1)) == ((uint16_t)((uint32_t)(0xFFFFFC00ULL)))) goto loc_003C90D5;
    if ((*(uint16_t *)(arg1 + 0x41E)) == 512) goto loc_003C8F10;
loc_003C8EF0:
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(arg1 + 0x41E))) << (4));
    a4 = (a4) - 1;
    result = (uint16_t)((result) + (15));
    *(uint16_t *)(arg1 + 0xC20 + a4 * 2 - 0x2 + 0x2) = (uint16_t)(result);
    if ((*(uint16_t *)(arg1 + *(uint16_t *)(arg1 + 0x41E) * 2)) != 512) goto loc_003C8EF0;
loc_003C8F10:
    local_r10 = (15) - 1;
    local_rdi = (uint16_t)(-((uint16_t)(a4)));
    local_rbx = (Arg1 + 1054) - (2);
    goto loc_003C8E95;
loc_003C8F23:
    if (((uint16_t)((uint32_t)(0xFFFFFC00ULL) + 1)) >= ((uint16_t)(local_rdi))) goto loc_003C8F60;
    result = (uint16_t)(((uint16_t)(local_rdi)) - ((uint16_t)((uint32_t)(0xFFFFFC00ULL) + 1)));
    result = (uint16_t)((result) - 1);
    result = (uint16_t)((result) >> (1));
    result = (uint16_t)((result) + 1);
    a4 = ((uint32_t)(0x3FFULL)) - ((uint16_t)(result));
loc_003C8F50:
    *(uint16_t *)(arg1 + 0xC1E) = (uint16_t)((uint32_t)(0xFFFFFC00ULL) + 1);
    Arg1 = (uint16_t)(((uint32_t)(0xFFFFFC00ULL) + 1) + (2));
    if (((uint16_t)(Arg1)) < ((uint16_t)(local_rdi))) goto loc_003C8F50;
loc_003C8F60:
    if (((uint16_t)(Arg1)) == ((uint16_t)(local_rdi))) goto loc_003C90D5;
loc_003C8F80:
    if (10 == 0) goto loc_003C90AF;
    Arg1 = (10) - (10);
loc_003C8F95:
    if ((*(uint16_t *)(arg1 + 0x414)) == 512) goto loc_003C905A;
    local_r11 = (uint16_t)(((uint16_t)(*(uint16_t *)(arg1 + 0x414))) << (4));
    local_r11 = (uint16_t)((local_r11) + (10));
    if (0 != 0) goto loc_003C90D5;
    result = (a4 + 1) << ((uint8_t)(Arg1));
    if (result > 0x400ULL) goto loc_003C90D5;
    Arg2 = (a4) << ((uint8_t)(Arg1));
    if (Arg1 == NULL) goto loc_003C8FE2;
    if (Arg1 != (10 - 9)) goto loc_003C8FFB;
loc_003C8FD9:
    *(uint16_t *)(arg1 + arg2 * 2 + 0x422) = (uint16_t)(local_r11);
loc_003C8FE2:
    *(uint16_t *)(arg1 + arg2 * 2 + 0x420) = (uint16_t)(local_r11);
    local_rdi = 0;
    if (a4 == 0) { local_rdi = (uint32_t)(10 - 9); }
    a4 = (a4) - 1;
    goto loc_003C8F95;
loc_003C8FFB:
    if (Arg1 != 2) goto loc_003C9015;
loc_003C9001:
    *(uint16_t *)(arg1 + arg2 * 2 + 0x426) = (uint16_t)(local_r11);
    *(uint16_t *)(arg1 + arg2 * 2 + 0x424) = (uint16_t)(local_r11);
    goto loc_003C8FD9;
loc_003C9015:
    result = (Arg1) - (3);
    if (result > 6) goto loc_003C9255;
    result = ((uint32_t)(*(uint32_t *)(v_rip - 0x3C8F7C + result * 4 + 0x3C9270))) + (v_rip - 3968892);
loc_003C905A:
    a4 = (a4) >> (1);
    local_rbx = (10) - 1;
    local_rsi = (Arg1 + 1044) - (2);
    goto loc_003C8F80;
loc_003C90AF:
    if ((uint32_t)(local_rdi) == 0) goto loc_003C921F;
loc_003C90B7:
    result = 0;
loc_003C90B9:
    return result;
loc_003C90D5:
    goto loc_003C90B9;
loc_003C921F:
loc_003C922B:
    if (2 <= 15) goto loc_003C925C;
    if ((*(uint16_t *)(arg1 + 0x402)) == 512) goto loc_003C90D5;
    goto loc_003C90B7;
loc_003C9255:
loc_003C925C:
    if ((*(uint16_t *)(37)) != 512) goto loc_003C90D5;
    result = ((int16_t)((uint16_t)(local_r11))) + 1;
    Arg1 = (37) + (2);
    goto loc_003C922B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x2` | `64` | `R` |
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x0` | `16` | `W` |
| `Arg1` | `+ 0x0 + r10*2` | `16` | `R` |
| `Arg1` | `+ 0x0 + r9*2` | `64` | `R` |
| `Arg1` | `+ 0x0 + rdx*2` | `16` | `R` |
| `Arg1` | `+ 0x0 + rsi*4` | `16` | `W` |
| `Arg1` | `+ 0x2` | `16` | `W` |
| `Arg1` | `+ 0x2 + r9*4` | `16` | `W` |
| `Arg1` | `+ 0x400` | `128` | `R` |
| `Arg1` | `+ 0x400 + rdi*2` | `16` | `R` |
| `Arg1` | `+ 0x400 + rdi*2` | `16` | `W` |
| `Arg1` | `+ 0x400 + rdx*2` | `16` | `R` |
| `Arg1` | `+ 0x400 + rdx*2` | `16` | `W` |
| `Arg1` | `+ 0x402` | `16` | `R` |
| `Arg1` | `+ 0x404` | `64` | `R` |
| `Arg1` | `+ 0x410` | `128` | `R` |
| `Arg1` | `+ 0x414` | `64` | `R` |
| `Arg1` | `+ 0x41E` | `64` | `R` |
| `Arg1` | `+ 0x420` | `64` | `R` |
| `Arg1` | `+ 0x420 + rdx*2` | `16` | `W` |
| `Arg1` | `+ 0x422 + rdx*2` | `16` | `W` |
| `Arg1` | `+ 0x424 + rdx*2` | `16` | `W` |
| `Arg1` | `+ 0x426 + rdx*2` | `16` | `W` |
| `Arg1` | `+ 0xC1E` | `64` | `R` |
| `Arg1` | `+ 0xC20` | `64` | `R` |
| `Arg2` | `+ 0x0` | `8` | `R` |
| `Arg2` | `+ 0x0 + rax*1` | `8` | `R` |
| `Arg2` | `+ 0x0 + rax*1` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003C8DA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
