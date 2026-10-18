# ExFreePool

- RVA: `0x00B82850`–`0x00B82861` (길이 `17` bytes)
- VA: `0x0000000140B82850`
- 실행 섹션: `POOLCODE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **129**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B82856` → [ExFreePoolWithTag](ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [IoFreeMdl](../../text/29/IoFreeMdl_function_0029EA80.md) at `0x0029EB37`
- [CcFreeWorkQueueEntry](../../text/35/CcFreeWorkQueueEntry_function_0035723C.md) at `0x003572D0`
- [KeFreeXStateContext](../../text/3D/KeFreeXStateContext_function_003D6324.md) at `0x003D63A1`
- [FsRtlUninitializeBaseMcb](../../text/44/FsRtlUninitializeBaseMcb_function_00446CB0.md) at `0x00446D52`
- [LZNT1DecompressChunkWorkItem](../../text/44/LZNT1DecompressChunkWorkItem_function_00448A20.md) at `0x00448AE2`
- [sub_0050C0E0](../../text/50/Unknown_function_0050C0E0.md) at `0x0051A821`
- [sub_0051ADC0](../../text/51/Unknown_function_0051ADC0.md) at `0x0051ADFD`
- [sub_0051ADC0](../../text/51/Unknown_function_0051ADC0.md) at `0x0051AE0F`
- [PiDrvDbQueryHiveFileName](../../page/74/PiDrvDbQueryHiveFileName_function_00741DDC.md) at `0x00741EB5`
- [PiDrvDbResolveSystemFilePath](../../page/74/PiDrvDbResolveSystemFilePath_function_00743514.md) at `0x007437C2`
- [RtlUpcaseUnicodeStringToAnsiString](../../page/78/RtlUpcaseUnicodeStringToAnsiString_function_0078A830.md) at `0x0078A8FE`
- [RtlpConstructCrossVmObjectPath](../../page/79/RtlpConstructCrossVmObjectPath_function_00790958.md) at `0x00790A9E`
- [RtlUTF8StringToUnicodeString](../../page/79/RtlUTF8StringToUnicodeString_function_00794B80.md) at `0x00794C5C`
- [RtlUnicodeStringToUTF8String](../../page/79/RtlUnicodeStringToUTF8String_function_00794C90.md) at `0x00794D89`
- [EtwpQueryRegistryCallback](../../page/7B/EtwpQueryRegistryCallback_function_007BEA40.md) at `0x007BEADC`
- [CmpSetVersionData](../../page/7E/CmpSetVersionData_function_007E7854.md) at `0x007E7C37`
- [CmpSetVersionData](../../page/7E/CmpSetVersionData_function_007E7854.md) at `0x007E7D40`
- [sub_00857959](../../page/85/Unknown_function_00857959.md) at `0x008579AA`
- [CmQueryKey](../../page/85/CmQueryKey_function_00858240.md) at `0x00858C57`
- [CmpCleanupPathInfo](../../page/85/CmpCleanupPathInfo_function_0085F6D0.md) at `0x0085F733`
- [sub_00864EE6](../../page/86/Unknown_function_00864EE6.md) at `0x00865008`
- [CmpCallCallBacksEx](../../page/86/CmpCallCallBacksEx_function_00865F40.md) at `0x00866701`
- [CmpCallCallBacksEx](../../page/86/CmpCallCallBacksEx_function_00865F40.md) at `0x00866827`
- [ObCreateObject](../../page/87/ObCreateObject_function_00872CB0.md) at `0x00872FC1`
- [ObCreateObject](../../page/87/ObCreateObject_function_00872CB0.md) at `0x0087314E`
- [ObDeleteCapturedInsertInfo](../../page/87/ObDeleteCapturedInsertInfo_function_00876E90.md) at `0x00876F0E`
- [CmpInitCmRM](../../page/87/CmpInitCmRM_function_0087C700.md) at `0x0087CC15`
- [CmpInitCmRM](../../page/87/CmpInitCmRM_function_0087C700.md) at `0x0087CC5E`
- [IopAllocRealFileObject](../../page/89/IopAllocRealFileObject_function_00899720.md) at `0x00899DD5`
- [IopAllocRealFileObject](../../page/89/IopAllocRealFileObject_function_00899720.md) at `0x00899E0D`
- [IopAllocRealFileObject](../../page/89/IopAllocRealFileObject_function_00899720.md) at `0x00899E67`
- [sub_0089AEE3](../../page/89/Unknown_function_0089AEE3.md) at `0x0089AFC4`
- [sub_0089AEE3](../../page/89/Unknown_function_0089AEE3.md) at `0x0089B002`
- [sub_0089AEE3](../../page/89/Unknown_function_0089AEE3.md) at `0x0089B040`
- [sub_0089AEE3](../../page/89/Unknown_function_0089AEE3.md) at `0x0089B08C`
- [ObCreateObjectEx](../../page/89/ObCreateObjectEx_function_0089B1E0.md) at `0x0089B779`
- [ObCreateObjectEx](../../page/89/ObCreateObjectEx_function_0089B1E0.md) at `0x0089B7B1`
- [EtwpWriteProcessEvent](../../page/8A/EtwpWriteProcessEvent_function_008A420C.md) at `0x008A4368`
- [EtwpTraceProcessRundown](../../page/8A/EtwpTraceProcessRundown_function_008A5024.md) at `0x008A5157`
- [IopCreateFile](../../page/8A/IopCreateFile_function_008AB298.md) at `0x008AB49C`
- [IopCreateFile](../../page/8A/IopCreateFile_function_008AB298.md) at `0x008AB9AD`
- [IopCreateFile](../../page/8A/IopCreateFile_function_008AB298.md) at `0x008ABAEF`
- [IopCreateFile](../../page/8A/IopCreateFile_function_008AB298.md) at `0x008ABB99`
- [IopCreateFile](../../page/8A/IopCreateFile_function_008AB298.md) at `0x008ABC80`
- [IopCreateFile](../../page/8A/IopCreateFile_function_008AB298.md) at `0x008ABD34`
- [IopCreateFile](../../page/8A/IopCreateFile_function_008AB298.md) at `0x008ABE5D`
- [NtCreateEvent](../../page/8B/NtCreateEvent_function_008B9140.md) at `0x008B9532`
- [NtCreateEvent](../../page/8B/NtCreateEvent_function_008B9140.md) at `0x008B970A`
- [ObInsertObjectEx](../../page/8B/ObInsertObjectEx_function_008B97A0.md) at `0x008B9EE1`
- [ObInsertObjectEx](../../page/8B/ObInsertObjectEx_function_008B97A0.md) at `0x008B9F3D`
- [ObReferenceObjectByNameEx](../../page/8B/ObReferenceObjectByNameEx_function_008BD524.md) at `0x008BD7FD`
- [sub_008C28B0](../../page/8C/Unknown_function_008C28B0.md) at `0x008C2D50`
- [sub_008C28B0](../../page/8C/Unknown_function_008C28B0.md) at `0x008C2D95`
- [NtCreateSemaphore](../../page/8C/NtCreateSemaphore_function_008C38D0.md) at `0x008C3B9A`
- [sub_008C405D](../../page/8C/Unknown_function_008C405D.md) at `0x008C40BC`
- [sub_008C405D](../../page/8C/Unknown_function_008C405D.md) at `0x008C40FA`
- [ObpFreeObjectNameBuffer](../../page/8C/ObpFreeObjectNameBuffer_function_008C4250.md) at `0x008C42C9`
- [NtCreateMutant](../../page/8C/NtCreateMutant_function_008C43D0.md) at `0x008C468C`
- [NtCreateWaitCompletionPacket](../../page/8C/NtCreateWaitCompletionPacket_function_008C4700.md) at `0x008C499A`
- [RtlpGetRegistryHandle](../../page/8C/RtlpGetRegistryHandle_function_008C955C.md) at `0x008C9749`
- [RtlpGetRegistryHandle](../../page/8C/RtlpGetRegistryHandle_function_008C955C.md) at `0x008C97A1`
- [PiSwCompleteCreate](../../page/8D/PiSwCompleteCreate_function_008DAB90.md) at `0x008DADE3`
- [SysCtxRegOpenCurrentUserKey](../../page/8F/SysCtxRegOpenCurrentUserKey_function_008F455C.md) at `0x008F47BE`
- [SepValidateReferencedCachedHandles](../../page/8F/SepValidateReferencedCachedHandles_function_008F4BB0.md) at `0x008F4D82`
- [PipProcessDevNodeTree](../../page/8F/PipProcessDevNodeTree_function_008F9068.md) at `0x008F94D1`
- [RtlUpcaseUnicodeStringToCountedOemString](../../page/90/RtlUpcaseUnicodeStringToCountedOemString_function_0090E4D0.md) at `0x0090E6C8`
- [MmGetSystemRoutineAddress](../../page/90/MmGetSystemRoutineAddress_function_0090EFE0.md) at `0x0090F052`
- [RtlUnicodeStringToCountedOemString](../../page/90/RtlUnicodeStringToCountedOemString_function_0090F1A0.md) at `0x0090F29A`
- [RtlOemStringToCountedUnicodeString](../../page/90/RtlOemStringToCountedUnicodeString_function_0090F3D0.md) at `0x0090F4A2`
- [RtlOemStringToUnicodeString](../../page/90/RtlOemStringToUnicodeString_function_0090F6C0.md) at `0x0090F799`
- [PopSetNewPolicyValue](../../page/91/PopSetNewPolicyValue_function_00914C6C.md) at `0x00914CB6`
- [BcdOpenObject](../../page/91/BcdOpenObject_function_00916704.md) at `0x009167CD`
- [DrvDbGetObjectDatabaseNode](../../page/93/DrvDbGetObjectDatabaseNode_function_00930228.md) at `0x0093031E`
- [sub_00931420](../../page/93/Unknown_function_00931420.md) at `0x0093149D`
- [EtwpAcquireLoggerContext](../../page/93/EtwpAcquireLoggerContext_function_009326AC.md) at `0x0093280B`
- [IopProcessSetInterfaceState](../../page/95/IopProcessSetInterfaceState_function_00950964.md) at `0x00950B54`
- [PpDevCfgProcessDeviceReset](../../page/96/PpDevCfgProcessDeviceReset_function_00965498.md) at `0x00965728`
- [PiDevCfgClearDeviceMigrationNode](../../page/96/PiDevCfgClearDeviceMigrationNode_function_00965780.md) at `0x009659C0`
- [PiDevCfgClearDeviceMigrationNode](../../page/96/PiDevCfgClearDeviceMigrationNode_function_00965780.md) at `0x009659DA`
- [PiOpenDriverRedirectedStateKey](../../page/96/PiOpenDriverRedirectedStateKey_function_00965D04.md) at `0x00965E78`
- [PiOpenDriverRedirectedStateKey](../../page/96/PiOpenDriverRedirectedStateKey_function_00965D04.md) at `0x00965E8D`
- [PiDevCfgResetDeviceDriverSettings](../../page/96/PiDevCfgResetDeviceDriverSettings_function_00966168.md) at `0x009664A0`
- [PiDevCfgQueryDriverConfiguration](../../page/97/PiDevCfgQueryDriverConfiguration_function_0097584C.md) at `0x00975E60`
- [PiDevCfgProcessDevice](../../page/97/PiDevCfgProcessDevice_function_00976D34.md) at `0x00976FCA`
- [PiDevCfgProcessDevice](../../page/97/PiDevCfgProcessDevice_function_00976D34.md) at `0x00976FDF`
- [PiDevCfgConfigureDevice](../../page/97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00977D7E`
- [PiDevCfgConfigureDevice](../../page/97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00977D93`
- [PiDevCfgConfigureDevice](../../page/97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00977DA8`
- [PiDevCfgConfigureDevice](../../page/97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00977DC0`
- [PiDevCfgConfigureDevice](../../page/97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00977DCD`
- [PiDevCfgConfigureDevice](../../page/97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00977DDE`
- [PiDevCfgConfigureDevice](../../page/97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00977DF2`
- [PiDevCfgConfigureDevice](../../page/97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00977E03`
- [PiDevCfgConfigureDevice](../../page/97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00977E14`
- [PiDevCfgConfigureDevice](../../page/97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00977E28`
- [PiDevCfgConfigureDevice](../../page/97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00977E35`
- [PiDevCfgConfigureDevice](../../page/97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00977E46`
- [PiDevCfgConfigureDevice](../../page/97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00977E57`
- [PiDevCfgConfigureDevice](../../page/97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00977E68`
- [PiDevCfgConfigureDevice](../../page/97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00977E7D`
- [PiDevCfgConfigureDevice](../../page/97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x00978EE7`
- [PiDevCfgConfigureDevice](../../page/97/PiDevCfgConfigureDevice_function_00977BB4.md) at `0x0097946D`
- [PiDevCfgBuildDriverNodeStrongName](../../page/97/PiDevCfgBuildDriverNodeStrongName_function_0097A33C.md) at `0x0097A486`
- [PiDevCfgBuildIndirectString](../../page/97/PiDevCfgBuildIndirectString_function_0097A890.md) at `0x0097A9C2`
- [PiDevCfgBuildIndirectString](../../page/97/PiDevCfgBuildIndirectString_function_0097A890.md) at `0x0097AB20`
- [EtwpCovSampModuleNameInfoCleanup](../../page/97/EtwpCovSampModuleNameInfoCleanup_function_0097D96C.md) at `0x0097D98D`
- [CmRealKCBToVirtualPath](../../page/99/CmRealKCBToVirtualPath_function_00990130.md) at `0x009902D2`
- [CmpGetVirtualizationID](../../page/99/CmpGetVirtualizationID_function_00990338.md) at `0x009903FD`
- [PiDqOpenUserObjectRegKey](../../page/99/PiDqOpenUserObjectRegKey_function_00990444.md) at `0x0099068D`
- [PipCallDriverAddDeviceQueryRoutine](../../page/99/PipCallDriverAddDeviceQueryRoutine_function_00996604.md) at `0x009966DB`
- [PiProcessDriverInstance](../../page/99/PiProcessDriverInstance_function_00998530.md) at `0x00998709`
- [IoOpenDriverRegistryKey](../../page/99/IoOpenDriverRegistryKey_function_00998BB0.md) at `0x00998D50`
- [PiCreateDriverRedirectedStateKey](../../page/99/PiCreateDriverRedirectedStateKey_function_0099957C.md) at `0x0099960A`
- [IopBuildFullDriverPath](../../page/99/IopBuildFullDriverPath_function_009998E4.md) at `0x00999B2E`
- [IopQueryRegistryKeySystemPath](../../page/99/IopQueryRegistryKeySystemPath_function_0099A1CC.md) at `0x0099A3B2`
- [PiNormalizeDeviceText](../../page/99/PiNormalizeDeviceText_function_0099A43C.md) at `0x0099A73D`
- [PiGetDefaultMessageString](../../page/99/PiGetDefaultMessageString_function_0099A87C.md) at `0x0099A922`
- [PiGetDefaultMessageString](../../page/99/PiGetDefaultMessageString_function_0099A87C.md) at `0x0099A936`
- [IopUpdateSecureDeviceClassState](../../page/9A/IopUpdateSecureDeviceClassState_function_009A2CE8.md) at `0x009A2F78`
- [IopCreateSecureDeviceClassSettings](../../page/9A/IopCreateSecureDeviceClassSettings_function_009A30D8.md) at `0x009A3189`
- [sub_009A5B41](../../page/9A/Unknown_function_009A5B41.md) at `0x009A5B71`
- [FsRtlTeardownPerStreamContexts](../../page/9A/FsRtlTeardownPerStreamContexts_function_009A5CD0.md) at `0x009A5D9B`
- [CmpTraceHiveMountBaseFileMounted](../../page/9B/CmpTraceHiveMountBaseFileMounted_function_009B8D0C.md) at `0x009B8DF9`
- [PiDevCfgQueryDeviceMigrationNode](../../page/9B/PiDevCfgQueryDeviceMigrationNode_function_009BD328.md) at `0x009BD687`
- [EtwpRealtimeCreateLogfile](../../page/9B/EtwpRealtimeCreateLogfile_function_009BE96C.md) at `0x009BEAD2`
- [EtwpCreateLogFile](../../page/9C/EtwpCreateLogFile_function_009C035C.md) at `0x009C0683`
- [RtlFreeAnsiString](../../page/9C/RtlFreeAnsiString_function_009C0800.md) at `0x009C0812`
- [WmipTranslatePDOInstanceNames](../../page/9E/WmipTranslatePDOInstanceNames_function_009E2F0C.md) at `0x009E310E`
- [WmipTranslatePDOInstanceNames](../../page/9E/WmipTranslatePDOInstanceNames_function_009E2F0C.md) at `0x009E3223`
- [LocalConvertSidToStringSidW](../../page/A0/LocalConvertSidToStringSidW_function_00A0191C.md) at `0x00A019A1`
- [LocalConvertSidToStringSidW](../../page/A0/LocalConvertSidToStringSidW_function_00A0191C.md) at `0x00A019B4`
- [CmGetMatchingFilteredDeviceInterfaceListWorker](../../page/A0/CmGetMatchingFilteredDeviceInterfaceListWorker_function_00A097EC.md) at `0x00A099E5`
- [RtlpCapabilityCheckSystemCapability](../../page/A2/RtlpCapabilityCheckSystemCapability_function_00A20768.md) at `0x00A207D0`
- [RtlpGetPolicyValueForSystemCapability](../../page/A2/RtlpGetPolicyValueForSystemCapability_function_00A207F8.md) at `0x00A208F1`
- [MiResolveImageReferences](../../page/A2/MiResolveImageReferences_function_00A23BE4.md) at `0x00A23E24`
- [MiResolveImageReferences](../../page/A2/MiResolveImageReferences_function_00A23BE4.md) at `0x00A23E53`
- [MiResolveImageReferences](../../page/A2/MiResolveImageReferences_function_00A23BE4.md) at `0x00A23F4D`
- [MiSnapThunk](../../page/A2/MiSnapThunk_function_00A24004.md) at `0x00A24251`
- [MiLogFailedDriverLoad](../../page/A2/MiLogFailedDriverLoad_function_00A24ACC.md) at `0x00A24CA4`
- [BcdGetElementDataWithFlags](../../page/A3/BcdGetElementDataWithFlags_function_00A3EBE4.md) at `0x00A3EDA7`
- [BiConvertElementToRegistryData](../../page/A4/BiConvertElementToRegistryData_function_00A400A8.md) at `0x00A4025D`
- [BiConvertElementToRegistryData](../../page/A4/BiConvertElementToRegistryData_function_00A400A8.md) at `0x00A402F2`
- [MiQuerySingleLoadedPatch](../../page/A4/MiQuerySingleLoadedPatch_function_00A41EB0.md) at `0x00A41FE0`
- [EtwpCovSampModuleGetName](../../page/A5/EtwpCovSampModuleGetName_function_00A5095C.md) at `0x00A50A14`
- [PspReadUserQuotaLimits](../../page/A6/PspReadUserQuotaLimits_function_00A68108.md) at `0x00A681DE`
- [IoGetDriverDirectory](../../page/A6/IoGetDriverDirectory_function_00A6F180.md) at `0x00A6F1E6`
- [PiGetDriverImageDirectory](../../page/A6/PiGetDriverImageDirectory_function_00A6F2C4.md) at `0x00A6F3C7`
- [RtlUpcaseUnicodeStringToOemString](../../page/A8/RtlUpcaseUnicodeStringToOemString_function_00A84220.md) at `0x00A84312`
- [PipGenerateContainerID](../../page/A8/PipGenerateContainerID_function_00A87694.md) at `0x00A87740`
- [EtwpGetAutoLoggerEventNameFilter](../../page/A9/EtwpGetAutoLoggerEventNameFilter_function_00A93E78.md) at `0x00A94391`
- [DbgkRegisterErrorPort](../../page/A9/DbgkRegisterErrorPort_function_00A9C39C.md) at `0x00A9C692`
- [PiDevCfgResolveVariableDeviceProperty](../../page/AA/PiDevCfgResolveVariableDeviceProperty_function_00AA63A0.md) at `0x00AA6782`
- [PiDevCfgConfigureDeviceLocation](../../page/AA/PiDevCfgConfigureDeviceLocation_function_00AA88C0.md) at `0x00AA8B94`
- [PiDevCfgResolveVariableKeyHandle](../../page/AB/PiDevCfgResolveVariableKeyHandle_function_00AB2A24.md) at `0x00AB313A`
- [RtlFreeOemString](../../page/AB/RtlFreeOemString_function_00AB5C50.md) at `0x00AB5C63`
- [PiCreateDriverSwDeviceCallback](../../page/AB/PiCreateDriverSwDeviceCallback_function_00ABB420.md) at `0x00ABB9DD`
- [PiCreateDriverSwDeviceCallback](../../page/AB/PiCreateDriverSwDeviceCallback_function_00ABB420.md) at `0x00ABB9FA`
- [PiCreateDriverSwDeviceCallback](../../page/AB/PiCreateDriverSwDeviceCallback_function_00ABB420.md) at `0x00ABBA0F`
- [PiCreateDriverSwDeviceCallback](../../page/AB/PiCreateDriverSwDeviceCallback_function_00ABB420.md) at `0x00ABBA24`
- [PiCreateDriverSwDeviceCallback](../../page/AB/PiCreateDriverSwDeviceCallback_function_00ABB420.md) at `0x00ABBA39`
- [PiCreateDriverSwDeviceCallback](../../page/AB/PiCreateDriverSwDeviceCallback_function_00ABB420.md) at `0x00ABBA4E`
- [PiDevCfgBuildDriverConfigurationId](../../page/AB/PiDevCfgBuildDriverConfigurationId_function_00ABC0D0.md) at `0x00ABC2EB`
- [PiDevCfgLogDeviceStarted](../../page/AB/PiDevCfgLogDeviceStarted_function_00ABEC8C.md) at `0x00ABF06B`
- [PiDevCfgLogDeviceStarted](../../page/AB/PiDevCfgLogDeviceStarted_function_00ABEC8C.md) at `0x00ABF080`
- [PiDevCfgLogDeviceStarted](../../page/AB/PiDevCfgLogDeviceStarted_function_00ABEC8C.md) at `0x00ABF096`
- [PiDevCfgLogDeviceStarted](../../page/AB/PiDevCfgLogDeviceStarted_function_00ABEC8C.md) at `0x00ABF0AD`
- [RtlUnicodeStringToOemString](../../page/AC/RtlUnicodeStringToOemString_function_00AC1C10.md) at `0x00AC1CDE`
- [PiDrvDbMountNode](../../page/AD/PiDrvDbMountNode_function_00AD4ECC.md) at `0x00AD4F56`
- [PiDrvDbMountNode](../../page/AD/PiDrvDbMountNode_function_00AD4ECC.md) at `0x00AD4F64`
- [RtlAnsiStringToUnicodeString$fin$0](../../page/B0/RtlAnsiStringToUnicodeString_fin_0_function_00B0F41B.md) at `0x00B0F446`
- [RtlUnicodeStringToAnsiString$fin$0](../../page/B0/RtlUnicodeStringToAnsiString_fin_0_function_00B0F470.md) at `0x00B0F49B`
- [RtlUpcaseUnicodeStringToCountedOemString$fin$0](../../page/B0/RtlUpcaseUnicodeStringToCountedOemString_fin_0_function_00B0F4BC.md) at `0x00B0F4E7`
- [RtlUnicodeStringToCountedOemString$fin$0](../../page/B0/RtlUnicodeStringToCountedOemString_fin_0_function_00B0F505.md) at `0x00B0F530`
- [RtlOemStringToCountedUnicodeString$fin$0](../../page/B0/RtlOemStringToCountedUnicodeString_fin_0_function_00B0F54E.md) at `0x00B0F576`
- [RtlOemStringToUnicodeString$fin$0](../../page/B0/RtlOemStringToUnicodeString_fin_0_function_00B0F594.md) at `0x00B0F5BC`
- [RtlDuplicateUnicodeString$fin$0](../../page/B0/RtlDuplicateUnicodeString_fin_0_function_00B0FB00.md) at `0x00B0FB19`
- [RtlUpcaseUnicodeString$fin$0](../../page/B0/RtlUpcaseUnicodeString_fin_0_function_00B0FD30.md) at `0x00B0FD4F`
- [RtlCreateUnicodeString$fin$0](../../page/B1/RtlCreateUnicodeString_fin_0_function_00B10987.md) at `0x00B109A0`
- [RtlDowncaseUnicodeString$fin$0](../../page/B1/RtlDowncaseUnicodeString_fin_0_function_00B109C0.md) at `0x00B109DF`
- [RtlUpcaseUnicodeStringToOemString$fin$0](../../page/B1/RtlUpcaseUnicodeStringToOemString_fin_0_function_00B13525.md) at `0x00B13550`
- [RtlUnicodeStringToOemString$fin$0](../../page/B1/RtlUnicodeStringToOemString_fin_0_function_00B13AF0.md) at `0x00B13B18`
- [RtlUpcaseUnicodeStringToAnsiString$fin$0](../../page/B1/RtlUpcaseUnicodeStringToAnsiString_fin_0_function_00B145A5.md) at `0x00B145CD`
- [sub_00B19FF6](../../page/B1/Unknown_function_00B19FF6.md) at `0x00B1A03E`
- [sub_00B19FF6](../../page/B1/Unknown_function_00B19FF6.md) at `0x00B1A10B`
- [sub_00B19FF6](../../page/B1/Unknown_function_00B19FF6.md) at `0x00B1A1D1`
- [KiFilterFiberContext](../../init/BE/KiFilterFiberContext_function_00BEFB50.md) at `0x00BEFEEC`
- [sub_00BF1290](../../init/BF/Unknown_function_00BF1290.md) at `0x00BF1521`
- [sub_00BF1290](../../init/BF/Unknown_function_00BF1290.md) at `0x00BF16B2`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00BF2203`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00BF221C`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00BF2EBA`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00BF31A7`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00BF4134`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00BF4416`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C062D5`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C06966`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C06970`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C07734`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C07B93`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C07B9D`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C168E1`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C172A8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B82850  48 83 EC 28                     sub rsp, 0x28
00B82854  33 D2                           xor edx, edx
00B82856  E8 15 00 00 00                  call 0x140b82870
00B8285B  48 83 C4 28                     add rsp, 0x28
00B8285F  C3                              ret
00B82860  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExFreePool(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExFreePool(void *Pool, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    result = ExFreePoolWithTag(Pool, Arg2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=poolcode&rva=0x00B82850&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B82850[BB_00B82850]
  bb_00B82860[BB_00B82860]
```
