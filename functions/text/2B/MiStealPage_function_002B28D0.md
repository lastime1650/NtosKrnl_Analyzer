# MiStealPage

- RVA: `0x002B28D0`–`0x002B3ED4` (길이 `5,636` bytes)
- VA: `0x00000001402B28D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006D79C`
- 디코드: `1,280`개 명령, `5,636/5,636` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **82**; 고유 호출 대상: **49**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **27**

### Outgoing calls
- `0x002B2930` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002B2996` → [MiGetLeafVa](../27/MiGetLeafVa_function_0027C0A0.md) (function, `0x0027C0A0`)
- `0x002B2A44` → [MiLockStealUserVm](MiLockStealUserVm_function_002B3EDC.md) (function, `0x002B3EDC`)
- `0x002B2ABA` → [MiGetPfnChannel](../33/MiGetPfnChannel_function_0033BA90.md) (function, `0x0033BA90`)
- `0x002B2AC5` → [MiPageToNode](../33/MiPageToNode_function_00338CD0.md) (function, `0x00338CD0`)
- `0x002B2B9C` → [MiGetPage](../28/MiGetPage_function_002884C0.md) (function, `0x002884C0`)
- `0x002B2C81` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x002B2D0D` → [MiFlushSingleTbEntry](../28/MiFlushSingleTbEntry_function_0028E730.md) (function, `0x0028E730`)
- `0x002B2D4C` → [MiChangePageAttribute](../33/MiChangePageAttribute_function_00332ECC.md) (function, `0x00332ECC`)
- `0x002B2D79` → [MiCopyPfnEntryEx](MiCopyPfnEntryEx_function_002B2670.md) (function, `0x002B2670`)
- `0x002B2E76` → [MiCopyPage](MiCopyPage_function_002B1B30.md) (function, `0x002B1B30`)
- `0x002B2EE1` → [MiFlushSingleTbEntry](../28/MiFlushSingleTbEntry_function_0028E730.md) (function, `0x0028E730`)
- `0x002B2FC2` → [MiClearPfnReuseFields](../37/MiClearPfnReuseFields_function_003759F0.md) (function, `0x003759F0`)
- `0x002B30E5` → [MiPteInShadowRange](../23/MiPteInShadowRange_function_0023FB00.md) (function, `0x0023FB00`)
- `0x002B3113` → [MiWritePteShadow](../29/MiWritePteShadow_function_00294EAC.md) (function, `0x00294EAC`)
- `0x002B316F` → [MiUnlockStealVm](../28/MiUnlockStealVm_function_0028EF40.md) (function, `0x0028EF40`)
- `0x002B3189` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002B320A` → [MiGetPagePrivilege](../28/MiGetPagePrivilege_function_00285420.md) (function, `0x00285420`)
- `0x002B3236` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x002B32EE` → [MiFlushSingleTbEntry](../28/MiFlushSingleTbEntry_function_0028E730.md) (function, `0x0028E730`)
- `0x002B32FE` → [MiPteInShadowRange](../23/MiPteInShadowRange_function_0023FB00.md) (function, `0x0023FB00`)
- `0x002B332C` → [MiWritePteShadow](../29/MiWritePteShadow_function_00294EAC.md) (function, `0x00294EAC`)
- `0x002B335F` → [MiLockStealSystemVm](../28/MiLockStealSystemVm_function_0028E330.md) (function, `0x0028E330`)
- `0x002B33C0` → [MiWriteValidPteNewPage](../37/MiWriteValidPteNewPage_function_00376068.md) (function, `0x00376068`)
- `0x002B33DA` → [MiReplacePageOfProtoPool](../36/MiReplacePageOfProtoPool_function_00364BB8.md) (function, `0x00364BB8`)
- `0x002B347E` → [MiPrepareToTradeUsingAccessedBit](../45/MiPrepareToTradeUsingAccessedBit_function_0045B488.md) (function, `0x0045B488`)
- `0x002B3576` → [MiHyperSpaceSize](../2C/MiHyperSpaceSize_function_002C2DFC.md) (function, `0x002C2DFC`)
- `0x002B35D7` → [MiLockProtoPoolPage](MiLockProtoPoolPage_function_002B8B80.md) (function, `0x002B8B80`)
- `0x002B360A` → [MiTransformValidPteInPlace](../37/MiTransformValidPteInPlace_function_003765E0.md) (function, `0x003765E0`)
- `0x002B36AA` → [MiRewritePteWithLockBit](../32/MiRewritePteWithLockBit_function_00322FEC.md) (function, `0x00322FEC`)
- `0x002B372C` → [MiReplacePageTablePage](../22/MiReplacePageTablePage_function_00229184.md) (function, `0x00229184`)
- `0x002B3785` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x002B37F9` → [MiWriteValidPteNewProtection](../28/MiWriteValidPteNewProtection_function_00281810.md) (function, `0x00281810`)
- `0x002B3817` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B3826` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002B383E` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B384D` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002B389A` → [MiWriteValidPteNewProtection](../28/MiWriteValidPteNewProtection_function_00281810.md) (function, `0x00281810`)
- `0x002B38AC` → [MiFlushSingleTbEntry](../28/MiFlushSingleTbEntry_function_0028E730.md) (function, `0x0028E730`)
- `0x002B38B8` → [MiCaptureDirtyBitToPfn](../37/MiCaptureDirtyBitToPfn_function_00370DD0.md) (function, `0x00370DD0`)
- `0x002B38DF` → [MiCaptureDirtyBitToPfn](../37/MiCaptureDirtyBitToPfn_function_00370DD0.md) (function, `0x00370DD0`)
- `0x002B3905` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B3915` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002B392D` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B393C` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002B397E` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x002B39AE` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B39BE` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002B3A55` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x002B3A6D` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B3A7C` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002B3A93` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002B3A9B` → [MI_NODE_FROM_PFN](MI_NODE_FROM_PFN_function_002B0F30.md) (function, `0x002B0F30`)
- `0x002B3AFA` → [MiInitializePageChainPacket](../43/MiInitializePageChainPacket_function_004367C0.md) (function, `0x004367C0`)
- `0x002B3B06` → [MiGetPageChain](../33/MiGetPageChain_function_00330130.md) (function, `0x00330130`)
- `0x002B3B78` → [MiVaIsPageFileHash](../43/MiVaIsPageFileHash_function_004349D0.md) (function, `0x004349D0`)
- `0x002B3B94` → [ExAcquireSpinLockSharedAtDpcLevel](../24/ExAcquireSpinLockSharedAtDpcLevel_function_00248E30.md) (function, `0x00248E30`)
- `0x002B3BA4` → [MiVaIsPageFileHash](../43/MiVaIsPageFileHash_function_004349D0.md) (function, `0x004349D0`)
- `0x002B3BB5` → [MiSmallVaStillMapsFrame](../47/MiSmallVaStillMapsFrame_function_00471090.md) (function, `0x00471090`)
- `0x002B3BCB` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x002B3BD9` → [MiSanitizeShadowPxe](../29/MiSanitizeShadowPxe_function_00294B68.md) (function, `0x00294B68`)
- `0x002B3BF4` → [ExReleaseSpinLockSharedFromDpcLevel](../24/ExReleaseSpinLockSharedFromDpcLevel_function_0024A590.md) (function, `0x0024A590`)
- `0x002B3C04` → [MiSetPfnContainingFrame](../36/MiSetPfnContainingFrame_function_00363FC0.md) (function, `0x00363FC0`)
- `0x002B3C12` → [MiSanitizeShadowPxe](../29/MiSanitizeShadowPxe_function_00294B68.md) (function, `0x00294B68`)
- `0x002B3C30` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B3C3F` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002B3C57` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B3C66` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002B3C82` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B3C91` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002B3CA9` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B3CB8` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002B3D17` → [MiReleaseFaultState](../27/MiReleaseFaultState_function_0027D290.md) (function, `0x0027D290`)
- `0x002B3D27` → [KeSwapDirectoryTableBase](../46/KeSwapDirectoryTableBase_function_0046590C.md) (function, `0x0046590C`)
- `0x002B3D30` → [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) (function, `0x003238A0`)
- `0x002B3DE7` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x002B3E07` → [MiUnlockProtoPoolPage](../24/MiUnlockProtoPoolPage_function_00246090.md) (function, `0x00246090`)
- `0x002B3E33` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x002B3E66` → [MiClearPfnImageVerified](../40/MiClearPfnImageVerified_function_00407000.md) (function, `0x00407000`)
- `0x002B3E8D` → [MiPfnIsActivePageTable](../4A/MiPfnIsActivePageTable_function_004AFFAC.md) (function, `0x004AFFAC`)
- `0x002B3E9D` → [MiRevertPfnActivePageTable](../29/MiRevertPfnActivePageTable_function_002938F4.md) (function, `0x002938F4`)
- `0x002B3ECA` → [MiReleaseFreshPage](../33/MiReleaseFreshPage_function_00334AE0.md) (function, `0x00334AE0`)

### Direct callers
- [MiTradePage](../28/MiTradePage_function_0028D160.md) at `0x0028D3E2`

### Static image references
- `0x002B28EC` → RVA `0x00E0A740` (`.data`; read)
- `0x002B2907` → RVA `0x00EF5140` (`.data`; read/write)
- `0x002B29DE` → RVA `0x00E30088` (`.data`; read)
- `0x002B2AAB` → RVA `0x00E2DCCC` (`.data`; read)
- `0x002B2B36` → RVA `0x00E2DCC0` (`.data`; read)
- `0x002B2BFD` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x002B3032` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x002B311D` → RVA `0x00EF5178` (`.data`; read/write)
- `0x002B31B5` → RVA `0x00EF5144` (`.data`; read/write)
- `0x002B3336` → RVA `0x00E2F380` (`.data`; read)
- `0x002B3400` → RVA `0x00EF5150` (`.data`; read/write)
- `0x002B3455` → RVA `0x00EF51A8` (`.data`; read/write)
- `0x002B345E` → RVA `0x00EF51AC` (`.data`; write)
- `0x002B34A3` → RVA `0x00EF5194` (`.data`; read/write)
- `0x002B3544` → RVA `0x00E2F390` (`.data`; read)
- `0x002B356A` → RVA `0x00E2F388` (`.data`; read)
- `0x002B35C6` → RVA `0x00EF5184` (`.data`; read/write)
- `0x002B35EC` → RVA `0x00EF51A0` (`.data`; read/write)
- `0x002B3809` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x002B3D60` → RVA `0x00EF5210` (`.data`; read/write)
- `0x002B3D6E` → RVA `0x00EF5198` (`.data`; read/write)
- `0x002B3D91` → RVA `0x00EF5220` (`.data`; read/write)
- `0x002B3DBA` → RVA `0x00EF5180` (`.data`; read/write)
- `0x002B3DC5` → RVA `0x00EF519C` (`.data`; read/write)
- `0x002B3DDF` → RVA `0x00EF51A4` (`.data`; read/write)
- `0x002B3E7F` → RVA `0x00EF518C` (`.data`; read/write)
- `0x002B3EBC` → RVA `0x00EF5148` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x002B2A85` → [sub_006DB77C](../6D/Unknown_function_006DB77C.md) (`tail-transfer`)
  - `0x002B2C6A` → [sub_006DB77C + 0x116](../6D/Unknown_function_006DB77C.md) (`tail-transfer`)
  - `0x002B3E94` → [sub_006DB77C + 0x172](../6D/Unknown_function_006DB77C.md) (`tail-transfer`)
  - `0x002B3EA3` → [sub_006DB77C + 0x172](../6D/Unknown_function_006DB77C.md) (`tail-transfer`)
  - `0x002B3EB6` → [sub_006DB77C + 0x203](../6D/Unknown_function_006DB77C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002B28D0  40 55                           push rbp
002B28D2  53                              push rbx
002B28D3  56                              push rsi
002B28D4  57                              push rdi
002B28D5  41 54                           push r12
002B28D7  41 55                           push r13
002B28D9  41 56                           push r14
002B28DB  41 57                           push r15
002B28DD  48 8D AC 24 38 FE FF FF         lea rbp, [rsp - 0x1c8]
002B28E5  48 81 EC C8 02 00 00            sub rsp, 0x2c8
002B28EC  48 8B 05 4D 7E B5 00            mov rax, qword ptr [rip + 0xb57e4d]
002B28F3  48 33 C4                        xor rax, rsp
002B28F6  48 89 85 B0 01 00 00            mov qword ptr [rbp + 0x1b0], rax
002B28FD  48 8B 85 38 02 00 00            mov rax, qword ptr [rbp + 0x238]
002B2904  0F B6 DA                        movzx ebx, dl
002B2907  FF 05 33 28 C4 00               inc dword ptr [rip + 0xc42833]
002B290D  41 8B F8                        mov edi, r8d
002B2910  88 54 24 70                     mov byte ptr [rsp + 0x70], dl
002B2914  4C 8B F1                        mov r14, rcx
002B2917  33 D2                           xor edx, edx
002B2919  44 89 45 80                     mov dword ptr [rbp - 0x80], r8d
002B291D  48 8D 8D 34 01 00 00            lea rcx, [rbp + 0x134]
002B2924  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
002B2928  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
002B292C  44 8D 42 74                     lea r8d, [rdx + 0x74]
002B2930  E8 0B 43 41 00                  call 0x1406c6c40
002B2935  4D 8B 7E 08                     mov r15, qword ptr [r14 + 8]
002B2939  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
002B2940  45 33 D2                        xor r10d, r10d
002B2943  89 BD 30 01 00 00               mov dword ptr [rbp + 0x130], edi
002B2949  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
002B294D  41 8B F2                        mov esi, r10d
002B2950  48 89 85 A8 01 00 00            mov qword ptr [rbp + 0x1a8], rax
002B2957  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
002B2961  4C 0B F8                        or r15, rax
002B2964  4C 89 55 90                     mov qword ptr [rbp - 0x70], r10
002B2968  49 8B FF                        mov rdi, r15
002B296B  4C 89 55 C8                     mov qword ptr [rbp - 0x38], r10
002B296F  48 C1 E7 19                     shl rdi, 0x19
002B2973  4C 89 7D A0                     mov qword ptr [rbp - 0x60], r15
002B2977  49 BB 00 00 00 00 80 F6 FF FF   movabs r11, 0xfffff68000000000
002B2981  49 8B C3                        mov rax, r11
002B2984  48 C1 E0 19                     shl rax, 0x19
002B2988  48 2B F8                        sub rdi, rax
002B298B  48 C1 FF 10                     sar rdi, 0x10
002B298F  48 8B CF                        mov rcx, rdi
002B2992  48 89 7D 88                     mov qword ptr [rbp - 0x78], rdi
002B2996  E8 05 97 FC FF                  call 0x14027c0a0
002B299B  4C 8B C8                        mov r9, rax
002B299E  49 8B C3                        mov rax, r11
002B29A1  48 3B F8                        cmp rdi, rax
002B29A4  0F 83 49 0B 00 00               jae 0x1402b34f3
002B29AA  83 8D 38 01 00 00 01            or dword ptr [rbp + 0x138], 1
002B29B1  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002B29BB  48 8B C0                        mov rax, rax
002B29BE  4D 8B E6                        mov r12, r14
002B29C1  4C 89 55 D8                     mov qword ptr [rbp - 0x28], r10
002B29C5  4C 2B E0                        sub r12, rax
002B29C8  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
002B29D2  49 C1 FC 04                     sar r12, 4
002B29D6  4C 0F AF E0                     imul r12, rax
002B29DA  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
002B29DE  48 8B 0D A3 D6 B7 00            mov rcx, qword ptr [rip + 0xb7d6a3]
002B29E5  48 C1 E8 2B                     shr rax, 0x2b
002B29E9  25 FF 03 00 00                  and eax, 0x3ff
002B29EE  4C 89 65 B8                     mov qword ptr [rbp - 0x48], r12
002B29F2  4C 8B 2C C1                     mov r13, qword ptr [rcx + rax*8]
002B29F6  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
002B2A00  4C 89 6D 98                     mov qword ptr [rbp - 0x68], r13
002B2A04  4C 3B C8                        cmp r9, rax
002B2A07  0F 83 29 09 00 00               jae 0x1402b3336
002B2A0D  44 8B 95 38 01 00 00            mov r10d, dword ptr [rbp + 0x138]
002B2A14  41 0F BA EA 0B                  bts r10d, 0xb
002B2A19  44 89 95 38 01 00 00            mov dword ptr [rbp + 0x138], r10d
002B2A20  41 0F BA E2 0B                  bt r10d, 0xb
002B2A25  0F 83 24 09 00 00               jae 0x1402b334f
002B2A2B  48 8D 85 30 01 00 00            lea rax, [rbp + 0x130]
002B2A32  4D 8B CF                        mov r9, r15
002B2A35  44 0F B6 C3                     movzx r8d, bl
002B2A39  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002B2A3E  49 8B D6                        mov rdx, r14
002B2A41  49 8B CD                        mov rcx, r13
002B2A44  E8 93 14 00 00                  call 0x1402b3edc
002B2A49  8B C8                           mov ecx, eax
002B2A4B  83 F8 01                        cmp eax, 1
002B2A4E  0F 85 01 0A 00 00               jne 0x1402b3455
002B2A54  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002B2A5D  33 D2                           xor edx, edx
002B2A5F  4C 8B 85 48 01 00 00            mov r8, qword ptr [rbp + 0x148]
002B2A66  89 54 24 7C                     mov dword ptr [rsp + 0x7c], edx
002B2A6A  4C 89 45 B0                     mov qword ptr [rbp - 0x50], r8
002B2A6E  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
002B2A75  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
002B2A79  89 54 24 78                     mov dword ptr [rsp + 0x78], edx
002B2A7D  44 8B 55 80                     mov r10d, dword ptr [rbp - 0x80]
002B2A81  41 38 76 23                     cmp byte ptr [r14 + 0x23], sil
002B2A85  0F 8C F1 8C 42 00               jl 0x1406db77c
002B2A8B  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002B2A8F  33 D2                           xor edx, edx
002B2A91  C1 E8 10                        shr eax, 0x10
002B2A94  44 0F B6 F8                     movzx r15d, al
002B2A98  49 8B C4                        mov rax, r12
002B2A9B  41 C1 EF 06                     shr r15d, 6
002B2A9F  44 89 7C 24 74                  mov dword ptr [rsp + 0x74], r15d
002B2AA4  41 0F BA E2 0E                  bt r10d, 0xe
002B2AA9  72 63                           jb 0x1402b2b0e
002B2AAB  8B 0D 1B B2 B7 00               mov ecx, dword ptr [rip + 0xb7b21b]
002B2AB1  48 F7 F1                        div rcx
002B2AB4  49 8B CE                        mov rcx, r14
002B2AB7  48 8B FA                        mov rdi, rdx
002B2ABA  E8 D1 8F 08 00                  call 0x14033ba90
002B2ABF  49 8B CC                        mov rcx, r12
002B2AC2  0F B6 D8                        movzx ebx, al
002B2AC5  E8 06 62 08 00                  call 0x140338cd0
002B2ACA  83 E3 01                        and ebx, 1
002B2ACD  83 E0 3F                        and eax, 0x3f
002B2AD0  41 8B D7                        mov edx, r15d
002B2AD3  C1 E2 09                        shl edx, 9
002B2AD6  0B D0                           or edx, eax
002B2AD8  40 0F B6 C7                     movzx eax, dil
002B2ADC  48 8B 7D 88                     mov rdi, qword ptr [rbp - 0x78]
002B2AE0  81 CA 80 01 00 00               or edx, 0x180
002B2AE6  03 D2                           add edx, edx
002B2AE8  0B D3                           or edx, ebx
002B2AEA  8B 5D 80                        mov ebx, dword ptr [rbp - 0x80]
002B2AED  81 E3 00 00 00 01               and ebx, 0x1000000
002B2AF3  C1 E2 08                        shl edx, 8
002B2AF6  0F BA EB 09                     bts ebx, 9
002B2AFA  0B D0                           or edx, eax
002B2AFC  C1 EB 09                        shr ebx, 9
002B2AFF  F7 45 80 00 00 00 02            test dword ptr [rbp - 0x80], 0x2000000
002B2B06  74 40                           je 0x1402b2b48
002B2B08  0F BA EB 0B                     bts ebx, 0xb
002B2B0C  EB 3A                           jmp 0x1402b2b48
002B2B0E  44 8B 05 B7 B1 B7 00            mov r8d, dword ptr [rip + 0xb7b1b7]
002B2B15  BB 01 30 00 00                  mov ebx, 0x3001
002B2B1A  8B 8D 30 02 00 00               mov ecx, dword ptr [rbp + 0x230]
002B2B20  44 8B C9                        mov r9d, ecx
002B2B23  49 F7 F0                        div r8
002B2B26  41 C1 E9 10                     shr r9d, 0x10
002B2B2A  48 8B C2                        mov rax, rdx
002B2B2D  41 83 E1 03                     and r9d, 3
002B2B31  33 D2                           xor edx, edx
002B2B33  45 8B C1                        mov r8d, r9d
002B2B36  4C 8D 0D 83 B1 B7 00            lea r9, [rip + 0xb7b183]
002B2B3D  43 F7 34 81                     div dword ptr [r9 + r8*4]
002B2B41  33 D1                           xor edx, ecx
002B2B43  0F B6 D2                        movzx edx, dl
002B2B46  33 D1                           xor edx, ecx
002B2B48  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
002B2B4C  48 85 C0                        test rax, rax
002B2B4F  74 37                           je 0x1402b2b88
002B2B51  4C 8B 28                        mov r13, qword ptr [rax]
002B2B54  4C 89 6D A8                     mov qword ptr [rbp - 0x58], r13
002B2B58  49 83 FD FF                     cmp r13, -1
002B2B5C  74 26                           je 0x1402b2b84
002B2B5E  4E 8D 3C 6D 00 00 00 00         lea r15, [r13*2]
002B2B66  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002B2B70  4D 03 FD                        add r15, r13
002B2B73  49 C1 E7 04                     shl r15, 4
002B2B77  48 8B C0                        mov rax, rax
002B2B7A  4C 03 F8                        add r15, rax
002B2B7D  BE 08 00 00 00                  mov esi, 8
002B2B82  EB 4D                           jmp 0x1402b2bd1
002B2B84  4C 8B 6D 98                     mov r13, qword ptr [rbp - 0x68]
002B2B88  48 83 BD A8 01 00 00 FF         cmp qword ptr [rbp + 0x1a8], -1
002B2B90  0F 85 F0 0E 00 00               jne 0x1402b3a86
002B2B96  44 8B C3                        mov r8d, ebx
002B2B99  49 8B CD                        mov rcx, r13
002B2B9C  E8 1F 59 FD FF                  call 0x1402884c0
002B2BA1  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
002B2BA5  4C 8B E8                        mov r13, rax
002B2BA8  48 83 F8 FF                     cmp rax, -1
002B2BAC  0F 84 F1 08 00 00               je 0x1402b34a3
002B2BB2  4C 8D 3C 45 00 00 00 00         lea r15, [rax*2]
002B2BBA  4C 03 F8                        add r15, rax
002B2BBD  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002B2BC7  49 C1 E7 04                     shl r15, 4
002B2BCB  48 8B C0                        mov rax, rax
002B2BCE  4C 03 F8                        add r15, rax
002B2BD1  4D 3B FE                        cmp r15, r14
002B2BD4  0F 84 9F 11 00 00               je 0x1402b3d79
002B2BDA  33 FF                           xor edi, edi
002B2BDC  8B DF                           mov ebx, edi
002B2BDE  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
002B2BE5  0F 82 45 04 00 00               jb 0x1402b3030
002B2BEB  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002B2BEF  8B 5D 80                        mov ebx, dword ptr [rbp - 0x80]
002B2BF2  C1 E8 18                        shr eax, 0x18
002B2BF5  A8 40                           test al, 0x40
002B2BF7  0F 85 8A 11 00 00               jne 0x1402b3d87
002B2BFD  48 F7 05 80 3E D1 00 00 40 00 00  test qword ptr [rip + 0xd13e80], 0x4000
002B2C08  0F 85 F2 05 00 00               jne 0x1402b3200
002B2C0E  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002B2C12  66 83 F8 01                     cmp ax, 1
002B2C16  0F 85 8F 11 00 00               jne 0x1402b3dab
002B2C1C  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002B2C20  C1 E8 18                        shr eax, 0x18
002B2C23  A8 08                           test al, 8
002B2C25  0F 85 72 09 00 00               jne 0x1402b359d
002B2C2B  49 8B 06                        mov rax, qword ptr [r14]
002B2C2E  A8 01                           test al, 1
002B2C30  0F 84 67 09 00 00               je 0x1402b359d
002B2C36  41 0F B6 46 22                  movzx eax, byte ptr [r14 + 0x22]
002B2C3B  24 07                           and al, 7
002B2C3D  3C 06                           cmp al, 6
002B2C3F  0F 85 2B 12 00 00               jne 0x1402b3e70
002B2C45  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
002B2C49  48 8B 0D 38 D4 B7 00            mov rcx, qword ptr [rip + 0xb7d438]
002B2C50  48 C1 E8 2B                     shr rax, 0x2b
002B2C54  25 FF 03 00 00                  and eax, 0x3ff
002B2C59  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
002B2C5D  48 39 55 98                     cmp qword ptr [rbp - 0x68], rdx
002B2C61  0F 85 09 12 00 00               jne 0x1402b3e70
002B2C67  83 FE 08                        cmp esi, 8
002B2C6A  0F 84 22 8C 42 00               je 0x1406db892
002B2C70  8B 85 38 01 00 00               mov eax, dword ptr [rbp + 0x138]
002B2C76  48 8B 5D A0                     mov rbx, qword ptr [rbp - 0x60]
002B2C7A  A8 20                           test al, 0x20
002B2C7C  75 11                           jne 0x1402b2c8f
002B2C7E  48 8B CB                        mov rcx, rbx
002B2C81  E8 1A FC FC FF                  call 0x1402828a0
002B2C86  48 8B F8                        mov rdi, rax
002B2C89  8B 85 38 01 00 00               mov eax, dword ptr [rbp + 0x138]
002B2C8F  83 BD 60 01 00 00 03            cmp dword ptr [rbp + 0x160], 3
002B2C96  74 21                           je 0x1402b2cb9
002B2C98  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002B2C9C  48 B9 FF FF FF FF FF FF FF 3F   movabs rcx, 0x3fffffffffffffff
002B2CA6  48 23 C1                        and rax, rcx
002B2CA9  48 83 F8 01                     cmp rax, 1
002B2CAD  0F 87 94 09 00 00               ja 0x1402b3647
002B2CB3  8B 85 38 01 00 00               mov eax, dword ptr [rbp + 0x138]
002B2CB9  83 BD 60 01 00 00 02            cmp dword ptr [rbp + 0x160], 2
002B2CC0  74 50                           je 0x1402b2d12
002B2CC2  A8 20                           test al, 0x20
002B2CC4  0F 85 AE 07 00 00               jne 0x1402b3478
002B2CCA  A8 08                           test al, 8
002B2CCC  0F 85 65 08 00 00               jne 0x1402b3537
002B2CD2  40 F6 C7 42                     test dil, 0x42
002B2CD6  0F 84 B5 05 00 00               je 0x1402b3291
002B2CDC  84 C0                           test al, al
002B2CDE  0F 88 0B 0B 00 00               js 0x1402b37ef
002B2CE4  83 C8 40                        or eax, 0x40
002B2CE7  41 B8 01 00 00 00               mov r8d, 1
002B2CED  89 85 38 01 00 00               mov dword ptr [rbp + 0x138], eax
002B2CF3  48 8B C7                        mov rax, rdi
002B2CF6  48 83 E0 FE                     and rax, 0xfffffffffffffffe
002B2CFA  48 0F BA E8 0A                  bts rax, 0xa
002B2CFF  48 89 03                        mov qword ptr [rbx], rax
002B2D02  83 CE 02                        or esi, 2
002B2D05  8B 54 24 78                     mov edx, dword ptr [rsp + 0x78]
002B2D09  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
002B2D0D  E8 1E BA FD FF                  call 0x14028e730
002B2D12  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
002B2D16  83 F8 01                        cmp eax, 1
002B2D19  0F 84 F5 08 00 00               je 0x1402b3614
002B2D1F  33 DB                           xor ebx, ebx
002B2D21  F0 49 0F BA 6F 18 3F            lock bts qword ptr [r15 + 0x18], 0x3f
002B2D28  0F 82 22 03 00 00               jb 0x1402b3050
002B2D2E  41 8B 47 20                     mov eax, dword ptr [r15 + 0x20]
002B2D32  8B 54 24 74                     mov edx, dword ptr [rsp + 0x74]
002B2D36  C1 E8 10                        shr eax, 0x10
002B2D39  0F B6 C0                        movzx eax, al
002B2D3C  C1 E8 06                        shr eax, 6
002B2D3F  3B C2                           cmp eax, edx
002B2D41  74 0E                           je 0x1402b2d51
002B2D43  41 B8 09 00 00 00               mov r8d, 9
002B2D49  49 8B CF                        mov rcx, r15
002B2D4C  E8 7B 01 08 00                  call 0x140332ecc
002B2D51  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
002B2D55  48 B9 FF FF FF FF FF FF FF C7   movabs rcx, 0xc7ffffffffffffff
002B2D5F  48 23 C1                        and rax, rcx
002B2D62  49 89 47 18                     mov qword ptr [r15 + 0x18], rax
002B2D66  83 BD 60 01 00 00 02            cmp dword ptr [rbp + 0x160], 2
002B2D6D  0F 84 FD 0D 00 00               je 0x1402b3b70
002B2D73  49 8B D6                        mov rdx, r14
002B2D76  49 8B CF                        mov rcx, r15
002B2D79  E8 F2 F8 FF FF                  call 0x1402b2670
002B2D7E  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
002B2D82  49 BC FF FF FF FF FF 00 00 00   movabs r12, 0xffffffffff
002B2D8C  49 23 C4                        and rax, r12
002B2D8F  83 CE 04                        or esi, 4
002B2D92  48 3B 45 B8                     cmp rax, qword ptr [rbp - 0x48]
002B2D96  0F 84 62 0E 00 00               je 0x1402b3bfe
002B2D9C  49 BD FF FF FF FF FF FF FF 7F   movabs r13, 0x7fffffffffffffff
002B2DA6  F0 4D 21 6F 18                  lock and qword ptr [r15 + 0x18], r13
002B2DAB  8B 9D 38 01 00 00               mov ebx, dword ptr [rbp + 0x138]
002B2DB1  F6 C3 20                        test bl, 0x20
002B2DB4  75 4F                           jne 0x1402b2e05
002B2DB6  83 BD 60 01 00 00 02            cmp dword ptr [rbp + 0x160], 2
002B2DBD  74 46                           je 0x1402b2e05
002B2DBF  0F BA E3 08                     bt ebx, 8
002B2DC3  72 30                           jb 0x1402b2df5
002B2DC5  8B 4C 24 78                     mov ecx, dword ptr [rsp + 0x78]
002B2DC9  F6 C3 08                        test bl, 8
002B2DCC  0F 85 E3 06 00 00               jne 0x1402b34b5
002B2DD2  85 C9                           test ecx, ecx
002B2DD4  0F 85 DB 06 00 00               jne 0x1402b34b5
002B2DDA  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002B2DDE  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
002B2DE2  C1 E8 10                        shr eax, 0x10
002B2DE5  24 FD                           and al, 0xfd
002B2DE7  0C 05                           or al, 5
002B2DE9  88 44 24 76                     mov byte ptr [rsp + 0x76], al
002B2DED  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
002B2DF1  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
002B2DF5  F0 4D 21 6E 18                  lock and qword ptr [r14 + 0x18], r13
002B2DFA  8B 9D 38 01 00 00               mov ebx, dword ptr [rbp + 0x138]
002B2E00  C6 44 24 70 11                  mov byte ptr [rsp + 0x70], 0x11
002B2E05  0F BA E3 08                     bt ebx, 8
002B2E09  0F 82 C2 07 00 00               jb 0x1402b35d1
002B2E0F  45 33 C9                        xor r9d, r9d
002B2E12  4C 89 4D 98                     mov qword ptr [rbp - 0x68], r9
002B2E16  0F BA E3 08                     bt ebx, 8
002B2E1A  0F 82 AA 05 00 00               jb 0x1402b33ca
002B2E20  83 BD 60 01 00 00 03            cmp dword ptr [rbp + 0x160], 3
002B2E27  0F 84 10 10 00 00               je 0x1402b3e3d
002B2E2D  8B C3                           mov eax, ebx
002B2E2F  24 0A                           and al, 0xa
002B2E31  3C 08                           cmp al, 8
002B2E33  0F 84 7B 08 00 00               je 0x1402b36b4
002B2E39  44 0F B6 64 24 70               movzx r12d, byte ptr [rsp + 0x70]
002B2E3F  81 E3 00 10 00 00               and ebx, 0x1000
002B2E45  0F BA EB 13                     bts ebx, 0x13
002B2E49  C1 EB 0B                        shr ebx, 0xb
002B2E4C  41 80 FC 11                     cmp r12b, 0x11
002B2E50  74 19                           je 0x1402b2e6b
002B2E52  83 CB 04                        or ebx, 4
002B2E55  45 8B E1                        mov r12d, r9d
002B2E58  F0 49 0F BA 6F 18 3F            lock bts qword ptr [r15 + 0x18], 0x3f
002B2E5F  0F 82 5B 03 00 00               jb 0x1402b31c0
002B2E65  44 0F B6 64 24 70               movzx r12d, byte ptr [rsp + 0x70]
002B2E6B  48 8B 55 B8                     mov rdx, qword ptr [rbp - 0x48]
002B2E6F  44 8B C3                        mov r8d, ebx
002B2E72  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
002B2E76  E8 B5 EC FF FF                  call 0x1402b1b30
002B2E7B  F6 C3 04                        test bl, 4
002B2E7E  74 05                           je 0x1402b2e85
002B2E80  F0 4D 21 6F 18                  lock and qword ptr [r15 + 0x18], r13
002B2E85  F6 85 38 01 00 00 20            test byte ptr [rbp + 0x138], 0x20
002B2E8C  0F 84 72 01 00 00               je 0x1402b3004
002B2E92  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
002B2E96  48 B9 FF 0F 00 00 00 00 F0 FF   movabs rcx, 0xfff0000000000fff
002B2EA0  48 C1 E0 0C                     shl rax, 0xc
002B2EA4  48 8B D8                        mov rbx, rax
002B2EA7  48 33 DF                        xor rbx, rdi
002B2EAA  48 23 D9                        and rbx, rcx
002B2EAD  48 33 D8                        xor rbx, rax
002B2EB0  F6 85 38 01 00 00 20            test byte ptr [rbp + 0x138], 0x20
002B2EB7  0F 85 B2 01 00 00               jne 0x1402b306f
002B2EBD  8B 85 38 01 00 00               mov eax, dword ptr [rbp + 0x138]
002B2EC3  0F BA E0 09                     bt eax, 9
002B2EC7  0F 83 01 02 00 00               jae 0x1402b30ce
002B2ECD  40 F6 C6 02                     test sil, 2
002B2ED1  75 13                           jne 0x1402b2ee6
002B2ED3  8B 54 24 78                     mov edx, dword ptr [rsp + 0x78]
002B2ED7  41 B8 40 00 00 00               mov r8d, 0x40
002B2EDD  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
002B2EE1  E8 4A B8 FD FF                  call 0x14028e730
002B2EE6  33 FF                           xor edi, edi
002B2EE8  F7 85 38 01 00 00 00 01 00 00   test dword ptr [rbp + 0x138], 0x100
002B2EF2  0F 85 2E 03 00 00               jne 0x1402b3226
002B2EF8  8B 85 38 01 00 00               mov eax, dword ptr [rbp + 0x138]
002B2EFE  0F B6 5C 24 70                  movzx ebx, byte ptr [rsp + 0x70]
002B2F03  24 50                           and al, 0x50
002B2F05  3C 10                           cmp al, 0x10
002B2F07  0F 84 82 07 00 00               je 0x1402b368f
002B2F0D  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
002B2F11  48 C1 E8 3C                     shr rax, 0x3c
002B2F15  24 07                           and al, 7
002B2F17  3C 03                           cmp al, 3
002B2F19  0F 84 34 0F 00 00               je 0x1402b3e53
002B2F1F  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002B2F23  83 BD 60 01 00 00 02            cmp dword ptr [rbp + 0x160], 2
002B2F2A  0F 84 B9 0C 00 00               je 0x1402b3be9
002B2F30  80 FB 11                        cmp bl, 0x11
002B2F33  75 0F                           jne 0x1402b2f44
002B2F35  8B DF                           mov ebx, edi
002B2F37  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
002B2F3E  0F 82 9D 02 00 00               jb 0x1402b31e1
002B2F44  49 8B 56 28                     mov rdx, qword ptr [r14 + 0x28]
002B2F48  0F 57 C0                        xorps xmm0, xmm0
002B2F4B  48 8B CA                        mov rcx, rdx
002B2F4E  48 89 7D 60                     mov qword ptr [rbp + 0x60], rdi
002B2F52  0F 57 C9                        xorps xmm1, xmm1
002B2F55  48 89 95 88 00 00 00            mov qword ptr [rbp + 0x88], rdx
002B2F5C  49 B8 FF FF FF FF FF FF FF 8F   movabs r8, 0x8fffffffffffffff
002B2F66  48 8B C2                        mov rax, rdx
002B2F69  49 23 C8                        and rcx, r8
002B2F6C  F3 0F 7F 45 68                  movdqu xmmword ptr [rbp + 0x68], xmm0
002B2F71  F3 0F 7F 4D 78                  movdqu xmmword ptr [rbp + 0x78], xmm1
002B2F76  0F 11 85 90 00 00 00            movups xmmword ptr [rbp + 0x90], xmm0
002B2F7D  0F 11 85 A0 00 00 00            movups xmmword ptr [rbp + 0xa0], xmm0
002B2F84  0F 11 85 B0 00 00 00            movups xmmword ptr [rbp + 0xb0], xmm0
002B2F8B  F0 49 0F B1 4E 28               lock cmpxchg qword ptr [r14 + 0x28], rcx
002B2F91  48 89 85 B8 00 00 00            mov qword ptr [rbp + 0xb8], rax
002B2F98  48 3B D0                        cmp rdx, rax
002B2F9B  74 22                           je 0x1402b2fbf
002B2F9D  48 8B C8                        mov rcx, rax
002B2FA0  48 89 85 88 00 00 00            mov qword ptr [rbp + 0x88], rax
002B2FA7  49 23 C8                        and rcx, r8
002B2FAA  48 8B D0                        mov rdx, rax
002B2FAD  F0 49 0F B1 4E 28               lock cmpxchg qword ptr [r14 + 0x28], rcx
002B2FB3  48 89 85 B8 00 00 00            mov qword ptr [rbp + 0xb8], rax
002B2FBA  48 3B D0                        cmp rdx, rax
002B2FBD  75 DE                           jne 0x1402b2f9d
002B2FBF  49 8B CE                        mov rcx, r14
002B2FC2  E8 29 2A 0C 00                  call 0x1403759f0
002B2FC7  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002B2FCB  48 B9 00 00 00 00 00 00 00 C0   movabs rcx, 0xc000000000000000
002B2FD5  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
002B2FD9  66 89 7C 24 74                  mov word ptr [rsp + 0x74], di
002B2FDE  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
002B2FE2  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
002B2FE6  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002B2FEA  48 23 C1                        and rax, rcx
002B2FED  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
002B2FF1  F0 4D 21 6E 18                  lock and qword ptr [r14 + 0x18], r13
002B2FF6  48 8B 7D 90                     mov rdi, qword ptr [rbp - 0x70]
002B2FFA  BB 01 00 00 00                  mov ebx, 1
002B2FFF  E9 A1 01 00 00                  jmp 0x1402b31a5
002B3004  41 80 FC 11                     cmp r12b, 0x11
002B3008  0F 84 84 FE FF FF               je 0x1402b2e92
002B300E  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002B3012  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
002B3016  C1 E8 10                        shr eax, 0x10
002B3019  24 FD                           and al, 0xfd
002B301B  0C 05                           or al, 5
002B301D  88 44 24 76                     mov byte ptr [rsp + 0x76], al
002B3021  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
002B3025  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
002B3029  E9 64 FE FF FF                  jmp 0x1402b2e92
002B302E  66 90                           nop
002B3030  FF C3                           inc ebx
002B3032  85 1D 74 22 D1 00               test dword ptr [rip + 0xd12274], ebx
002B3038  0F 84 CB 07 00 00               je 0x1402b3809
002B303E  F3 90                           pause
002B3040  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002B3044  48 85 C0                        test rax, rax
002B3047  0F 89 91 FB FF FF               jns 0x1402b2bde
002B304D  EB E1                           jmp 0x1402b3030
002B304F  90                              nop
002B3050  FF C3                           inc ebx
002B3052  85 1D 54 22 D1 00               test dword ptr [rip + 0xd12254], ebx
002B3058  0F 84 D2 07 00 00               je 0x1402b3830
002B305E  F3 90                           pause
002B3060  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
002B3064  48 85 C0                        test rax, rax
002B3067  0F 89 B4 FC FF FF               jns 0x1402b2d21
002B306D  EB E1                           jmp 0x1402b3050
002B306F  48 83 CB 20                     or rbx, 0x20
002B3073  33 D2                           xor edx, edx
002B3075  44 8B E2                        mov r12d, edx
002B3078  F0 49 0F BA 6F 18 3F            lock bts qword ptr [r15 + 0x18], 0x3f
002B307F  0F 82 EB 01 00 00               jb 0x1402b3270
002B3085  48 F7 05 F8 39 D1 00 00 00 00 02  test qword ptr [rip + 0xd139f8], 0x2000000
002B3090  74 03                           je 0x1402b3095
002B3092  0F AE E8                        lfence
002B3095  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
002B3099  48 8B C7                        mov rax, rdi
002B309C  F0 48 0F B1 19                  lock cmpxchg qword ptr [rcx], rbx
002B30A1  0F 84 6B 04 00 00               je 0x1402b3512
002B30A7  41 8B 47 20                     mov eax, dword ptr [r15 + 0x20]
002B30AB  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
002B30AF  C1 E8 10                        shr eax, 0x10
002B30B2  24 FD                           and al, 0xfd
002B30B4  0C 05                           or al, 5
002B30B6  88 44 24 76                     mov byte ptr [rsp + 0x76], al
002B30BA  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
002B30BE  41 89 47 20                     mov dword ptr [r15 + 0x20], eax
002B30C2  F0 4D 21 6F 18                  lock and qword ptr [r15 + 0x18], r13
002B30C7  F0 4D 21 6E 18                  lock and qword ptr [r14 + 0x18], r13
002B30CC  EB 69                           jmp 0x1402b3137
002B30CE  A8 40                           test al, 0x40
002B30D0  0F 84 6C 01 00 00               je 0x1402b3242
002B30D6  4C 8B 65 A0                     mov r12, qword ptr [rbp - 0x60]
002B30DA  33 D2                           xor edx, edx
002B30DC  49 8B CC                        mov rcx, r12
002B30DF  48 89 5D E0                     mov qword ptr [rbp - 0x20], rbx
002B30E3  8B FA                           mov edi, edx
002B30E5  E8 16 CA F8 FF                  call 0x14023fb00
002B30EA  85 C0                           test eax, eax
002B30EC  0F 85 E3 0A 00 00               jne 0x1402b3bd5
002B30F2  48 0F BA 25 8D 39 D1 00 24      bt qword ptr [rip + 0xd1398d], 0x24
002B30FB  0F 82 4C 06 00 00               jb 0x1402b374d
002B3101  49 89 1C 24                     mov qword ptr [r12], rbx
002B3105  85 FF                           test edi, edi
002B3107  0F 84 C0 FD FF FF               je 0x1402b2ecd
002B310D  48 8B D3                        mov rdx, rbx
002B3110  49 8B CC                        mov rcx, r12
002B3113  E8 94 1D FE FF                  call 0x140294eac
002B3118  E9 B0 FD FF FF                  jmp 0x1402b2ecd
002B311D  FF 05 55 20 C4 00               inc dword ptr [rip + 0xc42055]
002B3123  49 BD FF FF FF FF FF FF FF 7F   movabs r13, 0x7fffffffffffffff
002B312D  F0 4D 21 6F 18                  lock and qword ptr [r15 + 0x18], r13
002B3132  F0 4D 21 6E 18                  lock and qword ptr [r14 + 0x18], r13
002B3137  49 8B FF                        mov rdi, r15
002B313A  4D 85 FF                        test r15, r15
002B313D  0F 85 47 0D 00 00               jne 0x1402b3e8a
002B3143  8B 4C 24 7C                     mov ecx, dword ptr [rsp + 0x7c]
002B3147  83 F9 01                        cmp ecx, 1
002B314A  74 57                           je 0x1402b31a3
002B314C  41 0F B6 46 22                  movzx eax, byte ptr [r14 + 0x22]
002B3151  24 07                           and al, 7
002B3153  3C 06                           cmp al, 6
002B3155  0F 85 4D 0D 00 00               jne 0x1402b3ea8
002B315B  8B 5C 24 7C                     mov ebx, dword ptr [rsp + 0x7c]
002B315F  83 F9 02                        cmp ecx, 2
002B3162  0F 84 45 0D 00 00               je 0x1402b3ead
002B3168  48 8D 8D 30 01 00 00            lea rcx, [rbp + 0x130]
002B316F  E8 CC BD FD FF                  call 0x14028ef40
002B3174  48 85 FF                        test rdi, rdi
002B3177  0F 85 4A 0D 00 00               jne 0x1402b3ec7
002B317D  8B C3                           mov eax, ebx
002B317F  48 8B 8D B0 01 00 00            mov rcx, qword ptr [rbp + 0x1b0]
002B3186  48 33 CC                        xor rcx, rsp
002B3189  E8 B2 94 3F 00                  call 0x1406ac640
002B318E  48 81 C4 C8 02 00 00            add rsp, 0x2c8
002B3195  41 5F                           pop r15
002B3197  41 5E                           pop r14
002B3199  41 5D                           pop r13
002B319B  41 5C                           pop r12
002B319D  5F                              pop rdi
002B319E  5E                              pop rsi
002B319F  5B                              pop rbx
002B31A0  5D                              pop rbp
002B31A1  C3                              ret
002B31A2  CC                              int3
002B31A3  8B D9                           mov ebx, ecx
002B31A5  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
002B31A9  48 85 C9                        test rcx, rcx
002B31AC  74 07                           je 0x1402b31b5
002B31AE  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
002B31B2  48 89 01                        mov qword ptr [rcx], rax
002B31B5  FF 05 89 1F C4 00               inc dword ptr [rip + 0xc41f89]
002B31BB  EB AB                           jmp 0x1402b3168
002B31BD  0F 1F 00                        nop dword ptr [rax]
002B31C0  41 FF C4                        inc r12d
002B31C3  44 85 25 E2 20 D1 00            test dword ptr [rip + 0xd120e2], r12d
002B31CA  0F 84 27 07 00 00               je 0x1402b38f7
002B31D0  F3 90                           pause
002B31D2  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
002B31D6  48 85 C0                        test rax, rax
002B31D9  0F 89 79 FC FF FF               jns 0x1402b2e58
002B31DF  EB DF                           jmp 0x1402b31c0
002B31E1  FF C3                           inc ebx
002B31E3  85 1D C3 20 D1 00               test dword ptr [rip + 0xd120c3], ebx
002B31E9  0F 84 30 07 00 00               je 0x1402b391f
002B31EF  F3 90                           pause
002B31F1  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002B31F5  48 85 C0                        test rax, rax
002B31F8  0F 89 39 FD FF FF               jns 0x1402b2f37
002B31FE  EB E1                           jmp 0x1402b31e1
002B3200  45 33 C0                        xor r8d, r8d
002B3203  49 8B CE                        mov rcx, r14
002B3206  41 8D 50 01                     lea edx, [r8 + 1]
002B320A  E8 11 22 FD FF                  call 0x140285420
002B320F  85 C0                           test eax, eax
002B3211  0F 84 F7 F9 FF FF               je 0x1402b2c0e
002B3217  81 8D 38 01 00 00 00 10 00 00   or dword ptr [rbp + 0x138], 0x1000
002B3221  E9 E8 F9 FF FF                  jmp 0x1402b2c0e
002B3226  F0 4D 21 6F 18                  lock and qword ptr [r15 + 0x18], r13
002B322B  F0 4D 21 6E 18                  lock and qword ptr [r14 + 0x18], r13
002B3230  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
002B3234  B2 11                           mov dl, 0x11
002B3236  E8 55 2E F9 FF                  call 0x140246090
002B323B  B3 11                           mov bl, 0x11
002B323D  E9 CB FC FF FF                  jmp 0x1402b2f0d
002B3242  F7 85 38 01 00 00 00 01 00 00   test dword ptr [rbp + 0x138], 0x100
002B324C  75 52                           jne 0x1402b32a0
002B324E  8B 85 38 01 00 00               mov eax, dword ptr [rbp + 0x138]
002B3254  24 50                           and al, 0x50
002B3256  3C 10                           cmp al, 0x10
002B3258  0F 84 6A 07 00 00               je 0x1402b39c8
002B325E  4C 8B 65 A0                     mov r12, qword ptr [rbp - 0x60]
002B3262  EB 44                           jmp 0x1402b32a8
002B3264  0F 1F 40 00                     nop dword ptr [rax]
002B3268  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
002B3270  41 FF C4                        inc r12d
002B3273  44 85 25 32 20 D1 00            test dword ptr [rip + 0xd12032], r12d
002B327A  0F 84 20 07 00 00               je 0x1402b39a0
002B3280  F3 90                           pause
002B3282  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
002B3286  48 85 C0                        test rax, rax
002B3289  0F 89 E9 FD FF FF               jns 0x1402b3078
002B328F  EB DF                           jmp 0x1402b3270
002B3291  0F BA E0 0C                     bt eax, 0xc
002B3295  0F 82 41 FA FF FF               jb 0x1402b2cdc
002B329B  E9 72 FA FF FF                  jmp 0x1402b2d12
002B32A0  4C 8B 65 A0                     mov r12, qword ptr [rbp - 0x60]
002B32A4  49 8B 04 24                     mov rax, qword ptr [r12]
002B32A8  48 0F BA E3 0B                  bt rbx, 0xb
002B32AD  0F 83 04 01 00 00               jae 0x1402b33b7
002B32B3  F7 85 38 01 00 00 00 01 00 00   test dword ptr [rbp + 0x138], 0x100
002B32BD  0F 85 34 03 00 00               jne 0x1402b35f7
002B32C3  4C 8B CB                        mov r9, rbx
002B32C6  49 83 E1 FE                     and r9, 0xfffffffffffffffe
002B32CA  49 0F BA E9 0A                  bts r9, 0xa
002B32CF  F6 85 38 01 00 00 01            test byte ptr [rbp + 0x138], 1
002B32D6  0F 84 BD 03 00 00               je 0x1402b3699
002B32DC  4D 89 0C 24                     mov qword ptr [r12], r9
002B32E0  8B 54 24 78                     mov edx, dword ptr [rsp + 0x78]
002B32E4  41 B8 01 00 00 00               mov r8d, 1
002B32EA  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
002B32EE  E8 3D B4 FD FF                  call 0x14028e730
002B32F3  33 C0                           xor eax, eax
002B32F5  48 89 5D E8                     mov qword ptr [rbp - 0x18], rbx
002B32F9  49 8B CC                        mov rcx, r12
002B32FC  8B F8                           mov edi, eax
002B32FE  E8 FD C7 F8 FF                  call 0x14023fb00
002B3303  85 C0                           test eax, eax
002B3305  0F 85 03 09 00 00               jne 0x1402b3c0e
002B330B  48 0F BA 25 74 37 D1 00 24      bt qword ptr [rip + 0xd13774], 0x24
002B3314  0F 82 2C 06 00 00               jb 0x1402b3946
002B331A  49 89 1C 24                     mov qword ptr [r12], rbx
002B331E  85 FF                           test edi, edi
002B3320  0F 84 C0 FB FF FF               je 0x1402b2ee6
002B3326  48 8B D3                        mov rdx, rbx
002B3329  49 8B CC                        mov rcx, r12
002B332C  E8 7B 1B FE FF                  call 0x140294eac
002B3331  E9 B0 FB FF FF                  jmp 0x1402b2ee6
002B3336  4C 3B 0D 43 C0 B7 00            cmp r9, qword ptr [rip + 0xb7c043]
002B333D  0F 83 01 02 00 00               jae 0x1402b3544
002B3343  44 8B 95 38 01 00 00            mov r10d, dword ptr [rbp + 0x138]
002B334A  E9 D1 F6 FF FF                  jmp 0x1402b2a20
002B334F  4C 8D 8D 30 01 00 00            lea r9, [rbp + 0x130]
002B3356  4D 8B C7                        mov r8, r15
002B3359  0F B6 D3                        movzx edx, bl
002B335C  49 8B CE                        mov rcx, r14
002B335F  E8 CC AF FD FF                  call 0x14028e330
002B3364  8B C8                           mov ecx, eax
002B3366  83 F8 01                        cmp eax, 1
002B3369  0F 85 E6 00 00 00               jne 0x1402b3455
002B336F  48 8B 85 48 01 00 00            mov rax, qword ptr [rbp + 0x148]
002B3376  33 DB                           xor ebx, ebx
002B3378  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
002B337C  BA 01 00 00 00                  mov edx, 1
002B3381  8B CB                           mov ecx, ebx
002B3383  89 5C 24 7C                     mov dword ptr [rsp + 0x7c], ebx
002B3387  89 54 24 78                     mov dword ptr [rsp + 0x78], edx
002B338B  8B 80 B8 00 00 00               mov eax, dword ptr [rax + 0xb8]
002B3391  24 0F                           and al, 0xf
002B3393  3C 07                           cmp al, 7
002B3395  0F 85 91 02 00 00               jne 0x1402b362c
002B339B  44 8B 55 80                     mov r10d, dword ptr [rbp - 0x80]
002B339F  41 0F BA E2 1C                  bt r10d, 0x1c
002B33A4  0F 82 B6 09 00 00               jb 0x1402b3d60
002B33AA  C7 44 24 78 02 00 00 00         mov dword ptr [rsp + 0x78], 2
002B33B2  E9 CA F6 FF FF                  jmp 0x1402b2a81
002B33B7  45 33 C0                        xor r8d, r8d
002B33BA  48 8B D3                        mov rdx, rbx
002B33BD  49 8B CC                        mov rcx, r12
002B33C0  E8 A3 2C 0C 00                  call 0x140376068
002B33C5  E9 03 FB FF FF                  jmp 0x1402b2ecd
002B33CA  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
002B33CE  4C 8B 45 A8                     mov r8, qword ptr [rbp - 0x58]
002B33D2  48 8B 55 B8                     mov rdx, qword ptr [rbp - 0x48]
002B33D6  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
002B33DA  E8 D9 17 0B 00                  call 0x140364bb8
002B33DF  85 C0                           test eax, eax
002B33E1  74 03                           je 0x1402b33e6
002B33E3  83 CE 01                        or esi, 1
002B33E6  40 F6 C6 01                     test sil, 1
002B33EA  0F 84 4F 06 00 00               je 0x1402b3a3f
002B33F0  F7 85 38 01 00 00 00 01 00 00   test dword ptr [rbp + 0x138], 0x100
002B33FA  0F 85 8F 03 00 00               jne 0x1402b378f
002B3400  FF 05 4A 1D C4 00               inc dword ptr [rip + 0xc41d4a]
002B3406  33 D2                           xor edx, edx
002B3408  8B DA                           mov ebx, edx
002B340A  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
002B3411  0F 82 59 02 00 00               jb 0x1402b3670
002B3417  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002B341B  48 B9 01 00 00 00 00 00 00 C0   movabs rcx, 0xc000000000000001
002B3425  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
002B3429  C1 E8 10                        shr eax, 0x10
002B342C  24 FD                           and al, 0xfd
002B342E  0C 05                           or al, 5
002B3430  88 44 24 76                     mov byte ptr [rsp + 0x76], al
002B3434  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
002B3438  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
002B343C  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002B3440  48 23 C1                        and rax, rcx
002B3443  48 83 C8 01                     or rax, 1
002B3447  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
002B344B  F0 4D 21 6E 18                  lock and qword ptr [r14 + 0x18], r13
002B3450  E9 3D FA FF FF                  jmp 0x1402b2e92
002B3455  FF 05 4D 1D C4 00               inc dword ptr [rip + 0xc41d4d]
002B345B  48 8B DE                        mov rbx, rsi
002B345E  44 89 25 47 1D C4 00            mov dword ptr [rip + 0xc41d47], r12d
002B3465  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002B3469  48 0F BA E0 3E                  bt rax, 0x3e
002B346E  0F 42 CB                        cmovb ecx, ebx
002B3471  8B C1                           mov eax, ecx
002B3473  E9 07 FD FF FF                  jmp 0x1402b317f
002B3478  48 8B D3                        mov rdx, rbx
002B347B  49 8B CE                        mov rcx, r14
002B347E  E8 05 80 1A 00                  call 0x14045b488
002B3483  48 8B F8                        mov rdi, rax
002B3486  48 85 C0                        test rax, rax
002B3489  0F 85 83 F8 FF FF               jne 0x1402b2d12
002B348F  49 BD FF FF FF FF FF FF FF 7F   movabs r13, 0x7fffffffffffffff
002B3499  F0 4D 21 6E 18                  lock and qword ptr [r14 + 0x18], r13
002B349E  E9 94 FC FF FF                  jmp 0x1402b3137
002B34A3  FF 05 EB 1C C4 00               inc dword ptr [rip + 0xc41ceb]
002B34A9  8B 4C 24 7C                     mov ecx, dword ptr [rsp + 0x7c]
002B34AD  48 8B FE                        mov rdi, rsi
002B34B0  E9 97 FC FF FF                  jmp 0x1402b314c
002B34B5  8B C3                           mov eax, ebx
002B34B7  83 E0 0A                        and eax, 0xa
002B34BA  83 F8 0A                        cmp eax, 0xa
002B34BD  0F 84 17 F9 FF FF               je 0x1402b2dda
002B34C3  84 DB                           test bl, bl
002B34C5  0F 88 0F F9 FF FF               js 0x1402b2dda
002B34CB  83 F8 08                        cmp eax, 8
002B34CE  75 08                           jne 0x1402b34d8
002B34D0  85 C9                           test ecx, ecx
002B34D2  0F 84 1D F9 FF FF               je 0x1402b2df5
002B34D8  83 BD 60 01 00 00 03            cmp dword ptr [rbp + 0x160], 3
002B34DF  0F 85 20 F9 FF FF               jne 0x1402b2e05
002B34E5  F6 C3 04                        test bl, 4
002B34E8  0F 85 07 F9 FF FF               jne 0x1402b2df5
002B34EE  E9 12 F9 FF FF                  jmp 0x1402b2e05
002B34F3  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
002B34FD  48 3B F8                        cmp rdi, rax
002B3500  0F 87 A4 F4 FF FF               ja 0x1402b29aa
002B3506  83 8D 38 01 00 00 08            or dword ptr [rbp + 0x138], 8
002B350D  E9 9F F4 FF FF                  jmp 0x1402b29b1
002B3512  F0 4D 21 6F 18                  lock and qword ptr [r15 + 0x18], r13
002B3517  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002B351B  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
002B351F  C1 E8 10                        shr eax, 0x10
002B3522  24 FD                           and al, 0xfd
002B3524  0C 05                           or al, 5
002B3526  88 44 24 76                     mov byte ptr [rsp + 0x76], al
002B352A  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
002B352E  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
002B3532  E9 AF F9 FF FF                  jmp 0x1402b2ee6
002B3537  84 C0                           test al, al
002B3539  0F 89 D3 F7 FF FF               jns 0x1402b2d12
002B353F  E9 8E F7 FF FF                  jmp 0x1402b2cd2
002B3544  4C 3B 0D 45 BE B7 00            cmp r9, qword ptr [rip + 0xb7be45]
002B354B  0F 87 F2 FD FF FF               ja 0x1402b3343
002B3551  44 8B 9D 38 01 00 00            mov r11d, dword ptr [rbp + 0x138]
002B3558  41 83 CB 08                     or r11d, 8
002B355C  41 F6 C3 01                     test r11b, 1
002B3560  0F 84 22 04 00 00               je 0x1402b3988
002B3566  41 83 CB 02                     or r11d, 2
002B356A  48 3B 3D 17 BE B7 00            cmp rdi, qword ptr [rip + 0xb7be17]
002B3571  45 8B D3                        mov r10d, r11d
002B3574  72 16                           jb 0x1402b358c
002B3576  E8 81 F8 00 00                  call 0x1402c2dfc
002B357B  48 03 05 06 BE B7 00            add rax, qword ptr [rip + 0xb7be06]
002B3582  48 3B F8                        cmp rdi, rax
002B3585  73 05                           jae 0x1402b358c
002B3587  41 0F BA EA 07                  bts r10d, 7
002B358C  41 0F BA EA 0B                  bts r10d, 0xb
002B3591  44 89 95 38 01 00 00            mov dword ptr [rbp + 0x138], r10d
002B3598  E9 83 F4 FF FF                  jmp 0x1402b2a20
002B359D  83 BD 60 01 00 00 02            cmp dword ptr [rbp + 0x160], 2
002B35A4  0F 84 8C F6 FF FF               je 0x1402b2c36
002B35AA  F6 85 38 01 00 00 26            test byte ptr [rbp + 0x138], 0x26
002B35B1  0F 85 7F F6 FF FF               jne 0x1402b2c36
002B35B7  49 BD FF FF FF FF FF FF FF 7F   movabs r13, 0x7fffffffffffffff
002B35C1  F0 4D 21 6E 18                  lock and qword ptr [r14 + 0x18], r13
002B35C6  FF 05 B8 1B C4 00               inc dword ptr [rip + 0xc41bb8]
002B35CC  E9 66 FB FF FF                  jmp 0x1402b3137
002B35D1  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
002B35D5  33 D2                           xor edx, edx
002B35D7  E8 A4 55 00 00                  call 0x1402b8b80
002B35DC  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
002B35E0  48 8B C8                        mov rcx, rax
002B35E3  48 85 C0                        test rax, rax
002B35E6  0F 85 6B 02 00 00               jne 0x1402b3857
002B35EC  FF 05 AE 1B C4 00               inc dword ptr [rip + 0xc41bae]
002B35F2  E9 40 FB FF FF                  jmp 0x1402b3137
002B35F7  33 FF                           xor edi, edi
002B35F9  4C 8B C3                        mov r8, rbx
002B35FC  49 8B D4                        mov rdx, r12
002B35FF  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
002B3603  49 8B CC                        mov rcx, r12
002B3606  44 8D 4F 40                     lea r9d, [rdi + 0x40]
002B360A  E8 D1 2F 0C 00                  call 0x1403765e0
002B360F  E9 D4 F8 FF FF                  jmp 0x1402b2ee8
002B3614  F6 85 38 01 00 00 04            test byte ptr [rbp + 0x138], 4
002B361B  B9 02 00 00 00                  mov ecx, 2
002B3620  0F 45 C1                        cmovne eax, ecx
002B3623  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
002B3627  E9 F3 F6 FF FF                  jmp 0x1402b2d1f
002B362C  3C 02                           cmp al, 2
002B362E  0F 84 49 F4 FF FF               je 0x1402b2a7d
002B3634  39 95 60 01 00 00               cmp dword ptr [rbp + 0x160], edx
002B363A  B8 02 00 00 00                  mov eax, 2
002B363F  0F 44 D0                        cmove edx, eax
002B3642  E9 32 F4 FF FF                  jmp 0x1402b2a79
002B3647  83 7C 24 78 01                  cmp dword ptr [rsp + 0x78], 1
002B364C  0F 85 61 F6 FF FF               jne 0x1402b2cb3
002B3652  8B 85 38 01 00 00               mov eax, dword ptr [rbp + 0x138]
002B3658  A8 10                           test al, 0x10
002B365A  0F 84 65 07 00 00               je 0x1402b3dc5
002B3660  0D 08 01 00 00                  or eax, 0x108
002B3665  89 85 38 01 00 00               mov dword ptr [rbp + 0x138], eax
002B366B  E9 49 F6 FF FF                  jmp 0x1402b2cb9
002B3670  FF C3                           inc ebx
002B3672  85 1D 34 1C D1 00               test dword ptr [rip + 0xd11c34], ebx
002B3678  0F 84 E1 03 00 00               je 0x1402b3a5f
002B367E  F3 90                           pause
002B3680  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002B3684  48 85 C0                        test rax, rax
002B3687  0F 89 7D FD FF FF               jns 0x1402b340a
002B368D  EB E1                           jmp 0x1402b3670
002B368F  F0 4D 21 6F 18                  lock and qword ptr [r15 + 0x18], r13
002B3694  E9 74 F8 FF FF                  jmp 0x1402b2f0d
002B3699  0F B6 95 55 01 00 00            movzx edx, byte ptr [rbp + 0x155]
002B36A0  4D 8B C4                        mov r8, r12
002B36A3  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
002B36A7  83 E2 01                        and edx, 1
002B36AA  E8 3D F9 06 00                  call 0x140322fec
002B36AF  E9 2C FC FF FF                  jmp 0x1402b32e0
002B36B4  83 7C 24 78 00                  cmp dword ptr [rsp + 0x78], 0
002B36B9  0F 85 7A F7 FF FF               jne 0x1402b2e39
002B36BF  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
002B36C3  83 CE 01                        or esi, 1
002B36C6  4C 8B 45 B8                     mov r8, qword ptr [rbp - 0x48]
002B36CA  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
002B36CE  44 89 4D 44                     mov dword ptr [rbp + 0x44], r9d
002B36D2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002B36DB  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
002B36DF  48 89 4D 08                     mov qword ptr [rbp + 8], rcx
002B36E3  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
002B36E7  44 89 4D 38                     mov dword ptr [rbp + 0x38], r9d
002B36EB  44 89 4D 40                     mov dword ptr [rbp + 0x40], r9d
002B36EF  4C 89 4D 48                     mov qword ptr [rbp + 0x48], r9
002B36F3  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
002B36F7  48 89 4D 20                     mov qword ptr [rbp + 0x20], rcx
002B36FB  4C 89 4D 10                     mov qword ptr [rbp + 0x10], r9
002B36FF  48 89 55 00                     mov qword ptr [rbp], rdx
002B3703  4C 89 45 18                     mov qword ptr [rbp + 0x18], r8
002B3707  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
002B370E  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
002B3712  8B 45 80                        mov eax, dword ptr [rbp - 0x80]
002B3715  89 45 3C                        mov dword ptr [rbp + 0x3c], eax
002B3718  49 8B 46 28                     mov rax, qword ptr [r14 + 0x28]
002B371C  49 23 C4                        and rax, r12
002B371F  49 3B C0                        cmp rax, r8
002B3722  0F 84 9A 05 00 00               je 0x1402b3cc2
002B3728  48 8D 4D 00                     lea rcx, [rbp]
002B372C  E8 53 5A F7 FF                  call 0x140229184
002B3731  40 F6 C6 01                     test sil, 1
002B3735  0F 84 04 03 00 00               je 0x1402b3a3f
002B373B  83 7D 38 00                     cmp dword ptr [rbp + 0x38], 0
002B373F  0F 8D A1 FC FF FF               jge 0x1402b33e6
002B3745  83 E6 FE                        and esi, 0xfffffffe
002B3748  E9 99 FC FF FF                  jmp 0x1402b33e6
002B374D  F6 C3 20                        test bl, 0x20
002B3750  0F 85 AB F9 FF FF               jne 0x1402b3101
002B3756  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002B3760  48 8B C8                        mov rcx, rax
002B3763  48 B8 00 00 00 00 40 00 00 00   movabs rax, 0x4000000000
002B376D  48 03 C8                        add rcx, rax
002B3770  4C 3B E1                        cmp r12, rcx
002B3773  0F 82 88 F9 FF FF               jb 0x1402b3101
002B3779  41 B8 80 00 00 00               mov r8d, 0x80
002B377F  48 8B D3                        mov rdx, rbx
002B3782  49 8B CC                        mov rcx, r12
002B3785  E8 F6 F5 FD FF                  call 0x140292d80
002B378A  E9 72 F9 FF FF                  jmp 0x1402b3101
002B378F  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
002B3793  48 B9 01 00 00 00 00 00 00 C0   movabs rcx, 0xc000000000000001
002B379D  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
002B37A1  C1 E8 10                        shr eax, 0x10
002B37A4  24 FD                           and al, 0xfd
002B37A6  0C 05                           or al, 5
002B37A8  88 44 24 76                     mov byte ptr [rsp + 0x76], al
002B37AC  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
002B37B0  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
002B37B4  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002B37B8  48 23 C1                        and rax, rcx
002B37BB  48 83 C8 01                     or rax, 1
002B37BF  33 D2                           xor edx, edx
002B37C1  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
002B37C5  8B DA                           mov ebx, edx
002B37C7  F0 49 0F BA 6F 18 3F            lock bts qword ptr [r15 + 0x18], 0x3f
002B37CE  0F 83 BE F6 FF FF               jae 0x1402b2e92
002B37D4  FF C3                           inc ebx
002B37D6  85 1D D0 1A D1 00               test dword ptr [rip + 0xd11ad0], ebx
002B37DC  0F 84 40 04 00 00               je 0x1402b3c22
002B37E2  F3 90                           pause
002B37E4  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
002B37E8  48 85 C0                        test rax, rax
002B37EB  79 DA                           jns 0x1402b37c7
002B37ED  EB E5                           jmp 0x1402b37d4
002B37EF  48 8B D7                        mov rdx, rdi
002B37F2  48 8B CB                        mov rcx, rbx
002B37F5  48 83 E2 BD                     and rdx, 0xffffffffffffffbd
002B37F9  E8 12 E0 FC FF                  call 0x140281810
002B37FE  41 B8 02 00 00 00               mov r8d, 2
002B3804  E9 FC F4 FF FF                  jmp 0x1402b2d05
002B3809  8B 05 A9 32 D1 00               mov eax, dword ptr [rip + 0xd132a9]
002B380F  A8 40                           test al, 0x40
002B3811  0F 84 27 F8 FF FF               je 0x1402b303e
002B3817  E8 74 BC 05 00                  call 0x14030f490
002B381C  84 C0                           test al, al
002B381E  0F 84 1A F8 FF FF               je 0x1402b303e
002B3824  8B CB                           mov ecx, ebx
002B3826  E8 35 BC 05 00                  call 0x14030f460
002B382B  E9 10 F8 FF FF                  jmp 0x1402b3040
002B3830  8B 05 82 32 D1 00               mov eax, dword ptr [rip + 0xd13282]
002B3836  A8 40                           test al, 0x40
002B3838  0F 84 20 F8 FF FF               je 0x1402b305e
002B383E  E8 4D BC 05 00                  call 0x14030f490
002B3843  84 C0                           test al, al
002B3845  0F 84 13 F8 FF FF               je 0x1402b305e
002B384B  8B CB                           mov ecx, ebx
002B384D  E8 0E BC 05 00                  call 0x14030f460
002B3852  E9 09 F8 FF FF                  jmp 0x1402b3060
002B3857  8B 40 20                        mov eax, dword ptr [rax + 0x20]
002B385A  66 83 F8 02                     cmp ax, 2
002B385E  0F 87 7B 05 00 00               ja 0x1402b3ddf
002B3864  4C 8B 45 A0                     mov r8, qword ptr [rbp - 0x60]
002B3868  49 8B 38                        mov rdi, qword ptr [r8]
002B386B  40 F6 C7 42                     test dil, 0x42
002B386F  74 78                           je 0x1402b38e9
002B3871  33 C0                           xor eax, eax
002B3873  8B D8                           mov ebx, eax
002B3875  F0 48 0F BA 69 18 3F            lock bts qword ptr [rcx + 0x18], 0x3f
002B387C  0F 82 7E 01 00 00               jb 0x1402b3a00
002B3882  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
002B3885  66 83 F8 02                     cmp ax, 2
002B3889  0F 87 6B 05 00 00               ja 0x1402b3dfa
002B388F  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
002B3893  48 8B D7                        mov rdx, rdi
002B3896  48 83 E2 BD                     and rdx, 0xffffffffffffffbd
002B389A  E8 71 DF FC FF                  call 0x140281810
002B389F  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
002B38A3  BA 02 00 00 00                  mov edx, 2
002B38A8  44 8D 42 08                     lea r8d, [rdx + 8]
002B38AC  E8 7F AE FD FF                  call 0x14028e730
002B38B1  48 8B 5D 98                     mov rbx, qword ptr [rbp - 0x68]
002B38B5  48 8B CB                        mov rcx, rbx
002B38B8  E8 13 D5 0B 00                  call 0x140370dd0
002B38BD  F0 4C 21 6B 18                  lock and qword ptr [rbx + 0x18], r13
002B38C2  48 85 C0                        test rax, rax
002B38C5  0F 85 46 05 00 00               jne 0x1402b3e11
002B38CB  33 C0                           xor eax, eax
002B38CD  8B D8                           mov ebx, eax
002B38CF  F0 49 0F BA 6F 18 3F            lock bts qword ptr [r15 + 0x18], 0x3f
002B38D6  0F 82 44 01 00 00               jb 0x1402b3a20
002B38DC  49 8B CF                        mov rcx, r15
002B38DF  E8 EC D4 0B 00                  call 0x140370dd0
002B38E4  F0 4D 21 6F 18                  lock and qword ptr [r15 + 0x18], r13
002B38E9  8B 9D 38 01 00 00               mov ebx, dword ptr [rbp + 0x138]
002B38EF  45 33 C9                        xor r9d, r9d
002B38F2  E9 1F F5 FF FF                  jmp 0x1402b2e16
002B38F7  8B 05 BB 31 D1 00               mov eax, dword ptr [rip + 0xd131bb]
002B38FD  A8 40                           test al, 0x40
002B38FF  0F 84 CB F8 FF FF               je 0x1402b31d0
002B3905  E8 86 BB 05 00                  call 0x14030f490
002B390A  84 C0                           test al, al
002B390C  0F 84 BE F8 FF FF               je 0x1402b31d0
002B3912  41 8B CC                        mov ecx, r12d
002B3915  E8 46 BB 05 00                  call 0x14030f460
002B391A  E9 B3 F8 FF FF                  jmp 0x1402b31d2
002B391F  8B 05 93 31 D1 00               mov eax, dword ptr [rip + 0xd13193]
002B3925  A8 40                           test al, 0x40
002B3927  0F 84 C2 F8 FF FF               je 0x1402b31ef
002B392D  E8 5E BB 05 00                  call 0x14030f490
002B3932  84 C0                           test al, al
002B3934  0F 84 B5 F8 FF FF               je 0x1402b31ef
002B393A  8B CB                           mov ecx, ebx
002B393C  E8 1F BB 05 00                  call 0x14030f460
002B3941  E9 AB F8 FF FF                  jmp 0x1402b31f1
002B3946  F6 C3 20                        test bl, 0x20
002B3949  0F 85 CB F9 FF FF               jne 0x1402b331a
002B394F  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002B3959  48 8B C8                        mov rcx, rax
002B395C  48 B8 00 00 00 00 40 00 00 00   movabs rax, 0x4000000000
002B3966  48 03 C8                        add rcx, rax
002B3969  4C 3B E1                        cmp r12, rcx
002B396C  0F 82 A8 F9 FF FF               jb 0x1402b331a
002B3972  41 B8 80 00 00 00               mov r8d, 0x80
002B3978  48 8B D3                        mov rdx, rbx
002B397B  49 8B CC                        mov rcx, r12
002B397E  E8 FD F3 FD FF                  call 0x140292d80
002B3983  E9 92 F9 FF FF                  jmp 0x1402b331a
002B3988  45 8B D3                        mov r10d, r11d
002B398B  41 83 CA 04                     or r10d, 4
002B398F  41 0F BA EA 0B                  bts r10d, 0xb
002B3994  44 89 95 38 01 00 00            mov dword ptr [rbp + 0x138], r10d
002B399B  E9 80 F0 FF FF                  jmp 0x1402b2a20
002B39A0  8B 05 12 31 D1 00               mov eax, dword ptr [rip + 0xd13112]
002B39A6  A8 40                           test al, 0x40
002B39A8  0F 84 D2 F8 FF FF               je 0x1402b3280
002B39AE  E8 DD BA 05 00                  call 0x14030f490
002B39B3  84 C0                           test al, al
002B39B5  0F 84 C5 F8 FF FF               je 0x1402b3280
002B39BB  41 8B CC                        mov ecx, r12d
002B39BE  E8 9D BA 05 00                  call 0x14030f460
002B39C3  E9 BA F8 FF FF                  jmp 0x1402b3282
002B39C8  33 C0                           xor eax, eax
002B39CA  8B F8                           mov edi, eax
002B39CC  F0 49 0F BA 6F 18 3F            lock bts qword ptr [r15 + 0x18], 0x3f
002B39D3  0F 83 85 F8 FF FF               jae 0x1402b325e
002B39D9  FF C7                           inc edi
002B39DB  85 3D CB 18 D1 00               test dword ptr [rip + 0xd118cb], edi
002B39E1  0F 84 B4 02 00 00               je 0x1402b3c9b
002B39E7  F3 90                           pause
002B39E9  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
002B39ED  48 85 C0                        test rax, rax
002B39F0  79 DA                           jns 0x1402b39cc
002B39F2  EB E5                           jmp 0x1402b39d9
002B39F4  0F 1F 40 00                     nop dword ptr [rax]
002B39F8  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
002B3A00  FF C3                           inc ebx
002B3A02  85 1D A4 18 D1 00               test dword ptr [rip + 0xd118a4], ebx
002B3A08  0F 84 3B 02 00 00               je 0x1402b3c49
002B3A0E  F3 90                           pause
002B3A10  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
002B3A14  48 85 C0                        test rax, rax
002B3A17  0F 89 58 FE FF FF               jns 0x1402b3875
002B3A1D  EB E1                           jmp 0x1402b3a00
002B3A1F  90                              nop
002B3A20  FF C3                           inc ebx
002B3A22  85 1D 84 18 D1 00               test dword ptr [rip + 0xd11884], ebx
002B3A28  0F 84 46 02 00 00               je 0x1402b3c74
002B3A2E  F3 90                           pause
002B3A30  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
002B3A34  48 85 C0                        test rax, rax
002B3A37  0F 89 92 FE FF FF               jns 0x1402b38cf
002B3A3D  EB E1                           jmp 0x1402b3a20
002B3A3F  F7 85 38 01 00 00 00 01 00 00   test dword ptr [rbp + 0x138], 0x100
002B3A49  0F 84 E8 F6 FF FF               je 0x1402b3137
002B3A4F  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
002B3A53  B2 11                           mov dl, 0x11
002B3A55  E8 36 26 F9 FF                  call 0x140246090
002B3A5A  E9 D8 F6 FF FF                  jmp 0x1402b3137
002B3A5F  8B 05 53 30 D1 00               mov eax, dword ptr [rip + 0xd13053]
002B3A65  A8 40                           test al, 0x40
002B3A67  0F 84 11 FC FF FF               je 0x1402b367e
002B3A6D  E8 1E BA 05 00                  call 0x14030f490
002B3A72  84 C0                           test al, al
002B3A74  0F 84 04 FC FF FF               je 0x1402b367e
002B3A7A  8B CB                           mov ecx, ebx
002B3A7C  E8 DF B9 05 00                  call 0x14030f460
002B3A81  E9 FA FB FF FF                  jmp 0x1402b3680
002B3A86  33 D2                           xor edx, edx
002B3A88  48 8D 8D C0 00 00 00            lea rcx, [rbp + 0xc0]
002B3A8F  44 8D 42 70                     lea r8d, [rdx + 0x70]
002B3A93  E8 A8 31 41 00                  call 0x1406c6c40
002B3A98  49 8B CE                        mov rcx, r14
002B3A9B  E8 90 D4 FF FF                  call 0x1402b0f30
002B3AA0  44 0F B6 85 55 01 00 00         movzx r8d, byte ptr [rbp + 0x155]
002B3AA8  48 8D 8D C0 00 00 00            lea rcx, [rbp + 0xc0]
002B3AAF  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
002B3AB3  FF C0                           inc eax
002B3AB5  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
002B3ABA  41 83 E0 01                     and r8d, 1
002B3ABE  48 C7 44 24 58 01 00 00 00      mov qword ptr [rsp + 0x58], 1
002B3AC7  33 C9                           xor ecx, ecx
002B3AC9  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
002B3ACE  4C 8B CF                        mov r9, rdi
002B3AD1  C7 44 24 48 09 00 00 00         mov dword ptr [rsp + 0x48], 9
002B3AD9  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
002B3ADE  48 8B 8D A8 01 00 00            mov rcx, qword ptr [rbp + 0x1a8]
002B3AE5  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
002B3AEA  49 8B CD                        mov rcx, r13
002B3AED  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
002B3AF1  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
002B3AF6  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
002B3AFA  E8 C1 2C 18 00                  call 0x1404367c0
002B3AFF  48 8D 8D C0 00 00 00            lea rcx, [rbp + 0xc0]
002B3B06  E8 25 C6 07 00                  call 0x140330130
002B3B0B  48 39 B5 28 01 00 00            cmp qword ptr [rbp + 0x128], rsi
002B3B12  0F 84 56 02 00 00               je 0x1402b3d6e
002B3B18  4C 8B AD 18 01 00 00            mov r13, qword ptr [rbp + 0x118]
002B3B1F  4D 85 ED                        test r13, r13
002B3B22  74 1E                           je 0x1402b3b42
002B3B24  49 8B 45 00                     mov rax, qword ptr [r13]
002B3B28  48 83 AD 28 01 00 00 01         sub qword ptr [rbp + 0x128], 1
002B3B30  48 89 85 18 01 00 00            mov qword ptr [rbp + 0x118], rax
002B3B37  75 09                           jne 0x1402b3b42
002B3B39  33 DB                           xor ebx, ebx
002B3B3B  48 89 9D 20 01 00 00            mov qword ptr [rbp + 0x120], rbx
002B3B42  4D 8B FD                        mov r15, r13
002B3B45  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002B3B4F  48 8B C0                        mov rax, rax
002B3B52  4C 2B E8                        sub r13, rax
002B3B55  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
002B3B5F  49 C1 FD 04                     sar r13, 4
002B3B63  4C 0F AF E8                     imul r13, rax
002B3B67  4C 89 6D A8                     mov qword ptr [rbp - 0x58], r13
002B3B6B  E9 61 F0 FF FF                  jmp 0x1402b2bd1
002B3B70  48 8B 55 88                     mov rdx, qword ptr [rbp - 0x78]
002B3B74  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
002B3B78  E8 53 0E 18 00                  call 0x1404349d0
002B3B7D  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
002B3B81  48 85 C0                        test rax, rax
002B3B84  0F 84 93 F5 FF FF               je 0x1402b311d
002B3B8A  48 8D 98 C8 00 00 00            lea rbx, [rax + 0xc8]
002B3B91  48 8B CB                        mov rcx, rbx
002B3B94  E8 97 52 F9 FF                  call 0x140248e30
002B3B99  4C 8B 45 88                     mov r8, qword ptr [rbp - 0x78]
002B3B9D  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
002B3BA1  49 8B D0                        mov rdx, r8
002B3BA4  E8 27 0E 18 00                  call 0x1404349d0
002B3BA9  48 39 45 C8                     cmp qword ptr [rbp - 0x38], rax
002B3BAD  75 13                           jne 0x1402b3bc2
002B3BAF  49 8B D4                        mov rdx, r12
002B3BB2  49 8B C8                        mov rcx, r8
002B3BB5  E8 D6 D4 1B 00                  call 0x140471090
002B3BBA  85 C0                           test eax, eax
002B3BBC  0F 85 B1 F1 FF FF               jne 0x1402b2d73
002B3BC2  FF 05 B0 15 C4 00               inc dword ptr [rip + 0xc415b0]
002B3BC8  48 8B CB                        mov rcx, rbx
002B3BCB  E8 C0 69 F9 FF                  call 0x14024a590
002B3BD0  E9 4E F5 FF FF                  jmp 0x1402b3123
002B3BD5  48 8D 55 E0                     lea rdx, [rbp - 0x20]
002B3BD9  E8 8A 0F FE FF                  call 0x140294b68
002B3BDE  48 8B 5D E0                     mov rbx, qword ptr [rbp - 0x20]
002B3BE2  8B F8                           mov edi, eax
002B3BE4  E9 09 F5 FF FF                  jmp 0x1402b30f2
002B3BE9  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
002B3BED  48 81 C1 C8 00 00 00            add rcx, 0xc8
002B3BF4  E8 97 69 F9 FF                  call 0x14024a590
002B3BF9  E9 32 F3 FF FF                  jmp 0x1402b2f30
002B3BFE  49 8B D5                        mov rdx, r13
002B3C01  49 8B CF                        mov rcx, r15
002B3C04  E8 B7 03 0B 00                  call 0x140363fc0
002B3C09  E9 8E F1 FF FF                  jmp 0x1402b2d9c
002B3C0E  48 8D 55 E8                     lea rdx, [rbp - 0x18]
002B3C12  E8 51 0F FE FF                  call 0x140294b68
002B3C17  48 8B 5D E8                     mov rbx, qword ptr [rbp - 0x18]
002B3C1B  8B F8                           mov edi, eax
002B3C1D  E9 E9 F6 FF FF                  jmp 0x1402b330b
002B3C22  8B 05 90 2E D1 00               mov eax, dword ptr [rip + 0xd12e90]
002B3C28  A8 40                           test al, 0x40
002B3C2A  0F 84 B2 FB FF FF               je 0x1402b37e2
002B3C30  E8 5B B8 05 00                  call 0x14030f490
002B3C35  84 C0                           test al, al
002B3C37  0F 84 A5 FB FF FF               je 0x1402b37e2
002B3C3D  8B CB                           mov ecx, ebx
002B3C3F  E8 1C B8 05 00                  call 0x14030f460
002B3C44  E9 9B FB FF FF                  jmp 0x1402b37e4
002B3C49  8B 05 69 2E D1 00               mov eax, dword ptr [rip + 0xd12e69]
002B3C4F  A8 40                           test al, 0x40
002B3C51  0F 84 B7 FD FF FF               je 0x1402b3a0e
002B3C57  E8 34 B8 05 00                  call 0x14030f490
002B3C5C  84 C0                           test al, al
002B3C5E  0F 84 8D 01 00 00               je 0x1402b3df1
002B3C64  8B CB                           mov ecx, ebx
002B3C66  E8 F5 B7 05 00                  call 0x14030f460
002B3C6B  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
002B3C6F  E9 9C FD FF FF                  jmp 0x1402b3a10
002B3C74  8B 05 3E 2E D1 00               mov eax, dword ptr [rip + 0xd12e3e]
002B3C7A  A8 40                           test al, 0x40
002B3C7C  0F 84 AC FD FF FF               je 0x1402b3a2e
002B3C82  E8 09 B8 05 00                  call 0x14030f490
002B3C87  84 C0                           test al, al
002B3C89  0F 84 9F FD FF FF               je 0x1402b3a2e
002B3C8F  8B CB                           mov ecx, ebx
002B3C91  E8 CA B7 05 00                  call 0x14030f460
002B3C96  E9 95 FD FF FF                  jmp 0x1402b3a30
002B3C9B  8B 05 17 2E D1 00               mov eax, dword ptr [rip + 0xd12e17]
002B3CA1  A8 40                           test al, 0x40
002B3CA3  0F 84 3E FD FF FF               je 0x1402b39e7
002B3CA9  E8 E2 B7 05 00                  call 0x14030f490
002B3CAE  84 C0                           test al, al
002B3CB0  0F 84 31 FD FF FF               je 0x1402b39e7
002B3CB6  8B CF                           mov ecx, edi
002B3CB8  E8 A3 B7 05 00                  call 0x14030f460
002B3CBD  E9 27 FD FF FF                  jmp 0x1402b39e9
002B3CC2  8B 82 B8 00 00 00               mov eax, dword ptr [rdx + 0xb8]
002B3CC8  C1 E8 18                        shr eax, 0x18
002B3CCB  A8 02                           test al, 2
002B3CCD  74 08                           je 0x1402b3cd7
002B3CCF  83 E6 FE                        and esi, 0xfffffffe
002B3CD2  E9 5A FA FF FF                  jmp 0x1402b3731
002B3CD7  48 8B 5D D8                     mov rbx, qword ptr [rbp - 0x28]
002B3CDB  F0 0F BA AB FC 05 00 00 01      lock bts dword ptr [rbx + 0x5fc], 1
002B3CE4  0F 82 61 01 00 00               jb 0x1402b3e4b
002B3CEA  8B 8D 38 01 00 00               mov ecx, dword ptr [rbp + 0x138]
002B3CF0  48 8B 55 30                     mov rdx, qword ptr [rbp + 0x30]
002B3CF4  0F BA E9 09                     bts ecx, 9
002B3CF8  89 8D 38 01 00 00               mov dword ptr [rbp + 0x138], ecx
002B3CFE  48 8B 42 28                     mov rax, qword ptr [rdx + 0x28]
002B3D02  48 C1 E8 0C                     shr rax, 0xc
002B3D06  49 3B C0                        cmp rax, r8
002B3D09  75 37                           jne 0x1402b3d42
002B3D0B  45 33 C0                        xor r8d, r8d
002B3D0E  48 8D 8D 48 01 00 00            lea rcx, [rbp + 0x148]
002B3D15  B2 11                           mov dl, 0x11
002B3D17  E8 74 95 FC FF                  call 0x14027d290
002B3D1C  8B 55 40                        mov edx, dword ptr [rbp + 0x40]
002B3D1F  4C 8D 45 00                     lea r8, [rbp]
002B3D23  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
002B3D27  E8 E0 1B 1B 00                  call 0x14046590c
002B3D2C  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
002B3D30  E8 6B FB 06 00                  call 0x1403238a0
002B3D35  F0 83 A3 FC 05 00 00 FD         lock and dword ptr [rbx + 0x5fc], 0xfffffffd
002B3D3D  E9 EF F9 FF FF                  jmp 0x1402b3731
002B3D42  C7 45 40 01 00 00 00            mov dword ptr [rbp + 0x40], 1
002B3D49  0F BA E9 0D                     bts ecx, 0xd
002B3D4D  48 8B 82 08 05 00 00            mov rax, qword ptr [rdx + 0x508]
002B3D54  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
002B3D58  89 8D 38 01 00 00               mov dword ptr [rbp + 0x138], ecx
002B3D5E  EB AB                           jmp 0x1402b3d0b
002B3D60  FF 05 AA 14 C4 00               inc dword ptr [rip + 0xc414aa]
002B3D66  48 8B F9                        mov rdi, rcx
002B3D69  E9 DE F3 FF FF                  jmp 0x1402b314c
002B3D6E  FF 05 24 14 C4 00               inc dword ptr [rip + 0xc41424]
002B3D74  E9 30 F7 FF FF                  jmp 0x1402b34a9
002B3D79  48 8B 7D 90                     mov rdi, qword ptr [rbp - 0x70]
002B3D7D  BB 01 00 00 00                  mov ebx, 1
002B3D82  E9 1E F4 FF FF                  jmp 0x1402b31a5
002B3D87  0F BA E3 1C                     bt ebx, 0x1c
002B3D8B  0F 82 6C EE FF FF               jb 0x1402b2bfd
002B3D91  FF 05 89 14 C4 00               inc dword ptr [rip + 0xc41489]
002B3D97  49 BD FF FF FF FF FF FF FF 7F   movabs r13, 0x7fffffffffffffff
002B3DA1  F0 4D 21 6E 18                  lock and qword ptr [r14 + 0x18], r13
002B3DA6  E9 8C F3 FF FF                  jmp 0x1402b3137
002B3DAB  49 BD FF FF FF FF FF FF FF 7F   movabs r13, 0x7fffffffffffffff
002B3DB5  F0 4D 21 6E 18                  lock and qword ptr [r14 + 0x18], r13
002B3DBA  FF 05 C0 13 C4 00               inc dword ptr [rip + 0xc413c0]
002B3DC0  E9 72 F3 FF FF                  jmp 0x1402b3137
002B3DC5  FF 05 D1 13 C4 00               inc dword ptr [rip + 0xc413d1]
002B3DCB  49 BD FF FF FF FF FF FF FF 7F   movabs r13, 0x7fffffffffffffff
002B3DD5  F0 4D 21 6E 18                  lock and qword ptr [r14 + 0x18], r13
002B3DDA  E9 58 F3 FF FF                  jmp 0x1402b3137
002B3DDF  FF 05 BF 13 C4 00               inc dword ptr [rip + 0xc413bf]
002B3DE5  B2 11                           mov dl, 0x11
002B3DE7  E8 A4 22 F9 FF                  call 0x140246090
002B3DEC  E9 46 F3 FF FF                  jmp 0x1402b3137
002B3DF1  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
002B3DF5  E9 14 FC FF FF                  jmp 0x1402b3a0e
002B3DFA  FF 05 A4 13 C4 00               inc dword ptr [rip + 0xc413a4]
002B3E00  F0 4C 21 69 18                  lock and qword ptr [rcx + 0x18], r13
002B3E05  B2 11                           mov dl, 0x11
002B3E07  E8 84 22 F9 FF                  call 0x140246090
002B3E0C  E9 26 F3 FF FF                  jmp 0x1402b3137
002B3E11  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
002B3E15  41 B8 01 00 00 00               mov r8d, 1
002B3E1B  48 8B 15 66 C2 B7 00            mov rdx, qword ptr [rip + 0xb7c266]
002B3E22  48 C1 E9 2B                     shr rcx, 0x2b
002B3E26  81 E1 FF 03 00 00               and ecx, 0x3ff
002B3E2C  48 8B 0C CA                     mov rcx, qword ptr [rdx + rcx*8]
002B3E30  48 8B D0                        mov rdx, rax
002B3E33  E8 98 01 FD FF                  call 0x140283fd0
002B3E38  E9 8E FA FF FF                  jmp 0x1402b38cb
002B3E3D  F6 C3 04                        test bl, 4
002B3E40  0F 85 79 F8 FF FF               jne 0x1402b36bf
002B3E46  E9 E2 EF FF FF                  jmp 0x1402b2e2d
002B3E4B  83 E6 FE                        and esi, 0xfffffffe
002B3E4E  E9 DE F8 FF FF                  jmp 0x1402b3731
002B3E53  80 FB 11                        cmp bl, 0x11
002B3E56  BA 48 00 00 00                  mov edx, 0x48
002B3E5B  B8 0C 00 00 00                  mov eax, 0xc
002B3E60  49 8B CE                        mov rcx, r14
002B3E63  0F 45 D0                        cmovne edx, eax
002B3E66  E8 95 31 15 00                  call 0x140407000
002B3E6B  E9 AF F0 FF FF                  jmp 0x1402b2f1f
002B3E70  49 BD FF FF FF FF FF FF FF 7F   movabs r13, 0x7fffffffffffffff
002B3E7A  F0 4D 21 6E 18                  lock and qword ptr [r14 + 0x18], r13
002B3E7F  FF 05 07 13 C4 00               inc dword ptr [rip + 0xc41307]
002B3E85  E9 AD F2 FF FF                  jmp 0x1402b3137
002B3E8A  48 8B CF                        mov rcx, rdi
002B3E8D  E8 1A C1 1F 00                  call 0x1404affac
002B3E92  85 C0                           test eax, eax
002B3E94  0F 84 54 7A 42 00               je 0x1406db8ee
002B3E9A  48 8B CF                        mov rcx, rdi
002B3E9D  E8 52 FA FD FF                  call 0x1402938f4
002B3EA2  90                              nop
002B3EA3  E9 46 7A 42 00                  jmp 0x1406db8ee
002B3EA8  BB 02 00 00 00                  mov ebx, 2
002B3EAD  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
002B3EB1  48 0F BA E0 3E                  bt rax, 0x3e
002B3EB6  0F 82 C3 7A 42 00               jb 0x1406db97f
002B3EBC  FF 05 86 12 C4 00               inc dword ptr [rip + 0xc41286]
002B3EC2  E9 A1 F2 FF FF                  jmp 0x1402b3168
002B3EC7  48 8B CF                        mov rcx, rdi
002B3ECA  E8 11 0C 08 00                  call 0x140334ae0
002B3ECF  E9 A9 F2 FF FF                  jmp 0x1402b317d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiStealPage(__int64 a1, int a2, int a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1C0;
    unsigned int v_stack_m1C4;
    unsigned int v_stack_m1C8;
    unsigned int v_stack_m1CC;
    unsigned int v_stack_m1D0;
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
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned int v_stack_m288;
    unsigned int v_stack_m28C;
    unsigned int v_stack_m290;
    unsigned __int8 v_stack_m292;
    unsigned int v_stack_m294;
    unsigned __int8 v_stack_m298;
    unsigned __int64 v_stack_m2E8;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_mA8;
    unsigned __int8 v_stack_mB3;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p74;
    unsigned __int8 v_stack_p76;
    unsigned int v_stack_p78;
    unsigned int v_stack_p7C;

    v_rsp = (v_rsp) - (712);
    result = (*(unsigned __int64 *)(v_rip + 11894349)) ^ (v_rsp);
    v_stack_m58 = result;
    v_stack_m298 = (unsigned __int8)(a2);
    a2 = 0;
    v_stack_m288 = a3;
    v_stack_m238 = a4;
    v_stack_m218 = a6;
    result = memset(v_stack_mD4, a2, a2 + 116, a4);
    v_r10 = 0;
    v_stack_mD8 = (unsigned int)((unsigned int)(a3));
    v_stack_m260 = -1;
    v_stack_m60 = -1;
    v_r15 = (*(unsigned __int64 *)(a1 + 8)) | (-1);
    v_stack_m278 = 0;
    v_stack_m240 = 0;
    v_rdi = (v_r15) << (25);
    v_stack_m268 = v_r15;
    result = (v_r11) << (25);
    v_rdi = (v_rdi) - (result);
    v_rdi = (v_rdi) >> (16);
    v_stack_m280 = v_rdi;
    result = MiGetLeafVa(v_rdi, a2, a2 + 116, a4);
    if (v_rdi >= v_r11) goto loc_002B34F3;
loc_002B29AA:
loc_002B29B1:
    v_stack_m230 = 0;
    v_r12 = (a1) - (v_r11);
    v_r12 = (v_r12) >> (4);
    v_r12 = (v_r12) * (v_r11);
    result = (*(unsigned __int64 *)(a1 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_m250 = v_r12;
    v_stack_m270 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12048035) + result * 8);
    if (result >= result) goto loc_002B3336;
    v_stack_mD0 = (unsigned int)((unsigned int)(v_stack_mD0));
loc_002B2A20:
    if (result >= result) goto loc_002B334F;
    v_stack_m2E8 = v_stack_mD8;
    result = MiLockStealUserVm(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12048035) + result * 8), a1, (unsigned __int8)((unsigned __int8)(a2)), v_r15);
    if (((unsigned int)(result)) != 1) goto loc_002B3455;
    a2 = 0;
    v_stack_m28C = 0;
    v_stack_m258 = v_stack_mC0;
    v_stack_m230 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
loc_002B2A79:
    v_stack_m290 = 0;
loc_002B2A7D:
loc_002B2A81:
    a2 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (16));
    v_r15 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    v_stack_m294 = (unsigned int)(v_r15);
    if (condition_is_below) goto loc_002B2B0E;
    result = MiGetPfnChannel(a1, a2, v_stack_mC0, v_r15);
    result = MiPageToNode(v_r12, a2, v_stack_mC0, v_r15);
    v_rbx = (unsigned int)(((unsigned __int8)(result)) & (1));
    result = (unsigned int)((result) & (63));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) << (9));
    a2 = (unsigned int)((a2) | ((unsigned int)(result)));
    a2 = (unsigned int)((a2) | (384));
    a2 = (unsigned int)((a2) + (a2));
    a2 = (unsigned int)((a2) | ((unsigned int)(v_rbx)));
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m288)) & (0x1000000ULL));
    a2 = (unsigned int)((a2) << (8));
    a2 = (unsigned int)((a2) | (0));
    v_rbx = (unsigned int)((v_rbx) >> (9));
    if (((v_stack_m288) & (0x2000000ULL)) == 0) goto loc_002B2B48;
    goto loc_002B2B48;
loc_002B2B0E:
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) >> (16));
    a4 = (unsigned int)((a4) & (3));
    a2 = 0;
    a2 = (unsigned int)((a2) ^ ((unsigned int)((unsigned int)(a5))));
    a2 = (unsigned int)(((unsigned __int8)(a2)) ^ ((unsigned int)((unsigned int)(a5))));
loc_002B2B48:
    if (v_stack_m218 == 0) goto loc_002B2B88;
    v_stack_m260 = *(unsigned __int64 *)(v_stack_m218);
    if ((*(unsigned __int64 *)(v_stack_m218)) == -1) goto loc_002B2B84;
    v_r15 = (*(unsigned __int64 *)(v_stack_m218) * 2) + (*(unsigned __int64 *)(v_stack_m218));
    v_r15 = (v_r15) << (4);
    v_r15 = (v_r15) + (v_stack_m218);
    goto loc_002B2BD1;
loc_002B2B84:
loc_002B2B88:
    if (v_stack_m60 != -1) goto loc_002B3A86;
    result = MiGetPage(v_stack_m270, a2, (unsigned int)((unsigned int)((unsigned int)(0x3001ULL))), v_rip + 12038531);
    v_stack_m260 = result;
    if (result == -1) goto loc_002B34A3;
    v_r15 = (result * 2) + (result);
    v_r15 = (v_r15) << (4);
    v_r15 = (v_r15) + (result);
loc_002B2BD1:
    if (v_r15 == a1) goto loc_002B3D79;
    v_rdi = 0;
loc_002B2BDE:
    if (condition_is_below) goto loc_002B3030;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (64)) != 0) goto loc_002B3D87;
loc_002B2BFD:
    if (((*(unsigned __int64 *)(v_rip + 13713024)) & (0x4000ULL)) != 0) goto loc_002B3200;
loc_002B2C0E:
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(a1 + 32)))) != 1) goto loc_002B3DAB;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (8)) != 0) goto loc_002B359D;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1))) & (1)) == 0) goto loc_002B359D;
loc_002B2C36:
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 34)) & (7));
    if (((unsigned __int8)(result)) != 6) goto loc_002B3E70;
    result = (*(unsigned __int64 *)(a1 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (v_stack_m270 != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12047416) + result * 8))) goto loc_002B3E70;
    result = (unsigned int)(v_stack_mD0);
    if ((((unsigned __int8)((unsigned int)(v_stack_mD0))) & (32)) == 0) {
        a1 = v_stack_m268;
        result = MI_READ_PTE_LOCK_FREE(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12047416) + result * 8), (unsigned int)((unsigned int)((unsigned int)(0x3001ULL))), v_rip + 12038531);
        v_rdi = result;
        result = v_stack_mD0;
    }
    if (v_stack_mA8 == 3) goto loc_002B2CB9;
    result = (*(unsigned __int64 *)(a1 + 24)) & (a1);
    if (result > 1) goto loc_002B3647;
loc_002B2CB3:
loc_002B2CB9:
    if (v_stack_mA8 == 2) goto loc_002B2D12;
    if ((((unsigned __int8)((unsigned int)(v_stack_mD0))) & (32)) != 0) goto loc_002B3478;
    if ((((unsigned __int8)((unsigned int)(v_stack_mD0))) & (8)) != 0) goto loc_002B3537;
loc_002B2CD2:
    if ((((unsigned __int8)(v_rdi)) & (66)) == 0) goto loc_002B3291;
loc_002B2CDC:
    if (sign_flag) goto loc_002B37EF;
    result = (unsigned int)(((unsigned int)(v_stack_mD0)) | (64));
    v_stack_mD0 = (unsigned int)(result);
    result = (v_rdi) & (-2);
    *(unsigned __int64 *)(v_stack_m268) = result;
    v_rsi = (unsigned int)((8) | (2));
loc_002B2D05:
    result = MiFlushSingleTbEntry(v_stack_m280, (unsigned int)(v_stack_m290), 1, v_rip + 12038531);
loc_002B2D12:
    if (((unsigned int)((unsigned int)(v_stack_m290))) == 1) goto loc_002B3614;
loc_002B2D1F:
    v_rbx = 0;
loc_002B2D21:
    if (condition_is_below) goto loc_002B3050;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 32))) >> (16));
    result = (unsigned int)(((unsigned __int8)(result)) >> (6));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(v_stack_m294)))) {
        a3 = 9;
        a1 = v_r15;
        result = MiChangePageAttribute(a1, (unsigned int)(v_stack_m294), a3, v_rip + 12038531);
    }
    result = (*(unsigned __int64 *)(v_r15 + 24)) & (a1);
    *(unsigned __int64 *)(v_r15 + 24) = result;
    if (v_stack_mA8 == 2) goto loc_002B3B70;
loc_002B2D73:
    result = MiCopyPfnEntryEx(v_r15, a1, a3, v_rip + 12038531);
    result = (*(unsigned __int64 *)(a1 + 40)) & (v_r12);
    v_rsi = (unsigned int)((v_rsi) | (4));
    if (result == v_stack_m250) goto loc_002B3BFE;
loc_002B2D9C:
    if ((((unsigned __int8)((unsigned int)(v_stack_mD0))) & (32)) != 0) goto loc_002B2E05;
    if (v_stack_mA8 == 2) goto loc_002B2E05;
    if (v_stack_mA8 < 2) goto loc_002B2DF5;
    if ((((unsigned __int8)((unsigned int)(v_stack_mD0))) & (8)) != 0) goto loc_002B34B5;
    if ((unsigned int)((unsigned int)(v_stack_m290)) != 0) goto loc_002B34B5;
loc_002B2DDA:
    v_stack_m294 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (16));
    result = (unsigned __int8)((result) & (253));
    result = (unsigned __int8)((result) | (5));
    v_stack_m292 = (unsigned __int8)(result);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_m294));
loc_002B2DF5:
    v_stack_m298 = 17;
loc_002B2E05:
    if (condition_is_below) goto loc_002B35D1;
    a4 = 0;
    v_stack_m270 = 0;
loc_002B2E16:
    if (condition_is_below) goto loc_002B33CA;
    if (v_stack_mA8 == 3) goto loc_002B3E3D;
loc_002B2E2D:
    result = (unsigned __int8)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mD0)))) & (10));
    if (((unsigned __int8)(result)) == 8) goto loc_002B36B4;
loc_002B2E39:
    v_rbx = (unsigned int)(((unsigned int)(v_stack_mD0)) & (0x1000ULL));
    v_rbx = (unsigned int)((v_rbx) >> (11));
    if (((unsigned __int8)(v_stack_m298)) == 17) goto loc_002B2E6B;
    v_rbx = (unsigned int)((v_rbx) | (4));
loc_002B2E58:
    if (condition_is_below) goto loc_002B31C0;
loc_002B2E6B:
    result = MiCopyPage(v_stack_m260, v_stack_m250, (unsigned int)((unsigned int)(v_rbx)), a4);
    if ((((unsigned __int8)(v_rbx)) & (4)) != 0) {
    }
    if (((v_stack_mD0) & (32)) == 0) goto loc_002B3004;
loc_002B2E92:
    result = (v_stack_m260) << (12);
    v_rbx = (result) ^ (v_rdi);
    v_rbx = (v_rbx) & (v_stack_m260);
    v_rbx = (v_rbx) ^ (result);
    if (((v_stack_mD0) & (32)) != 0) goto loc_002B306F;
    if (condition_is_above_or_equal) goto loc_002B30CE;
loc_002B2ECD:
    result = (unsigned int)(v_stack_mD0);
    if ((((unsigned __int8)(v_rsi)) & (2)) == 0) {
        a2 = v_stack_m290;
        a3 = 64;
        a1 = v_stack_m280;
        result = MiFlushSingleTbEntry(a1, a2, a3, a4);
    }
    v_rdi = 0;
loc_002B2EE8:
    if (((v_stack_mD0) & (256)) != 0) goto loc_002B3226;
    result = (unsigned __int8)(((unsigned int)(v_stack_mD0)) & (80));
    if (((unsigned __int8)(result)) == 16) goto loc_002B368F;
loc_002B2F0D:
    result = (*(unsigned __int64 *)(a1 + 40)) >> (60);
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) == 3) goto loc_002B3E53;
loc_002B2F1F:
    if (v_stack_mA8 == 2) goto loc_002B3BE9;
loc_002B2F30:
    if (((unsigned __int8)(v_stack_m298)) != 17) goto loc_002B2F44;
loc_002B2F37:
    if (((unsigned __int8)(v_stack_m298)) < 17) goto loc_002B31E1;
loc_002B2F44:
    v_stack_m1A8 = 0;
    v_stack_m180 = *(unsigned __int64 *)(a1 + 40);
    a1 = (*(unsigned __int64 *)(a1 + 40)) & (a3);
    v_stack_m1A0 = v_xmm0;
    v_stack_m190 = v_xmm1;
    v_stack_m178 = v_xmm0;
    v_stack_m168 = v_xmm0;
    v_stack_m158 = v_xmm0;
    v_stack_m150 = *(unsigned __int64 *)(a1 + 40);
    if ((*(unsigned __int64 *)(a1 + 40)) == (*(unsigned __int64 *)(a1 + 40))) goto loc_002B2FBF;
loc_002B2F9D:
    v_stack_m180 = *(unsigned __int64 *)(a1 + 40);
    a1 = (*(unsigned __int64 *)(a1 + 40)) & (a3);
    v_stack_m150 = *(unsigned __int64 *)(a1 + 40);
    if ((*(unsigned __int64 *)(a1 + 40)) != (*(unsigned __int64 *)(a1 + 40))) goto loc_002B2F9D;
loc_002B2FBF:
    result = MiClearPfnReuseFields(a1, *(unsigned __int64 *)(a1 + 40), a3, a4);
    v_stack_m294 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    v_stack_m294 = 0;
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_m294));
    result = (*(unsigned __int64 *)(a1 + 24)) & (a1);
    *(unsigned __int64 *)(a1 + 24) = result;
    goto loc_002B31A5;
loc_002B3004:
    if (((unsigned __int8)(v_stack_m298)) == 17) goto loc_002B2E92;
    v_stack_m294 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (16));
    result = (unsigned __int8)((result) & (253));
    result = (unsigned __int8)((result) | (5));
    v_stack_m292 = (unsigned __int8)(result);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_m294));
    goto loc_002B2E92;
loc_002B3030:
    v_rbx = (unsigned int)((1) + 1);
    if (((*(unsigned int *)(v_rip + 13705844)) & ((unsigned int)(v_rbx))) == 0) goto loc_002B3809;
loc_002B303E:
loc_002B3040:
    if (!sign_flag) goto loc_002B2BDE;
    goto loc_002B3030;
loc_002B3050:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 13705812)) & ((unsigned int)(v_rbx))) == 0) goto loc_002B3830;
loc_002B305E:
loc_002B3060:
    if (!sign_flag) goto loc_002B2D21;
    goto loc_002B3050;
loc_002B306F:
    v_rbx = (v_rbx) | (32);
    a2 = 0;
loc_002B3078:
    if (condition_is_below) goto loc_002B3270;
    if (((*(unsigned __int64 *)(v_rip + 13711864)) & (0x2000000ULL)) != 0) {
    }
    if (((*(unsigned __int64 *)(v_rip + 13711864)) & (0x2000000ULL)) == 0) goto loc_002B3512;
    v_stack_m294 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 32))) >> (16));
    result = (unsigned __int8)((result) & (253));
    result = (unsigned __int8)((result) | (5));
    v_stack_m292 = (unsigned __int8)(result);
    *(unsigned int *)(v_r15 + 32) = (unsigned int)((unsigned int)(v_stack_m294));
    goto loc_002B3137;
loc_002B30CE:
    if ((((unsigned __int8)((unsigned int)(v_stack_m294))) & (64)) == 0) goto loc_002B3242;
    a2 = 0;
    v_stack_m228 = v_rbx;
    result = MiPteInShadowRange(v_stack_m268, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_002B3BD5;
loc_002B30F2:
    if (condition_is_below) goto loc_002B374D;
loc_002B3101:
    *(unsigned __int64 *)(v_stack_m268) = v_rbx;
    if (0 == 0) goto loc_002B2ECD;
    result = MiWritePteShadow(v_stack_m268, v_rbx, a3, a4);
    goto loc_002B2ECD;
loc_002B311D:
loc_002B3123:
loc_002B3137:
    if (v_r15 != 0) goto loc_002B3E8A;
    if (((unsigned int)((unsigned int)(v_stack_m28C))) == 1) goto loc_002B31A3;
loc_002B314C:
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 34)) & (7));
    if (((unsigned __int8)(result)) != 6) goto loc_002B3EA8;
    if (((unsigned int)((unsigned int)(v_stack_m28C))) == 2) goto loc_002B3EAD;
loc_002B3168:
    result = MiUnlockStealVm(v_stack_mD8, v_rbx, a3, a4);
    if (v_r15 != 0) goto loc_002B3EC7;
loc_002B317D:
loc_002B317F:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rbx, a3, a4);
    v_rsp = (v_rsp) + (712);
    return result;
loc_002B31A3:
loc_002B31A5:
    if (v_stack_m218 != 0) {
        result = v_stack_m260;
        *(unsigned __int64 *)(v_stack_m218) = result;
    }
    goto loc_002B3168;
loc_002B31C0:
    v_r12 = (unsigned int)((v_stack_m268) + 1);
    if (((*(unsigned int *)(v_rip + 13705442)) & ((unsigned int)(v_r12))) == 0) goto loc_002B38F7;
loc_002B31D0:
loc_002B31D2:
    if (!sign_flag) goto loc_002B2E58;
    goto loc_002B31C0;
loc_002B31E1:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(a1))) + 1);
    if (((*(unsigned int *)(v_rip + 13705411)) & ((unsigned int)(v_rbx))) == 0) goto loc_002B391F;
loc_002B31EF:
loc_002B31F1:
    if (!sign_flag) goto loc_002B2F37;
    goto loc_002B31E1;
loc_002B3200:
    a3 = 0;
    result = MiGetPagePrivilege(a1, a3 + 1, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_002B2C0E;
    goto loc_002B2C0E;
loc_002B3226:
    result = MiUnlockProtoPoolPage(v_stack_m270, 17, a3, a4);
    goto loc_002B2F0D;
loc_002B3242:
    if (((v_stack_mD0) & (256)) != 0) goto loc_002B32A0;
    result = (unsigned __int8)(((unsigned int)(v_stack_mD0)) & (80));
    if (((unsigned __int8)(result)) == 16) goto loc_002B39C8;
loc_002B325E:
    goto loc_002B32A8;
loc_002B3270:
    v_r12 = (unsigned int)((v_stack_m268) + 1);
    if (((*(unsigned int *)(v_rip + 13705266)) & ((unsigned int)(v_r12))) == 0) goto loc_002B39A0;
loc_002B3280:
loc_002B3282:
    if (!sign_flag) goto loc_002B3078;
    goto loc_002B3270;
loc_002B3291:
    if (condition_is_below) goto loc_002B2CDC;
    goto loc_002B2D12;
loc_002B32A0:
loc_002B32A8:
    if (condition_is_above_or_equal) goto loc_002B33B7;
    if (((v_stack_mD0) & (256)) != 0) goto loc_002B35F7;
    a4 = (17) & (-2);
    if (((v_stack_mD0) & (1)) == 0) goto loc_002B3699;
    *(unsigned __int64 *)(v_stack_m268) = a4;
loc_002B32E0:
    result = MiFlushSingleTbEntry(v_stack_m280, (unsigned int)(v_stack_p78), 1, a4);
    result = 0;
    v_stack_m220 = 17;
    result = MiPteInShadowRange(v_stack_m268, (unsigned int)(v_stack_p78), 1, a4);
    if ((unsigned int)(result) != 0) goto loc_002B3C0E;
loc_002B330B:
    if (condition_is_below) goto loc_002B3946;
loc_002B331A:
    *(unsigned __int64 *)(v_stack_m268) = 17;
    if (0 == 0) goto loc_002B2EE6;
    result = MiWritePteShadow(v_stack_m268, 17, 1, a4);
    goto loc_002B2EE6;
loc_002B3336:
    if (a4 >= (*(unsigned __int64 *)(v_rip + 12042307))) goto loc_002B3544;
loc_002B3343:
    goto loc_002B2A20;
loc_002B334F:
    result = MiLockStealSystemVm(a1, 17, v_r15, v_stack_mD8);
    if (((unsigned int)(result)) != 1) goto loc_002B3455;
    v_rbx = 0;
    v_stack_m258 = v_stack_mC0;
    v_stack_p7C = 0;
    v_stack_p78 = 1;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_mC0 + 184))) & (15));
    if (((unsigned __int8)(result)) != 7) goto loc_002B362C;
    if (((unsigned __int8)(result)) < 7) goto loc_002B3D60;
    v_stack_p78 = 2;
    goto loc_002B2A81;
loc_002B33B7:
    a3 = 0;
    result = MiWriteValidPteNewPage(v_stack_m268, 0, a3, v_stack_mD8);
    goto loc_002B2ECD;
loc_002B33CA:
    result = MiReplacePageOfProtoPool(v_stack_m280, v_stack_m250, v_stack_m260, v_stack_m238);
    if ((unsigned int)(result) != 0) {
        v_rsi = (unsigned int)((v_rsi) | (1));
    }
    if ((((unsigned __int8)(v_rsi)) & (1)) == 0) goto loc_002B3A3F;
    if (((v_stack_mD0) & (256)) != 0) goto loc_002B378F;
    a2 = 0;
loc_002B340A:
    if (condition_is_below) goto loc_002B3670;
    v_stack_p74 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (16));
    result = (unsigned __int8)((result) & (253));
    result = (unsigned __int8)((result) | (5));
    v_stack_p76 = (unsigned __int8)(result);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_p74));
    result = (*(unsigned __int64 *)(a1 + 24)) & (v_stack_m280);
    result = (result) | (1);
    *(unsigned __int64 *)(a1 + 24) = result;
    goto loc_002B2E92;
loc_002B3455:
    *(unsigned int *)(v_rip + 12852551) = (unsigned int)(v_stack_m268);
    a1 = v_stack_m280;
    if (condition_is_below) { a1 = (unsigned int)(v_rsi); }
    goto loc_002B317F;
loc_002B3478:
    result = MiPrepareToTradeUsingAccessedBit(a1, v_rsi, v_stack_m260, v_stack_m238);
    if (result != 0) goto loc_002B2D12;
    goto loc_002B3137;
loc_002B34A3:
loc_002B34A9:
    goto loc_002B314C;
loc_002B34B5:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & (10));
    if (((unsigned int)(result)) == 10) goto loc_002B2DDA;
    if (sign_flag) goto loc_002B2DDA;
    if (((unsigned int)(result)) != 8) goto loc_002B34D8;
    if ((unsigned int)((unsigned int)(v_stack_p7C)) == 0) goto loc_002B2DF5;
loc_002B34D8:
    if (v_stack_mA8 != 3) goto loc_002B2E05;
    if ((((unsigned __int8)(v_rsi)) & (4)) != 0) goto loc_002B2DF5;
    goto loc_002B2E05;
loc_002B34F3:
    if (v_rsi > result) goto loc_002B29AA;
    goto loc_002B29B1;
loc_002B3512:
    v_stack_p74 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (16));
    result = (unsigned __int8)((result) & (253));
    result = (unsigned __int8)((result) | (5));
    v_stack_p76 = (unsigned __int8)(result);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_p74));
    goto loc_002B2EE6;
loc_002B3537:
    if (!sign_flag) goto loc_002B2D12;
    goto loc_002B2CD2;
loc_002B3544:
    if (v_stack_m238 > (*(unsigned __int64 *)(v_rip + 12041797))) goto loc_002B3343;
    v_r11 = (unsigned int)(((unsigned int)(v_stack_mD0)) | (8));
    if ((((unsigned __int8)(v_r11)) & (1)) == 0) goto loc_002B3988;
    v_r11 = (unsigned int)((v_r11) | (2));
    if (v_rsi < (*(unsigned __int64 *)(v_rip + 12041751))) goto loc_002B358C;
    result = MiHyperSpaceSize((unsigned int)(v_stack_p7C), v_rsi, v_stack_m260, v_stack_m238);
    result = (result) + (*(unsigned __int64 *)(v_rip + 12041734));
    if (v_rsi < result) {
    }
    v_stack_mD0 = (unsigned int)((unsigned int)((unsigned int)(v_r11)));
    goto loc_002B2A20;
loc_002B359D:
    if (v_stack_mA8 == 2) goto loc_002B2C36;
    if (((v_stack_mD0) & (38)) != 0) goto loc_002B2C36;
    goto loc_002B3137;
loc_002B35D1:
    a2 = 0;
    result = MiLockProtoPoolPage(v_stack_m280, a2, v_stack_m260, v_stack_m238);
    v_stack_m270 = result;
    if (result != 0) goto loc_002B3857;
    goto loc_002B3137;
loc_002B35F7:
    v_rdi = 0;
    v_stack_p20 = 0;
    result = MiTransformValidPteInPlace(v_stack_m268, v_stack_m268, v_rsi, v_rdi + 64);
    goto loc_002B2EE8;
loc_002B3614:
    if (((v_stack_mD0) & (4)) != 0) { result = 2; }
    v_stack_p78 = (unsigned int)(result);
    goto loc_002B2D1F;
loc_002B362C:
    if (((unsigned __int8)(result)) == 2) goto loc_002B2A7D;
    a2 = v_stack_m268;
    if (v_stack_mA8 == ((unsigned int)(v_stack_m268))) { a2 = 2; }
    goto loc_002B2A79;
loc_002B3647:
    if (v_stack_p78 != 1) goto loc_002B2CB3;
    if ((((unsigned __int8)((unsigned int)(v_stack_mD0))) & (16)) == 0) goto loc_002B3DC5;
    result = (unsigned int)(((unsigned int)(v_stack_mD0)) | (264));
    v_stack_mD0 = (unsigned int)(result);
    goto loc_002B2CB9;
loc_002B3670:
    v_rbx = (unsigned int)((v_rsi) + 1);
    if (((*(unsigned int *)(v_rip + 13704244)) & ((unsigned int)(v_rbx))) == 0) goto loc_002B3A5F;
loc_002B367E:
loc_002B3680:
    if (!sign_flag) goto loc_002B340A;
    goto loc_002B3670;
loc_002B368F:
    goto loc_002B2F0D;
loc_002B3699:
    a2 = (unsigned int)((v_stack_mB3) & (1));
    result = MiRewritePteWithLockBit(v_stack_m258, a2, v_stack_m268, v_rdi + 64);
    goto loc_002B32E0;
loc_002B36B4:
    if (v_stack_p78 != 0) goto loc_002B2E39;
loc_002B36BF:
    v_rsi = (unsigned int)((v_rsi) | (1));
    v_stack_m1C4 = (unsigned int)(v_rdi + 64);
    v_stack_m1E0 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m200 = v_stack_m280;
    v_stack_m1D0 = (unsigned int)(v_rdi + 64);
    v_stack_m1C8 = (unsigned int)(v_rdi + 64);
    v_stack_m1C0 = v_rdi + 64;
    v_stack_m1E8 = v_stack_m260;
    v_stack_m1F8 = v_stack_m238;
    v_stack_m208 = v_stack_m258;
    v_stack_m1F0 = v_stack_m250;
    v_stack_m1D8 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_m1CC = (unsigned int)((unsigned int)(v_stack_m288));
    result = (*(unsigned __int64 *)(a1 + 40)) & (v_stack_m268);
    if (result == v_stack_m250) goto loc_002B3CC2;
    result = MiReplacePageTablePage(v_stack_m208, v_stack_m258, v_stack_m250, v_stack_m238);
loc_002B3731:
    if ((((unsigned __int8)(v_rsi)) & (1)) == 0) goto loc_002B3A3F;
    if (v_stack_m1D0 >= 0) goto loc_002B33E6;
    v_rsi = (unsigned int)((v_rsi) & (0xFFFFFFFEULL));
    goto loc_002B33E6;
loc_002B374D:
    if ((((unsigned __int8)(v_rbx)) & (32)) != 0) goto loc_002B3101;
    a1 = (result) + (result);
    if (v_stack_m268 < a1) goto loc_002B3101;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_m268, v_rbx, 128, v_stack_m238);
    goto loc_002B3101;
loc_002B378F:
    v_stack_p74 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (16));
    result = (unsigned __int8)((result) & (253));
    result = (unsigned __int8)((result) | (5));
    v_stack_p76 = (unsigned __int8)(result);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_p74));
    result = (*(unsigned __int64 *)(a1 + 24)) & (v_stack_m268);
    result = (result) | (1);
    a2 = 0;
    *(unsigned __int64 *)(a1 + 24) = result;
loc_002B37C7:
    if (condition_is_above_or_equal) goto loc_002B2E92;
loc_002B37D4:
    v_rbx = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 13703888)) & ((unsigned int)(v_rbx))) == 0) goto loc_002B3C22;
loc_002B37E2:
loc_002B37E4:
    if (!sign_flag) goto loc_002B37C7;
    goto loc_002B37D4;
loc_002B37EF:
    a2 = (0) & (-67);
    result = MiWriteValidPteNewProtection(v_rbx, a2, 128, v_stack_m238);
    goto loc_002B2D05;
loc_002B3809:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13709993)))) & (64)) == 0) goto loc_002B303E;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_rbx, a2, 2, v_stack_m238);
    if ((unsigned __int8)(result) == 0) goto loc_002B303E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), a2, 2, v_stack_m238);
    goto loc_002B3040;
loc_002B3830:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13709954)))) & (64)) == 0) goto loc_002B305E;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbx)), a2, 2, v_stack_m238);
    if ((unsigned __int8)(result) == 0) goto loc_002B305E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), a2, 2, v_stack_m238);
    goto loc_002B3060;
loc_002B3857:
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(result + 32)))) > 2) goto loc_002B3DDF;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m268))) & (66)) == 0) goto loc_002B38E9;
    result = 0;
loc_002B3875:
    if (condition_is_below) goto loc_002B3A00;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_rbx)) + 32)))) > 2) goto loc_002B3DFA;
    a2 = (*(unsigned __int64 *)(v_stack_m268)) & (-67);
    result = MiWriteValidPteNewProtection(v_stack_m268, a2, v_stack_m268, v_stack_m238);
    result = MiFlushSingleTbEntry(v_stack_m280, 2, 2 + 8, v_stack_m238);
    result = MiCaptureDirtyBitToPfn(v_stack_m270, 2, 2 + 8, v_stack_m238);
    if (result != 0) goto loc_002B3E11;
loc_002B38CB:
    result = 0;
loc_002B38CF:
    if (condition_is_below) goto loc_002B3A20;
    result = MiCaptureDirtyBitToPfn(v_r15, 2, 2 + 8, v_stack_m238);
loc_002B38E9:
    a4 = 0;
    goto loc_002B2E16;
loc_002B38F7:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13709755)))) & (64)) == 0) goto loc_002B31D0;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_r15, 2, 2 + 8, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002B31D0;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_m268)), 2, 2 + 8, a4);
    goto loc_002B31D2;
loc_002B391F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13709715)))) & (64)) == 0) goto loc_002B31EF;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_stack_m268)), 2, 2 + 8, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002B31EF;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((unsigned int)(v_stack_mD0))), 2, 2 + 8, a4);
    goto loc_002B31F1;
loc_002B3946:
    if ((((unsigned __int8)((unsigned int)(v_stack_mD0))) & (32)) != 0) goto loc_002B331A;
    a1 = (result) + (result);
    if (v_stack_m268 < a1) goto loc_002B331A;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_m268, (unsigned int)(v_stack_mD0), 128, a4);
    goto loc_002B331A;
loc_002B3988:
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(v_r11))) | (4));
    v_stack_mD0 = (unsigned int)(v_r10);
    goto loc_002B2A20;
loc_002B39A0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13709586)))) & (64)) == 0) goto loc_002B3280;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_m268, (unsigned int)(v_stack_mD0), 128, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002B3280;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_m268)), (unsigned int)(v_stack_mD0), 128, a4);
    goto loc_002B3282;
loc_002B39C8:
    result = 0;
loc_002B39CC:
    if (condition_is_above_or_equal) goto loc_002B325E;
loc_002B39D9:
    v_rdi = (unsigned int)((0) + 1);
    if (((*(unsigned int *)(v_rip + 13703371)) & ((unsigned int)(v_rdi))) == 0) goto loc_002B3C9B;
loc_002B39E7:
loc_002B39E9:
    if (!sign_flag) goto loc_002B39CC;
    goto loc_002B39D9;
loc_002B3A00:
    v_rbx = (unsigned int)(((unsigned int)(v_stack_mD0)) + 1);
    if (((*(unsigned int *)(v_rip + 13703332)) & ((unsigned int)(v_rbx))) == 0) goto loc_002B3C49;
loc_002B3A0E:
loc_002B3A10:
    if (!sign_flag) goto loc_002B3875;
    goto loc_002B3A00;
loc_002B3A20:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 13703300)) & ((unsigned int)(v_rbx))) == 0) goto loc_002B3C74;
loc_002B3A2E:
loc_002B3A30:
    if (!sign_flag) goto loc_002B38CF;
    goto loc_002B3A20;
loc_002B3A3F:
    if (((v_stack_mD0) & (256)) == 0) goto loc_002B3137;
    result = MiUnlockProtoPoolPage(v_stack_m270, 17, 128, a4);
    goto loc_002B3137;
loc_002B3A5F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13709395)))) & (64)) == 0) goto loc_002B367E;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_m270, 17, 128, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002B367E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), 17, 128, a4);
    goto loc_002B3680;
loc_002B3A86:
    a2 = 0;
    result = memset(v_stack_m148, a2, a2 + 112, a4);
    result = MI_NODE_FROM_PFN(a1, a2, a2 + 112, a4);
    result = (unsigned int)((result) + 1);
    v_stack_p60 = v_stack_m148;
    a3 = (unsigned int)((v_stack_mB3) & (1));
    v_stack_p58 = 1;
    a1 = 0;
    v_stack_p50 = 0;
    v_stack_p48 = 9;
    v_stack_p40 = 0;
    v_stack_p38 = v_stack_m60;
    v_stack_p30 = (unsigned int)(v_rbx);
    v_stack_p28 = (unsigned int)(v_r15);
    v_stack_p20 = (unsigned int)(result);
    result = MiInitializePageChainPacket(result, v_stack_m258, a3, v_rdi);
    result = MiGetPageChain(v_stack_m148, v_stack_m258, a3, v_rdi);
    if (v_stack_mE0 == v_rsi) goto loc_002B3D6E;
    if (v_stack_mF0 == 0) goto loc_002B3B42;
    v_stack_mF0 = *(unsigned __int64 *)(v_stack_mF0);
    if (v_stack_mF0 == 0) {
        v_rbx = 0;
        v_stack_mE8 = 0;
    }
    v_r13 = (v_stack_mF0) - (*(unsigned __int64 *)(v_stack_mF0));
    v_r13 = (v_r13) >> (4);
    v_r13 = (v_r13) * (*(unsigned __int64 *)(v_stack_mF0));
    v_stack_m260 = v_r13;
    goto loc_002B2BD1;
loc_002B3B70:
    result = MiVaIsPageFileHash(v_stack_m270, v_stack_m280, a3, v_rdi);
    v_stack_m240 = result;
    if (result == 0) goto loc_002B311D;
    result = ExAcquireSpinLockSharedAtDpcLevel(result + 200, v_stack_m280, a3, v_rdi);
    result = MiVaIsPageFileHash(v_stack_m270, v_stack_m280, v_stack_m280, v_rdi);
    if (v_stack_m240 != result) goto loc_002B3BC2;
    result = MiSmallVaStillMapsFrame(v_stack_m280, v_stack_m268, v_stack_m280, v_rdi);
    if ((unsigned int)(result) != 0) goto loc_002B2D73;
loc_002B3BC2:
    result = ExReleaseSpinLockSharedFromDpcLevel(result + 200, v_stack_m268, v_stack_m280, v_rdi);
    goto loc_002B3123;
loc_002B3BD5:
    result = MiSanitizeShadowPxe(result + 200, v_stack_m228, v_stack_m280, v_rdi);
    goto loc_002B30F2;
loc_002B3BE9:
    a1 = (v_stack_m240) + (200);
    result = ExReleaseSpinLockSharedFromDpcLevel(a1, v_stack_m228, v_stack_m280, v_rdi);
    goto loc_002B2F30;
loc_002B3BFE:
    result = MiSetPfnContainingFrame(v_stack_mF0, v_r13, v_stack_m280, v_rdi);
    goto loc_002B2D9C;
loc_002B3C0E:
    result = MiSanitizeShadowPxe(v_stack_mF0, v_stack_m220, v_stack_m280, v_rdi);
    goto loc_002B330B;
loc_002B3C22:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13708944)))) & (64)) == 0) goto loc_002B37E2;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_mF0, v_stack_m220, v_stack_m280, v_rdi);
    if ((unsigned __int8)(result) == 0) goto loc_002B37E2;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_m220)), v_stack_m220, v_stack_m280, v_rdi);
    goto loc_002B37E4;
loc_002B3C49:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13708905)))) & (64)) == 0) goto loc_002B3A0E;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_stack_m220)), v_stack_m220, v_stack_m280, v_rdi);
    if ((unsigned __int8)(result) == 0) goto loc_002B3DF1;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_m220)), v_stack_m220, v_stack_m280, v_rdi);
    goto loc_002B3A10;
loc_002B3C74:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13708862)))) & (64)) == 0) goto loc_002B3A2E;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_m270, v_stack_m220, v_stack_m280, v_rdi);
    if ((unsigned __int8)(result) == 0) goto loc_002B3A2E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_stack_m220)), v_stack_m220, v_stack_m280, v_rdi);
    goto loc_002B3A30;
loc_002B3C9B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13708823)))) & (64)) == 0) goto loc_002B39E7;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_stack_m220)), v_stack_m220, v_stack_m280, v_rdi);
    if ((unsigned __int8)(result) == 0) goto loc_002B39E7;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m220, v_stack_m280, v_rdi);
    goto loc_002B39E9;
loc_002B3CC2:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m220 + 184))) >> (24));
    if ((((unsigned __int8)(result)) & (2)) == 0) goto loc_002B3CD7;
    v_rsi = (unsigned int)((v_rsi) & (0xFFFFFFFEULL));
    goto loc_002B3731;
loc_002B3CD7:
    if (condition_is_below) goto loc_002B3E4B;
    v_stack_mD0 = (unsigned int)((unsigned int)(v_stack_mD0));
    result = (*(unsigned __int64 *)(v_stack_m1D8 + 40)) >> (12);
    if (result != v_stack_m280) goto loc_002B3D42;
loc_002B3D0B:
    a3 = 0;
    result = MiReleaseFaultState(v_stack_mC0, 17, a3, v_rdi);
    result = KeSwapDirectoryTableBase(v_stack_m1D8, (unsigned int)(v_stack_m1C8), v_stack_m208, v_rdi);
    result = MiLockWorkingSetExclusive(v_stack_m258, (unsigned int)(v_stack_m1C8), v_stack_m208, v_rdi);
    goto loc_002B3731;
loc_002B3D42:
    v_stack_m1C8 = 1;
    v_stack_m1C0 = *(unsigned __int64 *)((unsigned int)(v_stack_m1C8) + 1288);
    v_stack_mD0 = (unsigned int)(v_stack_m258);
    goto loc_002B3D0B;
loc_002B3D60:
    goto loc_002B314C;
loc_002B3D6E:
    goto loc_002B34A9;
loc_002B3D79:
    goto loc_002B31A5;
loc_002B3D87:
    if (condition_is_below) goto loc_002B2BFD;
    goto loc_002B3137;
loc_002B3DAB:
    goto loc_002B3137;
loc_002B3DC5:
    goto loc_002B3137;
loc_002B3DDF:
    result = MiUnlockProtoPoolPage(v_stack_m258, 17, v_stack_m208, v_rdi);
    goto loc_002B3137;
loc_002B3DF1:
    goto loc_002B3A0E;
loc_002B3DFA:
    result = MiUnlockProtoPoolPage(v_stack_m270, 17, v_stack_m208, v_rdi);
    goto loc_002B3137;
loc_002B3E11:
    a1 = (*(unsigned __int64 *)(1 + 40)) >> (43);
    a1 = (unsigned int)((a1) & (0x3FFULL));
    result = MiReleasePageFileInfo(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12042854) + a1 * 8), result, 1, v_rdi);
    goto loc_002B38CB;
loc_002B3E3D:
    if (((1) & (4)) != 0) goto loc_002B36BF;
    goto loc_002B2E2D;
loc_002B3E4B:
    v_rsi = (unsigned int)((v_rsi) & (0xFFFFFFFEULL));
    goto loc_002B3731;
loc_002B3E53:
    a2 = 72;
    if (1 != 17) { a2 = 12; }
    result = MiClearPfnImageVerified(a1, a2, 1, v_rdi);
    goto loc_002B2F1F;
loc_002B3E70:
    goto loc_002B3137;
loc_002B3E8A:
    result = MiPfnIsActivePageTable(v_stack_m278, a2, 1, v_rdi);
    result = MiRevertPfnActivePageTable(v_stack_m278, a2, 1, v_rdi);
loc_002B3EA8:
loc_002B3EAD:
    goto loc_002B3168;
loc_002B3EC7:
    result = MiReleaseFreshPage(v_stack_m278, a2, 1, v_rdi);
    goto loc_002B317D;
}
```

## 5. (Beta) C Style

```c
int64_t MiStealPage(void *Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m168;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m190;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1C0;
    uint32_t v_stack_m1C4;
    uint32_t v_stack_m1C8;
    uint32_t v_stack_m1CC;
    uint32_t v_stack_m1D0;
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
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m280;
    uint32_t v_stack_m288;
    uint32_t v_stack_m28C;
    uint32_t v_stack_m290;
    uint8_t v_stack_m292;
    uint32_t v_stack_m294;
    uint8_t v_stack_m298;
    uint64_t v_stack_m2E8;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_mA8;
    uint8_t v_stack_mB3;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint32_t v_stack_p74;
    uint8_t v_stack_p76;
    uint32_t v_stack_p78;
    uint32_t v_stack_p7C;

    local_rsp = (local_rsp) - (712);
    result = (*(uint64_t *)(v_rip + 0xB57E4D)) ^ (local_rsp);
    v_stack_m58 = result;
    v_stack_m298 = (uint8_t)(Arg2);
    Arg2 = 0;
    v_stack_m288 = Arg3;
    v_stack_m238 = Arg4;
    v_stack_m218 = Arg6;
    result = memset(v_stack_mD4, Arg2, Arg2 + 116, Arg4);
    local_r10 = 0;
    v_stack_mD8 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m260 = -1;
    v_stack_m60 = -1;
    local_r15 = (*(uint64_t *)(arg1 + 0x8)) | (-1);
    v_stack_m278 = 0;
    v_stack_m240 = 0;
    local_rdi = (local_r15) << (25);
    v_stack_m268 = local_r15;
    result = (local_r11) << (25);
    local_rdi = (local_rdi) - (result);
    local_rdi = (local_rdi) >> (16);
    v_stack_m280 = local_rdi;
    result = MiGetLeafVa(local_rdi, Arg2, Arg2 + 116, Arg4);
    if (local_rdi >= local_r11) goto loc_002B34F3;
loc_002B29AA:
loc_002B29B1:
    v_stack_m230 = 0;
    local_r12 = (Arg1) - (local_r11);
    local_r12 = (local_r12) >> (4);
    local_r12 = (local_r12) * (local_r11);
    result = (*(uint64_t *)(arg1 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_m250 = local_r12;
    v_stack_m270 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB7D6A3) + result * 8);
    if (result >= result) goto loc_002B3336;
    v_stack_mD0 = (uint32_t)((uint32_t)(v_stack_mD0));
loc_002B2A20:
    if (result >= result) goto loc_002B334F;
    v_stack_m2E8 = v_stack_mD8;
    result = MiLockStealUserVm(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7D6A3) + result * 8), Arg1, (uint8_t)((uint8_t)(Arg2)), local_r15);
    if (((uint32_t)(result)) != 1) goto loc_002B3455;
    Arg2 = 0;
    v_stack_m28C = 0;
    v_stack_m258 = v_stack_mC0;
    v_stack_m230 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
loc_002B2A79:
    v_stack_m290 = 0;
loc_002B2A7D:
loc_002B2A81:
    Arg2 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (16));
    local_r15 = (uint32_t)(((uint8_t)(result)) >> (6));
    v_stack_m294 = (uint32_t)(local_r15);
    if (condition_is_below) goto loc_002B2B0E;
    result = MiGetPfnChannel(Arg1, Arg2, v_stack_mC0, local_r15);
    result = MiPageToNode(local_r12, Arg2, v_stack_mC0, local_r15);
    local_rbx = (uint32_t)(((uint8_t)(result)) & (1));
    result = (uint32_t)((result) & (63));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) << (9));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(result)));
    Arg2 = (uint32_t)((Arg2) | (384));
    Arg2 = (uint32_t)((Arg2) + (Arg2));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(local_rbx)));
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m288)) & (0x1000000ULL));
    Arg2 = (uint32_t)((Arg2) << (8));
    Arg2 = (uint32_t)((Arg2) | (0));
    local_rbx = (uint32_t)((local_rbx) >> (9));
    if (((v_stack_m288) & (0x2000000ULL)) == 0) goto loc_002B2B48;
    goto loc_002B2B48;
loc_002B2B0E:
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) >> (16));
    Arg4 = (uint32_t)((Arg4) & (3));
    Arg2 = 0;
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)((uint32_t)(Arg5))));
    Arg2 = (uint32_t)(((uint8_t)(Arg2)) ^ ((uint32_t)((uint32_t)(Arg5))));
loc_002B2B48:
    if (v_stack_m218 == 0) goto loc_002B2B88;
    v_stack_m260 = *(uint64_t *)(v_stack_m218);
    if ((*(uint64_t *)(v_stack_m218)) == -1) goto loc_002B2B84;
    local_r15 = (*(uint64_t *)(v_stack_m218) * 2) + (*(uint64_t *)(v_stack_m218));
    local_r15 = (local_r15) << (4);
    local_r15 = (local_r15) + (v_stack_m218);
    goto loc_002B2BD1;
loc_002B2B84:
loc_002B2B88:
    if (v_stack_m60 != -1) goto loc_002B3A86;
    result = MiGetPage(v_stack_m270, Arg2, (uint32_t)((uint32_t)((uint32_t)(0x3001ULL))), v_rip + 12038531);
    v_stack_m260 = result;
    if (result == -1) goto loc_002B34A3;
    local_r15 = (result * 2) + (result);
    local_r15 = (local_r15) << (4);
    local_r15 = (local_r15) + (result);
loc_002B2BD1:
    if (local_r15 == Arg1) goto loc_002B3D79;
    local_rdi = 0;
loc_002B2BDE:
    if (condition_is_below) goto loc_002B3030;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (64)) != 0) goto loc_002B3D87;
loc_002B2BFD:
    if (((*(uint64_t *)(v_rip + 0xD13E80)) & (0x4000ULL)) != 0) goto loc_002B3200;
loc_002B2C0E:
    if (((uint16_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) != 1) goto loc_002B3DAB;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (8)) != 0) goto loc_002B359D;
    if ((((uint8_t)(*(uint64_t *)(arg1))) & (1)) == 0) goto loc_002B359D;
loc_002B2C36:
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x22)) & (7));
    if (((uint8_t)(result)) != 6) goto loc_002B3E70;
    result = (*(uint64_t *)(arg1 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (v_stack_m270 != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7D438) + result * 8))) goto loc_002B3E70;
    result = (uint32_t)(v_stack_mD0);
    if ((((uint8_t)((uint32_t)(v_stack_mD0))) & (32)) == 0) {
        Arg1 = v_stack_m268;
        result = MI_READ_PTE_LOCK_FREE(Arg1, *(uint64_t *)(*(uint64_t *)(v_rip + 0xB7D438) + result * 8), (uint32_t)((uint32_t)((uint32_t)(0x3001ULL))), v_rip + 12038531);
        local_rdi = result;
        result = v_stack_mD0;
    }
    if (v_stack_mA8 == 3) goto loc_002B2CB9;
    result = (*(uint64_t *)(arg1 + 0x18)) & (Arg1);
    if (result > 1) goto loc_002B3647;
loc_002B2CB3:
loc_002B2CB9:
    if (v_stack_mA8 == 2) goto loc_002B2D12;
    if ((((uint8_t)((uint32_t)(v_stack_mD0))) & (32)) != 0) goto loc_002B3478;
    if ((((uint8_t)((uint32_t)(v_stack_mD0))) & (8)) != 0) goto loc_002B3537;
loc_002B2CD2:
    if ((((uint8_t)(local_rdi)) & (66)) == 0) goto loc_002B3291;
loc_002B2CDC:
    if (sign_flag) goto loc_002B37EF;
    result = (uint32_t)(((uint32_t)(v_stack_mD0)) | (64));
    v_stack_mD0 = (uint32_t)(result);
    result = (local_rdi) & (-2);
    *(uint64_t *)(v_stack_m268) = result;
    local_rsi = (uint32_t)((8) | (2));
loc_002B2D05:
    result = MiFlushSingleTbEntry(v_stack_m280, (uint32_t)(v_stack_m290), 1, v_rip + 12038531);
loc_002B2D12:
    if (((uint32_t)((uint32_t)(v_stack_m290))) == 1) goto loc_002B3614;
loc_002B2D1F:
    local_rbx = 0;
loc_002B2D21:
    if (condition_is_below) goto loc_002B3050;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x20))) >> (16));
    result = (uint32_t)(((uint8_t)(result)) >> (6));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(v_stack_m294)))) {
        Arg3 = 9;
        Arg1 = local_r15;
        result = MiChangePageAttribute(Arg1, (uint32_t)(v_stack_m294), Arg3, v_rip + 12038531);
    }
    result = (*(uint64_t *)(local_r15 + 0x18)) & (Arg1);
    *(uint64_t *)(local_r15 + 0x18) = result;
    if (v_stack_mA8 == 2) goto loc_002B3B70;
loc_002B2D73:
    result = MiCopyPfnEntryEx(local_r15, Arg1, Arg3, v_rip + 12038531);
    result = (*(uint64_t *)(arg1 + 0x28)) & (local_r12);
    local_rsi = (uint32_t)((local_rsi) | (4));
    if (result == v_stack_m250) goto loc_002B3BFE;
loc_002B2D9C:
    if ((((uint8_t)((uint32_t)(v_stack_mD0))) & (32)) != 0) goto loc_002B2E05;
    if (v_stack_mA8 == 2) goto loc_002B2E05;
    if (v_stack_mA8 < 2) goto loc_002B2DF5;
    if ((((uint8_t)((uint32_t)(v_stack_mD0))) & (8)) != 0) goto loc_002B34B5;
    if ((uint32_t)((uint32_t)(v_stack_m290)) != 0) goto loc_002B34B5;
loc_002B2DDA:
    v_stack_m294 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (16));
    result = (uint8_t)((result) & (253));
    result = (uint8_t)((result) | (5));
    v_stack_m292 = (uint8_t)(result);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_m294));
loc_002B2DF5:
    v_stack_m298 = 17;
loc_002B2E05:
    if (condition_is_below) goto loc_002B35D1;
    Arg4 = 0;
    v_stack_m270 = 0;
loc_002B2E16:
    if (condition_is_below) goto loc_002B33CA;
    if (v_stack_mA8 == 3) goto loc_002B3E3D;
loc_002B2E2D:
    result = (uint8_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mD0)))) & (10));
    if (((uint8_t)(result)) == 8) goto loc_002B36B4;
loc_002B2E39:
    local_rbx = (uint32_t)(((uint32_t)(v_stack_mD0)) & (0x1000ULL));
    local_rbx = (uint32_t)((local_rbx) >> (11));
    if (((uint8_t)(v_stack_m298)) == 17) goto loc_002B2E6B;
    local_rbx = (uint32_t)((local_rbx) | (4));
loc_002B2E58:
    if (condition_is_below) goto loc_002B31C0;
loc_002B2E6B:
    result = MiCopyPage(v_stack_m260, v_stack_m250, (uint32_t)((uint32_t)(local_rbx)), Arg4);
    if ((((uint8_t)(local_rbx)) & (4)) != 0) {
    }
    if (((v_stack_mD0) & (32)) == 0) goto loc_002B3004;
loc_002B2E92:
    result = (v_stack_m260) << (12);
    local_rbx = (result) ^ (local_rdi);
    local_rbx = (local_rbx) & (v_stack_m260);
    local_rbx = (local_rbx) ^ (result);
    if (((v_stack_mD0) & (32)) != 0) goto loc_002B306F;
    if (condition_is_above_or_equal) goto loc_002B30CE;
loc_002B2ECD:
    result = (uint32_t)(v_stack_mD0);
    if ((((uint8_t)(local_rsi)) & (2)) == 0) {
        Arg2 = v_stack_m290;
        Arg3 = 64;
        Arg1 = v_stack_m280;
        result = MiFlushSingleTbEntry(Arg1, Arg2, Arg3, Arg4);
    }
    local_rdi = 0;
loc_002B2EE8:
    if (((v_stack_mD0) & (256)) != 0) goto loc_002B3226;
    result = (uint8_t)(((uint32_t)(v_stack_mD0)) & (80));
    if (((uint8_t)(result)) == 16) goto loc_002B368F;
loc_002B2F0D:
    result = (*(uint64_t *)(arg1 + 0x28)) >> (60);
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) == 3) goto loc_002B3E53;
loc_002B2F1F:
    if (v_stack_mA8 == 2) goto loc_002B3BE9;
loc_002B2F30:
    if (((uint8_t)(v_stack_m298)) != 17) goto loc_002B2F44;
loc_002B2F37:
    if (((uint8_t)(v_stack_m298)) < 17) goto loc_002B31E1;
loc_002B2F44:
    v_stack_m1A8 = 0;
    v_stack_m180 = *(uint64_t *)(arg1 + 0x28);
    Arg1 = (*(uint64_t *)(arg1 + 0x28)) & (Arg3);
    v_stack_m1A0 = v_xmm0;
    v_stack_m190 = v_xmm1;
    v_stack_m178 = v_xmm0;
    v_stack_m168 = v_xmm0;
    v_stack_m158 = v_xmm0;
    v_stack_m150 = *(uint64_t *)(arg1 + 0x28);
    if ((*(uint64_t *)(arg1 + 0x28)) == (*(uint64_t *)(arg1 + 0x28))) goto loc_002B2FBF;
loc_002B2F9D:
    v_stack_m180 = *(uint64_t *)(arg1 + 0x28);
    Arg1 = (*(uint64_t *)(arg1 + 0x28)) & (Arg3);
    v_stack_m150 = *(uint64_t *)(arg1 + 0x28);
    if ((*(uint64_t *)(arg1 + 0x28)) != (*(uint64_t *)(arg1 + 0x28))) goto loc_002B2F9D;
loc_002B2FBF:
    result = MiClearPfnReuseFields(Arg1, *(uint64_t *)(arg1 + 0x28), Arg3, Arg4);
    v_stack_m294 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    v_stack_m294 = 0;
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_m294));
    result = (*(uint64_t *)(arg1 + 0x18)) & (Arg1);
    *(uint64_t *)(arg1 + 0x18) = result;
    goto loc_002B31A5;
loc_002B3004:
    if (((uint8_t)(v_stack_m298)) == 17) goto loc_002B2E92;
    v_stack_m294 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (16));
    result = (uint8_t)((result) & (253));
    result = (uint8_t)((result) | (5));
    v_stack_m292 = (uint8_t)(result);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_m294));
    goto loc_002B2E92;
loc_002B3030:
    local_rbx = (uint32_t)((1) + 1);
    if (((*(uint32_t *)(v_rip + 0xD12274)) & ((uint32_t)(local_rbx))) == 0) goto loc_002B3809;
loc_002B303E:
loc_002B3040:
    if (!sign_flag) goto loc_002B2BDE;
    goto loc_002B3030;
loc_002B3050:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xD12254)) & ((uint32_t)(local_rbx))) == 0) goto loc_002B3830;
loc_002B305E:
loc_002B3060:
    if (!sign_flag) goto loc_002B2D21;
    goto loc_002B3050;
loc_002B306F:
    local_rbx = (local_rbx) | (32);
    Arg2 = 0;
loc_002B3078:
    if (condition_is_below) goto loc_002B3270;
    if (((*(uint64_t *)(v_rip + 0xD139F8)) & (0x2000000ULL)) != 0) {
    }
    if (((*(uint64_t *)(v_rip + 0xD139F8)) & (0x2000000ULL)) == 0) goto loc_002B3512;
    v_stack_m294 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x20))) >> (16));
    result = (uint8_t)((result) & (253));
    result = (uint8_t)((result) | (5));
    v_stack_m292 = (uint8_t)(result);
    *(uint32_t *)(local_r15 + 0x20) = (uint32_t)((uint32_t)(v_stack_m294));
    goto loc_002B3137;
loc_002B30CE:
    if ((((uint8_t)((uint32_t)(v_stack_m294))) & (64)) == 0) goto loc_002B3242;
    Arg2 = 0;
    v_stack_m228 = local_rbx;
    result = MiPteInShadowRange(v_stack_m268, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_002B3BD5;
loc_002B30F2:
    if (condition_is_below) goto loc_002B374D;
loc_002B3101:
    *(uint64_t *)(v_stack_m268) = local_rbx;
    if (0 == 0) goto loc_002B2ECD;
    result = MiWritePteShadow(v_stack_m268, local_rbx, Arg3, Arg4);
    goto loc_002B2ECD;
loc_002B311D:
loc_002B3123:
loc_002B3137:
    if (local_r15 != 0) goto loc_002B3E8A;
    if (((uint32_t)((uint32_t)(v_stack_m28C))) == 1) goto loc_002B31A3;
loc_002B314C:
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x22)) & (7));
    if (((uint8_t)(result)) != 6) goto loc_002B3EA8;
    if (((uint32_t)((uint32_t)(v_stack_m28C))) == 2) goto loc_002B3EAD;
loc_002B3168:
    result = MiUnlockStealVm(v_stack_mD8, local_rbx, Arg3, Arg4);
    if (local_r15 != 0) goto loc_002B3EC7;
loc_002B317D:
loc_002B317F:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, local_rbx, Arg3, Arg4);
    local_rsp = (local_rsp) + (712);
    return result;
loc_002B31A3:
loc_002B31A5:
    if (v_stack_m218 != 0) {
        result = v_stack_m260;
        *(uint64_t *)(v_stack_m218) = result;
    }
    goto loc_002B3168;
loc_002B31C0:
    local_r12 = (uint32_t)((v_stack_m268) + 1);
    if (((*(uint32_t *)(v_rip + 0xD120E2)) & ((uint32_t)(local_r12))) == 0) goto loc_002B38F7;
loc_002B31D0:
loc_002B31D2:
    if (!sign_flag) goto loc_002B2E58;
    goto loc_002B31C0;
loc_002B31E1:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) + 1);
    if (((*(uint32_t *)(v_rip + 0xD120C3)) & ((uint32_t)(local_rbx))) == 0) goto loc_002B391F;
loc_002B31EF:
loc_002B31F1:
    if (!sign_flag) goto loc_002B2F37;
    goto loc_002B31E1;
loc_002B3200:
    Arg3 = 0;
    result = MiGetPagePrivilege(Arg1, Arg3 + 1, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_002B2C0E;
    goto loc_002B2C0E;
loc_002B3226:
    result = MiUnlockProtoPoolPage(v_stack_m270, 17, Arg3, Arg4);
    goto loc_002B2F0D;
loc_002B3242:
    if (((v_stack_mD0) & (256)) != 0) goto loc_002B32A0;
    result = (uint8_t)(((uint32_t)(v_stack_mD0)) & (80));
    if (((uint8_t)(result)) == 16) goto loc_002B39C8;
loc_002B325E:
    goto loc_002B32A8;
loc_002B3270:
    local_r12 = (uint32_t)((v_stack_m268) + 1);
    if (((*(uint32_t *)(v_rip + 0xD12032)) & ((uint32_t)(local_r12))) == 0) goto loc_002B39A0;
loc_002B3280:
loc_002B3282:
    if (!sign_flag) goto loc_002B3078;
    goto loc_002B3270;
loc_002B3291:
    if (condition_is_below) goto loc_002B2CDC;
    goto loc_002B2D12;
loc_002B32A0:
loc_002B32A8:
    if (condition_is_above_or_equal) goto loc_002B33B7;
    if (((v_stack_mD0) & (256)) != 0) goto loc_002B35F7;
    Arg4 = (17) & (-2);
    if (((v_stack_mD0) & (1)) == 0) goto loc_002B3699;
    *(uint64_t *)(v_stack_m268) = Arg4;
loc_002B32E0:
    result = MiFlushSingleTbEntry(v_stack_m280, (uint32_t)(v_stack_p78), 1, Arg4);
    result = 0;
    v_stack_m220 = 17;
    result = MiPteInShadowRange(v_stack_m268, (uint32_t)(v_stack_p78), 1, Arg4);
    if ((uint32_t)(result) != 0) goto loc_002B3C0E;
loc_002B330B:
    if (condition_is_below) goto loc_002B3946;
loc_002B331A:
    *(uint64_t *)(v_stack_m268) = 17;
    if (0 == 0) goto loc_002B2EE6;
    result = MiWritePteShadow(v_stack_m268, 17, 1, Arg4);
    goto loc_002B2EE6;
loc_002B3336:
    if (Arg4 >= (*(uint64_t *)(v_rip + 0xB7C043))) goto loc_002B3544;
loc_002B3343:
    goto loc_002B2A20;
loc_002B334F:
    result = MiLockStealSystemVm(Arg1, 17, local_r15, v_stack_mD8);
    if (((uint32_t)(result)) != 1) goto loc_002B3455;
    local_rbx = 0;
    v_stack_m258 = v_stack_mC0;
    v_stack_p7C = 0;
    v_stack_p78 = 1;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_mC0 + 0xB8))) & (15));
    if (((uint8_t)(result)) != 7) goto loc_002B362C;
    if (((uint8_t)(result)) < 7) goto loc_002B3D60;
    v_stack_p78 = 2;
    goto loc_002B2A81;
loc_002B33B7:
    Arg3 = 0;
    result = MiWriteValidPteNewPage(v_stack_m268, 0, Arg3, v_stack_mD8);
    goto loc_002B2ECD;
loc_002B33CA:
    result = MiReplacePageOfProtoPool(v_stack_m280, v_stack_m250, v_stack_m260, v_stack_m238);
    if ((uint32_t)(result) != 0) {
        local_rsi = (uint32_t)((local_rsi) | (1));
    }
    if ((((uint8_t)(local_rsi)) & (1)) == 0) goto loc_002B3A3F;
    if (((v_stack_mD0) & (256)) != 0) goto loc_002B378F;
    Arg2 = 0;
loc_002B340A:
    if (condition_is_below) goto loc_002B3670;
    v_stack_p74 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (16));
    result = (uint8_t)((result) & (253));
    result = (uint8_t)((result) | (5));
    v_stack_p76 = (uint8_t)(result);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_p74));
    result = (*(uint64_t *)(arg1 + 0x18)) & (v_stack_m280);
    result = (result) | (1);
    *(uint64_t *)(arg1 + 0x18) = result;
    goto loc_002B2E92;
loc_002B3455:
    *(uint32_t *)(v_rip + 0xC41D47) = (uint32_t)(v_stack_m268);
    Arg1 = v_stack_m280;
    if (condition_is_below) { Arg1 = (uint32_t)(local_rsi); }
    goto loc_002B317F;
loc_002B3478:
    result = MiPrepareToTradeUsingAccessedBit(Arg1, local_rsi, v_stack_m260, v_stack_m238);
    if (result != 0) goto loc_002B2D12;
    goto loc_002B3137;
loc_002B34A3:
loc_002B34A9:
    goto loc_002B314C;
loc_002B34B5:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & (10));
    if (((uint32_t)(result)) == 10) goto loc_002B2DDA;
    if (sign_flag) goto loc_002B2DDA;
    if (((uint32_t)(result)) != 8) goto loc_002B34D8;
    if ((uint32_t)((uint32_t)(v_stack_p7C)) == 0) goto loc_002B2DF5;
loc_002B34D8:
    if (v_stack_mA8 != 3) goto loc_002B2E05;
    if ((((uint8_t)(local_rsi)) & (4)) != 0) goto loc_002B2DF5;
    goto loc_002B2E05;
loc_002B34F3:
    if (local_rsi > result) goto loc_002B29AA;
    goto loc_002B29B1;
loc_002B3512:
    v_stack_p74 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (16));
    result = (uint8_t)((result) & (253));
    result = (uint8_t)((result) | (5));
    v_stack_p76 = (uint8_t)(result);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_p74));
    goto loc_002B2EE6;
loc_002B3537:
    if (!sign_flag) goto loc_002B2D12;
    goto loc_002B2CD2;
loc_002B3544:
    if (v_stack_m238 > (*(uint64_t *)(v_rip + 0xB7BE45))) goto loc_002B3343;
    local_r11 = (uint32_t)(((uint32_t)(v_stack_mD0)) | (8));
    if ((((uint8_t)(local_r11)) & (1)) == 0) goto loc_002B3988;
    local_r11 = (uint32_t)((local_r11) | (2));
    if (local_rsi < (*(uint64_t *)(v_rip + 0xB7BE17))) goto loc_002B358C;
    result = MiHyperSpaceSize((uint32_t)(v_stack_p7C), local_rsi, v_stack_m260, v_stack_m238);
    result = (result) + (*(uint64_t *)(v_rip + 0xB7BE06));
    if (local_rsi < result) {
    }
    v_stack_mD0 = (uint32_t)((uint32_t)((uint32_t)(local_r11)));
    goto loc_002B2A20;
loc_002B359D:
    if (v_stack_mA8 == 2) goto loc_002B2C36;
    if (((v_stack_mD0) & (38)) != 0) goto loc_002B2C36;
    goto loc_002B3137;
loc_002B35D1:
    Arg2 = 0;
    result = MiLockProtoPoolPage(v_stack_m280, Arg2, v_stack_m260, v_stack_m238);
    v_stack_m270 = result;
    if (result != 0) goto loc_002B3857;
    goto loc_002B3137;
loc_002B35F7:
    local_rdi = 0;
    v_stack_p20 = 0;
    result = MiTransformValidPteInPlace(v_stack_m268, v_stack_m268, local_rsi, local_rdi + 64);
    goto loc_002B2EE8;
loc_002B3614:
    if (((v_stack_mD0) & (4)) != 0) { result = 2; }
    v_stack_p78 = (uint32_t)(result);
    goto loc_002B2D1F;
loc_002B362C:
    if (((uint8_t)(result)) == 2) goto loc_002B2A7D;
    Arg2 = v_stack_m268;
    if (v_stack_mA8 == ((uint32_t)(v_stack_m268))) { Arg2 = 2; }
    goto loc_002B2A79;
loc_002B3647:
    if (v_stack_p78 != 1) goto loc_002B2CB3;
    if ((((uint8_t)((uint32_t)(v_stack_mD0))) & (16)) == 0) goto loc_002B3DC5;
    result = (uint32_t)(((uint32_t)(v_stack_mD0)) | (264));
    v_stack_mD0 = (uint32_t)(result);
    goto loc_002B2CB9;
loc_002B3670:
    local_rbx = (uint32_t)((local_rsi) + 1);
    if (((*(uint32_t *)(v_rip + 0xD11C34)) & ((uint32_t)(local_rbx))) == 0) goto loc_002B3A5F;
loc_002B367E:
loc_002B3680:
    if (!sign_flag) goto loc_002B340A;
    goto loc_002B3670;
loc_002B368F:
    goto loc_002B2F0D;
loc_002B3699:
    Arg2 = (uint32_t)((v_stack_mB3) & (1));
    result = MiRewritePteWithLockBit(v_stack_m258, Arg2, v_stack_m268, local_rdi + 64);
    goto loc_002B32E0;
loc_002B36B4:
    if (v_stack_p78 != 0) goto loc_002B2E39;
loc_002B36BF:
    local_rsi = (uint32_t)((local_rsi) | (1));
    v_stack_m1C4 = (uint32_t)(local_rdi + 64);
    v_stack_m1E0 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m200 = v_stack_m280;
    v_stack_m1D0 = (uint32_t)(local_rdi + 64);
    v_stack_m1C8 = (uint32_t)(local_rdi + 64);
    v_stack_m1C0 = local_rdi + 64;
    v_stack_m1E8 = v_stack_m260;
    v_stack_m1F8 = v_stack_m238;
    v_stack_m208 = v_stack_m258;
    v_stack_m1F0 = v_stack_m250;
    v_stack_m1D8 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_m1CC = (uint32_t)((uint32_t)(v_stack_m288));
    result = (*(uint64_t *)(arg1 + 0x28)) & (v_stack_m268);
    if (result == v_stack_m250) goto loc_002B3CC2;
    result = MiReplacePageTablePage(v_stack_m208, v_stack_m258, v_stack_m250, v_stack_m238);
loc_002B3731:
    if ((((uint8_t)(local_rsi)) & (1)) == 0) goto loc_002B3A3F;
    if (v_stack_m1D0 >= 0) goto loc_002B33E6;
    local_rsi = (uint32_t)((local_rsi) & (0xFFFFFFFEULL));
    goto loc_002B33E6;
loc_002B374D:
    if ((((uint8_t)(local_rbx)) & (32)) != 0) goto loc_002B3101;
    Arg1 = (result) + (result);
    if (v_stack_m268 < Arg1) goto loc_002B3101;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_m268, local_rbx, 128, v_stack_m238);
    goto loc_002B3101;
loc_002B378F:
    v_stack_p74 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (16));
    result = (uint8_t)((result) & (253));
    result = (uint8_t)((result) | (5));
    v_stack_p76 = (uint8_t)(result);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_p74));
    result = (*(uint64_t *)(arg1 + 0x18)) & (v_stack_m268);
    result = (result) | (1);
    Arg2 = 0;
    *(uint64_t *)(arg1 + 0x18) = result;
loc_002B37C7:
    if (condition_is_above_or_equal) goto loc_002B2E92;
loc_002B37D4:
    local_rbx = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xD11AD0)) & ((uint32_t)(local_rbx))) == 0) goto loc_002B3C22;
loc_002B37E2:
loc_002B37E4:
    if (!sign_flag) goto loc_002B37C7;
    goto loc_002B37D4;
loc_002B37EF:
    Arg2 = (0) & (-67);
    result = MiWriteValidPteNewProtection(local_rbx, Arg2, 128, v_stack_m238);
    goto loc_002B2D05;
loc_002B3809:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD132A9)))) & (64)) == 0) goto loc_002B303E;
    result = KiCheckVpBackingLongSpinWaitHypercall(local_rbx, Arg2, 2, v_stack_m238);
    if ((uint8_t)(result) == 0) goto loc_002B303E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), Arg2, 2, v_stack_m238);
    goto loc_002B3040;
loc_002B3830:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD13282)))) & (64)) == 0) goto loc_002B305E;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbx)), Arg2, 2, v_stack_m238);
    if ((uint8_t)(result) == 0) goto loc_002B305E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), Arg2, 2, v_stack_m238);
    goto loc_002B3060;
loc_002B3857:
    if (((uint16_t)((uint32_t)(*(uint32_t *)(result + 0x20)))) > 2) goto loc_002B3DDF;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m268))) & (66)) == 0) goto loc_002B38E9;
    result = 0;
loc_002B3875:
    if (condition_is_below) goto loc_002B3A00;
    if (((uint16_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(local_rbx)) + 0x20)))) > 2) goto loc_002B3DFA;
    Arg2 = (*(uint64_t *)(v_stack_m268)) & (-67);
    result = MiWriteValidPteNewProtection(v_stack_m268, Arg2, v_stack_m268, v_stack_m238);
    result = MiFlushSingleTbEntry(v_stack_m280, 2, 2 + 8, v_stack_m238);
    result = MiCaptureDirtyBitToPfn(v_stack_m270, 2, 2 + 8, v_stack_m238);
    if (result != 0) goto loc_002B3E11;
loc_002B38CB:
    result = 0;
loc_002B38CF:
    if (condition_is_below) goto loc_002B3A20;
    result = MiCaptureDirtyBitToPfn(local_r15, 2, 2 + 8, v_stack_m238);
loc_002B38E9:
    Arg4 = 0;
    goto loc_002B2E16;
loc_002B38F7:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD131BB)))) & (64)) == 0) goto loc_002B31D0;
    result = KiCheckVpBackingLongSpinWaitHypercall(local_r15, 2, 2 + 8, Arg4);
    if ((uint8_t)(result) == 0) goto loc_002B31D0;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_m268)), 2, 2 + 8, Arg4);
    goto loc_002B31D2;
loc_002B391F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD13193)))) & (64)) == 0) goto loc_002B31EF;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(v_stack_m268)), 2, 2 + 8, Arg4);
    if ((uint8_t)(result) == 0) goto loc_002B31EF;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((uint32_t)(v_stack_mD0))), 2, 2 + 8, Arg4);
    goto loc_002B31F1;
loc_002B3946:
    if ((((uint8_t)((uint32_t)(v_stack_mD0))) & (32)) != 0) goto loc_002B331A;
    Arg1 = (result) + (result);
    if (v_stack_m268 < Arg1) goto loc_002B331A;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_m268, (uint32_t)(v_stack_mD0), 128, Arg4);
    goto loc_002B331A;
loc_002B3988:
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(local_r11))) | (4));
    v_stack_mD0 = (uint32_t)(local_r10);
    goto loc_002B2A20;
loc_002B39A0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD13112)))) & (64)) == 0) goto loc_002B3280;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_m268, (uint32_t)(v_stack_mD0), 128, Arg4);
    if ((uint8_t)(result) == 0) goto loc_002B3280;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_m268)), (uint32_t)(v_stack_mD0), 128, Arg4);
    goto loc_002B3282;
loc_002B39C8:
    result = 0;
loc_002B39CC:
    if (condition_is_above_or_equal) goto loc_002B325E;
loc_002B39D9:
    local_rdi = (uint32_t)((0) + 1);
    if (((*(uint32_t *)(v_rip + 0xD118CB)) & ((uint32_t)(local_rdi))) == 0) goto loc_002B3C9B;
loc_002B39E7:
loc_002B39E9:
    if (!sign_flag) goto loc_002B39CC;
    goto loc_002B39D9;
loc_002B3A00:
    local_rbx = (uint32_t)(((uint32_t)(v_stack_mD0)) + 1);
    if (((*(uint32_t *)(v_rip + 0xD118A4)) & ((uint32_t)(local_rbx))) == 0) goto loc_002B3C49;
loc_002B3A0E:
loc_002B3A10:
    if (!sign_flag) goto loc_002B3875;
    goto loc_002B3A00;
loc_002B3A20:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xD11884)) & ((uint32_t)(local_rbx))) == 0) goto loc_002B3C74;
loc_002B3A2E:
loc_002B3A30:
    if (!sign_flag) goto loc_002B38CF;
    goto loc_002B3A20;
loc_002B3A3F:
    if (((v_stack_mD0) & (256)) == 0) goto loc_002B3137;
    result = MiUnlockProtoPoolPage(v_stack_m270, 17, 128, Arg4);
    goto loc_002B3137;
loc_002B3A5F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD13053)))) & (64)) == 0) goto loc_002B367E;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_m270, 17, 128, Arg4);
    if ((uint8_t)(result) == 0) goto loc_002B367E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), 17, 128, Arg4);
    goto loc_002B3680;
loc_002B3A86:
    Arg2 = 0;
    result = memset(v_stack_m148, Arg2, Arg2 + 112, Arg4);
    result = MI_NODE_FROM_PFN(Arg1, Arg2, Arg2 + 112, Arg4);
    result = (uint32_t)((result) + 1);
    v_stack_p60 = v_stack_m148;
    Arg3 = (uint32_t)((v_stack_mB3) & (1));
    v_stack_p58 = 1;
    Arg1 = 0;
    v_stack_p50 = 0;
    v_stack_p48 = 9;
    v_stack_p40 = 0;
    v_stack_p38 = v_stack_m60;
    v_stack_p30 = (uint32_t)(local_rbx);
    v_stack_p28 = (uint32_t)(local_r15);
    v_stack_p20 = (uint32_t)(result);
    result = MiInitializePageChainPacket(result, v_stack_m258, Arg3, local_rdi);
    result = MiGetPageChain(v_stack_m148, v_stack_m258, Arg3, local_rdi);
    if (v_stack_mE0 == local_rsi) goto loc_002B3D6E;
    if (v_stack_mF0 == 0) goto loc_002B3B42;
    v_stack_mF0 = *(uint64_t *)(v_stack_mF0);
    if (v_stack_mF0 == 0) {
        local_rbx = 0;
        v_stack_mE8 = 0;
    }
    local_r13 = (v_stack_mF0) - (*(uint64_t *)(v_stack_mF0));
    local_r13 = (local_r13) >> (4);
    local_r13 = (local_r13) * (*(uint64_t *)(v_stack_mF0));
    v_stack_m260 = local_r13;
    goto loc_002B2BD1;
loc_002B3B70:
    result = MiVaIsPageFileHash(v_stack_m270, v_stack_m280, Arg3, local_rdi);
    v_stack_m240 = result;
    if (result == 0) goto loc_002B311D;
    result = ExAcquireSpinLockSharedAtDpcLevel(result + 200, v_stack_m280, Arg3, local_rdi);
    result = MiVaIsPageFileHash(v_stack_m270, v_stack_m280, v_stack_m280, local_rdi);
    if (v_stack_m240 != result) goto loc_002B3BC2;
    result = MiSmallVaStillMapsFrame(v_stack_m280, v_stack_m268, v_stack_m280, local_rdi);
    if ((uint32_t)(result) != 0) goto loc_002B2D73;
loc_002B3BC2:
    result = ExReleaseSpinLockSharedFromDpcLevel(result + 200, v_stack_m268, v_stack_m280, local_rdi);
    goto loc_002B3123;
loc_002B3BD5:
    result = MiSanitizeShadowPxe(result + 200, v_stack_m228, v_stack_m280, local_rdi);
    goto loc_002B30F2;
loc_002B3BE9:
    Arg1 = (v_stack_m240) + (200);
    result = ExReleaseSpinLockSharedFromDpcLevel(Arg1, v_stack_m228, v_stack_m280, local_rdi);
    goto loc_002B2F30;
loc_002B3BFE:
    result = MiSetPfnContainingFrame(v_stack_mF0, local_r13, v_stack_m280, local_rdi);
    goto loc_002B2D9C;
loc_002B3C0E:
    result = MiSanitizeShadowPxe(v_stack_mF0, v_stack_m220, v_stack_m280, local_rdi);
    goto loc_002B330B;
loc_002B3C22:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD12E90)))) & (64)) == 0) goto loc_002B37E2;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_mF0, v_stack_m220, v_stack_m280, local_rdi);
    if ((uint8_t)(result) == 0) goto loc_002B37E2;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_m220)), v_stack_m220, v_stack_m280, local_rdi);
    goto loc_002B37E4;
loc_002B3C49:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD12E69)))) & (64)) == 0) goto loc_002B3A0E;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(v_stack_m220)), v_stack_m220, v_stack_m280, local_rdi);
    if ((uint8_t)(result) == 0) goto loc_002B3DF1;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_m220)), v_stack_m220, v_stack_m280, local_rdi);
    goto loc_002B3A10;
loc_002B3C74:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD12E3E)))) & (64)) == 0) goto loc_002B3A2E;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_m270, v_stack_m220, v_stack_m280, local_rdi);
    if ((uint8_t)(result) == 0) goto loc_002B3A2E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(v_stack_m220)), v_stack_m220, v_stack_m280, local_rdi);
    goto loc_002B3A30;
loc_002B3C9B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD12E17)))) & (64)) == 0) goto loc_002B39E7;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(v_stack_m220)), v_stack_m220, v_stack_m280, local_rdi);
    if ((uint8_t)(result) == 0) goto loc_002B39E7;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m220, v_stack_m280, local_rdi);
    goto loc_002B39E9;
loc_002B3CC2:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m220 + 0xB8))) >> (24));
    if ((((uint8_t)(result)) & (2)) == 0) goto loc_002B3CD7;
    local_rsi = (uint32_t)((local_rsi) & (0xFFFFFFFEULL));
    goto loc_002B3731;
loc_002B3CD7:
    if (condition_is_below) goto loc_002B3E4B;
    v_stack_mD0 = (uint32_t)((uint32_t)(v_stack_mD0));
    result = (*(uint64_t *)(v_stack_m1D8 + 0x28)) >> (12);
    if (result != v_stack_m280) goto loc_002B3D42;
loc_002B3D0B:
    Arg3 = 0;
    result = MiReleaseFaultState(v_stack_mC0, 17, Arg3, local_rdi);
    result = KeSwapDirectoryTableBase(v_stack_m1D8, (uint32_t)(v_stack_m1C8), v_stack_m208, local_rdi);
    result = MiLockWorkingSetExclusive(v_stack_m258, (uint32_t)(v_stack_m1C8), v_stack_m208, local_rdi);
    goto loc_002B3731;
loc_002B3D42:
    v_stack_m1C8 = 1;
    v_stack_m1C0 = *(uint64_t *)((uint32_t)(v_stack_m1C8) + 0x508);
    v_stack_mD0 = (uint32_t)(v_stack_m258);
    goto loc_002B3D0B;
loc_002B3D60:
    goto loc_002B314C;
loc_002B3D6E:
    goto loc_002B34A9;
loc_002B3D79:
    goto loc_002B31A5;
loc_002B3D87:
    if (condition_is_below) goto loc_002B2BFD;
    goto loc_002B3137;
loc_002B3DAB:
    goto loc_002B3137;
loc_002B3DC5:
    goto loc_002B3137;
loc_002B3DDF:
    result = MiUnlockProtoPoolPage(v_stack_m258, 17, v_stack_m208, local_rdi);
    goto loc_002B3137;
loc_002B3DF1:
    goto loc_002B3A0E;
loc_002B3DFA:
    result = MiUnlockProtoPoolPage(v_stack_m270, 17, v_stack_m208, local_rdi);
    goto loc_002B3137;
loc_002B3E11:
    Arg1 = (*(uint64_t *)(1 + 0x28)) >> (43);
    Arg1 = (uint32_t)((Arg1) & (0x3FFULL));
    result = MiReleasePageFileInfo(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7C266) + arg1 * 8), result, 1, local_rdi);
    goto loc_002B38CB;
loc_002B3E3D:
    if (((1) & (4)) != 0) goto loc_002B36BF;
    goto loc_002B2E2D;
loc_002B3E4B:
    local_rsi = (uint32_t)((local_rsi) & (0xFFFFFFFEULL));
    goto loc_002B3731;
loc_002B3E53:
    Arg2 = 72;
    if (1 != 17) { Arg2 = 12; }
    result = MiClearPfnImageVerified(Arg1, Arg2, 1, local_rdi);
    goto loc_002B2F1F;
loc_002B3E70:
    goto loc_002B3137;
loc_002B3E8A:
    result = MiPfnIsActivePageTable(v_stack_m278, Arg2, 1, local_rdi);
    result = MiRevertPfnActivePageTable(v_stack_m278, Arg2, 1, local_rdi);
loc_002B3EA8:
loc_002B3EAD:
    goto loc_002B3168;
loc_002B3EC7:
    result = MiReleaseFreshPage(v_stack_m278, Arg2, 1, local_rdi);
    goto loc_002B317D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R/W` |
| `Arg1` | `+ 0x18` | `64` | `W` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `W` |
| `Arg1` | `+ 0x22` | `8` | `R` |
| `Arg1` | `+ 0x23` | `8` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002B28D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
