# PpmInstallCoordinatedIdleStates

- RVA: `0x007552A0`–`0x0075589E` (길이 `1,534` bytes)
- VA: `0x00000001407552A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A3178`
- 디코드: `380`개 명령, `1,534/1,534` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x007552C2` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x007552E7` → [PpmIdleUpdateCoordinatedDependencies](../77/PpmIdleUpdateCoordinatedDependencies_function_00770D54.md) (function, `0x00770D54`)
- `0x007553DA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007553EF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00755412` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00755464` → [PpmResetPlatformIdleAccounting](../../text/5D/PpmResetPlatformIdleAccounting_function_005D0820.md) (function, `0x005D0820`)
- `0x00755494` → [PpmIdleIsStateDisabled](../../text/4F/PpmIdleIsStateDisabled_function_004FD2E0.md) (function, `0x004FD2E0`)
- `0x0075554D` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00755563` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x0075560A` → [KeGetPrcb](../../text/2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x0075580E` → [KeGetPrcb](../../text/2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x0075583F` → [PpmCheckCoordinatedStateInitiator](../../text/5C/PpmCheckCoordinatedStateInitiator_function_005CF4AC.md) (function, `0x005CF4AC`)
- `0x00755868` → [PpmEnableCoordinatedIdleStates](PpmEnableCoordinatedIdleStates_function_00754CD0.md) (function, `0x00754CD0`)
- `0x00755885` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x007552BB` → RVA `0x00F0CA70` (`.data`; read)
- `0x007552C7` → RVA `0x00FC6AD0` (`ALMOSTRO`; read)
- `0x00755305` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x00755359` → RVA `0x00E67678` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **12**
  - `0x007552C2` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x007553DA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007553EF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00755412` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00755464` → [PpmResetPlatformIdleAccounting](../../text/5D/PpmResetPlatformIdleAccounting_function_005D0820.md) (`PAGE` → `.text`)
  - `0x00755494` → [PpmIdleIsStateDisabled](../../text/4F/PpmIdleIsStateDisabled_function_004FD2E0.md) (`PAGE` → `.text`)
  - `0x0075554D` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00755563` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (`PAGE` → `.text`)
  - `0x0075560A` → [KeGetPrcb](../../text/2D/KeGetPrcb_function_002D85D0.md) (`PAGE` → `.text`)
  - `0x0075580E` → [KeGetPrcb](../../text/2D/KeGetPrcb_function_002D85D0.md) (`PAGE` → `.text`)
  - `0x0075583F` → [PpmCheckCoordinatedStateInitiator](../../text/5C/PpmCheckCoordinatedStateInitiator_function_005CF4AC.md) (`PAGE` → `.text`)
  - `0x00755885` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007552A0  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
007552A5  53                              push rbx
007552A6  55                              push rbp
007552A7  56                              push rsi
007552A8  57                              push rdi
007552A9  41 54                           push r12
007552AB  41 55                           push r13
007552AD  41 56                           push r14
007552AF  41 57                           push r15
007552B1  48 83 EC 38                     sub rsp, 0x38
007552B5  4C 8B F1                        mov r14, rcx
007552B8  45 33 FF                        xor r15d, r15d
007552BB  48 8D 0D AE 77 7B 00            lea rcx, [rip + 0x7b77ae]
007552C2  E8 7D B8 CD FF                  call 0x140430b44
007552C7  4C 39 3D 02 18 87 00            cmp qword ptr [rip + 0x871802], r15
007552CE  41 8D 77 01                     lea esi, [r15 + 1]
007552D2  74 10                           je 0x1407552e4
007552D4  45 38 7E 28                     cmp byte ptr [r14 + 0x28], r15b
007552D8  75 0A                           jne 0x1407552e4
007552DA  BB 89 01 00 C0                  mov ebx, 0xc0000189
007552DF  E9 9A 05 00 00                  jmp 0x14075587e
007552E4  49 8B CE                        mov rcx, r14
007552E7  E8 68 BA 01 00                  call 0x140770d54
007552EC  8B D8                           mov ebx, eax
007552EE  85 C0                           test eax, eax
007552F0  0F 88 88 05 00 00               js 0x14075587e
007552F6  41 8B 2E                        mov ebp, dword ptr [r14]
007552F9  89 6C 24 20                     mov dword ptr [rsp + 0x20], ebp
007552FD  85 ED                           test ebp, ebp
007552FF  0F 84 74 05 00 00               je 0x140755879
00755305  44 8B 2D 74 17 87 00            mov r13d, dword ptr [rip + 0x871774]
0075530C  8B D5                           mov edx, ebp
0075530E  41 0F AF D5                     imul edx, r13d
00755312  45 33 C9                        xor r9d, r9d
00755315  44 89 AC 24 88 00 00 00         mov dword ptr [rsp + 0x88], r13d
0075531D  44 8B C5                        mov r8d, ebp
00755320  44 8B D2                        mov r10d, edx
00755323  85 ED                           test ebp, ebp
00755325  74 22                           je 0x140755349
00755327  49 8D 8E 58 01 00 00            lea rcx, [r14 + 0x158]
0075532E  44 8B DD                        mov r11d, ebp
00755331  8B 41 04                        mov eax, dword ptr [rcx + 4]
00755334  44 03 C8                        add r9d, eax
00755337  0F AF 01                        imul eax, dword ptr [rcx]
0075533A  48 8D 89 40 01 00 00            lea rcx, [rcx + 0x140]
00755341  44 03 D0                        add r10d, eax
00755344  4C 2B DE                        sub r11, rsi
00755347  75 E8                           jne 0x140755331
00755349  48 8B 3D 80 17 87 00            mov rdi, qword ptr [rip + 0x871780]
00755350  48 85 FF                        test rdi, rdi
00755353  0F 85 55 03 00 00               jne 0x1407556ae
00755359  48 8B 1D 18 23 71 00            mov rbx, qword ptr [rip + 0x712318]
00755360  43 8D 04 49                     lea eax, [r9 + r9*2]
00755364  41 BB F8 FF FF FF               mov r11d, 0xfffffff8
0075536A  69 CD C0 01 00 00               imul ecx, ebp, 0x1c0
00755370  44 8D 24 95 07 00 00 00         lea r12d, [rdx*4 + 7]
00755378  83 C1 47                        add ecx, 0x47
0075537B  41 23 CB                        and ecx, r11d
0075537E  89 8C 24 90 00 00 00            mov dword ptr [rsp + 0x90], ecx
00755385  8D 0C C1                        lea ecx, [rcx + rax*8]
00755388  89 8C 24 98 00 00 00            mov dword ptr [rsp + 0x98], ecx
0075538F  43 8D 04 52                     lea eax, [r10 + r10*2]
00755393  8D 04 C1                        lea eax, [rcx + rax*8]
00755396  44 03 E0                        add r12d, eax
00755399  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
0075539D  45 23 E3                        and r12d, r11d
007553A0  8D 0C AD 0F 00 00 00            lea ecx, [rbp*4 + 0xf]
007553A7  41 23 CB                        and ecx, r11d
007553AA  8B C5                           mov eax, ebp
007553AC  C1 E0 0A                        shl eax, 0xa
007553AF  8B F9                           mov edi, ecx
007553B1  83 C0 2F                        add eax, 0x2f
007553B4  41 0F AF FD                     imul edi, r13d
007553B8  41 03 C4                        add eax, r12d
007553BB  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
007553BF  41 23 C3                        and eax, r11d
007553C2  89 44 24 2C                     mov dword ptr [rsp + 0x2c], eax
007553C6  03 F8                           add edi, eax
007553C8  48 85 DB                        test rbx, rbx
007553CB  75 29                           jne 0x1407553f6
007553CD  8B D7                           mov edx, edi
007553CF  B9 48 00 00 00                  mov ecx, 0x48
007553D4  41 B8 50 50 4D 69               mov r8d, 0x694d5050
007553DA  E8 11 CD 42 00                  call 0x140b820f0
007553DF  48 8B F8                        mov rdi, rax
007553E2  48 85 C0                        test rax, rax
007553E5  75 42                           jne 0x140755429
007553E7  BA 50 50 4D 69                  mov edx, 0x694d5050
007553EC  49 8B CF                        mov rcx, r15
007553EF  E8 7C D4 42 00                  call 0x140b82870
007553F4  EB 29                           jmp 0x14075541f
007553F6  8B 5B 04                        mov ebx, dword ptr [rbx + 4]
007553F9  85 DB                           test ebx, ebx
007553FB  74 D0                           je 0x1407553cd
007553FD  8B D3                           mov edx, ebx
007553FF  B9 40 00 00 00                  mov ecx, 0x40
00755404  49 0F AF D0                     imul rdx, r8
00755408  41 B8 50 50 4D 69               mov r8d, 0x694d5050
0075540E  48 C1 E2 06                     shl rdx, 6
00755412  E8 D9 CC 42 00                  call 0x140b820f0
00755417  4C 8B F8                        mov r15, rax
0075541A  48 85 C0                        test rax, rax
0075541D  75 AE                           jne 0x1407553cd
0075541F  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00755424  E9 55 04 00 00                  jmp 0x14075587e
00755429  44 89 68 04                     mov dword ptr [rax + 4], r13d
0075542D  89 28                           mov dword ptr [rax], ebp
0075542F  40 88 70 08                     mov byte ptr [rax + 8], sil
00755433  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00755437  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
0075543B  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0075543F  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
00755443  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00755447  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
0075544B  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
0075544F  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
00755453  45 8B EC                        mov r13d, r12d
00755456  4C 03 EF                        add r13, rdi
00755459  4C 89 6F 30                     mov qword ptr [rdi + 0x30], r13
0075545D  49 8B CD                        mov rcx, r13
00755460  41 89 6D 04                     mov dword ptr [r13 + 4], ebp
00755464  E8 B7 B3 E7 FF                  call 0x1405d0820
00755469  45 33 D2                        xor r10d, r10d
0075546C  45 39 16                        cmp dword ptr [r14], r10d
0075546F  76 76                           jbe 0x1407554e7
00755471  45 8B DA                        mov r11d, r10d
00755474  48 8D 47 58                     lea rax, [rdi + 0x58]
00755478  4D 69 CB C0 01 00 00            imul r9, r11, 0x1c0
0075547F  41 8B D2                        mov edx, r10d
00755482  33 C9                           xor ecx, ecx
00755484  49 03 C1                        add rax, r9
00755487  48 89 40 08                     mov qword ptr [rax + 8], rax
0075548B  48 89 00                        mov qword ptr [rax], rax
0075548E  41 C6 44 39 68 07               mov byte ptr [r9 + rdi + 0x68], 7
00755494  E8 47 7E DA FF                  call 0x1404fd2e0
00755499  84 C0                           test al, al
0075549B  74 09                           je 0x1407554a6
0075549D  41 C7 44 39 50 00 00 00 80      mov dword ptr [r9 + rdi + 0x50], 0x80000000
007554A6  85 DB                           test ebx, ebx
007554A8  74 35                           je 0x1407554df
007554AA  41 8B 06                        mov eax, dword ptr [r14]
007554AD  2B C6                           sub eax, esi
007554AF  44 3B D0                        cmp r10d, eax
007554B2  75 05                           jne 0x1407554b9
007554B4  41 88 74 39 69                  mov byte ptr [r9 + rdi + 0x69], sil
007554B9  4D 89 7C 39 70                  mov qword ptr [r9 + rdi + 0x70], r15
007554BE  8B C3                           mov eax, ebx
007554C0  48 C1 E0 06                     shl rax, 6
007554C4  4C 03 F8                        add r15, rax
007554C7  41 89 5C 39 6C                  mov dword ptr [r9 + rdi + 0x6c], ebx
007554CC  48 8D 47 50                     lea rax, [rdi + 0x50]
007554D0  49 03 C1                        add rax, r9
007554D3  49 C1 E3 0A                     shl r11, 0xa
007554D7  4B 89 84 2B E0 00 00 00         mov qword ptr [r11 + r13 + 0xe0], rax
007554DF  44 03 D6                        add r10d, esi
007554E2  45 3B 16                        cmp r10d, dword ptr [r14]
007554E5  72 8A                           jb 0x140755471
007554E7  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
007554EE  44 8B BC 24 98 00 00 00         mov r15d, dword ptr [rsp + 0x98]
007554F6  48 03 C7                        add rax, rdi
007554F9  4C 03 FF                        add r15, rdi
007554FC  85 ED                           test ebp, ebp
007554FE  0F 84 D0 00 00 00               je 0x1407555d4
00755504  4D 8D A6 48 01 00 00            lea r12, [r14 + 0x148]
0075550B  4C 8B F0                        mov r14, rax
0075550E  4C 8D AF 82 00 00 00            lea r13, [rdi + 0x82]
00755515  41 0F 10 44 24 F0               movups xmm0, xmmword ptr [r12 - 0x10]
0075551B  49 8D 4D 06                     lea rcx, [r13 + 6]
0075551F  33 D2                           xor edx, edx
00755521  41 B8 00 01 00 00               mov r8d, 0x100
00755527  F3 41 0F 7F 85 06 01 00 00      movdqu xmmword ptr [r13 + 0x106], xmm0
00755530  49 8B 04 24                     mov rax, qword ptr [r12]
00755534  49 89 45 BE                     mov qword ptr [r13 - 0x42], rax
00755538  41 8A 44 24 1C                  mov al, byte ptr [r12 + 0x1c]
0075553D  41 88 45 F8                     mov byte ptr [r13 - 8], al
00755541  83 61 FC 00                     and dword ptr [rcx - 4], 0
00755545  41 C7 45 FE 01 00 20 00         mov dword ptr [r13 - 2], 0x200001
0075554D  E8 EE 16 F7 FF                  call 0x1406c6c40
00755552  41 0F B7 55 00                  movzx edx, word ptr [r13]
00755557  4D 8D 84 24 E8 FE FF FF         lea r8, [r12 - 0x118]
0075555F  49 8D 4D FE                     lea rcx, [r13 - 2]
00755563  E8 F8 92 B7 FF                  call 0x1402ce860
00755568  41 8B 44 24 14                  mov eax, dword ptr [r12 + 0x14]
0075556D  33 D2                           xor edx, edx
0075556F  41 89 45 FA                     mov dword ptr [r13 - 6], eax
00755573  4D 89 B5 16 01 00 00            mov qword ptr [r13 + 0x116], r14
0075557A  41 8B 4C 24 14                  mov ecx, dword ptr [r12 + 0x14]
0075557F  48 8D 04 49                     lea rax, [rcx + rcx*2]
00755583  4D 8D 34 C6                     lea r14, [r14 + rax*8]
00755587  85 C9                           test ecx, ecx
00755589  74 26                           je 0x1407555b1
0075558B  49 8B 85 16 01 00 00            mov rax, qword ptr [r13 + 0x116]
00755592  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
00755596  03 D6                           add edx, esi
00755598  4C 89 7C C8 10                  mov qword ptr [rax + rcx*8 + 0x10], r15
0075559D  41 8B 44 24 10                  mov eax, dword ptr [r12 + 0x10]
007555A2  48 8D 0C 40                     lea rcx, [rax + rax*2]
007555A6  4D 8D 3C CF                     lea r15, [r15 + rcx*8]
007555AA  41 3B 54 24 14                  cmp edx, dword ptr [r12 + 0x14]
007555AF  72 DA                           jb 0x14075558b
007555B1  49 81 C4 40 01 00 00            add r12, 0x140
007555B8  49 81 C5 C0 01 00 00            add r13, 0x1c0
007555BF  48 2B EE                        sub rbp, rsi
007555C2  0F 85 4D FF FF FF               jne 0x140755515
007555C8  8B 6C 24 20                     mov ebp, dword ptr [rsp + 0x20]
007555CC  4C 8B B4 24 80 00 00 00         mov r14, qword ptr [rsp + 0x80]
007555D4  44 8B 64 24 24                  mov r12d, dword ptr [rsp + 0x24]
007555D9  33 DB                           xor ebx, ebx
007555DB  44 8B AC 24 88 00 00 00         mov r13d, dword ptr [rsp + 0x88]
007555E3  4C 03 E7                        add r12, rdi
007555E6  45 85 ED                        test r13d, r13d
007555E9  0F 84 D1 00 00 00               je 0x1407556c0
007555EF  8B C5                           mov eax, ebp
007555F1  48 8D 0C 40                     lea rcx, [rax + rax*2]
007555F5  48 C1 E1 03                     shl rcx, 3
007555F9  48 C1 E0 02                     shl rax, 2
007555FD  4C 8B F1                        mov r14, rcx
00755600  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
00755608  8B CB                           mov ecx, ebx
0075560A  E8 C1 2F B8 FF                  call 0x1402d85d0
0075560F  45 33 C9                        xor r9d, r9d
00755612  4C 8B 80 40 88 00 00            mov r8, qword ptr [rax + 0x8840]
00755619  8B 44 24 28                     mov eax, dword ptr [rsp + 0x28]
0075561D  0F AF C3                        imul eax, ebx
00755620  4D 89 B8 00 04 00 00            mov qword ptr [r8 + 0x400], r15
00755627  4D 03 FE                        add r15, r14
0075562A  4D 89 A0 18 04 00 00            mov qword ptr [r8 + 0x418], r12
00755631  4C 03 A4 24 98 00 00 00         add r12, qword ptr [rsp + 0x98]
00755639  03 44 24 2C                     add eax, dword ptr [rsp + 0x2c]
0075563D  48 03 C7                        add rax, rdi
00755640  41 89 A8 F8 03 00 00            mov dword ptr [r8 + 0x3f8], ebp
00755647  49 89 80 E0 03 00 00            mov qword ptr [r8 + 0x3e0], rax
0075564E  41 89 A8 08 04 00 00            mov dword ptr [r8 + 0x408], ebp
00755655  85 ED                           test ebp, ebp
00755657  74 40                           je 0x140755699
00755659  4C 8D 97 98 01 00 00            lea r10, [rdi + 0x198]
00755660  49 8B 88 00 04 00 00            mov rcx, qword ptr [r8 + 0x400]
00755667  8B C5                           mov eax, ebp
00755669  41 2B C1                        sub eax, r9d
0075566C  2B C6                           sub eax, esi
0075566E  48 8D 14 40                     lea rdx, [rax + rax*2]
00755672  44 89 4C D1 04                  mov dword ptr [rcx + rdx*8 + 4], r9d
00755677  44 03 CE                        add r9d, esi
0075567A  41 8B 82 E4 FE FF FF            mov eax, dword ptr [r10 - 0x11c]
00755681  89 44 D1 08                     mov dword ptr [rcx + rdx*8 + 8], eax
00755685  49 8B 02                        mov rax, qword ptr [r10]
00755688  4D 8D 92 C0 01 00 00            lea r10, [r10 + 0x1c0]
0075568F  48 89 44 D1 10                  mov qword ptr [rcx + rdx*8 + 0x10], rax
00755694  44 3B CD                        cmp r9d, ebp
00755697  72 C7                           jb 0x140755660
00755699  03 DE                           add ebx, esi
0075569B  41 3B DD                        cmp ebx, r13d
0075569E  0F 82 64 FF FF FF               jb 0x140755608
007556A4  4C 8B B4 24 80 00 00 00         mov r14, qword ptr [rsp + 0x80]
007556AC  EB 12                           jmp 0x1407556c0
007556AE  44 39 6F 04                     cmp dword ptr [rdi + 4], r13d
007556B2  0F 85 C1 01 00 00               jne 0x140755879
007556B8  39 2F                           cmp dword ptr [rdi], ebp
007556BA  0F 85 B9 01 00 00               jne 0x140755879
007556C0  85 ED                           test ebp, ebp
007556C2  0F 84 3D 01 00 00               je 0x140755805
007556C8  8B CD                           mov ecx, ebp
007556CA  4C 8D 47 48                     lea r8, [rdi + 0x48]
007556CE  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
007556D6  49 81 C6 54 01 00 00            add r14, 0x154
007556DD  41 8B 46 FC                     mov eax, dword ptr [r14 - 4]
007556E1  45 33 D2                        xor r10d, r10d
007556E4  41 89 00                        mov dword ptr [r8], eax
007556E7  41 8B 06                        mov eax, dword ptr [r14]
007556EA  41 89 40 04                     mov dword ptr [r8 + 4], eax
007556EE  41 8A 46 0C                     mov al, byte ptr [r14 + 0xc]
007556F2  41 88 40 31                     mov byte ptr [r8 + 0x31], al
007556F6  45 39 56 08                     cmp dword ptr [r14 + 8], r10d
007556FA  0F 86 DE 00 00 00               jbe 0x1407557de
00755700  4D 8B A8 50 01 00 00            mov r13, qword ptr [r8 + 0x150]
00755707  4F 8D 24 52                     lea r12, [r10 + r10*2]
0075570B  45 8B CA                        mov r9d, r10d
0075570E  49 C1 E1 04                     shl r9, 4
00755712  4D 03 4E 14                     add r9, qword ptr [r14 + 0x14]
00755716  41 8B 01                        mov eax, dword ptr [r9]
00755719  43 89 44 E5 00                  mov dword ptr [r13 + r12*8], eax
0075571E  83 F8 FF                        cmp eax, -1
00755721  75 04                           jne 0x140755727
00755723  41 88 70 33                     mov byte ptr [r8 + 0x33], sil
00755727  41 8B 41 04                     mov eax, dword ptr [r9 + 4]
0075572B  45 33 FF                        xor r15d, r15d
0075572E  43 89 44 E5 08                  mov dword ptr [r13 + r12*8 + 8], eax
00755733  41 8B 41 04                     mov eax, dword ptr [r9 + 4]
00755737  85 C0                           test eax, eax
00755739  0F 84 8A 00 00 00               je 0x1407557c9
0075573F  49 8B 49 08                     mov rcx, qword ptr [r9 + 8]
00755743  41 2B C7                        sub eax, r15d
00755746  4B 8B 5C E5 10                  mov rbx, qword ptr [r13 + r12*8 + 0x10]
0075574B  2B C6                           sub eax, esi
0075574D  4C 8D 1C 40                     lea r11, [rax + rax*2]
00755751  42 0F B6 04 B9                  movzx eax, byte ptr [rcx + r15*4]
00755756  42 89 44 DB 04                  mov dword ptr [rbx + r11*8 + 4], eax
0075575B  42 80 7C B9 01 00               cmp byte ptr [rcx + r15*4 + 1], 0
00755761  89 84 24 90 00 00 00            mov dword ptr [rsp + 0x90], eax
00755768  0F 94 C0                        sete al
0075576B  42 88 04 DB                     mov byte ptr [rbx + r11*8], al
0075576F  42 8A 44 B9 02                  mov al, byte ptr [rcx + r15*4 + 2]
00755774  42 88 44 DB 01                  mov byte ptr [rbx + r11*8 + 1], al
00755779  42 8A 44 B9 03                  mov al, byte ptr [rcx + r15*4 + 3]
0075577E  42 88 44 DB 02                  mov byte ptr [rbx + r11*8 + 2], al
00755783  43 83 7C E5 00 FF               cmp dword ptr [r13 + r12*8], -1
00755789  75 21                           jne 0x1407557ac
0075578B  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
00755792  48 69 C8 C0 01 00 00            imul rcx, rax, 0x1c0
00755799  8B 44 39 7C                     mov eax, dword ptr [rcx + rdi + 0x7c]
0075579D  42 89 44 DB 08                  mov dword ptr [rbx + r11*8 + 8], eax
007557A2  48 8B 84 39 98 01 00 00         mov rax, qword ptr [rcx + rdi + 0x198]
007557AA  EB 08                           jmp 0x1407557b4
007557AC  42 83 64 DB 08 00               and dword ptr [rbx + r11*8 + 8], 0
007557B2  33 C0                           xor eax, eax
007557B4  4A 89 44 DB 10                  mov qword ptr [rbx + r11*8 + 0x10], rax
007557B9  44 03 FE                        add r15d, esi
007557BC  41 8B 41 04                     mov eax, dword ptr [r9 + 4]
007557C0  44 3B F8                        cmp r15d, eax
007557C3  0F 82 76 FF FF FF               jb 0x14075573f
007557C9  44 03 D6                        add r10d, esi
007557CC  45 3B 56 08                     cmp r10d, dword ptr [r14 + 8]
007557D0  0F 82 2A FF FF FF               jb 0x140755700
007557D6  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
007557DE  49 81 C0 C0 01 00 00            add r8, 0x1c0
007557E5  49 81 C6 40 01 00 00            add r14, 0x140
007557EC  48 2B CE                        sub rcx, rsi
007557EF  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
007557F7  0F 85 E0 FE FF FF               jne 0x1407556dd
007557FD  44 8B AC 24 88 00 00 00         mov r13d, dword ptr [rsp + 0x88]
00755805  33 DB                           xor ebx, ebx
00755807  45 85 ED                        test r13d, r13d
0075580A  74 4C                           je 0x140755858
0075580C  8B CB                           mov ecx, ebx
0075580E  E8 BD 2D B8 FF                  call 0x1402d85d0
00755813  45 33 F6                        xor r14d, r14d
00755816  4C 8B B8 40 88 00 00            mov r15, qword ptr [rax + 0x8840]
0075581D  85 ED                           test ebp, ebp
0075581F  74 30                           je 0x140755851
00755821  4D 8B 97 00 04 00 00            mov r10, qword ptr [r15 + 0x400]
00755828  8B C5                           mov eax, ebp
0075582A  41 2B C6                        sub eax, r14d
0075582D  8B CB                           mov ecx, ebx
0075582F  2B C6                           sub eax, esi
00755831  4C 8D 1C 40                     lea r11, [rax + rax*2]
00755835  4F 8B 44 DA 10                  mov r8, qword ptr [r10 + r11*8 + 0x10]
0075583A  43 8B 54 DA 08                  mov edx, dword ptr [r10 + r11*8 + 8]
0075583F  E8 68 9C E7 FF                  call 0x1405cf4ac
00755844  44 03 F6                        add r14d, esi
00755847  43 88 44 DA 01                  mov byte ptr [r10 + r11*8 + 1], al
0075584C  44 3B F5                        cmp r14d, ebp
0075584F  72 D0                           jb 0x140755821
00755851  03 DE                           add ebx, esi
00755853  41 3B DD                        cmp ebx, r13d
00755856  72 B4                           jb 0x14075580c
00755858  48 83 3D 70 12 87 00 00         cmp qword ptr [rip + 0x871270], 0
00755860  75 0E                           jne 0x140755870
00755862  40 8A D6                        mov dl, sil
00755865  48 8B CF                        mov rcx, rdi
00755868  E8 63 F4 FF FF                  call 0x140754cd0
0075586D  40 32 F6                        xor sil, sil
00755870  33 DB                           xor ebx, ebx
00755872  40 84 F6                        test sil, sil
00755875  74 13                           je 0x14075588a
00755877  EB 05                           jmp 0x14075587e
00755879  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0075587E  48 8D 0D EB 71 7B 00            lea rcx, [rip + 0x7b71eb]
00755885  E8 32 A3 B8 FF                  call 0x1402dfbbc
0075588A  8B C3                           mov eax, ebx
0075588C  48 83 C4 38                     add rsp, 0x38
00755890  41 5F                           pop r15
00755892  41 5E                           pop r14
00755894  41 5D                           pop r13
00755896  41 5C                           pop r12
00755898  5F                              pop rdi
00755899  5E                              pop rsi
0075589A  5D                              pop rbp
0075589B  5B                              pop rbx
0075589C  C3                              ret
0075589D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmInstallCoordinatedIdleStates(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (56);
    v_r15 = 0;
    result = PopAcquireRwLockExclusive(v_rip + 8091566, a2, a3, a4);
    if ((*(unsigned __int64 *)(v_rip + 8853506)) == 0) goto loc_007552E4;
    if ((*(unsigned __int8 *)(a1 + 40)) != 0) goto loc_007552E4;
    goto loc_0075587E;
loc_007552E4:
    result = PpmIdleUpdateCoordinatedDependencies(a1, a2, a3, a4);
    if (sign_flag) goto loc_0075587E;
    v_stack_m58 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1))) == 0) goto loc_00755879;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) * ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8853364)))));
    a4 = 0;
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8853364)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1))) == 0) goto loc_00755349;
loc_00755331:
    a4 = (unsigned int)((a4) + ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 344 + 4)))));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 344 + 4))) * (*(unsigned int *)(a1 + 344)));
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(a2))) + ((unsigned int)(result)));
    v_r11 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) - (v_r15 + 1);
    if (condition_is_not_equal) goto loc_00755331;
loc_00755349:
    if (*(unsigned __int64 *)(v_rip + 8853376) != 0) goto loc_007556AE;
    a1 = (unsigned int)((a1 + 344 + 320) * ((unsigned int)((unsigned int)(*(unsigned int *)(a1)))));
    a1 = (unsigned int)((a1) + (71));
    a1 = (unsigned int)((a1) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    v_stack_p18 = (unsigned int)(a1);
    v_stack_p20 = (unsigned int)(a1 + a4 + a4 * 2 * 8);
    v_r12 = (unsigned int)((a2 * 4 + 7) + ((unsigned int)(a1 + a4 + a4 * 2 * 8 + v_r10 + v_r10 * 2 * 8)));
    v_stack_m54 = (unsigned int)(a1 + a4 + a4 * 2 * 8 + v_r10 + v_r10 * 2 * 8);
    v_r12 = (unsigned int)((v_r12) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1)) * 4 + 15) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) << (10));
    result = (unsigned int)((result) + (47));
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(a1))) * ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8853364)))));
    result = (unsigned int)((result) + ((unsigned int)(v_r12)));
    v_stack_m50 = (unsigned int)(a1);
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    v_stack_m4C = (unsigned int)(result);
    v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(result)));
    if (*(unsigned __int64 *)(v_rip + 7414552) != 0) goto loc_007553F6;
loc_007553CD:
    result = ExAllocatePool2(72, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x694D5050ULL), a4);
    if (result != 0) goto loc_00755429;
    result = ExFreePoolWithTag(0, (unsigned int)(0x694D5050ULL), (unsigned int)(0x694D5050ULL), a4);
    goto loc_0075541F;
loc_007553F6:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7414552) + 4))) == 0) goto loc_007553CD;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7414552) + 4))))) * ((unsigned int)(0x694D5050ULL));
    a2 = (a2) << (6);
    result = ExAllocatePool2(64, a2, (unsigned int)(0x694D5050ULL), a4);
    if (result != 0) goto loc_007553CD;
loc_0075541F:
    goto loc_0075587E;
loc_00755429:
    *(unsigned int *)(result + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8853364)));
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    *(unsigned __int8 *)(result + 8) = (unsigned __int8)(v_r15 + 1);
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(a1 + 8);
    *(unsigned __int64 *)(result + 24) = *(unsigned __int64 *)(a1 + 16);
    *(unsigned __int64 *)(result + 32) = *(unsigned __int64 *)(a1 + 24);
    *(unsigned __int64 *)(result + 40) = *(unsigned __int64 *)(a1 + 32);
    v_r13 = ((unsigned int)((unsigned int)(v_r12))) + (result);
    *(unsigned __int64 *)(result + 48) = v_r13;
    *(unsigned int *)(v_r13 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    result = PpmResetPlatformIdleAccounting(v_r13, a2, (unsigned int)(0x694D5050ULL), a4);
    v_r10 = 0;
    if ((*(unsigned int *)(a1)) <= 0) goto loc_007554E7;
loc_00755471:
    a4 = (a4) * (0);
    a1 = 0;
    result = (result + 88) + (a4);
    *(unsigned __int64 *)(result + 8) = result;
    *(unsigned __int64 *)(result) = result;
    *(unsigned __int8 *)(a4 + result * 1 + 104) = 7;
    result = PpmIdleIsStateDisabled(a1, 0, (unsigned int)(0x694D5050ULL), a4);
    if ((unsigned __int8)(result) != 0) {
        *(unsigned int *)(a4 + result * 1 + 80) = 0x80000000ULL;
    }
    if ((unsigned int)((unsigned int)(0xC000009AULL)) == 0) goto loc_007554DF;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) - ((unsigned int)(v_r15 + 1)));
    if (0 == ((unsigned int)(result))) {
        *(unsigned __int8 *)(a4 + result * 1 + 105) = (unsigned __int8)(v_r15 + 1);
    }
    *(unsigned __int64 *)(a4 + result * 1 + 112) = result;
    result = ((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)))) << (6);
    v_r15 = (result) + (result);
    *(unsigned int *)(a4 + result * 1 + 108) = (unsigned int)((unsigned int)(0xC000009AULL));
    result = (result + 80) + (a4);
    v_r11 = (0) << (10);
    *(unsigned __int64 *)(v_r11 + v_r13 * 1 + 224) = result;
loc_007554DF:
    v_r10 = (unsigned int)((v_r10) + ((unsigned int)(v_r15 + 1)));
    if (((unsigned int)(v_r10)) < (*(unsigned int *)(a1))) goto loc_00755471;
loc_007554E7:
    result = ((unsigned int)(v_stack_p18)) + (result);
    v_r15 = ((unsigned int)(v_stack_p20)) + (result);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1))) == 0) goto loc_007555D4;
loc_00755515:
    a2 = 0;
    *(unsigned __int64 *)(result + 130 + 262) = v_xmm0;
    *(unsigned __int64 *)(result + 130 - 66) = *(unsigned __int64 *)(a1 + 328);
    *(unsigned __int8 *)(result + 130 - 8) = (unsigned __int8)(*(unsigned __int8 *)(a1 + 328 + 28));
    *(unsigned int *)(result + 130 - 2) = 0x200001ULL;
    result = memset(result + 130 + 6, a2, 256, a4);
    result = KiCopyAffinityEx(result + 130 - 2, *(unsigned __int16 *)(result + 130), a1 + 328 - 280, a4);
    a2 = 0;
    *(unsigned int *)(result + 130 - 6) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 328 + 20)));
    *(unsigned __int64 *)(result + 130 + 278) = result;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 328 + 20))) == 0) goto loc_007555B1;
loc_0075558B:
    a2 = (unsigned int)((a2) + ((unsigned int)(v_r15 + 1)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 130 + 278) + a2 + a2 * 2 * 8 + 16) = v_r15;
    if (((unsigned int)(a2)) < (*(unsigned int *)(a1 + 328 + 20))) goto loc_0075558B;
loc_007555B1:
    v_r12 = (a1 + 328) + (320);
    v_r13 = (result + 130) + (448);
    v_rbp = ((unsigned int)(*(unsigned int *)(a1))) - (v_r15 + 1);
    if (condition_is_not_equal) goto loc_00755515;
loc_007555D4:
    v_rbx = 0;
    v_r12 = ((unsigned int)(v_stack_m54)) + (result);
    if ((unsigned int)((unsigned int)(v_stack_p10)) == 0) goto loc_007556C0;
    a1 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m58))) + (unsigned int)((unsigned int)((unsigned int)(v_stack_m58))) * 2) << (3);
    result = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m58)))) << (2);
    v_stack_p20 = result;
loc_00755608:
    result = KeGetPrcb(0, a2, a1 + 328 - 280, a4);
    a4 = 0;
    result = (unsigned int)(((unsigned int)(v_stack_m50)) * (0));
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 34880) + 1024) = v_r15 + (unsigned int)(*(unsigned int *)(a1 + 328 + 16)) + (unsigned int)(*(unsigned int *)(a1 + 328 + 16)) * 2 * 8;
    v_r15 = (v_r15 + (unsigned int)(*(unsigned int *)(a1 + 328 + 16)) + (unsigned int)(*(unsigned int *)(a1 + 328 + 16)) * 2 * 8) + (a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 34880) + 1048) = v_r12;
    v_r12 = (v_r12) + (v_stack_p20);
    result = (unsigned int)((result) + (v_stack_m4C));
    result = (result) + (result);
    *(unsigned int *)(*(unsigned __int64 *)(result + 34880) + 1016) = (unsigned int)((unsigned int)(v_stack_m58));
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 34880) + 992) = result;
    *(unsigned int *)(*(unsigned __int64 *)(result + 34880) + 1032) = (unsigned int)((unsigned int)(v_stack_m58));
    if ((unsigned int)((unsigned int)(v_stack_m58)) == 0) goto loc_00755699;
loc_00755660:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m58)))) - (0));
    result = (unsigned int)((result) - ((unsigned int)(v_r15 + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 34880) + 1024) + result + result * 2 * 8 + 4) = 0;
    a4 = (unsigned int)((a4) + ((unsigned int)(v_r15 + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 34880) + 1024) + result + result * 2 * 8 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 408 - 284)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 34880) + 1024) + result + result * 2 * 8 + 16) = *(unsigned __int64 *)(result + 408);
    if (a4 < ((unsigned int)((unsigned int)(v_stack_m58)))) goto loc_00755660;
loc_00755699:
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(v_r15 + 1)));
    if (((unsigned int)(v_rbx)) < ((unsigned int)((unsigned int)(v_stack_p10)))) goto loc_00755608;
    goto loc_007556C0;
loc_007556AE:
    if ((*(unsigned int *)(result + 4)) != ((unsigned int)((unsigned int)(v_stack_p10)))) goto loc_00755879;
    if ((*(unsigned int *)(result)) != ((unsigned int)((unsigned int)(v_stack_m58)))) goto loc_00755879;
loc_007556C0:
    if ((unsigned int)((unsigned int)(v_stack_m58)) == 0) goto loc_00755805;
    v_stack_p20 = (unsigned int)((unsigned int)((unsigned int)(v_stack_m58)));
    v_r14 = (v_stack_p8) + (340);
loc_007556DD:
    v_r10 = 0;
    *(unsigned int *)(result + 72) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 - 4)));
    *(unsigned int *)(result + 72 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14)));
    *(unsigned __int8 *)(result + 72 + 49) = (unsigned __int8)(*(unsigned __int8 *)(v_r14 + 12));
    if ((*(unsigned int *)(v_r14 + 8)) <= 0) goto loc_007557DE;
loc_00755700:
    a4 = (0) << (4);
    a4 = (a4) + (*(unsigned __int64 *)(v_r14 + 20));
    *(unsigned int *)(*(unsigned __int64 *)(result + 72 + 336) + v_r10 + v_r10 * 2 * 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a4)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4)))) == -1) {
        *(unsigned __int8 *)(result + 72 + 51) = (unsigned __int8)(v_r15 + 1);
    }
    v_r15 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(result + 72 + 336) + v_r10 + v_r10 * 2 * 8 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))) == 0) goto loc_007557C9;
loc_0075573F:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 4))) - (0));
    result = (unsigned int)((result) - ((unsigned int)(v_r15 + 1)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72 + 336) + v_r10 + v_r10 * 2 * 8 + 16) + result + result * 2 * 8 + 4) = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a4 + 8) + v_r15 * 4));
    v_stack_p18 = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a4 + 8) + v_r15 * 4));
    result = ((*(unsigned __int8 *)(*(unsigned __int64 *)(a4 + 8) + v_r15 * 4 + 1)) == 0) ? 1 : 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72 + 336) + v_r10 + v_r10 * 2 * 8 + 16) + result + result * 2 * 8) = (unsigned __int8)(result);
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72 + 336) + v_r10 + v_r10 * 2 * 8 + 16) + result + result * 2 * 8 + 1) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a4 + 8) + v_r15 * 4 + 2));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72 + 336) + v_r10 + v_r10 * 2 * 8 + 16) + result + result * 2 * 8 + 2) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a4 + 8) + v_r15 * 4 + 3));
    if ((*(unsigned int *)(*(unsigned __int64 *)(result + 72 + 336) + v_r10 + v_r10 * 2 * 8)) != -1) goto loc_007557AC;
    a1 = (*(unsigned __int64 *)(a4 + 8)) * ((unsigned int)(v_stack_p18));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72 + 336) + v_r10 + v_r10 * 2 * 8 + 16) + result + result * 2 * 8 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + result * 1 + 124)));
    goto loc_007557B4;
loc_007557AC:
    result = 0;
loc_007557B4:
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 72 + 336) + v_r10 + v_r10 * 2 * 8 + 16) + result + result * 2 * 8 + 16) = 0;
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(v_r15 + 1)));
    if (((unsigned int)(v_r15)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4))))) goto loc_0075573F;
loc_007557C9:
    v_r10 = (unsigned int)((v_r10) + ((unsigned int)(v_r15 + 1)));
    if (((unsigned int)(v_r10)) < (*(unsigned int *)(v_r14 + 8))) goto loc_00755700;
loc_007557DE:
    a3 = (result + 72) + (448);
    v_r14 = (v_r14) + (320);
    a1 = (v_stack_p20) - (v_r15 + 1);
    v_stack_p20 = a1;
    if (condition_is_not_equal) goto loc_007556DD;
loc_00755805:
    v_rbx = 0;
    if ((unsigned int)((unsigned int)(v_stack_p10)) == 0) goto loc_00755858;
loc_0075580C:
    result = KeGetPrcb(0, result + result * 2, a3, a4);
    v_r14 = 0;
    if ((unsigned int)((unsigned int)(v_stack_m58)) == 0) goto loc_00755851;
loc_00755821:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m58)))) - (0));
    result = (unsigned int)((result) - ((unsigned int)(v_r15 + 1)));
    result = PpmCheckCoordinatedStateInitiator(0, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 34880) + 1024) + result + result * 2 * 8 + 8)), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 34880) + 1024) + result + result * 2 * 8 + 16), a4);
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_r15 + 1)));
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 34880) + 1024) + result + result * 2 * 8 + 1) = (unsigned __int8)(result);
    if (((unsigned int)(v_r14)) < ((unsigned int)((unsigned int)(v_stack_m58)))) goto loc_00755821;
loc_00755851:
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(v_r15 + 1)));
    if (((unsigned int)(v_rbx)) < ((unsigned int)((unsigned int)(v_stack_p10)))) goto loc_0075580C;
loc_00755858:
    v_rsi = v_r15 + 1;
    if ((*(unsigned __int64 *)(v_rip + 8852080)) == 0) {
        a2 = (unsigned __int8)(v_r15 + 1);
        a1 = result;
        result = PpmEnableCoordinatedIdleStates(a1, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 34880) + 1024) + result + result * 2 * 8 + 16), a4);
        v_rsi = 0;
    }
    v_rbx = 0;
    if (0 == 0) goto loc_0075588A;
    goto loc_0075587E;
loc_00755879:
loc_0075587E:
    result = PopReleaseRwLock(v_rip + 8090091, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 34880) + 1024) + result + result * 2 * 8 + 16), a4);
loc_0075588A:
    v_rsp = (v_rsp) + (56);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
}
```

## 5. (Beta) C Style

```c
int64_t PpmInstallCoordinatedIdleStates(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (56);
    local_r15 = 0;
    result = PopAcquireRwLockExclusive(v_rip + 8091566, Arg2, Arg3, Arg4);
    if ((*(uint64_t *)(v_rip + 0x871802)) == 0) goto loc_007552E4;
    if ((*(uint8_t *)(arg1 + 0x28)) != 0) goto loc_007552E4;
    goto loc_0075587E;
loc_007552E4:
    result = PpmIdleUpdateCoordinatedDependencies(Arg1, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_0075587E;
    v_stack_m58 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))) == 0) goto loc_00755879;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) * ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x871774)))));
    Arg4 = 0;
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x871774)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))) == 0) goto loc_00755349;
loc_00755331:
    Arg4 = (uint32_t)((Arg4) + ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x158 + 0x4)))));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x158 + 0x4))) * (*(uint32_t *)(arg1 + 0x158)));
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) + ((uint32_t)(result)));
    local_r11 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) - (local_r15 + 1);
    if (condition_is_not_equal) goto loc_00755331;
loc_00755349:
    if (*(uint64_t *)(v_rip + 0x871780) != 0) goto loc_007556AE;
    Arg1 = (uint32_t)((Arg1 + 344 + 320) * ((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))));
    Arg1 = (uint32_t)((Arg1) + (71));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    v_stack_p18 = (uint32_t)(Arg1);
    v_stack_p20 = (uint32_t)(Arg1 + Arg4 + Arg4 * 2 * 8);
    local_r12 = (uint32_t)((Arg2 * 4 + 7) + ((uint32_t)(Arg1 + Arg4 + Arg4 * 2 * 8 + local_r10 + local_r10 * 2 * 8)));
    v_stack_m54 = (uint32_t)(Arg1 + Arg4 + Arg4 * 2 * 8 + local_r10 + local_r10 * 2 * 8);
    local_r12 = (uint32_t)((local_r12) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1)) * 4 + 15) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) << (10));
    result = (uint32_t)((result) + (47));
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) * ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x871774)))));
    result = (uint32_t)((result) + ((uint32_t)(local_r12)));
    v_stack_m50 = (uint32_t)(Arg1);
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    v_stack_m4C = (uint32_t)(result);
    local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(result)));
    if (*(uint64_t *)(v_rip + 0x712318) != 0) goto loc_007553F6;
loc_007553CD:
    result = ExAllocatePool2(72, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x694D5050ULL), Arg4);
    if (result != 0) goto loc_00755429;
    result = ExFreePoolWithTag(0, (uint32_t)(0x694D5050ULL), (uint32_t)(0x694D5050ULL), Arg4);
    goto loc_0075541F;
loc_007553F6:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x712318) + 0x4))) == 0) goto loc_007553CD;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x712318) + 0x4))))) * ((uint32_t)(0x694D5050ULL));
    Arg2 = (Arg2) << (6);
    result = ExAllocatePool2(64, Arg2, (uint32_t)(0x694D5050ULL), Arg4);
    if (result != 0) goto loc_007553CD;
loc_0075541F:
    goto loc_0075587E;
loc_00755429:
    *(uint32_t *)(result + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x871774)));
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    *(uint8_t *)(result + 0x8) = (uint8_t)(local_r15 + 1);
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(arg1 + 0x8);
    *(uint64_t *)(result + 0x18) = *(uint64_t *)(arg1 + 0x10);
    *(uint64_t *)(result + 0x20) = *(uint64_t *)(arg1 + 0x18);
    *(uint64_t *)(result + 0x28) = *(uint64_t *)(arg1 + 0x20);
    local_r13 = ((uint32_t)((uint32_t)(local_r12))) + (result);
    *(uint64_t *)(result + 0x30) = local_r13;
    *(uint32_t *)(local_r13 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    result = PpmResetPlatformIdleAccounting(local_r13, Arg2, (uint32_t)(0x694D5050ULL), Arg4);
    local_r10 = 0;
    if ((*(uint32_t *)(arg1)) <= 0) goto loc_007554E7;
loc_00755471:
    Arg4 = (Arg4) * (0);
    Arg1 = 0;
    result = (result + 88) + (Arg4);
    *(uint64_t *)(result + 0x8) = result;
    *(uint64_t *)(result) = result;
    *(uint8_t *)(Arg4 + result * 1 + 0x68) = 7;
    result = PpmIdleIsStateDisabled(Arg1, 0, (uint32_t)(0x694D5050ULL), Arg4);
    if ((uint8_t)(result) != 0) {
        *(uint32_t *)(Arg4 + result * 1 + 0x50) = 0x80000000ULL;
    }
    if ((uint32_t)((uint32_t)(0xC000009AULL)) == 0) goto loc_007554DF;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) - ((uint32_t)(local_r15 + 1)));
    if (0 == ((uint32_t)(result))) {
        *(uint8_t *)(Arg4 + result * 1 + 0x69) = (uint8_t)(local_r15 + 1);
    }
    *(uint64_t *)(Arg4 + result * 1 + 0x70) = result;
    result = ((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)))) << (6);
    local_r15 = (result) + (result);
    *(uint32_t *)(Arg4 + result * 1 + 0x6C) = (uint32_t)((uint32_t)(0xC000009AULL));
    result = (result + 80) + (Arg4);
    local_r11 = (0) << (10);
    *(uint64_t *)(local_r11 + local_r13 * 1 + 0xE0) = result;
loc_007554DF:
    local_r10 = (uint32_t)((local_r10) + ((uint32_t)(local_r15 + 1)));
    if (((uint32_t)(local_r10)) < (*(uint32_t *)(arg1))) goto loc_00755471;
loc_007554E7:
    result = ((uint32_t)(v_stack_p18)) + (result);
    local_r15 = ((uint32_t)(v_stack_p20)) + (result);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))) == 0) goto loc_007555D4;
loc_00755515:
    Arg2 = 0;
    *(uint64_t *)(result + 0x82 + 0x106) = v_xmm0;
    *(uint64_t *)(result + 0x82 - 0x42) = *(uint64_t *)(arg1 + 0x148);
    *(uint8_t *)(result + 0x82 - 0x8) = (uint8_t)(*(uint8_t *)(arg1 + 0x148 + 0x1C));
    *(uint32_t *)(result + 0x82 - 0x2) = 0x200001ULL;
    result = memset(result + 130 + 6, Arg2, 256, Arg4);
    result = KiCopyAffinityEx(result + 130 - 2, *(uint16_t *)(result + 0x82), Arg1 + 328 - 280, Arg4);
    Arg2 = 0;
    *(uint32_t *)(result + 0x82 - 0x6) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x148 + 0x14)));
    *(uint64_t *)(result + 0x82 + 0x116) = result;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x148 + 0x14))) == 0) goto loc_007555B1;
loc_0075558B:
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r15 + 1)));
    *(uint64_t *)(*(uint64_t *)(result + 0x82 + 0x116) + Arg2 + Arg2 * 2 * 8 + 0x10) = local_r15;
    if (((uint32_t)(Arg2)) < (*(uint32_t *)(arg1 + 0x148 + 0x14))) goto loc_0075558B;
loc_007555B1:
    local_r12 = (Arg1 + 328) + (320);
    local_r13 = (result + 130) + (448);
    local_rbp = ((uint32_t)(*(uint32_t *)(arg1))) - (local_r15 + 1);
    if (condition_is_not_equal) goto loc_00755515;
loc_007555D4:
    local_rbx = 0;
    local_r12 = ((uint32_t)(v_stack_m54)) + (result);
    if ((uint32_t)((uint32_t)(v_stack_p10)) == 0) goto loc_007556C0;
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m58))) + (uint32_t)((uint32_t)((uint32_t)(v_stack_m58))) * 2) << (3);
    result = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m58)))) << (2);
    v_stack_p20 = result;
loc_00755608:
    result = KeGetPrcb(0, Arg2, Arg1 + 328 - 280, Arg4);
    Arg4 = 0;
    result = (uint32_t)(((uint32_t)(v_stack_m50)) * (0));
    *(uint64_t *)(*(uint64_t *)(result + 0x8840) + 0x400) = local_r15 + (uint32_t)(*(uint32_t *)(arg1 + 0x148 + 0x10)) + (uint32_t)(*(uint32_t *)(arg1 + 0x148 + 0x10)) * 2 * 8;
    local_r15 = (local_r15 + (uint32_t)(*(uint32_t *)(arg1 + 0x148 + 0x10)) + (uint32_t)(*(uint32_t *)(arg1 + 0x148 + 0x10)) * 2 * 8) + (Arg1);
    *(uint64_t *)(*(uint64_t *)(result + 0x8840) + 0x418) = local_r12;
    local_r12 = (local_r12) + (v_stack_p20);
    result = (uint32_t)((result) + (v_stack_m4C));
    result = (result) + (result);
    *(uint32_t *)(*(uint64_t *)(result + 0x8840) + 0x3F8) = (uint32_t)((uint32_t)(v_stack_m58));
    *(uint64_t *)(*(uint64_t *)(result + 0x8840) + 0x3E0) = result;
    *(uint32_t *)(*(uint64_t *)(result + 0x8840) + 0x408) = (uint32_t)((uint32_t)(v_stack_m58));
    if ((uint32_t)((uint32_t)(v_stack_m58)) == 0) goto loc_00755699;
loc_00755660:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m58)))) - (0));
    result = (uint32_t)((result) - ((uint32_t)(local_r15 + 1)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8840) + 0x400) + result + result * 2 * 8 + 0x4) = 0;
    Arg4 = (uint32_t)((Arg4) + ((uint32_t)(local_r15 + 1)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8840) + 0x400) + result + result * 2 * 8 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x198 - 0x11C)));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8840) + 0x400) + result + result * 2 * 8 + 0x10) = *(uint64_t *)(result + 0x198);
    if (Arg4 < ((uint32_t)((uint32_t)(v_stack_m58)))) goto loc_00755660;
loc_00755699:
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(local_r15 + 1)));
    if (((uint32_t)(local_rbx)) < ((uint32_t)((uint32_t)(v_stack_p10)))) goto loc_00755608;
    goto loc_007556C0;
loc_007556AE:
    if ((*(uint32_t *)(result + 0x4)) != ((uint32_t)((uint32_t)(v_stack_p10)))) goto loc_00755879;
    if ((*(uint32_t *)(result)) != ((uint32_t)((uint32_t)(v_stack_m58)))) goto loc_00755879;
loc_007556C0:
    if ((uint32_t)((uint32_t)(v_stack_m58)) == 0) goto loc_00755805;
    v_stack_p20 = (uint32_t)((uint32_t)((uint32_t)(v_stack_m58)));
    local_r14 = (v_stack_p8) + (340);
loc_007556DD:
    local_r10 = 0;
    *(uint32_t *)(result + 0x48) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 - 0x4)));
    *(uint32_t *)(result + 0x48 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14)));
    *(uint8_t *)(result + 0x48 + 0x31) = (uint8_t)(*(uint8_t *)(local_r14 + 0xC));
    if ((*(uint32_t *)(local_r14 + 0x8)) <= 0) goto loc_007557DE;
loc_00755700:
    Arg4 = (0) << (4);
    Arg4 = (Arg4) + (*(uint64_t *)(local_r14 + 0x14));
    *(uint32_t *)(*(uint64_t *)(result + 0x48 + 0x150) + local_r10 + local_r10 * 2 * 8) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4)))) == -1) {
        *(uint8_t *)(result + 0x48 + 0x33) = (uint8_t)(local_r15 + 1);
    }
    local_r15 = 0;
    *(uint32_t *)(*(uint64_t *)(result + 0x48 + 0x150) + local_r10 + local_r10 * 2 * 8 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) == 0) goto loc_007557C9;
loc_0075573F:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg4 + 0x4))) - (0));
    result = (uint32_t)((result) - ((uint32_t)(local_r15 + 1)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48 + 0x150) + local_r10 + local_r10 * 2 * 8 + 0x10) + result + result * 2 * 8 + 0x4) = (uint32_t)(*(uint8_t *)(*(uint64_t *)(Arg4 + 0x8) + local_r15 * 4));
    v_stack_p18 = (uint32_t)(*(uint8_t *)(*(uint64_t *)(Arg4 + 0x8) + local_r15 * 4));
    result = ((*(uint8_t *)(*(uint64_t *)(Arg4 + 0x8) + local_r15 * 4 + 0x1)) == 0) ? 1 : 0;
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48 + 0x150) + local_r10 + local_r10 * 2 * 8 + 0x10) + result + result * 2 * 8) = (uint8_t)(result);
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48 + 0x150) + local_r10 + local_r10 * 2 * 8 + 0x10) + result + result * 2 * 8 + 0x1) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(Arg4 + 0x8) + local_r15 * 4 + 0x2));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48 + 0x150) + local_r10 + local_r10 * 2 * 8 + 0x10) + result + result * 2 * 8 + 0x2) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(Arg4 + 0x8) + local_r15 * 4 + 0x3));
    if ((*(uint32_t *)(*(uint64_t *)(result + 0x48 + 0x150) + local_r10 + local_r10 * 2 * 8)) != -1) goto loc_007557AC;
    Arg1 = (*(uint64_t *)(Arg4 + 0x8)) * ((uint32_t)(v_stack_p18));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48 + 0x150) + local_r10 + local_r10 * 2 * 8 + 0x10) + result + result * 2 * 8 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + result * 1 + 0x7C)));
    goto loc_007557B4;
loc_007557AC:
    result = 0;
loc_007557B4:
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x48 + 0x150) + local_r10 + local_r10 * 2 * 8 + 0x10) + result + result * 2 * 8 + 0x10) = 0;
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(local_r15 + 1)));
    if (((uint32_t)(local_r15)) < ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4))))) goto loc_0075573F;
loc_007557C9:
    local_r10 = (uint32_t)((local_r10) + ((uint32_t)(local_r15 + 1)));
    if (((uint32_t)(local_r10)) < (*(uint32_t *)(local_r14 + 0x8))) goto loc_00755700;
loc_007557DE:
    Arg3 = (result + 72) + (448);
    local_r14 = (local_r14) + (320);
    Arg1 = (v_stack_p20) - (local_r15 + 1);
    v_stack_p20 = Arg1;
    if (condition_is_not_equal) goto loc_007556DD;
loc_00755805:
    local_rbx = 0;
    if ((uint32_t)((uint32_t)(v_stack_p10)) == 0) goto loc_00755858;
loc_0075580C:
    result = KeGetPrcb(0, result + result * 2, Arg3, Arg4);
    local_r14 = 0;
    if ((uint32_t)((uint32_t)(v_stack_m58)) == 0) goto loc_00755851;
loc_00755821:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m58)))) - (0));
    result = (uint32_t)((result) - ((uint32_t)(local_r15 + 1)));
    result = PpmCheckCoordinatedStateInitiator(0, (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8840) + 0x400) + result + result * 2 * 8 + 0x8)), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8840) + 0x400) + result + result * 2 * 8 + 0x10), Arg4);
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(local_r15 + 1)));
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8840) + 0x400) + result + result * 2 * 8 + 0x1) = (uint8_t)(result);
    if (((uint32_t)(local_r14)) < ((uint32_t)((uint32_t)(v_stack_m58)))) goto loc_00755821;
loc_00755851:
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(local_r15 + 1)));
    if (((uint32_t)(local_rbx)) < ((uint32_t)((uint32_t)(v_stack_p10)))) goto loc_0075580C;
loc_00755858:
    local_rsi = local_r15 + 1;
    if ((*(uint64_t *)(v_rip + 0x871270)) == 0) {
        Arg2 = (uint8_t)(local_r15 + 1);
        Arg1 = result;
        result = PpmEnableCoordinatedIdleStates(Arg1, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8840) + 0x400) + result + result * 2 * 8 + 0x10), Arg4);
        local_rsi = 0;
    }
    local_rbx = 0;
    if (0 == 0) goto loc_0075588A;
    goto loc_0075587E;
loc_00755879:
loc_0075587E:
    result = PopReleaseRwLock(v_rip + 8090091, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8840) + 0x400) + result + result * 2 * 8 + 0x10), Arg4);
loc_0075588A:
    local_rsp = (local_rsp) + (56);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x118` | `64` | `R` |
| `Arg1` | `- 0x10` | `128` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x14` | `32` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x1C` | `8` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `8` | `R` |
| `Arg1` | `+ 0x140` | `64` | `R` |
| `Arg1` | `+ 0x148` | `64` | `R` |
| `Arg1` | `+ 0x158` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007552A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
