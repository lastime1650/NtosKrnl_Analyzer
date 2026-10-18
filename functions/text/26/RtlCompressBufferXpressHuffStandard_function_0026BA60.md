# RtlCompressBufferXpressHuffStandard

- RVA: `0x0026BA60`–`0x0026C2AE` (길이 `2,126` bytes)
- VA: `0x000000014026BA60`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065548`
- 디코드: `515`개 명령, `2,126/2,126` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0026BB55` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0026BC2A` → [XpressBuildHuffmanEncodings](XpressBuildHuffmanEncodings_function_0026C2C0.md) (function, `0x0026C2C0`)
- `0x0026C1A5` → [XpressDoHuffmanPass](XpressDoHuffmanPass_function_0026C6E0.md) (function, `0x0026C6E0`)
- `0x0026C27F` → [RtlpMakeXpressCallback](../41/RtlpMakeXpressCallback_function_0041A7F0.md) (function, `0x0041A7F0`)
- `0x0026C29C` → [RtlpMakeXpressCallback](../41/RtlpMakeXpressCallback_function_0041A7F0.md) (function, `0x0041A7F0`)

### Direct callers
- [RtlCompressBufferXpressHuff](RtlCompressBufferXpressHuff_function_0026B9A0.md) at `0x0026B9F8`
- [RtlCompressBufferProgress](../5E/RtlCompressBufferProgress_function_005EF3C0.md) at `0x005EF505`

### Static image references
- `0x0026BE3C` → RVA `0x00010650` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0026BA60  4C 8B DC                        mov r11, rsp
0026BA63  49 89 5B 20                     mov qword ptr [r11 + 0x20], rbx
0026BA67  4D 89 43 18                     mov qword ptr [r11 + 0x18], r8
0026BA6B  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
0026BA6F  55                              push rbp
0026BA70  56                              push rsi
0026BA71  57                              push rdi
0026BA72  41 54                           push r12
0026BA74  41 55                           push r13
0026BA76  41 56                           push r14
0026BA78  41 57                           push r15
0026BA7A  48 81 EC A0 00 00 00            sub rsp, 0xa0
0026BA81  33 C0                           xor eax, eax
0026BA83  8B EA                           mov ebp, edx
0026BA85  4D 8B D0                        mov r10, r8
0026BA88  48 03 E9                        add rbp, rcx
0026BA8B  0F 57 C0                        xorps xmm0, xmm0
0026BA8E  48 89 6C 24 60                  mov qword ptr [rsp + 0x60], rbp
0026BA93  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
0026BA98  49 89 43 A8                     mov qword ptr [r11 - 0x58], rax
0026BA9C  4C 8B C1                        mov r8, rcx
0026BA9F  41 8B C1                        mov eax, r9d
0026BAA2  49 03 C2                        add rax, r10
0026BAA5  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0026BAAD  41 81 F9 2C 01 00 00            cmp r9d, 0x12c
0026BAB4  0F 82 A1 01 00 00               jb 0x14026bc5b
0026BABA  4C 8B B4 24 08 01 00 00         mov r14, qword ptr [rsp + 0x108]
0026BAC2  48 8B C1                        mov rax, rcx
0026BAC5  49 8B FE                        mov rdi, r14
0026BAC8  4C 89 54 24 68                  mov qword ptr [rsp + 0x68], r10
0026BACD  B9 F6 0A 00 00                  mov ecx, 0xaf6
0026BAD2  F3 48 AB                        rep stosq qword ptr [rdi], rax
0026BAD5  49 8D BE B0 57 00 00            lea rdi, [r14 + 0x57b0]
0026BADC  B9 EE 12 00 00                  mov ecx, 0x12ee
0026BAE1  F3 48 AB                        rep stosq qword ptr [rdi], rax
0026BAE4  48 8B F8                        mov rdi, rax
0026BAE7  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
0026BAEF  48 85 C0                        test rax, rax
0026BAF2  0F 84 FB 06 00 00               je 0x14026c1f3
0026BAF8  8B 8C 24 20 01 00 00            mov ecx, dword ptr [rsp + 0x120]
0026BAFF  3B CA                           cmp ecx, edx
0026BB01  0F 87 EC 06 00 00               ja 0x14026c1f3
0026BB07  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0026BB0C  4D 8D 8E 40 61 01 00            lea r9, [r14 + 0x16140]
0026BB13  48 8B 84 24 18 01 00 00         mov rax, qword ptr [rsp + 0x118]
0026BB1B  49 8D 9E 40 6A 01 00            lea rbx, [r14 + 0x16a40]
0026BB22  8B F1                           mov esi, ecx
0026BB24  33 D2                           xor edx, edx
0026BB26  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0026BB2B  89 8C 24 80 00 00 00            mov dword ptr [rsp + 0x80], ecx
0026BB32  48 89 B4 24 98 00 00 00         mov qword ptr [rsp + 0x98], rsi
0026BB3A  4C 8B EA                        mov r13, rdx
0026BB3D  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
0026BB42  4C 8B E2                        mov r12, rdx
0026BB45  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
0026BB4A  33 D2                           xor edx, edx
0026BB4C  41 B8 00 08 00 00               mov r8d, 0x800
0026BB52  49 8B C9                        mov rcx, r9
0026BB55  E8 E6 B0 45 00                  call 0x1406c6c40
0026BB5A  4C 8D 1C 3E                     lea r11, [rsi + rdi]
0026BB5E  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
0026BB63  48 8D 8F 00 00 01 00            lea rcx, [rdi + 0x10000]
0026BB6A  4C 8B FB                        mov r15, rbx
0026BB6D  48 3B CD                        cmp rcx, rbp
0026BB70  BE 01 00 00 00                  mov esi, 1
0026BB75  48 0F 47 CD                     cmova rcx, rbp
0026BB79  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
0026BB81  48 8D 51 D8                     lea rdx, [rcx - 0x28]
0026BB85  49 3B D3                        cmp rdx, r11
0026BB88  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
0026BB8D  4C 0F 42 DA                     cmovb r11, rdx
0026BB91  48 83 C3 04                     add rbx, 4
0026BB95  4C 89 5C 24 48                  mov qword ptr [rsp + 0x48], r11
0026BB9A  48 3B BC 24 E0 00 00 00         cmp rdi, qword ptr [rsp + 0xe0]
0026BBA2  75 1B                           jne 0x14026bbbf
0026BBA4  0F B6 07                        movzx eax, byte ptr [rdi]
0026BBA7  BE 02 00 00 00                  mov esi, 2
0026BBAC  41 FF 84 86 40 61 01 00         inc dword ptr [r14 + rax*4 + 0x16140]
0026BBB4  0F B6 07                        movzx eax, byte ptr [rdi]
0026BBB7  48 FF C7                        inc rdi
0026BBBA  88 03                           mov byte ptr [rbx], al
0026BBBC  48 FF C3                        inc rbx
0026BBBF  48 3B FA                        cmp rdi, rdx
0026BBC2  0F 82 B8 00 00 00               jb 0x14026bc80
0026BBC8  48 3B F9                        cmp rdi, rcx
0026BBCB  73 28                           jae 0x14026bbf5
0026BBCD  0F B6 07                        movzx eax, byte ptr [rdi]
0026BBD0  41 FF 84 86 40 61 01 00         inc dword ptr [r14 + rax*4 + 0x16140]
0026BBD8  0F B6 07                        movzx eax, byte ptr [rdi]
0026BBDB  48 FF C7                        inc rdi
0026BBDE  88 03                           mov byte ptr [rbx], al
0026BBE0  48 FF C3                        inc rbx
0026BBE3  8D 04 36                        lea eax, [rsi + rsi]
0026BBE6  85 F6                           test esi, esi
0026BBE8  0F 8E 35 06 00 00               jle 0x14026c223
0026BBEE  8B F0                           mov esi, eax
0026BBF0  48 3B F9                        cmp rdi, rcx
0026BBF3  72 D8                           jb 0x14026bbcd
0026BBF5  85 F6                           test esi, esi
0026BBF7  7E 0B                           jle 0x14026bc04
0026BBF9  8D 34 75 01 00 00 00            lea esi, [rsi*2 + 1]
0026BC00  85 F6                           test esi, esi
0026BC02  7F F5                           jg 0x14026bbf9
0026BC04  8D 04 75 01 00 00 00            lea eax, [rsi*2 + 1]
0026BC0B  41 89 07                        mov dword ptr [r15], eax
0026BC0E  48 3B FD                        cmp rdi, rbp
0026BC11  0F 82 E3 05 00 00               jb 0x14026c1fa
0026BC17  41 FF 86 40 65 01 00            inc dword ptr [r14 + 0x16540]
0026BC1E  BE 01 00 00 00                  mov esi, 1
0026BC23  49 8D 8E 20 EF 00 00            lea rcx, [r14 + 0xef20]
0026BC2A  E8 91 06 00 00                  call 0x14026c2c0
0026BC2F  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
0026BC34  48 8D 48 1F                     lea rcx, [rax + 0x1f]
0026BC38  49 03 CD                        add rcx, r13
0026BC3B  48 C1 E9 05                     shr rcx, 5
0026BC3F  49 8D 04 8C                     lea rax, [r12 + rcx*4]
0026BC43  49 8D 89 02 01 00 00            lea rcx, [r9 + 0x102]
0026BC4A  48 03 C8                        add rcx, rax
0026BC4D  48 3B 8C 24 90 00 00 00         cmp rcx, qword ptr [rsp + 0x90]
0026BC55  0F 82 32 05 00 00               jb 0x14026c18d
0026BC5B  B8 23 00 00 C0                  mov eax, 0xc0000023
0026BC60  48 8B 9C 24 F8 00 00 00         mov rbx, qword ptr [rsp + 0xf8]
0026BC68  48 81 C4 A0 00 00 00            add rsp, 0xa0
0026BC6F  41 5F                           pop r15
0026BC71  41 5E                           pop r14
0026BC73  41 5D                           pop r13
0026BC75  41 5C                           pop r12
0026BC77  5F                              pop rdi
0026BC78  5E                              pop rsi
0026BC79  5D                              pop rbp
0026BC7A  C3                              ret
0026BC7B  CC                              int3
0026BC7C  0F 1F 40 00                     nop dword ptr [rax]
0026BC80  0F B6 07                        movzx eax, byte ptr [rdi]
0026BC83  4C 8B D7                        mov r10, rdi
0026BC86  0F B6 4F 01                     movzx ecx, byte ptr [rdi + 1]
0026BC8A  49 8D 14 C6                     lea rdx, [r14 + rax*8]
0026BC8E  0F B6 47 02                     movzx eax, byte ptr [rdi + 2]
0026BC92  4C 8D 04 88                     lea r8, [rax + rcx*4]
0026BC96  49 8B C0                        mov rax, r8
0026BC99  48 03 C0                        add rax, rax
0026BC9C  4C 8B 0C C2                     mov r9, qword ptr [rdx + rax*8]
0026BCA0  48 89 3C C2                     mov qword ptr [rdx + rax*8], rdi
0026BCA4  0F B6 0F                        movzx ecx, byte ptr [rdi]
0026BCA7  41 38 09                        cmp byte ptr [r9], cl
0026BCAA  74 28                           je 0x14026bcd4
0026BCAC  41 0F B6 02                     movzx eax, byte ptr [r10]
0026BCB0  49 8D 7A 01                     lea rdi, [r10 + 1]
0026BCB4  41 FF 84 86 40 61 01 00         inc dword ptr [r14 + rax*4 + 0x16140]
0026BCBC  41 0F B6 02                     movzx eax, byte ptr [r10]
0026BCC0  88 03                           mov byte ptr [rbx], al
0026BCC2  48 FF C3                        inc rbx
0026BCC5  8D 04 36                        lea eax, [rsi + rsi]
0026BCC8  85 F6                           test esi, esi
0026BCCA  0F 8E 79 03 00 00               jle 0x14026c049
0026BCD0  8B F0                           mov esi, eax
0026BCD2  EB AC                           jmp 0x14026bc80
0026BCD4  0F B6 47 01                     movzx eax, byte ptr [rdi + 1]
0026BCD8  41 38 41 01                     cmp byte ptr [r9 + 1], al
0026BCDC  75 CE                           jne 0x14026bcac
0026BCDE  0F B6 47 02                     movzx eax, byte ptr [rdi + 2]
0026BCE2  41 38 41 02                     cmp byte ptr [r9 + 2], al
0026BCE6  75 C4                           jne 0x14026bcac
0026BCE8  48 8B C7                        mov rax, rdi
0026BCEB  49 2B C1                        sub rax, r9
0026BCEE  48 3D 00 00 01 00               cmp rax, 0x10000
0026BCF4  7D B6                           jge 0x14026bcac
0026BCF6  45 0F B6 59 03                  movzx r11d, byte ptr [r9 + 3]
0026BCFB  4C 8B E7                        mov r12, rdi
0026BCFE  0F B6 6F 03                     movzx ebp, byte ptr [rdi + 3]
0026BD02  41 3A EB                        cmp bpl, r11b
0026BD05  0F 85 D2 00 00 00               jne 0x14026bddd
0026BD0B  44 0F B6 6F 04                  movzx r13d, byte ptr [rdi + 4]
0026BD10  48 8D 47 04                     lea rax, [rdi + 4]
0026BD14  41 0F B6 69 04                  movzx ebp, byte ptr [r9 + 4]
0026BD19  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0026BD1E  44 3A ED                        cmp r13b, bpl
0026BD21  0F 85 06 02 00 00               jne 0x14026bf2d
0026BD27  0F B6 4F 05                     movzx ecx, byte ptr [rdi + 5]
0026BD2B  45 0F B6 69 05                  movzx r13d, byte ptr [r9 + 5]
0026BD30  88 8C 24 E8 00 00 00            mov byte ptr [rsp + 0xe8], cl
0026BD37  41 3A CD                        cmp cl, r13b
0026BD3A  0F 85 6B 02 00 00               jne 0x14026bfab
0026BD40  48 83 C7 06                     add rdi, 6
0026BD44  49 83 C1 06                     add r9, 6
0026BD48  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
0026BD4D  48 8D 41 D8                     lea rax, [rcx - 0x28]
0026BD51  48 3B F8                        cmp rdi, rax
0026BD54  0F 83 DD 04 00 00               jae 0x14026c237
0026BD5A  41 8B 09                        mov ecx, dword ptr [r9]
0026BD5D  8B 07                           mov eax, dword ptr [rdi]
0026BD5F  3B C1                           cmp eax, ecx
0026BD61  0F 85 95 01 00 00               jne 0x14026befc
0026BD67  41 8B 49 04                     mov ecx, dword ptr [r9 + 4]
0026BD6B  8B 47 04                        mov eax, dword ptr [rdi + 4]
0026BD6E  3B C1                           cmp eax, ecx
0026BD70  0F 85 7E 01 00 00               jne 0x14026bef4
0026BD76  41 8B 49 08                     mov ecx, dword ptr [r9 + 8]
0026BD7A  8B 47 08                        mov eax, dword ptr [rdi + 8]
0026BD7D  3B C1                           cmp eax, ecx
0026BD7F  0F 85 73 03 00 00               jne 0x14026c0f8
0026BD85  41 8B 49 0C                     mov ecx, dword ptr [r9 + 0xc]
0026BD89  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
0026BD8C  3B C1                           cmp eax, ecx
0026BD8E  0F 85 C5 03 00 00               jne 0x14026c159
0026BD94  41 8B 49 10                     mov ecx, dword ptr [r9 + 0x10]
0026BD98  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
0026BD9B  3B C1                           cmp eax, ecx
0026BD9D  0F 85 C3 03 00 00               jne 0x14026c166
0026BDA3  41 8B 49 14                     mov ecx, dword ptr [r9 + 0x14]
0026BDA7  8B 47 14                        mov eax, dword ptr [rdi + 0x14]
0026BDAA  3B C1                           cmp eax, ecx
0026BDAC  0F 85 CE 03 00 00               jne 0x14026c180
0026BDB2  41 8B 49 18                     mov ecx, dword ptr [r9 + 0x18]
0026BDB6  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
0026BDB9  3B C1                           cmp eax, ecx
0026BDBB  0F 85 B2 03 00 00               jne 0x14026c173
0026BDC1  41 8B 49 1C                     mov ecx, dword ptr [r9 + 0x1c]
0026BDC5  8B 47 1C                        mov eax, dword ptr [rdi + 0x1c]
0026BDC8  3B C1                           cmp eax, ecx
0026BDCA  0F 85 16 04 00 00               jne 0x14026c1e6
0026BDD0  48 83 C7 20                     add rdi, 0x20
0026BDD4  49 83 C1 20                     add r9, 0x20
0026BDD8  E9 6B FF FF FF                  jmp 0x14026bd48
0026BDDD  4E 8D 04 41                     lea r8, [rcx + r8*2]
0026BDE1  49 8D 04 28                     lea rax, [r8 + rbp]
0026BDE5  49 8B 8C C6 B0 57 00 00         mov rcx, qword ptr [r14 + rax*8 + 0x57b0]
0026BDED  4B 8D 04 18                     lea rax, [r8 + r11]
0026BDF1  4D 89 8C C6 B0 57 00 00         mov qword ptr [r14 + rax*8 + 0x57b0], r9
0026BDF9  48 8B C7                        mov rax, rdi
0026BDFC  48 2B C1                        sub rax, rcx
0026BDFF  48 3D 00 00 01 00               cmp rax, 0x10000
0026BE05  7D 0A                           jge 0x14026be11
0026BE07  8B 07                           mov eax, dword ptr [rdi]
0026BE09  3B 01                           cmp eax, dword ptr [rcx]
0026BE0B  0F 84 7F 02 00 00               je 0x14026c090
0026BE11  48 83 C7 03                     add rdi, 3
0026BE15  49 83 C1 03                     add r9, 3
0026BE19  4C 8B C7                        mov r8, rdi
0026BE1C  48 8B D7                        mov rdx, rdi
0026BE1F  4D 2B C4                        sub r8, r12
0026BE22  49 2B D1                        sub rdx, r9
0026BE25  49 83 F8 03                     cmp r8, 3
0026BE29  0F 84 FE 01 00 00               je 0x14026c02d
0026BE2F  48 81 FA 00 01 00 00            cmp rdx, 0x100
0026BE36  0F 83 9D 00 00 00               jae 0x14026bed9
0026BE3C  48 8D 05 0D 48 DA FF            lea rax, [rip - 0x25b7f3]
0026BE43  0F B6 0C 02                     movzx ecx, byte ptr [rdx + rax]
0026BE47  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
0026BE4C  4D 8D 48 FD                     lea r9, [r8 - 3]
0026BE50  4C 03 E9                        add r13, rcx
0026BE53  4C 8D 43 01                     lea r8, [rbx + 1]
0026BE57  B8 01 00 00 00                  mov eax, 1
0026BE5C  4C 89 6C 24 50                  mov qword ptr [rsp + 0x50], r13
0026BE61  48 D3 E0                        shl rax, cl
0026BE64  48 2B D0                        sub rdx, rax
0026BE67  C0 E1 04                        shl cl, 4
0026BE6A  49 8B C1                        mov rax, r9
0026BE6D  49 83 F9 0F                     cmp r9, 0xf
0026BE71  0F 83 30 02 00 00               jae 0x14026c0a7
0026BE77  02 C8                           add cl, al
0026BE79  88 0B                           mov byte ptr [rbx], cl
0026BE7B  49 8B D8                        mov rbx, r8
0026BE7E  0F B6 C1                        movzx eax, cl
0026BE81  41 FF 84 86 40 65 01 00         inc dword ptr [r14 + rax*4 + 0x16540]
0026BE89  8D 04 75 01 00 00 00            lea eax, [rsi*2 + 1]
0026BE90  66 89 13                        mov word ptr [rbx], dx
0026BE93  48 83 C3 02                     add rbx, 2
0026BE97  85 F6                           test esi, esi
0026BE99  0F 8E 66 02 00 00               jle 0x14026c105
0026BE9F  8B F0                           mov esi, eax
0026BEA1  4C 8B 5C 24 48                  mov r11, qword ptr [rsp + 0x48]
0026BEA6  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
0026BEAB  49 3B FB                        cmp rdi, r11
0026BEAE  0F 82 CC FD FF FF               jb 0x14026bc80
0026BEB4  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0026BEB9  48 3B F8                        cmp rdi, rax
0026BEBC  0F 82 CF 03 00 00               jb 0x14026c291
0026BEC2  4C 8B 64 24 38                  mov r12, qword ptr [rsp + 0x38]
0026BEC7  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
0026BECC  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
0026BED4  E9 EF FC FF FF                  jmp 0x14026bbc8
0026BED9  48 8B C2                        mov rax, rdx
0026BEDC  48 8D 0D 6D 47 DA FF            lea rcx, [rip - 0x25b893]
0026BEE3  48 C1 E8 08                     shr rax, 8
0026BEE7  0F B6 0C 08                     movzx ecx, byte ptr [rax + rcx]
0026BEEB  48 83 C1 08                     add rcx, 8
0026BEEF  E9 53 FF FF FF                  jmp 0x14026be47
0026BEF4  48 83 C7 04                     add rdi, 4
0026BEF8  49 83 C1 04                     add r9, 4
0026BEFC  3A C1                           cmp al, cl
0026BEFE  0F 85 15 FF FF FF               jne 0x14026be19
0026BF04  41 0F B6 41 01                  movzx eax, byte ptr [r9 + 1]
0026BF09  38 47 01                        cmp byte ptr [rdi + 1], al
0026BF0C  0F 85 8E 00 00 00               jne 0x14026bfa0
0026BF12  41 0F B6 41 02                  movzx eax, byte ptr [r9 + 2]
0026BF17  38 47 02                        cmp byte ptr [rdi + 2], al
0026BF1A  0F 84 F1 FE FF FF               je 0x14026be11
0026BF20  48 83 C7 02                     add rdi, 2
0026BF24  49 83 C1 02                     add r9, 2
0026BF28  E9 EC FE FF FF                  jmp 0x14026be19
0026BF2D  0F B6 57 01                     movzx edx, byte ptr [rdi + 1]
0026BF31  44 0F B6 07                     movzx r8d, byte ptr [rdi]
0026BF35  8D 42 61                        lea eax, [rdx + 0x61]
0026BF38  02 47 02                        add al, byte ptr [rdi + 2]
0026BF3B  D0 C8                           ror al, 1
0026BF3D  41 32 C0                        xor al, r8b
0026BF40  44 02 47 03                     add r8b, byte ptr [rdi + 3]
0026BF44  C0 C0 03                        rol al, 3
0026BF47  0F B6 C8                        movzx ecx, al
0026BF4A  41 C0 C0 03                     rol r8b, 3
0026BF4E  44 32 C2                        xor r8b, dl
0026BF51  41 D0 C8                        ror r8b, 1
0026BF54  41 0F B6 C0                     movzx eax, r8b
0026BF58  4C 8D 04 88                     lea r8, [rax + rcx*4]
0026BF5C  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0026BF61  4D 03 C0                        add r8, r8
0026BF64  4B 8D 04 28                     lea rax, [r8 + r13]
0026BF68  49 8B 94 C6 B0 57 00 00         mov rdx, qword ptr [r14 + rax*8 + 0x57b0]
0026BF70  49 8D 04 28                     lea rax, [r8 + rbp]
0026BF74  4D 89 8C C6 B0 57 00 00         mov qword ptr [r14 + rax*8 + 0x57b0], r9
0026BF7C  48 8B C7                        mov rax, rdi
0026BF7F  48 2B C2                        sub rax, rdx
0026BF82  48 3D 00 00 01 00               cmp rax, 0x10000
0026BF88  7D 0A                           jge 0x14026bf94
0026BF8A  8B 02                           mov eax, dword ptr [rdx]
0026BF8C  39 07                           cmp dword ptr [rdi], eax
0026BF8E  0F 84 39 01 00 00               je 0x14026c0cd
0026BF94  48 8B F9                        mov rdi, rcx
0026BF97  49 83 C1 04                     add r9, 4
0026BF9B  E9 79 FE FF FF                  jmp 0x14026be19
0026BFA0  48 FF C7                        inc rdi
0026BFA3  49 FF C1                        inc r9
0026BFA6  E9 6E FE FF FF                  jmp 0x14026be19
0026BFAB  0F B6 08                        movzx ecx, byte ptr [rax]
0026BFAE  44 0F B6 07                     movzx r8d, byte ptr [rdi]
0026BFB2  41 0F B6 C0                     movzx eax, r8b
0026BFB6  41 D2 C0                        rol r8b, cl
0026BFB9  D0 C8                           ror al, 1
0026BFBB  04 45                           add al, 0x45
0026BFBD  32 C1                           xor al, cl
0026BFBF  41 0F B6 C8                     movzx ecx, r8b
0026BFC3  C0 C0 03                        rol al, 3
0026BFC6  0F B6 D0                        movzx edx, al
0026BFC9  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
0026BFCD  C0 C0 03                        rol al, 3
0026BFD0  32 47 01                        xor al, byte ptr [rdi + 1]
0026BFD3  D0 C8                           ror al, 1
0026BFD5  0F B6 C0                        movzx eax, al
0026BFD8  48 03 D0                        add rdx, rax
0026BFDB  0F B6 47 02                     movzx eax, byte ptr [rdi + 2]
0026BFDF  48 33 C8                        xor rcx, rax
0026BFE2  0F B6 84 24 E8 00 00 00         movzx eax, byte ptr [rsp + 0xe8]
0026BFEA  4C 8D 04 91                     lea r8, [rcx + rdx*4]
0026BFEE  4D 03 C0                        add r8, r8
0026BFF1  49 03 C0                        add rax, r8
0026BFF4  49 8B 94 C6 B0 57 00 00         mov rdx, qword ptr [r14 + rax*8 + 0x57b0]
0026BFFC  4B 8D 04 28                     lea rax, [r8 + r13]
0026C000  4D 89 8C C6 B0 57 00 00         mov qword ptr [r14 + rax*8 + 0x57b0], r9
0026C008  48 8B C7                        mov rax, rdi
0026C00B  48 2B C2                        sub rax, rdx
0026C00E  48 3D 00 00 01 00               cmp rax, 0x10000
0026C014  7D 0A                           jge 0x14026c020
0026C016  8B 02                           mov eax, dword ptr [rdx]
0026C018  39 07                           cmp dword ptr [rdi], eax
0026C01A  0F 84 FF 00 00 00               je 0x14026c11f
0026C020  48 83 C7 05                     add rdi, 5
0026C024  49 83 C1 05                     add r9, 5
0026C028  E9 EC FD FF FF                  jmp 0x14026be19
0026C02D  48 81 FA 00 10 00 00            cmp rdx, 0x1000
0026C034  0F 86 F5 FD FF FF               jbe 0x14026be2f
0026C03A  4C 8B 5C 24 48                  mov r11, qword ptr [rsp + 0x48]
0026C03F  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
0026C044  E9 63 FC FF FF                  jmp 0x14026bcac
0026C049  41 89 07                        mov dword ptr [r15], eax
0026C04C  BE 01 00 00 00                  mov esi, 1
0026C051  4C 8B FB                        mov r15, rbx
0026C054  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
0026C059  48 83 C3 04                     add rbx, 4
0026C05D  49 3B FB                        cmp rdi, r11
0026C060  0F 82 1A FC FF FF               jb 0x14026bc80
0026C066  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0026C06B  48 3B F8                        cmp rdi, rax
0026C06E  0F 82 00 02 00 00               jb 0x14026c274
0026C074  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
0026C079  4C 8B 64 24 38                  mov r12, qword ptr [rsp + 0x38]
0026C07E  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
0026C083  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
0026C08B  E9 38 FB FF FF                  jmp 0x14026bbc8
0026C090  48 C1 E8 18                     shr rax, 0x18
0026C094  4C 8B C9                        mov r9, rcx
0026C097  49 03 C0                        add rax, r8
0026C09A  49 89 BC C6 B0 57 00 00         mov qword ptr [r14 + rax*8 + 0x57b0], rdi
0026C0A2  E9 64 FC FF FF                  jmp 0x14026bd0b
0026C0A7  80 C1 0F                        add cl, 0xf
0026C0AA  48 83 E8 0F                     sub rax, 0xf
0026C0AE  88 0B                           mov byte ptr [rbx], cl
0026C0B0  49 8D 58 01                     lea rbx, [r8 + 1]
0026C0B4  48 3D FF 00 00 00               cmp rax, 0xff
0026C0BA  0F 83 43 01 00 00               jae 0x14026c203
0026C0C0  48 FF 44 24 38                  inc qword ptr [rsp + 0x38]
0026C0C5  41 88 00                        mov byte ptr [r8], al
0026C0C8  E9 B1 FD FF FF                  jmp 0x14026be7e
0026C0CD  0F B6 01                        movzx eax, byte ptr [rcx]
0026C0D0  3A 42 04                        cmp al, byte ptr [rdx + 4]
0026C0D3  0F 85 BB FE FF FF               jne 0x14026bf94
0026C0D9  48 3B FA                        cmp rdi, rdx
0026C0DC  0F 84 B2 FE FF FF               je 0x14026bf94
0026C0E2  49 03 C0                        add rax, r8
0026C0E5  4C 8B CA                        mov r9, rdx
0026C0E8  49 89 BC C6 B0 57 00 00         mov qword ptr [r14 + rax*8 + 0x57b0], rdi
0026C0F0  48 8B C1                        mov rax, rcx
0026C0F3  E9 2F FC FF FF                  jmp 0x14026bd27
0026C0F8  48 83 C7 08                     add rdi, 8
0026C0FC  49 83 C1 08                     add r9, 8
0026C100  E9 F7 FD FF FF                  jmp 0x14026befc
0026C105  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0026C10A  BE 01 00 00 00                  mov esi, 1
0026C10F  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
0026C114  48 83 C3 04                     add rbx, 4
0026C118  89 01                           mov dword ptr [rcx], eax
0026C11A  E9 82 FD FF FF                  jmp 0x14026bea1
0026C11F  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0026C124  0F B6 42 04                     movzx eax, byte ptr [rdx + 4]
0026C128  38 01                           cmp byte ptr [rcx], al
0026C12A  0F 85 F0 FE FF FF               jne 0x14026c020
0026C130  0F B6 47 05                     movzx eax, byte ptr [rdi + 5]
0026C134  3A 42 05                        cmp al, byte ptr [rdx + 5]
0026C137  0F 85 E3 FE FF FF               jne 0x14026c020
0026C13D  48 3B FA                        cmp rdi, rdx
0026C140  0F 84 DA FE FF FF               je 0x14026c020
0026C146  49 03 C0                        add rax, r8
0026C149  4C 8B CA                        mov r9, rdx
0026C14C  49 89 BC C6 B0 57 00 00         mov qword ptr [r14 + rax*8 + 0x57b0], rdi
0026C154  E9 E7 FB FF FF                  jmp 0x14026bd40
0026C159  48 83 C7 0C                     add rdi, 0xc
0026C15D  49 83 C1 0C                     add r9, 0xc
0026C161  E9 96 FD FF FF                  jmp 0x14026befc
0026C166  48 83 C7 10                     add rdi, 0x10
0026C16A  49 83 C1 10                     add r9, 0x10
0026C16E  E9 89 FD FF FF                  jmp 0x14026befc
0026C173  48 83 C7 18                     add rdi, 0x18
0026C177  49 83 C1 18                     add r9, 0x18
0026C17B  E9 7C FD FF FF                  jmp 0x14026befc
0026C180  48 83 C7 14                     add rdi, 0x14
0026C184  49 83 C1 14                     add r9, 0x14
0026C188  E9 6F FD FF FF                  jmp 0x14026befc
0026C18D  4C 8B C3                        mov r8, rbx
0026C190  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
0026C194  49 8D 9E 40 6A 01 00            lea rbx, [r14 + 0x16a40]
0026C19B  48 8B D3                        mov rdx, rbx
0026C19E  49 8D 8E 20 EF 00 00            lea rcx, [r14 + 0xef20]
0026C1A5  E8 36 05 00 00                  call 0x14026c6e0
0026C1AA  85 F6                           test esi, esi
0026C1AC  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0026C1B1  48 8B B4 24 98 00 00 00         mov rsi, qword ptr [rsp + 0x98]
0026C1B9  4D 8D 8E 40 61 01 00            lea r9, [r14 + 0x16140]
0026C1C0  48 8B C8                        mov rcx, rax
0026C1C3  BA 00 00 00 00                  mov edx, 0
0026C1C8  0F 84 6C F9 FF FF               je 0x14026bb3a
0026C1CE  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
0026C1D6  2B 8C 24 F0 00 00 00            sub ecx, dword ptr [rsp + 0xf0]
0026C1DD  89 08                           mov dword ptr [rax], ecx
0026C1DF  33 C0                           xor eax, eax
0026C1E1  E9 7A FA FF FF                  jmp 0x14026bc60
0026C1E6  48 83 C7 1C                     add rdi, 0x1c
0026C1EA  49 83 C1 1C                     add r9, 0x1c
0026C1EE  E9 09 FD FF FF                  jmp 0x14026befc
0026C1F3  8B CA                           mov ecx, edx
0026C1F5  E9 0D F9 FF FF                  jmp 0x14026bb07
0026C1FA  33 C0                           xor eax, eax
0026C1FC  8B F0                           mov esi, eax
0026C1FE  E9 20 FA FF FF                  jmp 0x14026bc23
0026C203  41 C6 00 FF                     mov byte ptr [r8], 0xff
0026C207  49 81 F9 00 00 01 00            cmp r9, 0x10000
0026C20E  73 4C                           jae 0x14026c25c
0026C210  48 83 44 24 38 03               add qword ptr [rsp + 0x38], 3
0026C216  66 44 89 0B                     mov word ptr [rbx], r9w
0026C21A  49 8D 58 03                     lea rbx, [r8 + 3]
0026C21E  E9 5B FC FF FF                  jmp 0x14026be7e
0026C223  41 89 07                        mov dword ptr [r15], eax
0026C226  BE 01 00 00 00                  mov esi, 1
0026C22B  4C 8B FB                        mov r15, rbx
0026C22E  48 83 C3 04                     add rbx, 4
0026C232  E9 B9 F9 FF FF                  jmp 0x14026bbf0
0026C237  48 3B F9                        cmp rdi, rcx
0026C23A  0F 83 D9 FB FF FF               jae 0x14026be19
0026C240  41 0F B6 01                     movzx eax, byte ptr [r9]
0026C244  38 07                           cmp byte ptr [rdi], al
0026C246  0F 85 CD FB FF FF               jne 0x14026be19
0026C24C  48 FF C7                        inc rdi
0026C24F  49 FF C1                        inc r9
0026C252  48 3B F9                        cmp rdi, rcx
0026C255  72 E9                           jb 0x14026c240
0026C257  E9 BD FB FF FF                  jmp 0x14026be19
0026C25C  33 C0                           xor eax, eax
0026C25E  45 89 48 03                     mov dword ptr [r8 + 3], r9d
0026C262  48 83 44 24 38 07               add qword ptr [rsp + 0x38], 7
0026C268  66 89 03                        mov word ptr [rbx], ax
0026C26B  49 8D 58 07                     lea rbx, [r8 + 7]
0026C26F  E9 0A FC FF FF                  jmp 0x14026be7e
0026C274  4C 8B C7                        mov r8, rdi
0026C277  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
0026C27C  48 8B D0                        mov rdx, rax
0026C27F  E8 6C E5 1A 00                  call 0x14041a7f0
0026C284  4C 8B D8                        mov r11, rax
0026C287  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0026C28C  E9 EF F9 FF FF                  jmp 0x14026bc80
0026C291  4C 8B C7                        mov r8, rdi
0026C294  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
0026C299  48 8B D0                        mov rdx, rax
0026C29C  E8 4F E5 1A 00                  call 0x14041a7f0
0026C2A1  4C 8B D8                        mov r11, rax
0026C2A4  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0026C2A9  E9 D2 F9 FF FF                  jmp 0x14026bc80
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlCompressBufferXpressHuffStandard(__int64 a1, int a2, __int64 a3, int a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, unsigned int a9)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p98;
    unsigned __int8 v_stack_pE8;
    unsigned int v_stack_pF0;

    *(unsigned __int64 *)(v_rsp + 32) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (160);
    result = 0;
    v_rbp = ((unsigned int)(a2)) + (a1);
    v_stack_m78 = v_rbp;
    v_stack_m68 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 88) = 0;
    result = ((unsigned int)(a4)) + (a3);
    v_stack_m48 = result;
    if (a4 < 300) goto loc_0026BC5B;
    v_stack_m70 = a3;
    if (a7 == 0) goto loc_0026C1F3;
    if (((unsigned int)((unsigned int)(a9))) > a2) goto loc_0026C1F3;
loc_0026BB07:
    v_stack_m68 = a7;
    a2 = 0;
    v_stack_m60 = a8;
    v_stack_m58 = (unsigned int)((unsigned int)(a9));
    v_stack_m40 = (unsigned int)((unsigned int)((unsigned int)(a9)));
loc_0026BB3A:
    v_stack_m88 = 0;
    v_stack_mA0 = 0;
    a2 = 0;
    result = memset(a6 + 90432, a2, (unsigned int)(0x800ULL), a6 + 90432);
    v_stack_mA8 = a6 + 92736;
    a1 = a1 + 65536;
    if ((a1 + 65536) > v_rbp) { a1 = v_rbp; }
    v_stack_m50 = a1;
    v_stack_m80 = a1 - 40;
    v_r11 = (unsigned int)((unsigned int)((unsigned int)(a9))) + a1 * 1;
    if ((a1 - 40) < ((unsigned int)((unsigned int)((unsigned int)(a9))) + a1 * 1)) { v_r11 = a1 - 40; }
    v_rbx = (a6 + 92736) + (4);
    v_stack_m90 = v_r11;
    v_rsi = 1;
    v_rdi = a1;
    if (a1 == v_stack_p8) {
        result = *(unsigned __int8 *)(a1);
        v_rsi = 2;
        result = *(unsigned __int8 *)(a1);
        v_rdi = (a1) + 1;
        *(unsigned __int8 *)(v_rbx) = (unsigned __int8)(result);
        v_rbx = (v_rbx) + 1;
    }
    if (v_rdi < (a1 - 40)) goto loc_0026BC80;
loc_0026BBC8:
    if (v_rdi >= a1) goto loc_0026BBF5;
loc_0026BBCD:
    v_rdi = (v_rdi) + 1;
    *(unsigned __int8 *)(v_rbx) = (unsigned __int8)(*(unsigned __int8 *)(v_rdi));
    v_rbx = (v_rbx) + 1;
    if (condition_is_less_or_equal) goto loc_0026C223;
loc_0026BBF0:
    if (v_rdi < a1) goto loc_0026BBCD;
loc_0026BBF5:
    if (condition_is_less_or_equal) goto loc_0026BC04;
loc_0026BBF9:
    if (condition_is_greater) goto loc_0026BBF9;
loc_0026BC04:
    *(unsigned int *)(a6 + 92736) = (unsigned int)((unsigned int)((unsigned int)(v_rsi + v_rsi * 1)) * 2 + 1 * 2 + 1);
    if (v_rdi < v_rbp) goto loc_0026C1FA;
loc_0026BC23:
    result = XpressBuildHuffmanEncodings(a6 + 61216, a1 - 40, (unsigned int)(0x800ULL), a6 + 90432);
    a1 = (result + 31) + (0);
    a1 = (a1) >> (5);
    a1 = (v_stack_m70 + 258) + (0 + a1 * 4);
    if (a1 < v_stack_m48) goto loc_0026C18D;
loc_0026BC5B:
loc_0026BC60:
    v_rsp = (v_rsp) + (160);
    return (unsigned int)(0xC0000023ULL);
loc_0026BC80:
    result = (*(unsigned __int8 *)(v_rdi + 2) + *(unsigned __int8 *)(v_rdi + 1) * 4) + (*(unsigned __int8 *)(v_rdi + 2) + *(unsigned __int8 *)(v_rdi + 1) * 4);
    *(unsigned __int64 *)(a6 + *(unsigned __int8 *)(v_rdi) * 8 + result * 8) = v_rdi;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a6 + *(unsigned __int8 *)(v_rdi) * 8 + result * 8))) == ((unsigned __int8)(*(unsigned __int8 *)(v_rdi)))) goto loc_0026BCD4;
loc_0026BCAC:
    *(unsigned __int8 *)(v_stack_p20) = (unsigned __int8)(*(unsigned __int8 *)(v_rdi));
    v_rbx = (v_stack_p20) + 1;
    if (condition_is_less_or_equal) goto loc_0026C049;
    goto loc_0026BC80;
loc_0026BCD4:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a6 + *(unsigned __int8 *)(v_rdi) * 8 + result * 8) + 1)) != ((unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1 + 1)))) goto loc_0026BCAC;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a6 + *(unsigned __int8 *)(v_rdi) * 8 + result * 8) + 2)) != ((unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1 + 2)))) goto loc_0026BCAC;
    result = (v_rdi + 1) - (*(unsigned __int64 *)(a6 + *(unsigned __int8 *)(v_rdi) * 8 + result * 8));
    if (result >= 0x10000ULL) goto loc_0026BCAC;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1 + 3))) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a6 + *(unsigned __int8 *)(v_rdi) * 8 + result * 8) + 3)))) goto loc_0026BDDD;
loc_0026BD0B:
    v_stack_p40 = v_rdi + 1 + 4;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1 + 4))) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a6 + *(unsigned __int8 *)(v_rdi) * 8 + result * 8) + 4)))) goto loc_0026BF2D;
loc_0026BD27:
    v_stack_pE8 = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1 + 5));
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1 + 5))) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a6 + *(unsigned __int8 *)(v_rdi) * 8 + result * 8) + 5)))) goto loc_0026BFAB;
loc_0026BD40:
    v_rdi = (v_rdi + 1) + (6);
    a4 = (*(unsigned __int64 *)(a6 + *(unsigned __int8 *)(v_rdi) * 8 + result * 8)) + (6);
loc_0026BD48:
    if (v_rdi >= (v_stack_p60 - 40)) goto loc_0026C237;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) goto loc_0026BEFC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 4)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_0026BEF4;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8))))) goto loc_0026C0F8;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 12)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))) goto loc_0026C159;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 16)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16))))) goto loc_0026C166;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 20)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 20))))) goto loc_0026C180;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 24)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 24))))) goto loc_0026C173;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 28)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 28))))) goto loc_0026C1E6;
    v_rdi = (v_rdi) + (32);
    a4 = (a4) + (32);
    goto loc_0026BD48;
loc_0026BDDD:
    *(unsigned __int64 *)(a6 + (unsigned int)(*(unsigned int *)(a4 + 28)) + *(unsigned __int8 *)(v_rdi + 2) + *(unsigned __int8 *)(v_rdi + 1) * 4 * 2 + *(unsigned __int8 *)(*(unsigned __int64 *)(a6 + *(unsigned __int8 *)(v_rdi) * 8 + result * 8) + 3) * 1 * 8 + 22448) = a4;
    result = (v_rdi) - (*(unsigned __int64 *)(a6 + (unsigned int)(*(unsigned int *)(a4 + 28)) + *(unsigned __int8 *)(v_rdi + 2) + *(unsigned __int8 *)(v_rdi + 1) * 4 * 2 + *(unsigned __int8 *)(*(unsigned __int64 *)(a6 + *(unsigned __int8 *)(v_rdi) * 8 + result * 8) + 4) * 1 * 8 + 22448));
    if (result >= 0x10000ULL) goto loc_0026BE11;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi)))) == (*(unsigned int *)(*(unsigned __int64 *)(a6 + (unsigned int)(*(unsigned int *)(a4 + 28)) + *(unsigned __int8 *)(v_rdi + 2) + *(unsigned __int8 *)(v_rdi + 1) * 4 * 2 + *(unsigned __int8 *)(*(unsigned __int64 *)(a6 + *(unsigned __int8 *)(v_rdi) * 8 + result * 8) + 4) * 1 * 8 + 22448)))) goto loc_0026C090;
loc_0026BE11:
    v_rdi = (v_rdi) + (3);
    a4 = (a4) + (3);
loc_0026BE19:
    a3 = (v_rdi) - (v_rdi + 1);
    a2 = (v_rdi) - (a4);
    if (a3 == 3) goto loc_0026C02D;
loc_0026BE2F:
    if (a2 >= 256) goto loc_0026BED9;
loc_0026BE47:
    v_r13 = (v_stack_p50) + (*(unsigned __int8 *)(a2 + v_rip - 2471923 * 1));
    v_stack_p50 = v_r13;
    result = (1) << ((unsigned __int8)(*(unsigned __int8 *)(a2 + v_rip - 2471923 * 1)));
    a2 = (a2) - (result);
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a2 + v_rip - 2471923 * 1)) << (4));
    if ((a3 - 3) >= 15) goto loc_0026C0A7;
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a3 - 3)));
    *(unsigned __int8 *)(v_rbx) = (unsigned __int8)(a1);
loc_0026BE7E:
    *(unsigned __int16 *)(v_rbx + 1) = (unsigned __int16)(a2);
    v_rbx = (v_rbx + 1) + (2);
    if (condition_is_less_or_equal) goto loc_0026C105;
loc_0026BEA1:
    if (v_rdi < v_stack_p48) goto loc_0026BC80;
    if (v_rdi < v_stack_p58) goto loc_0026C291;
    goto loc_0026BBC8;
loc_0026BED9:
    result = (a2) >> (8);
    a1 = (*(unsigned __int8 *)(result + v_rip - 2472083 * 1)) + (8);
    goto loc_0026BE47;
loc_0026BEF4:
    v_rdi = (v_rdi) + (4);
    a4 = (a3 - 3) + (4);
loc_0026BEFC:
    if (((unsigned __int8)(result)) != ((unsigned __int8)(a1))) goto loc_0026BE19;
    if ((*(unsigned __int8 *)(v_rdi + 1)) != ((unsigned __int8)(*(unsigned __int8 *)(a4 + 1)))) goto loc_0026BFA0;
    if ((*(unsigned __int8 *)(v_rdi + 2)) == ((unsigned __int8)(*(unsigned __int8 *)(a4 + 2)))) goto loc_0026BE11;
    v_rdi = (v_rdi) + (2);
    a4 = (a4) + (2);
    goto loc_0026BE19;
loc_0026BF2D:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rdi + 1) + 97) + (*(unsigned __int8 *)(v_rdi + 2)));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(*(unsigned __int8 *)(v_rdi))));
    a3 = (unsigned __int8)((*(unsigned __int8 *)(v_rdi)) + (*(unsigned __int8 *)(v_rdi + 3)));
    a3 = (unsigned __int8)((a3) ^ ((unsigned __int8)(*(unsigned __int8 *)(v_rdi + 1))));
    a3 = ((unsigned __int8)(a3) + (unsigned __int8)(result) * 4) + ((unsigned __int8)(a3) + (unsigned __int8)(result) * 4);
    *(unsigned __int64 *)(a6 + a3 + v_stack_p60 * 1 * 8 + 22448) = a4;
    result = (v_rdi) - (*(unsigned __int64 *)(a6 + a3 + v_r13 * 1 * 8 + 22448));
    if (result >= 0x10000ULL) goto loc_0026BF94;
    if ((*(unsigned int *)(v_rdi)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a6 + a3 + v_r13 * 1 * 8 + 22448)))))) goto loc_0026C0CD;
loc_0026BF94:
    a4 = (a4) + (4);
    goto loc_0026BE19;
loc_0026BFA0:
    v_rdi = (v_stack_p40) + 1;
    a4 = (a4) + 1;
    goto loc_0026BE19;
loc_0026BFAB:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_rdi))) + (69));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(*(unsigned __int8 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a6 + a3 + v_r13 * 1 * 8 + 22448)))))));
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rdi + 3)) ^ (*(unsigned __int8 *)(v_rdi + 1)));
    a2 = ((unsigned __int8)(result)) + ((unsigned __int8)(result));
    a1 = ((unsigned __int8)(*(unsigned __int8 *)(v_rdi))) ^ (*(unsigned __int8 *)(v_rdi + 2));
    a3 = (a1 + a2 * 4) + (a1 + a2 * 4);
    result = (v_stack_pE8) + (a3);
    *(unsigned __int64 *)(a6 + a3 + v_r13 * 1 * 8 + 22448) = a4;
    result = (v_rdi) - (*(unsigned __int64 *)(a6 + result * 8 + 22448));
    if (result >= 0x10000ULL) goto loc_0026C020;
    if ((*(unsigned int *)(v_rdi)) == ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a6 + result * 8 + 22448)))))) goto loc_0026C11F;
loc_0026C020:
    v_rdi = (v_rdi) + (5);
    a4 = (a4) + (5);
    goto loc_0026BE19;
loc_0026C02D:
    if ((*(unsigned __int64 *)(a6 + result * 8 + 22448)) <= 0x1000ULL) goto loc_0026BE2F;
    goto loc_0026BCAC;
loc_0026C049:
    *(unsigned int *)(v_stack_p30) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a6 + result * 8 + 22448))));
    v_stack_p30 = v_rbx;
    v_rbx = (v_rbx) + (4);
    if (v_rdi < v_stack_p48) goto loc_0026BC80;
    if (v_rdi < v_stack_p58) goto loc_0026C274;
    goto loc_0026BBC8;
loc_0026C090:
    result = (v_stack_p58) >> (24);
    result = (result) + (a3);
    *(unsigned __int64 *)(a6 + result * 8 + 22448) = v_rdi;
    goto loc_0026BD0B;
loc_0026C0A7:
    a1 = (unsigned __int8)((v_stack_p88) + (15));
    result = (result) - (15);
    *(unsigned __int8 *)(v_rbx) = (unsigned __int8)(a1);
    if (result >= 255) goto loc_0026C203;
    *(unsigned __int8 *)(a3) = (unsigned __int8)(result);
    goto loc_0026BE7E;
loc_0026C0CD:
    if (((unsigned __int8)(*(unsigned __int8 *)(a1))) != (*(unsigned __int8 *)(*(unsigned __int64 *)(a6 + result * 8 + 22448) + 4))) goto loc_0026BF94;
    if (v_rdi == (*(unsigned __int64 *)(a6 + result * 8 + 22448))) goto loc_0026BF94;
    result = (*(unsigned __int8 *)(a1)) + (a3);
    *(unsigned __int64 *)(a6 + result * 8 + 22448) = v_rdi;
    goto loc_0026BD27;
loc_0026C0F8:
    v_rdi = (v_rdi) + (8);
    a4 = (*(unsigned __int64 *)(a6 + result * 8 + 22448)) + (8);
    goto loc_0026BEFC;
loc_0026C105:
    v_stack_p30 = a3 + 1;
    v_rbx = (a3 + 1) + (4);
    *(unsigned int *)(v_stack_p30) = (unsigned int)(a1);
    goto loc_0026BEA1;
loc_0026C11F:
    if ((*(unsigned __int8 *)(v_stack_p40)) != ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a6 + result * 8 + 22448) + 4)))) goto loc_0026C020;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rdi + 5))) != (*(unsigned __int8 *)(*(unsigned __int64 *)(a6 + result * 8 + 22448) + 5))) goto loc_0026C020;
    if (v_rdi == (*(unsigned __int64 *)(a6 + result * 8 + 22448))) goto loc_0026C020;
    result = (*(unsigned __int8 *)(v_rdi + 5)) + (a3);
    *(unsigned __int64 *)(a6 + result * 8 + 22448) = v_rdi;
    goto loc_0026BD40;
loc_0026C159:
    v_rdi = (v_rdi) + (12);
    a4 = (*(unsigned __int64 *)(a6 + result * 8 + 22448)) + (12);
    goto loc_0026BEFC;
loc_0026C166:
    v_rdi = (v_rdi) + (16);
    a4 = (a4) + (16);
    goto loc_0026BEFC;
loc_0026C173:
    v_rdi = (v_rdi) + (24);
    a4 = (a4) + (24);
    goto loc_0026BEFC;
loc_0026C180:
    v_rdi = (v_rdi) + (20);
    a4 = (a4) + (20);
    goto loc_0026BEFC;
loc_0026C18D:
    v_stack_p20 = 1;
    result = XpressDoHuffmanPass(a6 + 61216, a6 + 92736, v_rbx, a4);
    v_stack_p68 = result;
    if (1 == 0) goto loc_0026BB3A;
    a1 = (unsigned int)((result) - (v_stack_pF0));
    *(unsigned int *)(a5) = (unsigned int)(a1);
    result = 0;
    goto loc_0026BC60;
loc_0026C1E6:
    v_rdi = (v_rdi) + (28);
    a4 = (a6 + 90432) + (28);
    goto loc_0026BEFC;
loc_0026C1F3:
    goto loc_0026BB07;
loc_0026C1FA:
    result = 0;
    goto loc_0026BC23;
loc_0026C203:
    *(unsigned __int8 *)(v_rbx) = 255;
    if (a4 >= 0x10000ULL) goto loc_0026C25C;
    *(unsigned __int16 *)(a6 + 92736) = (unsigned __int16)(a4);
    goto loc_0026BE7E;
loc_0026C223:
    *(unsigned int *)(v_rbx) = 0;
    v_rbx = (v_rbx + 3) + (4);
    goto loc_0026BBF0;
loc_0026C237:
    if (v_rdi >= 0) goto loc_0026BE19;
loc_0026C240:
    if ((*(unsigned __int8 *)(v_rdi)) != ((unsigned __int8)(*(unsigned __int8 *)(a4)))) goto loc_0026BE19;
    v_rdi = (v_rdi) + 1;
    a4 = (a4) + 1;
    if (v_rdi < 0) goto loc_0026C240;
    goto loc_0026BE19;
loc_0026C25C:
    result = 0;
    *(unsigned int *)(v_rbx + 3) = a4;
    *(unsigned __int16 *)(v_rbx) = 0;
    goto loc_0026BE7E;
loc_0026C274:
    result = RtlpMakeXpressCallback(v_stack_p70, 0, v_rdi, a4);
    v_stack_p48 = result;
    goto loc_0026BC80;
loc_0026C291:
    result = RtlpMakeXpressCallback(v_stack_p70, result, v_rdi, a4);
    v_stack_p48 = result;
    goto loc_0026BC80;
}
```

## 5. (Beta) C Style

```c
int64_t RtlCompressBufferXpressHuffStandard(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, void *Arg5, void *Arg6, int64_t Arg7, int64_t Arg8, uint32_t Arg9)
{
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p8;
    uint64_t v_stack_p88;
    uint64_t v_stack_p98;
    uint8_t v_stack_pE8;
    uint32_t v_stack_pF0;

    *(uint64_t *)(local_rsp + 0x20) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (160);
    result = 0;
    local_rbp = ((uint32_t)(Arg2)) + (Arg1);
    v_stack_m78 = local_rbp;
    v_stack_m68 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x58) = 0;
    result = ((uint32_t)(Arg4)) + (Arg3);
    v_stack_m48 = result;
    if (Arg4 < 300) goto loc_0026BC5B;
    v_stack_m70 = Arg3;
    if (Arg7 == 0) goto loc_0026C1F3;
    if (((uint32_t)((uint32_t)(Arg9))) > Arg2) goto loc_0026C1F3;
loc_0026BB07:
    v_stack_m68 = Arg7;
    Arg2 = 0;
    v_stack_m60 = Arg8;
    v_stack_m58 = (uint32_t)((uint32_t)(Arg9));
    v_stack_m40 = (uint32_t)((uint32_t)((uint32_t)(Arg9)));
loc_0026BB3A:
    v_stack_m88 = 0;
    v_stack_mA0 = 0;
    Arg2 = 0;
    result = memset(Arg6 + 90432, Arg2, (uint32_t)(0x800ULL), Arg6 + 90432);
    v_stack_mA8 = Arg6 + 92736;
    Arg1 = Arg1 + 65536;
    if ((Arg1 + 65536) > local_rbp) { Arg1 = local_rbp; }
    v_stack_m50 = Arg1;
    v_stack_m80 = Arg1 - 40;
    local_r11 = (uint32_t)((uint32_t)((uint32_t)(Arg9))) + Arg1 * 1;
    if ((Arg1 - 40) < ((uint32_t)((uint32_t)((uint32_t)(Arg9))) + Arg1 * 1)) { local_r11 = Arg1 - 40; }
    local_rbx = (Arg6 + 92736) + (4);
    v_stack_m90 = local_r11;
    local_rsi = 1;
    local_rdi = Arg1;
    if (Arg1 == v_stack_p8) {
        result = *(uint8_t *)(Arg1);
        local_rsi = 2;
        result = *(uint8_t *)(Arg1);
        local_rdi = (Arg1) + 1;
        *(uint8_t *)(local_rbx) = (uint8_t)(result);
        local_rbx = (local_rbx) + 1;
    }
    if (local_rdi < (Arg1 - 40)) goto loc_0026BC80;
loc_0026BBC8:
    if (local_rdi >= Arg1) goto loc_0026BBF5;
loc_0026BBCD:
    local_rdi = (local_rdi) + 1;
    *(uint8_t *)(local_rbx) = (uint8_t)(*(uint8_t *)(local_rdi));
    local_rbx = (local_rbx) + 1;
    if (condition_is_less_or_equal) goto loc_0026C223;
loc_0026BBF0:
    if (local_rdi < Arg1) goto loc_0026BBCD;
loc_0026BBF5:
    if (condition_is_less_or_equal) goto loc_0026BC04;
loc_0026BBF9:
    if (condition_is_greater) goto loc_0026BBF9;
loc_0026BC04:
    *(uint32_t *)(arg6 + 0x16A40) = (uint32_t)((uint32_t)((uint32_t)(local_rsi + local_rsi * 1)) * 2 + 1 * 2 + 1);
    if (local_rdi < local_rbp) goto loc_0026C1FA;
loc_0026BC23:
    result = XpressBuildHuffmanEncodings(Arg6 + 61216, Arg1 - 40, (uint32_t)(0x800ULL), Arg6 + 90432);
    Arg1 = (result + 31) + (0);
    Arg1 = (Arg1) >> (5);
    Arg1 = (v_stack_m70 + 258) + (0 + Arg1 * 4);
    if (Arg1 < v_stack_m48) goto loc_0026C18D;
loc_0026BC5B:
loc_0026BC60:
    local_rsp = (local_rsp) + (160);
    return (uint32_t)(0xC0000023ULL);
loc_0026BC80:
    result = (*(uint8_t *)(local_rdi + 0x2) + *(uint8_t *)(local_rdi + 0x1) * 4) + (*(uint8_t *)(local_rdi + 0x2) + *(uint8_t *)(local_rdi + 0x1) * 4);
    *(uint64_t *)(arg6 + *(uint8_t *)(local_rdi) * 8 + result * 8) = local_rdi;
    if ((*(uint8_t *)(*(uint64_t *)(arg6 + *(uint8_t *)(local_rdi) * 8 + result * 8))) == ((uint8_t)(*(uint8_t *)(local_rdi)))) goto loc_0026BCD4;
loc_0026BCAC:
    *(uint8_t *)(v_stack_p20) = (uint8_t)(*(uint8_t *)(local_rdi));
    local_rbx = (v_stack_p20) + 1;
    if (condition_is_less_or_equal) goto loc_0026C049;
    goto loc_0026BC80;
loc_0026BCD4:
    if ((*(uint8_t *)(*(uint64_t *)(arg6 + *(uint8_t *)(local_rdi) * 8 + result * 8) + 0x1)) != ((uint8_t)(*(uint8_t *)(local_rdi + 0x1 + 0x1)))) goto loc_0026BCAC;
    if ((*(uint8_t *)(*(uint64_t *)(arg6 + *(uint8_t *)(local_rdi) * 8 + result * 8) + 0x2)) != ((uint8_t)(*(uint8_t *)(local_rdi + 0x1 + 0x2)))) goto loc_0026BCAC;
    result = (local_rdi + 1) - (*(uint64_t *)(arg6 + *(uint8_t *)(local_rdi) * 8 + result * 8));
    if (result >= 0x10000ULL) goto loc_0026BCAC;
    if (((uint8_t)(*(uint8_t *)(local_rdi + 0x1 + 0x3))) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg6 + *(uint8_t *)(local_rdi) * 8 + result * 8) + 0x3)))) goto loc_0026BDDD;
loc_0026BD0B:
    v_stack_p40 = local_rdi + 1 + 4;
    if (((uint8_t)(*(uint8_t *)(local_rdi + 0x1 + 0x4))) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg6 + *(uint8_t *)(local_rdi) * 8 + result * 8) + 0x4)))) goto loc_0026BF2D;
loc_0026BD27:
    v_stack_pE8 = (uint8_t)(*(uint8_t *)(local_rdi + 0x1 + 0x5));
    if (((uint8_t)(*(uint8_t *)(local_rdi + 0x1 + 0x5))) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg6 + *(uint8_t *)(local_rdi) * 8 + result * 8) + 0x5)))) goto loc_0026BFAB;
loc_0026BD40:
    local_rdi = (local_rdi + 1) + (6);
    Arg4 = (*(uint64_t *)(arg6 + *(uint8_t *)(local_rdi) * 8 + result * 8)) + (6);
loc_0026BD48:
    if (local_rdi >= (v_stack_p60 - 40)) goto loc_0026C237;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4))))) goto loc_0026BEFC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x4)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_0026BEF4;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x8))))) goto loc_0026C0F8;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0xC))))) goto loc_0026C159;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x10)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x10))))) goto loc_0026C166;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x14)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x14))))) goto loc_0026C180;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x18)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x18))))) goto loc_0026C173;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x1C)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x1C))))) goto loc_0026C1E6;
    local_rdi = (local_rdi) + (32);
    Arg4 = (Arg4) + (32);
    goto loc_0026BD48;
loc_0026BDDD:
    *(uint64_t *)(arg6 + (uint32_t)(*(uint32_t *)(Arg4 + 0x1C)) + *(uint8_t *)(local_rdi + 0x2) + *(uint8_t *)(local_rdi + 0x1) * 4 * 2 + *(uint8_t *)(*(uint64_t *)(arg6 + *(uint8_t *)(local_rdi) * 8 + result * 8) + 0x3) * 1 * 8 + 0x57B0) = Arg4;
    result = (local_rdi) - (*(uint64_t *)(arg6 + (uint32_t)(*(uint32_t *)(Arg4 + 0x1C)) + *(uint8_t *)(local_rdi + 0x2) + *(uint8_t *)(local_rdi + 0x1) * 4 * 2 + *(uint8_t *)(*(uint64_t *)(arg6 + *(uint8_t *)(local_rdi) * 8 + result * 8) + 0x4) * 1 * 8 + 0x57B0));
    if (result >= 0x10000ULL) goto loc_0026BE11;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi)))) == (*(uint32_t *)(*(uint64_t *)(arg6 + (uint32_t)(*(uint32_t *)(Arg4 + 0x1C)) + *(uint8_t *)(local_rdi + 0x2) + *(uint8_t *)(local_rdi + 0x1) * 4 * 2 + *(uint8_t *)(*(uint64_t *)(arg6 + *(uint8_t *)(local_rdi) * 8 + result * 8) + 0x4) * 1 * 8 + 0x57B0)))) goto loc_0026C090;
loc_0026BE11:
    local_rdi = (local_rdi) + (3);
    Arg4 = (Arg4) + (3);
loc_0026BE19:
    Arg3 = (local_rdi) - (local_rdi + 1);
    Arg2 = (local_rdi) - (Arg4);
    if (Arg3 == 3) goto loc_0026C02D;
loc_0026BE2F:
    if (Arg2 >= 256) goto loc_0026BED9;
loc_0026BE47:
    local_r13 = (v_stack_p50) + (*(uint8_t *)(Arg2 + v_rip - 0x25B7F3 * 1));
    v_stack_p50 = local_r13;
    result = (1) << ((uint8_t)(*(uint8_t *)(Arg2 + v_rip - 0x25B7F3 * 1)));
    Arg2 = (Arg2) - (result);
    Arg1 = (uint8_t)((*(uint8_t *)(Arg2 + v_rip - 0x25B7F3 * 1)) << (4));
    if ((Arg3 - 3) >= 15) goto loc_0026C0A7;
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(Arg3 - 3)));
    *(uint8_t *)(local_rbx) = (uint8_t)(Arg1);
loc_0026BE7E:
    *(uint16_t *)(local_rbx + 0x1) = (uint16_t)(Arg2);
    local_rbx = (local_rbx + 1) + (2);
    if (condition_is_less_or_equal) goto loc_0026C105;
loc_0026BEA1:
    if (local_rdi < v_stack_p48) goto loc_0026BC80;
    if (local_rdi < v_stack_p58) goto loc_0026C291;
    goto loc_0026BBC8;
loc_0026BED9:
    result = (Arg2) >> (8);
    Arg1 = (*(uint8_t *)(result + v_rip - 0x25B893 * 1)) + (8);
    goto loc_0026BE47;
loc_0026BEF4:
    local_rdi = (local_rdi) + (4);
    Arg4 = (Arg3 - 3) + (4);
loc_0026BEFC:
    if (((uint8_t)(result)) != ((uint8_t)(Arg1))) goto loc_0026BE19;
    if ((*(uint8_t *)(local_rdi + 0x1)) != ((uint8_t)(*(uint8_t *)(Arg4 + 0x1)))) goto loc_0026BFA0;
    if ((*(uint8_t *)(local_rdi + 0x2)) == ((uint8_t)(*(uint8_t *)(Arg4 + 0x2)))) goto loc_0026BE11;
    local_rdi = (local_rdi) + (2);
    Arg4 = (Arg4) + (2);
    goto loc_0026BE19;
loc_0026BF2D:
    result = (uint8_t)((*(uint8_t *)(local_rdi + 0x1) + 97) + (*(uint8_t *)(local_rdi + 0x2)));
    result = (uint8_t)((result) ^ ((uint8_t)(*(uint8_t *)(local_rdi))));
    Arg3 = (uint8_t)((*(uint8_t *)(local_rdi)) + (*(uint8_t *)(local_rdi + 0x3)));
    Arg3 = (uint8_t)((Arg3) ^ ((uint8_t)(*(uint8_t *)(local_rdi + 0x1))));
    Arg3 = ((uint8_t)(Arg3) + (uint8_t)(result) * 4) + ((uint8_t)(Arg3) + (uint8_t)(result) * 4);
    *(uint64_t *)(arg6 + Arg3 + v_stack_p60 * 1 * 8 + 0x57B0) = Arg4;
    result = (local_rdi) - (*(uint64_t *)(arg6 + Arg3 + local_r13 * 1 * 8 + 0x57B0));
    if (result >= 0x10000ULL) goto loc_0026BF94;
    if ((*(uint32_t *)(local_rdi)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg6 + Arg3 + local_r13 * 1 * 8 + 0x57B0)))))) goto loc_0026C0CD;
loc_0026BF94:
    Arg4 = (Arg4) + (4);
    goto loc_0026BE19;
loc_0026BFA0:
    local_rdi = (v_stack_p40) + 1;
    Arg4 = (Arg4) + 1;
    goto loc_0026BE19;
loc_0026BFAB:
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(local_rdi))) + (69));
    result = (uint8_t)((result) ^ ((uint8_t)(*(uint8_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg6 + Arg3 + local_r13 * 1 * 8 + 0x57B0)))))));
    result = (uint8_t)((*(uint8_t *)(local_rdi + 0x3)) ^ (*(uint8_t *)(local_rdi + 0x1)));
    Arg2 = ((uint8_t)(result)) + ((uint8_t)(result));
    Arg1 = ((uint8_t)(*(uint8_t *)(local_rdi))) ^ (*(uint8_t *)(local_rdi + 0x2));
    Arg3 = (Arg1 + Arg2 * 4) + (Arg1 + Arg2 * 4);
    result = (v_stack_pE8) + (Arg3);
    *(uint64_t *)(arg6 + Arg3 + local_r13 * 1 * 8 + 0x57B0) = Arg4;
    result = (local_rdi) - (*(uint64_t *)(arg6 + result * 8 + 0x57B0));
    if (result >= 0x10000ULL) goto loc_0026C020;
    if ((*(uint32_t *)(local_rdi)) == ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg6 + result * 8 + 0x57B0)))))) goto loc_0026C11F;
loc_0026C020:
    local_rdi = (local_rdi) + (5);
    Arg4 = (Arg4) + (5);
    goto loc_0026BE19;
loc_0026C02D:
    if ((*(uint64_t *)(arg6 + result * 8 + 0x57B0)) <= 0x1000ULL) goto loc_0026BE2F;
    goto loc_0026BCAC;
loc_0026C049:
    *(uint32_t *)(v_stack_p30) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg6 + result * 8 + 0x57B0))));
    v_stack_p30 = local_rbx;
    local_rbx = (local_rbx) + (4);
    if (local_rdi < v_stack_p48) goto loc_0026BC80;
    if (local_rdi < v_stack_p58) goto loc_0026C274;
    goto loc_0026BBC8;
loc_0026C090:
    result = (v_stack_p58) >> (24);
    result = (result) + (Arg3);
    *(uint64_t *)(arg6 + result * 8 + 0x57B0) = local_rdi;
    goto loc_0026BD0B;
loc_0026C0A7:
    Arg1 = (uint8_t)((v_stack_p88) + (15));
    result = (result) - (15);
    *(uint8_t *)(local_rbx) = (uint8_t)(Arg1);
    if (result >= 255) goto loc_0026C203;
    *(uint8_t *)(Arg3) = (uint8_t)(result);
    goto loc_0026BE7E;
loc_0026C0CD:
    if (((uint8_t)(*(uint8_t *)(Arg1))) != (*(uint8_t *)(*(uint64_t *)(arg6 + result * 8 + 0x57B0) + 0x4))) goto loc_0026BF94;
    if (local_rdi == (*(uint64_t *)(arg6 + result * 8 + 0x57B0))) goto loc_0026BF94;
    result = (*(uint8_t *)(Arg1)) + (Arg3);
    *(uint64_t *)(arg6 + result * 8 + 0x57B0) = local_rdi;
    goto loc_0026BD27;
loc_0026C0F8:
    local_rdi = (local_rdi) + (8);
    Arg4 = (*(uint64_t *)(arg6 + result * 8 + 0x57B0)) + (8);
    goto loc_0026BEFC;
loc_0026C105:
    v_stack_p30 = Arg3 + 1;
    local_rbx = (Arg3 + 1) + (4);
    *(uint32_t *)(v_stack_p30) = (uint32_t)(Arg1);
    goto loc_0026BEA1;
loc_0026C11F:
    if ((*(uint8_t *)(v_stack_p40)) != ((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg6 + result * 8 + 0x57B0) + 0x4)))) goto loc_0026C020;
    if (((uint8_t)(*(uint8_t *)(local_rdi + 0x5))) != (*(uint8_t *)(*(uint64_t *)(arg6 + result * 8 + 0x57B0) + 0x5))) goto loc_0026C020;
    if (local_rdi == (*(uint64_t *)(arg6 + result * 8 + 0x57B0))) goto loc_0026C020;
    result = (*(uint8_t *)(local_rdi + 0x5)) + (Arg3);
    *(uint64_t *)(arg6 + result * 8 + 0x57B0) = local_rdi;
    goto loc_0026BD40;
loc_0026C159:
    local_rdi = (local_rdi) + (12);
    Arg4 = (*(uint64_t *)(arg6 + result * 8 + 0x57B0)) + (12);
    goto loc_0026BEFC;
loc_0026C166:
    local_rdi = (local_rdi) + (16);
    Arg4 = (Arg4) + (16);
    goto loc_0026BEFC;
loc_0026C173:
    local_rdi = (local_rdi) + (24);
    Arg4 = (Arg4) + (24);
    goto loc_0026BEFC;
loc_0026C180:
    local_rdi = (local_rdi) + (20);
    Arg4 = (Arg4) + (20);
    goto loc_0026BEFC;
loc_0026C18D:
    v_stack_p20 = 1;
    result = XpressDoHuffmanPass(Arg6 + 61216, Arg6 + 92736, local_rbx, Arg4);
    v_stack_p68 = result;
    if (1 == 0) goto loc_0026BB3A;
    Arg1 = (uint32_t)((result) - (v_stack_pF0));
    *(uint32_t *)(arg5) = (uint32_t)(Arg1);
    result = 0;
    goto loc_0026BC60;
loc_0026C1E6:
    local_rdi = (local_rdi) + (28);
    Arg4 = (Arg6 + 90432) + (28);
    goto loc_0026BEFC;
loc_0026C1F3:
    goto loc_0026BB07;
loc_0026C1FA:
    result = 0;
    goto loc_0026BC23;
loc_0026C203:
    *(uint8_t *)(local_rbx) = 255;
    if (Arg4 >= 0x10000ULL) goto loc_0026C25C;
    *(uint16_t *)(arg6 + 0x16A40) = (uint16_t)(Arg4);
    goto loc_0026BE7E;
loc_0026C223:
    *(uint32_t *)(local_rbx) = 0;
    local_rbx = (local_rbx + 3) + (4);
    goto loc_0026BBF0;
loc_0026C237:
    if (local_rdi >= 0) goto loc_0026BE19;
loc_0026C240:
    if ((*(uint8_t *)(local_rdi)) != ((uint8_t)(*(uint8_t *)(Arg4)))) goto loc_0026BE19;
    local_rdi = (local_rdi) + 1;
    Arg4 = (Arg4) + 1;
    if (local_rdi < 0) goto loc_0026C240;
    goto loc_0026BE19;
loc_0026C25C:
    result = 0;
    *(uint32_t *)(local_rbx + 0x3) = Arg4;
    *(uint16_t *)(local_rbx) = 0;
    goto loc_0026BE7E;
loc_0026C274:
    result = RtlpMakeXpressCallback(v_stack_p70, 0, local_rdi, Arg4);
    v_stack_p48 = result;
    goto loc_0026BC80;
loc_0026C291:
    result = RtlpMakeXpressCallback(v_stack_p70, result, local_rdi, Arg4);
    v_stack_p48 = result;
    goto loc_0026BC80;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `32` | `W` |
| `Arg6` | `+ 0x0` | `8` | `W` |
| `Arg6` | `+ 0x0` | `64` | `W` |
| `Arg6` | `+ 0x0 + rax*8` | `64` | `R` |
| `Arg6` | `+ 0x0 + rax*8` | `64` | `W` |
| `Arg6` | `+ 0x57B0` | `64` | `R` |
| `Arg6` | `+ 0x57B0 + rax*8` | `64` | `R` |
| `Arg6` | `+ 0x57B0 + rax*8` | `64` | `W` |
| `Arg6` | `+ 0xEF20` | `64` | `R` |
| `Arg6` | `+ 0x16140` | `64` | `R` |
| `Arg6` | `+ 0x16140 + rax*4` | `32` | `R/W` |
| `Arg6` | `+ 0x16540` | `32` | `R/W` |
| `Arg6` | `+ 0x16540 + rax*4` | `32` | `R/W` |
| `Arg6` | `+ 0x16A40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0026BA60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
