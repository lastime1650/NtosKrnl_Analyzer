# MiResolveProtoPteFault

- RVA: `0x00321750`–`0x00322557` (길이 `3,591` bytes)
- VA: `0x0000000140321750`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00075790`
- 디코드: `852`개 명령, `3,591/3,591` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **41**; 고유 호출 대상: **28**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00321939` → [MiLockOwnedProtoPage](MiLockOwnedProtoPage_function_00322560.md) (function, `0x00322560`)
- `0x00321B17` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00321B63` → [MiCompleteProtoPteFault](../34/MiCompleteProtoPteFault_function_00345710.md) (function, `0x00345710`)
- `0x00321BAA` → [MiIsPfnCommitNotCharged](../31/MiIsPfnCommitNotCharged_function_00317370.md) (function, `0x00317370`)
- `0x00321BDF` → [MiChargeCommit](../28/MiChargeCommit_function_00286EB0.md) (function, `0x00286EB0`)
- `0x00321C3F` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00321D22` → [MiResolveTransitionFault](../28/MiResolveTransitionFault_function_00282940.md) (function, `0x00282940`)
- `0x00321D91` → [MiPteHasShadow](MiPteHasShadow_function_0032B998.md) (function, `0x0032B998`)
- `0x00321E66` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00321E7E` → [KeInvalidAccessAllowed](../34/KeInvalidAccessAllowed_function_0034B3F0.md) (function, `0x0034B3F0`)
- `0x00321E8E` → [MiIsPrototypePteVadLookup](MiIsPrototypePteVadLookup_function_00328B70.md) (function, `0x00328B70`)
- `0x00321EC2` → [MiMakeDemandZeroPte](../33/MiMakeDemandZeroPte_function_00337A00.md) (function, `0x00337A00`)
- `0x00321EDA` → [MiPteInShadowRange](../23/MiPteInShadowRange_function_0023FB00.md) (function, `0x0023FB00`)
- `0x00321F0C` → [MiResolveDemandZeroFault](../2B/MiResolveDemandZeroFault_function_002B5A40.md) (function, `0x002B5A40`)
- `0x00321F61` → [MiGetPfnPriority](MiGetPfnPriority_function_003226F0.md) (function, `0x003226F0`)
- `0x00321F83` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00321FA6` → [MiGetPagingFileOffset](../36/MiGetPagingFileOffset_function_0036F530.md) (function, `0x0036F530`)
- `0x00321FC3` → [KeInvalidAccessAllowed](../34/KeInvalidAccessAllowed_function_0034B3F0.md) (function, `0x0034B3F0`)
- `0x00321FE6` → [MiResolveDemandZeroFault](../2B/MiResolveDemandZeroFault_function_002B5A40.md) (function, `0x002B5A40`)
- `0x00322022` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00322089` → [MiAllowGuardFault](../34/MiAllowGuardFault_function_0034B5B0.md) (function, `0x0034B5B0`)
- `0x003220DB` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00322175` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x003221C1` → [MiIsPrototypePteVadLookup](MiIsPrototypePteVadLookup_function_00328B70.md) (function, `0x00328B70`)
- `0x003221E7` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x0032220D` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x00322244` → [MiResolveMappedFileFault](../36/MiResolveMappedFileFault_function_0036B640.md) (function, `0x0036B640`)
- `0x00322265` → [MiLockSpecialPurposeMemoryCachedPage](../40/MiLockSpecialPurposeMemoryCachedPage_function_004049F0.md) (function, `0x004049F0`)
- `0x003222A8` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003222B8` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003222D0` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003222DF` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00322333` → [MiResolvePageFileFault](../36/MiResolvePageFileFault_function_0036D968.md) (function, `0x0036D968`)
- `0x00322346` → [MiChargePartitionResidentAvailable](../28/MiChargePartitionResidentAvailable_function_0028B000.md) (function, `0x0028B000`)
- `0x00322365` → [MiReturnCommit](../24/MiReturnCommit_function_00248410.md) (function, `0x00248410`)
- `0x003223AA` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x003223FE` → [MiLockVadTree](../27/MiLockVadTree_function_0027C0F0.md) (function, `0x0027C0F0`)
- `0x00322406` → [MiLocateAddress](../31/MiLocateAddress_function_003168D0.md) (function, `0x003168D0`)
- `0x00322413` → [MiUnlockVadTree](../29/MiUnlockVadTree_function_00297020.md) (function, `0x00297020`)
- `0x003224BB` → [MiSanitizeShadowPxe](../29/MiSanitizeShadowPxe_function_00294B68.md) (function, `0x00294B68`)
- `0x003224D6` → [MiWritePteShadow](../29/MiWritePteShadow_function_00294EAC.md) (function, `0x00294EAC`)

### Direct callers
- [sub_00320540](Unknown_function_00320540.md) at `0x00320716`

### Static image references
- `0x00321826` → RVA `0x00E2DCE0` (`.data`; read)
- `0x0032196D` → RVA `0x00E2DC80` (`.data`; read)
- `0x00321A0E` → RVA `0x00E30088` (`.data`; read)
- `0x00321BF2` → RVA `0x00E38D00` (`.data`; read)
- `0x00321D73` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00321E4B` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x0032203A` → RVA `0x00011060` (`.rdata`; read)
- `0x0032229A` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00321750  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00321755  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0032175A  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0032175F  53                              push rbx
00321760  56                              push rsi
00321761  57                              push rdi
00321762  41 54                           push r12
00321764  41 55                           push r13
00321766  41 56                           push r14
00321768  41 57                           push r15
0032176A  48 83 EC 70                     sub rsp, 0x70
0032176E  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
00321772  45 33 FF                        xor r15d, r15d
00321775  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0032177A  49 B9 F8 FF FF FF 7F 00 00 00   movabs r9, 0x7ffffffff8
00321784  48 8B 01                        mov rax, qword ptr [rcx]
00321787  4C 8B E8                        mov r13, rax
0032178A  4D 89 38                        mov qword ptr [r8], r15
0032178D  49 C1 ED 09                     shr r13, 9
00321791  4D 23 E9                        and r13, r9
00321794  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00321799  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
003217A3  49 8B C0                        mov rax, r8
003217A6  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
003217AA  4C 03 E8                        add r13, rax
003217AD  48 8B C2                        mov rax, rdx
003217B0  4C 89 6C 24 60                  mov qword ptr [rsp + 0x60], r13
003217B5  83 E0 01                        and eax, 1
003217B8  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
003217BD  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
003217C2  0F 85 74 05 00 00               jne 0x140321d3c
003217C8  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
003217CD  4C 8B 61 68                     mov r12, qword ptr [rcx + 0x68]
003217D1  49 8B FC                        mov rdi, r12
003217D4  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
003217D9  48 C1 EF 09                     shr rdi, 9
003217DD  49 23 F9                        and rdi, r9
003217E0  49 8B C0                        mov rax, r8
003217E3  48 03 F8                        add rdi, rax
003217E6  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
003217F0  49 BA 00 00 00 00 00 DE FF FF   movabs r10, 0xffffde0000000000
003217FA  49 B9 00 00 00 00 00 00 40 00   movabs r9, 0x40000000000000
00321804  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
0032180E  66 90                           nop
00321810  48 8B 1F                        mov rbx, qword ptr [rdi]
00321813  F6 C3 01                        test bl, 1
00321816  74 6B                           je 0x140321883
00321818  48 0F BA E3 09                  bt rbx, 9
0032181D  72 64                           jb 0x140321883
0032181F  48 C1 EB 0C                     shr rbx, 0xc
00321823  48 23 DA                        and rbx, rdx
00321826  48 3B 1D B3 C4 B0 00            cmp rbx, qword ptr [rip + 0xb0c4b3]
0032182D  77 E1                           ja 0x140321810
0032182F  48 8D 0C 5B                     lea rcx, [rbx + rbx*2]
00321833  48 03 C9                        add rcx, rcx
00321836  48 8B C0                        mov rax, rax
00321839  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
0032183D  49 85 C1                        test r9, rax
00321840  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
0032184A  74 C4                           je 0x140321810
0032184C  49 8B C2                        mov rax, r10
0032184F  48 8D 34 C8                     lea rsi, [rax + rcx*8]
00321853  45 8B F7                        mov r14d, r15d
00321856  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
00321860  F0 48 0F BA 6E 18 3F            lock bts qword ptr [rsi + 0x18], 0x3f
00321867  0F 82 03 05 00 00               jb 0x140321d70
0032186D  48 8B 07                        mov rax, qword ptr [rdi]
00321870  A8 01                           test al, 1
00321872  75 25                           jne 0x140321899
00321874  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0032187E  F0 48 21 46 18                  lock and qword ptr [rsi + 0x18], rax
00321883  B8 16 00 00 C0                  mov eax, 0xc0000016
00321888  48 83 C4 70                     add rsp, 0x70
0032188C  41 5F                           pop r15
0032188E  41 5E                           pop r14
00321890  41 5D                           pop r13
00321892  41 5C                           pop r12
00321894  5F                              pop rdi
00321895  5E                              pop rsi
00321896  5B                              pop rbx
00321897  C3                              ret
00321898  CC                              int3
00321899  48 0F BA E0 09                  bt rax, 9
0032189E  72 D4                           jb 0x140321874
003218A0  48 C1 E8 0C                     shr rax, 0xc
003218A4  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
003218AE  48 23 C2                        and rax, rdx
003218B1  48 3B D8                        cmp rbx, rax
003218B4  0F 85 C9 02 00 00               jne 0x140321b83
003218BA  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
003218BE  41 BA FF FF FF FF               mov r10d, 0xffffffff
003218C4  48 0F BA E0 28                  bt rax, 0x28
003218C9  41 BE 01 00 00 00               mov r14d, 1
003218CF  72 46                           jb 0x140321917
003218D1  48 0F BA 66 28 35               bt qword ptr [rsi + 0x28], 0x35
003218D7  72 3E                           jb 0x140321917
003218D9  8B 56 20                        mov edx, dword ptr [rsi + 0x20]
003218DC  48 B9 FF FF FF FF FF FF FF 3F   movabs rcx, 0x3fffffffffffffff
003218E6  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
003218EA  48 23 C1                        and rax, rcx
003218ED  41 8B CF                        mov ecx, r15d
003218F0  66 85 D2                        test dx, dx
003218F3  0F 84 9E 02 00 00               je 0x140321b97
003218F9  66 41 3B D6                     cmp dx, r14w
003218FD  0F 85 1F 06 00 00               jne 0x140321f22
00321903  48 85 C0                        test rax, rax
00321906  0F 84 42 09 00 00               je 0x14032224e
0032190C  41 8B CE                        mov ecx, r14d
0032190F  85 C9                           test ecx, ecx
00321911  0F 85 80 02 00 00               jne 0x140321b97
00321917  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
0032191A  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
00321921  66 FF C0                        inc ax
00321924  66 89 84 24 C8 00 00 00         mov word ptr [rsp + 0xc8], ax
0032192C  8B 84 24 C8 00 00 00            mov eax, dword ptr [rsp + 0xc8]
00321933  89 46 20                        mov dword ptr [rsi + 0x20], eax
00321936  48 8B CE                        mov rcx, rsi
00321939  E8 22 0C 00 00                  call 0x140322560
0032193E  45 33 F6                        xor r14d, r14d
00321941  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
0032194B  49 8B 1C 24                     mov rbx, qword ptr [r12]
0032194F  48 8B C3                        mov rax, rbx
00321952  F6 C3 01                        test bl, 1
00321955  75 51                           jne 0x1403219a8
00321957  25 00 0C 00 00                  and eax, 0xc00
0032195C  48 3D 00 08 00 00               cmp rax, 0x800
00321962  0F 85 33 06 00 00               jne 0x140321f9b
00321968  48 85 DB                        test rbx, rbx
0032196B  74 10                           je 0x14032197d
0032196D  48 8B 05 0C C3 B0 00            mov rax, qword ptr [rip + 0xb0c30c]
00321974  48 85 C0                        test rax, rax
00321977  0F 85 D6 03 00 00               jne 0x140321d53
0032197D  48 8B 0D FC C2 B0 00            mov rcx, qword ptr [rip + 0xb0c2fc]
00321984  48 8B C3                        mov rax, rbx
00321987  48 85 C9                        test rcx, rcx
0032198A  74 12                           je 0x14032199e
0032198C  F6 C3 10                        test bl, 0x10
0032198F  0F 85 B8 05 00 00               jne 0x140321f4d
00321995  48 8B C1                        mov rax, rcx
00321998  48 F7 D0                        not rax
0032199B  48 23 C3                        and rax, rbx
0032199E  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
003219A8  48 C1 E8 0C                     shr rax, 0xc
003219AC  48 23 C1                        and rax, rcx
003219AF  48 3B 05 2A C3 B0 00            cmp rax, qword ptr [rip + 0xb0c32a]
003219B6  77 93                           ja 0x14032194b
003219B8  48 8D 0C 40                     lea rcx, [rax + rax*2]
003219BC  48 B8 28 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000028
003219C6  48 03 C9                        add rcx, rcx
003219C9  48 8B C0                        mov rax, rax
003219CC  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
003219D0  48 0F BA E0 36                  bt rax, 0x36
003219D5  0F 83 66 FF FF FF               jae 0x140321941
003219DB  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
003219E5  48 8B C0                        mov rax, rax
003219E8  4C 8D 3C C8                     lea r15, [rax + rcx*8]
003219EC  41 8B FE                        mov edi, r14d
003219EF  90                              nop
003219F0  F0 49 0F BA 6F 18 3F            lock bts qword ptr [r15 + 0x18], 0x3f
003219F7  0F 82 E3 03 00 00               jb 0x140321de0
003219FD  49 8B 04 24                     mov rax, qword ptr [r12]
00321A01  48 3B C3                        cmp rax, rbx
00321A04  0F 85 7A 07 00 00               jne 0x140322184
00321A0A  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
00321A0E  48 8B 15 73 E6 B0 00            mov rdx, qword ptr [rip + 0xb0e673]
00321A15  48 C1 E8 2B                     shr rax, 0x2b
00321A19  25 FF 03 00 00                  and eax, 0x3ff
00321A1E  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
00321A22  8B 40 04                        mov eax, dword ptr [rax + 4]
00321A25  84 C0                           test al, al
00321A27  0F 88 30 08 00 00               js 0x14032225d
00321A2D  4D 8B 34 24                     mov r14, qword ptr [r12]
00321A31  48 B8 00 D0 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed000
00321A3B  4C 3B E0                        cmp r12, rax
00321A3E  72 2F                           jb 0x140321a6f
00321A40  48 B8 F8 D7 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed7f8
00321A4A  4C 3B E0                        cmp r12, rax
00321A4D  77 20                           ja 0x140321a6f
00321A4F  41 F6 C6 01                     test r14b, 1
00321A53  0F 84 D7 01 00 00               je 0x140321c30
00321A59  41 F6 C6 42                     test r14b, 0x42
00321A5D  0F 95 C1                        setne cl
00321A60  41 F6 C6 20                     test r14b, 0x20
00321A64  0F 95 C0                        setne al
00321A67  84 C8                           test al, cl
00321A69  0F 84 22 03 00 00               je 0x140321d91
00321A6F  41 F6 C6 01                     test r14b, 1
00321A73  0F 84 B7 01 00 00               je 0x140321c30
00321A79  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
00321A7E  4D 85 D2                        test r10, r10
00321A81  0F 85 CF 04 00 00               jne 0x140321f56
00321A87  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
00321A8B  48 85 C0                        test rax, rax
00321A8E  79 54                           jns 0x140321ae4
00321A90  49 8B 7F 10                     mov rdi, qword ptr [r15 + 0x10]
00321A94  48 0F BA E7 0A                  bt rdi, 0xa
00321A99  73 49                           jae 0x140321ae4
00321A9B  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
00321A9F  48 C1 E8 3C                     shr rax, 0x3c
00321AA3  24 07                           and al, 7
00321AA5  3C 03                           cmp al, 3
00321AA7  74 3B                           je 0x140321ae4
00321AA9  48 8B 05 D0 C1 B0 00            mov rax, qword ptr [rip + 0xb0c1d0]
00321AB0  48 85 C0                        test rax, rax
00321AB3  74 0C                           je 0x140321ac1
00321AB5  40 F6 C7 10                     test dil, 0x10
00321AB9  75 06                           jne 0x140321ac1
00321ABB  48 F7 D0                        not rax
00321ABE  48 23 F8                        and rdi, rax
00321AC1  48 C1 FF 10                     sar rdi, 0x10
00321AC5  48 8B 1F                        mov rbx, qword ptr [rdi]
00321AC8  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
00321ACB  A8 20                           test al, 0x20
00321ACD  74 15                           je 0x140321ae4
00321ACF  48 8B 5B 60                     mov rbx, qword ptr [rbx + 0x60]
00321AD3  48 83 E3 F8                     and rbx, 0xfffffffffffffff8
00321AD7  48 8B 5B 28                     mov rbx, qword ptr [rbx + 0x28]
00321ADB  48 85 DB                        test rbx, rbx
00321ADE  0F 85 22 06 00 00               jne 0x140322106
00321AE4  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
00321AE8  48 BA 00 00 00 00 00 00 00 C0   movabs rdx, 0xc000000000000000
00321AF2  48 8D 48 01                     lea rcx, [rax + 1]
00321AF6  48 33 C1                        xor rax, rcx
00321AF9  48 23 C2                        and rax, rdx
00321AFC  48 33 C1                        xor rax, rcx
00321AFF  49 89 47 18                     mov qword ptr [r15 + 0x18], rax
00321B03  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00321B0D  F0 49 21 47 18                  lock and qword ptr [r15 + 0x18], rax
00321B12  B2 11                           mov dl, 0x11
00321B14  48 8B CE                        mov rcx, rsi
00321B17  E8 74 45 F2 FF                  call 0x140246090
00321B1C  65 FF 04 25 98 2E 00 00         inc dword ptr gs:[0x2e98]
00321B24  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00321B2E  48 8B C0                        mov rax, rax
00321B31  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00321B36  4C 2B F8                        sub r15, rax
00321B39  4C 8B 84 24 B8 00 00 00         mov r8, qword ptr [rsp + 0xb8]
00321B41  48 BA AB AA AA AA AA AA AA AA   movabs rdx, 0xaaaaaaaaaaaaaaab
00321B4B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00321B50  45 33 C9                        xor r9d, r9d
00321B53  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00321B5B  49 C1 FF 04                     sar r15, 4
00321B5F  49 0F AF D7                     imul rdx, r15
00321B63  E8 A8 3B 02 00                  call 0x140345710
00321B68  85 C0                           test eax, eax
00321B6A  B9 10 01 00 00                  mov ecx, 0x110
00321B6F  0F 49 C1                        cmovns eax, ecx
00321B72  48 83 C4 70                     add rsp, 0x70
00321B76  41 5F                           pop r15
00321B78  41 5E                           pop r14
00321B7A  41 5D                           pop r13
00321B7C  41 5C                           pop r12
00321B7E  5F                              pop rdi
00321B7F  5E                              pop rsi
00321B80  5B                              pop rbx
00321B81  C3                              ret
00321B82  CC                              int3
00321B83  49 B8 FF FF FF FF FF FF FF 7F   movabs r8, 0x7fffffffffffffff
00321B8D  F0 4C 21 46 18                  lock and qword ptr [rsi + 0x18], r8
00321B92  E9 59 FC FF FF                  jmp 0x1403217f0
00321B97  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
00321B9B  40 32 FF                        xor dil, dil
00321B9E  48 85 C0                        test rax, rax
00321BA1  0F 88 4C 05 00 00               js 0x1403220f3
00321BA7  48 8B CE                        mov rcx, rsi
00321BAA  E8 C1 57 FF FF                  call 0x140317370
00321BAF  85 C0                           test eax, eax
00321BB1  0F 84 0E 08 00 00               je 0x1403223c5
00321BB7  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
00321BBB  41 B8 04 00 00 00               mov r8d, 4
00321BC1  48 8B 05 C0 E4 B0 00            mov rax, qword ptr [rip + 0xb0e4c0]
00321BC8  49 8B D6                        mov rdx, r14
00321BCB  48 C1 E9 2B                     shr rcx, 0x2b
00321BCF  40 B7 01                        mov dil, 1
00321BD2  81 E1 FF 03 00 00               and ecx, 0x3ff
00321BD8  48 8B 1C C8                     mov rbx, qword ptr [rax + rcx*8]
00321BDC  48 8B CB                        mov rcx, rbx
00321BDF  E8 CC 52 F6 FF                  call 0x140286eb0
00321BE4  85 C0                           test eax, eax
00321BE6  0F 84 4A FD FF FF               je 0x140321936
00321BEC  41 BA FF FF FF FF               mov r10d, 0xffffffff
00321BF2  48 8D 05 07 71 B1 00            lea rax, [rip + 0xb17107]
00321BF9  48 3B D8                        cmp rbx, rax
00321BFC  0F 85 3B 07 00 00               jne 0x14032233d
00321C02  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
00321C0B  8B 82 9C 8B 00 00               mov eax, dword ptr [rdx + 0x8b9c]
00321C11  8D 48 FF                        lea ecx, [rax - 1]
00321C14  83 F9 FD                        cmp ecx, -3
00321C17  0F 87 20 07 00 00               ja 0x14032233d
00321C1D  8D 48 FF                        lea ecx, [rax - 1]
00321C20  F0 0F B1 8A 9C 8B 00 00         lock cmpxchg dword ptr [rdx + 0x8b9c], ecx
00321C28  0F 84 E9 FC FF FF               je 0x140321917
00321C2E  EB E1                           jmp 0x140321c11
00321C30  4D 85 F6                        test r14, r14
00321C33  0F 84 6C 07 00 00               je 0x1403223a5
00321C39  49 8B CD                        mov rcx, r13
00321C3C  45 33 E4                        xor r12d, r12d
00321C3F  E8 5C 0C F6 FF                  call 0x1402828a0
00321C44  4C 8B E8                        mov r13, rax
00321C47  48 0F BA E0 0A                  bt rax, 0xa
00321C4C  0F 83 9E 03 00 00               jae 0x140321ff0
00321C52  48 8B 0D 27 C0 B0 00            mov rcx, qword ptr [rip + 0xb0c027]
00321C59  48 85 C9                        test rcx, rcx
00321C5C  74 13                           je 0x140321c71
00321C5E  41 F6 C5 10                     test r13b, 0x10
00321C62  0F 85 DC 02 00 00               jne 0x140321f44
00321C68  48 8B C1                        mov rax, rcx
00321C6B  48 F7 D0                        not rax
00321C6E  49 23 C5                        and rax, r13
00321C71  48 C1 E8 20                     shr rax, 0x20
00321C75  B9 FF FF FF FF                  mov ecx, 0xffffffff
00321C7A  48 3B C1                        cmp rax, rcx
00321C7D  0F 85 6D 03 00 00               jne 0x140321ff0
00321C83  4D 8B E5                        mov r12, r13
00321C86  49 C1 EC 05                     shr r12, 5
00321C8A  41 83 E4 1F                     and r12d, 0x1f
00321C8E  41 8B C4                        mov eax, r12d
00321C91  83 E0 F8                        and eax, 0xfffffff8
00321C94  83 F8 10                        cmp eax, 0x10
00321C97  0F 84 59 05 00 00               je 0x1403221f6
00321C9D  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
00321CA2  48 8B 94 24 B8 00 00 00         mov rdx, qword ptr [rsp + 0xb8]
00321CAA  48 8B 0D CF BF B0 00            mov rcx, qword ptr [rip + 0xb0bfcf]
00321CB1  49 8B C6                        mov rax, r14
00321CB4  48 85 C9                        test rcx, rcx
00321CB7  74 0F                           je 0x140321cc8
00321CB9  41 F6 C6 10                     test r14b, 0x10
00321CBD  75 09                           jne 0x140321cc8
00321CBF  48 8B C1                        mov rax, rcx
00321CC2  48 F7 D0                        not rax
00321CC5  49 23 C6                        and rax, r14
00321CC8  48 BB 00 00 00 00 00 80 FF FF   movabs rbx, 0xffff800000000000
00321CD2  48 0F BA E0 0A                  bt rax, 0xa
00321CD7  72 0B                           jb 0x140321ce4
00321CD9  48 0F BA E0 0B                  bt rax, 0xb
00321CDE  0F 83 1B 01 00 00               jae 0x140321dff
00321CE4  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
00321CE9  49 0F BA E6 0A                  bt r14, 0xa
00321CEE  0F 82 34 05 00 00               jb 0x140322228
00321CF4  49 0F BA E6 0B                  bt r14, 0xb
00321CF9  0F 83 A4 02 00 00               jae 0x140321fa3
00321CFF  4C 8B 8C 24 C0 00 00 00         mov r9, qword ptr [rsp + 0xc0]
00321D07  4C 8B C6                        mov r8, rsi
00321D0A  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00321D12  48 8B D7                        mov rdx, rdi
00321D15  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00321D1A  4C 8B 8C 24 B8 00 00 00         mov r9, qword ptr [rsp + 0xb8]
00321D22  E8 19 0C F6 FF                  call 0x140282940
00321D27  8B D8                           mov ebx, eax
00321D29  8B C3                           mov eax, ebx
00321D2B  48 83 C4 70                     add rsp, 0x70
00321D2F  41 5F                           pop r15
00321D31  41 5E                           pop r14
00321D33  41 5D                           pop r13
00321D35  41 5C                           pop r12
00321D37  5F                              pop rdi
00321D38  5E                              pop rsi
00321D39  5B                              pop rbx
00321D3A  C3                              ret
00321D3B  CC                              int3
00321D3C  48 83 E2 FE                     and rdx, 0xfffffffffffffffe
00321D40  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
00321D45  80 3A 01                        cmp byte ptr [rdx], 1
00321D48  0F 84 7F FA FF FF               je 0x1403217cd
00321D4E  E9 75 FA FF FF                  jmp 0x1403217c8
00321D53  48 85 D8                        test rax, rbx
00321D56  0F 84 EF FB FF FF               je 0x14032194b
00321D5C  E9 1C FC FF FF                  jmp 0x14032197d
00321D61  0F 1F 40 00                     nop dword ptr [rax]
00321D65  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
00321D70  41 FF C6                        inc r14d
00321D73  44 85 35 32 35 CA 00            test dword ptr [rip + 0xca3532], r14d
00321D7A  0F 84 1A 05 00 00               je 0x14032229a
00321D80  F3 90                           pause
00321D82  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
00321D86  48 85 C0                        test rax, rax
00321D89  0F 89 D1 FA FF FF               jns 0x140321860
00321D8F  EB DF                           jmp 0x140321d70
00321D91  E8 02 9C 00 00                  call 0x14032b998
00321D96  48 85 C0                        test rax, rax
00321D99  0F 84 D0 FC FF FF               je 0x140321a6f
00321D9F  48 8B 88 08 05 00 00            mov rcx, qword ptr [rax + 0x508]
00321DA6  48 85 C9                        test rcx, rcx
00321DA9  0F 84 C0 FC FF FF               je 0x140321a6f
00321DAF  49 8B C4                        mov rax, r12
00321DB2  48 C1 E8 03                     shr rax, 3
00321DB6  25 FF 01 00 00                  and eax, 0x1ff
00321DBB  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
00321DBF  A8 20                           test al, 0x20
00321DC1  74 04                           je 0x140321dc7
00321DC3  49 83 CE 20                     or r14, 0x20
00321DC7  49 8B CE                        mov rcx, r14
00321DCA  49 83 CE 42                     or r14, 0x42
00321DCE  A8 42                           test al, 0x42
00321DD0  4C 0F 44 F1                     cmove r14, rcx
00321DD4  E9 96 FC FF FF                  jmp 0x140321a6f
00321DD9  0F 1F 80 00 00 00 00            nop dword ptr [rax]
00321DE0  FF C7                           inc edi
00321DE2  85 3D C4 34 CA 00               test dword ptr [rip + 0xca34c4], edi
00321DE8  0F 84 D4 04 00 00               je 0x1403222c2
00321DEE  F3 90                           pause
00321DF0  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
00321DF4  48 85 C0                        test rax, rax
00321DF7  0F 89 F3 FB FF FF               jns 0x1403219f0
00321DFD  EB E1                           jmp 0x140321de0
00321DFF  A8 04                           test al, 4
00321E01  0F 85 DD FE FF FF               jne 0x140321ce4
00321E07  41 8B C4                        mov eax, r12d
00321E0A  83 E0 05                        and eax, 5
00321E0D  3C 05                           cmp al, 5
00321E0F  0F 85 CF FE FF FF               jne 0x140321ce4
00321E15  48 85 D2                        test rdx, rdx
00321E18  0F 84 71 05 00 00               je 0x14032238f
00321E1E  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00321E23  8B 80 B8 00 00 00               mov eax, dword ptr [rax + 0xb8]
00321E29  A8 0F                           test al, 0xf
00321E2B  75 1E                           jne 0x140321e4b
00321E2D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00321E36  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00321E3D  48 83 B9 80 02 00 00 00         cmp qword ptr [rcx + 0x280], 0
00321E45  0F 85 99 FE FF FF               jne 0x140321ce4
00321E4B  48 F7 05 32 4C CA 00 00 80 00 00  test qword ptr [rip + 0xca4c32], 0x8000
00321E56  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
00321E5B  0F 85 0E 05 00 00               jne 0x14032236f
00321E61  B2 11                           mov dl, 0x11
00321E63  48 8B CE                        mov rcx, rsi
00321E66  E8 25 42 F2 FF                  call 0x140246090
00321E6B  48 83 7C 24 50 00               cmp qword ptr [rsp + 0x50], 0
00321E71  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00321E76  0F 85 19 06 00 00               jne 0x140322495
00321E7C  33 D2                           xor edx, edx
00321E7E  E8 6D 95 02 00                  call 0x14034b3f0
00321E83  84 C0                           test al, al
00321E85  0F 85 57 05 00 00               jne 0x1403223e2
00321E8B  49 8B CD                        mov rcx, r13
00321E8E  E8 DD 6C 00 00                  call 0x140328b70
00321E93  49 C1 ED 05                     shr r13, 5
00321E97  49 C1 EE 05                     shr r14, 5
00321E9B  85 C0                           test eax, eax
00321E9D  4D 0F 44 EE                     cmove r13, r14
00321EA1  41 8B CD                        mov ecx, r13d
00321EA4  41 83 E5 18                     and r13d, 0x18
00321EA8  83 E1 02                        and ecx, 2
00321EAB  83 C9 04                        or ecx, 4
00321EAE  41 83 FD 08                     cmp r13d, 8
00321EB2  0F 84 CF 04 00 00               je 0x140322387
00321EB8  41 83 FD 18                     cmp r13d, 0x18
00321EBC  0F 84 2B 05 00 00               je 0x1403223ed
00321EC2  E8 39 5B 01 00                  call 0x140337a00
00321EC7  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
00321ECC  48 8B D8                        mov rbx, rax
00321ECF  48 8B CF                        mov rcx, rdi
00321ED2  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
00321EDA  E8 21 DC F1 FF                  call 0x14023fb00
00321EDF  85 C0                           test eax, eax
00321EE1  0F 85 CC 05 00 00               jne 0x1403224b3
00321EE7  45 33 F6                        xor r14d, r14d
00321EEA  48 89 1F                        mov qword ptr [rdi], rbx
00321EED  45 85 F6                        test r14d, r14d
00321EF0  0F 85 DA 05 00 00               jne 0x1403224d0
00321EF6  4C 8B 8C 24 B8 00 00 00         mov r9, qword ptr [rsp + 0xb8]
00321EFE  45 33 C0                        xor r8d, r8d
00321F01  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00321F09  48 8B D7                        mov rdx, rdi
00321F0C  E8 2F 3B F9 FF                  call 0x1402b5a40
00321F11  48 83 C4 70                     add rsp, 0x70
00321F15  41 5F                           pop r15
00321F17  41 5E                           pop r14
00321F19  41 5D                           pop r13
00321F1B  41 5C                           pop r12
00321F1D  5F                              pop rdi
00321F1E  5E                              pop rsi
00321F1F  5B                              pop rbx
00321F20  C3                              ret
00321F21  CC                              int3
00321F22  66 83 FA 02                     cmp dx, 2
00321F26  0F 85 EB F9 FF FF               jne 0x140321917
00321F2C  48 85 C0                        test rax, rax
00321F2F  0F 84 E2 F9 FF FF               je 0x140321917
00321F35  F6 46 22 08                     test byte ptr [rsi + 0x22], 8
00321F39  0F 84 D8 F9 FF FF               je 0x140321917
00321F3F  E9 53 FC FF FF                  jmp 0x140321b97
00321F44  48 83 E0 EF                     and rax, 0xffffffffffffffef
00321F48  E9 24 FD FF FF                  jmp 0x140321c71
00321F4D  48 83 E0 EF                     and rax, 0xffffffffffffffef
00321F51  E9 48 FA FF FF                  jmp 0x14032199e
00321F56  45 8B 52 50                     mov r10d, dword ptr [r10 + 0x50]
00321F5A  49 8B CF                        mov rcx, r15
00321F5D  41 83 E2 07                     and r10d, 7
00321F61  E8 8A 07 00 00                  call 0x1403226f0
00321F66  44 3B D0                        cmp r10d, eax
00321F69  0F 87 7A 03 00 00               ja 0x1403222e9
00321F6F  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00321F79  F0 49 21 47 18                  lock and qword ptr [r15 + 0x18], rax
00321F7E  B2 11                           mov dl, 0x11
00321F80  48 8B CE                        mov rcx, rsi
00321F83  E8 08 41 F2 FF                  call 0x140246090
00321F88  33 C0                           xor eax, eax
00321F8A  48 83 C4 70                     add rsp, 0x70
00321F8E  41 5F                           pop r15
00321F90  41 5E                           pop r14
00321F92  41 5D                           pop r13
00321F94  41 5C                           pop r12
00321F96  5F                              pop rdi
00321F97  5E                              pop rsi
00321F98  5B                              pop rbx
00321F99  C3                              ret
00321F9A  CC                              int3
00321F9B  45 33 FF                        xor r15d, r15d
00321F9E  E9 8A FA FF FF                  jmp 0x140321a2d
00321FA3  49 8B CE                        mov rcx, r14
00321FA6  E8 85 D5 04 00                  call 0x14036f530
00321FAB  85 C0                           test eax, eax
00321FAD  0F 85 60 03 00 00               jne 0x140322313
00321FB3  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00321FB8  F6 C1 01                        test cl, 1
00321FBB  0F 85 D7 01 00 00               jne 0x140322198
00321FC1  33 D2                           xor edx, edx
00321FC3  E8 28 94 02 00                  call 0x14034b3f0
00321FC8  84 C0                           test al, al
00321FCA  0F 85 E5 01 00 00               jne 0x1403221b5
00321FD0  4C 8B 8C 24 B8 00 00 00         mov r9, qword ptr [rsp + 0xb8]
00321FD8  4C 8B C6                        mov r8, rsi
00321FDB  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00321FE3  48 8B D7                        mov rdx, rdi
00321FE6  E8 55 3A F9 FF                  call 0x1402b5a40
00321FEB  E9 37 FD FF FF                  jmp 0x140321d27
00321FF0  41 F6 C5 08                     test r13b, 8
00321FF4  0F 85 A3 FC FF FF               jne 0x140321c9d
00321FFA  49 8B C6                        mov rax, r14
00321FFD  48 C1 E8 05                     shr rax, 5
00322001  83 E0 1F                        and eax, 0x1f
00322004  44 8B E0                        mov r12d, eax
00322007  C1 E8 03                        shr eax, 3
0032200A  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
00322011  83 F8 02                        cmp eax, 2
00322014  0F 84 5A 04 00 00               je 0x140322474
0032201A  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
0032201F  48 8B CF                        mov rcx, rdi
00322022  E8 79 08 F6 FF                  call 0x1402828a0
00322027  48 8B D8                        mov rbx, rax
0032202A  A8 01                           test al, 1
0032202C  0F 85 40 02 00 00               jne 0x140322272
00322032  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
0032203A  48 8D 15 1F F0 CE FF            lea rdx, [rip - 0x310fe1]
00322041  0F B6 C1                        movzx eax, cl
00322044  48 85 C9                        test rcx, rcx
00322047  B9 01 00 00 00                  mov ecx, 1
0032204C  49 8B FC                        mov rdi, r12
0032204F  0F 44 C8                        cmove ecx, eax
00322052  49 8B C4                        mov rax, r12
00322055  83 E0 07                        and eax, 7
00322058  0F BE C9                        movsx ecx, cl
0032205B  0F BE 04 10                     movsx eax, byte ptr [rax + rdx]
0032205F  2B C1                           sub eax, ecx
00322061  83 F8 0A                        cmp eax, 0xa
00322064  0F 8C 21 04 00 00               jl 0x14032248b
0032206A  83 BC 24 C8 00 00 00 02         cmp dword ptr [rsp + 0xc8], 2
00322072  0F 85 25 FC FF FF               jne 0x140321c9d
00322078  48 83 7C 24 50 00               cmp qword ptr [rsp + 0x50], 0
0032207E  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00322083  0F 85 57 04 00 00               jne 0x1403224e0
00322089  E8 22 95 02 00                  call 0x14034b5b0
0032208E  85 C0                           test eax, eax
00322090  0F 84 B7 04 00 00               je 0x14032254d
00322096  48 8B C3                        mov rax, rbx
00322099  83 E7 0F                        and edi, 0xf
0032209C  48 81 E3 1F FC FF FF            and rbx, 0xfffffffffffffc1f
003220A3  48 C1 E7 05                     shl rdi, 5
003220A7  48 0B FB                        or rdi, rbx
003220AA  25 00 0C 00 00                  and eax, 0xc00
003220AF  48 3D 00 08 00 00               cmp rax, 0x800
003220B5  BB 01 00 00 80                  mov ebx, 0x80000001
003220BA  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
003220BF  48 89 38                        mov qword ptr [rax], rdi
003220C2  4D 85 FF                        test r15, r15
003220C5  74 0F                           je 0x1403220d6
003220C7  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003220D1  F0 49 21 47 18                  lock and qword ptr [r15 + 0x18], rax
003220D6  B2 11                           mov dl, 0x11
003220D8  48 8B CE                        mov rcx, rsi
003220DB  E8 B0 3F F2 FF                  call 0x140246090
003220E0  8B C3                           mov eax, ebx
003220E2  48 83 C4 70                     add rsp, 0x70
003220E6  41 5F                           pop r15
003220E8  41 5E                           pop r14
003220EA  41 5D                           pop r13
003220EC  41 5C                           pop r12
003220EE  5F                              pop rdi
003220EF  5E                              pop rsi
003220F0  5B                              pop rbx
003220F1  C3                              ret
003220F2  CC                              int3
003220F3  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
003220F6  48 0F BA E0 0A                  bt rax, 0xa
003220FB  0F 82 B6 FA FF FF               jb 0x140321bb7
00322101  E9 A1 FA FF FF                  jmp 0x140321ba7
00322106  48 8B C3                        mov rax, rbx
00322109  48 B9 F8 FF FF FF FF FF FF 7F   movabs rcx, 0x7ffffffffffffff8
00322113  48 83 E0 F8                     and rax, 0xfffffffffffffff8
00322117  48 3B C1                        cmp rax, rcx
0032211A  0F 86 C4 F9 FF FF               jbe 0x140321ae4
00322120  0F B6 C3                        movzx eax, bl
00322123  24 03                           and al, 3
00322125  3C 02                           cmp al, 2
00322127  0F 84 B7 F9 FF FF               je 0x140321ae4
0032212D  4C 8B 74 24 30                  mov r14, qword ptr [rsp + 0x30]
00322132  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
0032213C  4C 3B F0                        cmp r14, rax
0032213F  0F 82 B0 02 00 00               jb 0x1403223f5
00322145  48 F7 05 38 49 CA 00 00 80 00 00  test qword ptr [rip + 0xca4938], 0x8000
00322150  0F 84 8E F9 FF FF               je 0x140321ae4
00322156  41 F6 47 10 40                  test byte ptr [r15 + 0x10], 0x40
0032215B  0F 84 83 F9 FF FF               je 0x140321ae4
00322161  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0032216B  F0 49 21 47 18                  lock and qword ptr [r15 + 0x18], rax
00322170  B2 11                           mov dl, 0x11
00322172  48 8B CE                        mov rcx, rsi
00322175  E8 16 3F F2 FF                  call 0x140246090
0032217A  B8 28 04 00 C0                  mov eax, 0xc0000428
0032217F  E9 04 F7 FF FF                  jmp 0x140321888
00322184  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0032218E  F0 49 21 47 18                  lock and qword ptr [r15 + 0x18], rax
00322193  E9 A9 F7 FF FF                  jmp 0x140321941
00322198  48 8B C1                        mov rax, rcx
0032219B  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0032219F  80 38 01                        cmp byte ptr [rax], 1
003221A2  0F 85 4D 03 00 00               jne 0x1403224f5
003221A8  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
003221AC  80 39 06                        cmp byte ptr [rcx], 6
003221AF  0F 84 1B FE FF FF               je 0x140321fd0
003221B5  4C 3B FB                        cmp r15, rbx
003221B8  0F 82 12 FE FF FF               jb 0x140321fd0
003221BE  49 8B CD                        mov rcx, r13
003221C1  E8 AA 69 00 00                  call 0x140328b70
003221C6  49 C1 EE 05                     shr r14, 5
003221CA  49 C1 ED 05                     shr r13, 5
003221CE  85 C0                           test eax, eax
003221D0  4D 0F 45 F5                     cmovne r14, r13
003221D4  41 80 E6 18                     and r14b, 0x18
003221D8  41 80 FE 10                     cmp r14b, 0x10
003221DC  0F 85 EE FD FF FF               jne 0x140321fd0
003221E2  B2 11                           mov dl, 0x11
003221E4  48 8B CE                        mov rcx, rsi
003221E7  E8 A4 3E F2 FF                  call 0x140246090
003221EC  BB 05 00 00 C0                  mov ebx, 0xc0000005
003221F1  E9 33 FB FF FF                  jmp 0x140321d29
003221F6  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
003221FE  F6 40 45 10                     test byte ptr [rax + 0x45], 0x10
00322202  0F 84 95 FA FF FF               je 0x140321c9d
00322208  B2 11                           mov dl, 0x11
0032220A  48 8B CE                        mov rcx, rsi
0032220D  E8 7E 3E F2 FF                  call 0x140246090
00322212  B8 34 04 00 C0                  mov eax, 0xc0000434
00322217  48 83 C4 70                     add rsp, 0x70
0032221B  41 5F                           pop r15
0032221D  41 5E                           pop r14
0032221F  41 5D                           pop r13
00322221  41 5C                           pop r12
00322223  5F                              pop rdi
00322224  5E                              pop rsi
00322225  5B                              pop rbx
00322226  C3                              ret
00322227  CC                              int3
00322228  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00322230  F6 41 45 10                     test byte ptr [rcx + 0x45], 0x10
00322234  75 D2                           jne 0x140322208
00322236  4C 8B 8C 24 C0 00 00 00         mov r9, qword ptr [rsp + 0xc0]
0032223E  4C 8B C6                        mov r8, rsi
00322241  48 8B D7                        mov rdx, rdi
00322244  E8 F7 93 04 00                  call 0x14036b640
00322249  E9 D9 FA FF FF                  jmp 0x140321d27
0032224E  F6 46 22 08                     test byte ptr [rsi + 0x22], 8
00322252  0F 84 B7 F6 FF FF               je 0x14032190f
00322258  E9 AF F6 FF FF                  jmp 0x14032190c
0032225D  BA 02 00 00 00                  mov edx, 2
00322262  49 8B CF                        mov rcx, r15
00322265  E8 86 27 0E 00                  call 0x1404049f0
0032226A  4C 8B F8                        mov r15, rax
0032226D  E9 BB F7 FF FF                  jmp 0x140321a2d
00322272  48 8B 94 24 B8 00 00 00         mov rdx, qword ptr [rsp + 0xb8]
0032227A  48 85 D2                        test rdx, rdx
0032227D  0F 84 27 FA FF FF               je 0x140321caa
00322283  48 F7 C3 00 0A 00 00            test rbx, 0xa00
0032228A  0F 85 1A FA FF FF               jne 0x140321caa
00322290  BB 05 00 00 C0                  mov ebx, 0xc0000005
00322295  E9 28 FE FF FF                  jmp 0x1403220c2
0032229A  8B 05 18 48 CA 00               mov eax, dword ptr [rip + 0xca4818]
003222A0  A8 40                           test al, 0x40
003222A2  0F 84 D8 FA FF FF               je 0x140321d80
003222A8  E8 E3 D1 FE FF                  call 0x14030f490
003222AD  84 C0                           test al, al
003222AF  0F 84 CB FA FF FF               je 0x140321d80
003222B5  41 8B CE                        mov ecx, r14d
003222B8  E8 A3 D1 FE FF                  call 0x14030f460
003222BD  E9 C0 FA FF FF                  jmp 0x140321d82
003222C2  8B 05 F0 47 CA 00               mov eax, dword ptr [rip + 0xca47f0]
003222C8  A8 40                           test al, 0x40
003222CA  0F 84 1E FB FF FF               je 0x140321dee
003222D0  E8 BB D1 FE FF                  call 0x14030f490
003222D5  84 C0                           test al, al
003222D7  0F 84 11 FB FF FF               je 0x140321dee
003222DD  8B CF                           mov ecx, edi
003222DF  E8 7C D1 FE FF                  call 0x14030f460
003222E4  E9 07 FB FF FF                  jmp 0x140321df0
003222E9  41 8B 47 20                     mov eax, dword ptr [r15 + 0x20]
003222ED  89 84 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], eax
003222F4  C1 E8 18                        shr eax, 0x18
003222F7  24 F8                           and al, 0xf8
003222F9  41 0A C2                        or al, r10b
003222FC  88 84 24 B3 00 00 00            mov byte ptr [rsp + 0xb3], al
00322303  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
0032230A  41 89 47 20                     mov dword ptr [r15 + 0x20], eax
0032230E  E9 5C FC FF FF                  jmp 0x140321f6f
00322313  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
0032231B  F6 41 45 10                     test byte ptr [rcx + 0x45], 0x10
0032231F  0F 85 E3 FE FF FF               jne 0x140322208
00322325  4C 8B 8C 24 C0 00 00 00         mov r9, qword ptr [rsp + 0xc0]
0032232D  4C 8B C6                        mov r8, rsi
00322330  48 8B D7                        mov rdx, rdi
00322333  E8 30 B6 04 00                  call 0x14036d968
00322338  E9 EA F9 FF FF                  jmp 0x140321d27
0032233D  4D 8B C2                        mov r8, r10
00322340  49 8B D6                        mov rdx, r14
00322343  48 8B CB                        mov rcx, rbx
00322346  E8 B5 8C F6 FF                  call 0x14028b000
0032234B  85 C0                           test eax, eax
0032234D  0F 85 C4 F5 FF FF               jne 0x140321917
00322353  40 84 FF                        test dil, dil
00322356  0F 84 DA F5 FF FF               je 0x140321936
0032235C  45 33 C0                        xor r8d, r8d
0032235F  49 8B D6                        mov rdx, r14
00322362  48 8B CB                        mov rcx, rbx
00322365  E8 A6 60 F2 FF                  call 0x140248410
0032236A  E9 C7 F5 FF FF                  jmp 0x140321936
0032236F  4C 3B FB                        cmp r15, rbx
00322372  0F 82 E9 FA FF FF               jb 0x140321e61
00322378  41 F6 C4 02                     test r12b, 2
0032237C  0F 84 DF FA FF FF               je 0x140321e61
00322382  E9 62 F9 FF FF                  jmp 0x140321ce9
00322387  83 C9 08                        or ecx, 8
0032238A  E9 33 FB FF FF                  jmp 0x140321ec2
0032238F  41 0F B6 C6                     movzx eax, r14b
00322393  C0 E8 05                        shr al, 5
00322396  24 05                           and al, 5
00322398  3C 04                           cmp al, 4
0032239A  0F 85 7E FA FF FF               jne 0x140321e1e
003223A0  E9 3F F9 FF FF                  jmp 0x140321ce4
003223A5  B2 11                           mov dl, 0x11
003223A7  48 8B CE                        mov rcx, rsi
003223AA  E8 E1 3C F2 FF                  call 0x140246090
003223AF  B8 05 00 00 C0                  mov eax, 0xc0000005
003223B4  48 83 C4 70                     add rsp, 0x70
003223B8  41 5F                           pop r15
003223BA  41 5E                           pop r14
003223BC  41 5D                           pop r13
003223BE  41 5C                           pop r12
003223C0  5F                              pop rdi
003223C1  5E                              pop rsi
003223C2  5B                              pop rbx
003223C3  C3                              ret
003223C4  CC                              int3
003223C5  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
003223C9  48 8B 0D B8 DC B0 00            mov rcx, qword ptr [rip + 0xb0dcb8]
003223D0  48 C1 E8 2B                     shr rax, 0x2b
003223D4  25 FF 03 00 00                  and eax, 0x3ff
003223D9  48 8B 1C C1                     mov rbx, qword ptr [rcx + rax*8]
003223DD  E9 10 F8 FF FF                  jmp 0x140321bf2
003223E2  4C 3B FB                        cmp r15, rbx
003223E5  0F 82 A0 FA FF FF               jb 0x140321e8b
003223EB  EB C2                           jmp 0x1403223af
003223ED  83 C9 18                        or ecx, 0x18
003223F0  E9 CD FA FF FF                  jmp 0x140321ec2
003223F5  41 BC 01 00 00 00               mov r12d, 1
003223FB  41 8B CC                        mov ecx, r12d
003223FE  E8 ED 9C F5 FF                  call 0x14027c0f0
00322403  49 8B CE                        mov rcx, r14
00322406  E8 C5 44 FF FF                  call 0x1403168d0
0032240B  B2 11                           mov dl, 0x11
0032240D  41 8B CC                        mov ecx, r12d
00322410  4C 8B F0                        mov r14, rax
00322413  E8 08 4C F7 FF                  call 0x140297020
00322418  4D 85 F6                        test r14, r14
0032241B  0F 84 40 FD FF FF               je 0x140322161
00322421  41 8B 56 30                     mov edx, dword ptr [r14 + 0x30]
00322425  8B CA                           mov ecx, edx
00322427  80 E1 70                        and cl, 0x70
0032242A  80 F9 20                        cmp cl, 0x20
0032242D  0F 85 2E FD FF FF               jne 0x140322161
00322433  81 E2 80 0F 00 00               and edx, 0xf80
00322439  81 FA 80 00 00 00               cmp edx, 0x80
0032243F  0F 84 9F F6 FF FF               je 0x140321ae4
00322445  41 8B 46 40                     mov eax, dword ptr [r14 + 0x40]
00322449  A8 08                           test al, 8
0032244B  0F 85 EE 00 00 00               jne 0x14032253f
00322451  48 F7 05 2C 46 CA 00 00 04 00 00  test qword ptr [rip + 0xca462c], 0x400
0032245C  0F 84 FF FC FF FF               je 0x140322161
00322462  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
00322465  0F BA E0 11                     bt eax, 0x11
00322469  0F 82 75 F6 FF FF               jb 0x140321ae4
0032246F  E9 ED FC FF FF                  jmp 0x140322161
00322474  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
0032247C  F6 40 45 10                     test byte ptr [rax + 0x45], 0x10
00322480  0F 85 82 FD FF FF               jne 0x140322208
00322486  E9 8F FB FF FF                  jmp 0x14032201a
0032248B  BB 05 00 00 C0                  mov ebx, 0xc0000005
00322490  E9 2D FC FF FF                  jmp 0x1403220c2
00322495  48 8B C1                        mov rax, rcx
00322498  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0032249C  80 38 01                        cmp byte ptr [rax], 1
0032249F  75 79                           jne 0x14032251a
003224A1  48 83 E1 FE                     and rcx, 0xfffffffffffffffe
003224A5  80 39 06                        cmp byte ptr [rcx], 6
003224A8  0F 84 DD F9 FF FF               je 0x140321e8b
003224AE  E9 2F FF FF FF                  jmp 0x1403223e2
003224B3  48 8D 94 24 C0 00 00 00         lea rdx, [rsp + 0xc0]
003224BB  E8 A8 26 F7 FF                  call 0x140294b68
003224C0  48 8B 9C 24 C0 00 00 00         mov rbx, qword ptr [rsp + 0xc0]
003224C8  44 8B F0                        mov r14d, eax
003224CB  E9 1A FA FF FF                  jmp 0x140321eea
003224D0  48 8B D3                        mov rdx, rbx
003224D3  48 8B CF                        mov rcx, rdi
003224D6  E8 D1 29 F7 FF                  call 0x140294eac
003224DB  E9 16 FA FF FF                  jmp 0x140321ef6
003224E0  48 8B C1                        mov rax, rcx
003224E3  48 83 E0 FE                     and rax, 0xfffffffffffffffe
003224E7  80 38 01                        cmp byte ptr [rax], 1
003224EA  0F 84 AD F7 FF FF               je 0x140321c9d
003224F0  E9 94 FB FF FF                  jmp 0x140322089
003224F5  48 8B C1                        mov rax, rcx
003224F8  48 83 E0 FE                     and rax, 0xfffffffffffffffe
003224FC  80 38 03                        cmp byte ptr [rax], 3
003224FF  0F 84 A3 FC FF FF               je 0x1403221a8
00322505  48 8B C1                        mov rax, rcx
00322508  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0032250C  80 38 06                        cmp byte ptr [rax], 6
0032250F  0F 85 BB FA FF FF               jne 0x140321fd0
00322515  E9 8E FC FF FF                  jmp 0x1403221a8
0032251A  48 8B C1                        mov rax, rcx
0032251D  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00322521  80 38 03                        cmp byte ptr [rax], 3
00322524  0F 84 77 FF FF FF               je 0x1403224a1
0032252A  48 8B C1                        mov rax, rcx
0032252D  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00322531  80 38 06                        cmp byte ptr [rax], 6
00322534  0F 84 67 FF FF FF               je 0x1403224a1
0032253A  E9 4C F9 FF FF                  jmp 0x140321e8b
0032253F  F6 C3 04                        test bl, 4
00322542  0F 84 9C F5 FF FF               je 0x140321ae4
00322548  E9 04 FF FF FF                  jmp 0x140322451
0032254D  BB 05 00 00 C0                  mov ebx, 0xc0000005
00322552  E9 6B FB FF FF                  jmp 0x1403220c2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiResolveProtoPteFault(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p158;
    unsigned __int64 v_stack_p160;
    unsigned __int64 v_stack_p168;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p180;
    unsigned __int64 v_stack_p190;
    unsigned __int64 v_stack_p198;
    unsigned __int64 v_stack_p1A0;
    unsigned __int64 v_stack_p1A8;
    unsigned __int64 v_stack_p1B0;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p200;
    unsigned __int64 v_stack_p208;
    unsigned __int64 v_stack_p210;
    unsigned __int64 v_stack_p2D8;
    unsigned __int64 v_stack_p2E0;
    unsigned __int64 v_stack_p2F0;
    unsigned __int64 v_stack_p350;
    unsigned __int64 v_stack_p358;
    unsigned int v_stack_p368;
    unsigned __int64 v_stack_p378;
    unsigned __int64 v_stack_p3F8;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p4A0;
    unsigned __int8 v_stack_p4A3;
    unsigned __int64 v_stack_p4A8;
    unsigned __int64 v_stack_p4B0;
    unsigned __int64 v_stack_p548;
    unsigned __int64 v_stack_p558;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned int v_stack_pC8;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;

    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (112);
    v_r15 = 0;
    v_stack_m50 = *(unsigned __int64 *)(a1 + 56);
    *(unsigned __int64 *)(a3) = 0;
    v_r13 = (*(unsigned __int64 *)(a1)) >> (9);
    v_r13 = (v_r13) & (a4);
    v_stack_m78 = *(unsigned __int64 *)(a1);
    v_r13 = (v_r13) + (a3);
    v_stack_m48 = v_r13;
    result = (unsigned int)((*(unsigned __int64 *)(a1 + 16)) & (1));
    v_stack_m68 = *(unsigned __int64 *)(a1 + 16);
    v_stack_m58 = result;
    if (condition_is_not_equal) goto loc_00321D3C;
loc_003217C8:
    v_stack_m60 = 0;
loc_003217CD:
    v_stack_m70 = *(unsigned __int64 *)(a1 + 104);
    v_rdi = (*(unsigned __int64 *)(a1 + 104)) >> (9);
    v_rdi = (v_rdi) & (a4);
    v_rdi = (v_rdi) + (a3);
loc_003217F0:
loc_00321810:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (1)) == 0) goto loc_00321883;
    if (condition_is_below) goto loc_00321883;
    v_rbx = (*(unsigned __int64 *)(v_rdi)) >> (12);
    v_rbx = (v_rbx) & (*(unsigned __int64 *)(a1 + 16));
    if (v_rbx > (*(unsigned __int64 *)(v_rip + 11584691))) goto loc_00321810;
    a1 = (v_rbx + v_rbx * 2) + (v_rbx + v_rbx * 2);
    if (((a4) & (*(unsigned __int64 *)(a3 + a1 * 8))) == 0) goto loc_00321810;
loc_00321860:
    if (condition_is_below) goto loc_00321D70;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (1)) != 0) goto loc_00321899;
loc_00321874:
loc_00321883:
loc_00321888:
    v_rsp = (v_rsp) + (112);
    return (unsigned int)(0xC0000016ULL);
loc_00321899:
    if (condition_is_below) goto loc_00321874;
    result = ((unsigned int)(0xC0000016ULL)) >> (12);
    result = (result) & (*(unsigned __int64 *)(a1 + 16));
    if (v_rbx != result) goto loc_00321B83;
    if (v_rbx < result) goto loc_00321917;
    if (v_rbx < result) goto loc_00321917;
    result = (*(unsigned __int64 *)(v_r10 + a1 * 8 + 24)) & (a1);
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_r10 + a1 * 8 + 32))) == 0) goto loc_00321B97;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_r10 + a1 * 8 + 32)))) != 1) goto loc_00321F22;
    if (result == 0) goto loc_0032224E;
loc_0032190C:
loc_0032190F:
    if (1 != 0) goto loc_00321B97;
loc_00321917:
    v_stack_pC8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r10 + a1 * 8 + 32)));
    result = (unsigned __int16)(((unsigned int)(*(unsigned int *)(v_r10 + a1 * 8 + 32))) + 1);
    v_stack_pC8 = (unsigned __int16)(result);
    *(unsigned int *)(v_r10 + a1 * 8 + 32) = (unsigned int)((unsigned int)(v_stack_pC8));
loc_00321936:
    result = MiLockOwnedProtoPage(v_r10 + a1 * 8, (unsigned int)(*(unsigned int *)(v_r10 + a1 * 8 + 32)), a3, a4);
    v_r14 = 0;
loc_00321941:
loc_0032194B:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)))) & (1)) != 0) goto loc_003219A8;
    result = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104))) & (0xC00ULL));
    if (result != 0x800ULL) goto loc_00321F9B;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)) == 0) goto loc_0032197D;
    if (*(unsigned __int64 *)(v_rip + 11584268) != 0) goto loc_00321D53;
loc_0032197D:
    if (*(unsigned __int64 *)(v_rip + 11584252) == 0) goto loc_0032199E;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)))) & (16)) != 0) goto loc_00321F4D;
    result = ~(*(unsigned __int64 *)(v_rip + 11584252));
    result = (result) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)));
loc_0032199E:
loc_003219A8:
    result = (result) >> (12);
    result = (result) & (*(unsigned __int64 *)(v_rip + 11584252));
    if (result > (*(unsigned __int64 *)(v_rip + 11584298))) goto loc_0032194B;
    a1 = (result + result * 2) + (result + result * 2);
    if (condition_is_above_or_equal) goto loc_00321941;
loc_003219F0:
    if (condition_is_below) goto loc_00321DE0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)))) goto loc_00322184;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + a1 * 8) + a1 * 8 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (sign_flag) goto loc_0032225D;
loc_00321A2D:
    if ((*(unsigned __int64 *)(a1 + 104)) < ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11593331) + result * 8) + 4)))) goto loc_00321A6F;
    if ((*(unsigned __int64 *)(a1 + 104)) > ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11593331) + result * 8) + 4)))) goto loc_00321A6F;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)))) & (1)) == 0) goto loc_00321C30;
    a1 = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)))) & (66)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)))) & (32)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00321D91;
loc_00321A6F:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)))) & (1)) == 0) goto loc_00321C30;
    if (v_stack_p48 != 0) goto loc_00321F56;
    if (!sign_flag) goto loc_00321AE4;
    if (condition_is_above_or_equal) goto loc_00321AE4;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + a1 * 8) + a1 * 8 + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) == 3) goto loc_00321AE4;
    if (*(unsigned __int64 *)(v_rip + 11583952) == 0) goto loc_00321AC1;
    result = *(unsigned __int64 *)(v_rip + 11583952);
    v_rdi = *(unsigned __int64 *)(*(unsigned __int64 *)(result + a1 * 8) + a1 * 8 + 16);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + a1 * 8) + a1 * 8 + 16))) & (16)) == 0) {
        result = ~(*(unsigned __int64 *)(v_rip + 11583952));
        v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + a1 * 8) + a1 * 8 + 16)) & (result);
    }
    v_rdi = (v_rdi) >> (16);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi) + 56)))) & (32)) == 0) goto loc_00321AE4;
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) + 96)) & (-8);
    if (*(unsigned __int64 *)(v_rbx + 40) != 0) goto loc_00322106;
loc_00321AE4:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(result + a1 * 8) + a1 * 8 + 24)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(result + a1 * 8) + a1 * 8 + 24) + 1);
    result = (result) & (*(unsigned __int64 *)(v_rip + 11593331));
    result = (result) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(result + a1 * 8) + a1 * 8 + 24) + 1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + a1 * 8) + a1 * 8 + 24) = result;
    result = MiUnlockProtoPoolPage(v_r10 + a1 * 8, 17, a3, a4);
    v_r15 = (*(unsigned __int64 *)(result + a1 * 8) + a1 * 8) - (result);
    v_stack_p20 = v_stack_p40;
    a4 = 0;
    v_r15 = (v_r15) >> (4);
    a2 = (17) * (v_r15);
    result = MiCompleteProtoPteFault(v_stack_pB0, a2, v_stack_pB8, a4);
    if (!sign_flag) { result = 272; }
    v_rsp = (v_rsp) + (112);
    return result;
loc_00321B83:
    goto loc_003217F0;
loc_00321B97:
    v_rdi = 0;
    if (sign_flag) goto loc_003220F3;
loc_00321BA7:
    result = MiIsPfnCommitNotCharged(v_r10 + a1 * 8, a2, v_stack_pB8, a4);
    if ((unsigned int)(result) == 0) goto loc_003223C5;
loc_00321BB7:
    a1 = (*(unsigned __int64 *)(v_r10 + a1 * 8 + 40)) >> (43);
    a1 = (unsigned int)((a1) & (0x3FFULL));
    result = MiChargeCommit(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11592896) + a1 * 8), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)), 4, a4);
    if ((unsigned int)(result) == 0) goto loc_00321936;
loc_00321BF2:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11592896) + a1 * 8)) != (v_rip + 11628807)) goto loc_0032233D;
loc_00321C11:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)) - 1)) > -3) goto loc_0032233D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 35740)) - 1)) == -3) goto loc_00321917;
    goto loc_00321C11;
loc_00321C30:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)) == 0) goto loc_003223A5;
    v_r12 = 0;
    result = MI_READ_PTE_LOCK_FREE(v_r13, *(unsigned __int64 *)(gs_base + (0 + 32)), 4, a4);
    if (condition_is_above_or_equal) goto loc_00321FF0;
    if (*(unsigned __int64 *)(v_rip + 11583527) == 0) goto loc_00321C71;
    if ((((unsigned __int8)(result)) & (16)) != 0) goto loc_00321F44;
    result = ~(*(unsigned __int64 *)(v_rip + 11583527));
    result = (result) & (result);
loc_00321C71:
    result = (result) >> (32);
    if (result != ((unsigned int)(0xFFFFFFFFULL))) goto loc_00321FF0;
    v_r12 = (result) >> (5);
    v_r12 = (unsigned int)((v_r12) & (31));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (0xFFFFFFF8ULL));
    if (((unsigned int)(result)) == 16) goto loc_003221F6;
loc_00321C9D:
loc_00321CAA:
    if (*(unsigned __int64 *)(v_rip + 11583439) == 0) goto loc_00321CC8;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)))) & (16)) == 0) {
        result = *(unsigned __int64 *)(v_rip + 11583439);
        result = ~(result);
        result = (result) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104)));
    }
    if (condition_is_below) goto loc_00321CE4;
    if (condition_is_above_or_equal) goto loc_00321DFF;
loc_00321CE4:
loc_00321CE9:
    if (condition_is_below) goto loc_00322228;
    if (condition_is_above_or_equal) goto loc_00321FA3;
    v_stack_pC8 = v_stack_p168;
    result = MiResolveTransitionFault(v_stack_p158, v_stack_pE0, v_r10 + a1 * 8, v_stack_p160);
loc_00321D27:
loc_00321D29:
    v_rsp = (v_rsp) + (112);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00321D3C:
    a2 = (v_stack_pE0) & (-2);
    v_stack_p198 = a2;
    if ((*(unsigned __int8 *)(a2)) == 1) goto loc_003217CD;
    goto loc_003217C8;
loc_00321D53:
    if ((((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) & ((unsigned int)((unsigned int)(result)))) == 0) goto loc_0032194B;
    goto loc_0032197D;
loc_00321D70:
    v_r14 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104))) + 1);
    if (((*(unsigned int *)(v_rip + 13251890)) & ((unsigned int)(v_r14))) == 0) goto loc_0032229A;
loc_00321D80:
loc_00321D82:
    if (!sign_flag) goto loc_00321860;
    goto loc_00321D70;
loc_00321D91:
    result = MiPteHasShadow(v_stack_p158, a2, v_r10 + a1 * 8, v_stack_p160);
    if (result == 0) goto loc_00321A6F;
    if (*(unsigned __int64 *)(result + 1288) == 0) goto loc_00321A6F;
    result = (v_r12) >> (3);
    result = (unsigned int)((result) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (32)) != 0) {
        v_r14 = (v_r14) | (32);
    }
    v_r14 = (v_r14) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + result * 8))) & (66)) == 0) { v_r14 = v_r14; }
    goto loc_00321A6F;
loc_00321DE0:
    v_rdi = (unsigned int)((v_stack_pE0) + 1);
    if (((*(unsigned int *)(v_rip + 13251780)) & ((unsigned int)(v_rdi))) == 0) goto loc_003222C2;
loc_00321DEE:
loc_00321DF0:
    if (!sign_flag) goto loc_003219F0;
    goto loc_00321DE0;
loc_00321DFF:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_pD8 + 24))) & (4)) != 0) goto loc_00321CE4;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (5));
    if (((unsigned __int8)(result)) != 5) goto loc_00321CE4;
    if (a2 == 0) goto loc_0032238F;
loc_00321E1E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_p1A8 + 184)))) & (15)) != 0) goto loc_00321E4B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 640)) != 0) goto loc_00321CE4;
loc_00321E4B:
    if (((*(unsigned __int64 *)(v_rip + 13257778)) & (0x8000ULL)) != 0) goto loc_0032236F;
loc_00321E61:
    result = MiUnlockProtoPoolPage(v_r10 + a1 * 8, 17, v_r10 + a1 * 8, v_stack_p160);
    if (v_stack_p1A0 != 0) goto loc_00322495;
    a2 = 0;
    result = KeInvalidAccessAllowed(v_stack_p190, a2, v_r10 + a1 * 8, v_stack_p160);
    if ((unsigned __int8)(result) != 0) goto loc_003223E2;
loc_00321E8B:
    result = MiIsPrototypePteVadLookup(result, a2, v_r10 + a1 * 8, v_stack_p160);
    v_r13 = (result) >> (5);
    v_r14 = (v_r14) >> (5);
    if ((unsigned int)(result) == 0) { v_r13 = v_r14; }
    v_r13 = (unsigned int)((v_r13) & (24));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) & (2));
    a1 = (unsigned int)((a1) | (4));
    if (((unsigned int)(v_r13)) == 8) goto loc_00322387;
    if (((unsigned int)(v_r13)) == 24) goto loc_003223ED;
loc_00321EC2:
    result = MiMakeDemandZeroPte(a1, a2, v_r10 + a1 * 8, v_stack_p160);
    v_stack_p210 = result;
    result = MiPteInShadowRange(v_stack_p1B0, a2, v_r10 + a1 * 8, v_stack_p160);
    if ((unsigned int)(result) != 0) goto loc_003224B3;
    v_r14 = 0;
loc_00321EEA:
    *(unsigned __int64 *)(v_stack_p1B0) = result;
    if (0 != 0) goto loc_003224D0;
loc_00321EF6:
    a3 = 0;
    result = MiResolveDemandZeroFault(v_stack_p200, v_stack_p1B0, a3, v_stack_p208);
    v_rsp = (v_rsp) + (112);
    return result;
loc_00321F22:
    if (((unsigned __int16)(v_stack_p1B0)) != 2) goto loc_00321917;
    if (result == 0) goto loc_00321917;
    if (((*(unsigned __int8 *)(v_r10 + a1 * 8 + 34)) & (8)) == 0) goto loc_00321917;
    goto loc_00321B97;
loc_00321F44:
    result = (result) & (-17);
    goto loc_00321C71;
loc_00321F4D:
    result = (result) & (-17);
    goto loc_0032199E;
loc_00321F56:
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(0xFFFFFFFFULL) + 80))) & (7));
    result = MiGetPfnPriority(v_stack_p180, v_stack_p1B0, a3, v_stack_p208);
    if (((unsigned int)(v_r10)) > ((unsigned int)(result))) goto loc_003222E9;
loc_00321F6F:
    result = MiUnlockProtoPoolPage(v_r10 + a1 * 8, 17, a3, v_stack_p208);
    result = 0;
    v_rsp = (v_rsp) + (112);
    return result;
loc_00321F9B:
    v_r15 = 0;
    goto loc_00321A2D;
loc_00321FA3:
    result = MiGetPagingFileOffset(0, 17, a3, v_stack_p208);
    if ((unsigned int)(result) != 0) goto loc_00322313;
    if ((((unsigned __int8)(v_stack_p2E0)) & (1)) != 0) goto loc_00322198;
    a2 = 0;
    result = KeInvalidAccessAllowed(v_stack_p2E0, a2, a3, v_stack_p208);
    if ((unsigned __int8)(result) != 0) goto loc_003221B5;
loc_00321FD0:
    result = MiResolveDemandZeroFault(v_stack_p350, v_stack_p1B0, v_r10 + a1 * 8, v_stack_p358);
    goto loc_00321D27;
loc_00321FF0:
    if ((((unsigned __int8)(v_r13)) & (8)) != 0) goto loc_00321C9D;
    result = (0) >> (5);
    result = (unsigned int)((result) & (31));
    result = (unsigned int)((result) >> (3));
    v_stack_p368 = (unsigned int)(result);
    if (((unsigned int)(result)) == 2) goto loc_00322474;
loc_0032201A:
    result = MI_READ_PTE_LOCK_FREE(v_stack_p2D8, v_stack_p1B0, v_r10 + a1 * 8, v_stack_p358);
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_00322272;
    a1 = 1;
    if (v_stack_p358 == 0) { a1 = (unsigned int)((unsigned __int8)(v_stack_p358)); }
    result = (unsigned int)(((unsigned int)((unsigned int)(result))) & (7));
    result = (unsigned int)(((__int8)(*(unsigned __int8 *)(result + v_rip - 3215329 * 1))) - ((unsigned int)((__int8)((unsigned __int8)(a1)))));
    if (((unsigned int)(result)) < 10) goto loc_0032248B;
    if (v_stack_p368 != 2) goto loc_00321C9D;
    if (v_stack_p2F0 != 0) goto loc_003224E0;
loc_00322089:
    result = MiAllowGuardFault(v_stack_p2E0, v_rip - 3215329, v_r10 + a1 * 8, v_stack_p358);
    if ((unsigned int)(result) == 0) goto loc_0032254D;
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(result))) & (15));
    v_rbx = (result) & (-993);
    v_rdi = (v_rdi) << (5);
    v_rdi = (v_rdi) | (v_rbx);
    result = (unsigned int)((result) & (0xC00ULL));
    *(unsigned __int64 *)(v_stack_p2D8) = v_rdi;
loc_003220C2:
    if (0 != 0) {
    }
    result = MiUnlockProtoPoolPage(v_r10 + a1 * 8, 17, v_r10 + a1 * 8, v_stack_p358);
    v_rsp = (v_rsp) + (112);
    return (unsigned int)((unsigned int)((unsigned int)(0x80000001ULL)));
loc_003220F3:
    if (condition_is_below) goto loc_00321BB7;
    goto loc_00321BA7;
loc_00322106:
    result = ((unsigned int)(0x80000001ULL)) & (-8);
    if (result <= (v_r10 + a1 * 8)) goto loc_00321AE4;
    result = (unsigned __int8)(((unsigned __int8)((unsigned int)(0x80000001ULL))) & (3));
    if (((unsigned __int8)(result)) == 2) goto loc_00321AE4;
    if (v_stack_p378 < result) goto loc_003223F5;
    if (((*(unsigned __int64 *)(v_rip + 13257016)) & (0x8000ULL)) == 0) goto loc_00321AE4;
    if (((*(unsigned __int8 *)(v_r15 + 16)) & (64)) == 0) goto loc_00321AE4;
loc_00322161:
    result = MiUnlockProtoPoolPage(v_r10 + a1 * 8, 17, v_r10 + a1 * 8, v_stack_p358);
    goto loc_00321888;
loc_00322184:
    goto loc_00321941;
loc_00322198:
    result = (v_r10 + a1 * 8) & (-2);
    if ((*(unsigned __int8 *)(result)) != 1) goto loc_003224F5;
loc_003221A8:
    a1 = (v_r10 + a1 * 8) & (-2);
    if ((*(unsigned __int8 *)(a1)) == 6) goto loc_00321FD0;
loc_003221B5:
    if (0 < ((unsigned int)(0x80000001ULL))) goto loc_00321FD0;
    result = MiIsPrototypePteVadLookup(v_r13, 17, v_r10 + a1 * 8, v_stack_p358);
    v_r14 = (v_stack_p378) >> (5);
    v_r13 = (v_r13) >> (5);
    if ((unsigned int)(result) != 0) { v_r14 = v_r13; }
    v_r14 = (unsigned __int8)((v_r14) & (24));
    if (((unsigned __int8)(v_r14)) != 16) goto loc_00321FD0;
    result = MiUnlockProtoPoolPage(v_r10 + a1 * 8, 17, v_r10 + a1 * 8, v_stack_p358);
    goto loc_00321D29;
loc_003221F6:
    if (((*(unsigned __int8 *)(v_stack_p3F8 + 69)) & (16)) == 0) goto loc_00321C9D;
loc_00322208:
    result = MiUnlockProtoPoolPage(v_r10 + a1 * 8, 17, v_r10 + a1 * 8, v_stack_p358);
    v_rsp = (v_rsp) + (112);
    return (unsigned int)(0xC0000434ULL);
loc_00322228:
    if (((*(unsigned __int8 *)(v_stack_p4A0 + 69)) & (16)) != 0) goto loc_00322208;
    result = MiResolveMappedFileFault(v_stack_p4A0, v_rdi, v_r10 + a1 * 8, v_stack_p4B0);
    goto loc_00321D27;
loc_0032224E:
    if (((*(unsigned __int8 *)(v_r10 + a1 * 8 + 34)) & (8)) == 0) goto loc_0032190F;
    goto loc_0032190C;
loc_0032225D:
    result = MiLockSpecialPurposeMemoryCachedPage(0, 2, v_r10 + a1 * 8, v_stack_p4B0);
    goto loc_00321A2D;
loc_00322272:
    if (v_stack_p4A8 == 0) goto loc_00321CAA;
    if ((((unsigned int)(0xC0000005ULL)) & (0xA00ULL)) != 0) goto loc_00321CAA;
    goto loc_003220C2;
loc_0032229A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13256728)))) & (64)) == 0) goto loc_00321D80;
    result = KiCheckVpBackingLongSpinWaitHypercall(0, v_stack_p4A8, v_r10 + a1 * 8, v_stack_p4B0);
    if ((unsigned __int8)(result) == 0) goto loc_00321D80;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), v_stack_p4A8, v_r10 + a1 * 8, v_stack_p4B0);
    goto loc_00321D82;
loc_003222C2:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13256688)))) & (64)) == 0) goto loc_00321DEE;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_r14)), v_stack_p4A8, v_r10 + a1 * 8, v_stack_p4B0);
    if ((unsigned __int8)(result) == 0) goto loc_00321DEE;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), v_stack_p4A8, v_r10 + a1 * 8, v_stack_p4B0);
    goto loc_00321DF0;
loc_003222E9:
    v_stack_p4A0 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 32))) >> (24));
    result = (unsigned __int8)((result) & (248));
    result = (unsigned __int8)((result) | ((unsigned __int8)(v_r10)));
    v_stack_p4A3 = (unsigned __int8)(result);
    *(unsigned int *)(result + 32) = (unsigned int)((unsigned int)(v_stack_p4A0));
    goto loc_00321F6F;
loc_00322313:
    if (((*(unsigned __int8 *)(v_stack_p4A0 + 69)) & (16)) != 0) goto loc_00322208;
    result = MiResolvePageFileFault(v_stack_p4A0, v_rdi, v_r10 + a1 * 8, v_stack_p4B0);
    goto loc_00321D27;
loc_0032233D:
    result = MiChargePartitionResidentAvailable((unsigned int)(0xC0000005ULL), v_r14, v_r10, v_stack_p4B0);
    if ((unsigned int)(result) != 0) goto loc_00321917;
    if ((unsigned __int8)(v_rdi) == 0) goto loc_00321936;
    a3 = 0;
    result = MiReturnCommit((unsigned int)(0xC0000005ULL), v_r14, a3, v_stack_p4B0);
    goto loc_00321936;
loc_0032236F:
    if (result < ((unsigned int)(0xC0000005ULL))) goto loc_00321E61;
    if ((((unsigned __int8)((unsigned int)((unsigned int)(result)))) & (2)) == 0) goto loc_00321E61;
    goto loc_00321CE9;
loc_00322387:
    a1 = (unsigned int)(((unsigned int)(0xC0000005ULL)) | (8));
    goto loc_00321EC2;
loc_0032238F:
    result = (unsigned __int8)(((unsigned __int8)(v_r14)) >> (5));
    result = (unsigned __int8)((result) & (5));
    if (((unsigned __int8)(result)) != 4) goto loc_00321E1E;
    goto loc_00321CE4;
loc_003223A5:
    result = MiUnlockProtoPoolPage(v_r10 + a1 * 8, 17, a3, v_stack_p4B0);
loc_003223AF:
    v_rsp = (v_rsp) + (112);
    return (unsigned int)(0xC0000005ULL);
loc_003223C5:
    result = (*(unsigned __int64 *)(v_r10 + a1 * 8 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    goto loc_00321BF2;
loc_003223E2:
    if (result < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11590840) + result * 8))) goto loc_00321E8B;
    goto loc_003223AF;
loc_003223ED:
    a1 = (unsigned int)((*(unsigned __int64 *)(v_rip + 11590840)) | (24));
    goto loc_00321EC2;
loc_003223F5:
    result = MiLockVadTree(1, 17, a3, v_stack_p4B0);
    result = MiLocateAddress(v_r14, 17, a3, v_stack_p4B0);
    result = MiUnlockVadTree(1, 17, a3, v_stack_p4B0);
    if (result == 0) goto loc_00322161;
    a1 = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 48))))) & (112));
    if (((unsigned __int8)(a1)) != 32) goto loc_00322161;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 48))) & (0xF80ULL));
    if (((unsigned int)(a2)) == 128) goto loc_00321AE4;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 64)))) & (8)) != 0) goto loc_0032253F;
loc_00322451:
    if (((*(unsigned __int64 *)(v_rip + 13256236)) & (0x400ULL)) == 0) goto loc_00322161;
    if (condition_is_below) goto loc_00321AE4;
    goto loc_00322161;
loc_00322474:
    if (((*(unsigned __int8 *)(v_stack_p548 + 69)) & (16)) != 0) goto loc_00322208;
    goto loc_0032201A;
loc_0032248B:
    goto loc_003220C2;
loc_00322495:
    result = (a1) & (-2);
    if ((*(unsigned __int8 *)(result)) != 1) goto loc_0032251A;
loc_003224A1:
    a1 = (a1) & (-2);
    if ((*(unsigned __int8 *)(a1)) == 6) goto loc_00321E8B;
    goto loc_003223E2;
loc_003224B3:
    result = MiSanitizeShadowPxe(a1, v_stack_p558, a3, v_stack_p4B0);
    goto loc_00321EEA;
loc_003224D0:
    result = MiWritePteShadow(v_rdi, v_stack_p558, a3, v_stack_p4B0);
    goto loc_00321EF6;
loc_003224E0:
    result = (v_rdi) & (-2);
    if ((*(unsigned __int8 *)(result)) == 1) goto loc_00321C9D;
    goto loc_00322089;
loc_003224F5:
    result = (v_rdi) & (-2);
    if ((*(unsigned __int8 *)(result)) == 3) goto loc_003221A8;
    result = (v_rdi) & (-2);
    if ((*(unsigned __int8 *)(result)) != 6) goto loc_00321FD0;
    goto loc_003221A8;
loc_0032251A:
    result = (v_rdi) & (-2);
    if ((*(unsigned __int8 *)(result)) == 3) goto loc_003224A1;
    result = (v_rdi) & (-2);
    if ((*(unsigned __int8 *)(result)) == 6) goto loc_003224A1;
    goto loc_00321E8B;
loc_0032253F:
    if ((((unsigned __int8)(v_stack_p558)) & (4)) == 0) goto loc_00321AE4;
    goto loc_00322451;
loc_0032254D:
    goto loc_003220C2;
}
```

## 5. (Beta) C Style

```c
int64_t MiResolveProtoPteFault(void *Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_p10;
    uint64_t v_stack_p158;
    uint64_t v_stack_p160;
    uint64_t v_stack_p168;
    uint64_t v_stack_p18;
    uint64_t v_stack_p180;
    uint64_t v_stack_p190;
    uint64_t v_stack_p198;
    uint64_t v_stack_p1A0;
    uint64_t v_stack_p1A8;
    uint64_t v_stack_p1B0;
    uint64_t v_stack_p20;
    uint64_t v_stack_p200;
    uint64_t v_stack_p208;
    uint64_t v_stack_p210;
    uint64_t v_stack_p2D8;
    uint64_t v_stack_p2E0;
    uint64_t v_stack_p2F0;
    uint64_t v_stack_p350;
    uint64_t v_stack_p358;
    uint32_t v_stack_p368;
    uint64_t v_stack_p378;
    uint64_t v_stack_p3F8;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p4A0;
    uint8_t v_stack_p4A3;
    uint64_t v_stack_p4A8;
    uint64_t v_stack_p4B0;
    uint64_t v_stack_p548;
    uint64_t v_stack_p558;
    uint64_t v_stack_p8;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint32_t v_stack_pC8;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;

    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (112);
    local_r15 = 0;
    v_stack_m50 = *(uint64_t *)(arg1 + 0x38);
    *(uint64_t *)(arg3) = 0;
    local_r13 = (*(uint64_t *)(arg1)) >> (9);
    local_r13 = (local_r13) & (a4);
    v_stack_m78 = *(uint64_t *)(arg1);
    local_r13 = (local_r13) + (Arg3);
    v_stack_m48 = local_r13;
    result = (uint32_t)((*(uint64_t *)(arg1 + 0x10)) & (1));
    v_stack_m68 = *(uint64_t *)(arg1 + 0x10);
    v_stack_m58 = result;
    if (condition_is_not_equal) goto loc_00321D3C;
loc_003217C8:
    v_stack_m60 = 0;
loc_003217CD:
    v_stack_m70 = *(uint64_t *)(arg1 + 0x68);
    local_rdi = (*(uint64_t *)(arg1 + 0x68)) >> (9);
    local_rdi = (local_rdi) & (a4);
    local_rdi = (local_rdi) + (Arg3);
loc_003217F0:
loc_00321810:
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (1)) == 0) goto loc_00321883;
    if (condition_is_below) goto loc_00321883;
    local_rbx = (*(uint64_t *)(local_rdi)) >> (12);
    local_rbx = (local_rbx) & (*(uint64_t *)(arg1 + 0x10));
    if (local_rbx > (*(uint64_t *)(v_rip + 0xB0C4B3))) goto loc_00321810;
    Arg1 = (local_rbx + local_rbx * 2) + (local_rbx + local_rbx * 2);
    if (((a4) & (*(uint64_t *)(arg3 + arg1 * 8))) == 0) goto loc_00321810;
loc_00321860:
    if (condition_is_below) goto loc_00321D70;
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (1)) != 0) goto loc_00321899;
loc_00321874:
loc_00321883:
loc_00321888:
    local_rsp = (local_rsp) + (112);
    return (uint32_t)(0xC0000016ULL);
loc_00321899:
    if (condition_is_below) goto loc_00321874;
    result = ((uint32_t)(0xC0000016ULL)) >> (12);
    result = (result) & (*(uint64_t *)(arg1 + 0x10));
    if (local_rbx != result) goto loc_00321B83;
    if (local_rbx < result) goto loc_00321917;
    if (local_rbx < result) goto loc_00321917;
    result = (*(uint64_t *)(local_r10 + arg1 * 8 + 0x18)) & (Arg1);
    if ((uint16_t)((uint32_t)(*(uint32_t *)(local_r10 + arg1 * 8 + 0x20))) == 0) goto loc_00321B97;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(local_r10 + arg1 * 8 + 0x20)))) != 1) goto loc_00321F22;
    if (result == 0) goto loc_0032224E;
loc_0032190C:
loc_0032190F:
    if (1 != 0) goto loc_00321B97;
loc_00321917:
    v_stack_pC8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r10 + arg1 * 8 + 0x20)));
    result = (uint16_t)(((uint32_t)(*(uint32_t *)(local_r10 + arg1 * 8 + 0x20))) + 1);
    v_stack_pC8 = (uint16_t)(result);
    *(uint32_t *)(local_r10 + arg1 * 8 + 0x20) = (uint32_t)((uint32_t)(v_stack_pC8));
loc_00321936:
    result = MiLockOwnedProtoPage(local_r10 + Arg1 * 8, (uint32_t)(*(uint32_t *)(local_r10 + arg1 * 8 + 0x20)), Arg3, a4);
    local_r14 = 0;
loc_00321941:
loc_0032194B:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68)))) & (1)) != 0) goto loc_003219A8;
    result = (uint32_t)((*(uint64_t *)(*(uint64_t *)(arg1 + 0x68))) & (0xC00ULL));
    if (result != 0x800ULL) goto loc_00321F9B;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x68)) == 0) goto loc_0032197D;
    if (*(uint64_t *)(v_rip + 0xB0C30C) != 0) goto loc_00321D53;
loc_0032197D:
    if (*(uint64_t *)(v_rip + 0xB0C2FC) == 0) goto loc_0032199E;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68)))) & (16)) != 0) goto loc_00321F4D;
    result = ~(*(uint64_t *)(v_rip + 0xB0C2FC));
    result = (result) & (*(uint64_t *)(*(uint64_t *)(arg1 + 0x68)));
loc_0032199E:
loc_003219A8:
    result = (result) >> (12);
    result = (result) & (*(uint64_t *)(v_rip + 0xB0C2FC));
    if (result > (*(uint64_t *)(v_rip + 0xB0C32A))) goto loc_0032194B;
    Arg1 = (result + result * 2) + (result + result * 2);
    if (condition_is_above_or_equal) goto loc_00321941;
loc_003219F0:
    if (condition_is_below) goto loc_00321DE0;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x68))) != (*(uint64_t *)(*(uint64_t *)(arg1 + 0x68)))) goto loc_00322184;
    result = (*(uint64_t *)(*(uint64_t *)(result + arg1 * 8) + arg1 * 8 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (sign_flag) goto loc_0032225D;
loc_00321A2D:
    if ((*(uint64_t *)(arg1 + 0x68)) < ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0E673) + result * 8) + 0x4)))) goto loc_00321A6F;
    if ((*(uint64_t *)(arg1 + 0x68)) > ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0E673) + result * 8) + 0x4)))) goto loc_00321A6F;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68)))) & (1)) == 0) goto loc_00321C30;
    Arg1 = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68)))) & (66)) != 0) ? 1 : 0;
    result = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68)))) & (32)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00321D91;
loc_00321A6F:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68)))) & (1)) == 0) goto loc_00321C30;
    if (v_stack_p48 != 0) goto loc_00321F56;
    if (!sign_flag) goto loc_00321AE4;
    if (condition_is_above_or_equal) goto loc_00321AE4;
    result = (*(uint64_t *)(*(uint64_t *)(result + arg1 * 8) + arg1 * 8 + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) == 3) goto loc_00321AE4;
    if (*(uint64_t *)(v_rip + 0xB0C1D0) == 0) goto loc_00321AC1;
    result = *(uint64_t *)(v_rip + 0xB0C1D0);
    local_rdi = *(uint64_t *)(*(uint64_t *)(result + arg1 * 8) + arg1 * 8 + 0x10);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + arg1 * 8) + arg1 * 8 + 0x10))) & (16)) == 0) {
        result = ~(*(uint64_t *)(v_rip + 0xB0C1D0));
        local_rdi = (*(uint64_t *)(*(uint64_t *)(result + arg1 * 8) + arg1 * 8 + 0x10)) & (result);
    }
    local_rdi = (local_rdi) >> (16);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi) + 0x38)))) & (32)) == 0) goto loc_00321AE4;
    local_rbx = (*(uint64_t *)(*(uint64_t *)(local_rdi) + 0x60)) & (-8);
    if (*(uint64_t *)(local_rbx + 0x28) != 0) goto loc_00322106;
loc_00321AE4:
    result = (*(uint64_t *)(*(uint64_t *)(result + arg1 * 8) + arg1 * 8 + 0x18)) ^ (*(uint64_t *)(*(uint64_t *)(result + arg1 * 8) + arg1 * 8 + 0x18) + 1);
    result = (result) & (*(uint64_t *)(v_rip + 0xB0E673));
    result = (result) ^ (*(uint64_t *)(*(uint64_t *)(result + arg1 * 8) + arg1 * 8 + 0x18) + 1);
    *(uint64_t *)(*(uint64_t *)(result + arg1 * 8) + arg1 * 8 + 0x18) = result;
    result = MiUnlockProtoPoolPage(local_r10 + Arg1 * 8, 17, Arg3, a4);
    local_r15 = (*(uint64_t *)(result + arg1 * 8) + Arg1 * 8) - (result);
    v_stack_p20 = v_stack_p40;
    a4 = 0;
    local_r15 = (local_r15) >> (4);
    Arg2 = (17) * (local_r15);
    result = MiCompleteProtoPteFault(v_stack_pB0, Arg2, v_stack_pB8, a4);
    if (!sign_flag) { result = 272; }
    local_rsp = (local_rsp) + (112);
    return result;
loc_00321B83:
    goto loc_003217F0;
loc_00321B97:
    local_rdi = 0;
    if (sign_flag) goto loc_003220F3;
loc_00321BA7:
    result = MiIsPfnCommitNotCharged(local_r10 + Arg1 * 8, Arg2, v_stack_pB8, a4);
    if ((uint32_t)(result) == 0) goto loc_003223C5;
loc_00321BB7:
    Arg1 = (*(uint64_t *)(local_r10 + arg1 * 8 + 0x28)) >> (43);
    Arg1 = (uint32_t)((Arg1) & (0x3FFULL));
    result = MiChargeCommit(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0E4C0) + arg1 * 8), *(uint64_t *)(*(uint64_t *)(arg1 + 0x68)), 4, a4);
    if ((uint32_t)(result) == 0) goto loc_00321936;
loc_00321BF2:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0E4C0) + arg1 * 8)) != (v_rip + 11628807)) goto loc_0032233D;
loc_00321C11:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)) - 1)) > -3) goto loc_0032233D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8B9C)) - 1)) == -3) goto loc_00321917;
    goto loc_00321C11;
loc_00321C30:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x68)) == 0) goto loc_003223A5;
    local_r12 = 0;
    result = MI_READ_PTE_LOCK_FREE(local_r13, *(uint64_t *)(gs_base + (0 + 0x20)), 4, a4);
    if (condition_is_above_or_equal) goto loc_00321FF0;
    if (*(uint64_t *)(v_rip + 0xB0C027) == 0) goto loc_00321C71;
    if ((((uint8_t)(result)) & (16)) != 0) goto loc_00321F44;
    result = ~(*(uint64_t *)(v_rip + 0xB0C027));
    result = (result) & (result);
loc_00321C71:
    result = (result) >> (32);
    if (result != ((uint32_t)(0xFFFFFFFFULL))) goto loc_00321FF0;
    local_r12 = (result) >> (5);
    local_r12 = (uint32_t)((local_r12) & (31));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (0xFFFFFFF8ULL));
    if (((uint32_t)(result)) == 16) goto loc_003221F6;
loc_00321C9D:
loc_00321CAA:
    if (*(uint64_t *)(v_rip + 0xB0BFCF) == 0) goto loc_00321CC8;
    result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x68));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x68)))) & (16)) == 0) {
        result = *(uint64_t *)(v_rip + 0xB0BFCF);
        result = ~(result);
        result = (result) & (*(uint64_t *)(*(uint64_t *)(arg1 + 0x68)));
    }
    if (condition_is_below) goto loc_00321CE4;
    if (condition_is_above_or_equal) goto loc_00321DFF;
loc_00321CE4:
loc_00321CE9:
    if (condition_is_below) goto loc_00322228;
    if (condition_is_above_or_equal) goto loc_00321FA3;
    v_stack_pC8 = v_stack_p168;
    result = MiResolveTransitionFault(v_stack_p158, v_stack_pE0, local_r10 + Arg1 * 8, v_stack_p160);
loc_00321D27:
loc_00321D29:
    local_rsp = (local_rsp) + (112);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00321D3C:
    Arg2 = (v_stack_pE0) & (-2);
    v_stack_p198 = Arg2;
    if ((*(uint8_t *)(Arg2)) == 1) goto loc_003217CD;
    goto loc_003217C8;
loc_00321D53:
    if ((((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) & ((uint32_t)((uint32_t)(result)))) == 0) goto loc_0032194B;
    goto loc_0032197D;
loc_00321D70:
    local_r14 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(arg1 + 0x68))) + 1);
    if (((*(uint32_t *)(v_rip + 0xCA3532)) & ((uint32_t)(local_r14))) == 0) goto loc_0032229A;
loc_00321D80:
loc_00321D82:
    if (!sign_flag) goto loc_00321860;
    goto loc_00321D70;
loc_00321D91:
    result = MiPteHasShadow(v_stack_p158, Arg2, local_r10 + Arg1 * 8, v_stack_p160);
    if (result == 0) goto loc_00321A6F;
    if (*(uint64_t *)(result + 0x508) == 0) goto loc_00321A6F;
    result = (local_r12) >> (3);
    result = (uint32_t)((result) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (32)) != 0) {
        local_r14 = (local_r14) | (32);
    }
    local_r14 = (local_r14) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(result + 0x508) + result * 8))) & (66)) == 0) { local_r14 = local_r14; }
    goto loc_00321A6F;
loc_00321DE0:
    local_rdi = (uint32_t)((v_stack_pE0) + 1);
    if (((*(uint32_t *)(v_rip + 0xCA34C4)) & ((uint32_t)(local_rdi))) == 0) goto loc_003222C2;
loc_00321DEE:
loc_00321DF0:
    if (!sign_flag) goto loc_003219F0;
    goto loc_00321DE0;
loc_00321DFF:
    if ((((uint8_t)(*(uint64_t *)(v_stack_pD8 + 0x18))) & (4)) != 0) goto loc_00321CE4;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (5));
    if (((uint8_t)(result)) != 5) goto loc_00321CE4;
    if (Arg2 == 0) goto loc_0032238F;
loc_00321E1E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_p1A8 + 0xB8)))) & (15)) != 0) goto loc_00321E4B;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x280)) != 0) goto loc_00321CE4;
loc_00321E4B:
    if (((*(uint64_t *)(v_rip + 0xCA4C32)) & (0x8000ULL)) != 0) goto loc_0032236F;
loc_00321E61:
    result = MiUnlockProtoPoolPage(local_r10 + Arg1 * 8, 17, local_r10 + Arg1 * 8, v_stack_p160);
    if (v_stack_p1A0 != 0) goto loc_00322495;
    Arg2 = 0;
    result = KeInvalidAccessAllowed(v_stack_p190, Arg2, local_r10 + Arg1 * 8, v_stack_p160);
    if ((uint8_t)(result) != 0) goto loc_003223E2;
loc_00321E8B:
    result = MiIsPrototypePteVadLookup(result, Arg2, local_r10 + Arg1 * 8, v_stack_p160);
    local_r13 = (result) >> (5);
    local_r14 = (local_r14) >> (5);
    if ((uint32_t)(result) == 0) { local_r13 = local_r14; }
    local_r13 = (uint32_t)((local_r13) & (24));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) & (2));
    Arg1 = (uint32_t)((Arg1) | (4));
    if (((uint32_t)(local_r13)) == 8) goto loc_00322387;
    if (((uint32_t)(local_r13)) == 24) goto loc_003223ED;
loc_00321EC2:
    result = MiMakeDemandZeroPte(Arg1, Arg2, local_r10 + Arg1 * 8, v_stack_p160);
    v_stack_p210 = result;
    result = MiPteInShadowRange(v_stack_p1B0, Arg2, local_r10 + Arg1 * 8, v_stack_p160);
    if ((uint32_t)(result) != 0) goto loc_003224B3;
    local_r14 = 0;
loc_00321EEA:
    *(uint64_t *)(v_stack_p1B0) = result;
    if (0 != 0) goto loc_003224D0;
loc_00321EF6:
    Arg3 = 0;
    result = MiResolveDemandZeroFault(v_stack_p200, v_stack_p1B0, Arg3, v_stack_p208);
    local_rsp = (local_rsp) + (112);
    return result;
loc_00321F22:
    if (((uint16_t)(v_stack_p1B0)) != 2) goto loc_00321917;
    if (result == 0) goto loc_00321917;
    if (((*(uint8_t *)(local_r10 + arg1 * 8 + 0x22)) & (8)) == 0) goto loc_00321917;
    goto loc_00321B97;
loc_00321F44:
    result = (result) & (-17);
    goto loc_00321C71;
loc_00321F4D:
    result = (result) & (-17);
    goto loc_0032199E;
loc_00321F56:
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(0xFFFFFFFFULL) + 0x50))) & (7));
    result = MiGetPfnPriority(v_stack_p180, v_stack_p1B0, Arg3, v_stack_p208);
    if (((uint32_t)(local_r10)) > ((uint32_t)(result))) goto loc_003222E9;
loc_00321F6F:
    result = MiUnlockProtoPoolPage(local_r10 + Arg1 * 8, 17, Arg3, v_stack_p208);
    result = 0;
    local_rsp = (local_rsp) + (112);
    return result;
loc_00321F9B:
    local_r15 = 0;
    goto loc_00321A2D;
loc_00321FA3:
    result = MiGetPagingFileOffset(0, 17, Arg3, v_stack_p208);
    if ((uint32_t)(result) != 0) goto loc_00322313;
    if ((((uint8_t)(v_stack_p2E0)) & (1)) != 0) goto loc_00322198;
    Arg2 = 0;
    result = KeInvalidAccessAllowed(v_stack_p2E0, Arg2, Arg3, v_stack_p208);
    if ((uint8_t)(result) != 0) goto loc_003221B5;
loc_00321FD0:
    result = MiResolveDemandZeroFault(v_stack_p350, v_stack_p1B0, local_r10 + Arg1 * 8, v_stack_p358);
    goto loc_00321D27;
loc_00321FF0:
    if ((((uint8_t)(local_r13)) & (8)) != 0) goto loc_00321C9D;
    result = (0) >> (5);
    result = (uint32_t)((result) & (31));
    result = (uint32_t)((result) >> (3));
    v_stack_p368 = (uint32_t)(result);
    if (((uint32_t)(result)) == 2) goto loc_00322474;
loc_0032201A:
    result = MI_READ_PTE_LOCK_FREE(v_stack_p2D8, v_stack_p1B0, local_r10 + Arg1 * 8, v_stack_p358);
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_00322272;
    Arg1 = 1;
    if (v_stack_p358 == 0) { Arg1 = (uint32_t)((uint8_t)(v_stack_p358)); }
    result = (uint32_t)(((uint32_t)((uint32_t)(result))) & (7));
    result = (uint32_t)(((int8_t)(*(uint8_t *)(result + v_rip - 0x310FE1 * 1))) - ((uint32_t)((int8_t)((uint8_t)(Arg1)))));
    if (((uint32_t)(result)) < 10) goto loc_0032248B;
    if (v_stack_p368 != 2) goto loc_00321C9D;
    if (v_stack_p2F0 != 0) goto loc_003224E0;
loc_00322089:
    result = MiAllowGuardFault(v_stack_p2E0, v_rip - 3215329, local_r10 + Arg1 * 8, v_stack_p358);
    if ((uint32_t)(result) == 0) goto loc_0032254D;
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(result))) & (15));
    local_rbx = (result) & (-993);
    local_rdi = (local_rdi) << (5);
    local_rdi = (local_rdi) | (local_rbx);
    result = (uint32_t)((result) & (0xC00ULL));
    *(uint64_t *)(v_stack_p2D8) = local_rdi;
loc_003220C2:
    if (0 != 0) {
    }
    result = MiUnlockProtoPoolPage(local_r10 + Arg1 * 8, 17, local_r10 + Arg1 * 8, v_stack_p358);
    local_rsp = (local_rsp) + (112);
    return (uint32_t)((uint32_t)((uint32_t)(0x80000001ULL)));
loc_003220F3:
    if (condition_is_below) goto loc_00321BB7;
    goto loc_00321BA7;
loc_00322106:
    result = ((uint32_t)(0x80000001ULL)) & (-8);
    if (result <= (local_r10 + Arg1 * 8)) goto loc_00321AE4;
    result = (uint8_t)(((uint8_t)((uint32_t)(0x80000001ULL))) & (3));
    if (((uint8_t)(result)) == 2) goto loc_00321AE4;
    if (v_stack_p378 < result) goto loc_003223F5;
    if (((*(uint64_t *)(v_rip + 0xCA4938)) & (0x8000ULL)) == 0) goto loc_00321AE4;
    if (((*(uint8_t *)(local_r15 + 0x10)) & (64)) == 0) goto loc_00321AE4;
loc_00322161:
    result = MiUnlockProtoPoolPage(local_r10 + Arg1 * 8, 17, local_r10 + Arg1 * 8, v_stack_p358);
    goto loc_00321888;
loc_00322184:
    goto loc_00321941;
loc_00322198:
    result = (local_r10 + Arg1 * 8) & (-2);
    if ((*(uint8_t *)(result)) != 1) goto loc_003224F5;
loc_003221A8:
    Arg1 = (local_r10 + Arg1 * 8) & (-2);
    if ((*(uint8_t *)(arg1)) == 6) goto loc_00321FD0;
loc_003221B5:
    if (0 < ((uint32_t)(0x80000001ULL))) goto loc_00321FD0;
    result = MiIsPrototypePteVadLookup(local_r13, 17, local_r10 + Arg1 * 8, v_stack_p358);
    local_r14 = (v_stack_p378) >> (5);
    local_r13 = (local_r13) >> (5);
    if ((uint32_t)(result) != 0) { local_r14 = local_r13; }
    local_r14 = (uint8_t)((local_r14) & (24));
    if (((uint8_t)(local_r14)) != 16) goto loc_00321FD0;
    result = MiUnlockProtoPoolPage(local_r10 + Arg1 * 8, 17, local_r10 + Arg1 * 8, v_stack_p358);
    goto loc_00321D29;
loc_003221F6:
    if (((*(uint8_t *)(v_stack_p3F8 + 0x45)) & (16)) == 0) goto loc_00321C9D;
loc_00322208:
    result = MiUnlockProtoPoolPage(local_r10 + Arg1 * 8, 17, local_r10 + Arg1 * 8, v_stack_p358);
    local_rsp = (local_rsp) + (112);
    return (uint32_t)(0xC0000434ULL);
loc_00322228:
    if (((*(uint8_t *)(v_stack_p4A0 + 0x45)) & (16)) != 0) goto loc_00322208;
    result = MiResolveMappedFileFault(v_stack_p4A0, local_rdi, local_r10 + Arg1 * 8, v_stack_p4B0);
    goto loc_00321D27;
loc_0032224E:
    if (((*(uint8_t *)(local_r10 + arg1 * 8 + 0x22)) & (8)) == 0) goto loc_0032190F;
    goto loc_0032190C;
loc_0032225D:
    result = MiLockSpecialPurposeMemoryCachedPage(0, 2, local_r10 + Arg1 * 8, v_stack_p4B0);
    goto loc_00321A2D;
loc_00322272:
    if (v_stack_p4A8 == 0) goto loc_00321CAA;
    if ((((uint32_t)(0xC0000005ULL)) & (0xA00ULL)) != 0) goto loc_00321CAA;
    goto loc_003220C2;
loc_0032229A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCA4818)))) & (64)) == 0) goto loc_00321D80;
    result = KiCheckVpBackingLongSpinWaitHypercall(0, v_stack_p4A8, local_r10 + Arg1 * 8, v_stack_p4B0);
    if ((uint8_t)(result) == 0) goto loc_00321D80;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), v_stack_p4A8, local_r10 + Arg1 * 8, v_stack_p4B0);
    goto loc_00321D82;
loc_003222C2:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCA47F0)))) & (64)) == 0) goto loc_00321DEE;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_r14)), v_stack_p4A8, local_r10 + Arg1 * 8, v_stack_p4B0);
    if ((uint8_t)(result) == 0) goto loc_00321DEE;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), v_stack_p4A8, local_r10 + Arg1 * 8, v_stack_p4B0);
    goto loc_00321DF0;
loc_003222E9:
    v_stack_p4A0 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x20))) >> (24));
    result = (uint8_t)((result) & (248));
    result = (uint8_t)((result) | ((uint8_t)(local_r10)));
    v_stack_p4A3 = (uint8_t)(result);
    *(uint32_t *)(result + 0x20) = (uint32_t)((uint32_t)(v_stack_p4A0));
    goto loc_00321F6F;
loc_00322313:
    if (((*(uint8_t *)(v_stack_p4A0 + 0x45)) & (16)) != 0) goto loc_00322208;
    result = MiResolvePageFileFault(v_stack_p4A0, local_rdi, local_r10 + Arg1 * 8, v_stack_p4B0);
    goto loc_00321D27;
loc_0032233D:
    result = MiChargePartitionResidentAvailable((uint32_t)(0xC0000005ULL), local_r14, local_r10, v_stack_p4B0);
    if ((uint32_t)(result) != 0) goto loc_00321917;
    if ((uint8_t)(local_rdi) == 0) goto loc_00321936;
    Arg3 = 0;
    result = MiReturnCommit((uint32_t)(0xC0000005ULL), local_r14, Arg3, v_stack_p4B0);
    goto loc_00321936;
loc_0032236F:
    if (result < ((uint32_t)(0xC0000005ULL))) goto loc_00321E61;
    if ((((uint8_t)((uint32_t)((uint32_t)(result)))) & (2)) == 0) goto loc_00321E61;
    goto loc_00321CE9;
loc_00322387:
    Arg1 = (uint32_t)(((uint32_t)(0xC0000005ULL)) | (8));
    goto loc_00321EC2;
loc_0032238F:
    result = (uint8_t)(((uint8_t)(local_r14)) >> (5));
    result = (uint8_t)((result) & (5));
    if (((uint8_t)(result)) != 4) goto loc_00321E1E;
    goto loc_00321CE4;
loc_003223A5:
    result = MiUnlockProtoPoolPage(local_r10 + Arg1 * 8, 17, Arg3, v_stack_p4B0);
loc_003223AF:
    local_rsp = (local_rsp) + (112);
    return (uint32_t)(0xC0000005ULL);
loc_003223C5:
    result = (*(uint64_t *)(local_r10 + arg1 * 8 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    goto loc_00321BF2;
loc_003223E2:
    if (result < (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB0DCB8) + result * 8))) goto loc_00321E8B;
    goto loc_003223AF;
loc_003223ED:
    Arg1 = (uint32_t)((*(uint64_t *)(v_rip + 0xB0DCB8)) | (24));
    goto loc_00321EC2;
loc_003223F5:
    result = MiLockVadTree(1, 17, Arg3, v_stack_p4B0);
    result = MiLocateAddress(local_r14, 17, Arg3, v_stack_p4B0);
    result = MiUnlockVadTree(1, 17, Arg3, v_stack_p4B0);
    if (result == 0) goto loc_00322161;
    Arg1 = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x30))))) & (112));
    if (((uint8_t)(Arg1)) != 32) goto loc_00322161;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x30))) & (0xF80ULL));
    if (((uint32_t)(Arg2)) == 128) goto loc_00321AE4;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x40)))) & (8)) != 0) goto loc_0032253F;
loc_00322451:
    if (((*(uint64_t *)(v_rip + 0xCA462C)) & (0x400ULL)) == 0) goto loc_00322161;
    if (condition_is_below) goto loc_00321AE4;
    goto loc_00322161;
loc_00322474:
    if (((*(uint8_t *)(v_stack_p548 + 0x45)) & (16)) != 0) goto loc_00322208;
    goto loc_0032201A;
loc_0032248B:
    goto loc_003220C2;
loc_00322495:
    result = (Arg1) & (-2);
    if ((*(uint8_t *)(result)) != 1) goto loc_0032251A;
loc_003224A1:
    Arg1 = (Arg1) & (-2);
    if ((*(uint8_t *)(arg1)) == 6) goto loc_00321E8B;
    goto loc_003223E2;
loc_003224B3:
    result = MiSanitizeShadowPxe(Arg1, v_stack_p558, Arg3, v_stack_p4B0);
    goto loc_00321EEA;
loc_003224D0:
    result = MiWritePteShadow(local_rdi, v_stack_p558, Arg3, v_stack_p4B0);
    goto loc_00321EF6;
loc_003224E0:
    result = (local_rdi) & (-2);
    if ((*(uint8_t *)(result)) == 1) goto loc_00321C9D;
    goto loc_00322089;
loc_003224F5:
    result = (local_rdi) & (-2);
    if ((*(uint8_t *)(result)) == 3) goto loc_003221A8;
    result = (local_rdi) & (-2);
    if ((*(uint8_t *)(result)) != 6) goto loc_00321FD0;
    goto loc_003221A8;
loc_0032251A:
    result = (local_rdi) & (-2);
    if ((*(uint8_t *)(result)) == 3) goto loc_003224A1;
    result = (local_rdi) & (-2);
    if ((*(uint8_t *)(result)) == 6) goto loc_003224A1;
    goto loc_00321E8B;
loc_0032253F:
    if ((((uint8_t)(v_stack_p558)) & (4)) == 0) goto loc_00321AE4;
    goto loc_00322451;
loc_0032254D:
    goto loc_003220C2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00321750&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
