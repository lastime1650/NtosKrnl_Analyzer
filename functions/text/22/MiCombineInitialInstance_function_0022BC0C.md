# MiCombineInitialInstance

- RVA: `0x0022BC0C`–`0x0022CA96` (길이 `3,722` bytes)
- VA: `0x000000014022BC0C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005FF94`
- 디코드: `743`개 명령, `3,722/3,722` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **49**; 고유 호출 대상: **38**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x0022BDFF` → [MiMapSinglePage](MiMapSinglePage_function_00229D00.md) (function, `0x00229D00`)
- `0x0022BE64` → [MiSetOriginalPtePfnFromFreeList](../28/MiSetOriginalPtePfnFromFreeList_function_0028A99C.md) (function, `0x0028A99C`)
- `0x0022BEB5` → [MiTranslateCacheAttribute](../47/MiTranslateCacheAttribute_function_004749CC.md) (function, `0x004749CC`)
- `0x0022BED8` → [MiMapSinglePage](MiMapSinglePage_function_00229D00.md) (function, `0x00229D00`)
- `0x0022BEF8` → [KeCopyPage](../6B/KeCopyPage_function_006BA0F0.md) (function, `0x006BA0F0`)
- `0x0022BF9E` → [MiGetContainingPageTable](../34/MiGetContainingPageTable_function_003467F0.md) (function, `0x003467F0`)
- `0x0022C104` → [MiAbandonPrivatePfn](MiAbandonPrivatePfn_function_0022F548.md) (function, `0x0022F548`)
- `0x0022C141` → [MiFinalizePageAttribute](../33/MiFinalizePageAttribute_function_00332E30.md) (function, `0x00332E30`)
- `0x0022C15C` → [MiCopyPfnEntryEx](../2B/MiCopyPfnEntryEx_function_002B2670.md) (function, `0x002B2670`)
- `0x0022C164` → [MiGetPfnPriority](../32/MiGetPfnPriority_function_003226F0.md) (function, `0x003226F0`)
- `0x0022C1BB` → [MiSetPfnContainingFrame](../36/MiSetPfnContainingFrame_function_00363FC0.md) (function, `0x00363FC0`)
- `0x0022C1C8` → [MI_MAKE_PROTECT_WRITE_COPY](MI_MAKE_PROTECT_WRITE_COPY_function_0022F308.md) (function, `0x0022F308`)
- `0x0022C1E1` → [MiTransferPageFileOwnership](MiTransferPageFileOwnership_function_0022F320.md) (function, `0x0022F320`)
- `0x0022C28A` → [MiWriteValidPteNewPage](../37/MiWriteValidPteNewPage_function_00376068.md) (function, `0x00376068`)
- `0x0022C30D` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x0022C32B` → [MiSetWsleProtection](../29/MiSetWsleProtection_function_002939D8.md) (function, `0x002939D8`)
- `0x0022C33D` → [MiUpdateWorkingSetPrivateSize](../36/MiUpdateWorkingSetPrivateSize_function_00362250.md) (function, `0x00362250`)
- `0x0022C380` → [MiActivateCombineBlock](../26/MiActivateCombineBlock_function_00266094.md) (function, `0x00266094`)
- `0x0022C392` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0022C3B8` → [MiComputeHash64](../43/MiComputeHash64_function_00432DC0.md) (function, `0x00432DC0`)
- `0x0022C4DD` → [MiPfnReferenceCountIsZero](../2B/MiPfnReferenceCountIsZero_function_002B9E40.md) (function, `0x002B9E40`)
- `0x0022C523` → [MiLockAndDecrementShareCount](../2A/MiLockAndDecrementShareCount_function_002A2854.md) (function, `0x002A2854`)
- `0x0022C542` → [MiMakeTransitionPte](../36/MiMakeTransitionPte_function_00363F70.md) (function, `0x00363F70`)
- `0x0022C59D` → [MiUnlinkPageFromListEx](../28/MiUnlinkPageFromListEx_function_00287590.md) (function, `0x00287590`)
- `0x0022C5B3` → [MiDiscardTransitionPteEx](../37/MiDiscardTransitionPteEx_function_00375954.md) (function, `0x00375954`)
- `0x0022C5E4` → [MiDecrementCloneBlock](MiDecrementCloneBlock_function_0022BA8C.md) (function, `0x0022BA8C`)
- `0x0022C601` → [MiGetCloneCharges](MiGetCloneCharges_function_0022CB5C.md) (function, `0x0022CB5C`)
- `0x0022C647` → [MiMakePrototypePteDirect](../29/MiMakePrototypePteDirect_function_00294DE0.md) (function, `0x00294DE0`)
- `0x0022C657` → [MiWriteRepurposedTransitionPte](../4B/MiWriteRepurposedTransitionPte_function_004B0EC8.md) (function, `0x004B0EC8`)
- `0x0022C679` → [MiTransferPageFileOwnership](MiTransferPageFileOwnership_function_0022F320.md) (function, `0x0022F320`)
- `0x0022C689` → [MiPfnReferenceCountIsZero](../2B/MiPfnReferenceCountIsZero_function_002B9E40.md) (function, `0x002B9E40`)
- `0x0022C6CC` → [MiGetCloneCharges](MiGetCloneCharges_function_0022CB5C.md) (function, `0x0022CB5C`)
- `0x0022C734` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x0022C77C` → [MiStandbyPageStillCombineCandidate](MiStandbyPageStillCombineCandidate_function_0022A148.md) (function, `0x0022A148`)
- `0x0022C7A0` → [MiRecheckCombineVm](MiRecheckCombineVm_function_0022A1FC.md) (function, `0x0022A1FC`)
- `0x0022C7BB` → [KeCopyPage](../6B/KeCopyPage_function_006BA0F0.md) (function, `0x006BA0F0`)
- `0x0022C8D2` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0022C8E1` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0022C901` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0022C910` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0022C955` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0022C965` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0022C98B` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0022C997` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0022C9BC` → [MiChangePageAttribute](../33/MiChangePageAttribute_function_00332ECC.md) (function, `0x00332ECC`)
- `0x0022C9DF` → [MiHashIsCommon](../46/MiHashIsCommon_function_00460848.md) (function, `0x00460848`)
- `0x0022CA14` → [MiIdentifyPfn](../31/MiIdentifyPfn_function_0031CAC0.md) (function, `0x0031CAC0`)
- `0x0022CA7A` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x0022CA8C` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)

### Direct callers
- [MiConvertStandbyToProto](MiConvertStandbyToProto_function_0022A330.md) at `0x0022A43D`
- [MiConvertPrivateToProto](MiConvertPrivateToProto_function_0022B0E4.md) at `0x0022B169`

### Static image references
- `0x0022BC23` → RVA `0x00E0A740` (`.data`; read)
- `0x0022BCF3` → RVA `0x00E30088` (`.data`; read)
- `0x0022BF35` → RVA `0x00010880` (`.rdata`; read)
- `0x0022C297` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x0022C3C6` → RVA `0x00E2FF10` (`.data`; read)
- `0x0022C3E1` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x0022C42E` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0022C8C4` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0022BC0C  4C 8B DC                        mov r11, rsp
0022BC0F  49 89 5B 20                     mov qword ptr [r11 + 0x20], rbx
0022BC13  57                              push rdi
0022BC14  41 54                           push r12
0022BC16  41 55                           push r13
0022BC18  41 56                           push r14
0022BC1A  41 57                           push r15
0022BC1C  48 81 EC E0 01 00 00            sub rsp, 0x1e0
0022BC23  48 8B 05 16 EB BD 00            mov rax, qword ptr [rip + 0xbdeb16]
0022BC2A  48 33 C4                        xor rax, rsp
0022BC2D  48 89 84 24 D8 01 00 00         mov qword ptr [rsp + 0x1d8], rax
0022BC35  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
0022BC3A  48 89 94 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdx
0022BC42  4C 8B C9                        mov r9, rcx
0022BC45  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
0022BC4A  48 89 8C 24 50 01 00 00         mov qword ptr [rsp + 0x150], rcx
0022BC52  48 89 94 24 10 01 00 00         mov qword ptr [rsp + 0x110], rdx
0022BC5A  4C 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r8
0022BC62  48 83 64 24 58 00               and qword ptr [rsp + 0x58], 0
0022BC68  0F 57 C0                        xorps xmm0, xmm0
0022BC6B  41 0F 11 43 A0                  movups xmmword ptr [r11 - 0x60], xmm0
0022BC70  41 0F 11 43 B0                  movups xmmword ptr [r11 - 0x50], xmm0
0022BC75  48 8D 81 28 01 00 00            lea rax, [rcx + 0x128]
0022BC7C  48 89 84 24 98 01 00 00         mov qword ptr [rsp + 0x198], rax
0022BC84  48 8B 00                        mov rax, qword ptr [rax]
0022BC87  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0022BC8C  48 89 84 24 38 01 00 00         mov qword ptr [rsp + 0x138], rax
0022BC94  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0022BC99  48 8D 81 30 01 00 00            lea rax, [rcx + 0x130]
0022BCA0  48 89 84 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], rax
0022BCA8  4C 8B 28                        mov r13, qword ptr [rax]
0022BCAB  4C 89 AC 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r13
0022BCB3  4C 89 AC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r13
0022BCBB  48 8B 19                        mov rbx, qword ptr [rcx]
0022BCBE  48 89 9C 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rbx
0022BCC6  48 89 9C 24 90 01 00 00         mov qword ptr [rsp + 0x190], rbx
0022BCCE  8B 81 8C 00 00 00               mov eax, dword ptr [rcx + 0x8c]
0022BCD4  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0022BCD8  48 8B 41 70                     mov rax, qword ptr [rcx + 0x70]
0022BCDC  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
0022BCE4  48 89 84 24 70 01 00 00         mov qword ptr [rsp + 0x170], rax
0022BCEC  0F B7 88 AE 00 00 00            movzx ecx, word ptr [rax + 0xae]
0022BCF3  48 8B 05 8E 43 C0 00            mov rax, qword ptr [rip + 0xc0438e]
0022BCFA  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
0022BCFE  48 89 84 24 08 01 00 00         mov qword ptr [rsp + 0x108], rax
0022BD06  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
0022BD0E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0022BD13  4D 8B 91 90 00 00 00            mov r10, qword ptr [r9 + 0x90]
0022BD1A  4C 89 94 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r10
0022BD22  4C 89 94 24 58 01 00 00         mov qword ptr [rsp + 0x158], r10
0022BD2A  4B 8D 0C 52                     lea rcx, [r10 + r10*2]
0022BD2E  48 C1 E1 04                     shl rcx, 4
0022BD32  49 BB 00 00 00 00 00 DE FF FF   movabs r11, 0xffffde0000000000
0022BD3C  49 8B C3                        mov rax, r11
0022BD3F  48 03 C1                        add rax, rcx
0022BD42  4C 8B F0                        mov r14, rax
0022BD45  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
0022BD4D  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
0022BD55  4D 8B 61 60                     mov r12, qword ptr [r9 + 0x60]
0022BD59  4C 89 A4 24 60 01 00 00         mov qword ptr [rsp + 0x160], r12
0022BD61  48 8B 03                        mov rax, qword ptr [rbx]
0022BD64  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
0022BD6C  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
0022BD74  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0022BD79  49 8D 9C 24 00 10 00 00         lea rbx, [r12 + 0x1000]
0022BD81  48 89 9C 24 68 01 00 00         mov qword ptr [rsp + 0x168], rbx
0022BD89  48 8D 42 10                     lea rax, [rdx + 0x10]
0022BD8D  48 89 84 24 C8 01 00 00         mov qword ptr [rsp + 0x1c8], rax
0022BD95  48 8B 08                        mov rcx, qword ptr [rax]
0022BD98  48 C1 E9 09                     shr rcx, 9
0022BD9C  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0022BDA6  48 23 C8                        and rcx, rax
0022BDA9  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0022BDB3  48 8B C0                        mov rax, rax
0022BDB6  48 03 C8                        add rcx, rax
0022BDB9  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
0022BDBE  48 8D 42 20                     lea rax, [rdx + 0x20]
0022BDC2  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
0022BDCA  8B 10                           mov edx, dword ptr [rax]
0022BDCC  83 E2 1F                        and edx, 0x1f
0022BDCF  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
0022BDD3  49 8B C3                        mov rax, r11
0022BDD6  4D 8B FD                        mov r15, r13
0022BDD9  4C 2B F8                        sub r15, rax
0022BDDC  4D 85 C0                        test r8, r8
0022BDDF  0F 84 48 07 00 00               je 0x14022c52d
0022BDE5  48 8B 39                        mov rdi, qword ptr [rcx]
0022BDE8  48 89 BC 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rdi
0022BDF0  45 33 C9                        xor r9d, r9d
0022BDF3  41 B8 10 00 00 C0               mov r8d, 0xc0000010
0022BDF9  49 8B D2                        mov rdx, r10
0022BDFC  49 8B CC                        mov rcx, r12
0022BDFF  E8 FC DE FF FF                  call 0x140229d00
0022BE04  48 C7 84 24 20 01 00 00 38 00 00 00  mov qword ptr [rsp + 0x120], 0x38
0022BE10  49 B8 AB AA AA AA AA AA AA AA   movabs r8, 0xaaaaaaaaaaaaaaab
0022BE1A  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0022BE1F  48 83 C0 20                     add rax, 0x20
0022BE23  48 89 84 24 78 01 00 00         mov qword ptr [rsp + 0x178], rax
0022BE2B  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
0022BE33  48 8B D0                        mov rdx, rax
0022BE36  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
0022BE40  48 23 D1                        and rdx, rcx
0022BE43  48 89 94 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rdx
0022BE4B  0F 57 C0                        xorps xmm0, xmm0
0022BE4E  0F 11 00                        movups xmmword ptr [rax], xmm0
0022BE51  0F 11 40 10                     movups xmmword ptr [rax + 0x10], xmm0
0022BE55  49 8D 45 10                     lea rax, [r13 + 0x10]
0022BE59  48 89 84 24 88 01 00 00         mov qword ptr [rsp + 0x188], rax
0022BE61  48 8B C8                        mov rcx, rax
0022BE64  E8 33 EB 05 00                  call 0x14028a99c
0022BE69  49 C1 FF 04                     sar r15, 4
0022BE6D  4D 0F AF F8                     imul r15, r8
0022BE71  4C 89 BC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r15
0022BE79  49 8D 46 20                     lea rax, [r14 + 0x20]
0022BE7D  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
0022BE85  8B 00                           mov eax, dword ptr [rax]
0022BE87  C1 E8 10                        shr eax, 0x10
0022BE8A  44 0F B6 F8                     movzx r15d, al
0022BE8E  41 C1 EF 06                     shr r15d, 6
0022BE92  49 8D 45 20                     lea rax, [r13 + 0x20]
0022BE96  48 89 84 24 80 01 00 00         mov qword ptr [rsp + 0x180], rax
0022BE9E  8B 00                           mov eax, dword ptr [rax]
0022BEA0  C1 E8 10                        shr eax, 0x10
0022BEA3  0F B6 C8                        movzx ecx, al
0022BEA6  C1 E9 06                        shr ecx, 6
0022BEA9  41 3B CF                        cmp ecx, r15d
0022BEAC  0F 85 FE 0A 00 00               jne 0x14022c9b0
0022BEB2  41 8B CF                        mov ecx, r15d
0022BEB5  E8 12 8B 24 00                  call 0x1404749cc
0022BEBA  44 8B F8                        mov r15d, eax
0022BEBD  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
0022BEC4  45 33 C9                        xor r9d, r9d
0022BEC7  41 B8 10 00 00 40               mov r8d, 0x40000010
0022BECD  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
0022BED5  48 8B CB                        mov rcx, rbx
0022BED8  E8 23 DE FF FF                  call 0x140229d00
0022BEDD  41 BD 01 00 00 00               mov r13d, 1
0022BEE3  48 83 7C 24 38 00               cmp qword ptr [rsp + 0x38], 0
0022BEE9  0F 84 4F 08 00 00               je 0x14022c73e
0022BEEF  45 8B C7                        mov r8d, r15d
0022BEF2  49 8B D4                        mov rdx, r12
0022BEF5  48 8B CB                        mov rcx, rbx
0022BEF8  E8 F3 E1 48 00                  call 0x1406ba0f0
0022BEFD  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
0022BF07  48 B9 F8 FF FF FF 7F 00 00 00   movabs rcx, 0x7ffffffff8
0022BF11  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
0022BF16  4C 8B 84 24 90 00 00 00         mov r8, qword ptr [rsp + 0x90]
0022BF1E  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
0022BF23  4D 85 D2                        test r10, r10
0022BF26  74 20                           je 0x14022bf48
0022BF28  49 C1 EC 09                     shr r12, 9
0022BF2C  4C 23 E1                        and r12, rcx
0022BF2F  49 8B C1                        mov rax, r9
0022BF32  4C 03 E0                        add r12, rax
0022BF35  48 8B 05 44 49 DE FF            mov rax, qword ptr [rip - 0x21b6bc]
0022BF3C  48 89 84 24 18 01 00 00         mov qword ptr [rsp + 0x118], rax
0022BF44  49 89 04 24                     mov qword ptr [r12], rax
0022BF48  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0022BF4C  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0022BF51  45 85 ED                        test r13d, r13d
0022BF54  0F 85 57 04 00 00               jne 0x14022c3b1
0022BF5A  48 C1 EB 09                     shr rbx, 9
0022BF5E  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0022BF68  48 23 D8                        and rbx, rax
0022BF6B  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0022BF75  48 8B C0                        mov rax, rax
0022BF78  48 03 D8                        add rbx, rax
0022BF7B  48 8B 05 FE 48 DE FF            mov rax, qword ptr [rip - 0x21b702]
0022BF82  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
0022BF8A  48 89 03                        mov qword ptr [rbx], rax
0022BF8D  45 85 ED                        test r13d, r13d
0022BF90  0F 84 55 06 00 00               je 0x14022c5eb
0022BF96  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
0022BF9E  E8 4D A8 11 00                  call 0x1403467f0
0022BFA3  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
0022BFAB  48 8D 04 40                     lea rax, [rax + rax*2]
0022BFAF  48 C1 E0 04                     shl rax, 4
0022BFB3  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
0022BFBD  48 8B C9                        mov rcx, rcx
0022BFC0  48 03 C1                        add rax, rcx
0022BFC3  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
0022BFCB  48 8B 8C 24 28 01 00 00         mov rcx, qword ptr [rsp + 0x128]
0022BFD3  8B 09                           mov ecx, dword ptr [rcx]
0022BFD5  83 E1 1F                        and ecx, 0x1f
0022BFD8  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
0022BFDD  49 89 4C 24 30                  mov qword ptr [r12 + 0x30], rcx
0022BFE2  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
0022BFEA  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
0022BFEE  49 89 4C 24 18                  mov qword ptr [r12 + 0x18], rcx
0022BFF3  48 8B 4A 18                     mov rcx, qword ptr [rdx + 0x18]
0022BFF7  49 89 4C 24 40                  mov qword ptr [r12 + 0x40], rcx
0022BFFC  33 DB                           xor ebx, ebx
0022BFFE  4D 85 D2                        test r10, r10
0022C001  0F 84 5C 05 00 00               je 0x14022c563
0022C007  21 9C 24 A0 00 00 00            and dword ptr [rsp + 0xa0], ebx
0022C00E  44 8D 6B 01                     lea r13d, [rbx + 1]
0022C012  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
0022C019  0F 82 69 04 00 00               jb 0x14022c488
0022C01F  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
0022C023  48 B9 FF FF FF FF FF FF FF 3F   movabs rcx, 0x3fffffffffffffff
0022C02D  48 23 C1                        and rax, rcx
0022C030  49 3B C5                        cmp rax, r13
0022C033  0F 85 3A 04 00 00               jne 0x14022c473
0022C039  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
0022C041  8B 00                           mov eax, dword ptr [rax]
0022C043  66 41 3B C5                     cmp ax, r13w
0022C047  0F 85 26 04 00 00               jne 0x14022c473
0022C04D  33 D2                           xor edx, edx
0022C04F  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
0022C054  44 8D 7A 05                     lea r15d, [rdx + 5]
0022C058  4C 39 64 24 40                  cmp qword ptr [rsp + 0x40], r12
0022C05D  0F 85 0C 09 00 00               jne 0x14022c96f
0022C063  85 D2                           test edx, edx
0022C065  0F 85 93 05 00 00               jne 0x14022c5fe
0022C06B  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0022C070  49 3B C4                        cmp rax, r12
0022C073  74 0E                           je 0x14022c083
0022C075  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0022C07A  4C 01 68 28                     add qword ptr [rax + 0x28], r13
0022C07E  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0022C083  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
0022C088  85 DB                           test ebx, ebx
0022C08A  0F 88 4E 06 00 00               js 0x14022c6de
0022C090  4D 89 6C 24 38                  mov qword ptr [r12 + 0x38], r13
0022C095  45 33 E4                        xor r12d, r12d
0022C098  48 39 44 24 60                  cmp qword ptr [rsp + 0x60], rax
0022C09D  41 0F 95 C4                     setne r12b
0022C0A1  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
0022C0A6  48 85 D2                        test rdx, rdx
0022C0A9  0F 85 32 03 00 00               jne 0x14022c3e1
0022C0AF  21 54 24 50                     and dword ptr [rsp + 0x50], edx
0022C0B3  83 64 24 60 00                  and dword ptr [rsp + 0x60], 0
0022C0B8  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
0022C0C0  F0 48 0F BA 6A 18 3F            lock bts qword ptr [rdx + 0x18], 0x3f
0022C0C7  0F 82 56 03 00 00               jb 0x14022c423
0022C0CD  48 8B 42 18                     mov rax, qword ptr [rdx + 0x18]
0022C0D1  48 8D 48 01                     lea rcx, [rax + 1]
0022C0D5  4C 8B C1                        mov r8, rcx
0022C0D8  4C 33 C0                        xor r8, rax
0022C0DB  48 B8 00 00 00 00 00 00 00 C0   movabs rax, 0xc000000000000000
0022C0E5  4C 23 C0                        and r8, rax
0022C0E8  4C 33 C1                        xor r8, rcx
0022C0EB  4C 89 42 18                     mov qword ptr [rdx + 0x18], r8
0022C0EF  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0022C0F9  F0 48 21 42 18                  lock and qword ptr [rdx + 0x18], rax
0022C0FE  41 8B D4                        mov edx, r12d
0022C101  49 8B CE                        mov rcx, r14
0022C104  E8 3F 34 00 00                  call 0x14022f548
0022C109  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0022C10E  83 64 24 68 00                  and dword ptr [rsp + 0x68], 0
0022C113  4C 8B B4 24 C0 00 00 00         mov r14, qword ptr [rsp + 0xc0]
0022C11B  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
0022C122  0F 82 23 03 00 00               jb 0x14022c44b
0022C128  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
0022C130  8B 00                           mov eax, dword ptr [rax]
0022C132  C1 E8 10                        shr eax, 0x10
0022C135  0F B6 D0                        movzx edx, al
0022C138  C1 EA 06                        shr edx, 6
0022C13B  45 8B C5                        mov r8d, r13d
0022C13E  49 8B CE                        mov rcx, r14
0022C141  E8 EA 6C 10 00                  call 0x140332e30
0022C146  4C 8B B4 24 F0 00 00 00         mov r14, qword ptr [rsp + 0xf0]
0022C14E  49 8B D6                        mov rdx, r14
0022C151  48 8B 9C 24 C0 00 00 00         mov rbx, qword ptr [rsp + 0xc0]
0022C159  48 8B CB                        mov rcx, rbx
0022C15C  E8 0F 65 08 00                  call 0x1402b2670
0022C161  48 8B CB                        mov rcx, rbx
0022C164  E8 87 65 0F 00                  call 0x1403226f0
0022C169  41 3B C7                        cmp eax, r15d
0022C16C  73 21                           jae 0x14022c18f
0022C16E  48 8B 84 24 80 01 00 00         mov rax, qword ptr [rsp + 0x180]
0022C176  8B 00                           mov eax, dword ptr [rax]
0022C178  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0022C17C  C1 E8 18                        shr eax, 0x18
0022C17F  24 FD                           and al, 0xfd
0022C181  41 0A C7                        or al, r15b
0022C184  88 44 24 33                     mov byte ptr [rsp + 0x33], al
0022C188  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
0022C18C  89 43 20                        mov dword ptr [rbx + 0x20], eax
0022C18F  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
0022C197  48 89 43 08                     mov qword ptr [rbx + 8], rax
0022C19B  48 8B 43 28                     mov rax, qword ptr [rbx + 0x28]
0022C19F  48 B9 00 00 00 00 00 00 00 80   movabs rcx, 0x8000000000000000
0022C1A9  48 0B C1                        or rax, rcx
0022C1AC  48 89 43 28                     mov qword ptr [rbx + 0x28], rax
0022C1B0  48 8B 94 24 E0 00 00 00         mov rdx, qword ptr [rsp + 0xe0]
0022C1B8  48 8B CB                        mov rcx, rbx
0022C1BB  E8 00 7E 13 00                  call 0x140363fc0
0022C1C0  48 8B 8C 24 88 01 00 00         mov rcx, qword ptr [rsp + 0x188]
0022C1C8  E8 3B 31 00 00                  call 0x14022f308
0022C1CD  48 83 7C 24 38 00               cmp qword ptr [rsp + 0x38], 0
0022C1D3  0F 84 3F 04 00 00               je 0x14022c618
0022C1D9  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
0022C1DE  48 8B CB                        mov rcx, rbx
0022C1E1  E8 3A 31 00 00                  call 0x14022f320
0022C1E6  49 BC 00 00 00 00 00 00 00 40   movabs r12, 0x4000000000000000
0022C1F0  48 8B 94 24 B8 00 00 00         mov rdx, qword ptr [rsp + 0xb8]
0022C1F8  41 BF 18 00 00 00               mov r15d, 0x18
0022C1FE  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0022C208  F0 48 21 43 18                  lock and qword ptr [rbx + 0x18], rax
0022C20D  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
0022C215  48 3B 84 24 08 01 00 00         cmp rax, qword ptr [rsp + 0x108]
0022C21D  75 10                           jne 0x14022c22f
0022C21F  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
0022C223  C0 E8 02                        shr al, 2
0022C226  41 84 C5                        test r13b, al
0022C229  0F 85 6F 04 00 00               jne 0x14022c69e
0022C22F  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0022C234  48 85 C9                        test rcx, rcx
0022C237  0F 84 7C 02 00 00               je 0x14022c4b9
0022C23D  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
0022C245  48 C1 E0 0C                     shl rax, 0xc
0022C249  48 8B D8                        mov rbx, rax
0022C24C  48 33 DF                        xor rbx, rdi
0022C24F  48 BA FF 0F 00 00 00 00 F0 FF   movabs rdx, 0xfff0000000000fff
0022C259  48 23 DA                        and rbx, rdx
0022C25C  48 33 D8                        xor rbx, rax
0022C25F  8B 41 14                        mov eax, dword ptr [rcx + 0x14]
0022C262  83 C8 40                        or eax, 0x40
0022C265  89 41 14                        mov dword ptr [rcx + 0x14], eax
0022C268  48 0F BA E3 0B                  bt rbx, 0xb
0022C26D  73 10                           jae 0x14022c27f
0022C26F  48 0F BA F3 0B                  btr rbx, 0xb
0022C274  48 0F BA EB 09                  bts rbx, 9
0022C279  83 C8 20                        or eax, 0x20
0022C27C  89 41 14                        mov dword ptr [rcx + 0x14], eax
0022C27F  45 33 C0                        xor r8d, r8d
0022C282  48 8B D3                        mov rdx, rbx
0022C285  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
0022C28A  E8 D9 9D 14 00                  call 0x140376068
0022C28F  48 89 9C 24 30 01 00 00         mov qword ptr [rsp + 0x130], rbx
0022C297  48 0F BA 25 E8 A7 D9 00 24      bt qword ptr [rip + 0xd9a7e8], 0x24
0022C2A0  0F 82 4E 04 00 00               jb 0x14022c6f4
0022C2A6  48 8B BC 24 98 00 00 00         mov rdi, qword ptr [rsp + 0x98]
0022C2AE  48 89 1F                        mov qword ptr [rdi], rbx
0022C2B1  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
0022C2B5  49 0B C4                        or rax, r12
0022C2B8  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
0022C2BC  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
0022C2C4  8B 00                           mov eax, dword ptr [rax]
0022C2C6  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0022C2CA  C1 E8 10                        shr eax, 0x10
0022C2CD  0C 07                           or al, 7
0022C2CF  88 44 24 32                     mov byte ptr [rsp + 0x32], al
0022C2D3  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
0022C2D7  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
0022C2DB  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0022C2E5  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
0022C2EA  48 8B 84 24 C8 01 00 00         mov rax, qword ptr [rsp + 0x1c8]
0022C2F2  48 8B 18                        mov rbx, qword ptr [rax]
0022C2F5  48 81 E3 00 F0 FF FF            and rbx, 0xfffffffffffff000
0022C2FC  4C 89 30                        mov qword ptr [rax], r14
0022C2FF  45 33 C9                        xor r9d, r9d
0022C302  4D 8B C5                        mov r8, r13
0022C305  48 8B D3                        mov rdx, rbx
0022C308  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0022C30D  E8 5E 73 06 00                  call 0x140293670
0022C312  4C 8B B4 24 B0 00 00 00         mov r14, qword ptr [rsp + 0xb0]
0022C31A  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
0022C321  A8 0F                           test al, 0xf
0022C323  75 0B                           jne 0x14022c330
0022C325  45 33 C0                        xor r8d, r8d
0022C328  48 8B D3                        mov rdx, rbx
0022C32B  E8 A8 76 06 00                  call 0x1402939d8
0022C330  45 33 C9                        xor r9d, r9d
0022C333  49 83 C8 FF                     or r8, 0xffffffffffffffff
0022C337  48 8B D3                        mov rdx, rbx
0022C33A  49 8B CE                        mov rcx, r14
0022C33D  E8 0E 5F 13 00                  call 0x140362250
0022C342  83 7C 24 50 00                  cmp dword ptr [rsp + 0x50], 0
0022C347  0F 85 E3 06 00 00               jne 0x14022ca30
0022C34D  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0022C352  48 85 D2                        test rdx, rdx
0022C355  0F 85 29 07 00 00               jne 0x14022ca84
0022C35B  48 8B 84 24 98 01 00 00         mov rax, qword ptr [rsp + 0x198]
0022C363  48 83 20 00                     and qword ptr [rax], 0
0022C367  48 8B 84 24 A0 01 00 00         mov rax, qword ptr [rsp + 0x1a0]
0022C36F  48 83 20 00                     and qword ptr [rax], 0
0022C373  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
0022C378  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
0022C380  E8 0F 9D 03 00                  call 0x140266094
0022C385  33 C0                           xor eax, eax
0022C387  48 8B 8C 24 D8 01 00 00         mov rcx, qword ptr [rsp + 0x1d8]
0022C38F  48 33 CC                        xor rcx, rsp
0022C392  E8 A9 02 48 00                  call 0x1406ac640
0022C397  48 8B 9C 24 28 02 00 00         mov rbx, qword ptr [rsp + 0x228]
0022C39F  48 81 C4 E0 01 00 00            add rsp, 0x1e0
0022C3A6  41 5F                           pop r15
0022C3A8  41 5E                           pop r14
0022C3AA  41 5D                           pop r13
0022C3AC  41 5C                           pop r12
0022C3AE  5F                              pop rdi
0022C3AF  C3                              ret
0022C3B0  CC                              int3
0022C3B1  4D 8B 58 08                     mov r11, qword ptr [r8 + 8]
0022C3B5  48 8B CB                        mov rcx, rbx
0022C3B8  E8 03 6A 20 00                  call 0x140432dc0
0022C3BD  49 3B C3                        cmp rax, r11
0022C3C0  0F 85 08 06 00 00               jne 0x14022c9ce
0022C3C6  48 8B 05 43 3B C0 00            mov rax, qword ptr [rip + 0xc03b43]
0022C3CD  49 39 40 18                     cmp qword ptr [r8 + 0x18], rax
0022C3D1  0F 84 FF 05 00 00               je 0x14022c9d6
0022C3D7  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
0022C3DC  E9 79 FB FF FF                  jmp 0x14022bf5a
0022C3E1  48 8B 05 1C A7 D9 00            mov rax, qword ptr [rip + 0xd9a71c]
0022C3E8  A9 01 00 00 08                  test eax, 0x8000001
0022C3ED  B9 00 00 00 00                  mov ecx, 0
0022C3F2  0F 95 C1                        setne cl
0022C3F5  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
0022C3F9  A9 01 00 00 08                  test eax, 0x8000001
0022C3FE  0F 85 00 06 00 00               jne 0x14022ca04
0022C404  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0022C409  48 8B 38                        mov rdi, qword ptr [rax]
0022C40C  40 F6 C7 42                     test dil, 0x42
0022C410  0F 84 9D FC FF FF               je 0x14022c0b3
0022C416  48 83 E7 BD                     and rdi, 0xffffffffffffffbd
0022C41A  83 4A 14 0A                     or dword ptr [rdx + 0x14], 0xa
0022C41E  E9 90 FC FF FF                  jmp 0x14022c0b3
0022C423  8B 5C 24 60                     mov ebx, dword ptr [rsp + 0x60]
0022C427  41 03 DD                        add ebx, r13d
0022C42A  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
0022C42E  85 1D 78 8E D9 00               test dword ptr [rip + 0xd98e78], ebx
0022C434  0F 84 8A 04 00 00               je 0x14022c8c4
0022C43A  F3 90                           pause
0022C43C  48 8B 42 18                     mov rax, qword ptr [rdx + 0x18]
0022C440  48 85 C0                        test rax, rax
0022C443  0F 89 77 FC FF FF               jns 0x14022c0c0
0022C449  EB D8                           jmp 0x14022c423
0022C44B  8B 5C 24 68                     mov ebx, dword ptr [rsp + 0x68]
0022C44F  41 03 DD                        add ebx, r13d
0022C452  89 5C 24 68                     mov dword ptr [rsp + 0x68], ebx
0022C456  85 1D 50 8E D9 00               test dword ptr [rip + 0xd98e50], ebx
0022C45C  0F 84 91 04 00 00               je 0x14022c8f3
0022C462  F3 90                           pause
0022C464  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
0022C468  48 85 C0                        test rax, rax
0022C46B  0F 89 AA FC FF FF               jns 0x14022c11b
0022C471  EB D8                           jmp 0x14022c44b
0022C473  BB 18 00 00 C0                  mov ebx, 0xc0000018
0022C478  41 BF 05 00 00 00               mov r15d, 5
0022C47E  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0022C483  E9 00 FC FF FF                  jmp 0x14022c088
0022C488  44 8B BC 24 A0 00 00 00         mov r15d, dword ptr [rsp + 0xa0]
0022C490  45 03 FD                        add r15d, r13d
0022C493  44 89 BC 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r15d
0022C49B  44 85 3D 0A 8E D9 00            test dword ptr [rip + 0xd98e0a], r15d
0022C4A2  0F 84 9F 04 00 00               je 0x14022c947
0022C4A8  F3 90                           pause
0022C4AA  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
0022C4AE  48 85 C0                        test rax, rax
0022C4B1  0F 89 5B FB FF FF               jns 0x14022c012
0022C4B7  EB CF                           jmp 0x14022c488
0022C4B9  49 8B 5E 28                     mov rbx, qword ptr [r14 + 0x28]
0022C4BD  4A 8B 04 3A                     mov rax, qword ptr [rdx + r15]
0022C4C1  48 B9 00 00 00 00 00 00 00 C0   movabs rcx, 0xc000000000000000
0022C4CB  48 23 C1                        and rax, rcx
0022C4CE  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
0022C4D2  48 8B 94 24 D0 00 00 00         mov rdx, qword ptr [rsp + 0xd0]
0022C4DA  49 8B CE                        mov rcx, r14
0022C4DD  E8 5E D9 08 00                  call 0x1402b9e40
0022C4E2  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0022C4EC  48 8B 94 24 B8 00 00 00         mov rdx, qword ptr [rsp + 0xb8]
0022C4F4  F0 4A 21 04 3A                  lock and qword ptr [rdx + r15], rax
0022C4F9  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
0022C503  48 23 D8                        and rbx, rax
0022C506  48 8D 0C 5B                     lea rcx, [rbx + rbx*2]
0022C50A  48 C1 E1 04                     shl rcx, 4
0022C50E  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0022C518  48 8B C0                        mov rax, rax
0022C51B  48 03 C8                        add rcx, rax
0022C51E  BA 02 00 00 00                  mov edx, 2
0022C523  E8 2C 63 07 00                  call 0x1402a2854
0022C528  E9 20 FE FF FF                  jmp 0x14022c34d
0022C52D  49 8B CF                        mov rcx, r15
0022C530  48 C1 F9 04                     sar rcx, 4
0022C534  49 B8 AB AA AA AA AA AA AA AA   movabs r8, 0xaaaaaaaaaaaaaaab
0022C53E  49 0F AF C8                     imul rcx, r8
0022C542  E8 29 7A 13 00                  call 0x140363f70
0022C547  48 8B F8                        mov rdi, rax
0022C54A  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
0022C552  49 8D 41 48                     lea rax, [r9 + 0x48]
0022C556  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
0022C55E  E9 B7 F8 FF FF                  jmp 0x14022be1a
0022C563  33 D2                           xor edx, edx
0022C565  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
0022C56A  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
0022C56F  44 8D 7A 05                     lea r15d, [rdx + 5]
0022C573  4D 3B EC                        cmp r13, r12
0022C576  0F 85 22 04 00 00               jne 0x14022c99e
0022C57C  85 D2                           test edx, edx
0022C57E  0F 85 45 01 00 00               jne 0x14022c6c9
0022C584  4D 3B EC                        cmp r13, r12
0022C587  41 BD 01 00 00 00               mov r13d, 1
0022C58D  74 09                           je 0x14022c598
0022C58F  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0022C594  4C 01 68 28                     add qword ptr [rax + 0x28], r13
0022C598  33 D2                           xor edx, edx
0022C59A  49 8B CE                        mov rcx, r14
0022C59D  E8 EE AF 05 00                  call 0x140287590
0022C5A2  A8 03                           test al, 3
0022C5A4  0F 84 D4 FA FF FF               je 0x14022c07e
0022C5AA  21 5C 24 70                     and dword ptr [rsp + 0x70], ebx
0022C5AE  33 D2                           xor edx, edx
0022C5B0  49 8B CE                        mov rcx, r14
0022C5B3  E8 9C 93 14 00                  call 0x140375954
0022C5B8  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
0022C5BD  4C 89 6A 38                     mov qword ptr [rdx + 0x38], r13
0022C5C1  48 8D 44 24 70                  lea rax, [rsp + 0x70]
0022C5C6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0022C5CB  41 B9 04 00 00 00               mov r9d, 4
0022C5D1  4C 8B 84 24 78 01 00 00         mov r8, qword ptr [rsp + 0x178]
0022C5D9  48 8B 94 24 B0 00 00 00         mov rdx, qword ptr [rsp + 0xb0]
0022C5E1  49 8B CC                        mov rcx, r12
0022C5E4  E8 A3 F4 FF FF                  call 0x14022ba8c
0022C5E9  EB 23                           jmp 0x14022c60e
0022C5EB  4D 85 D2                        test r10, r10
0022C5EE  0F 84 FC 03 00 00               je 0x14022c9f0
0022C5F4  B8 18 00 00 C0                  mov eax, 0xc0000018
0022C5F9  E9 89 FD FF FF                  jmp 0x14022c387
0022C5FE  49 8B CC                        mov rcx, r12
0022C601  E8 56 05 00 00                  call 0x14022cb5c
0022C606  85 C0                           test eax, eax
0022C608  0F 85 5D FA FF FF               jne 0x14022c06b
0022C60E  BB 18 00 00 C0                  mov ebx, 0xc0000018
0022C613  E9 66 FA FF FF                  jmp 0x14022c07e
0022C618  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
0022C61C  48 B9 00 00 00 00 00 00 00 C0   movabs rcx, 0xc000000000000000
0022C626  48 23 C1                        and rax, rcx
0022C629  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
0022C62D  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
0022C635  48 83 20 00                     and qword ptr [rax], 0
0022C639  48 89 BC 24 28 01 00 00         mov qword ptr [rsp + 0x128], rdi
0022C641  48 89 38                        mov qword ptr [rax], rdi
0022C644  48 8B C8                        mov rcx, rax
0022C647  E8 94 87 06 00                  call 0x140294de0
0022C64C  48 0F BA E8 0B                  bts rax, 0xb
0022C651  48 8B D0                        mov rdx, rax
0022C654  49 8B CE                        mov rcx, r14
0022C657  E8 6C 48 28 00                  call 0x1404b0ec8
0022C65C  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
0022C660  49 BC 00 00 00 00 00 00 00 40   movabs r12, 0x4000000000000000
0022C66A  49 0B C4                        or rax, r12
0022C66D  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
0022C671  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
0022C676  48 8B CB                        mov rcx, rbx
0022C679  E8 A2 2C 00 00                  call 0x14022f320
0022C67E  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
0022C686  48 8B CB                        mov rcx, rbx
0022C689  E8 B2 D7 08 00                  call 0x1402b9e40
0022C68E  49 8B D6                        mov rdx, r14
0022C691  48 89 94 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdx
0022C699  E9 5A FB FF FF                  jmp 0x14022c1f8
0022C69E  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0022C6A2  48 83 E0 FB                     and rax, 0xfffffffffffffffb
0022C6A6  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
0022C6AA  48 83 7C 24 58 00               cmp qword ptr [rsp + 0x58], 0
0022C6B0  0F 84 79 FB FF FF               je 0x14022c22f
0022C6B6  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
0022C6BB  48 83 E0 FB                     and rax, 0xfffffffffffffffb
0022C6BF  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0022C6C4  E9 66 FB FF FF                  jmp 0x14022c22f
0022C6C9  49 8B CC                        mov rcx, r12
0022C6CC  E8 8B 04 00 00                  call 0x14022cb5c
0022C6D1  85 C0                           test eax, eax
0022C6D3  0F 85 AB FE FF FF               jne 0x14022c584
0022C6D9  BB 18 00 00 C0                  mov ebx, 0xc0000018
0022C6DE  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0022C6E8  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
0022C6ED  8B C3                           mov eax, ebx
0022C6EF  E9 93 FC FF FF                  jmp 0x14022c387
0022C6F4  F6 C3 20                        test bl, 0x20
0022C6F7  0F 85 A9 FB FF FF               jne 0x14022c2a6
0022C6FD  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0022C707  48 8B C0                        mov rax, rax
0022C70A  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
0022C714  48 03 C1                        add rax, rcx
0022C717  48 8B BC 24 98 00 00 00         mov rdi, qword ptr [rsp + 0x98]
0022C71F  48 3B F8                        cmp rdi, rax
0022C722  0F 82 86 FB FF FF               jb 0x14022c2ae
0022C728  41 B8 80 00 00 00               mov r8d, 0x80
0022C72E  48 8B D3                        mov rdx, rbx
0022C731  48 8B CF                        mov rcx, rdi
0022C734  E8 47 66 06 00                  call 0x140292d80
0022C739  E9 70 FB FF FF                  jmp 0x14022c2ae
0022C73E  83 A4 24 80 00 00 00 00         and dword ptr [rsp + 0x80], 0
0022C746  F0 49 0F BA 6E 18 3F            lock bts qword ptr [r14 + 0x18], 0x3f
0022C74D  0F 82 C7 01 00 00               jb 0x14022c91a
0022C753  48 8B 84 24 20 01 00 00         mov rax, qword ptr [rsp + 0x120]
0022C75B  48 8B 00                        mov rax, qword ptr [rax]
0022C75E  48 8B 00                        mov rax, qword ptr [rax]
0022C761  41 84 C5                        test r13b, al
0022C764  0F 84 5C 02 00 00               je 0x14022c9c6
0022C76A  44 8B 4C 24 50                  mov r9d, dword ptr [rsp + 0x50]
0022C76F  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
0022C774  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
0022C779  49 8B CE                        mov rcx, r14
0022C77C  E8 C7 D9 FF FF                  call 0x14022a148
0022C781  85 C0                           test eax, eax
0022C783  0F 84 3D 02 00 00               je 0x14022c9c6
0022C789  4C 8B 8C 24 B0 00 00 00         mov r9, qword ptr [rsp + 0xb0]
0022C791  4D 8B C6                        mov r8, r14
0022C794  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
0022C798  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
0022C7A0  E8 57 DA FF FF                  call 0x14022a1fc
0022C7A5  85 C0                           test eax, eax
0022C7A7  0F 84 19 02 00 00               je 0x14022c9c6
0022C7AD  44 8B 84 24 88 00 00 00         mov r8d, dword ptr [rsp + 0x88]
0022C7B5  49 8B D4                        mov rdx, r12
0022C7B8  48 8B CB                        mov rcx, rbx
0022C7BB  E8 30 D9 48 00                  call 0x1406ba0f0
0022C7C0  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
0022C7C5  4C 8B 84 24 90 00 00 00         mov r8, qword ptr [rsp + 0x90]
0022C7CD  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
0022C7D2  48 B9 F8 FF FF FF 7F 00 00 00   movabs rcx, 0x7ffffffff8
0022C7DC  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
0022C7E6  E9 38 F7 FF FF                  jmp 0x14022bf23
0022C7EB  45 33 ED                        xor r13d, r13d
0022C7EE  48 B9 F8 FF FF FF 7F 00 00 00   movabs rcx, 0x7ffffffff8
0022C7F8  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
0022C802  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
0022C80A  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
0022C812  4C 8B B4 24 F0 00 00 00         mov r14, qword ptr [rsp + 0xf0]
0022C81A  48 8B 84 24 58 01 00 00         mov rax, qword ptr [rsp + 0x158]
0022C822  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
0022C82A  48 8B BC 24 E8 00 00 00         mov rdi, qword ptr [rsp + 0xe8]
0022C832  4C 8B A4 24 60 01 00 00         mov r12, qword ptr [rsp + 0x160]
0022C83A  48 8B 9C 24 68 01 00 00         mov rbx, qword ptr [rsp + 0x168]
0022C842  48 8B 84 24 70 01 00 00         mov rax, qword ptr [rsp + 0x170]
0022C84A  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
0022C852  48 8B 84 24 90 01 00 00         mov rax, qword ptr [rsp + 0x190]
0022C85A  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
0022C862  48 8B 94 24 38 01 00 00         mov rdx, qword ptr [rsp + 0x138]
0022C86A  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
0022C86F  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
0022C877  48 89 84 24 08 01 00 00         mov qword ptr [rsp + 0x108], rax
0022C87F  48 8B 84 24 48 01 00 00         mov rax, qword ptr [rsp + 0x148]
0022C887  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
0022C88F  4C 8B BC 24 50 01 00 00         mov r15, qword ptr [rsp + 0x150]
0022C897  4C 8B 84 24 10 01 00 00         mov r8, qword ptr [rsp + 0x110]
0022C89F  4C 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], r8
0022C8A7  49 8B D6                        mov rdx, r14
0022C8AA  48 89 94 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdx
0022C8B2  4C 8B 94 24 E0 00 00 00         mov r10, qword ptr [rsp + 0xe0]
0022C8BA  4C 89 54 24 38                  mov qword ptr [rsp + 0x38], r10
0022C8BF  E9 5F F6 FF FF                  jmp 0x14022bf23
0022C8C4  8B 05 EE A1 D9 00               mov eax, dword ptr [rip + 0xd9a1ee]
0022C8CA  A8 40                           test al, 0x40
0022C8CC  0F 84 68 FB FF FF               je 0x14022c43a
0022C8D2  E8 B9 2B 0E 00                  call 0x14030f490
0022C8D7  84 C0                           test al, al
0022C8D9  0F 84 44 01 00 00               je 0x14022ca23
0022C8DF  8B CB                           mov ecx, ebx
0022C8E1  E8 7A 2B 0E 00                  call 0x14030f460
0022C8E6  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
0022C8EE  E9 49 FB FF FF                  jmp 0x14022c43c
0022C8F3  8B 05 BF A1 D9 00               mov eax, dword ptr [rip + 0xd9a1bf]
0022C8F9  A8 40                           test al, 0x40
0022C8FB  0F 84 61 FB FF FF               je 0x14022c462
0022C901  E8 8A 2B 0E 00                  call 0x14030f490
0022C906  84 C0                           test al, al
0022C908  0F 84 54 FB FF FF               je 0x14022c462
0022C90E  8B CB                           mov ecx, ebx
0022C910  E8 4B 2B 0E 00                  call 0x14030f460
0022C915  E9 4A FB FF FF                  jmp 0x14022c464
0022C91A  44 8B BC 24 80 00 00 00         mov r15d, dword ptr [rsp + 0x80]
0022C922  41 FF C7                        inc r15d
0022C925  44 89 BC 24 80 00 00 00         mov dword ptr [rsp + 0x80], r15d
0022C92D  44 85 3D 78 89 D9 00            test dword ptr [rip + 0xd98978], r15d
0022C934  74 4B                           je 0x14022c981
0022C936  F3 90                           pause
0022C938  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
0022C93C  48 85 C0                        test rax, rax
0022C93F  0F 89 01 FE FF FF               jns 0x14022c746
0022C945  EB D3                           jmp 0x14022c91a
0022C947  8B 05 6B A1 D9 00               mov eax, dword ptr [rip + 0xd9a16b]
0022C94D  A8 40                           test al, 0x40
0022C94F  0F 84 53 FB FF FF               je 0x14022c4a8
0022C955  E8 36 2B 0E 00                  call 0x14030f490
0022C95A  84 C0                           test al, al
0022C95C  0F 84 46 FB FF FF               je 0x14022c4a8
0022C962  41 8B CF                        mov ecx, r15d
0022C965  E8 F6 2A 0E 00                  call 0x14030f460
0022C96A  E9 3B FB FF FF                  jmp 0x14022c4aa
0022C96F  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0022C974  48 39 50 28                     cmp qword ptr [rax + 0x28], rdx
0022C978  41 0F 44 D7                     cmove edx, r15d
0022C97C  E9 E2 F6 FF FF                  jmp 0x14022c063
0022C981  8B 05 31 A1 D9 00               mov eax, dword ptr [rip + 0xd9a131]
0022C987  A8 40                           test al, 0x40
0022C989  74 AB                           je 0x14022c936
0022C98B  E8 00 2B 0E 00                  call 0x14030f490
0022C990  84 C0                           test al, al
0022C992  74 A2                           je 0x14022c936
0022C994  41 8B CF                        mov ecx, r15d
0022C997  E8 C4 2A 0E 00                  call 0x14030f460
0022C99C  EB 9A                           jmp 0x14022c938
0022C99E  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0022C9A3  48 39 50 28                     cmp qword ptr [rax + 0x28], rdx
0022C9A7  41 0F 44 D7                     cmove edx, r15d
0022C9AB  E9 CC FB FF FF                  jmp 0x14022c57c
0022C9B0  41 B8 10 00 00 00               mov r8d, 0x10
0022C9B6  41 8B D7                        mov edx, r15d
0022C9B9  49 8B CD                        mov rcx, r13
0022C9BC  E8 0B 65 10 00                  call 0x140332ecc
0022C9C1  E9 EC F4 FF FF                  jmp 0x14022beb2
0022C9C6  45 33 ED                        xor r13d, r13d
0022C9C9  E9 2F F5 FF FF                  jmp 0x14022befd
0022C9CE  45 33 ED                        xor r13d, r13d
0022C9D1  E9 01 FA FF FF                  jmp 0x14022c3d7
0022C9D6  4C 8B C3                        mov r8, rbx
0022C9D9  49 8B D3                        mov rdx, r11
0022C9DC  49 8B CF                        mov rcx, r15
0022C9DF  E8 64 3E 23 00                  call 0x140460848
0022C9E4  F7 D8                           neg eax
0022C9E6  1B C9                           sbb ecx, ecx
0022C9E8  44 23 E9                        and r13d, ecx
0022C9EB  E9 E7 F9 FF FF                  jmp 0x14022c3d7
0022C9F0  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0022C9FA  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
0022C9FF  E9 F0 FB FF FF                  jmp 0x14022c5f4
0022CA04  48 8D 94 24 A8 01 00 00         lea rdx, [rsp + 0x1a8]
0022CA0C  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
0022CA14  E8 A7 00 0F 00                  call 0x14031cac0
0022CA19  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
0022CA1E  E9 E1 F9 FF FF                  jmp 0x14022c404
0022CA23  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
0022CA2B  E9 0A FA FF FF                  jmp 0x14022c43a
0022CA30  48 89 BC 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], rdi
0022CA38  48 8D 84 24 A8 01 00 00         lea rax, [rsp + 0x1a8]
0022CA40  48 89 84 24 C8 01 00 00         mov qword ptr [rsp + 0x1c8], rax
0022CA48  C7 84 24 D0 01 00 00 20 00 00 00  mov dword ptr [rsp + 0x1d0], 0x20
0022CA53  83 A4 24 D4 01 00 00 00         and dword ptr [rsp + 0x1d4], 0
0022CA5B  41 B9 7A 02 00 00               mov r9d, 0x27a
0022CA61  C7 44 24 20 04 1B 50 11         mov dword ptr [rsp + 0x20], 0x11501b04
0022CA69  41 B8 01 00 00 28               mov r8d, 0x28000001
0022CA6F  41 8B D5                        mov edx, r13d
0022CA72  48 8D 8C 24 C8 01 00 00         lea rcx, [rsp + 0x1c8]
0022CA7A  E8 D1 88 00 00                  call 0x140235350
0022CA7F  E9 C9 F8 FF FF                  jmp 0x14022c34d
0022CA84  45 8B C5                        mov r8d, r13d
0022CA87  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0022CA8C  E8 3F 75 05 00                  call 0x140283fd0
0022CA91  E9 C5 F8 FF FF                  jmp 0x14022c35b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCombineInitialInstance(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m180;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned int v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int8 v_stack_m1D5;
    unsigned __int8 v_stack_m1D6;
    unsigned int v_stack_m1D8;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m40;
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
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p100;
    unsigned __int64 v_stack_p108;
    unsigned __int64 v_stack_p110;
    unsigned __int64 v_stack_p120;
    unsigned __int64 v_stack_p128;
    unsigned __int64 v_stack_p138;
    unsigned __int64 v_stack_p140;
    unsigned __int64 v_stack_p148;
    unsigned __int64 v_stack_p150;
    unsigned __int64 v_stack_p158;
    unsigned __int64 v_stack_p160;
    unsigned __int64 v_stack_p168;
    unsigned __int64 v_stack_p170;
    unsigned __int64 v_stack_p178;
    unsigned __int64 v_stack_p190;
    unsigned __int64 v_stack_p1A8;
    unsigned __int64 v_stack_p1C0;
    unsigned __int64 v_stack_p1C8;
    unsigned int v_stack_p1D0;
    unsigned int v_stack_p1D4;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned int v_stack_p80;
    unsigned int v_stack_p88;
    unsigned __int64 v_stack_p90;
    unsigned __int64 v_stack_p98;
    unsigned int v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pC0;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pE8;
    unsigned __int64 v_stack_pF0;

    *(unsigned __int64 *)(v_rsp + 32) = v_rbx;
    v_rsp = (v_rsp) - (480);
    result = (*(unsigned __int64 *)(v_rip + 12446486)) ^ (v_rsp);
    v_stack_m30 = result;
    v_stack_m1D0 = a3;
    v_stack_m178 = a2;
    v_stack_m1A0 = a1;
    v_stack_mB8 = a1;
    v_stack_mF8 = a2;
    v_stack_m128 = a3;
    *(unsigned __int64 *)(v_rsp - 96) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 80) = v_xmm0;
    v_stack_m70 = a1 + 296;
    v_stack_m1C0 = *(unsigned __int64 *)(a1 + 296);
    v_stack_mD0 = *(unsigned __int64 *)(a1 + 296);
    v_stack_m198 = *(unsigned __int64 *)(a1 + 296);
    v_stack_m68 = a1 + 304;
    v_stack_m148 = *(unsigned __int64 *)(a1 + 304);
    v_stack_m168 = *(unsigned __int64 *)(a1 + 304);
    v_stack_m130 = *(unsigned __int64 *)(a1);
    v_stack_m78 = *(unsigned __int64 *)(a1);
    v_stack_m1D8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 140)));
    v_stack_m158 = *(unsigned __int64 *)(a1 + 112);
    v_stack_m98 = *(unsigned __int64 *)(a1 + 112);
    v_stack_m100 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12600206) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 112) + 174) * 8);
    v_stack_mC8 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12600206) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 112) + 174) * 8);
    v_stack_m1C8 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12600206) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 112) + 174) * 8);
    v_stack_m138 = *(unsigned __int64 *)(a1 + 144);
    v_stack_mB0 = *(unsigned __int64 *)(a1 + 144);
    a1 = (*(unsigned __int64 *)(a1 + 144) + *(unsigned __int64 *)(a1 + 144) * 2) << (4);
    result = (v_rsp) + (a1);
    v_stack_m118 = result;
    v_stack_m150 = result;
    v_stack_mA8 = *(unsigned __int64 *)(a1 + 96);
    v_stack_m108 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1));
    v_stack_mC0 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1));
    v_stack_m1A8 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1));
    v_stack_mA0 = *(unsigned __int64 *)(a1 + 96) + 4096;
    v_stack_m40 = a2 + 16;
    a1 = (*(unsigned __int64 *)(a2 + 16)) >> (9);
    a1 = (a1) & (a2 + 16);
    a1 = (a1) + (a2 + 16);
    v_stack_m190 = a1;
    v_stack_mE0 = a2 + 32;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 32))) & (31));
    v_stack_m1B8 = (unsigned int)(a2);
    v_r15 = (*(unsigned __int64 *)(a1 + 304)) - (v_rsp);
    if (a3 == 0) goto loc_0022C52D;
    v_stack_m120 = *(unsigned __int64 *)(a1);
    a4 = 0;
    result = MiMapSinglePage(*(unsigned __int64 *)(a1 + 96), *(unsigned __int64 *)(a1 + 144), (unsigned int)(0xC0000010ULL), a4);
    v_stack_mE8 = 56;
loc_0022BE1A:
    result = (v_stack_m1C0) + (32);
    v_stack_m90 = result;
    v_stack_m170 = result;
    a2 = (result) & (*(unsigned __int64 *)(a1 + 96));
    v_stack_m110 = a2;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = v_xmm0;
    v_stack_m80 = *(unsigned __int64 *)(a1 + 304) + 16;
    result = MiSetOriginalPtePfnFromFreeList(*(unsigned __int64 *)(a1 + 304) + 16, a2, (unsigned int)(0xC0000010ULL), a4);
    v_r15 = (v_r15) >> (4);
    v_r15 = (v_r15) * ((unsigned int)(0xC0000010ULL));
    v_stack_m160 = v_r15;
    v_stack_m140 = result + 32;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 32))) >> (16));
    v_r15 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    v_stack_m88 = *(unsigned __int64 *)(a1 + 304) + 32;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 304) + 32))) >> (16));
    a1 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    if (((unsigned int)(a1)) != ((unsigned int)(v_r15))) goto loc_0022C9B0;
loc_0022BEB2:
    result = MiTranslateCacheAttribute((unsigned int)((unsigned int)(v_r15)), a2, (unsigned int)(0xC0000010ULL), a4);
    v_stack_m180 = (unsigned int)(result);
    a4 = 0;
    result = MiMapSinglePage(*(unsigned __int64 *)(a1 + 96) + 4096, v_stack_m160, (unsigned int)(0x40000010ULL), a4);
    if (v_stack_m1D0 == 0) goto loc_0022C73E;
    result = KeCopyPage(*(unsigned __int64 *)(a1 + 96) + 4096, *(unsigned __int64 *)(a1 + 96), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
loc_0022BEFD:
loc_0022BF23:
    v_r12 = *(unsigned __int64 *)(a1 + 96);
    if (v_stack_m1D0 != 0) {
        v_r12 = (*(unsigned __int64 *)(a1 + 96)) >> (9);
        v_r12 = (v_r12) & (*(unsigned __int64 *)(a1 + 96) + 4096);
        result = 0;
        v_r12 = (v_r12) + (result);
        result = *(unsigned __int64 *)(v_rip - 2209468);
        v_stack_mF0 = result;
        *(unsigned __int64 *)(v_r12) = result;
    }
    v_stack_m1B0 = *(unsigned __int64 *)(result + 16);
    if (1 != 0) goto loc_0022C3B1;
loc_0022BF5A:
    v_rbx = (*(unsigned __int64 *)(a1 + 96) + 4096) >> (9);
    v_rbx = (v_rbx) & (*(unsigned __int64 *)(result + 16));
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(result + 16));
    v_stack_mF8 = *(unsigned __int64 *)(v_rip - 2209538);
    *(unsigned __int64 *)(v_rbx) = *(unsigned __int64 *)(v_rip - 2209538);
    if (1 == 0) goto loc_0022C5EB;
    result = MiGetContainingPageTable(v_stack_m170, *(unsigned __int64 *)(a1 + 96), v_stack_m178, a4);
    v_stack_m128 = result;
    result = (result + result * 2) << (4);
    result = (result) + (v_stack_m170);
    v_stack_m180 = result;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mE0))) & (31));
    *(unsigned __int64 *)(v_stack_m1C0 + 48) = a1;
    *(unsigned __int64 *)(v_stack_m1C0 + 24) = *(unsigned __int64 *)(v_stack_m178 + 8);
    *(unsigned __int64 *)(v_stack_m1C0 + 64) = *(unsigned __int64 *)(v_stack_m178 + 24);
    v_rbx = 0;
    if (v_stack_m1D0 == 0) goto loc_0022C563;
loc_0022C012:
    if (condition_is_below) goto loc_0022C488;
    result = (*(unsigned __int64 *)(result + 24)) & (*(unsigned __int64 *)(v_stack_m178 + 24));
    if (result != (v_rbx + 1)) goto loc_0022C473;
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m140)))) != ((unsigned __int16)(v_rbx + 1))) goto loc_0022C473;
    a2 = 0;
    if (v_stack_m1C8 != v_stack_m1A8) goto loc_0022C96F;
loc_0022C063:
    if (0 != 0) goto loc_0022C5FE;
loc_0022C06B:
    if (v_stack_m1C8 == v_stack_m1A8) goto loc_0022C083;
loc_0022C07E:
loc_0022C083:
loc_0022C088:
    if (sign_flag) goto loc_0022C6DE;
    *(unsigned __int64 *)(v_stack_m1C0 + 56) = v_rbx + 1;
    v_r12 = 0;
    v_r12 = (v_stack_m1A8 != v_stack_m1C8) ? 1 : 0;
    if (v_stack_m1D0 != 0) goto loc_0022C3E1;
loc_0022C0B3:
loc_0022C0C0:
    if (condition_is_below) goto loc_0022C423;
    a3 = (*(unsigned __int64 *)(v_stack_m180 + 24) + 1) ^ (*(unsigned __int64 *)(v_stack_m180 + 24));
    a3 = (a3) & (*(unsigned __int64 *)(v_stack_m180 + 24));
    a3 = (a3) ^ (*(unsigned __int64 *)(v_stack_m180 + 24) + 1);
    *(unsigned __int64 *)(v_stack_m180 + 24) = a3;
    result = MiAbandonPrivatePfn(result, (unsigned int)((unsigned int)(v_r12)), a3, a4);
    v_stack_m1B0 = result;
loc_0022C11B:
    if (condition_is_below) goto loc_0022C44B;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m140))) >> (16));
    a2 = (unsigned int)(((unsigned __int8)(result)) >> (6));
    result = MiFinalizePageAttribute(v_stack_m148, a2, (unsigned int)((unsigned int)(v_rbx + 1)), a4);
    result = MiCopyPfnEntryEx(v_stack_m148, v_stack_m118, (unsigned int)((unsigned int)(v_rbx + 1)), a4);
    result = MiGetPfnPriority(v_stack_m148, v_stack_m118, (unsigned int)((unsigned int)(v_rbx + 1)), a4);
    if (((unsigned int)(result)) < ((unsigned int)(a2 + 5))) {
        result = v_stack_m88;
        result = *(unsigned int *)(result);
        v_stack_m1D8 = (unsigned int)(result);
        result = (unsigned int)((result) >> (24));
        result = (unsigned __int8)((result) & (253));
        result = (unsigned __int8)((result) | ((unsigned __int8)(a2 + 5)));
        v_stack_m1D5 = (unsigned __int8)(result);
        result = v_stack_m1D8;
        *(unsigned int *)(v_stack_m148 + 32) = (unsigned int)(result);
    }
    *(unsigned __int64 *)(v_stack_m148 + 8) = v_stack_m110;
    result = (*(unsigned __int64 *)(v_stack_m148 + 40)) | (v_stack_m148);
    *(unsigned __int64 *)(v_stack_m148 + 40) = result;
    result = MiSetPfnContainingFrame(v_stack_m148, v_stack_m128, (unsigned int)((unsigned int)(v_rbx + 1)), a4);
    result = MI_MAKE_PROTECT_WRITE_COPY(v_stack_m80, v_stack_m128, (unsigned int)((unsigned int)(v_rbx + 1)), a4);
    if (v_stack_m1D0 == 0) goto loc_0022C618;
    result = MiTransferPageFileOwnership(v_stack_m148, v_stack_m190, (unsigned int)((unsigned int)(v_rbx + 1)), a4);
loc_0022C1F8:
    if (v_stack_m108 != v_stack_m100) goto loc_0022C22F;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(v_stack_m118 + 16))) >> (2));
    if ((((unsigned __int8)(v_rbx + 1)) & ((unsigned __int8)(result))) != 0) goto loc_0022C69E;
loc_0022C22F:
    if (v_stack_m1D0 == 0) goto loc_0022C4B9;
    result = (v_stack_m160) << (12);
    v_rbx = (result) ^ (*(unsigned __int64 *)(a1));
    v_rbx = (v_rbx) & (v_stack_m150);
    v_rbx = (v_rbx) ^ (result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1D0 + 20))) | (64));
    *(unsigned int *)(v_stack_m1D0 + 20) = (unsigned int)(result);
    if (!(condition_is_above_or_equal)) {
        result = (unsigned int)((result) | (32));
        *(unsigned int *)(v_stack_m1D0 + 20) = (unsigned int)(result);
    }
    a3 = 0;
    result = MiWriteValidPteNewPage(v_stack_m190, v_rbx, a3, a4);
    v_stack_mD8 = v_rbx;
    if (condition_is_below) goto loc_0022C6F4;
loc_0022C2A6:
loc_0022C2AE:
    *(unsigned __int64 *)(v_stack_m170) = v_rbx;
    result = (*(unsigned __int64 *)(v_stack_m118 + 24)) | (v_r12);
    *(unsigned __int64 *)(v_stack_m118 + 24) = result;
    v_stack_m1D8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m140)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m140))) >> (16));
    result = (unsigned __int8)((result) | (7));
    v_stack_m1D6 = (unsigned __int8)(result);
    *(unsigned int *)(v_stack_m118 + 32) = (unsigned int)((unsigned int)(v_stack_m1D8));
    v_rbx = (*(unsigned __int64 *)(v_stack_m40)) & (0xFFFFFFFFFFFFF000ULL);
    *(unsigned __int64 *)(v_stack_m40) = v_stack_m118;
    a4 = 0;
    result = MiInsertTbFlushEntry(v_stack_m1D0, v_rbx, v_rbx + 1, a4);
    result = (unsigned int)(*(unsigned int *)(v_stack_m158 + 184));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m158 + 184)))) & (15)) == 0) {
        a3 = 0;
        a2 = v_rbx;
        result = MiSetWsleProtection(v_stack_m1D0, a2, a3, a4);
    }
    a4 = 0;
    a3 = (a3) | (-1);
    result = MiUpdateWorkingSetPrivateSize(v_stack_m158, v_rbx, a3, a4);
    if (v_stack_m1B8 != 0) goto loc_0022CA30;
loc_0022C34D:
    if (v_stack_m1B0 != 0) goto loc_0022CA84;
loc_0022C35B:
    result = MiActivateCombineBlock(v_stack_m130, v_stack_m1C0, a3, a4);
    result = 0;
loc_0022C387:
    a1 = (v_stack_m30) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m1C0, a3, a4);
    v_rsp = (v_rsp) + (480);
    return result;
loc_0022C3B1:
    result = MiComputeHash64(v_stack_p20, v_stack_m1C0, a3, a4);
    if (result != (*(unsigned __int64 *)(a3 + 8))) goto loc_0022C9CE;
    if ((*(unsigned __int64 *)(a3 + 24)) == (*(unsigned __int64 *)(v_rip + 12598083))) goto loc_0022C9D6;
loc_0022C3D7:
    goto loc_0022BF5A;
loc_0022C3E1:
    a1 = ((((unsigned int)(*(unsigned __int64 *)(v_rip + 14264092))) & (0x8000001ULL)) != 0) ? 1 : 0;
    v_stack_p50 = (unsigned int)(a1);
    if ((((unsigned int)(*(unsigned __int64 *)(v_rip + 14264092))) & (0x8000001ULL)) != 0) goto loc_0022CA04;
loc_0022C404:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_p78))) & (66)) == 0) goto loc_0022C0B3;
    v_rdi = (*(unsigned __int64 *)(v_stack_p78)) & (-67);
    goto loc_0022C0B3;
loc_0022C423:
    v_rbx = (unsigned int)(((unsigned int)(v_stack_p60)) + ((unsigned int)(v_rbx + 1)));
    v_stack_p60 = (unsigned int)(v_rbx);
    if (((*(unsigned int *)(v_rip + 14257784)) & ((unsigned int)(v_rbx))) == 0) goto loc_0022C8C4;
loc_0022C43A:
loc_0022C43C:
    if (!sign_flag) goto loc_0022C0C0;
    goto loc_0022C423;
loc_0022C44B:
    v_rbx = (unsigned int)(((unsigned int)(v_stack_p68)) + ((unsigned int)(v_rbx + 1)));
    v_stack_p68 = (unsigned int)(v_rbx);
    if (((*(unsigned int *)(v_rip + 14257744)) & ((unsigned int)(v_rbx))) == 0) goto loc_0022C8F3;
loc_0022C462:
loc_0022C464:
    if (!sign_flag) goto loc_0022C11B;
    goto loc_0022C44B;
loc_0022C473:
    goto loc_0022C088;
loc_0022C488:
    v_r15 = (unsigned int)(((unsigned int)(v_stack_pA0)) + ((unsigned int)(v_rbx + 1)));
    v_stack_pA0 = (unsigned int)(v_r15);
    if (((*(unsigned int *)(v_rip + 14257674)) & ((unsigned int)(v_r15))) == 0) goto loc_0022C947;
loc_0022C4A8:
loc_0022C4AA:
    if (!sign_flag) goto loc_0022C012;
    goto loc_0022C488;
loc_0022C4B9:
    result = (*(unsigned __int64 *)(v_stack_m1C0 + v_r15 * 1)) & (a1);
    *(unsigned __int64 *)(v_stack_m158 + 24) = result;
    result = MiPfnReferenceCountIsZero(v_stack_m158, v_stack_pD0, a3, a4);
    v_rbx = (*(unsigned __int64 *)(v_stack_m158 + 40)) & (result);
    a1 = (v_rbx + v_rbx * 2) << (4);
    a1 = (a1) + (result);
    result = MiLockAndDecrementShareCount(a1, 2, a3, a4);
    goto loc_0022C34D;
loc_0022C52D:
    a1 = (v_r15) >> (4);
    a1 = (a1) * (a3);
    result = MiMakeTransitionPte(a1, 2, a3, a4);
    v_stack_pE8 = result;
    v_stack_p120 = a4 + 72;
    goto loc_0022BE1A;
loc_0022C563:
    a2 = 0;
    if (v_stack_p40 != v_stack_p60) goto loc_0022C99E;
loc_0022C57C:
    if (0 != 0) goto loc_0022C6C9;
loc_0022C584:
    result = a4 + 72;
    if (v_stack_p40 != v_stack_p60) {
        result = v_stack_p70;
    }
    a2 = 0;
    result = MiUnlinkPageFromListEx(v_stack_m158, a2, a3, a4);
    if ((((unsigned __int8)(result)) & (3)) == 0) goto loc_0022C07E;
    a2 = 0;
    result = MiDiscardTransitionPteEx(v_stack_m158, a2, a3, a4);
    *(unsigned __int64 *)(v_stack_p48 + 56) = 1;
    v_stack_p20 = v_stack_p70;
    result = MiDecrementCloneBlock(v_stack_p60, v_stack_pB0, v_stack_p178, 4);
    goto loc_0022C60E;
loc_0022C5EB:
    if (v_stack_p38 == 0) goto loc_0022C9F0;
loc_0022C5F4:
    goto loc_0022C387;
loc_0022C5FE:
    result = MiGetCloneCharges(v_stack_p60, v_stack_pB0, v_stack_p178, 4);
    if ((unsigned int)(result) != 0) goto loc_0022C06B;
loc_0022C60E:
    goto loc_0022C07E;
loc_0022C618:
    result = (*(unsigned __int64 *)((unsigned int)(0xC0000018ULL) + 24)) & (v_stack_p60);
    *(unsigned __int64 *)((unsigned int)(0xC0000018ULL) + 24) = result;
    v_stack_p128 = result;
    *(unsigned __int64 *)(v_stack_p98) = result;
    result = MiMakePrototypePteDirect(v_stack_p98, v_stack_pB0, v_stack_p178, 4);
    result = MiWriteRepurposedTransitionPte(v_stack_m158, result, v_stack_p178, 4);
    result = (*(unsigned __int64 *)(v_stack_m158 + 24)) | (v_stack_p60);
    *(unsigned __int64 *)(v_stack_m158 + 24) = result;
    result = MiTransferPageFileOwnership((unsigned int)(0xC0000018ULL), v_stack_p78, v_stack_p178, 4);
    result = MiPfnReferenceCountIsZero((unsigned int)(0xC0000018ULL), v_stack_pA8, v_stack_p178, 4);
    v_stack_pB8 = v_stack_m158;
    goto loc_0022C1F8;
loc_0022C69E:
    result = (*(unsigned __int64 *)(v_stack_m158 + 16)) & (-5);
    *(unsigned __int64 *)(v_stack_m158 + 16) = result;
    if (v_stack_p58 == 0) goto loc_0022C22F;
    result = (v_stack_p58) & (-5);
    v_stack_p58 = result;
    goto loc_0022C22F;
loc_0022C6C9:
    result = MiGetCloneCharges(v_stack_p60, v_stack_m158, v_stack_p178, 4);
    if ((unsigned int)(result) != 0) goto loc_0022C584;
loc_0022C6DE:
    goto loc_0022C387;
loc_0022C6F4:
    if ((((unsigned __int8)((unsigned int)(0xC0000018ULL))) & (32)) != 0) goto loc_0022C2A6;
    result = ((unsigned int)((unsigned int)((unsigned int)(0xC0000018ULL)))) + (v_stack_p60);
    if (v_stack_p98 < result) goto loc_0022C2AE;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_p98, (unsigned int)(0xC0000018ULL), 128, 4);
    goto loc_0022C2AE;
loc_0022C73E:
loc_0022C746:
    if (v_stack_p98 < result) goto loc_0022C91A;
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p120))))) == 0) goto loc_0022C9C6;
    result = MiStandbyPageStillCombineCandidate(v_stack_m158, v_stack_p40, v_stack_p78, (unsigned int)(v_stack_p50));
    if ((unsigned int)(result) == 0) goto loc_0022C9C6;
    result = MiRecheckCombineVm(v_stack_pD8, (unsigned int)(v_stack_p30), v_stack_m158, v_stack_pB0);
    if ((unsigned int)(result) == 0) goto loc_0022C9C6;
    result = KeCopyPage((unsigned int)(0xC0000018ULL), v_stack_p60, (unsigned int)(v_stack_p88), v_stack_pB0);
    goto loc_0022BF23;
loc_0022C8C4:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14262766)))) & (64)) == 0) goto loc_0022C43A;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)(0xC0000018ULL), v_stack_p60, v_stack_p90, v_stack_pB0);
    if ((unsigned __int8)(result) == 0) goto loc_0022CA23;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((unsigned int)(0xC0000018ULL))), v_stack_p60, v_stack_p90, v_stack_pB0);
    goto loc_0022C43C;
loc_0022C8F3:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14262719)))) & (64)) == 0) goto loc_0022C462;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)((unsigned int)(0xC0000018ULL))), v_stack_p88, v_stack_p90, v_stack_pB0);
    if ((unsigned __int8)(result) == 0) goto loc_0022C462;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)((unsigned int)(0xC0000018ULL))), v_stack_p88, v_stack_p90, v_stack_pB0);
    goto loc_0022C464;
loc_0022C91A:
    v_r15 = (unsigned int)(((unsigned int)(v_stack_p80)) + 1);
    v_stack_p80 = (unsigned int)(v_r15);
    if (((*(unsigned int *)(v_rip + 14256504)) & ((unsigned int)(v_r15))) == 0) goto loc_0022C981;
loc_0022C936:
loc_0022C938:
    if (!sign_flag) goto loc_0022C746;
    goto loc_0022C91A;
loc_0022C947:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14262635)))) & (64)) == 0) goto loc_0022C4A8;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)((unsigned int)(0xC0000018ULL))), v_stack_p88, v_stack_p90, v_stack_pB0);
    if ((unsigned __int8)(result) == 0) goto loc_0022C4A8;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r15)), v_stack_p88, v_stack_p90, v_stack_pB0);
    goto loc_0022C4AA;
loc_0022C96F:
    a2 = v_stack_p88;
    if ((*(unsigned __int64 *)(v_stack_p70 + 40)) == v_stack_p88) { a2 = (unsigned int)(v_r15); }
    goto loc_0022C063;
loc_0022C981:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 14262577)))) & (64)) == 0) goto loc_0022C936;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_r15)), a2, v_stack_p90, v_stack_pB0);
    if ((unsigned __int8)(result) == 0) goto loc_0022C936;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r15)), a2, v_stack_p90, v_stack_pB0);
    goto loc_0022C938;
loc_0022C99E:
    if ((*(unsigned __int64 *)(v_stack_p70 + 40)) == a2) { a2 = (unsigned int)(v_r15); }
    goto loc_0022C57C;
loc_0022C9B0:
    result = MiChangePageAttribute(1, (unsigned int)((unsigned int)(v_r15)), 16, v_stack_pB0);
    goto loc_0022BEB2;
loc_0022C9C6:
    v_r13 = 0;
    goto loc_0022BEFD;
loc_0022C9CE:
    v_r13 = 0;
    goto loc_0022C3D7;
loc_0022C9D6:
    result = MiHashIsCommon(v_r15, *(unsigned __int64 *)(a3 + 8), (unsigned int)(0xC0000018ULL), v_stack_pB0);
    result = (unsigned int)(-(result));
    v_r13 = (unsigned int)((v_r13) & ((unsigned int)(v_r15)));
    goto loc_0022C3D7;
loc_0022C9F0:
    goto loc_0022C5F4;
loc_0022CA04:
    result = MiIdentifyPfn(v_stack_pD0, v_stack_p1A8, (unsigned int)(0xC0000018ULL), v_stack_pB0);
    goto loc_0022C404;
loc_0022CA23:
    goto loc_0022C43A;
loc_0022CA30:
    v_stack_p1C0 = v_stack_p98;
    v_stack_p1C8 = v_stack_p1A8;
    v_stack_p1D0 = 32;
    v_stack_p20 = 0x11501B04ULL;
    result = EtwTraceKernelEvent(v_stack_p1C8, (unsigned int)((unsigned int)(v_r13)), (unsigned int)(0x28000001ULL), 634);
    goto loc_0022C34D;
loc_0022CA84:
    result = MiReleasePageFileInfo(v_stack_p40, (unsigned int)((unsigned int)(v_r13)), (unsigned int)((unsigned int)(v_r13)), 634);
    goto loc_0022C35B;
}
```

## 5. (Beta) C Style

```c
int64_t MiCombineInitialInstance(void *Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint32_t v_stack_m180;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint32_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint8_t v_stack_m1D5;
    uint8_t v_stack_m1D6;
    uint32_t v_stack_m1D8;
    uint64_t v_stack_m30;
    uint64_t v_stack_m40;
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
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p100;
    uint64_t v_stack_p108;
    uint64_t v_stack_p110;
    uint64_t v_stack_p120;
    uint64_t v_stack_p128;
    uint64_t v_stack_p138;
    uint64_t v_stack_p140;
    uint64_t v_stack_p148;
    uint64_t v_stack_p150;
    uint64_t v_stack_p158;
    uint64_t v_stack_p160;
    uint64_t v_stack_p168;
    uint64_t v_stack_p170;
    uint64_t v_stack_p178;
    uint64_t v_stack_p190;
    uint64_t v_stack_p1A8;
    uint64_t v_stack_p1C0;
    uint64_t v_stack_p1C8;
    uint32_t v_stack_p1D0;
    uint32_t v_stack_p1D4;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint32_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint32_t v_stack_p80;
    uint32_t v_stack_p88;
    uint64_t v_stack_p90;
    uint64_t v_stack_p98;
    uint32_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pC0;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pE8;
    uint64_t v_stack_pF0;

    *(uint64_t *)(local_rsp + 0x20) = local_rbx;
    local_rsp = (local_rsp) - (480);
    result = (*(uint64_t *)(v_rip + 0xBDEB16)) ^ (local_rsp);
    v_stack_m30 = result;
    v_stack_m1D0 = Arg3;
    v_stack_m178 = Arg2;
    v_stack_m1A0 = Arg1;
    v_stack_mB8 = Arg1;
    v_stack_mF8 = Arg2;
    v_stack_m128 = Arg3;
    *(uint64_t *)(local_rsp - 0x60) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x50) = v_xmm0;
    v_stack_m70 = Arg1 + 296;
    v_stack_m1C0 = *(uint64_t *)(arg1 + 0x128);
    v_stack_mD0 = *(uint64_t *)(arg1 + 0x128);
    v_stack_m198 = *(uint64_t *)(arg1 + 0x128);
    v_stack_m68 = Arg1 + 304;
    v_stack_m148 = *(uint64_t *)(arg1 + 0x130);
    v_stack_m168 = *(uint64_t *)(arg1 + 0x130);
    v_stack_m130 = *(uint64_t *)(arg1);
    v_stack_m78 = *(uint64_t *)(arg1);
    v_stack_m1D8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8C)));
    v_stack_m158 = *(uint64_t *)(arg1 + 0x70);
    v_stack_m98 = *(uint64_t *)(arg1 + 0x70);
    v_stack_m100 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xC0438E) + *(uint16_t *)(*(uint64_t *)(arg1 + 0x70) + 0xAE) * 8);
    v_stack_mC8 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xC0438E) + *(uint16_t *)(*(uint64_t *)(arg1 + 0x70) + 0xAE) * 8);
    v_stack_m1C8 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xC0438E) + *(uint16_t *)(*(uint64_t *)(arg1 + 0x70) + 0xAE) * 8);
    v_stack_m138 = *(uint64_t *)(arg1 + 0x90);
    v_stack_mB0 = *(uint64_t *)(arg1 + 0x90);
    Arg1 = (*(uint64_t *)(arg1 + 0x90) + *(uint64_t *)(arg1 + 0x90) * 2) << (4);
    result = (local_rsp) + (Arg1);
    v_stack_m118 = result;
    v_stack_m150 = result;
    v_stack_mA8 = *(uint64_t *)(arg1 + 0x60);
    v_stack_m108 = *(uint64_t *)(*(uint64_t *)(arg1));
    v_stack_mC0 = *(uint64_t *)(*(uint64_t *)(arg1));
    v_stack_m1A8 = *(uint64_t *)(*(uint64_t *)(arg1));
    v_stack_mA0 = *(uint64_t *)(arg1 + 0x60) + 4096;
    v_stack_m40 = Arg2 + 16;
    Arg1 = (*(uint64_t *)(arg2 + 0x10)) >> (9);
    Arg1 = (Arg1) & (Arg2 + 16);
    Arg1 = (Arg1) + (Arg2 + 16);
    v_stack_m190 = Arg1;
    v_stack_mE0 = Arg2 + 32;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x20))) & (31));
    v_stack_m1B8 = (uint32_t)(Arg2);
    local_r15 = (*(uint64_t *)(arg1 + 0x130)) - (local_rsp);
    if (Arg3 == 0) goto loc_0022C52D;
    v_stack_m120 = *(uint64_t *)(arg1);
    a4 = 0;
    result = MiMapSinglePage(*(uint64_t *)(arg1 + 0x60), *(uint64_t *)(arg1 + 0x90), (uint32_t)(0xC0000010ULL), a4);
    v_stack_mE8 = 56;
loc_0022BE1A:
    result = (v_stack_m1C0) + (32);
    v_stack_m90 = result;
    v_stack_m170 = result;
    Arg2 = (result) & (*(uint64_t *)(arg1 + 0x60));
    v_stack_m110 = Arg2;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = v_xmm0;
    v_stack_m80 = *(uint64_t *)(arg1 + 0x130) + 16;
    result = MiSetOriginalPtePfnFromFreeList(*(uint64_t *)(arg1 + 0x130) + 16, Arg2, (uint32_t)(0xC0000010ULL), a4);
    local_r15 = (local_r15) >> (4);
    local_r15 = (local_r15) * ((uint32_t)(0xC0000010ULL));
    v_stack_m160 = local_r15;
    v_stack_m140 = result + 32;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x20))) >> (16));
    local_r15 = (uint32_t)(((uint8_t)(result)) >> (6));
    v_stack_m88 = *(uint64_t *)(arg1 + 0x130) + 32;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x130) + 0x20))) >> (16));
    Arg1 = (uint32_t)(((uint8_t)(result)) >> (6));
    if (((uint32_t)(Arg1)) != ((uint32_t)(local_r15))) goto loc_0022C9B0;
loc_0022BEB2:
    result = MiTranslateCacheAttribute((uint32_t)((uint32_t)(local_r15)), Arg2, (uint32_t)(0xC0000010ULL), a4);
    v_stack_m180 = (uint32_t)(result);
    a4 = 0;
    result = MiMapSinglePage(*(uint64_t *)(arg1 + 0x60) + 4096, v_stack_m160, (uint32_t)(0x40000010ULL), a4);
    if (v_stack_m1D0 == 0) goto loc_0022C73E;
    result = KeCopyPage(*(uint64_t *)(arg1 + 0x60) + 4096, *(uint64_t *)(arg1 + 0x60), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a4);
loc_0022BEFD:
loc_0022BF23:
    local_r12 = *(uint64_t *)(arg1 + 0x60);
    if (v_stack_m1D0 != 0) {
        local_r12 = (*(uint64_t *)(arg1 + 0x60)) >> (9);
        local_r12 = (local_r12) & (*(uint64_t *)(arg1 + 0x60) + 4096);
        result = 0;
        local_r12 = (local_r12) + (result);
        result = *(uint64_t *)(v_rip - 0x21B6BC);
        v_stack_mF0 = result;
        *(uint64_t *)(local_r12) = result;
    }
    v_stack_m1B0 = *(uint64_t *)(result + 0x10);
    if (1 != 0) goto loc_0022C3B1;
loc_0022BF5A:
    local_rbx = (*(uint64_t *)(arg1 + 0x60) + 4096) >> (9);
    local_rbx = (local_rbx) & (*(uint64_t *)(result + 0x10));
    local_rbx = (local_rbx) + (*(uint64_t *)(result + 0x10));
    v_stack_mF8 = *(uint64_t *)(v_rip - 0x21B702);
    *(uint64_t *)(local_rbx) = *(uint64_t *)(v_rip - 0x21B702);
    if (1 == 0) goto loc_0022C5EB;
    result = MiGetContainingPageTable(v_stack_m170, *(uint64_t *)(arg1 + 0x60), v_stack_m178, a4);
    v_stack_m128 = result;
    result = (result + result * 2) << (4);
    result = (result) + (v_stack_m170);
    v_stack_m180 = result;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mE0))) & (31));
    *(void **)(v_stack_m1C0 + 0x30) = Arg1;
    *(uint64_t *)(v_stack_m1C0 + 0x18) = *(uint64_t *)(v_stack_m178 + 0x8);
    *(uint64_t *)(v_stack_m1C0 + 0x40) = *(uint64_t *)(v_stack_m178 + 0x18);
    local_rbx = 0;
    if (v_stack_m1D0 == 0) goto loc_0022C563;
loc_0022C012:
    if (condition_is_below) goto loc_0022C488;
    result = (*(uint64_t *)(result + 0x18)) & (*(uint64_t *)(v_stack_m178 + 0x18));
    if (result != (local_rbx + 1)) goto loc_0022C473;
    if (((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m140)))) != ((uint16_t)(local_rbx + 1))) goto loc_0022C473;
    Arg2 = 0;
    if (v_stack_m1C8 != v_stack_m1A8) goto loc_0022C96F;
loc_0022C063:
    if (0 != 0) goto loc_0022C5FE;
loc_0022C06B:
    if (v_stack_m1C8 == v_stack_m1A8) goto loc_0022C083;
loc_0022C07E:
loc_0022C083:
loc_0022C088:
    if (sign_flag) goto loc_0022C6DE;
    *(uint64_t *)(v_stack_m1C0 + 0x38) = local_rbx + 1;
    local_r12 = 0;
    local_r12 = (v_stack_m1A8 != v_stack_m1C8) ? 1 : 0;
    if (v_stack_m1D0 != 0) goto loc_0022C3E1;
loc_0022C0B3:
loc_0022C0C0:
    if (condition_is_below) goto loc_0022C423;
    Arg3 = (*(uint64_t *)(v_stack_m180 + 0x18) + 1) ^ (*(uint64_t *)(v_stack_m180 + 0x18));
    Arg3 = (Arg3) & (*(uint64_t *)(v_stack_m180 + 0x18));
    Arg3 = (Arg3) ^ (*(uint64_t *)(v_stack_m180 + 0x18) + 1);
    *(uint64_t *)(v_stack_m180 + 0x18) = Arg3;
    result = MiAbandonPrivatePfn(result, (uint32_t)((uint32_t)(local_r12)), Arg3, a4);
    v_stack_m1B0 = result;
loc_0022C11B:
    if (condition_is_below) goto loc_0022C44B;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m140))) >> (16));
    Arg2 = (uint32_t)(((uint8_t)(result)) >> (6));
    result = MiFinalizePageAttribute(v_stack_m148, Arg2, (uint32_t)((uint32_t)(local_rbx + 1)), a4);
    result = MiCopyPfnEntryEx(v_stack_m148, v_stack_m118, (uint32_t)((uint32_t)(local_rbx + 1)), a4);
    result = MiGetPfnPriority(v_stack_m148, v_stack_m118, (uint32_t)((uint32_t)(local_rbx + 1)), a4);
    if (((uint32_t)(result)) < ((uint32_t)(Arg2 + 5))) {
        result = v_stack_m88;
        result = *(uint32_t *)(result);
        v_stack_m1D8 = (uint32_t)(result);
        result = (uint32_t)((result) >> (24));
        result = (uint8_t)((result) & (253));
        result = (uint8_t)((result) | ((uint8_t)(Arg2 + 5)));
        v_stack_m1D5 = (uint8_t)(result);
        result = v_stack_m1D8;
        *(uint32_t *)(v_stack_m148 + 0x20) = (uint32_t)(result);
    }
    *(uint64_t *)(v_stack_m148 + 0x8) = v_stack_m110;
    result = (*(uint64_t *)(v_stack_m148 + 0x28)) | (v_stack_m148);
    *(uint64_t *)(v_stack_m148 + 0x28) = result;
    result = MiSetPfnContainingFrame(v_stack_m148, v_stack_m128, (uint32_t)((uint32_t)(local_rbx + 1)), a4);
    result = MI_MAKE_PROTECT_WRITE_COPY(v_stack_m80, v_stack_m128, (uint32_t)((uint32_t)(local_rbx + 1)), a4);
    if (v_stack_m1D0 == 0) goto loc_0022C618;
    result = MiTransferPageFileOwnership(v_stack_m148, v_stack_m190, (uint32_t)((uint32_t)(local_rbx + 1)), a4);
loc_0022C1F8:
    if (v_stack_m108 != v_stack_m100) goto loc_0022C22F;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(v_stack_m118 + 0x10))) >> (2));
    if ((((uint8_t)(local_rbx + 1)) & ((uint8_t)(result))) != 0) goto loc_0022C69E;
loc_0022C22F:
    if (v_stack_m1D0 == 0) goto loc_0022C4B9;
    result = (v_stack_m160) << (12);
    local_rbx = (result) ^ (*(uint64_t *)(arg1));
    local_rbx = (local_rbx) & (v_stack_m150);
    local_rbx = (local_rbx) ^ (result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1D0 + 0x14))) | (64));
    *(uint32_t *)(v_stack_m1D0 + 0x14) = (uint32_t)(result);
    if (!(condition_is_above_or_equal)) {
        result = (uint32_t)((result) | (32));
        *(uint32_t *)(v_stack_m1D0 + 0x14) = (uint32_t)(result);
    }
    Arg3 = 0;
    result = MiWriteValidPteNewPage(v_stack_m190, local_rbx, Arg3, a4);
    v_stack_mD8 = local_rbx;
    if (condition_is_below) goto loc_0022C6F4;
loc_0022C2A6:
loc_0022C2AE:
    *(uint64_t *)(v_stack_m170) = local_rbx;
    result = (*(uint64_t *)(v_stack_m118 + 0x18)) | (local_r12);
    *(uint64_t *)(v_stack_m118 + 0x18) = result;
    v_stack_m1D8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m140)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m140))) >> (16));
    result = (uint8_t)((result) | (7));
    v_stack_m1D6 = (uint8_t)(result);
    *(uint32_t *)(v_stack_m118 + 0x20) = (uint32_t)((uint32_t)(v_stack_m1D8));
    local_rbx = (*(uint64_t *)(v_stack_m40)) & (0xFFFFFFFFFFFFF000ULL);
    *(uint64_t *)(v_stack_m40) = v_stack_m118;
    a4 = 0;
    result = MiInsertTbFlushEntry(v_stack_m1D0, local_rbx, local_rbx + 1, a4);
    result = (uint32_t)(*(uint32_t *)(v_stack_m158 + 0xB8));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m158 + 0xB8)))) & (15)) == 0) {
        Arg3 = 0;
        Arg2 = local_rbx;
        result = MiSetWsleProtection(v_stack_m1D0, Arg2, Arg3, a4);
    }
    a4 = 0;
    Arg3 = (Arg3) | (-1);
    result = MiUpdateWorkingSetPrivateSize(v_stack_m158, local_rbx, Arg3, a4);
    if (v_stack_m1B8 != 0) goto loc_0022CA30;
loc_0022C34D:
    if (v_stack_m1B0 != 0) goto loc_0022CA84;
loc_0022C35B:
    result = MiActivateCombineBlock(v_stack_m130, v_stack_m1C0, Arg3, a4);
    result = 0;
loc_0022C387:
    Arg1 = (v_stack_m30) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m1C0, Arg3, a4);
    local_rsp = (local_rsp) + (480);
    return result;
loc_0022C3B1:
    result = MiComputeHash64(v_stack_p20, v_stack_m1C0, Arg3, a4);
    if (result != (*(uint64_t *)(Arg3 + 0x8))) goto loc_0022C9CE;
    if ((*(uint64_t *)(Arg3 + 0x18)) == (*(uint64_t *)(v_rip + 0xC03B43))) goto loc_0022C9D6;
loc_0022C3D7:
    goto loc_0022BF5A;
loc_0022C3E1:
    Arg1 = ((((uint32_t)(*(uint64_t *)(v_rip + 0xD9A71C))) & (0x8000001ULL)) != 0) ? 1 : 0;
    v_stack_p50 = (uint32_t)(Arg1);
    if ((((uint32_t)(*(uint64_t *)(v_rip + 0xD9A71C))) & (0x8000001ULL)) != 0) goto loc_0022CA04;
loc_0022C404:
    if ((((uint8_t)(*(uint64_t *)(v_stack_p78))) & (66)) == 0) goto loc_0022C0B3;
    local_rdi = (*(uint64_t *)(v_stack_p78)) & (-67);
    goto loc_0022C0B3;
loc_0022C423:
    local_rbx = (uint32_t)(((uint32_t)(v_stack_p60)) + ((uint32_t)(local_rbx + 1)));
    v_stack_p60 = (uint32_t)(local_rbx);
    if (((*(uint32_t *)(v_rip + 0xD98E78)) & ((uint32_t)(local_rbx))) == 0) goto loc_0022C8C4;
loc_0022C43A:
loc_0022C43C:
    if (!sign_flag) goto loc_0022C0C0;
    goto loc_0022C423;
loc_0022C44B:
    local_rbx = (uint32_t)(((uint32_t)(v_stack_p68)) + ((uint32_t)(local_rbx + 1)));
    v_stack_p68 = (uint32_t)(local_rbx);
    if (((*(uint32_t *)(v_rip + 0xD98E50)) & ((uint32_t)(local_rbx))) == 0) goto loc_0022C8F3;
loc_0022C462:
loc_0022C464:
    if (!sign_flag) goto loc_0022C11B;
    goto loc_0022C44B;
loc_0022C473:
    goto loc_0022C088;
loc_0022C488:
    local_r15 = (uint32_t)(((uint32_t)(v_stack_pA0)) + ((uint32_t)(local_rbx + 1)));
    v_stack_pA0 = (uint32_t)(local_r15);
    if (((*(uint32_t *)(v_rip + 0xD98E0A)) & ((uint32_t)(local_r15))) == 0) goto loc_0022C947;
loc_0022C4A8:
loc_0022C4AA:
    if (!sign_flag) goto loc_0022C012;
    goto loc_0022C488;
loc_0022C4B9:
    result = (*(uint64_t *)(v_stack_m1C0 + local_r15 * 1)) & (Arg1);
    *(uint64_t *)(v_stack_m158 + 0x18) = result;
    result = MiPfnReferenceCountIsZero(v_stack_m158, v_stack_pD0, Arg3, a4);
    local_rbx = (*(uint64_t *)(v_stack_m158 + 0x28)) & (result);
    Arg1 = (local_rbx + local_rbx * 2) << (4);
    Arg1 = (Arg1) + (result);
    result = MiLockAndDecrementShareCount(Arg1, 2, Arg3, a4);
    goto loc_0022C34D;
loc_0022C52D:
    Arg1 = (local_r15) >> (4);
    Arg1 = (Arg1) * (Arg3);
    result = MiMakeTransitionPte(Arg1, 2, Arg3, a4);
    v_stack_pE8 = result;
    v_stack_p120 = a4 + 72;
    goto loc_0022BE1A;
loc_0022C563:
    Arg2 = 0;
    if (v_stack_p40 != v_stack_p60) goto loc_0022C99E;
loc_0022C57C:
    if (0 != 0) goto loc_0022C6C9;
loc_0022C584:
    result = a4 + 72;
    if (v_stack_p40 != v_stack_p60) {
        result = v_stack_p70;
    }
    Arg2 = 0;
    result = MiUnlinkPageFromListEx(v_stack_m158, Arg2, Arg3, a4);
    if ((((uint8_t)(result)) & (3)) == 0) goto loc_0022C07E;
    Arg2 = 0;
    result = MiDiscardTransitionPteEx(v_stack_m158, Arg2, Arg3, a4);
    *(uint64_t *)(v_stack_p48 + 0x38) = 1;
    v_stack_p20 = v_stack_p70;
    result = MiDecrementCloneBlock(v_stack_p60, v_stack_pB0, v_stack_p178, 4);
    goto loc_0022C60E;
loc_0022C5EB:
    if (v_stack_p38 == 0) goto loc_0022C9F0;
loc_0022C5F4:
    goto loc_0022C387;
loc_0022C5FE:
    result = MiGetCloneCharges(v_stack_p60, v_stack_pB0, v_stack_p178, 4);
    if ((uint32_t)(result) != 0) goto loc_0022C06B;
loc_0022C60E:
    goto loc_0022C07E;
loc_0022C618:
    result = (*(uint64_t *)((uint32_t)(0xC0000018ULL) + 0x18)) & (v_stack_p60);
    *(uint64_t *)((uint32_t)(0xC0000018ULL) + 0x18) = result;
    v_stack_p128 = result;
    *(uint64_t *)(v_stack_p98) = result;
    result = MiMakePrototypePteDirect(v_stack_p98, v_stack_pB0, v_stack_p178, 4);
    result = MiWriteRepurposedTransitionPte(v_stack_m158, result, v_stack_p178, 4);
    result = (*(uint64_t *)(v_stack_m158 + 0x18)) | (v_stack_p60);
    *(uint64_t *)(v_stack_m158 + 0x18) = result;
    result = MiTransferPageFileOwnership((uint32_t)(0xC0000018ULL), v_stack_p78, v_stack_p178, 4);
    result = MiPfnReferenceCountIsZero((uint32_t)(0xC0000018ULL), v_stack_pA8, v_stack_p178, 4);
    v_stack_pB8 = v_stack_m158;
    goto loc_0022C1F8;
loc_0022C69E:
    result = (*(uint64_t *)(v_stack_m158 + 0x10)) & (-5);
    *(uint64_t *)(v_stack_m158 + 0x10) = result;
    if (v_stack_p58 == 0) goto loc_0022C22F;
    result = (v_stack_p58) & (-5);
    v_stack_p58 = result;
    goto loc_0022C22F;
loc_0022C6C9:
    result = MiGetCloneCharges(v_stack_p60, v_stack_m158, v_stack_p178, 4);
    if ((uint32_t)(result) != 0) goto loc_0022C584;
loc_0022C6DE:
    goto loc_0022C387;
loc_0022C6F4:
    if ((((uint8_t)((uint32_t)(0xC0000018ULL))) & (32)) != 0) goto loc_0022C2A6;
    result = ((uint32_t)((uint32_t)((uint32_t)(0xC0000018ULL)))) + (v_stack_p60);
    if (v_stack_p98 < result) goto loc_0022C2AE;
    result = MiCheckLinearProtectedPteAccessedBit(v_stack_p98, (uint32_t)(0xC0000018ULL), 128, 4);
    goto loc_0022C2AE;
loc_0022C73E:
loc_0022C746:
    if (v_stack_p98 < result) goto loc_0022C91A;
    if (((1) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_p120))))) == 0) goto loc_0022C9C6;
    result = MiStandbyPageStillCombineCandidate(v_stack_m158, v_stack_p40, v_stack_p78, (uint32_t)(v_stack_p50));
    if ((uint32_t)(result) == 0) goto loc_0022C9C6;
    result = MiRecheckCombineVm(v_stack_pD8, (uint32_t)(v_stack_p30), v_stack_m158, v_stack_pB0);
    if ((uint32_t)(result) == 0) goto loc_0022C9C6;
    result = KeCopyPage((uint32_t)(0xC0000018ULL), v_stack_p60, (uint32_t)(v_stack_p88), v_stack_pB0);
    goto loc_0022BF23;
loc_0022C8C4:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD9A1EE)))) & (64)) == 0) goto loc_0022C43A;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)(0xC0000018ULL), v_stack_p60, v_stack_p90, v_stack_pB0);
    if ((uint8_t)(result) == 0) goto loc_0022CA23;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((uint32_t)(0xC0000018ULL))), v_stack_p60, v_stack_p90, v_stack_pB0);
    goto loc_0022C43C;
loc_0022C8F3:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD9A1BF)))) & (64)) == 0) goto loc_0022C462;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)((uint32_t)(0xC0000018ULL))), v_stack_p88, v_stack_p90, v_stack_pB0);
    if ((uint8_t)(result) == 0) goto loc_0022C462;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)((uint32_t)(0xC0000018ULL))), v_stack_p88, v_stack_p90, v_stack_pB0);
    goto loc_0022C464;
loc_0022C91A:
    local_r15 = (uint32_t)(((uint32_t)(v_stack_p80)) + 1);
    v_stack_p80 = (uint32_t)(local_r15);
    if (((*(uint32_t *)(v_rip + 0xD98978)) & ((uint32_t)(local_r15))) == 0) goto loc_0022C981;
loc_0022C936:
loc_0022C938:
    if (!sign_flag) goto loc_0022C746;
    goto loc_0022C91A;
loc_0022C947:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD9A16B)))) & (64)) == 0) goto loc_0022C4A8;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)((uint32_t)(0xC0000018ULL))), v_stack_p88, v_stack_p90, v_stack_pB0);
    if ((uint8_t)(result) == 0) goto loc_0022C4A8;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r15)), v_stack_p88, v_stack_p90, v_stack_pB0);
    goto loc_0022C4AA;
loc_0022C96F:
    Arg2 = v_stack_p88;
    if ((*(uint64_t *)(v_stack_p70 + 0x28)) == v_stack_p88) { Arg2 = (uint32_t)(local_r15); }
    goto loc_0022C063;
loc_0022C981:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD9A131)))) & (64)) == 0) goto loc_0022C936;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_r15)), Arg2, v_stack_p90, v_stack_pB0);
    if ((uint8_t)(result) == 0) goto loc_0022C936;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r15)), Arg2, v_stack_p90, v_stack_pB0);
    goto loc_0022C938;
loc_0022C99E:
    if ((*(uint64_t *)(v_stack_p70 + 0x28)) == Arg2) { Arg2 = (uint32_t)(local_r15); }
    goto loc_0022C57C;
loc_0022C9B0:
    result = MiChangePageAttribute(1, (uint32_t)((uint32_t)(local_r15)), 16, v_stack_pB0);
    goto loc_0022BEB2;
loc_0022C9C6:
    local_r13 = 0;
    goto loc_0022BEFD;
loc_0022C9CE:
    local_r13 = 0;
    goto loc_0022C3D7;
loc_0022C9D6:
    result = MiHashIsCommon(local_r15, *(uint64_t *)(Arg3 + 0x8), (uint32_t)(0xC0000018ULL), v_stack_pB0);
    result = (uint32_t)(-(result));
    local_r13 = (uint32_t)((local_r13) & ((uint32_t)(local_r15)));
    goto loc_0022C3D7;
loc_0022C9F0:
    goto loc_0022C5F4;
loc_0022CA04:
    result = MiIdentifyPfn(v_stack_pD0, v_stack_p1A8, (uint32_t)(0xC0000018ULL), v_stack_pB0);
    goto loc_0022C404;
loc_0022CA23:
    goto loc_0022C43A;
loc_0022CA30:
    v_stack_p1C0 = v_stack_p98;
    v_stack_p1C8 = v_stack_p1A8;
    v_stack_p1D0 = 32;
    v_stack_p20 = 0x11501B04ULL;
    result = EtwTraceKernelEvent(v_stack_p1C8, (uint32_t)((uint32_t)(local_r13)), (uint32_t)(0x28000001ULL), 634);
    goto loc_0022C34D;
loc_0022CA84:
    result = MiReleasePageFileInfo(v_stack_p40, (uint32_t)((uint32_t)(local_r13)), (uint32_t)((uint32_t)(local_r13)), 634);
    goto loc_0022C35B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x8C` | `32` | `R` |
| `Arg1` | `+ 0x90` | `64` | `R` |
| `Arg1` | `+ 0x128` | `64` | `R` |
| `Arg1` | `+ 0x130` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0022BC0C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
