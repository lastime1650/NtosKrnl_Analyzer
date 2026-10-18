# IopInitializeBootDrivers

- RVA: `0x00C2E6F4`–`0x00C2F291` (길이 `2,973` bytes)
- VA: `0x0000000140C2E6F4`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C81B4`
- 디코드: `716`개 명령, `2,973/2,973` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **89**; 고유 호출 대상: **54**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **34**

### Outgoing calls
- `0x00C2E787` → [PnpDiagnosticTrace](../../text/26/PnpDiagnosticTrace_function_0026E384.md) (function, `0x0026E384`)
- `0x00C2E7BB` → [IopOpenRegistryKeyEx](../../page/A5/IopOpenRegistryKeyEx_function_00A51B44.md) (function, `0x00A51B44`)
- `0x00C2E7E4` → [IopOpenRegistryKeyEx](../../page/A5/IopOpenRegistryKeyEx_function_00A51B44.md) (function, `0x00A51B44`)
- `0x00C2E801` → [IopGetRegistryValue](../../page/99/IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x00C2E80D` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00C2E83C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C2E869` → [PipInitializeCoreDriversAndElam](../C7/PipInitializeCoreDriversAndElam_function_00C73F84.md) (function, `0x00C73F84`)
- `0x00C2E8C4` → [PnpInitializeBootStartDriver](../C7/PnpInitializeBootStartDriver_function_00C760F0.md) (function, `0x00C760F0`)
- `0x00C2E8E5` → [PpInitGetGroupOrderIndex](../C7/PpInitGetGroupOrderIndex_function_00C77534.md) (function, `0x00C77534`)
- `0x00C2E908` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (function, `0x004B7DEC`)
- `0x00C2E933` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C2E94A` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (function, `0x004B7DEC`)
- `0x00C2E998` → [PipInitializeDriverDependentDLLs](../C7/PipInitializeDriverDependentDLLs_function_00C74398.md) (function, `0x00C74398`)
- `0x00C2E9A8` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C2E9B8` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C2E9EB` → [RtlCompareUnicodeString](../../page/93/RtlCompareUnicodeString_function_00937F90.md) (function, `0x00937F90`)
- `0x00C2EA05` → [RtlCompareUnicodeString](../../page/93/RtlCompareUnicodeString_function_00937F90.md) (function, `0x00937F90`)
- `0x00C2EA5B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C2EA88` → [IopOpenRegistryKeyEx](../../page/A5/IopOpenRegistryKeyEx_function_00A51B44.md) (function, `0x00A51B44`)
- `0x00C2EA96` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C2EAAB` → [PpInitGetGroupOrderIndex](../C7/PpInitGetGroupOrderIndex_function_00C77534.md) (function, `0x00C77534`)
- `0x00C2EAB8` → [PipGetDriverTagPriority](../C3/PipGetDriverTagPriority_function_00C30A10.md) (function, `0x00C30A10`)
- `0x00C2EB12` → [PnpNotifyEarlyLaunchStatusUpdate](../BE/PnpNotifyEarlyLaunchStatusUpdate_function_00BEF120.md) (function, `0x00BEF120`)
- `0x00C2EB7A` → [IopGetDriverNameFromKeyNode](../../page/99/IopGetDriverNameFromKeyNode_function_00998808.md) (function, `0x00998808`)
- `0x00C2EBA6` → [IopGetRegistryValue](../../page/99/IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x00C2EBDB` → [PipLookupGroupName](../C3/PipLookupGroupName_function_00C31578.md) (function, `0x00C31578`)
- `0x00C2EBE8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C2EBFA` → [PipCheckDependencies](../C7/PipCheckDependencies_function_00C77AE0.md) (function, `0x00C77AE0`)
- `0x00C2EC42` → [PnpInitializeBootStartDriver](../C7/PnpInitializeBootStartDriver_function_00C760F0.md) (function, `0x00C760F0`)
- `0x00C2EC5C` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00C2EC8D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C2EC9A` → [PnpLockDeviceActionQueue](../../text/4A/PnpLockDeviceActionQueue_function_004A4388.md) (function, `0x004A4388`)
- `0x00C2ECAC` → [PipApplyFunctionToServiceInstances](../../page/72/PipApplyFunctionToServiceInstances_function_0072BF40.md) (function, `0x0072BF40`)
- `0x00C2ECB1` → [PnpUnlockDeviceActionQueue](../../text/4A/PnpUnlockDeviceActionQueue_function_004A42F4.md) (function, `0x004A42F4`)
- `0x00C2ECB6` → [PnpWaitForEmptyDeviceActionQueue](../../page/73/PnpWaitForEmptyDeviceActionQueue_function_007375AC.md) (function, `0x007375AC`)
- `0x00C2ECD6` → [PnpRequestDeviceAction](../../text/47/PnpRequestDeviceAction_function_00477FF8.md) (function, `0x00477FF8`)
- `0x00C2ECDB` → [PnpWaitForEmptyDeviceEventQueue](../../page/70/PnpWaitForEmptyDeviceEventQueue_function_00704350.md) (function, `0x00704350`)
- `0x00C2ECF8` → [IopAllocateLegacyBootResources](../C3/IopAllocateLegacyBootResources_function_00C34138.md) (function, `0x00C34138`)
- `0x00C2ED20` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (function, `0x004B7DEC`)
- `0x00C2ED3E` → [PnpNotifyEarlyLaunchStatusUpdate](../BE/PnpNotifyEarlyLaunchStatusUpdate_function_00BEF120.md) (function, `0x00BEF120`)
- `0x00C2ED46` → [PipUnloadEarlyLaunchDrivers](../C3/PipUnloadEarlyLaunchDrivers_function_00C326D8.md) (function, `0x00C326D8`)
- `0x00C2ED6E` → [PnpRequestDeviceAction](../../text/47/PnpRequestDeviceAction_function_00477FF8.md) (function, `0x00477FF8`)
- `0x00C2ED73` → [PnpWaitForDevicesToStart](../C3/PnpWaitForDevicesToStart_function_00C32930.md) (function, `0x00C32930`)
- `0x00C2ED81` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (function, `0x004B7DEC`)
- `0x00C2ED92` → [IopCallBootDriverReinitializationRoutines](IopCallBootDriverReinitializationRoutines_function_00C2D9F0.md) (function, `0x00C2D9F0`)
- `0x00C2ED9B` → [PnpWaitForDevicesToStart](../C3/PnpWaitForDevicesToStart_function_00C32930.md) (function, `0x00C32930`)
- `0x00C2EDA9` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (function, `0x004B7DEC`)
- `0x00C2EDC6` → [RamdiskInitialize](../C6/RamdiskInitialize_function_00C6EF08.md) (function, `0x00C6EF08`)
- `0x00C2EDCF` → [PnpWaitForDevicesToStart](../C3/PnpWaitForDevicesToStart_function_00C32930.md) (function, `0x00C32930`)
- `0x00C2EDDD` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (function, `0x004B7DEC`)
- `0x00C2EDFB` → [RamdiskInitialize](../C6/RamdiskInitialize_function_00C6EF08.md) (function, `0x00C6EF08`)
- `0x00C2EE16` → [VhdInitialize](../C6/VhdInitialize_function_00C6DBB4.md) (function, `0x00C6DBB4`)
- `0x00C2EE1F` → [PnpWaitForDevicesToStart](../C3/PnpWaitForDevicesToStart_function_00C32930.md) (function, `0x00C32930`)
- `0x00C2EE2D` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (function, `0x004B7DEC`)
- `0x00C2EE47` → [CimfsInitialize](../C6/CimfsInitialize_function_00C6E64C.md) (function, `0x00C6E64C`)
- `0x00C2EE50` → [PnpWaitForDevicesToStart](../C3/PnpWaitForDevicesToStart_function_00C32930.md) (function, `0x00C32930`)
- `0x00C2EE5E` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (function, `0x004B7DEC`)
- `0x00C2EE8C` → [CompositefsBootIsEnabled](../C6/CompositefsBootIsEnabled_function_00C6F254.md) (function, `0x00C6F254`)
- `0x00C2EE9F` → `ext-ms-win-ntos-globmerger-l1-1-0.dll!CompositefsSetBootInformation` (import, 간접 대상; import `ext-ms-win-ntos-globmerger-l1-1-0.dll!CompositefsSetBootInformation`)
- `0x00C2EEC1` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C2EEC7` → [PnpWaitForDevicesToStart](../C3/PnpWaitForDevicesToStart_function_00C32930.md) (function, `0x00C32930`)
- `0x00C2EED5` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (function, `0x004B7DEC`)
- `0x00C2EEEC` → [IopCreateArcNames](IopCreateArcNames_function_00C2BF1C.md) (function, `0x00C2BF1C`)
- `0x00C2EF14` → [PnpBootDeviceWait](../../text/5A/PnpBootDeviceWait_function_005A4D68.md) (function, `0x005A4D68`)
- `0x00C2EF33` → [SbpStartLanman](../C6/SbpStartLanman_function_00C6F500.md) (function, `0x00C6F500`)
- `0x00C2EF3C` → [SbpWaitForVmbus](../C6/SbpWaitForVmbus_function_00C6F8D8.md) (function, `0x00C6F8D8`)
- `0x00C2EF45` → [SbpAddTransportToInstance](../C6/SbpAddTransportToInstance_function_00C6F314.md) (function, `0x00C6F314`)
- `0x00C2EF62` → [CimfsInitialize](../C6/CimfsInitialize_function_00C6E64C.md) (function, `0x00C6E64C`)
- `0x00C2EF7A` → [VhdAutoAttachVirtualDisks](../C6/VhdAutoAttachVirtualDisks_function_00C6D934.md) (function, `0x00C6D934`)
- `0x00C2EF82` → [PipWaitCriticalDevices](../C3/PipWaitCriticalDevices_function_00C3277C.md) (function, `0x00C3277C`)
- `0x00C2EF9A` → [PiCreateDriverDataDirectoryRoot](../C3/PiCreateDriverDataDirectoryRoot_function_00C329A8.md) (function, `0x00C329A8`)
- `0x00C2EFBC` → [PipHardwareConfigGetIndex](../../page/72/PipHardwareConfigGetIndex_function_007235B8.md) (function, `0x007235B8`)
- `0x00C2EFF2` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (function, `0x0042B390`)
- `0x00C2F036` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C2F04E` → [PnpDiagnosticTrace](../../text/26/PnpDiagnosticTrace_function_0026E384.md) (function, `0x0026E384`)
- `0x00C2F05F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00C2F0F3` → [IopGetRegistryValue](../../page/99/IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x00C2F144` → [PiCreateDriverRedirectedStateKey](../../page/99/PiCreateDriverRedirectedStateKey_function_0099957C.md) (function, `0x0099957C`)
- `0x00C2F18D` → [PnpCtxRegCreateKey](../../page/A6/PnpCtxRegCreateKey_function_00A692E4.md) (function, `0x00A692E4`)
- `0x00C2F1B8` → [PnpCtxRegSetValue](../../page/99/PnpCtxRegSetValue_function_00991B8C.md) (function, `0x00991B8C`)
- `0x00C2F1C2` → [PnpCtxRegCloseKey](../../page/A2/PnpCtxRegCloseKey_function_00A22E0C.md) (function, `0x00A22E0C`)
- `0x00C2F1E9` → [PnpUnicodeStringToWstr](../../page/9D/PnpUnicodeStringToWstr_function_009D90C0.md) (function, `0x009D90C0`)
- `0x00C2F212` → [McTemplateK0dzd_EtwWriteTransfer](../../text/5A/McTemplateK0dzd_EtwWriteTransfer_function_005A4538.md) (function, `0x005A4538`)
- `0x00C2F222` → [PnpUnicodeStringToWstrFree](../../page/8F/PnpUnicodeStringToWstrFree_function_008F59F0.md) (function, `0x008F59F0`)
- `0x00C2F233` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00C2F242` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C2F25A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00C2F276` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00C2F280` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [IoInitSystemPreDrivers](IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2BB77`

### Static image references
- `0x00C2E71A` → RVA `0x00E0A740` (`.data`; read)
- `0x00C2E747` → RVA `0x00027390` (`.rdata`; read)
- `0x00C2E78C` → RVA `0x00C7A050` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2E793` → RVA `0x01008684` (`INITDATA`; write)
- `0x00C2E7C4` → RVA `0x00C7A0D0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2E7FA` → RVA `0x00C7A150` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2E841` → RVA `0x01008684` (`INITDATA`; read)
- `0x00C2E86E` → RVA `0x00C7A1F0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2E880` → RVA `0x00C47090` (`RawInitialize`; read)
- `0x00C2E887` → RVA `0x00C7A210` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2E8D8` → RVA `0x00F8D8D0` (`.data`; write)
- `0x00C2E8F3` → RVA `0x00F8CFA0` (`.data`; write)
- `0x00C2E938` → RVA `0x00F8CFA8` (`.data`; write)
- `0x00C2E95F` → RVA `0x00F8CFA0` (`.data`; read)
- `0x00C2E99D` → RVA `0x00C7A220` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2E9AD` → RVA `0x00C7A240` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2E9BD` → RVA `0x00E66250` (`.data`; read)
- `0x00C2E9D2` → RVA `0x00E66248` (`.data`; read)
- `0x00C2EAC7` → RVA `0x00F8CFA8` (`.data`; read)
- `0x00C2EB9F` → RVA `0x00C7A180` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2ECFD` → RVA `0x0072E680` (`IopAllocateBootResources`; read)
- `0x00C2ED04` → RVA `0x00F8C5F8` (`.data`; write)
- `0x00C2ED0B` → RVA `0x00F8C138` (`.data`; write)
- `0x00C2ED4E` → RVA `0x00F8C5F9` (`.data`; write)
- `0x00C2EE9F` → RVA `0x001512A8` (`ext-ms-win-ntos-globmerger-l1-1-0.dll!CompositefsSetBootInformation (IAT)`; read)
- `0x00C2EF07` → RVA `0x00C2CFA0` (`IopMarkBootPartition`; read)
- `0x00C2EF20` → RVA `0x00F8C5FA` (`.data`; write)
- `0x00C2EFD7` → RVA `0x00C7A190` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2F03E` → RVA `0x00E66244` (`.data`; write)
- `0x00C2F047` → RVA `0x00026E00` (`.rdata`; read)
- `0x00C2F0EC` → RVA `0x00C79970` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2F15D` → RVA `0x00E66398` (`.data`; read)
- `0x00C2F16E` → RVA `0x00C7A1A0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C2F1C7` → RVA `0x00EF012B` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **55**
  - `0x00C2E787` → [PnpDiagnosticTrace](../../text/26/PnpDiagnosticTrace_function_0026E384.md) (`INIT` → `.text`)
  - `0x00C2E7BB` → [IopOpenRegistryKeyEx](../../page/A5/IopOpenRegistryKeyEx_function_00A51B44.md) (`INIT` → `PAGE`)
  - `0x00C2E7E4` → [IopOpenRegistryKeyEx](../../page/A5/IopOpenRegistryKeyEx_function_00A51B44.md) (`INIT` → `PAGE`)
  - `0x00C2E801` → [IopGetRegistryValue](../../page/99/IopGetRegistryValue_function_009990EC.md) (`INIT` → `PAGE`)
  - `0x00C2E80D` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`INIT` → `.text`)
  - `0x00C2E83C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C2E908` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (`INIT` → `.text`)
  - `0x00C2E933` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C2E94A` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (`INIT` → `.text`)
  - `0x00C2E9A8` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C2E9B8` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C2E9EB` → [RtlCompareUnicodeString](../../page/93/RtlCompareUnicodeString_function_00937F90.md) (`INIT` → `PAGE`)
  - `0x00C2EA05` → [RtlCompareUnicodeString](../../page/93/RtlCompareUnicodeString_function_00937F90.md) (`INIT` → `PAGE`)
  - `0x00C2EA5B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C2EA88` → [IopOpenRegistryKeyEx](../../page/A5/IopOpenRegistryKeyEx_function_00A51B44.md) (`INIT` → `PAGE`)
  - `0x00C2EA96` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C2EB7A` → [IopGetDriverNameFromKeyNode](../../page/99/IopGetDriverNameFromKeyNode_function_00998808.md) (`INIT` → `PAGE`)
  - `0x00C2EBA6` → [IopGetRegistryValue](../../page/99/IopGetRegistryValue_function_009990EC.md) (`INIT` → `PAGE`)
  - `0x00C2EBE8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C2EC5C` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`INIT` → `.text`)
  - `0x00C2EC8D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C2EC9A` → [PnpLockDeviceActionQueue](../../text/4A/PnpLockDeviceActionQueue_function_004A4388.md) (`INIT` → `.text`)
  - `0x00C2ECAC` → [PipApplyFunctionToServiceInstances](../../page/72/PipApplyFunctionToServiceInstances_function_0072BF40.md) (`INIT` → `PAGE`)
  - `0x00C2ECB1` → [PnpUnlockDeviceActionQueue](../../text/4A/PnpUnlockDeviceActionQueue_function_004A42F4.md) (`INIT` → `.text`)
  - `0x00C2ECB6` → [PnpWaitForEmptyDeviceActionQueue](../../page/73/PnpWaitForEmptyDeviceActionQueue_function_007375AC.md) (`INIT` → `PAGE`)
  - `0x00C2ECD6` → [PnpRequestDeviceAction](../../text/47/PnpRequestDeviceAction_function_00477FF8.md) (`INIT` → `.text`)
  - `0x00C2ECDB` → [PnpWaitForEmptyDeviceEventQueue](../../page/70/PnpWaitForEmptyDeviceEventQueue_function_00704350.md) (`INIT` → `PAGE`)
  - `0x00C2ED20` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (`INIT` → `.text`)
  - `0x00C2ED6E` → [PnpRequestDeviceAction](../../text/47/PnpRequestDeviceAction_function_00477FF8.md) (`INIT` → `.text`)
  - `0x00C2ED81` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (`INIT` → `.text`)
  - `0x00C2EDA9` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (`INIT` → `.text`)
  - `0x00C2EDDD` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (`INIT` → `.text`)
  - `0x00C2EE2D` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (`INIT` → `.text`)
  - `0x00C2EE5E` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (`INIT` → `.text`)
  - `0x00C2EEC1` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C2EED5` → [HeadlessKernelAddLogEntry](../../text/4B/HeadlessKernelAddLogEntry_function_004B7DEC.md) (`INIT` → `.text`)
  - `0x00C2EF14` → [PnpBootDeviceWait](../../text/5A/PnpBootDeviceWait_function_005A4D68.md) (`INIT` → `.text`)
  - `0x00C2EFBC` → [PipHardwareConfigGetIndex](../../page/72/PipHardwareConfigGetIndex_function_007235B8.md) (`INIT` → `PAGE`)
  - `0x00C2EFF2` → [RtlStringCchPrintfExW](../../text/42/RtlStringCchPrintfExW_function_0042B390.md) (`INIT` → `.text`)
  - `0x00C2F036` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C2F04E` → [PnpDiagnosticTrace](../../text/26/PnpDiagnosticTrace_function_0026E384.md) (`INIT` → `.text`)
  - `0x00C2F05F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
  - `0x00C2F0F3` → [IopGetRegistryValue](../../page/99/IopGetRegistryValue_function_009990EC.md) (`INIT` → `PAGE`)
  - `0x00C2F144` → [PiCreateDriverRedirectedStateKey](../../page/99/PiCreateDriverRedirectedStateKey_function_0099957C.md) (`INIT` → `PAGE`)
  - `0x00C2F18D` → [PnpCtxRegCreateKey](../../page/A6/PnpCtxRegCreateKey_function_00A692E4.md) (`INIT` → `PAGE`)
  - `0x00C2F1B8` → [PnpCtxRegSetValue](../../page/99/PnpCtxRegSetValue_function_00991B8C.md) (`INIT` → `PAGE`)
  - `0x00C2F1C2` → [PnpCtxRegCloseKey](../../page/A2/PnpCtxRegCloseKey_function_00A22E0C.md) (`INIT` → `PAGE`)
  - `0x00C2F1E9` → [PnpUnicodeStringToWstr](../../page/9D/PnpUnicodeStringToWstr_function_009D90C0.md) (`INIT` → `PAGE`)
  - `0x00C2F212` → [McTemplateK0dzd_EtwWriteTransfer](../../text/5A/McTemplateK0dzd_EtwWriteTransfer_function_005A4538.md) (`INIT` → `.text`)
  - `0x00C2F222` → [PnpUnicodeStringToWstrFree](../../page/8F/PnpUnicodeStringToWstrFree_function_008F59F0.md) (`INIT` → `PAGE`)
  - `0x00C2F233` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`INIT` → `.text`)
  - `0x00C2F242` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C2F25A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`INIT` → `.text`)
  - `0x00C2F276` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`INIT` → `.text`)
  - `0x00C2F280` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C2E6F4  48 8B C4                        mov rax, rsp
00C2E6F7  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00C2E6FB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00C2E6FF  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00C2E703  55                              push rbp
00C2E704  41 54                           push r12
00C2E706  41 55                           push r13
00C2E708  41 56                           push r14
00C2E70A  41 57                           push r15
00C2E70C  48 8D A8 48 FF FF FF            lea rbp, [rax - 0xb8]
00C2E713  48 81 EC 90 01 00 00            sub rsp, 0x190
00C2E71A  48 8B 05 1F C0 1D 00            mov rax, qword ptr [rip + 0x1dc01f]
00C2E721  48 33 C4                        xor rax, rsp
00C2E724  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
00C2E72B  45 33 E4                        xor r12d, r12d
00C2E72E  0F 57 C0                        xorps xmm0, xmm0
00C2E731  48 8B F1                        mov rsi, rcx
00C2E734  44 89 65 94                     mov dword ptr [rbp - 0x6c], r12d
00C2E738  0F 57 C9                        xorps xmm1, xmm1
00C2E73B  44 89 64 24 5C                  mov dword ptr [rsp + 0x5c], r12d
00C2E740  33 C0                           xor eax, eax
00C2E742  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
00C2E747  48 8D 0D 42 8C 3F FF            lea rcx, [rip - 0xc073be]
00C2E74E  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
00C2E753  45 33 C0                        xor r8d, r8d
00C2E756  44 89 65 84                     mov dword ptr [rbp - 0x7c], r12d
00C2E75A  33 D2                           xor edx, edx
00C2E75C  44 89 65 B4                     mov dword ptr [rbp - 0x4c], r12d
00C2E760  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00C2E764  4C 89 64 24 78                  mov qword ptr [rsp + 0x78], r12
00C2E769  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00C2E76D  4C 89 64 24 70                  mov qword ptr [rsp + 0x70], r12
00C2E772  44 89 64 24 58                  mov dword ptr [rsp + 0x58], r12d
00C2E777  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
00C2E77B  89 45 E0                        mov dword ptr [rbp - 0x20], eax
00C2E77E  0F 11 4D D0                     movups xmmword ptr [rbp - 0x30], xmm1
00C2E782  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
00C2E787  E8 F8 FB 63 FF                  call 0x14026e384
00C2E78C  48 8D 05 BD B8 04 00            lea rax, [rip + 0x4b8bd]
00C2E793  C7 05 E7 9E 3D 00 03 00 00 00   mov dword ptr [rip + 0x3d9ee7], 3
00C2E79D  BF 19 00 02 00                  mov edi, 0x20019
00C2E7A2  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00C2E7A6  44 8B CF                        mov r9d, edi
00C2E7A9  C7 45 80 7E 00 80 00            mov dword ptr [rbp - 0x80], 0x80007e
00C2E7B0  4C 8D 45 80                     lea r8, [rbp - 0x80]
00C2E7B4  33 D2                           xor edx, edx
00C2E7B6  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00C2E7BB  E8 84 33 E2 FF                  call 0x140a51b44
00C2E7C0  85 C0                           test eax, eax
00C2E7C2  79 29                           jns 0x140c2e7ed
00C2E7C4  48 8D 05 05 B9 04 00            lea rax, [rip + 0x4b905]
00C2E7CB  C7 45 80 7C 00 7E 00            mov dword ptr [rbp - 0x80], 0x7e007c
00C2E7D2  44 8B CF                        mov r9d, edi
00C2E7D5  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00C2E7D9  4C 8D 45 80                     lea r8, [rbp - 0x80]
00C2E7DD  33 D2                           xor edx, edx
00C2E7DF  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00C2E7E4  E8 5B 33 E2 FF                  call 0x140a51b44
00C2E7E9  85 C0                           test eax, eax
00C2E7EB  78 54                           js 0x140c2e841
00C2E7ED  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2E7F2  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
00C2E7F7  45 33 C0                        xor r8d, r8d
00C2E7FA  48 8D 15 4F B9 04 00            lea rdx, [rip + 0x4b94f]
00C2E801  E8 E6 A8 D6 FF                  call 0x1409990ec
00C2E806  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2E80B  8B D8                           mov ebx, eax
00C2E80D  E8 9E EA A7 FF                  call 0x1406ad2b0
00C2E812  85 DB                           test ebx, ebx
00C2E814  78 2B                           js 0x140c2e841
00C2E816  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
00C2E81B  41 83 78 04 04                  cmp dword ptr [r8 + 4], 4
00C2E820  75 15                           jne 0x140c2e837
00C2E822  41 83 78 0C 04                  cmp dword ptr [r8 + 0xc], 4
00C2E827  72 0E                           jb 0x140c2e837
00C2E829  41 8B 40 08                     mov eax, dword ptr [r8 + 8]
00C2E82D  42 8B 0C 00                     mov ecx, dword ptr [rax + r8]
00C2E831  89 0D 4D 9E 3D 00               mov dword ptr [rip + 0x3d9e4d], ecx
00C2E837  33 D2                           xor edx, edx
00C2E839  49 8B C8                        mov rcx, r8
00C2E83C  E8 2F 40 F5 FF                  call 0x140b82870
00C2E841  8B 05 3D 9E 3D 00               mov eax, dword ptr [rip + 0x3d9e3d]
00C2E847  83 F8 08                        cmp eax, 8
00C2E84A  75 09                           jne 0x140c2e855
00C2E84C  44 89 25 31 9E 3D 00            mov dword ptr [rip + 0x3d9e31], r12d
00C2E853  EB 11                           jmp 0x140c2e866
00C2E855  A9 F8 FF FF FF                  test eax, 0xfffffff8
00C2E85A  74 0A                           je 0x140c2e866
00C2E85C  C7 05 1E 9E 3D 00 03 00 00 00   mov dword ptr [rip + 0x3d9e1e], 3
00C2E866  48 8B CE                        mov rcx, rsi
00C2E869  E8 16 57 04 00                  call 0x140c73f84
00C2E86E  48 8D 05 7B B9 04 00            lea rax, [rip + 0x4b97b]
00C2E875  C7 45 B0 1E 00 20 00            mov dword ptr [rbp - 0x50], 0x20001e
00C2E87C  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00C2E880  4C 8D 05 09 88 01 00            lea r8, [rip + 0x18809]
00C2E887  48 8D 05 82 B9 04 00            lea rax, [rip + 0x4b982]
00C2E88E  C7 45 90 00 00 02 00            mov dword ptr [rbp - 0x70], 0x20000
00C2E895  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
00C2E899  48 8D 55 90                     lea rdx, [rbp - 0x70]
00C2E89D  BF 20 00 00 00                  mov edi, 0x20
00C2E8A2  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00C2E8A7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00C2E8AC  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00C2E8B0  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00C2E8B5  45 33 C9                        xor r9d, r9d
00C2E8B8  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00C2E8BD  8D 5F FE                        lea ebx, [rdi - 2]
00C2E8C0  44 8D 77 E2                     lea r14d, [rdi - 0x1e]
00C2E8C4  E8 27 78 04 00                  call 0x140c760f0
00C2E8C9  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
00C2E8CE  4C 89 6C 24 50                  mov qword ptr [rsp + 0x50], r13
00C2E8D3  4D 85 ED                        test r13, r13
00C2E8D6  75 0B                           jne 0x140c2e8e3
00C2E8D8  89 1D F2 EF 35 00               mov dword ptr [rip + 0x35eff2], ebx
00C2E8DE  E9 72 07 00 00                  jmp 0x140c2f055
00C2E8E3  33 C9                           xor ecx, ecx
00C2E8E5  E8 4A 8C 04 00                  call 0x140c77534
00C2E8EA  0F B7 C0                        movzx eax, ax
00C2E8ED  41 BF FF FF 00 00               mov r15d, 0xffff
00C2E8F3  89 05 A7 E6 35 00               mov dword ptr [rip + 0x35e6a7], eax
00C2E8F9  44 89 7C 24 68                  mov dword ptr [rsp + 0x68], r15d
00C2E8FE  41 3B C7                        cmp eax, r15d
00C2E901  75 1E                           jne 0x140c2e921
00C2E903  33 D2                           xor edx, edx
00C2E905  8D 4A 10                        lea ecx, [rdx + 0x10]
00C2E908  E8 DF 94 88 FF                  call 0x1404b7dec
00C2E90D  B8 25 02 00 C0                  mov eax, 0xc0000225
00C2E912  C7 05 B4 EF 35 00 1F 00 00 00   mov dword ptr [rip + 0x35efb4], 0x1f
00C2E91C  E9 34 07 00 00                  jmp 0x140c2f055
00C2E921  48 8B D0                        mov rdx, rax
00C2E924  B9 00 01 00 00                  mov ecx, 0x100
00C2E929  48 C1 E2 04                     shl rdx, 4
00C2E92D  41 B8 50 70 69 6E               mov r8d, 0x6e697050
00C2E933  E8 B8 37 F5 FF                  call 0x140b820f0
00C2E938  48 89 05 69 E6 35 00            mov qword ptr [rip + 0x35e669], rax
00C2E93F  48 8B D0                        mov rdx, rax
00C2E942  48 85 C0                        test rax, rax
00C2E945  75 18                           jne 0x140c2e95f
00C2E947  8D 48 11                        lea ecx, [rax + 0x11]
00C2E94A  E8 9D 94 88 FF                  call 0x1404b7dec
00C2E94F  B8 9A 00 00 C0                  mov eax, 0xc000009a
00C2E954  89 3D 76 EF 35 00               mov dword ptr [rip + 0x35ef76], edi
00C2E95A  E9 F6 06 00 00                  jmp 0x140c2f055
00C2E95F  44 8B 05 3A E6 35 00            mov r8d, dword ptr [rip + 0x35e63a]
00C2E966  41 0F B7 CC                     movzx ecx, r12w
00C2E96A  41 BF 01 00 00 00               mov r15d, 1
00C2E970  45 85 C0                        test r8d, r8d
00C2E973  74 1D                           je 0x140c2e992
00C2E975  0F B7 C1                        movzx eax, cx
00C2E978  66 41 03 CF                     add cx, r15w
00C2E97C  48 C1 E0 04                     shl rax, 4
00C2E980  48 03 C2                        add rax, rdx
00C2E983  48 89 40 08                     mov qword ptr [rax + 8], rax
00C2E987  48 89 00                        mov qword ptr [rax], rax
00C2E98A  0F B7 C1                        movzx eax, cx
00C2E98D  41 3B C0                        cmp eax, r8d
00C2E990  72 E3                           jb 0x140c2e975
00C2E992  48 8B D6                        mov rdx, rsi
00C2E995  41 8B CE                        mov ecx, r14d
00C2E998  E8 FB 59 04 00                  call 0x140c74398
00C2E99D  48 8D 15 7C B8 04 00            lea rdx, [rip + 0x4b87c]
00C2E9A4  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00C2E9A8  E8 D3 BD 7F FF                  call 0x14042a780
00C2E9AD  48 8D 15 8C B8 04 00            lea rdx, [rip + 0x4b88c]
00C2E9B4  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00C2E9B8  E8 C3 BD 7F FF                  call 0x14042a780
00C2E9BD  66 44 3B 25 8B 78 23 00         cmp r12w, word ptr [rip + 0x23788b]
00C2E9C5  41 0F B7 DC                     movzx ebx, r12w
00C2E9C9  41 0F B7 FC                     movzx edi, r12w
00C2E9CD  73 60                           jae 0x140c2ea2f
00C2E9CF  45 8B EE                        mov r13d, r14d
00C2E9D2  48 8B 0D 6F 78 23 00            mov rcx, qword ptr [rip + 0x23786f]
00C2E9D9  48 8D 55 A0                     lea rdx, [rbp - 0x60]
00C2E9DD  44 0F B7 F7                     movzx r14d, di
00C2E9E1  45 8A C7                        mov r8b, r15b
00C2E9E4  49 C1 E6 04                     shl r14, 4
00C2E9E8  49 03 CE                        add rcx, r14
00C2E9EB  E8 A0 95 D0 FF                  call 0x140937f90
00C2E9F0  85 C0                           test eax, eax
00C2E9F2  74 1F                           je 0x140c2ea13
00C2E9F4  48 8B 0D 4D 78 23 00            mov rcx, qword ptr [rip + 0x23784d]
00C2E9FB  48 8D 55 E8                     lea rdx, [rbp - 0x18]
00C2E9FF  49 03 CE                        add rcx, r14
00C2EA02  45 8A C7                        mov r8b, r15b
00C2EA05  E8 86 95 D0 FF                  call 0x140937f90
00C2EA0A  85 C0                           test eax, eax
00C2EA0C  75 09                           jne 0x140c2ea17
00C2EA0E  66 89 7C 24 68                  mov word ptr [rsp + 0x68], di
00C2EA13  66 41 03 DF                     add bx, r15w
00C2EA17  66 41 3B DD                     cmp bx, r13w
00C2EA1B  73 0D                           jae 0x140c2ea2a
00C2EA1D  66 41 03 FF                     add di, r15w
00C2EA21  66 3B 3D 28 78 23 00            cmp di, word ptr [rip + 0x237828]
00C2EA28  72 A8                           jb 0x140c2e9d2
00C2EA2A  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
00C2EA2F  4C 8D 7E 30                     lea r15, [rsi + 0x30]
00C2EA33  4D 8B 37                        mov r14, qword ptr [r15]
00C2EA36  E9 C5 00 00 00                  jmp 0x140c2eb00
00C2EA3B  49 8B DE                        mov rbx, r14
00C2EA3E  4D 8B 36                        mov r14, qword ptr [r14]
00C2EA41  44 39 63 38                     cmp dword ptr [rbx + 0x38], r12d
00C2EA45  0F 8C B5 00 00 00               jl 0x140c2eb00
00C2EA4B  BA 30 00 00 00                  mov edx, 0x30
00C2EA50  B9 00 01 00 00                  mov ecx, 0x100
00C2EA55  41 B8 50 70 69 6E               mov r8d, 0x6e697050
00C2EA5B  E8 90 36 F5 FF                  call 0x140b820f0
00C2EA60  48 8B F8                        mov rdi, rax
00C2EA63  48 85 C0                        test rax, rax
00C2EA66  0F 84 94 00 00 00               je 0x140c2eb00
00C2EA6C  48 89 40 08                     mov qword ptr [rax + 8], rax
00C2EA70  4C 8D 43 20                     lea r8, [rbx + 0x20]
00C2EA74  48 89 00                        mov qword ptr [rax], rax
00C2EA77  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00C2EA7C  33 D2                           xor edx, edx
00C2EA7E  48 89 58 18                     mov qword ptr [rax + 0x18], rbx
00C2EA82  41 B9 19 00 02 00               mov r9d, 0x20019
00C2EA88  E8 B7 30 E2 FF                  call 0x140a51b44
00C2EA8D  85 C0                           test eax, eax
00C2EA8F  79 0C                           jns 0x140c2ea9d
00C2EA91  33 D2                           xor edx, edx
00C2EA93  48 8B CF                        mov rcx, rdi
00C2EA96  E8 D5 3D F5 FF                  call 0x140b82870
00C2EA9B  EB 63                           jmp 0x140c2eb00
00C2EA9D  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00C2EAA2  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
00C2EAA6  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2EAAB  E8 84 8A 04 00                  call 0x140c77534
00C2EAB0  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2EAB5  0F B7 D8                        movzx ebx, ax
00C2EAB8  E8 53 1F 00 00                  call 0x140c30a10
00C2EABD  8B D3                           mov edx, ebx
00C2EABF  66 89 47 2C                     mov word ptr [rdi + 0x2c], ax
00C2EAC3  48 C1 E2 04                     shl rdx, 4
00C2EAC7  48 03 15 DA E4 35 00            add rdx, qword ptr [rip + 0x35e4da]
00C2EACE  48 8B 0A                        mov rcx, qword ptr [rdx]
00C2EAD1  EB 09                           jmp 0x140c2eadc
00C2EAD3  66 39 41 2C                     cmp word ptr [rcx + 0x2c], ax
00C2EAD7  77 08                           ja 0x140c2eae1
00C2EAD9  48 8B 09                        mov rcx, qword ptr [rcx]
00C2EADC  48 3B CA                        cmp rcx, rdx
00C2EADF  75 F2                           jne 0x140c2ead3
00C2EAE1  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00C2EAE5  48 8B 08                        mov rcx, qword ptr [rax]
00C2EAE8  48 39 41 08                     cmp qword ptr [rcx + 8], rax
00C2EAEC  0F 85 98 07 00 00               jne 0x140c2f28a
00C2EAF2  48 89 0F                        mov qword ptr [rdi], rcx
00C2EAF5  48 89 47 08                     mov qword ptr [rdi + 8], rax
00C2EAF9  48 89 79 08                     mov qword ptr [rcx + 8], rdi
00C2EAFD  48 89 38                        mov qword ptr [rax], rdi
00C2EB00  4D 3B F7                        cmp r14, r15
00C2EB03  0F 85 32 FF FF FF               jne 0x140c2ea3b
00C2EB09  41 BE 01 00 00 00               mov r14d, 1
00C2EB0F  41 8B CE                        mov ecx, r14d
00C2EB12  E8 09 06 FC FF                  call 0x140bef120
00C2EB17  45 0F B7 FC                     movzx r15d, r12w
00C2EB1B  41 0F B7 C7                     movzx eax, r15w
00C2EB1F  3B 05 7B E4 35 00               cmp eax, dword ptr [rip + 0x35e47b]
00C2EB25  0F 83 0E 02 00 00               jae 0x140c2ed39
00C2EB2B  48 8B 05 76 E4 35 00            mov rax, qword ptr [rip + 0x35e476]
00C2EB32  45 0F B7 E7                     movzx r12d, r15w
00C2EB36  49 C1 E4 04                     shl r12, 4
00C2EB3A  33 FF                           xor edi, edi
00C2EB3C  49 8B 1C 04                     mov rbx, qword ptr [r12 + rax]
00C2EB40  48 8B 0D 61 E4 35 00            mov rcx, qword ptr [rip + 0x35e461]
00C2EB47  49 03 CC                        add rcx, r12
00C2EB4A  48 3B D9                        cmp rbx, rcx
00C2EB4D  0F 84 99 01 00 00               je 0x140c2ecec
00C2EB53  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
00C2EB57  48 8D 55 90                     lea rdx, [rbp - 0x70]
00C2EB5B  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00C2EB60  4C 8B 73 18                     mov r14, qword ptr [rbx + 0x18]
00C2EB64  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
00C2EB69  49 8B 46 30                     mov rax, qword ptr [r14 + 0x30]
00C2EB6D  C6 43 2F 01                     mov byte ptr [rbx + 0x2f], 1
00C2EB71  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2EB76  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00C2EB7A  E8 89 9C D6 FF                  call 0x140998808
00C2EB7F  85 C0                           test eax, eax
00C2EB81  79 0F                           jns 0x140c2eb92
00C2EB83  41 BE 01 00 00 00               mov r14d, 1
00C2EB89  44 88 73 2E                     mov byte ptr [rbx + 0x2e], r14b
00C2EB8D  E9 02 01 00 00                  jmp 0x140c2ec94
00C2EB92  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2EB97  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
00C2EB9C  45 33 C0                        xor r8d, r8d
00C2EB9F  48 8D 15 DA B5 04 00            lea rdx, [rip + 0x4b5da]
00C2EBA6  E8 41 A5 D6 FF                  call 0x1409990ec
00C2EBAB  85 C0                           test eax, eax
00C2EBAD  78 43                           js 0x140c2ebf2
00C2EBAF  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
00C2EBB4  41 39 7E 0C                     cmp dword ptr [r14 + 0xc], edi
00C2EBB8  74 29                           je 0x140c2ebe3
00C2EBBA  41 0F B7 46 0C                  movzx eax, word ptr [r14 + 0xc]
00C2EBBF  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00C2EBC3  66 89 45 C0                     mov word ptr [rbp - 0x40], ax
00C2EBC7  BA 01 00 00 00                  mov edx, 1
00C2EBCC  66 89 45 C2                     mov word ptr [rbp - 0x3e], ax
00C2EBD0  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
00C2EBD4  49 03 C6                        add rax, r14
00C2EBD7  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00C2EBDB  E8 98 29 00 00                  call 0x140c31578
00C2EBE0  48 8B F8                        mov rdi, rax
00C2EBE3  33 D2                           xor edx, edx
00C2EBE5  49 8B CE                        mov rcx, r14
00C2EBE8  E8 83 3C F5 FF                  call 0x140b82870
00C2EBED  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
00C2EBF2  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C2EBF7  45 33 ED                        xor r13d, r13d
00C2EBFA  E8 E1 8E 04 00                  call 0x140c77ae0
00C2EBFF  85 C0                           test eax, eax
00C2EC01  74 7A                           je 0x140c2ec7d
00C2EC03  4C 8B 6B 10                     mov r13, qword ptr [rbx + 0x10]
00C2EC07  4C 89 6C 24 50                  mov qword ptr [rsp + 0x50], r13
00C2EC0C  4D 85 ED                        test r13, r13
00C2EC0F  75 52                           jne 0x140c2ec63
00C2EC11  44 38 6B 2E                     cmp byte ptr [rbx + 0x2e], r13b
00C2EC15  75 4C                           jne 0x140c2ec63
00C2EC17  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00C2EC1C  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00C2EC21  49 8D 56 20                     lea rdx, [r14 + 0x20]
00C2EC25  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
00C2EC29  45 8D 75 01                     lea r14d, [r13 + 1]
00C2EC2D  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00C2EC32  48 8D 4D 90                     lea rcx, [rbp - 0x70]
00C2EC36  44 21 6C 24 20                  and dword ptr [rsp + 0x20], r13d
00C2EC3B  4C 8B C8                        mov r9, rax
00C2EC3E  4C 8B 40 38                     mov r8, qword ptr [rax + 0x38]
00C2EC42  E8 A9 74 04 00                  call 0x140c760f0
00C2EC47  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
00C2EC4C  89 43 28                        mov dword ptr [rbx + 0x28], eax
00C2EC4F  4D 85 ED                        test r13, r13
00C2EC52  74 2F                           je 0x140c2ec83
00C2EC54  BA 44 66 6C 74                  mov edx, 0x746c6644
00C2EC59  49 8B CD                        mov rcx, r13
00C2EC5C  E8 AF 1A 5E FF                  call 0x140210710
00C2EC61  EB 06                           jmp 0x140c2ec69
00C2EC63  41 BE 01 00 00 00               mov r14d, 1
00C2EC69  4D 85 ED                        test r13, r13
00C2EC6C  74 15                           je 0x140c2ec83
00C2EC6E  48 85 FF                        test rdi, rdi
00C2EC71  74 04                           je 0x140c2ec77
00C2EC73  44 01 77 1C                     add dword ptr [rdi + 0x1c], r14d
00C2EC77  4C 89 6B 10                     mov qword ptr [rbx + 0x10], r13
00C2EC7B  EB 0A                           jmp 0x140c2ec87
00C2EC7D  41 BE 01 00 00 00               mov r14d, 1
00C2EC83  44 88 73 2E                     mov byte ptr [rbx + 0x2e], r14b
00C2EC87  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
00C2EC8B  33 D2                           xor edx, edx
00C2EC8D  E8 DE 3B F5 FF                  call 0x140b82870
00C2EC92  33 FF                           xor edi, edi
00C2EC94  40 38 7B 2E                     cmp byte ptr [rbx + 0x2e], dil
00C2EC98  75 41                           jne 0x140c2ecdb
00C2EC9A  E8 E9 56 87 FF                  call 0x1404a4388
00C2EC9F  49 8B 55 30                     mov rdx, qword ptr [r13 + 0x30]
00C2ECA3  48 83 C2 18                     add rdx, 0x18
00C2ECA7  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
00C2ECAC  E8 8F D2 AF FF                  call 0x14072bf40
00C2ECB1  E8 3E 56 87 FF                  call 0x1404a42f4
00C2ECB6  E8 F1 88 B0 FF                  call 0x1407375ac
00C2ECBB  45 33 C9                        xor r9d, r9d
00C2ECBE  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00C2ECC3  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00C2ECC8  45 33 C0                        xor r8d, r8d
00C2ECCB  33 C9                           xor ecx, ecx
00C2ECCD  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00C2ECD2  41 8D 51 07                     lea edx, [r9 + 7]
00C2ECD6  E8 1D 93 84 FF                  call 0x140477ff8
00C2ECDB  E8 70 56 AD FF                  call 0x140704350
00C2ECE0  85 C0                           test eax, eax
00C2ECE2  78 37                           js 0x140c2ed1b
00C2ECE4  48 8B 1B                        mov rbx, qword ptr [rbx]
00C2ECE7  E9 54 FE FF FF                  jmp 0x140c2eb40
00C2ECEC  66 44 3B 7C 24 68               cmp r15w, word ptr [rsp + 0x68]
00C2ECF2  75 1E                           jne 0x140c2ed12
00C2ECF4  33 D2                           xor edx, edx
00C2ECF6  33 C9                           xor ecx, ecx
00C2ECF8  E8 3B 54 00 00                  call 0x140c34138
00C2ECFD  48 8D 05 7C F9 AF FF            lea rax, [rip - 0x500684]
00C2ED04  44 88 35 ED D8 35 00            mov byte ptr [rip + 0x35d8ed], r14b
00C2ED0B  48 89 05 26 D4 35 00            mov qword ptr [rip + 0x35d426], rax
00C2ED12  66 45 03 FE                     add r15w, r14w
00C2ED16  E9 00 FE FF FF                  jmp 0x140c2eb1b
00C2ED1B  33 D2                           xor edx, edx
00C2ED1D  8D 4A 12                        lea ecx, [rdx + 0x12]
00C2ED20  E8 C7 90 88 FF                  call 0x1404b7dec
00C2ED25  C7 05 A1 EB 35 00 21 00 00 00   mov dword ptr [rip + 0x35eba1], 0x21
00C2ED2F  B8 7D 04 00 C0                  mov eax, 0xc000047d
00C2ED34  E9 1C 03 00 00                  jmp 0x140c2f055
00C2ED39  B9 02 00 00 00                  mov ecx, 2
00C2ED3E  E8 DD 03 FC FF                  call 0x140bef120
00C2ED43  48 8B CE                        mov rcx, rsi
00C2ED46  E8 8D 39 00 00                  call 0x140c326d8
00C2ED4B  45 33 E4                        xor r12d, r12d
00C2ED4E  44 88 35 A4 D8 35 00            mov byte ptr [rip + 0x35d8a4], r14b
00C2ED55  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
00C2ED5A  45 33 C9                        xor r9d, r9d
00C2ED5D  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00C2ED62  45 33 C0                        xor r8d, r8d
00C2ED65  33 D2                           xor edx, edx
00C2ED67  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C2ED6C  33 C9                           xor ecx, ecx
00C2ED6E  E8 85 92 84 FF                  call 0x140477ff8
00C2ED73  E8 B8 3B 00 00                  call 0x140c32930
00C2ED78  85 C0                           test eax, eax
00C2ED7A  75 16                           jne 0x140c2ed92
00C2ED7C  33 D2                           xor edx, edx
00C2ED7E  8D 48 13                        lea ecx, [rax + 0x13]
00C2ED81  E8 66 90 88 FF                  call 0x1404b7dec
00C2ED86  C7 05 40 EB 35 00 22 00 00 00   mov dword ptr [rip + 0x35eb40], 0x22
00C2ED90  EB 9D                           jmp 0x140c2ed2f
00C2ED92  E8 59 EC FF FF                  call 0x140c2d9f0
00C2ED97  84 C0                           test al, al
00C2ED99  74 22                           je 0x140c2edbd
00C2ED9B  E8 90 3B 00 00                  call 0x140c32930
00C2EDA0  85 C0                           test eax, eax
00C2EDA2  75 19                           jne 0x140c2edbd
00C2EDA4  33 D2                           xor edx, edx
00C2EDA6  8D 48 14                        lea ecx, [rax + 0x14]
00C2EDA9  E8 3E 90 88 FF                  call 0x1404b7dec
00C2EDAE  C7 05 18 EB 35 00 23 00 00 00   mov dword ptr [rip + 0x35eb18], 0x23
00C2EDB8  E9 72 FF FF FF                  jmp 0x140c2ed2f
00C2EDBD  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00C2EDC1  48 8B D6                        mov rdx, rsi
00C2EDC4  33 C9                           xor ecx, ecx
00C2EDC6  E8 3D 01 04 00                  call 0x140c6ef08
00C2EDCB  85 C0                           test eax, eax
00C2EDCD  78 44                           js 0x140c2ee13
00C2EDCF  E8 5C 3B 00 00                  call 0x140c32930
00C2EDD4  85 C0                           test eax, eax
00C2EDD6  75 19                           jne 0x140c2edf1
00C2EDD8  33 D2                           xor edx, edx
00C2EDDA  8D 48 13                        lea ecx, [rax + 0x13]
00C2EDDD  E8 0A 90 88 FF                  call 0x1404b7dec
00C2EDE2  C7 05 E4 EA 35 00 24 00 00 00   mov dword ptr [rip + 0x35eae4], 0x24
00C2EDEC  E9 3E FF FF FF                  jmp 0x140c2ed2f
00C2EDF1  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00C2EDF5  48 8B D6                        mov rdx, rsi
00C2EDF8  41 8B CE                        mov ecx, r14d
00C2EDFB  E8 08 01 04 00                  call 0x140c6ef08
00C2EE00  85 C0                           test eax, eax
00C2EE02  79 0F                           jns 0x140c2ee13
00C2EE04  C7 05 C2 EA 35 00 2E 00 00 00   mov dword ptr [rip + 0x35eac2], 0x2e
00C2EE0E  E9 42 02 00 00                  jmp 0x140c2f055
00C2EE13  48 8B CE                        mov rcx, rsi
00C2EE16  E8 99 ED 03 00                  call 0x140c6dbb4
00C2EE1B  85 C0                           test eax, eax
00C2EE1D  78 22                           js 0x140c2ee41
00C2EE1F  E8 0C 3B 00 00                  call 0x140c32930
00C2EE24  85 C0                           test eax, eax
00C2EE26  75 19                           jne 0x140c2ee41
00C2EE28  33 D2                           xor edx, edx
00C2EE2A  8D 48 13                        lea ecx, [rax + 0x13]
00C2EE2D  E8 BA 8F 88 FF                  call 0x1404b7dec
00C2EE32  C7 05 94 EA 35 00 25 00 00 00   mov dword ptr [rip + 0x35ea94], 0x25
00C2EE3C  E9 EE FE FF FF                  jmp 0x140c2ed2f
00C2EE41  41 8A D6                        mov dl, r14b
00C2EE44  48 8B CE                        mov rcx, rsi
00C2EE47  E8 00 F8 03 00                  call 0x140c6e64c
00C2EE4C  85 C0                           test eax, eax
00C2EE4E  78 22                           js 0x140c2ee72
00C2EE50  E8 DB 3A 00 00                  call 0x140c32930
00C2EE55  85 C0                           test eax, eax
00C2EE57  75 19                           jne 0x140c2ee72
00C2EE59  33 D2                           xor edx, edx
00C2EE5B  8D 48 13                        lea ecx, [rax + 0x13]
00C2EE5E  E8 89 8F 88 FF                  call 0x1404b7dec
00C2EE63  C7 05 63 EA 35 00 26 00 00 00   mov dword ptr [rip + 0x35ea63], 0x26
00C2EE6D  E9 BD FE FF FF                  jmp 0x140c2ed2f
00C2EE72  48 8B 86 F0 00 00 00            mov rax, qword ptr [rsi + 0xf0]
00C2EE79  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
00C2EE7E  44 39 A0 70 0F 00 00            cmp dword ptr [rax + 0xf70], r12d
00C2EE85  74 40                           je 0x140c2eec7
00C2EE87  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00C2EE8C  E8 C3 03 04 00                  call 0x140c6f254
00C2EE91  85 C0                           test eax, eax
00C2EE93  78 07                           js 0x140c2ee9c
00C2EE95  44 38 64 24 40                  cmp byte ptr [rsp + 0x40], r12b
00C2EE9A  74 2B                           je 0x140c2eec7
00C2EE9C  48 8B CE                        mov rcx, rsi
00C2EE9F  48 FF 15 02 24 52 FF            call qword ptr [rip - 0xaddbfe]
00C2EEA6  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00C2EEAB  85 C0                           test eax, eax
00C2EEAD  79 18                           jns 0x140c2eec7
00C2EEAF  45 33 C9                        xor r9d, r9d
00C2EEB2  4C 63 C0                        movsxd r8, eax
00C2EEB5  49 8B D6                        mov rdx, r14
00C2EEB8  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00C2EEBD  41 8D 49 7B                     lea ecx, [r9 + 0x7b]
00C2EEC1  E8 9A E7 8C FF                  call 0x1404fd660
00C2EEC6  CC                              int3
00C2EEC7  E8 64 3A 00 00                  call 0x140c32930
00C2EECC  85 C0                           test eax, eax
00C2EECE  75 19                           jne 0x140c2eee9
00C2EED0  33 D2                           xor edx, edx
00C2EED2  8D 48 13                        lea ecx, [rax + 0x13]
00C2EED5  E8 12 8F 88 FF                  call 0x1404b7dec
00C2EEDA  C7 05 EC E9 35 00 2C 00 00 00   mov dword ptr [rip + 0x35e9ec], 0x2c
00C2EEE4  E9 46 FE FF FF                  jmp 0x140c2ed2f
00C2EEE9  48 8B CE                        mov rcx, rsi
00C2EEEC  E8 2B D0 FF FF                  call 0x140c2bf1c
00C2EEF1  85 C0                           test eax, eax
00C2EEF3  79 0F                           jns 0x140c2ef04
00C2EEF5  C7 05 D1 E9 35 00 27 00 00 00   mov dword ptr [rip + 0x35e9d1], 0x27
00C2EEFF  E9 51 01 00 00                  jmp 0x140c2f055
00C2EF04  45 33 C9                        xor r9d, r9d
00C2EF07  4C 8D 05 92 E0 FF FF            lea r8, [rip - 0x1f6e]
00C2EF0E  41 8B D6                        mov edx, r14d
00C2EF11  48 8B CE                        mov rcx, rsi
00C2EF14  E8 4F 5E 97 FF                  call 0x1405a4d68
00C2EF19  48 8B 86 F0 00 00 00            mov rax, qword ptr [rsi + 0xf0]
00C2EF20  44 88 35 D3 D6 35 00            mov byte ptr [rip + 0x35d6d3], r14b
00C2EF27  F7 80 84 00 00 00 00 04 00 00   test dword ptr [rax + 0x84], 0x400
00C2EF31  74 2A                           je 0x140c2ef5d
00C2EF33  E8 C8 05 04 00                  call 0x140c6f500
00C2EF38  85 C0                           test eax, eax
00C2EF3A  78 12                           js 0x140c2ef4e
00C2EF3C  E8 97 09 04 00                  call 0x140c6f8d8
00C2EF41  85 C0                           test eax, eax
00C2EF43  78 09                           js 0x140c2ef4e
00C2EF45  E8 CA 03 04 00                  call 0x140c6f314
00C2EF4A  85 C0                           test eax, eax
00C2EF4C  79 0F                           jns 0x140c2ef5d
00C2EF4E  C7 05 78 E9 35 00 28 00 00 00   mov dword ptr [rip + 0x35e978], 0x28
00C2EF58  E9 F8 00 00 00                  jmp 0x140c2f055
00C2EF5D  33 D2                           xor edx, edx
00C2EF5F  48 8B CE                        mov rcx, rsi
00C2EF62  E8 E5 F6 03 00                  call 0x140c6e64c
00C2EF67  85 C0                           test eax, eax
00C2EF69  79 0F                           jns 0x140c2ef7a
00C2EF6B  C7 05 5B E9 35 00 29 00 00 00   mov dword ptr [rip + 0x35e95b], 0x29
00C2EF75  E9 DB 00 00 00                  jmp 0x140c2f055
00C2EF7A  E8 B5 E9 03 00                  call 0x140c6d934
00C2EF7F  48 8B CE                        mov rcx, rsi
00C2EF82  E8 F5 37 00 00                  call 0x140c3277c
00C2EF87  85 C0                           test eax, eax
00C2EF89  79 0F                           jns 0x140c2ef9a
00C2EF8B  C7 05 3B E9 35 00 2A 00 00 00   mov dword ptr [rip + 0x35e93b], 0x2a
00C2EF95  E9 BB 00 00 00                  jmp 0x140c2f055
00C2EF9A  E8 09 3A 00 00                  call 0x140c329a8
00C2EF9F  85 C0                           test eax, eax
00C2EFA1  79 0F                           jns 0x140c2efb2
00C2EFA3  C7 05 23 E9 35 00 2B 00 00 00   mov dword ptr [rip + 0x35e923], 0x2b
00C2EFAD  E9 A3 00 00 00                  jmp 0x140c2f055
00C2EFB2  48 8D 54 24 5C                  lea rdx, [rsp + 0x5c]
00C2EFB7  66 44 89 65 00                  mov word ptr [rbp], r12w
00C2EFBC  E8 F7 45 AF FF                  call 0x1407235b8
00C2EFC1  44 8B E8                        mov r13d, eax
00C2EFC4  85 C0                           test eax, eax
00C2EFC6  78 32                           js 0x140c2effa
00C2EFC8  8B 44 24 5C                     mov eax, dword ptr [rsp + 0x5c]
00C2EFCC  48 8D 4D 00                     lea rcx, [rbp]
00C2EFD0  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00C2EFD4  45 33 C9                        xor r9d, r9d
00C2EFD7  48 8D 05 B2 B1 04 00            lea rax, [rip + 0x4b1b2]
00C2EFDE  45 33 C0                        xor r8d, r8d
00C2EFE1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C2EFE6  C7 44 24 20 00 08 00 00         mov dword ptr [rsp + 0x20], 0x800
00C2EFEE  41 8D 51 40                     lea edx, [r9 + 0x40]
00C2EFF2  E8 99 C3 7F FF                  call 0x14042b390
00C2EFF7  44 8B E8                        mov r13d, eax
00C2EFFA  45 33 FF                        xor r15d, r15d
00C2EFFD  44 39 3D 9C DF 35 00            cmp dword ptr [rip + 0x35df9c], r15d
00C2F004  76 27                           jbe 0x140c2f02d
00C2F006  41 0F B7 D4                     movzx edx, r12w
00C2F00A  48 C1 E2 04                     shl rdx, 4
00C2F00E  48 03 15 93 DF 35 00            add rdx, qword ptr [rip + 0x35df93]
00C2F015  48 8B 1A                        mov rbx, qword ptr [rdx]
00C2F018  48 3B DA                        cmp rbx, rdx
00C2F01B  75 69                           jne 0x140c2f086
00C2F01D  66 45 03 E6                     add r12w, r14w
00C2F021  41 0F B7 C4                     movzx eax, r12w
00C2F025  3B 05 75 DF 35 00               cmp eax, dword ptr [rip + 0x35df75]
00C2F02B  72 D9                           jb 0x140c2f006
00C2F02D  48 8B 0D 74 DF 35 00            mov rcx, qword ptr [rip + 0x35df74]
00C2F034  33 D2                           xor edx, edx
00C2F036  E8 35 38 F5 FF                  call 0x140b82870
00C2F03B  45 33 C0                        xor r8d, r8d
00C2F03E  44 88 35 FF 71 23 00            mov byte ptr [rip + 0x2371ff], r14b
00C2F045  33 D2                           xor edx, edx
00C2F047  48 8D 0D B2 7D 3F FF            lea rcx, [rip - 0xc0824e]
00C2F04E  E8 31 F3 63 FF                  call 0x14026e384
00C2F053  33 C0                           xor eax, eax
00C2F055  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
00C2F05C  48 33 CC                        xor rcx, rsp
00C2F05F  E8 DC D5 A7 FF                  call 0x1406ac640
00C2F064  4C 8D 9C 24 90 01 00 00         lea r11, [rsp + 0x190]
00C2F06C  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00C2F070  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00C2F074  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00C2F078  49 8B E3                        mov rsp, r11
00C2F07B  41 5F                           pop r15
00C2F07D  41 5E                           pop r14
00C2F07F  41 5D                           pop r13
00C2F081  41 5C                           pop r12
00C2F083  5D                              pop rbp
00C2F084  C3                              ret
00C2F085  CC                              int3
00C2F086  48 39 53 08                     cmp qword ptr [rbx + 8], rdx
00C2F08A  0F 85 FA 01 00 00               jne 0x140c2f28a
00C2F090  48 8B 03                        mov rax, qword ptr [rbx]
00C2F093  48 39 58 08                     cmp qword ptr [rax + 8], rbx
00C2F097  0F 85 ED 01 00 00               jne 0x140c2f28a
00C2F09D  48 89 02                        mov qword ptr [rdx], rax
00C2F0A0  48 89 50 08                     mov qword ptr [rax + 8], rdx
00C2F0A4  48 8B 7B 10                     mov rdi, qword ptr [rbx + 0x10]
00C2F0A8  45 85 ED                        test r13d, r13d
00C2F0AB  0F 88 9C 01 00 00               js 0x140c2f24d
00C2F0B1  44 38 7B 2E                     cmp byte ptr [rbx + 0x2e], r15b
00C2F0B5  0F 85 92 01 00 00               jne 0x140c2f24d
00C2F0BB  4C 39 7F 08                     cmp qword ptr [rdi + 8], r15
00C2F0BF  0F 85 88 01 00 00               jne 0x140c2f24d
00C2F0C5  48 8B 47 30                     mov rax, qword ptr [rdi + 0x30]
00C2F0C9  4C 39 78 08                     cmp qword ptr [rax + 8], r15
00C2F0CD  0F 84 7A 01 00 00               je 0x140c2f24d
00C2F0D3  F7 47 10 08 04 00 00            test dword ptr [rdi + 0x10], 0x408
00C2F0DA  0F 85 6D 01 00 00               jne 0x140c2f24d
00C2F0E0  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
00C2F0E4  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
00C2F0E9  45 33 C0                        xor r8d, r8d
00C2F0EC  48 8D 15 7D A8 04 00            lea rdx, [rip + 0x4a87d]
00C2F0F3  E8 F4 9F D6 FF                  call 0x1409990ec
00C2F0F8  85 C0                           test eax, eax
00C2F0FA  0F 88 4D 01 00 00               js 0x140c2f24d
00C2F100  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
00C2F105  41 83 7E 04 04                  cmp dword ptr [r14 + 4], 4
00C2F10A  0F 85 2D 01 00 00               jne 0x140c2f23d
00C2F110  41 83 7E 0C 04                  cmp dword ptr [r14 + 0xc], 4
00C2F115  0F 82 22 01 00 00               jb 0x140c2f23d
00C2F11B  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
00C2F11F  42 8B 0C 30                     mov ecx, dword ptr [rax + r14]
00C2F123  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
00C2F127  85 C9                           test ecx, ecx
00C2F129  0F 85 0E 01 00 00               jne 0x140c2f23d
00C2F12F  C7 44 24 58 03 00 00 00         mov dword ptr [rsp + 0x58], 3
00C2F137  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00C2F13C  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
00C2F140  48 83 C1 18                     add rcx, 0x18
00C2F144  E8 33 A4 D6 FF                  call 0x14099957c
00C2F149  85 C0                           test eax, eax
00C2F14B  79 0B                           jns 0x140c2f158
00C2F14D  48 8B 73 20                     mov rsi, qword ptr [rbx + 0x20]
00C2F151  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
00C2F156  EB 05                           jmp 0x140c2f15d
00C2F158  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
00C2F15D  48 8B 0D 34 72 23 00            mov rcx, qword ptr [rip + 0x237234]
00C2F164  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00C2F169  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
00C2F16E  4C 8D 05 2B B0 04 00            lea r8, [rip + 0x4b02b]
00C2F175  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00C2F17A  45 33 C9                        xor r9d, r9d
00C2F17D  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
00C2F182  48 8B D6                        mov rdx, rsi
00C2F185  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
00C2F18D  E8 52 A1 E3 FF                  call 0x140a692e4
00C2F192  85 C0                           test eax, eax
00C2F194  0F 88 90 00 00 00               js 0x140c2f22a
00C2F19A  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
00C2F19F  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00C2F1A4  41 B9 04 00 00 00               mov r9d, 4
00C2F1AA  4C 8D 45 00                     lea r8, [rbp]
00C2F1AE  44 89 4C 24 28                  mov dword ptr [rsp + 0x28], r9d
00C2F1B3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C2F1B8  E8 CF 29 D6 FF                  call 0x140991b8c
00C2F1BD  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
00C2F1C2  E8 45 3C DF FF                  call 0x140a22e0c
00C2F1C7  F6 05 5D 0F 2C 00 02            test byte ptr [rip + 0x2c0f5d], 2
00C2F1CE  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
00C2F1D3  74 55                           je 0x140c2f22a
00C2F1D5  4C 8B 47 30                     mov r8, qword ptr [rdi + 0x30]
00C2F1D9  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
00C2F1DE  49 83 C0 18                     add r8, 0x18
00C2F1E2  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
00C2F1E7  33 D2                           xor edx, edx
00C2F1E9  E8 D2 9E DA FF                  call 0x1409d90c0
00C2F1EE  85 C0                           test eax, eax
00C2F1F0  78 38                           js 0x140c2f22a
00C2F1F2  F6 05 32 0F 2C 00 02            test byte ptr [rip + 0x2c0f32], 2
00C2F1F9  4C 8B 7C 24 50                  mov r15, qword ptr [rsp + 0x50]
00C2F1FE  74 17                           je 0x140c2f217
00C2F200  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
00C2F204  44 8B 4C 24 5C                  mov r9d, dword ptr [rsp + 0x5c]
00C2F209  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00C2F20D  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00C2F212  E8 21 53 97 FF                  call 0x1405a4538
00C2F217  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
00C2F21B  49 8B CF                        mov rcx, r15
00C2F21E  48 83 C2 18                     add rdx, 0x18
00C2F222  E8 C9 67 CC FF                  call 0x1408f59f0
00C2F227  45 33 FF                        xor r15d, r15d
00C2F22A  48 3B 73 20                     cmp rsi, qword ptr [rbx + 0x20]
00C2F22E  74 0D                           je 0x140c2f23d
00C2F230  48 8B CE                        mov rcx, rsi
00C2F233  E8 78 E0 A7 FF                  call 0x1406ad2b0
00C2F238  4C 89 7C 24 78                  mov qword ptr [rsp + 0x78], r15
00C2F23D  33 D2                           xor edx, edx
00C2F23F  49 8B CE                        mov rcx, r14
00C2F242  E8 29 36 F5 FF                  call 0x140b82870
00C2F247  41 BE 01 00 00 00               mov r14d, 1
00C2F24D  48 85 FF                        test rdi, rdi
00C2F250  74 0D                           je 0x140c2f25f
00C2F252  BA 44 66 6C 74                  mov edx, 0x746c6644
00C2F257  48 8B CF                        mov rcx, rdi
00C2F25A  E8 81 86 6C FF                  call 0x1402f78e0
00C2F25F  44 38 7B 2E                     cmp byte ptr [rbx + 0x2e], r15b
00C2F263  74 0D                           je 0x140c2f272
00C2F265  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00C2F269  48 8B 50 30                     mov rdx, qword ptr [rax + 0x30]
00C2F26D  0F BA 6A 68 11                  bts dword ptr [rdx + 0x68], 0x11
00C2F272  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
00C2F276  E8 35 E0 A7 FF                  call 0x1406ad2b0
00C2F27B  33 D2                           xor edx, edx
00C2F27D  48 8B CB                        mov rcx, rbx
00C2F280  E8 EB 35 F5 FF                  call 0x140b82870
00C2F285  E9 7C FD FF FF                  jmp 0x140c2f006
00C2F28A  B9 03 00 00 00                  mov ecx, 3
00C2F28F  CD 29                           int 0x29
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopInitializeBootDrivers(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m134;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned int v_stack_m15C;
    unsigned int v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int8 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned int v_stack_m190;
    unsigned int v_stack_m198;
    unsigned __int64 v_stack_m28;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (400);
    result = (*(unsigned __int64 *)(v_rip + 1949727)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 184 + 128) = result;
    v_r12 = 0;
    *(unsigned int *)(v_rsp - 184 - 108) = 0;
    v_stack_m15C = 0;
    result = 0;
    v_stack_m170 = 0;
    v_stack_m158 = 0;
    a3 = 0;
    *(unsigned int *)(v_rsp - 184 - 124) = 0;
    a2 = 0;
    *(unsigned int *)(v_rsp - 184 - 76) = 0;
    *(unsigned __int64 *)(v_rsp - 184 - 24) = v_xmm0;
    v_stack_m140 = 0;
    *(unsigned __int64 *)(v_rsp - 184 - 64) = v_xmm0;
    v_stack_m148 = 0;
    v_stack_m160 = 0;
    *(unsigned __int64 *)(v_rsp - 184 - 96) = v_xmm0;
    *(unsigned int *)(v_rsp - 184 - 32) = 0;
    *(unsigned __int64 *)(v_rsp - 184 - 48) = v_xmm1;
    v_stack_m168 = 0;
    result = PnpDiagnosticTrace(v_rip - 12612542, a2, a3, a4);
    *(unsigned int *)(v_rip + 4038375) = 3;
    *(unsigned __int64 *)(v_rsp - 184 - 120) = v_rip + 309437;
    *(unsigned int *)(v_rsp - 184 - 128) = 0x80007EULL;
    a2 = 0;
    result = IopOpenRegistryKeyEx(v_stack_m170, a2, v_rsp - 184 - 128, (unsigned int)((unsigned int)((unsigned int)(0x20019ULL))));
    if (!sign_flag) goto loc_00C2E7ED;
    *(unsigned int *)(v_rsp - 184 - 128) = 0x7E007CULL;
    *(unsigned __int64 *)(v_rsp - 184 - 120) = v_rip + 309509;
    a2 = 0;
    result = IopOpenRegistryKeyEx(v_stack_m170, a2, v_rsp - 184 - 128, (unsigned int)((unsigned int)((unsigned int)(0x20019ULL))));
    if (sign_flag) goto loc_00C2E841;
loc_00C2E7ED:
    a3 = 0;
    result = IopGetRegistryValue(v_stack_m170, v_rip + 309583, a3, v_stack_m158);
    result = ZwClose(v_stack_m170, v_rip + 309583, a3, v_stack_m158);
    if (sign_flag) goto loc_00C2E841;
    if ((*(unsigned int *)(v_stack_m158 + 4)) != 4) goto loc_00C2E837;
    if ((*(unsigned int *)(v_stack_m158 + 12)) >= 4) {
        result = *(unsigned int *)(v_stack_m158 + 8);
        a1 = *(unsigned int *)(result + v_stack_m158 * 1);
        *(unsigned int *)(v_rip + 4038221) = (unsigned int)(a1);
    }
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m158, a2, v_stack_m158, v_stack_m158);
loc_00C2E841:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4038205)))) != 8) goto loc_00C2E855;
    *(unsigned int *)(v_rip + 4038193) = 0;
    goto loc_00C2E866;
loc_00C2E855:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4038205)))) & (0xFFFFFFF8ULL)) != 0) {
        *(unsigned int *)(v_rip + 4038174) = 3;
    }
    result = PipInitializeCoreDriversAndElam(a1, a2, v_stack_m158, v_stack_m158);
    *(unsigned int *)(v_rsp - 184 - 80) = 0x20001EULL;
    *(unsigned __int64 *)(v_rsp - 184 - 72) = v_rip + 309627;
    *(unsigned int *)(v_rsp - 184 - 112) = 0x20000ULL;
    *(unsigned __int64 *)(v_rsp - 184 - 104) = v_rip + 309634;
    v_stack_m180 = v_stack_m168;
    v_stack_m190 = 0;
    a4 = 0;
    v_stack_m198 = 0;
    result = PnpInitializeBootStartDriver(v_rsp - 184 - 80, v_rsp - 184 - 112, v_rip + 100361, a4);
    v_stack_m168 = v_stack_m168;
    if (v_stack_m168 != 0) goto loc_00C2E8E3;
    *(unsigned int *)(v_rip + 3534834) = (unsigned int)(32 - 2);
    goto loc_00C2F055;
loc_00C2E8E3:
    a1 = 0;
    result = PpInitGetGroupOrderIndex(a1, v_rsp - 184 - 112, v_rip + 100361, a4);
    *(unsigned int *)(v_rip + 3532455) = (unsigned int)((unsigned __int16)(result));
    v_stack_m150 = (unsigned int)((unsigned int)(0xFFFFULL));
    if (((unsigned int)((unsigned __int16)(result))) != ((unsigned int)((unsigned int)(0xFFFFULL)))) goto loc_00C2E921;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(a2 + 16, a2, v_rip + 100361, a4);
    *(unsigned int *)(v_rip + 3534772) = 31;
    goto loc_00C2F055;
loc_00C2E921:
    a2 = ((unsigned int)(0xC0000225ULL)) << (4);
    result = ExAllocatePool2(256, a2, (unsigned int)(0x6E697050ULL), a4);
    *(unsigned __int64 *)(v_rip + 3532393) = result;
    if (result != 0) goto loc_00C2E95F;
    result = HeadlessKernelAddLogEntry(result + 17, result, (unsigned int)(0x6E697050ULL), a4);
    *(unsigned int *)(v_rip + 3534710) = 32;
    goto loc_00C2F055;
loc_00C2E95F:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3532346))) == 0) goto loc_00C2E992;
loc_00C2E975:
    a1 = (unsigned __int16)((0) + (1));
    result = (0) << (4);
    result = (result) + (result);
    *(unsigned __int64 *)(result + 8) = result;
    *(unsigned __int64 *)(result) = result;
    if (((unsigned int)((unsigned __int16)(a1))) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3532346))))) goto loc_00C2E975;
loc_00C2E992:
    result = PipInitializeDriverDependentDLLs((unsigned int)((unsigned int)(32 - 30)), a1, (unsigned int)(*(unsigned int *)(v_rip + 3532346)), a4);
    result = RtlInitUnicodeString(v_rsp - 184 - 96, v_rip + 309372, (unsigned int)(*(unsigned int *)(v_rip + 3532346)), a4);
    result = RtlInitUnicodeString(v_rsp - 184 - 24, v_rip + 309388, (unsigned int)(*(unsigned int *)(v_rip + 3532346)), a4);
    if (0 >= (*(unsigned __int16 *)(v_rip + 2324619))) goto loc_00C2EA2F;
loc_00C2E9D2:
    v_r14 = (0) << (4);
    a1 = (*(unsigned __int64 *)(v_rip + 2324591)) + (v_r14);
    result = RtlCompareUnicodeString(a1, v_rsp - 184 - 96, 1, a4);
    if ((unsigned int)(result) == 0) goto loc_00C2EA13;
    a1 = (*(unsigned __int64 *)(v_rip + 2324557)) + (v_r14);
    result = RtlCompareUnicodeString(a1, v_rsp - 184 - 24, 1, a4);
    if ((unsigned int)(result) != 0) goto loc_00C2EA17;
    v_stack_m150 = 0;
loc_00C2EA13:
    v_rbx = (unsigned __int16)((0) + (1));
loc_00C2EA17:
    if (((unsigned __int16)(v_rbx)) >= ((unsigned __int16)((unsigned int)((unsigned int)(32 - 30))))) goto loc_00C2EA2A;
    v_rdi = (unsigned __int16)((0) + (1));
    if (((unsigned __int16)(v_rdi)) < (*(unsigned __int16 *)(v_rip + 2324520))) goto loc_00C2E9D2;
loc_00C2EA2A:
loc_00C2EA2F:
    goto loc_00C2EB00;
loc_00C2EA3B:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 48) + 56)) < 0) goto loc_00C2EB00;
    result = ExAllocatePool2(256, 48, (unsigned int)(0x6E697050ULL), a4);
    if (result == 0) goto loc_00C2EB00;
    *(unsigned __int64 *)(result + 8) = result;
    *(unsigned __int64 *)(result) = result;
    a2 = 0;
    *(unsigned __int64 *)(result + 24) = *(unsigned __int64 *)(a1 + 48);
    result = IopOpenRegistryKeyEx(v_stack_m170, a2, *(unsigned __int64 *)(a1 + 48) + 32, (unsigned int)(0x20019ULL));
    if (!sign_flag) goto loc_00C2EA9D;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, *(unsigned __int64 *)(a1 + 48) + 32, (unsigned int)(0x20019ULL));
    goto loc_00C2EB00;
loc_00C2EA9D:
    *(unsigned __int64 *)(result + 32) = v_stack_m170;
    result = PpInitGetGroupOrderIndex(v_stack_m170, a2, *(unsigned __int64 *)(a1 + 48) + 32, (unsigned int)(0x20019ULL));
    result = PipGetDriverTagPriority(v_stack_m170, a2, *(unsigned __int64 *)(a1 + 48) + 32, (unsigned int)(0x20019ULL));
    *(unsigned __int16 *)(result + 44) = (unsigned __int16)(result);
    a2 = ((unsigned int)((unsigned int)((unsigned __int16)(result)))) << (4);
    a2 = (a2) + (*(unsigned __int64 *)(v_rip + 3531994));
    goto loc_00C2EADC;
loc_00C2EAD3:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2) + 44)) > ((unsigned __int16)(result))) goto loc_00C2EAE1;
loc_00C2EADC:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2))) != a2) goto loc_00C2EAD3;
loc_00C2EAE1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2)) + 8)) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2)) + 8))) goto loc_00C2F28A;
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2)) + 8));
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2)) + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2)) + 8)) + 8) = result;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2)) + 8)) = result;
loc_00C2EB00:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48))) != (a1 + 48)) goto loc_00C2EA3B;
    result = PnpNotifyEarlyLaunchStatusUpdate(1, a2, *(unsigned __int64 *)(a1 + 48) + 32, (unsigned int)(0x20019ULL));
loc_00C2EB1B:
    if (0 >= (*(unsigned int *)(v_rip + 3531899))) goto loc_00C2ED39;
    v_r12 = (0) << (4);
    v_rdi = 0;
loc_00C2EB40:
    a1 = (*(unsigned __int64 *)(v_rip + 3531873)) + (v_r12);
    if ((*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_rip + 3531894) * 1)) == a1) goto loc_00C2ECEC;
    v_stack_m170 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_rip + 3531894) * 1) + 32);
    v_stack_m168 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_rip + 3531894) * 1) + 24);
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_rip + 3531894) * 1) + 47) = 1;
    *(unsigned __int64 *)(v_rsp - 184 - 96) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_rip + 3531894) * 1) + 24) + 48);
    result = IopGetDriverNameFromKeyNode(v_stack_m170, v_rsp - 184 - 112, *(unsigned __int64 *)(a1 + 48) + 32, (unsigned int)(0x20019ULL));
    if (!sign_flag) goto loc_00C2EB92;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_rip + 3531894) * 1) + 46) = 1;
    goto loc_00C2EC94;
loc_00C2EB92:
    a3 = 0;
    result = IopGetRegistryValue(v_stack_m170, v_rip + 308698, a3, v_stack_m158);
    if (sign_flag) goto loc_00C2EBF2;
    if ((*(unsigned int *)(v_stack_m158 + 12)) != 0) {
        result = *(unsigned __int16 *)(v_stack_m158 + 12);
        a1 = v_rsp - 184 - 64;
        *(unsigned __int16 *)(v_rsp - 184 - 64) = (unsigned __int16)(result);
        a2 = 1;
        *(unsigned __int16 *)(v_rsp - 184 - 62) = (unsigned __int16)(result);
        result = *(unsigned int *)(v_stack_m158 + 8);
        result = (result) + (v_stack_m158);
        *(unsigned __int64 *)(v_rsp - 184 - 56) = result;
        result = PipLookupGroupName(a1, a2, a3, v_stack_m158);
        v_rdi = result;
    }
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m158, a2, a3, v_stack_m158);
loc_00C2EBF2:
    v_r13 = 0;
    result = PipCheckDependencies(v_stack_m170, a2, a3, v_stack_m158);
    if ((unsigned int)(result) == 0) goto loc_00C2EC7D;
    v_stack_m168 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_rip + 3531894) * 1) + 16);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_rip + 3531894) * 1) + 16) != 0) goto loc_00C2EC63;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_rip + 3531894) * 1) + 46)) != ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_rip + 3531894) * 1) + 16)))) goto loc_00C2EC63;
    v_stack_m180 = v_stack_m168;
    v_stack_m190 = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_rip + 3531894) * 1) + 16) + 1);
    result = PnpInitializeBootStartDriver(v_rsp - 184 - 112, v_stack_m168 + 32, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 184 - 96) + 56), *(unsigned __int64 *)(v_rsp - 184 - 96));
    *(unsigned int *)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_rip + 3531894) * 1) + 40) = (unsigned int)(result);
    if (v_stack_m168 == 0) goto loc_00C2EC83;
    result = ObfReferenceObjectWithTag(v_stack_m168, (unsigned int)(0x746C6644ULL), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 184 - 96) + 56), *(unsigned __int64 *)(v_rsp - 184 - 96));
    goto loc_00C2EC69;
loc_00C2EC63:
loc_00C2EC69:
    if (v_stack_m168 == 0) goto loc_00C2EC83;
    if (v_rdi != 0) {
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_rip + 3531894) * 1) + 16) = v_stack_m168;
    goto loc_00C2EC87;
loc_00C2EC7D:
loc_00C2EC83:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_rip + 3531894) * 1) + 46) = 1;
loc_00C2EC87:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 184 - 104), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 184 - 96) + 56), *(unsigned __int64 *)(v_rsp - 184 - 96));
    v_rdi = 0;
loc_00C2EC94:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_rip + 3531894) * 1) + 46)) == 0) {
        result = PnpLockDeviceActionQueue(*(unsigned __int64 *)(v_rsp - 184 - 104), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 184 - 96) + 56), *(unsigned __int64 *)(v_rsp - 184 - 96));
        a2 = *(unsigned __int64 *)(v_stack_m168 + 48);
        a2 = (a2) + (24);
        v_stack_m190 = v_stack_m168;
        result = PipApplyFunctionToServiceInstances(*(unsigned __int64 *)(v_rsp - 184 - 104), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 184 - 96) + 56), *(unsigned __int64 *)(v_rsp - 184 - 96));
        result = PnpUnlockDeviceActionQueue(*(unsigned __int64 *)(v_rsp - 184 - 104), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 184 - 96) + 56), *(unsigned __int64 *)(v_rsp - 184 - 96));
        result = PnpWaitForEmptyDeviceActionQueue(*(unsigned __int64 *)(v_rsp - 184 - 104), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 184 - 96) + 56), *(unsigned __int64 *)(v_rsp - 184 - 96));
        a4 = 0;
        v_stack_m188 = 0;
        v_stack_m190 = 0;
        a3 = 0;
        a1 = 0;
        v_stack_m198 = 0;
        a2 = a4 + 7;
        result = PnpRequestDeviceAction(a1, a2, a3, a4);
    }
    result = PnpWaitForEmptyDeviceEventQueue(a1, a2, a3, a4);
    if (sign_flag) goto loc_00C2ED1B;
    goto loc_00C2EB40;
loc_00C2ECEC:
    if (0 == v_stack_m150) {
        a2 = 0;
        a1 = 0;
        result = IopAllocateLegacyBootResources(a1, a2, a3, a4);
        result = v_rip - 5244548;
        *(unsigned __int8 *)(v_rip + 3528941) = 1;
        *(unsigned __int64 *)(v_rip + 3527718) = result;
    }
    v_r15 = (unsigned __int16)((0) + (1));
    goto loc_00C2EB1B;
loc_00C2ED1B:
    a2 = 0;
    result = HeadlessKernelAddLogEntry(a2 + 18, a2, a3, a4);
    *(unsigned int *)(v_rip + 3533729) = 33;
loc_00C2ED2F:
    goto loc_00C2F055;
loc_00C2ED39:
    result = PnpNotifyEarlyLaunchStatusUpdate(2, a2, a3, a4);
    result = PipUnloadEarlyLaunchDrivers(0, a2, a3, a4);
    v_r12 = 0;
    *(unsigned __int8 *)(v_rip + 3528868) = 1;
    v_stack_m188 = 0;
    a4 = 0;
    v_stack_m190 = 0;
    a3 = 0;
    a2 = 0;
    v_stack_m198 = 0;
    a1 = 0;
    result = PnpRequestDeviceAction(a1, a2, a3, a4);
    result = PnpWaitForDevicesToStart(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00C2ED92;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(result + 19, a2, a3, a4);
    *(unsigned int *)(v_rip + 3533632) = 34;
    goto loc_00C2ED2F;
loc_00C2ED92:
    result = IopCallBootDriverReinitializationRoutines(result + 19, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C2EDBD;
    result = PnpWaitForDevicesToStart(result + 19, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00C2EDBD;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(result + 20, a2, a3, a4);
    *(unsigned int *)(v_rip + 3533592) = 35;
    goto loc_00C2ED2F;
loc_00C2EDBD:
    a1 = 0;
    result = RamdiskInitialize(a1, 0, v_rsp - 184 - 48, a4);
    if (sign_flag) goto loc_00C2EE13;
    result = PnpWaitForDevicesToStart(a1, 0, v_rsp - 184 - 48, a4);
    if ((unsigned int)(result) != 0) goto loc_00C2EDF1;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(result + 19, a2, v_rsp - 184 - 48, a4);
    *(unsigned int *)(v_rip + 3533540) = 36;
    goto loc_00C2ED2F;
loc_00C2EDF1:
    result = RamdiskInitialize(1, 0, v_rsp - 184 - 48, a4);
    if (!sign_flag) goto loc_00C2EE13;
    *(unsigned int *)(v_rip + 3533506) = 46;
    goto loc_00C2F055;
loc_00C2EE13:
    result = VhdInitialize(0, 0, v_rsp - 184 - 48, a4);
    if (sign_flag) goto loc_00C2EE41;
    result = PnpWaitForDevicesToStart(0, 0, v_rsp - 184 - 48, a4);
    if ((unsigned int)(result) != 0) goto loc_00C2EE41;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(result + 19, a2, v_rsp - 184 - 48, a4);
    *(unsigned int *)(v_rip + 3533460) = 37;
    goto loc_00C2ED2F;
loc_00C2EE41:
    result = CimfsInitialize(0, 1, v_rsp - 184 - 48, a4);
    if (sign_flag) goto loc_00C2EE72;
    result = PnpWaitForDevicesToStart(0, 1, v_rsp - 184 - 48, a4);
    if ((unsigned int)(result) != 0) goto loc_00C2EE72;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(result + 19, a2, v_rsp - 184 - 48, a4);
    *(unsigned int *)(v_rip + 3533411) = 38;
    goto loc_00C2ED2F;
loc_00C2EE72:
    v_stack_m178 = 0;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 3952)) == 0) goto loc_00C2EEC7;
    result = CompositefsBootIsEnabled(v_stack_m178, a2, v_rsp - 184 - 48, a4);
    if (sign_flag) goto loc_00C2EE9C;
    if (v_stack_m178 == 0) goto loc_00C2EEC7;
loc_00C2EE9C:
    result = ext_ms_win_ntos_globmerger_l1_1_0_dll_CompositefsSetBootInformation(0, a2, v_rsp - 184 - 48, a4);
    if (sign_flag) {
        a4 = 0;
        a3 = (int)((unsigned int)(result));
        a2 = 1;
        v_stack_m198 = 0;
        a1 = a4 + 123;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = PnpWaitForDevicesToStart(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00C2EEE9;
    a2 = 0;
    result = HeadlessKernelAddLogEntry(result + 19, a2, a3, a4);
    *(unsigned int *)(v_rip + 3533292) = 44;
    goto loc_00C2ED2F;
loc_00C2EEE9:
    result = IopCreateArcNames(a1, a2, a3, a4);
    if (!sign_flag) goto loc_00C2EF04;
    *(unsigned int *)(v_rip + 3533265) = 39;
    goto loc_00C2F055;
loc_00C2EF04:
    a4 = 0;
    result = PnpBootDeviceWait(a1, 1, v_rip - 8046, a4);
    *(unsigned __int8 *)(v_rip + 3528403) = 1;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 132)) & (0x400ULL)) == 0) goto loc_00C2EF5D;
    result = SbpStartLanman(a1, 1, v_rip - 8046, a4);
    if (sign_flag) goto loc_00C2EF4E;
    result = SbpWaitForVmbus(a1, 1, v_rip - 8046, a4);
    if (sign_flag) goto loc_00C2EF4E;
    result = SbpAddTransportToInstance(a1, 1, v_rip - 8046, a4);
    if (!sign_flag) goto loc_00C2EF5D;
loc_00C2EF4E:
    *(unsigned int *)(v_rip + 3533176) = 40;
    goto loc_00C2F055;
loc_00C2EF5D:
    a2 = 0;
    result = CimfsInitialize(a1, a2, v_rip - 8046, a4);
    if (!sign_flag) goto loc_00C2EF7A;
    *(unsigned int *)(v_rip + 3533147) = 41;
    goto loc_00C2F055;
loc_00C2EF7A:
    result = VhdAutoAttachVirtualDisks(a1, a2, v_rip - 8046, a4);
    result = PipWaitCriticalDevices(a1, a2, v_rip - 8046, a4);
    if (!sign_flag) goto loc_00C2EF9A;
    *(unsigned int *)(v_rip + 3533115) = 42;
    goto loc_00C2F055;
loc_00C2EF9A:
    result = PiCreateDriverDataDirectoryRoot(a1, a2, v_rip - 8046, a4);
    if (!sign_flag) goto loc_00C2EFB2;
    *(unsigned int *)(v_rip + 3533091) = 43;
    goto loc_00C2F055;
loc_00C2EFB2:
    *(unsigned __int16 *)(v_rsp - 184) = 0;
    result = PipHardwareConfigGetIndex(a1, v_stack_m15C, v_rip - 8046, a4);
    v_r13 = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        result = v_stack_m15C;
        a1 = v_rsp - 184;
        v_stack_m188 = (unsigned int)(result);
        a4 = 0;
        result = v_rip + 307634;
        a3 = 0;
        v_stack_m190 = result;
        v_stack_m198 = 0x800ULL;
        a2 = a4 + 64;
        result = RtlStringCchPrintfExW(a1, a2, a3, a4);
        v_r13 = (unsigned int)(result);
    }
    v_r15 = 0;
    if ((*(unsigned int *)(v_rip + 3530652)) <= 0) goto loc_00C2F02D;
loc_00C2F006:
    a2 = (0) << (4);
    a2 = (a2) + (*(unsigned __int64 *)(v_rip + 3530643));
    if ((*(unsigned __int64 *)(a2)) != a2) goto loc_00C2F086;
    v_r12 = (unsigned __int16)((v_r12) + (1));
    if (((unsigned int)((unsigned __int16)(v_r12))) < (*(unsigned int *)(v_rip + 3530613))) goto loc_00C2F006;
loc_00C2F02D:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rip + 3530612), a2, a3, a4);
    a3 = 0;
    *(unsigned __int8 *)(v_rip + 2322943) = 1;
    a2 = 0;
    result = PnpDiagnosticTrace(v_rip - 12616270, a2, a3, a4);
    result = 0;
loc_00C2F055:
    a1 = (*(unsigned __int64 *)(v_rsp - 184 + 128)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
loc_00C2F086:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 8)) != 0) goto loc_00C2F28A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56)) + 8)) != (*(unsigned __int64 *)(v_stack_m28 + 56))) goto loc_00C2F28A;
    *(unsigned __int64 *)(a2) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56)) + 8) = 0;
    if (sign_flag) goto loc_00C2F24D;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 46)) != 0) goto loc_00C2F24D;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16) + 8)) != 0) goto loc_00C2F24D;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16) + 48) + 8)) == 0) goto loc_00C2F24D;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16) + 16)) & (0x408ULL)) != 0) goto loc_00C2F24D;
    a3 = 0;
    result = IopGetRegistryValue(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 32), v_rip + 305277, a3, v_stack_m130);
    if (sign_flag) goto loc_00C2F24D;
    if ((*(unsigned int *)(v_stack_m130 + 4)) != 4) goto loc_00C2F23D;
    if ((*(unsigned int *)(v_stack_m130 + 12)) < 4) goto loc_00C2F23D;
    v_stack_m138 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_m130 + 8)) + v_stack_m130 * 1)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_m130 + 8)) + v_stack_m130 * 1))) != 0) goto loc_00C2F23D;
    v_stack_m138 = 3;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16) + 48)) + (24);
    result = PiCreateDriverRedirectedStateKey(a1, v_rip + 305277, v_stack_m118, v_stack_m130);
    if (!sign_flag) goto loc_00C2F158;
    v_stack_m118 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 32);
    goto loc_00C2F15D;
loc_00C2F158:
loc_00C2F15D:
    v_stack_m158 = 0;
    v_stack_m160 = v_stack_m120;
    a4 = 0;
    v_stack_m168 = 0;
    v_stack_m170 = 2;
    result = PnpCtxRegCreateKey(*(unsigned __int64 *)(v_rip + 2322996), v_stack_m118, v_rip + 307243, a4);
    if (sign_flag) goto loc_00C2F22A;
    v_stack_m168 = 4;
    v_stack_m170 = v_stack_m138;
    result = PnpCtxRegSetValue(*(unsigned __int64 *)(v_rip + 2322996), v_stack_m120, v_rsp - 184, 4);
    result = PnpCtxRegCloseKey(*(unsigned __int64 *)(v_rip + 2322996), v_stack_m120, v_rsp - 184, 4);
    v_stack_m120 = 0;
    if (((*(unsigned __int8 *)(v_rip + 2887517)) & (2)) == 0) goto loc_00C2F22A;
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16) + 48)) + (24);
    v_stack_m140 = 0;
    a2 = 0;
    result = PnpUnicodeStringToWstr(v_stack_m140, a2, a3, 4);
    if (sign_flag) goto loc_00C2F22A;
    if (((*(unsigned __int8 *)(v_rip + 2887474)) & (2)) != 0) {
        result = v_stack_m138;
        a4 = v_stack_m134;
        v_stack_m168 = (unsigned int)(result);
        v_stack_m170 = v_stack_m140;
        result = McTemplateK0dzd_EtwWriteTransfer(v_stack_m140, a2, a3, a4);
    }
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16) + 48)) + (24);
    result = PnpUnicodeStringToWstrFree(v_stack_m140, a2, a3, a4);
    v_r15 = 0;
loc_00C2F22A:
    if (v_stack_m118 != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 32))) {
        a1 = v_stack_m118;
        result = ZwClose(a1, a2, a3, a4);
        v_stack_m118 = 0;
    }
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m130, a2, a3, a4);
loc_00C2F24D:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16) != 0) {
        a2 = 0x746C6644ULL;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 16);
        result = ObfDereferenceObjectWithTag(a1, a2, a3, a4);
    }
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 46)) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 24);
        a2 = *(unsigned __int64 *)(result + 48);
    }
    result = ZwClose(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 32), a2, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m28 + 56), a2, a3, a4);
    goto loc_00C2F006;
loc_00C2F28A:
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopInitializeBootDrivers(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m130;
    uint32_t v_stack_m134;
    uint32_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint32_t v_stack_m15C;
    uint32_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint8_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint32_t v_stack_m190;
    uint32_t v_stack_m198;
    uint64_t v_stack_m28;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (400);
    result = (*(uint64_t *)(v_rip + 0x1DC01F)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0xB8 + 0x80) = result;
    local_r12 = 0;
    *(uint32_t *)(local_rsp - 0xB8 - 0x6C) = 0;
    v_stack_m15C = 0;
    result = 0;
    v_stack_m170 = 0;
    v_stack_m158 = 0;
    Arg3 = 0;
    *(uint32_t *)(local_rsp - 0xB8 - 0x7C) = 0;
    Arg2 = 0;
    *(uint32_t *)(local_rsp - 0xB8 - 0x4C) = 0;
    *(uint64_t *)(local_rsp - 0xB8 - 0x18) = v_xmm0;
    v_stack_m140 = 0;
    *(uint64_t *)(local_rsp - 0xB8 - 0x40) = v_xmm0;
    v_stack_m148 = 0;
    v_stack_m160 = 0;
    *(uint64_t *)(local_rsp - 0xB8 - 0x60) = v_xmm0;
    *(uint32_t *)(local_rsp - 0xB8 - 0x20) = 0;
    *(uint64_t *)(local_rsp - 0xB8 - 0x30) = v_xmm1;
    v_stack_m168 = 0;
    result = PnpDiagnosticTrace(v_rip - 12612542, Arg2, Arg3, a4);
    *(uint32_t *)(v_rip + 0x3D9EE7) = 3;
    *(uint64_t *)(local_rsp - 0xB8 - 0x78) = v_rip + 309437;
    *(uint32_t *)(local_rsp - 0xB8 - 0x80) = 0x80007EULL;
    Arg2 = 0;
    result = IopOpenRegistryKeyEx(v_stack_m170, Arg2, local_rsp - 184 - 128, (uint32_t)((uint32_t)((uint32_t)(0x20019ULL))));
    if (!sign_flag) goto loc_00C2E7ED;
    *(uint32_t *)(local_rsp - 0xB8 - 0x80) = 0x7E007CULL;
    *(uint64_t *)(local_rsp - 0xB8 - 0x78) = v_rip + 309509;
    Arg2 = 0;
    result = IopOpenRegistryKeyEx(v_stack_m170, Arg2, local_rsp - 184 - 128, (uint32_t)((uint32_t)((uint32_t)(0x20019ULL))));
    if (sign_flag) goto loc_00C2E841;
loc_00C2E7ED:
    Arg3 = 0;
    result = IopGetRegistryValue(v_stack_m170, v_rip + 309583, Arg3, v_stack_m158);
    result = ZwClose(v_stack_m170, v_rip + 309583, Arg3, v_stack_m158);
    if (sign_flag) goto loc_00C2E841;
    if ((*(uint32_t *)(v_stack_m158 + 0x4)) != 4) goto loc_00C2E837;
    if ((*(uint32_t *)(v_stack_m158 + 0xC)) >= 4) {
        result = *(uint32_t *)(v_stack_m158 + 0x8);
        Arg1 = *(uint32_t *)(result + v_stack_m158 * 1);
        *(uint32_t *)(v_rip + 0x3D9E4D) = (uint32_t)(Arg1);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m158, Arg2, v_stack_m158, v_stack_m158);
loc_00C2E841:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3D9E3D)))) != 8) goto loc_00C2E855;
    *(uint32_t *)(v_rip + 0x3D9E31) = 0;
    goto loc_00C2E866;
loc_00C2E855:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3D9E3D)))) & (0xFFFFFFF8ULL)) != 0) {
        *(uint32_t *)(v_rip + 0x3D9E1E) = 3;
    }
    result = PipInitializeCoreDriversAndElam(Arg1, Arg2, v_stack_m158, v_stack_m158);
    *(uint32_t *)(local_rsp - 0xB8 - 0x50) = 0x20001EULL;
    *(uint64_t *)(local_rsp - 0xB8 - 0x48) = v_rip + 309627;
    *(uint32_t *)(local_rsp - 0xB8 - 0x70) = 0x20000ULL;
    *(uint64_t *)(local_rsp - 0xB8 - 0x68) = v_rip + 309634;
    v_stack_m180 = v_stack_m168;
    v_stack_m190 = 0;
    a4 = 0;
    v_stack_m198 = 0;
    result = PnpInitializeBootStartDriver(local_rsp - 184 - 80, local_rsp - 184 - 112, v_rip + 100361, a4);
    v_stack_m168 = v_stack_m168;
    if (v_stack_m168 != 0) goto loc_00C2E8E3;
    *(uint32_t *)(v_rip + 0x35EFF2) = (uint32_t)(32 - 2);
    goto loc_00C2F055;
loc_00C2E8E3:
    Arg1 = 0;
    result = PpInitGetGroupOrderIndex(Arg1, local_rsp - 184 - 112, v_rip + 100361, a4);
    *(uint32_t *)(v_rip + 0x35E6A7) = (uint32_t)((uint16_t)(result));
    v_stack_m150 = (uint32_t)((uint32_t)(0xFFFFULL));
    if (((uint32_t)((uint16_t)(result))) != ((uint32_t)((uint32_t)(0xFFFFULL)))) goto loc_00C2E921;
    Arg2 = 0;
    result = HeadlessKernelAddLogEntry(Arg2 + 16, Arg2, v_rip + 100361, a4);
    *(uint32_t *)(v_rip + 0x35EFB4) = 31;
    goto loc_00C2F055;
loc_00C2E921:
    Arg2 = ((uint32_t)(0xC0000225ULL)) << (4);
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x6E697050ULL), a4);
    *(uint64_t *)(v_rip + 0x35E669) = result;
    if (result != 0) goto loc_00C2E95F;
    result = HeadlessKernelAddLogEntry(result + 17, result, (uint32_t)(0x6E697050ULL), a4);
    *(uint32_t *)(v_rip + 0x35EF76) = 32;
    goto loc_00C2F055;
loc_00C2E95F:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x35E63A))) == 0) goto loc_00C2E992;
loc_00C2E975:
    Arg1 = (uint16_t)((0) + (1));
    result = (0) << (4);
    result = (result) + (result);
    *(uint64_t *)(result + 0x8) = result;
    *(uint64_t *)(result) = result;
    if (((uint32_t)((uint16_t)(Arg1))) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x35E63A))))) goto loc_00C2E975;
loc_00C2E992:
    result = PipInitializeDriverDependentDLLs((uint32_t)((uint32_t)(32 - 30)), Arg1, (uint32_t)(*(uint32_t *)(v_rip + 0x35E63A)), a4);
    result = RtlInitUnicodeString(local_rsp - 184 - 96, v_rip + 309372, (uint32_t)(*(uint32_t *)(v_rip + 0x35E63A)), a4);
    result = RtlInitUnicodeString(local_rsp - 184 - 24, v_rip + 309388, (uint32_t)(*(uint32_t *)(v_rip + 0x35E63A)), a4);
    if (0 >= (*(uint16_t *)(v_rip + 0x23788B))) goto loc_00C2EA2F;
loc_00C2E9D2:
    local_r14 = (0) << (4);
    Arg1 = (*(uint64_t *)(v_rip + 0x23786F)) + (local_r14);
    result = RtlCompareUnicodeString(Arg1, local_rsp - 184 - 96, 1, a4);
    if ((uint32_t)(result) == 0) goto loc_00C2EA13;
    Arg1 = (*(uint64_t *)(v_rip + 0x23784D)) + (local_r14);
    result = RtlCompareUnicodeString(Arg1, local_rsp - 184 - 24, 1, a4);
    if ((uint32_t)(result) != 0) goto loc_00C2EA17;
    v_stack_m150 = 0;
loc_00C2EA13:
    local_rbx = (uint16_t)((0) + (1));
loc_00C2EA17:
    if (((uint16_t)(local_rbx)) >= ((uint16_t)((uint32_t)((uint32_t)(32 - 30))))) goto loc_00C2EA2A;
    local_rdi = (uint16_t)((0) + (1));
    if (((uint16_t)(local_rdi)) < (*(uint16_t *)(v_rip + 0x237828))) goto loc_00C2E9D2;
loc_00C2EA2A:
loc_00C2EA2F:
    goto loc_00C2EB00;
loc_00C2EA3B:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x30) + 0x38)) < 0) goto loc_00C2EB00;
    result = ExAllocatePool2(256, 48, (uint32_t)(0x6E697050ULL), a4);
    if (result == 0) goto loc_00C2EB00;
    *(uint64_t *)(result + 0x8) = result;
    *(uint64_t *)(result) = result;
    Arg2 = 0;
    *(uint64_t *)(result + 0x18) = *(uint64_t *)(arg1 + 0x30);
    result = IopOpenRegistryKeyEx(v_stack_m170, Arg2, *(uint64_t *)(arg1 + 0x30) + 32, (uint32_t)(0x20019ULL));
    if (!sign_flag) goto loc_00C2EA9D;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, *(uint64_t *)(arg1 + 0x30) + 32, (uint32_t)(0x20019ULL));
    goto loc_00C2EB00;
loc_00C2EA9D:
    *(uint64_t *)(result + 0x20) = v_stack_m170;
    result = PpInitGetGroupOrderIndex(v_stack_m170, Arg2, *(uint64_t *)(arg1 + 0x30) + 32, (uint32_t)(0x20019ULL));
    result = PipGetDriverTagPriority(v_stack_m170, Arg2, *(uint64_t *)(arg1 + 0x30) + 32, (uint32_t)(0x20019ULL));
    *(uint16_t *)(result + 0x2C) = (uint16_t)(result);
    Arg2 = ((uint32_t)((uint32_t)((uint16_t)(result)))) << (4);
    Arg2 = (Arg2) + (*(uint64_t *)(v_rip + 0x35E4DA));
    goto loc_00C2EADC;
loc_00C2EAD3:
    if ((*(uint16_t *)(*(uint64_t *)(Arg2) + 0x2C)) > ((uint16_t)(result))) goto loc_00C2EAE1;
loc_00C2EADC:
    if ((*(uint64_t *)(*(uint64_t *)(Arg2))) != Arg2) goto loc_00C2EAD3;
loc_00C2EAE1:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2)) + 0x8)) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2)) + 0x8))) goto loc_00C2F28A;
    *(uint64_t *)(result) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2)) + 0x8));
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2)) + 0x8);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2)) + 0x8)) + 0x8) = result;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2)) + 0x8)) = result;
loc_00C2EB00:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x30))) != (Arg1 + 48)) goto loc_00C2EA3B;
    result = PnpNotifyEarlyLaunchStatusUpdate(1, Arg2, *(uint64_t *)(arg1 + 0x30) + 32, (uint32_t)(0x20019ULL));
loc_00C2EB1B:
    if (0 >= (*(uint32_t *)(v_rip + 0x35E47B))) goto loc_00C2ED39;
    local_r12 = (0) << (4);
    local_rdi = 0;
loc_00C2EB40:
    Arg1 = (*(uint64_t *)(v_rip + 0x35E461)) + (local_r12);
    if ((*(uint64_t *)(local_r12 + *(uint64_t *)(v_rip + 0x35E476) * 1)) == Arg1) goto loc_00C2ECEC;
    v_stack_m170 = *(uint64_t *)(*(uint64_t *)(local_r12 + *(uint64_t *)(v_rip + 0x35E476) * 1) + 0x20);
    v_stack_m168 = *(uint64_t *)(*(uint64_t *)(local_r12 + *(uint64_t *)(v_rip + 0x35E476) * 1) + 0x18);
    *(uint8_t *)(*(uint64_t *)(local_r12 + *(uint64_t *)(v_rip + 0x35E476) * 1) + 0x2F) = 1;
    *(uint64_t *)(local_rsp - 0xB8 - 0x60) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r12 + *(uint64_t *)(v_rip + 0x35E476) * 1) + 0x18) + 0x30);
    result = IopGetDriverNameFromKeyNode(v_stack_m170, local_rsp - 184 - 112, *(uint64_t *)(arg1 + 0x30) + 32, (uint32_t)(0x20019ULL));
    if (!sign_flag) goto loc_00C2EB92;
    *(uint8_t *)(*(uint64_t *)(local_r12 + *(uint64_t *)(v_rip + 0x35E476) * 1) + 0x2E) = 1;
    goto loc_00C2EC94;
loc_00C2EB92:
    Arg3 = 0;
    result = IopGetRegistryValue(v_stack_m170, v_rip + 308698, Arg3, v_stack_m158);
    if (sign_flag) goto loc_00C2EBF2;
    if ((*(uint32_t *)(v_stack_m158 + 0xC)) != 0) {
        result = *(uint16_t *)(v_stack_m158 + 0xC);
        Arg1 = local_rsp - 184 - 64;
        *(uint16_t *)(local_rsp - 0xB8 - 0x40) = (uint16_t)(result);
        Arg2 = 1;
        *(uint16_t *)(local_rsp - 0xB8 - 0x3E) = (uint16_t)(result);
        result = *(uint32_t *)(v_stack_m158 + 0x8);
        result = (result) + (v_stack_m158);
        *(uint64_t *)(local_rsp - 0xB8 - 0x38) = result;
        result = PipLookupGroupName(Arg1, Arg2, Arg3, v_stack_m158);
        local_rdi = result;
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m158, Arg2, Arg3, v_stack_m158);
loc_00C2EBF2:
    local_r13 = 0;
    result = PipCheckDependencies(v_stack_m170, Arg2, Arg3, v_stack_m158);
    if ((uint32_t)(result) == 0) goto loc_00C2EC7D;
    v_stack_m168 = *(uint64_t *)(*(uint64_t *)(local_r12 + *(uint64_t *)(v_rip + 0x35E476) * 1) + 0x10);
    if (*(uint64_t *)(*(uint64_t *)(local_r12 + *(uint64_t *)(v_rip + 0x35E476) * 1) + 0x10) != 0) goto loc_00C2EC63;
    if ((*(uint8_t *)(*(uint64_t *)(local_r12 + *(uint64_t *)(v_rip + 0x35E476) * 1) + 0x2E)) != ((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_r12 + *(uint64_t *)(v_rip + 0x35E476) * 1) + 0x10)))) goto loc_00C2EC63;
    v_stack_m180 = v_stack_m168;
    v_stack_m190 = (uint32_t)(*(uint64_t *)(*(uint64_t *)(local_r12 + *(uint64_t *)(v_rip + 0x35E476) * 1) + 0x10) + 1);
    result = PnpInitializeBootStartDriver(local_rsp - 184 - 112, v_stack_m168 + 32, *(uint64_t *)(*(uint64_t *)(local_rsp - 0xB8 - 0x60) + 0x38), *(uint64_t *)(local_rsp - 0xB8 - 0x60));
    *(uint32_t *)(*(uint64_t *)(local_r12 + *(uint64_t *)(v_rip + 0x35E476) * 1) + 0x28) = (uint32_t)(result);
    if (v_stack_m168 == 0) goto loc_00C2EC83;
    result = ObfReferenceObjectWithTag(v_stack_m168, (uint32_t)(0x746C6644ULL), *(uint64_t *)(*(uint64_t *)(local_rsp - 0xB8 - 0x60) + 0x38), *(uint64_t *)(local_rsp - 0xB8 - 0x60));
    goto loc_00C2EC69;
loc_00C2EC63:
loc_00C2EC69:
    if (v_stack_m168 == 0) goto loc_00C2EC83;
    if (local_rdi != 0) {
    }
    *(uint64_t *)(*(uint64_t *)(local_r12 + *(uint64_t *)(v_rip + 0x35E476) * 1) + 0x10) = v_stack_m168;
    goto loc_00C2EC87;
loc_00C2EC7D:
loc_00C2EC83:
    *(uint8_t *)(*(uint64_t *)(local_r12 + *(uint64_t *)(v_rip + 0x35E476) * 1) + 0x2E) = 1;
loc_00C2EC87:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0xB8 - 0x68), Arg2, *(uint64_t *)(*(uint64_t *)(local_rsp - 0xB8 - 0x60) + 0x38), *(uint64_t *)(local_rsp - 0xB8 - 0x60));
    local_rdi = 0;
loc_00C2EC94:
    if ((*(uint8_t *)(*(uint64_t *)(local_r12 + *(uint64_t *)(v_rip + 0x35E476) * 1) + 0x2E)) == 0) {
        result = PnpLockDeviceActionQueue(*(uint64_t *)(local_rsp - 0xB8 - 0x68), Arg2, *(uint64_t *)(*(uint64_t *)(local_rsp - 0xB8 - 0x60) + 0x38), *(uint64_t *)(local_rsp - 0xB8 - 0x60));
        Arg2 = *(uint64_t *)(v_stack_m168 + 0x30);
        Arg2 = (Arg2) + (24);
        v_stack_m190 = v_stack_m168;
        result = PipApplyFunctionToServiceInstances(*(uint64_t *)(local_rsp - 0xB8 - 0x68), Arg2, *(uint64_t *)(*(uint64_t *)(local_rsp - 0xB8 - 0x60) + 0x38), *(uint64_t *)(local_rsp - 0xB8 - 0x60));
        result = PnpUnlockDeviceActionQueue(*(uint64_t *)(local_rsp - 0xB8 - 0x68), Arg2, *(uint64_t *)(*(uint64_t *)(local_rsp - 0xB8 - 0x60) + 0x38), *(uint64_t *)(local_rsp - 0xB8 - 0x60));
        result = PnpWaitForEmptyDeviceActionQueue(*(uint64_t *)(local_rsp - 0xB8 - 0x68), Arg2, *(uint64_t *)(*(uint64_t *)(local_rsp - 0xB8 - 0x60) + 0x38), *(uint64_t *)(local_rsp - 0xB8 - 0x60));
        a4 = 0;
        v_stack_m188 = 0;
        v_stack_m190 = 0;
        Arg3 = 0;
        Arg1 = 0;
        v_stack_m198 = 0;
        Arg2 = a4 + 7;
        result = PnpRequestDeviceAction(Arg1, Arg2, Arg3, a4);
    }
    result = PnpWaitForEmptyDeviceEventQueue(Arg1, Arg2, Arg3, a4);
    if (sign_flag) goto loc_00C2ED1B;
    goto loc_00C2EB40;
loc_00C2ECEC:
    if (0 == v_stack_m150) {
        Arg2 = 0;
        Arg1 = 0;
        result = IopAllocateLegacyBootResources(Arg1, Arg2, Arg3, a4);
        result = v_rip - 5244548;
        *(uint8_t *)(v_rip + 0x35D8ED) = 1;
        *(uint64_t *)(v_rip + 0x35D426) = result;
    }
    local_r15 = (uint16_t)((0) + (1));
    goto loc_00C2EB1B;
loc_00C2ED1B:
    Arg2 = 0;
    result = HeadlessKernelAddLogEntry(Arg2 + 18, Arg2, Arg3, a4);
    *(uint32_t *)(v_rip + 0x35EBA1) = 33;
loc_00C2ED2F:
    goto loc_00C2F055;
loc_00C2ED39:
    result = PnpNotifyEarlyLaunchStatusUpdate(2, Arg2, Arg3, a4);
    result = PipUnloadEarlyLaunchDrivers(0, Arg2, Arg3, a4);
    local_r12 = 0;
    *(uint8_t *)(v_rip + 0x35D8A4) = 1;
    v_stack_m188 = 0;
    a4 = 0;
    v_stack_m190 = 0;
    Arg3 = 0;
    Arg2 = 0;
    v_stack_m198 = 0;
    Arg1 = 0;
    result = PnpRequestDeviceAction(Arg1, Arg2, Arg3, a4);
    result = PnpWaitForDevicesToStart(Arg1, Arg2, Arg3, a4);
    if ((uint32_t)(result) != 0) goto loc_00C2ED92;
    Arg2 = 0;
    result = HeadlessKernelAddLogEntry(result + 19, Arg2, Arg3, a4);
    *(uint32_t *)(v_rip + 0x35EB40) = 34;
    goto loc_00C2ED2F;
loc_00C2ED92:
    result = IopCallBootDriverReinitializationRoutines(result + 19, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C2EDBD;
    result = PnpWaitForDevicesToStart(result + 19, Arg2, Arg3, a4);
    if ((uint32_t)(result) != 0) goto loc_00C2EDBD;
    Arg2 = 0;
    result = HeadlessKernelAddLogEntry(result + 20, Arg2, Arg3, a4);
    *(uint32_t *)(v_rip + 0x35EB18) = 35;
    goto loc_00C2ED2F;
loc_00C2EDBD:
    Arg1 = 0;
    result = RamdiskInitialize(Arg1, 0, local_rsp - 184 - 48, a4);
    if (sign_flag) goto loc_00C2EE13;
    result = PnpWaitForDevicesToStart(Arg1, 0, local_rsp - 184 - 48, a4);
    if ((uint32_t)(result) != 0) goto loc_00C2EDF1;
    Arg2 = 0;
    result = HeadlessKernelAddLogEntry(result + 19, Arg2, local_rsp - 184 - 48, a4);
    *(uint32_t *)(v_rip + 0x35EAE4) = 36;
    goto loc_00C2ED2F;
loc_00C2EDF1:
    result = RamdiskInitialize(1, 0, local_rsp - 184 - 48, a4);
    if (!sign_flag) goto loc_00C2EE13;
    *(uint32_t *)(v_rip + 0x35EAC2) = 46;
    goto loc_00C2F055;
loc_00C2EE13:
    result = VhdInitialize(0, 0, local_rsp - 184 - 48, a4);
    if (sign_flag) goto loc_00C2EE41;
    result = PnpWaitForDevicesToStart(0, 0, local_rsp - 184 - 48, a4);
    if ((uint32_t)(result) != 0) goto loc_00C2EE41;
    Arg2 = 0;
    result = HeadlessKernelAddLogEntry(result + 19, Arg2, local_rsp - 184 - 48, a4);
    *(uint32_t *)(v_rip + 0x35EA94) = 37;
    goto loc_00C2ED2F;
loc_00C2EE41:
    result = CimfsInitialize(0, 1, local_rsp - 184 - 48, a4);
    if (sign_flag) goto loc_00C2EE72;
    result = PnpWaitForDevicesToStart(0, 1, local_rsp - 184 - 48, a4);
    if ((uint32_t)(result) != 0) goto loc_00C2EE72;
    Arg2 = 0;
    result = HeadlessKernelAddLogEntry(result + 19, Arg2, local_rsp - 184 - 48, a4);
    *(uint32_t *)(v_rip + 0x35EA63) = 38;
    goto loc_00C2ED2F;
loc_00C2EE72:
    v_stack_m178 = 0;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xF70)) == 0) goto loc_00C2EEC7;
    result = CompositefsBootIsEnabled(v_stack_m178, Arg2, local_rsp - 184 - 48, a4);
    if (sign_flag) goto loc_00C2EE9C;
    if (v_stack_m178 == 0) goto loc_00C2EEC7;
loc_00C2EE9C:
    result = kernel_indirect_call(0, Arg2, local_rsp - 184 - 48, a4);
    if (sign_flag) {
        a4 = 0;
        Arg3 = (int32_t)((uint32_t)(result));
        Arg2 = 1;
        v_stack_m198 = 0;
        Arg1 = a4 + 123;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, a4);
    }
    result = PnpWaitForDevicesToStart(Arg1, Arg2, Arg3, a4);
    if ((uint32_t)(result) != 0) goto loc_00C2EEE9;
    Arg2 = 0;
    result = HeadlessKernelAddLogEntry(result + 19, Arg2, Arg3, a4);
    *(uint32_t *)(v_rip + 0x35E9EC) = 44;
    goto loc_00C2ED2F;
loc_00C2EEE9:
    result = IopCreateArcNames(Arg1, Arg2, Arg3, a4);
    if (!sign_flag) goto loc_00C2EF04;
    *(uint32_t *)(v_rip + 0x35E9D1) = 39;
    goto loc_00C2F055;
loc_00C2EF04:
    a4 = 0;
    result = PnpBootDeviceWait(Arg1, 1, v_rip - 8046, a4);
    *(uint8_t *)(v_rip + 0x35D6D3) = 1;
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x84)) & (0x400ULL)) == 0) goto loc_00C2EF5D;
    result = SbpStartLanman(Arg1, 1, v_rip - 8046, a4);
    if (sign_flag) goto loc_00C2EF4E;
    result = SbpWaitForVmbus(Arg1, 1, v_rip - 8046, a4);
    if (sign_flag) goto loc_00C2EF4E;
    result = SbpAddTransportToInstance(Arg1, 1, v_rip - 8046, a4);
    if (!sign_flag) goto loc_00C2EF5D;
loc_00C2EF4E:
    *(uint32_t *)(v_rip + 0x35E978) = 40;
    goto loc_00C2F055;
loc_00C2EF5D:
    Arg2 = 0;
    result = CimfsInitialize(Arg1, Arg2, v_rip - 8046, a4);
    if (!sign_flag) goto loc_00C2EF7A;
    *(uint32_t *)(v_rip + 0x35E95B) = 41;
    goto loc_00C2F055;
loc_00C2EF7A:
    result = VhdAutoAttachVirtualDisks(Arg1, Arg2, v_rip - 8046, a4);
    result = PipWaitCriticalDevices(Arg1, Arg2, v_rip - 8046, a4);
    if (!sign_flag) goto loc_00C2EF9A;
    *(uint32_t *)(v_rip + 0x35E93B) = 42;
    goto loc_00C2F055;
loc_00C2EF9A:
    result = PiCreateDriverDataDirectoryRoot(Arg1, Arg2, v_rip - 8046, a4);
    if (!sign_flag) goto loc_00C2EFB2;
    *(uint32_t *)(v_rip + 0x35E923) = 43;
    goto loc_00C2F055;
loc_00C2EFB2:
    *(uint16_t *)(local_rsp - 0xB8) = 0;
    result = PipHardwareConfigGetIndex(Arg1, v_stack_m15C, v_rip - 8046, a4);
    local_r13 = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        result = v_stack_m15C;
        Arg1 = local_rsp - 184;
        v_stack_m188 = (uint32_t)(result);
        a4 = 0;
        result = v_rip + 307634;
        Arg3 = 0;
        v_stack_m190 = result;
        v_stack_m198 = 0x800ULL;
        Arg2 = a4 + 64;
        result = RtlStringCchPrintfExW(Arg1, Arg2, Arg3, a4);
        local_r13 = (uint32_t)(result);
    }
    local_r15 = 0;
    if ((*(uint32_t *)(v_rip + 0x35DF9C)) <= 0) goto loc_00C2F02D;
loc_00C2F006:
    Arg2 = (0) << (4);
    Arg2 = (Arg2) + (*(uint64_t *)(v_rip + 0x35DF93));
    if ((*(uint64_t *)(Arg2)) != Arg2) goto loc_00C2F086;
    local_r12 = (uint16_t)((local_r12) + (1));
    if (((uint32_t)((uint16_t)(local_r12))) < (*(uint32_t *)(v_rip + 0x35DF75))) goto loc_00C2F006;
loc_00C2F02D:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_rip + 0x35DF74), Arg2, Arg3, a4);
    Arg3 = 0;
    *(uint8_t *)(v_rip + 0x2371FF) = 1;
    Arg2 = 0;
    result = PnpDiagnosticTrace(v_rip - 12616270, Arg2, Arg3, a4);
    result = 0;
loc_00C2F055:
    Arg1 = (*(uint64_t *)(local_rsp - 0xB8 + 0x80)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    return result;
loc_00C2F086:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x8)) != 0) goto loc_00C2F28A;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38)) + 0x8)) != (*(uint64_t *)(v_stack_m28 + 0x38))) goto loc_00C2F28A;
    *(uint64_t *)(Arg2) = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38)) + 0x8) = 0;
    if (sign_flag) goto loc_00C2F24D;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x2E)) != 0) goto loc_00C2F24D;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10) + 0x8)) != 0) goto loc_00C2F24D;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10) + 0x30) + 0x8)) == 0) goto loc_00C2F24D;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10) + 0x10)) & (0x408ULL)) != 0) goto loc_00C2F24D;
    Arg3 = 0;
    result = IopGetRegistryValue(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x20), v_rip + 305277, Arg3, v_stack_m130);
    if (sign_flag) goto loc_00C2F24D;
    if ((*(uint32_t *)(v_stack_m130 + 0x4)) != 4) goto loc_00C2F23D;
    if ((*(uint32_t *)(v_stack_m130 + 0xC)) < 4) goto loc_00C2F23D;
    v_stack_m138 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_m130 + 0x8)) + v_stack_m130 * 1)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_m130 + 0x8)) + v_stack_m130 * 1))) != 0) goto loc_00C2F23D;
    v_stack_m138 = 3;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10) + 0x30)) + (24);
    result = PiCreateDriverRedirectedStateKey(Arg1, v_rip + 305277, v_stack_m118, v_stack_m130);
    if (!sign_flag) goto loc_00C2F158;
    v_stack_m118 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x20);
    goto loc_00C2F15D;
loc_00C2F158:
loc_00C2F15D:
    v_stack_m158 = 0;
    v_stack_m160 = v_stack_m120;
    a4 = 0;
    v_stack_m168 = 0;
    v_stack_m170 = 2;
    result = PnpCtxRegCreateKey(*(uint64_t *)(v_rip + 0x237234), v_stack_m118, v_rip + 307243, a4);
    if (sign_flag) goto loc_00C2F22A;
    v_stack_m168 = 4;
    v_stack_m170 = v_stack_m138;
    result = PnpCtxRegSetValue(*(uint64_t *)(v_rip + 0x237234), v_stack_m120, local_rsp - 184, 4);
    result = PnpCtxRegCloseKey(*(uint64_t *)(v_rip + 0x237234), v_stack_m120, local_rsp - 184, 4);
    v_stack_m120 = 0;
    if (((*(uint8_t *)(v_rip + 0x2C0F5D)) & (2)) == 0) goto loc_00C2F22A;
    Arg3 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10) + 0x30)) + (24);
    v_stack_m140 = 0;
    Arg2 = 0;
    result = PnpUnicodeStringToWstr(v_stack_m140, Arg2, Arg3, 4);
    if (sign_flag) goto loc_00C2F22A;
    if (((*(uint8_t *)(v_rip + 0x2C0F32)) & (2)) != 0) {
        result = v_stack_m138;
        a4 = v_stack_m134;
        v_stack_m168 = (uint32_t)(result);
        v_stack_m170 = v_stack_m140;
        result = McTemplateK0dzd_EtwWriteTransfer(v_stack_m140, Arg2, Arg3, a4);
    }
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10) + 0x30)) + (24);
    result = PnpUnicodeStringToWstrFree(v_stack_m140, Arg2, Arg3, a4);
    local_r15 = 0;
loc_00C2F22A:
    if (v_stack_m118 != (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x20))) {
        Arg1 = v_stack_m118;
        result = ZwClose(Arg1, Arg2, Arg3, a4);
        v_stack_m118 = 0;
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m130, Arg2, Arg3, a4);
loc_00C2F24D:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10) != 0) {
        Arg2 = 0x746C6644ULL;
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x10);
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, Arg3, a4);
    }
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x2E)) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x18);
        Arg2 = *(uint64_t *)(result + 0x30);
    }
    result = ZwClose(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x20), Arg2, Arg3, a4);
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m28 + 0x38), Arg2, Arg3, a4);
    goto loc_00C2F006;
loc_00C2F28A:
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0xF0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C2E6F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
