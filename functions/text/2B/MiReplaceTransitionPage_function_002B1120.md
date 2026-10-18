# MiReplaceTransitionPage

- RVA: `0x002B1120`–`0x002B1B28` (길이 `2,568` bytes)
- VA: `0x00000001402B1120`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006D638`
- 디코드: `606`개 명령, `2,568/2,568` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **40**; 고유 호출 대상: **32**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x002B1162` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002B1225` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x002B1257` → [MiChangePageAttribute](../33/MiChangePageAttribute_function_00332ECC.md) (function, `0x00332ECC`)
- `0x002B1277` → [MiCopyPfnEntryEx](MiCopyPfnEntryEx_function_002B2670.md) (function, `0x002B2670`)
- `0x002B12B5` → [MiCopyPage](MiCopyPage_function_002B1B30.md) (function, `0x002B1B30`)
- `0x002B1315` → [MiGetPfnPriority](../32/MiGetPfnPriority_function_003226F0.md) (function, `0x003226F0`)
- `0x002B134F` → [MI_NODE_FROM_PFN](MI_NODE_FROM_PFN_function_002B0F30.md) (function, `0x002B0F30`)
- `0x002B1359` → [MI_NODE_FROM_PFN](MI_NODE_FROM_PFN_function_002B0F30.md) (function, `0x002B0F30`)
- `0x002B1377` → [MiGetPfnSlabType](../28/MiGetPfnSlabType_function_0028E2D0.md) (function, `0x0028E2D0`)
- `0x002B13A0` → [MiAcquirePageListLock](../27/MiAcquirePageListLock_function_0027C450.md) (function, `0x0027C450`)
- `0x002B13B6` → [MiReplaceStandbyLookaside](../33/MiReplaceStandbyLookaside_function_003397D0.md) (function, `0x003397D0`)
- `0x002B1522` → [MiReplaceSecondaryListStandbyPage](MiReplaceSecondaryListStandbyPage_function_002B9270.md) (function, `0x002B9270`)
- `0x002B1550` → [MiUpdateLargePageCandidateValue](../33/MiUpdateLargePageCandidateValue_function_0033EF80.md) (function, `0x0033EF80`)
- `0x002B1573` → [MiUpdateLargePageCandidateValue](../33/MiUpdateLargePageCandidateValue_function_0033EF80.md) (function, `0x0033EF80`)
- `0x002B158F` → [MiReleasePageListLock](MiReleasePageListLock_function_002B1050.md) (function, `0x002B1050`)
- `0x002B1622` → [MiMapPageInHyperSpaceWorker](../33/MiMapPageInHyperSpaceWorker_function_00332B10.md) (function, `0x00332B10`)
- `0x002B163C` → [MI_READ_PTE_LOCK_FREE](../28/MI_READ_PTE_LOCK_FREE_function_002828A0.md) (function, `0x002828A0`)
- `0x002B1678` → [MiSwizzleInvalidPte](../28/MiSwizzleInvalidPte_function_0028F5E0.md) (function, `0x0028F5E0`)
- `0x002B168B` → [MiPteInShadowRange](../23/MiPteInShadowRange_function_0023FB00.md) (function, `0x0023FB00`)
- `0x002B176F` → [MiClearPfnReuseFields](../37/MiClearPfnReuseFields_function_003759F0.md) (function, `0x003759F0`)
- `0x002B17C9` → [MiIsDecayPfn](MiIsDecayPfn_function_002B9240.md) (function, `0x002B9240`)
- `0x002B17DD` → [MiUpdateTransitionPteFrame](../38/MiUpdateTransitionPteFrame_function_00385EDC.md) (function, `0x00385EDC`)
- `0x002B180A` → [MiAcquirePageListLock](../27/MiAcquirePageListLock_function_0027C450.md) (function, `0x0027C450`)
- `0x002B1825` → [MiIsDecayPfn](MiIsDecayPfn_function_002B9240.md) (function, `0x002B9240`)
- `0x002B1838` → [MiSetPfnContainingFrame](../36/MiSetPfnContainingFrame_function_00363FC0.md) (function, `0x00363FC0`)
- `0x002B1870` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002B188F` → [MiSetPfnContainingFrame](../36/MiSetPfnContainingFrame_function_00363FC0.md) (function, `0x00363FC0`)
- `0x002B18B3` → [MiDetermineModifiedPageListHead](MiDetermineModifiedPageListHead_function_002BAB00.md) (function, `0x002BAB00`)
- `0x002B18D2` → [MiGetSystemRegionType](../28/MiGetSystemRegionType_function_0028EC80.md) (function, `0x0028EC80`)
- `0x002B196E` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x002B197E` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x002B1998` → [MiUnlinkPageFromListEx](../28/MiUnlinkPageFromListEx_function_00287590.md) (function, `0x00287590`)
- `0x002B1A28` → [ExAcquireSpinLockExclusiveAtDpcLevel](../24/ExAcquireSpinLockExclusiveAtDpcLevel_function_00248E80.md) (function, `0x00248E80`)
- `0x002B1A3C` → [MiReplaceStandbyLookaside](../33/MiReplaceStandbyLookaside_function_003397D0.md) (function, `0x003397D0`)
- `0x002B1A46` → [MiSetStandbyLookasideState](../41/MiSetStandbyLookasideState_function_0041D620.md) (function, `0x0041D620`)
- `0x002B1A55` → [MiSanitizeShadowPxe](../29/MiSanitizeShadowPxe_function_00294B68.md) (function, `0x00294B68`)
- `0x002B1A6D` → [MiWritePteShadow](../29/MiWritePteShadow_function_00294EAC.md) (function, `0x00294EAC`)
- `0x002B1AA3` → [MiDecreaseAvailablePages](../3B/MiDecreaseAvailablePages_function_003BB570.md) (function, `0x003BB570`)
- `0x002B1AB5` → [MiGetPfnPriority](../32/MiGetPfnPriority_function_003226F0.md) (function, `0x003226F0`)
- `0x002B1B1E` → [MiInsertPageInList](MiInsertPageInList_function_002BA000.md) (function, `0x002BA000`)

### Direct callers
- [MiTradeTransitionPage](../28/MiTradeTransitionPage_function_0028B9AC.md) at `0x0028BC22`
- [MiWalkEntireImage](../36/MiWalkEntireImage_function_00365D70.md) at `0x00366F98`
- [MiHandleSpecialPurposeMemoryCachedFault](../44/MiHandleSpecialPurposeMemoryCachedFault_function_0044C740.md) at `0x0044C9FA`
- [MiRepointPteAtExtendedStandby](../68/MiRepointPteAtExtendedStandby_function_0068B6F4.md) at `0x0068B7B2`
- [MiMakeVaRangePhysicallyContiguous](../69/MiMakeVaRangePhysicallyContiguous_function_006936E0.md) at `0x006938BB`
- [sub_006F9D5A](../6F/Unknown_function_006F9D5A.md) at `0x006F9E0C`

### Static image references
- `0x002B1133` → RVA `0x00E0A740` (`.data`; read)
- `0x002B11A8` → RVA `0x00E30088` (`.data`; read)
- `0x002B12BE` → RVA `0x00FCF080` (`CACHEALI`; read)
- `0x002B1578` → RVA `0x00E3014C` (`.data`; read)
- `0x002B1641` → RVA `0x00E2DC80` (`.data`; read)
- `0x002B16D8` → RVA `0x00010880` (`.rdata`; read)
- `0x002B1783` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x002B18EB` → RVA `0x00FC6A87` (`ALMOSTRO`; read)
- `0x002B1960` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x002B19CD` → RVA `0x00E3D240` (`.data`; read)
- `0x002B1ADE` → RVA `0x00E301A8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x002B1B04` → [sub_006DB5D8](../6D/Unknown_function_006DB5D8.md) (`tail-transfer`)
  - `0x002B1B11` → [sub_006DB5D8 + 0x6D](../6D/Unknown_function_006DB5D8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002B1120  40 53                           push rbx
002B1122  56                              push rsi
002B1123  57                              push rdi
002B1124  41 54                           push r12
002B1126  41 55                           push r13
002B1128  41 56                           push r14
002B112A  41 57                           push r15
002B112C  48 81 EC F0 00 00 00            sub rsp, 0xf0
002B1133  48 8B 05 06 96 B5 00            mov rax, qword ptr [rip + 0xb59606]
002B113A  48 33 C4                        xor rax, rsp
002B113D  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
002B1145  41 8B D9                        mov ebx, r9d
002B1148  45 8B F0                        mov r14d, r8d
002B114B  4C 8B FA                        mov r15, rdx
002B114E  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
002B1152  48 8B F1                        mov rsi, rcx
002B1155  33 FF                           xor edi, edi
002B1157  33 D2                           xor edx, edx
002B1159  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
002B115E  44 8D 47 68                     lea r8d, [rdi + 0x68]
002B1162  E8 D9 5A 41 00                  call 0x1406c6c40
002B1167  B8 FF FF FF 00                  mov eax, 0xffffff
002B116C  48 BA 00 00 00 00 00 DE FF FF   movabs rdx, 0xffffde0000000000
002B1176  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002B117B  48 8B C2                        mov rax, rdx
002B117E  48 8B CE                        mov rcx, rsi
002B1181  49 B8 AB AA AA AA AA AA AA AA   movabs r8, 0xaaaaaaaaaaaaaaab
002B118B  48 2B C8                        sub rcx, rax
002B118E  48 C1 F9 04                     sar rcx, 4
002B1192  49 0F AF C8                     imul rcx, r8
002B1196  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
002B119B  48 8B C2                        mov rax, rdx
002B119E  4D 8B EF                        mov r13, r15
002B11A1  4C 2B E8                        sub r13, rax
002B11A4  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
002B11A8  48 8B 0D D9 EE B7 00            mov rcx, qword ptr [rip + 0xb7eed9]
002B11AF  48 C1 E8 2B                     shr rax, 0x2b
002B11B3  25 FF 03 00 00                  and eax, 0x3ff
002B11B8  49 C1 FD 04                     sar r13, 4
002B11BC  4D 0F AF E8                     imul r13, r8
002B11C0  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
002B11C4  0F B6 46 22                     movzx eax, byte ptr [rsi + 0x22]
002B11C8  83 E0 07                        and eax, 7
002B11CB  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
002B11D0  48 8B 84 C1 E0 1B 00 00         mov rax, qword ptr [rcx + rax*8 + 0x1be0]
002B11D8  8B CB                           mov ecx, ebx
002B11DA  83 E1 02                        and ecx, 2
002B11DD  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002B11E2  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
002B11E6  75 14                           jne 0x1402b11fc
002B11E8  45 33 E4                        xor r12d, r12d
002B11EB  F0 49 0F BA 6F 18 3F            lock bts qword ptr [r15 + 0x18], 0x3f
002B11F2  0F 82 88 05 00 00               jb 0x1402b1780
002B11F8  8B 4C 24 30                     mov ecx, dword ptr [rsp + 0x30]
002B11FC  41 8B 47 20                     mov eax, dword ptr [r15 + 0x20]
002B1200  C1 E8 18                        shr eax, 0x18
002B1203  A8 40                           test al, 0x40
002B1205  0F 85 45 06 00 00               jne 0x1402b1850
002B120B  0F B6 46 22                     movzx eax, byte ptr [rsi + 0x22]
002B120F  24 07                           and al, 7
002B1211  3C 03                           cmp al, 3
002B1213  0F 84 E9 06 00 00               je 0x1402b1902
002B1219  45 0F B6 67 24                  movzx r12d, byte ptr [r15 + 0x24]
002B121E  49 8B CF                        mov rcx, r15
002B1221  41 83 E4 0F                     and r12d, 0xf
002B1225  E8 A6 D0 FD FF                  call 0x14028e2d0
002B122A  8B 4E 20                        mov ecx, dword ptr [rsi + 0x20]
002B122D  C1 E9 10                        shr ecx, 0x10
002B1230  0F B6 D1                        movzx edx, cl
002B1233  41 8B 4F 20                     mov ecx, dword ptr [r15 + 0x20]
002B1237  C1 E9 10                        shr ecx, 0x10
002B123A  44 0F B6 C1                     movzx r8d, cl
002B123E  41 C1 E8 06                     shr r8d, 6
002B1242  C1 EA 06                        shr edx, 6
002B1245  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
002B1249  44 3B C2                        cmp r8d, edx
002B124C  74 0E                           je 0x1402b125c
002B124E  41 B8 01 00 00 00               mov r8d, 1
002B1254  49 8B CF                        mov rcx, r15
002B1257  E8 70 1C 08 00                  call 0x140332ecc
002B125C  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
002B1260  48 B9 FF FF FF FF FF FF FF C7   movabs rcx, 0xc7ffffffffffffff
002B126A  48 23 C1                        and rax, rcx
002B126D  48 8B D6                        mov rdx, rsi
002B1270  49 8B CF                        mov rcx, r15
002B1273  49 89 47 18                     mov qword ptr [r15 + 0x18], rax
002B1277  E8 F4 13 00 00                  call 0x1402b2670
002B127C  41 0F B6 47 24                  movzx eax, byte ptr [r15 + 0x24]
002B1281  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
002B128B  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
002B1290  24 F0                           and al, 0xf0
002B1292  41 0A C4                        or al, r12b
002B1295  41 88 47 24                     mov byte ptr [r15 + 0x24], al
002B1299  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
002B129D  48 23 C1                        and rax, rcx
002B12A0  48 3B C3                        cmp rax, rbx
002B12A3  0F 84 E0 05 00 00               je 0x1402b1889
002B12A9  41 B8 06 00 00 00               mov r8d, 6
002B12AF  48 8B D3                        mov rdx, rbx
002B12B2  49 8B CD                        mov rcx, r13
002B12B5  E8 76 08 00 00                  call 0x1402b1b30
002B12BA  F0 09 3C 24                     lock or dword ptr [rsp], edi
002B12BE  8B 15 BC DD D1 00               mov edx, dword ptr [rip + 0xd1ddbc]
002B12C4  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
002B12C8  48 C1 E2 3B                     shl rdx, 0x3b
002B12CC  48 8B CA                        mov rcx, rdx
002B12CF  48 33 C8                        xor rcx, rax
002B12D2  48 B8 FF FF FF FF FF FF FF C7   movabs rax, 0xc7ffffffffffffff
002B12DC  48 23 C8                        and rcx, rax
002B12DF  48 33 CA                        xor rcx, rdx
002B12E2  F6 44 24 40 01                  test byte ptr [rsp + 0x40], 1
002B12E7  49 89 4F 18                     mov qword ptr [r15 + 0x18], rcx
002B12EB  0F 85 A3 02 00 00               jne 0x1402b1594
002B12F1  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
002B12F6  41 BA 02 00 00 00               mov r10d, 2
002B12FC  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
002B12FF  41 3B C2                        cmp eax, r10d
002B1302  0F 85 E3 04 00 00               jne 0x1402b17eb
002B1308  48 8B CE                        mov rcx, rsi
002B130B  41 83 FE 09                     cmp r14d, 9
002B130F  0F 8C 73 06 00 00               jl 0x1402b1988
002B1315  E8 D6 13 07 00                  call 0x1403226f0
002B131A  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
002B131F  49 81 C4 C0 0C 00 00            add r12, 0xcc0
002B1326  8B C8                           mov ecx, eax
002B1328  48 6B D1 58                     imul rdx, rcx, 0x58
002B132C  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002B1331  4C 03 E2                        add r12, rdx
002B1334  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
002B1339  41 83 FE 09                     cmp r14d, 9
002B133D  75 0D                           jne 0x1402b134c
002B133F  8B 4E 20                        mov ecx, dword ptr [rsi + 0x20]
002B1342  C1 E9 18                        shr ecx, 0x18
002B1345  F6 C1 08                        test cl, 8
002B1348  41 0F 45 FA                     cmovne edi, r10d
002B134C  48 8B CE                        mov rcx, rsi
002B134F  E8 DC FB FF FF                  call 0x1402b0f30
002B1354  49 8B CF                        mov rcx, r15
002B1357  8B D8                           mov ebx, eax
002B1359  E8 D2 FB FF FF                  call 0x1402b0f30
002B135E  44 8B 64 24 30                  mov r12d, dword ptr [rsp + 0x30]
002B1363  3B D8                           cmp ebx, eax
002B1365  0F 85 B4 06 00 00               jne 0x1402b1a1f
002B136B  45 3B F4                        cmp r14d, r12d
002B136E  0F 85 AB 06 00 00               jne 0x1402b1a1f
002B1374  48 8B CE                        mov rcx, rsi
002B1377  E8 54 CF FD FF                  call 0x14028e2d0
002B137C  83 F8 08                        cmp eax, 8
002B137F  0F 84 3B 06 00 00               je 0x1402b19c0
002B1385  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
002B138A  48 8D 44 24 70                  lea rax, [rsp + 0x70]
002B138F  41 B9 01 00 00 00               mov r9d, 1
002B1395  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002B139A  45 8B C6                        mov r8d, r14d
002B139D  48 8B D6                        mov rdx, rsi
002B13A0  E8 AB B0 FC FF                  call 0x14027c450
002B13A5  44 0F B6 4C 24 70               movzx r9d, byte ptr [rsp + 0x70]
002B13AB  45 8B C6                        mov r8d, r14d
002B13AE  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
002B13B3  49 8B D5                        mov rdx, r13
002B13B6  E8 15 84 08 00                  call 0x1403397d0
002B13BB  48 8B 4E 18                     mov rcx, qword ptr [rsi + 0x18]
002B13BF  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
002B13C9  4C 8B 06                        mov r8, qword ptr [rsi]
002B13CC  49 B9 00 00 00 00 00 FF FF FF   movabs r9, 0xffffff0000000000
002B13D6  4D 8B D0                        mov r10, r8
002B13D9  49 8B D0                        mov rdx, r8
002B13DC  4C 23 D0                        and r10, rax
002B13DF  48 8B D9                        mov rbx, rcx
002B13E2  48 23 D8                        and rbx, rax
002B13E5  49 BB FF FF FF FF 3F 00 00 00   movabs r11, 0x3fffffffff
002B13EF  49 8B 07                        mov rax, qword ptr [r15]
002B13F2  48 33 D0                        xor rdx, rax
002B13F5  49 23 D1                        and rdx, r9
002B13F8  49 33 D0                        xor rdx, r8
002B13FB  4D 8B C1                        mov r8, r9
002B13FE  49 89 17                        mov qword ptr [r15], rdx
002B1401  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
002B1405  48 33 C1                        xor rax, rcx
002B1408  49 23 C1                        and rax, r9
002B140B  48 33 C1                        xor rax, rcx
002B140E  49 89 47 18                     mov qword ptr [r15 + 0x18], rax
002B1412  4D 3B D3                        cmp r10, r11
002B1415  0F 84 86 03 00 00               je 0x1402b17a1
002B141B  4F 8D 0C 52                     lea r9, [r10 + r10*2]
002B141F  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002B1429  49 C1 E1 04                     shl r9, 4
002B142D  48 8B C0                        mov rax, rax
002B1430  4C 8B 5C 24 50                  mov r11, qword ptr [rsp + 0x50]
002B1435  4C 03 C8                        add r9, rax
002B1438  41 81 FB FF FF FF 00            cmp r11d, 0xffffff
002B143F  0F 85 D4 03 00 00               jne 0x1402b1819
002B1445  49 8B 51 18                     mov rdx, qword ptr [r9 + 0x18]
002B1449  48 8B CA                        mov rcx, rdx
002B144C  48 8B C2                        mov rax, rdx
002B144F  49 33 CD                        xor rcx, r13
002B1452  49 23 C8                        and rcx, r8
002B1455  49 33 CD                        xor rcx, r13
002B1458  F0 49 0F B1 49 18               lock cmpxchg qword ptr [r9 + 0x18], rcx
002B145E  4C 8B C0                        mov r8, rax
002B1461  48 3B D0                        cmp rdx, rax
002B1464  74 2C                           je 0x1402b1492
002B1466  49 BC 00 00 00 00 00 FF FF FF   movabs r12, 0xffffff0000000000
002B1470  49 8B C8                        mov rcx, r8
002B1473  4D 33 C5                        xor r8, r13
002B1476  4D 23 C4                        and r8, r12
002B1479  48 8B C1                        mov rax, rcx
002B147C  4D 33 C5                        xor r8, r13
002B147F  F0 4D 0F B1 41 18               lock cmpxchg qword ptr [r9 + 0x18], r8
002B1485  4C 8B C0                        mov r8, rax
002B1488  48 3B C8                        cmp rcx, rax
002B148B  75 E3                           jne 0x1402b1470
002B148D  44 8B 64 24 30                  mov r12d, dword ptr [rsp + 0x30]
002B1492  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
002B1497  49 B8 00 00 00 00 00 FF FF FF   movabs r8, 0xffffff0000000000
002B14A1  48 B8 FF FF FF FF 3F 00 00 00   movabs rax, 0x3fffffffff
002B14AB  48 3B D8                        cmp rbx, rax
002B14AE  0F 84 93 03 00 00               je 0x1402b1847
002B14B4  4C 8D 0C 5B                     lea r9, [rbx + rbx*2]
002B14B8  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
002B14C2  49 C1 E1 04                     shl r9, 4
002B14C6  48 8B C0                        mov rax, rax
002B14C9  4C 03 C8                        add r9, rax
002B14CC  41 81 FB FF FF FF 00            cmp r11d, 0xffffff
002B14D3  0F 85 E4 02 00 00               jne 0x1402b17bd
002B14D9  49 8B 01                        mov rax, qword ptr [r9]
002B14DC  49 33 C5                        xor rax, r13
002B14DF  49 23 C0                        and rax, r8
002B14E2  49 33 C5                        xor rax, r13
002B14E5  49 89 01                        mov qword ptr [r9], rax
002B14E8  41 81 FB FF FF FF 00            cmp r11d, 0xffffff
002B14EF  74 36                           je 0x1402b1527
002B14F1  41 83 FE 09                     cmp r14d, 9
002B14F5  7C 10                           jl 0x1402b1507
002B14F7  41 83 FC 09                     cmp r12d, 9
002B14FB  7D 0F                           jge 0x1402b150c
002B14FD  41 83 FE 09                     cmp r14d, 9
002B1501  0F 84 70 05 00 00               je 0x1402b1a77
002B1507  83 FF 04                        cmp edi, 4
002B150A  73 1B                           jae 0x1402b1527
002B150C  48 8D 44 24 70                  lea rax, [rsp + 0x70]
002B1511  45 8B CC                        mov r9d, r12d
002B1514  45 8B C6                        mov r8d, r14d
002B1517  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002B151C  49 8B D7                        mov rdx, r15
002B151F  48 8B CE                        mov rcx, rsi
002B1522  E8 49 7D 00 00                  call 0x1402b9270
002B1527  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
002B152C  41 83 FE 09                     cmp r14d, 9
002B1530  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
002B1535  75 1E                           jne 0x1402b1555
002B1537  41 B9 02 00 00 00               mov r9d, 2
002B153D  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
002B1546  48 8B D3                        mov rdx, rbx
002B1549  49 8B CE                        mov rcx, r14
002B154C  45 8D 41 01                     lea r8d, [r9 + 1]
002B1550  E8 2B DA 08 00                  call 0x14033ef80
002B1555  41 83 FC 09                     cmp r12d, 9
002B1559  75 1D                           jne 0x1402b1578
002B155B  41 B9 03 00 00 00               mov r9d, 3
002B1561  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
002B156A  45 8B C1                        mov r8d, r9d
002B156D  49 8B D5                        mov rdx, r13
002B1570  49 8B CE                        mov rcx, r14
002B1573  E8 08 DA 08 00                  call 0x14033ef80
002B1578  83 3D CD EB B7 00 01            cmp dword ptr [rip + 0xb7ebcd], 1
002B157F  0F 84 59 05 00 00               je 0x1402b1ade
002B1585  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
002B158A  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
002B158F  E8 BC FA FF FF                  call 0x1402b1050
002B1594  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
002B1597  49 B9 00 00 00 00 00 FF FF FF   movabs r9, 0xffffff0000000000
002B15A1  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
002B15A5  C1 E8 10                        shr eax, 0x10
002B15A8  24 FD                           and al, 0xfd
002B15AA  0C 05                           or al, 5
002B15AC  88 44 24 32                     mov byte ptr [rsp + 0x32], al
002B15B0  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
002B15B4  89 46 20                        mov dword ptr [rsi + 0x20], eax
002B15B7  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
002B15BB  49 23 C1                        and rax, r9
002B15BE  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
002B15C2  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
002B15C7  8B 0D B3 DA D1 00               mov ecx, dword ptr [rip + 0xd1dab3]
002B15CD  48 BA FF FF FF FF FF FF FF C7   movabs rdx, 0xc7ffffffffffffff
002B15D7  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
002B15DB  48 C1 E1 3B                     shl rcx, 0x3b
002B15DF  48 33 C1                        xor rax, rcx
002B15E2  48 23 C2                        and rax, rdx
002B15E5  48 BA FF FF FF FF FF 00 00 00   movabs rdx, 0xffffffffff
002B15EF  48 33 C1                        xor rax, rcx
002B15F2  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
002B15FC  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
002B1600  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
002B1604  48 23 C2                        and rax, rdx
002B1607  48 3B C3                        cmp rax, rbx
002B160A  0F 84 13 03 00 00               je 0x1402b1923
002B1610  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
002B1614  41 B8 00 00 00 80               mov r8d, 0x80000000
002B161A  48 23 CA                        and rcx, rdx
002B161D  83 CF 01                        or edi, 1
002B1620  33 D2                           xor edx, edx
002B1622  E8 E9 14 08 00                  call 0x140332b10
002B1627  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
002B162B  48 C1 E9 03                     shr rcx, 3
002B162F  81 E1 FF 01 00 00               and ecx, 0x1ff
002B1635  4C 8D 34 C8                     lea r14, [rax + rcx*8]
002B1639  49 8B CE                        mov rcx, r14
002B163C  E8 5F 12 FD FF                  call 0x1402828a0
002B1641  48 8B 0D 38 C6 B7 00            mov rcx, qword ptr [rip + 0xb7c638]
002B1648  48 85 C9                        test rcx, rcx
002B164B  74 0E                           je 0x1402b165b
002B164D  A8 10                           test al, 0x10
002B164F  0F 85 5F 01 00 00               jne 0x1402b17b4
002B1655  48 F7 D1                        not rcx
002B1658  48 23 C1                        and rax, rcx
002B165B  49 8B D5                        mov rdx, r13
002B165E  48 C1 E2 0C                     shl rdx, 0xc
002B1662  48 8B CA                        mov rcx, rdx
002B1665  48 33 C8                        xor rcx, rax
002B1668  48 B8 FF 0F 00 00 00 00 F0 FF   movabs rax, 0xfff0000000000fff
002B1672  48 23 C8                        and rcx, rax
002B1675  48 33 CA                        xor rcx, rdx
002B1678  E8 63 DF FD FF                  call 0x14028f5e0
002B167D  49 8B CE                        mov rcx, r14
002B1680  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
002B1685  48 8B D8                        mov rbx, rax
002B1688  45 33 E4                        xor r12d, r12d
002B168B  E8 70 E4 F8 FF                  call 0x14023fb00
002B1690  85 C0                           test eax, eax
002B1692  0F 85 B8 03 00 00               jne 0x1402b1a50
002B1698  49 89 1E                        mov qword ptr [r14], rbx
002B169B  45 85 E4                        test r12d, r12d
002B169E  0F 85 C3 03 00 00               jne 0x1402b1a67
002B16A4  40 F6 C7 01                     test dil, 1
002B16A8  74 50                           je 0x1402b16fa
002B16AA  49 C1 EE 09                     shr r14, 9
002B16AE  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002B16B8  4C 23 F0                        and r14, rax
002B16BB  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002B16C5  4C 03 F0                        add r14, rax
002B16C8  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
002B16D1  48 8B 88 38 88 00 00            mov rcx, qword ptr [rax + 0x8838]
002B16D8  48 8B 05 A1 F1 D5 FF            mov rax, qword ptr [rip - 0x2a0e5f]
002B16DF  48 C7 01 00 00 00 00            mov qword ptr [rcx], 0
002B16E6  49 89 06                        mov qword ptr [r14], rax
002B16E9  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
002B16F3  4C 8B 76 08                     mov r14, qword ptr [rsi + 8]
002B16F7  4C 0B F0                        or r14, rax
002B16FA  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
002B16FE  48 85 C0                        test rax, rax
002B1701  0F 89 C8 01 00 00               jns 0x1402b18cf
002B1707  83 FF 04                        cmp edi, 4
002B170A  0F 83 06 04 00 00               jae 0x1402b1b16
002B1710  F6 44 24 40 02                  test byte ptr [rsp + 0x40], 2
002B1715  75 0F                           jne 0x1402b1726
002B1717  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
002B1721  F0 49 21 47 18                  lock and qword ptr [r15 + 0x18], rax
002B1726  40 F6 C7 02                     test dil, 2
002B172A  0F 85 FF 01 00 00               jne 0x1402b192f
002B1730  48 8B 56 28                     mov rdx, qword ptr [rsi + 0x28]
002B1734  49 B9 FF FF FF FF FF FF FF 8F   movabs r9, 0x8fffffffffffffff
002B173E  48 8B CA                        mov rcx, rdx
002B1741  48 8B C2                        mov rax, rdx
002B1744  49 23 C9                        and rcx, r9
002B1747  F0 48 0F B1 4E 28               lock cmpxchg qword ptr [rsi + 0x28], rcx
002B174D  4C 8B C0                        mov r8, rax
002B1750  48 3B D0                        cmp rdx, rax
002B1753  74 17                           je 0x1402b176c
002B1755  49 8B D0                        mov rdx, r8
002B1758  4D 23 C1                        and r8, r9
002B175B  48 8B C2                        mov rax, rdx
002B175E  F0 4C 0F B1 46 28               lock cmpxchg qword ptr [rsi + 0x28], r8
002B1764  4C 8B C0                        mov r8, rax
002B1767  48 3B D0                        cmp rdx, rax
002B176A  75 E9                           jne 0x1402b1755
002B176C  48 8B CE                        mov rcx, rsi
002B176F  E8 7C 42 0C 00                  call 0x1403759f0
002B1774  B8 01 00 00 00                  mov eax, 1
002B1779  E9 E7 00 00 00                  jmp 0x1402b1865
002B177E  66 90                           nop
002B1780  41 FF C4                        inc r12d
002B1783  44 85 25 22 3B D1 00            test dword ptr [rip + 0xd13b22], r12d
002B178A  0F 84 D0 01 00 00               je 0x1402b1960
002B1790  F3 90                           pause
002B1792  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
002B1796  48 85 C0                        test rax, rax
002B1799  0F 89 4C FA FF FF               jns 0x1402b11eb
002B179F  EB DF                           jmp 0x1402b1780
002B17A1  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
002B17A6  4C 8B 5C 24 50                  mov r11, qword ptr [rsp + 0x50]
002B17AB  4D 89 6A 18                     mov qword ptr [r10 + 0x18], r13
002B17AF  E9 ED FC FF FF                  jmp 0x1402b14a1
002B17B4  48 83 E0 EF                     and rax, 0xffffffffffffffef
002B17B8  E9 9E FE FF FF                  jmp 0x1402b165b
002B17BD  83 FF 02                        cmp edi, 2
002B17C0  0F 85 13 FD FF FF               jne 0x1402b14d9
002B17C6  48 8B CB                        mov rcx, rbx
002B17C9  E8 72 7A 00 00                  call 0x1402b9240
002B17CE  85 C0                           test eax, eax
002B17D0  0F 84 03 FD FF FF               je 0x1402b14d9
002B17D6  49 8B 49 10                     mov rcx, qword ptr [r9 + 0x10]
002B17DA  49 8B D5                        mov rdx, r13
002B17DD  E8 FA 46 0D 00                  call 0x140385edc
002B17E2  49 89 41 10                     mov qword ptr [r9 + 0x10], rax
002B17E6  E9 06 FD FF FF                  jmp 0x1402b14f1
002B17EB  83 F8 03                        cmp eax, 3
002B17EE  0F 84 A5 00 00 00               je 0x1402b1899
002B17F4  48 8D 44 24 70                  lea rax, [rsp + 0x70]
002B17F9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002B17FE  41 B9 01 00 00 00               mov r9d, 1
002B1804  45 8B C6                        mov r8d, r14d
002B1807  48 8B D6                        mov rdx, rsi
002B180A  E8 41 AC FC FF                  call 0x14027c450
002B180F  44 8B 64 24 30                  mov r12d, dword ptr [rsp + 0x30]
002B1814  E9 A2 FB FF FF                  jmp 0x1402b13bb
002B1819  83 FF 02                        cmp edi, 2
002B181C  0F 85 23 FC FF FF               jne 0x1402b1445
002B1822  49 8B CA                        mov rcx, r10
002B1825  E8 16 7A 00 00                  call 0x1402b9240
002B182A  85 C0                           test eax, eax
002B182C  0F 84 13 FC FF FF               je 0x1402b1445
002B1832  49 8B D5                        mov rdx, r13
002B1835  49 8B C9                        mov rcx, r9
002B1838  E8 83 27 0B 00                  call 0x140363fc0
002B183D  4C 8B 5C 24 50                  mov r11, qword ptr [rsp + 0x50]
002B1842  E9 4B FC FF FF                  jmp 0x1402b1492
002B1847  4D 89 6A 10                     mov qword ptr [r10 + 0x10], r13
002B184B  E9 98 FC FF FF                  jmp 0x1402b14e8
002B1850  85 C9                           test ecx, ecx
002B1852  75 0F                           jne 0x1402b1863
002B1854  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
002B185E  F0 49 21 47 18                  lock and qword ptr [r15 + 0x18], rax
002B1863  33 C0                           xor eax, eax
002B1865  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
002B186D  48 33 CC                        xor rcx, rsp
002B1870  E8 CB AD 3F 00                  call 0x1406ac640
002B1875  48 81 C4 F0 00 00 00            add rsp, 0xf0
002B187C  41 5F                           pop r15
002B187E  41 5E                           pop r14
002B1880  41 5D                           pop r13
002B1882  41 5C                           pop r12
002B1884  5F                              pop rdi
002B1885  5E                              pop rsi
002B1886  5B                              pop rbx
002B1887  C3                              ret
002B1888  CC                              int3
002B1889  49 8B D5                        mov rdx, r13
002B188C  49 8B CF                        mov rcx, r15
002B188F  E8 2C 27 0B 00                  call 0x140363fc0
002B1894  E9 10 FA FF FF                  jmp 0x1402b12a9
002B1899  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
002B189D  48 0F BA E0 0A                  bt rax, 0xa
002B18A2  0F 82 A3 00 00 00               jb 0x1402b194b
002B18A8  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
002B18AD  45 33 C0                        xor r8d, r8d
002B18B0  49 8B CF                        mov rcx, r15
002B18B3  E8 48 92 00 00                  call 0x1402bab00
002B18B8  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
002B18BD  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002B18C2  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
002B18C7  48 8B C8                        mov rcx, rax
002B18CA  E9 2F FF FF FF                  jmp 0x1402b17fe
002B18CF  49 8B CE                        mov rcx, r14
002B18D2  E8 A9 D3 FD FF                  call 0x14028ec80
002B18D7  83 F8 04                        cmp eax, 4
002B18DA  0F 85 27 FE FF FF               jne 0x1402b1707
002B18E0  49 C1 E5 0C                     shl r13, 0xc
002B18E4  49 8B C5                        mov rax, r13
002B18E7  48 83 C8 02                     or rax, 2
002B18EB  80 3D 95 51 D1 00 00            cmp byte ptr [rip + 0xd15195], 0
002B18F2  49 0F 44 C5                     cmove rax, r13
002B18F6  49 89 86 00 FD FF FF            mov qword ptr [r14 - 0x300], rax
002B18FD  E9 05 FE FF FF                  jmp 0x1402b1707
002B1902  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
002B1905  48 0F BA E0 0A                  bt rax, 0xa
002B190A  0F 83 09 F9 FF FF               jae 0x1402b1219
002B1910  44 0F B6 66 24                  movzx r12d, byte ptr [rsi + 0x24]
002B1915  41 0F B6 C4                     movzx eax, r12b
002B1919  24 F0                           and al, 0xf0
002B191B  88 46 24                        mov byte ptr [rsi + 0x24], al
002B191E  E9 FB F8 FF FF                  jmp 0x1402b121e
002B1923  4C 8B 76 08                     mov r14, qword ptr [rsi + 8]
002B1927  4C 0B F1                        or r14, rcx
002B192A  E9 0A FD FF FF                  jmp 0x1402b1639
002B192F  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
002B1932  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
002B1936  C1 E8 18                        shr eax, 0x18
002B1939  24 F7                           and al, 0xf7
002B193B  88 44 24 43                     mov byte ptr [rsp + 0x43], al
002B193F  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
002B1943  89 46 20                        mov dword ptr [rsi + 0x20], eax
002B1946  E9 E5 FD FF FF                  jmp 0x1402b1730
002B194B  41 8B C4                        mov eax, r12d
002B194E  48 83 C0 40                     add rax, 0x40
002B1952  48 6B C0 58                     imul rax, rax, 0x58
002B1956  48 03 44 24 48                  add rax, qword ptr [rsp + 0x48]
002B195B  E9 58 FF FF FF                  jmp 0x1402b18b8
002B1960  8B 05 52 51 D1 00               mov eax, dword ptr [rip + 0xd15152]
002B1966  A8 40                           test al, 0x40
002B1968  0F 84 22 FE FF FF               je 0x1402b1790
002B196E  E8 1D DB 05 00                  call 0x14030f490
002B1973  84 C0                           test al, al
002B1975  0F 84 15 FE FF FF               je 0x1402b1790
002B197B  41 8B CC                        mov ecx, r12d
002B197E  E8 DD DA 05 00                  call 0x14030f460
002B1983  E9 0A FE FF FF                  jmp 0x1402b1792
002B1988  8B 46 20                        mov eax, dword ptr [rsi + 0x20]
002B198B  C1 E8 18                        shr eax, 0x18
002B198E  A8 08                           test al, 8
002B1990  0F 84 1F 01 00 00               je 0x1402b1ab5
002B1996  33 D2                           xor edx, edx
002B1998  E8 F3 5B FD FF                  call 0x140287590
002B199D  41 8B 47 20                     mov eax, dword ptr [r15 + 0x20]
002B19A1  BF 04 00 00 00                  mov edi, 4
002B19A6  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
002B19AA  C1 E8 18                        shr eax, 0x18
002B19AD  24 F7                           and al, 0xf7
002B19AF  88 44 24 33                     mov byte ptr [rsp + 0x33], al
002B19B3  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
002B19B7  41 89 47 20                     mov dword ptr [r15 + 0x20], eax
002B19BB  E9 D4 FB FF FF                  jmp 0x1402b1594
002B19C0  49 B9 00 00 00 00 00 DE FF FF   movabs r9, 0xffffde0000000000
002B19CA  49 8B C1                        mov rax, r9
002B19CD  48 8B 15 6C B8 B8 00            mov rdx, qword ptr [rip + 0xb8b86c]
002B19D4  48 8B CE                        mov rcx, rsi
002B19D7  48 2B C8                        sub rcx, rax
002B19DA  49 BA AB AA AA AA AA AA AA AA   movabs r10, 0xaaaaaaaaaaaaaaab
002B19E4  48 C1 F9 04                     sar rcx, 4
002B19E8  49 0F AF CA                     imul rcx, r10
002B19EC  48 C1 E9 09                     shr rcx, 9
002B19F0  44 0F B6 44 4A 01               movzx r8d, byte ptr [rdx + rcx*2 + 1]
002B19F6  41 80 E0 7F                     and r8b, 0x7f
002B19FA  49 8B C1                        mov rax, r9
002B19FD  49 8B CF                        mov rcx, r15
002B1A00  48 2B C8                        sub rcx, rax
002B1A03  48 C1 F9 04                     sar rcx, 4
002B1A07  49 0F AF CA                     imul rcx, r10
002B1A0B  48 C1 E9 09                     shr rcx, 9
002B1A0F  0F B6 44 4A 01                  movzx eax, byte ptr [rdx + rcx*2 + 1]
002B1A14  24 7F                           and al, 0x7f
002B1A16  44 3A C0                        cmp r8b, al
002B1A19  0F 84 66 F9 FF FF               je 0x1402b1385
002B1A1F  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
002B1A24  48 83 C1 20                     add rcx, 0x20
002B1A28  E8 53 74 F9 FF                  call 0x140248e80
002B1A2D  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
002B1A32  45 33 C9                        xor r9d, r9d
002B1A35  45 8B C6                        mov r8d, r14d
002B1A38  49 8D 51 FF                     lea rdx, [r9 - 1]
002B1A3C  E8 8F 7D 08 00                  call 0x1403397d0
002B1A41  33 D2                           xor edx, edx
002B1A43  49 8B CD                        mov rcx, r13
002B1A46  E8 D5 BB 16 00                  call 0x14041d620
002B1A4B  E9 6B F9 FF FF                  jmp 0x1402b13bb
002B1A50  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
002B1A55  E8 0E 31 FE FF                  call 0x140294b68
002B1A5A  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
002B1A5F  44 8B E0                        mov r12d, eax
002B1A62  E9 31 FC FF FF                  jmp 0x1402b1698
002B1A67  48 8B D3                        mov rdx, rbx
002B1A6A  49 8B CE                        mov rcx, r14
002B1A6D  E8 3A 34 FE FF                  call 0x140294eac
002B1A72  E9 2D FC FF FF                  jmp 0x1402b16a4
002B1A77  F0 49 FF 0A                     lock dec qword ptr [r10]
002B1A7B  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
002B1A7F  48 85 C0                        test rax, rax
002B1A82  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
002B1A87  79 24                           jns 0x1402b1aad
002B1A89  48 05 40 1C 00 00               add rax, 0x1c40
002B1A8F  F0 48 FF 08                     lock dec qword ptr [rax]
002B1A93  45 33 C9                        xor r9d, r9d
002B1A96  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
002B1A9B  41 8D 51 01                     lea edx, [r9 + 1]
002B1A9F  4D 8D 41 FF                     lea r8, [r9 - 1]
002B1AA3  E8 C8 9A 10 00                  call 0x1403bb570
002B1AA8  E9 5A FA FF FF                  jmp 0x1402b1507
002B1AAD  48 05 C0 3F 00 00               add rax, 0x3fc0
002B1AB3  EB DA                           jmp 0x1402b1a8f
002B1AB5  E8 36 0C 07 00                  call 0x1403226f0
002B1ABA  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
002B1ABF  8B C0                           mov eax, eax
002B1AC1  48 81 C1 C0 0C 00 00            add rcx, 0xcc0
002B1AC8  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
002B1ACD  48 6B C0 58                     imul rax, rax, 0x58
002B1AD1  48 03 C1                        add rax, rcx
002B1AD4  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002B1AD9  E9 6E F8 FF FF                  jmp 0x1402b134c
002B1ADE  48 8B 05 C3 E6 B7 00            mov rax, qword ptr [rip + 0xb7e6c3]
002B1AE5  4C 8B CB                        mov r9, rbx
002B1AE8  41 83 E1 1F                     and r9d, 0x1f
002B1AEC  48 8B CB                        mov rcx, rbx
002B1AEF  48 C1 E9 05                     shr rcx, 5
002B1AF3  BA 01 00 00 00                  mov edx, 1
002B1AF8  4C 8D 04 88                     lea r8, [rax + rcx*4]
002B1AFC  49 8D 41 01                     lea rax, [r9 + 1]
002B1B00  48 83 F8 20                     cmp rax, 0x20
002B1B04  0F 87 CE 9A 42 00               ja 0x1406db5d8
002B1B0A  41 8B C9                        mov ecx, r9d
002B1B0D  8B C2                           mov eax, edx
002B1B0F  D3 E0                           shl eax, cl
002B1B11  E9 2F 9B 42 00                  jmp 0x1406db645
002B1B16  BA 00 08 00 00                  mov edx, 0x800
002B1B1B  49 8B CF                        mov rcx, r15
002B1B1E  E8 DD 84 00 00                  call 0x1402ba000
002B1B23  E9 E8 FB FF FF                  jmp 0x1402b1710
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReplaceTransitionPage(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m128;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int8 v_stack_mF6;
    unsigned int v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned __int8 v_stack_p33;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int8 v_stack_p43;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p70;

    v_rsp = (v_rsp) - (240);
    result = (*(unsigned __int64 *)(v_rip + 11900422)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_mE8 = (unsigned int)((unsigned int)(a4));
    v_rdi = 0;
    a2 = 0;
    result = memset(v_stack_mB8, a2, v_rdi + 104, a4);
    v_stack_mD8 = (unsigned int)(0xFFFFFFULL);
    a1 = (a1) - (0);
    a1 = (a1) >> (4);
    a1 = (a1) * (v_rdi + 104);
    v_stack_mD0 = a1;
    v_r13 = (0) - (0);
    result = (*(unsigned __int64 *)(a1 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_r13 = (v_r13) >> (4);
    v_r13 = (v_r13) * (v_rdi + 104);
    result = (unsigned int)((*(unsigned __int8 *)(a1 + 34)) & (7));
    v_stack_mE0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12054233) + result * 8);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (2));
    v_stack_mF0 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12054233) + result * 8) + result * 8 + 7136);
    v_stack_mF8 = (unsigned int)(a1);
    if (condition_is_not_equal) goto loc_002B11FC;
    v_r12 = 0;
loc_002B11EB:
    if (condition_is_below) goto loc_002B1780;
loc_002B11FC:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (64)) != 0) goto loc_002B1850;
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 34)) & (7));
    if (((unsigned __int8)(result)) == 3) goto loc_002B1902;
loc_002B1219:
loc_002B121E:
    v_r12 = (unsigned int)((*(unsigned __int8 *)(a2 + 36)) & (15));
    result = MiGetPfnSlabType(0, a2, v_rdi + 104, a4);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (16));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 32))) >> (16));
    a3 = (unsigned int)(((unsigned __int8)(a1)) >> (6));
    a2 = (unsigned int)(((unsigned __int8)(a1)) >> (6));
    v_stack_mF8 = (unsigned int)(result);
    if (a3 != ((unsigned int)(a2))) {
        a3 = 1;
        a1 = a2;
        result = MiChangePageAttribute(a1, a2, a3, a4);
    }
    result = (*(unsigned __int64 *)(a2 + 24)) & (a1);
    *(unsigned __int64 *)(a2 + 24) = result;
    result = MiCopyPfnEntryEx(a2, a1, a3, a4);
    result = (unsigned __int8)((*(unsigned __int8 *)(a2 + 36)) & (240));
    result = (unsigned __int8)((result) | ((unsigned __int8)(v_r12)));
    *(unsigned __int8 *)(a2 + 36) = (unsigned __int8)(result);
    result = (*(unsigned __int64 *)(a1 + 40)) & (a2);
    if (result == v_stack_mD0) goto loc_002B1889;
loc_002B12A9:
    result = MiCopyPage(v_r13, v_stack_mD0, 6, a4);
    a2 = ((unsigned int)(*(unsigned int *)(v_rip + 13753788))) << (59);
    a1 = (a2) ^ (*(unsigned __int64 *)(a2 + 24));
    a1 = (a1) & (*(unsigned __int64 *)(a2 + 24));
    a1 = (a1) ^ (a2);
    *(unsigned __int64 *)(a2 + 24) = a1;
    if (((v_stack_mE8) & (1)) != 0) goto loc_002B1594;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mF0 + 12)))) != 2) goto loc_002B17EB;
    if (((unsigned int)((unsigned int)(a3))) < 9) goto loc_002B1988;
    result = MiGetPfnPriority(a1, a2, 6, a4);
    v_r12 = (v_stack_mE0) + (0xCC0ULL);
    a2 = (a2) * ((unsigned int)((unsigned int)(result)));
    v_stack_mD8 = result;
    v_r12 = (v_r12) + (a2);
    v_stack_mF0 = v_r12;
    if (((unsigned int)((unsigned int)(a3))) == 9) {
        a1 = *(unsigned int *)(a1 + 32);
        a1 = (unsigned int)((a1) >> (24));
        if ((((unsigned __int8)(a1)) & (8)) != 0) { v_rdi = 2; }
    }
    result = MI_NODE_FROM_PFN(a1, a2, 6, a4);
    result = MI_NODE_FROM_PFN(a2, a2, 6, a4);
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)(result))) goto loc_002B1A1F;
    if (((unsigned int)((unsigned int)(a3))) != ((unsigned int)((unsigned int)(v_stack_mF8)))) goto loc_002B1A1F;
    result = MiGetPfnSlabType(a1, a2, 6, a4);
    if (((unsigned int)(result)) == 8) goto loc_002B19C0;
loc_002B1385:
    v_stack_m108 = v_stack_mB8;
    result = MiAcquirePageListLock(v_stack_mF0, a1, (unsigned int)((unsigned int)((unsigned int)(a3))), 1);
    result = MiReplaceStandbyLookaside(v_stack_mD0, v_r13, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_mB8);
loc_002B13BB:
    v_r10 = (*(unsigned __int64 *)(a1)) & (result);
    v_rbx = (*(unsigned __int64 *)(a1 + 24)) & (result);
    a2 = (*(unsigned __int64 *)(a1)) ^ (*(unsigned __int64 *)(a2));
    a2 = (a2) & (v_stack_mB8);
    a2 = (a2) ^ (*(unsigned __int64 *)(a1));
    *(unsigned __int64 *)(a2) = a2;
    result = (*(unsigned __int64 *)(a2 + 24)) ^ (*(unsigned __int64 *)(a1 + 24));
    result = (result) & (v_stack_mB8);
    result = (result) ^ (*(unsigned __int64 *)(a1 + 24));
    *(unsigned __int64 *)(a2 + 24) = result;
    if (v_r10 == v_r11) goto loc_002B17A1;
    a4 = (v_r10 + v_r10 * 2) << (4);
    a4 = (a4) + (result);
    if (((unsigned int)(v_stack_mD8)) != 0xFFFFFFULL) goto loc_002B1819;
loc_002B1445:
    a1 = (*(unsigned __int64 *)(a4 + 24)) ^ (v_r13);
    a1 = (a1) & (v_stack_mB8);
    a1 = (a1) ^ (v_r13);
    if ((*(unsigned __int64 *)(a4 + 24)) == (*(unsigned __int64 *)(a4 + 24))) goto loc_002B1492;
loc_002B1470:
    a3 = (*(unsigned __int64 *)(a4 + 24)) ^ (v_r13);
    a3 = (a3) & ((unsigned int)(v_stack_mF8));
    a3 = (a3) ^ (v_r13);
    if ((*(unsigned __int64 *)(a4 + 24)) != (*(unsigned __int64 *)(a4 + 24))) goto loc_002B1470;
loc_002B1492:
loc_002B14A1:
    if (v_rbx == (*(unsigned __int64 *)(a4 + 24))) goto loc_002B1847;
    a4 = (v_rbx + v_rbx * 2) << (4);
    a4 = (a4) + (*(unsigned __int64 *)(a4 + 24));
    if (((unsigned int)(v_stack_mD8)) != 0xFFFFFFULL) goto loc_002B17BD;
loc_002B14D9:
    result = (*(unsigned __int64 *)(a4)) ^ (v_r13);
    result = (result) & (*(unsigned __int64 *)(a4 + 24));
    result = (result) ^ (v_r13);
    *(unsigned __int64 *)(a4) = result;
loc_002B14E8:
    if (((unsigned int)(v_stack_mD8)) == 0xFFFFFFULL) goto loc_002B1527;
loc_002B14F1:
    if (((unsigned int)((unsigned int)(a3))) < 9) goto loc_002B1507;
    if (((unsigned int)((unsigned int)(v_stack_mF8))) >= 9) goto loc_002B150C;
    if (((unsigned int)((unsigned int)(a3))) == 9) goto loc_002B1A77;
loc_002B1507:
    if (((unsigned int)(v_rdi)) < 4) {
        result = v_stack_mB8;
        a4 = (unsigned int)((unsigned int)(v_stack_mF8));
        a3 = (unsigned int)((unsigned int)(a3));
        v_stack_m108 = result;
        a2 = a2;
        a1 = a1;
        result = MiReplaceSecondaryListStandbyPage(a1, a2, a3, a4);
    }
    if (((unsigned int)((unsigned int)(a3))) == 9) {
        a4 = 2;
        v_stack_m108 = 0;
        a2 = v_stack_mD0;
        a1 = v_stack_mE0;
        a3 = a4 + 1;
        result = MiUpdateLargePageCandidateValue(a1, a2, a3, a4);
    }
    if (((unsigned int)((unsigned int)(v_stack_mF8))) == 9) {
        a4 = 3;
        v_stack_m108 = 0;
        a3 = a4;
        a2 = v_r13;
        a1 = v_stack_mE0;
        result = MiUpdateLargePageCandidateValue(a1, a2, a3, a4);
    }
    if ((*(unsigned int *)(v_rip + 12053453)) == 1) goto loc_002B1ADE;
    result = MiReleasePageListLock(v_stack_mF0, v_stack_mB8, a3, a4);
loc_002B1594:
    v_stack_mF8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (16));
    result = (unsigned __int8)((result) & (253));
    result = (unsigned __int8)((result) | (5));
    v_stack_mF6 = (unsigned __int8)(result);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_mF8));
    result = (*(unsigned __int64 *)(a1 + 24)) & (a4);
    *(unsigned __int64 *)(a1 + 24) = result;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip + 13753011))) << (59);
    result = (*(unsigned __int64 *)(a1 + 24)) ^ (a1);
    result = (result) & (v_stack_mB8);
    result = (result) ^ (a1);
    *(unsigned __int64 *)(a1 + 24) = result;
    result = (*(unsigned __int64 *)(a1 + 40)) & (v_stack_mB8);
    if (result == v_stack_mD0) goto loc_002B1923;
    a1 = (*(unsigned __int64 *)(a1 + 40)) & (v_stack_mB8);
    v_rdi = (unsigned int)((v_rdi) | (1));
    a2 = 0;
    result = MiMapPageInHyperSpaceWorker(a1, a2, (unsigned int)(0x80000000ULL), a4);
    a1 = (*(unsigned __int64 *)(a1 + 8)) >> (3);
    a1 = (unsigned int)((a1) & (511));
loc_002B1639:
    result = MI_READ_PTE_LOCK_FREE(result + a1 * 8, a2, (unsigned int)(0x80000000ULL), a4);
    if (*(unsigned __int64 *)(v_rip + 12043832) == 0) goto loc_002B165B;
    if ((((unsigned __int8)(result)) & (16)) != 0) goto loc_002B17B4;
    a1 = ~(*(unsigned __int64 *)(v_rip + 12043832));
    result = (result) & (a1);
loc_002B165B:
    a2 = (v_r13) << (12);
    a1 = (a2) ^ (result);
    a1 = (a1) & (result);
    a1 = (a1) ^ (a2);
    result = MiSwizzleInvalidPte(a1, a2, (unsigned int)(0x80000000ULL), a4);
    v_stack_mC8 = result;
    v_r12 = 0;
    result = MiPteInShadowRange(result + a1 * 8, a2, (unsigned int)(0x80000000ULL), a4);
    if ((unsigned int)(result) != 0) goto loc_002B1A50;
loc_002B1698:
    *(unsigned __int64 *)(result + a1 * 8) = result;
    if (0 != 0) goto loc_002B1A67;
loc_002B16A4:
    v_r14 = result + a1 * 8;
    if ((((unsigned __int8)(v_rdi)) & (1)) != 0) {
        v_r14 = (result + a1 * 8) >> (9);
        v_r14 = (v_r14) & (result);
        v_r14 = (v_r14) + (result);
        result = *(unsigned __int64 *)(gs_base + (0 + 32));
        a1 = *(unsigned __int64 *)(result + 34872);
        result = *(unsigned __int64 *)(v_rip - 2756191);
        *(unsigned __int64 *)(a1) = 0;
        *(unsigned __int64 *)(v_r14) = result;
        v_r14 = *(unsigned __int64 *)(a1 + 8);
        v_r14 = (v_r14) | (result);
    }
    if (!sign_flag) goto loc_002B18CF;
loc_002B1707:
    if (((unsigned int)(v_rdi)) >= 4) goto loc_002B1B16;
loc_002B1710:
    if (((v_stack_mE8) & (2)) == 0) {
    }
    if ((((unsigned __int8)(v_rdi)) & (2)) != 0) goto loc_002B192F;
loc_002B1730:
    a1 = (*(unsigned __int64 *)(a1 + 40)) & (a4);
    if ((*(unsigned __int64 *)(a1 + 40)) == (*(unsigned __int64 *)(a1 + 40))) goto loc_002B176C;
loc_002B1755:
    a3 = (*(unsigned __int64 *)(a1 + 40)) & (a4);
    if ((*(unsigned __int64 *)(a1 + 40)) != (*(unsigned __int64 *)(a1 + 40))) goto loc_002B1755;
loc_002B176C:
    result = MiClearPfnReuseFields(a1, *(unsigned __int64 *)(a1 + 40), *(unsigned __int64 *)(a1 + 40), a4);
    goto loc_002B1865;
loc_002B1780:
    v_r12 = (unsigned int)((v_r12) + 1);
    if (((*(unsigned int *)(v_rip + 13712162)) & ((unsigned int)(v_r12))) == 0) goto loc_002B1960;
loc_002B1790:
loc_002B1792:
    if (!sign_flag) goto loc_002B11EB;
    goto loc_002B1780;
loc_002B17A1:
    *(unsigned __int64 *)(v_stack_mF0 + 24) = v_r13;
    goto loc_002B14A1;
loc_002B17B4:
    result = (*(unsigned __int64 *)(a2 + 24)) & (-17);
    goto loc_002B165B;
loc_002B17BD:
    if (((unsigned int)(v_rdi)) != 2) goto loc_002B14D9;
    result = MiIsDecayPfn(result, *(unsigned __int64 *)(a1 + 40), *(unsigned __int64 *)(a1 + 40), a4);
    if ((unsigned int)(result) == 0) goto loc_002B14D9;
    result = MiUpdateTransitionPteFrame(*(unsigned __int64 *)(a4 + 16), v_r13, *(unsigned __int64 *)(a1 + 40), a4);
    *(unsigned __int64 *)(a4 + 16) = result;
    goto loc_002B14F1;
loc_002B17EB:
    if (((unsigned int)(result)) == 3) goto loc_002B1899;
    v_stack_m108 = v_stack_mB8;
loc_002B17FE:
    result = MiAcquirePageListLock(*(unsigned __int64 *)(a4 + 16), a1, (unsigned int)((unsigned int)(v_r14)), 1);
    goto loc_002B13BB;
loc_002B1819:
    if (((unsigned int)(v_rdi)) != 2) goto loc_002B1445;
    result = MiIsDecayPfn(v_stack_mF0, a1, (unsigned int)((unsigned int)(v_r14)), 1);
    if ((unsigned int)(result) == 0) goto loc_002B1445;
    result = MiSetPfnContainingFrame(1, v_r13, (unsigned int)((unsigned int)(v_r14)), 1);
    goto loc_002B1492;
loc_002B1847:
    *(unsigned __int64 *)(v_stack_mF0 + 16) = v_r13;
    goto loc_002B14E8;
loc_002B1850:
    if (1 == 0) {
    }
    result = 0;
loc_002B1865:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_r13, (unsigned int)((unsigned int)(v_r14)), 1);
    v_rsp = (v_rsp) + (240);
    return result;
loc_002B1889:
    result = MiSetPfnContainingFrame(a2, v_r13, (unsigned int)((unsigned int)(v_r14)), 1);
    goto loc_002B12A9;
loc_002B1899:
    if (condition_is_below) goto loc_002B194B;
    a3 = 0;
    result = MiDetermineModifiedPageListHead(a2, v_stack_p48, a3, 1);
loc_002B18B8:
    v_stack_p38 = result;
    v_stack_p20 = v_stack_p70;
    goto loc_002B17FE;
loc_002B18CF:
    result = MiGetSystemRegionType(v_r14, v_stack_p48, a3, 1);
    if (((unsigned int)(result)) != 4) goto loc_002B1707;
    v_r13 = (v_r13) << (12);
    result = (v_r13) | (2);
    if ((*(unsigned __int8 *)(v_rip + 13717909)) == 0) { result = v_r13; }
    *(unsigned __int64 *)(v_r14 - 768) = result;
    goto loc_002B1707;
loc_002B1902:
    if ((*(unsigned __int8 *)(v_rip + 13717909)) >= 0) goto loc_002B1219;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(a1 + 36))) & (240));
    *(unsigned __int8 *)(a1 + 36) = (unsigned __int8)(result);
    goto loc_002B121E;
loc_002B1923:
    v_r14 = (*(unsigned __int64 *)(a1 + 8)) | (v_r14);
    goto loc_002B1639;
loc_002B192F:
    v_stack_p40 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (24));
    result = (unsigned __int8)((result) & (247));
    v_stack_p43 = (unsigned __int8)(result);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_p40));
    goto loc_002B1730;
loc_002B194B:
    result = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 36)))) + (64);
    result = (result) * (result);
    result = (result) + (v_stack_p48);
    goto loc_002B18B8;
loc_002B1960:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13717842)))) & (64)) == 0) goto loc_002B1790;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_r14, v_stack_p48, a3, 1);
    if ((unsigned __int8)(result) == 0) goto loc_002B1790;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 36))), v_stack_p48, a3, 1);
    goto loc_002B1792;
loc_002B1988:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (8)) == 0) goto loc_002B1AB5;
    a2 = 0;
    result = MiUnlinkPageFromListEx((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 36))), a2, a3, 1);
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 32))) >> (24));
    result = (unsigned __int8)((result) & (247));
    v_stack_p33 = (unsigned __int8)(result);
    *(unsigned int *)(a2 + 32) = (unsigned int)((unsigned int)(v_stack_p30));
    goto loc_002B1594;
loc_002B19C0:
    a1 = (a1) - (1);
    a1 = (a1) >> (4);
    a1 = (a1) * (v_stack_mF0);
    a1 = (a1) >> (9);
    a3 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12105836) + a1 * 2 + 1)) & (127));
    a1 = (0) - (1);
    a1 = (a1) >> (4);
    a1 = (a1) * (v_stack_mF0);
    a1 = (a1) >> (9);
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12105836) + a1 * 2 + 1)) & (127));
    if (((unsigned __int8)(a3)) == ((unsigned __int8)(result))) goto loc_002B1385;
loc_002B1A1F:
    a1 = (v_stack_p38) + (32);
    result = ExAcquireSpinLockExclusiveAtDpcLevel(a1, *(unsigned __int64 *)(v_rip + 12105836), a3, 1);
    a4 = 0;
    result = MiReplaceStandbyLookaside(v_stack_p58, a4 - 1, (unsigned int)((unsigned int)(v_r14)), a4);
    a2 = 0;
    result = MiSetStandbyLookasideState(v_r13, a2, (unsigned int)((unsigned int)(v_r14)), a4);
    goto loc_002B13BB;
loc_002B1A50:
    result = MiSanitizeShadowPxe(v_r13, v_stack_p60, (unsigned int)((unsigned int)(v_r14)), a4);
    goto loc_002B1698;
loc_002B1A67:
    result = MiWritePteShadow(v_r14, v_stack_p60, (unsigned int)((unsigned int)(v_r14)), a4);
    goto loc_002B16A4;
loc_002B1A77:
    if (!sign_flag) goto loc_002B1AAD;
    result = (v_stack_p48) + (0x1C40ULL);
loc_002B1A8F:
    a4 = 0;
    result = MiDecreaseAvailablePages(v_stack_p48, a4 + 1, a4 - 1, a4);
    goto loc_002B1507;
loc_002B1AAD:
    result = (result) + (0x3FC0ULL);
    goto loc_002B1A8F;
loc_002B1AB5:
    result = MiGetPfnPriority(v_stack_p48, a4 + 1, a4 - 1, a4);
    a1 = (v_stack_p48) + (0xCC0ULL);
    v_stack_p50 = (unsigned int)((unsigned int)(result));
    result = ((unsigned int)((unsigned int)(result))) * ((unsigned int)((unsigned int)(result)));
    result = (result) + (a1);
    v_stack_p38 = result;
    goto loc_002B134C;
loc_002B1ADE:
    a4 = (unsigned int)((v_stack_p60) & (31));
    a1 = (v_stack_p60) >> (5);
    result = (unsigned int)((1) << ((unsigned __int8)((unsigned int)(a4))));
loc_002B1B16:
    result = MiInsertPageInList(0, (unsigned int)(0x800ULL), *(unsigned __int64 *)(v_rip + 12052163) + a1 * 4, a4);
    goto loc_002B1710;
}
```

## 5. (Beta) C Style

```c
int64_t MiReplaceTransitionPage(void *Arg1, void *Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint32_t v_stack_m128;
    uint64_t v_stack_m48;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint8_t v_stack_mF6;
    uint32_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint8_t v_stack_p33;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint8_t v_stack_p43;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p70;

    local_rsp = (local_rsp) - (240);
    result = (*(uint64_t *)(v_rip + 0xB59606)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_mE8 = (uint32_t)((uint32_t)(Arg4));
    local_rdi = 0;
    Arg2 = 0;
    result = memset(v_stack_mB8, Arg2, local_rdi + 104, Arg4);
    v_stack_mD8 = (uint32_t)(0xFFFFFFULL);
    Arg1 = (Arg1) - (0);
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (local_rdi + 104);
    v_stack_mD0 = Arg1;
    local_r13 = (0) - (0);
    result = (*(uint64_t *)(arg1 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    local_r13 = (local_r13) >> (4);
    local_r13 = (local_r13) * (local_rdi + 104);
    result = (uint32_t)((*(uint8_t *)(arg1 + 0x22)) & (7));
    v_stack_mE0 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xB7EED9) + result * 8);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (2));
    v_stack_mF0 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB7EED9) + result * 8) + result * 8 + 0x1BE0);
    v_stack_mF8 = (uint32_t)(Arg1);
    if (condition_is_not_equal) goto loc_002B11FC;
    local_r12 = 0;
loc_002B11EB:
    if (condition_is_below) goto loc_002B1780;
loc_002B11FC:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (64)) != 0) goto loc_002B1850;
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x22)) & (7));
    if (((uint8_t)(result)) == 3) goto loc_002B1902;
loc_002B1219:
loc_002B121E:
    local_r12 = (uint32_t)((*(uint8_t *)(arg2 + 0x24)) & (15));
    result = MiGetPfnSlabType(0, Arg2, local_rdi + 104, Arg4);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (16));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x20))) >> (16));
    Arg3 = (uint32_t)(((uint8_t)(Arg1)) >> (6));
    Arg2 = (uint32_t)(((uint8_t)(Arg1)) >> (6));
    v_stack_mF8 = (uint32_t)(result);
    if (Arg3 != ((uint32_t)(Arg2))) {
        Arg3 = 1;
        Arg1 = Arg2;
        result = MiChangePageAttribute(Arg1, Arg2, Arg3, Arg4);
    }
    result = (*(uint64_t *)(arg2 + 0x18)) & (Arg1);
    *(uint64_t *)(arg2 + 0x18) = result;
    result = MiCopyPfnEntryEx(Arg2, Arg1, Arg3, Arg4);
    result = (uint8_t)((*(uint8_t *)(arg2 + 0x24)) & (240));
    result = (uint8_t)((result) | ((uint8_t)(local_r12)));
    *(uint8_t *)(arg2 + 0x24) = (uint8_t)(result);
    result = (*(uint64_t *)(arg1 + 0x28)) & (Arg2);
    if (result == v_stack_mD0) goto loc_002B1889;
loc_002B12A9:
    result = MiCopyPage(local_r13, v_stack_mD0, 6, Arg4);
    Arg2 = ((uint32_t)(*(uint32_t *)(v_rip + 0xD1DDBC))) << (59);
    Arg1 = (Arg2) ^ (*(uint64_t *)(arg2 + 0x18));
    Arg1 = (Arg1) & (*(uint64_t *)(arg2 + 0x18));
    Arg1 = (Arg1) ^ (Arg2);
    *(void **)(arg2 + 0x18) = Arg1;
    if (((v_stack_mE8) & (1)) != 0) goto loc_002B1594;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mF0 + 0xC)))) != 2) goto loc_002B17EB;
    if (((uint32_t)((uint32_t)(Arg3))) < 9) goto loc_002B1988;
    result = MiGetPfnPriority(Arg1, Arg2, 6, Arg4);
    local_r12 = (v_stack_mE0) + (0xCC0ULL);
    Arg2 = (Arg2) * ((uint32_t)((uint32_t)(result)));
    v_stack_mD8 = result;
    local_r12 = (local_r12) + (Arg2);
    v_stack_mF0 = local_r12;
    if (((uint32_t)((uint32_t)(Arg3))) == 9) {
        Arg1 = *(uint32_t *)(arg1 + 0x20);
        Arg1 = (uint32_t)((Arg1) >> (24));
        if ((((uint8_t)(Arg1)) & (8)) != 0) { local_rdi = 2; }
    }
    result = MI_NODE_FROM_PFN(Arg1, Arg2, 6, Arg4);
    result = MI_NODE_FROM_PFN(Arg2, Arg2, 6, Arg4);
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)(result))) goto loc_002B1A1F;
    if (((uint32_t)((uint32_t)(Arg3))) != ((uint32_t)((uint32_t)(v_stack_mF8)))) goto loc_002B1A1F;
    result = MiGetPfnSlabType(Arg1, Arg2, 6, Arg4);
    if (((uint32_t)(result)) == 8) goto loc_002B19C0;
loc_002B1385:
    v_stack_m108 = v_stack_mB8;
    result = MiAcquirePageListLock(v_stack_mF0, Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg3))), 1);
    result = MiReplaceStandbyLookaside(v_stack_mD0, local_r13, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_mB8);
loc_002B13BB:
    local_r10 = (*(uint64_t *)(arg1)) & (result);
    local_rbx = (*(uint64_t *)(arg1 + 0x18)) & (result);
    Arg2 = (*(uint64_t *)(arg1)) ^ (*(uint64_t *)(arg2));
    Arg2 = (Arg2) & (v_stack_mB8);
    Arg2 = (Arg2) ^ (*(uint64_t *)(arg1));
    *(void **)(arg2) = Arg2;
    result = (*(uint64_t *)(arg2 + 0x18)) ^ (*(uint64_t *)(arg1 + 0x18));
    result = (result) & (v_stack_mB8);
    result = (result) ^ (*(uint64_t *)(arg1 + 0x18));
    *(uint64_t *)(arg2 + 0x18) = result;
    if (local_r10 == local_r11) goto loc_002B17A1;
    Arg4 = (local_r10 + local_r10 * 2) << (4);
    Arg4 = (Arg4) + (result);
    if (((uint32_t)(v_stack_mD8)) != 0xFFFFFFULL) goto loc_002B1819;
loc_002B1445:
    Arg1 = (*(uint64_t *)(Arg4 + 0x18)) ^ (local_r13);
    Arg1 = (Arg1) & (v_stack_mB8);
    Arg1 = (Arg1) ^ (local_r13);
    if ((*(uint64_t *)(Arg4 + 0x18)) == (*(uint64_t *)(Arg4 + 0x18))) goto loc_002B1492;
loc_002B1470:
    Arg3 = (*(uint64_t *)(Arg4 + 0x18)) ^ (local_r13);
    Arg3 = (Arg3) & ((uint32_t)(v_stack_mF8));
    Arg3 = (Arg3) ^ (local_r13);
    if ((*(uint64_t *)(Arg4 + 0x18)) != (*(uint64_t *)(Arg4 + 0x18))) goto loc_002B1470;
loc_002B1492:
loc_002B14A1:
    if (local_rbx == (*(uint64_t *)(Arg4 + 0x18))) goto loc_002B1847;
    Arg4 = (local_rbx + local_rbx * 2) << (4);
    Arg4 = (Arg4) + (*(uint64_t *)(Arg4 + 0x18));
    if (((uint32_t)(v_stack_mD8)) != 0xFFFFFFULL) goto loc_002B17BD;
loc_002B14D9:
    result = (*(uint64_t *)(Arg4)) ^ (local_r13);
    result = (result) & (*(uint64_t *)(Arg4 + 0x18));
    result = (result) ^ (local_r13);
    *(uint64_t *)(Arg4) = result;
loc_002B14E8:
    if (((uint32_t)(v_stack_mD8)) == 0xFFFFFFULL) goto loc_002B1527;
loc_002B14F1:
    if (((uint32_t)((uint32_t)(Arg3))) < 9) goto loc_002B1507;
    if (((uint32_t)((uint32_t)(v_stack_mF8))) >= 9) goto loc_002B150C;
    if (((uint32_t)((uint32_t)(Arg3))) == 9) goto loc_002B1A77;
loc_002B1507:
    if (((uint32_t)(local_rdi)) < 4) {
        result = v_stack_mB8;
        Arg4 = (uint32_t)((uint32_t)(v_stack_mF8));
        Arg3 = (uint32_t)((uint32_t)(Arg3));
        v_stack_m108 = result;
        Arg2 = Arg2;
        Arg1 = Arg1;
        result = MiReplaceSecondaryListStandbyPage(Arg1, Arg2, Arg3, Arg4);
    }
    if (((uint32_t)((uint32_t)(Arg3))) == 9) {
        Arg4 = 2;
        v_stack_m108 = 0;
        Arg2 = v_stack_mD0;
        Arg1 = v_stack_mE0;
        Arg3 = Arg4 + 1;
        result = MiUpdateLargePageCandidateValue(Arg1, Arg2, Arg3, Arg4);
    }
    if (((uint32_t)((uint32_t)(v_stack_mF8))) == 9) {
        Arg4 = 3;
        v_stack_m108 = 0;
        Arg3 = Arg4;
        Arg2 = local_r13;
        Arg1 = v_stack_mE0;
        result = MiUpdateLargePageCandidateValue(Arg1, Arg2, Arg3, Arg4);
    }
    if ((*(uint32_t *)(v_rip + 0xB7EBCD)) == 1) goto loc_002B1ADE;
    result = MiReleasePageListLock(v_stack_mF0, v_stack_mB8, Arg3, Arg4);
loc_002B1594:
    v_stack_mF8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (16));
    result = (uint8_t)((result) & (253));
    result = (uint8_t)((result) | (5));
    v_stack_mF6 = (uint8_t)(result);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_mF8));
    result = (*(uint64_t *)(arg1 + 0x18)) & (Arg4);
    *(uint64_t *)(arg1 + 0x18) = result;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip + 0xD1DAB3))) << (59);
    result = (*(uint64_t *)(arg1 + 0x18)) ^ (Arg1);
    result = (result) & (v_stack_mB8);
    result = (result) ^ (Arg1);
    *(uint64_t *)(arg1 + 0x18) = result;
    result = (*(uint64_t *)(arg1 + 0x28)) & (v_stack_mB8);
    if (result == v_stack_mD0) goto loc_002B1923;
    Arg1 = (*(uint64_t *)(arg1 + 0x28)) & (v_stack_mB8);
    local_rdi = (uint32_t)((local_rdi) | (1));
    Arg2 = 0;
    result = MiMapPageInHyperSpaceWorker(Arg1, Arg2, (uint32_t)(0x80000000ULL), Arg4);
    Arg1 = (*(uint64_t *)(arg1 + 0x8)) >> (3);
    Arg1 = (uint32_t)((Arg1) & (511));
loc_002B1639:
    result = MI_READ_PTE_LOCK_FREE(result + Arg1 * 8, Arg2, (uint32_t)(0x80000000ULL), Arg4);
    if (*(uint64_t *)(v_rip + 0xB7C638) == 0) goto loc_002B165B;
    if ((((uint8_t)(result)) & (16)) != 0) goto loc_002B17B4;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xB7C638));
    result = (result) & (Arg1);
loc_002B165B:
    Arg2 = (local_r13) << (12);
    Arg1 = (Arg2) ^ (result);
    Arg1 = (Arg1) & (result);
    Arg1 = (Arg1) ^ (Arg2);
    result = MiSwizzleInvalidPte(Arg1, Arg2, (uint32_t)(0x80000000ULL), Arg4);
    v_stack_mC8 = result;
    local_r12 = 0;
    result = MiPteInShadowRange(result + Arg1 * 8, Arg2, (uint32_t)(0x80000000ULL), Arg4);
    if ((uint32_t)(result) != 0) goto loc_002B1A50;
loc_002B1698:
    *(uint64_t *)(result + arg1 * 8) = result;
    if (0 != 0) goto loc_002B1A67;
loc_002B16A4:
    local_r14 = result + Arg1 * 8;
    if ((((uint8_t)(local_rdi)) & (1)) != 0) {
        local_r14 = (result + Arg1 * 8) >> (9);
        local_r14 = (local_r14) & (result);
        local_r14 = (local_r14) + (result);
        result = *(uint64_t *)(gs_base + (0 + 0x20));
        Arg1 = *(uint64_t *)(result + 0x8838);
        result = *(uint64_t *)(v_rip - 0x2A0E5F);
        *(uint64_t *)(arg1) = 0;
        *(uint64_t *)(local_r14) = result;
        local_r14 = *(uint64_t *)(arg1 + 0x8);
        local_r14 = (local_r14) | (result);
    }
    if (!sign_flag) goto loc_002B18CF;
loc_002B1707:
    if (((uint32_t)(local_rdi)) >= 4) goto loc_002B1B16;
loc_002B1710:
    if (((v_stack_mE8) & (2)) == 0) {
    }
    if ((((uint8_t)(local_rdi)) & (2)) != 0) goto loc_002B192F;
loc_002B1730:
    Arg1 = (*(uint64_t *)(arg1 + 0x28)) & (Arg4);
    if ((*(uint64_t *)(arg1 + 0x28)) == (*(uint64_t *)(arg1 + 0x28))) goto loc_002B176C;
loc_002B1755:
    Arg3 = (*(uint64_t *)(arg1 + 0x28)) & (Arg4);
    if ((*(uint64_t *)(arg1 + 0x28)) != (*(uint64_t *)(arg1 + 0x28))) goto loc_002B1755;
loc_002B176C:
    result = MiClearPfnReuseFields(Arg1, *(uint64_t *)(arg1 + 0x28), *(uint64_t *)(arg1 + 0x28), Arg4);
    goto loc_002B1865;
loc_002B1780:
    local_r12 = (uint32_t)((local_r12) + 1);
    if (((*(uint32_t *)(v_rip + 0xD13B22)) & ((uint32_t)(local_r12))) == 0) goto loc_002B1960;
loc_002B1790:
loc_002B1792:
    if (!sign_flag) goto loc_002B11EB;
    goto loc_002B1780;
loc_002B17A1:
    *(uint64_t *)(v_stack_mF0 + 0x18) = local_r13;
    goto loc_002B14A1;
loc_002B17B4:
    result = (*(uint64_t *)(arg2 + 0x18)) & (-17);
    goto loc_002B165B;
loc_002B17BD:
    if (((uint32_t)(local_rdi)) != 2) goto loc_002B14D9;
    result = MiIsDecayPfn(result, *(uint64_t *)(arg1 + 0x28), *(uint64_t *)(arg1 + 0x28), Arg4);
    if ((uint32_t)(result) == 0) goto loc_002B14D9;
    result = MiUpdateTransitionPteFrame(*(uint64_t *)(Arg4 + 0x10), local_r13, *(uint64_t *)(arg1 + 0x28), Arg4);
    *(uint64_t *)(Arg4 + 0x10) = result;
    goto loc_002B14F1;
loc_002B17EB:
    if (((uint32_t)(result)) == 3) goto loc_002B1899;
    v_stack_m108 = v_stack_mB8;
loc_002B17FE:
    result = MiAcquirePageListLock(*(uint64_t *)(Arg4 + 0x10), Arg1, (uint32_t)((uint32_t)(local_r14)), 1);
    goto loc_002B13BB;
loc_002B1819:
    if (((uint32_t)(local_rdi)) != 2) goto loc_002B1445;
    result = MiIsDecayPfn(v_stack_mF0, Arg1, (uint32_t)((uint32_t)(local_r14)), 1);
    if ((uint32_t)(result) == 0) goto loc_002B1445;
    result = MiSetPfnContainingFrame(1, local_r13, (uint32_t)((uint32_t)(local_r14)), 1);
    goto loc_002B1492;
loc_002B1847:
    *(uint64_t *)(v_stack_mF0 + 0x10) = local_r13;
    goto loc_002B14E8;
loc_002B1850:
    if (1 == 0) {
    }
    result = 0;
loc_002B1865:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, local_r13, (uint32_t)((uint32_t)(local_r14)), 1);
    local_rsp = (local_rsp) + (240);
    return result;
loc_002B1889:
    result = MiSetPfnContainingFrame(Arg2, local_r13, (uint32_t)((uint32_t)(local_r14)), 1);
    goto loc_002B12A9;
loc_002B1899:
    if (condition_is_below) goto loc_002B194B;
    Arg3 = 0;
    result = MiDetermineModifiedPageListHead(Arg2, v_stack_p48, Arg3, 1);
loc_002B18B8:
    v_stack_p38 = result;
    v_stack_p20 = v_stack_p70;
    goto loc_002B17FE;
loc_002B18CF:
    result = MiGetSystemRegionType(local_r14, v_stack_p48, Arg3, 1);
    if (((uint32_t)(result)) != 4) goto loc_002B1707;
    local_r13 = (local_r13) << (12);
    result = (local_r13) | (2);
    if ((*(uint8_t *)(v_rip + 0xD15195)) == 0) { result = local_r13; }
    *(uint64_t *)(local_r14 - 0x300) = result;
    goto loc_002B1707;
loc_002B1902:
    if ((*(uint8_t *)(v_rip + 0xD15195)) >= 0) goto loc_002B1219;
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(arg1 + 0x24))) & (240));
    *(uint8_t *)(arg1 + 0x24) = (uint8_t)(result);
    goto loc_002B121E;
loc_002B1923:
    local_r14 = (*(uint64_t *)(arg1 + 0x8)) | (local_r14);
    goto loc_002B1639;
loc_002B192F:
    v_stack_p40 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (24));
    result = (uint8_t)((result) & (247));
    v_stack_p43 = (uint8_t)(result);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_p40));
    goto loc_002B1730;
loc_002B194B:
    result = ((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x24)))) + (64);
    result = (result) * (result);
    result = (result) + (v_stack_p48);
    goto loc_002B18B8;
loc_002B1960:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD15152)))) & (64)) == 0) goto loc_002B1790;
    result = KiCheckVpBackingLongSpinWaitHypercall(local_r14, v_stack_p48, Arg3, 1);
    if ((uint8_t)(result) == 0) goto loc_002B1790;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x24))), v_stack_p48, Arg3, 1);
    goto loc_002B1792;
loc_002B1988:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (8)) == 0) goto loc_002B1AB5;
    Arg2 = 0;
    result = MiUnlinkPageFromListEx((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x24))), Arg2, Arg3, 1);
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x20))) >> (24));
    result = (uint8_t)((result) & (247));
    v_stack_p33 = (uint8_t)(result);
    *(uint32_t *)(arg2 + 0x20) = (uint32_t)((uint32_t)(v_stack_p30));
    goto loc_002B1594;
loc_002B19C0:
    Arg1 = (Arg1) - (1);
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (v_stack_mF0);
    Arg1 = (Arg1) >> (9);
    Arg3 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0xB8B86C) + arg1 * 2 + 0x1)) & (127));
    Arg1 = (0) - (1);
    Arg1 = (Arg1) >> (4);
    Arg1 = (Arg1) * (v_stack_mF0);
    Arg1 = (Arg1) >> (9);
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0xB8B86C) + arg1 * 2 + 0x1)) & (127));
    if (((uint8_t)(Arg3)) == ((uint8_t)(result))) goto loc_002B1385;
loc_002B1A1F:
    Arg1 = (v_stack_p38) + (32);
    result = ExAcquireSpinLockExclusiveAtDpcLevel(Arg1, *(uint64_t *)(v_rip + 0xB8B86C), Arg3, 1);
    Arg4 = 0;
    result = MiReplaceStandbyLookaside(v_stack_p58, Arg4 - 1, (uint32_t)((uint32_t)(local_r14)), Arg4);
    Arg2 = 0;
    result = MiSetStandbyLookasideState(local_r13, Arg2, (uint32_t)((uint32_t)(local_r14)), Arg4);
    goto loc_002B13BB;
loc_002B1A50:
    result = MiSanitizeShadowPxe(local_r13, v_stack_p60, (uint32_t)((uint32_t)(local_r14)), Arg4);
    goto loc_002B1698;
loc_002B1A67:
    result = MiWritePteShadow(local_r14, v_stack_p60, (uint32_t)((uint32_t)(local_r14)), Arg4);
    goto loc_002B16A4;
loc_002B1A77:
    if (!sign_flag) goto loc_002B1AAD;
    result = (v_stack_p48) + (0x1C40ULL);
loc_002B1A8F:
    Arg4 = 0;
    result = MiDecreaseAvailablePages(v_stack_p48, Arg4 + 1, Arg4 - 1, Arg4);
    goto loc_002B1507;
loc_002B1AAD:
    result = (result) + (0x3FC0ULL);
    goto loc_002B1A8F;
loc_002B1AB5:
    result = MiGetPfnPriority(v_stack_p48, Arg4 + 1, Arg4 - 1, Arg4);
    Arg1 = (v_stack_p48) + (0xCC0ULL);
    v_stack_p50 = (uint32_t)((uint32_t)(result));
    result = ((uint32_t)((uint32_t)(result))) * ((uint32_t)((uint32_t)(result)));
    result = (result) + (Arg1);
    v_stack_p38 = result;
    goto loc_002B134C;
loc_002B1ADE:
    Arg4 = (uint32_t)((v_stack_p60) & (31));
    Arg1 = (v_stack_p60) >> (5);
    result = (uint32_t)((1) << ((uint8_t)((uint32_t)(Arg4))));
loc_002B1B16:
    result = MiInsertPageInList(0, (uint32_t)(0x800ULL), *(uint64_t *)(v_rip + 0xB7E6C3) + Arg1 * 4, Arg4);
    goto loc_002B1710;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `W` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `W` |
| `Arg1` | `+ 0x22` | `8` | `R` |
| `Arg1` | `+ 0x24` | `8` | `R` |
| `Arg1` | `+ 0x24` | `8` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R/W` |
| `Arg2` | `+ 0x18` | `64` | `W` |
| `Arg2` | `+ 0x20` | `32` | `R` |
| `Arg2` | `+ 0x20` | `32` | `W` |
| `Arg2` | `+ 0x24` | `8` | `R` |
| `Arg2` | `+ 0x24` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002B1120&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
