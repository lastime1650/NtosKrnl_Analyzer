# ObInsertObjectEx

- RVA: `0x008B97A0`–`0x008BA09A` (길이 `2,298` bytes)
- VA: `0x00000001408B97A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00082C94`
- 디코드: `536`개 명령, `2,298/2,298` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **45**; 고유 호출 대상: **30**
- 직접 호출자로 확인된 함수: **64**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x008B9806` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008B9817` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008B98F6` → [ObpCreateHandle](../86/ObpCreateHandle_function_0086B950.md) (function, `0x0086B950`)
- `0x008B992D` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x008B9935` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008B9946` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008B99BB` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (function, `0x0020FF80`)
- `0x008B99EE` → [SepCreateAccessStateFromSubjectContext](../../text/3E/SepCreateAccessStateFromSubjectContext_function_003EBF40.md) (function, `0x003EBF40`)
- `0x008B9A68` → [SeComputeAutoInheritByObjectTypeEx](../../text/43/SeComputeAutoInheritByObjectTypeEx_function_00433280.md) (function, `0x00433280`)
- `0x008B9ACE` → [SeAssignSecurityEx2](../../text/4E/SeAssignSecurityEx2_function_004E9AA0.md) (function, `0x004E9AA0`)
- `0x008B9B35` → [SeDefaultObjectMethod](SeDefaultObjectMethod_function_008BA2B0.md) (function, `0x008BA2B0`)
- `0x008B9B4D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B9B74` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B9BE8` → [ObpCreateHandle](../86/ObpCreateHandle_function_0086B950.md) (function, `0x0086B950`)
- `0x008B9BF3` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008B9C09` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B9C35` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x008B9C4A` → [SepDeleteAccessState](../../text/3F/SepDeleteAccessState_function_003FFF20.md) (function, `0x003FFF20`)
- `0x008B9CB6` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x008B9CE8` → [PspLockThreadSecurityShared](../../text/3C/PspLockThreadSecurityShared_function_003C4720.md) (function, `0x003C4720`)
- `0x008B9D17` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x008B9D30` → [PspUnlockThreadSecurityShared](../../text/3C/PspUnlockThreadSecurityShared_function_003C2E40.md) (function, `0x003C2E40`)
- `0x008B9D42` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008B9D53` → [SeDeleteAccessState](../8C/SeDeleteAccessState_function_008C5F70.md) (function, `0x008C5F70`)
- `0x008B9D60` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008B9D95` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008B9DB1` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x008B9DD6` → [ObpChargeQuotaForObject](../97/ObpChargeQuotaForObject_function_00975220.md) (function, `0x00975220`)
- `0x008B9E18` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008B9E26` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008B9E33` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008B9E42` → [RtlValidSecurityDescriptor](RtlValidSecurityDescriptor_function_008BD3F0.md) (function, `0x008BD3F0`)
- `0x008B9E6A` → [SeObjectCreateSaclAccessBits](SeObjectCreateSaclAccessBits_function_008BD8AC.md) (function, `0x008BD8AC`)
- `0x008B9E7C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008B9E9C` → [ObpAdjustCreatorAccessState](../87/ObpAdjustCreatorAccessState_function_00874650.md) (function, `0x00874650`)
- `0x008B9EE1` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x008B9EFF` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x008B9F3D` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x008B9F5C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008B9F85` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008BA043` → [SeReleaseSecurityDescriptor](../97/SeReleaseSecurityDescriptor_function_00975190.md) (function, `0x00975190`)
- `0x008BA057` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008BA064` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008BA079` → [SeDeleteAccessState](../8C/SeDeleteAccessState_function_008C5F70.md) (function, `0x008C5F70`)
- `0x008BA090` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [HalpDmaAllocateChildAdapterV3](../70/HalpDmaAllocateChildAdapterV3_function_007066A0.md) at `0x0070689D`
- [HalpDmaAllocateChildAdapterV2](../70/HalpDmaAllocateChildAdapterV2_function_0070A200.md) at `0x0070A2F3`
- [IoCreateController](../71/IoCreateController_function_0071D190.md) at `0x0071D23B`
- [NtCreateIoRing](../72/NtCreateIoRing_function_00720530.md) at `0x00720964`
- [PopEtEnergyTrackerCreate](../76/PopEtEnergyTrackerCreate_function_00769EE0.md) at `0x0076A16F`
- [TtmpDispatchCreateEventQueue](../77/TtmpDispatchCreateEventQueue_function_00778718.md) at `0x007787EC`
- [TtmiCreateTerminal](../77/TtmiCreateTerminal_function_0077C748.md) at `0x0077C989`
- [NtCreateProcessStateChange](../78/NtCreateProcessStateChange_function_007830C0.md) at `0x00783200`
- [PsCreateCpuPartition](../78/PsCreateCpuPartition_function_00783A8C.md) at `0x00783C45`
- [PspAllocatePartition](../78/PspAllocatePartition_function_0078802C.md) at `0x00788199`
- [PspSessionObjectCreate](../78/PspSessionObjectCreate_function_007892A8.md) at `0x00789556`
- [SepInitializationPhase1](../79/SepInitializationPhase1_function_0079C580.md) at `0x0079C609`
- [SeFilterToken](../79/SeFilterToken_function_0079CD00.md) at `0x0079CDF3`
- [EtwpRegisterPrivateSession](../7B/EtwpRegisterPrivateSession_function_007BC92C.md) at `0x007BCBF9`
- [EtwpSetCoverageSamplerInformation](../7C/EtwpSetCoverageSamplerInformation_function_007C288C.md) at `0x007C2F5F`
- [ExpProfileCreate](../7D/ExpProfileCreate_function_007D1AB8.md) at `0x007D1F40`
- [NtCreateKeyedEvent](../7D/NtCreateKeyedEvent_function_007D4CF0.md) at `0x007D4DC5`
- [sub_00891E2F](../89/Unknown_function_00891E2F.md) at `0x00891F35`
- [sub_00891F9F](../89/Unknown_function_00891F9F.md) at `0x00891FEA`
- [MiCreateSectionCommon](../8A/MiCreateSectionCommon_function_008A9AA4.md) at `0x008A9DE6`
- [NtDuplicateToken](NtDuplicateToken_function_008B6DF0.md) at `0x008B6FE8`
- [NtOpenThreadTokenEx](NtOpenThreadTokenEx_function_008B7840.md) at `0x008B7C4C`
- [ObInsertObject](ObInsertObject_function_008B9100.md) at `0x008B9120`
- [NtCreateEvent](NtCreateEvent_function_008B9140.md) at `0x008B9396`
- [sub_008C28B0](../8C/Unknown_function_008C28B0.md) at `0x008C29FB`
- [NtCreateSemaphore](../8C/NtCreateSemaphore_function_008C38D0.md) at `0x008C3AE7`
- [NtCreateMutant](../8C/NtCreateMutant_function_008C43D0.md) at `0x008C45CD`
- [NtCreateWaitCompletionPacket](../8C/NtCreateWaitCompletionPacket_function_008C4700.md) at `0x008C48E9`
- [WmipCreateGuidObject](../8C/WmipCreateGuidObject_function_008C7930.md) at `0x008C7AD5`
- [PsImpersonateClient](../8C/PsImpersonateClient_function_008CBE10.md) at `0x008CC143`
- [PsImpersonateClient](../8C/PsImpersonateClient_function_008CBE10.md) at `0x008CC2E6`
- [NtCreateJobObject](../91/NtCreateJobObject_function_009177E0.md) at `0x00917ACD`
- [AlpcpCreateClientPort](../92/AlpcpCreateClientPort_function_009270AC.md) at `0x0092748B`
- [PspInsertProcess](../94/PspInsertProcess_function_009472CC.md) at `0x009474AA`
- [PspSchedulerSharedDataRegionCreate](../98/PspSchedulerSharedDataRegionCreate_function_009825DC.md) at `0x00982852`
- [IopLoadDriver](../99/IopLoadDriver_function_00997B54.md) at `0x0099812E`
- [IoCreateDevice](../9A/IoCreateDevice_function_009A4B00.md) at `0x009A4E24`
- [sub_009A5974](../9A/Unknown_function_009A5974.md) at `0x009A5A84`
- [NtCreateWorkerFactory](../9A/NtCreateWorkerFactory_function_009A7E10.md) at `0x009A8148`
- [NtFilterToken](../9C/NtFilterToken_function_009C7890.md) at `0x009C7B8D`
- [NtCreatePrivateNamespace](../9C/NtCreatePrivateNamespace_function_009CA6D0.md) at `0x009CA85A`
- [AlpcpCreateConnectionPort](../9E/AlpcpCreateConnectionPort_function_009E70B0.md) at `0x009E725E`
- [SeCopyClientToken](../9E/SeCopyClientToken_function_009EC5A8.md) at `0x009EC66F`
- [PspInsertThread](../9F/PspInsertThread_function_009F0314.md) at `0x009F09B9`
- [NtCreateTimer](../9F/NtCreateTimer_function_009FF010.md) at `0x009FF13E`
- [NtCreateTimer2](../A2/NtCreateTimer2_function_00A2C660.md) at `0x00A2C7A2`
- [NtCreateIoCompletion](../A2/NtCreateIoCompletion_function_00A2CA60.md) at `0x00A2CB16`
- [ObCreateSymbolicLink](../A3/ObCreateSymbolicLink_function_00A33B98.md) at `0x00A33D29`
- [AlpcpAcceptConnectPort](../A3/AlpcpAcceptConnectPort_function_00A34290.md) at `0x00A34B63`
- [SepCopyAnonymousTokenAndSetSilo](../A3/SepCopyAnonymousTokenAndSetSilo_function_00A3A510.md) at `0x00A3A62A`
- [ObpCreateDirectoryObject](../A5/ObpCreateDirectoryObject_function_00A56230.md) at `0x00A563BA`
- [NtCreateRegistryTransaction](../A6/NtCreateRegistryTransaction_function_00A61370.md) at `0x00A61486`
- [EtwpRealtimeConnect](../A6/EtwpRealtimeConnect_function_00A65C88.md) at `0x00A6606B`
- [NtAllocateReserveObject](../A6/NtAllocateReserveObject_function_00A687A0.md) at `0x00A68892`
- [SeGetLogonSessionToken](../A6/SeGetLogonSessionToken_function_00A6E4B0.md) at `0x00A6E5A1`
- [NtCreateThreadStateChange](../A7/NtCreateThreadStateChange_function_00A77110.md) at `0x00A77283`
- [ExCreateCallback](../A7/ExCreateCallback_function_00A7B9D0.md) at `0x00A7BAED`
- [EtwpCreateUmReplyObject](../A8/EtwpCreateUmReplyObject_function_00A8DBE4.md) at `0x00A8DD94`
- [PspCreateActivityReference](../A8/PspCreateActivityReference_function_00A8F110.md) at `0x00A8F1F3`
- [SeSubProcessToken](../AA/SeSubProcessToken_function_00AAD570.md) at `0x00AADD7E`
- [MmCreateSpecialImageSection](../AB/MmCreateSpecialImageSection_function_00AB7360.md) at `0x00AB74A1`
- [NtCreateLowBoxToken](../AB/NtCreateLowBoxToken_function_00AB9880.md) at `0x00ABA2DC`
- [NtCreateDebugObject](../AC/NtCreateDebugObject_function_00AC2270.md) at `0x00AC23CD`
- [IoCreateDriver](../AC/IoCreateDriver_function_00AC9D70.md) at `0x00AC9FAF`
- [NtQueryInformationToken](../AE/NtQueryInformationToken_function_00AECDD0.md) at `0x00AED75E`
- [NtQueryInformationToken](../AE/NtQueryInformationToken_function_00AECDD0.md) at `0x00AEE9EE`

### Static image references
- `0x008B97BC` → RVA `0x00E0A740` (`.data`; read)
- `0x008B9827` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x008B9843` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x008B99C0` → RVA `0x00FD8010` (`PAGEDATA`; read)
- `0x008B9A7F` → RVA `0x00F0F650` (`.data`; read)
- `0x008B9B05` → RVA `0x008BA2B0` (`SeDefaultObjectMethod`; read)
- `0x008B9C9D` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x008B9ECA` → RVA `0x00B82850` (`ExFreePool`; read)
- `0x008B9FA6` → RVA `0x00E67B90` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **35**
  - `0x008B9806` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008B9817` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008B992D` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x008B9935` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008B9946` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008B99BB` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (`PAGE` → `.text`)
  - `0x008B99EE` → [SepCreateAccessStateFromSubjectContext](../../text/3E/SepCreateAccessStateFromSubjectContext_function_003EBF40.md) (`PAGE` → `.text`)
  - `0x008B9A68` → [SeComputeAutoInheritByObjectTypeEx](../../text/43/SeComputeAutoInheritByObjectTypeEx_function_00433280.md) (`PAGE` → `.text`)
  - `0x008B9ACE` → [SeAssignSecurityEx2](../../text/4E/SeAssignSecurityEx2_function_004E9AA0.md) (`PAGE` → `.text`)
  - `0x008B9B4D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B9B74` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B9BF3` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008B9C09` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B9C35` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x008B9C4A` → [SepDeleteAccessState](../../text/3F/SepDeleteAccessState_function_003FFF20.md) (`PAGE` → `.text`)
  - `0x008B9CB6` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (`PAGE` → `.text`)
  - `0x008B9CE8` → [PspLockThreadSecurityShared](../../text/3C/PspLockThreadSecurityShared_function_003C4720.md) (`PAGE` → `.text`)
  - `0x008B9D17` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x008B9D30` → [PspUnlockThreadSecurityShared](../../text/3C/PspUnlockThreadSecurityShared_function_003C2E40.md) (`PAGE` → `.text`)
  - `0x008B9D42` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008B9D60` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008B9D95` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008B9DB1` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x008B9E18` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008B9E26` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008B9E33` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008B9E7C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008B9EE1` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x008B9EFF` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x008B9F3D` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x008B9F5C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008B9F85` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008BA057` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008BA064` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008BA090` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x008BA070` → [sub_00B1A8FC](../B1/Unknown_function_00B1A8FC.md) (`tail-transfer`)
  - `0x008BA07F` → [sub_00B1A8FC](../B1/Unknown_function_00B1A8FC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008B97A0  40 55                           push rbp
008B97A2  53                              push rbx
008B97A3  56                              push rsi
008B97A4  57                              push rdi
008B97A5  41 54                           push r12
008B97A7  41 55                           push r13
008B97A9  41 56                           push r14
008B97AB  41 57                           push r15
008B97AD  48 8D AC 24 88 FE FF FF         lea rbp, [rsp - 0x178]
008B97B5  48 81 EC 78 02 00 00            sub rsp, 0x278
008B97BC  48 8B 05 7D 0F 55 00            mov rax, qword ptr [rip + 0x550f7d]
008B97C3  48 33 C4                        xor rax, rsp
008B97C6  48 89 85 60 01 00 00            mov qword ptr [rbp + 0x160], rax
008B97CD  48 8B 85 E8 01 00 00            mov rax, qword ptr [rbp + 0x1e8]
008B97D4  48 8B FA                        mov rdi, rdx
008B97D7  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
008B97DB  4C 8B E9                        mov r13, rcx
008B97DE  48 8B 85 F0 01 00 00            mov rax, qword ptr [rbp + 0x1f0]
008B97E5  33 D2                           xor edx, edx
008B97E7  44 89 44 24 64                  mov dword ptr [rsp + 0x64], r8d
008B97EC  41 B8 E0 00 00 00               mov r8d, 0xe0
008B97F2  48 89 4D 98                     mov qword ptr [rbp - 0x68], rcx
008B97F6  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
008B97FD  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
008B9801  44 89 4C 24 70                  mov dword ptr [rsp + 0x70], r9d
008B9806  E8 35 D4 E0 FF                  call 0x1406c6c40
008B980B  33 D2                           xor edx, edx
008B980D  48 8D 4D E0                     lea rcx, [rbp - 0x20]
008B9811  41 B8 A0 00 00 00               mov r8d, 0xa0
008B9817  E8 24 D4 E0 FF                  call 0x1406c6c40
008B981C  49 8B 5D F0                     mov rbx, qword ptr [r13 - 0x10]
008B9820  4D 8D 75 D0                     lea r14, [r13 - 0x30]
008B9824  45 33 C0                        xor r8d, r8d
008B9827  48 8D 15 D2 67 74 FF            lea rdx, [rip - 0x8b982e]
008B982E  49 8B C6                        mov rax, r14
008B9831  45 8B E0                        mov r12d, r8d
008B9834  48 C1 E8 08                     shr rax, 8
008B9838  0F B6 C8                        movzx ecx, al
008B983B  41 0F B6 46 18                  movzx eax, byte ptr [r14 + 0x18]
008B9840  48 33 C8                        xor rcx, rax
008B9843  0F B6 05 02 D6 70 00            movzx eax, byte ptr [rip + 0x70d602]
008B984A  48 33 C8                        xor rcx, rax
008B984D  41 0F B6 46 1A                  movzx eax, byte ptr [r14 + 0x1a]
008B9852  48 8B B4 CA 00 78 FC 00         mov rsi, qword ptr [rdx + rcx*8 + 0xfc7800]
008B985A  A8 02                           test al, 2
008B985C  74 17                           je 0x1408b9875
008B985E  83 E0 03                        and eax, 3
008B9861  0F B6 8C 10 80 FF F0 00         movzx ecx, byte ptr [rax + rdx + 0xf0ff80]
008B9869  49 8B C6                        mov rax, r14
008B986C  48 2B C1                        sub rax, rcx
008B986F  74 04                           je 0x1408b9875
008B9871  4C 8D 60 08                     lea r12, [rax + 8]
008B9875  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B987E  F6 46 42 08                     test byte ptr [rsi + 0x42], 8
008B9882  44 0F B6 B8 32 02 00 00         movzx r15d, byte ptr [rax + 0x232]
008B988A  44 88 7C 24 60                  mov byte ptr [rsp + 0x60], r15b
008B988F  0F 85 CB 00 00 00               jne 0x1408b9960
008B9895  4D 85 E4                        test r12, r12
008B9898  0F 85 C2 00 00 00               jne 0x1408b9960
008B989E  4C 39 43 20                     cmp qword ptr [rbx + 0x20], r8
008B98A2  0F 85 B8 00 00 00               jne 0x1408b9960
008B98A8  48 8B 55 A0                     mov rdx, qword ptr [rbp - 0x60]
008B98AC  4D 89 46 20                     mov qword ptr [r14 + 0x20], r8
008B98B0  48 85 D2                        test rdx, rdx
008B98B3  0F 84 B5 06 00 00               je 0x1408b9f6e
008B98B9  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
008B98BD  45 33 C9                        xor r9d, r9d
008B98C0  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
008B98C5  FF C1                           inc ecx
008B98C7  4C 89 02                        mov qword ptr [rdx], r8
008B98CA  48 8B 55 A8                     mov rdx, qword ptr [rbp - 0x58]
008B98CE  8B 03                           mov eax, dword ptr [rbx]
008B98D0  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
008B98D5  49 8B D5                        mov rdx, r13
008B98D8  44 89 44 24 40                  mov dword ptr [rsp + 0x40], r8d
008B98DD  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
008B98E2  44 8B 44 24 64                  mov r8d, dword ptr [rsp + 0x64]
008B98E7  44 88 7C 24 30                  mov byte ptr [rsp + 0x30], r15b
008B98EC  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
008B98F0  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
008B98F4  33 C9                           xor ecx, ecx
008B98F6  E8 55 20 FB FF                  call 0x14086b950
008B98FB  8B F8                           mov edi, eax
008B98FD  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
008B9901  48 85 C9                        test rcx, rcx
008B9904  0F 85 32 07 00 00               jne 0x1408ba03c
008B990A  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
008B9913  48 8B 8A 40 08 00 00            mov rcx, qword ptr [rdx + 0x840]
008B991A  FF 41 1C                        inc dword ptr [rcx + 0x1c]
008B991D  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008B9921  66 39 01                        cmp word ptr [rcx], ax
008B9924  0F 83 83 05 00 00               jae 0x1408b9ead
008B992A  48 8B D3                        mov rdx, rbx
008B992D  E8 7E 0C E0 FF                  call 0x1406ba5b0
008B9932  49 8B CD                        mov rcx, r13
008B9935  E8 16 FA A3 FF                  call 0x1402f9350
008B993A  8B C7                           mov eax, edi
008B993C  48 8B 8D 60 01 00 00            mov rcx, qword ptr [rbp + 0x160]
008B9943  48 33 CC                        xor rcx, rsp
008B9946  E8 F5 2C DF FF                  call 0x1406ac640
008B994B  48 81 C4 78 02 00 00            add rsp, 0x278
008B9952  41 5F                           pop r15
008B9954  41 5E                           pop r14
008B9956  41 5D                           pop r13
008B9958  41 5C                           pop r12
008B995A  5F                              pop rdi
008B995B  5E                              pop rsi
008B995C  5B                              pop rbx
008B995D  5D                              pop rbp
008B995E  C3                              ret
008B995F  CC                              int3
008B9960  48 85 FF                        test rdi, rdi
008B9963  0F 85 96 00 00 00               jne 0x1408b99ff
008B9969  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008B9972  48 8D 7D E0                     lea rdi, [rbp - 0x20]
008B9976  0F 57 C0                        xorps xmm0, xmm0
008B9979  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
008B997D  F3 0F 7F 45 B8                  movdqu xmmword ptr [rbp - 0x48], xmm0
008B9982  48 8B 81 B8 00 00 00            mov rax, qword ptr [rcx + 0xb8]
008B9989  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
008B998D  48 8B 80 D0 01 00 00            mov rax, qword ptr [rax + 0x1d0]
008B9994  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
008B9998  8B 81 A0 05 00 00               mov eax, dword ptr [rcx + 0x5a0]
008B999E  A8 08                           test al, 8
008B99A0  0F 85 32 03 00 00               jne 0x1408b9cd8
008B99A6  49 8B C0                        mov rax, r8
008B99A9  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
008B99AE  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
008B99B2  BA 53 65 53 75                  mov edx, 0x75536553
008B99B7  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
008B99BB  E8 C0 65 95 FF                  call 0x14020ff80
008B99C0  83 3D 49 E6 71 00 00            cmp dword ptr [rip + 0x71e649], 0
008B99C7  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
008B99CB  0F 85 15 06 00 00               jne 0x1408b9fe6
008B99D1  44 8B 4C 24 64                  mov r9d, dword ptr [rsp + 0x64]
008B99D6  48 8D 46 4C                     lea rax, [rsi + 0x4c]
008B99DA  4C 8D 85 80 00 00 00            lea r8, [rbp + 0x80]
008B99E1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B99E6  48 8D 55 E0                     lea rdx, [rbp - 0x20]
008B99EA  48 8D 4D B0                     lea rcx, [rbp - 0x50]
008B99EE  E8 4D 25 B3 FF                  call 0x1403ebf40
008B99F3  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
008B99F7  85 C0                           test eax, eax
008B99F9  0F 88 5E 03 00 00               js 0x1408b9d5d
008B99FF  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
008B9A03  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
008B9A07  48 89 47 40                     mov qword ptr [rdi + 0x40], rax
008B9A0B  48 85 C0                        test rax, rax
008B9A0E  0F 85 2B 04 00 00               jne 0x1408b9e3f
008B9A14  B9 01 00 00 00                  mov ecx, 1
008B9A19  4D 85 E4                        test r12, r12
008B9A1C  0F 85 6D 01 00 00               jne 0x1408b9b8f
008B9A22  F6 46 42 08                     test byte ptr [rsi + 0x42], 8
008B9A26  0F 84 BF 04 00 00               je 0x1408b9eeb
008B9A2C  44 8B AD E0 01 00 00            mov r13d, dword ptr [rbp + 0x1e0]
008B9A33  4C 8D 4C 24 64                  lea r9, [rsp + 0x64]
008B9A38  48 8B 57 40                     mov rdx, qword ptr [rdi + 0x40]
008B9A3C  33 C0                           xor eax, eax
008B9A3E  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
008B9A42  44 23 E9                        and r13d, ecx
008B9A45  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
008B9A49  45 33 C0                        xor r8d, r8d
008B9A4C  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008B9A51  48 8B CE                        mov rcx, rsi
008B9A54  48 8D 45 80                     lea rax, [rbp - 0x80]
008B9A58  41 C1 E5 04                     shl r13d, 4
008B9A5C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B9A61  C7 45 80 08 00 00 00            mov dword ptr [rbp - 0x80], 8
008B9A68  E8 13 98 B7 FF                  call 0x140433280
008B9A6D  44 8B F8                        mov r15d, eax
008B9A70  85 C0                           test eax, eax
008B9A72  0F 88 0C 06 00 00               js 0x1408ba084
008B9A78  8B 4C 24 64                     mov ecx, dword ptr [rsp + 0x64]
008B9A7C  41 0B CD                        or ecx, r13d
008B9A7F  48 3B 35 CA 5B 65 00            cmp rsi, qword ptr [rip + 0x655bca]
008B9A86  89 4C 24 64                     mov dword ptr [rsp + 0x64], ecx
008B9A8A  0F 84 D6 04 00 00               je 0x1408b9f66
008B9A90  45 33 C9                        xor r9d, r9d
008B9A93  4C 8B 6D 98                     mov r13, qword ptr [rbp - 0x68]
008B9A97  4C 8D 46 4C                     lea r8, [rsi + 0x4c]
008B9A9B  48 8B 57 40                     mov rdx, qword ptr [rdi + 0x40]
008B9A9F  48 8D 47 20                     lea rax, [rdi + 0x20]
008B9AA3  4C 89 6C 24 50                  mov qword ptr [rsp + 0x50], r13
008B9AA8  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
008B9AAD  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
008B9AB2  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008B9AB7  48 8D 45 80                     lea rax, [rbp - 0x80]
008B9ABB  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008B9AC0  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
008B9AC4  33 C9                           xor ecx, ecx
008B9AC6  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
008B9ACB  45 33 C9                        xor r9d, r9d
008B9ACE  E8 CD FF C2 FF                  call 0x1404e9aa0
008B9AD3  44 8B F8                        mov r15d, eax
008B9AD6  85 C0                           test eax, eax
008B9AD8  0F 88 61 02 00 00               js 0x1408b9d3f
008B9ADE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B9AE7  45 33 C0                        xor r8d, r8d
008B9AEA  4C 8B 96 98 00 00 00            mov r10, qword ptr [rsi + 0x98]
008B9AF1  4C 8B 4C 24 78                  mov r9, qword ptr [rsp + 0x78]
008B9AF6  0F B6 88 32 02 00 00            movzx ecx, byte ptr [rax + 0x232]
008B9AFD  41 8D 50 03                     lea edx, [r8 + 3]
008B9B01  88 4C 24 40                     mov byte ptr [rsp + 0x40], cl
008B9B05  48 8D 05 A4 07 00 00            lea rax, [rip + 0x7a4]
008B9B0C  4C 3B D0                        cmp r10, rax
008B9B0F  49 8B CD                        mov rcx, r13
008B9B12  48 8D 46 4C                     lea rax, [rsi + 0x4c]
008B9B16  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008B9B1B  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
008B9B23  0F 85 4D 04 00 00               jne 0x1408b9f76
008B9B29  33 C0                           xor eax, eax
008B9B2B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008B9B30  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B9B35  E8 76 07 00 00                  call 0x1408ba2b0
008B9B3A  44 8B F8                        mov r15d, eax
008B9B3D  85 C0                           test eax, eax
008B9B3F  79 22                           jns 0x1408b9b63
008B9B41  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
008B9B46  48 85 C9                        test rcx, rcx
008B9B49  74 07                           je 0x1408b9b52
008B9B4B  33 D2                           xor edx, edx
008B9B4D  E8 1E 8D 2C 00                  call 0x140b82870
008B9B52  45 33 C0                        xor r8d, r8d
008B9B55  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
008B9B5A  45 85 FF                        test r15d, r15d
008B9B5D  0F 88 DC 01 00 00               js 0x1408b9d3f
008B9B63  80 7B 10 01                     cmp byte ptr [rbx + 0x10], 1
008B9B67  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
008B9B6B  77 0C                           ja 0x1408b9b79
008B9B6D  48 85 C9                        test rcx, rcx
008B9B70  74 07                           je 0x1408b9b79
008B9B72  33 D2                           xor edx, edx
008B9B74  E8 F7 8C 2C 00                  call 0x140b82870
008B9B79  45 33 FF                        xor r15d, r15d
008B9B7C  B9 01 00 00 00                  mov ecx, 1
008B9B81  4C 89 7B 20                     mov qword ptr [rbx + 0x20], r15
008B9B85  4C 89 7F 40                     mov qword ptr [rdi + 0x40], r15
008B9B89  44 0F B6 7C 24 60               movzx r15d, byte ptr [rsp + 0x60]
008B9B8F  48 8B 55 A0                     mov rdx, qword ptr [rbp - 0x60]
008B9B93  33 C0                           xor eax, eax
008B9B95  49 89 46 20                     mov qword ptr [r14 + 0x20], rax
008B9B99  48 85 D2                        test rdx, rdx
008B9B9C  0F 84 CC 01 00 00               je 0x1408b9d6e
008B9BA2  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
008B9BA6  33 F6                           xor esi, esi
008B9BA8  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
008B9BAD  4D 85 E4                        test r12, r12
008B9BB0  48 89 32                        mov qword ptr [rdx], rsi
008B9BB3  48 8B C3                        mov rax, rbx
008B9BB6  48 8B 55 A8                     mov rdx, qword ptr [rbp - 0x58]
008B9BBA  48 0F 44 C6                     cmove rax, rsi
008B9BBE  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
008B9BC3  FF C1                           inc ecx
008B9BC5  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
008B9BC9  4C 8B CF                        mov r9, rdi
008B9BCC  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008B9BD1  45 33 C0                        xor r8d, r8d
008B9BD4  8B 03                           mov eax, dword ptr [rbx]
008B9BD6  49 8B D5                        mov rdx, r13
008B9BD9  44 88 7C 24 30                  mov byte ptr [rsp + 0x30], r15b
008B9BDE  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
008B9BE2  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
008B9BE6  33 C9                           xor ecx, ecx
008B9BE8  E8 63 1D FB FF                  call 0x14086b950
008B9BED  49 8B CD                        mov rcx, r13
008B9BF0  44 8B F8                        mov r15d, eax
008B9BF3  E8 58 F7 A3 FF                  call 0x1402f9350
008B9BF8  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
008B9BFC  48 85 C9                        test rcx, rcx
008B9BFF  74 11                           je 0x1408b9c12
008B9C01  80 7B 10 01                     cmp byte ptr [rbx + 0x10], 1
008B9C05  77 07                           ja 0x1408b9c0e
008B9C07  33 D2                           xor edx, edx
008B9C09  E8 62 8C 2C 00                  call 0x140b82870
008B9C0E  48 89 73 20                     mov qword ptr [rbx + 0x20], rsi
008B9C12  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
008B9C1B  48 8B 8A 40 08 00 00            mov rcx, qword ptr [rdx + 0x840]
008B9C22  FF 41 1C                        inc dword ptr [rcx + 0x1c]
008B9C25  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008B9C29  66 39 01                        cmp word ptr [rcx], ax
008B9C2C  0F 83 D7 02 00 00               jae 0x1408b9f09
008B9C32  48 8B D3                        mov rdx, rbx
008B9C35  E8 76 09 E0 FF                  call 0x1406ba5b0
008B9C3A  48 8D 45 E0                     lea rax, [rbp - 0x20]
008B9C3E  48 3B F8                        cmp rdi, rax
008B9C41  0F 85 89 00 00 00               jne 0x1408b9cd0
008B9C47  48 8B CF                        mov rcx, rdi
008B9C4A  E8 D1 62 B4 FF                  call 0x1403fff20
008B9C4F  83 3D BA E3 71 00 00            cmp dword ptr [rip + 0x71e3ba], 0
008B9C56  0F 85 33 03 00 00               jne 0x1408b9f8f
008B9C5C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B9C65  4C 8B 47 30                     mov r8, qword ptr [rdi + 0x30]
008B9C69  48 8B 90 B8 00 00 00            mov rdx, qword ptr [rax + 0xb8]
008B9C70  0F 0D 8A 48 02 00 00            prefetchw byte ptr [rdx + 0x248]
008B9C77  48 8B 82 48 02 00 00            mov rax, qword ptr [rdx + 0x248]
008B9C7E  48 8B C8                        mov rcx, rax
008B9C81  49 33 C8                        xor rcx, r8
008B9C84  48 83 F9 0F                     cmp rcx, 0xf
008B9C88  0F 83 C6 02 00 00               jae 0x1408b9f54
008B9C8E  48 8D 48 01                     lea rcx, [rax + 1]
008B9C92  F0 48 0F B1 8A 48 02 00 00      lock cmpxchg qword ptr [rdx + 0x248], rcx
008B9C9B  75 E1                           jne 0x1408b9c7e
008B9C9D  83 3D 6C B3 70 00 00            cmp dword ptr [rip + 0x70b36c], 0
008B9CA4  74 15                           je 0x1408b9cbb
008B9CA6  33 D2                           xor edx, edx
008B9CA8  49 8D 48 D0                     lea rcx, [r8 - 0x30]
008B9CAC  41 B9 53 65 53 75               mov r9d, 0x75536553
008B9CB2  44 8D 42 01                     lea r8d, [rdx + 1]
008B9CB6  E8 29 6D 95 FF                  call 0x1402109e4
008B9CBB  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
008B9CBF  48 89 77 30                     mov qword ptr [rdi + 0x30], rsi
008B9CC3  48 85 C9                        test rcx, rcx
008B9CC6  0F 85 AB 01 00 00               jne 0x1408b9e77
008B9CCC  48 89 77 20                     mov qword ptr [rdi + 0x20], rsi
008B9CD0  41 8B C7                        mov eax, r15d
008B9CD3  E9 64 FC FF FF                  jmp 0x1408b993c
008B9CD8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B9CE1  48 8B D0                        mov rdx, rax
008B9CE4  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
008B9CE8  E8 33 AA B0 FF                  call 0x1403c4720
008B9CED  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
008B9CF1  8B 81 A0 05 00 00               mov eax, dword ptr [rcx + 0x5a0]
008B9CF7  A8 08                           test al, 8
008B9CF9  0F 84 48 02 00 00               je 0x1408b9f47
008B9CFF  48 8B 81 38 05 00 00            mov rax, qword ptr [rcx + 0x538]
008B9D06  BA 53 65 53 75                  mov edx, 0x75536553
008B9D0B  48 83 E0 F8                     and rax, 0xfffffffffffffff8
008B9D0F  48 8B C8                        mov rcx, rax
008B9D12  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
008B9D17  E8 F4 69 95 FF                  call 0x140210710
008B9D1C  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
008B9D20  8B 81 38 05 00 00               mov eax, dword ptr [rcx + 0x538]
008B9D26  83 E0 03                        and eax, 3
008B9D29  89 45 B8                        mov dword ptr [rbp - 0x48], eax
008B9D2C  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
008B9D30  E8 0B 91 B0 FF                  call 0x1403c2e40
008B9D35  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
008B9D3A  E9 6F FC FF FF                  jmp 0x1408b99ae
008B9D3F  49 8B CD                        mov rcx, r13
008B9D42  E8 09 F6 A3 FF                  call 0x1402f9350
008B9D47  48 8D 45 E0                     lea rax, [rbp - 0x20]
008B9D4B  48 3B F8                        cmp rdi, rax
008B9D4E  75 80                           jne 0x1408b9cd0
008B9D50  48 8B CF                        mov rcx, rdi
008B9D53  E8 18 C2 00 00                  call 0x1408c5f70
008B9D58  E9 73 FF FF FF                  jmp 0x1408b9cd0
008B9D5D  49 8B CD                        mov rcx, r13
008B9D60  E8 EB F5 A3 FF                  call 0x1402f9350
008B9D65  8B 44 24 68                     mov eax, dword ptr [rsp + 0x68]
008B9D69  E9 CE FB FF FF                  jmp 0x1408b993c
008B9D6E  48 8D 45 E0                     lea rax, [rbp - 0x20]
008B9D72  48 3B F8                        cmp rdi, rax
008B9D75  0F 85 0B 01 00 00               jne 0x1408b9e86
008B9D7B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B9D84  49 8D 4E 10                     lea rcx, [r14 + 0x10]
008B9D88  45 33 C0                        xor r8d, r8d
008B9D8B  33 D2                           xor edx, edx
008B9D8D  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B9D94  90                              nop
008B9D95  E8 96 64 95 FF                  call 0x140210230
008B9D9A  F0 49 0F BA 6E 10 00            lock bts qword ptr [r14 + 0x10], 0
008B9DA1  4C 8B F8                        mov r15, rax
008B9DA4  73 10                           jae 0x1408b9db6
008B9DA6  4D 8D 46 10                     lea r8, [r14 + 0x10]
008B9DAA  48 8B D0                        mov rdx, rax
008B9DAD  49 8D 4E 10                     lea rcx, [r14 + 0x10]
008B9DB1  E8 DA 5E 95 FF                  call 0x14020fc90
008B9DB6  4D 85 FF                        test r15, r15
008B9DB9  74 05                           je 0x1408b9dc0
008B9DBB  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
008B9DC0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B9DC9  45 33 C0                        xor r8d, r8d
008B9DCC  49 8B CE                        mov rcx, r14
008B9DCF  48 8B 90 B8 00 00 00            mov rdx, qword ptr [rax + 0xb8]
008B9DD6  E8 45 B4 0B 00                  call 0x140975220
008B9DDB  44 8B F8                        mov r15d, eax
008B9DDE  41 0F 0D 4E 10                  prefetchw byte ptr [r14 + 0x10]
008B9DE3  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
008B9DE7  41 B8 00 00 00 00               mov r8d, 0
008B9DED  48 8B C8                        mov rcx, rax
008B9DF0  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
008B9DF4  48 83 F9 10                     cmp rcx, 0x10
008B9DF8  48 8D 50 F0                     lea rdx, [rax - 0x10]
008B9DFC  49 0F 46 D0                     cmovbe rdx, r8
008B9E00  A8 02                           test al, 2
008B9E02  0F 85 F3 00 00 00               jne 0x1408b9efb
008B9E08  F0 49 0F B1 56 10               lock cmpxchg qword ptr [r14 + 0x10], rdx
008B9E0E  0F 85 E7 00 00 00               jne 0x1408b9efb
008B9E14  49 8D 4E 10                     lea rcx, [r14 + 0x10]
008B9E18  E8 E3 77 A2 FF                  call 0x1402e1600
008B9E1D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008B9E26  E8 C5 51 9A FF                  call 0x14025eff0
008B9E2B  45 85 FF                        test r15d, r15d
008B9E2E  79 08                           jns 0x1408b9e38
008B9E30  49 8B CD                        mov rcx, r13
008B9E33  E8 18 F5 A3 FF                  call 0x1402f9350
008B9E38  33 F6                           xor esi, esi
008B9E3A  E9 B9 FD FF FF                  jmp 0x1408b9bf8
008B9E3F  48 8B C8                        mov rcx, rax
008B9E42  E8 A9 35 00 00                  call 0x1408bd3f0
008B9E47  84 C0                           test al, al
008B9E49  0F 84 12 02 00 00               je 0x1408ba061
008B9E4F  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
008B9E53  F6 41 02 10                     test byte ptr [rcx + 2], 0x10
008B9E57  0F 84 B7 FB FF FF               je 0x1408b9a14
008B9E5D  F7 47 14 00 00 00 01            test dword ptr [rdi + 0x14], 0x1000000
008B9E64  0F 85 AA FB FF FF               jne 0x1408b9a14
008B9E6A  E8 3D 3A 00 00                  call 0x1408bd8ac
008B9E6F  09 47 10                        or dword ptr [rdi + 0x10], eax
008B9E72  E9 9D FB FF FF                  jmp 0x1408b9a14
008B9E77  BA 53 65 53 75                  mov edx, 0x75536553
008B9E7C  E8 5F DA A3 FF                  call 0x1402f78e0
008B9E81  E9 46 FE FF FF                  jmp 0x1408b9ccc
008B9E86  F7 03 00 04 00 00               test dword ptr [rbx], 0x400
008B9E8C  4D 8B CD                        mov r9, r13
008B9E8F  41 0F B6 D7                     movzx edx, r15b
008B9E93  4C 8B C6                        mov r8, rsi
008B9E96  0F 45 D1                        cmovne edx, ecx
008B9E99  48 8B CF                        mov rcx, rdi
008B9E9C  E8 AF A7 FB FF                  call 0x140874650
008B9EA1  44 8B F8                        mov r15d, eax
008B9EA4  85 C0                           test eax, eax
008B9EA6  78 88                           js 0x1408b9e30
008B9EA8  E9 CE FE FF FF                  jmp 0x1408b9d7b
008B9EAD  FF 41 20                        inc dword ptr [rcx + 0x20]
008B9EB0  48 8B 8A 48 08 00 00            mov rcx, qword ptr [rdx + 0x848]
008B9EB7  FF 41 1C                        inc dword ptr [rcx + 0x1c]
008B9EBA  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008B9EBE  66 39 01                        cmp word ptr [rcx], ax
008B9EC1  0F 82 63 FA FF FF               jb 0x1408b992a
008B9EC7  FF 41 20                        inc dword ptr [rcx + 0x20]
008B9ECA  48 8D 05 7F 89 2C 00            lea rax, [rip + 0x2c897f]
008B9ED1  48 8B 51 38                     mov rdx, qword ptr [rcx + 0x38]
008B9ED5  48 8B CB                        mov rcx, rbx
008B9ED8  48 3B D0                        cmp rdx, rax
008B9EDB  0F 85 73 01 00 00               jne 0x1408ba054
008B9EE1  E8 6A 89 2C 00                  call 0x140b82850
008B9EE6  E9 47 FA FF FF                  jmp 0x1408b9932
008B9EEB  48 83 7B 20 00                  cmp qword ptr [rbx + 0x20], 0
008B9EF0  0F 85 36 FB FF FF               jne 0x1408b9a2c
008B9EF6  E9 94 FC FF FF                  jmp 0x1408b9b8f
008B9EFB  49 8D 4E 10                     lea rcx, [r14 + 0x10]
008B9EFF  E8 CC 99 9A FF                  call 0x1402638d0
008B9F04  E9 0B FF FF FF                  jmp 0x1408b9e14
008B9F09  FF 41 20                        inc dword ptr [rcx + 0x20]
008B9F0C  48 8B 8A 48 08 00 00            mov rcx, qword ptr [rdx + 0x848]
008B9F13  FF 41 1C                        inc dword ptr [rcx + 0x1c]
008B9F16  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008B9F1A  66 39 01                        cmp word ptr [rcx], ax
008B9F1D  0F 82 0F FD FF FF               jb 0x1408b9c32
008B9F23  FF 41 20                        inc dword ptr [rcx + 0x20]
008B9F26  48 8D 05 23 89 2C 00            lea rax, [rip + 0x2c8923]
008B9F2D  48 8B 51 38                     mov rdx, qword ptr [rcx + 0x38]
008B9F31  48 8B CB                        mov rcx, rbx
008B9F34  48 3B D0                        cmp rdx, rax
008B9F37  0F 85 50 01 00 00               jne 0x1408ba08d
008B9F3D  E8 0E 89 2C 00                  call 0x140b82850
008B9F42  E9 F3 FC FF FF                  jmp 0x1408b9c3a
008B9F47  45 33 C0                        xor r8d, r8d
008B9F4A  4C 89 44 24 68                  mov qword ptr [rsp + 0x68], r8
008B9F4F  E9 D8 FD FF FF                  jmp 0x1408b9d2c
008B9F54  BA 53 65 53 75                  mov edx, 0x75536553
008B9F59  49 8B C8                        mov rcx, r8
008B9F5C  E8 7F D9 A3 FF                  call 0x1402f78e0
008B9F61  E9 55 FD FF FF                  jmp 0x1408b9cbb
008B9F66  41 B1 01                        mov r9b, 1
008B9F69  E9 25 FB FF FF                  jmp 0x1408b9a93
008B9F6E  41 8B F8                        mov edi, r8d
008B9F71  E9 87 F9 FF FF                  jmp 0x1408b98fd
008B9F76  33 C0                           xor eax, eax
008B9F78  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008B9F7D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B9F82  49 8B C2                        mov rax, r10
008B9F85  E8 46 0B E0 FF                  call 0x1406baad0
008B9F8A  E9 AB FB FF FF                  jmp 0x1408b9b3a
008B9F8F  48 8B 47 30                     mov rax, qword ptr [rdi + 0x30]
008B9F93  48 85 C0                        test rax, rax
008B9F96  74 1C                           je 0x1408b9fb4
008B9F98  48 8B 80 78 04 00 00            mov rax, qword ptr [rax + 0x478]
008B9F9F  F0 FF 88 1C 01 00 00            lock dec dword ptr [rax + 0x11c]
008B9FA6  48 8B 05 E3 DB 5A 00            mov rax, qword ptr [rip + 0x5adbe3]
008B9FAD  48 39 47 30                     cmp qword ptr [rdi + 0x30], rax
008B9FB1  75 01                           jne 0x1408b9fb4
008B9FB3  CC                              int3
008B9FB4  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
008B9FB8  48 85 C0                        test rax, rax
008B9FBB  0F 84 9B FC FF FF               je 0x1408b9c5c
008B9FC1  48 8B 80 78 04 00 00            mov rax, qword ptr [rax + 0x478]
008B9FC8  F0 FF 88 1C 01 00 00            lock dec dword ptr [rax + 0x11c]
008B9FCF  48 8B 05 BA DB 5A 00            mov rax, qword ptr [rip + 0x5adbba]
008B9FD6  48 39 47 20                     cmp qword ptr [rdi + 0x20], rax
008B9FDA  0F 85 7C FC FF FF               jne 0x1408b9c5c
008B9FE0  CC                              int3
008B9FE1  E9 76 FC FF FF                  jmp 0x1408b9c5c
008B9FE6  48 85 C0                        test rax, rax
008B9FE9  74 4A                           je 0x1408ba035
008B9FEB  48 8B 88 78 04 00 00            mov rcx, qword ptr [rax + 0x478]
008B9FF2  F0 FF 81 1C 01 00 00            lock inc dword ptr [rcx + 0x11c]
008B9FF9  48 3B 05 90 DB 5A 00            cmp rax, qword ptr [rip + 0x5adb90]
008BA000  75 01                           jne 0x1408ba003
008BA002  CC                              int3
008BA003  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
008BA007  48 85 C0                        test rax, rax
008BA00A  0F 84 C1 F9 FF FF               je 0x1408b99d1
008BA010  48 8B 80 78 04 00 00            mov rax, qword ptr [rax + 0x478]
008BA017  F0 FF 80 1C 01 00 00            lock inc dword ptr [rax + 0x11c]
008BA01E  48 8B 05 6B DB 5A 00            mov rax, qword ptr [rip + 0x5adb6b]
008BA025  48 39 45 B0                     cmp qword ptr [rbp - 0x50], rax
008BA029  0F 85 A2 F9 FF FF               jne 0x1408b99d1
008BA02F  CC                              int3
008BA030  E9 9C F9 FF FF                  jmp 0x1408b99d1
008BA035  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
008BA03A  EB CB                           jmp 0x1408ba007
008BA03C  0F B6 53 10                     movzx edx, byte ptr [rbx + 0x10]
008BA040  41 B0 01                        mov r8b, 1
008BA043  E8 48 B1 0B 00                  call 0x140975190
008BA048  45 33 C0                        xor r8d, r8d
008BA04B  4C 89 43 20                     mov qword ptr [rbx + 0x20], r8
008BA04F  E9 B6 F8 FF FF                  jmp 0x1408b990a
008BA054  48 8B C2                        mov rax, rdx
008BA057  E8 74 0A E0 FF                  call 0x1406baad0
008BA05C  E9 D1 F8 FF FF                  jmp 0x1408b9932
008BA061  49 8B CD                        mov rcx, r13
008BA064  E8 E7 F2 A3 FF                  call 0x1402f9350
008BA069  48 8D 45 E0                     lea rax, [rbp - 0x20]
008BA06D  48 3B F8                        cmp rdi, rax
008BA070  0F 85 86 08 26 00               jne 0x140b1a8fc
008BA076  48 8B CF                        mov rcx, rdi
008BA079  E8 F2 BE 00 00                  call 0x1408c5f70
008BA07E  90                              nop
008BA07F  E9 78 08 26 00                  jmp 0x140b1a8fc
008BA084  4C 8B 6D 98                     mov r13, qword ptr [rbp - 0x68]
008BA088  E9 B2 FC FF FF                  jmp 0x1408b9d3f
008BA08D  48 8B C2                        mov rax, rdx
008BA090  E8 3B 0A E0 FF                  call 0x1406baad0
008BA095  E9 A0 FB FF FF                  jmp 0x1408b9c3a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObInsertObjectEx(__int64 a1, __int64 a2, int a3, int a4, unsigned int a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned int v_stack_m248;
    unsigned int v_stack_m254;
    unsigned __int8 v_stack_m258;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned int v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned __int8 v_stack_m288;
    unsigned int v_stack_m290;
    unsigned int v_stack_m298;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int8 v_stack_p60;
    unsigned int v_stack_p64;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_rsp = (v_rsp) - (632);
    result = (*(unsigned __int64 *)(v_rip + 5574525)) ^ (v_rsp);
    v_stack_m58 = result;
    v_stack_m210 = a6;
    a2 = 0;
    v_stack_m254 = a3;
    v_stack_m220 = a1;
    v_stack_m218 = a7;
    v_stack_m248 = a4;
    result = memset(v_stack_m138, a2, 224, a4);
    a2 = 0;
    result = memset(v_stack_m1D8, a2, 160, a4);
    a3 = 0;
    result = (a1 - 48) >> (8);
    a1 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(a1 - 48 + 24));
    a1 = (a1) ^ (*(unsigned __int8 *)(v_rip + 7394818));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 - 48 + 26))) & (2)) == 0) goto loc_008B9875;
    result = (unsigned int)((*(unsigned __int8 *)(a1 - 48 + 26)) & (3));
    result = (a1 - 48) - (*(unsigned __int8 *)(result + v_rip - 9148462 * 1 + 15794048));
    v_r12 = 0;
    if (!(condition_is_equal)) {
        v_r12 = result + 8;
    }
    v_stack_m258 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 9148462 + a1 * 8 + 16545792) + 66)) & (8)) != 0) goto loc_008B9960;
    if (v_r12 != 0) goto loc_008B9960;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 32)) != 0) goto loc_008B9960;
    *(unsigned __int64 *)(a1 - 48 + 32) = 0;
    if (v_stack_m218 == 0) goto loc_008B9F6E;
    a4 = 0;
    v_stack_m268 = v_stack_m218;
    a1 = (unsigned int)(((unsigned int)(v_stack_m248)) + 1);
    *(unsigned __int64 *)(v_stack_m218) = 0;
    v_stack_m270 = v_stack_m210;
    v_stack_m278 = 0;
    v_stack_m280 = 0;
    v_stack_m288 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m290 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 - 16))));
    v_stack_m298 = (unsigned int)(a1);
    a1 = 0;
    result = ObpCreateHandle(a1, a1, (unsigned int)(v_stack_m254), a4);
loc_008B98FD:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 32) != 0) goto loc_008BA03C;
loc_008B990A:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112))) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112) + 16)))) goto loc_008B9EAD;
loc_008B992A:
    result = ExpInterlockedPushEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112), *(unsigned __int64 *)(a1 - 16), (unsigned int)(v_stack_m254), a4);
loc_008B9932:
    result = ObfDereferenceObject(0, *(unsigned __int64 *)(a1 - 16), (unsigned int)(v_stack_m254), a4);
loc_008B993C:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(a1 - 16), (unsigned int)(v_stack_m254), a4);
    v_rsp = (v_rsp) + (632);
    return result;
loc_008B9960:
    if ((unsigned int)((unsigned int)(result)) != 0) goto loc_008B99FF;
    v_stack_m228 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m200 = v_xmm0;
    v_stack_m230 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_m1F0 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 464);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (8)) != 0) goto loc_008B9CD8;
    v_stack_p68 = (unsigned int)(v_stack_m254);
loc_008B99AE:
    v_stack_m208 = (unsigned int)(v_stack_m254);
    result = PsReferencePrimaryTokenWithTag(v_stack_m230, (unsigned int)(0x75536553ULL), (unsigned int)(v_stack_m254), a4);
    v_stack_m1F8 = result;
    if ((*(unsigned int *)(v_rip + 7464521)) != 0) goto loc_008B9FE6;
loc_008B99D1:
    v_stack_p20 = *(unsigned __int64 *)(v_rip - 9148462 + a1 * 8 + 16545792) + 76;
    result = SepCreateAccessStateFromSubjectContext(v_stack_m208, v_stack_m1D8, v_stack_m138, (unsigned int)(v_stack_p64));
    v_stack_p68 = (unsigned int)(result);
    if (sign_flag) goto loc_008B9D5D;
loc_008B99FF:
    v_stack_m230 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 32);
    *(unsigned __int64 *)(v_stack_m1D8 + 64) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 32);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 32) != 0) goto loc_008B9E3F;
loc_008B9A14:
    if (v_r12 != 0) goto loc_008B9B8F;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 9148462 + a1 * 8 + 16545792) + 66)) & (8)) == 0) goto loc_008B9EEB;
loc_008B9A2C:
    result = 0;
    v_stack_m238 = 0;
    v_r13 = (unsigned int)(((unsigned int)(a5)) & (1));
    v_stack_p64 = 0;
    a3 = 0;
    v_stack_p78 = 0;
    v_r13 = (unsigned int)((v_r13) << (4));
    v_stack_p20 = v_stack_m238;
    v_stack_m238 = 8;
    result = SeComputeAutoInheritByObjectTypeEx(*(unsigned __int64 *)(v_rip - 9148462 + a1 * 8 + 16545792), *(unsigned __int64 *)(v_stack_m1D8 + 64), a3, v_stack_p64);
    if (sign_flag) goto loc_008BA084;
    a1 = (unsigned int)(((unsigned int)(v_stack_p64)) | ((unsigned int)(v_r13)));
    v_stack_p64 = (unsigned int)(a1);
    if ((*(unsigned __int64 *)(v_rip - 9148462 + a1 * 8 + 16545792)) == (*(unsigned __int64 *)(v_rip + 6642634))) goto loc_008B9F66;
    a4 = 0;
loc_008B9A93:
    v_stack_p50 = v_stack_m220;
    v_stack_p40 = *(unsigned __int64 *)(v_rip - 9148462 + a1 * 8 + 16545792) + 76;
    v_stack_p38 = v_stack_m1D8 + 32;
    v_stack_p30 = v_stack_m238;
    v_stack_p28 = (unsigned int)(a1);
    a1 = 0;
    v_stack_p20 = 0;
    a4 = 0;
    result = SeAssignSecurityEx2(a1, *(unsigned __int64 *)(v_stack_m1D8 + 64), v_stack_p78, a4);
    if (sign_flag) goto loc_008B9D3F;
    a3 = 0;
    v_stack_p40 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_p38 = *(unsigned __int64 *)(v_rip - 9148462 + a1 * 8 + 16545792) + 76;
    v_stack_p30 = 1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9148462 + a1 * 8 + 16545792) + 152)) != (v_rip + 1956)) goto loc_008B9F76;
    result = 0;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = SeDefaultObjectMethod(v_stack_m220, a3 + 3, a3, v_stack_p78);
loc_008B9B3A:
    if (!sign_flag) goto loc_008B9B63;
    if (v_stack_p78 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_p78, a2, a3, v_stack_p78);
    }
    a3 = 0;
    v_stack_p78 = 0;
    if (sign_flag) goto loc_008B9D3F;
loc_008B9B63:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 - 16) + 16)) > 1) goto loc_008B9B79;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 32) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 32), a2, a3, v_stack_p78);
    }
    v_r15 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 32) = 0;
    *(unsigned __int64 *)(v_stack_m1D8 + 64) = 0;
loc_008B9B8F:
    result = 0;
    *(unsigned __int64 *)(a1 - 48 + 32) = 0;
    if (v_stack_m218 == 0) goto loc_008B9D6E;
    v_rsi = 0;
    v_stack_p50 = v_stack_m218;
    *(unsigned __int64 *)(v_stack_m218) = 0;
    result = *(unsigned __int64 *)(a1 - 16);
    if (v_r12 == 0) { result = 0; }
    v_stack_p48 = v_stack_m210;
    a1 = (unsigned int)(((unsigned int)(v_stack_p70)) + 1);
    v_stack_p40 = 0;
    v_stack_p38 = result;
    a3 = 0;
    v_stack_p30 = (unsigned __int8)(v_stack_p60);
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 - 16))));
    v_stack_p20 = (unsigned int)(a1);
    a1 = 0;
    result = ObpCreateHandle(a1, v_stack_m220, a3, v_stack_m1D8);
    result = ObfDereferenceObject(v_stack_m220, v_stack_m220, a3, v_stack_m1D8);
loc_008B9BF8:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 32) == 0) goto loc_008B9C12;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 - 16) + 16)) <= 1) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 32), a2, a3, v_stack_m1D8);
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 32) = 0;
loc_008B9C12:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112))) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112) + 16)))) goto loc_008B9F09;
loc_008B9C32:
    result = ExpInterlockedPushEntrySList(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 2112), *(unsigned __int64 *)(a1 - 16), a3, v_stack_m1D8);
loc_008B9C3A:
    if (v_stack_m1D8 != v_stack_m1D8) goto loc_008B9CD0;
    result = SepDeleteAccessState(v_stack_m1D8, *(unsigned __int64 *)(a1 - 16), a3, v_stack_m1D8);
    if ((*(unsigned int *)(v_rip + 7463866)) != 0) goto loc_008B9F8F;
loc_008B9C5C:
loc_008B9C7E:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 584)) ^ (*(unsigned __int64 *)(v_stack_m1D8 + 48));
    if (a1 >= 15) goto loc_008B9F54;
    if (a1 != 15) goto loc_008B9C7E;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 584);
    if ((*(unsigned int *)(v_rip + 7385964)) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_stack_m1D8 + 48) - 48;
        a4 = 0x75536553ULL;
        a3 = a2 + 1;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(v_stack_m1D8 + 48) = 0;
    if (*(unsigned __int64 *)(v_stack_m1D8 + 32) != 0) goto loc_008B9E77;
loc_008B9CCC:
    *(unsigned __int64 *)(v_stack_m1D8 + 32) = 0;
loc_008B9CD0:
    goto loc_008B993C;
loc_008B9CD8:
    v_stack_m1E8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = PspLockThreadSecurityShared(*(unsigned __int64 *)(v_stack_m1D8 + 32), *(unsigned __int64 *)(gs_base + (0 + 392)), a3, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m228 + 1440)))) & (8)) == 0) goto loc_008B9F47;
    result = (*(unsigned __int64 *)(v_stack_m228 + 1336)) & (-8);
    v_stack_p68 = result;
    result = ObfReferenceObjectWithTag(result, (unsigned int)(0x75536553ULL), a3, a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m228 + 1336))) & (3));
    v_stack_m200 = (unsigned int)(result);
loc_008B9D2C:
    result = PspUnlockThreadSecurityShared(v_stack_m228, v_stack_m1E8, a3, a4);
    goto loc_008B99AE;
loc_008B9D3F:
    result = ObfDereferenceObject(v_stack_m220, v_stack_m1E8, a3, a4);
    if (v_stack_m1D8 != v_stack_m1D8) goto loc_008B9CD0;
    result = SeDeleteAccessState(v_stack_m1D8, v_stack_m1E8, a3, a4);
    goto loc_008B9CD0;
loc_008B9D5D:
    result = ObfDereferenceObject(v_stack_m220, v_stack_m1E8, a3, a4);
    goto loc_008B993C;
loc_008B9D6E:
    if (v_stack_m1D8 != v_stack_m1D8) goto loc_008B9E86;
loc_008B9D7B:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 - 48 + 16, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 - 48 + 16;
        a2 = result;
        a1 = a1 - 48 + 16;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a3 = 0;
    result = ObpChargeQuotaForObject(a1 - 48, *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3, a4);
    a1 = (*(unsigned __int64 *)(a1 - 48 + 16)) & (-16);
    a2 = *(unsigned __int64 *)(a1 - 48 + 16) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 - 48 + 16))) & (2)) != 0) goto loc_008B9EFB;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 - 48 + 16))) & (2)) != 0) goto loc_008B9EFB;
loc_008B9E14:
    result = KeAbPostRelease(a1 - 48 + 16, a2, 0, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, 0, a4);
    if (sign_flag) {
        a1 = v_stack_m220;
        result = ObfDereferenceObject(a1, a2, 0, a4);
    }
    v_rsi = 0;
    goto loc_008B9BF8;
loc_008B9E3F:
    result = RtlValidSecurityDescriptor(result, a2, 0, a4);
    if ((unsigned __int8)(result) == 0) goto loc_008BA061;
    if (((*(unsigned __int8 *)(v_stack_m230 + 2)) & (16)) == 0) goto loc_008B9A14;
    if (((*(unsigned int *)(v_stack_m1D8 + 20)) & (0x1000000ULL)) != 0) goto loc_008B9A14;
    result = SeObjectCreateSaclAccessBits(v_stack_m230, a2, 0, a4);
    goto loc_008B9A14;
loc_008B9E77:
    result = ObfDereferenceObjectWithTag(v_stack_m230, (unsigned int)(0x75536553ULL), 0, a4);
    goto loc_008B9CCC;
loc_008B9E86:
    a2 = (unsigned __int8)((unsigned int)((unsigned int)(result)));
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 - 16))) & (0x400ULL)) != 0) { a2 = (unsigned int)(v_stack_m230); }
    result = ObpAdjustCreatorAccessState(v_stack_m1D8, a2, 0, v_stack_m220);
    if (sign_flag) goto loc_008B9E30;
    goto loc_008B9D7B;
loc_008B9EAD:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 2120))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 2120) + 16)))) goto loc_008B992A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 2120) + 56)) != (v_rip + 2918783)) goto loc_008BA054;
    result = ExFreePool(*(unsigned __int64 *)(a1 - 16), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 2120) + 56), 0, v_stack_m220);
    goto loc_008B9932;
loc_008B9EEB:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 32)) != 0) goto loc_008B9A2C;
    goto loc_008B9B8F;
loc_008B9EFB:
    result = ExfReleasePushLock(a1 - 48 + 16, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 2120) + 56), 0, v_stack_m220);
    goto loc_008B9E14;
loc_008B9F09:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 2120) + 56) + 2120))) < ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 2120) + 56) + 2120) + 16)))) goto loc_008B9C32;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 2120) + 56) + 2120) + 56)) != (v_rip + 2918691)) goto loc_008BA08D;
    result = ExFreePool(*(unsigned __int64 *)(a1 - 16), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 2120) + 56) + 2120) + 56), 0, v_stack_m220);
    goto loc_008B9C3A;
loc_008B9F47:
    a3 = 0;
    v_stack_p68 = 0;
    goto loc_008B9D2C;
loc_008B9F54:
    result = ObfDereferenceObjectWithTag(0, (unsigned int)(0x75536553ULL), a3, v_stack_m220);
    goto loc_008B9CBB;
loc_008B9F66:
    goto loc_008B9A93;
loc_008B9F6E:
    goto loc_008B98FD;
loc_008B9F76:
    result = 0;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = guard_dispatch_icall(0, (unsigned int)(0x75536553ULL), a3, 1);
    goto loc_008B9B3A;
loc_008B9F8F:
    if (*(unsigned __int64 *)(0 + 48) == 0) goto loc_008B9FB4;
    if ((*(unsigned __int64 *)(0 + 48)) == (*(unsigned __int64 *)(v_rip + 5954531))) {
    }
    if (*(unsigned __int64 *)(0 + 32) == 0) goto loc_008B9C5C;
    if ((*(unsigned __int64 *)(0 + 32)) != (*(unsigned __int64 *)(v_rip + 5954490))) goto loc_008B9C5C;
    goto loc_008B9C5C;
loc_008B9FE6:
    if (*(unsigned __int64 *)(v_rip + 5954490) == 0) goto loc_008BA035;
    if ((*(unsigned __int64 *)(v_rip + 5954490)) == (*(unsigned __int64 *)(v_rip + 5954448))) {
    }
loc_008BA007:
    if (v_stack_m208 == 0) goto loc_008B99D1;
    if (v_stack_m208 != (*(unsigned __int64 *)(v_rip + 5954411))) goto loc_008B99D1;
    goto loc_008B99D1;
loc_008BA035:
    goto loc_008BA007;
loc_008BA03C:
    result = SeReleaseSecurityDescriptor(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5954490) + 1144), *(unsigned __int8 *)(*(unsigned __int64 *)(a1 - 16) + 16), 1, 1);
    a3 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 - 16) + 32) = 0;
    goto loc_008B990A;
loc_008BA054:
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5954490) + 1144), *(unsigned __int8 *)(*(unsigned __int64 *)(a1 - 16) + 16), a3, 1);
    goto loc_008B9932;
loc_008BA061:
    result = ObfDereferenceObject(v_stack_m220, *(unsigned __int8 *)(*(unsigned __int64 *)(a1 - 16) + 16), a3, 1);
    result = SeDeleteAccessState(0, *(unsigned __int8 *)(*(unsigned __int64 *)(a1 - 16) + 16), a3, 1);
loc_008BA084:
    goto loc_008B9D3F;
loc_008BA08D:
    result = guard_dispatch_icall(0, *(unsigned __int8 *)(*(unsigned __int64 *)(a1 - 16) + 16), a3, 1);
    goto loc_008B9C3A;
}
```

## 5. (Beta) C Style

```c
int64_t ObInsertObjectEx(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, uint32_t Arg5, int64_t Arg6, int64_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m138;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint32_t v_stack_m248;
    uint32_t v_stack_m254;
    uint8_t v_stack_m258;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint32_t v_stack_m278;
    uint64_t v_stack_m280;
    uint8_t v_stack_m288;
    uint32_t v_stack_m290;
    uint32_t v_stack_m298;
    uint64_t v_stack_m58;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint8_t v_stack_p60;
    uint32_t v_stack_p64;
    uint64_t v_stack_p68;
    uint32_t v_stack_p70;
    uint64_t v_stack_p78;

    local_rsp = (local_rsp) - (632);
    result = (*(uint64_t *)(v_rip + 0x550F7D)) ^ (local_rsp);
    v_stack_m58 = result;
    v_stack_m210 = Arg6;
    Arg2 = 0;
    v_stack_m254 = Arg3;
    v_stack_m220 = Arg1;
    v_stack_m218 = Arg7;
    v_stack_m248 = Arg4;
    result = memset(v_stack_m138, Arg2, 224, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m1D8, Arg2, 160, Arg4);
    Arg3 = 0;
    result = (Arg1 - 48) >> (8);
    Arg1 = ((uint8_t)(result)) ^ (*(uint8_t *)(arg1 - 0x30 + 0x18));
    Arg1 = (Arg1) ^ (*(uint8_t *)(v_rip + 0x70D602));
    if ((((uint8_t)(*(uint8_t *)(arg1 - 0x30 + 0x1A))) & (2)) == 0) goto loc_008B9875;
    result = (uint32_t)((*(uint8_t *)(arg1 - 0x30 + 0x1A)) & (3));
    result = (Arg1 - 48) - (*(uint8_t *)(result + v_rip - 0x8B982E * 1 + 0xF0FF80));
    local_r12 = 0;
    if (!(condition_is_equal)) {
        local_r12 = result + 8;
    }
    v_stack_m258 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (((*(uint8_t *)(*(uint64_t *)(v_rip - 0x8B982E + arg1 * 8 + 0xFC7800) + 0x42)) & (8)) != 0) goto loc_008B9960;
    if (local_r12 != 0) goto loc_008B9960;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 - 0x10) + 0x20)) != 0) goto loc_008B9960;
    *(uint64_t *)(arg1 - 0x30 + 0x20) = 0;
    if (v_stack_m218 == 0) goto loc_008B9F6E;
    Arg4 = 0;
    v_stack_m268 = v_stack_m218;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m248)) + 1);
    *(uint64_t *)(v_stack_m218) = 0;
    v_stack_m270 = v_stack_m210;
    v_stack_m278 = 0;
    v_stack_m280 = 0;
    v_stack_m288 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m290 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 - 0x10))));
    v_stack_m298 = (uint32_t)(Arg1);
    Arg1 = 0;
    result = ObpCreateHandle(Arg1, Arg1, (uint32_t)(v_stack_m254), Arg4);
loc_008B98FD:
    if (*(uint64_t *)(*(uint64_t *)(arg1 - 0x10) + 0x20) != 0) goto loc_008BA03C;
loc_008B990A:
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840))) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840) + 0x10)))) goto loc_008B9EAD;
loc_008B992A:
    result = ExpInterlockedPushEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840), *(uint64_t *)(arg1 - 0x10), (uint32_t)(v_stack_m254), Arg4);
loc_008B9932:
    result = ObfDereferenceObject(0, *(uint64_t *)(arg1 - 0x10), (uint32_t)(v_stack_m254), Arg4);
loc_008B993C:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(arg1 - 0x10), (uint32_t)(v_stack_m254), Arg4);
    local_rsp = (local_rsp) + (632);
    return result;
loc_008B9960:
    if ((uint32_t)((uint32_t)(result)) != 0) goto loc_008B99FF;
    v_stack_m228 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m200 = v_xmm0;
    v_stack_m230 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_m1F0 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1D0);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (8)) != 0) goto loc_008B9CD8;
    v_stack_p68 = (uint32_t)(v_stack_m254);
loc_008B99AE:
    v_stack_m208 = (uint32_t)(v_stack_m254);
    result = PsReferencePrimaryTokenWithTag(v_stack_m230, (uint32_t)(0x75536553ULL), (uint32_t)(v_stack_m254), Arg4);
    v_stack_m1F8 = result;
    if ((*(uint32_t *)(v_rip + 0x71E649)) != 0) goto loc_008B9FE6;
loc_008B99D1:
    v_stack_p20 = *(uint64_t *)(v_rip - 0x8B982E + arg1 * 8 + 0xFC7800) + 76;
    result = SepCreateAccessStateFromSubjectContext(v_stack_m208, v_stack_m1D8, v_stack_m138, (uint32_t)(v_stack_p64));
    v_stack_p68 = (uint32_t)(result);
    if (sign_flag) goto loc_008B9D5D;
loc_008B99FF:
    v_stack_m230 = *(uint64_t *)(*(uint64_t *)(arg1 - 0x10) + 0x20);
    *(uint64_t *)(v_stack_m1D8 + 0x40) = *(uint64_t *)(*(uint64_t *)(arg1 - 0x10) + 0x20);
    if (*(uint64_t *)(*(uint64_t *)(arg1 - 0x10) + 0x20) != 0) goto loc_008B9E3F;
loc_008B9A14:
    if (local_r12 != 0) goto loc_008B9B8F;
    if (((*(uint8_t *)(*(uint64_t *)(v_rip - 0x8B982E + arg1 * 8 + 0xFC7800) + 0x42)) & (8)) == 0) goto loc_008B9EEB;
loc_008B9A2C:
    result = 0;
    v_stack_m238 = 0;
    local_r13 = (uint32_t)(((uint32_t)(Arg5)) & (1));
    v_stack_p64 = 0;
    Arg3 = 0;
    v_stack_p78 = 0;
    local_r13 = (uint32_t)((local_r13) << (4));
    v_stack_p20 = v_stack_m238;
    v_stack_m238 = 8;
    result = SeComputeAutoInheritByObjectTypeEx(*(uint64_t *)(v_rip - 0x8B982E + arg1 * 8 + 0xFC7800), *(uint64_t *)(v_stack_m1D8 + 0x40), Arg3, v_stack_p64);
    if (sign_flag) goto loc_008BA084;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p64)) | ((uint32_t)(local_r13)));
    v_stack_p64 = (uint32_t)(Arg1);
    if ((*(uint64_t *)(v_rip - 0x8B982E + arg1 * 8 + 0xFC7800)) == (*(uint64_t *)(v_rip + 0x655BCA))) goto loc_008B9F66;
    Arg4 = 0;
loc_008B9A93:
    v_stack_p50 = v_stack_m220;
    v_stack_p40 = *(uint64_t *)(v_rip - 0x8B982E + arg1 * 8 + 0xFC7800) + 76;
    v_stack_p38 = v_stack_m1D8 + 32;
    v_stack_p30 = v_stack_m238;
    v_stack_p28 = (uint32_t)(Arg1);
    Arg1 = 0;
    v_stack_p20 = 0;
    Arg4 = 0;
    result = SeAssignSecurityEx2(Arg1, *(uint64_t *)(v_stack_m1D8 + 0x40), v_stack_p78, Arg4);
    if (sign_flag) goto loc_008B9D3F;
    Arg3 = 0;
    v_stack_p40 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_p38 = *(uint64_t *)(v_rip - 0x8B982E + arg1 * 8 + 0xFC7800) + 76;
    v_stack_p30 = 1;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x8B982E + arg1 * 8 + 0xFC7800) + 0x98)) != (v_rip + 1956)) goto loc_008B9F76;
    result = 0;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = SeDefaultObjectMethod(v_stack_m220, Arg3 + 3, Arg3, v_stack_p78);
loc_008B9B3A:
    if (!sign_flag) goto loc_008B9B63;
    if (v_stack_p78 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_p78, Arg2, Arg3, v_stack_p78);
    }
    Arg3 = 0;
    v_stack_p78 = 0;
    if (sign_flag) goto loc_008B9D3F;
loc_008B9B63:
    if ((*(uint8_t *)(*(uint64_t *)(arg1 - 0x10) + 0x10)) > 1) goto loc_008B9B79;
    if (*(uint64_t *)(*(uint64_t *)(arg1 - 0x10) + 0x20) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(arg1 - 0x10) + 0x20), Arg2, Arg3, v_stack_p78);
    }
    local_r15 = 0;
    *(uint64_t *)(*(uint64_t *)(arg1 - 0x10) + 0x20) = 0;
    *(uint64_t *)(v_stack_m1D8 + 0x40) = 0;
loc_008B9B8F:
    result = 0;
    *(uint64_t *)(arg1 - 0x30 + 0x20) = 0;
    if (v_stack_m218 == 0) goto loc_008B9D6E;
    local_rsi = 0;
    v_stack_p50 = v_stack_m218;
    *(uint64_t *)(v_stack_m218) = 0;
    result = *(uint64_t *)(arg1 - 0x10);
    if (local_r12 == 0) { result = 0; }
    v_stack_p48 = v_stack_m210;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p70)) + 1);
    v_stack_p40 = 0;
    v_stack_p38 = result;
    Arg3 = 0;
    v_stack_p30 = (uint8_t)(v_stack_p60);
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 - 0x10))));
    v_stack_p20 = (uint32_t)(Arg1);
    Arg1 = 0;
    result = ObpCreateHandle(Arg1, v_stack_m220, Arg3, v_stack_m1D8);
    result = ObfDereferenceObject(v_stack_m220, v_stack_m220, Arg3, v_stack_m1D8);
loc_008B9BF8:
    if (*(uint64_t *)(*(uint64_t *)(arg1 - 0x10) + 0x20) == 0) goto loc_008B9C12;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 - 0x10) + 0x10)) <= 1) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(arg1 - 0x10) + 0x20), Arg2, Arg3, v_stack_m1D8);
    }
    *(uint64_t *)(*(uint64_t *)(arg1 - 0x10) + 0x20) = 0;
loc_008B9C12:
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840))) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840) + 0x10)))) goto loc_008B9F09;
loc_008B9C32:
    result = ExpInterlockedPushEntrySList(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x840), *(uint64_t *)(arg1 - 0x10), Arg3, v_stack_m1D8);
loc_008B9C3A:
    if (v_stack_m1D8 != v_stack_m1D8) goto loc_008B9CD0;
    result = SepDeleteAccessState(v_stack_m1D8, *(uint64_t *)(arg1 - 0x10), Arg3, v_stack_m1D8);
    if ((*(uint32_t *)(v_rip + 0x71E3BA)) != 0) goto loc_008B9F8F;
loc_008B9C5C:
loc_008B9C7E:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x248)) ^ (*(uint64_t *)(v_stack_m1D8 + 0x30));
    if (Arg1 >= 15) goto loc_008B9F54;
    if (Arg1 != 15) goto loc_008B9C7E;
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x248);
    if ((*(uint32_t *)(v_rip + 0x70B36C)) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(v_stack_m1D8 + 0x30) - 48;
        Arg4 = 0x75536553ULL;
        Arg3 = Arg2 + 1;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint64_t *)(v_stack_m1D8 + 0x30) = 0;
    if (*(uint64_t *)(v_stack_m1D8 + 0x20) != 0) goto loc_008B9E77;
loc_008B9CCC:
    *(uint64_t *)(v_stack_m1D8 + 0x20) = 0;
loc_008B9CD0:
    goto loc_008B993C;
loc_008B9CD8:
    v_stack_m1E8 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = PspLockThreadSecurityShared(*(uint64_t *)(v_stack_m1D8 + 0x20), *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m228 + 0x5A0)))) & (8)) == 0) goto loc_008B9F47;
    result = (*(uint64_t *)(v_stack_m228 + 0x538)) & (-8);
    v_stack_p68 = result;
    result = ObfReferenceObjectWithTag(result, (uint32_t)(0x75536553ULL), Arg3, Arg4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m228 + 0x538))) & (3));
    v_stack_m200 = (uint32_t)(result);
loc_008B9D2C:
    result = PspUnlockThreadSecurityShared(v_stack_m228, v_stack_m1E8, Arg3, Arg4);
    goto loc_008B99AE;
loc_008B9D3F:
    result = ObfDereferenceObject(v_stack_m220, v_stack_m1E8, Arg3, Arg4);
    if (v_stack_m1D8 != v_stack_m1D8) goto loc_008B9CD0;
    result = SeDeleteAccessState(v_stack_m1D8, v_stack_m1E8, Arg3, Arg4);
    goto loc_008B9CD0;
loc_008B9D5D:
    result = ObfDereferenceObject(v_stack_m220, v_stack_m1E8, Arg3, Arg4);
    goto loc_008B993C;
loc_008B9D6E:
    if (v_stack_m1D8 != v_stack_m1D8) goto loc_008B9E86;
loc_008B9D7B:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 - 48 + 16, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 - 48 + 16;
        Arg2 = result;
        Arg1 = Arg1 - 48 + 16;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg3 = 0;
    result = ObpChargeQuotaForObject(Arg1 - 48, *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3, Arg4);
    Arg1 = (*(uint64_t *)(arg1 - 0x30 + 0x10)) & (-16);
    Arg2 = *(uint64_t *)(arg1 - 0x30 + 0x10) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(arg1 - 0x30 + 0x10))) & (2)) != 0) goto loc_008B9EFB;
    if ((((uint8_t)(*(uint64_t *)(arg1 - 0x30 + 0x10))) & (2)) != 0) goto loc_008B9EFB;
loc_008B9E14:
    result = KeAbPostRelease(Arg1 - 48 + 16, Arg2, 0, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, 0, Arg4);
    if (sign_flag) {
        Arg1 = v_stack_m220;
        result = ObfDereferenceObject(Arg1, Arg2, 0, Arg4);
    }
    local_rsi = 0;
    goto loc_008B9BF8;
loc_008B9E3F:
    result = RtlValidSecurityDescriptor(result, Arg2, 0, Arg4);
    if ((uint8_t)(result) == 0) goto loc_008BA061;
    if (((*(uint8_t *)(v_stack_m230 + 0x2)) & (16)) == 0) goto loc_008B9A14;
    if (((*(uint32_t *)(v_stack_m1D8 + 0x14)) & (0x1000000ULL)) != 0) goto loc_008B9A14;
    result = SeObjectCreateSaclAccessBits(v_stack_m230, Arg2, 0, Arg4);
    goto loc_008B9A14;
loc_008B9E77:
    result = ObfDereferenceObjectWithTag(v_stack_m230, (uint32_t)(0x75536553ULL), 0, Arg4);
    goto loc_008B9CCC;
loc_008B9E86:
    Arg2 = (uint8_t)((uint32_t)((uint32_t)(result)));
    if (((*(uint32_t *)(*(uint64_t *)(arg1 - 0x10))) & (0x400ULL)) != 0) { Arg2 = (uint32_t)(v_stack_m230); }
    result = ObpAdjustCreatorAccessState(v_stack_m1D8, Arg2, 0, v_stack_m220);
    if (sign_flag) goto loc_008B9E30;
    goto loc_008B9D7B;
loc_008B9EAD:
    if ((*(uint16_t *)(*(uint64_t *)(Arg2 + 0x848))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(Arg2 + 0x848) + 0x10)))) goto loc_008B992A;
    if ((*(uint64_t *)(*(uint64_t *)(Arg2 + 0x848) + 0x38)) != (v_rip + 2918783)) goto loc_008BA054;
    result = ExFreePool(*(uint64_t *)(arg1 - 0x10), *(uint64_t *)(*(uint64_t *)(Arg2 + 0x848) + 0x38), 0, v_stack_m220);
    goto loc_008B9932;
loc_008B9EEB:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 - 0x10) + 0x20)) != 0) goto loc_008B9A2C;
    goto loc_008B9B8F;
loc_008B9EFB:
    result = ExfReleasePushLock(Arg1 - 48 + 16, *(uint64_t *)(*(uint64_t *)(Arg2 + 0x848) + 0x38), 0, v_stack_m220);
    goto loc_008B9E14;
loc_008B9F09:
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x848) + 0x38) + 0x848))) < ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x848) + 0x38) + 0x848) + 0x10)))) goto loc_008B9C32;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x848) + 0x38) + 0x848) + 0x38)) != (v_rip + 2918691)) goto loc_008BA08D;
    result = ExFreePool(*(uint64_t *)(arg1 - 0x10), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg2 + 0x848) + 0x38) + 0x848) + 0x38), 0, v_stack_m220);
    goto loc_008B9C3A;
loc_008B9F47:
    Arg3 = 0;
    v_stack_p68 = 0;
    goto loc_008B9D2C;
loc_008B9F54:
    result = ObfDereferenceObjectWithTag(0, (uint32_t)(0x75536553ULL), Arg3, v_stack_m220);
    goto loc_008B9CBB;
loc_008B9F66:
    goto loc_008B9A93;
loc_008B9F6E:
    goto loc_008B98FD;
loc_008B9F76:
    result = 0;
    v_stack_p28 = 0;
    v_stack_p20 = 0;
    result = guard_dispatch_icall(0, (uint32_t)(0x75536553ULL), Arg3, 1);
    goto loc_008B9B3A;
loc_008B9F8F:
    if (*(uint64_t *)(0 + 0x30) == 0) goto loc_008B9FB4;
    if ((*(uint64_t *)(0 + 0x30)) == (*(uint64_t *)(v_rip + 0x5ADBE3))) {
    }
    if (*(uint64_t *)(0 + 0x20) == 0) goto loc_008B9C5C;
    if ((*(uint64_t *)(0 + 0x20)) != (*(uint64_t *)(v_rip + 0x5ADBBA))) goto loc_008B9C5C;
    goto loc_008B9C5C;
loc_008B9FE6:
    if (*(uint64_t *)(v_rip + 0x5ADBBA) == 0) goto loc_008BA035;
    if ((*(uint64_t *)(v_rip + 0x5ADBBA)) == (*(uint64_t *)(v_rip + 0x5ADB90))) {
    }
loc_008BA007:
    if (v_stack_m208 == 0) goto loc_008B99D1;
    if (v_stack_m208 != (*(uint64_t *)(v_rip + 0x5ADB6B))) goto loc_008B99D1;
    goto loc_008B99D1;
loc_008BA035:
    goto loc_008BA007;
loc_008BA03C:
    result = SeReleaseSecurityDescriptor(*(uint64_t *)(*(uint64_t *)(v_rip + 0x5ADBBA) + 0x478), *(uint8_t *)(*(uint64_t *)(arg1 - 0x10) + 0x10), 1, 1);
    Arg3 = 0;
    *(uint64_t *)(*(uint64_t *)(arg1 - 0x10) + 0x20) = 0;
    goto loc_008B990A;
loc_008BA054:
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(v_rip + 0x5ADBBA) + 0x478), *(uint8_t *)(*(uint64_t *)(arg1 - 0x10) + 0x10), Arg3, 1);
    goto loc_008B9932;
loc_008BA061:
    result = ObfDereferenceObject(v_stack_m220, *(uint8_t *)(*(uint64_t *)(arg1 - 0x10) + 0x10), Arg3, 1);
    result = SeDeleteAccessState(0, *(uint8_t *)(*(uint64_t *)(arg1 - 0x10) + 0x10), Arg3, 1);
loc_008BA084:
    goto loc_008B9D3F;
loc_008BA08D:
    result = guard_dispatch_icall(0, *(uint8_t *)(*(uint64_t *)(arg1 - 0x10) + 0x10), Arg3, 1);
    goto loc_008B9C3A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x30` | `64` | `R` |
| `Arg1` | `- 0x10` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `8` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R/W` |
| `Arg1` | `+ 0x18` | `8` | `R` |
| `Arg1` | `+ 0x1A` | `8` | `R` |
| `Arg1` | `+ 0x20` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008B97A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
