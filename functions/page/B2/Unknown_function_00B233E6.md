# sub_00B233E6

- RVA: `0x00B233E6`–`0x00B2376A` (길이 `900` bytes)
- VA: `0x0000000140B233E6`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008EA2C`
- 디코드: `219`개 명령, `900/900` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **13**

### Outgoing calls
- `0x00B23430` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00B2371E` → [DrvDbFindDatabaseNode](../93/DrvDbFindDatabaseNode_function_00932628.md) (function, `0x00932628`)
- `0x00B23756` → [DrvDbOpenDriverDatabaseRegKey](../AA/DrvDbOpenDriverDatabaseRegKey_function_00AA0FB8.md) (function, `0x00AA0FB8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B23491` → RVA `0x000224C8` (`.rdata`; read)
- `0x00B2349E` → RVA `0x000224D0` (`.rdata`; read)
- `0x00B234EF` → RVA `0x00022368` (`.rdata`; read)
- `0x00B234FC` → RVA `0x00022370` (`.rdata`; read)
- `0x00B23548` → RVA `0x000217A0` (`.rdata`; read)
- `0x00B23555` → RVA `0x000217A8` (`.rdata`; read)
- `0x00B2359D` → RVA `0x00020C20` (`.rdata`; read)
- `0x00B235AA` → RVA `0x00020C28` (`.rdata`; read)
- `0x00B235F8` → RVA `0x00021BD8` (`.rdata`; read)
- `0x00B23605` → RVA `0x00021BE0` (`.rdata`; read)
- `0x00B2365B` → RVA `0x00022620` (`.rdata`; read)
- `0x00B23668` → RVA `0x00022628` (`.rdata`; read)
- `0x00B23707` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B23430` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **23**
  - `0x00B233E9` → [DrvDbGetDriverDatabaseMappedProperty + 0x6E](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B23436` → [DrvDbGetDriverDatabaseMappedProperty + 0x13B](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B23440` → [DrvDbGetDriverDatabaseMappedProperty + 0x13B](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B23448` → [DrvDbGetDriverDatabaseMappedProperty + 0x163](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B2344E` → [DrvDbGetDriverDatabaseMappedProperty + 0x96](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B23456` → [DrvDbGetDriverDatabaseMappedProperty + 0x13B](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B234A8` → [DrvDbGetDriverDatabaseMappedProperty + 0x13B](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B234E2` → [DrvDbGetDriverDatabaseMappedProperty + 0x13B](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B23506` → [DrvDbGetDriverDatabaseMappedProperty + 0x13B](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B2355F` → [DrvDbGetDriverDatabaseMappedProperty + 0x13B](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B23590` → [DrvDbGetDriverDatabaseMappedProperty + 0x13B](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B235B4` → [DrvDbGetDriverDatabaseMappedProperty + 0x13B](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B235EB` → [DrvDbGetDriverDatabaseMappedProperty + 0x13B](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B2360F` → [DrvDbGetDriverDatabaseMappedProperty + 0x13B](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B2364A` → [DrvDbGetDriverDatabaseMappedProperty + 0x13B](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B23652` → [DrvDbGetDriverDatabaseMappedProperty + 0x13B](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B23672` → [DrvDbGetDriverDatabaseMappedProperty + 0x13B](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B23687` → [DrvDbGetDriverDatabaseMappedProperty + 0x13B](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B236FF` → [DrvDbGetDriverDatabaseMappedProperty + 0x13B](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B23727` → [DrvDbGetDriverDatabaseMappedProperty + 0x13B](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B23737` → [DrvDbGetDriverDatabaseMappedProperty + 0xF7](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B2375F` → [DrvDbGetDriverDatabaseMappedProperty + 0x13B](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)
  - `0x00B23765` → [DrvDbGetDriverDatabaseMappedProperty + 0x10A](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B233E6  48 85 C0                        test rax, rax
00B233E9  0F 85 A7 BA E0 FF               jne 0x14092ee96
00B233EF  C7 06 12 00 00 00               mov dword ptr [rsi], 0x12
00B233F5  48 83 C8 FF                     or rax, 0xffffffffffffffff
00B233F9  48 FF C0                        inc rax
00B233FC  66 41 39 4C 45 00               cmp word ptr [r13 + rax*2], cx
00B23402  75 F5                           jne 0x140b233f9
00B23404  48 8B 4D 68                     mov rcx, qword ptr [rbp + 0x68]
00B23408  8D 04 45 02 00 00 00            lea eax, [rax*2 + 2]
00B2340F  41 89 04 24                     mov dword ptr [r12], eax
00B23413  48 85 C9                        test rcx, rcx
00B23416  74 23                           je 0x140b2343b
00B23418  39 45 70                        cmp dword ptr [rbp + 0x70], eax
00B2341B  72 1E                           jb 0x140b2343b
00B2341D  44 8B C0                        mov r8d, eax
00B23420  49 8B D5                        mov rdx, r13
00B23423  EB 0B                           jmp 0x140b23430
00B23425  48 8B 52 20                     mov rdx, qword ptr [rdx + 0x20]
00B23429  4C 8B C0                        mov r8, rax
00B2342C  48 8B 52 18                     mov rdx, qword ptr [rdx + 0x18]
00B23430  E8 0B 34 BA FF                  call 0x1406c6840
00B23435  90                              nop
00B23436  E9 28 BB E0 FF                  jmp 0x14092ef63
00B2343B  BB 23 00 00 C0                  mov ebx, 0xc0000023
00B23440  E9 1E BB E0 FF                  jmp 0x14092ef63
00B23445  48 85 C9                        test rcx, rcx
00B23448  0F 84 3D BB E0 FF               je 0x14092ef8b
00B2344E  E9 6B BA E0 FF                  jmp 0x14092eebe
00B23453  48 85 C0                        test rax, rax
00B23456  0F 85 07 BB E0 FF               jne 0x14092ef63
00B2345C  48 8B 55 68                     mov rdx, qword ptr [rbp + 0x68]
00B23460  C7 06 11 00 00 00               mov dword ptr [rsi], 0x11
00B23466  41 C7 04 24 01 00 00 00         mov dword ptr [r12], 1
00B2346E  48 85 D2                        test rdx, rdx
00B23471  74 C8                           je 0x140b2343b
00B23473  83 7D 70 01                     cmp dword ptr [rbp + 0x70], 1
00B23477  72 C2                           jb 0x140b2343b
00B23479  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00B2347D  48 8B 48 60                     mov rcx, qword ptr [rax + 0x60]
00B23481  48 F7 D9                        neg rcx
00B23484  E9 BD 01 00 00                  jmp 0x140b23646
00B23489  83 F8 06                        cmp eax, 6
00B2348C  75 59                           jne 0x140b234e7
00B2348E  48 8B 07                        mov rax, qword ptr [rdi]
00B23491  48 2B 05 30 F0 4F FF            sub rax, qword ptr [rip - 0xb00fd0]
00B23498  75 0B                           jne 0x140b234a5
00B2349A  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00B2349E  48 2B 05 2B F0 4F FF            sub rax, qword ptr [rip - 0xb00fd5]
00B234A5  48 85 C0                        test rax, rax
00B234A8  0F 85 B5 BA E0 FF               jne 0x14092ef63
00B234AE  48 8B 4D 68                     mov rcx, qword ptr [rbp + 0x68]
00B234B2  C7 06 11 00 00 00               mov dword ptr [rsi], 0x11
00B234B8  41 C7 04 24 01 00 00 00         mov dword ptr [r12], 1
00B234C0  48 85 C9                        test rcx, rcx
00B234C3  0F 84 72 FF FF FF               je 0x140b2343b
00B234C9  83 7D 70 01                     cmp dword ptr [rbp + 0x70], 1
00B234CD  0F 82 68 FF FF FF               jb 0x140b2343b
00B234D3  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00B234D7  49 39 47 30                     cmp qword ptr [r15 + 0x30], rax
00B234DB  0F 95 C0                        setne al
00B234DE  FE C8                           dec al
00B234E0  88 01                           mov byte ptr [rcx], al
00B234E2  E9 7C BA E0 FF                  jmp 0x14092ef63
00B234E7  83 F8 07                        cmp eax, 7
00B234EA  75 54                           jne 0x140b23540
00B234EC  48 8B 07                        mov rax, qword ptr [rdi]
00B234EF  48 2B 05 72 EE 4F FF            sub rax, qword ptr [rip - 0xb0118e]
00B234F6  75 0B                           jne 0x140b23503
00B234F8  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00B234FC  48 2B 05 6D EE 4F FF            sub rax, qword ptr [rip - 0xb01193]
00B23503  48 85 C0                        test rax, rax
00B23506  0F 85 57 BA E0 FF               jne 0x14092ef63
00B2350C  48 8B 55 68                     mov rdx, qword ptr [rbp + 0x68]
00B23510  C7 06 11 00 00 00               mov dword ptr [rsi], 0x11
00B23516  41 C7 04 24 01 00 00 00         mov dword ptr [r12], 1
00B2351E  48 85 D2                        test rdx, rdx
00B23521  0F 84 14 FF FF FF               je 0x140b2343b
00B23527  83 7D 70 01                     cmp dword ptr [rbp + 0x70], 1
00B2352B  0F 82 0A FF FF FF               jb 0x140b2343b
00B23531  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00B23535  8B 48 40                        mov ecx, dword ptr [rax + 0x40]
00B23538  80 E1 04                        and cl, 4
00B2353B  E9 04 01 00 00                  jmp 0x140b23644
00B23540  83 F8 0B                        cmp eax, 0xb
00B23543  75 50                           jne 0x140b23595
00B23545  48 8B 07                        mov rax, qword ptr [rdi]
00B23548  48 2B 05 51 E2 4F FF            sub rax, qword ptr [rip - 0xb01daf]
00B2354F  75 0B                           jne 0x140b2355c
00B23551  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00B23555  48 2B 05 4C E2 4F FF            sub rax, qword ptr [rip - 0xb01db4]
00B2355C  48 85 C0                        test rax, rax
00B2355F  0F 85 FE B9 E0 FF               jne 0x14092ef63
00B23565  48 8B 4D 68                     mov rcx, qword ptr [rbp + 0x68]
00B23569  C7 06 07 00 00 00               mov dword ptr [rsi], 7
00B2356F  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
00B23577  48 85 C9                        test rcx, rcx
00B2357A  0F 84 BB FE FF FF               je 0x140b2343b
00B23580  83 7D 70 04                     cmp dword ptr [rbp + 0x70], 4
00B23584  0F 82 B1 FE FF FF               jb 0x140b2343b
00B2358A  41 8B 47 0C                     mov eax, dword ptr [r15 + 0xc]
00B2358E  89 01                           mov dword ptr [rcx], eax
00B23590  E9 CE B9 E0 FF                  jmp 0x14092ef63
00B23595  83 F8 0F                        cmp eax, 0xf
00B23598  75 56                           jne 0x140b235f0
00B2359A  48 8B 07                        mov rax, qword ptr [rdi]
00B2359D  48 2B 05 7C D6 4F FF            sub rax, qword ptr [rip - 0xb02984]
00B235A4  75 0B                           jne 0x140b235b1
00B235A6  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00B235AA  48 2B 05 77 D6 4F FF            sub rax, qword ptr [rip - 0xb02989]
00B235B1  48 85 C0                        test rax, rax
00B235B4  0F 85 A9 B9 E0 FF               jne 0x14092ef63
00B235BA  48 8B 55 68                     mov rdx, qword ptr [rbp + 0x68]
00B235BE  C7 06 18 00 00 00               mov dword ptr [rsi], 0x18
00B235C4  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
00B235CC  48 85 D2                        test rdx, rdx
00B235CF  0F 84 66 FE FF FF               je 0x140b2343b
00B235D5  83 7D 70 04                     cmp dword ptr [rbp + 0x70], 4
00B235D9  0F 82 5C FE FF FF               jb 0x140b2343b
00B235DF  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00B235E3  8B 88 A0 00 00 00               mov ecx, dword ptr [rax + 0xa0]
00B235E9  89 0A                           mov dword ptr [rdx], ecx
00B235EB  E9 73 B9 E0 FF                  jmp 0x14092ef63
00B235F0  83 F8 17                        cmp eax, 0x17
00B235F3  75 5A                           jne 0x140b2364f
00B235F5  48 8B 07                        mov rax, qword ptr [rdi]
00B235F8  48 2B 05 D9 E5 4F FF            sub rax, qword ptr [rip - 0xb01a27]
00B235FF  75 0B                           jne 0x140b2360c
00B23601  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00B23605  48 2B 05 D4 E5 4F FF            sub rax, qword ptr [rip - 0xb01a2c]
00B2360C  48 85 C0                        test rax, rax
00B2360F  0F 85 4E B9 E0 FF               jne 0x14092ef63
00B23615  48 8B 55 68                     mov rdx, qword ptr [rbp + 0x68]
00B23619  C7 06 11 00 00 00               mov dword ptr [rsi], 0x11
00B2361F  41 C7 04 24 01 00 00 00         mov dword ptr [r12], 1
00B23627  48 85 D2                        test rdx, rdx
00B2362A  0F 84 0B FE FF FF               je 0x140b2343b
00B23630  83 7D 70 01                     cmp dword ptr [rbp + 0x70], 1
00B23634  0F 82 01 FE FF FF               jb 0x140b2343b
00B2363A  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
00B2363E  8B 48 40                        mov ecx, dword ptr [rax + 0x40]
00B23641  80 E1 10                        and cl, 0x10
00B23644  F6 D9                           neg cl
00B23646  1A C0                           sbb al, al
00B23648  88 02                           mov byte ptr [rdx], al
00B2364A  E9 14 B9 E0 FF                  jmp 0x14092ef63
00B2364F  83 F8 18                        cmp eax, 0x18
00B23652  0F 85 0B B9 E0 FF               jne 0x14092ef63
00B23658  48 8B 07                        mov rax, qword ptr [rdi]
00B2365B  48 2B 05 BE EF 4F FF            sub rax, qword ptr [rip - 0xb01042]
00B23662  75 0B                           jne 0x140b2366f
00B23664  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00B23668  48 2B 05 B9 EF 4F FF            sub rax, qword ptr [rip - 0xb01047]
00B2366F  48 85 C0                        test rax, rax
00B23672  0F 85 EB B8 E0 FF               jne 0x14092ef63
00B23678  48 8B 55 F0                     mov rdx, qword ptr [rbp - 0x10]
00B2367C  48 39 4A 20                     cmp qword ptr [rdx + 0x20], rcx
00B23680  75 0A                           jne 0x140b2368c
00B23682  BB 34 00 00 C0                  mov ebx, 0xc0000034
00B23687  E9 D7 B8 E0 FF                  jmp 0x14092ef63
00B2368C  C7 06 12 00 00 00               mov dword ptr [rsi], 0x12
00B23692  48 8B 42 20                     mov rax, qword ptr [rdx + 0x20]
00B23696  0F B7 48 10                     movzx ecx, word ptr [rax + 0x10]
00B2369A  83 C1 02                        add ecx, 2
00B2369D  8B C1                           mov eax, ecx
00B2369F  41 89 0C 24                     mov dword ptr [r12], ecx
00B236A3  48 8B 4D 68                     mov rcx, qword ptr [rbp + 0x68]
00B236A7  48 85 C9                        test rcx, rcx
00B236AA  0F 84 8B FD FF FF               je 0x140b2343b
00B236B0  39 45 70                        cmp dword ptr [rbp + 0x70], eax
00B236B3  0F 82 82 FD FF FF               jb 0x140b2343b
00B236B9  E9 67 FD FF FF                  jmp 0x140b23425
00B236BE  83 FA 04                        cmp edx, 4
00B236C1  73 32                           jae 0x140b236f5
00B236C3  4D 8D 88 C0 CE 00 00            lea r9, [r8 + 0xcec0]
00B236CA  8B C2                           mov eax, edx
00B236CC  48 8D 0C 80                     lea rcx, [rax + rax*4]
00B236D0  4D 8D 0C C9                     lea r9, [r9 + rcx*8]
00B236D4  4D 8B 01                        mov r8, qword ptr [r9]
00B236D7  45 39 50 10                     cmp dword ptr [r8 + 0x10], r10d
00B236DB  75 27                           jne 0x140b23704
00B236DD  49 8B 08                        mov rcx, qword ptr [r8]
00B236E0  48 2B 0F                        sub rcx, qword ptr [rdi]
00B236E3  75 08                           jne 0x140b236ed
00B236E5  49 8B 48 08                     mov rcx, qword ptr [r8 + 8]
00B236E9  48 2B 4F 08                     sub rcx, qword ptr [rdi + 8]
00B236ED  48 85 C9                        test rcx, rcx
00B236F0  75 12                           jne 0x140b23704
00B236F2  4D 8B F9                        mov r15, r9
00B236F5  4D 85 FF                        test r15, r15
00B236F8  75 16                           jne 0x140b23710
00B236FA  BB 16 00 00 C0                  mov ebx, 0xc0000016
00B236FF  E9 5F B8 E0 FF                  jmp 0x14092ef63
00B23704  41 03 D3                        add edx, r11d
00B23707  4C 8D 05 F2 C8 4D FF            lea r8, [rip - 0xb2370e]
00B2370E  EB AE                           jmp 0x140b236be
00B23710  48 8B 7D 40                     mov rdi, qword ptr [rbp + 0x40]
00B23714  4C 8D 45 F0                     lea r8, [rbp - 0x10]
00B23718  48 8B CF                        mov rcx, rdi
00B2371B  49 8B D5                        mov rdx, r13
00B2371E  E8 05 EF E0 FF                  call 0x140932628
00B23723  8B D8                           mov ebx, eax
00B23725  85 C0                           test eax, eax
00B23727  0F 88 36 B8 E0 FF               js 0x14092ef63
00B2372D  4C 8B 75 F0                     mov r14, qword ptr [rbp - 0x10]
00B23731  33 DB                           xor ebx, ebx
00B23733  44 8D 5B 01                     lea r11d, [rbx + 1]
00B23737  E9 E3 B7 E0 FF                  jmp 0x14092ef1f
00B2373C  48 8D 45 F8                     lea rax, [rbp - 8]
00B23740  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00B23745  45 33 C9                        xor r9d, r9d
00B23748  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B2374D  45 8B C3                        mov r8d, r11d
00B23750  49 8B D5                        mov rdx, r13
00B23753  48 8B CF                        mov rcx, rdi
00B23756  E8 5D D8 F7 FF                  call 0x140aa0fb8
00B2375B  8B D8                           mov ebx, eax
00B2375D  85 C0                           test eax, eax
00B2375F  0F 88 FE B7 E0 FF               js 0x14092ef63
00B23765  E9 C8 B7 E0 FF                  jmp 0x14092ef32
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B233E6(unsigned __int16 a1)
{
    __int64 result;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;

    *(unsigned int *)(v_rsi) = 18;
    result = (result) | (-1);
loc_00B233F9:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_r13 + result * 2)) != a1) goto loc_00B233F9;
    *(unsigned int *)(v_r12) = (unsigned int)(result * 2 + 2);
    if (*(unsigned __int64 *)(v_rbp + 104) == 0) goto loc_00B2343B;
    if ((*(unsigned int *)(v_rbp + 112)) < ((unsigned int)(result * 2 + 2))) goto loc_00B2343B;
    goto loc_00B23430;
loc_00B23430:
    result = memcpy(*(unsigned __int64 *)(v_rbp + 104), v_r13, (unsigned int)((unsigned int)(result * 2 + 2)), a4);
loc_00B2343B:
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B233E6(uint16_t Arg1)
{
    int64_t result;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;

    *(uint32_t *)(local_rsi) = 18;
    result = (result) | (-1);
loc_00B233F9:
    result = (result) + 1;
    if ((*(uint16_t *)(local_r13 + result * 2)) != Arg1) goto loc_00B233F9;
    *(uint32_t *)(local_r12) = (uint32_t)(result * 2 + 2);
    if (*(uint64_t *)(local_rbp + 0x68) == 0) goto loc_00B2343B;
    if ((*(uint32_t *)(local_rbp + 0x70)) < ((uint32_t)(result * 2 + 2))) goto loc_00B2343B;
    goto loc_00B23430;
loc_00B23430:
    result = memcpy(*(uint64_t *)(local_rbp + 0x68), local_r13, (uint32_t)((uint32_t)(result * 2 + 2)), a4);
loc_00B2343B:
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B233E6&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
