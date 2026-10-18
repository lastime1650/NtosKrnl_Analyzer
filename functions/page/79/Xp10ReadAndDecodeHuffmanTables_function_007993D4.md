# Xp10ReadAndDecodeHuffmanTables

- RVA: `0x007993D4`–`0x00799B60` (길이 `1,932` bytes)
- VA: `0x00000001407993D4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D02F0`
- 디코드: `565`개 명령, `1,932/1,932` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **17**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00799434` → [Xp10ScatteredReadBytes](Xp10ScatteredReadBytes_function_0079A220.md) (function, `0x0079A220`)
- `0x00799489` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007994F3` → [Xp10ScatteredReadBytes](Xp10ScatteredReadBytes_function_0079A220.md) (function, `0x0079A220`)
- `0x00799574` → [Xp10ScatteredReadBytes](Xp10ScatteredReadBytes_function_0079A220.md) (function, `0x0079A220`)
- `0x00799611` → [Xp10SortHuffmanSymbols](Xp10SortHuffmanSymbols_function_0079A2A4.md) (function, `0x0079A2A4`)
- `0x00799650` → [Xp10BuildHuffmanDecodeTable](Xp10BuildHuffmanDecodeTable_function_00796C00.md) (function, `0x00796C00`)
- `0x00799668` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007996C6` → [Xp10ScatteredReadBytes](Xp10ScatteredReadBytes_function_0079A220.md) (function, `0x0079A220`)
- `0x00799741` → [Xp10ScatteredReadBytes](Xp10ScatteredReadBytes_function_0079A220.md) (function, `0x0079A220`)
- `0x007997DC` → [Xp10ScatteredReadBytes](Xp10ScatteredReadBytes_function_0079A220.md) (function, `0x0079A220`)
- `0x00799932` → [Xp10ScatteredReadBytes](Xp10ScatteredReadBytes_function_0079A220.md) (function, `0x0079A220`)
- `0x007999C2` → [Xp10ScatteredReadBytes](Xp10ScatteredReadBytes_function_0079A220.md) (function, `0x0079A220`)
- `0x00799A3C` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00799AB7` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00799AD6` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00799AFB` → [Xp10SortHuffmanSymbols](Xp10SortHuffmanSymbols_function_0079A2A4.md) (function, `0x0079A2A4`)
- `0x00799B32` → [Xp10BuildHuffmanDecodeTable](Xp10BuildHuffmanDecodeTable_function_00796C00.md) (function, `0x00796C00`)

### Direct callers
- [Xp10ExecuteHuffmanDecode](Xp10ExecuteHuffmanDecode_function_007979C8.md) at `0x00797A4E`
- [Xp10ExecuteHuffmanDecode](Xp10ExecuteHuffmanDecode_function_007979C8.md) at `0x00797A87`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x00799489` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00799668` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00799A3C` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00799AB7` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00799AD6` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007993D4  48 8B C4                        mov rax, rsp
007993D7  48 89 58 08                     mov qword ptr [rax + 8], rbx
007993DB  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
007993DF  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
007993E3  89 50 10                        mov dword ptr [rax + 0x10], edx
007993E6  55                              push rbp
007993E7  56                              push rsi
007993E8  57                              push rdi
007993E9  41 54                           push r12
007993EB  41 55                           push r13
007993ED  41 56                           push r14
007993EF  41 57                           push r15
007993F1  48 8B EC                        mov rbp, rsp
007993F4  48 83 EC 60                     sub rsp, 0x60
007993F8  48 8B 5D 60                     mov rbx, qword ptr [rbp + 0x60]
007993FC  4C 8B F1                        mov r14, rcx
007993FF  33 C9                           xor ecx, ecx
00799401  44 8B FA                        mov r15d, edx
00799404  BE 02 00 00 00                  mov esi, 2
00799409  89 4D 58                        mov dword ptr [rbp + 0x58], ecx
0079940C  48 8B 03                        mov rax, qword ptr [rbx]
0079940F  48 85 C0                        test rax, rax
00799412  0F 84 2A 07 00 00               je 0x140799b42
00799418  48 3B C6                        cmp rax, rsi
0079941B  73 02                           jae 0x14079941f
0079941D  8B F0                           mov esi, eax
0079941F  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
00799422  3B C6                           cmp eax, esi
00799424  73 29                           jae 0x14079944f
00799426  48 8D 4B 18                     lea rcx, [rbx + 0x18]
0079942A  41 B8 04 00 00 00               mov r8d, 4
00799430  48 8D 55 58                     lea rdx, [rbp + 0x58]
00799434  E8 E7 0D 00 00                  call 0x14079a220
00799439  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
0079943C  8B 55 58                        mov edx, dword ptr [rbp + 0x58]
0079943F  48 D3 E2                        shl rdx, cl
00799442  48 09 53 08                     or qword ptr [rbx + 8], rdx
00799446  8D 04 C1                        lea eax, [rcx + rax*8]
00799449  3B C6                           cmp eax, esi
0079944B  73 02                           jae 0x14079944f
0079944D  8B F0                           mov esi, eax
0079944F  41 BC 01 00 00 00               mov r12d, 1
00799455  8B CE                           mov ecx, esi
00799457  2B C6                           sub eax, esi
00799459  41 8B FC                        mov edi, r12d
0079945C  48 D3 E7                        shl rdi, cl
0079945F  41 2B FC                        sub edi, r12d
00799462  8B CE                           mov ecx, esi
00799464  23 7B 08                        and edi, dword ptr [rbx + 8]
00799467  48 D3 6B 08                     shr qword ptr [rbx + 8], cl
0079946B  48 29 0B                        sub qword ptr [rbx], rcx
0079946E  89 43 10                        mov dword ptr [rbx + 0x10], eax
00799471  83 FE 02                        cmp esi, 2
00799474  0F 82 C8 06 00 00               jb 0x140799b42
0079947A  49 8D 76 18                     lea rsi, [r14 + 0x18]
0079947E  33 D2                           xor edx, edx
00799480  48 8B CE                        mov rcx, rsi
00799483  41 B8 C0 02 00 00               mov r8d, 0x2c0
00799489  E8 B2 D7 F2 FF                  call 0x1406c6c40
0079948E  45 33 C0                        xor r8d, r8d
00799491  85 FF                           test edi, edi
00799493  0F 84 00 06 00 00               je 0x140799a99
00799499  41 2B FC                        sub edi, r12d
0079949C  0F 84 ED 05 00 00               je 0x140799a8f
007994A2  41 3B FC                        cmp edi, r12d
007994A5  0F 85 97 06 00 00               jne 0x140799b42
007994AB  45 8D 7C 24 03                  lea r15d, [r12 + 3]
007994B0  41 8B F0                        mov esi, r8d
007994B3  45 8B EF                        mov r13d, r15d
007994B6  45 8B E7                        mov r12d, r15d
007994B9  83 FE 21                        cmp esi, 0x21
007994BC  0F 83 33 01 00 00               jae 0x1407995f5
007994C2  48 8B 03                        mov rax, qword ptr [rbx]
007994C5  BF 01 00 00 00                  mov edi, 1
007994CA  44 89 45 58                     mov dword ptr [rbp + 0x58], r8d
007994CE  48 85 C0                        test rax, rax
007994D1  0F 84 6B 06 00 00               je 0x140799b42
007994D7  48 3B C7                        cmp rax, rdi
007994DA  73 02                           jae 0x1407994de
007994DC  8B F8                           mov edi, eax
007994DE  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
007994E1  3B C7                           cmp eax, edi
007994E3  73 2C                           jae 0x140799511
007994E5  48 8D 4B 18                     lea rcx, [rbx + 0x18]
007994E9  41 B8 04 00 00 00               mov r8d, 4
007994EF  48 8D 55 58                     lea rdx, [rbp + 0x58]
007994F3  E8 28 0D 00 00                  call 0x14079a220
007994F8  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
007994FB  45 33 C0                        xor r8d, r8d
007994FE  8B 55 58                        mov edx, dword ptr [rbp + 0x58]
00799501  48 D3 E2                        shl rdx, cl
00799504  48 09 53 08                     or qword ptr [rbx + 8], rdx
00799508  8D 04 C1                        lea eax, [rcx + rax*8]
0079950B  3B C7                           cmp eax, edi
0079950D  73 02                           jae 0x140799511
0079950F  8B F8                           mov edi, eax
00799511  8B CF                           mov ecx, edi
00799513  2B C7                           sub eax, edi
00799515  BA 01 00 00 00                  mov edx, 1
0079951A  89 43 10                        mov dword ptr [rbx + 0x10], eax
0079951D  48 D3 E2                        shl rdx, cl
00799520  8B CF                           mov ecx, edi
00799522  FF CA                           dec edx
00799524  23 53 08                        and edx, dword ptr [rbx + 8]
00799527  48 D3 6B 08                     shr qword ptr [rbx + 8], cl
0079952B  48 29 0B                        sub qword ptr [rbx], rcx
0079952E  48 8B 0B                        mov rcx, qword ptr [rbx]
00799531  83 FF 01                        cmp edi, 1
00799534  0F 82 08 06 00 00               jb 0x140799b42
0079953A  85 D2                           test edx, edx
0079953C  0F 84 A5 00 00 00               je 0x1407995e7
00799542  83 FA 01                        cmp edx, 1
00799545  0F 85 F7 05 00 00               jne 0x140799b42
0079954B  44 89 45 58                     mov dword ptr [rbp + 0x58], r8d
0079954F  8D 7A 02                        lea edi, [rdx + 2]
00799552  48 85 C9                        test rcx, rcx
00799555  0F 84 E7 05 00 00               je 0x140799b42
0079955B  48 3B CF                        cmp rcx, rdi
0079955E  73 02                           jae 0x140799562
00799560  8B F9                           mov edi, ecx
00799562  3B C7                           cmp eax, edi
00799564  73 2C                           jae 0x140799592
00799566  48 8D 4B 18                     lea rcx, [rbx + 0x18]
0079956A  41 B8 04 00 00 00               mov r8d, 4
00799570  48 8D 55 58                     lea rdx, [rbp + 0x58]
00799574  E8 A7 0C 00 00                  call 0x14079a220
00799579  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
0079957C  45 33 C0                        xor r8d, r8d
0079957F  8B 55 58                        mov edx, dword ptr [rbp + 0x58]
00799582  48 D3 E2                        shl rdx, cl
00799585  48 09 53 08                     or qword ptr [rbx + 8], rdx
00799589  8D 04 C1                        lea eax, [rcx + rax*8]
0079958C  3B C7                           cmp eax, edi
0079958E  73 02                           jae 0x140799592
00799590  8B F8                           mov edi, eax
00799592  8B CF                           mov ecx, edi
00799594  2B C7                           sub eax, edi
00799596  BA 01 00 00 00                  mov edx, 1
0079959B  89 43 10                        mov dword ptr [rbx + 0x10], eax
0079959E  48 D3 E2                        shl rdx, cl
007995A1  FF CA                           dec edx
007995A3  8B CF                           mov ecx, edi
007995A5  23 53 08                        and edx, dword ptr [rbx + 8]
007995A8  48 D3 6B 08                     shr qword ptr [rbx + 8], cl
007995AC  48 29 0B                        sub qword ptr [rbx], rcx
007995AF  83 FF 03                        cmp edi, 3
007995B2  0F 82 8A 05 00 00               jb 0x140799b42
007995B8  41 3B D4                        cmp edx, r12d
007995BB  72 0B                           jb 0x1407995c8
007995BD  FF C2                           inc edx
007995BF  83 FA 08                        cmp edx, 8
007995C2  0F 87 7A 05 00 00               ja 0x140799b42
007995C8  8B C6                           mov eax, esi
007995CA  44 8B E2                        mov r12d, edx
007995CD  42 88 54 30 18                  mov byte ptr [rax + r14 + 0x18], dl
007995D2  85 D2                           test edx, edx
007995D4  74 07                           je 0x1407995dd
007995D6  41 3B D7                        cmp edx, r15d
007995D9  44 0F 42 FA                     cmovb r15d, edx
007995DD  41 3B D5                        cmp edx, r13d
007995E0  76 0C                           jbe 0x1407995ee
007995E2  44 8B EA                        mov r13d, edx
007995E5  EB 07                           jmp 0x1407995ee
007995E7  8B C6                           mov eax, esi
007995E9  46 88 64 30 18                  mov byte ptr [rax + r14 + 0x18], r12b
007995EE  FF C6                           inc esi
007995F0  E9 C4 FE FF FF                  jmp 0x1407994b9
007995F5  49 8D BE D8 02 00 00            lea rdi, [r14 + 0x2d8]
007995FC  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
00799601  48 8B D7                        mov rdx, rdi
00799604  49 8D 4E 18                     lea rcx, [r14 + 0x18]
00799608  45 8B CF                        mov r9d, r15d
0079960B  41 B8 21 00 00 00               mov r8d, 0x21
00799611  E8 8E 0C 00 00                  call 0x14079a2a4
00799616  85 C0                           test eax, eax
00799618  0F 84 24 05 00 00               je 0x140799b42
0079961E  4D 8D 8E 58 92 00 00            lea r9, [r14 + 0x9258]
00799625  4C 8B C7                        mov r8, rdi
00799628  49 8D 96 58 08 00 00            lea rdx, [r14 + 0x858]
0079962F  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00799634  49 8D 4E 18                     lea rcx, [r14 + 0x18]
00799638  4C 89 4C 24 30                  mov qword ptr [rsp + 0x30], r9
0079963D  44 8B C8                        mov r9d, eax
00799640  C7 44 24 28 04 00 00 00         mov dword ptr [rsp + 0x28], 4
00799648  C7 44 24 20 08 00 00 00         mov dword ptr [rsp + 0x20], 8
00799650  E8 AB D5 FF FF                  call 0x140796c00
00799655  49 8D 4E 18                     lea rcx, [r14 + 0x18]
00799659  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0079965D  33 D2                           xor edx, edx
0079965F  41 B8 C0 02 00 00               mov r8d, 0x2c0
00799665  48 8B F0                        mov rsi, rax
00799668  E8 D3 D5 F2 FF                  call 0x1406c6c40
0079966D  44 8B 7D 48                     mov r15d, dword ptr [rbp + 0x48]
00799671  41 BD 08 00 00 00               mov r13d, 8
00799677  45 33 C9                        xor r9d, r9d
0079967A  44 89 6D 70                     mov dword ptr [rbp + 0x70], r13d
0079967E  41 8B F9                        mov edi, r9d
00799681  44 89 6D 50                     mov dword ptr [rbp + 0x50], r13d
00799685  EB 04                           jmp 0x14079968b
00799687  48 8B 75 F0                     mov rsi, qword ptr [rbp - 0x10]
0079968B  41 3B FF                        cmp edi, r15d
0079968E  0F 83 F2 03 00 00               jae 0x140799a86
00799694  48 8B 0B                        mov rcx, qword ptr [rbx]
00799697  4C 8B E6                        mov r12, rsi
0079969A  48 89 75 F8                     mov qword ptr [rbp - 8], rsi
0079969E  BE 08 00 00 00                  mov esi, 8
007996A3  44 89 4D 58                     mov dword ptr [rbp + 0x58], r9d
007996A7  48 85 C9                        test rcx, rcx
007996AA  74 55                           je 0x140799701
007996AC  48 3B CE                        cmp rcx, rsi
007996AF  73 02                           jae 0x1407996b3
007996B1  8B F1                           mov esi, ecx
007996B3  39 73 10                        cmp dword ptr [rbx + 0x10], esi
007996B6  73 2E                           jae 0x1407996e6
007996B8  48 8D 4B 18                     lea rcx, [rbx + 0x18]
007996BC  41 B8 04 00 00 00               mov r8d, 4
007996C2  48 8D 55 58                     lea rdx, [rbp + 0x58]
007996C6  E8 55 0B 00 00                  call 0x14079a220
007996CB  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
007996CE  8B 55 58                        mov edx, dword ptr [rbp + 0x58]
007996D1  48 D3 E2                        shl rdx, cl
007996D4  48 09 53 08                     or qword ptr [rbx + 8], rdx
007996D8  8D 04 C1                        lea eax, [rcx + rax*8]
007996DB  3B C6                           cmp eax, esi
007996DD  89 43 10                        mov dword ptr [rbx + 0x10], eax
007996E0  0F 42 F0                        cmovb esi, eax
007996E3  45 33 C9                        xor r9d, r9d
007996E6  48 8B 13                        mov rdx, qword ptr [rbx]
007996E9  4C 8D 7B 08                     lea r15, [rbx + 8]
007996ED  8B CE                           mov ecx, esi
007996EF  B8 01 00 00 00                  mov eax, 1
007996F4  48 D3 E0                        shl rax, cl
007996F7  48 8B CA                        mov rcx, rdx
007996FA  FF C8                           dec eax
007996FC  41 23 07                        and eax, dword ptr [r15]
007996FF  EB 0A                           jmp 0x14079970b
00799701  41 8B C1                        mov eax, r9d
00799704  4C 8D 7B 08                     lea r15, [rbx + 8]
00799708  49 8B D1                        mov rdx, r9
0079970B  4C 8B 45 F0                     mov r8, qword ptr [rbp - 0x10]
0079970F  45 0F BF 04 40                  movsx r8d, word ptr [r8 + rax*2]
00799714  E9 86 00 00 00                  jmp 0x14079979f
00799719  44 89 4D 60                     mov dword ptr [rbp + 0x60], r9d
0079971D  BE 04 00 00 00                  mov esi, 4
00799722  48 85 C9                        test rcx, rcx
00799725  74 54                           je 0x14079977b
00799727  48 3B CE                        cmp rcx, rsi
0079972A  73 02                           jae 0x14079972e
0079972C  8B 33                           mov esi, dword ptr [rbx]
0079972E  39 73 10                        cmp dword ptr [rbx + 0x10], esi
00799731  73 33                           jae 0x140799766
00799733  48 8D 4B 18                     lea rcx, [rbx + 0x18]
00799737  41 B8 04 00 00 00               mov r8d, 4
0079973D  48 8D 55 60                     lea rdx, [rbp + 0x60]
00799741  E8 DA 0A 00 00                  call 0x14079a220
00799746  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
00799749  8B 55 60                        mov edx, dword ptr [rbp + 0x60]
0079974C  44 0F B7 45 58                  movzx r8d, word ptr [rbp + 0x58]
00799751  48 D3 E2                        shl rdx, cl
00799754  48 09 53 08                     or qword ptr [rbx + 8], rdx
00799758  8D 04 C1                        lea eax, [rcx + rax*8]
0079975B  3B C6                           cmp eax, esi
0079975D  89 43 10                        mov dword ptr [rbx + 0x10], eax
00799760  0F 42 F0                        cmovb esi, eax
00799763  45 33 C9                        xor r9d, r9d
00799766  8B CE                           mov ecx, esi
00799768  4C 8D 7B 08                     lea r15, [rbx + 8]
0079976C  BA 01 00 00 00                  mov edx, 1
00799771  48 D3 E2                        shl rdx, cl
00799774  FF CA                           dec edx
00799776  41 23 17                        and edx, dword ptr [r15]
00799779  EB 07                           jmp 0x140799782
0079977B  41 8B D1                        mov edx, r9d
0079977E  4C 8D 7B 08                     lea r15, [rbx + 8]
00799782  49 0F BF C0                     movsx rax, r8w
00799786  48 83 E0 F0                     and rax, 0xfffffffffffffff0
0079978A  4D 8D 24 44                     lea r12, [r12 + rax*2]
0079978E  8B C2                           mov eax, edx
00799790  48 8B 13                        mov rdx, qword ptr [rbx]
00799793  4C 89 65 F8                     mov qword ptr [rbp - 8], r12
00799797  48 8B CA                        mov rcx, rdx
0079979A  45 0F BF 04 44                  movsx r8d, word ptr [r12 + rax*2]
0079979F  41 8B F0                        mov esi, r8d
007997A2  44 89 4D 60                     mov dword ptr [rbp + 0x60], r9d
007997A6  83 E6 0F                        and esi, 0xf
007997A9  66 44 89 45 58                  mov word ptr [rbp + 0x58], r8w
007997AE  48 85 D2                        test rdx, rdx
007997B1  74 62                           je 0x140799815
007997B3  85 F6                           test esi, esi
007997B5  74 5E                           je 0x140799815
007997B7  8B C6                           mov eax, esi
007997B9  4D 8B E7                        mov r12, r15
007997BC  48 3B C2                        cmp rax, rdx
007997BF  76 06                           jbe 0x1407997c7
007997C1  8B 33                           mov esi, dword ptr [rbx]
007997C3  4C 8D 63 08                     lea r12, [rbx + 8]
007997C7  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
007997CA  3B C6                           cmp eax, esi
007997CC  73 33                           jae 0x140799801
007997CE  41 B8 04 00 00 00               mov r8d, 4
007997D4  48 8D 55 60                     lea rdx, [rbp + 0x60]
007997D8  48 8D 4B 18                     lea rcx, [rbx + 0x18]
007997DC  E8 3F 0A 00 00                  call 0x14079a220
007997E1  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
007997E4  45 33 C9                        xor r9d, r9d
007997E7  8B 55 60                        mov edx, dword ptr [rbp + 0x60]
007997EA  44 0F B7 45 58                  movzx r8d, word ptr [rbp + 0x58]
007997EF  48 D3 E2                        shl rdx, cl
007997F2  49 09 17                        or qword ptr [r15], rdx
007997F5  8D 04 C1                        lea eax, [rcx + rax*8]
007997F8  3B C6                           cmp eax, esi
007997FA  73 05                           jae 0x140799801
007997FC  4D 8B FC                        mov r15, r12
007997FF  8B F0                           mov esi, eax
00799801  4C 8B 65 F8                     mov r12, qword ptr [rbp - 8]
00799805  8B CE                           mov ecx, esi
00799807  49 D3 2F                        shr qword ptr [r15], cl
0079980A  48 29 0B                        sub qword ptr [rbx], rcx
0079980D  48 8B 0B                        mov rcx, qword ptr [rbx]
00799810  2B C6                           sub eax, esi
00799812  89 43 10                        mov dword ptr [rbx + 0x10], eax
00799815  66 45 85 C0                     test r8w, r8w
00799819  0F 88 FA FE FF FF               js 0x140799719
0079981F  41 0F B7 D0                     movzx edx, r8w
00799823  C1 EA 04                        shr edx, 4
00799826  8B C2                           mov eax, edx
00799828  83 E8 1C                        sub eax, 0x1c
0079982B  0F 84 1F 02 00 00               je 0x140799a50
00799831  83 E8 01                        sub eax, 1
00799834  0F 84 CA 00 00 00               je 0x140799904
0079983A  83 E8 01                        sub eax, 1
0079983D  0F 84 B5 00 00 00               je 0x1407998f8
00799843  83 E8 01                        sub eax, 1
00799846  0F 84 86 00 00 00               je 0x1407998d2
0079984C  83 F8 01                        cmp eax, 1
0079984F  74 42                           je 0x140799893
00799851  83 FA 1B                        cmp edx, 0x1b
00799854  0F 87 E8 02 00 00               ja 0x140799b42
0079985A  8B 4D 50                        mov ecx, dword ptr [rbp + 0x50]
0079985D  85 D2                           test edx, edx
0079985F  8B C7                           mov eax, edi
00799861  0F 45 CA                        cmovne ecx, edx
00799864  89 4D 50                        mov dword ptr [rbp + 0x50], ecx
00799867  42 88 54 30 18                  mov byte ptr [rax + r14 + 0x18], dl
0079986C  84 D2                           test dl, dl
0079986E  74 0A                           je 0x14079987a
00799870  0F B6 C2                        movzx eax, dl
00799873  41 3B C5                        cmp eax, r13d
00799876  44 0F 42 E8                     cmovb r13d, eax
0079987A  0F B6 C2                        movzx eax, dl
0079987D  8B 55 70                        mov edx, dword ptr [rbp + 0x70]
00799880  3B C2                           cmp eax, edx
00799882  0F 47 D0                        cmova edx, eax
00799885  89 55 70                        mov dword ptr [rbp + 0x70], edx
00799888  44 8B 7D 48                     mov r15d, dword ptr [rbp + 0x48]
0079988C  FF C7                           inc edi
0079988E  E9 F4 FD FF FF                  jmp 0x140799687
00799893  83 FF 10                        cmp edi, 0x10
00799896  0F 82 A6 02 00 00               jb 0x140799b42
0079989C  8D 47 F0                        lea eax, [rdi - 0x10]
0079989F  42 8A 54 30 18                  mov dl, byte ptr [rax + r14 + 0x18]
007998A4  FE C2                           inc dl
007998A6  8B C7                           mov eax, edi
007998A8  42 88 54 30 18                  mov byte ptr [rax + r14 + 0x18], dl
007998AD  8D 42 FF                        lea eax, [rdx - 1]
007998B0  3C 1A                           cmp al, 0x1a
007998B2  0F 87 8A 02 00 00               ja 0x140799b42
007998B8  8B 45 70                        mov eax, dword ptr [rbp + 0x70]
007998BB  0F B6 CA                        movzx ecx, dl
007998BE  41 3B CD                        cmp ecx, r13d
007998C1  89 4D 50                        mov dword ptr [rbp + 0x50], ecx
007998C4  44 0F 42 E9                     cmovb r13d, ecx
007998C8  3B C8                           cmp ecx, eax
007998CA  0F 47 C1                        cmova eax, ecx
007998CD  89 45 70                        mov dword ptr [rbp + 0x70], eax
007998D0  EB B6                           jmp 0x140799888
007998D2  83 FF 10                        cmp edi, 0x10
007998D5  0F 82 67 02 00 00               jb 0x140799b42
007998DB  8B D7                           mov edx, edi
007998DD  8D 47 F0                        lea eax, [rdi - 0x10]
007998E0  42 0F B6 44 30 18               movzx eax, byte ptr [rax + r14 + 0x18]
007998E6  42 88 44 32 18                  mov byte ptr [rdx + r14 + 0x18], al
007998EB  84 C0                           test al, al
007998ED  0F 84 4F 02 00 00               je 0x140799b42
007998F3  89 45 50                        mov dword ptr [rbp + 0x50], eax
007998F6  EB 90                           jmp 0x140799888
007998F8  8B 4D 50                        mov ecx, dword ptr [rbp + 0x50]
007998FB  8B C7                           mov eax, edi
007998FD  42 88 4C 30 18                  mov byte ptr [rax + r14 + 0x18], cl
00799902  EB 84                           jmp 0x140799888
00799904  44 89 4D 58                     mov dword ptr [rbp + 0x58], r9d
00799908  BE 02 00 00 00                  mov esi, 2
0079990D  48 85 C9                        test rcx, rcx
00799910  0F 84 2C 02 00 00               je 0x140799b42
00799916  48 3B CE                        cmp rcx, rsi
00799919  73 02                           jae 0x14079991d
0079991B  8B 33                           mov esi, dword ptr [rbx]
0079991D  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
00799920  3B C6                           cmp eax, esi
00799922  73 2C                           jae 0x140799950
00799924  48 8D 4B 18                     lea rcx, [rbx + 0x18]
00799928  41 B8 04 00 00 00               mov r8d, 4
0079992E  48 8D 55 58                     lea rdx, [rbp + 0x58]
00799932  E8 E9 08 00 00                  call 0x14079a220
00799937  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
0079993A  45 33 C9                        xor r9d, r9d
0079993D  8B 55 58                        mov edx, dword ptr [rbp + 0x58]
00799940  48 D3 E2                        shl rdx, cl
00799943  48 09 53 08                     or qword ptr [rbx + 8], rdx
00799947  8D 04 C1                        lea eax, [rcx + rax*8]
0079994A  3B C6                           cmp eax, esi
0079994C  73 02                           jae 0x140799950
0079994E  8B F0                           mov esi, eax
00799950  8B CE                           mov ecx, esi
00799952  2B C6                           sub eax, esi
00799954  BA 01 00 00 00                  mov edx, 1
00799959  89 43 10                        mov dword ptr [rbx + 0x10], eax
0079995C  48 D3 E2                        shl rdx, cl
0079995F  8B CE                           mov ecx, esi
00799961  FF CA                           dec edx
00799963  23 53 08                        and edx, dword ptr [rbx + 8]
00799966  48 D3 6B 08                     shr qword ptr [rbx + 8], cl
0079996A  48 29 0B                        sub qword ptr [rbx], rcx
0079996D  48 8B 0B                        mov rcx, qword ptr [rbx]
00799970  83 FE 02                        cmp esi, 2
00799973  0F 82 C9 01 00 00               jb 0x140799b42
00799979  8D 72 05                        lea esi, [rdx + 5]
0079997C  83 FA 03                        cmp edx, 3
0079997F  0F 85 91 00 00 00               jne 0x140799a16
00799985  BA 07 00 00 00                  mov edx, 7
0079998A  83 FA 07                        cmp edx, 7
0079998D  0F 85 83 00 00 00               jne 0x140799a16
00799993  44 89 4D 58                     mov dword ptr [rbp + 0x58], r9d
00799997  44 8D 7A FC                     lea r15d, [rdx - 4]
0079999B  48 85 C9                        test rcx, rcx
0079999E  0F 84 9E 01 00 00               je 0x140799b42
007999A4  49 3B CF                        cmp rcx, r15
007999A7  73 03                           jae 0x1407999ac
007999A9  44 8B 3B                        mov r15d, dword ptr [rbx]
007999AC  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
007999AF  41 3B C7                        cmp eax, r15d
007999B2  73 2E                           jae 0x1407999e2
007999B4  48 8D 4B 18                     lea rcx, [rbx + 0x18]
007999B8  41 B8 04 00 00 00               mov r8d, 4
007999BE  48 8D 55 58                     lea rdx, [rbp + 0x58]
007999C2  E8 59 08 00 00                  call 0x14079a220
007999C7  8B 4B 10                        mov ecx, dword ptr [rbx + 0x10]
007999CA  45 33 C9                        xor r9d, r9d
007999CD  8B 55 58                        mov edx, dword ptr [rbp + 0x58]
007999D0  48 D3 E2                        shl rdx, cl
007999D3  48 09 53 08                     or qword ptr [rbx + 8], rdx
007999D7  8D 04 C1                        lea eax, [rcx + rax*8]
007999DA  41 3B C7                        cmp eax, r15d
007999DD  73 03                           jae 0x1407999e2
007999DF  44 8B F8                        mov r15d, eax
007999E2  41 8B CF                        mov ecx, r15d
007999E5  41 2B C7                        sub eax, r15d
007999E8  BA 01 00 00 00                  mov edx, 1
007999ED  89 43 10                        mov dword ptr [rbx + 0x10], eax
007999F0  48 D3 E2                        shl rdx, cl
007999F3  41 8B CF                        mov ecx, r15d
007999F6  FF CA                           dec edx
007999F8  23 53 08                        and edx, dword ptr [rbx + 8]
007999FB  48 D3 6B 08                     shr qword ptr [rbx + 8], cl
007999FF  48 29 0B                        sub qword ptr [rbx], rcx
00799A02  48 8B 0B                        mov rcx, qword ptr [rbx]
00799A05  41 83 FF 03                     cmp r15d, 3
00799A09  0F 82 33 01 00 00               jb 0x140799b42
00799A0F  03 F2                           add esi, edx
00799A11  E9 74 FF FF FF                  jmp 0x14079998a
00799A16  44 8B 7D 48                     mov r15d, dword ptr [rbp + 0x48]
00799A1A  8D 04 3E                        lea eax, [rsi + rdi]
00799A1D  41 3B C7                        cmp eax, r15d
00799A20  0F 87 1C 01 00 00               ja 0x140799b42
00799A26  85 F6                           test esi, esi
00799A28  0F 84 59 FC FF FF               je 0x140799687
00799A2E  8B CF                           mov ecx, edi
00799A30  33 D2                           xor edx, edx
00799A32  48 83 C1 18                     add rcx, 0x18
00799A36  44 8B C6                        mov r8d, esi
00799A39  49 03 CE                        add rcx, r14
00799A3C  E8 FF D1 F2 FF                  call 0x1406c6c40
00799A41  FF C7                           inc edi
00799A43  83 C6 FF                        add esi, -1
00799A46  75 F9                           jne 0x140799a41
00799A48  45 33 C9                        xor r9d, r9d
00799A4B  E9 37 FC FF FF                  jmp 0x140799687
00799A50  44 8B 7D 48                     mov r15d, dword ptr [rbp + 0x48]
00799A54  48 8B 75 F0                     mov rsi, qword ptr [rbp - 0x10]
00799A58  8B C7                           mov eax, edi
00799A5A  FF C7                           inc edi
00799A5C  46 88 4C 30 18                  mov byte ptr [rax + r14 + 0x18], r9b
00799A61  40 F6 C7 0F                     test dil, 0xf
00799A65  0F 84 20 FC FF FF               je 0x14079968b
00799A6B  48 8B 75 F0                     mov rsi, qword ptr [rbp - 0x10]
00799A6F  41 3B FF                        cmp edi, r15d
00799A72  73 12                           jae 0x140799a86
00799A74  46 88 4C 37 18                  mov byte ptr [rdi + r14 + 0x18], r9b
00799A79  FF C7                           inc edi
00799A7B  40 F6 C7 0F                     test dil, 0xf
00799A7F  75 EA                           jne 0x140799a6b
00799A81  E9 05 FC FF FF                  jmp 0x14079968b
00799A86  8B 55 70                        mov edx, dword ptr [rbp + 0x70]
00799A89  49 8D 76 18                     lea rsi, [r14 + 0x18]
00799A8D  EB 54                           jmp 0x140799ae3
00799A8F  B8 02 00 00 C0                  mov eax, 0xc0000002
00799A94  E9 AE 00 00 00                  jmp 0x140799b47
00799A99  45 0F BD EF                     bsr r13d, r15d
00799A9D  41 8B DC                        mov ebx, r12d
00799AA0  41 8B D0                        mov edx, r8d
00799AA3  41 8D 4D 01                     lea ecx, [r13 + 1]
00799AA7  D3 E3                           shl ebx, cl
00799AA9  41 2B DF                        sub ebx, r15d
00799AAC  74 10                           je 0x140799abe
00799AAE  44 8B C3                        mov r8d, ebx
00799AB1  41 8A D5                        mov dl, r13b
00799AB4  48 8B CE                        mov rcx, rsi
00799AB7  E8 84 D1 F2 FF                  call 0x1406c6c40
00799ABC  8B D3                           mov edx, ebx
00799ABE  41 3B D7                        cmp edx, r15d
00799AC1  73 1C                           jae 0x140799adf
00799AC3  8B CA                           mov ecx, edx
00799AC5  45 8B C7                        mov r8d, r15d
00799AC8  48 83 C1 18                     add rcx, 0x18
00799ACC  44 2B C2                        sub r8d, edx
00799ACF  49 03 CE                        add rcx, r14
00799AD2  43 8D 14 2C                     lea edx, [r12 + r13]
00799AD6  E8 65 D1 F2 FF                  call 0x1406c6c40
00799ADB  49 8D 76 18                     lea rsi, [r14 + 0x18]
00799ADF  41 8D 55 01                     lea edx, [r13 + 1]
00799AE3  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
00799AE7  49 8D 9E D8 02 00 00            lea rbx, [r14 + 0x2d8]
00799AEE  48 8B D3                        mov rdx, rbx
00799AF1  49 8D 4E 18                     lea rcx, [r14 + 0x18]
00799AF5  45 8B CD                        mov r9d, r13d
00799AF8  45 8B C7                        mov r8d, r15d
00799AFB  E8 A4 07 00 00                  call 0x14079a2a4
00799B00  85 C0                           test eax, eax
00799B02  74 3E                           je 0x140799b42
00799B04  48 8B 4D 68                     mov rcx, qword ptr [rbp + 0x68]
00799B08  49 8D 96 58 92 00 00            lea rdx, [r14 + 0x9258]
00799B0F  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00799B14  44 8B C8                        mov r9d, eax
00799B17  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00799B1C  4C 8B C3                        mov r8, rbx
00799B1F  C7 44 24 28 06 00 00 00         mov dword ptr [rsp + 0x28], 6
00799B27  48 8B CE                        mov rcx, rsi
00799B2A  C7 44 24 20 0C 00 00 00         mov dword ptr [rsp + 0x20], 0xc
00799B32  E8 C9 D0 FF FF                  call 0x140796c00
00799B37  48 8B 4D 78                     mov rcx, qword ptr [rbp + 0x78]
00799B3B  48 89 01                        mov qword ptr [rcx], rax
00799B3E  33 C0                           xor eax, eax
00799B40  EB 05                           jmp 0x140799b47
00799B42  B8 42 02 00 C0                  mov eax, 0xc0000242
00799B47  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
00799B4F  48 83 C4 60                     add rsp, 0x60
00799B53  41 5F                           pop r15
00799B55  41 5E                           pop r14
00799B57  41 5D                           pop r13
00799B59  41 5C                           pop r12
00799B5B  5F                              pop rdi
00799B5C  5E                              pop rsi
00799B5D  5D                              pop rbp
00799B5E  C3                              ret
00799B5F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Xp10ReadAndDecodeHuffmanTables(__int64 a1, int a2, int a3, int a4, unsigned int a5, __int64 a6, unsigned int a7, __int64 a8)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned int v_stack_m78;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (96);
    a1 = 0;
    v_stack_p20 = 0;
    if (*(unsigned __int64 *)(a5) == 0) goto loc_00799B42;
    v_rsi = 2;
    if ((*(unsigned __int64 *)(a5)) < 2) {
        v_rsi = (unsigned int)(*(unsigned __int64 *)(a5));
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 16)))) >= ((unsigned int)(v_rsi))) goto loc_0079944F;
    result = Xp10ScatteredReadBytes(a5 + 24, v_stack_p20, 4, a4);
    a2 = ((unsigned int)(v_stack_p20)) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a5 + 16))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 16)) + result * 8)) < ((unsigned int)(v_rsi))) {
        v_rsi = (unsigned int)((unsigned int)(*(unsigned int *)(a5 + 16)) + result * 8);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a5 + 16)) + result * 8) - ((unsigned int)(v_rsi)));
    v_rdi = (1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rsi))));
    v_rdi = (unsigned int)((v_rdi) - (1));
    v_rdi = (unsigned int)((v_rdi) & (*(unsigned int *)(a5 + 8)));
    *(unsigned int *)(a5 + 16) = (unsigned int)(result);
    if (((unsigned int)(v_rsi)) < 2) goto loc_00799B42;
    a2 = 0;
    result = memset(a1 + 24, a2, 704, a4);
    a3 = 0;
    if ((unsigned int)(v_rdi) == 0) goto loc_00799A99;
    v_rdi = (unsigned int)((v_rdi) - (1));
    if (condition_is_equal) goto loc_00799A8F;
    if (((unsigned int)(v_rdi)) != 1) goto loc_00799B42;
loc_007994B9:
    if (0 >= 33) goto loc_007995F5;
    v_stack_p20 = 0;
    if (*(unsigned __int64 *)(a5) == 0) goto loc_00799B42;
    v_rdi = 1;
    if ((*(unsigned __int64 *)(a5)) < 1) {
        v_rdi = (unsigned int)(*(unsigned __int64 *)(a5));
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 16)))) >= ((unsigned int)(v_rdi))) goto loc_00799511;
    result = Xp10ScatteredReadBytes(a5 + 24, v_stack_p20, 4, a4);
    a3 = 0;
    a2 = ((unsigned int)(v_stack_p20)) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a5 + 16))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 16)) + result * 8)) < ((unsigned int)(v_rdi))) {
        v_rdi = (unsigned int)((unsigned int)(*(unsigned int *)(a5 + 16)) + result * 8);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a5 + 16)) + result * 8) - ((unsigned int)(v_rdi)));
    *(unsigned int *)(a5 + 16) = (unsigned int)(result);
    a2 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi))));
    a2 = (unsigned int)((a2) - 1);
    a2 = (unsigned int)((a2) & (*(unsigned int *)(a5 + 8)));
    if (((unsigned int)(v_rdi)) < 1) goto loc_00799B42;
    if (a2 == 0) goto loc_007995E7;
    if (a2 != 1) goto loc_00799B42;
    v_stack_p20 = 0;
    if (*(unsigned __int64 *)(a5) == 0) goto loc_00799B42;
    v_rdi = a2 + 2;
    if ((*(unsigned __int64 *)(a5)) < (a2 + 2)) {
        v_rdi = (unsigned int)(*(unsigned __int64 *)(a5));
    }
    if (((unsigned int)(result)) >= ((unsigned int)(v_rdi))) goto loc_00799592;
    result = Xp10ScatteredReadBytes(a5 + 24, v_stack_p20, 4, a4);
    a3 = 0;
    a2 = ((unsigned int)(v_stack_p20)) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a5 + 16))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 16)) + result * 8)) < ((unsigned int)(v_rdi))) {
        v_rdi = (unsigned int)((unsigned int)(*(unsigned int *)(a5 + 16)) + result * 8);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a5 + 16)) + result * 8) - ((unsigned int)(v_rdi)));
    *(unsigned int *)(a5 + 16) = (unsigned int)(result);
    a2 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rdi))));
    a2 = (unsigned int)((a2) - 1);
    a2 = (unsigned int)((a2) & (*(unsigned int *)(a5 + 8)));
    if (((unsigned int)(v_rdi)) < 3) goto loc_00799B42;
    if (a2 < ((unsigned int)((unsigned int)((unsigned int)(1 + 3))))) goto loc_007995C8;
    a2 = (unsigned int)((a2) + 1);
    if (a2 > 8) goto loc_00799B42;
loc_007995C8:
    *(unsigned __int8 *)(0 + a1 * 1 + 24) = (unsigned __int8)(a2);
    v_r15 = 1 + 3;
    if (a2 != 0) {
        v_r15 = 1 + 3;
        if (a2 < ((unsigned int)(1 + 3))) { v_r15 = a2; }
    }
    if (a2 <= ((unsigned int)((unsigned int)((unsigned int)(1 + 3))))) goto loc_007995EE;
    goto loc_007995EE;
loc_007995E7:
    *(unsigned __int8 *)(0 + a1 * 1 + 24) = (unsigned __int8)((unsigned int)(a2));
loc_007995EE:
    v_rsi = (unsigned int)((0) + 1);
    goto loc_007994B9;
loc_007995F5:
    v_stack_m78 = (unsigned int)((unsigned int)(a2));
    result = Xp10SortHuffmanSymbols(a1 + 24, a1 + 728, 33, (unsigned int)((unsigned int)(v_r15)));
    if ((unsigned int)(result) == 0) goto loc_00799B42;
    v_stack_m58 = a1 + 2136;
    v_stack_m68 = a1 + 37464;
    v_stack_m70 = 4;
    v_stack_m78 = 8;
    result = Xp10BuildHuffmanDecodeTable(a1 + 24, a1 + 2136, a1 + 728, (unsigned int)((unsigned int)(result)));
    v_stack_m48 = result;
    a2 = 0;
    result = memset(a1 + 24, a2, 704, (unsigned int)((unsigned int)(result)));
    a4 = 0;
    v_stack_p38 = 8;
    v_stack_p18 = 8;
    goto loc_0079968B;
loc_00799687:
loc_0079968B:
    if (0 >= ((unsigned int)((unsigned int)(v_stack_p10)))) goto loc_00799A86;
    v_stack_m40 = v_stack_m48;
    v_stack_p20 = 0;
    if (*(unsigned __int64 *)(a5) == 0) goto loc_00799701;
    v_rsi = 8;
    if ((*(unsigned __int64 *)(a5)) < 8) {
        v_rsi = (unsigned int)(*(unsigned __int64 *)(a5));
    }
    if ((*(unsigned int *)(a5 + 16)) < ((unsigned int)(v_rsi))) {
        a1 = a5 + 24;
        a3 = 4;
        a2 = v_stack_p20;
        result = Xp10ScatteredReadBytes(a1, a2, a3, a4);
        a1 = *(unsigned int *)(a5 + 16);
        a2 = v_stack_p20;
        a2 = (a2) << ((unsigned __int8)(a1));
        result = a1 + result * 8;
        *(unsigned int *)(a5 + 16) = (unsigned int)(result);
        if (((unsigned int)(result)) < ((unsigned int)(v_rsi))) { v_rsi = (unsigned int)(result); }
        a4 = 0;
    }
    result = (1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rsi))));
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) & (*(unsigned int *)(a5 + 8)));
    goto loc_0079970B;
loc_00799701:
loc_0079970B:
    goto loc_0079979F;
loc_00799719:
    v_stack_p28 = 0;
    if (*(unsigned __int64 *)(a5) == 0) goto loc_0079977B;
    v_rsi = 4;
    if ((*(unsigned __int64 *)(a5)) < 4) {
        v_rsi = *(unsigned int *)(a5);
    }
    result = 0;
    if ((*(unsigned int *)(a5 + 16)) < ((unsigned int)(v_rsi))) {
        a1 = a5 + 24;
        a3 = 4;
        a2 = a5;
        result = Xp10ScatteredReadBytes(a1, a2, a3, a4);
        a1 = *(unsigned int *)(a5 + 16);
        a2 = a5;
        a3 = v_stack_p20;
        a2 = (a2) << ((unsigned __int8)(a1));
        result = a1 + result * 8;
        *(unsigned int *)(a5 + 16) = (unsigned int)(result);
        if (((unsigned int)(result)) < ((unsigned int)(v_rsi))) { v_rsi = (unsigned int)(result); }
        a4 = 0;
    }
    a2 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rsi))));
    a2 = (unsigned int)((a2) - 1);
    a2 = (unsigned int)((a2) & (*(unsigned int *)(a5 + 8)));
    goto loc_00799782;
loc_0079977B:
loc_00799782:
    result = ((__int16)((unsigned __int16)(a3))) & (-16);
    v_stack_m40 = v_stack_m48 + result * 2;
loc_0079979F:
    v_stack_p28 = 0;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((__int16)(*(unsigned __int16 *)(v_stack_m48 + result * 2 + 0 * 2))))) & (15));
    v_stack_p20 = (unsigned __int16)((__int16)(*(unsigned __int16 *)(v_stack_m48 + result * 2 + 0 * 2)));
    if (*(unsigned __int64 *)(a5) == 0) goto loc_00799815;
    if ((unsigned int)(v_rsi) == 0) goto loc_00799815;
    v_r12 = a5 + 8;
    if (((unsigned int)((unsigned int)(v_rsi))) >= = (*(unsigned __int64 *)(a5))) {
        v_rsi = *(unsigned int *)(a5);
        v_r12 = a5 + 8;
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 16)))) >= ((unsigned int)(v_rsi))) goto loc_00799801;
    result = Xp10ScatteredReadBytes(a5 + 24, a5, 4, a4);
    a4 = 0;
    a2 = ((unsigned int)(a5)) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a5 + 16))));
    v_r15 = a5 + 8;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 16)) + result * 8)) < ((unsigned int)(v_rsi))) {
        v_r15 = v_r12;
        v_rsi = (unsigned int)((unsigned int)(*(unsigned int *)(a5 + 16)) + result * 8);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a5 + 16)) + result * 8) - ((unsigned int)(v_rsi)));
    *(unsigned int *)(a5 + 16) = (unsigned int)(result);
loc_00799815:
    if (sign_flag) goto loc_00799719;
    a2 = (unsigned int)(((unsigned __int16)(v_stack_p20)) >> (4));
    result = (unsigned int)(((unsigned int)(a2)) - (28));
    if (condition_is_equal) goto loc_00799A50;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_00799904;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_007998F8;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_007998D2;
    if (((unsigned int)(result)) == 1) goto loc_00799893;
    if (a2 > 27) goto loc_00799B42;
    a1 = (unsigned int)(v_stack_p18);
    if (a2 != 0) { a1 = a2; }
    v_stack_p18 = (unsigned int)(a1);
    *(unsigned __int8 *)(0 + a1 * 1 + 24) = (unsigned __int8)(a2);
    result = 0;
    v_r13 = 8;
    if ((unsigned __int8)(a2) != 0) {
        result = (unsigned __int8)(a2);
        v_r13 = 8;
        if (((unsigned int)(result)) < 8) { v_r13 = (unsigned int)(result); }
    }
    a2 = (unsigned int)(a7);
    if (((unsigned int)((unsigned __int8)(a2))) > ((unsigned int)((unsigned int)(a7)))) { a2 = (unsigned int)((unsigned __int8)(a2)); }
    v_stack_p38 = a2;
loc_00799888:
    v_rdi = (unsigned int)((0) + 1);
    goto loc_00799687;
loc_00799893:
    if (((unsigned int)(v_rdi)) < 16) goto loc_00799B42;
    a2 = (unsigned __int8)((*(unsigned __int8 *)(v_rdi - 16 + a1 * 1 + 24)) + 1);
    *(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + a1 * 1 + 24) = (unsigned __int8)(a2);
    if (((unsigned __int8)(a2 - 1)) > 26) goto loc_00799B42;
    v_stack_p18 = (unsigned int)((unsigned __int8)(a2));
    if (((unsigned int)((unsigned __int8)(a2))) < ((unsigned int)(v_r13))) { v_r13 = (unsigned int)((unsigned __int8)(a2)); }
    result = (unsigned int)(a7);
    if (((unsigned int)((unsigned __int8)(a2))) > ((unsigned int)((unsigned int)(a7)))) { result = (unsigned int)((unsigned __int8)(a2)); }
    v_stack_p38 = (unsigned int)(result);
    goto loc_00799888;
loc_007998D2:
    if (((unsigned int)(v_rdi)) < 16) goto loc_00799B42;
    *(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + a1 * 1 + 24) = (unsigned __int8)(*(unsigned __int8 *)(v_rdi - 16 + a1 * 1 + 24));
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rdi - 16 + a1 * 1 + 24)) == 0) goto loc_00799B42;
    v_stack_p18 = (unsigned int)(*(unsigned __int8 *)(v_rdi - 16 + a1 * 1 + 24));
    goto loc_00799888;
loc_007998F8:
    *(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + a1 * 1 + 24) = (unsigned __int8)((unsigned int)(v_stack_p18));
    goto loc_00799888;
loc_00799904:
    v_stack_p20 = 0;
    if ((unsigned int)(v_stack_p18) == 0) goto loc_00799B42;
    v_rsi = 2;
    if (((unsigned int)(v_stack_p18)) < 2) {
        v_rsi = *(unsigned int *)(a5);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 16)))) >= ((unsigned int)(v_rsi))) goto loc_00799950;
    result = Xp10ScatteredReadBytes(a5 + 24, v_stack_p20, 4, a4);
    a4 = 0;
    a2 = ((unsigned int)(v_stack_p20)) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a5 + 16))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 16)) + result * 8)) < ((unsigned int)(v_rsi))) {
        v_rsi = (unsigned int)((unsigned int)(*(unsigned int *)(a5 + 16)) + result * 8);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a5 + 16)) + result * 8) - ((unsigned int)(v_rsi)));
    *(unsigned int *)(a5 + 16) = (unsigned int)(result);
    a2 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_rsi))));
    a2 = (unsigned int)((a2) - 1);
    a2 = (unsigned int)((a2) & (*(unsigned int *)(a5 + 8)));
    if (((unsigned int)(v_rsi)) < 2) goto loc_00799B42;
    if (a2 != 3) goto loc_00799A16;
loc_0079998A:
    if (7 != 7) goto loc_00799A16;
    v_stack_p20 = 0;
    if (*(unsigned __int64 *)(a5) == 0) goto loc_00799B42;
    v_r15 = 7 - 4;
    if ((*(unsigned __int64 *)(a5)) < (7 - 4)) {
        v_r15 = *(unsigned int *)(a5);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 16)))) >= ((unsigned int)(v_r15))) goto loc_007999E2;
    result = Xp10ScatteredReadBytes(a5 + 24, v_stack_p20, 4, a4);
    a4 = 0;
    a2 = ((unsigned int)(v_stack_p20)) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a5 + 16))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a5 + 16)) + result * 8)) < ((unsigned int)(v_r15))) {
        v_r15 = (unsigned int)((unsigned int)(*(unsigned int *)(a5 + 16)) + result * 8);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a5 + 16)) + result * 8) - ((unsigned int)(v_r15)));
    *(unsigned int *)(a5 + 16) = (unsigned int)(result);
    a2 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r15))));
    a2 = (unsigned int)((a2) - 1);
    a2 = (unsigned int)((a2) & (*(unsigned int *)(a5 + 8)));
    if (((unsigned int)(v_r15)) < 3) goto loc_00799B42;
    v_rsi = (unsigned int)((a2 + 5) + (a2));
    goto loc_0079998A;
loc_00799A16:
    if (((unsigned int)(v_rsi + v_rdi * 1)) > ((unsigned int)((unsigned int)(v_stack_p10)))) goto loc_00799B42;
    if ((unsigned int)(v_rsi) == 0) goto loc_00799687;
    a2 = 0;
    a1 = ((unsigned int)((unsigned int)(v_rdi))) + (24);
    a1 = (a1) + (a1);
    result = memset(a1, a2, (unsigned int)((unsigned int)(v_rsi)), a4);
loc_00799A41:
    v_rdi = (unsigned int)((v_rdi) + 1);
    v_rsi = (unsigned int)((v_rsi) + (-1));
    if (condition_is_not_equal) goto loc_00799A41;
    a4 = 0;
    goto loc_00799687;
loc_00799A50:
    v_rdi = (unsigned int)((v_rdi) + 1);
    *(unsigned __int8 *)((unsigned int)((unsigned int)(v_rdi)) + a1 * 1 + 24) = 0;
    if ((((unsigned __int8)(v_rdi)) & (15)) == 0) goto loc_0079968B;
loc_00799A6B:
    if (((unsigned int)(v_rdi)) >= ((unsigned int)((unsigned int)(v_stack_p10)))) goto loc_00799A86;
    *(unsigned __int8 *)(v_rdi + a1 * 1 + 24) = 0;
    v_rdi = (unsigned int)((v_rdi) + 1);
    if ((((unsigned __int8)(v_rdi)) & (15)) != 0) goto loc_00799A6B;
    goto loc_0079968B;
loc_00799A86:
    goto loc_00799AE3;
loc_00799A8F:
    goto loc_00799B47;
loc_00799A99:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m40))) << ((unsigned __int8)(v_r13 + 1)));
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)((unsigned int)(v_stack_p10))));
    result = (unsigned int)(0xC0000002ULL);
    if (!(condition_is_equal)) {
        a3 = (unsigned int)(v_rbx);
        a2 = (unsigned __int8)(v_r13);
        a1 = a1 + 24;
        result = memset(a1, a2, a3, a4);
        a2 = (unsigned int)(v_rbx);
    }
    v_rsi = a1 + 24;
    if (a2 < ((unsigned int)((unsigned int)(v_stack_p10)))) {
        a1 = a2;
        a3 = (unsigned int)((unsigned int)(v_stack_p10));
        a1 = (a1) + (24);
        a3 = (unsigned int)((a3) - (a2));
        a1 = (a1) + (a1);
        a2 = v_stack_m40 + v_r13 * 1;
        result = memset(a1, a2, a3, a4);
        v_rsi = a1 + 24;
    }
loc_00799AE3:
    v_stack_m78 = (unsigned int)(v_r13 + 1);
    result = Xp10SortHuffmanSymbols(a1 + 24, a1 + 728, (unsigned int)((unsigned int)((unsigned int)(v_stack_p10))), (unsigned int)((unsigned int)(v_r13)));
    if ((unsigned int)(result) == 0) goto loc_00799B42;
    v_stack_m58 = a6;
    v_stack_m68 = a1 + 37464;
    v_stack_m70 = 6;
    v_stack_m78 = 12;
    result = Xp10BuildHuffmanDecodeTable(v_rsi, a1 + 37464, a1 + 728, (unsigned int)((unsigned int)(result)));
    *(unsigned __int64 *)(a8) = result;
    result = 0;
    goto loc_00799B47;
loc_00799B42:
loc_00799B47:
    v_rsp = (v_rsp) + (96);
    return (unsigned int)(0xC0000242ULL);
}
```

## 5. (Beta) C Style

```c
int64_t Xp10ReadAndDecodeHuffmanTables(void *Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4, void *Arg5, int64_t Arg6, uint32_t Arg7, void *Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint32_t v_stack_m78;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p38;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (96);
    Arg1 = 0;
    v_stack_p20 = 0;
    if (*(uint64_t *)(arg5) == 0) goto loc_00799B42;
    local_rsi = 2;
    if ((*(uint64_t *)(arg5)) < 2) {
        local_rsi = (uint32_t)(*(uint64_t *)(arg5));
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10)))) >= ((uint32_t)(local_rsi))) goto loc_0079944F;
    result = Xp10ScatteredReadBytes(Arg5 + 24, v_stack_p20, 4, Arg4);
    Arg2 = ((uint32_t)(v_stack_p20)) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10)) + result * 8)) < ((uint32_t)(local_rsi))) {
        local_rsi = (uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10)) + result * 8);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg5 + 0x10)) + result * 8) - ((uint32_t)(local_rsi)));
    local_rdi = (1) << ((uint8_t)((uint32_t)((uint32_t)(local_rsi))));
    local_rdi = (uint32_t)((local_rdi) - (1));
    local_rdi = (uint32_t)((local_rdi) & (*(uint32_t *)(arg5 + 0x8)));
    *(uint32_t *)(arg5 + 0x10) = (uint32_t)(result);
    if (((uint32_t)(local_rsi)) < 2) goto loc_00799B42;
    Arg2 = 0;
    result = memset(Arg1 + 24, Arg2, 704, Arg4);
    Arg3 = 0;
    if ((uint32_t)(local_rdi) == 0) goto loc_00799A99;
    local_rdi = (uint32_t)((local_rdi) - (1));
    if (condition_is_equal) goto loc_00799A8F;
    if (((uint32_t)(local_rdi)) != 1) goto loc_00799B42;
loc_007994B9:
    if (0 >= 33) goto loc_007995F5;
    v_stack_p20 = 0;
    if (*(uint64_t *)(arg5) == 0) goto loc_00799B42;
    local_rdi = 1;
    if ((*(uint64_t *)(arg5)) < 1) {
        local_rdi = (uint32_t)(*(uint64_t *)(arg5));
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10)))) >= ((uint32_t)(local_rdi))) goto loc_00799511;
    result = Xp10ScatteredReadBytes(Arg5 + 24, v_stack_p20, 4, Arg4);
    Arg3 = 0;
    Arg2 = ((uint32_t)(v_stack_p20)) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10)) + result * 8)) < ((uint32_t)(local_rdi))) {
        local_rdi = (uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10)) + result * 8);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg5 + 0x10)) + result * 8) - ((uint32_t)(local_rdi)));
    *(uint32_t *)(arg5 + 0x10) = (uint32_t)(result);
    Arg2 = (1) << ((uint8_t)((uint32_t)((uint32_t)(local_rdi))));
    Arg2 = (uint32_t)((Arg2) - 1);
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(arg5 + 0x8)));
    if (((uint32_t)(local_rdi)) < 1) goto loc_00799B42;
    if (Arg2 == 0) goto loc_007995E7;
    if (Arg2 != 1) goto loc_00799B42;
    v_stack_p20 = 0;
    if (*(uint64_t *)(arg5) == 0) goto loc_00799B42;
    local_rdi = Arg2 + 2;
    if ((*(uint64_t *)(arg5)) < (Arg2 + 2)) {
        local_rdi = (uint32_t)(*(uint64_t *)(arg5));
    }
    if (((uint32_t)(result)) >= ((uint32_t)(local_rdi))) goto loc_00799592;
    result = Xp10ScatteredReadBytes(Arg5 + 24, v_stack_p20, 4, Arg4);
    Arg3 = 0;
    Arg2 = ((uint32_t)(v_stack_p20)) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10)) + result * 8)) < ((uint32_t)(local_rdi))) {
        local_rdi = (uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10)) + result * 8);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg5 + 0x10)) + result * 8) - ((uint32_t)(local_rdi)));
    *(uint32_t *)(arg5 + 0x10) = (uint32_t)(result);
    Arg2 = (1) << ((uint8_t)((uint32_t)((uint32_t)(local_rdi))));
    Arg2 = (uint32_t)((Arg2) - 1);
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(arg5 + 0x8)));
    if (((uint32_t)(local_rdi)) < 3) goto loc_00799B42;
    if (Arg2 < ((uint32_t)((uint32_t)((uint32_t)(1 + 3))))) goto loc_007995C8;
    Arg2 = (uint32_t)((Arg2) + 1);
    if (Arg2 > 8) goto loc_00799B42;
loc_007995C8:
    *(uint8_t *)(0 + arg1 * 1 + 0x18) = (uint8_t)(Arg2);
    local_r15 = 1 + 3;
    if (Arg2 != 0) {
        local_r15 = 1 + 3;
        if (Arg2 < ((uint32_t)(1 + 3))) { local_r15 = Arg2; }
    }
    if (Arg2 <= ((uint32_t)((uint32_t)((uint32_t)(1 + 3))))) goto loc_007995EE;
    goto loc_007995EE;
loc_007995E7:
    *(uint8_t *)(0 + arg1 * 1 + 0x18) = (uint8_t)((uint32_t)(Arg2));
loc_007995EE:
    local_rsi = (uint32_t)((0) + 1);
    goto loc_007994B9;
loc_007995F5:
    v_stack_m78 = (uint32_t)((uint32_t)(Arg2));
    result = Xp10SortHuffmanSymbols(Arg1 + 24, Arg1 + 728, 33, (uint32_t)((uint32_t)(local_r15)));
    if ((uint32_t)(result) == 0) goto loc_00799B42;
    v_stack_m58 = Arg1 + 2136;
    v_stack_m68 = Arg1 + 37464;
    v_stack_m70 = 4;
    v_stack_m78 = 8;
    result = Xp10BuildHuffmanDecodeTable(Arg1 + 24, Arg1 + 2136, Arg1 + 728, (uint32_t)((uint32_t)(result)));
    v_stack_m48 = result;
    Arg2 = 0;
    result = memset(Arg1 + 24, Arg2, 704, (uint32_t)((uint32_t)(result)));
    Arg4 = 0;
    v_stack_p38 = 8;
    v_stack_p18 = 8;
    goto loc_0079968B;
loc_00799687:
loc_0079968B:
    if (0 >= ((uint32_t)((uint32_t)(v_stack_p10)))) goto loc_00799A86;
    v_stack_m40 = v_stack_m48;
    v_stack_p20 = 0;
    if (*(uint64_t *)(arg5) == 0) goto loc_00799701;
    local_rsi = 8;
    if ((*(uint64_t *)(arg5)) < 8) {
        local_rsi = (uint32_t)(*(uint64_t *)(arg5));
    }
    if ((*(uint32_t *)(arg5 + 0x10)) < ((uint32_t)(local_rsi))) {
        Arg1 = Arg5 + 24;
        Arg3 = 4;
        Arg2 = v_stack_p20;
        result = Xp10ScatteredReadBytes(Arg1, Arg2, Arg3, Arg4);
        Arg1 = *(uint32_t *)(arg5 + 0x10);
        Arg2 = v_stack_p20;
        Arg2 = (Arg2) << ((uint8_t)(Arg1));
        result = Arg1 + result * 8;
        *(uint32_t *)(arg5 + 0x10) = (uint32_t)(result);
        if (((uint32_t)(result)) < ((uint32_t)(local_rsi))) { local_rsi = (uint32_t)(result); }
        Arg4 = 0;
    }
    result = (1) << ((uint8_t)((uint32_t)((uint32_t)(local_rsi))));
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) & (*(uint32_t *)(arg5 + 0x8)));
    goto loc_0079970B;
loc_00799701:
loc_0079970B:
    goto loc_0079979F;
loc_00799719:
    v_stack_p28 = 0;
    if (*(uint64_t *)(arg5) == 0) goto loc_0079977B;
    local_rsi = 4;
    if ((*(uint64_t *)(arg5)) < 4) {
        local_rsi = *(uint32_t *)(arg5);
    }
    result = 0;
    if ((*(uint32_t *)(arg5 + 0x10)) < ((uint32_t)(local_rsi))) {
        Arg1 = Arg5 + 24;
        Arg3 = 4;
        Arg2 = Arg5;
        result = Xp10ScatteredReadBytes(Arg1, Arg2, Arg3, Arg4);
        Arg1 = *(uint32_t *)(arg5 + 0x10);
        Arg2 = Arg5;
        Arg3 = v_stack_p20;
        Arg2 = (Arg2) << ((uint8_t)(Arg1));
        result = Arg1 + result * 8;
        *(uint32_t *)(arg5 + 0x10) = (uint32_t)(result);
        if (((uint32_t)(result)) < ((uint32_t)(local_rsi))) { local_rsi = (uint32_t)(result); }
        Arg4 = 0;
    }
    Arg2 = (1) << ((uint8_t)((uint32_t)((uint32_t)(local_rsi))));
    Arg2 = (uint32_t)((Arg2) - 1);
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(arg5 + 0x8)));
    goto loc_00799782;
loc_0079977B:
loc_00799782:
    result = ((int16_t)((uint16_t)(Arg3))) & (-16);
    v_stack_m40 = v_stack_m48 + result * 2;
loc_0079979F:
    v_stack_p28 = 0;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((int16_t)(*(uint16_t *)(v_stack_m48 + result * 2 + 0x0 * 2))))) & (15));
    v_stack_p20 = (uint16_t)((int16_t)(*(uint16_t *)(v_stack_m48 + result * 2 + 0x0 * 2)));
    if (*(uint64_t *)(arg5) == 0) goto loc_00799815;
    if ((uint32_t)(local_rsi) == 0) goto loc_00799815;
    local_r12 = Arg5 + 8;
    if (((uint32_t)((uint32_t)(local_rsi))) >= = (*(uint64_t *)(arg5))) {
        local_rsi = *(uint32_t *)(arg5);
        local_r12 = Arg5 + 8;
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10)))) >= ((uint32_t)(local_rsi))) goto loc_00799801;
    result = Xp10ScatteredReadBytes(Arg5 + 24, Arg5, 4, Arg4);
    Arg4 = 0;
    Arg2 = ((uint32_t)(Arg5)) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10))));
    local_r15 = Arg5 + 8;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10)) + result * 8)) < ((uint32_t)(local_rsi))) {
        local_r15 = local_r12;
        local_rsi = (uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10)) + result * 8);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg5 + 0x10)) + result * 8) - ((uint32_t)(local_rsi)));
    *(uint32_t *)(arg5 + 0x10) = (uint32_t)(result);
loc_00799815:
    if (sign_flag) goto loc_00799719;
    Arg2 = (uint32_t)(((uint16_t)(v_stack_p20)) >> (4));
    result = (uint32_t)(((uint32_t)(Arg2)) - (28));
    if (condition_is_equal) goto loc_00799A50;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_00799904;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_007998F8;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_007998D2;
    if (((uint32_t)(result)) == 1) goto loc_00799893;
    if (Arg2 > 27) goto loc_00799B42;
    Arg1 = (uint32_t)(v_stack_p18);
    if (Arg2 != 0) { Arg1 = Arg2; }
    v_stack_p18 = (uint32_t)(Arg1);
    *(uint8_t *)(0 + arg1 * 1 + 0x18) = (uint8_t)(Arg2);
    result = 0;
    local_r13 = 8;
    if ((uint8_t)(Arg2) != 0) {
        result = (uint8_t)(Arg2);
        local_r13 = 8;
        if (((uint32_t)(result)) < 8) { local_r13 = (uint32_t)(result); }
    }
    Arg2 = (uint32_t)(Arg7);
    if (((uint32_t)((uint8_t)(Arg2))) > ((uint32_t)((uint32_t)(Arg7)))) { Arg2 = (uint32_t)((uint8_t)(Arg2)); }
    v_stack_p38 = Arg2;
loc_00799888:
    local_rdi = (uint32_t)((0) + 1);
    goto loc_00799687;
loc_00799893:
    if (((uint32_t)(local_rdi)) < 16) goto loc_00799B42;
    Arg2 = (uint8_t)((*(uint8_t *)(local_rdi - 0x10 + arg1 * 1 + 0x18)) + 1);
    *(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + arg1 * 1 + 0x18) = (uint8_t)(Arg2);
    if (((uint8_t)(Arg2 - 1)) > 26) goto loc_00799B42;
    v_stack_p18 = (uint32_t)((uint8_t)(Arg2));
    if (((uint32_t)((uint8_t)(Arg2))) < ((uint32_t)(local_r13))) { local_r13 = (uint32_t)((uint8_t)(Arg2)); }
    result = (uint32_t)(Arg7);
    if (((uint32_t)((uint8_t)(Arg2))) > ((uint32_t)((uint32_t)(Arg7)))) { result = (uint32_t)((uint8_t)(Arg2)); }
    v_stack_p38 = (uint32_t)(result);
    goto loc_00799888;
loc_007998D2:
    if (((uint32_t)(local_rdi)) < 16) goto loc_00799B42;
    *(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + arg1 * 1 + 0x18) = (uint8_t)(*(uint8_t *)(local_rdi - 0x10 + arg1 * 1 + 0x18));
    if ((uint8_t)(*(uint8_t *)(local_rdi - 0x10 + arg1 * 1 + 0x18)) == 0) goto loc_00799B42;
    v_stack_p18 = (uint32_t)(*(uint8_t *)(local_rdi - 0x10 + arg1 * 1 + 0x18));
    goto loc_00799888;
loc_007998F8:
    *(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + arg1 * 1 + 0x18) = (uint8_t)((uint32_t)(v_stack_p18));
    goto loc_00799888;
loc_00799904:
    v_stack_p20 = 0;
    if ((uint32_t)(v_stack_p18) == 0) goto loc_00799B42;
    local_rsi = 2;
    if (((uint32_t)(v_stack_p18)) < 2) {
        local_rsi = *(uint32_t *)(arg5);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10)))) >= ((uint32_t)(local_rsi))) goto loc_00799950;
    result = Xp10ScatteredReadBytes(Arg5 + 24, v_stack_p20, 4, Arg4);
    Arg4 = 0;
    Arg2 = ((uint32_t)(v_stack_p20)) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10)) + result * 8)) < ((uint32_t)(local_rsi))) {
        local_rsi = (uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10)) + result * 8);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg5 + 0x10)) + result * 8) - ((uint32_t)(local_rsi)));
    *(uint32_t *)(arg5 + 0x10) = (uint32_t)(result);
    Arg2 = (1) << ((uint8_t)((uint32_t)((uint32_t)(local_rsi))));
    Arg2 = (uint32_t)((Arg2) - 1);
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(arg5 + 0x8)));
    if (((uint32_t)(local_rsi)) < 2) goto loc_00799B42;
    if (Arg2 != 3) goto loc_00799A16;
loc_0079998A:
    if (7 != 7) goto loc_00799A16;
    v_stack_p20 = 0;
    if (*(uint64_t *)(arg5) == 0) goto loc_00799B42;
    local_r15 = 7 - 4;
    if ((*(uint64_t *)(arg5)) < (7 - 4)) {
        local_r15 = *(uint32_t *)(arg5);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10)))) >= ((uint32_t)(local_r15))) goto loc_007999E2;
    result = Xp10ScatteredReadBytes(Arg5 + 24, v_stack_p20, 4, Arg4);
    Arg4 = 0;
    Arg2 = ((uint32_t)(v_stack_p20)) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10)) + result * 8)) < ((uint32_t)(local_r15))) {
        local_r15 = (uint32_t)((uint32_t)(*(uint32_t *)(arg5 + 0x10)) + result * 8);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg5 + 0x10)) + result * 8) - ((uint32_t)(local_r15)));
    *(uint32_t *)(arg5 + 0x10) = (uint32_t)(result);
    Arg2 = (1) << ((uint8_t)((uint32_t)((uint32_t)(local_r15))));
    Arg2 = (uint32_t)((Arg2) - 1);
    Arg2 = (uint32_t)((Arg2) & (*(uint32_t *)(arg5 + 0x8)));
    if (((uint32_t)(local_r15)) < 3) goto loc_00799B42;
    local_rsi = (uint32_t)((Arg2 + 5) + (Arg2));
    goto loc_0079998A;
loc_00799A16:
    if (((uint32_t)(local_rsi + local_rdi * 1)) > ((uint32_t)((uint32_t)(v_stack_p10)))) goto loc_00799B42;
    if ((uint32_t)(local_rsi) == 0) goto loc_00799687;
    Arg2 = 0;
    Arg1 = ((uint32_t)((uint32_t)(local_rdi))) + (24);
    Arg1 = (Arg1) + (Arg1);
    result = memset(Arg1, Arg2, (uint32_t)((uint32_t)(local_rsi)), Arg4);
loc_00799A41:
    local_rdi = (uint32_t)((local_rdi) + 1);
    local_rsi = (uint32_t)((local_rsi) + (-1));
    if (condition_is_not_equal) goto loc_00799A41;
    Arg4 = 0;
    goto loc_00799687;
loc_00799A50:
    local_rdi = (uint32_t)((local_rdi) + 1);
    *(uint8_t *)((uint32_t)((uint32_t)(local_rdi)) + arg1 * 1 + 0x18) = 0;
    if ((((uint8_t)(local_rdi)) & (15)) == 0) goto loc_0079968B;
loc_00799A6B:
    if (((uint32_t)(local_rdi)) >= ((uint32_t)((uint32_t)(v_stack_p10)))) goto loc_00799A86;
    *(uint8_t *)(local_rdi + arg1 * 1 + 0x18) = 0;
    local_rdi = (uint32_t)((local_rdi) + 1);
    if ((((uint8_t)(local_rdi)) & (15)) != 0) goto loc_00799A6B;
    goto loc_0079968B;
loc_00799A86:
    goto loc_00799AE3;
loc_00799A8F:
    goto loc_00799B47;
loc_00799A99:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m40))) << ((uint8_t)(local_r13 + 1)));
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)((uint32_t)(v_stack_p10))));
    result = (uint32_t)(0xC0000002ULL);
    if (!(condition_is_equal)) {
        Arg3 = (uint32_t)(local_rbx);
        Arg2 = (uint8_t)(local_r13);
        Arg1 = Arg1 + 24;
        result = memset(Arg1, Arg2, Arg3, Arg4);
        Arg2 = (uint32_t)(local_rbx);
    }
    local_rsi = Arg1 + 24;
    if (Arg2 < ((uint32_t)((uint32_t)(v_stack_p10)))) {
        Arg1 = Arg2;
        Arg3 = (uint32_t)((uint32_t)(v_stack_p10));
        Arg1 = (Arg1) + (24);
        Arg3 = (uint32_t)((Arg3) - (Arg2));
        Arg1 = (Arg1) + (Arg1);
        Arg2 = v_stack_m40 + local_r13 * 1;
        result = memset(Arg1, Arg2, Arg3, Arg4);
        local_rsi = Arg1 + 24;
    }
loc_00799AE3:
    v_stack_m78 = (uint32_t)(local_r13 + 1);
    result = Xp10SortHuffmanSymbols(Arg1 + 24, Arg1 + 728, (uint32_t)((uint32_t)((uint32_t)(v_stack_p10))), (uint32_t)((uint32_t)(local_r13)));
    if ((uint32_t)(result) == 0) goto loc_00799B42;
    v_stack_m58 = Arg6;
    v_stack_m68 = Arg1 + 37464;
    v_stack_m70 = 6;
    v_stack_m78 = 12;
    result = Xp10BuildHuffmanDecodeTable(local_rsi, Arg1 + 37464, Arg1 + 728, (uint32_t)((uint32_t)(result)));
    *(uint64_t *)(arg8) = result;
    result = 0;
    goto loc_00799B47;
loc_00799B42:
loc_00799B47:
    local_rsp = (local_rsp) + (96);
    return (uint32_t)(0xC0000242ULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x2D8` | `64` | `R` |
| `Arg1` | `+ 0x858` | `64` | `R` |
| `Arg1` | `+ 0x9258` | `64` | `R` |
| `Arg5` | `+ 0x0` | `32` | `R` |
| `Arg5` | `+ 0x0` | `64` | `R` |
| `Arg5` | `+ 0x0` | `64` | `R/W` |
| `Arg5` | `+ 0x8` | `32` | `R` |
| `Arg5` | `+ 0x8` | `64` | `R` |
| `Arg5` | `+ 0x8` | `64` | `R/W` |
| `Arg5` | `+ 0x10` | `32` | `R` |
| `Arg5` | `+ 0x10` | `32` | `W` |
| `Arg5` | `+ 0x18` | `64` | `R` |
| `Arg8` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007993D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
