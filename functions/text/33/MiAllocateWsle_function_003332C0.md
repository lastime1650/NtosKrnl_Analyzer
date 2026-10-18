# MiAllocateWsle

- RVA: `0x003332C0`–`0x00333F5C` (길이 `3,228` bytes)
- VA: `0x00000001403332C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076720`
- 디코드: `667`개 명령, `3,228/3,228` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **31**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **15**

### Outgoing calls
- `0x00333687` → [MiAddWorkingSetEntries](../27/MiAddWorkingSetEntries_function_0027DC00.md) (function, `0x0027DC00`)
- `0x00333722` → [MiGetPagePrivilege](../28/MiGetPagePrivilege_function_00285420.md) (function, `0x00285420`)
- `0x0033378E` → [VslSetPrivilegedPte](../40/VslSetPrivilegedPte_function_00407D0C.md) (function, `0x00407D0C`)
- `0x003337C4` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00333840` → [MiGetPagePrivilege](../28/MiGetPagePrivilege_function_00285420.md) (function, `0x00285420`)
- `0x00333859` → [MiMarkPfnVerified](../38/MiMarkPfnVerified_function_003833C4.md) (function, `0x003833C4`)
- `0x003338E0` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x00333A8A` → [MiReleaseWsSwapReservationPfn](../36/MiReleaseWsSwapReservationPfn_function_003628DC.md) (function, `0x003628DC`)
- `0x00333AD2` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x00333AE6` → [MiWriteValidPteNewProtection](../28/MiWriteValidPteNewProtection_function_00281810.md) (function, `0x00281810`)
- `0x00333B3B` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x00333BD9` → [KdpSetOwedBreakpoints](../../pagekd/B8/KdpSetOwedBreakpoints_function_00B8A7DC.md) (function, `0x00B8A7DC`)
- `0x00333C38` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00333C48` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00333C60` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00333C70` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00333C7F` → [MiSanitizeShadowPxe](../29/MiSanitizeShadowPxe_function_00294B68.md) (function, `0x00294B68`)
- `0x00333C9D` → [MiWritePteShadow](../29/MiWritePteShadow_function_00294EAC.md) (function, `0x00294EAC`)
- `0x00333CC1` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x00333CE7` → [MiGetVirtualFaultPageInfo](../46/MiGetVirtualFaultPageInfo_function_0046705C.md) (function, `0x0046705C`)
- `0x00333D45` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00333D54` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00333D70` → [MiLogAllocateWsleEvent](../4B/MiLogAllocateWsleEvent_function_004BC098.md) (function, `0x004BC098`)
- `0x00333D82` → [MiReplicatePteChange](../4F/MiReplicatePteChange_function_004F8A24.md) (function, `0x004F8A24`)
- `0x00333D8E` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x00333DF7` → [MiFillVirtualFaultInfo](../46/MiFillVirtualFaultInfo_function_00467090.md) (function, `0x00467090`)
- `0x00333E65` → [MiCompleteSecureProcessFault](../46/MiCompleteSecureProcessFault_function_0046710C.md) (function, `0x0046710C`)
- `0x00333EC4` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00333F39` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x00333F45` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x00333F52` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)

### Direct callers
- [MiResolveProtoCombine](../22/MiResolveProtoCombine_function_0022CD00.md) at `0x0022CEB7`
- [MiResolveTransitionFault](../28/MiResolveTransitionFault_function_00282940.md) at `0x0028315A`
- [MiMakeSystemCachePteValid](../2A/MiMakeSystemCachePteValid_function_002A35D8.md) at `0x002A373C`
- [MiCompleteRestrictedImageFault](../2C/MiCompleteRestrictedImageFault_function_002C60D4.md) at `0x002C62BA`
- [MiCompletePrivateZeroFault](MiCompletePrivateZeroFault_function_00330CC0.md) at `0x00331202`
- [MiCompleteProtoPteFault](../34/MiCompleteProtoPteFault_function_00345710.md) at `0x00345BAC`
- [sub_003475D9](../34/Unknown_function_003475D9.md) at `0x0034770A`
- [MiIssueHardFault](../38/MiIssueHardFault_function_00380074.md) at `0x0038044A`
- [MiBuildForkPageTable](../4A/MiBuildForkPageTable_function_004ACF5C.md) at `0x004AD244`
- [MiInitializeWorkingSetList](../4A/MiInitializeWorkingSetList_function_004AE640.md) at `0x004AE768`
- [sub_006FB3A8](../6F/Unknown_function_006FB3A8.md) at `0x006FB401`

### Static image references
- `0x003334C5` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x0033356F` → RVA `0x00E0AA1C` (`.data`; read)
- `0x003336A6` → RVA `0x00E388C0` (`.data`; read/write)
- `0x003336AD` → RVA `0x00E37518` (`.data`; read)
- `0x003336C8` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x0033387E` → RVA `0x00E2DCE0` (`.data`; read)
- `0x003338AC` → RVA `0x00E35C00` (`.data`; read)
- `0x00333903` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x00333AA0` → RVA `0x00E30088` (`.data`; read)
- `0x00333BC9` → RVA `0x00F55BC0` (`.data`; read)
- `0x00333C2A` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00333CB7` → RVA `0x00E374C0` (`.data`; read)
- `0x00333E90` → RVA `0x00E2D9A8` (`.data`; read)
- `0x00333E9C` → RVA `0x00E2D9B0` (`.data`; read)
- `0x00333F24` → RVA `0x00E37518` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00333BD9` → [KdpSetOwedBreakpoints](../../pagekd/B8/KdpSetOwedBreakpoints_function_00B8A7DC.md) (`.text` → `PAGEKD`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003332C0  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
003332C5  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
003332CA  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
003332CF  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
003332D4  53                              push rbx
003332D5  56                              push rsi
003332D6  57                              push rdi
003332D7  41 54                           push r12
003332D9  41 55                           push r13
003332DB  41 56                           push r14
003332DD  41 57                           push r15
003332DF  48 81 EC 80 00 00 00            sub rsp, 0x80
003332E6  4C 8B EA                        mov r13, rdx
003332E9  0F 57 C0                        xorps xmm0, xmm0
003332EC  33 D2                           xor edx, edx
003332EE  49 C1 E5 19                     shl r13, 0x19
003332F2  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
003332F7  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
00333301  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
00333306  48 8B C2                        mov rax, rdx
00333309  8B B1 B8 00 00 00               mov esi, dword ptr [rcx + 0xb8]
0033330F  48 C1 E0 19                     shl rax, 0x19
00333313  4C 2B E8                        sub r13, rax
00333316  C7 44 24 3C 00 00 00 00         mov dword ptr [rsp + 0x3c], 0
0033331E  49 C1 FD 10                     sar r13, 0x10
00333322  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
00333326  48 8B C2                        mov rax, rdx
00333329  48 B9 FF FF FF FF FF F6 FF FF   movabs rcx, 0xfffff6ffffffffff
00333333  41 BA 01 00 00 00               mov r10d, 1
00333339  4C 3B E8                        cmp r13, rax
0033333C  0F 83 0A 08 00 00               jae 0x140333b4c
00333342  4D 8B E2                        mov r12, r10
00333345  44 89 54 24 3C                  mov dword ptr [rsp + 0x3c], r10d
0033334A  44 8B B4 24 E8 00 00 00         mov r14d, dword ptr [rsp + 0xe8]
00333352  45 84 F2                        test r10b, r14b
00333355  0F 85 0D 07 00 00               jne 0x140333a68
0033335B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00333364  32 D2                           xor dl, dl
00333366  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
0033336A  8B 81 A8 05 00 00               mov eax, dword ptr [rcx + 0x5a8]
00333370  0F BA E0 08                     bt eax, 8
00333374  0F 83 76 06 00 00               jae 0x1403339f0
0033337A  C1 E8 09                        shr eax, 9
0033337D  83 E0 07                        and eax, 7
00333380  41 B8 05 00 00 00               mov r8d, 5
00333386  8D 3C C5 00 00 00 00            lea edi, [rax*8]
0033338D  4D 85 E4                        test r12, r12
00333390  0F 84 34 04 00 00               je 0x1403337ca
00333396  41 F6 C6 02                     test r14b, 2
0033339A  0F 85 6F 08 00 00               jne 0x140333c0f
003333A0  41 3B C0                        cmp eax, r8d
003333A3  0F 82 B8 06 00 00               jb 0x140333a61
003333A9  41 F6 C6 08                     test r14b, 8
003333AD  0F 85 63 08 00 00               jne 0x140333c16
003333B3  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
003333BB  A8 01                           test al, 1
003333BD  74 0D                           je 0x1403333cc
003333BF  A8 20                           test al, 0x20
003333C1  0F B6 D2                        movzx edx, dl
003333C4  41 0F 44 D2                     cmove edx, r10d
003333C8  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
003333CC  41 80 E1 07                     and r9b, 7
003333D0  41 C0 E1 04                     shl r9b, 4
003333D4  44 0A CA                        or r9b, dl
003333D7  44 89 8C 24 D8 00 00 00         mov dword ptr [rsp + 0xd8], r9d
003333DF  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
003333E7  49 BA AB AA AA AA AA AA AA AA   movabs r10, 0xaaaaaaaaaaaaaaab
003333F1  49 B9 00 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000000
003333FB  8B 40 20                        mov eax, dword ptr [rax + 0x20]
003333FE  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00333406  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0033340A  8B 51 20                        mov edx, dword ptr [rcx + 0x20]
0033340D  4C 8B BC 24 D0 00 00 00         mov r15, qword ptr [rsp + 0xd0]
00333415  C1 EA 18                        shr edx, 0x18
00333418  F6 C2 08                        test dl, 8
0033341B  0F 85 51 04 00 00               jne 0x140333872
00333421  44 0F B6 44 24 37               movzx r8d, byte ptr [rsp + 0x37]
00333427  41 83 E0 07                     and r8d, 7
0033342B  8B DF                           mov ebx, edi
0033342D  C1 EB 03                        shr ebx, 3
00333430  44 3B C3                        cmp r8d, ebx
00333433  73 59                           jae 0x14033348e
00333435  45 33 F6                        xor r14d, r14d
00333438  F0 49 0F BA 6F 18 3F            lock bts qword ptr [r15 + 0x18], 0x3f
0033343F  0F 82 BB 04 00 00               jb 0x140333900
00333445  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
0033344D  48 BA FF FF FF FF FF FF FF 7F   movabs rdx, 0x7fffffffffffffff
00333457  8B 48 20                        mov ecx, dword ptr [rax + 0x20]
0033345A  89 4C 24 34                     mov dword ptr [rsp + 0x34], ecx
0033345E  C1 E9 18                        shr ecx, 0x18
00333461  80 E1 F8                        and cl, 0xf8
00333464  0A CB                           or cl, bl
00333466  88 4C 24 37                     mov byte ptr [rsp + 0x37], cl
0033346A  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00333472  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
00333476  89 41 20                        mov dword ptr [rcx + 0x20], eax
00333479  F0 48 21 51 18                  lock and qword ptr [rcx + 0x18], rdx
0033347E  4C 8B BC 24 D0 00 00 00         mov r15, qword ptr [rsp + 0xd0]
00333486  44 8B B4 24 E8 00 00 00         mov r14d, dword ptr [rsp + 0xe8]
0033348E  49 8B 07                        mov rax, qword ptr [r15]
00333491  A8 01                           test al, 1
00333493  0F 84 D1 04 00 00               je 0x14033396a
00333499  4C 8B 84 24 E0 00 00 00         mov r8, qword ptr [rsp + 0xe0]
003334A1  41 F6 C0 01                     test r8b, 1
003334A5  0F 84 77 01 00 00               je 0x140333622
003334AB  40 0F B6 DE                     movzx ebx, sil
003334AF  48 BA 00 00 00 00 00 00 00 80   movabs rdx, 0x8000000000000000
003334B9  80 E3 0F                        and bl, 0xf
003334BC  80 FB 01                        cmp bl, 1
003334BF  0F 84 FE 04 00 00               je 0x1403339c3
003334C5  48 8B 05 BC 35 C9 00            mov rax, qword ptr [rip + 0xc935bc]
003334CC  48 0F BA E0 0F                  bt rax, 0xf
003334D1  0F 82 10 03 00 00               jb 0x1403337e7
003334D7  48 F7 05 A6 35 C9 00 00 40 00 00  test qword ptr [rip + 0xc935a6], 0x4000
003334E2  0F 85 06 02 00 00               jne 0x1403336ee
003334E8  4C 8B 94 24 F0 00 00 00         mov r10, qword ptr [rsp + 0xf0]
003334F0  4D 85 D2                        test r10, r10
003334F3  0F 85 E8 07 00 00               jne 0x140333ce1
003334F9  8B 94 24 D8 00 00 00            mov edx, dword ptr [rsp + 0xd8]
00333500  48 C7 44 24 40 00 00 00 00      mov qword ptr [rsp + 0x40], 0
00333509  4D 85 E4                        test r12, r12
0033350C  0F 85 0F 04 00 00               jne 0x140333921
00333512  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
0033351C  84 DB                           test bl, bl
0033351E  0F 85 BB 04 00 00               jne 0x1403339df
00333524  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0033352D  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00333534  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
00333539  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
00333541  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00333546  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
0033354E  48 C1 E8 0C                     shr rax, 0xc
00333552  48 23 C2                        and rax, rdx
00333555  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0033355A  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0033355F  65 4C 8B 3C 25 20 00 00 00      mov r15, qword ptr gs:[0x20]
00333568  49 89 87 08 9C 00 00            mov qword ptr [r15 + 0x9c08], rax
0033356F  80 3D A6 74 AD 00 00            cmp byte ptr [rip + 0xad74a6], 0
00333576  0F 84 4D 06 00 00               je 0x140333bc9
0033357C  49 B8 00 D0 BE 7D FB F6 FF FF   movabs r8, 0xfffff6fb7dbed000
00333586  49 8B C0                        mov rax, r8
00333589  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
00333591  48 3B D0                        cmp rdx, rax
00333594  0F 83 0A 06 00 00               jae 0x140333ba4
0033359A  48 8B 9C 24 E0 00 00 00         mov rbx, qword ptr [rsp + 0xe0]
003335A2  33 C9                           xor ecx, ecx
003335A4  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
003335A9  89 8C 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ecx
003335B0  49 8B C0                        mov rax, r8
003335B3  48 3B D0                        cmp rdx, rax
003335B6  72 20                           jb 0x1403335d8
003335B8  48 B8 F8 D7 BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbed7f8
003335C2  48 39 84 24 C8 00 00 00         cmp qword ptr [rsp + 0xc8], rax
003335CA  0F 86 AA 06 00 00               jbe 0x140333c7a
003335D0  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
003335D8  48 0F BA 25 A7 34 C9 00 24      bt qword ptr [rip + 0xc934a7], 0x24
003335E1  0F 82 17 05 00 00               jb 0x140333afe
003335E7  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
003335EF  48 89 18                        mov qword ptr [rax], rbx
003335F2  85 C9                           test ecx, ecx
003335F4  0F 85 9D 06 00 00               jne 0x140333c97
003335FA  40 F6 C7 01                     test dil, 1
003335FE  0F 85 76 07 00 00               jne 0x140333d7a
00333604  4D 85 FF                        test r15, r15
00333607  74 0B                           je 0x140333614
00333609  49 C7 87 08 9C 00 00 00 00 00 00  mov qword ptr [r15 + 0x9c08], 0
00333614  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00333619  48 85 DB                        test rbx, rbx
0033361C  0F 85 86 07 00 00               jne 0x140333da8
00333622  4D 85 E4                        test r12, r12
00333625  74 0A                           je 0x140333631
00333627  40 F6 C7 02                     test dil, 2
0033362B  0F 84 67 07 00 00               je 0x140333d98
00333631  41 F6 C6 02                     test r14b, 2
00333635  75 57                           jne 0x14033368e
00333637  41 F6 C6 04                     test r14b, 4
0033363B  0F 85 82 00 00 00               jne 0x1403336c3
00333641  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00333649  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
0033364D  48 85 C0                        test rax, rax
00333650  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
00333654  78 03                           js 0x140333659
00333656  83 C8 02                        or eax, 2
00333659  4D 85 E4                        test r12, r12
0033365C  0F 84 6E 03 00 00               je 0x1403339d0
00333662  83 C8 04                        or eax, 4
00333665  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
0033366D  44 8B C8                        mov r9d, eax
00333670  41 83 C9 08                     or r9d, 8
00333674  BB 01 00 00 00                  mov ebx, 1
00333679  41 F6 C6 20                     test r14b, 0x20
0033367D  44 8B C3                        mov r8d, ebx
00333680  49 8B D5                        mov rdx, r13
00333683  44 0F 44 C8                     cmove r9d, eax
00333687  E8 74 A5 F4 FF                  call 0x14027dc00
0033368C  EB 3A                           jmp 0x1403336c8
0033368E  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
00333696  F0 FF 41 04                     lock inc dword ptr [rcx + 4]
0033369A  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
003336A0  24 0F                           and al, 0xf
003336A2  3C 01                           cmp al, 1
003336A4  75 07                           jne 0x1403336ad
003336A6  F0 FF 05 13 52 B0 00            lock inc dword ptr [rip + 0xb05213]
003336AD  8B 05 65 3E B0 00               mov eax, dword ptr [rip + 0xb03e65]
003336B3  85 C0                           test eax, eax
003336B5  0F 84 52 08 00 00               je 0x140333f0d
003336BB  65 FF 04 25 90 2E 00 00         inc dword ptr gs:[0x2e90]
003336C3  BB 01 00 00 00                  mov ebx, 1
003336C8  F7 05 32 34 C9 00 01 00 00 08   test dword ptr [rip + 0xc93432], 0x8000001
003336D2  0F 85 86 06 00 00               jne 0x140333d5e
003336D8  8B C3                           mov eax, ebx
003336DA  48 81 C4 80 00 00 00            add rsp, 0x80
003336E1  41 5F                           pop r15
003336E3  41 5E                           pop r14
003336E5  41 5D                           pop r13
003336E7  41 5C                           pop r12
003336E9  5F                              pop rdi
003336EA  5E                              pop rsi
003336EB  5B                              pop rbx
003336EC  C3                              ret
003336ED  CC                              int3
003336EE  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
003336F6  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
003336FA  48 C1 E8 3C                     shr rax, 0x3c
003336FE  24 07                           and al, 7
00333700  3C 03                           cmp al, 3
00333702  0F 85 E0 FD FF FF               jne 0x1403334e8
00333708  3A D8                           cmp bl, al
0033370A  0F 85 D8 FD FF FF               jne 0x1403334e8
00333710  0F 57 C0                        xorps xmm0, xmm0
00333713  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00333718  BA 02 00 00 00                  mov edx, 2
0033371D  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
00333722  E8 F9 1C F5 FF                  call 0x140285420
00333727  85 C0                           test eax, eax
00333729  0F 84 B9 FD FF FF               je 0x1403334e8
0033372F  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00333737  A8 20                           test al, 0x20
00333739  75 1E                           jne 0x140333759
0033373B  48 0F BA 25 44 33 C9 00 24      bt qword ptr [rip + 0xc93344], 0x24
00333744  73 13                           jae 0x140333759
00333746  F6 44 24 41 08                  test byte ptr [rsp + 0x41], 8
0033374B  74 0C                           je 0x140333759
0033374D  48 83 C8 20                     or rax, 0x20
00333751  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
00333759  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
00333763  48 8B C0                        mov rax, rax
00333766  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
0033376E  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00333773  48 2B C8                        sub rcx, rax
00333776  45 33 C9                        xor r9d, r9d
00333779  48 C1 F9 04                     sar rcx, 4
0033377D  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00333787  48 0F AF C8                     imul rcx, rax
0033378B  49 8B D5                        mov rdx, r13
0033378E  E8 79 45 0D 00                  call 0x140407d0c
00333793  3D 35 00 00 80                  cmp eax, 0x80000035
00333798  0F 84 F2 06 00 00               je 0x140333e90
0033379E  85 C0                           test eax, eax
003337A0  0F 89 42 FD FF FF               jns 0x1403334e8
003337A6  4C 8B 84 24 D0 00 00 00         mov r8, qword ptr [rsp + 0xd0]
003337AE  BA 10 15 05 00                  mov edx, 0x51510
003337B3  4C 63 C8                        movsxd r9, eax
003337B6  B9 1A 00 00 00                  mov ecx, 0x1a
003337BB  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
003337C4  E8 97 9E 1C 00                  call 0x1404fd660
003337C9  CC                              int3
003337CA  41 3B C0                        cmp eax, r8d
003337CD  C6 84 24 D8 00 00 00 00         mov byte ptr [rsp + 0xd8], 0
003337D5  41 8B F8                        mov edi, r8d
003337D8  0F 47 F8                        cmova edi, eax
003337DB  8D 3C FD 00 00 00 00            lea edi, [rdi*8]
003337E2  E9 F8 FB FF FF                  jmp 0x1403333df
003337E7  48 B9 00 00 00 00 80 F6 FF FF   movabs rcx, 0xfffff68000000000
003337F1  48 8B C9                        mov rcx, rcx
003337F4  4C 3B E9                        cmp r13, rcx
003337F7  0F 83 26 02 00 00               jae 0x140333a23
003337FD  48 85 94 24 E0 00 00 00         test qword ptr [rsp + 0xe0], rdx
00333805  0F 85 CC FC FF FF               jne 0x1403334d7
0033380B  48 0F BA E0 11                  bt rax, 0x11
00333810  0F 83 C1 FC FF FF               jae 0x1403334d7
00333816  4C 8B B4 24 D0 00 00 00         mov r14, qword ptr [rsp + 0xd0]
0033381E  45 33 FF                        xor r15d, r15d
00333821  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
00333828  0F 82 C2 06 00 00               jb 0x140333ef0
0033382E  4C 8B BC 24 D0 00 00 00         mov r15, qword ptr [rsp + 0xd0]
00333836  45 33 C0                        xor r8d, r8d
00333839  49 8B CF                        mov rcx, r15
0033383C  41 8D 50 01                     lea edx, [r8 + 1]
00333840  E8 DB 1B F5 FF                  call 0x140285420
00333845  44 8B B4 24 E8 00 00 00         mov r14d, dword ptr [rsp + 0xe8]
0033384D  85 C0                           test eax, eax
0033384F  75 0D                           jne 0x14033385e
00333851  BA 07 00 00 00                  mov edx, 7
00333856  49 8B CF                        mov rcx, r15
00333859  E8 66 FB 04 00                  call 0x1403833c4
0033385E  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
00333868  F0 49 21 47 18                  lock and qword ptr [r15 + 0x18], rax
0033386D  E9 65 FC FF FF                  jmp 0x1403334d7
00333872  49 8B C9                        mov rcx, r9
00333875  4C 3B F9                        cmp r15, rcx
00333878  0F 82 AD FB FF FF               jb 0x14033342b
0033387E  48 8B 0D 5B A4 AF 00            mov rcx, qword ptr [rip + 0xafa45b]
00333885  48 8D 14 49                     lea rdx, [rcx + rcx*2]
00333889  48 C1 E2 04                     shl rdx, 4
0033388D  48 B9 30 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000030
00333897  48 03 D1                        add rdx, rcx
0033389A  4C 3B FA                        cmp r15, rdx
0033389D  0F 83 88 FB FF FF               jae 0x14033342b
003338A3  49 8B C9                        mov rcx, r9
003338A6  49 8B D7                        mov rdx, r15
003338A9  48 2B D1                        sub rdx, rcx
003338AC  48 8B 0D 4D 23 B0 00            mov rcx, qword ptr [rip + 0xb0234d]
003338B3  48 C1 FA 04                     sar rdx, 4
003338B7  49 0F AF D2                     imul rdx, r10
003338BB  48 3B D1                        cmp rdx, rcx
003338BE  72 10                           jb 0x1403338d0
003338C0  48 81 C1 00 08 00 00            add rcx, 0x800
003338C7  48 3B D1                        cmp rdx, rcx
003338CA  0F 82 5B FB FF FF               jb 0x14033342b
003338D0  C1 E8 10                        shr eax, 0x10
003338D3  24 07                           and al, 7
003338D5  3C 06                           cmp al, 6
003338D7  0F 84 44 FB FF FF               je 0x140333421
003338DD  49 8B CF                        mov rcx, r15
003338E0  E8 EB A9 F5 FF                  call 0x14028e2d0
003338E5  83 F8 09                        cmp eax, 9
003338E8  0F 84 3D FB FF FF               je 0x14033342b
003338EE  E9 2E FB FF FF                  jmp 0x140333421
003338F3  0F 1F 40 00                     nop dword ptr [rax]
003338F7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
00333900  41 FF C6                        inc r14d
00333903  44 85 35 A2 19 C9 00            test dword ptr [rip + 0xc919a2], r14d
0033390A  0F 84 1A 03 00 00               je 0x140333c2a
00333910  F3 90                           pause
00333912  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
00333916  48 85 C0                        test rax, rax
00333919  0F 89 19 FB FF FF               jns 0x140333438
0033391F  EB DF                           jmp 0x140333900
00333921  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
00333929  49 B8 FF FF FF FF FF FF FF F0   movabs r8, 0xf0ffffffffffffff
00333933  49 23 C8                        and rcx, r8
00333936  0F B6 C2                        movzx eax, dl
00333939  48 C1 E0 38                     shl rax, 0x38
0033393D  48 0B C1                        or rax, rcx
00333940  0F B6 CA                        movzx ecx, dl
00333943  48 C1 E1 38                     shl rcx, 0x38
00333947  48 BA FF FF FF FF FF FF FF 8F   movabs rdx, 0x8fffffffffffffff
00333951  48 33 C1                        xor rax, rcx
00333954  48 23 C2                        and rax, rdx
00333957  48 33 C1                        xor rax, rcx
0033395A  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
00333962  83 CF 02                        or edi, 2
00333965  E9 A8 FB FF FF                  jmp 0x140333512
0033396A  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
00333972  45 33 FF                        xor r15d, r15d
00333975  F0 48 0F BA 6B 18 3F            lock bts qword ptr [rbx + 0x18], 0x3f
0033397C  0F 82 BE 00 00 00               jb 0x140333a40
00333982  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
0033398A  48 8B 00                        mov rax, qword ptr [rax]
0033398D  A8 01                           test al, 1
0033398F  0F 85 88 02 00 00               jne 0x140333c1d
00333995  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
0033399D  48 8B 00                        mov rax, qword ptr [rax]
003339A0  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
003339A8  48 83 C8 01                     or rax, 1
003339AC  48 89 01                        mov qword ptr [rcx], rax
003339AF  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003339B9  F0 48 21 41 18                  lock and qword ptr [rcx + 0x18], rax
003339BE  E9 D6 FA FF FF                  jmp 0x140333499
003339C3  48 09 94 24 E0 00 00 00         or qword ptr [rsp + 0xe0], rdx
003339CB  E9 07 FB FF FF                  jmp 0x1403334d7
003339D0  40 F6 C6 0F                     test sil, 0xf
003339D4  0F 85 8B FC FF FF               jne 0x140333665
003339DA  E9 83 FC FF FF                  jmp 0x140333662
003339DF  80 FB 03                        cmp bl, 3
003339E2  0F 84 51 FB FF FF               je 0x140333539
003339E8  45 33 FF                        xor r15d, r15d
003339EB  E9 8C FB FF FF                  jmp 0x14033357c
003339F0  8B 81 A0 05 00 00               mov eax, dword ptr [rcx + 0x5a0]
003339F6  48 8B 89 20 02 00 00            mov rcx, qword ptr [rcx + 0x220]
003339FD  C1 E8 0C                        shr eax, 0xc
00333A00  83 E0 07                        and eax, 7
00333A03  48 8B 89 A0 02 00 00            mov rcx, qword ptr [rcx + 0x2a0]
00333A0A  48 85 C9                        test rcx, rcx
00333A0D  0F 84 6A F9 FF FF               je 0x14033337d
00333A13  8B 89 44 04 00 00               mov ecx, dword ptr [rcx + 0x444]
00333A19  3B C1                           cmp eax, ecx
00333A1B  0F 43 C1                        cmovae eax, ecx
00333A1E  E9 5A F9 FF FF                  jmp 0x14033337d
00333A23  48 B9 FF FF FF FF FF F6 FF FF   movabs rcx, 0xfffff6ffffffffff
00333A2D  48 8B C9                        mov rcx, rcx
00333A30  4C 3B E9                        cmp r13, rcx
00333A33  0F 86 9E FA FF FF               jbe 0x1403334d7
00333A39  E9 BF FD FF FF                  jmp 0x1403337fd
00333A3E  66 90                           nop
00333A40  41 FF C7                        inc r15d
00333A43  44 85 3D 62 18 C9 00            test dword ptr [rip + 0xc91862], r15d
00333A4A  0F 84 02 02 00 00               je 0x140333c52
00333A50  F3 90                           pause
00333A52  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00333A56  48 85 C0                        test rax, rax
00333A59  0F 89 16 FF FF FF               jns 0x140333975
00333A5F  EB DF                           jmp 0x140333a40
00333A61  B2 07                           mov dl, 7
00333A63  E9 60 F9 FF FF                  jmp 0x1403333c8
00333A68  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
00333A70  33 FF                           xor edi, edi
00333A72  F0 48 0F BA 6B 18 3F            lock bts qword ptr [rbx + 0x18], 0x3f
00333A79  0F 82 71 01 00 00               jb 0x140333bf0
00333A7F  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
00333A87  48 8B CB                        mov rcx, rbx
00333A8A  E8 4D EE 02 00                  call 0x1403628dc
00333A8F  48 8B D0                        mov rdx, rax
00333A92  49 B8 FF FF FF FF FF FF FF 7F   movabs r8, 0x7fffffffffffffff
00333A9C  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
00333AA0  48 8B 0D E1 C5 AF 00            mov rcx, qword ptr [rip + 0xafc5e1]
00333AA7  48 C1 E8 2B                     shr rax, 0x2b
00333AAB  25 FF 03 00 00                  and eax, 0x3ff
00333AB0  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
00333AB4  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00333ABC  F0 4C 21 40 18                  lock and qword ptr [rax + 0x18], r8
00333AC1  48 85 D2                        test rdx, rdx
00333AC4  0F 85 82 04 00 00               jne 0x140333f4c
00333ACA  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
00333AD2  E8 C9 ED F4 FF                  call 0x1402828a0
00333AD7  48 83 E0 DF                     and rax, 0xffffffffffffffdf
00333ADB  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
00333AE3  48 8B D0                        mov rdx, rax
00333AE6  E8 25 DD F4 FF                  call 0x140281810
00333AEB  44 8B 8C 24 D8 00 00 00         mov r9d, dword ptr [rsp + 0xd8]
00333AF3  41 BA 01 00 00 00               mov r10d, 1
00333AF9  E9 5D F8 FF FF                  jmp 0x14033335b
00333AFE  F6 C3 20                        test bl, 0x20
00333B01  0F 85 E0 FA FF FF               jne 0x1403335e7
00333B07  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00333B11  48 8B C0                        mov rax, rax
00333B14  49 B8 00 00 00 00 40 00 00 00   movabs r8, 0x4000000000
00333B1E  49 03 C0                        add rax, r8
00333B21  48 3B D0                        cmp rdx, rax
00333B24  0F 82 BD FA FF FF               jb 0x1403335e7
00333B2A  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
00333B32  41 B8 80 00 00 00               mov r8d, 0x80
00333B38  48 8B D3                        mov rdx, rbx
00333B3B  E8 40 F2 F5 FF                  call 0x140292d80
00333B40  8B 8C 24 E8 00 00 00            mov ecx, dword ptr [rsp + 0xe8]
00333B47  E9 9B FA FF FF                  jmp 0x1403335e7
00333B4C  48 8B C1                        mov rax, rcx
00333B4F  4C 3B E8                        cmp r13, rax
00333B52  0F 87 EA F7 FF FF               ja 0x140333342
00333B58  45 33 E4                        xor r12d, r12d
00333B5B  40 F6 C6 0F                     test sil, 0xf
00333B5F  0F 85 E5 F7 FF FF               jne 0x14033334a
00333B65  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00333B6D  48 8B 00                        mov rax, qword ptr [rax]
00333B70  48 C1 E8 2A                     shr rax, 0x2a
00333B74  A8 07                           test al, 7
00333B76  0F 84 CE F7 FF FF               je 0x14033334a
00333B7C  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00333B84  48 B9 FF FF FF FF FF E3 FF FF   movabs rcx, 0xffffe3ffffffffff
00333B8E  48 8B 00                        mov rax, qword ptr [rax]
00333B91  48 23 C1                        and rax, rcx
00333B94  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00333B9C  48 89 01                        mov qword ptr [rcx], rax
00333B9F  E9 A6 F7 FF FF                  jmp 0x14033334a
00333BA4  48 B8 FF DF BE 7D FB F6 FF FF   movabs rax, 0xfffff6fb7dbedfff
00333BAE  48 39 84 24 C8 00 00 00         cmp qword ptr [rsp + 0xc8], rax
00333BB6  0F 86 F3 00 00 00               jbe 0x140333caf
00333BBC  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
00333BC4  E9 D1 F9 FF FF                  jmp 0x14033359a
00333BC9  80 3D F0 1F C2 00 00            cmp byte ptr [rip + 0xc21ff0], 0
00333BD0  0F 84 A6 F9 FF FF               je 0x14033357c
00333BD6  49 8B CD                        mov rcx, r13
00333BD9  E8 FE 6B 85 00                  call 0x140b8a7dc
00333BDE  E9 99 F9 FF FF                  jmp 0x14033357c
00333BE3  0F 1F 40 00                     nop dword ptr [rax]
00333BE7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
00333BF0  FF C7                           inc edi
00333BF2  85 3D B4 16 C9 00               test dword ptr [rip + 0xc916b4], edi
00333BF8  0F 84 39 01 00 00               je 0x140333d37
00333BFE  F3 90                           pause
00333C00  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00333C04  48 85 C0                        test rax, rax
00333C07  0F 89 65 FE FF FF               jns 0x140333a72
00333C0D  EB E1                           jmp 0x140333bf0
00333C0F  B2 09                           mov dl, 9
00333C11  E9 B2 F7 FF FF                  jmp 0x1403333c8
00333C16  B2 06                           mov dl, 6
00333C18  E9 AB F7 FF FF                  jmp 0x1403333c8
00333C1D  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00333C25  E9 85 FD FF FF                  jmp 0x1403339af
00333C2A  8B 05 88 2E C9 00               mov eax, dword ptr [rip + 0xc92e88]
00333C30  A8 40                           test al, 0x40
00333C32  0F 84 D8 FC FF FF               je 0x140333910
00333C38  E8 53 B8 FD FF                  call 0x14030f490
00333C3D  84 C0                           test al, al
00333C3F  0F 84 CB FC FF FF               je 0x140333910
00333C45  41 8B CE                        mov ecx, r14d
00333C48  E8 13 B8 FD FF                  call 0x14030f460
00333C4D  E9 C0 FC FF FF                  jmp 0x140333912
00333C52  8B 05 60 2E C9 00               mov eax, dword ptr [rip + 0xc92e60]
00333C58  A8 40                           test al, 0x40
00333C5A  0F 84 F0 FD FF FF               je 0x140333a50
00333C60  E8 2B B8 FD FF                  call 0x14030f490
00333C65  84 C0                           test al, al
00333C67  0F 84 E3 FD FF FF               je 0x140333a50
00333C6D  41 8B CF                        mov ecx, r15d
00333C70  E8 EB B7 FD FF                  call 0x14030f460
00333C75  E9 D8 FD FF FF                  jmp 0x140333a52
00333C7A  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00333C7F  E8 E4 0E F6 FF                  call 0x140294b68
00333C84  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
00333C89  8B C8                           mov ecx, eax
00333C8B  89 84 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], eax
00333C92  E9 39 F9 FF FF                  jmp 0x1403335d0
00333C97  48 8B D3                        mov rdx, rbx
00333C9A  48 8B C8                        mov rcx, rax
00333C9D  E8 0A 12 F6 FF                  call 0x140294eac
00333CA2  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
00333CAA  E9 4B F9 FF FF                  jmp 0x1403335fa
00333CAF  84 DB                           test bl, bl
00333CB1  0F 84 05 FF FF FF               je 0x140333bbc
00333CB7  48 8D 0D 02 38 B0 00            lea rcx, [rip + 0xb03802]
00333CBE  83 CF 01                        or edi, 1
00333CC1  E8 BA 51 F1 FF                  call 0x140248e80
00333CC6  48 8B 9C 24 E0 00 00 00         mov rbx, qword ptr [rsp + 0xe0]
00333CCE  33 C9                           xor ecx, ecx
00333CD0  89 8C 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ecx
00333CD7  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00333CDC  E9 D7 F8 FF FF                  jmp 0x1403335b8
00333CE1  49 8B D5                        mov rdx, r13
00333CE4  49 8B CA                        mov rcx, r10
00333CE7  E8 70 33 13 00                  call 0x14046705c
00333CEC  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00333CF1  48 85 C0                        test rax, rax
00333CF4  0F 84 FF F7 FF FF               je 0x1403334f9
00333CFA  41 8B 4A 38                     mov ecx, dword ptr [r10 + 0x38]
00333CFE  F6 C1 20                        test cl, 0x20
00333D01  0F 85 FA 00 00 00               jne 0x140333e01
00333D07  41 8B 42 38                     mov eax, dword ptr [r10 + 0x38]
00333D0B  8B 94 24 D8 00 00 00            mov edx, dword ptr [rsp + 0xd8]
00333D12  A8 10                           test al, 0x10
00333D14  0F 84 EF F7 FF FF               je 0x140333509
00333D1A  80 7C 24 30 06                  cmp byte ptr [rsp + 0x30], 6
00333D1F  0F 83 E4 F7 FF FF               jae 0x140333509
00333D25  80 E2 F6                        and dl, 0xf6
00333D28  80 CA 06                        or dl, 6
00333D2B  89 94 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], edx
00333D32  E9 D2 F7 FF FF                  jmp 0x140333509
00333D37  8B 05 7B 2D C9 00               mov eax, dword ptr [rip + 0xc92d7b]
00333D3D  A8 40                           test al, 0x40
00333D3F  0F 84 B9 FE FF FF               je 0x140333bfe
00333D45  E8 46 B7 FD FF                  call 0x14030f490
00333D4A  84 C0                           test al, al
00333D4C  0F 84 AC FE FF FF               je 0x140333bfe
00333D52  8B CF                           mov ecx, edi
00333D54  E8 07 B7 FD FF                  call 0x14030f460
00333D59  E9 A2 FE FF FF                  jmp 0x140333c00
00333D5E  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00333D66  4D 8B C5                        mov r8, r13
00333D69  40 0F B6 D6                     movzx edx, sil
00333D6D  83 E2 0F                        and edx, 0xf
00333D70  E8 23 83 18 00                  call 0x1404bc098
00333D75  E9 5E F9 FF FF                  jmp 0x1403336d8
00333D7A  BA 01 00 00 00                  mov edx, 1
00333D7F  48 8B C8                        mov rcx, rax
00333D82  E8 9D 4C 1C 00                  call 0x1404f8a24
00333D87  48 8D 0D 32 37 B0 00            lea rcx, [rip + 0xb03732]
00333D8E  E8 4D 5A F1 FF                  call 0x1402497e0
00333D93  E9 6C F8 FF FF                  jmp 0x140333604
00333D98  8B 84 24 D8 00 00 00            mov eax, dword ptr [rsp + 0xd8]
00333D9F  41 88 04 24                     mov byte ptr [r12], al
00333DA3  E9 89 F8 FF FF                  jmp 0x140333631
00333DA8  4C 8B 84 24 F0 00 00 00         mov r8, qword ptr [rsp + 0xf0]
00333DB0  41 8B 40 38                     mov eax, dword ptr [r8 + 0x38]
00333DB4  A8 01                           test al, 1
00333DB6  0F 85 C1 00 00 00               jne 0x140333e7d
00333DBC  A8 02                           test al, 2
00333DBE  0F 85 06 01 00 00               jne 0x140333eca
00333DC4  83 CF 04                        or edi, 4
00333DC7  44 8B FF                        mov r15d, edi
00333DCA  A8 20                           test al, 0x20
00333DCC  75 79                           jne 0x140333e47
00333DCE  40 F6 C7 04                     test dil, 4
00333DD2  0F 84 4A F8 FF FF               je 0x140333622
00333DD8  4C 8B 84 24 E0 00 00 00         mov r8, qword ptr [rsp + 0xe0]
00333DE0  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
00333DEA  49 8B D0                        mov rdx, r8
00333DED  48 8B CB                        mov rcx, rbx
00333DF0  48 C1 EA 0C                     shr rdx, 0xc
00333DF4  48 23 D0                        and rdx, rax
00333DF7  E8 94 32 13 00                  call 0x140467090
00333DFC  E9 21 F8 FF FF                  jmp 0x140333622
00333E01  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00333E09  48 8B 40 28                     mov rax, qword ptr [rax + 0x28]
00333E0D  48 0F BA E0 28                  bt rax, 0x28
00333E12  0F 82 EF FE FF FF               jb 0x140333d07
00333E18  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00333E20  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00333E24  48 85 C0                        test rax, rax
00333E27  0F 88 DA FE FF FF               js 0x140333d07
00333E2D  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00333E35  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00333E39  48 85 C0                        test rax, rax
00333E3C  0F 85 B7 F6 FF FF               jne 0x1403334f9
00333E42  E9 C0 FE FF FF                  jmp 0x140333d07
00333E47  83 E7 FB                        and edi, 0xfffffffb
00333E4A  49 83 78 30 00                  cmp qword ptr [r8 + 0x30], 0
00333E4F  0F 85 79 FF FF FF               jne 0x140333dce
00333E55  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
00333E5D  48 8D 8C 24 D0 00 00 00         lea rcx, [rsp + 0xd0]
00333E65  E8 A2 32 13 00                  call 0x14046710c
00333E6A  8B F8                           mov edi, eax
00333E6C  C1 E7 02                        shl edi, 2
00333E6F  41 33 FF                        xor edi, r15d
00333E72  83 E7 04                        and edi, 4
00333E75  41 33 FF                        xor edi, r15d
00333E78  E9 51 FF FF FF                  jmp 0x140333dce
00333E7D  F6 84 24 E0 00 00 00 42         test byte ptr [rsp + 0xe0], 0x42
00333E85  0F 85 31 FF FF FF               jne 0x140333dbc
00333E8B  E9 92 F7 FF FF                  jmp 0x140333622
00333E90  48 8B 05 11 9B AF 00            mov rax, qword ptr [rip + 0xaf9b11]
00333E97  4C 3B E8                        cmp r13, rax
00333E9A  72 10                           jb 0x140333eac
00333E9C  48 8B 05 0D 9B AF 00            mov rax, qword ptr [rip + 0xaf9b0d]
00333EA3  4C 3B E8                        cmp r13, rax
00333EA6  0F 82 3C F6 FF FF               jb 0x1403334e8
00333EAC  45 33 C9                        xor r9d, r9d
00333EAF  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
00333EB8  4D 8B C5                        mov r8, r13
00333EBB  BA 17 15 05 00                  mov edx, 0x51517
00333EC0  41 8D 49 1A                     lea ecx, [r9 + 0x1a]
00333EC4  E8 97 97 1C 00                  call 0x1404fd660
00333EC9  CC                              int3
00333ECA  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
00333ED4  48 85 8C 24 E0 00 00 00         test qword ptr [rsp + 0xe0], rcx
00333EDC  0F 84 E2 FE FF FF               je 0x140333dc4
00333EE2  E9 3B F7 FF FF                  jmp 0x140333622
00333EE7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
00333EF0  41 FF C7                        inc r15d
00333EF3  44 85 3D B2 13 C9 00            test dword ptr [rip + 0xc913b2], r15d
00333EFA  74 33                           je 0x140333f2f
00333EFC  F3 90                           pause
00333EFE  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00333F02  48 85 C0                        test rax, rax
00333F05  0F 89 16 F9 FF FF               jns 0x140333821
00333F0B  EB E3                           jmp 0x140333ef0
00333F0D  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
00333F13  24 0F                           and al, 0xf
00333F15  FE C8                           dec al
00333F17  3C 03                           cmp al, 3
00333F19  0F 87 9C F7 FF FF               ja 0x1403336bb
00333F1F  B8 01 00 00 00                  mov eax, 1
00333F24  89 05 EE 35 B0 00               mov dword ptr [rip + 0xb035ee], eax
00333F2A  E9 8C F7 FF FF                  jmp 0x1403336bb
00333F2F  8B 05 83 2B C9 00               mov eax, dword ptr [rip + 0xc92b83]
00333F35  A8 40                           test al, 0x40
00333F37  74 C3                           je 0x140333efc
00333F39  E8 52 B5 FD FF                  call 0x14030f490
00333F3E  84 C0                           test al, al
00333F40  74 BA                           je 0x140333efc
00333F42  41 8B CF                        mov ecx, r15d
00333F45  E8 16 B5 FD FF                  call 0x14030f460
00333F4A  EB B2                           jmp 0x140333efe
00333F4C  41 B8 01 00 00 00               mov r8d, 1
00333F52  E8 79 00 F5 FF                  call 0x140283fd0
00333F57  E9 6E FB FF FF                  jmp 0x140333aca
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAllocateWsle(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned __int8 a5, unsigned int a6, __int64 a7)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned __int8 v_stack_m81;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p41;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pD0;
    unsigned __int8 v_stack_pD8;
    unsigned __int64 v_stack_pE0;
    unsigned int v_stack_pE8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (128);
    a2 = 0;
    v_r13 = (a2) << (25);
    v_stack_m58 = 0;
    v_stack_m68 = v_xmm0;
    result = (0) << (25);
    v_r13 = (v_r13) - (result);
    v_stack_m7C = 0;
    v_r13 = (v_r13) >> (16);
    v_stack_m78 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 184)));
    if (v_r13 >= 0) goto loc_00333B4C;
loc_00333342:
    v_stack_m7C = 1;
loc_0033334A:
    if (((1) & ((unsigned __int8)((unsigned int)(a6)))) != 0) goto loc_00333A68;
loc_0033335B:
    a2 = 0;
    v_stack_m88 = 0;
    if (condition_is_above_or_equal) goto loc_003339F0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1448))) >> (9));
loc_0033337D:
    result = (unsigned int)((result) & (7));
    if (1 == 0) goto loc_003337CA;
    if ((((unsigned __int8)((unsigned int)(a6))) & (2)) != 0) goto loc_00333C0F;
    if (((unsigned int)(result)) < 5) goto loc_00333A61;
    if ((((unsigned __int8)((unsigned int)(a6))) & (8)) != 0) goto loc_00333C16;
    if (((a5) & (1)) == 0) goto loc_003333CC;
    a2 = 0;
    if (((a5) & (32)) == 0) { a2 = 1; }
loc_003333C8:
    v_stack_m88 = (unsigned int)(a2);
loc_003333CC:
    a4 = (unsigned __int8)((a4) & (7));
    a4 = (unsigned __int8)((a4) << (4));
    a4 = (unsigned __int8)((a4) | ((unsigned __int8)(a2)));
    v_stack_p20 = a4;
loc_003333DF:
    v_stack_m84 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18 + 32)));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p18 + 32))) >> (24));
    if ((((unsigned __int8)(a2)) & (8)) != 0) goto loc_00333872;
loc_00333421:
    a3 = (unsigned int)((v_stack_m81) & (7));
loc_0033342B:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result * 8))) >> (3));
    if (((unsigned int)(a3)) >= ((unsigned int)(v_rbx))) goto loc_0033348E;
    v_r14 = 0;
loc_00333438:
    if (condition_is_below) goto loc_00333900;
    v_stack_m84 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p18 + 32)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p18 + 32))) >> (24));
    a1 = (unsigned __int8)((a1) & (248));
    a1 = (unsigned __int8)((a1) | ((unsigned __int8)(v_rbx)));
    v_stack_m81 = (unsigned __int8)(a1);
    *(unsigned int *)(v_stack_p18 + 32) = (unsigned int)((unsigned int)(v_stack_m84));
loc_0033348E:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p18))) & (1)) == 0) goto loc_0033396A;
loc_00333499:
    if (((a5) & (1)) == 0) goto loc_00333622;
    v_rbx = (unsigned __int8)(((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184)))) & (15));
    if (((unsigned __int8)(v_rbx)) == 1) goto loc_003339C3;
    if (((unsigned __int8)(v_rbx)) < 1) goto loc_003337E7;
loc_003334D7:
    if (((*(unsigned __int64 *)(v_rip + 13186470)) & (0x4000ULL)) != 0) goto loc_003336EE;
loc_003334E8:
    if (a7 != 0) goto loc_00333CE1;
loc_003334F9:
    v_stack_m78 = 0;
loc_00333509:
    if (1 != 0) goto loc_00333921;
loc_00333512:
    if ((unsigned __int8)(v_rbx) != 0) goto loc_003339DF;
    v_stack_m68 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
loc_00333539:
    v_stack_m60 = v_stack_p10;
    result = (a5) >> (12);
    result = (result) & ((unsigned int)(v_stack_p20));
    v_stack_m58 = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 39944) = v_stack_m68;
    if ((*(unsigned __int8 *)(v_rip + 11367590)) == 0) goto loc_00333BC9;
loc_0033357C:
    if (v_stack_p10 >= a5) goto loc_00333BA4;
loc_0033359A:
    a1 = 0;
    v_stack_m70 = a5;
    v_stack_p30 = 0;
    if (v_stack_p10 < a5) goto loc_003335D8;
loc_003335B8:
    if (v_stack_p10 <= a5) goto loc_00333C7A;
loc_003335D0:
loc_003335D8:
    if (v_stack_p10 < a5) goto loc_00333AFE;
loc_003335E7:
    *(unsigned __int64 *)(v_stack_p10) = a5;
    if (0 != 0) goto loc_00333C97;
loc_003335FA:
    if ((((unsigned __int8)(result * 8)) & (1)) != 0) goto loc_00333D7A;
loc_00333604:
    if (*(unsigned __int64 *)(gs_base + (0 + 32)) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 39944) = 0;
    }
    if (v_stack_m78 != 0) goto loc_00333DA8;
loc_00333622:
    if (1 == 0) goto loc_00333631;
    if ((((unsigned __int8)(result * 8)) & (2)) == 0) goto loc_00333D98;
loc_00333631:
    if ((((unsigned __int8)((unsigned int)(a6))) & (2)) != 0) goto loc_0033368E;
    if ((((unsigned __int8)((unsigned int)(a6))) & (4)) != 0) goto loc_003336C3;
    result = (unsigned int)(v_stack_m7C);
    if (!(sign_flag)) {
        result = (unsigned int)(((unsigned int)(v_stack_m7C)) | (2));
    }
    if (1 == 0) goto loc_003339D0;
loc_00333662:
    result = (unsigned int)((result) | (4));
loc_00333665:
    a4 = (unsigned int)(((unsigned int)((unsigned int)(result))) | (8));
    if ((((unsigned __int8)((unsigned int)(a6))) & (32)) == 0) { a4 = (unsigned int)(result); }
    result = MiAddWorkingSetEntries(v_stack_p8, v_r13, 1, a4);
    goto loc_003336C8;
loc_0033368E:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_p8 + 184))) & (15));
    if (((unsigned __int8)(result)) == 1) {
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11550309))) == 0) goto loc_00333F0D;
loc_003336BB:
loc_003336C3:
loc_003336C8:
    if (((*(unsigned int *)(v_rip + 13186098)) & (0x8000001ULL)) != 0) goto loc_00333D5E;
loc_003336D8:
    v_rsp = (v_rsp) + (128);
    return 1;
loc_003336EE:
    result = (*(unsigned __int64 *)(v_stack_pD0 + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) != 3) goto loc_003334E8;
    if (1 != ((unsigned __int8)(result))) goto loc_003334E8;
    v_stack_p68 = v_xmm0;
    result = MiGetPagePrivilege(v_stack_pD0, 2, v_stack_p68, a4);
    if ((unsigned int)(result) == 0) goto loc_003334E8;
    if (((a5) & (32)) != 0) goto loc_00333759;
    if (condition_is_above_or_equal) goto loc_00333759;
    result = a5;
    if (((v_stack_p41) & (8)) != 0) {
        result = (a5) | (32);
        v_stack_pE0 = result;
    }
    a1 = (v_stack_pD0) - (result);
    a4 = 0;
    a1 = (a1) >> (4);
    a1 = (a1) * (result);
    result = VslSetPrivilegedPte(a1, v_r13, v_stack_p68, a4);
    if (((unsigned int)(result)) == 0x80000035ULL) goto loc_00333E90;
    if (!sign_flag) goto loc_003334E8;
    v_stack_p20 = 0;
    result = KeBugCheckEx(26, (unsigned int)(0x51510ULL), v_stack_pD0, (int)((unsigned int)(result)));
loc_003337CA:
    v_stack_pD8 = 0;
    v_rdi = (unsigned int)((unsigned int)(v_stack_pD0));
    if (((unsigned int)(result)) > ((unsigned int)(v_stack_pD0))) { v_rdi = (unsigned int)(result); }
    goto loc_003333DF;
loc_003337E7:
    if (v_r13 >= 26) goto loc_00333A23;
loc_003337FD:
    if (((a5) & ((unsigned int)(0x51510ULL))) != 0) goto loc_003334D7;
    if (condition_is_above_or_equal) goto loc_003334D7;
    v_r15 = 0;
loc_00333821:
    if (condition_is_below) goto loc_00333EF0;
    a3 = 0;
    result = MiGetPagePrivilege(v_stack_pD0, a3 + 1, a3, (int)((unsigned int)(result)));
    if ((unsigned int)(result) == 0) {
        a2 = 7;
        a1 = v_stack_pD0;
        result = MiMarkPfnVerified(a1, a2, a3, (int)((unsigned int)(result)));
    }
    goto loc_003334D7;
loc_00333872:
    if (v_stack_pD0 < ((int)((unsigned int)(result)))) goto loc_0033342B;
    a2 = (*(unsigned __int64 *)(v_rip + 11510875) + *(unsigned __int64 *)(v_rip + 11510875) * 2) << (4);
    a2 = (a2) + (*(unsigned __int64 *)(v_rip + 11510875));
    if (v_stack_pD0 >= a2) goto loc_0033342B;
    a2 = (v_stack_pD0) - ((int)((unsigned int)(result)));
    a2 = (a2) >> (4);
    a2 = (a2) * (a7);
    if (a2 < (*(unsigned __int64 *)(v_rip + 11543373))) goto loc_003338D0;
    a1 = (*(unsigned __int64 *)(v_rip + 11543373)) + (0x800ULL);
    if (a2 < a1) goto loc_0033342B;
loc_003338D0:
    result = (unsigned int)((result) >> (16));
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) == 6) goto loc_00333421;
    result = MiGetPfnSlabType(v_stack_pD0, a2, a3, (int)((unsigned int)(result)));
    if (((unsigned int)(result)) == 9) goto loc_0033342B;
    goto loc_00333421;
loc_00333900:
    v_r14 = (unsigned int)(((unsigned int)(a6)) + 1);
    if (((*(unsigned int *)(v_rip + 13179298)) & ((unsigned int)(v_r14))) == 0) goto loc_00333C2A;
loc_00333910:
loc_00333912:
    if (!sign_flag) goto loc_00333438;
    goto loc_00333900;
loc_00333921:
    a1 = (a5) & (0);
    result = ((unsigned __int8)(a2)) << (56);
    result = (result) | (a1);
    a1 = ((unsigned __int8)(a2)) << (56);
    result = (result) ^ (a1);
    result = (result) & (a2);
    result = (result) ^ (a1);
    v_stack_pE0 = result;
    v_rdi = (unsigned int)((v_rdi * 8) | (2));
    goto loc_00333512;
loc_0033396A:
    v_r15 = 0;
loc_00333975:
    if (condition_is_below) goto loc_00333A40;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_pD0))) & (1)) != 0) goto loc_00333C1D;
    result = (*(unsigned __int64 *)(v_stack_pD0)) | (1);
    *(unsigned __int64 *)(v_stack_pD0) = result;
loc_003339AF:
    goto loc_00333499;
loc_003339C3:
    goto loc_003334D7;
loc_003339D0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184)))) & (15)) != 0) goto loc_00333665;
    goto loc_00333662;
loc_003339DF:
    if (((unsigned __int8)(v_stack_pD0)) == 3) goto loc_00333539;
    v_r15 = 0;
    goto loc_0033357C;
loc_003339F0:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_pD0 + 1440))) >> (12));
    result = (unsigned int)((result) & (7));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pD0 + 544) + 672) == 0) goto loc_0033337D;
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pD0 + 544) + 672) + 1092))))) { result = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pD0 + 544) + 672) + 1092))); }
    goto loc_0033337D;
loc_00333A23:
    if (v_r13 <= ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pD0 + 544) + 672) + 1092)))) goto loc_003334D7;
    goto loc_003337FD;
loc_00333A40:
    v_r15 = (unsigned int)((v_r15) + 1);
    if (((*(unsigned int *)(v_rip + 13178978)) & ((unsigned int)(v_r15))) == 0) goto loc_00333C52;
loc_00333A50:
loc_00333A52:
    if (!sign_flag) goto loc_00333975;
    goto loc_00333A40;
loc_00333A61:
    goto loc_003333C8;
loc_00333A68:
    v_rdi = 0;
loc_00333A72:
    if (condition_is_below) goto loc_00333BF0;
    result = MiReleaseWsSwapReservationPfn(v_stack_pD0, 7, a3, (int)((unsigned int)(result)));
    result = (*(unsigned __int64 *)(v_stack_pD0 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (result != 0) goto loc_00333F4C;
loc_00333ACA:
    result = MI_READ_PTE_LOCK_FREE(a5, result, a3, (int)((unsigned int)(result)));
    result = (result) & (-33);
    result = MiWriteValidPteNewProtection(a5, result, a3, (int)((unsigned int)(result)));
    goto loc_0033335B;
loc_00333AFE:
    if ((((unsigned __int8)(v_stack_pD0)) & (32)) != 0) goto loc_003335E7;
    result = (result) + (0);
    if (result < result) goto loc_003335E7;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_pC8, v_stack_pD0, 128, (unsigned int)(v_stack_pD8));
    goto loc_003335E7;
loc_00333B4C:
    if (v_r13 > ((unsigned int)(a6))) goto loc_00333342;
    v_r12 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184)))) & (15)) != 0) goto loc_0033334A;
    result = (*(unsigned __int64 *)(v_stack_pD0)) >> (42);
    if ((((unsigned __int8)(result)) & (7)) == 0) goto loc_0033334A;
    result = (*(unsigned __int64 *)(v_stack_pD0)) & ((unsigned int)(a6));
    *(unsigned __int64 *)(v_stack_pD0) = result;
    goto loc_0033334A;
loc_00333BA4:
    if (v_stack_pC8 <= result) goto loc_00333CAF;
loc_00333BBC:
    goto loc_0033359A;
loc_00333BC9:
    if ((*(unsigned __int8 *)(v_rip + 12722160)) == 0) goto loc_0033357C;
    result = KdpSetOwedBreakpoints(v_r13, v_stack_pC8, 128, (unsigned int)(v_stack_pD8));
    goto loc_0033357C;
loc_00333BF0:
    v_rdi = (unsigned int)((v_rdi) + 1);
    if (((*(unsigned int *)(v_rip + 13178548)) & ((unsigned int)(v_rdi))) == 0) goto loc_00333D37;
loc_00333BFE:
loc_00333C00:
    if (!sign_flag) goto loc_00333A72;
    goto loc_00333BF0;
loc_00333C0F:
    goto loc_003333C8;
loc_00333C16:
    goto loc_003333C8;
loc_00333C1D:
    goto loc_003339AF;
loc_00333C2A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13184648)))) & (64)) == 0) goto loc_00333910;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_pD0, 6, 128, (unsigned int)(v_stack_pD8));
    if ((unsigned __int8)(result) == 0) goto loc_00333910;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r14)), 6, 128, (unsigned int)(v_stack_pD8));
    goto loc_00333912;
loc_00333C52:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13184608)))) & (64)) == 0) goto loc_00333A50;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_r14)), 6, 128, (unsigned int)(v_stack_pD8));
    if ((unsigned __int8)(result) == 0) goto loc_00333A50;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r15)), 6, 128, (unsigned int)(v_stack_pD8));
    goto loc_00333A52;
loc_00333C7A:
    result = MiSanitizeShadowPxe((unsigned int)((unsigned int)(v_r15)), v_stack_p48, 128, (unsigned int)(v_stack_pD8));
    v_stack_pE8 = (unsigned int)(result);
    goto loc_003335D0;
loc_00333C97:
    result = MiWritePteShadow(result, v_stack_p48, 128, (unsigned int)(v_stack_pD8));
    goto loc_003335FA;
loc_00333CAF:
    if ((unsigned __int8)(v_stack_p48) == 0) goto loc_00333BBC;
    v_rdi = (unsigned int)((v_rdi) | (1));
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 11548674, v_stack_p48, 128, (unsigned int)(v_stack_pD8));
    a1 = 0;
    v_stack_pE8 = 0;
    v_stack_p48 = a5;
    goto loc_003335B8;
loc_00333CE1:
    result = MiGetVirtualFaultPageInfo(1, v_r13, 128, (unsigned int)(v_stack_pD8));
    v_stack_p40 = result;
    if (result == 0) goto loc_003334F9;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(1 + 56)))) & (32)) != 0) goto loc_00333E01;
loc_00333D07:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(1 + 56)))) & (16)) == 0) goto loc_00333509;
    if (v_stack_p30 >= 6) goto loc_00333509;
    a2 = (unsigned __int8)(((unsigned int)(v_stack_pD8)) & (246));
    a2 = (unsigned __int8)((a2) | (6));
    v_stack_pD8 = (unsigned int)(a2);
    goto loc_00333509;
loc_00333D37:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13184379)))) & (64)) == 0) goto loc_00333BFE;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)(*(unsigned int *)(1 + 56)), a2, 128, (unsigned int)(v_stack_pD8));
    if ((unsigned __int8)(result) == 0) goto loc_00333BFE;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rdi)), a2, 128, (unsigned int)(v_stack_pD8));
    goto loc_00333C00;
loc_00333D5E:
    a2 = (unsigned int)(((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 184)))) & (15));
    result = MiLogAllocateWsleEvent(v_stack_pD0, a2, v_r13, (unsigned int)(v_stack_pD8));
    goto loc_003336D8;
loc_00333D7A:
    result = MiReplicatePteChange(result, 1, v_r13, (unsigned int)(v_stack_pD8));
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 11548466, 1, v_r13, (unsigned int)(v_stack_pD8));
    goto loc_00333604;
loc_00333D98:
    *(unsigned __int8 *)(v_r12) = (unsigned __int8)((unsigned int)(v_stack_pD8));
    goto loc_00333631;
loc_00333DA8:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a7 + 56)))) & (1)) != 0) goto loc_00333E7D;
loc_00333DBC:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a7 + 56)))) & (2)) != 0) goto loc_00333ECA;
loc_00333DC4:
    v_rdi = (unsigned int)((v_rdi) | (4));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a7 + 56)))) & (32)) != 0) goto loc_00333E47;
loc_00333DCE:
    if ((((unsigned __int8)(v_rdi)) & (4)) == 0) goto loc_00333622;
    a2 = (a5) >> (12);
    a2 = (a2) & ((unsigned int)(*(unsigned int *)(a7 + 56)));
    result = MiFillVirtualFaultInfo(a5, a2, a5, (unsigned int)(v_stack_pD8));
    goto loc_00333622;
loc_00333E01:
    if (condition_is_below) goto loc_00333D07;
    if (sign_flag) goto loc_00333D07;
    if (*(unsigned __int64 *)(v_stack_pD0 + 8) != 0) goto loc_003334F9;
    goto loc_00333D07;
loc_00333E47:
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFFBULL));
    if ((*(unsigned __int64 *)(a5 + 48)) != 0) goto loc_00333DCE;
    result = MiCompleteSecureProcessFault(v_stack_pD0, a5, a5, (unsigned int)(v_stack_pD8));
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(result))) << (2));
    v_rdi = (unsigned int)((v_rdi) ^ ((unsigned int)((unsigned int)((unsigned int)(v_rdi)))));
    v_rdi = (unsigned int)((v_rdi) & (4));
    v_rdi = (unsigned int)((v_rdi) ^ ((unsigned int)((unsigned int)((unsigned int)(v_rdi)))));
    goto loc_00333DCE;
loc_00333E7D:
    if (((a5) & (66)) != 0) goto loc_00333DBC;
    goto loc_00333622;
loc_00333E90:
    if (v_r13 < (*(unsigned __int64 *)(v_rip + 11508497))) goto loc_00333EAC;
    if (v_r13 < (*(unsigned __int64 *)(v_rip + 11508493))) goto loc_003334E8;
loc_00333EAC:
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a4 + 26, (unsigned int)(0x51517ULL), v_r13, a4);
loc_00333ECA:
    if (((a5) & (a4 + 26)) == 0) goto loc_00333DC4;
    goto loc_00333622;
loc_00333EF0:
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) + 1);
    if (((*(unsigned int *)(v_rip + 13177778)) & ((unsigned int)(v_r15))) == 0) goto loc_00333F2F;
loc_00333EFC:
loc_00333EFE:
    if (!sign_flag) goto loc_00333821;
    goto loc_00333EF0;
loc_00333F0D:
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a4 + 26 + 184))) & (15));
    result = (unsigned __int8)((result) - 1);
    if (((unsigned __int8)(result)) > 3) goto loc_003336BB;
    *(unsigned int *)(v_rip + 11548142) = 1;
    goto loc_003336BB;
loc_00333F2F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13183875)))) & (64)) == 0) goto loc_00333EFC;
    result = KiCheckVpBackingLongSpinWaitHypercall(a4 + 26, (unsigned int)(0x51517ULL), v_r13, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00333EFC;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r15)), (unsigned int)(0x51517ULL), v_r13, a4);
    goto loc_00333EFE;
loc_00333F4C:
    result = MiReleasePageFileInfo((unsigned int)((unsigned int)(v_r15)), (unsigned int)(0x51517ULL), 1, a4);
    goto loc_00333ACA;
}
```

## 5. (Beta) C Style

```c
int64_t MiAllocateWsle(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint8_t Arg5, uint32_t Arg6, void *Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint8_t v_stack_m81;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p30;
    uint64_t v_stack_p40;
    uint8_t v_stack_p41;
    uint64_t v_stack_p48;
    uint64_t v_stack_p68;
    uint64_t v_stack_p8;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pD0;
    uint8_t v_stack_pD8;
    uint64_t v_stack_pE0;
    uint32_t v_stack_pE8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (128);
    Arg2 = 0;
    local_r13 = (Arg2) << (25);
    v_stack_m58 = 0;
    v_stack_m68 = v_xmm0;
    result = (0) << (25);
    local_r13 = (local_r13) - (result);
    v_stack_m7C = 0;
    local_r13 = (local_r13) >> (16);
    v_stack_m78 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)));
    if (local_r13 >= 0) goto loc_00333B4C;
loc_00333342:
    v_stack_m7C = 1;
loc_0033334A:
    if (((1) & ((uint8_t)((uint32_t)(Arg6)))) != 0) goto loc_00333A68;
loc_0033335B:
    Arg2 = 0;
    v_stack_m88 = 0;
    if (condition_is_above_or_equal) goto loc_003339F0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A8))) >> (9));
loc_0033337D:
    result = (uint32_t)((result) & (7));
    if (1 == 0) goto loc_003337CA;
    if ((((uint8_t)((uint32_t)(Arg6))) & (2)) != 0) goto loc_00333C0F;
    if (((uint32_t)(result)) < 5) goto loc_00333A61;
    if ((((uint8_t)((uint32_t)(Arg6))) & (8)) != 0) goto loc_00333C16;
    if (((Arg5) & (1)) == 0) goto loc_003333CC;
    Arg2 = 0;
    if (((Arg5) & (32)) == 0) { Arg2 = 1; }
loc_003333C8:
    v_stack_m88 = (uint32_t)(Arg2);
loc_003333CC:
    Arg4 = (uint8_t)((Arg4) & (7));
    Arg4 = (uint8_t)((Arg4) << (4));
    Arg4 = (uint8_t)((Arg4) | ((uint8_t)(Arg2)));
    v_stack_p20 = Arg4;
loc_003333DF:
    v_stack_m84 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x20)));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x20))) >> (24));
    if ((((uint8_t)(Arg2)) & (8)) != 0) goto loc_00333872;
loc_00333421:
    Arg3 = (uint32_t)((v_stack_m81) & (7));
loc_0033342B:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result * 8))) >> (3));
    if (((uint32_t)(Arg3)) >= ((uint32_t)(local_rbx))) goto loc_0033348E;
    local_r14 = 0;
loc_00333438:
    if (condition_is_below) goto loc_00333900;
    v_stack_m84 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x20)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x20))) >> (24));
    Arg1 = (uint8_t)((Arg1) & (248));
    Arg1 = (uint8_t)((Arg1) | ((uint8_t)(local_rbx)));
    v_stack_m81 = (uint8_t)(Arg1);
    *(uint32_t *)(v_stack_p18 + 0x20) = (uint32_t)((uint32_t)(v_stack_m84));
loc_0033348E:
    if ((((uint8_t)(*(uint64_t *)(v_stack_p18))) & (1)) == 0) goto loc_0033396A;
loc_00333499:
    if (((Arg5) & (1)) == 0) goto loc_00333622;
    local_rbx = (uint8_t)(((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)))) & (15));
    if (((uint8_t)(local_rbx)) == 1) goto loc_003339C3;
    if (((uint8_t)(local_rbx)) < 1) goto loc_003337E7;
loc_003334D7:
    if (((*(uint64_t *)(v_rip + 0xC935A6)) & (0x4000ULL)) != 0) goto loc_003336EE;
loc_003334E8:
    if (Arg7 != NULL) goto loc_00333CE1;
loc_003334F9:
    v_stack_m78 = 0;
loc_00333509:
    if (1 != 0) goto loc_00333921;
loc_00333512:
    if ((uint8_t)(local_rbx) != 0) goto loc_003339DF;
    v_stack_m68 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
loc_00333539:
    v_stack_m60 = v_stack_p10;
    result = (Arg5) >> (12);
    result = (result) & ((uint32_t)(v_stack_p20));
    v_stack_m58 = result;
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9C08) = v_stack_m68;
    if ((*(uint8_t *)(v_rip + 0xAD74A6)) == 0) goto loc_00333BC9;
loc_0033357C:
    if (v_stack_p10 >= Arg5) goto loc_00333BA4;
loc_0033359A:
    Arg1 = 0;
    v_stack_m70 = Arg5;
    v_stack_p30 = 0;
    if (v_stack_p10 < Arg5) goto loc_003335D8;
loc_003335B8:
    if (v_stack_p10 <= Arg5) goto loc_00333C7A;
loc_003335D0:
loc_003335D8:
    if (v_stack_p10 < Arg5) goto loc_00333AFE;
loc_003335E7:
    *(uint64_t *)(v_stack_p10) = Arg5;
    if (0 != 0) goto loc_00333C97;
loc_003335FA:
    if ((((uint8_t)(result * 8)) & (1)) != 0) goto loc_00333D7A;
loc_00333604:
    if (*(uint64_t *)(gs_base + (0 + 0x20)) != 0) {
        *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x9C08) = 0;
    }
    if (v_stack_m78 != 0) goto loc_00333DA8;
loc_00333622:
    if (1 == 0) goto loc_00333631;
    if ((((uint8_t)(result * 8)) & (2)) == 0) goto loc_00333D98;
loc_00333631:
    if ((((uint8_t)((uint32_t)(Arg6))) & (2)) != 0) goto loc_0033368E;
    if ((((uint8_t)((uint32_t)(Arg6))) & (4)) != 0) goto loc_003336C3;
    result = (uint32_t)(v_stack_m7C);
    if (!(sign_flag)) {
        result = (uint32_t)(((uint32_t)(v_stack_m7C)) | (2));
    }
    if (1 == 0) goto loc_003339D0;
loc_00333662:
    result = (uint32_t)((result) | (4));
loc_00333665:
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(result))) | (8));
    if ((((uint8_t)((uint32_t)(Arg6))) & (32)) == 0) { Arg4 = (uint32_t)(result); }
    result = MiAddWorkingSetEntries(v_stack_p8, local_r13, 1, Arg4);
    goto loc_003336C8;
loc_0033368E:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_p8 + 0xB8))) & (15));
    if (((uint8_t)(result)) == 1) {
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB03E65))) == 0) goto loc_00333F0D;
loc_003336BB:
loc_003336C3:
loc_003336C8:
    if (((*(uint32_t *)(v_rip + 0xC93432)) & (0x8000001ULL)) != 0) goto loc_00333D5E;
loc_003336D8:
    local_rsp = (local_rsp) + (128);
    return 1;
loc_003336EE:
    result = (*(uint64_t *)(v_stack_pD0 + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) != 3) goto loc_003334E8;
    if (1 != ((uint8_t)(result))) goto loc_003334E8;
    v_stack_p68 = v_xmm0;
    result = MiGetPagePrivilege(v_stack_pD0, 2, v_stack_p68, Arg4);
    if ((uint32_t)(result) == 0) goto loc_003334E8;
    if (((Arg5) & (32)) != 0) goto loc_00333759;
    if (condition_is_above_or_equal) goto loc_00333759;
    result = Arg5;
    if (((v_stack_p41) & (8)) != 0) {
        result = (Arg5) | (32);
        v_stack_pE0 = result;
    }
    Arg1 = (v_stack_pD0) - (result);
    Arg4 = 0;
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (result);
    result = VslSetPrivilegedPte(Arg1, local_r13, v_stack_p68, Arg4);
    if (((uint32_t)(result)) == 0x80000035ULL) goto loc_00333E90;
    if (!sign_flag) goto loc_003334E8;
    v_stack_p20 = 0;
    result = KeBugCheckEx(26, (uint32_t)(0x51510ULL), v_stack_pD0, (int32_t)((uint32_t)(result)));
loc_003337CA:
    v_stack_pD8 = 0;
    local_rdi = (uint32_t)((uint32_t)(v_stack_pD0));
    if (((uint32_t)(result)) > ((uint32_t)(v_stack_pD0))) { local_rdi = (uint32_t)(result); }
    goto loc_003333DF;
loc_003337E7:
    if (local_r13 >= 26) goto loc_00333A23;
loc_003337FD:
    if (((Arg5) & ((uint32_t)(0x51510ULL))) != 0) goto loc_003334D7;
    if (condition_is_above_or_equal) goto loc_003334D7;
    local_r15 = 0;
loc_00333821:
    if (condition_is_below) goto loc_00333EF0;
    Arg3 = 0;
    result = MiGetPagePrivilege(v_stack_pD0, Arg3 + 1, Arg3, (int32_t)((uint32_t)(result)));
    if ((uint32_t)(result) == 0) {
        Arg2 = 7;
        Arg1 = v_stack_pD0;
        result = MiMarkPfnVerified(Arg1, Arg2, Arg3, (int32_t)((uint32_t)(result)));
    }
    goto loc_003334D7;
loc_00333872:
    if (v_stack_pD0 < ((int32_t)((uint32_t)(result)))) goto loc_0033342B;
    Arg2 = (*(uint64_t *)(v_rip + 0xAFA45B) + *(uint64_t *)(v_rip + 0xAFA45B) * 2) << (4);
    Arg2 = (Arg2) + (*(uint64_t *)(v_rip + 0xAFA45B));
    if (v_stack_pD0 >= Arg2) goto loc_0033342B;
    Arg2 = (v_stack_pD0) - ((int32_t)((uint32_t)(result)));
    Arg2 = (Arg2) >> (4);
    Arg2 = (Arg2) * (Arg7);
    if (Arg2 < (*(uint64_t *)(v_rip + 0xB0234D))) goto loc_003338D0;
    Arg1 = (*(uint64_t *)(v_rip + 0xB0234D)) + (0x800ULL);
    if (Arg2 < Arg1) goto loc_0033342B;
loc_003338D0:
    result = (uint32_t)((result) >> (16));
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) == 6) goto loc_00333421;
    result = MiGetPfnSlabType(v_stack_pD0, Arg2, Arg3, (int32_t)((uint32_t)(result)));
    if (((uint32_t)(result)) == 9) goto loc_0033342B;
    goto loc_00333421;
loc_00333900:
    local_r14 = (uint32_t)(((uint32_t)(Arg6)) + 1);
    if (((*(uint32_t *)(v_rip + 0xC919A2)) & ((uint32_t)(local_r14))) == 0) goto loc_00333C2A;
loc_00333910:
loc_00333912:
    if (!sign_flag) goto loc_00333438;
    goto loc_00333900;
loc_00333921:
    Arg1 = (Arg5) & (0);
    result = ((uint8_t)(Arg2)) << (56);
    result = (result) | (Arg1);
    Arg1 = ((uint8_t)(Arg2)) << (56);
    result = (result) ^ (Arg1);
    result = (result) & (Arg2);
    result = (result) ^ (Arg1);
    v_stack_pE0 = result;
    local_rdi = (uint32_t)((local_rdi * 8) | (2));
    goto loc_00333512;
loc_0033396A:
    local_r15 = 0;
loc_00333975:
    if (condition_is_below) goto loc_00333A40;
    if ((((uint8_t)(*(uint64_t *)(v_stack_pD0))) & (1)) != 0) goto loc_00333C1D;
    result = (*(uint64_t *)(v_stack_pD0)) | (1);
    *(uint64_t *)(v_stack_pD0) = result;
loc_003339AF:
    goto loc_00333499;
loc_003339C3:
    goto loc_003334D7;
loc_003339D0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)))) & (15)) != 0) goto loc_00333665;
    goto loc_00333662;
loc_003339DF:
    if (((uint8_t)(v_stack_pD0)) == 3) goto loc_00333539;
    local_r15 = 0;
    goto loc_0033357C;
loc_003339F0:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_pD0 + 0x5A0))) >> (12));
    result = (uint32_t)((result) & (7));
    if (*(uint64_t *)(*(uint64_t *)(v_stack_pD0 + 0x220) + 0x2A0) == 0) goto loc_0033337D;
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_pD0 + 0x220) + 0x2A0) + 0x444))))) { result = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_pD0 + 0x220) + 0x2A0) + 0x444))); }
    goto loc_0033337D;
loc_00333A23:
    if (local_r13 <= ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_pD0 + 0x220) + 0x2A0) + 0x444)))) goto loc_003334D7;
    goto loc_003337FD;
loc_00333A40:
    local_r15 = (uint32_t)((local_r15) + 1);
    if (((*(uint32_t *)(v_rip + 0xC91862)) & ((uint32_t)(local_r15))) == 0) goto loc_00333C52;
loc_00333A50:
loc_00333A52:
    if (!sign_flag) goto loc_00333975;
    goto loc_00333A40;
loc_00333A61:
    goto loc_003333C8;
loc_00333A68:
    local_rdi = 0;
loc_00333A72:
    if (condition_is_below) goto loc_00333BF0;
    result = MiReleaseWsSwapReservationPfn(v_stack_pD0, 7, Arg3, (int32_t)((uint32_t)(result)));
    result = (*(uint64_t *)(v_stack_pD0 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (result != 0) goto loc_00333F4C;
loc_00333ACA:
    result = MI_READ_PTE_LOCK_FREE(Arg5, result, Arg3, (int32_t)((uint32_t)(result)));
    result = (result) & (-33);
    result = MiWriteValidPteNewProtection(Arg5, result, Arg3, (int32_t)((uint32_t)(result)));
    goto loc_0033335B;
loc_00333AFE:
    if ((((uint8_t)(v_stack_pD0)) & (32)) != 0) goto loc_003335E7;
    result = (result) + (0);
    if (result < result) goto loc_003335E7;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_pC8, v_stack_pD0, 128, (uint32_t)(v_stack_pD8));
    goto loc_003335E7;
loc_00333B4C:
    if (local_r13 > ((uint32_t)(Arg6))) goto loc_00333342;
    local_r12 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)))) & (15)) != 0) goto loc_0033334A;
    result = (*(uint64_t *)(v_stack_pD0)) >> (42);
    if ((((uint8_t)(result)) & (7)) == 0) goto loc_0033334A;
    result = (*(uint64_t *)(v_stack_pD0)) & ((uint32_t)(Arg6));
    *(uint64_t *)(v_stack_pD0) = result;
    goto loc_0033334A;
loc_00333BA4:
    if (v_stack_pC8 <= result) goto loc_00333CAF;
loc_00333BBC:
    goto loc_0033359A;
loc_00333BC9:
    if ((*(uint8_t *)(v_rip + 0xC21FF0)) == 0) goto loc_0033357C;
    result = KdpSetOwedBreakpoints(local_r13, v_stack_pC8, 128, (uint32_t)(v_stack_pD8));
    goto loc_0033357C;
loc_00333BF0:
    local_rdi = (uint32_t)((local_rdi) + 1);
    if (((*(uint32_t *)(v_rip + 0xC916B4)) & ((uint32_t)(local_rdi))) == 0) goto loc_00333D37;
loc_00333BFE:
loc_00333C00:
    if (!sign_flag) goto loc_00333A72;
    goto loc_00333BF0;
loc_00333C0F:
    goto loc_003333C8;
loc_00333C16:
    goto loc_003333C8;
loc_00333C1D:
    goto loc_003339AF;
loc_00333C2A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC92E88)))) & (64)) == 0) goto loc_00333910;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_pD0, 6, 128, (uint32_t)(v_stack_pD8));
    if ((uint8_t)(result) == 0) goto loc_00333910;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r14)), 6, 128, (uint32_t)(v_stack_pD8));
    goto loc_00333912;
loc_00333C52:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC92E60)))) & (64)) == 0) goto loc_00333A50;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_r14)), 6, 128, (uint32_t)(v_stack_pD8));
    if ((uint8_t)(result) == 0) goto loc_00333A50;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r15)), 6, 128, (uint32_t)(v_stack_pD8));
    goto loc_00333A52;
loc_00333C7A:
    result = MiSanitizeShadowPxe((uint32_t)((uint32_t)(local_r15)), v_stack_p48, 128, (uint32_t)(v_stack_pD8));
    v_stack_pE8 = (uint32_t)(result);
    goto loc_003335D0;
loc_00333C97:
    result = MiWritePteShadow(result, v_stack_p48, 128, (uint32_t)(v_stack_pD8));
    goto loc_003335FA;
loc_00333CAF:
    if ((uint8_t)(v_stack_p48) == 0) goto loc_00333BBC;
    local_rdi = (uint32_t)((local_rdi) | (1));
    result = ExAcquireSpinLockExclusiveAtDpcLevel(v_rip + 11548674, v_stack_p48, 128, (uint32_t)(v_stack_pD8));
    Arg1 = 0;
    v_stack_pE8 = 0;
    v_stack_p48 = Arg5;
    goto loc_003335B8;
loc_00333CE1:
    result = MiGetVirtualFaultPageInfo(1, local_r13, 128, (uint32_t)(v_stack_pD8));
    v_stack_p40 = result;
    if (result == 0) goto loc_003334F9;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(1 + 0x38)))) & (32)) != 0) goto loc_00333E01;
loc_00333D07:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(1 + 0x38)))) & (16)) == 0) goto loc_00333509;
    if (v_stack_p30 >= 6) goto loc_00333509;
    Arg2 = (uint8_t)(((uint32_t)(v_stack_pD8)) & (246));
    Arg2 = (uint8_t)((Arg2) | (6));
    v_stack_pD8 = (uint32_t)(Arg2);
    goto loc_00333509;
loc_00333D37:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC92D7B)))) & (64)) == 0) goto loc_00333BFE;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)(*(uint32_t *)(1 + 0x38)), Arg2, 128, (uint32_t)(v_stack_pD8));
    if ((uint8_t)(result) == 0) goto loc_00333BFE;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rdi)), Arg2, 128, (uint32_t)(v_stack_pD8));
    goto loc_00333C00;
loc_00333D5E:
    Arg2 = (uint32_t)(((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB8)))) & (15));
    result = MiLogAllocateWsleEvent(v_stack_pD0, Arg2, local_r13, (uint32_t)(v_stack_pD8));
    goto loc_003336D8;
loc_00333D7A:
    result = MiReplicatePteChange(result, 1, local_r13, (uint32_t)(v_stack_pD8));
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 11548466, 1, local_r13, (uint32_t)(v_stack_pD8));
    goto loc_00333604;
loc_00333D98:
    *(uint8_t *)(local_r12) = (uint8_t)((uint32_t)(v_stack_pD8));
    goto loc_00333631;
loc_00333DA8:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg7 + 0x38)))) & (1)) != 0) goto loc_00333E7D;
loc_00333DBC:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg7 + 0x38)))) & (2)) != 0) goto loc_00333ECA;
loc_00333DC4:
    local_rdi = (uint32_t)((local_rdi) | (4));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg7 + 0x38)))) & (32)) != 0) goto loc_00333E47;
loc_00333DCE:
    if ((((uint8_t)(local_rdi)) & (4)) == 0) goto loc_00333622;
    Arg2 = (Arg5) >> (12);
    Arg2 = (Arg2) & ((uint32_t)(*(uint32_t *)(arg7 + 0x38)));
    result = MiFillVirtualFaultInfo(Arg5, Arg2, Arg5, (uint32_t)(v_stack_pD8));
    goto loc_00333622;
loc_00333E01:
    if (condition_is_below) goto loc_00333D07;
    if (sign_flag) goto loc_00333D07;
    if (*(uint64_t *)(v_stack_pD0 + 0x8) != 0) goto loc_003334F9;
    goto loc_00333D07;
loc_00333E47:
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFFBULL));
    if ((*(uint64_t *)(Arg5 + 0x30)) != 0) goto loc_00333DCE;
    result = MiCompleteSecureProcessFault(v_stack_pD0, Arg5, Arg5, (uint32_t)(v_stack_pD8));
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(result))) << (2));
    local_rdi = (uint32_t)((local_rdi) ^ ((uint32_t)((uint32_t)((uint32_t)(local_rdi)))));
    local_rdi = (uint32_t)((local_rdi) & (4));
    local_rdi = (uint32_t)((local_rdi) ^ ((uint32_t)((uint32_t)((uint32_t)(local_rdi)))));
    goto loc_00333DCE;
loc_00333E7D:
    if (((Arg5) & (66)) != 0) goto loc_00333DBC;
    goto loc_00333622;
loc_00333E90:
    if (local_r13 < (*(uint64_t *)(v_rip + 0xAF9B11))) goto loc_00333EAC;
    if (local_r13 < (*(uint64_t *)(v_rip + 0xAF9B0D))) goto loc_003334E8;
loc_00333EAC:
    Arg4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(Arg4 + 26, (uint32_t)(0x51517ULL), local_r13, Arg4);
loc_00333ECA:
    if (((Arg5) & (Arg4 + 26)) == 0) goto loc_00333DC4;
    goto loc_00333622;
loc_00333EF0:
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) + 1);
    if (((*(uint32_t *)(v_rip + 0xC913B2)) & ((uint32_t)(local_r15))) == 0) goto loc_00333F2F;
loc_00333EFC:
loc_00333EFE:
    if (!sign_flag) goto loc_00333821;
    goto loc_00333EF0;
loc_00333F0D:
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(Arg4 + 0x1A + 0xB8))) & (15));
    result = (uint8_t)((result) - 1);
    if (((uint8_t)(result)) > 3) goto loc_003336BB;
    *(uint32_t *)(v_rip + 0xB035EE) = 1;
    goto loc_003336BB;
loc_00333F2F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC92B83)))) & (64)) == 0) goto loc_00333EFC;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg4 + 26, (uint32_t)(0x51517ULL), local_r13, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00333EFC;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r15)), (uint32_t)(0x51517ULL), local_r13, Arg4);
    goto loc_00333EFE;
loc_00333F4C:
    result = MiReleasePageFileInfo((uint32_t)((uint32_t)(local_r15)), (uint32_t)(0x51517ULL), 1, Arg4);
    goto loc_00333ACA;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB8` | `32` | `R` |
| `Arg7` | `+ 0x38` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003332C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
