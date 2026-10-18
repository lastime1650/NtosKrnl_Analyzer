# MiPurgeSubsection

- RVA: `0x003712F0`–`0x00371B5B` (길이 `2,155` bytes)
- VA: `0x00000001403712F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007A80C`
- 디코드: `492`개 명령, `2,155/2,155` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00371476` → [MiDeleteTransitionPte](MiDeleteTransitionPte_function_00371B70.md) (function, `0x00371B70`)
- `0x0037161E` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00371817` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x0037187F` → [KeShouldYieldProcessor](../27/KeShouldYieldProcessor_function_002773E0.md) (function, `0x002773E0`)
- `0x00371897` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x003718C1` → [MiLockSpecialPurposeMemoryCachedPage](../40/MiLockSpecialPurposeMemoryCachedPage_function_004049F0.md) (function, `0x004049F0`)
- `0x003718DE` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x003718F4` → [MiCheckProtoPtePageState](../31/MiCheckProtoPtePageState_function_003183E0.md) (function, `0x003183E0`)
- `0x0037193A` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00371949` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0037195E` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x0037199A` → [MiChangingSubsectionProtos](../68/MiChangingSubsectionProtos_function_0068057C.md) (function, `0x0068057C`)
- `0x003719EF` → [MiDeleteSectionCluster](MiDeleteSectionCluster_function_00373DF0.md) (function, `0x00373DF0`)
- `0x00371A27` → [MiPurgeValidPage](../47/MiPurgeValidPage_function_0047D15C.md) (function, `0x0047D15C`)
- `0x00371A8E` → [MiWaitForPageWriteCompletion](../2C/MiWaitForPageWriteCompletion_function_002C9EBC.md) (function, `0x002C9EBC`)
- `0x00371AA3` → [MiMakeGlobalSubsectionPte](../4D/MiMakeGlobalSubsectionPte_function_004DFEA8.md) (function, `0x004DFEA8`)
- `0x00371ABD` → [MiMakeDemandZeroPte](../33/MiMakeDemandZeroPte_function_00337A00.md) (function, `0x00337A00`)
- `0x00371AD9` → [MiReleasePageFileSpace](../28/MiReleasePageFileSpace_function_00285980.md) (function, `0x00285980`)
- `0x00371AE9` → [MiMakeGlobalSubsectionPte](../4D/MiMakeGlobalSubsectionPte_function_004DFEA8.md) (function, `0x004DFEA8`)
- `0x00371B37` → [MiSubsectionProtosCreated](../4D/MiSubsectionProtosCreated_function_004D9570.md) (function, `0x004D9570`)
- `0x00371B4D` → [MiDeleteSubsectionLargePages](../4D/MiDeleteSubsectionLargePages_function_004D51E0.md) (function, `0x004D51E0`)

### Direct callers
- [MiDeleteCachedSubsection](../29/MiDeleteCachedSubsection_function_00297888.md) at `0x0029791F`
- [MiDeleteSubsectionPages](../32/MiDeleteSubsectionPages_function_00326340.md) at `0x003263B6`
- [MmPurgeSection](../38/MmPurgeSection_function_0038B450.md) at `0x0038B5E1`
- [MiPurgeImageSection](../../page/AD/MiPurgeImageSection_function_00ADBFF4.md) at `0x00ADC03E`

### Static image references
- `0x00371355` → RVA `0x00E30088` (`.data`; read)
- `0x003713C3` → RVA `0x00E2DC80` (`.data`; read)
- `0x00371567` → RVA `0x00E2DCE0` (`.data`; read)
- `0x003716A2` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0037192C` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x003713FA` → [sub_006E3D4A + 0x18](../6E/Unknown_function_006E3D4A.md) (`tail-transfer`)
  - `0x00371A6C` → [sub_006E3D4A](../6E/Unknown_function_006E3D4A.md) (`tail-transfer`)
  - `0x00371AB2` → [sub_006E3D4A + 0x65](../6E/Unknown_function_006E3D4A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003712F0  4C 8B DC                        mov r11, rsp
003712F3  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
003712F7  53                              push rbx
003712F8  56                              push rsi
003712F9  57                              push rdi
003712FA  41 54                           push r12
003712FC  41 55                           push r13
003712FE  41 56                           push r14
00371300  41 57                           push r15
00371302  48 81 EC A0 00 00 00            sub rsp, 0xa0
00371309  48 8B 19                        mov rbx, qword ptr [rcx]
0037130C  33 C0                           xor eax, eax
0037130E  48 8B BC 24 00 01 00 00         mov rdi, qword ptr [rsp + 0x100]
00371316  0F 57 C0                        xorps xmm0, xmm0
00371319  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
0037131E  49 89 43 B8                     mov qword ptr [r11 - 0x48], rax
00371322  4C 8B D1                        mov r10, rcx
00371325  41 0F 11 43 A8                  movups xmmword ptr [r11 - 0x58], xmm0
0037132A  B9 FF 03 00 00                  mov ecx, 0x3ff
0037132F  45 8B E9                        mov r13d, r9d
00371332  0F 11 07                        movups xmmword ptr [rdi], xmm0
00371335  45 33 C9                        xor r9d, r9d
00371338  4D 8B E0                        mov r12, r8
0037133B  0F 11 47 10                     movups xmmword ptr [rdi + 0x10], xmm0
0037133F  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
00371343  4C 8B FA                        mov r15, rdx
00371346  0F B7 43 3C                     movzx eax, word ptr [rbx + 0x3c]
0037134A  66 23 C1                        and ax, cx
0037134D  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00371352  0F B7 C8                        movzx ecx, ax
00371355  48 8B 05 2C ED AB 00            mov rax, qword ptr [rip + 0xabed2c]
0037135C  4C 8B 1C C8                     mov r11, qword ptr [rax + rcx*8]
00371360  0F B6 43 3E                     movzx eax, byte ptr [rbx + 0x3e]
00371364  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
00371369  A8 0C                           test al, 0xc
0037136B  75 05                           jne 0x140371372
0037136D  41 8B C9                        mov ecx, r9d
00371370  EB 17                           jmp 0x140371389
00371372  24 0C                           and al, 0xc
00371374  B9 01 00 00 00                  mov ecx, 1
00371379  89 8C 24 F0 00 00 00            mov dword ptr [rsp + 0xf0], ecx
00371380  3C 08                           cmp al, 8
00371382  75 0C                           jne 0x140371390
00371384  B9 03 00 00 00                  mov ecx, 3
00371389  89 8C 24 F0 00 00 00            mov dword ptr [rsp + 0xf0], ecx
00371390  41 8B C5                        mov eax, r13d
00371393  C6 84 24 F8 00 00 00 11         mov byte ptr [rsp + 0xf8], 0x11
0037139B  83 E0 02                        and eax, 2
0037139E  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
003713A3  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
003713A7  49 8B F1                        mov rsi, r9
003713AA  0F 84 C9 05 00 00               je 0x140371979
003713B0  41 BE 01 00 00 00               mov r14d, 1
003713B6  44 89 B4 24 E8 00 00 00         mov dword ptr [rsp + 0xe8], r14d
003713BE  E9 07 01 00 00                  jmp 0x1403714ca
003713C3  48 8B 05 B6 C8 AB 00            mov rax, qword ptr [rip + 0xabc8b6]
003713CA  48 85 C0                        test rax, rax
003713CD  74 0F                           je 0x1403713de
003713CF  F6 C3 10                        test bl, 0x10
003713D2  0F 85 90 03 00 00               jne 0x140371768
003713D8  48 F7 D0                        not rax
003713DB  48 23 D8                        and rbx, rax
003713DE  48 C1 EB 0C                     shr rbx, 0xc
003713E2  85 F6                           test esi, esi
003713E4  0F 85 CB 05 00 00               jne 0x1403719b5
003713EA  8B 74 24 40                     mov esi, dword ptr [rsp + 0x40]
003713EE  85 F6                           test esi, esi
003713F0  0F 84 C9 03 00 00               je 0x1403717bf
003713F6  41 F6 C5 04                     test r13b, 4
003713FA  0F 85 62 29 37 00               jne 0x1406e3d62
00371400  41 B9 F0 FF FF FF               mov r9d, 0xfffffff0
00371406  49 8D 57 08                     lea rdx, [r15 + 8]
0037140A  49 23 D9                        and rbx, r9
0037140D  41 B8 08 00 00 00               mov r8d, 8
00371413  49 3B D4                        cmp rdx, r12
00371416  73 52                           jae 0x14037146a
00371418  48 F7 C2 FF 0F 00 00            test rdx, 0xfff
0037141F  74 49                           je 0x14037146a
00371421  48 8B 02                        mov rax, qword ptr [rdx]
00371424  A8 01                           test al, 1
00371426  75 3C                           jne 0x140371464
00371428  48 8B C8                        mov rcx, rax
0037142B  81 E1 00 0C 00 00               and ecx, 0xc00
00371431  48 81 F9 00 08 00 00            cmp rcx, 0x800
00371438  75 2A                           jne 0x140371464
0037143A  48 8B 0D 3F C8 AB 00            mov rcx, qword ptr [rip + 0xabc83f]
00371441  48 85 C9                        test rcx, rcx
00371444  74 0E                           je 0x140371454
00371446  A8 10                           test al, 0x10
00371448  0F 85 D6 01 00 00               jne 0x140371624
0037144E  48 F7 D1                        not rcx
00371451  48 23 C1                        and rax, rcx
00371454  48 C1 E8 0C                     shr rax, 0xc
00371458  49 23 C1                        and rax, r9
0037145B  48 3B C3                        cmp rax, rbx
0037145E  0F 84 C9 01 00 00               je 0x14037162d
00371464  41 83 C0 FF                     add r8d, -1
00371468  75 AE                           jne 0x140371418
0037146A  45 33 C9                        xor r9d, r9d
0037146D  41 B0 11                        mov r8b, 0x11
00371470  49 8B D6                        mov rdx, r14
00371473  49 8B CF                        mov rcx, r15
00371476  E8 F5 06 00 00                  call 0x140371b70
0037147B  48 8B BC 24 00 01 00 00         mov rdi, qword ptr [rsp + 0x100]
00371483  83 F8 03                        cmp eax, 3
00371486  0F 84 18 05 00 00               je 0x1403719a4
0037148C  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00371491  48 FF 07                        inc qword ptr [rdi]
00371494  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
00371497  24 A0                           and al, 0xa0
00371499  3C 80                           cmp al, 0x80
0037149B  0F 84 56 03 00 00               je 0x1403717f7
003714A1  41 F6 C5 04                     test r13b, 4
003714A5  0F 85 ED 05 00 00               jne 0x140371a98
003714AB  49 83 C7 08                     add r15, 8
003714AF  F6 07 0F                        test byte ptr [rdi], 0xf
003714B2  0F 84 B0 03 00 00               je 0x140371868
003714B8  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
003714BD  44 8B B4 24 E8 00 00 00         mov r14d, dword ptr [rsp + 0xe8]
003714C5  4C 8B 5C 24 30                  mov r11, qword ptr [rsp + 0x30]
003714CA  49 B8 FF FF FF FF FF 00 00 00   movabs r8, 0xffffffffff
003714D4  4D 3B FC                        cmp r15, r12
003714D7  0F 83 2A 03 00 00               jae 0x140371807
003714DD  49 F7 C7 FF 0F 00 00            test r15, 0xfff
003714E4  0F 84 E4 03 00 00               je 0x1403718ce
003714EA  80 BC 24 F8 00 00 00 11         cmp byte ptr [rsp + 0xf8], 0x11
003714F2  0F 84 EB 03 00 00               je 0x1403718e3
003714F8  41 8B F5                        mov esi, r13d
003714FB  83 E6 04                        and esi, 4
003714FE  0F 84 BB 01 00 00               je 0x1403716bf
00371504  49 8B 1F                        mov rbx, qword ptr [r15]
00371507  48 8B C3                        mov rax, rbx
0037150A  F6 C3 01                        test bl, 1
0037150D  75 47                           jne 0x140371556
0037150F  25 00 0C 00 00                  and eax, 0xc00
00371514  48 3D 00 08 00 00               cmp rax, 0x800
0037151A  0F 85 18 01 00 00               jne 0x140371638
00371520  48 85 DB                        test rbx, rbx
00371523  74 10                           je 0x140371535
00371525  48 8B 05 54 C7 AB 00            mov rax, qword ptr [rip + 0xabc754]
0037152C  48 85 C0                        test rax, rax
0037152F  0F 85 54 01 00 00               jne 0x140371689
00371535  48 8B 0D 44 C7 AB 00            mov rcx, qword ptr [rip + 0xabc744]
0037153C  48 8B C3                        mov rax, rbx
0037153F  48 85 C9                        test rcx, rcx
00371542  74 12                           je 0x140371556
00371544  F6 C3 10                        test bl, 0x10
00371547  0F 85 69 02 00 00               jne 0x1403717b6
0037154D  48 8B C1                        mov rax, rcx
00371550  48 F7 D0                        not rax
00371553  48 23 C3                        and rax, rbx
00371556  48 C1 E8 0C                     shr rax, 0xc
0037155A  49 B8 FF FF FF FF FF 00 00 00   movabs r8, 0xffffffffff
00371564  49 23 C0                        and rax, r8
00371567  48 3B 05 72 C7 AB 00            cmp rax, qword ptr [rip + 0xabc772]
0037156E  77 94                           ja 0x140371504
00371570  48 8D 0C 40                     lea rcx, [rax + rax*2]
00371574  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
0037157E  48 03 C9                        add rcx, rcx
00371581  48 8B C0                        mov rax, rax
00371584  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
00371588  48 0F BA E0 36                  bt rax, 0x36
0037158D  0F 83 71 FF FF FF               jae 0x140371504
00371593  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0037159D  48 8B C0                        mov rax, rax
003715A0  4C 8D 34 C8                     lea r14, [rax + rcx*8]
003715A4  33 FF                           xor edi, edi
003715A6  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
003715B0  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
003715B7  0F 82 E3 00 00 00               jb 0x1403716a0
003715BD  49 8B 07                        mov rax, qword ptr [r15]
003715C0  48 3B C3                        cmp rax, rbx
003715C3  0F 85 8B 02 00 00               jne 0x140371854
003715C9  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
003715CD  48 8B 0D B4 EA AB 00            mov rcx, qword ptr [rip + 0xabeab4]
003715D4  48 C1 E8 2B                     shr rax, 0x2b
003715D8  25 FF 03 00 00                  and eax, 0x3ff
003715DD  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
003715E1  8B 40 04                        mov eax, dword ptr [rax + 4]
003715E4  84 C0                           test al, al
003715E6  0F 88 D0 02 00 00               js 0x1403718bc
003715EC  49 8B 1F                        mov rbx, qword ptr [r15]
003715EF  4D 85 F6                        test r14, r14
003715F2  74 47                           je 0x14037163b
003715F4  F6 C3 01                        test bl, 1
003715F7  0F 85 11 04 00 00               jne 0x140371a0e
003715FD  48 0F BA E3 0A                  bt rbx, 0xa
00371602  0F 83 69 01 00 00               jae 0x140371771
00371608  4D 8B 4E 08                     mov r9, qword ptr [r14 + 8]
0037160C  4D 8B C7                        mov r8, r15
0037160F  BA 01 00 00 00                  mov edx, 1
00371614  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00371619  B9 DE 00 00 00                  mov ecx, 0xde
0037161E  E8 3D C0 18 00                  call 0x1404fd660
00371623  CC                              int3
00371624  48 83 E0 EF                     and rax, 0xffffffffffffffef
00371628  E9 27 FE FF FF                  jmp 0x140371454
0037162D  41 B9 01 00 00 00               mov r9d, 1
00371633  E9 35 FE FF FF                  jmp 0x14037146d
00371638  49 8B 1F                        mov rbx, qword ptr [r15]
0037163B  48 0F BA E3 0A                  bt rbx, 0xa
00371640  72 31                           jb 0x140371673
00371642  83 7C 24 40 00                  cmp dword ptr [rsp + 0x40], 0
00371647  0F 84 63 04 00 00               je 0x140371ab0
0037164D  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
00371652  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00371657  0F B6 C2                        movzx eax, dl
0037165A  C0 E8 02                        shr al, 2
0037165D  A8 01                           test al, 1
0037165F  75 09                           jne 0x14037166a
00371661  0F B6 C2                        movzx eax, dl
00371664  D0 E8                           shr al, 1
00371666  A8 01                           test al, 1
00371668  74 09                           je 0x140371673
0037166A  48 85 D2                        test rdx, rdx
0037166D  0F 85 E0 02 00 00               jne 0x140371953
00371673  48 8B BC 24 00 01 00 00         mov rdi, qword ptr [rsp + 0x100]
0037167B  49 83 C7 08                     add r15, 8
0037167F  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00371684  E9 2F FE FF FF                  jmp 0x1403714b8
00371689  48 85 D8                        test rax, rbx
0037168C  0F 84 72 FE FF FF               je 0x140371504
00371692  E9 9E FE FF FF                  jmp 0x140371535
00371697  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
003716A0  FF C7                           inc edi
003716A2  85 3D 04 3C C5 00               test dword ptr [rip + 0xc53c04], edi
003716A8  0F 84 7E 02 00 00               je 0x14037192c
003716AE  F3 90                           pause
003716B0  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
003716B4  48 85 C0                        test rax, rax
003716B7  0F 89 F3 FE FF FF               jns 0x1403715b0
003716BD  EB E1                           jmp 0x1403716a0
003716BF  49 8B C4                        mov rax, r12
003716C2  49 2B C7                        sub rax, r15
003716C5  48 C1 F8 03                     sar rax, 3
003716C9  48 83 F8 10                     cmp rax, 0x10
003716CD  0F 82 31 FE FF FF               jb 0x140371504
003716D3  41 8B CF                        mov ecx, r15d
003716D6  B8 00 10 00 00                  mov eax, 0x1000
003716DB  81 E1 FF 0F 00 00               and ecx, 0xfff
003716E1  2B C1                           sub eax, ecx
003716E3  8B C8                           mov ecx, eax
003716E5  48 83 E1 F8                     and rcx, 0xfffffffffffffff8
003716E9  48 81 F9 80 00 00 00            cmp rcx, 0x80
003716F0  0F 82 0E FE FF FF               jb 0x140371504
003716F6  49 8B 0F                        mov rcx, qword ptr [r15]
003716F9  48 8B C1                        mov rax, rcx
003716FC  25 01 0C 00 00                  and eax, 0xc01
00371701  48 3D 00 08 00 00               cmp rax, 0x800
00371707  0F 85 F7 FD FF FF               jne 0x140371504
0037170D  48 8B 05 6C C5 AB 00            mov rax, qword ptr [rip + 0xabc56c]
00371714  48 85 C0                        test rax, rax
00371717  74 0F                           je 0x140371728
00371719  F6 C1 10                        test cl, 0x10
0037171C  0F 85 29 01 00 00               jne 0x14037184b
00371722  48 F7 D0                        not rax
00371725  48 23 C8                        and rcx, rax
00371728  48 C1 E9 0C                     shr rcx, 0xc
0037172C  49 23 C8                        and rcx, r8
0037172F  F6 C1 0F                        test cl, 0xf
00371732  0F 85 CC FD FF FF               jne 0x140371504
00371738  48 8D 51 01                     lea rdx, [rcx + 1]
0037173C  B9 01 00 00 00                  mov ecx, 1
00371741  8B C1                           mov eax, ecx
00371743  48 83 F8 10                     cmp rax, 0x10
00371747  0F 83 99 02 00 00               jae 0x1403719e6
0037174D  49 8B 04 C7                     mov rax, qword ptr [r15 + rax*8]
00371751  48 C1 E8 0C                     shr rax, 0xc
00371755  49 23 C0                        and rax, r8
00371758  48 3B C2                        cmp rax, rdx
0037175B  0F 85 A3 FD FF FF               jne 0x140371504
00371761  48 FF C2                        inc rdx
00371764  FF C1                           inc ecx
00371766  EB D9                           jmp 0x140371741
00371768  48 83 E3 EF                     and rbx, 0xffffffffffffffef
0037176C  E9 6D FC FF FF                  jmp 0x1403713de
00371771  41 F6 46 10 01                  test byte ptr [r14 + 0x10], 1
00371776  0F 85 8C FE FF FF               jne 0x140371608
0037177C  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00371780  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
0037178A  48 0B C1                        or rax, rcx
0037178D  49 3B C7                        cmp rax, r15
00371790  0F 85 72 FE FF FF               jne 0x140371608
00371796  49 8B 56 10                     mov rdx, qword ptr [r14 + 0x10]
0037179A  41 F6 C5 06                     test r13b, 6
0037179E  0F 94 C1                        sete cl
003717A1  48 0F BA E2 0A                  bt rdx, 0xa
003717A6  0F 93 C0                        setae al
003717A9  84 C8                           test al, cl
003717AB  0F 85 57 FE FF FF               jne 0x140371608
003717B1  E9 0D FC FF FF                  jmp 0x1403713c3
003717B6  48 83 E0 EF                     and rax, 0xffffffffffffffef
003717BA  E9 97 FD FF FF                  jmp 0x140371556
003717BF  41 F6 46 22 10                  test byte ptr [r14 + 0x22], 0x10
003717C4  48 8B BC 24 00 01 00 00         mov rdi, qword ptr [rsp + 0x100]
003717CC  0F 85 D7 00 00 00               jne 0x1403718a9
003717D2  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
003717D6  66 85 C0                        test ax, ax
003717D9  0F 85 6F 02 00 00               jne 0x140371a4e
003717DF  8B 84 24 F0 00 00 00            mov eax, dword ptr [rsp + 0xf0]
003717E6  A8 02                           test al, 2
003717E8  0F 84 08 FC FF FF               je 0x1403713f6
003717EE  C6 47 09 01                     mov byte ptr [rdi + 9], 1
003717F2  E9 FF FB FF FF                  jmp 0x1403713f6
003717F7  48 83 7B 20 00                  cmp qword ptr [rbx + 0x20], 0
003717FC  0F 85 9F FC FF FF               jne 0x1403714a1
00371802  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00371807  0F B6 94 24 F8 00 00 00         movzx edx, byte ptr [rsp + 0xf8]
0037180F  80 FA 11                        cmp dl, 0x11
00371812  74 08                           je 0x14037181c
00371814  48 8B CE                        mov rcx, rsi
00371817  E8 74 48 ED FF                  call 0x140246090
0037181C  83 BC 24 F0 00 00 00 00         cmp dword ptr [rsp + 0xf0], 0
00371824  0F 85 E4 02 00 00               jne 0x140371b0e
0037182A  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
0037182E  48 85 D2                        test rdx, rdx
00371831  0F 85 0A 03 00 00               jne 0x140371b41
00371837  48 81 C4 A0 00 00 00            add rsp, 0xa0
0037183E  41 5F                           pop r15
00371840  41 5E                           pop r14
00371842  41 5D                           pop r13
00371844  41 5C                           pop r12
00371846  5F                              pop rdi
00371847  5E                              pop rsi
00371848  5B                              pop rbx
00371849  C3                              ret
0037184A  CC                              int3
0037184B  48 83 E1 EF                     and rcx, 0xffffffffffffffef
0037184F  E9 D4 FE FF FF                  jmp 0x140371728
00371854  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0037185E  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
00371863  E9 9C FC FF FF                  jmp 0x140371504
00371868  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0037186D  48 B9 FE FF FF FF FF 0F 00 00   movabs rcx, 0xffffffffffe
00371877  48 8B 06                        mov rax, qword ptr [rsi]
0037187A  48 85 C1                        test rcx, rax
0037187D  75 0D                           jne 0x14037188c
0037187F  E8 5C 5B F0 FF                  call 0x1402773e0
00371884  85 C0                           test eax, eax
00371886  0F 84 2C FC FF FF               je 0x1403714b8
0037188C  0F B6 94 24 F8 00 00 00         movzx edx, byte ptr [rsp + 0xf8]
00371894  48 8B CE                        mov rcx, rsi
00371897  E8 F4 47 ED FF                  call 0x140246090
0037189C  C6 84 24 F8 00 00 00 11         mov byte ptr [rsp + 0xf8], 0x11
003718A4  E9 14 FC FF FF                  jmp 0x1403714bd
003718A9  41 F6 C5 01                     test r13b, 1
003718AD  0F 84 43 02 00 00               je 0x140371af6
003718B3  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
003718B7  E9 16 FF FF FF                  jmp 0x1403717d2
003718BC  33 D2                           xor edx, edx
003718BE  49 8B CE                        mov rcx, r14
003718C1  E8 2A 31 09 00                  call 0x1404049f0
003718C6  4C 8B F0                        mov r14, rax
003718C9  E9 1E FD FF FF                  jmp 0x1403715ec
003718CE  0F B6 94 24 F8 00 00 00         movzx edx, byte ptr [rsp + 0xf8]
003718D6  80 FA 11                        cmp dl, 0x11
003718D9  74 08                           je 0x1403718e3
003718DB  48 8B CE                        mov rcx, rsi
003718DE  E8 AD 47 ED FF                  call 0x140246090
003718E3  4C 8D 8C 24 F8 00 00 00         lea r9, [rsp + 0xf8]
003718EB  45 8B C6                        mov r8d, r14d
003718EE  49 8B D7                        mov rdx, r15
003718F1  48 8B CB                        mov rcx, rbx
003718F4  E8 E7 6A FA FF                  call 0x1403183e0
003718F9  4C 8B 5C 24 30                  mov r11, qword ptr [rsp + 0x30]
003718FE  48 8B F0                        mov rsi, rax
00371901  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00371906  49 B8 FF FF FF FF FF 00 00 00   movabs r8, 0xffffffffff
00371910  48 85 C0                        test rax, rax
00371913  0F 85 DF FB FF FF               jne 0x1403714f8
00371919  49 81 E7 00 F0 FF FF            and r15, 0xfffffffffffff000
00371920  49 81 C7 00 10 00 00            add r15, 0x1000
00371927  E9 A8 FB FF FF                  jmp 0x1403714d4
0037192C  8B 05 86 51 C5 00               mov eax, dword ptr [rip + 0xc55186]
00371932  A8 40                           test al, 0x40
00371934  0F 84 74 FD FF FF               je 0x1403716ae
0037193A  E8 51 DB F9 FF                  call 0x14030f490
0037193F  84 C0                           test al, al
00371941  0F 84 67 FD FF FF               je 0x1403716ae
00371947  8B CF                           mov ecx, edi
00371949  E8 12 DB F9 FF                  call 0x14030f460
0037194E  E9 5D FD FF FF                  jmp 0x1403716b0
00371953  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00371958  41 B8 01 00 00 00               mov r8d, 1
0037195E  E8 6D 26 F1 FF                  call 0x140283fd0
00371963  48 8B BC 24 00 01 00 00         mov rdi, qword ptr [rsp + 0x100]
0037196B  49 83 C7 08                     add r15, 8
0037196F  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00371974  E9 3F FB FF FF                  jmp 0x1403714b8
00371979  44 89 8C 24 E8 00 00 00         mov dword ptr [rsp + 0xe8], r9d
00371981  45 8B F1                        mov r14d, r9d
00371984  F6 C1 01                        test cl, 1
00371987  0F 84 3D FB FF FF               je 0x1403714ca
0037198D  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
00371992  BA 20 00 00 00                  mov edx, 0x20
00371997  49 8B CA                        mov rcx, r10
0037199A  E8 DD EB 30 00                  call 0x14068057c
0037199F  E9 21 FB FF FF                  jmp 0x1403714c5
003719A4  85 F6                           test esi, esi
003719A6  0F 84 E0 FA FF FF               je 0x14037148c
003719AC  48 FF 47 20                     inc qword ptr [rdi + 0x20]
003719B0  E9 D7 FA FF FF                  jmp 0x14037148c
003719B5  41 0F B6 4E 22                  movzx ecx, byte ptr [r14 + 0x22]
003719BA  C0 E9 04                        shr cl, 4
003719BD  48 0F BA E2 0A                  bt rdx, 0xa
003719C2  F6 D1                           not cl
003719C4  0F 92 C0                        setb al
003719C7  22 C8                           and cl, al
003719C9  F6 C1 01                        test cl, 1
003719CC  0F 84 18 FA FF FF               je 0x1403713ea
003719D2  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003719DC  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
003719E1  E9 8D FC FF FF                  jmp 0x140371673
003719E6  45 8B C5                        mov r8d, r13d
003719E9  49 8B D7                        mov rdx, r15
003719EC  49 8B CB                        mov rcx, r11
003719EF  E8 FC 23 00 00                  call 0x140373df0
003719F4  48 85 C0                        test rax, rax
003719F7  0F 84 07 FB FF FF               je 0x140371504
003719FD  48 01 07                        add qword ptr [rdi], rax
00371A00  4D 8D 3C C7                     lea r15, [r15 + rax*8]
00371A04  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00371A09  E9 B7 FA FF FF                  jmp 0x1403714c5
00371A0E  83 7C 24 40 00                  cmp dword ptr [rsp + 0x40], 0
00371A13  48 8B BC 24 00 01 00 00         mov rdi, qword ptr [rsp + 0x100]
00371A1B  0F 84 D5 00 00 00               je 0x140371af6
00371A21  4C 8B C7                        mov r8, rdi
00371A24  48 8B D3                        mov rdx, rbx
00371A27  E8 30 B7 10 00                  call 0x14047d15c
00371A2C  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00371A36  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
00371A3B  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00371A40  49 83 C7 08                     add r15, 8
00371A44  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00371A49  E9 6F FA FF FF                  jmp 0x1403714bd
00371A4E  41 F6 C5 08                     test r13b, 8
00371A52  0F 85 9E 00 00 00               jne 0x140371af6
00371A58  41 0F B6 4E 22                  movzx ecx, byte ptr [r14 + 0x22]
00371A5D  C0 E9 03                        shr cl, 3
00371A60  41 F6 C5 04                     test r13b, 4
00371A64  0F 94 C0                        sete al
00371A67  22 C8                           and cl, al
00371A69  F6 C1 01                        test cl, 1
00371A6C  0F 84 D8 22 37 00               je 0x1406e3d4a
00371A72  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00371A77  49 8B CE                        mov rcx, r14
00371A7A  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00371A7F  4C 8B C6                        mov r8, rsi
00371A82  44 0F B6 8C 24 F8 00 00 00      movzx r9d, byte ptr [rsp + 0xf8]
00371A8B  48 8B D3                        mov rdx, rbx
00371A8E  E8 29 84 F5 FF                  call 0x1402c9ebc
00371A93  E9 04 FE FF FF                  jmp 0x14037189c
00371A98  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
00371AA0  49 8B D7                        mov rdx, r15
00371AA3  E8 00 E4 16 00                  call 0x1404dfea8
00371AA8  49 89 07                        mov qword ptr [r15], rax
00371AAB  E9 FB F9 FF FF                  jmp 0x1403714ab
00371AB0  85 F6                           test esi, esi
00371AB2  0F 84 F7 22 37 00               je 0x1406e3daf
00371AB8  B9 18 00 00 00                  mov ecx, 0x18
00371ABD  E8 3E 5F FC FF                  call 0x140337a00
00371AC2  48 3B D8                        cmp rbx, rax
00371AC5  0F 84 A8 FB FF FF               je 0x140371673
00371ACB  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00371AD0  41 B8 01 00 00 00               mov r8d, 1
00371AD6  48 8B D3                        mov rdx, rbx
00371AD9  E8 A2 3E F1 FF                  call 0x140285980
00371ADE  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
00371AE6  49 8B D7                        mov rdx, r15
00371AE9  E8 BA E3 16 00                  call 0x1404dfea8
00371AEE  49 89 07                        mov qword ptr [r15], rax
00371AF1  E9 7D FB FF FF                  jmp 0x140371673
00371AF6  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00371B00  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
00371B05  C6 47 08 01                     mov byte ptr [rdi + 8], 1
00371B09  E9 F4 FC FF FF                  jmp 0x140371802
00371B0E  41 F6 C5 02                     test r13b, 2
00371B12  0F 85 12 FD FF FF               jne 0x14037182a
00371B18  48 83 3F 00                     cmp qword ptr [rdi], 0
00371B1C  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00371B21  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
00371B29  B8 00 00 00 00                  mov eax, 0
00371B2E  0F 95 C0                        setne al
00371B31  45 33 C0                        xor r8d, r8d
00371B34  44 8B C8                        mov r9d, eax
00371B37  E8 34 7A 16 00                  call 0x1404d9570
00371B3C  E9 E9 FC FF FF                  jmp 0x14037182a
00371B41  4C 8B 47 18                     mov r8, qword ptr [rdi + 0x18]
00371B45  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
00371B4D  E8 8E 36 16 00                  call 0x1404d51e0
00371B52  48 01 47 20                     add qword ptr [rdi + 0x20], rax
00371B56  E9 DC FC FF FF                  jmp 0x140371837
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiPurgeSubsection(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_pE0;
    unsigned int v_stack_pE8;
    unsigned __int8 v_stack_pF8;

    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (160);
    result = 0;
    v_stack_m68 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 72) = 0;
    *(unsigned __int64 *)(v_rsp - 88) = v_xmm0;
    *(unsigned __int64 *)(a5) = v_xmm0;
    a4 = 0;
    *(unsigned __int64 *)(a5 + 16) = v_xmm0;
    *(unsigned __int64 *)(a5 + 32) = 0;
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 60)) & ((unsigned __int16)((unsigned int)(0x3FFULL))));
    v_stack_m90 = *(unsigned __int64 *)(a1);
    v_stack_mA8 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11267372) + (unsigned __int16)(result) * 8);
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 62))) & (12)) != 0) goto loc_00371372;
    goto loc_00371389;
loc_00371372:
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 62)) & (12));
    v_stack_p18 = 1;
    if (((unsigned __int8)(result)) != 8) goto loc_00371390;
loc_00371389:
    v_stack_p18 = 3;
loc_00371390:
    v_stack_p20 = 17;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (2));
    v_stack_mA0 = 0;
    v_stack_m98 = (unsigned int)(result);
    if (condition_is_equal) goto loc_00371979;
    v_stack_p10 = 1;
    goto loc_003714CA;
loc_003713C3:
    if (*(unsigned __int64 *)(v_rip + 11258038) == 0) goto loc_003713DE;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1))) & (16)) != 0) goto loc_00371768;
    result = ~(*(unsigned __int64 *)(v_rip + 11258038));
    v_rbx = (*(unsigned __int64 *)(a1)) & (result);
loc_003713DE:
    v_rbx = (v_rbx) >> (12);
    if (0 != 0) goto loc_003719B5;
loc_003713EA:
    if ((unsigned int)((unsigned int)(v_stack_m98)) == 0) goto loc_003717BF;
loc_003713F6:
    v_rbx = (v_rbx) & ((unsigned int)(0xFFFFFFF0ULL));
    if ((a2 + 8) >= a3) goto loc_0037146A;
loc_00371418:
    if (((a2 + 8) & (0xFFFULL)) == 0) goto loc_0037146A;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 + 8))) & (1)) != 0) goto loc_00371464;
    a1 = (unsigned int)((*(unsigned __int64 *)(a2 + 8)) & (0xC00ULL));
    if (a1 != 0x800ULL) goto loc_00371464;
    if (*(unsigned __int64 *)(v_rip + 11257919) == 0) goto loc_00371454;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 + 8))) & (16)) != 0) goto loc_00371624;
    a1 = ~(*(unsigned __int64 *)(v_rip + 11257919));
    result = (*(unsigned __int64 *)(a2 + 8)) & (a1);
loc_00371454:
    result = (result) >> (12);
    result = (result) & ((unsigned int)(0xFFFFFFF0ULL));
    if (result == v_rbx) goto loc_0037162D;
loc_00371464:
    a3 = (unsigned int)((8) + (-1));
    if (condition_is_not_equal) goto loc_00371418;
loc_0037146A:
    a4 = 0;
loc_0037146D:
    result = MiDeleteTransitionPte(a2, 1, 17, a4);
    if (((unsigned int)(result)) == 3) goto loc_003719A4;
loc_0037148C:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_m90 + 56))) & (160));
    if (((unsigned __int8)(result)) == 128) goto loc_003717F7;
loc_003714A1:
    if ((((unsigned __int8)((unsigned int)(a4))) & (4)) != 0) goto loc_00371A98;
loc_003714AB:
    v_r15 = (a2) + (8);
    if (((*(unsigned __int8 *)(a5)) & (15)) == 0) goto loc_00371868;
loc_003714B8:
loc_003714BD:
loc_003714C5:
loc_003714CA:
loc_003714D4:
    if (v_r15 >= a3) goto loc_00371807;
    if (((v_r15) & (0xFFFULL)) == 0) goto loc_003718CE;
    if (v_stack_p20 == 17) goto loc_003718E3;
loc_003714F8:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (4));
    if (condition_is_equal) goto loc_003716BF;
loc_00371504:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (1)) != 0) goto loc_00371556;
    result = (unsigned int)((*(unsigned __int64 *)(v_r15)) & (0xC00ULL));
    if (result != 0x800ULL) goto loc_00371638;
    if (*(unsigned __int64 *)(v_r15) == 0) goto loc_00371535;
    if (*(unsigned __int64 *)(v_rip + 11257684) != 0) goto loc_00371689;
loc_00371535:
    if (*(unsigned __int64 *)(v_rip + 11257668) == 0) goto loc_00371556;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (16)) != 0) goto loc_003717B6;
    result = ~(*(unsigned __int64 *)(v_rip + 11257668));
    result = (result) & (*(unsigned __int64 *)(v_r15));
loc_00371556:
    result = (result) >> (12);
    result = (result) & (17);
    if (result > (*(unsigned __int64 *)(v_rip + 11257714))) goto loc_00371504;
    a1 = (result + result * 2) + (result + result * 2);
    if (condition_is_above_or_equal) goto loc_00371504;
    v_rdi = 0;
loc_003715B0:
    if (condition_is_below) goto loc_003716A0;
    if ((*(unsigned __int64 *)(v_r15)) != (*(unsigned __int64 *)(v_r15))) goto loc_00371854;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + a1 * 8) + a1 * 8 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (sign_flag) goto loc_003718BC;
loc_003715EC:
    if (*(unsigned __int64 *)(result + a1 * 8) + a1 * 8 == 0) goto loc_0037163B;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (1)) != 0) goto loc_00371A0E;
    if (condition_is_above_or_equal) goto loc_00371771;
loc_00371608:
    v_stack_mB8 = *(unsigned __int64 *)(v_r15);
    result = KeBugCheckEx(222, 1, v_r15, *(unsigned __int64 *)(*(unsigned __int64 *)(result + a1 * 8) + a1 * 8 + 8));
loc_00371624:
    result = (result) & (-17);
    goto loc_00371454;
loc_0037162D:
    goto loc_0037146D;
loc_00371638:
loc_0037163B:
    if (condition_is_below) goto loc_00371673;
    if (v_stack_m98 == 0) goto loc_00371AB0;
    v_stack_m88 = *(unsigned __int64 *)(v_r15);
    result = (unsigned __int8)(((unsigned __int8)(v_stack_m88)) >> (2));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_0037166A;
    result = (unsigned __int8)(((unsigned __int8)(v_stack_m88)) >> (1));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_00371673;
loc_0037166A:
    if (v_stack_m88 != 0) goto loc_00371953;
loc_00371673:
    v_r15 = (v_r15) + (8);
    goto loc_003714B8;
loc_00371689:
    if (((result) & (v_stack_m90)) == 0) goto loc_00371504;
    goto loc_00371535;
loc_003716A0:
    v_rdi = (unsigned int)((a5) + 1);
    if (((*(unsigned int *)(v_rip + 12925956)) & ((unsigned int)(v_rdi))) == 0) goto loc_0037192C;
loc_003716AE:
loc_003716B0:
    if (!sign_flag) goto loc_003715B0;
    goto loc_003716A0;
loc_003716BF:
    result = (a3) - (v_r15);
    result = (result) >> (3);
    if (result < 16) goto loc_00371504;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (0xFFFULL));
    result = (unsigned int)(((unsigned int)(0x1000ULL)) - ((unsigned int)(a1)));
    a1 = ((unsigned int)((unsigned int)(result))) & (-8);
    if (a1 < 128) goto loc_00371504;
    result = (unsigned int)((*(unsigned __int64 *)(v_r15)) & (0xC01ULL));
    if (result != 0x800ULL) goto loc_00371504;
    if (*(unsigned __int64 *)(v_rip + 11257196) == 0) goto loc_00371728;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r15))) & (16)) != 0) goto loc_0037184B;
    result = ~(*(unsigned __int64 *)(v_rip + 11257196));
    a1 = (*(unsigned __int64 *)(v_r15)) & (result);
loc_00371728:
    a1 = (a1) >> (12);
    a1 = (a1) & (v_r15);
    if ((((unsigned __int8)(a1)) & (15)) != 0) goto loc_00371504;
loc_00371741:
    if (1 >= 16) goto loc_003719E6;
    result = (*(unsigned __int64 *)(v_r15 + 1 * 8)) >> (12);
    result = (result) & (v_r15);
    if (result != (a1 + 1)) goto loc_00371504;
    a2 = (a1 + 1) + 1;
    a1 = (unsigned int)((1) + 1);
    goto loc_00371741;
loc_00371768:
    v_rbx = (v_stack_m90) & (-17);
    goto loc_003713DE;
loc_00371771:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(result + a1 * 8) + a1 * 8 + 16)) & (1)) != 0) goto loc_00371608;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + a1 * 8) + a1 * 8 + 8)) | (a1);
    if (result != v_r15) goto loc_00371608;
    a1 = ((((unsigned __int8)((unsigned int)(a4))) & (6)) == 0) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_00371608;
    goto loc_003713C3;
loc_003717B6:
    result = (result) & (-17);
    goto loc_00371556;
loc_003717BF:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(result + a1 * 8) + a1 * 8 + 34)) & (16)) != 0) goto loc_003718A9;
loc_003717D2:
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + a1 * 8) + a1 * 8 + 32))) != 0) goto loc_00371A4E;
    if ((((unsigned __int8)((unsigned int)(v_stack_p18))) & (2)) == 0) goto loc_003713F6;
    *(unsigned __int8 *)(a5 + 9) = 1;
    goto loc_003713F6;
loc_003717F7:
    if ((*(unsigned __int64 *)(v_rbx + 32)) != 0) goto loc_003714A1;
loc_00371802:
loc_00371807:
    result = (unsigned int)(v_stack_p18);
    if (((unsigned __int8)(v_stack_p20)) != 17) {
        a1 = v_stack_mA0;
        result = MiUnlockProtoPoolPage(a1, v_stack_p20, v_r15, 1);
    }
    if (v_stack_p18 != 0) goto loc_00371B0E;
loc_0037182A:
    if (*(unsigned __int64 *)(a5 + 16) != 0) goto loc_00371B41;
loc_00371837:
    v_rsp = (v_rsp) + (160);
    return result;
loc_0037184B:
    a1 = (a1) & (-17);
    goto loc_00371728;
loc_00371854:
    goto loc_00371504;
loc_00371868:
    if (((a1) & (*(unsigned __int64 *)(v_stack_p38))) != 0) goto loc_0037188C;
    result = KeShouldYieldProcessor(a1, *(unsigned __int64 *)(a5 + 16), v_r15, 1);
    if ((unsigned int)(result) == 0) goto loc_003714B8;
loc_0037188C:
    result = MiUnlockProtoPoolPage(v_stack_p38, v_stack_pF8, v_r15, 1);
loc_0037189C:
    v_stack_pF8 = 17;
    goto loc_003714BD;
loc_003718A9:
    if ((((unsigned __int8)((unsigned int)(a4))) & (1)) == 0) goto loc_00371AF6;
    *(unsigned __int8 *)(a5 + 10) = 1;
    goto loc_003717D2;
loc_003718BC:
    a2 = 0;
    result = MiLockSpecialPurposeMemoryCachedPage(*(unsigned __int64 *)(result + a1 * 8) + a1 * 8, a2, v_r15, 1);
    goto loc_003715EC;
loc_003718CE:
    if (((unsigned __int8)(v_stack_pF8)) != 17) {
        a1 = v_stack_p38;
        result = MiUnlockProtoPoolPage(a1, v_stack_pF8, v_r15, 1);
    }
    result = MiCheckProtoPtePageState(v_rbx, v_r15, (unsigned int)((unsigned int)(result)), v_stack_pF8);
    v_stack_p38 = result;
    if (result != 0) goto loc_003714F8;
    v_r15 = (v_r15) & (0xFFFFFFFFFFFFF000ULL);
    v_r15 = (v_r15) + (0x1000ULL);
    goto loc_003714D4;
loc_0037192C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12931462)))) & (64)) == 0) goto loc_003716AE;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_rbx, v_r15, (unsigned int)((unsigned int)(result)), v_stack_pF8);
    if ((unsigned __int8)(result) == 0) goto loc_003716AE;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(a5)), v_r15, (unsigned int)((unsigned int)(result)), v_stack_pF8);
    goto loc_003716B0;
loc_00371953:
    result = MiReleasePageFileInfo(v_stack_p30, v_r15, 1, v_stack_pF8);
    v_r15 = (v_r15) + (8);
    goto loc_003714B8;
loc_00371979:
    v_stack_pE8 = (unsigned int)(v_stack_pF8);
    if ((((unsigned __int8)(v_stack_p30)) & (1)) == 0) goto loc_003714CA;
    result = MiChangingSubsectionProtos(a1, 32, v_stack_p70, v_stack_pF8);
    goto loc_003714C5;
loc_003719A4:
    if ((unsigned int)(result) == 0) goto loc_0037148C;
    goto loc_0037148C;
loc_003719B5:
    a1 = (unsigned __int8)((*(unsigned __int8 *)((unsigned int)((unsigned int)(v_stack_pF8)) + 34)) >> (4));
    a1 = (unsigned __int8)(~(a1));
    result = (condition_is_below) ? 1 : 0;
    a1 = (unsigned __int8)((a1) & ((unsigned __int8)(result)));
    if ((((unsigned __int8)(a1)) & (1)) == 0) goto loc_003713EA;
    goto loc_00371673;
loc_003719E6:
    result = MiDeleteSectionCluster(v_stack_p30, v_r15, (unsigned int)((unsigned int)((unsigned int)(a4))), v_stack_pF8);
    if (result == 0) goto loc_00371504;
    goto loc_003714C5;
loc_00371A0E:
    if (v_stack_p40 == 0) goto loc_00371AF6;
    result = MiPurgeValidPage(v_stack_p30, v_stack_p48, a5, v_stack_pF8);
    v_r15 = (v_r15 + result * 8) + (8);
    goto loc_003714BD;
loc_00371A4E:
    if ((((unsigned __int8)((unsigned int)(a4))) & (8)) != 0) goto loc_00371AF6;
    a1 = (unsigned __int8)((*(unsigned __int8 *)((unsigned int)((unsigned int)(v_stack_pF8)) + 34)) >> (3));
    result = ((((unsigned __int8)((unsigned int)(a4))) & (4)) == 0) ? 1 : 0;
    a1 = (unsigned __int8)((a1) & ((unsigned __int8)(result)));
    result = MiWaitForPageWriteCompletion((unsigned int)((unsigned int)(v_stack_pF8)), v_stack_p48, v_stack_p38, v_stack_pF8);
    goto loc_0037189C;
loc_00371A98:
    result = MiMakeGlobalSubsectionPte(v_stack_pE0, v_r15, v_stack_p38, v_stack_pF8);
    *(unsigned __int64 *)(v_r15) = result;
    goto loc_003714AB;
loc_00371AB0:
    result = MiMakeDemandZeroPte(24, v_r15, v_stack_p38, v_stack_pF8);
    if (v_stack_p48 == result) goto loc_00371673;
    result = MiReleasePageFileSpace(v_stack_p30, v_stack_p48, 1, v_stack_pF8);
    result = MiMakeGlobalSubsectionPte(v_stack_pE0, v_r15, 1, v_stack_pF8);
    *(unsigned __int64 *)(v_r15) = result;
    goto loc_00371673;
loc_00371AF6:
    *(unsigned __int8 *)(a5 + 8) = 1;
    goto loc_00371802;
loc_00371B0E:
    if ((((unsigned __int8)((unsigned int)(a4))) & (2)) != 0) goto loc_0037182A;
    result = ((*(unsigned __int64 *)(a5)) != 0) ? 1 : 0;
    a3 = 0;
    result = MiSubsectionProtosCreated(v_stack_pE0, v_stack_p70, a3, (unsigned int)((unsigned int)(result)));
    goto loc_0037182A;
loc_00371B41:
    result = MiDeleteSubsectionLargePages(v_stack_pE0, v_stack_p70, *(unsigned __int64 *)(a5 + 24), (unsigned int)((unsigned int)(result)));
    goto loc_00371837;
}
```

## 5. (Beta) C Style

```c
int64_t MiPurgeSubsection(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m68;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p70;
    uint64_t v_stack_pE0;
    uint32_t v_stack_pE8;
    uint8_t v_stack_pF8;

    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (160);
    result = 0;
    v_stack_m68 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x48) = 0;
    *(uint64_t *)(local_rsp - 0x58) = v_xmm0;
    *(uint64_t *)(arg5) = v_xmm0;
    Arg4 = 0;
    *(uint64_t *)(arg5 + 0x10) = v_xmm0;
    *(uint64_t *)(arg5 + 0x20) = 0;
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(arg1) + 0x3C)) & ((uint16_t)((uint32_t)(0x3FFULL))));
    v_stack_m90 = *(uint64_t *)(arg1);
    v_stack_mA8 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xABED2C) + (uint16_t)(result) * 8);
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1) + 0x3E))) & (12)) != 0) goto loc_00371372;
    goto loc_00371389;
loc_00371372:
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1) + 0x3E)) & (12));
    v_stack_p18 = 1;
    if (((uint8_t)(result)) != 8) goto loc_00371390;
loc_00371389:
    v_stack_p18 = 3;
loc_00371390:
    v_stack_p20 = 17;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (2));
    v_stack_mA0 = 0;
    v_stack_m98 = (uint32_t)(result);
    if (condition_is_equal) goto loc_00371979;
    v_stack_p10 = 1;
    goto loc_003714CA;
loc_003713C3:
    if (*(uint64_t *)(v_rip + 0xABC8B6) == 0) goto loc_003713DE;
    if ((((uint8_t)(*(uint64_t *)(arg1))) & (16)) != 0) goto loc_00371768;
    result = ~(*(uint64_t *)(v_rip + 0xABC8B6));
    local_rbx = (*(uint64_t *)(arg1)) & (result);
loc_003713DE:
    local_rbx = (local_rbx) >> (12);
    if (0 != 0) goto loc_003719B5;
loc_003713EA:
    if ((uint32_t)((uint32_t)(v_stack_m98)) == 0) goto loc_003717BF;
loc_003713F6:
    local_rbx = (local_rbx) & ((uint32_t)(0xFFFFFFF0ULL));
    if ((Arg2 + 8) >= Arg3) goto loc_0037146A;
loc_00371418:
    if (((Arg2 + 8) & (0xFFFULL)) == 0) goto loc_0037146A;
    if ((((uint8_t)(*(uint64_t *)(Arg2 + 0x8))) & (1)) != 0) goto loc_00371464;
    Arg1 = (uint32_t)((*(uint64_t *)(Arg2 + 0x8)) & (0xC00ULL));
    if (Arg1 != 0x800ULL) goto loc_00371464;
    if (*(uint64_t *)(v_rip + 0xABC83F) == 0) goto loc_00371454;
    if ((((uint8_t)(*(uint64_t *)(Arg2 + 0x8))) & (16)) != 0) goto loc_00371624;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xABC83F));
    result = (*(uint64_t *)(Arg2 + 0x8)) & (Arg1);
loc_00371454:
    result = (result) >> (12);
    result = (result) & ((uint32_t)(0xFFFFFFF0ULL));
    if (result == local_rbx) goto loc_0037162D;
loc_00371464:
    Arg3 = (uint32_t)((8) + (-1));
    if (condition_is_not_equal) goto loc_00371418;
loc_0037146A:
    Arg4 = 0;
loc_0037146D:
    result = MiDeleteTransitionPte(Arg2, 1, 17, Arg4);
    if (((uint32_t)(result)) == 3) goto loc_003719A4;
loc_0037148C:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_m90 + 0x38))) & (160));
    if (((uint8_t)(result)) == 128) goto loc_003717F7;
loc_003714A1:
    if ((((uint8_t)((uint32_t)(Arg4))) & (4)) != 0) goto loc_00371A98;
loc_003714AB:
    local_r15 = (Arg2) + (8);
    if (((*(uint8_t *)(arg5)) & (15)) == 0) goto loc_00371868;
loc_003714B8:
loc_003714BD:
loc_003714C5:
loc_003714CA:
loc_003714D4:
    if (local_r15 >= Arg3) goto loc_00371807;
    if (((local_r15) & (0xFFFULL)) == 0) goto loc_003718CE;
    if (v_stack_p20 == 17) goto loc_003718E3;
loc_003714F8:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (4));
    if (condition_is_equal) goto loc_003716BF;
loc_00371504:
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (1)) != 0) goto loc_00371556;
    result = (uint32_t)((*(uint64_t *)(local_r15)) & (0xC00ULL));
    if (result != 0x800ULL) goto loc_00371638;
    if (*(uint64_t *)(local_r15) == 0) goto loc_00371535;
    if (*(uint64_t *)(v_rip + 0xABC754) != 0) goto loc_00371689;
loc_00371535:
    if (*(uint64_t *)(v_rip + 0xABC744) == 0) goto loc_00371556;
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (16)) != 0) goto loc_003717B6;
    result = ~(*(uint64_t *)(v_rip + 0xABC744));
    result = (result) & (*(uint64_t *)(local_r15));
loc_00371556:
    result = (result) >> (12);
    result = (result) & (17);
    if (result > (*(uint64_t *)(v_rip + 0xABC772))) goto loc_00371504;
    Arg1 = (result + result * 2) + (result + result * 2);
    if (condition_is_above_or_equal) goto loc_00371504;
    local_rdi = 0;
loc_003715B0:
    if (condition_is_below) goto loc_003716A0;
    if ((*(uint64_t *)(local_r15)) != (*(uint64_t *)(local_r15))) goto loc_00371854;
    result = (*(uint64_t *)(*(uint64_t *)(result + arg1 * 8) + arg1 * 8 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (sign_flag) goto loc_003718BC;
loc_003715EC:
    if (*(uint64_t *)(result + arg1 * 8) + Arg1 * 8 == 0) goto loc_0037163B;
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (1)) != 0) goto loc_00371A0E;
    if (condition_is_above_or_equal) goto loc_00371771;
loc_00371608:
    v_stack_mB8 = *(uint64_t *)(local_r15);
    result = KeBugCheckEx(222, 1, local_r15, *(uint64_t *)(*(uint64_t *)(result + arg1 * 8) + arg1 * 8 + 0x8));
loc_00371624:
    result = (result) & (-17);
    goto loc_00371454;
loc_0037162D:
    goto loc_0037146D;
loc_00371638:
loc_0037163B:
    if (condition_is_below) goto loc_00371673;
    if (v_stack_m98 == 0) goto loc_00371AB0;
    v_stack_m88 = *(uint64_t *)(local_r15);
    result = (uint8_t)(((uint8_t)(v_stack_m88)) >> (2));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_0037166A;
    result = (uint8_t)(((uint8_t)(v_stack_m88)) >> (1));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_00371673;
loc_0037166A:
    if (v_stack_m88 != 0) goto loc_00371953;
loc_00371673:
    local_r15 = (local_r15) + (8);
    goto loc_003714B8;
loc_00371689:
    if (((result) & (v_stack_m90)) == 0) goto loc_00371504;
    goto loc_00371535;
loc_003716A0:
    local_rdi = (uint32_t)((Arg5) + 1);
    if (((*(uint32_t *)(v_rip + 0xC53C04)) & ((uint32_t)(local_rdi))) == 0) goto loc_0037192C;
loc_003716AE:
loc_003716B0:
    if (!sign_flag) goto loc_003715B0;
    goto loc_003716A0;
loc_003716BF:
    result = (Arg3) - (local_r15);
    result = (result) >> (3);
    if (result < 16) goto loc_00371504;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (0xFFFULL));
    result = (uint32_t)(((uint32_t)(0x1000ULL)) - ((uint32_t)(Arg1)));
    Arg1 = ((uint32_t)((uint32_t)(result))) & (-8);
    if (Arg1 < 128) goto loc_00371504;
    result = (uint32_t)((*(uint64_t *)(local_r15)) & (0xC01ULL));
    if (result != 0x800ULL) goto loc_00371504;
    if (*(uint64_t *)(v_rip + 0xABC56C) == 0) goto loc_00371728;
    if ((((uint8_t)(*(uint64_t *)(local_r15))) & (16)) != 0) goto loc_0037184B;
    result = ~(*(uint64_t *)(v_rip + 0xABC56C));
    Arg1 = (*(uint64_t *)(local_r15)) & (result);
loc_00371728:
    Arg1 = (Arg1) >> (12);
    Arg1 = (Arg1) & (local_r15);
    if ((((uint8_t)(Arg1)) & (15)) != 0) goto loc_00371504;
loc_00371741:
    if (1 >= 16) goto loc_003719E6;
    result = (*(uint64_t *)(local_r15 + 0x1 * 8)) >> (12);
    result = (result) & (local_r15);
    if (result != (Arg1 + 1)) goto loc_00371504;
    Arg2 = (Arg1 + 1) + 1;
    Arg1 = (uint32_t)((1) + 1);
    goto loc_00371741;
loc_00371768:
    local_rbx = (v_stack_m90) & (-17);
    goto loc_003713DE;
loc_00371771:
    if (((*(uint8_t *)(*(uint64_t *)(result + arg1 * 8) + arg1 * 8 + 0x10)) & (1)) != 0) goto loc_00371608;
    result = (*(uint64_t *)(*(uint64_t *)(result + arg1 * 8) + arg1 * 8 + 0x8)) | (Arg1);
    if (result != local_r15) goto loc_00371608;
    Arg1 = ((((uint8_t)((uint32_t)(Arg4))) & (6)) == 0) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_00371608;
    goto loc_003713C3;
loc_003717B6:
    result = (result) & (-17);
    goto loc_00371556;
loc_003717BF:
    if (((*(uint8_t *)(*(uint64_t *)(result + arg1 * 8) + arg1 * 8 + 0x22)) & (16)) != 0) goto loc_003718A9;
loc_003717D2:
    if ((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + arg1 * 8) + arg1 * 8 + 0x20))) != 0) goto loc_00371A4E;
    if ((((uint8_t)((uint32_t)(v_stack_p18))) & (2)) == 0) goto loc_003713F6;
    *(uint8_t *)(arg5 + 0x9) = 1;
    goto loc_003713F6;
loc_003717F7:
    if ((*(uint64_t *)(local_rbx + 0x20)) != 0) goto loc_003714A1;
loc_00371802:
loc_00371807:
    result = (uint32_t)(v_stack_p18);
    if (((uint8_t)(v_stack_p20)) != 17) {
        Arg1 = v_stack_mA0;
        result = MiUnlockProtoPoolPage(Arg1, v_stack_p20, local_r15, 1);
    }
    if (v_stack_p18 != 0) goto loc_00371B0E;
loc_0037182A:
    if (*(uint64_t *)(arg5 + 0x10) != 0) goto loc_00371B41;
loc_00371837:
    local_rsp = (local_rsp) + (160);
    return result;
loc_0037184B:
    Arg1 = (Arg1) & (-17);
    goto loc_00371728;
loc_00371854:
    goto loc_00371504;
loc_00371868:
    if (((Arg1) & (*(uint64_t *)(v_stack_p38))) != 0) goto loc_0037188C;
    result = KeShouldYieldProcessor(Arg1, *(uint64_t *)(arg5 + 0x10), local_r15, 1);
    if ((uint32_t)(result) == 0) goto loc_003714B8;
loc_0037188C:
    result = MiUnlockProtoPoolPage(v_stack_p38, v_stack_pF8, local_r15, 1);
loc_0037189C:
    v_stack_pF8 = 17;
    goto loc_003714BD;
loc_003718A9:
    if ((((uint8_t)((uint32_t)(Arg4))) & (1)) == 0) goto loc_00371AF6;
    *(uint8_t *)(arg5 + 0xA) = 1;
    goto loc_003717D2;
loc_003718BC:
    Arg2 = 0;
    result = MiLockSpecialPurposeMemoryCachedPage(*(uint64_t *)(result + arg1 * 8) + Arg1 * 8, Arg2, local_r15, 1);
    goto loc_003715EC;
loc_003718CE:
    if (((uint8_t)(v_stack_pF8)) != 17) {
        Arg1 = v_stack_p38;
        result = MiUnlockProtoPoolPage(Arg1, v_stack_pF8, local_r15, 1);
    }
    result = MiCheckProtoPtePageState(local_rbx, local_r15, (uint32_t)((uint32_t)(result)), v_stack_pF8);
    v_stack_p38 = result;
    if (result != 0) goto loc_003714F8;
    local_r15 = (local_r15) & (0xFFFFFFFFFFFFF000ULL);
    local_r15 = (local_r15) + (0x1000ULL);
    goto loc_003714D4;
loc_0037192C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC55186)))) & (64)) == 0) goto loc_003716AE;
    result = KiCheckVpBackingLongSpinWaitHypercall(local_rbx, local_r15, (uint32_t)((uint32_t)(result)), v_stack_pF8);
    if ((uint8_t)(result) == 0) goto loc_003716AE;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(Arg5)), local_r15, (uint32_t)((uint32_t)(result)), v_stack_pF8);
    goto loc_003716B0;
loc_00371953:
    result = MiReleasePageFileInfo(v_stack_p30, local_r15, 1, v_stack_pF8);
    local_r15 = (local_r15) + (8);
    goto loc_003714B8;
loc_00371979:
    v_stack_pE8 = (uint32_t)(v_stack_pF8);
    if ((((uint8_t)(v_stack_p30)) & (1)) == 0) goto loc_003714CA;
    result = MiChangingSubsectionProtos(Arg1, 32, v_stack_p70, v_stack_pF8);
    goto loc_003714C5;
loc_003719A4:
    if ((uint32_t)(result) == 0) goto loc_0037148C;
    goto loc_0037148C;
loc_003719B5:
    Arg1 = (uint8_t)((*(uint8_t *)((uint32_t)((uint32_t)(v_stack_pF8)) + 0x22)) >> (4));
    Arg1 = (uint8_t)(~(Arg1));
    result = (condition_is_below) ? 1 : 0;
    Arg1 = (uint8_t)((Arg1) & ((uint8_t)(result)));
    if ((((uint8_t)(Arg1)) & (1)) == 0) goto loc_003713EA;
    goto loc_00371673;
loc_003719E6:
    result = MiDeleteSectionCluster(v_stack_p30, local_r15, (uint32_t)((uint32_t)((uint32_t)(Arg4))), v_stack_pF8);
    if (result == 0) goto loc_00371504;
    goto loc_003714C5;
loc_00371A0E:
    if (v_stack_p40 == 0) goto loc_00371AF6;
    result = MiPurgeValidPage(v_stack_p30, v_stack_p48, Arg5, v_stack_pF8);
    local_r15 = (local_r15 + result * 8) + (8);
    goto loc_003714BD;
loc_00371A4E:
    if ((((uint8_t)((uint32_t)(Arg4))) & (8)) != 0) goto loc_00371AF6;
    Arg1 = (uint8_t)((*(uint8_t *)((uint32_t)((uint32_t)(v_stack_pF8)) + 0x22)) >> (3));
    result = ((((uint8_t)((uint32_t)(Arg4))) & (4)) == 0) ? 1 : 0;
    Arg1 = (uint8_t)((Arg1) & ((uint8_t)(result)));
    result = MiWaitForPageWriteCompletion((uint32_t)((uint32_t)(v_stack_pF8)), v_stack_p48, v_stack_p38, v_stack_pF8);
    goto loc_0037189C;
loc_00371A98:
    result = MiMakeGlobalSubsectionPte(v_stack_pE0, local_r15, v_stack_p38, v_stack_pF8);
    *(uint64_t *)(local_r15) = result;
    goto loc_003714AB;
loc_00371AB0:
    result = MiMakeDemandZeroPte(24, local_r15, v_stack_p38, v_stack_pF8);
    if (v_stack_p48 == result) goto loc_00371673;
    result = MiReleasePageFileSpace(v_stack_p30, v_stack_p48, 1, v_stack_pF8);
    result = MiMakeGlobalSubsectionPte(v_stack_pE0, local_r15, 1, v_stack_pF8);
    *(uint64_t *)(local_r15) = result;
    goto loc_00371673;
loc_00371AF6:
    *(uint8_t *)(arg5 + 0x8) = 1;
    goto loc_00371802;
loc_00371B0E:
    if ((((uint8_t)((uint32_t)(Arg4))) & (2)) != 0) goto loc_0037182A;
    result = ((*(uint64_t *)(arg5)) != 0) ? 1 : 0;
    Arg3 = 0;
    result = MiSubsectionProtosCreated(v_stack_pE0, v_stack_p70, Arg3, (uint32_t)((uint32_t)(result)));
    goto loc_0037182A;
loc_00371B41:
    result = MiDeleteSubsectionLargePages(v_stack_pE0, v_stack_p70, *(uint64_t *)(arg5 + 0x18), (uint32_t)((uint32_t)(result)));
    goto loc_00371837;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg5` | `+ 0x0` | `8` | `R` |
| `Arg5` | `+ 0x0` | `64` | `R` |
| `Arg5` | `+ 0x0` | `64` | `R/W` |
| `Arg5` | `+ 0x0` | `128` | `R` |
| `Arg5` | `+ 0x8` | `8` | `W` |
| `Arg5` | `+ 0x9` | `8` | `W` |
| `Arg5` | `+ 0xA` | `8` | `W` |
| `Arg5` | `+ 0x10` | `64` | `R` |
| `Arg5` | `+ 0x10` | `128` | `R` |
| `Arg5` | `+ 0x18` | `64` | `R` |
| `Arg5` | `+ 0x20` | `64` | `R/W` |
| `Arg5` | `+ 0x20` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003712F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
