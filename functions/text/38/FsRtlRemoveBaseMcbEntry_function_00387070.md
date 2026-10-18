# FsRtlRemoveBaseMcbEntry

- RVA: `0x00387070`–`0x0038753D` (길이 `1,229` bytes)
- VA: `0x0000000140387070`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007FD1C`
- 디코드: `328`개 명령, `1,229/1,229` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003871A1` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00387254` → [FsRtlAddEntry](FsRtlAddEntry_function_00387BE0.md) (function, `0x00387BE0`)
- `0x003872F8` → [FsRtlRemoveLargeEntry](FsRtlRemoveLargeEntry_function_00387EA0.md) (function, `0x00387EA0`)
- `0x0038732D` → [FsRtlAddEntry](FsRtlAddEntry_function_00387BE0.md) (function, `0x00387BE0`)
- `0x00387471` → [FsRtlAddEntry](FsRtlAddEntry_function_00387BE0.md) (function, `0x00387BE0`)

### Direct callers
- [FsRtlRemoveLargeMcbEntry](FsRtlRemoveLargeMcbEntry_function_00386C40.md) at `0x00386C6F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00387532` → [sub_006E4E46](../6E/Unknown_function_006E4E46.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00387070  48 8B C4                        mov rax, rsp
00387073  48 89 58 08                     mov qword ptr [rax + 8], rbx
00387077  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0038707B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0038707F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00387083  41 55                           push r13
00387085  41 56                           push r14
00387087  41 57                           push r15
00387089  48 83 EC 20                     sub rsp, 0x20
0038708D  49 8B E8                        mov rbp, r8
00387090  48 8B F2                        mov rsi, rdx
00387093  48 8B F9                        mov rdi, rcx
00387096  48 85 D2                        test rdx, rdx
00387099  0F 84 10 01 00 00               je 0x1403871af
0038709F  41 83 CD FF                     or r13d, 0xffffffff
003870A3  41 BB 02 00 00 00               mov r11d, 2
003870A9  48 85 ED                        test rbp, rbp
003870AC  0F 8E 1F 01 00 00               jle 0x1403871d1
003870B2  44 8B 57 04                     mov r10d, dword ptr [rdi + 4]
003870B6  45 33 C0                        xor r8d, r8d
003870B9  45 8D 72 FF                     lea r14d, [r10 - 1]
003870BD  45 8B CE                        mov r9d, r14d
003870C0  45 3B C1                        cmp r8d, r9d
003870C3  0F 8F 08 01 00 00               jg 0x1403871d1
003870C9  43 8D 04 01                     lea eax, [r9 + r8]
003870CD  99                              cdq
003870CE  41 F7 FB                        idiv r11d
003870D1  8B D8                           mov ebx, eax
003870D3  85 C0                           test eax, eax
003870D5  74 2C                           je 0x140387103
003870D7  8D 50 FF                        lea edx, [rax - 1]
003870DA  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
003870DE  48 63 CA                        movsxd rcx, edx
003870E1  8B 04 C8                        mov eax, dword ptr [rax + rcx*8]
003870E4  3B F0                           cmp esi, eax
003870E6  72 16                           jb 0x1403870fe
003870E8  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
003870EC  48 63 C3                        movsxd rax, ebx
003870EF  8B 0C C2                        mov ecx, dword ptr [rdx + rax*8]
003870F2  FF C9                           dec ecx
003870F4  3B F1                           cmp esi, ecx
003870F6  76 12                           jbe 0x14038710a
003870F8  44 8D 43 01                     lea r8d, [rbx + 1]
003870FC  EB C2                           jmp 0x1403870c0
003870FE  44 8B CA                        mov r9d, edx
00387101  EB BD                           jmp 0x1403870c0
00387103  33 C0                           xor eax, eax
00387105  83 CA FF                        or edx, 0xffffffff
00387108  EB DA                           jmp 0x1403870e4
0038710A  44 8D 43 FF                     lea r8d, [rbx - 1]
0038710E  85 DB                           test ebx, ebx
00387110  0F 84 A6 02 00 00               je 0x1403873bc
00387116  42 8B 04 C2                     mov eax, dword ptr [rdx + r8*8]
0038711A  48 3B C6                        cmp rax, rsi
0038711D  0F 85 D6 00 00 00               jne 0x1403871f9
00387123  44 8B 1C DA                     mov r11d, dword ptr [rdx + rbx*8]
00387127  48 8D 04 2E                     lea rax, [rsi + rbp]
0038712B  41 8D 4B FF                     lea ecx, [r11 - 1]
0038712F  48 3B C8                        cmp rcx, rax
00387132  0F 8D BB 00 00 00               jge 0x1403871f3
00387138  45 8B C8                        mov r9d, r8d
0038713B  85 DB                           test ebx, ebx
0038713D  0F 84 09 03 00 00               je 0x14038744c
00387143  42 8B 04 C2                     mov eax, dword ptr [rdx + r8*8]
00387147  44 2B D8                        sub r11d, eax
0038714A  41 8B C3                        mov eax, r11d
0038714D  41 BB 02 00 00 00               mov r11d, 2
00387153  48 03 F0                        add rsi, rax
00387156  48 2B E8                        sub rbp, rax
00387159  44 39 6C DA 04                  cmp dword ptr [rdx + rbx*8 + 4], r13d
0038715E  0F 84 45 FF FF FF               je 0x1403870a9
00387164  41 3B DE                        cmp ebx, r14d
00387167  0F 85 1C 01 00 00               jne 0x140387289
0038716D  85 DB                           test ebx, ebx
0038716F  0F 84 65 02 00 00               je 0x1403873da
00387175  4E 8D 1C CA                     lea r11, [rdx + r9*8]
00387179  45 8B 4B 04                     mov r9d, dword ptr [r11 + 4]
0038717D  45 3B CD                        cmp r9d, r13d
00387180  0F 85 3D 02 00 00               jne 0x1403873c3
00387186  41 8D 40 02                     lea eax, [r8 + 2]
0038718A  41 3B C2                        cmp eax, r10d
0038718D  73 17                           jae 0x1403871a6
0038718F  45 2B D0                        sub r10d, r8d
00387192  48 8D 14 C2                     lea rdx, [rdx + rax*8]
00387196  49 8B CB                        mov rcx, r11
00387199  45 8D 42 FE                     lea r8d, [r10 - 2]
0038719D  49 C1 E0 03                     shl r8, 3
003871A1  E8 9A F6 33 00                  call 0x1406c6840
003871A6  83 47 04 FE                     add dword ptr [rdi + 4], -2
003871AA  E9 F4 FE FF FF                  jmp 0x1403870a3
003871AF  8B 41 04                        mov eax, dword ptr [rcx + 4]
003871B2  85 C0                           test eax, eax
003871B4  0F 84 E5 FE FF FF               je 0x14038709f
003871BA  8D 48 FF                        lea ecx, [rax - 1]
003871BD  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
003871C1  8B 0C C8                        mov ecx, dword ptr [rax + rcx*8]
003871C4  4C 3B C1                        cmp r8, rcx
003871C7  0F 8C D2 FE FF FF               jl 0x14038709f
003871CD  83 67 04 00                     and dword ptr [rdi + 4], 0
003871D1  B0 01                           mov al, 1
003871D3  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
003871D8  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
003871DD  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
003871E2  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
003871E7  48 83 C4 20                     add rsp, 0x20
003871EB  41 5F                           pop r15
003871ED  41 5E                           pop r14
003871EF  41 5D                           pop r13
003871F1  C3                              ret
003871F2  CC                              int3
003871F3  41 BB 02 00 00 00               mov r11d, 2
003871F9  85 DB                           test ebx, ebx
003871FB  0F 84 52 02 00 00               je 0x140387453
00387201  42 8B 04 C2                     mov eax, dword ptr [rdx + r8*8]
00387205  4C 8B F3                        mov r14, rbx
00387208  48 3B C6                        cmp rax, rsi
0038720B  0F 85 F1 00 00 00               jne 0x140387302
00387211  44 39 6C DA 04                  cmp dword ptr [rdx + rbx*8 + 4], r13d
00387216  74 67                           je 0x14038727f
00387218  85 DB                           test ebx, ebx
0038721A  74 2D                           je 0x140387249
0038721C  8D 43 FF                        lea eax, [rbx - 1]
0038721F  44 8B 4C C2 04                  mov r9d, dword ptr [rdx + rax*8 + 4]
00387224  44 8B C0                        mov r8d, eax
00387227  45 3B CD                        cmp r9d, r13d
0038722A  0F 84 7F 02 00 00               je 0x1403874af
00387230  85 C0                           test eax, eax
00387232  0F 85 64 02 00 00               jne 0x14038749c
00387238  33 C9                           xor ecx, ecx
0038723A  42 8B 04 C2                     mov eax, dword ptr [rdx + r8*8]
0038723E  2B C1                           sub eax, ecx
00387240  41 03 C1                        add eax, r9d
00387243  0F 84 66 02 00 00               je 0x1403874af
00387249  41 B8 01 00 00 00               mov r8d, 1
0038724F  8B D3                           mov edx, ebx
00387251  48 8B CF                        mov rcx, rdi
00387254  E8 87 09 00 00                  call 0x140387be0
00387259  84 C0                           test al, al
0038725B  0F 84 54 01 00 00               je 0x1403873b5
00387261  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00387265  8D 14 2E                        lea edx, [rsi + rbp]
00387268  8D 4B 01                        lea ecx, [rbx + 1]
0038726B  44 89 6C D8 04                  mov dword ptr [rax + rbx*8 + 4], r13d
00387270  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00387274  89 14 D8                        mov dword ptr [rax + rbx*8], edx
00387277  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0038727B  01 6C C8 04                     add dword ptr [rax + rcx*8 + 4], ebp
0038727F  48 03 F5                        add rsi, rbp
00387282  33 ED                           xor ebp, ebp
00387284  E9 1A FE FF FF                  jmp 0x1403870a3
00387289  49 C1 E1 03                     shl r9, 3
0038728D  85 DB                           test ebx, ebx
0038728F  0F 84 6E 01 00 00               je 0x140387403
00387295  45 8B 54 11 04                  mov r10d, dword ptr [r9 + rdx + 4]
0038729A  45 3B D5                        cmp r10d, r13d
0038729D  0F 85 44 01 00 00               jne 0x1403873e7
003872A3  45 8B 54 11 04                  mov r10d, dword ptr [r9 + rdx + 4]
003872A8  45 3B D5                        cmp r10d, r13d
003872AB  0F 85 17 02 00 00               jne 0x1403874c8
003872B1  85 DB                           test ebx, ebx
003872B3  0F 84 27 02 00 00               je 0x1403874e0
003872B9  8D 43 FF                        lea eax, [rbx - 1]
003872BC  4C 8D 14 C2                     lea r10, [rdx + rax*8]
003872C0  44 8B C8                        mov r9d, eax
003872C3  45 8B 42 04                     mov r8d, dword ptr [r10 + 4]
003872C7  45 3B C5                        cmp r8d, r13d
003872CA  0F 85 60 02 00 00               jne 0x140387530
003872D0  41 3B DE                        cmp ebx, r14d
003872D3  0F 83 D4 00 00 00               jae 0x1403873ad
003872D9  8D 43 01                        lea eax, [rbx + 1]
003872DC  44 39 6C C2 04                  cmp dword ptr [rdx + rax*8 + 4], r13d
003872E1  0F 84 C6 00 00 00               je 0x1403873ad
003872E7  44 89 6C DA 04                  mov dword ptr [rdx + rbx*8 + 4], r13d
003872EC  41 B8 01 00 00 00               mov r8d, 1
003872F2  41 8B D1                        mov edx, r9d
003872F5  48 8B CF                        mov rcx, rdi
003872F8  E8 A3 0B 00 00                  call 0x140387ea0
003872FD  E9 A1 FD FF FF                  jmp 0x1403870a3
00387302  44 8B 3C DA                     mov r15d, dword ptr [rdx + rbx*8]
00387306  48 8D 04 2E                     lea rax, [rsi + rbp]
0038730A  44 8B 44 DA 04                  mov r8d, dword ptr [rdx + rbx*8 + 4]
0038730F  41 8D 4F FF                     lea ecx, [r15 - 1]
00387313  48 3B C8                        cmp rcx, rax
00387316  0F 8C 08 01 00 00               jl 0x140387424
0038731C  45 3B C5                        cmp r8d, r13d
0038731F  0F 84 5A FF FF FF               je 0x14038727f
00387325  45 8B C3                        mov r8d, r11d
00387328  8B D3                           mov edx, ebx
0038732A  48 8B CF                        mov rcx, rdi
0038732D  E8 AE 08 00 00                  call 0x140387be0
00387332  84 C0                           test al, al
00387334  74 7F                           je 0x1403873b5
00387336  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
0038733A  8D 43 02                        lea eax, [rbx + 2]
0038733D  44 8B D0                        mov r10d, eax
00387340  44 8D 43 01                     lea r8d, [rbx + 1]
00387344  45 8B D8                        mov r11d, r8d
00387347  8B 44 C1 04                     mov eax, dword ptr [rcx + rax*8 + 4]
0038734B  89 44 D9 04                     mov dword ptr [rcx + rbx*8 + 4], eax
0038734F  8D 0C 2E                        lea ecx, [rsi + rbp]
00387352  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00387356  89 34 D8                        mov dword ptr [rax + rbx*8], esi
00387359  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0038735D  46 89 6C C0 04                  mov dword ptr [rax + r8*8 + 4], r13d
00387362  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00387366  42 89 0C C0                     mov dword ptr [rax + r8*8], ecx
0038736A  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
0038736E  85 DB                           test ebx, ebx
00387370  0F 84 4A 01 00 00               je 0x1403874c0
00387376  8D 43 FF                        lea eax, [rbx - 1]
00387379  44 8B 0C C2                     mov r9d, dword ptr [rdx + rax*8]
0038737D  45 85 C0                        test r8d, r8d
00387380  0F 84 21 01 00 00               je 0x1403874a7
00387386  44 8B 04 DA                     mov r8d, dword ptr [rdx + rbx*8]
0038738A  8B 0C DA                        mov ecx, dword ptr [rdx + rbx*8]
0038738D  42 03 0C DA                     add ecx, dword ptr [rdx + r11*8]
00387391  41 2B C8                        sub ecx, r8d
00387394  41 2B C9                        sub ecx, r9d
00387397  42 01 4C D2 04                  add dword ptr [rdx + r10*8 + 4], ecx
0038739C  E9 DE FE FF FF                  jmp 0x14038727f
003873A1  44 2B C0                        sub r8d, eax
003873A4  45 03 02                        add r8d, dword ptr [r10]
003873A7  0F 84 23 FF FF FF               je 0x1403872d0
003873AD  45 8B C3                        mov r8d, r11d
003873B0  E9 3D FF FF FF                  jmp 0x1403872f2
003873B5  32 C0                           xor al, al
003873B7  E9 17 FE FF FF                  jmp 0x1403871d3
003873BC  33 C0                           xor eax, eax
003873BE  E9 57 FD FF FF                  jmp 0x14038711a
003873C3  45 85 C0                        test r8d, r8d
003873C6  0F 85 59 01 00 00               jne 0x140387525
003873CC  33 C0                           xor eax, eax
003873CE  44 2B C8                        sub r9d, eax
003873D1  45 03 0B                        add r9d, dword ptr [r11]
003873D4  0F 84 AC FD FF FF               je 0x140387186
003873DA  41 B8 01 00 00 00               mov r8d, 1
003873E0  8B D3                           mov edx, ebx
003873E2  E9 0E FF FF FF                  jmp 0x1403872f5
003873E7  45 85 C0                        test r8d, r8d
003873EA  0F 84 18 01 00 00               je 0x140387508
003873F0  8D 43 FE                        lea eax, [rbx - 2]
003873F3  8B 04 C2                        mov eax, dword ptr [rdx + rax*8]
003873F6  44 2B D0                        sub r10d, eax
003873F9  45 03 14 11                     add r10d, dword ptr [r9 + rdx]
003873FD  0F 84 A0 FE FF FF               je 0x1403872a3
00387403  41 3B DE                        cmp ebx, r14d
00387406  0F 83 03 01 00 00               jae 0x14038750f
0038740C  8D 43 01                        lea eax, [rbx + 1]
0038740F  44 39 6C C2 04                  cmp dword ptr [rdx + rax*8 + 4], r13d
00387414  0F 84 F5 00 00 00               je 0x14038750f
0038741A  44 89 6C DA 04                  mov dword ptr [rdx + rbx*8 + 4], r13d
0038741F  E9 85 FC FF FF                  jmp 0x1403870a9
00387424  44 2B FE                        sub r15d, esi
00387427  45 3B C5                        cmp r8d, r13d
0038742A  74 12                           je 0x14038743e
0038742C  41 8D 42 FF                     lea eax, [r10 - 1]
00387430  3B D8                           cmp ebx, eax
00387432  72 26                           jb 0x14038745a
00387434  0F 84 DF 00 00 00               je 0x140387519
0038743A  42 89 34 F2                     mov dword ptr [rdx + r14*8], esi
0038743E  41 8B C7                        mov eax, r15d
00387441  48 03 F0                        add rsi, rax
00387444  48 2B E8                        sub rbp, rax
00387447  E9 57 FC FF FF                  jmp 0x1403870a3
0038744C  33 C0                           xor eax, eax
0038744E  E9 F4 FC FF FF                  jmp 0x140387147
00387453  33 C0                           xor eax, eax
00387455  E9 AB FD FF FF                  jmp 0x140387205
0038745A  8D 4B 01                        lea ecx, [rbx + 1]
0038745D  8B D9                           mov ebx, ecx
0038745F  44 39 6C CA 04                  cmp dword ptr [rdx + rcx*8 + 4], r13d
00387464  74 D4                           je 0x14038743a
00387466  8B D1                           mov edx, ecx
00387468  41 B8 01 00 00 00               mov r8d, 1
0038746E  48 8B CF                        mov rcx, rdi
00387471  E8 6A 07 00 00                  call 0x140387be0
00387476  84 C0                           test al, al
00387478  0F 84 37 FF FF FF               je 0x1403873b5
0038747E  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00387482  44 89 6C D8 04                  mov dword ptr [rax + rbx*8 + 4], r13d
00387487  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
0038748B  42 8B 04 F1                     mov eax, dword ptr [rcx + r14*8]
0038748F  89 04 D9                        mov dword ptr [rcx + rbx*8], eax
00387492  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
00387496  46 29 3C F0                     sub dword ptr [rax + r14*8], r15d
0038749A  EB A2                           jmp 0x14038743e
0038749C  8D 43 FE                        lea eax, [rbx - 2]
0038749F  8B 0C C2                        mov ecx, dword ptr [rdx + rax*8]
003874A2  E9 93 FD FF FF                  jmp 0x14038723a
003874A7  45 33 C0                        xor r8d, r8d
003874AA  E9 DB FE FF FF                  jmp 0x14038738a
003874AF  42 01 2C C2                     add dword ptr [rdx + r8*8], ebp
003874B3  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
003874B7  01 6C D8 04                     add dword ptr [rax + rbx*8 + 4], ebp
003874BB  E9 BF FD FF FF                  jmp 0x14038727f
003874C0  45 33 C9                        xor r9d, r9d
003874C3  E9 B5 FE FF FF                  jmp 0x14038737d
003874C8  45 85 C0                        test r8d, r8d
003874CB  74 54                           je 0x140387521
003874CD  8D 43 FE                        lea eax, [rbx - 2]
003874D0  8B 04 C2                        mov eax, dword ptr [rdx + rax*8]
003874D3  44 2B D0                        sub r10d, eax
003874D6  45 03 14 11                     add r10d, dword ptr [r9 + rdx]
003874DA  0F 84 D1 FD FF FF               je 0x1403872b1
003874E0  41 3B DE                        cmp ebx, r14d
003874E3  0F 83 F1 FE FF FF               jae 0x1403873da
003874E9  8D 43 01                        lea eax, [rbx + 1]
003874EC  44 39 6C C2 04                  cmp dword ptr [rdx + rax*8 + 4], r13d
003874F1  0F 84 E3 FE FF FF               je 0x1403873da
003874F7  85 DB                           test ebx, ebx
003874F9  0F 85 BA FD FF FF               jne 0x1403872b9
003874FF  44 8D 4B FF                     lea r9d, [rbx - 1]
00387503  E9 C8 FD FF FF                  jmp 0x1403872d0
00387508  33 C0                           xor eax, eax
0038750A  E9 E7 FE FF FF                  jmp 0x1403873f6
0038750F  85 DB                           test ebx, ebx
00387511  0F 85 8C FD FF FF               jne 0x1403872a3
00387517  EB C7                           jmp 0x1403874e0
00387519  89 34 DA                        mov dword ptr [rdx + rbx*8], esi
0038751C  E9 1D FF FF FF                  jmp 0x14038743e
00387521  33 C0                           xor eax, eax
00387523  EB AE                           jmp 0x1403874d3
00387525  8D 43 FE                        lea eax, [rbx - 2]
00387528  8B 04 C2                        mov eax, dword ptr [rdx + rax*8]
0038752B  E9 9E FE FF FF                  jmp 0x1403873ce
00387530  85 C0                           test eax, eax
00387532  0F 85 0E D9 35 00               jne 0x1406e4e46
00387538  E9 64 FE FF FF                  jmp 0x1403873a1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlRemoveBaseMcbEntry(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (32);
    if (a2 == 0) goto loc_003871AF;
loc_0038709F:
    v_r13 = (unsigned int)((v_r13) | (0xFFFFFFFFULL));
loc_003870A3:
loc_003870A9:
    if (condition_is_less_or_equal) goto loc_003871D1;
    a3 = 0;
loc_003870C0:
    if (0 > ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1))))) goto loc_003871D1;
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1)) + a3 * 1) == 0) goto loc_00387103;
loc_003870E4:
    if (((unsigned int)(a2)) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + (int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1)) + a3 * 1 - 1)) * 8))))) goto loc_003870FE;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + (int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1)) + a3 * 1)))) * 8))) - 1);
    if (((unsigned int)(a2)) <= ((unsigned int)(a1))) goto loc_0038710A;
    goto loc_003870C0;
loc_003870FE:
    goto loc_003870C0;
loc_00387103:
    result = 0;
    a2 = (unsigned int)((*(unsigned __int64 *)(a1 + 16)) | (0xFFFFFFFFULL));
    goto loc_003870E4;
loc_0038710A:
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1)) + a3 * 1))) == 0) goto loc_003873BC;
loc_0038711A:
    if (((unsigned int)(*(unsigned int *)(a2 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1)) + a3 * 1)) - 1 * 8))) != a2) goto loc_003871F9;
    if (((unsigned int)(*(unsigned int *)(a2 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1)) + a3 * 1)) * 8)) - 1) >= (a2 + a3 * 1)) goto loc_003871F3;
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1)) + a3 * 1))) == 0) goto loc_0038744C;
loc_00387147:
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1)) + a3 * 1)) * 8))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1)) + a3 * 1)) - 1 * 8)))));
    v_rsi = (a2) + ((unsigned int)((unsigned int)(v_r11)));
    v_rbp = (a3) - ((unsigned int)((unsigned int)(v_r11)));
    if ((*(unsigned int *)(a2 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1)) + a3 * 1)) * 8 + 4)) == ((unsigned int)(v_r13))) goto loc_003870A9;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1)) + a3 * 1)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1))) goto loc_00387289;
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1)) + a3 * 1))) == 0) goto loc_003873DA;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1)) + a3 * 1)) - 1)) * 8 + 4)))) != ((unsigned int)(v_r13))) goto loc_003873C3;
loc_00387186:
    result = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1)) + a3 * 1)) - 1 + 2;
    v_r10 = (unsigned int)(*(unsigned int *)(a1 + 4));
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1)) + a3 * 1)) - 1 + 2)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))))) {
        v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 4))) - ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1)) + a3 * 1)) - 1)));
        a2 = a2 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1)) + a3 * 1)) - 1 + 2 * 8;
        a1 = a2 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1)) + a3 * 1)) - 1)) * 8;
        a3 = v_r10 - 2;
        a3 = (a3) << (3);
        result = memcpy(a1, a2, a3, (unsigned int)(*(unsigned int *)(a2 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)) - 1)) + a3 * 1)) - 1)) * 8 + 4)));
    }
    goto loc_003870A3;
loc_003871AF:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))) == 0) goto loc_0038709F;
    if (a3 < ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + (unsigned int)(*(unsigned int *)(a1 + 4)) - 1 * 8)))) goto loc_0038709F;
loc_003871D1:
loc_003871D3:
    v_rsp = (v_rsp) + (32);
    return 1;
loc_003871F3:
loc_003871F9:
    if ((unsigned int)(v_stack_p8) == 0) goto loc_00387453;
loc_00387205:
    if (((unsigned int)(*(unsigned int *)(a2 + a3 * 8))) != v_stack_p18) goto loc_00387302;
    if ((*(unsigned int *)(a2 + v_stack_p8 * 8 + 4)) == ((unsigned int)(v_r13))) goto loc_0038727F;
    if ((unsigned int)(v_stack_p8) == 0) goto loc_00387249;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + v_stack_p8 - 1 * 8 + 4)))) == ((unsigned int)(v_r13))) goto loc_003874AF;
    if ((unsigned int)(v_stack_p8 - 1) != 0) goto loc_0038749C;
    a1 = 0;
loc_0038723A:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + (unsigned int)((unsigned int)(v_stack_p8 - 1)) * 8))) - (0));
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + v_stack_p8 - 1 * 8 + 4)))));
    if (condition_is_equal) goto loc_003874AF;
loc_00387249:
    result = FsRtlAddEntry(v_stack_p20, (unsigned int)((unsigned int)(v_stack_p8)), 1, (unsigned int)(*(unsigned int *)(a2 + v_stack_p8 - 1 * 8 + 4)));
    if ((unsigned __int8)(result) == 0) goto loc_003873B5;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 16) + v_stack_p8 * 8 + 4) = (unsigned int)(v_r13);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 16) + v_stack_p8 * 8) = (unsigned int)(v_stack_p18 + v_stack_p10 * 1);
loc_0038727F:
    v_rsi = (v_stack_p18) + (v_stack_p10);
    v_rbp = 0;
    goto loc_003870A3;
loc_00387289:
    a4 = ((unsigned int)(*(unsigned int *)(a2 + v_stack_p8 - 1 * 8 + 4))) << (3);
    if ((unsigned int)(v_stack_p8) == 0) goto loc_00387403;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + v_stack_p18 + v_stack_p10 * 1 * 1 + 4)))) != ((unsigned int)(v_r13))) goto loc_003873E7;
loc_003872A3:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + v_stack_p18 + v_stack_p10 * 1 * 1 + 4)))) != ((unsigned int)(v_r13))) goto loc_003874C8;
loc_003872B1:
    if ((unsigned int)(v_stack_p8) == 0) goto loc_003874E0;
loc_003872B9:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18 + v_stack_p10 * 1 + v_stack_p8 - 1 * 8 + 4)))) != ((unsigned int)(v_r13))) goto loc_00387530;
loc_003872D0:
    if (((unsigned int)(v_stack_p8)) >= ((unsigned int)(v_stack_p8))) goto loc_003873AD;
    if ((*(unsigned int *)(v_stack_p18 + v_stack_p10 * 1 + v_stack_p8 + 1 * 8 + 4)) == ((unsigned int)(v_r13))) goto loc_003873AD;
    *(unsigned int *)(v_stack_p18 + v_stack_p10 * 1 + v_stack_p8 * 8 + 4) = (unsigned int)(v_r13);
loc_003872F2:
loc_003872F5:
    result = FsRtlRemoveLargeEntry(v_stack_p20, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p8 - 1)))), 1, (unsigned int)((unsigned int)(v_stack_p8 - 1)));
    goto loc_003870A3;
loc_00387302:
    if (((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p8 - 1)))) + v_stack_p8 * 8)) - 1) < (v_rsi + v_rbp * 1)) goto loc_00387424;
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p8 - 1)))) + v_stack_p8 * 8 + 4)))) == ((unsigned int)(v_r13))) goto loc_0038727F;
    result = FsRtlAddEntry(v_stack_p20, (unsigned int)((unsigned int)(v_stack_p8)), 2, (unsigned int)((unsigned int)(v_stack_p8 - 1)));
    if ((unsigned __int8)(result) == 0) goto loc_003873B5;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 16) + v_stack_p8 * 8 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 16) + v_stack_p8 + 2 * 8 + 4)));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 16) + v_stack_p8 * 8) = (unsigned int)(v_rsi);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 16) + v_stack_p8 + 1 * 8 + 4) = (unsigned int)(v_r13);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 16) + v_stack_p8 + 1 * 8) = (unsigned int)(v_rsi + v_rbp * 1);
    if ((unsigned int)(v_stack_p8) == 0) goto loc_003874C0;
loc_0038737D:
    if ((unsigned int)(v_stack_p8 + 1) == 0) goto loc_003874A7;
loc_0038738A:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 16) + v_stack_p8 * 8))) + (*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 16) + (unsigned int)((unsigned int)(v_stack_p8 + 1)) * 8)));
    a1 = (unsigned int)((a1) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 16) + v_stack_p8 * 8)))));
    a1 = (unsigned int)((a1) - ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 16) + v_stack_p8 - 1 * 8)))));
    goto loc_0038727F;
loc_003873A1:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 16) + v_stack_p8 * 8))) - ((unsigned int)(v_stack_p8 - 1)));
    a3 = (unsigned int)((a3) + (*(unsigned int *)((unsigned int)((unsigned int)(v_stack_p8 + 2)))));
    if (condition_is_equal) goto loc_003872D0;
loc_003873AD:
    goto loc_003872F2;
loc_003873B5:
    result = 0;
    goto loc_003871D3;
loc_003873BC:
    result = 0;
    goto loc_0038711A;
loc_003873C3:
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p8 + 1))))) != 0) goto loc_00387525;
    result = 0;
loc_003873CE:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 16) + v_stack_p8 - 1 * 8))) - (0));
    a4 = (unsigned int)((a4) + (*(unsigned int *)((unsigned int)((unsigned int)(v_stack_p8 + 1)))));
    if (condition_is_equal) goto loc_00387186;
loc_003873DA:
    goto loc_003872F5;
loc_003873E7:
    if (1 == 0) goto loc_00387508;
loc_003873F6:
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p8 + 2))) - ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_stack_p8)) + v_stack_p8 - 2 * 8)))));
    v_r10 = (unsigned int)((v_r10) + (*(unsigned int *)(a4 + (unsigned int)((unsigned int)(v_stack_p8)) * 1)));
    if (condition_is_equal) goto loc_003872A3;
loc_00387403:
    if (((unsigned int)(v_stack_p8)) >= ((unsigned int)(v_stack_p8))) goto loc_0038750F;
    if ((*(unsigned int *)((unsigned int)((unsigned int)(v_stack_p8)) + v_stack_p8 + 1 * 8 + 4)) == ((unsigned int)(v_r13))) goto loc_0038750F;
    *(unsigned int *)((unsigned int)((unsigned int)(v_stack_p8)) + v_stack_p8 * 8 + 4) = (unsigned int)(v_r13);
    goto loc_003870A9;
loc_00387424:
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p8 - 1)))) + v_stack_p8 * 8))) - ((unsigned int)(v_rsi)));
    if (1 == ((unsigned int)(v_r13))) goto loc_0038743E;
    if (((unsigned int)(v_stack_p8)) < ((unsigned int)(v_r10 - 1))) goto loc_0038745A;
    if (((unsigned int)(v_stack_p8)) == ((unsigned int)(v_r10 - 1))) goto loc_00387519;
loc_0038743A:
    *(unsigned int *)((unsigned int)((unsigned int)(v_stack_p8)) + v_stack_p8 * 8) = (unsigned int)(v_rsi);
loc_0038743E:
    v_rsi = (v_rsi) + ((unsigned int)((unsigned int)(v_r15)));
    v_rbp = (v_rbp) - ((unsigned int)((unsigned int)(v_r15)));
    goto loc_003870A3;
loc_0038744C:
    result = 0;
    goto loc_00387147;
loc_00387453:
    result = 0;
    goto loc_00387205;
loc_0038745A:
    if ((*(unsigned int *)((unsigned int)((unsigned int)(v_stack_p8)) + v_stack_p8 + 1 * 8 + 4)) == ((unsigned int)(v_r13))) goto loc_0038743A;
    result = FsRtlAddEntry(v_stack_p20, (unsigned int)((unsigned int)(v_stack_p8 + 1)), 1, a4);
    if ((unsigned __int8)(result) == 0) goto loc_003873B5;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 16) + (unsigned int)((unsigned int)(v_stack_p8 + 1)) * 8 + 4) = (unsigned int)(v_r13);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 16) + (unsigned int)((unsigned int)(v_stack_p8 + 1)) * 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p20 + 16) + v_stack_p8 * 8)));
    goto loc_0038743E;
loc_0038749C:
    goto loc_0038723A;
loc_003874A7:
    a3 = 0;
    goto loc_0038738A;
loc_003874AF:
    goto loc_0038727F;
loc_003874C0:
    a4 = 0;
    goto loc_0038737D;
loc_003874C8:
    if (0 == 0) goto loc_00387521;
loc_003874D3:
    v_r10 = (unsigned int)((v_r10) - ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_stack_p8 + 1)) + (unsigned int)((unsigned int)(v_stack_p8 + 1)) - 2 * 8)))));
    v_r10 = (unsigned int)((v_r10) + (*(unsigned int *)(a4 + (unsigned int)((unsigned int)(v_stack_p8 + 1)) * 1)));
    if (condition_is_equal) goto loc_003872B1;
loc_003874E0:
    if (((unsigned int)((unsigned int)((unsigned int)(v_stack_p8 + 1)))) >= ((unsigned int)(v_stack_p8))) goto loc_003873DA;
    if ((*(unsigned int *)((unsigned int)((unsigned int)(v_stack_p8 + 1)) + (unsigned int)((unsigned int)(v_stack_p8 + 1)) + 1 * 8 + 4)) == ((unsigned int)(v_r13))) goto loc_003873DA;
    if ((unsigned int)((unsigned int)((unsigned int)(v_stack_p8 + 1))) != 0) goto loc_003872B9;
    goto loc_003872D0;
loc_00387508:
    result = 0;
    goto loc_003873F6;
loc_0038750F:
    if ((unsigned int)((unsigned int)((unsigned int)(v_stack_p8 + 1))) != 0) goto loc_003872A3;
    goto loc_003874E0;
loc_00387519:
    *(unsigned int *)((unsigned int)((unsigned int)(v_stack_p8 + 1)) + (unsigned int)((unsigned int)(v_stack_p8 + 1)) * 8) = (unsigned int)(v_rsi);
    goto loc_0038743E;
loc_00387521:
    result = 0;
    goto loc_003874D3;
loc_00387525:
    goto loc_003873CE;
loc_00387530:
    goto loc_003873A1;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlRemoveBaseMcbEntry(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (32);
    if (Arg2 == 0) goto loc_003871AF;
loc_0038709F:
    local_r13 = (uint32_t)((local_r13) | (0xFFFFFFFFULL));
loc_003870A3:
loc_003870A9:
    if (condition_is_less_or_equal) goto loc_003871D1;
    Arg3 = 0;
loc_003870C0:
    if (0 > ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 1))))) goto loc_003871D1;
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 1)) + Arg3 * 1) == 0) goto loc_00387103;
loc_003870E4:
    if (((uint32_t)(Arg2)) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + (int32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 0x1)) + Arg3 * 1 - 0x1)) * 8))))) goto loc_003870FE;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + (int32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 0x1)) + Arg3 * 1)))) * 8))) - 1);
    if (((uint32_t)(Arg2)) <= ((uint32_t)(Arg1))) goto loc_0038710A;
    goto loc_003870C0;
loc_003870FE:
    goto loc_003870C0;
loc_00387103:
    result = 0;
    Arg2 = (uint32_t)((*(uint64_t *)(arg1 + 0x10)) | (0xFFFFFFFFULL));
    goto loc_003870E4;
loc_0038710A:
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 1)) + Arg3 * 1))) == 0) goto loc_003873BC;
loc_0038711A:
    if (((uint32_t)(*(uint32_t *)(Arg2 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 0x1)) + Arg3 * 1)) - 0x1 * 8))) != Arg2) goto loc_003871F9;
    if (((uint32_t)(*(uint32_t *)(Arg2 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 0x1)) + Arg3 * 1)) * 8)) - 1) >= (Arg2 + Arg3 * 1)) goto loc_003871F3;
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 1)) + Arg3 * 1))) == 0) goto loc_0038744C;
loc_00387147:
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 0x1)) + Arg3 * 1)) * 8))) - ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 0x1)) + Arg3 * 1)) - 0x1 * 8)))));
    local_rsi = (Arg2) + ((uint32_t)((uint32_t)(local_r11)));
    local_rbp = (Arg3) - ((uint32_t)((uint32_t)(local_r11)));
    if ((*(uint32_t *)(Arg2 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 0x1)) + Arg3 * 1)) * 8 + 0x4)) == ((uint32_t)(local_r13))) goto loc_003870A9;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 1)) + Arg3 * 1)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 1))) goto loc_00387289;
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 1)) + Arg3 * 1))) == 0) goto loc_003873DA;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 0x1)) + Arg3 * 1)) - 0x1)) * 8 + 0x4)))) != ((uint32_t)(local_r13))) goto loc_003873C3;
loc_00387186:
    result = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 1)) + Arg3 * 1)) - 1 + 2;
    local_r10 = (uint32_t)(*(uint32_t *)(arg1 + 0x4));
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 1)) + Arg3 * 1)) - 1 + 2)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))))) {
        local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x4))) - ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 1)) + Arg3 * 1)) - 1)));
        Arg2 = Arg2 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 1)) + Arg3 * 1)) - 1 + 2 * 8;
        Arg1 = Arg2 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 1)) + Arg3 * 1)) - 1)) * 8;
        Arg3 = local_r10 - 2;
        Arg3 = (Arg3) << (3);
        result = memcpy(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(Arg2 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 0x1)) + Arg3 * 1)) - 0x1)) * 8 + 0x4)));
    }
    goto loc_003870A3;
loc_003871AF:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))) == 0) goto loc_0038709F;
    if (Arg3 < ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + (uint32_t)(*(uint32_t *)(arg1 + 0x4)) - 0x1 * 8)))) goto loc_0038709F;
loc_003871D1:
loc_003871D3:
    local_rsp = (local_rsp) + (32);
    return 1;
loc_003871F3:
loc_003871F9:
    if ((uint32_t)(v_stack_p8) == 0) goto loc_00387453;
loc_00387205:
    if (((uint32_t)(*(uint32_t *)(Arg2 + Arg3 * 8))) != v_stack_p18) goto loc_00387302;
    if ((*(uint32_t *)(Arg2 + v_stack_p8 * 8 + 0x4)) == ((uint32_t)(local_r13))) goto loc_0038727F;
    if ((uint32_t)(v_stack_p8) == 0) goto loc_00387249;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + v_stack_p8 - 0x1 * 8 + 0x4)))) == ((uint32_t)(local_r13))) goto loc_003874AF;
    if ((uint32_t)(v_stack_p8 - 1) != 0) goto loc_0038749C;
    Arg1 = 0;
loc_0038723A:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + (uint32_t)((uint32_t)(v_stack_p8 - 0x1)) * 8))) - (0));
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + v_stack_p8 - 0x1 * 8 + 0x4)))));
    if (condition_is_equal) goto loc_003874AF;
loc_00387249:
    result = FsRtlAddEntry(v_stack_p20, (uint32_t)((uint32_t)(v_stack_p8)), 1, (uint32_t)(*(uint32_t *)(Arg2 + v_stack_p8 - 0x1 * 8 + 0x4)));
    if ((uint8_t)(result) == 0) goto loc_003873B5;
    *(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x10) + v_stack_p8 * 8 + 0x4) = (uint32_t)(local_r13);
    *(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x10) + v_stack_p8 * 8) = (uint32_t)(v_stack_p18 + v_stack_p10 * 1);
loc_0038727F:
    local_rsi = (v_stack_p18) + (v_stack_p10);
    local_rbp = 0;
    goto loc_003870A3;
loc_00387289:
    a4 = ((uint32_t)(*(uint32_t *)(Arg2 + v_stack_p8 - 0x1 * 8 + 0x4))) << (3);
    if ((uint32_t)(v_stack_p8) == 0) goto loc_00387403;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(a4 + v_stack_p18 + v_stack_p10 * 1 * 1 + 0x4)))) != ((uint32_t)(local_r13))) goto loc_003873E7;
loc_003872A3:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(a4 + v_stack_p18 + v_stack_p10 * 1 * 1 + 0x4)))) != ((uint32_t)(local_r13))) goto loc_003874C8;
loc_003872B1:
    if ((uint32_t)(v_stack_p8) == 0) goto loc_003874E0;
loc_003872B9:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + v_stack_p10 * 1 + v_stack_p8 - 0x1 * 8 + 0x4)))) != ((uint32_t)(local_r13))) goto loc_00387530;
loc_003872D0:
    if (((uint32_t)(v_stack_p8)) >= ((uint32_t)(v_stack_p8))) goto loc_003873AD;
    if ((*(uint32_t *)(v_stack_p18 + v_stack_p10 * 1 + v_stack_p8 + 0x1 * 8 + 0x4)) == ((uint32_t)(local_r13))) goto loc_003873AD;
    *(uint32_t *)(v_stack_p18 + v_stack_p10 * 1 + v_stack_p8 * 8 + 0x4) = (uint32_t)(local_r13);
loc_003872F2:
loc_003872F5:
    result = FsRtlRemoveLargeEntry(v_stack_p20, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p8 - 1)))), 1, (uint32_t)((uint32_t)(v_stack_p8 - 1)));
    goto loc_003870A3;
loc_00387302:
    if (((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p8 - 0x1)))) + v_stack_p8 * 8)) - 1) < (local_rsi + local_rbp * 1)) goto loc_00387424;
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p8 - 0x1)))) + v_stack_p8 * 8 + 0x4)))) == ((uint32_t)(local_r13))) goto loc_0038727F;
    result = FsRtlAddEntry(v_stack_p20, (uint32_t)((uint32_t)(v_stack_p8)), 2, (uint32_t)((uint32_t)(v_stack_p8 - 1)));
    if ((uint8_t)(result) == 0) goto loc_003873B5;
    *(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x10) + v_stack_p8 * 8 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x10) + v_stack_p8 + 0x2 * 8 + 0x4)));
    *(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x10) + v_stack_p8 * 8) = (uint32_t)(local_rsi);
    *(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x10) + v_stack_p8 + 0x1 * 8 + 0x4) = (uint32_t)(local_r13);
    *(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x10) + v_stack_p8 + 0x1 * 8) = (uint32_t)(local_rsi + local_rbp * 1);
    if ((uint32_t)(v_stack_p8) == 0) goto loc_003874C0;
loc_0038737D:
    if ((uint32_t)(v_stack_p8 + 1) == 0) goto loc_003874A7;
loc_0038738A:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x10) + v_stack_p8 * 8))) + (*(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x10) + (uint32_t)((uint32_t)(v_stack_p8 + 0x1)) * 8)));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x10) + v_stack_p8 * 8)))));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x10) + v_stack_p8 - 0x1 * 8)))));
    goto loc_0038727F;
loc_003873A1:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x10) + v_stack_p8 * 8))) - ((uint32_t)(v_stack_p8 - 1)));
    Arg3 = (uint32_t)((Arg3) + (*(uint32_t *)((uint32_t)((uint32_t)(v_stack_p8 + 0x2)))));
    if (condition_is_equal) goto loc_003872D0;
loc_003873AD:
    goto loc_003872F2;
loc_003873B5:
    result = 0;
    goto loc_003871D3;
loc_003873BC:
    result = 0;
    goto loc_0038711A;
loc_003873C3:
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p8 + 1))))) != 0) goto loc_00387525;
    result = 0;
loc_003873CE:
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x10) + v_stack_p8 - 0x1 * 8))) - (0));
    a4 = (uint32_t)((a4) + (*(uint32_t *)((uint32_t)((uint32_t)(v_stack_p8 + 0x1)))));
    if (condition_is_equal) goto loc_00387186;
loc_003873DA:
    goto loc_003872F5;
loc_003873E7:
    if (1 == 0) goto loc_00387508;
loc_003873F6:
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p8 + 2))) - ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(v_stack_p8)) + v_stack_p8 - 0x2 * 8)))));
    local_r10 = (uint32_t)((local_r10) + (*(uint32_t *)(a4 + (uint32_t)((uint32_t)(v_stack_p8)) * 1)));
    if (condition_is_equal) goto loc_003872A3;
loc_00387403:
    if (((uint32_t)(v_stack_p8)) >= ((uint32_t)(v_stack_p8))) goto loc_0038750F;
    if ((*(uint32_t *)((uint32_t)((uint32_t)(v_stack_p8)) + v_stack_p8 + 0x1 * 8 + 0x4)) == ((uint32_t)(local_r13))) goto loc_0038750F;
    *(uint32_t *)((uint32_t)((uint32_t)(v_stack_p8)) + v_stack_p8 * 8 + 0x4) = (uint32_t)(local_r13);
    goto loc_003870A9;
loc_00387424:
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p8 - 0x1)))) + v_stack_p8 * 8))) - ((uint32_t)(local_rsi)));
    if (1 == ((uint32_t)(local_r13))) goto loc_0038743E;
    if (((uint32_t)(v_stack_p8)) < ((uint32_t)(local_r10 - 1))) goto loc_0038745A;
    if (((uint32_t)(v_stack_p8)) == ((uint32_t)(local_r10 - 1))) goto loc_00387519;
loc_0038743A:
    *(uint32_t *)((uint32_t)((uint32_t)(v_stack_p8)) + v_stack_p8 * 8) = (uint32_t)(local_rsi);
loc_0038743E:
    local_rsi = (local_rsi) + ((uint32_t)((uint32_t)(local_r15)));
    local_rbp = (local_rbp) - ((uint32_t)((uint32_t)(local_r15)));
    goto loc_003870A3;
loc_0038744C:
    result = 0;
    goto loc_00387147;
loc_00387453:
    result = 0;
    goto loc_00387205;
loc_0038745A:
    if ((*(uint32_t *)((uint32_t)((uint32_t)(v_stack_p8)) + v_stack_p8 + 0x1 * 8 + 0x4)) == ((uint32_t)(local_r13))) goto loc_0038743A;
    result = FsRtlAddEntry(v_stack_p20, (uint32_t)((uint32_t)(v_stack_p8 + 1)), 1, a4);
    if ((uint8_t)(result) == 0) goto loc_003873B5;
    *(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x10) + (uint32_t)((uint32_t)(v_stack_p8 + 0x1)) * 8 + 0x4) = (uint32_t)(local_r13);
    *(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x10) + (uint32_t)((uint32_t)(v_stack_p8 + 0x1)) * 8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p20 + 0x10) + v_stack_p8 * 8)));
    goto loc_0038743E;
loc_0038749C:
    goto loc_0038723A;
loc_003874A7:
    Arg3 = 0;
    goto loc_0038738A;
loc_003874AF:
    goto loc_0038727F;
loc_003874C0:
    a4 = 0;
    goto loc_0038737D;
loc_003874C8:
    if (0 == 0) goto loc_00387521;
loc_003874D3:
    local_r10 = (uint32_t)((local_r10) - ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(v_stack_p8 + 0x1)) + (uint32_t)((uint32_t)(v_stack_p8 + 0x1)) - 0x2 * 8)))));
    local_r10 = (uint32_t)((local_r10) + (*(uint32_t *)(a4 + (uint32_t)((uint32_t)(v_stack_p8 + 0x1)) * 1)));
    if (condition_is_equal) goto loc_003872B1;
loc_003874E0:
    if (((uint32_t)((uint32_t)((uint32_t)(v_stack_p8 + 1)))) >= ((uint32_t)(v_stack_p8))) goto loc_003873DA;
    if ((*(uint32_t *)((uint32_t)((uint32_t)(v_stack_p8 + 0x1)) + (uint32_t)((uint32_t)(v_stack_p8 + 0x1)) + 0x1 * 8 + 0x4)) == ((uint32_t)(local_r13))) goto loc_003873DA;
    if ((uint32_t)((uint32_t)((uint32_t)(v_stack_p8 + 1))) != 0) goto loc_003872B9;
    goto loc_003872D0;
loc_00387508:
    result = 0;
    goto loc_003873F6;
loc_0038750F:
    if ((uint32_t)((uint32_t)((uint32_t)(v_stack_p8 + 1))) != 0) goto loc_003872A3;
    goto loc_003874E0;
loc_00387519:
    *(uint32_t *)((uint32_t)((uint32_t)(v_stack_p8 + 0x1)) + (uint32_t)((uint32_t)(v_stack_p8 + 0x1)) * 8) = (uint32_t)(local_rsi);
    goto loc_0038743E;
loc_00387521:
    result = 0;
    goto loc_003874D3;
loc_00387525:
    goto loc_003873CE;
loc_00387530:
    goto loc_003873A1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R/W` |
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00387070&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
