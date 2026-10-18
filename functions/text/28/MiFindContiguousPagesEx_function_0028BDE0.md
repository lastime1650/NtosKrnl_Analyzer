# MiFindContiguousPagesEx

- RVA: `0x0028BDE0`–`0x0028CE26` (길이 `4,166` bytes)
- VA: `0x000000014028BDE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00066FE0`
- 디코드: `956`개 명령, `4,166/4,166` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **38**; 고유 호출 대상: **31**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **29**

### Outgoing calls
- `0x0028BE84` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0028BEE1` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0028BF5E` → [MiAcquireNonPagedResources](MiAcquireNonPagedResources_function_00286C60.md) (function, `0x00286C60`)
- `0x0028BFBD` → [MiInitializePageColorBase](../32/MiInitializePageColorBase_function_00320410.md) (function, `0x00320410`)
- `0x0028BFE6` → [MiCreateUltraThreadContext](MiCreateUltraThreadContext_function_00288200.md) (function, `0x00288200`)
- `0x0028C027` → [MiReferencePageRuns](../37/MiReferencePageRuns_function_00379540.md) (function, `0x00379540`)
- `0x0028C144` → [MiCollapseRunTopDown](MiCollapseRunTopDown_function_0028CE30.md) (function, `0x0028CE30`)
- `0x0028C1E2` → [MiPfnsWorthTrying](../31/MiPfnsWorthTrying_function_0031B0C0.md) (function, `0x0031B0C0`)
- `0x0028C24C` → [MiAdjustCachedStacks](../2D/MiAdjustCachedStacks_function_002D8AAC.md) (function, `0x002D8AAC`)
- `0x0028C2DC` → [MiTradePage](MiTradePage_function_0028D160.md) (function, `0x0028D160`)
- `0x0028C362` → [MiIsPageOnBadList](../2B/MiIsPageOnBadList_function_002B1018.md) (function, `0x002B1018`)
- `0x0028C421` → [MiReleaseFreshPage](../33/MiReleaseFreshPage_function_00334AE0.md) (function, `0x00334AE0`)
- `0x0028C456` → [MiDereferencePageRuns](../3B/MiDereferencePageRuns_function_003BD388.md) (function, `0x003BD388`)
- `0x0028C462` → [MiDeleteUltraThreadContext](../32/MiDeleteUltraThreadContext_function_00322C90.md) (function, `0x00322C90`)
- `0x0028C474` → [MiReleaseNonPagedResources](../32/MiReleaseNonPagedResources_function_0032299C.md) (function, `0x0032299C`)
- `0x0028C485` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0028C4D5` → [MiDereferencePageRuns](../3B/MiDereferencePageRuns_function_003BD388.md) (function, `0x003BD388`)
- `0x0028C4E1` → [MiDeleteUltraThreadContext](../32/MiDeleteUltraThreadContext_function_00322C90.md) (function, `0x00322C90`)
- `0x0028C534` → [MiSufficientAvailablePages](../36/MiSufficientAvailablePages_function_0036D0B0.md) (function, `0x0036D0B0`)
- `0x0028C640` → [MiConvertContiguousPages](../29/MiConvertContiguousPages_function_0029F894.md) (function, `0x0029F894`)
- `0x0028C78A` → [MiFindLargeNodePage](../4D/MiFindLargeNodePage_function_004DB7E8.md) (function, `0x004DB7E8`)
- `0x0028C7C6` → [MiIsPageOnBadList](../2B/MiIsPageOnBadList_function_002B1018.md) (function, `0x002B1018`)
- `0x0028C7E8` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x0028C893` → [MiSetPfnOwnedAndActive](../46/MiSetPfnOwnedAndActive_function_004652AC.md) (function, `0x004652AC`)
- `0x0028C8E8` → [MiLockPageInline](../31/MiLockPageInline_function_0031A340.md) (function, `0x0031A340`)
- `0x0028C919` → [MiPageToNode](../33/MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)
- `0x0028C9BC` → [MiUnlockPage](../31/MiUnlockPage_function_0031A3E0.md) (function, `0x0031A3E0`)
- `0x0028CA0B` → [MiUpdateLargePageBitMap](../37/MiUpdateLargePageBitMap_function_0037619C.md) (function, `0x0037619C`)
- `0x0028CA32` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0028CA41` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0028CA5C` → [MiGetPfnPageSizeIndex](../31/MiGetPfnPageSizeIndex_function_0031C710.md) (function, `0x0031C710`)
- `0x0028CA6E` → [MiInitializeFoundLargeNodePage](../4F/MiInitializeFoundLargeNodePage_function_004F97E8.md) (function, `0x004F97E8`)
- `0x0028CAFB` → [MiFreeContiguousPages](../3F/MiFreeContiguousPages_function_003F7178.md) (function, `0x003F7178`)
- `0x0028CC2D` → [MiFindBestLargePageStealCandidates](../45/MiFindBestLargePageStealCandidates_function_00453EEC.md) (function, `0x00453EEC`)
- `0x0028CCAE` → [MiPfnsWorthTrying](../31/MiPfnsWorthTrying_function_0031B0C0.md) (function, `0x0031B0C0`)
- `0x0028CCD1` → [MiAdjustCachedStacks](../2D/MiAdjustCachedStacks_function_002D8AAC.md) (function, `0x002D8AAC`)
- `0x0028CD19` → [MiClaimPhysicalRun](MiClaimPhysicalRun_function_0028CF00.md) (function, `0x0028CF00`)
- `0x0028CDFC` → [qsort](../50/qsort_function_005009F0.md) (function, `0x005009F0`)

### Direct callers
- [MiAllocateMostlyContiguousPagesForMdl](../37/MiAllocateMostlyContiguousPagesForMdl_function_003769B0.md) at `0x00376B62`
- [MiAllocateSkipPagesForMdl](../3B/MiAllocateSkipPagesForMdl_function_003B7C08.md) at `0x003B7CEA`
- [MiRebuildLargePage](../3B/MiRebuildLargePage_function_003BBAEC.md) at `0x003BBC7B`
- [MiAllocateContiguousMemory](../3E/MiAllocateContiguousMemory_function_003E9FDC.md) at `0x003EA263`
- [MiIdealClusterPage](../4D/MiIdealClusterPage_function_004DB964.md) at `0x004DBF88`
- [MmMarkPhysicalMemoryAsBad](../67/MmMarkPhysicalMemoryAsBad_function_0067AA50.md) at `0x0067AE58`
- [sub_006E4582](../6E/Unknown_function_006E4582.md) at `0x006E463A`
- [MmRemovePhysicalMemory](../../page/7F/MmRemovePhysicalMemory_function_007FB560.md) at `0x007FB69E`
- [MiCreatePagefileMemoryExtents](../../page/80/MiCreatePagefileMemoryExtents_function_0080F1BC.md) at `0x0080F27C`
- [MiFindLargePageMemory](../../page/AA/MiFindLargePageMemory_function_00AA8334.md) at `0x00AA84F5`
- [sub_00B42C66](../../page/B4/Unknown_function_00B42C66.md) at `0x00B42CC3`

### Static image references
- `0x0028BDFC` → RVA `0x00E0A740` (`.data`; read)
- `0x0028BE8C` → RVA `0x00EF5140` (`.data`; read)
- `0x0028BEAA` → RVA `0x00EF5124` (`.data`; read)
- `0x0028BF01` → RVA `0x00FC5000` (`ALMOSTRO`; read)
- `0x0028C0B2` → RVA `0x00FC5002` (`ALMOSTRO`; read)
- `0x0028C23C` → RVA `0x00EF5328` (`.data`; read/write)
- `0x0028C349` → RVA `0x00E30088` (`.data`; read)
- `0x0028C3C3` → RVA `0x00EF5320` (`.data`; read/write)
- `0x0028C3F9` → RVA `0x00EF5324` (`.data`; write)
- `0x0028C5BA` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x0028C5DC` → RVA `0x00EF523C` (`.data`; read/write)
- `0x0028C69C` → RVA `0x00FC6B30` (`ALMOSTRO`; read)
- `0x0028C6A5` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0028C802` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0028C92F` → RVA `0x00E2DBD0` (`.data`; read)
- `0x0028CA24` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x0028CB60` → RVA `0x00EF5354` (`.data`; read)
- `0x0028CB67` → RVA `0x00EF5348` (`.data`; read)
- `0x0028CB6E` → RVA `0x00EF5360` (`.data`; read)
- `0x0028CB75` → RVA `0x00EF536C` (`.data`; read)
- `0x0028CB81` → RVA `0x00EF5358` (`.data`; read)
- `0x0028CB88` → RVA `0x00EF534C` (`.data`; read)
- `0x0028CB8F` → RVA `0x00EF5364` (`.data`; read)
- `0x0028CB96` → RVA `0x00EF5370` (`.data`; read)
- `0x0028CD35` → RVA `0x00EF5350` (`.data`; read)
- `0x0028CD3C` → RVA `0x00EF5344` (`.data`; read)
- `0x0028CD43` → RVA `0x00EF535C` (`.data`; read)
- `0x0028CD4A` → RVA `0x00EF5368` (`.data`; read)
- `0x0028CDE3` → RVA `0x004A94E0` (`MiSortBestStealCandidates`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0028C43E` → [sub_006DA40C](../6D/Unknown_function_006DA40C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0028BDE0  40 55                           push rbp
0028BDE2  53                              push rbx
0028BDE3  56                              push rsi
0028BDE4  57                              push rdi
0028BDE5  41 54                           push r12
0028BDE7  41 55                           push r13
0028BDE9  41 56                           push r14
0028BDEB  41 57                           push r15
0028BDED  48 8D AC 24 48 FE FF FF         lea rbp, [rsp - 0x1b8]
0028BDF5  48 81 EC B8 02 00 00            sub rsp, 0x2b8
0028BDFC  48 8B 05 3D E9 B7 00            mov rax, qword ptr [rip + 0xb7e93d]
0028BE03  48 33 C4                        xor rax, rsp
0028BE06  48 89 85 A0 01 00 00            mov qword ptr [rbp + 0x1a0], rax
0028BE0D  48 8B 85 28 02 00 00            mov rax, qword ptr [rbp + 0x228]
0028BE14  4C 8B F2                        mov r14, rdx
0028BE17  8B 9D 38 02 00 00               mov ebx, dword ptr [rbp + 0x238]
0028BE1D  4C 8B F9                        mov r15, rcx
0028BE20  48 8B BD 60 02 00 00            mov rdi, qword ptr [rbp + 0x260]
0028BE27  0F 57 C0                        xorps xmm0, xmm0
0028BE2A  44 8B AD 48 02 00 00            mov r13d, dword ptr [rbp + 0x248]
0028BE31  33 D2                           xor edx, edx
0028BE33  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0028BE38  49 8B F1                        mov rsi, r9
0028BE3B  8B 85 30 02 00 00               mov eax, dword ptr [rbp + 0x230]
0028BE41  89 45 A8                        mov dword ptr [rbp - 0x58], eax
0028BE44  48 8B 85 58 02 00 00            mov rax, qword ptr [rbp + 0x258]
0028BE4B  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
0028BE4F  48 8B 85 68 02 00 00            mov rax, qword ptr [rbp + 0x268]
0028BE56  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
0028BE5A  41 B8 80 00 00 00               mov r8d, 0x80
0028BE60  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
0028BE65  48 8D 8D 20 01 00 00            lea rcx, [rbp + 0x120]
0028BE6C  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
0028BE70  89 5C 24 70                     mov dword ptr [rsp + 0x70], ebx
0028BE74  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
0028BE79  48 89 7D A0                     mov qword ptr [rbp - 0x60], rdi
0028BE7D  0F 11 85 B0 00 00 00            movups xmmword ptr [rbp + 0xb0], xmm0
0028BE84  E8 B7 AD 43 00                  call 0x1406c6c40
0028BE89  45 33 E4                        xor r12d, r12d
0028BE8C  48 8D 0D AD 92 C6 00            lea rcx, [rip + 0xc692ad]
0028BE93  33 C0                           xor eax, eax
0028BE95  44 89 64 24 54                  mov dword ptr [rsp + 0x54], r12d
0028BE9A  0F 57 C0                        xorps xmm0, xmm0
0028BE9D  48 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], rax
0028BEA4  89 85 08 01 00 00               mov dword ptr [rbp + 0x108], eax
0028BEAA  8B 05 74 92 C6 00               mov eax, dword ptr [rip + 0xc69274]
0028BEB0  4C 89 65 F0                     mov qword ptr [rbp - 0x10], r12
0028BEB4  4C 89 65 F8                     mov qword ptr [rbp - 8], r12
0028BEB8  4C 89 65 08                     mov qword ptr [rbp + 8], r12
0028BEBC  4C 89 65 28                     mov qword ptr [rbp + 0x28], r12
0028BEC0  0F 11 85 D0 00 00 00            movups xmmword ptr [rbp + 0xd0], xmm0
0028BEC7  0F 11 85 E0 00 00 00            movups xmmword ptr [rbp + 0xe0], xmm0
0028BECE  0F 11 85 F0 00 00 00            movups xmmword ptr [rbp + 0xf0], xmm0
0028BED5  A8 01                           test al, 1
0028BED7  74 0D                           je 0x14028bee6
0028BED9  33 D2                           xor edx, edx
0028BEDB  41 B8 54 03 00 00               mov r8d, 0x354
0028BEE1  E8 5A AD 43 00                  call 0x1406c6c40
0028BEE6  48 85 FF                        test rdi, rdi
0028BEE9  74 04                           je 0x14028beef
0028BEEB  44 89 67 0C                     mov dword ptr [rdi + 0xc], r12d
0028BEEF  44 0F 20 C7                     mov rdi, cr8
0028BEF3  48 89 7D D8                     mov qword ptr [rbp - 0x28], rdi
0028BEF7  40 80 FF 02                     cmp dil, 2
0028BEFB  0F 87 63 07 00 00               ja 0x14028c664
0028BF01  0F B7 05 F8 90 D3 00            movzx eax, word ptr [rip + 0xd390f8]
0028BF08  3B D8                           cmp ebx, eax
0028BF0A  73 1B                           jae 0x14028bf27
0028BF0C  48 69 C3 80 DF 00 00            imul rax, rbx, 0xdf80
0028BF13  49 03 47 10                     add rax, qword ptr [r15 + 0x10]
0028BF17  48 8B 80 80 3A 00 00            mov rax, qword ptr [rax + 0x3a80]
0028BF1E  48 85 C0                        test rax, rax
0028BF21  0F 84 CA 06 00 00               je 0x14028c5f1
0028BF27  40 80 FF 02                     cmp dil, 2
0028BF2B  0F 84 4F 07 00 00               je 0x14028c680
0028BF31  65 8B 04 25 3C 3A 00 00         mov eax, dword ptr gs:[0x3a3c]
0028BF39  A9 01 00 01 00                  test eax, 0x10001
0028BF3E  0F 85 3C 07 00 00               jne 0x14028c680
0028BF44  B8 02 00 00 00                  mov eax, 2
0028BF49  41 0F BA E5 1D                  bt r13d, 0x1d
0028BF4E  72 1B                           jb 0x14028bf6b
0028BF50  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0028BF55  44 8B C8                        mov r9d, eax
0028BF58  45 33 C0                        xor r8d, r8d
0028BF5B  49 8B CF                        mov rcx, r15
0028BF5E  E8 FD AC FF FF                  call 0x140286c60
0028BF63  85 C0                           test eax, eax
0028BF65  0F 88 E5 05 00 00               js 0x14028c550
0028BF6B  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
0028BF6F  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0028BF74  48 85 C0                        test rax, rax
0028BF77  0F 85 CD 06 00 00               jne 0x14028c64a
0028BF7D  44 89 65 C0                     mov dword ptr [rbp - 0x40], r12d
0028BF81  41 F6 C5 40                     test r13b, 0x40
0028BF85  0F 85 03 07 00 00               jne 0x14028c68e
0028BF8B  41 8B 47 04                     mov eax, dword ptr [r15 + 4]
0028BF8F  A8 10                           test al, 0x10
0028BF91  0F 84 93 05 00 00               je 0x14028c52a
0028BF97  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0028BFA0  4C 8D 8D B0 00 00 00            lea r9, [rbp + 0xb0]
0028BFA7  45 8B C4                        mov r8d, r12d
0028BFAA  BA 03 00 00 00                  mov edx, 3
0028BFAF  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0028BFB6  48 81 C1 00 04 00 00            add rcx, 0x400
0028BFBD  E8 4E 44 09 00                  call 0x140320410
0028BFC2  40 80 FF 02                     cmp dil, 2
0028BFC6  48 8D 95 B0 00 00 00            lea rdx, [rbp + 0xb0]
0028BFCD  41 B9 04 00 00 00               mov r9d, 4
0028BFD3  48 8D 8D 20 01 00 00            lea rcx, [rbp + 0x120]
0028BFDA  BF 08 00 00 00                  mov edi, 8
0028BFDF  45 0F 45 CC                     cmovne r9d, r12d
0028BFE3  44 8B C7                        mov r8d, edi
0028BFE6  E8 15 C2 FF FF                  call 0x140288200
0028BFEB  85 C0                           test eax, eax
0028BFED  0F 84 22 0A 00 00               je 0x14028ca15
0028BFF3  41 8B C5                        mov eax, r13d
0028BFF6  8D 4F F9                        lea ecx, [rdi - 7]
0028BFF9  25 08 00 80 0B                  and eax, 0xb800008
0028BFFE  41 8B D4                        mov edx, r12d
0028C001  89 55 94                        mov dword ptr [rbp - 0x6c], edx
0028C004  3D 00 00 00 08                  cmp eax, 0x8000000
0028C009  0F 84 5F 06 00 00               je 0x14028c66e
0028C00F  0F B7 05 EA 8F D3 00            movzx eax, word ptr [rip + 0xd38fea]
0028C016  3B D8                           cmp ebx, eax
0028C018  72 08                           jb 0x14028c022
0028C01A  0F BA EB 1F                     bts ebx, 0x1f
0028C01E  89 5C 24 70                     mov dword ptr [rsp + 0x70], ebx
0028C022  8B D1                           mov edx, ecx
0028C024  49 8B CF                        mov rcx, r15
0028C027  E8 14 D5 0E 00                  call 0x140379540
0028C02C  4C 8B 55 A0                     mov r10, qword ptr [rbp - 0x60]
0028C030  48 8D 4E FF                     lea rcx, [rsi - 1]
0028C034  4C 8B C0                        mov r8, rax
0028C037  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
0028C03B  BB FF FF FF FF                  mov ebx, 0xffffffff
0028C040  4C 89 65 30                     mov qword ptr [rbp + 0x30], r12
0028C044  44 8B 08                        mov r9d, dword ptr [rax]
0028C047  49 FF C1                        inc r9
0028C04A  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0028C04E  49 C1 E1 04                     shl r9, 4
0028C052  4C 03 C8                        add r9, rax
0028C055  4C 89 75 00                     mov qword ptr [rbp], r14
0028C059  48 85 CE                        test rsi, rcx
0028C05C  4C 89 4D 58                     mov qword ptr [rbp + 0x58], r9
0028C060  49 8B C4                        mov rax, r12
0028C063  4C 89 65 20                     mov qword ptr [rbp + 0x20], r12
0028C067  48 0F 44 C6                     cmove rax, rsi
0028C06B  44 89 65 90                     mov dword ptr [rbp - 0x70], r12d
0028C06F  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
0028C074  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
0028C078  41 8B C5                        mov eax, r13d
0028C07B  C1 E8 0D                        shr eax, 0xd
0028C07E  24 01                           and al, 1
0028C080  48 89 75 18                     mov qword ptr [rbp + 0x18], rsi
0028C084  88 45 28                        mov byte ptr [rbp + 0x28], al
0028C087  44 89 64 24 60                  mov dword ptr [rsp + 0x60], r12d
0028C08C  49 BB 00 00 00 00 00 DE FF FF   movabs r11, 0xffffde0000000000
0028C096  4D 85 D2                        test r10, r10
0028C099  0F 85 77 0A 00 00               jne 0x14028cb16
0028C09F  4D 8B 77 10                     mov r14, qword ptr [r15 + 0x10]
0028C0A3  41 81 E5 00 20 00 00            and r13d, 0x2000
0028C0AA  4C 89 75 38                     mov qword ptr [rbp + 0x38], r14
0028C0AE  44 89 6D B0                     mov dword ptr [rbp - 0x50], r13d
0028C0B2  0F B6 3D 49 8F D3 00            movzx edi, byte ptr [rip + 0xd38f49]
0028C0B9  4D 8B CC                        mov r9, r12
0028C0BC  4C 89 65 88                     mov qword ptr [rbp - 0x78], r12
0028C0C0  40 80 FF 01                     cmp dil, 1
0028C0C4  0F 87 2C 08 00 00               ja 0x14028c8f6
0028C0CA  8B 74 24 70                     mov esi, dword ptr [rsp + 0x70]
0028C0CE  4C 8B 45 B8                     mov r8, qword ptr [rbp - 0x48]
0028C0D2  40 0F B6 CF                     movzx ecx, dil
0028C0D6  49 03 C9                        add rcx, r9
0028C0D9  48 89 4D 60                     mov qword ptr [rbp + 0x60], rcx
0028C0DD  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
0028C0E1  48 89 45 08                     mov qword ptr [rbp + 8], rax
0028C0E5  41 8B 00                        mov eax, dword ptr [r8]
0028C0E8  44 89 64 24 74                  mov dword ptr [rsp + 0x74], r12d
0028C0ED  85 C0                           test eax, eax
0028C0EF  0F 84 3C 03 00 00               je 0x14028c431
0028C0F5  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
0028C0F9  FF C8                           dec eax
0028C0FB  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
0028C0FF  8B 3C C1                        mov edi, dword ptr [rcx + rax*8]
0028C102  0F B6 54 C1 04                  movzx edx, byte ptr [rcx + rax*8 + 4]
0028C107  48 03 C0                        add rax, rax
0028C10A  49 8B 4C C0 10                  mov rcx, qword ptr [r8 + rax*8 + 0x10]
0028C10F  48 89 4D F0                     mov qword ptr [rbp - 0x10], rcx
0028C113  49 03 4C C0 18                  add rcx, qword ptr [r8 + rax*8 + 0x18]
0028C118  48 89 4D F8                     mov qword ptr [rbp - 8], rcx
0028C11C  48 39 4D 00                     cmp qword ptr [rbp], rcx
0028C120  0F 83 0B 03 00 00               jae 0x14028c431
0028C126  85 F6                           test esi, esi
0028C128  0F 89 EB 03 00 00               jns 0x14028c519
0028C12E  4D 85 C9                        test r9, r9
0028C131  74 0D                           je 0x14028c140
0028C133  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
0028C137  41 3A 11                        cmp dl, byte ptr [r9]
0028C13A  75 B1                           jne 0x14028c0ed
0028C13C  0F 1F 40 00                     nop dword ptr [rax]
0028C140  48 8D 4D F0                     lea rcx, [rbp - 0x10]
0028C144  E8 E7 0C 00 00                  call 0x14028ce30
0028C149  85 C0                           test eax, eax
0028C14B  0F 84 76 04 00 00               je 0x14028c5c7
0028C151  48 69 C7 80 DF 00 00            imul rax, rdi, 0xdf80
0028C158  49 03 47 10                     add rax, qword ptr [r15 + 0x10]
0028C15C  48 8B 80 80 3A 00 00            mov rax, qword ptr [rax + 0x3a80]
0028C163  48 85 C0                        test rax, rax
0028C166  0F 84 4E 04 00 00               je 0x14028c5ba
0028C16C  80 7D 28 00                     cmp byte ptr [rbp + 0x28], 0
0028C170  4C 8B 45 18                     mov r8, qword ptr [rbp + 0x18]
0028C174  48 8B 75 F8                     mov rsi, qword ptr [rbp - 8]
0028C178  4D 8B E8                        mov r13, r8
0028C17B  4C 89 45 80                     mov qword ptr [rbp - 0x80], r8
0028C17F  0F 85 E0 03 00 00               jne 0x14028c565
0028C185  48 8B 55 A0                     mov rdx, qword ptr [rbp - 0x60]
0028C189  4C 8B FE                        mov r15, rsi
0028C18C  4D 2B FD                        sub r15, r13
0028C18F  44 89 64 24 54                  mov dword ptr [rsp + 0x54], r12d
0028C194  4C 89 7D 40                     mov qword ptr [rbp + 0x40], r15
0028C198  4D 8B F4                        mov r14, r12
0028C19B  48 85 D2                        test rdx, rdx
0028C19E  0F 85 D8 03 00 00               jne 0x14028c57c
0028C1A4  4F 8D 24 7F                     lea r12, [r15 + r15*2]
0028C1A8  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0028C1B2  49 C1 E4 04                     shl r12, 4
0028C1B6  48 8B C0                        mov rax, rax
0028C1B9  4C 03 E0                        add r12, rax
0028C1BC  80 7D 28 00                     cmp byte ptr [rbp + 0x28], 0
0028C1C0  4C 89 65 D0                     mov qword ptr [rbp - 0x30], r12
0028C1C4  75 24                           jne 0x14028c1ea
0028C1C6  4D 85 F6                        test r14, r14
0028C1C9  75 24                           jne 0x14028c1ef
0028C1CB  44 8B 4C 24 50                  mov r9d, dword ptr [rsp + 0x50]
0028C1D0  48 8D 44 24 54                  lea rax, [rsp + 0x54]
0028C1D5  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0028C1DA  49 8B D4                        mov rdx, r12
0028C1DD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0028C1E2  E8 D9 EE 08 00                  call 0x14031b0c0
0028C1E7  4C 8B F0                        mov r14, rax
0028C1EA  4D 85 F6                        test r14, r14
0028C1ED  74 46                           je 0x14028c235
0028C1EF  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
0028C1F4  F6 44 24 54 02                  test byte ptr [rsp + 0x54], 2
0028C1F9  0F 85 5B 04 00 00               jne 0x14028c65a
0028C1FF  48 8B C6                        mov rax, rsi
0028C202  48 2B 45 F0                     sub rax, qword ptr [rbp - 0x10]
0028C206  4C 3B F0                        cmp r14, rax
0028C209  73 0E                           jae 0x14028c219
0028C20B  80 7D 28 00                     cmp byte ptr [rbp + 0x28], 0
0028C20F  75 15                           jne 0x14028c226
0028C211  49 2B C6                        sub rax, r14
0028C214  49 3B C5                        cmp rax, r13
0028C217  73 0D                           jae 0x14028c226
0028C219  48 8B C6                        mov rax, rsi
0028C21C  49 2B C6                        sub rax, r14
0028C21F  48 FF C8                        dec rax
0028C222  48 89 45 08                     mov qword ptr [rbp + 8], rax
0028C226  49 2B F6                        sub rsi, r14
0028C229  48 89 75 F8                     mov qword ptr [rbp - 8], rsi
0028C22D  45 33 E4                        xor r12d, r12d
0028C230  E9 0B FF FF FF                  jmp 0x14028c140
0028C235  F6 44 24 54 01                  test byte ptr [rsp + 0x54], 1
0028C23A  74 15                           je 0x14028c251
0028C23C  FF 05 E6 90 C6 00               inc dword ptr [rip + 0xc690e6]
0028C242  BA 01 00 00 00                  mov edx, 1
0028C247  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0028C24C  E8 5B C8 04 00                  call 0x1402d8aac
0028C251  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
0028C255  33 C9                           xor ecx, ecx
0028C257  48 89 85 A8 00 00 00            mov qword ptr [rbp + 0xa8], rax
0028C25E  49 8B F7                        mov rsi, r15
0028C261  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0028C266  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
0028C26A  48 8D 85 20 01 00 00            lea rax, [rbp + 0x120]
0028C271  48 89 45 78                     mov qword ptr [rbp + 0x78], rax
0028C275  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
0028C279  89 85 88 00 00 00               mov dword ptr [rbp + 0x88], eax
0028C27F  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
0028C283  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
0028C28A  4C 89 AD 80 00 00 00            mov qword ptr [rbp + 0x80], r13
0028C291  44 8B E9                        mov r13d, ecx
0028C294  48 89 8D 98 00 00 00            mov qword ptr [rbp + 0x98], rcx
0028C29B  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
0028C29F  89 8D 8C 00 00 00               mov dword ptr [rbp + 0x8c], ecx
0028C2A5  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
0028C2A9  48 C7 85 90 00 00 00 FF FF FF FF  mov qword ptr [rbp + 0x90], 0xffffffffffffffff
0028C2B4  4C 8B F1                        mov r14, rcx
0028C2B7  48 8D 04 49                     lea rax, [rcx + rcx*2]
0028C2BB  48 C1 E0 04                     shl rax, 4
0028C2BF  49 03 C4                        add rax, r12
0028C2C2  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
0028C2C6  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
0028C2D0  4C 8D 44 24 54                  lea r8, [rsp + 0x54]
0028C2D5  48 8B D6                        mov rdx, rsi
0028C2D8  48 8D 4D 70                     lea rcx, [rbp + 0x70]
0028C2DC  E8 7F 0E 00 00                  call 0x14028d160
0028C2E1  48 8B C8                        mov rcx, rax
0028C2E4  48 85 C0                        test rax, rax
0028C2E7  0F 84 96 00 00 00               je 0x14028c383
0028C2ED  48 29 85 80 00 00 00            sub qword ptr [rbp + 0x80], rax
0028C2F4  0F 84 E2 02 00 00               je 0x14028c5dc
0028C2FA  48 8D 04 49                     lea rax, [rcx + rcx*2]
0028C2FE  48 C7 85 90 00 00 00 FF FF FF FF  mov qword ptr [rbp + 0x90], 0xffffffffffffffff
0028C309  48 C1 E0 04                     shl rax, 4
0028C30D  48 03 F1                        add rsi, rcx
0028C310  4C 03 E0                        add r12, rax
0028C313  4C 3B 65 50                     cmp r12, qword ptr [rbp + 0x50]
0028C317  72 B7                           jb 0x14028c2d0
0028C319  83 7D B0 00                     cmp dword ptr [rbp - 0x50], 0
0028C31D  0F 84 A0 00 00 00               je 0x14028c3c3
0028C323  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
0028C327  45 33 E4                        xor r12d, r12d
0028C32A  48 85 C9                        test rcx, rcx
0028C32D  0F 85 8D 01 00 00               jne 0x14028c4c0
0028C333  4D 85 F6                        test r14, r14
0028C336  0F 84 95 01 00 00               je 0x14028c4d1
0028C33C  4C 8B 6D D0                     mov r13, qword ptr [rbp - 0x30]
0028C340  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
0028C345  49 8B 45 28                     mov rax, qword ptr [r13 + 0x28]
0028C349  48 8B 0D 38 3D BA 00            mov rcx, qword ptr [rip + 0xba3d38]
0028C350  48 C1 E8 2B                     shr rax, 0x2b
0028C354  25 FF 03 00 00                  and eax, 0x3ff
0028C359  4C 39 3C C1                     cmp qword ptr [rcx + rax*8], r15
0028C35D  75 17                           jne 0x14028c376
0028C35F  49 8B CD                        mov rcx, r13
0028C362  E8 B1 4C 02 00                  call 0x1402b1018
0028C367  85 C0                           test eax, eax
0028C369  0F 85 3B 04 00 00               jne 0x14028c7aa
0028C36F  C7 45 90 01 00 00 00            mov dword ptr [rbp - 0x70], 1
0028C376  48 8B 75 F8                     mov rsi, qword ptr [rbp - 8]
0028C37A  4C 8B 6D 80                     mov r13, qword ptr [rbp - 0x80]
0028C37E  E9 71 FE FF FF                  jmp 0x14028c1f4
0028C383  48 8B 95 98 00 00 00            mov rdx, qword ptr [rbp + 0x98]
0028C38A  41 B8 01 00 00 00               mov r8d, 1
0028C390  41 8B C8                        mov ecx, r8d
0028C393  49 3B D0                        cmp rdx, r8
0028C396  0F 87 7F 04 00 00               ja 0x14028c81b
0028C39C  45 85 ED                        test r13d, r13d
0028C39F  0F 84 FA 00 00 00               je 0x14028c49f
0028C3A5  83 7D B0 00                     cmp dword ptr [rbp - 0x50], 0
0028C3A9  74 18                           je 0x14028c3c3
0028C3AB  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
0028C3AF  49 03 C7                        add rax, r15
0028C3B2  48 2B C6                        sub rax, rsi
0028C3B5  48 3B C8                        cmp rcx, rax
0028C3B8  0F 82 3C FF FF FF               jb 0x14028c2fa
0028C3BE  E9 60 FF FF FF                  jmp 0x14028c323
0028C3C3  FF 05 57 8F C6 00               inc dword ptr [rip + 0xc68f57]
0028C3C9  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0028C3D3  48 8B C0                        mov rax, rax
0028C3D6  48 8B 75 80                     mov rsi, qword ptr [rbp - 0x80]
0028C3DA  49 8B CC                        mov rcx, r12
0028C3DD  48 2B B5 80 00 00 00            sub rsi, qword ptr [rbp + 0x80]
0028C3E4  48 2B C8                        sub rcx, rax
0028C3E7  48 C1 F9 04                     sar rcx, 4
0028C3EB  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
0028C3F5  48 0F AF C8                     imul rcx, rax
0028C3F9  89 0D 25 8F C6 00               mov dword ptr [rip + 0xc68f25], ecx
0028C3FF  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
0028C403  48 85 C9                        test rcx, rcx
0028C406  74 09                           je 0x14028c411
0028C408  69 C6 00 F0 FF FF               imul eax, esi, 0xfffff000
0028C40E  01 41 28                        add dword ptr [rcx + 0x28], eax
0028C411  48 85 F6                        test rsi, rsi
0028C414  0F 84 0D FF FF FF               je 0x14028c327
0028C41A  49 83 EC 30                     sub r12, 0x30
0028C41E  49 8B CC                        mov rcx, r12
0028C421  E8 BA 86 0A 00                  call 0x140334ae0
0028C426  48 83 EE 01                     sub rsi, 1
0028C42A  75 EE                           jne 0x14028c41a
0028C42C  E9 F2 FE FF FF                  jmp 0x14028c323
0028C431  4D 85 C9                        test r9, r9
0028C434  0F 85 70 04 00 00               jne 0x14028c8aa
0028C43A  83 7D 94 00                     cmp dword ptr [rbp - 0x6c], 0
0028C43E  0F 85 C8 DF 44 00               jne 0x1406da40c
0028C444  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
0028C449  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
0028C44E  49 8B C8                        mov rcx, r8
0028C451  BF 17 00 00 C0                  mov edi, 0xc0000017
0028C456  E8 2D 0F 13 00                  call 0x1403bd388
0028C45B  48 8D 8D 20 01 00 00            lea rcx, [rbp + 0x120]
0028C462  E8 29 68 09 00                  call 0x140322c90
0028C467  41 0F BA E5 1D                  bt r13d, 0x1d
0028C46C  72 0B                           jb 0x14028c479
0028C46E  48 8B D6                        mov rdx, rsi
0028C471  49 8B CF                        mov rcx, r15
0028C474  E8 23 65 09 00                  call 0x14032299c
0028C479  8B C7                           mov eax, edi
0028C47B  48 8B 8D A0 01 00 00            mov rcx, qword ptr [rbp + 0x1a0]
0028C482  48 33 CC                        xor rcx, rsp
0028C485  E8 B6 01 42 00                  call 0x1406ac640
0028C48A  48 81 C4 B8 02 00 00            add rsp, 0x2b8
0028C491  41 5F                           pop r15
0028C493  41 5E                           pop r14
0028C495  41 5D                           pop r13
0028C497  41 5C                           pop r12
0028C499  5F                              pop rdi
0028C49A  5E                              pop rsi
0028C49B  5B                              pop rbx
0028C49C  5D                              pop rbp
0028C49D  C3                              ret
0028C49E  CC                              int3
0028C49F  48 85 D2                        test rdx, rdx
0028C4A2  74 14                           je 0x14028c4b8
0028C4A4  4C 8B 75 80                     mov r14, qword ptr [rbp - 0x80]
0028C4A8  48 8D 42 FF                     lea rax, [rdx - 1]
0028C4AC  48 F7 D0                        not rax
0028C4AF  4D 03 F7                        add r14, r15
0028C4B2  48 23 C6                        and rax, rsi
0028C4B5  4C 2B F0                        sub r14, rax
0028C4B8  45 8B E8                        mov r13d, r8d
0028C4BB  E9 E5 FE FF FF                  jmp 0x14028c3a5
0028C4C0  8B 49 28                        mov ecx, dword ptr [rcx + 0x28]
0028C4C3  8B 45 C0                        mov eax, dword ptr [rbp - 0x40]
0028C4C6  C1 E9 0C                        shr ecx, 0xc
0028C4C9  3B C8                           cmp ecx, eax
0028C4CB  0F 85 89 00 00 00               jne 0x14028c55a
0028C4D1  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
0028C4D5  E8 AE 0E 13 00                  call 0x1403bd388
0028C4DA  48 8D 8D 20 01 00 00            lea rcx, [rbp + 0x120]
0028C4E1  E8 AA 67 09 00                  call 0x140322c90
0028C4E6  8B 7C 24 50                     mov edi, dword ptr [rsp + 0x50]
0028C4EA  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
0028C4EF  0F BA E7 0D                     bt edi, 0xd
0028C4F3  0F 83 0F 01 00 00               jae 0x14028c608
0028C4F9  48 8B 75 D0                     mov rsi, qword ptr [rbp - 0x30]
0028C4FD  44 8B 75 A8                     mov r14d, dword ptr [rbp - 0x58]
0028C501  0F BA E7 1E                     bt edi, 0x1e
0028C505  0F 83 3E 03 00 00               jae 0x14028c849
0028C50B  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0028C50F  4C 89 38                        mov qword ptr [rax], r15
0028C512  33 C0                           xor eax, eax
0028C514  E9 62 FF FF FF                  jmp 0x14028c47b
0028C519  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
0028C51D  3B FE                           cmp edi, esi
0028C51F  0F 84 09 FC FF FF               je 0x14028c12e
0028C525  E9 C3 FB FF FF                  jmp 0x14028c0ed
0028C52A  48 81 C2 A0 00 00 00            add rdx, 0xa0
0028C531  49 8B CF                        mov rcx, r15
0028C534  E8 77 0B 0E 00                  call 0x14036d0b0
0028C539  85 C0                           test eax, eax
0028C53B  0F 85 56 FA FF FF               jne 0x14028bf97
0028C541  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
0028C546  BF 9A 00 00 C0                  mov edi, 0xc000009a
0028C54B  E9 0B FF FF FF                  jmp 0x14028c45b
0028C550  B8 9A 00 00 C0                  mov eax, 0xc000009a
0028C555  E9 21 FF FF FF                  jmp 0x14028c47b
0028C55A  2B C1                           sub eax, ecx
0028C55C  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
0028C560  E9 D7 FD FF FF                  jmp 0x14028c33c
0028C565  48 8B C6                        mov rax, rsi
0028C568  48 2B 45 F0                     sub rax, qword ptr [rbp - 0x10]
0028C56C  4C 3B E8                        cmp r13, rax
0028C56F  4C 0F 47 E8                     cmova r13, rax
0028C573  4C 89 6D 80                     mov qword ptr [rbp - 0x80], r13
0028C577  E9 09 FC FF FF                  jmp 0x14028c185
0028C57C  8B 4A 04                        mov ecx, dword ptr [rdx + 4]
0028C57F  85 C9                           test ecx, ecx
0028C581  0F 84 1D FC FF FF               je 0x14028c1a4
0028C587  44 8B 4C 24 74                  mov r9d, dword ptr [rsp + 0x74]
0028C58C  44 3B C9                        cmp r9d, ecx
0028C58F  0F 83 0F FC FF FF               jae 0x14028c1a4
0028C595  41 8B C1                        mov eax, r9d
0028C598  4C 3B 7C C2 18                  cmp r15, qword ptr [rdx + rax*8 + 0x18]
0028C59D  0F 82 01 04 00 00               jb 0x14028c9a4
0028C5A3  0F 85 FB FB FF FF               jne 0x14028c1a4
0028C5A9  4C 8B 75 10                     mov r14, qword ptr [rbp + 0x10]
0028C5AD  41 FF C1                        inc r9d
0028C5B0  44 89 4C 24 74                  mov dword ptr [rsp + 0x74], r9d
0028C5B5  E9 EA FB FF FF                  jmp 0x14028c1a4
0028C5BA  F6 05 C7 A4 D3 00 30            test byte ptr [rip + 0xd3a4c7], 0x30
0028C5C1  0F 84 A5 FB FF FF               je 0x14028c16c
0028C5C7  8B 74 24 70                     mov esi, dword ptr [rsp + 0x70]
0028C5CB  4C 8B 45 B8                     mov r8, qword ptr [rbp - 0x48]
0028C5CF  4C 8B 4D 88                     mov r9, qword ptr [rbp - 0x78]
0028C5D3  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
0028C5D7  E9 11 FB FF FF                  jmp 0x14028c0ed
0028C5DC  FF 05 5A 8C C6 00               inc dword ptr [rip + 0xc68c5a]
0028C5E2  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
0028C5E6  45 33 E4                        xor r12d, r12d
0028C5E9  45 8B F4                        mov r14d, r12d
0028C5EC  E9 39 FD FF FF                  jmp 0x14028c32a
0028C5F1  F6 05 90 A4 D3 00 30            test byte ptr [rip + 0xd3a490], 0x30
0028C5F8  0F 84 29 F9 FF FF               je 0x14028bf27
0028C5FE  B8 17 00 00 C0                  mov eax, 0xc0000017
0028C603  E9 73 FE FF FF                  jmp 0x14028c47b
0028C608  49 8D 97 FF 01 00 00            lea rdx, [r15 + 0x1ff]
0028C60F  4E 8D 04 3B                     lea r8, [rbx + r15]
0028C613  48 81 E2 00 FE FF FF            and rdx, 0xfffffffffffffe00
0028C61A  49 81 E0 00 FE FF FF            and r8, 0xfffffffffffffe00
0028C621  49 3B D0                        cmp rdx, r8
0028C624  0F 82 B4 03 00 00               jb 0x14028c9de
0028C62A  48 8B 75 D0                     mov rsi, qword ptr [rbp - 0x30]
0028C62E  48 8B D3                        mov rdx, rbx
0028C631  44 8B 75 A8                     mov r14d, dword ptr [rbp - 0x58]
0028C635  48 8B CE                        mov rcx, rsi
0028C638  44 0F B6 4D D8                  movzx r9d, byte ptr [rbp - 0x28]
0028C63D  45 8B C6                        mov r8d, r14d
0028C640  E8 4F 32 01 00                  call 0x14029f894
0028C645  E9 B7 FE FF FF                  jmp 0x14028c501
0028C64A  8B 40 28                        mov eax, dword ptr [rax + 0x28]
0028C64D  C1 E8 0C                        shr eax, 0xc
0028C650  03 C2                           add eax, edx
0028C652  89 45 C0                        mov dword ptr [rbp - 0x40], eax
0028C655  E9 27 F9 FF FF                  jmp 0x14028bf81
0028C65A  83 4C 24 60 01                  or dword ptr [rsp + 0x60], 1
0028C65F  E9 9B FB FF FF                  jmp 0x14028c1ff
0028C664  B8 BB 00 00 C0                  mov eax, 0xc00000bb
0028C669  E9 0D FE FF FF                  jmp 0x14028c47b
0028C66E  F6 05 13 A4 D3 00 30            test byte ptr [rip + 0xd3a413], 0x30
0028C675  0F 45 D1                        cmovne edx, ecx
0028C678  89 55 94                        mov dword ptr [rbp - 0x6c], edx
0028C67B  E9 8F F9 FF FF                  jmp 0x14028c00f
0028C680  41 83 CD 08                     or r13d, 8
0028C684  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
0028C689  E9 B6 F8 FF FF                  jmp 0x14028bf44
0028C68E  49 81 FE 00 00 10 00            cmp r14, 0x100000
0028C695  75 05                           jne 0x14028c69c
0028C697  41 0F BA ED 0F                  bts r13d, 0xf
0028C69C  48 0F BA 25 8B A4 D3 00 25      bt qword ptr [rip + 0xd3a48b], 0x25
0028C6A5  4C 8D 35 54 39 D7 FF            lea r14, [rip - 0x28c6ac]
0028C6AC  45 8B C4                        mov r8d, r12d
0028C6AF  49 8D 8E 60 1C 01 00            lea rcx, [r14 + 0x11c60]
0028C6B6  41 B9 01 00 00 00               mov r9d, 1
0028C6BC  45 0F 43 C1                     cmovae r8d, r9d
0028C6C0  4A 8D 0C C1                     lea rcx, [rcx + r8*8]
0028C6C4  48 3B 11                        cmp rdx, qword ptr [rcx]
0028C6C7  74 0D                           je 0x14028c6d6
0028C6C9  41 FF C0                        inc r8d
0028C6CC  48 83 C1 08                     add rcx, 8
0028C6D0  41 83 F8 03                     cmp r8d, 3
0028C6D4  72 EE                           jb 0x14028c6c4
0028C6D6  44 0F B7 1D 22 89 D3 00         movzx r11d, word ptr [rip + 0xd38922]
0028C6DE  48 8D 95 D0 00 00 00            lea rdx, [rbp + 0xd0]
0028C6E5  83 E2 04                        and edx, 4
0028C6E8  0F 85 1C 04 00 00               jne 0x14028cb0a
0028C6EE  48 85 D2                        test rdx, rdx
0028C6F1  48 8D 85 D4 00 00 00            lea rax, [rbp + 0xd4]
0028C6F8  4C 8D 95 D0 00 00 00            lea r10, [rbp + 0xd0]
0028C6FF  49 8B C9                        mov rcx, r9
0028C702  4C 0F 45 D0                     cmovne r10, rax
0028C706  49 8B C3                        mov rax, r11
0028C709  48 C1 E0 20                     shl rax, 0x20
0028C70D  49 8B FA                        mov rdi, r10
0028C710  49 0B C3                        or rax, r11
0028C713  F3 48 AB                        rep stosq qword ptr [rdi], rax
0028C716  48 85 D2                        test rdx, rdx
0028C719  75 13                           jne 0x14028c72e
0028C71B  BF 08 00 00 00                  mov edi, 8
0028C720  41 B9 04 00 00 00               mov r9d, 4
0028C726  44 0F 44 CF                     cmove r9d, edi
0028C72A  47 89 1C 11                     mov dword ptr [r9 + r10], r11d
0028C72E  41 8B CC                        mov ecx, r12d
0028C731  83 F9 03                        cmp ecx, 3
0028C734  73 20                           jae 0x14028c756
0028C736  8B C1                           mov eax, ecx
0028C738  48 8D 04 C5 00 00 00 00         lea rax, [rax*8]
0028C740  4A 3B B4 30 60 1C 01 00         cmp rsi, qword ptr [rax + r14 + 0x11c60]
0028C748  0F 85 9D 03 00 00               jne 0x14028caeb
0028C74E  4E 8B A4 30 D0 EC E0 00         mov r12, qword ptr [rax + r14 + 0xe0ecd0]
0028C756  44 8B 75 A8                     mov r14d, dword ptr [rbp - 0x58]
0028C75A  48 8D 85 D0 00 00 00            lea rax, [rbp + 0xd0]
0028C761  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0028C766  0F 57 C0                        xorps xmm0, xmm0
0028C769  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
0028C76E  45 8B C8                        mov r9d, r8d
0028C771  8B D3                           mov edx, ebx
0028C773  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
0028C778  49 8B CF                        mov rcx, r15
0028C77B  66 0F 7F 85 00 01 00 00         movdqa xmmword ptr [rbp + 0x100], xmm0
0028C783  4C 89 A5 F8 00 00 00            mov qword ptr [rbp + 0xf8], r12
0028C78A  E8 59 F0 24 00                  call 0x1404db7e8
0028C78F  48 8B F8                        mov rdi, rax
0028C792  48 85 C0                        test rax, rax
0028C795  0F 85 BE 02 00 00               jne 0x14028ca59
0028C79B  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
0028C7A0  BF 17 00 00 C0                  mov edi, 0xc0000017
0028C7A5  E9 B1 FC FF FF                  jmp 0x14028c45b
0028C7AA  80 7D D8 02                     cmp byte ptr [rbp - 0x28], 2
0028C7AE  0F 85 31 01 00 00               jne 0x14028c8e5
0028C7B4  41 B7 11                        mov r15b, 0x11
0028C7B7  41 8B F4                        mov esi, r12d
0028C7BA  F0 49 0F BA 6D 18 3F            lock bts qword ptr [r13 + 0x18], 0x3f
0028C7C1  72 3D                           jb 0x14028c800
0028C7C3  49 8B CD                        mov rcx, r13
0028C7C6  E8 4D 48 02 00                  call 0x1402b1018
0028C7CB  85 C0                           test eax, eax
0028C7CD  0F 84 47 06 00 00               je 0x14028ce1a
0028C7D3  F7 44 24 50 00 00 00 10         test dword ptr [rsp + 0x50], 0x10000000
0028C7DB  0F 85 D4 01 00 00               jne 0x14028c9b5
0028C7E1  41 0F B6 D7                     movzx edx, r15b
0028C7E5  49 8B CD                        mov rcx, r13
0028C7E8  E8 F3 DB 08 00                  call 0x14031a3e0
0028C7ED  48 8B 75 F8                     mov rsi, qword ptr [rbp - 8]
0028C7F1  4C 8B 6D 80                     mov r13, qword ptr [rbp - 0x80]
0028C7F5  E9 F5 F9 FF FF                  jmp 0x14028c1ef
0028C7FA  66 0F 1F 44 00 00               nop word ptr [rax + rax]
0028C800  FF C6                           inc esi
0028C802  85 35 A4 8A D3 00               test dword ptr [rip + 0xd38aa4], esi
0028C808  0F 84 16 02 00 00               je 0x14028ca24
0028C80E  F3 90                           pause
0028C810  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
0028C814  48 85 C0                        test rax, rax
0028C817  79 A1                           jns 0x14028c7ba
0028C819  EB E5                           jmp 0x14028c800
0028C81B  4C 8D 42 FF                     lea r8, [rdx - 1]
0028C81F  49 F7 D0                        not r8
0028C822  49 8B C0                        mov rax, r8
0028C825  48 23 C6                        and rax, rsi
0028C828  48 3B F0                        cmp rsi, rax
0028C82B  0F 84 1A 02 00 00               je 0x14028ca4b
0028C831  48 8D 4A FF                     lea rcx, [rdx - 1]
0028C835  48 03 CE                        add rcx, rsi
0028C838  49 23 C8                        and rcx, r8
0028C83B  41 B8 01 00 00 00               mov r8d, 1
0028C841  48 2B CE                        sub rcx, rsi
0028C844  E9 53 FB FF FF                  jmp 0x14028c39c
0028C849  0F BA E7 14                     bt edi, 0x14
0028C84D  41 BF 00 00 00 00               mov r15d, 0
0028C853  48 8D 3C 5B                     lea rdi, [rbx + rbx*2]
0028C857  8B 9D 50 02 00 00               mov ebx, dword ptr [rbp + 0x250]
0028C85D  41 0F 92 C7                     setb r15b
0028C861  48 C1 E7 04                     shl rdi, 4
0028C865  83 CB 04                        or ebx, 4
0028C868  48 03 FE                        add rdi, rsi
0028C86B  66 41 FF C7                     inc r15w
0028C86F  80 7D D8 02                     cmp byte ptr [rbp - 0x28], 2
0028C873  0F 45 9D 50 02 00 00            cmovne ebx, dword ptr [rbp + 0x250]
0028C87A  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
0028C87E  45 8B CE                        mov r9d, r14d
0028C881  49 C7 C0 F8 FF FF FF            mov r8, 0xfffffffffffffff8
0028C888  66 44 89 7C 24 20               mov word ptr [rsp + 0x20], r15w
0028C88E  8B D3                           mov edx, ebx
0028C890  48 8B CE                        mov rcx, rsi
0028C893  E8 14 8A 1D 00                  call 0x1404652ac
0028C898  48 83 C6 30                     add rsi, 0x30
0028C89C  48 3B F7                        cmp rsi, rdi
0028C89F  75 D9                           jne 0x14028c87a
0028C8A1  4C 8B 7D 40                     mov r15, qword ptr [rbp + 0x40]
0028C8A5  E9 61 FC FF FF                  jmp 0x14028c50b
0028C8AA  49 FF C1                        inc r9
0028C8AD  4C 89 4D 88                     mov qword ptr [rbp - 0x78], r9
0028C8B1  4C 3B 4D 60                     cmp r9, qword ptr [rbp + 0x60]
0028C8B5  0F 82 22 F8 FF FF               jb 0x14028c0dd
0028C8BB  83 FB FF                        cmp ebx, -1
0028C8BE  0F 84 76 FB FF FF               je 0x14028c43a
0028C8C4  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
0028C8C8  48 83 C2 04                     add rdx, 4
0028C8CC  48 89 55 E0                     mov qword ptr [rbp - 0x20], rdx
0028C8D0  48 3B 55 30                     cmp rdx, qword ptr [rbp + 0x30]
0028C8D4  0F 84 60 FB FF FF               je 0x14028c43a
0028C8DA  8B 1A                           mov ebx, dword ptr [rdx]
0028C8DC  4C 8B 75 38                     mov r14, qword ptr [rbp + 0x38]
0028C8E0  E9 CD F7 FF FF                  jmp 0x14028c0b2
0028C8E5  49 8B CD                        mov rcx, r13
0028C8E8  E8 53 DA 08 00                  call 0x14031a340
0028C8ED  44 0F B6 F8                     movzx r15d, al
0028C8F1  E9 CD FE FF FF                  jmp 0x14028c7c3
0028C8F6  8B 74 24 70                     mov esi, dword ptr [rsp + 0x70]
0028C8FA  85 F6                           test esi, esi
0028C8FC  0F 89 99 00 00 00               jns 0x14028c99b
0028C902  83 FB FF                        cmp ebx, -1
0028C905  75 3F                           jne 0x14028c946
0028C907  49 8B 87 48 48 00 00            mov rax, qword ptr [r15 + 0x4848]
0028C90E  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
0028C912  48 3B C8                        cmp rcx, rax
0028C915  48 0F 47 C8                     cmova rcx, rax
0028C919  E8 B2 C3 0A 00                  call 0x140338cd0
0028C91E  0F B7 15 DB 86 D3 00            movzx edx, word ptr [rip + 0xd386db]
0028C925  8B D8                           mov ebx, eax
0028C927  8B CA                           mov ecx, edx
0028C929  4D 8B CC                        mov r9, r12
0028C92C  0F AF C8                        imul ecx, eax
0028C92F  48 8B 05 9A 12 BA 00            mov rax, qword ptr [rip + 0xba129a]
0028C936  4C 8D 04 88                     lea r8, [rax + rcx*4]
0028C93A  49 8D 04 90                     lea rax, [r8 + rdx*4]
0028C93E  4C 89 45 E0                     mov qword ptr [rbp - 0x20], r8
0028C942  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
0028C946  8B C3                           mov eax, ebx
0028C948  48 69 C8 80 DF 00 00            imul rcx, rax, 0xdf80
0028C94F  49 03 CE                        add rcx, r14
0028C952  8B 81 50 3B 00 00               mov eax, dword ptr [rcx + 0x3b50]
0028C958  A8 01                           test al, 1
0028C95A  0F 84 6E F7 FF FF               je 0x14028c0ce
0028C960  80 BD 40 02 00 00 00            cmp byte ptr [rbp + 0x240], 0
0028C967  4C 8D 89 83 3B 00 00            lea r9, [rcx + 0x3b83]
0028C96E  4C 89 4D 88                     mov qword ptr [rbp - 0x78], r9
0028C972  0F 85 56 F7 FF FF               jne 0x14028c0ce
0028C978  41 8B C4                        mov eax, r12d
0028C97B  40 84 FF                        test dil, dil
0028C97E  74 13                           je 0x14028c993
0028C980  41 80 39 00                     cmp byte ptr [r9], 0
0028C984  74 09                           je 0x14028c98f
0028C986  49 FF C1                        inc r9
0028C989  FF C0                           inc eax
0028C98B  3B C7                           cmp eax, edi
0028C98D  72 F1                           jb 0x14028c980
0028C98F  4C 89 4D 88                     mov qword ptr [rbp - 0x78], r9
0028C993  40 B7 01                        mov dil, 1
0028C996  E9 33 F7 FF FF                  jmp 0x14028c0ce
0028C99B  48 69 CE 80 DF 00 00            imul rcx, rsi, 0xdf80
0028C9A2  EB AB                           jmp 0x14028c94f
0028C9A4  48 8B 55 A0                     mov rdx, qword ptr [rbp - 0x60]
0028C9A8  41 FF C1                        inc r9d
0028C9AB  44 89 4C 24 74                  mov dword ptr [rsp + 0x74], r9d
0028C9B0  E9 D7 FB FF FF                  jmp 0x14028c58c
0028C9B5  41 0F B6 D7                     movzx edx, r15b
0028C9B9  49 8B CD                        mov rcx, r13
0028C9BC  E8 1F DA 08 00                  call 0x14031a3e0
0028C9C1  4C 8B 45 B8                     mov r8, qword ptr [rbp - 0x48]
0028C9C5  41 8B C4                        mov eax, r12d
0028C9C8  4C 8B 4D 88                     mov r9, qword ptr [rbp - 0x78]
0028C9CC  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
0028C9D1  8B 74 24 70                     mov esi, dword ptr [rsp + 0x70]
0028C9D5  44 89 65 94                     mov dword ptr [rbp - 0x6c], r12d
0028C9D9  E9 0F F7 FF FF                  jmp 0x14028c0ed
0028C9DE  8B C7                           mov eax, edi
0028C9E0  25 00 10 00 80                  and eax, 0x80001000
0028C9E5  3D 00 10 00 80                  cmp eax, 0x80001000
0028C9EA  0F 84 3A FC FF FF               je 0x14028c62a
0028C9F0  80 7D D8 02                     cmp byte ptr [rbp - 0x28], 2
0028C9F4  41 B9 07 00 00 00               mov r9d, 7
0028C9FA  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0028C9FF  B8 03 00 00 00                  mov eax, 3
0028CA04  44 0F 45 C8                     cmovne r9d, eax
0028CA08  4C 2B C2                        sub r8, rdx
0028CA0B  E8 8C 97 0E 00                  call 0x14037619c
0028CA10  E9 15 FC FF FF                  jmp 0x14028c62a
0028CA15  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
0028CA1A  BF 9A 00 00 C0                  mov edi, 0xc000009a
0028CA1F  E9 37 FA FF FF                  jmp 0x14028c45b
0028CA24  8B 05 8E A0 D3 00               mov eax, dword ptr [rip + 0xd3a08e]
0028CA2A  A8 40                           test al, 0x40
0028CA2C  0F 84 DC FD FF FF               je 0x14028c80e
0028CA32  E8 59 2A 08 00                  call 0x14030f490
0028CA37  84 C0                           test al, al
0028CA39  0F 84 CF FD FF FF               je 0x14028c80e
0028CA3F  8B CE                           mov ecx, esi
0028CA41  E8 1A 2A 08 00                  call 0x14030f460
0028CA46  E9 C5 FD FF FF                  jmp 0x14028c810
0028CA4B  48 8B CA                        mov rcx, rdx
0028CA4E  41 B8 01 00 00 00               mov r8d, 1
0028CA54  E9 43 F9 FF FF                  jmp 0x14028c39c
0028CA59  48 8B CF                        mov rcx, rdi
0028CA5C  E8 AF FC 08 00                  call 0x14031c710
0028CA61  44 8B 85 50 02 00 00            mov r8d, dword ptr [rbp + 0x250]
0028CA68  41 8B D5                        mov edx, r13d
0028CA6B  48 8B CF                        mov rcx, rdi
0028CA6E  E8 75 CD 26 00                  call 0x1404f97e8
0028CA73  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0028CA7D  48 8B C0                        mov rax, rax
0028CA80  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
0028CA85  48 2B F8                        sub rdi, rax
0028CA88  48 C1 FF 04                     sar rdi, 4
0028CA8C  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
0028CA96  48 0F AF F8                     imul rdi, rax
0028CA9A  48 8D 46 FF                     lea rax, [rsi - 1]
0028CA9E  48 03 C7                        add rax, rdi
0028CAA1  48 3B 45 C8                     cmp rax, qword ptr [rbp - 0x38]
0028CAA5  77 4B                           ja 0x14028caf2
0028CAA7  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0028CAAB  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
0028CAAF  48 89 38                        mov qword ptr [rax], rdi
0028CAB2  48 85 D2                        test rdx, rdx
0028CAB5  74 2D                           je 0x14028cae4
0028CAB7  8B 4A 28                        mov ecx, dword ptr [rdx + 0x28]
0028CABA  48 C1 E9 0C                     shr rcx, 0xc
0028CABE  48 83 C1 06                     add rcx, 6
0028CAC2  48 8D 0C CA                     lea rcx, [rdx + rcx*8]
0028CAC6  48 85 F6                        test rsi, rsi
0028CAC9  74 13                           je 0x14028cade
0028CACB  48 8B C6                        mov rax, rsi
0028CACE  48 89 39                        mov qword ptr [rcx], rdi
0028CAD1  48 8D 49 08                     lea rcx, [rcx + 8]
0028CAD5  48 FF C7                        inc rdi
0028CAD8  48 83 E8 01                     sub rax, 1
0028CADC  75 F0                           jne 0x14028cace
0028CADE  C1 E6 0C                        shl esi, 0xc
0028CAE1  01 72 28                        add dword ptr [rdx + 0x28], esi
0028CAE4  33 C0                           xor eax, eax
0028CAE6  E9 90 F9 FF FF                  jmp 0x14028c47b
0028CAEB  FF C1                           inc ecx
0028CAED  E9 3F FC FF FF                  jmp 0x14028c731
0028CAF2  45 33 C0                        xor r8d, r8d
0028CAF5  48 8B D6                        mov rdx, rsi
0028CAF8  48 8B CF                        mov rcx, rdi
0028CAFB  E8 78 A6 16 00                  call 0x1403f7178
0028CB00  BF 17 00 00 C0                  mov edi, 0xc0000017
0028CB05  E9 51 F9 FF FF                  jmp 0x14028c45b
0028CB0A  44 89 9D D0 00 00 00            mov dword ptr [rbp + 0xd0], r11d
0028CB11  E9 D8 FB FF FF                  jmp 0x14028c6ee
0028CB16  84 C0                           test al, al
0028CB18  75 20                           jne 0x14028cb3a
0028CB1A  80 3D E1 84 D3 00 01            cmp byte ptr [rip + 0xd384e1], 1
0028CB21  75 17                           jne 0x14028cb3a
0028CB23  4D 3B 47 20                     cmp r8, qword ptr [r15 + 0x20]
0028CB27  75 11                           jne 0x14028cb3a
0028CB29  49 83 7A 10 FF                  cmp qword ptr [r10 + 0x10], -1
0028CB2E  75 13                           jne 0x14028cb43
0028CB30  41 8B 42 04                     mov eax, dword ptr [r10 + 4]
0028CB34  41 39 42 08                     cmp dword ptr [r10 + 8], eax
0028CB38  72 09                           jb 0x14028cb43
0028CB3A  4D 89 62 04                     mov qword ptr [r10 + 4], r12
0028CB3E  E9 5C F5 FF FF                  jmp 0x14028c09f
0028CB43  41 B8 02 00 00 00               mov r8d, 2
0028CB49  48 83 FE 10                     cmp rsi, 0x10
0028CB4D  74 2F                           je 0x14028cb7e
0028CB4F  48 81 FE 00 02 00 00            cmp rsi, 0x200
0028CB56  0F 85 D9 01 00 00               jne 0x14028cd35
0028CB5C  45 8D 60 FF                     lea r12d, [r8 - 1]
0028CB60  4C 8D 2D ED 87 C6 00            lea r13, [rip + 0xc687ed]
0028CB67  4C 8D 3D DA 87 C6 00            lea r15, [rip + 0xc687da]
0028CB6E  48 8D 35 EB 87 C6 00            lea rsi, [rip + 0xc687eb]
0028CB75  48 8D 05 F0 87 C6 00            lea rax, [rip + 0xc687f0]
0028CB7C  EB 1F                           jmp 0x14028cb9d
0028CB7E  45 8B E0                        mov r12d, r8d
0028CB81  4C 8D 2D D0 87 C6 00            lea r13, [rip + 0xc687d0]
0028CB88  4C 8D 3D BD 87 C6 00            lea r15, [rip + 0xc687bd]
0028CB8F  48 8D 35 CE 87 C6 00            lea rsi, [rip + 0xc687ce]
0028CB96  48 8D 05 D3 87 C6 00            lea rax, [rip + 0xc687d3]
0028CB9D  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0028CBA1  48 8D 0D 98 85 C6 00            lea rcx, [rip + 0xc68598]
0028CBA8  41 8B C4                        mov eax, r12d
0028CBAB  BA 01 00 00 00                  mov edx, 1
0028CBB0  4C 89 7D B0                     mov qword ptr [rbp - 0x50], r15
0028CBB4  89 54 24 74                     mov dword ptr [rsp + 0x74], edx
0028CBB8  4C 8D 0C 85 00 00 00 00         lea r9, [rax*4]
0028CBC0  41 FF 84 09 EC 01 00 00         inc dword ptr [r9 + rcx + 0x1ec]
0028CBC8  41 8B 4A 08                     mov ecx, dword ptr [r10 + 8]
0028CBCC  41 8B 42 04                     mov eax, dword ptr [r10 + 4]
0028CBD0  4C 89 4D 88                     mov qword ptr [rbp - 0x78], r9
0028CBD4  3B C8                           cmp ecx, eax
0028CBD6  0F 82 7A 01 00 00               jb 0x14028cd56
0028CBDC  45 33 C0                        xor r8d, r8d
0028CBDF  44 89 44 24 78                  mov dword ptr [rsp + 0x78], r8d
0028CBE4  44 3B C2                        cmp r8d, edx
0028CBE7  0F 83 EC 01 00 00               jae 0x14028cdd9
0028CBED  3B C8                           cmp ecx, eax
0028CBEF  75 6F                           jne 0x14028cc60
0028CBF1  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
0028CBF5  48 8D 05 44 85 C6 00            lea rax, [rip + 0xc68544]
0028CBFC  41 FF 84 01 F8 01 00 00         inc dword ptr [r9 + rax + 0x1f8]
0028CC04  45 8B C4                        mov r8d, r12d
0028CC07  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
0028CC0B  4D 8B CE                        mov r9, r14
0028CC0E  48 8B 55 B8                     mov rdx, qword ptr [rbp - 0x48]
0028CC12  4C 89 54 24 30                  mov qword ptr [rsp + 0x30], r10
0028CC17  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0028CC1B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0028CC20  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0028CC25  41 C7 42 08 00 00 00 00         mov dword ptr [r10 + 8], 0
0028CC2D  E8 BA 72 1C 00                  call 0x140453eec
0028CC32  4C 8B 55 A0                     mov r10, qword ptr [rbp - 0x60]
0028CC36  4C 8B 4D 88                     mov r9, qword ptr [rbp - 0x78]
0028CC3A  49 BB 00 00 00 00 00 DE FF FF   movabs r11, 0xffffde0000000000
0028CC44  41 83 7A 04 00                  cmp dword ptr [r10 + 4], 0
0028CC49  0F 84 19 01 00 00               je 0x14028cd68
0028CC4F  41 FF 07                        inc dword ptr [r15]
0028CC52  0F 1F 40 00                     nop dword ptr [rax]
0028CC56  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
0028CC60  41 8B 4A 08                     mov ecx, dword ptr [r10 + 8]
0028CC64  41 8B 42 04                     mov eax, dword ptr [r10 + 4]
0028CC68  3B C8                           cmp ecx, eax
0028CC6A  0F 83 54 01 00 00               jae 0x14028cdc4
0028CC70  4D 8B 7C CA 18                  mov r15, qword ptr [r10 + rcx*8 + 0x18]
0028CC75  8D 41 01                        lea eax, [rcx + 1]
0028CC78  4C 89 7D 40                     mov qword ptr [rbp + 0x40], r15
0028CC7C  41 89 42 08                     mov dword ptr [r10 + 8], eax
0028CC80  4B 8D 0C 7F                     lea rcx, [r15 + r15*2]
0028CC84  48 C1 E1 04                     shl rcx, 4
0028CC88  49 8B C3                        mov rax, r11
0028CC8B  44 8B 4C 24 50                  mov r9d, dword ptr [rsp + 0x50]
0028CC90  48 03 C8                        add rcx, rax
0028CC93  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
0028CC98  48 8D 44 24 54                  lea rax, [rsp + 0x54]
0028CC9D  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0028CCA1  48 8B D1                        mov rdx, rcx
0028CCA4  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0028CCA9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0028CCAE  E8 0D E4 08 00                  call 0x14031b0c0
0028CCB3  48 85 C0                        test rax, rax
0028CCB6  0F 85 B5 00 00 00               jne 0x14028cd71
0028CCBC  F6 44 24 54 01                  test byte ptr [rsp + 0x54], 1
0028CCC1  74 13                           je 0x14028ccd6
0028CCC3  FF 05 5F 86 C6 00               inc dword ptr [rip + 0xc6865f]
0028CCC9  8D 50 01                        lea edx, [rax + 1]
0028CCCC  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0028CCD1  E8 D6 BD 04 00                  call 0x1402d8aac
0028CCD6  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
0028CCDA  48 8D 44 24 54                  lea rax, [rsp + 0x54]
0028CCDF  4C 8B 4D C8                     mov r9, qword ptr [rbp - 0x38]
0028CCE3  49 8B D7                        mov rdx, r15
0028CCE6  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
0028CCEB  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0028CCF0  33 C0                           xor eax, eax
0028CCF2  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0028CCF7  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0028CCFC  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0028CD01  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0028CD05  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
0028CD09  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0028CD0D  48 8D 85 20 01 00 00            lea rax, [rbp + 0x120]
0028CD14  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0028CD19  E8 E2 01 00 00                  call 0x14028cf00
0028CD1E  48 85 C0                        test rax, rax
0028CD21  75 74                           jne 0x14028cd97
0028CD23  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
0028CD27  FF 06                           inc dword ptr [rsi]
0028CD29  C7 40 0C 01 00 00 00            mov dword ptr [rax + 0xc], 1
0028CD30  E9 9C F7 FF FF                  jmp 0x14028c4d1
0028CD35  4C 8D 2D 14 86 C6 00            lea r13, [rip + 0xc68614]
0028CD3C  4C 8D 3D 01 86 C6 00            lea r15, [rip + 0xc68601]
0028CD43  48 8D 35 12 86 C6 00            lea rsi, [rip + 0xc68612]
0028CD4A  48 8D 05 17 86 C6 00            lea rax, [rip + 0xc68617]
0028CD51  E9 47 FE FF FF                  jmp 0x14028cb9d
0028CD56  49 83 7A 10 FF                  cmp qword ptr [r10 + 0x10], -1
0028CD5B  41 0F 45 D0                     cmovne edx, r8d
0028CD5F  89 54 24 74                     mov dword ptr [rsp + 0x74], edx
0028CD63  E9 74 FE FF FF                  jmp 0x14028cbdc
0028CD68  41 FF 45 00                     inc dword ptr [r13]
0028CD6C  E9 EF FE FF FF                  jmp 0x14028cc60
0028CD71  4C 8B 4D 88                     mov r9, qword ptr [rbp - 0x78]
0028CD75  48 8D 05 C4 83 C6 00            lea rax, [rip + 0xc683c4]
0028CD7C  4C 8B 55 A0                     mov r10, qword ptr [rbp - 0x60]
0028CD80  49 BB 00 00 00 00 00 DE FF FF   movabs r11, 0xffffde0000000000
0028CD8A  41 FF 84 01 28 02 00 00         inc dword ptr [r9 + rax + 0x228]
0028CD92  E9 C9 FE FF FF                  jmp 0x14028cc60
0028CD97  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
0028CD9B  4C 8B 4D 88                     mov r9, qword ptr [rbp - 0x78]
0028CD9F  4C 8B 55 A0                     mov r10, qword ptr [rbp - 0x60]
0028CDA3  49 BB 00 00 00 00 00 DE FF FF   movabs r11, 0xffffde0000000000
0028CDAD  FF 02                           inc dword ptr [rdx]
0028CDAF  F6 44 24 54 02                  test byte ptr [rsp + 0x54], 2
0028CDB4  0F 84 A6 FE FF FF               je 0x14028cc60
0028CDBA  83 4C 24 60 01                  or dword ptr [rsp + 0x60], 1
0028CDBF  E9 9C FE FF FF                  jmp 0x14028cc60
0028CDC4  44 8B 44 24 78                  mov r8d, dword ptr [rsp + 0x78]
0028CDC9  4C 8B 7D B0                     mov r15, qword ptr [rbp - 0x50]
0028CDCD  41 FF C0                        inc r8d
0028CDD0  8B 54 24 74                     mov edx, dword ptr [rsp + 0x74]
0028CDD4  E9 06 FE FF FF                  jmp 0x14028cbdf
0028CDD9  41 8B C4                        mov eax, r12d
0028CDDC  48 8D 0D 5D 83 C6 00            lea rcx, [rip + 0xc6835d]
0028CDE3  4C 8D 0D F6 C6 21 00            lea r9, [rip + 0x21c6f6]
0028CDEA  4C 8B C7                        mov r8, rdi
0028CDED  FF 84 81 34 02 00 00            inc dword ptr [rcx + rax*4 + 0x234]
0028CDF4  49 8D 4A 18                     lea rcx, [r10 + 0x18]
0028CDF8  41 8B 52 04                     mov edx, dword ptr [r10 + 4]
0028CDFC  E8 EF 3B 27 00                  call 0x1405009f0
0028CE01  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
0028CE06  45 33 E4                        xor r12d, r12d
0028CE09  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
0028CE0E  C7 45 90 01 00 00 00            mov dword ptr [rbp - 0x70], 1
0028CE15  E9 85 F2 FF FF                  jmp 0x14028c09f
0028CE1A  C7 45 90 01 00 00 00            mov dword ptr [rbp - 0x70], 1
0028CE21  E9 BB F9 FF FF                  jmp 0x14028c7e1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFindContiguousPagesEx(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, unsigned int a8, unsigned __int8 a9, unsigned int a10, unsigned int a11, __int64 a12, __int64 a13, __int64 a14)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m124;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m16C;
    unsigned int v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned int v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned int v_stack_m248;
    unsigned int v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned int v_stack_m264;
    unsigned int v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned int v_stack_m280;
    unsigned int v_stack_m284;
    unsigned int v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned int v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned int v_stack_m2A4;
    unsigned int v_stack_m2A8;
    unsigned __int64 v_stack_m2D8;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p54;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p70;
    unsigned int v_stack_p74;
    unsigned int v_stack_p78;

    v_rsp = (v_rsp) - (696);
    result = (*(unsigned __int64 *)(v_rip + 12052797)) ^ (v_rsp);
    v_stack_m58 = result;
    a2 = 0;
    v_stack_m2A0 = a6;
    v_stack_m250 = (unsigned int)((unsigned int)(a7));
    v_stack_m260 = a12;
    v_stack_m230 = a3;
    v_stack_m290 = a1;
    v_stack_m1B0 = a14;
    v_stack_m288 = (unsigned int)((unsigned int)(a8));
    v_stack_m2A8 = (unsigned int)((unsigned int)(a10));
    v_stack_m258 = a13;
    v_stack_m148 = v_xmm0;
    result = memset(v_stack_mD8, a2, 128, a4);
    v_r12 = 0;
    result = 0;
    v_stack_m2A4 = 0;
    v_stack_mF8 = 0;
    v_stack_mF0 = 0;
    v_stack_m208 = 0;
    v_stack_m200 = 0;
    v_stack_m1F0 = 0;
    v_stack_m1D0 = 0;
    v_stack_m128 = v_xmm0;
    v_stack_m118 = v_xmm0;
    v_stack_m108 = v_xmm0;
    result = (unsigned int)(*(unsigned int *)(v_rip + 13013620));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13013620)))) & (1)) != 0) {
        a2 = 0;
        a3 = 852;
        result = memset(v_rip + 13013677, a2, a3, a4);
    }
    if (a13 != 0) {
        *(unsigned int *)(a13 + 12) = 0;
    }
    v_stack_m220 = v_cr8;
    if (((unsigned __int8)(v_cr8)) > 2) goto loc_0028C664;
    if (((unsigned int)((unsigned int)(a8))) >= ((unsigned int)(*(unsigned __int16 *)(v_rip + 13865208)))) goto loc_0028BF27;
    result = (*(unsigned __int16 *)(v_rip + 13865208)) * ((unsigned int)(a8));
    result = (result) + (*(unsigned __int64 *)(a1 + 16));
    if (*(unsigned __int64 *)(result + 14976) == 0) goto loc_0028C5F1;
loc_0028BF27:
    if (((unsigned __int8)(v_cr8)) == 2) goto loc_0028C680;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 14908))))) & (0x10001ULL)) != 0) goto loc_0028C680;
loc_0028BF44:
    if (condition_is_below) goto loc_0028BF6B;
    a3 = 0;
    result = MiAcquireNonPagedResources(a1, v_stack_m2A0, a3, 2);
    if (sign_flag) goto loc_0028C550;
loc_0028BF6B:
    if (v_stack_m260 != 0) goto loc_0028C64A;
    v_stack_m238 = 0;
loc_0028BF81:
    if ((((unsigned __int8)((unsigned int)(a10))) & (64)) != 0) goto loc_0028C68E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 4)))) & (16)) == 0) goto loc_0028C52A;
loc_0028BF97:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    result = MiInitializePageColorBase(a1, 3, 0, v_stack_m148);
    a4 = 4;
    if (((unsigned __int8)(v_cr8)) != 2) { a4 = 0; }
    result = MiCreateUltraThreadContext(v_stack_mD8, v_stack_m148, 8, a4);
    if ((unsigned int)(result) == 0) goto loc_0028CA15;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a10)))) & (0xB800008ULL));
    v_stack_m264 = 0;
    if (((unsigned int)(result)) == 0x8000000ULL) goto loc_0028C66E;
loc_0028C00F:
    if (((unsigned int)((unsigned int)(a8))) >= ((unsigned int)(*(unsigned __int16 *)(v_rip + 13864938)))) {
        v_stack_m288 = (unsigned int)((unsigned int)(a8));
    }
    result = MiReferencePageRuns(a1, (unsigned int)((unsigned int)(8 - 7)), 8, a4);
    v_stack_m240 = result;
    v_stack_m1C8 = 0;
    a4 = ((unsigned int)(*(unsigned int *)(result))) + 1;
    v_stack_m218 = 0;
    a4 = (a4) << (4);
    a4 = (a4) + (result);
    v_stack_m1F8 = 0;
    v_stack_m1A0 = a4;
    v_stack_m1D8 = 0;
    result = 0;
    if (((a4) & (a4 - 1)) == 0) { result = a4; }
    v_stack_m268 = 0;
    v_stack_m1E8 = result;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a10)))) >> (13));
    result = (unsigned __int8)((result) & (1));
    v_stack_m1E0 = v_stack_m2A0;
    v_stack_m1D0 = (unsigned __int8)(result);
    v_stack_m298 = 0;
    if (v_stack_m258 != 0) goto loc_0028CB16;
loc_0028C09F:
    v_r13 = (unsigned int)(((unsigned int)(a10)) & (0x2000ULL));
    v_stack_m1C0 = *(unsigned __int64 *)(a1 + 16);
    v_stack_m248 = (unsigned int)(v_r13);
loc_0028C0B2:
    v_stack_m270 = 0;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rip + 13864777))) > 1) goto loc_0028C8F6;
loc_0028C0CE:
    a1 = ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 13864777))) + (0);
    v_stack_m198 = a1;
loc_0028C0DD:
    v_stack_m1F0 = v_stack_m230;
    v_stack_m284 = 0;
loc_0028C0ED:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m240))) == 0) goto loc_0028C431;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m240))) - 1);
    v_stack_m280 = (unsigned int)(result);
    result = (result) + (result);
    v_stack_m208 = *(unsigned __int64 *)(v_stack_m240 + result * 8 + 16);
    a1 = (*(unsigned __int64 *)(v_stack_m240 + result * 8 + 16)) + (*(unsigned __int64 *)(v_stack_m240 + result * 8 + 24));
    v_stack_m200 = a1;
    if (v_stack_m1F8 >= a1) goto loc_0028C431;
    if (!sign_flag) goto loc_0028C519;
loc_0028C12E:
    if (0 == 0) goto loc_0028C140;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_stack_m1A0 + result * 8 + 4))) != (*(unsigned __int8 *)(0))) goto loc_0028C0ED;
loc_0028C140:
    result = MiCollapseRunTopDown(v_stack_m208, *(unsigned __int8 *)(v_stack_m1A0 + result * 8 + 4), v_stack_m240, 0);
    if ((unsigned int)(result) == 0) goto loc_0028C5C7;
    result = (result) * ((unsigned int)(*(unsigned int *)(v_stack_m1A0 + result * 8)));
    result = (result) + (*(unsigned __int64 *)(a1 + 16));
    if (*(unsigned __int64 *)(result + 14976) == 0) goto loc_0028C5BA;
loc_0028C16C:
    v_stack_m278 = v_stack_m1E0;
    if (v_stack_m1D0 != 0) goto loc_0028C565;
loc_0028C185:
    v_r15 = (v_stack_m200) - (v_stack_m1E0);
    v_stack_m2A4 = 0;
    v_stack_m1B8 = v_r15;
    if (v_stack_m258 != 0) goto loc_0028C57C;
loc_0028C1A4:
    v_r12 = (v_r15 + v_r15 * 2) << (4);
    v_r12 = (v_r12) + (*(unsigned __int64 *)(result + 14976));
    v_stack_m228 = v_r12;
    if (v_stack_m1D0 != 0) goto loc_0028C1EA;
    if (0 != 0) goto loc_0028C1EF;
    v_stack_m2D8 = v_stack_m2A4;
    result = MiPfnsWorthTrying(v_stack_m290, v_r12, v_stack_m1E0, (unsigned int)(v_stack_m2A8));
loc_0028C1EA:
    if (result == 0) goto loc_0028C235;
loc_0028C1EF:
loc_0028C1F4:
    if (((v_stack_m2A4) & (2)) != 0) goto loc_0028C65A;
loc_0028C1FF:
    result = (v_stack_m200) - (v_stack_m208);
    if (result >= result) goto loc_0028C219;
    if (v_stack_m1D0 != 0) goto loc_0028C226;
    result = (result) - (result);
    if (result < v_stack_m1E0) {
        result = v_stack_m200;
        result = (result) - (result);
        result = (result) - 1;
        v_stack_m1F0 = result;
    }
    v_rsi = (v_stack_m200) - (result);
    v_stack_m200 = v_rsi;
    v_r12 = 0;
    goto loc_0028C140;
loc_0028C235:
    if (((v_stack_m2A4) & (1)) != 0) {
        a2 = 1;
        a1 = v_stack_m290;
        result = MiAdjustCachedStacks(a1, a2, v_stack_m1E0, (unsigned int)(v_stack_m2A8));
    }
    a1 = 0;
    v_stack_m150 = v_stack_m260;
    v_stack_m188 = v_stack_m290;
    v_stack_m180 = v_stack_mD8;
    v_stack_m170 = (unsigned int)((unsigned int)(v_stack_m2A8));
    v_stack_m158 = v_stack_m1F0;
    v_stack_m178 = v_stack_m1E0;
    v_stack_m160 = 0;
    v_stack_m2A4 = 0;
    v_stack_m16C = 0;
    v_stack_m168 = -1;
    result = (v_stack_m278 + v_stack_m278 * 2) << (4);
    result = (result) + (0);
    v_stack_m1A8 = result;
loc_0028C2D0:
    result = MiTradePage(v_stack_m188, v_stack_m290, v_stack_m2A4, (unsigned int)(v_stack_m2A8));
    if (result == 0) goto loc_0028C383;
    if (result == 0) goto loc_0028C5DC;
loc_0028C2FA:
    v_stack_m168 = -1;
    result = (result + result * 2) << (4);
    v_rsi = (v_stack_m290) + (result);
    v_r12 = (v_r12) + (result);
    if (v_r12 < v_stack_m1A8) goto loc_0028C2D0;
    if (v_stack_m248 == 0) goto loc_0028C3C3;
loc_0028C323:
loc_0028C327:
    v_r12 = 0;
loc_0028C32A:
    if (v_stack_m260 != 0) goto loc_0028C4C0;
    if (v_stack_m278 == 0) goto loc_0028C4D1;
loc_0028C33C:
    result = (*(unsigned __int64 *)(v_stack_m228 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12205368) + result * 8)) != v_stack_m290) goto loc_0028C376;
    result = MiIsPageOnBadList(v_stack_m228, v_stack_m290, v_stack_m2A4, (unsigned int)(v_stack_m2A8));
    if ((unsigned int)(result) != 0) goto loc_0028C7AA;
    v_stack_m268 = 1;
loc_0028C376:
    goto loc_0028C1F4;
loc_0028C383:
    if (v_stack_m160 > 1) goto loc_0028C81B;
loc_0028C39C:
    if ((unsigned int)(v_stack_m278) == 0) goto loc_0028C49F;
loc_0028C3A5:
    if (v_stack_m248 == 0) goto loc_0028C3C3;
    result = (v_stack_m278) + (v_stack_m290);
    result = (result) - (v_stack_m200);
    if (1 < result) goto loc_0028C2FA;
    goto loc_0028C323;
loc_0028C3C3:
    v_rsi = (v_stack_m278) - (v_stack_m178);
    a1 = (0) - (result);
    a1 = (a1) >> (4);
    a1 = (a1) * (result);
    *(unsigned int *)(v_rip + 13012773) = (unsigned int)(a1);
    if (v_stack_m260 != 0) {
        result = (unsigned int)((result) * ((unsigned int)(v_rsi)));
    }
    if (v_rsi == 0) goto loc_0028C327;
loc_0028C41A:
    v_r12 = (v_r12) - (48);
    result = MiReleaseFreshPage(v_r12, v_stack_m160, 1, (unsigned int)(v_stack_m2A8));
    v_rsi = (v_rsi) - (1);
    if (condition_is_not_equal) goto loc_0028C41A;
    goto loc_0028C323;
loc_0028C431:
    if ((unsigned int)(v_stack_m2A8) != 0) goto loc_0028C8AA;
loc_0028C43A:
    result = MiDereferencePageRuns(1, v_stack_m160, 1, (unsigned int)(v_stack_m2A8));
loc_0028C45B:
    result = MiDeleteUltraThreadContext(v_stack_mD8, v_stack_m160, 1, (unsigned int)(v_stack_m2A8));
    if (v_stack_m264 >= 0) {
        a2 = v_stack_m2A0;
        a1 = v_stack_m290;
        result = MiReleaseNonPagedResources(a1, a2, 1, (unsigned int)(v_stack_m2A8));
    }
loc_0028C47B:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 1, (unsigned int)(v_stack_m2A8));
    v_rsp = (v_rsp) + (696);
    return result;
loc_0028C49F:
    v_r14 = v_stack_m278;
    if (a2 != 0) {
        v_r14 = v_stack_m278;
        result = a2 - 1;
        result = ~(result);
        v_r14 = (v_r14) + (v_stack_m290);
        result = (result) & (v_stack_m2A0);
        v_r14 = (v_r14) - (result);
    }
    goto loc_0028C3A5;
loc_0028C4C0:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 40))) >> (12));
    if (((unsigned int)(a1)) != ((unsigned int)((unsigned int)(v_stack_m238)))) goto loc_0028C55A;
loc_0028C4D1:
    result = MiDereferencePageRuns(v_stack_m240, a2, 1, (unsigned int)(v_stack_m2A8));
    result = MiDeleteUltraThreadContext(v_stack_mD8, a2, 1, (unsigned int)(v_stack_m2A8));
    if (((unsigned int)(a1)) >= ((unsigned int)((unsigned int)(v_stack_m238)))) goto loc_0028C608;
loc_0028C501:
    if (((unsigned int)(a1)) >= ((unsigned int)((unsigned int)(v_stack_m238)))) goto loc_0028C849;
loc_0028C50B:
    *(unsigned __int64 *)(v_stack_m1B0) = v_stack_m290;
    result = 0;
    goto loc_0028C47B;
loc_0028C519:
    if (((unsigned int)((unsigned int)(v_stack_p50))) == ((unsigned int)(v_stack_m228))) goto loc_0028C12E;
    goto loc_0028C0ED;
loc_0028C52A:
    a2 = (a2) + (160);
    result = MiSufficientAvailablePages(v_stack_m290, a2, 1, (unsigned int)(v_stack_m2A8));
    if ((unsigned int)(result) != 0) goto loc_0028BF97;
    goto loc_0028C45B;
loc_0028C550:
    goto loc_0028C47B;
loc_0028C55A:
    result = (unsigned int)(((unsigned int)(0xC000009AULL)) - ((unsigned int)(v_stack_m290)));
    v_stack_m1E0 = result;
    goto loc_0028C33C;
loc_0028C565:
    result = (v_stack_p58) - (v_stack_m208);
    v_r13 = 1;
    if (1 > result) { v_r13 = result; }
    v_stack_m278 = v_r13;
    goto loc_0028C185;
loc_0028C57C:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4))) == 0) goto loc_0028C1A4;
loc_0028C58C:
    if (((unsigned int)((unsigned int)(v_stack_p74))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 4))))) goto loc_0028C1A4;
    if (v_stack_m290 < (*(unsigned __int64 *)(a2 + (unsigned int)((unsigned int)((unsigned int)(v_stack_p74))) * 8 + 24))) goto loc_0028C9A4;
    if (v_stack_m290 != (*(unsigned __int64 *)(a2 + (unsigned int)((unsigned int)((unsigned int)(v_stack_p74))) * 8 + 24))) goto loc_0028C1A4;
    a4 = (unsigned int)(((unsigned int)(v_stack_p74)) + 1);
    v_stack_p74 = (unsigned int)(a4);
    goto loc_0028C1A4;
loc_0028C5BA:
    if (((*(unsigned __int8 *)(v_rip + 13870279)) & (48)) == 0) goto loc_0028C16C;
loc_0028C5C7:
    goto loc_0028C0ED;
loc_0028C5DC:
    v_r12 = 0;
    goto loc_0028C32A;
loc_0028C5F1:
    if (((*(unsigned __int8 *)(v_rip + 13870224)) & (48)) == 0) goto loc_0028BF27;
    goto loc_0028C47B;
loc_0028C608:
    a2 = (v_stack_m290 + 511) & (-512);
    a3 = (v_stack_p58 + v_stack_m290 * 1) & (-512);
    if (a2 < a3) goto loc_0028C9DE;
loc_0028C62A:
    result = MiConvertContiguousPages(v_stack_m228, v_stack_p58, (unsigned int)((unsigned int)((unsigned int)(v_stack_m250))), v_stack_m220);
    goto loc_0028C501;
loc_0028C64A:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 40))) >> (12));
    result = (unsigned int)((result) + ((unsigned int)(v_stack_p58)));
    v_stack_m238 = (unsigned int)(result);
    goto loc_0028BF81;
loc_0028C65A:
    goto loc_0028C1FF;
loc_0028C664:
    goto loc_0028C47B;
loc_0028C66E:
    a2 = v_stack_p58;
    if (((*(unsigned __int8 *)(v_rip + 13870099)) & (48)) != 0) { a2 = (unsigned int)(v_stack_m228); }
    v_stack_m264 = (unsigned int)(a2);
    goto loc_0028C00F;
loc_0028C680:
    v_r13 = (unsigned int)((v_r13) | (8));
    v_stack_p50 = (unsigned int)(v_r13);
    goto loc_0028BF44;
loc_0028C68E:
    if (((unsigned int)(v_stack_m250)) == 0x100000ULL) {
    }
    a3 = 0;
    if (((unsigned int)(v_stack_m250)) >= 0x100000ULL) { a3 = 1; }
loc_0028C6C4:
    if (a2 == (*(unsigned __int64 *)(v_rip - 2672300 + 72800 + a3 * 8))) goto loc_0028C6D6;
    a3 = (unsigned int)((a3) + 1);
    a1 = (v_rip - 2672300 + 72800 + a3 * 8) + (8);
    if (((unsigned int)(a3)) < 3) goto loc_0028C6C4;
loc_0028C6D6:
    a2 = (unsigned int)((v_stack_m128) & (4));
    if (condition_is_not_equal) goto loc_0028CB0A;
loc_0028C6EE:
    v_r10 = v_stack_m128;
    if (a2 != 0) { v_r10 = v_stack_m124; }
    result = (*(unsigned __int16 *)(v_rip + 13863202)) << (32);
    result = (result) | (*(unsigned __int16 *)(v_rip + 13863202));
    v_rdi = v_r10;
    if (a2 == 0) {
        v_rdi = 8;
        a4 = 4;
        if (a2 == 0) { a4 = (unsigned int)(v_rdi); }
        *(unsigned int *)(a4 + v_r10 * 1) = (unsigned int)(*(unsigned __int16 *)(v_rip + 13863202));
    }
loc_0028C731:
    if (0 >= 3) goto loc_0028C756;
    if (v_stack_m228 != (*(unsigned __int64 *)(0 * 8 + v_rip - 2672300 * 1 + 72800))) goto loc_0028CAEB;
loc_0028C756:
    v_stack_p30 = v_stack_m128;
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_m250));
    v_stack_p20 = (unsigned int)(v_r13);
    v_stack_mF8 = v_xmm0;
    v_stack_m100 = *(unsigned __int64 *)(0 * 8 + v_rip - 2672300 * 1 + 14740688);
    result = MiFindLargeNodePage(v_stack_m290, (unsigned int)((unsigned int)(v_stack_p58)), a3, (unsigned int)((unsigned int)(a3)));
    if (result != 0) goto loc_0028CA59;
    goto loc_0028C45B;
loc_0028C7AA:
    if (v_stack_m220 != 2) goto loc_0028C8E5;
loc_0028C7BA:
    if (v_stack_m220 < 2) goto loc_0028C800;
loc_0028C7C3:
    result = MiIsPageOnBadList(v_r13, (unsigned int)((unsigned int)(v_stack_p58)), a3, (unsigned int)((unsigned int)(a3)));
    if ((unsigned int)(result) == 0) goto loc_0028CE1A;
    if (((v_stack_p50) & (0x10000000ULL)) != 0) goto loc_0028C9B5;
loc_0028C7E1:
    result = MiUnlockPage(v_r13, 17, a3, (unsigned int)((unsigned int)(a3)));
    goto loc_0028C1EF;
loc_0028C800:
    v_rsi = (unsigned int)((v_stack_m200) + 1);
    if (((*(unsigned int *)(v_rip + 13863588)) & ((unsigned int)(v_rsi))) == 0) goto loc_0028CA24;
loc_0028C80E:
loc_0028C810:
    if (!sign_flag) goto loc_0028C7BA;
    goto loc_0028C800;
loc_0028C81B:
    a3 = ~(17 - 1);
    result = (a3) & (v_rsi);
    if (v_rsi == result) goto loc_0028CA4B;
    a1 = (17 - 1) + (v_rsi);
    a1 = (a1) & (a3);
    a1 = (a1) - (v_rsi);
    goto loc_0028C39C;
loc_0028C849:
    v_r15 = (condition_is_below) ? 1 : 0;
    v_rdi = (v_stack_p58 + v_stack_p58 * 2) << (4);
    v_rbx = (unsigned int)(((unsigned int)(a11)) | (4));
    v_rdi = (v_rdi) + (v_rsi);
    v_r15 = (unsigned __int16)((v_r15) + 1);
    if (v_stack_m220 != 2) { v_rbx = a11; }
loc_0028C87A:
    v_stack_p20 = (unsigned __int16)(v_r15);
    result = MiSetPfnOwnedAndActive(v_rsi, (unsigned int)((unsigned int)(v_rbx)), -8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m250))));
    v_rsi = (v_rsi) + (48);
    if (v_rsi != v_rdi) goto loc_0028C87A;
    goto loc_0028C50B;
loc_0028C8AA:
    a4 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m250)))) + 1;
    v_stack_m270 = a4;
    if (a4 < v_stack_m198) goto loc_0028C0DD;
    if (((unsigned int)(v_rbx)) == -1) goto loc_0028C43A;
    a2 = (v_stack_m218) + (4);
    v_stack_m218 = a2;
    if (a2 == v_stack_m1C8) goto loc_0028C43A;
    goto loc_0028C0B2;
loc_0028C8E5:
    result = MiLockPageInline(v_stack_m278, a2, -8, a4);
    goto loc_0028C7C3;
loc_0028C8F6:
    if (!sign_flag) goto loc_0028C99B;
    v_rbx = (unsigned int)(*(unsigned int *)(a2));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2)))) == -1) {
        result = *(unsigned __int64 *)((unsigned __int8)(result) + 18504);
        a1 = v_stack_m230;
        if (a1 > result) { a1 = result; }
        result = MiPageToNode(a1, a2, -8, a4);
        a2 = *(unsigned __int16 *)(v_rip + 13862619);
        v_rbx = (unsigned int)(result);
        a1 = (unsigned int)(a2);
        a4 = *(unsigned __int64 *)(0 * 8 + v_rip - 2672300 * 1 + 14740688);
        a1 = (unsigned int)((a1) * ((unsigned int)(result)));
        result = *(unsigned __int64 *)(v_rip + 12194458);
        a3 = result + a1 * 4;
        result = a3 + a2 * 4;
        v_stack_m218 = a3;
        v_stack_m1C8 = result;
    }
    a1 = (a1) * ((unsigned int)((unsigned int)(v_rbx)));
loc_0028C94F:
    a1 = (a1) + (v_stack_m1C0);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 15184)))) & (1)) == 0) goto loc_0028C0CE;
    v_stack_m270 = a1 + 15235;
    if (a9 != 0) goto loc_0028C0CE;
    if ((unsigned __int8)(v_rdi) == 0) goto loc_0028C993;
loc_0028C980:
    if ((*(unsigned __int8 *)(a1 + 15235)) == 0) goto loc_0028C98F;
    a4 = (a1 + 15235) + 1;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(0 * 8 + v_rip - 2672300 * 1 + 14740688)))) + 1);
    if (((unsigned int)(result)) < ((unsigned int)(v_rdi))) goto loc_0028C980;
loc_0028C98F:
    v_stack_m270 = a4;
loc_0028C993:
    goto loc_0028C0CE;
loc_0028C99B:
    a1 = (a1) * ((unsigned int)(v_stack_p70));
    goto loc_0028C94F;
loc_0028C9A4:
    a4 = (unsigned int)((a4) + 1);
    v_stack_p74 = (unsigned int)(a4);
    goto loc_0028C58C;
loc_0028C9B5:
    result = MiUnlockPage(v_stack_m278, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    v_stack_m264 = (unsigned int)(*(unsigned __int64 *)(0 * 8 + v_rip - 2672300 * 1 + 14740688));
    goto loc_0028C0ED;
loc_0028C9DE:
    result = (unsigned int)((1) & (0x80001000ULL));
    if (((unsigned int)(result)) == 0x80001000ULL) goto loc_0028C62A;
    a4 = 7;
    if (v_stack_m220 != 2) { a4 = 3; }
    a3 = (v_stack_m240) - ((unsigned __int8)((unsigned __int8)(result)));
    result = MiUpdateLargePageBitMap(v_stack_p68, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    goto loc_0028C62A;
loc_0028CA15:
    goto loc_0028C45B;
loc_0028CA24:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13869198)))) & (64)) == 0) goto loc_0028C80E;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p68, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0028C80E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_p58)), (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    goto loc_0028C810;
loc_0028CA4B:
    goto loc_0028C39C;
loc_0028CA59:
    result = MiGetPfnPageSizeIndex((unsigned int)(0xC000009AULL), (unsigned __int8)((unsigned __int8)(result)), 1, a4);
    result = MiInitializeFoundLargeNodePage((unsigned int)(0xC000009AULL), (unsigned int)((unsigned int)(v_stack_m278)), (unsigned int)(a11), a4);
    v_rdi = ((unsigned int)(0xC000009AULL)) - (result);
    v_rdi = (v_rdi) >> (4);
    v_rdi = (v_rdi) * (result);
    result = (v_stack_p58 - 1) + (v_rdi);
    if (result > v_stack_m230) goto loc_0028CAF2;
    *(unsigned __int64 *)(v_stack_m1B0) = v_rdi;
    if (v_stack_m260 == 0) goto loc_0028CAE4;
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_m260 + 40))) >> (12);
    a1 = (a1) + (6);
    if (v_stack_p58 == 0) goto loc_0028CADE;
loc_0028CACE:
    *(unsigned __int64 *)(v_stack_m260 + a1 * 8) = v_rdi;
    v_rdi = (v_rdi) + 1;
    result = (v_stack_p58) - (1);
    if (condition_is_not_equal) goto loc_0028CACE;
loc_0028CADE:
    v_rsi = (unsigned int)((v_stack_p58) << (12));
loc_0028CAE4:
    result = 0;
    goto loc_0028C47B;
loc_0028CAEB:
    a1 = (unsigned int)((v_stack_m260 + a1 * 8 + 8) + 1);
    goto loc_0028C731;
loc_0028CAF2:
    a3 = 0;
    result = MiFreeContiguousPages(v_rdi, v_rsi, a3, a4);
    goto loc_0028C45B;
loc_0028CB0A:
    v_stack_m128 = (unsigned int)(*(unsigned __int16 *)(v_rip + 13863202));
    goto loc_0028C6EE;
loc_0028CB16:
    if ((unsigned __int8)(result) != 0) goto loc_0028CB3A;
    if ((*(unsigned __int8 *)(v_rip + 13862113)) != 1) goto loc_0028CB3A;
    if (0 != (*(unsigned __int64 *)(v_stack_p68 + 32))) goto loc_0028CB3A;
    if ((*(unsigned __int64 *)(v_r10 + 16)) != -1) goto loc_0028CB43;
    if ((*(unsigned int *)(v_r10 + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + 4))))) goto loc_0028CB43;
loc_0028CB3A:
    *(unsigned __int64 *)(v_r10 + 4) = *(unsigned __int64 *)(0 * 8 + v_rip - 2672300 * 1 + 14740688);
    goto loc_0028C09F;
loc_0028CB43:
    if (v_rsi == 16) goto loc_0028CB7E;
    if (v_rsi != 512) goto loc_0028CD35;
    goto loc_0028CB9D;
loc_0028CB7E:
loc_0028CB9D:
    v_stack_m278 = v_rip + 13010899;
    v_stack_m248 = v_rip + 13010877;
    v_stack_p74 = 1;
    v_stack_m270 = 2 * 4;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + 8)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + 4))))) goto loc_0028CD56;
loc_0028CBDC:
    a3 = 0;
loc_0028CBDF:
    v_stack_p78 = 0;
    if (0 >= 1) goto loc_0028CDD9;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + 8)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + 4))))) goto loc_0028CC60;
    v_stack_p30 = v_r10;
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_p70));
    v_stack_p20 = v_stack_m230;
    *(unsigned int *)(v_r10 + 8) = 0;
    result = MiFindBestLargePageStealCandidates(v_stack_p68, v_stack_m240, 2, v_stack_m1C0);
    if ((*(unsigned int *)(v_stack_m258 + 4)) == 0) goto loc_0028CD68;
loc_0028CC60:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m258 + 8)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m258 + 4))))) goto loc_0028CDC4;
    v_stack_m1B8 = *(unsigned __int64 *)(v_stack_m258 + (unsigned int)(*(unsigned int *)(v_stack_m258 + 8)) * 8 + 24);
    *(unsigned int *)(v_stack_m258 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m258 + 8)) + 1);
    a1 = (*(unsigned __int64 *)(v_stack_m258 + (unsigned int)(*(unsigned int *)(v_stack_m258 + 8)) * 8 + 24) + *(unsigned __int64 *)(v_stack_m258 + (unsigned int)(*(unsigned int *)(v_stack_m258 + 8)) * 8 + 24) * 2) << (4);
    a1 = (a1) + (*(unsigned __int16 *)(v_rip + 13863202));
    v_stack_m228 = a1;
    v_stack_p20 = v_stack_p54;
    result = MiPfnsWorthTrying(v_stack_p68, a1, v_stack_p58, (unsigned int)(v_stack_p50));
    if (result != 0) goto loc_0028CD71;
    if (((v_stack_p54) & (1)) != 0) {
        a2 = result + 1;
        a1 = v_stack_p68;
        result = MiAdjustCachedStacks(a1, a2, v_stack_p58, (unsigned int)(v_stack_p50));
    }
    v_stack_p48 = v_stack_p54;
    result = 0;
    v_stack_p40 = 0;
    v_stack_p38 = v_stack_m260;
    v_stack_p30 = 0;
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_p50));
    v_stack_p20 = v_stack_mD8;
    result = MiClaimPhysicalRun(v_stack_p68, *(unsigned __int64 *)(v_stack_m258 + (unsigned int)(*(unsigned int *)(v_stack_m258 + 8)) * 8 + 24), v_stack_p58, v_stack_m230);
    if (result != 0) goto loc_0028CD97;
    *(unsigned int *)(v_stack_m258 + 12) = 1;
    goto loc_0028C4D1;
loc_0028CD35:
    goto loc_0028CB9D;
loc_0028CD56:
    a2 = *(unsigned __int64 *)(v_stack_m258 + (unsigned int)(*(unsigned int *)(v_stack_m258 + 8)) * 8 + 24);
    if ((*(unsigned __int64 *)(v_stack_m258 + 16)) != -1) { a2 = (unsigned int)(v_stack_p58); }
    v_stack_p74 = (unsigned int)(a2);
    goto loc_0028CBDC;
loc_0028CD68:
    goto loc_0028CC60;
loc_0028CD71:
    goto loc_0028CC60;
loc_0028CD97:
    if (((v_stack_p54) & (2)) == 0) goto loc_0028CC60;
    goto loc_0028CC60;
loc_0028CDC4:
    a3 = (unsigned int)(((unsigned int)(v_stack_p78)) + 1);
    goto loc_0028CBDF;
loc_0028CDD9:
    result = qsort(v_stack_m258 + 24, (unsigned int)(*(unsigned int *)(v_stack_m258 + 4)), (unsigned int)(0xC0000017ULL), v_rip + 2213622);
    v_r12 = 0;
    v_stack_m268 = 1;
    goto loc_0028C09F;
loc_0028CE1A:
    v_stack_m268 = 1;
    goto loc_0028C7E1;
}
```

## 5. (Beta) C Style

```c
int64_t MiFindContiguousPagesEx(void *Arg1, int64_t Arg2, int64_t Arg3, void *Arg4, uint64_t Arg5, int64_t Arg6, uint32_t Arg7, uint32_t Arg8, uint8_t Arg9, uint32_t Arg10, uint32_t Arg11, int64_t Arg12, int64_t Arg13, int64_t Arg14)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m118;
    uint64_t v_stack_m124;
    uint64_t v_stack_m128;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint32_t v_stack_m16C;
    uint32_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint32_t v_stack_m238;
    uint64_t v_stack_m240;
    uint32_t v_stack_m248;
    uint32_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint32_t v_stack_m264;
    uint32_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint32_t v_stack_m280;
    uint32_t v_stack_m284;
    uint32_t v_stack_m288;
    uint64_t v_stack_m290;
    uint32_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint32_t v_stack_m2A4;
    uint32_t v_stack_m2A8;
    uint64_t v_stack_m2D8;
    uint64_t v_stack_m58;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint64_t v_stack_p54;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint64_t v_stack_p68;
    uint32_t v_stack_p70;
    uint32_t v_stack_p74;
    uint32_t v_stack_p78;

    local_rsp = (local_rsp) - (696);
    result = (*(uint64_t *)(v_rip + 0xB7E93D)) ^ (local_rsp);
    v_stack_m58 = result;
    Arg2 = 0;
    v_stack_m2A0 = Arg6;
    v_stack_m250 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m260 = Arg12;
    v_stack_m230 = Arg3;
    v_stack_m290 = Arg1;
    v_stack_m1B0 = Arg14;
    v_stack_m288 = (uint32_t)((uint32_t)(Arg8));
    v_stack_m2A8 = (uint32_t)((uint32_t)(Arg10));
    v_stack_m258 = Arg13;
    v_stack_m148 = v_xmm0;
    result = memset(v_stack_mD8, Arg2, 128, Arg4);
    local_r12 = 0;
    result = 0;
    v_stack_m2A4 = 0;
    v_stack_mF8 = 0;
    v_stack_mF0 = 0;
    v_stack_m208 = 0;
    v_stack_m200 = 0;
    v_stack_m1F0 = 0;
    v_stack_m1D0 = 0;
    v_stack_m128 = v_xmm0;
    v_stack_m118 = v_xmm0;
    v_stack_m108 = v_xmm0;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xC69274));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC69274)))) & (1)) != 0) {
        Arg2 = 0;
        Arg3 = 852;
        result = memset(v_rip + 13013677, Arg2, Arg3, Arg4);
    }
    if (Arg13 != 0) {
        *(uint32_t *)(Arg13 + 0xC) = 0;
    }
    v_stack_m220 = v_cr8;
    if (((uint8_t)(v_cr8)) > 2) goto loc_0028C664;
    if (((uint32_t)((uint32_t)(Arg8))) >= ((uint32_t)(*(uint16_t *)(v_rip + 0xD390F8)))) goto loc_0028BF27;
    result = (*(uint16_t *)(v_rip + 0xD390F8)) * ((uint32_t)(Arg8));
    result = (result) + (*(uint64_t *)(arg1 + 0x10));
    if (*(uint64_t *)(result + 0x3A80) == 0) goto loc_0028C5F1;
loc_0028BF27:
    if (((uint8_t)(v_cr8)) == 2) goto loc_0028C680;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x3A3C))))) & (0x10001ULL)) != 0) goto loc_0028C680;
loc_0028BF44:
    if (condition_is_below) goto loc_0028BF6B;
    Arg3 = 0;
    result = MiAcquireNonPagedResources(Arg1, v_stack_m2A0, Arg3, 2);
    if (sign_flag) goto loc_0028C550;
loc_0028BF6B:
    if (v_stack_m260 != 0) goto loc_0028C64A;
    v_stack_m238 = 0;
loc_0028BF81:
    if ((((uint8_t)((uint32_t)(Arg10))) & (64)) != 0) goto loc_0028C68E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) & (16)) == 0) goto loc_0028C52A;
loc_0028BF97:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    result = MiInitializePageColorBase(Arg1, 3, 0, v_stack_m148);
    Arg4 = 4;
    if (((uint8_t)(v_cr8)) != 2) { Arg4 = 0; }
    result = MiCreateUltraThreadContext(v_stack_mD8, v_stack_m148, 8, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0028CA15;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg10)))) & (0xB800008ULL));
    v_stack_m264 = 0;
    if (((uint32_t)(result)) == 0x8000000ULL) goto loc_0028C66E;
loc_0028C00F:
    if (((uint32_t)((uint32_t)(Arg8))) >= ((uint32_t)(*(uint16_t *)(v_rip + 0xD38FEA)))) {
        v_stack_m288 = (uint32_t)((uint32_t)(Arg8));
    }
    result = MiReferencePageRuns(Arg1, (uint32_t)((uint32_t)(8 - 7)), 8, Arg4);
    v_stack_m240 = result;
    v_stack_m1C8 = 0;
    Arg4 = ((uint32_t)(*(uint32_t *)(result))) + 1;
    v_stack_m218 = 0;
    Arg4 = (Arg4) << (4);
    Arg4 = (Arg4) + (result);
    v_stack_m1F8 = 0;
    v_stack_m1A0 = Arg4;
    v_stack_m1D8 = 0;
    result = 0;
    if (((Arg4) & (Arg4 - 1)) == 0) { result = Arg4; }
    v_stack_m268 = 0;
    v_stack_m1E8 = result;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg10)))) >> (13));
    result = (uint8_t)((result) & (1));
    v_stack_m1E0 = v_stack_m2A0;
    v_stack_m1D0 = (uint8_t)(result);
    v_stack_m298 = 0;
    if (v_stack_m258 != 0) goto loc_0028CB16;
loc_0028C09F:
    local_r13 = (uint32_t)(((uint32_t)(Arg10)) & (0x2000ULL));
    v_stack_m1C0 = *(uint64_t *)(arg1 + 0x10);
    v_stack_m248 = (uint32_t)(local_r13);
loc_0028C0B2:
    v_stack_m270 = 0;
    if (((uint8_t)(*(uint8_t *)(v_rip + 0xD38F49))) > 1) goto loc_0028C8F6;
loc_0028C0CE:
    Arg1 = ((uint8_t)(*(uint8_t *)(v_rip + 0xD38F49))) + (0);
    v_stack_m198 = Arg1;
loc_0028C0DD:
    v_stack_m1F0 = v_stack_m230;
    v_stack_m284 = 0;
loc_0028C0ED:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m240))) == 0) goto loc_0028C431;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m240))) - 1);
    v_stack_m280 = (uint32_t)(result);
    result = (result) + (result);
    v_stack_m208 = *(uint64_t *)(v_stack_m240 + result * 8 + 0x10);
    Arg1 = (*(uint64_t *)(v_stack_m240 + result * 8 + 0x10)) + (*(uint64_t *)(v_stack_m240 + result * 8 + 0x18));
    v_stack_m200 = Arg1;
    if (v_stack_m1F8 >= Arg1) goto loc_0028C431;
    if (!sign_flag) goto loc_0028C519;
loc_0028C12E:
    if (0 == 0) goto loc_0028C140;
    if (((uint8_t)(*(uint8_t *)(v_stack_m1A0 + result * 8 + 0x4))) != (*(uint8_t *)(0))) goto loc_0028C0ED;
loc_0028C140:
    result = MiCollapseRunTopDown(v_stack_m208, *(uint8_t *)(v_stack_m1A0 + result * 8 + 0x4), v_stack_m240, 0);
    if ((uint32_t)(result) == 0) goto loc_0028C5C7;
    result = (result) * ((uint32_t)(*(uint32_t *)(v_stack_m1A0 + result * 8)));
    result = (result) + (*(uint64_t *)(arg1 + 0x10));
    if (*(uint64_t *)(result + 0x3A80) == 0) goto loc_0028C5BA;
loc_0028C16C:
    v_stack_m278 = v_stack_m1E0;
    if (v_stack_m1D0 != 0) goto loc_0028C565;
loc_0028C185:
    local_r15 = (v_stack_m200) - (v_stack_m1E0);
    v_stack_m2A4 = 0;
    v_stack_m1B8 = local_r15;
    if (v_stack_m258 != 0) goto loc_0028C57C;
loc_0028C1A4:
    local_r12 = (local_r15 + local_r15 * 2) << (4);
    local_r12 = (local_r12) + (*(uint64_t *)(result + 0x3A80));
    v_stack_m228 = local_r12;
    if (v_stack_m1D0 != 0) goto loc_0028C1EA;
    if (0 != 0) goto loc_0028C1EF;
    v_stack_m2D8 = v_stack_m2A4;
    result = MiPfnsWorthTrying(v_stack_m290, local_r12, v_stack_m1E0, (uint32_t)(v_stack_m2A8));
loc_0028C1EA:
    if (result == 0) goto loc_0028C235;
loc_0028C1EF:
loc_0028C1F4:
    if (((v_stack_m2A4) & (2)) != 0) goto loc_0028C65A;
loc_0028C1FF:
    result = (v_stack_m200) - (v_stack_m208);
    if (result >= result) goto loc_0028C219;
    if (v_stack_m1D0 != 0) goto loc_0028C226;
    result = (result) - (result);
    if (result < v_stack_m1E0) {
        result = v_stack_m200;
        result = (result) - (result);
        result = (result) - 1;
        v_stack_m1F0 = result;
    }
    local_rsi = (v_stack_m200) - (result);
    v_stack_m200 = local_rsi;
    local_r12 = 0;
    goto loc_0028C140;
loc_0028C235:
    if (((v_stack_m2A4) & (1)) != 0) {
        Arg2 = 1;
        Arg1 = v_stack_m290;
        result = MiAdjustCachedStacks(Arg1, Arg2, v_stack_m1E0, (uint32_t)(v_stack_m2A8));
    }
    Arg1 = 0;
    v_stack_m150 = v_stack_m260;
    v_stack_m188 = v_stack_m290;
    v_stack_m180 = v_stack_mD8;
    v_stack_m170 = (uint32_t)((uint32_t)(v_stack_m2A8));
    v_stack_m158 = v_stack_m1F0;
    v_stack_m178 = v_stack_m1E0;
    v_stack_m160 = 0;
    v_stack_m2A4 = 0;
    v_stack_m16C = 0;
    v_stack_m168 = -1;
    result = (v_stack_m278 + v_stack_m278 * 2) << (4);
    result = (result) + (0);
    v_stack_m1A8 = result;
loc_0028C2D0:
    result = MiTradePage(v_stack_m188, v_stack_m290, v_stack_m2A4, (uint32_t)(v_stack_m2A8));
    if (result == 0) goto loc_0028C383;
    if (result == 0) goto loc_0028C5DC;
loc_0028C2FA:
    v_stack_m168 = -1;
    result = (result + result * 2) << (4);
    local_rsi = (v_stack_m290) + (result);
    local_r12 = (local_r12) + (result);
    if (local_r12 < v_stack_m1A8) goto loc_0028C2D0;
    if (v_stack_m248 == 0) goto loc_0028C3C3;
loc_0028C323:
loc_0028C327:
    local_r12 = 0;
loc_0028C32A:
    if (v_stack_m260 != 0) goto loc_0028C4C0;
    if (v_stack_m278 == 0) goto loc_0028C4D1;
loc_0028C33C:
    result = (*(uint64_t *)(v_stack_m228 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xBA3D38) + result * 8)) != v_stack_m290) goto loc_0028C376;
    result = MiIsPageOnBadList(v_stack_m228, v_stack_m290, v_stack_m2A4, (uint32_t)(v_stack_m2A8));
    if ((uint32_t)(result) != 0) goto loc_0028C7AA;
    v_stack_m268 = 1;
loc_0028C376:
    goto loc_0028C1F4;
loc_0028C383:
    if (v_stack_m160 > 1) goto loc_0028C81B;
loc_0028C39C:
    if ((uint32_t)(v_stack_m278) == 0) goto loc_0028C49F;
loc_0028C3A5:
    if (v_stack_m248 == 0) goto loc_0028C3C3;
    result = (v_stack_m278) + (v_stack_m290);
    result = (result) - (v_stack_m200);
    if (1 < result) goto loc_0028C2FA;
    goto loc_0028C323;
loc_0028C3C3:
    local_rsi = (v_stack_m278) - (v_stack_m178);
    Arg1 = (0) - (result);
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (result);
    *(uint32_t *)(v_rip + 0xC68F25) = (uint32_t)(Arg1);
    if (v_stack_m260 != 0) {
        result = (uint32_t)((result) * ((uint32_t)(local_rsi)));
    }
    if (local_rsi == 0) goto loc_0028C327;
loc_0028C41A:
    local_r12 = (local_r12) - (48);
    result = MiReleaseFreshPage(local_r12, v_stack_m160, 1, (uint32_t)(v_stack_m2A8));
    local_rsi = (local_rsi) - (1);
    if (condition_is_not_equal) goto loc_0028C41A;
    goto loc_0028C323;
loc_0028C431:
    if ((uint32_t)(v_stack_m2A8) != 0) goto loc_0028C8AA;
loc_0028C43A:
    result = MiDereferencePageRuns(1, v_stack_m160, 1, (uint32_t)(v_stack_m2A8));
loc_0028C45B:
    result = MiDeleteUltraThreadContext(v_stack_mD8, v_stack_m160, 1, (uint32_t)(v_stack_m2A8));
    if (v_stack_m264 >= 0) {
        Arg2 = v_stack_m2A0;
        Arg1 = v_stack_m290;
        result = MiReleaseNonPagedResources(Arg1, Arg2, 1, (uint32_t)(v_stack_m2A8));
    }
loc_0028C47B:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 1, (uint32_t)(v_stack_m2A8));
    local_rsp = (local_rsp) + (696);
    return result;
loc_0028C49F:
    local_r14 = v_stack_m278;
    if (Arg2 != 0) {
        local_r14 = v_stack_m278;
        result = Arg2 - 1;
        result = ~(result);
        local_r14 = (local_r14) + (v_stack_m290);
        result = (result) & (v_stack_m2A0);
        local_r14 = (local_r14) - (result);
    }
    goto loc_0028C3A5;
loc_0028C4C0:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x28))) >> (12));
    if (((uint32_t)(Arg1)) != ((uint32_t)((uint32_t)(v_stack_m238)))) goto loc_0028C55A;
loc_0028C4D1:
    result = MiDereferencePageRuns(v_stack_m240, Arg2, 1, (uint32_t)(v_stack_m2A8));
    result = MiDeleteUltraThreadContext(v_stack_mD8, Arg2, 1, (uint32_t)(v_stack_m2A8));
    if (((uint32_t)(Arg1)) >= ((uint32_t)((uint32_t)(v_stack_m238)))) goto loc_0028C608;
loc_0028C501:
    if (((uint32_t)(Arg1)) >= ((uint32_t)((uint32_t)(v_stack_m238)))) goto loc_0028C849;
loc_0028C50B:
    *(uint64_t *)(v_stack_m1B0) = v_stack_m290;
    result = 0;
    goto loc_0028C47B;
loc_0028C519:
    if (((uint32_t)((uint32_t)(v_stack_p50))) == ((uint32_t)(v_stack_m228))) goto loc_0028C12E;
    goto loc_0028C0ED;
loc_0028C52A:
    Arg2 = (Arg2) + (160);
    result = MiSufficientAvailablePages(v_stack_m290, Arg2, 1, (uint32_t)(v_stack_m2A8));
    if ((uint32_t)(result) != 0) goto loc_0028BF97;
    goto loc_0028C45B;
loc_0028C550:
    goto loc_0028C47B;
loc_0028C55A:
    result = (uint32_t)(((uint32_t)(0xC000009AULL)) - ((uint32_t)(v_stack_m290)));
    v_stack_m1E0 = result;
    goto loc_0028C33C;
loc_0028C565:
    result = (v_stack_p58) - (v_stack_m208);
    local_r13 = 1;
    if (1 > result) { local_r13 = result; }
    v_stack_m278 = local_r13;
    goto loc_0028C185;
loc_0028C57C:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x4))) == 0) goto loc_0028C1A4;
loc_0028C58C:
    if (((uint32_t)((uint32_t)(v_stack_p74))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x4))))) goto loc_0028C1A4;
    if (v_stack_m290 < (*(uint64_t *)(Arg2 + (uint32_t)((uint32_t)((uint32_t)(v_stack_p74))) * 8 + 0x18))) goto loc_0028C9A4;
    if (v_stack_m290 != (*(uint64_t *)(Arg2 + (uint32_t)((uint32_t)((uint32_t)(v_stack_p74))) * 8 + 0x18))) goto loc_0028C1A4;
    Arg4 = (uint32_t)(((uint32_t)(v_stack_p74)) + 1);
    v_stack_p74 = (uint32_t)(Arg4);
    goto loc_0028C1A4;
loc_0028C5BA:
    if (((*(uint8_t *)(v_rip + 0xD3A4C7)) & (48)) == 0) goto loc_0028C16C;
loc_0028C5C7:
    goto loc_0028C0ED;
loc_0028C5DC:
    local_r12 = 0;
    goto loc_0028C32A;
loc_0028C5F1:
    if (((*(uint8_t *)(v_rip + 0xD3A490)) & (48)) == 0) goto loc_0028BF27;
    goto loc_0028C47B;
loc_0028C608:
    Arg2 = (v_stack_m290 + 511) & (-512);
    Arg3 = (v_stack_p58 + v_stack_m290 * 1) & (-512);
    if (Arg2 < Arg3) goto loc_0028C9DE;
loc_0028C62A:
    result = MiConvertContiguousPages(v_stack_m228, v_stack_p58, (uint32_t)((uint32_t)((uint32_t)(v_stack_m250))), v_stack_m220);
    goto loc_0028C501;
loc_0028C64A:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x28))) >> (12));
    result = (uint32_t)((result) + ((uint32_t)(v_stack_p58)));
    v_stack_m238 = (uint32_t)(result);
    goto loc_0028BF81;
loc_0028C65A:
    goto loc_0028C1FF;
loc_0028C664:
    goto loc_0028C47B;
loc_0028C66E:
    Arg2 = v_stack_p58;
    if (((*(uint8_t *)(v_rip + 0xD3A413)) & (48)) != 0) { Arg2 = (uint32_t)(v_stack_m228); }
    v_stack_m264 = (uint32_t)(Arg2);
    goto loc_0028C00F;
loc_0028C680:
    local_r13 = (uint32_t)((local_r13) | (8));
    v_stack_p50 = (uint32_t)(local_r13);
    goto loc_0028BF44;
loc_0028C68E:
    if (((uint32_t)(v_stack_m250)) == 0x100000ULL) {
    }
    Arg3 = 0;
    if (((uint32_t)(v_stack_m250)) >= 0x100000ULL) { Arg3 = 1; }
loc_0028C6C4:
    if (Arg2 == (*(uint64_t *)(v_rip - 0x28C6AC + 0x11C60 + Arg3 * 8))) goto loc_0028C6D6;
    Arg3 = (uint32_t)((Arg3) + 1);
    Arg1 = (v_rip - 2672300 + 72800 + Arg3 * 8) + (8);
    if (((uint32_t)(Arg3)) < 3) goto loc_0028C6C4;
loc_0028C6D6:
    Arg2 = (uint32_t)((v_stack_m128) & (4));
    if (condition_is_not_equal) goto loc_0028CB0A;
loc_0028C6EE:
    local_r10 = v_stack_m128;
    if (Arg2 != 0) { local_r10 = v_stack_m124; }
    result = (*(uint16_t *)(v_rip + 0xD38922)) << (32);
    result = (result) | (*(uint16_t *)(v_rip + 0xD38922));
    local_rdi = local_r10;
    if (Arg2 == 0) {
        local_rdi = 8;
        Arg4 = 4;
        if (Arg2 == 0) { Arg4 = (uint32_t)(local_rdi); }
        *(uint32_t *)(arg4 + local_r10 * 1) = (uint32_t)(*(uint16_t *)(v_rip + 0xD38922));
    }
loc_0028C731:
    if (0 >= 3) goto loc_0028C756;
    if (v_stack_m228 != (*(uint64_t *)(0 * 8 + v_rip - 0x28C6AC * 1 + 0x11C60))) goto loc_0028CAEB;
loc_0028C756:
    v_stack_p30 = v_stack_m128;
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_m250));
    v_stack_p20 = (uint32_t)(local_r13);
    v_stack_mF8 = v_xmm0;
    v_stack_m100 = *(uint64_t *)(0 * 8 + v_rip - 0x28C6AC * 1 + 0xE0ECD0);
    result = MiFindLargeNodePage(v_stack_m290, (uint32_t)((uint32_t)(v_stack_p58)), Arg3, (uint32_t)((uint32_t)(Arg3)));
    if (result != 0) goto loc_0028CA59;
    goto loc_0028C45B;
loc_0028C7AA:
    if (v_stack_m220 != 2) goto loc_0028C8E5;
loc_0028C7BA:
    if (v_stack_m220 < 2) goto loc_0028C800;
loc_0028C7C3:
    result = MiIsPageOnBadList(local_r13, (uint32_t)((uint32_t)(v_stack_p58)), Arg3, (uint32_t)((uint32_t)(Arg3)));
    if ((uint32_t)(result) == 0) goto loc_0028CE1A;
    if (((v_stack_p50) & (0x10000000ULL)) != 0) goto loc_0028C9B5;
loc_0028C7E1:
    result = MiUnlockPage(local_r13, 17, Arg3, (uint32_t)((uint32_t)(Arg3)));
    goto loc_0028C1EF;
loc_0028C800:
    local_rsi = (uint32_t)((v_stack_m200) + 1);
    if (((*(uint32_t *)(v_rip + 0xD38AA4)) & ((uint32_t)(local_rsi))) == 0) goto loc_0028CA24;
loc_0028C80E:
loc_0028C810:
    if (!sign_flag) goto loc_0028C7BA;
    goto loc_0028C800;
loc_0028C81B:
    Arg3 = ~(17 - 1);
    result = (Arg3) & (local_rsi);
    if (local_rsi == result) goto loc_0028CA4B;
    Arg1 = (17 - 1) + (local_rsi);
    Arg1 = (Arg1) & (Arg3);
    Arg1 = (Arg1) - (local_rsi);
    goto loc_0028C39C;
loc_0028C849:
    local_r15 = (condition_is_below) ? 1 : 0;
    local_rdi = (v_stack_p58 + v_stack_p58 * 2) << (4);
    local_rbx = (uint32_t)(((uint32_t)(Arg11)) | (4));
    local_rdi = (local_rdi) + (local_rsi);
    local_r15 = (uint16_t)((local_r15) + 1);
    if (v_stack_m220 != 2) { local_rbx = Arg11; }
loc_0028C87A:
    v_stack_p20 = (uint16_t)(local_r15);
    result = MiSetPfnOwnedAndActive(local_rsi, (uint32_t)((uint32_t)(local_rbx)), -8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m250))));
    local_rsi = (local_rsi) + (48);
    if (local_rsi != local_rdi) goto loc_0028C87A;
    goto loc_0028C50B;
loc_0028C8AA:
    Arg4 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m250)))) + 1;
    v_stack_m270 = Arg4;
    if (Arg4 < v_stack_m198) goto loc_0028C0DD;
    if (((uint32_t)(local_rbx)) == -1) goto loc_0028C43A;
    Arg2 = (v_stack_m218) + (4);
    v_stack_m218 = Arg2;
    if (Arg2 == v_stack_m1C8) goto loc_0028C43A;
    goto loc_0028C0B2;
loc_0028C8E5:
    result = MiLockPageInline(v_stack_m278, Arg2, -8, Arg4);
    goto loc_0028C7C3;
loc_0028C8F6:
    if (!sign_flag) goto loc_0028C99B;
    local_rbx = (uint32_t)(*(uint32_t *)(Arg2));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg2)))) == -1) {
        result = *(uint64_t *)((uint8_t)(result) + 0x4848);
        Arg1 = v_stack_m230;
        if (Arg1 > result) { Arg1 = result; }
        result = MiPageToNode(Arg1, Arg2, -8, Arg4);
        Arg2 = *(uint16_t *)(v_rip + 0xD386DB);
        local_rbx = (uint32_t)(result);
        Arg1 = (uint32_t)(Arg2);
        Arg4 = *(uint64_t *)(0 * 8 + v_rip - 0x28C6AC * 1 + 0xE0ECD0);
        Arg1 = (uint32_t)((Arg1) * ((uint32_t)(result)));
        result = *(uint64_t *)(v_rip + 0xBA129A);
        Arg3 = result + Arg1 * 4;
        result = Arg3 + Arg2 * 4;
        v_stack_m218 = Arg3;
        v_stack_m1C8 = result;
    }
    Arg1 = (Arg1) * ((uint32_t)((uint32_t)(local_rbx)));
loc_0028C94F:
    Arg1 = (Arg1) + (v_stack_m1C0);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x3B50)))) & (1)) == 0) goto loc_0028C0CE;
    v_stack_m270 = Arg1 + 15235;
    if (Arg9 != 0) goto loc_0028C0CE;
    if ((uint8_t)(local_rdi) == 0) goto loc_0028C993;
loc_0028C980:
    if ((*(uint8_t *)(arg1 + 0x3B83)) == 0) goto loc_0028C98F;
    Arg4 = (Arg1 + 15235) + 1;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(0 * 8 + v_rip - 0x28C6AC * 1 + 0xE0ECD0)))) + 1);
    if (((uint32_t)(result)) < ((uint32_t)(local_rdi))) goto loc_0028C980;
loc_0028C98F:
    v_stack_m270 = Arg4;
loc_0028C993:
    goto loc_0028C0CE;
loc_0028C99B:
    Arg1 = (Arg1) * ((uint32_t)(v_stack_p70));
    goto loc_0028C94F;
loc_0028C9A4:
    Arg4 = (uint32_t)((Arg4) + 1);
    v_stack_p74 = (uint32_t)(Arg4);
    goto loc_0028C58C;
loc_0028C9B5:
    result = MiUnlockPage(v_stack_m278, (uint8_t)((uint8_t)(result)), Arg3, Arg4);
    v_stack_m264 = (uint32_t)(*(uint64_t *)(0 * 8 + v_rip - 0x28C6AC * 1 + 0xE0ECD0));
    goto loc_0028C0ED;
loc_0028C9DE:
    result = (uint32_t)((1) & (0x80001000ULL));
    if (((uint32_t)(result)) == 0x80001000ULL) goto loc_0028C62A;
    Arg4 = 7;
    if (v_stack_m220 != 2) { Arg4 = 3; }
    Arg3 = (v_stack_m240) - ((uint8_t)((uint8_t)(result)));
    result = MiUpdateLargePageBitMap(v_stack_p68, (uint8_t)((uint8_t)(result)), Arg3, Arg4);
    goto loc_0028C62A;
loc_0028CA15:
    goto loc_0028C45B;
loc_0028CA24:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD3A08E)))) & (64)) == 0) goto loc_0028C80E;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_p68, (uint8_t)((uint8_t)(result)), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0028C80E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_p58)), (uint8_t)((uint8_t)(result)), Arg3, Arg4);
    goto loc_0028C810;
loc_0028CA4B:
    goto loc_0028C39C;
loc_0028CA59:
    result = MiGetPfnPageSizeIndex((uint32_t)(0xC000009AULL), (uint8_t)((uint8_t)(result)), 1, Arg4);
    result = MiInitializeFoundLargeNodePage((uint32_t)(0xC000009AULL), (uint32_t)((uint32_t)(v_stack_m278)), (uint32_t)(Arg11), Arg4);
    local_rdi = ((uint32_t)(0xC000009AULL)) - (result);
    local_rdi = (local_rdi) >> (4);
    local_rdi = (local_rdi) * (result);
    result = (v_stack_p58 - 1) + (local_rdi);
    if (result > v_stack_m230) goto loc_0028CAF2;
    *(uint64_t *)(v_stack_m1B0) = local_rdi;
    if (v_stack_m260 == 0) goto loc_0028CAE4;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_m260 + 0x28))) >> (12);
    Arg1 = (Arg1) + (6);
    if (v_stack_p58 == 0) goto loc_0028CADE;
loc_0028CACE:
    *(uint64_t *)(v_stack_m260 + arg1 * 8) = local_rdi;
    local_rdi = (local_rdi) + 1;
    result = (v_stack_p58) - (1);
    if (condition_is_not_equal) goto loc_0028CACE;
loc_0028CADE:
    local_rsi = (uint32_t)((v_stack_p58) << (12));
loc_0028CAE4:
    result = 0;
    goto loc_0028C47B;
loc_0028CAEB:
    Arg1 = (uint32_t)((v_stack_m260 + Arg1 * 8 + 8) + 1);
    goto loc_0028C731;
loc_0028CAF2:
    Arg3 = 0;
    result = MiFreeContiguousPages(local_rdi, local_rsi, Arg3, Arg4);
    goto loc_0028C45B;
loc_0028CB0A:
    v_stack_m128 = (uint32_t)(*(uint16_t *)(v_rip + 0xD38922));
    goto loc_0028C6EE;
loc_0028CB16:
    if ((uint8_t)(result) != 0) goto loc_0028CB3A;
    if ((*(uint8_t *)(v_rip + 0xD384E1)) != 1) goto loc_0028CB3A;
    if (0 != (*(uint64_t *)(v_stack_p68 + 0x20))) goto loc_0028CB3A;
    if ((*(uint64_t *)(local_r10 + 0x10)) != -1) goto loc_0028CB43;
    if ((*(uint32_t *)(local_r10 + 0x8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + 0x4))))) goto loc_0028CB43;
loc_0028CB3A:
    *(uint64_t *)(local_r10 + 0x4) = *(uint64_t *)(0 * 8 + v_rip - 0x28C6AC * 1 + 0xE0ECD0);
    goto loc_0028C09F;
loc_0028CB43:
    if (local_rsi == 16) goto loc_0028CB7E;
    if (local_rsi != 512) goto loc_0028CD35;
    goto loc_0028CB9D;
loc_0028CB7E:
loc_0028CB9D:
    v_stack_m278 = v_rip + 13010899;
    v_stack_m248 = v_rip + 13010877;
    v_stack_p74 = 1;
    v_stack_m270 = 2 * 4;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + 0x8)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + 0x4))))) goto loc_0028CD56;
loc_0028CBDC:
    Arg3 = 0;
loc_0028CBDF:
    v_stack_p78 = 0;
    if (0 >= 1) goto loc_0028CDD9;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + 0x8)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + 0x4))))) goto loc_0028CC60;
    v_stack_p30 = local_r10;
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_p70));
    v_stack_p20 = v_stack_m230;
    *(uint32_t *)(local_r10 + 0x8) = 0;
    result = MiFindBestLargePageStealCandidates(v_stack_p68, v_stack_m240, 2, v_stack_m1C0);
    if ((*(uint32_t *)(v_stack_m258 + 0x4)) == 0) goto loc_0028CD68;
loc_0028CC60:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m258 + 0x8)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m258 + 0x4))))) goto loc_0028CDC4;
    v_stack_m1B8 = *(uint64_t *)(v_stack_m258 + (uint32_t)(*(uint32_t *)(v_stack_m258 + 0x8)) * 8 + 0x18);
    *(uint32_t *)(v_stack_m258 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m258 + 0x8)) + 1);
    Arg1 = (*(uint64_t *)(v_stack_m258 + (uint32_t)(*(uint32_t *)(v_stack_m258 + 0x8)) * 8 + 0x18) + *(uint64_t *)(v_stack_m258 + (uint32_t)(*(uint32_t *)(v_stack_m258 + 0x8)) * 8 + 0x18) * 2) << (4);
    Arg1 = (Arg1) + (*(uint16_t *)(v_rip + 0xD38922));
    v_stack_m228 = Arg1;
    v_stack_p20 = v_stack_p54;
    result = MiPfnsWorthTrying(v_stack_p68, Arg1, v_stack_p58, (uint32_t)(v_stack_p50));
    if (result != 0) goto loc_0028CD71;
    if (((v_stack_p54) & (1)) != 0) {
        Arg2 = result + 1;
        Arg1 = v_stack_p68;
        result = MiAdjustCachedStacks(Arg1, Arg2, v_stack_p58, (uint32_t)(v_stack_p50));
    }
    v_stack_p48 = v_stack_p54;
    result = 0;
    v_stack_p40 = 0;
    v_stack_p38 = v_stack_m260;
    v_stack_p30 = 0;
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_p50));
    v_stack_p20 = v_stack_mD8;
    result = MiClaimPhysicalRun(v_stack_p68, *(uint64_t *)(v_stack_m258 + (uint32_t)(*(uint32_t *)(v_stack_m258 + 0x8)) * 8 + 0x18), v_stack_p58, v_stack_m230);
    if (result != 0) goto loc_0028CD97;
    *(uint32_t *)(v_stack_m258 + 0xC) = 1;
    goto loc_0028C4D1;
loc_0028CD35:
    goto loc_0028CB9D;
loc_0028CD56:
    Arg2 = *(uint64_t *)(v_stack_m258 + (uint32_t)(*(uint32_t *)(v_stack_m258 + 0x8)) * 8 + 0x18);
    if ((*(uint64_t *)(v_stack_m258 + 0x10)) != -1) { Arg2 = (uint32_t)(v_stack_p58); }
    v_stack_p74 = (uint32_t)(Arg2);
    goto loc_0028CBDC;
loc_0028CD68:
    goto loc_0028CC60;
loc_0028CD71:
    goto loc_0028CC60;
loc_0028CD97:
    if (((v_stack_p54) & (2)) == 0) goto loc_0028CC60;
    goto loc_0028CC60;
loc_0028CDC4:
    Arg3 = (uint32_t)(((uint32_t)(v_stack_p78)) + 1);
    goto loc_0028CBDF;
loc_0028CDD9:
    result = qsort(v_stack_m258 + 24, (uint32_t)(*(uint32_t *)(v_stack_m258 + 0x4)), (uint32_t)(0xC0000017ULL), v_rip + 2213622);
    local_r12 = 0;
    v_stack_m268 = 1;
    goto loc_0028C09F;
loc_0028CE1A:
    v_stack_m268 = 1;
    goto loc_0028C7E1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg4` | `- 0x1` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0028BDE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
