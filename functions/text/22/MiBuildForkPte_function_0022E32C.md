# MiBuildForkPte

- RVA: `0x0022E32C`–`0x0022F301` (길이 `4,053` bytes)
- VA: `0x000000014022E32C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000600AC`
- 디코드: `961`개 명령, `4,053/4,053` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **81**; 고유 호출 대상: **49**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x0022E446` → [MI_IS_SOFTWARE_PTE_SHADOW_STACK](../38/MI_IS_SOFTWARE_PTE_SHADOW_STACK_function_003815D0.md) (function, `0x003815D0`)
- `0x0022E479` → [MiGetWsleContents](../31/MiGetWsleContents_function_00316540.md) (function, `0x00316540`)
- `0x0022E556` → [MiLockPageTablePage](../23/MiLockPageTablePage_function_0023E120.md) (function, `0x0023E120`)
- `0x0022E566` → [MiReturnCloneCharges](../37/MiReturnCloneCharges_function_00370F50.md) (function, `0x00370F50`)
- `0x0022E5F8` → [MiCaptureDirtyBitToPfn](../37/MiCaptureDirtyBitToPfn_function_00370DD0.md) (function, `0x00370DD0`)
- `0x0022E635` → [MiSetPfnContainingFrame](../36/MiSetPfnContainingFrame_function_00363FC0.md) (function, `0x00363FC0`)
- `0x0022E63E` → [MI_MAKE_PROTECT_WRITE_COPY](MI_MAKE_PROTECT_WRITE_COPY_function_0022F308.md) (function, `0x0022F308`)
- `0x0022E652` → [MiTransferPageFileOwnership](MiTransferPageFileOwnership_function_0022F320.md) (function, `0x0022F320`)
- `0x0022E682` → [MiWriteValidPteNewProtection](../28/MiWriteValidPteNewProtection_function_00281810.md) (function, `0x00281810`)
- `0x0022E6A4` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x0022E6C6` → [MiSetWsleProtection](../29/MiSetWsleProtection_function_002939D8.md) (function, `0x002939D8`)
- `0x0022E6DC` → [MiMakePrototypePteDirect](../29/MiMakePrototypePteDirect_function_00294DE0.md) (function, `0x00294DE0`)
- `0x0022E736` → [MiIncreaseUsedPtesInPfn](../38/MiIncreaseUsedPtesInPfn_function_00382D90.md) (function, `0x00382D90`)
- `0x0022E769` → [MiUpdateWorkingSetPrivateSize](../36/MiUpdateWorkingSetPrivateSize_function_00362250.md) (function, `0x00362250`)
- `0x0022E7FF` → [IS_PTE_NOT_DEMAND_ZERO](IS_PTE_NOT_DEMAND_ZERO_function_0022F4D0.md) (function, `0x0022F4D0`)
- `0x0022E81F` → [MiUpdatePageFileHighInPte](../36/MiUpdatePageFileHighInPte_function_0036D840.md) (function, `0x0036D840`)
- `0x0022E831` → [MI_IS_SOFTWARE_PTE_SHADOW_STACK](../38/MI_IS_SOFTWARE_PTE_SHADOW_STACK_function_003815D0.md) (function, `0x003815D0`)
- `0x0022E850` → [MiFindZeroCloneBlock](MiFindZeroCloneBlock_function_0022F514.md) (function, `0x0022F514`)
- `0x0022E88F` → [MiGetCloneCharges](MiGetCloneCharges_function_0022CB5C.md) (function, `0x0022CB5C`)
- `0x0022E8BB` → [MiGetWsleProtection](../29/MiGetWsleProtection_function_00294A80.md) (function, `0x00294A80`)
- `0x0022E8CB` → [MiMakePrototypePteDirect](../29/MiMakePrototypePteDirect_function_00294DE0.md) (function, `0x00294DE0`)
- `0x0022E922` → [MiReferenceExistingCloneProto](MiReferenceExistingCloneProto_function_0022B040.md) (function, `0x0022B040`)
- `0x0022E93E` → [MiIsPrototypePteVadLookup](../32/MiIsPrototypePteVadLookup_function_00328B70.md) (function, `0x00328B70`)
- `0x0022E957` → [MiIsVadLargePrivate](../32/MiIsVadLargePrivate_function_0032F720.md) (function, `0x0032F720`)
- `0x0022E96D` → [MiMakePerSessionProtoPte](MiMakePerSessionProtoPte_function_0022F7EC.md) (function, `0x0022F7EC`)
- `0x0022E9A2` → [MiIncreaseUsedPtesInPfn](../38/MiIncreaseUsedPtesInPfn_function_00382D90.md) (function, `0x00382D90`)
- `0x0022EA00` → [MiIncrementCombinedPte](MiIncrementCombinedPte_function_0022B248.md) (function, `0x0022B248`)
- `0x0022EA15` → [MiWriteUselessChildPte](../38/MiWriteUselessChildPte_function_00382CFC.md) (function, `0x00382CFC`)
- `0x0022EA2E` → [MiHandleForkTransitionPte](MiHandleForkTransitionPte_function_0022D34C.md) (function, `0x0022D34C`)
- `0x0022EA96` → [MiInitializePageColorBase](../32/MiInitializePageColorBase_function_00320410.md) (function, `0x00320410`)
- `0x0022EB0A` → [MiGetPage](../28/MiGetPage_function_002884C0.md) (function, `0x002884C0`)
- `0x0022EB48` → [MiFinalizePageAttribute](../33/MiFinalizePageAttribute_function_00332E30.md) (function, `0x00332E30`)
- `0x0022EB65` → [MiDuplicateCloneLeaf](../38/MiDuplicateCloneLeaf_function_003825F0.md) (function, `0x003825F0`)
- `0x0022EB9C` → [MiUnlockWorkingSetExclusive](../27/MiUnlockWorkingSetExclusive_function_0027EC70.md) (function, `0x0027EC70`)
- `0x0022EBD4` → [MiPrefetchVirtualMemory](../36/MiPrefetchVirtualMemory_function_0036C560.md) (function, `0x0036C560`)
- `0x0022EBDC` → [MiLockWorkingSetExclusive](../32/MiLockWorkingSetExclusive_function_003238A0.md) (function, `0x003238A0`)
- `0x0022EBF7` → [MiGetProcessorFlushList](../24/MiGetProcessorFlushList_function_00242C90.md) (function, `0x00242C90`)
- `0x0022EC16` → [MiInitializeTbFlushList](../29/MiInitializeTbFlushList_function_00294F00.md) (function, `0x00294F00`)
- `0x0022EC46` → [MI_PROTO_FORMAT_COMBINED](MI_PROTO_FORMAT_COMBINED_function_0022F720.md) (function, `0x0022F720`)
- `0x0022EC6E` → [MiReferenceExistingCloneProto](MiReferenceExistingCloneProto_function_0022B040.md) (function, `0x0022B040`)
- `0x0022EC8C` → [MiIsPrototypePteVadLookup](../32/MiIsPrototypePteVadLookup_function_00328B70.md) (function, `0x00328B70`)
- `0x0022ECA5` → [MiIsVadLargePrivate](../32/MiIsVadLargePrivate_function_0032F720.md) (function, `0x0032F720`)
- `0x0022ECBC` → [MiMakePerSessionProtoPte](MiMakePerSessionProtoPte_function_0022F7EC.md) (function, `0x0022F7EC`)
- `0x0022ED3B` → [MI_IS_SOFTWARE_PTE_SHADOW_STACK](../38/MI_IS_SOFTWARE_PTE_SHADOW_STACK_function_003815D0.md) (function, `0x003815D0`)
- `0x0022EDA4` → [MiGetCloneCharges](MiGetCloneCharges_function_0022CB5C.md) (function, `0x0022CB5C`)
- `0x0022EE00` → [MiUpdatePageFileBlockOwner](MiUpdatePageFileBlockOwner_function_0022F6BC.md) (function, `0x0022F6BC`)
- `0x0022EE33` → [MiMakePrototypePteDirect](../29/MiMakePrototypePteDirect_function_00294DE0.md) (function, `0x00294DE0`)
- `0x0022EE8D` → [MiIncreaseUsedPtesInPfn](../38/MiIncreaseUsedPtesInPfn_function_00382D90.md) (function, `0x00382D90`)
- `0x0022EEED` → [MiWriteSharedDemandZeroPte](../4A/MiWriteSharedDemandZeroPte_function_004A8DDC.md) (function, `0x004A8DDC`)
- `0x0022EF06` → [MiMakePrototypePteVadLookup](../2C/MiMakePrototypePteVadLookup_function_002C3480.md) (function, `0x002C3480`)
- `0x0022EF4C` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x0022EF62` → [MiFindZeroCloneBlock](MiFindZeroCloneBlock_function_0022F514.md) (function, `0x0022F514`)
- `0x0022EF8B` → [MiWriteSharedDemandZeroPte](../4A/MiWriteSharedDemandZeroPte_function_004A8DDC.md) (function, `0x004A8DDC`)
- `0x0022EFCD` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0022EFDC` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0022EFF8` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0022F007` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0022F028` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0022F037` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0022F04E` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x0022F07F` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0022F08F` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0022F0A7` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0022F0B6` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0022F0CE` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0022F0DD` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0022F0F5` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0022F104` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0022F11C` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0022F12B` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0022F13E` → [MiMakeSystemAddressValid](../27/MiMakeSystemAddressValid_function_0027FF70.md) (function, `0x0027FF70`)
- `0x0022F185` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x0022F18A` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x0022F1B7` → [MiCaptureWriteWatchDirtyBit](../46/MiCaptureWriteWatchDirtyBit_function_00465224.md) (function, `0x00465224`)
- `0x0022F242` → [MiIncrementCombinedPte](MiIncrementCombinedPte_function_0022B248.md) (function, `0x0022B248`)
- `0x0022F26A` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x0022F26F` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)
- `0x0022F2A7` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)
- `0x0022F2B0` → [MiClearPageFileReservation](../32/MiClearPageFileReservation_function_0032B68C.md) (function, `0x0032B68C`)
- `0x0022F2C8` → [MiClearPageFileReservation](../32/MiClearPageFileReservation_function_0032B68C.md) (function, `0x0032B68C`)
- `0x0022F2F7` → [MiLockAndInsertPageInFreeList](../47/MiLockAndInsertPageInFreeList_function_00470FA8.md) (function, `0x00470FA8`)

### Direct callers
- [MiCloneVads](MiCloneVads_function_0022DC1C.md) at `0x0022DFB6`

### Static image references
- `0x0022E4D7` → RVA `0x00010880` (`.rdata`; read)
- `0x0022E4E4` → RVA `0x00E30088` (`.data`; read)
- `0x0022E6A9` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x0022E779` → RVA `0x000105C0` (`.rdata`; read)
- `0x0022E9C1` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0022EAAD` → RVA `0x00E2DCC0` (`.data`; read)
- `0x0022EC20` → RVA `0x00E2DC80` (`.data`; read)
- `0x0022EFBF` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x0022F1EE` → [sub_006D7206](../6D/Unknown_function_006D7206.md) (`tail-transfer`)
  - `0x0022F1F8` → [sub_006D7206](../6D/Unknown_function_006D7206.md) (`tail-transfer`)
  - `0x0022F204` → [sub_006D7206](../6D/Unknown_function_006D7206.md) (`tail-transfer`)
  - `0x0022F264` → [sub_006D7206 + 0x21](../6D/Unknown_function_006D7206.md) (`tail-transfer`)
  - `0x0022F279` → [sub_006D7206 + 0x21](../6D/Unknown_function_006D7206.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0022E32C  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0022E331  55                              push rbp
0022E332  53                              push rbx
0022E333  56                              push rsi
0022E334  57                              push rdi
0022E335  41 54                           push r12
0022E337  41 55                           push r13
0022E339  41 56                           push r14
0022E33B  41 57                           push r15
0022E33D  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
0022E342  48 81 EC C8 00 00 00            sub rsp, 0xc8
0022E349  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
0022E34D  0F 57 C0                        xorps xmm0, xmm0
0022E350  48 83 65 97 00                  and qword ptr [rbp - 0x69], 0
0022E355  4C 8B F9                        mov r15, rcx
0022E358  48 8B 79 28                     mov rdi, qword ptr [rcx + 0x28]
0022E35C  48 8B 59 10                     mov rbx, qword ptr [rcx + 0x10]
0022E360  4C 8B 59 08                     mov r11, qword ptr [rcx + 8]
0022E364  4C 8B 69 40                     mov r13, qword ptr [rcx + 0x40]
0022E368  48 8B 51 30                     mov rdx, qword ptr [rcx + 0x30]
0022E36C  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
0022E370  48 8B 00                        mov rax, qword ptr [rax]
0022E373  48 89 7D DF                     mov qword ptr [rbp - 0x21], rdi
0022E377  48 89 5D F7                     mov qword ptr [rbp - 9], rbx
0022E37B  4C 89 5D 8F                     mov qword ptr [rbp - 0x71], r11
0022E37F  4C 89 6D 87                     mov qword ptr [rbp - 0x79], r13
0022E383  48 89 45 7F                     mov qword ptr [rbp + 0x7f], rax
0022E387  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
0022E38B  48 85 C0                        test rax, rax
0022E38E  0F 84 1C 04 00 00               je 0x14022e7b0
0022E394  4C 8B 29                        mov r13, qword ptr [rcx]
0022E397  33 DB                           xor ebx, ebx
0022E399  4C 8B 61 48                     mov r12, qword ptr [rcx + 0x48]
0022E39D  33 FF                           xor edi, edi
0022E39F  48 83 4D AF FF                  or qword ptr [rbp - 0x51], 0xffffffffffffffff
0022E3A4  4C 89 6D 9F                     mov qword ptr [rbp - 0x61], r13
0022E3A8  49 8D B5 00 04 00 00            lea rsi, [r13 + 0x400]
0022E3AF  48 89 75 A7                     mov qword ptr [rbp - 0x59], rsi
0022E3B3  44 8D 4B 01                     lea r9d, [rbx + 1]
0022E3B7  49 BD 00 00 00 00 80 F6 FF FF   movabs r13, 0xfffff68000000000
0022E3C1  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
0022E3CB  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
0022E3D5  4C 8B 75 BF                     mov r14, qword ptr [rbp - 0x41]
0022E3D9  0F 57 C0                        xorps xmm0, xmm0
0022E3DC  41 0F 11 04 24                  movups xmmword ptr [r12], xmm0
0022E3E1  41 0F 11 44 24 10               movups xmmword ptr [r12 + 0x10], xmm0
0022E3E7  49 C7 44 24 18 02 00 00 00      mov qword ptr [r12 + 0x18], 2
0022E3F0  85 FF                           test edi, edi
0022E3F2  0F 85 3D 0D 00 00               jne 0x14022f135
0022E3F8  4C 8B 45 7F                     mov r8, qword ptr [rbp + 0x7f]
0022E3FC  45 33 D2                        xor r10d, r10d
0022E3FF  44 89 4D 77                     mov dword ptr [rbp + 0x77], r9d
0022E403  44 89 55 6F                     mov dword ptr [rbp + 0x6f], r10d
0022E407  41 8B F9                        mov edi, r9d
0022E40A  45 84 C1                        test r9b, r8b
0022E40D  0F 84 C9 03 00 00               je 0x14022e7dc
0022E413  49 C1 E8 0C                     shr r8, 0xc
0022E417  4C 23 C0                        and r8, rax
0022E41A  4F 8D 2C 40                     lea r13, [r8 + r8*2]
0022E41E  49 C1 E5 04                     shl r13, 4
0022E422  48 8B C1                        mov rax, rcx
0022E425  4C 03 E8                        add r13, rax
0022E428  85 DB                           test ebx, ebx
0022E42A  0F 85 58 06 00 00               jne 0x14022ea88
0022E430  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
0022E434  49 8D 75 28                     lea rsi, [r13 + 0x28]
0022E438  66 41 3B C1                     cmp ax, r9w
0022E43C  0F 87 36 06 00 00               ja 0x14022ea78
0022E442  49 8B 4D 10                     mov rcx, qword ptr [r13 + 0x10]
0022E446  E8 85 31 15 00                  call 0x1403815d0
0022E44B  85 C0                           test eax, eax
0022E44D  0F 85 31 06 00 00               jne 0x14022ea84
0022E453  49 8B FE                        mov rdi, r14
0022E456  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0022E460  48 C1 E7 19                     shl rdi, 0x19
0022E464  48 8B C0                        mov rax, rax
0022E467  48 C1 E0 19                     shl rax, 0x19
0022E46B  48 2B F8                        sub rdi, rax
0022E46E  48 C1 FF 10                     sar rdi, 0x10
0022E472  48 8B D7                        mov rdx, rdi
0022E475  48 89 7D D7                     mov qword ptr [rbp - 0x29], rdi
0022E479  E8 C2 80 0E 00                  call 0x140316540
0022E47E  48 8B 0E                        mov rcx, qword ptr [rsi]
0022E481  8A D8                           mov bl, al
0022E483  48 85 C9                        test rcx, rcx
0022E486  0F 88 19 04 00 00               js 0x14022e8a5
0022E48C  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0022E496  4D 8B F4                        mov r14, r12
0022E499  49 C1 EE 09                     shr r14, 9
0022E49D  4C 23 F0                        and r14, rax
0022E4A0  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0022E4AA  48 8B C0                        mov rax, rax
0022E4AD  4D 8B 34 06                     mov r14, qword ptr [r14 + rax]
0022E4B1  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
0022E4BB  49 C1 EE 0C                     shr r14, 0xc
0022E4BF  4C 23 F0                        and r14, rax
0022E4C2  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0022E4CC  4F 8D 04 76                     lea r8, [r14 + r14*2]
0022E4D0  49 C1 E0 04                     shl r8, 4
0022E4D4  48 8B C0                        mov rax, rax
0022E4D7  48 8B 3D A2 23 DE FF            mov rdi, qword ptr [rip - 0x21dc5e]
0022E4DE  4C 03 C0                        add r8, rax
0022E4E1  48 8B 06                        mov rax, qword ptr [rsi]
0022E4E4  48 8B 0D 9D 1B C0 00            mov rcx, qword ptr [rip + 0xc01b9d]
0022E4EB  48 C1 E8 2B                     shr rax, 0x2b
0022E4EF  25 FF 03 00 00                  and eax, 0x3ff
0022E4F4  4C 89 45 B7                     mov qword ptr [rbp - 0x49], r8
0022E4F8  4C 8B 0C C1                     mov r9, qword ptr [rcx + rax*8]
0022E4FC  41 0F B7 83 AE 04 00 00         movzx eax, word ptr [r11 + 0x4ae]
0022E504  4C 89 4D CF                     mov qword ptr [rbp - 0x31], r9
0022E508  4C 39 0C C1                     cmp qword ptr [rcx + rax*8], r9
0022E50C  0F 85 5B 0C 00 00               jne 0x14022f16d
0022E512  49 8B 74 24 10                  mov rsi, qword ptr [r12 + 0x10]
0022E517  41 8B 47 18                     mov eax, dword ptr [r15 + 0x18]
0022E51B  A8 01                           test al, 1
0022E51D  74 1E                           je 0x14022e53d
0022E51F  41 83 CA 02                     or r10d, 2
0022E523  48 B8 3F 00 00 00 00 00 00 F0   movabs rax, 0xf00000000000003f
0022E52D  48 23 F0                        and rsi, rax
0022E530  44 89 55 6F                     mov dword ptr [rbp + 0x6f], r10d
0022E534  48 83 CE 20                     or rsi, 0x20
0022E538  49 89 74 24 10                  mov qword ptr [r12 + 0x10], rsi
0022E53D  45 85 D2                        test r10d, r10d
0022E540  0F 85 43 03 00 00               jne 0x14022e889
0022E546  80 E3 0F                        and bl, 0xf
0022E549  80 FB 08                        cmp bl, 8
0022E54C  75 36                           jne 0x14022e584
0022E54E  BA 03 00 00 00                  mov edx, 3
0022E553  49 8B C8                        mov rcx, r8
0022E556  E8 C5 FB 00 00                  call 0x14023e120
0022E55B  85 C0                           test eax, eax
0022E55D  75 25                           jne 0x14022e584
0022E55F  8B 55 6F                        mov edx, dword ptr [rbp + 0x6f]
0022E562  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
0022E566  E8 E5 29 14 00                  call 0x140370f50
0022E56B  4C 8B 5D 8F                     mov r11, qword ptr [rbp - 0x71]
0022E56F  41 B9 01 00 00 00               mov r9d, 1
0022E575  8B 7D 77                        mov edi, dword ptr [rbp + 0x77]
0022E578  41 8B D9                        mov ebx, r9d
0022E57B  48 8B 75 A7                     mov rsi, qword ptr [rbp - 0x59]
0022E57F  E9 33 FE FF FF                  jmp 0x14022e3b7
0022E584  48 8B 55 B7                     mov rdx, qword ptr [rbp - 0x49]
0022E588  33 DB                           xor ebx, ebx
0022E58A  F0 48 0F BA 6A 18 3F            lock bts qword ptr [rdx + 0x18], 0x3f
0022E591  0F 82 28 04 00 00               jb 0x14022e9bf
0022E597  48 8B 42 18                     mov rax, qword ptr [rdx + 0x18]
0022E59B  49 B8 00 00 00 00 00 00 00 C0   movabs r8, 0xc000000000000000
0022E5A5  48 BB FF FF FF FF FF FF FF 7F   movabs rbx, 0x7fffffffffffffff
0022E5AF  48 8D 48 01                     lea rcx, [rax + 1]
0022E5B3  48 33 C1                        xor rax, rcx
0022E5B6  49 23 C0                        and rax, r8
0022E5B9  48 33 C1                        xor rax, rcx
0022E5BC  48 89 42 18                     mov qword ptr [rdx + 0x18], rax
0022E5C0  F0 48 21 5A 18                  lock and qword ptr [rdx + 0x18], rbx
0022E5C5  F6 45 7F 42                     test byte ptr [rbp + 0x7f], 0x42
0022E5C9  0F 84 90 04 00 00               je 0x14022ea5f
0022E5CF  4C 8B 45 DF                     mov r8, qword ptr [rbp - 0x21]
0022E5D3  B9 00 00 60 00                  mov ecx, 0x600000
0022E5D8  41 8B 40 30                     mov eax, dword ptr [r8 + 0x30]
0022E5DC  23 C1                           and eax, ecx
0022E5DE  3B C1                           cmp eax, ecx
0022E5E0  0F 84 BC 0B 00 00               je 0x14022f1a2
0022E5E6  33 FF                           xor edi, edi
0022E5E8  F0 49 0F BA 6D 18 3F            lock bts qword ptr [r13 + 0x18], 0x3f
0022E5EF  0F 82 4B 04 00 00               jb 0x14022ea40
0022E5F5  49 8B CD                        mov rcx, r13
0022E5F8  E8 D3 27 14 00                  call 0x140370dd0
0022E5FD  48 83 65 7F BD                  and qword ptr [rbp + 0x7f], 0xffffffffffffffbd
0022E602  48 8B F8                        mov rdi, rax
0022E605  4D 8B 45 10                     mov r8, qword ptr [r13 + 0x10]
0022E609  41 8A C0                        mov al, r8b
0022E60C  D0 E8                           shr al, 1
0022E60E  A8 01                           test al, 1
0022E610  0F 85 AB 0B 00 00               jne 0x14022f1c1
0022E616  4D 89 65 08                     mov qword ptr [r13 + 8], r12
0022E61A  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
0022E624  49 8B 45 28                     mov rax, qword ptr [r13 + 0x28]
0022E628  49 8B D6                        mov rdx, r14
0022E62B  48 0B C1                        or rax, rcx
0022E62E  49 8B CD                        mov rcx, r13
0022E631  49 89 45 28                     mov qword ptr [r13 + 0x28], rax
0022E635  E8 86 59 13 00                  call 0x140363fc0
0022E63A  49 8D 4D 10                     lea rcx, [r13 + 0x10]
0022E63E  E8 C5 0C 00 00                  call 0x14022f308
0022E643  4D 8B 75 10                     mov r14, qword ptr [r13 + 0x10]
0022E647  49 8B CD                        mov rcx, r13
0022E64A  48 8B 55 BF                     mov rdx, qword ptr [rbp - 0x41]
0022E64E  49 C1 EE 05                     shr r14, 5
0022E652  E8 C9 0C 00 00                  call 0x14022f320
0022E657  F0 49 21 5D 18                  lock and qword ptr [r13 + 0x18], rbx
0022E65C  48 85 FF                        test rdi, rdi
0022E65F  0F 85 DC 09 00 00               jne 0x14022f041
0022E665  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
0022E669  48 0F BA E2 0B                  bt rdx, 0xb
0022E66E  73 0E                           jae 0x14022e67e
0022E670  48 0F BA F2 0B                  btr rdx, 0xb
0022E675  48 0F BA EA 09                  bts rdx, 9
0022E67A  48 89 55 7F                     mov qword ptr [rbp + 0x7f], rdx
0022E67E  48 8B 4D BF                     mov rcx, qword ptr [rbp - 0x41]
0022E682  E8 89 31 05 00                  call 0x140281810
0022E687  49 83 7F 68 00                  cmp qword ptr [r15 + 0x68], 0
0022E68C  0F 84 65 05 00 00               je 0x14022ebf7
0022E692  48 8B 7D D7                     mov rdi, qword ptr [rbp - 0x29]
0022E696  45 33 C9                        xor r9d, r9d
0022E699  49 8B 4F 68                     mov rcx, qword ptr [r15 + 0x68]
0022E69D  48 8B D7                        mov rdx, rdi
0022E6A0  45 8D 41 01                     lea r8d, [r9 + 1]
0022E6A4  E8 C7 4F 06 00                  call 0x140293670
0022E6A9  48 0F BA 25 D6 83 D9 00 24      bt qword ptr [rip + 0xd983d6], 0x24
0022E6B2  48 8B 5D 7F                     mov rbx, qword ptr [rbp + 0x7f]
0022E6B6  0F 82 58 08 00 00               jb 0x14022ef14
0022E6BC  45 33 C0                        xor r8d, r8d
0022E6BF  49 89 1C 24                     mov qword ptr [r12], rbx
0022E6C3  48 8B D7                        mov rdx, rdi
0022E6C6  E8 0D 53 06 00                  call 0x1402939d8
0022E6CB  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
0022E6CF  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
0022E6D9  48 0B C8                        or rcx, rax
0022E6DC  E8 FF 66 06 00                  call 0x140294de0
0022E6E1  41 8B 4F 18                     mov ecx, dword ptr [r15 + 0x18]
0022E6E5  48 89 45 7F                     mov qword ptr [rbp + 0x7f], rax
0022E6E9  F6 C1 01                        test cl, 1
0022E6EC  74 0C                           je 0x14022e6fa
0022E6EE  49 FF 47 20                     inc qword ptr [r15 + 0x20]
0022E6F2  48 83 C8 08                     or rax, 8
0022E6F6  48 89 45 7F                     mov qword ptr [rbp + 0x7f], rax
0022E6FA  41 8B CE                        mov ecx, r14d
0022E6FD  48 33 CE                        xor rcx, rsi
0022E700  41 8B C6                        mov eax, r14d
0022E703  48 83 E1 E0                     and rcx, 0xffffffffffffffe0
0022E707  48 33 C8                        xor rcx, rax
0022E70A  49 89 4C 24 10                  mov qword ptr [r12 + 0x10], rcx
0022E70F  33 DB                           xor ebx, ebx
0022E711  49 8B 7F 50                     mov rdi, qword ptr [r15 + 0x50]
0022E715  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
0022E71C  0F 82 BC 02 00 00               jb 0x14022e9de
0022E722  48 8B 4D 87                     mov rcx, qword ptr [rbp - 0x79]
0022E726  BA 01 00 00 00                  mov edx, 1
0022E72B  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
0022E72F  48 89 01                        mov qword ptr [rcx], rax
0022E732  49 8B 4F 50                     mov rcx, qword ptr [r15 + 0x50]
0022E736  E8 55 46 15 00                  call 0x140382d90
0022E73B  4D 8B 5F 50                     mov r11, qword ptr [r15 + 0x50]
0022E73F  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0022E749  F0 49 21 43 18                  lock and qword ptr [r11 + 0x18], rax
0022E74E  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
0022E752  45 33 C9                        xor r9d, r9d
0022E755  48 8B 55 D7                     mov rdx, qword ptr [rbp - 0x29]
0022E759  49 83 C8 FF                     or r8, 0xffffffffffffffff
0022E75D  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
0022E761  F0 48 FF 88 88 02 00 00         lock dec qword ptr [rax + 0x288]
0022E769  E8 E2 3A 13 00                  call 0x140362250
0022E76E  49 83 47 48 20                  add qword ptr [r15 + 0x48], 0x20
0022E773  F3 41 0F 6F 47 38               movdqu xmm0, xmmword ptr [r15 + 0x38]
0022E779  66 0F 6F 0D 3F 1E DE FF         movdqa xmm1, xmmword ptr [rip - 0x21e1c1]
0022E781  66 0F D4 C8                     paddq xmm1, xmm0
0022E785  F3 41 0F 7F 4F 38               movdqu xmmword ptr [r15 + 0x38], xmm1
0022E78B  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
0022E78F  48 83 F8 FF                     cmp rax, -1
0022E793  0F 85 46 0B 00 00               jne 0x14022f2df
0022E799  33 C0                           xor eax, eax
0022E79B  48 81 C4 C8 00 00 00            add rsp, 0xc8
0022E7A2  41 5F                           pop r15
0022E7A4  41 5E                           pop r14
0022E7A6  41 5D                           pop r13
0022E7A8  41 5C                           pop r12
0022E7AA  5F                              pop rdi
0022E7AB  5E                              pop rsi
0022E7AC  5B                              pop rbx
0022E7AD  5D                              pop rbp
0022E7AE  C3                              ret
0022E7AF  CC                              int3
0022E7B0  48 85 DB                        test rbx, rbx
0022E7B3  74 0D                           je 0x14022e7c2
0022E7B5  F7 42 30 00 00 00 02            test dword ptr [rdx + 0x30], 0x2000000
0022E7BC  0F 85 94 07 00 00               jne 0x14022ef56
0022E7C2  F3 41 0F 6F 47 38               movdqu xmm0, xmmword ptr [r15 + 0x38]
0022E7C8  66 0F 6F 0D F0 1D DE FF         movdqa xmm1, xmmword ptr [rip - 0x21e210]
0022E7D0  66 0F D4 C8                     paddq xmm1, xmm0
0022E7D4  F3 41 0F 7F 4F 38               movdqu xmmword ptr [r15 + 0x38], xmm1
0022E7DA  EB BD                           jmp 0x14022e799
0022E7DC  49 0F BA E0 0A                  bt r8, 0xa
0022E7E1  0F 82 39 04 00 00               jb 0x14022ec20
0022E7E7  49 0F BA E0 0B                  bt r8, 0xb
0022E7EC  0F 82 35 02 00 00               jb 0x14022ea27
0022E7F2  49 8B F8                        mov rdi, r8
0022E7F5  49 8B C8                        mov rcx, r8
0022E7F8  48 C1 EF 05                     shr rdi, 5
0022E7FC  83 E7 1F                        and edi, 0x1f
0022E7FF  E8 CC 0C 00 00                  call 0x14022f4d0
0022E804  85 C0                           test eax, eax
0022E806  0F 85 67 03 00 00               jne 0x14022eb73
0022E80C  41 8A C0                        mov al, r8b
0022E80F  D0 E8                           shr al, 1
0022E811  41 84 C1                        test r9b, al
0022E814  0F 85 AA 0A 00 00               jne 0x14022f2c4
0022E81A  33 D2                           xor edx, edx
0022E81C  49 8B C8                        mov rcx, r8
0022E81F  E8 1C F0 13 00                  call 0x14036d840
0022E824  48 25 FF 0F FF FF               and rax, 0xffffffffffff0fff
0022E82A  48 8B C8                        mov rcx, rax
0022E82D  48 89 45 7F                     mov qword ptr [rbp + 0x7f], rax
0022E831  E8 9A 2D 15 00                  call 0x1403815d0
0022E836  85 C0                           test eax, eax
0022E838  0F 85 D3 07 00 00               jne 0x14022f011
0022E83E  48 8B 5D F7                     mov rbx, qword ptr [rbp - 9]
0022E842  48 85 DB                        test rbx, rbx
0022E845  0F 84 C6 07 00 00               je 0x14022f011
0022E84B  8B D7                           mov edx, edi
0022E84D  48 8B CB                        mov rcx, rbx
0022E850  E8 BF 0C 00 00                  call 0x14022f514
0022E855  4C 8B 6D 87                     mov r13, qword ptr [rbp - 0x79]
0022E859  4C 8B C0                        mov r8, rax
0022E85C  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
0022E860  48 85 C0                        test rax, rax
0022E863  0F 85 6C 06 00 00               jne 0x14022eed5
0022E869  49 8B 7F 50                     mov rdi, qword ptr [r15 + 0x50]
0022E86D  33 DB                           xor ebx, ebx
0022E86F  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
0022E876  0F 82 9D 04 00 00               jb 0x14022ed19
0022E87C  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
0022E880  49 89 45 00                     mov qword ptr [r13], rax
0022E884  E9 10 01 00 00                  jmp 0x14022e999
0022E889  41 8B D2                        mov edx, r10d
0022E88C  49 8B C9                        mov rcx, r9
0022E88F  E8 C8 E2 FF FF                  call 0x14022cb5c
0022E894  85 C0                           test eax, eax
0022E896  0F 84 71 01 00 00               je 0x14022ea0d
0022E89C  4C 8B 45 B7                     mov r8, qword ptr [rbp - 0x49]
0022E8A0  E9 A1 FC FF FF                  jmp 0x14022e546
0022E8A5  4D 8B 5D 08                     mov r11, qword ptr [r13 + 8]
0022E8A9  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
0022E8B3  8A D3                           mov dl, bl
0022E8B5  48 8B CF                        mov rcx, rdi
0022E8B8  4C 0B D8                        or r11, rax
0022E8BB  E8 C0 61 06 00                  call 0x140294a80
0022E8C0  85 C0                           test eax, eax
0022E8C2  0F 85 3C 06 00 00               jne 0x14022ef04
0022E8C8  49 8B CB                        mov rcx, r11
0022E8CB  E8 10 65 06 00                  call 0x140294de0
0022E8D0  48 89 45 7F                     mov qword ptr [rbp + 0x7f], rax
0022E8D4  48 8B 06                        mov rax, qword ptr [rsi]
0022E8D7  48 0F BA E0 28                  bt rax, 0x28
0022E8DC  72 0D                           jb 0x14022e8eb
0022E8DE  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
0022E8E2  48 85 C0                        test rax, rax
0022E8E5  0F 89 1E 09 00 00               jns 0x14022f209
0022E8EB  49 8B 45 28                     mov rax, qword ptr [r13 + 0x28]
0022E8EF  48 0F BA E0 28                  bt rax, 0x28
0022E8F4  72 0D                           jb 0x14022e903
0022E8F6  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
0022E8FA  48 85 C0                        test rax, rax
0022E8FD  0F 89 1E 09 00 00               jns 0x14022f221
0022E903  48 8B 5D 8F                     mov rbx, qword ptr [rbp - 0x71]
0022E907  48 8D 45 97                     lea rax, [rbp - 0x69]
0022E90B  45 8B 47 18                     mov r8d, dword ptr [r15 + 0x18]
0022E90F  4D 8D 4F 20                     lea r9, [r15 + 0x20]
0022E913  49 8B D3                        mov rdx, r11
0022E916  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0022E91B  48 8D 8B 00 04 00 00            lea rcx, [rbx + 0x400]
0022E922  E8 19 C7 FF FF                  call 0x14022b040
0022E927  85 C0                           test eax, eax
0022E929  0F 84 DE 00 00 00               je 0x14022ea0d
0022E92F  48 83 7D 97 00                  cmp qword ptr [rbp - 0x69], 0
0022E934  0F 85 7B 06 00 00               jne 0x14022efb5
0022E93A  49 8B 4D 10                     mov rcx, qword ptr [r13 + 0x10]
0022E93E  E8 2D A2 0F 00                  call 0x140328b70
0022E943  85 C0                           test eax, eax
0022E945  75 34                           jne 0x14022e97b
0022E947  48 8B 7D DF                     mov rdi, qword ptr [rbp - 0x21]
0022E94B  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
0022E94E  24 70                           and al, 0x70
0022E950  3C 20                           cmp al, 0x20
0022E952  75 27                           jne 0x14022e97b
0022E954  48 8B CF                        mov rcx, rdi
0022E957  E8 C4 0D 10 00                  call 0x14032f720
0022E95C  85 C0                           test eax, eax
0022E95E  75 1B                           jne 0x14022e97b
0022E960  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
0022E964  4C 8B CF                        mov r9, rdi
0022E967  4D 8B C6                        mov r8, r14
0022E96A  48 8B D3                        mov rdx, rbx
0022E96D  E8 7A 0E 00 00                  call 0x14022f7ec
0022E972  48 85 C0                        test rax, rax
0022E975  0F 85 D9 08 00 00               jne 0x14022f254
0022E97B  49 8B 7F 50                     mov rdi, qword ptr [r15 + 0x50]
0022E97F  33 DB                           xor ebx, ebx
0022E981  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
0022E988  0F 82 28 05 00 00               jb 0x14022eeb6
0022E98E  48 8B 4D 87                     mov rcx, qword ptr [rbp - 0x79]
0022E992  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
0022E996  48 89 01                        mov qword ptr [rcx], rax
0022E999  49 8B 4F 50                     mov rcx, qword ptr [r15 + 0x50]
0022E99D  BA 01 00 00 00                  mov edx, 1
0022E9A2  E8 E9 43 15 00                  call 0x140382d90
0022E9A7  4D 8B 5F 50                     mov r11, qword ptr [r15 + 0x50]
0022E9AB  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0022E9B5  F0 49 21 43 18                  lock and qword ptr [r11 + 0x18], rax
0022E9BA  E9 B4 FD FF FF                  jmp 0x14022e773
0022E9BF  FF C3                           inc ebx
0022E9C1  85 1D E5 68 D9 00               test dword ptr [rip + 0xd968e5], ebx
0022E9C7  0F 84 F2 05 00 00               je 0x14022efbf
0022E9CD  F3 90                           pause
0022E9CF  48 8B 42 18                     mov rax, qword ptr [rdx + 0x18]
0022E9D3  48 85 C0                        test rax, rax
0022E9D6  0F 89 AE FB FF FF               jns 0x14022e58a
0022E9DC  EB E1                           jmp 0x14022e9bf
0022E9DE  FF C3                           inc ebx
0022E9E0  85 1D C6 68 D9 00               test dword ptr [rip + 0xd968c6], ebx
0022E9E6  0F 84 FE 05 00 00               je 0x14022efea
0022E9EC  F3 90                           pause
0022E9EE  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0022E9F2  48 85 C0                        test rax, rax
0022E9F5  0F 89 1A FD FF FF               jns 0x14022e715
0022E9FB  EB E1                           jmp 0x14022e9de
0022E9FD  45 8B C1                        mov r8d, r9d
0022EA00  E8 43 C8 FF FF                  call 0x14022b248
0022EA05  85 C0                           test eax, eax
0022EA07  0F 85 BD 02 00 00               jne 0x14022ecca
0022EA0D  49 8B 57 50                     mov rdx, qword ptr [r15 + 0x50]
0022EA11  48 8B 4D 87                     mov rcx, qword ptr [rbp - 0x79]
0022EA15  E8 E2 42 15 00                  call 0x140382cfc
0022EA1A  41 C7 47 60 01 00 00 00         mov dword ptr [r15 + 0x60], 1
0022EA22  E9 4C FD FF FF                  jmp 0x14022e773
0022EA27  48 8D 55 AF                     lea rdx, [rbp - 0x51]
0022EA2B  49 8B CF                        mov rcx, r15
0022EA2E  E8 19 E9 FF FF                  call 0x14022d34c
0022EA33  85 C0                           test eax, eax
0022EA35  0F 85 50 FD FF FF               jne 0x14022e78b
0022EA3B  E9 A8 01 00 00                  jmp 0x14022ebe8
0022EA40  FF C7                           inc edi
0022EA42  85 3D 64 68 D9 00               test dword ptr [rip + 0xd96864], edi
0022EA48  0F 84 CC 05 00 00               je 0x14022f01a
0022EA4E  F3 90                           pause
0022EA50  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
0022EA54  48 85 C0                        test rax, rax
0022EA57  0F 89 8B FB FF FF               jns 0x14022e5e8
0022EA5D  EB E1                           jmp 0x14022ea40
0022EA5F  45 33 FF                        xor r15d, r15d
0022EA62  F0 49 0F BA 6D 18 3F            lock bts qword ptr [r13 + 0x18], 0x3f
0022EA69  0F 82 89 02 00 00               jb 0x14022ecf8
0022EA6F  4C 8B 7D 67                     mov r15, qword ptr [rbp + 0x67]
0022EA73  E9 8D FB FF FF                  jmp 0x14022e605
0022EA78  48 8B 06                        mov rax, qword ptr [rsi]
0022EA7B  48 85 C0                        test rax, rax
0022EA7E  0F 88 BE F9 FF FF               js 0x14022e442
0022EA84  48 8B 75 A7                     mov rsi, qword ptr [rbp - 0x59]
0022EA88  45 33 C0                        xor r8d, r8d
0022EA8B  4C 8D 4D E7                     lea r9, [rbp - 0x19]
0022EA8F  48 8B CE                        mov rcx, rsi
0022EA92  41 8D 50 03                     lea edx, [r8 + 3]
0022EA96  E8 75 19 0F 00                  call 0x140320410
0022EA9B  4C 8B 4D E7                     mov r9, qword ptr [rbp - 0x19]
0022EA9F  B8 01 00 00 00                  mov eax, 1
0022EAA4  F0 41 0F C1 01                  lock xadd dword ptr [r9], eax
0022EAA9  48 8B 5D 8F                     mov rbx, qword ptr [rbp - 0x71]
0022EAAD  4C 8D 05 0C F2 BF 00            lea r8, [rip + 0xbff20c]
0022EAB4  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
0022EAB8  33 D2                           xor edx, edx
0022EABA  48 C1 E9 10                     shr rcx, 0x10
0022EABE  83 E1 03                        and ecx, 3
0022EAC1  41 F7 34 88                     div dword ptr [r8 + rcx*4]
0022EAC5  48 8B 05 BC 15 C0 00            mov rax, qword ptr [rip + 0xc015bc]
0022EACC  0F B7 8B AE 04 00 00            movzx ecx, word ptr [rbx + 0x4ae]
0022EAD3  48 8B 1C C8                     mov rbx, qword ptr [rax + rcx*8]
0022EAD7  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
0022EADB  48 83 F8 FF                     cmp rax, -1
0022EADF  75 3C                           jne 0x14022eb1d
0022EAE1  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
0022EAE5  41 B8 01 00 00 00               mov r8d, 1
0022EAEB  C1 E8 10                        shr eax, 0x10
0022EAEE  0F B6 C8                        movzx ecx, al
0022EAF1  0F B6 C2                        movzx eax, dl
0022EAF4  83 E1 C0                        and ecx, 0xffffffc0
0022EAF7  8B 55 EF                        mov edx, dword ptr [rbp - 0x11]
0022EAFA  C1 E1 0C                        shl ecx, 0xc
0022EAFD  81 E2 00 FF F3 FF               and edx, 0xfff3ff00
0022EB03  0B C8                           or ecx, eax
0022EB05  0B D1                           or edx, ecx
0022EB07  48 8B CB                        mov rcx, rbx
0022EB0A  E8 B1 99 05 00                  call 0x1402884c0
0022EB0F  48 89 45 AF                     mov qword ptr [rbp - 0x51], rax
0022EB13  48 83 F8 FF                     cmp rax, -1
0022EB17  0F 84 40 07 00 00               je 0x14022f25d
0022EB1D  48 8D 0C 40                     lea rcx, [rax + rax*2]
0022EB21  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0022EB2B  48 C1 E1 04                     shl rcx, 4
0022EB2F  48 8B C0                        mov rax, rax
0022EB32  48 03 C8                        add rcx, rax
0022EB35  41 B8 10 00 00 00               mov r8d, 0x10
0022EB3B  41 8B 45 20                     mov eax, dword ptr [r13 + 0x20]
0022EB3F  C1 E8 10                        shr eax, 0x10
0022EB42  0F B6 D0                        movzx edx, al
0022EB45  C1 EA 06                        shr edx, 6
0022EB48  E8 E3 42 10 00                  call 0x140332e30
0022EB4D  41 8A 47 1C                     mov al, byte ptr [r15 + 0x1c]
0022EB51  4D 8B 4F 50                     mov r9, qword ptr [r15 + 0x50]
0022EB55  4C 8B 45 AF                     mov r8, qword ptr [rbp - 0x51]
0022EB59  49 8B 57 40                     mov rdx, qword ptr [r15 + 0x40]
0022EB5D  49 8B 4F 38                     mov rcx, qword ptr [r15 + 0x38]
0022EB61  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0022EB65  E8 86 3A 15 00                  call 0x1403825f0
0022EB6A  49 FF 47 58                     inc qword ptr [r15 + 0x58]
0022EB6E  E9 4F FC FF FF                  jmp 0x14022e7c2
0022EB73  8B C7                           mov eax, edi
0022EB75  83 E0 F8                        and eax, 0xfffffff8
0022EB78  83 F8 10                        cmp eax, 0x10
0022EB7B  0F 85 B7 01 00 00               jne 0x14022ed38
0022EB81  49 8B 4F 68                     mov rcx, qword ptr [r15 + 0x68]
0022EB85  0F 57 C0                        xorps xmm0, xmm0
0022EB88  0F 11 45 FF                     movups xmmword ptr [rbp - 1], xmm0
0022EB8C  48 85 C9                        test rcx, rcx
0022EB8F  0F 85 F0 05 00 00               jne 0x14022f185
0022EB95  41 8A 57 1C                     mov dl, byte ptr [r15 + 0x1c]
0022EB99  48 8B CE                        mov rcx, rsi
0022EB9C  E8 CF 00 05 00                  call 0x14027ec70
0022EBA1  49 8B CE                        mov rcx, r14
0022EBA4  48 C1 E1 19                     shl rcx, 0x19
0022EBA8  49 8B C5                        mov rax, r13
0022EBAB  48 C1 E0 19                     shl rax, 0x19
0022EBAF  48 8D 55 FF                     lea rdx, [rbp - 1]
0022EBB3  48 2B C8                        sub rcx, rax
0022EBB6  48 C7 45 07 00 10 00 00         mov qword ptr [rbp + 7], 0x1000
0022EBBE  48 C1 F9 10                     sar rcx, 0x10
0022EBC2  41 B9 AD 00 00 00               mov r9d, 0xad
0022EBC8  48 89 4D FF                     mov qword ptr [rbp - 1], rcx
0022EBCC  4C 8B C6                        mov r8, rsi
0022EBCF  B9 01 00 00 00                  mov ecx, 1
0022EBD4  E8 87 D9 13 00                  call 0x14036c560
0022EBD9  48 8B CE                        mov rcx, rsi
0022EBDC  E8 BF 4C 0F 00                  call 0x1403238a0
0022EBE1  8B 7D 77                        mov edi, dword ptr [rbp + 0x77]
0022EBE4  41 88 47 1C                     mov byte ptr [r15 + 0x1c], al
0022EBE8  4C 8B 5D 8F                     mov r11, qword ptr [rbp - 0x71]
0022EBEC  41 B9 01 00 00 00               mov r9d, 1
0022EBF2  E9 CA F7 FF FF                  jmp 0x14022e3c1
0022EBF7  E8 94 40 01 00                  call 0x140242c90
0022EBFC  48 8B 55 A7                     mov rdx, qword ptr [rbp - 0x59]
0022EC00  45 33 C9                        xor r9d, r9d
0022EC03  49 89 47 68                     mov qword ptr [r15 + 0x68], rax
0022EC07  48 8B C8                        mov rcx, rax
0022EC0A  C7 44 24 20 20 00 00 00         mov dword ptr [rsp + 0x20], 0x20
0022EC12  44 8B 40 0C                     mov r8d, dword ptr [rax + 0xc]
0022EC16  E8 E5 62 06 00                  call 0x140294f00
0022EC1B  E9 72 FA FF FF                  jmp 0x14022e692
0022EC20  48 8B 0D 59 F0 BF 00            mov rcx, qword ptr [rip + 0xbff059]
0022EC27  4D 8B D0                        mov r10, r8
0022EC2A  49 8B C0                        mov rax, r8
0022EC2D  48 85 C9                        test rcx, rcx
0022EC30  74 0D                           je 0x14022ec3f
0022EC32  A8 10                           test al, 0x10
0022EC34  75 09                           jne 0x14022ec3f
0022EC36  4C 8B D1                        mov r10, rcx
0022EC39  49 F7 D2                        not r10
0022EC3C  4C 23 D0                        and r10, rax
0022EC3F  49 8B C8                        mov rcx, r8
0022EC42  49 C1 FA 10                     sar r10, 0x10
0022EC46  E8 D5 0A 00 00                  call 0x14022f720
0022EC4B  49 8D 8B 00 04 00 00            lea rcx, [r11 + 0x400]
0022EC52  49 8B D2                        mov rdx, r10
0022EC55  84 C0                           test al, al
0022EC57  0F 85 A0 FD FF FF               jne 0x14022e9fd
0022EC5D  45 8B 47 18                     mov r8d, dword ptr [r15 + 0x18]
0022EC61  48 8D 45 97                     lea rax, [rbp - 0x69]
0022EC65  4D 8D 4F 20                     lea r9, [r15 + 0x20]
0022EC69  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0022EC6E  E8 CD C3 FF FF                  call 0x14022b040
0022EC73  85 C0                           test eax, eax
0022EC75  0F 84 92 FD FF FF               je 0x14022ea0d
0022EC7B  48 8B 45 97                     mov rax, qword ptr [rbp - 0x69]
0022EC7F  48 85 C0                        test rax, rax
0022EC82  0F 85 D0 03 00 00               jne 0x14022f058
0022EC88  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
0022EC8C  E8 DF 9E 0F 00                  call 0x140328b70
0022EC91  85 C0                           test eax, eax
0022EC93  75 35                           jne 0x14022ecca
0022EC95  48 8B 7D DF                     mov rdi, qword ptr [rbp - 0x21]
0022EC99  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
0022EC9C  24 70                           and al, 0x70
0022EC9E  3C 20                           cmp al, 0x20
0022ECA0  75 28                           jne 0x14022ecca
0022ECA2  48 8B CF                        mov rcx, rdi
0022ECA5  E8 76 0A 10 00                  call 0x14032f720
0022ECAA  85 C0                           test eax, eax
0022ECAC  75 1C                           jne 0x14022ecca
0022ECAE  48 8B 55 8F                     mov rdx, qword ptr [rbp - 0x71]
0022ECB2  4C 8B CF                        mov r9, rdi
0022ECB5  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
0022ECB9  4D 8B C6                        mov r8, r14
0022ECBC  E8 2B 0B 00 00                  call 0x14022f7ec
0022ECC1  48 85 C0                        test rax, rax
0022ECC4  0F 85 0C 06 00 00               jne 0x14022f2d6
0022ECCA  49 8B 7F 50                     mov rdi, qword ptr [r15 + 0x50]
0022ECCE  33 DB                           xor ebx, ebx
0022ECD0  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
0022ECD7  0F 83 B1 FC FF FF               jae 0x14022e98e
0022ECDD  FF C3                           inc ebx
0022ECDF  85 1D C7 65 D9 00               test dword ptr [rip + 0xd965c7], ebx
0022ECE5  0F 84 23 04 00 00               je 0x14022f10e
0022ECEB  F3 90                           pause
0022ECED  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0022ECF1  48 85 C0                        test rax, rax
0022ECF4  79 DA                           jns 0x14022ecd0
0022ECF6  EB E5                           jmp 0x14022ecdd
0022ECF8  41 FF C7                        inc r15d
0022ECFB  44 85 3D AA 65 D9 00            test dword ptr [rip + 0xd965aa], r15d
0022ED02  0F 84 69 03 00 00               je 0x14022f071
0022ED08  F3 90                           pause
0022ED0A  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
0022ED0E  48 85 C0                        test rax, rax
0022ED11  0F 89 4B FD FF FF               jns 0x14022ea62
0022ED17  EB DF                           jmp 0x14022ecf8
0022ED19  FF C3                           inc ebx
0022ED1B  85 1D 8B 65 D9 00               test dword ptr [rip + 0xd9658b], ebx
0022ED21  0F 84 72 03 00 00               je 0x14022f099
0022ED27  F3 90                           pause
0022ED29  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0022ED2D  48 85 C0                        test rax, rax
0022ED30  0F 89 39 FB FF FF               jns 0x14022e86f
0022ED36  EB E1                           jmp 0x14022ed19
0022ED38  49 8B C8                        mov rcx, r8
0022ED3B  E8 90 28 15 00                  call 0x1403815d0
0022ED40  85 C0                           test eax, eax
0022ED42  0F 85 39 FE FF FF               jne 0x14022eb81
0022ED48  48 8B 0D 39 13 C0 00            mov rcx, qword ptr [rip + 0xc01339]
0022ED4F  4C 8B 6D 9F                     mov r13, qword ptr [rbp - 0x61]
0022ED53  41 0F B7 85 AE 04 00 00         movzx eax, word ptr [r13 + 0x4ae]
0022ED5B  48 8B 34 C1                     mov rsi, qword ptr [rcx + rax*8]
0022ED5F  41 0F B7 83 AE 04 00 00         movzx eax, word ptr [r11 + 0x4ae]
0022ED67  48 39 34 C1                     cmp qword ptr [rcx + rax*8], rsi
0022ED6B  0F 85 0D 05 00 00               jne 0x14022f27e
0022ED71  49 8B 5C 24 10                  mov rbx, qword ptr [r12 + 0x10]
0022ED76  41 8B 47 18                     mov eax, dword ptr [r15 + 0x18]
0022ED7A  41 84 C1                        test r9b, al
0022ED7D  74 1A                           je 0x14022ed99
0022ED7F  48 B8 3F 00 00 00 00 00 00 F0   movabs rax, 0xf00000000000003f
0022ED89  41 83 CA 02                     or r10d, 2
0022ED8D  48 23 D8                        and rbx, rax
0022ED90  48 83 CB 20                     or rbx, 0x20
0022ED94  49 89 5C 24 10                  mov qword ptr [r12 + 0x10], rbx
0022ED99  45 85 D2                        test r10d, r10d
0022ED9C  74 19                           je 0x14022edb7
0022ED9E  41 8B D2                        mov edx, r10d
0022EDA1  48 8B CE                        mov rcx, rsi
0022EDA4  E8 B3 DD FF FF                  call 0x14022cb5c
0022EDA9  85 C0                           test eax, eax
0022EDAB  0F 84 5C FC FF FF               je 0x14022ea0d
0022EDB1  41 B9 01 00 00 00               mov r9d, 1
0022EDB7  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
0022EDBB  8A C2                           mov al, dl
0022EDBD  C0 E8 02                        shr al, 2
0022EDC0  41 84 C1                        test r9b, al
0022EDC3  74 46                           je 0x14022ee0b
0022EDC5  48 8B 05 B4 EE BF 00            mov rax, qword ptr [rip + 0xbfeeb4]
0022EDCC  48 8B CA                        mov rcx, rdx
0022EDCF  48 85 C0                        test rax, rax
0022EDD2  74 0E                           je 0x14022ede2
0022EDD4  F6 C1 10                        test cl, 0x10
0022EDD7  75 09                           jne 0x14022ede2
0022EDD9  48 8B D0                        mov rdx, rax
0022EDDC  48 F7 D2                        not rdx
0022EDDF  48 23 D1                        and rdx, rcx
0022EDE2  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
0022EDE7  4D 8B CE                        mov r9, r14
0022EDEA  48 C1 E9 0C                     shr rcx, 0xc
0022EDEE  4D 8B C4                        mov r8, r12
0022EDF1  83 E1 0F                        and ecx, 0xf
0022EDF4  48 C1 EA 20                     shr rdx, 0x20
0022EDF8  48 8B 8C CE 60 48 00 00         mov rcx, qword ptr [rsi + rcx*8 + 0x4860]
0022EE00  E8 B7 08 00 00                  call 0x14022f6bc
0022EE05  41 B9 01 00 00 00               mov r9d, 1
0022EE0B  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
0022EE0F  84 C0                           test al, al
0022EE11  79 08                           jns 0x14022ee1b
0022EE13  48 83 C8 20                     or rax, 0x20
0022EE17  48 89 45 7F                     mov qword ptr [rbp + 0x7f], rax
0022EE1B  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
0022EE1F  8A D0                           mov dl, al
0022EE21  D0 EA                           shr dl, 1
0022EE23  41 84 D1                        test r9b, dl
0022EE26  0F 85 62 04 00 00               jne 0x14022f28e
0022EE2C  49 8B CC                        mov rcx, r12
0022EE2F  49 89 04 24                     mov qword ptr [r12], rax
0022EE33  E8 A8 5F 06 00                  call 0x140294de0
0022EE38  48 89 45 7F                     mov qword ptr [rbp + 0x7f], rax
0022EE3C  49 89 06                        mov qword ptr [r14], rax
0022EE3F  41 8B 47 18                     mov eax, dword ptr [r15 + 0x18]
0022EE43  41 84 C1                        test r9b, al
0022EE46  74 0E                           je 0x14022ee56
0022EE48  4D 01 4F 20                     add qword ptr [r15 + 0x20], r9
0022EE4C  83 FF 18                        cmp edi, 0x18
0022EE4F  74 05                           je 0x14022ee56
0022EE51  48 83 4D 7F 08                  or qword ptr [rbp + 0x7f], 8
0022EE56  48 83 E3 E0                     and rbx, 0xffffffffffffffe0
0022EE5A  8B C7                           mov eax, edi
0022EE5C  48 0B D8                        or rbx, rax
0022EE5F  49 89 5C 24 10                  mov qword ptr [r12 + 0x10], rbx
0022EE64  33 DB                           xor ebx, ebx
0022EE66  49 8B 7F 50                     mov rdi, qword ptr [r15 + 0x50]
0022EE6A  44 8D 6B 01                     lea r13d, [rbx + 1]
0022EE6E  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
0022EE75  0F 82 1A 01 00 00               jb 0x14022ef95
0022EE7B  48 8B 4D 87                     mov rcx, qword ptr [rbp - 0x79]
0022EE7F  41 8B D5                        mov edx, r13d
0022EE82  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
0022EE86  48 89 01                        mov qword ptr [rcx], rax
0022EE89  49 8B 4F 50                     mov rcx, qword ptr [r15 + 0x50]
0022EE8D  E8 FE 3E 15 00                  call 0x140382d90
0022EE92  4D 8B 5F 50                     mov r11, qword ptr [r15 + 0x50]
0022EE96  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0022EEA0  F0 49 21 43 18                  lock and qword ptr [r11 + 0x18], rax
0022EEA5  4C 8B 6D 9F                     mov r13, qword ptr [rbp - 0x61]
0022EEA9  F0 49 FF 8D 88 02 00 00         lock dec qword ptr [r13 + 0x288]
0022EEB1  E9 B8 F8 FF FF                  jmp 0x14022e76e
0022EEB6  FF C3                           inc ebx
0022EEB8  85 1D EE 63 D9 00               test dword ptr [rip + 0xd963ee], ebx
0022EEBE  0F 84 FC 01 00 00               je 0x14022f0c0
0022EEC4  F3 90                           pause
0022EEC6  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0022EECA  48 85 C0                        test rax, rax
0022EECD  0F 89 AE FA FF FF               jns 0x14022e981
0022EED3  EB E1                           jmp 0x14022eeb6
0022EED5  49 8D 47 20                     lea rax, [r15 + 0x20]
0022EED9  4D 8B CD                        mov r9, r13
0022EEDC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0022EEE1  49 8B CB                        mov rcx, r11
0022EEE4  49 8B 47 50                     mov rax, qword ptr [r15 + 0x50]
0022EEE8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0022EEED  E8 EA 9E 27 00                  call 0x1404a8ddc
0022EEF2  85 C0                           test eax, eax
0022EEF4  0F 85 79 F8 FF FF               jne 0x14022e773
0022EEFA  48 83 65 97 00                  and qword ptr [rbp - 0x69], 0
0022EEFF  E9 65 F9 FF FF                  jmp 0x14022e869
0022EF04  8B C8                           mov ecx, eax
0022EF06  E8 75 45 09 00                  call 0x1402c3480
0022EF0B  48 89 45 7F                     mov qword ptr [rbp + 0x7f], rax
0022EF0F  E9 D7 F9 FF FF                  jmp 0x14022e8eb
0022EF14  F6 C3 20                        test bl, 0x20
0022EF17  0F 85 9F F7 FF FF               jne 0x14022e6bc
0022EF1D  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0022EF27  48 8B C0                        mov rax, rax
0022EF2A  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
0022EF34  48 03 C1                        add rax, rcx
0022EF37  4C 3B E0                        cmp r12, rax
0022EF3A  0F 82 7C F7 FF FF               jb 0x14022e6bc
0022EF40  41 B8 80 00 00 00               mov r8d, 0x80
0022EF46  48 8B D3                        mov rdx, rbx
0022EF49  49 8B CC                        mov rcx, r12
0022EF4C  E8 2F 3E 06 00                  call 0x140292d80
0022EF51  E9 66 F7 FF FF                  jmp 0x14022e6bc
0022EF56  8B 57 30                        mov edx, dword ptr [rdi + 0x30]
0022EF59  48 8B CB                        mov rcx, rbx
0022EF5C  C1 EA 07                        shr edx, 7
0022EF5F  83 E2 1F                        and edx, 0x1f
0022EF62  E8 AD 05 00 00                  call 0x14022f514
0022EF67  4C 8B C0                        mov r8, rax
0022EF6A  48 85 C0                        test rax, rax
0022EF6D  0F 84 4F F8 FF FF               je 0x14022e7c2
0022EF73  49 8D 47 20                     lea rax, [r15 + 0x20]
0022EF77  4D 8B CD                        mov r9, r13
0022EF7A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0022EF7F  49 8B CB                        mov rcx, r11
0022EF82  49 8B 47 50                     mov rax, qword ptr [r15 + 0x50]
0022EF86  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0022EF8B  E8 4C 9E 27 00                  call 0x1404a8ddc
0022EF90  E9 2D F8 FF FF                  jmp 0x14022e7c2
0022EF95  41 03 DD                        add ebx, r13d
0022EF98  85 1D 0E 63 D9 00               test dword ptr [rip + 0xd9630e], ebx
0022EF9E  0F 84 43 01 00 00               je 0x14022f0e7
0022EFA4  F3 90                           pause
0022EFA6  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
0022EFAA  48 85 C0                        test rax, rax
0022EFAD  0F 89 BB FE FF FF               jns 0x14022ee6e
0022EFB3  EB E0                           jmp 0x14022ef95
0022EFB5  48 83 4D 7F 08                  or qword ptr [rbp + 0x7f], 8
0022EFBA  E9 BC F9 FF FF                  jmp 0x14022e97b
0022EFBF  8B 05 F3 7A D9 00               mov eax, dword ptr [rip + 0xd97af3]
0022EFC5  A8 40                           test al, 0x40
0022EFC7  0F 84 00 FA FF FF               je 0x14022e9cd
0022EFCD  E8 BE 04 0E 00                  call 0x14030f490
0022EFD2  84 C0                           test al, al
0022EFD4  0F 84 BF 01 00 00               je 0x14022f199
0022EFDA  8B CB                           mov ecx, ebx
0022EFDC  E8 7F 04 0E 00                  call 0x14030f460
0022EFE1  48 8B 55 B7                     mov rdx, qword ptr [rbp - 0x49]
0022EFE5  E9 E5 F9 FF FF                  jmp 0x14022e9cf
0022EFEA  8B 05 C8 7A D9 00               mov eax, dword ptr [rip + 0xd97ac8]
0022EFF0  A8 40                           test al, 0x40
0022EFF2  0F 84 F4 F9 FF FF               je 0x14022e9ec
0022EFF8  E8 93 04 0E 00                  call 0x14030f490
0022EFFD  84 C0                           test al, al
0022EFFF  0F 84 E7 F9 FF FF               je 0x14022e9ec
0022F005  8B CB                           mov ecx, ebx
0022F007  E8 54 04 0E 00                  call 0x14030f460
0022F00C  E9 DD F9 FF FF                  jmp 0x14022e9ee
0022F011  4C 8B 6D 87                     mov r13, qword ptr [rbp - 0x79]
0022F015  E9 4F F8 FF FF                  jmp 0x14022e869
0022F01A  8B 05 98 7A D9 00               mov eax, dword ptr [rip + 0xd97a98]
0022F020  A8 40                           test al, 0x40
0022F022  0F 84 26 FA FF FF               je 0x14022ea4e
0022F028  E8 63 04 0E 00                  call 0x14030f490
0022F02D  84 C0                           test al, al
0022F02F  0F 84 19 FA FF FF               je 0x14022ea4e
0022F035  8B CF                           mov ecx, edi
0022F037  E8 24 04 0E 00                  call 0x14030f460
0022F03C  E9 0F FA FF FF                  jmp 0x14022ea50
0022F041  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
0022F045  41 B8 01 00 00 00               mov r8d, 1
0022F04B  48 8B D7                        mov rdx, rdi
0022F04E  E8 7D 4F 05 00                  call 0x140283fd0
0022F053  E9 0D F6 FF FF                  jmp 0x14022e665
0022F058  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
0022F05C  83 E0 1F                        and eax, 0x1f
0022F05F  3C 18                           cmp al, 0x18
0022F061  0F 84 63 FC FF FF               je 0x14022ecca
0022F067  48 83 4D 7F 08                  or qword ptr [rbp + 0x7f], 8
0022F06C  E9 59 FC FF FF                  jmp 0x14022ecca
0022F071  8B 05 41 7A D9 00               mov eax, dword ptr [rip + 0xd97a41]
0022F077  A8 40                           test al, 0x40
0022F079  0F 84 89 FC FF FF               je 0x14022ed08
0022F07F  E8 0C 04 0E 00                  call 0x14030f490
0022F084  84 C0                           test al, al
0022F086  0F 84 7C FC FF FF               je 0x14022ed08
0022F08C  41 8B CF                        mov ecx, r15d
0022F08F  E8 CC 03 0E 00                  call 0x14030f460
0022F094  E9 71 FC FF FF                  jmp 0x14022ed0a
0022F099  8B 05 19 7A D9 00               mov eax, dword ptr [rip + 0xd97a19]
0022F09F  A8 40                           test al, 0x40
0022F0A1  0F 84 80 FC FF FF               je 0x14022ed27
0022F0A7  E8 E4 03 0E 00                  call 0x14030f490
0022F0AC  84 C0                           test al, al
0022F0AE  0F 84 73 FC FF FF               je 0x14022ed27
0022F0B4  8B CB                           mov ecx, ebx
0022F0B6  E8 A5 03 0E 00                  call 0x14030f460
0022F0BB  E9 69 FC FF FF                  jmp 0x14022ed29
0022F0C0  8B 05 F2 79 D9 00               mov eax, dword ptr [rip + 0xd979f2]
0022F0C6  A8 40                           test al, 0x40
0022F0C8  0F 84 F6 FD FF FF               je 0x14022eec4
0022F0CE  E8 BD 03 0E 00                  call 0x14030f490
0022F0D3  84 C0                           test al, al
0022F0D5  0F 84 E9 FD FF FF               je 0x14022eec4
0022F0DB  8B CB                           mov ecx, ebx
0022F0DD  E8 7E 03 0E 00                  call 0x14030f460
0022F0E2  E9 DF FD FF FF                  jmp 0x14022eec6
0022F0E7  8B 05 CB 79 D9 00               mov eax, dword ptr [rip + 0xd979cb]
0022F0ED  A8 40                           test al, 0x40
0022F0EF  0F 84 AF FE FF FF               je 0x14022efa4
0022F0F5  E8 96 03 0E 00                  call 0x14030f490
0022F0FA  84 C0                           test al, al
0022F0FC  0F 84 A2 FE FF FF               je 0x14022efa4
0022F102  8B CB                           mov ecx, ebx
0022F104  E8 57 03 0E 00                  call 0x14030f460
0022F109  E9 98 FE FF FF                  jmp 0x14022efa6
0022F10E  8B 05 A4 79 D9 00               mov eax, dword ptr [rip + 0xd979a4]
0022F114  A8 40                           test al, 0x40
0022F116  0F 84 CF FB FF FF               je 0x14022eceb
0022F11C  E8 6F 03 0E 00                  call 0x14030f490
0022F121  84 C0                           test al, al
0022F123  0F 84 C2 FB FF FF               je 0x14022eceb
0022F129  8B CB                           mov ecx, ebx
0022F12B  E8 30 03 0E 00                  call 0x14030f460
0022F130  E9 B8 FB FF FF                  jmp 0x14022eced
0022F135  45 8A 47 1C                     mov r8b, byte ptr [r15 + 0x1c]
0022F139  33 D2                           xor edx, edx
0022F13B  49 8B CE                        mov rcx, r14
0022F13E  E8 2D 0E 05 00                  call 0x14027ff70
0022F143  4D 8B 06                        mov r8, qword ptr [r14]
0022F146  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
0022F150  4C 8B 5D 8F                     mov r11, qword ptr [rbp - 0x71]
0022F154  41 B9 01 00 00 00               mov r9d, 1
0022F15A  4C 89 45 7F                     mov qword ptr [rbp + 0x7f], r8
0022F15E  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
0022F168  E9 8F F2 FF FF                  jmp 0x14022e3fc
0022F16D  41 BA 05 00 00 00               mov r10d, 5
0022F173  49 C7 44 24 08 01 00 00 00      mov qword ptr [r12 + 8], 1
0022F17C  44 89 55 6F                     mov dword ptr [rbp + 0x6f], r10d
0022F180  E9 8D F3 FF FF                  jmp 0x14022e512
0022F185  E8 36 2E 0E 00                  call 0x140311fc0
0022F18A  E8 E1 4A 0E 00                  call 0x140313c70
0022F18F  49 83 67 68 00                  and qword ptr [r15 + 0x68], 0
0022F194  E9 FC F9 FF FF                  jmp 0x14022eb95
0022F199  48 8B 55 B7                     mov rdx, qword ptr [rbp - 0x49]
0022F19D  E9 2B F8 FF FF                  jmp 0x14022e9cd
0022F1A2  49 8B 45 28                     mov rax, qword ptr [r13 + 0x28]
0022F1A6  48 85 C0                        test rax, rax
0022F1A9  0F 88 37 F4 FF FF               js 0x14022e5e6
0022F1AF  48 8B 55 D7                     mov rdx, qword ptr [rbp - 0x29]
0022F1B3  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
0022F1B7  E8 68 60 23 00                  call 0x140465224
0022F1BC  E9 25 F4 FF FF                  jmp 0x14022e5e6
0022F1C1  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
0022F1C5  49 8B C0                        mov rax, r8
0022F1C8  48 C1 E8 0C                     shr rax, 0xc
0022F1CC  83 E0 0F                        and eax, 0xf
0022F1CF  48 F7 DF                        neg rdi
0022F1D2  45 1B C9                        sbb r9d, r9d
0022F1D5  48 8B 94 C1 60 48 00 00         mov rdx, qword ptr [rcx + rax*8 + 0x4860]
0022F1DD  41 F7 D9                        neg r9d
0022F1E0  48 8B 05 99 EA BF 00            mov rax, qword ptr [rip + 0xbfea99]
0022F1E7  41 83 C1 02                     add r9d, 2
0022F1EB  48 85 C0                        test rax, rax
0022F1EE  0F 84 12 80 4A 00               je 0x1406d7206
0022F1F4  41 F6 C0 10                     test r8b, 0x10
0022F1F8  0F 85 08 80 4A 00               jne 0x1406d7206
0022F1FE  48 F7 D0                        not rax
0022F201  4C 23 C0                        and r8, rax
0022F204  E9 FD 7F 4A 00                  jmp 0x1406d7206
0022F209  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
0022F20D  48 85 C0                        test rax, rax
0022F210  0F 84 D5 F6 FF FF               je 0x14022e8eb
0022F216  48 0F BA 6D 7F 0B               bts qword ptr [rbp + 0x7f], 0xb
0022F21C  E9 CA F6 FF FF                  jmp 0x14022e8eb
0022F221  49 8B 45 08                     mov rax, qword ptr [r13 + 8]
0022F225  48 85 C0                        test rax, rax
0022F228  0F 84 D5 F6 FF FF               je 0x14022e903
0022F22E  48 8B 4D 8F                     mov rcx, qword ptr [rbp - 0x71]
0022F232  41 B8 01 00 00 00               mov r8d, 1
0022F238  48 81 C1 00 04 00 00            add rcx, 0x400
0022F23F  49 8B D3                        mov rdx, r11
0022F242  E8 01 C0 FF FF                  call 0x14022b248
0022F247  85 C0                           test eax, eax
0022F249  0F 85 2C F7 FF FF               jne 0x14022e97b
0022F24F  E9 B9 F7 FF FF                  jmp 0x14022ea0d
0022F254  48 89 45 7F                     mov qword ptr [rbp + 0x7f], rax
0022F258  E9 1E F7 FF FF                  jmp 0x14022e97b
0022F25D  49 8B 4F 68                     mov rcx, qword ptr [r15 + 0x68]
0022F261  48 85 C9                        test rcx, rcx
0022F264  0F 84 BD 7F 4A 00               je 0x1406d7227
0022F26A  E8 51 2D 0E 00                  call 0x140311fc0
0022F26F  E8 FC 49 0E 00                  call 0x140313c70
0022F274  49 83 67 68 00                  and qword ptr [r15 + 0x68], 0
0022F279  E9 A9 7F 4A 00                  jmp 0x1406d7227
0022F27E  41 BA 05 00 00 00               mov r10d, 5
0022F284  4D 89 4C 24 08                  mov qword ptr [r12 + 8], r9
0022F289  E9 E3 FA FF FF                  jmp 0x14022ed71
0022F28E  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
0022F292  45 8B C1                        mov r8d, r9d
0022F295  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
0022F299  48 8B CE                        mov rcx, rsi
0022F29C  48 83 E0 FB                     and rax, 0xfffffffffffffffb
0022F2A0  48 8B D0                        mov rdx, rax
0022F2A3  48 89 45 C7                     mov qword ptr [rbp - 0x39], rax
0022F2A7  E8 24 4D 05 00                  call 0x140283fd0
0022F2AC  48 8D 4D 7F                     lea rcx, [rbp + 0x7f]
0022F2B0  E8 D7 C3 0F 00                  call 0x14032b68c
0022F2B5  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
0022F2B9  41 B9 01 00 00 00               mov r9d, 1
0022F2BF  E9 68 FB FF FF                  jmp 0x14022ee2c
0022F2C4  48 8D 4D 7F                     lea rcx, [rbp + 0x7f]
0022F2C8  E8 BF C3 0F 00                  call 0x14032b68c
0022F2CD  4C 8B 45 7F                     mov r8, qword ptr [rbp + 0x7f]
0022F2D1  E9 44 F5 FF FF                  jmp 0x14022e81a
0022F2D6  48 89 45 7F                     mov qword ptr [rbp + 0x7f], rax
0022F2DA  E9 EB F9 FF FF                  jmp 0x14022ecca
0022F2DF  48 8D 0C 40                     lea rcx, [rax + rax*2]
0022F2E3  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0022F2ED  48 C1 E1 04                     shl rcx, 4
0022F2F1  48 8B C0                        mov rax, rax
0022F2F4  48 03 C8                        add rcx, rax
0022F2F7  E8 AC 1C 24 00                  call 0x140470fa8
0022F2FC  E9 98 F4 FF FF                  jmp 0x14022e799
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiBuildForkPte(__int64 a1)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (200);
    v_stack_mA0 = *(unsigned __int64 *)(a1 + 56);
    v_stack_m80 = *(unsigned __int64 *)(a1 + 40);
    v_stack_m68 = *(unsigned __int64 *)(a1 + 16);
    v_stack_mD0 = *(unsigned __int64 *)(a1 + 8);
    v_stack_mD8 = *(unsigned __int64 *)(a1 + 64);
    v_stack_p20 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56));
    v_stack_m78 = v_xmm0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56)) == 0) goto loc_0022E7B0;
    v_rbx = 0;
    v_rdi = 0;
    v_stack_mC0 = *(unsigned __int64 *)(a1);
    v_stack_mB8 = *(unsigned __int64 *)(a1) + 1024;
loc_0022E3B7:
loc_0022E3C1:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 16) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 24) = 2;
    if (0 != 0) goto loc_0022F135;
loc_0022E3FC:
    v_r10 = 0;
    v_stack_p18 = (unsigned int)(v_rbx + 1);
    v_stack_p10 = 0;
    if ((((unsigned __int8)(v_rbx + 1)) & ((unsigned __int8)(v_stack_p20))) == 0) goto loc_0022E7DC;
    a3 = (v_stack_p20) >> (12);
    a3 = (a3) & (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56)));
    v_r13 = (a3 + a3 * 2) << (4);
    v_r13 = (v_r13) + (a1);
    if (0 != 0) goto loc_0022EA88;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_r13 + 32)))) > ((unsigned __int16)(v_rbx + 1))) goto loc_0022EA78;
loc_0022E442:
    result = MI_IS_SOFTWARE_PTE_SHADOW_STACK(*(unsigned __int64 *)(v_r13 + 16), *(unsigned __int64 *)(a1 + 48), a3, v_rbx + 1);
    if ((unsigned int)(result) != 0) goto loc_0022EA84;
    v_rdi = (v_stack_mA0) << (25);
    result = (result) << (25);
    v_rdi = (v_rdi) - (result);
    v_rdi = (v_rdi) >> (16);
    v_stack_m88 = v_rdi;
    result = MiGetWsleContents(*(unsigned __int64 *)(v_r13 + 16), v_rdi, a3, v_rbx + 1);
    if (sign_flag) goto loc_0022E8A5;
    v_r14 = (*(unsigned __int64 *)(a1 + 72)) >> (9);
    v_r14 = (v_r14) & (result);
    v_r14 = (*(unsigned __int64 *)(v_r14 + result * 1)) >> (12);
    v_r14 = (v_r14) & (result);
    a3 = (v_r14 + v_r14 * 2) << (4);
    a3 = (a3) + (result);
    result = (*(unsigned __int64 *)(v_r13 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_stack_mA8 = a3;
    v_stack_m90 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12589981) + result * 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12589981) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 1198) * 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12589981) + result * 8))) goto loc_0022F16D;
loc_0022E512:
    v_rsi = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 16);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 24)))) & (1)) != 0) {
        v_r10 = (unsigned int)((v_r10) | (2));
        v_rsi = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 16)) & ((unsigned int)(*(unsigned int *)(a1 + 24)));
        v_stack_p10 = (unsigned int)(v_r10);
        v_rsi = (v_rsi) | (32);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 16) = v_rsi;
    }
    if ((unsigned int)(v_r10) != 0) goto loc_0022E889;
loc_0022E546:
    v_rbx = (unsigned __int8)(((unsigned __int8)(result)) & (15));
    if (((unsigned __int8)(v_rbx)) != 8) goto loc_0022E584;
    result = MiLockPageTablePage(a3, 3, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12589981) + result * 8));
    if ((unsigned int)(result) != 0) goto loc_0022E584;
    result = MiReturnCloneCharges(v_stack_m90, (unsigned int)(v_stack_p10), a3, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12589981) + result * 8));
    goto loc_0022E3B7;
loc_0022E584:
    v_rbx = 0;
loc_0022E58A:
    if (condition_is_below) goto loc_0022E9BF;
    result = (*(unsigned __int64 *)(v_stack_mA8 + 24)) ^ (*(unsigned __int64 *)(v_stack_mA8 + 24) + 1);
    result = (result) & (a3);
    result = (result) ^ (*(unsigned __int64 *)(v_stack_mA8 + 24) + 1);
    *(unsigned __int64 *)(v_stack_mA8 + 24) = result;
    if (((v_stack_p20) & (66)) == 0) goto loc_0022EA5F;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m80 + 48))) & ((unsigned int)((unsigned int)(0x600000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x600000ULL)))) goto loc_0022F1A2;
loc_0022E5E6:
    v_rdi = 0;
loc_0022E5E8:
    if (condition_is_below) goto loc_0022EA40;
    result = MiCaptureDirtyBitToPfn(v_r13, v_stack_mA8, v_stack_m80, 1);
loc_0022E605:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_r13 + 16))) >> (1));
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_0022F1C1;
    *(unsigned __int64 *)(v_r13 + 8) = *(unsigned __int64 *)(a1 + 72);
    result = (*(unsigned __int64 *)(v_r13 + 40)) | (v_r13);
    *(unsigned __int64 *)(v_r13 + 40) = result;
    result = MiSetPfnContainingFrame(v_r13, v_r14, *(unsigned __int64 *)(v_r13 + 16), 1);
    result = MI_MAKE_PROTECT_WRITE_COPY(v_r13 + 16, v_r14, *(unsigned __int64 *)(v_r13 + 16), 1);
    v_r14 = (*(unsigned __int64 *)(v_r13 + 16)) >> (5);
    result = MiTransferPageFileOwnership(v_r13, v_stack_mA0, *(unsigned __int64 *)(v_r13 + 16), 1);
    if (result != 0) goto loc_0022F041;
loc_0022E665:
    if (!(condition_is_above_or_equal)) {
        v_stack_p20 = v_stack_p20;
    }
    result = MiWriteValidPteNewProtection(v_stack_mA0, v_stack_p20, *(unsigned __int64 *)(v_r13 + 16), 1);
    if ((*(unsigned __int64 *)(a1 + 104)) == 0) goto loc_0022EBF7;
loc_0022E692:
    a4 = 0;
    result = MiInsertTbFlushEntry(*(unsigned __int64 *)(a1 + 104), v_stack_m88, a4 + 1, a4);
    if (condition_is_below) goto loc_0022EF14;
loc_0022E6BC:
    a3 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) = v_stack_p20;
    result = MiSetWsleProtection(*(unsigned __int64 *)(a1 + 104), v_stack_m88, a3, a4);
    a1 = (*(unsigned __int64 *)(v_r13 + 8)) | (result);
    result = MiMakePrototypePteDirect(a1, v_stack_m88, a3, a4);
    v_stack_p20 = result;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 24)))) & (1)) != 0) {
        result = (result) | (8);
        v_stack_p20 = result;
    }
    a1 = ((unsigned int)((unsigned int)(v_r14))) ^ (v_stack_mB8);
    a1 = (a1) & (-32);
    a1 = (a1) ^ ((unsigned int)((unsigned int)(v_r14)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 16) = a1;
    v_rbx = 0;
loc_0022E715:
    if (condition_is_below) goto loc_0022E9DE;
    *(unsigned __int64 *)(v_stack_mD8) = v_stack_p20;
    result = MiIncreaseUsedPtesInPfn(*(unsigned __int64 *)(a1 + 80), 1, a3, a4);
    a4 = 0;
    a3 = (a3) | (-1);
    result = MiUpdateWorkingSetPrivateSize(v_stack_mB8, v_stack_m88, a3, a4);
loc_0022E76E:
loc_0022E773:
    *(unsigned __int64 *)(a1 + 56) = v_xmm1;
loc_0022E78B:
    if (v_stack_mB0 != -1) goto loc_0022F2DF;
loc_0022E799:
    result = 0;
    v_rsp = (v_rsp) + (200);
    return result;
loc_0022E7B0:
    if (0 == 0) goto loc_0022E7C2;
    if (((*(unsigned int *)(v_stack_m88 + 48)) & (0x2000000ULL)) != 0) goto loc_0022EF56;
loc_0022E7C2:
    *(unsigned __int64 *)(a1 + 56) = v_xmm1;
    goto loc_0022E799;
loc_0022E7DC:
    if (condition_is_below) goto loc_0022EC20;
    if (condition_is_below) goto loc_0022EA27;
    v_rdi = (a3) >> (5);
    v_rdi = (unsigned int)((v_rdi) & (31));
    result = IS_PTE_NOT_DEMAND_ZERO(a3, v_stack_m88, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_0022EB73;
    result = (unsigned __int8)(((unsigned __int8)(a3)) >> (1));
    if (((0) & ((unsigned __int8)(result))) != 0) goto loc_0022F2C4;
loc_0022E81A:
    a2 = 0;
    result = MiUpdatePageFileHighInPte(a3, a2, a3, a4);
    result = (result) & (0xFFFFFFFFFFFF0FFFULL);
    v_stack_p20 = result;
    result = MI_IS_SOFTWARE_PTE_SHADOW_STACK(result, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_0022F011;
    if (v_stack_m68 == 0) goto loc_0022F011;
    result = MiFindZeroCloneBlock(v_stack_m68, (unsigned int)((unsigned int)(v_rdi)), a3, a4);
    v_stack_mC8 = result;
    if (result != 0) goto loc_0022EED5;
loc_0022E869:
    v_rbx = 0;
loc_0022E86F:
    if (condition_is_below) goto loc_0022ED19;
    *(unsigned __int64 *)(v_stack_mD8) = v_stack_p20;
    goto loc_0022E999;
loc_0022E889:
    result = MiGetCloneCharges(0, (unsigned int)((unsigned int)(v_r10)), result, a4);
    if ((unsigned int)(result) == 0) goto loc_0022EA0D;
    goto loc_0022E546;
loc_0022E8A5:
    v_r11 = (*(unsigned __int64 *)(v_stack_mD8 + 8)) | (result);
    result = MiGetWsleProtection(*(unsigned __int64 *)(a1 + 80), 0, v_stack_mA8, a4);
    if ((unsigned int)(result) != 0) goto loc_0022EF04;
    result = MiMakePrototypePteDirect(v_r11, 0, v_stack_mA8, a4);
    v_stack_p20 = result;
    if (condition_is_below) goto loc_0022E8EB;
    if (!sign_flag) goto loc_0022F209;
loc_0022E8EB:
    if (condition_is_below) goto loc_0022E903;
    if (!sign_flag) goto loc_0022F221;
loc_0022E903:
    v_stack_p20 = v_stack_mC8;
    result = MiReferenceExistingCloneProto(v_stack_mD0 + 1024, v_r11, (unsigned int)(*(unsigned int *)(a1 + 24)), a1 + 32);
    if ((unsigned int)(result) == 0) goto loc_0022EA0D;
    if (v_stack_mC8 != 0) goto loc_0022EFB5;
    result = MiIsPrototypePteVadLookup(*(unsigned __int64 *)(v_stack_mD8 + 16), v_r11, (unsigned int)(*(unsigned int *)(a1 + 24)), a1 + 32);
    if ((unsigned int)(result) != 0) goto loc_0022E97B;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_m80 + 48))) & (112));
    if (((unsigned __int8)(result)) != 32) goto loc_0022E97B;
    result = MiIsVadLargePrivate(v_stack_m80, v_r11, (unsigned int)(*(unsigned int *)(a1 + 24)), a1 + 32);
    if ((unsigned int)(result) != 0) goto loc_0022E97B;
    result = MiMakePerSessionProtoPte(v_stack_mC0, v_stack_mD0, v_r14, v_stack_m80);
    if (result != 0) goto loc_0022F254;
loc_0022E97B:
    v_rbx = 0;
loc_0022E981:
    if (condition_is_below) goto loc_0022EEB6;
loc_0022E98E:
    *(unsigned __int64 *)(v_stack_mD8) = v_stack_p20;
loc_0022E999:
    result = MiIncreaseUsedPtesInPfn(*(unsigned __int64 *)(a1 + 80), 1, v_r14, v_stack_m80);
    goto loc_0022E773;
loc_0022E9BF:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 14248165)) & ((unsigned int)(v_rbx))) == 0) goto loc_0022EFBF;
loc_0022E9CD:
loc_0022E9CF:
    if (!sign_flag) goto loc_0022E58A;
    goto loc_0022E9BF;
loc_0022E9DE:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 14248134)) & ((unsigned int)(v_rbx))) == 0) goto loc_0022EFEA;
loc_0022E9EC:
loc_0022E9EE:
    if (!sign_flag) goto loc_0022E715;
    goto loc_0022E9DE;
loc_0022E9FD:
    result = MiIncrementCombinedPte(*(unsigned __int64 *)(a1 + 80), 1, (unsigned int)((unsigned int)(v_stack_m80)), v_stack_m80);
    if ((unsigned int)(result) != 0) goto loc_0022ECCA;
loc_0022EA0D:
    result = MiWriteUselessChildPte(v_stack_mD8, *(unsigned __int64 *)(a1 + 80), (unsigned int)((unsigned int)(v_stack_m80)), v_stack_m80);
    *(unsigned int *)(a1 + 96) = 1;
    goto loc_0022E773;
loc_0022EA27:
    result = MiHandleForkTransitionPte(a1, v_stack_mB0, (unsigned int)((unsigned int)(v_stack_m80)), v_stack_m80);
    if ((unsigned int)(result) != 0) goto loc_0022E78B;
    goto loc_0022EBE8;
loc_0022EA40:
    v_rdi = (unsigned int)((*(unsigned __int64 *)(a1 + 80)) + 1);
    if (((*(unsigned int *)(v_rip + 14248036)) & ((unsigned int)(v_rdi))) == 0) goto loc_0022F01A;
loc_0022EA4E:
loc_0022EA50:
    if (!sign_flag) goto loc_0022E5E8;
    goto loc_0022EA40;
loc_0022EA5F:
    v_r15 = 0;
loc_0022EA62:
    if (condition_is_below) goto loc_0022ECF8;
    goto loc_0022E605;
loc_0022EA78:
    if (sign_flag) goto loc_0022E442;
loc_0022EA84:
loc_0022EA88:
    a3 = 0;
    result = MiInitializePageColorBase(v_stack_mB8, a3 + 3, a3, v_stack_m78);
    a2 = 0;
    a1 = (v_stack_m70) >> (16);
    a1 = (unsigned int)((a1) & (3));
    if (v_stack_mB0 != -1) goto loc_0022EB1D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mD8 + 32))) >> (16));
    a1 = (unsigned int)(((unsigned __int8)(result)) & (0xFFFFFFC0ULL));
    a1 = (unsigned int)((a1) << (12));
    a2 = (unsigned int)(((unsigned int)(v_stack_m70)) & (0xFFF3FF00ULL));
    a1 = (unsigned int)((a1) | (0));
    a2 = (unsigned int)((a2) | ((unsigned int)(a1)));
    result = MiGetPage(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12588476) + *(unsigned __int16 *)(v_stack_mD0 + 1198) * 8), a2, 1, v_stack_m78);
    v_stack_mB0 = result;
    if (result == -1) goto loc_0022F25D;
loc_0022EB1D:
    a1 = (result + result * 2) << (4);
    a1 = (a1) + (result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mD8 + 32))) >> (16));
    a2 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    result = MiFinalizePageAttribute(a1, a2, 16, v_stack_m78);
    v_stack_p20 = (unsigned __int8)(*(unsigned __int8 *)(v_stack_p8 + 28));
    result = MiDuplicateCloneLeaf(*(unsigned __int64 *)(v_stack_p8 + 56), *(unsigned __int64 *)(v_stack_p8 + 64), v_stack_mB0, *(unsigned __int64 *)(v_stack_p8 + 80));
    goto loc_0022E7C2;
loc_0022EB73:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (0xFFFFFFF8ULL));
    if (((unsigned int)(result)) != 16) goto loc_0022ED38;
loc_0022EB81:
    v_stack_m60 = v_xmm0;
    if (*(unsigned __int64 *)(v_stack_p8 + 104) != 0) goto loc_0022F185;
loc_0022EB95:
    result = MiUnlockWorkingSetExclusive(v_stack_mB8, *(unsigned __int8 *)(v_stack_p8 + 28), v_stack_mB0, *(unsigned __int64 *)(v_stack_p8 + 80));
    a1 = (v_r14) << (25);
    result = (v_stack_mD8) << (25);
    a1 = (a1) - (result);
    v_stack_m58 = 0x1000ULL;
    a1 = (a1) >> (16);
    v_stack_m60 = a1;
    result = MiPrefetchVirtualMemory(1, v_stack_m60, v_stack_mB8, 173);
    result = MiLockWorkingSetExclusive(v_stack_mB8, v_stack_m60, v_stack_mB8, 173);
    *(unsigned __int8 *)(v_stack_p8 + 28) = (unsigned __int8)(result);
loc_0022EBE8:
    goto loc_0022E3C1;
loc_0022EBF7:
    result = MiGetProcessorFlushList(v_stack_mB8, v_stack_m60, v_stack_mB8, 1);
    a4 = 0;
    *(unsigned __int64 *)(v_stack_p8 + 104) = result;
    v_stack_p20 = 32;
    result = MiInitializeTbFlushList(result, v_stack_mB8, (unsigned int)(*(unsigned int *)(result + 12)), a4);
    goto loc_0022E692;
loc_0022EC20:
    if (*(unsigned __int64 *)(v_rip + 12578905) == 0) goto loc_0022EC3F;
    v_r10 = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (16)) == 0) {
        v_r10 = *(unsigned __int64 *)(v_rip + 12578905);
        v_r10 = ~(v_r10);
        v_r10 = (v_r10) & ((unsigned int)(*(unsigned int *)(result + 12)));
    }
    v_r10 = (v_r10) >> (16);
    result = MI_PROTO_FORMAT_COMBINED((unsigned int)(*(unsigned int *)(result + 12)), v_stack_mB8, (unsigned int)(*(unsigned int *)(result + 12)), a4);
    if ((unsigned __int8)(result) != 0) goto loc_0022E9FD;
    v_stack_p20 = v_stack_mC8;
    result = MiReferenceExistingCloneProto(v_stack_mD0 + 1024, v_r10, (unsigned int)(*(unsigned int *)(v_stack_p8 + 24)), v_stack_p8 + 32);
    if ((unsigned int)(result) == 0) goto loc_0022EA0D;
    if (v_stack_mC8 != 0) goto loc_0022F058;
    result = MiIsPrototypePteVadLookup(v_stack_p20, v_r10, (unsigned int)(*(unsigned int *)(v_stack_p8 + 24)), v_stack_p8 + 32);
    if ((unsigned int)(result) != 0) goto loc_0022ECCA;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_m80 + 48))) & (112));
    if (((unsigned __int8)(result)) != 32) goto loc_0022ECCA;
    result = MiIsVadLargePrivate(v_stack_m80, v_r10, (unsigned int)(*(unsigned int *)(v_stack_p8 + 24)), v_stack_p8 + 32);
    if ((unsigned int)(result) != 0) goto loc_0022ECCA;
    result = MiMakePerSessionProtoPte(v_stack_mC0, v_stack_mD0, v_r14, v_stack_m80);
    if (result != 0) goto loc_0022F2D6;
loc_0022ECCA:
    v_rbx = 0;
loc_0022ECD0:
    if (condition_is_above_or_equal) goto loc_0022E98E;
loc_0022ECDD:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 14247367)) & ((unsigned int)(v_rbx))) == 0) goto loc_0022F10E;
loc_0022ECEB:
loc_0022ECED:
    if (!sign_flag) goto loc_0022ECD0;
    goto loc_0022ECDD;
loc_0022ECF8:
    v_r15 = (unsigned int)((v_stack_p8) + 1);
    if (((*(unsigned int *)(v_rip + 14247338)) & ((unsigned int)(v_r15))) == 0) goto loc_0022F071;
loc_0022ED08:
loc_0022ED0A:
    if (!sign_flag) goto loc_0022EA62;
    goto loc_0022ECF8;
loc_0022ED19:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 14247307)) & ((unsigned int)(v_rbx))) == 0) goto loc_0022F099;
loc_0022ED27:
loc_0022ED29:
    if (!sign_flag) goto loc_0022E86F;
    goto loc_0022ED19;
loc_0022ED38:
    result = MI_IS_SOFTWARE_PTE_SHADOW_STACK(v_r14, v_stack_mD0, v_r14, v_stack_m80);
    if ((unsigned int)(result) != 0) goto loc_0022EB81;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12587833) + *(unsigned __int16 *)(v_stack_mD0 + 1198) * 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12587833) + *(unsigned __int16 *)(v_stack_mC0 + 1198) * 8))) goto loc_0022F27E;
loc_0022ED71:
    v_rbx = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 16);
    if ((((unsigned __int8)(v_stack_m80)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r15 + 24))))) != 0) {
        v_r10 = (unsigned int)((v_r10) | (2));
        v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 16)) & ((unsigned int)(*(unsigned int *)(v_r15 + 24)));
        v_rbx = (v_rbx) | (32);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 16) = v_rbx;
    }
    if ((unsigned int)(v_r10) == 0) goto loc_0022EDB7;
    result = MiGetCloneCharges(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12587833) + *(unsigned __int16 *)(v_stack_mC0 + 1198) * 8), (unsigned int)((unsigned int)(v_r10)), v_r14, v_stack_m80);
    if ((unsigned int)(result) == 0) goto loc_0022EA0D;
loc_0022EDB7:
    result = (unsigned __int8)(((unsigned __int8)(v_stack_p20)) >> (2));
    if (((1) & ((unsigned __int8)(result))) == 0) goto loc_0022EE0B;
    if (*(unsigned __int64 *)(v_rip + 12578484) == 0) goto loc_0022EDE2;
    if ((((unsigned __int8)(v_stack_p20)) & (16)) == 0) {
        a2 = *(unsigned __int64 *)(v_rip + 12578484);
        a2 = ~(a2);
        a2 = (a2) & (v_stack_p20);
    }
    a1 = (v_stack_p20) >> (12);
    a1 = (unsigned int)((a1) & (15));
    a2 = (a2) >> (32);
    result = MiUpdatePageFileBlockOwner(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12587833) + *(unsigned __int16 *)(v_stack_mC0 + 1198) * 8) + a1 * 8 + 18528), a2, *(unsigned __int64 *)(a1 + 72), v_r14);
loc_0022EE0B:
    result = v_stack_p20;
    if (sign_flag) {
        result = (v_stack_p20) | (32);
        v_stack_p20 = result;
    }
    a2 = (unsigned __int8)(((unsigned __int8)(v_stack_p20)) >> (1));
    if (((1) & ((unsigned __int8)(a2))) != 0) goto loc_0022F28E;
loc_0022EE2C:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72)) = v_stack_p20;
    result = MiMakePrototypePteDirect(*(unsigned __int64 *)(a1 + 72), a2, *(unsigned __int64 *)(a1 + 72), 1);
    v_stack_p20 = result;
    *(unsigned __int64 *)(v_r14) = result;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_r15 + 24))))) == 0) goto loc_0022EE56;
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_p8 + 80))) != 24) {
    }
    v_rbx = (v_rbx) & (-32);
    v_rbx = (v_rbx) | ((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_p8 + 80))));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 16) = v_rbx;
    v_rbx = 0;
loc_0022EE6E:
    if (condition_is_below) goto loc_0022EF95;
    *(unsigned __int64 *)(v_stack_mD8) = v_stack_p20;
    result = MiIncreaseUsedPtesInPfn(*(unsigned __int64 *)(v_r15 + 80), (unsigned int)((unsigned int)(v_rbx + 1)), *(unsigned __int64 *)(a1 + 72), 1);
    goto loc_0022E76E;
loc_0022EEB6:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 14246894)) & ((unsigned int)(v_rbx))) == 0) goto loc_0022F0C0;
loc_0022EEC4:
loc_0022EEC6:
    if (!sign_flag) goto loc_0022E981;
    goto loc_0022EEB6;
loc_0022EED5:
    v_stack_p28 = v_r15 + 32;
    v_stack_p20 = *(unsigned __int64 *)(v_r15 + 80);
    result = MiWriteSharedDemandZeroPte(*(unsigned __int64 *)(v_r15 + 80), (unsigned int)((unsigned int)(v_rbx + 1)), *(unsigned __int64 *)(a1 + 72), v_stack_mC0);
    if ((unsigned int)(result) != 0) goto loc_0022E773;
    goto loc_0022E869;
loc_0022EF04:
    result = MiMakePrototypePteVadLookup((unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_rbx + 1)), *(unsigned __int64 *)(a1 + 72), v_stack_mC0);
    v_stack_p20 = result;
    goto loc_0022E8EB;
loc_0022EF14:
    if ((((unsigned __int8)(v_rbx)) & (32)) != 0) goto loc_0022E6BC;
    result = (result) + ((unsigned int)((unsigned int)(result)));
    if ((*(unsigned __int64 *)(a1 + 72)) < result) goto loc_0022E6BC;
    result = MiCheckLinearProtectedPteAccessedBit(*(unsigned __int64 *)(a1 + 72), v_rbx, 128, v_stack_mC0);
    goto loc_0022E6BC;
loc_0022EF56:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r15 + 80) + 48))) >> (7));
    a2 = (unsigned int)((a2) & (31));
    result = MiFindZeroCloneBlock(v_rbx, a2, 128, v_stack_mC0);
    if (result == 0) goto loc_0022E7C2;
    v_stack_p28 = v_r15 + 32;
    v_stack_p20 = *(unsigned __int64 *)(v_r15 + 80);
    result = MiWriteSharedDemandZeroPte(*(unsigned __int64 *)(v_r15 + 80), a2, result, v_stack_mC0);
    goto loc_0022E7C2;
loc_0022EF95:
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(v_stack_mC0)));
    if (((*(unsigned int *)(v_rip + 14246670)) & ((unsigned int)(v_rbx))) == 0) goto loc_0022F0E7;
loc_0022EFA4:
loc_0022EFA6:
    if (!sign_flag) goto loc_0022EE6E;
    goto loc_0022EF95;
loc_0022EFB5:
    goto loc_0022E97B;
loc_0022EFBF:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14252787)))) & (64)) == 0) goto loc_0022E9CD;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(v_r15 + 80), a2, result, v_stack_mC0);
    if ((unsigned __int8)(result) == 0) goto loc_0022F199;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), a2, result, v_stack_mC0);
    goto loc_0022E9CF;
loc_0022EFEA:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14252744)))) & (64)) == 0) goto loc_0022E9EC;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbx)), v_stack_mA8, result, v_stack_mC0);
    if ((unsigned __int8)(result) == 0) goto loc_0022E9EC;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), v_stack_mA8, result, v_stack_mC0);
    goto loc_0022E9EE;
loc_0022F011:
    goto loc_0022E869;
loc_0022F01A:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14252696)))) & (64)) == 0) goto loc_0022EA4E;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbx)), v_stack_mA8, result, v_stack_mC0);
    if ((unsigned __int8)(result) == 0) goto loc_0022EA4E;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_r15 + 80))), v_stack_mA8, result, v_stack_mC0);
    goto loc_0022EA50;
loc_0022F041:
    result = MiReleasePageFileInfo(v_stack_m90, *(unsigned __int64 *)(v_r15 + 80), 1, v_stack_mC0);
    goto loc_0022E665;
loc_0022F058:
    result = (unsigned int)((*(unsigned __int64 *)(result + 16)) & (31));
    if (((unsigned __int8)(result)) == 24) goto loc_0022ECCA;
    goto loc_0022ECCA;
loc_0022F071:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14252609)))) & (64)) == 0) goto loc_0022ED08;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_m90, *(unsigned __int64 *)(v_r15 + 80), 1, v_stack_mC0);
    if ((unsigned __int8)(result) == 0) goto loc_0022ED08;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r15)), *(unsigned __int64 *)(v_r15 + 80), 1, v_stack_mC0);
    goto loc_0022ED0A;
loc_0022F099:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14252569)))) & (64)) == 0) goto loc_0022ED27;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_r15)), *(unsigned __int64 *)(v_r15 + 80), 1, v_stack_mC0);
    if ((unsigned __int8)(result) == 0) goto loc_0022ED27;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), *(unsigned __int64 *)(v_r15 + 80), 1, v_stack_mC0);
    goto loc_0022ED29;
loc_0022F0C0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14252530)))) & (64)) == 0) goto loc_0022EEC4;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbx)), *(unsigned __int64 *)(v_r15 + 80), 1, v_stack_mC0);
    if ((unsigned __int8)(result) == 0) goto loc_0022EEC4;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), *(unsigned __int64 *)(v_r15 + 80), 1, v_stack_mC0);
    goto loc_0022EEC6;
loc_0022F0E7:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14252491)))) & (64)) == 0) goto loc_0022EFA4;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbx)), *(unsigned __int64 *)(v_r15 + 80), 1, v_stack_mC0);
    if ((unsigned __int8)(result) == 0) goto loc_0022EFA4;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), *(unsigned __int64 *)(v_r15 + 80), 1, v_stack_mC0);
    goto loc_0022EFA6;
loc_0022F10E:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14252452)))) & (64)) == 0) goto loc_0022ECEB;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbx)), *(unsigned __int64 *)(v_r15 + 80), 1, v_stack_mC0);
    if ((unsigned __int8)(result) == 0) goto loc_0022ECEB;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), *(unsigned __int64 *)(v_r15 + 80), 1, v_stack_mC0);
    goto loc_0022ECED;
loc_0022F135:
    a2 = 0;
    result = MiMakeSystemAddressValid(v_r14, a2, *(unsigned __int8 *)(v_r15 + 28), v_stack_mC0);
    v_stack_p20 = *(unsigned __int64 *)(v_r14);
    goto loc_0022E3FC;
loc_0022F16D:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 8) = 1;
    v_stack_p10 = 5;
    goto loc_0022E512;
loc_0022F185:
    result = MiFlushTbList(v_r14, a2, *(unsigned __int64 *)(v_r14), 1);
    result = MiReleaseProcessorFlushList(v_r14, a2, *(unsigned __int64 *)(v_r14), 1);
    goto loc_0022EB95;
loc_0022F199:
    goto loc_0022E9CD;
loc_0022F1A2:
    if (sign_flag) goto loc_0022E5E6;
    result = MiCaptureWriteWatchDirtyBit(v_stack_mC0, v_stack_m88, *(unsigned __int64 *)(v_r14), 1);
    goto loc_0022E5E6;
loc_0022F1C1:
    result = (*(unsigned __int64 *)(v_r14)) >> (12);
    result = (unsigned int)((result) & (15));
    v_rdi = -(*(unsigned __int64 *)(v_r15 + 80));
    a4 = (unsigned int)(-(1));
    a4 = (unsigned int)((a4) + (2));
    result = ~(*(unsigned __int64 *)(v_rip + 12577433));
    a3 = (*(unsigned __int64 *)(v_r14)) & (result);
loc_0022F209:
    if (*(unsigned __int64 *)(v_stack_mD8 + 8) == 0) goto loc_0022E8EB;
    goto loc_0022E8EB;
loc_0022F221:
    if (*(unsigned __int64 *)(v_stack_mD8 + 8) == 0) goto loc_0022E903;
    a1 = (v_stack_mD0) + (0x400ULL);
    result = MiIncrementCombinedPte(a1, v_stack_mD0, 1, a4);
    if ((unsigned int)(result) != 0) goto loc_0022E97B;
    goto loc_0022EA0D;
loc_0022F254:
    v_stack_p20 = result;
    goto loc_0022E97B;
loc_0022F25D:
    result = MiFlushTbList(*(unsigned __int64 *)(v_r15 + 104), v_stack_mD0, 1, a4);
    result = MiReleaseProcessorFlushList(*(unsigned __int64 *)(v_r15 + 104), v_stack_mD0, 1, a4);
loc_0022F27E:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 8) = a4;
    goto loc_0022ED71;
loc_0022F28E:
    v_stack_m98 = result;
    result = (v_stack_m98) & (-5);
    v_stack_m98 = result;
    result = MiReleasePageFileInfo(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12587833) + *(unsigned __int16 *)(v_stack_mC0 + 1198) * 8), result, (unsigned int)((unsigned int)(a4)), a4);
    result = MiClearPageFileReservation(v_stack_p20, result, (unsigned int)((unsigned int)(a4)), a4);
    goto loc_0022EE2C;
loc_0022F2C4:
    result = MiClearPageFileReservation(v_stack_p20, result, (unsigned int)((unsigned int)(a4)), 1);
    goto loc_0022E81A;
loc_0022F2D6:
    v_stack_p20 = result;
    goto loc_0022ECCA;
loc_0022F2DF:
    a1 = (result + result * 2) << (4);
    a1 = (a1) + (result);
    result = MiLockAndInsertPageInFreeList(a1, result, v_stack_p20, 1);
    goto loc_0022E799;
}
```

## 5. (Beta) C Style

```c
int64_t MiBuildForkPte(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (200);
    v_stack_mA0 = *(uint64_t *)(arg1 + 0x38);
    v_stack_m80 = *(uint64_t *)(arg1 + 0x28);
    v_stack_m68 = *(uint64_t *)(arg1 + 0x10);
    v_stack_mD0 = *(uint64_t *)(arg1 + 0x8);
    v_stack_mD8 = *(uint64_t *)(arg1 + 0x40);
    v_stack_p20 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x38));
    v_stack_m78 = v_xmm0;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x38)) == 0) goto loc_0022E7B0;
    local_rbx = 0;
    local_rdi = 0;
    v_stack_mC0 = *(uint64_t *)(arg1);
    v_stack_mB8 = *(uint64_t *)(arg1) + 1024;
loc_0022E3B7:
loc_0022E3C1:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x10) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x18) = 2;
    if (0 != 0) goto loc_0022F135;
loc_0022E3FC:
    local_r10 = 0;
    v_stack_p18 = (uint32_t)(local_rbx + 1);
    v_stack_p10 = 0;
    if ((((uint8_t)(local_rbx + 1)) & ((uint8_t)(v_stack_p20))) == 0) goto loc_0022E7DC;
    a3 = (v_stack_p20) >> (12);
    a3 = (a3) & (*(uint64_t *)(*(uint64_t *)(arg1 + 0x38)));
    local_r13 = (a3 + a3 * 2) << (4);
    local_r13 = (local_r13) + (Arg1);
    if (0 != 0) goto loc_0022EA88;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(local_r13 + 0x20)))) > ((uint16_t)(local_rbx + 1))) goto loc_0022EA78;
loc_0022E442:
    result = MI_IS_SOFTWARE_PTE_SHADOW_STACK(*(uint64_t *)(local_r13 + 0x10), *(uint64_t *)(arg1 + 0x30), a3, local_rbx + 1);
    if ((uint32_t)(result) != 0) goto loc_0022EA84;
    local_rdi = (v_stack_mA0) << (25);
    result = (result) << (25);
    local_rdi = (local_rdi) - (result);
    local_rdi = (local_rdi) >> (16);
    v_stack_m88 = local_rdi;
    result = MiGetWsleContents(*(uint64_t *)(local_r13 + 0x10), local_rdi, a3, local_rbx + 1);
    if (sign_flag) goto loc_0022E8A5;
    local_r14 = (*(uint64_t *)(arg1 + 0x48)) >> (9);
    local_r14 = (local_r14) & (result);
    local_r14 = (*(uint64_t *)(local_r14 + result * 1)) >> (12);
    local_r14 = (local_r14) & (result);
    a3 = (local_r14 + local_r14 * 2) << (4);
    a3 = (a3) + (result);
    result = (*(uint64_t *)(local_r13 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    v_stack_mA8 = a3;
    v_stack_m90 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xC01B9D) + result * 8);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01B9D) + *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x4AE) * 8)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01B9D) + result * 8))) goto loc_0022F16D;
loc_0022E512:
    local_rsi = *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x10);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))) & (1)) != 0) {
        local_r10 = (uint32_t)((local_r10) | (2));
        local_rsi = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x10)) & ((uint32_t)(*(uint32_t *)(arg1 + 0x18)));
        v_stack_p10 = (uint32_t)(local_r10);
        local_rsi = (local_rsi) | (32);
        *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x10) = local_rsi;
    }
    if ((uint32_t)(local_r10) != 0) goto loc_0022E889;
loc_0022E546:
    local_rbx = (uint8_t)(((uint8_t)(result)) & (15));
    if (((uint8_t)(local_rbx)) != 8) goto loc_0022E584;
    result = MiLockPageTablePage(a3, 3, a3, *(uint64_t *)(*(uint64_t *)(v_rip + 0xC01B9D) + result * 8));
    if ((uint32_t)(result) != 0) goto loc_0022E584;
    result = MiReturnCloneCharges(v_stack_m90, (uint32_t)(v_stack_p10), a3, *(uint64_t *)(*(uint64_t *)(v_rip + 0xC01B9D) + result * 8));
    goto loc_0022E3B7;
loc_0022E584:
    local_rbx = 0;
loc_0022E58A:
    if (condition_is_below) goto loc_0022E9BF;
    result = (*(uint64_t *)(v_stack_mA8 + 0x18)) ^ (*(uint64_t *)(v_stack_mA8 + 0x18) + 1);
    result = (result) & (a3);
    result = (result) ^ (*(uint64_t *)(v_stack_mA8 + 0x18) + 1);
    *(uint64_t *)(v_stack_mA8 + 0x18) = result;
    if (((v_stack_p20) & (66)) == 0) goto loc_0022EA5F;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x30))) & ((uint32_t)((uint32_t)(0x600000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x600000ULL)))) goto loc_0022F1A2;
loc_0022E5E6:
    local_rdi = 0;
loc_0022E5E8:
    if (condition_is_below) goto loc_0022EA40;
    result = MiCaptureDirtyBitToPfn(local_r13, v_stack_mA8, v_stack_m80, 1);
loc_0022E605:
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(local_r13 + 0x10))) >> (1));
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_0022F1C1;
    *(uint64_t *)(local_r13 + 0x8) = *(uint64_t *)(arg1 + 0x48);
    result = (*(uint64_t *)(local_r13 + 0x28)) | (local_r13);
    *(uint64_t *)(local_r13 + 0x28) = result;
    result = MiSetPfnContainingFrame(local_r13, local_r14, *(uint64_t *)(local_r13 + 0x10), 1);
    result = MI_MAKE_PROTECT_WRITE_COPY(local_r13 + 16, local_r14, *(uint64_t *)(local_r13 + 0x10), 1);
    local_r14 = (*(uint64_t *)(local_r13 + 0x10)) >> (5);
    result = MiTransferPageFileOwnership(local_r13, v_stack_mA0, *(uint64_t *)(local_r13 + 0x10), 1);
    if (result != 0) goto loc_0022F041;
loc_0022E665:
    if (!(condition_is_above_or_equal)) {
        v_stack_p20 = v_stack_p20;
    }
    result = MiWriteValidPteNewProtection(v_stack_mA0, v_stack_p20, *(uint64_t *)(local_r13 + 0x10), 1);
    if ((*(uint64_t *)(arg1 + 0x68)) == 0) goto loc_0022EBF7;
loc_0022E692:
    a4 = 0;
    result = MiInsertTbFlushEntry(*(uint64_t *)(arg1 + 0x68), v_stack_m88, a4 + 1, a4);
    if (condition_is_below) goto loc_0022EF14;
loc_0022E6BC:
    a3 = 0;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) = v_stack_p20;
    result = MiSetWsleProtection(*(uint64_t *)(arg1 + 0x68), v_stack_m88, a3, a4);
    Arg1 = (*(uint64_t *)(local_r13 + 0x8)) | (result);
    result = MiMakePrototypePteDirect(Arg1, v_stack_m88, a3, a4);
    v_stack_p20 = result;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))) & (1)) != 0) {
        result = (result) | (8);
        v_stack_p20 = result;
    }
    Arg1 = ((uint32_t)((uint32_t)(local_r14))) ^ (v_stack_mB8);
    Arg1 = (Arg1) & (-32);
    Arg1 = (Arg1) ^ ((uint32_t)((uint32_t)(local_r14)));
    *(void **)(*(uint64_t *)(arg1 + 0x48) + 0x10) = Arg1;
    local_rbx = 0;
loc_0022E715:
    if (condition_is_below) goto loc_0022E9DE;
    *(uint64_t *)(v_stack_mD8) = v_stack_p20;
    result = MiIncreaseUsedPtesInPfn(*(uint64_t *)(arg1 + 0x50), 1, a3, a4);
    a4 = 0;
    a3 = (a3) | (-1);
    result = MiUpdateWorkingSetPrivateSize(v_stack_mB8, v_stack_m88, a3, a4);
loc_0022E76E:
loc_0022E773:
    *(uint64_t *)(arg1 + 0x38) = v_xmm1;
loc_0022E78B:
    if (v_stack_mB0 != -1) goto loc_0022F2DF;
loc_0022E799:
    result = 0;
    local_rsp = (local_rsp) + (200);
    return result;
loc_0022E7B0:
    if (0 == 0) goto loc_0022E7C2;
    if (((*(uint32_t *)(v_stack_m88 + 0x30)) & (0x2000000ULL)) != 0) goto loc_0022EF56;
loc_0022E7C2:
    *(uint64_t *)(arg1 + 0x38) = v_xmm1;
    goto loc_0022E799;
loc_0022E7DC:
    if (condition_is_below) goto loc_0022EC20;
    if (condition_is_below) goto loc_0022EA27;
    local_rdi = (a3) >> (5);
    local_rdi = (uint32_t)((local_rdi) & (31));
    result = IS_PTE_NOT_DEMAND_ZERO(a3, v_stack_m88, a3, a4);
    if ((uint32_t)(result) != 0) goto loc_0022EB73;
    result = (uint8_t)(((uint8_t)(a3)) >> (1));
    if (((0) & ((uint8_t)(result))) != 0) goto loc_0022F2C4;
loc_0022E81A:
    a2 = 0;
    result = MiUpdatePageFileHighInPte(a3, a2, a3, a4);
    result = (result) & (0xFFFFFFFFFFFF0FFFULL);
    v_stack_p20 = result;
    result = MI_IS_SOFTWARE_PTE_SHADOW_STACK(result, a2, a3, a4);
    if ((uint32_t)(result) != 0) goto loc_0022F011;
    if (v_stack_m68 == 0) goto loc_0022F011;
    result = MiFindZeroCloneBlock(v_stack_m68, (uint32_t)((uint32_t)(local_rdi)), a3, a4);
    v_stack_mC8 = result;
    if (result != 0) goto loc_0022EED5;
loc_0022E869:
    local_rbx = 0;
loc_0022E86F:
    if (condition_is_below) goto loc_0022ED19;
    *(uint64_t *)(v_stack_mD8) = v_stack_p20;
    goto loc_0022E999;
loc_0022E889:
    result = MiGetCloneCharges(0, (uint32_t)((uint32_t)(local_r10)), result, a4);
    if ((uint32_t)(result) == 0) goto loc_0022EA0D;
    goto loc_0022E546;
loc_0022E8A5:
    local_r11 = (*(uint64_t *)(v_stack_mD8 + 0x8)) | (result);
    result = MiGetWsleProtection(*(uint64_t *)(arg1 + 0x50), 0, v_stack_mA8, a4);
    if ((uint32_t)(result) != 0) goto loc_0022EF04;
    result = MiMakePrototypePteDirect(local_r11, 0, v_stack_mA8, a4);
    v_stack_p20 = result;
    if (condition_is_below) goto loc_0022E8EB;
    if (!sign_flag) goto loc_0022F209;
loc_0022E8EB:
    if (condition_is_below) goto loc_0022E903;
    if (!sign_flag) goto loc_0022F221;
loc_0022E903:
    v_stack_p20 = v_stack_mC8;
    result = MiReferenceExistingCloneProto(v_stack_mD0 + 1024, local_r11, (uint32_t)(*(uint32_t *)(arg1 + 0x18)), Arg1 + 32);
    if ((uint32_t)(result) == 0) goto loc_0022EA0D;
    if (v_stack_mC8 != 0) goto loc_0022EFB5;
    result = MiIsPrototypePteVadLookup(*(uint64_t *)(v_stack_mD8 + 0x10), local_r11, (uint32_t)(*(uint32_t *)(arg1 + 0x18)), Arg1 + 32);
    if ((uint32_t)(result) != 0) goto loc_0022E97B;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x30))) & (112));
    if (((uint8_t)(result)) != 32) goto loc_0022E97B;
    result = MiIsVadLargePrivate(v_stack_m80, local_r11, (uint32_t)(*(uint32_t *)(arg1 + 0x18)), Arg1 + 32);
    if ((uint32_t)(result) != 0) goto loc_0022E97B;
    result = MiMakePerSessionProtoPte(v_stack_mC0, v_stack_mD0, local_r14, v_stack_m80);
    if (result != 0) goto loc_0022F254;
loc_0022E97B:
    local_rbx = 0;
loc_0022E981:
    if (condition_is_below) goto loc_0022EEB6;
loc_0022E98E:
    *(uint64_t *)(v_stack_mD8) = v_stack_p20;
loc_0022E999:
    result = MiIncreaseUsedPtesInPfn(*(uint64_t *)(arg1 + 0x50), 1, local_r14, v_stack_m80);
    goto loc_0022E773;
loc_0022E9BF:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xD968E5)) & ((uint32_t)(local_rbx))) == 0) goto loc_0022EFBF;
loc_0022E9CD:
loc_0022E9CF:
    if (!sign_flag) goto loc_0022E58A;
    goto loc_0022E9BF;
loc_0022E9DE:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xD968C6)) & ((uint32_t)(local_rbx))) == 0) goto loc_0022EFEA;
loc_0022E9EC:
loc_0022E9EE:
    if (!sign_flag) goto loc_0022E715;
    goto loc_0022E9DE;
loc_0022E9FD:
    result = MiIncrementCombinedPte(*(uint64_t *)(arg1 + 0x50), 1, (uint32_t)((uint32_t)(v_stack_m80)), v_stack_m80);
    if ((uint32_t)(result) != 0) goto loc_0022ECCA;
loc_0022EA0D:
    result = MiWriteUselessChildPte(v_stack_mD8, *(uint64_t *)(arg1 + 0x50), (uint32_t)((uint32_t)(v_stack_m80)), v_stack_m80);
    *(uint32_t *)(arg1 + 0x60) = 1;
    goto loc_0022E773;
loc_0022EA27:
    result = MiHandleForkTransitionPte(Arg1, v_stack_mB0, (uint32_t)((uint32_t)(v_stack_m80)), v_stack_m80);
    if ((uint32_t)(result) != 0) goto loc_0022E78B;
    goto loc_0022EBE8;
loc_0022EA40:
    local_rdi = (uint32_t)((*(uint64_t *)(arg1 + 0x50)) + 1);
    if (((*(uint32_t *)(v_rip + 0xD96864)) & ((uint32_t)(local_rdi))) == 0) goto loc_0022F01A;
loc_0022EA4E:
loc_0022EA50:
    if (!sign_flag) goto loc_0022E5E8;
    goto loc_0022EA40;
loc_0022EA5F:
    local_r15 = 0;
loc_0022EA62:
    if (condition_is_below) goto loc_0022ECF8;
    goto loc_0022E605;
loc_0022EA78:
    if (sign_flag) goto loc_0022E442;
loc_0022EA84:
loc_0022EA88:
    a3 = 0;
    result = MiInitializePageColorBase(v_stack_mB8, a3 + 3, a3, v_stack_m78);
    a2 = 0;
    Arg1 = (v_stack_m70) >> (16);
    Arg1 = (uint32_t)((Arg1) & (3));
    if (v_stack_mB0 != -1) goto loc_0022EB1D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mD8 + 0x20))) >> (16));
    Arg1 = (uint32_t)(((uint8_t)(result)) & (0xFFFFFFC0ULL));
    Arg1 = (uint32_t)((Arg1) << (12));
    a2 = (uint32_t)(((uint32_t)(v_stack_m70)) & (0xFFF3FF00ULL));
    Arg1 = (uint32_t)((Arg1) | (0));
    a2 = (uint32_t)((a2) | ((uint32_t)(Arg1)));
    result = MiGetPage(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC015BC) + *(uint16_t *)(v_stack_mD0 + 0x4AE) * 8), a2, 1, v_stack_m78);
    v_stack_mB0 = result;
    if (result == -1) goto loc_0022F25D;
loc_0022EB1D:
    Arg1 = (result + result * 2) << (4);
    Arg1 = (Arg1) + (result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mD8 + 0x20))) >> (16));
    a2 = (uint32_t)(((uint8_t)(result)) >> (6));
    result = MiFinalizePageAttribute(Arg1, a2, 16, v_stack_m78);
    v_stack_p20 = (uint8_t)(*(uint8_t *)(v_stack_p8 + 0x1C));
    result = MiDuplicateCloneLeaf(*(uint64_t *)(v_stack_p8 + 0x38), *(uint64_t *)(v_stack_p8 + 0x40), v_stack_mB0, *(uint64_t *)(v_stack_p8 + 0x50));
    goto loc_0022E7C2;
loc_0022EB73:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (0xFFFFFFF8ULL));
    if (((uint32_t)(result)) != 16) goto loc_0022ED38;
loc_0022EB81:
    v_stack_m60 = v_xmm0;
    if (*(uint64_t *)(v_stack_p8 + 0x68) != 0) goto loc_0022F185;
loc_0022EB95:
    result = MiUnlockWorkingSetExclusive(v_stack_mB8, *(uint8_t *)(v_stack_p8 + 0x1C), v_stack_mB0, *(uint64_t *)(v_stack_p8 + 0x50));
    Arg1 = (local_r14) << (25);
    result = (v_stack_mD8) << (25);
    Arg1 = (Arg1) - (result);
    v_stack_m58 = 0x1000ULL;
    Arg1 = (Arg1) >> (16);
    v_stack_m60 = Arg1;
    result = MiPrefetchVirtualMemory(1, v_stack_m60, v_stack_mB8, 173);
    result = MiLockWorkingSetExclusive(v_stack_mB8, v_stack_m60, v_stack_mB8, 173);
    *(uint8_t *)(v_stack_p8 + 0x1C) = (uint8_t)(result);
loc_0022EBE8:
    goto loc_0022E3C1;
loc_0022EBF7:
    result = MiGetProcessorFlushList(v_stack_mB8, v_stack_m60, v_stack_mB8, 1);
    a4 = 0;
    *(uint64_t *)(v_stack_p8 + 0x68) = result;
    v_stack_p20 = 32;
    result = MiInitializeTbFlushList(result, v_stack_mB8, (uint32_t)(*(uint32_t *)(result + 0xC)), a4);
    goto loc_0022E692;
loc_0022EC20:
    if (*(uint64_t *)(v_rip + 0xBFF059) == 0) goto loc_0022EC3F;
    local_r10 = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (16)) == 0) {
        local_r10 = *(uint64_t *)(v_rip + 0xBFF059);
        local_r10 = ~(local_r10);
        local_r10 = (local_r10) & ((uint32_t)(*(uint32_t *)(result + 0xC)));
    }
    local_r10 = (local_r10) >> (16);
    result = MI_PROTO_FORMAT_COMBINED((uint32_t)(*(uint32_t *)(result + 0xC)), v_stack_mB8, (uint32_t)(*(uint32_t *)(result + 0xC)), a4);
    if ((uint8_t)(result) != 0) goto loc_0022E9FD;
    v_stack_p20 = v_stack_mC8;
    result = MiReferenceExistingCloneProto(v_stack_mD0 + 1024, local_r10, (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x18)), v_stack_p8 + 32);
    if ((uint32_t)(result) == 0) goto loc_0022EA0D;
    if (v_stack_mC8 != 0) goto loc_0022F058;
    result = MiIsPrototypePteVadLookup(v_stack_p20, local_r10, (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x18)), v_stack_p8 + 32);
    if ((uint32_t)(result) != 0) goto loc_0022ECCA;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x30))) & (112));
    if (((uint8_t)(result)) != 32) goto loc_0022ECCA;
    result = MiIsVadLargePrivate(v_stack_m80, local_r10, (uint32_t)(*(uint32_t *)(v_stack_p8 + 0x18)), v_stack_p8 + 32);
    if ((uint32_t)(result) != 0) goto loc_0022ECCA;
    result = MiMakePerSessionProtoPte(v_stack_mC0, v_stack_mD0, local_r14, v_stack_m80);
    if (result != 0) goto loc_0022F2D6;
loc_0022ECCA:
    local_rbx = 0;
loc_0022ECD0:
    if (condition_is_above_or_equal) goto loc_0022E98E;
loc_0022ECDD:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xD965C7)) & ((uint32_t)(local_rbx))) == 0) goto loc_0022F10E;
loc_0022ECEB:
loc_0022ECED:
    if (!sign_flag) goto loc_0022ECD0;
    goto loc_0022ECDD;
loc_0022ECF8:
    local_r15 = (uint32_t)((v_stack_p8) + 1);
    if (((*(uint32_t *)(v_rip + 0xD965AA)) & ((uint32_t)(local_r15))) == 0) goto loc_0022F071;
loc_0022ED08:
loc_0022ED0A:
    if (!sign_flag) goto loc_0022EA62;
    goto loc_0022ECF8;
loc_0022ED19:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xD9658B)) & ((uint32_t)(local_rbx))) == 0) goto loc_0022F099;
loc_0022ED27:
loc_0022ED29:
    if (!sign_flag) goto loc_0022E86F;
    goto loc_0022ED19;
loc_0022ED38:
    result = MI_IS_SOFTWARE_PTE_SHADOW_STACK(local_r14, v_stack_mD0, local_r14, v_stack_m80);
    if ((uint32_t)(result) != 0) goto loc_0022EB81;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01339) + *(uint16_t *)(v_stack_mD0 + 0x4AE) * 8)) != (*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01339) + *(uint16_t *)(v_stack_mC0 + 0x4AE) * 8))) goto loc_0022F27E;
loc_0022ED71:
    local_rbx = *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x10);
    if ((((uint8_t)(v_stack_m80)) & ((uint8_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x18))))) != 0) {
        local_r10 = (uint32_t)((local_r10) | (2));
        local_rbx = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x10)) & ((uint32_t)(*(uint32_t *)(local_r15 + 0x18)));
        local_rbx = (local_rbx) | (32);
        *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x10) = local_rbx;
    }
    if ((uint32_t)(local_r10) == 0) goto loc_0022EDB7;
    result = MiGetCloneCharges(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01339) + *(uint16_t *)(v_stack_mC0 + 0x4AE) * 8), (uint32_t)((uint32_t)(local_r10)), local_r14, v_stack_m80);
    if ((uint32_t)(result) == 0) goto loc_0022EA0D;
loc_0022EDB7:
    result = (uint8_t)(((uint8_t)(v_stack_p20)) >> (2));
    if (((1) & ((uint8_t)(result))) == 0) goto loc_0022EE0B;
    if (*(uint64_t *)(v_rip + 0xBFEEB4) == 0) goto loc_0022EDE2;
    if ((((uint8_t)(v_stack_p20)) & (16)) == 0) {
        a2 = *(uint64_t *)(v_rip + 0xBFEEB4);
        a2 = ~(a2);
        a2 = (a2) & (v_stack_p20);
    }
    Arg1 = (v_stack_p20) >> (12);
    Arg1 = (uint32_t)((Arg1) & (15));
    a2 = (a2) >> (32);
    result = MiUpdatePageFileBlockOwner(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01339) + *(uint16_t *)(v_stack_mC0 + 0x4AE) * 8) + arg1 * 8 + 0x4860), a2, *(uint64_t *)(arg1 + 0x48), local_r14);
loc_0022EE0B:
    result = v_stack_p20;
    if (sign_flag) {
        result = (v_stack_p20) | (32);
        v_stack_p20 = result;
    }
    a2 = (uint8_t)(((uint8_t)(v_stack_p20)) >> (1));
    if (((1) & ((uint8_t)(a2))) != 0) goto loc_0022F28E;
loc_0022EE2C:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x48)) = v_stack_p20;
    result = MiMakePrototypePteDirect(*(uint64_t *)(arg1 + 0x48), a2, *(uint64_t *)(arg1 + 0x48), 1);
    v_stack_p20 = result;
    *(uint64_t *)(local_r14) = result;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x18))))) == 0) goto loc_0022EE56;
    if (((uint32_t)(*(uint64_t *)(v_stack_p8 + 0x50))) != 24) {
    }
    local_rbx = (local_rbx) & (-32);
    local_rbx = (local_rbx) | ((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_p8 + 0x50))));
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x10) = local_rbx;
    local_rbx = 0;
loc_0022EE6E:
    if (condition_is_below) goto loc_0022EF95;
    *(uint64_t *)(v_stack_mD8) = v_stack_p20;
    result = MiIncreaseUsedPtesInPfn(*(uint64_t *)(local_r15 + 0x50), (uint32_t)((uint32_t)(local_rbx + 1)), *(uint64_t *)(arg1 + 0x48), 1);
    goto loc_0022E76E;
loc_0022EEB6:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xD963EE)) & ((uint32_t)(local_rbx))) == 0) goto loc_0022F0C0;
loc_0022EEC4:
loc_0022EEC6:
    if (!sign_flag) goto loc_0022E981;
    goto loc_0022EEB6;
loc_0022EED5:
    v_stack_p28 = local_r15 + 32;
    v_stack_p20 = *(uint64_t *)(local_r15 + 0x50);
    result = MiWriteSharedDemandZeroPte(*(uint64_t *)(local_r15 + 0x50), (uint32_t)((uint32_t)(local_rbx + 1)), *(uint64_t *)(arg1 + 0x48), v_stack_mC0);
    if ((uint32_t)(result) != 0) goto loc_0022E773;
    goto loc_0022E869;
loc_0022EF04:
    result = MiMakePrototypePteVadLookup((uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_rbx + 1)), *(uint64_t *)(arg1 + 0x48), v_stack_mC0);
    v_stack_p20 = result;
    goto loc_0022E8EB;
loc_0022EF14:
    if ((((uint8_t)(local_rbx)) & (32)) != 0) goto loc_0022E6BC;
    result = (result) + ((uint32_t)((uint32_t)(result)));
    if ((*(uint64_t *)(arg1 + 0x48)) < result) goto loc_0022E6BC;
    result = MiCheckLinearProtectedPteAccessedBit(*(uint64_t *)(arg1 + 0x48), local_rbx, 128, v_stack_mC0);
    goto loc_0022E6BC;
loc_0022EF56:
    a2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r15 + 0x50) + 0x30))) >> (7));
    a2 = (uint32_t)((a2) & (31));
    result = MiFindZeroCloneBlock(local_rbx, a2, 128, v_stack_mC0);
    if (result == 0) goto loc_0022E7C2;
    v_stack_p28 = local_r15 + 32;
    v_stack_p20 = *(uint64_t *)(local_r15 + 0x50);
    result = MiWriteSharedDemandZeroPte(*(uint64_t *)(local_r15 + 0x50), a2, result, v_stack_mC0);
    goto loc_0022E7C2;
loc_0022EF95:
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(v_stack_mC0)));
    if (((*(uint32_t *)(v_rip + 0xD9630E)) & ((uint32_t)(local_rbx))) == 0) goto loc_0022F0E7;
loc_0022EFA4:
loc_0022EFA6:
    if (!sign_flag) goto loc_0022EE6E;
    goto loc_0022EF95;
loc_0022EFB5:
    goto loc_0022E97B;
loc_0022EFBF:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD97AF3)))) & (64)) == 0) goto loc_0022E9CD;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(local_r15 + 0x50), a2, result, v_stack_mC0);
    if ((uint8_t)(result) == 0) goto loc_0022F199;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), a2, result, v_stack_mC0);
    goto loc_0022E9CF;
loc_0022EFEA:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD97AC8)))) & (64)) == 0) goto loc_0022E9EC;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbx)), v_stack_mA8, result, v_stack_mC0);
    if ((uint8_t)(result) == 0) goto loc_0022E9EC;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), v_stack_mA8, result, v_stack_mC0);
    goto loc_0022E9EE;
loc_0022F011:
    goto loc_0022E869;
loc_0022F01A:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD97A98)))) & (64)) == 0) goto loc_0022EA4E;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbx)), v_stack_mA8, result, v_stack_mC0);
    if ((uint8_t)(result) == 0) goto loc_0022EA4E;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(*(uint64_t *)(local_r15 + 0x50))), v_stack_mA8, result, v_stack_mC0);
    goto loc_0022EA50;
loc_0022F041:
    result = MiReleasePageFileInfo(v_stack_m90, *(uint64_t *)(local_r15 + 0x50), 1, v_stack_mC0);
    goto loc_0022E665;
loc_0022F058:
    result = (uint32_t)((*(uint64_t *)(result + 0x10)) & (31));
    if (((uint8_t)(result)) == 24) goto loc_0022ECCA;
    goto loc_0022ECCA;
loc_0022F071:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD97A41)))) & (64)) == 0) goto loc_0022ED08;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_stack_m90, *(uint64_t *)(local_r15 + 0x50), 1, v_stack_mC0);
    if ((uint8_t)(result) == 0) goto loc_0022ED08;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r15)), *(uint64_t *)(local_r15 + 0x50), 1, v_stack_mC0);
    goto loc_0022ED0A;
loc_0022F099:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD97A19)))) & (64)) == 0) goto loc_0022ED27;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_r15)), *(uint64_t *)(local_r15 + 0x50), 1, v_stack_mC0);
    if ((uint8_t)(result) == 0) goto loc_0022ED27;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), *(uint64_t *)(local_r15 + 0x50), 1, v_stack_mC0);
    goto loc_0022ED29;
loc_0022F0C0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD979F2)))) & (64)) == 0) goto loc_0022EEC4;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbx)), *(uint64_t *)(local_r15 + 0x50), 1, v_stack_mC0);
    if ((uint8_t)(result) == 0) goto loc_0022EEC4;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), *(uint64_t *)(local_r15 + 0x50), 1, v_stack_mC0);
    goto loc_0022EEC6;
loc_0022F0E7:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD979CB)))) & (64)) == 0) goto loc_0022EFA4;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbx)), *(uint64_t *)(local_r15 + 0x50), 1, v_stack_mC0);
    if ((uint8_t)(result) == 0) goto loc_0022EFA4;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), *(uint64_t *)(local_r15 + 0x50), 1, v_stack_mC0);
    goto loc_0022EFA6;
loc_0022F10E:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD979A4)))) & (64)) == 0) goto loc_0022ECEB;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbx)), *(uint64_t *)(local_r15 + 0x50), 1, v_stack_mC0);
    if ((uint8_t)(result) == 0) goto loc_0022ECEB;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), *(uint64_t *)(local_r15 + 0x50), 1, v_stack_mC0);
    goto loc_0022ECED;
loc_0022F135:
    a2 = 0;
    result = MiMakeSystemAddressValid(local_r14, a2, *(uint8_t *)(local_r15 + 0x1C), v_stack_mC0);
    v_stack_p20 = *(uint64_t *)(local_r14);
    goto loc_0022E3FC;
loc_0022F16D:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x8) = 1;
    v_stack_p10 = 5;
    goto loc_0022E512;
loc_0022F185:
    result = MiFlushTbList(local_r14, a2, *(uint64_t *)(local_r14), 1);
    result = MiReleaseProcessorFlushList(local_r14, a2, *(uint64_t *)(local_r14), 1);
    goto loc_0022EB95;
loc_0022F199:
    goto loc_0022E9CD;
loc_0022F1A2:
    if (sign_flag) goto loc_0022E5E6;
    result = MiCaptureWriteWatchDirtyBit(v_stack_mC0, v_stack_m88, *(uint64_t *)(local_r14), 1);
    goto loc_0022E5E6;
loc_0022F1C1:
    result = (*(uint64_t *)(local_r14)) >> (12);
    result = (uint32_t)((result) & (15));
    local_rdi = -(*(uint64_t *)(local_r15 + 0x50));
    a4 = (uint32_t)(-(1));
    a4 = (uint32_t)((a4) + (2));
    result = ~(*(uint64_t *)(v_rip + 0xBFEA99));
    a3 = (*(uint64_t *)(local_r14)) & (result);
loc_0022F209:
    if (*(uint64_t *)(v_stack_mD8 + 0x8) == 0) goto loc_0022E8EB;
    goto loc_0022E8EB;
loc_0022F221:
    if (*(uint64_t *)(v_stack_mD8 + 0x8) == 0) goto loc_0022E903;
    Arg1 = (v_stack_mD0) + (0x400ULL);
    result = MiIncrementCombinedPte(Arg1, v_stack_mD0, 1, a4);
    if ((uint32_t)(result) != 0) goto loc_0022E97B;
    goto loc_0022EA0D;
loc_0022F254:
    v_stack_p20 = result;
    goto loc_0022E97B;
loc_0022F25D:
    result = MiFlushTbList(*(uint64_t *)(local_r15 + 0x68), v_stack_mD0, 1, a4);
    result = MiReleaseProcessorFlushList(*(uint64_t *)(local_r15 + 0x68), v_stack_mD0, 1, a4);
loc_0022F27E:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x8) = a4;
    goto loc_0022ED71;
loc_0022F28E:
    v_stack_m98 = result;
    result = (v_stack_m98) & (-5);
    v_stack_m98 = result;
    result = MiReleasePageFileInfo(*(uint64_t *)(*(uint64_t *)(v_rip + 0xC01339) + *(uint16_t *)(v_stack_mC0 + 0x4AE) * 8), result, (uint32_t)((uint32_t)(a4)), a4);
    result = MiClearPageFileReservation(v_stack_p20, result, (uint32_t)((uint32_t)(a4)), a4);
    goto loc_0022EE2C;
loc_0022F2C4:
    result = MiClearPageFileReservation(v_stack_p20, result, (uint32_t)((uint32_t)(a4)), 1);
    goto loc_0022E81A;
loc_0022F2D6:
    v_stack_p20 = result;
    goto loc_0022ECCA;
loc_0022F2DF:
    Arg1 = (result + result * 2) << (4);
    Arg1 = (Arg1) + (result);
    result = MiLockAndInsertPageInFreeList(Arg1, result, v_stack_p20, 1);
    goto loc_0022E799;
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
| `Arg1` | `+ 0x1C` | `8` | `R` |
| `Arg1` | `+ 0x1C` | `8` | `W` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R/W` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x38` | `128` | `R` |
| `Arg1` | `+ 0x38` | `128` | `W` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R/W` |
| `Arg1` | `+ 0x60` | `32` | `W` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0022E32C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
