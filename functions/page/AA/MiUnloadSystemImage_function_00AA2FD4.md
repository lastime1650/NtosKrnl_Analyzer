# MiUnloadSystemImage

- RVA: `0x00AA2FD4`–`0x00AA3498` (길이 `1,220` bytes)
- VA: `0x0000000140AA2FD4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BB268`
- 디코드: `304`개 명령, `1,220/1,220` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **47**; 고유 호출 대상: **45**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00AA2FFC` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AA301C` → [MiGetBaseLoaderPortion](../../text/4D/MiGetBaseLoaderPortion_function_004D9D34.md) (function, `0x004D9D34`)
- `0x00AA303D` → [MiAcquireLoadLock](../../text/2A/MiAcquireLoadLock_function_002A3950.md) (function, `0x002A3950`)
- `0x00AA305E` → [MmReleaseLoadLock](../../text/4D/MmReleaseLoadLock_function_004D36D0.md) (function, `0x004D36D0`)
- `0x00AA3092` → [MiSectionControlArea](../../text/29/MiSectionControlArea_function_00294CB0.md) (function, `0x00294CB0`)
- `0x00AA30B3` → [MiGetPteAddress](../../text/43/MiGetPteAddress_function_0043E130.md) (function, `0x0043E130`)
- `0x00AA30E0` → [KeCleanupImageTracepoints](KeCleanupImageTracepoints_function_00AA76E4.md) (function, `0x00AA76E4`)
- `0x00AA30FB` → [MiMarkKernelImageCfgBits](../A4/MiMarkKernelImageCfgBits_function_00A4B1E0.md) (function, `0x00A4B1E0`)
- `0x00AA311B` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00AA313E` → [MiClearDriverTablePtes](../../text/68/MiClearDriverTablePtes_function_00683024.md) (function, `0x00683024`)
- `0x00AA3146` → [MiUnmapKernelScp](../../text/4A/MiUnmapKernelScp_function_004A82E8.md) (function, `0x004A82E8`)
- `0x00AA314B` → [KeIsRetpolineEnabled](../../text/44/KeIsRetpolineEnabled_function_0044EE20.md) (function, `0x0044EE20`)
- `0x00AA3159` → [MiMarkKernelImageRetpolineBits](MiMarkKernelImageRetpolineBits_function_00AA0348.md) (function, `0x00AA0348`)
- `0x00AA3161` → [MiIsImageFullyRetpolined](../AB/MiIsImageFullyRetpolined_function_00AB01D4.md) (function, `0x00AB01D4`)
- `0x00AA316A` → [KeFlushRsb](../../text/5B/KeFlushRsb_function_005BE8E4.md) (function, `0x005BE8E4`)
- `0x00AA317E` → [MiFreeRetpolineRelocationInformation](../93/MiFreeRetpolineRelocationInformation_function_0093F194.md) (function, `0x0093F194`)
- `0x00AA3199` → [VfDriverUnloadImage](../../pagevrfy/B9/VfDriverUnloadImage_function_00B9A5B0.md) (function, `0x00B9A5B0`)
- `0x00AA31AD` → [KseDriverUnloadImage](../95/KseDriverUnloadImage_function_009587E0.md) (function, `0x009587E0`)
- `0x00AA31C1` → [KasanDriverUnloadImage](../../text/5A/KasanDriverUnloadImage_function_005AA9B0.md) (function, `0x005AA9B0`)
- `0x00AA31CE` → [MiDereferenceImports](../7F/MiDereferenceImports_function_007F7DB4.md) (function, `0x007F7DB4`)
- `0x00AA31D6` → [MiFreeLoadedImportList](../AB/MiFreeLoadedImportList_function_00AB6380.md) (function, `0x00AB6380`)
- `0x00AA31E3` → [LdrUnloadAlternateResourceModule](../../text/45/LdrUnloadAlternateResourceModule_function_00454ACC.md) (function, `0x00454ACC`)
- `0x00AA31FE` → [DbgUnLoadImageSymbolsUnicode](../../text/4A/DbgUnLoadImageSymbolsUnicode_function_004AE114.md) (function, `0x004AE114`)
- `0x00AA320C` → [MiBytesToMapSystemImage](../A7/MiBytesToMapSystemImage_function_00A750C4.md) (function, `0x00A750C4`)
- `0x00AA3246` → [MiRememberUnloadedDriver](../AC/MiRememberUnloadedDriver_function_00ACDC80.md) (function, `0x00ACDC80`)
- `0x00AA3278` → [MiManageSubsectionView](../../text/2E/MiManageSubsectionView_function_002E2570.md) (function, `0x002E2570`)
- `0x00AA3280` → [MiUnlockDriverCode](../A9/MiUnlockDriverCode_function_00A9FFEC.md) (function, `0x00A9FFEC`)
- `0x00AA32B7` → [MiDecommitPages](../../text/24/MiDecommitPages_function_00241BD0.md) (function, `0x00241BD0`)
- `0x00AA32D2` → [MmHasImageBeenImportOptimized](../70/MmHasImageBeenImportOptimized_function_00704CD8.md) (function, `0x00704CD8`)
- `0x00AA32DB` → [MiFreeRetpolineImportInfo](MiFreeRetpolineImportInfo_function_00AAFF1C.md) (function, `0x00AAFF1C`)
- `0x00AA32E5` → [Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting](../../text/22/Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting_function_00222FE0.md) (function, `0x00222FE0`)
- `0x00AA3306` → [MiUnloadSystemImageSoftWsles](../../text/69/MiUnloadSystemImageSoftWsles_function_00697978.md) (function, `0x00697978`)
- `0x00AA331F` → [MiReturnSystemImageCommitment](MiReturnSystemImageCommitment_function_00AA6BE8.md) (function, `0x00AA6BE8`)
- `0x00AA3333` → [MiRemoveLoaderEntry](../../text/67/MiRemoveLoaderEntry_function_006713C8.md) (function, `0x006713C8`)
- `0x00AA337D` → [PerfLogImageUnload](../A2/PerfLogImageUnload_function_00A2216C.md) (function, `0x00A2216C`)
- `0x00AA3391` → [MiUpdateDriverLoadInProgress](../../text/43/MiUpdateDriverLoadInProgress_function_004318DC.md) (function, `0x004318DC`)
- `0x00AA33B9` → [MiReleasePrivilegedPtes](../7F/MiReleasePrivilegedPtes_function_007F9264.md) (function, `0x007F9264`)
- `0x00AA33D6` → [MiReleaseDriverPtes](../A7/MiReleaseDriverPtes_function_00A7F1B4.md) (function, `0x00A7F1B4`)
- `0x00AA33EB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AA3408` → [MiReturnResident](../../text/28/MiReturnResident_function_00286890.md) (function, `0x00286890`)
- `0x00AA3425` → [MiFreePrivateFixupEntryForSystemImage](../../text/4B/MiFreePrivateFixupEntryForSystemImage_function_004B8F54.md) (function, `0x004B8F54`)
- `0x00AA3432` → [MiReturnSystemImageAddress](../A7/MiReturnSystemImageAddress_function_00A7F190.md) (function, `0x00A7F190`)
- `0x00AA3446` → [MiReturnCrossPartitionControlAreaCharges](../../text/4D/MiReturnCrossPartitionControlAreaCharges_function_004D6184.md) (function, `0x004D6184`)
- `0x00AA345A` → [MiDereferenceControlArea](../../text/47/MiDereferenceControlArea_function_00479A20.md) (function, `0x00479A20`)
- `0x00AA3467` → [ObDereferenceObjectDeferDeleteWithTag](../../text/26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x00AA3474` → [MmReleaseLoadLock](../../text/4D/MmReleaseLoadLock_function_004D36D0.md) (function, `0x004D36D0`)
- `0x00AA347E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MiDereferenceImports](../7F/MiDereferenceImports_function_007F7DB4.md) at `0x007F7E15`
- [MmLoadSystemImageEx](../99/MmLoadSystemImageEx_function_00999B8C.md) at `0x00999D02`
- [MmUnloadSystemImage](MmUnloadSystemImage_function_00AA2F60.md) at `0x00AA2FA7`
- [MmRegisterHotPatches](../../init/C6/MmRegisterHotPatches_function_00C678DC.md) at `0x00C67C4B`

### Static image references
- `0x00AA312D` → RVA `0x00E375AC` (`.data`; read)
- `0x00AA3133` → RVA `0x00E375B0` (`.data`; read)
- `0x00AA32C8` → RVA `0x00E2D974` (`.data`; read/write)
- `0x00AA3338` → RVA `0x00FC6B00` (`ALMOSTRO`; read)
- `0x00AA3401` → RVA `0x00E38D00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **29**
  - `0x00AA2FFC` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AA301C` → [MiGetBaseLoaderPortion](../../text/4D/MiGetBaseLoaderPortion_function_004D9D34.md) (`PAGE` → `.text`)
  - `0x00AA303D` → [MiAcquireLoadLock](../../text/2A/MiAcquireLoadLock_function_002A3950.md) (`PAGE` → `.text`)
  - `0x00AA305E` → [MmReleaseLoadLock](../../text/4D/MmReleaseLoadLock_function_004D36D0.md) (`PAGE` → `.text`)
  - `0x00AA3092` → [MiSectionControlArea](../../text/29/MiSectionControlArea_function_00294CB0.md) (`PAGE` → `.text`)
  - `0x00AA30B3` → [MiGetPteAddress](../../text/43/MiGetPteAddress_function_0043E130.md) (`PAGE` → `.text`)
  - `0x00AA311B` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00AA313E` → [MiClearDriverTablePtes](../../text/68/MiClearDriverTablePtes_function_00683024.md) (`PAGE` → `.text`)
  - `0x00AA3146` → [MiUnmapKernelScp](../../text/4A/MiUnmapKernelScp_function_004A82E8.md) (`PAGE` → `.text`)
  - `0x00AA314B` → [KeIsRetpolineEnabled](../../text/44/KeIsRetpolineEnabled_function_0044EE20.md) (`PAGE` → `.text`)
  - `0x00AA316A` → [KeFlushRsb](../../text/5B/KeFlushRsb_function_005BE8E4.md) (`PAGE` → `.text`)
  - `0x00AA3199` → [VfDriverUnloadImage](../../pagevrfy/B9/VfDriverUnloadImage_function_00B9A5B0.md) (`PAGE` → `PAGEVRFY`)
  - `0x00AA31C1` → [KasanDriverUnloadImage](../../text/5A/KasanDriverUnloadImage_function_005AA9B0.md) (`PAGE` → `.text`)
  - `0x00AA31E3` → [LdrUnloadAlternateResourceModule](../../text/45/LdrUnloadAlternateResourceModule_function_00454ACC.md) (`PAGE` → `.text`)
  - `0x00AA31FE` → [DbgUnLoadImageSymbolsUnicode](../../text/4A/DbgUnLoadImageSymbolsUnicode_function_004AE114.md) (`PAGE` → `.text`)
  - `0x00AA3278` → [MiManageSubsectionView](../../text/2E/MiManageSubsectionView_function_002E2570.md) (`PAGE` → `.text`)
  - `0x00AA32B7` → [MiDecommitPages](../../text/24/MiDecommitPages_function_00241BD0.md) (`PAGE` → `.text`)
  - `0x00AA32E5` → [Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting](../../text/22/Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting_function_00222FE0.md) (`PAGE` → `.text`)
  - `0x00AA3306` → [MiUnloadSystemImageSoftWsles](../../text/69/MiUnloadSystemImageSoftWsles_function_00697978.md) (`PAGE` → `.text`)
  - `0x00AA3333` → [MiRemoveLoaderEntry](../../text/67/MiRemoveLoaderEntry_function_006713C8.md) (`PAGE` → `.text`)
  - `0x00AA3391` → [MiUpdateDriverLoadInProgress](../../text/43/MiUpdateDriverLoadInProgress_function_004318DC.md) (`PAGE` → `.text`)
  - `0x00AA33EB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AA3408` → [MiReturnResident](../../text/28/MiReturnResident_function_00286890.md) (`PAGE` → `.text`)
  - `0x00AA3425` → [MiFreePrivateFixupEntryForSystemImage](../../text/4B/MiFreePrivateFixupEntryForSystemImage_function_004B8F54.md) (`PAGE` → `.text`)
  - `0x00AA3446` → [MiReturnCrossPartitionControlAreaCharges](../../text/4D/MiReturnCrossPartitionControlAreaCharges_function_004D6184.md) (`PAGE` → `.text`)
  - `0x00AA345A` → [MiDereferenceControlArea](../../text/47/MiDereferenceControlArea_function_00479A20.md) (`PAGE` → `.text`)
  - `0x00AA3467` → [ObDereferenceObjectDeferDeleteWithTag](../../text/26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (`PAGE` → `.text`)
  - `0x00AA3474` → [MmReleaseLoadLock](../../text/4D/MmReleaseLoadLock_function_004D36D0.md) (`PAGE` → `.text`)
  - `0x00AA347E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA2FD4  40 55                           push rbp
00AA2FD6  53                              push rbx
00AA2FD7  56                              push rsi
00AA2FD8  57                              push rdi
00AA2FD9  41 54                           push r12
00AA2FDB  41 55                           push r13
00AA2FDD  41 56                           push r14
00AA2FDF  41 57                           push r15
00AA2FE1  48 8D 6C 24 C8                  lea rbp, [rsp - 0x38]
00AA2FE6  48 81 EC 38 01 00 00            sub rsp, 0x138
00AA2FED  48 8B D9                        mov rbx, rcx
00AA2FF0  33 D2                           xor edx, edx
00AA2FF2  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00AA2FF6  41 B8 98 00 00 00               mov r8d, 0x98
00AA2FFC  E8 3F 3C C2 FF                  call 0x1406c6c40
00AA3001  0F 57 C0                        xorps xmm0, xmm0
00AA3004  33 C0                           xor eax, eax
00AA3006  48 8B CB                        mov rcx, rbx
00AA3009  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00AA300D  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
00AA3012  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
00AA3017  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
00AA301C  E8 13 6D A3 FF                  call 0x1404d9d34
00AA3021  45 33 E4                        xor r12d, r12d
00AA3024  48 8B F8                        mov rdi, rax
00AA3027  F7 80 B8 00 00 00 00 01 00 00   test dword ptr [rax + 0xb8], 0x100
00AA3031  74 05                           je 0x140aa3038
00AA3033  45 8B F4                        mov r14d, r12d
00AA3036  EB 0D                           jmp 0x140aa3045
00AA3038  B9 01 00 00 00                  mov ecx, 1
00AA303D  E8 0E 09 80 FF                  call 0x1402a3950
00AA3042  4C 8B F0                        mov r14, rax
00AA3045  4C 8B BB 88 00 00 00            mov r15, qword ptr [rbx + 0x88]
00AA304C  49 83 FF 01                     cmp r15, 1
00AA3050  75 16                           jne 0x140aa3068
00AA3052  4D 85 F6                        test r14, r14
00AA3055  0F 84 28 04 00 00               je 0x140aa3483
00AA305B  49 8B CE                        mov rcx, r14
00AA305E  E8 6D 06 A3 FF                  call 0x1404d36d0
00AA3063  E9 1B 04 00 00                  jmp 0x140aa3483
00AA3068  B8 FF FF 00 00                  mov eax, 0xffff
00AA306D  66 01 43 6C                     add word ptr [rbx + 0x6c], ax
00AA3071  75 DF                           jne 0x140aa3052
00AA3073  44 8B 87 B8 00 00 00            mov r8d, dword ptr [rdi + 0xb8]
00AA307A  41 0F BA E8 09                  bts r8d, 9
00AA307F  44 89 87 B8 00 00 00            mov dword ptr [rdi + 0xb8], r8d
00AA3086  4C 8B 6B 70                     mov r13, qword ptr [rbx + 0x70]
00AA308A  4D 85 ED                        test r13, r13
00AA308D  74 11                           je 0x140aa30a0
00AA308F  49 8B CD                        mov rcx, r13
00AA3092  E8 19 1C 7F FF                  call 0x140294cb0
00AA3097  48 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], rax
00AA309E  EB 07                           jmp 0x140aa30a7
00AA30A0  4C 89 A5 90 00 00 00            mov qword ptr [rbp + 0x90], r12
00AA30A7  48 8B 73 30                     mov rsi, qword ptr [rbx + 0x30]
00AA30AB  48 85 F6                        test rsi, rsi
00AA30AE  74 11                           je 0x140aa30c1
00AA30B0  48 8B CE                        mov rcx, rsi
00AA30B3  E8 78 B0 99 FF                  call 0x14043e130
00AA30B8  48 89 85 88 00 00 00            mov qword ptr [rbp + 0x88], rax
00AA30BF  EB 07                           jmp 0x140aa30c8
00AA30C1  4C 89 A5 88 00 00 00            mov qword ptr [rbp + 0x88], r12
00AA30C8  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
00AA30CB  48 C1 E8 0C                     shr rax, 0xc
00AA30CF  48 89 85 98 00 00 00            mov qword ptr [rbp + 0x98], rax
00AA30D6  41 0F BA E0 0A                  bt r8d, 0xa
00AA30DB  73 08                           jae 0x140aa30e5
00AA30DD  48 8B CB                        mov rcx, rbx
00AA30E0  E8 FF 45 00 00                  call 0x140aa76e4
00AA30E5  F7 87 B8 00 00 00 00 00 08 00   test dword ptr [rdi + 0xb8], 0x80000
00AA30EF  75 05                           jne 0x140aa30f6
00AA30F1  4D 85 ED                        test r13, r13
00AA30F4  75 2B                           jne 0x140aa3121
00AA30F6  33 D2                           xor edx, edx
00AA30F8  48 8B CB                        mov rcx, rbx
00AA30FB  E8 E0 80 FA FF                  call 0x140a4b1e0
00AA3100  85 C0                           test eax, eax
00AA3102  79 1D                           jns 0x140aa3121
00AA3104  48 98                           cdqe
00AA3106  4C 8B CB                        mov r9, rbx
00AA3109  4C 8B C6                        mov r8, rsi
00AA310C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AA3111  BA 15 10 00 00                  mov edx, 0x1015
00AA3116  B9 1A 00 00 00                  mov ecx, 0x1a
00AA311B  E8 40 A5 A5 FF                  call 0x1404fd660
00AA3120  CC                              int3
00AA3121  F7 87 B8 00 00 00 00 00 04 00   test dword ptr [rdi + 0xb8], 0x40000
00AA312B  74 45                           je 0x140aa3172
00AA312D  8B 0D 79 44 39 00               mov ecx, dword ptr [rip + 0x394479]
00AA3133  03 0D 77 44 39 00               add ecx, dword ptr [rip + 0x394477]
00AA3139  74 08                           je 0x140aa3143
00AA313B  48 8B CB                        mov rcx, rbx
00AA313E  E8 E1 FE BD FF                  call 0x140683024
00AA3143  48 8B CB                        mov rcx, rbx
00AA3146  E8 9D 51 A0 FF                  call 0x1404a82e8
00AA314B  E8 D0 BC 9A FF                  call 0x14044ee20
00AA3150  84 C0                           test al, al
00AA3152  74 1E                           je 0x140aa3172
00AA3154  33 D2                           xor edx, edx
00AA3156  48 8B CB                        mov rcx, rbx
00AA3159  E8 EA D1 FF FF                  call 0x140aa0348
00AA315E  48 8B CB                        mov rcx, rbx
00AA3161  E8 6E D0 00 00                  call 0x140ab01d4
00AA3166  85 C0                           test eax, eax
00AA3168  74 05                           je 0x140aa316f
00AA316A  E8 75 B7 B1 FF                  call 0x1405be8e4
00AA316F  0F AE E8                        lfence
00AA3172  48 8B 8F 18 01 00 00            mov rcx, qword ptr [rdi + 0x118]
00AA3179  48 85 C9                        test rcx, rcx
00AA317C  74 0C                           je 0x140aa318a
00AA317E  E8 11 C0 E9 FF                  call 0x14093f194
00AA3183  4C 89 A7 18 01 00 00            mov qword ptr [rdi + 0x118], r12
00AA318A  F7 87 B8 00 00 00 00 80 00 00   test dword ptr [rdi + 0xb8], 0x8000
00AA3194  74 1C                           je 0x140aa31b2
00AA3196  48 8B CB                        mov rcx, rbx
00AA3199  E8 12 74 0F 00                  call 0x140b9a5b0
00AA319E  F7 87 B8 00 00 00 00 00 01 00   test dword ptr [rdi + 0xb8], 0x10000
00AA31A8  74 08                           je 0x140aa31b2
00AA31AA  48 8B CB                        mov rcx, rbx
00AA31AD  E8 2E 56 EB FF                  call 0x1409587e0
00AA31B2  F7 87 B8 00 00 00 00 00 02 00   test dword ptr [rdi + 0xb8], 0x20000
00AA31BC  74 08                           je 0x140aa31c6
00AA31BE  48 8B CB                        mov rcx, rbx
00AA31C1  E8 EA 77 B0 FF                  call 0x1405aa9b0
00AA31C6  4D 85 FF                        test r15, r15
00AA31C9  74 10                           je 0x140aa31db
00AA31CB  49 8B CF                        mov rcx, r15
00AA31CE  E8 E1 4B D5 FF                  call 0x1407f7db4
00AA31D3  49 8B CF                        mov rcx, r15
00AA31D6  E8 A5 31 01 00                  call 0x140ab6380
00AA31DB  48 85 F6                        test rsi, rsi
00AA31DE  74 08                           je 0x140aa31e8
00AA31E0  48 8B CE                        mov rcx, rsi
00AA31E3  E8 E4 18 9B FF                  call 0x140454acc
00AA31E8  F7 43 68 00 00 10 00            test dword ptr [rbx + 0x68], 0x100000
00AA31EF  74 12                           je 0x140aa3203
00AA31F1  41 B8 FF FF FF FF               mov r8d, 0xffffffff
00AA31F7  48 8D 4B 58                     lea rcx, [rbx + 0x58]
00AA31FB  48 8B D6                        mov rdx, rsi
00AA31FE  E8 11 AF A0 FF                  call 0x1404ae114
00AA3203  8B 43 40                        mov eax, dword ptr [rbx + 0x40]
00AA3206  85 C0                           test eax, eax
00AA3208  74 09                           je 0x140aa3213
00AA320A  8B C8                           mov ecx, eax
00AA320C  E8 B3 1E FD FF                  call 0x140a750c4
00AA3211  EB 02                           jmp 0x140aa3215
00AA3213  33 C0                           xor eax, eax
00AA3215  4C 8B F8                        mov r15, rax
00AA3218  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00AA321D  49 C1 EF 0C                     shr r15, 0xc
00AA3221  F7 87 B8 00 00 00 00 40 00 00   test dword ptr [rdi + 0xb8], 0x4000
00AA322B  44 88 A5 80 00 00 00            mov byte ptr [rbp + 0x80], r12b
00AA3232  0F 84 EC 00 00 00               je 0x140aa3324
00AA3238  4D 8B C7                        mov r8, r15
00AA323B  48 8D 4B 58                     lea rcx, [rbx + 0x58]
00AA323F  49 C1 E0 0C                     shl r8, 0xc
00AA3243  48 8B D6                        mov rdx, rsi
00AA3246  E8 35 AA 02 00                  call 0x140acdc80
00AA324B  4C 8B A5 90 00 00 00            mov r12, qword ptr [rbp + 0x90]
00AA3252  4D 85 ED                        test r13, r13
00AA3255  74 26                           je 0x140aa327d
00AA3257  F7 87 B8 00 00 00 00 04 00 00   test dword ptr [rdi + 0xb8], 0x400
00AA3261  74 1A                           je 0x140aa327d
00AA3263  48 8D 97 A0 00 00 00            lea rdx, [rdi + 0xa0]
00AA326A  4C 89 65 90                     mov qword ptr [rbp - 0x70], r12
00AA326E  41 B8 04 00 00 00               mov r8d, 4
00AA3274  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00AA3278  E8 F3 F2 83 FF                  call 0x1402e2570
00AA327D  48 8B CB                        mov rcx, rbx
00AA3280  E8 67 CD FF FF                  call 0x140a9ffec
00AA3285  48 8B 95 98 00 00 00            mov rdx, qword ptr [rbp + 0x98]
00AA328C  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00AA3291  48 8B 8D 88 00 00 00            mov rcx, qword ptr [rbp + 0x88]
00AA3298  45 33 C9                        xor r9d, r9d
00AA329B  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AA32A0  4D 8B C4                        mov r8, r12
00AA32A3  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00AA32A9  C7 44 24 28 20 00 00 00         mov dword ptr [rsp + 0x28], 0x20
00AA32B1  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00AA32B7  E8 14 E9 79 FF                  call 0x140241bd0
00AA32BC  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
00AA32C0  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
00AA32C5  41 2B C4                        sub eax, r12d
00AA32C8  F0 01 05 A5 A6 38 00            lock add dword ptr [rip + 0x38a6a5], eax
00AA32CF  48 8B CB                        mov rcx, rbx
00AA32D2  E8 01 1A C6 FF                  call 0x140704cd8
00AA32D7  85 C0                           test eax, eax
00AA32D9  74 05                           je 0x140aa32e0
00AA32DB  E8 3C CC 00 00                  call 0x140aaff1c
00AA32E0  4D 85 ED                        test r13, r13
00AA32E3  75 2D                           jne 0x140aa3312
00AA32E5  E8 F6 FC 77 FF                  call 0x140222fe0
00AA32EA  85 C0                           test eax, eax
00AA32EC  75 1D                           jne 0x140aa330b
00AA32EE  48 8B 85 98 00 00 00            mov rax, qword ptr [rbp + 0x98]
00AA32F5  49 8B D7                        mov rdx, r15
00AA32F8  48 8B 8D 88 00 00 00            mov rcx, qword ptr [rbp + 0x88]
00AA32FF  48 2B D0                        sub rdx, rax
00AA3302  48 8D 0C C1                     lea rcx, [rcx + rax*8]
00AA3306  E8 6D 46 BF FF                  call 0x140697978
00AA330B  C6 85 80 00 00 00 01            mov byte ptr [rbp + 0x80], 1
00AA3312  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00AA3317  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
00AA331C  48 8B CB                        mov rcx, rbx
00AA331F  E8 C4 38 00 00                  call 0x140aa6be8
00AA3324  F7 87 B8 00 00 00 00 04 00 00   test dword ptr [rdi + 0xb8], 0x400
00AA332E  48 8B CB                        mov rcx, rbx
00AA3331  74 51                           je 0x140aa3384
00AA3333  E8 90 E0 BC FF                  call 0x1406713c8
00AA3338  8B 05 C2 37 52 00               mov eax, dword ptr [rip + 0x5237c2]
00AA333E  A8 04                           test al, 4
00AA3340  74 54                           je 0x140aa3396
00AA3342  83 64 24 40 00                  and dword ptr [rsp + 0x40], 0
00AA3347  48 8D 4B 48                     lea rcx, [rbx + 0x48]
00AA334B  44 0F B7 43 6E                  movzx r8d, word ptr [rbx + 0x6e]
00AA3350  4C 8B CE                        mov r9, rsi
00AA3353  8B 53 40                        mov edx, dword ptr [rbx + 0x40]
00AA3356  41 8B C0                        mov eax, r8d
00AA3359  C1 E8 04                        shr eax, 4
00AA335C  41 83 E0 0F                     and r8d, 0xf
00AA3360  83 E0 07                        and eax, 7
00AA3363  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00AA3367  8B 43 78                        mov eax, dword ptr [rbx + 0x78]
00AA336A  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
00AA336F  45 33 C0                        xor r8d, r8d
00AA3372  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00AA3376  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00AA337B  33 D2                           xor edx, edx
00AA337D  E8 EA ED F7 FF                  call 0x140a2216c
00AA3382  EB 12                           jmp 0x140aa3396
00AA3384  44 8B 43 40                     mov r8d, dword ptr [rbx + 0x40]
00AA3388  41 B9 03 00 00 00               mov r9d, 3
00AA338E  48 8B D6                        mov rdx, rsi
00AA3391  E8 46 E5 98 FF                  call 0x1404318dc
00AA3396  4D 85 ED                        test r13, r13
00AA3399  74 0C                           je 0x140aa33a7
00AA339B  F7 87 B8 00 00 00 00 00 08 00   test dword ptr [rdi + 0xb8], 0x80000
00AA33A5  74 19                           je 0x140aa33c0
00AA33A7  4C 8B A5 88 00 00 00            mov r12, qword ptr [rbp + 0x88]
00AA33AE  4D 85 FF                        test r15, r15
00AA33B1  74 14                           je 0x140aa33c7
00AA33B3  41 8B D7                        mov edx, r15d
00AA33B6  49 8B CC                        mov rcx, r12
00AA33B9  E8 A6 5E D5 FF                  call 0x1407f9264
00AA33BE  EB 07                           jmp 0x140aa33c7
00AA33C0  4C 8B A5 88 00 00 00            mov r12, qword ptr [rbp + 0x88]
00AA33C7  80 BD 80 00 00 00 00            cmp byte ptr [rbp + 0x80], 0
00AA33CE  74 0B                           je 0x140aa33db
00AA33D0  41 8B D7                        mov edx, r15d
00AA33D3  49 8B CC                        mov rcx, r12
00AA33D6  E8 D9 BD FD FF                  call 0x140a7f1b4
00AA33DB  8B 87 B8 00 00 00               mov eax, dword ptr [rdi + 0xb8]
00AA33E1  A8 01                           test al, 1
00AA33E3  74 0B                           je 0x140aa33f0
00AA33E5  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
00AA33E9  33 D2                           xor edx, edx
00AA33EB  E8 80 F4 0D 00                  call 0x140b82870
00AA33F0  4D 85 ED                        test r13, r13
00AA33F3  74 77                           je 0x140aa346c
00AA33F5  48 8B 97 C0 00 00 00            mov rdx, qword ptr [rdi + 0xc0]
00AA33FC  48 85 D2                        test rdx, rdx
00AA33FF  74 0C                           je 0x140aa340d
00AA3401  48 8D 0D F8 58 39 00            lea rcx, [rip + 0x3958f8]
00AA3408  E8 83 34 7E FF                  call 0x140286890
00AA340D  4C 8B BD 90 00 00 00            mov r15, qword ptr [rbp + 0x90]
00AA3414  48 85 F6                        test rsi, rsi
00AA3417  74 1E                           je 0x140aa3437
00AA3419  49 8B 07                        mov rax, qword ptr [r15]
00AA341C  48 3B 70 20                     cmp rsi, qword ptr [rax + 0x20]
00AA3420  74 15                           je 0x140aa3437
00AA3422  48 8B CE                        mov rcx, rsi
00AA3425  E8 2A 5B A1 FF                  call 0x1404b8f54
00AA342A  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00AA342F  48 8B CE                        mov rcx, rsi
00AA3432  E8 59 BD FD FF                  call 0x140a7f190
00AA3437  F7 87 B8 00 00 00 00 08 00 00   test dword ptr [rdi + 0xb8], 0x800
00AA3441  74 08                           je 0x140aa344b
00AA3443  49 8B CF                        mov rcx, r15
00AA3446  E8 39 2D A3 FF                  call 0x1404d6184
00AA344B  F7 87 B8 00 00 00 00 00 08 00   test dword ptr [rdi + 0xb8], 0x80000
00AA3455  74 08                           je 0x140aa345f
00AA3457  49 8B CF                        mov rcx, r15
00AA345A  E8 C1 65 9D FF                  call 0x140479a20
00AA345F  BA 4D 6D 53 63                  mov edx, 0x63536d4d
00AA3464  49 8B CD                        mov rcx, r13
00AA3467  E8 34 0A 7C FF                  call 0x140263ea0
00AA346C  4D 85 F6                        test r14, r14
00AA346F  74 08                           je 0x140aa3479
00AA3471  49 8B CE                        mov rcx, r14
00AA3474  E8 57 02 A3 FF                  call 0x1404d36d0
00AA3479  33 D2                           xor edx, edx
00AA347B  48 8B CB                        mov rcx, rbx
00AA347E  E8 ED F3 0D 00                  call 0x140b82870
00AA3483  48 81 C4 38 01 00 00            add rsp, 0x138
00AA348A  41 5F                           pop r15
00AA348C  41 5E                           pop r14
00AA348E  41 5D                           pop r13
00AA3490  41 5C                           pop r12
00AA3492  5F                              pop rdi
00AA3493  5E                              pop rsi
00AA3494  5B                              pop rbx
00AA3495  5D                              pop rbp
00AA3496  C3                              ret
00AA3497  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUnloadSystemImage(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_rsp = (v_rsp) - (312);
    a2 = 0;
    result = memset(v_stack_mE8, a2, 152, a4);
    result = 0;
    v_stack_mF0 = 0;
    v_stack_m120 = v_xmm0;
    v_stack_m110 = v_xmm0;
    v_stack_m100 = v_xmm0;
    result = MiGetBaseLoaderPortion(a1, a2, 152, a4);
    v_r12 = 0;
    if (((*(unsigned int *)(result + 184)) & (256)) == 0) goto loc_00AA3038;
    goto loc_00AA3045;
loc_00AA3038:
    result = MiAcquireLoadLock(1, a2, 152, a4);
loc_00AA3045:
    if ((*(unsigned __int64 *)(a1 + 136)) != 1) goto loc_00AA3068;
loc_00AA3052:
    if (result == 0) goto loc_00AA3483;
    result = MmReleaseLoadLock(result, a2, 152, a4);
    goto loc_00AA3483;
loc_00AA3068:
    if (result != 0) goto loc_00AA3052;
    *(unsigned int *)(result + 184) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 184)));
    if (*(unsigned __int64 *)(a1 + 112) == 0) goto loc_00AA30A0;
    result = MiSectionControlArea(*(unsigned __int64 *)(a1 + 112), a2, (unsigned int)(*(unsigned int *)(result + 184)), a4);
    v_stack_p18 = result;
    goto loc_00AA30A7;
loc_00AA30A0:
    v_stack_p18 = 0;
loc_00AA30A7:
    if (*(unsigned __int64 *)(a1 + 48) == 0) goto loc_00AA30C1;
    result = MiGetPteAddress(*(unsigned __int64 *)(a1 + 48), a2, (unsigned int)(*(unsigned int *)(result + 184)), a4);
    v_stack_p10 = result;
    goto loc_00AA30C8;
loc_00AA30C1:
    v_stack_p10 = 0;
loc_00AA30C8:
    result = ((unsigned int)(*(unsigned int *)(a1 + 64))) >> (12);
    v_stack_p20 = result;
    if (!(condition_is_above_or_equal)) {
        a1 = a1;
        result = KeCleanupImageTracepoints(a1, a2, (unsigned int)(*(unsigned int *)(result + 184)), a4);
    }
    if (((*(unsigned int *)(result + 184)) & (0x80000ULL)) != 0) goto loc_00AA30F6;
    if (*(unsigned __int64 *)(a1 + 112) != 0) goto loc_00AA3121;
loc_00AA30F6:
    a2 = 0;
    result = MiMarkKernelImageCfgBits(a1, a2, (unsigned int)(*(unsigned int *)(result + 184)), a4);
    if (sign_flag) {
        a4 = a1;
        a3 = *(unsigned __int64 *)(a1 + 48);
        v_stack_m158 = result;
        a2 = 0x1015ULL;
        a1 = 26;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (((*(unsigned int *)(result + 184)) & (0x40000ULL)) == 0) goto loc_00AA3172;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3753081))) + (*(unsigned int *)(v_rip + 3753079)));
    if (!(condition_is_equal)) {
        a1 = a1;
        result = MiClearDriverTablePtes(a1, a2, a3, a4);
    }
    result = MiUnmapKernelScp(a1, a2, a3, a4);
    result = KeIsRetpolineEnabled(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AA3172;
    a2 = 0;
    result = MiMarkKernelImageRetpolineBits(a1, a2, a3, a4);
    result = MiIsImageFullyRetpolined(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) {
        result = KeFlushRsb(a1, a2, a3, a4);
    }
loc_00AA3172:
    if (*(unsigned __int64 *)(result + 280) != 0) {
        result = MiFreeRetpolineRelocationInformation(*(unsigned __int64 *)(result + 280), a2, a3, a4);
        *(unsigned __int64 *)(result + 280) = 0;
    }
    if (((*(unsigned int *)(result + 184)) & (0x8000ULL)) == 0) goto loc_00AA31B2;
    result = VfDriverUnloadImage(a1, a2, a3, a4);
    if (((*(unsigned int *)(result + 184)) & (0x10000ULL)) != 0) {
        a1 = a1;
        result = KseDriverUnloadImage(a1, a2, a3, a4);
    }
    if (((*(unsigned int *)(result + 184)) & (0x20000ULL)) != 0) {
        a1 = a1;
        result = KasanDriverUnloadImage(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(a1 + 136) != 0) {
        a1 = *(unsigned __int64 *)(a1 + 136);
        result = MiDereferenceImports(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(a1 + 136);
        result = MiFreeLoadedImportList(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(a1 + 48) != 0) {
        a1 = *(unsigned __int64 *)(a1 + 48);
        result = LdrUnloadAlternateResourceModule(a1, a2, a3, a4);
    }
    if (((*(unsigned int *)(a1 + 104)) & (0x100000ULL)) != 0) {
        a3 = 0xFFFFFFFFULL;
        a1 = a1 + 88;
        a2 = *(unsigned __int64 *)(a1 + 48);
        result = DbgUnLoadImageSymbolsUnicode(a1, a2, a3, a4);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64))) == 0) goto loc_00AA3213;
    result = MiBytesToMapSystemImage((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64)))), a2, a3, a4);
    goto loc_00AA3215;
loc_00AA3213:
    result = 0;
loc_00AA3215:
    v_stack_m128 = 0;
    v_r15 = (0) >> (12);
    v_stack_p8 = 0;
    if (((*(unsigned int *)(result + 184)) & (0x4000ULL)) == 0) goto loc_00AA3324;
    a3 = (v_r15) << (12);
    result = MiRememberUnloadedDriver(a1 + 88, *(unsigned __int64 *)(a1 + 48), a3, a4);
    if (*(unsigned __int64 *)(a1 + 112) == 0) goto loc_00AA327D;
    if (((*(unsigned int *)(result + 184)) & (0x400ULL)) != 0) {
        a2 = result + 160;
        v_stack_mE8 = v_stack_p18;
        a3 = 4;
        a1 = v_stack_mE8;
        result = MiManageSubsectionView(a1, a2, a3, a4);
    }
    result = MiUnlockDriverCode(a1, a2, a3, a4);
    a4 = 0;
    v_stack_m140 = v_stack_m120;
    v_stack_m150 = 32;
    result = MiDecommitPages(v_stack_p10, v_stack_p20, v_stack_p18, a4);
    result = (unsigned int)(((unsigned int)(v_stack_m120)) - ((unsigned int)(v_stack_m108)));
    result = MmHasImageBeenImportOptimized(a1, v_stack_p20, v_stack_p18, a4);
    if ((unsigned int)(result) != 0) {
        result = MiFreeRetpolineImportInfo(a1, v_stack_p20, v_stack_p18, a4);
    }
    if (*(unsigned __int64 *)(a1 + 112) != 0) goto loc_00AA3312;
    result = Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting(a1, v_stack_p20, v_stack_p18, a4);
    if ((unsigned int)(result) == 0) {
        result = v_stack_p20;
        a2 = v_r15;
        a1 = v_stack_p10;
        a2 = (a2) - (result);
        a1 = a1 + result * 8;
        result = MiUnloadSystemImageSoftWsles(a1, a2, v_stack_p18, a4);
    }
    v_stack_p8 = 1;
loc_00AA3312:
    v_stack_m120 = v_stack_m108;
    result = MiReturnSystemImageCommitment(a1, v_stack_m120, v_stack_p18, a4);
loc_00AA3324:
    if (((*(unsigned int *)(result + 184)) & (0x400ULL)) == 0) goto loc_00AA3384;
    result = MiRemoveLoaderEntry(a1, v_stack_m120, v_stack_p18, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5388226)))) & (4)) == 0) goto loc_00AA3396;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + 110)))) >> (4));
    a3 = (unsigned int)((*(unsigned __int16 *)(a1 + 110)) & (15));
    result = (unsigned int)((result) & (7));
    v_stack_m140 = (unsigned int)(result);
    v_stack_m148 = (unsigned int)(a3);
    a3 = 0;
    v_stack_m150 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 120)));
    v_stack_m158 = (unsigned int)(*(unsigned int *)(a1 + 64));
    a2 = 0;
    result = PerfLogImageUnload(a1 + 72, a2, a3, *(unsigned __int64 *)(a1 + 48));
    goto loc_00AA3396;
loc_00AA3384:
    result = MiUpdateDriverLoadInProgress(a1 + 72, *(unsigned __int64 *)(a1 + 48), (unsigned int)(*(unsigned int *)(a1 + 64)), 3);
loc_00AA3396:
    if (*(unsigned __int64 *)(a1 + 112) == 0) goto loc_00AA33A7;
    if (((*(unsigned int *)(result + 184)) & (0x80000ULL)) == 0) goto loc_00AA33C0;
loc_00AA33A7:
    if (v_r15 == 0) goto loc_00AA33C7;
    result = MiReleasePrivilegedPtes(v_stack_p10, (unsigned int)((unsigned int)(v_r15)), (unsigned int)(*(unsigned int *)(a1 + 64)), 3);
    goto loc_00AA33C7;
loc_00AA33C0:
loc_00AA33C7:
    if (v_stack_p8 != 0) {
        a2 = (unsigned int)(v_r15);
        a1 = v_stack_p10;
        result = MiReleaseDriverPtes(a1, a2, (unsigned int)(*(unsigned int *)(a1 + 64)), 3);
    }
    result = (unsigned int)(*(unsigned int *)(result + 184));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 184)))) & (1)) != 0) {
        a1 = *(unsigned __int64 *)(a1 + 80);
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(*(unsigned int *)(a1 + 64)), 3);
    }
    if (*(unsigned __int64 *)(a1 + 112) == 0) goto loc_00AA346C;
    if (*(unsigned __int64 *)(result + 192) != 0) {
        a1 = v_rip + 3758328;
        result = MiReturnResident(a1, *(unsigned __int64 *)(result + 192), (unsigned int)(*(unsigned int *)(a1 + 64)), 3);
    }
    if (*(unsigned __int64 *)(a1 + 48) == 0) goto loc_00AA3437;
    result = *(unsigned __int64 *)(v_stack_p18);
    if ((*(unsigned __int64 *)(a1 + 48)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p18) + 32))) {
        a1 = *(unsigned __int64 *)(a1 + 48);
        result = MiFreePrivateFixupEntryForSystemImage(a1, *(unsigned __int64 *)(result + 192), (unsigned int)(*(unsigned int *)(a1 + 64)), 3);
        a2 = v_stack_m128;
        a1 = *(unsigned __int64 *)(a1 + 48);
        result = MiReturnSystemImageAddress(a1, a2, (unsigned int)(*(unsigned int *)(a1 + 64)), 3);
    }
    if (((*(unsigned int *)(result + 184)) & (0x800ULL)) != 0) {
        a1 = v_stack_p18;
        result = MiReturnCrossPartitionControlAreaCharges(a1, a2, (unsigned int)(*(unsigned int *)(a1 + 64)), 3);
    }
    if (((*(unsigned int *)(result + 184)) & (0x80000ULL)) != 0) {
        a1 = v_stack_p18;
        result = MiDereferenceControlArea(a1, a2, (unsigned int)(*(unsigned int *)(a1 + 64)), 3);
    }
    result = ObDereferenceObjectDeferDeleteWithTag(*(unsigned __int64 *)(a1 + 112), (unsigned int)(0x63536D4DULL), (unsigned int)(*(unsigned int *)(a1 + 64)), 3);
loc_00AA346C:
    if (result != 0) {
        a1 = result;
        result = MmReleaseLoadLock(a1, (unsigned int)(0x63536D4DULL), (unsigned int)(*(unsigned int *)(a1 + 64)), 3);
    }
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, (unsigned int)(*(unsigned int *)(a1 + 64)), 3);
loc_00AA3483:
    v_rsp = (v_rsp) + (312);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiUnloadSystemImage(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m78;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p8;

    local_rsp = (local_rsp) - (312);
    Arg2 = 0;
    result = memset(v_stack_mE8, Arg2, 152, a4);
    result = 0;
    v_stack_mF0 = 0;
    v_stack_m120 = v_xmm0;
    v_stack_m110 = v_xmm0;
    v_stack_m100 = v_xmm0;
    result = MiGetBaseLoaderPortion(Arg1, Arg2, 152, a4);
    local_r12 = 0;
    if (((*(uint32_t *)(result + 0xB8)) & (256)) == 0) goto loc_00AA3038;
    goto loc_00AA3045;
loc_00AA3038:
    result = MiAcquireLoadLock(1, Arg2, 152, a4);
loc_00AA3045:
    if ((*(uint64_t *)(arg1 + 0x88)) != 1) goto loc_00AA3068;
loc_00AA3052:
    if (result == 0) goto loc_00AA3483;
    result = MmReleaseLoadLock(result, Arg2, 152, a4);
    goto loc_00AA3483;
loc_00AA3068:
    if (result != 0) goto loc_00AA3052;
    *(uint32_t *)(result + 0xB8) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0xB8)));
    if (*(uint64_t *)(arg1 + 0x70) == 0) goto loc_00AA30A0;
    result = MiSectionControlArea(*(uint64_t *)(arg1 + 0x70), Arg2, (uint32_t)(*(uint32_t *)(result + 0xB8)), a4);
    v_stack_p18 = result;
    goto loc_00AA30A7;
loc_00AA30A0:
    v_stack_p18 = 0;
loc_00AA30A7:
    if (*(uint64_t *)(arg1 + 0x30) == 0) goto loc_00AA30C1;
    result = MiGetPteAddress(*(uint64_t *)(arg1 + 0x30), Arg2, (uint32_t)(*(uint32_t *)(result + 0xB8)), a4);
    v_stack_p10 = result;
    goto loc_00AA30C8;
loc_00AA30C1:
    v_stack_p10 = 0;
loc_00AA30C8:
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x40))) >> (12);
    v_stack_p20 = result;
    if (!(condition_is_above_or_equal)) {
        Arg1 = Arg1;
        result = KeCleanupImageTracepoints(Arg1, Arg2, (uint32_t)(*(uint32_t *)(result + 0xB8)), a4);
    }
    if (((*(uint32_t *)(result + 0xB8)) & (0x80000ULL)) != 0) goto loc_00AA30F6;
    if (*(uint64_t *)(arg1 + 0x70) != 0) goto loc_00AA3121;
loc_00AA30F6:
    Arg2 = 0;
    result = MiMarkKernelImageCfgBits(Arg1, Arg2, (uint32_t)(*(uint32_t *)(result + 0xB8)), a4);
    if (sign_flag) {
        a4 = Arg1;
        a3 = *(uint64_t *)(arg1 + 0x30);
        v_stack_m158 = result;
        Arg2 = 0x1015ULL;
        Arg1 = 26;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    if (((*(uint32_t *)(result + 0xB8)) & (0x40000ULL)) == 0) goto loc_00AA3172;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x394479))) + (*(uint32_t *)(v_rip + 0x394477)));
    if (!(condition_is_equal)) {
        Arg1 = Arg1;
        result = MiClearDriverTablePtes(Arg1, Arg2, a3, a4);
    }
    result = MiUnmapKernelScp(Arg1, Arg2, a3, a4);
    result = KeIsRetpolineEnabled(Arg1, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00AA3172;
    Arg2 = 0;
    result = MiMarkKernelImageRetpolineBits(Arg1, Arg2, a3, a4);
    result = MiIsImageFullyRetpolined(Arg1, Arg2, a3, a4);
    if ((uint32_t)(result) != 0) {
        result = KeFlushRsb(Arg1, Arg2, a3, a4);
    }
loc_00AA3172:
    if (*(uint64_t *)(result + 0x118) != 0) {
        result = MiFreeRetpolineRelocationInformation(*(uint64_t *)(result + 0x118), Arg2, a3, a4);
        *(uint64_t *)(result + 0x118) = 0;
    }
    if (((*(uint32_t *)(result + 0xB8)) & (0x8000ULL)) == 0) goto loc_00AA31B2;
    result = VfDriverUnloadImage(Arg1, Arg2, a3, a4);
    if (((*(uint32_t *)(result + 0xB8)) & (0x10000ULL)) != 0) {
        Arg1 = Arg1;
        result = KseDriverUnloadImage(Arg1, Arg2, a3, a4);
    }
    if (((*(uint32_t *)(result + 0xB8)) & (0x20000ULL)) != 0) {
        Arg1 = Arg1;
        result = KasanDriverUnloadImage(Arg1, Arg2, a3, a4);
    }
    if (*(uint64_t *)(arg1 + 0x88) != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x88);
        result = MiDereferenceImports(Arg1, Arg2, a3, a4);
        Arg1 = *(uint64_t *)(arg1 + 0x88);
        result = MiFreeLoadedImportList(Arg1, Arg2, a3, a4);
    }
    if (*(uint64_t *)(arg1 + 0x30) != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x30);
        result = LdrUnloadAlternateResourceModule(Arg1, Arg2, a3, a4);
    }
    if (((*(uint32_t *)(arg1 + 0x68)) & (0x100000ULL)) != 0) {
        a3 = 0xFFFFFFFFULL;
        Arg1 = Arg1 + 88;
        Arg2 = *(uint64_t *)(arg1 + 0x30);
        result = DbgUnLoadImageSymbolsUnicode(Arg1, Arg2, a3, a4);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40))) == 0) goto loc_00AA3213;
    result = MiBytesToMapSystemImage((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40)))), Arg2, a3, a4);
    goto loc_00AA3215;
loc_00AA3213:
    result = 0;
loc_00AA3215:
    v_stack_m128 = 0;
    local_r15 = (0) >> (12);
    v_stack_p8 = 0;
    if (((*(uint32_t *)(result + 0xB8)) & (0x4000ULL)) == 0) goto loc_00AA3324;
    a3 = (local_r15) << (12);
    result = MiRememberUnloadedDriver(Arg1 + 88, *(uint64_t *)(arg1 + 0x30), a3, a4);
    if (*(uint64_t *)(arg1 + 0x70) == 0) goto loc_00AA327D;
    if (((*(uint32_t *)(result + 0xB8)) & (0x400ULL)) != 0) {
        Arg2 = result + 160;
        v_stack_mE8 = v_stack_p18;
        a3 = 4;
        Arg1 = v_stack_mE8;
        result = MiManageSubsectionView(Arg1, Arg2, a3, a4);
    }
    result = MiUnlockDriverCode(Arg1, Arg2, a3, a4);
    a4 = 0;
    v_stack_m140 = v_stack_m120;
    v_stack_m150 = 32;
    result = MiDecommitPages(v_stack_p10, v_stack_p20, v_stack_p18, a4);
    result = (uint32_t)(((uint32_t)(v_stack_m120)) - ((uint32_t)(v_stack_m108)));
    result = MmHasImageBeenImportOptimized(Arg1, v_stack_p20, v_stack_p18, a4);
    if ((uint32_t)(result) != 0) {
        result = MiFreeRetpolineImportInfo(Arg1, v_stack_p20, v_stack_p18, a4);
    }
    if (*(uint64_t *)(arg1 + 0x70) != 0) goto loc_00AA3312;
    result = Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting(Arg1, v_stack_p20, v_stack_p18, a4);
    if ((uint32_t)(result) == 0) {
        result = v_stack_p20;
        Arg2 = local_r15;
        Arg1 = v_stack_p10;
        Arg2 = (Arg2) - (result);
        Arg1 = Arg1 + result * 8;
        result = MiUnloadSystemImageSoftWsles(Arg1, Arg2, v_stack_p18, a4);
    }
    v_stack_p8 = 1;
loc_00AA3312:
    v_stack_m120 = v_stack_m108;
    result = MiReturnSystemImageCommitment(Arg1, v_stack_m120, v_stack_p18, a4);
loc_00AA3324:
    if (((*(uint32_t *)(result + 0xB8)) & (0x400ULL)) == 0) goto loc_00AA3384;
    result = MiRemoveLoaderEntry(Arg1, v_stack_m120, v_stack_p18, a4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5237C2)))) & (4)) == 0) goto loc_00AA3396;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(arg1 + 0x6E)))) >> (4));
    a3 = (uint32_t)((*(uint16_t *)(arg1 + 0x6E)) & (15));
    result = (uint32_t)((result) & (7));
    v_stack_m140 = (uint32_t)(result);
    v_stack_m148 = (uint32_t)(a3);
    a3 = 0;
    v_stack_m150 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x78)));
    v_stack_m158 = (uint32_t)(*(uint32_t *)(arg1 + 0x40));
    Arg2 = 0;
    result = PerfLogImageUnload(Arg1 + 72, Arg2, a3, *(uint64_t *)(arg1 + 0x30));
    goto loc_00AA3396;
loc_00AA3384:
    result = MiUpdateDriverLoadInProgress(Arg1 + 72, *(uint64_t *)(arg1 + 0x30), (uint32_t)(*(uint32_t *)(arg1 + 0x40)), 3);
loc_00AA3396:
    if (*(uint64_t *)(arg1 + 0x70) == 0) goto loc_00AA33A7;
    if (((*(uint32_t *)(result + 0xB8)) & (0x80000ULL)) == 0) goto loc_00AA33C0;
loc_00AA33A7:
    if (local_r15 == 0) goto loc_00AA33C7;
    result = MiReleasePrivilegedPtes(v_stack_p10, (uint32_t)((uint32_t)(local_r15)), (uint32_t)(*(uint32_t *)(arg1 + 0x40)), 3);
    goto loc_00AA33C7;
loc_00AA33C0:
loc_00AA33C7:
    if (v_stack_p8 != 0) {
        Arg2 = (uint32_t)(local_r15);
        Arg1 = v_stack_p10;
        result = MiReleaseDriverPtes(Arg1, Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x40)), 3);
    }
    result = (uint32_t)(*(uint32_t *)(result + 0xB8));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xB8)))) & (1)) != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x50);
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x40)), 3);
    }
    if (*(uint64_t *)(arg1 + 0x70) == 0) goto loc_00AA346C;
    if (*(uint64_t *)(result + 0xC0) != 0) {
        Arg1 = v_rip + 3758328;
        result = MiReturnResident(Arg1, *(uint64_t *)(result + 0xC0), (uint32_t)(*(uint32_t *)(arg1 + 0x40)), 3);
    }
    if (*(uint64_t *)(arg1 + 0x30) == 0) goto loc_00AA3437;
    result = *(uint64_t *)(v_stack_p18);
    if ((*(uint64_t *)(arg1 + 0x30)) != (*(uint64_t *)(*(uint64_t *)(v_stack_p18) + 0x20))) {
        Arg1 = *(uint64_t *)(arg1 + 0x30);
        result = MiFreePrivateFixupEntryForSystemImage(Arg1, *(uint64_t *)(result + 0xC0), (uint32_t)(*(uint32_t *)(arg1 + 0x40)), 3);
        Arg2 = v_stack_m128;
        Arg1 = *(uint64_t *)(arg1 + 0x30);
        result = MiReturnSystemImageAddress(Arg1, Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x40)), 3);
    }
    if (((*(uint32_t *)(result + 0xB8)) & (0x800ULL)) != 0) {
        Arg1 = v_stack_p18;
        result = MiReturnCrossPartitionControlAreaCharges(Arg1, Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x40)), 3);
    }
    if (((*(uint32_t *)(result + 0xB8)) & (0x80000ULL)) != 0) {
        Arg1 = v_stack_p18;
        result = MiDereferenceControlArea(Arg1, Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x40)), 3);
    }
    result = ObDereferenceObjectDeferDeleteWithTag(*(uint64_t *)(arg1 + 0x70), (uint32_t)(0x63536D4DULL), (uint32_t)(*(uint32_t *)(arg1 + 0x40)), 3);
loc_00AA346C:
    if (result != 0) {
        Arg1 = result;
        result = MmReleaseLoadLock(Arg1, (uint32_t)(0x63536D4DULL), (uint32_t)(*(uint32_t *)(arg1 + 0x40)), 3);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x40)), 3);
loc_00AA3483:
    local_rsp = (local_rsp) + (312);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x68` | `32` | `R` |
| `Arg1` | `+ 0x6C` | `16` | `R/W` |
| `Arg1` | `+ 0x6E` | `16` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x78` | `32` | `R` |
| `Arg1` | `+ 0x88` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA2FD4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
