# IopXxxControlFile

- RVA: `0x008E9AD0`–`0x008EB3C6` (길이 `6,390` bytes)
- VA: `0x00000001408E9AD0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00086B70`
- 디코드: `1,359`개 명령, `6,390/6,390` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **70**; 고유 호출 대상: **42**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **16**

### Outgoing calls
- `0x008E9CC0` → [ExRaiseAccessViolation](ExRaiseAccessViolation_function_008E9240.md) (function, `0x008E9240`)
- `0x008E9CF3` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (function, `0x0029D530`)
- `0x008E9D87` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x008E9DAF` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x008E9E19` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x008EA075` → [ExRaiseAccessViolation](ExRaiseAccessViolation_function_008E9240.md) (function, `0x008E9240`)
- `0x008EA0C4` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)
- `0x008EA0D6` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008EA0DE` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008EA1B9` → [PiCMFastIoDeviceDispatch](PiCMFastIoDeviceDispatch_function_008EB3D0.md) (function, `0x008EB3D0`)
- `0x008EA1DD` → [VfFastIoCheckState](../../pagevrfy/BB/VfFastIoCheckState_function_00BB9440.md) (function, `0x00BB9440`)
- `0x008EA20A` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x008EA228` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (function, `0x00207720`)
- `0x008EA342` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008EA363` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008EA3CE` → [IopExceptionCleanupEx](../8A/IopExceptionCleanupEx_function_008AE5C8.md) (function, `0x008AE5C8`)
- `0x008EA3EB` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008EA46E` → [IopSynchronousServiceTail](IopSynchronousServiceTail_function_008EB440.md) (function, `0x008EB440`)
- `0x008EA47E` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008EA53E` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008EA552` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008EA55F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008EA67B` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x008EA683` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008EA69A` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)
- `0x008EA6BA` → [IopDecrementCompletionContextUsageCount](../../text/45/IopDecrementCompletionContextUsageCount_function_00452678.md) (function, `0x00452678`)
- `0x008EA6C2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008EA6E7` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008EA723` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008EA751` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x008EA782` → [IoGetAttachedDevice](../../text/41/IoGetAttachedDevice_function_00410810.md) (function, `0x00410810`)
- `0x008EA7B2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008EA7C9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008EA7ED` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008EA822` → [IoGetAttachedDevice](../../text/41/IoGetAttachedDevice_function_00410810.md) (function, `0x00410810`)
- `0x008EA832` → [FsRtlGetSupportedFeatures](../../text/47/FsRtlGetSupportedFeatures_function_00473F20.md) (function, `0x00473F20`)
- `0x008EA874` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008EA8E7` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008EA8FE` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (function, `0x0029B120`)
- `0x008EA94D` → [IopIncrementCompletionContextUsageCountAndReadData](../../text/44/IopIncrementCompletionContextUsageCountAndReadData_function_00443C60.md) (function, `0x00443C60`)
- `0x008EA99A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008EA9B1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008EA9E7` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (function, `0x0029EBF0`)
- `0x008EAA05` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x008EAA27` → [MmProbeAndLockPages](../../text/23/MmProbeAndLockPages_function_0023B990.md) (function, `0x0023B990`)
- `0x008EAA59` → [MmUpdateMdlTracker](../../text/45/MmUpdateMdlTracker_function_00456468.md) (function, `0x00456468`)
- `0x008EAA92` → [IopExceptionCleanupEx](../8A/IopExceptionCleanupEx_function_008AE5C8.md) (function, `0x008AE5C8`)
- `0x008EAB09` → [EtwTimLogProhibitFsctlSystemCalls](../A8/EtwTimLogProhibitFsctlSystemCalls_function_00A81E18.md) (function, `0x00A81E18`)
- `0x008EAB6A` → [IoSetIoCompletionEx](../../text/24/IoSetIoCompletionEx_function_0024FA80.md) (function, `0x0024FA80`)
- `0x008EABB9` → [AstAddBloomFilter](../97/AstAddBloomFilter_function_0097CBF8.md) (function, `0x0097CBF8`)
- `0x008EABCC` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008EABF3` → [memcpy_s](../../text/50/memcpy_s_function_00505D40.md) (function, `0x00505D40`)
- `0x008EB03B` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x008EB065` → [IopWaitAndAcquireFileObjectLock](../8A/IopWaitAndAcquireFileObjectLock_function_008AE6D8.md) (function, `0x008AE6D8`)
- `0x008EB0A2` → [MmIsDriverVerifying](../../text/4A/MmIsDriverVerifying_function_004A8770.md) (function, `0x004A8770`)
- `0x008EB0B4` → [VfFastIoSnapState](../../pagevrfy/BB/VfFastIoSnapState_function_00BB97BC.md) (function, `0x00BB97BC`)
- `0x008EB133` → [IopExceptionCleanupEx](../8A/IopExceptionCleanupEx_function_008AE5C8.md) (function, `0x008AE5C8`)
- `0x008EB167` → [IoThreadToProcess](../../text/44/IoThreadToProcess_function_00448540.md) (function, `0x00448540`)
- `0x008EB17F` → [SeCaptureSubjectContextEx](../8C/SeCaptureSubjectContextEx_function_008C4C90.md) (function, `0x008C4C90`)
- `0x008EB190` → [RtlIsSandboxedToken](../8B/RtlIsSandboxedToken_function_008B3AB0.md) (function, `0x008B3AB0`)
- `0x008EB1A5` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x008EB1E4` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008EB1F8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008EB200` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008EB214` → [IopSetFileObjectExtensionFlag](../../text/43/IopSetFileObjectExtensionFlag_function_0043D710.md) (function, `0x0043D710`)
- `0x008EB228` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008EB2DB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008EB34C` → [IopValidateJunctionTarget](../71/IopValidateJunctionTarget_function_0071C808.md) (function, `0x0071C808`)
- `0x008EB3AF` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008EB3BC` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (function, `0x00250A90`)

### Direct callers
- [PfSnGetSectionObject](../8A/PfSnGetSectionObject_function_008A9448.md) at `0x008A9903`
- [PfSnPrefetchFileMetadata](../8A/PfSnPrefetchFileMetadata_function_008AA178.md) at `0x008AA25B`
- [NtFsControlFile](NtFsControlFile_function_008E9260.md) at `0x008E92B9`
- [NtDeviceIoControlFile](NtDeviceIoControlFile_function_008E9A60.md) at `0x008E9AB9`
- [PfpVolumePrefetchMetadata](../93/PfpVolumePrefetchMetadata_function_0093A158.md) at `0x0093A3AD`
- [PfpPrefetchDirectoryStream](../93/PfpPrefetchDirectoryStream_function_0093AA94.md) at `0x0093AC69`
- [PfpPrefetchEntireDirectory](../93/PfpPrefetchEntireDirectory_function_0093B0FC.md) at `0x0093B223`
- [NtCopyFileChunk](../94/NtCopyFileChunk_function_0094B600.md) at `0x0094B802`
- [sub_00B19EB2](../B1/Unknown_function_00B19EB2.md) at `0x00B19F3F`
- [sub_00B250B4](../B2/Unknown_function_00B250B4.md) at `0x00B25102`

### Static image references
- `0x008E9AEC` → RVA `0x00E0A740` (`.data`; read)
- `0x008E9D5A` → RVA `0x00FC6B80` (`ALMOSTRO`; read)
- `0x008E9E31` → RVA `0x00F8D058` (`.data`; read)
- `0x008E9E3E` → RVA `0x00E06F10` (`.data`; read)
- `0x008E9E8B` → RVA `0x00F8D040` (`.data`; read)
- `0x008E9E92` → RVA `0x00F8D050` (`.data`; read)
- `0x008E9F42` → RVA `0x00F8D048` (`.data`; read)
- `0x008EA0F7` → RVA `0x00FC5008` (`ALMOSTRO`; read)
- `0x008EA117` → RVA `0x00F04A20` (`.data`; read)
- `0x008EA12A` → RVA `0x008EC5B0` (`PiDaFastIoDispatch`; read)
- `0x008EA152` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x008EA166` → RVA `0x008EB3D0` (`PiCMFastIoDeviceDispatch`; read)
- `0x008EAA2C` → RVA `0x00FC6BBC` (`ALMOSTRO`; read)
- `0x008EAF36` → RVA `0x00E06F20` (`.data`; read)
- `0x008EB02D` → RVA `0x00046C06` (`.rdata`; read)
- `0x008EB2F3` → RVA `0x00E06F28` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **55**
  - `0x008E9CF3` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (`PAGE` → `.text`)
  - `0x008E9DAF` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (`PAGE` → `.text`)
  - `0x008E9E19` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (`PAGE` → `.text`)
  - `0x008EA0C4` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (`PAGE` → `.text`)
  - `0x008EA0D6` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008EA0DE` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008EA1DD` → [VfFastIoCheckState](../../pagevrfy/BB/VfFastIoCheckState_function_00BB9440.md) (`PAGE` → `PAGEVRFY`)
  - `0x008EA20A` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (`PAGE` → `.text`)
  - `0x008EA228` → [IopAllocateIrpExReturn](../../text/20/IopAllocateIrpExReturn_function_00207720.md) (`PAGE` → `.text`)
  - `0x008EA342` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008EA363` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008EA3EB` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008EA47E` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008EA53E` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008EA552` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008EA55F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008EA67B` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x008EA683` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008EA69A` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (`PAGE` → `.text`)
  - `0x008EA6BA` → [IopDecrementCompletionContextUsageCount](../../text/45/IopDecrementCompletionContextUsageCount_function_00452678.md) (`PAGE` → `.text`)
  - `0x008EA6C2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008EA6E7` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008EA723` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008EA751` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x008EA782` → [IoGetAttachedDevice](../../text/41/IoGetAttachedDevice_function_00410810.md) (`PAGE` → `.text`)
  - `0x008EA7B2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008EA7C9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008EA7ED` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008EA822` → [IoGetAttachedDevice](../../text/41/IoGetAttachedDevice_function_00410810.md) (`PAGE` → `.text`)
  - `0x008EA832` → [FsRtlGetSupportedFeatures](../../text/47/FsRtlGetSupportedFeatures_function_00473F20.md) (`PAGE` → `.text`)
  - `0x008EA874` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008EA8E7` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008EA8FE` → [IoGetRelatedDeviceObject](../../text/29/IoGetRelatedDeviceObject_function_0029B120.md) (`PAGE` → `.text`)
  - `0x008EA94D` → [IopIncrementCompletionContextUsageCountAndReadData](../../text/44/IopIncrementCompletionContextUsageCountAndReadData_function_00443C60.md) (`PAGE` → `.text`)
  - `0x008EA99A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008EA9B1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008EA9E7` → [IoAllocateMdl](../../text/29/IoAllocateMdl_function_0029EBF0.md) (`PAGE` → `.text`)
  - `0x008EAA05` → [RtlRaiseStatus](../../text/2F/RtlRaiseStatus_function_002F6A50.md) (`PAGE` → `.text`)
  - `0x008EAA27` → [MmProbeAndLockPages](../../text/23/MmProbeAndLockPages_function_0023B990.md) (`PAGE` → `.text`)
  - `0x008EAA59` → [MmUpdateMdlTracker](../../text/45/MmUpdateMdlTracker_function_00456468.md) (`PAGE` → `.text`)
  - `0x008EAB6A` → [IoSetIoCompletionEx](../../text/24/IoSetIoCompletionEx_function_0024FA80.md) (`PAGE` → `.text`)
  - `0x008EABCC` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008EABF3` → [memcpy_s](../../text/50/memcpy_s_function_00505D40.md) (`PAGE` → `.text`)
  - `0x008EB03B` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x008EB0A2` → [MmIsDriverVerifying](../../text/4A/MmIsDriverVerifying_function_004A8770.md) (`PAGE` → `.text`)
  - `0x008EB0B4` → [VfFastIoSnapState](../../pagevrfy/BB/VfFastIoSnapState_function_00BB97BC.md) (`PAGE` → `PAGEVRFY`)
  - `0x008EB167` → [IoThreadToProcess](../../text/44/IoThreadToProcess_function_00448540.md) (`PAGE` → `.text`)
  - `0x008EB1E4` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008EB1F8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008EB200` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008EB214` → [IopSetFileObjectExtensionFlag](../../text/43/IopSetFileObjectExtensionFlag_function_0043D710.md) (`PAGE` → `.text`)
  - `0x008EB228` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008EB2DB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008EB3AF` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008EB3BC` → [IopReleaseFileObjectLock](../../text/25/IopReleaseFileObjectLock_function_00250A90.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x008EB2D2` → [sub_00B1D806](../B1/Unknown_function_00B1D806.md) (`tail-transfer`)
  - `0x008EB2E1` → [sub_00B1D806](../B1/Unknown_function_00B1D806.md) (`tail-transfer`)
  - `0x008EB35C` → [sub_00B1D806 + 0x11](../B1/Unknown_function_00B1D806.md) (`tail-transfer`)
  - `0x008EB3A7` → [sub_00B1D806 + 0x11](../B1/Unknown_function_00B1D806.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008E9AD0  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
008E9AD5  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
008E9ADA  53                              push rbx
008E9ADB  56                              push rsi
008E9ADC  57                              push rdi
008E9ADD  41 54                           push r12
008E9ADF  41 55                           push r13
008E9AE1  41 56                           push r14
008E9AE3  41 57                           push r15
008E9AE5  48 81 EC 30 02 00 00            sub rsp, 0x230
008E9AEC  48 8B 05 4D 0C 52 00            mov rax, qword ptr [rip + 0x520c4d]
008E9AF3  48 33 C4                        xor rax, rsp
008E9AF6  48 89 84 24 20 02 00 00         mov qword ptr [rsp + 0x220], rax
008E9AFE  4C 8B EA                        mov r13, rdx
008E9B01  48 89 94 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rdx
008E9B09  4C 8B D1                        mov r10, rcx
008E9B0C  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
008E9B14  0F B6 9C 24 C0 02 00 00         movzx ebx, byte ptr [rsp + 0x2c0]
008E9B1C  88 5C 24 72                     mov byte ptr [rsp + 0x72], bl
008E9B20  48 89 94 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rdx
008E9B28  48 8B 84 24 90 02 00 00         mov rax, qword ptr [rsp + 0x290]
008E9B30  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
008E9B38  4C 8B 84 24 A0 02 00 00         mov r8, qword ptr [rsp + 0x2a0]
008E9B40  4C 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r8
008E9B48  8B 84 24 A8 02 00 00            mov eax, dword ptr [rsp + 0x2a8]
008E9B4F  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
008E9B53  48 8B 94 24 B0 02 00 00         mov rdx, qword ptr [rsp + 0x2b0]
008E9B5B  48 89 94 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdx
008E9B63  8B 84 24 B8 02 00 00            mov eax, dword ptr [rsp + 0x2b8]
008E9B6A  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
008E9B6E  45 33 F6                        xor r14d, r14d
008E9B71  4C 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r14
008E9B79  4C 89 B4 24 98 00 00 00         mov qword ptr [rsp + 0x98], r14
008E9B81  4C 89 B4 24 08 01 00 00         mov qword ptr [rsp + 0x108], r14
008E9B89  0F 57 C0                        xorps xmm0, xmm0
008E9B8C  0F 11 84 24 B8 00 00 00         movups xmmword ptr [rsp + 0xb8], xmm0
008E9B94  44 8B BC 24 98 02 00 00         mov r15d, dword ptr [rsp + 0x298]
008E9B9C  45 8B E7                        mov r12d, r15d
008E9B9F  41 83 E4 03                     and r12d, 3
008E9BA3  44 89 A4 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r12d
008E9BAB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008E9BB4  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
008E9BBC  0F B6 B0 32 02 00 00            movzx esi, byte ptr [rax + 0x232]
008E9BC3  40 88 74 24 52                  mov byte ptr [rsp + 0x52], sil
008E9BC8  40 84 F6                        test sil, sil
008E9BCB  0F 84 2B 0C 00 00               je 0x1408ea7fc
008E9BD1  84 DB                           test bl, bl
008E9BD3  0F 84 AC 0C 00 00               je 0x1408ea885
008E9BD9  40 84 F6                        test sil, sil
008E9BDC  0F 84 1A 0C 00 00               je 0x1408ea7fc
008E9BE2  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
008E9BEA  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
008E9BF4  49 3B CD                        cmp rcx, r13
008E9BF7  49 0F 43 CD                     cmovae rcx, r13
008E9BFB  8B 01                           mov eax, dword ptr [rcx]
008E9BFD  89 01                           mov dword ptr [rcx], eax
008E9BFF  45 85 E4                        test r12d, r12d
008E9C02  74 59                           je 0x1408e9c5d
008E9C04  8B 7C 24 68                     mov edi, dword ptr [rsp + 0x68]
008E9C08  89 7C 24 54                     mov dword ptr [rsp + 0x54], edi
008E9C0C  41 83 FC 03                     cmp r12d, 3
008E9C10  0F 84 B0 00 00 00               je 0x1408e9cc6
008E9C16  4D 85 C0                        test r8, r8
008E9C19  74 3B                           je 0x1408e9c56
008E9C1B  F6 84 24 C8 02 00 00 01         test byte ptr [rsp + 0x2c8], 1
008E9C23  0F 85 9D 00 00 00               jne 0x1408e9cc6
008E9C29  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
008E9C2D  85 C0                           test eax, eax
008E9C2F  0F 84 91 00 00 00               je 0x1408e9cc6
008E9C35  49 8D 0C 00                     lea rcx, [r8 + rax]
008E9C39  49 3B CD                        cmp rcx, r13
008E9C3C  77 09                           ja 0x1408e9c47
008E9C3E  49 3B C8                        cmp rcx, r8
008E9C41  0F 83 7F 00 00 00               jae 0x1408e9cc6
008E9C47  41 0F B6 45 00                  movzx eax, byte ptr [r13]
008E9C4C  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
008E9C50  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
008E9C54  EB 70                           jmp 0x1408e9cc6
008E9C56  44 89 74 24 60                  mov dword ptr [rsp + 0x60], r14d
008E9C5B  EB 69                           jmp 0x1408e9cc6
008E9C5D  48 85 D2                        test rdx, rdx
008E9C60  74 4F                           je 0x1408e9cb1
008E9C62  8B 7C 24 68                     mov edi, dword ptr [rsp + 0x68]
008E9C66  89 7C 24 54                     mov dword ptr [rsp + 0x54], edi
008E9C6A  85 FF                           test edi, edi
008E9C6C  74 3D                           je 0x1408e9cab
008E9C6E  48 8B C2                        mov rax, rdx
008E9C71  4C 8D 4F FF                     lea r9, [rdi - 1]
008E9C75  4C 03 CA                        add r9, rdx
008E9C78  49 3B D1                        cmp rdx, r9
008E9C7B  77 43                           ja 0x1408e9cc0
008E9C7D  4D 3B CD                        cmp r9, r13
008E9C80  73 3E                           jae 0x1408e9cc0
008E9C82  49 81 E1 00 F0 FF FF            and r9, 0xfffffffffffff000
008E9C89  49 81 C1 00 10 00 00            add r9, 0x1000
008E9C90  0F B6 08                        movzx ecx, byte ptr [rax]
008E9C93  88 08                           mov byte ptr [rax], cl
008E9C95  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
008E9C9B  48 05 00 10 00 00               add rax, 0x1000
008E9CA1  49 3B C1                        cmp rax, r9
008E9CA4  75 EA                           jne 0x1408e9c90
008E9CA6  E9 59 FF FF FF                  jmp 0x1408e9c04
008E9CAB  90                              nop
008E9CAC  E9 5B FF FF FF                  jmp 0x1408e9c0c
008E9CB1  44 89 74 24 54                  mov dword ptr [rsp + 0x54], r14d
008E9CB6  44 89 74 24 68                  mov dword ptr [rsp + 0x68], r14d
008E9CBB  E9 4C FF FF FF                  jmp 0x1408e9c0c
008E9CC0  E8 7B F5 FF FF                  call 0x1408e9240
008E9CC5  CC                              int3
008E9CC6  4C 8B AC 24 D8 00 00 00         mov r13, qword ptr [rsp + 0xd8]
008E9CCE  EB 05                           jmp 0x1408e9cd5
008E9CD0  E9 9E 07 00 00                  jmp 0x1408ea473
008E9CD5  48 8D 84 24 08 01 00 00         lea rax, [rsp + 0x108]
008E9CDD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008E9CE2  4C 8D 8C 24 88 00 00 00         lea r9, [rsp + 0x88]
008E9CEA  44 0F B6 C6                     movzx r8d, sil
008E9CEE  33 D2                           xor edx, edx
008E9CF0  49 8B CA                        mov rcx, r10
008E9CF3  E8 38 38 9B FF                  call 0x14029d530
008E9CF8  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
008E9CFC  85 C0                           test eax, eax
008E9CFE  0F 88 6F 07 00 00               js 0x1408ea473
008E9D04  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
008E9D0C  48 83 BF B0 00 00 00 00         cmp qword ptr [rdi + 0xb0], 0
008E9D14  0F 85 BE 0A 00 00               jne 0x1408ea7d8
008E9D1A  40 84 F6                        test sil, sil
008E9D1D  74 0F                           je 0x1408e9d2e
008E9D1F  41 8B CF                        mov ecx, r15d
008E9D22  C1 E9 0E                        shr ecx, 0xe
008E9D25  83 E1 03                        and ecx, 3
008E9D28  0F 85 A5 09 00 00               jne 0x1408ea6d3
008E9D2E  41 81 FF 64 42 09 00            cmp r15d, 0x94264
008E9D35  0F 84 CE 0A 00 00               je 0x1408ea809
008E9D3B  41 81 FF 68 82 09 00            cmp r15d, 0x98268
008E9D42  0F 84 C1 0A 00 00               je 0x1408ea809
008E9D48  41 81 FF 2C 04 09 00            cmp r15d, 0x9042c
008E9D4F  0F 84 B7 14 00 00               je 0x1408eb20c
008E9D55  4D 85 ED                        test r13, r13
008E9D58  74 5A                           je 0x1408e9db4
008E9D5A  4C 8B 05 1F CE 6D 00            mov r8, qword ptr [rip + 0x6dce1f]
008E9D61  4C 89 B4 24 10 01 00 00         mov qword ptr [rsp + 0x110], r14
008E9D69  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
008E9D6E  48 8D 84 24 10 01 00 00         lea rax, [rsp + 0x110]
008E9D76  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008E9D7B  44 0F B6 CE                     movzx r9d, sil
008E9D7F  BA 02 00 00 00                  mov edx, 2
008E9D84  49 8B CD                        mov rcx, r13
008E9D87  E8 24 F0 F7 FF                  call 0x140868db0
008E9D8C  44 8B E8                        mov r13d, eax
008E9D8F  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
008E9D93  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
008E9D9B  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
008E9DA3  45 85 ED                        test r13d, r13d
008E9DA6  0F 88 38 0B 00 00               js 0x1408ea8e4
008E9DAC  48 8B C8                        mov rcx, rax
008E9DAF  E8 9C E5 95 FF                  call 0x140248350
008E9DB4  4C 89 B4 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r14
008E9DBC  C6 44 24 51 00                  mov byte ptr [rsp + 0x51], 0
008E9DC1  45 32 C0                        xor r8b, r8b
008E9DC4  44 88 44 24 58                  mov byte ptr [rsp + 0x58], r8b
008E9DC9  40 84 F6                        test sil, sil
008E9DCC  74 1F                           je 0x1408e9ded
008E9DCE  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
008E9DD3  41 81 FF A4 00 09 00            cmp r15d, 0x900a4
008E9DDA  0F 84 56 14 00 00               je 0x1408eb236
008E9DE0  41 81 FF 0C 04 09 00            cmp r15d, 0x9040c
008E9DE7  0F 84 55 13 00 00               je 0x1408eb142
008E9DED  44 8B 6F 50                     mov r13d, dword ptr [rdi + 0x50]
008E9DF1  41 F6 C5 02                     test r13b, 2
008E9DF5  0F 85 FB 08 00 00               jne 0x1408ea6f6
008E9DFB  C6 44 24 50 00                  mov byte ptr [rsp + 0x50], 0
008E9E00  40 84 F6                        test sil, sil
008E9E03  0F 85 A8 06 00 00               jne 0x1408ea4b1
008E9E09  F7 47 50 00 08 00 00            test dword ptr [rdi + 0x50], 0x800
008E9E10  0F 85 68 09 00 00               jne 0x1408ea77e
008E9E16  48 8B CF                        mov rcx, rdi
008E9E19  E8 02 13 9B FF                  call 0x14029b120
008E9E1E  4C 8B D8                        mov r11, rax
008E9E21  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
008E9E29  84 DB                           test bl, bl
008E9E2B  0F 84 BE 03 00 00               je 0x1408ea1ef
008E9E31  80 3D 20 32 6A 00 00            cmp byte ptr [rip + 0x6a3220], 0
008E9E38  0F 84 5D 01 00 00               je 0x1408e9f9b
008E9E3E  83 3D CB D0 51 00 00            cmp dword ptr [rip + 0x51d0cb], 0
008E9E45  0F 87 A9 0A 00 00               ja 0x1408ea8f4
008E9E4B  32 C0                           xor al, al
008E9E4D  84 C0                           test al, al
008E9E4F  0F 84 46 01 00 00               je 0x1408e9f9b
008E9E55  4D 8D 6B D0                     lea r13, [r11 - 0x30]
008E9E59  41 0F B6 45 1A                  movzx eax, byte ptr [r13 + 0x1a]
008E9E5E  A8 02                           test al, 2
008E9E60  0F 85 31 06 00 00               jne 0x1408ea497
008E9E66  4D 8B EE                        mov r13, r14
008E9E69  4D 85 ED                        test r13, r13
008E9E6C  0F 84 29 01 00 00               je 0x1408e9f9b
008E9E72  45 8B D7                        mov r10d, r15d
008E9E75  49 C1 E2 20                     shl r10, 0x20
008E9E79  49 8B C3                        mov rax, r11
008E9E7C  48 C1 E8 04                     shr rax, 4
008E9E80  4C 33 D0                        xor r10, rax
008E9E83  4C 89 94 24 60 01 00 00         mov qword ptr [rsp + 0x160], r10
008E9E8B  44 8B 0D AE 31 6A 00            mov r9d, dword ptr [rip + 0x6a31ae]
008E9E92  8B 05 B8 31 6A 00               mov eax, dword ptr [rip + 0x6a31b8]
008E9E98  48 6B C8 25                     imul rcx, rax, 0x25
008E9E9C  41 0F B6 C2                     movzx eax, r10b
008E9EA0  48 03 C8                        add rcx, rax
008E9EA3  48 6B D1 25                     imul rdx, rcx, 0x25
008E9EA7  49 8B C2                        mov rax, r10
008E9EAA  48 C1 E8 08                     shr rax, 8
008E9EAE  0F B6 C0                        movzx eax, al
008E9EB1  48 03 D0                        add rdx, rax
008E9EB4  48 6B CA 25                     imul rcx, rdx, 0x25
008E9EB8  49 8B C2                        mov rax, r10
008E9EBB  48 C1 E8 10                     shr rax, 0x10
008E9EBF  0F B6 C0                        movzx eax, al
008E9EC2  48 03 C8                        add rcx, rax
008E9EC5  48 6B D1 25                     imul rdx, rcx, 0x25
008E9EC9  49 8B C2                        mov rax, r10
008E9ECC  48 C1 E8 18                     shr rax, 0x18
008E9ED0  0F B6 C0                        movzx eax, al
008E9ED3  48 03 D0                        add rdx, rax
008E9ED6  48 6B CA 25                     imul rcx, rdx, 0x25
008E9EDA  49 8B C2                        mov rax, r10
008E9EDD  48 C1 E8 20                     shr rax, 0x20
008E9EE1  0F B6 C0                        movzx eax, al
008E9EE4  48 03 C8                        add rcx, rax
008E9EE7  48 6B D1 25                     imul rdx, rcx, 0x25
008E9EEB  49 8B C2                        mov rax, r10
008E9EEE  48 C1 E8 28                     shr rax, 0x28
008E9EF2  0F B6 C0                        movzx eax, al
008E9EF5  48 03 D0                        add rdx, rax
008E9EF8  48 6B CA 25                     imul rcx, rdx, 0x25
008E9EFC  49 8B C2                        mov rax, r10
008E9EFF  48 C1 E8 30                     shr rax, 0x30
008E9F03  0F B6 C0                        movzx eax, al
008E9F06  48 03 C8                        add rcx, rax
008E9F09  4C 6B C1 25                     imul r8, rcx, 0x25
008E9F0D  49 8B CA                        mov rcx, r10
008E9F10  48 C1 E9 38                     shr rcx, 0x38
008E9F14  4C 03 C1                        add r8, rcx
008E9F17  41 8B C0                        mov eax, r8d
008E9F1A  C1 E8 10                        shr eax, 0x10
008E9F1D  33 D2                           xor edx, edx
008E9F1F  41 F7 F1                        div r9d
008E9F22  89 94 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], edx
008E9F29  33 D2                           xor edx, edx
008E9F2B  49 8B C2                        mov rax, r10
008E9F2E  49 F7 F1                        div r9
008E9F31  4C 8B D2                        mov r10, rdx
008E9F34  33 D2                           xor edx, edx
008E9F36  41 8B C0                        mov eax, r8d
008E9F39  41 F7 F1                        div r9d
008E9F3C  8B C2                           mov eax, edx
008E9F3E  48 C1 E8 03                     shr rax, 3
008E9F42  4C 8B 05 FF 30 6A 00            mov r8, qword ptr [rip + 0x6a30ff]
008E9F49  83 E2 07                        and edx, 7
008E9F4C  42 0F B6 04 00                  movzx eax, byte ptr [rax + r8]
008E9F51  0F B6 CA                        movzx ecx, dl
008E9F54  D2 F8                           sar al, cl
008E9F56  A8 01                           test al, 1
008E9F58  0F 84 55 0C 00 00               je 0x1408eabb3
008E9F5E  8B 8C 24 A0 00 00 00            mov ecx, dword ptr [rsp + 0xa0]
008E9F65  8B C1                           mov eax, ecx
008E9F67  48 C1 E8 03                     shr rax, 3
008E9F6B  83 E1 07                        and ecx, 7
008E9F6E  42 0F B6 04 00                  movzx eax, byte ptr [rax + r8]
008E9F73  D2 F8                           sar al, cl
008E9F75  A8 01                           test al, 1
008E9F77  0F 84 36 0C 00 00               je 0x1408eabb3
008E9F7D  41 8B C2                        mov eax, r10d
008E9F80  48 C1 E8 03                     shr rax, 3
008E9F84  41 83 E2 07                     and r10d, 7
008E9F88  42 0F B6 04 00                  movzx eax, byte ptr [rax + r8]
008E9F8D  41 0F B6 CA                     movzx ecx, r10b
008E9F91  D2 F8                           sar al, cl
008E9F93  A8 01                           test al, 1
008E9F95  0F 84 18 0C 00 00               je 0x1408eabb3
008E9F9B  84 DB                           test bl, bl
008E9F9D  0F 84 4C 02 00 00               je 0x1408ea1ef
008E9FA3  80 7C 24 51 00                  cmp byte ptr [rsp + 0x51], 0
008E9FA8  0F 85 41 02 00 00               jne 0x1408ea1ef
008E9FAE  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
008E9FB6  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
008E9FBA  4C 8B 50 50                     mov r10, qword ptr [rax + 0x50]
008E9FBE  4D 85 D2                        test r10, r10
008E9FC1  0F 84 28 02 00 00               je 0x1408ea1ef
008E9FC7  4D 8B 52 50                     mov r10, qword ptr [r10 + 0x50]
008E9FCB  4C 89 94 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r10
008E9FD3  4D 85 D2                        test r10, r10
008E9FD6  0F 84 13 02 00 00               je 0x1408ea1ef
008E9FDC  40 84 F6                        test sil, sil
008E9FDF  0F 84 05 01 00 00               je 0x1408ea0ea
008E9FE5  48 8B 94 24 B0 00 00 00         mov rdx, qword ptr [rsp + 0xb0]
008E9FED  48 85 D2                        test rdx, rdx
008E9FF0  0F 84 F4 00 00 00               je 0x1408ea0ea
008E9FF6  41 83 FC 01                     cmp r12d, 1
008E9FFA  0F 84 7B 00 00 00               je 0x1408ea07b
008EA000  41 83 FC 02                     cmp r12d, 2
008EA004  0F 85 A4 00 00 00               jne 0x1408ea0ae
008EA00A  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
008EA00E  44 8B C0                        mov r8d, eax
008EA011  85 C0                           test eax, eax
008EA013  74 5D                           je 0x1408ea072
008EA015  48 8B CA                        mov rcx, rdx
008EA018  49 FF C8                        dec r8
008EA01B  4C 03 C2                        add r8, rdx
008EA01E  49 3B D0                        cmp rdx, r8
008EA021  77 52                           ja 0x1408ea075
008EA023  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
008EA02D  4C 3B C0                        cmp r8, rax
008EA030  73 43                           jae 0x1408ea075
008EA032  49 81 E0 00 F0 FF FF            and r8, 0xfffffffffffff000
008EA039  49 81 C0 00 10 00 00            add r8, 0x1000
008EA040  0F B6 01                        movzx eax, byte ptr [rcx]
008EA043  88 01                           mov byte ptr [rcx], al
008EA045  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
008EA04C  48 81 C1 00 10 00 00            add rcx, 0x1000
008EA053  49 3B C8                        cmp rcx, r8
008EA056  75 E8                           jne 0x1408ea040
008EA058  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
008EA060  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
008EA064  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
008EA068  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
008EA070  EB 3C                           jmp 0x1408ea0ae
008EA072  90                              nop
008EA073  EB 39                           jmp 0x1408ea0ae
008EA075  E8 C6 F1 FF FF                  call 0x1408e9240
008EA07A  CC                              int3
008EA07B  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
008EA07F  85 C0                           test eax, eax
008EA081  74 2B                           je 0x1408ea0ae
008EA083  4C 8D 04 02                     lea r8, [rdx + rax]
008EA087  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
008EA091  4C 3B C2                        cmp r8, rdx
008EA094  72 05                           jb 0x1408ea09b
008EA096  4C 3B C0                        cmp r8, rax
008EA099  76 13                           jbe 0x1408ea0ae
008EA09B  0F B6 00                        movzx eax, byte ptr [rax]
008EA09E  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
008EA0A6  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
008EA0AA  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
008EA0AE  EB 3A                           jmp 0x1408ea0ea
008EA0B0  8B F8                           mov edi, eax
008EA0B2  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
008EA0BA  80 7C 24 50 00                  cmp byte ptr [rsp + 0x50], 0
008EA0BF  74 08                           je 0x1408ea0c9
008EA0C1  48 8B CB                        mov rcx, rbx
008EA0C4  E8 C7 69 96 FF                  call 0x140250a90
008EA0C9  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
008EA0D1  48 85 C9                        test rcx, rcx
008EA0D4  74 05                           je 0x1408ea0db
008EA0D6  E8 75 F2 A0 FF                  call 0x1402f9350
008EA0DB  48 8B CB                        mov rcx, rbx
008EA0DE  E8 6D F2 A0 FF                  call 0x1402f9350
008EA0E3  8B C7                           mov eax, edi
008EA0E5  E9 89 03 00 00                  jmp 0x1408ea473
008EA0EA  41 81 FF 20 00 09 00            cmp r15d, 0x90020
008EA0F1  0F 85 E3 07 00 00               jne 0x1408ea8da
008EA0F7  48 8B 05 0A AF 6D 00            mov rax, qword ptr [rip + 0x6daf0a]
008EA0FE  F0 FF 80 DC 02 00 00            lock inc dword ptr [rax + 0x2dc]
008EA105  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
008EA10D  44 8B 6C 24 68                  mov r13d, dword ptr [rsp + 0x68]
008EA112  44 89 6C 24 54                  mov dword ptr [rsp + 0x54], r13d
008EA117  8B 05 03 A9 61 00               mov eax, dword ptr [rip + 0x61a903]
008EA11D  A8 10                           test al, 0x10
008EA11F  0F 85 71 0F 00 00               jne 0x1408eb096
008EA125  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
008EA12A  48 8D 05 7F 24 00 00            lea rax, [rip + 0x247f]
008EA131  4C 3B D0                        cmp r10, rax
008EA134  0F 85 27 12 00 00               jne 0x1408eb361
008EA13A  32 C9                           xor cl, cl
008EA13C  88 4C 24 52                     mov byte ptr [rsp + 0x52], cl
008EA140  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
008EA144  48 83 F8 05                     cmp rax, 5
008EA148  0F 83 7F 00 00 00               jae 0x1408ea1cd
008EA14E  48 8D 04 40                     lea rax, [rax + rax*2]
008EA152  4C 8D 1D A7 5E 71 FF            lea r11, [rip - 0x8ea159]
008EA159  4D 8B 9C C3 A0 19 00 00         mov r11, qword ptr [r11 + rax*8 + 0x19a0]
008EA161  4D 85 DB                        test r11, r11
008EA164  74 67                           je 0x1408ea1cd
008EA166  48 8D 05 63 12 00 00            lea rax, [rip + 0x1263]
008EA16D  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
008EA172  4C 8B 84 24 A8 00 00 00         mov r8, qword ptr [rsp + 0xa8]
008EA17A  B2 01                           mov dl, 1
008EA17C  48 8B CF                        mov rcx, rdi
008EA17F  4C 3B D8                        cmp r11, rax
008EA182  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
008EA18A  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008EA18F  48 8D 84 24 B8 00 00 00         lea rax, [rsp + 0xb8]
008EA197  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008EA19C  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
008EA1A1  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
008EA1A9  44 89 6C 24 28                  mov dword ptr [rsp + 0x28], r13d
008EA1AE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008EA1B3  0F 85 A0 11 00 00               jne 0x1408eb359
008EA1B9  E8 12 12 00 00                  call 0x1408eb3d0
008EA1BE  0F B6 C8                        movzx ecx, al
008EA1C1  88 44 24 52                     mov byte ptr [rsp + 0x52], al
008EA1C5  4C 8B 94 24 A0 00 00 00         mov r10, qword ptr [rsp + 0xa0]
008EA1CD  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
008EA1D2  48 85 C0                        test rax, rax
008EA1D5  74 10                           je 0x1408ea1e7
008EA1D7  49 8B D2                        mov rdx, r10
008EA1DA  48 8B C8                        mov rcx, rax
008EA1DD  E8 5E F2 2C 00                  call 0x140bb9440
008EA1E2  0F B6 4C 24 52                  movzx ecx, byte ptr [rsp + 0x52]
008EA1E7  84 C9                           test cl, cl
008EA1E9  0F 85 BB 03 00 00               jne 0x1408ea5aa
008EA1EF  48 8D 47 50                     lea rax, [rdi + 0x50]
008EA1F3  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
008EA1FB  F7 00 00 00 00 04               test dword ptr [rax], 0x4000000
008EA201  75 0C                           jne 0x1408ea20f
008EA203  48 8D 8F 98 00 00 00            lea rcx, [rdi + 0x98]
008EA20A  E8 41 E1 95 FF                  call 0x140248350
008EA20F  44 0F B6 44 24 50               movzx r8d, byte ptr [rsp + 0x50]
008EA215  41 80 F0 01                     xor r8b, 1
008EA219  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
008EA221  0F B6 50 4C                     movzx edx, byte ptr [rax + 0x4c]
008EA225  48 8B C8                        mov rcx, rax
008EA228  E8 F3 D4 91 FF                  call 0x140207720
008EA22D  4C 8B E8                        mov r13, rax
008EA230  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
008EA238  48 85 C0                        test rax, rax
008EA23B  0F 84 4B 05 00 00               je 0x1408ea78c
008EA241  48 89 B8 C0 00 00 00            mov qword ptr [rax + 0xc0], rdi
008EA248  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
008EA250  49 89 85 98 00 00 00            mov qword ptr [r13 + 0x98], rax
008EA257  4D 89 B5 A0 00 00 00            mov qword ptr [r13 + 0xa0], r14
008EA25E  41 88 75 40                     mov byte ptr [r13 + 0x40], sil
008EA262  41 C6 45 41 00                  mov byte ptr [r13 + 0x41], 0
008EA267  41 C6 45 44 00                  mov byte ptr [r13 + 0x44], 0
008EA26C  4D 89 75 68                     mov qword ptr [r13 + 0x68], r14
008EA270  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
008EA278  49 89 45 50                     mov qword ptr [r13 + 0x50], rax
008EA27C  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
008EA284  49 89 45 48                     mov qword ptr [r13 + 0x48], rax
008EA288  48 8B 84 24 80 02 00 00         mov rax, qword ptr [rsp + 0x280]
008EA290  49 89 45 58                     mov qword ptr [r13 + 0x58], rax
008EA294  48 8B 94 24 88 02 00 00         mov rdx, qword ptr [rsp + 0x288]
008EA29C  49 89 55 60                     mov qword ptr [r13 + 0x60], rdx
008EA2A0  49 8B 95 B8 00 00 00            mov rdx, qword ptr [r13 + 0xb8]
008EA2A7  48 83 EA 48                     sub rdx, 0x48
008EA2AB  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
008EA2B0  41 8B C6                        mov eax, r14d
008EA2B3  44 0F B6 44 24 72               movzx r8d, byte ptr [rsp + 0x72]
008EA2B9  45 84 C0                        test r8b, r8b
008EA2BC  0F 95 C0                        setne al
008EA2BF  83 C0 0D                        add eax, 0xd
008EA2C2  89 02                           mov dword ptr [rdx], eax
008EA2C4  48 89 7A 30                     mov qword ptr [rdx + 0x30], rdi
008EA2C8  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
008EA2CC  89 42 08                        mov dword ptr [rdx + 8], eax
008EA2CF  8B 4C 24 60                     mov ecx, dword ptr [rsp + 0x60]
008EA2D3  89 4A 10                        mov dword ptr [rdx + 0x10], ecx
008EA2D6  44 89 7A 18                     mov dword ptr [rdx + 0x18], r15d
008EA2DA  4D 89 75 08                     mov qword ptr [r13 + 8], r14
008EA2DE  4D 89 75 18                     mov qword ptr [r13 + 0x18], r14
008EA2E2  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
008EA2EA  F7 40 30 00 00 08 00            test dword ptr [rax + 0x30], 0x80000
008EA2F1  0F 85 8C 0D 00 00               jne 0x1408eb083
008EA2F7  45 85 E4                        test r12d, r12d
008EA2FA  0F 85 6B 02 00 00               jne 0x1408ea56b
008EA300  4C 89 72 20                     mov qword ptr [rdx + 0x20], r14
008EA304  44 8B 64 24 54                  mov r12d, dword ptr [rsp + 0x54]
008EA309  85 C9                           test ecx, ecx
008EA30B  75 09                           jne 0x1408ea316
008EA30D  45 85 E4                        test r12d, r12d
008EA310  0F 84 84 00 00 00               je 0x1408ea39a
008EA316  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
008EA31E  48 85 C0                        test rax, rax
008EA321  75 71                           jne 0x1408ea394
008EA323  41 8B D4                        mov edx, r12d
008EA326  41 3B CC                        cmp ecx, r12d
008EA329  0F 47 D1                        cmova edx, ecx
008EA32C  B9 69 00 00 00                  mov ecx, 0x69
008EA331  B8 61 00 00 00                  mov eax, 0x61
008EA336  45 84 C0                        test r8b, r8b
008EA339  0F 44 C8                        cmove ecx, eax
008EA33C  41 B8 49 6F 53 42               mov r8d, 0x42536f49
008EA342  E8 A9 7D 29 00                  call 0x140b820f0
008EA347  48 8B C8                        mov rcx, rax
008EA34A  49 89 45 18                     mov qword ptr [r13 + 0x18], rax
008EA34E  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
008EA356  48 85 C0                        test rax, rax
008EA359  74 0D                           je 0x1408ea368
008EA35B  44 8B 44 24 60                  mov r8d, dword ptr [rsp + 0x60]
008EA360  48 8B D0                        mov rdx, rax
008EA363  E8 D8 C4 DD FF                  call 0x1406c6840
008EA368  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
008EA36D  8B 4C 24 60                     mov ecx, dword ptr [rsp + 0x60]
008EA371  41 C7 45 10 30 00 00 00         mov dword ptr [r13 + 0x10], 0x30
008EA379  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
008EA381  49 89 45 70                     mov qword ptr [r13 + 0x70], rax
008EA385  45 85 E4                        test r12d, r12d
008EA388  74 18                           je 0x1408ea3a2
008EA38A  41 C7 45 10 70 00 00 00         mov dword ptr [r13 + 0x10], 0x70
008EA392  EB 0E                           jmp 0x1408ea3a2
008EA394  49 89 45 18                     mov qword ptr [r13 + 0x18], rax
008EA398  EB D7                           jmp 0x1408ea371
008EA39A  45 89 75 10                     mov dword ptr [r13 + 0x10], r14d
008EA39E  4D 89 75 70                     mov qword ptr [r13 + 0x70], r14
008EA3A2  EB 36                           jmp 0x1408ea3da
008EA3A4  8B D8                           mov ebx, eax
008EA3A6  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
008EA3AE  0F B6 51 50                     movzx edx, byte ptr [rcx + 0x50]
008EA3B2  D1 EA                           shr edx, 1
008EA3B4  83 E2 01                        and edx, 1
008EA3B7  88 54 24 20                     mov byte ptr [rsp + 0x20], dl
008EA3BB  45 33 C9                        xor r9d, r9d
008EA3BE  4C 8B 84 24 98 00 00 00         mov r8, qword ptr [rsp + 0x98]
008EA3C6  48 8B 94 24 D8 00 00 00         mov rdx, qword ptr [rsp + 0xd8]
008EA3CE  E8 F5 41 FC FF                  call 0x1408ae5c8
008EA3D3  8B C3                           mov eax, ebx
008EA3D5  E9 99 00 00 00                  jmp 0x1408ea473
008EA3DA  41 3B CC                        cmp ecx, r12d
008EA3DD  73 16                           jae 0x1408ea3f5
008EA3DF  44 2B E1                        sub r12d, ecx
008EA3E2  45 8B C4                        mov r8d, r12d
008EA3E5  49 03 4D 18                     add rcx, qword ptr [r13 + 0x18]
008EA3E9  33 D2                           xor edx, edx
008EA3EB  E8 50 C8 DD FF                  call 0x1406c6c40
008EA3F0  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
008EA3F5  8B 84 24 0C 01 00 00            mov eax, dword ptr [rsp + 0x10c]
008EA3FC  0F B6 C8                        movzx ecx, al
008EA3FF  80 E1 02                        and cl, 2
008EA402  02 C9                           add cl, cl
008EA404  24 01                           and al, 1
008EA406  0A C8                           or cl, al
008EA408  08 4A 02                        or byte ptr [rdx + 2], cl
008EA40B  84 DB                           test bl, bl
008EA40D  75 08                           jne 0x1408ea417
008EA40F  41 81 4D 10 00 08 00 00         or dword ptr [r13 + 0x10], 0x800
008EA417  41 81 FF 20 00 09 00            cmp r15d, 0x90020
008EA41E  75 16                           jne 0x1408ea436
008EA420  48 8B 05 E1 AB 6D 00            mov rax, qword ptr [rip + 0x6dabe1]
008EA427  F0 FF 80 DC 02 00 00            lock inc dword ptr [rax + 0x2dc]
008EA42E  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
008EA436  80 7C 24 51 00                  cmp byte ptr [rsp + 0x51], 0
008EA43B  0F 85 A7 0C 00 00               jne 0x1408eb0e8
008EA441  80 7C 24 72 00                  cmp byte ptr [rsp + 0x72], 0
008EA446  41 0F 94 C1                     sete r9b
008EA44A  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
008EA452  0F B6 44 24 50                  movzx eax, byte ptr [rsp + 0x50]
008EA457  88 44 24 28                     mov byte ptr [rsp + 0x28], al
008EA45B  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
008EA460  4C 8B C7                        mov r8, rdi
008EA463  49 8B D5                        mov rdx, r13
008EA466  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
008EA46E  E8 CD 0F 00 00                  call 0x1408eb440
008EA473  48 8B 8C 24 20 02 00 00         mov rcx, qword ptr [rsp + 0x220]
008EA47B  48 33 CC                        xor rcx, rsp
008EA47E  E8 BD 21 DC FF                  call 0x1406ac640
008EA483  48 81 C4 30 02 00 00            add rsp, 0x230
008EA48A  41 5F                           pop r15
008EA48C  41 5E                           pop r14
008EA48E  41 5D                           pop r13
008EA490  41 5C                           pop r12
008EA492  5F                              pop rdi
008EA493  5E                              pop rsi
008EA494  5B                              pop rbx
008EA495  C3                              ret
008EA496  CC                              int3
008EA497  83 E0 03                        and eax, 3
008EA49A  48 8D 0D 5F 5B 71 FF            lea rcx, [rip - 0x8ea4a1]
008EA4A1  0F B6 84 08 80 FF F0 00         movzx eax, byte ptr [rax + rcx + 0xf0ff80]
008EA4A9  4C 2B E8                        sub r13, rax
008EA4AC  E9 B8 F9 FF FF                  jmp 0x1408e9e69
008EA4B1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008EA4BA  48 89 84 24 58 01 00 00         mov qword ptr [rsp + 0x158], rax
008EA4C2  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
008EA4C9  48 83 B9 10 03 00 00 00         cmp qword ptr [rcx + 0x310], 0
008EA4D1  74 47                           je 0x1408ea51a
008EA4D3  0F B7 81 EC 06 00 00            movzx eax, word ptr [rcx + 0x6ec]
008EA4DA  B9 4C 01 00 00                  mov ecx, 0x14c
008EA4DF  66 3B C1                        cmp ax, cx
008EA4E2  75 2C                           jne 0x1408ea510
008EA4E4  48 8B 94 24 80 02 00 00         mov rdx, qword ptr [rsp + 0x280]
008EA4EC  48 83 CA 01                     or rdx, 1
008EA4F0  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
008EA4F8  8B 08                           mov ecx, dword ptr [rax]
008EA4FA  8B 01                           mov eax, dword ptr [rcx]
008EA4FC  89 01                           mov dword ptr [rcx], eax
008EA4FE  48 89 8C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rcx
008EA506  48 89 94 24 80 02 00 00         mov qword ptr [rsp + 0x280], rdx
008EA50E  EB 0A                           jmp 0x1408ea51a
008EA510  B9 C4 01 00 00                  mov ecx, 0x1c4
008EA515  66 3B C1                        cmp ax, cx
008EA518  74 CA                           je 0x1408ea4e4
008EA51A  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
008EA522  8B 4C 24 68                     mov ecx, dword ptr [rsp + 0x68]
008EA526  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
008EA52A  E9 DA F8 FF FF                  jmp 0x1408e9e09
008EA52F  8B D8                           mov ebx, eax
008EA531  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
008EA539  48 85 C9                        test rcx, rcx
008EA53C  74 05                           je 0x1408ea543
008EA53E  E8 0D EE A0 FF                  call 0x1402f9350
008EA543  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
008EA54B  48 85 C9                        test rcx, rcx
008EA54E  74 07                           je 0x1408ea557
008EA550  33 D2                           xor edx, edx
008EA552  E8 19 83 29 00                  call 0x140b82870
008EA557  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
008EA55F  E8 EC ED A0 FF                  call 0x1402f9350
008EA564  8B C3                           mov eax, ebx
008EA566  E9 08 FF FF FF                  jmp 0x1408ea473
008EA56B  41 8B C4                        mov eax, r12d
008EA56E  83 E8 01                        sub eax, 1
008EA571  0F 84 F0 03 00 00               je 0x1408ea967
008EA577  83 E8 01                        sub eax, 1
008EA57A  0F 84 E7 03 00 00               je 0x1408ea967
008EA580  83 F8 01                        cmp eax, 1
008EA583  0F 85 6C FE FF FF               jne 0x1408ea3f5
008EA589  45 89 75 10                     mov dword ptr [r13 + 0x10], r14d
008EA58D  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
008EA595  49 89 45 70                     mov qword ptr [r13 + 0x70], rax
008EA599  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
008EA5A1  48 89 42 20                     mov qword ptr [rdx + 0x20], rax
008EA5A5  E9 4B FE FF FF                  jmp 0x1408ea3f5
008EA5AA  49 8B F6                        mov rsi, r14
008EA5AD  4C 89 B4 24 00 01 00 00         mov qword ptr [rsp + 0x100], r14
008EA5B5  4C 89 B4 24 18 01 00 00         mov qword ptr [rsp + 0x118], r14
008EA5BD  C6 44 24 71 00                  mov byte ptr [rsp + 0x71], 0
008EA5C2  F6 84 24 80 02 00 00 01         test byte ptr [rsp + 0x280], 1
008EA5CA  75 15                           jne 0x1408ea5e1
008EA5CC  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
008EA5D4  0F 10 84 24 B8 00 00 00         movups xmm0, xmmword ptr [rsp + 0xb8]
008EA5DC  0F 11 00                        movups xmmword ptr [rax], xmm0
008EA5DF  EB 1B                           jmp 0x1408ea5fc
008EA5E1  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
008EA5E8  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
008EA5F0  89 41 04                        mov dword ptr [rcx + 4], eax
008EA5F3  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
008EA5FA  89 01                           mov dword ptr [rcx], eax
008EA5FC  44 8B 8C 24 B8 00 00 00         mov r9d, dword ptr [rsp + 0xb8]
008EA604  48 8B 9C 24 D8 00 00 00         mov rbx, qword ptr [rsp + 0xd8]
008EA60C  41 BF 00 00 00 80               mov r15d, 0x80000000
008EA612  EB 37                           jmp 0x1408ea64b
008EA614  44 8B C8                        mov r9d, eax
008EA617  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
008EA61E  48 C7 84 24 C0 00 00 00 00 00 00 00  mov qword ptr [rsp + 0xc0], 0
008EA62A  45 33 F6                        xor r14d, r14d
008EA62D  41 BF 00 00 00 80               mov r15d, 0x80000000
008EA633  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
008EA63B  48 8B B4 24 00 01 00 00         mov rsi, qword ptr [rsp + 0x100]
008EA643  48 8B 9C 24 F0 00 00 00         mov rbx, qword ptr [rsp + 0xf0]
008EA64B  48 83 BF B0 00 00 00 00         cmp qword ptr [rdi + 0xb0], 0
008EA653  0F 85 AF 02 00 00               jne 0x1408ea908
008EA659  48 85 DB                        test rbx, rbx
008EA65C  74 32                           je 0x1408ea690
008EA65E  F7 47 50 00 00 00 08            test dword ptr [rdi + 0x50], 0x8000000
008EA665  0F 85 06 0A 00 00               jne 0x1408eb071
008EA66B  45 33 C0                        xor r8d, r8d
008EA66E  33 D2                           xor edx, edx
008EA670  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
008EA678  48 8B CB                        mov rcx, rbx
008EA67B  E8 90 4C A5 FF                  call 0x14033f310
008EA680  48 8B CB                        mov rcx, rbx
008EA683  E8 C8 EC A0 FF                  call 0x1402f9350
008EA688  44 8B 8C 24 B8 00 00 00         mov r9d, dword ptr [rsp + 0xb8]
008EA690  80 7C 24 50 00                  cmp byte ptr [rsp + 0x50], 0
008EA695  74 10                           je 0x1408ea6a7
008EA697  48 8B CF                        mov rcx, rdi
008EA69A  E8 F1 63 96 FF                  call 0x140250a90
008EA69F  44 8B 8C 24 B8 00 00 00         mov r9d, dword ptr [rsp + 0xb8]
008EA6A7  48 85 F6                        test rsi, rsi
008EA6AA  0F 85 84 04 00 00               jne 0x1408eab34
008EA6B0  80 7C 24 71 00                  cmp byte ptr [rsp + 0x71], 0
008EA6B5  74 08                           je 0x1408ea6bf
008EA6B7  48 8B CF                        mov rcx, rdi
008EA6BA  E8 B9 7F B6 FF                  call 0x140452678
008EA6BF  48 8B CF                        mov rcx, rdi
008EA6C2  E8 89 EC A0 FF                  call 0x1402f9350
008EA6C7  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
008EA6CE  E9 A0 FD FF FF                  jmp 0x1408ea473
008EA6D3  8B 84 24 0C 01 00 00            mov eax, dword ptr [rsp + 0x10c]
008EA6DA  23 C1                           and eax, ecx
008EA6DC  3B C1                           cmp eax, ecx
008EA6DE  0F 84 4A F6 FF FF               je 0x1408e9d2e
008EA6E4  48 8B CF                        mov rcx, rdi
008EA6E7  E8 64 EC A0 FF                  call 0x1402f9350
008EA6EC  B8 22 00 00 C0                  mov eax, 0xc0000022
008EA6F1  E9 7D FD FF FF                  jmp 0x1408ea473
008EA6F6  41 C1 ED 02                     shr r13d, 2
008EA6FA  41 80 E5 01                     and r13b, 1
008EA6FE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008EA707  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008EA70E  90                              nop
008EA70F  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
008EA717  48 8D 8B 80 00 00 00            lea rcx, [rbx + 0x80]
008EA71E  45 33 C0                        xor r8d, r8d
008EA721  33 D2                           xor edx, edx
008EA723  E8 08 5B 92 FF                  call 0x140210230
008EA728  C6 44 24 70 00                  mov byte ptr [rsp + 0x70], 0
008EA72D  B9 01 00 00 00                  mov ecx, 1
008EA732  87 4B 74                        xchg dword ptr [rbx + 0x74], ecx
008EA735  85 C9                           test ecx, ecx
008EA737  0F 85 08 09 00 00               jne 0x1408eb045
008EA73D  48 85 C0                        test rax, rax
008EA740  74 04                           je 0x1408ea746
008EA742  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
008EA746  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
008EA74E  48 8B CF                        mov rcx, rdi
008EA751  E8 CA 52 92 FF                  call 0x14020fa20
008EA756  41 8B DE                        mov ebx, r14d
008EA759  80 7C 24 70 00                  cmp byte ptr [rsp + 0x70], 0
008EA75E  0F 85 70 0A 00 00               jne 0x1408eb1d4
008EA764  C6 44 24 50 01                  mov byte ptr [rsp + 0x50], 1
008EA769  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
008EA76D  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
008EA771  0F B6 9C 24 C0 02 00 00         movzx ebx, byte ptr [rsp + 0x2c0]
008EA779  E9 8B F6 FF FF                  jmp 0x1408e9e09
008EA77E  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
008EA782  E8 89 60 B2 FF                  call 0x140410810
008EA787  E9 92 F6 FF FF                  jmp 0x1408e9e1e
008EA78C  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
008EA794  48 85 C0                        test rax, rax
008EA797  0F 85 0F 0C 00 00               jne 0x1408eb3ac
008EA79D  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
008EA7A5  8B 00                           mov eax, dword ptr [rax]
008EA7A7  A8 02                           test al, 2
008EA7A9  0F 85 0A 0C 00 00               jne 0x1408eb3b9
008EA7AF  48 8B CF                        mov rcx, rdi
008EA7B2  E8 99 EB A0 FF                  call 0x1402f9350
008EA7B7  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
008EA7BF  48 85 C0                        test rax, rax
008EA7C2  74 0A                           je 0x1408ea7ce
008EA7C4  33 D2                           xor edx, edx
008EA7C6  48 8B C8                        mov rcx, rax
008EA7C9  E8 A2 80 29 00                  call 0x140b82870
008EA7CE  B8 9A 00 00 C0                  mov eax, 0xc000009a
008EA7D3  E9 9B FC FF FF                  jmp 0x1408ea473
008EA7D8  48 F7 84 24 80 02 00 00 FE FF FF FF  test qword ptr [rsp + 0x280], -2
008EA7E4  0F 84 30 F5 FF FF               je 0x1408e9d1a
008EA7EA  48 8B CF                        mov rcx, rdi
008EA7ED  E8 5E EB A0 FF                  call 0x1402f9350
008EA7F2  B8 0D 00 00 C0                  mov eax, 0xc000000d
008EA7F7  E9 77 FC FF FF                  jmp 0x1408ea473
008EA7FC  8B 7C 24 68                     mov edi, dword ptr [rsp + 0x68]
008EA800  89 7C 24 54                     mov dword ptr [rsp + 0x54], edi
008EA804  E9 CC F4 FF FF                  jmp 0x1408e9cd5
008EA809  44 89 B4 24 C8 00 00 00         mov dword ptr [rsp + 0xc8], r14d
008EA811  F7 47 50 00 08 00 00            test dword ptr [rdi + 0x50], 0x800
008EA818  0F 84 DD 00 00 00               je 0x1408ea8fb
008EA81E  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
008EA822  E8 E9 5F B2 FF                  call 0x140410810
008EA827  48 8D 94 24 C8 00 00 00         lea rdx, [rsp + 0xc8]
008EA82F  48 8B C8                        mov rcx, rax
008EA832  E8 E9 96 B8 FF                  call 0x140473f20
008EA837  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
008EA83E  85 C0                           test eax, eax
008EA840  78 23                           js 0x1408ea865
008EA842  41 81 FF 64 42 09 00            cmp r15d, 0x94264
008EA849  0F 85 4F 03 00 00               jne 0x1408eab9e
008EA84F  F6 84 24 C8 00 00 00 01         test byte ptr [rsp + 0xc8], 1
008EA857  75 0C                           jne 0x1408ea865
008EA859  B8 A1 A2 00 C0                  mov eax, 0xc000a2a1
008EA85E  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
008EA865  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
008EA869  85 C0                           test eax, eax
008EA86B  0F 89 E4 F4 FF FF               jns 0x1408e9d55
008EA871  48 8B CF                        mov rcx, rdi
008EA874  E8 D7 EA A0 FF                  call 0x1402f9350
008EA879  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
008EA880  E9 EE FB FF FF                  jmp 0x1408ea473
008EA885  41 81 FF 00 30 11 00            cmp r15d, 0x113000
008EA88C  0F 84 47 F3 FF FF               je 0x1408e9bd9
008EA892  41 81 FF 28 00 11 00            cmp r15d, 0x110028
008EA899  0F 87 FF 01 00 00               ja 0x1408eaa9e
008EA89F  0F 84 34 F3 FF FF               je 0x1408e9bd9
008EA8A5  41 8B CF                        mov ecx, r15d
008EA8A8  81 E9 28 00 09 00               sub ecx, 0x90028
008EA8AE  0F 84 25 F3 FF FF               je 0x1408e9bd9
008EA8B4  81 E9 DC FF 07 00               sub ecx, 0x7ffdc
008EA8BA  0F 84 19 F3 FF FF               je 0x1408e9bd9
008EA8C0  83 E9 04                        sub ecx, 4
008EA8C3  0F 84 10 F3 FF FF               je 0x1408e9bd9
008EA8C9  83 E9 10                        sub ecx, 0x10
008EA8CC  0F 84 07 F3 FF FF               je 0x1408e9bd9
008EA8D2  83 F9 04                        cmp ecx, 4
008EA8D5  E9 FA 01 00 00                  jmp 0x1408eaad4
008EA8DA  44 8B 6C 24 54                  mov r13d, dword ptr [rsp + 0x54]
008EA8DF  E9 33 F8 FF FF                  jmp 0x1408ea117
008EA8E4  48 8B CF                        mov rcx, rdi
008EA8E7  E8 64 EA A0 FF                  call 0x1402f9350
008EA8EC  41 8B C5                        mov eax, r13d
008EA8EF  E9 7F FB FF FF                  jmp 0x1408ea473
008EA8F4  B0 01                           mov al, 1
008EA8F6  E9 52 F5 FF FF                  jmp 0x1408e9e4d
008EA8FB  48 8B CF                        mov rcx, rdi
008EA8FE  E8 1D 08 9B FF                  call 0x14029b120
008EA903  E9 1F FF FF FF                  jmp 0x1408ea827
008EA908  F7 47 50 00 00 00 02            test dword ptr [rdi + 0x50], 0x2000000
008EA90F  74 11                           je 0x1408ea922
008EA911  41 8B C1                        mov eax, r9d
008EA914  25 00 00 00 C0                  and eax, 0xc0000000
008EA919  41 3B C7                        cmp eax, r15d
008EA91C  0F 85 37 FD FF FF               jne 0x1408ea659
008EA922  41 8B C1                        mov eax, r9d
008EA925  25 00 00 00 C0                  and eax, 0xc0000000
008EA92A  3D 00 00 00 C0                  cmp eax, 0xc0000000
008EA92F  0F 84 24 FD FF FF               je 0x1408ea659
008EA935  4C 8D 8C 24 18 01 00 00         lea r9, [rsp + 0x118]
008EA93D  4C 8D 84 24 00 01 00 00         lea r8, [rsp + 0x100]
008EA945  48 8D 54 24 71                  lea rdx, [rsp + 0x71]
008EA94A  48 8B CF                        mov rcx, rdi
008EA94D  E8 0E 93 B5 FF                  call 0x140443c60
008EA952  44 8B 8C 24 B8 00 00 00         mov r9d, dword ptr [rsp + 0xb8]
008EA95A  48 8B B4 24 00 01 00 00         mov rsi, qword ptr [rsp + 0x100]
008EA962  E9 F2 FC FF FF                  jmp 0x1408ea659
008EA967  45 89 75 10                     mov dword ptr [r13 + 0x10], r14d
008EA96B  4C 89 72 20                     mov qword ptr [rdx + 0x20], r14
008EA96F  85 C9                           test ecx, ecx
008EA971  74 53                           je 0x1408ea9c6
008EA973  48 83 BC 24 A8 00 00 00 00      cmp qword ptr [rsp + 0xa8], 0
008EA97C  74 48                           je 0x1408ea9c6
008EA97E  48 8B D9                        mov rbx, rcx
008EA981  B9 6B 00 00 00                  mov ecx, 0x6b
008EA986  B8 63 00 00 00                  mov eax, 0x63
008EA98B  45 84 C0                        test r8b, r8b
008EA98E  0F 44 C8                        cmove ecx, eax
008EA991  41 B8 49 6F 53 42               mov r8d, 0x42536f49
008EA997  48 8B D3                        mov rdx, rbx
008EA99A  E8 51 77 29 00                  call 0x140b820f0
008EA99F  49 89 45 18                     mov qword ptr [r13 + 0x18], rax
008EA9A3  4C 8B C3                        mov r8, rbx
008EA9A6  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
008EA9AE  48 8B C8                        mov rcx, rax
008EA9B1  E8 8A BE DD FF                  call 0x1406c6840
008EA9B6  41 C7 45 10 30 00 00 00         mov dword ptr [r13 + 0x10], 0x30
008EA9BE  0F B6 9C 24 C0 02 00 00         movzx ebx, byte ptr [rsp + 0x2c0]
008EA9C6  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
008EA9CA  85 C0                           test eax, eax
008EA9CC  0F 84 8C 00 00 00               je 0x1408eaa5e
008EA9D2  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
008EA9D7  41 B1 01                        mov r9b, 1
008EA9DA  45 33 C0                        xor r8d, r8d
008EA9DD  8B D0                           mov edx, eax
008EA9DF  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
008EA9E7  E8 04 42 9B FF                  call 0x14029ebf0
008EA9EC  48 8B C8                        mov rcx, rax
008EA9EF  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
008EA9F7  49 89 45 08                     mov qword ptr [r13 + 8], rax
008EA9FB  48 85 C0                        test rax, rax
008EA9FE  75 0A                           jne 0x1408eaa0a
008EAA00  B9 9A 00 00 C0                  mov ecx, 0xc000009a
008EAA05  E8 46 C0 A0 FF                  call 0x1402f6a50
008EAA0A  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
008EAA0F  8B 00                           mov eax, dword ptr [rax]
008EAA11  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
008EAA18  41 83 FC 01                     cmp r12d, 1
008EAA1C  41 0F 95 C6                     setne r14b
008EAA20  45 8B C6                        mov r8d, r14d
008EAA23  40 0F B6 D6                     movzx edx, sil
008EAA27  E8 64 0F 95 FF                  call 0x14023b990
008EAA2C  8B 05 8A C1 6D 00               mov eax, dword ptr [rip + 0x6dc18a]
008EAA32  A8 01                           test al, 1
008EAA34  74 28                           je 0x1408eaa5e
008EAA36  8B 94 24 A0 00 00 00            mov edx, dword ptr [rsp + 0xa0]
008EAA3D  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
008EAA45  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
008EAA49  48 8B 54 D0 70                  mov rdx, qword ptr [rax + rdx*8 + 0x70]
008EAA4E  4C 8B C1                        mov r8, rcx
008EAA51  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
008EAA59  E8 0A BA B6 FF                  call 0x140456468
008EAA5E  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
008EAA63  E9 8D F9 FF FF                  jmp 0x1408ea3f5
008EAA68  8B D8                           mov ebx, eax
008EAA6A  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
008EAA72  0F B6 51 50                     movzx edx, byte ptr [rcx + 0x50]
008EAA76  D1 EA                           shr edx, 1
008EAA78  83 E2 01                        and edx, 1
008EAA7B  88 54 24 20                     mov byte ptr [rsp + 0x20], dl
008EAA7F  45 33 C9                        xor r9d, r9d
008EAA82  4C 8B 84 24 98 00 00 00         mov r8, qword ptr [rsp + 0x98]
008EAA8A  48 8B 94 24 D8 00 00 00         mov rdx, qword ptr [rsp + 0xd8]
008EAA92  E8 31 3B FC FF                  call 0x1408ae5c8
008EAA97  8B C3                           mov eax, ebx
008EAA99  E9 D5 F9 FF FF                  jmp 0x1408ea473
008EAA9E  41 8B CF                        mov ecx, r15d
008EAAA1  81 E9 30 00 11 00               sub ecx, 0x110030
008EAAA7  0F 84 2C F1 FF FF               je 0x1408e9bd9
008EAAAD  83 E9 08                        sub ecx, 8
008EAAB0  0F 84 23 F1 FF FF               je 0x1408e9bd9
008EAAB6  81 E9 C4 2F 00 00               sub ecx, 0x2fc4
008EAABC  0F 84 17 F1 FF FF               je 0x1408e9bd9
008EAAC2  81 E9 10 10 00 00               sub ecx, 0x1010
008EAAC8  0F 84 0B F1 FF FF               je 0x1408e9bd9
008EAACE  81 F9 0B 80 00 00               cmp ecx, 0x800b
008EAAD4  0F 84 FF F0 FF FF               je 0x1408e9bd9
008EAADA  4C 8B 88 B8 00 00 00            mov r9, qword ptr [rax + 0xb8]
008EAAE1  41 8B 81 D8 07 00 00            mov eax, dword ptr [r9 + 0x7d8]
008EAAE8  0F B6 F8                        movzx edi, al
008EAAEB  24 04                           and al, 4
008EAAED  40 80 E7 02                     and dil, 2
008EAAF1  75 08                           jne 0x1408eaafb
008EAAF3  84 C0                           test al, al
008EAAF5  0F 84 DE F0 FF FF               je 0x1408e9bd9
008EAAFB  41 8B CE                        mov ecx, r14d
008EAAFE  40 84 FF                        test dil, dil
008EAB01  0F 95 C1                        setne cl
008EAB04  FF C1                           inc ecx
008EAB06  49 8B D1                        mov rdx, r9
008EAB09  E8 0A 73 19 00                  call 0x140a81e18
008EAB0E  40 84 FF                        test dil, dil
008EAB11  0F 85 D5 FB FF FF               jne 0x1408ea6ec
008EAB17  48 8B 94 24 B0 00 00 00         mov rdx, qword ptr [rsp + 0xb0]
008EAB1F  4C 8B 84 24 A8 00 00 00         mov r8, qword ptr [rsp + 0xa8]
008EAB27  4C 8B 94 24 80 00 00 00         mov r10, qword ptr [rsp + 0x80]
008EAB2F  E9 A5 F0 FF FF                  jmp 0x1408e9bd9
008EAB34  48 8B 94 24 88 02 00 00         mov rdx, qword ptr [rsp + 0x288]
008EAB3C  48 85 D2                        test rdx, rdx
008EAB3F  0F 84 6B FB FF FF               je 0x1408ea6b0
008EAB45  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
008EAB4A  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
008EAB4F  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
008EAB57  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008EAB5C  4C 8B C2                        mov r8, rdx
008EAB5F  48 8B 94 24 18 01 00 00         mov rdx, qword ptr [rsp + 0x118]
008EAB67  48 8B CE                        mov rcx, rsi
008EAB6A  E8 11 4F 96 FF                  call 0x14024fa80
008EAB6F  8B 8C 24 B8 00 00 00            mov ecx, dword ptr [rsp + 0xb8]
008EAB76  BA 9A 00 00 C0                  mov edx, 0xc000009a
008EAB7B  85 C0                           test eax, eax
008EAB7D  0F 48 CA                        cmovs ecx, edx
008EAB80  8B C1                           mov eax, ecx
008EAB82  25 00 00 00 C0                  and eax, 0xc0000000
008EAB87  BA 03 01 00 00                  mov edx, 0x103
008EAB8C  41 3B C7                        cmp eax, r15d
008EAB8F  0F 44 CA                        cmove ecx, edx
008EAB92  89 8C 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], ecx
008EAB99  E9 12 FB FF FF                  jmp 0x1408ea6b0
008EAB9E  F6 84 24 C8 00 00 00 02         test byte ptr [rsp + 0xc8], 2
008EABA6  B9 A2 A2 00 C0                  mov ecx, 0xc000a2a2
008EABAB  0F 44 C1                        cmove eax, ecx
008EABAE  E9 AB FC FF FF                  jmp 0x1408ea85e
008EABB3  45 8B C7                        mov r8d, r15d
008EABB6  49 8B D3                        mov rdx, r11
008EABB9  E8 3A 20 09 00                  call 0x14097cbf8
008EABBE  33 D2                           xor edx, edx
008EABC0  44 8D 42 40                     lea r8d, [rdx + 0x40]
008EABC4  48 8D 8C 24 70 01 00 00         lea rcx, [rsp + 0x170]
008EABCC  E8 6F C0 DD FF                  call 0x1406c6c40
008EABD1  41 0F B7 45 08                  movzx eax, word ptr [r13 + 8]
008EABD6  83 F8 40                        cmp eax, 0x40
008EABD9  44 8B C8                        mov r9d, eax
008EABDC  0F 83 E9 04 00 00               jae 0x1408eb0cb
008EABE2  4D 8B 45 10                     mov r8, qword ptr [r13 + 0x10]
008EABE6  BA 40 00 00 00                  mov edx, 0x40
008EABEB  48 8D 8C 24 70 01 00 00         lea rcx, [rsp + 0x170]
008EABF3  E8 48 B1 C1 FF                  call 0x140505d40
008EABF8  4C 8B 9C 24 90 01 00 00         mov r11, qword ptr [rsp + 0x190]
008EAC00  49 C1 E3 08                     shl r11, 8
008EAC04  4C 33 9C 24 70 01 00 00         xor r11, qword ptr [rsp + 0x170]
008EAC0C  4C 89 9C 24 70 01 00 00         mov qword ptr [rsp + 0x170], r11
008EAC14  4C 8B 94 24 98 01 00 00         mov r10, qword ptr [rsp + 0x198]
008EAC1C  49 C1 E2 08                     shl r10, 8
008EAC20  4C 33 94 24 78 01 00 00         xor r10, qword ptr [rsp + 0x178]
008EAC28  4C 89 94 24 78 01 00 00         mov qword ptr [rsp + 0x178], r10
008EAC30  4C 8B 84 24 A0 01 00 00         mov r8, qword ptr [rsp + 0x1a0]
008EAC38  49 C1 E0 08                     shl r8, 8
008EAC3C  4C 33 84 24 80 01 00 00         xor r8, qword ptr [rsp + 0x180]
008EAC44  4C 89 84 24 80 01 00 00         mov qword ptr [rsp + 0x180], r8
008EAC4C  4C 8B 8C 24 A8 01 00 00         mov r9, qword ptr [rsp + 0x1a8]
008EAC54  49 C1 E1 08                     shl r9, 8
008EAC58  4C 33 8C 24 88 01 00 00         xor r9, qword ptr [rsp + 0x188]
008EAC60  4C 89 8C 24 88 01 00 00         mov qword ptr [rsp + 0x188], r9
008EAC68  49 8B C0                        mov rax, r8
008EAC6B  48 C1 E8 18                     shr rax, 0x18
008EAC6F  0F B6 C0                        movzx eax, al
008EAC72  48 6B C8 25                     imul rcx, rax, 0x25
008EAC76  49 8B C0                        mov rax, r8
008EAC79  48 C1 E8 20                     shr rax, 0x20
008EAC7D  0F B6 C0                        movzx eax, al
008EAC80  48 03 C8                        add rcx, rax
008EAC83  48 6B D1 25                     imul rdx, rcx, 0x25
008EAC87  49 8B C0                        mov rax, r8
008EAC8A  48 C1 E8 28                     shr rax, 0x28
008EAC8E  0F B6 C0                        movzx eax, al
008EAC91  48 03 D0                        add rdx, rax
008EAC94  48 6B CA 25                     imul rcx, rdx, 0x25
008EAC98  49 8B C0                        mov rax, r8
008EAC9B  48 C1 E8 30                     shr rax, 0x30
008EAC9F  0F B6 C0                        movzx eax, al
008EACA2  48 03 C8                        add rcx, rax
008EACA5  48 6B C9 25                     imul rcx, rcx, 0x25
008EACA9  49 8B C0                        mov rax, r8
008EACAC  48 C1 E8 38                     shr rax, 0x38
008EACB0  48 03 C8                        add rcx, rax
008EACB3  48 6B C9 25                     imul rcx, rcx, 0x25
008EACB7  41 0F B6 C1                     movzx eax, r9b
008EACBB  48 03 C8                        add rcx, rax
008EACBE  48 6B D1 25                     imul rdx, rcx, 0x25
008EACC2  49 8B C1                        mov rax, r9
008EACC5  48 C1 E8 08                     shr rax, 8
008EACC9  0F B6 C0                        movzx eax, al
008EACCC  48 03 D0                        add rdx, rax
008EACCF  48 6B CA 25                     imul rcx, rdx, 0x25
008EACD3  49 8B C1                        mov rax, r9
008EACD6  48 C1 E8 10                     shr rax, 0x10
008EACDA  0F B6 C0                        movzx eax, al
008EACDD  48 03 C8                        add rcx, rax
008EACE0  48 6B D1 25                     imul rdx, rcx, 0x25
008EACE4  49 8B C1                        mov rax, r9
008EACE7  48 C1 E8 18                     shr rax, 0x18
008EACEB  0F B6 C0                        movzx eax, al
008EACEE  48 03 D0                        add rdx, rax
008EACF1  48 6B CA 25                     imul rcx, rdx, 0x25
008EACF5  49 8B C1                        mov rax, r9
008EACF8  48 C1 E8 20                     shr rax, 0x20
008EACFC  0F B6 C0                        movzx eax, al
008EACFF  48 03 C8                        add rcx, rax
008EAD02  48 6B D1 25                     imul rdx, rcx, 0x25
008EAD06  49 8B C1                        mov rax, r9
008EAD09  48 C1 E8 28                     shr rax, 0x28
008EAD0D  0F B6 C0                        movzx eax, al
008EAD10  48 03 D0                        add rdx, rax
008EAD13  48 6B CA 25                     imul rcx, rdx, 0x25
008EAD17  49 8B C1                        mov rax, r9
008EAD1A  48 C1 E8 30                     shr rax, 0x30
008EAD1E  0F B6 C0                        movzx eax, al
008EAD21  48 03 C8                        add rcx, rax
008EAD24  48 6B D1 25                     imul rdx, rcx, 0x25
008EAD28  49 8B C3                        mov rax, r11
008EAD2B  48 C1 E8 20                     shr rax, 0x20
008EAD2F  0F B6 C8                        movzx ecx, al
008EAD32  48 B8 FD 63 C3 80 F5 DA E1 4F   movabs rax, 0x4fe1daf580c363fd
008EAD3C  48 0F AF C8                     imul rcx, rax
008EAD40  48 03 D1                        add rdx, rcx
008EAD43  49 8B C0                        mov rax, r8
008EAD46  48 C1 E8 10                     shr rax, 0x10
008EAD4A  0F B6 C8                        movzx ecx, al
008EAD4D  48 B8 35 8F FF 80 F0 B6 33 34   movabs rax, 0x3433b6f080ff8f35
008EAD57  48 0F AF C8                     imul rcx, rax
008EAD5B  48 03 D1                        add rdx, rcx
008EAD5E  49 8B C2                        mov rax, r10
008EAD61  48 C1 E8 18                     shr rax, 0x18
008EAD65  0F B6 C8                        movzx ecx, al
008EAD68  48 B8 B1 26 FC FA 21 DD 24 BB   movabs rax, 0xbb24dd21fafc26b1
008EAD72  48 0F AF C8                     imul rcx, rax
008EAD76  48 03 D1                        add rdx, rcx
008EAD79  49 8B C3                        mov rax, r11
008EAD7C  48 C1 E8 10                     shr rax, 0x10
008EAD80  0F B6 C8                        movzx ecx, al
008EAD83  48 B8 F5 B3 E1 94 DD EA CB 2E   movabs rax, 0x2ecbeadd94e1b3f5
008EAD8D  48 0F AF C8                     imul rcx, rax
008EAD91  48 03 D1                        add rdx, rcx
008EAD94  49 8B C2                        mov rax, r10
008EAD97  48 C1 E8 10                     shr rax, 0x10
008EAD9B  0F B6 C8                        movzx ecx, al
008EAD9E  48 B8 95 97 71 46 E9 F5 53 0C   movabs rax, 0xc53f5e946719795
008EADA8  48 0F AF C8                     imul rcx, rax
008EADAC  48 03 D1                        add rdx, rcx
008EADAF  49 8B C0                        mov rax, r8
008EADB2  48 C1 E8 08                     shr rax, 8
008EADB6  0F B6 C8                        movzx ecx, al
008EADB9  48 B8 A9 B2 EF A4 C2 70 79 8B   movabs rax, 0x8b7970c2a4efb2a9
008EADC3  48 0F AF C8                     imul rcx, rax
008EADC7  48 03 D1                        add rdx, rcx
008EADCA  49 8B C3                        mov rax, r11
008EADCD  48 C1 E8 18                     shr rax, 0x18
008EADD1  0F B6 C8                        movzx ecx, al
008EADD4  48 B8 91 73 3D 9C 7B A5 A4 8B   movabs rax, 0x8ba4a57b9c3d7391
008EADDE  48 0F AF C8                     imul rcx, rax
008EADE2  48 03 D1                        add rdx, rcx
008EADE5  49 8B C3                        mov rax, r11
008EADE8  48 C1 E8 08                     shr rax, 8
008EADEC  0F B6 C8                        movzx ecx, al
008EADEF  48 B8 69 02 9F 84 06 F2 78 C3   movabs rax, 0xc378f206849f0269
008EADF9  48 0F AF C8                     imul rcx, rax
008EADFD  48 03 D1                        add rdx, rcx
008EAE00  49 8B C2                        mov rax, r10
008EAE03  48 C1 E8 08                     shr rax, 8
008EAE07  0F B6 C8                        movzx ecx, al
008EAE0A  48 B8 89 E8 6A 2E B7 8A 22 C8   movabs rax, 0xc8228ab72e6ae889
008EAE14  48 0F AF C8                     imul rcx, rax
008EAE18  48 03 D1                        add rdx, rcx
008EAE1B  49 8B C2                        mov rax, r10
008EAE1E  48 C1 E8 20                     shr rax, 0x20
008EAE22  0F B6 C8                        movzx ecx, al
008EAE25  48 B8 9D D0 06 F2 53 3D EC 65   movabs rax, 0x65ec3d53f206d09d
008EAE2F  48 0F AF C8                     imul rcx, rax
008EAE33  48 03 D1                        add rdx, rcx
008EAE36  49 8B C3                        mov rax, r11
008EAE39  48 C1 E8 28                     shr rax, 0x28
008EAE3D  0F B6 C8                        movzx ecx, al
008EAE40  48 B8 F9 40 B2 9B B3 6D EA 16   movabs rax, 0x16ea6db39bb240f9
008EAE4A  48 0F AF C8                     imul rcx, rax
008EAE4E  48 03 D1                        add rdx, rcx
008EAE51  49 8B C2                        mov rax, r10
008EAE54  48 C1 E8 30                     shr rax, 0x30
008EAE58  0F B6 C8                        movzx ecx, al
008EAE5B  48 B8 E5 48 69 D7 F4 20 9C DB   movabs rax, 0xdb9c20f4d76948e5
008EAE65  48 0F AF C8                     imul rcx, rax
008EAE69  48 03 D1                        add rdx, rcx
008EAE6C  49 8B C3                        mov rax, r11
008EAE6F  48 C1 E8 30                     shr rax, 0x30
008EAE73  0F B6 C8                        movzx ecx, al
008EAE76  48 B8 45 2B 3C 57 DB B6 90 5A   movabs rax, 0x5a90b6db573c2b45
008EAE80  48 0F AF C8                     imul rcx, rax
008EAE84  48 03 D1                        add rdx, rcx
008EAE87  49 8B C2                        mov rax, r10
008EAE8A  48 C1 E8 28                     shr rax, 0x28
008EAE8E  0F B6 C8                        movzx ecx, al
008EAE91  48 B8 19 89 37 22 63 C3 90 BD   movabs rax, 0xbd90c36322378919
008EAE9B  48 0F AF C8                     imul rcx, rax
008EAE9F  48 03 D1                        add rdx, rcx
008EAEA2  41 0F B6 C0                     movzx eax, r8b
008EAEA6  48 B9 6D D2 A4 D6 21 4C 8D 28   movabs rcx, 0x288d4c21d6a4d26d
008EAEB0  48 0F AF C1                     imul rax, rcx
008EAEB4  48 03 D0                        add rdx, rax
008EAEB7  41 0F B6 C2                     movzx eax, r10b
008EAEBB  48 B9 CD 9B 73 B5 79 0C FE EC   movabs rcx, 0xecfe0c79b5739bcd
008EAEC5  48 0F AF C1                     imul rax, rcx
008EAEC9  48 03 D0                        add rdx, rax
008EAECC  41 0F B6 C3                     movzx eax, r11b
008EAED0  48 B9 2D 59 FB 2A F1 FA 7A 40   movabs rcx, 0x407afaf12afb592d
008EAEDA  48 0F AF C1                     imul rax, rcx
008EAEDE  48 03 D0                        add rdx, rax
008EAEE1  49 C1 EA 38                     shr r10, 0x38
008EAEE5  48 B8 C1 69 D2 05 E4 00 6C DC   movabs rax, 0xdc6c00e405d269c1
008EAEEF  4C 0F AF D0                     imul r10, rax
008EAEF3  49 03 D2                        add rdx, r10
008EAEF6  49 C1 EB 38                     shr r11, 0x38
008EAEFA  48 B8 A1 84 B5 39 97 CD B7 40   movabs rax, 0x40b7cd9739b584a1
008EAF04  4C 0F AF D8                     imul r11, rax
008EAF08  49 03 D3                        add rdx, r11
008EAF0B  49 C1 E9 38                     shr r9, 0x38
008EAF0F  48 B8 0B 04 B9 21 14 75 D9 04   movabs rax, 0x4d9751421b9040b
008EAF19  48 03 D0                        add rdx, rax
008EAF1C  49 03 D1                        add rdx, r9
008EAF1F  83 3D EA BF 51 00 05            cmp dword ptr [rip + 0x51bfea], 5
008EAF26  0F 86 6F F0 FF FF               jbe 0x1408e9f9b
008EAF2C  49 B8 00 00 00 00 00 20 00 00   movabs r8, 0x200000000000
008EAF36  4C 85 05 E3 BF 51 00            test qword ptr [rip + 0x51bfe3], r8
008EAF3D  0F 85 B0 03 00 00               jne 0x1408eb2f3
008EAF43  32 C0                           xor al, al
008EAF45  84 C0                           test al, al
008EAF47  0F 84 4E F0 FF FF               je 0x1408e9f9b
008EAF4D  B8 00 00 00 80                  mov eax, 0x80000000
008EAF52  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
008EAF5A  48 8D 84 24 20 01 00 00         lea rax, [rsp + 0x120]
008EAF62  48 89 84 24 D0 01 00 00         mov qword ptr [rsp + 0x1d0], rax
008EAF6A  48 C7 84 24 D8 01 00 00 08 00 00 00  mov qword ptr [rsp + 0x1d8], 8
008EAF76  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
008EAF7E  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
008EAF86  48 8D 84 24 28 01 00 00         lea rax, [rsp + 0x128]
008EAF8E  48 89 84 24 E0 01 00 00         mov qword ptr [rsp + 0x1e0], rax
008EAF96  48 C7 84 24 E8 01 00 00 08 00 00 00  mov qword ptr [rsp + 0x1e8], 8
008EAFA2  44 89 BC 24 F8 00 00 00         mov dword ptr [rsp + 0xf8], r15d
008EAFAA  48 8D 84 24 F8 00 00 00         lea rax, [rsp + 0xf8]
008EAFB2  48 89 84 24 F0 01 00 00         mov qword ptr [rsp + 0x1f0], rax
008EAFBA  48 C7 84 24 F8 01 00 00 04 00 00 00  mov qword ptr [rsp + 0x1f8], 4
008EAFC6  48 89 94 24 30 01 00 00         mov qword ptr [rsp + 0x130], rdx
008EAFCE  48 8D 84 24 30 01 00 00         lea rax, [rsp + 0x130]
008EAFD6  48 89 84 24 00 02 00 00         mov qword ptr [rsp + 0x200], rax
008EAFDE  48 C7 84 24 08 02 00 00 08 00 00 00  mov qword ptr [rsp + 0x208], 8
008EAFEA  41 0F B7 45 08                  movzx eax, word ptr [r13 + 8]
008EAFEF  89 84 24 FC 00 00 00            mov dword ptr [rsp + 0xfc], eax
008EAFF6  48 8D 84 24 FC 00 00 00         lea rax, [rsp + 0xfc]
008EAFFE  48 89 84 24 10 02 00 00         mov qword ptr [rsp + 0x210], rax
008EB006  48 C7 84 24 18 02 00 00 04 00 00 00  mov qword ptr [rsp + 0x218], 4
008EB012  48 8D 84 24 B0 01 00 00         lea rax, [rsp + 0x1b0]
008EB01A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008EB01F  C7 44 24 20 07 00 00 00         mov dword ptr [rsp + 0x20], 7
008EB027  45 33 C9                        xor r9d, r9d
008EB02A  45 33 C0                        xor r8d, r8d
008EB02D  48 8D 15 D2 BB 75 FF            lea rdx, [rip - 0x8a442e]
008EB034  48 8D 0D D5 BE 51 00            lea rcx, [rip + 0x51bed5]
008EB03B  E8 A0 B0 B3 FF                  call 0x1404260e0
008EB040  E9 56 EF FF FF                  jmp 0x1408e9f9b
008EB045  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
008EB04A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
008EB04F  4C 8B C8                        mov r9, rax
008EB052  45 0F B6 C5                     movzx r8d, r13b
008EB056  40 0F B6 D6                     movzx edx, sil
008EB05A  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
008EB062  48 8B CF                        mov rcx, rdi
008EB065  E8 6E 36 FC FF                  call 0x1408ae6d8
008EB06A  8B D8                           mov ebx, eax
008EB06C  E9 E8 F6 FF FF                  jmp 0x1408ea759
008EB071  48 85 F6                        test rsi, rsi
008EB074  75 60                           jne 0x1408eb0d6
008EB076  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
008EB07E  E9 FD F5 FF FF                  jmp 0x1408ea680
008EB083  B8 03 00 00 00                  mov eax, 3
008EB088  80 7C 24 51 00                  cmp byte ptr [rsp + 0x51], 0
008EB08D  44 0F 44 E0                     cmove r12d, eax
008EB091  E9 61 F2 FF FF                  jmp 0x1408ea2f7
008EB096  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
008EB09A  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008EB09F  48 8B C8                        mov rcx, rax
008EB0A2  E8 C9 D6 BB FF                  call 0x1404a8770
008EB0A7  85 C0                           test eax, eax
008EB0A9  0F 84 37 02 00 00               je 0x1408eb2e6
008EB0AF  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
008EB0B4  E8 03 E7 2C 00                  call 0x140bb97bc
008EB0B9  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008EB0BE  4C 8B 94 24 A0 00 00 00         mov r10, qword ptr [rsp + 0xa0]
008EB0C6  E9 5F F0 FF FF                  jmp 0x1408ea12a
008EB0CB  41 B9 40 00 00 00               mov r9d, 0x40
008EB0D1  E9 0C FB FF FF                  jmp 0x1408eabe2
008EB0D6  41 81 E1 00 00 00 C0            and r9d, 0xc0000000
008EB0DD  45 3B CF                        cmp r9d, r15d
008EB0E0  0F 84 85 F5 FF FF               je 0x1408ea66b
008EB0E6  EB 8E                           jmp 0x1408eb076
008EB0E8  80 7C 24 58 00                  cmp byte ptr [rsp + 0x58], 0
008EB0ED  0F 85 4E F3 FF FF               jne 0x1408ea441
008EB0F3  49 8B 45 18                     mov rax, qword ptr [r13 + 0x18]
008EB0F7  41 81 FF 0C 04 09 00            cmp r15d, 0x9040c
008EB0FE  75 04                           jne 0x1408eb104
008EB100  48 83 C0 20                     add rax, 0x20
008EB104  81 38 03 00 00 A0               cmp dword ptr [rax], 0xa0000003
008EB10A  0F 85 31 F3 FF FF               jne 0x1408ea441
008EB110  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
008EB118  8B 00                           mov eax, dword ptr [rax]
008EB11A  D1 E8                           shr eax, 1
008EB11C  24 01                           and al, 1
008EB11E  88 44 24 20                     mov byte ptr [rsp + 0x20], al
008EB122  45 33 C9                        xor r9d, r9d
008EB125  4C 8B 84 24 98 00 00 00         mov r8, qword ptr [rsp + 0x98]
008EB12D  49 8B D5                        mov rdx, r13
008EB130  48 8B CF                        mov rcx, rdi
008EB133  E8 90 34 FC FF                  call 0x1408ae5c8
008EB138  B8 0D 00 00 C0                  mov eax, 0xc000000d
008EB13D  E9 31 F3 FF FF                  jmp 0x1408ea473
008EB142  41 83 FD 24                     cmp r13d, 0x24
008EB146  0F 82 A1 EC FF FF               jb 0x1408e9ded
008EB14C  0F 57 C0                        xorps xmm0, xmm0
008EB14F  0F 11 84 24 38 01 00 00         movups xmmword ptr [rsp + 0x138], xmm0
008EB157  0F 11 84 24 48 01 00 00         movups xmmword ptr [rsp + 0x148], xmm0
008EB15F  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
008EB167  E8 D4 D3 B5 FF                  call 0x140448540
008EB16C  48 8B D0                        mov rdx, rax
008EB16F  4C 8D 84 24 38 01 00 00         lea r8, [rsp + 0x138]
008EB177  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
008EB17F  E8 0C 9B FD FF                  call 0x1408c4c90
008EB184  40 0F B6 D6                     movzx edx, sil
008EB188  48 8D 8C 24 38 01 00 00         lea rcx, [rsp + 0x138]
008EB190  E8 1B 89 FC FF                  call 0x1408b3ab0
008EB195  88 44 24 51                     mov byte ptr [rsp + 0x51], al
008EB199  88 44 24 50                     mov byte ptr [rsp + 0x50], al
008EB19D  48 8D 8C 24 38 01 00 00         lea rcx, [rsp + 0x138]
008EB1A5  E8 66 05 F8 FF                  call 0x14086b710
008EB1AA  80 7C 24 51 00                  cmp byte ptr [rsp + 0x51], 0
008EB1AF  0F 84 38 EC FF FF               je 0x1408e9ded
008EB1B5  44 89 B4 24 CC 00 00 00         mov dword ptr [rsp + 0xcc], r14d
008EB1BD  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
008EB1C5  41 81 FF 0C 04 09 00            cmp r15d, 0x9040c
008EB1CC  75 77                           jne 0x1408eb245
008EB1CE  44 8B 41 20                     mov r8d, dword ptr [rcx + 0x20]
008EB1D2  EB 74                           jmp 0x1408eb248
008EB1D4  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
008EB1DC  48 85 C0                        test rax, rax
008EB1DF  74 08                           je 0x1408eb1e9
008EB1E1  48 8B C8                        mov rcx, rax
008EB1E4  E8 67 E1 A0 FF                  call 0x1402f9350
008EB1E9  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
008EB1F1  48 85 C9                        test rcx, rcx
008EB1F4  74 07                           je 0x1408eb1fd
008EB1F6  33 D2                           xor edx, edx
008EB1F8  E8 73 76 29 00                  call 0x140b82870
008EB1FD  48 8B CF                        mov rcx, rdi
008EB200  E8 4B E1 A0 FF                  call 0x1402f9350
008EB205  8B C3                           mov eax, ebx
008EB207  E9 67 F2 FF FF                  jmp 0x1408ea473
008EB20C  BA 10 00 00 00                  mov edx, 0x10
008EB211  48 8B CF                        mov rcx, rdi
008EB214  E8 F7 24 B5 FF                  call 0x14043d710
008EB219  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
008EB21D  85 C0                           test eax, eax
008EB21F  0F 89 30 EB FF FF               jns 0x1408e9d55
008EB225  48 8B CF                        mov rcx, rdi
008EB228  E8 23 E1 A0 FF                  call 0x1402f9350
008EB22D  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
008EB231  E9 3D F2 FF FF                  jmp 0x1408ea473
008EB236  41 83 FD 04                     cmp r13d, 4
008EB23A  0F 82 A0 EB FF FF               jb 0x1408e9de0
008EB240  E9 07 FF FF FF                  jmp 0x1408eb14c
008EB245  44 8B 01                        mov r8d, dword ptr [rcx]
008EB248  44 89 84 24 CC 00 00 00         mov dword ptr [rsp + 0xcc], r8d
008EB250  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
008EB254  8B 54 24 78                     mov edx, dword ptr [rsp + 0x78]
008EB258  EB 69                           jmp 0x1408eb2c3
008EB25A  8B D0                           mov edx, eax
008EB25C  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
008EB260  45 33 F6                        xor r14d, r14d
008EB263  44 8B BC 24 98 02 00 00         mov r15d, dword ptr [rsp + 0x298]
008EB26B  48 8B BC 24 88 00 00 00         mov rdi, qword ptr [rsp + 0x88]
008EB273  44 8B A4 24 A0 00 00 00         mov r12d, dword ptr [rsp + 0xa0]
008EB27B  0F B6 74 24 52                  movzx esi, byte ptr [rsp + 0x52]
008EB280  44 8B 84 24 CC 00 00 00         mov r8d, dword ptr [rsp + 0xcc]
008EB288  0F B6 44 24 50                  movzx eax, byte ptr [rsp + 0x50]
008EB28D  88 44 24 51                     mov byte ptr [rsp + 0x51], al
008EB291  44 88 74 24 58                  mov byte ptr [rsp + 0x58], r14b
008EB296  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
008EB29E  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
008EB2A6  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
008EB2AE  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
008EB2B2  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
008EB2B6  0F B6 9C 24 C0 02 00 00         movzx ebx, byte ptr [rsp + 0x2c0]
008EB2BE  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
008EB2C3  85 D2                           test edx, edx
008EB2C5  79 54                           jns 0x1408eb31b
008EB2C7  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
008EB2CF  48 85 C0                        test rax, rax
008EB2D2  0F 84 2E 25 23 00               je 0x140b1d806
008EB2D8  48 8B C8                        mov rcx, rax
008EB2DB  E8 70 E0 A0 FF                  call 0x1402f9350
008EB2E0  90                              nop
008EB2E1  E9 20 25 23 00                  jmp 0x140b1d806
008EB2E6  4C 8B 94 24 A0 00 00 00         mov r10, qword ptr [rsp + 0xa0]
008EB2EE  E9 32 EE FF FF                  jmp 0x1408ea125
008EB2F3  48 8B 05 2E BC 51 00            mov rax, qword ptr [rip + 0x51bc2e]
008EB2FA  49 23 C0                        and rax, r8
008EB2FD  48 3B 05 24 BC 51 00            cmp rax, qword ptr [rip + 0x51bc24]
008EB304  0F 85 39 FC FF FF               jne 0x1408eaf43
008EB30A  B0 01                           mov al, 1
008EB30C  E9 34 FC FF FF                  jmp 0x1408eaf45
008EB311  85 D2                           test edx, edx
008EB313  0F 89 D4 EA FF FF               jns 0x1408e9ded
008EB319  EB AC                           jmp 0x1408eb2c7
008EB31B  41 81 F8 03 00 00 A0            cmp r8d, 0xa0000003
008EB322  75 ED                           jne 0x1408eb311
008EB324  C6 44 24 58 01                  mov byte ptr [rsp + 0x58], 1
008EB329  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
008EB32E  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
008EB333  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
008EB33B  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
008EB340  44 8B C8                        mov r9d, eax
008EB343  45 8B C5                        mov r8d, r13d
008EB346  48 8B D1                        mov rdx, rcx
008EB349  41 8B CF                        mov ecx, r15d
008EB34C  E8 B7 14 E3 FF                  call 0x14071c808
008EB351  8B D0                           mov edx, eax
008EB353  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
008EB357  EB B8                           jmp 0x1408eb311
008EB359  49 8B C3                        mov rax, r11
008EB35C  E9 B6 24 23 00                  jmp 0x140b1d817
008EB361  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
008EB369  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008EB36E  48 8D 84 24 B8 00 00 00         lea rax, [rsp + 0xb8]
008EB376  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008EB37B  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
008EB380  44 89 6C 24 28                  mov dword ptr [rsp + 0x28], r13d
008EB385  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
008EB38D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008EB392  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
008EB397  4C 8B 84 24 A8 00 00 00         mov r8, qword ptr [rsp + 0xa8]
008EB39F  B2 01                           mov dl, 1
008EB3A1  48 8B CF                        mov rcx, rdi
008EB3A4  49 8B C2                        mov rax, r10
008EB3A7  E9 6B 24 23 00                  jmp 0x140b1d817
008EB3AC  48 8B C8                        mov rcx, rax
008EB3AF  E8 9C DF A0 FF                  call 0x1402f9350
008EB3B4  E9 E4 F3 FF FF                  jmp 0x1408ea79d
008EB3B9  48 8B CF                        mov rcx, rdi
008EB3BC  E8 CF 56 96 FF                  call 0x140250a90
008EB3C1  E9 E9 F3 FF FF                  jmp 0x1408ea7af
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopXxxControlFile(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, __int64 a7, unsigned int a8, __int64 a9, unsigned int a10, unsigned __int8 a11, unsigned __int8 a12)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m158;
    unsigned int v_stack_m15C;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned int v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned int v_stack_m1F0;
    unsigned __int8 v_stack_m1F6;
    unsigned int v_stack_m200;
    unsigned int v_stack_m208;
    unsigned __int8 v_stack_m210;
    unsigned int v_stack_m214;
    unsigned __int8 v_stack_m216;
    unsigned __int8 v_stack_m217;
    unsigned __int8 v_stack_m218;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned int v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p100;
    unsigned int v_stack_p10C;
    unsigned __int64 v_stack_p118;
    unsigned __int64 v_stack_p120;
    unsigned __int64 v_stack_p128;
    unsigned __int64 v_stack_p130;
    unsigned __int64 v_stack_p138;
    unsigned __int64 v_stack_p148;
    unsigned __int64 v_stack_p158;
    unsigned __int64 v_stack_p170;
    unsigned __int64 v_stack_p178;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p180;
    unsigned __int64 v_stack_p188;
    unsigned __int64 v_stack_p190;
    unsigned __int64 v_stack_p198;
    unsigned __int64 v_stack_p1A0;
    unsigned __int64 v_stack_p1A8;
    unsigned __int64 v_stack_p1B0;
    unsigned __int64 v_stack_p1D0;
    unsigned __int64 v_stack_p1D8;
    unsigned __int64 v_stack_p1E0;
    unsigned __int64 v_stack_p1E8;
    unsigned __int64 v_stack_p1F0;
    unsigned __int64 v_stack_p1F8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p200;
    unsigned __int64 v_stack_p208;
    unsigned __int64 v_stack_p210;
    unsigned __int64 v_stack_p218;
    unsigned __int8 v_stack_p28;
    unsigned __int64 v_stack_p280;
    unsigned __int64 v_stack_p288;
    unsigned int v_stack_p298;
    unsigned __int8 v_stack_p2C0;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p50;
    unsigned __int8 v_stack_p51;
    unsigned __int8 v_stack_p52;
    unsigned int v_stack_p54;
    unsigned __int8 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned int v_stack_p68;
    unsigned __int8 v_stack_p70;
    unsigned __int8 v_stack_p71;
    unsigned int v_stack_p78;
    unsigned int v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_p98;
    unsigned int v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned int v_stack_pC0;
    unsigned int v_stack_pC8;
    unsigned int v_stack_pCC;
    unsigned __int64 v_stack_pD0;
    unsigned __int64 v_stack_pD8;
    unsigned __int64 v_stack_pE0;
    unsigned __int64 v_stack_pE8;
    unsigned __int64 v_stack_pF0;
    unsigned int v_stack_pF8;
    unsigned int v_stack_pFC;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (560);
    result = (*(unsigned __int64 *)(v_rip + 5377101)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m190 = a2;
    v_stack_m1E8 = a1;
    v_stack_m1F6 = a11;
    v_stack_m178 = a2;
    v_stack_m198 = a5;
    v_stack_m1C0 = a7;
    v_stack_m208 = (unsigned int)((unsigned int)(a8));
    v_stack_m1B8 = a9;
    v_stack_m200 = (unsigned int)((unsigned int)(a10));
    v_r14 = 0;
    v_stack_m1E0 = 0;
    v_stack_m1D0 = 0;
    v_stack_m160 = 0;
    v_stack_m1B0 = v_xmm0;
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) & (3));
    v_stack_m1C8 = (unsigned int)(v_r12);
    v_stack_m180 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m216 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_008EA7FC;
    if (a11 == 0) goto loc_008EA885;
loc_008E9BD9:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_008EA7FC;
    a1 = v_stack_m198;
    if (v_stack_m198 >= a2) { a1 = a2; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    if ((unsigned int)(v_r12) == 0) goto loc_008E9C5D;
loc_008E9C04:
    v_stack_m214 = (unsigned int)((unsigned int)(v_stack_m200));
loc_008E9C0C:
    if (((unsigned int)(v_r12)) == 3) goto loc_008E9CC6;
    if (a7 == 0) goto loc_008E9C56;
    if (((a12) & (1)) != 0) goto loc_008E9CC6;
    if ((unsigned int)((unsigned int)(v_stack_m208)) == 0) goto loc_008E9CC6;
    if ((a7 + (unsigned int)(v_stack_m208) * 1) > a2) goto loc_008E9C47;
    if ((a7 + (unsigned int)(v_stack_m208) * 1) >= a7) goto loc_008E9CC6;
loc_008E9C47:
    v_stack_m214 = (unsigned int)((unsigned int)(v_stack_m200));
    goto loc_008E9CC6;
loc_008E9C56:
    v_stack_m208 = 0;
    goto loc_008E9CC6;
loc_008E9C5D:
    if (a9 == 0) goto loc_008E9CB1;
    v_stack_m214 = (unsigned int)((unsigned int)(v_stack_m200));
    if ((unsigned int)((unsigned int)(v_stack_m200)) == 0) goto loc_008E9CAB;
    a4 = ((unsigned int)(v_stack_m200) - 1) + (a9);
    if (a9 > a4) goto loc_008E9CC0;
    if (a4 >= a2) goto loc_008E9CC0;
    a4 = (a4) & (0xFFFFFFFFFFFFF000ULL);
    a4 = (a4) + (0x1000ULL);
loc_008E9C90:
    *(unsigned __int8 *)(a9) = (unsigned __int8)(*(unsigned __int8 *)(a9));
    result = (a9) & (0xFFFFFFFFFFFFF000ULL);
    result = (result) + (0x1000ULL);
    if (result != a4) goto loc_008E9C90;
    goto loc_008E9C04;
loc_008E9CAB:
    goto loc_008E9C0C;
loc_008E9CB1:
    v_stack_m214 = 0;
    v_stack_m200 = 0;
    goto loc_008E9C0C;
loc_008E9CC0:
    result = ExRaiseAccessViolation(*(unsigned __int8 *)(a9), a9, a7, a4);
loc_008E9CC6:
    goto loc_008E9CD5;
loc_008E9CD5:
    v_stack_m248 = v_stack_m160;
    a2 = 0;
    result = IopReferenceFileObject(a1, a2, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_m1E0);
    v_stack_m1F0 = (unsigned int)(result);
    if (sign_flag) goto loc_008EA473;
    if ((*(unsigned __int64 *)(v_stack_m1E0 + 176)) != 0) goto loc_008EA7D8;
loc_008E9D1A:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_008E9D2E;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) >> (14));
    a1 = (unsigned int)((a1) & (3));
    if (condition_is_not_equal) goto loc_008EA6D3;
loc_008E9D2E:
    if (((unsigned int)((unsigned int)(a6))) == 0x94264ULL) goto loc_008EA809;
    if (((unsigned int)((unsigned int)(a6))) == 0x98268ULL) goto loc_008EA809;
    if (((unsigned int)((unsigned int)(a6))) == 0x9042CULL) goto loc_008EB20C;
loc_008E9D55:
    if (v_stack_m190 == 0) goto loc_008E9DB4;
    v_stack_m158 = 0;
    v_stack_m240 = 0;
    v_stack_m248 = v_stack_m158;
    result = ObReferenceObjectByHandle(v_stack_m190, 2, *(unsigned __int64 *)(v_rip + 7196191), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_stack_m1F0 = (unsigned int)(result);
    v_stack_m1D0 = v_stack_m158;
    if (sign_flag) goto loc_008EA8E4;
    result = KeResetEvent(v_stack_m158, 2, *(unsigned __int64 *)(v_rip + 7196191), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
loc_008E9DB4:
    v_stack_m188 = 0;
    v_stack_m217 = 0;
    a3 = 0;
    v_stack_m210 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_008E9DED;
    if (((unsigned int)((unsigned int)(a6))) == 0x900A4ULL) goto loc_008EB236;
loc_008E9DE0:
    if (((unsigned int)((unsigned int)(a6))) == 0x9040CULL) goto loc_008EB142;
loc_008E9DED:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m1E0 + 80)))) & (2)) != 0) goto loc_008EA6F6;
    v_stack_m218 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_008EA4B1;
loc_008E9E09:
    if (((*(unsigned int *)(v_stack_m1E0 + 80)) & (0x800ULL)) != 0) goto loc_008EA77E;
    result = IoGetRelatedDeviceObject(v_stack_m1E0, 2, a3, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
loc_008E9E1E:
    v_stack_m1E8 = result;
    if (a11 == 0) goto loc_008EA1EF;
    if ((*(unsigned __int8 *)(v_rip + 6959648)) == 0) goto loc_008E9F9B;
    if ((*(unsigned int *)(v_rip + 5361867)) > 0) goto loc_008EA8F4;
    result = 0;
loc_008E9E4D:
    if (0 == 0) goto loc_008E9F9B;
    if ((((unsigned __int8)(*(unsigned __int8 *)(result - 48 + 26))) & (2)) != 0) goto loc_008EA497;
loc_008E9E69:
    if (0 == 0) goto loc_008E9F9B;
    v_r10 = ((unsigned int)((unsigned int)((unsigned int)(a6)))) << (32);
    result = (0) >> (4);
    v_r10 = (v_r10) ^ (result);
    v_stack_m108 = v_r10;
    a1 = (v_stack_m1E0) * ((unsigned int)(*(unsigned int *)(v_rip + 6959544)));
    a1 = (a1) + ((unsigned __int8)(v_r10));
    a2 = (2) * (a1);
    result = (v_r10) >> (8);
    a2 = (a2) + ((unsigned __int8)(result));
    a1 = (a1) * (a2);
    result = (v_r10) >> (16);
    a1 = (a1) + ((unsigned __int8)(result));
    a2 = (a2) * (a1);
    result = (v_r10) >> (24);
    a2 = (a2) + ((unsigned __int8)(result));
    a1 = (a1) * (a2);
    result = (v_r10) >> (32);
    a1 = (a1) + ((unsigned __int8)(result));
    a2 = (a2) * (a1);
    result = (v_r10) >> (40);
    a2 = (a2) + ((unsigned __int8)(result));
    a1 = (a1) * (a2);
    result = (v_r10) >> (48);
    a1 = (a1) + ((unsigned __int8)(result));
    a3 = (a3) * (a1);
    a1 = (v_r10) >> (56);
    a3 = (a3) + (a1);
    result = (unsigned int)(((unsigned int)((unsigned int)(a3))) >> (16));
    a2 = 0;
    v_stack_m1C8 = 0;
    a2 = 0;
    a2 = 0;
    result = (0) >> (3);
    a2 = (unsigned int)((a2) & (7));
    result = (unsigned __int8)((*(unsigned __int8 *)(result + *(unsigned __int64 *)(v_rip + 6959359) * 1)) >> ((unsigned __int8)((unsigned __int8)(a2))));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_008EABB3;
    result = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m1C8)))) >> (3);
    a1 = (unsigned int)(((unsigned int)(v_stack_m1C8)) & (7));
    result = (unsigned __int8)((*(unsigned __int8 *)(result + *(unsigned __int64 *)(v_rip + 6959359) * 1)) >> ((unsigned __int8)(a1)));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_008EABB3;
    result = (0) >> (3);
    v_r10 = (unsigned int)((0) & (7));
    result = (unsigned __int8)((*(unsigned __int8 *)(result + *(unsigned __int64 *)(v_rip + 6959359) * 1)) >> ((unsigned __int8)((unsigned __int8)(v_r10))));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_008EABB3;
loc_008E9F9B:
    if (a11 == 0) goto loc_008EA1EF;
    if (v_stack_m217 != 0) goto loc_008EA1EF;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1E8 + 8) + 80) == 0) goto loc_008EA1EF;
    v_stack_m1C8 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1E8 + 8) + 80) + 80);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1E8 + 8) + 80) + 80) == 0) goto loc_008EA1EF;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_008EA0EA;
    if (v_stack_m1B8 == 0) goto loc_008EA0EA;
    if (((unsigned int)(v_r12)) == 1) goto loc_008EA07B;
    if (((unsigned int)(v_r12)) != 2) goto loc_008EA0AE;
    if ((unsigned int)((unsigned int)(v_stack_m214)) == 0) goto loc_008EA072;
    a3 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m214)))) - 1;
    a3 = (a3) + (v_stack_m1B8);
    if (v_stack_m1B8 > a3) goto loc_008EA075;
    if (a3 >= ((unsigned int)(v_stack_m214))) goto loc_008EA075;
    a3 = (a3) & (0xFFFFFFFFFFFFF000ULL);
    a3 = (a3) + (0x1000ULL);
loc_008EA040:
    *(unsigned __int8 *)(v_stack_m1B8) = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m1B8));
    a1 = (v_stack_m1B8) & (0xFFFFFFFFFFFFF000ULL);
    a1 = (a1) + (0x1000ULL);
    if (a1 != a3) goto loc_008EA040;
    v_stack_m214 = (unsigned int)((unsigned int)(v_stack_m200));
    goto loc_008EA0AE;
loc_008EA072:
    goto loc_008EA0AE;
loc_008EA075:
    result = ExRaiseAccessViolation(v_stack_m1E8, v_stack_m1B8, a3, (unsigned int)(*(unsigned int *)(v_rip + 6959534)));
loc_008EA07B:
    if ((unsigned int)((unsigned int)(v_stack_m214)) == 0) goto loc_008EA0AE;
    if ((v_stack_m1B8 + (unsigned int)(v_stack_m214) * 1) < v_stack_m1B8) goto loc_008EA09B;
    result = (unsigned int)(v_stack_m214);
    v_rdi = v_stack_m1E0;
    if ((v_stack_m1B8 + (unsigned int)(v_stack_m214) * 1) >= = ((unsigned int)(v_stack_m214))) {
        result = *(unsigned __int8 *)((unsigned int)(v_stack_m214));
        v_rdi = v_stack_m1E0;
        result = v_stack_m200;
        v_stack_m214 = (unsigned int)(result);
    }
    goto loc_008EA0EA;
loc_008EA0EA:
    if (((unsigned int)((unsigned int)(a6))) != 0x90020ULL) goto loc_008EA8DA;
    v_stack_m214 = (unsigned int)((unsigned int)(v_stack_m200));
loc_008EA117:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 6400259)))) & (16)) != 0) goto loc_008EB096;
loc_008EA125:
    v_stack_m1F0 = 0;
loc_008EA12A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1E8 + 8) + 80) + 80)) != (v_rip + 9343)) goto loc_008EB361;
    a1 = 0;
    v_stack_m216 = 0;
    if ((*(unsigned __int64 *)(v_stack_m1E0 + 24)) >= 5) goto loc_008EA1CD;
    if (*(unsigned __int64 *)(v_rip - 9347417 + *(unsigned __int64 *)(v_stack_m1E0 + 24) + *(unsigned __int64 *)(v_stack_m1E0 + 24) * 2 * 8 + 6560) == 0) goto loc_008EA1CD;
    v_stack_m228 = v_stack_m1E8;
    v_stack_m230 = v_stack_m1B0;
    v_stack_m238 = (unsigned int)((unsigned int)(a6));
    v_stack_m240 = (unsigned int)((unsigned int)(v_stack_m200));
    v_stack_m248 = v_stack_m1B8;
    if ((*(unsigned __int64 *)(v_rip - 9347417 + *(unsigned __int64 *)(v_stack_m1E0 + 24) + *(unsigned __int64 *)(v_stack_m1E0 + 24) * 2 * 8 + 6560)) != (v_rip + 4707)) goto loc_008EB359;
    result = PiCMFastIoDeviceDispatch(v_stack_m1E0, 1, v_stack_m1C0, (unsigned int)(v_stack_m208));
    v_stack_m216 = (unsigned __int8)(result);
loc_008EA1CD:
    result = v_stack_m1F0;
    if (v_stack_m1F0 != 0) {
        a2 = v_stack_m1C8;
        a1 = v_stack_m1F0;
        result = VfFastIoCheckState(a1, a2, v_stack_m1C0, (unsigned int)(v_stack_m208));
        a1 = v_stack_m216;
    }
    if ((unsigned __int8)(a1) != 0) goto loc_008EA5AA;
loc_008EA1EF:
    v_stack_m178 = v_stack_m1E0 + 80;
    result = v_stack_m1E0 + 80;
    if (((*(unsigned int *)(v_stack_m1E0 + 80)) & (0x4000000ULL)) == 0) {
        a1 = v_stack_m1E0 + 152;
        result = KeResetEvent(a1, a2, v_stack_m1C0, (unsigned int)(v_stack_m208));
    }
    a3 = (unsigned __int8)((v_stack_m218) ^ (1));
    result = IopAllocateIrpExReturn(v_stack_m1E8, *(unsigned __int8 *)(v_stack_m1E8 + 76), a3, (unsigned int)(v_stack_m208));
    v_stack_m190 = result;
    if (result == 0) goto loc_008EA78C;
    *(unsigned __int64 *)(result + 192) = v_stack_m1E0;
    *(unsigned __int64 *)(result + 152) = v_stack_m180;
    *(unsigned __int64 *)(result + 160) = 0;
    *(unsigned __int8 *)(result + 64) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    *(unsigned __int8 *)(result + 65) = 0;
    *(unsigned __int8 *)(result + 68) = 0;
    *(unsigned __int64 *)(result + 104) = 0;
    *(unsigned __int64 *)(result + 80) = v_stack_m1D0;
    *(unsigned __int64 *)(result + 72) = v_stack_m198;
    *(unsigned __int64 *)(result + 88) = v_stack_p18;
    *(unsigned __int64 *)(result + 96) = v_stack_p20;
    a2 = (*(unsigned __int64 *)(result + 184)) - (72);
    v_stack_m1F0 = a2;
    result = ((unsigned __int8)(v_stack_m1F6) != 0) ? 1 : 0;
    result = (unsigned int)((result) + (13));
    *(unsigned int *)(a2) = (unsigned int)(result);
    *(unsigned __int64 *)(a2 + 48) = v_stack_m1E0;
    *(unsigned int *)(a2 + 8) = (unsigned int)((unsigned int)(v_stack_m214));
    *(unsigned int *)(a2 + 16) = (unsigned int)((unsigned int)(v_stack_m208));
    *(unsigned int *)(a2 + 24) = (unsigned int)((unsigned int)(a6));
    *(unsigned __int64 *)(result + 8) = 0;
    *(unsigned __int64 *)(result + 24) = 0;
    if (((*(unsigned int *)(v_stack_m1E8 + 48)) & (0x80000ULL)) != 0) goto loc_008EB083;
loc_008EA2F7:
    if ((unsigned int)(v_r12) != 0) goto loc_008EA56B;
    *(unsigned __int64 *)(a2 + 32) = 0;
    if ((unsigned int)((unsigned int)(v_stack_m208)) != 0) goto loc_008EA316;
    if ((unsigned int)((unsigned int)(v_stack_m214)) == 0) goto loc_008EA39A;
loc_008EA316:
    if (v_stack_m188 != 0) goto loc_008EA394;
    a2 = (unsigned int)((unsigned int)((unsigned int)(v_stack_m214)));
    if (((unsigned int)((unsigned int)(v_stack_m208))) > ((unsigned int)((unsigned int)(v_stack_m214)))) { a2 = (unsigned int)((unsigned int)(v_stack_m208)); }
    a1 = 105;
    if ((unsigned __int8)(v_stack_m1F6) == 0) { a1 = 97; }
    result = ExAllocatePool2(a1, a2, (unsigned int)(0x42536F49ULL), (unsigned int)(v_stack_m208));
    *(unsigned __int64 *)(result + 24) = result;
    result = v_stack_m1C0;
    if (v_stack_m1C0 != 0) {
        a3 = v_stack_m208;
        a2 = v_stack_m1C0;
        result = memcpy(result, a2, a3, (unsigned int)(v_stack_m208));
    }
loc_008EA371:
    *(unsigned int *)(result + 16) = 48;
    *(unsigned __int64 *)(result + 112) = v_stack_m1B8;
    if ((unsigned int)((unsigned int)(v_stack_m214)) == 0) goto loc_008EA3A2;
    *(unsigned int *)(result + 16) = 112;
    goto loc_008EA3A2;
loc_008EA394:
    *(unsigned __int64 *)(result + 24) = v_stack_m1B8;
    goto loc_008EA371;
loc_008EA39A:
    *(unsigned int *)(result + 16) = 0;
    *(unsigned __int64 *)(result + 112) = 0;
loc_008EA3A2:
    goto loc_008EA3DA;
loc_008EA3DA:
    result = v_stack_m1B8;
    v_r12 = (unsigned int)(v_stack_m214);
    if (((unsigned int)((unsigned int)(v_stack_m208))) < ((unsigned int)((unsigned int)(v_stack_m214)))) {
        v_r12 = (unsigned int)(((unsigned int)(v_stack_m214)) - ((unsigned int)((unsigned int)(v_stack_m208))));
        a3 = (unsigned int)(v_r12);
        a1 = ((unsigned int)(v_stack_m208)) + (*(unsigned __int64 *)(result + 24));
        a2 = 0;
        result = memset(a1, a2, a3, (unsigned int)(v_stack_m208));
        a2 = v_stack_m1F0;
    }
    a1 = (unsigned __int8)(((unsigned __int8)((unsigned int)(v_stack_m15C))) & (2));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a1)));
    result = (unsigned __int8)(((unsigned int)(v_stack_m15C)) & (1));
    a1 = (unsigned __int8)((a1) | ((unsigned __int8)(result)));
    if (a11 == 0) {
    }
    v_rdi = v_stack_m1E0;
    if (((unsigned int)((unsigned int)(a6))) == 0x90020ULL) {
        result = *(unsigned __int64 *)(v_rip + 7187425);
        v_rdi = v_stack_m1E0;
    }
    if (v_stack_m217 != 0) goto loc_008EB0E8;
loc_008EA441:
    a4 = (v_stack_m1F6 == 0) ? 1 : 0;
    v_stack_m238 = 2;
    v_stack_m240 = (unsigned __int8)(v_stack_m218);
    v_stack_m248 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    result = IopSynchronousServiceTail(v_stack_m1E8, result, v_rdi, a4);
loc_008EA473:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, result, v_rdi, a4);
    v_rsp = (v_rsp) + (560);
    return result;
loc_008EA497:
    result = (unsigned int)((result) & (3));
    v_r13 = (result) - (*(unsigned __int8 *)(result + v_rip - 9348257 * 1 + 15794048));
    goto loc_008E9E69;
loc_008EA4B1:
    v_stack_p158 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 784)) == 0) goto loc_008EA51A;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772))) != 332) goto loc_008EA510;
loc_008EA4E4:
    a2 = (v_stack_p280) | (1);
    *(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_pD0))) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_pD0)))));
    v_stack_pD0 = (unsigned int)(*(unsigned int *)(v_stack_pD0));
    v_stack_p280 = a2;
    goto loc_008EA51A;
loc_008EA510:
    if (((unsigned __int16)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_pD0)))))) == 452) goto loc_008EA4E4;
loc_008EA51A:
    v_stack_p54 = (unsigned int)((unsigned int)(v_stack_p68));
    goto loc_008E9E09;
loc_008EA56B:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) - (1));
    if (condition_is_equal) goto loc_008EA967;
    result = (unsigned int)((result) - (1));
    if (condition_is_equal) goto loc_008EA967;
    if (((unsigned int)(result)) != 1) goto loc_008EA3F5;
    *(unsigned int *)(v_r13 + 16) = 0;
    *(unsigned __int64 *)(v_r13 + 112) = v_stack_pB0;
    *(unsigned __int64 *)(a2 + 32) = v_stack_pA8;
    goto loc_008EA3F5;
loc_008EA5AA:
    v_stack_p100 = 0;
    v_stack_p118 = 0;
    v_stack_p71 = 0;
    if (((v_stack_p280) & (1)) != 0) goto loc_008EA5E1;
    *(unsigned __int64 *)(v_stack_pD0) = v_xmm0;
    goto loc_008EA5FC;
loc_008EA5E1:
    *(unsigned int *)(v_stack_pD0 + 4) = (unsigned int)((unsigned int)(v_stack_pC0));
    *(unsigned int *)(v_stack_pD0) = (unsigned int)((unsigned int)(v_stack_pB8));
loc_008EA5FC:
    goto loc_008EA64B;
loc_008EA64B:
    if ((*(unsigned __int64 *)(v_stack_p88 + 176)) != 0) goto loc_008EA908;
loc_008EA659:
    if (v_stack_pD8 == 0) goto loc_008EA690;
    if (((*(unsigned int *)(v_stack_p88 + 80)) & (0x8000000ULL)) != 0) goto loc_008EB071;
loc_008EA66B:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_stack_p98, a2, a3, (unsigned int)(v_stack_pB8));
loc_008EA680:
    result = ObfDereferenceObject(v_stack_p98, a2, a3, (unsigned int)(v_stack_pB8));
loc_008EA690:
    if (v_stack_p50 != 0) {
        a1 = v_stack_p88;
        result = IopReleaseFileObjectLock(a1, a2, a3, (unsigned int)(v_stack_pB8));
        a4 = v_stack_pB8;
    }
    if (0 != 0) goto loc_008EAB34;
loc_008EA6B0:
    if (v_stack_p71 != 0) {
        a1 = v_stack_p88;
        result = IopDecrementCompletionContextUsageCount(a1, a2, a3, a4);
    }
    result = ObfDereferenceObject(v_stack_p88, a2, a3, a4);
    goto loc_008EA473;
loc_008EA6D3:
    result = (unsigned int)(((unsigned int)(v_stack_p10C)) & ((unsigned int)(v_stack_p88)));
    if (((unsigned int)(result)) == ((unsigned int)(v_stack_p88))) goto loc_008E9D2E;
    result = ObfDereferenceObject(v_stack_p88, a2, a3, a4);
loc_008EA6EC:
    goto loc_008EA473;
loc_008EA6F6:
    v_r13 = (unsigned int)((v_r13) >> (2));
    v_r13 = (unsigned __int8)((v_r13) & (1));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_p88 + 128, a2, a3, a4);
    v_stack_p70 = 0;
    if (1 != 0) goto loc_008EB045;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = ObfReferenceObject(v_stack_p88, a2, a3, a4);
loc_008EA759:
    if (v_stack_p70 != 0) goto loc_008EB1D4;
    v_stack_p50 = 1;
    v_stack_p54 = (unsigned int)((unsigned int)(v_stack_p68));
    goto loc_008E9E09;
loc_008EA77E:
    result = IoGetAttachedDevice(*(unsigned __int64 *)(v_stack_p88 + 8), a2, a3, a4);
    goto loc_008E9E1E;
loc_008EA78C:
    if (v_stack_p98 != 0) goto loc_008EB3AC;
loc_008EA79D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_pF0)))) & (2)) != 0) goto loc_008EB3B9;
loc_008EA7AF:
    result = ObfDereferenceObject(v_stack_p88, a2, a3, a4);
    result = v_stack_pE0;
    if (v_stack_pE0 != 0) {
        a2 = 0;
        a1 = v_stack_pE0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    goto loc_008EA473;
loc_008EA7D8:
    if (((v_stack_p280) & (-2)) == 0) goto loc_008E9D1A;
    result = ObfDereferenceObject(v_stack_p88, a2, a3, a4);
    goto loc_008EA473;
loc_008EA7FC:
    v_stack_p54 = (unsigned int)((unsigned int)(v_stack_p68));
    goto loc_008E9CD5;
loc_008EA809:
    v_stack_pC8 = 0;
    if (((*(unsigned int *)((unsigned int)(v_stack_p68) + 80)) & (0x800ULL)) == 0) goto loc_008EA8FB;
    result = IoGetAttachedDevice(*(unsigned __int64 *)((unsigned int)(v_stack_p68) + 8), a2, a3, a4);
loc_008EA827:
    result = FsRtlGetSupportedFeatures(result, v_stack_pC8, a3, a4);
    v_stack_p80 = (unsigned int)(result);
    if (sign_flag) goto loc_008EA865;
    if (((unsigned int)((unsigned int)(0x80000000ULL))) != 0x94264ULL) goto loc_008EAB9E;
    if (((v_stack_pC8) & (1)) != 0) goto loc_008EA865;
loc_008EA85E:
    v_stack_p80 = (unsigned int)((unsigned int)(0xC000A2A1ULL));
loc_008EA865:
    v_stack_p78 = (unsigned int)((unsigned int)(0xC000A2A1ULL));
    if (!sign_flag) goto loc_008E9D55;
    result = ObfDereferenceObject((unsigned int)(v_stack_p68), v_stack_pC8, a3, a4);
    goto loc_008EA473;
loc_008EA885:
    if (((unsigned int)((unsigned int)(0x80000000ULL))) == 0x113000ULL) goto loc_008E9BD9;
    if (((unsigned int)((unsigned int)(0x80000000ULL))) > 0x110028ULL) goto loc_008EAA9E;
    if (((unsigned int)((unsigned int)(0x80000000ULL))) == 0x110028ULL) goto loc_008E9BD9;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x80000000ULL)))) - (0x90028ULL));
    if (condition_is_equal) goto loc_008E9BD9;
    a1 = (unsigned int)((a1) - (0x7FFDCULL));
    if (condition_is_equal) goto loc_008E9BD9;
    a1 = (unsigned int)((a1) - (4));
    if (condition_is_equal) goto loc_008E9BD9;
    a1 = (unsigned int)((a1) - (16));
    if (condition_is_equal) goto loc_008E9BD9;
    goto loc_008EAAD4;
loc_008EA8DA:
    goto loc_008EA117;
loc_008EA8E4:
    result = ObfDereferenceObject((unsigned int)(v_stack_p68), v_stack_pC8, a3, a4);
    goto loc_008EA473;
loc_008EA8F4:
    goto loc_008E9E4D;
loc_008EA8FB:
    result = IoGetRelatedDeviceObject((unsigned int)(v_stack_p68), v_stack_pC8, a3, a4);
    goto loc_008EA827;
loc_008EA908:
    if (((*(unsigned int *)((unsigned int)(v_stack_p68) + 80)) & (0x2000000ULL)) == 0) goto loc_008EA922;
    result = (unsigned int)(((unsigned int)((unsigned int)(a4))) & (0xC0000000ULL));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x80000000ULL)))) goto loc_008EA659;
loc_008EA922:
    result = (unsigned int)(((unsigned int)((unsigned int)(a4))) & (0xC0000000ULL));
    if (((unsigned int)(result)) == 0xC0000000ULL) goto loc_008EA659;
    result = IopIncrementCompletionContextUsageCountAndReadData((unsigned int)(v_stack_p68), v_stack_p71, v_stack_p100, v_stack_p118);
    goto loc_008EA659;
loc_008EA967:
    *(unsigned int *)((unsigned int)(v_stack_p54) + 16) = 0;
    *(unsigned __int64 *)(v_stack_p71 + 32) = 0;
    if ((unsigned int)((unsigned int)(v_stack_p68)) == 0) goto loc_008EA9C6;
    v_rbx = a11;
    if (v_stack_pA8 != 0) {
        v_rbx = (unsigned int)(v_stack_p68);
        a1 = 107;
        result = 99;
        if ((unsigned __int8)(v_stack_p100) == 0) { a1 = (unsigned int)(result); }
        a3 = 0x42536F49ULL;
        a2 = v_rbx;
        result = ExAllocatePool2(a1, a2, a3, (unsigned int)(v_stack_pB8));
        *(unsigned __int64 *)((unsigned int)(v_stack_p54) + 24) = result;
        a3 = v_rbx;
        a2 = v_stack_pA8;
        a1 = result;
        result = memcpy(a1, a2, a3, (unsigned int)(v_stack_pB8));
        *(unsigned int *)((unsigned int)(v_stack_p54) + 16) = 48;
        v_rbx = a11;
    }
    if ((unsigned int)((unsigned int)(v_stack_p54)) == 0) goto loc_008EAA5E;
    v_stack_p20 = (unsigned int)(v_stack_p54);
    a3 = 0;
    result = IoAllocateMdl(v_stack_pB0, (unsigned int)((unsigned int)((unsigned int)(v_stack_p54))), a3, 1);
    v_stack_pE8 = result;
    *(unsigned __int64 *)((unsigned int)(v_stack_p54) + 8) = result;
    if (result == 0) {
        a1 = 0xC000009AULL;
        result = RtlRaiseStatus(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p54))), a3, 1);
    }
    v_stack_pA0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p78)));
    v_r14 = (((unsigned int)(v_r12)) != 1) ? 1 : 0;
    result = MmProbeAndLockPages(a1, (unsigned __int8)(v_stack_p100), (unsigned int)((unsigned int)(v_r14)), 1);
    result = (unsigned int)(*(unsigned int *)(v_rip + 7192970));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 7192970)))) & (1)) != 0) {
        a2 = v_stack_pA0;
        a1 = v_stack_p80;
        result = *(unsigned __int64 *)(a1 + 8);
        a2 = *(unsigned __int64 *)(result + a2 * 8 + 112);
        a3 = a1;
        a1 = v_stack_pE8;
        result = MmUpdateMdlTracker(a1, a2, a3, 1);
    }
    goto loc_008EA3F5;
loc_008EAA9E:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x80000000ULL)))) - (0x110030ULL));
    if (condition_is_equal) goto loc_008E9BD9;
    a1 = (unsigned int)((a1) - (8));
    if (condition_is_equal) goto loc_008E9BD9;
    a1 = (unsigned int)((a1) - (0x2FC4ULL));
    if (condition_is_equal) goto loc_008E9BD9;
    a1 = (unsigned int)((a1) - (0x1010ULL));
    if (condition_is_equal) goto loc_008E9BD9;
loc_008EAAD4:
    if (((unsigned int)(a1)) == 0x800BULL) goto loc_008E9BD9;
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 184) + 2008))) & (4));
    v_rdi = (unsigned __int8)(((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 184) + 2008)))) & (2));
    if (condition_is_not_equal) goto loc_008EAAFB;
    if ((unsigned __int8)(result) == 0) goto loc_008E9BD9;
loc_008EAAFB:
    a1 = ((unsigned __int8)(v_rdi) != 0) ? 1 : 0;
    a1 = (unsigned int)((a1) + 1);
    result = EtwTimLogProhibitFsctlSystemCalls(a1, *(unsigned __int64 *)(result + 184), a3, *(unsigned __int64 *)(result + 184));
    if ((unsigned __int8)(v_rdi) != 0) goto loc_008EA6EC;
    goto loc_008E9BD9;
loc_008EAB34:
    if (v_stack_p288 == 0) goto loc_008EA6B0;
    v_stack_p30 = v_r14;
    v_stack_p28 = 1;
    v_stack_p20 = v_stack_pC0;
    result = IoSetIoCompletionEx(v_stack_p100, v_stack_p118, v_stack_p288, *(unsigned __int64 *)(result + 184));
    a1 = (unsigned int)(v_stack_pB8);
    if (sign_flag) { a1 = (unsigned int)((unsigned int)(0xC000009AULL)); }
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (0xC0000000ULL));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x80000000ULL)))) { a1 = 259; }
    v_stack_pB8 = (unsigned int)(a1);
    goto loc_008EA6B0;
loc_008EAB9E:
    if (((v_stack_pC8) & (2)) == 0) { result = (unsigned int)((unsigned int)(0xC000A2A2ULL)); }
    goto loc_008EA85E;
loc_008EABB3:
    result = AstAddBloomFilter((unsigned int)(0xC000A2A2ULL), *(unsigned __int64 *)(v_rip - 9347417 + *(unsigned __int64 *)(v_stack_m1E0 + 24) + *(unsigned __int64 *)(v_stack_m1E0 + 24) * 2 * 8 + 6560), (unsigned int)((unsigned int)((unsigned int)(0x80000000ULL))), *(unsigned __int64 *)(result + 184));
    a2 = 0;
    result = memset(v_stack_p170, a2, a2 + 64, *(unsigned __int64 *)(result + 184));
    if (((unsigned int)(*(unsigned __int16 *)((unsigned int)(v_stack_p54) + 8))) >= 64) goto loc_008EB0CB;
loc_008EABE2:
    result = memcpy_s(v_stack_p170, 64, *(unsigned __int64 *)((unsigned int)(v_stack_p54) + 16), (unsigned int)((unsigned int)(*(unsigned __int16 *)((unsigned int)(v_stack_p54) + 8))));
    v_r11 = (v_stack_p190) << (8);
    v_r11 = (v_r11) ^ (v_stack_p170);
    v_stack_p170 = v_r11;
    v_r10 = (v_stack_p198) << (8);
    v_r10 = (v_r10) ^ (v_stack_p178);
    v_stack_p178 = v_r10;
    a3 = (v_stack_p1A0) << (8);
    a3 = (a3) ^ (v_stack_p180);
    v_stack_p180 = a3;
    a4 = (v_stack_p1A8) << (8);
    a4 = (a4) ^ (v_stack_p188);
    v_stack_p188 = a4;
    result = (a3) >> (24);
    a1 = (v_stack_p170) * ((unsigned __int8)(result));
    result = (a3) >> (32);
    a1 = (a1) + ((unsigned __int8)(result));
    a2 = (64) * (a1);
    result = (a3) >> (40);
    a2 = (a2) + ((unsigned __int8)(result));
    a1 = (a1) * (a2);
    result = (a3) >> (48);
    a1 = (a1) + ((unsigned __int8)(result));
    a1 = (a1) * (a1);
    result = (a3) >> (56);
    a1 = (a1) + (result);
    a1 = (a1) * (a1);
    a1 = (a1) + ((unsigned __int8)(a4));
    a2 = (a2) * (a1);
    result = (a4) >> (8);
    a2 = (a2) + ((unsigned __int8)(result));
    a1 = (a1) * (a2);
    result = (a4) >> (16);
    a1 = (a1) + ((unsigned __int8)(result));
    a2 = (a2) * (a1);
    result = (a4) >> (24);
    a2 = (a2) + ((unsigned __int8)(result));
    a1 = (a1) * (a2);
    result = (a4) >> (32);
    a1 = (a1) + ((unsigned __int8)(result));
    a2 = (a2) * (a1);
    result = (a4) >> (40);
    a2 = (a2) + ((unsigned __int8)(result));
    a1 = (a1) * (a2);
    result = (a4) >> (48);
    a1 = (a1) + ((unsigned __int8)(result));
    a2 = (a2) * (a1);
    result = (v_r11) >> (32);
    a1 = ((unsigned __int8)(result)) * (result);
    a2 = (a2) + (a1);
    result = (a3) >> (16);
    a1 = ((unsigned __int8)(result)) * (result);
    a2 = (a2) + (a1);
    result = (v_r10) >> (24);
    a1 = ((unsigned __int8)(result)) * (result);
    a2 = (a2) + (a1);
    result = (v_r11) >> (16);
    a1 = ((unsigned __int8)(result)) * (result);
    a2 = (a2) + (a1);
    result = (v_r10) >> (16);
    a1 = ((unsigned __int8)(result)) * (result);
    a2 = (a2) + (a1);
    result = (a3) >> (8);
    a1 = ((unsigned __int8)(result)) * (result);
    a2 = (a2) + (a1);
    result = (v_r11) >> (24);
    a1 = ((unsigned __int8)(result)) * (result);
    a2 = (a2) + (a1);
    result = (v_r11) >> (8);
    a1 = ((unsigned __int8)(result)) * (result);
    a2 = (a2) + (a1);
    result = (v_r10) >> (8);
    a1 = ((unsigned __int8)(result)) * (result);
    a2 = (a2) + (a1);
    result = (v_r10) >> (32);
    a1 = ((unsigned __int8)(result)) * (result);
    a2 = (a2) + (a1);
    result = (v_r11) >> (40);
    a1 = ((unsigned __int8)(result)) * (result);
    a2 = (a2) + (a1);
    result = (v_r10) >> (48);
    a1 = ((unsigned __int8)(result)) * (result);
    a2 = (a2) + (a1);
    result = (v_r11) >> (48);
    a1 = ((unsigned __int8)(result)) * (result);
    a2 = (a2) + (a1);
    result = (v_r10) >> (40);
    a1 = ((unsigned __int8)(result)) * (result);
    a2 = (a2) + (a1);
    result = ((unsigned __int8)(a3)) * (a1);
    a2 = (a2) + (result);
    result = ((unsigned __int8)(v_r10)) * (a1);
    a2 = (a2) + (result);
    result = ((unsigned __int8)(v_r11)) * (a1);
    a2 = (a2) + (result);
    v_r10 = (v_r10) >> (56);
    v_r10 = (v_r10) * (result);
    a2 = (a2) + (v_r10);
    v_r11 = (v_r11) >> (56);
    v_r11 = (v_r11) * (result);
    a2 = (a2) + (v_r11);
    a4 = (a4) >> (56);
    a2 = (a2) + (result);
    a2 = (a2) + (a4);
    if ((*(unsigned int *)(v_rip + 5357546)) <= 5) goto loc_008E9F9B;
    if (((*(unsigned __int64 *)(v_rip + 5357539)) & (a3)) != 0) goto loc_008EB2F3;
loc_008EAF43:
    result = 0;
loc_008EAF45:
    if (0 == 0) goto loc_008E9F9B;
    v_stack_p120 = (unsigned int)(0x80000000ULL);
    v_stack_p1D0 = v_stack_p120;
    v_stack_p1D8 = 8;
    v_stack_p128 = v_stack_p80;
    v_stack_p1E0 = v_stack_p128;
    v_stack_p1E8 = 8;
    v_stack_pF8 = (unsigned int)((unsigned int)(0x80000000ULL));
    v_stack_p1F0 = v_stack_pF8;
    v_stack_p1F8 = 4;
    v_stack_p130 = a2;
    v_stack_p200 = v_stack_p130;
    v_stack_p208 = 8;
    v_stack_pFC = (unsigned int)(*(unsigned __int16 *)((unsigned int)(v_stack_p54) + 8));
    v_stack_p210 = v_stack_pFC;
    v_stack_p218 = 4;
    v_stack_p28 = v_stack_p1B0;
    v_stack_p20 = 7;
    a4 = 0;
    a3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 5357269, v_rip - 9061422, a3, a4);
    goto loc_008E9F9B;
loc_008EB045:
    v_stack_p20 = v_stack_p70;
    result = IopWaitAndAcquireFileObjectLock(v_stack_p88, (unsigned __int8)(v_stack_p100), (unsigned __int8)((unsigned int)(v_stack_p54)), result);
    goto loc_008EA759;
loc_008EB071:
    if (v_stack_p100 != 0) goto loc_008EB0D6;
loc_008EB076:
    goto loc_008EA680;
loc_008EB083:
    if (v_stack_p51 == 0) { v_r12 = 3; }
    goto loc_008EA2F7;
loc_008EB096:
    v_stack_p78 = *(unsigned __int64 *)(v_stack_p88 + 8);
    result = MmIsDriverVerifying(*(unsigned __int64 *)(v_stack_p88 + 8), (unsigned __int8)(v_stack_p100), (unsigned __int8)((unsigned int)(v_stack_p54)), result);
    if ((unsigned int)(result) == 0) goto loc_008EB2E6;
    result = VfFastIoSnapState(v_stack_p78, (unsigned __int8)(v_stack_p100), (unsigned __int8)((unsigned int)(v_stack_p54)), result);
    v_stack_p78 = result;
    goto loc_008EA12A;
loc_008EB0CB:
    goto loc_008EABE2;
loc_008EB0D6:
    a4 = (unsigned int)((64) & (0xC0000000ULL));
    if (((unsigned int)(a4)) == ((unsigned int)((unsigned int)(0x80000000ULL)))) goto loc_008EA66B;
    goto loc_008EB076;
loc_008EB0E8:
    if (v_stack_p58 != 0) goto loc_008EA441;
    result = *(unsigned __int64 *)((unsigned int)(v_stack_p54) + 24);
    if (((unsigned int)((unsigned int)(0x80000000ULL))) == 0x9040CULL) {
        result = (*(unsigned __int64 *)((unsigned int)(v_stack_p54) + 24)) + (32);
    }
    if ((*(unsigned int *)(result)) != 0xA0000003ULL) goto loc_008EA441;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_pF0))) >> (1));
    result = (unsigned __int8)((result) & (1));
    v_stack_p20 = (unsigned __int8)(result);
    a4 = 0;
    result = IopExceptionCleanupEx(v_stack_p88, (unsigned int)(v_stack_p54), v_stack_p98, a4);
    goto loc_008EA473;
loc_008EB142:
    if (((unsigned int)((unsigned int)(v_stack_p54))) < 36) goto loc_008E9DED;
loc_008EB14C:
    v_stack_p138 = v_xmm0;
    v_stack_p148 = v_xmm0;
    result = IoThreadToProcess(v_stack_pE8, (unsigned int)(v_stack_p54), v_stack_p98, a4);
    result = SeCaptureSubjectContextEx(v_stack_pE8, result, v_stack_p138, a4);
    result = RtlIsSandboxedToken(v_stack_p138, (unsigned __int8)(v_stack_p100), v_stack_p138, a4);
    v_stack_p51 = (unsigned __int8)(result);
    v_stack_p50 = (unsigned __int8)(result);
    result = SeReleaseSubjectContext(v_stack_p138, (unsigned __int8)(v_stack_p100), v_stack_p138, a4);
    if (v_stack_p51 == 0) goto loc_008E9DED;
    v_stack_pCC = (unsigned int)(v_r14);
    if (((unsigned int)((unsigned int)(0x80000000ULL))) != 0x9040CULL) goto loc_008EB245;
    goto loc_008EB248;
loc_008EB1D4:
    result = v_stack_p98;
    if (v_stack_p98 != 0) {
        a1 = v_stack_p98;
        result = ObfDereferenceObject(a1, (unsigned __int8)(v_stack_p100), (unsigned int)(*(unsigned int *)(v_stack_pA8 + 32)), a4);
    }
    if (v_stack_pE0 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_pE0, a2, (unsigned int)(*(unsigned int *)(v_stack_pA8 + 32)), a4);
    }
    result = ObfDereferenceObject(v_stack_p88, a2, (unsigned int)(*(unsigned int *)(v_stack_pA8 + 32)), a4);
    goto loc_008EA473;
loc_008EB20C:
    result = IopSetFileObjectExtensionFlag(v_stack_p88, 16, (unsigned int)(*(unsigned int *)(v_stack_pA8 + 32)), a4);
    v_stack_p78 = (unsigned int)(result);
    if (!sign_flag) goto loc_008E9D55;
    result = ObfDereferenceObject(v_stack_p88, 16, (unsigned int)(*(unsigned int *)(v_stack_pA8 + 32)), a4);
    goto loc_008EA473;
loc_008EB236:
    if (((unsigned int)((unsigned int)(v_stack_p54))) < 4) goto loc_008E9DE0;
    goto loc_008EB14C;
loc_008EB245:
loc_008EB248:
    v_stack_pCC = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p88)));
    goto loc_008EB2C3;
loc_008EB2C3:
    if (!sign_flag) goto loc_008EB31B;
loc_008EB2C7:
    result = ObfDereferenceObject(v_stack_p98, (unsigned int)(v_stack_p78), (unsigned int)(*(unsigned int *)(v_stack_p88)), a4);
loc_008EB2E6:
    goto loc_008EA125;
loc_008EB2F3:
    result = (*(unsigned __int64 *)(v_rip + 5356590)) & ((unsigned int)(*(unsigned int *)(v_stack_p88)));
    if (result != (*(unsigned __int64 *)(v_rip + 5356580))) goto loc_008EAF43;
    goto loc_008EAF45;
loc_008EB311:
    if (!sign_flag) goto loc_008E9DED;
    goto loc_008EB2C7;
loc_008EB31B:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p88)))) != 0xA0000003ULL) goto loc_008EB311;
    v_stack_p58 = 1;
    v_stack_p28 = v_stack_p60;
    v_stack_p20 = v_stack_pE0;
    result = IopValidateJunctionTarget((unsigned int)((unsigned int)((unsigned int)(0x80000000ULL))), v_stack_p98, (unsigned int)((unsigned int)((unsigned int)(v_stack_p54))), 1);
    v_stack_p78 = (unsigned int)(result);
    goto loc_008EB311;
loc_008EB359:
loc_008EB361:
    v_stack_p40 = v_stack_p80;
    v_stack_p38 = v_stack_pB8;
    v_stack_p30 = (unsigned int)((unsigned int)(0x80000000ULL));
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_p54));
    v_stack_p20 = v_stack_pB0;
loc_008EB3AC:
    result = ObfDereferenceObject(v_stack_pA0, 1, v_stack_pA8, (unsigned int)(v_stack_p60));
    goto loc_008EA79D;
loc_008EB3B9:
    result = IopReleaseFileObjectLock(v_stack_p88, 1, v_stack_pA8, (unsigned int)(v_stack_p60));
    goto loc_008EA7AF;
}
```

## 5. (Beta) C Style

```c
int64_t IopXxxControlFile(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, int64_t Arg7, uint32_t Arg8, int64_t Arg9, uint32_t Arg10, uint8_t Arg11, uint8_t Arg12)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m158;
    uint32_t v_stack_m15C;
    uint64_t v_stack_m160;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint32_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint32_t v_stack_m1F0;
    uint8_t v_stack_m1F6;
    uint32_t v_stack_m200;
    uint32_t v_stack_m208;
    uint8_t v_stack_m210;
    uint32_t v_stack_m214;
    uint8_t v_stack_m216;
    uint8_t v_stack_m217;
    uint8_t v_stack_m218;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint32_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m48;
    uint64_t v_stack_p100;
    uint32_t v_stack_p10C;
    uint64_t v_stack_p118;
    uint64_t v_stack_p120;
    uint64_t v_stack_p128;
    uint64_t v_stack_p130;
    uint64_t v_stack_p138;
    uint64_t v_stack_p148;
    uint64_t v_stack_p158;
    uint64_t v_stack_p170;
    uint64_t v_stack_p178;
    uint64_t v_stack_p18;
    uint64_t v_stack_p180;
    uint64_t v_stack_p188;
    uint64_t v_stack_p190;
    uint64_t v_stack_p198;
    uint64_t v_stack_p1A0;
    uint64_t v_stack_p1A8;
    uint64_t v_stack_p1B0;
    uint64_t v_stack_p1D0;
    uint64_t v_stack_p1D8;
    uint64_t v_stack_p1E0;
    uint64_t v_stack_p1E8;
    uint64_t v_stack_p1F0;
    uint64_t v_stack_p1F8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p200;
    uint64_t v_stack_p208;
    uint64_t v_stack_p210;
    uint64_t v_stack_p218;
    uint8_t v_stack_p28;
    uint64_t v_stack_p280;
    uint64_t v_stack_p288;
    uint32_t v_stack_p298;
    uint8_t v_stack_p2C0;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint8_t v_stack_p50;
    uint8_t v_stack_p51;
    uint8_t v_stack_p52;
    uint32_t v_stack_p54;
    uint8_t v_stack_p58;
    uint32_t v_stack_p60;
    uint32_t v_stack_p68;
    uint8_t v_stack_p70;
    uint8_t v_stack_p71;
    uint32_t v_stack_p78;
    uint32_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_p98;
    uint32_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint32_t v_stack_pC0;
    uint32_t v_stack_pC8;
    uint32_t v_stack_pCC;
    uint64_t v_stack_pD0;
    uint64_t v_stack_pD8;
    uint64_t v_stack_pE0;
    uint64_t v_stack_pE8;
    uint64_t v_stack_pF0;
    uint32_t v_stack_pF8;
    uint32_t v_stack_pFC;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (560);
    result = (*(uint64_t *)(v_rip + 0x520C4D)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m190 = Arg2;
    v_stack_m1E8 = Arg1;
    v_stack_m1F6 = Arg11;
    v_stack_m178 = Arg2;
    v_stack_m198 = Arg5;
    v_stack_m1C0 = Arg7;
    v_stack_m208 = (uint32_t)((uint32_t)(Arg8));
    v_stack_m1B8 = Arg9;
    v_stack_m200 = (uint32_t)((uint32_t)(Arg10));
    local_r14 = 0;
    v_stack_m1E0 = 0;
    v_stack_m1D0 = 0;
    v_stack_m160 = 0;
    v_stack_m1B0 = v_xmm0;
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) & (3));
    v_stack_m1C8 = (uint32_t)(local_r12);
    v_stack_m180 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m216 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_008EA7FC;
    if (Arg11 == 0) goto loc_008EA885;
loc_008E9BD9:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_008EA7FC;
    Arg1 = v_stack_m198;
    if (v_stack_m198 >= Arg2) { Arg1 = Arg2; }
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    if ((uint32_t)(local_r12) == 0) goto loc_008E9C5D;
loc_008E9C04:
    v_stack_m214 = (uint32_t)((uint32_t)(v_stack_m200));
loc_008E9C0C:
    if (((uint32_t)(local_r12)) == 3) goto loc_008E9CC6;
    if (Arg7 == 0) goto loc_008E9C56;
    if (((Arg12) & (1)) != 0) goto loc_008E9CC6;
    if ((uint32_t)((uint32_t)(v_stack_m208)) == 0) goto loc_008E9CC6;
    if ((Arg7 + (uint32_t)(v_stack_m208) * 1) > Arg2) goto loc_008E9C47;
    if ((Arg7 + (uint32_t)(v_stack_m208) * 1) >= Arg7) goto loc_008E9CC6;
loc_008E9C47:
    v_stack_m214 = (uint32_t)((uint32_t)(v_stack_m200));
    goto loc_008E9CC6;
loc_008E9C56:
    v_stack_m208 = 0;
    goto loc_008E9CC6;
loc_008E9C5D:
    if (Arg9 == 0) goto loc_008E9CB1;
    v_stack_m214 = (uint32_t)((uint32_t)(v_stack_m200));
    if ((uint32_t)((uint32_t)(v_stack_m200)) == 0) goto loc_008E9CAB;
    Arg4 = ((uint32_t)(v_stack_m200) - 1) + (Arg9);
    if (Arg9 > Arg4) goto loc_008E9CC0;
    if (Arg4 >= Arg2) goto loc_008E9CC0;
    Arg4 = (Arg4) & (0xFFFFFFFFFFFFF000ULL);
    Arg4 = (Arg4) + (0x1000ULL);
loc_008E9C90:
    *(uint8_t *)(Arg9) = (uint8_t)(*(uint8_t *)(Arg9));
    result = (Arg9) & (0xFFFFFFFFFFFFF000ULL);
    result = (result) + (0x1000ULL);
    if (result != Arg4) goto loc_008E9C90;
    goto loc_008E9C04;
loc_008E9CAB:
    goto loc_008E9C0C;
loc_008E9CB1:
    v_stack_m214 = 0;
    v_stack_m200 = 0;
    goto loc_008E9C0C;
loc_008E9CC0:
    result = ExRaiseAccessViolation(*(uint8_t *)(Arg9), Arg9, Arg7, Arg4);
loc_008E9CC6:
    goto loc_008E9CD5;
loc_008E9CD5:
    v_stack_m248 = v_stack_m160;
    Arg2 = 0;
    result = IopReferenceFileObject(Arg1, Arg2, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_m1E0);
    v_stack_m1F0 = (uint32_t)(result);
    if (sign_flag) goto loc_008EA473;
    if ((*(uint64_t *)(v_stack_m1E0 + 0xB0)) != 0) goto loc_008EA7D8;
loc_008E9D1A:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_008E9D2E;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) >> (14));
    Arg1 = (uint32_t)((Arg1) & (3));
    if (condition_is_not_equal) goto loc_008EA6D3;
loc_008E9D2E:
    if (((uint32_t)((uint32_t)(Arg6))) == 0x94264ULL) goto loc_008EA809;
    if (((uint32_t)((uint32_t)(Arg6))) == 0x98268ULL) goto loc_008EA809;
    if (((uint32_t)((uint32_t)(Arg6))) == 0x9042CULL) goto loc_008EB20C;
loc_008E9D55:
    if (v_stack_m190 == 0) goto loc_008E9DB4;
    v_stack_m158 = 0;
    v_stack_m240 = 0;
    v_stack_m248 = v_stack_m158;
    result = ObReferenceObjectByHandle(v_stack_m190, 2, *(uint64_t *)(v_rip + 0x6DCE1F), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    v_stack_m1F0 = (uint32_t)(result);
    v_stack_m1D0 = v_stack_m158;
    if (sign_flag) goto loc_008EA8E4;
    result = KeResetEvent(v_stack_m158, 2, *(uint64_t *)(v_rip + 0x6DCE1F), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
loc_008E9DB4:
    v_stack_m188 = 0;
    v_stack_m217 = 0;
    Arg3 = 0;
    v_stack_m210 = 0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_008E9DED;
    if (((uint32_t)((uint32_t)(Arg6))) == 0x900A4ULL) goto loc_008EB236;
loc_008E9DE0:
    if (((uint32_t)((uint32_t)(Arg6))) == 0x9040CULL) goto loc_008EB142;
loc_008E9DED:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m1E0 + 0x50)))) & (2)) != 0) goto loc_008EA6F6;
    v_stack_m218 = 0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_008EA4B1;
loc_008E9E09:
    if (((*(uint32_t *)(v_stack_m1E0 + 0x50)) & (0x800ULL)) != 0) goto loc_008EA77E;
    result = IoGetRelatedDeviceObject(v_stack_m1E0, 2, Arg3, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
loc_008E9E1E:
    v_stack_m1E8 = result;
    if (Arg11 == 0) goto loc_008EA1EF;
    if ((*(uint8_t *)(v_rip + 0x6A3220)) == 0) goto loc_008E9F9B;
    if ((*(uint32_t *)(v_rip + 0x51D0CB)) > 0) goto loc_008EA8F4;
    result = 0;
loc_008E9E4D:
    if (0 == 0) goto loc_008E9F9B;
    if ((((uint8_t)(*(uint8_t *)(result - 0x30 + 0x1A))) & (2)) != 0) goto loc_008EA497;
loc_008E9E69:
    if (0 == 0) goto loc_008E9F9B;
    local_r10 = ((uint32_t)((uint32_t)((uint32_t)(Arg6)))) << (32);
    result = (0) >> (4);
    local_r10 = (local_r10) ^ (result);
    v_stack_m108 = local_r10;
    Arg1 = (v_stack_m1E0) * ((uint32_t)(*(uint32_t *)(v_rip + 0x6A31B8)));
    Arg1 = (Arg1) + ((uint8_t)(local_r10));
    Arg2 = (2) * (Arg1);
    result = (local_r10) >> (8);
    Arg2 = (Arg2) + ((uint8_t)(result));
    Arg1 = (Arg1) * (Arg2);
    result = (local_r10) >> (16);
    Arg1 = (Arg1) + ((uint8_t)(result));
    Arg2 = (Arg2) * (Arg1);
    result = (local_r10) >> (24);
    Arg2 = (Arg2) + ((uint8_t)(result));
    Arg1 = (Arg1) * (Arg2);
    result = (local_r10) >> (32);
    Arg1 = (Arg1) + ((uint8_t)(result));
    Arg2 = (Arg2) * (Arg1);
    result = (local_r10) >> (40);
    Arg2 = (Arg2) + ((uint8_t)(result));
    Arg1 = (Arg1) * (Arg2);
    result = (local_r10) >> (48);
    Arg1 = (Arg1) + ((uint8_t)(result));
    Arg3 = (Arg3) * (Arg1);
    Arg1 = (local_r10) >> (56);
    Arg3 = (Arg3) + (Arg1);
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg3))) >> (16));
    Arg2 = 0;
    v_stack_m1C8 = 0;
    Arg2 = 0;
    Arg2 = 0;
    result = (0) >> (3);
    Arg2 = (uint32_t)((Arg2) & (7));
    result = (uint8_t)((*(uint8_t *)(result + *(uint64_t *)(v_rip + 0x6A30FF) * 1)) >> ((uint8_t)((uint8_t)(Arg2))));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_008EABB3;
    result = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m1C8)))) >> (3);
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m1C8)) & (7));
    result = (uint8_t)((*(uint8_t *)(result + *(uint64_t *)(v_rip + 0x6A30FF) * 1)) >> ((uint8_t)(Arg1)));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_008EABB3;
    result = (0) >> (3);
    local_r10 = (uint32_t)((0) & (7));
    result = (uint8_t)((*(uint8_t *)(result + *(uint64_t *)(v_rip + 0x6A30FF) * 1)) >> ((uint8_t)((uint8_t)(local_r10))));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_008EABB3;
loc_008E9F9B:
    if (Arg11 == 0) goto loc_008EA1EF;
    if (v_stack_m217 != 0) goto loc_008EA1EF;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m1E8 + 0x8) + 0x50) == 0) goto loc_008EA1EF;
    v_stack_m1C8 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m1E8 + 0x8) + 0x50) + 0x50);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m1E8 + 0x8) + 0x50) + 0x50) == 0) goto loc_008EA1EF;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_008EA0EA;
    if (v_stack_m1B8 == 0) goto loc_008EA0EA;
    if (((uint32_t)(local_r12)) == 1) goto loc_008EA07B;
    if (((uint32_t)(local_r12)) != 2) goto loc_008EA0AE;
    if ((uint32_t)((uint32_t)(v_stack_m214)) == 0) goto loc_008EA072;
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m214)))) - 1;
    Arg3 = (Arg3) + (v_stack_m1B8);
    if (v_stack_m1B8 > Arg3) goto loc_008EA075;
    if (Arg3 >= ((uint32_t)(v_stack_m214))) goto loc_008EA075;
    Arg3 = (Arg3) & (0xFFFFFFFFFFFFF000ULL);
    Arg3 = (Arg3) + (0x1000ULL);
loc_008EA040:
    *(uint8_t *)(v_stack_m1B8) = (uint8_t)(*(uint8_t *)(v_stack_m1B8));
    Arg1 = (v_stack_m1B8) & (0xFFFFFFFFFFFFF000ULL);
    Arg1 = (Arg1) + (0x1000ULL);
    if (Arg1 != Arg3) goto loc_008EA040;
    v_stack_m214 = (uint32_t)((uint32_t)(v_stack_m200));
    goto loc_008EA0AE;
loc_008EA072:
    goto loc_008EA0AE;
loc_008EA075:
    result = ExRaiseAccessViolation(v_stack_m1E8, v_stack_m1B8, Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0x6A31AE)));
loc_008EA07B:
    if ((uint32_t)((uint32_t)(v_stack_m214)) == 0) goto loc_008EA0AE;
    if ((v_stack_m1B8 + (uint32_t)(v_stack_m214) * 1) < v_stack_m1B8) goto loc_008EA09B;
    result = (uint32_t)(v_stack_m214);
    local_rdi = v_stack_m1E0;
    if ((v_stack_m1B8 + (uint32_t)(v_stack_m214) * 1) >= = ((uint32_t)(v_stack_m214))) {
        result = *(uint8_t *)((uint32_t)(v_stack_m214));
        local_rdi = v_stack_m1E0;
        result = v_stack_m200;
        v_stack_m214 = (uint32_t)(result);
    }
    goto loc_008EA0EA;
loc_008EA0EA:
    if (((uint32_t)((uint32_t)(Arg6))) != 0x90020ULL) goto loc_008EA8DA;
    v_stack_m214 = (uint32_t)((uint32_t)(v_stack_m200));
loc_008EA117:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x61A903)))) & (16)) != 0) goto loc_008EB096;
loc_008EA125:
    v_stack_m1F0 = 0;
loc_008EA12A:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m1E8 + 0x8) + 0x50) + 0x50)) != (v_rip + 9343)) goto loc_008EB361;
    Arg1 = 0;
    v_stack_m216 = 0;
    if ((*(uint64_t *)(v_stack_m1E0 + 0x18)) >= 5) goto loc_008EA1CD;
    if (*(uint64_t *)(v_rip - 0x8EA159 + *(uint64_t *)(v_stack_m1E0 + 0x18) + *(uint64_t *)(v_stack_m1E0 + 0x18) * 2 * 8 + 0x19A0) == 0) goto loc_008EA1CD;
    v_stack_m228 = v_stack_m1E8;
    v_stack_m230 = v_stack_m1B0;
    v_stack_m238 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m240 = (uint32_t)((uint32_t)(v_stack_m200));
    v_stack_m248 = v_stack_m1B8;
    if ((*(uint64_t *)(v_rip - 0x8EA159 + *(uint64_t *)(v_stack_m1E0 + 0x18) + *(uint64_t *)(v_stack_m1E0 + 0x18) * 2 * 8 + 0x19A0)) != (v_rip + 4707)) goto loc_008EB359;
    result = PiCMFastIoDeviceDispatch(v_stack_m1E0, 1, v_stack_m1C0, (uint32_t)(v_stack_m208));
    v_stack_m216 = (uint8_t)(result);
loc_008EA1CD:
    result = v_stack_m1F0;
    if (v_stack_m1F0 != 0) {
        Arg2 = v_stack_m1C8;
        Arg1 = v_stack_m1F0;
        result = VfFastIoCheckState(Arg1, Arg2, v_stack_m1C0, (uint32_t)(v_stack_m208));
        Arg1 = v_stack_m216;
    }
    if ((uint8_t)(Arg1) != 0) goto loc_008EA5AA;
loc_008EA1EF:
    v_stack_m178 = v_stack_m1E0 + 80;
    result = v_stack_m1E0 + 80;
    if (((*(uint32_t *)(v_stack_m1E0 + 0x50)) & (0x4000000ULL)) == 0) {
        Arg1 = v_stack_m1E0 + 152;
        result = KeResetEvent(Arg1, Arg2, v_stack_m1C0, (uint32_t)(v_stack_m208));
    }
    Arg3 = (uint8_t)((v_stack_m218) ^ (1));
    result = IopAllocateIrpExReturn(v_stack_m1E8, *(uint8_t *)(v_stack_m1E8 + 0x4C), Arg3, (uint32_t)(v_stack_m208));
    v_stack_m190 = result;
    if (result == 0) goto loc_008EA78C;
    *(uint64_t *)(result + 0xC0) = v_stack_m1E0;
    *(uint64_t *)(result + 0x98) = v_stack_m180;
    *(uint64_t *)(result + 0xA0) = 0;
    *(uint8_t *)(result + 0x40) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    *(uint8_t *)(result + 0x41) = 0;
    *(uint8_t *)(result + 0x44) = 0;
    *(uint64_t *)(result + 0x68) = 0;
    *(uint64_t *)(result + 0x50) = v_stack_m1D0;
    *(uint64_t *)(result + 0x48) = v_stack_m198;
    *(uint64_t *)(result + 0x58) = v_stack_p18;
    *(uint64_t *)(result + 0x60) = v_stack_p20;
    Arg2 = (*(uint64_t *)(result + 0xB8)) - (72);
    v_stack_m1F0 = Arg2;
    result = ((uint8_t)(v_stack_m1F6) != 0) ? 1 : 0;
    result = (uint32_t)((result) + (13));
    *(uint32_t *)(Arg2) = (uint32_t)(result);
    *(uint64_t *)(Arg2 + 0x30) = v_stack_m1E0;
    *(uint32_t *)(Arg2 + 0x8) = (uint32_t)((uint32_t)(v_stack_m214));
    *(uint32_t *)(Arg2 + 0x10) = (uint32_t)((uint32_t)(v_stack_m208));
    *(uint32_t *)(Arg2 + 0x18) = (uint32_t)((uint32_t)(Arg6));
    *(uint64_t *)(result + 0x8) = 0;
    *(uint64_t *)(result + 0x18) = 0;
    if (((*(uint32_t *)(v_stack_m1E8 + 0x30)) & (0x80000ULL)) != 0) goto loc_008EB083;
loc_008EA2F7:
    if ((uint32_t)(local_r12) != 0) goto loc_008EA56B;
    *(uint64_t *)(Arg2 + 0x20) = 0;
    if ((uint32_t)((uint32_t)(v_stack_m208)) != 0) goto loc_008EA316;
    if ((uint32_t)((uint32_t)(v_stack_m214)) == 0) goto loc_008EA39A;
loc_008EA316:
    if (v_stack_m188 != 0) goto loc_008EA394;
    Arg2 = (uint32_t)((uint32_t)((uint32_t)(v_stack_m214)));
    if (((uint32_t)((uint32_t)(v_stack_m208))) > ((uint32_t)((uint32_t)(v_stack_m214)))) { Arg2 = (uint32_t)((uint32_t)(v_stack_m208)); }
    Arg1 = 105;
    if ((uint8_t)(v_stack_m1F6) == 0) { Arg1 = 97; }
    result = ExAllocatePool2(Arg1, Arg2, (uint32_t)(0x42536F49ULL), (uint32_t)(v_stack_m208));
    *(uint64_t *)(result + 0x18) = result;
    result = v_stack_m1C0;
    if (v_stack_m1C0 != 0) {
        Arg3 = v_stack_m208;
        Arg2 = v_stack_m1C0;
        result = memcpy(result, Arg2, Arg3, (uint32_t)(v_stack_m208));
    }
loc_008EA371:
    *(uint32_t *)(result + 0x10) = 48;
    *(uint64_t *)(result + 0x70) = v_stack_m1B8;
    if ((uint32_t)((uint32_t)(v_stack_m214)) == 0) goto loc_008EA3A2;
    *(uint32_t *)(result + 0x10) = 112;
    goto loc_008EA3A2;
loc_008EA394:
    *(uint64_t *)(result + 0x18) = v_stack_m1B8;
    goto loc_008EA371;
loc_008EA39A:
    *(uint32_t *)(result + 0x10) = 0;
    *(uint64_t *)(result + 0x70) = 0;
loc_008EA3A2:
    goto loc_008EA3DA;
loc_008EA3DA:
    result = v_stack_m1B8;
    local_r12 = (uint32_t)(v_stack_m214);
    if (((uint32_t)((uint32_t)(v_stack_m208))) < ((uint32_t)((uint32_t)(v_stack_m214)))) {
        local_r12 = (uint32_t)(((uint32_t)(v_stack_m214)) - ((uint32_t)((uint32_t)(v_stack_m208))));
        Arg3 = (uint32_t)(local_r12);
        Arg1 = ((uint32_t)(v_stack_m208)) + (*(uint64_t *)(result + 0x18));
        Arg2 = 0;
        result = memset(Arg1, Arg2, Arg3, (uint32_t)(v_stack_m208));
        Arg2 = v_stack_m1F0;
    }
    Arg1 = (uint8_t)(((uint8_t)((uint32_t)(v_stack_m15C))) & (2));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(Arg1)));
    result = (uint8_t)(((uint32_t)(v_stack_m15C)) & (1));
    Arg1 = (uint8_t)((Arg1) | ((uint8_t)(result)));
    if (Arg11 == 0) {
    }
    local_rdi = v_stack_m1E0;
    if (((uint32_t)((uint32_t)(Arg6))) == 0x90020ULL) {
        result = *(uint64_t *)(v_rip + 0x6DABE1);
        local_rdi = v_stack_m1E0;
    }
    if (v_stack_m217 != 0) goto loc_008EB0E8;
loc_008EA441:
    Arg4 = (v_stack_m1F6 == 0) ? 1 : 0;
    v_stack_m238 = 2;
    v_stack_m240 = (uint8_t)(v_stack_m218);
    v_stack_m248 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    result = IopSynchronousServiceTail(v_stack_m1E8, result, local_rdi, Arg4);
loc_008EA473:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, result, local_rdi, Arg4);
    local_rsp = (local_rsp) + (560);
    return result;
loc_008EA497:
    result = (uint32_t)((result) & (3));
    local_r13 = (result) - (*(uint8_t *)(result + v_rip - 0x8EA4A1 * 1 + 0xF0FF80));
    goto loc_008E9E69;
loc_008EA4B1:
    v_stack_p158 = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x310)) == 0) goto loc_008EA51A;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC))) != 332) goto loc_008EA510;
loc_008EA4E4:
    Arg2 = (v_stack_p280) | (1);
    *(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_pD0))) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_pD0)))));
    v_stack_pD0 = (uint32_t)(*(uint32_t *)(v_stack_pD0));
    v_stack_p280 = Arg2;
    goto loc_008EA51A;
loc_008EA510:
    if (((uint16_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_pD0)))))) == 452) goto loc_008EA4E4;
loc_008EA51A:
    v_stack_p54 = (uint32_t)((uint32_t)(v_stack_p68));
    goto loc_008E9E09;
loc_008EA56B:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) - (1));
    if (condition_is_equal) goto loc_008EA967;
    result = (uint32_t)((result) - (1));
    if (condition_is_equal) goto loc_008EA967;
    if (((uint32_t)(result)) != 1) goto loc_008EA3F5;
    *(uint32_t *)(local_r13 + 0x10) = 0;
    *(uint64_t *)(local_r13 + 0x70) = v_stack_pB0;
    *(uint64_t *)(Arg2 + 0x20) = v_stack_pA8;
    goto loc_008EA3F5;
loc_008EA5AA:
    v_stack_p100 = 0;
    v_stack_p118 = 0;
    v_stack_p71 = 0;
    if (((v_stack_p280) & (1)) != 0) goto loc_008EA5E1;
    *(uint64_t *)(v_stack_pD0) = v_xmm0;
    goto loc_008EA5FC;
loc_008EA5E1:
    *(uint32_t *)(v_stack_pD0 + 0x4) = (uint32_t)((uint32_t)(v_stack_pC0));
    *(uint32_t *)(v_stack_pD0) = (uint32_t)((uint32_t)(v_stack_pB8));
loc_008EA5FC:
    goto loc_008EA64B;
loc_008EA64B:
    if ((*(uint64_t *)(v_stack_p88 + 0xB0)) != 0) goto loc_008EA908;
loc_008EA659:
    if (v_stack_pD8 == 0) goto loc_008EA690;
    if (((*(uint32_t *)(v_stack_p88 + 0x50)) & (0x8000000ULL)) != 0) goto loc_008EB071;
loc_008EA66B:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_stack_p98, Arg2, Arg3, (uint32_t)(v_stack_pB8));
loc_008EA680:
    result = ObfDereferenceObject(v_stack_p98, Arg2, Arg3, (uint32_t)(v_stack_pB8));
loc_008EA690:
    if (v_stack_p50 != 0) {
        Arg1 = v_stack_p88;
        result = IopReleaseFileObjectLock(Arg1, Arg2, Arg3, (uint32_t)(v_stack_pB8));
        Arg4 = v_stack_pB8;
    }
    if (0 != 0) goto loc_008EAB34;
loc_008EA6B0:
    if (v_stack_p71 != 0) {
        Arg1 = v_stack_p88;
        result = IopDecrementCompletionContextUsageCount(Arg1, Arg2, Arg3, Arg4);
    }
    result = ObfDereferenceObject(v_stack_p88, Arg2, Arg3, Arg4);
    goto loc_008EA473;
loc_008EA6D3:
    result = (uint32_t)(((uint32_t)(v_stack_p10C)) & ((uint32_t)(v_stack_p88)));
    if (((uint32_t)(result)) == ((uint32_t)(v_stack_p88))) goto loc_008E9D2E;
    result = ObfDereferenceObject(v_stack_p88, Arg2, Arg3, Arg4);
loc_008EA6EC:
    goto loc_008EA473;
loc_008EA6F6:
    local_r13 = (uint32_t)((local_r13) >> (2));
    local_r13 = (uint8_t)((local_r13) & (1));
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_p88 + 128, Arg2, Arg3, Arg4);
    v_stack_p70 = 0;
    if (1 != 0) goto loc_008EB045;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = ObfReferenceObject(v_stack_p88, Arg2, Arg3, Arg4);
loc_008EA759:
    if (v_stack_p70 != 0) goto loc_008EB1D4;
    v_stack_p50 = 1;
    v_stack_p54 = (uint32_t)((uint32_t)(v_stack_p68));
    goto loc_008E9E09;
loc_008EA77E:
    result = IoGetAttachedDevice(*(uint64_t *)(v_stack_p88 + 0x8), Arg2, Arg3, Arg4);
    goto loc_008E9E1E;
loc_008EA78C:
    if (v_stack_p98 != 0) goto loc_008EB3AC;
loc_008EA79D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_pF0)))) & (2)) != 0) goto loc_008EB3B9;
loc_008EA7AF:
    result = ObfDereferenceObject(v_stack_p88, Arg2, Arg3, Arg4);
    result = v_stack_pE0;
    if (v_stack_pE0 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_pE0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_008EA473;
loc_008EA7D8:
    if (((v_stack_p280) & (-2)) == 0) goto loc_008E9D1A;
    result = ObfDereferenceObject(v_stack_p88, Arg2, Arg3, Arg4);
    goto loc_008EA473;
loc_008EA7FC:
    v_stack_p54 = (uint32_t)((uint32_t)(v_stack_p68));
    goto loc_008E9CD5;
loc_008EA809:
    v_stack_pC8 = 0;
    if (((*(uint32_t *)((uint32_t)(v_stack_p68) + 0x50)) & (0x800ULL)) == 0) goto loc_008EA8FB;
    result = IoGetAttachedDevice(*(uint64_t *)((uint32_t)(v_stack_p68) + 0x8), Arg2, Arg3, Arg4);
loc_008EA827:
    result = FsRtlGetSupportedFeatures(result, v_stack_pC8, Arg3, Arg4);
    v_stack_p80 = (uint32_t)(result);
    if (sign_flag) goto loc_008EA865;
    if (((uint32_t)((uint32_t)(0x80000000ULL))) != 0x94264ULL) goto loc_008EAB9E;
    if (((v_stack_pC8) & (1)) != 0) goto loc_008EA865;
loc_008EA85E:
    v_stack_p80 = (uint32_t)((uint32_t)(0xC000A2A1ULL));
loc_008EA865:
    v_stack_p78 = (uint32_t)((uint32_t)(0xC000A2A1ULL));
    if (!sign_flag) goto loc_008E9D55;
    result = ObfDereferenceObject((uint32_t)(v_stack_p68), v_stack_pC8, Arg3, Arg4);
    goto loc_008EA473;
loc_008EA885:
    if (((uint32_t)((uint32_t)(0x80000000ULL))) == 0x113000ULL) goto loc_008E9BD9;
    if (((uint32_t)((uint32_t)(0x80000000ULL))) > 0x110028ULL) goto loc_008EAA9E;
    if (((uint32_t)((uint32_t)(0x80000000ULL))) == 0x110028ULL) goto loc_008E9BD9;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x80000000ULL)))) - (0x90028ULL));
    if (condition_is_equal) goto loc_008E9BD9;
    Arg1 = (uint32_t)((Arg1) - (0x7FFDCULL));
    if (condition_is_equal) goto loc_008E9BD9;
    Arg1 = (uint32_t)((Arg1) - (4));
    if (condition_is_equal) goto loc_008E9BD9;
    Arg1 = (uint32_t)((Arg1) - (16));
    if (condition_is_equal) goto loc_008E9BD9;
    goto loc_008EAAD4;
loc_008EA8DA:
    goto loc_008EA117;
loc_008EA8E4:
    result = ObfDereferenceObject((uint32_t)(v_stack_p68), v_stack_pC8, Arg3, Arg4);
    goto loc_008EA473;
loc_008EA8F4:
    goto loc_008E9E4D;
loc_008EA8FB:
    result = IoGetRelatedDeviceObject((uint32_t)(v_stack_p68), v_stack_pC8, Arg3, Arg4);
    goto loc_008EA827;
loc_008EA908:
    if (((*(uint32_t *)((uint32_t)(v_stack_p68) + 0x50)) & (0x2000000ULL)) == 0) goto loc_008EA922;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) & (0xC0000000ULL));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x80000000ULL)))) goto loc_008EA659;
loc_008EA922:
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) & (0xC0000000ULL));
    if (((uint32_t)(result)) == 0xC0000000ULL) goto loc_008EA659;
    result = IopIncrementCompletionContextUsageCountAndReadData((uint32_t)(v_stack_p68), v_stack_p71, v_stack_p100, v_stack_p118);
    goto loc_008EA659;
loc_008EA967:
    *(uint32_t *)((uint32_t)(v_stack_p54) + 0x10) = 0;
    *(uint64_t *)(v_stack_p71 + 0x20) = 0;
    if ((uint32_t)((uint32_t)(v_stack_p68)) == 0) goto loc_008EA9C6;
    local_rbx = Arg11;
    if (v_stack_pA8 != 0) {
        local_rbx = (uint32_t)(v_stack_p68);
        Arg1 = 107;
        result = 99;
        if ((uint8_t)(v_stack_p100) == 0) { Arg1 = (uint32_t)(result); }
        Arg3 = 0x42536F49ULL;
        Arg2 = local_rbx;
        result = ExAllocatePool2(Arg1, Arg2, Arg3, (uint32_t)(v_stack_pB8));
        *(uint64_t *)((uint32_t)(v_stack_p54) + 0x18) = result;
        Arg3 = local_rbx;
        Arg2 = v_stack_pA8;
        Arg1 = result;
        result = memcpy(Arg1, Arg2, Arg3, (uint32_t)(v_stack_pB8));
        *(uint32_t *)((uint32_t)(v_stack_p54) + 0x10) = 48;
        local_rbx = Arg11;
    }
    if ((uint32_t)((uint32_t)(v_stack_p54)) == 0) goto loc_008EAA5E;
    v_stack_p20 = (uint32_t)(v_stack_p54);
    Arg3 = 0;
    result = IoAllocateMdl(v_stack_pB0, (uint32_t)((uint32_t)((uint32_t)(v_stack_p54))), Arg3, 1);
    v_stack_pE8 = result;
    *(uint64_t *)((uint32_t)(v_stack_p54) + 0x8) = result;
    if (result == 0) {
        Arg1 = 0xC000009AULL;
        result = RtlRaiseStatus(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p54))), Arg3, 1);
    }
    v_stack_pA0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p78)));
    local_r14 = (((uint32_t)(local_r12)) != 1) ? 1 : 0;
    result = MmProbeAndLockPages(Arg1, (uint8_t)(v_stack_p100), (uint32_t)((uint32_t)(local_r14)), 1);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x6DC18A));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x6DC18A)))) & (1)) != 0) {
        Arg2 = v_stack_pA0;
        Arg1 = v_stack_p80;
        result = *(uint64_t *)(Arg1 + 0x8);
        Arg2 = *(uint64_t *)(result + Arg2 * 8 + 0x70);
        Arg3 = Arg1;
        Arg1 = v_stack_pE8;
        result = MmUpdateMdlTracker(Arg1, Arg2, Arg3, 1);
    }
    goto loc_008EA3F5;
loc_008EAA9E:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x80000000ULL)))) - (0x110030ULL));
    if (condition_is_equal) goto loc_008E9BD9;
    Arg1 = (uint32_t)((Arg1) - (8));
    if (condition_is_equal) goto loc_008E9BD9;
    Arg1 = (uint32_t)((Arg1) - (0x2FC4ULL));
    if (condition_is_equal) goto loc_008E9BD9;
    Arg1 = (uint32_t)((Arg1) - (0x1010ULL));
    if (condition_is_equal) goto loc_008E9BD9;
loc_008EAAD4:
    if (((uint32_t)(Arg1)) == 0x800BULL) goto loc_008E9BD9;
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0xB8) + 0x7D8))) & (4));
    local_rdi = (uint8_t)(((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0xB8) + 0x7D8)))) & (2));
    if (condition_is_not_equal) goto loc_008EAAFB;
    if ((uint8_t)(result) == 0) goto loc_008E9BD9;
loc_008EAAFB:
    Arg1 = ((uint8_t)(local_rdi) != 0) ? 1 : 0;
    Arg1 = (uint32_t)((Arg1) + 1);
    result = EtwTimLogProhibitFsctlSystemCalls(Arg1, *(uint64_t *)(result + 0xB8), Arg3, *(uint64_t *)(result + 0xB8));
    if ((uint8_t)(local_rdi) != 0) goto loc_008EA6EC;
    goto loc_008E9BD9;
loc_008EAB34:
    if (v_stack_p288 == 0) goto loc_008EA6B0;
    v_stack_p30 = local_r14;
    v_stack_p28 = 1;
    v_stack_p20 = v_stack_pC0;
    result = IoSetIoCompletionEx(v_stack_p100, v_stack_p118, v_stack_p288, *(uint64_t *)(result + 0xB8));
    Arg1 = (uint32_t)(v_stack_pB8);
    if (sign_flag) { Arg1 = (uint32_t)((uint32_t)(0xC000009AULL)); }
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (0xC0000000ULL));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x80000000ULL)))) { Arg1 = 259; }
    v_stack_pB8 = (uint32_t)(Arg1);
    goto loc_008EA6B0;
loc_008EAB9E:
    if (((v_stack_pC8) & (2)) == 0) { result = (uint32_t)((uint32_t)(0xC000A2A2ULL)); }
    goto loc_008EA85E;
loc_008EABB3:
    result = AstAddBloomFilter((uint32_t)(0xC000A2A2ULL), *(uint64_t *)(v_rip - 0x8EA159 + *(uint64_t *)(v_stack_m1E0 + 0x18) + *(uint64_t *)(v_stack_m1E0 + 0x18) * 2 * 8 + 0x19A0), (uint32_t)((uint32_t)((uint32_t)(0x80000000ULL))), *(uint64_t *)(result + 0xB8));
    Arg2 = 0;
    result = memset(v_stack_p170, Arg2, Arg2 + 64, *(uint64_t *)(result + 0xB8));
    if (((uint32_t)(*(uint16_t *)((uint32_t)(v_stack_p54) + 0x8))) >= 64) goto loc_008EB0CB;
loc_008EABE2:
    result = memcpy_s(v_stack_p170, 64, *(uint64_t *)((uint32_t)(v_stack_p54) + 0x10), (uint32_t)((uint32_t)(*(uint16_t *)((uint32_t)(v_stack_p54) + 0x8))));
    local_r11 = (v_stack_p190) << (8);
    local_r11 = (local_r11) ^ (v_stack_p170);
    v_stack_p170 = local_r11;
    local_r10 = (v_stack_p198) << (8);
    local_r10 = (local_r10) ^ (v_stack_p178);
    v_stack_p178 = local_r10;
    Arg3 = (v_stack_p1A0) << (8);
    Arg3 = (Arg3) ^ (v_stack_p180);
    v_stack_p180 = Arg3;
    Arg4 = (v_stack_p1A8) << (8);
    Arg4 = (Arg4) ^ (v_stack_p188);
    v_stack_p188 = Arg4;
    result = (Arg3) >> (24);
    Arg1 = (v_stack_p170) * ((uint8_t)(result));
    result = (Arg3) >> (32);
    Arg1 = (Arg1) + ((uint8_t)(result));
    Arg2 = (64) * (Arg1);
    result = (Arg3) >> (40);
    Arg2 = (Arg2) + ((uint8_t)(result));
    Arg1 = (Arg1) * (Arg2);
    result = (Arg3) >> (48);
    Arg1 = (Arg1) + ((uint8_t)(result));
    Arg1 = (Arg1) * (Arg1);
    result = (Arg3) >> (56);
    Arg1 = (Arg1) + (result);
    Arg1 = (Arg1) * (Arg1);
    Arg1 = (Arg1) + ((uint8_t)(Arg4));
    Arg2 = (Arg2) * (Arg1);
    result = (Arg4) >> (8);
    Arg2 = (Arg2) + ((uint8_t)(result));
    Arg1 = (Arg1) * (Arg2);
    result = (Arg4) >> (16);
    Arg1 = (Arg1) + ((uint8_t)(result));
    Arg2 = (Arg2) * (Arg1);
    result = (Arg4) >> (24);
    Arg2 = (Arg2) + ((uint8_t)(result));
    Arg1 = (Arg1) * (Arg2);
    result = (Arg4) >> (32);
    Arg1 = (Arg1) + ((uint8_t)(result));
    Arg2 = (Arg2) * (Arg1);
    result = (Arg4) >> (40);
    Arg2 = (Arg2) + ((uint8_t)(result));
    Arg1 = (Arg1) * (Arg2);
    result = (Arg4) >> (48);
    Arg1 = (Arg1) + ((uint8_t)(result));
    Arg2 = (Arg2) * (Arg1);
    result = (local_r11) >> (32);
    Arg1 = ((uint8_t)(result)) * (result);
    Arg2 = (Arg2) + (Arg1);
    result = (Arg3) >> (16);
    Arg1 = ((uint8_t)(result)) * (result);
    Arg2 = (Arg2) + (Arg1);
    result = (local_r10) >> (24);
    Arg1 = ((uint8_t)(result)) * (result);
    Arg2 = (Arg2) + (Arg1);
    result = (local_r11) >> (16);
    Arg1 = ((uint8_t)(result)) * (result);
    Arg2 = (Arg2) + (Arg1);
    result = (local_r10) >> (16);
    Arg1 = ((uint8_t)(result)) * (result);
    Arg2 = (Arg2) + (Arg1);
    result = (Arg3) >> (8);
    Arg1 = ((uint8_t)(result)) * (result);
    Arg2 = (Arg2) + (Arg1);
    result = (local_r11) >> (24);
    Arg1 = ((uint8_t)(result)) * (result);
    Arg2 = (Arg2) + (Arg1);
    result = (local_r11) >> (8);
    Arg1 = ((uint8_t)(result)) * (result);
    Arg2 = (Arg2) + (Arg1);
    result = (local_r10) >> (8);
    Arg1 = ((uint8_t)(result)) * (result);
    Arg2 = (Arg2) + (Arg1);
    result = (local_r10) >> (32);
    Arg1 = ((uint8_t)(result)) * (result);
    Arg2 = (Arg2) + (Arg1);
    result = (local_r11) >> (40);
    Arg1 = ((uint8_t)(result)) * (result);
    Arg2 = (Arg2) + (Arg1);
    result = (local_r10) >> (48);
    Arg1 = ((uint8_t)(result)) * (result);
    Arg2 = (Arg2) + (Arg1);
    result = (local_r11) >> (48);
    Arg1 = ((uint8_t)(result)) * (result);
    Arg2 = (Arg2) + (Arg1);
    result = (local_r10) >> (40);
    Arg1 = ((uint8_t)(result)) * (result);
    Arg2 = (Arg2) + (Arg1);
    result = ((uint8_t)(Arg3)) * (Arg1);
    Arg2 = (Arg2) + (result);
    result = ((uint8_t)(local_r10)) * (Arg1);
    Arg2 = (Arg2) + (result);
    result = ((uint8_t)(local_r11)) * (Arg1);
    Arg2 = (Arg2) + (result);
    local_r10 = (local_r10) >> (56);
    local_r10 = (local_r10) * (result);
    Arg2 = (Arg2) + (local_r10);
    local_r11 = (local_r11) >> (56);
    local_r11 = (local_r11) * (result);
    Arg2 = (Arg2) + (local_r11);
    Arg4 = (Arg4) >> (56);
    Arg2 = (Arg2) + (result);
    Arg2 = (Arg2) + (Arg4);
    if ((*(uint32_t *)(v_rip + 0x51BFEA)) <= 5) goto loc_008E9F9B;
    if (((*(uint64_t *)(v_rip + 0x51BFE3)) & (Arg3)) != 0) goto loc_008EB2F3;
loc_008EAF43:
    result = 0;
loc_008EAF45:
    if (0 == 0) goto loc_008E9F9B;
    v_stack_p120 = (uint32_t)(0x80000000ULL);
    v_stack_p1D0 = v_stack_p120;
    v_stack_p1D8 = 8;
    v_stack_p128 = v_stack_p80;
    v_stack_p1E0 = v_stack_p128;
    v_stack_p1E8 = 8;
    v_stack_pF8 = (uint32_t)((uint32_t)(0x80000000ULL));
    v_stack_p1F0 = v_stack_pF8;
    v_stack_p1F8 = 4;
    v_stack_p130 = Arg2;
    v_stack_p200 = v_stack_p130;
    v_stack_p208 = 8;
    v_stack_pFC = (uint32_t)(*(uint16_t *)((uint32_t)(v_stack_p54) + 0x8));
    v_stack_p210 = v_stack_pFC;
    v_stack_p218 = 4;
    v_stack_p28 = v_stack_p1B0;
    v_stack_p20 = 7;
    Arg4 = 0;
    Arg3 = 0;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 5357269, v_rip - 9061422, Arg3, Arg4);
    goto loc_008E9F9B;
loc_008EB045:
    v_stack_p20 = v_stack_p70;
    result = IopWaitAndAcquireFileObjectLock(v_stack_p88, (uint8_t)(v_stack_p100), (uint8_t)((uint32_t)(v_stack_p54)), result);
    goto loc_008EA759;
loc_008EB071:
    if (v_stack_p100 != 0) goto loc_008EB0D6;
loc_008EB076:
    goto loc_008EA680;
loc_008EB083:
    if (v_stack_p51 == 0) { local_r12 = 3; }
    goto loc_008EA2F7;
loc_008EB096:
    v_stack_p78 = *(uint64_t *)(v_stack_p88 + 0x8);
    result = MmIsDriverVerifying(*(uint64_t *)(v_stack_p88 + 0x8), (uint8_t)(v_stack_p100), (uint8_t)((uint32_t)(v_stack_p54)), result);
    if ((uint32_t)(result) == 0) goto loc_008EB2E6;
    result = VfFastIoSnapState(v_stack_p78, (uint8_t)(v_stack_p100), (uint8_t)((uint32_t)(v_stack_p54)), result);
    v_stack_p78 = result;
    goto loc_008EA12A;
loc_008EB0CB:
    goto loc_008EABE2;
loc_008EB0D6:
    Arg4 = (uint32_t)((64) & (0xC0000000ULL));
    if (((uint32_t)(Arg4)) == ((uint32_t)((uint32_t)(0x80000000ULL)))) goto loc_008EA66B;
    goto loc_008EB076;
loc_008EB0E8:
    if (v_stack_p58 != 0) goto loc_008EA441;
    result = *(uint64_t *)((uint32_t)(v_stack_p54) + 0x18);
    if (((uint32_t)((uint32_t)(0x80000000ULL))) == 0x9040CULL) {
        result = (*(uint64_t *)((uint32_t)(v_stack_p54) + 0x18)) + (32);
    }
    if ((*(uint32_t *)(result)) != 0xA0000003ULL) goto loc_008EA441;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_pF0))) >> (1));
    result = (uint8_t)((result) & (1));
    v_stack_p20 = (uint8_t)(result);
    Arg4 = 0;
    result = IopExceptionCleanupEx(v_stack_p88, (uint32_t)(v_stack_p54), v_stack_p98, Arg4);
    goto loc_008EA473;
loc_008EB142:
    if (((uint32_t)((uint32_t)(v_stack_p54))) < 36) goto loc_008E9DED;
loc_008EB14C:
    v_stack_p138 = v_xmm0;
    v_stack_p148 = v_xmm0;
    result = IoThreadToProcess(v_stack_pE8, (uint32_t)(v_stack_p54), v_stack_p98, Arg4);
    result = SeCaptureSubjectContextEx(v_stack_pE8, result, v_stack_p138, Arg4);
    result = RtlIsSandboxedToken(v_stack_p138, (uint8_t)(v_stack_p100), v_stack_p138, Arg4);
    v_stack_p51 = (uint8_t)(result);
    v_stack_p50 = (uint8_t)(result);
    result = SeReleaseSubjectContext(v_stack_p138, (uint8_t)(v_stack_p100), v_stack_p138, Arg4);
    if (v_stack_p51 == 0) goto loc_008E9DED;
    v_stack_pCC = (uint32_t)(local_r14);
    if (((uint32_t)((uint32_t)(0x80000000ULL))) != 0x9040CULL) goto loc_008EB245;
    goto loc_008EB248;
loc_008EB1D4:
    result = v_stack_p98;
    if (v_stack_p98 != 0) {
        Arg1 = v_stack_p98;
        result = ObfDereferenceObject(Arg1, (uint8_t)(v_stack_p100), (uint32_t)(*(uint32_t *)(v_stack_pA8 + 0x20)), Arg4);
    }
    if (v_stack_pE0 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_pE0, Arg2, (uint32_t)(*(uint32_t *)(v_stack_pA8 + 0x20)), Arg4);
    }
    result = ObfDereferenceObject(v_stack_p88, Arg2, (uint32_t)(*(uint32_t *)(v_stack_pA8 + 0x20)), Arg4);
    goto loc_008EA473;
loc_008EB20C:
    result = IopSetFileObjectExtensionFlag(v_stack_p88, 16, (uint32_t)(*(uint32_t *)(v_stack_pA8 + 0x20)), Arg4);
    v_stack_p78 = (uint32_t)(result);
    if (!sign_flag) goto loc_008E9D55;
    result = ObfDereferenceObject(v_stack_p88, 16, (uint32_t)(*(uint32_t *)(v_stack_pA8 + 0x20)), Arg4);
    goto loc_008EA473;
loc_008EB236:
    if (((uint32_t)((uint32_t)(v_stack_p54))) < 4) goto loc_008E9DE0;
    goto loc_008EB14C;
loc_008EB245:
loc_008EB248:
    v_stack_pCC = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p88)));
    goto loc_008EB2C3;
loc_008EB2C3:
    if (!sign_flag) goto loc_008EB31B;
loc_008EB2C7:
    result = ObfDereferenceObject(v_stack_p98, (uint32_t)(v_stack_p78), (uint32_t)(*(uint32_t *)(v_stack_p88)), Arg4);
loc_008EB2E6:
    goto loc_008EA125;
loc_008EB2F3:
    result = (*(uint64_t *)(v_rip + 0x51BC2E)) & ((uint32_t)(*(uint32_t *)(v_stack_p88)));
    if (result != (*(uint64_t *)(v_rip + 0x51BC24))) goto loc_008EAF43;
    goto loc_008EAF45;
loc_008EB311:
    if (!sign_flag) goto loc_008E9DED;
    goto loc_008EB2C7;
loc_008EB31B:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p88)))) != 0xA0000003ULL) goto loc_008EB311;
    v_stack_p58 = 1;
    v_stack_p28 = v_stack_p60;
    v_stack_p20 = v_stack_pE0;
    result = IopValidateJunctionTarget((uint32_t)((uint32_t)((uint32_t)(0x80000000ULL))), v_stack_p98, (uint32_t)((uint32_t)((uint32_t)(v_stack_p54))), 1);
    v_stack_p78 = (uint32_t)(result);
    goto loc_008EB311;
loc_008EB359:
loc_008EB361:
    v_stack_p40 = v_stack_p80;
    v_stack_p38 = v_stack_pB8;
    v_stack_p30 = (uint32_t)((uint32_t)(0x80000000ULL));
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_p54));
    v_stack_p20 = v_stack_pB0;
loc_008EB3AC:
    result = ObfDereferenceObject(v_stack_pA0, 1, v_stack_pA8, (uint32_t)(v_stack_p60));
    goto loc_008EA79D;
loc_008EB3B9:
    result = IopReleaseFileObjectLock(v_stack_p88, 1, v_stack_pA8, (uint32_t)(v_stack_p60));
    goto loc_008EA7AF;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008E9AD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
