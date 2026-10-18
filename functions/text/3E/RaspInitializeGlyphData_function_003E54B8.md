# RaspInitializeGlyphData

- RVA: `0x003E54B8`–`0x003E5941` (길이 `1,161` bytes)
- VA: `0x00000001403E54B8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00094E74`
- 디코드: `332`개 명령, `1,161/1,161` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003E55E0` → [RaspAllocateMemory](RaspAllocateMemory_function_003E42F8.md) (function, `0x003E42F8`)
- `0x003E5695` → [RaspAllocateMemory](RaspAllocateMemory_function_003E42F8.md) (function, `0x003E42F8`)
- `0x003E56B4` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003E571F` → [FioFwReadUshortAtOffset](../4F/FioFwReadUshortAtOffset_function_004F98A0.md) (function, `0x004F98A0`)
- `0x003E5743` → [FioFwReadBytesAtOffset](FioFwReadBytesAtOffset_function_003E5948.md) (function, `0x003E5948`)
- `0x003E5763` → [RaspAllocateMemory](RaspAllocateMemory_function_003E42F8.md) (function, `0x003E42F8`)
- `0x003E577E` → [RaspFreeMemory](RaspFreeMemory_function_003E28E4.md) (function, `0x003E28E4`)
- `0x003E5798` → [FioFwReadBytesAtOffset](FioFwReadBytesAtOffset_function_003E5948.md) (function, `0x003E5948`)
- `0x003E583B` → [FioFwReadBytesAtOffset](FioFwReadBytesAtOffset_function_003E5948.md) (function, `0x003E5948`)
- `0x003E5866` → [FioFwReadUshortAtOffset](../4F/FioFwReadUshortAtOffset_function_004F98A0.md) (function, `0x004F98A0`)
- `0x003E58C5` → [FioFwReadBytesAtOffset](FioFwReadBytesAtOffset_function_003E5948.md) (function, `0x003E5948`)
- `0x003E58EC` → [FioFwReadUshortAtOffset](../4F/FioFwReadUshortAtOffset_function_004F98A0.md) (function, `0x004F98A0`)
- `0x003E5920` → [RaspFreeMemory](RaspFreeMemory_function_003E28E4.md) (function, `0x003E28E4`)

### Direct callers
- [RaspLoadGlyphData](../6A/RaspLoadGlyphData_function_006A2818.md) at `0x006A28D6`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003E54B8  48 8B C4                        mov rax, rsp
003E54BB  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
003E54BF  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
003E54C3  89 50 10                        mov dword ptr [rax + 0x10], edx
003E54C6  48 89 48 08                     mov qword ptr [rax + 8], rcx
003E54CA  53                              push rbx
003E54CB  55                              push rbp
003E54CC  56                              push rsi
003E54CD  57                              push rdi
003E54CE  41 54                           push r12
003E54D0  41 55                           push r13
003E54D2  41 56                           push r14
003E54D4  41 57                           push r15
003E54D6  48 83 EC 48                     sub rsp, 0x48
003E54DA  33 F6                           xor esi, esi
003E54DC  49 8B E8                        mov rbp, r8
003E54DF  45 33 C0                        xor r8d, r8d
003E54E2  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
003E54E7  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
003E54EC  4D 8B D9                        mov r11, r9
003E54EF  66 44 89 44 24 20               mov word ptr [rsp + 0x20], r8w
003E54F5  48 8B C1                        mov rax, rcx
003E54F8  45 0F B7 D0                     movzx r10d, r8w
003E54FC  45 0F B7 E0                     movzx r12d, r8w
003E5500  48 85 C9                        test rcx, rcx
003E5503  0F 84 21 04 00 00               je 0x1403e592a
003E5509  8B 49 3C                        mov ecx, dword ptr [rcx + 0x3c]
003E550C  85 C9                           test ecx, ecx
003E550E  0F 84 16 04 00 00               je 0x1403e592a
003E5514  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
003E5518  4C 8B 70 10                     mov r14, qword ptr [rax + 0x10]
003E551C  8D 04 11                        lea eax, [rcx + rdx]
003E551F  8D 50 02                        lea edx, [rax + 2]
003E5522  45 8B 46 08                     mov r8d, dword ptr [r14 + 8]
003E5526  41 3B D0                        cmp edx, r8d
003E5529  77 14                           ja 0x1403e553f
003E552B  8B C8                           mov ecx, eax
003E552D  49 8B 06                        mov rax, qword ptr [r14]
003E5530  0F B7 1C 01                     movzx ebx, word ptr [rcx + rax]
003E5534  66 89 5C 24 30                  mov word ptr [rsp + 0x30], bx
003E5539  66 C1 CB 08                     ror bx, 8
003E553D  EB 05                           jmp 0x1403e5544
003E553F  0F B7 5C 24 30                  movzx ebx, word ptr [rsp + 0x30]
003E5544  44 8D 4A 02                     lea r9d, [rdx + 2]
003E5548  45 3B C8                        cmp r9d, r8d
003E554B  77 15                           ja 0x1403e5562
003E554D  49 8B 06                        mov rax, qword ptr [r14]
003E5550  44 0F B7 3C 02                  movzx r15d, word ptr [rdx + rax]
003E5555  66 44 89 7C 24 32               mov word ptr [rsp + 0x32], r15w
003E555B  66 41 C1 CF 08                  ror r15w, 8
003E5560  EB 06                           jmp 0x1403e5568
003E5562  44 0F B7 7C 24 32               movzx r15d, word ptr [rsp + 0x32]
003E5568  41 8D 51 02                     lea edx, [r9 + 2]
003E556C  41 3B D0                        cmp edx, r8d
003E556F  77 13                           ja 0x1403e5584
003E5571  49 8B 06                        mov rax, qword ptr [r14]
003E5574  41 0F B7 3C 01                  movzx edi, word ptr [r9 + rax]
003E5579  66 89 7C 24 34                  mov word ptr [rsp + 0x34], di
003E557E  66 C1 CF 08                     ror di, 8
003E5582  EB 05                           jmp 0x1403e5589
003E5584  0F B7 7C 24 34                  movzx edi, word ptr [rsp + 0x34]
003E5589  44 8D 4A 02                     lea r9d, [rdx + 2]
003E558D  45 3B C8                        cmp r9d, r8d
003E5590  77 15                           ja 0x1403e55a7
003E5592  49 8B 06                        mov rax, qword ptr [r14]
003E5595  44 0F B7 2C 02                  movzx r13d, word ptr [rdx + rax]
003E559A  66 44 89 6C 24 36               mov word ptr [rsp + 0x36], r13w
003E55A0  66 41 C1 CD 08                  ror r13w, 8
003E55A5  EB 06                           jmp 0x1403e55ad
003E55A7  44 0F B7 6C 24 36               movzx r13d, word ptr [rsp + 0x36]
003E55AD  41 8D 41 02                     lea eax, [r9 + 2]
003E55B1  41 3B C0                        cmp eax, r8d
003E55B4  77 11                           ja 0x1403e55c7
003E55B6  49 8B 06                        mov rax, qword ptr [r14]
003E55B9  41 0F B7 34 01                  movzx esi, word ptr [r9 + rax]
003E55BE  66 C1 CE 08                     ror si, 8
003E55C2  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
003E55C7  66 85 DB                        test bx, bx
003E55CA  79 0A                           jns 0x1403e55d6
003E55CC  B8 0D 00 00 C0                  mov eax, 0xc000000d
003E55D1  E9 59 03 00 00                  jmp 0x1403e592f
003E55D6  75 49                           jne 0x1403e5621
003E55D8  49 8B D3                        mov rdx, r11
003E55DB  B9 42 00 00 00                  mov ecx, 0x42
003E55E0  E8 13 ED FF FF                  call 0x1403e42f8
003E55E5  45 33 C0                        xor r8d, r8d
003E55E8  48 85 C0                        test rax, rax
003E55EB  0F 84 B1 00 00 00               je 0x1403e56a2
003E55F1  0F BF CF                        movsx ecx, di
003E55F4  89 48 06                        mov dword ptr [rax + 6], ecx
003E55F7  41 0F BF CD                     movsx ecx, r13w
003E55FB  41 0F BF D7                     movsx edx, r15w
003E55FF  89 48 0A                        mov dword ptr [rax + 0xa], ecx
003E5602  0F BF CE                        movsx ecx, si
003E5605  89 48 0E                        mov dword ptr [rax + 0xe], ecx
003E5608  66 44 89 00                     mov word ptr [rax], r8w
003E560C  89 50 02                        mov dword ptr [rax + 2], edx
003E560F  89 50 12                        mov dword ptr [rax + 0x12], edx
003E5612  44 89 40 16                     mov dword ptr [rax + 0x16], r8d
003E5616  48 89 45 00                     mov qword ptr [rbp], rax
003E561A  33 C0                           xor eax, eax
003E561C  E9 0E 03 00 00                  jmp 0x1403e592f
003E5621  0F BF C3                        movsx eax, bx
003E5624  41 8D 0C 41                     lea ecx, [r9 + rax*2]
003E5628  8D 51 02                        lea edx, [rcx + 2]
003E562B  41 3B D0                        cmp edx, r8d
003E562E  77 0D                           ja 0x1403e563d
003E5630  49 8B 06                        mov rax, qword ptr [r14]
003E5633  44 0F B7 24 01                  movzx r12d, word ptr [rcx + rax]
003E5638  66 41 C1 CC 08                  ror r12w, 8
003E563D  66 41 FF C4                     inc r12w
003E5641  8D 42 02                        lea eax, [rdx + 2]
003E5644  41 3B C0                        cmp eax, r8d
003E5647  77 13                           ja 0x1403e565c
003E5649  49 8B 06                        mov rax, qword ptr [r14]
003E564C  44 0F B7 14 02                  movzx r10d, word ptr [rdx + rax]
003E5651  66 41 C1 CA 08                  ror r10w, 8
003E5656  66 44 89 54 24 20               mov word ptr [rsp + 0x20], r10w
003E565C  41 0F B7 CA                     movzx ecx, r10w
003E5660  41 0F B7 C4                     movzx eax, r12w
003E5664  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
003E5668  41 0F B7 C4                     movzx eax, r12w
003E566C  41 0F B7 D4                     movzx edx, r12w
003E5670  48 83 C2 42                     add rdx, 0x42
003E5674  4C 8D 04 85 08 00 00 00         lea r8, [rax*4 + 8]
003E567C  48 0F BF C3                     movsx rax, bx
003E5680  49 03 C0                        add rax, r8
003E5683  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
003E5688  48 8D 2C 41                     lea rbp, [rcx + rax*2]
003E568C  48 03 EA                        add rbp, rdx
003E568F  49 8B D3                        mov rdx, r11
003E5692  48 8B CD                        mov rcx, rbp
003E5695  E8 5E EC FF FF                  call 0x1403e42f8
003E569A  48 8B F0                        mov rsi, rax
003E569D  48 85 C0                        test rax, rax
003E56A0  75 0A                           jne 0x1403e56ac
003E56A2  B8 9A 00 00 C0                  mov eax, 0xc000009a
003E56A7  E9 83 02 00 00                  jmp 0x1403e592f
003E56AC  4C 8B C5                        mov r8, rbp
003E56AF  33 D2                           xor edx, edx
003E56B1  48 8B CE                        mov rcx, rsi
003E56B4  E8 87 15 2E 00                  call 0x1406c6c40
003E56B9  0F BF C7                        movsx eax, di
003E56BC  48 8B EE                        mov rbp, rsi
003E56BF  8B BC 24 98 00 00 00            mov edi, dword ptr [rsp + 0x98]
003E56C6  89 46 06                        mov dword ptr [rsi + 6], eax
003E56C9  83 C7 0A                        add edi, 0xa
003E56CC  41 0F BF C5                     movsx eax, r13w
003E56D0  45 33 ED                        xor r13d, r13d
003E56D3  89 46 0A                        mov dword ptr [rsi + 0xa], eax
003E56D6  0F BF 44 24 28                  movsx eax, word ptr [rsp + 0x28]
003E56DB  89 46 0E                        mov dword ptr [rsi + 0xe], eax
003E56DE  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
003E56E6  41 0F BF CF                     movsx ecx, r15w
003E56EA  44 0F B7 7C 24 20               movzx r15d, word ptr [rsp + 0x20]
003E56F0  66 89 1E                        mov word ptr [rsi], bx
003E56F3  89 4E 02                        mov dword ptr [rsi + 2], ecx
003E56F6  89 4E 12                        mov dword ptr [rsi + 0x12], ecx
003E56F9  66 44 89 7E 16                  mov word ptr [rsi + 0x16], r15w
003E56FE  66 44 89 66 18                  mov word ptr [rsi + 0x18], r12w
003E5703  48 83 C6 42                     add rsi, 0x42
003E5707  03 78 3C                        add edi, dword ptr [rax + 0x3c]
003E570A  48 89 75 1A                     mov qword ptr [rbp + 0x1a], rsi
003E570E  66 44 3B EB                     cmp r13w, bx
003E5712  7D 1D                           jge 0x1403e5731
003E5714  0F B7 DB                        movzx ebx, bx
003E5717  4C 8B C6                        mov r8, rsi
003E571A  8B D7                           mov edx, edi
003E571C  49 8B CE                        mov rcx, r14
003E571F  E8 7C 41 11 00                  call 0x1404f98a0
003E5724  83 C7 02                        add edi, 2
003E5727  48 83 C6 02                     add rsi, 2
003E572B  48 83 EB 01                     sub rbx, 1
003E572F  75 E6                           jne 0x1403e5717
003E5731  83 C7 02                        add edi, 2
003E5734  48 89 75 22                     mov qword ptr [rbp + 0x22], rsi
003E5738  8B D7                           mov edx, edi
003E573A  4C 8B CE                        mov r9, rsi
003E573D  45 8B C7                        mov r8d, r15d
003E5740  49 8B CE                        mov rcx, r14
003E5743  E8 00 02 00 00                  call 0x1403e5948
003E5748  49 03 F7                        add rsi, r15
003E574B  41 0F B7 DC                     movzx ebx, r12w
003E574F  41 03 FF                        add edi, r15d
003E5752  48 89 75 2A                     mov qword ptr [rbp + 0x2a], rsi
003E5756  4C 8B BC 24 A8 00 00 00         mov r15, qword ptr [rsp + 0xa8]
003E575E  8B CB                           mov ecx, ebx
003E5760  49 8B D7                        mov rdx, r15
003E5763  E8 90 EB FF FF                  call 0x1403e42f8
003E5768  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
003E5770  4C 8B E0                        mov r12, rax
003E5773  48 85 C0                        test rax, rax
003E5776  75 10                           jne 0x1403e5788
003E5778  49 8B D7                        mov rdx, r15
003E577B  48 8B CD                        mov rcx, rbp
003E577E  E8 61 D1 FF FF                  call 0x1403e28e4
003E5783  E9 1A FF FF FF                  jmp 0x1403e56a2
003E5788  44 8B 6C 24 24                  mov r13d, dword ptr [rsp + 0x24]
003E578D  4D 8B CC                        mov r9, r12
003E5790  45 8B C5                        mov r8d, r13d
003E5793  8B D7                           mov edx, edi
003E5795  49 8B CE                        mov rcx, r14
003E5798  E8 AB 01 00 00                  call 0x1403e5948
003E579D  45 33 DB                        xor r11d, r11d
003E57A0  45 8B C3                        mov r8d, r11d
003E57A3  45 0F B7 CB                     movzx r9d, r11w
003E57A7  45 85 ED                        test r13d, r13d
003E57AA  74 54                           je 0x1403e5800
003E57AC  45 8D 7B 01                     lea r15d, [r11 + 1]
003E57B0  48 8B 4D 2A                     mov rcx, qword ptr [rbp + 0x2a]
003E57B4  45 8B D0                        mov r10d, r8d
003E57B7  49 0F BF D1                     movsx rdx, r9w
003E57BB  66 45 03 CF                     add r9w, r15w
003E57BF  43 8A 04 22                     mov al, byte ptr [r10 + r12]
003E57C3  88 04 0A                        mov byte ptr [rdx + rcx], al
003E57C6  43 F6 04 22 08                  test byte ptr [r10 + r12], 8
003E57CB  74 27                           je 0x1403e57f4
003E57CD  41 FF C0                        inc r8d
003E57D0  43 0F B6 0C 20                  movzx ecx, byte ptr [r8 + r12]
003E57D5  84 C9                           test cl, cl
003E57D7  74 1B                           je 0x1403e57f4
003E57D9  44 8B D9                        mov r11d, ecx
003E57DC  48 8B 4D 2A                     mov rcx, qword ptr [rbp + 0x2a]
003E57E0  43 8A 04 22                     mov al, byte ptr [r10 + r12]
003E57E4  49 0F BF D1                     movsx rdx, r9w
003E57E8  66 45 03 CF                     add r9w, r15w
003E57EC  88 04 0A                        mov byte ptr [rdx + rcx], al
003E57EF  4D 2B DF                        sub r11, r15
003E57F2  75 E8                           jne 0x1403e57dc
003E57F4  45 03 C7                        add r8d, r15d
003E57F7  41 0F BF C1                     movsx eax, r9w
003E57FB  41 3B C5                        cmp eax, r13d
003E57FE  7C B0                           jl 0x1403e57b0
003E5800  48 03 F3                        add rsi, rbx
003E5803  41 03 F8                        add edi, r8d
003E5806  48 89 75 32                     mov qword ptr [rbp + 0x32], rsi
003E580A  45 0F B7 FB                     movzx r15d, r11w
003E580E  45 85 ED                        test r13d, r13d
003E5811  74 73                           je 0x1403e5886
003E5813  41 BC 01 00 00 00               mov r12d, 1
003E5819  49 0F BF CF                     movsx rcx, r15w
003E581D  48 8D 1C 8E                     lea rbx, [rsi + rcx*4]
003E5821  44 89 1B                        mov dword ptr [rbx], r11d
003E5824  48 8B 45 2A                     mov rax, qword ptr [rbp + 0x2a]
003E5828  8A 14 01                        mov dl, byte ptr [rcx + rax]
003E582B  F6 C2 02                        test dl, 2
003E582E  74 29                           je 0x1403e5859
003E5830  4C 8B CB                        mov r9, rbx
003E5833  45 8B C4                        mov r8d, r12d
003E5836  8B D7                           mov edx, edi
003E5838  49 8B CE                        mov rcx, r14
003E583B  E8 08 01 00 00                  call 0x1403e5948
003E5840  48 8B 45 2A                     mov rax, qword ptr [rbp + 0x2a]
003E5844  41 03 FC                        add edi, r12d
003E5847  49 0F BF CF                     movsx rcx, r15w
003E584B  F6 04 01 10                     test byte ptr [rcx + rax], 0x10
003E584F  75 1D                           jne 0x1403e586e
003E5851  8B 03                           mov eax, dword ptr [rbx]
003E5853  F7 D8                           neg eax
003E5855  89 03                           mov dword ptr [rbx], eax
003E5857  EB 15                           jmp 0x1403e586e
003E5859  F6 C2 10                        test dl, 0x10
003E585C  75 13                           jne 0x1403e5871
003E585E  4C 8B C3                        mov r8, rbx
003E5861  8B D7                           mov edx, edi
003E5863  49 8B CE                        mov rcx, r14
003E5866  E8 35 40 11 00                  call 0x1404f98a0
003E586B  83 C7 02                        add edi, 2
003E586E  45 33 DB                        xor r11d, r11d
003E5871  66 45 03 FC                     add r15w, r12w
003E5875  41 0F BF C7                     movsx eax, r15w
003E5879  41 3B C5                        cmp eax, r13d
003E587C  7C 9B                           jl 0x1403e5819
003E587E  4C 8B A4 24 90 00 00 00         mov r12, qword ptr [rsp + 0x90]
003E5886  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
003E588B  41 0F B7 F3                     movzx esi, r11w
003E588F  48 03 4D 32                     add rcx, qword ptr [rbp + 0x32]
003E5893  48 89 4D 3A                     mov qword ptr [rbp + 0x3a], rcx
003E5897  45 85 ED                        test r13d, r13d
003E589A  74 6E                           je 0x1403e590a
003E589C  4C 8B E1                        mov r12, rcx
003E589F  4C 0F BF FE                     movsx r15, si
003E58A3  4B 8D 1C BC                     lea rbx, [r12 + r15*4]
003E58A7  44 89 1B                        mov dword ptr [rbx], r11d
003E58AA  48 8B 45 2A                     mov rax, qword ptr [rbp + 0x2a]
003E58AE  41 8A 0C 07                     mov cl, byte ptr [r15 + rax]
003E58B2  F6 C1 04                        test cl, 4
003E58B5  74 28                           je 0x1403e58df
003E58B7  4C 8B CB                        mov r9, rbx
003E58BA  41 B8 01 00 00 00               mov r8d, 1
003E58C0  8B D7                           mov edx, edi
003E58C2  49 8B CE                        mov rcx, r14
003E58C5  E8 7E 00 00 00                  call 0x1403e5948
003E58CA  48 8B 45 2A                     mov rax, qword ptr [rbp + 0x2a]
003E58CE  FF C7                           inc edi
003E58D0  41 F6 04 07 20                  test byte ptr [r15 + rax], 0x20
003E58D5  75 1D                           jne 0x1403e58f4
003E58D7  8B 03                           mov eax, dword ptr [rbx]
003E58D9  F7 D8                           neg eax
003E58DB  89 03                           mov dword ptr [rbx], eax
003E58DD  EB 15                           jmp 0x1403e58f4
003E58DF  F6 C1 20                        test cl, 0x20
003E58E2  75 13                           jne 0x1403e58f7
003E58E4  4C 8B C3                        mov r8, rbx
003E58E7  8B D7                           mov edx, edi
003E58E9  49 8B CE                        mov rcx, r14
003E58EC  E8 AF 3F 11 00                  call 0x1404f98a0
003E58F1  83 C7 02                        add edi, 2
003E58F4  45 33 DB                        xor r11d, r11d
003E58F7  66 FF C6                        inc si
003E58FA  0F BF C6                        movsx eax, si
003E58FD  41 3B C5                        cmp eax, r13d
003E5900  7C 9D                           jl 0x1403e589f
003E5902  4C 8B A4 24 90 00 00 00         mov r12, qword ptr [rsp + 0x90]
003E590A  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
003E5912  49 8B CC                        mov rcx, r12
003E5915  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
003E591D  48 89 28                        mov qword ptr [rax], rbp
003E5920  E8 BF CF FF FF                  call 0x1403e28e4
003E5925  E9 F0 FC FF FF                  jmp 0x1403e561a
003E592A  B8 01 00 00 C0                  mov eax, 0xc0000001
003E592F  48 83 C4 48                     add rsp, 0x48
003E5933  41 5F                           pop r15
003E5935  41 5E                           pop r14
003E5937  41 5D                           pop r13
003E5939  41 5C                           pop r12
003E593B  5F                              pop rdi
003E593C  5E                              pop rsi
003E593D  5D                              pop rbp
003E593E  5B                              pop rbx
003E593F  C3                              ret
003E5940  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RaspInitializeGlyphData(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int16 v_stack_m52;
    unsigned __int16 v_stack_m54;
    unsigned __int16 v_stack_m56;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m64;
    unsigned __int16 v_stack_m68;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = (unsigned int)(a2);
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (72);
    v_rsi = 0;
    a3 = 0;
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    v_stack_m68 = 0;
    if (a1 == 0) goto loc_003E592A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 60))) == 0) goto loc_003E592A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 60)) + a2 * 1 + 2)) > ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16) + 8))))) goto loc_003E553F;
    v_stack_m58 = (unsigned __int16)(*(unsigned __int16 *)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 60)) + a2 * 1)) + *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16)) * 1));
    goto loc_003E5544;
loc_003E553F:
loc_003E5544:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 60)) + a2 * 1 + 2 + 2)) > ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16) + 8))))) goto loc_003E5562;
    v_stack_m56 = (unsigned __int16)(*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(a1 + 60)) + a2 * 1 + 2 + *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16)) * 1));
    goto loc_003E5568;
loc_003E5562:
loc_003E5568:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 60)) + a2 * 1 + 2 + 2 + 2)) > ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16) + 8))))) goto loc_003E5584;
    v_stack_m54 = (unsigned __int16)(*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(a1 + 60)) + a2 * 1 + 2 + 2 + *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16)) * 1));
    goto loc_003E5589;
loc_003E5584:
loc_003E5589:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 60)) + a2 * 1 + 2 + 2 + 2 + 2)) > ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16) + 8))))) goto loc_003E55A7;
    v_stack_m52 = (unsigned __int16)(*(unsigned __int16 *)((unsigned int)(*(unsigned int *)(a1 + 60)) + a2 * 1 + 2 + 2 + 2 + *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16)) * 1));
    goto loc_003E55AD;
loc_003E55A7:
loc_003E55AD:
    result = (unsigned int)(*(unsigned int *)(a1 + 60)) + a2 * 1 + 2 + 2 + 2 + 2 + 2;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 60)) + a2 * 1 + 2 + 2 + 2 + 2 + 2)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16) + 8))))) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16));
        v_rsi = *(unsigned __int16 *)((unsigned int)(*(unsigned int *)(a1 + 60)) + a2 * 1 + 2 + 2 + 2 + 2 + result * 1);
        v_stack_m60 = v_rsi;
    }
    if (!sign_flag) goto loc_003E55D6;
    goto loc_003E592F;
loc_003E55D6:
    if ((unsigned __int16)(v_stack_m58) != 0) goto loc_003E5621;
    result = RaspAllocateMemory(66, a4, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16) + 8)), (unsigned int)(*(unsigned int *)(a1 + 60)) + a2 * 1 + 2 + 2 + 2 + 2);
    a3 = 0;
    if (result == 0) goto loc_003E56A2;
    *(unsigned int *)(result + 6) = (unsigned int)((__int16)((unsigned __int16)(v_stack_m54)));
    *(unsigned int *)(result + 10) = (unsigned int)((__int16)((unsigned __int16)(v_stack_m52)));
    *(unsigned int *)(result + 14) = (unsigned int)((__int16)((unsigned __int16)(v_rsi)));
    *(unsigned __int16 *)(result) = 0;
    *(unsigned int *)(result + 2) = (unsigned int)((__int16)((unsigned __int16)(v_stack_m56)));
    *(unsigned int *)(result + 18) = (unsigned int)((__int16)((unsigned __int16)(v_stack_m56)));
    *(unsigned int *)(result + 22) = 0;
    *(unsigned __int64 *)(a3) = result;
loc_003E561A:
    result = 0;
    goto loc_003E592F;
loc_003E5621:
    result = (__int16)((unsigned __int16)(v_stack_m58));
    v_r12 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 60)) + a2 * 1 + 2 + 2 + 2 + 2 + (__int16)((unsigned __int16)(v_stack_m58)) * 2 + 2)) <= 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16));
        v_r12 = *(unsigned __int16 *)((unsigned int)(*(unsigned int *)(a1 + 60)) + a2 * 1 + 2 + 2 + 2 + 2 + (__int16)((unsigned __int16)(v_stack_m58)) * 2 + result * 1);
    }
    v_r12 = (unsigned __int16)((v_r12) + 1);
    result = (unsigned int)(*(unsigned int *)(a1 + 60)) + a2 * 1 + 2 + 2 + 2 + 2 + (__int16)((unsigned __int16)(v_stack_m58)) * 2 + 2 + 2;
    v_r10 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 60)) + a2 * 1 + 2 + 2 + 2 + 2 + (__int16)((unsigned __int16)(v_stack_m58)) * 2 + 2 + 2)) <= 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16));
        v_r10 = *(unsigned __int16 *)((unsigned int)(*(unsigned int *)(a1 + 60)) + a2 * 1 + 2 + 2 + 2 + 2 + (__int16)((unsigned __int16)(v_stack_m58)) * 2 + 2 + result * 1);
        v_stack_m68 = (unsigned __int16)(v_r10);
    }
    v_stack_m64 = (unsigned int)((unsigned __int16)(v_r12));
    a2 = ((unsigned __int16)(v_r12)) + (66);
    result = ((__int16)((unsigned __int16)(v_stack_m58))) + ((unsigned __int16)(v_r12) * 4 + 8);
    v_stack_m58 = (unsigned __int16)(v_r12) * 4 + 8;
    v_rbp = ((unsigned __int16)(v_r10) + result * 2) + (a2);
    result = RaspAllocateMemory(v_rbp, a4, (unsigned __int16)(v_r12) * 4 + 8, (unsigned int)(*(unsigned int *)(a1 + 60)) + a2 * 1 + 2 + 2 + 2 + 2);
    if (result != 0) goto loc_003E56AC;
loc_003E56A2:
    goto loc_003E592F;
loc_003E56AC:
    a2 = 0;
    result = memset(result, a2, v_rbp, (unsigned int)(*(unsigned int *)(a1 + 60)) + a2 * 1 + 2 + 2 + 2 + 2);
    *(unsigned int *)(result + 6) = (unsigned int)((__int16)((unsigned __int16)(v_stack_m54)));
    v_rdi = (unsigned int)(((unsigned int)(v_stack_p10)) + (10));
    v_r13 = 0;
    *(unsigned int *)(result + 10) = (unsigned int)((__int16)((unsigned __int16)(v_stack_m52)));
    *(unsigned int *)(result + 14) = (unsigned int)((__int16)(v_stack_m60));
    *(unsigned __int16 *)(result) = (unsigned __int16)(v_stack_m58);
    *(unsigned int *)(result + 2) = (unsigned int)((__int16)((unsigned __int16)(v_stack_m56)));
    *(unsigned int *)(result + 18) = (unsigned int)((__int16)((unsigned __int16)(v_stack_m56)));
    *(unsigned __int16 *)(result + 22) = (unsigned __int16)(v_stack_m68);
    *(unsigned __int16 *)(result + 24) = (unsigned __int16)(v_r12);
    v_rsi = (result) + (66);
    v_rdi = (unsigned int)((v_rdi) + (*(unsigned int *)(v_stack_p8 + 60)));
    *(unsigned __int64 *)(result + 26) = v_rsi;
    if (0 >= ((unsigned __int16)(v_stack_m58))) goto loc_003E5731;
loc_003E5717:
    result = FioFwReadUshortAtOffset(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16), (unsigned int)((unsigned int)(v_rdi)), v_rsi, (unsigned int)(*(unsigned int *)(a1 + 60)) + a2 * 1 + 2 + 2 + 2 + 2);
    v_rdi = (unsigned int)((v_rdi) + (2));
    v_rsi = (v_rsi) + (2);
    v_rbx = ((unsigned __int16)(v_stack_m58)) - (1);
    if (condition_is_not_equal) goto loc_003E5717;
loc_003E5731:
    v_rdi = (unsigned int)((v_rdi) + (2));
    *(unsigned __int64 *)(result + 34) = v_rsi;
    result = FioFwReadBytesAtOffset(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16), (unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)(v_stack_m68)), v_rsi);
    v_rsi = (v_rsi) + (v_stack_m68);
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_stack_m68)));
    *(unsigned __int64 *)(result + 42) = v_rsi;
    result = RaspAllocateMemory((unsigned int)((unsigned int)((unsigned __int16)(v_r12))), v_stack_p20, (unsigned int)((unsigned int)(v_stack_m68)), v_rsi);
    v_stack_p8 = result;
    if (result != 0) goto loc_003E5788;
    result = RaspFreeMemory(result, v_stack_p20, (unsigned int)((unsigned int)(v_stack_m68)), v_rsi);
    goto loc_003E56A2;
loc_003E5788:
    result = FioFwReadBytesAtOffset(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16), (unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)((unsigned int)(v_stack_m64))), result);
    v_r11 = 0;
    if ((unsigned int)((unsigned int)(v_stack_m64)) == 0) goto loc_003E5800;
loc_003E57B0:
    a4 = (unsigned __int16)((0) + ((unsigned __int16)(v_r11 + 1)));
    *(unsigned __int8 *)((__int16)(0) + *(unsigned __int64 *)(result + 42) * 1) = (unsigned __int8)(*(unsigned __int8 *)(0 + result * 1));
    if (((*(unsigned __int8 *)(0 + result * 1)) & (8)) == 0) goto loc_003E57F4;
    a3 = (unsigned int)((0) + 1);
    if ((unsigned __int8)(*(unsigned __int8 *)(a3 + result * 1)) == 0) goto loc_003E57F4;
loc_003E57DC:
    a4 = (unsigned __int16)((a4) + ((unsigned __int16)(v_r11 + 1)));
    *(unsigned __int8 *)((__int16)((unsigned __int16)(a4)) + *(unsigned __int64 *)(result + 42) * 1) = (unsigned __int8)(*(unsigned __int8 *)(0 + result * 1));
    v_r11 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(a3 + result * 1)))) - (v_r11 + 1);
    if (condition_is_not_equal) goto loc_003E57DC;
loc_003E57F4:
    a3 = (unsigned int)((a3) + ((unsigned int)(v_r11 + 1)));
    if (((unsigned int)((__int16)((unsigned __int16)(a4)))) < ((unsigned int)((unsigned int)(v_stack_m64)))) goto loc_003E57B0;
loc_003E5800:
    v_rsi = (v_rsi) + ((unsigned __int16)(v_r12));
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(a3)));
    *(unsigned __int64 *)(result + 50) = v_rsi;
    if ((unsigned int)((unsigned int)(v_stack_m64)) == 0) goto loc_003E5886;
loc_003E5819:
    *(unsigned int *)(v_rsi + (__int16)((unsigned __int16)((unsigned __int16)(v_r11))) * 4) = (unsigned int)(v_r11);
    if ((((unsigned __int8)(*(unsigned __int8 *)((__int16)((unsigned __int16)((unsigned __int16)(v_r11))) + *(unsigned __int64 *)(result + 42) * 1))) & (2)) == 0) goto loc_003E5859;
    result = FioFwReadBytesAtOffset(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16), (unsigned int)((unsigned int)(v_rdi)), 1, v_rsi + (__int16)((unsigned __int16)((unsigned __int16)(v_r11))) * 4);
    v_rdi = (unsigned int)((v_rdi) + (1));
    if (((*(unsigned __int8 *)((__int16)((unsigned __int16)((unsigned __int16)(v_r11))) + *(unsigned __int64 *)(result + 42) * 1)) & (16)) != 0) goto loc_003E586E;
    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_rsi + (__int16)((unsigned __int16)((unsigned __int16)(v_r11))) * 4))));
    *(unsigned int *)(v_rsi + (__int16)((unsigned __int16)((unsigned __int16)(v_r11))) * 4) = (unsigned int)(result);
    goto loc_003E586E;
loc_003E5859:
    if ((((unsigned __int8)((unsigned int)((unsigned int)(v_rdi)))) & (16)) != 0) goto loc_003E5871;
    result = FioFwReadUshortAtOffset(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16), (unsigned int)((unsigned int)(v_rdi)), v_rsi + (__int16)((unsigned __int16)((unsigned __int16)(v_r11))) * 4, v_rsi + (__int16)((unsigned __int16)((unsigned __int16)(v_r11))) * 4);
    v_rdi = (unsigned int)((v_rdi) + (2));
loc_003E586E:
    v_r11 = 0;
loc_003E5871:
    v_r15 = (unsigned __int16)(((unsigned __int16)(v_r11)) + (1));
    if (((unsigned int)((__int16)((unsigned __int16)(v_r15)))) < ((unsigned int)((unsigned int)(v_stack_m64)))) goto loc_003E5819;
loc_003E5886:
    a1 = (v_stack_m58) + (*(unsigned __int64 *)(result + 50));
    *(unsigned __int64 *)(result + 58) = a1;
    if ((unsigned int)((unsigned int)(v_stack_m64)) == 0) goto loc_003E590A;
loc_003E589F:
    *(unsigned int *)(a1 + (__int16)(0) * 4) = 0;
    if ((((unsigned __int8)(*(unsigned __int8 *)((__int16)(0) + *(unsigned __int64 *)(result + 42) * 1))) & (4)) == 0) goto loc_003E58DF;
    result = FioFwReadBytesAtOffset(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16), (unsigned int)((unsigned int)(v_rdi)), 1, a1 + (__int16)(0) * 4);
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((*(unsigned __int8 *)((__int16)(0) + *(unsigned __int64 *)(result + 42) * 1)) & (32)) != 0) goto loc_003E58F4;
    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(a1 + (__int16)(0) * 4))));
    *(unsigned int *)(a1 + (__int16)(0) * 4) = (unsigned int)(result);
    goto loc_003E58F4;
loc_003E58DF:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16))) & (32)) != 0) goto loc_003E58F7;
    result = FioFwReadUshortAtOffset(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 16), (unsigned int)((unsigned int)(v_rdi)), a1 + (__int16)(0) * 4, a1 + (__int16)(0) * 4);
    v_rdi = (unsigned int)((v_rdi) + (2));
loc_003E58F4:
    v_r11 = 0;
loc_003E58F7:
    v_rsi = (unsigned __int16)((0) + 1);
    if (((unsigned int)((__int16)((unsigned __int16)(v_rsi)))) < ((unsigned int)((unsigned int)(v_stack_m64)))) goto loc_003E589F;
loc_003E590A:
    *(unsigned __int64 *)(v_stack_p18) = result;
    result = RaspFreeMemory(v_stack_p8, v_stack_p20, a1 + (__int16)(0) * 4, a1 + (__int16)(0) * 4);
    goto loc_003E561A;
loc_003E592A:
loc_003E592F:
    v_rsp = (v_rsp) + (72);
    return (unsigned int)(0xC0000001ULL);
}
```

## 5. (Beta) C Style

```c
int64_t RaspInitializeGlyphData(void *Arg1, int64_t Arg2, void *Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint16_t v_stack_m52;
    uint16_t v_stack_m54;
    uint16_t v_stack_m56;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m64;
    uint16_t v_stack_m68;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(void **)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = (uint32_t)(Arg2);
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (72);
    local_rsi = 0;
    Arg3 = 0;
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    v_stack_m68 = 0;
    if (Arg1 == NULL) goto loc_003E592A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x3C))) == 0) goto loc_003E592A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x3C)) + Arg2 * 1 + 2)) > ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10) + 0x8))))) goto loc_003E553F;
    v_stack_m58 = (uint16_t)(*(uint16_t *)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x3C)) + Arg2 * 1)) + *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10)) * 1));
    goto loc_003E5544;
loc_003E553F:
loc_003E5544:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x3C)) + Arg2 * 1 + 2 + 2)) > ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10) + 0x8))))) goto loc_003E5562;
    v_stack_m56 = (uint16_t)(*(uint16_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x3C)) + Arg2 * 1 + 0x2 + *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10)) * 1));
    goto loc_003E5568;
loc_003E5562:
loc_003E5568:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x3C)) + Arg2 * 1 + 2 + 2 + 2)) > ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10) + 0x8))))) goto loc_003E5584;
    v_stack_m54 = (uint16_t)(*(uint16_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x3C)) + Arg2 * 1 + 0x2 + 0x2 + *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10)) * 1));
    goto loc_003E5589;
loc_003E5584:
loc_003E5589:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x3C)) + Arg2 * 1 + 2 + 2 + 2 + 2)) > ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10) + 0x8))))) goto loc_003E55A7;
    v_stack_m52 = (uint16_t)(*(uint16_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x3C)) + Arg2 * 1 + 0x2 + 0x2 + 0x2 + *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10)) * 1));
    goto loc_003E55AD;
loc_003E55A7:
loc_003E55AD:
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x3C)) + Arg2 * 1 + 2 + 2 + 2 + 2 + 2;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x3C)) + Arg2 * 1 + 2 + 2 + 2 + 2 + 2)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10) + 0x8))))) {
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10));
        local_rsi = *(uint16_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x3C)) + Arg2 * 1 + 0x2 + 0x2 + 0x2 + 0x2 + result * 1);
        v_stack_m60 = local_rsi;
    }
    if (!sign_flag) goto loc_003E55D6;
    goto loc_003E592F;
loc_003E55D6:
    if ((uint16_t)(v_stack_m58) != 0) goto loc_003E5621;
    result = RaspAllocateMemory(66, Arg4, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10) + 0x8)), (uint32_t)(*(uint32_t *)(arg1 + 0x3C)) + Arg2 * 1 + 2 + 2 + 2 + 2);
    Arg3 = 0;
    if (result == 0) goto loc_003E56A2;
    *(uint32_t *)(result + 0x6) = (uint32_t)((int16_t)((uint16_t)(v_stack_m54)));
    *(uint32_t *)(result + 0xA) = (uint32_t)((int16_t)((uint16_t)(v_stack_m52)));
    *(uint32_t *)(result + 0xE) = (uint32_t)((int16_t)((uint16_t)(local_rsi)));
    *(uint16_t *)(result) = 0;
    *(uint32_t *)(result + 0x2) = (uint32_t)((int16_t)((uint16_t)(v_stack_m56)));
    *(uint32_t *)(result + 0x12) = (uint32_t)((int16_t)((uint16_t)(v_stack_m56)));
    *(uint32_t *)(result + 0x16) = 0;
    *(uint64_t *)(arg3) = result;
loc_003E561A:
    result = 0;
    goto loc_003E592F;
loc_003E5621:
    result = (int16_t)((uint16_t)(v_stack_m58));
    local_r12 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x3C)) + Arg2 * 1 + 2 + 2 + 2 + 2 + (int16_t)((uint16_t)(v_stack_m58)) * 2 + 2)) <= 0) {
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10));
        local_r12 = *(uint16_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x3C)) + Arg2 * 1 + 0x2 + 0x2 + 0x2 + 0x2 + (int16_t)((uint16_t)(v_stack_m58)) * 2 + result * 1);
    }
    local_r12 = (uint16_t)((local_r12) + 1);
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x3C)) + Arg2 * 1 + 2 + 2 + 2 + 2 + (int16_t)((uint16_t)(v_stack_m58)) * 2 + 2 + 2;
    local_r10 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x3C)) + Arg2 * 1 + 2 + 2 + 2 + 2 + (int16_t)((uint16_t)(v_stack_m58)) * 2 + 2 + 2)) <= 0) {
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10));
        local_r10 = *(uint16_t *)((uint32_t)(*(uint32_t *)(arg1 + 0x3C)) + Arg2 * 1 + 0x2 + 0x2 + 0x2 + 0x2 + (int16_t)((uint16_t)(v_stack_m58)) * 2 + 0x2 + result * 1);
        v_stack_m68 = (uint16_t)(local_r10);
    }
    v_stack_m64 = (uint32_t)((uint16_t)(local_r12));
    Arg2 = ((uint16_t)(local_r12)) + (66);
    result = ((int16_t)((uint16_t)(v_stack_m58))) + ((uint16_t)(local_r12) * 4 + 8);
    v_stack_m58 = (uint16_t)(local_r12) * 4 + 8;
    local_rbp = ((uint16_t)(local_r10) + result * 2) + (Arg2);
    result = RaspAllocateMemory(local_rbp, Arg4, (uint16_t)(local_r12) * 4 + 8, (uint32_t)(*(uint32_t *)(arg1 + 0x3C)) + Arg2 * 1 + 2 + 2 + 2 + 2);
    if (result != 0) goto loc_003E56AC;
loc_003E56A2:
    goto loc_003E592F;
loc_003E56AC:
    Arg2 = 0;
    result = memset(result, Arg2, local_rbp, (uint32_t)(*(uint32_t *)(arg1 + 0x3C)) + Arg2 * 1 + 2 + 2 + 2 + 2);
    *(uint32_t *)(result + 0x6) = (uint32_t)((int16_t)((uint16_t)(v_stack_m54)));
    local_rdi = (uint32_t)(((uint32_t)(v_stack_p10)) + (10));
    local_r13 = 0;
    *(uint32_t *)(result + 0xA) = (uint32_t)((int16_t)((uint16_t)(v_stack_m52)));
    *(uint32_t *)(result + 0xE) = (uint32_t)((int16_t)(v_stack_m60));
    *(uint16_t *)(result) = (uint16_t)(v_stack_m58);
    *(uint32_t *)(result + 0x2) = (uint32_t)((int16_t)((uint16_t)(v_stack_m56)));
    *(uint32_t *)(result + 0x12) = (uint32_t)((int16_t)((uint16_t)(v_stack_m56)));
    *(uint16_t *)(result + 0x16) = (uint16_t)(v_stack_m68);
    *(uint16_t *)(result + 0x18) = (uint16_t)(local_r12);
    local_rsi = (result) + (66);
    local_rdi = (uint32_t)((local_rdi) + (*(uint32_t *)(v_stack_p8 + 0x3C)));
    *(uint64_t *)(result + 0x1A) = local_rsi;
    if (0 >= ((uint16_t)(v_stack_m58))) goto loc_003E5731;
loc_003E5717:
    result = FioFwReadUshortAtOffset(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10), (uint32_t)((uint32_t)(local_rdi)), local_rsi, (uint32_t)(*(uint32_t *)(arg1 + 0x3C)) + Arg2 * 1 + 2 + 2 + 2 + 2);
    local_rdi = (uint32_t)((local_rdi) + (2));
    local_rsi = (local_rsi) + (2);
    local_rbx = ((uint16_t)(v_stack_m58)) - (1);
    if (condition_is_not_equal) goto loc_003E5717;
loc_003E5731:
    local_rdi = (uint32_t)((local_rdi) + (2));
    *(uint64_t *)(result + 0x22) = local_rsi;
    result = FioFwReadBytesAtOffset(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10), (uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)(v_stack_m68)), local_rsi);
    local_rsi = (local_rsi) + (v_stack_m68);
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(v_stack_m68)));
    *(uint64_t *)(result + 0x2A) = local_rsi;
    result = RaspAllocateMemory((uint32_t)((uint32_t)((uint16_t)(local_r12))), v_stack_p20, (uint32_t)((uint32_t)(v_stack_m68)), local_rsi);
    v_stack_p8 = result;
    if (result != 0) goto loc_003E5788;
    result = RaspFreeMemory(result, v_stack_p20, (uint32_t)((uint32_t)(v_stack_m68)), local_rsi);
    goto loc_003E56A2;
loc_003E5788:
    result = FioFwReadBytesAtOffset(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10), (uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)((uint32_t)(v_stack_m64))), result);
    local_r11 = 0;
    if ((uint32_t)((uint32_t)(v_stack_m64)) == 0) goto loc_003E5800;
loc_003E57B0:
    Arg4 = (uint16_t)((0) + ((uint16_t)(local_r11 + 1)));
    *(uint8_t *)((int16_t)(0) + *(uint64_t *)(result + 0x2A) * 1) = (uint8_t)(*(uint8_t *)(0 + result * 1));
    if (((*(uint8_t *)(0 + result * 1)) & (8)) == 0) goto loc_003E57F4;
    Arg3 = (uint32_t)((0) + 1);
    if ((uint8_t)(*(uint8_t *)(arg3 + result * 1)) == 0) goto loc_003E57F4;
loc_003E57DC:
    Arg4 = (uint16_t)((Arg4) + ((uint16_t)(local_r11 + 1)));
    *(uint8_t *)((int16_t)((uint16_t)(Arg4)) + *(uint64_t *)(result + 0x2A) * 1) = (uint8_t)(*(uint8_t *)(0 + result * 1));
    local_r11 = ((uint32_t)((uint32_t)(*(uint8_t *)(arg3 + result * 1)))) - (local_r11 + 1);
    if (condition_is_not_equal) goto loc_003E57DC;
loc_003E57F4:
    Arg3 = (uint32_t)((Arg3) + ((uint32_t)(local_r11 + 1)));
    if (((uint32_t)((int16_t)((uint16_t)(Arg4)))) < ((uint32_t)((uint32_t)(v_stack_m64)))) goto loc_003E57B0;
loc_003E5800:
    local_rsi = (local_rsi) + ((uint16_t)(local_r12));
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(Arg3)));
    *(uint64_t *)(result + 0x32) = local_rsi;
    if ((uint32_t)((uint32_t)(v_stack_m64)) == 0) goto loc_003E5886;
loc_003E5819:
    *(uint32_t *)(local_rsi + (int16_t)((uint16_t)((uint16_t)(local_r11))) * 4) = (uint32_t)(local_r11);
    if ((((uint8_t)(*(uint8_t *)((int16_t)((uint16_t)((uint16_t)(local_r11))) + *(uint64_t *)(result + 0x2A) * 1))) & (2)) == 0) goto loc_003E5859;
    result = FioFwReadBytesAtOffset(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10), (uint32_t)((uint32_t)(local_rdi)), 1, local_rsi + (int16_t)((uint16_t)((uint16_t)(local_r11))) * 4);
    local_rdi = (uint32_t)((local_rdi) + (1));
    if (((*(uint8_t *)((int16_t)((uint16_t)((uint16_t)(local_r11))) + *(uint64_t *)(result + 0x2A) * 1)) & (16)) != 0) goto loc_003E586E;
    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(local_rsi + (int16_t)((uint16_t)((uint16_t)(local_r11))) * 4))));
    *(uint32_t *)(local_rsi + (int16_t)((uint16_t)((uint16_t)(local_r11))) * 4) = (uint32_t)(result);
    goto loc_003E586E;
loc_003E5859:
    if ((((uint8_t)((uint32_t)((uint32_t)(local_rdi)))) & (16)) != 0) goto loc_003E5871;
    result = FioFwReadUshortAtOffset(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10), (uint32_t)((uint32_t)(local_rdi)), local_rsi + (int16_t)((uint16_t)((uint16_t)(local_r11))) * 4, local_rsi + (int16_t)((uint16_t)((uint16_t)(local_r11))) * 4);
    local_rdi = (uint32_t)((local_rdi) + (2));
loc_003E586E:
    local_r11 = 0;
loc_003E5871:
    local_r15 = (uint16_t)(((uint16_t)(local_r11)) + (1));
    if (((uint32_t)((int16_t)((uint16_t)(local_r15)))) < ((uint32_t)((uint32_t)(v_stack_m64)))) goto loc_003E5819;
loc_003E5886:
    Arg1 = (v_stack_m58) + (*(uint64_t *)(result + 0x32));
    *(void **)(result + 0x3A) = Arg1;
    if ((uint32_t)((uint32_t)(v_stack_m64)) == 0) goto loc_003E590A;
loc_003E589F:
    *(uint32_t *)(arg1 + (int16_t)(0) * 4) = 0;
    if ((((uint8_t)(*(uint8_t *)((int16_t)(0) + *(uint64_t *)(result + 0x2A) * 1))) & (4)) == 0) goto loc_003E58DF;
    result = FioFwReadBytesAtOffset(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10), (uint32_t)((uint32_t)(local_rdi)), 1, Arg1 + (int16_t)(0) * 4);
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((*(uint8_t *)((int16_t)(0) + *(uint64_t *)(result + 0x2A) * 1)) & (32)) != 0) goto loc_003E58F4;
    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(arg1 + (int16_t)(0) * 4))));
    *(uint32_t *)(arg1 + (int16_t)(0) * 4) = (uint32_t)(result);
    goto loc_003E58F4;
loc_003E58DF:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10))) & (32)) != 0) goto loc_003E58F7;
    result = FioFwReadUshortAtOffset(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10), (uint32_t)((uint32_t)(local_rdi)), Arg1 + (int16_t)(0) * 4, Arg1 + (int16_t)(0) * 4);
    local_rdi = (uint32_t)((local_rdi) + (2));
loc_003E58F4:
    local_r11 = 0;
loc_003E58F7:
    local_rsi = (uint16_t)((0) + 1);
    if (((uint32_t)((int16_t)((uint16_t)(local_rsi)))) < ((uint32_t)((uint32_t)(v_stack_m64)))) goto loc_003E589F;
loc_003E590A:
    *(uint64_t *)(v_stack_p18) = result;
    result = RaspFreeMemory(v_stack_p8, v_stack_p20, Arg1 + (int16_t)(0) * 4, Arg1 + (int16_t)(0) * 4);
    goto loc_003E561A;
loc_003E592A:
loc_003E592F:
    local_rsp = (local_rsp) + (72);
    return (uint32_t)(0xC0000001ULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E54B8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
