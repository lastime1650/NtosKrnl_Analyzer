# Xp10BuildAndWriteHuffmanTables

- RVA: `0x0079617C`–`0x00796BF7` (길이 `2,683` bytes)
- VA: `0x000000014079617C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BCE60`
- 디코드: `818`개 명령, `2,683/2,683` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x007961CC` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007961DA` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007962E1` → [Xp10BuildHuffmanEncodings](Xp10BuildHuffmanEncodings_function_00796EA4.md) (function, `0x00796EA4`)
- `0x00796BD6` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [Xp10BuildAndWriteHuffmanEncodings](Xp10BuildAndWriteHuffmanEncodings_function_00795DB0.md) at `0x00795F2F`

### Static image references
- `0x00796198` → RVA `0x00E0A740` (`.data`; read)
- `0x007962F2` → RVA `0x00034820` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x007961CC` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007961DA` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00796BD6` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0079617C  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00796181  55                              push rbp
00796182  56                              push rsi
00796183  57                              push rdi
00796184  41 54                           push r12
00796186  41 55                           push r13
00796188  41 56                           push r14
0079618A  41 57                           push r15
0079618C  48 8D 6C 24 90                  lea rbp, [rsp - 0x70]
00796191  48 81 EC 70 01 00 00            sub rsp, 0x170
00796198  48 8B 05 A1 45 67 00            mov rax, qword ptr [rip + 0x6745a1]
0079619F  48 33 C4                        xor rax, rsp
007961A2  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
007961A6  45 8B E8                        mov r13d, r8d
007961A9  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
007961AE  48 8B F2                        mov rsi, rdx
007961B1  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
007961B6  48 8B F9                        mov rdi, rcx
007961B9  41 BE 84 00 00 00               mov r14d, 0x84
007961BF  45 8B C6                        mov r8d, r14d
007961C2  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
007961C7  33 D2                           xor edx, edx
007961C9  49 8B D9                        mov rbx, r9
007961CC  E8 6F 0A F3 FF                  call 0x1406c6c40
007961D1  45 8B C6                        mov r8d, r14d
007961D4  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007961D8  33 D2                           xor edx, edx
007961DA  E8 61 0A F3 FF                  call 0x1406c6c40
007961DF  45 8D 5E 84                     lea r11d, [r14 - 0x7c]
007961E3  33 C0                           xor eax, eax
007961E5  45 8B CB                        mov r9d, r11d
007961E8  0F B7 D0                        movzx edx, ax
007961EB  66 41 BF 10 00                  mov r15w, 0x10
007961F0  45 8D 73 17                     lea r14d, [r11 + 0x17]
007961F4  45 8D 63 18                     lea r12d, [r11 + 0x18]
007961F8  45 8D 53 F9                     lea r10d, [r11 - 7]
007961FC  45 85 ED                        test r13d, r13d
007961FF  0F 84 BF 00 00 00               je 0x1407962c4
00796205  0F B7 C2                        movzx eax, dx
00796208  8B 0C 86                        mov ecx, dword ptr [rsi + rax*4]
0079620B  41 23 CE                        and ecx, r14d
0079620E  74 3F                           je 0x14079624f
00796210  44 8B C1                        mov r8d, ecx
00796213  41 3B C9                        cmp ecx, r9d
00796216  75 08                           jne 0x140796220
00796218  41 B8 1E 00 00 00               mov r8d, 0x1e
0079621E  EB 21                           jmp 0x140796241
00796220  66 41 3B D7                     cmp dx, r15w
00796224  72 18                           jb 0x14079623e
00796226  8B 44 86 C0                     mov eax, dword ptr [rsi + rax*4 - 0x40]
0079622A  41 23 C6                        and eax, r14d
0079622D  3B C8                           cmp ecx, eax
0079622F  75 05                           jne 0x140796236
00796231  45 8B C6                        mov r8d, r14d
00796234  EB 08                           jmp 0x14079623e
00796236  FF C0                           inc eax
00796238  3B C8                           cmp ecx, eax
0079623A  45 0F 44 C4                     cmove r8d, r12d
0079623E  44 8B C9                        mov r9d, ecx
00796241  41 8B C0                        mov eax, r8d
00796244  44 01 54 84 40                  add dword ptr [rsp + rax*4 + 0x40], r10d
00796249  66 41 03 D2                     add dx, r10w
0079624D  EB 69                           jmp 0x1407962b8
0079624F  44 0F B7 C2                     movzx r8d, dx
00796253  EB 0F                           jmp 0x140796264
00796255  0F B7 C2                        movzx eax, dx
00796258  8B 0C 86                        mov ecx, dword ptr [rsi + rax*4]
0079625B  41 84 CE                        test r14b, cl
0079625E  75 0C                           jne 0x14079626c
00796260  66 41 03 D2                     add dx, r10w
00796264  0F B7 C2                        movzx eax, dx
00796267  41 3B C5                        cmp eax, r13d
0079626A  72 E9                           jb 0x140796255
0079626C  0F B7 C2                        movzx eax, dx
0079626F  66 41 33 C0                     xor ax, r8w
00796273  66 41 3B C7                     cmp ax, r15w
00796277  72 25                           jb 0x14079629e
00796279  41 BC F0 FF 00 00               mov r12d, 0xfff0
0079627F  44 01 55 B0                     add dword ptr [rbp - 0x50], r10d
00796283  66 45 23 C4                     and r8w, r12w
00796287  66 45 03 C7                     add r8w, r15w
0079628B  0F B7 C2                        movzx eax, dx
0079628E  66 41 33 C0                     xor ax, r8w
00796292  66 41 3B C7                     cmp ax, r15w
00796296  73 E7                           jae 0x14079627f
00796298  41 BC 20 00 00 00               mov r12d, 0x20
0079629E  0F B7 CA                        movzx ecx, dx
007962A1  41 0F B7 C0                     movzx eax, r8w
007962A5  2B C8                           sub ecx, eax
007962A7  74 0F                           je 0x1407962b8
007962A9  83 F9 05                        cmp ecx, 5
007962AC  73 06                           jae 0x1407962b4
007962AE  01 4C 24 40                     add dword ptr [rsp + 0x40], ecx
007962B2  EB 04                           jmp 0x1407962b8
007962B4  44 01 55 B4                     add dword ptr [rbp - 0x4c], r10d
007962B8  0F B7 C2                        movzx eax, dx
007962BB  41 3B C5                        cmp eax, r13d
007962BE  0F 82 41 FF FF FF               jb 0x140796205
007962C4  48 8D 45 D0                     lea rax, [rbp - 0x30]
007962C8  41 BC 21 00 00 00               mov r12d, 0x21
007962CE  45 8B C4                        mov r8d, r12d
007962D1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007962D6  45 8B CB                        mov r9d, r11d
007962D9  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
007962DE  48 8B CF                        mov rcx, rdi
007962E1  E8 BE 0B 00 00                  call 0x140796ea4
007962E6  45 33 ED                        xor r13d, r13d
007962E9  45 8D 74 24 E3                  lea r14d, [r12 - 0x1d]
007962EE  4C 8D 7D D0                     lea r15, [rbp - 0x30]
007962F2  48 8D 35 27 E5 89 FF            lea rsi, [rip - 0x761ad9]
007962F9  41 8B 3F                        mov edi, dword ptr [r15]
007962FC  48 8B 03                        mov rax, qword ptr [rbx]
007962FF  83 E7 1F                        and edi, 0x1f
00796302  8B 4B 08                        mov ecx, dword ptr [rbx + 8]
00796305  44 8B 53 0C                     mov r10d, dword ptr [rbx + 0xc]
00796309  41 3B FE                        cmp edi, r14d
0079630C  75 78                           jne 0x140796386
0079630E  BF 01 00 00 00                  mov edi, 1
00796313  8B D1                           mov edx, ecx
00796315  48 C1 EA 03                     shr rdx, 3
00796319  44 8B C7                        mov r8d, edi
0079631C  48 03 D0                        add rdx, rax
0079631F  8B C1                           mov eax, ecx
00796321  83 E0 07                        and eax, 7
00796324  44 8D 4F 07                     lea r9d, [rdi + 7]
00796328  44 2B C8                        sub r9d, eax
0079632B  8D 41 01                        lea eax, [rcx + 1]
0079632E  41 3B C2                        cmp eax, r10d
00796331  76 0C                           jbe 0x14079633f
00796333  45 8B C2                        mov r8d, r10d
00796336  44 2B C1                        sub r8d, ecx
00796339  0F 84 10 02 00 00               je 0x14079654f
0079633F  45 3B C8                        cmp r9d, r8d
00796342  41 8B C0                        mov eax, r8d
00796345  41 8B C8                        mov ecx, r8d
00796348  41 0F 42 C1                     cmovb eax, r9d
0079634C  48 03 D7                        add rdx, rdi
0079634F  2B C8                           sub ecx, eax
00796351  45 8B CD                        mov r9d, r13d
00796354  83 F9 08                        cmp ecx, 8
00796357  72 18                           jb 0x140796371
00796359  8B C1                           mov eax, ecx
0079635B  48 C1 E8 03                     shr rax, 3
0079635F  44 88 0A                        mov byte ptr [rdx], r9b
00796362  83 C1 F8                        add ecx, -8
00796365  41 C1 E9 08                     shr r9d, 8
00796369  48 03 D7                        add rdx, rdi
0079636C  48 2B C7                        sub rax, rdi
0079636F  75 EE                           jne 0x14079635f
00796371  85 C9                           test ecx, ecx
00796373  74 08                           je 0x14079637d
00796375  8A 0C 8E                        mov cl, byte ptr [rsi + rcx*4]
00796378  41 22 C9                        and cl, r9b
0079637B  08 0A                           or byte ptr [rdx], cl
0079637D  44 01 43 08                     add dword ptr [rbx + 8], r8d
00796381  E9 C9 01 00 00                  jmp 0x14079654f
00796386  41 B9 01 00 00 00               mov r9d, 1
0079638C  4C 8B C1                        mov r8, rcx
0079638F  49 C1 E8 03                     shr r8, 3
00796393  8B F1                           mov esi, ecx
00796395  83 E6 07                        and esi, 7
00796398  4C 03 C0                        add r8, rax
0079639B  8D 41 01                        lea eax, [rcx + 1]
0079639E  45 8D 59 07                     lea r11d, [r9 + 7]
007963A2  44 2B DE                        sub r11d, esi
007963A5  41 3B C2                        cmp eax, r10d
007963A8  76 08                           jbe 0x1407963b2
007963AA  45 8B CA                        mov r9d, r10d
007963AD  44 2B C9                        sub r9d, ecx
007963B0  74 78                           je 0x14079642a
007963B2  45 3B D9                        cmp r11d, r9d
007963B5  48 8D 15 64 E4 89 FF            lea rdx, [rip - 0x761b9c]
007963BC  8B CE                           mov ecx, esi
007963BE  41 8B C1                        mov eax, r9d
007963C1  41 0F 42 C3                     cmovb eax, r11d
007963C5  BE 01 00 00 00                  mov esi, 1
007963CA  44 8B D6                        mov r10d, esi
007963CD  8A 14 82                        mov dl, byte ptr [rdx + rax*4]
007963D0  41 8B C1                        mov eax, r9d
007963D3  80 E2 01                        and dl, 1
007963D6  D2 E2                           shl dl, cl
007963D8  41 8B CB                        mov ecx, r11d
007963DB  41 08 10                        or byte ptr [r8], dl
007963DE  41 8B D1                        mov edx, r9d
007963E1  45 3B D9                        cmp r11d, r9d
007963E4  41 0F 42 C3                     cmovb eax, r11d
007963E8  41 D3 EA                        shr r10d, cl
007963EB  2B D0                           sub edx, eax
007963ED  4C 03 C6                        add r8, rsi
007963F0  83 FA 08                        cmp edx, 8
007963F3  72 18                           jb 0x14079640d
007963F5  8B C2                           mov eax, edx
007963F7  48 C1 E8 03                     shr rax, 3
007963FB  45 88 10                        mov byte ptr [r8], r10b
007963FE  83 C2 F8                        add edx, -8
00796401  41 C1 EA 08                     shr r10d, 8
00796405  4C 03 C6                        add r8, rsi
00796408  48 2B C6                        sub rax, rsi
0079640B  75 EE                           jne 0x1407963fb
0079640D  85 D2                           test edx, edx
0079640F  74 10                           je 0x140796421
00796411  48 8D 0D 08 E4 89 FF            lea rcx, [rip - 0x761bf8]
00796418  8A 0C 91                        mov cl, byte ptr [rcx + rdx*4]
0079641B  41 22 CA                        and cl, r10b
0079641E  41 08 08                        or byte ptr [r8], cl
00796421  8B 4B 08                        mov ecx, dword ptr [rbx + 8]
00796424  41 03 C9                        add ecx, r9d
00796427  89 4B 08                        mov dword ptr [rbx + 8], ecx
0079642A  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
0079642D  8D 51 03                        lea edx, [rcx + 3]
00796430  44 8B C1                        mov r8d, ecx
00796433  8B F1                           mov esi, ecx
00796435  49 C1 E8 03                     shr r8, 3
00796439  83 E6 07                        and esi, 7
0079643C  4C 03 03                        add r8, qword ptr [rbx]
0079643F  41 BA 08 00 00 00               mov r10d, 8
00796445  44 2B D6                        sub r10d, esi
00796448  41 B9 03 00 00 00               mov r9d, 3
0079644E  41 3B FE                        cmp edi, r14d
00796451  76 73                           jbe 0x1407964c6
00796453  44 8D 5F FF                     lea r11d, [rdi - 1]
00796457  3B D0                           cmp edx, eax
00796459  76 0C                           jbe 0x140796467
0079645B  44 8B C8                        mov r9d, eax
0079645E  44 2B C9                        sub r9d, ecx
00796461  0F 84 D9 00 00 00               je 0x140796540
00796467  45 3B D1                        cmp r10d, r9d
0079646A  4C 8D 35 AF E3 89 FF            lea r14, [rip - 0x761c51]
00796471  8B CE                           mov ecx, esi
00796473  41 8B C1                        mov eax, r9d
00796476  41 0F 42 C2                     cmovb eax, r10d
0079647A  41 8A 14 86                     mov dl, byte ptr [r14 + rax*4]
0079647E  41 8B C1                        mov eax, r9d
00796481  41 22 D3                        and dl, r11b
00796484  D2 E2                           shl dl, cl
00796486  41 8B CA                        mov ecx, r10d
00796489  41 08 10                        or byte ptr [r8], dl
0079648C  41 8B D1                        mov edx, r9d
0079648F  45 3B D1                        cmp r10d, r9d
00796492  41 0F 42 C2                     cmovb eax, r10d
00796496  41 D3 EB                        shr r11d, cl
00796499  B9 01 00 00 00                  mov ecx, 1
0079649E  2B D0                           sub edx, eax
007964A0  4C 03 C1                        add r8, rcx
007964A3  83 FA 08                        cmp edx, 8
007964A6  0F 82 82 00 00 00               jb 0x14079652e
007964AC  8B C2                           mov eax, edx
007964AE  48 C1 E8 03                     shr rax, 3
007964B2  45 88 18                        mov byte ptr [r8], r11b
007964B5  83 C2 F8                        add edx, -8
007964B8  41 C1 EB 08                     shr r11d, 8
007964BC  4C 03 C1                        add r8, rcx
007964BF  48 2B C1                        sub rax, rcx
007964C2  75 EE                           jne 0x1407964b2
007964C4  EB 68                           jmp 0x14079652e
007964C6  3B D0                           cmp edx, eax
007964C8  76 08                           jbe 0x1407964d2
007964CA  44 8B C8                        mov r9d, eax
007964CD  44 2B C9                        sub r9d, ecx
007964D0  74 6E                           je 0x140796540
007964D2  45 3B D1                        cmp r10d, r9d
007964D5  4C 8D 35 44 E3 89 FF            lea r14, [rip - 0x761cbc]
007964DC  8B CE                           mov ecx, esi
007964DE  41 8B C1                        mov eax, r9d
007964E1  41 0F 42 C2                     cmovb eax, r10d
007964E5  44 8B DF                        mov r11d, edi
007964E8  41 8A 14 86                     mov dl, byte ptr [r14 + rax*4]
007964EC  41 8B C1                        mov eax, r9d
007964EF  40 22 D7                        and dl, dil
007964F2  D2 E2                           shl dl, cl
007964F4  41 8B CA                        mov ecx, r10d
007964F7  41 08 10                        or byte ptr [r8], dl
007964FA  41 8B D1                        mov edx, r9d
007964FD  45 3B D1                        cmp r10d, r9d
00796500  41 0F 42 C2                     cmovb eax, r10d
00796504  41 D3 EB                        shr r11d, cl
00796507  B9 01 00 00 00                  mov ecx, 1
0079650C  2B D0                           sub edx, eax
0079650E  4C 03 C1                        add r8, rcx
00796511  83 FA 08                        cmp edx, 8
00796514  72 18                           jb 0x14079652e
00796516  8B C2                           mov eax, edx
00796518  48 C1 E8 03                     shr rax, 3
0079651C  45 88 18                        mov byte ptr [r8], r11b
0079651F  83 C2 F8                        add edx, -8
00796522  41 C1 EB 08                     shr r11d, 8
00796526  4C 03 C1                        add r8, rcx
00796529  48 2B C1                        sub rax, rcx
0079652C  75 EE                           jne 0x14079651c
0079652E  85 D2                           test edx, edx
00796530  74 0A                           je 0x14079653c
00796532  41 8A 0C 96                     mov cl, byte ptr [r14 + rdx*4]
00796536  41 22 CB                        and cl, r11b
00796539  41 08 08                        or byte ptr [r8], cl
0079653C  44 01 4B 08                     add dword ptr [rbx + 8], r9d
00796540  44 8B F7                        mov r14d, edi
00796543  48 8D 35 D6 E2 89 FF            lea rsi, [rip - 0x761d2a]
0079654A  BF 01 00 00 00                  mov edi, 1
0079654F  49 83 C7 04                     add r15, 4
00796553  4C 2B E7                        sub r12, rdi
00796556  0F 85 9D FD FF FF               jne 0x1407962f9
0079655C  45 0F B7 FD                     movzx r15d, r13w
00796560  41 BC 08 00 00 00               mov r12d, 8
00796566  44 8B 6C 24 30                  mov r13d, dword ptr [rsp + 0x30]
0079656B  44 89 64 24 34                  mov dword ptr [rsp + 0x34], r12d
00796570  45 85 ED                        test r13d, r13d
00796573  0F 84 54 06 00 00               je 0x140796bcd
00796579  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
0079657E  41 0F B7 C7                     movzx eax, r15w
00796582  41 8B 0C 80                     mov ecx, dword ptr [r8 + rax*4]
00796586  83 E1 1F                        and ecx, 0x1f
00796589  0F 84 EB 00 00 00               je 0x14079667a
0079658F  8B D1                           mov edx, ecx
00796591  41 3B CC                        cmp ecx, r12d
00796594  75 07                           jne 0x14079659d
00796596  BA 1E 00 00 00                  mov edx, 0x1e
0079659B  EB 2D                           jmp 0x1407965ca
0079659D  66 41 83 FF 10                  cmp r15w, 0x10
007965A2  72 1F                           jb 0x1407965c3
007965A4  41 8B 44 80 C0                  mov eax, dword ptr [r8 + rax*4 - 0x40]
007965A9  83 E0 1F                        and eax, 0x1f
007965AC  3B C8                           cmp ecx, eax
007965AE  75 07                           jne 0x1407965b7
007965B0  BA 1F 00 00 00                  mov edx, 0x1f
007965B5  EB 0C                           jmp 0x1407965c3
007965B7  FF C0                           inc eax
007965B9  3B C8                           cmp ecx, eax
007965BB  B8 20 00 00 00                  mov eax, 0x20
007965C0  0F 44 D0                        cmove edx, eax
007965C3  44 8B E1                        mov r12d, ecx
007965C6  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
007965CA  8B 7B 0C                        mov edi, dword ptr [rbx + 0xc]
007965CD  41 BB 08 00 00 00               mov r11d, 8
007965D3  8B C2                           mov eax, edx
007965D5  8B 53 08                        mov edx, dword ptr [rbx + 8]
007965D8  44 8B C2                        mov r8d, edx
007965DB  8B CA                           mov ecx, edx
007965DD  49 C1 E8 03                     shr r8, 3
007965E1  83 E1 07                        and ecx, 7
007965E4  44 8B 54 85 D0                  mov r10d, dword ptr [rbp + rax*4 - 0x30]
007965E9  44 2B D9                        sub r11d, ecx
007965EC  4C 03 03                        add r8, qword ptr [rbx]
007965EF  45 8B CA                        mov r9d, r10d
007965F2  41 83 E1 1F                     and r9d, 0x1f
007965F6  41 C1 EA 05                     shr r10d, 5
007965FA  42 8D 04 0A                     lea eax, [rdx + r9]
007965FE  3B C7                           cmp eax, edi
00796600  76 08                           jbe 0x14079660a
00796602  44 8B CF                        mov r9d, edi
00796605  44 2B CA                        sub r9d, edx
00796608  74 62                           je 0x14079666c
0079660A  45 3B D9                        cmp r11d, r9d
0079660D  41 8B C1                        mov eax, r9d
00796610  BF 01 00 00 00                  mov edi, 1
00796615  41 0F 42 C3                     cmovb eax, r11d
00796619  8A 14 86                        mov dl, byte ptr [rsi + rax*4]
0079661C  41 8B C1                        mov eax, r9d
0079661F  41 22 D2                        and dl, r10b
00796622  D2 E2                           shl dl, cl
00796624  41 8B CB                        mov ecx, r11d
00796627  41 08 10                        or byte ptr [r8], dl
0079662A  41 8B D1                        mov edx, r9d
0079662D  45 3B D9                        cmp r11d, r9d
00796630  41 0F 42 C3                     cmovb eax, r11d
00796634  41 D3 EA                        shr r10d, cl
00796637  2B D0                           sub edx, eax
00796639  4C 03 C7                        add r8, rdi
0079663C  83 FA 08                        cmp edx, 8
0079663F  72 18                           jb 0x140796659
00796641  8B C2                           mov eax, edx
00796643  48 C1 E8 03                     shr rax, 3
00796647  45 88 10                        mov byte ptr [r8], r10b
0079664A  83 C2 F8                        add edx, -8
0079664D  41 C1 EA 08                     shr r10d, 8
00796651  4C 03 C7                        add r8, rdi
00796654  48 2B C7                        sub rax, rdi
00796657  75 EE                           jne 0x140796647
00796659  85 D2                           test edx, edx
0079665B  74 09                           je 0x140796666
0079665D  8A 0C 96                        mov cl, byte ptr [rsi + rdx*4]
00796660  41 22 CA                        and cl, r10b
00796663  41 08 08                        or byte ptr [r8], cl
00796666  44 01 4B 08                     add dword ptr [rbx + 8], r9d
0079666A  EB 05                           jmp 0x140796671
0079666C  BF 01 00 00 00                  mov edi, 1
00796671  66 44 03 FF                     add r15w, di
00796675  E9 46 05 00 00                  jmp 0x140796bc0
0079667A  45 0F B7 D7                     movzx r10d, r15w
0079667E  EB 11                           jmp 0x140796691
00796680  41 0F B7 C7                     movzx eax, r15w
00796684  41 8B 0C 80                     mov ecx, dword ptr [r8 + rax*4]
00796688  F6 C1 1F                        test cl, 0x1f
0079668B  75 0D                           jne 0x14079669a
0079668D  66 44 03 FF                     add r15w, di
00796691  41 0F B7 C7                     movzx eax, r15w
00796695  41 3B C5                        cmp eax, r13d
00796698  72 E6                           jb 0x140796680
0079669A  41 0F B7 C7                     movzx eax, r15w
0079669E  66 41 33 C2                     xor ax, r10w
007966A2  66 83 F8 10                     cmp ax, 0x10
007966A6  0F 82 DB 00 00 00               jb 0x140796787
007966AC  8B 75 40                        mov esi, dword ptr [rbp + 0x40]
007966AF  4C 8D 2D 6A E1 89 FF            lea r13, [rip - 0x761e96]
007966B6  44 8B 75 40                     mov r14d, dword ptr [rbp + 0x40]
007966BA  83 E6 1F                        and esi, 0x1f
007966BD  41 C1 EE 05                     shr r14d, 5
007966C1  41 BC F0 FF 00 00               mov r12d, 0xfff0
007966C7  8B 53 08                        mov edx, dword ptr [rbx + 8]
007966CA  BF 08 00 00 00                  mov edi, 8
007966CF  44 8B 5B 0C                     mov r11d, dword ptr [rbx + 0xc]
007966D3  44 8B C2                        mov r8d, edx
007966D6  49 C1 E8 03                     shr r8, 3
007966DA  8B CA                           mov ecx, edx
007966DC  4C 03 03                        add r8, qword ptr [rbx]
007966DF  83 E1 07                        and ecx, 7
007966E2  2B F9                           sub edi, ecx
007966E4  8D 04 32                        lea eax, [rdx + rsi]
007966E7  44 8B CE                        mov r9d, esi
007966EA  41 3B C3                        cmp eax, r11d
007966ED  76 08                           jbe 0x1407966f7
007966EF  45 8B CB                        mov r9d, r11d
007966F2  44 2B CA                        sub r9d, edx
007966F5  74 66                           je 0x14079675d
007966F7  41 3B F9                        cmp edi, r9d
007966FA  41 8B C1                        mov eax, r9d
007966FD  45 8B DE                        mov r11d, r14d
00796700  0F 42 C7                        cmovb eax, edi
00796703  41 8A 54 85 00                  mov dl, byte ptr [r13 + rax*4]
00796708  41 8B C1                        mov eax, r9d
0079670B  41 22 D6                        and dl, r14b
0079670E  D2 E2                           shl dl, cl
00796710  8B CF                           mov ecx, edi
00796712  41 08 10                        or byte ptr [r8], dl
00796715  41 8B D1                        mov edx, r9d
00796718  41 3B F9                        cmp edi, r9d
0079671B  0F 42 C7                        cmovb eax, edi
0079671E  BF 01 00 00 00                  mov edi, 1
00796723  4C 03 C7                        add r8, rdi
00796726  41 D3 EB                        shr r11d, cl
00796729  2B D0                           sub edx, eax
0079672B  83 FA 08                        cmp edx, 8
0079672E  72 18                           jb 0x140796748
00796730  8B C2                           mov eax, edx
00796732  48 C1 E8 03                     shr rax, 3
00796736  45 88 18                        mov byte ptr [r8], r11b
00796739  83 C2 F8                        add edx, -8
0079673C  41 C1 EB 08                     shr r11d, 8
00796740  4C 03 C7                        add r8, rdi
00796743  48 2B C7                        sub rax, rdi
00796746  75 EE                           jne 0x140796736
00796748  85 D2                           test edx, edx
0079674A  74 0B                           je 0x140796757
0079674C  41 8A 4C 95 00                  mov cl, byte ptr [r13 + rdx*4]
00796751  41 22 CB                        and cl, r11b
00796754  41 08 08                        or byte ptr [r8], cl
00796757  44 01 4B 08                     add dword ptr [rbx + 8], r9d
0079675B  EB 05                           jmp 0x140796762
0079675D  BF 01 00 00 00                  mov edi, 1
00796762  66 45 23 D4                     and r10w, r12w
00796766  41 0F B7 C7                     movzx eax, r15w
0079676A  66 41 83 C2 10                  add r10w, 0x10
0079676F  66 41 33 C2                     xor ax, r10w
00796773  66 83 F8 10                     cmp ax, 0x10
00796777  0F 83 4A FF FF FF               jae 0x1407966c7
0079677D  44 8B 64 24 34                  mov r12d, dword ptr [rsp + 0x34]
00796782  44 8B 6C 24 30                  mov r13d, dword ptr [rsp + 0x30]
00796787  45 0F B7 CF                     movzx r9d, r15w
0079678B  41 0F B7 C2                     movzx eax, r10w
0079678F  44 2B C8                        sub r9d, eax
00796792  0F 84 21 04 00 00               je 0x140796bb9
00796798  41 83 F9 05                     cmp r9d, 5
0079679C  0F 83 C4 00 00 00               jae 0x140796866
007967A2  8B 75 D0                        mov esi, dword ptr [rbp - 0x30]
007967A5  4C 8D 2D 74 E0 89 FF            lea r13, [rip - 0x761f8c]
007967AC  44 8B 75 D0                     mov r14d, dword ptr [rbp - 0x30]
007967B0  83 E6 1F                        and esi, 0x1f
007967B3  41 C1 EE 05                     shr r14d, 5
007967B7  8B 53 08                        mov edx, dword ptr [rbx + 8]
007967BA  BF 08 00 00 00                  mov edi, 8
007967BF  44 8B 5B 0C                     mov r11d, dword ptr [rbx + 0xc]
007967C3  44 8B C2                        mov r8d, edx
007967C6  49 C1 E8 03                     shr r8, 3
007967CA  8B CA                           mov ecx, edx
007967CC  4C 03 03                        add r8, qword ptr [rbx]
007967CF  83 E1 07                        and ecx, 7
007967D2  2B F9                           sub edi, ecx
007967D4  8D 04 32                        lea eax, [rdx + rsi]
007967D7  44 8B D6                        mov r10d, esi
007967DA  41 3B C3                        cmp eax, r11d
007967DD  76 08                           jbe 0x1407967e7
007967DF  45 8B D3                        mov r10d, r11d
007967E2  44 2B D2                        sub r10d, edx
007967E5  74 66                           je 0x14079684d
007967E7  41 3B FA                        cmp edi, r10d
007967EA  41 8B C2                        mov eax, r10d
007967ED  45 8B DE                        mov r11d, r14d
007967F0  0F 42 C7                        cmovb eax, edi
007967F3  41 8A 54 85 00                  mov dl, byte ptr [r13 + rax*4]
007967F8  41 8B C2                        mov eax, r10d
007967FB  41 22 D6                        and dl, r14b
007967FE  D2 E2                           shl dl, cl
00796800  8B CF                           mov ecx, edi
00796802  41 08 10                        or byte ptr [r8], dl
00796805  41 8B D2                        mov edx, r10d
00796808  41 3B FA                        cmp edi, r10d
0079680B  0F 42 C7                        cmovb eax, edi
0079680E  BF 01 00 00 00                  mov edi, 1
00796813  4C 03 C7                        add r8, rdi
00796816  41 D3 EB                        shr r11d, cl
00796819  2B D0                           sub edx, eax
0079681B  83 FA 08                        cmp edx, 8
0079681E  72 18                           jb 0x140796838
00796820  8B C2                           mov eax, edx
00796822  48 C1 E8 03                     shr rax, 3
00796826  45 88 18                        mov byte ptr [r8], r11b
00796829  83 C2 F8                        add edx, -8
0079682C  41 C1 EB 08                     shr r11d, 8
00796830  4C 03 C7                        add r8, rdi
00796833  48 2B C7                        sub rax, rdi
00796836  75 EE                           jne 0x140796826
00796838  85 D2                           test edx, edx
0079683A  74 0B                           je 0x140796847
0079683C  41 8A 4C 95 00                  mov cl, byte ptr [r13 + rdx*4]
00796841  41 22 CB                        and cl, r11b
00796844  41 08 08                        or byte ptr [r8], cl
00796847  44 01 53 08                     add dword ptr [rbx + 8], r10d
0079684B  EB 05                           jmp 0x140796852
0079684D  BF 01 00 00 00                  mov edi, 1
00796852  41 83 C1 FF                     add r9d, -1
00796856  0F 85 5B FF FF FF               jne 0x1407967b7
0079685C  44 8B 6C 24 30                  mov r13d, dword ptr [rsp + 0x30]
00796861  E9 53 03 00 00                  jmp 0x140796bb9
00796866  8B 4B 08                        mov ecx, dword ptr [rbx + 8]
00796869  BF 08 00 00 00                  mov edi, 8
0079686E  44 8B 55 44                     mov r10d, dword ptr [rbp + 0x44]
00796872  44 8B C1                        mov r8d, ecx
00796875  44 8B 5D 44                     mov r11d, dword ptr [rbp + 0x44]
00796879  41 83 E2 1F                     and r10d, 0x1f
0079687D  8B 53 0C                        mov edx, dword ptr [rbx + 0xc]
00796880  8B F1                           mov esi, ecx
00796882  49 C1 E8 03                     shr r8, 3
00796886  83 E6 07                        and esi, 7
00796889  4C 03 03                        add r8, qword ptr [rbx]
0079688C  2B FE                           sub edi, esi
0079688E  42 8D 04 11                     lea eax, [rcx + r10]
00796892  41 C1 EB 05                     shr r11d, 5
00796896  3B C2                           cmp eax, edx
00796898  76 08                           jbe 0x1407968a2
0079689A  44 8B D2                        mov r10d, edx
0079689D  44 2B D1                        sub r10d, ecx
007968A0  74 6F                           je 0x140796911
007968A2  41 3B FA                        cmp edi, r10d
007968A5  4C 8D 35 74 DF 89 FF            lea r14, [rip - 0x76208c]
007968AC  8B CE                           mov ecx, esi
007968AE  41 8B C2                        mov eax, r10d
007968B1  0F 42 C7                        cmovb eax, edi
007968B4  BE 01 00 00 00                  mov esi, 1
007968B9  41 8A 14 86                     mov dl, byte ptr [r14 + rax*4]
007968BD  41 8B C2                        mov eax, r10d
007968C0  41 22 D3                        and dl, r11b
007968C3  D2 E2                           shl dl, cl
007968C5  8B CF                           mov ecx, edi
007968C7  41 08 10                        or byte ptr [r8], dl
007968CA  41 8B D2                        mov edx, r10d
007968CD  41 3B FA                        cmp edi, r10d
007968D0  0F 42 C7                        cmovb eax, edi
007968D3  41 D3 EB                        shr r11d, cl
007968D6  2B D0                           sub edx, eax
007968D8  4C 03 C6                        add r8, rsi
007968DB  83 FA 08                        cmp edx, 8
007968DE  72 18                           jb 0x1407968f8
007968E0  8B C2                           mov eax, edx
007968E2  48 C1 E8 03                     shr rax, 3
007968E6  45 88 18                        mov byte ptr [r8], r11b
007968E9  83 C2 F8                        add edx, -8
007968EC  41 C1 EB 08                     shr r11d, 8
007968F0  4C 03 C6                        add r8, rsi
007968F3  48 2B C6                        sub rax, rsi
007968F6  75 EE                           jne 0x1407968e6
007968F8  85 D2                           test edx, edx
007968FA  74 0A                           je 0x140796906
007968FC  41 8A 0C 96                     mov cl, byte ptr [r14 + rdx*4]
00796900  41 22 CB                        and cl, r11b
00796903  41 08 08                        or byte ptr [r8], cl
00796906  8B 4B 08                        mov ecx, dword ptr [rbx + 8]
00796909  41 03 CA                        add ecx, r10d
0079690C  89 4B 08                        mov dword ptr [rbx + 8], ecx
0079690F  EB 0C                           jmp 0x14079691d
00796911  BE 01 00 00 00                  mov esi, 1
00796916  4C 8D 35 03 DF 89 FF            lea r14, [rip - 0x7620fd]
0079691D  8B 53 0C                        mov edx, dword ptr [rbx + 0xc]
00796920  8B F9                           mov edi, ecx
00796922  83 E7 07                        and edi, 7
00796925  44 8B C1                        mov r8d, ecx
00796928  49 C1 E8 03                     shr r8, 3
0079692C  41 BB 08 00 00 00               mov r11d, 8
00796932  4C 03 03                        add r8, qword ptr [rbx]
00796935  44 2B DF                        sub r11d, edi
00796938  8B C1                           mov eax, ecx
0079693A  41 83 C1 FB                     add r9d, -5
0079693E  83 C0 02                        add eax, 2
00796941  41 BA 02 00 00 00               mov r10d, 2
00796947  41 83 F9 03                     cmp r9d, 3
0079694B  73 7E                           jae 0x1407969cb
0079694D  3B C2                           cmp eax, edx
0079694F  76 0C                           jbe 0x14079695d
00796951  44 8B D2                        mov r10d, edx
00796954  44 2B D1                        sub r10d, ecx
00796957  0F 84 57 02 00 00               je 0x140796bb4
0079695D  45 3B DA                        cmp r11d, r10d
00796960  48 8D 35 B9 DE 89 FF            lea rsi, [rip - 0x762147]
00796967  8B CF                           mov ecx, edi
00796969  41 8B C2                        mov eax, r10d
0079696C  41 0F 42 C3                     cmovb eax, r11d
00796970  BF 01 00 00 00                  mov edi, 1
00796975  8A 14 86                        mov dl, byte ptr [rsi + rax*4]
00796978  41 8B C2                        mov eax, r10d
0079697B  41 22 D1                        and dl, r9b
0079697E  D2 E2                           shl dl, cl
00796980  41 8B CB                        mov ecx, r11d
00796983  41 08 10                        or byte ptr [r8], dl
00796986  41 8B D2                        mov edx, r10d
00796989  45 3B DA                        cmp r11d, r10d
0079698C  41 0F 42 C3                     cmovb eax, r11d
00796990  41 D3 E9                        shr r9d, cl
00796993  2B D0                           sub edx, eax
00796995  4C 03 C7                        add r8, rdi
00796998  83 FA 08                        cmp edx, 8
0079699B  72 18                           jb 0x1407969b5
0079699D  8B C2                           mov eax, edx
0079699F  48 C1 E8 03                     shr rax, 3
007969A3  45 88 08                        mov byte ptr [r8], r9b
007969A6  83 C2 F8                        add edx, -8
007969A9  41 C1 E9 08                     shr r9d, 8
007969AD  4C 03 C7                        add r8, rdi
007969B0  48 2B C7                        sub rax, rdi
007969B3  75 EE                           jne 0x1407969a3
007969B5  85 D2                           test edx, edx
007969B7  74 09                           je 0x1407969c2
007969B9  8A 0C 96                        mov cl, byte ptr [rsi + rdx*4]
007969BC  41 22 C9                        and cl, r9b
007969BF  41 08 08                        or byte ptr [r8], cl
007969C2  44 01 53 08                     add dword ptr [rbx + 8], r10d
007969C6  E9 F5 01 00 00                  jmp 0x140796bc0
007969CB  3B C2                           cmp eax, edx
007969CD  76 08                           jbe 0x1407969d7
007969CF  44 8B D2                        mov r10d, edx
007969D2  44 2B D1                        sub r10d, ecx
007969D5  74 6A                           je 0x140796a41
007969D7  8B CF                           mov ecx, edi
007969D9  45 3B DA                        cmp r11d, r10d
007969DC  41 8B C2                        mov eax, r10d
007969DF  BF 03 00 00 00                  mov edi, 3
007969E4  41 0F 42 C3                     cmovb eax, r11d
007969E8  41 8A 14 86                     mov dl, byte ptr [r14 + rax*4]
007969EC  41 8B C2                        mov eax, r10d
007969EF  80 E2 03                        and dl, 3
007969F2  D2 E2                           shl dl, cl
007969F4  41 8B CB                        mov ecx, r11d
007969F7  41 08 10                        or byte ptr [r8], dl
007969FA  41 8B D2                        mov edx, r10d
007969FD  45 3B DA                        cmp r11d, r10d
00796A00  41 0F 42 C3                     cmovb eax, r11d
00796A04  D3 EF                           shr edi, cl
00796A06  2B D0                           sub edx, eax
00796A08  4C 03 C6                        add r8, rsi
00796A0B  83 FA 08                        cmp edx, 8
00796A0E  72 17                           jb 0x140796a27
00796A10  8B C2                           mov eax, edx
00796A12  48 C1 E8 03                     shr rax, 3
00796A16  41 88 38                        mov byte ptr [r8], dil
00796A19  83 C2 F8                        add edx, -8
00796A1C  C1 EF 08                        shr edi, 8
00796A1F  4C 03 C6                        add r8, rsi
00796A22  48 2B C6                        sub rax, rsi
00796A25  75 EF                           jne 0x140796a16
00796A27  85 D2                           test edx, edx
00796A29  74 0A                           je 0x140796a35
00796A2B  41 8A 0C 96                     mov cl, byte ptr [r14 + rdx*4]
00796A2F  40 22 CF                        and cl, dil
00796A32  41 08 08                        or byte ptr [r8], cl
00796A35  8B 4B 08                        mov ecx, dword ptr [rbx + 8]
00796A38  8B 53 0C                        mov edx, dword ptr [rbx + 0xc]
00796A3B  41 03 CA                        add ecx, r10d
00796A3E  89 4B 08                        mov dword ptr [rbx + 8], ecx
00796A41  41 83 C1 FD                     add r9d, -3
00796A45  44 8B DA                        mov r11d, edx
00796A48  41 83 F9 07                     cmp r9d, 7
00796A4C  0F 82 D6 00 00 00               jb 0x140796b28
00796A52  B8 25 49 92 24                  mov eax, 0x24924925
00796A57  4C 8D 2D C2 DD 89 FF            lea r13, [rip - 0x76223e]
00796A5E  41 F7 E1                        mul r9d
00796A61  45 8B F1                        mov r14d, r9d
00796A64  44 2B F2                        sub r14d, edx
00796A67  41 D1 EE                        shr r14d, 1
00796A6A  44 03 F2                        add r14d, edx
00796A6D  41 C1 EE 02                     shr r14d, 2
00796A71  41 BA 03 00 00 00               mov r10d, 3
00796A77  44 8B C1                        mov r8d, ecx
00796A7A  49 C1 E8 03                     shr r8, 3
00796A7E  8D 41 03                        lea eax, [rcx + 3]
00796A81  4C 03 03                        add r8, qword ptr [rbx]
00796A84  8B F1                           mov esi, ecx
00796A86  83 E6 07                        and esi, 7
00796A89  41 8B D3                        mov edx, r11d
00796A8C  41 8D 7A 05                     lea edi, [r10 + 5]
00796A90  2B FE                           sub edi, esi
00796A92  41 3B C3                        cmp eax, r11d
00796A95  76 0A                           jbe 0x140796aa1
00796A97  44 8B D2                        mov r10d, edx
00796A9A  8B C1                           mov eax, ecx
00796A9C  44 2B D1                        sub r10d, ecx
00796A9F  74 72                           je 0x140796b13
00796AA1  41 3B FA                        cmp edi, r10d
00796AA4  8B CE                           mov ecx, esi
00796AA6  41 8B C2                        mov eax, r10d
00796AA9  41 BB 07 00 00 00               mov r11d, 7
00796AAF  0F 42 C7                        cmovb eax, edi
00796AB2  41 8A 54 85 00                  mov dl, byte ptr [r13 + rax*4]
00796AB7  41 8B C2                        mov eax, r10d
00796ABA  80 E2 07                        and dl, 7
00796ABD  D2 E2                           shl dl, cl
00796ABF  8B CF                           mov ecx, edi
00796AC1  41 08 10                        or byte ptr [r8], dl
00796AC4  41 8B D2                        mov edx, r10d
00796AC7  41 3B FA                        cmp edi, r10d
00796ACA  0F 42 C7                        cmovb eax, edi
00796ACD  41 D3 EB                        shr r11d, cl
00796AD0  B9 01 00 00 00                  mov ecx, 1
00796AD5  2B D0                           sub edx, eax
00796AD7  4C 03 C1                        add r8, rcx
00796ADA  83 FA 08                        cmp edx, 8
00796ADD  72 18                           jb 0x140796af7
00796ADF  8B C2                           mov eax, edx
00796AE1  48 C1 E8 03                     shr rax, 3
00796AE5  45 88 18                        mov byte ptr [r8], r11b
00796AE8  83 C2 F8                        add edx, -8
00796AEB  41 C1 EB 08                     shr r11d, 8
00796AEF  4C 03 C1                        add r8, rcx
00796AF2  48 2B C1                        sub rax, rcx
00796AF5  75 EE                           jne 0x140796ae5
00796AF7  85 D2                           test edx, edx
00796AF9  74 0B                           je 0x140796b06
00796AFB  41 8A 4C 95 00                  mov cl, byte ptr [r13 + rdx*4]
00796B00  41 22 CB                        and cl, r11b
00796B03  41 08 08                        or byte ptr [r8], cl
00796B06  44 01 53 08                     add dword ptr [rbx + 8], r10d
00796B0A  8B 53 0C                        mov edx, dword ptr [rbx + 0xc]
00796B0D  44 8B DA                        mov r11d, edx
00796B10  8B 43 08                        mov eax, dword ptr [rbx + 8]
00796B13  41 83 C1 F9                     add r9d, -7
00796B17  8B C8                           mov ecx, eax
00796B19  49 83 EE 01                     sub r14, 1
00796B1D  0F 85 4E FF FF FF               jne 0x140796a71
00796B23  44 8B 6C 24 30                  mov r13d, dword ptr [rsp + 0x30]
00796B28  41 BA 03 00 00 00               mov r10d, 3
00796B2E  44 8B C1                        mov r8d, ecx
00796B31  49 C1 E8 03                     shr r8, 3
00796B35  8D 41 03                        lea eax, [rcx + 3]
00796B38  4C 03 03                        add r8, qword ptr [rbx]
00796B3B  8B F9                           mov edi, ecx
00796B3D  83 E7 07                        and edi, 7
00796B40  45 8D 5A 05                     lea r11d, [r10 + 5]
00796B44  44 2B DF                        sub r11d, edi
00796B47  3B C2                           cmp eax, edx
00796B49  76 08                           jbe 0x140796b53
00796B4B  44 8B D2                        mov r10d, edx
00796B4E  44 2B D1                        sub r10d, ecx
00796B51  74 61                           je 0x140796bb4
00796B53  45 3B DA                        cmp r11d, r10d
00796B56  48 8D 35 C3 DC 89 FF            lea rsi, [rip - 0x76233d]
00796B5D  8B CF                           mov ecx, edi
00796B5F  41 8B C2                        mov eax, r10d
00796B62  41 0F 42 C3                     cmovb eax, r11d
00796B66  BF 01 00 00 00                  mov edi, 1
00796B6B  8A 14 86                        mov dl, byte ptr [rsi + rax*4]
00796B6E  41 8B C2                        mov eax, r10d
00796B71  41 22 D1                        and dl, r9b
00796B74  D2 E2                           shl dl, cl
00796B76  41 8B CB                        mov ecx, r11d
00796B79  41 08 10                        or byte ptr [r8], dl
00796B7C  41 8B D2                        mov edx, r10d
00796B7F  45 3B DA                        cmp r11d, r10d
00796B82  41 0F 42 C3                     cmovb eax, r11d
00796B86  41 D3 E9                        shr r9d, cl
00796B89  2B D0                           sub edx, eax
00796B8B  4C 03 C7                        add r8, rdi
00796B8E  83 FA 08                        cmp edx, 8
00796B91  0F 82 1E FE FF FF               jb 0x1407969b5
00796B97  8B C2                           mov eax, edx
00796B99  48 C1 E8 03                     shr rax, 3
00796B9D  45 88 08                        mov byte ptr [r8], r9b
00796BA0  83 C2 F8                        add edx, -8
00796BA3  41 C1 E9 08                     shr r9d, 8
00796BA7  4C 03 C7                        add r8, rdi
00796BAA  48 2B C7                        sub rax, rdi
00796BAD  75 EE                           jne 0x140796b9d
00796BAF  E9 01 FE FF FF                  jmp 0x1407969b5
00796BB4  BF 01 00 00 00                  mov edi, 1
00796BB9  48 8D 35 60 DC 89 FF            lea rsi, [rip - 0x7623a0]
00796BC0  41 0F B7 C7                     movzx eax, r15w
00796BC4  41 3B C5                        cmp eax, r13d
00796BC7  0F 82 AC F9 FF FF               jb 0x140796579
00796BCD  33 C0                           xor eax, eax
00796BCF  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
00796BD3  48 33 CC                        xor rcx, rsp
00796BD6  E8 65 5A F1 FF                  call 0x1406ac640
00796BDB  48 8B 9C 24 C0 01 00 00         mov rbx, qword ptr [rsp + 0x1c0]
00796BE3  48 81 C4 70 01 00 00            add rsp, 0x170
00796BEA  41 5F                           pop r15
00796BEC  41 5E                           pop r14
00796BEE  41 5D                           pop r13
00796BF0  41 5C                           pop r12
00796BF2  5F                              pop rdi
00796BF3  5E                              pop rsi
00796BF4  5D                              pop rbp
00796BF5  C3                              ret
00796BF6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Xp10BuildAndWriteHuffmanTables(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned int v_stack_m174;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mF4;
    unsigned int v_stack_mF8;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (368);
    result = (*(unsigned __int64 *)(v_rip + 6768033)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m178 = a3;
    v_stack_m170 = a2;
    a2 = 0;
    result = memset(v_stack_m168, a2, 132, a4);
    a2 = 0;
    result = memset(v_stack_mD8, a2, 132, a4);
    result = 0;
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_007962C4;
loc_00796205:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 0 * 4))) & ((unsigned int)(132 - 124 + 23)));
    if (condition_is_equal) goto loc_0079624F;
    if (((unsigned int)(a1)) != ((unsigned int)((unsigned int)((unsigned int)(132 - 124))))) goto loc_00796220;
    goto loc_00796241;
loc_00796220:
    if (0 < 16) goto loc_0079623E;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 0 * 4 - 64))) & ((unsigned int)(132 - 124 + 23)));
    if (((unsigned int)(a1)) != ((unsigned int)(result))) goto loc_00796236;
    goto loc_0079623E;
loc_00796236:
    result = (unsigned int)((result) + 1);
    a3 = (unsigned int)((unsigned int)(132 - 124 + 23));
    if (((unsigned int)(a1)) == ((unsigned int)(result))) { a3 = (unsigned int)(132 - 124 + 24); }
loc_0079623E:
loc_00796241:
    a2 = (unsigned __int16)((0) + ((unsigned __int16)(132 - 124 - 7)));
    goto loc_007962B8;
loc_0079624F:
    goto loc_00796264;
loc_00796255:
    if ((((unsigned __int8)(132 - 124 + 23)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + (unsigned __int16)(a2) * 4))))) != 0) goto loc_0079626C;
    a2 = (unsigned __int16)((a2) + ((unsigned __int16)(132 - 124 - 7)));
loc_00796264:
    if (((unsigned int)((unsigned __int16)(a2))) < ((unsigned int)((unsigned int)(a3)))) goto loc_00796255;
loc_0079626C:
    result = (unsigned __int16)(((unsigned __int16)(a2)) ^ ((unsigned __int16)((unsigned __int16)(a2))));
    if (((unsigned __int16)(result)) < 16) goto loc_0079629E;
loc_0079627F:
    a3 = (unsigned __int16)(((unsigned __int16)(a2)) & ((unsigned __int16)((unsigned int)(0xFFF0ULL))));
    a3 = (unsigned __int16)((a3) + (16));
    result = (unsigned __int16)(((unsigned __int16)(a2)) ^ ((unsigned __int16)(a3)));
    if (((unsigned __int16)(result)) >= 16) goto loc_0079627F;
loc_0079629E:
    a1 = (unsigned int)(((unsigned __int16)(a2)) - ((unsigned int)((unsigned __int16)(a3))));
    if (condition_is_equal) goto loc_007962B8;
    if (((unsigned int)(a1)) >= 5) goto loc_007962B4;
    goto loc_007962B8;
loc_007962B4:
loc_007962B8:
    if (((unsigned int)((unsigned __int16)(a2))) < ((unsigned int)((unsigned int)(a3)))) goto loc_00796205;
loc_007962C4:
    v_stack_m188 = v_stack_mD8;
    result = Xp10BuildHuffmanEncodings(a1, v_stack_m168, 33, (unsigned int)((unsigned int)(132 - 124)));
    v_r13 = 0;
loc_007962F9:
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mD8))) & (31));
    if (((unsigned int)(v_rdi)) != ((unsigned int)(33 - 29))) goto loc_00796386;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8))))) >> (3);
    a2 = (a2) + (*(unsigned __int64 *)(a4));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8))))) & (7));
    a4 = (unsigned int)((1 + 7) - ((unsigned int)(result)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8)) + 1)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))) goto loc_0079633F;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8)))));
    if (condition_is_equal) goto loc_0079654F;
loc_0079633F:
    result = (unsigned int)(a3);
    if (((unsigned int)(a4)) < a3) { result = (unsigned int)(a4); }
    a2 = (a2) + (1);
    a1 = (unsigned int)(((unsigned int)(a3)) - ((unsigned int)(result)));
    if (((unsigned int)(a1)) < 8) goto loc_00796371;
    result = ((unsigned int)((unsigned int)(a1))) >> (3);
loc_0079635F:
    *(unsigned __int8 *)(a2) = 0;
    a1 = (unsigned int)((a1) + (-8));
    a4 = (unsigned int)((0) >> (8));
    a2 = (a2) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_0079635F;
loc_00796371:
    if ((unsigned int)(a1) != 0) {
        a1 = *(unsigned __int8 *)(v_rip - 7740121 + a1 * 4);
        a1 = (unsigned __int8)((a1) & ((unsigned __int8)(a4)));
    }
    goto loc_0079654F;
loc_00796386:
    a3 = (a1) >> (3);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (7));
    a3 = (a3) + (result);
    v_r11 = (unsigned int)((1 + 7) - ((unsigned int)(v_rsi)));
    if (((unsigned int)(a1 + 1)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))) goto loc_007963B2;
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))) - ((unsigned int)(a1)));
    if (condition_is_equal) goto loc_0079642A;
loc_007963B2:
    result = (unsigned int)((unsigned int)(a4));
    if (((unsigned int)(v_r11)) < ((unsigned int)(a4))) { result = (unsigned int)(v_r11); }
    a2 = (unsigned __int8)((*(unsigned __int8 *)(v_rip - 7740316 + result * 4)) & (1));
    a2 = (unsigned __int8)((a2) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rsi)))));
    result = (unsigned int)((unsigned int)(a4));
    if (((unsigned int)(v_r11)) < ((unsigned int)(a4))) { result = (unsigned int)(v_r11); }
    v_r10 = (unsigned int)((1) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_r11)))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a4))) - ((unsigned int)(result)));
    a3 = (a3) + (1);
    if (((unsigned int)(a2)) < 8) goto loc_0079640D;
    result = ((unsigned int)((unsigned int)(a2))) >> (3);
loc_007963FB:
    *(unsigned __int8 *)(a3) = (unsigned __int8)(v_r10);
    a2 = (unsigned int)((a2) + (-8));
    v_r10 = (unsigned int)((v_r10) >> (8));
    a3 = (a3) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_007963FB;
loc_0079640D:
    if ((unsigned int)(a2) != 0) {
        a1 = v_rip - 7740408;
        a1 = *(unsigned __int8 *)(a1 + a2 * 4);
        a1 = (unsigned __int8)((a1) & ((unsigned __int8)(v_r10)));
    }
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 8))) + ((unsigned int)(a4)));
    *(unsigned int *)(a4 + 8) = (unsigned int)(a1);
loc_0079642A:
    a3 = ((unsigned int)((unsigned int)(a1))) >> (3);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (7));
    a3 = (a3) + (*(unsigned __int64 *)(a4));
    v_r10 = (unsigned int)((8) - ((unsigned int)(v_rsi)));
    if (1 <= ((unsigned int)(33 - 29))) goto loc_007964C6;
    if (((unsigned int)(a1 + 3)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))) goto loc_00796467;
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))) - ((unsigned int)(a1)));
    if (condition_is_equal) goto loc_00796540;
loc_00796467:
    result = (unsigned int)((unsigned int)(a4));
    if (((unsigned int)(v_r10)) < ((unsigned int)(a4))) { result = (unsigned int)(v_r10); }
    a2 = (unsigned __int8)((*(unsigned __int8 *)(v_rip - 7740497 + result * 4)) & ((unsigned __int8)(1 - 1)));
    a2 = (unsigned __int8)((a2) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rsi)))));
    result = (unsigned int)((unsigned int)(a4));
    if (((unsigned int)(v_r10)) < ((unsigned int)(a4))) { result = (unsigned int)(v_r10); }
    v_r11 = (unsigned int)((1 - 1) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_r10)))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a4))) - ((unsigned int)(result)));
    a3 = (a3) + (1);
    if (((unsigned int)(a2)) < 8) goto loc_0079652E;
    result = ((unsigned int)((unsigned int)(a2))) >> (3);
loc_007964B2:
    *(unsigned __int8 *)(a3) = (unsigned __int8)(v_r11);
    a2 = (unsigned int)((a2) + (-8));
    v_r11 = (unsigned int)((v_r11) >> (8));
    a3 = (a3) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_007964B2;
    goto loc_0079652E;
loc_007964C6:
    if (((unsigned int)(a2)) <= ((unsigned int)(result))) goto loc_007964D2;
    a4 = (unsigned int)(((unsigned int)((unsigned int)(result))) - (1));
    if (condition_is_equal) goto loc_00796540;
loc_007964D2:
    result = (unsigned int)((unsigned int)(a4));
    if (((unsigned int)(v_r10)) < ((unsigned int)(a4))) { result = (unsigned int)(v_r10); }
    a2 = (unsigned __int8)((*(unsigned __int8 *)(v_rip - 7740604 + result * 4)) & (1));
    a2 = (unsigned __int8)((a2) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rsi)))));
    result = (unsigned int)((unsigned int)(a4));
    if (((unsigned int)(v_r10)) < ((unsigned int)(a4))) { result = (unsigned int)(v_r10); }
    v_r11 = (unsigned int)((1) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_r10)))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a4))) - ((unsigned int)(result)));
    a3 = (a3) + (1);
    if (((unsigned int)(a2)) < 8) goto loc_0079652E;
    result = ((unsigned int)((unsigned int)(a2))) >> (3);
loc_0079651C:
    *(unsigned __int8 *)(a3) = (unsigned __int8)(v_r11);
    a2 = (unsigned int)((a2) + (-8));
    v_r11 = (unsigned int)((v_r11) >> (8));
    a3 = (a3) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_0079651C;
loc_0079652E:
    if ((unsigned int)(a2) != 0) {
        a1 = *(unsigned __int8 *)(v_rip - 7740604 + a2 * 4);
        a1 = (unsigned __int8)((a1) & ((unsigned __int8)(v_r11)));
    }
loc_00796540:
loc_0079654F:
    v_r15 = (v_stack_mD8) + (4);
    v_r12 = (33) - (1);
    if (condition_is_not_equal) goto loc_007962F9;
    v_stack_m174 = 8;
    if ((unsigned int)((unsigned int)(v_stack_m178)) == 0) goto loc_00796BCD;
loc_00796579:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m170 + 0 * 4))) & (31));
    if (condition_is_equal) goto loc_0079667A;
    if (((unsigned int)(a1)) != 8) goto loc_0079659D;
    goto loc_007965CA;
loc_0079659D:
    if (0 < 16) goto loc_007965C3;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m170 + 0 * 4 - 64))) & (31));
    if (((unsigned int)(a1)) != ((unsigned int)(result))) goto loc_007965B7;
    goto loc_007965C3;
loc_007965B7:
    result = (unsigned int)((result) + 1);
    a2 = 31;
    if (((unsigned int)(a1)) == ((unsigned int)(result))) { a2 = 32; }
loc_007965C3:
    v_stack_m174 = (unsigned int)(a1);
loc_007965CA:
    a3 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8))))) >> (3);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8))))) & (7));
    v_r11 = (unsigned int)((8) - ((unsigned int)(a1)));
    a3 = (a3) + (*(unsigned __int64 *)(a4));
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mA8 + (unsigned int)((unsigned int)(a2)) * 4 - 48))))) & (31));
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mA8 + (unsigned int)((unsigned int)(a2)) * 4 - 48))) >> (5));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8)) + a4 * 1)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))) goto loc_0079660A;
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8)))));
    if (condition_is_equal) goto loc_0079666C;
loc_0079660A:
    result = (unsigned int)((unsigned int)(a4));
    if (((unsigned int)(v_r11)) < ((unsigned int)(a4))) { result = (unsigned int)(v_r11); }
    a2 = (unsigned __int8)((*(unsigned __int8 *)(v_rip - 7740714 + result * 4)) & ((unsigned __int8)(v_r10)));
    a2 = (unsigned __int8)((a2) << ((unsigned __int8)(a1)));
    result = (unsigned int)((unsigned int)(a4));
    if (((unsigned int)(v_r11)) < ((unsigned int)(a4))) { result = (unsigned int)(v_r11); }
    v_r10 = (unsigned int)((v_r10) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_r11)))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a4))) - ((unsigned int)(result)));
    a3 = (a3) + (1);
    if (((unsigned int)(a2)) < 8) goto loc_00796659;
    result = ((unsigned int)((unsigned int)(a2))) >> (3);
loc_00796647:
    *(unsigned __int8 *)(a3) = (unsigned __int8)(v_r10);
    a2 = (unsigned int)((a2) + (-8));
    v_r10 = (unsigned int)((v_r10) >> (8));
    a3 = (a3) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00796647;
loc_00796659:
    if ((unsigned int)(a2) != 0) {
        a1 = *(unsigned __int8 *)(v_rip - 7740714 + a2 * 4);
        a1 = (unsigned __int8)((a1) & ((unsigned __int8)(v_r10)));
    }
    goto loc_00796671;
loc_0079666C:
loc_00796671:
    v_r15 = (unsigned __int16)((0) + (1));
    goto loc_00796BC0;
loc_0079667A:
    goto loc_00796691;
loc_00796680:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + (unsigned __int16)(v_r15) * 4)))) & (31)) != 0) goto loc_0079669A;
    v_r15 = (unsigned __int16)((v_r15) + (1));
loc_00796691:
    if (((unsigned int)((unsigned __int16)(v_r15))) < ((unsigned int)((unsigned int)(v_stack_m178)))) goto loc_00796680;
loc_0079669A:
    result = (unsigned __int16)(((unsigned __int16)(v_r15)) ^ ((unsigned __int16)((unsigned __int16)(v_r15))));
    if (((unsigned __int16)(result)) < 16) goto loc_00796787;
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m68)) & (31));
    v_r14 = (unsigned int)(((unsigned int)(v_stack_m68)) >> (5));
loc_007966C7:
    a3 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8))))) >> (3);
    a3 = (a3) + (*(unsigned __int64 *)(a4));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8))))) & (7));
    v_rdi = (unsigned int)((8) - ((unsigned int)(a1)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8)) + v_rsi * 1)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))) goto loc_007966F7;
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8)))));
    if (condition_is_equal) goto loc_0079675D;
loc_007966F7:
    result = (unsigned int)((unsigned int)(a4));
    if (((unsigned int)(v_rdi)) < ((unsigned int)(a4))) { result = (unsigned int)(v_rdi); }
    a2 = (unsigned __int8)((*(unsigned __int8 *)(v_rip - 7741078 + result * 4)) & ((unsigned __int8)(v_r14)));
    a2 = (unsigned __int8)((a2) << ((unsigned __int8)(a1)));
    result = (unsigned int)((unsigned int)(a4));
    if (((unsigned int)(v_rdi)) < ((unsigned int)(a4))) { result = (unsigned int)(v_rdi); }
    a3 = (a3) + (1);
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi)))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a4))) - ((unsigned int)(result)));
    if (((unsigned int)(a2)) < 8) goto loc_00796748;
    result = ((unsigned int)((unsigned int)(a2))) >> (3);
loc_00796736:
    *(unsigned __int8 *)(a3) = (unsigned __int8)(v_r11);
    a2 = (unsigned int)((a2) + (-8));
    v_r11 = (unsigned int)((v_r11) >> (8));
    a3 = (a3) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00796736;
loc_00796748:
    if ((unsigned int)(a2) != 0) {
        a1 = *(unsigned __int8 *)(v_rip - 7741078 + a2 * 4);
        a1 = (unsigned __int8)((a1) & ((unsigned __int8)(v_r11)));
    }
    goto loc_00796762;
loc_0079675D:
loc_00796762:
    v_r10 = (unsigned __int16)(((unsigned __int16)(v_r15)) & ((unsigned __int16)((unsigned int)(0xFFF0ULL))));
    v_r10 = (unsigned __int16)((v_r10) + (16));
    result = (unsigned __int16)(((unsigned __int16)(v_r15)) ^ ((unsigned __int16)(v_r10)));
    if (((unsigned __int16)(result)) >= 16) goto loc_007966C7;
loc_00796787:
    a4 = (unsigned int)(((unsigned __int16)(v_r15)) - ((unsigned int)((unsigned __int16)(v_r10))));
    if (condition_is_equal) goto loc_00796BB9;
    if (((unsigned int)(a4)) >= 5) goto loc_00796866;
    v_rsi = (unsigned int)(((unsigned int)(v_stack_mD8)) & (31));
    v_r14 = (unsigned int)(((unsigned int)(v_stack_mD8)) >> (5));
loc_007967B7:
    a3 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8))))) >> (3);
    a3 = (a3) + (*(unsigned __int64 *)(a4));
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8))))) & (7));
    v_rdi = (unsigned int)((8) - ((unsigned int)(a1)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8)) + v_rsi * 1)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))) goto loc_007967E7;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8)))));
    if (condition_is_equal) goto loc_0079684D;
loc_007967E7:
    result = (unsigned int)((unsigned int)(v_r10));
    if (((unsigned int)(v_rdi)) < ((unsigned int)(v_r10))) { result = (unsigned int)(v_rdi); }
    a2 = (unsigned __int8)((*(unsigned __int8 *)(v_rip - 7741324 + result * 4)) & ((unsigned __int8)(v_r14)));
    a2 = (unsigned __int8)((a2) << ((unsigned __int8)(a1)));
    result = (unsigned int)((unsigned int)(v_r10));
    if (((unsigned int)(v_rdi)) < ((unsigned int)(v_r10))) { result = (unsigned int)(v_rdi); }
    a3 = (a3) + (1);
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi)))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) - ((unsigned int)(result)));
    if (((unsigned int)(a2)) < 8) goto loc_00796838;
    result = ((unsigned int)((unsigned int)(a2))) >> (3);
loc_00796826:
    *(unsigned __int8 *)(a3) = (unsigned __int8)(v_r11);
    a2 = (unsigned int)((a2) + (-8));
    v_r11 = (unsigned int)((v_r11) >> (8));
    a3 = (a3) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00796826;
loc_00796838:
    if ((unsigned int)(a2) != 0) {
        a1 = *(unsigned __int8 *)(v_rip - 7741324 + a2 * 4);
        a1 = (unsigned __int8)((a1) & ((unsigned __int8)(v_r11)));
    }
    goto loc_00796852;
loc_0079684D:
loc_00796852:
    a4 = (unsigned int)((a4) + (-1));
    if (condition_is_not_equal) goto loc_007967B7;
    goto loc_00796BB9;
loc_00796866:
    v_r10 = (unsigned int)(((unsigned int)(v_stack_m64)) & (31));
    a3 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8))))) >> (3);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8))))) & (7));
    a3 = (a3) + (*(unsigned __int64 *)(a4));
    v_rdi = (unsigned int)((8) - ((unsigned int)(v_rsi)));
    v_r11 = (unsigned int)(((unsigned int)(v_stack_m64)) >> (5));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8)) + v_r10 * 1)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))) goto loc_007968A2;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8)))));
    if (condition_is_equal) goto loc_00796911;
loc_007968A2:
    result = (unsigned int)((unsigned int)(v_r10));
    if (((unsigned int)(v_rdi)) < ((unsigned int)(v_r10))) { result = (unsigned int)(v_rdi); }
    a2 = (unsigned __int8)((*(unsigned __int8 *)(v_rip - 7741580 + result * 4)) & ((unsigned __int8)(v_r11)));
    a2 = (unsigned __int8)((a2) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rsi)))));
    result = (unsigned int)((unsigned int)(v_r10));
    if (((unsigned int)(v_rdi)) < ((unsigned int)(v_r10))) { result = (unsigned int)(v_rdi); }
    v_r11 = (unsigned int)((v_r11) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi)))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) - ((unsigned int)(result)));
    a3 = (a3) + (1);
    if (((unsigned int)(a2)) < 8) goto loc_007968F8;
    result = ((unsigned int)((unsigned int)(a2))) >> (3);
loc_007968E6:
    *(unsigned __int8 *)(a3) = (unsigned __int8)(v_r11);
    a2 = (unsigned int)((a2) + (-8));
    v_r11 = (unsigned int)((v_r11) >> (8));
    a3 = (a3) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_007968E6;
loc_007968F8:
    if ((unsigned int)(a2) != 0) {
        a1 = *(unsigned __int8 *)(v_rip - 7741580 + a2 * 4);
        a1 = (unsigned __int8)((a1) & ((unsigned __int8)(v_r11)));
    }
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 8))) + ((unsigned int)(v_r10)));
    *(unsigned int *)(a4 + 8) = (unsigned int)(a1);
    goto loc_0079691D;
loc_00796911:
loc_0079691D:
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (7));
    a3 = ((unsigned int)((unsigned int)(a1))) >> (3);
    a3 = (a3) + (*(unsigned __int64 *)(a4));
    v_r11 = (unsigned int)((8) - ((unsigned int)(v_rdi)));
    a4 = (unsigned int)((a4) + (-5));
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) + (2));
    if (((unsigned int)(a4)) >= 3) goto loc_007969CB;
    if (((unsigned int)(result)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))) goto loc_0079695D;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))) - ((unsigned int)(a1)));
    if (condition_is_equal) goto loc_00796BB4;
loc_0079695D:
    result = (unsigned int)((unsigned int)(v_r10));
    if (((unsigned int)(v_r11)) < ((unsigned int)(v_r10))) { result = (unsigned int)(v_r11); }
    a2 = (unsigned __int8)((*(unsigned __int8 *)(v_rip - 7741767 + result * 4)) & ((unsigned __int8)(a4)));
    a2 = (unsigned __int8)((a2) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi)))));
    result = (unsigned int)((unsigned int)(v_r10));
    if (((unsigned int)(v_r11)) < ((unsigned int)(v_r10))) { result = (unsigned int)(v_r11); }
    a4 = (unsigned int)((a4) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_r11)))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) - ((unsigned int)(result)));
    a3 = (a3) + (1);
    if (((unsigned int)(a2)) < 8) goto loc_007969B5;
    result = ((unsigned int)((unsigned int)(a2))) >> (3);
loc_007969A3:
    *(unsigned __int8 *)(a3) = (unsigned __int8)(a4);
    a2 = (unsigned int)((a2) + (-8));
    a4 = (unsigned int)((a4) >> (8));
    a3 = (a3) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_007969A3;
loc_007969B5:
    if ((unsigned int)(a2) != 0) {
        a1 = *(unsigned __int8 *)(v_rip - 7741767 + a2 * 4);
        a1 = (unsigned __int8)((a1) & ((unsigned __int8)(a4)));
    }
    goto loc_00796BC0;
loc_007969CB:
    if (((unsigned int)(result)) <= ((unsigned int)(a2))) goto loc_007969D7;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(a2))) - ((unsigned int)(a1)));
    if (condition_is_equal) goto loc_00796A41;
loc_007969D7:
    result = (unsigned int)((unsigned int)(v_r10));
    if (((unsigned int)(v_r11)) < ((unsigned int)(v_r10))) { result = (unsigned int)(v_r11); }
    a2 = (unsigned __int8)((*(unsigned __int8 *)(v_rip - 7741693 + result * 4)) & (3));
    a2 = (unsigned __int8)((a2) << (1));
    result = (unsigned int)((unsigned int)(v_r10));
    if (((unsigned int)(v_r11)) < ((unsigned int)(v_r10))) { result = (unsigned int)(v_r11); }
    v_rdi = (unsigned int)((3) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_r11)))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) - ((unsigned int)(result)));
    a3 = (a3) + (v_rip - 7741767);
    if (((unsigned int)(a2)) < 8) goto loc_00796A27;
    result = ((unsigned int)((unsigned int)(a2))) >> (3);
loc_00796A16:
    *(unsigned __int8 *)(a3) = (unsigned __int8)(v_rdi);
    a2 = (unsigned int)((a2) + (-8));
    v_rdi = (unsigned int)((v_rdi) >> (8));
    a3 = (a3) + (v_rip - 7741767);
    result = (result) - (v_rip - 7741767);
    if (condition_is_not_equal) goto loc_00796A16;
loc_00796A27:
    if ((unsigned int)(a2) != 0) {
        a1 = *(unsigned __int8 *)(v_rip - 7741693 + a2 * 4);
        a1 = (unsigned __int8)((a1) & ((unsigned __int8)(v_rdi)));
    }
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 8))) + ((unsigned int)(v_r10)));
    *(unsigned int *)(a4 + 8) = (unsigned int)(a1);
loc_00796A41:
    a4 = (unsigned int)((a4) + (-3));
    if (((unsigned int)(a4)) < 7) goto loc_00796B28;
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)(a4))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12)))));
    v_r14 = (unsigned int)((v_r14) >> (1));
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12)))));
    v_r14 = (unsigned int)((v_r14) >> (2));
loc_00796A71:
    a3 = ((unsigned int)((unsigned int)(a1))) >> (3);
    a3 = (a3) + (*(unsigned __int64 *)(a4));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (7));
    v_rdi = (unsigned int)((3 + 5) - ((unsigned int)(v_rsi)));
    if (((unsigned int)(a1 + 3)) <= ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))))) goto loc_00796AA1;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))))))) - ((unsigned int)(a1)));
    if (condition_is_equal) goto loc_00796B13;
loc_00796AA1:
    result = (unsigned int)((unsigned int)(v_r10));
    if (((unsigned int)(v_rdi)) < ((unsigned int)(v_r10))) { result = (unsigned int)(v_rdi); }
    a2 = (unsigned __int8)((*(unsigned __int8 *)(v_rip - 7742014 + result * 4)) & (7));
    a2 = (unsigned __int8)((a2) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rsi)))));
    result = (unsigned int)((unsigned int)(v_r10));
    if (((unsigned int)(v_rdi)) < ((unsigned int)(v_r10))) { result = (unsigned int)(v_rdi); }
    v_r11 = (unsigned int)((7) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi)))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) - ((unsigned int)(result)));
    a3 = (a3) + (1);
    if (((unsigned int)(a2)) < 8) goto loc_00796AF7;
    result = ((unsigned int)((unsigned int)(a2))) >> (3);
loc_00796AE5:
    *(unsigned __int8 *)(a3) = (unsigned __int8)(v_r11);
    a2 = (unsigned int)((a2) + (-8));
    v_r11 = (unsigned int)((v_r11) >> (8));
    a3 = (a3) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00796AE5;
loc_00796AF7:
    if ((unsigned int)(a2) != 0) {
        a1 = *(unsigned __int8 *)(v_rip - 7742014 + a2 * 4);
        a1 = (unsigned __int8)((a1) & ((unsigned __int8)(v_r11)));
    }
loc_00796B13:
    a4 = (unsigned int)((a4) + (-7));
    v_r14 = (v_r14) - (1);
    if (condition_is_not_equal) goto loc_00796A71;
loc_00796B28:
    a3 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8))))))) >> (3);
    a3 = (a3) + (*(unsigned __int64 *)(a4));
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8))))))) & (7));
    v_r11 = (unsigned int)((3 + 5) - ((unsigned int)(v_rdi)));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8)))) + 3)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))) goto loc_00796B53;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 12))))) - ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 8)))))));
    if (condition_is_equal) goto loc_00796BB4;
loc_00796B53:
    result = (unsigned int)((unsigned int)(v_r10));
    if (((unsigned int)(v_r11)) < ((unsigned int)(v_r10))) { result = (unsigned int)(v_r11); }
    a2 = (unsigned __int8)((*(unsigned __int8 *)(v_rip - 7742269 + result * 4)) & ((unsigned __int8)(a4)));
    a2 = (unsigned __int8)((a2) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi)))));
    result = (unsigned int)((unsigned int)(v_r10));
    if (((unsigned int)(v_r11)) < ((unsigned int)(v_r10))) { result = (unsigned int)(v_r11); }
    a4 = (unsigned int)((a4) >> ((unsigned __int8)((unsigned int)((unsigned int)(v_r11)))));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) - ((unsigned int)(result)));
    a3 = (a3) + (1);
    if (((unsigned int)(a2)) < 8) goto loc_007969B5;
    result = ((unsigned int)((unsigned int)(a2))) >> (3);
loc_00796B9D:
    *(unsigned __int8 *)(a3) = (unsigned __int8)(a4);
    a2 = (unsigned int)((a2) + (-8));
    a4 = (unsigned int)((a4) >> (8));
    a3 = (a3) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00796B9D;
    goto loc_007969B5;
loc_00796BB4:
loc_00796BB9:
loc_00796BC0:
    if (((unsigned int)((unsigned __int16)(v_r15))) < ((unsigned int)((unsigned int)(v_stack_m178)))) goto loc_00796579;
loc_00796BCD:
    result = 0;
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (368);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Xp10BuildAndWriteHuffmanTables(int64_t Arg1, void *Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint32_t v_stack_m174;
    uint32_t v_stack_m178;
    uint64_t v_stack_m188;
    uint64_t v_stack_m48;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mF4;
    uint32_t v_stack_mF8;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (368);
    result = (*(uint64_t *)(v_rip + 0x6745A1)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m178 = Arg3;
    v_stack_m170 = Arg2;
    Arg2 = 0;
    result = memset(v_stack_m168, Arg2, 132, Arg4);
    Arg2 = 0;
    result = memset(v_stack_mD8, Arg2, 132, Arg4);
    result = 0;
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_007962C4;
loc_00796205:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x0 * 4))) & ((uint32_t)(132 - 124 + 23)));
    if (condition_is_equal) goto loc_0079624F;
    if (((uint32_t)(Arg1)) != ((uint32_t)((uint32_t)((uint32_t)(132 - 124))))) goto loc_00796220;
    goto loc_00796241;
loc_00796220:
    if (0 < 16) goto loc_0079623E;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x0 * 4 - 0x40))) & ((uint32_t)(132 - 124 + 23)));
    if (((uint32_t)(Arg1)) != ((uint32_t)(result))) goto loc_00796236;
    goto loc_0079623E;
loc_00796236:
    result = (uint32_t)((result) + 1);
    Arg3 = (uint32_t)((uint32_t)(132 - 124 + 23));
    if (((uint32_t)(Arg1)) == ((uint32_t)(result))) { Arg3 = (uint32_t)(132 - 124 + 24); }
loc_0079623E:
loc_00796241:
    Arg2 = (uint16_t)((0) + ((uint16_t)(132 - 124 - 7)));
    goto loc_007962B8;
loc_0079624F:
    goto loc_00796264;
loc_00796255:
    if ((((uint8_t)(132 - 124 + 23)) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + (uint16_t)(arg2) * 4))))) != 0) goto loc_0079626C;
    Arg2 = (uint16_t)((Arg2) + ((uint16_t)(132 - 124 - 7)));
loc_00796264:
    if (((uint32_t)((uint16_t)(Arg2))) < ((uint32_t)((uint32_t)(Arg3)))) goto loc_00796255;
loc_0079626C:
    result = (uint16_t)(((uint16_t)(Arg2)) ^ ((uint16_t)((uint16_t)(Arg2))));
    if (((uint16_t)(result)) < 16) goto loc_0079629E;
loc_0079627F:
    Arg3 = (uint16_t)(((uint16_t)(Arg2)) & ((uint16_t)((uint32_t)(0xFFF0ULL))));
    Arg3 = (uint16_t)((Arg3) + (16));
    result = (uint16_t)(((uint16_t)(Arg2)) ^ ((uint16_t)(Arg3)));
    if (((uint16_t)(result)) >= 16) goto loc_0079627F;
loc_0079629E:
    Arg1 = (uint32_t)(((uint16_t)(Arg2)) - ((uint32_t)((uint16_t)(Arg3))));
    if (condition_is_equal) goto loc_007962B8;
    if (((uint32_t)(Arg1)) >= 5) goto loc_007962B4;
    goto loc_007962B8;
loc_007962B4:
loc_007962B8:
    if (((uint32_t)((uint16_t)(Arg2))) < ((uint32_t)((uint32_t)(Arg3)))) goto loc_00796205;
loc_007962C4:
    v_stack_m188 = v_stack_mD8;
    result = Xp10BuildHuffmanEncodings(Arg1, v_stack_m168, 33, (uint32_t)((uint32_t)(132 - 124)));
    local_r13 = 0;
loc_007962F9:
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mD8))) & (31));
    if (((uint32_t)(local_rdi)) != ((uint32_t)(33 - 29))) goto loc_00796386;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8))))) >> (3);
    Arg2 = (Arg2) + (*(uint64_t *)(arg4));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8))))) & (7));
    Arg4 = (uint32_t)((1 + 7) - ((uint32_t)(result)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8)) + 1)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC))))) goto loc_0079633F;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC))))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8)))));
    if (condition_is_equal) goto loc_0079654F;
loc_0079633F:
    result = (uint32_t)(Arg3);
    if (((uint32_t)(Arg4)) < Arg3) { result = (uint32_t)(Arg4); }
    Arg2 = (Arg2) + (1);
    Arg1 = (uint32_t)(((uint32_t)(Arg3)) - ((uint32_t)(result)));
    if (((uint32_t)(Arg1)) < 8) goto loc_00796371;
    result = ((uint32_t)((uint32_t)(Arg1))) >> (3);
loc_0079635F:
    *(uint8_t *)(arg2) = 0;
    Arg1 = (uint32_t)((Arg1) + (-8));
    Arg4 = (uint32_t)((0) >> (8));
    Arg2 = (Arg2) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_0079635F;
loc_00796371:
    if ((uint32_t)(Arg1) != 0) {
        Arg1 = *(uint8_t *)(v_rip - 0x761AD9 + Arg1 * 4);
        Arg1 = (uint8_t)((Arg1) & ((uint8_t)(Arg4)));
    }
    goto loc_0079654F;
loc_00796386:
    Arg3 = (Arg1) >> (3);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (7));
    Arg3 = (Arg3) + (result);
    local_r11 = (uint32_t)((1 + 7) - ((uint32_t)(local_rsi)));
    if (((uint32_t)(Arg1 + 1)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC))))) goto loc_007963B2;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC))))) - ((uint32_t)(Arg1)));
    if (condition_is_equal) goto loc_0079642A;
loc_007963B2:
    result = (uint32_t)((uint32_t)(Arg4));
    if (((uint32_t)(local_r11)) < ((uint32_t)(Arg4))) { result = (uint32_t)(local_r11); }
    Arg2 = (uint8_t)((*(uint8_t *)(v_rip - 0x761B9C + result * 4)) & (1));
    Arg2 = (uint8_t)((Arg2) << ((uint8_t)((uint32_t)((uint32_t)(local_rsi)))));
    result = (uint32_t)((uint32_t)(Arg4));
    if (((uint32_t)(local_r11)) < ((uint32_t)(Arg4))) { result = (uint32_t)(local_r11); }
    local_r10 = (uint32_t)((1) >> ((uint8_t)((uint32_t)((uint32_t)(local_r11)))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) - ((uint32_t)(result)));
    Arg3 = (Arg3) + (1);
    if (((uint32_t)(Arg2)) < 8) goto loc_0079640D;
    result = ((uint32_t)((uint32_t)(Arg2))) >> (3);
loc_007963FB:
    *(uint8_t *)(Arg3) = (uint8_t)(local_r10);
    Arg2 = (uint32_t)((Arg2) + (-8));
    local_r10 = (uint32_t)((local_r10) >> (8));
    Arg3 = (Arg3) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_007963FB;
loc_0079640D:
    if ((uint32_t)(Arg2) != 0) {
        Arg1 = v_rip - 7740408;
        Arg1 = *(uint8_t *)(Arg1 + arg2 * 4);
        Arg1 = (uint8_t)((Arg1) & ((uint8_t)(local_r10)));
    }
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4 + 0x8))) + ((uint32_t)(Arg4)));
    *(uint32_t *)(arg4 + 0x8) = (uint32_t)(Arg1);
loc_0079642A:
    Arg3 = ((uint32_t)((uint32_t)(Arg1))) >> (3);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (7));
    Arg3 = (Arg3) + (*(uint64_t *)(arg4));
    local_r10 = (uint32_t)((8) - ((uint32_t)(local_rsi)));
    if (1 <= ((uint32_t)(33 - 29))) goto loc_007964C6;
    if (((uint32_t)(Arg1 + 3)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC))))) goto loc_00796467;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC))))) - ((uint32_t)(Arg1)));
    if (condition_is_equal) goto loc_00796540;
loc_00796467:
    result = (uint32_t)((uint32_t)(Arg4));
    if (((uint32_t)(local_r10)) < ((uint32_t)(Arg4))) { result = (uint32_t)(local_r10); }
    Arg2 = (uint8_t)((*(uint8_t *)(v_rip - 0x761C51 + result * 4)) & ((uint8_t)(1 - 1)));
    Arg2 = (uint8_t)((Arg2) << ((uint8_t)((uint32_t)((uint32_t)(local_rsi)))));
    result = (uint32_t)((uint32_t)(Arg4));
    if (((uint32_t)(local_r10)) < ((uint32_t)(Arg4))) { result = (uint32_t)(local_r10); }
    local_r11 = (uint32_t)((1 - 1) >> ((uint8_t)((uint32_t)((uint32_t)(local_r10)))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) - ((uint32_t)(result)));
    Arg3 = (Arg3) + (1);
    if (((uint32_t)(Arg2)) < 8) goto loc_0079652E;
    result = ((uint32_t)((uint32_t)(Arg2))) >> (3);
loc_007964B2:
    *(uint8_t *)(Arg3) = (uint8_t)(local_r11);
    Arg2 = (uint32_t)((Arg2) + (-8));
    local_r11 = (uint32_t)((local_r11) >> (8));
    Arg3 = (Arg3) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_007964B2;
    goto loc_0079652E;
loc_007964C6:
    if (((uint32_t)(Arg2)) <= ((uint32_t)(result))) goto loc_007964D2;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(result))) - (1));
    if (condition_is_equal) goto loc_00796540;
loc_007964D2:
    result = (uint32_t)((uint32_t)(Arg4));
    if (((uint32_t)(local_r10)) < ((uint32_t)(Arg4))) { result = (uint32_t)(local_r10); }
    Arg2 = (uint8_t)((*(uint8_t *)(v_rip - 0x761CBC + result * 4)) & (1));
    Arg2 = (uint8_t)((Arg2) << ((uint8_t)((uint32_t)((uint32_t)(local_rsi)))));
    result = (uint32_t)((uint32_t)(Arg4));
    if (((uint32_t)(local_r10)) < ((uint32_t)(Arg4))) { result = (uint32_t)(local_r10); }
    local_r11 = (uint32_t)((1) >> ((uint8_t)((uint32_t)((uint32_t)(local_r10)))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) - ((uint32_t)(result)));
    Arg3 = (Arg3) + (1);
    if (((uint32_t)(Arg2)) < 8) goto loc_0079652E;
    result = ((uint32_t)((uint32_t)(Arg2))) >> (3);
loc_0079651C:
    *(uint8_t *)(Arg3) = (uint8_t)(local_r11);
    Arg2 = (uint32_t)((Arg2) + (-8));
    local_r11 = (uint32_t)((local_r11) >> (8));
    Arg3 = (Arg3) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_0079651C;
loc_0079652E:
    if ((uint32_t)(Arg2) != 0) {
        Arg1 = *(uint8_t *)(v_rip - 0x761CBC + arg2 * 4);
        Arg1 = (uint8_t)((Arg1) & ((uint8_t)(local_r11)));
    }
loc_00796540:
loc_0079654F:
    local_r15 = (v_stack_mD8) + (4);
    local_r12 = (33) - (1);
    if (condition_is_not_equal) goto loc_007962F9;
    v_stack_m174 = 8;
    if ((uint32_t)((uint32_t)(v_stack_m178)) == 0) goto loc_00796BCD;
loc_00796579:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x0 * 4))) & (31));
    if (condition_is_equal) goto loc_0079667A;
    if (((uint32_t)(Arg1)) != 8) goto loc_0079659D;
    goto loc_007965CA;
loc_0079659D:
    if (0 < 16) goto loc_007965C3;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m170 + 0x0 * 4 - 0x40))) & (31));
    if (((uint32_t)(Arg1)) != ((uint32_t)(result))) goto loc_007965B7;
    goto loc_007965C3;
loc_007965B7:
    result = (uint32_t)((result) + 1);
    Arg2 = 31;
    if (((uint32_t)(Arg1)) == ((uint32_t)(result))) { Arg2 = 32; }
loc_007965C3:
    v_stack_m174 = (uint32_t)(Arg1);
loc_007965CA:
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8))))) >> (3);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8))))) & (7));
    local_r11 = (uint32_t)((8) - ((uint32_t)(Arg1)));
    Arg3 = (Arg3) + (*(uint64_t *)(arg4));
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mA8 + (uint32_t)((uint32_t)(arg2)) * 4 - 0x30))))) & (31));
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mA8 + (uint32_t)((uint32_t)(arg2)) * 4 - 0x30))) >> (5));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8)) + Arg4 * 1)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC))))) goto loc_0079660A;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC))))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8)))));
    if (condition_is_equal) goto loc_0079666C;
loc_0079660A:
    result = (uint32_t)((uint32_t)(Arg4));
    if (((uint32_t)(local_r11)) < ((uint32_t)(Arg4))) { result = (uint32_t)(local_r11); }
    Arg2 = (uint8_t)((*(uint8_t *)(v_rip - 0x761D2A + result * 4)) & ((uint8_t)(local_r10)));
    Arg2 = (uint8_t)((Arg2) << ((uint8_t)(Arg1)));
    result = (uint32_t)((uint32_t)(Arg4));
    if (((uint32_t)(local_r11)) < ((uint32_t)(Arg4))) { result = (uint32_t)(local_r11); }
    local_r10 = (uint32_t)((local_r10) >> ((uint8_t)((uint32_t)((uint32_t)(local_r11)))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) - ((uint32_t)(result)));
    Arg3 = (Arg3) + (1);
    if (((uint32_t)(Arg2)) < 8) goto loc_00796659;
    result = ((uint32_t)((uint32_t)(Arg2))) >> (3);
loc_00796647:
    *(uint8_t *)(Arg3) = (uint8_t)(local_r10);
    Arg2 = (uint32_t)((Arg2) + (-8));
    local_r10 = (uint32_t)((local_r10) >> (8));
    Arg3 = (Arg3) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00796647;
loc_00796659:
    if ((uint32_t)(Arg2) != 0) {
        Arg1 = *(uint8_t *)(v_rip - 0x761D2A + arg2 * 4);
        Arg1 = (uint8_t)((Arg1) & ((uint8_t)(local_r10)));
    }
    goto loc_00796671;
loc_0079666C:
loc_00796671:
    local_r15 = (uint16_t)((0) + (1));
    goto loc_00796BC0;
loc_0079667A:
    goto loc_00796691;
loc_00796680:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg3 + (uint16_t)(local_r15) * 4)))) & (31)) != 0) goto loc_0079669A;
    local_r15 = (uint16_t)((local_r15) + (1));
loc_00796691:
    if (((uint32_t)((uint16_t)(local_r15))) < ((uint32_t)((uint32_t)(v_stack_m178)))) goto loc_00796680;
loc_0079669A:
    result = (uint16_t)(((uint16_t)(local_r15)) ^ ((uint16_t)((uint16_t)(local_r15))));
    if (((uint16_t)(result)) < 16) goto loc_00796787;
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m68)) & (31));
    local_r14 = (uint32_t)(((uint32_t)(v_stack_m68)) >> (5));
loc_007966C7:
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8))))) >> (3);
    Arg3 = (Arg3) + (*(uint64_t *)(arg4));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8))))) & (7));
    local_rdi = (uint32_t)((8) - ((uint32_t)(Arg1)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8)) + local_rsi * 1)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC))))) goto loc_007966F7;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC))))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8)))));
    if (condition_is_equal) goto loc_0079675D;
loc_007966F7:
    result = (uint32_t)((uint32_t)(Arg4));
    if (((uint32_t)(local_rdi)) < ((uint32_t)(Arg4))) { result = (uint32_t)(local_rdi); }
    Arg2 = (uint8_t)((*(uint8_t *)(v_rip - 0x761E96 + result * 4)) & ((uint8_t)(local_r14)));
    Arg2 = (uint8_t)((Arg2) << ((uint8_t)(Arg1)));
    result = (uint32_t)((uint32_t)(Arg4));
    if (((uint32_t)(local_rdi)) < ((uint32_t)(Arg4))) { result = (uint32_t)(local_rdi); }
    Arg3 = (Arg3) + (1);
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) >> ((uint8_t)((uint32_t)((uint32_t)(local_rdi)))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) - ((uint32_t)(result)));
    if (((uint32_t)(Arg2)) < 8) goto loc_00796748;
    result = ((uint32_t)((uint32_t)(Arg2))) >> (3);
loc_00796736:
    *(uint8_t *)(Arg3) = (uint8_t)(local_r11);
    Arg2 = (uint32_t)((Arg2) + (-8));
    local_r11 = (uint32_t)((local_r11) >> (8));
    Arg3 = (Arg3) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00796736;
loc_00796748:
    if ((uint32_t)(Arg2) != 0) {
        Arg1 = *(uint8_t *)(v_rip - 0x761E96 + arg2 * 4);
        Arg1 = (uint8_t)((Arg1) & ((uint8_t)(local_r11)));
    }
    goto loc_00796762;
loc_0079675D:
loc_00796762:
    local_r10 = (uint16_t)(((uint16_t)(local_r15)) & ((uint16_t)((uint32_t)(0xFFF0ULL))));
    local_r10 = (uint16_t)((local_r10) + (16));
    result = (uint16_t)(((uint16_t)(local_r15)) ^ ((uint16_t)(local_r10)));
    if (((uint16_t)(result)) >= 16) goto loc_007966C7;
loc_00796787:
    Arg4 = (uint32_t)(((uint16_t)(local_r15)) - ((uint32_t)((uint16_t)(local_r10))));
    if (condition_is_equal) goto loc_00796BB9;
    if (((uint32_t)(Arg4)) >= 5) goto loc_00796866;
    local_rsi = (uint32_t)(((uint32_t)(v_stack_mD8)) & (31));
    local_r14 = (uint32_t)(((uint32_t)(v_stack_mD8)) >> (5));
loc_007967B7:
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8))))) >> (3);
    Arg3 = (Arg3) + (*(uint64_t *)(arg4));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8))))) & (7));
    local_rdi = (uint32_t)((8) - ((uint32_t)(Arg1)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8)) + local_rsi * 1)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC))))) goto loc_007967E7;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC))))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8)))));
    if (condition_is_equal) goto loc_0079684D;
loc_007967E7:
    result = (uint32_t)((uint32_t)(local_r10));
    if (((uint32_t)(local_rdi)) < ((uint32_t)(local_r10))) { result = (uint32_t)(local_rdi); }
    Arg2 = (uint8_t)((*(uint8_t *)(v_rip - 0x761F8C + result * 4)) & ((uint8_t)(local_r14)));
    Arg2 = (uint8_t)((Arg2) << ((uint8_t)(Arg1)));
    result = (uint32_t)((uint32_t)(local_r10));
    if (((uint32_t)(local_rdi)) < ((uint32_t)(local_r10))) { result = (uint32_t)(local_rdi); }
    Arg3 = (Arg3) + (1);
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) >> ((uint8_t)((uint32_t)((uint32_t)(local_rdi)))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) - ((uint32_t)(result)));
    if (((uint32_t)(Arg2)) < 8) goto loc_00796838;
    result = ((uint32_t)((uint32_t)(Arg2))) >> (3);
loc_00796826:
    *(uint8_t *)(Arg3) = (uint8_t)(local_r11);
    Arg2 = (uint32_t)((Arg2) + (-8));
    local_r11 = (uint32_t)((local_r11) >> (8));
    Arg3 = (Arg3) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00796826;
loc_00796838:
    if ((uint32_t)(Arg2) != 0) {
        Arg1 = *(uint8_t *)(v_rip - 0x761F8C + arg2 * 4);
        Arg1 = (uint8_t)((Arg1) & ((uint8_t)(local_r11)));
    }
    goto loc_00796852;
loc_0079684D:
loc_00796852:
    Arg4 = (uint32_t)((Arg4) + (-1));
    if (condition_is_not_equal) goto loc_007967B7;
    goto loc_00796BB9;
loc_00796866:
    local_r10 = (uint32_t)(((uint32_t)(v_stack_m64)) & (31));
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8))))) >> (3);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8))))) & (7));
    Arg3 = (Arg3) + (*(uint64_t *)(arg4));
    local_rdi = (uint32_t)((8) - ((uint32_t)(local_rsi)));
    local_r11 = (uint32_t)(((uint32_t)(v_stack_m64)) >> (5));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8)) + local_r10 * 1)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC))))) goto loc_007968A2;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC))))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8)))));
    if (condition_is_equal) goto loc_00796911;
loc_007968A2:
    result = (uint32_t)((uint32_t)(local_r10));
    if (((uint32_t)(local_rdi)) < ((uint32_t)(local_r10))) { result = (uint32_t)(local_rdi); }
    Arg2 = (uint8_t)((*(uint8_t *)(v_rip - 0x76208C + result * 4)) & ((uint8_t)(local_r11)));
    Arg2 = (uint8_t)((Arg2) << ((uint8_t)((uint32_t)((uint32_t)(local_rsi)))));
    result = (uint32_t)((uint32_t)(local_r10));
    if (((uint32_t)(local_rdi)) < ((uint32_t)(local_r10))) { result = (uint32_t)(local_rdi); }
    local_r11 = (uint32_t)((local_r11) >> ((uint8_t)((uint32_t)((uint32_t)(local_rdi)))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) - ((uint32_t)(result)));
    Arg3 = (Arg3) + (1);
    if (((uint32_t)(Arg2)) < 8) goto loc_007968F8;
    result = ((uint32_t)((uint32_t)(Arg2))) >> (3);
loc_007968E6:
    *(uint8_t *)(Arg3) = (uint8_t)(local_r11);
    Arg2 = (uint32_t)((Arg2) + (-8));
    local_r11 = (uint32_t)((local_r11) >> (8));
    Arg3 = (Arg3) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_007968E6;
loc_007968F8:
    if ((uint32_t)(Arg2) != 0) {
        Arg1 = *(uint8_t *)(v_rip - 0x76208C + arg2 * 4);
        Arg1 = (uint8_t)((Arg1) & ((uint8_t)(local_r11)));
    }
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4 + 0x8))) + ((uint32_t)(local_r10)));
    *(uint32_t *)(arg4 + 0x8) = (uint32_t)(Arg1);
    goto loc_0079691D;
loc_00796911:
loc_0079691D:
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (7));
    Arg3 = ((uint32_t)((uint32_t)(Arg1))) >> (3);
    Arg3 = (Arg3) + (*(uint64_t *)(arg4));
    local_r11 = (uint32_t)((8) - ((uint32_t)(local_rdi)));
    Arg4 = (uint32_t)((Arg4) + (-5));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) + (2));
    if (((uint32_t)(Arg4)) >= 3) goto loc_007969CB;
    if (((uint32_t)(result)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC))))) goto loc_0079695D;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC))))) - ((uint32_t)(Arg1)));
    if (condition_is_equal) goto loc_00796BB4;
loc_0079695D:
    result = (uint32_t)((uint32_t)(local_r10));
    if (((uint32_t)(local_r11)) < ((uint32_t)(local_r10))) { result = (uint32_t)(local_r11); }
    Arg2 = (uint8_t)((*(uint8_t *)(v_rip - 0x762147 + result * 4)) & ((uint8_t)(Arg4)));
    Arg2 = (uint8_t)((Arg2) << ((uint8_t)((uint32_t)((uint32_t)(local_rdi)))));
    result = (uint32_t)((uint32_t)(local_r10));
    if (((uint32_t)(local_r11)) < ((uint32_t)(local_r10))) { result = (uint32_t)(local_r11); }
    Arg4 = (uint32_t)((Arg4) >> ((uint8_t)((uint32_t)((uint32_t)(local_r11)))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) - ((uint32_t)(result)));
    Arg3 = (Arg3) + (1);
    if (((uint32_t)(Arg2)) < 8) goto loc_007969B5;
    result = ((uint32_t)((uint32_t)(Arg2))) >> (3);
loc_007969A3:
    *(uint8_t *)(Arg3) = (uint8_t)(Arg4);
    Arg2 = (uint32_t)((Arg2) + (-8));
    Arg4 = (uint32_t)((Arg4) >> (8));
    Arg3 = (Arg3) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_007969A3;
loc_007969B5:
    if ((uint32_t)(Arg2) != 0) {
        Arg1 = *(uint8_t *)(v_rip - 0x762147 + arg2 * 4);
        Arg1 = (uint8_t)((Arg1) & ((uint8_t)(Arg4)));
    }
    goto loc_00796BC0;
loc_007969CB:
    if (((uint32_t)(result)) <= ((uint32_t)(Arg2))) goto loc_007969D7;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) - ((uint32_t)(Arg1)));
    if (condition_is_equal) goto loc_00796A41;
loc_007969D7:
    result = (uint32_t)((uint32_t)(local_r10));
    if (((uint32_t)(local_r11)) < ((uint32_t)(local_r10))) { result = (uint32_t)(local_r11); }
    Arg2 = (uint8_t)((*(uint8_t *)(v_rip - 0x7620FD + result * 4)) & (3));
    Arg2 = (uint8_t)((Arg2) << (1));
    result = (uint32_t)((uint32_t)(local_r10));
    if (((uint32_t)(local_r11)) < ((uint32_t)(local_r10))) { result = (uint32_t)(local_r11); }
    local_rdi = (uint32_t)((3) >> ((uint8_t)((uint32_t)((uint32_t)(local_r11)))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) - ((uint32_t)(result)));
    Arg3 = (Arg3) + (v_rip - 7741767);
    if (((uint32_t)(Arg2)) < 8) goto loc_00796A27;
    result = ((uint32_t)((uint32_t)(Arg2))) >> (3);
loc_00796A16:
    *(uint8_t *)(Arg3) = (uint8_t)(local_rdi);
    Arg2 = (uint32_t)((Arg2) + (-8));
    local_rdi = (uint32_t)((local_rdi) >> (8));
    Arg3 = (Arg3) + (v_rip - 7741767);
    result = (result) - (v_rip - 7741767);
    if (condition_is_not_equal) goto loc_00796A16;
loc_00796A27:
    if ((uint32_t)(Arg2) != 0) {
        Arg1 = *(uint8_t *)(v_rip - 0x7620FD + arg2 * 4);
        Arg1 = (uint8_t)((Arg1) & ((uint8_t)(local_rdi)));
    }
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4 + 0x8))) + ((uint32_t)(local_r10)));
    *(uint32_t *)(arg4 + 0x8) = (uint32_t)(Arg1);
loc_00796A41:
    Arg4 = (uint32_t)((Arg4) + (-3));
    if (((uint32_t)(Arg4)) < 7) goto loc_00796B28;
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC)))));
    local_r14 = (uint32_t)((local_r14) >> (1));
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC)))));
    local_r14 = (uint32_t)((local_r14) >> (2));
loc_00796A71:
    Arg3 = ((uint32_t)((uint32_t)(Arg1))) >> (3);
    Arg3 = (Arg3) + (*(uint64_t *)(arg4));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (7));
    local_rdi = (uint32_t)((3 + 5) - ((uint32_t)(local_rsi)));
    if (((uint32_t)(Arg1 + 3)) <= ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC))))))) goto loc_00796AA1;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC))))))))) - ((uint32_t)(Arg1)));
    if (condition_is_equal) goto loc_00796B13;
loc_00796AA1:
    result = (uint32_t)((uint32_t)(local_r10));
    if (((uint32_t)(local_rdi)) < ((uint32_t)(local_r10))) { result = (uint32_t)(local_rdi); }
    Arg2 = (uint8_t)((*(uint8_t *)(v_rip - 0x76223E + result * 4)) & (7));
    Arg2 = (uint8_t)((Arg2) << ((uint8_t)((uint32_t)((uint32_t)(local_rsi)))));
    result = (uint32_t)((uint32_t)(local_r10));
    if (((uint32_t)(local_rdi)) < ((uint32_t)(local_r10))) { result = (uint32_t)(local_rdi); }
    local_r11 = (uint32_t)((7) >> ((uint8_t)((uint32_t)((uint32_t)(local_rdi)))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) - ((uint32_t)(result)));
    Arg3 = (Arg3) + (1);
    if (((uint32_t)(Arg2)) < 8) goto loc_00796AF7;
    result = ((uint32_t)((uint32_t)(Arg2))) >> (3);
loc_00796AE5:
    *(uint8_t *)(Arg3) = (uint8_t)(local_r11);
    Arg2 = (uint32_t)((Arg2) + (-8));
    local_r11 = (uint32_t)((local_r11) >> (8));
    Arg3 = (Arg3) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00796AE5;
loc_00796AF7:
    if ((uint32_t)(Arg2) != 0) {
        Arg1 = *(uint8_t *)(v_rip - 0x76223E + arg2 * 4);
        Arg1 = (uint8_t)((Arg1) & ((uint8_t)(local_r11)));
    }
loc_00796B13:
    Arg4 = (uint32_t)((Arg4) + (-7));
    local_r14 = (local_r14) - (1);
    if (condition_is_not_equal) goto loc_00796A71;
loc_00796B28:
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8))))))) >> (3);
    Arg3 = (Arg3) + (*(uint64_t *)(arg4));
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8))))))) & (7));
    local_r11 = (uint32_t)((3 + 5) - ((uint32_t)(local_rdi)));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8)))) + 3)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC))))) goto loc_00796B53;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0xC))))) - ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x8)))))));
    if (condition_is_equal) goto loc_00796BB4;
loc_00796B53:
    result = (uint32_t)((uint32_t)(local_r10));
    if (((uint32_t)(local_r11)) < ((uint32_t)(local_r10))) { result = (uint32_t)(local_r11); }
    Arg2 = (uint8_t)((*(uint8_t *)(v_rip - 0x76233D + result * 4)) & ((uint8_t)(Arg4)));
    Arg2 = (uint8_t)((Arg2) << ((uint8_t)((uint32_t)((uint32_t)(local_rdi)))));
    result = (uint32_t)((uint32_t)(local_r10));
    if (((uint32_t)(local_r11)) < ((uint32_t)(local_r10))) { result = (uint32_t)(local_r11); }
    Arg4 = (uint32_t)((Arg4) >> ((uint8_t)((uint32_t)((uint32_t)(local_r11)))));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) - ((uint32_t)(result)));
    Arg3 = (Arg3) + (1);
    if (((uint32_t)(Arg2)) < 8) goto loc_007969B5;
    result = ((uint32_t)((uint32_t)(Arg2))) >> (3);
loc_00796B9D:
    *(uint8_t *)(Arg3) = (uint8_t)(Arg4);
    Arg2 = (uint32_t)((Arg2) + (-8));
    Arg4 = (uint32_t)((Arg4) >> (8));
    Arg3 = (Arg3) + (1);
    result = (result) - (1);
    if (condition_is_not_equal) goto loc_00796B9D;
    goto loc_007969B5;
loc_00796BB4:
loc_00796BB9:
loc_00796BC0:
    if (((uint32_t)((uint16_t)(local_r15))) < ((uint32_t)((uint32_t)(v_stack_m178)))) goto loc_00796579;
loc_00796BCD:
    result = 0;
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (368);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `- 0x40 + rax*4` | `32` | `R` |
| `Arg2` | `+ 0x0 + rax*4` | `32` | `R` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x8` | `32` | `R` |
| `Arg4` | `+ 0x8` | `32` | `R/W` |
| `Arg4` | `+ 0x8` | `32` | `W` |
| `Arg4` | `+ 0xC` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0079617C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
