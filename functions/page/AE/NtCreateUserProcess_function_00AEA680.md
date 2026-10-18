# NtCreateUserProcess

- RVA: `0x00AEA680`–`0x00AEB86F` (길이 `4,591` bytes)
- VA: `0x0000000140AEA680`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CEFF8`
- 디코드: `1,043`개 명령, `4,591/4,591` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **83**; 고유 호출 대상: **59**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x00AEA752` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AEA793` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AEA826` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AEA8F6` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AEA910` → [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) (function, `0x009ED6E0`)
- `0x00AEA98A` → [PspCaptureCreateInfo](../A4/PspCaptureCreateInfo_function_00A4A9B0.md) (function, `0x00A4A9B0`)
- `0x00AEA9D8` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AEAA09` → [PspEstimateNewProcessServerSilo](../A5/PspEstimateNewProcessServerSilo_function_00A5F7E4.md) (function, `0x00A5F7E4`)
- `0x00AEAA52` → [PspReferenceTokenForNewProcess](../A1/PspReferenceTokenForNewProcess_function_00A12D58.md) (function, `0x00A12D58`)
- `0x00AEAA7D` → [SeQueryServerSiloToken](../91/SeQueryServerSiloToken_function_00912F30.md) (function, `0x00912F30`)
- `0x00AEAA91` → [PspIsSiloInSilo](../A6/PspIsSiloInSilo_function_00A6EC8C.md) (function, `0x00A6EC8C`)
- `0x00AEAAFA` → [ZwSystemDebugControl](../../text/6B/ZwSystemDebugControl_function_006B0AF0.md) (function, `0x006B0AF0`)
- `0x00AEAB10` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AEAB59` → [SeQuerySigningPolicy](../A1/SeQuerySigningPolicy_function_00A12F44.md) (function, `0x00A12F44`)
- `0x00AEAB77` → [SeCompareSigningLevels](../A1/SeCompareSigningLevels_function_00A13760.md) (function, `0x00A13760`)
- `0x00AEABE6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AEAC16` → [PspGetMemoryPartitionContext](../87/PspGetMemoryPartitionContext_function_0087D808.md) (function, `0x0087D808`)
- `0x00AEAC33` → [PspCreateUserProcessEcp](../8A/PspCreateUserProcessEcp_function_008A2288.md) (function, `0x008A2288`)
- `0x00AEACA7` → [IoCreateFileEx](../8A/IoCreateFileEx_function_008AB000.md) (function, `0x008AB000`)
- `0x00AEAD18` → [IoCreateFileEx](../8A/IoCreateFileEx_function_008AB000.md) (function, `0x008AB000`)
- `0x00AEAD37` → [PspUpdateCreateInfo](PspUpdateCreateInfo_function_00AEC060.md) (function, `0x00AEC060`)
- `0x00AEAD69` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00AEADA4` → [Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline_function_004F4150.md) (function, `0x004F4150`)
- `0x00AEADE0` → [SeDuplicateTokenWithPredictedClaims](../6F/SeDuplicateTokenWithPredictedClaims_function_006FD084.md) (function, `0x006FD084`)
- `0x00AEAE38` → [PsDisableImpersonation](../9E/PsDisableImpersonation_function_009E89B0.md) (function, `0x009E89B0`)
- `0x00AEAE4A` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AEAE6C` → [PsRestoreImpersonation](../9E/PsRestoreImpersonation_function_009E6F10.md) (function, `0x009E6F10`)
- `0x00AEAE8B` → [PsRestoreImpersonation](../9E/PsRestoreImpersonation_function_009E6F10.md) (function, `0x009E6F10`)
- `0x00AEAEB8` → [SeDuplicateTokenAndAddOriginClaim](../AC/SeDuplicateTokenAndAddOriginClaim_function_00AC6DF4.md) (function, `0x00AC6DF4`)
- `0x00AEAF12` → [MmCreateSpecialImageSection](../AB/MmCreateSpecialImageSection_function_00AB7360.md) (function, `0x00AB7360`)
- `0x00AEAF46` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00AEAF69` → [PspGetProcessProtectionRequirementsFromImage](../A6/PspGetProcessProtectionRequirementsFromImage_function_00A6DCF4.md) (function, `0x00A6DCF4`)
- `0x00AEAFB1` → [SeQuerySigningPolicy](../A1/SeQuerySigningPolicy_function_00A12F44.md) (function, `0x00A12F44`)
- `0x00AEAFE5` → [SeCompareSigningLevels](../A1/SeCompareSigningLevels_function_00A13760.md) (function, `0x00A13760`)
- `0x00AEAFFB` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x00AEB007` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AEB045` → [MmCreateSpecialImageSection](../AB/MmCreateSpecialImageSection_function_00AB7360.md) (function, `0x00AB7360`)
- `0x00AEB076` → [PspValidateCreateProcessProtection](../AA/PspValidateCreateProcessProtection_function_00AA2AD8.md) (function, `0x00AA2AD8`)
- `0x00AEB0A5` → [PspCheckForInvalidAccessByProtection](../A1/PspCheckForInvalidAccessByProtection_function_00A10098.md) (function, `0x00A10098`)
- `0x00AEB0C3` → [PspGetProcessParameterOverrides](../A6/PspGetProcessParameterOverrides_function_00A66A50.md) (function, `0x00A66A50`)
- `0x00AEB0D6` → [PspCaptureProcessParameters](../9E/PspCaptureProcessParameters_function_009E6350.md) (function, `0x009E6350`)
- `0x00AEB1BB` → [PspValidateCreateProcessProtection](../AA/PspValidateCreateProcessProtection_function_00AA2AD8.md) (function, `0x00AA2AD8`)
- `0x00AEB246` → [PspAllocateProcess](../A1/PspAllocateProcess_function_00A13B3C.md) (function, `0x00A13B3C`)
- `0x00AEB2A0` → [RtlGetExtendedContextLength2](../../text/49/RtlGetExtendedContextLength2_function_00493FE0.md) (function, `0x00493FE0`)
- `0x00AEB2CE` → [_chkstk](../../text/6B/_chkstk_function_006BA960.md) (function, `0x006BA960`)
- `0x00AEB2E7` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AEB2FF` → [RtlInitializeExtendedContext2](../../text/2F/RtlInitializeExtendedContext2_function_002F5D40.md) (function, `0x002F5D40`)
- `0x00AEB341` → [PspCreateUserContext](../A2/PspCreateUserContext_function_00A22520.md) (function, `0x00A22520`)
- `0x00AEB35A` → [PspGetContextThreadInternal](../8D/PspGetContextThreadInternal_function_008D4770.md) (function, `0x008D4770`)
- `0x00AEB36D` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (function, `0x004601C0`)
- `0x00AEB378` → [PspRundownSingleProcess](../90/PspRundownSingleProcess_function_00906D50.md) (function, `0x00906D50`)
- `0x00AEB3AB` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00AEB3F5` → [PspMapThreadCreationFlags](../A2/PspMapThreadCreationFlags_function_00A26D08.md) (function, `0x00A26D08`)
- `0x00AEB47C` → [PspAllocateThread](../9E/PspAllocateThread_function_009EF72C.md) (function, `0x009EF72C`)
- `0x00AEB48F` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (function, `0x004601C0`)
- `0x00AEB49A` → [PspRundownSingleProcess](../90/PspRundownSingleProcess_function_00906D50.md) (function, `0x00906D50`)
- `0x00AEB4B6` → [PsTestProtectedProcessIncompatibility](../A1/PsTestProtectedProcessIncompatibility_function_00A1003C.md) (function, `0x00A1003C`)
- `0x00AEB4C3` → [Feature_ID51912085__private_IsEnabledPreCheck](../../text/46/Feature_ID51912085__private_IsEnabledPreCheck_function_00467684.md) (function, `0x00467684`)
- `0x00AEB54F` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x00AEB563` → [SeAdjustAntiTamperCreatorAccess](../../text/60/SeAdjustAntiTamperCreatorAccess_function_00607590.md) (function, `0x00607590`)
- `0x00AEB576` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (function, `0x004601C0`)
- `0x00AEB581` → [PspRundownSingleProcess](../90/PspRundownSingleProcess_function_00906D50.md) (function, `0x00906D50`)
- `0x00AEB59A` → [SeAdjustAntiTamperCreatorAccess](../../text/60/SeAdjustAntiTamperCreatorAccess_function_00607590.md) (function, `0x00607590`)
- `0x00AEB5ED` → [PspInsertProcess](../94/PspInsertProcess_function_009472CC.md) (function, `0x009472CC`)
- `0x00AEB648` → [PspInsertThread](../9F/PspInsertThread_function_009F0314.md) (function, `0x009F0314`)
- `0x00AEB653` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x00AEB662` → [PspRundownSingleProcess](../90/PspRundownSingleProcess_function_00906D50.md) (function, `0x00906D50`)
- `0x00AEB676` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (function, `0x0044BEE0`)
- `0x00AEB694` → [SeDeleteAccessState](../8C/SeDeleteAccessState_function_008C5F70.md) (function, `0x008C5F70`)
- `0x00AEB6A3` → [PsTerminateProcess](../90/PsTerminateProcess_function_00904C64.md) (function, `0x00904C64`)
- `0x00AEB6AC` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AEB6BA` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AEB6D6` → [PspCreateObjectHandle](../A1/PspCreateObjectHandle_function_00A1E51C.md) (function, `0x00A1E51C`)
- `0x00AEB762` → [PspUpdateCreateInfo](PspUpdateCreateInfo_function_00AEC060.md) (function, `0x00AEC060`)
- `0x00AEB796` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x00AEB7D2` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x00AEB7FD` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AEB809` → [PspDeleteMemoryPartitionContext](../A8/PspDeleteMemoryPartitionContext_function_00A85D50.md) (function, `0x00A85D50`)
- `0x00AEB815` → [PspDeleteCreateProcessContext](../9E/PspDeleteCreateProcessContext_function_009EF4C4.md) (function, `0x009EF4C4`)
- `0x00AEB826` → [FsRtlFreeExtraCreateParameterList](../8A/FsRtlFreeExtraCreateParameterList_function_008A1420.md) (function, `0x008A1420`)
- `0x00AEB834` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AEB84E` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00AEB868` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00AEA69C` → RVA `0x00E0A740` (`.data`; read)
- `0x00AEA9A8` → RVA `0x00FC6A98` (`ALMOSTRO`; read)
- `0x00AEAAC4` → RVA `0x00FC42C0` (`.data`; read)
- `0x00AEAB09` → RVA `0x00FD9AD0` (`PAGEDATA`; read)
- `0x00AEABD3` → RVA `0x00FD83D0` (`PAGEDATA`; read)
- `0x00AEAD41` → RVA `0x00FC6AE0` (`ALMOSTRO`; read)
- `0x00AEAE43` → RVA `0x00FD9A78` (`PAGEDATA`; read)
- `0x00AEAF21` → RVA `0x00FC6BD8` (`ALMOSTRO`; read)
- `0x00AEB334` → RVA `0x00FC7480` (`ALMOSTRO`; read)
- `0x00AEB4CE` → RVA `0x00B4C270` (`RtlProtectedAccess2`; read)
- `0x00AEB7F1` → RVA `0x00F04F10` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **27**
  - `0x00AEA752` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AEA793` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AEA826` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AEA8F6` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AEAAFA` → [ZwSystemDebugControl](../../text/6B/ZwSystemDebugControl_function_006B0AF0.md) (`PAGE` → `.text`)
  - `0x00AEABE6` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AEADA4` → [Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline_function_004F4150.md) (`PAGE` → `.text`)
  - `0x00AEB007` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AEB2A0` → [RtlGetExtendedContextLength2](../../text/49/RtlGetExtendedContextLength2_function_00493FE0.md) (`PAGE` → `.text`)
  - `0x00AEB2CE` → [_chkstk](../../text/6B/_chkstk_function_006BA960.md) (`PAGE` → `.text`)
  - `0x00AEB2E7` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AEB2FF` → [RtlInitializeExtendedContext2](../../text/2F/RtlInitializeExtendedContext2_function_002F5D40.md) (`PAGE` → `.text`)
  - `0x00AEB36D` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (`PAGE` → `.text`)
  - `0x00AEB3AB` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x00AEB48F` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (`PAGE` → `.text`)
  - `0x00AEB4C3` → [Feature_ID51912085__private_IsEnabledPreCheck](../../text/46/Feature_ID51912085__private_IsEnabledPreCheck_function_00467684.md) (`PAGE` → `.text`)
  - `0x00AEB54F` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (`PAGE` → `.text`)
  - `0x00AEB563` → [SeAdjustAntiTamperCreatorAccess](../../text/60/SeAdjustAntiTamperCreatorAccess_function_00607590.md) (`PAGE` → `.text`)
  - `0x00AEB576` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (`PAGE` → `.text`)
  - `0x00AEB59A` → [SeAdjustAntiTamperCreatorAccess](../../text/60/SeAdjustAntiTamperCreatorAccess_function_00607590.md) (`PAGE` → `.text`)
  - `0x00AEB653` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x00AEB676` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (`PAGE` → `.text`)
  - `0x00AEB6AC` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AEB6BA` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AEB7FD` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AEB834` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AEB84E` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AEA680  40 55                           push rbp
00AEA682  53                              push rbx
00AEA683  56                              push rsi
00AEA684  57                              push rdi
00AEA685  41 54                           push r12
00AEA687  41 55                           push r13
00AEA689  41 56                           push r14
00AEA68B  41 57                           push r15
00AEA68D  48 81 EC E8 07 00 00            sub rsp, 0x7e8
00AEA694  48 8D AC 24 80 00 00 00         lea rbp, [rsp + 0x80]
00AEA69C  48 8B 05 9D 00 32 00            mov rax, qword ptr [rip + 0x32009d]
00AEA6A3  48 33 C5                        xor rax, rbp
00AEA6A6  48 89 85 50 07 00 00            mov qword ptr [rbp + 0x750], rax
00AEA6AD  48 89 95 90 00 00 00            mov qword ptr [rbp + 0x90], rdx
00AEA6B4  48 89 8D 98 00 00 00            mov qword ptr [rbp + 0x98], rcx
00AEA6BB  4C 8B A5 D0 07 00 00            mov r12, qword ptr [rbp + 0x7d0]
00AEA6C2  4C 89 A5 88 00 00 00            mov qword ptr [rbp + 0x88], r12
00AEA6C9  44 89 45 28                     mov dword ptr [rbp + 0x28], r8d
00AEA6CD  44 89 4D 30                     mov dword ptr [rbp + 0x30], r9d
00AEA6D1  48 8B 85 D8 07 00 00            mov rax, qword ptr [rbp + 0x7d8]
00AEA6D8  48 89 85 D8 00 00 00            mov qword ptr [rbp + 0xd8], rax
00AEA6DF  48 8B 85 F0 07 00 00            mov rax, qword ptr [rbp + 0x7f0]
00AEA6E6  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
00AEA6EA  4C 8B B5 F8 07 00 00            mov r14, qword ptr [rbp + 0x7f8]
00AEA6F1  48 8B B5 00 08 00 00            mov rsi, qword ptr [rbp + 0x800]
00AEA6F8  33 FF                           xor edi, edi
00AEA6FA  66 89 7D 20                     mov word ptr [rbp + 0x20], di
00AEA6FE  89 7D 18                        mov dword ptr [rbp + 0x18], edi
00AEA701  33 C0                           xor eax, eax
00AEA703  89 85 FA 00 00 00               mov dword ptr [rbp + 0xfa], eax
00AEA709  66 89 85 FE 00 00 00            mov word ptr [rbp + 0xfe], ax
00AEA710  0F 57 C0                        xorps xmm0, xmm0
00AEA713  0F 11 85 30 01 00 00            movups xmmword ptr [rbp + 0x130], xmm0
00AEA71A  48 89 7D 10                     mov qword ptr [rbp + 0x10], rdi
00AEA71E  48 89 7D 78                     mov qword ptr [rbp + 0x78], rdi
00AEA722  0F 11 85 A0 00 00 00            movups xmmword ptr [rbp + 0xa0], xmm0
00AEA729  0F 11 85 B0 00 00 00            movups xmmword ptr [rbp + 0xb0], xmm0
00AEA730  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
00AEA737  89 85 C8 00 00 00               mov dword ptr [rbp + 0xc8], eax
00AEA73D  48 89 7D 60                     mov qword ptr [rbp + 0x60], rdi
00AEA741  BB 90 01 00 00                  mov ebx, 0x190
00AEA746  44 8B C3                        mov r8d, ebx
00AEA749  33 D2                           xor edx, edx
00AEA74B  48 8D 8D 10 04 00 00            lea rcx, [rbp + 0x410]
00AEA752  E8 E9 C4 BD FF                  call 0x1406c6c40
00AEA757  0F 57 C0                        xorps xmm0, xmm0
00AEA75A  0F 11 85 20 01 00 00            movups xmmword ptr [rbp + 0x120], xmm0
00AEA761  40 88 7D 0A                     mov byte ptr [rbp + 0xa], dil
00AEA765  40 88 7D 04                     mov byte ptr [rbp + 4], dil
00AEA769  40 88 7D 09                     mov byte ptr [rbp + 9], dil
00AEA76D  40 88 7D 05                     mov byte ptr [rbp + 5], dil
00AEA771  33 C0                           xor eax, eax
00AEA773  0F 11 85 30 07 00 00            movups xmmword ptr [rbp + 0x730], xmm0
00AEA77A  48 89 85 40 07 00 00            mov qword ptr [rbp + 0x740], rax
00AEA781  88 85 48 07 00 00               mov byte ptr [rbp + 0x748], al
00AEA787  44 8B C3                        mov r8d, ebx
00AEA78A  33 D2                           xor edx, edx
00AEA78C  48 8D 8D A0 05 00 00            lea rcx, [rbp + 0x5a0]
00AEA793  E8 A8 C4 BD FF                  call 0x1406c6c40
00AEA798  48 89 BD D0 00 00 00            mov qword ptr [rbp + 0xd0], rdi
00AEA79F  89 7D 38                        mov dword ptr [rbp + 0x38], edi
00AEA7A2  48 89 7D 40                     mov qword ptr [rbp + 0x40], rdi
00AEA7A6  0F 57 C0                        xorps xmm0, xmm0
00AEA7A9  33 C0                           xor eax, eax
00AEA7AB  0F 11 85 40 01 00 00            movups xmmword ptr [rbp + 0x140], xmm0
00AEA7B2  48 89 85 50 01 00 00            mov qword ptr [rbp + 0x150], rax
00AEA7B9  0F 11 85 E8 00 00 00            movups xmmword ptr [rbp + 0xe8], xmm0
00AEA7C0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AEA7C9  48 89 45 68                     mov qword ptr [rbp + 0x68], rax
00AEA7CD  48 8B 98 B8 00 00 00            mov rbx, qword ptr [rax + 0xb8]
00AEA7D4  48 89 5D 48                     mov qword ptr [rbp + 0x48], rbx
00AEA7D8  48 89 9D E0 00 00 00            mov qword ptr [rbp + 0xe0], rbx
00AEA7DF  44 8A B8 32 02 00 00            mov r15b, byte ptr [rax + 0x232]
00AEA7E6  44 88 7D 1C                     mov byte ptr [rbp + 0x1c], r15b
00AEA7EA  48 89 BD 80 00 00 00            mov qword ptr [rbp + 0x80], rdi
00AEA7F1  48 89 7D 50                     mov qword ptr [rbp + 0x50], rdi
00AEA7F5  40 8A C7                        mov al, dil
00AEA7F8  89 45 00                        mov dword ptr [rbp], eax
00AEA7FB  88 45 08                        mov byte ptr [rbp + 8], al
00AEA7FE  40 88 7D 07                     mov byte ptr [rbp + 7], dil
00AEA802  33 C0                           xor eax, eax
00AEA804  0F 11 85 F8 00 00 00            movups xmmword ptr [rbp + 0xf8], xmm0
00AEA80B  0F 11 85 08 01 00 00            movups xmmword ptr [rbp + 0x108], xmm0
00AEA812  48 89 85 18 01 00 00            mov qword ptr [rbp + 0x118], rax
00AEA819  33 D2                           xor edx, edx
00AEA81B  44 8D 47 48                     lea r8d, [rdi + 0x48]
00AEA81F  48 8D 8D 60 01 00 00            lea rcx, [rbp + 0x160]
00AEA826  E8 15 C4 BD FF                  call 0x1406c6c40
00AEA82B  44 8B AD E0 07 00 00            mov r13d, dword ptr [rbp + 0x7e0]
00AEA832  41 F7 C5 38 78 31 FF            test r13d, 0xff317838
00AEA839  0F 85 00 10 00 00               jne 0x140aeb83f
00AEA83F  F7 85 E8 07 00 00 FE FF FF FF   test dword ptr [rbp + 0x7e8], 0xfffffffe
00AEA849  0F 85 F0 0F 00 00               jne 0x140aeb83f
00AEA84F  41 8B C5                        mov eax, r13d
00AEA852  B9 00 84 00 00                  mov ecx, 0x8400
00AEA857  23 C1                           and eax, ecx
00AEA859  3B C1                           cmp eax, ecx
00AEA85B  75 0A                           jne 0x140aea867
00AEA85D  B8 30 00 00 C0                  mov eax, 0xc0000030
00AEA862  E9 DD 0F 00 00                  jmp 0x140aeb844
00AEA867  44 88 BD 94 05 00 00            mov byte ptr [rbp + 0x594], r15b
00AEA86E  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
00AEA878  45 84 FF                        test r15b, r15b
00AEA87B  74 30                           je 0x140aea8ad
00AEA87D  48 8B CA                        mov rcx, rdx
00AEA880  48 39 95 98 00 00 00            cmp qword ptr [rbp + 0x98], rdx
00AEA887  48 0F 42 8D 98 00 00 00         cmovb rcx, qword ptr [rbp + 0x98]
00AEA88F  48 8B 01                        mov rax, qword ptr [rcx]
00AEA892  48 89 01                        mov qword ptr [rcx], rax
00AEA895  48 8B CA                        mov rcx, rdx
00AEA898  48 39 95 90 00 00 00            cmp qword ptr [rbp + 0x90], rdx
00AEA89F  48 0F 42 8D 90 00 00 00         cmovb rcx, qword ptr [rbp + 0x90]
00AEA8A7  48 8B 01                        mov rax, qword ptr [rcx]
00AEA8AA  48 89 01                        mov qword ptr [rcx], rax
00AEA8AD  4D 85 E4                        test r12, r12
00AEA8B0  74 35                           je 0x140aea8e7
00AEA8B2  45 84 FF                        test r15b, r15b
00AEA8B5  74 14                           je 0x140aea8cb
00AEA8B7  41 F6 C4 03                     test r12b, 3
00AEA8BB  0F 85 A7 0F 00 00               jne 0x140aeb868
00AEA8C1  4C 3B E2                        cmp r12, rdx
00AEA8C4  49 0F 42 D4                     cmovb rdx, r12
00AEA8C8  90                              nop
00AEA8C9  8A 02                           mov al, byte ptr [rdx]
00AEA8CB  41 8B 44 24 18                  mov eax, dword ptr [r12 + 0x18]
00AEA8D0  45 84 FF                        test r15b, r15b
00AEA8D3  75 07                           jne 0x140aea8dc
00AEA8D5  25 F2 1F 01 00                  and eax, 0x11ff2
00AEA8DA  EB 05                           jmp 0x140aea8e1
00AEA8DC  25 F2 1D 00 00                  and eax, 0x1df2
00AEA8E1  89 85 90 05 00 00               mov dword ptr [rbp + 0x590], eax
00AEA8E7  33 D2                           xor edx, edx
00AEA8E9  41 B8 60 02 00 00               mov r8d, 0x260
00AEA8EF  48 8D 8D B0 01 00 00            lea rcx, [rbp + 0x1b0]
00AEA8F6  E8 45 C3 BD FF                  call 0x1406c6c40
00AEA8FB  48 85 F6                        test rsi, rsi
00AEA8FE  74 28                           je 0x140aea928
00AEA900  4C 8D 8D B0 01 00 00            lea r9, [rbp + 0x1b0]
00AEA907  45 33 C0                        xor r8d, r8d
00AEA90A  41 8A D7                        mov dl, r15b
00AEA90D  48 8B CE                        mov rcx, rsi
00AEA910  E8 CB 2D F0 FF                  call 0x1409ed6e0
00AEA915  85 C0                           test eax, eax
00AEA917  0F 88 27 0F 00 00               js 0x140aeb844
00AEA91D  48 39 BD 18 03 00 00            cmp qword ptr [rbp + 0x318], rdi
00AEA924  0F 95 45 07                     setne byte ptr [rbp + 7]
00AEA928  41 BC 00 00 02 00               mov r12d, 0x20000
00AEA92E  41 F6 C5 40                     test r13b, 0x40
00AEA932  74 1F                           je 0x140aea953
00AEA934  4C 85 A5 B8 01 00 00            test qword ptr [rbp + 0x1b8], r12
00AEA93B  74 16                           je 0x140aea953
00AEA93D  40 38 BD B1 01 00 00            cmp byte ptr [rbp + 0x1b1], dil
00AEA944  75 0D                           jne 0x140aea953
00AEA946  41 83 E5 BF                     and r13d, 0xffffffbf
00AEA94A  48 0F BA B5 B8 01 00 00 11      btr qword ptr [rbp + 0x1b8], 0x11
00AEA953  41 F6 C5 04                     test r13b, 4
00AEA957  75 11                           jne 0x140aea96a
00AEA959  48 F7 85 B8 01 00 00 00 08 00 00  test qword ptr [rbp + 0x1b8], 0x800
00AEA964  0F 85 72 0E 00 00               jne 0x140aeb7dc
00AEA96A  4C 85 A5 B8 01 00 00            test qword ptr [rbp + 0x1b8], r12
00AEA971  74 0A                           je 0x140aea97d
00AEA973  41 F6 C5 40                     test r13b, 0x40
00AEA977  0F 84 5F 0E 00 00               je 0x140aeb7dc
00AEA97D  4C 8D 85 B0 01 00 00            lea r8, [rbp + 0x1b0]
00AEA984  49 8B D6                        mov rdx, r14
00AEA987  41 8A CF                        mov cl, r15b
00AEA98A  E8 21 00 F6 FF                  call 0x140a4a9b0
00AEA98F  8B F0                           mov esi, eax
00AEA991  85 C0                           test eax, eax
00AEA993  0F 88 48 0E 00 00               js 0x140aeb7e1
00AEA999  41 BE 01 00 00 00               mov r14d, 1
00AEA99F  44 84 B5 B8 01 00 00            test byte ptr [rbp + 0x1b8], r14b
00AEA9A6  74 4C                           je 0x140aea9f4
00AEA9A8  4C 8B 05 E9 C0 4D 00            mov r8, qword ptr [rip + 0x4dc0e9]
00AEA9AF  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AEA9B4  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AEA9B9  48 8D 45 60                     lea rax, [rbp + 0x60]
00AEA9BD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEA9C2  C7 44 24 20 50 73 43 72         mov dword ptr [rsp + 0x20], 0x72437350
00AEA9CA  45 8A CF                        mov r9b, r15b
00AEA9CD  41 8D 56 7F                     lea edx, [r14 + 0x7f]
00AEA9D1  48 8B 8D 30 02 00 00            mov rcx, qword ptr [rbp + 0x230]
00AEA9D8  E8 73 EC D7 FF                  call 0x140869650
00AEA9DD  8B F0                           mov esi, eax
00AEA9DF  85 C0                           test eax, eax
00AEA9E1  0F 88 FA 0D 00 00               js 0x140aeb7e1
00AEA9E7  48 8B 5D 60                     mov rbx, qword ptr [rbp + 0x60]
00AEA9EB  48 89 9D 38 02 00 00            mov qword ptr [rbp + 0x238], rbx
00AEA9F2  EB 04                           jmp 0x140aea9f8
00AEA9F4  48 89 5D 60                     mov qword ptr [rbp + 0x60], rbx
00AEA9F8  44 8B 85 2C 03 00 00            mov r8d, dword ptr [rbp + 0x32c]
00AEA9FF  48 8B 95 20 03 00 00            mov rdx, qword ptr [rbp + 0x320]
00AEAA06  48 8B CB                        mov rcx, rbx
00AEAA09  E8 D6 4D F7 FF                  call 0x140a5f7e4
00AEAA0E  48 89 85 58 03 00 00            mov qword ptr [rbp + 0x358], rax
00AEAA15  8A 85 C1 01 00 00               mov al, byte ptr [rbp + 0x1c1]
00AEAA1B  24 0C                           and al, 0xc
00AEAA1D  3C 04                           cmp al, 4
00AEAA1F  75 1D                           jne 0x140aeaa3e
00AEAA21  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
00AEAA25  48 3B D8                        cmp rbx, rax
00AEAA28  0F 85 AE 0D 00 00               jne 0x140aeb7dc
00AEAA2E  F7 80 FC 05 00 00 00 10 00 00   test dword ptr [rax + 0x5fc], 0x1000
00AEAA38  0F 85 9E 0D 00 00               jne 0x140aeb7dc
00AEAA3E  4C 8D 8D 50 02 00 00            lea r9, [rbp + 0x250]
00AEAA45  45 8A C7                        mov r8b, r15b
00AEAA48  48 8B 95 48 02 00 00            mov rdx, qword ptr [rbp + 0x248]
00AEAA4F  48 8B CB                        mov rcx, rbx
00AEAA52  E8 01 83 F2 FF                  call 0x140a12d58
00AEAA57  8B F0                           mov esi, eax
00AEAA59  85 C0                           test eax, eax
00AEAA5B  79 0C                           jns 0x140aeaa69
00AEAA5D  48 89 BD 50 02 00 00            mov qword ptr [rbp + 0x250], rdi
00AEAA64  E9 78 0D 00 00                  jmp 0x140aeb7e1
00AEAA69  48 39 BD 48 02 00 00            cmp qword ptr [rbp + 0x248], rdi
00AEAA70  74 2C                           je 0x140aeaa9e
00AEAA72  48 8D 55 40                     lea rdx, [rbp + 0x40]
00AEAA76  48 8B 8D 50 02 00 00            mov rcx, qword ptr [rbp + 0x250]
00AEAA7D  E8 AE 84 E2 FF                  call 0x140912f30
00AEAA82  85 C0                           test eax, eax
00AEAA84  78 18                           js 0x140aeaa9e
00AEAA86  48 8B 95 58 03 00 00            mov rdx, qword ptr [rbp + 0x358]
00AEAA8D  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00AEAA91  E8 F6 41 F8 FF                  call 0x140a6ec8c
00AEAA96  84 C0                           test al, al
00AEAA98  0F 84 3E 0D 00 00               je 0x140aeb7dc
00AEAA9E  8A 85 B8 01 00 00               mov al, byte ptr [rbp + 0x1b8]
00AEAAA4  A8 20                           test al, 0x20
00AEAAA6  0F 84 74 06 00 00               je 0x140aeb120
00AEAAAC  48 8B 85 B8 01 00 00            mov rax, qword ptr [rbp + 0x1b8]
00AEAAB3  49 23 C4                        and rax, r12
00AEAAB6  48 F7 D8                        neg rax
00AEAAB9  1A DB                           sbb bl, bl
00AEAABB  22 9D B1 01 00 00               and bl, byte ptr [rbp + 0x1b1]
00AEAAC1  88 5D 06                        mov byte ptr [rbp + 6], bl
00AEAAC4  F7 05 F2 97 4D 00 00 00 04 00   test dword ptr [rip + 0x4d97f2], 0x40000
00AEAACE  74 2F                           je 0x140aeaaff
00AEAAD0  0F 10 85 A0 02 00 00            movups xmm0, xmmword ptr [rbp + 0x2a0]
00AEAAD7  F3 0F 7F 85 20 01 00 00         movdqu xmmword ptr [rbp + 0x120], xmm0
00AEAADF  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00AEAAE4  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00AEAAE8  45 33 C9                        xor r9d, r9d
00AEAAEB  45 8D 41 10                     lea r8d, [r9 + 0x10]
00AEAAEF  48 8D 95 20 01 00 00            lea rdx, [rbp + 0x120]
00AEAAF6  41 8D 49 26                     lea ecx, [r9 + 0x26]
00AEAAFA  E8 F1 5F BC FF                  call 0x1406b0af0
00AEAAFF  41 0F BA E5 16                  bt r13d, 0x16
00AEAB04  73 1D                           jae 0x140aeab23
00AEAB06  41 8A D7                        mov dl, r15b
00AEAB09  48 8B 0D C0 EF 4E 00            mov rcx, qword ptr [rip + 0x4eefc0]
00AEAB10  E8 0B 73 D8 FF                  call 0x140871e20
00AEAB15  84 C0                           test al, al
00AEAB17  75 0A                           jne 0x140aeab23
00AEAB19  BE 61 00 00 C0                  mov esi, 0xc0000061
00AEAB1E  E9 BE 0C 00 00                  jmp 0x140aeb7e1
00AEAB23  45 8B C5                        mov r8d, r13d
00AEAB26  41 C1 E8 06                     shr r8d, 6
00AEAB2A  45 23 C6                        and r8d, r14d
00AEAB2D  48 8D 45 06                     lea rax, [rbp + 6]
00AEAB31  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEAB36  48 8D 45 09                     lea rax, [rbp + 9]
00AEAB3A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEAB3F  48 8D 45 04                     lea rax, [rbp + 4]
00AEAB43  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEAB48  44 8A CB                        mov r9b, bl
00AEAB4B  48 8D 95 A0 02 00 00            lea rdx, [rbp + 0x2a0]
00AEAB52  48 8B 8D 50 02 00 00            mov rcx, qword ptr [rbp + 0x250]
00AEAB59  E8 E6 83 F2 FF                  call 0x140a12f44
00AEAB5E  8B F0                           mov esi, eax
00AEAB60  85 C0                           test eax, eax
00AEAB62  0F 88 79 0C 00 00               js 0x140aeb7e1
00AEAB68  BB 08 00 00 00                  mov ebx, 8
00AEAB6D  45 85 EC                        test r12d, r13d
00AEAB70  74 1B                           je 0x140aeab8d
00AEAB72  8A D3                           mov dl, bl
00AEAB74  8A 4D 04                        mov cl, byte ptr [rbp + 4]
00AEAB77  E8 E4 8B F2 FF                  call 0x140a13760
00AEAB7C  44 0F B6 65 04                  movzx r12d, byte ptr [rbp + 4]
00AEAB81  85 C0                           test eax, eax
00AEAB83  44 0F 44 E3                     cmove r12d, ebx
00AEAB87  44 88 65 04                     mov byte ptr [rbp + 4], r12b
00AEAB8B  EB 04                           jmp 0x140aeab91
00AEAB8D  44 8A 65 04                     mov r12b, byte ptr [rbp + 4]
00AEAB91  C7 85 A0 00 00 00 30 00 00 00   mov dword ptr [rbp + 0xa0], 0x30
00AEAB9B  48 89 BD A8 00 00 00            mov qword ptr [rbp + 0xa8], rdi
00AEABA2  B8 40 06 00 00                  mov eax, 0x640
00AEABA7  B9 40 02 00 00                  mov ecx, 0x240
00AEABAC  45 3A FE                        cmp r15b, r14b
00AEABAF  0F 45 C1                        cmovne eax, ecx
00AEABB2  89 85 B8 00 00 00               mov dword ptr [rbp + 0xb8], eax
00AEABB8  48 8D 85 A0 02 00 00            lea rax, [rbp + 0x2a0]
00AEABBF  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
00AEABC6  0F 57 C0                        xorps xmm0, xmm0
00AEABC9  F3 0F 7F 85 C0 00 00 00         movdqu xmmword ptr [rbp + 0xc0], xmm0
00AEABD1  8B F7                           mov esi, edi
00AEABD3  48 8B 05 F6 D7 4E 00            mov rax, qword ptr [rip + 0x4ed7f6]
00AEABDA  48 85 C0                        test rax, rax
00AEABDD  74 0E                           je 0x140aeabed
00AEABDF  48 8B 8D 50 02 00 00            mov rcx, qword ptr [rbp + 0x250]
00AEABE6  E8 E5 FE BC FF                  call 0x1406baad0
00AEABEB  8B F0                           mov esi, eax
00AEABED  85 F6                           test esi, esi
00AEABEF  0F 88 EC 0B 00 00               js 0x140aeb7e1
00AEABF5  44 8B 8D 2C 03 00 00            mov r9d, dword ptr [rbp + 0x32c]
00AEABFC  48 8D 85 80 00 00 00            lea rax, [rbp + 0x80]
00AEAC03  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEAC08  4C 8B 85 20 03 00 00            mov r8, qword ptr [rbp + 0x320]
00AEAC0F  41 8B D5                        mov edx, r13d
00AEAC12  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
00AEAC16  E8 ED 2B D9 FF                  call 0x14087d808
00AEAC1B  8B F0                           mov esi, eax
00AEAC1D  85 C0                           test eax, eax
00AEAC1F  0F 88 BC 0B 00 00               js 0x140aeb7e1
00AEAC25  48 8B 95 50 02 00 00            mov rdx, qword ptr [rbp + 0x250]
00AEAC2C  48 8D 8D F8 00 00 00            lea rcx, [rbp + 0xf8]
00AEAC33  E8 50 76 DB FF                  call 0x1408a2288
00AEAC38  8B F0                           mov esi, eax
00AEAC3A  85 C0                           test eax, eax
00AEAC3C  0F 88 9F 0B 00 00               js 0x140aeb7e1
00AEAC42  8B 95 5C 02 00 00               mov edx, dword ptr [rbp + 0x25c]
00AEAC48  81 CA 20 00 10 00               or edx, 0x100020
00AEAC4E  48 8D 85 F8 00 00 00            lea rax, [rbp + 0xf8]
00AEAC55  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00AEAC5A  89 7C 24 68                     mov dword ptr [rsp + 0x68], edi
00AEAC5E  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
00AEAC63  89 7C 24 58                     mov dword ptr [rsp + 0x58], edi
00AEAC67  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00AEAC6B  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00AEAC70  C7 44 24 40 60 00 00 00         mov dword ptr [rsp + 0x40], 0x60
00AEAC78  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
00AEAC7D  C7 44 24 30 05 00 00 00         mov dword ptr [rsp + 0x30], 5
00AEAC85  C7 44 24 28 80 00 00 00         mov dword ptr [rsp + 0x28], 0x80
00AEAC8D  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00AEAC92  4C 8D 8D 30 01 00 00            lea r9, [rbp + 0x130]
00AEAC99  4C 8D 85 A0 00 00 00            lea r8, [rbp + 0xa0]
00AEACA0  48 8D 8D 60 02 00 00            lea rcx, [rbp + 0x260]
00AEACA7  E8 54 03 DC FF                  call 0x1408ab000
00AEACAC  8B F0                           mov esi, eax
00AEACAE  85 C0                           test eax, eax
00AEACB0  79 6D                           jns 0x140aead1f
00AEACB2  39 BD 5C 02 00 00               cmp dword ptr [rbp + 0x25c], edi
00AEACB8  74 65                           je 0x140aead1f
00AEACBA  48 8D 85 F8 00 00 00            lea rax, [rbp + 0xf8]
00AEACC1  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00AEACC6  89 7C 24 68                     mov dword ptr [rsp + 0x68], edi
00AEACCA  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
00AEACCF  89 7C 24 58                     mov dword ptr [rsp + 0x58], edi
00AEACD3  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
00AEACD7  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00AEACDC  C7 44 24 40 60 00 00 00         mov dword ptr [rsp + 0x40], 0x60
00AEACE4  44 89 74 24 38                  mov dword ptr [rsp + 0x38], r14d
00AEACE9  C7 44 24 30 05 00 00 00         mov dword ptr [rsp + 0x30], 5
00AEACF1  C7 44 24 28 80 00 00 00         mov dword ptr [rsp + 0x28], 0x80
00AEACF9  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00AEACFE  4C 8D 8D 30 01 00 00            lea r9, [rbp + 0x130]
00AEAD05  4C 8D 85 A0 00 00 00            lea r8, [rbp + 0xa0]
00AEAD0C  BA 20 00 10 00                  mov edx, 0x100020
00AEAD11  48 8D 8D 60 02 00 00            lea rcx, [rbp + 0x260]
00AEAD18  E8 E3 02 DC FF                  call 0x1408ab000
00AEAD1D  8B F0                           mov esi, eax
00AEAD1F  85 F6                           test esi, esi
00AEAD21  79 1E                           jns 0x140aead41
00AEAD23  48 89 BD 60 02 00 00            mov qword ptr [rbp + 0x260], rdi
00AEAD2A  41 8B CE                        mov ecx, r14d
00AEAD2D  48 8D 95 B0 01 00 00            lea rdx, [rbp + 0x1b0]
00AEAD34  45 33 C0                        xor r8d, r8d
00AEAD37  E8 24 13 00 00                  call 0x140aec060
00AEAD3C  E9 A0 0A 00 00                  jmp 0x140aeb7e1
00AEAD41  4C 8B 05 98 BD 4D 00            mov r8, qword ptr [rip + 0x4dbd98]
00AEAD48  48 89 7D 58                     mov qword ptr [rbp + 0x58], rdi
00AEAD4C  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00AEAD51  48 8D 45 58                     lea rax, [rbp + 0x58]
00AEAD55  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEAD5A  45 33 C9                        xor r9d, r9d
00AEAD5D  BA 20 00 10 00                  mov edx, 0x100020
00AEAD62  48 8B 8D 60 02 00 00            mov rcx, qword ptr [rbp + 0x260]
00AEAD69  E8 42 E0 D7 FF                  call 0x140868db0
00AEAD6E  8B F0                           mov esi, eax
00AEAD70  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00AEAD74  48 89 85 68 02 00 00            mov qword ptr [rbp + 0x268], rax
00AEAD7B  85 F6                           test esi, esi
00AEAD7D  79 10                           jns 0x140aead8f
00AEAD7F  48 89 BD 68 02 00 00            mov qword ptr [rbp + 0x268], rdi
00AEAD86  44 8B 7D 00                     mov r15d, dword ptr [rbp]
00AEAD8A  E9 73 0A 00 00                  jmp 0x140aeb802
00AEAD8F  48 89 BD B0 00 00 00            mov qword ptr [rbp + 0xb0], rdi
00AEAD96  0F B6 45 07                     movzx eax, byte ptr [rbp + 7]
00AEAD9A  8D 34 85 01 00 00 00            lea esi, [rax*4 + 1]
00AEADA1  89 75 40                        mov dword ptr [rbp + 0x40], esi
00AEADA4  E8 A7 93 A0 FF                  call 0x1404f4150
00AEADA9  85 C0                           test eax, eax
00AEADAB  0F 84 E9 00 00 00               je 0x140aeae9a
00AEADB1  48 8D 45 50                     lea rax, [rbp + 0x50]
00AEADB5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEADBA  8B 85 3C 03 00 00               mov eax, dword ptr [rbp + 0x33c]
00AEADC0  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00AEADC4  4C 8B 8D 40 03 00 00            mov r9, qword ptr [rbp + 0x340]
00AEADCB  44 8B 85 38 03 00 00            mov r8d, dword ptr [rbp + 0x338]
00AEADD2  48 8B 95 68 02 00 00            mov rdx, qword ptr [rbp + 0x268]
00AEADD9  48 8B 8D 50 02 00 00            mov rcx, qword ptr [rbp + 0x250]
00AEADE0  E8 9F 22 C1 FF                  call 0x1406fd084
00AEADE5  8B F0                           mov esi, eax
00AEADE7  85 C0                           test eax, eax
00AEADE9  0F 88 F2 09 00 00               js 0x140aeb7e1
00AEADEF  48 39 7D 50                     cmp qword ptr [rbp + 0x50], rdi
00AEADF3  74 0B                           je 0x140aeae00
00AEADF5  41 8A CE                        mov cl, r14b
00AEADF8  89 4D 00                        mov dword ptr [rbp], ecx
00AEADFB  88 4D 08                        mov byte ptr [rbp + 8], cl
00AEADFE  EB 14                           jmp 0x140aeae14
00AEAE00  40 8A C7                        mov al, dil
00AEAE03  89 45 00                        mov dword ptr [rbp], eax
00AEAE06  88 45 08                        mov byte ptr [rbp + 8], al
00AEAE09  48 8B 85 50 02 00 00            mov rax, qword ptr [rbp + 0x250]
00AEAE10  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
00AEAE14  8B 75 40                        mov esi, dword ptr [rbp + 0x40]
00AEAE17  8B C6                           mov eax, esi
00AEAE19  89 45 40                        mov dword ptr [rbp + 0x40], eax
00AEAE1C  84 9D 38 03 00 00               test byte ptr [rbp + 0x338], bl
00AEAE22  0F 84 C5 00 00 00               je 0x140aeaeed
00AEAE28  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00AEAE31  48 8D 95 E8 00 00 00            lea rdx, [rbp + 0xe8]
00AEAE38  E8 73 DB EF FF                  call 0x1409e89b0
00AEAE3D  44 8A E0                        mov r12b, al
00AEAE40  41 8A D7                        mov dl, r15b
00AEAE43  48 8B 0D 2E EC 4E 00            mov rcx, qword ptr [rip + 0x4eec2e]
00AEAE4A  E8 D1 6F D8 FF                  call 0x140871e20
00AEAE4F  84 C0                           test al, al
00AEAE51  75 23                           jne 0x140aeae76
00AEAE53  45 84 E4                        test r12b, r12b
00AEAE56  0F 84 BD FC FF FF               je 0x140aeab19
00AEAE5C  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00AEAE65  48 8D 95 E8 00 00 00            lea rdx, [rbp + 0xe8]
00AEAE6C  E8 9F C0 EF FF                  call 0x1409e6f10
00AEAE71  E9 A3 FC FF FF                  jmp 0x140aeab19
00AEAE76  45 84 E4                        test r12b, r12b
00AEAE79  74 15                           je 0x140aeae90
00AEAE7B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00AEAE84  48 8D 95 E8 00 00 00            lea rdx, [rbp + 0xe8]
00AEAE8B  E8 80 C0 EF FF                  call 0x1409e6f10
00AEAE90  8B C6                           mov eax, esi
00AEAE92  0B C3                           or eax, ebx
00AEAE94  44 8A 65 04                     mov r12b, byte ptr [rbp + 4]
00AEAE98  EB 50                           jmp 0x140aeaeea
00AEAE9A  48 8B 95 40 03 00 00            mov rdx, qword ptr [rbp + 0x340]
00AEAEA1  48 85 D2                        test rdx, rdx
00AEAEA4  74 2B                           je 0x140aeaed1
00AEAEA6  4C 8D 4D 50                     lea r9, [rbp + 0x50]
00AEAEAA  44 8B 85 3C 03 00 00            mov r8d, dword ptr [rbp + 0x33c]
00AEAEB1  48 8B 8D 50 02 00 00            mov rcx, qword ptr [rbp + 0x250]
00AEAEB8  E8 37 BF FD FF                  call 0x140ac6df4
00AEAEBD  8B 4D 00                        mov ecx, dword ptr [rbp]
00AEAEC0  0F B6 C9                        movzx ecx, cl
00AEAEC3  85 C0                           test eax, eax
00AEAEC5  41 0F 49 CE                     cmovns ecx, r14d
00AEAEC9  89 4D 00                        mov dword ptr [rbp], ecx
00AEAECC  88 4D 08                        mov byte ptr [rbp + 8], cl
00AEAECF  EB 03                           jmp 0x140aeaed4
00AEAED1  8B 4D 00                        mov ecx, dword ptr [rbp]
00AEAED4  8B C6                           mov eax, esi
00AEAED6  89 45 40                        mov dword ptr [rbp + 0x40], eax
00AEAED9  84 C9                           test cl, cl
00AEAEDB  75 10                           jne 0x140aeaeed
00AEAEDD  48 8B 85 50 02 00 00            mov rax, qword ptr [rbp + 0x250]
00AEAEE4  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
00AEAEE8  8B C6                           mov eax, esi
00AEAEEA  89 45 40                        mov dword ptr [rbp + 0x40], eax
00AEAEED  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00AEAEF1  48 8B 85 60 02 00 00            mov rax, qword ptr [rbp + 0x260]
00AEAEF8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEAEFD  45 8A CC                        mov r9b, r12b
00AEAF00  4C 8B 45 50                     mov r8, qword ptr [rbp + 0x50]
00AEAF04  48 8D 95 A0 00 00 00            lea rdx, [rbp + 0xa0]
00AEAF0B  48 8D 8D 70 02 00 00            lea rcx, [rbp + 0x270]
00AEAF12  E8 49 C4 FC FF                  call 0x140ab7360
00AEAF17  8B F0                           mov esi, eax
00AEAF19  85 C0                           test eax, eax
00AEAF1B  0F 88 EE 01 00 00               js 0x140aeb10f
00AEAF21  4C 8B 05 B0 BC 4D 00            mov r8, qword ptr [rip + 0x4dbcb0]
00AEAF28  48 89 7D 58                     mov qword ptr [rbp + 0x58], rdi
00AEAF2C  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00AEAF31  48 8D 45 58                     lea rax, [rbp + 0x58]
00AEAF35  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEAF3A  45 33 C9                        xor r9d, r9d
00AEAF3D  8B D3                           mov edx, ebx
00AEAF3F  48 8B 8D 70 02 00 00            mov rcx, qword ptr [rbp + 0x270]
00AEAF46  E8 65 DE D7 FF                  call 0x140868db0
00AEAF4B  8B F0                           mov esi, eax
00AEAF4D  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
00AEAF51  48 89 8D 80 02 00 00            mov qword ptr [rbp + 0x280], rcx
00AEAF58  85 C0                           test eax, eax
00AEAF5A  0F 88 A3 01 00 00               js 0x140aeb103
00AEAF60  4C 8D 45 0A                     lea r8, [rbp + 0xa]
00AEAF64  8A 5D 06                        mov bl, byte ptr [rbp + 6]
00AEAF67  8A D3                           mov dl, bl
00AEAF69  E8 86 2D F8 FF                  call 0x140a6dcf4
00AEAF6E  8B F0                           mov esi, eax
00AEAF70  85 C0                           test eax, eax
00AEAF72  0F 88 69 08 00 00               js 0x140aeb7e1
00AEAF78  44 8A 4D 0A                     mov r9b, byte ptr [rbp + 0xa]
00AEAF7C  44 3A CB                        cmp r9b, bl
00AEAF7F  0F 84 DC 00 00 00               je 0x140aeb061
00AEAF85  48 8D 45 06                     lea rax, [rbp + 6]
00AEAF89  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEAF8E  48 8D 45 09                     lea rax, [rbp + 9]
00AEAF92  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEAF97  48 8D 45 05                     lea rax, [rbp + 5]
00AEAF9B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEAFA0  45 8B C6                        mov r8d, r14d
00AEAFA3  48 8D 95 A0 02 00 00            lea rdx, [rbp + 0x2a0]
00AEAFAA  48 8B 8D 50 02 00 00            mov rcx, qword ptr [rbp + 0x250]
00AEAFB1  E8 8E 7F F2 FF                  call 0x140a12f44
00AEAFB6  8B F0                           mov esi, eax
00AEAFB8  85 C0                           test eax, eax
00AEAFBA  0F 88 21 08 00 00               js 0x140aeb7e1
00AEAFC0  8A 5D 05                        mov bl, byte ptr [rbp + 5]
00AEAFC3  41 3A DC                        cmp bl, r12b
00AEAFC6  0F 84 92 00 00 00               je 0x140aeb05e
00AEAFCC  41 8A CC                        mov cl, r12b
00AEAFCF  80 E1 30                        and cl, 0x30
00AEAFD2  74 0C                           je 0x140aeafe0
00AEAFD4  8A C3                           mov al, bl
00AEAFD6  24 30                           and al, 0x30
00AEAFD8  3A C1                           cmp al, cl
00AEAFDA  0F 85 FC 07 00 00               jne 0x140aeb7dc
00AEAFE0  41 8A D4                        mov dl, r12b
00AEAFE3  8A CB                           mov cl, bl
00AEAFE5  E8 76 87 F2 FF                  call 0x140a13760
00AEAFEA  85 C0                           test eax, eax
00AEAFEC  0F 84 EA 07 00 00               je 0x140aeb7dc
00AEAFF2  33 D2                           xor edx, edx
00AEAFF4  48 8B 8D 70 02 00 00            mov rcx, qword ptr [rbp + 0x270]
00AEAFFB  E8 70 68 DB FF                  call 0x1408a1870
00AEB000  48 8B 8D 80 02 00 00            mov rcx, qword ptr [rbp + 0x280]
00AEB007  E8 44 E3 80 FF                  call 0x1402f9350
00AEB00C  48 89 BD 70 02 00 00            mov qword ptr [rbp + 0x270], rdi
00AEB013  48 89 BD 80 02 00 00            mov qword ptr [rbp + 0x280], rdi
00AEB01A  44 8A E3                        mov r12b, bl
00AEB01D  8B 45 40                        mov eax, dword ptr [rbp + 0x40]
00AEB020  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00AEB024  48 8B 85 60 02 00 00            mov rax, qword ptr [rbp + 0x260]
00AEB02B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEB030  44 8A CB                        mov r9b, bl
00AEB033  4C 8B 45 50                     mov r8, qword ptr [rbp + 0x50]
00AEB037  48 8D 95 A0 00 00 00            lea rdx, [rbp + 0xa0]
00AEB03E  48 8D 8D 70 02 00 00            lea rcx, [rbp + 0x270]
00AEB045  E8 16 C3 FC FF                  call 0x140ab7360
00AEB04A  8B F0                           mov esi, eax
00AEB04C  85 C0                           test eax, eax
00AEB04E  0F 88 BB 00 00 00               js 0x140aeb10f
00AEB054  BB 08 00 00 00                  mov ebx, 8
00AEB059  E9 C3 FE FF FF                  jmp 0x140aeaf21
00AEB05E  8A 5D 06                        mov bl, byte ptr [rbp + 6]
00AEB061  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
00AEB065  45 8B CD                        mov r9d, r13d
00AEB068  45 8A C7                        mov r8b, r15b
00AEB06B  48 8D 95 B0 01 00 00            lea rdx, [rbp + 0x1b0]
00AEB072  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
00AEB076  E8 5D 7A FB FF                  call 0x140aa2ad8
00AEB07B  8B F0                           mov esi, eax
00AEB07D  85 C0                           test eax, eax
00AEB07F  0F 88 5C 07 00 00               js 0x140aeb7e1
00AEB085  41 0F BA E5 12                  bt r13d, 0x12
00AEB08A  72 22                           jb 0x140aeb0ae
00AEB08C  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
00AEB090  8A 90 FA 05 00 00               mov dl, byte ptr [rax + 0x5fa]
00AEB096  8A C3                           mov al, bl
00AEB098  24 07                           and al, 7
00AEB09A  41 3A C6                        cmp al, r14b
00AEB09D  74 16                           je 0x140aeb0b5
00AEB09F  44 8A C3                        mov r8b, bl
00AEB0A2  41 8A CF                        mov cl, r15b
00AEB0A5  E8 EE 4F F2 FF                  call 0x140a10098
00AEB0AA  84 C0                           test al, al
00AEB0AC  74 07                           je 0x140aeb0b5
00AEB0AE  80 8D C0 01 00 00 08            or byte ptr [rbp + 0x1c0], 8
00AEB0B5  48 8B 95 80 00 00 00            mov rdx, qword ptr [rbp + 0x80]
00AEB0BC  48 8D 8D B0 01 00 00            lea rcx, [rbp + 0x1b0]
00AEB0C3  E8 88 B9 F7 FF                  call 0x140a66a50
00AEB0C8  4C 8D 85 B0 01 00 00            lea r8, [rbp + 0x1b0]
00AEB0CF  48 8B 55 70                     mov rdx, qword ptr [rbp + 0x70]
00AEB0D3  41 8A CF                        mov cl, r15b
00AEB0D6  E8 75 B2 EF FF                  call 0x1409e6350
00AEB0DB  8B F0                           mov esi, eax
00AEB0DD  85 C0                           test eax, eax
00AEB0DF  79 0C                           jns 0x140aeb0ed
00AEB0E1  80 A5 C0 01 00 00 FB            and byte ptr [rbp + 0x1c0], 0xfb
00AEB0E8  E9 F4 06 00 00                  jmp 0x140aeb7e1
00AEB0ED  48 8D 85 30 07 00 00            lea rax, [rbp + 0x730]
00AEB0F4  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
00AEB0F8  8A 45 09                        mov al, byte ptr [rbp + 9]
00AEB0FB  88 45 05                        mov byte ptr [rbp + 5], al
00AEB0FE  E9 CB 00 00 00                  jmp 0x140aeb1ce
00AEB103  48 89 BD 80 02 00 00            mov qword ptr [rbp + 0x280], rdi
00AEB10A  E9 D2 06 00 00                  jmp 0x140aeb7e1
00AEB10F  48 89 BD 70 02 00 00            mov qword ptr [rbp + 0x270], rdi
00AEB116  B9 02 00 00 00                  mov ecx, 2
00AEB11B  E9 0D FC FF FF                  jmp 0x140aead2d
00AEB120  4C 8B 55 48                     mov r10, qword ptr [rbp + 0x48]
00AEB124  49 3B DA                        cmp rbx, r10
00AEB127  0F 85 AF 06 00 00               jne 0x140aeb7dc
00AEB12D  45 84 FF                        test r15b, r15b
00AEB130  0F 84 A6 06 00 00               je 0x140aeb7dc
00AEB136  48 39 7D 70                     cmp qword ptr [rbp + 0x70], rdi
00AEB13A  0F 85 9C 06 00 00               jne 0x140aeb7dc
00AEB140  F6 85 C1 01 00 00 0C            test byte ptr [rbp + 0x1c1], 0xc
00AEB147  0F 85 8F 06 00 00               jne 0x140aeb7dc
00AEB14D  84 C0                           test al, al
00AEB14F  0F 88 87 06 00 00               js 0x140aeb7dc
00AEB155  4C 85 A5 B8 01 00 00            test qword ptr [rbp + 0x1b8], r12
00AEB15C  0F 85 7A 06 00 00               jne 0x140aeb7dc
00AEB162  8A 85 C0 01 00 00               mov al, byte ptr [rbp + 0x1c0]
00AEB168  A8 10                           test al, 0x10
00AEB16A  0F 85 6C 06 00 00               jne 0x140aeb7dc
00AEB170  24 FB                           and al, 0xfb
00AEB172  88 85 C0 01 00 00               mov byte ptr [rbp + 0x1c0], al
00AEB178  8A 9B FA 05 00 00               mov bl, byte ptr [rbx + 0x5fa]
00AEB17E  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00AEB182  8A 88 F9 05 00 00               mov cl, byte ptr [rax + 0x5f9]
00AEB188  88 4D 05                        mov byte ptr [rbp + 5], cl
00AEB18B  44 8A A0 F8 05 00 00            mov r12b, byte ptr [rax + 0x5f8]
00AEB192  41 F6 C5 40                     test r13b, 0x40
00AEB196  74 0F                           je 0x140aeb1a7
00AEB198  F6 C3 07                        test bl, 7
00AEB19B  75 0A                           jne 0x140aeb1a7
00AEB19D  BE 22 00 00 C0                  mov esi, 0xc0000022
00AEB1A2  E9 3A 06 00 00                  jmp 0x140aeb7e1
00AEB1A7  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
00AEB1AB  45 8B CD                        mov r9d, r13d
00AEB1AE  45 8A C7                        mov r8b, r15b
00AEB1B1  48 8D 95 B0 01 00 00            lea rdx, [rbp + 0x1b0]
00AEB1B8  49 8B CA                        mov rcx, r10
00AEB1BB  E8 18 79 FB FF                  call 0x140aa2ad8
00AEB1C0  8B F0                           mov esi, eax
00AEB1C2  85 C0                           test eax, eax
00AEB1C4  0F 88 17 06 00 00               js 0x140aeb7e1
00AEB1CA  48 89 7D 70                     mov qword ptr [rbp + 0x70], rdi
00AEB1CE  8B CF                           mov ecx, edi
00AEB1D0  48 39 BD 48 02 00 00            cmp qword ptr [rbp + 0x248], rdi
00AEB1D7  0F 95 C1                        setne cl
00AEB1DA  48 8D 45 10                     lea rax, [rbp + 0x10]
00AEB1DE  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00AEB1E3  48 8D 45 20                     lea rax, [rbp + 0x20]
00AEB1E7  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00AEB1EC  48 8B 85 80 00 00 00            mov rax, qword ptr [rbp + 0x80]
00AEB1F3  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00AEB1F8  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
00AEB1FC  48 8D 85 B0 01 00 00            lea rax, [rbp + 0x1b0]
00AEB203  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00AEB208  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
00AEB20C  44 89 6C 24 40                  mov dword ptr [rsp + 0x40], r13d
00AEB211  48 8B 85 50 02 00 00            mov rax, qword ptr [rbp + 0x250]
00AEB218  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AEB21D  48 8B 85 80 02 00 00            mov rax, qword ptr [rbp + 0x280]
00AEB224  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEB229  8A 45 05                        mov al, byte ptr [rbp + 5]
00AEB22C  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00AEB230  44 88 64 24 20                  mov byte ptr [rsp + 0x20], r12b
00AEB235  44 8A CB                        mov r9b, bl
00AEB238  4C 8B 85 88 00 00 00            mov r8, qword ptr [rbp + 0x88]
00AEB23F  41 8A D7                        mov dl, r15b
00AEB242  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
00AEB246  E8 F1 88 F2 FF                  call 0x140a13b3c
00AEB24B  8B F0                           mov esi, eax
00AEB24D  85 C0                           test eax, eax
00AEB24F  0F 88 8C 05 00 00               js 0x140aeb7e1
00AEB255  48 8B 85 80 02 00 00            mov rax, qword ptr [rbp + 0x280]
00AEB25C  48 F7 D8                        neg rax
00AEB25F  1B F6                           sbb esi, esi
00AEB261  83 E6 F0                        and esi, 0xfffffff0
00AEB264  81 C6 1B 00 10 00               add esi, 0x10001b
00AEB26A  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
00AEB26E  8B 88 54 07 00 00               mov ecx, dword ptr [rax + 0x754]
00AEB274  81 E1 00 40 00 00               and ecx, 0x4000
00AEB27A  8B C1                           mov eax, ecx
00AEB27C  F7 D8                           neg eax
00AEB27E  48 1B C0                        sbb rax, rax
00AEB281  25 00 08 00 00                  and eax, 0x800
00AEB286  48 89 85 88 00 00 00            mov qword ptr [rbp + 0x88], rax
00AEB28D  85 C9                           test ecx, ecx
00AEB28F  74 06                           je 0x140aeb297
00AEB291  81 CE 40 00 10 00               or esi, 0x100040
00AEB297  4C 8B C0                        mov r8, rax
00AEB29A  48 8D 55 38                     lea rdx, [rbp + 0x38]
00AEB29E  8B CE                           mov ecx, esi
00AEB2A0  E8 3B 8D 9A FF                  call 0x140493fe0
00AEB2A5  48 89 7D 58                     mov qword ptr [rbp + 0x58], rdi
00AEB2A9  40 38 7D 07                     cmp byte ptr [rbp + 7], dil
00AEB2AD  0F 85 EC 00 00 00               jne 0x140aeb39f
00AEB2B3  44 8B 45 38                     mov r8d, dword ptr [rbp + 0x38]
00AEB2B7  49 8D 40 0F                     lea rax, [r8 + 0xf]
00AEB2BB  49 3B C0                        cmp rax, r8
00AEB2BE  77 0A                           ja 0x140aeb2ca
00AEB2C0  48 B8 F0 FF FF FF FF FF FF 0F   movabs rax, 0xffffffffffffff0
00AEB2CA  48 83 E0 F0                     and rax, 0xfffffffffffffff0
00AEB2CE  E8 8D F6 BC FF                  call 0x1406ba960
00AEB2D3  48 2B E0                        sub rsp, rax
00AEB2D6  4C 8D A4 24 80 00 00 00         lea r12, [rsp + 0x80]
00AEB2DE  4C 89 65 58                     mov qword ptr [rbp + 0x58], r12
00AEB2E2  33 D2                           xor edx, edx
00AEB2E4  49 8B CC                        mov rcx, r12
00AEB2E7  E8 54 B9 BD FF                  call 0x1406c6c40
00AEB2EC  4C 8B 8D 88 00 00 00            mov r9, qword ptr [rbp + 0x88]
00AEB2F3  4C 8D 85 D0 00 00 00            lea r8, [rbp + 0xd0]
00AEB2FA  8B D6                           mov edx, esi
00AEB2FC  49 8B CC                        mov rcx, r12
00AEB2FF  E8 3C AA 80 FF                  call 0x1402f5d40
00AEB304  48 39 BD 80 02 00 00            cmp qword ptr [rbp + 0x280], rdi
00AEB30B  74 3B                           je 0x140aeb348
00AEB30D  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00AEB311  48 83 B9 10 03 00 00 00         cmp qword ptr [rcx + 0x310], 0
00AEB319  8B 85 9C 02 00 00               mov eax, dword ptr [rbp + 0x29c]
00AEB31F  75 07                           jne 0x140aeb328
00AEB321  48 8B 81 E0 02 00 00            mov rax, qword ptr [rcx + 0x2e0]
00AEB328  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEB32D  4C 8B 8D E8 01 00 00            mov r9, qword ptr [rbp + 0x1e8]
00AEB334  4C 8B 05 45 C1 4D 00            mov r8, qword ptr [rip + 0x4dc145]
00AEB33B  41 8B D6                        mov edx, r14d
00AEB33E  49 8B CC                        mov rcx, r12
00AEB341  E8 DA 71 F3 FF                  call 0x140a22520
00AEB346  EB 43                           jmp 0x140aeb38b
00AEB348  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
00AEB34D  45 8A CE                        mov r9b, r14b
00AEB350  45 33 C0                        xor r8d, r8d
00AEB353  49 8B D4                        mov rdx, r12
00AEB356  48 8B 4D 68                     mov rcx, qword ptr [rbp + 0x68]
00AEB35A  E8 11 94 DE FF                  call 0x1408d4770
00AEB35F  8B F0                           mov esi, eax
00AEB361  85 C0                           test eax, eax
00AEB363  79 1D                           jns 0x140aeb382
00AEB365  48 8B 55 68                     mov rdx, qword ptr [rbp + 0x68]
00AEB369  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00AEB36D  E8 4E 4E 97 FF                  call 0x1404601c0
00AEB372  33 D2                           xor edx, edx
00AEB374  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00AEB378  E8 D3 B9 E1 FF                  call 0x140906d50
00AEB37D  E9 5F 04 00 00                  jmp 0x140aeb7e1
00AEB382  49 C7 44 24 78 29 01 00 00      mov qword ptr [r12 + 0x78], 0x129
00AEB38B  48 8D 85 60 01 00 00            lea rax, [rbp + 0x160]
00AEB392  48 89 85 40 01 00 00            mov qword ptr [rbp + 0x140], rax
00AEB399  4C 8B 65 70                     mov r12, qword ptr [rbp + 0x70]
00AEB39D  EB 03                           jmp 0x140aeb3a2
00AEB39F  4C 8B E7                        mov r12, rdi
00AEB3A2  BA 50 73 43 72                  mov edx, 0x72437350
00AEB3A7  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00AEB3AB  E8 60 53 72 FF                  call 0x140210710
00AEB3B0  4D 85 E4                        test r12, r12
00AEB3B3  74 33                           je 0x140aeb3e8
00AEB3B5  41 88 3C 24                     mov byte ptr [r12], dil
00AEB3B9  48 8B 85 F8 01 00 00            mov rax, qword ptr [rbp + 0x1f8]
00AEB3C0  B9 00 00 04 00                  mov ecx, 0x40000
00AEB3C5  48 3B C1                        cmp rax, rcx
00AEB3C8  48 0F 42 C1                     cmovb rax, rcx
00AEB3CC  49 89 44 24 18                  mov qword ptr [r12 + 0x18], rax
00AEB3D1  48 8B 85 00 02 00 00            mov rax, qword ptr [rbp + 0x200]
00AEB3D8  49 89 44 24 10                  mov qword ptr [r12 + 0x10], rax
00AEB3DD  8B 85 F0 01 00 00               mov eax, dword ptr [rbp + 0x1f0]
00AEB3E3  49 89 44 24 08                  mov qword ptr [r12 + 8], rax
00AEB3E8  89 7D 38                        mov dword ptr [rbp + 0x38], edi
00AEB3EB  48 8D 55 18                     lea rdx, [rbp + 0x18]
00AEB3EF  8B 8D E8 07 00 00               mov ecx, dword ptr [rbp + 0x7e8]
00AEB3F5  E8 0E B9 F3 FF                  call 0x140a26d08
00AEB3FA  40 38 7D 20                     cmp byte ptr [rbp + 0x20], dil
00AEB3FE  74 0B                           je 0x140aeb40b
00AEB400  C7 45 38 02 00 00 00            mov dword ptr [rbp + 0x38], 2
00AEB407  83 4D 18 10                     or dword ptr [rbp + 0x18], 0x10
00AEB40B  40 38 7D 21                     cmp byte ptr [rbp + 0x21], dil
00AEB40F  74 05                           je 0x140aeb416
00AEB411  41 0F BA ED 0A                  bts r13d, 0xa
00AEB416  40 38 7D 07                     cmp byte ptr [rbp + 7], dil
00AEB41A  74 05                           je 0x140aeb421
00AEB41C  0F BA 6D 18 0A                  bts dword ptr [rbp + 0x18], 0xa
00AEB421  83 4D 18 60                     or dword ptr [rbp + 0x18], 0x60
00AEB425  48 8D 85 A0 05 00 00            lea rax, [rbp + 0x5a0]
00AEB42C  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00AEB431  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
00AEB436  48 8D 45 78                     lea rax, [rbp + 0x78]
00AEB43A  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00AEB43F  48 8D 45 18                     lea rax, [rbp + 0x18]
00AEB443  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00AEB448  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AEB44D  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AEB452  48 8D 85 40 01 00 00            lea rax, [rbp + 0x140]
00AEB459  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AEB45E  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00AEB462  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEB467  4C 8D 8D B0 01 00 00            lea r9, [rbp + 0x1b0]
00AEB46E  45 8A C7                        mov r8b, r15b
00AEB471  48 8B 95 D8 00 00 00            mov rdx, qword ptr [rbp + 0xd8]
00AEB478  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00AEB47C  E8 AB 42 F0 FF                  call 0x1409ef72c
00AEB481  8B F0                           mov esi, eax
00AEB483  85 C0                           test eax, eax
00AEB485  79 21                           jns 0x140aeb4a8
00AEB487  48 8B 55 68                     mov rdx, qword ptr [rbp + 0x68]
00AEB48B  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00AEB48F  E8 2C 4D 97 FF                  call 0x1404601c0
00AEB494  33 D2                           xor edx, edx
00AEB496  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00AEB49A  E8 B1 B8 E1 FF                  call 0x140906d50
00AEB49F  44 8B 7D 00                     mov r15d, dword ptr [rbp]
00AEB4A3  E9 09 02 00 00                  jmp 0x140aeb6b1
00AEB4A8  4C 8B 45 10                     mov r8, qword ptr [rbp + 0x10]
00AEB4AC  48 8B 75 48                     mov rsi, qword ptr [rbp + 0x48]
00AEB4B0  48 8B D6                        mov rdx, rsi
00AEB4B3  41 8A CF                        mov cl, r15b
00AEB4B6  E8 81 4B F2 FF                  call 0x140a1003c
00AEB4BB  84 C0                           test al, al
00AEB4BD  0F 84 8C 00 00 00               je 0x140aeb54f
00AEB4C3  E8 BC C1 97 FF                  call 0x140467684
00AEB4C8  41 B8 00 00 00 02               mov r8d, 0x2000000
00AEB4CE  48 8D 15 9B 0D 06 00            lea rdx, [rip + 0x60d9b]
00AEB4D5  44 85 45 28                     test dword ptr [rbp + 0x28], r8d
00AEB4D9  74 37                           je 0x140aeb512
00AEB4DB  0F B6 C3                        movzx eax, bl
00AEB4DE  48 C1 E8 04                     shr rax, 4
00AEB4E2  48 8D 0C 40                     lea rcx, [rax + rax*2]
00AEB4E6  8B 44 8A 04                     mov eax, dword ptr [rdx + rcx*4 + 4]
00AEB4EA  F7 D0                           not eax
00AEB4EC  25 FF FF 1F 00                  and eax, 0x1fffff
00AEB4F1  0B 45 28                        or eax, dword ptr [rbp + 0x28]
00AEB4F4  0F BA F0 19                     btr eax, 0x19
00AEB4F8  89 45 28                        mov dword ptr [rbp + 0x28], eax
00AEB4FB  48 8B 8D 38 02 00 00            mov rcx, qword ptr [rbp + 0x238]
00AEB502  48 85 C9                        test rcx, rcx
00AEB505  74 05                           je 0x140aeb50c
00AEB507  48 3B F1                        cmp rsi, rcx
00AEB50A  75 06                           jne 0x140aeb512
00AEB50C  41 0B C6                        or eax, r14d
00AEB50F  89 45 28                        mov dword ptr [rbp + 0x28], eax
00AEB512  44 85 45 30                     test dword ptr [rbp + 0x30], r8d
00AEB516  74 37                           je 0x140aeb54f
00AEB518  0F B6 C3                        movzx eax, bl
00AEB51B  48 C1 E8 04                     shr rax, 4
00AEB51F  48 8D 0C 40                     lea rcx, [rax + rax*2]
00AEB523  8B 44 8A 08                     mov eax, dword ptr [rdx + rcx*4 + 8]
00AEB527  F7 D0                           not eax
00AEB529  25 FF FF 1F 00                  and eax, 0x1fffff
00AEB52E  0B 45 30                        or eax, dword ptr [rbp + 0x30]
00AEB531  0F BA F0 19                     btr eax, 0x19
00AEB535  89 45 30                        mov dword ptr [rbp + 0x30], eax
00AEB538  48 8B 8D 38 02 00 00            mov rcx, qword ptr [rbp + 0x238]
00AEB53F  48 85 C9                        test rcx, rcx
00AEB542  74 05                           je 0x140aeb549
00AEB544  48 3B F1                        cmp rsi, rcx
00AEB547  75 06                           jne 0x140aeb54f
00AEB549  41 0B C6                        or eax, r14d
00AEB54C  89 45 30                        mov dword ptr [rbp + 0x30], eax
00AEB54F  E8 14 24 AE FF                  call 0x1405cd968
00AEB554  85 C0                           test eax, eax
00AEB556  74 4D                           je 0x140aeb5a5
00AEB558  4C 8D 45 28                     lea r8, [rbp + 0x28]
00AEB55C  41 8A D7                        mov dl, r15b
00AEB55F  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00AEB563  E8 28 C0 B1 FF                  call 0x140607590
00AEB568  8B F0                           mov esi, eax
00AEB56A  85 C0                           test eax, eax
00AEB56C  79 21                           jns 0x140aeb58f
00AEB56E  48 8B 55 68                     mov rdx, qword ptr [rbp + 0x68]
00AEB572  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00AEB576  E8 45 4C 97 FF                  call 0x1404601c0
00AEB57B  33 D2                           xor edx, edx
00AEB57D  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00AEB581  E8 CA B7 E1 FF                  call 0x140906d50
00AEB586  44 8B 7D 00                     mov r15d, dword ptr [rbp]
00AEB58A  E9 19 01 00 00                  jmp 0x140aeb6a8
00AEB58F  4C 8D 45 30                     lea r8, [rbp + 0x30]
00AEB593  41 8A D7                        mov dl, r15b
00AEB596  48 8B 4D 78                     mov rcx, qword ptr [rbp + 0x78]
00AEB59A  E8 F1 BF B1 FF                  call 0x140607590
00AEB59F  8B F0                           mov esi, eax
00AEB5A1  85 C0                           test eax, eax
00AEB5A3  78 C9                           js 0x140aeb56e
00AEB5A5  48 8B 85 88 02 00 00            mov rax, qword ptr [rbp + 0x288]
00AEB5AC  48 85 C0                        test rax, rax
00AEB5AF  74 06                           je 0x140aeb5b7
00AEB5B1  48 83 C0 70                     add rax, 0x70
00AEB5B5  EB 03                           jmp 0x140aeb5ba
00AEB5B7  48 8B C7                        mov rax, rdi
00AEB5BA  48 8D 8D 10 04 00 00            lea rcx, [rbp + 0x410]
00AEB5C1  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00AEB5C6  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEB5CB  8B 45 38                        mov eax, dword ptr [rbp + 0x38]
00AEB5CE  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00AEB5D2  48 8B 85 40 02 00 00            mov rax, qword ptr [rbp + 0x240]
00AEB5D9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AEB5DE  45 8B CD                        mov r9d, r13d
00AEB5E1  44 8B 45 28                     mov r8d, dword ptr [rbp + 0x28]
00AEB5E5  48 8B 55 60                     mov rdx, qword ptr [rbp + 0x60]
00AEB5E9  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00AEB5ED  E8 DA BC E5 FF                  call 0x1409472cc
00AEB5F2  8B D8                           mov ebx, eax
00AEB5F4  48 8B 8D C8 01 00 00            mov rcx, qword ptr [rbp + 0x1c8]
00AEB5FB  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
00AEB600  48 8B 85 90 00 00 00            mov rax, qword ptr [rbp + 0x90]
00AEB607  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00AEB60C  48 8D 85 A0 05 00 00            lea rax, [rbp + 0x5a0]
00AEB613  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00AEB618  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AEB61D  48 8D 85 B0 01 00 00            lea rax, [rbp + 0x1b0]
00AEB624  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AEB629  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00AEB62E  8B 4D 30                        mov ecx, dword ptr [rbp + 0x30]
00AEB631  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00AEB635  4C 8D 4D 18                     lea r9, [rbp + 0x18]
00AEB639  4C 8D 85 60 01 00 00            lea r8, [rbp + 0x160]
00AEB640  48 8B 55 10                     mov rdx, qword ptr [rbp + 0x10]
00AEB644  48 8B 4D 78                     mov rcx, qword ptr [rbp + 0x78]
00AEB648  E8 C7 4C F0 FF                  call 0x1409f0314
00AEB64D  8B F0                           mov esi, eax
00AEB64F  48 8B 4D 68                     mov rcx, qword ptr [rbp + 0x68]
00AEB653  E8 B8 39 77 FF                  call 0x14025f010
00AEB658  85 DB                           test ebx, ebx
00AEB65A  79 12                           jns 0x140aeb66e
00AEB65C  33 D2                           xor edx, edx
00AEB65E  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00AEB662  E8 E9 B6 E1 FF                  call 0x140906d50
00AEB667  8B F3                           mov esi, ebx
00AEB669  E9 18 FF FF FF                  jmp 0x140aeb586
00AEB66E  85 F6                           test esi, esi
00AEB670  78 17                           js 0x140aeb689
00AEB672  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00AEB676  E8 65 08 96 FF                  call 0x14044bee0
00AEB67B  48 3B 85 58 03 00 00            cmp rax, qword ptr [rbp + 0x358]
00AEB682  74 40                           je 0x140aeb6c4
00AEB684  BE 2D 02 00 C0                  mov esi, 0xc000022d
00AEB689  44 8B 7D 00                     mov r15d, dword ptr [rbp]
00AEB68D  48 8D 8D 10 04 00 00            lea rcx, [rbp + 0x410]
00AEB694  E8 D7 A8 DD FF                  call 0x1408c5f70
00AEB699  85 F6                           test esi, esi
00AEB69B  79 0B                           jns 0x140aeb6a8
00AEB69D  8B D6                           mov edx, esi
00AEB69F  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00AEB6A3  E8 BC 95 E1 FF                  call 0x140904c64
00AEB6A8  48 8B 4D 78                     mov rcx, qword ptr [rbp + 0x78]
00AEB6AC  E8 9F DC 80 FF                  call 0x1402f9350
00AEB6B1  BA 50 73 43 72                  mov edx, 0x72437350
00AEB6B6  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00AEB6BA  E8 21 C2 80 FF                  call 0x1402f78e0
00AEB6BF  E9 21 01 00 00                  jmp 0x140aeb7e5
00AEB6C4  4C 8B 05 CD B3 4D 00            mov r8, qword ptr [rip + 0x4db3cd]
00AEB6CB  48 8D 95 10 04 00 00            lea rdx, [rbp + 0x410]
00AEB6D2  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
00AEB6D6  E8 41 2E F3 FF                  call 0x140a1e51c
00AEB6DB  8B F0                           mov esi, eax
00AEB6DD  85 C0                           test eax, eax
00AEB6DF  0F 88 B8 00 00 00               js 0x140aeb79d
00AEB6E5  48 8B 85 D8 01 00 00            mov rax, qword ptr [rbp + 0x1d8]
00AEB6EC  48 85 C0                        test rax, rax
00AEB6EF  74 2B                           je 0x140aeb71c
00AEB6F1  0F 10 85 E8 01 00 00            movups xmm0, xmmword ptr [rbp + 0x1e8]
00AEB6F8  0F 11 00                        movups xmmword ptr [rax], xmm0
00AEB6FB  0F 10 8D F8 01 00 00            movups xmm1, xmmword ptr [rbp + 0x1f8]
00AEB702  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
00AEB706  0F 10 85 08 02 00 00            movups xmm0, xmmword ptr [rbp + 0x208]
00AEB70D  0F 11 40 20                     movups xmmword ptr [rax + 0x20], xmm0
00AEB711  0F 10 8D 18 02 00 00            movups xmm1, xmmword ptr [rbp + 0x218]
00AEB718  0F 11 48 30                     movups xmmword ptr [rax + 0x30], xmm1
00AEB71C  48 8B 85 98 05 00 00            mov rax, qword ptr [rbp + 0x598]
00AEB723  48 8B 8D 98 00 00 00            mov rcx, qword ptr [rbp + 0x98]
00AEB72A  48 89 01                        mov qword ptr [rcx], rax
00AEB72D  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
00AEB731  44 8B 7D 00                     mov r15d, dword ptr [rbp]
00AEB735  EB 17                           jmp 0x140aeb74e
00AEB737  8B F0                           mov esi, eax
00AEB739  33 FF                           xor edi, edi
00AEB73B  44 8D 77 01                     lea r14d, [rdi + 1]
00AEB73F  48 8B 9D E0 00 00 00            mov rbx, qword ptr [rbp + 0xe0]
00AEB746  48 89 5D 48                     mov qword ptr [rbp + 0x48], rbx
00AEB74A  44 8A 7D 08                     mov r15b, byte ptr [rbp + 8]
00AEB74E  85 F6                           test esi, esi
00AEB750  78 1F                           js 0x140aeb771
00AEB752  4C 8B 45 10                     mov r8, qword ptr [rbp + 0x10]
00AEB756  48 8D 95 B0 01 00 00            lea rdx, [rbp + 0x1b0]
00AEB75D  B9 06 00 00 00                  mov ecx, 6
00AEB762  E8 F9 08 00 00                  call 0x140aec060
00AEB767  8B F0                           mov esi, eax
00AEB769  85 C0                           test eax, eax
00AEB76B  0F 89 1C FF FF FF               jns 0x140aeb68d
00AEB771  F7 85 90 05 00 00 00 02 00 00   test dword ptr [rbp + 0x590], 0x200
00AEB77B  75 0F                           jne 0x140aeb78c
00AEB77D  F7 83 FC 05 00 00 00 10 00 00   test dword ptr [rbx + 0x5fc], 0x1000
00AEB787  41 8A D6                        mov dl, r14b
00AEB78A  74 03                           je 0x140aeb78f
00AEB78C  40 8A D7                        mov dl, dil
00AEB78F  48 8B 8D 98 05 00 00            mov rcx, qword ptr [rbp + 0x598]
00AEB796  E8 D5 60 DB FF                  call 0x1408a1870
00AEB79B  EB 04                           jmp 0x140aeb7a1
00AEB79D  44 8B 7D 00                     mov r15d, dword ptr [rbp]
00AEB7A1  85 F6                           test esi, esi
00AEB7A3  0F 89 E4 FE FF FF               jns 0x140aeb68d
00AEB7A9  F7 85 20 07 00 00 00 02 00 00   test dword ptr [rbp + 0x720], 0x200
00AEB7B3  75 10                           jne 0x140aeb7c5
00AEB7B5  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
00AEB7B9  F7 80 FC 05 00 00 00 10 00 00   test dword ptr [rax + 0x5fc], 0x1000
00AEB7C3  74 03                           je 0x140aeb7c8
00AEB7C5  44 8A F7                        mov r14b, dil
00AEB7C8  41 8A D6                        mov dl, r14b
00AEB7CB  48 8B 8D 28 07 00 00            mov rcx, qword ptr [rbp + 0x728]
00AEB7D2  E8 99 60 DB FF                  call 0x1408a1870
00AEB7D7  E9 B1 FE FF FF                  jmp 0x140aeb68d
00AEB7DC  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AEB7E1  44 8B 7D 00                     mov r15d, dword ptr [rbp]
00AEB7E5  48 8B 8D 68 02 00 00            mov rcx, qword ptr [rbp + 0x268]
00AEB7EC  48 85 C9                        test rcx, rcx
00AEB7EF  74 11                           je 0x140aeb802
00AEB7F1  48 8B 05 18 97 41 00            mov rax, qword ptr [rip + 0x419718]
00AEB7F8  48 85 C0                        test rax, rax
00AEB7FB  74 05                           je 0x140aeb802
00AEB7FD  E8 CE F2 BC FF                  call 0x1406baad0
00AEB802  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
00AEB809  E8 42 A5 F9 FF                  call 0x140a85d50
00AEB80E  48 8D 8D B0 01 00 00            lea rcx, [rbp + 0x1b0]
00AEB815  E8 AA 3C F0 FF                  call 0x1409ef4c4
00AEB81A  48 8B 8D 00 01 00 00            mov rcx, qword ptr [rbp + 0x100]
00AEB821  48 85 C9                        test rcx, rcx
00AEB824  74 05                           je 0x140aeb82b
00AEB826  E8 F5 5B DB FF                  call 0x1408a1420
00AEB82B  45 84 FF                        test r15b, r15b
00AEB82E  74 09                           je 0x140aeb839
00AEB830  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
00AEB834  E8 17 DB 80 FF                  call 0x1402f9350
00AEB839  8B C6                           mov eax, esi
00AEB83B  EB 07                           jmp 0x140aeb844
00AEB83D  EB 05                           jmp 0x140aeb844
00AEB83F  B8 0D 00 00 C0                  mov eax, 0xc000000d
00AEB844  48 8B 8D 50 07 00 00            mov rcx, qword ptr [rbp + 0x750]
00AEB84B  48 33 CD                        xor rcx, rbp
00AEB84E  E8 ED 0D BC FF                  call 0x1406ac640
00AEB853  48 8D A5 68 07 00 00            lea rsp, [rbp + 0x768]
00AEB85A  41 5F                           pop r15
00AEB85C  41 5E                           pop r14
00AEB85E  41 5D                           pop r13
00AEB860  41 5C                           pop r12
00AEB862  5F                              pop rdi
00AEB863  5E                              pop rsi
00AEB864  5B                              pop rbx
00AEB865  5D                              pop rbp
00AEB866  C3                              ret
00AEB867  CC                              int3
00AEB868  E8 63 E7 DA FF                  call 0x140899fd0
00AEB86D  90                              nop
00AEB86E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtCreateUserProcess(__int64 a1, __int64 a2, int a3, int a4, __int64 a5, __int64 a6, unsigned int a7, unsigned int a8, __int64 a9, __int64 a10, __int64 a11)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int8 v_stack_m214;
    unsigned int v_stack_m218;
    unsigned __int64 v_stack_m398;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m450;
    unsigned __int64 v_stack_m468;
    unsigned int v_stack_m46C;
    unsigned int v_stack_m470;
    unsigned int v_stack_m47C;
    unsigned __int64 v_stack_m488;
    unsigned __int64 v_stack_m490;
    unsigned __int64 v_stack_m508;
    unsigned int v_stack_m50C;
    unsigned __int64 v_stack_m520;
    unsigned __int64 v_stack_m528;
    unsigned __int64 v_stack_m538;
    unsigned __int64 v_stack_m540;
    unsigned __int64 v_stack_m548;
    unsigned int v_stack_m54C;
    unsigned __int64 v_stack_m558;
    unsigned __int64 v_stack_m560;
    unsigned __int64 v_stack_m568;
    unsigned __int64 v_stack_m570;
    unsigned __int64 v_stack_m578;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m590;
    unsigned __int64 v_stack_m5A0;
    unsigned __int64 v_stack_m5A8;
    unsigned __int64 v_stack_m5B0;
    unsigned int v_stack_m5B8;
    unsigned __int64 v_stack_m5C0;
    unsigned __int64 v_stack_m5D0;
    unsigned __int64 v_stack_m5E0;
    unsigned __int8 v_stack_m5E7;
    unsigned __int8 v_stack_m5E8;
    unsigned __int64 v_stack_m5F0;
    unsigned __int8 v_stack_m5F7;
    unsigned __int64 v_stack_m5F8;
    unsigned __int8 v_stack_m60;
    unsigned __int64 v_stack_m648;
    unsigned __int64 v_stack_m658;
    unsigned __int64 v_stack_m668;
    unsigned __int64 v_stack_m678;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m688;
    unsigned __int64 v_stack_m690;
    unsigned __int64 v_stack_m6A0;
    unsigned __int64 v_stack_m6A8;
    unsigned __int16 v_stack_m6AA;
    unsigned int v_stack_m6AE;
    unsigned __int64 v_stack_m6B0;
    unsigned __int64 v_stack_m6C0;
    unsigned __int64 v_stack_m6C8;
    unsigned __int64 v_stack_m6D0;
    unsigned __int64 v_stack_m6D8;
    unsigned int v_stack_m6E0;
    unsigned __int64 v_stack_m6E8;
    unsigned int v_stack_m6F0;
    unsigned __int64 v_stack_m6F8;
    unsigned __int64 v_stack_m700;
    unsigned __int64 v_stack_m708;
    unsigned __int64 v_stack_m710;
    unsigned __int64 v_stack_m718;
    unsigned __int64 v_stack_m720;
    unsigned __int64 v_stack_m728;
    unsigned __int64 v_stack_m730;
    unsigned __int64 v_stack_m738;
    unsigned __int64 v_stack_m740;
    unsigned __int64 v_stack_m748;
    unsigned __int64 v_stack_m750;
    unsigned __int64 v_stack_m758;
    unsigned __int64 v_stack_m760;
    unsigned __int64 v_stack_m768;
    unsigned int v_stack_m770;
    unsigned int v_stack_m778;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m780;
    unsigned __int8 v_stack_m787;
    unsigned __int16 v_stack_m788;
    unsigned __int8 v_stack_m78C;
    unsigned int v_stack_m790;
    unsigned __int64 v_stack_m798;
    unsigned __int8 v_stack_m79E;
    unsigned __int8 v_stack_m79F;
    unsigned __int8 v_stack_m7A0;
    unsigned __int8 v_stack_m7A1;
    unsigned __int8 v_stack_m7A2;
    unsigned __int8 v_stack_m7A3;
    unsigned __int8 v_stack_m7A4;
    unsigned __int64 v_stack_m7A8;
    unsigned __int64 v_stack_m7B8;
    unsigned int v_stack_m7C0;
    unsigned __int64 v_stack_m7C8;
    unsigned int v_stack_m7D0;
    unsigned int v_stack_m7D8;
    unsigned __int64 v_stack_m7E0;
    unsigned int v_stack_m7E8;
    unsigned __int64 v_stack_m7F0;
    unsigned __int64 v_stack_m7F8;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m800;
    unsigned int v_stack_m808;
    unsigned int v_stack_m88;

    v_rsp = (v_rsp) - (0x7E8ULL);
    result = (*(unsigned __int64 *)(v_rip + 3276957)) ^ (v_stack_m7A8);
    v_stack_m58 = result;
    v_stack_m718 = a2;
    v_stack_m710 = a1;
    v_stack_m720 = a5;
    v_stack_m780 = a3;
    v_stack_m778 = a4;
    v_stack_m6D0 = a6;
    v_stack_m738 = a9;
    v_rdi = 0;
    v_stack_m788 = 0;
    v_stack_m790 = 0;
    result = 0;
    v_stack_m6AE = 0;
    v_stack_m6AA = 0;
    v_stack_m678 = v_xmm0;
    v_stack_m798 = 0;
    v_stack_m730 = 0;
    v_stack_m708 = v_xmm0;
    v_stack_m6F8 = v_xmm0;
    v_stack_m6E8 = 0;
    v_stack_m6E0 = 0;
    v_stack_m748 = 0;
    a2 = 0;
    result = memset(v_stack_m398, a2, 400, a4);
    v_stack_m688 = v_xmm0;
    v_stack_m79E = 0;
    v_stack_m7A4 = 0;
    v_stack_m79F = 0;
    v_stack_m7A3 = 0;
    result = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    a2 = 0;
    result = memset(v_stack_m208, a2, 400, a4);
    v_stack_m6D8 = 0;
    v_stack_m770 = 0;
    v_stack_m768 = 0;
    result = 0;
    v_stack_m668 = v_xmm0;
    v_stack_m658 = 0;
    v_stack_m6C0 = v_xmm0;
    v_stack_m740 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m760 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_m6C8 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_m78C = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m728 = 0;
    v_stack_m758 = 0;
    v_stack_m7A8 = 0;
    v_stack_m7A0 = 0;
    v_stack_m7A1 = 0;
    result = 0;
    v_stack_m6B0 = v_xmm0;
    v_stack_m6A0 = v_xmm0;
    v_stack_m690 = 0;
    a2 = 0;
    result = memset(v_stack_m648, a2, v_rdi + 72, a4);
    if ((((unsigned int)((unsigned int)(a7))) & (0xFF317838ULL)) != 0) goto loc_00AEB83F;
    if (((a8) & (0xFFFFFFFEULL)) != 0) goto loc_00AEB83F;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a7)))) & ((unsigned int)((unsigned int)(0x8400ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x8400ULL)))) goto loc_00AEA867;
    goto loc_00AEB844;
loc_00AEA867:
    v_stack_m214 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    result = (unsigned int)(0xC0000030ULL);
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) {
        a1 = 0;
        if (v_stack_m710 < 0) { a1 = v_stack_m710; }
        result = *(unsigned __int64 *)(a1);
        *(unsigned __int64 *)(a1) = result;
        a1 = 0;
        if (v_stack_m718 < 0) { a1 = v_stack_m718; }
        result = *(unsigned __int64 *)(a1);
        *(unsigned __int64 *)(a1) = result;
    }
    if (a5 == 0) goto loc_00AEA8E7;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AEA8CB;
    if ((((unsigned __int8)(a5)) & (3)) != 0) goto loc_00AEB868;
    if (a5 < 0) { a2 = a5; }
loc_00AEA8CB:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_00AEA8DC;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a5 + 24))) & (0x11FF2ULL));
    goto loc_00AEA8E1;
loc_00AEA8DC:
    result = (unsigned int)((result) & (0x1DF2ULL));
loc_00AEA8E1:
    v_stack_m218 = (unsigned int)(result);
loc_00AEA8E7:
    a2 = 0;
    result = memset(v_stack_m5F8, a2, 608, a4);
    if (a11 == 0) goto loc_00AEA928;
    a3 = 0;
    result = PspBuildCreateProcessContext(a11, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, v_stack_m5F8);
    if (sign_flag) goto loc_00AEB844;
loc_00AEA928:
    if ((((unsigned __int8)((unsigned int)(a7))) & (64)) == 0) goto loc_00AEA953;
    if (((v_stack_m5F0) & ((unsigned int)(0x20000ULL))) == 0) goto loc_00AEA953;
    v_r13 = (unsigned int)(a7);
    if (v_stack_m5F7 == 0) {
        v_r13 = (unsigned int)(((unsigned int)(a7)) & (0xFFFFFFBFULL));
    }
    if ((((unsigned __int8)(v_r13)) & (4)) != 0) goto loc_00AEA96A;
    if (((v_stack_m5F0) & (0x800ULL)) != 0) goto loc_00AEB7DC;
loc_00AEA96A:
    if (((v_stack_m5F0) & ((unsigned int)(0x20000ULL))) == 0) goto loc_00AEA97D;
    if ((((unsigned __int8)(v_r13)) & (64)) == 0) goto loc_00AEB7DC;
loc_00AEA97D:
    result = PspCaptureCreateInfo((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a10, v_stack_m5F8, v_stack_m5F8);
    if (sign_flag) goto loc_00AEB7E1;
    if (((v_stack_m5F0) & (1)) == 0) goto loc_00AEA9F4;
    v_stack_m7F0 = 0;
    v_stack_m7F8 = 0;
    v_stack_m800 = v_stack_m748;
    v_stack_m808 = 0x72437350ULL;
    result = ObpReferenceObjectByHandleWithTag(v_stack_m578, 1 + 127, *(unsigned __int64 *)(v_rip + 5095657), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (sign_flag) goto loc_00AEB7E1;
    v_stack_m570 = v_stack_m748;
    goto loc_00AEA9F8;
loc_00AEA9F4:
    v_stack_m748 = v_stack_m748;
loc_00AEA9F8:
    result = PspEstimateNewProcessServerSilo(v_stack_m748, v_stack_m488, (unsigned int)(v_stack_m47C), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_stack_m450 = result;
    result = (unsigned __int8)((v_stack_m5E7) & (12));
    if (((unsigned __int8)(result)) != 4) goto loc_00AEAA3E;
    if (v_stack_m748 != v_stack_m760) goto loc_00AEB7DC;
    if (((*(unsigned int *)(v_stack_m760 + 1532)) & (0x1000ULL)) != 0) goto loc_00AEB7DC;
loc_00AEAA3E:
    result = PspReferenceTokenForNewProcess(v_stack_m748, v_stack_m560, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_m558);
    if (!sign_flag) goto loc_00AEAA69;
    v_stack_m558 = 0;
    goto loc_00AEB7E1;
loc_00AEAA69:
    if (v_stack_m560 == 0) goto loc_00AEAA9E;
    result = SeQueryServerSiloToken(v_stack_m558, v_stack_m768, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_m558);
    if (sign_flag) goto loc_00AEAA9E;
    result = PspIsSiloInSilo(v_stack_m768, v_stack_m450, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_m558);
    if ((unsigned __int8)(result) == 0) goto loc_00AEB7DC;
loc_00AEAA9E:
    if ((((unsigned __int8)(v_stack_m5F0)) & (32)) == 0) goto loc_00AEB120;
    result = (v_stack_m5F0) & ((unsigned int)(0x20000ULL));
    result = -(result);
    v_rbx = (unsigned __int8)((v_stack_m748) & (v_stack_m5F7));
    v_stack_m7A2 = (unsigned __int8)(v_rbx);
    if (((*(unsigned int *)(v_rip + 5085170)) & (0x40000ULL)) != 0) {
        v_stack_m688 = v_xmm0;
        v_stack_m800 = 0;
        v_stack_m808 = 0;
        a4 = 0;
        a3 = a4 + 16;
        a2 = v_stack_m688;
        a1 = a4 + 38;
        result = ZwSystemDebugControl(a1, a2, a3, a4);
    }
    if (condition_is_above_or_equal) goto loc_00AEAB23;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5173184), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00AEAB23;
loc_00AEAB19:
    goto loc_00AEB7E1;
loc_00AEAB23:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) >> (6));
    a3 = (unsigned int)((a3) & (1));
    v_stack_m7F8 = v_stack_m7A2;
    v_stack_m800 = v_stack_m79F;
    v_stack_m808 = v_stack_m7A4;
    result = SeQuerySigningPolicy(v_stack_m558, v_stack_m508, a3, (unsigned __int8)(v_rbx));
    if (sign_flag) goto loc_00AEB7E1;
    if ((((unsigned int)((unsigned int)(0x20000ULL))) & ((unsigned int)(v_r13))) == 0) goto loc_00AEAB8D;
    result = SeCompareSigningLevels(v_stack_m7A4, 8, a3, (unsigned __int8)(v_rbx));
    v_r12 = v_stack_m7A4;
    if ((unsigned int)(result) == 0) { v_r12 = 8; }
    v_stack_m7A4 = (unsigned __int8)(v_r12);
    goto loc_00AEAB91;
loc_00AEAB8D:
loc_00AEAB91:
    v_stack_m708 = 48;
    v_stack_m700 = 0;
    result = (unsigned int)(0x640ULL);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562))) != 1) { result = 576; }
    v_stack_m6F0 = (unsigned int)(result);
    v_stack_m6F8 = v_stack_m508;
    v_stack_m6E8 = v_xmm0;
    result = *(unsigned __int64 *)(v_rip + 5167094);
    v_rsi = 0;
    if (*(unsigned __int64 *)(v_rip + 5167094) != 0) {
        a1 = v_stack_m558;
        result = guard_dispatch_icall(a1, 8, a3, (unsigned __int8)(v_rbx));
        v_rsi = (unsigned int)(result);
    }
    if (sign_flag) goto loc_00AEB7E1;
    v_stack_m808 = v_stack_m728;
    result = PspGetMemoryPartitionContext(v_stack_m748, (unsigned int)((unsigned int)(v_r13)), v_stack_m488, (unsigned int)(v_stack_m47C));
    if (sign_flag) goto loc_00AEB7E1;
    result = PspCreateUserProcessEcp(v_stack_m6B0, v_stack_m558, v_stack_m488, (unsigned int)(v_stack_m47C));
    if (sign_flag) goto loc_00AEB7E1;
    a2 = (unsigned int)(((unsigned int)(v_stack_m54C)) | (0x100020ULL));
    v_stack_m7B8 = v_stack_m6B0;
    v_stack_m7C0 = 0;
    v_stack_m7C8 = 0;
    v_stack_m7D0 = 0;
    v_stack_m7D8 = 0;
    v_stack_m7E0 = 0;
    v_stack_m7E8 = 96;
    v_stack_m7F0 = 1;
    v_stack_m7F8 = 5;
    v_stack_m800 = 128;
    v_stack_m808 = 0;
    result = IoCreateFileEx(v_stack_m548, a2, v_stack_m708, v_stack_m678);
    if (!sign_flag) goto loc_00AEAD1F;
    v_rsi = (unsigned int)((unsigned int)(result));
    if (v_stack_m54C != 0) {
        result = v_stack_m6B0;
        v_stack_m7B8 = result;
        v_stack_m7C0 = 0;
        v_stack_m7C8 = 0;
        v_stack_m7D0 = 0;
        v_stack_m7D8 = 0;
        v_stack_m7E0 = 0;
        v_stack_m7E8 = 96;
        v_stack_m7F0 = 1;
        v_stack_m7F8 = 5;
        v_stack_m800 = 128;
        v_stack_m808 = 0;
        a4 = v_stack_m678;
        a3 = v_stack_m708;
        a2 = 0x100020ULL;
        a1 = v_stack_m548;
        result = IoCreateFileEx(a1, a2, a3, a4);
        v_rsi = (unsigned int)(result);
    }
    if (!sign_flag) goto loc_00AEAD41;
    v_stack_m548 = 0;
loc_00AEAD2D:
    a3 = 0;
    result = PspUpdateCreateInfo(1, v_stack_m5F8, a3, a4);
    goto loc_00AEB7E1;
loc_00AEAD41:
    v_stack_m750 = 0;
    v_stack_m800 = 0;
    v_stack_m808 = v_stack_m750;
    a4 = 0;
    result = ObReferenceObjectByHandle(v_stack_m548, (unsigned int)(0x100020ULL), *(unsigned __int64 *)(v_rip + 5094808), a4);
    v_stack_m540 = v_stack_m750;
    if (!sign_flag) goto loc_00AEAD8F;
    v_stack_m540 = 0;
    goto loc_00AEB802;
loc_00AEAD8F:
    v_stack_m6F8 = 0;
    v_stack_m768 = (unsigned int)(v_stack_m7A1 * 4 + 1);
    result = Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline(v_stack_m548, (unsigned int)(0x100020ULL), *(unsigned __int64 *)(v_rip + 5094808), a4);
    if ((unsigned int)(result) == 0) goto loc_00AEAE9A;
    v_stack_m800 = v_stack_m758;
    v_stack_m808 = (unsigned int)((unsigned int)(v_stack_m46C));
    result = SeDuplicateTokenWithPredictedClaims(v_stack_m558, v_stack_m540, (unsigned int)(v_stack_m470), v_stack_m468);
    if (sign_flag) goto loc_00AEB7E1;
    if (v_stack_m758 == 0) goto loc_00AEAE00;
    v_stack_m7A8 = 1;
    v_stack_m7A0 = 1;
    goto loc_00AEAE14;
loc_00AEAE00:
    v_stack_m7A8 = 0;
    v_stack_m7A0 = 0;
    v_stack_m758 = v_stack_m558;
loc_00AEAE14:
    v_stack_m768 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m768))));
    if (((v_stack_m470) & (8)) == 0) goto loc_00AEAEED;
    result = PsDisableImpersonation(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m6C0, (unsigned int)(v_stack_m470), v_stack_m468);
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5172270), (unsigned __int8)((unsigned int)(v_stack_m7A8)), (unsigned int)(v_stack_m470), v_stack_m468);
    if ((unsigned __int8)(result) != 0) goto loc_00AEAE76;
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_00AEAB19;
    result = PsRestoreImpersonation(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m6C0, (unsigned int)(v_stack_m470), v_stack_m468);
    goto loc_00AEAB19;
loc_00AEAE76:
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = v_stack_m6C0;
        result = PsRestoreImpersonation(a1, a2, (unsigned int)(v_stack_m470), v_stack_m468);
    }
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m768)))) | (8));
    goto loc_00AEAEEA;
loc_00AEAE9A:
    if (v_stack_m468 == 0) goto loc_00AEAED1;
    result = SeDuplicateTokenAndAddOriginClaim(v_stack_m558, v_stack_m468, (unsigned int)(v_stack_m46C), v_stack_m758);
    a1 = (unsigned __int8)((unsigned int)(v_stack_m7A8));
    if (!sign_flag) { a1 = 1; }
    v_stack_m7A8 = (unsigned int)(a1);
    v_stack_m7A0 = (unsigned __int8)(a1);
    goto loc_00AEAED4;
loc_00AEAED1:
loc_00AEAED4:
    v_stack_m768 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m768))));
    if ((unsigned __int8)((unsigned int)(v_stack_m7A8)) != 0) goto loc_00AEAEED;
    v_stack_m758 = v_stack_m558;
loc_00AEAEEA:
    v_stack_m768 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m768))));
loc_00AEAEED:
    v_stack_m800 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m768))));
    v_stack_m808 = v_stack_m548;
    result = MmCreateSpecialImageSection(v_stack_m538, v_stack_m708, v_stack_m758, (unsigned __int8)(v_stack_m7A4));
    if (sign_flag) goto loc_00AEB10F;
loc_00AEAF21:
    v_stack_m750 = 0;
    v_stack_m800 = 0;
    v_stack_m808 = v_stack_m750;
    a4 = 0;
    result = ObReferenceObjectByHandle(v_stack_m538, 8, *(unsigned __int64 *)(v_rip + 5094576), a4);
    v_stack_m528 = v_stack_m750;
    if (sign_flag) goto loc_00AEB103;
    result = PspGetProcessProtectionRequirementsFromImage(v_stack_m750, (unsigned __int8)(v_stack_m7A2), v_stack_m79E, a4);
    if (sign_flag) goto loc_00AEB7E1;
    if (((unsigned __int8)(v_stack_m79E)) == ((unsigned __int8)(v_stack_m7A2))) goto loc_00AEB061;
    v_stack_m7F8 = v_stack_m7A2;
    v_stack_m800 = v_stack_m79F;
    v_stack_m808 = v_stack_m7A3;
    result = SeQuerySigningPolicy(v_stack_m558, v_stack_m508, 1, v_stack_m79E);
    if (sign_flag) goto loc_00AEB7E1;
    if (((unsigned __int8)(v_stack_m7A3)) == ((unsigned __int8)(v_stack_m7A4))) goto loc_00AEB05E;
    a1 = (unsigned __int8)(((unsigned __int8)(v_stack_m7A4)) & (48));
    if (condition_is_equal) goto loc_00AEAFE0;
    result = (unsigned __int8)(((unsigned __int8)(v_stack_m7A3)) & (48));
    if (((unsigned __int8)(result)) != ((unsigned __int8)(a1))) goto loc_00AEB7DC;
loc_00AEAFE0:
    result = SeCompareSigningLevels((unsigned __int8)(v_stack_m7A3), (unsigned __int8)(v_stack_m7A4), 1, v_stack_m79E);
    if ((unsigned int)(result) == 0) goto loc_00AEB7DC;
    a2 = 0;
    result = ObCloseHandle(v_stack_m538, a2, 1, v_stack_m79E);
    result = ObfDereferenceObject(v_stack_m528, a2, 1, v_stack_m79E);
    v_stack_m538 = 0;
    v_stack_m528 = 0;
    v_stack_m800 = (unsigned int)((unsigned int)(v_stack_m768));
    v_stack_m808 = v_stack_m548;
    result = MmCreateSpecialImageSection(v_stack_m538, v_stack_m708, v_stack_m758, (unsigned __int8)(v_stack_m7A3));
    if (sign_flag) goto loc_00AEB10F;
    goto loc_00AEAF21;
loc_00AEB05E:
loc_00AEB061:
    v_stack_m808 = (unsigned __int8)(v_stack_m7A2);
    result = PspValidateCreateProcessProtection(v_stack_m760, v_stack_m5F8, (unsigned __int8)((unsigned int)(v_stack_m7A8)), (unsigned int)((unsigned int)(v_r13)));
    if (sign_flag) goto loc_00AEB7E1;
    if (condition_is_below) goto loc_00AEB0AE;
    result = (unsigned __int8)(((unsigned __int8)(v_stack_m7A2)) & (7));
    if (((unsigned __int8)(result)) == 1) goto loc_00AEB0B5;
    result = PspCheckForInvalidAccessByProtection((unsigned __int8)((unsigned int)(v_stack_m7A8)), *(unsigned __int8 *)(v_stack_m760 + 1530), (unsigned __int8)(v_stack_m7A2), (unsigned int)((unsigned int)(v_r13)));
    if ((unsigned __int8)(result) != 0) {
    }
    result = PspGetProcessParameterOverrides(v_stack_m5F8, v_stack_m728, (unsigned __int8)(v_stack_m7A2), (unsigned int)((unsigned int)(v_r13)));
    result = PspCaptureProcessParameters((unsigned __int8)((unsigned int)(v_stack_m7A8)), v_stack_m738, v_stack_m5F8, (unsigned int)((unsigned int)(v_r13)));
    if (!sign_flag) goto loc_00AEB0ED;
    goto loc_00AEB7E1;
loc_00AEB0ED:
    v_stack_m738 = v_stack_m78;
    v_stack_m7A3 = (unsigned __int8)(v_stack_m79F);
    goto loc_00AEB1CE;
loc_00AEB103:
    v_stack_m528 = 0;
    goto loc_00AEB7E1;
loc_00AEB10F:
    v_stack_m538 = 0;
    goto loc_00AEAD2D;
loc_00AEB120:
    if (v_stack_m7A2 != v_stack_m760) goto loc_00AEB7DC;
    if ((unsigned __int8)((unsigned int)(v_stack_m7A8)) == 0) goto loc_00AEB7DC;
    if (v_stack_m738 != 0) goto loc_00AEB7DC;
    if (((v_stack_m5E7) & (12)) != 0) goto loc_00AEB7DC;
    if (sign_flag) goto loc_00AEB7DC;
    if (((v_stack_m5F0) & ((unsigned __int8)(v_stack_m7A3))) != 0) goto loc_00AEB7DC;
    if ((((unsigned __int8)(v_stack_m5E8)) & (16)) != 0) goto loc_00AEB7DC;
    result = (unsigned __int8)((v_stack_m5E8) & (251));
    v_stack_m5E8 = (unsigned __int8)(result);
    v_stack_m7A3 = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m748 + 1529));
    if ((((unsigned __int8)(v_r13)) & (64)) == 0) goto loc_00AEB1A7;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_m7A2 + 1530))) & (7)) != 0) goto loc_00AEB1A7;
    goto loc_00AEB7E1;
loc_00AEB1A7:
    v_stack_m808 = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m7A2 + 1530));
    result = PspValidateCreateProcessProtection(v_stack_m760, v_stack_m5F8, (unsigned __int8)((unsigned int)(v_stack_m7A8)), (unsigned int)((unsigned int)(v_r13)));
    if (sign_flag) goto loc_00AEB7E1;
    v_stack_m738 = 0;
loc_00AEB1CE:
    a1 = (v_stack_m560 != 0) ? 1 : 0;
    v_stack_m7B8 = v_stack_m798;
    v_stack_m7C0 = v_stack_m788;
    v_stack_m7C8 = v_stack_m728;
    v_stack_m7D0 = (unsigned int)(a1);
    v_stack_m7D8 = v_stack_m5F8;
    v_stack_m7E0 = 0;
    v_stack_m7E8 = (unsigned int)(v_r13);
    v_stack_m7F0 = v_stack_m558;
    v_stack_m7F8 = v_stack_m528;
    v_stack_m800 = (unsigned __int8)(v_stack_m7A3);
    v_stack_m808 = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m748 + 1528));
    result = PspAllocateProcess(v_stack_m748, (unsigned __int8)((unsigned int)(v_stack_m7A8)), v_stack_m720, (unsigned __int8)(*(unsigned __int8 *)(v_stack_m7A2 + 1530)));
    if (sign_flag) goto loc_00AEB7E1;
    result = -(v_stack_m528);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(result))) & (0xFFFFFFF0ULL));
    v_rsi = (unsigned int)((v_rsi) + (0x10001BULL));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m798 + 1876))) & (0x4000ULL));
    result = (unsigned int)(-((unsigned int)((unsigned int)(a1))));
    result = (unsigned int)((result) & (0x800ULL));
    v_stack_m720 = result;
    if ((unsigned int)(a1) != 0) {
        v_rsi = (unsigned int)((v_rsi) | (0x100040ULL));
    }
    result = RtlGetExtendedContextLength2((unsigned int)((unsigned int)(v_rsi)), v_stack_m770, result, (unsigned __int8)(*(unsigned __int8 *)(v_stack_m7A2 + 1530)));
    v_stack_m750 = 0;
    if (v_stack_m7A1 != 0) goto loc_00AEB39F;
    if (((unsigned int)(v_stack_m770) + 15) <= ((unsigned int)(v_stack_m770))) {
    }
    result = ((unsigned int)(v_stack_m770) + 15) & (-16);
    result = _chkstk((unsigned int)((unsigned int)(v_rsi)), v_stack_m770, (unsigned int)(v_stack_m770), (unsigned __int8)(*(unsigned __int8 *)(v_stack_m7A2 + 1530)));
    v_rsp = (v_rsp) - (result);
    v_stack_m750 = v_stack_m7A8;
    a2 = 0;
    result = memset(v_stack_m7A8, a2, (unsigned int)(v_stack_m770), (unsigned __int8)(*(unsigned __int8 *)(v_stack_m7A2 + 1530)));
    result = RtlInitializeExtendedContext2(v_stack_m7A8, (unsigned int)((unsigned int)(v_rsi)), v_stack_m6D8, v_stack_m720);
    if (v_stack_m528 == 0) goto loc_00AEB348;
    result = (unsigned int)(v_stack_m50C);
    if ((*(unsigned __int64 *)(v_stack_m798 + 784)) == 0) {
        result = *(unsigned __int64 *)(v_stack_m798 + 736);
    }
    v_stack_m808 = result;
    result = PspCreateUserContext(v_stack_m7A8, 1, *(unsigned __int64 *)(v_rip + 5095749), v_stack_m5C0);
    goto loc_00AEB38B;
loc_00AEB348:
    v_stack_m808 = 1;
    a3 = 0;
    result = PspGetContextThreadInternal(v_stack_m740, v_stack_m7A8, a3, 1);
    if (!sign_flag) goto loc_00AEB382;
    result = PspUnlockProcessExclusive(v_stack_m798, v_stack_m740, a3, 1);
    a2 = 0;
    result = PspRundownSingleProcess(v_stack_m798, a2, a3, 1);
    goto loc_00AEB7E1;
loc_00AEB382:
    *(unsigned __int64 *)(v_stack_m7A8 + 120) = 297;
loc_00AEB38B:
    v_stack_m668 = v_stack_m648;
    goto loc_00AEB3A2;
loc_00AEB39F:
loc_00AEB3A2:
    result = ObfReferenceObjectWithTag(v_stack_m798, (unsigned int)(0x72437350ULL), a3, 1);
    if (0 != 0) {
        *(unsigned __int8 *)(0) = 0;
        result = v_stack_m5B0;
        a1 = 0x40000ULL;
        if (result < a1) { result = a1; }
        *(unsigned __int64 *)(0 + 24) = result;
        result = v_stack_m5A8;
        *(unsigned __int64 *)(0 + 16) = result;
        result = v_stack_m5B8;
        *(unsigned __int64 *)(0 + 8) = result;
    }
    v_stack_m770 = 0;
    result = PspMapThreadCreationFlags((unsigned int)(a8), v_stack_m790, a3, 1);
    if (v_stack_m788 != 0) {
        v_stack_m770 = 2;
    }
    if (v_stack_m787 != 0) {
    }
    if (v_stack_m7A1 != 0) {
    }
    v_stack_m7D0 = v_stack_m208;
    v_stack_m7D8 = 0;
    v_stack_m7E0 = v_stack_m730;
    v_stack_m7E8 = v_stack_m790;
    v_stack_m7F0 = 0;
    v_stack_m7F8 = 0;
    v_stack_m800 = v_stack_m668;
    v_stack_m808 = v_stack_m750;
    result = PspAllocateThread(v_stack_m798, v_stack_m6D0, (unsigned __int8)((unsigned int)(v_stack_m7A8)), v_stack_m5F8);
    if (!sign_flag) goto loc_00AEB4A8;
    result = PspUnlockProcessExclusive(v_stack_m798, v_stack_m740, (unsigned __int8)((unsigned int)(v_stack_m7A8)), v_stack_m5F8);
    a2 = 0;
    result = PspRundownSingleProcess(v_stack_m798, a2, (unsigned __int8)((unsigned int)(v_stack_m7A8)), v_stack_m5F8);
    goto loc_00AEB6B1;
loc_00AEB4A8:
    result = PsTestProtectedProcessIncompatibility((unsigned __int8)((unsigned int)(v_stack_m7A8)), v_stack_m760, v_stack_m798, v_stack_m5F8);
    if ((unsigned __int8)(result) == 0) goto loc_00AEB54F;
    result = Feature_ID51912085__private_IsEnabledPreCheck((unsigned __int8)((unsigned int)(v_stack_m7A8)), v_stack_m760, v_stack_m798, v_stack_m5F8);
    if (((v_stack_m780) & ((unsigned int)((unsigned int)(0x2000000ULL)))) == 0) goto loc_00AEB512;
    result = ((unsigned __int8)(*(unsigned __int8 *)(v_stack_m7A2 + 1530))) >> (4);
    result = (unsigned int)(~((unsigned int)(*(unsigned int *)(v_rip + 396699 + result + result * 2 * 4 + 4))));
    result = (unsigned int)((result) & (0x1FFFFFULL));
    result = (unsigned int)((result) | (v_stack_m780));
    v_stack_m780 = (unsigned int)(result);
    if (v_stack_m570 == 0) goto loc_00AEB50C;
    if (v_stack_m760 == v_stack_m570) {
        result = (unsigned int)((result) | (1));
        v_stack_m780 = (unsigned int)(result);
    }
    if (((v_stack_m778) & ((unsigned int)((unsigned int)(0x2000000ULL)))) == 0) goto loc_00AEB54F;
    result = ((unsigned __int8)(*(unsigned __int8 *)(v_stack_m7A2 + 1530))) >> (4);
    result = (unsigned int)(~((unsigned int)(*(unsigned int *)(v_rip + 396699 + result + result * 2 * 4 + 8))));
    result = (unsigned int)((result) & (0x1FFFFFULL));
    result = (unsigned int)((result) | (v_stack_m778));
    v_stack_m778 = (unsigned int)(result);
    if (v_stack_m570 == 0) goto loc_00AEB549;
    if (v_stack_m760 == v_stack_m570) {
        result = (unsigned int)((result) | (1));
        v_stack_m778 = (unsigned int)(result);
    }
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(v_stack_m570, v_rip + 396699, (unsigned int)(0x2000000ULL), v_stack_m5F8);
    if ((unsigned int)(result) == 0) goto loc_00AEB5A5;
    result = SeAdjustAntiTamperCreatorAccess(v_stack_m798, (unsigned __int8)((unsigned int)(v_stack_m7A8)), v_stack_m780, v_stack_m5F8);
    if (!sign_flag) goto loc_00AEB58F;
loc_00AEB56E:
    result = PspUnlockProcessExclusive(v_stack_m798, v_stack_m740, v_stack_m780, v_stack_m5F8);
    a2 = 0;
    result = PspRundownSingleProcess(v_stack_m798, a2, v_stack_m780, v_stack_m5F8);
loc_00AEB586:
    goto loc_00AEB6A8;
loc_00AEB58F:
    result = SeAdjustAntiTamperCreatorAccess(v_stack_m730, (unsigned __int8)((unsigned int)(v_stack_m7A8)), v_stack_m778, v_stack_m5F8);
    if (sign_flag) goto loc_00AEB56E;
loc_00AEB5A5:
    if (v_stack_m520 == 0) goto loc_00AEB5B7;
    result = (v_stack_m520) + (112);
    goto loc_00AEB5BA;
loc_00AEB5B7:
loc_00AEB5BA:
    v_stack_m7F0 = v_stack_m398;
    v_stack_m7F8 = 0;
    v_stack_m800 = (unsigned int)((unsigned int)(v_stack_m770));
    v_stack_m808 = v_stack_m568;
    result = PspInsertProcess(v_stack_m798, v_stack_m748, (unsigned int)(v_stack_m780), (unsigned int)((unsigned int)(v_r13)));
    v_stack_m7D8 = v_stack_m5E0;
    v_stack_m7E0 = v_stack_m718;
    v_stack_m7E8 = v_stack_m208;
    v_stack_m7F0 = 0;
    v_stack_m7F8 = v_stack_m5F8;
    v_stack_m800 = 0;
    v_stack_m808 = (unsigned int)((unsigned int)(v_stack_m778));
    result = PspInsertThread(v_stack_m730, v_stack_m798, v_stack_m648, v_stack_m790);
    result = KiLeaveCriticalRegionUnsafe(v_stack_m740, v_stack_m798, v_stack_m648, v_stack_m790);
    if (!sign_flag) goto loc_00AEB66E;
    a2 = 0;
    result = PspRundownSingleProcess(v_stack_m798, a2, v_stack_m648, v_stack_m790);
    goto loc_00AEB586;
loc_00AEB66E:
    if (sign_flag) goto loc_00AEB689;
    result = PsGetProcessServerSilo(v_stack_m798, a2, v_stack_m648, v_stack_m790);
    if (result == v_stack_m450) goto loc_00AEB6C4;
loc_00AEB689:
loc_00AEB68D:
    result = SeDeleteAccessState(v_stack_m398, a2, v_stack_m648, v_stack_m790);
    if (sign_flag) {
        a2 = (unsigned int)((unsigned int)(0xC000022DULL));
        a1 = v_stack_m798;
        result = PsTerminateProcess(a1, a2, v_stack_m648, v_stack_m790);
    }
    result = ObfDereferenceObject(v_stack_m730, a2, v_stack_m648, v_stack_m790);
loc_00AEB6B1:
    result = ObfDereferenceObjectWithTag(v_stack_m798, (unsigned int)(0x72437350ULL), v_stack_m648, v_stack_m790);
    goto loc_00AEB7E5;
loc_00AEB6C4:
    result = PspCreateObjectHandle(v_stack_m798, v_stack_m398, *(unsigned __int64 *)(v_rip + 5092301), v_stack_m790);
    if (sign_flag) goto loc_00AEB79D;
    if (v_stack_m5D0 != 0) {
        *(unsigned __int64 *)(v_stack_m5D0) = v_xmm0;
        *(unsigned __int64 *)(v_stack_m5D0 + 16) = v_xmm1;
        *(unsigned __int64 *)(v_stack_m5D0 + 32) = v_xmm0;
        *(unsigned __int64 *)(v_stack_m5D0 + 48) = v_xmm1;
    }
    *(unsigned __int64 *)(v_stack_m710) = v_stack_m210;
    goto loc_00AEB74E;
loc_00AEB74E:
    if (sign_flag) goto loc_00AEB771;
    result = PspUpdateCreateInfo(6, v_stack_m5F8, v_stack_m798, v_stack_m790);
    if (!sign_flag) goto loc_00AEB68D;
loc_00AEB771:
    if (((v_stack_m218) & (512)) != 0) goto loc_00AEB78C;
    if (((*(unsigned int *)(v_stack_m760 + 1532)) & (0x1000ULL)) != 0) {
        a2 = 0;
    }
    result = ObCloseHandle(v_stack_m210, a2, v_stack_m798, v_stack_m790);
    goto loc_00AEB7A1;
loc_00AEB79D:
loc_00AEB7A1:
    if (!sign_flag) goto loc_00AEB68D;
    if (((v_stack_m88) & (512)) != 0) goto loc_00AEB7C5;
    v_r14 = 1;
    if (((*(unsigned int *)(v_stack_m760 + 1532)) & (0x1000ULL)) != 0) {
        v_r14 = 0;
    }
    result = ObCloseHandle(v_stack_m80, (unsigned __int8)(v_r14), v_stack_m798, v_stack_m790);
    goto loc_00AEB68D;
loc_00AEB7DC:
loc_00AEB7E1:
loc_00AEB7E5:
    if (v_stack_m540 == 0) goto loc_00AEB802;
    result = *(unsigned __int64 *)(v_rip + 4298520);
    if (*(unsigned __int64 *)(v_rip + 4298520) != 0) {
        result = guard_dispatch_icall(v_stack_m540, (unsigned __int8)(v_r14), v_stack_m798, v_stack_m790);
    }
    result = PspDeleteMemoryPartitionContext(v_stack_m728, (unsigned __int8)(v_r14), v_stack_m798, v_stack_m790);
    result = PspDeleteCreateProcessContext(v_stack_m5F8, (unsigned __int8)(v_r14), v_stack_m798, v_stack_m790);
    if (v_stack_m6A8 != 0) {
        result = FsRtlFreeExtraCreateParameterList(v_stack_m6A8, (unsigned __int8)(v_r14), v_stack_m798, v_stack_m790);
    }
    if ((unsigned __int8)((unsigned int)(v_stack_m7A8)) != 0) {
        a1 = v_stack_m758;
        result = ObfDereferenceObject(a1, (unsigned __int8)(v_r14), v_stack_m798, v_stack_m790);
    }
    goto loc_00AEB844;
loc_00AEB83F:
loc_00AEB844:
    a1 = (v_stack_m58) ^ (v_stack_m7A8);
    result = _security_check_cookie(a1, (unsigned __int8)(v_r14), v_stack_m798, v_stack_m790);
    return result;
loc_00AEB868:
    result = ExRaiseDatatypeMisalignment(a1, (unsigned __int8)(v_r14), v_stack_m798, v_stack_m790);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtCreateUserProcess(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6, uint32_t Arg7, uint32_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint8_t v_stack_m214;
    uint32_t v_stack_m218;
    uint64_t v_stack_m398;
    uint64_t v_stack_m40;
    uint64_t v_stack_m450;
    uint64_t v_stack_m468;
    uint32_t v_stack_m46C;
    uint32_t v_stack_m470;
    uint32_t v_stack_m47C;
    uint64_t v_stack_m488;
    uint64_t v_stack_m490;
    uint64_t v_stack_m508;
    uint32_t v_stack_m50C;
    uint64_t v_stack_m520;
    uint64_t v_stack_m528;
    uint64_t v_stack_m538;
    uint64_t v_stack_m540;
    uint64_t v_stack_m548;
    uint32_t v_stack_m54C;
    uint64_t v_stack_m558;
    uint64_t v_stack_m560;
    uint64_t v_stack_m568;
    uint64_t v_stack_m570;
    uint64_t v_stack_m578;
    uint64_t v_stack_m58;
    uint64_t v_stack_m590;
    uint64_t v_stack_m5A0;
    uint64_t v_stack_m5A8;
    uint64_t v_stack_m5B0;
    uint32_t v_stack_m5B8;
    uint64_t v_stack_m5C0;
    uint64_t v_stack_m5D0;
    uint64_t v_stack_m5E0;
    uint8_t v_stack_m5E7;
    uint8_t v_stack_m5E8;
    uint64_t v_stack_m5F0;
    uint8_t v_stack_m5F7;
    uint64_t v_stack_m5F8;
    uint8_t v_stack_m60;
    uint64_t v_stack_m648;
    uint64_t v_stack_m658;
    uint64_t v_stack_m668;
    uint64_t v_stack_m678;
    uint64_t v_stack_m68;
    uint64_t v_stack_m688;
    uint64_t v_stack_m690;
    uint64_t v_stack_m6A0;
    uint64_t v_stack_m6A8;
    uint16_t v_stack_m6AA;
    uint32_t v_stack_m6AE;
    uint64_t v_stack_m6B0;
    uint64_t v_stack_m6C0;
    uint64_t v_stack_m6C8;
    uint64_t v_stack_m6D0;
    uint64_t v_stack_m6D8;
    uint32_t v_stack_m6E0;
    uint64_t v_stack_m6E8;
    uint32_t v_stack_m6F0;
    uint64_t v_stack_m6F8;
    uint64_t v_stack_m700;
    uint64_t v_stack_m708;
    uint64_t v_stack_m710;
    uint64_t v_stack_m718;
    uint64_t v_stack_m720;
    uint64_t v_stack_m728;
    uint64_t v_stack_m730;
    uint64_t v_stack_m738;
    uint64_t v_stack_m740;
    uint64_t v_stack_m748;
    uint64_t v_stack_m750;
    uint64_t v_stack_m758;
    uint64_t v_stack_m760;
    uint64_t v_stack_m768;
    uint32_t v_stack_m770;
    uint32_t v_stack_m778;
    uint64_t v_stack_m78;
    uint32_t v_stack_m780;
    uint8_t v_stack_m787;
    uint16_t v_stack_m788;
    uint8_t v_stack_m78C;
    uint32_t v_stack_m790;
    uint64_t v_stack_m798;
    uint8_t v_stack_m79E;
    uint8_t v_stack_m79F;
    uint8_t v_stack_m7A0;
    uint8_t v_stack_m7A1;
    uint8_t v_stack_m7A2;
    uint8_t v_stack_m7A3;
    uint8_t v_stack_m7A4;
    uint64_t v_stack_m7A8;
    uint64_t v_stack_m7B8;
    uint32_t v_stack_m7C0;
    uint64_t v_stack_m7C8;
    uint32_t v_stack_m7D0;
    uint32_t v_stack_m7D8;
    uint64_t v_stack_m7E0;
    uint32_t v_stack_m7E8;
    uint64_t v_stack_m7F0;
    uint64_t v_stack_m7F8;
    uint64_t v_stack_m80;
    uint64_t v_stack_m800;
    uint32_t v_stack_m808;
    uint32_t v_stack_m88;

    local_rsp = (local_rsp) - (0x7E8ULL);
    result = (*(uint64_t *)(v_rip + 0x32009D)) ^ (v_stack_m7A8);
    v_stack_m58 = result;
    v_stack_m718 = Arg2;
    v_stack_m710 = Arg1;
    v_stack_m720 = Arg5;
    v_stack_m780 = Arg3;
    v_stack_m778 = Arg4;
    v_stack_m6D0 = Arg6;
    v_stack_m738 = Arg9;
    local_rdi = 0;
    v_stack_m788 = 0;
    v_stack_m790 = 0;
    result = 0;
    v_stack_m6AE = 0;
    v_stack_m6AA = 0;
    v_stack_m678 = v_xmm0;
    v_stack_m798 = 0;
    v_stack_m730 = 0;
    v_stack_m708 = v_xmm0;
    v_stack_m6F8 = v_xmm0;
    v_stack_m6E8 = 0;
    v_stack_m6E0 = 0;
    v_stack_m748 = 0;
    Arg2 = 0;
    result = memset(v_stack_m398, Arg2, 400, Arg4);
    v_stack_m688 = v_xmm0;
    v_stack_m79E = 0;
    v_stack_m7A4 = 0;
    v_stack_m79F = 0;
    v_stack_m7A3 = 0;
    result = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    Arg2 = 0;
    result = memset(v_stack_m208, Arg2, 400, Arg4);
    v_stack_m6D8 = 0;
    v_stack_m770 = 0;
    v_stack_m768 = 0;
    result = 0;
    v_stack_m668 = v_xmm0;
    v_stack_m658 = 0;
    v_stack_m6C0 = v_xmm0;
    v_stack_m740 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m760 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_m6C8 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_m78C = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m728 = 0;
    v_stack_m758 = 0;
    v_stack_m7A8 = 0;
    v_stack_m7A0 = 0;
    v_stack_m7A1 = 0;
    result = 0;
    v_stack_m6B0 = v_xmm0;
    v_stack_m6A0 = v_xmm0;
    v_stack_m690 = 0;
    Arg2 = 0;
    result = memset(v_stack_m648, Arg2, local_rdi + 72, Arg4);
    if ((((uint32_t)((uint32_t)(Arg7))) & (0xFF317838ULL)) != 0) goto loc_00AEB83F;
    if (((Arg8) & (0xFFFFFFFEULL)) != 0) goto loc_00AEB83F;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg7)))) & ((uint32_t)((uint32_t)(0x8400ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x8400ULL)))) goto loc_00AEA867;
    goto loc_00AEB844;
loc_00AEA867:
    v_stack_m214 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    result = (uint32_t)(0xC0000030ULL);
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) {
        Arg1 = 0;
        if (v_stack_m710 < 0) { Arg1 = v_stack_m710; }
        result = *(uint64_t *)(Arg1);
        *(uint64_t *)(Arg1) = result;
        Arg1 = 0;
        if (v_stack_m718 < 0) { Arg1 = v_stack_m718; }
        result = *(uint64_t *)(Arg1);
        *(uint64_t *)(Arg1) = result;
    }
    if (Arg5 == 0) goto loc_00AEA8E7;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AEA8CB;
    if ((((uint8_t)(Arg5)) & (3)) != 0) goto loc_00AEB868;
    if (Arg5 < 0) { Arg2 = Arg5; }
loc_00AEA8CB:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_00AEA8DC;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg5 + 0x18))) & (0x11FF2ULL));
    goto loc_00AEA8E1;
loc_00AEA8DC:
    result = (uint32_t)((result) & (0x1DF2ULL));
loc_00AEA8E1:
    v_stack_m218 = (uint32_t)(result);
loc_00AEA8E7:
    Arg2 = 0;
    result = memset(v_stack_m5F8, Arg2, 608, Arg4);
    if (Arg11 == 0) goto loc_00AEA928;
    Arg3 = 0;
    result = PspBuildCreateProcessContext(Arg11, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, v_stack_m5F8);
    if (sign_flag) goto loc_00AEB844;
loc_00AEA928:
    if ((((uint8_t)((uint32_t)(Arg7))) & (64)) == 0) goto loc_00AEA953;
    if (((v_stack_m5F0) & ((uint32_t)(0x20000ULL))) == 0) goto loc_00AEA953;
    local_r13 = (uint32_t)(Arg7);
    if (v_stack_m5F7 == 0) {
        local_r13 = (uint32_t)(((uint32_t)(Arg7)) & (0xFFFFFFBFULL));
    }
    if ((((uint8_t)(local_r13)) & (4)) != 0) goto loc_00AEA96A;
    if (((v_stack_m5F0) & (0x800ULL)) != 0) goto loc_00AEB7DC;
loc_00AEA96A:
    if (((v_stack_m5F0) & ((uint32_t)(0x20000ULL))) == 0) goto loc_00AEA97D;
    if ((((uint8_t)(local_r13)) & (64)) == 0) goto loc_00AEB7DC;
loc_00AEA97D:
    result = PspCaptureCreateInfo((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg10, v_stack_m5F8, v_stack_m5F8);
    if (sign_flag) goto loc_00AEB7E1;
    if (((v_stack_m5F0) & (1)) == 0) goto loc_00AEA9F4;
    v_stack_m7F0 = 0;
    v_stack_m7F8 = 0;
    v_stack_m800 = v_stack_m748;
    v_stack_m808 = 0x72437350ULL;
    result = ObpReferenceObjectByHandleWithTag(v_stack_m578, 1 + 127, *(uint64_t *)(v_rip + 0x4DC0E9), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (sign_flag) goto loc_00AEB7E1;
    v_stack_m570 = v_stack_m748;
    goto loc_00AEA9F8;
loc_00AEA9F4:
    v_stack_m748 = v_stack_m748;
loc_00AEA9F8:
    result = PspEstimateNewProcessServerSilo(v_stack_m748, v_stack_m488, (uint32_t)(v_stack_m47C), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    v_stack_m450 = result;
    result = (uint8_t)((v_stack_m5E7) & (12));
    if (((uint8_t)(result)) != 4) goto loc_00AEAA3E;
    if (v_stack_m748 != v_stack_m760) goto loc_00AEB7DC;
    if (((*(uint32_t *)(v_stack_m760 + 0x5FC)) & (0x1000ULL)) != 0) goto loc_00AEB7DC;
loc_00AEAA3E:
    result = PspReferenceTokenForNewProcess(v_stack_m748, v_stack_m560, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_m558);
    if (!sign_flag) goto loc_00AEAA69;
    v_stack_m558 = 0;
    goto loc_00AEB7E1;
loc_00AEAA69:
    if (v_stack_m560 == 0) goto loc_00AEAA9E;
    result = SeQueryServerSiloToken(v_stack_m558, v_stack_m768, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_m558);
    if (sign_flag) goto loc_00AEAA9E;
    result = PspIsSiloInSilo(v_stack_m768, v_stack_m450, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_m558);
    if ((uint8_t)(result) == 0) goto loc_00AEB7DC;
loc_00AEAA9E:
    if ((((uint8_t)(v_stack_m5F0)) & (32)) == 0) goto loc_00AEB120;
    result = (v_stack_m5F0) & ((uint32_t)(0x20000ULL));
    result = -(result);
    local_rbx = (uint8_t)((v_stack_m748) & (v_stack_m5F7));
    v_stack_m7A2 = (uint8_t)(local_rbx);
    if (((*(uint32_t *)(v_rip + 0x4D97F2)) & (0x40000ULL)) != 0) {
        v_stack_m688 = v_xmm0;
        v_stack_m800 = 0;
        v_stack_m808 = 0;
        Arg4 = 0;
        Arg3 = Arg4 + 16;
        Arg2 = v_stack_m688;
        Arg1 = Arg4 + 38;
        result = ZwSystemDebugControl(Arg1, Arg2, Arg3, Arg4);
    }
    if (condition_is_above_or_equal) goto loc_00AEAB23;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4EEFC0), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00AEAB23;
loc_00AEAB19:
    goto loc_00AEB7E1;
loc_00AEAB23:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) >> (6));
    Arg3 = (uint32_t)((Arg3) & (1));
    v_stack_m7F8 = v_stack_m7A2;
    v_stack_m800 = v_stack_m79F;
    v_stack_m808 = v_stack_m7A4;
    result = SeQuerySigningPolicy(v_stack_m558, v_stack_m508, Arg3, (uint8_t)(local_rbx));
    if (sign_flag) goto loc_00AEB7E1;
    if ((((uint32_t)((uint32_t)(0x20000ULL))) & ((uint32_t)(local_r13))) == 0) goto loc_00AEAB8D;
    result = SeCompareSigningLevels(v_stack_m7A4, 8, Arg3, (uint8_t)(local_rbx));
    local_r12 = v_stack_m7A4;
    if ((uint32_t)(result) == 0) { local_r12 = 8; }
    v_stack_m7A4 = (uint8_t)(local_r12);
    goto loc_00AEAB91;
loc_00AEAB8D:
loc_00AEAB91:
    v_stack_m708 = 48;
    v_stack_m700 = 0;
    result = (uint32_t)(0x640ULL);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232))) != 1) { result = 576; }
    v_stack_m6F0 = (uint32_t)(result);
    v_stack_m6F8 = v_stack_m508;
    v_stack_m6E8 = v_xmm0;
    result = *(uint64_t *)(v_rip + 0x4ED7F6);
    local_rsi = 0;
    if (*(uint64_t *)(v_rip + 0x4ED7F6) != 0) {
        Arg1 = v_stack_m558;
        result = guard_dispatch_icall(Arg1, 8, Arg3, (uint8_t)(local_rbx));
        local_rsi = (uint32_t)(result);
    }
    if (sign_flag) goto loc_00AEB7E1;
    v_stack_m808 = v_stack_m728;
    result = PspGetMemoryPartitionContext(v_stack_m748, (uint32_t)((uint32_t)(local_r13)), v_stack_m488, (uint32_t)(v_stack_m47C));
    if (sign_flag) goto loc_00AEB7E1;
    result = PspCreateUserProcessEcp(v_stack_m6B0, v_stack_m558, v_stack_m488, (uint32_t)(v_stack_m47C));
    if (sign_flag) goto loc_00AEB7E1;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m54C)) | (0x100020ULL));
    v_stack_m7B8 = v_stack_m6B0;
    v_stack_m7C0 = 0;
    v_stack_m7C8 = 0;
    v_stack_m7D0 = 0;
    v_stack_m7D8 = 0;
    v_stack_m7E0 = 0;
    v_stack_m7E8 = 96;
    v_stack_m7F0 = 1;
    v_stack_m7F8 = 5;
    v_stack_m800 = 128;
    v_stack_m808 = 0;
    result = IoCreateFileEx(v_stack_m548, Arg2, v_stack_m708, v_stack_m678);
    if (!sign_flag) goto loc_00AEAD1F;
    local_rsi = (uint32_t)((uint32_t)(result));
    if (v_stack_m54C != 0) {
        result = v_stack_m6B0;
        v_stack_m7B8 = result;
        v_stack_m7C0 = 0;
        v_stack_m7C8 = 0;
        v_stack_m7D0 = 0;
        v_stack_m7D8 = 0;
        v_stack_m7E0 = 0;
        v_stack_m7E8 = 96;
        v_stack_m7F0 = 1;
        v_stack_m7F8 = 5;
        v_stack_m800 = 128;
        v_stack_m808 = 0;
        Arg4 = v_stack_m678;
        Arg3 = v_stack_m708;
        Arg2 = 0x100020ULL;
        Arg1 = v_stack_m548;
        result = IoCreateFileEx(Arg1, Arg2, Arg3, Arg4);
        local_rsi = (uint32_t)(result);
    }
    if (!sign_flag) goto loc_00AEAD41;
    v_stack_m548 = 0;
loc_00AEAD2D:
    Arg3 = 0;
    result = PspUpdateCreateInfo(1, v_stack_m5F8, Arg3, Arg4);
    goto loc_00AEB7E1;
loc_00AEAD41:
    v_stack_m750 = 0;
    v_stack_m800 = 0;
    v_stack_m808 = v_stack_m750;
    Arg4 = 0;
    result = ObReferenceObjectByHandle(v_stack_m548, (uint32_t)(0x100020ULL), *(uint64_t *)(v_rip + 0x4DBD98), Arg4);
    v_stack_m540 = v_stack_m750;
    if (!sign_flag) goto loc_00AEAD8F;
    v_stack_m540 = 0;
    goto loc_00AEB802;
loc_00AEAD8F:
    v_stack_m6F8 = 0;
    v_stack_m768 = (uint32_t)(v_stack_m7A1 * 4 + 1);
    result = Feature_TrustedLaunchHosts__private_IsEnabledDeviceUsageNoInline(v_stack_m548, (uint32_t)(0x100020ULL), *(uint64_t *)(v_rip + 0x4DBD98), Arg4);
    if ((uint32_t)(result) == 0) goto loc_00AEAE9A;
    v_stack_m800 = v_stack_m758;
    v_stack_m808 = (uint32_t)((uint32_t)(v_stack_m46C));
    result = SeDuplicateTokenWithPredictedClaims(v_stack_m558, v_stack_m540, (uint32_t)(v_stack_m470), v_stack_m468);
    if (sign_flag) goto loc_00AEB7E1;
    if (v_stack_m758 == 0) goto loc_00AEAE00;
    v_stack_m7A8 = 1;
    v_stack_m7A0 = 1;
    goto loc_00AEAE14;
loc_00AEAE00:
    v_stack_m7A8 = 0;
    v_stack_m7A0 = 0;
    v_stack_m758 = v_stack_m558;
loc_00AEAE14:
    v_stack_m768 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m768))));
    if (((v_stack_m470) & (8)) == 0) goto loc_00AEAEED;
    result = PsDisableImpersonation(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m6C0, (uint32_t)(v_stack_m470), v_stack_m468);
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4EEC2E), (uint8_t)((uint32_t)(v_stack_m7A8)), (uint32_t)(v_stack_m470), v_stack_m468);
    if ((uint8_t)(result) != 0) goto loc_00AEAE76;
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_00AEAB19;
    result = PsRestoreImpersonation(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m6C0, (uint32_t)(v_stack_m470), v_stack_m468);
    goto loc_00AEAB19;
loc_00AEAE76:
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg2 = v_stack_m6C0;
        result = PsRestoreImpersonation(Arg1, Arg2, (uint32_t)(v_stack_m470), v_stack_m468);
    }
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m768)))) | (8));
    goto loc_00AEAEEA;
loc_00AEAE9A:
    if (v_stack_m468 == 0) goto loc_00AEAED1;
    result = SeDuplicateTokenAndAddOriginClaim(v_stack_m558, v_stack_m468, (uint32_t)(v_stack_m46C), v_stack_m758);
    Arg1 = (uint8_t)((uint32_t)(v_stack_m7A8));
    if (!sign_flag) { Arg1 = 1; }
    v_stack_m7A8 = (uint32_t)(Arg1);
    v_stack_m7A0 = (uint8_t)(Arg1);
    goto loc_00AEAED4;
loc_00AEAED1:
loc_00AEAED4:
    v_stack_m768 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m768))));
    if ((uint8_t)((uint32_t)(v_stack_m7A8)) != 0) goto loc_00AEAEED;
    v_stack_m758 = v_stack_m558;
loc_00AEAEEA:
    v_stack_m768 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m768))));
loc_00AEAEED:
    v_stack_m800 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m768))));
    v_stack_m808 = v_stack_m548;
    result = MmCreateSpecialImageSection(v_stack_m538, v_stack_m708, v_stack_m758, (uint8_t)(v_stack_m7A4));
    if (sign_flag) goto loc_00AEB10F;
loc_00AEAF21:
    v_stack_m750 = 0;
    v_stack_m800 = 0;
    v_stack_m808 = v_stack_m750;
    Arg4 = 0;
    result = ObReferenceObjectByHandle(v_stack_m538, 8, *(uint64_t *)(v_rip + 0x4DBCB0), Arg4);
    v_stack_m528 = v_stack_m750;
    if (sign_flag) goto loc_00AEB103;
    result = PspGetProcessProtectionRequirementsFromImage(v_stack_m750, (uint8_t)(v_stack_m7A2), v_stack_m79E, Arg4);
    if (sign_flag) goto loc_00AEB7E1;
    if (((uint8_t)(v_stack_m79E)) == ((uint8_t)(v_stack_m7A2))) goto loc_00AEB061;
    v_stack_m7F8 = v_stack_m7A2;
    v_stack_m800 = v_stack_m79F;
    v_stack_m808 = v_stack_m7A3;
    result = SeQuerySigningPolicy(v_stack_m558, v_stack_m508, 1, v_stack_m79E);
    if (sign_flag) goto loc_00AEB7E1;
    if (((uint8_t)(v_stack_m7A3)) == ((uint8_t)(v_stack_m7A4))) goto loc_00AEB05E;
    Arg1 = (uint8_t)(((uint8_t)(v_stack_m7A4)) & (48));
    if (condition_is_equal) goto loc_00AEAFE0;
    result = (uint8_t)(((uint8_t)(v_stack_m7A3)) & (48));
    if (((uint8_t)(result)) != ((uint8_t)(Arg1))) goto loc_00AEB7DC;
loc_00AEAFE0:
    result = SeCompareSigningLevels((uint8_t)(v_stack_m7A3), (uint8_t)(v_stack_m7A4), 1, v_stack_m79E);
    if ((uint32_t)(result) == 0) goto loc_00AEB7DC;
    Arg2 = 0;
    result = ObCloseHandle(v_stack_m538, Arg2, 1, v_stack_m79E);
    result = ObfDereferenceObject(v_stack_m528, Arg2, 1, v_stack_m79E);
    v_stack_m538 = 0;
    v_stack_m528 = 0;
    v_stack_m800 = (uint32_t)((uint32_t)(v_stack_m768));
    v_stack_m808 = v_stack_m548;
    result = MmCreateSpecialImageSection(v_stack_m538, v_stack_m708, v_stack_m758, (uint8_t)(v_stack_m7A3));
    if (sign_flag) goto loc_00AEB10F;
    goto loc_00AEAF21;
loc_00AEB05E:
loc_00AEB061:
    v_stack_m808 = (uint8_t)(v_stack_m7A2);
    result = PspValidateCreateProcessProtection(v_stack_m760, v_stack_m5F8, (uint8_t)((uint32_t)(v_stack_m7A8)), (uint32_t)((uint32_t)(local_r13)));
    if (sign_flag) goto loc_00AEB7E1;
    if (condition_is_below) goto loc_00AEB0AE;
    result = (uint8_t)(((uint8_t)(v_stack_m7A2)) & (7));
    if (((uint8_t)(result)) == 1) goto loc_00AEB0B5;
    result = PspCheckForInvalidAccessByProtection((uint8_t)((uint32_t)(v_stack_m7A8)), *(uint8_t *)(v_stack_m760 + 0x5FA), (uint8_t)(v_stack_m7A2), (uint32_t)((uint32_t)(local_r13)));
    if ((uint8_t)(result) != 0) {
    }
    result = PspGetProcessParameterOverrides(v_stack_m5F8, v_stack_m728, (uint8_t)(v_stack_m7A2), (uint32_t)((uint32_t)(local_r13)));
    result = PspCaptureProcessParameters((uint8_t)((uint32_t)(v_stack_m7A8)), v_stack_m738, v_stack_m5F8, (uint32_t)((uint32_t)(local_r13)));
    if (!sign_flag) goto loc_00AEB0ED;
    goto loc_00AEB7E1;
loc_00AEB0ED:
    v_stack_m738 = v_stack_m78;
    v_stack_m7A3 = (uint8_t)(v_stack_m79F);
    goto loc_00AEB1CE;
loc_00AEB103:
    v_stack_m528 = 0;
    goto loc_00AEB7E1;
loc_00AEB10F:
    v_stack_m538 = 0;
    goto loc_00AEAD2D;
loc_00AEB120:
    if (v_stack_m7A2 != v_stack_m760) goto loc_00AEB7DC;
    if ((uint8_t)((uint32_t)(v_stack_m7A8)) == 0) goto loc_00AEB7DC;
    if (v_stack_m738 != 0) goto loc_00AEB7DC;
    if (((v_stack_m5E7) & (12)) != 0) goto loc_00AEB7DC;
    if (sign_flag) goto loc_00AEB7DC;
    if (((v_stack_m5F0) & ((uint8_t)(v_stack_m7A3))) != 0) goto loc_00AEB7DC;
    if ((((uint8_t)(v_stack_m5E8)) & (16)) != 0) goto loc_00AEB7DC;
    result = (uint8_t)((v_stack_m5E8) & (251));
    v_stack_m5E8 = (uint8_t)(result);
    v_stack_m7A3 = (uint8_t)(*(uint8_t *)(v_stack_m748 + 0x5F9));
    if ((((uint8_t)(local_r13)) & (64)) == 0) goto loc_00AEB1A7;
    if ((((uint8_t)(*(uint8_t *)(v_stack_m7A2 + 0x5FA))) & (7)) != 0) goto loc_00AEB1A7;
    goto loc_00AEB7E1;
loc_00AEB1A7:
    v_stack_m808 = (uint8_t)(*(uint8_t *)(v_stack_m7A2 + 0x5FA));
    result = PspValidateCreateProcessProtection(v_stack_m760, v_stack_m5F8, (uint8_t)((uint32_t)(v_stack_m7A8)), (uint32_t)((uint32_t)(local_r13)));
    if (sign_flag) goto loc_00AEB7E1;
    v_stack_m738 = 0;
loc_00AEB1CE:
    Arg1 = (v_stack_m560 != 0) ? 1 : 0;
    v_stack_m7B8 = v_stack_m798;
    v_stack_m7C0 = v_stack_m788;
    v_stack_m7C8 = v_stack_m728;
    v_stack_m7D0 = (uint32_t)(Arg1);
    v_stack_m7D8 = v_stack_m5F8;
    v_stack_m7E0 = 0;
    v_stack_m7E8 = (uint32_t)(local_r13);
    v_stack_m7F0 = v_stack_m558;
    v_stack_m7F8 = v_stack_m528;
    v_stack_m800 = (uint8_t)(v_stack_m7A3);
    v_stack_m808 = (uint8_t)(*(uint8_t *)(v_stack_m748 + 0x5F8));
    result = PspAllocateProcess(v_stack_m748, (uint8_t)((uint32_t)(v_stack_m7A8)), v_stack_m720, (uint8_t)(*(uint8_t *)(v_stack_m7A2 + 0x5FA)));
    if (sign_flag) goto loc_00AEB7E1;
    result = -(v_stack_m528);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(result))) & (0xFFFFFFF0ULL));
    local_rsi = (uint32_t)((local_rsi) + (0x10001BULL));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m798 + 0x754))) & (0x4000ULL));
    result = (uint32_t)(-((uint32_t)((uint32_t)(Arg1))));
    result = (uint32_t)((result) & (0x800ULL));
    v_stack_m720 = result;
    if ((uint32_t)(Arg1) != 0) {
        local_rsi = (uint32_t)((local_rsi) | (0x100040ULL));
    }
    result = RtlGetExtendedContextLength2((uint32_t)((uint32_t)(local_rsi)), v_stack_m770, result, (uint8_t)(*(uint8_t *)(v_stack_m7A2 + 0x5FA)));
    v_stack_m750 = 0;
    if (v_stack_m7A1 != 0) goto loc_00AEB39F;
    if (((uint32_t)(v_stack_m770) + 15) <= ((uint32_t)(v_stack_m770))) {
    }
    result = ((uint32_t)(v_stack_m770) + 15) & (-16);
    result = _chkstk((uint32_t)((uint32_t)(local_rsi)), v_stack_m770, (uint32_t)(v_stack_m770), (uint8_t)(*(uint8_t *)(v_stack_m7A2 + 0x5FA)));
    local_rsp = (local_rsp) - (result);
    v_stack_m750 = v_stack_m7A8;
    Arg2 = 0;
    result = memset(v_stack_m7A8, Arg2, (uint32_t)(v_stack_m770), (uint8_t)(*(uint8_t *)(v_stack_m7A2 + 0x5FA)));
    result = RtlInitializeExtendedContext2(v_stack_m7A8, (uint32_t)((uint32_t)(local_rsi)), v_stack_m6D8, v_stack_m720);
    if (v_stack_m528 == 0) goto loc_00AEB348;
    result = (uint32_t)(v_stack_m50C);
    if ((*(uint64_t *)(v_stack_m798 + 0x310)) == 0) {
        result = *(uint64_t *)(v_stack_m798 + 0x2E0);
    }
    v_stack_m808 = result;
    result = PspCreateUserContext(v_stack_m7A8, 1, *(uint64_t *)(v_rip + 0x4DC145), v_stack_m5C0);
    goto loc_00AEB38B;
loc_00AEB348:
    v_stack_m808 = 1;
    Arg3 = 0;
    result = PspGetContextThreadInternal(v_stack_m740, v_stack_m7A8, Arg3, 1);
    if (!sign_flag) goto loc_00AEB382;
    result = PspUnlockProcessExclusive(v_stack_m798, v_stack_m740, Arg3, 1);
    Arg2 = 0;
    result = PspRundownSingleProcess(v_stack_m798, Arg2, Arg3, 1);
    goto loc_00AEB7E1;
loc_00AEB382:
    *(uint64_t *)(v_stack_m7A8 + 0x78) = 297;
loc_00AEB38B:
    v_stack_m668 = v_stack_m648;
    goto loc_00AEB3A2;
loc_00AEB39F:
loc_00AEB3A2:
    result = ObfReferenceObjectWithTag(v_stack_m798, (uint32_t)(0x72437350ULL), Arg3, 1);
    if (0 != 0) {
        *(uint8_t *)(0) = 0;
        result = v_stack_m5B0;
        Arg1 = 0x40000ULL;
        if (result < Arg1) { result = Arg1; }
        *(uint64_t *)(0 + 0x18) = result;
        result = v_stack_m5A8;
        *(uint64_t *)(0 + 0x10) = result;
        result = v_stack_m5B8;
        *(uint64_t *)(0 + 0x8) = result;
    }
    v_stack_m770 = 0;
    result = PspMapThreadCreationFlags((uint32_t)(Arg8), v_stack_m790, Arg3, 1);
    if (v_stack_m788 != 0) {
        v_stack_m770 = 2;
    }
    if (v_stack_m787 != 0) {
    }
    if (v_stack_m7A1 != 0) {
    }
    v_stack_m7D0 = v_stack_m208;
    v_stack_m7D8 = 0;
    v_stack_m7E0 = v_stack_m730;
    v_stack_m7E8 = v_stack_m790;
    v_stack_m7F0 = 0;
    v_stack_m7F8 = 0;
    v_stack_m800 = v_stack_m668;
    v_stack_m808 = v_stack_m750;
    result = PspAllocateThread(v_stack_m798, v_stack_m6D0, (uint8_t)((uint32_t)(v_stack_m7A8)), v_stack_m5F8);
    if (!sign_flag) goto loc_00AEB4A8;
    result = PspUnlockProcessExclusive(v_stack_m798, v_stack_m740, (uint8_t)((uint32_t)(v_stack_m7A8)), v_stack_m5F8);
    Arg2 = 0;
    result = PspRundownSingleProcess(v_stack_m798, Arg2, (uint8_t)((uint32_t)(v_stack_m7A8)), v_stack_m5F8);
    goto loc_00AEB6B1;
loc_00AEB4A8:
    result = PsTestProtectedProcessIncompatibility((uint8_t)((uint32_t)(v_stack_m7A8)), v_stack_m760, v_stack_m798, v_stack_m5F8);
    if ((uint8_t)(result) == 0) goto loc_00AEB54F;
    result = Feature_ID51912085__private_IsEnabledPreCheck((uint8_t)((uint32_t)(v_stack_m7A8)), v_stack_m760, v_stack_m798, v_stack_m5F8);
    if (((v_stack_m780) & ((uint32_t)((uint32_t)(0x2000000ULL)))) == 0) goto loc_00AEB512;
    result = ((uint8_t)(*(uint8_t *)(v_stack_m7A2 + 0x5FA))) >> (4);
    result = (uint32_t)(~((uint32_t)(*(uint32_t *)(v_rip + 0x60D9B + result + result * 2 * 4 + 0x4))));
    result = (uint32_t)((result) & (0x1FFFFFULL));
    result = (uint32_t)((result) | (v_stack_m780));
    v_stack_m780 = (uint32_t)(result);
    if (v_stack_m570 == 0) goto loc_00AEB50C;
    if (v_stack_m760 == v_stack_m570) {
        result = (uint32_t)((result) | (1));
        v_stack_m780 = (uint32_t)(result);
    }
    if (((v_stack_m778) & ((uint32_t)((uint32_t)(0x2000000ULL)))) == 0) goto loc_00AEB54F;
    result = ((uint8_t)(*(uint8_t *)(v_stack_m7A2 + 0x5FA))) >> (4);
    result = (uint32_t)(~((uint32_t)(*(uint32_t *)(v_rip + 0x60D9B + result + result * 2 * 4 + 0x8))));
    result = (uint32_t)((result) & (0x1FFFFFULL));
    result = (uint32_t)((result) | (v_stack_m778));
    v_stack_m778 = (uint32_t)(result);
    if (v_stack_m570 == 0) goto loc_00AEB549;
    if (v_stack_m760 == v_stack_m570) {
        result = (uint32_t)((result) | (1));
        v_stack_m778 = (uint32_t)(result);
    }
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(v_stack_m570, v_rip + 396699, (uint32_t)(0x2000000ULL), v_stack_m5F8);
    if ((uint32_t)(result) == 0) goto loc_00AEB5A5;
    result = SeAdjustAntiTamperCreatorAccess(v_stack_m798, (uint8_t)((uint32_t)(v_stack_m7A8)), v_stack_m780, v_stack_m5F8);
    if (!sign_flag) goto loc_00AEB58F;
loc_00AEB56E:
    result = PspUnlockProcessExclusive(v_stack_m798, v_stack_m740, v_stack_m780, v_stack_m5F8);
    Arg2 = 0;
    result = PspRundownSingleProcess(v_stack_m798, Arg2, v_stack_m780, v_stack_m5F8);
loc_00AEB586:
    goto loc_00AEB6A8;
loc_00AEB58F:
    result = SeAdjustAntiTamperCreatorAccess(v_stack_m730, (uint8_t)((uint32_t)(v_stack_m7A8)), v_stack_m778, v_stack_m5F8);
    if (sign_flag) goto loc_00AEB56E;
loc_00AEB5A5:
    if (v_stack_m520 == 0) goto loc_00AEB5B7;
    result = (v_stack_m520) + (112);
    goto loc_00AEB5BA;
loc_00AEB5B7:
loc_00AEB5BA:
    v_stack_m7F0 = v_stack_m398;
    v_stack_m7F8 = 0;
    v_stack_m800 = (uint32_t)((uint32_t)(v_stack_m770));
    v_stack_m808 = v_stack_m568;
    result = PspInsertProcess(v_stack_m798, v_stack_m748, (uint32_t)(v_stack_m780), (uint32_t)((uint32_t)(local_r13)));
    v_stack_m7D8 = v_stack_m5E0;
    v_stack_m7E0 = v_stack_m718;
    v_stack_m7E8 = v_stack_m208;
    v_stack_m7F0 = 0;
    v_stack_m7F8 = v_stack_m5F8;
    v_stack_m800 = 0;
    v_stack_m808 = (uint32_t)((uint32_t)(v_stack_m778));
    result = PspInsertThread(v_stack_m730, v_stack_m798, v_stack_m648, v_stack_m790);
    result = KiLeaveCriticalRegionUnsafe(v_stack_m740, v_stack_m798, v_stack_m648, v_stack_m790);
    if (!sign_flag) goto loc_00AEB66E;
    Arg2 = 0;
    result = PspRundownSingleProcess(v_stack_m798, Arg2, v_stack_m648, v_stack_m790);
    goto loc_00AEB586;
loc_00AEB66E:
    if (sign_flag) goto loc_00AEB689;
    result = PsGetProcessServerSilo(v_stack_m798, Arg2, v_stack_m648, v_stack_m790);
    if (result == v_stack_m450) goto loc_00AEB6C4;
loc_00AEB689:
loc_00AEB68D:
    result = SeDeleteAccessState(v_stack_m398, Arg2, v_stack_m648, v_stack_m790);
    if (sign_flag) {
        Arg2 = (uint32_t)((uint32_t)(0xC000022DULL));
        Arg1 = v_stack_m798;
        result = PsTerminateProcess(Arg1, Arg2, v_stack_m648, v_stack_m790);
    }
    result = ObfDereferenceObject(v_stack_m730, Arg2, v_stack_m648, v_stack_m790);
loc_00AEB6B1:
    result = ObfDereferenceObjectWithTag(v_stack_m798, (uint32_t)(0x72437350ULL), v_stack_m648, v_stack_m790);
    goto loc_00AEB7E5;
loc_00AEB6C4:
    result = PspCreateObjectHandle(v_stack_m798, v_stack_m398, *(uint64_t *)(v_rip + 0x4DB3CD), v_stack_m790);
    if (sign_flag) goto loc_00AEB79D;
    if (v_stack_m5D0 != 0) {
        *(uint64_t *)(v_stack_m5D0) = v_xmm0;
        *(uint64_t *)(v_stack_m5D0 + 0x10) = v_xmm1;
        *(uint64_t *)(v_stack_m5D0 + 0x20) = v_xmm0;
        *(uint64_t *)(v_stack_m5D0 + 0x30) = v_xmm1;
    }
    *(uint64_t *)(v_stack_m710) = v_stack_m210;
    goto loc_00AEB74E;
loc_00AEB74E:
    if (sign_flag) goto loc_00AEB771;
    result = PspUpdateCreateInfo(6, v_stack_m5F8, v_stack_m798, v_stack_m790);
    if (!sign_flag) goto loc_00AEB68D;
loc_00AEB771:
    if (((v_stack_m218) & (512)) != 0) goto loc_00AEB78C;
    if (((*(uint32_t *)(v_stack_m760 + 0x5FC)) & (0x1000ULL)) != 0) {
        Arg2 = 0;
    }
    result = ObCloseHandle(v_stack_m210, Arg2, v_stack_m798, v_stack_m790);
    goto loc_00AEB7A1;
loc_00AEB79D:
loc_00AEB7A1:
    if (!sign_flag) goto loc_00AEB68D;
    if (((v_stack_m88) & (512)) != 0) goto loc_00AEB7C5;
    local_r14 = 1;
    if (((*(uint32_t *)(v_stack_m760 + 0x5FC)) & (0x1000ULL)) != 0) {
        local_r14 = 0;
    }
    result = ObCloseHandle(v_stack_m80, (uint8_t)(local_r14), v_stack_m798, v_stack_m790);
    goto loc_00AEB68D;
loc_00AEB7DC:
loc_00AEB7E1:
loc_00AEB7E5:
    if (v_stack_m540 == 0) goto loc_00AEB802;
    result = *(uint64_t *)(v_rip + 0x419718);
    if (*(uint64_t *)(v_rip + 0x419718) != 0) {
        result = guard_dispatch_icall(v_stack_m540, (uint8_t)(local_r14), v_stack_m798, v_stack_m790);
    }
    result = PspDeleteMemoryPartitionContext(v_stack_m728, (uint8_t)(local_r14), v_stack_m798, v_stack_m790);
    result = PspDeleteCreateProcessContext(v_stack_m5F8, (uint8_t)(local_r14), v_stack_m798, v_stack_m790);
    if (v_stack_m6A8 != 0) {
        result = FsRtlFreeExtraCreateParameterList(v_stack_m6A8, (uint8_t)(local_r14), v_stack_m798, v_stack_m790);
    }
    if ((uint8_t)((uint32_t)(v_stack_m7A8)) != 0) {
        Arg1 = v_stack_m758;
        result = ObfDereferenceObject(Arg1, (uint8_t)(local_r14), v_stack_m798, v_stack_m790);
    }
    goto loc_00AEB844;
loc_00AEB83F:
loc_00AEB844:
    Arg1 = (v_stack_m58) ^ (v_stack_m7A8);
    result = _security_check_cookie(Arg1, (uint8_t)(local_r14), v_stack_m798, v_stack_m790);
    return result;
loc_00AEB868:
    result = ExRaiseDatatypeMisalignment(Arg1, (uint8_t)(local_r14), v_stack_m798, v_stack_m790);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AEA680&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
