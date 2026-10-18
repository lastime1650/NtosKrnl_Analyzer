# MiReservePtes

- RVA: `0x00318D20`–`0x0031983D` (길이 `2,845` bytes)
- VA: `0x0000000140318D20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00074C5C`
- 디코드: `709`개 명령, `2,845/2,845` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **45**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00318D8A` → [MiCheckProcessorPteCache](MiCheckProcessorPteCache_function_0031A430.md) (function, `0x0031A430`)
- `0x00318DFA` → [MiVaToFlushVm](MiVaToFlushVm_function_0031AD84.md) (function, `0x0031AD84`)
- `0x00318E16` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00318F3A` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0031908D` → [MiFlushTbList](MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x003190A1` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003190C4` → [MiCompareTbFlushTimeStamp](MiCompareTbFlushTimeStamp_function_0031ADE4.md) (function, `0x0031ADE4`)
- `0x003190FA` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x0031913D` → [MiEmptyPteBins](MiEmptyPteBins_function_0031AAE4.md) (function, `0x0031AAE4`)
- `0x00319148` → [MiExpandPtes](../3B/MiExpandPtes_function_003B4B78.md) (function, `0x003B4B78`)
- `0x00319236` → [RtlInterlockedSetClearRunEx](../23/RtlInterlockedSetClearRunEx_function_00238660.md) (function, `0x00238660`)
- `0x003193F2` → [MiMakeSystemPtesAppear](../46/MiMakeSystemPtesAppear_function_00463FB4.md) (function, `0x00463FB4`)
- `0x00319405` → [MiExpandPtes](../3B/MiExpandPtes_function_003B4B78.md) (function, `0x003B4B78`)
- `0x00319435` → [MiEmptyPteBins](MiEmptyPteBins_function_0031AAE4.md) (function, `0x0031AAE4`)
- `0x003194F7` → [qsort](../50/qsort_function_005009F0.md) (function, `0x005009F0`)
- `0x00319500` → [MiCompressTbFlushList](../2A/MiCompressTbFlushList_function_002A93A8.md) (function, `0x002A93A8`)
- `0x0031958B` → [MiCheckPteReserve](../4D/MiCheckPteReserve_function_004D2988.md) (function, `0x004D2988`)
- `0x0031982A` → [MiCheckPteReserve](../4D/MiCheckPteReserve_function_004D2988.md) (function, `0x004D2988`)

### Direct callers
- [MiMapSinglePage](../22/MiMapSinglePage_function_00229D00.md) at `0x00229DDD`
- [MiMakePageAvoidRead](../2B/MiMakePageAvoidRead_function_002B7DE0.md) at `0x002B8049`
- [MmMapLockedPagesSpecifyCache](MmMapLockedPagesSpecifyCache_function_00318800.md) at `0x00318895`
- [MiMapContiguousMemory](../32/MiMapContiguousMemory_function_0032787C.md) at `0x003279D6`
- [sub_0033827F](../33/Unknown_function_0033827F.md) at `0x003382AE`
- [MmCopyToCachedPage](../34/MmCopyToCachedPage_function_00347B44.md) at `0x003480B1`
- [MiPrivateFixup](../36/MiPrivateFixup_function_003693E8.md) at `0x00369685`
- [MiInsertInSystemSpace](../3B/MiInsertInSystemSpace_function_003B2F5C.md) at `0x003B309A`
- [MiBuildReservationCluster](../40/MiBuildReservationCluster_function_004071A0.md) at `0x0040737B`
- [MiUpdateImagePfnImportRelocations](../44/MiUpdateImagePfnImportRelocations_function_00449E84.md) at `0x00449EF7`
- [MiCreatePteCopyList](../48/MiCreatePteCopyList_function_004887E8.md) at `0x0048880F`
- [MmMapMdl](../67/MmMapMdl_function_0067CBA0.md) at `0x0067CCC5`
- [MiInitializePageFaultResources](../67/MiInitializePageFaultResources_function_0067E490.md) at `0x0067E579`
- [MiBuildDynamicRegion](../67/MiBuildDynamicRegion_function_0067F470.md) at `0x0067F542`
- [MiInitializeDebuggerSupport](../68/MiInitializeDebuggerSupport_function_0068605C.md) at `0x0068606C`
- [MiPrepareEnclaveMetadataPage](../68/MiPrepareEnclaveMetadataPage_function_00686EAC.md) at `0x00686EEA`
- [MiCopyMemoryPagefileData](../69/MiCopyMemoryPagefileData_function_00694C04.md) at `0x00694C50`
- [MiReservePageHash](../69/MiReservePageHash_function_00697B80.md) at `0x00697BAE`
- [MiAllocateZeroCalibrationBuffer](../69/MiAllocateZeroCalibrationBuffer_function_00699844.md) at `0x0069993D`
- [MmAllocateNonCachedMemory](../../page/7F/MmAllocateNonCachedMemory_function_007FBB60.md) at `0x007FBC0C`
- [MiLockAndMapEntireDriver](../../page/80/MiLockAndMapEntireDriver_function_008015C8.md) at `0x008016ED`
- [MiMapHotPatchImageInSystemSpace](../../page/80/MiMapHotPatchImageInSystemSpace_function_00806438.md) at `0x00806559`
- [MiAllocateEnclaveVad](../../page/80/MiAllocateEnclaveVad_function_008080A4.md) at `0x008081BA`
- [MiCreatePfnBitMaps](../../page/80/MiCreatePfnBitMaps_function_0080BBC8.md) at `0x0080BC64`
- [MiCreatePfnBitMaps](../../page/80/MiCreatePfnBitMaps_function_0080BBC8.md) at `0x0080BD29`
- [MiCreatePfnBitMaps](../../page/80/MiCreatePfnBitMaps_function_0080BBC8.md) at `0x0080BDA4`
- [MiCreatePfnBitMaps](../../page/80/MiCreatePfnBitMaps_function_0080BBC8.md) at `0x0080BE69`
- [MiCreatePfnBitMaps](../../page/80/MiCreatePfnBitMaps_function_0080BBC8.md) at `0x0080BEF1`
- [MiCreatePfnBitMaps](../../page/80/MiCreatePfnBitMaps_function_0080BBC8.md) at `0x0080BF56`
- [MiExpandPartitionIds](../../page/80/MiExpandPartitionIds_function_0080D258.md) at `0x0080D2FF`
- [MiValidateImagePfn](../../page/93/MiValidateImagePfn_function_0093EA08.md) at `0x0093EA74`
- [MiRelocateImagePfn](../../page/93/MiRelocateImagePfn_function_0093F2A8.md) at `0x0093F476`
- [MiRelocateImageAgain](../../page/98/MiRelocateImageAgain_function_009885C8.md) at `0x0098866B`
- [MiAllocateProcessShadow](../../page/A5/MiAllocateProcessShadow_function_00A5F1A0.md) at `0x00A5F1F8`
- [MmAllocateMappingAddressEx](../../page/A7/MmAllocateMappingAddressEx_function_00A726B0.md) at `0x00A7273E`
- [MiApplyImportOptimizationToRuntimeDriver](../../page/A9/MiApplyImportOptimizationToRuntimeDriver_function_00A9F93C.md) at `0x00A9F9BA`
- [MmAllocateIndependentPagesEx](../../page/AA/MmAllocateIndependentPagesEx_function_00AA0CFC.md) at `0x00AA0D42`
- [MmAllocateDumpHibernateResources](../../page/AB/MmAllocateDumpHibernateResources_function_00AB3B4C.md) at `0x00AB3B6C`
- [MmInitializeProcessor](../../pagelk/B7/MmInitializeProcessor_function_00B737F8.md) at `0x00B738C9`
- [MiInitSystem](../../init/C5/MiInitSystem_function_00C5E6C0.md) at `0x00C5E756`
- [MiInitSystem](../../init/C5/MiInitSystem_function_00C5E6C0.md) at `0x00C5E764`
- [MiInitSystem](../../init/C5/MiInitSystem_function_00C5E6C0.md) at `0x00C5EA2A`
- [MiMapDummyPages](../../init/C6/MiMapDummyPages_function_00C60A58.md) at `0x00C60A7F`
- [MiProtectSharedUserPage](../../init/C6/MiProtectSharedUserPage_function_00C60F44.md) at `0x00C6100C`
- [MiSectionInitialization](../../init/C6/MiSectionInitialization_function_00C644A4.md) at `0x00C64704`
- [MiInitializeMirroring](../../init/C6/MiInitializeMirroring_function_00C64730.md) at `0x00C647C9`
- [MmInitializeImageViewExtensionCfg](../../init/C6/MmInitializeImageViewExtensionCfg_function_00C64FC4.md) at `0x00C65017`
- [MiCreateRetpolineBitmap](../../init/C6/MiCreateRetpolineBitmap_function_00C66418.md) at `0x00C66436`
- [MiInitializeRetpoline](../../init/C6/MiInitializeRetpoline_function_00C66544.md) at `0x00C66586`
- [MiInitializeKernelCfg](../../init/C6/MiInitializeKernelCfg_function_00C6A2FC.md) at `0x00C6A32A`
- [MiInitializePteInfo](../../init/C6/MiInitializePteInfo_function_00C6A7E0.md) at `0x00C6A873`
- [MiInitializePteInfo](../../init/C6/MiInitializePteInfo_function_00C6A7E0.md) at `0x00C6A88D`
- [MiInitializeTbFlush](../../init/C6/MiInitializeTbFlush_function_00C6B01C.md) at `0x00C6B051`

### Static image references
- `0x00318D3C` → RVA `0x00E0A740` (`.data`; read)
- `0x00318D4D` → RVA `0x00E37668` (`.data`; read)
- `0x00318DC6` → RVA `0x00E2DC80` (`.data`; read)
- `0x00318EFD` → RVA `0x00010880` (`.rdata`; read)
- `0x003194EA` → RVA `0x00695890` (`MiTbFlushSort`; read)
- `0x003196CD` → RVA `0x00E35E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00318D20  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00318D25  55                              push rbp
00318D26  56                              push rsi
00318D27  57                              push rdi
00318D28  41 54                           push r12
00318D2A  41 55                           push r13
00318D2C  41 56                           push r14
00318D2E  41 57                           push r15
00318D30  48 8D 6C 24 80                  lea rbp, [rsp - 0x80]
00318D35  48 81 EC 80 01 00 00            sub rsp, 0x180
00318D3C  48 8B 05 FD 19 AF 00            mov rax, qword ptr [rip + 0xaf19fd]
00318D43  48 33 C4                        xor rax, rsp
00318D46  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
00318D4A  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
00318D4D  4C 8D 3D 14 E9 B1 00            lea r15, [rip + 0xb1e914]
00318D54  8B DA                           mov ebx, edx
00318D56  0F 57 C0                        xorps xmm0, xmm0
00318D59  C7 44 24 40 00 00 00 00         mov dword ptr [rsp + 0x40], 0
00318D61  48 8B F1                        mov rsi, rcx
00318D64  8B FA                           mov edi, edx
00318D66  44 8B F2                        mov r14d, edx
00318D69  0F 11 45 80                     movups xmmword ptr [rbp - 0x80], xmm0
00318D6D  A8 01                           test al, 1
00318D6F  0F 85 AD 03 00 00               jne 0x140319122
00318D75  49 3B CF                        cmp rcx, r15
00318D78  0F 85 AB 03 00 00               jne 0x140319129
00318D7E  48 83 FF 40                     cmp rdi, 0x40
00318D82  0F 87 A1 03 00 00               ja 0x140319129
00318D88  8B CF                           mov ecx, edi
00318D8A  E8 A1 16 00 00                  call 0x14031a430
00318D8F  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00318D94  4C 8B E0                        mov r12, rax
00318D97  48 85 C0                        test rax, rax
00318D9A  0F 84 89 03 00 00               je 0x140319129
00318DA0  8B 46 28                        mov eax, dword ptr [rsi + 0x28]
00318DA3  A8 04                           test al, 4
00318DA5  0F 85 76 0A 00 00               jne 0x140319821
00318DAB  83 FB 10                        cmp ebx, 0x10
00318DAE  77 47                           ja 0x140318df7
00318DB0  33 C9                           xor ecx, ecx
00318DB2  85 DB                           test ebx, ebx
00318DB4  74 39                           je 0x140318def
00318DB6  4D 8B C4                        mov r8, r12
00318DB9  49 B9 00 00 00 00 FF FF FF FF   movabs r9, 0xffffffff00000000
00318DC3  49 8B 00                        mov rax, qword ptr [r8]
00318DC6  48 8B 15 B3 4E B1 00            mov rdx, qword ptr [rip + 0xb14eb3]
00318DCD  48 85 D2                        test rdx, rdx
00318DD0  74 0E                           je 0x140318de0
00318DD2  A8 10                           test al, 0x10
00318DD4  0F 85 92 03 00 00               jne 0x14031916c
00318DDA  48 F7 D2                        not rdx
00318DDD  48 23 C2                        and rax, rdx
00318DE0  49 85 C1                        test r9, rax
00318DE3  75 0A                           jne 0x140318def
00318DE5  FF C1                           inc ecx
00318DE7  49 83 C0 08                     add r8, 8
00318DEB  3B CB                           cmp ecx, ebx
00318DED  72 D4                           jb 0x140318dc3
00318DEF  3B CB                           cmp ecx, ebx
00318DF1  0F 84 A0 02 00 00               je 0x140319097
00318DF7  49 8B CC                        mov rcx, r12
00318DFA  E8 85 1F 00 00                  call 0x14031ad84
00318DFF  48 8B D8                        mov rbx, rax
00318E02  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00318E06  33 C0                           xor eax, eax
00318E08  33 D2                           xor edx, edx
00318E0A  41 B8 98 00 00 00               mov r8d, 0x98
00318E10  88 45 BB                        mov byte ptr [rbp - 0x45], al
00318E13  49 8B F4                        mov rsi, r12
00318E16  E8 25 DE 3A 00                  call 0x1406c6c40
00318E1B  8B 83 B8 00 00 00               mov eax, dword ptr [rbx + 0xb8]
00318E21  45 33 E4                        xor r12d, r12d
00318E24  C1 E8 08                        shr eax, 8
00318E27  41 BF 01 00 00 00               mov r15d, 1
00318E2D  C0 E8 03                        shr al, 3
00318E30  41 8B D4                        mov edx, r12d
00318E33  41 22 C7                        and al, r15b
00318E36  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00318E3A  88 45 B8                        mov byte ptr [rbp - 0x48], al
00318E3D  45 8B EC                        mov r13d, r12d
00318E40  8B 83 B8 00 00 00               mov eax, dword ptr [rbx + 0xb8]
00318E46  C7 45 AC 14 00 00 00            mov dword ptr [rbp - 0x54], 0x14
00318E4D  C7 45 B0 08 00 00 00            mov dword ptr [rbp - 0x50], 8
00318E54  44 89 7D B4                     mov dword ptr [rbp - 0x4c], r15d
00318E58  48 89 5D A0                     mov qword ptr [rbp - 0x60], rbx
00318E5C  A8 0F                           test al, 0xf
00318E5E  75 20                           jne 0x140318e80
00318E60  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00318E69  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00318E70  48 81 C1 00 04 00 00            add rcx, 0x400
00318E77  48 3B D9                        cmp rbx, rcx
00318E7A  0F 85 15 07 00 00               jne 0x140319595
00318E80  8B 83 B8 00 00 00               mov eax, dword ptr [rbx + 0xb8]
00318E86  41 8B CC                        mov ecx, r12d
00318E89  A8 0F                           test al, 0xf
00318E8B  8B 45 B0                        mov eax, dword ptr [rbp - 0x50]
00318E8E  41 0F 44 CF                     cmove ecx, r15d
00318E92  83 E0 DB                        and eax, 0xffffffdb
00318E95  89 4D A8                        mov dword ptr [rbp - 0x58], ecx
00318E98  89 45 B0                        mov dword ptr [rbp - 0x50], eax
00318E9B  4D 8B F4                        mov r14, r12
00318E9E  66 89 55 B9                     mov word ptr [rbp - 0x47], dx
00318EA2  44 89 65 BC                     mov dword ptr [rbp - 0x44], r12d
00318EA6  4C 89 65 C0                     mov qword ptr [rbp - 0x40], r12
00318EAA  4C 89 65 C8                     mov qword ptr [rbp - 0x38], r12
00318EAE  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
00318EB8  49 B9 FF FF FF FF FF F6 FF FF   movabs r9, 0xfffff6ffffffffff
00318EC2  4C 3B F7                        cmp r14, rdi
00318EC5  0F 83 BE 01 00 00               jae 0x140319089
00318ECB  48 8B 1E                        mov rbx, qword ptr [rsi]
00318ECE  48 F7 C3 01 0C 00 00            test rbx, 0xc01
00318ED5  0F 94 C1                        sete cl
00318ED8  48 F7 C3 E0 03 00 00            test rbx, 0x3e0
00318EDF  0F 94 C0                        sete al
00318EE2  84 C8                           test al, cl
00318EE4  74 3C                           je 0x140318f22
00318EE6  48 8B 05 93 4D B1 00            mov rax, qword ptr [rip + 0xb14d93]
00318EED  48 85 C0                        test rax, rax
00318EF0  74 0B                           je 0x140318efd
00318EF2  F6 C3 10                        test bl, 0x10
00318EF5  75 49                           jne 0x140318f40
00318EF7  48 F7 D0                        not rax
00318EFA  48 23 D8                        and rbx, rax
00318EFD  48 8B 05 7C 79 CF FF            mov rax, qword ptr [rip - 0x308684]
00318F04  48 C1 EB 20                     shr rbx, 0x20
00318F08  48 89 06                        mov qword ptr [rsi], rax
00318F0B  85 DB                           test ebx, ebx
00318F0D  75 37                           jne 0x140318f46
00318F0F  41 8B D4                        mov edx, r12d
00318F12  45 8B EC                        mov r13d, r12d
00318F15  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00318F19  49 FF C6                        inc r14
00318F1C  48 83 C6 08                     add rsi, 8
00318F20  EB A0                           jmp 0x140318ec2
00318F22  49 2B FE                        sub rdi, r14
00318F25  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00318F2A  4C 8B CF                        mov r9, rdi
00318F2D  4C 8B C6                        mov r8, rsi
00318F30  BA 00 51 00 00                  mov edx, 0x5100
00318F35  B9 1A 00 00 00                  mov ecx, 0x1a
00318F3A  E8 21 47 1E 00                  call 0x1404fd660
00318F3F  CC                              int3
00318F40  48 83 E3 EF                     and rbx, 0xffffffffffffffef
00318F44  EB B7                           jmp 0x140318efd
00318F46  41 3B DD                        cmp ebx, r13d
00318F49  0F 85 73 01 00 00               jne 0x1403190c2
00318F4F  85 D2                           test edx, edx
00318F51  74 C6                           je 0x140318f19
00318F53  48 8B DE                        mov rbx, rsi
00318F56  48 C1 E3 19                     shl rbx, 0x19
00318F5A  49 8B C0                        mov rax, r8
00318F5D  44 8B 55 B0                     mov r10d, dword ptr [rbp - 0x50]
00318F61  48 C1 E0 19                     shl rax, 0x19
00318F65  48 2B D8                        sub rbx, rax
00318F68  48 C1 FB 10                     sar rbx, 0x10
00318F6C  83 7D A8 01                     cmp dword ptr [rbp - 0x58], 1
00318F70  0F 85 0D 03 00 00               jne 0x140319283
00318F76  44 8B 4D BC                     mov r9d, dword ptr [rbp - 0x44]
00318F7A  45 85 C9                        test r9d, r9d
00318F7D  0F 84 92 00 00 00               je 0x140319015
00318F83  41 F6 C2 02                     test r10b, 2
00318F87  75 4C                           jne 0x140318fd5
00318F89  41 8D 41 FF                     lea eax, [r9 - 1]
00318F8D  4C 8D 5D C8                     lea r11, [rbp - 0x38]
00318F91  4D 8D 1C C3                     lea r11, [r11 + rax*8]
00318F95  49 8B 03                        mov rax, qword ptr [r11]
00318F98  48 A9 00 0C 00 00               test rax, 0xc00
00318F9E  75 35                           jne 0x140318fd5
00318FA0  4C 8B C0                        mov r8, rax
00318FA3  48 8B C8                        mov rcx, rax
00318FA6  41 81 E0 FF 03 00 00            and r8d, 0x3ff
00318FAD  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
00318FB4  49 8D 50 01                     lea rdx, [r8 + 1]
00318FB8  48 C1 E2 0C                     shl rdx, 0xc
00318FBC  48 03 D1                        add rdx, rcx
00318FBF  48 3B D3                        cmp rdx, rbx
00318FC2  75 11                           jne 0x140318fd5
00318FC4  4B 8D 0C 07                     lea rcx, [r15 + r8]
00318FC8  48 81 F9 FF 03 00 00            cmp rcx, 0x3ff
00318FCF  0F 86 DD 02 00 00               jbe 0x1403192b2
00318FD5  45 85 C9                        test r9d, r9d
00318FD8  74 3B                           je 0x140319015
00318FDA  41 F6 C2 02                     test r10b, 2
00318FDE  75 35                           jne 0x140319015
00318FE0  41 8D 41 FF                     lea eax, [r9 - 1]
00318FE4  4C 8D 55 C8                     lea r10, [rbp - 0x38]
00318FE8  4D 8D 14 C2                     lea r10, [r10 + rax*8]
00318FEC  49 8B 02                        mov rax, qword ptr [r10]
00318FEF  48 A9 00 0C 00 00               test rax, 0xc00
00318FF5  75 1E                           jne 0x140319015
00318FF7  4D 8B C7                        mov r8, r15
00318FFA  48 8B C8                        mov rcx, rax
00318FFD  49 C1 E0 0C                     shl r8, 0xc
00319001  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
00319008  4A 8D 14 03                     lea rdx, [rbx + r8]
0031900C  48 3B CA                        cmp rcx, rdx
0031900F  0F 84 1F 05 00 00               je 0x140319534
00319015  44 3B 4D AC                     cmp r9d, dword ptr [rbp - 0x54]
00319019  0F 84 5B 01 00 00               je 0x14031917a
0031901F  4D 85 FF                        test r15, r15
00319022  0F 84 67 01 00 00               je 0x14031918f
00319028  49 8D 47 FF                     lea rax, [r15 - 1]
0031902C  48 8B CB                        mov rcx, rbx
0031902F  48 3D FF 03 00 00               cmp rax, 0x3ff
00319035  BA 00 04 00 00                  mov edx, 0x400
0031903A  49 0F 46 D7                     cmovbe rdx, r15
0031903E  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
00319045  48 8D 42 FF                     lea rax, [rdx - 1]
00319049  25 FF 03 00 00                  and eax, 0x3ff
0031904E  48 0B C1                        or rax, rcx
00319051  48 8B CA                        mov rcx, rdx
00319054  48 C1 E1 0C                     shl rcx, 0xc
00319058  48 03 D9                        add rbx, rcx
0031905B  41 8B C9                        mov ecx, r9d
0031905E  48 89 44 CD C8                  mov qword ptr [rbp + rcx*8 - 0x38], rax
00319063  44 8B 4D BC                     mov r9d, dword ptr [rbp - 0x44]
00319067  48 01 55 C0                     add qword ptr [rbp - 0x40], rdx
0031906B  41 FF C1                        inc r9d
0031906E  44 89 4D BC                     mov dword ptr [rbp - 0x44], r9d
00319072  4C 2B FA                        sub r15, rdx
00319075  74 A8                           je 0x14031901f
00319077  44 3B 4D AC                     cmp r9d, dword ptr [rbp - 0x54]
0031907B  75 A2                           jne 0x14031901f
0031907D  44 8B 55 B0                     mov r10d, dword ptr [rbp - 0x50]
00319081  45 33 E4                        xor r12d, r12d
00319084  E9 F1 FE FF FF                  jmp 0x140318f7a
00319089  48 8D 4D A0                     lea rcx, [rbp - 0x60]
0031908D  E8 2E 8F FF FF                  call 0x140311fc0
00319092  4C 8B 64 24 38                  mov r12, qword ptr [rsp + 0x38]
00319097  49 8B C4                        mov rax, r12
0031909A  48 8B 4D 70                     mov rcx, qword ptr [rbp + 0x70]
0031909E  48 33 CC                        xor rcx, rsp
003190A1  E8 9A 35 39 00                  call 0x1406ac640
003190A6  48 8B 9C 24 D0 01 00 00         mov rbx, qword ptr [rsp + 0x1d0]
003190AE  48 81 C4 80 01 00 00            add rsp, 0x180
003190B5  41 5F                           pop r15
003190B7  41 5E                           pop r14
003190B9  41 5D                           pop r13
003190BB  41 5C                           pop r12
003190BD  5F                              pop rdi
003190BE  5E                              pop rsi
003190BF  5D                              pop rbp
003190C0  C3                              ret
003190C1  CC                              int3
003190C2  8B CB                           mov ecx, ebx
003190C4  E8 1B 1D 00 00                  call 0x14031ade4
003190C9  84 C0                           test al, al
003190CB  0F 84 A4 00 00 00               je 0x140319175
003190D1  48 8B D6                        mov rdx, rsi
003190D4  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
003190DE  48 C1 E2 19                     shl rdx, 0x19
003190E2  48 8B C0                        mov rax, rax
003190E5  48 C1 E0 19                     shl rax, 0x19
003190E9  48 8D 4D A0                     lea rcx, [rbp - 0x60]
003190ED  48 2B D0                        sub rdx, rax
003190F0  45 33 C9                        xor r9d, r9d
003190F3  48 C1 FA 10                     sar rdx, 0x10
003190F7  4D 8B C7                        mov r8, r15
003190FA  E8 71 A5 F7 FF                  call 0x140293670
003190FF  41 8B D7                        mov edx, r15d
00319102  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
00319106  44 8B EB                        mov r13d, ebx
00319109  49 B9 FF FF FF FF FF F6 FF FF   movabs r9, 0xfffff6ffffffffff
00319113  49 B8 00 00 00 00 80 F6 FF FF   movabs r8, 0xfffff68000000000
0031911D  E9 F7 FD FF FF                  jmp 0x140318f19
00319122  4C 8B F7                        mov r14, rdi
00319125  49 C1 EE 04                     shr r14, 4
00319129  81 FB 00 02 00 00               cmp ebx, 0x200
0031912F  72 6F                           jb 0x1403191a0
00319131  41 B8 06 00 00 00               mov r8d, 6
00319137  48 8B D7                        mov rdx, rdi
0031913A  48 8B CE                        mov rcx, rsi
0031913D  E8 A2 19 00 00                  call 0x14031aae4
00319142  48 8B D7                        mov rdx, rdi
00319145  48 8B CE                        mov rcx, rsi
00319148  E8 2B BA 09 00                  call 0x1403b4b78
0031914D  4C 8B E0                        mov r12, rax
00319150  48 85 C0                        test rax, rax
00319153  0F 85 1D 04 00 00               jne 0x140319576
00319159  49 3B F7                        cmp rsi, r15
0031915C  0F 85 6B 05 00 00               jne 0x1403196cd
00319162  FF 46 30                        inc dword ptr [rsi + 0x30]
00319165  33 C0                           xor eax, eax
00319167  E9 2E FF FF FF                  jmp 0x14031909a
0031916C  48 83 E0 EF                     and rax, 0xffffffffffffffef
00319170  E9 6B FC FF FF                  jmp 0x140318de0
00319175  41 8B D4                        mov edx, r12d
00319178  EB 88                           jmp 0x140319102
0031917A  0F B6 45 B9                     movzx eax, byte ptr [rbp - 0x47]
0031917E  45 85 E4                        test r12d, r12d
00319181  0F 84 54 03 00 00               je 0x1403194db
00319187  84 C0                           test al, al
00319189  0F 84 A5 06 00 00               je 0x140319834
0031918F  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
00319193  45 33 E4                        xor r12d, r12d
00319196  45 8D 7C 24 01                  lea r15d, [r12 + 1]
0031919B  E9 69 FF FF FF                  jmp 0x140319109
003191A0  45 33 E4                        xor r12d, r12d
003191A3  4C 8B 46 40                     mov r8, qword ptr [rsi + 0x40]
003191A7  4C 8B EE                        mov r13, rsi
003191AA  48 8B 06                        mov rax, qword ptr [rsi]
003191AD  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
003191B2  48 85 C0                        test rax, rax
003191B5  0F 84 1A 02 00 00               je 0x1403193d5
003191BB  4C 8B 66 48                     mov r12, qword ptr [rsi + 0x48]
003191BF  4D 85 E4                        test r12, r12
003191C2  74 37                           je 0x1403191fb
003191C4  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
003191C8  49 8B CC                        mov rcx, r12
003191CB  48 C1 E9 06                     shr rcx, 6
003191CF  48 8D 14 C8                     lea rdx, [rax + rcx*8]
003191D3  48 8B 06                        mov rax, qword ptr [rsi]
003191D6  49 3B C4                        cmp rax, r12
003191D9  0F 82 F4 02 00 00               jb 0x1403194d3
003191DF  49 2B C4                        sub rax, r12
003191E2  48 89 55 88                     mov qword ptr [rbp - 0x78], rdx
003191E6  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
003191EA  4C 8D 6D 80                     lea r13, [rbp - 0x80]
003191EE  4C 89 6C 24 78                  mov qword ptr [rsp + 0x78], r13
003191F3  4D 85 C0                        test r8, r8
003191F6  74 03                           je 0x1403191fb
003191F8  4D 2B C4                        sub r8, r12
003191FB  4D 8B 5D 00                     mov r11, qword ptr [r13]
003191FF  45 33 FF                        xor r15d, r15d
00319202  49 8B 4D 08                     mov rcx, qword ptr [r13 + 8]
00319206  4D 3B C3                        cmp r8, r11
00319209  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0031920E  4D 0F 42 F8                     cmovb r15, r8
00319212  4D 8D 53 FF                     lea r10, [r11 - 1]
00319216  4D 85 F6                        test r14, r14
00319219  0F 85 B8 00 00 00               jne 0x1403192d7
0031921F  49 83 E7 F8                     and r15, 0xfffffffffffffff8
00319223  49 83 FF FF                     cmp r15, -1
00319227  0F 84 A8 01 00 00               je 0x1403193d5
0031922D  4D 8B C6                        mov r8, r14
00319230  49 8B D7                        mov rdx, r15
00319233  49 8B CD                        mov rcx, r13
00319236  E8 25 F4 F1 FF                  call 0x140238660
0031923B  85 C0                           test eax, eax
0031923D  0F 84 60 FF FF FF               je 0x1403191a3
00319243  48 8B C7                        mov rax, rdi
00319246  48 F7 D8                        neg rax
00319249  F0 48 01 46 58                  lock add qword ptr [rsi + 0x58], rax
0031924E  48 8D 45 80                     lea rax, [rbp - 0x80]
00319252  4C 3B E8                        cmp r13, rax
00319255  75 03                           jne 0x14031925a
00319257  4D 03 FC                        add r15, r12
0031925A  4B 8D 04 3E                     lea rax, [r14 + r15]
0031925E  49 8B CF                        mov rcx, r15
00319261  48 C1 E1 04                     shl rcx, 4
00319265  48 89 46 40                     mov qword ptr [rsi + 0x40], rax
00319269  F6 46 28 01                     test byte ptr [rsi + 0x28], 1
0031926D  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
00319271  49 0F 44 CF                     cmove rcx, r15
00319275  4C 8D 24 C8                     lea r12, [rax + rcx*8]
00319279  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
0031927E  E9 1D FB FF FF                  jmp 0x140318da0
00319283  41 F6 C2 04                     test r10b, 4
00319287  0F 85 E9 FC FF FF               jne 0x140318f76
0031928D  49 8B C0                        mov rax, r8
00319290  48 3B D8                        cmp rbx, rax
00319293  0F 82 DD FC FF FF               jb 0x140318f76
00319299  49 8B C1                        mov rax, r9
0031929C  48 3B D8                        cmp rbx, rax
0031929F  0F 87 D1 FC FF FF               ja 0x140318f76
003192A5  41 83 CA 04                     or r10d, 4
003192A9  44 89 55 B0                     mov dword ptr [rbp - 0x50], r10d
003192AD  E9 C4 FC FF FF                  jmp 0x140318f76
003192B2  49 3B C8                        cmp rcx, r8
003192B5  0F 86 1A FD FF FF               jbe 0x140318fd5
003192BB  4C 01 7D C0                     add qword ptr [rbp - 0x40], r15
003192BF  4A 8D 0C 38                     lea rcx, [rax + r15]
003192C3  48 33 C1                        xor rax, rcx
003192C6  48 25 00 FC FF FF               and rax, 0xfffffffffffffc00
003192CC  48 33 C1                        xor rax, rcx
003192CF  49 89 03                        mov qword ptr [r11], rax
003192D2  E9 B8 FE FF FF                  jmp 0x14031918f
003192D7  41 BD 40 00 00 00               mov r13d, 0x40
003192DD  49 8B C2                        mov rax, r10
003192E0  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
003192E5  49 2B C7                        sub rax, r15
003192E8  C7 44 24 44 00 00 00 00         mov dword ptr [rsp + 0x44], 0
003192F0  48 FF C0                        inc rax
003192F3  49 3B C6                        cmp rax, r14
003192F6  0F 82 77 04 00 00               jb 0x140319773
003192FC  49 8B C2                        mov rax, r10
003192FF  41 B9 01 00 00 00               mov r9d, 1
00319305  49 2B C6                        sub rax, r14
00319308  48 FF C0                        inc rax
0031930B  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00319310  48 C1 E8 06                     shr rax, 6
00319314  48 8D 04 C1                     lea rax, [rcx + rax*8]
00319318  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0031931D  49 8B C7                        mov rax, r15
00319320  48 C1 E8 06                     shr rax, 6
00319324  48 8D 14 C1                     lea rdx, [rcx + rax*8]
00319328  41 0F B6 CF                     movzx ecx, r15b
0031932C  80 E1 3F                        and cl, 0x3f
0031932F  49 D3 E1                        shl r9, cl
00319332  49 FF C9                        dec r9
00319335  4C 0B 0A                        or r9, qword ptr [rdx]
00319338  49 83 FE 7F                     cmp r14, 0x7f
0031933C  0F 87 8C 02 00 00               ja 0x1403195ce
00319342  49 83 FE 40                     cmp r14, 0x40
00319346  0F 83 C8 01 00 00               jae 0x140319514
0031934C  49 83 FE 01                     cmp r14, 1
00319350  0F 87 E9 00 00 00               ja 0x14031943f
00319356  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0031935B  49 83 F9 FF                     cmp r9, -1
0031935F  75 33                           jne 0x140319394
00319361  48 83 C2 08                     add rdx, 8
00319365  48 3B D0                        cmp rdx, rax
00319368  76 66                           jbe 0x1403193d0
0031936A  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0031936F  49 C7 C7 FF FF FF FF            mov r15, 0xffffffffffffffff
00319376  48 83 7C 24 70 00               cmp qword ptr [rsp + 0x70], 0
0031937C  74 48                           je 0x1403193c6
0031937E  4F 8D 14 06                     lea r10, [r14 + r8]
00319382  4D 3B D3                        cmp r10, r11
00319385  4D 0F 47 D3                     cmova r10, r11
00319389  49 FF CA                        dec r10
0031938C  45 33 FF                        xor r15d, r15d
0031938F  E9 49 FF FF FF                  jmp 0x1403192dd
00319394  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00319399  49 F7 D1                        not r9
0031939C  49 0F BC C1                     bsf rax, r9
003193A0  4C 8B FA                        mov r15, rdx
003193A3  4C 2B F9                        sub r15, rcx
003193A6  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
003193AA  49 C1 FF 03                     sar r15, 3
003193AE  49 C1 E7 06                     shl r15, 6
003193B2  4C 03 F8                        add r15, rax
003193B5  4C 3B 7C 24 48                  cmp r15, qword ptr [rsp + 0x48]
003193BA  0F 87 07 01 00 00               ja 0x1403194c7
003193C0  49 83 FF FF                     cmp r15, -1
003193C4  74 B0                           je 0x140319376
003193C6  4C 8B 6C 24 78                  mov r13, qword ptr [rsp + 0x78]
003193CB  E9 53 FE FF FF                  jmp 0x140319223
003193D0  4C 8B 0A                        mov r9, qword ptr [rdx]
003193D3  EB 86                           jmp 0x14031935b
003193D5  4D 85 E4                        test r12, r12
003193D8  74 0D                           je 0x1403193e7
003193DA  48 8B 46 48                     mov rax, qword ptr [rsi + 0x48]
003193DE  4C 3B E0                        cmp r12, rax
003193E1  0F 85 BC FD FF FF               jne 0x1403191a3
003193E7  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
003193EC  48 8B D7                        mov rdx, rdi
003193EF  48 8B CE                        mov rcx, rsi
003193F2  E8 BD AB 14 00                  call 0x140463fb4
003193F7  85 C0                           test eax, eax
003193F9  0F 85 A4 FD FF FF               jne 0x1403191a3
003193FF  48 8B D7                        mov rdx, rdi
00319402  48 8B CE                        mov rcx, rsi
00319405  E8 6E B7 09 00                  call 0x1403b4b78
0031940A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0031940F  48 85 C0                        test rax, rax
00319412  0F 85 01 04 00 00               jne 0x140319819
00319418  83 7C 24 40 06                  cmp dword ptr [rsp + 0x40], 6
0031941D  0F 84 3F FD FF FF               je 0x140319162
00319423  44 8D 40 01                     lea r8d, [rax + 1]
00319427  C7 44 24 40 06 00 00 00         mov dword ptr [rsp + 0x40], 6
0031942F  48 8B D7                        mov rdx, rdi
00319432  48 8B CE                        mov rcx, rsi
00319435  E8 AA 16 00 00                  call 0x14031aae4
0031943A  E9 64 FD FF FF                  jmp 0x1403191a3
0031943F  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00319444  45 33 FF                        xor r15d, r15d
00319447  49 C1 EA 06                     shr r10, 6
0031944B  4A 8D 04 D0                     lea rax, [rax + r10*8]
0031944F  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00319453  49 83 F9 FF                     cmp r9, -1
00319457  0F 84 4D 01 00 00               je 0x1403195aa
0031945D  49 0F BC C1                     bsf rax, r9
00319461  C7 44 24 64 00 00 00 00         mov dword ptr [rsp + 0x64], 0
00319469  41 0F 44 C5                     cmove eax, r13d
0031946D  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00319471  41 8D 0C 07                     lea ecx, [r15 + rax]
00319475  49 3B CE                        cmp rcx, r14
00319478  0F 83 24 01 00 00               jae 0x1403195a2
0031947E  4D 8B D1                        mov r10, r9
00319481  45 8B FE                        mov r15d, r14d
00319484  49 F7 D2                        not r10
00319487  49 8B C2                        mov rax, r10
0031948A  41 8B CF                        mov ecx, r15d
0031948D  D1 E9                           shr ecx, 1
0031948F  48 D3 E8                        shr rax, cl
00319492  4C 23 D0                        and r10, rax
00319495  0F 84 47 02 00 00               je 0x1403196e2
0031949B  44 2B F9                        sub r15d, ecx
0031949E  41 83 FF 01                     cmp r15d, 1
003194A2  77 E3                           ja 0x140319487
003194A4  49 0F BC C2                     bsf rax, r10
003194A8  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
003194AC  44 8B F8                        mov r15d, eax
003194AF  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
003194B4  48 2B D1                        sub rdx, rcx
003194B7  48 C1 FA 03                     sar rdx, 3
003194BB  48 C1 E2 06                     shl rdx, 6
003194BF  4C 03 FA                        add r15, rdx
003194C2  E9 EE FE FF FF                  jmp 0x1403193b5
003194C7  49 C7 C7 FF FF FF FF            mov r15, 0xffffffffffffffff
003194CE  E9 A3 FE FF FF                  jmp 0x140319376
003194D3  45 33 E4                        xor r12d, r12d
003194D6  E9 20 FD FF FF                  jmp 0x1403191fb
003194DB  84 C0                           test al, al
003194DD  0F 85 AC FC FF FF               jne 0x14031918f
003194E3  41 8B D1                        mov edx, r9d
003194E6  48 8D 4D C8                     lea rcx, [rbp - 0x38]
003194EA  4C 8D 0D 9F C3 37 00            lea r9, [rip + 0x37c39f]
003194F1  41 B8 08 00 00 00               mov r8d, 8
003194F7  E8 F4 74 1E 00                  call 0x1405009f0
003194FC  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00319500  E8 A3 FE F8 FF                  call 0x1402a93a8
00319505  44 8B 55 B0                     mov r10d, dword ptr [rbp - 0x50]
00319509  41 BC 01 00 00 00               mov r12d, 1
0031950F  E9 62 FA FF FF                  jmp 0x140318f76
00319514  4C 8B 54 24 38                  mov r10, qword ptr [rsp + 0x38]
00319519  4D 85 C9                        test r9, r9
0031951C  0F 89 11 02 00 00               jns 0x140319733
00319522  48 83 C2 08                     add rdx, 8
00319526  49 3B D2                        cmp rdx, r10
00319529  0F 87 3B FE FF FF               ja 0x14031936a
0031952F  4C 8B 0A                        mov r9, qword ptr [rdx]
00319532  EB E5                           jmp 0x140319519
00319534  48 8B C8                        mov rcx, rax
00319537  81 E1 FF 03 00 00               and ecx, 0x3ff
0031953D  49 8D 14 0F                     lea rdx, [r15 + rcx]
00319541  48 81 FA FF 03 00 00            cmp rdx, 0x3ff
00319548  0F 87 C7 FA FF FF               ja 0x140319015
0031954E  48 3B D1                        cmp rdx, rcx
00319551  0F 86 BE FA FF FF               jbe 0x140319015
00319557  4C 01 7D C0                     add qword ptr [rbp - 0x40], r15
0031955B  49 2B C0                        sub rax, r8
0031955E  4A 8D 0C 38                     lea rcx, [rax + r15]
00319562  48 33 C1                        xor rax, rcx
00319565  48 25 00 FC FF FF               and rax, 0xfffffffffffffc00
0031956B  48 33 C1                        xor rax, rcx
0031956E  49 89 02                        mov qword ptr [r10], rax
00319571  E9 19 FC FF FF                  jmp 0x14031918f
00319576  8B 56 28                        mov edx, dword ptr [rsi + 0x28]
00319579  F6 C2 04                        test dl, 4
0031957C  0F 84 15 FB FF FF               je 0x140319097
00319582  4C 8B C7                        mov r8, rdi
00319585  49 8B D4                        mov rdx, r12
00319588  48 8B CE                        mov rcx, rsi
0031958B  E8 F8 93 1B 00                  call 0x1404d2988
00319590  E9 02 FB FF FF                  jmp 0x140319097
00319595  41 8B CC                        mov ecx, r12d
00319598  B8 09 00 00 00                  mov eax, 9
0031959D  E9 F0 F8 FF FF                  jmp 0x140318e92
003195A2  49 F7 DF                        neg r15
003195A5  E9 05 FF FF FF                  jmp 0x1403194af
003195AA  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
003195AF  90                              nop
003195B0  48 83 C2 08                     add rdx, 8
003195B4  48 3B D0                        cmp rdx, rax
003195B7  0F 87 AD FD FF FF               ja 0x14031936a
003195BD  4C 8B 0A                        mov r9, qword ptr [rdx]
003195C0  49 83 F9 FF                     cmp r9, -1
003195C4  74 EA                           je 0x1403195b0
003195C6  45 33 FF                        xor r15d, r15d
003195C9  E9 8F FE FF FF                  jmp 0x14031945d
003195CE  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
003195D3  F6 44 24 48 3F                  test byte ptr [rsp + 0x48], 0x3f
003195D8  4C 8D 50 08                     lea r10, [rax + 8]
003195DC  4C 0F 44 D0                     cmove r10, rax
003195E0  4D 85 C9                        test r9, r9
003195E3  0F 84 DD 00 00 00               je 0x1403196c6
003195E9  48 83 C2 08                     add rdx, 8
003195ED  48 83 3A 00                     cmp qword ptr [rdx], 0
003195F1  75 5B                           jne 0x14031964e
003195F3  49 0F BD C1                     bsr rax, r9
003195F7  C7 44 24 50 00 00 00 00         mov dword ptr [rsp + 0x50], 0
003195FF  0F 84 D9 01 00 00               je 0x1403197de
00319605  B9 3F 00 00 00                  mov ecx, 0x3f
0031960A  2B C8                           sub ecx, eax
0031960C  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
00319610  4C 8B FA                        mov r15, rdx
00319613  44 8B C9                        mov r9d, ecx
00319616  4C 2B 7C 24 30                  sub r15, qword ptr [rsp + 0x30]
0031961B  49 C1 FF 03                     sar r15, 3
0031961F  49 C1 E7 06                     shl r15, 6
00319623  4D 2B F9                        sub r15, r9
00319626  4C 3B 7C 24 48                  cmp r15, qword ptr [rsp + 0x48]
0031962B  0F 87 39 FD FF FF               ja 0x14031936a
00319631  49 8B C6                        mov rax, r14
00319634  49 2B C1                        sub rax, r9
00319637  48 C1 E8 06                     shr rax, 6
0031963B  4C 8D 0C C2                     lea r9, [rdx + rax*8]
0031963F  48 83 C2 08                     add rdx, 8
00319643  49 3B D1                        cmp rdx, r9
00319646  74 45                           je 0x14031968d
00319648  48 83 3A 00                     cmp qword ptr [rdx], 0
0031964C  74 F1                           je 0x14031963f
0031964E  48 8B C2                        mov rax, rdx
00319651  49 3B D2                        cmp rdx, r10
00319654  0F 87 AA 01 00 00               ja 0x140319804
0031965A  48 83 C2 08                     add rdx, 8
0031965E  48 83 3A 00                     cmp qword ptr [rdx], 0
00319662  75 EA                           jne 0x14031964e
00319664  48 8B 00                        mov rax, qword ptr [rax]
00319667  4C 0F BD C8                     bsr r9, rax
0031966B  C7 44 24 54 00 00 00 00         mov dword ptr [rsp + 0x54], 0
00319673  0F 84 6D 01 00 00               je 0x1403197e6
00319679  B9 3F 00 00 00                  mov ecx, 0x3f
0031967E  41 BD 40 00 00 00               mov r13d, 0x40
00319684  41 2B C9                        sub ecx, r9d
00319687  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
0031968B  EB 83                           jmp 0x140319610
0031968D  45 8B CE                        mov r9d, r14d
00319690  44 2B C9                        sub r9d, ecx
00319693  41 83 E1 3F                     and r9d, 0x3f
00319697  74 23                           je 0x1403196bc
00319699  48 8B 02                        mov rax, qword ptr [rdx]
0031969C  48 0F BC C8                     bsf rcx, rax
003196A0  B8 40 00 00 00                  mov eax, 0x40
003196A5  C7 44 24 58 00 00 00 00         mov dword ptr [rsp + 0x58], 0
003196AD  0F 44 C8                        cmove ecx, eax
003196B0  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
003196B4  41 3B C9                        cmp ecx, r9d
003196B7  72 95                           jb 0x14031964e
003196B9  44 8B E8                        mov r13d, eax
003196BC  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
003196C1  E9 FA FC FF FF                  jmp 0x1403193c0
003196C6  33 C9                           xor ecx, ecx
003196C8  E9 43 FF FF FF                  jmp 0x140319610
003196CD  48 8D 05 AC C7 B1 00            lea rax, [rip + 0xb1c7ac]
003196D4  48 3B F0                        cmp rsi, rax
003196D7  0F 84 85 FA FF FF               je 0x140319162
003196DD  E9 BE FA FF FF                  jmp 0x1403191a0
003196E2  48 3B 55 90                     cmp rdx, qword ptr [rbp - 0x70]
003196E6  0F 84 7E FC FF FF               je 0x14031936a
003196EC  49 0F BD C1                     bsr rax, r9
003196F0  C7 44 24 68 00 00 00 00         mov dword ptr [rsp + 0x68], 0
003196F8  74 1B                           je 0x140319715
003196FA  4C 8B 4A 08                     mov r9, qword ptr [rdx + 8]
003196FE  41 BF 3F 00 00 00               mov r15d, 0x3f
00319704  44 2B F8                        sub r15d, eax
00319707  48 83 C2 08                     add rdx, 8
0031970B  44 89 7C 24 68                  mov dword ptr [rsp + 0x68], r15d
00319710  E9 3E FD FF FF                  jmp 0x140319453
00319715  4C 8B 4A 08                     mov r9, qword ptr [rdx + 8]
00319719  48 83 C2 08                     add rdx, 8
0031971D  41 BF 40 00 00 00               mov r15d, 0x40
00319723  41 BD 40 00 00 00               mov r13d, 0x40
00319729  44 89 7C 24 68                  mov dword ptr [rsp + 0x68], r15d
0031972E  E9 20 FD FF FF                  jmp 0x140319453
00319733  49 0F BD C9                     bsr rcx, r9
00319737  C7 44 24 5C 00 00 00 00         mov dword ptr [rsp + 0x5c], 0
0031973F  0F 84 B2 00 00 00               je 0x1403197f7
00319745  B8 3F 00 00 00                  mov eax, 0x3f
0031974A  2B C1                           sub eax, ecx
0031974C  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00319751  4C 8B FA                        mov r15, rdx
00319754  4C 2B F9                        sub r15, rcx
00319757  44 8B C8                        mov r9d, eax
0031975A  49 C1 FF 03                     sar r15, 3
0031975E  49 FF C7                        inc r15
00319761  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
00319765  49 C1 E7 06                     shl r15, 6
00319769  4D 2B F9                        sub r15, r9
0031976C  4C 3B 7C 24 48                  cmp r15, qword ptr [rsp + 0x48]
00319771  76 0C                           jbe 0x14031977f
00319773  49 C7 C7 FF FF FF FF            mov r15, 0xffffffffffffffff
0031977A  E9 F7 FB FF FF                  jmp 0x140319376
0031977F  49 8B CE                        mov rcx, r14
00319782  49 2B C9                        sub rcx, r9
00319785  0F 84 31 FF FF FF               je 0x1403196bc
0031978B  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
0031978F  48 83 C2 08                     add rdx, 8
00319793  4C 8B C8                        mov r9, rax
00319796  48 83 F9 40                     cmp rcx, 0x40
0031979A  72 1B                           jb 0x1403197b7
0031979C  48 85 C0                        test rax, rax
0031979F  0F 85 74 FD FF FF               jne 0x140319519
003197A5  48 83 E9 40                     sub rcx, 0x40
003197A9  0F 84 0D FF FF FF               je 0x1403196bc
003197AF  4C 8B 4A 08                     mov r9, qword ptr [rdx + 8]
003197B3  48 83 C2 08                     add rdx, 8
003197B7  49 0F BC C1                     bsf rax, r9
003197BB  C7 44 24 60 00 00 00 00         mov dword ptr [rsp + 0x60], 0
003197C3  41 0F 44 C5                     cmove eax, r13d
003197C7  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
003197CB  48 3B C1                        cmp rax, rcx
003197CE  0F 82 45 FD FF FF               jb 0x140319519
003197D4  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
003197D9  E9 E2 FB FF FF                  jmp 0x1403193c0
003197DE  41 8B CD                        mov ecx, r13d
003197E1  E9 26 FE FF FF                  jmp 0x14031960c
003197E6  B9 40 00 00 00                  mov ecx, 0x40
003197EB  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
003197EF  44 8B E9                        mov r13d, ecx
003197F2  E9 19 FE FF FF                  jmp 0x140319610
003197F7  B8 40 00 00 00                  mov eax, 0x40
003197FC  44 8B E8                        mov r13d, eax
003197FF  E9 48 FF FF FF                  jmp 0x14031974c
00319804  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00319809  49 C7 C7 FF FF FF FF            mov r15, 0xffffffffffffffff
00319810  45 8D 6F 41                     lea r13d, [r15 + 0x41]
00319814  E9 5D FB FF FF                  jmp 0x140319376
00319819  4C 8B E0                        mov r12, rax
0031981C  E9 7F F5 FF FF                  jmp 0x140318da0
00319821  4C 8B C7                        mov r8, rdi
00319824  49 8B D4                        mov rdx, r12
00319827  48 8B CE                        mov rcx, rsi
0031982A  E8 59 91 1B 00                  call 0x1404d2988
0031982F  E9 77 F5 FF FF                  jmp 0x140318dab
00319834  C6 45 B9 01                     mov byte ptr [rbp - 0x47], 1
00319838  E9 52 F9 FF FF                  jmp 0x14031918f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReservePtes(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m100;
    unsigned int v_stack_m104;
    unsigned int v_stack_m108;
    unsigned int v_stack_m10C;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m188;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_mFC;
    unsigned __int8 v_stack_mFD;
    unsigned __int16 v_stack_mFF;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p44;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned int v_stack_p54;
    unsigned int v_stack_p58;
    unsigned int v_stack_p5C;
    unsigned int v_stack_p60;
    unsigned int v_stack_p64;
    unsigned int v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (384);
    result = (*(unsigned __int64 *)(v_rip + 11475453)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m178 = 0;
    v_stack_m138 = v_xmm0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 40)))) & (1)) != 0) goto loc_00319122;
    if (a1 != (v_rip + 11659540)) goto loc_00319129;
    if (((unsigned int)(a2)) > 64) goto loc_00319129;
    result = MiCheckProcessorPteCache((unsigned int)((unsigned int)((unsigned int)(a2))), a2, a3, a4);
    v_stack_m180 = result;
    if (result == 0) goto loc_00319129;
loc_00318DA0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 40)))) & (4)) != 0) goto loc_00319821;
loc_00318DAB:
    if (((unsigned int)((unsigned int)(a2))) > 16) goto loc_00318DF7;
    a1 = 0;
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_00318DEF;
loc_00318DC3:
    if (*(unsigned __int64 *)(v_rip + 11620019) == 0) goto loc_00318DE0;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result))) & (16)) != 0) goto loc_0031916C;
    a2 = ~(*(unsigned __int64 *)(v_rip + 11620019));
    result = (*(unsigned __int64 *)(result)) & (a2);
loc_00318DE0:
    if (((a4) & (result)) != 0) goto loc_00318DEF;
    a1 = (unsigned int)((a1) + 1);
    a3 = (result) + (8);
    if (((unsigned int)(a1)) < ((unsigned int)((unsigned int)(a2)))) goto loc_00318DC3;
loc_00318DEF:
    if (((unsigned int)(a1)) == ((unsigned int)((unsigned int)(a2)))) goto loc_00319097;
loc_00318DF7:
    result = MiVaToFlushVm(result, a2, a3, a4);
    result = 0;
    a2 = 0;
    v_stack_mFD = 0;
    result = memset(v_stack_mE8, a2, 152, a4);
    v_r12 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 184))) >> (8));
    result = (unsigned __int8)((result) >> (3));
    result = (unsigned __int8)((result) & (1));
    v_stack_m188 = 0;
    v_stack_m100 = (unsigned __int8)(result);
    v_stack_m10C = 20;
    v_stack_m108 = 8;
    v_stack_m104 = 1;
    v_stack_m118 = result;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 184)))) & (15)) != 0) goto loc_00318E80;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    if (result != a1) goto loc_00319595;
loc_00318E80:
    a1 = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 184)))) & (15)) == 0) { a1 = 1; }
loc_00318E92:
    result = (unsigned int)(((unsigned int)(v_stack_m108)) & (0xFFFFFFDBULL));
    v_stack_m110 = (unsigned int)(a1);
    v_stack_m108 = (unsigned int)(result);
    v_stack_mFF = 0;
    v_stack_mFC = 0;
    v_stack_mF8 = 0;
    v_stack_mF0 = 0;
loc_00318EC2:
    if (0 >= ((unsigned int)(a2))) goto loc_00319089;
    a1 = (((*(unsigned __int64 *)(0)) & (0xC01ULL)) == 0) ? 1 : 0;
    result = (((*(unsigned __int64 *)(0)) & (992)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00318F22;
    if (*(unsigned __int64 *)(v_rip + 11619731) == 0) goto loc_00318EFD;
    if ((((unsigned __int8)(*(unsigned __int64 *)(0))) & (16)) != 0) goto loc_00318F40;
    result = ~(*(unsigned __int64 *)(v_rip + 11619731));
    v_rbx = (*(unsigned __int64 *)(0)) & (result);
loc_00318EFD:
    v_rbx = (v_rbx) >> (32);
    *(unsigned __int64 *)(0) = *(unsigned __int64 *)(v_rip - 3180164);
    if ((unsigned int)(v_rbx) != 0) goto loc_00318F46;
    v_stack_m188 = 0;
loc_00318F19:
    v_r14 = (0) + 1;
    v_rsi = (0) + (8);
    goto loc_00318EC2;
loc_00318F22:
    v_rdi = ((unsigned int)(a2)) - (v_r14);
    v_stack_m198 = v_rbx;
    result = KeBugCheckEx(26, (unsigned int)(0x5100ULL), v_rsi, v_rdi);
loc_00318F40:
    v_rbx = (v_rbx) & (-17);
    goto loc_00318EFD;
loc_00318F46:
    if (((unsigned int)(v_rbx)) != 0) goto loc_003190C2;
    if ((unsigned int)((unsigned int)(0x5100ULL)) == 0) goto loc_00318F19;
    v_rbx = (v_rsi) << (25);
    result = (v_rsi) << (25);
    v_rbx = (v_rbx) - (result);
    v_rbx = (v_rbx) >> (16);
    if (v_stack_m110 != 1) goto loc_00319283;
loc_00318F76:
loc_00318F7A:
    if ((unsigned int)((unsigned int)(v_stack_mFC)) == 0) goto loc_00319015;
    if ((((unsigned __int8)((unsigned int)(v_stack_m108))) & (2)) != 0) goto loc_00318FD5;
    if (((*(unsigned __int64 *)(v_stack_mF0 + (unsigned int)(v_stack_mFC) - 1 * 8)) & (0xC00ULL)) != 0) goto loc_00318FD5;
    a3 = (unsigned int)((*(unsigned __int64 *)(v_stack_mF0 + (unsigned int)(v_stack_mFC) - 1 * 8)) & (0x3FFULL));
    a1 = (*(unsigned __int64 *)(v_stack_mF0 + (unsigned int)(v_stack_mFC) - 1 * 8)) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (a3 + 1) << (12);
    a2 = (a2) + (a1);
    if (a2 != v_rbx) goto loc_00318FD5;
    if ((1 + a3 * 1) <= 0x3FFULL) goto loc_003192B2;
loc_00318FD5:
    if ((unsigned int)((unsigned int)(v_stack_mFC)) == 0) goto loc_00319015;
    if ((((unsigned __int8)((unsigned int)(v_stack_m108))) & (2)) != 0) goto loc_00319015;
    if (((*(unsigned __int64 *)(v_stack_mF0 + (unsigned int)(v_stack_mFC) - 1 * 8)) & (0xC00ULL)) != 0) goto loc_00319015;
    a3 = (1) << (12);
    a1 = (*(unsigned __int64 *)(v_stack_mF0 + (unsigned int)(v_stack_mFC) - 1 * 8)) & (0xFFFFFFFFFFFFF000ULL);
    if (a1 == (v_rbx + a3 * 1)) goto loc_00319534;
loc_00319015:
    if (((unsigned int)((unsigned int)(v_stack_mFC))) == v_stack_m10C) goto loc_0031917A;
loc_0031901F:
    if (1 == 0) goto loc_0031918F;
    a2 = (unsigned int)(0x400ULL);
    if ((1 - 1) <= 0x3FFULL) { a2 = 1; }
    a1 = (v_rbx) & (0xFFFFFFFFFFFFF000ULL);
    result = (unsigned int)((a2 - 1) & (0x3FFULL));
    result = (result) | (a1);
    a1 = (a2) << (12);
    v_rbx = (v_rbx) + (a1);
    *(unsigned __int64 *)(v_stack_mB8 + (unsigned int)((unsigned int)((unsigned int)(v_stack_mFC))) * 8 - 56) = result;
    a4 = (unsigned int)(((unsigned int)(v_stack_mFC)) + 1);
    v_stack_mFC = (unsigned int)(a4);
    v_r15 = (1) - (a2);
    if (condition_is_equal) goto loc_0031901F;
    if (((unsigned int)(a4)) != v_stack_m10C) goto loc_0031901F;
    v_r12 = 0;
    goto loc_00318F7A;
loc_00319089:
    result = MiFlushTbList(v_stack_m118, a2, a3, a4);
loc_00319097:
loc_0031909A:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (384);
    return result;
loc_003190C2:
    result = MiCompareTbFlushTimeStamp((unsigned int)((unsigned int)(v_stack_p18)), a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00319175;
    a2 = (v_rsi) << (25);
    result = (result) << (25);
    a2 = (a2) - (result);
    a4 = 0;
    a2 = (a2) >> (16);
    result = MiInsertTbFlushEntry(v_stack_m118, a2, v_r15, a4);
loc_00319102:
    v_stack_p30 = (unsigned int)((unsigned int)((unsigned int)(v_r15)));
loc_00319109:
    goto loc_00318F19;
loc_00319122:
    v_r14 = (v_rdi) >> (4);
loc_00319129:
    if (((unsigned int)(v_stack_p18)) < 512) goto loc_003191A0;
    result = MiEmptyPteBins(v_rsi, v_rdi, 6, a4);
    result = MiExpandPtes(v_rsi, v_rdi, 6, a4);
    if (result != 0) goto loc_00319576;
    if (v_rsi != v_r15) goto loc_003196CD;
loc_00319162:
    result = 0;
    goto loc_0031909A;
loc_0031916C:
    result = (result) & (-17);
    goto loc_00318DE0;
loc_00319175:
    goto loc_00319102;
loc_0031917A:
    if ((unsigned int)(result) == 0) goto loc_003194DB;
    if ((unsigned __int8)(v_stack_mFF) == 0) goto loc_00319834;
loc_0031918F:
    v_r12 = 0;
    goto loc_00319109;
loc_003191A0:
    v_r12 = 0;
loc_003191A3:
    v_stack_p78 = v_rsi;
    if (*(unsigned __int64 *)(v_rsi) == 0) goto loc_003193D5;
    if (*(unsigned __int64 *)(v_rsi + 72) == 0) goto loc_003191FB;
    a1 = (*(unsigned __int64 *)(v_rsi + 72)) >> (6);
    if ((*(unsigned __int64 *)(v_rsi)) < (*(unsigned __int64 *)(v_rsi + 72))) goto loc_003194D3;
    result = (*(unsigned __int64 *)(v_rsi)) - (*(unsigned __int64 *)(v_rsi + 72));
    v_stack_m130 = *(unsigned __int64 *)(v_rsi + 8) + a1 * 8;
    v_stack_m138 = result;
    v_stack_p78 = v_stack_m138;
    if (*(unsigned __int64 *)(v_rsi + 64) != 0) {
        a3 = (*(unsigned __int64 *)(v_rsi + 64)) - (*(unsigned __int64 *)(v_rsi + 72));
    }
    v_r15 = 0;
    v_stack_p30 = *(unsigned __int64 *)(v_stack_m138 + 8);
    if (a3 < (*(unsigned __int64 *)(v_stack_m138))) { v_r15 = a3; }
    if (v_r14 != 0) goto loc_003192D7;
    v_r15 = (v_r15) & (-8);
loc_00319223:
    if (v_r15 == -1) goto loc_003193D5;
    result = RtlInterlockedSetClearRunEx(v_stack_m138, v_r15, v_r14, a4);
    if ((unsigned int)(result) == 0) goto loc_003191A3;
    result = -(v_rdi);
    if (v_stack_m138 == v_stack_m138) {
        v_r15 = (v_r15) + (*(unsigned __int64 *)(v_rsi + 72));
    }
    a1 = (v_r15) << (4);
    *(unsigned __int64 *)(v_rsi + 64) = v_r14 + v_r15 * 1;
    if (((*(unsigned __int8 *)(v_rsi + 40)) & (1)) == 0) { a1 = v_r15; }
    v_stack_p38 = *(unsigned __int64 *)(v_rsi + 32) + a1 * 8;
    goto loc_00318DA0;
loc_00319283:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m138) - 1)) & (4)) != 0) goto loc_00318F76;
    if (v_stack_p18 < v_r14) goto loc_00318F76;
    if (v_stack_p18 > 0) goto loc_00318F76;
    v_r10 = (unsigned int)((*(unsigned __int64 *)(v_stack_m138) - 1) | (4));
    v_stack_m108 = (unsigned int)(v_r10);
    goto loc_00318F76;
loc_003192B2:
    if (a1 <= v_r14) goto loc_00318FD5;
    result = (0) ^ (0 + v_r15 * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (0 + v_r15 * 1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m138)) = result;
    goto loc_0031918F;
loc_003192D7:
loc_003192DD:
    v_stack_p70 = v_r15;
    result = (v_r10) - (v_r15);
    v_stack_p44 = 0;
    result = (result) + 1;
    if (result < v_r14) goto loc_00319773;
    result = (v_r10) - (v_r14);
    result = (result) + 1;
    v_stack_p48 = result;
    result = (result) >> (6);
    v_stack_p38 = 0 + v_r15 * 1 + result * 8;
    result = (v_r15) >> (6);
    a1 = (unsigned __int8)(((unsigned __int8)(v_r15)) & (63));
    a4 = (1) << ((unsigned __int8)(a1));
    a4 = (a4) - 1;
    a4 = (a4) | (*(unsigned __int64 *)(0 + v_r15 * 1 + result * 8));
    if (v_r14 > 127) goto loc_003195CE;
    if (v_r14 >= 64) goto loc_00319514;
    if (v_r14 > 1) goto loc_0031943F;
loc_0031935B:
    if (a4 != -1) goto loc_00319394;
    a2 = (0 + v_r15 * 1 + result * 8) + (8);
    if (a2 <= v_stack_p38) goto loc_003193D0;
loc_0031936A:
loc_00319376:
    if (v_stack_p70 == 0) goto loc_003193C6;
    v_r10 = v_r14 + v_r14 * 1;
    if ((v_r14 + v_r14 * 1) > (*(unsigned __int64 *)(v_stack_m138))) { v_r10 = *(unsigned __int64 *)(v_stack_m138); }
    v_r10 = (v_r10) - 1;
    v_r15 = 0;
    goto loc_003192DD;
loc_00319394:
    a4 = ~(a4);
    v_r15 = (a2) - (v_stack_p30);
    v_stack_p44 = (unsigned int)(v_stack_p38);
    v_r15 = (v_r15) >> (3);
    v_r15 = (v_r15) << (6);
    v_r15 = (v_r15) + (v_stack_p38);
loc_003193B5:
    if (v_r15 > v_stack_p48) goto loc_003194C7;
loc_003193C0:
    if (v_r15 == -1) goto loc_00319376;
loc_003193C6:
    goto loc_00319223;
loc_003193D0:
    goto loc_0031935B;
loc_003193D5:
    if (*(unsigned __int64 *)(v_rsi + 32) + a1 * 8 == 0) goto loc_003193E7;
    if ((*(unsigned __int64 *)(v_rsi + 32) + a1 * 8) != (*(unsigned __int64 *)(v_rsi + 72))) goto loc_003191A3;
loc_003193E7:
    result = MiMakeSystemPtesAppear(v_rsi, v_rdi, v_stack_p40, *(unsigned __int64 *)(a2));
    if ((unsigned int)(result) != 0) goto loc_003191A3;
    result = MiExpandPtes(v_rsi, v_rdi, v_stack_p40, *(unsigned __int64 *)(a2));
    v_stack_p38 = result;
    if (result != 0) goto loc_00319819;
    if (v_stack_p40 == 6) goto loc_00319162;
    v_stack_p40 = 6;
    result = MiEmptyPteBins(v_rsi, v_rdi, result + 1, *(unsigned __int64 *)(a2));
    goto loc_003191A3;
loc_0031943F:
    v_r15 = 0;
    v_r10 = (v_r10) >> (6);
    v_stack_m128 = v_stack_p30 + v_r10 * 8;
loc_00319453:
    if ((*(unsigned __int64 *)(a2)) == -1) goto loc_003195AA;
loc_0031945D:
    v_stack_p64 = 0;
    result = v_stack_p30 + v_r10 * 8;
    if ((*(unsigned __int64 *)(a2)) == -1) { result = (unsigned int)(v_stack_p78); }
    v_stack_p64 = (unsigned int)(result);
    if ((v_r15 + result * 1) >= v_r14) goto loc_003195A2;
    v_r10 = ~(*(unsigned __int64 *)(a2));
loc_00319487:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r14))))) >> (1));
    result = (v_r10) >> ((unsigned __int8)(a1));
    v_r10 = (v_r10) & (result);
    if (condition_is_equal) goto loc_003196E2;
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - ((unsigned int)(a1)));
    if (((unsigned int)(v_r15)) > 1) goto loc_00319487;
    v_stack_p44 = (unsigned int)(result);
loc_003194AF:
    a2 = (v_rdi) - (v_stack_p30);
    a2 = (a2) >> (3);
    a2 = (a2) << (6);
    v_r15 = ((unsigned int)((unsigned int)(result))) + (a2);
    goto loc_003193B5;
loc_003194C7:
    goto loc_00319376;
loc_003194D3:
    v_r12 = 0;
    goto loc_003191FB;
loc_003194DB:
    if ((unsigned __int8)(result) != 0) goto loc_0031918F;
    result = qsort(v_stack_mF0, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a2))), 8, v_rip + 3654559);
    result = MiCompressTbFlushList(v_stack_m118, (unsigned int)((unsigned int)(*(unsigned __int64 *)(a2))), 8, v_rip + 3654559);
    goto loc_00318F76;
loc_00319514:
loc_00319519:
    if (!sign_flag) goto loc_00319733;
    a2 = ((unsigned int)((unsigned int)(*(unsigned __int64 *)(a2)))) + (8);
    if (a2 > v_stack_p38) goto loc_0031936A;
    goto loc_00319519;
loc_00319534:
    a1 = (unsigned int)((result) & (0x3FFULL));
    if ((-1 + a1 * 1) > 0x3FFULL) goto loc_00319015;
    if ((-1 + a1 * 1) <= a1) goto loc_00319015;
    result = (result) - (8);
    result = (result) ^ (result + -1 * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (result + -1 * 1);
    *(unsigned __int64 *)(v_stack_p38) = result;
    goto loc_0031918F;
loc_00319576:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsi + 40)))) & (4)) == 0) goto loc_00319097;
    result = MiCheckPteReserve(v_rsi, 1, v_rdi, *(unsigned __int64 *)(a2));
    goto loc_00319097;
loc_00319595:
    goto loc_00318E92;
loc_003195A2:
    v_r15 = -(-1);
    goto loc_003194AF;
loc_003195AA:
loc_003195B0:
    a2 = (1) + (8);
    if (a2 > v_stack_p38) goto loc_0031936A;
    if ((*(unsigned __int64 *)(a2)) == -1) goto loc_003195B0;
    v_r15 = 0;
    goto loc_0031945D;
loc_003195CE:
    v_r10 = v_stack_p38 + 8;
    if (((v_stack_p48) & (63)) == 0) { v_r10 = v_stack_p38; }
    if (*(unsigned __int64 *)(a2) == 0) goto loc_003196C6;
    a2 = (a2) + (8);
    if ((*(unsigned __int64 *)(a2)) != 0) goto loc_0031964E;
    v_stack_p50 = 0;
    if ((*(unsigned __int64 *)(a2)) == 0) goto loc_003197DE;
    a1 = (unsigned int)((63) - ((unsigned int)(v_stack_p38)));
loc_0031960C:
    v_stack_p50 = (unsigned int)(a1);
loc_00319610:
    v_r15 = (a2) - (v_stack_p30);
    v_r15 = (v_r15) >> (3);
    v_r15 = (v_r15) << (6);
    v_r15 = (v_r15) - ((unsigned int)((unsigned int)(a1)));
    if (v_r15 > v_stack_p48) goto loc_0031936A;
    result = (v_r14) - ((unsigned int)((unsigned int)(a1)));
    result = (result) >> (6);
loc_0031963F:
    a2 = (a2) + (8);
    if (a2 == (a2 + result * 8)) goto loc_0031968D;
    if ((*(unsigned __int64 *)(a2)) == 0) goto loc_0031963F;
loc_0031964E:
    if (a2 > v_r10) goto loc_00319804;
    a2 = (a2) + (8);
    if ((*(unsigned __int64 *)(a2)) != 0) goto loc_0031964E;
    v_stack_p54 = 0;
    if ((*(unsigned __int64 *)(a2)) == 0) goto loc_003197E6;
    a1 = (unsigned int)((63) - ((unsigned int)(a2 + result * 8)));
    v_stack_p54 = (unsigned int)(a1);
    goto loc_00319610;
loc_0031968D:
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - ((unsigned int)(a1)));
    a4 = (unsigned int)((a4) & (63));
    if (condition_is_equal) goto loc_003196BC;
    v_stack_p58 = 0;
    if (condition_is_equal) { a1 = 64; }
    v_stack_p58 = (unsigned int)(a1);
    if (((unsigned int)(a1)) < ((unsigned int)(a4))) goto loc_0031964E;
loc_003196BC:
    goto loc_003193C0;
loc_003196C6:
    a1 = 0;
    goto loc_00319610;
loc_003196CD:
    if (v_rsi == (v_rip + 11650988)) goto loc_00319162;
    goto loc_003191A0;
loc_003196E2:
    if (a2 == v_stack_m128) goto loc_0031936A;
    v_stack_p68 = 0;
    if (a2 == v_stack_m128) goto loc_00319715;
    v_r15 = (unsigned int)((63) - ((unsigned int)(v_rip + 11650988)));
    a2 = (a2) + (8);
    v_stack_p68 = (unsigned int)(v_r15);
    goto loc_00319453;
loc_00319715:
    a2 = (a2) + (8);
    v_stack_p68 = 64;
    goto loc_00319453;
loc_00319733:
    v_stack_p5C = 0;
    if (condition_is_equal) goto loc_003197F7;
    result = (unsigned int)((63) - (0));
loc_0031974C:
    v_r15 = (a2) - (v_stack_p30);
    v_r15 = (v_r15) >> (3);
    v_r15 = (v_r15) + 1;
    v_stack_p5C = (unsigned int)(result);
    v_r15 = (v_r15) << (6);
    v_r15 = (v_r15) - ((unsigned int)((unsigned int)(result)));
    if (v_r15 <= v_stack_p48) goto loc_0031977F;
loc_00319773:
    goto loc_00319376;
loc_0031977F:
    a1 = (v_r14) - ((unsigned int)((unsigned int)(result)));
    if (condition_is_equal) goto loc_003196BC;
    a2 = (a2) + (8);
    if (a1 < 64) goto loc_003197B7;
    if (*(unsigned __int64 *)(a2 + 8) != 0) goto loc_00319519;
    a1 = (a1) - (64);
    if (condition_is_equal) goto loc_003196BC;
    a2 = (a2) + (8);
loc_003197B7:
    v_stack_p60 = 0;
    result = *(unsigned __int64 *)(a2 + 8);
    if (condition_is_equal) { result = 64; }
    v_stack_p60 = (unsigned int)(result);
    if (result < a1) goto loc_00319519;
    goto loc_003193C0;
loc_003197DE:
    goto loc_0031960C;
loc_003197E6:
    v_stack_p54 = 64;
    goto loc_00319610;
loc_003197F7:
    goto loc_0031974C;
loc_00319804:
    goto loc_00319376;
loc_00319819:
    goto loc_00318DA0;
loc_00319821:
    result = MiCheckPteReserve(v_rsi, 64, v_rdi, *(unsigned __int64 *)(a2 + 8));
    goto loc_00318DAB;
loc_00319834:
    v_stack_mFF = 1;
    goto loc_0031918F;
}
```

## 5. (Beta) C Style

```c
int64_t MiReservePtes(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m100;
    uint32_t v_stack_m104;
    uint32_t v_stack_m108;
    uint32_t v_stack_m10C;
    uint32_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint32_t v_stack_m178;
    uint64_t v_stack_m180;
    uint32_t v_stack_m188;
    uint64_t v_stack_m198;
    uint64_t v_stack_m48;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_mFC;
    uint8_t v_stack_mFD;
    uint16_t v_stack_mFF;
    uint64_t v_stack_p18;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p44;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint32_t v_stack_p54;
    uint32_t v_stack_p58;
    uint32_t v_stack_p5C;
    uint32_t v_stack_p60;
    uint32_t v_stack_p64;
    uint32_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (384);
    result = (*(uint64_t *)(v_rip + 0xAF19FD)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m178 = 0;
    v_stack_m138 = v_xmm0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) & (1)) != 0) goto loc_00319122;
    if (Arg1 != (v_rip + 11659540)) goto loc_00319129;
    if (((uint32_t)(Arg2)) > 64) goto loc_00319129;
    result = MiCheckProcessorPteCache((uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg2, a3, a4);
    v_stack_m180 = result;
    if (result == 0) goto loc_00319129;
loc_00318DA0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) & (4)) != 0) goto loc_00319821;
loc_00318DAB:
    if (((uint32_t)((uint32_t)(Arg2))) > 16) goto loc_00318DF7;
    Arg1 = 0;
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_00318DEF;
loc_00318DC3:
    if (*(uint64_t *)(v_rip + 0xB14EB3) == 0) goto loc_00318DE0;
    if ((((uint8_t)(*(uint64_t *)(result))) & (16)) != 0) goto loc_0031916C;
    Arg2 = ~(*(uint64_t *)(v_rip + 0xB14EB3));
    result = (*(uint64_t *)(result)) & (Arg2);
loc_00318DE0:
    if (((a4) & (result)) != 0) goto loc_00318DEF;
    Arg1 = (uint32_t)((Arg1) + 1);
    a3 = (result) + (8);
    if (((uint32_t)(Arg1)) < ((uint32_t)((uint32_t)(Arg2)))) goto loc_00318DC3;
loc_00318DEF:
    if (((uint32_t)(Arg1)) == ((uint32_t)((uint32_t)(Arg2)))) goto loc_00319097;
loc_00318DF7:
    result = MiVaToFlushVm(result, Arg2, a3, a4);
    result = 0;
    Arg2 = 0;
    v_stack_mFD = 0;
    result = memset(v_stack_mE8, Arg2, 152, a4);
    local_r12 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0xB8))) >> (8));
    result = (uint8_t)((result) >> (3));
    result = (uint8_t)((result) & (1));
    v_stack_m188 = 0;
    v_stack_m100 = (uint8_t)(result);
    v_stack_m10C = 20;
    v_stack_m108 = 8;
    v_stack_m104 = 1;
    v_stack_m118 = result;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xB8)))) & (15)) != 0) goto loc_00318E80;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    if (result != Arg1) goto loc_00319595;
loc_00318E80:
    Arg1 = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xB8)))) & (15)) == 0) { Arg1 = 1; }
loc_00318E92:
    result = (uint32_t)(((uint32_t)(v_stack_m108)) & (0xFFFFFFDBULL));
    v_stack_m110 = (uint32_t)(Arg1);
    v_stack_m108 = (uint32_t)(result);
    v_stack_mFF = 0;
    v_stack_mFC = 0;
    v_stack_mF8 = 0;
    v_stack_mF0 = 0;
loc_00318EC2:
    if (0 >= ((uint32_t)(Arg2))) goto loc_00319089;
    Arg1 = (((*(uint64_t *)(0)) & (0xC01ULL)) == 0) ? 1 : 0;
    result = (((*(uint64_t *)(0)) & (992)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00318F22;
    if (*(uint64_t *)(v_rip + 0xB14D93) == 0) goto loc_00318EFD;
    if ((((uint8_t)(*(uint64_t *)(0))) & (16)) != 0) goto loc_00318F40;
    result = ~(*(uint64_t *)(v_rip + 0xB14D93));
    local_rbx = (*(uint64_t *)(0)) & (result);
loc_00318EFD:
    local_rbx = (local_rbx) >> (32);
    *(uint64_t *)(0) = *(uint64_t *)(v_rip - 0x308684);
    if ((uint32_t)(local_rbx) != 0) goto loc_00318F46;
    v_stack_m188 = 0;
loc_00318F19:
    local_r14 = (0) + 1;
    local_rsi = (0) + (8);
    goto loc_00318EC2;
loc_00318F22:
    local_rdi = ((uint32_t)(Arg2)) - (local_r14);
    v_stack_m198 = local_rbx;
    result = KeBugCheckEx(26, (uint32_t)(0x5100ULL), local_rsi, local_rdi);
loc_00318F40:
    local_rbx = (local_rbx) & (-17);
    goto loc_00318EFD;
loc_00318F46:
    if (((uint32_t)(local_rbx)) != 0) goto loc_003190C2;
    if ((uint32_t)((uint32_t)(0x5100ULL)) == 0) goto loc_00318F19;
    local_rbx = (local_rsi) << (25);
    result = (local_rsi) << (25);
    local_rbx = (local_rbx) - (result);
    local_rbx = (local_rbx) >> (16);
    if (v_stack_m110 != 1) goto loc_00319283;
loc_00318F76:
loc_00318F7A:
    if ((uint32_t)((uint32_t)(v_stack_mFC)) == 0) goto loc_00319015;
    if ((((uint8_t)((uint32_t)(v_stack_m108))) & (2)) != 0) goto loc_00318FD5;
    if (((*(uint64_t *)(v_stack_mF0 + (uint32_t)(v_stack_mFC) - 0x1 * 8)) & (0xC00ULL)) != 0) goto loc_00318FD5;
    a3 = (uint32_t)((*(uint64_t *)(v_stack_mF0 + (uint32_t)(v_stack_mFC) - 0x1 * 8)) & (0x3FFULL));
    Arg1 = (*(uint64_t *)(v_stack_mF0 + (uint32_t)(v_stack_mFC) - 0x1 * 8)) & (0xFFFFFFFFFFFFF000ULL);
    Arg2 = (a3 + 1) << (12);
    Arg2 = (Arg2) + (Arg1);
    if (Arg2 != local_rbx) goto loc_00318FD5;
    if ((1 + a3 * 1) <= 0x3FFULL) goto loc_003192B2;
loc_00318FD5:
    if ((uint32_t)((uint32_t)(v_stack_mFC)) == 0) goto loc_00319015;
    if ((((uint8_t)((uint32_t)(v_stack_m108))) & (2)) != 0) goto loc_00319015;
    if (((*(uint64_t *)(v_stack_mF0 + (uint32_t)(v_stack_mFC) - 0x1 * 8)) & (0xC00ULL)) != 0) goto loc_00319015;
    a3 = (1) << (12);
    Arg1 = (*(uint64_t *)(v_stack_mF0 + (uint32_t)(v_stack_mFC) - 0x1 * 8)) & (0xFFFFFFFFFFFFF000ULL);
    if (Arg1 == (local_rbx + a3 * 1)) goto loc_00319534;
loc_00319015:
    if (((uint32_t)((uint32_t)(v_stack_mFC))) == v_stack_m10C) goto loc_0031917A;
loc_0031901F:
    if (1 == 0) goto loc_0031918F;
    Arg2 = (uint32_t)(0x400ULL);
    if ((1 - 1) <= 0x3FFULL) { Arg2 = 1; }
    Arg1 = (local_rbx) & (0xFFFFFFFFFFFFF000ULL);
    result = (uint32_t)((Arg2 - 1) & (0x3FFULL));
    result = (result) | (Arg1);
    Arg1 = (Arg2) << (12);
    local_rbx = (local_rbx) + (Arg1);
    *(uint64_t *)(v_stack_mB8 + (uint32_t)((uint32_t)((uint32_t)(v_stack_mFC))) * 8 - 0x38) = result;
    a4 = (uint32_t)(((uint32_t)(v_stack_mFC)) + 1);
    v_stack_mFC = (uint32_t)(a4);
    local_r15 = (1) - (Arg2);
    if (condition_is_equal) goto loc_0031901F;
    if (((uint32_t)(a4)) != v_stack_m10C) goto loc_0031901F;
    local_r12 = 0;
    goto loc_00318F7A;
loc_00319089:
    result = MiFlushTbList(v_stack_m118, Arg2, a3, a4);
loc_00319097:
loc_0031909A:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (384);
    return result;
loc_003190C2:
    result = MiCompareTbFlushTimeStamp((uint32_t)((uint32_t)(v_stack_p18)), Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00319175;
    Arg2 = (local_rsi) << (25);
    result = (result) << (25);
    Arg2 = (Arg2) - (result);
    a4 = 0;
    Arg2 = (Arg2) >> (16);
    result = MiInsertTbFlushEntry(v_stack_m118, Arg2, local_r15, a4);
loc_00319102:
    v_stack_p30 = (uint32_t)((uint32_t)((uint32_t)(local_r15)));
loc_00319109:
    goto loc_00318F19;
loc_00319122:
    local_r14 = (local_rdi) >> (4);
loc_00319129:
    if (((uint32_t)(v_stack_p18)) < 512) goto loc_003191A0;
    result = MiEmptyPteBins(local_rsi, local_rdi, 6, a4);
    result = MiExpandPtes(local_rsi, local_rdi, 6, a4);
    if (result != 0) goto loc_00319576;
    if (local_rsi != local_r15) goto loc_003196CD;
loc_00319162:
    result = 0;
    goto loc_0031909A;
loc_0031916C:
    result = (result) & (-17);
    goto loc_00318DE0;
loc_00319175:
    goto loc_00319102;
loc_0031917A:
    if ((uint32_t)(result) == 0) goto loc_003194DB;
    if ((uint8_t)(v_stack_mFF) == 0) goto loc_00319834;
loc_0031918F:
    local_r12 = 0;
    goto loc_00319109;
loc_003191A0:
    local_r12 = 0;
loc_003191A3:
    v_stack_p78 = local_rsi;
    if (*(uint64_t *)(local_rsi) == 0) goto loc_003193D5;
    if (*(uint64_t *)(local_rsi + 0x48) == 0) goto loc_003191FB;
    Arg1 = (*(uint64_t *)(local_rsi + 0x48)) >> (6);
    if ((*(uint64_t *)(local_rsi)) < (*(uint64_t *)(local_rsi + 0x48))) goto loc_003194D3;
    result = (*(uint64_t *)(local_rsi)) - (*(uint64_t *)(local_rsi + 0x48));
    v_stack_m130 = *(uint64_t *)(local_rsi + 0x8) + Arg1 * 8;
    v_stack_m138 = result;
    v_stack_p78 = v_stack_m138;
    if (*(uint64_t *)(local_rsi + 0x40) != 0) {
        a3 = (*(uint64_t *)(local_rsi + 0x40)) - (*(uint64_t *)(local_rsi + 0x48));
    }
    local_r15 = 0;
    v_stack_p30 = *(uint64_t *)(v_stack_m138 + 0x8);
    if (a3 < (*(uint64_t *)(v_stack_m138))) { local_r15 = a3; }
    if (local_r14 != 0) goto loc_003192D7;
    local_r15 = (local_r15) & (-8);
loc_00319223:
    if (local_r15 == -1) goto loc_003193D5;
    result = RtlInterlockedSetClearRunEx(v_stack_m138, local_r15, local_r14, a4);
    if ((uint32_t)(result) == 0) goto loc_003191A3;
    result = -(local_rdi);
    if (v_stack_m138 == v_stack_m138) {
        local_r15 = (local_r15) + (*(uint64_t *)(local_rsi + 0x48));
    }
    Arg1 = (local_r15) << (4);
    *(uint64_t *)(local_rsi + 0x40) = local_r14 + local_r15 * 1;
    if (((*(uint8_t *)(local_rsi + 0x28)) & (1)) == 0) { Arg1 = local_r15; }
    v_stack_p38 = *(uint64_t *)(local_rsi + 0x20) + Arg1 * 8;
    goto loc_00318DA0;
loc_00319283:
    if ((((uint8_t)(*(uint64_t *)(v_stack_m138) - 1)) & (4)) != 0) goto loc_00318F76;
    if (v_stack_p18 < local_r14) goto loc_00318F76;
    if (v_stack_p18 > 0) goto loc_00318F76;
    local_r10 = (uint32_t)((*(uint64_t *)(v_stack_m138) - 1) | (4));
    v_stack_m108 = (uint32_t)(local_r10);
    goto loc_00318F76;
loc_003192B2:
    if (Arg1 <= local_r14) goto loc_00318FD5;
    result = (0) ^ (0 + local_r15 * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (0 + local_r15 * 1);
    *(uint64_t *)(*(uint64_t *)(v_stack_m138)) = result;
    goto loc_0031918F;
loc_003192D7:
loc_003192DD:
    v_stack_p70 = local_r15;
    result = (local_r10) - (local_r15);
    v_stack_p44 = 0;
    result = (result) + 1;
    if (result < local_r14) goto loc_00319773;
    result = (local_r10) - (local_r14);
    result = (result) + 1;
    v_stack_p48 = result;
    result = (result) >> (6);
    v_stack_p38 = 0 + local_r15 * 1 + result * 8;
    result = (local_r15) >> (6);
    Arg1 = (uint8_t)(((uint8_t)(local_r15)) & (63));
    a4 = (1) << ((uint8_t)(Arg1));
    a4 = (a4) - 1;
    a4 = (a4) | (*(uint64_t *)(0 + local_r15 * 1 + result * 8));
    if (local_r14 > 127) goto loc_003195CE;
    if (local_r14 >= 64) goto loc_00319514;
    if (local_r14 > 1) goto loc_0031943F;
loc_0031935B:
    if (a4 != -1) goto loc_00319394;
    Arg2 = (0 + local_r15 * 1 + result * 8) + (8);
    if (Arg2 <= v_stack_p38) goto loc_003193D0;
loc_0031936A:
loc_00319376:
    if (v_stack_p70 == 0) goto loc_003193C6;
    local_r10 = local_r14 + local_r14 * 1;
    if ((local_r14 + local_r14 * 1) > (*(uint64_t *)(v_stack_m138))) { local_r10 = *(uint64_t *)(v_stack_m138); }
    local_r10 = (local_r10) - 1;
    local_r15 = 0;
    goto loc_003192DD;
loc_00319394:
    a4 = ~(a4);
    local_r15 = (Arg2) - (v_stack_p30);
    v_stack_p44 = (uint32_t)(v_stack_p38);
    local_r15 = (local_r15) >> (3);
    local_r15 = (local_r15) << (6);
    local_r15 = (local_r15) + (v_stack_p38);
loc_003193B5:
    if (local_r15 > v_stack_p48) goto loc_003194C7;
loc_003193C0:
    if (local_r15 == -1) goto loc_00319376;
loc_003193C6:
    goto loc_00319223;
loc_003193D0:
    goto loc_0031935B;
loc_003193D5:
    if (*(uint64_t *)(local_rsi + 0x20) + Arg1 * 8 == 0) goto loc_003193E7;
    if ((*(uint64_t *)(local_rsi + 0x20) + Arg1 * 8) != (*(uint64_t *)(local_rsi + 0x48))) goto loc_003191A3;
loc_003193E7:
    result = MiMakeSystemPtesAppear(local_rsi, local_rdi, v_stack_p40, *(uint64_t *)(Arg2));
    if ((uint32_t)(result) != 0) goto loc_003191A3;
    result = MiExpandPtes(local_rsi, local_rdi, v_stack_p40, *(uint64_t *)(Arg2));
    v_stack_p38 = result;
    if (result != 0) goto loc_00319819;
    if (v_stack_p40 == 6) goto loc_00319162;
    v_stack_p40 = 6;
    result = MiEmptyPteBins(local_rsi, local_rdi, result + 1, *(uint64_t *)(Arg2));
    goto loc_003191A3;
loc_0031943F:
    local_r15 = 0;
    local_r10 = (local_r10) >> (6);
    v_stack_m128 = v_stack_p30 + local_r10 * 8;
loc_00319453:
    if ((*(uint64_t *)(Arg2)) == -1) goto loc_003195AA;
loc_0031945D:
    v_stack_p64 = 0;
    result = v_stack_p30 + local_r10 * 8;
    if ((*(uint64_t *)(Arg2)) == -1) { result = (uint32_t)(v_stack_p78); }
    v_stack_p64 = (uint32_t)(result);
    if ((local_r15 + result * 1) >= local_r14) goto loc_003195A2;
    local_r10 = ~(*(uint64_t *)(Arg2));
loc_00319487:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r14))))) >> (1));
    result = (local_r10) >> ((uint8_t)(Arg1));
    local_r10 = (local_r10) & (result);
    if (condition_is_equal) goto loc_003196E2;
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - ((uint32_t)(Arg1)));
    if (((uint32_t)(local_r15)) > 1) goto loc_00319487;
    v_stack_p44 = (uint32_t)(result);
loc_003194AF:
    Arg2 = (local_rdi) - (v_stack_p30);
    Arg2 = (Arg2) >> (3);
    Arg2 = (Arg2) << (6);
    local_r15 = ((uint32_t)((uint32_t)(result))) + (Arg2);
    goto loc_003193B5;
loc_003194C7:
    goto loc_00319376;
loc_003194D3:
    local_r12 = 0;
    goto loc_003191FB;
loc_003194DB:
    if ((uint8_t)(result) != 0) goto loc_0031918F;
    result = qsort(v_stack_mF0, (uint32_t)((uint32_t)(*(uint64_t *)(Arg2))), 8, v_rip + 3654559);
    result = MiCompressTbFlushList(v_stack_m118, (uint32_t)((uint32_t)(*(uint64_t *)(Arg2))), 8, v_rip + 3654559);
    goto loc_00318F76;
loc_00319514:
loc_00319519:
    if (!sign_flag) goto loc_00319733;
    Arg2 = ((uint32_t)((uint32_t)(*(uint64_t *)(Arg2)))) + (8);
    if (Arg2 > v_stack_p38) goto loc_0031936A;
    goto loc_00319519;
loc_00319534:
    Arg1 = (uint32_t)((result) & (0x3FFULL));
    if ((-1 + Arg1 * 1) > 0x3FFULL) goto loc_00319015;
    if ((-1 + Arg1 * 1) <= Arg1) goto loc_00319015;
    result = (result) - (8);
    result = (result) ^ (result + -1 * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (result + -1 * 1);
    *(uint64_t *)(v_stack_p38) = result;
    goto loc_0031918F;
loc_00319576:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsi + 0x28)))) & (4)) == 0) goto loc_00319097;
    result = MiCheckPteReserve(local_rsi, 1, local_rdi, *(uint64_t *)(Arg2));
    goto loc_00319097;
loc_00319595:
    goto loc_00318E92;
loc_003195A2:
    local_r15 = -(-1);
    goto loc_003194AF;
loc_003195AA:
loc_003195B0:
    Arg2 = (1) + (8);
    if (Arg2 > v_stack_p38) goto loc_0031936A;
    if ((*(uint64_t *)(Arg2)) == -1) goto loc_003195B0;
    local_r15 = 0;
    goto loc_0031945D;
loc_003195CE:
    local_r10 = v_stack_p38 + 8;
    if (((v_stack_p48) & (63)) == 0) { local_r10 = v_stack_p38; }
    if (*(uint64_t *)(Arg2) == 0) goto loc_003196C6;
    Arg2 = (Arg2) + (8);
    if ((*(uint64_t *)(Arg2)) != 0) goto loc_0031964E;
    v_stack_p50 = 0;
    if ((*(uint64_t *)(Arg2)) == 0) goto loc_003197DE;
    Arg1 = (uint32_t)((63) - ((uint32_t)(v_stack_p38)));
loc_0031960C:
    v_stack_p50 = (uint32_t)(Arg1);
loc_00319610:
    local_r15 = (Arg2) - (v_stack_p30);
    local_r15 = (local_r15) >> (3);
    local_r15 = (local_r15) << (6);
    local_r15 = (local_r15) - ((uint32_t)((uint32_t)(Arg1)));
    if (local_r15 > v_stack_p48) goto loc_0031936A;
    result = (local_r14) - ((uint32_t)((uint32_t)(Arg1)));
    result = (result) >> (6);
loc_0031963F:
    Arg2 = (Arg2) + (8);
    if (Arg2 == (Arg2 + result * 8)) goto loc_0031968D;
    if ((*(uint64_t *)(Arg2)) == 0) goto loc_0031963F;
loc_0031964E:
    if (Arg2 > local_r10) goto loc_00319804;
    Arg2 = (Arg2) + (8);
    if ((*(uint64_t *)(Arg2)) != 0) goto loc_0031964E;
    v_stack_p54 = 0;
    if ((*(uint64_t *)(Arg2)) == 0) goto loc_003197E6;
    Arg1 = (uint32_t)((63) - ((uint32_t)(Arg2 + result * 8)));
    v_stack_p54 = (uint32_t)(Arg1);
    goto loc_00319610;
loc_0031968D:
    a4 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - ((uint32_t)(Arg1)));
    a4 = (uint32_t)((a4) & (63));
    if (condition_is_equal) goto loc_003196BC;
    v_stack_p58 = 0;
    if (condition_is_equal) { Arg1 = 64; }
    v_stack_p58 = (uint32_t)(Arg1);
    if (((uint32_t)(Arg1)) < ((uint32_t)(a4))) goto loc_0031964E;
loc_003196BC:
    goto loc_003193C0;
loc_003196C6:
    Arg1 = 0;
    goto loc_00319610;
loc_003196CD:
    if (local_rsi == (v_rip + 11650988)) goto loc_00319162;
    goto loc_003191A0;
loc_003196E2:
    if (Arg2 == v_stack_m128) goto loc_0031936A;
    v_stack_p68 = 0;
    if (Arg2 == v_stack_m128) goto loc_00319715;
    local_r15 = (uint32_t)((63) - ((uint32_t)(v_rip + 11650988)));
    Arg2 = (Arg2) + (8);
    v_stack_p68 = (uint32_t)(local_r15);
    goto loc_00319453;
loc_00319715:
    Arg2 = (Arg2) + (8);
    v_stack_p68 = 64;
    goto loc_00319453;
loc_00319733:
    v_stack_p5C = 0;
    if (condition_is_equal) goto loc_003197F7;
    result = (uint32_t)((63) - (0));
loc_0031974C:
    local_r15 = (Arg2) - (v_stack_p30);
    local_r15 = (local_r15) >> (3);
    local_r15 = (local_r15) + 1;
    v_stack_p5C = (uint32_t)(result);
    local_r15 = (local_r15) << (6);
    local_r15 = (local_r15) - ((uint32_t)((uint32_t)(result)));
    if (local_r15 <= v_stack_p48) goto loc_0031977F;
loc_00319773:
    goto loc_00319376;
loc_0031977F:
    Arg1 = (local_r14) - ((uint32_t)((uint32_t)(result)));
    if (condition_is_equal) goto loc_003196BC;
    Arg2 = (Arg2) + (8);
    if (Arg1 < 64) goto loc_003197B7;
    if (*(uint64_t *)(Arg2 + 0x8) != 0) goto loc_00319519;
    Arg1 = (Arg1) - (64);
    if (condition_is_equal) goto loc_003196BC;
    Arg2 = (Arg2) + (8);
loc_003197B7:
    v_stack_p60 = 0;
    result = *(uint64_t *)(Arg2 + 0x8);
    if (condition_is_equal) { result = 64; }
    v_stack_p60 = (uint32_t)(result);
    if (result < Arg1) goto loc_00319519;
    goto loc_003193C0;
loc_003197DE:
    goto loc_0031960C;
loc_003197E6:
    v_stack_p54 = 64;
    goto loc_00319610;
loc_003197F7:
    goto loc_0031974C;
loc_00319804:
    goto loc_00319376;
loc_00319819:
    goto loc_00318DA0;
loc_00319821:
    result = MiCheckPteReserve(local_rsi, 64, local_rdi, *(uint64_t *)(Arg2 + 0x8));
    goto loc_00318DAB;
loc_00319834:
    v_stack_mFF = 1;
    goto loc_0031918F;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00318D20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
