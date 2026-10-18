# MiCopyOnWrite

- RVA: `0x00362A0C`–`0x003635AD` (길이 `2,977` bytes)
- VA: `0x0000000140362A0C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00079E24`
- 디코드: `688`개 명령, `2,977/2,977` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **48**; 고유 호출 대상: **42**
- 직접 호출자로 확인된 함수: **20**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x00362AEC` → [MiGetSystemRegionType](../28/MiGetSystemRegionType_function_0028EC80.md) (function, `0x0028EC80`)
- `0x00362B7C` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00362B94` → [MiComputeFaultNode](../2B/MiComputeFaultNode_function_002B60C0.md) (function, `0x002B60C0`)
- `0x00362BD0` → [MiGetWsleContents](../31/MiGetWsleContents_function_00316540.md) (function, `0x00316540`)
- `0x00362C26` → [MiGetWsleProtection](../29/MiGetWsleProtection_function_00294A80.md) (function, `0x00294A80`)
- `0x00362C79` → [MiInitializePageColorBase](../32/MiInitializePageColorBase_function_00320410.md) (function, `0x00320410`)
- `0x00362CE4` → [MiGetCurrentSlabIdentity](../3B/MiGetCurrentSlabIdentity_function_003BD020.md) (function, `0x003BD020`)
- `0x00362CFE` → [MiGetPage](../28/MiGetPage_function_002884C0.md) (function, `0x002884C0`)
- `0x00362D4D` → [MiMakeDemandZeroPte](../33/MiMakeDemandZeroPte_function_00337A00.md) (function, `0x00337A00`)
- `0x00362D6C` → [MiUpdateWorkingSetPrivateSize](MiUpdateWorkingSetPrivateSize_function_00362250.md) (function, `0x00362250`)
- `0x00362D77` → [MiSetWsleProtection](../29/MiSetWsleProtection_function_002939D8.md) (function, `0x002939D8`)
- `0x00362D83` → [MiGetContainingPageTable](../34/MiGetContainingPageTable_function_003467F0.md) (function, `0x003467F0`)
- `0x00362D8E` → [MiSetPfnContainingFrame](MiSetPfnContainingFrame_function_00363FC0.md) (function, `0x00363FC0`)
- `0x00362D9C` → [MiGetEffectivePagePriorityThread](MiGetEffectivePagePriorityThread_function_003626E0.md) (function, `0x003626E0`)
- `0x00362DF7` → [MiSetPfnModified](MiSetPfnModified_function_00362960.md) (function, `0x00362960`)
- `0x00362E0F` → [MiFinalizePageAttribute](../33/MiFinalizePageAttribute_function_00332E30.md) (function, `0x00332E30`)
- `0x00362F00` → [MiCopyPage](../2B/MiCopyPage_function_002B1B30.md) (function, `0x002B1B30`)
- `0x00362F0D` → [MiVmAccessLoggingEnabled](MiVmAccessLoggingEnabled_function_003629D4.md) (function, `0x003629D4`)
- `0x00362FB3` → [MiFlushSingleTbEntry](../28/MiFlushSingleTbEntry_function_0028E730.md) (function, `0x0028E730`)
- `0x00363004` → [MiDecrementShareCountEx](../33/MiDecrementShareCountEx_function_00333F70.md) (function, `0x00333F70`)
- `0x00363034` → [MiLocateCloneAddress](../3D/MiLocateCloneAddress_function_003D26B4.md) (function, `0x003D26B4`)
- `0x00363044` → [MiDecrementCloneBlockReference](../22/MiDecrementCloneBlockReference_function_0022B9D0.md) (function, `0x0022B9D0`)
- `0x00363057` → [MiDecrementCombinedPteEx](../22/MiDecrementCombinedPteEx_function_0022B940.md) (function, `0x0022B940`)
- `0x00363071` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0036312D` → [MI_WRITE_INVALID_PTE_TB_FLUSH_NEEDED](../24/MI_WRITE_INVALID_PTE_TB_FLUSH_NEEDED_function_002400C0.md) (function, `0x002400C0`)
- `0x00363184` → [MiPteInShadowRange](../23/MiPteInShadowRange_function_0023FB00.md) (function, `0x0023FB00`)
- `0x003631A4` → [MiFlushSingleTbEntry](../28/MiFlushSingleTbEntry_function_0028E730.md) (function, `0x0028E730`)
- `0x00363245` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x0036326C` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00363298` → [MiGetVmAccessLoggingPartition](../38/MiGetVmAccessLoggingPartition_function_003815A0.md) (function, `0x003815A0`)
- `0x003632B3` → [MiLogPageAccess](../24/MiLogPageAccess_function_00240870.md) (function, `0x00240870`)
- `0x00363304` → [MiReturnCommit](../24/MiReturnCommit_function_00248410.md) (function, `0x00248410`)
- `0x00363345` → [MiUnlockPageTableCharges](../40/MiUnlockPageTableCharges_function_00408140.md) (function, `0x00408140`)
- `0x003633C8` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x00363410` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00363424` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00363434` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0036344C` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0036345B` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0036348D` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00363499` → [MiWritePteShadow](../29/MiWritePteShadow_function_00294EAC.md) (function, `0x00294EAC`)
- `0x003634C3` → [MiGetSlabPage](../37/MiGetSlabPage_function_00376FBC.md) (function, `0x00376FBC`)
- `0x003634FE` → [MiLockVadTree](../27/MiLockVadTree_function_0027C0F0.md) (function, `0x0027C0F0`)
- `0x00363506` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x0036351A` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x00363543` → [MiIdentifyPfn](../31/MiIdentifyPfn_function_0031CAC0.md) (function, `0x0031CAC0`)
- `0x00363582` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x003635A3` → [MiChargeCommit](../28/MiChargeCommit_function_00286EB0.md) (function, `0x00286EB0`)

### Direct callers
- [sub_0023DB14](../23/Unknown_function_0023DB14.md) at `0x0023DB62`
- [MiWalkVaRange](../24/MiWalkVaRange_function_00243BF0.md) at `0x0024473B`
- [MmProtectPool](../26/MmProtectPool_function_002697AC.md) at `0x00269ECF`
- [MiSplitPrivatePage](../2A/MiSplitPrivatePage_function_002A6210.md) at `0x002A666A`
- [sub_002C3A7C](../2C/Unknown_function_002C3A7C.md) at `0x002C3F89`
- [MiMakeProtoPrivate](../2C/MiMakeProtoPrivate_function_002C64A4.md) at `0x002C6545`
- [MiValidFault](../32/MiValidFault_function_003280B4.md) at `0x00328293`
- [MiCompleteProtoPteFault](../34/MiCompleteProtoPteFault_function_00345710.md) at `0x00346425`
- [MiSystemFault](../34/MiSystemFault_function_0034AA64.md) at `0x0034AEBB`
- [MiLockCode](MiLockCode_function_0036F91C.md) at `0x0036FFBB`
- [MiMakeDriverPagesPrivate](../38/MiMakeDriverPagesPrivate_function_00384C60.md) at `0x00385013`
- [MiValidVirtualizationFault](../46/MiValidVirtualizationFault_function_00466EC0.md) at `0x00466FD8`
- [MiFaultInPagedPool](../4B/MiFaultInPagedPool_function_004B3BC0.md) at `0x004B3C85`
- [MiSplitReducedCommitClonePage](../4F/MiSplitReducedCommitClonePage_function_004FA808.md) at `0x004FA976`
- [MiLockDriverPageRange](../67/MiLockDriverPageRange_function_00670160.md) at `0x006704B2`
- [MiReplaceImportEntry](../67/MiReplaceImportEntry_function_00671440.md) at `0x006715AD`
- [MiPrepareImagePagesForHotPatch](../68/MiPrepareImagePagesForHotPatch_function_00683800.md) at `0x00683AB3`
- [sub_006D9212](../6D/Unknown_function_006D9212.md) at `0x006D94A3`
- [sub_006E94B4](../6E/Unknown_function_006E94B4.md) at `0x006E94D0`
- [sub_006F541A](../6F/Unknown_function_006F541A.md) at `0x006F543E`

### Static image references
- `0x00362A2B` → RVA `0x00E0A740` (`.data`; read)
- `0x00362BAD` → RVA `0x00E30088` (`.data`; read)
- `0x00362C41` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00362DA1` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x00362FB8` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x003630A4` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x003630E6` → RVA `0x00E37E40` (`.data`; read)
- `0x003633D6` → RVA `0x00E380C0` (`.data`; read)
- `0x00363416` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x003634F6` → [sub_006E30F6](../6E/Unknown_function_006E30F6.md) (`tail-transfer`)
  - `0x00363522` → [sub_006E30F6 + 0x3B](../6E/Unknown_function_006E30F6.md) (`tail-transfer`)
  - `0x0036352D` → [sub_006E30F6](../6E/Unknown_function_006E30F6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00362A0C  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00362A11  55                              push rbp
00362A12  56                              push rsi
00362A13  57                              push rdi
00362A14  41 54                           push r12
00362A16  41 55                           push r13
00362A18  41 56                           push r14
00362A1A  41 57                           push r15
00362A1C  48 8D AC 24 70 FF FF FF         lea rbp, [rsp - 0x90]
00362A24  48 81 EC 90 01 00 00            sub rsp, 0x190
00362A2B  48 8B 05 0E 7D AA 00            mov rax, qword ptr [rip + 0xaa7d0e]
00362A32  48 33 C4                        xor rax, rsp
00362A35  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
00362A3C  48 8B 85 F0 00 00 00            mov rax, qword ptr [rbp + 0xf0]
00362A43  0F 57 C9                        xorps xmm1, xmm1
00362A46  44 89 4C 24 50                  mov dword ptr [rsp + 0x50], r9d
00362A4B  0F 57 C0                        xorps xmm0, xmm0
00362A4E  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
00362A53  4C 8B E2                        mov r12, rdx
00362A56  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
00362A5A  4C 8B E9                        mov r13, rcx
00362A5D  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
00362A61  0F 11 45 90                     movups xmmword ptr [rbp - 0x70], xmm0
00362A65  0F 11 4D B0                     movups xmmword ptr [rbp - 0x50], xmm1
00362A69  0F 11 4D C0                     movups xmmword ptr [rbp - 0x40], xmm1
00362A6D  48 85 C0                        test rax, rax
00362A70  74 04                           je 0x140362a76
00362A72  48 83 20 00                     and qword ptr [rax], 0
00362A76  48 8B 32                        mov rsi, qword ptr [rdx]
00362A79  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00362A83  48 8B C6                        mov rax, rsi
00362A86  48 C1 E8 0C                     shr rax, 0xc
00362A8A  48 23 C1                        and rax, rcx
00362A8D  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
00362A91  4C 8D 3C 40                     lea r15, [rax + rax*2]
00362A95  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00362A9F  49 C1 E7 04                     shl r15, 4
00362AA3  48 8B C0                        mov rax, rax
00362AA6  48 83 64 24 68 00               and qword ptr [rsp + 0x68], 0
00362AAC  4C 03 F8                        add r15, rax
00362AAF  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
00362AB9  4C 8B F6                        mov r14, rsi
00362ABC  49 C1 EE 09                     shr r14, 9
00362AC0  33 DB                           xor ebx, ebx
00362AC2  41 F7 D6                        not r14d
00362AC5  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
00362AC9  41 83 E6 01                     and r14d, 1
00362ACD  48 0B C1                        or rax, rcx
00362AD0  49 8B CD                        mov rcx, r13
00362AD3  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00362AD7  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00362AE0  48 8B B8 B8 00 00 00            mov rdi, qword ptr [rax + 0xb8]
00362AE7  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
00362AEC  E8 8F C1 F2 FF                  call 0x14028ec80
00362AF1  45 33 DB                        xor r11d, r11d
00362AF4  8D 4B 01                        lea ecx, [rbx + 1]
00362AF7  44 89 5C 24 3C                  mov dword ptr [rsp + 0x3c], r11d
00362AFC  8D 53 02                        lea edx, [rbx + 2]
00362AFF  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
00362B03  83 F8 0B                        cmp eax, 0xb
00362B06  0F 84 D6 05 00 00               je 0x1403630e2
00362B0C  83 F8 0F                        cmp eax, 0xf
00362B0F  77 11                           ja 0x140362b22
00362B11  B9 00 A1 00 00                  mov ecx, 0xa100
00362B16  0F A3 C1                        bt ecx, eax
00362B19  0F 82 30 07 00 00               jb 0x14036324f
00362B1F  8D 4B 01                        lea ecx, [rbx + 1]
00362B22  83 F8 05                        cmp eax, 5
00362B25  0F 84 A7 08 00 00               je 0x1403633d2
00362B2B  83 F8 04                        cmp eax, 4
00362B2E  0F 84 40 09 00 00               je 0x140363474
00362B34  48 39 9F 70 02 00 00            cmp qword ptr [rdi + 0x270], rbx
00362B3B  0F 85 10 06 00 00               jne 0x140363151
00362B41  21 5C 24 54                     and dword ptr [rsp + 0x54], ebx
00362B45  48 8D 9F 00 04 00 00            lea rbx, [rdi + 0x400]
00362B4C  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
00362B50  41 8B FE                        mov edi, r14d
00362B53  48 0F BA E0 28                  bt rax, 0x28
00362B58  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00362B5D  89 4C 24 3C                     mov dword ptr [rsp + 0x3c], ecx
00362B61  72 0D                           jb 0x140362b70
00362B63  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
00362B67  48 85 C0                        test rax, rax
00362B6A  0F 89 3E 06 00 00               jns 0x1403631ae
00362B70  33 D2                           xor edx, edx
00362B72  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00362B76  41 B8 98 00 00 00               mov r8d, 0x98
00362B7C  E8 BF 40 36 00                  call 0x1406c6c40
00362B81  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00362B86  48 89 5D 08                     mov qword ptr [rbp + 8], rbx
00362B8A  33 D2                           xor edx, edx
00362B8C  4C 89 6D D0                     mov qword ptr [rbp - 0x30], r13
00362B90  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00362B94  E8 27 35 F5 FF                  call 0x1402b60c0
00362B99  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
00362B9E  8B D8                           mov ebx, eax
00362BA0  44 8B 5C 24 3C                  mov r11d, dword ptr [rsp + 0x3c]
00362BA5  41 0F B7 92 AE 00 00 00         movzx edx, word ptr [r10 + 0xae]
00362BAD  48 8B 0D D4 D4 AC 00            mov rcx, qword ptr [rip + 0xacd4d4]
00362BB4  4D 8B 37                        mov r14, qword ptr [r15]
00362BB7  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
00362BBC  49 83 E6 01                     and r14, 1
00362BC0  4C 89 75 A0                     mov qword ptr [rbp - 0x60], r14
00362BC4  48 8B 04 D1                     mov rax, qword ptr [rcx + rdx*8]
00362BC8  49 8B D5                        mov rdx, r13
00362BCB  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00362BD0  E8 6B 39 FB FF                  call 0x140316540
00362BD5  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
00362BD9  41 B9 09 00 00 00               mov r9d, 9
00362BDF  41 B0 0A                        mov r8b, 0xa
00362BE2  41 8D 51 F8                     lea edx, [r9 - 8]
00362BE6  23 CA                           and ecx, edx
00362BE8  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00362BEC  75 1C                           jne 0x140362c0a
00362BEE  8A C8                           mov cl, al
00362BF0  80 E1 0F                        and cl, 0xf
00362BF3  41 3A C8                        cmp cl, r8b
00362BF6  74 12                           je 0x140362c0a
00362BF8  41 3A C9                        cmp cl, r9b
00362BFB  0F 84 63 07 00 00               je 0x140363364
00362C01  44 3B DA                        cmp r11d, edx
00362C04  0F 85 4A 07 00 00               jne 0x140363354
00362C0A  8A C8                           mov cl, al
00362C0C  80 E1 0F                        and cl, 0xf
00362C0F  88 4C 24 38                     mov byte ptr [rsp + 0x38], cl
00362C13  41 3A C8                        cmp cl, r8b
00362C16  74 1C                           je 0x140362c34
00362C18  80 F9 08                        cmp cl, 8
00362C1B  0F 84 4D 07 00 00               je 0x14036336e
00362C21  8A D0                           mov dl, al
00362C23  49 8B CD                        mov rcx, r13
00362C26  E8 55 1E F3 FF                  call 0x140294a80
00362C2B  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
00362C30  85 C0                           test eax, eax
00362C32  75 0B                           jne 0x140362c3f
00362C34  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
00362C38  48 C1 E8 05                     shr rax, 5
00362C3C  83 E0 1F                        and eax, 0x1f
00362C3F  8B C0                           mov eax, eax
00362C41  48 8D 0D B8 D3 C9 FF            lea rcx, [rip - 0x362c48]
00362C48  8B 84 81 70 10 01 00            mov eax, dword ptr [rcx + rax*4 + 0x11070]
00362C4F  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00362C53  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00362C58  48 83 F8 FF                     cmp rax, -1
00362C5C  0F 85 B0 00 00 00               jne 0x140362d12
00362C62  41 8B 47 20                     mov eax, dword ptr [r15 + 0x20]
00362C66  4C 8D 4D 90                     lea r9, [rbp - 0x70]
00362C6A  44 8B C3                        mov r8d, ebx
00362C6D  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00362C71  BA 03 00 00 00                  mov edx, 3
00362C76  49 8B CA                        mov rcx, r10
00362C79  E8 92 D7 FB FF                  call 0x140320410
00362C7E  8B 45 98                        mov eax, dword ptr [rbp - 0x68]
00362C81  44 0F B6 4C 24 42               movzx r9d, byte ptr [rsp + 0x42]
00362C87  25 FF FF F3 FF                  and eax, 0xfff3ffff
00362C8C  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
00362C90  41 83 E1 C0                     and r9d, 0xffffffc0
00362C94  41 C1 E1 0C                     shl r9d, 0xc
00362C98  44 0B C8                        or r9d, eax
00362C9B  B8 01 00 00 00                  mov eax, 1
00362CA0  44 89 4D 98                     mov dword ptr [rbp - 0x68], r9d
00362CA4  F0 0F C1 01                     lock xadd dword ptr [rcx], eax
00362CA8  33 D2                           xor edx, edx
00362CAA  4C 8D 05 4F D3 C9 FF            lea r8, [rip - 0x362cb1]
00362CB1  41 8B C9                        mov ecx, r9d
00362CB4  48 C1 E9 10                     shr rcx, 0x10
00362CB8  83 E1 03                        and ecx, 3
00362CBB  41 F7 B4 88 C0 DC E2 00         div dword ptr [r8 + rcx*4 + 0xe2dcc0]
00362CC3  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00362CC8  41 33 D1                        xor edx, r9d
00362CCB  0F B6 DA                        movzx ebx, dl
00362CCE  41 33 D9                        xor ebx, r9d
00362CD1  8B 80 B8 00 00 00               mov eax, dword ptr [rax + 0xb8]
00362CD7  A8 0F                           test al, 0xf
00362CD9  75 16                           jne 0x140362cf1
00362CDB  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00362CE4  E8 37 A3 05 00                  call 0x1403bd020
00362CE9  3C FF                           cmp al, 0xff
00362CEB  0F 85 B2 07 00 00               jne 0x1403634a3
00362CF1  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00362CF6  41 B8 01 00 00 00               mov r8d, 1
00362CFC  8B D3                           mov edx, ebx
00362CFE  E8 BD 57 F2 FF                  call 0x1402884c0
00362D03  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00362D08  48 83 F8 FF                     cmp rax, -1
00362D0C  0F 84 35 04 00 00               je 0x140363147
00362D12  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00362D16  BA 01 00 00 00                  mov edx, 1
00362D1B  3B C2                           cmp eax, edx
00362D1D  0F 83 BE 05 00 00               jae 0x1403632e1
00362D23  8B 4C 24 34                     mov ecx, dword ptr [rsp + 0x34]
00362D27  83 F9 18                        cmp ecx, 0x18
00362D2A  0F 84 BA 07 00 00               je 0x1403634ea
00362D30  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00362D35  48 8D 1C 40                     lea rbx, [rax + rax*2]
00362D39  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00362D43  48 C1 E3 04                     shl rbx, 4
00362D47  48 8B C0                        mov rax, rax
00362D4A  48 03 D8                        add rbx, rax
00362D4D  E8 AE 4C FD FF                  call 0x140337a00
00362D52  80 7C 24 38 0A                  cmp byte ptr [rsp + 0x38], 0xa
00362D57  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
00362D5B  74 23                           je 0x140362d80
00362D5D  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00362D62  45 33 C9                        xor r9d, r9d
00362D65  49 8B D5                        mov rdx, r13
00362D68  45 8D 41 01                     lea r8d, [r9 + 1]
00362D6C  E8 DF F4 FF FF                  call 0x140362250
00362D71  45 33 C0                        xor r8d, r8d
00362D74  49 8B D5                        mov rdx, r13
00362D77  E8 5C 0C F3 FF                  call 0x1402939d8
00362D7C  49 8B 34 24                     mov rsi, qword ptr [r12]
00362D80  49 8B CC                        mov rcx, r12
00362D83  E8 68 3A FE FF                  call 0x1403467f0
00362D88  48 8B D0                        mov rdx, rax
00362D8B  48 8B CB                        mov rcx, rbx
00362D8E  E8 2D 12 00 00                  call 0x140363fc0
00362D93  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00362D9C  E8 3F F9 FF FF                  call 0x1403626e0
00362DA1  F7 05 59 3D C6 00 01 00 00 08   test dword ptr [rip + 0xc63d59], 0x8000001
00362DAB  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00362DAF  0F 85 7D 07 00 00               jne 0x140363532
00362DB5  45 33 ED                        xor r13d, r13d
00362DB8  45 8D 75 01                     lea r14d, [r13 + 1]
00362DBC  F0 48 0F BA 6B 18 3F            lock bts qword ptr [rbx + 0x18], 0x3f
00362DC3  0F 82 D8 02 00 00               jb 0x1403630a1
00362DC9  83 7D A0 00                     cmp dword ptr [rbp - 0x60], 0
00362DCD  49 8B CE                        mov rcx, r14
00362DD0  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
00362DD3  4C 8B 6D 88                     mov r13, qword ptr [rbp - 0x78]
00362DD7  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00362DDB  66 89 4C 24 30                  mov word ptr [rsp + 0x30], cx
00362DE0  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00362DE4  89 43 20                        mov dword ptr [rbx + 0x20], eax
00362DE7  74 09                           je 0x140362df2
00362DE9  48 8B 03                        mov rax, qword ptr [rbx]
00362DEC  48 0B C1                        or rax, rcx
00362DEF  48 89 03                        mov qword ptr [rbx], rax
00362DF2  8B D1                           mov edx, ecx
00362DF4  48 8B CB                        mov rcx, rbx
00362DF7  E8 64 FB FF FF                  call 0x140362960
00362DFC  41 8B 47 20                     mov eax, dword ptr [r15 + 0x20]
00362E00  4D 8B C6                        mov r8, r14
00362E03  C1 E8 10                        shr eax, 0x10
00362E06  48 8B CB                        mov rcx, rbx
00362E09  0F B6 D0                        movzx edx, al
00362E0C  C1 EA 06                        shr edx, 6
00362E0F  E8 1C 00 FD FF                  call 0x140332e30
00362E14  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00362E18  48 B9 01 00 00 00 00 00 00 C0   movabs rcx, 0xc000000000000001
00362E22  48 23 C1                        and rax, rcx
00362E25  49 8B D6                        mov rdx, r14
00362E28  48 0B C2                        or rax, rdx
00362E2B  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
00362E2F  8B 4B 20                        mov ecx, dword ptr [rbx + 0x20]
00362E32  8A 44 24 40                     mov al, byte ptr [rsp + 0x40]
00362E36  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00362E3A  C1 E9 18                        shr ecx, 0x18
00362E3D  32 C1                           xor al, cl
00362E3F  24 07                           and al, 7
00362E41  32 C1                           xor al, cl
00362E43  88 44 24 33                     mov byte ptr [rsp + 0x33], al
00362E47  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00362E4B  89 43 20                        mov dword ptr [rbx + 0x20], eax
00362E4E  4C 89 63 08                     mov qword ptr [rbx + 8], r12
00362E52  8B 43 20                        mov eax, dword ptr [rbx + 0x20]
00362E55  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00362E59  C1 E8 10                        shr eax, 0x10
00362E5C  24 FE                           and al, 0xfe
00362E5E  0C 06                           or al, 6
00362E60  83 7C 24 3C 00                  cmp dword ptr [rsp + 0x3c], 0
00362E65  88 44 24 32                     mov byte ptr [rsp + 0x32], al
00362E69  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00362E6D  89 43 20                        mov dword ptr [rbx + 0x20], eax
00362E70  0F 84 FC 03 00 00               je 0x140363272
00362E76  80 63 23 F7                     and byte ptr [rbx + 0x23], 0xf7
00362E7A  44 8B F7                        mov r14d, edi
00362E7D  41 83 E6 04                     and r14d, 4
00362E81  0F 85 B3 06 00 00               jne 0x14036353a
00362E87  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00362E91  F0 48 21 43 18                  lock and qword ptr [rbx + 0x18], rax
00362E96  45 85 F6                        test r14d, r14d
00362E99  0F 85 B3 06 00 00               jne 0x140363552
00362E9F  65 FF 04 25 94 2E 00 00         inc dword ptr gs:[0x2e94]
00362EA7  B9 02 00 00 00                  mov ecx, 2
00362EAC  41 BE 00 01 00 00               mov r14d, 0x100
00362EB2  84 4C 24 34                     test byte ptr [rsp + 0x34], cl
00362EB6  0F 85 06 03 00 00               jne 0x1403631c2
00362EBC  41 BE 08 01 00 00               mov r14d, 0x108
00362EC2  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
00362ECC  4C 3B E8                        cmp r13, rax
00362ECF  73 23                           jae 0x140362ef4
00362ED1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00362EDA  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00362EE1  8A 81 70 01 00 00               mov al, byte ptr [rcx + 0x170]
00362EE7  B9 01 00 00 00                  mov ecx, 1
00362EEC  84 C1                           test cl, al
00362EEE  0F 85 98 06 00 00               jne 0x14036358c
00362EF4  48 8B 55 A8                     mov rdx, qword ptr [rbp - 0x58]
00362EF8  45 8B C6                        mov r8d, r14d
00362EFB  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00362F00  E8 2B EC F4 FF                  call 0x1402b1b30
00362F05  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
00362F0A  49 8B C8                        mov rcx, r8
00362F0D  E8 C2 FA FF FF                  call 0x1403629d4
00362F12  85 C0                           test eax, eax
00362F14  0F 85 7B 03 00 00               jne 0x140363295
00362F1A  B8 40 00 00 00                  mov eax, 0x40
00362F1F  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00362F23  8D 50 C1                        lea edx, [rax - 0x3f]
00362F26  40 84 FA                        test dl, dil
00362F29  75 25                           jne 0x140362f50
00362F2B  48 85 F6                        test rsi, rsi
00362F2E  0F 89 5E 01 00 00               jns 0x140363092
00362F34  B8 50 00 00 00                  mov eax, 0x50
00362F39  48 83 CE 42                     or rsi, 0x42
00362F3D  83 C8 24                        or eax, 0x24
00362F40  48 0F BA F6 09                  btr rsi, 9
00362F45  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00362F49  48 81 CE 20 08 00 00            or rsi, 0x820
00362F50  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00362F55  48 B9 FF 0F 00 00 00 00 F0 FF   movabs rcx, 0xfff0000000000fff
00362F5F  48 C1 E0 0C                     shl rax, 0xc
00362F63  48 8B D8                        mov rbx, rax
00362F66  48 33 DE                        xor rbx, rsi
00362F69  48 23 D9                        and rbx, rcx
00362F6C  48 33 D8                        xor rbx, rax
00362F6F  F6 44 24 50 08                  test byte ptr [rsp + 0x50], 8
00362F74  0F 85 A7 01 00 00               jne 0x140363121
00362F7A  83 FF 08                        cmp edi, 8
00362F7D  73 4C                           jae 0x140362fcb
00362F7F  41 F6 C6 20                     test r14b, 0x20
00362F83  0F 85 D2 01 00 00               jne 0x14036315b
00362F89  F6 C3 42                        test bl, 0x42
00362F8C  0F 84 C9 01 00 00               je 0x14036315b
00362F92  44 8B C2                        mov r8d, edx
00362F95  48 8B C3                        mov rax, rbx
00362F98  8B 54 24 54                     mov edx, dword ptr [rsp + 0x54]
00362F9C  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00362FA0  48 0F BA E8 0A                  bts rax, 0xa
00362FA5  49 81 E5 00 F0 FF FF            and r13, 0xfffffffffffff000
00362FAC  49 8B CD                        mov rcx, r13
00362FAF  49 89 04 24                     mov qword ptr [r12], rax
00362FB3  E8 78 B7 F2 FF                  call 0x14028e730
00362FB8  48 0F BA 25 C7 3A C6 00 24      bt qword ptr [rip + 0xc63ac7], 0x24
00362FC1  0F 82 46 02 00 00               jb 0x14036320d
00362FC7  49 89 1C 24                     mov qword ptr [r12], rbx
00362FCB  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
00362FD0  41 BE 01 00 00 00               mov r14d, 1
00362FD6  44 39 74 24 3C                  cmp dword ptr [rsp + 0x3c], r14d
00362FDB  75 08                           jne 0x140362fe5
00362FDD  F0 48 FF 86 88 02 00 00         lock inc qword ptr [rsi + 0x288]
00362FE5  33 DB                           xor ebx, ebx
00362FE7  F0 49 0F BA 6F 18 3F            lock bts qword ptr [r15 + 0x18], 0x3f
00362FEE  0F 82 CE 00 00 00               jb 0x1403630c2
00362FF4  83 7C 24 3C 00                  cmp dword ptr [rsp + 0x3c], 0
00362FF9  0F 84 BE 02 00 00               je 0x1403632bd
00362FFF  33 D2                           xor edx, edx
00363001  49 8B CF                        mov rcx, r15
00363004  E8 67 0F FD FF                  call 0x140333f70
00363009  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00363013  F0 49 21 47 18                  lock and qword ptr [r15 + 0x18], rax
00363018  40 F6 C7 02                     test dil, 2
0036301C  75 2D                           jne 0x14036304b
0036301E  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00363023  8B 80 B8 00 00 00               mov eax, dword ptr [rax + 0xb8]
00363029  A8 0F                           test al, 0xf
0036302B  75 38                           jne 0x140363065
0036302D  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
00363031  48 8B CE                        mov rcx, rsi
00363034  E8 7B F6 06 00                  call 0x1403d26b4
00363039  48 85 C0                        test rax, rax
0036303C  74 27                           je 0x140363065
0036303E  4C 8B C6                        mov r8, rsi
00363041  48 8B C8                        mov rcx, rax
00363044  E8 87 89 EC FF                  call 0x14022b9d0
00363049  EB 11                           jmp 0x14036305c
0036304B  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
0036304F  45 33 C0                        xor r8d, r8d
00363052  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00363057  E8 E4 88 EC FF                  call 0x14022b940
0036305C  83 F8 03                        cmp eax, 3
0036305F  0F 84 30 05 00 00               je 0x140363595
00363065  33 C0                           xor eax, eax
00363067  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
0036306E  48 33 CC                        xor rcx, rsp
00363071  E8 CA 95 34 00                  call 0x1406ac640
00363076  48 8B 9C 24 E8 01 00 00         mov rbx, qword ptr [rsp + 0x1e8]
0036307E  48 81 C4 90 01 00 00            add rsp, 0x190
00363085  41 5F                           pop r15
00363087  41 5E                           pop r14
00363089  41 5D                           pop r13
0036308B  41 5C                           pop r12
0036308D  5F                              pop rdi
0036308E  5E                              pop rsi
0036308F  5D                              pop rbp
00363090  C3                              ret
00363091  CC                              int3
00363092  39 54 24 3C                     cmp dword ptr [rsp + 0x3c], edx
00363096  0F 84 A1 FE FF FF               je 0x140362f3d
0036309C  E9 93 FE FF FF                  jmp 0x140362f34
003630A1  45 03 EE                        add r13d, r14d
003630A4  44 85 2D 01 22 C6 00            test dword ptr [rip + 0xc62201], r13d
003630AB  0F 84 65 03 00 00               je 0x140363416
003630B1  F3 90                           pause
003630B3  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
003630B7  48 85 C0                        test rax, rax
003630BA  0F 89 FC FC FF FF               jns 0x140362dbc
003630C0  EB DF                           jmp 0x1403630a1
003630C2  41 03 DE                        add ebx, r14d
003630C5  85 1D E1 21 C6 00               test dword ptr [rip + 0xc621e1], ebx
003630CB  0F 84 6D 03 00 00               je 0x14036343e
003630D1  F3 90                           pause
003630D3  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
003630D7  48 85 C0                        test rax, rax
003630DA  0F 89 07 FF FF FF               jns 0x140362fe7
003630E0  EB E0                           jmp 0x1403630c2
003630E2  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
003630E6  4C 8D 15 53 4D AD 00            lea r10, [rip + 0xad4d53]
003630ED  48 0F BA E0 28                  bt rax, 0x28
003630F2  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
003630F7  41 8B FE                        mov edi, r14d
003630FA  0F 82 A5 FA FF FF               jb 0x140362ba5
00363100  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
00363104  48 85 C0                        test rax, rax
00363107  0F 88 98 FA FF FF               js 0x140362ba5
0036310D  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
00363111  48 85 C0                        test rax, rax
00363114  0F 84 8B FA FF FF               je 0x140362ba5
0036311A  0B FA                           or edi, edx
0036311C  E9 84 FA FF FF                  jmp 0x140362ba5
00363121  41 B8 04 00 00 00               mov r8d, 4
00363127  48 8B D3                        mov rdx, rbx
0036312A  49 8B CC                        mov rcx, r12
0036312D  E8 8E CF ED FF                  call 0x1402400c0
00363132  BA 01 00 00 00                  mov edx, 1
00363137  85 C0                           test eax, eax
00363139  0F 85 3B FE FF FF               jne 0x140362f7a
0036313F  83 CF 08                        or edi, 8
00363142  E9 33 FE FF FF                  jmp 0x140362f7a
00363147  B8 17 00 00 C0                  mov eax, 0xc0000017
0036314C  E9 16 FF FF FF                  jmp 0x140363067
00363151  B8 34 04 00 C0                  mov eax, 0xc0000434
00363156  E9 0C FF FF FF                  jmp 0x140363067
0036315B  48 F7 05 22 39 C6 00 00 00 00 02  test qword ptr [rip + 0xc63922], 0x2000000
00363166  74 03                           je 0x14036316b
00363168  0F AE E8                        lfence
0036316B  48 0F BA 25 14 39 C6 00 24      bt qword ptr [rip + 0xc63914], 0x24
00363174  0F 82 13 02 00 00               jb 0x14036338d
0036317A  48 8B C3                        mov rax, rbx
0036317D  49 8B CC                        mov rcx, r12
00363180  49 87 04 24                     xchg qword ptr [r12], rax
00363184  E8 77 C9 ED FF                  call 0x14023fb00
00363189  85 C0                           test eax, eax
0036318B  0F 85 02 03 00 00               jne 0x140363493
00363191  44 8B 44 24 40                  mov r8d, dword ptr [rsp + 0x40]
00363196  49 81 E5 00 F0 FF FF            and r13, 0xfffffffffffff000
0036319D  8B 54 24 54                     mov edx, dword ptr [rsp + 0x54]
003631A1  49 8B CD                        mov rcx, r13
003631A4  E8 87 B5 F2 FF                  call 0x14028e730
003631A9  E9 1D FE FF FF                  jmp 0x140362fcb
003631AE  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
003631B2  48 85 C0                        test rax, rax
003631B5  0F 84 B5 F9 FF FF               je 0x140362b70
003631BB  0B FA                           or edi, edx
003631BD  E9 AE F9 FF FF                  jmp 0x140362b70
003631C2  48 8B 05 BF 38 C6 00            mov rax, qword ptr [rip + 0xc638bf]
003631C9  48 0F BA E0 11                  bt rax, 0x11
003631CE  0F 82 EE FC FF FF               jb 0x140362ec2
003631D4  48 0F BA E0 0F                  bt rax, 0xf
003631D9  0F 83 E3 FC FF FF               jae 0x140362ec2
003631DF  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
003631E9  4C 3B E8                        cmp r13, rax
003631EC  0F 82 DF FC FF FF               jb 0x140362ed1
003631F2  41 BE 10 01 00 00               mov r14d, 0x110
003631F8  84 4C 24 50                     test byte ptr [rsp + 0x50], cl
003631FC  0F 84 F2 FC FF FF               je 0x140362ef4
00363202  41 BE 30 01 00 00               mov r14d, 0x130
00363208  E9 E7 FC FF FF                  jmp 0x140362ef4
0036320D  F6 C3 20                        test bl, 0x20
00363210  0F 85 B1 FD FF FF               jne 0x140362fc7
00363216  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00363220  48 8B C0                        mov rax, rax
00363223  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
0036322D  48 03 C1                        add rax, rcx
00363230  4C 3B E0                        cmp r12, rax
00363233  0F 82 8E FD FF FF               jb 0x140362fc7
00363239  41 B8 80 00 00 00               mov r8d, 0x80
0036323F  48 8B D3                        mov rdx, rbx
00363242  49 8B CC                        mov rcx, r12
00363245  E8 36 FB F2 FF                  call 0x140292d80
0036324A  E9 78 FD FF FF                  jmp 0x140362fc7
0036324F  C1 E0 10                        shl eax, 0x10
00363252  4C 8B CE                        mov r9, rsi
00363255  48 98                           cdqe
00363257  4D 8B C5                        mov r8, r13
0036325A  48 0B C2                        or rax, rdx
0036325D  B9 1A 00 00 00                  mov ecx, 0x1a
00363262  BA 00 33 00 00                  mov edx, 0x3300
00363267  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0036326C  E8 EF A3 19 00                  call 0x1404fd660
00363271  CC                              int3
00363272  41 8B 47 20                     mov eax, dword ptr [r15 + 0x20]
00363276  C1 E8 18                        shr eax, 0x18
00363279  A8 08                           test al, 8
0036327B  0F 84 F5 FB FF FF               je 0x140362e76
00363281  83 7C 24 60 00                  cmp dword ptr [rsp + 0x60], 0
00363286  0F 85 EA FB FF FF               jne 0x140362e76
0036328C  80 4B 23 08                     or byte ptr [rbx + 0x23], 8
00363290  E9 E5 FB FF FF                  jmp 0x140362e7a
00363295  49 8B C8                        mov rcx, r8
00363298  E8 03 E3 01 00                  call 0x1403815a0
0036329D  8B 4C 24 40                     mov ecx, dword ptr [rsp + 0x40]
003632A1  3B 88 30 44 00 00               cmp ecx, dword ptr [rax + 0x4430]
003632A7  0F 82 6D FC FF FF               jb 0x140362f1a
003632AD  49 8B D4                        mov rdx, r12
003632B0  49 8B C8                        mov rcx, r8
003632B3  E8 B8 D5 ED FF                  call 0x140240870
003632B8  E9 5D FC FF FF                  jmp 0x140362f1a
003632BD  83 7C 24 60 00                  cmp dword ptr [rsp + 0x60], 0
003632C2  0F 85 37 FD FF FF               jne 0x140362fff
003632C8  41 8B 47 20                     mov eax, dword ptr [r15 + 0x20]
003632CC  C1 E8 18                        shr eax, 0x18
003632CF  A8 08                           test al, 8
003632D1  0F 84 28 FD FF FF               je 0x140362fff
003632D7  41 80 67 23 F7                  and byte ptr [r15 + 0x23], 0xf7
003632DC  E9 1E FD FF FF                  jmp 0x140362fff
003632E1  83 F8 02                        cmp eax, 2
003632E4  72 36                           jb 0x14036331c
003632E6  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
003632EA  45 33 C0                        xor r8d, r8d
003632ED  48 8B 0D 94 CD AC 00            mov rcx, qword ptr [rip + 0xaccd94]
003632F4  48 C1 E8 2B                     shr rax, 0x2b
003632F8  25 FF 03 00 00                  and eax, 0x3ff
003632FD  48 8B 1C C1                     mov rbx, qword ptr [rcx + rax*8]
00363301  48 8B CB                        mov rcx, rbx
00363304  E8 07 51 EE FF                  call 0x140248410
00363309  BA 01 00 00 00                  mov edx, 1
0036330E  39 54 24 3C                     cmp dword ptr [rsp + 0x3c], edx
00363312  75 08                           jne 0x14036331c
00363314  F0 48 FF 8B B0 4C 00 00         lock dec qword ptr [rbx + 0x4cb0]
0036331C  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
00363320  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
0036332A  48 23 C1                        and rax, rcx
0036332D  48 8D 0C 40                     lea rcx, [rax + rax*2]
00363331  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0036333B  48 C1 E1 04                     shl rcx, 4
0036333F  48 8B C0                        mov rax, rax
00363342  48 03 C8                        add rcx, rax
00363345  E8 F6 4D 0A 00                  call 0x140408140
0036334A  BA 01 00 00 00                  mov edx, 1
0036334F  E9 CF F9 FF FF                  jmp 0x140362d23
00363354  41 8B 4F 20                     mov ecx, dword ptr [r15 + 0x20]
00363358  C1 E9 18                        shr ecx, 0x18
0036335B  F6 C1 08                        test cl, 8
0036335E  0F 84 A6 F8 FF FF               je 0x140362c0a
00363364  24 FA                           and al, 0xfa
00363366  41 0A C0                        or al, r8b
00363369  E9 9C F8 FF FF                  jmp 0x140362c0a
0036336E  41 8B 4F 10                     mov ecx, dword ptr [r15 + 0x10]
00363372  44 8B DA                        mov r11d, edx
00363375  48 0F BA E1 0A                  bt rcx, 0xa
0036337A  B9 02 00 00 00                  mov ecx, 2
0036337F  44 0F 42 D9                     cmovb r11d, ecx
00363383  44 89 5C 24 30                  mov dword ptr [rsp + 0x30], r11d
00363388  E9 94 F8 FF FF                  jmp 0x140362c21
0036338D  8A C3                           mov al, bl
0036338F  24 21                           and al, 0x21
00363391  3A C2                           cmp al, dl
00363393  0F 85 E1 FD FF FF               jne 0x14036317a
00363399  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
003633A3  48 8B C0                        mov rax, rax
003633A6  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
003633B0  48 03 C1                        add rax, rcx
003633B3  4C 3B E0                        cmp r12, rax
003633B6  0F 82 BE FD FF FF               jb 0x14036317a
003633BC  41 B8 80 00 00 00               mov r8d, 0x80
003633C2  48 8B D3                        mov rdx, rbx
003633C5  49 8B CC                        mov rcx, r12
003633C8  E8 B3 F9 F2 FF                  call 0x140292d80
003633CD  E9 A8 FD FF FF                  jmp 0x14036317a
003633D2  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
003633D6  4C 8D 15 E3 4C AD 00            lea r10, [rip + 0xad4ce3]
003633DD  41 8B FE                        mov edi, r14d
003633E0  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
003633E5  0B FA                           or edi, edx
003633E7  48 0F BA E0 28                  bt rax, 0x28
003633EC  72 09                           jb 0x1403633f7
003633EE  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
003633F2  48 85 C0                        test rax, rax
003633F5  79 6E                           jns 0x140363465
003633F7  4C 8B CE                        mov r9, rsi
003633FA  48 C7 44 24 20 00 00 05 00      mov qword ptr [rsp + 0x20], 0x50000
00363403  4D 8B C5                        mov r8, r13
00363406  BA 00 33 00 00                  mov edx, 0x3300
0036340B  B9 1A 00 00 00                  mov ecx, 0x1a
00363410  E8 4B A2 19 00                  call 0x1404fd660
00363415  CC                              int3
00363416  8B 05 9C 36 C6 00               mov eax, dword ptr [rip + 0xc6369c]
0036341C  A8 40                           test al, 0x40
0036341E  0F 84 8D FC FF FF               je 0x1403630b1
00363424  E8 67 C0 FA FF                  call 0x14030f490
00363429  84 C0                           test al, al
0036342B  0F 84 80 FC FF FF               je 0x1403630b1
00363431  41 8B CD                        mov ecx, r13d
00363434  E8 27 C0 FA FF                  call 0x14030f460
00363439  E9 75 FC FF FF                  jmp 0x1403630b3
0036343E  8B 05 74 36 C6 00               mov eax, dword ptr [rip + 0xc63674]
00363444  A8 40                           test al, 0x40
00363446  0F 84 85 FC FF FF               je 0x1403630d1
0036344C  E8 3F C0 FA FF                  call 0x14030f490
00363451  84 C0                           test al, al
00363453  0F 84 78 FC FF FF               je 0x1403630d1
00363459  8B CB                           mov ecx, ebx
0036345B  E8 00 C0 FA FF                  call 0x14030f460
00363460  E9 6E FC FF FF                  jmp 0x1403630d3
00363465  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
00363469  48 85 C0                        test rax, rax
0036346C  0F 85 33 F7 FF FF               jne 0x140362ba5
00363472  EB 83                           jmp 0x1403633f7
00363474  4C 8B CE                        mov r9, rsi
00363477  48 C7 44 24 20 01 00 04 00      mov qword ptr [rsp + 0x20], 0x40001
00363480  4D 8B C5                        mov r8, r13
00363483  BA 00 33 00 00                  mov edx, 0x3300
00363488  B9 1A 00 00 00                  mov ecx, 0x1a
0036348D  E8 CE A1 19 00                  call 0x1404fd660
00363492  CC                              int3
00363493  48 8B D3                        mov rdx, rbx
00363496  49 8B CC                        mov rcx, r12
00363499  E8 0E 1A F3 FF                  call 0x140294eac
0036349E  E9 EE FC FF FF                  jmp 0x140363191
003634A3  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
003634A7  41 B9 10 00 00 00               mov r9d, 0x10
003634AD  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
003634B2  44 8B C3                        mov r8d, ebx
003634B5  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
003634BA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003634BF  41 8D 51 F8                     lea edx, [r9 - 8]
003634C3  E8 F4 3A 01 00                  call 0x140376fbc
003634C8  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
003634CD  48 83 F8 FF                     cmp rax, -1
003634D1  0F 85 3B F8 FF FF               jne 0x140362d12
003634D7  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
003634DB  48 83 38 00                     cmp qword ptr [rax], 0
003634DF  0F 85 62 FC FF FF               jne 0x140363147
003634E5  E9 07 F8 FF FF                  jmp 0x140362cf1
003634EA  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
003634EF  89 54 24 34                     mov dword ptr [rsp + 0x34], edx
003634F3  48 85 DB                        test rbx, rbx
003634F6  0F 85 FA FB 37 00               jne 0x1406e30f6
003634FC  8B CA                           mov ecx, edx
003634FE  E8 ED 8B F1 FF                  call 0x14027c0f0
00363503  49 8B CD                        mov rcx, r13
00363506  E8 C5 33 FB FF                  call 0x1403168d0
0036350B  B2 11                           mov dl, 0x11
0036350D  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00363512  B9 01 00 00 00                  mov ecx, 1
00363517  48 8B D8                        mov rbx, rax
0036351A  E8 01 3B F3 FF                  call 0x140297020
0036351F  48 85 DB                        test rbx, rbx
00363522  0F 84 09 FC 37 00               je 0x1406e3131
00363528  BA 01 00 00 00                  mov edx, 1
0036352D  E9 C4 FB 37 00                  jmp 0x1406e30f6
00363532  83 CF 04                        or edi, 4
00363535  E9 7B F8 FF FF                  jmp 0x140362db5
0036353A  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0036353F  48 8D 55 B0                     lea rdx, [rbp - 0x50]
00363543  E8 78 95 FB FF                  call 0x14031cac0
00363548  BA 01 00 00 00                  mov edx, 1
0036354D  E9 35 F9 FF FF                  jmp 0x140362e87
00363552  48 83 4D C8 08                  or qword ptr [rbp - 0x38], 8
00363557  48 8D 45 B0                     lea rax, [rbp - 0x50]
0036355B  83 65 7C 00                     and dword ptr [rbp + 0x7c], 0
0036355F  48 8D 4D 70                     lea rcx, [rbp + 0x70]
00363563  41 B9 82 02 00 00               mov r9d, 0x282
00363569  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
0036356D  41 B8 01 00 00 28               mov r8d, 0x28000001
00363573  C7 45 78 20 00 00 00            mov dword ptr [rbp + 0x78], 0x20
0036357A  C7 44 24 20 04 1B 50 11         mov dword ptr [rsp + 0x20], 0x11501b04
00363582  E8 C9 1D ED FF                  call 0x140235350
00363587  E9 13 F9 FF FF                  jmp 0x140362e9f
0036358C  41 83 CE 10                     or r14d, 0x10
00363590  E9 5F F9 FF FF                  jmp 0x140362ef4
00363595  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0036359A  41 B8 04 00 00 00               mov r8d, 4
003635A0  49 8B D6                        mov rdx, r14
003635A3  E8 08 39 F2 FF                  call 0x140286eb0
003635A8  E9 B8 FA FF FF                  jmp 0x140363065
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCopyOnWrite(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_r11;
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
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned int v_stack_m174;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int8 v_stack_m186;
    unsigned int v_stack_m188;
    unsigned int v_stack_m18C;
    unsigned __int8 v_stack_m190;
    unsigned int v_stack_m194;
    unsigned __int8 v_stack_m195;
    unsigned __int8 v_stack_m196;
    unsigned int v_stack_m198;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned int v_stack_p3C;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int8 v_stack_p50;
    unsigned int v_stack_p54;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (400);
    result = (*(unsigned __int64 *)(v_rip + 11173134)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m178 = a4;
    v_stack_m170 = a3;
    v_stack_m140 = a1;
    v_stack_m58 = a5;
    v_stack_m138 = v_xmm0;
    v_stack_m118 = v_xmm1;
    v_stack_m108 = v_xmm1;
    if (a5 != 0) {
    }
    result = (*(unsigned __int64 *)(a2)) >> (12);
    result = (result) & (a1);
    v_stack_m120 = result;
    v_r15 = (result + result * 2) << (4);
    v_r15 = (v_r15) + (result);
    v_r14 = (*(unsigned __int64 *)(a2)) >> (9);
    v_rbx = 0;
    v_r14 = (unsigned int)(~(v_r14));
    v_r14 = (unsigned int)((v_r14) & (1));
    result = (*(unsigned __int64 *)(v_r15 + 8)) | (a1);
    v_stack_m148 = result;
    v_stack_m150 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    result = MiGetSystemRegionType(a1, a2, a3, a4);
    v_r11 = 0;
    v_stack_m18C = 0;
    v_stack_m174 = (unsigned int)(v_rbx + 1);
    if (((unsigned int)(result)) == 11) goto loc_003630E2;
    if (((unsigned int)(result)) > 15) goto loc_00362B22;
    if (((unsigned int)(result)) < 15) goto loc_0036324F;
loc_00362B22:
    if (((unsigned int)(result)) == 5) goto loc_003633D2;
    if (((unsigned int)(result)) == 4) goto loc_00363474;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 624)) != 0) goto loc_00363151;
    v_stack_m180 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024;
    v_stack_m18C = (unsigned int)(v_rbx + 1);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 624)) < 0) goto loc_00362B70;
    if (!sign_flag) goto loc_003631AE;
loc_00362B70:
    a2 = 0;
    result = memset(v_stack_mF8, a2, 152, a4);
    v_stack_mC0 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1024;
    a2 = 0;
    v_stack_mF8 = a1;
    result = MiComputeFaultNode(v_stack_mF8, a2, v_stack_m160, a4);
loc_00362BA5:
    v_r14 = (*(unsigned __int64 *)(v_r15)) & (1);
    v_stack_m128 = v_r14;
    v_stack_m158 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11326676) + *(unsigned __int16 *)(v_stack_m180 + 174) * 8);
    result = MiGetWsleContents(*(unsigned __int64 *)(v_rip + 11326676), a1, v_stack_m160, a4);
    a1 = (unsigned int)(((unsigned int)(v_stack_m178)) & ((unsigned int)(9 - 8)));
    v_stack_m168 = (unsigned int)(a1);
    if (condition_is_not_equal) goto loc_00362C0A;
    a1 = (unsigned __int8)(((unsigned __int8)(result)) & (15));
    if (((unsigned __int8)(a1)) == 10) goto loc_00362C0A;
    if (((unsigned __int8)(a1)) == 9) goto loc_00363364;
    if (((unsigned int)((unsigned int)(v_stack_m18C))) != ((unsigned int)(9 - 8))) goto loc_00363354;
loc_00362C0A:
    a1 = (unsigned __int8)(((unsigned __int8)(result)) & (15));
    v_stack_m190 = (unsigned __int8)(a1);
    if (((unsigned __int8)(a1)) == 10) goto loc_00362C34;
    if (((unsigned __int8)(a1)) == 8) goto loc_0036336E;
loc_00362C21:
    result = MiGetWsleProtection(a1, (unsigned __int8)(result), 10, 9);
    if ((unsigned int)(result) == 0) {
        result = *(unsigned int *)(v_r15 + 16);
        result = (result) >> (5);
        result = (unsigned int)((result) & (31));
    }
    v_stack_m194 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 3550280 + (unsigned int)((unsigned int)(result)) * 4 + 69744)));
    if (v_stack_m170 != -1) goto loc_00362D12;
    v_stack_m188 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 32)));
    result = MiInitializePageColorBase(v_stack_m180, 3, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m138);
    result = (unsigned int)(((unsigned int)(v_stack_m130)) & (0xFFF3FFFFULL));
    a4 = (unsigned int)((v_stack_m186) & (0xFFFFFFC0ULL));
    a4 = (unsigned int)((a4) << (12));
    a4 = (unsigned int)((a4) | ((unsigned int)(result)));
    v_stack_m130 = a4;
    a2 = 0;
    a1 = ((unsigned int)(a4)) >> (16);
    a1 = (unsigned int)((a1) & (3));
    a2 = (unsigned int)((a2) ^ (a4));
    v_rbx = (unsigned int)(((unsigned __int8)(a2)) ^ (a4));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m180 + 184)))) & (15)) != 0) goto loc_00362CF1;
    result = MiGetCurrentSlabIdentity(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, v_rip - 3550385, a4);
    if (((unsigned __int8)(result)) != 255) goto loc_003634A3;
loc_00362CF1:
    result = MiGetPage(v_stack_m158, (unsigned int)((unsigned int)(v_rbx)), 1, a4);
    v_stack_m170 = result;
    if (result == -1) goto loc_00363147;
loc_00362D12:
    if (((unsigned int)((unsigned int)(v_stack_m198))) >= 1) goto loc_003632E1;
loc_00362D23:
    if (((unsigned int)((unsigned int)(v_stack_m194))) == 24) goto loc_003634EA;
    v_rbx = (v_stack_m170 + v_stack_m170 * 2) << (4);
    v_rbx = (v_rbx) + (v_stack_m170);
    result = MiMakeDemandZeroPte((unsigned int)(v_stack_m194), 1, 1, a4);
    *(unsigned __int64 *)(v_rbx + 16) = result;
    v_rsi = *(unsigned __int64 *)(a2);
    if (v_stack_m190 != 10) {
        a1 = v_stack_m180;
        a4 = 0;
        a2 = a1;
        a3 = a4 + 1;
        result = MiUpdateWorkingSetPrivateSize(a1, a2, a3, a4);
        a3 = 0;
        a2 = a1;
        result = MiSetWsleProtection(a1, a2, a3, a4);
        v_rsi = *(unsigned __int64 *)(a2);
    }
    result = MiGetContainingPageTable(a2, a2, a3, a4);
    result = MiSetPfnContainingFrame(v_rbx, result, a3, a4);
    result = MiGetEffectivePagePriorityThread(*(unsigned __int64 *)(gs_base + (0 + 392)), result, a3, a4);
    v_stack_m188 = (unsigned int)(result);
    if (((*(unsigned int *)(v_rip + 12991833)) & (0x8000001ULL)) != 0) goto loc_00363532;
loc_00362DB5:
    v_r13 = 0;
loc_00362DBC:
    if (condition_is_below) goto loc_003630A1;
    v_stack_m198 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 32)));
    v_stack_m198 = (unsigned __int16)(v_r13 + 1);
    *(unsigned int *)(v_rbx + 32) = (unsigned int)((unsigned int)(v_stack_m198));
    result = (unsigned int)(v_stack_m198);
    if (v_stack_m128 != 0) {
        result = *(unsigned __int64 *)(v_rbx);
        result = (result) | (v_r13 + 1);
        *(unsigned __int64 *)(v_rbx) = result;
    }
    result = MiSetPfnModified(v_rbx, (unsigned int)((unsigned int)(v_r13 + 1)), a3, a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 32))) >> (16));
    a2 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    result = MiFinalizePageAttribute(v_rbx, a2, v_r13 + 1, a4);
    result = (*(unsigned __int64 *)(v_rbx + 24)) & (v_rbx);
    result = (result) | (v_r13 + 1);
    *(unsigned __int64 *)(v_rbx + 24) = result;
    v_stack_m198 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 32)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 32))) >> (24));
    result = (unsigned __int8)((v_stack_m188) ^ ((unsigned __int8)(a1)));
    result = (unsigned __int8)((result) & (7));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a1)));
    v_stack_m195 = (unsigned __int8)(result);
    *(unsigned int *)(v_rbx + 32) = (unsigned int)((unsigned int)(v_stack_m198));
    *(unsigned __int64 *)(v_rbx + 8) = a2;
    v_stack_m198 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 32))) >> (16));
    result = (unsigned __int8)((result) & (254));
    result = (unsigned __int8)((result) | (6));
    v_stack_m196 = (unsigned __int8)(result);
    *(unsigned int *)(v_rbx + 32) = (unsigned int)((unsigned int)(v_stack_m198));
    if (v_stack_m18C == 0) goto loc_00363272;
loc_00362E76:
loc_00362E7A:
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r14))))) & (4));
    if (condition_is_not_equal) goto loc_0036353A;
loc_00362E87:
    if ((unsigned int)(v_r14) != 0) goto loc_00363552;
loc_00362E9F:
    if (((v_stack_m194) & (2)) != 0) goto loc_003631C2;
loc_00362EC2:
    if (v_stack_m140 >= ((unsigned int)(v_stack_m198))) goto loc_00362EF4;
loc_00362ED1:
    if (((1) & ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 368)))) != 0) goto loc_0036358C;
loc_00362EF4:
    result = MiCopyPage(v_stack_m170, v_stack_m120, 264, a4);
    result = MiVmAccessLoggingEnabled(v_stack_m180, v_stack_m120, v_stack_m180, a4);
    if ((unsigned int)(result) != 0) goto loc_00363295;
loc_00362F1A:
    v_stack_m188 = 64;
    if ((((unsigned __int8)(64 - 63)) & ((unsigned __int8)((unsigned int)((unsigned int)(v_r14))))) != 0) goto loc_00362F50;
    if (!sign_flag) goto loc_00363092;
loc_00362F34:
    v_rsi = (v_rsi) | (66);
loc_00362F3D:
    result = (unsigned int)((80) | (36));
    v_stack_m188 = (unsigned int)(result);
    v_rsi = (v_rsi) | (0x820ULL);
loc_00362F50:
    result = (v_stack_m170) << (12);
    v_rbx = (result) ^ (v_rsi);
    v_rbx = (v_rbx) & (v_stack_m180);
    v_rbx = (v_rbx) ^ (result);
    if (((v_stack_m178) & (8)) != 0) goto loc_00363121;
loc_00362F7A:
    if (((unsigned int)((unsigned int)((unsigned int)(v_r14)))) >= 8) goto loc_00362FCB;
    if (((264) & (32)) != 0) goto loc_0036315B;
    if ((((unsigned __int8)(v_rbx)) & (66)) == 0) goto loc_0036315B;
    result = (v_rbx) & (-2);
    v_r13 = (v_stack_m140) & (0xFFFFFFFFFFFFF000ULL);
    *(unsigned __int64 *)(a2) = result;
    result = MiFlushSingleTbEntry(v_r13, (unsigned int)(v_stack_m174), (unsigned int)((unsigned int)(64 - 63)), a4);
    if (condition_is_below) goto loc_0036320D;
loc_00362FC7:
    *(unsigned __int64 *)(a2) = v_rbx;
loc_00362FCB:
    if (v_stack_m18C == 1) {
    }
    v_rbx = 0;
loc_00362FE7:
    if (condition_is_below) goto loc_003630C2;
    if (v_stack_m18C == 0) goto loc_003632BD;
loc_00362FFF:
    a2 = 0;
    result = MiDecrementShareCountEx(v_r15, a2, (unsigned int)((unsigned int)(64 - 63)), a4);
    if ((((unsigned __int8)((unsigned int)((unsigned int)(v_r14)))) & (2)) != 0) goto loc_0036304B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m180 + 184)))) & (15)) != 0) goto loc_00363065;
    result = MiLocateCloneAddress(v_stack_m150, v_stack_m148, (unsigned int)((unsigned int)(64 - 63)), a4);
    if (result == 0) goto loc_00363065;
    result = MiDecrementCloneBlockReference(result, v_stack_m148, v_stack_m150, a4);
    goto loc_0036305C;
loc_0036304B:
    a3 = 0;
    result = MiDecrementCombinedPteEx(v_stack_m180, v_stack_m148, a3, a4);
loc_0036305C:
    if (((unsigned int)(result)) == 3) goto loc_00363595;
loc_00363065:
    result = 0;
loc_00363067:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m148, a3, a4);
    v_rsp = (v_rsp) + (400);
    return result;
loc_00363092:
    if (v_stack_p3C == ((unsigned int)(v_stack_m148))) goto loc_00362F3D;
    goto loc_00362F34;
loc_003630A1:
    v_r13 = (unsigned int)((v_r13) + (1));
    if (((*(unsigned int *)(v_rip + 12984833)) & ((unsigned int)(v_r13))) == 0) goto loc_00363416;
loc_003630B1:
loc_003630B3:
    if (!sign_flag) goto loc_00362DBC;
    goto loc_003630A1;
loc_003630C2:
    v_rbx = (unsigned int)((v_stack_p20) + (1));
    if (((*(unsigned int *)(v_rip + 12984801)) & ((unsigned int)(v_rbx))) == 0) goto loc_0036343E;
loc_003630D1:
loc_003630D3:
    if (!sign_flag) goto loc_00362FE7;
    goto loc_003630C2;
loc_003630E2:
    v_stack_p48 = v_rip + 11357523;
    if (condition_is_below) goto loc_00362BA5;
    if (sign_flag) goto loc_00362BA5;
    if (*(unsigned __int64 *)(v_r15 + 8) == 0) goto loc_00362BA5;
    v_rdi = (unsigned int)((1) | ((unsigned int)(v_stack_m148)));
    goto loc_00362BA5;
loc_00363121:
    result = MI_WRITE_INVALID_PTE_TB_FLUSH_NEEDED(0, v_rbx, 4, a4);
    if ((unsigned int)(result) != 0) goto loc_00362F7A;
    v_rdi = (unsigned int)((v_rdi) | (8));
    goto loc_00362F7A;
loc_00363147:
    goto loc_00363067;
loc_00363151:
    goto loc_00363067;
loc_0036315B:
    if (((*(unsigned __int64 *)(v_rip + 12990754)) & (0x2000000ULL)) != 0) {
    }
    if (condition_is_below) goto loc_0036338D;
loc_0036317A:
    result = MiPteInShadowRange(0, 1, 4, a4);
    if ((unsigned int)(result) != 0) goto loc_00363493;
loc_00363191:
    v_r13 = (v_r13) & (0xFFFFFFFFFFFFF000ULL);
    result = MiFlushSingleTbEntry(v_r13, (unsigned int)(v_stack_p54), (unsigned int)(v_stack_p40), a4);
    goto loc_00362FCB;
loc_003631AE:
    if (*(unsigned __int64 *)(v_r15 + 8) == 0) goto loc_00362B70;
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)((unsigned int)(v_stack_p54))));
    goto loc_00362B70;
loc_003631C2:
    if (condition_is_below) goto loc_00362EC2;
    if (condition_is_above_or_equal) goto loc_00362EC2;
    if (v_r13 < (*(unsigned __int64 *)(v_rip + 12990655))) goto loc_00362ED1;
    if (((v_stack_p50) & ((unsigned __int8)(v_r13))) == 0) goto loc_00362EF4;
    goto loc_00362EF4;
loc_0036320D:
    if ((((unsigned __int8)(v_rbx)) & (32)) != 0) goto loc_00362FC7;
    result = (*(unsigned __int64 *)(v_rip + 12990655)) + (v_r13);
    if (0 < result) goto loc_00362FC7;
    result = MiCheckLinearProtectedPteAccessedBit(0, v_rbx, 128, a4);
    goto loc_00362FC7;
loc_0036324F:
    result = (unsigned int)((result) << (16));
    result = (result) | (v_rbx);
    v_stack_p20 = result;
    result = KeBugCheckEx(26, (unsigned int)(0x3300ULL), v_r13, v_stack_m150);
loc_00363272:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (8)) == 0) goto loc_00362E76;
    if (v_stack_p60 != 0) goto loc_00362E76;
    goto loc_00362E7A;
loc_00363295:
    result = MiGetVmAccessLoggingPartition(v_r13, (unsigned int)(0x3300ULL), v_r13, v_stack_m150);
    if (((unsigned int)((unsigned int)(v_stack_p40))) < (*(unsigned int *)(result + 17456))) goto loc_00362F1A;
    result = MiLogPageAccess(v_r13, 0, v_r13, v_stack_m150);
    goto loc_00362F1A;
loc_003632BD:
    if (v_stack_p60 != 0) goto loc_00362FFF;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (8)) == 0) goto loc_00362FFF;
    goto loc_00362FFF;
loc_003632E1:
    if (((unsigned int)(result)) < 2) goto loc_0036331C;
    a3 = 0;
    result = (*(unsigned __int64 *)(v_r15 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    result = MiReturnCommit(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11324820) + result * 8), 0, a3, v_stack_m150);
    if (v_stack_p3C == 1) {
    }
    result = (*(unsigned __int64 *)(v_r15 + 40)) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11324820) + result * 8));
    a1 = (result + result * 2) << (4);
    a1 = (a1) + (result);
    result = MiUnlockPageTableCharges(a1, 1, a3, v_stack_m150);
    goto loc_00362D23;
loc_00363354:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 32))) >> (24));
    if ((((unsigned __int8)(a1)) & (8)) == 0) goto loc_00362C0A;
loc_00363364:
    result = (unsigned __int8)((result) & (250));
    result = (unsigned __int8)((result) | (0));
    goto loc_00362C0A;
loc_0036336E:
    v_r11 = 1;
    if (condition_is_below) { v_r11 = 2; }
    v_stack_p30 = (unsigned int)(v_r11);
    goto loc_00362C21;
loc_0036338D:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11324820) + result * 8))) & (33));
    if (((unsigned __int8)(result)) != 1) goto loc_0036317A;
    result = (result) + (2);
    if (0 < result) goto loc_0036317A;
    result = MiCheckLinearProtectedPteAccessedBit(0, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11324820) + result * 8), 128, v_stack_m150);
    goto loc_0036317A;
loc_003633D2:
    v_stack_p48 = v_rip + 11357411;
    v_rdi = (unsigned int)((304) | ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11324820) + result * 8))));
    if (condition_is_below) goto loc_003633F7;
    if (!sign_flag) goto loc_00363465;
loc_003633F7:
    v_stack_p20 = 0x50000ULL;
    result = KeBugCheckEx(26, (unsigned int)(0x3300ULL), v_r13, v_stack_m150);
loc_00363416:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12990108)))) & (64)) == 0) goto loc_003630B1;
    result = KiCheckVpBackingLongSpinWaitHypercall(26, (unsigned int)(0x3300ULL), v_r13, v_stack_m150);
    if ((unsigned __int8)(result) == 0) goto loc_003630B1;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r13)), (unsigned int)(0x3300ULL), v_r13, v_stack_m150);
    goto loc_003630B3;
loc_0036343E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12990068)))) & (64)) == 0) goto loc_003630D1;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_r13)), (unsigned int)(0x3300ULL), v_r13, v_stack_m150);
    if ((unsigned __int8)(result) == 0) goto loc_003630D1;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11324820) + result * 8))), (unsigned int)(0x3300ULL), v_r13, v_stack_m150);
    goto loc_003630D3;
loc_00363465:
    if (*(unsigned __int64 *)(v_r15 + 8) != 0) goto loc_00362BA5;
    goto loc_003633F7;
loc_00363474:
    v_stack_p20 = 0x40001ULL;
    result = KeBugCheckEx(26, (unsigned int)(0x3300ULL), v_r13, v_stack_m150);
loc_00363493:
    result = MiWritePteShadow(0, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11324820) + result * 8), v_r13, v_stack_m150);
    goto loc_00363191;
loc_003634A3:
    v_stack_p20 = v_stack_m58;
    result = MiGetSlabPage(v_stack_p70, 16 - 8, (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11324820) + result * 8))), 16);
    v_stack_p58 = result;
    if (result != -1) goto loc_00362D12;
    if ((*(unsigned __int64 *)(v_stack_m58)) != 0) goto loc_00363147;
    goto loc_00362CF1;
loc_003634EA:
    v_stack_p34 = (unsigned int)(16 - 8);
    result = MiLockVadTree((unsigned int)((unsigned int)(16 - 8)), 16 - 8, (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11324820) + result * 8))), 16);
    result = MiLocateAddress(v_r13, 16 - 8, (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11324820) + result * 8))), 16);
    v_stack_p68 = result;
    result = MiUnlockVadTree(1, 17, (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11324820) + result * 8))), 16);
loc_00363532:
    v_rdi = (unsigned int)((v_rdi) | (4));
    goto loc_00362DB5;
loc_0036353A:
    result = MiIdentifyPfn(v_stack_p58, v_stack_m118, (unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11324820) + result * 8))), 16);
    goto loc_00362E87;
loc_00363552:
    v_stack_m58 = v_stack_m118;
    v_stack_m50 = 32;
    v_stack_p20 = 0x11501B04ULL;
    result = EtwTraceKernelEvent(v_stack_m58, 1, (unsigned int)(0x28000001ULL), 642);
    goto loc_00362E9F;
loc_0036358C:
    v_r14 = (unsigned int)((304) | (16));
    goto loc_00362EF4;
loc_00363595:
    result = MiChargeCommit(v_stack_p70, v_r14, 4, 642);
    goto loc_00363065;
}
```

## 5. (Beta) C Style

```c
int64_t MiCopyOnWrite(int64_t Arg1, void *Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r11;
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
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint32_t v_stack_m168;
    uint64_t v_stack_m170;
    uint32_t v_stack_m174;
    uint32_t v_stack_m178;
    uint64_t v_stack_m180;
    uint8_t v_stack_m186;
    uint32_t v_stack_m188;
    uint32_t v_stack_m18C;
    uint8_t v_stack_m190;
    uint32_t v_stack_m194;
    uint8_t v_stack_m195;
    uint8_t v_stack_m196;
    uint32_t v_stack_m198;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint32_t v_stack_p3C;
    uint32_t v_stack_p40;
    uint64_t v_stack_p48;
    uint8_t v_stack_p50;
    uint32_t v_stack_p54;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (400);
    result = (*(uint64_t *)(v_rip + 0xAA7D0E)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m178 = Arg4;
    v_stack_m170 = Arg3;
    v_stack_m140 = Arg1;
    v_stack_m58 = Arg5;
    v_stack_m138 = v_xmm0;
    v_stack_m118 = v_xmm1;
    v_stack_m108 = v_xmm1;
    if (Arg5 != 0) {
    }
    result = (*(uint64_t *)(arg2)) >> (12);
    result = (result) & (Arg1);
    v_stack_m120 = result;
    local_r15 = (result + result * 2) << (4);
    local_r15 = (local_r15) + (result);
    local_r14 = (*(uint64_t *)(arg2)) >> (9);
    local_rbx = 0;
    local_r14 = (uint32_t)(~(local_r14));
    local_r14 = (uint32_t)((local_r14) & (1));
    result = (*(uint64_t *)(local_r15 + 0x8)) | (Arg1);
    v_stack_m148 = result;
    v_stack_m150 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    result = MiGetSystemRegionType(Arg1, Arg2, Arg3, Arg4);
    local_r11 = 0;
    v_stack_m18C = 0;
    v_stack_m174 = (uint32_t)(local_rbx + 1);
    if (((uint32_t)(result)) == 11) goto loc_003630E2;
    if (((uint32_t)(result)) > 15) goto loc_00362B22;
    if (((uint32_t)(result)) < 15) goto loc_0036324F;
loc_00362B22:
    if (((uint32_t)(result)) == 5) goto loc_003633D2;
    if (((uint32_t)(result)) == 4) goto loc_00363474;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x270)) != 0) goto loc_00363151;
    v_stack_m180 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024;
    v_stack_m18C = (uint32_t)(local_rbx + 1);
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x270)) < 0) goto loc_00362B70;
    if (!sign_flag) goto loc_003631AE;
loc_00362B70:
    Arg2 = 0;
    result = memset(v_stack_mF8, Arg2, 152, Arg4);
    v_stack_mC0 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 1024;
    Arg2 = 0;
    v_stack_mF8 = Arg1;
    result = MiComputeFaultNode(v_stack_mF8, Arg2, v_stack_m160, Arg4);
loc_00362BA5:
    local_r14 = (*(uint64_t *)(local_r15)) & (1);
    v_stack_m128 = local_r14;
    v_stack_m158 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xACD4D4) + *(uint16_t *)(v_stack_m180 + 0xAE) * 8);
    result = MiGetWsleContents(*(uint64_t *)(v_rip + 0xACD4D4), Arg1, v_stack_m160, Arg4);
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m178)) & ((uint32_t)(9 - 8)));
    v_stack_m168 = (uint32_t)(Arg1);
    if (condition_is_not_equal) goto loc_00362C0A;
    Arg1 = (uint8_t)(((uint8_t)(result)) & (15));
    if (((uint8_t)(Arg1)) == 10) goto loc_00362C0A;
    if (((uint8_t)(Arg1)) == 9) goto loc_00363364;
    if (((uint32_t)((uint32_t)(v_stack_m18C))) != ((uint32_t)(9 - 8))) goto loc_00363354;
loc_00362C0A:
    Arg1 = (uint8_t)(((uint8_t)(result)) & (15));
    v_stack_m190 = (uint8_t)(Arg1);
    if (((uint8_t)(Arg1)) == 10) goto loc_00362C34;
    if (((uint8_t)(Arg1)) == 8) goto loc_0036336E;
loc_00362C21:
    result = MiGetWsleProtection(Arg1, (uint8_t)(result), 10, 9);
    if ((uint32_t)(result) == 0) {
        result = *(uint32_t *)(local_r15 + 0x10);
        result = (result) >> (5);
        result = (uint32_t)((result) & (31));
    }
    v_stack_m194 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x362C48 + (uint32_t)((uint32_t)(result)) * 4 + 0x11070)));
    if (v_stack_m170 != -1) goto loc_00362D12;
    v_stack_m188 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x20)));
    result = MiInitializePageColorBase(v_stack_m180, 3, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m138);
    result = (uint32_t)(((uint32_t)(v_stack_m130)) & (0xFFF3FFFFULL));
    Arg4 = (uint32_t)((v_stack_m186) & (0xFFFFFFC0ULL));
    Arg4 = (uint32_t)((Arg4) << (12));
    Arg4 = (uint32_t)((Arg4) | ((uint32_t)(result)));
    v_stack_m130 = Arg4;
    Arg2 = 0;
    Arg1 = ((uint32_t)(Arg4)) >> (16);
    Arg1 = (uint32_t)((Arg1) & (3));
    Arg2 = (uint32_t)((Arg2) ^ (Arg4));
    local_rbx = (uint32_t)(((uint8_t)(Arg2)) ^ (Arg4));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m180 + 0xB8)))) & (15)) != 0) goto loc_00362CF1;
    result = MiGetCurrentSlabIdentity(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, v_rip - 3550385, Arg4);
    if (((uint8_t)(result)) != 255) goto loc_003634A3;
loc_00362CF1:
    result = MiGetPage(v_stack_m158, (uint32_t)((uint32_t)(local_rbx)), 1, Arg4);
    v_stack_m170 = result;
    if (result == -1) goto loc_00363147;
loc_00362D12:
    if (((uint32_t)((uint32_t)(v_stack_m198))) >= 1) goto loc_003632E1;
loc_00362D23:
    if (((uint32_t)((uint32_t)(v_stack_m194))) == 24) goto loc_003634EA;
    local_rbx = (v_stack_m170 + v_stack_m170 * 2) << (4);
    local_rbx = (local_rbx) + (v_stack_m170);
    result = MiMakeDemandZeroPte((uint32_t)(v_stack_m194), 1, 1, Arg4);
    *(uint64_t *)(local_rbx + 0x10) = result;
    local_rsi = *(uint64_t *)(arg2);
    if (v_stack_m190 != 10) {
        Arg1 = v_stack_m180;
        Arg4 = 0;
        Arg2 = Arg1;
        Arg3 = Arg4 + 1;
        result = MiUpdateWorkingSetPrivateSize(Arg1, Arg2, Arg3, Arg4);
        Arg3 = 0;
        Arg2 = Arg1;
        result = MiSetWsleProtection(Arg1, Arg2, Arg3, Arg4);
        local_rsi = *(uint64_t *)(arg2);
    }
    result = MiGetContainingPageTable(Arg2, Arg2, Arg3, Arg4);
    result = MiSetPfnContainingFrame(local_rbx, result, Arg3, Arg4);
    result = MiGetEffectivePagePriorityThread(*(uint64_t *)(gs_base + (0 + 0x188)), result, Arg3, Arg4);
    v_stack_m188 = (uint32_t)(result);
    if (((*(uint32_t *)(v_rip + 0xC63D59)) & (0x8000001ULL)) != 0) goto loc_00363532;
loc_00362DB5:
    local_r13 = 0;
loc_00362DBC:
    if (condition_is_below) goto loc_003630A1;
    v_stack_m198 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x20)));
    v_stack_m198 = (uint16_t)(local_r13 + 1);
    *(uint32_t *)(local_rbx + 0x20) = (uint32_t)((uint32_t)(v_stack_m198));
    result = (uint32_t)(v_stack_m198);
    if (v_stack_m128 != 0) {
        result = *(uint64_t *)(local_rbx);
        result = (result) | (local_r13 + 1);
        *(uint64_t *)(local_rbx) = result;
    }
    result = MiSetPfnModified(local_rbx, (uint32_t)((uint32_t)(local_r13 + 1)), Arg3, Arg4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x20))) >> (16));
    Arg2 = (uint32_t)(((uint8_t)(result)) >> (6));
    result = MiFinalizePageAttribute(local_rbx, Arg2, local_r13 + 1, Arg4);
    result = (*(uint64_t *)(local_rbx + 0x18)) & (local_rbx);
    result = (result) | (local_r13 + 1);
    *(uint64_t *)(local_rbx + 0x18) = result;
    v_stack_m198 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x20)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x20))) >> (24));
    result = (uint8_t)((v_stack_m188) ^ ((uint8_t)(Arg1)));
    result = (uint8_t)((result) & (7));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg1)));
    v_stack_m195 = (uint8_t)(result);
    *(uint32_t *)(local_rbx + 0x20) = (uint32_t)((uint32_t)(v_stack_m198));
    *(void **)(local_rbx + 0x8) = Arg2;
    v_stack_m198 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x20))) >> (16));
    result = (uint8_t)((result) & (254));
    result = (uint8_t)((result) | (6));
    v_stack_m196 = (uint8_t)(result);
    *(uint32_t *)(local_rbx + 0x20) = (uint32_t)((uint32_t)(v_stack_m198));
    if (v_stack_m18C == 0) goto loc_00363272;
loc_00362E76:
loc_00362E7A:
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r14))))) & (4));
    if (condition_is_not_equal) goto loc_0036353A;
loc_00362E87:
    if ((uint32_t)(local_r14) != 0) goto loc_00363552;
loc_00362E9F:
    if (((v_stack_m194) & (2)) != 0) goto loc_003631C2;
loc_00362EC2:
    if (v_stack_m140 >= ((uint32_t)(v_stack_m198))) goto loc_00362EF4;
loc_00362ED1:
    if (((1) & ((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x170)))) != 0) goto loc_0036358C;
loc_00362EF4:
    result = MiCopyPage(v_stack_m170, v_stack_m120, 264, Arg4);
    result = MiVmAccessLoggingEnabled(v_stack_m180, v_stack_m120, v_stack_m180, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00363295;
loc_00362F1A:
    v_stack_m188 = 64;
    if ((((uint8_t)(64 - 63)) & ((uint8_t)((uint32_t)((uint32_t)(local_r14))))) != 0) goto loc_00362F50;
    if (!sign_flag) goto loc_00363092;
loc_00362F34:
    local_rsi = (local_rsi) | (66);
loc_00362F3D:
    result = (uint32_t)((80) | (36));
    v_stack_m188 = (uint32_t)(result);
    local_rsi = (local_rsi) | (0x820ULL);
loc_00362F50:
    result = (v_stack_m170) << (12);
    local_rbx = (result) ^ (local_rsi);
    local_rbx = (local_rbx) & (v_stack_m180);
    local_rbx = (local_rbx) ^ (result);
    if (((v_stack_m178) & (8)) != 0) goto loc_00363121;
loc_00362F7A:
    if (((uint32_t)((uint32_t)((uint32_t)(local_r14)))) >= 8) goto loc_00362FCB;
    if (((264) & (32)) != 0) goto loc_0036315B;
    if ((((uint8_t)(local_rbx)) & (66)) == 0) goto loc_0036315B;
    result = (local_rbx) & (-2);
    local_r13 = (v_stack_m140) & (0xFFFFFFFFFFFFF000ULL);
    *(uint64_t *)(arg2) = result;
    result = MiFlushSingleTbEntry(local_r13, (uint32_t)(v_stack_m174), (uint32_t)((uint32_t)(64 - 63)), Arg4);
    if (condition_is_below) goto loc_0036320D;
loc_00362FC7:
    *(uint64_t *)(arg2) = local_rbx;
loc_00362FCB:
    if (v_stack_m18C == 1) {
    }
    local_rbx = 0;
loc_00362FE7:
    if (condition_is_below) goto loc_003630C2;
    if (v_stack_m18C == 0) goto loc_003632BD;
loc_00362FFF:
    Arg2 = 0;
    result = MiDecrementShareCountEx(local_r15, Arg2, (uint32_t)((uint32_t)(64 - 63)), Arg4);
    if ((((uint8_t)((uint32_t)((uint32_t)(local_r14)))) & (2)) != 0) goto loc_0036304B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m180 + 0xB8)))) & (15)) != 0) goto loc_00363065;
    result = MiLocateCloneAddress(v_stack_m150, v_stack_m148, (uint32_t)((uint32_t)(64 - 63)), Arg4);
    if (result == 0) goto loc_00363065;
    result = MiDecrementCloneBlockReference(result, v_stack_m148, v_stack_m150, Arg4);
    goto loc_0036305C;
loc_0036304B:
    Arg3 = 0;
    result = MiDecrementCombinedPteEx(v_stack_m180, v_stack_m148, Arg3, Arg4);
loc_0036305C:
    if (((uint32_t)(result)) == 3) goto loc_00363595;
loc_00363065:
    result = 0;
loc_00363067:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m148, Arg3, Arg4);
    local_rsp = (local_rsp) + (400);
    return result;
loc_00363092:
    if (v_stack_p3C == ((uint32_t)(v_stack_m148))) goto loc_00362F3D;
    goto loc_00362F34;
loc_003630A1:
    local_r13 = (uint32_t)((local_r13) + (1));
    if (((*(uint32_t *)(v_rip + 0xC62201)) & ((uint32_t)(local_r13))) == 0) goto loc_00363416;
loc_003630B1:
loc_003630B3:
    if (!sign_flag) goto loc_00362DBC;
    goto loc_003630A1;
loc_003630C2:
    local_rbx = (uint32_t)((v_stack_p20) + (1));
    if (((*(uint32_t *)(v_rip + 0xC621E1)) & ((uint32_t)(local_rbx))) == 0) goto loc_0036343E;
loc_003630D1:
loc_003630D3:
    if (!sign_flag) goto loc_00362FE7;
    goto loc_003630C2;
loc_003630E2:
    v_stack_p48 = v_rip + 11357523;
    if (condition_is_below) goto loc_00362BA5;
    if (sign_flag) goto loc_00362BA5;
    if (*(uint64_t *)(local_r15 + 0x8) == 0) goto loc_00362BA5;
    local_rdi = (uint32_t)((1) | ((uint32_t)(v_stack_m148)));
    goto loc_00362BA5;
loc_00363121:
    result = MI_WRITE_INVALID_PTE_TB_FLUSH_NEEDED(0, local_rbx, 4, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00362F7A;
    local_rdi = (uint32_t)((local_rdi) | (8));
    goto loc_00362F7A;
loc_00363147:
    goto loc_00363067;
loc_00363151:
    goto loc_00363067;
loc_0036315B:
    if (((*(uint64_t *)(v_rip + 0xC63922)) & (0x2000000ULL)) != 0) {
    }
    if (condition_is_below) goto loc_0036338D;
loc_0036317A:
    result = MiPteInShadowRange(0, 1, 4, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00363493;
loc_00363191:
    local_r13 = (local_r13) & (0xFFFFFFFFFFFFF000ULL);
    result = MiFlushSingleTbEntry(local_r13, (uint32_t)(v_stack_p54), (uint32_t)(v_stack_p40), Arg4);
    goto loc_00362FCB;
loc_003631AE:
    if (*(uint64_t *)(local_r15 + 0x8) == 0) goto loc_00362B70;
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)((uint32_t)(v_stack_p54))));
    goto loc_00362B70;
loc_003631C2:
    if (condition_is_below) goto loc_00362EC2;
    if (condition_is_above_or_equal) goto loc_00362EC2;
    if (local_r13 < (*(uint64_t *)(v_rip + 0xC638BF))) goto loc_00362ED1;
    if (((v_stack_p50) & ((uint8_t)(local_r13))) == 0) goto loc_00362EF4;
    goto loc_00362EF4;
loc_0036320D:
    if ((((uint8_t)(local_rbx)) & (32)) != 0) goto loc_00362FC7;
    result = (*(uint64_t *)(v_rip + 0xC638BF)) + (local_r13);
    if (0 < result) goto loc_00362FC7;
    result = MiCheckLinearProtectedPteAccessedBit(0, local_rbx, 128, Arg4);
    goto loc_00362FC7;
loc_0036324F:
    result = (uint32_t)((result) << (16));
    result = (result) | (local_rbx);
    v_stack_p20 = result;
    result = KeBugCheckEx(26, (uint32_t)(0x3300ULL), local_r13, v_stack_m150);
loc_00363272:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (8)) == 0) goto loc_00362E76;
    if (v_stack_p60 != 0) goto loc_00362E76;
    goto loc_00362E7A;
loc_00363295:
    result = MiGetVmAccessLoggingPartition(local_r13, (uint32_t)(0x3300ULL), local_r13, v_stack_m150);
    if (((uint32_t)((uint32_t)(v_stack_p40))) < (*(uint32_t *)(result + 0x4430))) goto loc_00362F1A;
    result = MiLogPageAccess(local_r13, 0, local_r13, v_stack_m150);
    goto loc_00362F1A;
loc_003632BD:
    if (v_stack_p60 != 0) goto loc_00362FFF;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (8)) == 0) goto loc_00362FFF;
    goto loc_00362FFF;
loc_003632E1:
    if (((uint32_t)(result)) < 2) goto loc_0036331C;
    Arg3 = 0;
    result = (*(uint64_t *)(local_r15 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    result = MiReturnCommit(*(uint64_t *)(*(uint64_t *)(v_rip + 0xACCD94) + result * 8), 0, Arg3, v_stack_m150);
    if (v_stack_p3C == 1) {
    }
    result = (*(uint64_t *)(local_r15 + 0x28)) & (*(uint64_t *)(*(uint64_t *)(v_rip + 0xACCD94) + result * 8));
    Arg1 = (result + result * 2) << (4);
    Arg1 = (Arg1) + (result);
    result = MiUnlockPageTableCharges(Arg1, 1, Arg3, v_stack_m150);
    goto loc_00362D23;
loc_00363354:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x20))) >> (24));
    if ((((uint8_t)(Arg1)) & (8)) == 0) goto loc_00362C0A;
loc_00363364:
    result = (uint8_t)((result) & (250));
    result = (uint8_t)((result) | (0));
    goto loc_00362C0A;
loc_0036336E:
    local_r11 = 1;
    if (condition_is_below) { local_r11 = 2; }
    v_stack_p30 = (uint32_t)(local_r11);
    goto loc_00362C21;
loc_0036338D:
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xACCD94) + result * 8))) & (33));
    if (((uint8_t)(result)) != 1) goto loc_0036317A;
    result = (result) + (2);
    if (0 < result) goto loc_0036317A;
    result = MiCheckLinearProtectedPteAccessedBit(0, *(uint64_t *)(*(uint64_t *)(v_rip + 0xACCD94) + result * 8), 128, v_stack_m150);
    goto loc_0036317A;
loc_003633D2:
    v_stack_p48 = v_rip + 11357411;
    local_rdi = (uint32_t)((304) | ((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xACCD94) + result * 8))));
    if (condition_is_below) goto loc_003633F7;
    if (!sign_flag) goto loc_00363465;
loc_003633F7:
    v_stack_p20 = 0x50000ULL;
    result = KeBugCheckEx(26, (uint32_t)(0x3300ULL), local_r13, v_stack_m150);
loc_00363416:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC6369C)))) & (64)) == 0) goto loc_003630B1;
    result = KiCheckVpBackingLongSpinWaitHypercall(26, (uint32_t)(0x3300ULL), local_r13, v_stack_m150);
    if ((uint8_t)(result) == 0) goto loc_003630B1;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r13)), (uint32_t)(0x3300ULL), local_r13, v_stack_m150);
    goto loc_003630B3;
loc_0036343E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC63674)))) & (64)) == 0) goto loc_003630D1;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_r13)), (uint32_t)(0x3300ULL), local_r13, v_stack_m150);
    if ((uint8_t)(result) == 0) goto loc_003630D1;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xACCD94) + result * 8))), (uint32_t)(0x3300ULL), local_r13, v_stack_m150);
    goto loc_003630D3;
loc_00363465:
    if (*(uint64_t *)(local_r15 + 0x8) != 0) goto loc_00362BA5;
    goto loc_003633F7;
loc_00363474:
    v_stack_p20 = 0x40001ULL;
    result = KeBugCheckEx(26, (uint32_t)(0x3300ULL), local_r13, v_stack_m150);
loc_00363493:
    result = MiWritePteShadow(0, *(uint64_t *)(*(uint64_t *)(v_rip + 0xACCD94) + result * 8), local_r13, v_stack_m150);
    goto loc_00363191;
loc_003634A3:
    v_stack_p20 = v_stack_m58;
    result = MiGetSlabPage(v_stack_p70, 16 - 8, (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xACCD94) + result * 8))), 16);
    v_stack_p58 = result;
    if (result != -1) goto loc_00362D12;
    if ((*(uint64_t *)(v_stack_m58)) != 0) goto loc_00363147;
    goto loc_00362CF1;
loc_003634EA:
    v_stack_p34 = (uint32_t)(16 - 8);
    result = MiLockVadTree((uint32_t)((uint32_t)(16 - 8)), 16 - 8, (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xACCD94) + result * 8))), 16);
    result = MiLocateAddress(local_r13, 16 - 8, (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xACCD94) + result * 8))), 16);
    v_stack_p68 = result;
    result = MiUnlockVadTree(1, 17, (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xACCD94) + result * 8))), 16);
loc_00363532:
    local_rdi = (uint32_t)((local_rdi) | (4));
    goto loc_00362DB5;
loc_0036353A:
    result = MiIdentifyPfn(v_stack_p58, v_stack_m118, (uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xACCD94) + result * 8))), 16);
    goto loc_00362E87;
loc_00363552:
    v_stack_m58 = v_stack_m118;
    v_stack_m50 = 32;
    v_stack_p20 = 0x11501B04ULL;
    result = EtwTraceKernelEvent(v_stack_m58, 1, (uint32_t)(0x28000001ULL), 642);
    goto loc_00362E9F;
loc_0036358C:
    local_r14 = (uint32_t)((304) | (16));
    goto loc_00362EF4;
loc_00363595:
    result = MiChargeCommit(v_stack_p70, local_r14, 4, 642);
    goto loc_00363065;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00362A0C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
