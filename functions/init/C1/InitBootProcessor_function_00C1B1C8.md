# InitBootProcessor

- RVA: `0x00C1B1C8`–`0x00C1BE9C` (길이 `3,284` bytes)
- VA: `0x0000000140C1B1C8`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C37F0`
- 디코드: `752`개 명령, `3,284/3,284` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **93**; 고유 호출 대상: **65**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **97**

### Outgoing calls
- `0x00C1B2C8` → [ExpInitLicensing](../../page/7C/ExpInitLicensing_function_007C85C8.md) (function, `0x007C85C8`)
- `0x00C1B2D4` → [RtlNlsInitState](../../page/78/RtlNlsInitState_function_0078BEC4.md) (function, `0x0078BEC4`)
- `0x00C1B2DB` → [VslGetNestedPageProtectionFlags](../../text/2F/VslGetNestedPageProtectionFlags_function_002F2164.md) (function, `0x002F2164`)
- `0x00C1B321` → [KeSetPagePrivilege](../../text/40/KeSetPagePrivilege_function_00407970.md) (function, `0x00407970`)
- `0x00C1B34F` → [strupr](../../text/4F/strupr_function_004FEEE0.md) (function, `0x004FEEE0`)
- `0x00C1B35E` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1B372` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1B380` → [atol](../../text/4F/atol_function_004FF8D0.md) (function, `0x004FF8D0`)
- `0x00C1B394` → [ExBurnMemory](ExBurnMemory_function_00C1AE80.md) (function, `0x00C1AE80`)
- `0x00C1B3A3` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C1B3E3` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1B400` → [ExPreInitializeNls](../../page/7C/ExPreInitializeNls_function_007CACDC.md) (function, `0x007CACDC`)
- `0x00C1B41A` → [WheaInitializeServices](../C5/WheaInitializeServices_function_00C5516C.md) (function, `0x00C5516C`)
- `0x00C1B42D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00C1B44B` → [HalInitSystem](../../pagelk/B5/HalInitSystem_function_00B5B6E0.md) (function, `0x00B5B6E0`)
- `0x00C1B459` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00C1B478` → [KeInitializeClock](../C7/KeInitializeClock_function_00C70C30.md) (function, `0x00C70C30`)
- `0x00C1B480` → [PsInitializeQuotaSystem](../C4/PsInitializeQuotaSystem_function_00C46364.md) (function, `0x00C46364`)
- `0x00C1B488` → [CmInitSystem0](../C5/CmInitSystem0_function_00C58E88.md) (function, `0x00C58E88`)
- `0x00C1B4A8` → [KeInitSystem](../C7/KeInitSystem_function_00C71660.md) (function, `0x00C71660`)
- `0x00C1B4C8` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1B576` → [LdrFindResource_U](../../page/78/LdrFindResource_U_function_0078BD20.md) (function, `0x0078BD20`)
- `0x00C1B595` → [LdrAccessResource](../../page/78/LdrAccessResource_function_0078B9E0.md) (function, `0x0078B9E0`)
- `0x00C1B62D` → [KeAdjustInterruptTime](../../text/4C/KeAdjustInterruptTime_function_004C9EB0.md) (function, `0x004C9EB0`)
- `0x00C1B634` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C1B693` → [ExInitSystem](../C5/ExInitSystem_function_00C511A8.md) (function, `0x00C511A8`)
- `0x00C1B6BA` → [IpmiHwInitializeContext](../../text/6A/IpmiHwInitializeContext_function_006A64F8.md) (function, `0x006A64F8`)
- `0x00C1B6C3` → [WheaSelLogSetNtSchedulerAvailability](../../text/65/WheaSelLogSetNtSchedulerAvailability_function_0065DB18.md) (function, `0x0065DB18`)
- `0x00C1B6F0` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (function, `0x007D6800`)
- `0x00C1B6F5` → [KeNumaInitialize](../C3/KeNumaInitialize_function_00C36E74.md) (function, `0x00C36E74`)
- `0x00C1B6FD` → [VerifierInitSystem](../C4/VerifierInitSystem_function_00C4BC84.md) (function, `0x00C4BC84`)
- `0x00C1B702` → [InitializeDynamicPartitioningPolicy](InitializeDynamicPartitioningPolicy_function_00C1C2E8.md) (function, `0x00C1C2E8`)
- `0x00C1B707` → [KeInitializeXSaveStructures](../../pagelk/B6/KeInitializeXSaveStructures_function_00B66CEC.md) (function, `0x00B66CEC`)
- `0x00C1B729` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C1B74C` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C1B75D` → [MmInitSystem](../BE/MmInitSystem_function_00BEE990.md) (function, `0x00BEE990`)
- `0x00C1B764` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C1B7AC` → `symcryptk.dll!SymCryptEntropyAccumulatorInit1` (import, 간접 대상; import `symcryptk.dll!SymCryptEntropyAccumulatorInit1`)
- `0x00C1B7BD` → [EtwInitialize](../../page/7B/EtwInitialize_function_007B4D40.md) (function, `0x007B4D40`)
- `0x00C1B7CB` → [VmInitSystem](../BE/VmInitSystem_function_00BEEEB8.md) (function, `0x00BEEEB8`)
- `0x00C1B7E7` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1B7F2` → [HalInitializeBios](../../text/53/HalInitializeBios_function_0053D9A0.md) (function, `0x0053D9A0`)
- `0x00C1B7FF` → [InbvDriverInitialize](../C2/InbvDriverInitialize_function_00C2A420.md) (function, `0x00C2A420`)
- `0x00C1B820` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C1B835` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00C1B848` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C1B880` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1B89E` → [MiEnumerateSystemImages](../../text/2A/MiEnumerateSystemImages_function_002A3D40.md) (function, `0x002A3D40`)
- `0x00C1B8AF` → [DbgBreakPointWithStatus](../../text/4F/DbgBreakPointWithStatus_function_004FE4E0.md) (function, `0x004FE4E0`)
- `0x00C1B93F` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00C1B9A2` → [PsInitializeWin32kServiceTable](../C4/PsInitializeWin32kServiceTable_function_00C44C08.md) (function, `0x00C44C08`)
- `0x00C1B9A7` → [PsInitializeWin32kKernelExports](../../text/5E/PsInitializeWin32kKernelExports_function_005E2190.md) (function, `0x005E2190`)
- `0x00C1B9C5` → [MiEnumerateSystemImages](../../text/2A/MiEnumerateSystemImages_function_002A3D40.md) (function, `0x002A3D40`)
- `0x00C1B9CD` → [HvlPhase1Initialize](../../text/58/HvlPhase1Initialize_function_00583D80.md) (function, `0x00583D80`)
- `0x00C1B9E4` → [HeadlessInit](../C5/HeadlessInit_function_00C52C28.md) (function, `0x00C52C28`)
- `0x00C1B9EC` → [BootApplicationPersistentDataInitialize](../C5/BootApplicationPersistentDataInitialize_function_00C50DD8.md) (function, `0x00C50DD8`)
- `0x00C1BA41` → [RtlFindMessage](../../page/99/RtlFindMessage_function_0099B220.md) (function, `0x0099B220`)
- `0x00C1BA5C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1BA6F` → [RtlInitAnsiString](../../text/47/RtlInitAnsiString_function_00470F40.md) (function, `0x00470F40`)
- `0x00C1BAB2` → [RtlStringCbPrintfA](../../text/53/RtlStringCbPrintfA_function_0053BC0C.md) (function, `0x0053BC0C`)
- `0x00C1BACE` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1BAFC` → [RtlStringCbCatExA](../../text/53/RtlStringCbCatExA_function_0053BB58.md) (function, `0x0053BB58`)
- `0x00C1BB18` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1BB37` → [RtlStringCbPrintfA](../../text/53/RtlStringCbPrintfA_function_0053BC0C.md) (function, `0x0053BC0C`)
- `0x00C1BB57` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1BB67` → [RtlStringExValidateDestA](../../text/53/RtlStringExValidateDestA_function_0053BED8.md) (function, `0x0053BED8`)
- `0x00C1BB8F` → [RtlStringCopyWorkerA](../../text/44/RtlStringCopyWorkerA_function_00448140.md) (function, `0x00448140`)
- `0x00C1BBDA` → [RtlInitAnsiString](../../text/47/RtlInitAnsiString_function_00470F40.md) (function, `0x00470F40`)
- `0x00C1BBEE` → [RtlAnsiStringToUnicodeString](../../page/90/RtlAnsiStringToUnicodeString_function_0090BEA0.md) (function, `0x0090BEA0`)
- `0x00C1BC0A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1BC30` → [RtlStringCbPrintfA](../../text/53/RtlStringCbPrintfA_function_0053BC0C.md) (function, `0x0053BC0C`)
- `0x00C1BC4C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1BC5D` → [RtlCreateUnicodeStringFromAsciiz](../../page/78/RtlCreateUnicodeStringFromAsciiz_function_0078B990.md) (function, `0x0078B990`)
- `0x00C1BC96` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C1BCB7` → [RtlpInitializeStackTraceDatabase](../../page/78/RtlpInitializeStackTraceDatabase_function_0078C908.md) (function, `0x0078C908`)
- `0x00C1BCC6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00C1BCE3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C1BCFC` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C1BD27` → [HalQueryMaximumProcessorCount](../../text/4A/HalQueryMaximumProcessorCount_function_004AC9A0.md) (function, `0x004AC9A0`)
- `0x00C1BD34` → [ObInitSystem](../C7/ObInitSystem_function_00C71C7C.md) (function, `0x00C71C7C`)
- `0x00C1BD42` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00C1BD50` → `symcryptk.dll!SymCryptModuleInit` (import, 간접 대상; import `symcryptk.dll!SymCryptModuleInit`)
- `0x00C1BD5C` → [SeInitSystem](../C4/SeInitSystem_function_00C4A74C.md) (function, `0x00C4A74C`)
- `0x00C1BD6A` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00C1BD75` → [PsInitSystem](../BE/PsInitSystem_function_00BEED58.md) (function, `0x00BEED58`)
- `0x00C1BD82` → [DbgkInitialize](../C2/DbgkInitialize_function_00C261E4.md) (function, `0x00C261E4`)
- `0x00C1BD8F` → [PpInitSystem](../C3/PpInitSystem_function_00C32964.md) (function, `0x00C32964`)
- `0x00C1BD9D` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00C1BE1D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00C1BE49` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00C1BE65` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C1BE70` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00C1BE96` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [KiInitializeKernel](../../pagelk/B6/KiInitializeKernel_function_00B68D20.md) at `0x00B6951E`

### Static image references
- `0x00C1B1EE` → RVA `0x00E0A740` (`.data`; read)
- `0x00C1B1FF` → RVA `0x00FD08F4` (`CACHEALI`; read/write)
- `0x00C1B206` → RVA `0x00FD0740` (`CACHEALI`; read)
- `0x00C1B210` → RVA `0x00FCFE08` (`CACHEALI`; write)
- `0x00C1B217` → RVA `0x00E0A74C` (`.data`; read)
- `0x00C1B22B` → RVA `0x00FCFE3C` (`CACHEALI`; write)
- `0x00C1B239` → RVA `0x00FCFD48` (`CACHEALI`; write)
- `0x00C1B240` → RVA `0x00FCFE38` (`CACHEALI`; write)
- `0x00C1B247` → RVA `0x00FCFD88` (`CACHEALI`; write)
- `0x00C1B24E` → RVA `0x00FCFE78` (`CACHEALI`; write)
- `0x00C1B2B4` → RVA `0x00FC5008` (`ALMOSTRO`; read)
- `0x00C1B2C1` → RVA `0x00FCF940` (`CACHEALI`; read)
- `0x00C1B340` → RVA `0x00FC41A0` (`.data`; write)
- `0x00C1B354` → RVA `0x00C78BC0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1B368` → RVA `0x00C78BD0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1B399` → RVA `0x00C78BE0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1B3AD` → RVA `0x00FC6AF2` (`ALMOSTRO`; write)
- `0x00C1B3F9` → RVA `0x01008190` (`INITDATA`; write)
- `0x00C1B413` → RVA `0x00EFEE38` (`.data`; write)
- `0x00C1B41F` → RVA `0x00E00B10` (`.data`; read)
- `0x00C1B426` → RVA `0x00E06D28` (`.data`; read)
- `0x00C1B434` → RVA `0x00FC41A0` (`.data`; read)
- `0x00C1B444` → RVA `0x010087F8` (`INITDATA`; write)
- `0x00C1B471` → RVA `0x01008800` (`INITDATA`; write)
- `0x00C1B48D` → RVA `0x00F0EFD0` (`.data`; read)
- `0x00C1B496` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x00C1B4CE` → RVA `0x00FC6AA0` (`ALMOSTRO`; read)
- `0x00C1B532` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00C1B541` → RVA `0x00EFEDB8` (`.data`; write)
- `0x00C1B5A3` → RVA `0x00FC6DF8` (`ALMOSTRO`; write)
- `0x00C1B5AA` → RVA `0x010086B0` (`INITDATA`; read/write)
- `0x00C1B5B4` → RVA `0x010086F4` (`INITDATA`; read)
- `0x00C1B5D5` → RVA `0x00FC414C` (`.data`; read)
- `0x00C1B5E0` → RVA `0x00FC41C2` (`.data`; write)
- `0x00C1B5E8` → RVA `0x00FC42C4` (`.data`; read)
- `0x00C1B5EF` → RVA `0x00FC414C` (`.data`; write)
- `0x00C1B5FA` → RVA `0x00FC41C0` (`.data`; read/write)
- `0x00C1B600` → RVA `0x0100817C` (`INITDATA`; read)
- `0x00C1B608` → RVA `0x01008178` (`INITDATA`; read)
- `0x00C1B610` → RVA `0x0100869C` (`INITDATA`; write)
- `0x00C1B617` → RVA `0x0100869C` (`INITDATA`; read)
- `0x00C1B647` → RVA `0x00E668C0` (`.data`; write)
- `0x00C1B64E` → RVA `0x010086B4` (`INITDATA`; read)
- `0x00C1B656` → RVA `0x00FC42C0` (`.data`; read/write)
- `0x00C1B65C` → RVA `0x010086B0` (`INITDATA`; read)
- `0x00C1B662` → RVA `0x00FC43C0` (`.data`; read/write)
- `0x00C1B6A0` → RVA `0x00EFA0F0` (`.data`; write)
- `0x00C1B712` → RVA `0x00F22EA0` (`.data`; write)
- `0x00C1B720` → RVA `0x00F22EA8` (`.data`; read)
- `0x00C1B72E` → RVA `0x00F22FB0` (`.data`; read)
- `0x00C1B735` → RVA `0x00F22FA8` (`.data`; write)
- `0x00C1B73E` → RVA `0x00F22FB8` (`.data`; write)
- `0x00C1B745` → RVA `0x00F22FB0` (`.data`; write)
- `0x00C1B754` → RVA `0x010087A0` (`INITDATA`; write)
- `0x00C1B769` → RVA `0x010087A8` (`INITDATA`; write)
- `0x00C1B7AC` → RVA `0x00151720` (`symcryptk.dll!SymCryptEntropyAccumulatorInit1 (IAT)`; read)
- `0x00C1B7C4` → RVA `0x00F21B00` (`.data`; write)
- `0x00C1B804` → RVA `0x00FC6DF8` (`ALMOSTRO`; read)
- `0x00C1B866` → RVA `0x00E660B8` (`.data`; write)
- `0x00C1B897` → RVA `0x00C1BEB0` (`InitLoadDebuggerSymbols`; read)
- `0x00C1B8A3` → RVA `0x00F59CC9` (`.data`; read)
- `0x00C1B8C4` → RVA `0x00FC6ADD` (`ALMOSTRO`; read)
- `0x00C1B8D6` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x00C1B8EA` → RVA `0x00FC6ADD` (`ALMOSTRO`; write)
- `0x00C1B907` → RVA `0x00EFF050` (`.data`; write)
- `0x00C1B91B` → RVA `0x00EFF040` (`.data`; write)
- `0x00C1B931` → RVA `0x00EFF058` (`.data`; write)
- `0x00C1B938` → RVA `0x00EFF040` (`.data`; read)
- `0x00C1B944` → RVA `0x01201841` (`CFGRO`; read)
- `0x00C1B94D` → RVA `0x01201842` (`CFGRO`; read)
- `0x00C1B959` → RVA `0x00F475DC` (`.data`; read)
- `0x00C1B962` → RVA `0x00F475DD` (`.data`; read)
- `0x00C1B96F` → RVA `0x00FC6BD6` (`ALMOSTRO`; write)
- `0x00C1B976` → RVA `0x01201842` (`CFGRO`; write)
- `0x00C1B9AC` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x00C1B9BC` → RVA `0x00C5F5E0` (`MiProtectKernelCfgData`; read)
- `0x00C1BA16` → RVA `0x00FC41C0` (`.data`; read)
- `0x00C1BA83` → RVA `0x00C78BF0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1BAA0` → RVA `0x00FC41C1` (`.data`; read)
- `0x00C1BB1E` → RVA `0x00FC41C2` (`.data`; read)
- `0x00C1BB26` → RVA `0x00C78C10` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1BB77` → RVA `0x00C78C20` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1BBC9` → RVA `0x00FC41B2` (`.data`; write)
- `0x00C1BBE7` → RVA `0x00FC41B0` (`.data`; read)
- `0x00C1BC1E` → RVA `0x00C78C30` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C1BC56` → RVA `0x00FC41D0` (`.data`; read)
- `0x00C1BC6A` → RVA `0x00FC42C0` (`.data`; read)
- `0x00C1BCCB` → RVA `0x00FC42C0` (`.data`; reference)
- `0x00C1BCE8` → RVA `0x00E67AF0` (`.data`; write)
- `0x00C1BD01` → RVA `0x00F05C9C` (`.data`; write)
- `0x00C1BD0B` → RVA `0x00FD9FC8` (`PAGEDATA`; read)
- `0x00C1BD12` → RVA `0x00FD9BA0` (`PAGEDATA`; write)
- `0x00C1BD19` → RVA `0x00FD9FD0` (`PAGEDATA`; write)
- `0x00C1BD20` → RVA `0x00FD9FC8` (`PAGEDATA`; write)
- `0x00C1BD2E` → RVA `0x00FD9B18` (`PAGEDATA`; write)
- `0x00C1BD50` → RVA `0x00151730` (`symcryptk.dll!SymCryptModuleInit (IAT)`; read)
- `0x00C1BDDA` → RVA `0x00FC5078` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **70**
  - `0x00C1B2C8` → [ExpInitLicensing](../../page/7C/ExpInitLicensing_function_007C85C8.md) (`INIT` → `PAGE`)
  - `0x00C1B2D4` → [RtlNlsInitState](../../page/78/RtlNlsInitState_function_0078BEC4.md) (`INIT` → `PAGE`)
  - `0x00C1B2DB` → [VslGetNestedPageProtectionFlags](../../text/2F/VslGetNestedPageProtectionFlags_function_002F2164.md) (`INIT` → `.text`)
  - `0x00C1B321` → [KeSetPagePrivilege](../../text/40/KeSetPagePrivilege_function_00407970.md) (`INIT` → `.text`)
  - `0x00C1B34F` → [strupr](../../text/4F/strupr_function_004FEEE0.md) (`INIT` → `.text`)
  - `0x00C1B35E` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1B372` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1B380` → [atol](../../text/4F/atol_function_004FF8D0.md) (`INIT` → `.text`)
  - `0x00C1B3A3` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C1B3E3` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1B400` → [ExPreInitializeNls](../../page/7C/ExPreInitializeNls_function_007CACDC.md) (`INIT` → `PAGE`)
  - `0x00C1B42D` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`INIT` → `.text`)
  - `0x00C1B44B` → [HalInitSystem](../../pagelk/B5/HalInitSystem_function_00B5B6E0.md) (`INIT` → `PAGELK`)
  - `0x00C1B459` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`INIT` → `.text`)
  - `0x00C1B4C8` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1B576` → [LdrFindResource_U](../../page/78/LdrFindResource_U_function_0078BD20.md) (`INIT` → `PAGE`)
  - `0x00C1B595` → [LdrAccessResource](../../page/78/LdrAccessResource_function_0078B9E0.md) (`INIT` → `PAGE`)
  - `0x00C1B62D` → [KeAdjustInterruptTime](../../text/4C/KeAdjustInterruptTime_function_004C9EB0.md) (`INIT` → `.text`)
  - `0x00C1B634` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C1B6BA` → [IpmiHwInitializeContext](../../text/6A/IpmiHwInitializeContext_function_006A64F8.md) (`INIT` → `.text`)
  - `0x00C1B6C3` → [WheaSelLogSetNtSchedulerAvailability](../../text/65/WheaSelLogSetNtSchedulerAvailability_function_0065DB18.md) (`INIT` → `.text`)
  - `0x00C1B6F0` → [WheaSelLogCheckPoint](../../page/7D/WheaSelLogCheckPoint_function_007D6800.md) (`INIT` → `PAGE`)
  - `0x00C1B707` → [KeInitializeXSaveStructures](../../pagelk/B6/KeInitializeXSaveStructures_function_00B66CEC.md) (`INIT` → `PAGELK`)
  - `0x00C1B729` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C1B74C` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C1B764` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C1B7BD` → [EtwInitialize](../../page/7B/EtwInitialize_function_007B4D40.md) (`INIT` → `PAGE`)
  - `0x00C1B7E7` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1B7F2` → [HalInitializeBios](../../text/53/HalInitializeBios_function_0053D9A0.md) (`INIT` → `.text`)
  - `0x00C1B820` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C1B835` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`INIT` → `.text`)
  - `0x00C1B848` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C1B880` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1B89E` → [MiEnumerateSystemImages](../../text/2A/MiEnumerateSystemImages_function_002A3D40.md) (`INIT` → `.text`)
  - `0x00C1B8AF` → [DbgBreakPointWithStatus](../../text/4F/DbgBreakPointWithStatus_function_004FE4E0.md) (`INIT` → `.text`)
  - `0x00C1B93F` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`INIT` → `.text`)
  - `0x00C1B9A7` → [PsInitializeWin32kKernelExports](../../text/5E/PsInitializeWin32kKernelExports_function_005E2190.md) (`INIT` → `.text`)
  - `0x00C1B9C5` → [MiEnumerateSystemImages](../../text/2A/MiEnumerateSystemImages_function_002A3D40.md) (`INIT` → `.text`)
  - `0x00C1B9CD` → [HvlPhase1Initialize](../../text/58/HvlPhase1Initialize_function_00583D80.md) (`INIT` → `.text`)
  - `0x00C1BA41` → [RtlFindMessage](../../page/99/RtlFindMessage_function_0099B220.md) (`INIT` → `PAGE`)
  - `0x00C1BA5C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1BA6F` → [RtlInitAnsiString](../../text/47/RtlInitAnsiString_function_00470F40.md) (`INIT` → `.text`)
  - `0x00C1BAB2` → [RtlStringCbPrintfA](../../text/53/RtlStringCbPrintfA_function_0053BC0C.md) (`INIT` → `.text`)
  - `0x00C1BACE` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1BAFC` → [RtlStringCbCatExA](../../text/53/RtlStringCbCatExA_function_0053BB58.md) (`INIT` → `.text`)
  - `0x00C1BB18` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1BB37` → [RtlStringCbPrintfA](../../text/53/RtlStringCbPrintfA_function_0053BC0C.md) (`INIT` → `.text`)
  - `0x00C1BB57` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1BB67` → [RtlStringExValidateDestA](../../text/53/RtlStringExValidateDestA_function_0053BED8.md) (`INIT` → `.text`)
  - `0x00C1BB8F` → [RtlStringCopyWorkerA](../../text/44/RtlStringCopyWorkerA_function_00448140.md) (`INIT` → `.text`)
  - `0x00C1BBDA` → [RtlInitAnsiString](../../text/47/RtlInitAnsiString_function_00470F40.md) (`INIT` → `.text`)
  - `0x00C1BBEE` → [RtlAnsiStringToUnicodeString](../../page/90/RtlAnsiStringToUnicodeString_function_0090BEA0.md) (`INIT` → `PAGE`)
  - `0x00C1BC0A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1BC30` → [RtlStringCbPrintfA](../../text/53/RtlStringCbPrintfA_function_0053BC0C.md) (`INIT` → `.text`)
  - `0x00C1BC4C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1BC5D` → [RtlCreateUnicodeStringFromAsciiz](../../page/78/RtlCreateUnicodeStringFromAsciiz_function_0078B990.md) (`INIT` → `PAGE`)
  - `0x00C1BC96` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C1BCB7` → [RtlpInitializeStackTraceDatabase](../../page/78/RtlpInitializeStackTraceDatabase_function_0078C908.md) (`INIT` → `PAGE`)
  - `0x00C1BCC6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`INIT` → `POOLCODE`)
  - `0x00C1BCE3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C1BCFC` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C1BD27` → [HalQueryMaximumProcessorCount](../../text/4A/HalQueryMaximumProcessorCount_function_004AC9A0.md) (`INIT` → `.text`)
  - `0x00C1BD42` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`INIT` → `.text`)
  - `0x00C1BD6A` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`INIT` → `.text`)
  - `0x00C1BD9D` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`INIT` → `.text`)
  - `0x00C1BE1D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
  - `0x00C1BE49` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`INIT` → `.text`)
  - `0x00C1BE65` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C1BE70` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`INIT` → `.text`)
  - `0x00C1BE96` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C1B1C8  48 8B C4                        mov rax, rsp
00C1B1CB  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00C1B1CF  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00C1B1D3  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00C1B1D7  55                              push rbp
00C1B1D8  41 54                           push r12
00C1B1DA  41 55                           push r13
00C1B1DC  41 56                           push r14
00C1B1DE  41 57                           push r15
00C1B1E0  48 8D A8 B8 FE FF FF            lea rbp, [rax - 0x148]
00C1B1E7  48 81 EC 20 02 00 00            sub rsp, 0x220
00C1B1EE  48 8B 05 4B F5 1E 00            mov rax, qword ptr [rip + 0x1ef54b]
00C1B1F5  48 33 C4                        xor rax, rsp
00C1B1F8  48 89 85 10 01 00 00            mov qword ptr [rbp + 0x110], rax
00C1B1FF  83 0D EE 56 3B 00 FF            or dword ptr [rip + 0x3b56ee], 0xffffffff
00C1B206  48 8D 05 33 55 3B 00            lea rax, [rip + 0x3b5533]
00C1B20D  45 33 ED                        xor r13d, r13d
00C1B210  48 89 05 F1 4B 3B 00            mov qword ptr [rip + 0x3b4bf1], rax
00C1B217  8B 05 2F F5 1E 00               mov eax, dword ptr [rip + 0x1ef52f]
00C1B21D  48 8B D9                        mov rbx, rcx
00C1B220  0F B7 C8                        movzx ecx, ax
00C1B223  0F 57 C0                        xorps xmm0, xmm0
00C1B226  B8 E9 FD 00 00                  mov eax, 0xfde9
00C1B22B  C7 05 07 4C 3B 00 03 01 00 00   mov dword ptr [rip + 0x3b4c07], 0x103
00C1B235  45 8D 7D 01                     lea r15d, [r13 + 1]
00C1B239  66 89 05 08 4B 3B 00            mov word ptr [rip + 0x3b4b08], ax
00C1B240  44 89 3D F1 4B 3B 00            mov dword ptr [rip + 0x3b4bf1], r15d
00C1B247  66 89 05 3A 4B 3B 00            mov word ptr [rip + 0x3b4b3a], ax
00C1B24E  89 0D 24 4C 3B 00               mov dword ptr [rip + 0x3b4c24], ecx
00C1B254  8B 13                           mov edx, dword ptr [rbx]
00C1B256  4C 89 6C 24 60                  mov qword ptr [rsp + 0x60], r13
00C1B25B  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
00C1B260  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00C1B265  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
00C1B26A  83 FA 0A                        cmp edx, 0xa
00C1B26D  0F 85 03 0C 00 00               jne 0x140c1be76
00C1B273  44 39 6B 04                     cmp dword ptr [rbx + 4], r13d
00C1B277  0F 85 F9 0B 00 00               jne 0x140c1be76
00C1B27D  81 7B 08 70 01 00 00            cmp dword ptr [rbx + 8], 0x170
00C1B284  0F 85 EC 0B 00 00               jne 0x140c1be76
00C1B28A  48 8B 8B F0 00 00 00            mov rcx, qword ptr [rbx + 0xf0]
00C1B291  8B 01                           mov eax, dword ptr [rcx]
00C1B293  3D 30 11 00 00                  cmp eax, 0x1130
00C1B298  0F 85 DB 0B 00 00               jne 0x140c1be79
00C1B29E  81 B9 A8 0B 00 00 10 00 00 0A   cmp dword ptr [rcx + 0xba8], 0xa000010
00C1B2A8  0F 85 CB 0B 00 00               jne 0x140c1be79
00C1B2AE  8B 89 54 0B 00 00               mov ecx, dword ptr [rcx + 0xb54]
00C1B2B4  48 8B 05 4D 9D 3A 00            mov rax, qword ptr [rip + 0x3a9d4d]
00C1B2BB  89 88 C4 02 00 00               mov dword ptr [rax + 0x2c4], ecx
00C1B2C1  48 8D 0D 78 46 3B 00            lea rcx, [rip + 0x3b4678]
00C1B2C8  E8 FB D2 BA FF                  call 0x1407c85c8
00C1B2CD  48 8D 0D 6C 46 3B 00            lea rcx, [rip + 0x3b466c]
00C1B2D4  E8 EB 0B B7 FF                  call 0x14078bec4
00C1B2D9  33 C9                           xor ecx, ecx
00C1B2DB  E8 84 6E 6D FF                  call 0x1402f2164
00C1B2E0  83 E0 06                        and eax, 6
00C1B2E3  41 8D 7D 04                     lea edi, [r13 + 4]
00C1B2E7  3C 06                           cmp al, 6
00C1B2E9  75 4E                           jne 0x140c1b339
00C1B2EB  4C 8D 7B 20                     lea r15, [rbx + 0x20]
00C1B2EF  4C 89 6D A8                     mov qword ptr [rbp - 0x58], r13
00C1B2F3  49 8B 37                        mov rsi, qword ptr [r15]
00C1B2F6  4C 89 6D A0                     mov qword ptr [rbp - 0x60], r13
00C1B2FA  49 3B F7                        cmp rsi, r15
00C1B2FD  74 34                           je 0x140c1b333
00C1B2FF  39 7E 18                        cmp dword ptr [rsi + 0x18], edi
00C1B302  75 2A                           jne 0x140c1b32e
00C1B304  4C 8B 76 20                     mov r14, qword ptr [rsi + 0x20]
00C1B308  4D 8D 66 FF                     lea r12, [r14 - 1]
00C1B30C  4C 03 66 28                     add r12, qword ptr [rsi + 0x28]
00C1B310  EB 17                           jmp 0x140c1b329
00C1B312  41 B9 10 00 00 00               mov r9d, 0x10
00C1B318  4C 8D 45 A0                     lea r8, [rbp - 0x60]
00C1B31C  33 D2                           xor edx, edx
00C1B31E  49 8B CE                        mov rcx, r14
00C1B321  E8 4A C6 7E FF                  call 0x140407970
00C1B326  49 FF C6                        inc r14
00C1B329  4D 3B F4                        cmp r14, r12
00C1B32C  76 E4                           jbe 0x140c1b312
00C1B32E  48 8B 36                        mov rsi, qword ptr [rsi]
00C1B331  EB C7                           jmp 0x140c1b2fa
00C1B333  41 BF 01 00 00 00               mov r15d, 1
00C1B339  48 8B B3 D8 00 00 00            mov rsi, qword ptr [rbx + 0xd8]
00C1B340  44 89 2D 59 8E 3A 00            mov dword ptr [rip + 0x3a8e59], r13d
00C1B347  48 85 F6                        test rsi, rsi
00C1B34A  74 68                           je 0x140c1b3b4
00C1B34C  48 8B CE                        mov rcx, rsi
00C1B34F  E8 8C 3B 8E FF                  call 0x1404feee0
00C1B354  48 8D 15 65 D8 05 00            lea rdx, [rip + 0x5d865]
00C1B35B  48 8B CE                        mov rcx, rsi
00C1B35E  E8 1D 43 8E FF                  call 0x1404ff680
00C1B363  48 85 C0                        test rax, rax
00C1B366  74 31                           je 0x140c1b399
00C1B368  48 8D 15 61 D8 05 00            lea rdx, [rip + 0x5d861]
00C1B36F  48 8B C8                        mov rcx, rax
00C1B372  E8 09 43 8E FF                  call 0x1404ff680
00C1B377  48 85 C0                        test rax, rax
00C1B37A  74 1D                           je 0x140c1b399
00C1B37C  48 8D 48 01                     lea rcx, [rax + 1]
00C1B380  E8 4B 45 8E FF                  call 0x1404ff8d0
00C1B385  48 63 D0                        movsxd rdx, eax
00C1B388  48 C1 E2 08                     shl rdx, 8
00C1B38C  48 85 D2                        test rdx, rdx
00C1B38F  74 08                           je 0x140c1b399
00C1B391  48 8B CB                        mov rcx, rbx
00C1B394  E8 E7 FA FF FF                  call 0x140c1ae80
00C1B399  48 8D 15 40 D8 05 00            lea rdx, [rip + 0x5d840]
00C1B3A0  48 8B CE                        mov rcx, rsi
00C1B3A3  E8 D8 42 8E FF                  call 0x1404ff680
00C1B3A8  48 85 C0                        test rax, rax
00C1B3AB  74 07                           je 0x140c1b3b4
00C1B3AD  44 88 3D 3E B7 3A 00            mov byte ptr [rip + 0x3ab73e], r15b
00C1B3B4  48 8D 4B 20                     lea rcx, [rbx + 0x20]
00C1B3B8  49 8B C5                        mov rax, r13
00C1B3BB  48 8B 11                        mov rdx, qword ptr [rcx]
00C1B3BE  48 3B D1                        cmp rdx, rcx
00C1B3C1  74 26                           je 0x140c1b3e9
00C1B3C3  4C 8B 42 20                     mov r8, qword ptr [rdx + 0x20]
00C1B3C7  4C 8B 4A 28                     mov r9, qword ptr [rdx + 0x28]
00C1B3CB  4C 3B C0                        cmp r8, rax
00C1B3CE  72 09                           jb 0x140c1b3d9
00C1B3D0  48 8B 12                        mov rdx, qword ptr [rdx]
00C1B3D3  4B 8D 04 08                     lea rax, [r8 + r9]
00C1B3D7  EB E5                           jmp 0x140c1b3be
00C1B3D9  B9 31 00 00 00                  mov ecx, 0x31
00C1B3DE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C1B3E3  E8 78 22 8E FF                  call 0x1404fd660
00C1B3E8  CC                              int3
00C1B3E9  48 8B 83 E0 00 00 00            mov rax, qword ptr [rbx + 0xe0]
00C1B3F0  48 85 C0                        test rax, rax
00C1B3F3  74 10                           je 0x140c1b405
00C1B3F5  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00C1B3F9  48 89 05 90 CD 3E 00            mov qword ptr [rip + 0x3ecd90], rax
00C1B400  E8 D7 F8 BA FF                  call 0x1407cacdc
00C1B405  48 8B 83 F0 00 00 00            mov rax, qword ptr [rbx + 0xf0]
00C1B40C  48 8B 88 A0 0B 00 00            mov rcx, qword ptr [rax + 0xba0]
00C1B413  48 89 0D 1E 3A 2E 00            mov qword ptr [rip + 0x2e3a1e], rcx
00C1B41A  E8 4D 9D 03 00                  call 0x140c5516c
00C1B41F  48 8B 05 EA 56 1E 00            mov rax, qword ptr [rip + 0x1e56ea]
00C1B426  48 8B 0D FB B8 1E 00            mov rcx, qword ptr [rip + 0x1eb8fb]
00C1B42D  E8 9E F6 A9 FF                  call 0x1406baad0
00C1B432  0F 31                           rdtsc
00C1B434  8B 0D 66 8D 3A 00               mov ecx, dword ptr [rip + 0x3a8d66]
00C1B43A  48 C1 E2 20                     shl rdx, 0x20
00C1B43E  48 0B C2                        or rax, rdx
00C1B441  48 8B D3                        mov rdx, rbx
00C1B444  48 89 05 AD D3 3E 00            mov qword ptr [rip + 0x3ed3ad], rax
00C1B44B  E8 90 02 F4 FF                  call 0x140b5b6e0
00C1B450  84 C0                           test al, al
00C1B452  75 0B                           jne 0x140c1b45f
00C1B454  B9 5C 00 00 00                  mov ecx, 0x5c
00C1B459  E8 E2 21 8E FF                  call 0x1404fd640
00C1B45E  CC                              int3
00C1B45F  0F 31                           rdtsc
00C1B461  8B 0D 39 8D 3A 00               mov ecx, dword ptr [rip + 0x3a8d39]
00C1B467  48 C1 E2 20                     shl rdx, 0x20
00C1B46B  48 0B C2                        or rax, rdx
00C1B46E  48 8B D3                        mov rdx, rbx
00C1B471  48 89 05 88 D3 3E 00            mov qword ptr [rip + 0x3ed388], rax
00C1B478  E8 B3 57 05 00                  call 0x140c70c30
00C1B47D  41 8B CF                        mov ecx, r15d
00C1B480  E8 DF AE 02 00                  call 0x140c46364
00C1B485  48 8B CB                        mov rcx, rbx
00C1B488  E8 FB D9 03 00                  call 0x140c58e88
00C1B48D  44 38 2D 3C 3B 2F 00            cmp byte ptr [rip + 0x2f3b3c], r13b
00C1B494  75 10                           jne 0x140c1b4a6
00C1B496  48 8B 05 A3 D7 3A 00            mov rax, qword ptr [rip + 0x3ad7a3]
00C1B49D  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
00C1B4A1  F0 0F BA 31 15                  lock btr dword ptr [rcx], 0x15
00C1B4A6  33 C9                           xor ecx, ecx
00C1B4A8  E8 B3 61 05 00                  call 0x140c71660
00C1B4AD  84 C0                           test al, al
00C1B4AF  75 1D                           jne 0x140c1b4ce
00C1B4B1  45 33 C9                        xor r9d, r9d
00C1B4B4  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1B4B9  48 C7 C2 01 00 00 C0            mov rdx, 0xffffffffc0000001
00C1B4C0  41 8D 49 31                     lea ecx, [r9 + 0x31]
00C1B4C4  45 8D 41 0B                     lea r8d, [r9 + 0xb]
00C1B4C8  E8 93 21 8E FF                  call 0x1404fd660
00C1B4CD  CC                              int3
00C1B4CE  44 8B 05 CB B5 3A 00            mov r8d, dword ptr [rip + 0x3ab5cb]
00C1B4D5  B8 59 17 B7 D1                  mov eax, 0xd1b71759
00C1B4DA  41 F7 E0                        mul r8d
00C1B4DD  45 8B CD                        mov r9d, r13d
00C1B4E0  41 BA 18 00 00 00               mov r10d, 0x18
00C1B4E6  C1 EA 0D                        shr edx, 0xd
00C1B4E9  41 BB 10 27 00 00               mov r11d, 0x2710
00C1B4EF  69 C2 10 27 00 00               imul eax, edx, 0x2710
00C1B4F5  44 2B C0                        sub r8d, eax
00C1B4F8  45 03 C0                        add r8d, r8d
00C1B4FB  45 03 C9                        add r9d, r9d
00C1B4FE  41 8B C1                        mov eax, r9d
00C1B501  41 8B C8                        mov ecx, r8d
00C1B504  45 0B CF                        or r9d, r15d
00C1B507  45 3B C3                        cmp r8d, r11d
00C1B50A  44 0F 42 C8                     cmovb r9d, eax
00C1B50E  41 8B C0                        mov eax, r8d
00C1B511  41 81 C0 F0 D8 FF FF            add r8d, 0xffffd8f0
00C1B518  41 3B C3                        cmp eax, r11d
00C1B51B  44 0F 42 C0                     cmovb r8d, eax
00C1B51F  4D 2B D7                        sub r10, r15
00C1B522  75 D4                           jne 0x140c1b4f8
00C1B524  48 8B 05 DD 9A 3A 00            mov rax, qword ptr [rip + 0x3a9add]
00C1B52B  45 8D 42 03                     lea r8d, [r10 + 3]
00C1B52F  C1 E2 18                        shl edx, 0x18
00C1B532  48 8D 0D C7 4A 3E FF            lea rcx, [rip - 0xc1b539]
00C1B539  41 0B D1                        or edx, r9d
00C1B53C  4C 89 6C 24 40                  mov qword ptr [rsp + 0x40], r13
00C1B541  89 15 71 38 2E 00               mov dword ptr [rip + 0x2e3871], edx
00C1B547  4C 8D 4C 24 58                  lea r9, [rsp + 0x58]
00C1B54C  89 50 04                        mov dword ptr [rax + 4], edx
00C1B54F  48 8D 55 B0                     lea rdx, [rbp - 0x50]
00C1B553  48 8B 05 AE 9A 3A 00            mov rax, qword ptr [rip + 0x3a9aae]
00C1B55A  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
00C1B55F  44 89 A8 3C 02 00 00            mov dword ptr [rax + 0x23c], r13d
00C1B566  48 C7 45 B0 0B 00 00 00         mov qword ptr [rbp - 0x50], 0xb
00C1B56E  4C 89 7D B8                     mov qword ptr [rbp - 0x48], r15
00C1B572  4C 89 6D C0                     mov qword ptr [rbp - 0x40], r13
00C1B576  E8 A5 07 B7 FF                  call 0x14078bd20
00C1B57B  85 C0                           test eax, eax
00C1B57D  78 2B                           js 0x140c1b5aa
00C1B57F  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00C1B584  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
00C1B589  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
00C1B58E  48 8D 0D 6B 4A 3E FF            lea rcx, [rip - 0xc1b595]
00C1B595  E8 46 04 B7 FF                  call 0x14078b9e0
00C1B59A  85 C0                           test eax, eax
00C1B59C  78 0C                           js 0x140c1b5aa
00C1B59E  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00C1B5A3  48 89 05 4E B8 3A 00            mov qword ptr [rip + 0x3ab84e], rax
00C1B5AA  81 25 FC D0 3E 00 1F 20 00 00   and dword ptr [rip + 0x3ed0fc], 0x201f
00C1B5B4  8B 05 3A D1 3E 00               mov eax, dword ptr [rip + 0x3ed13a]
00C1B5BA  48 8B 0D 47 9A 3A 00            mov rcx, qword ptr [rip + 0x3a9a47]
00C1B5C1  89 81 58 02 00 00               mov dword ptr [rcx + 0x258], eax
00C1B5C7  48 8B 05 3A 9A 3A 00            mov rax, qword ptr [rip + 0x3a9a3a]
00C1B5CE  44 88 B8 8B 02 00 00            mov byte ptr [rax + 0x28b], r15b
00C1B5D5  8B 05 71 8B 3A 00               mov eax, dword ptr [rip + 0x3a8b71]
00C1B5DB  25 FF 0F 00 00                  and eax, 0xfff
00C1B5E0  66 44 89 2D DA 8B 3A 00         mov word ptr [rip + 0x3a8bda], r13w
00C1B5E8  44 39 2D D5 8C 3A 00            cmp dword ptr [rip + 0x3a8cd5], r13d
00C1B5EF  89 05 57 8B 3A 00               mov dword ptr [rip + 0x3a8b57], eax
00C1B5F5  74 09                           je 0x140c1b600
00C1B5F7  C1 E0 10                        shl eax, 0x10
00C1B5FA  09 05 C0 8B 3A 00               or dword ptr [rip + 0x3a8bc0], eax
00C1B600  39 3D 76 CB 3E 00               cmp dword ptr [rip + 0x3ecb76], edi
00C1B606  75 08                           jne 0x140c1b610
00C1B608  39 3D 6A CB 3E 00               cmp dword ptr [rip + 0x3ecb6a], edi
00C1B60E  74 07                           je 0x140c1b617
00C1B610  44 89 2D 85 D0 3E 00            mov dword ptr [rip + 0x3ed085], r13d
00C1B617  8B 05 7F D0 3E 00               mov eax, dword ptr [rip + 0x3ed07f]
00C1B61D  85 C0                           test eax, eax
00C1B61F  74 2D                           je 0x140c1b64e
00C1B621  F7 D8                           neg eax
00C1B623  41 8A D7                        mov dl, r15b
00C1B626  48 69 C8 10 27 00 00            imul rcx, rax, 0x2710
00C1B62D  E8 7E E8 8A FF                  call 0x1404c9eb0
00C1B632  33 C9                           xor ecx, ecx
00C1B634  E8 A7 31 76 FF                  call 0x14037e7e0
00C1B639  48 8B 0D C8 99 3A 00            mov rcx, qword ptr [rip + 0x3a99c8]
00C1B640  48 89 81 48 03 00 00            mov qword ptr [rcx + 0x348], rax
00C1B647  4C 89 2D 72 B2 24 00            mov qword ptr [rip + 0x24b272], r13
00C1B64E  8B 05 60 D0 3E 00               mov eax, dword ptr [rip + 0x3ed060]
00C1B654  33 C9                           xor ecx, ecx
00C1B656  09 05 64 8C 3A 00               or dword ptr [rip + 0x3a8c64], eax
00C1B65C  8B 05 4E D0 3E 00               mov eax, dword ptr [rip + 0x3ed04e]
00C1B662  09 05 58 8D 3A 00               or dword ptr [rip + 0x3a8d58], eax
00C1B668  48 8B 05 99 99 3A 00            mov rax, qword ptr [rip + 0x3a9999]
00C1B66F  44 89 B8 C0 03 00 00            mov dword ptr [rax + 0x3c0], r15d
00C1B676  48 8B 05 8B 99 3A 00            mov rax, qword ptr [rip + 0x3a998b]
00C1B67D  44 88 B8 C4 03 00 00            mov byte ptr [rax + 0x3c4], r15b
00C1B684  48 8B 05 7D 99 3A 00            mov rax, qword ptr [rip + 0x3a997d]
00C1B68B  66 44 89 B8 6A 03 00 00         mov word ptr [rax + 0x36a], r15w
00C1B693  E8 10 5B 03 00                  call 0x140c511a8
00C1B698  84 C0                           test al, al
00C1B69A  0F 84 CB 07 00 00               je 0x140c1be6b
00C1B6A0  4C 89 2D 49 EA 2D 00            mov qword ptr [rip + 0x2dea49], r13
00C1B6A7  48 8B 83 F0 00 00 00            mov rax, qword ptr [rbx + 0xf0]
00C1B6AE  48 8B 88 78 0E 00 00            mov rcx, qword ptr [rax + 0xe78]
00C1B6B5  48 85 C9                        test rcx, rcx
00C1B6B8  74 3B                           je 0x140c1b6f5
00C1B6BA  E8 39 AE A8 FF                  call 0x1406a64f8
00C1B6BF  85 C0                           test eax, eax
00C1B6C1  78 32                           js 0x140c1b6f5
00C1B6C3  E8 50 24 A4 FF                  call 0x14065db18
00C1B6C8  48 8B 8B F0 00 00 00            mov rcx, qword ptr [rbx + 0xf0]
00C1B6CF  F7 81 84 00 00 00 00 00 08 00   test dword ptr [rcx + 0x84], 0x80000
00C1B6D9  74 1A                           je 0x140c1b6f5
00C1B6DB  8A 81 58 0A 00 00               mov al, byte ptr [rcx + 0xa58]
00C1B6E1  B9 05 00 00 00                  mov ecx, 5
00C1B6E6  40 22 C7                        and al, dil
00C1B6E9  F6 D8                           neg al
00C1B6EB  1B D2                           sbb edx, edx
00C1B6ED  83 E2 03                        and edx, 3
00C1B6F0  E8 0B B1 BB FF                  call 0x1407d6800
00C1B6F5  E8 7A B7 01 00                  call 0x140c36e74
00C1B6FA  48 8B CB                        mov rcx, rbx
00C1B6FD  E8 82 05 03 00                  call 0x140c4bc84
00C1B702  E8 E1 0B 00 00                  call 0x140c1c2e8
00C1B707  E8 E0 B5 F4 FF                  call 0x140b66cec
00C1B70C  41 BE 00 01 00 00               mov r14d, 0x100
00C1B712  48 C7 05 83 77 30 00 01 00 20 00  mov qword ptr [rip + 0x307783], 0x200001
00C1B71D  45 8B C6                        mov r8d, r14d
00C1B720  48 8D 0D 81 77 30 00            lea rcx, [rip + 0x307781]
00C1B727  33 D2                           xor edx, edx
00C1B729  E8 12 B5 AA FF                  call 0x1406c6c40
00C1B72E  48 8D 05 7B 78 30 00            lea rax, [rip + 0x30787b]
00C1B735  4C 89 2D 6C 78 30 00            mov qword ptr [rip + 0x30786c], r13
00C1B73C  33 C9                           xor ecx, ecx
00C1B73E  48 89 05 73 78 30 00            mov qword ptr [rip + 0x307873], rax
00C1B745  48 89 05 64 78 30 00            mov qword ptr [rip + 0x307864], rax
00C1B74C  E8 8F 30 76 FF                  call 0x14037e7e0
00C1B751  48 8B D3                        mov rdx, rbx
00C1B754  48 89 05 45 D0 3E 00            mov qword ptr [rip + 0x3ed045], rax
00C1B75B  33 C9                           xor ecx, ecx
00C1B75D  E8 2E 32 FD FF                  call 0x140bee990
00C1B762  33 C9                           xor ecx, ecx
00C1B764  E8 77 30 76 FF                  call 0x14037e7e0
00C1B769  48 89 05 38 D0 3E 00            mov qword ptr [rip + 0x3ed038], rax
00C1B770  49 8B D5                        mov rdx, r13
00C1B773  48 8B 8B F0 00 00 00            mov rcx, qword ptr [rbx + 0xf0]
00C1B77A  BE 08 00 00 00                  mov esi, 8
00C1B77F  48 85 C9                        test rcx, rcx
00C1B782  74 1A                           je 0x140c1b79e
00C1B784  48 8B 81 58 0B 00 00            mov rax, qword ptr [rcx + 0xb58]
00C1B78B  48 85 C0                        test rax, rax
00C1B78E  74 0E                           je 0x140c1b79e
00C1B790  8B 00                           mov eax, dword ptr [rax]
00C1B792  40 84 C6                        test sil, al
00C1B795  74 07                           je 0x140c1b79e
00C1B797  48 8B 91 18 11 00 00            mov rdx, qword ptr [rcx + 0x1118]
00C1B79E  48 8B 0D 9B D4 3A 00            mov rcx, qword ptr [rip + 0x3ad49b]
00C1B7A5  48 81 C1 C0 91 00 00            add rcx, 0x91c0
00C1B7AC  48 FF 15 6D 5F 53 FF            call qword ptr [rip - 0xaca093]
00C1B7B3  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00C1B7B8  48 8B D3                        mov rdx, rbx
00C1B7BB  33 C9                           xor ecx, ecx
00C1B7BD  E8 7E 95 B9 FF                  call 0x1407b4d40
00C1B7C2  33 C9                           xor ecx, ecx
00C1B7C4  4C 89 2D 35 63 30 00            mov qword ptr [rip + 0x306335], r13
00C1B7CB  E8 E8 36 FD FF                  call 0x140beeeb8
00C1B7D0  85 C0                           test eax, eax
00C1B7D2  79 19                           jns 0x140c1b7ed
00C1B7D4  45 33 C9                        xor r9d, r9d
00C1B7D7  48 63 D0                        movsxd rdx, eax
00C1B7DA  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1B7DF  41 8D 49 31                     lea ecx, [r9 + 0x31]
00C1B7E3  45 8D 41 13                     lea r8d, [r9 + 0x13]
00C1B7E7  E8 74 1E 8E FF                  call 0x1404fd660
00C1B7EC  CC                              int3
00C1B7ED  48 8B D3                        mov rdx, rbx
00C1B7F0  33 C9                           xor ecx, ecx
00C1B7F2  E8 A9 21 92 FF                  call 0x14053d9a0
00C1B7F7  45 33 C0                        xor r8d, r8d
00C1B7FA  48 8B D3                        mov rdx, rbx
00C1B7FD  33 C9                           xor ecx, ecx
00C1B7FF  E8 1C EC 00 00                  call 0x140c2a420
00C1B804  4C 39 2D ED B5 3A 00            cmp qword ptr [rip + 0x3ab5ed], r13
00C1B80B  74 4D                           je 0x140c1b85a
00C1B80D  44 8B 64 24 30                  mov r12d, dword ptr [rsp + 0x30]
00C1B812  41 B8 4B 69 42 63               mov r8d, 0x6342694b
00C1B818  41 8B D4                        mov edx, r12d
00C1B81B  B9 40 00 00 00                  mov ecx, 0x40
00C1B820  E8 CB 68 F6 FF                  call 0x140b820f0
00C1B825  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00C1B82A  4C 8B F8                        mov r15, rax
00C1B82D  48 85 C0                        test rax, rax
00C1B830  75 09                           jne 0x140c1b83b
00C1B832  8D 48 7D                        lea ecx, [rax + 0x7d]
00C1B835  E8 06 1E 8E FF                  call 0x1404fd640
00C1B83A  CC                              int3
00C1B83B  48 8B 15 B6 B5 3A 00            mov rdx, qword ptr [rip + 0x3ab5b6]
00C1B842  4D 8B C4                        mov r8, r12
00C1B845  49 8B CF                        mov rcx, r15
00C1B848  E8 F3 AF AA FF                  call 0x1406c6840
00C1B84D  4C 89 3D A4 B5 3A 00            mov qword ptr [rip + 0x3ab5a4], r15
00C1B854  41 BF 01 00 00 00               mov r15d, 1
00C1B85A  41 BC 02 00 00 00               mov r12d, 2
00C1B860  44 39 63 0C                     cmp dword ptr [rbx + 0xc], r12d
00C1B864  73 20                           jae 0x140c1b886
00C1B866  44 89 2D 4B A8 24 00            mov dword ptr [rip + 0x24a84b], r13d
00C1B86D  45 33 C9                        xor r9d, r9d
00C1B870  8B 53 0C                        mov edx, dword ptr [rbx + 0xc]
00C1B873  45 8B C4                        mov r8d, r12d
00C1B876  B9 96 01 00 00                  mov ecx, 0x196
00C1B87B  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1B880  E8 DB 1D 8E FF                  call 0x1404fd660
00C1B885  CC                              int3
00C1B886  45 33 C0                        xor r8d, r8d
00C1B889  4C 89 6D 80                     mov qword ptr [rbp - 0x80], r13
00C1B88D  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00C1B892  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
00C1B897  48 8D 0D 12 06 00 00            lea rcx, [rip + 0x612]
00C1B89E  E8 9D 84 68 FF                  call 0x1402a3d40
00C1B8A3  44 38 2D 1F E4 33 00            cmp byte ptr [rip + 0x33e41f], r13b
00C1B8AA  74 08                           je 0x140c1b8b4
00C1B8AC  41 8B CF                        mov ecx, r15d
00C1B8AF  E8 2C 2C 8E FF                  call 0x1404fe4e0
00C1B8B4  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00C1B8BD  48 8B 88 B8 8E 00 00            mov rcx, qword ptr [rax + 0x8eb8]
00C1B8C4  8A 05 13 B2 3A 00               mov al, byte ptr [rip + 0x3ab213]
00C1B8CA  48 F7 D9                        neg rcx
00C1B8CD  1A D2                           sbb dl, dl
00C1B8CF  24 FD                           and al, 0xfd
00C1B8D1  41 22 D4                        and dl, r12b
00C1B8D4  0A D0                           or dl, al
00C1B8D6  8B 05 DC B1 3A 00               mov eax, dword ptr [rip + 0x3ab1dc]
00C1B8DC  C1 E8 1C                        shr eax, 0x1c
00C1B8DF  80 E2 FB                        and dl, 0xfb
00C1B8E2  40 22 C7                        and al, dil
00C1B8E5  41 0A C7                        or al, r15b
00C1B8E8  0A D0                           or dl, al
00C1B8EA  88 15 ED B1 3A 00               mov byte ptr [rip + 0x3ab1ed], dl
00C1B8F0  BA 20 00 00 00                  mov edx, 0x20
00C1B8F5  8A 83 08 01 00 00               mov al, byte ptr [rbx + 0x108]
00C1B8FB  41 22 C7                        and al, r15b
00C1B8FE  F6 D8                           neg al
00C1B900  1B C9                           sbb ecx, ecx
00C1B902  F7 D9                           neg ecx
00C1B904  41 03 CF                        add ecx, r15d
00C1B907  89 0D 43 37 2E 00               mov dword ptr [rip + 0x2e3743], ecx
00C1B90D  48 8B 83 F0 00 00 00            mov rax, qword ptr [rbx + 0xf0]
00C1B914  0F 10 80 00 01 00 00            movups xmm0, xmmword ptr [rax + 0x100]
00C1B91B  F3 0F 7F 05 1D 37 2E 00         movdqu xmmword ptr [rip + 0x2e371d], xmm0
00C1B923  48 8B 83 F0 00 00 00            mov rax, qword ptr [rbx + 0xf0]
00C1B92A  48 8B 88 58 0A 00 00            mov rcx, qword ptr [rax + 0xa58]
00C1B931  48 89 0D 20 37 2E 00            mov qword ptr [rip + 0x2e3720], rcx
00C1B938  48 8D 0D 01 37 2E 00            lea rcx, [rip + 0x2e3701]
00C1B93F  E8 30 CA 80 FF                  call 0x140428374
00C1B944  44 38 2D F6 5E 5E 00            cmp byte ptr [rip + 0x5e5ef6], r13b
00C1B94B  74 55                           je 0x140c1b9a2
00C1B94D  44 8A 05 EE 5E 5E 00            mov r8b, byte ptr [rip + 0x5e5eee]
00C1B954  45 84 C4                        test r12b, r8b
00C1B957  74 24                           je 0x140c1b97d
00C1B959  44 38 2D 7C BC 32 00            cmp byte ptr [rip + 0x32bc7c], r13b
00C1B960  74 1B                           je 0x140c1b97d
00C1B962  44 38 2D 74 BC 32 00            cmp byte ptr [rip + 0x32bc74], r13b
00C1B969  75 12                           jne 0x140c1b97d
00C1B96B  41 80 E0 FD                     and r8b, 0xfd
00C1B96F  44 88 3D 60 B2 3A 00            mov byte ptr [rip + 0x3ab260], r15b
00C1B976  44 88 05 C5 5E 5E 00            mov byte ptr [rip + 0x5e5ec5], r8b
00C1B97D  B9 A2 06 00 00                  mov ecx, 0x6a2
00C1B982  0F 32                           rdmsr
00C1B984  48 C1 E2 20                     shl rdx, 0x20
00C1B988  48 0B C2                        or rax, rdx
00C1B98B  45 84 C0                        test r8b, r8b
00C1B98E  75 06                           jne 0x140c1b996
00C1B990  48 83 E0 FD                     and rax, 0xfffffffffffffffd
00C1B994  EB 03                           jmp 0x140c1b999
00C1B996  49 0B C4                        or rax, r12
00C1B999  48 8B D0                        mov rdx, rax
00C1B99C  48 C1 EA 20                     shr rdx, 0x20
00C1B9A0  0F 30                           wrmsr
00C1B9A2  E8 61 92 02 00                  call 0x140c44c08
00C1B9A7  E8 E4 67 9C FF                  call 0x1405e2190
00C1B9AC  48 F7 05 D1 B0 3A 00 00 00 04 00  test qword ptr [rip + 0x3ab0d1], 0x40000
00C1B9B7  74 11                           je 0x140c1b9ca
00C1B9B9  45 33 C0                        xor r8d, r8d
00C1B9BC  48 8D 0D 1D 3C 04 00            lea rcx, [rip + 0x43c1d]
00C1B9C3  33 D2                           xor edx, edx
00C1B9C5  E8 76 83 68 FF                  call 0x1402a3d40
00C1B9CA  48 8B CB                        mov rcx, rbx
00C1B9CD  E8 AE 83 96 FF                  call 0x140583d80
00C1B9D2  48 8B 83 F0 00 00 00            mov rax, qword ptr [rbx + 0xf0]
00C1B9D9  81 38 30 11 00 00               cmp dword ptr [rax], 0x1130
00C1B9DF  72 08                           jb 0x140c1b9e9
00C1B9E1  48 8B CB                        mov rcx, rbx
00C1B9E4  E8 3F 72 03 00                  call 0x140c52c28
00C1B9E9  48 8B CB                        mov rcx, rbx
00C1B9EC  E8 E7 53 03 00                  call 0x140c50dd8
00C1B9F1  48 8B 05 10 96 3A 00            mov rax, qword ptr [rip + 0x3a9610]
00C1B9F8  41 BC 00 00 00 80               mov r12d, 0x80000000
00C1B9FE  C7 80 B4 02 00 00 FF FF FE 7F   mov dword ptr [rax + 0x2b4], 0x7ffeffff
00C1BA08  48 8B 05 F9 95 3A 00            mov rax, qword ptr [rip + 0x3a95f9]
00C1BA0F  44 89 A0 B8 02 00 00            mov dword ptr [rax + 0x2b8], r12d
00C1BA16  44 39 2D A3 87 3A 00            cmp dword ptr [rip + 0x3a87a3], r13d
00C1BA1D  0F 84 3A 01 00 00               je 0x140c1bb5d
00C1BA23  45 33 C0                        xor r8d, r8d
00C1BA26  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00C1BA2B  41 B9 87 00 00 40               mov r9d, 0x40000087
00C1BA31  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C1BA36  48 8D 0D C3 45 3E FF            lea rcx, [rip - 0xc1ba3d]
00C1BA3D  41 8D 50 0B                     lea edx, [r8 + 0xb]
00C1BA41  E8 DA F7 D7 FF                  call 0x14099b220
00C1BA46  85 C0                           test eax, eax
00C1BA48  79 18                           jns 0x140c1ba62
00C1BA4A  45 33 C9                        xor r9d, r9d
00C1BA4D  48 63 D0                        movsxd rdx, eax
00C1BA50  4C 8B C7                        mov r8, rdi
00C1BA53  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1BA58  41 8D 49 31                     lea ecx, [r9 + 0x31]
00C1BA5C  E8 FF 1B 8E FF                  call 0x1404fd660
00C1BA61  CC                              int3
00C1BA62  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
00C1BA67  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00C1BA6C  48 03 D7                        add rdx, rdi
00C1BA6F  E8 CC 54 85 FF                  call 0x140470f40
00C1BA74  B8 FE FF 00 00                  mov eax, 0xfffe
00C1BA79  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
00C1BA7E  66 01 44 24 48                  add word ptr [rsp + 0x48], ax
00C1BA83  4C 8D 05 66 D1 05 00            lea r8, [rip + 0x5d166]
00C1BA8A  8B 05 30 87 3A 00               mov eax, dword ptr [rip + 0x3a8730]
00C1BA90  0F B6 C8                        movzx ecx, al
00C1BA93  8D 41 40                        lea eax, [rcx + 0x40]
00C1BA96  F7 D9                           neg ecx
00C1BA98  48 8D 4D 10                     lea rcx, [rbp + 0x10]
00C1BA9C  1B D2                           sbb edx, edx
00C1BA9E  23 D0                           and edx, eax
00C1BAA0  0F B6 05 1A 87 3A 00            movzx eax, byte ptr [rip + 0x3a871a]
00C1BAA7  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
00C1BAAB  49 8B D6                        mov rdx, r14
00C1BAAE  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00C1BAB2  E8 55 01 92 FF                  call 0x14053bc0c
00C1BAB7  85 C0                           test eax, eax
00C1BAB9  79 19                           jns 0x140c1bad4
00C1BABB  45 33 C9                        xor r9d, r9d
00C1BABE  48 63 D0                        movsxd rdx, eax
00C1BAC1  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1BAC6  41 8D 49 31                     lea ecx, [r9 + 0x31]
00C1BACA  45 8D 41 05                     lea r8d, [r9 + 5]
00C1BACE  E8 8D 1B 8E FF                  call 0x1404fd660
00C1BAD3  CC                              int3
00C1BAD4  F7 05 E2 86 3A 00 00 00 FF FF   test dword ptr [rip + 0x3a86e2], 0xffff0000
00C1BADE  0F 84 ED 00 00 00               je 0x140c1bbd1
00C1BAE4  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00C1BAE9  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
00C1BAEE  4C 8D 4C 24 68                  lea r9, [rsp + 0x68]
00C1BAF3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C1BAF8  48 8D 4D 10                     lea rcx, [rbp + 0x10]
00C1BAFC  E8 57 00 92 FF                  call 0x14053bb58
00C1BB01  85 C0                           test eax, eax
00C1BB03  79 19                           jns 0x140c1bb1e
00C1BB05  45 33 C9                        xor r9d, r9d
00C1BB08  48 63 D0                        movsxd rdx, eax
00C1BB0B  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1BB10  41 8D 49 31                     lea ecx, [r9 + 0x31]
00C1BB14  45 8D 41 06                     lea r8d, [r9 + 6]
00C1BB18  E8 43 1B 8E FF                  call 0x1404fd660
00C1BB1D  CC                              int3
00C1BB1E  44 0F B7 0D 9C 86 3A 00         movzx r9d, word ptr [rip + 0x3a869c]
00C1BB26  4C 8D 05 E3 D0 05 00            lea r8, [rip + 0x5d0e3]
00C1BB2D  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
00C1BB32  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00C1BB37  E8 D0 00 92 FF                  call 0x14053bc0c
00C1BB3C  85 C0                           test eax, eax
00C1BB3E  0F 89 8D 00 00 00               jns 0x140c1bbd1
00C1BB44  45 33 C9                        xor r9d, r9d
00C1BB47  48 63 D0                        movsxd rdx, eax
00C1BB4A  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1BB4F  41 8D 49 31                     lea ecx, [r9 + 0x31]
00C1BB53  45 8D 41 07                     lea r8d, [r9 + 7]
00C1BB57  E8 04 1B 8E FF                  call 0x1404fd660
00C1BB5C  CC                              int3
00C1BB5D  45 33 C9                        xor r9d, r9d
00C1BB60  48 8D 4D 10                     lea rcx, [rbp + 0x10]
00C1BB64  49 8B D6                        mov rdx, r14
00C1BB67  E8 6C 03 92 FF                  call 0x14053bed8
00C1BB6C  44 8B C0                        mov r8d, eax
00C1BB6F  85 C0                           test eax, eax
00C1BB71  0F 88 D8 02 00 00               js 0x140c1be4f
00C1BB77  4C 8D 0D A2 D0 05 00            lea r9, [rip + 0x5d0a2]
00C1BB7E  4C 89 6C 24 70                  mov qword ptr [rsp + 0x70], r13
00C1BB83  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
00C1BB88  49 8B D6                        mov rdx, r14
00C1BB8B  48 8D 4D 10                     lea rcx, [rbp + 0x10]
00C1BB8F  E8 AC C5 82 FF                  call 0x140448140
00C1BB94  49 8B CE                        mov rcx, r14
00C1BB97  44 8B C0                        mov r8d, eax
00C1BB9A  48 2B 4C 24 70                  sub rcx, qword ptr [rsp + 0x70]
00C1BB9F  41 03 C4                        add eax, r12d
00C1BBA2  41 85 C4                        test r12d, eax
00C1BBA5  75 10                           jne 0x140c1bbb7
00C1BBA7  41 81 F8 05 00 00 80            cmp r8d, 0x80000005
00C1BBAE  74 07                           je 0x140c1bbb7
00C1BBB0  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00C1BBB5  EB 05                           jmp 0x140c1bbbc
00C1BBB7  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00C1BBBC  45 85 C0                        test r8d, r8d
00C1BBBF  0F 88 8E 02 00 00               js 0x140c1be53
00C1BBC5  66 44 2B F1                     sub r14w, cx
00C1BBC9  66 44 89 35 E1 85 3A 00         mov word ptr [rip + 0x3a85e1], r14w
00C1BBD1  48 8D 55 10                     lea rdx, [rbp + 0x10]
00C1BBD5  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00C1BBDA  E8 61 53 85 FF                  call 0x140470f40
00C1BBDF  45 8A C7                        mov r8b, r15b
00C1BBE2  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00C1BBE7  48 8D 0D C2 85 3A 00            lea rcx, [rip + 0x3a85c2]
00C1BBEE  E8 AD 02 CF FF                  call 0x14090bea0
00C1BBF3  85 C0                           test eax, eax
00C1BBF5  79 19                           jns 0x140c1bc10
00C1BBF7  45 33 C9                        xor r9d, r9d
00C1BBFA  48 63 D0                        movsxd rdx, eax
00C1BBFD  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1BC02  41 8D 49 31                     lea ecx, [r9 + 0x31]
00C1BC06  45 8D 41 09                     lea r8d, [r9 + 9]
00C1BC0A  E8 51 1A 8E FF                  call 0x1404fd660
00C1BC0F  CC                              int3
00C1BC10  41 B9 06 00 00 00               mov r9d, 6
00C1BC16  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
00C1BC1E  4C 8D 05 0B D0 05 00            lea r8, [rip + 0x5d00b]
00C1BC25  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00C1BC29  45 8D 79 3A                     lea r15d, [r9 + 0x3a]
00C1BC2D  41 8B D7                        mov edx, r15d
00C1BC30  E8 D7 FF 91 FF                  call 0x14053bc0c
00C1BC35  85 C0                           test eax, eax
00C1BC37  79 19                           jns 0x140c1bc52
00C1BC39  48 63 D0                        movsxd rdx, eax
00C1BC3C  41 8D 4F F1                     lea ecx, [r15 - 0xf]
00C1BC40  45 33 C9                        xor r9d, r9d
00C1BC43  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1BC48  45 8D 47 CA                     lea r8d, [r15 - 0x36]
00C1BC4C  E8 0F 1A 8E FF                  call 0x1404fd660
00C1BC51  CC                              int3
00C1BC52  48 8D 55 D0                     lea rdx, [rbp - 0x30]
00C1BC56  48 8D 0D 73 85 3A 00            lea rcx, [rip + 0x3a8573]
00C1BC5D  E8 2E FD B6 FF                  call 0x14078b990
00C1BC62  84 C0                           test al, al
00C1BC64  0F 84 01 02 00 00               je 0x140c1be6b
00C1BC6A  F7 05 4C 86 3A 00 00 20 00 00   test dword ptr [rip + 0x3a864c], 0x2000
00C1BC74  BE 00 00 80 00                  mov esi, 0x800000
00C1BC79  74 50                           je 0x140c1bccb
00C1BC7B  0F 57 C0                        xorps xmm0, xmm0
00C1BC7E  33 C0                           xor eax, eax
00C1BC80  41 BE 53 74 61 63               mov r14d, 0x63617453
00C1BC86  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
00C1BC8A  45 8B C6                        mov r8d, r14d
00C1BC8D  8B D6                           mov edx, esi
00C1BC8F  49 8B CF                        mov rcx, r15
00C1BC92  0F 11 45 88                     movups xmmword ptr [rbp - 0x78], xmm0
00C1BC96  E8 55 64 F6 FF                  call 0x140b820f0
00C1BC9B  48 8B F8                        mov rdi, rax
00C1BC9E  48 85 C0                        test rax, rax
00C1BCA1  74 28                           je 0x140c1bccb
00C1BCA3  44 8B C6                        mov r8d, esi
00C1BCA6  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00C1BCAA  8B D6                           mov edx, esi
00C1BCAC  48 89 75 90                     mov qword ptr [rbp - 0x70], rsi
00C1BCB0  48 8B C8                        mov rcx, rax
00C1BCB3  48 89 75 98                     mov qword ptr [rbp - 0x68], rsi
00C1BCB7  E8 4C 0C B7 FF                  call 0x14078c908
00C1BCBC  85 C0                           test eax, eax
00C1BCBE  79 0B                           jns 0x140c1bccb
00C1BCC0  41 8B D6                        mov edx, r14d
00C1BCC3  48 8B CF                        mov rcx, rdi
00C1BCC6  E8 A5 6B F6 FF                  call 0x140b82870
00C1BCCB  85 35 EF 85 3A 00               test dword ptr [rip + 0x3a85ef], esi
00C1BCD1  74 38                           je 0x140c1bd0b
00C1BCD3  BF 20 16 01 00                  mov edi, 0x11620
00C1BCD8  41 B8 45 64 62 67               mov r8d, 0x67626445
00C1BCDE  8B D7                           mov edx, edi
00C1BCE0  49 8B CF                        mov rcx, r15
00C1BCE3  E8 08 64 F6 FF                  call 0x140b820f0
00C1BCE8  48 89 05 01 BE 24 00            mov qword ptr [rip + 0x24be01], rax
00C1BCEF  48 85 C0                        test rax, rax
00C1BCF2  74 17                           je 0x140c1bd0b
00C1BCF4  44 8B C7                        mov r8d, edi
00C1BCF7  33 D2                           xor edx, edx
00C1BCF9  48 8B C8                        mov rcx, rax
00C1BCFC  E8 3F AF AA FF                  call 0x1406c6c40
00C1BD01  C7 05 91 9F 2E 00 32 00 00 00   mov dword ptr [rip + 0x2e9f91], 0x32
00C1BD0B  48 8D 05 B6 E2 3B 00            lea rax, [rip + 0x3be2b6]
00C1BD12  4C 89 2D 87 DE 3B 00            mov qword ptr [rip + 0x3bde87], r13
00C1BD19  48 89 05 B0 E2 3B 00            mov qword ptr [rip + 0x3be2b0], rax
00C1BD20  48 89 05 A1 E2 3B 00            mov qword ptr [rip + 0x3be2a1], rax
00C1BD27  E8 74 0C 89 FF                  call 0x1404ac9a0
00C1BD2C  33 C9                           xor ecx, ecx
00C1BD2E  89 05 E4 DD 3B 00               mov dword ptr [rip + 0x3bdde4], eax
00C1BD34  E8 43 5F 05 00                  call 0x140c71c7c
00C1BD39  84 C0                           test al, al
00C1BD3B  75 0B                           jne 0x140c1bd48
00C1BD3D  B9 5E 00 00 00                  mov ecx, 0x5e
00C1BD42  E8 F9 18 8E FF                  call 0x1404fd640
00C1BD47  CC                              int3
00C1BD48  BA 0C 00 00 00                  mov edx, 0xc
00C1BD4D  8D 4A 5B                        lea ecx, [rdx + 0x5b]
00C1BD50  48 FF 15 D9 59 53 FF            call qword ptr [rip - 0xaca627]
00C1BD57  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00C1BD5C  E8 EB E9 02 00                  call 0x140c4a74c
00C1BD61  84 C0                           test al, al
00C1BD63  75 0B                           jne 0x140c1bd70
00C1BD65  B9 5F 00 00 00                  mov ecx, 0x5f
00C1BD6A  E8 D1 18 8E FF                  call 0x1404fd640
00C1BD6F  CC                              int3
00C1BD70  48 8B D3                        mov rdx, rbx
00C1BD73  33 C9                           xor ecx, ecx
00C1BD75  E8 DE 2F FD FF                  call 0x140beed58
00C1BD7A  84 C0                           test al, al
00C1BD7C  0F 84 C2 00 00 00               je 0x140c1be44
00C1BD82  E8 5D A4 00 00                  call 0x140c261e4
00C1BD87  85 C0                           test eax, eax
00C1BD89  0F 88 B5 00 00 00               js 0x140c1be44
00C1BD8F  E8 D0 6B 01 00                  call 0x140c32964
00C1BD94  84 C0                           test al, al
00C1BD96  75 0B                           jne 0x140c1bda3
00C1BD98  B9 8F 00 00 00                  mov ecx, 0x8f
00C1BD9D  E8 9E 18 8E FF                  call 0x1404fd640
00C1BDA2  CC                              int3
00C1BDA3  48 8B 05 5E 92 3A 00            mov rax, qword ptr [rip + 0x3a925e]
00C1BDAA  C7 80 6C 02 00 00 0A 00 00 00   mov dword ptr [rax + 0x26c], 0xa
00C1BDB4  48 8B 05 4D 92 3A 00            mov rax, qword ptr [rip + 0x3a924d]
00C1BDBB  44 89 A8 70 02 00 00            mov dword ptr [rax + 0x270], r13d
00C1BDC2  48 8B 05 3F 92 3A 00            mov rax, qword ptr [rip + 0x3a923f]
00C1BDC9  C7 80 60 02 00 00 F4 65 00 00   mov dword ptr [rax + 0x260], 0x65f4
00C1BDD3  48 8B 0D 2E 92 3A 00            mov rcx, qword ptr [rip + 0x3a922e]
00C1BDDA  0F B7 05 97 92 3A 00            movzx eax, word ptr [rip + 0x3a9297]
00C1BDE1  66 89 81 6A 02 00 00            mov word ptr [rcx + 0x26a], ax
00C1BDE8  B9 64 86 00 00                  mov ecx, 0x8664
00C1BDED  48 8B 05 14 92 3A 00            mov rax, qword ptr [rip + 0x3a9214]
00C1BDF4  66 89 48 2C                     mov word ptr [rax + 0x2c], cx
00C1BDF8  48 8B 05 09 92 3A 00            mov rax, qword ptr [rip + 0x3a9209]
00C1BDFF  66 89 48 2E                     mov word ptr [rax + 0x2e], cx
00C1BE03  48 8B 05 FE 91 3A 00            mov rax, qword ptr [rip + 0x3a91fe]
00C1BE0A  44 89 A8 A4 03 00 00            mov dword ptr [rax + 0x3a4], r13d
00C1BE11  33 C0                           xor eax, eax
00C1BE13  48 8B 8D 10 01 00 00            mov rcx, qword ptr [rbp + 0x110]
00C1BE1A  48 33 CC                        xor rcx, rsp
00C1BE1D  E8 1E 08 A9 FF                  call 0x1406ac640
00C1BE22  4C 8D 9C 24 20 02 00 00         lea r11, [rsp + 0x220]
00C1BE2A  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00C1BE2E  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00C1BE32  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00C1BE36  49 8B E3                        mov rsp, r11
00C1BE39  41 5F                           pop r15
00C1BE3B  41 5E                           pop r14
00C1BE3D  41 5D                           pop r13
00C1BE3F  41 5C                           pop r12
00C1BE41  5D                              pop rbp
00C1BE42  C3                              ret
00C1BE43  CC                              int3
00C1BE44  B9 60 00 00 00                  mov ecx, 0x60
00C1BE49  E8 F2 17 8E FF                  call 0x1404fd640
00C1BE4E  CC                              int3
00C1BE4F  44 88 6D 10                     mov byte ptr [rbp + 0x10], r13b
00C1BE53  45 33 C9                        xor r9d, r9d
00C1BE56  49 63 D0                        movsxd rdx, r8d
00C1BE59  4C 8B C6                        mov r8, rsi
00C1BE5C  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00C1BE61  41 8D 49 31                     lea ecx, [r9 + 0x31]
00C1BE65  E8 F6 17 8E FF                  call 0x1404fd660
00C1BE6A  CC                              int3
00C1BE6B  B9 31 00 00 00                  mov ecx, 0x31
00C1BE70  E8 CB 17 8E FF                  call 0x1404fd640
00C1BE75  CC                              int3
00C1BE76  41 8B C5                        mov eax, r13d
00C1BE79  BF 04 00 00 00                  mov edi, 4
00C1BE7E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C1BE83  48 8B CB                        mov rcx, rbx
00C1BE86  B9 00 01 00 00                  mov ecx, 0x100
00C1BE8B  44 8B 04 3B                     mov r8d, dword ptr [rbx + rdi]
00C1BE8F  8D 77 04                        lea esi, [rdi + 4]
00C1BE92  44 8B 0C 33                     mov r9d, dword ptr [rbx + rsi]
00C1BE96  E8 C5 17 8E FF                  call 0x1404fd660
00C1BE9B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall InitBootProcessor(__int64 a1)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rsp;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned int v_stack_m218;
    unsigned int v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m28;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (544);
    result = (*(unsigned __int64 *)(v_rip + 2028875)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 328 + 272) = result;
    v_r13 = 0;
    *(unsigned __int64 *)(v_rip + 3886065) = v_rip + 3888435;
    *(unsigned int *)(v_rip + 3886087) = 259;
    *(unsigned __int16 *)(v_rip + 3885832) = (unsigned __int16)((unsigned int)(0xFDE9ULL));
    *(unsigned int *)(v_rip + 3886065) = (unsigned int)(v_r13 + 1);
    *(unsigned __int16 *)(v_rip + 3885882) = (unsigned __int16)((unsigned int)(0xFDE9ULL));
    *(unsigned int *)(v_rip + 3886116) = (unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rip + 2028847))));
    v_stack_m1E8 = 0;
    v_stack_m1F0 = 0;
    v_stack_m210 = 0;
    v_stack_m200 = v_xmm0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1)))) != 10) goto loc_00C1BE76;
    if ((*(unsigned int *)(a1 + 4)) != 0) goto loc_00C1BE76;
    if ((*(unsigned int *)(a1 + 8)) != 368) goto loc_00C1BE76;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 240))))) != 0x1130ULL) goto loc_00C1BE79;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 2984)) != 0xA000010ULL) goto loc_00C1BE79;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3841357) + 708) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 2900)));
    result = ExpInitLicensing(v_rip + 3884664, (unsigned int)(*(unsigned int *)(a1)), a3, a4);
    result = RtlNlsInitState(v_rip + 3884652, (unsigned int)(*(unsigned int *)(a1)), a3, a4);
    a1 = 0;
    result = VslGetNestedPageProtectionFlags(a1, (unsigned int)(*(unsigned int *)(a1)), a3, a4);
    result = (unsigned int)((result) & (6));
    if (((unsigned __int8)(result)) != 6) goto loc_00C1B339;
    *(unsigned __int64 *)(v_rsp - 328 - 88) = 0;
    *(unsigned __int64 *)(v_rsp - 328 - 96) = 0;
loc_00C1B2FA:
    if ((*(unsigned __int64 *)(a1 + 32)) == (a1 + 32)) goto loc_00C1B333;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 24)) != ((unsigned int)(v_r13 + 4))) goto loc_00C1B32E;
    v_r12 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32) - 1) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 40));
    goto loc_00C1B329;
loc_00C1B312:
    a2 = 0;
    result = KeSetPagePrivilege(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32), a2, v_rsp - 328 - 96, 16);
    v_r14 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32)) + 1;
loc_00C1B329:
    if (v_r14 <= v_r12) goto loc_00C1B312;
loc_00C1B32E:
    goto loc_00C1B2FA;
loc_00C1B333:
loc_00C1B339:
    *(unsigned int *)(v_rip + 3837529) = 0;
    if (*(unsigned __int64 *)(a1 + 216) == 0) goto loc_00C1B3B4;
    result = strupr(*(unsigned __int64 *)(a1 + 216), a2, v_rsp - 328 - 96, 16);
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip + 383077, v_rsp - 328 - 96, 16);
    if (result == 0) goto loc_00C1B399;
    result = strstr(result, v_rip + 383073, v_rsp - 328 - 96, 16);
    if (result == 0) goto loc_00C1B399;
    result = atol(result + 1, v_rip + 383073, v_rsp - 328 - 96, 16);
    a2 = ((int)((unsigned int)(result))) << (8);
    if (a2 != 0) {
        a1 = 0;
        result = ExBurnMemory(a1, a2, v_rsp - 328 - 96, 16);
    }
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip + 383040, v_rsp - 328 - 96, 16);
    if (result != 0) {
        *(unsigned __int8 *)(v_rip + 3847998) = 1;
    }
loc_00C1B3BE:
    if ((*(unsigned __int64 *)(a1 + 32)) == (a1 + 32)) goto loc_00C1B3E9;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32)) < 0) goto loc_00C1B3D9;
    goto loc_00C1B3BE;
loc_00C1B3D9:
    v_stack_m228 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32) + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 40) * 1;
    result = KeBugCheckEx(49, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 40));
loc_00C1B3E9:
    result = *(unsigned __int64 *)(a1 + 224);
    if (*(unsigned __int64 *)(a1 + 224) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 16);
        *(unsigned __int64 *)(v_rip + 4115856) = result;
        result = ExPreInitializeNls(49, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 40));
    }
    *(unsigned __int64 *)(v_rip + 3029534) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 2976);
    result = WheaInitializeServices(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 2976), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 40));
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rip + 2013435), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 40));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32))) << (32);
    result = (result) | (a2);
    *(unsigned __int64 *)(v_rip + 4117421) = result;
    result = HalInitSystem((unsigned int)(*(unsigned int *)(v_rip + 3837286)), a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 40));
    if ((unsigned __int8)(result) == 0) {
        a1 = 92;
        result = KeBugCheck(a1, a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 40));
    }
    a2 = (a1) << (32);
    result = (result) | (a2);
    *(unsigned __int64 *)(v_rip + 4117384) = result;
    result = KeInitializeClock((unsigned int)(*(unsigned int *)(v_rip + 3837241)), a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 40));
    result = PsInitializeQuotaSystem(1, a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 40));
    result = CmInitSystem0(a1, a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 40));
    if ((*(unsigned __int8 *)(v_rip + 3095356)) == 0) {
        result = *(unsigned __int64 *)(v_rip + 3856291);
        a1 = *(unsigned __int64 *)(result + 24);
    }
    a1 = 0;
    result = KeInitSystem(a1, a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 40));
    if ((unsigned __int8)(result) == 0) {
        a4 = 0;
        v_stack_m228 = 0;
        a2 = 0xFFFFFFFFC0000001ULL;
        a1 = a4 + 49;
        a3 = a4 + 11;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    a2 = (unsigned int)((a2) >> (13));
    result = (unsigned int)(((unsigned int)(0xD1B71759ULL)) * ((unsigned int)(a2)));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3847627))) - ((unsigned int)(result)));
loc_00C1B4F8:
    a3 = (unsigned int)((a3) + ((unsigned int)(a3)));
    a4 = (unsigned int)((0) + (0));
    a4 = (unsigned int)((a4) | (1));
    if (((unsigned int)(a3)) < ((unsigned int)((unsigned int)(0x2710ULL)))) { a4 = (unsigned int)((unsigned int)((unsigned int)(a4))); }
    a3 = (unsigned int)((a3) + (0xFFFFD8F0ULL));
    if (((unsigned int)((unsigned int)((unsigned int)(a3)))) < ((unsigned int)((unsigned int)(0x2710ULL)))) { a3 = (unsigned int)((unsigned int)((unsigned int)(a3))); }
    v_r10 = (24) - (1);
    if (condition_is_not_equal) goto loc_00C1B4F8;
    a2 = (unsigned int)((a2) << (24));
    a2 = (unsigned int)((a2) | ((unsigned int)(a4)));
    v_stack_m208 = 0;
    *(unsigned int *)(v_rip + 3029105) = (unsigned int)(a2);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3840733) + 4) = (unsigned int)(a2);
    v_stack_m218 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3840686) + 572) = 0;
    *(unsigned __int64 *)(v_rsp - 328 - 80) = 11;
    *(unsigned __int64 *)(v_rsp - 328 - 72) = 1;
    *(unsigned __int64 *)(v_rsp - 328 - 64) = 0;
    result = LdrFindResource_U(v_rip - 12694841, v_rsp - 328 - 80, v_r10 + 3, v_stack_m1F0);
    if (sign_flag) goto loc_00C1B5AA;
    result = LdrAccessResource(v_rip - 12694933, v_stack_m1F0, v_stack_m208, v_stack_m218);
    if (!(sign_flag)) {
        result = v_stack_m208;
        *(unsigned __int64 *)(v_rip + 3848270) = result;
    }
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3840583) + 600) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4116794)));
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3840570) + 651) = 1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3836785))) & (0xFFFULL));
    *(unsigned __int16 *)(v_rip + 3836890) = 0;
    *(unsigned int *)(v_rip + 3836759) = (unsigned int)(result);
    if ((*(unsigned int *)(v_rip + 3837141)) != 0) {
        result = (unsigned int)((result) << (16));
    }
    if ((*(unsigned int *)(v_rip + 4115318)) != ((unsigned int)(v_r13 + 4))) goto loc_00C1B610;
    if ((*(unsigned int *)(v_rip + 4115306)) != ((unsigned int)(v_r13 + 4))) {
        *(unsigned int *)(v_rip + 4116613) = 0;
    }
    result = (unsigned int)(*(unsigned int *)(v_rip + 4116607));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4116607))) != 0) {
        result = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_rip + 4116607))));
        a2 = 1;
        a1 = (*(unsigned __int64 *)(v_rip + 3840583)) * (result);
        result = KeAdjustInterruptTime(a1, a2, v_stack_m208, v_stack_m218);
        a1 = 0;
        result = KeQueryPerformanceCounter(a1, a2, v_stack_m208, v_stack_m218);
        a1 = *(unsigned __int64 *)(v_rip + 3840456);
        *(unsigned __int64 *)(a1 + 840) = result;
        *(unsigned __int64 *)(v_rip + 2404978) = 0;
    }
    a1 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3840409) + 960) = 1;
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 3840395) + 964) = 1;
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3840381) + 874) = 1;
    result = ExInitSystem(a1, a2, v_stack_m208, v_stack_m218);
    if ((unsigned __int8)(result) == 0) goto loc_00C1BE6B;
    *(unsigned __int64 *)(v_rip + 3009097) = 0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3704) == 0) goto loc_00C1B6F5;
    result = IpmiHwInitializeContext(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3704), a2, v_stack_m208, v_stack_m218);
    if (sign_flag) goto loc_00C1B6F5;
    result = WheaSelLogSetNtSchedulerAvailability(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3704), a2, v_stack_m208, v_stack_m218);
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 132)) & (0x80000ULL)) != 0) {
        result = *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 240) + 2648);
        a1 = 5;
        result = (unsigned __int8)((result) & ((unsigned __int8)(v_r13 + 4)));
        result = (unsigned __int8)(-(result));
        a2 = (unsigned int)((a2) & (3));
        result = WheaSelLogCheckPoint(a1, a2, v_stack_m208, v_stack_m218);
    }
    result = KeNumaInitialize(a1, a2, v_stack_m208, v_stack_m218);
    result = VerifierInitSystem(a1, a2, v_stack_m208, v_stack_m218);
    result = InitializeDynamicPartitioningPolicy(a1, a2, v_stack_m208, v_stack_m218);
    result = KeInitializeXSaveStructures(a1, a2, v_stack_m208, v_stack_m218);
    *(unsigned __int64 *)(v_rip + 3176323) = 0x200001ULL;
    a2 = 0;
    result = memset(v_rip + 3176321, a2, 256, v_stack_m218);
    *(unsigned __int64 *)(v_rip + 3176556) = 0;
    a1 = 0;
    *(unsigned __int64 *)(v_rip + 3176563) = v_rip + 3176571;
    *(unsigned __int64 *)(v_rip + 3176548) = v_rip + 3176571;
    result = KeQueryPerformanceCounter(a1, a2, 256, v_stack_m218);
    *(unsigned __int64 *)(v_rip + 4116549) = result;
    a1 = 0;
    result = MmInitSystem(a1, 0, 256, v_stack_m218);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, 0, 256, v_stack_m218);
    *(unsigned __int64 *)(v_rip + 4116536) = result;
    if (*(unsigned __int64 *)(a1 + 240) == 0) goto loc_00C1B79E;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 2904) == 0) goto loc_00C1B79E;
    if (((8) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 2904)))))) != 0) {
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 4376);
    }
    a1 = (*(unsigned __int64 *)(v_rip + 3855515)) + (0x91C0ULL);
    result = symcryptk_dll_SymCryptEntropyAccumulatorInit1(a1, a2, 256, v_stack_m218);
    a1 = 0;
    result = EtwInitialize(a1, a1, 256, v_stack_m218);
    a1 = 0;
    *(unsigned __int64 *)(v_rip + 3171125) = 0;
    result = VmInitSystem(a1, a1, 256, v_stack_m218);
    if (sign_flag) {
        a4 = 0;
        a2 = (int)((unsigned int)(result));
        v_stack_m228 = 0;
        a1 = a4 + 49;
        a3 = a4 + 19;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    a1 = 0;
    result = HalInitializeBios(a1, a1, a3, a4);
    a3 = 0;
    a1 = 0;
    result = InbvDriverInitialize(a1, 0, a3, a4);
    if ((*(unsigned __int64 *)(v_rip + 3847661)) == 0) goto loc_00C1B85A;
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)((unsigned int)(v_stack_m218))), (unsigned int)(0x6342694BULL), a4);
    v_stack_m208 = result;
    if (result == 0) {
        a1 = result + 125;
        result = KeBugCheck(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m218))), (unsigned int)(0x6342694BULL), a4);
    }
    result = memcpy(result, *(unsigned __int64 *)(v_rip + 3847606), (unsigned int)(v_stack_m218), a4);
    *(unsigned __int64 *)(v_rip + 3847588) = result;
loc_00C1B85A:
    if ((*(unsigned int *)(a1 + 12)) < 2) {
        *(unsigned int *)(v_rip + 2402379) = 0;
        a4 = 0;
        a2 = *(unsigned int *)(a1 + 12);
        a3 = 2;
        a1 = 406;
        v_stack_m228 = 0;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 328 - 128) = 0;
    v_stack_m1D0 = a1;
    result = MiEnumerateSystemImages(v_rip + 1554, v_stack_m1D0, a3, a4);
    if ((*(unsigned __int8 *)(v_rip + 3400735)) != 0) {
        a1 = 1;
        result = DbgBreakPointWithStatus(a1, v_stack_m1D0, a3, a4);
    }
    a1 = -(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36536));
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 3846675)) & (253));
    a2 = (unsigned __int8)((v_stack_m1D0) & (2));
    a2 = (unsigned __int8)((a2) | ((unsigned __int8)(result)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3846620))) >> (28));
    a2 = (unsigned __int8)((a2) & (251));
    result = (unsigned __int8)((result) & ((unsigned __int8)(v_r13 + 4)));
    result = (unsigned __int8)((result) | (1));
    a2 = (unsigned __int8)((a2) | ((unsigned __int8)(result)));
    *(unsigned __int8 *)(v_rip + 3846637) = (unsigned __int8)(a2);
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 264)) & (1));
    result = (unsigned __int8)(-(result));
    a1 = (unsigned int)(-(a1));
    a1 = (unsigned int)((a1) + (1));
    *(unsigned int *)(v_rip + 3028803) = (unsigned int)(a1);
    *(unsigned __int64 *)(v_rip + 3028765) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 3028768) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 2648);
    result = IoAddTriageDumpDataBlock(v_rip + 3028737, 32, a3, a4);
    if ((*(unsigned __int8 *)(v_rip + 6184694)) == 0) goto loc_00C1B9A2;
    if (((2) & ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 6184686)))) == 0) goto loc_00C1B97D;
    if ((*(unsigned __int8 *)(v_rip + 3325052)) == 0) goto loc_00C1B97D;
    if ((*(unsigned __int8 *)(v_rip + 3325044)) == 0) {
        a3 = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 6184686)) & (253));
        *(unsigned __int8 *)(v_rip + 3846752) = 1;
        *(unsigned __int8 *)(v_rip + 6184645) = (unsigned __int8)(a3);
    }
    a2 = (32) << (32);
    result = (result) | (a2);
    if ((unsigned __int8)(a3) != 0) goto loc_00C1B996;
    result = (result) & (-3);
    goto loc_00C1B999;
loc_00C1B996:
    result = (result) | (2);
loc_00C1B999:
    a2 = (result) >> (32);
loc_00C1B9A2:
    result = PsInitializeWin32kServiceTable((unsigned int)(0x6A2ULL), a2, a3, a4);
    result = PsInitializeWin32kKernelExports((unsigned int)(0x6A2ULL), a2, a3, a4);
    if (((*(unsigned __int64 *)(v_rip + 3846353)) & (0x40000ULL)) != 0) {
        a3 = 0;
        a1 = v_rip + 277533;
        a2 = 0;
        result = MiEnumerateSystemImages(a1, a2, a3, a4);
    }
    result = HvlPhase1Initialize(a1, a2, a3, a4);
    result = *(unsigned __int64 *)(a1 + 240);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 240))) >= 0x1130ULL) {
        a1 = a1;
        result = HeadlessInit(a1, a2, a3, a4);
    }
    result = BootApplicationPersistentDataInitialize(a1, a2, a3, a4);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3839504) + 692) = 0x7FFEFFFFULL;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3839481) + 696) = (unsigned int)((unsigned int)(0x80000000ULL));
    if ((*(unsigned int *)(v_rip + 3835811)) == 0) goto loc_00C1BB5D;
    a3 = 0;
    v_stack_m228 = v_stack_m1E8;
    result = RtlFindMessage(v_rip - 12696125, a3 + 11, a3, (unsigned int)(0x40000087ULL));
    if (sign_flag) {
        a4 = 0;
        a2 = (int)((unsigned int)(result));
        a3 = v_r13 + 4;
        v_stack_m228 = 0;
        a1 = a4 + 49;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    a2 = (v_stack_m1E8) + (v_r13 + 4);
    result = RtlInitAnsiString(v_stack_m200, a2, a3, a4);
    a1 = (unsigned int)(-((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 3835696)))));
    a2 = (unsigned int)((a2) & ((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 3835696))) + 64)));
    v_stack_m220 = (unsigned int)(a2);
    v_stack_m228 = (unsigned int)(*(unsigned __int8 *)(v_rip + 3835674));
    result = RtlStringCbPrintfA(v_rsp - 328 + 16, 256, v_rip + 381286, v_stack_m200);
    if (sign_flag) {
        a4 = 0;
        a2 = (int)((unsigned int)(result));
        v_stack_m228 = 0;
        a1 = a4 + 49;
        a3 = a4 + 5;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (((*(unsigned int *)(v_rip + 3835618)) & (0xFFFF0000ULL)) == 0) goto loc_00C1BBD1;
    v_stack_m1E0 = 0;
    v_stack_m228 = v_stack_m210;
    result = RtlStringCbCatExA(v_rsp - 328 + 16, a2, a3, v_stack_m1E0);
    if (sign_flag) {
        a4 = 0;
        a2 = (int)((unsigned int)(result));
        v_stack_m228 = 0;
        a1 = a4 + 49;
        a3 = a4 + 6;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = RtlStringCbPrintfA(v_stack_m1E0, v_stack_m210, v_rip + 381155, *(unsigned __int16 *)(v_rip + 3835548));
    if (!sign_flag) goto loc_00C1BBD1;
    a4 = 0;
    v_stack_m228 = 0;
    result = KeBugCheckEx(a4 + 49, (int)((unsigned int)(result)), a4 + 7, a4);
loc_00C1BB5D:
    a4 = 0;
    result = RtlStringExValidateDestA(v_rsp - 328 + 16, 256, a4 + 7, a4);
    if (sign_flag) goto loc_00C1BE4F;
    v_stack_m1D8 = 0;
    result = RtlStringCopyWorkerA(v_rsp - 328 + 16, 256, v_stack_m1D8, v_rip + 381090);
    a1 = (256) - (v_stack_m1D8);
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result))) != 0) goto loc_00C1BBB7;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0x80000005ULL) goto loc_00C1BBB7;
    goto loc_00C1BBBC;
loc_00C1BBB7:
    v_stack_m210 = v_stack_m210;
loc_00C1BBBC:
    if (sign_flag) goto loc_00C1BE53;
    v_r14 = (unsigned __int16)((256) - ((unsigned __int16)(v_stack_m210)));
    *(unsigned __int16 *)(v_rip + 3835361) = (unsigned __int16)(v_r14);
loc_00C1BBD1:
    result = RtlInitAnsiString(v_stack_m200, v_rsp - 328 + 16, (unsigned int)((unsigned int)(result)), v_rip + 381090);
    result = RtlAnsiStringToUnicodeString(v_rip + 3835330, v_stack_m200, 1, v_rip + 381090);
    if (sign_flag) {
        a4 = 0;
        a2 = (int)((unsigned int)(result));
        v_stack_m228 = 0;
        a1 = a4 + 49;
        a3 = a4 + 9;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    v_stack_m228 = 3;
    result = RtlStringCbPrintfA(v_rsp - 328 - 48, (unsigned int)((unsigned int)(6 + 58)), v_rip + 380939, 6);
    if (sign_flag) {
        a2 = (int)((unsigned int)(result));
        a1 = 6 + 58 - 15;
        a4 = 0;
        v_stack_m228 = 0;
        a3 = 6 + 58 - 54;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = RtlCreateUnicodeStringFromAsciiz(v_rip + 3835251, v_rsp - 328 - 48, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C1BE6B;
    if (((*(unsigned int *)(v_rip + 3835468)) & (0x2000ULL)) == 0) goto loc_00C1BCCB;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 328 - 104) = 0;
    *(unsigned __int64 *)(v_rsp - 328 - 120) = v_xmm0;
    result = ExAllocatePool2(6 + 58, (unsigned int)((unsigned int)((unsigned int)(0x800000ULL))), (unsigned int)((unsigned int)((unsigned int)(0x63617453ULL))), a4);
    if (result == 0) goto loc_00C1BCCB;
    *(unsigned __int64 *)(v_rsp - 328 - 120) = result;
    *(unsigned __int64 *)(v_rsp - 328 - 112) = (unsigned int)(0x800000ULL);
    *(unsigned __int64 *)(v_rsp - 328 - 104) = (unsigned int)(0x800000ULL);
    result = RtlpInitializeStackTraceDatabase(result, (unsigned int)((unsigned int)((unsigned int)(0x800000ULL))), (unsigned int)((unsigned int)((unsigned int)(0x800000ULL))), a4);
    if (sign_flag) {
        a2 = (unsigned int)((unsigned int)(0x63617453ULL));
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)((unsigned int)(0x800000ULL))), a4);
    }
    if (((*(unsigned int *)(v_rip + 3835375)) & ((unsigned int)((unsigned int)(0x800000ULL)))) == 0) goto loc_00C1BD0B;
    result = ExAllocatePool2(6 + 58, (unsigned int)((unsigned int)((unsigned int)(0x11620ULL))), (unsigned int)(0x67626445ULL), a4);
    *(unsigned __int64 *)(v_rip + 2407937) = result;
    if (result != 0) {
        a3 = (unsigned int)((unsigned int)(0x11620ULL));
        a2 = 0;
        a1 = result;
        result = memset(a1, a2, a3, a4);
        *(unsigned int *)(v_rip + 3055505) = 50;
    }
    *(unsigned __int64 *)(v_rip + 3923591) = 0;
    *(unsigned __int64 *)(v_rip + 3924656) = v_rip + 3924662;
    *(unsigned __int64 *)(v_rip + 3924641) = v_rip + 3924662;
    result = HalQueryMaximumProcessorCount(a1, a2, a3, a4);
    a1 = 0;
    *(unsigned int *)(v_rip + 3923428) = (unsigned int)(result);
    result = ObInitSystem(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        a1 = 94;
        result = KeBugCheck(a1, a2, a3, a4);
    }
    result = symcryptk_dll_SymCryptModuleInit(12 + 91, 12, a3, a4);
    result = SeInitSystem(12 + 91, 12, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        a1 = 95;
        result = KeBugCheck(a1, 12, a3, a4);
    }
    a1 = 0;
    result = PsInitSystem(a1, a1, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00C1BE44;
    result = DbgkInitialize(a1, a1, a3, a4);
    if (sign_flag) goto loc_00C1BE44;
    result = PpInitSystem(a1, a1, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        a1 = 143;
        result = KeBugCheck(a1, a1, a3, a4);
    }
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3838558) + 620) = 10;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3838541) + 624) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3838527) + 608) = 0x65F4ULL;
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3838510) + 618) = (unsigned __int16)(*(unsigned __int16 *)(v_rip + 3838615));
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3838484) + 44) = (unsigned __int16)((unsigned int)(0x8664ULL));
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 3838473) + 46) = (unsigned __int16)((unsigned int)(0x8664ULL));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3838462) + 932) = 0;
    result = 0;
    a1 = (*(unsigned __int64 *)(v_rsp - 328 + 272)) ^ (v_rsp);
    result = _security_check_cookie(a1, a1, a3, a4);
    return result;
loc_00C1BE44:
    result = KeBugCheck(96, a1, a3, a4);
loc_00C1BE4F:
    *(unsigned __int8 *)(v_rsp - 328 + 16) = 0;
loc_00C1BE53:
    a4 = 0;
    v_stack_m200 = 0;
    result = KeBugCheckEx(a4 + 49, (int)((unsigned int)(a3)), *(unsigned __int64 *)(v_stack_m28 + 64), a4);
loc_00C1BE6B:
    result = KeBugCheck(49, (int)((unsigned int)(a3)), *(unsigned __int64 *)(v_stack_m28 + 64), a4);
loc_00C1BE76:
loc_00C1BE79:
    v_stack_m200 = 0;
    result = KeBugCheckEx(256, (int)((unsigned int)(a3)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 4 * 1)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 56) + 4 + 4 * 1)));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t InitBootProcessor(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rsp;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint32_t v_stack_m218;
    uint32_t v_stack_m220;
    uint64_t v_stack_m228;
    uint64_t v_stack_m28;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (544);
    result = (*(uint64_t *)(v_rip + 0x1EF54B)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x148 + 0x110) = result;
    local_r13 = 0;
    *(uint64_t *)(v_rip + 0x3B4BF1) = v_rip + 3888435;
    *(uint32_t *)(v_rip + 0x3B4C07) = 259;
    *(uint16_t *)(v_rip + 0x3B4B08) = (uint16_t)((uint32_t)(0xFDE9ULL));
    *(uint32_t *)(v_rip + 0x3B4BF1) = (uint32_t)(local_r13 + 1);
    *(uint16_t *)(v_rip + 0x3B4B3A) = (uint16_t)((uint32_t)(0xFDE9ULL));
    *(uint32_t *)(v_rip + 0x3B4C24) = (uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1EF52F))));
    v_stack_m1E8 = 0;
    v_stack_m1F0 = 0;
    v_stack_m210 = 0;
    v_stack_m200 = v_xmm0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1)))) != 10) goto loc_00C1BE76;
    if ((*(uint32_t *)(arg1 + 0x4)) != 0) goto loc_00C1BE76;
    if ((*(uint32_t *)(arg1 + 0x8)) != 368) goto loc_00C1BE76;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0))))) != 0x1130ULL) goto loc_00C1BE79;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xBA8)) != 0xA000010ULL) goto loc_00C1BE79;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x3A9D4D) + 0x2C4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xB54)));
    result = ExpInitLicensing(v_rip + 3884664, (uint32_t)(*(uint32_t *)(arg1)), a3, a4);
    result = RtlNlsInitState(v_rip + 3884652, (uint32_t)(*(uint32_t *)(arg1)), a3, a4);
    Arg1 = 0;
    result = VslGetNestedPageProtectionFlags(Arg1, (uint32_t)(*(uint32_t *)(arg1)), a3, a4);
    result = (uint32_t)((result) & (6));
    if (((uint8_t)(result)) != 6) goto loc_00C1B339;
    *(uint64_t *)(local_rsp - 0x148 - 0x58) = 0;
    *(uint64_t *)(local_rsp - 0x148 - 0x60) = 0;
loc_00C1B2FA:
    if ((*(uint64_t *)(arg1 + 0x20)) == (Arg1 + 32)) goto loc_00C1B333;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x20) + 0x18)) != ((uint32_t)(local_r13 + 4))) goto loc_00C1B32E;
    local_r12 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20) - 1) + (*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x28));
    goto loc_00C1B329;
loc_00C1B312:
    a2 = 0;
    result = KeSetPagePrivilege(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20), a2, local_rsp - 328 - 96, 16);
    local_r14 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20)) + 1;
loc_00C1B329:
    if (local_r14 <= local_r12) goto loc_00C1B312;
loc_00C1B32E:
    goto loc_00C1B2FA;
loc_00C1B333:
loc_00C1B339:
    *(uint32_t *)(v_rip + 0x3A8E59) = 0;
    if (*(uint64_t *)(arg1 + 0xD8) == 0) goto loc_00C1B3B4;
    result = strupr(*(uint64_t *)(arg1 + 0xD8), a2, local_rsp - 328 - 96, 16);
    result = strstr(*(uint64_t *)(arg1 + 0xD8), v_rip + 383077, local_rsp - 328 - 96, 16);
    if (result == 0) goto loc_00C1B399;
    result = strstr(result, v_rip + 383073, local_rsp - 328 - 96, 16);
    if (result == 0) goto loc_00C1B399;
    result = atol(result + 1, v_rip + 383073, local_rsp - 328 - 96, 16);
    a2 = ((int32_t)((uint32_t)(result))) << (8);
    if (a2 != 0) {
        Arg1 = 0;
        result = ExBurnMemory(Arg1, a2, local_rsp - 328 - 96, 16);
    }
    result = strstr(*(uint64_t *)(arg1 + 0xD8), v_rip + 383040, local_rsp - 328 - 96, 16);
    if (result != 0) {
        *(uint8_t *)(v_rip + 0x3AB73E) = 1;
    }
loc_00C1B3BE:
    if ((*(uint64_t *)(arg1 + 0x20)) == (Arg1 + 32)) goto loc_00C1B3E9;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20)) < 0) goto loc_00C1B3D9;
    goto loc_00C1B3BE;
loc_00C1B3D9:
    v_stack_m228 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20) + *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x28) * 1;
    result = KeBugCheckEx(49, *(uint64_t *)(*(uint64_t *)(arg1 + 0x20)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20), *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x28));
loc_00C1B3E9:
    result = *(uint64_t *)(arg1 + 0xE0);
    if (*(uint64_t *)(arg1 + 0xE0) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0xE0) + 0x10);
        *(uint64_t *)(v_rip + 0x3ECD90) = result;
        result = ExPreInitializeNls(49, *(uint64_t *)(*(uint64_t *)(arg1 + 0x20)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20), *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x28));
    }
    *(uint64_t *)(v_rip + 0x2E3A1E) = *(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xBA0);
    result = WheaInitializeServices(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xBA0), *(uint64_t *)(*(uint64_t *)(arg1 + 0x20)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20), *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x28));
    result = guard_dispatch_icall(*(uint64_t *)(v_rip + 0x1EB8FB), *(uint64_t *)(*(uint64_t *)(arg1 + 0x20)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20), *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x28));
    a2 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x20))) << (32);
    result = (result) | (a2);
    *(uint64_t *)(v_rip + 0x3ED3AD) = result;
    result = HalInitSystem((uint32_t)(*(uint32_t *)(v_rip + 0x3A8D66)), Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20), *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x28));
    if ((uint8_t)(result) == 0) {
        Arg1 = 92;
        result = KeBugCheck(Arg1, Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20), *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x28));
    }
    a2 = (Arg1) << (32);
    result = (result) | (a2);
    *(uint64_t *)(v_rip + 0x3ED388) = result;
    result = KeInitializeClock((uint32_t)(*(uint32_t *)(v_rip + 0x3A8D39)), Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20), *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x28));
    result = PsInitializeQuotaSystem(1, Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20), *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x28));
    result = CmInitSystem0(Arg1, Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20), *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x28));
    if ((*(uint8_t *)(v_rip + 0x2F3B3C)) == 0) {
        result = *(uint64_t *)(v_rip + 0x3AD7A3);
        Arg1 = *(uint64_t *)(result + 0x18);
    }
    Arg1 = 0;
    result = KeInitSystem(Arg1, Arg1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x20), *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x28));
    if ((uint8_t)(result) == 0) {
        a4 = 0;
        v_stack_m228 = 0;
        a2 = 0xFFFFFFFFC0000001ULL;
        Arg1 = a4 + 49;
        a3 = a4 + 11;
        result = KeBugCheckEx(Arg1, a2, a3, a4);
    }
    a2 = (uint32_t)((a2) >> (13));
    result = (uint32_t)(((uint32_t)(0xD1B71759ULL)) * ((uint32_t)(a2)));
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x3AB5CB))) - ((uint32_t)(result)));
loc_00C1B4F8:
    a3 = (uint32_t)((a3) + ((uint32_t)(a3)));
    a4 = (uint32_t)((0) + (0));
    a4 = (uint32_t)((a4) | (1));
    if (((uint32_t)(a3)) < ((uint32_t)((uint32_t)(0x2710ULL)))) { a4 = (uint32_t)((uint32_t)((uint32_t)(a4))); }
    a3 = (uint32_t)((a3) + (0xFFFFD8F0ULL));
    if (((uint32_t)((uint32_t)((uint32_t)(a3)))) < ((uint32_t)((uint32_t)(0x2710ULL)))) { a3 = (uint32_t)((uint32_t)((uint32_t)(a3))); }
    local_r10 = (24) - (1);
    if (condition_is_not_equal) goto loc_00C1B4F8;
    a2 = (uint32_t)((a2) << (24));
    a2 = (uint32_t)((a2) | ((uint32_t)(a4)));
    v_stack_m208 = 0;
    *(uint32_t *)(v_rip + 0x2E3871) = (uint32_t)(a2);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x3A9ADD) + 0x4) = (uint32_t)(a2);
    v_stack_m218 = 0;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x3A9AAE) + 0x23C) = 0;
    *(uint64_t *)(local_rsp - 0x148 - 0x50) = 11;
    *(uint64_t *)(local_rsp - 0x148 - 0x48) = 1;
    *(uint64_t *)(local_rsp - 0x148 - 0x40) = 0;
    result = LdrFindResource_U(v_rip - 12694841, local_rsp - 328 - 80, local_r10 + 3, v_stack_m1F0);
    if (sign_flag) goto loc_00C1B5AA;
    result = LdrAccessResource(v_rip - 12694933, v_stack_m1F0, v_stack_m208, v_stack_m218);
    if (!(sign_flag)) {
        result = v_stack_m208;
        *(uint64_t *)(v_rip + 0x3AB84E) = result;
    }
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x3A9A47) + 0x258) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3ED13A)));
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x3A9A3A) + 0x28B) = 1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x3A8B71))) & (0xFFFULL));
    *(uint16_t *)(v_rip + 0x3A8BDA) = 0;
    *(uint32_t *)(v_rip + 0x3A8B57) = (uint32_t)(result);
    if ((*(uint32_t *)(v_rip + 0x3A8CD5)) != 0) {
        result = (uint32_t)((result) << (16));
    }
    if ((*(uint32_t *)(v_rip + 0x3ECB76)) != ((uint32_t)(local_r13 + 4))) goto loc_00C1B610;
    if ((*(uint32_t *)(v_rip + 0x3ECB6A)) != ((uint32_t)(local_r13 + 4))) {
        *(uint32_t *)(v_rip + 0x3ED085) = 0;
    }
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x3ED07F));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3ED07F))) != 0) {
        result = (uint32_t)(-((uint32_t)(*(uint32_t *)(v_rip + 0x3ED07F))));
        a2 = 1;
        Arg1 = (*(uint64_t *)(v_rip + 0x3A9A47)) * (result);
        result = KeAdjustInterruptTime(Arg1, a2, v_stack_m208, v_stack_m218);
        Arg1 = 0;
        result = KeQueryPerformanceCounter(Arg1, a2, v_stack_m208, v_stack_m218);
        Arg1 = *(uint64_t *)(v_rip + 0x3A99C8);
        *(uint64_t *)(arg1 + 0x348) = result;
        *(uint64_t *)(v_rip + 0x24B272) = 0;
    }
    Arg1 = 0;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x3A9999) + 0x3C0) = 1;
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x3A998B) + 0x3C4) = 1;
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x3A997D) + 0x36A) = 1;
    result = ExInitSystem(Arg1, a2, v_stack_m208, v_stack_m218);
    if ((uint8_t)(result) == 0) goto loc_00C1BE6B;
    *(uint64_t *)(v_rip + 0x2DEA49) = 0;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xE78) == 0) goto loc_00C1B6F5;
    result = IpmiHwInitializeContext(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xE78), a2, v_stack_m208, v_stack_m218);
    if (sign_flag) goto loc_00C1B6F5;
    result = WheaSelLogSetNtSchedulerAvailability(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xE78), a2, v_stack_m208, v_stack_m218);
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x84)) & (0x80000ULL)) != 0) {
        result = *(uint8_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xA58);
        Arg1 = 5;
        result = (uint8_t)((result) & ((uint8_t)(local_r13 + 4)));
        result = (uint8_t)(-(result));
        a2 = (uint32_t)((a2) & (3));
        result = WheaSelLogCheckPoint(Arg1, a2, v_stack_m208, v_stack_m218);
    }
    result = KeNumaInitialize(Arg1, a2, v_stack_m208, v_stack_m218);
    result = VerifierInitSystem(Arg1, a2, v_stack_m208, v_stack_m218);
    result = InitializeDynamicPartitioningPolicy(Arg1, a2, v_stack_m208, v_stack_m218);
    result = KeInitializeXSaveStructures(Arg1, a2, v_stack_m208, v_stack_m218);
    *(uint64_t *)(v_rip + 0x307783) = 0x200001ULL;
    a2 = 0;
    result = memset(v_rip + 3176321, a2, 256, v_stack_m218);
    *(uint64_t *)(v_rip + 0x30786C) = 0;
    Arg1 = 0;
    *(uint64_t *)(v_rip + 0x307873) = v_rip + 3176571;
    *(uint64_t *)(v_rip + 0x307864) = v_rip + 3176571;
    result = KeQueryPerformanceCounter(Arg1, a2, 256, v_stack_m218);
    *(uint64_t *)(v_rip + 0x3ED045) = result;
    Arg1 = 0;
    result = MmInitSystem(Arg1, 0, 256, v_stack_m218);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, 0, 256, v_stack_m218);
    *(uint64_t *)(v_rip + 0x3ED038) = result;
    if (*(uint64_t *)(arg1 + 0xF0) == 0) goto loc_00C1B79E;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xB58) == 0) goto loc_00C1B79E;
    if (((8) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xB58)))))) != 0) {
        a2 = *(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x1118);
    }
    Arg1 = (*(uint64_t *)(v_rip + 0x3AD49B)) + (0x91C0ULL);
    result = kernel_indirect_call(Arg1, a2, 256, v_stack_m218);
    Arg1 = 0;
    result = EtwInitialize(Arg1, Arg1, 256, v_stack_m218);
    Arg1 = 0;
    *(uint64_t *)(v_rip + 0x306335) = 0;
    result = VmInitSystem(Arg1, Arg1, 256, v_stack_m218);
    if (sign_flag) {
        a4 = 0;
        a2 = (int32_t)((uint32_t)(result));
        v_stack_m228 = 0;
        Arg1 = a4 + 49;
        a3 = a4 + 19;
        result = KeBugCheckEx(Arg1, a2, a3, a4);
    }
    Arg1 = 0;
    result = HalInitializeBios(Arg1, Arg1, a3, a4);
    a3 = 0;
    Arg1 = 0;
    result = InbvDriverInitialize(Arg1, 0, a3, a4);
    if ((*(uint64_t *)(v_rip + 0x3AB5ED)) == 0) goto loc_00C1B85A;
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)((uint32_t)(v_stack_m218))), (uint32_t)(0x6342694BULL), a4);
    v_stack_m208 = result;
    if (result == 0) {
        Arg1 = result + 125;
        result = KeBugCheck(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m218))), (uint32_t)(0x6342694BULL), a4);
    }
    result = memcpy(result, *(uint64_t *)(v_rip + 0x3AB5B6), (uint32_t)(v_stack_m218), a4);
    *(uint64_t *)(v_rip + 0x3AB5A4) = result;
loc_00C1B85A:
    if ((*(uint32_t *)(arg1 + 0xC)) < 2) {
        *(uint32_t *)(v_rip + 0x24A84B) = 0;
        a4 = 0;
        a2 = *(uint32_t *)(arg1 + 0xC);
        a3 = 2;
        Arg1 = 406;
        v_stack_m228 = 0;
        result = KeBugCheckEx(Arg1, a2, a3, a4);
    }
    a3 = 0;
    *(uint64_t *)(local_rsp - 0x148 - 0x80) = 0;
    v_stack_m1D0 = Arg1;
    result = MiEnumerateSystemImages(v_rip + 1554, v_stack_m1D0, a3, a4);
    if ((*(uint8_t *)(v_rip + 0x33E41F)) != 0) {
        Arg1 = 1;
        result = DbgBreakPointWithStatus(Arg1, v_stack_m1D0, a3, a4);
    }
    Arg1 = -(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8EB8));
    result = (uint8_t)((*(uint8_t *)(v_rip + 0x3AB213)) & (253));
    a2 = (uint8_t)((v_stack_m1D0) & (2));
    a2 = (uint8_t)((a2) | ((uint8_t)(result)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x3AB1DC))) >> (28));
    a2 = (uint8_t)((a2) & (251));
    result = (uint8_t)((result) & ((uint8_t)(local_r13 + 4)));
    result = (uint8_t)((result) | (1));
    a2 = (uint8_t)((a2) | ((uint8_t)(result)));
    *(uint8_t *)(v_rip + 0x3AB1ED) = (uint8_t)(a2);
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x108)) & (1));
    result = (uint8_t)(-(result));
    Arg1 = (uint32_t)(-(Arg1));
    Arg1 = (uint32_t)((Arg1) + (1));
    *(uint32_t *)(v_rip + 0x2E3743) = (uint32_t)(Arg1);
    *(uint64_t *)(v_rip + 0x2E371D) = v_xmm0;
    *(uint64_t *)(v_rip + 0x2E3720) = *(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xA58);
    result = IoAddTriageDumpDataBlock(v_rip + 3028737, 32, a3, a4);
    if ((*(uint8_t *)(v_rip + 0x5E5EF6)) == 0) goto loc_00C1B9A2;
    if (((2) & ((uint8_t)(*(uint8_t *)(v_rip + 0x5E5EEE)))) == 0) goto loc_00C1B97D;
    if ((*(uint8_t *)(v_rip + 0x32BC7C)) == 0) goto loc_00C1B97D;
    if ((*(uint8_t *)(v_rip + 0x32BC74)) == 0) {
        a3 = (uint8_t)((*(uint8_t *)(v_rip + 0x5E5EEE)) & (253));
        *(uint8_t *)(v_rip + 0x3AB260) = 1;
        *(uint8_t *)(v_rip + 0x5E5EC5) = (uint8_t)(a3);
    }
    a2 = (32) << (32);
    result = (result) | (a2);
    if ((uint8_t)(a3) != 0) goto loc_00C1B996;
    result = (result) & (-3);
    goto loc_00C1B999;
loc_00C1B996:
    result = (result) | (2);
loc_00C1B999:
    a2 = (result) >> (32);
loc_00C1B9A2:
    result = PsInitializeWin32kServiceTable((uint32_t)(0x6A2ULL), a2, a3, a4);
    result = PsInitializeWin32kKernelExports((uint32_t)(0x6A2ULL), a2, a3, a4);
    if (((*(uint64_t *)(v_rip + 0x3AB0D1)) & (0x40000ULL)) != 0) {
        a3 = 0;
        Arg1 = v_rip + 277533;
        a2 = 0;
        result = MiEnumerateSystemImages(Arg1, a2, a3, a4);
    }
    result = HvlPhase1Initialize(Arg1, a2, a3, a4);
    result = *(uint64_t *)(arg1 + 0xF0);
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0))) >= 0x1130ULL) {
        Arg1 = Arg1;
        result = HeadlessInit(Arg1, a2, a3, a4);
    }
    result = BootApplicationPersistentDataInitialize(Arg1, a2, a3, a4);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x3A9610) + 0x2B4) = 0x7FFEFFFFULL;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x3A95F9) + 0x2B8) = (uint32_t)((uint32_t)(0x80000000ULL));
    if ((*(uint32_t *)(v_rip + 0x3A87A3)) == 0) goto loc_00C1BB5D;
    a3 = 0;
    v_stack_m228 = v_stack_m1E8;
    result = RtlFindMessage(v_rip - 12696125, a3 + 11, a3, (uint32_t)(0x40000087ULL));
    if (sign_flag) {
        a4 = 0;
        a2 = (int32_t)((uint32_t)(result));
        a3 = local_r13 + 4;
        v_stack_m228 = 0;
        Arg1 = a4 + 49;
        result = KeBugCheckEx(Arg1, a2, a3, a4);
    }
    a2 = (v_stack_m1E8) + (local_r13 + 4);
    result = RtlInitAnsiString(v_stack_m200, a2, a3, a4);
    Arg1 = (uint32_t)(-((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3A8730)))));
    a2 = (uint32_t)((a2) & ((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3A8730))) + 64)));
    v_stack_m220 = (uint32_t)(a2);
    v_stack_m228 = (uint32_t)(*(uint8_t *)(v_rip + 0x3A871A));
    result = RtlStringCbPrintfA(local_rsp - 328 + 16, 256, v_rip + 381286, v_stack_m200);
    if (sign_flag) {
        a4 = 0;
        a2 = (int32_t)((uint32_t)(result));
        v_stack_m228 = 0;
        Arg1 = a4 + 49;
        a3 = a4 + 5;
        result = KeBugCheckEx(Arg1, a2, a3, a4);
    }
    if (((*(uint32_t *)(v_rip + 0x3A86E2)) & (0xFFFF0000ULL)) == 0) goto loc_00C1BBD1;
    v_stack_m1E0 = 0;
    v_stack_m228 = v_stack_m210;
    result = RtlStringCbCatExA(local_rsp - 328 + 16, a2, a3, v_stack_m1E0);
    if (sign_flag) {
        a4 = 0;
        a2 = (int32_t)((uint32_t)(result));
        v_stack_m228 = 0;
        Arg1 = a4 + 49;
        a3 = a4 + 6;
        result = KeBugCheckEx(Arg1, a2, a3, a4);
    }
    result = RtlStringCbPrintfA(v_stack_m1E0, v_stack_m210, v_rip + 381155, *(uint16_t *)(v_rip + 0x3A869C));
    if (!sign_flag) goto loc_00C1BBD1;
    a4 = 0;
    v_stack_m228 = 0;
    result = KeBugCheckEx(a4 + 49, (int32_t)((uint32_t)(result)), a4 + 7, a4);
loc_00C1BB5D:
    a4 = 0;
    result = RtlStringExValidateDestA(local_rsp - 328 + 16, 256, a4 + 7, a4);
    if (sign_flag) goto loc_00C1BE4F;
    v_stack_m1D8 = 0;
    result = RtlStringCopyWorkerA(local_rsp - 328 + 16, 256, v_stack_m1D8, v_rip + 381090);
    Arg1 = (256) - (v_stack_m1D8);
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result))) != 0) goto loc_00C1BBB7;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0x80000005ULL) goto loc_00C1BBB7;
    goto loc_00C1BBBC;
loc_00C1BBB7:
    v_stack_m210 = v_stack_m210;
loc_00C1BBBC:
    if (sign_flag) goto loc_00C1BE53;
    local_r14 = (uint16_t)((256) - ((uint16_t)(v_stack_m210)));
    *(uint16_t *)(v_rip + 0x3A85E1) = (uint16_t)(local_r14);
loc_00C1BBD1:
    result = RtlInitAnsiString(v_stack_m200, local_rsp - 328 + 16, (uint32_t)((uint32_t)(result)), v_rip + 381090);
    result = RtlAnsiStringToUnicodeString(v_rip + 3835330, v_stack_m200, 1, v_rip + 381090);
    if (sign_flag) {
        a4 = 0;
        a2 = (int32_t)((uint32_t)(result));
        v_stack_m228 = 0;
        Arg1 = a4 + 49;
        a3 = a4 + 9;
        result = KeBugCheckEx(Arg1, a2, a3, a4);
    }
    v_stack_m228 = 3;
    result = RtlStringCbPrintfA(local_rsp - 328 - 48, (uint32_t)((uint32_t)(6 + 58)), v_rip + 380939, 6);
    if (sign_flag) {
        a2 = (int32_t)((uint32_t)(result));
        Arg1 = 6 + 58 - 15;
        a4 = 0;
        v_stack_m228 = 0;
        a3 = 6 + 58 - 54;
        result = KeBugCheckEx(Arg1, a2, a3, a4);
    }
    result = RtlCreateUnicodeStringFromAsciiz(v_rip + 3835251, local_rsp - 328 - 48, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C1BE6B;
    if (((*(uint32_t *)(v_rip + 0x3A864C)) & (0x2000ULL)) == 0) goto loc_00C1BCCB;
    result = 0;
    *(uint64_t *)(local_rsp - 0x148 - 0x68) = 0;
    *(uint64_t *)(local_rsp - 0x148 - 0x78) = v_xmm0;
    result = ExAllocatePool2(6 + 58, (uint32_t)((uint32_t)((uint32_t)(0x800000ULL))), (uint32_t)((uint32_t)((uint32_t)(0x63617453ULL))), a4);
    if (result == 0) goto loc_00C1BCCB;
    *(uint64_t *)(local_rsp - 0x148 - 0x78) = result;
    *(uint64_t *)(local_rsp - 0x148 - 0x70) = (uint32_t)(0x800000ULL);
    *(uint64_t *)(local_rsp - 0x148 - 0x68) = (uint32_t)(0x800000ULL);
    result = RtlpInitializeStackTraceDatabase(result, (uint32_t)((uint32_t)((uint32_t)(0x800000ULL))), (uint32_t)((uint32_t)((uint32_t)(0x800000ULL))), a4);
    if (sign_flag) {
        a2 = (uint32_t)((uint32_t)(0x63617453ULL));
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, a2, (uint32_t)((uint32_t)((uint32_t)(0x800000ULL))), a4);
    }
    if (((*(uint32_t *)(v_rip + 0x3A85EF)) & ((uint32_t)((uint32_t)(0x800000ULL)))) == 0) goto loc_00C1BD0B;
    result = ExAllocatePool2(6 + 58, (uint32_t)((uint32_t)((uint32_t)(0x11620ULL))), (uint32_t)(0x67626445ULL), a4);
    *(uint64_t *)(v_rip + 0x24BE01) = result;
    if (result != 0) {
        a3 = (uint32_t)((uint32_t)(0x11620ULL));
        a2 = 0;
        Arg1 = result;
        result = memset(Arg1, a2, a3, a4);
        *(uint32_t *)(v_rip + 0x2E9F91) = 50;
    }
    *(uint64_t *)(v_rip + 0x3BDE87) = 0;
    *(uint64_t *)(v_rip + 0x3BE2B0) = v_rip + 3924662;
    *(uint64_t *)(v_rip + 0x3BE2A1) = v_rip + 3924662;
    result = HalQueryMaximumProcessorCount(Arg1, a2, a3, a4);
    Arg1 = 0;
    *(uint32_t *)(v_rip + 0x3BDDE4) = (uint32_t)(result);
    result = ObInitSystem(Arg1, a2, a3, a4);
    if ((uint8_t)(result) == 0) {
        Arg1 = 94;
        result = KeBugCheck(Arg1, a2, a3, a4);
    }
    result = kernel_indirect_call(12 + 91, 12, a3, a4);
    result = SeInitSystem(12 + 91, 12, a3, a4);
    if ((uint8_t)(result) == 0) {
        Arg1 = 95;
        result = KeBugCheck(Arg1, 12, a3, a4);
    }
    Arg1 = 0;
    result = PsInitSystem(Arg1, Arg1, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00C1BE44;
    result = DbgkInitialize(Arg1, Arg1, a3, a4);
    if (sign_flag) goto loc_00C1BE44;
    result = PpInitSystem(Arg1, Arg1, a3, a4);
    if ((uint8_t)(result) == 0) {
        Arg1 = 143;
        result = KeBugCheck(Arg1, Arg1, a3, a4);
    }
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x3A925E) + 0x26C) = 10;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x3A924D) + 0x270) = 0;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x3A923F) + 0x260) = 0x65F4ULL;
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x3A922E) + 0x26A) = (uint16_t)(*(uint16_t *)(v_rip + 0x3A9297));
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x3A9214) + 0x2C) = (uint16_t)((uint32_t)(0x8664ULL));
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x3A9209) + 0x2E) = (uint16_t)((uint32_t)(0x8664ULL));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x3A91FE) + 0x3A4) = 0;
    result = 0;
    Arg1 = (*(uint64_t *)(local_rsp - 0x148 + 0x110)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg1, a3, a4);
    return result;
loc_00C1BE44:
    result = KeBugCheck(96, Arg1, a3, a4);
loc_00C1BE4F:
    *(uint8_t *)(local_rsp - 0x148 + 0x10) = 0;
loc_00C1BE53:
    a4 = 0;
    v_stack_m200 = 0;
    result = KeBugCheckEx(a4 + 49, (int32_t)((uint32_t)(a3)), *(uint64_t *)(v_stack_m28 + 0x40), a4);
loc_00C1BE6B:
    result = KeBugCheck(49, (int32_t)((uint32_t)(a3)), *(uint64_t *)(v_stack_m28 + 0x40), a4);
loc_00C1BE76:
loc_00C1BE79:
    v_stack_m200 = 0;
    result = KeBugCheckEx(256, (int32_t)((uint32_t)(a3)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x4 * 1)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x38) + 0x4 + 0x4 * 1)));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0 + rdi*1` | `32` | `R` |
| `Arg1` | `+ 0x0 + rsi*1` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0xD8` | `64` | `R` |
| `Arg1` | `+ 0xE0` | `64` | `R` |
| `Arg1` | `+ 0xF0` | `64` | `R` |
| `Arg1` | `+ 0x108` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C1B1C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
