# MiTradePage

- RVA: `0x0028D160`–`0x0028DBA8` (길이 `2,632` bytes)
- VA: `0x000000014028D160`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00067034`
- 디코드: `591`개 명령, `2,632/2,632` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **36**; 고유 호출 대상: **28**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **34**

### Outgoing calls
- `0x0028D1E5` → [MiSafeLockPage](../32/MiSafeLockPage_function_00321620.md) (function, `0x00321620`)
- `0x0028D274` → [MiGetPfnSlabType](MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x0028D2FD` → [MiActivePageClaimCandidate](../31/MiActivePageClaimCandidate_function_0031BB00.md) (function, `0x0031BB00`)
- `0x0028D33B` → [MiUnlinkFreeOrZeroedPage](../33/MiUnlinkFreeOrZeroedPage_function_00336C40.md) (function, `0x00336C40`)
- `0x0028D35B` → [MiAddMdlPageToTradeBlock](../44/MiAddMdlPageToTradeBlock_function_00449920.md) (function, `0x00449920`)
- `0x0028D399` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0028D3E2` → [MiStealPage](../2B/MiStealPage_function_002B28D0.md) (function, `0x002B28D0`)
- `0x0028D42F` → [MiSetOriginalPtePfnFromFreeList](MiSetOriginalPtePfnFromFreeList_function_0028A99C.md) (function, `0x0028A99C`)
- `0x0028D509` → [MiTradeTransitionPage](MiTradeTransitionPage_function_0028B9AC.md) (function, `0x0028B9AC`)
- `0x0028D552` → [MiLockAndInsertPageInFreeList](../47/MiLockAndInsertPageInFreeList_function_00470FA8.md) (function, `0x00470FA8`)
- `0x0028D55C` → [MiTrimSharedPage](../29/MiTrimSharedPage_function_00297D14.md) (function, `0x00297D14`)
- `0x0028D574` → [MiIsPageOnBadList](../2B/MiIsPageOnBadList_function_002B1018.md) (function, `0x002B1018`)
- `0x0028D59D` → [MI_PAGE_TO_FULL_COLOR](../33/MI_PAGE_TO_FULL_COLOR_function_00337820.md) (function, `0x00337820`)
- `0x0028D5BA` → [MiColorHasSlists](MiColorHasSlists_function_0028B1D0.md) (function, `0x0028B1D0`)
- `0x0028D5CA` → [MiInvalidPteConforms](../37/MiInvalidPteConforms_function_00372A10.md) (function, `0x00372A10`)
- `0x0028D62C` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x0028D646` → [MiDrainZeroLookasides](../44/MiDrainZeroLookasides_function_0044D818.md) (function, `0x0044D818`)
- `0x0028D6A1` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x0028D6C9` → [MiSwapStackPage](../29/MiSwapStackPage_function_0029FDE0.md) (function, `0x0029FDE0`)
- `0x0028D74B` → [MiDemoteLargeFreePage](../43/MiDemoteLargeFreePage_function_00435118.md) (function, `0x00435118`)
- `0x0028D78F` → [MI_NODE_FROM_PFN](../2B/MI_NODE_FROM_PFN_function_002B0F30.md) (function, `0x002B0F30`)
- `0x0028D7B0` → [MiSnapPageMoveInProgress](../3B/MiSnapPageMoveInProgress_function_003B8C04.md) (function, `0x003B8C04`)
- `0x0028D7BF` → [MiSnapPageMoveInProgress](../3B/MiSnapPageMoveInProgress_function_003B8C04.md) (function, `0x003B8C04`)
- `0x0028D7D0` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x0028D7F4` → [MiWaitForPageMoveComplete](../3B/MiWaitForPageMoveComplete_function_003B8C30.md) (function, `0x003B8C30`)
- `0x0028D88E` → [MiReuseStandbyPage](../44/MiReuseStandbyPage_function_0044CA90.md) (function, `0x0044CA90`)
- `0x0028D8AB` → [MiAddMdlPageToTradeBlock](../44/MiAddMdlPageToTradeBlock_function_00449920.md) (function, `0x00449920`)
- `0x0028D8BE` → [MiLockAndInsertPageInFreeList](../47/MiLockAndInsertPageInFreeList_function_00470FA8.md) (function, `0x00470FA8`)
- `0x0028D8E1` → [MiGetBaseResidentPage](../31/MiGetBaseResidentPage_function_0031C750.md) (function, `0x0031C750`)
- `0x0028D8FF` → [MiGetPfnPageSizeIndex](../31/MiGetPfnPageSizeIndex_function_0031C710.md) (function, `0x0031C710`)
- `0x0028D930` → [MI_PAGE_TO_FULL_COLOR](../33/MI_PAGE_TO_FULL_COLOR_function_00337820.md) (function, `0x00337820`)
- `0x0028DA16` → [MiLargeFreePageToMdl](../42/MiLargeFreePageToMdl_function_00420880.md) (function, `0x00420880`)
- `0x0028DAB5` → [MiIsPageOnBadList](../2B/MiIsPageOnBadList_function_002B1018.md) (function, `0x002B1018`)
- `0x0028DAD0` → [MiIsPageOnBadList](../2B/MiIsPageOnBadList_function_002B1018.md) (function, `0x002B1018`)
- `0x0028DB03` → [MiReleaseFreshPageLocked](../44/MiReleaseFreshPageLocked_function_0044CDD8.md) (function, `0x0044CDD8`)
- `0x0028DB38` → [MiPfnLargeBitSet](../41/MiPfnLargeBitSet_function_00415A20.md) (function, `0x00415A20`)

### Direct callers
- [MiFindContiguousPagesEx](MiFindContiguousPagesEx_function_0028BDE0.md) at `0x0028C2DC`
- [MiClaimPhysicalRun](MiClaimPhysicalRun_function_0028CF00.md) at `0x0028CFDB`

### Static image references
- `0x0028D1FA` → RVA `0x00E30088` (`.data`; read)
- `0x0028D30B` → RVA `0x00EF531C` (`.data`; read/write)
- `0x0028D348` → RVA `0x00EF5224` (`.data`; read/write)
- `0x0028D388` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0028D41B` → RVA `0x00EF5238` (`.data`; read/write)
- `0x0028D421` → RVA `0x00010880` (`.rdata`; read)
- `0x0028D443` → RVA `0x00FCF080` (`CACHEALI`; read)
- `0x0028D566` → RVA `0x00EF52A4` (`.data`; read/write)
- `0x0028D5D7` → RVA `0x00E2DC80` (`.data`; read)
- `0x0028D640` → RVA `0x00EF5228` (`.data`; read/write)
- `0x0028D685` → RVA `0x00EF524C` (`.data`; read/write)
- `0x0028D6E5` → RVA `0x00EF5234` (`.data`; read/write)
- `0x0028D6F3` → RVA `0x00011C60` (`.rdata`; read)
- `0x0028D841` → RVA `0x00EF5254` (`.data`; read/write)
- `0x0028D862` → RVA `0x00EF5244` (`.data`; read/write)
- `0x0028D8B5` → RVA `0x00EF5250` (`.data`; read/write)
- `0x0028D8C8` → RVA `0x00EF529C` (`.data`; read/write)
- `0x0028D8D3` → RVA `0x00EF5264` (`.data`; read/write)
- `0x0028D974` → RVA `0x00EF5258` (`.data`; read/write)
- `0x0028D99B` → RVA `0x00EF522C` (`.data`; read/write)
- `0x0028D9A6` → RVA `0x00EF5260` (`.data`; read/write)
- `0x0028D9B9` → RVA `0x00EF5270` (`.data`; read/write)
- `0x0028D9C4` → RVA `0x00EF5298` (`.data`; read/write)
- `0x0028D9CF` → RVA `0x00EF5248` (`.data`; read/write)
- `0x0028DA2E` → RVA `0x00EF5240` (`.data`; read/write)
- `0x0028DA44` → RVA `0x00EF5288` (`.data`; read/write)
- `0x0028DAA7` → RVA `0x00EF5284` (`.data`; read/write)
- `0x0028DAC2` → RVA `0x00EF5290` (`.data`; read/write)
- `0x0028DADF` → RVA `0x00EF5268` (`.data`; read/write)
- `0x0028DAEA` → RVA `0x00EF525C` (`.data`; read/write)
- `0x0028DAF5` → RVA `0x00EF5274` (`.data`; read/write)
- `0x0028DB31` → RVA `0x00E38D00` (`.data`; read)
- `0x0028DB6B` → RVA `0x00EF5294` (`.data`; read/write)
- `0x0028DB83` → RVA `0x00EF528C` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0028D160  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0028D165  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0028D16A  53                              push rbx
0028D16B  55                              push rbp
0028D16C  56                              push rsi
0028D16D  57                              push rdi
0028D16E  41 54                           push r12
0028D170  41 55                           push r13
0028D172  41 56                           push r14
0028D174  41 57                           push r15
0028D176  48 83 EC 78                     sub rsp, 0x78
0028D17A  44 8B 69 18                     mov r13d, dword ptr [rcx + 0x18]
0028D17E  33 ED                           xor ebp, ebp
0028D180  48 8B 01                        mov rax, qword ptr [rcx]
0028D183  48 8B DA                        mov rbx, rdx
0028D186  89 6C 24 30                     mov dword ptr [rsp + 0x30], ebp
0028D18A  4C 8B F1                        mov r14, rcx
0028D18D  48 89 69 28                     mov qword ptr [rcx + 0x28], rbp
0028D191  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0028D196  41 0F BA E5 16                  bt r13d, 0x16
0028D19B  0F 82 10 08 00 00               jb 0x14028d9b1
0028D1A1  8B FD                           mov edi, ebp
0028D1A3  48 8D 34 52                     lea rsi, [rdx + rdx*2]
0028D1A7  48 89 6C 24 48                  mov qword ptr [rsp + 0x48], rbp
0028D1AC  48 C1 E6 04                     shl rsi, 4
0028D1B0  49 C7 C4 FF FF FF FF            mov r12, 0xffffffffffffffff
0028D1B7  C7 44 24 50 01 00 00 00         mov dword ptr [rsp + 0x50], 1
0028D1BF  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0028D1C9  48 8B C0                        mov rax, rax
0028D1CC  48 03 F0                        add rsi, rax
0028D1CF  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
0028D1D3  49 8B CC                        mov rcx, r12
0028D1D6  48 3B C1                        cmp rax, rcx
0028D1D9  48 0F 45 C8                     cmovne rcx, rax
0028D1DD  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
0028D1E2  48 8B CB                        mov rcx, rbx
0028D1E5  E8 36 44 09 00                  call 0x140321620
0028D1EA  44 0F B6 F8                     movzx r15d, al
0028D1EE  3C 11                           cmp al, 0x11
0028D1F0  0F 84 D9 07 00 00               je 0x14028d9cf
0028D1F6  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0028D1FA  48 8B 0D 87 2E BA 00            mov rcx, qword ptr [rip + 0xba2e87]
0028D201  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
0028D206  48 C1 E8 2B                     shr rax, 0x2b
0028D20A  25 FF 03 00 00                  and eax, 0x3ff
0028D20F  48 39 14 C1                     cmp qword ptr [rcx + rax*8], rdx
0028D213  0F 85 05 09 00 00               jne 0x14028db1e
0028D219  44 0F B6 46 22                  movzx r8d, byte ptr [rsi + 0x22]
0028D21E  41 BA 03 00 00 00               mov r10d, 3
0028D224  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0028D228  41 83 E0 07                     and r8d, 7
0028D22C  48 0F BA E0 28                  bt rax, 0x28
0028D231  44 89 94 24 C0 00 00 00         mov dword ptr [rsp + 0xc0], r10d
0028D239  48 8B D5                        mov rdx, rbp
0028D23C  44 89 84 24 D8 00 00 00         mov dword ptr [rsp + 0xd8], r8d
0028D244  8B DD                           mov ebx, ebp
0028D246  0F 82 92 06 00 00               jb 0x14028d8de
0028D24C  41 83 F8 05                     cmp r8d, 5
0028D250  0F 84 1B 03 00 00               je 0x14028d571
0028D256  48 0F BA 66 28 35               bt qword ptr [rsi + 0x28], 0x35
0028D25C  0F 82 B1 08 00 00               jb 0x14028db13
0028D262  41 8B C5                        mov eax, r13d
0028D265  25 00 00 41 00                  and eax, 0x410000
0028D26A  3D 00 00 41 00                  cmp eax, 0x410000
0028D26F  74 11                           je 0x14028d282
0028D271  48 8B CE                        mov rcx, rsi
0028D274  E8 57 10 00 00                  call 0x14028e2d0
0028D279  83 F8 09                        cmp eax, 9
0028D27C  0F 85 03 04 00 00               jne 0x14028d685
0028D282  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
0028D285  8B C8                           mov ecx, eax
0028D287  C1 E9 10                        shr ecx, 0x10
0028D28A  C1 E8 18                        shr eax, 0x18
0028D28D  A8 40                           test al, 0x40
0028D28F  0F 85 A4 07 00 00               jne 0x14028da39
0028D295  41 83 F8 01                     cmp r8d, 1
0028D299  76 7C                           jbe 0x14028d317
0028D29B  84 C0                           test al, al
0028D29D  0F 88 D2 05 00 00               js 0x14028d875
0028D2A3  41 83 F8 04                     cmp r8d, 4
0028D2A7  0F 86 1B 02 00 00               jbe 0x14028d4c8
0028D2AD  41 83 F8 06                     cmp r8d, 6
0028D2B1  0F 85 0D 07 00 00               jne 0x14028d9c4
0028D2B7  41 0F BA E5 15                  bt r13d, 0x15
0028D2BC  0F 82 0B 08 00 00               jb 0x14028dacd
0028D2C2  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0028D2C6  48 C1 E8 3C                     shr rax, 0x3c
0028D2CA  24 07                           and al, 7
0028D2CC  3C 02                           cmp al, 2
0028D2CE  0F 84 BC 03 00 00               je 0x14028d690
0028D2D4  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
0028D2DC  45 8B CD                        mov r9d, r13d
0028D2DF  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0028D2E4  41 B8 01 00 00 00               mov r8d, 1
0028D2EA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0028D2EF  48 8B CB                        mov rcx, rbx
0028D2F2  48 8B D6                        mov rdx, rsi
0028D2F5  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
0028D2FD  E8 FE E7 08 00                  call 0x14031bb00
0028D302  48 85 C0                        test rax, rax
0028D305  0F 84 A0 00 00 00               je 0x14028d3ab
0028D30B  FF 05 0B 80 C6 00               inc dword ptr [rip + 0xc6800b]
0028D311  49 89 46 28                     mov qword ptr [r14 + 0x28], rax
0028D315  EB 58                           jmp 0x14028d36f
0028D317  41 83 FA 03                     cmp r10d, 3
0028D31B  0F 85 CF 03 00 00               jne 0x14028d6f0
0028D321  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
0028D329  41 0F BA E5 16                  bt r13d, 0x16
0028D32E  72 18                           jb 0x14028d348
0028D330  33 D2                           xor edx, edx
0028D332  41 B8 00 01 00 00               mov r8d, 0x100
0028D338  48 8B CB                        mov rcx, rbx
0028D33B  E8 00 99 0A 00                  call 0x140336c40
0028D340  85 C0                           test eax, eax
0028D342  0F 84 71 06 00 00               je 0x14028d9b9
0028D348  FF 05 D6 7E C6 00               inc dword ptr [rip + 0xc67ed6]
0028D34E  41 0F BA E5 16                  bt r13d, 0x16
0028D353  72 0B                           jb 0x14028d360
0028D355  48 8B D3                        mov rdx, rbx
0028D358  49 8B CE                        mov rcx, r14
0028D35B  E8 C0 C5 1B 00                  call 0x140449920
0028D360  BD 01 00 00 00                  mov ebp, 1
0028D365  41 80 FF 11                     cmp r15b, 0x11
0028D369  0F 84 40 01 00 00               je 0x14028d4af
0028D36F  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0028D379  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
0028D37E  41 80 FF 02                     cmp r15b, 2
0028D382  0F 83 27 01 00 00               jae 0x14028d4af
0028D388  83 3D 91 99 D3 00 00            cmp dword ptr [rip + 0xd39991], 0
0028D38F  74 0D                           je 0x14028d39e
0028D391  44 0F 20 C1                     mov rcx, cr8
0028D395  41 0F B6 D7                     movzx edx, r15b
0028D399  E8 FA 82 26 00                  call 0x1404f5698
0028D39E  41 0F B6 C7                     movzx eax, r15b
0028D3A2  44 0F 22 C0                     mov cr8, rax
0028D3A6  E9 04 01 00 00                  jmp 0x14028d4af
0028D3AB  41 F6 C5 08                     test r13b, 8
0028D3AF  0F 85 B6 07 00 00               jne 0x14028db6b
0028D3B5  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0028D3B9  45 8B C5                        mov r8d, r13d
0028D3BC  41 0F B6 D7                     movzx edx, r15b
0028D3C0  48 8B CE                        mov rcx, rsi
0028D3C3  48 85 C0                        test rax, rax
0028D3C6  0F 88 90 01 00 00               js 0x14028d55c
0028D3CC  4D 8B 4E 08                     mov r9, qword ptr [r14 + 8]
0028D3D0  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0028D3D5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0028D3DA  41 8B 46 1C                     mov eax, dword ptr [r14 + 0x1c]
0028D3DE  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0028D3E2  E8 E9 54 02 00                  call 0x1402b28d0
0028D3E7  83 F8 02                        cmp eax, 2
0028D3EA  0F 84 AB 07 00 00               je 0x14028db9b
0028D3F0  85 C0                           test eax, eax
0028D3F2  0F 84 6E 01 00 00               je 0x14028d566
0028D3F8  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0028D3FC  48 8B 0D 85 2C BA 00            mov rcx, qword ptr [rip + 0xba2c85]
0028D403  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
0028D408  48 C1 E8 2B                     shr rax, 0x2b
0028D40C  25 FF 03 00 00                  and eax, 0x3ff
0028D411  48 39 1C C1                     cmp qword ptr [rcx + rax*8], rbx
0028D415  0F 85 9A 04 00 00               jne 0x14028d8b5
0028D41B  FF 05 17 7E C6 00               inc dword ptr [rip + 0xc67e17]
0028D421  48 8B 05 58 34 D8 FF            mov rax, qword ptr [rip - 0x27cba8]
0028D428  48 8D 4E 10                     lea rcx, [rsi + 0x10]
0028D42C  48 89 01                        mov qword ptr [rcx], rax
0028D42F  E8 68 D5 FF FF                  call 0x14028a99c
0028D434  41 0F BA E5 16                  bt r13d, 0x16
0028D439  0F 82 10 01 00 00               jb 0x14028d54f
0028D43F  F0 09 2C 24                     lock or dword ptr [rsp], ebp
0028D443  44 8B 05 36 1C D4 00            mov r8d, dword ptr [rip + 0xd41c36]
0028D44A  49 B9 FF FF FF FF FF FF FF C7   movabs r9, 0xc7ffffffffffffff
0028D454  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
0028D458  49 C1 E0 3B                     shl r8, 0x3b
0028D45C  48 8B C1                        mov rax, rcx
0028D45F  49 8B D0                        mov rdx, r8
0028D462  48 33 D1                        xor rdx, rcx
0028D465  49 23 D1                        and rdx, r9
0028D468  49 33 D0                        xor rdx, r8
0028D46B  F0 48 0F B1 56 18               lock cmpxchg qword ptr [rsi + 0x18], rdx
0028D471  48 8B D0                        mov rdx, rax
0028D474  48 3B C8                        cmp rcx, rax
0028D477  74 24                           je 0x14028d49d
0028D479  0F 1F 80 00 00 00 00            nop dword ptr [rax]
0028D480  48 8B CA                        mov rcx, rdx
0028D483  49 33 D0                        xor rdx, r8
0028D486  49 23 D1                        and rdx, r9
0028D489  48 8B C1                        mov rax, rcx
0028D48C  49 33 D0                        xor rdx, r8
0028D48F  F0 48 0F B1 56 18               lock cmpxchg qword ptr [rsi + 0x18], rdx
0028D495  48 8B D0                        mov rdx, rax
0028D498  48 3B C8                        cmp rcx, rax
0028D49B  75 E3                           jne 0x14028d480
0028D49D  49 8B 4E 38                     mov rcx, qword ptr [r14 + 0x38]
0028D4A1  48 85 C9                        test rcx, rcx
0028D4A4  0F 85 AE 01 00 00               jne 0x14028d658
0028D4AA  BD 01 00 00 00                  mov ebp, 1
0028D4AF  4D 89 66 20                     mov qword ptr [r14 + 0x20], r12
0028D4B3  48 8B C5                        mov rax, rbp
0028D4B6  48 83 C4 78                     add rsp, 0x78
0028D4BA  41 5F                           pop r15
0028D4BC  41 5E                           pop r14
0028D4BE  41 5D                           pop r13
0028D4C0  41 5C                           pop r12
0028D4C2  5F                              pop rdi
0028D4C3  5E                              pop rsi
0028D4C4  5D                              pop rbp
0028D4C5  5B                              pop rbx
0028D4C6  C3                              ret
0028D4C7  CC                              int3
0028D4C8  41 0F BA E5 1A                  bt r13d, 0x1a
0028D4CD  72 18                           jb 0x14028d4e7
0028D4CF  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0028D4D3  48 0F BA E0 28                  bt rax, 0x28
0028D4D8  72 0D                           jb 0x14028d4e7
0028D4DA  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0028D4DE  48 85 C0                        test rax, rax
0028D4E1  0F 89 8F 06 00 00               jns 0x14028db76
0028D4E7  41 0F BA E5 15                  bt r13d, 0x15
0028D4EC  0F 82 C0 05 00 00               jb 0x14028dab2
0028D4F2  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0028D4F7  45 8B CD                        mov r9d, r13d
0028D4FA  44 8B C7                        mov r8d, edi
0028D4FD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0028D502  41 0F B6 D7                     movzx edx, r15b
0028D506  48 8B CE                        mov rcx, rsi
0028D509  E8 9E E4 FF FF                  call 0x14028b9ac
0028D50E  83 F8 02                        cmp eax, 2
0028D511  0F 84 61 01 00 00               je 0x14028d678
0028D517  83 F8 03                        cmp eax, 3
0028D51A  75 93                           jne 0x14028d4af
0028D51C  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0028D520  48 8B 0D 61 2B BA 00            mov rcx, qword ptr [rip + 0xba2b61]
0028D527  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
0028D52C  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
0028D531  48 C1 E8 2B                     shr rax, 0x2b
0028D535  25 FF 03 00 00                  and eax, 0x3ff
0028D53A  48 39 14 C1                     cmp qword ptr [rcx + rax*8], rdx
0028D53E  0F 85 71 03 00 00               jne 0x14028d8b5
0028D544  41 0F BA E5 16                  bt r13d, 0x16
0028D549  0F 83 4E FF FF FF               jae 0x14028d49d
0028D54F  48 8B CE                        mov rcx, rsi
0028D552  E8 51 3A 1E 00                  call 0x140470fa8
0028D557  E9 4E FF FF FF                  jmp 0x14028d4aa
0028D55C  E8 B3 A7 00 00                  call 0x140297d14
0028D561  E9 81 FE FF FF                  jmp 0x14028d3e7
0028D566  FF 05 38 7D C6 00               inc dword ptr [rip + 0xc67d38]
0028D56C  E9 3E FF FF FF                  jmp 0x14028d4af
0028D571  48 8B CE                        mov rcx, rsi
0028D574  E8 9F 3A 02 00                  call 0x1402b1018
0028D579  85 C0                           test eax, eax
0028D57B  0F 85 69 05 00 00               jne 0x14028daea
0028D581  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0028D585  48 83 F8 F8                     cmp rax, -8
0028D589  0F 84 17 04 00 00               je 0x14028d9a6
0028D58F  41 83 FA 03                     cmp r10d, 3
0028D593  75 23                           jne 0x14028d5b8
0028D595  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
0028D59D  E8 7E A2 0A 00                  call 0x140337820
0028D5A2  48 8B 56 10                     mov rdx, qword ptr [rsi + 0x10]
0028D5A6  8B D8                           mov ebx, eax
0028D5A8  44 8B 84 24 D8 00 00 00         mov r8d, dword ptr [rsp + 0xd8]
0028D5B0  44 8B 94 24 C0 00 00 00         mov r10d, dword ptr [rsp + 0xc0]
0028D5B8  8B CB                           mov ecx, ebx
0028D5BA  E8 11 DC FF FF                  call 0x14028b1d0
0028D5BF  85 C0                           test eax, eax
0028D5C1  0F 84 99 01 00 00               je 0x14028d760
0028D5C7  48 8B CA                        mov rcx, rdx
0028D5CA  E8 41 54 0E 00                  call 0x140372a10
0028D5CF  85 C0                           test eax, eax
0028D5D1  0F 84 FC 02 00 00               je 0x14028d8d3
0028D5D7  48 8B 0D A2 06 BA 00            mov rcx, qword ptr [rip + 0xba06a2]
0028D5DE  48 8B C2                        mov rax, rdx
0028D5E1  48 85 C9                        test rcx, rcx
0028D5E4  74 0E                           je 0x14028d5f4
0028D5E6  F6 C2 10                        test dl, 0x10
0028D5E9  75 09                           jne 0x14028d5f4
0028D5EB  48 8B C1                        mov rax, rcx
0028D5EE  48 F7 D0                        not rax
0028D5F1  48 23 C2                        and rax, rdx
0028D5F4  48 C1 E8 20                     shr rax, 0x20
0028D5F8  B9 FE FF FF FF                  mov ecx, 0xfffffffe
0028D5FD  48 3B C1                        cmp rax, rcx
0028D600  0F 85 CD 02 00 00               jne 0x14028d8d3
0028D606  48 39 74 24 48                  cmp qword ptr [rsp + 0x48], rsi
0028D60B  0F 84 76 03 00 00               je 0x14028d987
0028D611  48 8B C2                        mov rax, rdx
0028D614  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
0028D619  48 C1 E8 0C                     shr rax, 0xc
0028D61D  41 0F B6 D7                     movzx edx, r15b
0028D621  83 E0 0F                        and eax, 0xf
0028D624  48 8B CE                        mov rcx, rsi
0028D627  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0028D62C  E8 AF CD 08 00                  call 0x14031a3e0
0028D631  4D 8B 46 10                     mov r8, qword ptr [r14 + 0x10]
0028D635  44 8B CB                        mov r9d, ebx
0028D638  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0028D63D  48 8B D6                        mov rdx, rsi
0028D640  FF 05 E2 7B C6 00               inc dword ptr [rip + 0xc67be2]
0028D646  E8 CD 01 1C 00                  call 0x14044d818
0028D64B  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
0028D653  E9 77 FB FF FF                  jmp 0x14028d1cf
0028D658  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
0028D65B  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
0028D663  48 C1 E8 0C                     shr rax, 0xc
0028D667  48 89 54 C1 30                  mov qword ptr [rcx + rax*8 + 0x30], rdx
0028D66C  81 41 28 00 10 00 00            add dword ptr [rcx + 0x28], 0x1000
0028D673  E9 32 FE FF FF                  jmp 0x14028d4aa
0028D678  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
0028D680  E9 4A FB FF FF                  jmp 0x14028d1cf
0028D685  FF 05 C1 7B C6 00               inc dword ptr [rip + 0xc67bc1]
0028D68B  E9 DF FC FF FF                  jmp 0x14028d36f
0028D690  41 F6 C5 08                     test r13b, 8
0028D694  0F 85 D1 04 00 00               jne 0x14028db6b
0028D69A  41 0F B6 D7                     movzx edx, r15b
0028D69E  48 8B CE                        mov rcx, rsi
0028D6A1  E8 3A CD 08 00                  call 0x14031a3e0
0028D6A6  45 8B 46 1C                     mov r8d, dword ptr [r14 + 0x1c]
0028D6AA  48 8D 44 24 30                  lea rax, [rsp + 0x30]
0028D6AF  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0028D6B4  45 8B CD                        mov r9d, r13d
0028D6B7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0028D6BC  48 8B D6                        mov rdx, rsi
0028D6BF  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0028D6C4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0028D6C9  E8 12 27 01 00                  call 0x14029fde0
0028D6CE  85 C0                           test eax, eax
0028D6D0  0F 84 7E 01 00 00               je 0x14028d854
0028D6D6  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
0028D6DB  39 6C 24 30                     cmp dword ptr [rsp + 0x30], ebp
0028D6DF  0F 84 49 03 00 00               je 0x14028da2e
0028D6E5  FF 05 49 7B C6 00               inc dword ptr [rip + 0xc67b49]
0028D6EB  E9 31 FD FF FF                  jmp 0x14028d421
0028D6F0  41 8B C2                        mov eax, r10d
0028D6F3  48 8D 0D 66 45 D8 FF            lea rcx, [rip - 0x27ba9a]
0028D6FA  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
0028D6FE  48 89 94 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rdx
0028D706  41 0F BA E5 19                  bt r13d, 0x19
0028D70B  0F 82 3E 03 00 00               jb 0x14028da4f
0028D711  41 0F BA E5 18                  bt r13d, 0x18
0028D716  0F 82 45 03 00 00               jb 0x14028da61
0028D71C  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
0028D724  48 8D 42 FF                     lea rax, [rdx - 1]
0028D728  48 F7 D0                        not rax
0028D72B  48 23 C3                        and rax, rbx
0028D72E  48 3B C3                        cmp rax, rbx
0028D731  0F 94 C1                        sete cl
0028D734  41 0F BA E5 16                  bt r13d, 0x16
0028D739  0F 93 C0                        setae al
0028D73C  84 C8                           test al, cl
0028D73E  0F 85 96 02 00 00               jne 0x14028d9da
0028D744  41 0F B6 D7                     movzx edx, r15b
0028D748  48 8B CB                        mov rcx, rbx
0028D74B  E8 C8 79 1A 00                  call 0x140435118
0028D750  85 C0                           test eax, eax
0028D752  0F 84 77 FA FF FF               je 0x14028d1cf
0028D758  41 B7 11                        mov r15b, 0x11
0028D75B  E9 E8 FB FF FF                  jmp 0x14028d348
0028D760  41 83 FA 03                     cmp r10d, 3
0028D764  0F 84 EC FA FF FF               je 0x14028d256
0028D76A  41 0F BA E5 19                  bt r13d, 0x19
0028D76F  73 0A                           jae 0x14028d77b
0028D771  41 83 FA 01                     cmp r10d, 1
0028D775  0F 86 F4 FB FF FF               jbe 0x14028d36f
0028D77B  41 0F BA E5 18                  bt r13d, 0x18
0028D780  73 0A                           jae 0x14028d78c
0028D782  41 83 FA 02                     cmp r10d, 2
0028D786  0F 84 E3 FB FF FF               je 0x14028d36f
0028D78C  48 8B CE                        mov rcx, rsi
0028D78F  E8 9C 37 02 00                  call 0x1402b0f30
0028D794  8B C8                           mov ecx, eax
0028D796  BA 02 00 00 00                  mov edx, 2
0028D79B  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0028D7A0  48 69 C9 80 DF 00 00            imul rcx, rcx, 0xdf80
0028D7A7  48 03 48 10                     add rcx, qword ptr [rax + 0x10]
0028D7AB  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
0028D7B0  E8 4F B4 12 00                  call 0x1403b8c04
0028D7B5  BA 01 00 00 00                  mov edx, 1
0028D7BA  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0028D7BF  E8 40 B4 12 00                  call 0x1403b8c04
0028D7C4  41 0F B6 D7                     movzx edx, r15b
0028D7C8  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0028D7CD  48 8B CE                        mov rcx, rsi
0028D7D0  E8 0B CC 08 00                  call 0x14031a3e0
0028D7D5  48 8D 5C 24 60                  lea rbx, [rsp + 0x60]
0028D7DA  44 8B FD                        mov r15d, ebp
0028D7DD  48 89 9C 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rbx
0028D7E5  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0028D7EA  41 8B C7                        mov eax, r15d
0028D7ED  F7 D8                           neg eax
0028D7EF  1B D2                           sbb edx, edx
0028D7F1  83 C2 02                        add edx, 2
0028D7F4  E8 37 B4 12 00                  call 0x1403b8c30
0028D7F9  48 33 03                        xor rax, qword ptr [rbx]
0028D7FC  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
0028D804  48 A9 00 00 FF FF               test rax, -0x10000
0028D80A  0F 85 BF F9 FF FF               jne 0x14028d1cf
0028D810  48 8B 9C 24 D8 00 00 00         mov rbx, qword ptr [rsp + 0xd8]
0028D818  41 FF C7                        inc r15d
0028D81B  48 83 C3 08                     add rbx, 8
0028D81F  48 89 9C 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rbx
0028D827  41 83 FF 02                     cmp r15d, 2
0028D82B  72 B8                           jb 0x14028d7e5
0028D82D  0F 85 5B 03 00 00               jne 0x14028db8e
0028D833  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
0028D83A  48 8D 0D 1F 44 D8 FF            lea rcx, [rip - 0x27bbe1]
0028D841  FF 05 0D 7A C6 00               inc dword ptr [rip + 0xc67a0d]
0028D847  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
0028D84B  49 89 46 28                     mov qword ptr [r14 + 0x28], rax
0028D84F  E9 5B FC FF FF                  jmp 0x14028d4af
0028D854  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0028D858  48 C1 E8 3C                     shr rax, 0x3c
0028D85C  24 07                           and al, 7
0028D85E  3C 02                           cmp al, 2
0028D860  74 66                           je 0x14028d8c8
0028D862  FF 05 DC 79 C6 00               inc dword ptr [rip + 0xc679dc]
0028D868  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
0028D870  E9 5A F9 FF FF                  jmp 0x14028d1cf
0028D875  41 83 F8 02                     cmp r8d, 2
0028D879  0F 85 F1 01 00 00               jne 0x14028da70
0028D87F  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
0028D882  66 85 C0                        test ax, ax
0028D885  0F 85 6A 02 00 00               jne 0x14028daf5
0028D88B  48 8B CE                        mov rcx, rsi
0028D88E  E8 FD F1 1B 00                  call 0x14044ca90
0028D893  85 C0                           test eax, eax
0028D895  0F 84 65 02 00 00               je 0x14028db00
0028D89B  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
0028D8A3  49 8B CE                        mov rcx, r14
0028D8A6  BD 01 00 00 00                  mov ebp, 1
0028D8AB  E8 70 C0 1B 00                  call 0x140449920
0028D8B0  E9 BA FA FF FF                  jmp 0x14028d36f
0028D8B5  FF 05 95 79 C6 00               inc dword ptr [rip + 0xc67995]
0028D8BB  48 8B CE                        mov rcx, rsi
0028D8BE  E8 E5 36 1E 00                  call 0x140470fa8
0028D8C3  E9 E7 FB FF FF                  jmp 0x14028d4af
0028D8C8  FF 05 CE 79 C6 00               inc dword ptr [rip + 0xc679ce]
0028D8CE  E9 DC FB FF FF                  jmp 0x14028d4af
0028D8D3  FF 05 8B 79 C6 00               inc dword ptr [rip + 0xc6798b]
0028D8D9  E9 91 FA FF FF                  jmp 0x14028d36f
0028D8DE  48 8B CE                        mov rcx, rsi
0028D8E1  E8 6A EE 08 00                  call 0x14031c750
0028D8E6  48 8B D8                        mov rbx, rax
0028D8E9  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0028D8EE  48 8B CB                        mov rcx, rbx
0028D8F1  0F B6 40 22                     movzx eax, byte ptr [rax + 0x22]
0028D8F5  83 E0 07                        and eax, 7
0028D8F8  89 84 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], eax
0028D8FF  E8 0C EE 08 00                  call 0x14031c710
0028D904  89 84 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], eax
0028D90B  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0028D915  48 8B C0                        mov rax, rax
0028D918  48 8B CB                        mov rcx, rbx
0028D91B  48 2B C8                        sub rcx, rax
0028D91E  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
0028D928  48 C1 F9 04                     sar rcx, 4
0028D92C  48 0F AF C8                     imul rcx, rax
0028D930  E8 EB 9E 0A 00                  call 0x140337820
0028D935  8B D8                           mov ebx, eax
0028D937  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0028D93C  48 8B 50 10                     mov rdx, qword ptr [rax + 0x10]
0028D940  48 3B C6                        cmp rax, rsi
0028D943  74 0F                           je 0x14028d954
0028D945  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
0028D94F  F0 48 21 48 18                  lock and qword ptr [rax + 0x18], rcx
0028D954  44 8B 84 24 D8 00 00 00         mov r8d, dword ptr [rsp + 0xd8]
0028D95C  41 83 F8 06                     cmp r8d, 6
0028D960  0F 85 F8 01 00 00               jne 0x14028db5e
0028D966  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
0028D96D  48 8D 0D EC 42 D8 FF            lea rcx, [rip - 0x27bd14]
0028D974  FF 05 DE 78 C6 00               inc dword ptr [rip + 0xc678de]
0028D97A  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
0028D97E  49 89 46 28                     mov qword ptr [r14 + 0x28], rax
0028D982  E9 E8 F9 FF FF                  jmp 0x14028d36f
0028D987  48 8B C2                        mov rax, rdx
0028D98A  48 C1 E8 0C                     shr rax, 0xc
0028D98E  83 E0 0F                        and eax, 0xf
0028D991  39 44 24 50                     cmp dword ptr [rsp + 0x50], eax
0028D995  0F 84 44 01 00 00               je 0x14028dadf
0028D99B  FF 05 8B 78 C6 00               inc dword ptr [rip + 0xc6788b]
0028D9A1  E9 6B FC FF FF                  jmp 0x14028d611
0028D9A6  FF 05 B4 78 C6 00               inc dword ptr [rip + 0xc678b4]
0028D9AC  E9 BE F9 FF FF                  jmp 0x14028d36f
0028D9B1  8B 79 1C                        mov edi, dword ptr [rcx + 0x1c]
0028D9B4  E9 EA F7 FF FF                  jmp 0x14028d1a3
0028D9B9  FF 05 B1 78 C6 00               inc dword ptr [rip + 0xc678b1]
0028D9BF  E9 AB F9 FF FF                  jmp 0x14028d36f
0028D9C4  FF 05 CE 78 C6 00               inc dword ptr [rip + 0xc678ce]
0028D9CA  E9 A0 F9 FF FF                  jmp 0x14028d36f
0028D9CF  FF 05 73 78 C6 00               inc dword ptr [rip + 0xc67873]
0028D9D5  E9 D5 FA FF FF                  jmp 0x14028d4af
0028D9DA  49 39 56 10                     cmp qword ptr [r14 + 0x10], rdx
0028D9DE  0F 82 60 FD FF FF               jb 0x14028d744
0028D9E4  48 8D 43 FF                     lea rax, [rbx - 1]
0028D9E8  48 03 C2                        add rax, rdx
0028D9EB  49 3B 46 30                     cmp rax, qword ptr [r14 + 0x30]
0028D9EF  0F 87 4F FD FF FF               ja 0x14028d744
0028D9F5  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0028D9F9  48 0F BA E0 29                  bt rax, 0x29
0028D9FE  0F 82 40 FD FF FF               jb 0x14028d744
0028DA04  4D 8B 46 38                     mov r8, qword ptr [r14 + 0x38]
0028DA08  45 8B CD                        mov r9d, r13d
0028DA0B  41 8B D2                        mov edx, r10d
0028DA0E  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
0028DA13  48 8B CB                        mov rcx, rbx
0028DA16  E8 65 2E 19 00                  call 0x140420880
0028DA1B  48 8B AC 24 C0 00 00 00         mov rbp, qword ptr [rsp + 0xc0]
0028DA23  01 2D FB 77 C6 00               add dword ptr [rip + 0xc677fb], ebp
0028DA29  E9 81 FA FF FF                  jmp 0x14028d4af
0028DA2E  FF 05 0C 78 C6 00               inc dword ptr [rip + 0xc6780c]
0028DA34  E9 E8 F9 FF FF                  jmp 0x14028d421
0028DA39  41 0F BA E5 1C                  bt r13d, 0x1c
0028DA3E  0F 82 51 F8 FF FF               jb 0x14028d295
0028DA44  FF 05 3E 78 C6 00               inc dword ptr [rip + 0xc6783e]
0028DA4A  E9 20 F9 FF FF                  jmp 0x14028d36f
0028DA4F  48 81 FA 00 02 00 00            cmp rdx, 0x200
0028DA56  0F 82 B5 FC FF FF               jb 0x14028d711
0028DA5C  E9 0E F9 FF FF                  jmp 0x14028d36f
0028DA61  48 83 FA 10                     cmp rdx, 0x10
0028DA65  0F 85 B1 FC FF FF               jne 0x14028d71c
0028DA6B  E9 FF F8 FF FF                  jmp 0x14028d36f
0028DA70  41 83 F8 06                     cmp r8d, 6
0028DA74  75 31                           jne 0x14028daa7
0028DA76  F6 C1 10                        test cl, 0x10
0028DA79  75 2C                           jne 0x14028daa7
0028DA7B  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
0028DA7E  66 83 F8 01                     cmp ax, 1
0028DA82  75 23                           jne 0x14028daa7
0028DA84  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
0028DA88  48 C1 E8 3C                     shr rax, 0x3c
0028DA8C  24 07                           and al, 7
0028DA8E  3C 02                           cmp al, 2
0028DA90  74 15                           je 0x14028daa7
0028DA92  48 8B 06                        mov rax, qword ptr [rsi]
0028DA95  A8 01                           test al, 1
0028DA97  74 0E                           je 0x14028daa7
0028DA99  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
0028DA9C  C1 E8 18                        shr eax, 0x18
0028DA9F  A8 08                           test al, 8
0028DAA1  0F 84 10 F8 FF FF               je 0x14028d2b7
0028DAA7  FF 05 D7 77 C6 00               inc dword ptr [rip + 0xc677d7]
0028DAAD  E9 BD F8 FF FF                  jmp 0x14028d36f
0028DAB2  48 8B CE                        mov rcx, rsi
0028DAB5  E8 5E 35 02 00                  call 0x1402b1018
0028DABA  85 C0                           test eax, eax
0028DABC  0F 84 30 FA FF FF               je 0x14028d4f2
0028DAC2  FF 05 C8 77 C6 00               inc dword ptr [rip + 0xc677c8]
0028DAC8  E9 A2 F8 FF FF                  jmp 0x14028d36f
0028DACD  48 8B CE                        mov rcx, rsi
0028DAD0  E8 43 35 02 00                  call 0x1402b1018
0028DAD5  85 C0                           test eax, eax
0028DAD7  0F 84 E5 F7 FF FF               je 0x14028d2c2
0028DADD  EB E3                           jmp 0x14028dac2
0028DADF  FF 05 83 77 C6 00               inc dword ptr [rip + 0xc67783]
0028DAE5  E9 85 F8 FF FF                  jmp 0x14028d36f
0028DAEA  FF 05 6C 77 C6 00               inc dword ptr [rip + 0xc6776c]
0028DAF0  E9 7A F8 FF FF                  jmp 0x14028d36f
0028DAF5  FF 05 79 77 C6 00               inc dword ptr [rip + 0xc67779]
0028DAFB  E9 6F F8 FF FF                  jmp 0x14028d36f
0028DB00  48 8B CE                        mov rcx, rsi
0028DB03  E8 D0 F2 1B 00                  call 0x14044cdd8
0028DB08  FF 05 62 77 C6 00               inc dword ptr [rip + 0xc67762]
0028DB0E  E9 5C F8 FF FF                  jmp 0x14028d36f
0028DB13  FF 05 2F 77 C6 00               inc dword ptr [rip + 0xc6772f]
0028DB19  E9 51 F8 FF FF                  jmp 0x14028d36f
0028DB1E  41 81 E5 00 00 41 00            and r13d, 0x410000
0028DB25  41 81 FD 00 00 41 00            cmp r13d, 0x410000
0028DB2C  74 25                           je 0x14028db53
0028DB2E  48 8B D3                        mov rdx, rbx
0028DB31  48 8D 0D C8 B1 BA 00            lea rcx, [rip + 0xbab1c8]
0028DB38  E8 E3 7E 18 00                  call 0x140415a20
0028DB3D  83 F8 03                        cmp eax, 3
0028DB40  74 11                           je 0x14028db53
0028DB42  8B C0                           mov eax, eax
0028DB44  48 8D 0D 15 41 D8 FF            lea rcx, [rip - 0x27beeb]
0028DB4B  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
0028DB4F  49 89 46 28                     mov qword ptr [r14 + 0x28], rax
0028DB53  FF 05 F7 76 C6 00               inc dword ptr [rip + 0xc676f7]
0028DB59  E9 11 F8 FF FF                  jmp 0x14028d36f
0028DB5E  44 8B 94 24 C0 00 00 00         mov r10d, dword ptr [rsp + 0xc0]
0028DB66  E9 E1 F6 FF FF                  jmp 0x14028d24c
0028DB6B  FF 05 23 77 C6 00               inc dword ptr [rip + 0xc67723]
0028DB71  E9 F9 F7 FF FF                  jmp 0x14028d36f
0028DB76  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0028DB7A  48 85 C0                        test rax, rax
0028DB7D  0F 84 64 F9 FF FF               je 0x14028d4e7
0028DB83  FF 05 03 77 C6 00               inc dword ptr [rip + 0xc67703]
0028DB89  E9 E1 F7 FF FF                  jmp 0x14028d36f
0028DB8E  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
0028DB96  E9 34 F6 FF FF                  jmp 0x14028d1cf
0028DB9B  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
0028DBA3  E9 27 F6 FF FF                  jmp 0x14028d1cf
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiTradePage(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p8;
    unsigned int v_stack_pC0;
    unsigned __int64 v_stack_pC8;
    unsigned int v_stack_pD8;

    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (120);
    v_rbp = 0;
    v_stack_m88 = 0;
    *(unsigned __int64 *)(a1 + 40) = 0;
    v_stack_m80 = *(unsigned __int64 *)(a1);
    if (condition_is_below) goto loc_0028D9B1;
loc_0028D1A3:
    v_stack_m70 = 0;
    v_rsi = (a2 + a2 * 2) << (4);
    v_stack_m68 = 1;
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(a1));
loc_0028D1CF:
    a1 = -1;
    if ((*(unsigned __int64 *)(a1 + 32)) != -1) { a1 = *(unsigned __int64 *)(a1 + 32); }
    v_stack_m78 = a1;
    result = MiSafeLockPage(a2, a2, a3, a4);
    if (((unsigned __int8)(result)) == 17) goto loc_0028D9CF;
    result = (*(unsigned __int64 *)(v_rsi + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12201607) + result * 8)) != v_stack_m80) goto loc_0028DB1E;
    a3 = (unsigned int)((*(unsigned __int8 *)(v_rsi + 34)) & (7));
    v_stack_p8 = 3;
    v_stack_p20 = (unsigned int)(a3);
    if (condition_is_below) goto loc_0028D8DE;
loc_0028D24C:
    if (((unsigned int)(a3)) == 5) goto loc_0028D571;
loc_0028D256:
    if (((unsigned int)(a3)) < 5) goto loc_0028DB13;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24))))) & (0x410000ULL));
    if (((unsigned int)(result)) == 0x410000ULL) goto loc_0028D282;
    result = MiGetPfnSlabType(v_rsi, 0, a3, a4);
    if (((unsigned int)(result)) != 9) goto loc_0028D685;
loc_0028D282:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsi + 32))))) >> (16));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (64)) != 0) goto loc_0028DA39;
loc_0028D295:
    if (((unsigned int)(a3)) <= 1) goto loc_0028D317;
    if (sign_flag) goto loc_0028D875;
    if (((unsigned int)(a3)) <= 4) goto loc_0028D4C8;
    if (((unsigned int)(a3)) != 6) goto loc_0028D9C4;
loc_0028D2B7:
    if (((unsigned int)(a3)) < 6) goto loc_0028DACD;
loc_0028D2C2:
    result = (*(unsigned __int64 *)(v_rsi + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) == 2) goto loc_0028D690;
    v_stack_m90 = v_stack_p18;
    v_stack_m98 = 1;
    result = MiActivePageClaimCandidate(v_stack_m80, v_rsi, 1, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    if (result == 0) goto loc_0028D3AB;
    *(unsigned __int64 *)(a1 + 40) = result;
    goto loc_0028D36F;
loc_0028D317:
    if (3 != 3) goto loc_0028D6F0;
    if (3 < 3) goto loc_0028D348;
    a2 = 0;
    result = MiUnlinkFreeOrZeroedPage(v_stack_p10, a2, 256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    if ((unsigned int)(result) == 0) goto loc_0028D9B9;
loc_0028D348:
    if (!(condition_is_below)) {
        a2 = v_stack_p10;
        a1 = a1;
        result = MiAddMdlPageToTradeBlock(a1, a2, 256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    }
    if (((unsigned __int8)((unsigned __int8)(result))) == 17) goto loc_0028D4AF;
loc_0028D36F:
    if (((unsigned __int8)((unsigned __int8)(result))) >= 2) goto loc_0028D4AF;
    if ((*(unsigned int *)(v_rip + 13867409)) != 0) {
        a1 = v_cr8;
        a2 = (unsigned __int8)((unsigned __int8)(result));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, 256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    }
    goto loc_0028D4AF;
loc_0028D3AB:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 24)))) & (8)) != 0) goto loc_0028DB6B;
    if (sign_flag) goto loc_0028D55C;
    v_stack_m90 = v_stack_m78;
    v_stack_m98 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 28)));
    result = MiStealPage(v_rsi, (unsigned __int8)((unsigned __int8)(result)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))), *(unsigned __int64 *)(a1 + 8));
loc_0028D3E7:
    if (((unsigned int)(result)) == 2) goto loc_0028DB9B;
    if ((unsigned int)(result) == 0) goto loc_0028D566;
    result = (*(unsigned __int64 *)(v_rsi + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12201093) + result * 8)) != v_stack_p10) goto loc_0028D8B5;
loc_0028D421:
    *(unsigned __int64 *)(v_rsi + 16) = *(unsigned __int64 *)(v_rip - 2608040);
    result = MiSetOriginalPtePfnFromFreeList(v_rsi + 16, (unsigned __int8)((unsigned __int8)(result)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))), *(unsigned __int64 *)(a1 + 8));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12201093) + result * 8)) < v_stack_p10) goto loc_0028D54F;
    a3 = ((unsigned int)(*(unsigned int *)(v_rip + 13900854))) << (59);
    a2 = (a3) ^ (*(unsigned __int64 *)(v_rsi + 24));
    a2 = (a2) & (*(unsigned __int64 *)(a1 + 8));
    a2 = (a2) ^ (a3);
    if ((*(unsigned __int64 *)(v_rsi + 24)) == (*(unsigned __int64 *)(v_rsi + 24))) goto loc_0028D49D;
loc_0028D480:
    a2 = (*(unsigned __int64 *)(v_rsi + 24)) ^ (a3);
    a2 = (a2) & (*(unsigned __int64 *)(a1 + 8));
    a2 = (a2) ^ (a3);
    if ((*(unsigned __int64 *)(v_rsi + 24)) != (*(unsigned __int64 *)(v_rsi + 24))) goto loc_0028D480;
loc_0028D49D:
    if (*(unsigned __int64 *)(a1 + 56) != 0) goto loc_0028D658;
loc_0028D4AA:
loc_0028D4AF:
    *(unsigned __int64 *)(a1 + 32) = v_stack_m78;
    v_rsp = (v_rsp) + (120);
    return 1;
loc_0028D4C8:
    if (condition_is_below) goto loc_0028D4E7;
    if (condition_is_below) goto loc_0028D4E7;
    if (!sign_flag) goto loc_0028DB76;
loc_0028D4E7:
    if (condition_is_below) goto loc_0028DAB2;
loc_0028D4F2:
    v_stack_p20 = v_stack_p40;
    result = MiTradeTransitionPage(v_rsi, (unsigned __int8)((unsigned __int8)(result)), 0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    if (((unsigned int)(result)) == 2) goto loc_0028D678;
    if (((unsigned int)(result)) != 3) goto loc_0028D4AF;
    result = (*(unsigned __int64 *)(v_rsi + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12200801) + result * 8)) != v_stack_p38) goto loc_0028D8B5;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12200801) + result * 8)) >= v_stack_p38) goto loc_0028D49D;
loc_0028D54F:
    result = MiLockAndInsertPageInFreeList(v_rsi, v_stack_p38, 0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    goto loc_0028D4AA;
loc_0028D55C:
    result = MiTrimSharedPage(v_rsi, v_stack_p38, 0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    goto loc_0028D3E7;
loc_0028D566:
    goto loc_0028D4AF;
loc_0028D571:
    result = MiIsPageOnBadList(v_rsi, v_stack_p38, 0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    if ((unsigned int)(result) != 0) goto loc_0028DAEA;
    if ((*(unsigned __int64 *)(v_rsi + 8)) == -8) goto loc_0028D9A6;
    result = *(unsigned __int64 *)(v_rsi + 8);
    v_rbx = v_stack_p10;
    v_r10 = 3;
    if (3 == 3) {
        a1 = v_stack_pC8;
        result = MI_PAGE_TO_FULL_COLOR(a1, v_stack_p38, 0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
        a2 = *(unsigned __int64 *)(v_rsi + 16);
        v_rbx = (unsigned int)(result);
        a3 = v_stack_pD8;
        v_r10 = v_stack_pC0;
    }
    result = MiColorHasSlists((unsigned int)((unsigned int)(v_rbx)), a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    if ((unsigned int)(result) == 0) goto loc_0028D760;
    result = MiInvalidPteConforms(a2, a2, a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    if ((unsigned int)(result) == 0) goto loc_0028D8D3;
    if (*(unsigned __int64 *)(v_rip + 12191394) == 0) goto loc_0028D5F4;
    result = a2;
    if ((((unsigned __int8)(a2)) & (16)) == 0) {
        result = *(unsigned __int64 *)(v_rip + 12191394);
        result = ~(result);
        result = (result) & (a2);
    }
    result = (result) >> (32);
    if (result != ((unsigned int)(0xFFFFFFFEULL))) goto loc_0028D8D3;
    if (v_stack_p48 == v_rsi) goto loc_0028D987;
loc_0028D611:
    v_stack_p48 = v_rsi;
    result = (a2) >> (12);
    result = (unsigned int)((result) & (15));
    v_stack_p50 = result;
    result = MiUnlockPage(v_rsi, (unsigned __int8)((unsigned __int8)(result)), a3, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    result = MiDrainZeroLookasides(v_stack_p38, v_rsi, *(unsigned __int64 *)(a1 + 16), (unsigned int)((unsigned int)(v_rbx)));
    goto loc_0028D1CF;
loc_0028D658:
    result = ((unsigned int)(*(unsigned int *)(v_stack_p38 + 40))) >> (12);
    *(unsigned __int64 *)(v_stack_p38 + result * 8 + 48) = v_stack_pC8;
    goto loc_0028D4AA;
loc_0028D678:
    goto loc_0028D1CF;
loc_0028D685:
    goto loc_0028D36F;
loc_0028D690:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 24)))) & (8)) != 0) goto loc_0028DB6B;
    result = MiUnlockPage(v_rsi, (unsigned __int8)((unsigned __int8)(result)), *(unsigned __int64 *)(a1 + 16), (unsigned int)((unsigned int)(v_rbx)));
    v_stack_p28 = v_stack_p30;
    v_stack_p20 = v_stack_p40;
    result = MiSwapStackPage(v_stack_p38, v_rsi, (unsigned int)(*(unsigned int *)(a1 + 28)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    if ((unsigned int)(result) == 0) goto loc_0028D854;
    if (v_stack_p30 == 1) goto loc_0028DA2E;
    goto loc_0028D421;
loc_0028D6F0:
    v_stack_pC0 = *(unsigned __int64 *)(v_rip - 2603674 + (unsigned int)((unsigned int)(v_r10)) * 8);
    if (v_stack_p30 < 1) goto loc_0028DA4F;
loc_0028D711:
    if (v_stack_p30 < 1) goto loc_0028DA61;
loc_0028D71C:
    result = ~(*(unsigned __int64 *)(v_rip - 2603674 + (unsigned int)((unsigned int)(v_r10)) * 8) - 1);
    result = (result) & (v_stack_pC8);
    a1 = (result == v_stack_pC8) ? 1 : 0;
    result = (result >= v_stack_pC8) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_0028D9DA;
loc_0028D744:
    result = MiDemoteLargeFreePage(v_stack_pC8, (unsigned __int8)((unsigned __int8)(result)), (unsigned int)(*(unsigned int *)(a1 + 28)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    if ((unsigned int)(result) == 0) goto loc_0028D1CF;
    goto loc_0028D348;
loc_0028D760:
    if (((unsigned int)(v_r10)) == 3) goto loc_0028D256;
    if (((unsigned int)(v_r10)) >= 3) goto loc_0028D77B;
    if (((unsigned int)(v_r10)) <= 1) goto loc_0028D36F;
loc_0028D77B:
    if (((unsigned int)(v_r10)) >= 1) goto loc_0028D78C;
    if (((unsigned int)(v_r10)) == 2) goto loc_0028D36F;
loc_0028D78C:
    result = MI_NODE_FROM_PFN(v_rsi, (unsigned __int8)((unsigned __int8)(result)), (unsigned int)(*(unsigned int *)(a1 + 28)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    a1 = ((unsigned int)((unsigned int)(result))) * ((unsigned int)((unsigned int)(result)));
    a1 = (a1) + (*(unsigned __int64 *)(v_stack_p38 + 16));
    v_stack_p58 = a1;
    result = MiSnapPageMoveInProgress(a1, 2, (unsigned int)(*(unsigned int *)(a1 + 28)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    v_stack_p60 = result;
    result = MiSnapPageMoveInProgress(a1, 1, (unsigned int)(*(unsigned int *)(a1 + 28)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    v_stack_p68 = result;
    result = MiUnlockPage(v_rsi, 17, (unsigned int)(*(unsigned int *)(a1 + 28)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    v_stack_pD8 = v_stack_p60;
loc_0028D7E5:
    result = (unsigned int)(-(1));
    a2 = (unsigned int)((17) + (2));
    result = MiWaitForPageMoveComplete(v_stack_p58, a2, (unsigned int)(*(unsigned int *)(a1 + 28)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    result = (result) ^ (*(unsigned __int64 *)(v_stack_p60));
    if (((result) & (0xFFFFFFFFFFFF0000ULL)) != 0) goto loc_0028D1CF;
    v_r15 = (unsigned int)((1) + 1);
    v_rbx = (v_stack_pD8) + (8);
    v_stack_pD8 = v_rbx;
    if (((unsigned int)(v_r15)) < 2) goto loc_0028D7E5;
    if (((unsigned int)(v_r15)) != 2) goto loc_0028DB8E;
    *(unsigned __int64 *)(a1 + 40) = *(unsigned __int64 *)(v_rip - 2604001 + (unsigned int)(v_stack_pC0) * 8);
    goto loc_0028D4AF;
loc_0028D854:
    result = (*(unsigned __int64 *)(v_rsi + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) == 2) goto loc_0028D8C8;
    goto loc_0028D1CF;
loc_0028D875:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 28)))) != 2) goto loc_0028DA70;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsi + 32))) != 0) goto loc_0028DAF5;
    result = MiReuseStandbyPage(v_rsi, a2, (unsigned int)(*(unsigned int *)(a1 + 28)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    if ((unsigned int)(result) == 0) goto loc_0028DB00;
    result = MiAddMdlPageToTradeBlock(a1, v_stack_pC8, (unsigned int)(*(unsigned int *)(a1 + 28)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    goto loc_0028D36F;
loc_0028D8B5:
    result = MiLockAndInsertPageInFreeList(v_rsi, v_stack_pC8, (unsigned int)(*(unsigned int *)(a1 + 28)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    goto loc_0028D4AF;
loc_0028D8C8:
    goto loc_0028D4AF;
loc_0028D8D3:
    goto loc_0028D36F;
loc_0028D8DE:
    result = MiGetBaseResidentPage(v_rsi, v_stack_pC8, (unsigned int)(*(unsigned int *)(a1 + 28)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    v_stack_p58 = result;
    result = (unsigned int)((*(unsigned __int8 *)(result + 34)) & (7));
    v_stack_pD8 = (unsigned int)(result);
    result = MiGetPfnPageSizeIndex(result, v_stack_pC8, (unsigned int)(*(unsigned int *)(a1 + 28)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    v_stack_pC0 = (unsigned int)(result);
    a1 = (result) - (result);
    a1 = (a1) >> (4);
    a1 = (a1) * (result);
    result = MI_PAGE_TO_FULL_COLOR(a1, v_stack_pC8, (unsigned int)(*(unsigned int *)(a1 + 28)), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    if (v_stack_p58 != v_rsi) {
    }
    if (((unsigned int)((unsigned int)(v_stack_pD8))) != 6) goto loc_0028DB5E;
    *(unsigned __int64 *)(a1 + 40) = *(unsigned __int64 *)(v_rip - 2604308 + (unsigned int)(v_stack_pC0) * 8);
    goto loc_0028D36F;
loc_0028D987:
    result = (*(unsigned __int64 *)(v_stack_p58 + 16)) >> (12);
    result = (unsigned int)((result) & (15));
    if (v_stack_p50 == ((unsigned int)(result))) goto loc_0028DADF;
    goto loc_0028D611;
loc_0028D9A6:
    goto loc_0028D36F;
loc_0028D9B1:
    goto loc_0028D1A3;
loc_0028D9B9:
    goto loc_0028D36F;
loc_0028D9C4:
    goto loc_0028D36F;
loc_0028D9CF:
    goto loc_0028D4AF;
loc_0028D9DA:
    if ((*(unsigned __int64 *)(a1 + 16)) < (*(unsigned __int64 *)(v_stack_p58 + 16))) goto loc_0028D744;
    result = ((unsigned int)((unsigned int)(result)) - 1) + (*(unsigned __int64 *)(v_stack_p58 + 16));
    if (result > (*(unsigned __int64 *)(a1 + 48))) goto loc_0028D744;
    if (result < (*(unsigned __int64 *)(a1 + 48))) goto loc_0028D744;
    v_stack_p20 = (unsigned __int8)(v_r15);
    result = MiLargeFreePageToMdl((unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_r10)), *(unsigned __int64 *)(a1 + 56), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    goto loc_0028D4AF;
loc_0028DA2E:
    goto loc_0028D421;
loc_0028DA39:
    if (result < (*(unsigned __int64 *)(a1 + 48))) goto loc_0028D295;
    goto loc_0028D36F;
loc_0028DA4F:
    if (((unsigned int)((unsigned int)(v_r10))) < 512) goto loc_0028D711;
    goto loc_0028D36F;
loc_0028DA61:
    if (((unsigned int)((unsigned int)(v_r10))) != 16) goto loc_0028D71C;
    goto loc_0028D36F;
loc_0028DA70:
    if (((unsigned int)(*(unsigned __int64 *)(a1 + 56))) != 6) goto loc_0028DAA7;
    if ((((unsigned __int8)((unsigned int)((unsigned int)(result)))) & (16)) != 0) goto loc_0028DAA7;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsi + 32)))) != 1) goto loc_0028DAA7;
    result = (*(unsigned __int64 *)(v_rsi + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) == 2) goto loc_0028DAA7;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rsi))) & (1)) == 0) goto loc_0028DAA7;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsi + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (8)) == 0) goto loc_0028D2B7;
loc_0028DAA7:
    goto loc_0028D36F;
loc_0028DAB2:
    result = MiIsPageOnBadList(v_rsi, (unsigned int)((unsigned int)(v_r10)), *(unsigned __int64 *)(a1 + 56), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    if ((unsigned int)(result) == 0) goto loc_0028D4F2;
loc_0028DAC2:
    goto loc_0028D36F;
loc_0028DACD:
    result = MiIsPageOnBadList(v_rsi, (unsigned int)((unsigned int)(v_r10)), *(unsigned __int64 *)(a1 + 56), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    if ((unsigned int)(result) == 0) goto loc_0028D2C2;
    goto loc_0028DAC2;
loc_0028DADF:
    goto loc_0028D36F;
loc_0028DAEA:
    goto loc_0028D36F;
loc_0028DAF5:
    goto loc_0028D36F;
loc_0028DB00:
    result = MiReleaseFreshPageLocked(v_rsi, (unsigned int)((unsigned int)(v_r10)), *(unsigned __int64 *)(a1 + 56), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    goto loc_0028D36F;
loc_0028DB13:
    goto loc_0028D36F;
loc_0028DB1E:
    v_r13 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 24))) & (0x410000ULL));
    if (((unsigned int)(v_r13)) == 0x410000ULL) goto loc_0028DB53;
    result = MiPfnLargeBitSet(v_rip + 12235208, (unsigned int)((unsigned int)(result)), *(unsigned __int64 *)(a1 + 56), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    if (((unsigned int)(result)) != 3) {
        result = (unsigned int)(result);
        a1 = v_rip - 2604779;
        result = *(unsigned __int64 *)(a1 + result * 8);
        *(unsigned __int64 *)(a1 + 40) = result;
    }
    goto loc_0028D36F;
loc_0028DB5E:
    goto loc_0028D24C;
loc_0028DB6B:
    goto loc_0028D36F;
loc_0028DB76:
    if (*(unsigned __int64 *)(v_rsi + 8) == 0) goto loc_0028D4E7;
    goto loc_0028D36F;
loc_0028DB8E:
    goto loc_0028D1CF;
loc_0028DB9B:
    goto loc_0028D1CF;
}
```

## 5. (Beta) C Style

```c
int64_t MiTradePage(void *Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint32_t v_stack_mB8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint32_t v_stack_p8;
    uint32_t v_stack_pC0;
    uint64_t v_stack_pC8;
    uint32_t v_stack_pD8;

    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (120);
    local_rbp = 0;
    v_stack_m88 = 0;
    *(uint64_t *)(arg1 + 0x28) = 0;
    v_stack_m80 = *(uint64_t *)(arg1);
    if (condition_is_below) goto loc_0028D9B1;
loc_0028D1A3:
    v_stack_m70 = 0;
    local_rsi = (Arg2 + Arg2 * 2) << (4);
    v_stack_m68 = 1;
    local_rsi = (local_rsi) + (*(uint64_t *)(arg1));
loc_0028D1CF:
    Arg1 = -1;
    if ((*(uint64_t *)(arg1 + 0x20)) != -1) { Arg1 = *(uint64_t *)(arg1 + 0x20); }
    v_stack_m78 = Arg1;
    result = MiSafeLockPage(Arg2, Arg2, Arg3, a4);
    if (((uint8_t)(result)) == 17) goto loc_0028D9CF;
    result = (*(uint64_t *)(local_rsi + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA2E87) + result * 8)) != v_stack_m80) goto loc_0028DB1E;
    Arg3 = (uint32_t)((*(uint8_t *)(local_rsi + 0x22)) & (7));
    v_stack_p8 = 3;
    v_stack_p20 = (uint32_t)(Arg3);
    if (condition_is_below) goto loc_0028D8DE;
loc_0028D24C:
    if (((uint32_t)(Arg3)) == 5) goto loc_0028D571;
loc_0028D256:
    if (((uint32_t)(Arg3)) < 5) goto loc_0028DB13;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18))))) & (0x410000ULL));
    if (((uint32_t)(result)) == 0x410000ULL) goto loc_0028D282;
    result = MiGetPfnSlabType(local_rsi, 0, Arg3, a4);
    if (((uint32_t)(result)) != 9) goto loc_0028D685;
loc_0028D282:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x20))))) >> (16));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (64)) != 0) goto loc_0028DA39;
loc_0028D295:
    if (((uint32_t)(Arg3)) <= 1) goto loc_0028D317;
    if (sign_flag) goto loc_0028D875;
    if (((uint32_t)(Arg3)) <= 4) goto loc_0028D4C8;
    if (((uint32_t)(Arg3)) != 6) goto loc_0028D9C4;
loc_0028D2B7:
    if (((uint32_t)(Arg3)) < 6) goto loc_0028DACD;
loc_0028D2C2:
    result = (*(uint64_t *)(local_rsi + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) == 2) goto loc_0028D690;
    v_stack_m90 = v_stack_p18;
    v_stack_m98 = 1;
    result = MiActivePageClaimCandidate(v_stack_m80, local_rsi, 1, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    if (result == 0) goto loc_0028D3AB;
    *(uint64_t *)(arg1 + 0x28) = result;
    goto loc_0028D36F;
loc_0028D317:
    if (3 != 3) goto loc_0028D6F0;
    if (3 < 3) goto loc_0028D348;
    Arg2 = 0;
    result = MiUnlinkFreeOrZeroedPage(v_stack_p10, Arg2, 256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    if ((uint32_t)(result) == 0) goto loc_0028D9B9;
loc_0028D348:
    if (!(condition_is_below)) {
        Arg2 = v_stack_p10;
        Arg1 = Arg1;
        result = MiAddMdlPageToTradeBlock(Arg1, Arg2, 256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    }
    if (((uint8_t)((uint8_t)(result))) == 17) goto loc_0028D4AF;
loc_0028D36F:
    if (((uint8_t)((uint8_t)(result))) >= 2) goto loc_0028D4AF;
    if ((*(uint32_t *)(v_rip + 0xD39991)) != 0) {
        Arg1 = v_cr8;
        Arg2 = (uint8_t)((uint8_t)(result));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, 256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    }
    goto loc_0028D4AF;
loc_0028D3AB:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))) & (8)) != 0) goto loc_0028DB6B;
    if (sign_flag) goto loc_0028D55C;
    v_stack_m90 = v_stack_m78;
    v_stack_m98 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C)));
    result = MiStealPage(local_rsi, (uint8_t)((uint8_t)(result)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))), *(uint64_t *)(arg1 + 0x8));
loc_0028D3E7:
    if (((uint32_t)(result)) == 2) goto loc_0028DB9B;
    if ((uint32_t)(result) == 0) goto loc_0028D566;
    result = (*(uint64_t *)(local_rsi + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA2C85) + result * 8)) != v_stack_p10) goto loc_0028D8B5;
loc_0028D421:
    *(uint64_t *)(local_rsi + 0x10) = *(uint64_t *)(v_rip - 0x27CBA8);
    result = MiSetOriginalPtePfnFromFreeList(local_rsi + 16, (uint8_t)((uint8_t)(result)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))), *(uint64_t *)(arg1 + 0x8));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA2C85) + result * 8)) < v_stack_p10) goto loc_0028D54F;
    Arg3 = ((uint32_t)(*(uint32_t *)(v_rip + 0xD41C36))) << (59);
    Arg2 = (Arg3) ^ (*(uint64_t *)(local_rsi + 0x18));
    Arg2 = (Arg2) & (*(uint64_t *)(arg1 + 0x8));
    Arg2 = (Arg2) ^ (Arg3);
    if ((*(uint64_t *)(local_rsi + 0x18)) == (*(uint64_t *)(local_rsi + 0x18))) goto loc_0028D49D;
loc_0028D480:
    Arg2 = (*(uint64_t *)(local_rsi + 0x18)) ^ (Arg3);
    Arg2 = (Arg2) & (*(uint64_t *)(arg1 + 0x8));
    Arg2 = (Arg2) ^ (Arg3);
    if ((*(uint64_t *)(local_rsi + 0x18)) != (*(uint64_t *)(local_rsi + 0x18))) goto loc_0028D480;
loc_0028D49D:
    if (*(uint64_t *)(arg1 + 0x38) != 0) goto loc_0028D658;
loc_0028D4AA:
loc_0028D4AF:
    *(uint64_t *)(arg1 + 0x20) = v_stack_m78;
    local_rsp = (local_rsp) + (120);
    return 1;
loc_0028D4C8:
    if (condition_is_below) goto loc_0028D4E7;
    if (condition_is_below) goto loc_0028D4E7;
    if (!sign_flag) goto loc_0028DB76;
loc_0028D4E7:
    if (condition_is_below) goto loc_0028DAB2;
loc_0028D4F2:
    v_stack_p20 = v_stack_p40;
    result = MiTradeTransitionPage(local_rsi, (uint8_t)((uint8_t)(result)), 0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    if (((uint32_t)(result)) == 2) goto loc_0028D678;
    if (((uint32_t)(result)) != 3) goto loc_0028D4AF;
    result = (*(uint64_t *)(local_rsi + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA2B61) + result * 8)) != v_stack_p38) goto loc_0028D8B5;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA2B61) + result * 8)) >= v_stack_p38) goto loc_0028D49D;
loc_0028D54F:
    result = MiLockAndInsertPageInFreeList(local_rsi, v_stack_p38, 0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    goto loc_0028D4AA;
loc_0028D55C:
    result = MiTrimSharedPage(local_rsi, v_stack_p38, 0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    goto loc_0028D3E7;
loc_0028D566:
    goto loc_0028D4AF;
loc_0028D571:
    result = MiIsPageOnBadList(local_rsi, v_stack_p38, 0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    if ((uint32_t)(result) != 0) goto loc_0028DAEA;
    if ((*(uint64_t *)(local_rsi + 0x8)) == -8) goto loc_0028D9A6;
    result = *(uint64_t *)(local_rsi + 0x8);
    local_rbx = v_stack_p10;
    local_r10 = 3;
    if (3 == 3) {
        Arg1 = v_stack_pC8;
        result = MI_PAGE_TO_FULL_COLOR(Arg1, v_stack_p38, 0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
        Arg2 = *(uint64_t *)(local_rsi + 0x10);
        local_rbx = (uint32_t)(result);
        Arg3 = v_stack_pD8;
        local_r10 = v_stack_pC0;
    }
    result = MiColorHasSlists((uint32_t)((uint32_t)(local_rbx)), Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    if ((uint32_t)(result) == 0) goto loc_0028D760;
    result = MiInvalidPteConforms(Arg2, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    if ((uint32_t)(result) == 0) goto loc_0028D8D3;
    if (*(uint64_t *)(v_rip + 0xBA06A2) == 0) goto loc_0028D5F4;
    result = Arg2;
    if ((((uint8_t)(Arg2)) & (16)) == 0) {
        result = *(uint64_t *)(v_rip + 0xBA06A2);
        result = ~(result);
        result = (result) & (Arg2);
    }
    result = (result) >> (32);
    if (result != ((uint32_t)(0xFFFFFFFEULL))) goto loc_0028D8D3;
    if (v_stack_p48 == local_rsi) goto loc_0028D987;
loc_0028D611:
    v_stack_p48 = local_rsi;
    result = (Arg2) >> (12);
    result = (uint32_t)((result) & (15));
    v_stack_p50 = result;
    result = MiUnlockPage(local_rsi, (uint8_t)((uint8_t)(result)), Arg3, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    result = MiDrainZeroLookasides(v_stack_p38, local_rsi, *(uint64_t *)(arg1 + 0x10), (uint32_t)((uint32_t)(local_rbx)));
    goto loc_0028D1CF;
loc_0028D658:
    result = ((uint32_t)(*(uint32_t *)(v_stack_p38 + 0x28))) >> (12);
    *(uint64_t *)(v_stack_p38 + result * 8 + 0x30) = v_stack_pC8;
    goto loc_0028D4AA;
loc_0028D678:
    goto loc_0028D1CF;
loc_0028D685:
    goto loc_0028D36F;
loc_0028D690:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))) & (8)) != 0) goto loc_0028DB6B;
    result = MiUnlockPage(local_rsi, (uint8_t)((uint8_t)(result)), *(uint64_t *)(arg1 + 0x10), (uint32_t)((uint32_t)(local_rbx)));
    v_stack_p28 = v_stack_p30;
    v_stack_p20 = v_stack_p40;
    result = MiSwapStackPage(v_stack_p38, local_rsi, (uint32_t)(*(uint32_t *)(arg1 + 0x1C)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    if ((uint32_t)(result) == 0) goto loc_0028D854;
    if (v_stack_p30 == 1) goto loc_0028DA2E;
    goto loc_0028D421;
loc_0028D6F0:
    v_stack_pC0 = *(uint64_t *)(v_rip - 0x27BA9A + (uint32_t)((uint32_t)(local_r10)) * 8);
    if (v_stack_p30 < 1) goto loc_0028DA4F;
loc_0028D711:
    if (v_stack_p30 < 1) goto loc_0028DA61;
loc_0028D71C:
    result = ~(*(uint64_t *)(v_rip - 0x27BA9A + (uint32_t)((uint32_t)(local_r10)) * 8) - 1);
    result = (result) & (v_stack_pC8);
    Arg1 = (result == v_stack_pC8) ? 1 : 0;
    result = (result >= v_stack_pC8) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_0028D9DA;
loc_0028D744:
    result = MiDemoteLargeFreePage(v_stack_pC8, (uint8_t)((uint8_t)(result)), (uint32_t)(*(uint32_t *)(arg1 + 0x1C)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    if ((uint32_t)(result) == 0) goto loc_0028D1CF;
    goto loc_0028D348;
loc_0028D760:
    if (((uint32_t)(local_r10)) == 3) goto loc_0028D256;
    if (((uint32_t)(local_r10)) >= 3) goto loc_0028D77B;
    if (((uint32_t)(local_r10)) <= 1) goto loc_0028D36F;
loc_0028D77B:
    if (((uint32_t)(local_r10)) >= 1) goto loc_0028D78C;
    if (((uint32_t)(local_r10)) == 2) goto loc_0028D36F;
loc_0028D78C:
    result = MI_NODE_FROM_PFN(local_rsi, (uint8_t)((uint8_t)(result)), (uint32_t)(*(uint32_t *)(arg1 + 0x1C)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    Arg1 = ((uint32_t)((uint32_t)(result))) * ((uint32_t)((uint32_t)(result)));
    Arg1 = (Arg1) + (*(uint64_t *)(v_stack_p38 + 0x10));
    v_stack_p58 = Arg1;
    result = MiSnapPageMoveInProgress(Arg1, 2, (uint32_t)(*(uint32_t *)(arg1 + 0x1C)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    v_stack_p60 = result;
    result = MiSnapPageMoveInProgress(Arg1, 1, (uint32_t)(*(uint32_t *)(arg1 + 0x1C)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    v_stack_p68 = result;
    result = MiUnlockPage(local_rsi, 17, (uint32_t)(*(uint32_t *)(arg1 + 0x1C)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    v_stack_pD8 = v_stack_p60;
loc_0028D7E5:
    result = (uint32_t)(-(1));
    Arg2 = (uint32_t)((17) + (2));
    result = MiWaitForPageMoveComplete(v_stack_p58, Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x1C)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    result = (result) ^ (*(uint64_t *)(v_stack_p60));
    if (((result) & (0xFFFFFFFFFFFF0000ULL)) != 0) goto loc_0028D1CF;
    local_r15 = (uint32_t)((1) + 1);
    local_rbx = (v_stack_pD8) + (8);
    v_stack_pD8 = local_rbx;
    if (((uint32_t)(local_r15)) < 2) goto loc_0028D7E5;
    if (((uint32_t)(local_r15)) != 2) goto loc_0028DB8E;
    *(uint64_t *)(arg1 + 0x28) = *(uint64_t *)(v_rip - 0x27BBE1 + (uint32_t)(v_stack_pC0) * 8);
    goto loc_0028D4AF;
loc_0028D854:
    result = (*(uint64_t *)(local_rsi + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) == 2) goto loc_0028D8C8;
    goto loc_0028D1CF;
loc_0028D875:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x1C)))) != 2) goto loc_0028DA70;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x20))) != 0) goto loc_0028DAF5;
    result = MiReuseStandbyPage(local_rsi, Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x1C)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    if ((uint32_t)(result) == 0) goto loc_0028DB00;
    result = MiAddMdlPageToTradeBlock(Arg1, v_stack_pC8, (uint32_t)(*(uint32_t *)(arg1 + 0x1C)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    goto loc_0028D36F;
loc_0028D8B5:
    result = MiLockAndInsertPageInFreeList(local_rsi, v_stack_pC8, (uint32_t)(*(uint32_t *)(arg1 + 0x1C)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    goto loc_0028D4AF;
loc_0028D8C8:
    goto loc_0028D4AF;
loc_0028D8D3:
    goto loc_0028D36F;
loc_0028D8DE:
    result = MiGetBaseResidentPage(local_rsi, v_stack_pC8, (uint32_t)(*(uint32_t *)(arg1 + 0x1C)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    v_stack_p58 = result;
    result = (uint32_t)((*(uint8_t *)(result + 0x22)) & (7));
    v_stack_pD8 = (uint32_t)(result);
    result = MiGetPfnPageSizeIndex(result, v_stack_pC8, (uint32_t)(*(uint32_t *)(arg1 + 0x1C)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    v_stack_pC0 = (uint32_t)(result);
    Arg1 = (result) - (result);
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (result);
    result = MI_PAGE_TO_FULL_COLOR(Arg1, v_stack_pC8, (uint32_t)(*(uint32_t *)(arg1 + 0x1C)), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    if (v_stack_p58 != local_rsi) {
    }
    if (((uint32_t)((uint32_t)(v_stack_pD8))) != 6) goto loc_0028DB5E;
    *(uint64_t *)(arg1 + 0x28) = *(uint64_t *)(v_rip - 0x27BD14 + (uint32_t)(v_stack_pC0) * 8);
    goto loc_0028D36F;
loc_0028D987:
    result = (*(uint64_t *)(v_stack_p58 + 0x10)) >> (12);
    result = (uint32_t)((result) & (15));
    if (v_stack_p50 == ((uint32_t)(result))) goto loc_0028DADF;
    goto loc_0028D611;
loc_0028D9A6:
    goto loc_0028D36F;
loc_0028D9B1:
    goto loc_0028D1A3;
loc_0028D9B9:
    goto loc_0028D36F;
loc_0028D9C4:
    goto loc_0028D36F;
loc_0028D9CF:
    goto loc_0028D4AF;
loc_0028D9DA:
    if ((*(uint64_t *)(arg1 + 0x10)) < (*(uint64_t *)(v_stack_p58 + 0x10))) goto loc_0028D744;
    result = ((uint32_t)((uint32_t)(result)) - 1) + (*(uint64_t *)(v_stack_p58 + 0x10));
    if (result > (*(uint64_t *)(arg1 + 0x30))) goto loc_0028D744;
    if (result < (*(uint64_t *)(arg1 + 0x30))) goto loc_0028D744;
    v_stack_p20 = (uint8_t)(local_r15);
    result = MiLargeFreePageToMdl((uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_r10)), *(uint64_t *)(arg1 + 0x38), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    goto loc_0028D4AF;
loc_0028DA2E:
    goto loc_0028D421;
loc_0028DA39:
    if (result < (*(uint64_t *)(arg1 + 0x30))) goto loc_0028D295;
    goto loc_0028D36F;
loc_0028DA4F:
    if (((uint32_t)((uint32_t)(local_r10))) < 512) goto loc_0028D711;
    goto loc_0028D36F;
loc_0028DA61:
    if (((uint32_t)((uint32_t)(local_r10))) != 16) goto loc_0028D71C;
    goto loc_0028D36F;
loc_0028DA70:
    if (((uint32_t)(*(uint64_t *)(arg1 + 0x38))) != 6) goto loc_0028DAA7;
    if ((((uint8_t)((uint32_t)((uint32_t)(result)))) & (16)) != 0) goto loc_0028DAA7;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x20)))) != 1) goto loc_0028DAA7;
    result = (*(uint64_t *)(local_rsi + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) == 2) goto loc_0028DAA7;
    if ((((uint8_t)(*(uint64_t *)(local_rsi))) & (1)) == 0) goto loc_0028DAA7;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsi + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (8)) == 0) goto loc_0028D2B7;
loc_0028DAA7:
    goto loc_0028D36F;
loc_0028DAB2:
    result = MiIsPageOnBadList(local_rsi, (uint32_t)((uint32_t)(local_r10)), *(uint64_t *)(arg1 + 0x38), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    if ((uint32_t)(result) == 0) goto loc_0028D4F2;
loc_0028DAC2:
    goto loc_0028D36F;
loc_0028DACD:
    result = MiIsPageOnBadList(local_rsi, (uint32_t)((uint32_t)(local_r10)), *(uint64_t *)(arg1 + 0x38), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    if ((uint32_t)(result) == 0) goto loc_0028D2C2;
    goto loc_0028DAC2;
loc_0028DADF:
    goto loc_0028D36F;
loc_0028DAEA:
    goto loc_0028D36F;
loc_0028DAF5:
    goto loc_0028D36F;
loc_0028DB00:
    result = MiReleaseFreshPageLocked(local_rsi, (uint32_t)((uint32_t)(local_r10)), *(uint64_t *)(arg1 + 0x38), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    goto loc_0028D36F;
loc_0028DB13:
    goto loc_0028D36F;
loc_0028DB1E:
    local_r13 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x18))) & (0x410000ULL));
    if (((uint32_t)(local_r13)) == 0x410000ULL) goto loc_0028DB53;
    result = MiPfnLargeBitSet(v_rip + 12235208, (uint32_t)((uint32_t)(result)), *(uint64_t *)(arg1 + 0x38), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    if (((uint32_t)(result)) != 3) {
        result = (uint32_t)(result);
        Arg1 = v_rip - 2604779;
        result = *(uint64_t *)(arg1 + result * 8);
        *(uint64_t *)(arg1 + 0x28) = result;
    }
    goto loc_0028D36F;
loc_0028DB5E:
    goto loc_0028D24C;
loc_0028DB6B:
    goto loc_0028D36F;
loc_0028DB76:
    if (*(uint64_t *)(local_rsi + 0x8) == 0) goto loc_0028D4E7;
    goto loc_0028D36F;
loc_0028DB8E:
    goto loc_0028D1CF;
loc_0028DB9B:
    goto loc_0028D1CF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg2` | `+ 0x0 + rdx*2` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0028D160&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
