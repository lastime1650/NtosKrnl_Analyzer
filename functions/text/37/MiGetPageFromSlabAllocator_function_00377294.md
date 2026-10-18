# MiGetPageFromSlabAllocator

- RVA: `0x00377294`–`0x00377760` (길이 `1,228` bytes)
- VA: `0x0000000140377294`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007AD24`
- 디코드: `315`개 명령, `1,228/1,228` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x003772F0` → [ExAcquireSpinLockSharedAtDpcLevel](../24/ExAcquireSpinLockSharedAtDpcLevel_function_00248E30.md) (function, `0x00248E30`)
- `0x0037732B` → [MiGetPageFromSlabEntry](MiGetPageFromSlabEntry_function_00377768.md) (function, `0x00377768`)
- `0x00377399` → [MiGetPageFromSlabEntry](MiGetPageFromSlabEntry_function_00377768.md) (function, `0x00377768`)
- `0x003773D4` → [MiReleaseSpinLockShared](../34/MiReleaseSpinLockShared_function_00348BF0.md) (function, `0x00348BF0`)
- `0x00377415` → [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x0037742D` → [MiUpdateSlabPagePlaceholderState](../2A/MiUpdateSlabPagePlaceholderState_function_002A0FB0.md) (function, `0x002A0FB0`)
- `0x00377438` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x00377447` → [MiGetRepurposedSlabStandbyPage](MiGetRepurposedSlabStandbyPage_function_003755A8.md) (function, `0x003755A8`)
- `0x003774B7` → [MiAsyncSlabReplenish](../4A/MiAsyncSlabReplenish_function_004AA54C.md) (function, `0x004AA54C`)
- `0x003774BE` → [ExAcquireSpinLockShared](../24/ExAcquireSpinLockShared_function_0024DCE0.md) (function, `0x0024DCE0`)
- `0x003774E2` → [MiRepurposeStandbySlabPage](../38/MiRepurposeStandbySlabPage_function_00385780.md) (function, `0x00385780`)
- `0x0037750A` → [MiRepurposeStandbySlabPage](../38/MiRepurposeStandbySlabPage_function_00385780.md) (function, `0x00385780`)
- `0x00377556` → [MiGetPageFromSlabEntry](MiGetPageFromSlabEntry_function_00377768.md) (function, `0x00377768`)
- `0x00377663` → [MiGetCurrentSlabIdentity](../3B/MiGetCurrentSlabIdentity_function_003BD020.md) (function, `0x003BD020`)
- `0x0037767E` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0037768D` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003776FE` → [MiGetPageFromSlabAllocatorByIdentity](../4D/MiGetPageFromSlabAllocatorByIdentity_function_004D50A0.md) (function, `0x004D50A0`)
- `0x00377749` → [MiGetPageFromSlabEntry](MiGetPageFromSlabEntry_function_00377768.md) (function, `0x00377768`)

### Direct callers
- [MiGetSlabPage](MiGetSlabPage_function_00376FBC.md) at `0x00377074`

### Static image references
- `0x003775B9` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00377670` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x003776AD` → [sub_006E3F8C](../6E/Unknown_function_006E3F8C.md) (`tail-transfer`)
  - `0x003776B9` → [sub_006E3F8C](../6E/Unknown_function_006E3F8C.md) (`tail-transfer`)
  - `0x003776CE` → [sub_006E3F8C](../6E/Unknown_function_006E3F8C.md) (`tail-transfer`)
  - `0x0037771A` → [sub_006E3F8C + 0x36](../6E/Unknown_function_006E3F8C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00377294  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00377299  55                              push rbp
0037729A  56                              push rsi
0037729B  57                              push rdi
0037729C  41 54                           push r12
0037729E  41 55                           push r13
003772A0  41 56                           push r14
003772A2  41 57                           push r15
003772A4  48 83 EC 20                     sub rsp, 0x20
003772A8  83 B9 80 00 00 00 08            cmp dword ptr [rcx + 0x80], 8
003772AF  44 8B EA                        mov r13d, edx
003772B2  48 8B D9                        mov rbx, rcx
003772B5  0F 84 9F 03 00 00               je 0x14037765a
003772BB  40 B5 FF                        mov bpl, 0xff
003772BE  48 8B 43 60                     mov rax, qword ptr [rbx + 0x60]
003772C2  40 8A F5                        mov sil, bpl
003772C5  40 88 6C 24 70                  mov byte ptr [rsp + 0x70], bpl
003772CA  48 85 C0                        test rax, rax
003772CD  0F 84 71 01 00 00               je 0x140377444
003772D3  49 83 CC FF                     or r12, 0xffffffffffffffff
003772D7  48 8D 73 10                     lea rsi, [rbx + 0x10]
003772DB  45 8B F5                        mov r14d, r13d
003772DE  48 8B CE                        mov rcx, rsi
003772E1  41 83 E6 10                     and r14d, 0x10
003772E5  0F 84 D3 01 00 00               je 0x1403774be
003772EB  C6 44 24 60 11                  mov byte ptr [rsp + 0x60], 0x11
003772F0  E8 3B 1B ED FF                  call 0x140248e30
003772F5  83 BB 80 00 00 00 08            cmp dword ptr [rbx + 0x80], 8
003772FC  0F 84 D0 02 00 00               je 0x1403775d2
00377302  48 8D 4B 20                     lea rcx, [rbx + 0x20]
00377306  48 85 C9                        test rcx, rcx
00377309  74 56                           je 0x140377361
0037730B  48 8B 09                        mov rcx, qword ptr [rcx]
0037730E  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00377313  48 85 C9                        test rcx, rcx
00377316  74 49                           je 0x140377361
00377318  40 80 FD FF                     cmp bpl, 0xff
0037731C  0F 85 87 03 00 00               jne 0x1403776a9
00377322  48 83 F9 01                     cmp rcx, 1
00377326  74 1B                           je 0x140377343
00377328  48 8B D3                        mov rdx, rbx
0037732B  E8 38 04 00 00                  call 0x140377768
00377330  48 8B F8                        mov rdi, rax
00377333  48 83 F8 FF                     cmp rax, -1
00377337  0F 85 38 01 00 00               jne 0x140377475
0037733D  48 83 64 24 78 00               and qword ptr [rsp + 0x78], 0
00377343  83 BB 80 00 00 00 08            cmp dword ptr [rbx + 0x80], 8
0037734A  0F 84 EF 02 00 00               je 0x14037763f
00377350  48 8D 53 20                     lea rdx, [rbx + 0x20]
00377354  48 85 D2                        test rdx, rdx
00377357  74 08                           je 0x140377361
00377359  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0037735E  48 89 02                        mov qword ptr [rdx], rax
00377361  83 BB 80 00 00 00 08            cmp dword ptr [rbx + 0x80], 8
00377368  0F 84 B6 02 00 00               je 0x140377624
0037736E  48 8D 53 28                     lea rdx, [rbx + 0x28]
00377372  48 85 D2                        test rdx, rdx
00377375  0F 84 9C 01 00 00               je 0x140377517
0037737B  48 8B 0A                        mov rcx, qword ptr [rdx]
0037737E  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00377383  48 85 C9                        test rcx, rcx
00377386  0F 84 91 01 00 00               je 0x14037751d
0037738C  40 80 FD FF                     cmp bpl, 0xff
00377390  0F 85 3D 03 00 00               jne 0x1403776d3
00377396  48 8B D3                        mov rdx, rbx
00377399  E8 CA 03 00 00                  call 0x140377768
0037739E  48 8B F8                        mov rdi, rax
003773A1  48 83 F8 FF                     cmp rax, -1
003773A5  0F 84 72 01 00 00               je 0x14037751d
003773AB  41 B6 11                        mov r14b, 0x11
003773AE  83 BB 80 00 00 00 08            cmp dword ptr [rbx + 0x80], 8
003773B5  0F 84 32 02 00 00               je 0x1403775ed
003773BB  48 8D 53 20                     lea rdx, [rbx + 0x20]
003773BF  48 85 D2                        test rdx, rdx
003773C2  74 08                           je 0x1403773cc
003773C4  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
003773C9  48 89 02                        mov qword ptr [rdx], rax
003773CC  8A 54 24 60                     mov dl, byte ptr [rsp + 0x60]
003773D0  48 8D 4B 10                     lea rcx, [rbx + 0x10]
003773D4  E8 17 18 FD FF                  call 0x140348bf0
003773D9  48 83 FF FF                     cmp rdi, -1
003773DD  74 60                           je 0x14037743f
003773DF  8B 83 80 00 00 00               mov eax, dword ptr [rbx + 0x80]
003773E5  85 C0                           test eax, eax
003773E7  78 6C                           js 0x140377455
003773E9  83 F8 04                        cmp eax, 4
003773EC  7F 67                           jg 0x140377455
003773EE  83 F8 02                        cmp eax, 2
003773F1  74 62                           je 0x140377455
003773F3  48 8D 34 7F                     lea rsi, [rdi + rdi*2]
003773F7  48 C1 E6 04                     shl rsi, 4
003773FB  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00377405  48 03 F0                        add rsi, rax
00377408  41 F6 C5 10                     test r13b, 0x10
0037740C  0F 85 96 01 00 00               jne 0x1403775a8
00377412  48 8B CE                        mov rcx, rsi
00377415  E8 26 2F FA FF                  call 0x14031a340
0037741A  44 8A F0                        mov r14b, al
0037741D  8B 8B 80 00 00 00               mov ecx, dword ptr [rbx + 0x80]
00377423  45 33 C9                        xor r9d, r9d
00377426  48 8B D7                        mov rdx, rdi
00377429  45 8D 41 01                     lea r8d, [r9 + 1]
0037742D  E8 7E 9B F2 FF                  call 0x1402a0fb0
00377432  41 8A D6                        mov dl, r14b
00377435  48 8B CE                        mov rcx, rsi
00377438  E8 A3 2F FA FF                  call 0x14031a3e0
0037743D  EB 16                           jmp 0x140377455
0037743F  40 8A 74 24 70                  mov sil, byte ptr [rsp + 0x70]
00377444  48 8B CB                        mov rcx, rbx
00377447  E8 5C E1 FF FF                  call 0x1403755a8
0037744C  48 8B F8                        mov rdi, rax
0037744F  48 83 F8 FF                     cmp rax, -1
00377453  74 77                           je 0x1403774cc
00377455  48 83 7B 68 00                  cmp qword ptr [rbx + 0x68], 0
0037745A  75 21                           jne 0x14037747d
0037745C  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
00377461  48 8B C7                        mov rax, rdi
00377464  48 83 C4 20                     add rsp, 0x20
00377468  41 5F                           pop r15
0037746A  41 5E                           pop r14
0037746C  41 5D                           pop r13
0037746E  41 5C                           pop r12
00377470  5F                              pop rdi
00377471  5E                              pop rsi
00377472  5D                              pop rbp
00377473  C3                              ret
00377474  CC                              int3
00377475  41 B6 11                        mov r14b, 0x11
00377478  E9 4F FF FF FF                  jmp 0x1403773cc
0037747D  48 8B 83 D0 00 00 00            mov rax, qword ptr [rbx + 0xd0]
00377484  48 85 C0                        test rax, rax
00377487  75 D3                           jne 0x14037745c
00377489  48 8B 53 60                     mov rdx, qword ptr [rbx + 0x60]
0037748D  48 8B 43 50                     mov rax, qword ptr [rbx + 0x50]
00377491  4C 8B 00                        mov r8, qword ptr [rax]
00377494  48 8B 43 68                     mov rax, qword ptr [rbx + 0x68]
00377498  4C 03 C2                        add r8, rdx
0037749B  48 D1 E8                        shr rax, 1
0037749E  4C 3B C0                        cmp r8, rax
003774A1  77 B9                           ja 0x14037745c
003774A3  41 83 E5 10                     and r13d, 0x10
003774A7  33 D2                           xor edx, edx
003774A9  41 83 CD 04                     or r13d, 4
003774AD  48 8B CB                        mov rcx, rbx
003774B0  41 C1 ED 02                     shr r13d, 2
003774B4  45 8B C5                        mov r8d, r13d
003774B7  E8 90 30 13 00                  call 0x1404aa54c
003774BC  EB 9E                           jmp 0x14037745c
003774BE  E8 1D 68 ED FF                  call 0x14024dce0
003774C3  88 44 24 60                     mov byte ptr [rsp + 0x60], al
003774C7  E9 29 FE FF FF                  jmp 0x1403772f5
003774CC  48 8B 83 B0 00 00 00            mov rax, qword ptr [rbx + 0xb0]
003774D3  48 85 C0                        test rax, rax
003774D6  0F 84 79 FF FF FF               je 0x140377455
003774DC  40 8A D6                        mov dl, sil
003774DF  48 8B CB                        mov rcx, rbx
003774E2  E8 99 E2 00 00                  call 0x140385780
003774E7  48 8B F8                        mov rdi, rax
003774EA  48 83 F8 FF                     cmp rax, -1
003774EE  0F 85 61 FF FF FF               jne 0x140377455
003774F4  40 80 FE FF                     cmp sil, 0xff
003774F8  0F 84 57 FF FF FF               je 0x140377455
003774FE  F0 FF 83 A4 00 00 00            lock inc dword ptr [rbx + 0xa4]
00377505  B2 FF                           mov dl, 0xff
00377507  48 8B CB                        mov rcx, rbx
0037750A  E8 71 E2 00 00                  call 0x140385780
0037750F  48 8B F8                        mov rdi, rax
00377512  E9 3E FF FF FF                  jmp 0x140377455
00377517  48 83 64 24 78 00               and qword ptr [rsp + 0x78], 0
0037751D  45 33 FF                        xor r15d, r15d
00377520  40 80 FD FF                     cmp bpl, 0xff
00377524  0F 85 C9 01 00 00               jne 0x1403776f3
0037752A  41 B6 11                        mov r14b, 0x11
0037752D  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00377531  A8 01                           test al, 1
00377533  0F 85 CF 00 00 00               jne 0x140377608
00377539  48 8B F0                        mov rsi, rax
0037753C  48 85 F6                        test rsi, rsi
0037753F  0F 84 52 01 00 00               je 0x140377697
00377545  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
0037754A  48 3B 73 30                     cmp rsi, qword ptr [rbx + 0x30]
0037754E  74 53                           je 0x1403775a3
00377550  48 8B D3                        mov rdx, rbx
00377553  48 8B CE                        mov rcx, rsi
00377556  E8 0D 02 00 00                  call 0x140377768
0037755B  48 8B F8                        mov rdi, rax
0037755E  48 83 F8 FF                     cmp rax, -1
00377562  0F 85 46 FE FF FF               jne 0x1403773ae
00377568  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0037756C  48 8B CE                        mov rcx, rsi
0037756F  48 85 C0                        test rax, rax
00377572  74 1B                           je 0x14037758f
00377574  48 8B 08                        mov rcx, qword ptr [rax]
00377577  48 8B F0                        mov rsi, rax
0037757A  48 85 C9                        test rcx, rcx
0037757D  74 BD                           je 0x14037753c
0037757F  48 8B 01                        mov rax, qword ptr [rcx]
00377582  48 8B F1                        mov rsi, rcx
00377585  48 8B C8                        mov rcx, rax
00377588  48 85 C0                        test rax, rax
0037758B  75 F2                           jne 0x14037757f
0037758D  EB AD                           jmp 0x14037753c
0037758F  48 8B 76 10                     mov rsi, qword ptr [rsi + 0x10]
00377593  48 83 E6 FC                     and rsi, 0xfffffffffffffffc
00377597  74 A3                           je 0x14037753c
00377599  48 39 0E                        cmp qword ptr [rsi], rcx
0037759C  74 9E                           je 0x14037753c
0037759E  48 8B CE                        mov rcx, rsi
003775A1  EB EC                           jmp 0x14037758f
003775A3  4C 8B FE                        mov r15, rsi
003775A6  EB C0                           jmp 0x140377568
003775A8  33 ED                           xor ebp, ebp
003775AA  F0 48 0F BA 6E 18 3F            lock bts qword ptr [rsi + 0x18], 0x3f
003775B1  0F 83 66 FE FF FF               jae 0x14037741d
003775B7  FF C5                           inc ebp
003775B9  85 2D ED DC C4 00               test dword ptr [rip + 0xc4dced], ebp
003775BF  0F 84 AB 00 00 00               je 0x140377670
003775C5  F3 90                           pause
003775C7  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
003775CB  48 85 C0                        test rax, rax
003775CE  79 DA                           jns 0x1403775aa
003775D0  EB E5                           jmp 0x1403775b7
003775D2  40 80 FD FF                     cmp bpl, 0xff
003775D6  0F 84 85 FD FF FF               je 0x140377361
003775DC  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
003775E0  40 0F B6 D5                     movzx edx, bpl
003775E4  48 8D 0C D1                     lea rcx, [rcx + rdx*8]
003775E8  E9 19 FD FF FF                  jmp 0x140377306
003775ED  40 80 FD FF                     cmp bpl, 0xff
003775F1  0F 84 D5 FD FF FF               je 0x1403773cc
003775F7  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
003775FB  40 0F B6 CD                     movzx ecx, bpl
003775FF  48 8D 14 C8                     lea rdx, [rax + rcx*8]
00377603  E9 B7 FD FF FF                  jmp 0x1403773bf
00377608  48 83 F8 01                     cmp rax, 1
0037760C  74 0F                           je 0x14037761d
0037760E  48 8B F3                        mov rsi, rbx
00377611  48 83 CE 01                     or rsi, 1
00377615  48 33 F0                        xor rsi, rax
00377618  E9 1F FF FF FF                  jmp 0x14037753c
0037761D  33 F6                           xor esi, esi
0037761F  E9 18 FF FF FF                  jmp 0x14037753c
00377624  40 80 FD FF                     cmp bpl, 0xff
00377628  0F 84 E9 FE FF FF               je 0x140377517
0037762E  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
00377632  40 0F B6 CD                     movzx ecx, bpl
00377636  48 8D 14 C8                     lea rdx, [rax + rcx*8]
0037763A  E9 33 FD FF FF                  jmp 0x140377372
0037763F  40 80 FD FF                     cmp bpl, 0xff
00377643  0F 84 18 FD FF FF               je 0x140377361
00377649  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
0037764D  40 0F B6 CD                     movzx ecx, bpl
00377651  48 8D 14 C8                     lea rdx, [rax + rcx*8]
00377655  E9 FA FC FF FF                  jmp 0x140377354
0037765A  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00377663  E8 B8 59 04 00                  call 0x1403bd020
00377668  40 8A E8                        mov bpl, al
0037766B  E9 4E FC FF FF                  jmp 0x1403772be
00377670  8B 05 42 F4 C4 00               mov eax, dword ptr [rip + 0xc4f442]
00377676  A8 40                           test al, 0x40
00377678  0F 84 47 FF FF FF               je 0x1403775c5
0037767E  E8 0D 7E F9 FF                  call 0x14030f490
00377683  84 C0                           test al, al
00377685  0F 84 3A FF FF FF               je 0x1403775c5
0037768B  8B CD                           mov ecx, ebp
0037768D  E8 CE 7D F9 FF                  call 0x14030f460
00377692  E9 30 FF FF FF                  jmp 0x1403775c7
00377697  4D 85 FF                        test r15, r15
0037769A  0F 85 88 00 00 00               jne 0x140377728
003776A0  48 83 CF FF                     or rdi, 0xffffffffffffffff
003776A4  E9 23 FD FF FF                  jmp 0x1403773cc
003776A9  48 83 F9 01                     cmp rcx, 1
003776AD  0F 84 D9 C8 36 00               je 0x1406e3f8c
003776B3  8B 51 5C                        mov edx, dword ptr [rcx + 0x5c]
003776B6  F6 C2 04                        test dl, 4
003776B9  0F 84 CD C8 36 00               je 0x1406e3f8c
003776BF  C1 EA 03                        shr edx, 3
003776C2  83 E2 3F                        and edx, 0x3f
003776C5  40 3A D5                        cmp dl, bpl
003776C8  0F 84 5A FC FF FF               je 0x140377328
003776CE  E9 B9 C8 36 00                  jmp 0x1406e3f8c
003776D3  8B 51 5C                        mov edx, dword ptr [rcx + 0x5c]
003776D6  F6 C2 04                        test dl, 4
003776D9  0F 84 3E FE FF FF               je 0x14037751d
003776DF  C1 EA 03                        shr edx, 3
003776E2  83 E2 3F                        and edx, 0x3f
003776E5  40 3A D5                        cmp dl, bpl
003776E8  0F 85 2F FE FF FF               jne 0x14037751d
003776EE  E9 A3 FC FF FF                  jmp 0x140377396
003776F3  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
003776F8  40 8A D5                        mov dl, bpl
003776FB  48 8B CB                        mov rcx, rbx
003776FE  E8 9D D9 15 00                  call 0x1404d50a0
00377703  48 8B F8                        mov rdi, rax
00377706  48 83 F8 FF                     cmp rax, -1
0037770A  0F 85 9B FC FF FF               jne 0x1403773ab
00377710  48 8B 83 B0 00 00 00            mov rax, qword ptr [rbx + 0xb0]
00377717  48 85 C0                        test rax, rax
0037771A  0F 85 A2 C8 36 00               jne 0x1406e3fc2
00377720  48 0B FF                        or rdi, rdi
00377723  E9 83 FC FF FF                  jmp 0x1403773ab
00377728  48 8B 43 50                     mov rax, qword ptr [rbx + 0x50]
0037772C  48 8B 10                        mov rdx, qword ptr [rax]
0037772F  48 85 D2                        test rdx, rdx
00377732  0F 85 68 FF FF FF               jne 0x1403776a0
00377738  49 8B C7                        mov rax, r15
0037773B  48 8B D3                        mov rdx, rbx
0037773E  48 83 C8 02                     or rax, 2
00377742  49 8B CF                        mov rcx, r15
00377745  48 89 43 30                     mov qword ptr [rbx + 0x30], rax
00377749  E8 1A 00 00 00                  call 0x140377768
0037774E  48 8B F8                        mov rdi, rax
00377751  48 83 F8 FF                     cmp rax, -1
00377755  0F 84 45 FF FF FF               je 0x1403776a0
0037775B  E9 4E FC FF FF                  jmp 0x1403773ae
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetPageFromSlabAllocator(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p60;
    unsigned __int64 v_stack_p78;
    unsigned __int8 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(a1 + 128)) == 8) goto loc_0037765A;
loc_003772BE:
    v_stack_p18 = 255;
    if (*(unsigned __int64 *)(a1 + 96) == 0) goto loc_00377444;
    v_r12 = (v_r12) | (-1);
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) & (16));
    if (condition_is_equal) goto loc_003774BE;
    v_stack_p8 = 17;
    result = ExAcquireSpinLockSharedAtDpcLevel(a1 + 16, a2, a3, a4);
loc_003772F5:
    if ((*(unsigned int *)(a1 + 128)) == 8) goto loc_003775D2;
loc_00377306:
    if (a1 + 32 == 0) goto loc_00377361;
    v_stack_p20 = *(unsigned __int64 *)(a1 + 32);
    if (*(unsigned __int64 *)(a1 + 32) == 0) goto loc_00377361;
    if (255 != 255) goto loc_003776A9;
    if ((*(unsigned __int64 *)(a1 + 32)) == 1) goto loc_00377343;
loc_00377328:
    result = MiGetPageFromSlabEntry(*(unsigned __int64 *)(a1 + 32), a1, a3, a4);
    if (result != -1) goto loc_00377475;
loc_00377343:
    if ((*(unsigned int *)(a1 + 128)) == 8) goto loc_0037763F;
loc_00377354:
    if (a1 + 32 != 0) {
        result = v_stack_p20;
        *(unsigned __int64 *)(a1 + 32) = result;
    }
    if ((*(unsigned int *)(a1 + 128)) == 8) goto loc_00377624;
loc_00377372:
    if (a1 + 40 == 0) goto loc_00377517;
    v_stack_p20 = *(unsigned __int64 *)(a1 + 40);
    if (*(unsigned __int64 *)(a1 + 40) == 0) goto loc_0037751D;
    if (255 != 255) goto loc_003776D3;
loc_00377396:
    result = MiGetPageFromSlabEntry(*(unsigned __int64 *)(a1 + 40), a1, a3, a4);
    if (result == -1) goto loc_0037751D;
loc_003773AB:
loc_003773AE:
    if ((*(unsigned int *)(a1 + 128)) == 8) goto loc_003775ED;
loc_003773BF:
    if (a1 + 32 != 0) {
        result = v_stack_p20;
        *(unsigned __int64 *)(a1 + 32) = result;
    }
    result = MiReleaseSpinLockShared(a1 + 16, v_stack_p8, a3, a4);
    if (result == -1) goto loc_0037743F;
    if (sign_flag) goto loc_00377455;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 128)))) > 4) goto loc_00377455;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 128)))) == 2) goto loc_00377455;
    v_rsi = (result + result * 2) << (4);
    v_rsi = (v_rsi) + ((unsigned int)(*(unsigned int *)(a1 + 128)));
    if ((((unsigned __int8)((unsigned int)(a2))) & (16)) != 0) goto loc_003775A8;
    result = MiLockPageInline(v_rsi, v_stack_p8, a3, a4);
loc_0037741D:
    a4 = 0;
    result = MiUpdateSlabPagePlaceholderState((unsigned int)(*(unsigned int *)(a1 + 128)), result, a4 + 1, a4);
    result = MiUnlockPage(v_rsi, (unsigned __int8)((unsigned __int8)(result)), a4 + 1, a4);
    goto loc_00377455;
loc_0037743F:
loc_00377444:
    result = MiGetRepurposedSlabStandbyPage(a1, (unsigned __int8)((unsigned __int8)(result)), a4 + 1, a4);
    if (result == -1) goto loc_003774CC;
loc_00377455:
    if ((*(unsigned __int64 *)(a1 + 104)) != 0) goto loc_0037747D;
loc_0037745C:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00377475:
    goto loc_003773CC;
loc_0037747D:
    if (*(unsigned __int64 *)(v_stack_p10 + 208) != 0) goto loc_0037745C;
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 80))) + (*(unsigned __int64 *)(v_stack_p10 + 96));
    result = (*(unsigned __int64 *)(v_stack_p10 + 104)) >> (1);
    if (a3 > result) goto loc_0037745C;
    v_r13 = (unsigned int)(((unsigned int)(a2)) & (16));
    a2 = 0;
    v_r13 = (unsigned int)((v_r13) | (4));
    v_r13 = (unsigned int)((v_r13) >> (2));
    result = MiAsyncSlabReplenish(v_stack_p10, a2, (unsigned int)((unsigned int)(v_r13)), a4);
    goto loc_0037745C;
loc_003774BE:
    result = ExAcquireSpinLockShared(v_stack_p10, a2, (unsigned int)((unsigned int)(v_r13)), a4);
    v_stack_p60 = (unsigned __int8)(result);
    goto loc_003772F5;
loc_003774CC:
    if (*(unsigned __int64 *)(v_stack_p10 + 176) == 0) goto loc_00377455;
    result = MiRepurposeStandbySlabPage(v_stack_p10, (unsigned __int8)(v_stack_p18), (unsigned int)((unsigned int)(v_r13)), a4);
    if (result != -1) goto loc_00377455;
    if (((unsigned __int8)(v_stack_p18)) == 255) goto loc_00377455;
    result = MiRepurposeStandbySlabPage(v_stack_p10, 255, (unsigned int)((unsigned int)(v_r13)), a4);
    goto loc_00377455;
loc_00377517:
loc_0037751D:
    v_r15 = 0;
    if (255 != 255) goto loc_003776F3;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p10 + 8))) & (1)) != 0) goto loc_00377608;
loc_0037753C:
    if (*(unsigned __int64 *)(v_stack_p10 + 8) == 0) goto loc_00377697;
    v_stack_p78 = *(unsigned __int64 *)(v_stack_p10 + 8);
    if ((*(unsigned __int64 *)(v_stack_p10 + 8)) == (*(unsigned __int64 *)(v_stack_p10 + 48))) goto loc_003775A3;
    result = MiGetPageFromSlabEntry(*(unsigned __int64 *)(v_stack_p10 + 8), v_stack_p10, (unsigned int)((unsigned int)(v_r13)), a4);
    if (result != -1) goto loc_003773AE;
loc_00377568:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 8) + 8) == 0) goto loc_0037758F;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 8) + 8)) == 0) goto loc_0037753C;
loc_0037757F:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 8) + 8))) != 0) goto loc_0037757F;
    goto loc_0037753C;
loc_0037758F:
    v_rsi = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 8) + 8)) + 16)) & (-4);
    if (condition_is_equal) goto loc_0037753C;
    if ((*(unsigned __int64 *)(v_rsi)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 8) + 8))))) goto loc_0037753C;
    goto loc_0037758F;
loc_003775A3:
    goto loc_00377568;
loc_003775A8:
    v_rbp = 0;
loc_003775AA:
    if (condition_is_above_or_equal) goto loc_0037741D;
loc_003775B7:
    v_rbp = (unsigned int)((v_rbp) + 1);
    if (((*(unsigned int *)(v_rip + 12901613)) & ((unsigned int)(v_rbp))) == 0) goto loc_00377670;
loc_003775C5:
loc_003775C7:
    if (!sign_flag) goto loc_003775AA;
    goto loc_003775B7;
loc_003775D2:
    if (((unsigned __int8)(v_rbp)) == 255) goto loc_00377361;
    goto loc_00377306;
loc_003775ED:
    if (((unsigned __int8)(v_rbp)) == 255) goto loc_003773CC;
    goto loc_003773BF;
loc_00377608:
    if ((*(unsigned __int64 *)(v_stack_p10 + 32)) == 1) goto loc_0037761D;
    v_rsi = (v_stack_p10) | (1);
    v_rsi = (v_rsi) ^ (*(unsigned __int64 *)(v_stack_p10 + 32));
    goto loc_0037753C;
loc_0037761D:
    v_rsi = 0;
    goto loc_0037753C;
loc_00377624:
    if (((unsigned __int8)(v_rbp)) == 255) goto loc_00377517;
    goto loc_00377372;
loc_0037763F:
    if (((unsigned __int8)(v_rbp)) == 255) goto loc_00377361;
    goto loc_00377354;
loc_0037765A:
    result = MiGetCurrentSlabIdentity(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(v_stack_p10 + 32) + (unsigned __int8)(v_rbp) * 8, (unsigned int)((unsigned int)(v_r13)), a4);
    goto loc_003772BE;
loc_00377670:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12907586)))) & (64)) == 0) goto loc_003775C5;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(v_stack_p10 + 32) + (unsigned __int8)(v_rbp) * 8, (unsigned int)((unsigned int)(v_r13)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_003775C5;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((unsigned __int8)(result))), *(unsigned __int64 *)(v_stack_p10 + 32) + (unsigned __int8)(v_rbp) * 8, (unsigned int)((unsigned int)(v_r13)), a4);
    goto loc_003775C7;
loc_00377697:
    if (0 != 0) goto loc_00377728;
loc_003776A0:
    v_rdi = (result) | (-1);
    goto loc_003773CC;
loc_003776A9:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned __int8)(result))) + 92))) >> (3));
    a2 = (unsigned int)((a2) & (63));
    if (((unsigned __int8)(a2)) == ((unsigned __int8)((unsigned __int8)(result)))) goto loc_00377328;
loc_003776D3:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned __int8)(result))) + 92)))) & (4)) == 0) goto loc_0037751D;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)((unsigned __int8)(result))) + 92))) >> (3));
    a2 = (unsigned int)((a2) & (63));
    if (((unsigned __int8)(a2)) != ((unsigned __int8)((unsigned __int8)(result)))) goto loc_0037751D;
    goto loc_00377396;
loc_003776F3:
    result = MiGetPageFromSlabAllocatorByIdentity(v_stack_p10, (unsigned __int8)((unsigned __int8)(result)), v_stack_p78, a4);
    if (result != -1) goto loc_003773AB;
    v_rdi = (result) | (result);
    goto loc_003773AB;
loc_00377728:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + 80)) != 0) goto loc_003776A0;
    result = (0) | (2);
    *(unsigned __int64 *)(v_stack_p10 + 48) = result;
    result = MiGetPageFromSlabEntry(0, v_stack_p10, v_stack_p78, a4);
    if (result == -1) goto loc_003776A0;
    goto loc_003773AE;
}
```

## 5. (Beta) C Style

```c
int64_t MiGetPageFromSlabAllocator(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint8_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p60;
    uint64_t v_stack_p78;
    uint8_t v_stack_p8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(arg1 + 0x80)) == 8) goto loc_0037765A;
loc_003772BE:
    v_stack_p18 = 255;
    if (*(uint64_t *)(arg1 + 0x60) == 0) goto loc_00377444;
    local_r12 = (local_r12) | (-1);
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) & (16));
    if (condition_is_equal) goto loc_003774BE;
    v_stack_p8 = 17;
    result = ExAcquireSpinLockSharedAtDpcLevel(Arg1 + 16, Arg2, Arg3, Arg4);
loc_003772F5:
    if ((*(uint32_t *)(arg1 + 0x80)) == 8) goto loc_003775D2;
loc_00377306:
    if (Arg1 + 32 == 0) goto loc_00377361;
    v_stack_p20 = *(uint64_t *)(arg1 + 0x20);
    if (*(uint64_t *)(arg1 + 0x20) == 0) goto loc_00377361;
    if (255 != 255) goto loc_003776A9;
    if ((*(uint64_t *)(arg1 + 0x20)) == 1) goto loc_00377343;
loc_00377328:
    result = MiGetPageFromSlabEntry(*(uint64_t *)(arg1 + 0x20), Arg1, Arg3, Arg4);
    if (result != -1) goto loc_00377475;
loc_00377343:
    if ((*(uint32_t *)(arg1 + 0x80)) == 8) goto loc_0037763F;
loc_00377354:
    if (Arg1 + 32 != 0) {
        result = v_stack_p20;
        *(uint64_t *)(arg1 + 0x20) = result;
    }
    if ((*(uint32_t *)(arg1 + 0x80)) == 8) goto loc_00377624;
loc_00377372:
    if (Arg1 + 40 == 0) goto loc_00377517;
    v_stack_p20 = *(uint64_t *)(arg1 + 0x28);
    if (*(uint64_t *)(arg1 + 0x28) == 0) goto loc_0037751D;
    if (255 != 255) goto loc_003776D3;
loc_00377396:
    result = MiGetPageFromSlabEntry(*(uint64_t *)(arg1 + 0x28), Arg1, Arg3, Arg4);
    if (result == -1) goto loc_0037751D;
loc_003773AB:
loc_003773AE:
    if ((*(uint32_t *)(arg1 + 0x80)) == 8) goto loc_003775ED;
loc_003773BF:
    if (Arg1 + 32 != 0) {
        result = v_stack_p20;
        *(uint64_t *)(arg1 + 0x20) = result;
    }
    result = MiReleaseSpinLockShared(Arg1 + 16, v_stack_p8, Arg3, Arg4);
    if (result == -1) goto loc_0037743F;
    if (sign_flag) goto loc_00377455;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x80)))) > 4) goto loc_00377455;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x80)))) == 2) goto loc_00377455;
    local_rsi = (result + result * 2) << (4);
    local_rsi = (local_rsi) + ((uint32_t)(*(uint32_t *)(arg1 + 0x80)));
    if ((((uint8_t)((uint32_t)(Arg2))) & (16)) != 0) goto loc_003775A8;
    result = MiLockPageInline(local_rsi, v_stack_p8, Arg3, Arg4);
loc_0037741D:
    Arg4 = 0;
    result = MiUpdateSlabPagePlaceholderState((uint32_t)(*(uint32_t *)(arg1 + 0x80)), result, Arg4 + 1, Arg4);
    result = MiUnlockPage(local_rsi, (uint8_t)((uint8_t)(result)), Arg4 + 1, Arg4);
    goto loc_00377455;
loc_0037743F:
loc_00377444:
    result = MiGetRepurposedSlabStandbyPage(Arg1, (uint8_t)((uint8_t)(result)), Arg4 + 1, Arg4);
    if (result == -1) goto loc_003774CC;
loc_00377455:
    if ((*(uint64_t *)(arg1 + 0x68)) != 0) goto loc_0037747D;
loc_0037745C:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00377475:
    goto loc_003773CC;
loc_0037747D:
    if (*(uint64_t *)(v_stack_p10 + 0xD0) != 0) goto loc_0037745C;
    Arg3 = (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x50))) + (*(uint64_t *)(v_stack_p10 + 0x60));
    result = (*(uint64_t *)(v_stack_p10 + 0x68)) >> (1);
    if (Arg3 > result) goto loc_0037745C;
    local_r13 = (uint32_t)(((uint32_t)(Arg2)) & (16));
    Arg2 = 0;
    local_r13 = (uint32_t)((local_r13) | (4));
    local_r13 = (uint32_t)((local_r13) >> (2));
    result = MiAsyncSlabReplenish(v_stack_p10, Arg2, (uint32_t)((uint32_t)(local_r13)), Arg4);
    goto loc_0037745C;
loc_003774BE:
    result = ExAcquireSpinLockShared(v_stack_p10, Arg2, (uint32_t)((uint32_t)(local_r13)), Arg4);
    v_stack_p60 = (uint8_t)(result);
    goto loc_003772F5;
loc_003774CC:
    if (*(uint64_t *)(v_stack_p10 + 0xB0) == 0) goto loc_00377455;
    result = MiRepurposeStandbySlabPage(v_stack_p10, (uint8_t)(v_stack_p18), (uint32_t)((uint32_t)(local_r13)), Arg4);
    if (result != -1) goto loc_00377455;
    if (((uint8_t)(v_stack_p18)) == 255) goto loc_00377455;
    result = MiRepurposeStandbySlabPage(v_stack_p10, 255, (uint32_t)((uint32_t)(local_r13)), Arg4);
    goto loc_00377455;
loc_00377517:
loc_0037751D:
    local_r15 = 0;
    if (255 != 255) goto loc_003776F3;
    if ((((uint8_t)(*(uint64_t *)(v_stack_p10 + 0x8))) & (1)) != 0) goto loc_00377608;
loc_0037753C:
    if (*(uint64_t *)(v_stack_p10 + 0x8) == 0) goto loc_00377697;
    v_stack_p78 = *(uint64_t *)(v_stack_p10 + 0x8);
    if ((*(uint64_t *)(v_stack_p10 + 0x8)) == (*(uint64_t *)(v_stack_p10 + 0x30))) goto loc_003775A3;
    result = MiGetPageFromSlabEntry(*(uint64_t *)(v_stack_p10 + 0x8), v_stack_p10, (uint32_t)((uint32_t)(local_r13)), Arg4);
    if (result != -1) goto loc_003773AE;
loc_00377568:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x8) + 0x8) == 0) goto loc_0037758F;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x8) + 0x8)) == 0) goto loc_0037753C;
loc_0037757F:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x8) + 0x8))) != 0) goto loc_0037757F;
    goto loc_0037753C;
loc_0037758F:
    local_rsi = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x8) + 0x8)) + 0x10)) & (-4);
    if (condition_is_equal) goto loc_0037753C;
    if ((*(uint64_t *)(local_rsi)) == (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x8) + 0x8))))) goto loc_0037753C;
    goto loc_0037758F;
loc_003775A3:
    goto loc_00377568;
loc_003775A8:
    local_rbp = 0;
loc_003775AA:
    if (condition_is_above_or_equal) goto loc_0037741D;
loc_003775B7:
    local_rbp = (uint32_t)((local_rbp) + 1);
    if (((*(uint32_t *)(v_rip + 0xC4DCED)) & ((uint32_t)(local_rbp))) == 0) goto loc_00377670;
loc_003775C5:
loc_003775C7:
    if (!sign_flag) goto loc_003775AA;
    goto loc_003775B7;
loc_003775D2:
    if (((uint8_t)(local_rbp)) == 255) goto loc_00377361;
    goto loc_00377306;
loc_003775ED:
    if (((uint8_t)(local_rbp)) == 255) goto loc_003773CC;
    goto loc_003773BF;
loc_00377608:
    if ((*(uint64_t *)(v_stack_p10 + 0x20)) == 1) goto loc_0037761D;
    local_rsi = (v_stack_p10) | (1);
    local_rsi = (local_rsi) ^ (*(uint64_t *)(v_stack_p10 + 0x20));
    goto loc_0037753C;
loc_0037761D:
    local_rsi = 0;
    goto loc_0037753C;
loc_00377624:
    if (((uint8_t)(local_rbp)) == 255) goto loc_00377517;
    goto loc_00377372;
loc_0037763F:
    if (((uint8_t)(local_rbp)) == 255) goto loc_00377361;
    goto loc_00377354;
loc_0037765A:
    result = MiGetCurrentSlabIdentity(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(v_stack_p10 + 0x20) + (uint8_t)(local_rbp) * 8, (uint32_t)((uint32_t)(local_r13)), Arg4);
    goto loc_003772BE;
loc_00377670:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC4F442)))) & (64)) == 0) goto loc_003775C5;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(v_stack_p10 + 0x20) + (uint8_t)(local_rbp) * 8, (uint32_t)((uint32_t)(local_r13)), Arg4);
    if ((uint8_t)(result) == 0) goto loc_003775C5;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((uint8_t)(result))), *(uint64_t *)(v_stack_p10 + 0x20) + (uint8_t)(local_rbp) * 8, (uint32_t)((uint32_t)(local_r13)), Arg4);
    goto loc_003775C7;
loc_00377697:
    if (0 != 0) goto loc_00377728;
loc_003776A0:
    local_rdi = (result) | (-1);
    goto loc_003773CC;
loc_003776A9:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint8_t)(result))) + 0x5C))) >> (3));
    Arg2 = (uint32_t)((Arg2) & (63));
    if (((uint8_t)(Arg2)) == ((uint8_t)((uint8_t)(result)))) goto loc_00377328;
loc_003776D3:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint8_t)(result))) + 0x5C)))) & (4)) == 0) goto loc_0037751D;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)((uint8_t)(result))) + 0x5C))) >> (3));
    Arg2 = (uint32_t)((Arg2) & (63));
    if (((uint8_t)(Arg2)) != ((uint8_t)((uint8_t)(result)))) goto loc_0037751D;
    goto loc_00377396;
loc_003776F3:
    result = MiGetPageFromSlabAllocatorByIdentity(v_stack_p10, (uint8_t)((uint8_t)(result)), v_stack_p78, Arg4);
    if (result != -1) goto loc_003773AB;
    local_rdi = (result) | (result);
    goto loc_003773AB;
loc_00377728:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + 0x50)) != 0) goto loc_003776A0;
    result = (0) | (2);
    *(uint64_t *)(v_stack_p10 + 0x30) = result;
    result = MiGetPageFromSlabEntry(0, v_stack_p10, v_stack_p78, Arg4);
    if (result == -1) goto loc_003776A0;
    goto loc_003773AE;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x80` | `32` | `R` |
| `Arg1` | `+ 0xA4` | `32` | `R/W` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xD0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00377294&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
