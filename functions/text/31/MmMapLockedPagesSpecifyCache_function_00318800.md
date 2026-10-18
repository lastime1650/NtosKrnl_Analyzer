# MmMapLockedPagesSpecifyCache

- RVA: `0x00318800`–`0x00318D18` (길이 `1,304` bytes)
- VA: `0x0000000140318800`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00074C2C`
- 디코드: `303`개 명령, `1,304/1,304` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **75**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00318895` → [MiReservePtes](MiReservePtes_function_00318D20.md) (function, `0x00318D20`)
- `0x00318929` → [MiFillSystemPtes](MiFillSystemPtes_function_00319850.md) (function, `0x00319850`)
- `0x00318B77` → [MiReleasePtes](../24/MiReleasePtes_function_00247240.md) (function, `0x00247240`)
- `0x00318C28` → [MiIssueNoPtesBugcheck](../4F/MiIssueNoPtesBugcheck_function_004F6B9C.md) (function, `0x004F6B9C`)
- `0x00318C86` → [MiCheckLinearProtectedPteAccessedBit](../29/MiCheckLinearProtectedPteAccessedBit_function_00292D80.md) (function, `0x00292D80`)
- `0x00318CA1` → [MiMapLockedPagesInUserSpace](../../page/97/MiMapLockedPagesInUserSpace_function_0097FE04.md) (function, `0x0097FE04`)
- `0x00318CE9` → [MiIssueNoPtesBugcheck](../4F/MiIssueNoPtesBugcheck_function_004F6B9C.md) (function, `0x004F6B9C`)

### Direct callers
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmIoCtxWorkItemComplete](../20/SMKM_STORE_MGR_SM_TRAITS_SmIoCtxWorkItemComplete_function_00205850.md) at `0x0020597D`
- [sub_00205FE2](../20/Unknown_function_00205FE2.md) at `0x00206040`
- [MiGetWorkingSetInfo](../29/MiGetWorkingSetInfo_function_0029E498.md) at `0x0029E615`
- [MiInitializeImageProtos](../2A/MiInitializeImageProtos_function_002ABDAC.md) at `0x002AC0AB`
- [MiGetWorkingSetInfoList](../2A/MiGetWorkingSetInfoList_function_002AF770.md) at `0x002B0A98`
- [MiStoreWriteModifiedPages](../2B/MiStoreWriteModifiedPages_function_002B46C4.md) at `0x002B52A8`
- [SmFpAllocate](SmFpAllocate_function_00317D10.md) at `0x00317DB9`
- [ST_STORE&lt;SM_TRAITS&gt;::StDmSinglePageTransfer](ST_STORE_SM_TRAITS_StDmSinglePageTransfer_function_00317E50.md) at `0x00317F2B`
- [SmMapPage](SmMapPage_function_003187A0.md) at `0x003187E9`
- [MiValidateInPage](../38/MiValidateInPage_function_00382E0C.md) at `0x00383313`
- [CcLockSystemCacheBuffer](../3C/CcLockSystemCacheBuffer_function_003CC5B8.md) at `0x003CC66B`
- [HalpDmaFlushBuffer](../3D/HalpDmaFlushBuffer_function_003DC1DC.md) at `0x003DC31A`
- [sub_003DF1AF](../3D/Unknown_function_003DF1AF.md) at `0x003DF1C7`
- [PspIumFreePhysicalPages](../3E/PspIumFreePhysicalPages_function_003E7874.md) at `0x003E78DC`
- [HalpAllocateCommonBufferVectorInternal](../3E/HalpAllocateCommonBufferVectorInternal_function_003E848C.md) at `0x003E860C`
- [HalpAllocateDomainCommonBufferInternal](../3E/HalpAllocateDomainCommonBufferInternal_function_003E8B64.md) at `0x003E8E30`
- [HalpAllocateCommonBufferDmarThin](../3E/HalpAllocateCommonBufferDmarThin_function_003E8FF0.md) at `0x003E9105`
- [EtwpAllocatePartitionMemory](../3E/EtwpAllocatePartitionMemory_function_003EB12C.md) at `0x003EB18D`
- [MiPersistMdl](../40/MiPersistMdl_function_00402B2C.md) at `0x00402B8F`
- [sub_004201AA](../42/Unknown_function_004201AA.md) at `0x00420433`
- [CcCompleteAsyncRead](../45/CcCompleteAsyncRead_function_0045E7DC.md) at `0x0045E963`
- [MiTransferMemoryPagefileData](../4D/MiTransferMemoryPagefileData_function_004DB6FC.md) at `0x004DB759`
- [FsRtlCancelNotify](../4E/FsRtlCancelNotify_function_004E7F90.md) at `0x004E80DA`
- [FsRtlCancelNotify](../4E/FsRtlCancelNotify_function_004E7F90.md) at `0x004E8176`
- [HalInitializeBios](../53/HalInitializeBios_function_0053D9A0.md) at `0x0053DB9F`
- [HalCreateCommonBufferFromMdl](../55/HalCreateCommonBufferFromMdl_function_00551680.md) at `0x005519A8`
- [HalCreateCommonBufferFromMdlDmaThin](../55/HalCreateCommonBufferFromMdlDmaThin_function_00552800.md) at `0x00552A99`
- [HalCreateCommonBufferFromMdlDmarThin](../55/HalCreateCommonBufferFromMdlDmarThin_function_00552DA0.md) at `0x00552F14`
- [IopLiveDumpAllocateFromIOSpace](../59/IopLiveDumpAllocateFromIOSpace_function_00599DEC.md) at `0x0059A0D6`
- [IopLiveDumpAllocateFromVMMemoryPartition](../59/IopLiveDumpAllocateFromVMMemoryPartition_function_0059A2D8.md) at `0x0059A4AE`
- [KiOpPatchCode](../5C/KiOpPatchCode_function_005C6900.md) at `0x005C6A32`
- [PspIumAllocatePhysicalPages](../5E/PspIumAllocatePhysicalPages_function_005E4574.md) at `0x005E461E`
- [PspIumAllocateSecurePool](../5E/PspIumAllocateSecurePool_function_005E4698.md) at `0x005E480C`
- [SmRecordDecompressionFailureDumpPayload](../61/SmRecordDecompressionFailureDumpPayload_function_00611120.md) at `0x00611229`
- [MdlInvariantPostProcessing1](../61/MdlInvariantPostProcessing1_function_00613AE0.md) at `0x00613BAD`
- [MdlInvariantPreProcessing1](../61/MdlInvariantPreProcessing1_function_00613CEC.md) at `0x00613D84`
- [DifMmMapLockedPagesSpecifyCacheWrapper](../63/DifMmMapLockedPagesSpecifyCacheWrapper_function_00635D60.md) at `0x00635E6F`
- [DifMmMapLockedPagesWrapper](../63/DifMmMapLockedPagesWrapper_function_00635F10.md) at `0x00635FFA`
- [MmMapLockedPages](../67/MmMapLockedPages_function_00674BB0.md) at `0x00674BCA`
- [MiLockPatchIatForDV](../68/MiLockPatchIatForDV_function_00682050.md) at `0x006821E4`
- [MiReapplyImportOptimizationForDriverVerifier](../68/MiReapplyImportOptimizationForDriverVerifier_function_00682268.md) at `0x006823C6`
- [sub_006E9A0A](../6E/Unknown_function_006E9A0A.md) at `0x006E9A33`
- [sub_006E9F12](../6E/Unknown_function_006E9F12.md) at `0x006E9F85`
- [sub_006EA56C](../6E/Unknown_function_006EA56C.md) at `0x006EA5E3`
- [sub_006EA972](../6E/Unknown_function_006EA972.md) at `0x006EAA33`
- [sub_006EABA2](../6E/Unknown_function_006EABA2.md) at `0x006EABFF`
- [sub_006EAD16](../6E/Unknown_function_006EAD16.md) at `0x006EAD80`
- [sub_006F88AE](../6F/Unknown_function_006F88AE.md) at `0x006F8C42`
- [IopAllocateAndLockMdl](../../page/71/IopAllocateAndLockMdl_function_0071AC6C.md) at `0x0071ACE5`
- [IopSetFileObjectIosbRange](../../page/71/IopSetFileObjectIosbRange_function_0071C1C8.md) at `0x0071C429`
- [IoReserveKsrPersistentMemoryEx](../../page/72/IoReserveKsrPersistentMemoryEx_function_007248C0.md) at `0x00724C5F`
- [PipGetPersistentMemory](../../page/72/PipGetPersistentMemory_function_00725290.md) at `0x007257D2`
- [ExInitializeLeapSecondData](../../page/7C/ExInitializeLeapSecondData_function_007C562C.md) at `0x007C579C`
- [NtStartProfile](../../page/7D/NtStartProfile_function_007D22C0.md) at `0x007D2437`
- [NtPssCaptureVaSpaceBulk](../../page/7D/NtPssCaptureVaSpaceBulk_function_007D4EA0.md) at `0x007D50E7`
- [MiApplyImageHotPatch](../../page/80/MiApplyImageHotPatch_function_00802330.md) at `0x00802415`
- [ExLockUserBuffer](../../page/95/ExLockUserBuffer_function_009533B8.md) at `0x009534E2`
- [MiCreateMdl](../../page/98/MiCreateMdl_function_009883A8.md) at `0x00988488`
- [WbMakeUserExecutablePagesKernelWritable](../../page/9A/WbMakeUserExecutablePagesKernelWritable_function_009A14F4.md) at `0x009A1584`
- [WbMakeUserDataPagesKernelWritable](../../page/9A/WbMakeUserDataPagesKernelWritable_function_009A15FC.md) at `0x009A16CC`
- [MiCopyVirtualMemory](../../page/9B/MiCopyVirtualMemory_function_009BBB50.md) at `0x009BC345`
- [AlpcpInitializeCompletionList](../../page/A1/AlpcpInitializeCompletionList_function_00A1A6D0.md) at `0x00A1AB76`
- [FsRtlNotifyFilterReportChange](../../page/A1/FsRtlNotifyFilterReportChange_function_00A1E880.md) at `0x00A1F194`
- [FsRtlNotifyFilterReportChangeLiteEx](../../page/A1/FsRtlNotifyFilterReportChangeLiteEx_function_00A1F2B0.md) at `0x00A1F8FC`
- [FsRtlNotifyCompleteIrp](../../page/A1/FsRtlNotifyCompleteIrp_function_00A1FA28.md) at `0x00A1FAE8`
- [MiCopyPagesIntoEnclave](../../page/A4/MiCopyPagesIntoEnclave_function_00A472AC.md) at `0x00A47645`
- [HalpDmaAllocateScatterMemory](../../page/AA/HalpDmaAllocateScatterMemory_function_00AA2D70.md) at `0x00AA2E24`
- [MiQueryMemoryPhysicalContiguity](../../page/AD/MiQueryMemoryPhysicalContiguity_function_00AD5B98.md) at `0x00AD5E7C`
- [PopAllocatePages](../../pagelk/B7/PopAllocatePages_function_00B7E3FC.md) at `0x00B7E42D`
- [ViAllocateMapRegisterFile](../../pagevrfy/B9/ViAllocateMapRegisterFile_function_00B97E9C.md) at `0x00B97FEB`
- [ViGetMdlBufferSa](../../pagevrfy/B9/ViGetMdlBufferSa_function_00B98FC8.md) at `0x00B99024`
- [ViMapDoubleBuffer](../../pagevrfy/B9/ViMapDoubleBuffer_function_00B99640.md) at `0x00B997BA`
- [ViMapDoubleBuffer](../../pagevrfy/B9/ViMapDoubleBuffer_function_00B99640.md) at `0x00B99994`
- [VfFillAllocatePagesForMdl](../../pagevrfy/BB/VfFillAllocatePagesForMdl_function_00BB1020.md) at `0x00BB1060`
- [ResFwGetContext](../../pagebgfx/BC/ResFwGetContext_function_00BC19D8.md) at `0x00BC1AB2`
- [KiComputeNumaCosts](../../init/C3/KiComputeNumaCosts_function_00C37AD4.md) at `0x00C37D54`
- [PpmHeteroInitializeIntelWpsSupport](../../init/C4/PpmHeteroInitializeIntelWpsSupport_function_00C440C8.md) at `0x00C4425F`

### Static image references
- `0x0031887C` → RVA `0x00FC6C14` (`ALMOSTRO`; read)
- `0x0031888E` → RVA `0x00E37668` (`.data`; read)
- `0x003188D8` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00318A8C` → RVA `0x00FC51FC` (`ALMOSTRO`; read)
- `0x00318AF9` → RVA `0x00E2EF70` (`.data`; read)
- `0x00318B00` → RVA `0x00E38A48` (`.data`; read)
- `0x00318B14` → RVA `0x00E376C0` (`.data`; read)
- `0x00318B57` → RVA `0x00E37698` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00318CA1` → [MiMapLockedPagesInUserSpace](../../page/97/MiMapLockedPagesInUserSpace_function_0097FE04.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00318D09` → [sub_006E141E](../6E/Unknown_function_006E141E.md) (`tail-transfer`)
  - `0x00318D13` → [sub_006E141E](../6E/Unknown_function_006E141E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00318800  48 8B C4                        mov rax, rsp
00318803  48 89 58 08                     mov qword ptr [rax + 8], rbx
00318807  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0031880B  48 89 70 20                     mov qword ptr [rax + 0x20], rsi
0031880F  57                              push rdi
00318810  41 54                           push r12
00318812  41 55                           push r13
00318814  41 56                           push r14
00318816  41 57                           push r15
00318818  48 83 EC 50                     sub rsp, 0x50
0031881C  8B BC 24 A8 00 00 00            mov edi, dword ptr [rsp + 0xa8]
00318823  44 0F B6 D2                     movzx r10d, dl
00318827  8B 51 2C                        mov edx, dword ptr [rcx + 0x2c]
0031882A  48 8B F1                        mov rsi, rcx
0031882D  48 03 51 20                     add rdx, qword ptr [rcx + 0x20]
00318831  C7 40 18 00 00 00 00            mov dword ptr [rax + 0x18], 0
00318838  41 83 F8 03                     cmp r8d, 3
0031883C  0F 85 EC 03 00 00               jne 0x140318c2e
00318842  41 BD 01 00 00 00               mov r13d, 1
00318848  45 84 D2                        test r10b, r10b
0031884B  0F 85 49 04 00 00               jne 0x140318c9a
00318851  0F BA E7 1D                     bt edi, 0x1d
00318855  0F 82 21 03 00 00               jb 0x140318b7c
0031885B  8B 5E 28                        mov ebx, dword ptr [rsi + 0x28]
0031885E  81 E2 FF 0F 00 00               and edx, 0xfff
00318864  48 81 C3 FF 0F 00 00            add rbx, 0xfff
0031886B  48 03 DA                        add rbx, rdx
0031886E  48 C1 EB 0C                     shr rbx, 0xc
00318872  40 F6 C7 20                     test dil, 0x20
00318876  0F 84 4F 02 00 00               je 0x140318acb
0031887C  83 3D 91 E3 CA 00 00            cmp dword ptr [rip + 0xcae391], 0
00318883  44 8B F3                        mov r14d, ebx
00318886  74 03                           je 0x14031888b
00318888  41 FF C6                        inc r14d
0031888B  41 8B D6                        mov edx, r14d
0031888E  48 8D 0D D3 ED B1 00            lea rcx, [rip + 0xb1edd3]
00318895  E8 86 04 00 00                  call 0x140318d20
0031889A  4C 8B E0                        mov r12, rax
0031889D  48 85 C0                        test rax, rax
003188A0  0F 84 66 03 00 00               je 0x140318c0c
003188A6  4C 8B F8                        mov r15, rax
003188A9  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
003188B3  49 C1 E7 19                     shl r15, 0x19
003188B7  48 8B C0                        mov rax, rax
003188BA  48 C1 E0 19                     shl rax, 0x19
003188BE  8B CF                           mov ecx, edi
003188C0  4C 2B F8                        sub r15, rax
003188C3  C1 F9 1F                        sar ecx, 0x1f
003188C6  8B 46 2C                        mov eax, dword ptr [rsi + 0x2c]
003188C9  83 E1 FD                        and ecx, 0xfffffffd
003188CC  83 C1 04                        add ecx, 4
003188CF  49 C1 FF 10                     sar r15, 0x10
003188D3  4C 03 F8                        add r15, rax
003188D6  8B E9                           mov ebp, ecx
003188D8  48 F7 05 A5 E1 CA 00 00 80 00 00  test qword ptr [rip + 0xcae1a5], 0x8000
003188E3  B8 00 00 00 40                  mov eax, 0x40000000
003188E8  0F 44 C7                        cmove eax, edi
003188EB  83 CD 02                        or ebp, 2
003188EE  0F BA E0 1E                     bt eax, 0x1e
003188F2  0F 42 E9                        cmovb ebp, ecx
003188F5  45 85 ED                        test r13d, r13d
003188F8  0F 84 EF 02 00 00               je 0x140318bed
003188FE  41 83 FD 02                     cmp r13d, 2
00318902  75 03                           jne 0x140318907
00318904  83 CD 18                        or ebp, 0x18
00318907  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
0031890F  44 8B CD                        mov r9d, ebp
00318912  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00318917  4C 8D 46 30                     lea r8, [rsi + 0x30]
0031891B  48 8B D3                        mov rdx, rbx
0031891E  C7 44 24 20 00 00 00 00         mov dword ptr [rsp + 0x20], 0
00318926  49 8B CC                        mov rcx, r12
00318929  E8 22 0F 00 00                  call 0x140319850
0031892E  0F B7 4E 0A                     movzx ecx, word ptr [rsi + 0xa]
00318932  85 C0                           test eax, eax
00318934  0F 88 25 02 00 00               js 0x140318b5f
0031893A  44 8B 84 24 90 00 00 00         mov r8d, dword ptr [rsp + 0x90]
00318942  48 8D 5E 0A                     lea rbx, [rsi + 0xa]
00318946  66 83 C9 01                     or cx, 1
0031894A  4C 89 7E 18                     mov qword ptr [rsi + 0x18], r15
0031894E  66 89 4E 0A                     mov word ptr [rsi + 0xa], cx
00318952  41 F6 C0 01                     test r8b, 1
00318956  0F 84 30 01 00 00               je 0x140318a8c
0031895C  4D 8B F7                        mov r14, r15
0031895F  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
00318969  49 C1 EE 09                     shr r14, 9
0031896D  49 BC F8 FF FF FF 7F 00 00 00   movabs r12, 0x7ffffffff8
00318977  4D 23 F4                        and r14, r12
0031897A  48 8B C2                        mov rax, rdx
0031897D  4C 03 F0                        add r14, rax
00318980  41 BA 04 00 00 00               mov r10d, 4
00318986  49 8B CE                        mov rcx, r14
00318989  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
0031898E  48 C1 E9 09                     shr rcx, 9
00318992  49 23 CC                        and rcx, r12
00318995  48 8B C2                        mov rax, rdx
00318998  48 03 C8                        add rcx, rax
0031899B  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
003189A0  48 C1 E9 09                     shr rcx, 9
003189A4  49 23 CC                        and rcx, r12
003189A7  48 8B C2                        mov rax, rdx
003189AA  48 03 C8                        add rcx, rax
003189AD  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
003189B2  48 C1 E9 09                     shr rcx, 9
003189B6  49 23 CC                        and rcx, r12
003189B9  48 8B C2                        mov rax, rdx
003189BC  48 03 C8                        add rcx, rax
003189BF  48 BF 00 D0 BE 7D FB F6 FF FF   movabs rdi, 0xfffff6fb7dbed000
003189C9  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
003189CE  45 8B DA                        mov r11d, r10d
003189D1  48 BB F8 D7 BE 7D FB F6 FF FF   movabs rbx, 0xfffff6fb7dbed7f8
003189DB  4E 8B 4C DC 28                  mov r9, qword ptr [rsp + r11*8 + 0x28]
003189E0  49 FF CB                        dec r11
003189E3  41 FF CA                        dec r10d
003189E6  49 8B 01                        mov rax, qword ptr [r9]
003189E9  48 8B CF                        mov rcx, rdi
003189EC  4C 3B C9                        cmp r9, rcx
003189EF  72 23                           jb 0x140318a14
003189F1  48 8B CB                        mov rcx, rbx
003189F4  4C 3B C9                        cmp r9, rcx
003189F7  77 1B                           ja 0x140318a14
003189F9  48 8B C8                        mov rcx, rax
003189FC  A8 01                           test al, 1
003189FE  74 1C                           je 0x140318a1c
00318A00  A8 42                           test al, 0x42
00318A02  41 0F 95 C0                     setne r8b
00318A06  A8 20                           test al, 0x20
00318A08  0F 95 C2                        setne dl
00318A0B  44 84 C2                        test dl, r8b
00318A0E  0F 84 6F 01 00 00               je 0x140318b83
00318A14  A8 01                           test al, 1
00318A16  0F 85 D9 01 00 00               jne 0x140318bf5
00318A1C  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
00318A26  EB 13                           jmp 0x140318a3b
00318A28  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
00318A32  45 85 D2                        test r10d, r10d
00318A35  0F 85 85 02 00 00               jne 0x140318cc0
00318A3B  49 8B 1E                        mov rbx, qword ptr [r14]
00318A3E  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
00318A48  48 8B FB                        mov rdi, rbx
00318A4B  48 0F BA EF 09                  bts rdi, 9
00318A50  48 F7 05 2D E0 CA 00 00 00 00 02  test qword ptr [rip + 0xcae02d], 0x2000000
00318A5B  74 03                           je 0x140318a60
00318A5D  0F AE E8                        lfence
00318A60  48 0F BA 25 1F E0 CA 00 24      bt qword ptr [rip + 0xcae01f], 0x24
00318A69  0F 82 EE 01 00 00               jb 0x140318c5d
00318A6F  48 8B C3                        mov rax, rbx
00318A72  F0 49 0F B1 3E                  lock cmpxchg qword ptr [r14], rdi
00318A77  48 8B D8                        mov rbx, rax
00318A7A  0F 85 6F 02 00 00               jne 0x140318cef
00318A80  44 8B 84 24 90 00 00 00         mov r8d, dword ptr [rsp + 0x90]
00318A88  48 8D 5E 0A                     lea rbx, [rsi + 0xa]
00318A8C  8B 05 6A C7 CA 00               mov eax, dword ptr [rip + 0xcac76a]
00318A92  A8 01                           test al, 1
00318A94  0F 85 64 02 00 00               jne 0x140318cfe
00318A9A  0F B7 46 0A                     movzx eax, word ptr [rsi + 0xa]
00318A9E  A8 10                           test al, 0x10
00318AA0  74 07                           je 0x140318aa9
00318AA2  66 83 C8 20                     or ax, 0x20
00318AA6  66 89 03                        mov word ptr [rbx], ax
00318AA9  49 8B C7                        mov rax, r15
00318AAC  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
00318AB1  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00318AB5  49 8B 6B 38                     mov rbp, qword ptr [r11 + 0x38]
00318AB9  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
00318ABD  49 8B E3                        mov rsp, r11
00318AC0  41 5F                           pop r15
00318AC2  41 5E                           pop r14
00318AC4  41 5D                           pop r13
00318AC6  41 5C                           pop r12
00318AC8  5F                              pop rdi
00318AC9  C3                              ret
00318ACA  CC                              int3
00318ACB  B9 00 08 00 00                  mov ecx, 0x800
00318AD0  8B C7                           mov eax, edi
00318AD2  25 FF FF FF 3F                  and eax, 0x3fffffff
00318AD7  41 B8 00 02 00 00               mov r8d, 0x200
00318ADD  83 F8 10                        cmp eax, 0x10
00318AE0  44 0F 45 C1                     cmovne r8d, ecx
00318AE4  33 C9                           xor ecx, ecx
00318AE6  83 F8 10                        cmp eax, 0x10
00318AE9  B8 00 00 00 04                  mov eax, 0x4000000
00318AEE  0F 94 C1                        sete cl
00318AF1  33 D2                           xor edx, edx
00318AF3  FF C1                           inc ecx
00318AF5  F7 F1                           div ecx
00318AF7  8B C8                           mov ecx, eax
00318AF9  48 8B 05 70 64 B1 00            mov rax, qword ptr [rip + 0xb16470]
00318B00  48 2B 05 41 FF B1 00            sub rax, qword ptr [rip + 0xb1ff41]
00318B07  48 C1 E0 15                     shl rax, 0x15
00318B0B  48 3B C1                        cmp rax, rcx
00318B0E  0F 83 68 FD FF FF               jae 0x14031887c
00318B14  48 8B 05 A5 EB B1 00            mov rax, qword ptr [rip + 0xb1eba5]
00318B1B  4C 3B C0                        cmp r8, rax
00318B1E  73 0C                           jae 0x140318b2c
00318B20  49 2B C0                        sub rax, r8
00318B23  48 3B D8                        cmp rbx, rax
00318B26  0F 82 50 FD FF FF               jb 0x14031887c
00318B2C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00318B35  8B 88 A4 05 00 00               mov ecx, dword ptr [rax + 0x5a4]
00318B3B  F6 C1 02                        test cl, 2
00318B3E  0F 85 38 FD FF FF               jne 0x14031887c
00318B44  65 8B 04 25 3C 3A 00 00         mov eax, dword ptr gs:[0x3a3c]
00318B4C  A9 01 00 01 00                  test eax, 0x10001
00318B51  0F 85 25 FD FF FF               jne 0x14031887c
00318B57  FF 05 3B EB B1 00               inc dword ptr [rip + 0xb1eb3b]
00318B5D  EB 1D                           jmp 0x140318b7c
00318B5F  66 0F BA E1 0D                  bt cx, 0xd
00318B64  0F 83 6F 01 00 00               jae 0x140318cd9
00318B6A  45 8B C6                        mov r8d, r14d
00318B6D  48 8D 0D F4 EA B1 00            lea rcx, [rip + 0xb1eaf4]
00318B74  49 8B D4                        mov rdx, r12
00318B77  E8 C4 E6 F2 FF                  call 0x140247240
00318B7C  33 C0                           xor eax, eax
00318B7E  E9 29 FF FF FF                  jmp 0x140318aac
00318B83  48 F7 05 FA DE CA 00 00 00 60 00  test qword ptr [rip + 0xcadefa], 0x600000
00318B8E  0F 84 80 FE FF FF               je 0x140318a14
00318B94  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
00318B9D  4C 8B 82 B8 00 00 00            mov r8, qword ptr [rdx + 0xb8]
00318BA4  41 80 B8 60 01 00 00 01         cmp byte ptr [r8 + 0x160], 1
00318BAC  0F 84 62 FE FF FF               je 0x140318a14
00318BB2  49 8B 90 08 05 00 00            mov rdx, qword ptr [r8 + 0x508]
00318BB9  48 85 D2                        test rdx, rdx
00318BBC  0F 84 52 FE FF FF               je 0x140318a14
00318BC2  49 C1 E9 03                     shr r9, 3
00318BC6  41 81 E1 FF 01 00 00            and r9d, 0x1ff
00318BCD  4A 8B 14 CA                     mov rdx, qword ptr [rdx + r9*8]
00318BD1  F6 C2 20                        test dl, 0x20
00318BD4  74 04                           je 0x140318bda
00318BD6  48 83 C9 20                     or rcx, 0x20
00318BDA  48 8B C1                        mov rax, rcx
00318BDD  48 83 C8 42                     or rax, 0x42
00318BE1  F6 C2 42                        test dl, 0x42
00318BE4  48 0F 44 C1                     cmove rax, rcx
00318BE8  E9 27 FE FF FF                  jmp 0x140318a14
00318BED  83 CD 08                        or ebp, 8
00318BF0  E9 12 FD FF FF                  jmp 0x140318907
00318BF5  84 C0                           test al, al
00318BF7  0F 88 2B FE FF FF               js 0x140318a28
00318BFD  49 83 FB 01                     cmp r11, 1
00318C01  0F 84 15 FE FF FF               je 0x140318a1c
00318C07  E9 CF FD FF FF                  jmp 0x1403189db
00318C0C  66 0F BA 66 0A 0D               bt word ptr [rsi + 0xa], 0xd
00318C12  0F 82 64 FF FF FF               jb 0x140318b7c
00318C18  83 BC 24 A0 00 00 00 00         cmp dword ptr [rsp + 0xa0], 0
00318C20  0F 84 56 FF FF FF               je 0x140318b7c
00318C26  8B CB                           mov ecx, ebx
00318C28  E8 6F DF 1D 00                  call 0x1404f6b9c
00318C2D  CC                              int3
00318C2E  41 8B C8                        mov ecx, r8d
00318C31  45 85 C0                        test r8d, r8d
00318C34  74 78                           je 0x140318cae
00318C36  83 E9 01                        sub ecx, 1
00318C39  0F 84 03 FC FF FF               je 0x140318842
00318C3F  83 E9 01                        sub ecx, 1
00318C42  74 0E                           je 0x140318c52
00318C44  83 E9 02                        sub ecx, 2
00318C47  74 65                           je 0x140318cae
00318C49  83 F9 01                        cmp ecx, 1
00318C4C  0F 85 2A FF FF FF               jne 0x140318b7c
00318C52  41 BD 02 00 00 00               mov r13d, 2
00318C58  E9 EB FB FF FF                  jmp 0x140318848
00318C5D  40 0F B6 C7                     movzx eax, dil
00318C61  24 21                           and al, 0x21
00318C63  3C 01                           cmp al, 1
00318C65  0F 85 04 FE FF FF               jne 0x140318a6f
00318C6B  48 8B C2                        mov rax, rdx
00318C6E  48 03 C1                        add rax, rcx
00318C71  4C 3B F0                        cmp r14, rax
00318C74  0F 82 F5 FD FF FF               jb 0x140318a6f
00318C7A  41 B8 80 00 00 00               mov r8d, 0x80
00318C80  48 8B D7                        mov rdx, rdi
00318C83  49 8B CE                        mov rcx, r14
00318C86  E8 F5 A0 F7 FF                  call 0x140292d80
00318C8B  48 B9 00 00 00 00 40 00 00 00   movabs rcx, 0x4000000000
00318C95  E9 D5 FD FF FF                  jmp 0x140318a6f
00318C9A  48 8B CE                        mov rcx, rsi
00318C9D  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00318CA1  E8 5E 71 66 00                  call 0x14097fe04
00318CA6  4C 8B F8                        mov r15, rax
00318CA9  E9 FB FD FF FF                  jmp 0x140318aa9
00318CAE  45 33 ED                        xor r13d, r13d
00318CB1  E9 92 FB FF FF                  jmp 0x140318848
00318CB6  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
00318CC0  49 C1 EE 09                     shr r14, 9
00318CC4  4D 23 F4                        and r14, r12
00318CC7  48 8B C2                        mov rax, rdx
00318CCA  4C 03 F0                        add r14, rax
00318CCD  41 83 C2 FF                     add r10d, -1
00318CD1  0F 84 64 FD FF FF               je 0x140318a3b
00318CD7  EB E7                           jmp 0x140318cc0
00318CD9  83 BC 24 A0 00 00 00 00         cmp dword ptr [rsp + 0xa0], 0
00318CE1  0F 84 83 FE FF FF               je 0x140318b6a
00318CE7  8B CB                           mov ecx, ebx
00318CE9  E8 AE DE 1D 00                  call 0x1404f6b9c
00318CEE  CC                              int3
00318CEF  48 BA 00 00 00 00 80 F6 FF FF   movabs rdx, 0xfffff68000000000
00318CF9  E9 4A FD FF FF                  jmp 0x140318a48
00318CFE  41 83 E0 01                     and r8d, 1
00318D02  83 3D 0B DF CA 00 00            cmp dword ptr [rip + 0xcadf0b], 0
00318D09  0F 84 0F 87 3C 00               je 0x1406e141e
00318D0F  41 83 C8 02                     or r8d, 2
00318D13  E9 06 87 3C 00                  jmp 0x1406e141e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmMapLockedPagesSpecifyCache(__int64 a1, unsigned __int8 a2, int a3, __int64 a4, unsigned int a5, unsigned int a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_p18;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    v_rsp = (v_rsp) - (80);
    a2 = ((unsigned int)(*(unsigned int *)(a1 + 44))) + (*(unsigned __int64 *)(a1 + 32));
    *(unsigned int *)(v_rsp + 24) = 0;
    if (a3 != 3) goto loc_00318C2E;
loc_00318842:
loc_00318848:
    if (a2 != 0) goto loc_00318C9A;
    if (condition_is_below) goto loc_00318B7C;
    a2 = (unsigned int)((a2) & (0xFFFULL));
    v_rbx = ((unsigned int)(*(unsigned int *)(a1 + 40))) + (0xFFFULL);
    v_rbx = (v_rbx) + (a2);
    v_rbx = (v_rbx) >> (12);
    if ((((unsigned __int8)((unsigned int)(a6))) & (32)) == 0) goto loc_00318ACB;
loc_0031887C:
    v_r14 = (unsigned int)((unsigned int)(v_rbx));
    if ((*(unsigned int *)(v_rip + 13296529)) != 0) {
        v_r14 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) + 1);
    }
    result = MiReservePtes(v_rip + 11660755, (unsigned int)((unsigned int)(v_r14)), a3, a4);
    if (result == 0) goto loc_00318C0C;
    v_r15 = (result) << (25);
    result = (result) << (25);
    v_r15 = (v_r15) - (result);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) >> (31));
    a1 = (unsigned int)((a1) & (0xFFFFFFFDULL));
    a1 = (unsigned int)((a1) + (4));
    v_r15 = (v_r15) >> (16);
    v_r15 = (v_r15) + ((unsigned int)(*(unsigned int *)(a1 + 44)));
    result = (unsigned int)(0x40000000ULL);
    if (((*(unsigned __int64 *)(v_rip + 13296037)) & (0x8000ULL)) == 0) { result = (unsigned int)((unsigned int)(a6)); }
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (2));
    if (condition_is_below) { v_rbp = (unsigned int)(a1); }
    if (1 == 0) goto loc_00318BED;
    if (1 == 2) {
        v_rbp = (unsigned int)((v_rbp) | (24));
    }
    v_stack_m50 = v_stack_p18;
    v_stack_m58 = 0;
    result = MiFillSystemPtes(result, v_rbx, a1 + 48, (unsigned int)((unsigned int)(v_rbp)));
    if (sign_flag) goto loc_00318B5F;
    a1 = (unsigned __int16)((*(unsigned __int16 *)(a1 + 10)) | (1));
    *(unsigned __int64 *)(a1 + 24) = v_r15;
    *(unsigned __int16 *)(a1 + 10) = (unsigned __int16)(a1);
    if ((((unsigned __int8)((unsigned int)(v_stack_p18))) & (1)) == 0) goto loc_00318A8C;
    v_r14 = (v_r15) >> (9);
    v_r14 = (v_r14) & (result);
    v_r14 = (v_r14) + (v_rbx);
    v_stack_m48 = v_r14;
    a1 = (v_r14) >> (9);
    a1 = (a1) & (result);
    a1 = (a1) + (v_rbx);
    v_stack_m40 = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (result);
    a1 = (a1) + (v_rbx);
    v_stack_m38 = a1;
    a1 = (a1) >> (9);
    a1 = (a1) & (result);
    a1 = (a1) + (v_rbx);
    v_stack_m30 = a1;
loc_003189DB:
    v_r11 = (4) - 1;
    v_r10 = (unsigned int)((4) - 1);
    if ((*(unsigned __int64 *)(v_rsp + 4 * 8 + 40)) < ((unsigned int)(a6))) goto loc_00318A14;
    if ((*(unsigned __int64 *)(v_rsp + 4 * 8 + 40)) > (a1 + 10)) goto loc_00318A14;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 4 * 8 + 40)))) & (1)) == 0) goto loc_00318A1C;
    a3 = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 4 * 8 + 40)))) & (66)) != 0) ? 1 : 0;
    a2 = ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 4 * 8 + 40)))) & (32)) != 0) ? 1 : 0;
    if (((a2) & ((unsigned __int8)(a3))) == 0) goto loc_00318B83;
loc_00318A14:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp + 4 * 8 + 40)))) & (1)) != 0) goto loc_00318BF5;
loc_00318A1C:
    goto loc_00318A3B;
loc_00318A28:
    if ((unsigned int)(v_r10) != 0) goto loc_00318CC0;
loc_00318A3B:
loc_00318A48:
    if (((*(unsigned __int64 *)(v_rip + 13295661)) & (0x2000000ULL)) != 0) {
    }
    if (condition_is_below) goto loc_00318C5D;
loc_00318A6F:
    if (((*(unsigned __int64 *)(v_rip + 13295661)) & (0x2000000ULL)) != 0) goto loc_00318CEF;
loc_00318A8C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13289322)))) & (1)) != 0) goto loc_00318CFE;
    result = *(unsigned __int16 *)(a1 + 10);
    if ((((unsigned __int8)(*(unsigned __int16 *)(a1 + 10))) & (16)) != 0) {
        result = (unsigned __int16)((*(unsigned __int16 *)(a1 + 10)) | (32));
        *(unsigned __int16 *)(a1 + 10) = (unsigned __int16)(result);
    }
loc_00318AAC:
    return v_r15;
loc_00318ACB:
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_r14)))) & (0x3FFFFFFFULL));
    a3 = 512;
    if (((unsigned int)(result)) != 16) { a3 = (unsigned int)((unsigned int)(0x800ULL)); }
    a1 = 0;
    a1 = (((unsigned int)(result)) == 16) ? 1 : 0;
    a2 = 0;
    a1 = (unsigned int)((a1) + 1);
    result = (*(unsigned __int64 *)(v_rip + 11625584)) - (*(unsigned __int64 *)(v_rip + 11665217));
    result = (result) << (21);
    if (result >= ((unsigned int)((unsigned int)((unsigned int)(0x4000000ULL))))) goto loc_0031887C;
    if (a3 >= (*(unsigned __int64 *)(v_rip + 11660197))) goto loc_00318B2C;
    result = (*(unsigned __int64 *)(v_rip + 11660197)) - (a3);
    if ((*(unsigned __int64 *)(v_stack_m28 + 48)) < result) goto loc_0031887C;
loc_00318B2C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1444)))) & (2)) != 0) goto loc_0031887C;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 14908))))) & (0x10001ULL)) != 0) goto loc_0031887C;
    goto loc_00318B7C;
loc_00318B5F:
    if (condition_is_above_or_equal) goto loc_00318CD9;
loc_00318B6A:
    result = MiReleasePtes(v_rip + 11660020, result, (unsigned int)((unsigned int)(v_r14)), *(unsigned __int64 *)(v_rsp + 4 * 8 + 40));
loc_00318B7C:
    result = 0;
    goto loc_00318AAC;
loc_00318B83:
    if (((*(unsigned __int64 *)(v_rip + 13295354)) & (0x600000ULL)) == 0) goto loc_00318A14;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 352)) == 1) goto loc_00318A14;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) == 0) goto loc_00318A14;
    a4 = (*(unsigned __int64 *)(v_rsp + 4 * 8 + 40)) >> (3);
    a4 = (unsigned int)((a4) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a4 * 8))) & (32)) != 0) {
        a1 = (v_rip + 11660020) | (32);
    }
    result = (a1) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a4 * 8))) & (66)) == 0) { result = a1; }
    goto loc_00318A14;
loc_00318BED:
    v_rbp = (unsigned int)((*(unsigned __int64 *)(v_stack_m28 + 56)) | (8));
    goto loc_00318907;
loc_00318BF5:
    if (sign_flag) goto loc_00318A28;
    if (v_stack_m28 == 1) goto loc_00318A1C;
    goto loc_003189DB;
loc_00318C0C:
    if (v_stack_m28 < 1) goto loc_00318B7C;
    if (a5 == 0) goto loc_00318B7C;
    result = MiIssueNoPtesBugcheck((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48))), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a4 * 8), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a4);
loc_00318C2E:
    if ((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) == 0) goto loc_00318CAE;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)))) - (1));
    if (condition_is_equal) goto loc_00318842;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00318C52;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00318CAE;
    if (((unsigned int)(a1)) != 1) goto loc_00318B7C;
loc_00318C52:
    goto loc_00318848;
loc_00318C5D:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int64 *)(v_r14))) & (33));
    if (((unsigned __int8)(result)) != 1) goto loc_00318A6F;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a4 * 8)) + (a1);
    if (v_r14 < result) goto loc_00318A6F;
    result = MiCheckLinearProtectedPteAccessedBit(v_r14, *(unsigned __int64 *)(v_r14), 128, a4);
    goto loc_00318A6F;
loc_00318C9A:
    v_stack_m30 = (unsigned int)(*(unsigned __int64 *)(v_r14));
    result = MiMapLockedPagesInUserSpace(*(unsigned __int64 *)(v_stack_m28 + 72), *(unsigned __int64 *)(v_r14), 128, a4);
    goto loc_00318AA9;
loc_00318CAE:
    v_r13 = 0;
    goto loc_00318848;
loc_00318CC0:
    v_r14 = (v_r14) >> (9);
    v_r14 = (v_r14) & (result);
    v_r14 = (v_r14) + (*(unsigned __int64 *)(v_r14));
    v_r10 = (unsigned int)((v_r10) + (-1));
    if (condition_is_equal) goto loc_00318A3B;
    goto loc_00318CC0;
loc_00318CD9:
    if (a5 == 0) goto loc_00318B6A;
    result = MiIssueNoPtesBugcheck((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 48))), *(unsigned __int64 *)(v_r14), 128, a4);
loc_00318CEF:
    goto loc_00318A48;
loc_00318CFE:
    a3 = (unsigned int)((128) & (1));
    a3 = (unsigned int)((a3) | (2));
}
```

## 5. (Beta) C Style

```c
int64_t MmMapLockedPagesSpecifyCache(void *Arg1, uint8_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_p18;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    local_rsp = (local_rsp) - (80);
    Arg2 = ((uint32_t)(*(uint32_t *)(arg1 + 0x2C))) + (*(uint64_t *)(arg1 + 0x20));
    *(uint32_t *)(local_rsp + 0x18) = 0;
    if (Arg3 != 3) goto loc_00318C2E;
loc_00318842:
loc_00318848:
    if (Arg2 != 0) goto loc_00318C9A;
    if (condition_is_below) goto loc_00318B7C;
    Arg2 = (uint32_t)((Arg2) & (0xFFFULL));
    local_rbx = ((uint32_t)(*(uint32_t *)(arg1 + 0x28))) + (0xFFFULL);
    local_rbx = (local_rbx) + (Arg2);
    local_rbx = (local_rbx) >> (12);
    if ((((uint8_t)((uint32_t)(Arg6))) & (32)) == 0) goto loc_00318ACB;
loc_0031887C:
    local_r14 = (uint32_t)((uint32_t)(local_rbx));
    if ((*(uint32_t *)(v_rip + 0xCAE391)) != 0) {
        local_r14 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) + 1);
    }
    result = MiReservePtes(v_rip + 11660755, (uint32_t)((uint32_t)(local_r14)), Arg3, Arg4);
    if (result == 0) goto loc_00318C0C;
    local_r15 = (result) << (25);
    result = (result) << (25);
    local_r15 = (local_r15) - (result);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) >> (31));
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFFFDULL));
    Arg1 = (uint32_t)((Arg1) + (4));
    local_r15 = (local_r15) >> (16);
    local_r15 = (local_r15) + ((uint32_t)(*(uint32_t *)(arg1 + 0x2C)));
    result = (uint32_t)(0x40000000ULL);
    if (((*(uint64_t *)(v_rip + 0xCAE1A5)) & (0x8000ULL)) == 0) { result = (uint32_t)((uint32_t)(Arg6)); }
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (2));
    if (condition_is_below) { local_rbp = (uint32_t)(Arg1); }
    if (1 == 0) goto loc_00318BED;
    if (1 == 2) {
        local_rbp = (uint32_t)((local_rbp) | (24));
    }
    v_stack_m50 = v_stack_p18;
    v_stack_m58 = 0;
    result = MiFillSystemPtes(result, local_rbx, Arg1 + 48, (uint32_t)((uint32_t)(local_rbp)));
    if (sign_flag) goto loc_00318B5F;
    Arg1 = (uint16_t)((*(uint16_t *)(arg1 + 0xA)) | (1));
    *(uint64_t *)(arg1 + 0x18) = local_r15;
    *(uint16_t *)(arg1 + 0xA) = (uint16_t)(Arg1);
    if ((((uint8_t)((uint32_t)(v_stack_p18))) & (1)) == 0) goto loc_00318A8C;
    local_r14 = (local_r15) >> (9);
    local_r14 = (local_r14) & (result);
    local_r14 = (local_r14) + (local_rbx);
    v_stack_m48 = local_r14;
    Arg1 = (local_r14) >> (9);
    Arg1 = (Arg1) & (result);
    Arg1 = (Arg1) + (local_rbx);
    v_stack_m40 = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (result);
    Arg1 = (Arg1) + (local_rbx);
    v_stack_m38 = Arg1;
    Arg1 = (Arg1) >> (9);
    Arg1 = (Arg1) & (result);
    Arg1 = (Arg1) + (local_rbx);
    v_stack_m30 = Arg1;
loc_003189DB:
    local_r11 = (4) - 1;
    local_r10 = (uint32_t)((4) - 1);
    if ((*(uint64_t *)(local_rsp + 0x4 * 8 + 0x28)) < ((uint32_t)(Arg6))) goto loc_00318A14;
    if ((*(uint64_t *)(local_rsp + 0x4 * 8 + 0x28)) > (Arg1 + 10)) goto loc_00318A14;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x4 * 8 + 0x28)))) & (1)) == 0) goto loc_00318A1C;
    Arg3 = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x4 * 8 + 0x28)))) & (66)) != 0) ? 1 : 0;
    Arg2 = ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x4 * 8 + 0x28)))) & (32)) != 0) ? 1 : 0;
    if (((Arg2) & ((uint8_t)(Arg3))) == 0) goto loc_00318B83;
loc_00318A14:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_rsp + 0x4 * 8 + 0x28)))) & (1)) != 0) goto loc_00318BF5;
loc_00318A1C:
    goto loc_00318A3B;
loc_00318A28:
    if ((uint32_t)(local_r10) != 0) goto loc_00318CC0;
loc_00318A3B:
loc_00318A48:
    if (((*(uint64_t *)(v_rip + 0xCAE02D)) & (0x2000000ULL)) != 0) {
    }
    if (condition_is_below) goto loc_00318C5D;
loc_00318A6F:
    if (((*(uint64_t *)(v_rip + 0xCAE02D)) & (0x2000000ULL)) != 0) goto loc_00318CEF;
loc_00318A8C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCAC76A)))) & (1)) != 0) goto loc_00318CFE;
    result = *(uint16_t *)(arg1 + 0xA);
    if ((((uint8_t)(*(uint16_t *)(arg1 + 0xA))) & (16)) != 0) {
        result = (uint16_t)((*(uint16_t *)(arg1 + 0xA)) | (32));
        *(uint16_t *)(arg1 + 0xA) = (uint16_t)(result);
    }
loc_00318AAC:
    return local_r15;
loc_00318ACB:
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(local_r14)))) & (0x3FFFFFFFULL));
    Arg3 = 512;
    if (((uint32_t)(result)) != 16) { Arg3 = (uint32_t)((uint32_t)(0x800ULL)); }
    Arg1 = 0;
    Arg1 = (((uint32_t)(result)) == 16) ? 1 : 0;
    Arg2 = 0;
    Arg1 = (uint32_t)((Arg1) + 1);
    result = (*(uint64_t *)(v_rip + 0xB16470)) - (*(uint64_t *)(v_rip + 0xB1FF41));
    result = (result) << (21);
    if (result >= ((uint32_t)((uint32_t)((uint32_t)(0x4000000ULL))))) goto loc_0031887C;
    if (Arg3 >= (*(uint64_t *)(v_rip + 0xB1EBA5))) goto loc_00318B2C;
    result = (*(uint64_t *)(v_rip + 0xB1EBA5)) - (Arg3);
    if ((*(uint64_t *)(v_stack_m28 + 0x30)) < result) goto loc_0031887C;
loc_00318B2C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A4)))) & (2)) != 0) goto loc_0031887C;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x3A3C))))) & (0x10001ULL)) != 0) goto loc_0031887C;
    goto loc_00318B7C;
loc_00318B5F:
    if (condition_is_above_or_equal) goto loc_00318CD9;
loc_00318B6A:
    result = MiReleasePtes(v_rip + 11660020, result, (uint32_t)((uint32_t)(local_r14)), *(uint64_t *)(local_rsp + 0x4 * 8 + 0x28));
loc_00318B7C:
    result = 0;
    goto loc_00318AAC;
loc_00318B83:
    if (((*(uint64_t *)(v_rip + 0xCADEFA)) & (0x600000ULL)) == 0) goto loc_00318A14;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x160)) == 1) goto loc_00318A14;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) == 0) goto loc_00318A14;
    Arg4 = (*(uint64_t *)(local_rsp + 0x4 * 8 + 0x28)) >> (3);
    Arg4 = (uint32_t)((Arg4) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg4 * 8))) & (32)) != 0) {
        Arg1 = (v_rip + 11660020) | (32);
    }
    result = (Arg1) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg4 * 8))) & (66)) == 0) { result = Arg1; }
    goto loc_00318A14;
loc_00318BED:
    local_rbp = (uint32_t)((*(uint64_t *)(v_stack_m28 + 0x38)) | (8));
    goto loc_00318907;
loc_00318BF5:
    if (sign_flag) goto loc_00318A28;
    if (v_stack_m28 == 1) goto loc_00318A1C;
    goto loc_003189DB;
loc_00318C0C:
    if (v_stack_m28 < 1) goto loc_00318B7C;
    if (Arg5 == 0) goto loc_00318B7C;
    result = MiIssueNoPtesBugcheck((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30))), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg4 * 8), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg4);
loc_00318C2E:
    if ((uint32_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) == 0) goto loc_00318CAE;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)))) - (1));
    if (condition_is_equal) goto loc_00318842;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00318C52;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00318CAE;
    if (((uint32_t)(Arg1)) != 1) goto loc_00318B7C;
loc_00318C52:
    goto loc_00318848;
loc_00318C5D:
    result = (uint8_t)(((uint8_t)(*(uint64_t *)(local_r14))) & (33));
    if (((uint8_t)(result)) != 1) goto loc_00318A6F;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + Arg4 * 8)) + (Arg1);
    if (local_r14 < result) goto loc_00318A6F;
    result = MiCheckLinearProtectedPteAccessedBit(local_r14, *(uint64_t *)(local_r14), 128, Arg4);
    goto loc_00318A6F;
loc_00318C9A:
    v_stack_m30 = (uint32_t)(*(uint64_t *)(local_r14));
    result = MiMapLockedPagesInUserSpace(*(uint64_t *)(v_stack_m28 + 0x48), *(uint64_t *)(local_r14), 128, Arg4);
    goto loc_00318AA9;
loc_00318CAE:
    local_r13 = 0;
    goto loc_00318848;
loc_00318CC0:
    local_r14 = (local_r14) >> (9);
    local_r14 = (local_r14) & (result);
    local_r14 = (local_r14) + (*(uint64_t *)(local_r14));
    local_r10 = (uint32_t)((local_r10) + (-1));
    if (condition_is_equal) goto loc_00318A3B;
    goto loc_00318CC0;
loc_00318CD9:
    if (Arg5 == 0) goto loc_00318B6A;
    result = MiIssueNoPtesBugcheck((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x30))), *(uint64_t *)(local_r14), 128, Arg4);
loc_00318CEF:
    goto loc_00318A48;
loc_00318CFE:
    Arg3 = (uint32_t)((128) & (1));
    Arg3 = (uint32_t)((Arg3) | (2));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `W` |
| `Arg1` | `+ 0xA` | `16` | `R` |
| `Arg1` | `+ 0xA` | `16` | `W` |
| `Arg1` | `+ 0xA` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `W` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x2C` | `32` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00318800&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
