# punycode_encode

- RVA: `0x007926F4`–`0x00792C22` (길이 `1,326` bytes)
- VA: `0x00000001407926F4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CFDBC`
- 디코드: `353`개 명령, `1,326/1,326` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00792782` → [FindLabelEnd](../../text/5E/FindLabelEnd_function_005ECAA4.md) (function, `0x005ECAA4`)
- `0x007927F9` → [RtlStringCchCopyNExW](../../text/43/RtlStringCchCopyNExW_function_00437CB0.md) (function, `0x00437CB0`)
- `0x0079283D` → [ValidateStd3Range](../../text/5E/ValidateStd3Range_function_005ED154.md) (function, `0x005ED154`)
- `0x00792926` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (function, `0x005001C0`)
- `0x00792999` → [GetUTF32](../../text/5E/GetUTF32_function_005ECAE0.md) (function, `0x005ECAE0`)
- `0x007929EC` → [GetUTF32](../../text/5E/GetUTF32_function_005ECAE0.md) (function, `0x005ECAE0`)
- `0x00792AC8` → [adapt](../../text/5E/adapt_function_005ED190.md) (function, `0x005ED190`)

### Direct callers
- [RtlpNameprepAsciiRealWorker](../../text/5E/RtlpNameprepAsciiRealWorker_function_005ECDF8.md) at `0x005ED08F`

### Static image references
- `0x007927C0` → RVA `0x00031520` (`.rdata`; read)
- `0x007927CC` → RVA `0x00031510` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x00792782` → [FindLabelEnd](../../text/5E/FindLabelEnd_function_005ECAA4.md) (`PAGE` → `.text`)
  - `0x007927F9` → [RtlStringCchCopyNExW](../../text/43/RtlStringCchCopyNExW_function_00437CB0.md) (`PAGE` → `.text`)
  - `0x0079283D` → [ValidateStd3Range](../../text/5E/ValidateStd3Range_function_005ED154.md) (`PAGE` → `.text`)
  - `0x00792926` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (`PAGE` → `.text`)
  - `0x00792999` → [GetUTF32](../../text/5E/GetUTF32_function_005ECAE0.md) (`PAGE` → `.text`)
  - `0x007929EC` → [GetUTF32](../../text/5E/GetUTF32_function_005ECAE0.md) (`PAGE` → `.text`)
  - `0x00792AC8` → [adapt](../../text/5E/adapt_function_005ED190.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007926F4  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
007926F9  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
007926FE  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00792703  53                              push rbx
00792704  55                              push rbp
00792705  56                              push rsi
00792706  57                              push rdi
00792707  41 54                           push r12
00792709  41 55                           push r13
0079270B  41 56                           push r14
0079270D  41 57                           push r15
0079270F  48 81 EC 88 00 00 00            sub rsp, 0x88
00792716  48 63 C2                        movsxd rax, edx
00792719  4D 8B E1                        mov r12, r9
0079271C  49 8B D8                        mov rbx, r8
0079271F  45 33 DB                        xor r11d, r11d
00792722  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
00792727  4C 8B C9                        mov r9, rcx
0079272A  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
0079272F  48 8B F9                        mov rdi, rcx
00792732  4C 8D 3C 41                     lea r15, [rcx + rax*2]
00792736  49 63 04 24                     movsxd rax, dword ptr [r12]
0079273A  4C 89 7C 24 68                  mov qword ptr [rsp + 0x68], r15
0079273F  4C 8B F1                        mov r14, rcx
00792742  4D 8B D0                        mov r10, r8
00792745  49 8D 04 40                     lea rax, [r8 + rax*2]
00792749  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0079274E  85 D2                           test edx, edx
00792750  0F 8E 69 04 00 00               jle 0x140792bbf
00792756  40 8A B4 24 F0 00 00 00         mov sil, byte ptr [rsp + 0xf0]
0079275E  4C 8B E0                        mov r12, rax
00792761  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
00792766  41 BD 02 00 00 00               mov r13d, 2
0079276C  41 8D 6D 2B                     lea ebp, [r13 + 0x2b]
00792770  49 3B FF                        cmp rdi, r15
00792773  0F 83 64 04 00 00               jae 0x140792bdd
00792779  44 8A C6                        mov r8b, sil
0079277C  49 8B D7                        mov rdx, r15
0079277F  49 8B CE                        mov rcx, r14
00792782  E8 1D A3 E5 FF                  call 0x1405ecaa4
00792787  48 8B F8                        mov rdi, rax
0079278A  49 3B C6                        cmp rax, r14
0079278D  0F 84 1A 04 00 00               je 0x140792bad
00792793  40 84 F6                        test sil, sil
00792796  75 23                           jne 0x1407927bb
00792798  44 38 9C 24 F8 00 00 00         cmp byte ptr [rsp + 0xf8], r11b
007927A0  74 19                           je 0x1407927bb
007927A2  66 41 39 2E                     cmp word ptr [r14], bp
007927A6  0F 84 0B 04 00 00               je 0x140792bb7
007927AC  49 3B C1                        cmp rax, r9
007927AF  76 0A                           jbe 0x1407927bb
007927B1  66 39 68 FE                     cmp word ptr [rax - 2], bp
007927B5  0F 84 FC 03 00 00               je 0x140792bb7
007927BB  44 89 5C 24 30                  mov dword ptr [rsp + 0x30], r11d
007927C0  48 8D 05 59 ED 89 FF            lea rax, [rip - 0x7612a7]
007927C7  4C 89 5C 24 28                  mov qword ptr [rsp + 0x28], r11
007927CC  4C 8D 05 3D ED 89 FF            lea r8, [rip - 0x7612c3]
007927D3  40 84 F6                        test sil, sil
007927D6  49 8B D4                        mov rdx, r12
007927D9  41 B9 04 00 00 00               mov r9d, 4
007927DF  48 8B CB                        mov rcx, rbx
007927E2  4C 0F 44 C0                     cmove r8, rax
007927E6  48 2B D3                        sub rdx, rbx
007927E9  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
007927F1  48 D1 FA                        sar rdx, 1
007927F4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007927F9  E8 B2 54 CA FF                  call 0x140437cb0
007927FE  45 33 DB                        xor r11d, r11d
00792801  85 C0                           test eax, eax
00792803  0F 88 92 03 00 00               js 0x140792b9b
00792809  48 8B 9C 24 E0 00 00 00         mov rbx, qword ptr [rsp + 0xe0]
00792811  41 8B EB                        mov ebp, r11d
00792814  4D 8B C6                        mov r8, r14
00792817  4C 3B C7                        cmp r8, rdi
0079281A  0F 83 91 00 00 00               jae 0x1407928b1
00792820  41 0F B7 08                     movzx ecx, word ptr [r8]
00792824  B8 80 00 00 00                  mov eax, 0x80
00792829  66 3B C8                        cmp cx, ax
0079282C  73 66                           jae 0x140792894
0079282E  40 84 F6                        test sil, sil
00792831  75 27                           jne 0x14079285a
00792833  44 38 9C 24 F8 00 00 00         cmp byte ptr [rsp + 0xf8], r11b
0079283B  74 0D                           je 0x14079284a
0079283D  E8 12 A9 E5 FF                  call 0x1405ed154
00792842  84 C0                           test al, al
00792844  0F 84 6D 03 00 00               je 0x140792bb7
0079284A  66 83 F9 20                     cmp cx, 0x20
0079284E  0F 82 63 03 00 00               jb 0x140792bb7
00792854  66 83 F9 7F                     cmp cx, 0x7f
00792858  EB 03                           jmp 0x14079285d
0079285A  66 85 C9                        test cx, cx
0079285D  0F 84 54 03 00 00               je 0x140792bb7
00792863  49 3B DC                        cmp rbx, r12
00792866  0F 83 2F 03 00 00               jae 0x140792b9b
0079286C  40 84 F6                        test sil, sil
0079286F  75 11                           jne 0x140792882
00792871  8D 41 BF                        lea eax, [rcx - 0x41]
00792874  BA 19 00 00 00                  mov edx, 0x19
00792879  66 3B C2                        cmp ax, dx
0079287C  77 04                           ja 0x140792882
0079287E  66 83 C1 20                     add cx, 0x20
00792882  66 89 0B                        mov word ptr [rbx], cx
00792885  49 03 DD                        add rbx, r13
00792888  48 89 9C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rbx
00792890  FF C5                           inc ebp
00792892  EB 15                           jmp 0x1407928a9
00792894  B8 00 28 00 00                  mov eax, 0x2800
00792899  66 03 C8                        add cx, ax
0079289C  B8 FF 03 00 00                  mov eax, 0x3ff
007928A1  66 3B C8                        cmp cx, ax
007928A4  77 03                           ja 0x1407928a9
007928A6  4D 03 C5                        add r8, r13
007928A9  4D 03 C5                        add r8, r13
007928AC  E9 66 FF FF FF                  jmp 0x140792817
007928B1  4C 8B EF                        mov r13, rdi
007928B4  48 63 C5                        movsxd rax, ebp
007928B7  4D 2B EE                        sub r13, r14
007928BA  89 6C 24 44                     mov dword ptr [rsp + 0x44], ebp
007928BE  49 D1 FD                        sar r13, 1
007928C1  49 3B C5                        cmp rax, r13
007928C4  75 32                           jne 0x1407928f8
007928C6  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
007928CB  48 8D 53 F8                     lea rdx, [rbx - 8]
007928CF  49 8B C8                        mov rcx, r8
007928D2  4C 3B C2                        cmp r8, rdx
007928D5  73 10                           jae 0x1407928e7
007928D7  0F B7 41 08                     movzx eax, word ptr [rcx + 8]
007928DB  66 89 01                        mov word ptr [rcx], ax
007928DE  48 83 C1 02                     add rcx, 2
007928E2  48 3B CA                        cmp rcx, rdx
007928E5  72 F0                           jb 0x1407928d7
007928E7  48 83 EB 08                     sub rbx, 8
007928EB  48 89 9C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rbx
007928F3  E9 41 02 00 00                  jmp 0x140792b39
007928F8  49 8B C7                        mov rax, r15
007928FB  49 2B C6                        sub rax, r14
007928FE  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00792902  48 83 F8 08                     cmp rax, 8
00792906  7C 2E                           jl 0x140792936
00792908  48 8D 05 11 EC 89 FF            lea rax, [rip - 0x7613ef]
0079290F  40 84 F6                        test sil, sil
00792912  48 8D 15 F7 EB 89 FF            lea rdx, [rip - 0x761409]
00792919  41 B8 04 00 00 00               mov r8d, 4
0079291F  48 0F 44 D0                     cmove rdx, rax
00792923  49 8B CE                        mov rcx, r14
00792926  E8 95 D8 D6 FF                  call 0x1405001c0
0079292B  45 33 DB                        xor r11d, r11d
0079292E  85 C0                           test eax, eax
00792930  0F 84 81 02 00 00               je 0x140792bb7
00792936  41 8B D3                        mov edx, r11d
00792939  89 94 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], edx
00792940  85 ED                           test ebp, ebp
00792942  7E 21                           jle 0x140792965
00792944  49 3B DC                        cmp rbx, r12
00792947  0F 83 4E 02 00 00               jae 0x140792b9b
0079294D  41 BC 02 00 00 00               mov r12d, 2
00792953  66 C7 03 2D 00                  mov word ptr [rbx], 0x2d
00792958  49 03 DC                        add rbx, r12
0079295B  48 89 9C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rbx
00792963  EB 06                           jmp 0x14079296b
00792965  41 BC 02 00 00 00               mov r12d, 2
0079296B  41 BF 80 00 00 00               mov r15d, 0x80
00792971  C7 44 24 40 48 00 00 00         mov dword ptr [rsp + 0x40], 0x48
00792979  45 8B D3                        mov r10d, r11d
0079297C  48 63 C5                        movsxd rax, ebp
0079297F  49 3B C5                        cmp rax, r13
00792982  0F 8D 9F 01 00 00               jge 0x140792b27
00792988  41 BB FF FF FF 07               mov r11d, 0x7ffffff
0079298E  4D 8B CE                        mov r9, r14
00792991  4C 3B F7                        cmp r14, rdi
00792994  73 31                           jae 0x1407929c7
00792996  49 8B C9                        mov rcx, r9
00792999  E8 42 A1 E5 FF                  call 0x1405ecae0
0079299E  41 3B C7                        cmp eax, r15d
007929A1  7C 07                           jl 0x1407929aa
007929A3  41 3B C3                        cmp eax, r11d
007929A6  44 0F 4C D8                     cmovl r11d, eax
007929AA  3D 00 00 01 00                  cmp eax, 0x10000
007929AF  B9 04 00 00 00                  mov ecx, 4
007929B4  49 0F 4C CC                     cmovl rcx, r12
007929B8  4C 03 C9                        add r9, rcx
007929BB  4C 3B CF                        cmp r9, rdi
007929BE  72 D6                           jb 0x140792996
007929C0  8B 94 24 D8 00 00 00            mov edx, dword ptr [rsp + 0xd8]
007929C7  8B CD                           mov ecx, ebp
007929C9  41 8B C3                        mov eax, r11d
007929CC  2B CA                           sub ecx, edx
007929CE  41 2B C7                        sub eax, r15d
007929D1  FF C1                           inc ecx
007929D3  4D 8B E6                        mov r12, r14
007929D6  0F AF C8                        imul ecx, eax
007929D9  44 03 D1                        add r10d, ecx
007929DC  45 8D 4A 01                     lea r9d, [r10 + 1]
007929E0  4C 3B E7                        cmp r12, rdi
007929E3  0F 83 2C 01 00 00               jae 0x140792b15
007929E9  49 8B CC                        mov rcx, r12
007929EC  E8 EF A0 E5 FF                  call 0x1405ecae0
007929F1  41 3B C3                        cmp eax, r11d
007929F4  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
007929F8  45 0F 4D CA                     cmovge r9d, r10d
007929FC  45 8B D1                        mov r10d, r9d
007929FF  0F 85 EE 00 00 00               jne 0x140792af3
00792A05  BA 02 00 00 00                  mov edx, 2
00792A0A  45 8B F9                        mov r15d, r9d
00792A0D  44 8D 4A 22                     lea r9d, [rdx + 0x22]
00792A11  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
00792A15  44 3B C9                        cmp r9d, ecx
00792A18  7F 08                           jg 0x140792a22
00792A1A  41 B8 01 00 00 00               mov r8d, 1
00792A20  EB 16                           jmp 0x140792a38
00792A22  8D 41 1A                        lea eax, [rcx + 0x1a]
00792A25  44 3B C8                        cmp r9d, eax
00792A28  7C 08                           jl 0x140792a32
00792A2A  41 B8 1A 00 00 00               mov r8d, 0x1a
00792A30  EB 06                           jmp 0x140792a38
00792A32  45 8B C1                        mov r8d, r9d
00792A35  44 2B C1                        sub r8d, ecx
00792A38  45 3B F8                        cmp r15d, r8d
00792A3B  7C 46                           jl 0x140792a83
00792A3D  48 3B 5C 24 50                  cmp rbx, qword ptr [rsp + 0x50]
00792A42  0F 83 50 01 00 00               jae 0x140792b98
00792A48  45 2B F8                        sub r15d, r8d
00792A4B  B9 24 00 00 00                  mov ecx, 0x24
00792A50  41 2B C8                        sub ecx, r8d
00792A53  41 8B C7                        mov eax, r15d
00792A56  99                              cdq
00792A57  F7 F9                           idiv ecx
00792A59  44 8B F8                        mov r15d, eax
00792A5C  42 8D 0C 02                     lea ecx, [rdx + r8]
00792A60  BA 16 00 00 00                  mov edx, 0x16
00792A65  8D 42 03                        lea eax, [rdx + 3]
00792A68  3B C8                           cmp ecx, eax
00792A6A  8D 42 4B                        lea eax, [rdx + 0x4b]
00792A6D  66 0F 4E D0                     cmovle dx, ax
00792A71  66 03 D1                        add dx, cx
00792A74  66 89 13                        mov word ptr [rbx], dx
00792A77  8D 50 A1                        lea edx, [rax - 0x5f]
00792A7A  48 03 DA                        add rbx, rdx
00792A7D  41 83 C1 24                     add r9d, 0x24
00792A81  EB 8E                           jmp 0x140792a11
00792A83  48 3B 5C 24 50                  cmp rbx, qword ptr [rsp + 0x50]
00792A88  0F 83 0A 01 00 00               jae 0x140792b98
00792A8E  B8 16 00 00 00                  mov eax, 0x16
00792A93  8D 48 03                        lea ecx, [rax + 3]
00792A96  44 3B F9                        cmp r15d, ecx
00792A99  8D 48 4B                        lea ecx, [rax + 0x4b]
00792A9C  66 0F 4E C1                     cmovle ax, cx
00792AA0  41 8B CA                        mov ecx, r10d
00792AA3  66 41 03 C7                     add ax, r15w
00792AA7  66 89 03                        mov word ptr [rbx], ax
00792AAA  48 03 DA                        add rbx, rdx
00792AAD  3B 6C 24 44                     cmp ebp, dword ptr [rsp + 0x44]
00792AB1  8B D5                           mov edx, ebp
00792AB3  48 89 9C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rbx
00792ABB  41 0F 94 C0                     sete r8b
00792ABF  2B 94 24 D8 00 00 00            sub edx, dword ptr [rsp + 0xd8]
00792AC6  FF C2                           inc edx
00792AC8  E8 C3 A6 E5 FF                  call 0x1405ed190
00792ACD  8B 94 24 D8 00 00 00            mov edx, dword ptr [rsp + 0xd8]
00792AD4  45 33 D2                        xor r10d, r10d
00792AD7  FF C5                           inc ebp
00792AD9  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00792ADD  41 81 FB 00 00 01 00            cmp r11d, 0x10000
00792AE4  7C 14                           jl 0x140792afa
00792AE6  FF C5                           inc ebp
00792AE8  FF C2                           inc edx
00792AEA  89 94 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], edx
00792AF1  EB 07                           jmp 0x140792afa
00792AF3  8B 94 24 D8 00 00 00            mov edx, dword ptr [rsp + 0xd8]
00792AFA  81 7C 24 48 00 00 01 00         cmp dword ptr [rsp + 0x48], 0x10000
00792B02  B9 04 00 00 00                  mov ecx, 4
00792B07  8D 41 FE                        lea eax, [rcx - 2]
00792B0A  0F 4C C8                        cmovl ecx, eax
00792B0D  4C 03 E1                        add r12, rcx
00792B10  E9 C7 FE FF FF                  jmp 0x1407929dc
00792B15  45 8B D1                        mov r10d, r9d
00792B18  45 8D 7B 01                     lea r15d, [r11 + 1]
00792B1C  41 BC 02 00 00 00               mov r12d, 2
00792B22  E9 55 FE FF FF                  jmp 0x14079297c
00792B27  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
00792B2C  45 33 DB                        xor r11d, r11d
00792B2F  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
00792B34  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00792B39  40 84 F6                        test sil, sil
00792B3C  75 10                           jne 0x140792b4e
00792B3E  48 8B C3                        mov rax, rbx
00792B41  49 2B C0                        sub rax, r8
00792B44  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00792B48  48 83 F8 7E                     cmp rax, 0x7e
00792B4C  7F 69                           jg 0x140792bb7
00792B4E  49 3B FF                        cmp rdi, r15
00792B51  74 2F                           je 0x140792b82
00792B53  49 3B DC                        cmp rbx, r12
00792B56  73 43                           jae 0x140792b9b
00792B58  0F B7 07                        movzx eax, word ptr [rdi]
00792B5B  66 89 03                        mov word ptr [rbx], ax
00792B5E  48 83 C3 02                     add rbx, 2
00792B62  48 89 9C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rbx
00792B6A  40 84 F6                        test sil, sil
00792B6D  74 13                           je 0x140792b82
00792B6F  66 83 3F 40                     cmp word ptr [rdi], 0x40
00792B73  75 0D                           jne 0x140792b82
00792B75  41 8A F3                        mov sil, r11b
00792B78  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
00792B7D  4C 8B D3                        mov r10, rbx
00792B80  EB 05                           jmp 0x140792b87
00792B82  4C 8B 54 24 58                  mov r10, qword ptr [rsp + 0x58]
00792B87  4C 8B 8C 24 D0 00 00 00         mov r9, qword ptr [rsp + 0xd0]
00792B8F  4C 8D 77 02                     lea r14, [rdi + 2]
00792B93  E9 C9 FB FF FF                  jmp 0x140792761
00792B98  45 33 DB                        xor r11d, r11d
00792B9B  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
00792BA3  44 89 18                        mov dword ptr [rax], r11d
00792BA6  B8 23 00 00 C0                  mov eax, 0xc0000023
00792BAB  EB 1B                           jmp 0x140792bc8
00792BAD  40 84 F6                        test sil, sil
00792BB0  75 05                           jne 0x140792bb7
00792BB2  49 3B FF                        cmp rdi, r15
00792BB5  74 2B                           je 0x140792be2
00792BB7  4C 8B A4 24 E8 00 00 00         mov r12, qword ptr [rsp + 0xe8]
00792BBF  45 89 1C 24                     mov dword ptr [r12], r11d
00792BC3  B8 16 07 00 C0                  mov eax, 0xc0000716
00792BC8  48 81 C4 88 00 00 00            add rsp, 0x88
00792BCF  41 5F                           pop r15
00792BD1  41 5E                           pop r14
00792BD3  41 5D                           pop r13
00792BD5  41 5C                           pop r12
00792BD7  5F                              pop rdi
00792BD8  5E                              pop rsi
00792BD9  5D                              pop rbp
00792BDA  5B                              pop rbx
00792BDB  C3                              ret
00792BDC  CC                              int3
00792BDD  40 84 F6                        test sil, sil
00792BE0  75 23                           jne 0x140792c05
00792BE2  0F B7 43 FE                     movzx eax, word ptr [rbx - 2]
00792BE6  66 83 E8 2E                     sub ax, 0x2e
00792BEA  66 F7 D8                        neg ax
00792BED  48 8B C3                        mov rax, rbx
00792BF0  48 1B C9                        sbb rcx, rcx
00792BF3  49 2B C2                        sub rax, r10
00792BF6  48 D1 F8                        sar rax, 1
00792BF9  48 81 C1 FF 00 00 00            add rcx, 0xff
00792C00  48 3B C1                        cmp rax, rcx
00792C03  7F B2                           jg 0x140792bb7
00792C05  66 83 7B FE 40                  cmp word ptr [rbx - 2], 0x40
00792C0A  74 AB                           je 0x140792bb7
00792C0C  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
00792C14  48 2B 5C 24 70                  sub rbx, qword ptr [rsp + 0x70]
00792C19  48 D1 FB                        sar rbx, 1
00792C1C  89 18                           mov dword ptr [rax], ebx
00792C1E  33 C0                           xor eax, eax
00792C20  EB A6                           jmp 0x140792bc8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall punycode_encode(__int64 a1, int a2, __int64 a3, __int64 a4, unsigned __int8 a5, unsigned __int8 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pE8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (136);
    v_r11 = 0;
    v_stack_m70 = a3;
    v_stack_m58 = a3;
    v_stack_m60 = a1 + (int)(a2) * 2;
    v_stack_m78 = a3 + (int)(*(unsigned int *)(a4)) * 2;
    if (condition_is_less_or_equal) goto loc_00792BBF;
loc_00792761:
    v_stack_m68 = a3;
    if (a1 >= (a1 + (int)(a2) * 2)) goto loc_00792BDD;
    result = FindLabelEnd(a1, a1 + (int)(a2) * 2, a5, a1);
    if (result == a1) goto loc_00792BAD;
    if (a5 != 0) goto loc_007927BB;
    if (a6 == 0) goto loc_007927BB;
    if ((*(unsigned __int16 *)(a1)) == ((unsigned __int16)(2 + 43))) goto loc_00792BB7;
    if (result <= a1) goto loc_007927BB;
    if ((*(unsigned __int16 *)(result - 2)) == ((unsigned __int16)(2 + 43))) goto loc_00792BB7;
loc_007927BB:
    v_stack_m98 = 0;
    v_stack_mA0 = 0;
    a3 = v_rip - 7738051;
    if (a5 == 0) { a3 = v_rip - 7738023; }
    a2 = (a3 + (int)(*(unsigned int *)(a4)) * 2) - (a3);
    a2 = (a2) >> (1);
    v_stack_mA8 = v_stack_p18;
    result = RtlStringCchCopyNExW(a3, a2, a3, 4);
    v_r11 = 0;
    if (sign_flag) goto loc_00792B9B;
loc_00792817:
    if (a1 >= result) goto loc_007928B1;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1))) >= 128) goto loc_00792894;
    if (a5 != 0) goto loc_0079285A;
    if (a6 == 0) goto loc_0079284A;
    result = ValidateStd3Range(*(unsigned __int16 *)(a1), a2, a1, 4);
    if ((unsigned __int8)(result) == 0) goto loc_00792BB7;
loc_0079284A:
    if (((unsigned __int16)(*(unsigned __int16 *)(a1))) < 32) goto loc_00792BB7;
    goto loc_0079285D;
loc_0079285A:
loc_0079285D:
    if ((unsigned __int16)(*(unsigned __int16 *)(a1)) == 0) goto loc_00792BB7;
    if (v_stack_p18 >= (a3 + (int)(*(unsigned int *)(a4)) * 2)) goto loc_00792B9B;
    if (a5 != 0) goto loc_00792882;
    if (((unsigned __int16)(*(unsigned __int16 *)(a1) - 65)) <= 25) {
        a1 = (unsigned __int16)((*(unsigned __int16 *)(a1)) + (32));
    }
    *(unsigned __int16 *)(v_stack_p18) = (unsigned __int16)(a1);
    v_rbx = (v_stack_p18) + (2);
    v_stack_p18 = v_rbx;
    v_rbp = (unsigned int)((0) + 1);
    goto loc_007928A9;
loc_00792894:
    a1 = (unsigned __int16)((a1) + ((unsigned __int16)((unsigned int)(0x2800ULL))));
    if (((unsigned __int16)(a1)) <= ((unsigned __int16)((unsigned int)(0x3FFULL)))) {
        a3 = (a1) + (2);
    }
    a3 = (a3) + (2);
    goto loc_00792817;
loc_007928B1:
    v_r13 = (result) - (a1);
    v_stack_m84 = (unsigned int)(v_rbp);
    v_r13 = (v_r13) >> (1);
    if (((int)((unsigned int)(v_rbp))) != v_r13) goto loc_007928F8;
    if (v_stack_m68 >= (v_rbx - 8)) goto loc_007928E7;
loc_007928D7:
    *(unsigned __int16 *)(v_stack_m68) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m68 + 8));
    a1 = (v_stack_m68) + (2);
    if (a1 < (v_rbx - 8)) goto loc_007928D7;
loc_007928E7:
    v_rbx = (v_rbx) - (8);
    v_stack_p18 = v_rbx;
    goto loc_00792B39;
loc_007928F8:
    result = (a1 + (int)(a2) * 2) - (a1);
    result = (result) & (-2);
    if (result < 8) goto loc_00792936;
    a2 = v_rip - 7738377;
    if (a5 == 0) { a2 = v_rip - 7738351; }
    result = wcsnicmp(a1, a2, 4, 4);
    v_r11 = 0;
    if ((unsigned int)(result) == 0) goto loc_00792BB7;
loc_00792936:
    v_stack_p10 = 0;
    if (condition_is_less_or_equal) goto loc_00792965;
    if (v_rbx >= (a3 + (int)(*(unsigned int *)(a4)) * 2)) goto loc_00792B9B;
    *(unsigned __int16 *)(v_rbx) = 45;
    v_rbx = (v_rbx) + (2);
    v_stack_p18 = v_rbx;
    goto loc_0079296B;
loc_00792965:
loc_0079296B:
    v_stack_m88 = 72;
loc_0079297C:
    if (((int)((unsigned int)(v_rbp))) >= v_r13) goto loc_00792B27;
    if (a1 >= result) goto loc_007929C7;
loc_00792996:
    result = GetUTF32(a1, 0, 4, a1);
    v_r11 = (unsigned int)(0x7FFFFFFULL);
    if (((unsigned int)(result)) >= 128) {
        v_r11 = (unsigned int)(0x7FFFFFFULL);
        if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(0x7FFFFFFULL)))) { v_r11 = (unsigned int)(result); }
    }
    a1 = 4;
    if (((unsigned int)(result)) < 0x10000ULL) { a1 = 2; }
    a4 = (a1) + (a1);
    if (a4 < result) goto loc_00792996;
loc_007929C7:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbp))) - ((unsigned int)((unsigned int)(v_stack_p10))));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r11))) - (128));
    a1 = (unsigned int)((a1) + 1);
    a1 = (unsigned int)((a1) * ((unsigned int)(result)));
    v_r10 = (unsigned int)((0) + ((unsigned int)(a1)));
loc_007929DC:
    if (a1 >= result) goto loc_00792B15;
    result = GetUTF32(a1, (unsigned int)(v_stack_p10), 4, v_r10 + 1);
    v_stack_m80 = (unsigned int)(result);
    a4 = v_r10 + 1;
    if (((unsigned int)(result)) >= ((unsigned int)(v_r11))) { a4 = (unsigned int)(v_r10); }
    if (((unsigned int)(result)) != ((unsigned int)(v_r11))) goto loc_00792AF3;
loc_00792A11:
    if (((unsigned int)(2 + 34)) > ((unsigned int)((unsigned int)(v_stack_m88)))) goto loc_00792A22;
    goto loc_00792A38;
loc_00792A22:
    if (((unsigned int)(2 + 34)) < ((unsigned int)((unsigned int)(v_stack_m88) + 26))) goto loc_00792A32;
    goto loc_00792A38;
loc_00792A32:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(2 + 34))) - ((unsigned int)((unsigned int)(v_stack_m88))));
loc_00792A38:
    if (((unsigned int)((unsigned int)((unsigned int)(a4)))) < ((unsigned int)(a3))) goto loc_00792A83;
    if (v_rbx >= v_stack_m78) goto loc_00792B98;
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(a4))) - ((unsigned int)(a3)));
    a1 = (unsigned int)((36) - ((unsigned int)(a3)));
    a2 = 22;
    if (((unsigned int)(2 + a3 * 1)) <= ((unsigned int)(22 + 3))) { a2 = (unsigned __int16)(22 + 75); }
    a2 = (unsigned __int16)((a2) + ((unsigned __int16)(2 + a3 * 1)));
    *(unsigned __int16 *)(v_rbx) = (unsigned __int16)(a2);
    v_rbx = (v_rbx) + (22 + 75 - 95);
    a4 = (unsigned int)((2 + 34) + (36));
    goto loc_00792A11;
loc_00792A83:
    if (v_rbx >= v_stack_m78) goto loc_00792B98;
    result = 22;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r15)))))) <= ((unsigned int)(22 + 3))) { result = (unsigned __int16)(22 + 75); }
    result = (unsigned __int16)((result) + ((unsigned __int16)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r15)))))));
    *(unsigned __int16 *)(v_rbx) = (unsigned __int16)(result);
    v_rbx = (v_rbx) + (22 + 75 - 95);
    v_stack_p18 = v_rbx;
    a3 = (((unsigned int)(v_rbp)) == v_stack_m84) ? 1 : 0;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rbp))) - (v_stack_p10));
    a2 = (unsigned int)((a2) + 1);
    result = adapt((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4)))), a2, a3, a4);
    v_r10 = 0;
    v_rbp = (unsigned int)((v_rbp) + 1);
    v_stack_m88 = (unsigned int)(result);
    if (((unsigned int)(v_r11)) < 0x10000ULL) goto loc_00792AFA;
    v_rbp = (unsigned int)((v_rbp) + 1);
    a2 = (unsigned int)(((unsigned int)(v_stack_p10)) + 1);
    v_stack_p10 = a2;
    goto loc_00792AFA;
loc_00792AF3:
loc_00792AFA:
    a1 = 4;
    if (v_stack_m80 < 0x10000ULL) { a1 = (unsigned int)(4 - 2); }
    v_r12 = (a1) + (a1);
    goto loc_007929DC;
loc_00792B15:
    goto loc_0079297C;
loc_00792B27:
    v_r11 = 0;
loc_00792B39:
    if (a5 != 0) goto loc_00792B4E;
    result = (v_rbx) - (v_stack_m68);
    result = (result) & (-2);
    if (result > 126) goto loc_00792BB7;
loc_00792B4E:
    if (result == v_stack_m60) goto loc_00792B82;
    if (v_rbx >= v_stack_m78) goto loc_00792B9B;
    *(unsigned __int16 *)(v_rbx) = (unsigned __int16)(*(unsigned __int16 *)(result));
    v_rbx = (v_rbx) + (2);
    v_stack_p18 = v_rbx;
    if (a5 == 0) goto loc_00792B82;
    if ((*(unsigned __int16 *)(result)) != 64) goto loc_00792B82;
    v_stack_m70 = v_rbx;
    goto loc_00792B87;
loc_00792B82:
loc_00792B87:
    goto loc_00792761;
loc_00792B98:
    v_r11 = 0;
loc_00792B9B:
    *(unsigned int *)(v_stack_p20) = 0;
    goto loc_00792BC8;
loc_00792BAD:
    if (0 != 0) goto loc_00792BB7;
    if (result == v_stack_m60) goto loc_00792BE2;
loc_00792BB7:
loc_00792BBF:
    *(unsigned int *)(v_stack_p20) = 0;
loc_00792BC8:
    v_rsp = (v_rsp) + (136);
    return (unsigned int)(0xC0000716ULL);
loc_00792BDD:
    if (0 != 0) goto loc_00792C05;
loc_00792BE2:
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rbx - 2)) - (46));
    result = (unsigned __int16)(-(result));
    result = (v_rbx) - (v_stack_m70);
    result = (result) >> (1);
    a1 = (a1) + (255);
    if (result > a1) goto loc_00792BB7;
loc_00792C05:
    if ((*(unsigned __int16 *)(v_rbx - 2)) == 64) goto loc_00792BB7;
    v_rbx = (v_rbx) - (v_stack_p70);
    v_rbx = (v_rbx) >> (1);
    *(unsigned int *)(v_stack_pE8) = (unsigned int)(v_rbx);
    result = 0;
    goto loc_00792BC8;
}
```

## 5. (Beta) C Style

```c
int64_t punycode_encode(void *Arg1, int32_t Arg2, void *Arg3, void *Arg4, uint8_t Arg5, uint8_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p70;
    uint64_t v_stack_p8;
    uint64_t v_stack_pE8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (136);
    local_r11 = 0;
    v_stack_m70 = Arg3;
    v_stack_m58 = Arg3;
    v_stack_m60 = Arg1 + (int32_t)(Arg2) * 2;
    v_stack_m78 = Arg3 + (int32_t)(*(uint32_t *)(arg4)) * 2;
    if (condition_is_less_or_equal) goto loc_00792BBF;
loc_00792761:
    v_stack_m68 = Arg3;
    if (Arg1 >= (Arg1 + (int32_t)(Arg2) * 2)) goto loc_00792BDD;
    result = FindLabelEnd(Arg1, Arg1 + (int32_t)(Arg2) * 2, Arg5, Arg1);
    if (result == Arg1) goto loc_00792BAD;
    if (Arg5 != 0) goto loc_007927BB;
    if (Arg6 == 0) goto loc_007927BB;
    if ((*(uint16_t *)(arg1)) == ((uint16_t)(2 + 43))) goto loc_00792BB7;
    if (result <= Arg1) goto loc_007927BB;
    if ((*(uint16_t *)(result - 0x2)) == ((uint16_t)(2 + 43))) goto loc_00792BB7;
loc_007927BB:
    v_stack_m98 = 0;
    v_stack_mA0 = 0;
    Arg3 = v_rip - 7738051;
    if (Arg5 == 0) { Arg3 = v_rip - 7738023; }
    Arg2 = (Arg3 + (int32_t)(*(uint32_t *)(arg4)) * 2) - (Arg3);
    Arg2 = (Arg2) >> (1);
    v_stack_mA8 = v_stack_p18;
    result = RtlStringCchCopyNExW(Arg3, Arg2, Arg3, 4);
    local_r11 = 0;
    if (sign_flag) goto loc_00792B9B;
loc_00792817:
    if (Arg1 >= result) goto loc_007928B1;
    if (((uint16_t)(*(uint16_t *)(arg1))) >= 128) goto loc_00792894;
    if (Arg5 != 0) goto loc_0079285A;
    if (Arg6 == 0) goto loc_0079284A;
    result = ValidateStd3Range(*(uint16_t *)(arg1), Arg2, Arg1, 4);
    if ((uint8_t)(result) == 0) goto loc_00792BB7;
loc_0079284A:
    if (((uint16_t)(*(uint16_t *)(arg1))) < 32) goto loc_00792BB7;
    goto loc_0079285D;
loc_0079285A:
loc_0079285D:
    if ((uint16_t)(*(uint16_t *)(arg1)) == 0) goto loc_00792BB7;
    if (v_stack_p18 >= (Arg3 + (int32_t)(*(uint32_t *)(arg4)) * 2)) goto loc_00792B9B;
    if (Arg5 != 0) goto loc_00792882;
    if (((uint16_t)(*(uint16_t *)(arg1) - 65)) <= 25) {
        Arg1 = (uint16_t)((*(uint16_t *)(arg1)) + (32));
    }
    *(uint16_t *)(v_stack_p18) = (uint16_t)(Arg1);
    local_rbx = (v_stack_p18) + (2);
    v_stack_p18 = local_rbx;
    local_rbp = (uint32_t)((0) + 1);
    goto loc_007928A9;
loc_00792894:
    Arg1 = (uint16_t)((Arg1) + ((uint16_t)((uint32_t)(0x2800ULL))));
    if (((uint16_t)(Arg1)) <= ((uint16_t)((uint32_t)(0x3FFULL)))) {
        Arg3 = (Arg1) + (2);
    }
    Arg3 = (Arg3) + (2);
    goto loc_00792817;
loc_007928B1:
    local_r13 = (result) - (Arg1);
    v_stack_m84 = (uint32_t)(local_rbp);
    local_r13 = (local_r13) >> (1);
    if (((int32_t)((uint32_t)(local_rbp))) != local_r13) goto loc_007928F8;
    if (v_stack_m68 >= (local_rbx - 8)) goto loc_007928E7;
loc_007928D7:
    *(uint16_t *)(v_stack_m68) = (uint16_t)(*(uint16_t *)(v_stack_m68 + 0x8));
    Arg1 = (v_stack_m68) + (2);
    if (Arg1 < (local_rbx - 8)) goto loc_007928D7;
loc_007928E7:
    local_rbx = (local_rbx) - (8);
    v_stack_p18 = local_rbx;
    goto loc_00792B39;
loc_007928F8:
    result = (Arg1 + (int32_t)(Arg2) * 2) - (Arg1);
    result = (result) & (-2);
    if (result < 8) goto loc_00792936;
    Arg2 = v_rip - 7738377;
    if (Arg5 == 0) { Arg2 = v_rip - 7738351; }
    result = wcsnicmp(Arg1, Arg2, 4, 4);
    local_r11 = 0;
    if ((uint32_t)(result) == 0) goto loc_00792BB7;
loc_00792936:
    v_stack_p10 = 0;
    if (condition_is_less_or_equal) goto loc_00792965;
    if (local_rbx >= (Arg3 + (int32_t)(*(uint32_t *)(arg4)) * 2)) goto loc_00792B9B;
    *(uint16_t *)(local_rbx) = 45;
    local_rbx = (local_rbx) + (2);
    v_stack_p18 = local_rbx;
    goto loc_0079296B;
loc_00792965:
loc_0079296B:
    v_stack_m88 = 72;
loc_0079297C:
    if (((int32_t)((uint32_t)(local_rbp))) >= local_r13) goto loc_00792B27;
    if (Arg1 >= result) goto loc_007929C7;
loc_00792996:
    result = GetUTF32(Arg1, 0, 4, Arg1);
    local_r11 = (uint32_t)(0x7FFFFFFULL);
    if (((uint32_t)(result)) >= 128) {
        local_r11 = (uint32_t)(0x7FFFFFFULL);
        if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(0x7FFFFFFULL)))) { local_r11 = (uint32_t)(result); }
    }
    Arg1 = 4;
    if (((uint32_t)(result)) < 0x10000ULL) { Arg1 = 2; }
    Arg4 = (Arg1) + (Arg1);
    if (Arg4 < result) goto loc_00792996;
loc_007929C7:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbp))) - ((uint32_t)((uint32_t)(v_stack_p10))));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r11))) - (128));
    Arg1 = (uint32_t)((Arg1) + 1);
    Arg1 = (uint32_t)((Arg1) * ((uint32_t)(result)));
    local_r10 = (uint32_t)((0) + ((uint32_t)(Arg1)));
loc_007929DC:
    if (Arg1 >= result) goto loc_00792B15;
    result = GetUTF32(Arg1, (uint32_t)(v_stack_p10), 4, local_r10 + 1);
    v_stack_m80 = (uint32_t)(result);
    Arg4 = local_r10 + 1;
    if (((uint32_t)(result)) >= ((uint32_t)(local_r11))) { Arg4 = (uint32_t)(local_r10); }
    if (((uint32_t)(result)) != ((uint32_t)(local_r11))) goto loc_00792AF3;
loc_00792A11:
    if (((uint32_t)(2 + 34)) > ((uint32_t)((uint32_t)(v_stack_m88)))) goto loc_00792A22;
    goto loc_00792A38;
loc_00792A22:
    if (((uint32_t)(2 + 34)) < ((uint32_t)((uint32_t)(v_stack_m88) + 26))) goto loc_00792A32;
    goto loc_00792A38;
loc_00792A32:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(2 + 34))) - ((uint32_t)((uint32_t)(v_stack_m88))));
loc_00792A38:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg4)))) < ((uint32_t)(Arg3))) goto loc_00792A83;
    if (local_rbx >= v_stack_m78) goto loc_00792B98;
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) - ((uint32_t)(Arg3)));
    Arg1 = (uint32_t)((36) - ((uint32_t)(Arg3)));
    Arg2 = 22;
    if (((uint32_t)(2 + Arg3 * 1)) <= ((uint32_t)(22 + 3))) { Arg2 = (uint16_t)(22 + 75); }
    Arg2 = (uint16_t)((Arg2) + ((uint16_t)(2 + Arg3 * 1)));
    *(uint16_t *)(local_rbx) = (uint16_t)(Arg2);
    local_rbx = (local_rbx) + (22 + 75 - 95);
    Arg4 = (uint32_t)((2 + 34) + (36));
    goto loc_00792A11;
loc_00792A83:
    if (local_rbx >= v_stack_m78) goto loc_00792B98;
    result = 22;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r15)))))) <= ((uint32_t)(22 + 3))) { result = (uint16_t)(22 + 75); }
    result = (uint16_t)((result) + ((uint16_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r15)))))));
    *(uint16_t *)(local_rbx) = (uint16_t)(result);
    local_rbx = (local_rbx) + (22 + 75 - 95);
    v_stack_p18 = local_rbx;
    Arg3 = (((uint32_t)(local_rbp)) == v_stack_m84) ? 1 : 0;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rbp))) - (v_stack_p10));
    Arg2 = (uint32_t)((Arg2) + 1);
    result = adapt((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4)))), Arg2, Arg3, Arg4);
    local_r10 = 0;
    local_rbp = (uint32_t)((local_rbp) + 1);
    v_stack_m88 = (uint32_t)(result);
    if (((uint32_t)(local_r11)) < 0x10000ULL) goto loc_00792AFA;
    local_rbp = (uint32_t)((local_rbp) + 1);
    Arg2 = (uint32_t)(((uint32_t)(v_stack_p10)) + 1);
    v_stack_p10 = Arg2;
    goto loc_00792AFA;
loc_00792AF3:
loc_00792AFA:
    Arg1 = 4;
    if (v_stack_m80 < 0x10000ULL) { Arg1 = (uint32_t)(4 - 2); }
    local_r12 = (Arg1) + (Arg1);
    goto loc_007929DC;
loc_00792B15:
    goto loc_0079297C;
loc_00792B27:
    local_r11 = 0;
loc_00792B39:
    if (Arg5 != 0) goto loc_00792B4E;
    result = (local_rbx) - (v_stack_m68);
    result = (result) & (-2);
    if (result > 126) goto loc_00792BB7;
loc_00792B4E:
    if (result == v_stack_m60) goto loc_00792B82;
    if (local_rbx >= v_stack_m78) goto loc_00792B9B;
    *(uint16_t *)(local_rbx) = (uint16_t)(*(uint16_t *)(result));
    local_rbx = (local_rbx) + (2);
    v_stack_p18 = local_rbx;
    if (Arg5 == 0) goto loc_00792B82;
    if ((*(uint16_t *)(result)) != 64) goto loc_00792B82;
    v_stack_m70 = local_rbx;
    goto loc_00792B87;
loc_00792B82:
loc_00792B87:
    goto loc_00792761;
loc_00792B98:
    local_r11 = 0;
loc_00792B9B:
    *(uint32_t *)(v_stack_p20) = 0;
    goto loc_00792BC8;
loc_00792BAD:
    if (0 != 0) goto loc_00792BB7;
    if (result == v_stack_m60) goto loc_00792BE2;
loc_00792BB7:
loc_00792BBF:
    *(uint32_t *)(v_stack_p20) = 0;
loc_00792BC8:
    local_rsp = (local_rsp) + (136);
    return (uint32_t)(0xC0000716ULL);
loc_00792BDD:
    if (0 != 0) goto loc_00792C05;
loc_00792BE2:
    result = (uint16_t)((*(uint16_t *)(local_rbx - 0x2)) - (46));
    result = (uint16_t)(-(result));
    result = (local_rbx) - (v_stack_m70);
    result = (result) >> (1);
    Arg1 = (Arg1) + (255);
    if (result > Arg1) goto loc_00792BB7;
loc_00792C05:
    if ((*(uint16_t *)(local_rbx - 0x2)) == 64) goto loc_00792BB7;
    local_rbx = (local_rbx) - (v_stack_p70);
    local_rbx = (local_rbx) >> (1);
    *(uint32_t *)(v_stack_pE8) = (uint32_t)(local_rbx);
    result = 0;
    goto loc_00792BC8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rax*2` | `64` | `R` |
| `Arg3` | `+ 0x0 + rax*2` | `64` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007926F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
