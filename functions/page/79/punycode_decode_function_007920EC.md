# punycode_decode

- RVA: `0x007920EC`–`0x007926EC` (길이 `1,536` bytes)
- VA: `0x00000001407920EC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CFDA0`
- 디코드: `408`개 명령, `1,536/1,536` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00792190` → [FindLabelEnd](../../text/5E/FindLabelEnd_function_005ECAA4.md) (function, `0x005ECAA4`)
- `0x00792209` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (function, `0x005001C0`)
- `0x00792291` → [ValidateStd3Range](../../text/5E/ValidateStd3Range_function_005ED154.md) (function, `0x005ED154`)
- `0x00792413` → [adapt](../../text/5E/adapt_function_005ED190.md) (function, `0x005ED190`)
- `0x00792519` → [InsertChar](../../text/5E/InsertChar_function_005ECB14.md) (function, `0x005ECB14`)
- `0x00792541` → [InsertChar](../../text/5E/InsertChar_function_005ECB14.md) (function, `0x005ECB14`)
- `0x00792593` → [ValidateStd3Range](../../text/5E/ValidateStd3Range_function_005ED154.md) (function, `0x005ED154`)

### Direct callers
- [RtlpIdnToUnicodeWorker](../../text/5E/RtlpIdnToUnicodeWorker_function_005ECB3C.md) at `0x005ECC30`

### Static image references
- `0x007921EB` → RVA `0x00031520` (`.rdata`; read)
- `0x007921F5` → RVA `0x00031510` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x00792190` → [FindLabelEnd](../../text/5E/FindLabelEnd_function_005ECAA4.md) (`PAGE` → `.text`)
  - `0x00792209` → [wcsnicmp](../../text/50/wcsnicmp_function_005001C0.md) (`PAGE` → `.text`)
  - `0x00792291` → [ValidateStd3Range](../../text/5E/ValidateStd3Range_function_005ED154.md) (`PAGE` → `.text`)
  - `0x00792413` → [adapt](../../text/5E/adapt_function_005ED190.md) (`PAGE` → `.text`)
  - `0x00792519` → [InsertChar](../../text/5E/InsertChar_function_005ECB14.md) (`PAGE` → `.text`)
  - `0x00792541` → [InsertChar](../../text/5E/InsertChar_function_005ECB14.md) (`PAGE` → `.text`)
  - `0x00792593` → [ValidateStd3Range](../../text/5E/ValidateStd3Range_function_005ED154.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007920EC  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
007920F1  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
007920F6  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
007920FB  53                              push rbx
007920FC  55                              push rbp
007920FD  56                              push rsi
007920FE  57                              push rdi
007920FF  41 54                           push r12
00792101  41 55                           push r13
00792103  41 56                           push r14
00792105  41 57                           push r15
00792107  48 83 EC 58                     sub rsp, 0x58
0079210B  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00792113  45 33 DB                        xor r11d, r11d
00792116  49 8B D8                        mov rbx, r8
00792119  4D 63 01                        movsxd r8, dword ptr [r9]
0079211C  45 89 19                        mov dword ptr [r9], r11d
0079211F  4C 8B D1                        mov r10, rcx
00792122  C6 00 01                        mov byte ptr [rax], 1
00792125  85 D2                           test edx, edx
00792127  0F 8E 3D 05 00 00               jle 0x14079266a
0079212D  44 8A A4 24 C8 00 00 00         mov r12b, byte ptr [rsp + 0xc8]
00792135  4A 8D 2C 43                     lea rbp, [rbx + r8*2]
00792139  44 8A AC 24 C0 00 00 00         mov r13b, byte ptr [rsp + 0xc0]
00792141  48 8B F9                        mov rdi, rcx
00792144  48 63 C2                        movsxd rax, edx
00792147  4C 8B F1                        mov r14, rcx
0079214A  48 8D 51 FE                     lea rdx, [rcx - 2]
0079214E  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00792153  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00792158  4C 8B FB                        mov r15, rbx
0079215B  48 89 6C 24 30                  mov qword ptr [rsp + 0x30], rbp
00792160  41 B9 80 00 00 00               mov r9d, 0x80
00792166  48 8D 34 41                     lea rsi, [rcx + rax*2]
0079216A  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
00792172  48 8D 43 FE                     lea rax, [rbx - 2]
00792176  48 89 01                        mov qword ptr [rcx], rax
00792179  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
0079217E  48 3B FE                        cmp rdi, rsi
00792181  0F 83 22 05 00 00               jae 0x1407926a9
00792187  45 8A C5                        mov r8b, r13b
0079218A  48 8B D6                        mov rdx, rsi
0079218D  49 8B CE                        mov rcx, r14
00792190  E8 0F A9 E5 FF                  call 0x1405ecaa4
00792195  48 8B F8                        mov rdi, rax
00792198  49 3B C6                        cmp rax, r14
0079219B  0F 84 F9 04 00 00               je 0x14079269a
007921A1  45 84 ED                        test r13b, r13b
007921A4  75 31                           jne 0x1407921d7
007921A6  45 84 E4                        test r12b, r12b
007921A9  74 1B                           je 0x1407921c6
007921AB  66 41 83 3E 2D                  cmp word ptr [r14], 0x2d
007921B0  0F 84 B4 04 00 00               je 0x14079266a
007921B6  49 3B C2                        cmp rax, r10
007921B9  76 0B                           jbe 0x1407921c6
007921BB  66 83 78 FE 2D                  cmp word ptr [rax - 2], 0x2d
007921C0  0F 84 A4 04 00 00               je 0x14079266a
007921C6  49 2B C6                        sub rax, r14
007921C9  48 83 E0 FE                     and rax, 0xfffffffffffffffe
007921CD  48 83 F8 7E                     cmp rax, 0x7e
007921D1  0F 8F 93 04 00 00               jg 0x14079266a
007921D7  48 8B C6                        mov rax, rsi
007921DA  49 2B C6                        sub rax, r14
007921DD  48 83 E0 FE                     and rax, 0xfffffffffffffffe
007921E1  48 83 F8 08                     cmp rax, 8
007921E5  0F 8C 75 03 00 00               jl 0x140792560
007921EB  48 8D 05 2E F3 89 FF            lea rax, [rip - 0x760cd2]
007921F2  45 84 ED                        test r13b, r13b
007921F5  48 8D 15 14 F3 89 FF            lea rdx, [rip - 0x760cec]
007921FC  41 B8 04 00 00 00               mov r8d, 4
00792202  48 0F 44 D0                     cmove rdx, rax
00792206  49 8B CE                        mov rcx, r14
00792209  E8 B2 DF D6 FF                  call 0x1405001c0
0079220E  45 33 DB                        xor r11d, r11d
00792211  85 C0                           test eax, eax
00792213  0F 85 41 03 00 00               jne 0x14079255a
00792219  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00792221  49 83 C6 08                     add r14, 8
00792225  44 88 18                        mov byte ptr [rax], r11b
00792228  48 8D 47 FE                     lea rax, [rdi - 2]
0079222C  4C 8B C0                        mov r8, rax
0079222F  4D 3B C6                        cmp r8, r14
00792232  72 0D                           jb 0x140792241
00792234  66 41 83 38 2D                  cmp word ptr [r8], 0x2d
00792239  74 09                           je 0x140792244
0079223B  49 83 E8 02                     sub r8, 2
0079223F  EB EE                           jmp 0x14079222f
00792241  4D 8B C3                        mov r8, r11
00792244  4C 3B C0                        cmp r8, rax
00792247  0F 84 1D 04 00 00               je 0x14079266a
0079224D  4D 85 C0                        test r8, r8
00792250  0F 84 A6 00 00 00               je 0x1407922fc
00792256  4D 3B C6                        cmp r8, r14
00792259  0F 86 9D 00 00 00               jbe 0x1407922fc
0079225F  4D 8B D0                        mov r10, r8
00792262  4D 8B CE                        mov r9, r14
00792265  4D 2B D6                        sub r10, r14
00792268  41 BF 80 00 00 00               mov r15d, 0x80
0079226E  49 D1 FA                        sar r10, 1
00792271  4D 3B C8                        cmp r9, r8
00792274  0F 84 8B 00 00 00               je 0x140792305
0079227A  48 3B DD                        cmp rbx, rbp
0079227D  0F 83 E7 03 00 00               jae 0x14079266a
00792283  45 84 ED                        test r13b, r13b
00792286  75 33                           jne 0x1407922bb
00792288  45 84 E4                        test r12b, r12b
0079228B  74 11                           je 0x14079229e
0079228D  41 0F B7 09                     movzx ecx, word ptr [r9]
00792291  E8 BE AE E5 FF                  call 0x1405ed154
00792296  84 C0                           test al, al
00792298  0F 84 CC 03 00 00               je 0x14079266a
0079229E  41 0F B7 01                     movzx eax, word ptr [r9]
007922A2  66 83 F8 20                     cmp ax, 0x20
007922A6  0F 82 BE 03 00 00               jb 0x14079266a
007922AC  66 83 F8 7F                     cmp ax, 0x7f
007922B0  0F 84 B4 03 00 00               je 0x14079266a
007922B6  0F B7 C8                        movzx ecx, ax
007922B9  EB 0D                           jmp 0x1407922c8
007922BB  41 0F B7 09                     movzx ecx, word ptr [r9]
007922BF  66 85 C9                        test cx, cx
007922C2  0F 84 A2 03 00 00               je 0x14079266a
007922C8  66 41 3B CF                     cmp cx, r15w
007922CC  0F 83 98 03 00 00               jae 0x14079266a
007922D2  45 84 ED                        test r13b, r13b
007922D5  75 0D                           jne 0x1407922e4
007922D7  8D 41 BF                        lea eax, [rcx - 0x41]
007922DA  66 83 F8 19                     cmp ax, 0x19
007922DE  77 04                           ja 0x1407922e4
007922E0  66 83 C1 20                     add cx, 0x20
007922E4  66 89 0B                        mov word ptr [rbx], cx
007922E7  48 83 C3 02                     add rbx, 2
007922EB  48 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rbx
007922F3  49 83 C1 02                     add r9, 2
007922F7  E9 75 FF FF FF                  jmp 0x140792271
007922FC  45 8B D3                        mov r10d, r11d
007922FF  41 BF 80 00 00 00               mov r15d, 0x80
00792305  45 85 D2                        test r10d, r10d
00792308  41 8D 42 01                     lea eax, [r10 + 1]
0079230C  41 0F 4E C3                     cmovle eax, r11d
00792310  33 ED                           xor ebp, ebp
00792312  21 AC 24 A8 00 00 00            and dword ptr [rsp + 0xa8], ebp
00792319  48 98                           cdqe
0079231B  44 8D 5D 48                     lea r11d, [rbp + 0x48]
0079231F  4D 8D 24 46                     lea r12, [r14 + rax*2]
00792323  4C 3B E7                        cmp r12, rdi
00792326  0F 83 B4 02 00 00               jae 0x1407925e0
0079232C  41 B9 01 00 00 00               mov r9d, 1
00792332  44 8B D5                        mov r10d, ebp
00792335  45 8D 41 23                     lea r8d, [r9 + 0x23]
00792339  4C 3B E7                        cmp r12, rdi
0079233C  0F 83 28 03 00 00               jae 0x14079266a
00792342  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
00792347  8D 41 D0                        lea eax, [rcx - 0x30]
0079234A  66 83 F8 09                     cmp ax, 9
0079234E  77 05                           ja 0x140792355
00792350  83 E9 16                        sub ecx, 0x16
00792353  EB 28                           jmp 0x14079237d
00792355  0F B7 C1                        movzx eax, cx
00792358  BA 61 00 00 00                  mov edx, 0x61
0079235D  66 2B C2                        sub ax, dx
00792360  66 83 F8 19                     cmp ax, 0x19
00792364  76 15                           jbe 0x14079237b
00792366  0F B7 C1                        movzx eax, cx
00792369  BA 41 00 00 00                  mov edx, 0x41
0079236E  66 2B C2                        sub ax, dx
00792371  66 83 F8 19                     cmp ax, 0x19
00792375  0F 87 EF 02 00 00               ja 0x14079266a
0079237B  2B CA                           sub ecx, edx
0079237D  49 83 C4 02                     add r12, 2
00792381  85 C9                           test ecx, ecx
00792383  0F 88 E1 02 00 00               js 0x14079266a
00792389  B8 FF FF FF 07                  mov eax, 0x7ffffff
0079238E  2B C5                           sub eax, ebp
00792390  99                              cdq
00792391  41 F7 F9                        idiv r9d
00792394  3B C8                           cmp ecx, eax
00792396  0F 8F CE 02 00 00               jg 0x14079266a
0079239C  8B C1                           mov eax, ecx
0079239E  41 0F AF C1                     imul eax, r9d
007923A2  03 E8                           add ebp, eax
007923A4  45 3B C3                        cmp r8d, r11d
007923A7  7F 07                           jg 0x1407923b0
007923A9  B8 01 00 00 00                  mov eax, 1
007923AE  EB 16                           jmp 0x1407923c6
007923B0  41 8D 43 1A                     lea eax, [r11 + 0x1a]
007923B4  44 3B C0                        cmp r8d, eax
007923B7  7C 07                           jl 0x1407923c0
007923B9  B8 1A 00 00 00                  mov eax, 0x1a
007923BE  EB 06                           jmp 0x1407923c6
007923C0  41 8B C0                        mov eax, r8d
007923C3  41 2B C3                        sub eax, r11d
007923C6  3B C8                           cmp ecx, eax
007923C8  7C 25                           jl 0x1407923ef
007923CA  B9 24 00 00 00                  mov ecx, 0x24
007923CF  2B C8                           sub ecx, eax
007923D1  B8 FF FF FF 07                  mov eax, 0x7ffffff
007923D6  99                              cdq
007923D7  F7 F9                           idiv ecx
007923D9  44 3B C8                        cmp r9d, eax
007923DC  0F 8F 88 02 00 00               jg 0x14079266a
007923E2  44 0F AF C9                     imul r9d, ecx
007923E6  41 83 C0 24                     add r8d, 0x24
007923EA  E9 4A FF FF FF                  jmp 0x140792339
007923EF  8B CD                           mov ecx, ebp
007923F1  4C 8B DB                        mov r11, rbx
007923F4  4C 2B 5C 24 28                  sub r11, qword ptr [rsp + 0x28]
007923F9  49 D1 FB                        sar r11, 1
007923FC  41 83 FA 00                     cmp r10d, 0
00792400  41 8B D3                        mov edx, r11d
00792403  41 0F 94 C0                     sete r8b
00792407  2B 94 24 A8 00 00 00            sub edx, dword ptr [rsp + 0xa8]
0079240E  FF C2                           inc edx
00792410  41 2B CA                        sub ecx, r10d
00792413  E8 78 AD E5 FF                  call 0x1405ed190
00792418  4C 63 84 24 A8 00 00 00         movsxd r8, dword ptr [rsp + 0xa8]
00792420  B9 FF FF FF 07                  mov ecx, 0x7ffffff
00792425  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00792429  4D 2B D8                        sub r11, r8
0079242C  48 63 C5                        movsxd rax, ebp
0079242F  49 FF C3                        inc r11
00792432  48 99                           cqo
00792434  41 2B CF                        sub ecx, r15d
00792437  49 F7 FB                        idiv r11
0079243A  48 63 C9                        movsxd rcx, ecx
0079243D  48 8B EA                        mov rbp, rdx
00792440  48 3B C1                        cmp rax, rcx
00792443  0F 8F 21 02 00 00               jg 0x14079266a
00792449  44 03 F8                        add r15d, eax
0079244C  41 8D 47 80                     lea eax, [r15 - 0x80]
00792450  3D 7F FF 10 00                  cmp eax, 0x10ff7f
00792455  0F 87 0F 02 00 00               ja 0x14079266a
0079245B  41 8D 87 00 28 FF FF            lea eax, [r15 - 0xd800]
00792462  BA FF 07 00 00                  mov edx, 0x7ff
00792467  3B C2                           cmp eax, edx
00792469  0F 86 FB 01 00 00               jbe 0x14079266a
0079246F  45 85 C0                        test r8d, r8d
00792472  7E 33                           jle 0x1407924a7
00792474  4C 8B 54 24 28                  mov r10, qword ptr [rsp + 0x28]
00792479  8B CD                           mov ecx, ebp
0079247B  41 B8 00 28 00 00               mov r8d, 0x2800
00792481  85 C9                           test ecx, ecx
00792483  7E 2E                           jle 0x1407924b3
00792485  4C 3B D3                        cmp r10, rbx
00792488  0F 83 DC 01 00 00               jae 0x14079266a
0079248E  41 0F B7 02                     movzx eax, word ptr [r10]
00792492  66 41 03 C0                     add ax, r8w
00792496  66 3B C2                        cmp ax, dx
00792499  77 04                           ja 0x14079249f
0079249B  49 83 C2 02                     add r10, 2
0079249F  FF C9                           dec ecx
007924A1  49 83 C2 02                     add r10, 2
007924A5  EB DA                           jmp 0x140792481
007924A7  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
007924AC  48 63 C5                        movsxd rax, ebp
007924AF  4C 8D 14 41                     lea r10, [rcx + rax*2]
007924B3  41 81 FF 00 00 01 00            cmp r15d, 0x10000
007924BA  7D 1A                           jge 0x1407924d6
007924BC  48 3B 5C 24 30                  cmp rbx, qword ptr [rsp + 0x30]
007924C1  0F 83 A3 01 00 00               jae 0x14079266a
007924C7  4C 3B D3                        cmp r10, rbx
007924CA  0F 87 9A 01 00 00               ja 0x14079266a
007924D0  45 0F B7 DF                     movzx r11d, r15w
007924D4  EB 5C                           jmp 0x140792532
007924D6  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
007924DB  48 83 C0 FE                     add rax, -2
007924DF  48 3B D8                        cmp rbx, rax
007924E2  0F 83 82 01 00 00               jae 0x14079266a
007924E8  4C 3B D3                        cmp r10, rbx
007924EB  0F 87 79 01 00 00               ja 0x14079266a
007924F1  41 8D 87 00 00 FF FF            lea eax, [r15 - 0x10000]
007924F8  B9 00 04 00 00                  mov ecx, 0x400
007924FD  99                              cdq
007924FE  4C 8D 84 24 B0 00 00 00         lea r8, [rsp + 0xb0]
00792506  F7 F9                           idiv ecx
00792508  B9 00 28 00 00                  mov ecx, 0x2800
0079250D  66 2B C1                        sub ax, cx
00792510  44 8B DA                        mov r11d, edx
00792513  0F B7 C8                        movzx ecx, ax
00792516  49 8B D2                        mov rdx, r10
00792519  E8 F6 A5 E5 FF                  call 0x1405ecb14
0079251E  FF 84 24 A8 00 00 00            inc dword ptr [rsp + 0xa8]
00792525  B8 00 24 00 00                  mov eax, 0x2400
0079252A  66 44 2B D8                     sub r11w, ax
0079252E  49 83 C2 02                     add r10, 2
00792532  4C 8D 84 24 B0 00 00 00         lea r8, [rsp + 0xb0]
0079253A  49 8B D2                        mov rdx, r10
0079253D  41 0F B7 CB                     movzx ecx, r11w
00792541  E8 CE A5 E5 FF                  call 0x1405ecb14
00792546  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
0079254E  FF C5                           inc ebp
00792550  44 8B 5C 24 20                  mov r11d, dword ptr [rsp + 0x20]
00792555  E9 C9 FD FF FF                  jmp 0x140792323
0079255A  41 B9 80 00 00 00               mov r9d, 0x80
00792560  48 8B CF                        mov rcx, rdi
00792563  48 8B C5                        mov rax, rbp
00792566  49 2B CE                        sub rcx, r14
00792569  48 2B C3                        sub rax, rbx
0079256C  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
00792570  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00792574  48 3B C1                        cmp rax, rcx
00792577  0F 8C ED 00 00 00               jl 0x14079266a
0079257D  4D 8B C6                        mov r8, r14
00792580  4C 3B C7                        cmp r8, rdi
00792583  73 76                           jae 0x1407925fb
00792585  45 84 ED                        test r13b, r13b
00792588  75 2A                           jne 0x1407925b4
0079258A  45 84 E4                        test r12b, r12b
0079258D  74 11                           je 0x1407925a0
0079258F  41 0F B7 08                     movzx ecx, word ptr [r8]
00792593  E8 BC AB E5 FF                  call 0x1405ed154
00792598  84 C0                           test al, al
0079259A  0F 84 CA 00 00 00               je 0x14079266a
007925A0  41 0F B7 00                     movzx eax, word ptr [r8]
007925A4  66 83 F8 20                     cmp ax, 0x20
007925A8  0F 82 BC 00 00 00               jb 0x14079266a
007925AE  66 83 F8 7F                     cmp ax, 0x7f
007925B2  EB 07                           jmp 0x1407925bb
007925B4  41 0F B7 00                     movzx eax, word ptr [r8]
007925B8  66 85 C0                        test ax, ax
007925BB  0F 84 A9 00 00 00               je 0x14079266a
007925C1  66 41 3B C1                     cmp ax, r9w
007925C5  0F 83 9F 00 00 00               jae 0x14079266a
007925CB  49 83 C0 02                     add r8, 2
007925CF  66 89 03                        mov word ptr [rbx], ax
007925D2  48 83 C3 02                     add rbx, 2
007925D6  48 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rbx
007925DE  EB A0                           jmp 0x140792580
007925E0  4C 8B 7C 24 28                  mov r15, qword ptr [rsp + 0x28]
007925E5  45 33 DB                        xor r11d, r11d
007925E8  48 8B 6C 24 30                  mov rbp, qword ptr [rsp + 0x30]
007925ED  41 B9 80 00 00 00               mov r9d, 0x80
007925F3  44 8A A4 24 C8 00 00 00         mov r12b, byte ptr [rsp + 0xc8]
007925FB  45 84 ED                        test r13b, r13b
007925FE  75 15                           jne 0x140792615
00792600  48 8B C7                        mov rax, rdi
00792603  49 2B C6                        sub rax, r14
00792606  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0079260A  48 83 F8 7E                     cmp rax, 0x7e
0079260E  7F 5A                           jg 0x14079266a
00792610  49 3B DF                        cmp rbx, r15
00792613  74 55                           je 0x14079266a
00792615  48 3B FE                        cmp rdi, rsi
00792618  74 17                           je 0x140792631
0079261A  48 3B DD                        cmp rbx, rbp
0079261D  73 4B                           jae 0x14079266a
0079261F  0F B7 07                        movzx eax, word ptr [rdi]
00792622  66 89 03                        mov word ptr [rbx], ax
00792625  48 83 C3 02                     add rbx, 2
00792629  48 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rbx
00792631  45 84 ED                        test r13b, r13b
00792634  74 4B                           je 0x140792681
00792636  48 8B C7                        mov rax, rdi
00792639  48 8B D7                        mov rdx, rdi
0079263C  48 2B C6                        sub rax, rsi
0079263F  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00792644  48 F7 D8                        neg rax
00792647  45 8A EB                        mov r13b, r11b
0079264A  48 8B C3                        mov rax, rbx
0079264D  48 1B C9                        sbb rcx, rcx
00792650  83 E1 02                        and ecx, 2
00792653  48 2B C1                        sub rax, rcx
00792656  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
0079265E  48 89 01                        mov qword ptr [rcx], rax
00792661  48 8D 46 FE                     lea rax, [rsi - 2]
00792665  48 3B F8                        cmp rdi, rax
00792668  75 1C                           jne 0x140792686
0079266A  B8 16 07 00 C0                  mov eax, 0xc0000716
0079266F  48 83 C4 58                     add rsp, 0x58
00792673  41 5F                           pop r15
00792675  41 5E                           pop r14
00792677  41 5D                           pop r13
00792679  41 5C                           pop r12
0079267B  5F                              pop rdi
0079267C  5E                              pop rsi
0079267D  5D                              pop rbp
0079267E  5B                              pop rbx
0079267F  C3                              ret
00792680  CC                              int3
00792681  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
00792686  4C 8B 94 24 A0 00 00 00         mov r10, qword ptr [rsp + 0xa0]
0079268E  4C 8D 77 02                     lea r14, [rdi + 2]
00792692  4C 8B FB                        mov r15, rbx
00792695  E9 DF FA FF FF                  jmp 0x140792179
0079269A  45 84 ED                        test r13b, r13b
0079269D  75 CB                           jne 0x14079266a
0079269F  48 3B FE                        cmp rdi, rsi
007926A2  75 C6                           jne 0x14079266a
007926A4  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
007926A9  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
007926AE  49 3B D9                        cmp rbx, r9
007926B1  74 B7                           je 0x14079266a
007926B3  45 84 ED                        test r13b, r13b
007926B6  75 20                           jne 0x1407926d8
007926B8  0F B7 46 FE                     movzx eax, word ptr [rsi - 2]
007926BC  66 83 E8 2E                     sub ax, 0x2e
007926C0  66 F7 D8                        neg ax
007926C3  48 1B C9                        sbb rcx, rcx
007926C6  48 2B F2                        sub rsi, rdx
007926C9  48 D1 FE                        sar rsi, 1
007926CC  48 81 C1 00 01 00 00            add rcx, 0x100
007926D3  48 3B F1                        cmp rsi, rcx
007926D6  7F 92                           jg 0x14079266a
007926D8  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
007926E0  49 2B D9                        sub rbx, r9
007926E3  48 D1 FB                        sar rbx, 1
007926E6  89 18                           mov dword ptr [rax], ebx
007926E8  33 C0                           xor eax, eax
007926EA  EB 83                           jmp 0x14079266f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall punycode_decode(__int64 a1, int a2, __int64 a3, __int64 a4, unsigned __int8 a5, unsigned __int8 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pB8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (88);
    v_r11 = 0;
    *(unsigned int *)(a4) = 0;
    *(unsigned __int8 *)(a7) = 1;
    if (condition_is_less_or_equal) goto loc_0079266A;
    v_stack_m58 = a3;
    v_stack_m60 = a1 - 2;
    v_stack_m68 = a3 + (int)(*(unsigned int *)(a4)) * 2;
    *(unsigned __int64 *)(a8) = a3 - 2;
loc_00792179:
    v_stack_m70 = a3;
    if (a1 >= (a1 + (int)(a2) * 2)) goto loc_007926A9;
    result = FindLabelEnd(a1, a1 + (int)(a2) * 2, a5, 128);
    if (result == a1) goto loc_0079269A;
    if (a5 != 0) goto loc_007921D7;
    if (a6 == 0) goto loc_007921C6;
    if ((*(unsigned __int16 *)(a1)) == 45) goto loc_0079266A;
    if (result <= a1) goto loc_007921C6;
    if ((*(unsigned __int16 *)(result - 2)) == 45) goto loc_0079266A;
loc_007921C6:
    result = (result) - (a1);
    result = (result) & (-2);
    if (result > 126) goto loc_0079266A;
loc_007921D7:
    result = (a1 + (int)(a2) * 2) - (a1);
    result = (result) & (-2);
    if (result < 8) goto loc_00792560;
    a2 = v_rip - 7736556;
    if (a5 == 0) { a2 = v_rip - 7736530; }
    result = wcsnicmp(a1, a2, 4, 128);
    v_r11 = 0;
    if ((unsigned int)(result) != 0) goto loc_0079255A;
    v_r14 = (a1) + (8);
    *(unsigned __int8 *)(a7) = 0;
loc_0079222F:
    if ((result - 2) < v_r14) goto loc_00792241;
    if ((*(unsigned __int16 *)(result - 2)) == 45) goto loc_00792244;
    a3 = (result - 2) - (2);
    goto loc_0079222F;
loc_00792241:
loc_00792244:
    if (0 == (result - 2)) goto loc_0079266A;
    if (0 == 0) goto loc_007922FC;
    if (0 <= v_r14) goto loc_007922FC;
    v_r10 = (0) - (v_r14);
    v_r10 = (v_r10) >> (1);
loc_00792271:
    if (v_r14 == 0) goto loc_00792305;
    if (a3 >= (a3 + (int)(*(unsigned int *)(a4)) * 2)) goto loc_0079266A;
    if (a5 != 0) goto loc_007922BB;
    if (a6 == 0) goto loc_0079229E;
    result = ValidateStd3Range(*(unsigned __int16 *)(v_r14), a2, 0, v_r14);
    if ((unsigned __int8)(result) == 0) goto loc_0079266A;
loc_0079229E:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r14))) < 32) goto loc_0079266A;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r14))) == 127) goto loc_0079266A;
    goto loc_007922C8;
loc_007922BB:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_r14)) == 0) goto loc_0079266A;
loc_007922C8:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r14))) >= 128) goto loc_0079266A;
    if (a5 != 0) goto loc_007922E4;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r14) - 65)) <= 25) {
        a1 = (unsigned __int16)((*(unsigned __int16 *)(v_r14)) + (32));
    }
    *(unsigned __int16 *)(a3) = (unsigned __int16)(a1);
    v_rbx = (a3) + (2);
    v_stack_p18 = v_rbx;
    a4 = (v_r14) + (2);
    goto loc_00792271;
loc_007922FC:
loc_00792305:
    result = 0 + 1;
    if (condition_is_less_or_equal) { result = 0; }
    v_rbp = 0;
loc_00792323:
    if ((v_r14 + result * 2) >= result) goto loc_007925E0;
loc_00792339:
    if ((v_r14 + result * 2) >= result) goto loc_0079266A;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r14 + result * 2) - 48)) > 9) goto loc_00792355;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_r14 + result * 2)) - (22));
    goto loc_0079237D;
loc_00792355:
    result = (unsigned __int16)(((unsigned __int16)(a1)) - (97));
    if (((unsigned __int16)(result)) <= 25) goto loc_0079237B;
    result = (unsigned __int16)(((unsigned __int16)(a1)) - (65));
    if (((unsigned __int16)(result)) > 25) goto loc_0079266A;
loc_0079237B:
    a1 = (unsigned int)((a1) - (65));
loc_0079237D:
    v_r12 = (v_r14 + result * 2) + (2);
    if (sign_flag) goto loc_0079266A;
    result = (unsigned int)(((unsigned int)(0x7FFFFFFULL)) - (0));
    if (((unsigned int)(a1)) > ((unsigned int)(result))) goto loc_0079266A;
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) * (1));
    v_rbp = (unsigned int)((v_rbp) + ((unsigned int)(result)));
    if (((unsigned int)(1 + 35)) > ((unsigned int)(v_rbp + 72))) goto loc_007923B0;
    goto loc_007923C6;
loc_007923B0:
    if (((unsigned int)(1 + 35)) < ((unsigned int)(v_rbp + 72 + 26))) goto loc_007923C0;
    goto loc_007923C6;
loc_007923C0:
    result = (unsigned int)(((unsigned int)((unsigned int)(1 + 35))) - ((unsigned int)(v_rbp + 72)));
loc_007923C6:
    if (((unsigned int)(a1)) < ((unsigned int)(result))) goto loc_007923EF;
    a1 = (unsigned int)((36) - ((unsigned int)(result)));
    if (1 > ((unsigned int)((unsigned int)(0x7FFFFFFULL)))) goto loc_0079266A;
    a4 = (unsigned int)((1) * ((unsigned int)(a1)));
    a3 = (unsigned int)((1 + 35) + (36));
    goto loc_00792339;
loc_007923EF:
    v_r11 = (v_rbx) - (v_stack_m70);
    v_r11 = (v_r11) >> (1);
    a3 = (0 == 0) ? 1 : 0;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r11))) - (v_stack_p10));
    a2 = (unsigned int)((a2) + 1);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbp))) - (0));
    result = adapt(a1, a2, a3, a4);
    v_stack_m78 = (unsigned int)(result);
    v_r11 = (v_r11) - ((int)(v_stack_p10));
    v_r11 = (v_r11) + 1;
    a1 = (unsigned int)(((unsigned int)(0x7FFFFFFULL)) - (128));
    if (((int)((unsigned int)(v_rbp))) > ((int)((unsigned int)(a1)))) goto loc_0079266A;
    v_r15 = (unsigned int)((128) + ((unsigned int)((int)((unsigned int)(v_rbp)))));
    if (((unsigned int)(v_r15 - 128)) > 0x10FF7FULL) goto loc_0079266A;
    if (((unsigned int)(v_r15 - 55296)) <= ((unsigned int)((unsigned int)(0x7FFULL)))) goto loc_0079266A;
    if (condition_is_less_or_equal) goto loc_007924A7;
loc_00792481:
    if (condition_is_less_or_equal) goto loc_007924B3;
    if (v_stack_m70 >= v_rbx) goto loc_0079266A;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m70)) + ((unsigned __int16)((unsigned int)(0x2800ULL))));
    v_r10 = v_stack_m70;
    if (((unsigned __int16)(result)) <= ((unsigned __int16)((unsigned int)(0x7FFULL)))) {
        v_r10 = (v_stack_m70) + (2);
    }
    a1 = (unsigned int)(((unsigned int)(a2)) - 1);
    v_r10 = (v_r10) + (2);
    goto loc_00792481;
loc_007924A7:
loc_007924B3:
    if (((unsigned int)(v_r15)) >= 0x10000ULL) goto loc_007924D6;
    if (v_rbx >= v_stack_m68) goto loc_0079266A;
    if ((v_stack_m70 + (int)(a2) * 2) > v_rbx) goto loc_0079266A;
    goto loc_00792532;
loc_007924D6:
    result = (v_stack_m68) + (-2);
    if (v_rbx >= result) goto loc_0079266A;
    if ((v_stack_m70 + (int)(a2) * 2) > v_rbx) goto loc_0079266A;
    result = (unsigned __int16)((v_r15 - 65536) - ((unsigned __int16)((unsigned int)(0x2800ULL))));
    result = InsertChar((unsigned __int16)(result), v_stack_m70 + (int)(a2) * 2, v_stack_p18, a4);
    v_r11 = (unsigned __int16)(((unsigned int)((unsigned int)((unsigned int)(0x7FFULL)))) - ((unsigned __int16)((unsigned int)(0x2400ULL))));
    v_r10 = (v_stack_m70 + (int)(a2) * 2) + (2);
loc_00792532:
    result = InsertChar((unsigned __int16)(v_r11), v_r10, v_stack_p18, a4);
    v_rbp = (unsigned int)((a2) + 1);
    goto loc_00792323;
loc_0079255A:
loc_00792560:
    a1 = (result) - (v_r14);
    result = (v_rbp) - (v_stack_p18);
    a1 = (a1) & (-2);
    result = (result) & (-2);
    if (result < a1) goto loc_0079266A;
loc_00792580:
    if (v_r14 >= result) goto loc_007925FB;
    if (a5 != 0) goto loc_007925B4;
    if ((unsigned __int8)(v_r12) == 0) goto loc_007925A0;
    result = ValidateStd3Range(*(unsigned __int16 *)(v_r14), v_r10, v_r14, 128);
    if ((unsigned __int8)(result) == 0) goto loc_0079266A;
loc_007925A0:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r14))) < 32) goto loc_0079266A;
    goto loc_007925BB;
loc_007925B4:
loc_007925BB:
    if ((unsigned __int16)(*(unsigned __int16 *)(v_r14)) == 0) goto loc_0079266A;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r14))) >= 128) goto loc_0079266A;
    a3 = (v_r14) + (2);
    *(unsigned __int16 *)(v_stack_p18) = (unsigned __int16)(*(unsigned __int16 *)(v_r14));
    v_rbx = (v_stack_p18) + (2);
    v_stack_p18 = v_rbx;
    goto loc_00792580;
loc_007925E0:
    v_r11 = 0;
loc_007925FB:
    if (a5 != 0) goto loc_00792615;
    result = (result) - (v_r14);
    result = (result) & (-2);
    if (result > 126) goto loc_0079266A;
    if (v_rbx == v_stack_m70) goto loc_0079266A;
loc_00792615:
    if (result == (a1 + (int)(a2) * 2)) goto loc_00792631;
    if (v_rbx >= v_stack_m68) goto loc_0079266A;
    *(unsigned __int16 *)(v_rbx) = (unsigned __int16)(*(unsigned __int16 *)(result));
    v_rbx = (v_rbx) + (2);
    v_stack_p18 = v_rbx;
loc_00792631:
    if (a5 == 0) goto loc_00792681;
    result = (result) - (a1 + (int)(a2) * 2);
    v_stack_m60 = result;
    result = -(result);
    a1 = (unsigned int)((*(unsigned __int16 *)(v_r14)) & (2));
    result = (v_rbx) - (a1);
    *(unsigned __int64 *)(a8) = result;
    if (result != (a1 + (int)(a2) * 2 - 2)) goto loc_00792686;
loc_0079266A:
loc_0079266F:
    v_rsp = (v_rsp) + (88);
    return (unsigned int)(0xC0000716ULL);
loc_00792681:
loc_00792686:
    goto loc_00792179;
loc_0079269A:
    if (0 != 0) goto loc_0079266A;
    if (result != (a1 + (int)(a2) * 2)) goto loc_0079266A;
loc_007926A9:
    if (v_rbx == v_stack_p40) goto loc_0079266A;
    if (0 != 0) goto loc_007926D8;
    result = (unsigned __int16)((*(unsigned __int16 *)(a1 + (int)(a2) * 2 - 2)) - (46));
    result = (unsigned __int16)(-(result));
    v_rsi = (a1 + (int)(a2) * 2) - (v_stack_p38);
    v_rsi = (v_rsi) >> (1);
    a1 = (a8) + (256);
    if (v_rsi > a1) goto loc_0079266A;
loc_007926D8:
    v_rbx = (v_rbx) - (v_stack_p40);
    v_rbx = (v_rbx) >> (1);
    *(unsigned int *)(v_stack_pB8) = (unsigned int)(v_rbx);
    result = 0;
    goto loc_0079266F;
}
```

## 5. (Beta) C Style

```c
int64_t punycode_decode(void *Arg1, int32_t Arg2, void *Arg3, void *Arg4, uint8_t Arg5, uint8_t Arg6, void *Arg7, void *Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p8;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pB8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (88);
    local_r11 = 0;
    *(uint32_t *)(arg4) = 0;
    *(uint8_t *)(arg7) = 1;
    if (condition_is_less_or_equal) goto loc_0079266A;
    v_stack_m58 = Arg3;
    v_stack_m60 = Arg1 - 2;
    v_stack_m68 = Arg3 + (int32_t)(*(uint32_t *)(arg4)) * 2;
    *(void **)(arg8) = Arg3 - 2;
loc_00792179:
    v_stack_m70 = Arg3;
    if (Arg1 >= (Arg1 + (int32_t)(Arg2) * 2)) goto loc_007926A9;
    result = FindLabelEnd(Arg1, Arg1 + (int32_t)(Arg2) * 2, Arg5, 128);
    if (result == Arg1) goto loc_0079269A;
    if (Arg5 != 0) goto loc_007921D7;
    if (Arg6 == 0) goto loc_007921C6;
    if ((*(uint16_t *)(arg1)) == 45) goto loc_0079266A;
    if (result <= Arg1) goto loc_007921C6;
    if ((*(uint16_t *)(result - 0x2)) == 45) goto loc_0079266A;
loc_007921C6:
    result = (result) - (Arg1);
    result = (result) & (-2);
    if (result > 126) goto loc_0079266A;
loc_007921D7:
    result = (Arg1 + (int32_t)(Arg2) * 2) - (Arg1);
    result = (result) & (-2);
    if (result < 8) goto loc_00792560;
    Arg2 = v_rip - 7736556;
    if (Arg5 == 0) { Arg2 = v_rip - 7736530; }
    result = wcsnicmp(Arg1, Arg2, 4, 128);
    local_r11 = 0;
    if ((uint32_t)(result) != 0) goto loc_0079255A;
    local_r14 = (Arg1) + (8);
    *(uint8_t *)(arg7) = 0;
loc_0079222F:
    if ((result - 2) < local_r14) goto loc_00792241;
    if ((*(uint16_t *)(result - 0x2)) == 45) goto loc_00792244;
    Arg3 = (result - 2) - (2);
    goto loc_0079222F;
loc_00792241:
loc_00792244:
    if (0 == (result - 2)) goto loc_0079266A;
    if (0 == 0) goto loc_007922FC;
    if (0 <= local_r14) goto loc_007922FC;
    local_r10 = (0) - (local_r14);
    local_r10 = (local_r10) >> (1);
loc_00792271:
    if (local_r14 == 0) goto loc_00792305;
    if (Arg3 >= (Arg3 + (int32_t)(*(uint32_t *)(arg4)) * 2)) goto loc_0079266A;
    if (Arg5 != 0) goto loc_007922BB;
    if (Arg6 == 0) goto loc_0079229E;
    result = ValidateStd3Range(*(uint16_t *)(local_r14), Arg2, 0, local_r14);
    if ((uint8_t)(result) == 0) goto loc_0079266A;
loc_0079229E:
    if (((uint16_t)(*(uint16_t *)(local_r14))) < 32) goto loc_0079266A;
    if (((uint16_t)(*(uint16_t *)(local_r14))) == 127) goto loc_0079266A;
    goto loc_007922C8;
loc_007922BB:
    if ((uint16_t)(*(uint16_t *)(local_r14)) == 0) goto loc_0079266A;
loc_007922C8:
    if (((uint16_t)(*(uint16_t *)(local_r14))) >= 128) goto loc_0079266A;
    if (Arg5 != 0) goto loc_007922E4;
    if (((uint16_t)(*(uint16_t *)(local_r14) - 65)) <= 25) {
        Arg1 = (uint16_t)((*(uint16_t *)(local_r14)) + (32));
    }
    *(uint16_t *)(arg3) = (uint16_t)(Arg1);
    local_rbx = (Arg3) + (2);
    v_stack_p18 = local_rbx;
    Arg4 = (local_r14) + (2);
    goto loc_00792271;
loc_007922FC:
loc_00792305:
    result = 0 + 1;
    if (condition_is_less_or_equal) { result = 0; }
    local_rbp = 0;
loc_00792323:
    if ((local_r14 + result * 2) >= result) goto loc_007925E0;
loc_00792339:
    if ((local_r14 + result * 2) >= result) goto loc_0079266A;
    if (((uint16_t)(*(uint16_t *)(local_r14 + result * 2) - 48)) > 9) goto loc_00792355;
    Arg1 = (uint32_t)((*(uint16_t *)(local_r14 + result * 2)) - (22));
    goto loc_0079237D;
loc_00792355:
    result = (uint16_t)(((uint16_t)(Arg1)) - (97));
    if (((uint16_t)(result)) <= 25) goto loc_0079237B;
    result = (uint16_t)(((uint16_t)(Arg1)) - (65));
    if (((uint16_t)(result)) > 25) goto loc_0079266A;
loc_0079237B:
    Arg1 = (uint32_t)((Arg1) - (65));
loc_0079237D:
    local_r12 = (local_r14 + result * 2) + (2);
    if (sign_flag) goto loc_0079266A;
    result = (uint32_t)(((uint32_t)(0x7FFFFFFULL)) - (0));
    if (((uint32_t)(Arg1)) > ((uint32_t)(result))) goto loc_0079266A;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) * (1));
    local_rbp = (uint32_t)((local_rbp) + ((uint32_t)(result)));
    if (((uint32_t)(1 + 35)) > ((uint32_t)(local_rbp + 72))) goto loc_007923B0;
    goto loc_007923C6;
loc_007923B0:
    if (((uint32_t)(1 + 35)) < ((uint32_t)(local_rbp + 72 + 26))) goto loc_007923C0;
    goto loc_007923C6;
loc_007923C0:
    result = (uint32_t)(((uint32_t)((uint32_t)(1 + 35))) - ((uint32_t)(local_rbp + 72)));
loc_007923C6:
    if (((uint32_t)(Arg1)) < ((uint32_t)(result))) goto loc_007923EF;
    Arg1 = (uint32_t)((36) - ((uint32_t)(result)));
    if (1 > ((uint32_t)((uint32_t)(0x7FFFFFFULL)))) goto loc_0079266A;
    Arg4 = (uint32_t)((1) * ((uint32_t)(Arg1)));
    Arg3 = (uint32_t)((1 + 35) + (36));
    goto loc_00792339;
loc_007923EF:
    local_r11 = (local_rbx) - (v_stack_m70);
    local_r11 = (local_r11) >> (1);
    Arg3 = (0 == 0) ? 1 : 0;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r11))) - (v_stack_p10));
    Arg2 = (uint32_t)((Arg2) + 1);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbp))) - (0));
    result = adapt(Arg1, Arg2, Arg3, Arg4);
    v_stack_m78 = (uint32_t)(result);
    local_r11 = (local_r11) - ((int32_t)(v_stack_p10));
    local_r11 = (local_r11) + 1;
    Arg1 = (uint32_t)(((uint32_t)(0x7FFFFFFULL)) - (128));
    if (((int32_t)((uint32_t)(local_rbp))) > ((int32_t)((uint32_t)(Arg1)))) goto loc_0079266A;
    local_r15 = (uint32_t)((128) + ((uint32_t)((int32_t)((uint32_t)(local_rbp)))));
    if (((uint32_t)(local_r15 - 128)) > 0x10FF7FULL) goto loc_0079266A;
    if (((uint32_t)(local_r15 - 55296)) <= ((uint32_t)((uint32_t)(0x7FFULL)))) goto loc_0079266A;
    if (condition_is_less_or_equal) goto loc_007924A7;
loc_00792481:
    if (condition_is_less_or_equal) goto loc_007924B3;
    if (v_stack_m70 >= local_rbx) goto loc_0079266A;
    result = (uint16_t)((*(uint16_t *)(v_stack_m70)) + ((uint16_t)((uint32_t)(0x2800ULL))));
    local_r10 = v_stack_m70;
    if (((uint16_t)(result)) <= ((uint16_t)((uint32_t)(0x7FFULL)))) {
        local_r10 = (v_stack_m70) + (2);
    }
    Arg1 = (uint32_t)(((uint32_t)(Arg2)) - 1);
    local_r10 = (local_r10) + (2);
    goto loc_00792481;
loc_007924A7:
loc_007924B3:
    if (((uint32_t)(local_r15)) >= 0x10000ULL) goto loc_007924D6;
    if (local_rbx >= v_stack_m68) goto loc_0079266A;
    if ((v_stack_m70 + (int32_t)(Arg2) * 2) > local_rbx) goto loc_0079266A;
    goto loc_00792532;
loc_007924D6:
    result = (v_stack_m68) + (-2);
    if (local_rbx >= result) goto loc_0079266A;
    if ((v_stack_m70 + (int32_t)(Arg2) * 2) > local_rbx) goto loc_0079266A;
    result = (uint16_t)((local_r15 - 65536) - ((uint16_t)((uint32_t)(0x2800ULL))));
    result = InsertChar((uint16_t)(result), v_stack_m70 + (int32_t)(Arg2) * 2, v_stack_p18, Arg4);
    local_r11 = (uint16_t)(((uint32_t)((uint32_t)((uint32_t)(0x7FFULL)))) - ((uint16_t)((uint32_t)(0x2400ULL))));
    local_r10 = (v_stack_m70 + (int32_t)(Arg2) * 2) + (2);
loc_00792532:
    result = InsertChar((uint16_t)(local_r11), local_r10, v_stack_p18, Arg4);
    local_rbp = (uint32_t)((Arg2) + 1);
    goto loc_00792323;
loc_0079255A:
loc_00792560:
    Arg1 = (result) - (local_r14);
    result = (local_rbp) - (v_stack_p18);
    Arg1 = (Arg1) & (-2);
    result = (result) & (-2);
    if (result < Arg1) goto loc_0079266A;
loc_00792580:
    if (local_r14 >= result) goto loc_007925FB;
    if (Arg5 != 0) goto loc_007925B4;
    if ((uint8_t)(local_r12) == 0) goto loc_007925A0;
    result = ValidateStd3Range(*(uint16_t *)(local_r14), local_r10, local_r14, 128);
    if ((uint8_t)(result) == 0) goto loc_0079266A;
loc_007925A0:
    if (((uint16_t)(*(uint16_t *)(local_r14))) < 32) goto loc_0079266A;
    goto loc_007925BB;
loc_007925B4:
loc_007925BB:
    if ((uint16_t)(*(uint16_t *)(local_r14)) == 0) goto loc_0079266A;
    if (((uint16_t)(*(uint16_t *)(local_r14))) >= 128) goto loc_0079266A;
    Arg3 = (local_r14) + (2);
    *(uint16_t *)(v_stack_p18) = (uint16_t)(*(uint16_t *)(local_r14));
    local_rbx = (v_stack_p18) + (2);
    v_stack_p18 = local_rbx;
    goto loc_00792580;
loc_007925E0:
    local_r11 = 0;
loc_007925FB:
    if (Arg5 != 0) goto loc_00792615;
    result = (result) - (local_r14);
    result = (result) & (-2);
    if (result > 126) goto loc_0079266A;
    if (local_rbx == v_stack_m70) goto loc_0079266A;
loc_00792615:
    if (result == (Arg1 + (int32_t)(Arg2) * 2)) goto loc_00792631;
    if (local_rbx >= v_stack_m68) goto loc_0079266A;
    *(uint16_t *)(local_rbx) = (uint16_t)(*(uint16_t *)(result));
    local_rbx = (local_rbx) + (2);
    v_stack_p18 = local_rbx;
loc_00792631:
    if (Arg5 == 0) goto loc_00792681;
    result = (result) - (Arg1 + (int32_t)(Arg2) * 2);
    v_stack_m60 = result;
    result = -(result);
    Arg1 = (uint32_t)((*(uint16_t *)(local_r14)) & (2));
    result = (local_rbx) - (Arg1);
    *(uint64_t *)(arg8) = result;
    if (result != (Arg1 + (int32_t)(Arg2) * 2 - 2)) goto loc_00792686;
loc_0079266A:
loc_0079266F:
    local_rsp = (local_rsp) + (88);
    return (uint32_t)(0xC0000716ULL);
loc_00792681:
loc_00792686:
    goto loc_00792179;
loc_0079269A:
    if (0 != 0) goto loc_0079266A;
    if (result != (Arg1 + (int32_t)(Arg2) * 2)) goto loc_0079266A;
loc_007926A9:
    if (local_rbx == v_stack_p40) goto loc_0079266A;
    if (0 != 0) goto loc_007926D8;
    result = (uint16_t)((*(uint16_t *)(arg1 + (int32_t)(Arg2) * 2 - 0x2)) - (46));
    result = (uint16_t)(-(result));
    local_rsi = (Arg1 + (int32_t)(Arg2) * 2) - (v_stack_p38);
    local_rsi = (local_rsi) >> (1);
    Arg1 = (Arg8) + (256);
    if (local_rsi > Arg1) goto loc_0079266A;
loc_007926D8:
    local_rbx = (local_rbx) - (v_stack_p40);
    local_rbx = (local_rbx) >> (1);
    *(uint32_t *)(v_stack_pB8) = (uint32_t)(local_rbx);
    result = 0;
    goto loc_0079266F;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x2` | `16` | `R` |
| `Arg1` | `- 0x2` | `64` | `R` |
| `Arg1` | `+ 0x0 + rax*2` | `64` | `R` |
| `Arg3` | `- 0x2` | `64` | `R` |
| `Arg3` | `+ 0x0 + r8*2` | `64` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `32` | `W` |
| `Arg7` | `+ 0x0` | `8` | `W` |
| `Arg8` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007920EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
