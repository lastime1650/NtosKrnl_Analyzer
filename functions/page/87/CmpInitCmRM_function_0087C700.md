# CmpInitCmRM

- RVA: `0x0087C700`–`0x0087D274` (길이 `2,932` bytes)
- VA: `0x000000014087C700`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006CF84`
- 디코드: `688`개 명령, `2,932/2,932` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **70**; 고유 호출 대상: **42**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **23**

### Outgoing calls
- `0x0087C7FE` → [ExUuidCreate](../91/ExUuidCreate_function_00917500.md) (function, `0x00917500`)
- `0x0087C819` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x0087C83A` → [CmpLogTxrInitEvent](CmpLogTxrInitEvent_function_0087D27C.md) (function, `0x0087D27C`)
- `0x0087C84A` → [ExUuidCreate](../91/ExUuidCreate_function_00917500.md) (function, `0x00917500`)
- `0x0087C865` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x0087C880` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0087C8AC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0087C8C2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0087C90D` → [ExInitializeResourceLite](../../text/41/ExInitializeResourceLite_function_0041F9A0.md) (function, `0x0041F9A0`)
- `0x0087C9FF` → [RtlStringFromGUIDEx](../91/RtlStringFromGUIDEx_function_00915450.md) (function, `0x00915450`)
- `0x0087CA26` → [Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline_function_004F79EC.md) (function, `0x004F79EC`)
- `0x0087CA72` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0087CA90` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x0087CA9D` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x0087CAAB` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x0087CABC` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (function, `0x0040FA50`)
- `0x0087CAC9` → [CmpQueryFileSecurityDescriptor](CmpQueryFileSecurityDescriptor_function_0087B318.md) (function, `0x0087B318`)
- `0x0087CB1B` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsCreateLogFile` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsCreateLogFile`)
- `0x0087CB29` → [Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline_function_004F79EC.md) (function, `0x004F79EC`)
- `0x0087CB79` → [CmpDeleteCorruptedLogfile](../7F/CmpDeleteCorruptedLogfile_function_007F6C80.md) (function, `0x007F6C80`)
- `0x0087CB95` → [CmpQueryNameString](../9B/CmpQueryNameString_function_009BA2AC.md) (function, `0x009BA2AC`)
- `0x0087CBA8` → [Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline_function_004F79EC.md) (function, `0x004F79EC`)
- `0x0087CBBE` → [CmpIsFileInSystemConfig](../7F/CmpIsFileInSystemConfig_function_007F1F80.md) (function, `0x007F1F80`)
- `0x0087CC15` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x0087CC38` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x0087CC43` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0087CC5E` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x0087CC71` → [CmpLogTxrInitEvent](CmpLogTxrInitEvent_function_0087D27C.md) (function, `0x0087D27C`)
- `0x0087CCA0` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsMgmtRegisterManagedClient` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsMgmtRegisterManagedClient`)
- `0x0087CCCC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0087CD12` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0087CD2A` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsMgmtInstallPolicy` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsMgmtInstallPolicy`)
- `0x0087CD3D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0087CDB5` → [ZwCreateTransactionManager](../../text/6A/ZwCreateTransactionManager_function_006AEAD0.md) (function, `0x006AEAD0`)
- `0x0087CDD2` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x0087CDE0` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsCloseLogFileObject` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsCloseLogFileObject`)
- `0x0087CDF9` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsMgmtDeregisterManagedClient` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsMgmtDeregisterManagedClient`)
- `0x0087CE57` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x0087CE5F` → [HvLockHiveFlusherShared](../84/HvLockHiveFlusherShared_function_0084F95C.md) (function, `0x0084F95C`)
- `0x0087CE67` → [HvLockHiveWriter](../85/HvLockHiveWriter_function_00859894.md) (function, `0x00859894`)
- `0x0087CE6F` → [HvMarkBaseBlockDirty](HvMarkBaseBlockDirty_function_0087BD04.md) (function, `0x0087BD04`)
- `0x0087CE77` → [HvUnlockHiveWriter](../85/HvUnlockHiveWriter_function_008598E4.md) (function, `0x008598E4`)
- `0x0087CE7F` → [HvUnlockHiveFlusherShared](../84/HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x0087CE84` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x0087CEB4` → [ZwRecoverTransactionManager](../../text/6B/ZwRecoverTransactionManager_function_006B0030.md) (function, `0x006B0030`)
- `0x0087CEC0` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x0087CEE1` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsCloseLogFileObject` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsCloseLogFileObject`)
- `0x0087CEFA` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsMgmtDeregisterManagedClient` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsMgmtDeregisterManagedClient`)
- `0x0087CF2F` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x0087CFA4` → [ZwCreateResourceManager](../../text/6A/ZwCreateResourceManager_function_006AE970.md) (function, `0x006AE970`)
- `0x0087CFCB` → [ZwOpenResourceManager](../../text/6A/ZwOpenResourceManager_function_006AF790.md) (function, `0x006AF790`)
- `0x0087CFE8` → [ZwRecoverResourceManager](../../text/6B/ZwRecoverResourceManager_function_006B0010.md) (function, `0x006B0010`)
- `0x0087D029` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x0087D0D4` → [LOCK_CM_RM_LIST](../9B/LOCK_CM_RM_LIST_function_009B1490.md) (function, `0x009B1490`)
- `0x0087D10B` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x0087D110` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x0087D121` → [CmpStartRMLog](../7F/CmpStartRMLog_function_007F0AFC.md) (function, `0x007F0AFC`)
- `0x0087D132` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0087D1BD` → [CmpLogTxrInitEvent](CmpLogTxrInitEvent_function_0087D27C.md) (function, `0x0087D27C`)
- `0x0087D1CB` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsMgmtDeregisterManagedClient` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsMgmtDeregisterManagedClient`)
- `0x0087D1E4` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsCloseLogFileObject` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsCloseLogFileObject`)
- `0x0087D1FA` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x0087D209` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x0087D219` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x0087D227` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0087D235` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0087D243` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0087D250` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0087D259` → [ExDeleteResourceLite](../../text/38/ExDeleteResourceLite_function_0038BA60.md) (function, `0x0038BA60`)
- `0x0087D264` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [CmpLoadKeyCommon](../../text/46/CmpLoadKeyCommon_function_0046E9F8.md) at `0x0046ED69`
- [CmpFinishSystemHivesLoad](../7D/CmpFinishSystemHivesLoad_function_007DA210.md) at `0x007DA3D2`
- [CmpFinishSystemHivesLoad](../7D/CmpFinishSystemHivesLoad_function_007DA210.md) at `0x007DAA98`
- [CmpMountPreloadedHives](../7D/CmpMountPreloadedHives_function_007DBE18.md) at `0x007DC44D`

### Static image references
- `0x0087C728` → RVA `0x00E0A740` (`.data`; read)
- `0x0087C74D` → RVA `0x00FD8006` (`PAGEDATA`; read)
- `0x0087C7D7` → RVA `0x00E09AE0` (`.data`; read)
- `0x0087CA17` → RVA `0x000013C8` (`.rdata`; read)
- `0x0087CA58` → RVA `0x00E0A040` (`.data`; read)
- `0x0087CA5F` → RVA `0x00E0A030` (`.data`; read)
- `0x0087CB1B` → RVA `0x00151268` (`ext-ms-win-fs-clfs-l1-1-0.dll!ClfsCreateLogFile (IAT)`; read)
- `0x0087CB4C` → RVA `0x00B09B20` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0087CB5F` → RVA `0x00E0A020` (`.data`; read)
- `0x0087CCA0` → RVA `0x00151260` (`ext-ms-win-fs-clfs-l1-1-0.dll!ClfsMgmtRegisterManagedClient (IAT)`; read)
- `0x0087CD0B` → RVA `0x00E0A028` (`.data`; read)
- `0x0087CD2A` → RVA `0x00151258` (`ext-ms-win-fs-clfs-l1-1-0.dll!ClfsMgmtInstallPolicy (IAT)`; read)
- `0x0087CDE0` → RVA `0x00151250` (`ext-ms-win-fs-clfs-l1-1-0.dll!ClfsCloseLogFileObject (IAT)`; read)
- `0x0087CDF9` → RVA `0x00151248` (`ext-ms-win-fs-clfs-l1-1-0.dll!ClfsMgmtDeregisterManagedClient (IAT)`; read)
- `0x0087CF0A` → RVA `0x00FC7330` (`ALMOSTRO`; read)
- `0x0087D009` → RVA `0x00FC7338` (`ALMOSTRO`; read)
- `0x0087D050` → RVA `0x00EEFC78` (`.data`; write)
- `0x0087D057` → RVA `0x00E098B8` (`.data`; read)
- `0x0087D0AD` → RVA `0x00FD9A90` (`PAGEDATA`; read)
- `0x0087D0D9` → RVA `0x00EF56B8` (`.data`; read)
- `0x0087D0E0` → RVA `0x00EF56B0` (`.data`; read)
- `0x0087D0F6` → RVA `0x00EF5660` (`.data`; read)
- `0x0087D104` → RVA `0x00EF56B8` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **36**
  - `0x0087C819` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (`PAGE` → `.text`)
  - `0x0087C865` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (`PAGE` → `.text`)
  - `0x0087C880` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0087C8AC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0087C8C2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0087C90D` → [ExInitializeResourceLite](../../text/41/ExInitializeResourceLite_function_0041F9A0.md) (`PAGE` → `.text`)
  - `0x0087CA26` → [Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline_function_004F79EC.md) (`PAGE` → `.text`)
  - `0x0087CA72` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0087CA90` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (`PAGE` → `.text`)
  - `0x0087CA9D` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (`PAGE` → `.text`)
  - `0x0087CAAB` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (`PAGE` → `.text`)
  - `0x0087CABC` → [RtlAppendUnicodeStringToString](../../text/40/RtlAppendUnicodeStringToString_function_0040FA50.md) (`PAGE` → `.text`)
  - `0x0087CB29` → [Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline_function_004F79EC.md) (`PAGE` → `.text`)
  - `0x0087CBA8` → [Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline_function_004F79EC.md) (`PAGE` → `.text`)
  - `0x0087CC15` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x0087CC43` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0087CC5E` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x0087CCCC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0087CD12` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0087CD3D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0087CDB5` → [ZwCreateTransactionManager](../../text/6A/ZwCreateTransactionManager_function_006AEAD0.md) (`PAGE` → `.text`)
  - `0x0087CE57` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x0087CE84` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x0087CEB4` → [ZwRecoverTransactionManager](../../text/6B/ZwRecoverTransactionManager_function_006B0030.md) (`PAGE` → `.text`)
  - `0x0087CFA4` → [ZwCreateResourceManager](../../text/6A/ZwCreateResourceManager_function_006AE970.md) (`PAGE` → `.text`)
  - `0x0087CFCB` → [ZwOpenResourceManager](../../text/6A/ZwOpenResourceManager_function_006AF790.md) (`PAGE` → `.text`)
  - `0x0087CFE8` → [ZwRecoverResourceManager](../../text/6B/ZwRecoverResourceManager_function_006B0010.md) (`PAGE` → `.text`)
  - `0x0087D10B` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`PAGE` → `.text`)
  - `0x0087D110` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x0087D132` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0087D227` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x0087D235` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0087D243` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x0087D250` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0087D259` → [ExDeleteResourceLite](../../text/38/ExDeleteResourceLite_function_0038BA60.md) (`PAGE` → `.text`)
  - `0x0087D264` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0087C700  48 8B C4                        mov rax, rsp
0087C703  48 89 58 18                     mov qword ptr [rax + 0x18], rbx
0087C707  55                              push rbp
0087C708  56                              push rsi
0087C709  57                              push rdi
0087C70A  41 54                           push r12
0087C70C  41 55                           push r13
0087C70E  41 56                           push r14
0087C710  41 57                           push r15
0087C712  48 8D A8 08 FF FF FF            lea rbp, [rax - 0xf8]
0087C719  48 81 EC C0 01 00 00            sub rsp, 0x1c0
0087C720  0F 29 70 B8                     movaps xmmword ptr [rax - 0x48], xmm6
0087C724  0F 29 78 A8                     movaps xmmword ptr [rax - 0x58], xmm7
0087C728  48 8B 05 11 E0 58 00            mov rax, qword ptr [rip + 0x58e011]
0087C72F  48 33 C4                        xor rax, rsp
0087C732  48 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], rax
0087C739  45 33 F6                        xor r14d, r14d
0087C73C  88 54 24 60                     mov byte ptr [rsp + 0x60], dl
0087C740  0F 57 C0                        xorps xmm0, xmm0
0087C743  48 89 4D D8                     mov qword ptr [rbp - 0x28], rcx
0087C747  33 C0                           xor eax, eax
0087C749  4C 89 75 A0                     mov qword ptr [rbp - 0x60], r14
0087C74D  44 38 35 B2 B8 75 00            cmp byte ptr [rip + 0x75b8b2], r14b
0087C754  0F 57 C9                        xorps xmm1, xmm1
0087C757  41 BC 00 02 00 00               mov r12d, 0x200
0087C75D  4C 89 75 A8                     mov qword ptr [rbp - 0x58], r14
0087C761  4C 8B E9                        mov r13, rcx
0087C764  48 89 45 00                     mov qword ptr [rbp], rax
0087C768  0F 11 85 80 00 00 00            movups xmmword ptr [rbp + 0x80], xmm0
0087C76F  89 45 08                        mov dword ptr [rbp + 8], eax
0087C772  45 8A FE                        mov r15b, r14b
0087C775  0F 11 4D 50                     movups xmmword ptr [rbp + 0x50], xmm1
0087C779  4C 89 75 B8                     mov qword ptr [rbp - 0x48], r14
0087C77D  0F 11 45 60                     movups xmmword ptr [rbp + 0x60], xmm0
0087C781  4C 89 75 C0                     mov qword ptr [rbp - 0x40], r14
0087C785  0F 11 4D 70                     movups xmmword ptr [rbp + 0x70], xmm1
0087C789  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
0087C78E  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0087C792  4C 89 75 80                     mov qword ptr [rbp - 0x80], r14
0087C796  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0087C79A  4C 89 75 90                     mov qword ptr [rbp - 0x70], r14
0087C79E  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
0087C7A2  4C 89 75 D0                     mov qword ptr [rbp - 0x30], r14
0087C7A6  44 89 74 24 70                  mov dword ptr [rsp + 0x70], r14d
0087C7AB  4C 89 75 88                     mov qword ptr [rbp - 0x78], r14
0087C7AF  4C 89 75 98                     mov qword ptr [rbp - 0x68], r14
0087C7B3  0F 11 45 18                     movups xmmword ptr [rbp + 0x18], xmm0
0087C7B7  89 45 48                        mov dword ptr [rbp + 0x48], eax
0087C7BA  0F 11 45 28                     movups xmmword ptr [rbp + 0x28], xmm0
0087C7BE  44 89 74 24 64                  mov dword ptr [rsp + 0x64], r14d
0087C7C3  0F 11 45 38                     movups xmmword ptr [rbp + 0x38], xmm0
0087C7C7  44 89 64 24 6C                  mov dword ptr [rsp + 0x6c], r12d
0087C7CC  44 88 74 24 68                  mov byte ptr [rsp + 0x68], r14b
0087C7D1  0F 85 4F 09 00 00               jne 0x14087d126
0087C7D7  48 8B 1D 02 D3 58 00            mov rbx, qword ptr [rip + 0x58d302]
0087C7DE  48 85 C9                        test rcx, rcx
0087C7E1  48 0F 45 D9                     cmovne rbx, rcx
0087C7E5  F7 83 A0 00 00 00 01 80 00 00   test dword ptr [rbx + 0xa0], 0x8001
0087C7EF  0F 85 31 09 00 00               jne 0x14087d126
0087C7F5  BE 2D 02 00 C0                  mov esi, 0xc000022d
0087C7FA  48 8D 4D 60                     lea rcx, [rbp + 0x60]
0087C7FE  E8 FD AC 09 00                  call 0x140917500
0087C803  8B F8                           mov edi, eax
0087C805  3B C6                           cmp eax, esi
0087C807  75 17                           jne 0x14087c820
0087C809  4C 8D 45 B0                     lea r8, [rbp - 0x50]
0087C80D  48 C7 45 B0 80 69 67 FF         mov qword ptr [rbp - 0x50], 0xffffffffff676980
0087C815  33 D2                           xor edx, edx
0087C817  33 C9                           xor ecx, ecx
0087C819  E8 32 CD 98 FF                  call 0x140209550
0087C81E  EB DA                           jmp 0x14087c7fa
0087C820  85 FF                           test edi, edi
0087C822  79 22                           jns 0x14087c846
0087C824  C7 83 40 10 00 00 01 00 00 00   mov dword ptr [rbx + 0x1040], 1
0087C82E  44 8B C7                        mov r8d, edi
0087C831  89 BB 44 10 00 00               mov dword ptr [rbx + 0x1044], edi
0087C837  48 8B D3                        mov rdx, rbx
0087C83A  E8 3D 0A 00 00                  call 0x14087d27c
0087C83F  8B C7                           mov eax, edi
0087C841  E9 E2 08 00 00                  jmp 0x14087d128
0087C846  48 8D 4D 70                     lea rcx, [rbp + 0x70]
0087C84A  E8 B1 AC 09 00                  call 0x140917500
0087C84F  8B F8                           mov edi, eax
0087C851  3B C6                           cmp eax, esi
0087C853  75 17                           jne 0x14087c86c
0087C855  4C 8D 45 B0                     lea r8, [rbp - 0x50]
0087C859  48 C7 45 B0 80 69 67 FF         mov qword ptr [rbp - 0x50], 0xffffffffff676980
0087C861  33 D2                           xor edx, edx
0087C863  33 C9                           xor ecx, ecx
0087C865  E8 E6 CC 98 FF                  call 0x140209550
0087C86A  EB DA                           jmp 0x14087c846
0087C86C  85 FF                           test edi, edi
0087C86E  78 B4                           js 0x14087c824
0087C870  BA 88 00 00 00                  mov edx, 0x88
0087C875  BF 43 4D 52 6D                  mov edi, 0x6d524d43
0087C87A  44 8B C7                        mov r8d, edi
0087C87D  8D 4A 78                        lea ecx, [rdx + 0x78]
0087C880  E8 6B 58 30 00                  call 0x140b820f0
0087C885  48 8B F0                        mov rsi, rax
0087C888  48 85 C0                        test rax, rax
0087C88B  75 11                           jne 0x14087c89e
0087C88D  C7 83 40 10 00 00 01 00 00 00   mov dword ptr [rbx + 0x1040], 1
0087C897  BF 9A 00 00 C0                  mov edi, 0xc000009a
0087C89C  EB 90                           jmp 0x14087c82e
0087C89E  BA 68 00 00 00                  mov edx, 0x68
0087C8A3  41 B8 43 4D 72 6C               mov r8d, 0x6c724d43
0087C8A9  8D 4A D8                        lea ecx, [rdx - 0x28]
0087C8AC  E8 3F 58 30 00                  call 0x140b820f0
0087C8B1  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
0087C8B5  48 8B D0                        mov rdx, rax
0087C8B8  48 85 C0                        test rax, rax
0087C8BB  75 16                           jne 0x14087c8d3
0087C8BD  8B D7                           mov edx, edi
0087C8BF  48 8B CE                        mov rcx, rsi
0087C8C2  E8 A9 5F 30 00                  call 0x140b82870
0087C8C7  C7 83 40 10 00 00 02 00 00 00   mov dword ptr [rbx + 0x1040], 2
0087C8D1  EB C4                           jmp 0x14087c897
0087C8D3  8B 7C 24 60                     mov edi, dword ptr [rsp + 0x60]
0087C8D7  48 8D 46 10                     lea rax, [rsi + 0x10]
0087C8DB  48 89 40 08                     mov qword ptr [rax + 8], rax
0087C8DF  48 89 00                        mov qword ptr [rax], rax
0087C8E2  40 8A C7                        mov al, dil
0087C8E5  F6 D8                           neg al
0087C8E7  4C 89 76 58                     mov qword ptr [rsi + 0x58], r14
0087C8EB  4C 89 76 60                     mov qword ptr [rsi + 0x60], r14
0087C8EF  1B C9                           sbb ecx, ecx
0087C8F1  83 E1 04                        and ecx, 4
0087C8F4  89 4E 68                        mov dword ptr [rsi + 0x68], ecx
0087C8F7  48 8B CA                        mov rcx, rdx
0087C8FA  4C 89 76 6C                     mov qword ptr [rsi + 0x6c], r14
0087C8FE  44 89 76 44                     mov dword ptr [rsi + 0x44], r14d
0087C902  4C 89 76 48                     mov qword ptr [rsi + 0x48], r14
0087C906  48 89 96 80 00 00 00            mov qword ptr [rsi + 0x80], rdx
0087C90D  E8 8E 30 BA FF                  call 0x14041f9a0
0087C912  4C 8B 43 40                     mov r8, qword ptr [rbx + 0x40]
0087C916  B8 72 6D 74 6D                  mov eax, 0x6d746d72
0087C91B  0F 10 75 60                     movups xmm6, xmmword ptr [rbp + 0x60]
0087C91F  41 BE 01 00 00 00               mov r14d, 1
0087C925  0F 10 7D 70                     movups xmm7, xmmword ptr [rbp + 0x70]
0087C929  41 39 80 A4 00 00 00            cmp dword ptr [r8 + 0xa4], eax
0087C930  74 0F                           je 0x14087c941
0087C932  41 89 80 A4 00 00 00            mov dword ptr [r8 + 0xa4], eax
0087C939  45 33 FF                        xor r15d, r15d
0087C93C  E9 DC 04 00 00                  jmp 0x14087ce1d
0087C941  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
0087C948  4C 8B 8D 88 00 00 00            mov r9, qword ptr [rbp + 0x88]
0087C94F  48 8B D1                        mov rdx, rcx
0087C952  49 2B 90 94 00 00 00            sub rdx, qword ptr [r8 + 0x94]
0087C959  75 0A                           jne 0x14087c965
0087C95B  49 8B D1                        mov rdx, r9
0087C95E  49 2B 90 9C 00 00 00            sub rdx, qword ptr [r8 + 0x9c]
0087C965  48 85 D2                        test rdx, rdx
0087C968  75 11                           jne 0x14087c97b
0087C96A  44 89 74 24 64                  mov dword ptr [rsp + 0x64], r14d
0087C96F  45 8A FE                        mov r15b, r14b
0087C972  F3 41 0F 7F B8 94 00 00 00      movdqu xmmword ptr [r8 + 0x94], xmm7
0087C97B  4C 8B 43 40                     mov r8, qword ptr [rbx + 0x40]
0087C97F  48 8B D1                        mov rdx, rcx
0087C982  49 2B 50 70                     sub rdx, qword ptr [r8 + 0x70]
0087C986  75 07                           jne 0x14087c98f
0087C988  49 8B D1                        mov rdx, r9
0087C98B  49 2B 50 78                     sub rdx, qword ptr [r8 + 0x78]
0087C98F  48 85 D2                        test rdx, rdx
0087C992  75 09                           jne 0x14087c99d
0087C994  45 8A FE                        mov r15b, r14b
0087C997  F3 41 0F 7F 70 70               movdqu xmmword ptr [r8 + 0x70], xmm6
0087C99D  48 8B 53 40                     mov rdx, qword ptr [rbx + 0x40]
0087C9A1  48 2B 8A 80 00 00 00            sub rcx, qword ptr [rdx + 0x80]
0087C9A8  75 0A                           jne 0x14087c9b4
0087C9AA  49 8B C9                        mov rcx, r9
0087C9AD  48 2B 8A 88 00 00 00            sub rcx, qword ptr [rdx + 0x88]
0087C9B4  48 85 C9                        test rcx, rcx
0087C9B7  75 0F                           jne 0x14087c9c8
0087C9B9  0F 10 42 70                     movups xmm0, xmmword ptr [rdx + 0x70]
0087C9BD  45 8A FE                        mov r15b, r14b
0087C9C0  F3 0F 7F 82 80 00 00 00         movdqu xmmword ptr [rdx + 0x80], xmm0
0087C9C8  83 64 24 70 00                  and dword ptr [rsp + 0x70], 0
0087C9CD  44 89 64 24 6C                  mov dword ptr [rsp + 0x6c], r12d
0087C9D2  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
0087C9D6  45 84 FF                        test r15b, r15b
0087C9D9  0F 85 75 04 00 00               jne 0x14087ce54
0087C9DF  45 33 FF                        xor r15d, r15d
0087C9E2  48 8B 4B 40                     mov rcx, qword ptr [rbx + 0x40]
0087C9E6  48 8D 55 A0                     lea rdx, [rbp - 0x60]
0087C9EA  48 8B 83 08 06 00 00            mov rax, qword ptr [rbx + 0x608]
0087C9F1  48 81 C1 94 00 00 00            add rcx, 0x94
0087C9F8  45 8A C6                        mov r8b, r14b
0087C9FB  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
0087C9FF  E8 4C 8A 09 00                  call 0x140915450
0087CA04  8B F8                           mov edi, eax
0087CA06  85 C0                           test eax, eax
0087CA08  0F 88 9F 07 00 00               js 0x14087d1ad
0087CA0E  4D 85 ED                        test r13, r13
0087CA11  0F 85 73 01 00 00               jne 0x14087cb8a
0087CA17  4C 8D 2D AA 49 78 FF            lea r13, [rip - 0x87b656]
0087CA1E  C7 44 24 70 34 00 00 00         mov dword ptr [rsp + 0x70], 0x34
0087CA26  E8 C1 AF C7 FF                  call 0x1404f79ec
0087CA2B  41 8B CC                        mov ecx, r12d
0087CA2E  0F BA E9 18                     bts ecx, 0x18
0087CA32  85 C0                           test eax, eax
0087CA34  41 0F 44 CC                     cmove ecx, r12d
0087CA38  89 4C 24 6C                     mov dword ptr [rsp + 0x6c], ecx
0087CA3C  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
0087CA40  44 8B 7C 24 60                  mov r15d, dword ptr [rsp + 0x60]
0087CA45  44 8B E0                        mov r12d, eax
0087CA48  B9 00 01 00 00                  mov ecx, 0x100
0087CA4D  41 0F B7 45 00                  movzx eax, word ptr [r13]
0087CA52  41 B8 53 74 72 67               mov r8d, 0x67727453
0087CA58  66 03 05 E1 D5 58 00            add ax, word ptr [rip + 0x58d5e1]
0087CA5F  66 03 05 CA D5 58 00            add ax, word ptr [rip + 0x58d5ca]
0087CA66  66 03 45 A0                     add ax, word ptr [rbp - 0x60]
0087CA6A  0F B7 D0                        movzx edx, ax
0087CA6D  66 89 54 24 7A                  mov word ptr [rsp + 0x7a], dx
0087CA72  E8 79 56 30 00                  call 0x140b820f0
0087CA77  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0087CA7B  48 85 C0                        test rax, rax
0087CA7E  0F 84 09 07 00 00               je 0x14087d18d
0087CA84  48 8D 15 A5 D5 58 00            lea rdx, [rip + 0x58d5a5]
0087CA8B  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
0087CA90  E8 BB 2F B9 FF                  call 0x14040fa50
0087CA95  49 8B D5                        mov rdx, r13
0087CA98  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
0087CA9D  E8 AE 2F B9 FF                  call 0x14040fa50
0087CAA2  48 8D 55 A0                     lea rdx, [rbp - 0x60]
0087CAA6  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
0087CAAB  E8 A0 2F B9 FF                  call 0x14040fa50
0087CAB0  48 8D 15 89 D5 58 00            lea rdx, [rip + 0x58d589]
0087CAB7  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
0087CABC  E8 8F 2F B9 FF                  call 0x14040fa50
0087CAC1  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
0087CAC5  48 8D 55 88                     lea rdx, [rbp - 0x78]
0087CAC9  E8 4A E8 FF FF                  call 0x14087b318
0087CACE  33 C9                           xor ecx, ecx
0087CAD0  8B F8                           mov edi, eax
0087CAD2  85 C0                           test eax, eax
0087CAD4  0F 88 A7 06 00 00               js 0x14087d181
0087CADA  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
0087CADE  44 8D 49 07                     lea r9d, [rcx + 7]
0087CAE2  89 4C 24 50                     mov dword ptr [rsp + 0x50], ecx
0087CAE6  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
0087CAEB  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0087CAF0  41 B8 00 00 00 C0               mov r8d, 0xc0000000
0087CAF6  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0087CAFA  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
0087CAFE  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
0087CB02  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0087CB06  C7 44 24 30 08 00 00 00         mov dword ptr [rsp + 0x30], 8
0087CB0E  C7 44 24 28 03 00 00 00         mov dword ptr [rsp + 0x28], 3
0087CB16  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0087CB1B  48 FF 15 46 47 8D FF            call qword ptr [rip - 0x72b8ba]
0087CB22  0F 1F 44 00 00                  nop dword ptr [rax + rax]
0087CB27  8B F8                           mov edi, eax
0087CB29  E8 BE AE C7 FF                  call 0x1404f79ec
0087CB2E  85 C0                           test eax, eax
0087CB30  0F 84 CE 00 00 00               je 0x14087cc04
0087CB36  44 89 64 24 64                  mov dword ptr [rsp + 0x64], r12d
0087CB3B  44 88 7C 24 60                  mov byte ptr [rsp + 0x60], r15b
0087CB40  81 FF 0D 00 1A C0               cmp edi, 0xc01a000d
0087CB46  0F 85 BD 00 00 00               jne 0x14087cc09
0087CB4C  48 8D 05 CD CF 28 00            lea rax, [rip + 0x28cfcd]
0087CB53  66 C7 44 24 30 46 00            mov word ptr [rsp + 0x30], 0x46
0087CB5A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0087CB5F  4C 8D 0D BA D4 58 00            lea r9, [rip + 0x58d4ba]
0087CB66  4C 8D 05 D3 D4 58 00            lea r8, [rip + 0x58d4d3]
0087CB6D  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
0087CB72  48 8D 55 A0                     lea rdx, [rbp - 0x60]
0087CB76  49 8B CD                        mov rcx, r13
0087CB79  E8 02 A1 F7 FF                  call 0x1407f6c80
0087CB7E  44 89 64 24 64                  mov dword ptr [rsp + 0x64], r12d
0087CB83  44 88 7C 24 60                  mov byte ptr [rsp + 0x60], r15b
0087CB88  EB 7F                           jmp 0x14087cc09
0087CB8A  49 8B 8D 08 06 00 00            mov rcx, qword ptr [r13 + 0x608]
0087CB91  48 8D 55 B8                     lea rdx, [rbp - 0x48]
0087CB95  E8 12 D7 13 00                  call 0x1409ba2ac
0087CB9A  8B F8                           mov edi, eax
0087CB9C  85 C0                           test eax, eax
0087CB9E  0F 88 FD 05 00 00               js 0x14087d1a1
0087CBA4  4C 8D 6D B8                     lea r13, [rbp - 0x48]
0087CBA8  E8 3F AE C7 FF                  call 0x1404f79ec
0087CBAD  85 C0                           test eax, eax
0087CBAF  0F 84 87 FE FF FF               je 0x14087ca3c
0087CBB5  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
0087CBBA  48 8D 4D B8                     lea rcx, [rbp - 0x48]
0087CBBE  E8 BD 53 F7 FF                  call 0x1407f1f80
0087CBC3  8B F8                           mov edi, eax
0087CBC5  85 C0                           test eax, eax
0087CBC7  0F 88 C1 02 00 00               js 0x14087ce8e
0087CBCD  44 38 7C 24 68                  cmp byte ptr [rsp + 0x68], r15b
0087CBD2  44 8B 7C 24 60                  mov r15d, dword ptr [rsp + 0x60]
0087CBD7  8B 7C 24 70                     mov edi, dword ptr [rsp + 0x70]
0087CBDB  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
0087CBDF  44 89 7C 24 60                  mov dword ptr [rsp + 0x60], r15d
0087CBE4  89 7C 24 70                     mov dword ptr [rsp + 0x70], edi
0087CBE8  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
0087CBEC  74 0F                           je 0x14087cbfd
0087CBEE  41 0F BA EC 18                  bts r12d, 0x18
0087CBF3  44 89 64 24 6C                  mov dword ptr [rsp + 0x6c], r12d
0087CBF8  E9 48 FE FF FF                  jmp 0x14087ca45
0087CBFD  41 0F BA F4 18                  btr r12d, 0x18
0087CC02  EB EF                           jmp 0x14087cbf3
0087CC04  44 8B 64 24 64                  mov r12d, dword ptr [rsp + 0x64]
0087CC09  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
0087CC0D  45 33 FF                        xor r15d, r15d
0087CC10  48 85 C9                        test rcx, rcx
0087CC13  74 16                           je 0x14087cc2b
0087CC15  E8 36 5C 30 00                  call 0x140b82850
0087CC1A  0F 57 C0                        xorps xmm0, xmm0
0087CC1D  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
0087CC21  66 0F 73 D8 08                  psrldq xmm0, 8
0087CC26  66 0F D6 45 A8                  movq qword ptr [rbp - 0x58], xmm0
0087CC2B  4C 8B 6D D8                     mov r13, qword ptr [rbp - 0x28]
0087CC2F  4D 85 ED                        test r13, r13
0087CC32  74 09                           je 0x14087cc3d
0087CC34  48 8D 4D B8                     lea rcx, [rbp - 0x48]
0087CC38  E8 C3 3B 14 00                  call 0x1409c0800
0087CC3D  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
0087CC41  33 D2                           xor edx, edx
0087CC43  E8 28 5C 30 00                  call 0x140b82870
0087CC48  85 FF                           test edi, edi
0087CC4A  79 2F                           jns 0x14087cc7b
0087CC4C  45 85 E4                        test r12d, r12d
0087CC4F  0F 85 48 02 00 00               jne 0x14087ce9d
0087CC55  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
0087CC59  48 85 C9                        test rcx, rcx
0087CC5C  74 0D                           je 0x14087cc6b
0087CC5E  E8 ED 5B 30 00                  call 0x140b82850
0087CC63  0F 57 C0                        xorps xmm0, xmm0
0087CC66  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
0087CC6B  44 8B C7                        mov r8d, edi
0087CC6E  48 8B D3                        mov rdx, rbx
0087CC71  E8 06 06 00 00                  call 0x14087d27c
0087CC76  E9 99 01 00 00                  jmp 0x14087ce14
0087CC7B  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0087CC7F  4C 8D 45 98                     lea r8, [rbp - 0x68]
0087CC83  0F 57 C0                        xorps xmm0, xmm0
0087CC86  48 8D 55 18                     lea rdx, [rbp + 0x18]
0087CC8A  33 C0                           xor eax, eax
0087CC8C  0F 11 45 18                     movups xmmword ptr [rbp + 0x18], xmm0
0087CC90  44 89 75 18                     mov dword ptr [rbp + 0x18], r14d
0087CC94  0F 11 45 28                     movups xmmword ptr [rbp + 0x28], xmm0
0087CC98  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
0087CC9C  0F 11 45 38                     movups xmmword ptr [rbp + 0x38], xmm0
0087CCA0  48 FF 15 B9 45 8D FF            call qword ptr [rip - 0x72ba47]
0087CCA7  0F 1F 44 00 00                  nop dword ptr [rax + rax]
0087CCAC  8B F8                           mov edi, eax
0087CCAE  85 C0                           test eax, eax
0087CCB0  0F 88 BF 04 00 00               js 0x14087d175
0087CCB6  0F B7 15 63 D3 58 00            movzx edx, word ptr [rip + 0x58d363]
0087CCBD  B9 00 01 00 00                  mov ecx, 0x100
0087CCC2  48 83 C2 18                     add rdx, 0x18
0087CCC6  41 B8 43 4D 52 6D               mov r8d, 0x6d524d43
0087CCCC  E8 1F 54 30 00                  call 0x140b820f0
0087CCD1  4C 8B F8                        mov r15, rax
0087CCD4  48 85 C0                        test rax, rax
0087CCD7  0F 84 8C 04 00 00               je 0x14087d169
0087CCDD  44 89 30                        mov dword ptr [rax], r14d
0087CCE0  0F B7 0D 39 D3 58 00            movzx ecx, word ptr [rip + 0x58d339]
0087CCE7  83 C1 18                        add ecx, 0x18
0087CCEA  C7 40 0C 09 00 00 00            mov dword ptr [rax + 0xc], 9
0087CCF1  89 48 04                        mov dword ptr [rax + 4], ecx
0087CCF4  0F B7 0D 25 D3 58 00            movzx ecx, word ptr [rip + 0x58d325]
0087CCFB  66 89 48 10                     mov word ptr [rax + 0x10], cx
0087CCFF  48 8D 48 12                     lea rcx, [rax + 0x12]
0087CD03  44 0F B7 05 15 D3 58 00         movzx r8d, word ptr [rip + 0x58d315]
0087CD0B  48 8B 15 16 D3 58 00            mov rdx, qword ptr [rip + 0x58d316]
0087CD12  E8 29 9B E4 FF                  call 0x1406c6840
0087CD17  44 0F B7 05 01 D3 58 00         movzx r8d, word ptr [rip + 0x58d301]
0087CD1F  49 8B D7                        mov rdx, r15
0087CD22  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0087CD26  41 83 C0 18                     add r8d, 0x18
0087CD2A  48 FF 15 27 45 8D FF            call qword ptr [rip - 0x72bad9]
0087CD31  0F 1F 44 00 00                  nop dword ptr [rax + rax]
0087CD36  33 D2                           xor edx, edx
0087CD38  49 8B CF                        mov rcx, r15
0087CD3B  8B F8                           mov edi, eax
0087CD3D  E8 2E 5B 30 00                  call 0x140b82870
0087CD42  45 33 FF                        xor r15d, r15d
0087CD45  85 FF                           test edi, edi
0087CD47  0F 88 10 04 00 00               js 0x14087d15d
0087CD4D  0F B7 0D DC D2 58 00            movzx ecx, word ptr [rip + 0x58d2dc]
0087CD54  4C 8D 66 20                     lea r12, [rsi + 0x20]
0087CD58  0F B7 44 24 78                  movzx eax, word ptr [rsp + 0x78]
0087CD5D  4C 8D 4D C8                     lea r9, [rbp - 0x38]
0087CD61  66 2B C1                        sub ax, cx
0087CD64  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
0087CD69  66 89 45 C8                     mov word ptr [rbp - 0x38], ax
0087CD6D  4C 8D 45 E0                     lea r8, [rbp - 0x20]
0087CD71  0F B7 44 24 7A                  movzx eax, word ptr [rsp + 0x7a]
0087CD76  0F 57 C0                        xorps xmm0, xmm0
0087CD79  66 2B C1                        sub ax, cx
0087CD7C  C7 45 E0 30 00 00 00            mov dword ptr [rbp - 0x20], 0x30
0087CD83  66 89 45 CA                     mov word ptr [rbp - 0x36], ax
0087CD87  BA 3F 00 0F 00                  mov edx, 0xf003f
0087CD8C  8B C1                           mov eax, ecx
0087CD8E  4C 89 7D E8                     mov qword ptr [rbp - 0x18], r15
0087CD92  48 03 45 80                     add rax, qword ptr [rbp - 0x80]
0087CD96  49 8B CC                        mov rcx, r12
0087CD99  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0087CD9D  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
0087CDA1  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0087CDA5  C7 45 F8 40 02 00 00            mov dword ptr [rbp - 8], 0x240
0087CDAC  4C 89 7D F0                     mov qword ptr [rbp - 0x10], r15
0087CDB0  F3 0F 7F 45 00                  movdqu xmmword ptr [rbp], xmm0
0087CDB5  E8 16 1D E3 FF                  call 0x1406aead0
0087CDBA  8B F8                           mov edi, eax
0087CDBC  3D 35 00 00 C0                  cmp eax, 0xc0000035
0087CDC1  0F 85 E5 00 00 00               jne 0x14087ceac
0087CDC7  4C 39 7D 80                     cmp qword ptr [rbp - 0x80], r15
0087CDCB  74 0A                           je 0x14087cdd7
0087CDCD  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
0087CDD2  E8 29 3A 14 00                  call 0x1409c0800
0087CDD7  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0087CDDB  48 85 C9                        test rcx, rcx
0087CDDE  74 10                           je 0x14087cdf0
0087CDE0  48 FF 15 69 44 8D FF            call qword ptr [rip - 0x72bb97]
0087CDE7  0F 1F 44 00 00                  nop dword ptr [rax + rax]
0087CDEC  4C 89 7D 90                     mov qword ptr [rbp - 0x70], r15
0087CDF0  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
0087CDF4  48 85 C9                        test rcx, rcx
0087CDF7  74 10                           je 0x14087ce09
0087CDF9  48 FF 15 48 44 8D FF            call qword ptr [rip - 0x72bbb8]
0087CE00  0F 1F 44 00 00                  nop dword ptr [rax + rax]
0087CE05  4C 89 7D 98                     mov qword ptr [rbp - 0x68], r15
0087CE09  44 39 7C 24 64                  cmp dword ptr [rsp + 0x64], r15d
0087CE0E  0F 85 A7 00 00 00               jne 0x14087cebb
0087CE14  8B 7C 24 60                     mov edi, dword ptr [rsp + 0x60]
0087CE18  44 8B 64 24 6C                  mov r12d, dword ptr [rsp + 0x6c]
0087CE1D  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0087CE21  4D 85 ED                        test r13, r13
0087CE24  40 0F B6 FF                     movzx edi, dil
0087CE28  41 0F 44 FE                     cmove edi, r14d
0087CE2C  44 89 74 24 64                  mov dword ptr [rsp + 0x64], r14d
0087CE31  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
0087CE35  F3 0F 7F B8 94 00 00 00         movdqu xmmword ptr [rax + 0x94], xmm7
0087CE3D  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0087CE41  F3 0F 7F 70 70                  movdqu xmmword ptr [rax + 0x70], xmm6
0087CE46  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0087CE4A  F3 0F 7F B0 80 00 00 00         movdqu xmmword ptr [rax + 0x80], xmm6
0087CE52  EB 03                           jmp 0x14087ce57
0087CE54  45 33 FF                        xor r15d, r15d
0087CE57  E8 D8 CC 34 00                  call 0x140bc9b34
0087CE5C  48 8B CB                        mov rcx, rbx
0087CE5F  E8 F8 2A FD FF                  call 0x14084f95c
0087CE64  48 8B CB                        mov rcx, rbx
0087CE67  E8 28 CA FD FF                  call 0x140859894
0087CE6C  48 8B CB                        mov rcx, rbx
0087CE6F  E8 90 EE FF FF                  call 0x14087bd04
0087CE74  48 8B CB                        mov rcx, rbx
0087CE77  E8 68 CA FD FF                  call 0x1408598e4
0087CE7C  48 8B CB                        mov rcx, rbx
0087CE7F  E8 B4 B8 FC FF                  call 0x140848738
0087CE84  E8 FB CB 34 00                  call 0x140bc9a84
0087CE89  E9 54 FB FF FF                  jmp 0x14087c9e2
0087CE8E  C7 83 40 10 00 00 10 00 00 00   mov dword ptr [rbx + 0x1040], 0x10
0087CE98  E9 1A 03 00 00                  jmp 0x14087d1b7
0087CE9D  C7 83 40 10 00 00 07 00 00 00   mov dword ptr [rbx + 0x1040], 7
0087CEA7  E9 0B 03 00 00                  jmp 0x14087d1b7
0087CEAC  85 C0                           test eax, eax
0087CEAE  78 0B                           js 0x14087cebb
0087CEB0  49 8B 0C 24                     mov rcx, qword ptr [r12]
0087CEB4  E8 77 31 E3 FF                  call 0x1406b0030
0087CEB9  8B F8                           mov edi, eax
0087CEBB  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
0087CEC0  E8 3B 39 14 00                  call 0x1409c0800
0087CEC5  85 FF                           test edi, edi
0087CEC7  79 0F                           jns 0x14087ced8
0087CEC9  C7 83 40 10 00 00 0B 00 00 00   mov dword ptr [rbx + 0x1040], 0xb
0087CED3  E9 DF 02 00 00                  jmp 0x14087d1b7
0087CED8  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0087CEDC  48 85 C9                        test rcx, rcx
0087CEDF  74 10                           je 0x14087cef1
0087CEE1  48 FF 15 68 43 8D FF            call qword ptr [rip - 0x72bc98]
0087CEE8  0F 1F 44 00 00                  nop dword ptr [rax + rax]
0087CEED  4C 89 7D 90                     mov qword ptr [rbp - 0x70], r15
0087CEF1  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
0087CEF5  48 85 C9                        test rcx, rcx
0087CEF8  74 10                           je 0x14087cf0a
0087CEFA  48 FF 15 47 43 8D FF            call qword ptr [rip - 0x72bcb9]
0087CF01  0F 1F 44 00 00                  nop dword ptr [rax + rax]
0087CF06  4C 89 7D 98                     mov qword ptr [rbp - 0x68], r15
0087CF0A  4C 8B 05 1F A4 74 00            mov r8, qword ptr [rip + 0x74a41f]
0087CF11  48 8D 45 88                     lea rax, [rbp - 0x78]
0087CF15  49 8B 0C 24                     mov rcx, qword ptr [r12]
0087CF19  45 33 C9                        xor r9d, r9d
0087CF1C  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
0087CF21  BA 3F 00 0F 00                  mov edx, 0xf003f
0087CF26  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0087CF2B  4C 89 7D 88                     mov qword ptr [rbp - 0x78], r15
0087CF2F  E8 7C BE FE FF                  call 0x140868db0
0087CF34  8B F8                           mov edi, eax
0087CF36  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
0087CF3A  48 89 46 28                     mov qword ptr [rsi + 0x28], rax
0087CF3E  85 FF                           test edi, edi
0087CF40  79 0F                           jns 0x14087cf51
0087CF42  C7 83 40 10 00 00 0C 00 00 00   mov dword ptr [rbx + 0x1040], 0xc
0087CF4C  E9 66 02 00 00                  jmp 0x14087d1b7
0087CF51  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
0087CF55  4C 8D 4D 50                     lea r9, [rbp + 0x50]
0087CF59  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0087CF5F  BA 7F 00 1F 00                  mov edx, 0x1f007f
0087CF64  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
0087CF69  0F 10 40 70                     movups xmm0, xmmword ptr [rax + 0x70]
0087CF6D  4C 89 7D E8                     mov qword ptr [rbp - 0x18], r15
0087CF71  48 8D 45 E0                     lea rax, [rbp - 0x20]
0087CF75  4C 89 7D F0                     mov qword ptr [rbp - 0x10], r15
0087CF79  4C 8D 7E 30                     lea r15, [rsi + 0x30]
0087CF7D  F3 0F 7F 45 50                  movdqu xmmword ptr [rbp + 0x50], xmm0
0087CF82  C7 45 E0 30 00 00 00            mov dword ptr [rbp - 0x20], 0x30
0087CF89  49 8B CF                        mov rcx, r15
0087CF8C  0F 57 C0                        xorps xmm0, xmm0
0087CF8F  C7 45 F8 40 02 00 00            mov dword ptr [rbp - 8], 0x240
0087CF96  F3 0F 7F 45 00                  movdqu xmmword ptr [rbp], xmm0
0087CF9B  4D 8B 04 24                     mov r8, qword ptr [r12]
0087CF9F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0087CFA4  E8 C7 19 E3 FF                  call 0x1406ae970
0087CFA9  8B F8                           mov edi, eax
0087CFAB  3D 35 00 00 C0                  cmp eax, 0xc0000035
0087CFB0  75 20                           jne 0x14087cfd2
0087CFB2  4D 8B 04 24                     mov r8, qword ptr [r12]
0087CFB6  48 8D 45 E0                     lea rax, [rbp - 0x20]
0087CFBA  4C 8D 4D 50                     lea r9, [rbp + 0x50]
0087CFBE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0087CFC3  BA 7F 00 1F 00                  mov edx, 0x1f007f
0087CFC8  49 8B CF                        mov rcx, r15
0087CFCB  E8 C0 27 E3 FF                  call 0x1406af790
0087CFD0  8B F8                           mov edi, eax
0087CFD2  85 FF                           test edi, edi
0087CFD4  79 0F                           jns 0x14087cfe5
0087CFD6  C7 83 40 10 00 00 0D 00 00 00   mov dword ptr [rbx + 0x1040], 0xd
0087CFE0  E9 B7 01 00 00                  jmp 0x14087d19c
0087CFE5  49 8B 0F                        mov rcx, qword ptr [r15]
0087CFE8  E8 23 30 E3 FF                  call 0x1406b0010
0087CFED  8B F8                           mov edi, eax
0087CFEF  85 C0                           test eax, eax
0087CFF1  79 0F                           jns 0x14087d002
0087CFF3  C7 83 40 10 00 00 0E 00 00 00   mov dword ptr [rbx + 0x1040], 0xe
0087CFFD  E9 9A 01 00 00                  jmp 0x14087d19c
0087D002  49 8B 0F                        mov rcx, qword ptr [r15]
0087D005  48 8D 45 88                     lea rax, [rbp - 0x78]
0087D009  4C 8B 05 28 A3 74 00            mov r8, qword ptr [rip + 0x74a328]
0087D010  45 33 FF                        xor r15d, r15d
0087D013  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
0087D018  45 33 C9                        xor r9d, r9d
0087D01B  BA 7F 00 1F 00                  mov edx, 0x1f007f
0087D020  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0087D025  4C 89 7D 88                     mov qword ptr [rbp - 0x78], r15
0087D029  E8 82 BD FE FF                  call 0x140868db0
0087D02E  8B F8                           mov edi, eax
0087D030  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
0087D034  48 89 46 38                     mov qword ptr [rsi + 0x38], rax
0087D038  85 FF                           test edi, edi
0087D03A  79 0F                           jns 0x14087d04b
0087D03C  C7 83 40 10 00 00 0F 00 00 00   mov dword ptr [rbx + 0x1040], 0xf
0087D046  E9 6C 01 00 00                  jmp 0x14087d1b7
0087D04B  4D 85 ED                        test r13, r13
0087D04E  75 75                           jne 0x14087d0c5
0087D050  48 89 35 21 2C 67 00            mov qword ptr [rip + 0x672c21], rsi
0087D057  48 8D 0D 5A C8 58 00            lea rcx, [rip + 0x58c85a]
0087D05E  41 BD 07 00 00 00               mov r13d, 7
0087D064  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0087D068  48 85 C0                        test rax, rax
0087D06B  74 14                           je 0x14087d081
0087D06D  8B 80 A0 00 00 00               mov eax, dword ptr [rax + 0xa0]
0087D073  A8 02                           test al, 2
0087D075  75 0A                           jne 0x14087d081
0087D077  44 01 76 40                     add dword ptr [rsi + 0x40], r14d
0087D07B  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0087D07F  EB 19                           jmp 0x14087d09a
0087D081  48 8B 01                        mov rax, qword ptr [rcx]
0087D084  48 85 C0                        test rax, rax
0087D087  74 18                           je 0x14087d0a1
0087D089  8B 80 A0 00 00 00               mov eax, dword ptr [rax + 0xa0]
0087D08F  A8 02                           test al, 2
0087D091  75 0E                           jne 0x14087d0a1
0087D093  44 01 76 40                     add dword ptr [rsi + 0x40], r14d
0087D097  48 8B 01                        mov rax, qword ptr [rcx]
0087D09A  48 89 B0 38 10 00 00            mov qword ptr [rax + 0x1038], rsi
0087D0A1  48 81 C1 B8 00 00 00            add rcx, 0xb8
0087D0A8  4D 2B EE                        sub r13, r14
0087D0AB  75 B7                           jne 0x14087d064
0087D0AD  48 8B 05 DC C9 75 00            mov rax, qword ptr [rip + 0x75c9dc]
0087D0B4  4C 8B 6D D8                     mov r13, qword ptr [rbp - 0x28]
0087D0B8  48 89 B0 38 10 00 00            mov qword ptr [rax + 0x1038], rsi
0087D0BF  44 01 76 40                     add dword ptr [rsi + 0x40], r14d
0087D0C3  EB 0B                           jmp 0x14087d0d0
0087D0C5  49 89 B5 38 10 00 00            mov qword ptr [r13 + 0x1038], rsi
0087D0CC  44 89 76 40                     mov dword ptr [rsi + 0x40], r14d
0087D0D0  4C 89 6E 50                     mov qword ptr [rsi + 0x50], r13
0087D0D4  E8 B7 43 13 00                  call 0x1409b1490
0087D0D9  48 8B 05 D8 85 67 00            mov rax, qword ptr [rip + 0x6785d8]
0087D0E0  48 8D 15 C9 85 67 00            lea rdx, [rip + 0x6785c9]
0087D0E7  48 39 10                        cmp qword ptr [rax], rdx
0087D0EA  74 07                           je 0x14087d0f3
0087D0EC  B9 03 00 00 00                  mov ecx, 3
0087D0F1  CD 29                           int 0x29
0087D0F3  48 89 16                        mov qword ptr [rsi], rdx
0087D0F6  48 8D 0D 63 85 67 00            lea rcx, [rip + 0x678563]
0087D0FD  48 89 46 08                     mov qword ptr [rsi + 8], rax
0087D101  48 89 30                        mov qword ptr [rax], rsi
0087D104  48 89 35 AD 85 67 00            mov qword ptr [rip + 0x6785ad], rsi
0087D10B  E8 90 32 9D FF                  call 0x1402503a0
0087D110  E8 9B 07 9E FF                  call 0x14025d8b0
0087D115  44 38 7C 24 60                  cmp byte ptr [rsp + 0x60], r15b
0087D11A  74 0A                           je 0x14087d126
0087D11C  33 D2                           xor edx, edx
0087D11E  48 8B CE                        mov rcx, rsi
0087D121  E8 D6 39 F7 FF                  call 0x1407f0afc
0087D126  33 C0                           xor eax, eax
0087D128  48 8B 8D 90 00 00 00            mov rcx, qword ptr [rbp + 0x90]
0087D12F  48 33 CC                        xor rcx, rsp
0087D132  E8 09 F5 E2 FF                  call 0x1406ac640
0087D137  4C 8D 9C 24 C0 01 00 00         lea r11, [rsp + 0x1c0]
0087D13F  49 8B 5B 50                     mov rbx, qword ptr [r11 + 0x50]
0087D143  41 0F 28 73 F0                  movaps xmm6, xmmword ptr [r11 - 0x10]
0087D148  41 0F 28 7B E0                  movaps xmm7, xmmword ptr [r11 - 0x20]
0087D14D  49 8B E3                        mov rsp, r11
0087D150  41 5F                           pop r15
0087D152  41 5E                           pop r14
0087D154  41 5D                           pop r13
0087D156  41 5C                           pop r12
0087D158  5F                              pop rdi
0087D159  5E                              pop rsi
0087D15A  5D                              pop rbp
0087D15B  C3                              ret
0087D15C  CC                              int3
0087D15D  C7 83 40 10 00 00 0A 00 00 00   mov dword ptr [rbx + 0x1040], 0xa
0087D167  EB 4E                           jmp 0x14087d1b7
0087D169  C7 83 40 10 00 00 09 00 00 00   mov dword ptr [rbx + 0x1040], 9
0087D173  EB 27                           jmp 0x14087d19c
0087D175  C7 83 40 10 00 00 08 00 00 00   mov dword ptr [rbx + 0x1040], 8
0087D17F  EB 36                           jmp 0x14087d1b7
0087D181  C7 83 40 10 00 00 06 00 00 00   mov dword ptr [rbx + 0x1040], 6
0087D18B  EB 0F                           jmp 0x14087d19c
0087D18D  BF 9A 00 00 C0                  mov edi, 0xc000009a
0087D192  C7 83 40 10 00 00 05 00 00 00   mov dword ptr [rbx + 0x1040], 5
0087D19C  45 33 FF                        xor r15d, r15d
0087D19F  EB 16                           jmp 0x14087d1b7
0087D1A1  C7 83 40 10 00 00 04 00 00 00   mov dword ptr [rbx + 0x1040], 4
0087D1AB  EB 0A                           jmp 0x14087d1b7
0087D1AD  C7 83 40 10 00 00 03 00 00 00   mov dword ptr [rbx + 0x1040], 3
0087D1B7  44 8B C7                        mov r8d, edi
0087D1BA  48 8B D3                        mov rdx, rbx
0087D1BD  E8 BA 00 00 00                  call 0x14087d27c
0087D1C2  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
0087D1C6  48 85 C9                        test rcx, rcx
0087D1C9  74 10                           je 0x14087d1db
0087D1CB  48 FF 15 76 40 8D FF            call qword ptr [rip - 0x72bf8a]
0087D1D2  0F 1F 44 00 00                  nop dword ptr [rax + rax]
0087D1D7  4C 89 7D 98                     mov qword ptr [rbp - 0x68], r15
0087D1DB  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0087D1DF  48 85 C9                        test rcx, rcx
0087D1E2  74 0C                           je 0x14087d1f0
0087D1E4  48 FF 15 65 40 8D FF            call qword ptr [rip - 0x72bf9b]
0087D1EB  0F 1F 44 00 00                  nop dword ptr [rax + rax]
0087D1F0  4C 39 7D A8                     cmp qword ptr [rbp - 0x58], r15
0087D1F4  74 09                           je 0x14087d1ff
0087D1F6  48 8D 4D A0                     lea rcx, [rbp - 0x60]
0087D1FA  E8 01 36 14 00                  call 0x1409c0800
0087D1FF  4C 39 7D C0                     cmp qword ptr [rbp - 0x40], r15
0087D203  74 09                           je 0x14087d20e
0087D205  48 8D 4D B8                     lea rcx, [rbp - 0x48]
0087D209  E8 F2 35 14 00                  call 0x1409c0800
0087D20E  4C 39 7D 80                     cmp qword ptr [rbp - 0x80], r15
0087D212  74 0A                           je 0x14087d21e
0087D214  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
0087D219  E8 E2 35 14 00                  call 0x1409c0800
0087D21E  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
0087D222  48 85 C9                        test rcx, rcx
0087D225  74 05                           je 0x14087d22c
0087D227  E8 84 00 E3 FF                  call 0x1406ad2b0
0087D22C  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
0087D230  48 85 C9                        test rcx, rcx
0087D233  74 05                           je 0x14087d23a
0087D235  E8 16 C1 A7 FF                  call 0x1402f9350
0087D23A  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
0087D23E  48 85 C9                        test rcx, rcx
0087D241  74 05                           je 0x14087d248
0087D243  E8 68 00 E3 FF                  call 0x1406ad2b0
0087D248  BA 43 4D 52 6D                  mov edx, 0x6d524d43
0087D24D  48 8B CE                        mov rcx, rsi
0087D250  E8 1B 56 30 00                  call 0x140b82870
0087D255  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
0087D259  E8 02 E8 B0 FF                  call 0x14038ba60
0087D25E  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
0087D262  33 D2                           xor edx, edx
0087D264  E8 07 56 30 00                  call 0x140b82870
0087D269  89 BB 44 10 00 00               mov dword ptr [rbx + 0x1044], edi
0087D26F  E9 CB F5 FF FF                  jmp 0x14087c83f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpInitCmRM(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m148;
    unsigned __int16 v_stack_m17E;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m188;
    unsigned int v_stack_m18C;
    unsigned __int8 v_stack_m190;
    unsigned int v_stack_m194;
    unsigned __int8 v_stack_m198;
    unsigned int v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned int v_stack_m1B8;
    unsigned int v_stack_m1C0;
    unsigned int v_stack_m1C8;
    unsigned int v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m38;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    v_rsp = (v_rsp) - (448);
    *(unsigned __int64 *)(v_rsp - 72) = v_xmm6;
    *(unsigned __int64 *)(v_rsp - 88) = v_xmm7;
    result = (*(unsigned __int64 *)(v_rip + 5824529)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 248 + 144) = result;
    v_r14 = 0;
    v_stack_m198 = (unsigned __int8)(a2);
    *(unsigned __int64 *)(v_rsp - 248 - 40) = a1;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 248 - 96) = 0;
    *(unsigned __int64 *)(v_rsp - 248 - 88) = 0;
    *(unsigned __int64 *)(v_rsp - 248) = 0;
    *(unsigned __int64 *)(v_rsp - 248 + 128) = v_xmm0;
    *(unsigned int *)(v_rsp - 248 + 8) = 0;
    *(unsigned __int64 *)(v_rsp - 248 + 80) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 248 - 72) = 0;
    *(unsigned __int64 *)(v_rsp - 248 + 96) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 248 - 64) = 0;
    *(unsigned __int64 *)(v_rsp - 248 + 112) = v_xmm1;
    v_stack_m180 = 0;
    *(unsigned __int64 *)(v_rsp - 248 - 32) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 248 - 128) = 0;
    *(unsigned __int64 *)(v_rsp - 248 - 16) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 248 - 112) = 0;
    *(unsigned __int64 *)(v_rsp - 248 - 56) = 0;
    *(unsigned __int64 *)(v_rsp - 248 - 48) = 0;
    v_stack_m188 = 0;
    *(unsigned __int64 *)(v_rsp - 248 - 120) = 0;
    *(unsigned __int64 *)(v_rsp - 248 - 104) = 0;
    *(unsigned __int64 *)(v_rsp - 248 + 24) = v_xmm0;
    *(unsigned int *)(v_rsp - 248 + 72) = 0;
    *(unsigned __int64 *)(v_rsp - 248 + 40) = v_xmm0;
    v_stack_m194 = 0;
    *(unsigned __int64 *)(v_rsp - 248 + 56) = v_xmm0;
    v_stack_m18C = 512;
    v_stack_m190 = 0;
    if ((*(unsigned __int8 *)(v_rip + 7714994)) != 0) goto loc_0087D126;
    v_rbx = *(unsigned __int64 *)(v_rip + 5821186);
    if (a1 != 0) { v_rbx = a1; }
    if (((*(unsigned int *)(v_rbx + 160)) & (0x8001ULL)) != 0) goto loc_0087D126;
loc_0087C7FA:
    result = ExUuidCreate(v_rsp - 248 + 96, a2, a3, a4);
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC000022DULL)))) goto loc_0087C820;
    *(unsigned __int64 *)(v_rsp - 248 - 80) = 0xFFFFFFFFFF676980ULL;
    a2 = 0;
    a1 = 0;
    result = KeDelayExecutionThread(a1, a2, v_rsp - 248 - 80, a4);
    goto loc_0087C7FA;
loc_0087C820:
    if (!sign_flag) goto loc_0087C846;
loc_0087C824:
    *(unsigned int *)(v_rbx + 4160) = 1;
loc_0087C82E:
    *(unsigned int *)(v_rbx + 4164) = (unsigned int)((unsigned int)((unsigned int)(result)));
    result = CmpLogTxrInitEvent(a1, v_rbx, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
loc_0087C83F:
    goto loc_0087D128;
loc_0087C846:
    result = ExUuidCreate(v_rsp - 248 + 112, v_rbx, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a4);
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0xC000022DULL)))) goto loc_0087C86C;
    *(unsigned __int64 *)(v_rsp - 248 - 80) = 0xFFFFFFFFFF676980ULL;
    a2 = 0;
    a1 = 0;
    result = KeDelayExecutionThread(a1, a2, v_rsp - 248 - 80, a4);
    goto loc_0087C846;
loc_0087C86C:
    if (sign_flag) goto loc_0087C824;
    result = ExAllocatePool2(136 + 120, 136, (unsigned int)((unsigned int)((unsigned int)(0x6D524D43ULL))), a4);
    if (result != 0) goto loc_0087C89E;
    *(unsigned int *)(v_rbx + 4160) = 1;
loc_0087C897:
    goto loc_0087C82E;
loc_0087C89E:
    result = ExAllocatePool2(104 - 40, 104, (unsigned int)(0x6C724D43ULL), a4);
    *(unsigned __int64 *)(v_rsp - 248 + 16) = result;
    if (result != 0) goto loc_0087C8D3;
    result = ExFreePoolWithTag(result, (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), (unsigned int)(0x6C724D43ULL), a4);
    *(unsigned int *)(v_rbx + 4160) = 2;
    goto loc_0087C897;
loc_0087C8D3:
    *(unsigned __int64 *)(result + 16 + 8) = result + 16;
    *(unsigned __int64 *)(result + 16) = result + 16;
    result = (unsigned __int8)(-((unsigned __int8)((unsigned int)(v_stack_m198))));
    *(unsigned __int64 *)(result + 88) = 0;
    *(unsigned __int64 *)(result + 96) = 0;
    a1 = (unsigned int)((result) & (4));
    *(unsigned int *)(result + 104) = (unsigned int)(a1);
    *(unsigned __int64 *)(result + 108) = 0;
    *(unsigned int *)(result + 68) = 0;
    *(unsigned __int64 *)(result + 72) = 0;
    *(unsigned __int64 *)(result + 128) = (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)));
    result = ExInitializeResourceLite((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), (unsigned int)(0x6C724D43ULL), a4);
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rbx + 64) + 164)) == ((unsigned int)((unsigned int)(0x6D746D72ULL)))) goto loc_0087C941;
    *(unsigned int *)(*(unsigned __int64 *)(v_rbx + 64) + 164) = (unsigned int)((unsigned int)(0x6D746D72ULL));
    v_r15 = 0;
    goto loc_0087CE1D;
loc_0087C941:
    a2 = (*(unsigned __int64 *)(v_rsp - 248 + 128)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 64) + 148));
    if (!(condition_is_not_equal)) {
        a2 = *(unsigned __int64 *)(v_rsp - 248 + 136);
        a2 = (a2) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 64) + 156));
    }
    if (a2 == 0) {
        v_stack_m194 = 1;
        v_r15 = 1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 64) + 148) = v_xmm7;
    }
    a2 = (*(unsigned __int64 *)(v_rsp - 248 + 128)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 64) + 112));
    if (!(condition_is_not_equal)) {
        a2 = *(unsigned __int64 *)(v_rsp - 248 + 136);
        a2 = (a2) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 64) + 120));
    }
    if (a2 == 0) {
        v_r15 = 1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 64) + 112) = v_xmm6;
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 248 + 128)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 64) + 128));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int64 *)(v_rsp - 248 + 136);
        a1 = (a1) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 64) + 136));
    }
    if (a1 == 0) {
        v_r15 = 1;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 64) + 128) = v_xmm0;
    }
    v_stack_m18C = 512;
    v_stack_m198 = (unsigned int)((unsigned int)(v_stack_m198));
    if ((unsigned __int8)(v_r15) != 0) goto loc_0087CE54;
    v_r15 = 0;
loc_0087C9E2:
    a1 = (*(unsigned __int64 *)(v_rbx + 64)) + (148);
    *(unsigned __int64 *)(v_rsp - 248 - 80) = *(unsigned __int64 *)(v_rbx + 1544);
    result = RtlStringFromGUIDEx(a1, v_rsp - 248 - 96, 1, *(unsigned __int64 *)(v_rsp - 248 + 136));
    if (sign_flag) goto loc_0087D1AD;
    if (a1 != 0) goto loc_0087CB8A;
    v_stack_m188 = 52;
    result = Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline(a1, v_rsp - 248 - 96, 1, *(unsigned __int64 *)(v_rsp - 248 + 136));
    a1 = 512;
    if ((unsigned int)(result) == 0) { a1 = 512; }
    v_stack_m18C = (unsigned int)(a1);
loc_0087CA3C:
loc_0087CA45:
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rip - 8894038)) + (*(unsigned __int16 *)(v_rip + 5821921)));
    result = (unsigned __int16)((result) + (*(unsigned __int16 *)(v_rip + 5821898)));
    result = (unsigned __int16)((result) + (*(unsigned __int16 *)(v_rsp - 248 - 96)));
    v_stack_m17E = (unsigned __int16)((unsigned __int16)(result));
    result = ExAllocatePool2(256, (unsigned __int16)(result), (unsigned int)(0x67727453ULL), *(unsigned __int64 *)(v_rsp - 248 + 136));
    *(unsigned __int64 *)(v_rsp - 248 - 128) = result;
    if (result == 0) goto loc_0087D18D;
    result = RtlAppendUnicodeStringToString(v_stack_m180, v_rip + 5821861, (unsigned int)(0x67727453ULL), *(unsigned __int64 *)(v_rsp - 248 + 136));
    result = RtlAppendUnicodeStringToString(v_stack_m180, v_rip - 8894038, (unsigned int)(0x67727453ULL), *(unsigned __int64 *)(v_rsp - 248 + 136));
    result = RtlAppendUnicodeStringToString(v_stack_m180, v_rsp - 248 - 96, (unsigned int)(0x67727453ULL), *(unsigned __int64 *)(v_rsp - 248 + 136));
    result = RtlAppendUnicodeStringToString(v_stack_m180, v_rip + 5821833, (unsigned int)(0x67727453ULL), *(unsigned __int64 *)(v_rsp - 248 + 136));
    result = CmpQueryFileSecurityDescriptor(*(unsigned __int64 *)(v_rsp - 248 - 80), v_rsp - 248 - 120, (unsigned int)(0x67727453ULL), *(unsigned __int64 *)(v_rsp - 248 + 136));
    a1 = 0;
    if (sign_flag) goto loc_0087D181;
    v_stack_m1A8 = 0;
    v_stack_m1B0 = 0;
    v_stack_m1B8 = (unsigned int)((unsigned int)(v_stack_m18C));
    v_stack_m1C0 = 0;
    v_stack_m1C8 = 8;
    v_stack_m1D0 = 3;
    v_stack_m1D8 = *(unsigned __int64 *)(v_rsp - 248 - 120);
    result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsCreateLogFile(v_rsp - 248 - 112, v_stack_m180, (unsigned int)(0xC0000000ULL), a1 + 7);
    result = Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline(v_rsp - 248 - 112, v_stack_m180, (unsigned int)(0xC0000000ULL), a1 + 7);
    if ((unsigned int)(result) == 0) goto loc_0087CC04;
    v_stack_m194 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m194))));
    v_stack_m198 = (unsigned __int8)((unsigned int)(v_stack_m198));
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC01A000DULL) goto loc_0087CC09;
    v_stack_m1C8 = 70;
    v_stack_m1D0 = v_rip + 2674637;
    v_stack_m1D8 = 1;
    result = CmpDeleteCorruptedLogfile(v_rip - 8894038, v_rsp - 248 - 96, v_rip + 5821651, v_rip + 5821626);
    v_stack_m194 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m194))));
    v_stack_m198 = (unsigned __int8)((unsigned int)(v_stack_m198));
    goto loc_0087CC09;
loc_0087CB8A:
    result = CmpQueryNameString(*(unsigned __int64 *)(v_rip - 8894038 + 1544), v_rsp - 248 - 72, v_rip + 5821651, v_rip + 5821626);
    if (sign_flag) goto loc_0087D1A1;
    result = Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(v_rip - 8894038 + 1544), v_rsp - 248 - 72, v_rip + 5821651, v_rip + 5821626);
    if ((unsigned int)(result) == 0) goto loc_0087CA3C;
    result = CmpIsFileInSystemConfig(v_rsp - 248 - 72, v_stack_m190, v_rip + 5821651, v_rip + 5821626);
    if (sign_flag) goto loc_0087CE8E;
    v_stack_m198 = (unsigned int)((unsigned int)(v_stack_m198));
    v_stack_m188 = (unsigned int)((unsigned int)(v_stack_m188));
    v_stack_m194 = (unsigned int)((unsigned int)(v_stack_m194));
    if (v_stack_m190 == ((unsigned __int8)((unsigned int)(v_stack_m198)))) goto loc_0087CBFD;
loc_0087CBF3:
    v_stack_m18C = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m194))));
    goto loc_0087CA45;
loc_0087CBFD:
    goto loc_0087CBF3;
loc_0087CC04:
loc_0087CC09:
    v_r15 = 0;
    result = (unsigned int)(v_stack_m194);
    if (*(unsigned __int64 *)(v_rsp - 248 - 88) != 0) {
        result = ExFreePool(*(unsigned __int64 *)(v_rsp - 248 - 88), v_stack_m190, v_rip + 5821651, v_rip + 5821626);
        *(unsigned __int64 *)(v_rsp - 248 - 96) = v_xmm0;
        *(unsigned __int64 *)(v_rsp - 248 - 88) = v_xmm0;
    }
    if (*(unsigned __int64 *)(v_rsp - 248 - 40) != 0) {
        a1 = v_rsp - 248 - 72;
        result = RtlFreeAnsiString(a1, v_stack_m190, v_rip + 5821651, v_rip + 5821626);
    }
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 248 - 120), a2, v_rip + 5821651, v_rip + 5821626);
    if (!sign_flag) goto loc_0087CC7B;
    if ((unsigned int)((unsigned int)(v_stack_m194)) != 0) goto loc_0087CE9D;
    if (*(unsigned __int64 *)(v_rsp - 248 - 128) != 0) {
        result = ExFreePool(*(unsigned __int64 *)(v_rsp - 248 - 128), a2, v_rip + 5821651, v_rip + 5821626);
        v_stack_m180 = v_xmm0;
    }
    result = CmpLogTxrInitEvent(*(unsigned __int64 *)(v_rsp - 248 - 128), v_rbx, (unsigned int)((unsigned int)((unsigned int)(v_stack_m188))), v_rip + 5821626);
    goto loc_0087CE14;
loc_0087CC7B:
    result = 0;
    *(unsigned __int64 *)(v_rsp - 248 + 24) = v_xmm0;
    *(unsigned int *)(v_rsp - 248 + 24) = 1;
    *(unsigned __int64 *)(v_rsp - 248 + 40) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 248 + 72) = 0;
    *(unsigned __int64 *)(v_rsp - 248 + 56) = v_xmm0;
    result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsMgmtRegisterManagedClient(*(unsigned __int64 *)(v_rsp - 248 - 112), v_rsp - 248 + 24, v_rsp - 248 - 104, v_rip + 5821626);
    if (sign_flag) goto loc_0087D175;
    a2 = (*(unsigned __int16 *)(v_rip + 5821283)) + (24);
    result = ExAllocatePool2(256, a2, (unsigned int)(0x6D524D43ULL), v_rip + 5821626);
    if (result == 0) goto loc_0087D169;
    *(unsigned int *)(result) = 1;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rip + 5821241)) + (24));
    *(unsigned int *)(result + 12) = 9;
    *(unsigned int *)(result + 4) = (unsigned int)(a1);
    *(unsigned __int16 *)(result + 16) = (unsigned __int16)(*(unsigned __int16 *)(v_rip + 5821221));
    result = memcpy(result + 18, *(unsigned __int64 *)(v_rip + 5821206), *(unsigned __int16 *)(v_rip + 5821205), v_rip + 5821626);
    a3 = (unsigned int)((*(unsigned __int16 *)(v_rip + 5821185)) + (24));
    result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsMgmtInstallPolicy(*(unsigned __int64 *)(v_rsp - 248 - 112), result, a3, v_rip + 5821626);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, v_rip + 5821626);
    v_r15 = 0;
    if (sign_flag) goto loc_0087D15D;
    result = (unsigned __int16)((v_stack_m180) - ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 5821148))));
    v_stack_m1D0 = 0;
    *(unsigned __int16 *)(v_rsp - 248 - 56) = (unsigned __int16)(result);
    result = (unsigned __int16)((v_stack_m17E) - ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 5821148))));
    *(unsigned int *)(v_rsp - 248 - 32) = 48;
    *(unsigned __int16 *)(v_rsp - 248 - 54) = (unsigned __int16)(result);
    *(unsigned __int64 *)(v_rsp - 248 - 24) = 0;
    result = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rip + 5821148)))) + (*(unsigned __int64 *)(v_rsp - 248 - 128));
    *(unsigned __int64 *)(v_rsp - 248 - 48) = result;
    v_stack_m1D8 = (unsigned int)((unsigned int)(v_stack_m188));
    *(unsigned int *)(v_rsp - 248 - 8) = 576;
    *(unsigned __int64 *)(v_rsp - 248 - 16) = 0;
    *(unsigned __int64 *)(v_rsp - 248) = v_xmm0;
    result = ZwCreateTransactionManager(result + 32, (unsigned int)(0xF003FULL), v_rsp - 248 - 32, v_rsp - 248 - 56);
    if (((unsigned int)(result)) != 0xC0000035ULL) goto loc_0087CEAC;
    if ((*(unsigned __int64 *)(v_rsp - 248 - 128)) != 0) {
        a1 = v_stack_m180;
        result = RtlFreeAnsiString(a1, (unsigned int)(0xF003FULL), v_rsp - 248 - 32, v_rsp - 248 - 56);
    }
    if (*(unsigned __int64 *)(v_rsp - 248 - 112) != 0) {
        result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsCloseLogFileObject(*(unsigned __int64 *)(v_rsp - 248 - 112), (unsigned int)(0xF003FULL), v_rsp - 248 - 32, v_rsp - 248 - 56);
        *(unsigned __int64 *)(v_rsp - 248 - 112) = 0;
    }
    if (*(unsigned __int64 *)(v_rsp - 248 - 104) != 0) {
        result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsMgmtDeregisterManagedClient(*(unsigned __int64 *)(v_rsp - 248 - 104), (unsigned int)(0xF003FULL), v_rsp - 248 - 32, v_rsp - 248 - 56);
        *(unsigned __int64 *)(v_rsp - 248 - 104) = 0;
    }
    if (v_stack_m194 != 0) goto loc_0087CEBB;
loc_0087CE14:
loc_0087CE1D:
    v_rdi = (unsigned __int8)((unsigned int)(v_stack_m198));
    if (*(unsigned __int64 *)(v_rsp - 248 - 40) == 0) { v_rdi = 1; }
    v_stack_m194 = 1;
    v_stack_m198 = (unsigned int)(v_rdi);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 64) + 148) = v_xmm7;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 64) + 112) = v_xmm6;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 64) + 128) = v_xmm6;
    goto loc_0087CE57;
loc_0087CE54:
    v_r15 = 0;
loc_0087CE57:
    result = CmpLockRegistry(*(unsigned __int64 *)(v_rsp - 248 - 104), (unsigned int)(0xF003FULL), v_rsp - 248 - 32, v_rsp - 248 - 56);
    result = HvLockHiveFlusherShared(v_rbx, (unsigned int)(0xF003FULL), v_rsp - 248 - 32, v_rsp - 248 - 56);
    result = HvLockHiveWriter(v_rbx, (unsigned int)(0xF003FULL), v_rsp - 248 - 32, v_rsp - 248 - 56);
    result = HvMarkBaseBlockDirty(v_rbx, (unsigned int)(0xF003FULL), v_rsp - 248 - 32, v_rsp - 248 - 56);
    result = HvUnlockHiveWriter(v_rbx, (unsigned int)(0xF003FULL), v_rsp - 248 - 32, v_rsp - 248 - 56);
    result = HvUnlockHiveFlusherShared(v_rbx, (unsigned int)(0xF003FULL), v_rsp - 248 - 32, v_rsp - 248 - 56);
    result = CmpUnlockRegistry(v_rbx, (unsigned int)(0xF003FULL), v_rsp - 248 - 32, v_rsp - 248 - 56);
    goto loc_0087C9E2;
loc_0087CE8E:
    *(unsigned int *)(v_rbx + 4160) = 16;
    goto loc_0087D1B7;
loc_0087CE9D:
    *(unsigned int *)(v_rbx + 4160) = 7;
    goto loc_0087D1B7;
loc_0087CEAC:
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)((unsigned int)(v_stack_m18C));
        result = ZwRecoverTransactionManager(a1, (unsigned int)(0xF003FULL), v_rsp - 248 - 32, v_rsp - 248 - 56);
        v_rdi = (unsigned int)(result);
    }
    result = RtlFreeAnsiString(v_stack_m180, (unsigned int)(0xF003FULL), v_rsp - 248 - 32, v_rsp - 248 - 56);
    if (!sign_flag) goto loc_0087CED8;
    *(unsigned int *)(v_rbx + 4160) = 11;
    goto loc_0087D1B7;
loc_0087CED8:
    if (*(unsigned __int64 *)(v_rsp - 248 - 112) != 0) {
        result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsCloseLogFileObject(*(unsigned __int64 *)(v_rsp - 248 - 112), (unsigned int)(0xF003FULL), v_rsp - 248 - 32, v_rsp - 248 - 56);
        *(unsigned __int64 *)(v_rsp - 248 - 112) = 0;
    }
    if (*(unsigned __int64 *)(v_rsp - 248 - 104) != 0) {
        result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsMgmtDeregisterManagedClient(*(unsigned __int64 *)(v_rsp - 248 - 104), (unsigned int)(0xF003FULL), v_rsp - 248 - 32, v_rsp - 248 - 56);
        *(unsigned __int64 *)(v_rsp - 248 - 104) = 0;
    }
    a4 = 0;
    v_stack_m1D0 = 0;
    v_stack_m1D8 = v_rsp - 248 - 120;
    *(unsigned __int64 *)(v_rsp - 248 - 120) = 0;
    result = ObReferenceObjectByHandle(*(unsigned __int64 *)((unsigned int)(v_stack_m18C)), (unsigned int)(0xF003FULL), *(unsigned __int64 *)(v_rip + 7644191), a4);
    *(unsigned __int64 *)(result + 40) = *(unsigned __int64 *)(v_rsp - 248 - 120);
    if (!sign_flag) goto loc_0087CF51;
    *(unsigned int *)(v_rbx + 4160) = 12;
    goto loc_0087D1B7;
loc_0087CF51:
    *(unsigned __int64 *)(v_rsp - 248 - 24) = 0;
    *(unsigned __int64 *)(v_rsp - 248 - 16) = 0;
    *(unsigned __int64 *)(v_rsp - 248 + 80) = v_xmm0;
    *(unsigned int *)(v_rsp - 248 - 32) = 48;
    *(unsigned int *)(v_rsp - 248 - 8) = 576;
    *(unsigned __int64 *)(v_rsp - 248) = v_xmm0;
    v_stack_m1D8 = v_rsp - 248 - 32;
    result = ZwCreateResourceManager(result + 48, (unsigned int)(0x1F007FULL), *(unsigned __int64 *)((unsigned int)(v_stack_m18C)), v_rsp - 248 + 80);
    v_rdi = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(result)) == 0xC0000035ULL) {
        a3 = *(unsigned __int64 *)((unsigned int)(v_stack_m18C));
        result = v_rsp - 248 - 32;
        a4 = v_rsp - 248 + 80;
        v_stack_m1D8 = result;
        a2 = 0x1F007FULL;
        a1 = result + 48;
        result = ZwOpenResourceManager(a1, a2, a3, a4);
        v_rdi = (unsigned int)(result);
    }
    if (!sign_flag) goto loc_0087CFE5;
    *(unsigned int *)(v_rbx + 4160) = 13;
    goto loc_0087D19C;
loc_0087CFE5:
    result = ZwRecoverResourceManager(*(unsigned __int64 *)(result + 48), a2, a3, a4);
    if (!sign_flag) goto loc_0087D002;
    *(unsigned int *)(v_rbx + 4160) = 14;
    goto loc_0087D19C;
loc_0087D002:
    v_r15 = 0;
    v_stack_m1D0 = 0;
    a4 = 0;
    v_stack_m1D8 = v_rsp - 248 - 120;
    *(unsigned __int64 *)(v_rsp - 248 - 120) = 0;
    result = ObReferenceObjectByHandle(*(unsigned __int64 *)(result + 48), (unsigned int)(0x1F007FULL), *(unsigned __int64 *)(v_rip + 7643944), a4);
    *(unsigned __int64 *)(result + 56) = *(unsigned __int64 *)(v_rsp - 248 - 120);
    if (!sign_flag) goto loc_0087D04B;
    *(unsigned int *)(v_rbx + 4160) = 15;
    goto loc_0087D1B7;
loc_0087D04B:
    if (*(unsigned __int64 *)(v_rsp - 248 - 40) != 0) goto loc_0087D0C5;
    *(unsigned __int64 *)(v_rip + 6761505) = result;
loc_0087D064:
    if (*(unsigned __int64 *)(v_rip + 5818458 + 24) == 0) goto loc_0087D081;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5818458 + 24) + 160)))) & (2)) != 0) goto loc_0087D081;
    goto loc_0087D09A;
loc_0087D081:
    if (*(unsigned __int64 *)(v_rip + 5818458) == 0) goto loc_0087D0A1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 5818458) + 160)))) & (2)) != 0) goto loc_0087D0A1;
loc_0087D09A:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5818458) + 4152) = result;
loc_0087D0A1:
    a1 = (v_rip + 5818458) + (184);
    v_r13 = (7) - (1);
    if (condition_is_not_equal) goto loc_0087D064;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7719388) + 4152) = result;
    goto loc_0087D0D0;
loc_0087D0C5:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 248 - 40) + 4152) = result;
    *(unsigned int *)(result + 64) = 1;
loc_0087D0D0:
    *(unsigned __int64 *)(result + 80) = *(unsigned __int64 *)(v_rsp - 248 - 40);
    result = LOCK_CM_RM_LIST(a1, (unsigned int)(0x1F007FULL), *(unsigned __int64 *)(v_rip + 7643944), a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6784472))) != (v_rip + 6784457)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(result) = v_rip + 6784457;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(v_rip + 6784472);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6784472)) = result;
    *(unsigned __int64 *)(v_rip + 6784429) = result;
    result = ExReleaseFastMutexUnsafe(v_rip + 6784355, v_rip + 6784457, *(unsigned __int64 *)(v_rip + 7643944), a4);
    result = KeLeaveCriticalRegion(v_rip + 6784355, v_rip + 6784457, *(unsigned __int64 *)(v_rip + 7643944), a4);
    if (v_stack_m198 != 0) {
        a2 = 0;
        a1 = result;
        result = CmpStartRMLog(a1, a2, *(unsigned __int64 *)(v_rip + 7643944), a4);
    }
    result = 0;
loc_0087D128:
    a1 = (*(unsigned __int64 *)(v_rsp - 248 + 144)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, *(unsigned __int64 *)(v_rip + 7643944), a4);
    return result;
loc_0087D15D:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m38 + 80) + 4160) = 10;
    goto loc_0087D1B7;
loc_0087D169:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m38 + 80) + 4160) = 9;
    goto loc_0087D19C;
loc_0087D175:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m38 + 80) + 4160) = 8;
    goto loc_0087D1B7;
loc_0087D181:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m38 + 80) + 4160) = 6;
    goto loc_0087D19C;
loc_0087D18D:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m38 + 80) + 4160) = 5;
loc_0087D19C:
    v_r15 = 0;
    goto loc_0087D1B7;
loc_0087D1A1:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m38 + 80) + 4160) = 4;
    goto loc_0087D1B7;
loc_0087D1AD:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m38 + 80) + 4160) = 3;
loc_0087D1B7:
    result = CmpLogTxrInitEvent(a1, *(unsigned __int64 *)(v_stack_m38 + 80), (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), a4);
    if (*(unsigned __int64 *)(v_rsp - 248 - 104) != 0) {
        result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsMgmtDeregisterManagedClient(*(unsigned __int64 *)(v_rsp - 248 - 104), *(unsigned __int64 *)(v_stack_m38 + 80), (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), a4);
        *(unsigned __int64 *)(v_rsp - 248 - 104) = 0;
    }
    if (*(unsigned __int64 *)(v_rsp - 248 - 112) != 0) {
        result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsCloseLogFileObject(*(unsigned __int64 *)(v_rsp - 248 - 112), *(unsigned __int64 *)(v_stack_m38 + 80), (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), a4);
    }
    if ((*(unsigned __int64 *)(v_rsp - 248 - 88)) != 0) {
        a1 = v_rsp - 248 - 96;
        result = RtlFreeAnsiString(a1, *(unsigned __int64 *)(v_stack_m38 + 80), (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), a4);
    }
    if ((*(unsigned __int64 *)(v_rsp - 248 - 64)) != 0) {
        a1 = v_rsp - 248 - 72;
        result = RtlFreeAnsiString(a1, *(unsigned __int64 *)(v_stack_m38 + 80), (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), a4);
    }
    if ((*(unsigned __int64 *)(v_rsp - 248 - 128)) != 0) {
        a1 = v_stack_m148;
        result = RtlFreeAnsiString(a1, *(unsigned __int64 *)(v_stack_m38 + 80), (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), a4);
    }
    if (*(unsigned __int64 *)(result + 48) != 0) {
        result = ZwClose(*(unsigned __int64 *)(result + 48), *(unsigned __int64 *)(v_stack_m38 + 80), (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), a4);
    }
    if (*(unsigned __int64 *)(result + 40) != 0) {
        result = ObfDereferenceObject(*(unsigned __int64 *)(result + 40), *(unsigned __int64 *)(v_stack_m38 + 80), (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), a4);
    }
    if (*(unsigned __int64 *)(result + 32) != 0) {
        result = ZwClose(*(unsigned __int64 *)(result + 32), *(unsigned __int64 *)(v_stack_m38 + 80), (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), a4);
    }
    result = ExFreePoolWithTag(result, (unsigned int)(0x6D524D43ULL), (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), a4);
    result = ExDeleteResourceLite(*(unsigned __int64 *)(v_rsp - 248 + 16), (unsigned int)(0x6D524D43ULL), (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), a4);
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 248 + 16), a2, (unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), a4);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m38 + 80) + 4164) = (unsigned int)((unsigned int)(0xC000009AULL));
    goto loc_0087C83F;
}
```

## 5. (Beta) C Style

```c
int64_t CmpInitCmRM(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m148;
    uint16_t v_stack_m17E;
    uint64_t v_stack_m180;
    uint32_t v_stack_m188;
    uint32_t v_stack_m18C;
    uint8_t v_stack_m190;
    uint32_t v_stack_m194;
    uint8_t v_stack_m198;
    uint32_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint32_t v_stack_m1B8;
    uint32_t v_stack_m1C0;
    uint32_t v_stack_m1C8;
    uint32_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m38;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    local_rsp = (local_rsp) - (448);
    *(uint64_t *)(local_rsp - 0x48) = v_xmm6;
    *(uint64_t *)(local_rsp - 0x58) = v_xmm7;
    result = (*(uint64_t *)(v_rip + 0x58E011)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0xF8 + 0x90) = result;
    local_r14 = 0;
    v_stack_m198 = (uint8_t)(Arg2);
    *(uint64_t *)(local_rsp - 0xF8 - 0x28) = Arg1;
    result = 0;
    *(uint64_t *)(local_rsp - 0xF8 - 0x60) = 0;
    *(uint64_t *)(local_rsp - 0xF8 - 0x58) = 0;
    *(uint64_t *)(local_rsp - 0xF8) = 0;
    *(uint64_t *)(local_rsp - 0xF8 + 0x80) = v_xmm0;
    *(uint32_t *)(local_rsp - 0xF8 + 0x8) = 0;
    *(uint64_t *)(local_rsp - 0xF8 + 0x50) = v_xmm1;
    *(uint64_t *)(local_rsp - 0xF8 - 0x48) = 0;
    *(uint64_t *)(local_rsp - 0xF8 + 0x60) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xF8 - 0x40) = 0;
    *(uint64_t *)(local_rsp - 0xF8 + 0x70) = v_xmm1;
    v_stack_m180 = 0;
    *(uint64_t *)(local_rsp - 0xF8 - 0x20) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xF8 - 0x80) = 0;
    *(uint64_t *)(local_rsp - 0xF8 - 0x10) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xF8 - 0x70) = 0;
    *(uint64_t *)(local_rsp - 0xF8 - 0x38) = 0;
    *(uint64_t *)(local_rsp - 0xF8 - 0x30) = 0;
    v_stack_m188 = 0;
    *(uint64_t *)(local_rsp - 0xF8 - 0x78) = 0;
    *(uint64_t *)(local_rsp - 0xF8 - 0x68) = 0;
    *(uint64_t *)(local_rsp - 0xF8 + 0x18) = v_xmm0;
    *(uint32_t *)(local_rsp - 0xF8 + 0x48) = 0;
    *(uint64_t *)(local_rsp - 0xF8 + 0x28) = v_xmm0;
    v_stack_m194 = 0;
    *(uint64_t *)(local_rsp - 0xF8 + 0x38) = v_xmm0;
    v_stack_m18C = 512;
    v_stack_m190 = 0;
    if ((*(uint8_t *)(v_rip + 0x75B8B2)) != 0) goto loc_0087D126;
    local_rbx = *(uint64_t *)(v_rip + 0x58D302);
    if (Arg1 != 0) { local_rbx = Arg1; }
    if (((*(uint32_t *)(local_rbx + 0xA0)) & (0x8001ULL)) != 0) goto loc_0087D126;
loc_0087C7FA:
    result = ExUuidCreate(local_rsp - 248 + 96, Arg2, a3, a4);
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC000022DULL)))) goto loc_0087C820;
    *(uint64_t *)(local_rsp - 0xF8 - 0x50) = 0xFFFFFFFFFF676980ULL;
    Arg2 = 0;
    Arg1 = 0;
    result = KeDelayExecutionThread(Arg1, Arg2, local_rsp - 248 - 80, a4);
    goto loc_0087C7FA;
loc_0087C820:
    if (!sign_flag) goto loc_0087C846;
loc_0087C824:
    *(uint32_t *)(local_rbx + 0x1040) = 1;
loc_0087C82E:
    *(uint32_t *)(local_rbx + 0x1044) = (uint32_t)((uint32_t)((uint32_t)(result)));
    result = CmpLogTxrInitEvent(Arg1, local_rbx, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a4);
loc_0087C83F:
    goto loc_0087D128;
loc_0087C846:
    result = ExUuidCreate(local_rsp - 248 + 112, local_rbx, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), a4);
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0xC000022DULL)))) goto loc_0087C86C;
    *(uint64_t *)(local_rsp - 0xF8 - 0x50) = 0xFFFFFFFFFF676980ULL;
    Arg2 = 0;
    Arg1 = 0;
    result = KeDelayExecutionThread(Arg1, Arg2, local_rsp - 248 - 80, a4);
    goto loc_0087C846;
loc_0087C86C:
    if (sign_flag) goto loc_0087C824;
    result = ExAllocatePool2(136 + 120, 136, (uint32_t)((uint32_t)((uint32_t)(0x6D524D43ULL))), a4);
    if (result != 0) goto loc_0087C89E;
    *(uint32_t *)(local_rbx + 0x1040) = 1;
loc_0087C897:
    goto loc_0087C82E;
loc_0087C89E:
    result = ExAllocatePool2(104 - 40, 104, (uint32_t)(0x6C724D43ULL), a4);
    *(uint64_t *)(local_rsp - 0xF8 + 0x10) = result;
    if (result != 0) goto loc_0087C8D3;
    result = ExFreePoolWithTag(result, (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), (uint32_t)(0x6C724D43ULL), a4);
    *(uint32_t *)(local_rbx + 0x1040) = 2;
    goto loc_0087C897;
loc_0087C8D3:
    *(uint64_t *)(result + 0x10 + 0x8) = result + 16;
    *(uint64_t *)(result + 0x10) = result + 16;
    result = (uint8_t)(-((uint8_t)((uint32_t)(v_stack_m198))));
    *(uint64_t *)(result + 0x58) = 0;
    *(uint64_t *)(result + 0x60) = 0;
    Arg1 = (uint32_t)((result) & (4));
    *(uint32_t *)(result + 0x68) = (uint32_t)(Arg1);
    *(uint64_t *)(result + 0x6C) = 0;
    *(uint32_t *)(result + 0x44) = 0;
    *(uint64_t *)(result + 0x48) = 0;
    *(uint64_t *)(result + 0x80) = (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)));
    result = ExInitializeResourceLite((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), (uint32_t)(0x6C724D43ULL), a4);
    if ((*(uint32_t *)(*(uint64_t *)(local_rbx + 0x40) + 0xA4)) == ((uint32_t)((uint32_t)(0x6D746D72ULL)))) goto loc_0087C941;
    *(uint32_t *)(*(uint64_t *)(local_rbx + 0x40) + 0xA4) = (uint32_t)((uint32_t)(0x6D746D72ULL));
    local_r15 = 0;
    goto loc_0087CE1D;
loc_0087C941:
    Arg2 = (*(uint64_t *)(local_rsp - 0xF8 + 0x80)) - (*(uint64_t *)(*(uint64_t *)(local_rbx + 0x40) + 0x94));
    if (!(condition_is_not_equal)) {
        Arg2 = *(uint64_t *)(local_rsp - 0xF8 + 0x88);
        Arg2 = (Arg2) - (*(uint64_t *)(*(uint64_t *)(local_rbx + 0x40) + 0x9C));
    }
    if (Arg2 == 0) {
        v_stack_m194 = 1;
        local_r15 = 1;
        *(uint64_t *)(*(uint64_t *)(local_rbx + 0x40) + 0x94) = v_xmm7;
    }
    Arg2 = (*(uint64_t *)(local_rsp - 0xF8 + 0x80)) - (*(uint64_t *)(*(uint64_t *)(local_rbx + 0x40) + 0x70));
    if (!(condition_is_not_equal)) {
        Arg2 = *(uint64_t *)(local_rsp - 0xF8 + 0x88);
        Arg2 = (Arg2) - (*(uint64_t *)(*(uint64_t *)(local_rbx + 0x40) + 0x78));
    }
    if (Arg2 == 0) {
        local_r15 = 1;
        *(uint64_t *)(*(uint64_t *)(local_rbx + 0x40) + 0x70) = v_xmm6;
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0xF8 + 0x80)) - (*(uint64_t *)(*(uint64_t *)(local_rbx + 0x40) + 0x80));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint64_t *)(local_rsp - 0xF8 + 0x88);
        Arg1 = (Arg1) - (*(uint64_t *)(*(uint64_t *)(local_rbx + 0x40) + 0x88));
    }
    if (Arg1 == 0) {
        local_r15 = 1;
        *(uint64_t *)(*(uint64_t *)(local_rbx + 0x40) + 0x80) = v_xmm0;
    }
    v_stack_m18C = 512;
    v_stack_m198 = (uint32_t)((uint32_t)(v_stack_m198));
    if ((uint8_t)(local_r15) != 0) goto loc_0087CE54;
    local_r15 = 0;
loc_0087C9E2:
    Arg1 = (*(uint64_t *)(local_rbx + 0x40)) + (148);
    *(uint64_t *)(local_rsp - 0xF8 - 0x50) = *(uint64_t *)(local_rbx + 0x608);
    result = RtlStringFromGUIDEx(Arg1, local_rsp - 248 - 96, 1, *(uint64_t *)(local_rsp - 0xF8 + 0x88));
    if (sign_flag) goto loc_0087D1AD;
    if (Arg1 != 0) goto loc_0087CB8A;
    v_stack_m188 = 52;
    result = Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline(Arg1, local_rsp - 248 - 96, 1, *(uint64_t *)(local_rsp - 0xF8 + 0x88));
    Arg1 = 512;
    if ((uint32_t)(result) == 0) { Arg1 = 512; }
    v_stack_m18C = (uint32_t)(Arg1);
loc_0087CA3C:
loc_0087CA45:
    result = (uint16_t)((*(uint16_t *)(v_rip - 0x87B656)) + (*(uint16_t *)(v_rip + 0x58D5E1)));
    result = (uint16_t)((result) + (*(uint16_t *)(v_rip + 0x58D5CA)));
    result = (uint16_t)((result) + (*(uint16_t *)(local_rsp - 0xF8 - 0x60)));
    v_stack_m17E = (uint16_t)((uint16_t)(result));
    result = ExAllocatePool2(256, (uint16_t)(result), (uint32_t)(0x67727453ULL), *(uint64_t *)(local_rsp - 0xF8 + 0x88));
    *(uint64_t *)(local_rsp - 0xF8 - 0x80) = result;
    if (result == 0) goto loc_0087D18D;
    result = RtlAppendUnicodeStringToString(v_stack_m180, v_rip + 5821861, (uint32_t)(0x67727453ULL), *(uint64_t *)(local_rsp - 0xF8 + 0x88));
    result = RtlAppendUnicodeStringToString(v_stack_m180, v_rip - 8894038, (uint32_t)(0x67727453ULL), *(uint64_t *)(local_rsp - 0xF8 + 0x88));
    result = RtlAppendUnicodeStringToString(v_stack_m180, local_rsp - 248 - 96, (uint32_t)(0x67727453ULL), *(uint64_t *)(local_rsp - 0xF8 + 0x88));
    result = RtlAppendUnicodeStringToString(v_stack_m180, v_rip + 5821833, (uint32_t)(0x67727453ULL), *(uint64_t *)(local_rsp - 0xF8 + 0x88));
    result = CmpQueryFileSecurityDescriptor(*(uint64_t *)(local_rsp - 0xF8 - 0x50), local_rsp - 248 - 120, (uint32_t)(0x67727453ULL), *(uint64_t *)(local_rsp - 0xF8 + 0x88));
    Arg1 = 0;
    if (sign_flag) goto loc_0087D181;
    v_stack_m1A8 = 0;
    v_stack_m1B0 = 0;
    v_stack_m1B8 = (uint32_t)((uint32_t)(v_stack_m18C));
    v_stack_m1C0 = 0;
    v_stack_m1C8 = 8;
    v_stack_m1D0 = 3;
    v_stack_m1D8 = *(uint64_t *)(local_rsp - 0xF8 - 0x78);
    result = kernel_indirect_call(local_rsp - 248 - 112, v_stack_m180, (uint32_t)(0xC0000000ULL), Arg1 + 7);
    result = Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline(local_rsp - 248 - 112, v_stack_m180, (uint32_t)(0xC0000000ULL), Arg1 + 7);
    if ((uint32_t)(result) == 0) goto loc_0087CC04;
    v_stack_m194 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m194))));
    v_stack_m198 = (uint8_t)((uint32_t)(v_stack_m198));
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC01A000DULL) goto loc_0087CC09;
    v_stack_m1C8 = 70;
    v_stack_m1D0 = v_rip + 2674637;
    v_stack_m1D8 = 1;
    result = CmpDeleteCorruptedLogfile(v_rip - 8894038, local_rsp - 248 - 96, v_rip + 5821651, v_rip + 5821626);
    v_stack_m194 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m194))));
    v_stack_m198 = (uint8_t)((uint32_t)(v_stack_m198));
    goto loc_0087CC09;
loc_0087CB8A:
    result = CmpQueryNameString(*(uint64_t *)(v_rip - 0x87B656 + 0x608), local_rsp - 248 - 72, v_rip + 5821651, v_rip + 5821626);
    if (sign_flag) goto loc_0087D1A1;
    result = Feature_CLFS_Signing__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(v_rip - 0x87B656 + 0x608), local_rsp - 248 - 72, v_rip + 5821651, v_rip + 5821626);
    if ((uint32_t)(result) == 0) goto loc_0087CA3C;
    result = CmpIsFileInSystemConfig(local_rsp - 248 - 72, v_stack_m190, v_rip + 5821651, v_rip + 5821626);
    if (sign_flag) goto loc_0087CE8E;
    v_stack_m198 = (uint32_t)((uint32_t)(v_stack_m198));
    v_stack_m188 = (uint32_t)((uint32_t)(v_stack_m188));
    v_stack_m194 = (uint32_t)((uint32_t)(v_stack_m194));
    if (v_stack_m190 == ((uint8_t)((uint32_t)(v_stack_m198)))) goto loc_0087CBFD;
loc_0087CBF3:
    v_stack_m18C = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m194))));
    goto loc_0087CA45;
loc_0087CBFD:
    goto loc_0087CBF3;
loc_0087CC04:
loc_0087CC09:
    local_r15 = 0;
    result = (uint32_t)(v_stack_m194);
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x58) != 0) {
        result = ExFreePool(*(uint64_t *)(local_rsp - 0xF8 - 0x58), v_stack_m190, v_rip + 5821651, v_rip + 5821626);
        *(uint64_t *)(local_rsp - 0xF8 - 0x60) = v_xmm0;
        *(uint64_t *)(local_rsp - 0xF8 - 0x58) = v_xmm0;
    }
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x28) != 0) {
        Arg1 = local_rsp - 248 - 72;
        result = RtlFreeAnsiString(Arg1, v_stack_m190, v_rip + 5821651, v_rip + 5821626);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0xF8 - 0x78), Arg2, v_rip + 5821651, v_rip + 5821626);
    if (!sign_flag) goto loc_0087CC7B;
    if ((uint32_t)((uint32_t)(v_stack_m194)) != 0) goto loc_0087CE9D;
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x80) != 0) {
        result = ExFreePool(*(uint64_t *)(local_rsp - 0xF8 - 0x80), Arg2, v_rip + 5821651, v_rip + 5821626);
        v_stack_m180 = v_xmm0;
    }
    result = CmpLogTxrInitEvent(*(uint64_t *)(local_rsp - 0xF8 - 0x80), local_rbx, (uint32_t)((uint32_t)((uint32_t)(v_stack_m188))), v_rip + 5821626);
    goto loc_0087CE14;
loc_0087CC7B:
    result = 0;
    *(uint64_t *)(local_rsp - 0xF8 + 0x18) = v_xmm0;
    *(uint32_t *)(local_rsp - 0xF8 + 0x18) = 1;
    *(uint64_t *)(local_rsp - 0xF8 + 0x28) = v_xmm0;
    *(uint64_t *)(local_rsp - 0xF8 + 0x48) = 0;
    *(uint64_t *)(local_rsp - 0xF8 + 0x38) = v_xmm0;
    result = kernel_indirect_call(*(uint64_t *)(local_rsp - 0xF8 - 0x70), local_rsp - 248 + 24, local_rsp - 248 - 104, v_rip + 5821626);
    if (sign_flag) goto loc_0087D175;
    Arg2 = (*(uint16_t *)(v_rip + 0x58D363)) + (24);
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x6D524D43ULL), v_rip + 5821626);
    if (result == 0) goto loc_0087D169;
    *(uint32_t *)(result) = 1;
    Arg1 = (uint32_t)((*(uint16_t *)(v_rip + 0x58D339)) + (24));
    *(uint32_t *)(result + 0xC) = 9;
    *(uint32_t *)(result + 0x4) = (uint32_t)(Arg1);
    *(uint16_t *)(result + 0x10) = (uint16_t)(*(uint16_t *)(v_rip + 0x58D325));
    result = memcpy(result + 18, *(uint64_t *)(v_rip + 0x58D316), *(uint16_t *)(v_rip + 0x58D315), v_rip + 5821626);
    a3 = (uint32_t)((*(uint16_t *)(v_rip + 0x58D301)) + (24));
    result = kernel_indirect_call(*(uint64_t *)(local_rsp - 0xF8 - 0x70), result, a3, v_rip + 5821626);
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, a3, v_rip + 5821626);
    local_r15 = 0;
    if (sign_flag) goto loc_0087D15D;
    result = (uint16_t)((v_stack_m180) - ((uint16_t)(*(uint16_t *)(v_rip + 0x58D2DC))));
    v_stack_m1D0 = 0;
    *(uint16_t *)(local_rsp - 0xF8 - 0x38) = (uint16_t)(result);
    result = (uint16_t)((v_stack_m17E) - ((uint16_t)(*(uint16_t *)(v_rip + 0x58D2DC))));
    *(uint32_t *)(local_rsp - 0xF8 - 0x20) = 48;
    *(uint16_t *)(local_rsp - 0xF8 - 0x36) = (uint16_t)(result);
    *(uint64_t *)(local_rsp - 0xF8 - 0x18) = 0;
    result = ((uint32_t)((uint32_t)(*(uint16_t *)(v_rip + 0x58D2DC)))) + (*(uint64_t *)(local_rsp - 0xF8 - 0x80));
    *(uint64_t *)(local_rsp - 0xF8 - 0x30) = result;
    v_stack_m1D8 = (uint32_t)((uint32_t)(v_stack_m188));
    *(uint32_t *)(local_rsp - 0xF8 - 0x8) = 576;
    *(uint64_t *)(local_rsp - 0xF8 - 0x10) = 0;
    *(uint64_t *)(local_rsp - 0xF8) = v_xmm0;
    result = ZwCreateTransactionManager(result + 32, (uint32_t)(0xF003FULL), local_rsp - 248 - 32, local_rsp - 248 - 56);
    if (((uint32_t)(result)) != 0xC0000035ULL) goto loc_0087CEAC;
    if ((*(uint64_t *)(local_rsp - 0xF8 - 0x80)) != 0) {
        Arg1 = v_stack_m180;
        result = RtlFreeAnsiString(Arg1, (uint32_t)(0xF003FULL), local_rsp - 248 - 32, local_rsp - 248 - 56);
    }
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x70) != 0) {
        result = kernel_indirect_call(*(uint64_t *)(local_rsp - 0xF8 - 0x70), (uint32_t)(0xF003FULL), local_rsp - 248 - 32, local_rsp - 248 - 56);
        *(uint64_t *)(local_rsp - 0xF8 - 0x70) = 0;
    }
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x68) != 0) {
        result = kernel_indirect_call(*(uint64_t *)(local_rsp - 0xF8 - 0x68), (uint32_t)(0xF003FULL), local_rsp - 248 - 32, local_rsp - 248 - 56);
        *(uint64_t *)(local_rsp - 0xF8 - 0x68) = 0;
    }
    if (v_stack_m194 != 0) goto loc_0087CEBB;
loc_0087CE14:
loc_0087CE1D:
    local_rdi = (uint8_t)((uint32_t)(v_stack_m198));
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x28) == 0) { local_rdi = 1; }
    v_stack_m194 = 1;
    v_stack_m198 = (uint32_t)(local_rdi);
    *(uint64_t *)(*(uint64_t *)(local_rbx + 0x40) + 0x94) = v_xmm7;
    *(uint64_t *)(*(uint64_t *)(local_rbx + 0x40) + 0x70) = v_xmm6;
    *(uint64_t *)(*(uint64_t *)(local_rbx + 0x40) + 0x80) = v_xmm6;
    goto loc_0087CE57;
loc_0087CE54:
    local_r15 = 0;
loc_0087CE57:
    result = CmpLockRegistry(*(uint64_t *)(local_rsp - 0xF8 - 0x68), (uint32_t)(0xF003FULL), local_rsp - 248 - 32, local_rsp - 248 - 56);
    result = HvLockHiveFlusherShared(local_rbx, (uint32_t)(0xF003FULL), local_rsp - 248 - 32, local_rsp - 248 - 56);
    result = HvLockHiveWriter(local_rbx, (uint32_t)(0xF003FULL), local_rsp - 248 - 32, local_rsp - 248 - 56);
    result = HvMarkBaseBlockDirty(local_rbx, (uint32_t)(0xF003FULL), local_rsp - 248 - 32, local_rsp - 248 - 56);
    result = HvUnlockHiveWriter(local_rbx, (uint32_t)(0xF003FULL), local_rsp - 248 - 32, local_rsp - 248 - 56);
    result = HvUnlockHiveFlusherShared(local_rbx, (uint32_t)(0xF003FULL), local_rsp - 248 - 32, local_rsp - 248 - 56);
    result = CmpUnlockRegistry(local_rbx, (uint32_t)(0xF003FULL), local_rsp - 248 - 32, local_rsp - 248 - 56);
    goto loc_0087C9E2;
loc_0087CE8E:
    *(uint32_t *)(local_rbx + 0x1040) = 16;
    goto loc_0087D1B7;
loc_0087CE9D:
    *(uint32_t *)(local_rbx + 0x1040) = 7;
    goto loc_0087D1B7;
loc_0087CEAC:
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)((uint32_t)(v_stack_m18C));
        result = ZwRecoverTransactionManager(Arg1, (uint32_t)(0xF003FULL), local_rsp - 248 - 32, local_rsp - 248 - 56);
        local_rdi = (uint32_t)(result);
    }
    result = RtlFreeAnsiString(v_stack_m180, (uint32_t)(0xF003FULL), local_rsp - 248 - 32, local_rsp - 248 - 56);
    if (!sign_flag) goto loc_0087CED8;
    *(uint32_t *)(local_rbx + 0x1040) = 11;
    goto loc_0087D1B7;
loc_0087CED8:
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x70) != 0) {
        result = kernel_indirect_call(*(uint64_t *)(local_rsp - 0xF8 - 0x70), (uint32_t)(0xF003FULL), local_rsp - 248 - 32, local_rsp - 248 - 56);
        *(uint64_t *)(local_rsp - 0xF8 - 0x70) = 0;
    }
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x68) != 0) {
        result = kernel_indirect_call(*(uint64_t *)(local_rsp - 0xF8 - 0x68), (uint32_t)(0xF003FULL), local_rsp - 248 - 32, local_rsp - 248 - 56);
        *(uint64_t *)(local_rsp - 0xF8 - 0x68) = 0;
    }
    a4 = 0;
    v_stack_m1D0 = 0;
    v_stack_m1D8 = local_rsp - 248 - 120;
    *(uint64_t *)(local_rsp - 0xF8 - 0x78) = 0;
    result = ObReferenceObjectByHandle(*(uint64_t *)((uint32_t)(v_stack_m18C)), (uint32_t)(0xF003FULL), *(uint64_t *)(v_rip + 0x74A41F), a4);
    *(uint64_t *)(result + 0x28) = *(uint64_t *)(local_rsp - 0xF8 - 0x78);
    if (!sign_flag) goto loc_0087CF51;
    *(uint32_t *)(local_rbx + 0x1040) = 12;
    goto loc_0087D1B7;
loc_0087CF51:
    *(uint64_t *)(local_rsp - 0xF8 - 0x18) = 0;
    *(uint64_t *)(local_rsp - 0xF8 - 0x10) = 0;
    *(uint64_t *)(local_rsp - 0xF8 + 0x50) = v_xmm0;
    *(uint32_t *)(local_rsp - 0xF8 - 0x20) = 48;
    *(uint32_t *)(local_rsp - 0xF8 - 0x8) = 576;
    *(uint64_t *)(local_rsp - 0xF8) = v_xmm0;
    v_stack_m1D8 = local_rsp - 248 - 32;
    result = ZwCreateResourceManager(result + 48, (uint32_t)(0x1F007FULL), *(uint64_t *)((uint32_t)(v_stack_m18C)), local_rsp - 248 + 80);
    local_rdi = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(result)) == 0xC0000035ULL) {
        a3 = *(uint64_t *)((uint32_t)(v_stack_m18C));
        result = local_rsp - 248 - 32;
        a4 = local_rsp - 248 + 80;
        v_stack_m1D8 = result;
        Arg2 = 0x1F007FULL;
        Arg1 = result + 48;
        result = ZwOpenResourceManager(Arg1, Arg2, a3, a4);
        local_rdi = (uint32_t)(result);
    }
    if (!sign_flag) goto loc_0087CFE5;
    *(uint32_t *)(local_rbx + 0x1040) = 13;
    goto loc_0087D19C;
loc_0087CFE5:
    result = ZwRecoverResourceManager(*(uint64_t *)(result + 0x30), Arg2, a3, a4);
    if (!sign_flag) goto loc_0087D002;
    *(uint32_t *)(local_rbx + 0x1040) = 14;
    goto loc_0087D19C;
loc_0087D002:
    local_r15 = 0;
    v_stack_m1D0 = 0;
    a4 = 0;
    v_stack_m1D8 = local_rsp - 248 - 120;
    *(uint64_t *)(local_rsp - 0xF8 - 0x78) = 0;
    result = ObReferenceObjectByHandle(*(uint64_t *)(result + 0x30), (uint32_t)(0x1F007FULL), *(uint64_t *)(v_rip + 0x74A328), a4);
    *(uint64_t *)(result + 0x38) = *(uint64_t *)(local_rsp - 0xF8 - 0x78);
    if (!sign_flag) goto loc_0087D04B;
    *(uint32_t *)(local_rbx + 0x1040) = 15;
    goto loc_0087D1B7;
loc_0087D04B:
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x28) != 0) goto loc_0087D0C5;
    *(uint64_t *)(v_rip + 0x672C21) = result;
loc_0087D064:
    if (*(uint64_t *)(v_rip + 0x58C85A + 0x18) == 0) goto loc_0087D081;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x58C85A + 0x18) + 0xA0)))) & (2)) != 0) goto loc_0087D081;
    goto loc_0087D09A;
loc_0087D081:
    if (*(uint64_t *)(v_rip + 0x58C85A) == 0) goto loc_0087D0A1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x58C85A) + 0xA0)))) & (2)) != 0) goto loc_0087D0A1;
loc_0087D09A:
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x58C85A) + 0x1038) = result;
loc_0087D0A1:
    Arg1 = (v_rip + 5818458) + (184);
    local_r13 = (7) - (1);
    if (condition_is_not_equal) goto loc_0087D064;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x75C9DC) + 0x1038) = result;
    goto loc_0087D0D0;
loc_0087D0C5:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0xF8 - 0x28) + 0x1038) = result;
    *(uint32_t *)(result + 0x40) = 1;
loc_0087D0D0:
    *(uint64_t *)(result + 0x50) = *(uint64_t *)(local_rsp - 0xF8 - 0x28);
    result = LOCK_CM_RM_LIST(Arg1, (uint32_t)(0x1F007FULL), *(uint64_t *)(v_rip + 0x74A328), a4);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x6785D8))) != (v_rip + 6784457)) {
        Arg1 = 3;
    }
    *(uint64_t *)(result) = v_rip + 6784457;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(v_rip + 0x6785D8);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x6785D8)) = result;
    *(uint64_t *)(v_rip + 0x6785AD) = result;
    result = ExReleaseFastMutexUnsafe(v_rip + 6784355, v_rip + 6784457, *(uint64_t *)(v_rip + 0x74A328), a4);
    result = KeLeaveCriticalRegion(v_rip + 6784355, v_rip + 6784457, *(uint64_t *)(v_rip + 0x74A328), a4);
    if (v_stack_m198 != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = CmpStartRMLog(Arg1, Arg2, *(uint64_t *)(v_rip + 0x74A328), a4);
    }
    result = 0;
loc_0087D128:
    Arg1 = (*(uint64_t *)(local_rsp - 0xF8 + 0x90)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, *(uint64_t *)(v_rip + 0x74A328), a4);
    return result;
loc_0087D15D:
    *(uint32_t *)(*(uint64_t *)(v_stack_m38 + 0x50) + 0x1040) = 10;
    goto loc_0087D1B7;
loc_0087D169:
    *(uint32_t *)(*(uint64_t *)(v_stack_m38 + 0x50) + 0x1040) = 9;
    goto loc_0087D19C;
loc_0087D175:
    *(uint32_t *)(*(uint64_t *)(v_stack_m38 + 0x50) + 0x1040) = 8;
    goto loc_0087D1B7;
loc_0087D181:
    *(uint32_t *)(*(uint64_t *)(v_stack_m38 + 0x50) + 0x1040) = 6;
    goto loc_0087D19C;
loc_0087D18D:
    *(uint32_t *)(*(uint64_t *)(v_stack_m38 + 0x50) + 0x1040) = 5;
loc_0087D19C:
    local_r15 = 0;
    goto loc_0087D1B7;
loc_0087D1A1:
    *(uint32_t *)(*(uint64_t *)(v_stack_m38 + 0x50) + 0x1040) = 4;
    goto loc_0087D1B7;
loc_0087D1AD:
    *(uint32_t *)(*(uint64_t *)(v_stack_m38 + 0x50) + 0x1040) = 3;
loc_0087D1B7:
    result = CmpLogTxrInitEvent(Arg1, *(uint64_t *)(v_stack_m38 + 0x50), (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), a4);
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x68) != 0) {
        result = kernel_indirect_call(*(uint64_t *)(local_rsp - 0xF8 - 0x68), *(uint64_t *)(v_stack_m38 + 0x50), (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), a4);
        *(uint64_t *)(local_rsp - 0xF8 - 0x68) = 0;
    }
    if (*(uint64_t *)(local_rsp - 0xF8 - 0x70) != 0) {
        result = kernel_indirect_call(*(uint64_t *)(local_rsp - 0xF8 - 0x70), *(uint64_t *)(v_stack_m38 + 0x50), (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), a4);
    }
    if ((*(uint64_t *)(local_rsp - 0xF8 - 0x58)) != 0) {
        Arg1 = local_rsp - 248 - 96;
        result = RtlFreeAnsiString(Arg1, *(uint64_t *)(v_stack_m38 + 0x50), (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), a4);
    }
    if ((*(uint64_t *)(local_rsp - 0xF8 - 0x40)) != 0) {
        Arg1 = local_rsp - 248 - 72;
        result = RtlFreeAnsiString(Arg1, *(uint64_t *)(v_stack_m38 + 0x50), (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), a4);
    }
    if ((*(uint64_t *)(local_rsp - 0xF8 - 0x80)) != 0) {
        Arg1 = v_stack_m148;
        result = RtlFreeAnsiString(Arg1, *(uint64_t *)(v_stack_m38 + 0x50), (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), a4);
    }
    if (*(uint64_t *)(result + 0x30) != 0) {
        result = ZwClose(*(uint64_t *)(result + 0x30), *(uint64_t *)(v_stack_m38 + 0x50), (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), a4);
    }
    if (*(uint64_t *)(result + 0x28) != 0) {
        result = ObfDereferenceObject(*(uint64_t *)(result + 0x28), *(uint64_t *)(v_stack_m38 + 0x50), (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), a4);
    }
    if (*(uint64_t *)(result + 0x20) != 0) {
        result = ZwClose(*(uint64_t *)(result + 0x20), *(uint64_t *)(v_stack_m38 + 0x50), (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), a4);
    }
    result = ExFreePoolWithTag(result, (uint32_t)(0x6D524D43ULL), (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), a4);
    result = ExDeleteResourceLite(*(uint64_t *)(local_rsp - 0xF8 + 0x10), (uint32_t)(0x6D524D43ULL), (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), a4);
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0xF8 + 0x10), Arg2, (uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), a4);
    *(uint32_t *)(*(uint64_t *)(v_stack_m38 + 0x50) + 0x1044) = (uint32_t)((uint32_t)(0xC000009AULL));
    goto loc_0087C83F;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0087C700&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
