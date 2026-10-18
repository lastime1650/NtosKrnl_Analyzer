# MiReleasePtes

- RVA: `0x00247240`–`0x00247969` (길이 `1,833` bytes)
- VA: `0x0000000140247240`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000623A8`
- 디코드: `458`개 명령, `1,833/1,833` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **48**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00247289` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0024733E` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002473C1` → [MiInsertCachedPte](MiInsertCachedPte_function_00247970.md) (function, `0x00247970`)
- `0x002473D1` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00247436` → [MiInitializeTbFlushStamps](../44/MiInitializeTbFlushStamps_function_004499EC.md) (function, `0x004499EC`)
- `0x002474A2` → [MiVaToFlushVm](../31/MiVaToFlushVm_function_0031AD84.md) (function, `0x0031AD84`)
- `0x002476D9` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x00247742` → [MiAttemptCoalesce](../47/MiAttemptCoalesce_function_00479EB0.md) (function, `0x00479EB0`)
- `0x0024782B` → [qsort](../50/qsort_function_005009F0.md) (function, `0x005009F0`)
- `0x00247835` → [MiCompressTbFlushList](../2A/MiCompressTbFlushList_function_002A93A8.md) (function, `0x002A93A8`)
- `0x002478FD` → [MiReturnSystemPtes](../23/MiReturnSystemPtes_function_002385C0.md) (function, `0x002385C0`)
- `0x00247937` → [MiCheckPteRelease](../69/MiCheckPteRelease_function_006948C4.md) (function, `0x006948C4`)

### Direct callers
- [sub_00246F4D](Unknown_function_00246F4D.md) at `0x00247110`
- [MiRemoveFromSystemSpace](../29/MiRemoveFromSystemSpace_function_002962FC.md) at `0x00296543`
- [MmFreeIndependentPages](../2A/MmFreeIndependentPages_function_002A2510.md) at `0x002A26DC`
- [MiReturnPteMappingSet](../2B/MiReturnPteMappingSet_function_002B2600.md) at `0x002B2659`
- [MiMakePageAvoidRead](../2B/MiMakePageAvoidRead_function_002B7DE0.md) at `0x002B810A`
- [MiDeleteCachedKernelStack](../2D/MiDeleteCachedKernelStack_function_002D986C.md) at `0x002D98FA`
- [MmMapLockedPagesSpecifyCache](../31/MmMapLockedPagesSpecifyCache_function_00318800.md) at `0x00318B77`
- [MiMapContiguousMemory](../32/MiMapContiguousMemory_function_0032787C.md) at `0x00327A18`
- [sub_0033827F](../33/Unknown_function_0033827F.md) at `0x0033866F`
- [MmDeleteKernelStack](../33/MmDeleteKernelStack_function_0033A960.md) at `0x0033AD93`
- [MmCopyToCachedPage](../34/MmCopyToCachedPage_function_00347B44.md) at `0x0034804D`
- [MiPrivateFixup](../36/MiPrivateFixup_function_003693E8.md) at `0x0036974D`
- [MiUnmapContiguousMemory](../3F/MiUnmapContiguousMemory_function_003F7908.md) at `0x003F79DE`
- [MiBuildReservationCluster](../40/MiBuildReservationCluster_function_004071A0.md) at `0x00407648`
- [MiUpdateImagePfnImportRelocations](../44/MiUpdateImagePfnImportRelocations_function_00449E84.md) at `0x00449FB7`
- [MiDeleteProcessShadow](../46/MiDeleteProcessShadow_function_00465BF8.md) at `0x00465D33`
- [MiDeleteCachedKernelShadowStack](../49/MiDeleteCachedKernelShadowStack_function_004956CC.md) at `0x00495719`
- [MiReleasePteCopyList](../4B/MiReleasePteCopyList_function_004B0D14.md) at `0x004B0D2C`
- [MiUnmapSinglePage](../4D/MiUnmapSinglePage_function_004D4B00.md) at `0x004D4B2F`
- [MmMapMdl](../67/MmMapMdl_function_0067CBA0.md) at `0x0067CDAC`
- [MiChangePagingFileMaximum](../67/MiChangePagingFileMaximum_function_0067FEFC.md) at `0x006802B1`
- [MiPrepareEnclaveMetadataPage](../68/MiPrepareEnclaveMetadataPage_function_00686EAC.md) at `0x0068705F`
- [MiCopyMemoryPagefileData](../69/MiCopyMemoryPagefileData_function_00694C04.md) at `0x00694D64`
- [MiReleasePageHash](../69/MiReleasePageHash_function_00697B20.md) at `0x00697B6E`
- [MiFreeZeroCalibrationBuffer](../69/MiFreeZeroCalibrationBuffer_function_00699E44.md) at `0x00699EA5`
- [sub_006E710A](../6E/Unknown_function_006E710A.md) at `0x006E7123`
- [MmDeleteProcessor](../../page/7F/MmDeleteProcessor_function_007F8FB4.md) at `0x007F8FE1`
- [MmReleaseDumpHibernateResources](../../page/7F/MmReleaseDumpHibernateResources_function_007FE418.md) at `0x007FE443`
- [MiUnlockEntireDriver](../../page/80/MiUnlockEntireDriver_function_00801780.md) at `0x008017C3`
- [MmFreeIsrStack](../../page/80/MmFreeIsrStack_function_00807FC0.md) at `0x00808004`
- [MiAllocateEnclaveVad](../../page/80/MiAllocateEnclaveVad_function_008080A4.md) at `0x00808285`
- [MiCreatePfnBitMaps](../../page/80/MiCreatePfnBitMaps_function_0080BBC8.md) at `0x0080BCC6`
- [MiDeleteSparseRange](../../page/80/MiDeleteSparseRange_function_0080C1D0.md) at `0x0080C213`
- [MiExpandPartitionIds](../../page/80/MiExpandPartitionIds_function_0080D258.md) at `0x0080D374`
- [MiValidateImagePfn](../../page/93/MiValidateImagePfn_function_0093EA08.md) at `0x0093EBE2`
- [MiRelocateImagePfn](../../page/93/MiRelocateImagePfn_function_0093F2A8.md) at `0x0093F50E`
- [MiRelocateImageAgain](../../page/98/MiRelocateImageAgain_function_009885C8.md) at `0x00988762`
- [MmFreeMappingAddress](../../page/A7/MmFreeMappingAddress_function_00A75F20.md) at `0x00A75FA5`
- [MiApplyImportOptimizationToRuntimeDriver](../../page/A9/MiApplyImportOptimizationToRuntimeDriver_function_00A9F93C.md) at `0x00A9FAEE`
- [MmAllocateIndependentPagesEx](../../page/AA/MmAllocateIndependentPagesEx_function_00AA0CFC.md) at `0x00AA0D74`
- [MmFreeNonCachedMemory](../../page/AB/MmFreeNonCachedMemory_function_00AB4640.md) at `0x00AB46AB`
- [MiReleaseHotPatchResources](../../page/AC/MiReleaseHotPatchResources_function_00ACCD60.md) at `0x00ACCDA4`
- [MiReleaseEnclaveMetadataPage](../../pagelk/B7/MiReleaseEnclaveMetadataPage_function_00B74EE4.md) at `0x00B74F1D`
- [MiDeleteEnclavePages](../../pagelk/B7/MiDeleteEnclavePages_function_00B7E228.md) at `0x00B7E2E6`
- [MmInitializeImageViewExtensionCfg](../../init/C6/MmInitializeImageViewExtensionCfg_function_00C64FC4.md) at `0x00C65265`
- [MiCreateRetpolineBitmap](../../init/C6/MiCreateRetpolineBitmap_function_00C66418.md) at `0x00C66495`
- [MiInitializePteInfo](../../init/C6/MiInitializePteInfo_function_00C6A7E0.md) at `0x00C6A8E3`
- [MiInitializeTbFlush](../../init/C6/MiInitializeTbFlush_function_00C6B01C.md) at `0x00C6B172`

### Static image references
- `0x0024725C` → RVA `0x00E0A740` (`.data`; read)
- `0x0024739F` → RVA `0x00010880` (`.rdata`; read)
- `0x00247449` → RVA `0x00E2DC80` (`.data`; read)
- `0x002477C5` → RVA `0x00E37668` (`.data`; read)
- `0x002477D1` → RVA `0x00E35E80` (`.data`; read)
- `0x0024781E` → RVA `0x00695890` (`MiTbFlushSort`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00247240  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00247245  55                              push rbp
00247246  56                              push rsi
00247247  57                              push rdi
00247248  41 54                           push r12
0024724A  41 55                           push r13
0024724C  41 56                           push r14
0024724E  41 57                           push r15
00247250  48 8D 6C 24 C0                  lea rbp, [rsp - 0x40]
00247255  48 81 EC 40 01 00 00            sub rsp, 0x140
0024725C  48 8B 05 DD 34 BC 00            mov rax, qword ptr [rip + 0xbc34dd]
00247263  48 33 C4                        xor rax, rsp
00247266  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
0024726A  45 8B E0                        mov r12d, r8d
0024726D  48 8B FA                        mov rdi, rdx
00247270  4C 8B F1                        mov r14, rcx
00247273  48 C7 44 24 48 00 00 00 00      mov qword ptr [rsp + 0x48], 0
0024727C  33 D2                           xor edx, edx
0024727E  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00247283  41 B8 C8 00 00 00               mov r8d, 0xc8
00247289  E8 B2 F9 47 00                  call 0x1406c6c40
0024728E  41 8B 46 28                     mov eax, dword ptr [r14 + 0x28]
00247292  45 8B FC                        mov r15d, r12d
00247295  A8 04                           test al, 4
00247297  0F 85 91 06 00 00               jne 0x14024792e
0024729D  41 8B 46 28                     mov eax, dword ptr [r14 + 0x28]
002472A1  48 8B DF                        mov rbx, rdi
002472A4  49 2B 5E 20                     sub rbx, qword ptr [r14 + 0x20]
002472A8  48 C1 FB 03                     sar rbx, 3
002472AC  83 E0 01                        and eax, 1
002472AF  74 04                           je 0x1402472b5
002472B1  48 C1 EB 04                     shr rbx, 4
002472B5  49 8B F7                        mov rsi, r15
002472B8  41 BD 01 00 00 00               mov r13d, 1
002472BE  48 C1 EE 04                     shr rsi, 4
002472C2  85 C0                           test eax, eax
002472C4  49 0F 44 F7                     cmove rsi, r15
002472C8  41 81 FC 00 02 00 00            cmp r12d, 0x200
002472CF  0F 83 F0 04 00 00               jae 0x1402477c5
002472D5  49 8B 06                        mov rax, qword ptr [r14]
002472D8  C7 44 24 30 00 00 00 00         mov dword ptr [rsp + 0x30], 0
002472E0  48 3B D8                        cmp rbx, rax
002472E3  73 28                           jae 0x14024730d
002472E5  49 3B F5                        cmp rsi, r13
002472E8  77 5A                           ja 0x140247344
002472EA  75 21                           jne 0x14024730d
002472EC  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
002472F0  48 8B D3                        mov rdx, rbx
002472F3  83 E2 3F                        and edx, 0x3f
002472F6  48 8B CB                        mov rcx, rbx
002472F9  48 C1 E9 06                     shr rcx, 6
002472FD  48 0F A3 14 C8                  bt qword ptr [rax + rcx*8], rdx
00247302  0F 92 C0                        setb al
00247305  84 C0                           test al, al
00247307  0F 85 8D 00 00 00               jne 0x14024739a
0024730D  48 C1 E7 19                     shl rdi, 0x19
00247311  49 BC 00 00 00 00 80 F6 FF FF   movabs r12, 0xfffff68000000000
0024731B  49 8B C4                        mov rax, r12
0024731E  48 C1 E0 19                     shl rax, 0x19
00247322  4D 8B CF                        mov r9, r15
00247325  48 2B F8                        sub rdi, rax
00247328  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0024732D  48 C1 FF 10                     sar rdi, 0x10
00247331  BA 02 03 00 00                  mov edx, 0x302
00247336  4C 8B C7                        mov r8, rdi
00247339  B9 DA 00 00 00                  mov ecx, 0xda
0024733E  E8 1D 63 2B 00                  call 0x1404fd660
00247343  CC                              int3
00247344  48 2B C3                        sub rax, rbx
00247347  48 3B C6                        cmp rax, rsi
0024734A  72 C1                           jb 0x14024730d
0024734C  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
00247350  4C 8D 4E FF                     lea r9, [rsi - 1]
00247354  4C 03 CB                        add r9, rbx
00247357  48 8B C3                        mov rax, rbx
0024735A  48 C1 E8 06                     shr rax, 6
0024735E  4C 8B 14 C1                     mov r10, qword ptr [rcx + rax*8]
00247362  48 8D 14 C1                     lea rdx, [rcx + rax*8]
00247366  49 8B C1                        mov rax, r9
00247369  48 C1 E8 06                     shr rax, 6
0024736D  4C 8D 04 C1                     lea r8, [rcx + rax*8]
00247371  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
00247378  49 3B D0                        cmp rdx, r8
0024737B  75 75                           jne 0x1402473f2
0024737D  B9 40 00 00 00                  mov ecx, 0x40
00247382  40 2A CE                        sub cl, sil
00247385  48 D3 E8                        shr rax, cl
00247388  48 8B CB                        mov rcx, rbx
0024738B  48 D3 E0                        shl rax, cl
0024738E  4C 23 D0                        and r10, rax
00247391  4C 3B D0                        cmp r10, rax
00247394  0F 85 73 FF FF FF               jne 0x14024730d
0024739A  45 85 E4                        test r12d, r12d
0024739D  74 19                           je 0x1402473b8
0024739F  48 8B 05 DA 94 DC FF            mov rax, qword ptr [rip - 0x236b26]
002473A6  48 8B CF                        mov rcx, rdi
002473A9  49 8B D7                        mov rdx, r15
002473AC  48 89 01                        mov qword ptr [rcx], rax
002473AF  48 8D 49 08                     lea rcx, [rcx + 8]
002473B3  49 2B D5                        sub rdx, r13
002473B6  75 F4                           jne 0x1402473ac
002473B8  45 8B C4                        mov r8d, r12d
002473BB  48 8B D7                        mov rdx, rdi
002473BE  49 8B CE                        mov rcx, r14
002473C1  E8 AA 05 00 00                  call 0x140247970
002473C6  85 C0                           test eax, eax
002473C8  74 51                           je 0x14024741b
002473CA  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
002473CE  48 33 CC                        xor rcx, rsp
002473D1  E8 6A 52 46 00                  call 0x1406ac640
002473D6  48 8B 9C 24 98 01 00 00         mov rbx, qword ptr [rsp + 0x198]
002473DE  48 81 C4 40 01 00 00            add rsp, 0x140
002473E5  41 5F                           pop r15
002473E7  41 5E                           pop r14
002473E9  41 5D                           pop r13
002473EB  41 5C                           pop r12
002473ED  5F                              pop rdi
002473EE  5E                              pop rsi
002473EF  5D                              pop rbp
002473F0  C3                              ret
002473F1  CC                              int3
002473F2  48 8B CB                        mov rcx, rbx
002473F5  48 D3 E0                        shl rax, cl
002473F8  4C 23 D0                        and r10, rax
002473FB  4C 3B D0                        cmp r10, rax
002473FE  0F 85 09 FF FF FF               jne 0x14024730d
00247404  4C 8B 52 08                     mov r10, qword ptr [rdx + 8]
00247408  48 83 C2 08                     add rdx, 8
0024740C  49 3B D0                        cmp rdx, r8
0024740F  0F 84 8A 02 00 00               je 0x14024769f
00247415  49 83 FA FF                     cmp r10, -1
00247419  EB E3                           jmp 0x1402473fe
0024741B  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
0024741F  41 3B C5                        cmp eax, r13d
00247422  0F 84 BE 04 00 00               je 0x1402478e6
00247428  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
0024742D  48 C7 44 24 48 00 00 00 00      mov qword ptr [rsp + 0x48], 0
00247436  E8 B1 25 20 00                  call 0x1404499ec
0024743B  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00247440  45 85 E4                        test r12d, r12d
00247443  0F 85 AE 03 00 00               jne 0x1402477f7
00247449  48 8B 15 30 68 BE 00            mov rdx, qword ptr [rip + 0xbe6830]
00247450  49 8B CF                        mov rcx, r15
00247453  48 F7 D9                        neg rcx
00247456  48 8D 3C CF                     lea rdi, [rdi + rcx*8]
0024745A  48 8B C8                        mov rcx, rax
0024745D  48 85 D2                        test rdx, rdx
00247460  74 0E                           je 0x140247470
00247462  F6 C1 10                        test cl, 0x10
00247465  75 09                           jne 0x140247470
00247467  48 8B C2                        mov rax, rdx
0024746A  48 F7 D0                        not rax
0024746D  48 23 C1                        and rax, rcx
00247470  48 B9 00 00 00 00 FF FF FF FF   movabs rcx, 0xffffffff00000000
0024747A  48 85 C1                        test rcx, rax
0024747D  0F 85 5B 02 00 00               jne 0x1402476de
00247483  48 C1 E7 19                     shl rdi, 0x19
00247487  49 BC 00 00 00 00 80 F6 FF FF   movabs r12, 0xfffff68000000000
00247491  49 8B C4                        mov rax, r12
00247494  48 C1 E0 19                     shl rax, 0x19
00247498  48 2B F8                        sub rdi, rax
0024749B  48 C1 FF 10                     sar rdi, 0x10
0024749F  48 8B CF                        mov rcx, rdi
002474A2  E8 DD 38 0D 00                  call 0x14031ad84
002474A7  C7 44 24 6C 14 00 00 00         mov dword ptr [rsp + 0x6c], 0x14
002474AF  48 8B D0                        mov rdx, rax
002474B2  C7 44 24 70 08 00 00 00         mov dword ptr [rsp + 0x70], 8
002474BA  44 89 6C 24 74                  mov dword ptr [rsp + 0x74], r13d
002474BF  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
002474C4  8B 88 B8 00 00 00               mov ecx, dword ptr [rax + 0xb8]
002474CA  C1 E9 08                        shr ecx, 8
002474CD  C0 E9 03                        shr cl, 3
002474D0  41 22 CD                        and cl, r13b
002474D3  88 4C 24 78                     mov byte ptr [rsp + 0x78], cl
002474D7  8B 88 B8 00 00 00               mov ecx, dword ptr [rax + 0xb8]
002474DD  F6 C1 0F                        test cl, 0xf
002474E0  75 20                           jne 0x140247502
002474E2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002474EB  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
002474F2  48 81 C1 00 04 00 00            add rcx, 0x400
002474F9  48 3B D1                        cmp rdx, rcx
002474FC  0F 85 58 03 00 00               jne 0x14024785a
00247502  8B 82 B8 00 00 00               mov eax, dword ptr [rdx + 0xb8]
00247508  44 8B 44 24 70                  mov r8d, dword ptr [rsp + 0x70]
0024750D  A8 0F                           test al, 0xf
0024750F  0F 85 4B 03 00 00               jne 0x140247860
00247515  45 33 C9                        xor r9d, r9d
00247518  44 89 6C 24 68                  mov dword ptr [rsp + 0x68], r13d
0024751D  45 33 DB                        xor r11d, r11d
00247520  44 89 4C 24 7C                  mov dword ptr [rsp + 0x7c], r9d
00247525  49 8B D7                        mov rdx, r15
00247528  4C 89 5D 80                     mov qword ptr [rbp - 0x80], r11
0024752C  41 83 E0 DB                     and r8d, 0xffffffdb
00247530  4C 89 4D 88                     mov qword ptr [rbp - 0x78], r9
00247534  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
00247539  4C 8B D7                        mov r10, rdi
0024753C  66 C7 44 24 79 00 00            mov word ptr [rsp + 0x79], 0
00247543  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
00247548  44 89 44 24 70                  mov dword ptr [rsp + 0x70], r8d
0024754D  45 33 E4                        xor r12d, r12d
00247550  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00247555  45 85 C9                        test r9d, r9d
00247558  0F 84 AA 00 00 00               je 0x140247608
0024755E  41 F6 C0 02                     test r8b, 2
00247562  75 64                           jne 0x1402475c8
00247564  41 8D 41 FF                     lea eax, [r9 - 1]
00247568  48 8D 7D 88                     lea rdi, [rbp - 0x78]
0024756C  48 8D 3C C7                     lea rdi, [rdi + rax*8]
00247570  48 8B 07                        mov rax, qword ptr [rdi]
00247573  48 A9 00 0C 00 00               test rax, 0xc00
00247579  75 4D                           jne 0x1402475c8
0024757B  4C 8B D0                        mov r10, rax
0024757E  48 8B C8                        mov rcx, rax
00247581  41 81 E2 FF 03 00 00            and r10d, 0x3ff
00247588  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
0024758F  49 8D 52 01                     lea rdx, [r10 + 1]
00247593  48 C1 E2 0C                     shl rdx, 0xc
00247597  48 03 D1                        add rdx, rcx
0024759A  48 3B 54 24 40                  cmp rdx, qword ptr [rsp + 0x40]
0024759F  0F 85 C9 01 00 00               jne 0x14024776e
002475A5  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
002475AA  49 8D 14 0A                     lea rdx, [r10 + rcx]
002475AE  49 3B D2                        cmp rdx, r10
002475B1  76 0D                           jbe 0x1402475c0
002475B3  48 81 FA FF 03 00 00            cmp rdx, 0x3ff
002475BA  0F 86 81 03 00 00               jbe 0x140247941
002475C0  48 8B D1                        mov rdx, rcx
002475C3  4C 8B 54 24 40                  mov r10, qword ptr [rsp + 0x40]
002475C8  45 85 C9                        test r9d, r9d
002475CB  74 3B                           je 0x140247608
002475CD  41 F6 C0 02                     test r8b, 2
002475D1  75 35                           jne 0x140247608
002475D3  41 8D 41 FF                     lea eax, [r9 - 1]
002475D7  48 8D 7D 88                     lea rdi, [rbp - 0x78]
002475DB  48 8D 3C C7                     lea rdi, [rdi + rax*8]
002475DF  48 8B 07                        mov rax, qword ptr [rdi]
002475E2  48 A9 00 0C 00 00               test rax, 0xc00
002475E8  75 1E                           jne 0x140247608
002475EA  4C 8B C2                        mov r8, rdx
002475ED  48 8B C8                        mov rcx, rax
002475F0  49 C1 E0 0C                     shl r8, 0xc
002475F4  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
002475FB  4B 8D 14 10                     lea rdx, [r8 + r10]
002475FF  48 3B CA                        cmp rcx, rdx
00247602  0F 84 B9 02 00 00               je 0x1402478c1
00247608  44 3B 4C 24 6C                  cmp r9d, dword ptr [rsp + 0x6c]
0024760D  0F 84 AD 00 00 00               je 0x1402476c0
00247613  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00247618  48 85 C9                        test rcx, rcx
0024761B  0F 84 B3 00 00 00               je 0x1402476d4
00247621  48 8D 41 FF                     lea rax, [rcx - 1]
00247625  BA 00 04 00 00                  mov edx, 0x400
0024762A  48 3D FF 03 00 00               cmp rax, 0x3ff
00247630  48 0F 46 D1                     cmovbe rdx, rcx
00247634  48 2B CA                        sub rcx, rdx
00247637  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0024763C  49 8B CA                        mov rcx, r10
0024763F  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
00247646  48 8D 42 FF                     lea rax, [rdx - 1]
0024764A  25 FF 03 00 00                  and eax, 0x3ff
0024764F  48 0B C1                        or rax, rcx
00247652  48 8B CA                        mov rcx, rdx
00247655  48 C1 E1 0C                     shl rcx, 0xc
00247659  4C 03 D1                        add r10, rcx
0024765C  41 8B C9                        mov ecx, r9d
0024765F  4C 89 54 24 40                  mov qword ptr [rsp + 0x40], r10
00247664  48 89 44 CD 88                  mov qword ptr [rbp + rcx*8 - 0x78], rax
00247669  44 8B 4C 24 7C                  mov r9d, dword ptr [rsp + 0x7c]
0024766E  4C 8B 5D 80                     mov r11, qword ptr [rbp - 0x80]
00247672  41 FF C1                        inc r9d
00247675  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0024767A  4C 03 DA                        add r11, rdx
0024767D  44 89 4C 24 7C                  mov dword ptr [rsp + 0x7c], r9d
00247682  4C 89 5D 80                     mov qword ptr [rbp - 0x80], r11
00247686  48 85 C9                        test rcx, rcx
00247689  74 49                           je 0x1402476d4
0024768B  44 3B 4C 24 6C                  cmp r9d, dword ptr [rsp + 0x6c]
00247690  75 86                           jne 0x140247618
00247692  44 8B 44 24 70                  mov r8d, dword ptr [rsp + 0x70]
00247697  48 8B D1                        mov rdx, rcx
0024769A  E9 AE FE FF FF                  jmp 0x14024754d
0024769F  41 0F B6 C9                     movzx ecx, r9b
002476A3  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
002476AA  F6 D1                           not cl
002476AC  48 D3 E8                        shr rax, cl
002476AF  4C 23 D0                        and r10, rax
002476B2  4C 3B D0                        cmp r10, rax
002476B5  0F 85 52 FC FF FF               jne 0x14024730d
002476BB  E9 DA FC FF FF                  jmp 0x14024739a
002476C0  45 85 E4                        test r12d, r12d
002476C3  0F 84 43 01 00 00               je 0x14024780c
002476C9  80 7C 24 79 00                  cmp byte ptr [rsp + 0x79], 0
002476CE  0F 84 8B 02 00 00               je 0x14024795f
002476D4  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
002476D9  E8 E2 A8 0C 00                  call 0x140311fc0
002476DE  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
002476E2  4C 8B C3                        mov r8, rbx
002476E5  41 83 E0 1F                     and r8d, 0x1f
002476E9  48 8B CB                        mov rcx, rbx
002476EC  48 C1 E9 05                     shr rcx, 5
002476F0  4C 8B CE                        mov r9, rsi
002476F3  4C 8D 14 88                     lea r10, [rax + rcx*4]
002476F7  49 8D 04 30                     lea rax, [r8 + rsi]
002476FB  48 83 F8 20                     cmp rax, 0x20
002476FF  77 4B                           ja 0x14024774c
00247701  48 83 FE 20                     cmp rsi, 0x20
00247705  0F 84 E0 00 00 00               je 0x1402477eb
0024770B  48 8B CE                        mov rcx, rsi
0024770E  41 D3 E5                        shl r13d, cl
00247711  41 8B C8                        mov ecx, r8d
00247714  41 FF CD                        dec r13d
00247717  41 D3 E5                        shl r13d, cl
0024771A  41 F7 D5                        not r13d
0024771D  F0 45 21 2A                     lock and dword ptr [r10], r13d
00247721  49 8B C7                        mov rax, r15
00247724  F0 49 0F C1 46 58               lock xadd qword ptr [r14 + 0x58], rax
0024772A  49 03 C7                        add rax, r15
0024772D  48 3D 00 00 20 00               cmp rax, 0x200000
00247733  0F 86 91 FC FF FF               jbe 0x1402473ca
00247739  4C 8B C6                        mov r8, rsi
0024773C  48 8B D3                        mov rdx, rbx
0024773F  49 8B CE                        mov rcx, r14
00247742  E8 69 27 23 00                  call 0x140479eb0
00247747  E9 7E FC FF FF                  jmp 0x1402473ca
0024774C  4D 85 C0                        test r8, r8
0024774F  75 48                           jne 0x140247799
00247751  49 83 F9 20                     cmp r9, 0x20
00247755  73 21                           jae 0x140247778
00247757  4D 85 C9                        test r9, r9
0024775A  74 C5                           je 0x140247721
0024775C  49 8B C9                        mov rcx, r9
0024775F  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
00247766  D3 E0                           shl eax, cl
00247768  F0 41 21 02                     lock and dword ptr [r10], eax
0024776C  EB B3                           jmp 0x140247721
0024776E  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
00247773  E9 4B FE FF FF                  jmp 0x1402475c3
00247778  49 8B C9                        mov rcx, r9
0024777B  48 C1 E9 05                     shr rcx, 5
0024777F  48 6B C1 E0                     imul rax, rcx, -0x20
00247783  4C 03 C8                        add r9, rax
00247786  41 C7 02 00 00 00 00            mov dword ptr [r10], 0
0024778D  49 83 C2 04                     add r10, 4
00247791  48 83 E9 01                     sub rcx, 1
00247795  74 C0                           je 0x140247757
00247797  EB ED                           jmp 0x140247786
00247799  8B C3                           mov eax, ebx
0024779B  BA 20 00 00 00                  mov edx, 0x20
002477A0  83 E0 1F                        and eax, 0x1f
002477A3  2B D0                           sub edx, eax
002477A5  8B CA                           mov ecx, edx
002477A7  41 D3 E5                        shl r13d, cl
002477AA  49 8B C8                        mov rcx, r8
002477AD  41 FF CD                        dec r13d
002477B0  41 D3 E5                        shl r13d, cl
002477B3  41 F7 D5                        not r13d
002477B6  F0 45 21 2A                     lock and dword ptr [r10], r13d
002477BA  8B C2                           mov eax, edx
002477BC  4C 2B C8                        sub r9, rax
002477BF  49 83 C2 04                     add r10, 4
002477C3  EB 8C                           jmp 0x140247751
002477C5  48 8D 05 9C FE BE 00            lea rax, [rip + 0xbefe9c]
002477CC  4C 3B F0                        cmp r14, rax
002477CF  74 10                           je 0x1402477e1
002477D1  48 8D 05 A8 E6 BE 00            lea rax, [rip + 0xbee6a8]
002477D8  4C 3B F0                        cmp r14, rax
002477DB  0F 85 F4 FA FF FF               jne 0x1402472d5
002477E1  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
002477E6  E9 B4 FB FF FF                  jmp 0x14024739f
002477EB  41 C7 02 00 00 00 00            mov dword ptr [r10], 0
002477F2  E9 2A FF FF FF                  jmp 0x140247721
002477F7  49 8B CF                        mov rcx, r15
002477FA  48 89 07                        mov qword ptr [rdi], rax
002477FD  48 83 C7 08                     add rdi, 8
00247801  49 2B CD                        sub rcx, r13
00247804  0F 84 3F FC FF FF               je 0x140247449
0024780A  EB EE                           jmp 0x1402477fa
0024780C  80 7C 24 79 00                  cmp byte ptr [rsp + 0x79], 0
00247811  0F 85 BD FE FF FF               jne 0x1402476d4
00247817  41 8B D1                        mov edx, r9d
0024781A  48 8D 4D 88                     lea rcx, [rbp - 0x78]
0024781E  4C 8D 0D 6B E0 44 00            lea r9, [rip + 0x44e06b]
00247825  41 B8 08 00 00 00               mov r8d, 8
0024782B  E8 C0 91 2B 00                  call 0x1405009f0
00247830  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00247835  E8 6E 1B 06 00                  call 0x1402a93a8
0024783A  4C 8B 5D 80                     mov r11, qword ptr [rbp - 0x80]
0024783E  45 8B E5                        mov r12d, r13d
00247841  44 8B 4C 24 7C                  mov r9d, dword ptr [rsp + 0x7c]
00247846  44 8B 44 24 70                  mov r8d, dword ptr [rsp + 0x70]
0024784B  4C 8B 54 24 40                  mov r10, qword ptr [rsp + 0x40]
00247850  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
00247855  E9 F6 FC FF FF                  jmp 0x140247550
0024785A  41 B8 09 00 00 00               mov r8d, 9
00247860  33 C0                           xor eax, eax
00247862  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
00247867  41 83 E0 DB                     and r8d, 0xffffffdb
0024786B  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0024786F  49 8B D7                        mov rdx, r15
00247872  44 89 44 24 70                  mov dword ptr [rsp + 0x70], r8d
00247877  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
0024787C  41 8B C8                        mov ecx, r8d
0024787F  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00247883  44 8B D8                        mov r11d, eax
00247886  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
0024788A  44 8B C8                        mov r9d, eax
0024788D  66 89 44 24 79                  mov word ptr [rsp + 0x79], ax
00247892  4C 8B D7                        mov r10, rdi
00247895  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
00247899  49 8B C4                        mov rax, r12
0024789C  48 3B F8                        cmp rdi, rax
0024789F  0F 82 A8 FC FF FF               jb 0x14024754d
002478A5  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
002478AF  48 3B F8                        cmp rdi, rax
002478B2  0F 87 95 FC FF FF               ja 0x14024754d
002478B8  41 83 C8 04                     or r8d, 4
002478BC  E9 87 FC FF FF                  jmp 0x140247548
002478C1  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
002478C6  48 8B C8                        mov rcx, rax
002478C9  81 E1 FF 03 00 00               and ecx, 0x3ff
002478CF  4C 8D 24 11                     lea r12, [rcx + rdx]
002478D3  49 81 FC FF 03 00 00            cmp r12, 0x3ff
002478DA  76 2B                           jbe 0x140247907
002478DC  44 8B 64 24 30                  mov r12d, dword ptr [rsp + 0x30]
002478E1  E9 22 FD FF FF                  jmp 0x140247608
002478E6  4D 8D 8C 24 FF 01 00 00         lea r9, [r12 + 0x1ff]
002478EE  4C 8B C3                        mov r8, rbx
002478F1  49 81 E1 00 FE FF FF            and r9, 0xfffffffffffffe00
002478F8  8B D0                           mov edx, eax
002478FA  49 8B CE                        mov rcx, r14
002478FD  E8 BE 0C FF FF                  call 0x1402385c0
00247902  E9 C3 FA FF FF                  jmp 0x1402473ca
00247907  4C 3B E1                        cmp r12, rcx
0024790A  76 D0                           jbe 0x1402478dc
0024790C  49 2B C0                        sub rax, r8
0024790F  4C 03 DA                        add r11, rdx
00247912  4C 89 5D 80                     mov qword ptr [rbp - 0x80], r11
00247916  48 8D 0C 10                     lea rcx, [rax + rdx]
0024791A  48 33 C1                        xor rax, rcx
0024791D  48 25 00 FC FF FF               and rax, 0xfffffffffffffc00
00247923  48 33 C1                        xor rax, rcx
00247926  48 89 07                        mov qword ptr [rdi], rax
00247929  E9 A6 FD FF FF                  jmp 0x1402476d4
0024792E  4D 8B C7                        mov r8, r15
00247931  48 8B D7                        mov rdx, rdi
00247934  49 8B CE                        mov rcx, r14
00247937  E8 88 CF 44 00                  call 0x1406948c4
0024793C  E9 5C F9 FF FF                  jmp 0x14024729d
00247941  4C 03 D9                        add r11, rcx
00247944  48 03 C8                        add rcx, rax
00247947  48 33 C1                        xor rax, rcx
0024794A  4C 89 5D 80                     mov qword ptr [rbp - 0x80], r11
0024794E  48 25 00 FC FF FF               and rax, 0xfffffffffffffc00
00247954  48 33 C1                        xor rax, rcx
00247957  48 89 07                        mov qword ptr [rdi], rax
0024795A  E9 75 FD FF FF                  jmp 0x1402476d4
0024795F  44 88 6C 24 79                  mov byte ptr [rsp + 0x79], r13b
00247964  E9 6B FD FF FF                  jmp 0x1402476d4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReleasePtes(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p60;
    unsigned int v_stack_p68;
    unsigned int v_stack_p6C;
    unsigned int v_stack_p70;
    unsigned int v_stack_p74;
    unsigned __int8 v_stack_p78;
    unsigned __int16 v_stack_p79;
    unsigned int v_stack_p7C;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (320);
    result = (*(unsigned __int64 *)(v_rip + 12334301)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m130 = 0;
    a2 = 0;
    result = memset(v_stack_m118, a2, 200, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 40)))) & (4)) != 0) goto loc_0024792E;
loc_0024729D:
    v_rbx = (0) - (*(unsigned __int64 *)(a1 + 32));
    v_rbx = (v_rbx) >> (3);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 40))) & (1));
    if (!(condition_is_equal)) {
        v_rbx = (v_rbx) >> (4);
    }
    v_rsi = ((unsigned int)((unsigned int)((unsigned int)(a3)))) >> (4);
    if ((unsigned int)(result) == 0) { v_rsi = (unsigned int)((unsigned int)((unsigned int)(a3))); }
    if (((unsigned int)((unsigned int)(a3))) >= 512) goto loc_002477C5;
loc_002472D5:
    v_stack_m148 = 0;
    if (v_rbx >= (*(unsigned __int64 *)(a1))) goto loc_0024730D;
    if (v_rsi > 1) goto loc_00247344;
    if (v_rsi != 1) goto loc_0024730D;
    a2 = (unsigned int)((v_rbx) & (63));
    a1 = (v_rbx) >> (6);
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) goto loc_0024739A;
loc_0024730D:
    v_rdi = (a2) << (25);
    result = ((unsigned int)(a3)) << (25);
    v_rdi = (v_rdi) - (result);
    v_stack_m158 = v_rbx;
    v_rdi = (v_rdi) >> (16);
    result = KeBugCheckEx(218, 770, v_rdi, (unsigned int)((unsigned int)((unsigned int)(a3))));
loc_00247344:
    result = (result) - (v_rbx);
    if (result < v_rsi) goto loc_0024730D;
    a4 = (v_rsi - 1) + (v_rbx);
    result = (v_rbx) >> (6);
    result = (a4) >> (6);
    if ((*(unsigned __int64 *)(a1 + 8) + result * 8) != (*(unsigned __int64 *)(a1 + 8) + result * 8)) goto loc_002473F2;
    a1 = (unsigned __int8)((64) - ((unsigned __int8)(v_rsi)));
    result = (-1) >> ((unsigned __int8)(a1));
    result = (result) << ((unsigned __int8)(v_rbx));
    v_r10 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + result * 8)) & (result);
    if (v_r10 != result) goto loc_0024730D;
loc_0024739A:
    if ((unsigned int)((unsigned int)(a3)) == 0) goto loc_002473B8;
loc_0024739F:
loc_002473AC:
    *(unsigned __int64 *)(v_rdi) = *(unsigned __int64 *)(v_rip - 2321190);
    a2 = ((unsigned int)((unsigned int)((unsigned int)(a3)))) - (1);
    if (condition_is_not_equal) goto loc_002473AC;
loc_002473B8:
    result = MiInsertCachedPte(a1, v_rdi, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned int)(result) == 0) goto loc_0024741B;
loc_002473CA:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rdi, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    v_rsp = (v_rsp) + (320);
    return result;
loc_002473F2:
    result = (result) << ((unsigned __int8)(v_stack_p20));
    v_r10 = (v_r10) & (result);
loc_002473FE:
    if (v_r10 != result) goto loc_0024730D;
    a2 = (v_rdi) + (8);
    if (a2 == ((unsigned int)((unsigned int)((unsigned int)(a3))))) goto loc_0024769F;
    goto loc_002473FE;
loc_0024741B:
    if (((unsigned int)((unsigned int)(v_stack_p30))) == 1) goto loc_002478E6;
    v_stack_p48 = 0;
    result = MiInitializeTbFlushStamps(v_stack_p48, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned int)((unsigned int)(a3)) != 0) goto loc_002477F7;
loc_00247449:
    a1 = -((unsigned int)((unsigned int)((unsigned int)(a3))));
    if (*(unsigned __int64 *)(v_rip + 12478512) == 0) goto loc_00247470;
    result = v_stack_p48;
    if ((((unsigned __int8)(v_stack_p48)) & (16)) == 0) {
        result = *(unsigned __int64 *)(v_rip + 12478512);
        result = ~(result);
        result = (result) & (v_stack_p48);
    }
    if (((v_stack_p48) & (result)) != 0) goto loc_002476DE;
    v_rdi = (v_rdi + a1 * 8) << (25);
    result = ((unsigned int)(a3)) << (25);
    v_rdi = (v_rdi) - (result);
    v_rdi = (v_rdi) >> (16);
    result = MiVaToFlushVm(v_rdi, *(unsigned __int64 *)(v_rip + 12478512), (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    v_stack_p6C = 20;
    v_stack_p70 = 8;
    v_stack_p74 = 1;
    v_stack_p60 = result;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 184))) >> (8));
    a1 = (unsigned __int8)((a1) >> (3));
    a1 = (unsigned __int8)((a1) & (1));
    v_stack_p78 = (unsigned __int8)(a1);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 184)))) & (15)) != 0) goto loc_00247502;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
    if (result != a1) goto loc_0024785A;
loc_00247502:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 184)))) & (15)) != 0) goto loc_00247860;
    a4 = 0;
    v_stack_p68 = 1;
    v_r11 = 0;
    v_stack_p7C = 0;
    v_stack_mF8 = 0;
    a3 = (unsigned int)(((unsigned int)(v_stack_p70)) & (0xFFFFFFDBULL));
    v_stack_mF0 = 0;
    v_stack_p38 = (unsigned int)((unsigned int)((unsigned int)(a3)));
    v_stack_p79 = 0;
    v_stack_p40 = v_rdi;
loc_00247548:
    v_stack_p70 = a3;
loc_0024754D:
    v_r12 = 0;
loc_00247550:
    v_stack_p30 = 0;
    if (0 == 0) goto loc_00247608;
    if ((((unsigned __int8)(a3)) & (2)) != 0) goto loc_002475C8;
    if (((*(unsigned __int64 *)(v_stack_mF0 + a4 - 1 * 8)) & (0xC00ULL)) != 0) goto loc_002475C8;
    v_r10 = (unsigned int)((*(unsigned __int64 *)(v_stack_mF0 + a4 - 1 * 8)) & (0x3FFULL));
    a1 = (*(unsigned __int64 *)(v_stack_mF0 + a4 - 1 * 8)) & (0xFFFFFFFFFFFFF000ULL);
    a2 = (v_r10 + 1) << (12);
    a2 = (a2) + (a1);
    if (a2 != v_stack_p40) goto loc_0024776E;
    if ((v_r10 + v_stack_p38 * 1) <= v_r10) goto loc_002475C0;
    if ((v_r10 + v_stack_p38 * 1) <= 0x3FFULL) goto loc_00247941;
loc_002475C0:
loc_002475C3:
loc_002475C8:
    if (0 == 0) goto loc_00247608;
    if ((((unsigned __int8)(a3)) & (2)) != 0) goto loc_00247608;
    if (((*(unsigned __int64 *)(v_stack_mF0 + a4 - 1 * 8)) & (0xC00ULL)) != 0) goto loc_00247608;
    a3 = (v_stack_p38) << (12);
    a1 = (*(unsigned __int64 *)(v_stack_mF0 + a4 - 1 * 8)) & (0xFFFFFFFFFFFFF000ULL);
    if (a1 == (a3 + v_stack_p40 * 1)) goto loc_002478C1;
loc_00247608:
    if (0 == v_stack_p6C) goto loc_002476C0;
loc_00247618:
    if (v_stack_p38 == 0) goto loc_002476D4;
    a2 = (unsigned int)(0x400ULL);
    if ((v_stack_p38 - 1) <= 0x3FFULL) { a2 = v_stack_p38; }
    a1 = (v_stack_p38) - (a2);
    v_stack_p38 = a1;
    a1 = (v_stack_p40) & (0xFFFFFFFFFFFFF000ULL);
    result = (unsigned int)((a2 - 1) & (0x3FFULL));
    result = (result) | (a1);
    a1 = (a2) << (12);
    v_r10 = (v_stack_p40) + (a1);
    v_stack_p40 = v_r10;
    *(unsigned __int64 *)(v_stack_m78 + 0 * 8 - 120) = result;
    a4 = (unsigned int)(((unsigned int)(v_stack_p7C)) + 1);
    v_r11 = (v_stack_mF8) + (a2);
    v_stack_p7C = (unsigned int)(a4);
    v_stack_mF8 = v_r11;
    if (v_stack_p38 == 0) goto loc_002476D4;
    if (((unsigned int)(a4)) != v_stack_p6C) goto loc_00247618;
    goto loc_0024754D;
loc_0024769F:
    a1 = (unsigned __int8)(~((unsigned __int8)(a4)));
    result = (-1) >> ((unsigned __int8)(a1));
    v_r10 = (v_r10) & (result);
    if (v_r10 != result) goto loc_0024730D;
    goto loc_0024739A;
loc_002476C0:
    if (0 == 0) goto loc_0024780C;
    if (v_stack_p79 == 0) goto loc_0024795F;
loc_002476D4:
    result = MiFlushTbList(v_stack_p60, v_stack_p38, (unsigned int)(v_stack_p70), a4);
loc_002476DE:
    a3 = (unsigned int)((v_stack_p20) & (31));
    a1 = (v_stack_p20) >> (5);
    if ((a3 + v_rsi * 1) > 32) goto loc_0024774C;
    if (v_rsi == 32) goto loc_002477EB;
    v_r13 = (unsigned int)((1) << ((unsigned __int8)(v_rsi)));
    v_r13 = (unsigned int)((v_r13) - 1);
    v_r13 = (unsigned int)((v_r13) << ((unsigned __int8)((unsigned int)(a3))));
    v_r13 = (unsigned int)(~(v_r13));
loc_00247721:
    result = ((unsigned int)((unsigned int)((unsigned int)(a3)))) + ((unsigned int)((unsigned int)((unsigned int)(a3))));
    if (result <= 0x200000ULL) goto loc_002473CA;
    result = MiAttemptCoalesce(a1, v_stack_p20, v_rsi, v_rsi);
    goto loc_002473CA;
loc_0024774C:
    if (v_rsi != 0) goto loc_00247799;
loc_00247751:
    if (v_rsi >= 32) goto loc_00247778;
loc_00247757:
    if (v_rsi == 0) goto loc_00247721;
    result = (unsigned int)((-1) << ((unsigned __int8)(v_rsi)));
    goto loc_00247721;
loc_0024776E:
    goto loc_002475C3;
loc_00247778:
    a1 = (v_rsi) >> (5);
    result = (result) * (a1);
    a4 = (v_rsi) + (result);
loc_00247786:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + a1 * 4) = 0;
    v_r10 = (*(unsigned __int64 *)(a1 + 8) + a1 * 4) + (4);
    a1 = (a1) - (1);
    if (condition_is_equal) goto loc_00247757;
    goto loc_00247786;
loc_00247799:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p20))) & (31));
    a2 = (unsigned int)((32) - ((unsigned int)(result)));
    v_r13 = (unsigned int)((v_r13) << ((unsigned __int8)((unsigned int)((unsigned int)(a2)))));
    v_r13 = (unsigned int)((v_r13) - 1);
    v_r13 = (unsigned int)((v_r13) << ((unsigned __int8)(v_rsi)));
    v_r13 = (unsigned int)(~(v_r13));
    a4 = (a4) - ((unsigned int)((unsigned int)(a2)));
    v_r10 = (v_r10) + (4);
    goto loc_00247751;
loc_002477C5:
    if (a1 == (v_rip + 12517020)) goto loc_002477E1;
    if (a1 != (v_rip + 12510888)) goto loc_002472D5;
loc_002477E1:
    v_stack_p30 = (unsigned int)(v_r13);
    goto loc_0024739F;
loc_002477EB:
    *(unsigned int *)(v_r10) = 0;
    goto loc_00247721;
loc_002477F7:
loc_002477FA:
    *(unsigned __int64 *)(v_stack_mF0 + a4 - 1 * 8) = v_rip + 12510888;
    v_rdi = (v_stack_mF0 + a4 - 1 * 8) + (8);
    a1 = ((unsigned int)((unsigned int)((unsigned int)(a3)))) - (v_r13);
    if (condition_is_equal) goto loc_00247449;
    goto loc_002477FA;
loc_0024780C:
    if (v_stack_p79 != 0) goto loc_002476D4;
    result = qsort(v_stack_mF0, (unsigned int)((unsigned int)(a4)), 8, v_rip + 4513899);
    result = MiCompressTbFlushList(v_stack_p60, (unsigned int)((unsigned int)(a4)), 8, v_rip + 4513899);
    goto loc_00247550;
loc_0024785A:
loc_00247860:
    result = 0;
    v_stack_p40 = v_rdi;
    a3 = (unsigned int)((9) & (0xFFFFFFDBULL));
    v_stack_mF0 = 0;
    v_stack_p70 = a3;
    v_stack_p38 = (unsigned int)((unsigned int)((unsigned int)(a3)));
    v_stack_mF8 = 0;
    v_stack_p7C = 0;
    v_stack_p79 = 0;
    v_stack_p68 = 0;
    if (v_rdi < ((unsigned int)((unsigned int)(v_r13)))) goto loc_0024754D;
    if (v_rdi > ((unsigned int)((unsigned int)(v_r13)))) goto loc_0024754D;
    a3 = (unsigned int)((a3) | (4));
    goto loc_00247548;
loc_002478C1:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) & (0x3FFULL));
    if ((a1 + v_stack_p38 * 1) <= 0x3FFULL) goto loc_00247907;
loc_002478DC:
    goto loc_00247608;
loc_002478E6:
    a4 = ((unsigned int)(v_stack_p30) + 511) & (-512);
    result = MiReturnSystemPtes(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r13)))), v_stack_p20, a4);
    goto loc_002473CA;
loc_00247907:
    if (((unsigned int)(v_stack_p30)) <= a1) goto loc_002478DC;
    result = (result) - (v_stack_p20);
    v_r11 = (0) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r13)))));
    v_stack_mF8 = v_r11;
    result = (result) ^ (result + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r13)))) * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (result + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r13)))) * 1);
    *(unsigned __int64 *)(v_rdi) = result;
    goto loc_002476D4;
loc_0024792E:
    result = MiCheckPteRelease(a1, v_rdi, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    goto loc_0024729D;
loc_00247941:
    v_r11 = (v_r11) + (a1);
    a1 = (a1) + (result);
    result = (result) ^ (a1);
    v_stack_mF8 = v_r11;
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (a1);
    *(unsigned __int64 *)(v_rdi) = result;
    goto loc_002476D4;
loc_0024795F:
    v_stack_p79 = (unsigned __int8)(v_r13);
    goto loc_002476D4;
}
```

## 5. (Beta) C Style

```c
int64_t MiReleasePtes(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m118;
    uint64_t v_stack_m130;
    uint32_t v_stack_m148;
    uint64_t v_stack_m158;
    uint64_t v_stack_m48;
    uint64_t v_stack_m78;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p60;
    uint32_t v_stack_p68;
    uint32_t v_stack_p6C;
    uint32_t v_stack_p70;
    uint32_t v_stack_p74;
    uint8_t v_stack_p78;
    uint16_t v_stack_p79;
    uint32_t v_stack_p7C;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (320);
    result = (*(uint64_t *)(v_rip + 0xBC34DD)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m130 = 0;
    Arg2 = 0;
    result = memset(v_stack_m118, Arg2, 200, a4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) & (4)) != 0) goto loc_0024792E;
loc_0024729D:
    local_rbx = (0) - (*(uint64_t *)(arg1 + 0x20));
    local_rbx = (local_rbx) >> (3);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x28))) & (1));
    if (!(condition_is_equal)) {
        local_rbx = (local_rbx) >> (4);
    }
    local_rsi = ((uint32_t)((uint32_t)((uint32_t)(Arg3)))) >> (4);
    if ((uint32_t)(result) == 0) { local_rsi = (uint32_t)((uint32_t)((uint32_t)(Arg3))); }
    if (((uint32_t)((uint32_t)(Arg3))) >= 512) goto loc_002477C5;
loc_002472D5:
    v_stack_m148 = 0;
    if (local_rbx >= (*(uint64_t *)(arg1))) goto loc_0024730D;
    if (local_rsi > 1) goto loc_00247344;
    if (local_rsi != 1) goto loc_0024730D;
    Arg2 = (uint32_t)((local_rbx) & (63));
    Arg1 = (local_rbx) >> (6);
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) != 0) goto loc_0024739A;
loc_0024730D:
    local_rdi = (Arg2) << (25);
    result = ((uint32_t)(Arg3)) << (25);
    local_rdi = (local_rdi) - (result);
    v_stack_m158 = local_rbx;
    local_rdi = (local_rdi) >> (16);
    result = KeBugCheckEx(218, 770, local_rdi, (uint32_t)((uint32_t)((uint32_t)(Arg3))));
loc_00247344:
    result = (result) - (local_rbx);
    if (result < local_rsi) goto loc_0024730D;
    a4 = (local_rsi - 1) + (local_rbx);
    result = (local_rbx) >> (6);
    result = (a4) >> (6);
    if ((*(uint64_t *)(arg1 + 0x8) + result * 8) != (*(uint64_t *)(arg1 + 0x8) + result * 8)) goto loc_002473F2;
    Arg1 = (uint8_t)((64) - ((uint8_t)(local_rsi)));
    result = (-1) >> ((uint8_t)(Arg1));
    result = (result) << ((uint8_t)(local_rbx));
    local_r10 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + result * 8)) & (result);
    if (local_r10 != result) goto loc_0024730D;
loc_0024739A:
    if ((uint32_t)((uint32_t)(Arg3)) == 0) goto loc_002473B8;
loc_0024739F:
loc_002473AC:
    *(uint64_t *)(local_rdi) = *(uint64_t *)(v_rip - 0x236B26);
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(Arg3)))) - (1);
    if (condition_is_not_equal) goto loc_002473AC;
loc_002473B8:
    result = MiInsertCachedPte(Arg1, local_rdi, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    if ((uint32_t)(result) == 0) goto loc_0024741B;
loc_002473CA:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, local_rdi, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    local_rsp = (local_rsp) + (320);
    return result;
loc_002473F2:
    result = (result) << ((uint8_t)(v_stack_p20));
    local_r10 = (local_r10) & (result);
loc_002473FE:
    if (local_r10 != result) goto loc_0024730D;
    Arg2 = (local_rdi) + (8);
    if (Arg2 == ((uint32_t)((uint32_t)((uint32_t)(Arg3))))) goto loc_0024769F;
    goto loc_002473FE;
loc_0024741B:
    if (((uint32_t)((uint32_t)(v_stack_p30))) == 1) goto loc_002478E6;
    v_stack_p48 = 0;
    result = MiInitializeTbFlushStamps(v_stack_p48, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    if ((uint32_t)((uint32_t)(Arg3)) != 0) goto loc_002477F7;
loc_00247449:
    Arg1 = -((uint32_t)((uint32_t)((uint32_t)(Arg3))));
    if (*(uint64_t *)(v_rip + 0xBE6830) == 0) goto loc_00247470;
    result = v_stack_p48;
    if ((((uint8_t)(v_stack_p48)) & (16)) == 0) {
        result = *(uint64_t *)(v_rip + 0xBE6830);
        result = ~(result);
        result = (result) & (v_stack_p48);
    }
    if (((v_stack_p48) & (result)) != 0) goto loc_002476DE;
    local_rdi = (local_rdi + Arg1 * 8) << (25);
    result = ((uint32_t)(Arg3)) << (25);
    local_rdi = (local_rdi) - (result);
    local_rdi = (local_rdi) >> (16);
    result = MiVaToFlushVm(local_rdi, *(uint64_t *)(v_rip + 0xBE6830), (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    v_stack_p6C = 20;
    v_stack_p70 = 8;
    v_stack_p74 = 1;
    v_stack_p60 = result;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0xB8))) >> (8));
    Arg1 = (uint8_t)((Arg1) >> (3));
    Arg1 = (uint8_t)((Arg1) & (1));
    v_stack_p78 = (uint8_t)(Arg1);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xB8)))) & (15)) != 0) goto loc_00247502;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
    if (result != Arg1) goto loc_0024785A;
loc_00247502:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xB8)))) & (15)) != 0) goto loc_00247860;
    a4 = 0;
    v_stack_p68 = 1;
    local_r11 = 0;
    v_stack_p7C = 0;
    v_stack_mF8 = 0;
    Arg3 = (uint32_t)(((uint32_t)(v_stack_p70)) & (0xFFFFFFDBULL));
    v_stack_mF0 = 0;
    v_stack_p38 = (uint32_t)((uint32_t)((uint32_t)(Arg3)));
    v_stack_p79 = 0;
    v_stack_p40 = local_rdi;
loc_00247548:
    v_stack_p70 = Arg3;
loc_0024754D:
    local_r12 = 0;
loc_00247550:
    v_stack_p30 = 0;
    if (0 == 0) goto loc_00247608;
    if ((((uint8_t)(Arg3)) & (2)) != 0) goto loc_002475C8;
    if (((*(uint64_t *)(v_stack_mF0 + a4 - 0x1 * 8)) & (0xC00ULL)) != 0) goto loc_002475C8;
    local_r10 = (uint32_t)((*(uint64_t *)(v_stack_mF0 + a4 - 0x1 * 8)) & (0x3FFULL));
    Arg1 = (*(uint64_t *)(v_stack_mF0 + a4 - 0x1 * 8)) & (0xFFFFFFFFFFFFF000ULL);
    Arg2 = (local_r10 + 1) << (12);
    Arg2 = (Arg2) + (Arg1);
    if (Arg2 != v_stack_p40) goto loc_0024776E;
    if ((local_r10 + v_stack_p38 * 1) <= local_r10) goto loc_002475C0;
    if ((local_r10 + v_stack_p38 * 1) <= 0x3FFULL) goto loc_00247941;
loc_002475C0:
loc_002475C3:
loc_002475C8:
    if (0 == 0) goto loc_00247608;
    if ((((uint8_t)(Arg3)) & (2)) != 0) goto loc_00247608;
    if (((*(uint64_t *)(v_stack_mF0 + a4 - 0x1 * 8)) & (0xC00ULL)) != 0) goto loc_00247608;
    Arg3 = (v_stack_p38) << (12);
    Arg1 = (*(uint64_t *)(v_stack_mF0 + a4 - 0x1 * 8)) & (0xFFFFFFFFFFFFF000ULL);
    if (Arg1 == (Arg3 + v_stack_p40 * 1)) goto loc_002478C1;
loc_00247608:
    if (0 == v_stack_p6C) goto loc_002476C0;
loc_00247618:
    if (v_stack_p38 == 0) goto loc_002476D4;
    Arg2 = (uint32_t)(0x400ULL);
    if ((v_stack_p38 - 1) <= 0x3FFULL) { Arg2 = v_stack_p38; }
    Arg1 = (v_stack_p38) - (Arg2);
    v_stack_p38 = Arg1;
    Arg1 = (v_stack_p40) & (0xFFFFFFFFFFFFF000ULL);
    result = (uint32_t)((Arg2 - 1) & (0x3FFULL));
    result = (result) | (Arg1);
    Arg1 = (Arg2) << (12);
    local_r10 = (v_stack_p40) + (Arg1);
    v_stack_p40 = local_r10;
    *(uint64_t *)(v_stack_m78 + 0x0 * 8 - 0x78) = result;
    a4 = (uint32_t)(((uint32_t)(v_stack_p7C)) + 1);
    local_r11 = (v_stack_mF8) + (Arg2);
    v_stack_p7C = (uint32_t)(a4);
    v_stack_mF8 = local_r11;
    if (v_stack_p38 == 0) goto loc_002476D4;
    if (((uint32_t)(a4)) != v_stack_p6C) goto loc_00247618;
    goto loc_0024754D;
loc_0024769F:
    Arg1 = (uint8_t)(~((uint8_t)(a4)));
    result = (-1) >> ((uint8_t)(Arg1));
    local_r10 = (local_r10) & (result);
    if (local_r10 != result) goto loc_0024730D;
    goto loc_0024739A;
loc_002476C0:
    if (0 == 0) goto loc_0024780C;
    if (v_stack_p79 == 0) goto loc_0024795F;
loc_002476D4:
    result = MiFlushTbList(v_stack_p60, v_stack_p38, (uint32_t)(v_stack_p70), a4);
loc_002476DE:
    Arg3 = (uint32_t)((v_stack_p20) & (31));
    Arg1 = (v_stack_p20) >> (5);
    if ((Arg3 + local_rsi * 1) > 32) goto loc_0024774C;
    if (local_rsi == 32) goto loc_002477EB;
    local_r13 = (uint32_t)((1) << ((uint8_t)(local_rsi)));
    local_r13 = (uint32_t)((local_r13) - 1);
    local_r13 = (uint32_t)((local_r13) << ((uint8_t)((uint32_t)(Arg3))));
    local_r13 = (uint32_t)(~(local_r13));
loc_00247721:
    result = ((uint32_t)((uint32_t)((uint32_t)(Arg3)))) + ((uint32_t)((uint32_t)((uint32_t)(Arg3))));
    if (result <= 0x200000ULL) goto loc_002473CA;
    result = MiAttemptCoalesce(Arg1, v_stack_p20, local_rsi, local_rsi);
    goto loc_002473CA;
loc_0024774C:
    if (local_rsi != 0) goto loc_00247799;
loc_00247751:
    if (local_rsi >= 32) goto loc_00247778;
loc_00247757:
    if (local_rsi == 0) goto loc_00247721;
    result = (uint32_t)((-1) << ((uint8_t)(local_rsi)));
    goto loc_00247721;
loc_0024776E:
    goto loc_002475C3;
loc_00247778:
    Arg1 = (local_rsi) >> (5);
    result = (result) * (Arg1);
    a4 = (local_rsi) + (result);
loc_00247786:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + arg1 * 4) = 0;
    local_r10 = (*(uint64_t *)(arg1 + 0x8) + Arg1 * 4) + (4);
    Arg1 = (Arg1) - (1);
    if (condition_is_equal) goto loc_00247757;
    goto loc_00247786;
loc_00247799:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p20))) & (31));
    Arg2 = (uint32_t)((32) - ((uint32_t)(result)));
    local_r13 = (uint32_t)((local_r13) << ((uint8_t)((uint32_t)((uint32_t)(Arg2)))));
    local_r13 = (uint32_t)((local_r13) - 1);
    local_r13 = (uint32_t)((local_r13) << ((uint8_t)(local_rsi)));
    local_r13 = (uint32_t)(~(local_r13));
    a4 = (a4) - ((uint32_t)((uint32_t)(Arg2)));
    local_r10 = (local_r10) + (4);
    goto loc_00247751;
loc_002477C5:
    if (Arg1 == (v_rip + 12517020)) goto loc_002477E1;
    if (Arg1 != (v_rip + 12510888)) goto loc_002472D5;
loc_002477E1:
    v_stack_p30 = (uint32_t)(local_r13);
    goto loc_0024739F;
loc_002477EB:
    *(uint32_t *)(local_r10) = 0;
    goto loc_00247721;
loc_002477F7:
loc_002477FA:
    *(uint64_t *)(v_stack_mF0 + a4 - 0x1 * 8) = v_rip + 12510888;
    local_rdi = (v_stack_mF0 + a4 - 1 * 8) + (8);
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(Arg3)))) - (local_r13);
    if (condition_is_equal) goto loc_00247449;
    goto loc_002477FA;
loc_0024780C:
    if (v_stack_p79 != 0) goto loc_002476D4;
    result = qsort(v_stack_mF0, (uint32_t)((uint32_t)(a4)), 8, v_rip + 4513899);
    result = MiCompressTbFlushList(v_stack_p60, (uint32_t)((uint32_t)(a4)), 8, v_rip + 4513899);
    goto loc_00247550;
loc_0024785A:
loc_00247860:
    result = 0;
    v_stack_p40 = local_rdi;
    Arg3 = (uint32_t)((9) & (0xFFFFFFDBULL));
    v_stack_mF0 = 0;
    v_stack_p70 = Arg3;
    v_stack_p38 = (uint32_t)((uint32_t)((uint32_t)(Arg3)));
    v_stack_mF8 = 0;
    v_stack_p7C = 0;
    v_stack_p79 = 0;
    v_stack_p68 = 0;
    if (local_rdi < ((uint32_t)((uint32_t)(local_r13)))) goto loc_0024754D;
    if (local_rdi > ((uint32_t)((uint32_t)(local_r13)))) goto loc_0024754D;
    Arg3 = (uint32_t)((Arg3) | (4));
    goto loc_00247548;
loc_002478C1:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) & (0x3FFULL));
    if ((Arg1 + v_stack_p38 * 1) <= 0x3FFULL) goto loc_00247907;
loc_002478DC:
    goto loc_00247608;
loc_002478E6:
    a4 = ((uint32_t)(v_stack_p30) + 511) & (-512);
    result = MiReturnSystemPtes(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r13)))), v_stack_p20, a4);
    goto loc_002473CA;
loc_00247907:
    if (((uint32_t)(v_stack_p30)) <= Arg1) goto loc_002478DC;
    result = (result) - (v_stack_p20);
    local_r11 = (0) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r13)))));
    v_stack_mF8 = local_r11;
    result = (result) ^ (result + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r13)))) * 1);
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (result + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r13)))) * 1);
    *(uint64_t *)(local_rdi) = result;
    goto loc_002476D4;
loc_0024792E:
    result = MiCheckPteRelease(Arg1, local_rdi, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    goto loc_0024729D;
loc_00247941:
    local_r11 = (local_r11) + (Arg1);
    Arg1 = (Arg1) + (result);
    result = (result) ^ (Arg1);
    v_stack_mF8 = local_r11;
    result = (result) & (0xFFFFFFFFFFFFFC00ULL);
    result = (result) ^ (Arg1);
    *(uint64_t *)(local_rdi) = result;
    goto loc_002476D4;
loc_0024795F:
    v_stack_p79 = (uint8_t)(local_r13);
    goto loc_002476D4;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00247240&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
