# MiHandleForkTransitionPte

- RVA: `0x0022D34C`–`0x0022DC15` (길이 `2,249` bytes)
- VA: `0x000000014022D34C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006004C`
- 디코드: `517`개 명령, `2,249/2,249` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **40**; 고유 호출 대상: **27**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x0022D398` → [MiMakePrototypePteDirect](../29/MiMakePrototypePteDirect_function_00294DE0.md) (function, `0x00294DE0`)
- `0x0022D426` → [MiGetCloneCharges](MiGetCloneCharges_function_0022CB5C.md) (function, `0x0022CB5C`)
- `0x0022D43A` → [MiWriteUselessChildPte](../38/MiWriteUselessChildPte_function_00382CFC.md) (function, `0x00382CFC`)
- `0x0022D44F` → [MiInvalidPteConforms](../37/MiInvalidPteConforms_function_00372A10.md) (function, `0x00372A10`)
- `0x0022D4C5` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0022D4FA` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0022D582` → [MI_IS_SOFTWARE_PTE_SHADOW_STACK](../38/MI_IS_SOFTWARE_PTE_SHADOW_STACK_function_003815D0.md) (function, `0x003815D0`)
- `0x0022D595` → [MI_MAKE_PROTECT_WRITE_COPY](MI_MAKE_PROTECT_WRITE_COPY_function_0022F308.md) (function, `0x0022F308`)
- `0x0022D62D` → [MI_MAKE_PROTECT_WRITE_COPY](MI_MAKE_PROTECT_WRITE_COPY_function_0022F308.md) (function, `0x0022F308`)
- `0x0022D669` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x0022D67E` → [MiSetPfnContainingFrame](../36/MiSetPfnContainingFrame_function_00363FC0.md) (function, `0x00363FC0`)
- `0x0022D691` → [MiTransferPageFileOwnership](MiTransferPageFileOwnership_function_0022F320.md) (function, `0x0022F320`)
- `0x0022D744` → [MiIncreaseUsedPtesInPfn](../38/MiIncreaseUsedPtesInPfn_function_00382D90.md) (function, `0x00382D90`)
- `0x0022D777` → [MiLockAndDecrementShareCount](../2A/MiLockAndDecrementShareCount_function_002A2854.md) (function, `0x002A2854`)
- `0x0022D87D` → [MiReturnCloneCharges](../37/MiReturnCloneCharges_function_00370F50.md) (function, `0x00370F50`)
- `0x0022D8C9` → [MiFinalizePageAttribute](../33/MiFinalizePageAttribute_function_00332E30.md) (function, `0x00332E30`)
- `0x0022D903` → [MiDuplicateCloneLeaf](../38/MiDuplicateCloneLeaf_function_003825F0.md) (function, `0x003825F0`)
- `0x0022D91E` → [MiLockSpecialPurposeMemoryCachedPage](../40/MiLockSpecialPurposeMemoryCachedPage_function_004049F0.md) (function, `0x004049F0`)
- `0x0022D940` → [MiReturnCloneCharges](../37/MiReturnCloneCharges_function_00370F50.md) (function, `0x00370F50`)
- `0x0022D96B` → [MiInitializePageColorBase](../32/MiInitializePageColorBase_function_00320410.md) (function, `0x00320410`)
- `0x0022D9B1` → [MiGetPage](../28/MiGetPage_function_002884C0.md) (function, `0x002884C0`)
- `0x0022D9ED` → [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)
- `0x0022D9F7` → [MiWaitForFreePage](../2A/MiWaitForFreePage_function_002A3324.md) (function, `0x002A3324`)
- `0x0022D9FF` → [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) (function, `0x003238A0`)
- `0x0022DA16` → [MiMakeSystemAddressValid](../27/MiMakeSystemAddressValid_function_0027FF70.md) (function, `0x0027FF70`)
- `0x0022DA26` → [MiGetPage](../28/MiGetPage_function_002884C0.md) (function, `0x002884C0`)
- `0x0022DAA7` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0022DAC3` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0022DAD3` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0022DAEB` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0022DAFA` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0022DB12` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0022DB24` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0022DB48` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0022DB59` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0022DB78` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x0022DB7D` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x0022DBA5` → [MiUnlinkPageFromListEx](../28/MiUnlinkPageFromListEx_function_00287590.md) (function, `0x00287590`)
- `0x0022DBF8` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x0022DBFD` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)

### Direct callers
- [MiBuildForkPte](MiBuildForkPte_function_0022E32C.md) at `0x0022EA2E`

### Static image references
- `0x0022D39D` → RVA `0x00010880` (`.rdata`; read)
- `0x0022D3B8` → RVA `0x00E30088` (`.data`; read)
- `0x0022D458` → RVA `0x00E2DC80` (`.data`; read)
- `0x0022D49B` → RVA `0x00E2DCE0` (`.data`; read)
- `0x0022D799` → RVA `0x000105C0` (`.rdata`; read)
- `0x0022D7CC` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0022D984` → RVA `0x00E2DCC0` (`.data`; read)
- `0x0022DAB5` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **6**
  - `0x0022DB9A` → [sub_006D715C](../6D/Unknown_function_006D715C.md) (`tail-transfer`)
  - `0x0022DBAF` → [sub_006D715C + 0x3](../6D/Unknown_function_006D715C.md) (`tail-transfer`)
  - `0x0022DBCB` → [sub_006D715C + 0x29](../6D/Unknown_function_006D715C.md) (`tail-transfer`)
  - `0x0022DBE4` → [sub_006D715C + 0x29](../6D/Unknown_function_006D715C.md) (`tail-transfer`)
  - `0x0022DBF2` → [sub_006D715C + 0x45](../6D/Unknown_function_006D715C.md) (`tail-transfer`)
  - `0x0022DC10` → [sub_006D715C + 0x45](../6D/Unknown_function_006D715C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0022D34C  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0022D351  53                              push rbx
0022D352  55                              push rbp
0022D353  56                              push rsi
0022D354  57                              push rdi
0022D355  41 54                           push r12
0022D357  41 55                           push r13
0022D359  41 56                           push r14
0022D35B  41 57                           push r15
0022D35D  48 81 EC 88 00 00 00            sub rsp, 0x88
0022D364  4C 8B 79 48                     mov r15, qword ptr [rcx + 0x48]
0022D368  4C 8B F1                        mov r14, rcx
0022D36B  48 8B 11                        mov rdx, qword ptr [rcx]
0022D36E  0F 57 C0                        xorps xmm0, xmm0
0022D371  4C 8B 69 38                     mov r13, qword ptr [rcx + 0x38]
0022D375  48 8B 59 40                     mov rbx, qword ptr [rcx + 0x40]
0022D379  49 8B CF                        mov rcx, r15
0022D37C  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
0022D381  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0022D386  4C 89 AC 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], r13
0022D38E  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
0022D393  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
0022D398  E8 43 7A 06 00                  call 0x140294de0
0022D39D  48 8B 3D DC 34 DE FF            mov rdi, qword ptr [rip - 0x21cb24]
0022D3A4  48 8B F0                        mov rsi, rax
0022D3A7  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0022D3AC  33 ED                           xor ebp, ebp
0022D3AE  0F B7 82 AE 04 00 00            movzx eax, word ptr [rdx + 0x4ae]
0022D3B5  44 8B E5                        mov r12d, ebp
0022D3B8  48 8B 15 C9 2C C0 00            mov rdx, qword ptr [rip + 0xc02cc9]
0022D3BF  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
0022D3C4  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
0022D3C9  4C 8B 04 C2                     mov r8, qword ptr [rdx + rax*8]
0022D3CD  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0022D3D1  4C 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r8
0022D3D9  0F B7 88 AE 04 00 00            movzx ecx, word ptr [rax + 0x4ae]
0022D3E0  48 8B 04 CA                     mov rax, qword ptr [rdx + rcx*8]
0022D3E4  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0022D3E9  49 3B C0                        cmp rax, r8
0022D3EC  0F 85 73 07 00 00               jne 0x14022db65
0022D3F2  41 8B 46 18                     mov eax, dword ptr [r14 + 0x18]
0022D3F6  A8 01                           test al, 1
0022D3F8  74 1D                           je 0x14022d417
0022D3FA  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
0022D3FE  48 B9 3F 00 00 00 00 00 00 F0   movabs rcx, 0xf00000000000003f
0022D408  48 23 C1                        and rax, rcx
0022D40B  41 83 CC 02                     or r12d, 2
0022D40F  48 83 C8 20                     or rax, 0x20
0022D413  49 89 47 10                     mov qword ptr [r15 + 0x10], rax
0022D417  45 85 E4                        test r12d, r12d
0022D41A  0F 84 A2 00 00 00               je 0x14022d4c2
0022D420  41 8B D4                        mov edx, r12d
0022D423  49 8B C8                        mov rcx, r8
0022D426  E8 31 F7 FF FF                  call 0x14022cb5c
0022D42B  85 C0                           test eax, eax
0022D42D  0F 85 8F 00 00 00               jne 0x14022d4c2
0022D433  49 8B 56 50                     mov rdx, qword ptr [r14 + 0x50]
0022D437  48 8B CB                        mov rcx, rbx
0022D43A  E8 BD 58 15 00                  call 0x140382cfc
0022D43F  41 C7 46 60 01 00 00 00         mov dword ptr [r14 + 0x60], 1
0022D447  E9 42 03 00 00                  jmp 0x14022d78e
0022D44C  48 8B CB                        mov rcx, rbx
0022D44F  E8 BC 55 14 00                  call 0x140372a10
0022D454  85 C0                           test eax, eax
0022D456  74 6A                           je 0x14022d4c2
0022D458  48 8B 05 21 08 C0 00            mov rax, qword ptr [rip + 0xc00821]
0022D45F  48 85 C0                        test rax, rax
0022D462  74 12                           je 0x14022d476
0022D464  F6 C3 10                        test bl, 0x10
0022D467  0F 85 53 03 00 00               jne 0x14022d7c0
0022D46D  48 8B C8                        mov rcx, rax
0022D470  48 F7 D1                        not rcx
0022D473  48 23 CB                        and rcx, rbx
0022D476  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
0022D480  48 C1 E9 0C                     shr rcx, 0xc
0022D484  48 23 C8                        and rcx, rax
0022D487  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0022D491  48 8D 14 49                     lea rdx, [rcx + rcx*2]
0022D495  48 03 D2                        add rdx, rdx
0022D498  48 8B C0                        mov rax, rax
0022D49B  48 3B 0D 3E 08 C0 00            cmp rcx, qword ptr [rip + 0xc0083e]
0022D4A2  48 8D 2C D0                     lea rbp, [rax + rdx*8]
0022D4A6  77 18                           ja 0x14022d4c0
0022D4A8  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
0022D4B2  48 8B 04 D0                     mov rax, qword ptr [rax + rdx*8]
0022D4B6  48 C1 E8 36                     shr rax, 0x36
0022D4BA  0F BA E0 00                     bt eax, 0
0022D4BE  72 1D                           jb 0x14022d4dd
0022D4C0  33 ED                           xor ebp, ebp
0022D4C2  49 8B CD                        mov rcx, r13
0022D4C5  E8 D6 53 05 00                  call 0x1402828a0
0022D4CA  48 8B D8                        mov rbx, rax
0022D4CD  48 0F BA E0 0B                  bt rax, 0xb
0022D4D2  0F 82 74 FF FF FF               jb 0x14022d44c
0022D4D8  E9 55 04 00 00                  jmp 0x14022d932
0022D4DD  33 C0                           xor eax, eax
0022D4DF  44 8B E8                        mov r13d, eax
0022D4E2  F0 48 0F BA 6D 18 3F            lock bts qword ptr [rbp + 0x18], 0x3f
0022D4E9  0F 82 DA 02 00 00               jb 0x14022d7c9
0022D4EF  4C 8B AC 24 E8 00 00 00         mov r13, qword ptr [rsp + 0xe8]
0022D4F7  49 8B CD                        mov rcx, r13
0022D4FA  E8 A1 53 05 00                  call 0x1402828a0
0022D4FF  48 3B C3                        cmp rax, rbx
0022D502  0F 85 22 03 00 00               jne 0x14022d82a
0022D508  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
0022D50C  48 8B 15 75 2B C0 00            mov rdx, qword ptr [rip + 0xc02b75]
0022D513  48 C1 E8 2B                     shr rax, 0x2b
0022D517  25 FF 03 00 00                  and eax, 0x3ff
0022D51C  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
0022D520  8B 40 04                        mov eax, dword ptr [rax + 4]
0022D523  84 C0                           test al, al
0022D525  0F 88 EE 03 00 00               js 0x14022d919
0022D52B  45 33 D2                        xor r10d, r10d
0022D52E  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
0022D532  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
0022D53C  48 0B C1                        or rax, rcx
0022D53F  49 3B C5                        cmp rax, r13
0022D542  0F 85 37 05 00 00               jne 0x14022da7f
0022D548  48 85 ED                        test rbp, rbp
0022D54B  0F 84 E1 03 00 00               je 0x14022d932
0022D551  49 8B 55 00                     mov rdx, qword ptr [r13]
0022D555  8B 45 20                        mov eax, dword ptr [rbp + 0x20]
0022D558  4C 8B EA                        mov r13, rdx
0022D55B  49 C1 ED 05                     shr r13, 5
0022D55F  41 83 E5 1F                     and r13d, 0x1f
0022D563  66 85 C0                        test ax, ax
0022D566  0F 85 D2 02 00 00               jne 0x14022d83e
0022D56C  41 8B C5                        mov eax, r13d
0022D56F  83 E0 F8                        and eax, 0xfffffff8
0022D572  83 F8 10                        cmp eax, 0x10
0022D575  0F 84 C3 02 00 00               je 0x14022d83e
0022D57B  48 8D 5D 10                     lea rbx, [rbp + 0x10]
0022D57F  48 8B 0B                        mov rcx, qword ptr [rbx]
0022D582  E8 49 40 15 00                  call 0x1403815d0
0022D587  85 C0                           test eax, eax
0022D589  0F 85 AF 02 00 00               jne 0x14022d83e
0022D58F  49 8B CF                        mov rcx, r15
0022D592  49 89 17                        mov qword ptr [r15], rdx
0022D595  E8 6E 1D 00 00                  call 0x14022f308
0022D59A  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
0022D59E  41 8B 4E 18                     mov ecx, dword ptr [r14 + 0x18]
0022D5A2  F6 C1 01                        test cl, 1
0022D5A5  74 04                           je 0x14022d5ab
0022D5A7  49 FF 46 20                     inc qword ptr [r14 + 0x20]
0022D5AB  48 83 E0 E0                     and rax, 0xffffffffffffffe0
0022D5AF  41 8B CD                        mov ecx, r13d
0022D5B2  48 0B C1                        or rax, rcx
0022D5B5  49 89 47 10                     mov qword ptr [r15 + 0x10], rax
0022D5B9  48 8B 0B                        mov rcx, qword ptr [rbx]
0022D5BC  8A C1                           mov al, cl
0022D5BE  D0 E8                           shr al, 1
0022D5C0  A8 01                           test al, 1
0022D5C2  0F 85 C3 05 00 00               jne 0x14022db8b
0022D5C8  4C 89 7D 08                     mov qword ptr [rbp + 8], r15
0022D5CC  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
0022D5D0  48 8B 0D B1 2A C0 00            mov rcx, qword ptr [rip + 0xc02ab1]
0022D5D7  48 C1 E8 2B                     shr rax, 0x2b
0022D5DB  25 FF 03 00 00                  and eax, 0x3ff
0022D5E0  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
0022D5E4  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
0022D5E8  48 85 C0                        test rax, rax
0022D5EB  4C 8D 82 C0 3F 00 00            lea r8, [rdx + 0x3fc0]
0022D5F2  49 8B C0                        mov rax, r8
0022D5F5  48 8D 8A 40 1C 00 00            lea rcx, [rdx + 0x1c40]
0022D5FC  0F 88 AB 04 00 00               js 0x14022daad
0022D602  F0 48 FF 08                     lock dec qword ptr [rax]
0022D606  48 BA 00 00 00 00 00 00 00 80   movabs rdx, 0x8000000000000000
0022D610  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
0022D614  48 0B C2                        or rax, rdx
0022D617  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
0022D61B  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
0022D61F  48 85 C0                        test rax, rax
0022D622  49 0F 49 C8                     cmovns rcx, r8
0022D626  F0 48 FF 01                     lock inc qword ptr [rcx]
0022D62A  48 8B CB                        mov rcx, rbx
0022D62D  E8 D6 1C 00 00                  call 0x14022f308
0022D632  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
0022D636  49 BC FF FF FF FF FF 00 00 00   movabs r12, 0xffffffffff
0022D640  49 23 C4                        and rax, r12
0022D643  49 C1 EF 09                     shr r15, 9
0022D647  48 B9 F8 FF FF FF 7F 00 00 00   movabs rcx, 0x7ffffffff8
0022D651  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
0022D659  49 23 CF                        and rcx, r15
0022D65C  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0022D666  48 03 C8                        add rcx, rax
0022D669  E8 32 52 05 00                  call 0x1402828a0
0022D66E  48 8B D8                        mov rbx, rax
0022D671  48 8B CD                        mov rcx, rbp
0022D674  48 C1 EB 0C                     shr rbx, 0xc
0022D678  49 23 DC                        and rbx, r12
0022D67B  48 8B D3                        mov rdx, rbx
0022D67E  E8 3D 69 13 00                  call 0x140363fc0
0022D683  4C 8B BC 24 E8 00 00 00         mov r15, qword ptr [rsp + 0xe8]
0022D68B  48 8B CD                        mov rcx, rbp
0022D68E  49 8B D7                        mov rdx, r15
0022D691  E8 8A 1C 00 00                  call 0x14022f320
0022D696  33 C0                           xor eax, eax
0022D698  48 8D 1C 5B                     lea rbx, [rbx + rbx*2]
0022D69C  44 8B E0                        mov r12d, eax
0022D69F  48 C1 E3 04                     shl rbx, 4
0022D6A3  49 B8 18 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000018
0022D6AD  33 C9                           xor ecx, ecx
0022D6AF  F0 4A 0F BA 2C 03 3F            lock bts qword ptr [rbx + r8], 0x3f
0022D6B6  0F 82 2E 01 00 00               jb 0x14022d7ea
0022D6BC  4A 8B 04 03                     mov rax, qword ptr [rbx + r8]
0022D6C0  48 8D 48 01                     lea rcx, [rax + 1]
0022D6C4  48 8B D1                        mov rdx, rcx
0022D6C7  48 33 D0                        xor rdx, rax
0022D6CA  48 B8 00 00 00 00 00 00 00 C0   movabs rax, 0xc000000000000000
0022D6D4  48 23 D0                        and rdx, rax
0022D6D7  48 33 D1                        xor rdx, rcx
0022D6DA  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
0022D6E4  48 8B C1                        mov rax, rcx
0022D6E7  48 89 54 03 18                  mov qword ptr [rbx + rax + 0x18], rdx
0022D6EC  49 BC FF FF FF FF FF FF FF 7F   movabs r12, 0x7fffffffffffffff
0022D6F6  F0 4E 21 24 03                  lock and qword ptr [rbx + r8], r12
0022D6FB  49 89 37                        mov qword ptr [r15], rsi
0022D6FE  F0 4C 21 65 18                  lock and qword ptr [rbp + 0x18], r12
0022D703  33 ED                           xor ebp, ebp
0022D705  48 85 FF                        test rdi, rdi
0022D708  0F 85 B5 04 00 00               jne 0x14022dbc3
0022D70E  41 8B 46 18                     mov eax, dword ptr [r14 + 0x18]
0022D712  A8 01                           test al, 1
0022D714  74 0A                           je 0x14022d720
0022D716  41 83 FD 18                     cmp r13d, 0x18
0022D71A  74 04                           je 0x14022d720
0022D71C  48 83 CE 08                     or rsi, 8
0022D720  49 8B 7E 50                     mov rdi, qword ptr [r14 + 0x50]
0022D724  8B DD                           mov ebx, ebp
0022D726  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
0022D72D  0F 82 D8 00 00 00               jb 0x14022d80b
0022D733  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
0022D738  48 89 32                        mov qword ptr [rdx], rsi
0022D73B  BA 01 00 00 00                  mov edx, 1
0022D740  49 8B 4E 50                     mov rcx, qword ptr [r14 + 0x50]
0022D744  E8 47 56 15 00                  call 0x140382d90
0022D749  4D 8B 5E 50                     mov r11, qword ptr [r14 + 0x50]
0022D74D  F0 4D 21 63 18                  lock and qword ptr [r11 + 0x18], r12
0022D752  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
0022D75A  48 8D 0C 40                     lea rcx, [rax + rax*2]
0022D75E  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0022D768  48 C1 E1 04                     shl rcx, 4
0022D76C  48 8B C0                        mov rax, rax
0022D76F  48 03 C8                        add rcx, rax
0022D772  BA 02 00 00 00                  mov edx, 2
0022D777  E8 D8 50 07 00                  call 0x1402a2854
0022D77C  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0022D781  F0 48 FF 88 88 02 00 00         lock dec qword ptr [rax + 0x288]
0022D789  49 83 46 48 20                  add qword ptr [r14 + 0x48], 0x20
0022D78E  F3 41 0F 6F 46 38               movdqu xmm0, xmmword ptr [r14 + 0x38]
0022D794  B8 01 00 00 00                  mov eax, 1
0022D799  66 0F 6F 0D 1F 2E DE FF         movdqa xmm1, xmmword ptr [rip - 0x21d1e1]
0022D7A1  66 0F D4 C8                     paddq xmm1, xmm0
0022D7A5  F3 41 0F 7F 4E 38               movdqu xmmword ptr [r14 + 0x38], xmm1
0022D7AB  48 81 C4 88 00 00 00            add rsp, 0x88
0022D7B2  41 5F                           pop r15
0022D7B4  41 5E                           pop r14
0022D7B6  41 5D                           pop r13
0022D7B8  41 5C                           pop r12
0022D7BA  5F                              pop rdi
0022D7BB  5E                              pop rsi
0022D7BC  5D                              pop rbp
0022D7BD  5B                              pop rbx
0022D7BE  C3                              ret
0022D7BF  CC                              int3
0022D7C0  48 83 E1 EF                     and rcx, 0xffffffffffffffef
0022D7C4  E9 AD FC FF FF                  jmp 0x14022d476
0022D7C9  41 FF C5                        inc r13d
0022D7CC  44 85 2D D9 7A D9 00            test dword ptr [rip + 0xd97ad9], r13d
0022D7D3  0F 84 DC 02 00 00               je 0x14022dab5
0022D7D9  F3 90                           pause
0022D7DB  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
0022D7DF  48 85 C0                        test rax, rax
0022D7E2  0F 89 FA FC FF FF               jns 0x14022d4e2
0022D7E8  EB DF                           jmp 0x14022d7c9
0022D7EA  41 FF C4                        inc r12d
0022D7ED  44 85 25 B8 7A D9 00            test dword ptr [rip + 0xd97ab8], r12d
0022D7F4  0F 84 0A 03 00 00               je 0x14022db04
0022D7FA  F3 90                           pause
0022D7FC  4A 8B 04 03                     mov rax, qword ptr [rbx + r8]
0022D800  48 85 C0                        test rax, rax
0022D803  0F 89 A6 FE FF FF               jns 0x14022d6af
0022D809  EB DF                           jmp 0x14022d7ea
0022D80B  FF C3                           inc ebx
0022D80D  85 1D 99 7A D9 00               test dword ptr [rip + 0xd97a99], ebx
0022D813  0F 84 C4 02 00 00               je 0x14022dadd
0022D819  F3 90                           pause
0022D81B  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0022D81F  48 85 C0                        test rax, rax
0022D822  0F 89 FE FE FF FF               jns 0x14022d726
0022D828  EB E1                           jmp 0x14022d80b
0022D82A  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0022D834  F0 48 21 45 18                  lock and qword ptr [rbp + 0x18], rax
0022D839  E9 82 FC FF FF                  jmp 0x14022d4c0
0022D83E  8B 45 20                        mov eax, dword ptr [rbp + 0x20]
0022D841  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
0022D846  C1 E8 10                        shr eax, 0x10
0022D849  49 81 C5 00 04 00 00            add r13, 0x400
0022D850  0F B6 C0                        movzx eax, al
0022D853  C1 E8 06                        shr eax, 6
0022D856  89 84 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], eax
0022D85D  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
0022D865  48 83 38 FF                     cmp qword ptr [rax], -1
0022D869  0F 84 DD 00 00 00               je 0x14022d94c
0022D86F  4C 8B BC 24 E0 00 00 00         mov r15, qword ptr [rsp + 0xe0]
0022D877  41 8B D4                        mov edx, r12d
0022D87A  49 8B CF                        mov rcx, r15
0022D87D  E8 CE 36 14 00                  call 0x140370f50
0022D882  48 8B B4 24 D8 00 00 00         mov rsi, qword ptr [rsp + 0xd8]
0022D88A  33 C9                           xor ecx, ecx
0022D88C  44 8B E1                        mov r12d, ecx
0022D88F  48 8B 06                        mov rax, qword ptr [rsi]
0022D892  48 8D 1C 40                     lea rbx, [rax + rax*2]
0022D896  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0022D8A0  48 C1 E3 04                     shl rbx, 4
0022D8A4  48 8B C0                        mov rax, rax
0022D8A7  48 03 D8                        add rbx, rax
0022D8AA  8B F9                           mov edi, ecx
0022D8AC  F0 48 0F BA 6B 18 3F            lock bts qword ptr [rbx + 0x18], 0x3f
0022D8B3  0F 82 A7 01 00 00               jb 0x14022da60
0022D8B9  8B 94 24 D0 00 00 00            mov edx, dword ptr [rsp + 0xd0]
0022D8C0  41 B8 09 00 00 00               mov r8d, 9
0022D8C6  48 8B CB                        mov rcx, rbx
0022D8C9  E8 62 55 10 00                  call 0x140332e30
0022D8CE  48 BA FF FF FF FF FF FF FF 7F   movabs rdx, 0x7fffffffffffffff
0022D8D8  F0 48 21 53 18                  lock and qword ptr [rbx + 0x18], rdx
0022D8DD  F6 45 22 20                     test byte ptr [rbp + 0x22], 0x20
0022D8E1  0F 85 02 03 00 00               jne 0x14022dbe9
0022D8E7  41 8A 46 1C                     mov al, byte ptr [r14 + 0x1c]
0022D8EB  4D 8B 4E 50                     mov r9, qword ptr [r14 + 0x50]
0022D8EF  4C 8B 06                        mov r8, qword ptr [rsi]
0022D8F2  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
0022D8F7  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
0022D8FF  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0022D903  E8 E8 4C 15 00                  call 0x1403825f0
0022D908  85 C0                           test eax, eax
0022D90A  74 2E                           je 0x14022d93a
0022D90C  48 83 0E FF                     or qword ptr [rsi], 0xffffffffffffffff
0022D910  49 FF 46 58                     inc qword ptr [r14 + 0x58]
0022D914  E9 75 FE FF FF                  jmp 0x14022d78e
0022D919  33 D2                           xor edx, edx
0022D91B  48 8B CD                        mov rcx, rbp
0022D91E  E8 CD 70 1D 00                  call 0x1404049f0
0022D923  45 33 D2                        xor r10d, r10d
0022D926  48 8B E8                        mov rbp, rax
0022D929  48 85 C0                        test rax, rax
0022D92C  0F 85 FC FB FF FF               jne 0x14022d52e
0022D932  4C 8B BC 24 E0 00 00 00         mov r15, qword ptr [rsp + 0xe0]
0022D93A  41 8B D4                        mov edx, r12d
0022D93D  49 8B CF                        mov rcx, r15
0022D940  E8 0B 36 14 00                  call 0x140370f50
0022D945  33 C0                           xor eax, eax
0022D947  E9 5F FE FF FF                  jmp 0x14022d7ab
0022D94C  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0022D956  F0 48 21 45 18                  lock and qword ptr [rbp + 0x18], rax
0022D95B  4C 8D 4C 24 68                  lea r9, [rsp + 0x68]
0022D960  45 8B C2                        mov r8d, r10d
0022D963  BA 03 00 00 00                  mov edx, 3
0022D968  49 8B CD                        mov rcx, r13
0022D96B  E8 A0 2A 0F 00                  call 0x140320410
0022D970  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
0022D975  B8 01 00 00 00                  mov eax, 1
0022D97A  F0 41 0F C1 01                  lock xadd dword ptr [r9], eax
0022D97F  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
0022D984  4C 8D 0D 35 03 C0 00            lea r9, [rip + 0xc00335]
0022D98B  33 D2                           xor edx, edx
0022D98D  49 8B C8                        mov rcx, r8
0022D990  48 C1 E9 10                     shr rcx, 0x10
0022D994  83 E1 03                        and ecx, 3
0022D997  41 F7 34 89                     div dword ptr [r9 + rcx*4]
0022D99B  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0022D9A0  41 33 D0                        xor edx, r8d
0022D9A3  0F B6 DA                        movzx ebx, dl
0022D9A6  41 33 D8                        xor ebx, r8d
0022D9A9  41 B8 01 00 00 00               mov r8d, 1
0022D9AF  8B D3                           mov edx, ebx
0022D9B1  E8 0A AB 05 00                  call 0x1402884c0
0022D9B6  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
0022D9BE  48 89 01                        mov qword ptr [rcx], rax
0022D9C1  48 83 F8 FF                     cmp rax, -1
0022D9C5  75 7C                           jne 0x14022da43
0022D9C7  48 8B AC 24 E8 00 00 00         mov rbp, qword ptr [rsp + 0xe8]
0022D9CF  4C 8B F9                        mov r15, rcx
0022D9D2  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0022D9D7  33 FF                           xor edi, edi
0022D9D9  49 8B 4E 68                     mov rcx, qword ptr [r14 + 0x68]
0022D9DD  48 85 C9                        test rcx, rcx
0022D9E0  0F 85 92 01 00 00               jne 0x14022db78
0022D9E6  41 8A 56 1C                     mov dl, byte ptr [r14 + 0x1c]
0022D9EA  49 8B CD                        mov rcx, r13
0022D9ED  E8 7E 12 05 00                  call 0x14027ec70
0022D9F2  33 D2                           xor edx, edx
0022D9F4  48 8B CE                        mov rcx, rsi
0022D9F7  E8 28 59 07 00                  call 0x1402a3324
0022D9FC  49 8B CD                        mov rcx, r13
0022D9FF  E8 9C 5E 0F 00                  call 0x1403238a0
0022DA04  41 B9 01 00 00 00               mov r9d, 1
0022DA0A  41 88 46 1C                     mov byte ptr [r14 + 0x1c], al
0022DA0E  44 8A C0                        mov r8b, al
0022DA11  8B D7                           mov edx, edi
0022DA13  48 8B CD                        mov rcx, rbp
0022DA16  E8 55 25 05 00                  call 0x14027ff70
0022DA1B  41 B8 01 00 00 00               mov r8d, 1
0022DA21  8B D3                           mov edx, ebx
0022DA23  48 8B CE                        mov rcx, rsi
0022DA26  E8 95 AA 05 00                  call 0x1402884c0
0022DA2B  49 89 07                        mov qword ptr [r15], rax
0022DA2E  48 83 F8 FF                     cmp rax, -1
0022DA32  74 A5                           je 0x14022d9d9
0022DA34  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
0022DA39  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
0022DA3E  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
0022DA43  4C 8B AC 24 E8 00 00 00         mov r13, qword ptr [rsp + 0xe8]
0022DA4B  49 8B 45 00                     mov rax, qword ptr [r13]
0022DA4F  48 A9 01 04 00 00               test rax, 0x401
0022DA55  0F 84 65 FA FF FF               je 0x14022d4c0
0022DA5B  E9 D2 FE FF FF                  jmp 0x14022d932
0022DA60  FF C7                           inc edi
0022DA62  85 3D 44 78 D9 00               test dword ptr [rip + 0xd97844], edi
0022DA68  0F 84 CC 00 00 00               je 0x14022db3a
0022DA6E  F3 90                           pause
0022DA70  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0022DA74  48 85 C0                        test rax, rax
0022DA77  0F 89 2F FE FF FF               jns 0x14022d8ac
0022DA7D  EB E1                           jmp 0x14022da60
0022DA7F  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
0022DA83  48 0F BA E0 28                  bt rax, 0x28
0022DA88  0F 82 BA FA FF FF               jb 0x14022d548
0022DA8E  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
0022DA92  4C 8B CB                        mov r9, rbx
0022DA95  4D 8B C5                        mov r8, r13
0022DA98  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0022DA9D  BA 11 04 00 00                  mov edx, 0x411
0022DAA2  B9 1A 00 00 00                  mov ecx, 0x1a
0022DAA7  E8 B4 FB 2C 00                  call 0x1404fd660
0022DAAC  CC                              int3
0022DAAD  48 8B C1                        mov rax, rcx
0022DAB0  E9 4D FB FF FF                  jmp 0x14022d602
0022DAB5  8B 05 FD 8F D9 00               mov eax, dword ptr [rip + 0xd98ffd]
0022DABB  A8 40                           test al, 0x40
0022DABD  0F 84 16 FD FF FF               je 0x14022d7d9
0022DAC3  E8 C8 19 0E 00                  call 0x14030f490
0022DAC8  84 C0                           test al, al
0022DACA  0F 84 09 FD FF FF               je 0x14022d7d9
0022DAD0  41 8B CD                        mov ecx, r13d
0022DAD3  E8 88 19 0E 00                  call 0x14030f460
0022DAD8  E9 FE FC FF FF                  jmp 0x14022d7db
0022DADD  8B 05 D5 8F D9 00               mov eax, dword ptr [rip + 0xd98fd5]
0022DAE3  A8 40                           test al, 0x40
0022DAE5  0F 84 2E FD FF FF               je 0x14022d819
0022DAEB  E8 A0 19 0E 00                  call 0x14030f490
0022DAF0  84 C0                           test al, al
0022DAF2  0F 84 21 FD FF FF               je 0x14022d819
0022DAF8  8B CB                           mov ecx, ebx
0022DAFA  E8 61 19 0E 00                  call 0x14030f460
0022DAFF  E9 17 FD FF FF                  jmp 0x14022d81b
0022DB04  8B 05 AE 8F D9 00               mov eax, dword ptr [rip + 0xd98fae]
0022DB0A  A8 40                           test al, 0x40
0022DB0C  0F 84 E8 FC FF FF               je 0x14022d7fa
0022DB12  E8 79 19 0E 00                  call 0x14030f490
0022DB17  33 C9                           xor ecx, ecx
0022DB19  84 C0                           test al, al
0022DB1B  0F 84 93 00 00 00               je 0x14022dbb4
0022DB21  41 8B CC                        mov ecx, r12d
0022DB24  E8 37 19 0E 00                  call 0x14030f460
0022DB29  33 C9                           xor ecx, ecx
0022DB2B  49 B8 18 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000018
0022DB35  E9 C2 FC FF FF                  jmp 0x14022d7fc
0022DB3A  8B 05 78 8F D9 00               mov eax, dword ptr [rip + 0xd98f78]
0022DB40  A8 40                           test al, 0x40
0022DB42  0F 84 26 FF FF FF               je 0x14022da6e
0022DB48  E8 43 19 0E 00                  call 0x14030f490
0022DB4D  33 C9                           xor ecx, ecx
0022DB4F  84 C0                           test al, al
0022DB51  0F 84 17 FF FF FF               je 0x14022da6e
0022DB57  8B CF                           mov ecx, edi
0022DB59  E8 02 19 0E 00                  call 0x14030f460
0022DB5E  33 C9                           xor ecx, ecx
0022DB60  E9 0B FF FF FF                  jmp 0x14022da70
0022DB65  41 BC 05 00 00 00               mov r12d, 5
0022DB6B  49 C7 47 08 01 00 00 00         mov qword ptr [r15 + 8], 1
0022DB73  E9 7A F8 FF FF                  jmp 0x14022d3f2
0022DB78  E8 43 44 0E 00                  call 0x140311fc0
0022DB7D  E8 EE 60 0E 00                  call 0x140313c70
0022DB82  49 89 7E 68                     mov qword ptr [r14 + 0x68], rdi
0022DB86  E9 5B FE FF FF                  jmp 0x14022d9e6
0022DB8B  8A 45 22                        mov al, byte ptr [rbp + 0x22]
0022DB8E  48 8B F9                        mov rdi, rcx
0022DB91  24 07                           and al, 7
0022DB93  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0022DB98  3C 03                           cmp al, 3
0022DB9A  0F 85 BC 95 4A 00               jne 0x1406d715c
0022DBA0  33 D2                           xor edx, edx
0022DBA2  48 8B CD                        mov rcx, rbp
0022DBA5  E8 E6 99 05 00                  call 0x140287590
0022DBAA  B9 01 00 00 00                  mov ecx, 1
0022DBAF  E9 AB 95 4A 00                  jmp 0x1406d715f
0022DBB4  49 B8 18 00 00 00 00 DE FF FF   movabs r8, 0xffffde0000000018
0022DBBE  E9 37 FC FF FF                  jmp 0x14022d7fa
0022DBC3  40 8A C7                        mov al, dil
0022DBC6  C0 E8 02                        shr al, 2
0022DBC9  A8 01                           test al, 1
0022DBCB  0F 84 B4 95 4A 00               je 0x1406d7185
0022DBD1  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0022DBD6  48 83 E0 FB                     and rax, 0xfffffffffffffffb
0022DBDA  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0022DBDF  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
0022DBE4  E9 9C 95 4A 00                  jmp 0x1406d7185
0022DBE9  49 8B 4E 68                     mov rcx, qword ptr [r14 + 0x68]
0022DBED  33 DB                           xor ebx, ebx
0022DBEF  48 85 C9                        test rcx, rcx
0022DBF2  0F 84 A9 95 4A 00               je 0x1406d71a1
0022DBF8  E8 C3 43 0E 00                  call 0x140311fc0
0022DBFD  E8 6E 60 0E 00                  call 0x140313c70
0022DC02  48 BA FF FF FF FF FF FF FF 7F   movabs rdx, 0x7fffffffffffffff
0022DC0C  49 89 5E 68                     mov qword ptr [r14 + 0x68], rbx
0022DC10  E9 8C 95 4A 00                  jmp 0x1406d71a1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiHandleForkTransitionPte(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p8;
    unsigned int v_stack_pD0;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pE8;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (136);
    v_stack_m60 = v_xmm0;
    v_stack_m88 = *(unsigned __int64 *)(a1);
    v_stack_p20 = *(unsigned __int64 *)(a1 + 56);
    v_stack_m80 = *(unsigned __int64 *)(a1 + 64);
    v_stack_m68 = *(unsigned __int64 *)(a1 + 72);
    result = MiMakePrototypePteDirect(*(unsigned __int64 *)(a1 + 72), *(unsigned __int64 *)(a1), a3, a4);
    v_stack_m70 = result;
    v_rbp = 0;
    v_stack_m78 = *(unsigned __int64 *)(v_rip - 2214692);
    v_stack_m98 = *(unsigned __int64 *)(v_rip - 2214692);
    v_stack_p18 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12594377) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 1198) * 8);
    v_stack_m90 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12594377) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 1198) * 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12594377) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 1198) * 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12594377) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 1198) * 8))) goto loc_0022DB65;
loc_0022D3F2:
    result = (unsigned int)(*(unsigned int *)(a1 + 24));
    v_r12 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 24)))) & (1)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 16);
        result = (result) & (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 1198));
        v_r12 = (unsigned int)((0) | (2));
        result = (result) | (32);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 16) = result;
    }
    if ((unsigned int)(v_r12) == 0) goto loc_0022D4C2;
    result = MiGetCloneCharges(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12594377) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 1198) * 8), (unsigned int)((unsigned int)(v_r12)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12594377) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 1198) * 8), a4);
    if ((unsigned int)(result) != 0) goto loc_0022D4C2;
    result = MiWriteUselessChildPte(*(unsigned __int64 *)(a1 + 64), *(unsigned __int64 *)(a1 + 80), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12594377) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 1198) * 8), a4);
    *(unsigned int *)(a1 + 96) = 1;
    goto loc_0022D78E;
loc_0022D44C:
    result = MiInvalidPteConforms(*(unsigned __int64 *)(a1 + 64), *(unsigned __int64 *)(a1 + 80), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12594377) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 1198) * 8), a4);
    if ((unsigned int)(result) == 0) goto loc_0022D4C2;
    if (*(unsigned __int64 *)(v_rip + 12584993) == 0) goto loc_0022D476;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 64))) & (16)) != 0) goto loc_0022D7C0;
    a1 = ~(*(unsigned __int64 *)(v_rip + 12584993));
    a1 = (a1) & (*(unsigned __int64 *)(a1 + 64));
loc_0022D476:
    a1 = (a1) >> (12);
    a1 = (a1) & (*(unsigned __int64 *)(v_rip + 12584993));
    a2 = (a1 + a1 * 2) + (a1 + a1 * 2);
    if (a1 > (*(unsigned __int64 *)(v_rip + 12585022))) goto loc_0022D4C0;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12584993) + a2 * 8)) >> (54);
    if (condition_is_below) goto loc_0022D4DD;
loc_0022D4C0:
    v_rbp = 0;
loc_0022D4C2:
    result = MI_READ_PTE_LOCK_FREE(*(unsigned __int64 *)(a1 + 56), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12594377) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 1198) * 8), a4);
    if (condition_is_below) goto loc_0022D44C;
    goto loc_0022D932;
loc_0022D4DD:
    result = 0;
loc_0022D4E2:
    if (condition_is_below) goto loc_0022D7C9;
    result = MI_READ_PTE_LOCK_FREE(v_stack_p20, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12594377) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 1198) * 8), a4);
    if (result != result) goto loc_0022D82A;
    result = (*(unsigned __int64 *)(v_rbp + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (sign_flag) goto loc_0022D919;
    v_r10 = 0;
loc_0022D52E:
    result = (*(unsigned __int64 *)(v_rbp + 8)) | (v_stack_p20);
    if (result != v_stack_p20) goto loc_0022DA7F;
loc_0022D548:
    if (0 == 0) goto loc_0022D932;
    v_r13 = (*(unsigned __int64 *)(v_stack_p20)) >> (5);
    v_r13 = (unsigned int)((v_r13) & (31));
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rbp + 32))) != 0) goto loc_0022D83E;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) & (0xFFFFFFF8ULL));
    if (((unsigned int)(result)) == 16) goto loc_0022D83E;
    result = MI_IS_SOFTWARE_PTE_SHADOW_STACK(*(unsigned __int64 *)(v_rbp + 16), *(unsigned __int64 *)(v_stack_p20), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12594377) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 1198) * 8), a4);
    if ((unsigned int)(result) != 0) goto loc_0022D83E;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) = *(unsigned __int64 *)(v_stack_p20);
    result = MI_MAKE_PROTECT_WRITE_COPY(*(unsigned __int64 *)(a1 + 72), *(unsigned __int64 *)(v_stack_p20), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12594377) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 1198) * 8), a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 24)))) & (1)) != 0) {
    }
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 16)) & (-32);
    result = (result) | ((unsigned int)((unsigned int)(v_r13)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 16) = result;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_rbp + 16))) >> (1));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_0022DB8B;
    *(unsigned __int64 *)(v_rbp + 8) = *(unsigned __int64 *)(a1 + 72);
    result = (*(unsigned __int64 *)(v_rbp + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (sign_flag) goto loc_0022DAAD;
loc_0022D602:
    result = (*(unsigned __int64 *)(v_rbp + 40)) | (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12593841) + result * 8));
    *(unsigned __int64 *)(v_rbp + 40) = result;
    a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12593841) + result * 8) + 7232;
    if (!sign_flag) { a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12593841) + result * 8) + 16320; }
    result = MI_MAKE_PROTECT_WRITE_COPY(v_rbp + 16, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12593841) + result * 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12593841) + result * 8) + 16320, a4);
    result = (*(unsigned __int64 *)(v_rbp + 40)) & (v_r12);
    v_r15 = (*(unsigned __int64 *)(a1 + 72)) >> (9);
    v_stack_p8 = result;
    a1 = (v_rbp + 16) & (v_r15);
    a1 = (a1) + (result);
    result = MI_READ_PTE_LOCK_FREE(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12593841) + result * 8), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12593841) + result * 8) + 16320, a4);
    v_rbx = (result) >> (12);
    v_rbx = (v_rbx) & (v_r12);
    result = MiSetPfnContainingFrame(0, v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12593841) + result * 8) + 16320, a4);
    result = MiTransferPageFileOwnership(0, v_stack_p20, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12593841) + result * 8) + 16320, a4);
    result = 0;
    v_rbx = (v_rbx + v_rbx * 2) << (4);
    a1 = 0;
loc_0022D6AF:
    if (condition_is_below) goto loc_0022D7EA;
    a2 = (*(unsigned __int64 *)(v_rbx + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12593841) + result * 8) + 16320 * 1) + 1) ^ (*(unsigned __int64 *)(v_rbx + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12593841) + result * 8) + 16320 * 1));
    a2 = (a2) & (*(unsigned __int64 *)(v_rbx + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12593841) + result * 8) + 16320 * 1));
    a2 = (a2) ^ (*(unsigned __int64 *)(v_rbx + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12593841) + result * 8) + 16320 * 1) + 1);
    *(unsigned __int64 *)(v_rbx + *(unsigned __int64 *)(v_rbx + *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12593841) + result * 8) + 16320 * 1) + 1 * 1 + 24) = a2;
    *(unsigned __int64 *)(v_stack_p20) = 0;
    v_rbp = 0;
    if (*(unsigned __int64 *)(v_rip - 2214692) != 0) goto loc_0022DBC3;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 24)))) & (1)) == 0) goto loc_0022D720;
    v_rsi = result;
    if (((unsigned int)(v_r13)) != 24) {
        v_rsi = (result) | (8);
    }
loc_0022D726:
    if (condition_is_below) goto loc_0022D80B;
    *(unsigned __int64 *)(v_stack_m80) = v_rsi;
    result = MiIncreaseUsedPtesInPfn(*(unsigned __int64 *)(a1 + 80), 1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12593841) + result * 8) + 16320, a4);
    a1 = (v_stack_p8 + v_stack_p8 * 2) << (4);
    a1 = (a1) + (v_stack_p8);
    result = MiLockAndDecrementShareCount(a1, 2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12593841) + result * 8) + 16320, a4);
loc_0022D78E:
    *(unsigned __int64 *)(a1 + 56) = v_xmm1;
loc_0022D7AB:
    v_rsp = (v_rsp) + (136);
    return 1;
loc_0022D7C0:
    a1 = (a1) & (-17);
    goto loc_0022D476;
loc_0022D7C9:
    v_r13 = (unsigned int)((v_r13) + 1);
    if (((*(unsigned int *)(v_rip + 14252761)) & ((unsigned int)(v_r13))) == 0) goto loc_0022DAB5;
loc_0022D7D9:
loc_0022D7DB:
    if (!sign_flag) goto loc_0022D4E2;
    goto loc_0022D7C9;
loc_0022D7EA:
    v_r12 = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 14252728)) & ((unsigned int)(v_r12))) == 0) goto loc_0022DB04;
loc_0022D7FA:
loc_0022D7FC:
    if (!sign_flag) goto loc_0022D6AF;
    goto loc_0022D7EA;
loc_0022D80B:
    v_rbx = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 14252697)) & ((unsigned int)(v_rbx))) == 0) goto loc_0022DADD;
loc_0022D819:
loc_0022D81B:
    if (!sign_flag) goto loc_0022D726;
    goto loc_0022D80B;
loc_0022D82A:
    goto loc_0022D4C0;
loc_0022D83E:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp + 32))) >> (16));
    v_r13 = (v_stack_p40) + (0x400ULL);
    result = (unsigned int)(((unsigned __int8)(result)) >> (6));
    v_stack_pD0 = (unsigned int)(result);
    if ((*(unsigned __int64 *)(v_stack_pD8)) == -1) goto loc_0022D94C;
    result = MiReturnCloneCharges(v_stack_pE0, (unsigned int)((unsigned int)(v_r12)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12593841) + result * 8) + 16320, a4);
    a1 = 0;
    v_rbx = (*(unsigned __int64 *)(v_stack_pD8) + *(unsigned __int64 *)(v_stack_pD8) * 2) << (4);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_stack_pD8));
loc_0022D8AC:
    if (condition_is_below) goto loc_0022DA60;
    result = MiFinalizePageAttribute(v_rbx, (unsigned int)(v_stack_pD0), 9, a4);
    if (((*(unsigned __int8 *)(v_rbp + 34)) & (32)) != 0) goto loc_0022DBE9;
    v_stack_p20 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 28));
    result = MiDuplicateCloneLeaf(v_stack_pE8, v_stack_p48, *(unsigned __int64 *)(v_stack_pD8), *(unsigned __int64 *)(a1 + 80));
    if ((unsigned int)(result) == 0) goto loc_0022D93A;
    goto loc_0022D78E;
loc_0022D919:
    a2 = 0;
    result = MiLockSpecialPurposeMemoryCachedPage(0, a2, *(unsigned __int64 *)(v_stack_pD8), *(unsigned __int64 *)(a1 + 80));
    v_r10 = 0;
    if (result != 0) goto loc_0022D52E;
loc_0022D932:
loc_0022D93A:
    result = MiReturnCloneCharges(v_stack_pE0, 0, *(unsigned __int64 *)(v_stack_pD8), *(unsigned __int64 *)(a1 + 80));
    result = 0;
    goto loc_0022D7AB;
loc_0022D94C:
    result = MiInitializePageColorBase(v_r13, 3, 0, v_stack_p68);
    a2 = 0;
    a1 = (v_stack_p70) >> (16);
    a1 = (unsigned int)((a1) & (3));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(v_stack_p70)));
    v_rbx = (unsigned int)(((unsigned __int8)(a2)) ^ ((unsigned int)(v_stack_p70)));
    result = MiGetPage(v_stack_p38, (unsigned int)((unsigned int)(v_rbx)), 1, v_rip + 12583733);
    *(unsigned __int64 *)(v_stack_pD8) = result;
    if (result != -1) goto loc_0022DA43;
    v_rdi = 0;
loc_0022D9D9:
    if (*(unsigned __int64 *)(a1 + 104) != 0) goto loc_0022DB78;
loc_0022D9E6:
    result = MiUnlockWorkingSetExclusive(v_r13, *(unsigned __int8 *)(a1 + 28), 1, v_rip + 12583733);
    a2 = 0;
    result = MiWaitForFreePage(v_stack_p38, a2, 1, v_rip + 12583733);
    result = MiLockWorkingSetExclusive(v_r13, a2, 1, v_rip + 12583733);
    *(unsigned __int8 *)(a1 + 28) = (unsigned __int8)(result);
    result = MiMakeSystemAddressValid(v_stack_pE8, 0, (unsigned __int8)(result), 1);
    result = MiGetPage(v_stack_p38, (unsigned int)((unsigned int)(v_rbx)), 1, 1);
    *(unsigned __int64 *)(v_stack_pD8) = result;
    if (result == -1) goto loc_0022D9D9;
loc_0022DA43:
    if (((*(unsigned __int64 *)(v_stack_pE8)) & (0x401ULL)) == 0) goto loc_0022D4C0;
    goto loc_0022D932;
loc_0022DA60:
    v_rdi = (unsigned int)((v_stack_p50) + 1);
    if (((*(unsigned int *)(v_rip + 14252100)) & ((unsigned int)(v_rdi))) == 0) goto loc_0022DB3A;
loc_0022DA6E:
loc_0022DA70:
    if (!sign_flag) goto loc_0022D8AC;
    goto loc_0022DA60;
loc_0022DA7F:
    if (condition_is_below) goto loc_0022D548;
    v_stack_p20 = *(unsigned __int64 *)(v_stack_pE8 + 8);
    result = KeBugCheckEx(26, (unsigned int)(0x411ULL), v_stack_pE8, v_rbx);
loc_0022DAAD:
    goto loc_0022D602;
loc_0022DAB5:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14258173)))) & (64)) == 0) goto loc_0022D7D9;
    result = KiCheckVpBackingLongSpinWaitHypercall(26, (unsigned int)(0x411ULL), v_stack_pE8, v_rbx);
    if ((unsigned __int8)(result) == 0) goto loc_0022D7D9;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_pE8)), (unsigned int)(0x411ULL), v_stack_pE8, v_rbx);
    goto loc_0022D7DB;
loc_0022DADD:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14258133)))) & (64)) == 0) goto loc_0022D819;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_stack_pE8)), (unsigned int)(0x411ULL), v_stack_pE8, v_rbx);
    if ((unsigned __int8)(result) == 0) goto loc_0022D819;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), (unsigned int)(0x411ULL), v_stack_pE8, v_rbx);
    goto loc_0022D81B;
loc_0022DB04:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14258094)))) & (64)) == 0) goto loc_0022D7FA;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbx)), (unsigned int)(0x411ULL), v_stack_pE8, v_rbx);
    a1 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_0022DBB4;
    result = HvlNotifyLongSpinWait(0, (unsigned int)(0x411ULL), v_stack_pE8, v_rbx);
    a1 = 0;
    goto loc_0022D7FC;
loc_0022DB3A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14258040)))) & (64)) == 0) goto loc_0022DA6E;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, (unsigned int)(0x411ULL), v_stack_pE8, v_rbx);
    a1 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_0022DA6E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), (unsigned int)(0x411ULL), v_stack_pE8, v_rbx);
    a1 = 0;
    goto loc_0022DA70;
loc_0022DB65:
    *(unsigned __int64 *)(v_stack_p60 + 8) = 1;
    goto loc_0022D3F2;
loc_0022DB78:
    result = MiFlushTbList(a1, (unsigned int)(0x411ULL), v_stack_pE8, v_rbx);
    result = MiReleaseProcessorFlushList(a1, (unsigned int)(0x411ULL), v_stack_pE8, v_rbx);
    *(unsigned __int64 *)(a1 + 104) = v_rdi;
    goto loc_0022D9E6;
loc_0022DB8B:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_pE8 + 34)) & (7));
    v_stack_p30 = 0;
    a2 = 0;
    result = MiUnlinkPageFromListEx(v_stack_pE8, a2, v_stack_pE8, v_rbx);
loc_0022DBB4:
    goto loc_0022D7FA;
loc_0022DBC3:
    result = (unsigned __int8)((0) >> (2));
    result = (v_stack_p30) & (-5);
    v_stack_p30 = result;
loc_0022DBE9:
    v_rbx = 0;
    result = MiFlushTbList(*(unsigned __int64 *)(a1 + 104), a2, v_stack_pE8, v_rbx);
    result = MiReleaseProcessorFlushList(*(unsigned __int64 *)(a1 + 104), a2, v_stack_pE8, v_rbx);
    *(unsigned __int64 *)(a1 + 104) = 0;
}
```

## 5. (Beta) C Style

```c
int64_t MiHandleForkTransitionPte(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p8;
    uint32_t v_stack_pD0;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pE8;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (136);
    v_stack_m60 = v_xmm0;
    v_stack_m88 = *(uint64_t *)(arg1);
    v_stack_p20 = *(uint64_t *)(arg1 + 0x38);
    v_stack_m80 = *(uint64_t *)(arg1 + 0x40);
    v_stack_m68 = *(uint64_t *)(arg1 + 0x48);
    result = MiMakePrototypePteDirect(*(uint64_t *)(arg1 + 0x48), *(uint64_t *)(arg1), a3, a4);
    v_stack_m70 = result;
    local_rbp = 0;
    v_stack_m78 = *(uint64_t *)(v_rip - 0x21CB24);
    v_stack_m98 = *(uint64_t *)(v_rip - 0x21CB24);
    v_stack_p18 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02CC9) + *(uint16_t *)(*(uint64_t *)(arg1) + 0x4AE) * 8);
    v_stack_m90 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02CC9) + *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x4AE) * 8);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xC02CC9) + *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x4AE) * 8)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC02CC9) + *(uint16_t *)(*(uint64_t *)(arg1) + 0x4AE) * 8))) goto loc_0022DB65;
loc_0022D3F2:
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x18));
    local_r12 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))) & (1)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x10);
        result = (result) & (*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x4AE));
        local_r12 = (uint32_t)((0) | (2));
        result = (result) | (32);
        *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x10) = result;
    }
    if ((uint32_t)(local_r12) == 0) goto loc_0022D4C2;
    result = MiGetCloneCharges(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC02CC9) + *(uint16_t *)(*(uint64_t *)(arg1) + 0x4AE) * 8), (uint32_t)((uint32_t)(local_r12)), *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02CC9) + *(uint16_t *)(*(uint64_t *)(arg1) + 0x4AE) * 8), a4);
    if ((uint32_t)(result) != 0) goto loc_0022D4C2;
    result = MiWriteUselessChildPte(*(uint64_t *)(arg1 + 0x40), *(uint64_t *)(arg1 + 0x50), *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02CC9) + *(uint16_t *)(*(uint64_t *)(arg1) + 0x4AE) * 8), a4);
    *(uint32_t *)(arg1 + 0x60) = 1;
    goto loc_0022D78E;
loc_0022D44C:
    result = MiInvalidPteConforms(*(uint64_t *)(arg1 + 0x40), *(uint64_t *)(arg1 + 0x50), *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02CC9) + *(uint16_t *)(*(uint64_t *)(arg1) + 0x4AE) * 8), a4);
    if ((uint32_t)(result) == 0) goto loc_0022D4C2;
    if (*(uint64_t *)(v_rip + 0xC00821) == 0) goto loc_0022D476;
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x40))) & (16)) != 0) goto loc_0022D7C0;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xC00821));
    Arg1 = (Arg1) & (*(uint64_t *)(arg1 + 0x40));
loc_0022D476:
    Arg1 = (Arg1) >> (12);
    Arg1 = (Arg1) & (*(uint64_t *)(v_rip + 0xC00821));
    Arg2 = (Arg1 + Arg1 * 2) + (Arg1 + Arg1 * 2);
    if (Arg1 > (*(uint64_t *)(v_rip + 0xC0083E))) goto loc_0022D4C0;
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC00821) + Arg2 * 8)) >> (54);
    if (condition_is_below) goto loc_0022D4DD;
loc_0022D4C0:
    local_rbp = 0;
loc_0022D4C2:
    result = MI_READ_PTE_LOCK_FREE(*(uint64_t *)(arg1 + 0x38), Arg2, *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02CC9) + *(uint16_t *)(*(uint64_t *)(arg1) + 0x4AE) * 8), a4);
    if (condition_is_below) goto loc_0022D44C;
    goto loc_0022D932;
loc_0022D4DD:
    result = 0;
loc_0022D4E2:
    if (condition_is_below) goto loc_0022D7C9;
    result = MI_READ_PTE_LOCK_FREE(v_stack_p20, Arg2, *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02CC9) + *(uint16_t *)(*(uint64_t *)(arg1) + 0x4AE) * 8), a4);
    if (result != result) goto loc_0022D82A;
    result = (*(uint64_t *)(local_rbp + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (sign_flag) goto loc_0022D919;
    local_r10 = 0;
loc_0022D52E:
    result = (*(uint64_t *)(local_rbp + 0x8)) | (v_stack_p20);
    if (result != v_stack_p20) goto loc_0022DA7F;
loc_0022D548:
    if (0 == 0) goto loc_0022D932;
    local_r13 = (*(uint64_t *)(v_stack_p20)) >> (5);
    local_r13 = (uint32_t)((local_r13) & (31));
    if ((uint16_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x20))) != 0) goto loc_0022D83E;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) & (0xFFFFFFF8ULL));
    if (((uint32_t)(result)) == 16) goto loc_0022D83E;
    result = MI_IS_SOFTWARE_PTE_SHADOW_STACK(*(uint64_t *)(local_rbp + 0x10), *(uint64_t *)(v_stack_p20), *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02CC9) + *(uint16_t *)(*(uint64_t *)(arg1) + 0x4AE) * 8), a4);
    if ((uint32_t)(result) != 0) goto loc_0022D83E;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) = *(uint64_t *)(v_stack_p20);
    result = MI_MAKE_PROTECT_WRITE_COPY(*(uint64_t *)(arg1 + 0x48), *(uint64_t *)(v_stack_p20), *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02CC9) + *(uint16_t *)(*(uint64_t *)(arg1) + 0x4AE) * 8), a4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))) & (1)) != 0) {
    }
    result = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x10)) & (-32);
    result = (result) | ((uint32_t)((uint32_t)(local_r13)));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x10) = result;
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(local_rbp + 0x10))) >> (1));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_0022DB8B;
    *(uint64_t *)(local_rbp + 0x8) = *(uint64_t *)(arg1 + 0x48);
    result = (*(uint64_t *)(local_rbp + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (sign_flag) goto loc_0022DAAD;
loc_0022D602:
    result = (*(uint64_t *)(local_rbp + 0x28)) | (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC02AB1) + result * 8));
    *(uint64_t *)(local_rbp + 0x28) = result;
    Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02AB1) + result * 8) + 7232;
    if (!sign_flag) { Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02AB1) + result * 8) + 16320; }
    result = MI_MAKE_PROTECT_WRITE_COPY(local_rbp + 16, *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02AB1) + result * 8), *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02AB1) + result * 8) + 16320, a4);
    result = (*(uint64_t *)(local_rbp + 0x28)) & (local_r12);
    local_r15 = (*(uint64_t *)(arg1 + 0x48)) >> (9);
    v_stack_p8 = result;
    Arg1 = (local_rbp + 16) & (local_r15);
    Arg1 = (Arg1) + (result);
    result = MI_READ_PTE_LOCK_FREE(Arg1, *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02AB1) + result * 8), *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02AB1) + result * 8) + 16320, a4);
    local_rbx = (result) >> (12);
    local_rbx = (local_rbx) & (local_r12);
    result = MiSetPfnContainingFrame(0, local_rbx, *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02AB1) + result * 8) + 16320, a4);
    result = MiTransferPageFileOwnership(0, v_stack_p20, *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02AB1) + result * 8) + 16320, a4);
    result = 0;
    local_rbx = (local_rbx + local_rbx * 2) << (4);
    Arg1 = 0;
loc_0022D6AF:
    if (condition_is_below) goto loc_0022D7EA;
    Arg2 = (*(uint64_t *)(local_rbx + *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02AB1) + result * 8) + 0x3FC0 * 1) + 1) ^ (*(uint64_t *)(local_rbx + *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02AB1) + result * 8) + 0x3FC0 * 1));
    Arg2 = (Arg2) & (*(uint64_t *)(local_rbx + *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02AB1) + result * 8) + 0x3FC0 * 1));
    Arg2 = (Arg2) ^ (*(uint64_t *)(local_rbx + *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02AB1) + result * 8) + 0x3FC0 * 1) + 1);
    *(uint64_t *)(local_rbx + *(uint64_t *)(local_rbx + *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02AB1) + result * 8) + 0x3FC0 * 1) + 0x1 * 1 + 0x18) = Arg2;
    *(uint64_t *)(v_stack_p20) = 0;
    local_rbp = 0;
    if (*(uint64_t *)(v_rip - 0x21CB24) != 0) goto loc_0022DBC3;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))) & (1)) == 0) goto loc_0022D720;
    local_rsi = result;
    if (((uint32_t)(local_r13)) != 24) {
        local_rsi = (result) | (8);
    }
loc_0022D726:
    if (condition_is_below) goto loc_0022D80B;
    *(uint64_t *)(v_stack_m80) = local_rsi;
    result = MiIncreaseUsedPtesInPfn(*(uint64_t *)(arg1 + 0x50), 1, *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02AB1) + result * 8) + 16320, a4);
    Arg1 = (v_stack_p8 + v_stack_p8 * 2) << (4);
    Arg1 = (Arg1) + (v_stack_p8);
    result = MiLockAndDecrementShareCount(Arg1, 2, *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02AB1) + result * 8) + 16320, a4);
loc_0022D78E:
    *(uint64_t *)(arg1 + 0x38) = v_xmm1;
loc_0022D7AB:
    local_rsp = (local_rsp) + (136);
    return 1;
loc_0022D7C0:
    Arg1 = (Arg1) & (-17);
    goto loc_0022D476;
loc_0022D7C9:
    local_r13 = (uint32_t)((local_r13) + 1);
    if (((*(uint32_t *)(v_rip + 0xD97AD9)) & ((uint32_t)(local_r13))) == 0) goto loc_0022DAB5;
loc_0022D7D9:
loc_0022D7DB:
    if (!sign_flag) goto loc_0022D4E2;
    goto loc_0022D7C9;
loc_0022D7EA:
    local_r12 = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xD97AB8)) & ((uint32_t)(local_r12))) == 0) goto loc_0022DB04;
loc_0022D7FA:
loc_0022D7FC:
    if (!sign_flag) goto loc_0022D6AF;
    goto loc_0022D7EA;
loc_0022D80B:
    local_rbx = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xD97A99)) & ((uint32_t)(local_rbx))) == 0) goto loc_0022DADD;
loc_0022D819:
loc_0022D81B:
    if (!sign_flag) goto loc_0022D726;
    goto loc_0022D80B;
loc_0022D82A:
    goto loc_0022D4C0;
loc_0022D83E:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp + 0x20))) >> (16));
    local_r13 = (v_stack_p40) + (0x400ULL);
    result = (uint32_t)(((uint8_t)(result)) >> (6));
    v_stack_pD0 = (uint32_t)(result);
    if ((*(uint64_t *)(v_stack_pD8)) == -1) goto loc_0022D94C;
    result = MiReturnCloneCharges(v_stack_pE0, (uint32_t)((uint32_t)(local_r12)), *(uint64_t *)(*(uint64_t *)(v_rip + 0xC02AB1) + result * 8) + 16320, a4);
    Arg1 = 0;
    local_rbx = (*(uint64_t *)(v_stack_pD8) + *(uint64_t *)(v_stack_pD8) * 2) << (4);
    local_rbx = (local_rbx) + (*(uint64_t *)(v_stack_pD8));
loc_0022D8AC:
    if (condition_is_below) goto loc_0022DA60;
    result = MiFinalizePageAttribute(local_rbx, (uint32_t)(v_stack_pD0), 9, a4);
    if (((*(uint8_t *)(local_rbp + 0x22)) & (32)) != 0) goto loc_0022DBE9;
    v_stack_p20 = (uint8_t)(*(uint8_t *)(arg1 + 0x1C));
    result = MiDuplicateCloneLeaf(v_stack_pE8, v_stack_p48, *(uint64_t *)(v_stack_pD8), *(uint64_t *)(arg1 + 0x50));
    if ((uint32_t)(result) == 0) goto loc_0022D93A;
    goto loc_0022D78E;
loc_0022D919:
    Arg2 = 0;
    result = MiLockSpecialPurposeMemoryCachedPage(0, Arg2, *(uint64_t *)(v_stack_pD8), *(uint64_t *)(arg1 + 0x50));
    local_r10 = 0;
    if (result != 0) goto loc_0022D52E;
loc_0022D932:
loc_0022D93A:
    result = MiReturnCloneCharges(v_stack_pE0, 0, *(uint64_t *)(v_stack_pD8), *(uint64_t *)(arg1 + 0x50));
    result = 0;
    goto loc_0022D7AB;
loc_0022D94C:
    result = MiInitializePageColorBase(local_r13, 3, 0, v_stack_p68);
    Arg2 = 0;
    Arg1 = (v_stack_p70) >> (16);
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(v_stack_p70)));
    local_rbx = (uint32_t)(((uint8_t)(Arg2)) ^ ((uint32_t)(v_stack_p70)));
    result = MiGetPage(v_stack_p38, (uint32_t)((uint32_t)(local_rbx)), 1, v_rip + 12583733);
    *(uint64_t *)(v_stack_pD8) = result;
    if (result != -1) goto loc_0022DA43;
    local_rdi = 0;
loc_0022D9D9:
    if (*(uint64_t *)(arg1 + 0x68) != 0) goto loc_0022DB78;
loc_0022D9E6:
    result = MiUnlockWorkingSetExclusive(local_r13, *(uint8_t *)(arg1 + 0x1C), 1, v_rip + 12583733);
    Arg2 = 0;
    result = MiWaitForFreePage(v_stack_p38, Arg2, 1, v_rip + 12583733);
    result = MiLockWorkingSetExclusive(local_r13, Arg2, 1, v_rip + 12583733);
    *(uint8_t *)(arg1 + 0x1C) = (uint8_t)(result);
    result = MiMakeSystemAddressValid(v_stack_pE8, 0, (uint8_t)(result), 1);
    result = MiGetPage(v_stack_p38, (uint32_t)((uint32_t)(local_rbx)), 1, 1);
    *(uint64_t *)(v_stack_pD8) = result;
    if (result == -1) goto loc_0022D9D9;
loc_0022DA43:
    if (((*(uint64_t *)(v_stack_pE8)) & (0x401ULL)) == 0) goto loc_0022D4C0;
    goto loc_0022D932;
loc_0022DA60:
    local_rdi = (uint32_t)((v_stack_p50) + 1);
    if (((*(uint32_t *)(v_rip + 0xD97844)) & ((uint32_t)(local_rdi))) == 0) goto loc_0022DB3A;
loc_0022DA6E:
loc_0022DA70:
    if (!sign_flag) goto loc_0022D8AC;
    goto loc_0022DA60;
loc_0022DA7F:
    if (condition_is_below) goto loc_0022D548;
    v_stack_p20 = *(uint64_t *)(v_stack_pE8 + 0x8);
    result = KeBugCheckEx(26, (uint32_t)(0x411ULL), v_stack_pE8, local_rbx);
loc_0022DAAD:
    goto loc_0022D602;
loc_0022DAB5:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD98FFD)))) & (64)) == 0) goto loc_0022D7D9;
    result = KiCheckVpBackingLongSpinWaitHypercall(26, (uint32_t)(0x411ULL), v_stack_pE8, local_rbx);
    if ((uint8_t)(result) == 0) goto loc_0022D7D9;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_pE8)), (uint32_t)(0x411ULL), v_stack_pE8, local_rbx);
    goto loc_0022D7DB;
loc_0022DADD:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD98FD5)))) & (64)) == 0) goto loc_0022D819;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(v_stack_pE8)), (uint32_t)(0x411ULL), v_stack_pE8, local_rbx);
    if ((uint8_t)(result) == 0) goto loc_0022D819;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), (uint32_t)(0x411ULL), v_stack_pE8, local_rbx);
    goto loc_0022D81B;
loc_0022DB04:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD98FAE)))) & (64)) == 0) goto loc_0022D7FA;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbx)), (uint32_t)(0x411ULL), v_stack_pE8, local_rbx);
    Arg1 = 0;
    if ((uint8_t)(result) == 0) goto loc_0022DBB4;
    result = HvlNotifyLongSpinWait(0, (uint32_t)(0x411ULL), v_stack_pE8, local_rbx);
    Arg1 = 0;
    goto loc_0022D7FC;
loc_0022DB3A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD98F78)))) & (64)) == 0) goto loc_0022DA6E;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, (uint32_t)(0x411ULL), v_stack_pE8, local_rbx);
    Arg1 = 0;
    if ((uint8_t)(result) == 0) goto loc_0022DA6E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), (uint32_t)(0x411ULL), v_stack_pE8, local_rbx);
    Arg1 = 0;
    goto loc_0022DA70;
loc_0022DB65:
    *(uint64_t *)(v_stack_p60 + 0x8) = 1;
    goto loc_0022D3F2;
loc_0022DB78:
    result = MiFlushTbList(Arg1, (uint32_t)(0x411ULL), v_stack_pE8, local_rbx);
    result = MiReleaseProcessorFlushList(Arg1, (uint32_t)(0x411ULL), v_stack_pE8, local_rbx);
    *(uint64_t *)(arg1 + 0x68) = local_rdi;
    goto loc_0022D9E6;
loc_0022DB8B:
    result = (uint8_t)((*(uint8_t *)(v_stack_pE8 + 0x22)) & (7));
    v_stack_p30 = 0;
    Arg2 = 0;
    result = MiUnlinkPageFromListEx(v_stack_pE8, Arg2, v_stack_pE8, local_rbx);
loc_0022DBB4:
    goto loc_0022D7FA;
loc_0022DBC3:
    result = (uint8_t)((0) >> (2));
    result = (v_stack_p30) & (-5);
    v_stack_p30 = result;
loc_0022DBE9:
    local_rbx = 0;
    result = MiFlushTbList(*(uint64_t *)(arg1 + 0x68), Arg2, v_stack_pE8, local_rbx);
    result = MiReleaseProcessorFlushList(*(uint64_t *)(arg1 + 0x68), Arg2, v_stack_pE8, local_rbx);
    *(uint64_t *)(arg1 + 0x68) = 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `8` | `R` |
| `Arg1` | `+ 0x1C` | `8` | `W` |
| `Arg1` | `+ 0x20` | `64` | `R/W` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x38` | `128` | `R` |
| `Arg1` | `+ 0x38` | `128` | `W` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R/W` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R/W` |
| `Arg1` | `+ 0x60` | `32` | `W` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0022D34C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
