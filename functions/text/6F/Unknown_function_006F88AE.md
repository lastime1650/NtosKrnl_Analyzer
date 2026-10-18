# sub_006F88AE

- RVA: `0x006F88AE`–`0x006F9072` (길이 `1,988` bytes)
- VA: `0x00000001406F88AE`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B6188`
- 디코드: `489`개 명령, `1,988/1,988` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **57**; 고유 호출 대상: **54**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006F88B8` → [ZwTerminateProcess](../6A/ZwTerminateProcess_function_006AD650.md) (function, `0x006AD650`)
- `0x006F88C7` → [DbgkpSuspendProcess](../../page/8A/DbgkpSuspendProcess_function_008A34D4.md) (function, `0x008A34D4`)
- `0x006F88D6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x006F88EC` → [PspIumGetSystemData](../../page/78/PspIumGetSystemData_function_00787CC8.md) (function, `0x00787CC8`)
- `0x006F8995` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x006F89B3` → [KeWaitForAlertByThreadId](../3C/KeWaitForAlertByThreadId_function_003C4B14.md) (function, `0x003C4B14`)
- `0x006F89DC` → [MmProtectVirtualMemory](../../page/88/MmProtectVirtualMemory_function_00881050.md) (function, `0x00881050`)
- `0x006F89F3` → [KiUnstackDetachProcess](../21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x006F8A48` → [EtwSetInformation](../../page/7B/EtwSetInformation_function_007B9070.md) (function, `0x007B9070`)
- `0x006F8A56` → [EtwUnregister](../../page/A7/EtwUnregister_function_00A723D0.md) (function, `0x00A723D0`)
- `0x006F8A83` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (function, `0x00920960`)
- `0x006F8AA9` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x006F8ABD` → [DbgkpSendErrorMessage](../../page/92/DbgkpSendErrorMessage_function_009210A8.md) (function, `0x009210A8`)
- `0x006F8ACB` → [DbgkpResumeProcess](../../page/A7/DbgkpResumeProcess_function_00A7954C.md) (function, `0x00A7954C`)
- `0x006F8B23` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x006F8B58` → [VslFreePoolTransferObject](../4C/VslFreePoolTransferObject_function_004C4290.md) (function, `0x004C4290`)
- `0x006F8B7D` → [VslAllocatePool](../4B/VslAllocatePool_function_004BAF80.md) (function, `0x004BAF80`)
- `0x006F8B87` → [PspIumAllocateSecurePool](../5E/PspIumAllocateSecurePool_function_005E4698.md) (function, `0x005E4698`)
- `0x006F8BBC` → [HvlpDepositPages](../58/HvlpDepositPages_function_00585474.md) (function, `0x00585474`)
- `0x006F8BC9` → [VslHandleKsrCall](../58/VslHandleKsrCall_function_0058E7F0.md) (function, `0x0058E7F0`)
- `0x006F8BDB` → [PspIumVerifyParentSd](../../page/78/PspIumVerifyParentSd_function_00787D04.md) (function, `0x00787D04`)
- `0x006F8BF8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x006F8C42` → [MmMapLockedPagesSpecifyCache](../31/MmMapLockedPagesSpecifyCache_function_00318800.md) (function, `0x00318800`)
- `0x006F8CC8` → [DbgkMapViewOfSection](../../page/89/DbgkMapViewOfSection_function_00897460.md) (function, `0x00897460`)
- `0x006F8CF3` → [DbgkPostModuleMessage](../49/DbgkPostModuleMessage_function_004913C4.md) (function, `0x004913C4`)
- `0x006F8D07` → [MmUnlockLoadedModuleListExclusive](../43/MmUnlockLoadedModuleListExclusive_function_004322E0.md) (function, `0x004322E0`)
- `0x006F8D12` → [MmLockLoadedModuleListExclusive](../43/MmLockLoadedModuleListExclusive_function_0043229C.md) (function, `0x0043229C`)
- `0x006F8D25` → [MmUnmapProtectedKernelPageRange](../../page/AA/MmUnmapProtectedKernelPageRange_function_00AA36DC.md) (function, `0x00AA36DC`)
- `0x006F8D3E` → [MmMapProtectedKernelPage](../../page/AB/MmMapProtectedKernelPage_function_00AB6690.md) (function, `0x00AB6690`)
- `0x006F8D4D` → [MmMapDriverTablePage](../68/MmMapDriverTablePage_function_00683EAC.md) (function, `0x00683EAC`)
- `0x006F8D63` → [MmUnmapLockedPages](../24/MmUnmapLockedPages_function_00246E60.md) (function, `0x00246E60`)
- `0x006F8D6D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x006F8D7B` → [PspMapView](../4C/PspMapView_function_004C77E8.md) (function, `0x004C77E8`)
- `0x006F8DB1` → [PspIumReplenishPartitionPages](../2C/PspIumReplenishPartitionPages_function_002C8710.md) (function, `0x002C8710`)
- `0x006F8DD5` → [PspIumFreePartitionState](../5E/PspIumFreePartitionState_function_005E48C4.md) (function, `0x005E48C4`)
- `0x006F8DE3` → [PspIumAllocatePartitionState](../5E/PspIumAllocatePartitionState_function_005E43A8.md) (function, `0x005E43A8`)
- `0x006F8DF6` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x006F8E0A` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x006F8E3B` → [KiStackAttachProcess](../21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x006F8E47` → [MmUnmapViewOfSection](../../page/88/MmUnmapViewOfSection_function_0088A310.md) (function, `0x0088A310`)
- `0x006F8E5B` → [KiStackAttachProcess](../21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x006F8E6C` → [MmPrepareImagePagesForHotPatch](../../page/80/MmPrepareImagePagesForHotPatch_function_008074E8.md) (function, `0x008074E8`)
- `0x006F8E83` → [KiUnstackDetachProcess](../21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x006F8E9A` → [PsTerminateVsmEnclave](../../page/78/PsTerminateVsmEnclave_function_00788A64.md) (function, `0x00788A64`)
- `0x006F8F0C` → [MmFreeSecurePoolMemory](../68/MmFreeSecurePoolMemory_function_00682E10.md) (function, `0x00682E10`)
- `0x006F8F23` → [PsAdjustBasicEnclaveThreadList](../5E/PsAdjustBasicEnclaveThreadList_function_005E4BD8.md) (function, `0x005E4BD8`)
- `0x006F8F39` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x006F8F50` → [MmUpdateSlabRangeType](../../init/C6/MmUpdateSlabRangeType_function_00C6A10C.md) (function, `0x00C6A10C`)
- `0x006F8F5F` → [MmUnlockPages](../29/MmUnlockPages_function_0029EEE0.md) (function, `0x0029EEE0`)
- `0x006F8F68` → [IoFreeMdl](../29/IoFreeMdl_function_0029EA80.md) (function, `0x0029EA80`)
- `0x006F8FCC` → [MmCreateSectionForHotpatch](../../page/80/MmCreateSectionForHotpatch_function_00807360.md) (function, `0x00807360`)
- `0x006F8FE7` → [MmGetSectionStrongImageReference](../../page/70/MmGetSectionStrongImageReference_function_00701DF0.md) (function, `0x00701DF0`)
- `0x006F8FFA` → [ObCloseHandle](../../page/8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x006F9021` → [PspIumAlertMultipleThreadByThreadId](../5E/PspIumAlertMultipleThreadByThreadId_function_005E4324.md) (function, `0x005E4324`)
- `0x006F902E` → [MmRemoveSecureImageActivePatch](../../page/80/MmRemoveSecureImageActivePatch_function_0080760C.md) (function, `0x0080760C`)
- `0x006F904E` → [MmInsertSecureImageActivePatch](../../page/80/MmInsertSecureImageActivePatch_function_008073E4.md) (function, `0x008073E4`)
- `0x006F9061` → [MmCommitHotPatchTable](../../page/80/MmCommitHotPatchTable_function_00807278.md) (function, `0x00807278`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006F898A` → RVA `0x006CC550` (` ?? ::FNODOBFM::`string'`; read)
- `0x006F8A69` → RVA `0x00AB8E20` (`VslIumEtwEnableCallback`; read)
- `0x006F8F32` → RVA `0x00F05DC0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **25**
  - `0x006F88C7` → [DbgkpSuspendProcess](../../page/8A/DbgkpSuspendProcess_function_008A34D4.md) (`.text` → `PAGE`)
  - `0x006F88D6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x006F88EC` → [PspIumGetSystemData](../../page/78/PspIumGetSystemData_function_00787CC8.md) (`.text` → `PAGE`)
  - `0x006F89DC` → [MmProtectVirtualMemory](../../page/88/MmProtectVirtualMemory_function_00881050.md) (`.text` → `PAGE`)
  - `0x006F8A48` → [EtwSetInformation](../../page/7B/EtwSetInformation_function_007B9070.md) (`.text` → `PAGE`)
  - `0x006F8A56` → [EtwUnregister](../../page/A7/EtwUnregister_function_00A723D0.md) (`.text` → `PAGE`)
  - `0x006F8A83` → [EtwRegister](../../page/92/EtwRegister_function_00920960.md) (`.text` → `PAGE`)
  - `0x006F8ABD` → [DbgkpSendErrorMessage](../../page/92/DbgkpSendErrorMessage_function_009210A8.md) (`.text` → `PAGE`)
  - `0x006F8ACB` → [DbgkpResumeProcess](../../page/A7/DbgkpResumeProcess_function_00A7954C.md) (`.text` → `PAGE`)
  - `0x006F8BDB` → [PspIumVerifyParentSd](../../page/78/PspIumVerifyParentSd_function_00787D04.md) (`.text` → `PAGE`)
  - `0x006F8BF8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x006F8CC8` → [DbgkMapViewOfSection](../../page/89/DbgkMapViewOfSection_function_00897460.md) (`.text` → `PAGE`)
  - `0x006F8D25` → [MmUnmapProtectedKernelPageRange](../../page/AA/MmUnmapProtectedKernelPageRange_function_00AA36DC.md) (`.text` → `PAGE`)
  - `0x006F8D3E` → [MmMapProtectedKernelPage](../../page/AB/MmMapProtectedKernelPage_function_00AB6690.md) (`.text` → `PAGE`)
  - `0x006F8D6D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x006F8E47` → [MmUnmapViewOfSection](../../page/88/MmUnmapViewOfSection_function_0088A310.md) (`.text` → `PAGE`)
  - `0x006F8E6C` → [MmPrepareImagePagesForHotPatch](../../page/80/MmPrepareImagePagesForHotPatch_function_008074E8.md) (`.text` → `PAGE`)
  - `0x006F8E9A` → [PsTerminateVsmEnclave](../../page/78/PsTerminateVsmEnclave_function_00788A64.md) (`.text` → `PAGE`)
  - `0x006F8F50` → [MmUpdateSlabRangeType](../../init/C6/MmUpdateSlabRangeType_function_00C6A10C.md) (`.text` → `INIT`)
  - `0x006F8FCC` → [MmCreateSectionForHotpatch](../../page/80/MmCreateSectionForHotpatch_function_00807360.md) (`.text` → `PAGE`)
  - `0x006F8FE7` → [MmGetSectionStrongImageReference](../../page/70/MmGetSectionStrongImageReference_function_00701DF0.md) (`.text` → `PAGE`)
  - `0x006F8FFA` → [ObCloseHandle](../../page/8A/ObCloseHandle_function_008A1870.md) (`.text` → `PAGE`)
  - `0x006F902E` → [MmRemoveSecureImageActivePatch](../../page/80/MmRemoveSecureImageActivePatch_function_0080760C.md) (`.text` → `PAGE`)
  - `0x006F904E` → [MmInsertSecureImageActivePatch](../../page/80/MmInsertSecureImageActivePatch_function_008073E4.md) (`.text` → `PAGE`)
  - `0x006F9061` → [MmCommitHotPatchTable](../../page/80/MmCommitHotPatchTable_function_00807278.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **38**
  - `0x006F88BE` → [PsDispatchIumService + 0x76](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F88E4` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F88F2` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F899E` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F89A5` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F89FB` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8A33` → [PsDispatchIumService + 0x3A5](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8AD1` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8B4C` → [PsDispatchIumService + 0x3A5](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8B8F` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8BCF` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8CA8` → [PsDispatchIumService + 0x3A5](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8CCE` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8CF9` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8D0D` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8D18` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8D2B` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8D44` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8D53` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8D73` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8DA0` → [PsDispatchIumService + 0x3A5](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8DB8` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8DC6` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8DDB` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8DFC` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8E10` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8E8C` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8EA0` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8ED8` → [PsDispatchIumService + 0x3A5](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8F12` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8F3F` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8F56` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8F6E` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F8F9A` → [PsDispatchIumService + 0x3A5](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F9019` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F9034` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F9054` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)
  - `0x006F906D` → [PsDispatchIumService + 0xCF](../4A/PsDispatchIumService_function_004A2F0C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F88AE  8B 51 10                        mov edx, dword ptr [rcx + 0x10]
006F88B1  48 83 CB FF                     or rbx, 0xffffffffffffffff
006F88B5  48 8B CB                        mov rcx, rbx
006F88B8  E8 93 4D FB FF                  call 0x1406ad650
006F88BD  90                              nop
006F88BE  E9 BF A6 DA FF                  jmp 0x1404a2f82
006F88C3  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F88C7  E8 08 AC 1A 00                  call 0x1408a34d4
006F88CC  0F B6 C0                        movzx eax, al
006F88CF  EB 0F                           jmp 0x1406f88e0
006F88D1  33 D2                           xor edx, edx
006F88D3  48 8B CB                        mov rcx, rbx
006F88D6  E8 95 9F 48 00                  call 0x140b82870
006F88DB  B8 9A 00 00 C0                  mov eax, 0xc000009a
006F88E0  48 89 47 08                     mov qword ptr [rdi + 8], rax
006F88E4  E9 F2 A6 DA FF                  jmp 0x1404a2fdb
006F88E9  48 8B CF                        mov rcx, rdi
006F88EC  E8 D7 F3 08 00                  call 0x140787cc8
006F88F1  90                              nop
006F88F2  E9 E4 A6 DA FF                  jmp 0x1404a2fdb
006F88F7  0F 10 47 0A                     movups xmm0, xmmword ptr [rdi + 0xa]
006F88FB  0F 29 84 24 E0 01 00 00         movaps xmmword ptr [rsp + 0x1e0], xmm0
006F8903  0F 10 4F 1A                     movups xmm1, xmmword ptr [rdi + 0x1a]
006F8907  0F 29 8C 24 F0 01 00 00         movaps xmmword ptr [rsp + 0x1f0], xmm1
006F890F  0F 10 47 2A                     movups xmm0, xmmword ptr [rdi + 0x2a]
006F8913  0F 29 84 24 00 02 00 00         movaps xmmword ptr [rsp + 0x200], xmm0
006F891B  0F 10 4F 3A                     movups xmm1, xmmword ptr [rdi + 0x3a]
006F891F  0F 29 8C 24 10 02 00 00         movaps xmmword ptr [rsp + 0x210], xmm1
006F8927  0F 10 47 4A                     movups xmm0, xmmword ptr [rdi + 0x4a]
006F892B  0F 29 84 24 20 02 00 00         movaps xmmword ptr [rsp + 0x220], xmm0
006F8933  F2 0F 10 4F 5A                  movsd xmm1, qword ptr [rdi + 0x5a]
006F8938  F2 0F 11 8C 24 30 02 00 00      movsd qword ptr [rsp + 0x230], xmm1
006F8941  8B 47 62                        mov eax, dword ptr [rdi + 0x62]
006F8944  89 84 24 38 02 00 00            mov dword ptr [rsp + 0x238], eax
006F894B  0F B7 47 66                     movzx eax, word ptr [rdi + 0x66]
006F894F  66 89 84 24 3C 02 00 00         mov word ptr [rsp + 0x23c], ax
006F8957  40 88 B4 24 3E 02 00 00         mov byte ptr [rsp + 0x23e], sil
006F895F  44 0F B7 4F 08                  movzx r9d, word ptr [rdi + 8]
006F8964  41 8B C1                        mov eax, r9d
006F8967  D1 E8                           shr eax, 1
006F8969  25 FF 0F 00 00                  and eax, 0xfff
006F896E  41 C1 E9 0D                     shr r9d, 0xd
006F8972  48 8D 8C 24 E0 01 00 00         lea rcx, [rsp + 0x1e0]
006F897A  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
006F897F  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
006F8983  8B 47 04                        mov eax, dword ptr [rdi + 4]
006F8986  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
006F898A  4C 8D 05 BF 3B FD FF            lea r8, [rip - 0x2c441]
006F8991  33 D2                           xor edx, edx
006F8993  33 C9                           xor ecx, ecx
006F8995  E8 F6 08 C6 FF                  call 0x140359290
006F899A  F6 47 08 01                     test byte ptr [rdi + 8], 1
006F899E  0F 84 37 A6 DA FF               je 0x1404a2fdb
006F89A4  CC                              int3
006F89A5  E9 31 A6 DA FF                  jmp 0x1404a2fdb
006F89AA  45 33 C0                        xor r8d, r8d
006F89AD  48 8B D6                        mov rdx, rsi
006F89B0  8A 4F 08                        mov cl, byte ptr [rdi + 8]
006F89B3  E8 5C C1 CC FF                  call 0x1403c4b14
006F89B8  E9 A9 06 00 00                  jmp 0x1406f9066
006F89BD  48 8D 47 28                     lea rax, [rdi + 0x28]
006F89C1  4C 8D 4F 20                     lea r9, [rdi + 0x20]
006F89C5  4C 8D 47 18                     lea r8, [rdi + 0x18]
006F89C9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
006F89CE  8B 00                           mov eax, dword ptr [rax]
006F89D0  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
006F89D4  48 8B 57 08                     mov rdx, qword ptr [rdi + 8]
006F89D8  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
006F89DC  E8 6F 86 18 00                  call 0x140881050
006F89E1  8B F0                           mov esi, eax
006F89E3  48 3B 5F 08                     cmp rbx, qword ptr [rdi + 8]
006F89E7  74 0F                           je 0x1406f89f8
006F89E9  33 D2                           xor edx, edx
006F89EB  48 8D 8C 24 98 00 00 00         lea rcx, [rsp + 0x98]
006F89F3  E8 38 F3 B1 FF                  call 0x140217d30
006F89F8  89 77 08                        mov dword ptr [rdi + 8], esi
006F89FB  E9 DB A5 DA FF                  jmp 0x1404a2fdb
006F8A00  83 F9 15                        cmp ecx, 0x15
006F8A03  0F 87 24 01 00 00               ja 0x1406f8b2d
006F8A09  0F 84 C7 00 00 00               je 0x1406f8ad6
006F8A0F  83 E9 0F                        sub ecx, 0xf
006F8A12  0F 84 AB FE FF FF               je 0x1406f88c3
006F8A18  83 E9 01                        sub ecx, 1
006F8A1B  0F 84 A6 00 00 00               je 0x1406f8ac7
006F8A21  83 E9 01                        sub ecx, 1
006F8A24  74 73                           je 0x1406f8a99
006F8A26  83 E9 01                        sub ecx, 1
006F8A29  74 35                           je 0x1406f8a60
006F8A2B  83 E9 01                        sub ecx, 1
006F8A2E  74 22                           je 0x1406f8a52
006F8A30  83 F9 01                        cmp ecx, 1
006F8A33  0F 85 78 A8 DA FF               jne 0x1404a32b1
006F8A39  44 8B 4F 20                     mov r9d, dword ptr [rdi + 0x20]
006F8A3D  4C 8B 47 18                     mov r8, qword ptr [rdi + 0x18]
006F8A41  8B 57 10                        mov edx, dword ptr [rdi + 0x10]
006F8A44  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F8A48  E8 23 06 0C 00                  call 0x1407b9070
006F8A4D  E9 14 06 00 00                  jmp 0x1406f9066
006F8A52  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F8A56  E8 75 99 37 00                  call 0x140a723d0
006F8A5B  E9 06 06 00 00                  jmp 0x1406f9066
006F8A60  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
006F8A65  4C 8B 47 18                     mov r8, qword ptr [rdi + 0x18]
006F8A69  48 8D 05 B0 03 3C 00            lea rax, [rip + 0x3c03b0]
006F8A70  4D 85 C0                        test r8, r8
006F8A73  48 0F 45 F0                     cmovne rsi, rax
006F8A77  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
006F8A7C  48 8B D6                        mov rdx, rsi
006F8A7F  48 8D 4F 08                     lea rcx, [rdi + 8]
006F8A83  E8 D8 7E 22 00                  call 0x140920960
006F8A88  48 63 C8                        movsxd rcx, eax
006F8A8B  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
006F8A90  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
006F8A94  E9 D0 05 00 00                  jmp 0x1406f9069
006F8A99  33 D2                           xor edx, edx
006F8A9B  41 B8 10 01 00 00               mov r8d, 0x110
006F8AA1  48 8D 8C 24 D0 00 00 00         lea rcx, [rsp + 0xd0]
006F8AA9  E8 92 E1 FC FF                  call 0x1406c6c40
006F8AAE  4C 8D 84 24 D0 00 00 00         lea r8, [rsp + 0xd0]
006F8AB6  8B 57 10                        mov edx, dword ptr [rdi + 0x10]
006F8AB9  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F8ABD  E8 E6 85 22 00                  call 0x1409210a8
006F8AC2  E9 9F 05 00 00                  jmp 0x1406f9066
006F8AC7  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F8ACB  E8 7C 0A 38 00                  call 0x140a7954c
006F8AD0  90                              nop
006F8AD1  E9 05 A5 DA FF                  jmp 0x1404a2fdb
006F8AD6  4C 8B 57 08                     mov r10, qword ptr [rdi + 8]
006F8ADA  48 8D 4F 20                     lea rcx, [rdi + 0x20]
006F8ADE  48 39 31                        cmp qword ptr [rcx], rsi
006F8AE1  75 09                           jne 0x1406f8aec
006F8AE3  48 39 77 28                     cmp qword ptr [rdi + 0x28], rsi
006F8AE7  75 03                           jne 0x1406f8aec
006F8AE9  48 8B CE                        mov rcx, rsi
006F8AEC  48 39 77 30                     cmp qword ptr [rdi + 0x30], rsi
006F8AF0  75 06                           jne 0x1406f8af8
006F8AF2  48 39 77 38                     cmp qword ptr [rdi + 0x38], rsi
006F8AF6  74 04                           je 0x1406f8afc
006F8AF8  48 8D 77 30                     lea rsi, [rdi + 0x30]
006F8AFC  48 8B 47 48                     mov rax, qword ptr [rdi + 0x48]
006F8B00  8B 57 40                        mov edx, dword ptr [rdi + 0x40]
006F8B03  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
006F8B08  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
006F8B0C  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
006F8B11  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006F8B16  45 33 C9                        xor r9d, r9d
006F8B19  45 33 C0                        xor r8d, r8d
006F8B1C  48 8D 57 10                     lea rdx, [rdi + 0x10]
006F8B20  49 8B CA                        mov rcx, r10
006F8B23  E8 A8 65 B6 FF                  call 0x14025f0d0
006F8B28  E9 39 05 00 00                  jmp 0x1406f9066
006F8B2D  83 E9 16                        sub ecx, 0x16
006F8B30  0F 84 9E 00 00 00               je 0x1406f8bd4
006F8B36  83 E9 01                        sub ecx, 1
006F8B39  0F 84 87 00 00 00               je 0x1406f8bc6
006F8B3F  83 E9 01                        sub ecx, 1
006F8B42  74 50                           je 0x1406f8b94
006F8B44  83 E9 01                        sub ecx, 1
006F8B47  74 1C                           je 0x1406f8b65
006F8B49  83 F9 01                        cmp ecx, 1
006F8B4C  0F 85 5F A7 DA FF               jne 0x1404a32b1
006F8B52  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F8B56  33 D2                           xor edx, edx
006F8B58  E8 33 B7 DC FF                  call 0x1404c4290
006F8B5D  48 8B C8                        mov rcx, rax
006F8B60  E9 06 02 00 00                  jmp 0x1406f8d6b
006F8B65  48 8D 47 20                     lea rax, [rdi + 0x20]
006F8B69  4C 8D 4F 18                     lea r9, [rdi + 0x18]
006F8B6D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006F8B72  4C 8D 47 10                     lea r8, [rdi + 0x10]
006F8B76  8B 57 10                        mov edx, dword ptr [rdi + 0x10]
006F8B79  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F8B7D  E8 FE 23 DC FF                  call 0x1404baf80
006F8B82  EB 08                           jmp 0x1406f8b8c
006F8B84  48 8B CF                        mov rcx, rdi
006F8B87  E8 0C BB EE FF                  call 0x1405e4698
006F8B8C  89 47 08                        mov dword ptr [rdi + 8], eax
006F8B8F  E9 47 A4 DA FF                  jmp 0x1404a2fdb
006F8B94  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
006F8B97  8D 81 7F FF CA 3F               lea eax, [rcx + 0x3fcaff7f]
006F8B9D  83 F8 01                        cmp eax, 1
006F8BA0  41 0F 96 C1                     setbe r9b
006F8BA4  81 F9 75 00 35 C0               cmp ecx, 0xc0350075
006F8BAA  74 08                           je 0x1406f8bb4
006F8BAC  81 F9 82 00 35 C0               cmp ecx, 0xc0350082
006F8BB2  75 03                           jne 0x1406f8bb7
006F8BB4  40 B6 01                        mov sil, 1
006F8BB7  33 C9                           xor ecx, ecx
006F8BB9  44 8A C6                        mov r8b, sil
006F8BBC  E8 B3 C8 E8 FF                  call 0x140585474
006F8BC1  E9 A0 04 00 00                  jmp 0x1406f9066
006F8BC6  48 8B CF                        mov rcx, rdi
006F8BC9  E8 22 5C E9 FF                  call 0x14058e7f0
006F8BCE  90                              nop
006F8BCF  E9 07 A4 DA FF                  jmp 0x1404a2fdb
006F8BD4  4C 8B 47 18                     mov r8, qword ptr [rdi + 0x18]
006F8BD8  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
006F8BDB  E8 24 F1 08 00                  call 0x140787d04
006F8BE0  E9 81 04 00 00                  jmp 0x1406f9066
006F8BE5  41 B8 4D 6D 6C 64               mov r8d, 0x646c6d4d
006F8BEB  41 BE 38 00 00 00               mov r14d, 0x38
006F8BF1  41 8B D6                        mov edx, r14d
006F8BF4  41 8D 4E 08                     lea ecx, [r14 + 8]
006F8BF8  E8 F3 94 48 00                  call 0x140b820f0
006F8BFD  48 8B D8                        mov rbx, rax
006F8C00  48 85 C0                        test rax, rax
006F8C03  0F 84 D2 FC FF FF               je 0x1406f88db
006F8C09  48 89 30                        mov qword ptr [rax], rsi
006F8C0C  44 89 70 08                     mov dword ptr [rax + 8], r14d
006F8C10  48 89 70 20                     mov qword ptr [rax + 0x20], rsi
006F8C14  48 C7 40 28 00 10 00 00         mov qword ptr [rax + 0x28], 0x1000
006F8C1C  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
006F8C20  48 89 43 30                     mov qword ptr [rbx + 0x30], rax
006F8C24  66 C7 43 0A 02 00               mov word ptr [rbx + 0xa], 2
006F8C2A  C7 44 24 28 10 00 00 40         mov dword ptr [rsp + 0x28], 0x40000010
006F8C32  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
006F8C36  45 33 C9                        xor r9d, r9d
006F8C39  33 D2                           xor edx, edx
006F8C3B  45 8D 46 C9                     lea r8d, [r14 - 0x37]
006F8C3F  48 8B CB                        mov rcx, rbx
006F8C42  E8 B9 FB C1 FF                  call 0x140318800
006F8C47  F6 43 0A 01                     test byte ptr [rbx + 0xa], 1
006F8C4B  0F 84 80 FC FF FF               je 0x1406f88d1
006F8C51  48 89 77 08                     mov qword ptr [rdi + 8], rsi
006F8C55  48 89 5F 10                     mov qword ptr [rdi + 0x10], rbx
006F8C59  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
006F8C5D  E9 B3 03 00 00                  jmp 0x1406f9015
006F8C62  83 F9 28                        cmp ecx, 0x28
006F8C65  0F 87 3A 02 00 00               ja 0x1406f8ea5
006F8C6B  0F 84 20 02 00 00               je 0x1406f8e91
006F8C71  83 F9 22                        cmp ecx, 0x22
006F8C74  0F 87 0B 01 00 00               ja 0x1406f8d85
006F8C7A  0F 84 F8 00 00 00               je 0x1406f8d78
006F8C80  83 E9 1C                        sub ecx, 0x1c
006F8C83  0F 84 CF 00 00 00               je 0x1406f8d58
006F8C89  83 E9 01                        sub ecx, 1
006F8C8C  0F 84 9E 00 00 00               je 0x1406f8d30
006F8C92  83 E9 01                        sub ecx, 1
006F8C95  0F 84 82 00 00 00               je 0x1406f8d1d
006F8C9B  83 E9 01                        sub ecx, 1
006F8C9E  74 5E                           je 0x1406f8cfe
006F8CA0  83 E9 01                        sub ecx, 1
006F8CA3  74 2E                           je 0x1406f8cd3
006F8CA5  83 F9 01                        cmp ecx, 1
006F8CA8  0F 85 03 A6 DA FF               jne 0x1404a32b1
006F8CAE  8B 47 38                        mov eax, dword ptr [rdi + 0x38]
006F8CB1  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
006F8CB5  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
006F8CB8  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
006F8CBC  4C 8B 47 18                     mov r8, qword ptr [rdi + 0x18]
006F8CC0  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
006F8CC4  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F8CC8  E8 93 E7 19 00                  call 0x140897460
006F8CCD  90                              nop
006F8CCE  E9 08 A3 DA FF                  jmp 0x1404a2fdb
006F8CD3  48 8B 47 30                     mov rax, qword ptr [rdi + 0x30]
006F8CD7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
006F8CDC  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
006F8CDF  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
006F8CE3  44 8B 4F 20                     mov r9d, dword ptr [rdi + 0x20]
006F8CE7  4C 8B 47 18                     mov r8, qword ptr [rdi + 0x18]
006F8CEB  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
006F8CEF  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F8CF3  E8 CC 86 D9 FF                  call 0x1404913c4
006F8CF8  90                              nop
006F8CF9  E9 DD A2 DA FF                  jmp 0x1404a2fdb
006F8CFE  48 39 77 08                     cmp qword ptr [rdi + 8], rsi
006F8D02  75 0E                           jne 0x1406f8d12
006F8D04  8A 4F 10                        mov cl, byte ptr [rdi + 0x10]
006F8D07  E8 D4 95 D3 FF                  call 0x1404322e0
006F8D0C  90                              nop
006F8D0D  E9 C9 A2 DA FF                  jmp 0x1404a2fdb
006F8D12  E8 85 95 D3 FF                  call 0x14043229c
006F8D17  90                              nop
006F8D18  E9 BE A2 DA FF                  jmp 0x1404a2fdb
006F8D1D  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
006F8D21  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F8D25  E8 B2 A9 3A 00                  call 0x140aa36dc
006F8D2A  90                              nop
006F8D2B  E9 AB A2 DA FF                  jmp 0x1404a2fdb
006F8D30  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
006F8D34  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F8D38  48 39 77 18                     cmp qword ptr [rdi + 0x18], rsi
006F8D3C  75 0B                           jne 0x1406f8d49
006F8D3E  E8 4D D9 3B 00                  call 0x140ab6690
006F8D43  90                              nop
006F8D44  E9 92 A2 DA FF                  jmp 0x1404a2fdb
006F8D49  44 8B 4F 20                     mov r9d, dword ptr [rdi + 0x20]
006F8D4D  E8 5A B1 F8 FF                  call 0x140683eac
006F8D52  90                              nop
006F8D53  E9 83 A2 DA FF                  jmp 0x1404a2fdb
006F8D58  48 8B 5F 08                     mov rbx, qword ptr [rdi + 8]
006F8D5C  48 8B D3                        mov rdx, rbx
006F8D5F  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
006F8D63  E8 F8 E0 B4 FF                  call 0x140246e60
006F8D68  48 8B CB                        mov rcx, rbx
006F8D6B  33 D2                           xor edx, edx
006F8D6D  E8 FE 9A 48 00                  call 0x140b82870
006F8D72  90                              nop
006F8D73  E9 63 A2 DA FF                  jmp 0x1404a2fdb
006F8D78  48 8B CF                        mov rcx, rdi
006F8D7B  E8 68 EA DC FF                  call 0x1404c77e8
006F8D80  E9 E1 02 00 00                  jmp 0x1406f9066
006F8D85  83 E9 23                        sub ecx, 0x23
006F8D88  0F 84 87 00 00 00               je 0x1406f8e15
006F8D8E  83 E9 01                        sub ecx, 1
006F8D91  74 6E                           je 0x1406f8e01
006F8D93  83 E9 01                        sub ecx, 1
006F8D96  74 55                           je 0x1406f8ded
006F8D98  83 E9 01                        sub ecx, 1
006F8D9B  74 2E                           je 0x1406f8dcb
006F8D9D  83 F9 01                        cmp ecx, 1
006F8DA0  0F 85 0B A5 DA FF               jne 0x1404a32b1
006F8DA6  48 89 77 18                     mov qword ptr [rdi + 0x18], rsi
006F8DAA  8B 57 10                        mov edx, dword ptr [rdi + 0x10]
006F8DAD  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F8DB1  E8 5A F9 BC FF                  call 0x1402c8710
006F8DB6  84 C0                           test al, al
006F8DB8  0F 84 1D A2 DA FF               je 0x1404a2fdb
006F8DBE  48 C7 47 18 01 00 00 00         mov qword ptr [rdi + 0x18], 1
006F8DC6  E9 10 A2 DA FF                  jmp 0x1404a2fdb
006F8DCB  48 39 77 08                     cmp qword ptr [rdi + 8], rsi
006F8DCF  75 0F                           jne 0x1406f8de0
006F8DD1  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
006F8DD5  E8 EA BA EE FF                  call 0x1405e48c4
006F8DDA  90                              nop
006F8DDB  E9 FB A1 DA FF                  jmp 0x1404a2fdb
006F8DE0  48 8B CF                        mov rcx, rdi
006F8DE3  E8 C0 B5 EE FF                  call 0x1405e43a8
006F8DE8  E9 79 02 00 00                  jmp 0x1406f9066
006F8DED  45 33 C0                        xor r8d, r8d
006F8DF0  33 D2                           xor edx, edx
006F8DF2  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F8DF6  E8 15 65 C4 FF                  call 0x14033f310
006F8DFB  90                              nop
006F8DFC  E9 DA A1 DA FF                  jmp 0x1404a2fdb
006F8E01  BA 44 66 6C 74                  mov edx, 0x746c6644
006F8E06  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F8E0A  E8 D1 EA BF FF                  call 0x1402f78e0
006F8E0F  90                              nop
006F8E10  E9 C6 A1 DA FF                  jmp 0x1404a2fdb
006F8E15  48 8B 5F 08                     mov rbx, qword ptr [rdi + 8]
006F8E19  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
006F8E22  48 8B B0 B8 00 00 00            mov rsi, qword ptr [rax + 0xb8]
006F8E29  48 3B F3                        cmp rsi, rbx
006F8E2C  74 12                           je 0x1406f8e40
006F8E2E  4C 8D 84 24 98 00 00 00         lea r8, [rsp + 0x98]
006F8E36  33 D2                           xor edx, edx
006F8E38  48 8B CB                        mov rcx, rbx
006F8E3B  E8 E0 D9 B1 FF                  call 0x140216820
006F8E40  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
006F8E44  48 8B CB                        mov rcx, rbx
006F8E47  E8 C4 14 19 00                  call 0x14088a310
006F8E4C  EB 23                           jmp 0x1406f8e71
006F8E4E  4C 8D 84 24 98 00 00 00         lea r8, [rsp + 0x98]
006F8E56  33 D2                           xor edx, edx
006F8E58  48 8B CB                        mov rcx, rbx
006F8E5B  E8 C0 D9 B1 FF                  call 0x140216820
006F8E60  4C 8D 47 10                     lea r8, [rdi + 0x10]
006F8E64  48 8B 57 18                     mov rdx, qword ptr [rdi + 0x18]
006F8E68  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
006F8E6C  E8 77 E6 10 00                  call 0x1408074e8
006F8E71  4C 63 F0                        movsxd r14, eax
006F8E74  48 3B F3                        cmp rsi, rbx
006F8E77  74 0F                           je 0x1406f8e88
006F8E79  33 D2                           xor edx, edx
006F8E7B  48 8D 8C 24 98 00 00 00         lea rcx, [rsp + 0x98]
006F8E83  E8 A8 EE B1 FF                  call 0x140217d30
006F8E88  4C 89 77 08                     mov qword ptr [rdi + 8], r14
006F8E8C  E9 4A A1 DA FF                  jmp 0x1404a2fdb
006F8E91  BA 00 00 00 80                  mov edx, 0x80000000
006F8E96  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F8E9A  E8 C5 FB 08 00                  call 0x140788a64
006F8E9F  90                              nop
006F8EA0  E9 36 A1 DA FF                  jmp 0x1404a2fdb
006F8EA5  83 F9 2F                        cmp ecx, 0x2f
006F8EA8  0F 87 C5 00 00 00               ja 0x1406f8f73
006F8EAE  0F 84 A7 00 00 00               je 0x1406f8f5b
006F8EB4  83 E9 29                        sub ecx, 0x29
006F8EB7  0F 84 87 00 00 00               je 0x1406f8f44
006F8EBD  83 E9 01                        sub ecx, 1
006F8EC0  74 6B                           je 0x1406f8f2d
006F8EC2  83 E9 01                        sub ecx, 1
006F8EC5  74 50                           je 0x1406f8f17
006F8EC7  83 E9 01                        sub ecx, 1
006F8ECA  0F 84 B4 FC FF FF               je 0x1406f8b84
006F8ED0  83 E9 01                        sub ecx, 1
006F8ED3  74 2B                           je 0x1406f8f00
006F8ED5  83 F9 01                        cmp ecx, 1
006F8ED8  0F 85 D3 A3 DA FF               jne 0x1404a32b1
006F8EDE  48 8B 5F 08                     mov rbx, qword ptr [rdi + 8]
006F8EE2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
006F8EEB  48 8B B0 B8 00 00 00            mov rsi, qword ptr [rax + 0xb8]
006F8EF2  48 3B F3                        cmp rsi, rbx
006F8EF5  0F 84 65 FF FF FF               je 0x1406f8e60
006F8EFB  E9 4E FF FF FF                  jmp 0x1406f8e4e
006F8F00  44 8B 47 28                     mov r8d, dword ptr [rdi + 0x28]
006F8F04  48 8B 57 20                     mov rdx, qword ptr [rdi + 0x20]
006F8F08  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
006F8F0C  E8 FF 9E F8 FF                  call 0x140682e10
006F8F11  90                              nop
006F8F12  E9 C4 A0 DA FF                  jmp 0x1404a2fdb
006F8F17  44 8B 47 18                     mov r8d, dword ptr [rdi + 0x18]
006F8F1B  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
006F8F1F  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F8F23  E8 B0 BC EE FF                  call 0x1405e4bd8
006F8F28  E9 39 01 00 00                  jmp 0x1406f9066
006F8F2D  BA 01 00 00 00                  mov edx, 1
006F8F32  48 8D 0D 87 CE 80 00            lea rcx, [rip + 0x80ce87]
006F8F39  E8 E2 05 C0 FF                  call 0x1402f9520
006F8F3E  90                              nop
006F8F3F  E9 97 A0 DA FF                  jmp 0x1404a2fdb
006F8F44  44 8B 47 18                     mov r8d, dword ptr [rdi + 0x18]
006F8F48  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
006F8F4C  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F8F50  E8 B7 11 57 00                  call 0x140c6a10c
006F8F55  90                              nop
006F8F56  E9 80 A0 DA FF                  jmp 0x1404a2fdb
006F8F5B  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F8F5F  E8 7C 5F BA FF                  call 0x14029eee0
006F8F64  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F8F68  E8 13 5B BA FF                  call 0x14029ea80
006F8F6D  90                              nop
006F8F6E  E9 68 A0 DA FF                  jmp 0x1404a2fdb
006F8F73  83 E9 30                        sub ecx, 0x30
006F8F76  0F 84 DD 00 00 00               je 0x1406f9059
006F8F7C  83 E9 01                        sub ecx, 1
006F8F7F  0F 84 B4 00 00 00               je 0x1406f9039
006F8F85  83 E9 01                        sub ecx, 1
006F8F88  0F 84 9A 00 00 00               je 0x1406f9028
006F8F8E  83 E9 01                        sub ecx, 1
006F8F91  0F 84 87 00 00 00               je 0x1406f901e
006F8F97  83 F9 01                        cmp ecx, 1
006F8F9A  0F 85 11 A3 DA FF               jne 0x1404a32b1
006F8FA0  44 8A 77 1C                     mov r14b, byte ptr [rdi + 0x1c]
006F8FA4  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
006F8FA9  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
006F8FAE  48 8D 44 24 60                  lea rax, [rsp + 0x60]
006F8FB3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
006F8FB8  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
006F8FBD  44 8B 4F 18                     mov r9d, dword ptr [rdi + 0x18]
006F8FC1  44 8B 47 14                     mov r8d, dword ptr [rdi + 0x14]
006F8FC5  8B 57 10                        mov edx, dword ptr [rdi + 0x10]
006F8FC8  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F8FCC  E8 8F E3 10 00                  call 0x140807360
006F8FD1  8B D8                           mov ebx, eax
006F8FD3  85 C0                           test eax, eax
006F8FD5  78 2D                           js 0x1406f9004
006F8FD7  4C 8D 4C 24 68                  lea r9, [rsp + 0x68]
006F8FDC  45 33 C0                        xor r8d, r8d
006F8FDF  41 8A D6                        mov dl, r14b
006F8FE2  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
006F8FE7  E8 04 8E 00 00                  call 0x140701df0
006F8FEC  8B D8                           mov ebx, eax
006F8FEE  85 C0                           test eax, eax
006F8FF0  79 12                           jns 0x1406f9004
006F8FF2  41 8A D6                        mov dl, r14b
006F8FF5  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
006F8FFA  E8 71 88 1A 00                  call 0x1408a1870
006F8FFF  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
006F9004  89 5F 08                        mov dword ptr [rdi + 8], ebx
006F9007  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
006F900C  48 89 47 10                     mov qword ptr [rdi + 0x10], rax
006F9010  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
006F9015  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
006F9019  E9 BD 9F DA FF                  jmp 0x1404a2fdb
006F901E  48 8B CF                        mov rcx, rdi
006F9021  E8 FE B2 EE FF                  call 0x1405e4324
006F9026  EB 3E                           jmp 0x1406f9066
006F9028  8B 57 10                        mov edx, dword ptr [rdi + 0x10]
006F902B  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
006F902E  E8 D9 E5 10 00                  call 0x14080760c
006F9033  90                              nop
006F9034  E9 A2 9F DA FF                  jmp 0x1404a2fdb
006F9039  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
006F903C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
006F9040  44 8B 4F 20                     mov r9d, dword ptr [rdi + 0x20]
006F9044  44 8B 47 18                     mov r8d, dword ptr [rdi + 0x18]
006F9048  8B 57 10                        mov edx, dword ptr [rdi + 0x10]
006F904B  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
006F904E  E8 91 E3 10 00                  call 0x1408073e4
006F9053  90                              nop
006F9054  E9 82 9F DA FF                  jmp 0x1404a2fdb
006F9059  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
006F905D  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
006F9061  E8 12 E2 10 00                  call 0x140807278
006F9066  48 63 C8                        movsxd rcx, eax
006F9069  48 89 4F 08                     mov qword ptr [rdi + 8], rcx
006F906D  E9 69 9F DA FF                  jmp 0x1404a2fdb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006F88AE(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    unsigned __int64 v_stack_p1E0;
    unsigned __int64 v_stack_p1F0;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p200;
    unsigned __int64 v_stack_p210;
    unsigned __int64 v_stack_p220;
    unsigned __int64 v_stack_p230;
    unsigned int v_stack_p238;
    unsigned __int16 v_stack_p23C;
    unsigned __int8 v_stack_p23E;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p98;
    unsigned __int64 v_stack_pD0;

    v_rbx = (v_rbx) | (-1);
    result = ZwTerminateProcess(v_rbx, (unsigned int)(*(unsigned int *)(a1 + 16)), a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_006F88AE(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    uint64_t v_stack_p1E0;
    uint64_t v_stack_p1F0;
    uint32_t v_stack_p20;
    uint64_t v_stack_p200;
    uint64_t v_stack_p210;
    uint64_t v_stack_p220;
    uint64_t v_stack_p230;
    uint32_t v_stack_p238;
    uint16_t v_stack_p23C;
    uint8_t v_stack_p23E;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p98;
    uint64_t v_stack_pD0;

    local_rbx = (local_rbx) | (-1);
    result = ZwTerminateProcess(local_rbx, (uint32_t)(*(uint32_t *)(arg1 + 0x10)), a3, a4);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F88AE&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
