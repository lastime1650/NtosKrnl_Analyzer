# MiFindBestLargePageStealCandidates

- RVA: `0x00453EEC`–`0x00454450` (길이 `1,380` bytes)
- VA: `0x0000000140453EEC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A78E4`
- 디코드: `340`개 명령, `1,380/1,380` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00453F1E` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004540A2` → [MiCollapseRunTopDown](../28/MiCollapseRunTopDown_function_0028CE30.md) (function, `0x0028CE30`)
- `0x004542D0` → [MiFindNextLowerLargePageCandidate](MiFindNextLowerLargePageCandidate_function_00454458.md) (function, `0x00454458`)
- `0x0045440A` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [MiFindContiguousPagesEx](../28/MiFindContiguousPagesEx_function_0028BDE0.md) at `0x0028CC2D`

### Static image references
- `0x00453F27` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00453FC5` → RVA `0x00010850` (`.rdata`; read)
- `0x004541BA` → RVA `0x00E3CCF8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00453EEC  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00453EF1  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00453EF6  55                              push rbp
00453EF7  53                              push rbx
00453EF8  56                              push rsi
00453EF9  57                              push rdi
00453EFA  41 54                           push r12
00453EFC  41 55                           push r13
00453EFE  41 56                           push r14
00453F00  41 57                           push r15
00453F02  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
00453F07  48 81 EC F8 00 00 00            sub rsp, 0xf8
00453F0E  33 D2                           xor edx, edx
00453F10  45 8B F0                        mov r14d, r8d
00453F13  48 8D 4D AF                     lea rcx, [rbp - 0x51]
00453F17  49 8B D9                        mov rbx, r9
00453F1A  44 8D 42 40                     lea r8d, [rdx + 0x40]
00453F1E  E8 1D 2D 27 00                  call 0x1406c6c40
00453F23  4C 8B 6D 7F                     mov r13, qword ptr [rbp + 0x7f]
00453F27  48 8D 0D D2 C0 BA FF            lea rcx, [rip - 0x453f2e]
00453F2E  4E 8B 94 F1 60 1C 01 00         mov r10, qword ptr [rcx + r14*8 + 0x11c60]
00453F36  45 33 C9                        xor r9d, r9d
00453F39  42 8B 84 B1 E8 35 01 00         mov eax, dword ptr [rcx + r14*4 + 0x135e8]
00453F41  45 33 FF                        xor r15d, r15d
00453F44  44 21 4C 24 28                  and dword ptr [rsp + 0x28], r9d
00453F49  45 33 E4                        xor r12d, r12d
00453F4C  4C 21 4C 24 50                  and qword ptr [rsp + 0x50], r9
00453F51  49 8D 7D 18                     lea rdi, [r13 + 0x18]
00453F55  41 8B 75 00                     mov esi, dword ptr [r13]
00453F59  49 8B D2                        mov rdx, r10
00453F5C  4C 8B 5D 4F                     mov r11, qword ptr [rbp + 0x4f]
00453F60  49 8B CA                        mov rcx, r10
00453F63  89 45 7F                        mov dword ptr [rbp + 0x7f], eax
00453F66  4D 8B C2                        mov r8, r10
00453F69  48 C1 EA 04                     shr rdx, 4
00453F6D  49 8B C2                        mov rax, r10
00453F70  48 C1 E8 04                     shr rax, 4
00453F74  48 C1 E9 02                     shr rcx, 2
00453F78  49 C1 E8 02                     shr r8, 2
00453F7C  41 83 FE 02                     cmp r14d, 2
00453F80  44 89 4D 5F                     mov dword ptr [rbp + 0x5f], r9d
00453F84  C7 45 67 01 00 00 00            mov dword ptr [rbp + 0x67], 1
00453F8B  4C 0F 45 C0                     cmovne r8, rax
00453F8F  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
00453F94  48 83 4C 24 20 FF               or qword ptr [rsp + 0x20], 0xffffffffffffffff
00453F9A  48 8D 04 49                     lea rax, [rcx + rcx*2]
00453F9E  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00453FA3  49 8B C2                        mov rax, r10
00453FA6  48 2B C2                        sub rax, rdx
00453FA9  4C 89 44 24 70                  mov qword ptr [rsp + 0x70], r8
00453FAE  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00453FB3  49 81 FA 00 02 00 00            cmp r10, 0x200
00453FBA  0F 86 FA 03 00 00               jbe 0x1404543ba
00453FC0  4C 21 4C 24 38                  and qword ptr [rsp + 0x38], r9
00453FC5  66 0F 6F 05 83 C8 BB FF         movdqa xmm0, xmmword ptr [rip - 0x44377d]
00453FCD  45 33 C0                        xor r8d, r8d
00453FD0  0F 11 45 97                     movups xmmword ptr [rbp - 0x69], xmm0
00453FD4  45 85 F6                        test r14d, r14d
00453FD7  74 3C                           je 0x140454015
00453FD9  33 D2                           xor edx, edx
00453FDB  4C 8D 0D 1E C0 BA FF            lea r9, [rip - 0x453fe2]
00453FE2  33 C9                           xor ecx, ecx
00453FE4  42 8B 84 0A E8 35 01 00         mov eax, dword ptr [rdx + r9 + 0x135e8]
00453FEC  2B 45 7F                        sub eax, dword ptr [rbp + 0x7f]
00453FEF  89 44 14 40                     mov dword ptr [rsp + rdx + 0x40], eax
00453FF3  41 83 FE 02                     cmp r14d, 2
00453FF7  0F 84 17 04 00 00               je 0x140454414
00453FFD  4C 89 54 0D 87                  mov qword ptr [rbp + rcx - 0x79], r10
00454002  41 FF C0                        inc r8d
00454005  48 83 C2 04                     add rdx, 4
00454009  48 83 C1 08                     add rcx, 8
0045400D  45 3B C6                        cmp r8d, r14d
00454010  72 D2                           jb 0x140453fe4
00454012  45 33 C9                        xor r9d, r9d
00454015  48 8B 55 6F                     mov rdx, qword ptr [rbp + 0x6f]
00454019  B8 00 00 10 00                  mov eax, 0x100000
0045401E  48 3B D8                        cmp rbx, rax
00454021  0F 82 7A 03 00 00               jb 0x1404543a1
00454027  49 8B 4D 10                     mov rcx, qword ptr [r13 + 0x10]
0045402B  48 FF C9                        dec rcx
0045402E  4C 89 55 CF                     mov qword ptr [rbp - 0x31], r10
00454032  49 03 CA                        add rcx, r10
00454035  4C 89 55 DF                     mov qword ptr [rbp - 0x21], r10
00454039  48 3B D1                        cmp rdx, rcx
0045403C  4C 89 55 D7                     mov qword ptr [rbp - 0x29], r10
00454040  4C 8B 55 57                     mov r10, qword ptr [rbp + 0x57]
00454044  48 0F 42 CA                     cmovb rcx, rdx
00454048  48 89 5D BF                     mov qword ptr [rbp - 0x41], rbx
0045404C  48 89 4D C7                     mov qword ptr [rbp - 0x39], rcx
00454050  41 8B 02                        mov eax, dword ptr [r10]
00454053  4C 8D 40 01                     lea r8, [rax + 1]
00454057  49 C1 E0 04                     shl r8, 4
0045405B  4D 03 C2                        add r8, r10
0045405E  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
00454063  85 C0                           test eax, eax
00454065  0F 84 C4 02 00 00               je 0x14045432f
0045406B  FF C8                           dec eax
0045406D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00454072  8B D0                           mov edx, eax
00454074  48 03 C0                        add rax, rax
00454077  49 8B 4C C2 10                  mov rcx, qword ptr [r10 + rax*8 + 0x10]
0045407C  48 89 4D AF                     mov qword ptr [rbp - 0x51], rcx
00454080  49 03 4C C2 18                  add rcx, qword ptr [r10 + rax*8 + 0x18]
00454085  48 89 4D B7                     mov qword ptr [rbp - 0x49], rcx
00454089  48 39 4D BF                     cmp qword ptr [rbp - 0x41], rcx
0045408D  0F 83 9C 02 00 00               jae 0x14045432f
00454093  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
00454096  85 C0                           test eax, eax
00454098  0F 89 3A 03 00 00               jns 0x1404543d8
0045409E  48 8D 4D AF                     lea rcx, [rbp - 0x51]
004540A2  E8 89 8D E3 FF                  call 0x14028ce30
004540A7  85 C0                           test eax, eax
004540A9  0F 84 9B 01 00 00               je 0x14045424a
004540AF  8B 4D 7F                        mov ecx, dword ptr [rbp + 0x7f]
004540B2  48 8B 55 B7                     mov rdx, qword ptr [rbp - 0x49]
004540B6  48 8B 5D AF                     mov rbx, qword ptr [rbp - 0x51]
004540BA  4C 8B DA                        mov r11, rdx
004540BD  48 D3 EB                        shr rbx, cl
004540C0  49 D3 EB                        shr r11, cl
004540C3  48 89 5D 6F                     mov qword ptr [rbp + 0x6f], rbx
004540C7  45 85 F6                        test r14d, r14d
004540CA  0F 85 A5 02 00 00               jne 0x140454375
004540D0  48 2B 54 24 48                  sub rdx, qword ptr [rsp + 0x48]
004540D5  4D 8D 43 FF                     lea r8, [r11 - 1]
004540D9  4C 8B 54 24 20                  mov r10, qword ptr [rsp + 0x20]
004540DE  49 89 55 10                     mov qword ptr [r13 + 0x10], rdx
004540E2  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
004540E7  48 8B CA                        mov rcx, rdx
004540EA  48 C1 E9 12                     shr rcx, 0x12
004540EE  48 85 C0                        test rax, rax
004540F1  74 09                           je 0x1404540fc
004540F3  49 3B CA                        cmp rcx, r10
004540F6  0F 85 A7 01 00 00               jne 0x1404542a3
004540FC  45 33 C9                        xor r9d, r9d
004540FF  45 3B CE                        cmp r9d, r14d
00454102  73 1D                           jae 0x140454121
00454104  42 8B 5C 8C 40                  mov ebx, dword ptr [rsp + r9*4 + 0x40]
00454109  49 8B D0                        mov rdx, r8
0045410C  8B CB                           mov ecx, ebx
0045410E  48 D3 EA                        shr rdx, cl
00454111  4A 39 54 CD 97                  cmp qword ptr [rbp + r9*8 - 0x69], rdx
00454116  0F 85 D3 00 00 00               jne 0x1404541ef
0045411C  41 FF C1                        inc r9d
0045411F  EB DE                           jmp 0x1404540ff
00454121  41 83 FE 02                     cmp r14d, 2
00454125  0F 84 8F 00 00 00               je 0x1404541ba
0045412B  48 8B 45 4F                     mov rax, qword ptr [rbp + 0x4f]
0045412F  41 83 FE 01                     cmp r14d, 1
00454133  0F 85 02 03 00 00               jne 0x14045443b
00454139  48 8B 80 00 40 00 00            mov rax, qword ptr [rax + 0x4000]
00454140  42 0F B7 04 40                  movzx eax, word ptr [rax + r8*2]
00454145  25 FF 03 00 00                  and eax, 0x3ff
0045414A  48 3B 44 24 60                  cmp rax, qword ptr [rsp + 0x60]
0045414F  0F 83 0C 01 00 00               jae 0x140454261
00454155  48 8B 5D 6F                     mov rbx, qword ptr [rbp + 0x6f]
00454159  4C 8B 54 24 20                  mov r10, qword ptr [rsp + 0x20]
0045415E  48 3B 44 24 70                  cmp rax, qword ptr [rsp + 0x70]
00454163  73 6D                           jae 0x1404541d2
00454165  44 8B 4D 5F                     mov r9d, dword ptr [rbp + 0x5f]
00454169  4D 85 C0                        test r8, r8
0045416C  0F 84 BD 01 00 00               je 0x14045432f
00454172  49 8B 55 10                     mov rdx, qword ptr [r13 + 0x10]
00454176  49 FF C8                        dec r8
00454179  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0045417E  48 2B 54 24 48                  sub rdx, qword ptr [rsp + 0x48]
00454183  48 FF C0                        inc rax
00454186  49 89 55 10                     mov qword ptr [r13 + 0x10], rdx
0045418A  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0045418F  4C 3B C3                        cmp r8, rbx
00454192  0F 82 B6 00 00 00               jb 0x14045424e
00454198  48 3D 00 00 02 00               cmp rax, 0x20000
0045419E  0F 82 3E FF FF FF               jb 0x1404540e2
004541A4  48 8D 0D 55 BE BA FF            lea rcx, [rip - 0x4541ab]
004541AB  42 FF 84 B1 80 53 EF 00         inc dword ptr [rcx + r14*4 + 0xef5380]
004541B3  33 DB                           xor ebx, ebx
004541B5  E9 78 01 00 00                  jmp 0x140454332
004541BA  48 8B 05 37 8B 9E 00            mov rax, qword ptr [rip + 0x9e8b37]
004541C1  42 0F B7 04 40                  movzx eax, word ptr [rax + r8*2]
004541C6  48 C1 E8 05                     shr rax, 5
004541CA  83 E0 1F                        and eax, 0x1f
004541CD  E9 78 FF FF FF                  jmp 0x14045414a
004541D2  44 8B 4D 5F                     mov r9d, dword ptr [rbp + 0x5f]
004541D6  44 3B FE                        cmp r15d, esi
004541D9  73 8E                           jae 0x140454169
004541DB  41 FF C4                        inc r12d
004541DE  8B C6                           mov eax, esi
004541E0  41 2B C4                        sub eax, r12d
004541E3  41 FF C7                        inc r15d
004541E6  4C 89 04 C7                     mov qword ptr [rdi + rax*8], r8
004541EA  E9 7A FF FF FF                  jmp 0x140454169
004541EF  4E 8B 5C CD 87                  mov r11, qword ptr [rbp + r9*8 - 0x79]
004541F4  4A 89 54 CD 97                  mov qword ptr [rbp + r9*8 - 0x69], rdx
004541F9  48 8B 45 4F                     mov rax, qword ptr [rbp + 0x4f]
004541FD  45 85 C9                        test r9d, r9d
00454200  0F 84 EB 00 00 00               je 0x1404542f1
00454206  48 8B 80 00 40 00 00            mov rax, qword ptr [rax + 0x4000]
0045420D  0F B7 04 50                     movzx eax, word ptr [rax + rdx*2]
00454211  25 FF 03 00 00                  and eax, 0x3ff
00454216  49 3B C3                        cmp rax, r11
00454219  0F 83 FD FE FF FF               jae 0x14045411c
0045421F  8B CB                           mov ecx, ebx
00454221  4C 8B C2                        mov r8, rdx
00454224  49 D3 E0                        shl r8, cl
00454227  8B 4D 7F                        mov ecx, dword ptr [rbp + 0x7f]
0045422A  49 FF C8                        dec r8
0045422D  49 8B C0                        mov rax, r8
00454230  48 D3 E0                        shl rax, cl
00454233  49 89 45 10                     mov qword ptr [r13 + 0x10], rax
00454237  48 85 D2                        test rdx, rdx
0045423A  0F 84 EB 00 00 00               je 0x14045432b
00454240  48 FF CA                        dec rdx
00454243  4A 3B 54 CD EF                  cmp rdx, qword ptr [rbp + r9*8 - 0x11]
00454248  73 AF                           jae 0x1404541f9
0045424A  44 8B 4D 5F                     mov r9d, dword ptr [rbp + 0x5f]
0045424E  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00454253  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
00454258  4C 8B 55 57                     mov r10, qword ptr [rbp + 0x57]
0045425C  E9 02 FE FF FF                  jmp 0x140454063
00454261  44 8B 4D 5F                     mov r9d, dword ptr [rbp + 0x5f]
00454265  48 3B 44 24 68                  cmp rax, qword ptr [rsp + 0x68]
0045426A  0F 83 9D 00 00 00               jae 0x14045430d
00454270  4E 89 04 CF                     mov qword ptr [rdi + r9*8], r8
00454274  8B C6                           mov eax, esi
00454276  41 2B C4                        sub eax, r12d
00454279  44 3B C8                        cmp r9d, eax
0045427C  0F 85 83 00 00 00               jne 0x140454305
00454282  41 FF CC                        dec r12d
00454285  41 FF C1                        inc r9d
00454288  44 89 4D 5F                     mov dword ptr [rbp + 0x5f], r9d
0045428C  44 3B CE                        cmp r9d, esi
0045428F  0F 84 1E FF FF FF               je 0x1404541b3
00454295  48 8B 5D 6F                     mov rbx, qword ptr [rbp + 0x6f]
00454299  4C 8B 54 24 20                  mov r10, qword ptr [rsp + 0x20]
0045429E  E9 C6 FE FF FF                  jmp 0x140454169
004542A3  48 8B 40 08                     mov rax, qword ptr [rax + 8]
004542A7  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
004542AC  48 0F A3 08                     bt qword ptr [rax], rcx
004542B0  0F 92 C0                        setb al
004542B3  84 C0                           test al, al
004542B5  0F 84 41 FE FF FF               je 0x1404540fc
004542BB  48 8B 4D 4F                     mov rcx, qword ptr [rbp + 0x4f]
004542BF  48 81 E2 00 00 FC FF            and rdx, 0xfffffffffffc0000
004542C6  41 B8 00 00 04 00               mov r8d, 0x40000
004542CC  49 89 55 10                     mov qword ptr [r13 + 0x10], rdx
004542D0  E8 83 01 00 00                  call 0x140454458
004542D5  4C 8B 54 24 20                  mov r10, qword ptr [rsp + 0x20]
004542DA  4C 8B C0                        mov r8, rax
004542DD  8B 4D 7F                        mov ecx, dword ptr [rbp + 0x7f]
004542E0  49 D3 E8                        shr r8, cl
004542E3  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
004542E8  49 89 45 10                     mov qword ptr [r13 + 0x10], rax
004542EC  E9 74 FE FF FF                  jmp 0x140454165
004542F1  48 8B 80 38 40 00 00            mov rax, qword ptr [rax + 0x4038]
004542F8  8B 04 90                        mov eax, dword ptr [rax + rdx*4]
004542FB  25 FF FF 07 00                  and eax, 0x7ffff
00454300  E9 11 FF FF FF                  jmp 0x140454216
00454305  41 FF C7                        inc r15d
00454308  E9 78 FF FF FF                  jmp 0x140454285
0045430D  44 8B 54 24 28                  mov r10d, dword ptr [rsp + 0x28]
00454312  4A 8B 04 D7                     mov rax, qword ptr [rdi + r10*8]
00454316  4A 89 04 CF                     mov qword ptr [rdi + r9*8], rax
0045431A  4E 89 04 D7                     mov qword ptr [rdi + r10*8], r8
0045431E  41 FF C2                        inc r10d
00454321  44 89 54 24 28                  mov dword ptr [rsp + 0x28], r10d
00454326  E9 49 FF FF FF                  jmp 0x140454274
0045432B  44 8B 4D 5F                     mov r9d, dword ptr [rbp + 0x5f]
0045432F  8B 5D 67                        mov ebx, dword ptr [rbp + 0x67]
00454332  45 85 E4                        test r12d, r12d
00454335  0F 85 B1 00 00 00               jne 0x1404543ec
0045433B  45 85 FF                        test r15d, r15d
0045433E  74 13                           je 0x140454353
00454340  8B 4D 7F                        mov ecx, dword ptr [rbp + 0x7f]
00454343  41 8B C7                        mov eax, r15d
00454346  48 D3 27                        shl qword ptr [rdi], cl
00454349  48 8D 7F 08                     lea rdi, [rdi + 8]
0045434D  48 83 E8 01                     sub rax, 1
00454351  75 F3                           jne 0x140454346
00454353  85 DB                           test ebx, ebx
00454355  74 05                           je 0x14045435c
00454357  49 83 4D 10 FF                  or qword ptr [r13 + 0x10], 0xffffffffffffffff
0045435C  45 89 7D 04                     mov dword ptr [r13 + 4], r15d
00454360  48 81 C4 F8 00 00 00            add rsp, 0xf8
00454367  41 5F                           pop r15
00454369  41 5E                           pop r14
0045436B  41 5D                           pop r13
0045436D  41 5C                           pop r12
0045436F  5F                              pop rdi
00454370  5E                              pop rsi
00454371  5B                              pop rbx
00454372  5D                              pop rbp
00454373  C3                              ret
00454374  CC                              int3
00454375  4C 8D 45 EF                     lea r8, [rbp - 0x11]
00454379  4D 8B D6                        mov r10, r14
0045437C  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
00454381  41 8B 09                        mov ecx, dword ptr [r9]
00454384  48 8B C3                        mov rax, rbx
00454387  48 D3 E8                        shr rax, cl
0045438A  4D 8D 49 04                     lea r9, [r9 + 4]
0045438E  49 89 00                        mov qword ptr [r8], rax
00454391  4D 8D 40 08                     lea r8, [r8 + 8]
00454395  49 83 EA 01                     sub r10, 1
00454399  0F 84 31 FD FF FF               je 0x1404540d0
0045439F  EB E0                           jmp 0x140454381
004543A1  48 3B D0                        cmp rdx, rax
004543A4  0F 86 7D FC FF FF               jbe 0x140454027
004543AA  49 39 83 48 48 00 00            cmp qword ptr [r11 + 0x4848], rax
004543B1  48 0F 47 D8                     cmova rbx, rax
004543B5  E9 6D FC FF FF                  jmp 0x140454027
004543BA  45 38 8B E6 3E 00 00            cmp byte ptr [r11 + 0x3ee6], r9b
004543C1  0F 84 F9 FB FF FF               je 0x140453fc0
004543C7  49 8D 83 C8 3F 00 00            lea rax, [r11 + 0x3fc8]
004543CE  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
004543D3  E9 ED FB FF FF                  jmp 0x140453fc5
004543D8  41 39 04 D0                     cmp dword ptr [r8 + rdx*8], eax
004543DC  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
004543E1  0F 84 B7 FC FF FF               je 0x14045409e
004543E7  E9 77 FC FF FF                  jmp 0x140454063
004543EC  41 2B F4                        sub esi, r12d
004543EF  44 3B CE                        cmp r9d, esi
004543F2  0F 84 43 FF FF FF               je 0x14045433b
004543F8  41 8B C1                        mov eax, r9d
004543FB  48 8D 14 F7                     lea rdx, [rdi + rsi*8]
004543FF  45 8B C4                        mov r8d, r12d
00454402  49 C1 E0 03                     shl r8, 3
00454406  48 8D 0C C7                     lea rcx, [rdi + rax*8]
0045440A  E8 31 24 27 00                  call 0x1406c6840
0045440F  E9 27 FF FF FF                  jmp 0x14045433b
00454414  4A 8B 84 09 60 1C 01 00         mov rax, qword ptr [rcx + r9 + 0x11c60]
0045441C  48 C1 E8 03                     shr rax, 3
00454420  48 89 44 0D 87                  mov qword ptr [rbp + rcx - 0x79], rax
00454425  45 85 C0                        test r8d, r8d
00454428  0F 85 D4 FB FF FF               jne 0x140454002
0045442E  48 D1 E8                        shr rax, 1
00454431  48 89 44 0D 87                  mov qword ptr [rbp + rcx - 0x79], rax
00454436  E9 C7 FB FF FF                  jmp 0x140454002
0045443B  48 8B 80 38 40 00 00            mov rax, qword ptr [rax + 0x4038]
00454442  42 8B 04 80                     mov eax, dword ptr [rax + r8*4]
00454446  25 FF FF 07 00                  and eax, 0x7ffff
0045444B  E9 FA FC FF FF                  jmp 0x14045414a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFindBestLargePageStealCandidates(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, unsigned int a6, unsigned int a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m47;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (248);
    a2 = 0;
    result = memset(v_stack_m98, a2, a2 + 64, a4);
    a4 = 0;
    v_r15 = 0;
    v_r12 = 0;
    v_stack_p38 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 4538158 + (unsigned int)(a3) * 4 + 79336)));
    a2 = (*(unsigned __int64 *)(v_rip - 4538158 + (unsigned int)(a3) * 8 + 72800)) >> (4);
    result = (*(unsigned __int64 *)(v_rip - 4538158 + (unsigned int)(a3) * 8 + 72800)) >> (4);
    a1 = (*(unsigned __int64 *)(v_rip - 4538158 + (unsigned int)(a3) * 8 + 72800)) >> (2);
    a3 = (*(unsigned __int64 *)(v_rip - 4538158 + (unsigned int)(a3) * 8 + 72800)) >> (2);
    v_stack_p18 = 0;
    v_stack_p20 = 1;
    if (((unsigned int)((unsigned int)(a3))) != 2) { a3 = result; }
    v_stack_mF0 = *(unsigned __int64 *)(v_rip - 4538158 + (unsigned int)(a3) * 8 + 72800);
    v_stack_mD8 = a1 + a1 * 2;
    result = (*(unsigned __int64 *)(v_rip - 4538158 + (unsigned int)(a3) * 8 + 72800)) - (a2);
    v_stack_mC8 = a3;
    v_stack_mD0 = result;
    if ((*(unsigned __int64 *)(v_rip - 4538158 + (unsigned int)(a3) * 8 + 72800)) <= 512) goto loc_004543BA;
loc_00453FC0:
loc_00453FC5:
    a3 = 0;
    v_stack_mB0 = v_xmm0;
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_00454015;
    a2 = 0;
    a1 = 0;
loc_00453FE4:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + v_rip - 4538338 * 1 + 79336))) - (a7));
    *(unsigned int *)(v_rsp + a2 * 1 + 64) = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(a3))) == 2) goto loc_00454414;
    *(unsigned __int64 *)(v_stack_m47 + a1 * 1 - 121) = *(unsigned __int64 *)(v_rip - 4538158 + (unsigned int)(a3) * 8 + 72800);
loc_00454002:
    a3 = (unsigned int)((a3) + 1);
    a2 = (a2) + (4);
    a1 = (a1) + (8);
    if (a3 < ((unsigned int)((unsigned int)(a3)))) goto loc_00453FE4;
    a4 = 0;
loc_00454015:
    if (0 < ((unsigned int)(0x100000ULL))) goto loc_004543A1;
loc_00454027:
    a1 = (*(unsigned __int64 *)(a7 + 16)) - 1;
    v_stack_m78 = *(unsigned __int64 *)(v_rip - 4538158 + (unsigned int)(a3) * 8 + 72800);
    a1 = (a1) + (*(unsigned __int64 *)(v_rip - 4538158 + (unsigned int)(a3) * 8 + 72800));
    v_stack_m68 = *(unsigned __int64 *)(v_rip - 4538158 + (unsigned int)(a3) * 8 + 72800);
    v_stack_m70 = *(unsigned __int64 *)(v_rip - 4538158 + (unsigned int)(a3) * 8 + 72800);
    if (a5 < a1) { a1 = a5; }
    v_stack_m88 = 0;
    v_stack_m80 = a1;
    a3 = ((unsigned int)(*(unsigned int *)(v_stack_p10)) + 1) << (4);
    a3 = (a3) + (v_stack_p10);
    v_stack_mE0 = a3;
loc_00454063:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10))) == 0) goto loc_0045432F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p10))) - 1);
    v_stack_m108 = result;
    result = (result) + (result);
    v_stack_m98 = *(unsigned __int64 *)(v_stack_p10 + result * 8 + 16);
    a1 = (*(unsigned __int64 *)(v_stack_p10 + result * 8 + 16)) + (*(unsigned __int64 *)(v_stack_p10 + result * 8 + 24));
    v_stack_m90 = a1;
    if (v_stack_m88 >= a1) goto loc_0045432F;
    if (!sign_flag) goto loc_004543D8;
loc_0045409E:
    result = MiCollapseRunTopDown(v_stack_m98, (unsigned int)((unsigned int)(result)), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_0045424A;
    v_rbx = (v_stack_m98) >> ((unsigned __int8)((unsigned int)(a7)));
    v_r11 = (v_stack_m90) >> ((unsigned __int8)((unsigned int)(a7)));
    v_stack_p28 = v_rbx;
    if ((unsigned int)((unsigned int)(a3)) != 0) goto loc_00454375;
loc_004540D0:
    a2 = (v_stack_m90) - (v_stack_mF0);
    *(unsigned __int64 *)(a7 + 16) = a2;
loc_004540E2:
    a1 = (a2) >> (18);
    if (v_stack_m100 == 0) goto loc_004540FC;
    if (a1 != v_stack_m118) goto loc_004542A3;
loc_004540FC:
    a4 = 0;
loc_004540FF:
    if (0 >= ((unsigned int)((unsigned int)(a3)))) goto loc_00454121;
    a2 = (v_r11 - 1) >> ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + a4 * 4 + 64))))));
    if ((*(unsigned __int64 *)(v_stack_m47 + a4 * 8 - 105)) != a2) goto loc_004541EF;
loc_0045411C:
    a4 = (unsigned int)((a4) + 1);
    goto loc_004540FF;
loc_00454121:
    if (((unsigned int)((unsigned int)(a3))) == 2) goto loc_004541BA;
    if (((unsigned int)((unsigned int)(a3))) != 1) goto loc_0045443B;
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 16384) + v_r11 - 1 * 2)) & (0x3FFULL));
loc_0045414A:
    if (result >= v_stack_mD8) goto loc_00454261;
    if (result >= v_stack_mC8) goto loc_004541D2;
loc_00454165:
loc_00454169:
    if (v_r11 - 1 == 0) goto loc_0045432F;
    a3 = (v_r11 - 1) - 1;
    a2 = (*(unsigned __int64 *)(a7 + 16)) - (v_stack_mF0);
    result = (v_stack_mE8) + 1;
    *(unsigned __int64 *)(a7 + 16) = a2;
    v_stack_mE8 = result;
    if (a3 < a5) goto loc_0045424E;
    if (result < 0x20000ULL) goto loc_004540E2;
loc_004541B3:
    v_rbx = 0;
    goto loc_00454332;
loc_004541BA:
    result = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 10390327) + a3 * 2)) >> (5);
    result = (unsigned int)((result) & (31));
    goto loc_0045414A;
loc_004541D2:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(a7))))) goto loc_00454169;
    v_r12 = (unsigned int)((v_r12) + 1);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a7))))) - ((unsigned int)(v_r12)));
    v_r15 = (unsigned int)((v_r15) + 1);
    *(unsigned __int64 *)(a7 + 24 + result * 8) = a3;
    goto loc_00454169;
loc_004541EF:
    *(unsigned __int64 *)(v_stack_m47 + (unsigned int)(v_stack_p18) * 8 - 105) = a2;
loc_004541F9:
    if ((unsigned int)((unsigned int)(v_stack_p18)) == 0) goto loc_004542F1;
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 16384) + a2 * 2)) & (0x3FFULL));
loc_00454216:
    if (result >= (*(unsigned __int64 *)(v_stack_m47 + (unsigned int)(v_stack_p18) * 8 - 121))) goto loc_0045411C;
    a3 = (a2) << (0);
    a3 = (a3) - 1;
    result = (a3) << ((unsigned __int8)((unsigned int)(a7)));
    *(unsigned __int64 *)(a7 + 16) = result;
    if (a2 == 0) goto loc_0045432B;
    a2 = (a2) - 1;
    if (a2 >= (*(unsigned __int64 *)(v_stack_m47 + (unsigned int)(v_stack_p18) * 8 - 17))) goto loc_004541F9;
loc_0045424A:
loc_0045424E:
    goto loc_00454063;
loc_00454261:
    if (v_stack_m108 >= v_stack_mD0) goto loc_0045430D;
    *(unsigned __int64 *)(a7 + 24 + (unsigned int)(v_stack_p18) * 8) = v_stack_mE0;
loc_00454274:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a7))))) - ((unsigned int)(v_r12)));
    if (((unsigned int)((unsigned int)(v_stack_p18))) != ((unsigned int)(result))) goto loc_00454305;
    v_r12 = (unsigned int)((v_r12) - 1);
loc_00454285:
    a4 = (unsigned int)(((unsigned int)(v_stack_p18)) + 1);
    v_stack_p18 = (unsigned int)(a4);
    if (((unsigned int)(a4)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a7))))) goto loc_004541B3;
    goto loc_00454169;
loc_004542A3:
    v_stack_m118 = (unsigned int)(a7);
    result = (((unsigned int)(a4)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a7))))) ? 1 : 0;
    if ((unsigned __int8)(result) == 0) goto loc_004540FC;
    a2 = (a2) & (0xFFFFFFFFFFFC0000ULL);
    *(unsigned __int64 *)(a7 + 16) = a2;
    result = MiFindNextLowerLargePageCandidate(v_stack_p8, a2, (unsigned int)(0x40000ULL), a4);
    a3 = (result) >> ((unsigned __int8)((unsigned int)(a7)));
    v_stack_m118 = v_stack_m118;
    *(unsigned __int64 *)(a7 + 16) = result;
    goto loc_00454165;
loc_004542F1:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 16440) + a2 * 4))) & (0x7FFFFULL));
    goto loc_00454216;
loc_00454305:
    v_r15 = (unsigned int)((v_r15) + 1);
    goto loc_00454285;
loc_0045430D:
    *(unsigned __int64 *)(a7 + 24 + a4 * 8) = *(unsigned __int64 *)(a7 + 24 + (unsigned int)(v_stack_m110) * 8);
    *(unsigned __int64 *)(a7 + 24 + (unsigned int)(v_stack_m110) * 8) = a3;
    v_r10 = (unsigned int)(((unsigned int)(v_stack_m110)) + 1);
    v_stack_m110 = (unsigned int)(v_r10);
    goto loc_00454274;
loc_0045432B:
loc_0045432F:
loc_00454332:
    if ((unsigned int)(v_r12) != 0) goto loc_004543EC;
loc_0045433B:
    if ((unsigned int)(v_r15) == 0) goto loc_00454353;
loc_00454346:
    result = ((unsigned int)((unsigned int)(v_r15))) - (1);
    if (condition_is_not_equal) goto loc_00454346;
loc_00454353:
    if ((unsigned int)((unsigned int)(v_stack_p20)) != 0) {
    }
    *(unsigned int *)(a7 + 4) = (unsigned int)(v_r15);
    v_rsp = (v_rsp) + (248);
    return result;
loc_00454375:
loc_00454381:
    result = ((unsigned int)(v_stack_p20)) >> ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p40))));
    *(unsigned __int64 *)(v_stack_m58) = result;
    v_r10 = ((unsigned int)(a3)) - (1);
    if (condition_is_equal) goto loc_004540D0;
    goto loc_00454381;
loc_004543A1:
    if (a2 <= result) goto loc_00454027;
    v_rbx = (unsigned int)(v_stack_p20);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m47 + (unsigned int)(v_stack_p18) * 8 - 121) + 18504)) > result) { v_rbx = result; }
    goto loc_00454027;
loc_004543BA:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m47 + (unsigned int)(v_stack_p18) * 8 - 121) + 16102)) == ((unsigned __int8)(v_stack_p40 + 4))) goto loc_00453FC0;
    v_stack_p38 = *(unsigned __int64 *)(v_stack_m47 + (unsigned int)(v_stack_p18) * 8 - 121) + 16328;
    goto loc_00453FC5;
loc_004543D8:
    if ((*(unsigned int *)(v_stack_m58 + 8 + a2 * 8)) == ((unsigned int)(*(unsigned __int64 *)(v_stack_m47 + (unsigned int)(v_stack_p18) * 8 - 121) + 16328))) goto loc_0045409E;
    goto loc_00454063;
loc_004543EC:
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(a7))) - ((unsigned int)(v_r12)));
    if (((unsigned int)(v_stack_p40 + 4)) == ((unsigned int)(v_rsi))) goto loc_0045433B;
    a3 = ((unsigned int)((unsigned int)(v_r12))) << (3);
    result = memcpy(a7 + 24 + 8 + (unsigned int)((unsigned int)(v_stack_p40 + 4)) * 8, a7 + 24 + 8 + v_rsi * 8, a3, v_stack_p40 + 4);
    goto loc_0045433B;
loc_00454414:
    result = (*(unsigned __int64 *)(a7 + 24 + 8 + (unsigned int)((unsigned int)(v_stack_p40 + 4)) * 8 + v_stack_p40 + 4 * 1 + 72800)) >> (3);
    *(unsigned __int64 *)(v_stack_m47 + a7 + 24 + 8 + (unsigned int)((unsigned int)(v_stack_p40 + 4)) * 8 * 1 - 121) = result;
    if (a3 != 0) goto loc_00454002;
    result = (result) >> (1);
    *(unsigned __int64 *)(v_stack_m47 + a7 + 24 + 8 + (unsigned int)((unsigned int)(v_stack_p40 + 4)) * 8 * 1 - 121) = result;
    goto loc_00454002;
loc_0045443B:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 16440) + a3 * 4))) & (0x7FFFFULL));
    goto loc_0045414A;
}
```

## 5. (Beta) C Style

```c
int64_t MiFindBestLargePageStealCandidates(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, void *Arg7)
{
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint32_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m47;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p8;

    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (248);
    Arg2 = 0;
    result = memset(v_stack_m98, Arg2, Arg2 + 64, Arg4);
    Arg4 = 0;
    local_r15 = 0;
    local_r12 = 0;
    v_stack_p38 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x453F2E + (uint32_t)(Arg3) * 4 + 0x135E8)));
    Arg2 = (*(uint64_t *)(v_rip - 0x453F2E + (uint32_t)(Arg3) * 8 + 0x11C60)) >> (4);
    result = (*(uint64_t *)(v_rip - 0x453F2E + (uint32_t)(Arg3) * 8 + 0x11C60)) >> (4);
    Arg1 = (*(uint64_t *)(v_rip - 0x453F2E + (uint32_t)(Arg3) * 8 + 0x11C60)) >> (2);
    Arg3 = (*(uint64_t *)(v_rip - 0x453F2E + (uint32_t)(Arg3) * 8 + 0x11C60)) >> (2);
    v_stack_p18 = 0;
    v_stack_p20 = 1;
    if (((uint32_t)((uint32_t)(Arg3))) != 2) { Arg3 = result; }
    v_stack_mF0 = *(uint64_t *)(v_rip - 0x453F2E + (uint32_t)(Arg3) * 8 + 0x11C60);
    v_stack_mD8 = Arg1 + Arg1 * 2;
    result = (*(uint64_t *)(v_rip - 0x453F2E + (uint32_t)(Arg3) * 8 + 0x11C60)) - (Arg2);
    v_stack_mC8 = Arg3;
    v_stack_mD0 = result;
    if ((*(uint64_t *)(v_rip - 0x453F2E + (uint32_t)(Arg3) * 8 + 0x11C60)) <= 512) goto loc_004543BA;
loc_00453FC0:
loc_00453FC5:
    Arg3 = 0;
    v_stack_mB0 = v_xmm0;
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_00454015;
    Arg2 = 0;
    Arg1 = 0;
loc_00453FE4:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + v_rip - 0x453FE2 * 1 + 0x135E8))) - (Arg7));
    *(uint32_t *)(local_rsp + Arg2 * 1 + 0x40) = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(Arg3))) == 2) goto loc_00454414;
    *(uint64_t *)(v_stack_m47 + Arg1 * 1 - 0x79) = *(uint64_t *)(v_rip - 0x453F2E + (uint32_t)(Arg3) * 8 + 0x11C60);
loc_00454002:
    Arg3 = (uint32_t)((Arg3) + 1);
    Arg2 = (Arg2) + (4);
    Arg1 = (Arg1) + (8);
    if (Arg3 < ((uint32_t)((uint32_t)(Arg3)))) goto loc_00453FE4;
    Arg4 = 0;
loc_00454015:
    if (0 < ((uint32_t)(0x100000ULL))) goto loc_004543A1;
loc_00454027:
    Arg1 = (*(uint64_t *)(arg7 + 0x10)) - 1;
    v_stack_m78 = *(uint64_t *)(v_rip - 0x453F2E + (uint32_t)(Arg3) * 8 + 0x11C60);
    Arg1 = (Arg1) + (*(uint64_t *)(v_rip - 0x453F2E + (uint32_t)(Arg3) * 8 + 0x11C60));
    v_stack_m68 = *(uint64_t *)(v_rip - 0x453F2E + (uint32_t)(Arg3) * 8 + 0x11C60);
    v_stack_m70 = *(uint64_t *)(v_rip - 0x453F2E + (uint32_t)(Arg3) * 8 + 0x11C60);
    if (Arg5 < Arg1) { Arg1 = Arg5; }
    v_stack_m88 = 0;
    v_stack_m80 = Arg1;
    Arg3 = ((uint32_t)(*(uint32_t *)(v_stack_p10)) + 1) << (4);
    Arg3 = (Arg3) + (v_stack_p10);
    v_stack_mE0 = Arg3;
loc_00454063:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10))) == 0) goto loc_0045432F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p10))) - 1);
    v_stack_m108 = result;
    result = (result) + (result);
    v_stack_m98 = *(uint64_t *)(v_stack_p10 + result * 8 + 0x10);
    Arg1 = (*(uint64_t *)(v_stack_p10 + result * 8 + 0x10)) + (*(uint64_t *)(v_stack_p10 + result * 8 + 0x18));
    v_stack_m90 = Arg1;
    if (v_stack_m88 >= Arg1) goto loc_0045432F;
    if (!sign_flag) goto loc_004543D8;
loc_0045409E:
    result = MiCollapseRunTopDown(v_stack_m98, (uint32_t)((uint32_t)(result)), Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0045424A;
    local_rbx = (v_stack_m98) >> ((uint8_t)((uint32_t)(Arg7)));
    local_r11 = (v_stack_m90) >> ((uint8_t)((uint32_t)(Arg7)));
    v_stack_p28 = local_rbx;
    if ((uint32_t)((uint32_t)(Arg3)) != 0) goto loc_00454375;
loc_004540D0:
    Arg2 = (v_stack_m90) - (v_stack_mF0);
    *(uint64_t *)(arg7 + 0x10) = Arg2;
loc_004540E2:
    Arg1 = (Arg2) >> (18);
    if (v_stack_m100 == 0) goto loc_004540FC;
    if (Arg1 != v_stack_m118) goto loc_004542A3;
loc_004540FC:
    Arg4 = 0;
loc_004540FF:
    if (0 >= ((uint32_t)((uint32_t)(Arg3)))) goto loc_00454121;
    Arg2 = (local_r11 - 1) >> ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + Arg4 * 4 + 0x40))))));
    if ((*(uint64_t *)(v_stack_m47 + Arg4 * 8 - 0x69)) != Arg2) goto loc_004541EF;
loc_0045411C:
    Arg4 = (uint32_t)((Arg4) + 1);
    goto loc_004540FF;
loc_00454121:
    if (((uint32_t)((uint32_t)(Arg3))) == 2) goto loc_004541BA;
    if (((uint32_t)((uint32_t)(Arg3))) != 1) goto loc_0045443B;
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x4000) + local_r11 - 0x1 * 2)) & (0x3FFULL));
loc_0045414A:
    if (result >= v_stack_mD8) goto loc_00454261;
    if (result >= v_stack_mC8) goto loc_004541D2;
loc_00454165:
loc_00454169:
    if (local_r11 - 1 == 0) goto loc_0045432F;
    Arg3 = (local_r11 - 1) - 1;
    Arg2 = (*(uint64_t *)(arg7 + 0x10)) - (v_stack_mF0);
    result = (v_stack_mE8) + 1;
    *(uint64_t *)(arg7 + 0x10) = Arg2;
    v_stack_mE8 = result;
    if (Arg3 < Arg5) goto loc_0045424E;
    if (result < 0x20000ULL) goto loc_004540E2;
loc_004541B3:
    local_rbx = 0;
    goto loc_00454332;
loc_004541BA:
    result = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x9E8B37) + Arg3 * 2)) >> (5);
    result = (uint32_t)((result) & (31));
    goto loc_0045414A;
loc_004541D2:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg7))))) goto loc_00454169;
    local_r12 = (uint32_t)((local_r12) + 1);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg7))))) - ((uint32_t)(local_r12)));
    local_r15 = (uint32_t)((local_r15) + 1);
    *(uint64_t *)(arg7 + 0x18 + result * 8) = Arg3;
    goto loc_00454169;
loc_004541EF:
    *(uint64_t *)(v_stack_m47 + (uint32_t)(v_stack_p18) * 8 - 0x69) = Arg2;
loc_004541F9:
    if ((uint32_t)((uint32_t)(v_stack_p18)) == 0) goto loc_004542F1;
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x4000) + Arg2 * 2)) & (0x3FFULL));
loc_00454216:
    if (result >= (*(uint64_t *)(v_stack_m47 + (uint32_t)(v_stack_p18) * 8 - 0x79))) goto loc_0045411C;
    Arg3 = (Arg2) << (0);
    Arg3 = (Arg3) - 1;
    result = (Arg3) << ((uint8_t)((uint32_t)(Arg7)));
    *(uint64_t *)(arg7 + 0x10) = result;
    if (Arg2 == 0) goto loc_0045432B;
    Arg2 = (Arg2) - 1;
    if (Arg2 >= (*(uint64_t *)(v_stack_m47 + (uint32_t)(v_stack_p18) * 8 - 0x11))) goto loc_004541F9;
loc_0045424A:
loc_0045424E:
    goto loc_00454063;
loc_00454261:
    if (v_stack_m108 >= v_stack_mD0) goto loc_0045430D;
    *(uint64_t *)(arg7 + 0x18 + (uint32_t)(v_stack_p18) * 8) = v_stack_mE0;
loc_00454274:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg7))))) - ((uint32_t)(local_r12)));
    if (((uint32_t)((uint32_t)(v_stack_p18))) != ((uint32_t)(result))) goto loc_00454305;
    local_r12 = (uint32_t)((local_r12) - 1);
loc_00454285:
    Arg4 = (uint32_t)(((uint32_t)(v_stack_p18)) + 1);
    v_stack_p18 = (uint32_t)(Arg4);
    if (((uint32_t)(Arg4)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg7))))) goto loc_004541B3;
    goto loc_00454169;
loc_004542A3:
    v_stack_m118 = (uint32_t)(Arg7);
    result = (((uint32_t)(Arg4)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg7))))) ? 1 : 0;
    if ((uint8_t)(result) == 0) goto loc_004540FC;
    Arg2 = (Arg2) & (0xFFFFFFFFFFFC0000ULL);
    *(uint64_t *)(arg7 + 0x10) = Arg2;
    result = MiFindNextLowerLargePageCandidate(v_stack_p8, Arg2, (uint32_t)(0x40000ULL), Arg4);
    Arg3 = (result) >> ((uint8_t)((uint32_t)(Arg7)));
    v_stack_m118 = v_stack_m118;
    *(uint64_t *)(arg7 + 0x10) = result;
    goto loc_00454165;
loc_004542F1:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x4038) + Arg2 * 4))) & (0x7FFFFULL));
    goto loc_00454216;
loc_00454305:
    local_r15 = (uint32_t)((local_r15) + 1);
    goto loc_00454285;
loc_0045430D:
    *(uint64_t *)(arg7 + 0x18 + Arg4 * 8) = *(uint64_t *)(arg7 + 0x18 + (uint32_t)(v_stack_m110) * 8);
    *(uint64_t *)(arg7 + 0x18 + (uint32_t)(v_stack_m110) * 8) = Arg3;
    local_r10 = (uint32_t)(((uint32_t)(v_stack_m110)) + 1);
    v_stack_m110 = (uint32_t)(local_r10);
    goto loc_00454274;
loc_0045432B:
loc_0045432F:
loc_00454332:
    if ((uint32_t)(local_r12) != 0) goto loc_004543EC;
loc_0045433B:
    if ((uint32_t)(local_r15) == 0) goto loc_00454353;
loc_00454346:
    result = ((uint32_t)((uint32_t)(local_r15))) - (1);
    if (condition_is_not_equal) goto loc_00454346;
loc_00454353:
    if ((uint32_t)((uint32_t)(v_stack_p20)) != 0) {
    }
    *(uint32_t *)(arg7 + 0x4) = (uint32_t)(local_r15);
    local_rsp = (local_rsp) + (248);
    return result;
loc_00454375:
loc_00454381:
    result = ((uint32_t)(v_stack_p20)) >> ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p40))));
    *(uint64_t *)(v_stack_m58) = result;
    local_r10 = ((uint32_t)(Arg3)) - (1);
    if (condition_is_equal) goto loc_004540D0;
    goto loc_00454381;
loc_004543A1:
    if (Arg2 <= result) goto loc_00454027;
    local_rbx = (uint32_t)(v_stack_p20);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m47 + (uint32_t)(v_stack_p18) * 8 - 0x79) + 0x4848)) > result) { local_rbx = result; }
    goto loc_00454027;
loc_004543BA:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m47 + (uint32_t)(v_stack_p18) * 8 - 0x79) + 0x3EE6)) == ((uint8_t)(v_stack_p40 + 4))) goto loc_00453FC0;
    v_stack_p38 = *(uint64_t *)(v_stack_m47 + (uint32_t)(v_stack_p18) * 8 - 0x79) + 16328;
    goto loc_00453FC5;
loc_004543D8:
    if ((*(uint32_t *)(v_stack_m58 + 0x8 + Arg2 * 8)) == ((uint32_t)(*(uint64_t *)(v_stack_m47 + (uint32_t)(v_stack_p18) * 8 - 0x79) + 16328))) goto loc_0045409E;
    goto loc_00454063;
loc_004543EC:
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(arg7))) - ((uint32_t)(local_r12)));
    if (((uint32_t)(v_stack_p40 + 4)) == ((uint32_t)(local_rsi))) goto loc_0045433B;
    Arg3 = ((uint32_t)((uint32_t)(local_r12))) << (3);
    result = memcpy(Arg7 + 24 + 8 + (uint32_t)((uint32_t)(v_stack_p40 + 4)) * 8, Arg7 + 24 + 8 + local_rsi * 8, Arg3, v_stack_p40 + 4);
    goto loc_0045433B;
loc_00454414:
    result = (*(uint64_t *)(arg7 + 0x18 + 0x8 + (uint32_t)((uint32_t)(v_stack_p40 + 0x4)) * 8 + v_stack_p40 + 0x4 * 1 + 0x11C60)) >> (3);
    *(uint64_t *)(v_stack_m47 + arg7 + 0x18 + 0x8 + (uint32_t)((uint32_t)(v_stack_p40 + 0x4)) * 8 * 1 - 0x79) = result;
    if (Arg3 != 0) goto loc_00454002;
    result = (result) >> (1);
    *(uint64_t *)(v_stack_m47 + arg7 + 0x18 + 0x8 + (uint32_t)((uint32_t)(v_stack_p40 + 0x4)) * 8 * 1 - 0x79) = result;
    goto loc_00454002;
loc_0045443B:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x4038) + Arg3 * 4))) & (0x7FFFFULL));
    goto loc_0045414A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg7` | `+ 0x0` | `32` | `R` |
| `Arg7` | `+ 0x0` | `64` | `R/W` |
| `Arg7` | `+ 0x0 + r10*8` | `64` | `R` |
| `Arg7` | `+ 0x0 + r10*8` | `64` | `W` |
| `Arg7` | `+ 0x0 + r9*8` | `64` | `W` |
| `Arg7` | `+ 0x0 + rax*8` | `64` | `R` |
| `Arg7` | `+ 0x0 + rax*8` | `64` | `W` |
| `Arg7` | `+ 0x0 + rsi*8` | `64` | `R` |
| `Arg7` | `+ 0x4` | `32` | `W` |
| `Arg7` | `+ 0x8` | `64` | `R` |
| `Arg7` | `+ 0x10` | `64` | `R` |
| `Arg7` | `+ 0x10` | `64` | `R/W` |
| `Arg7` | `+ 0x10` | `64` | `W` |
| `Arg7` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00453EEC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
