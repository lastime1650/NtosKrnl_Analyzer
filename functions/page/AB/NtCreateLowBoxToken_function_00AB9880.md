# NtCreateLowBoxToken

- RVA: `0x00AB9880`–`0x00ABA414` (길이 `2,964` bytes)
- VA: `0x0000000140AB9880`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD338`
- 디코드: `667`개 명령, `2,964/2,964` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **65**; 고유 호출 대상: **43**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00AB98AD` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x00AB9955` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00AB99E2` → [SeCaptureSid](../92/SeCaptureSid_function_009276D4.md) (function, `0x009276D4`)
- `0x00AB9A58` → [SeCaptureSidAndAttributesArray](../9C/SeCaptureSidAndAttributesArray_function_009C9D70.md) (function, `0x009C9D70`)
- `0x00AB9A82` → [SeCaptureHandles](../../text/60/SeCaptureHandles_function_00609FEC.md) (function, `0x00609FEC`)
- `0x00AB9B22` → [SepCreateAppContainerToken](../../text/4F/SepCreateAppContainerToken_function_004F43AC.md) (function, `0x004F43AC`)
- `0x00AB9B39` → [SeReleaseLuidAndAttributesArray](../9C/SeReleaseLuidAndAttributesArray_function_009C7C40.md) (function, `0x009C7C40`)
- `0x00AB9B51` → [SeReleaseSid](../A2/SeReleaseSid_function_00A2EF50.md) (function, `0x00A2EF50`)
- `0x00AB9B69` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AB9C27` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00AB9CC1` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00AB9CE6` → [SeCaptureSid](../92/SeCaptureSid_function_009276D4.md) (function, `0x009276D4`)
- `0x00AB9CFA` → [SepCheckCreateAppContainer](../70/SepCheckCreateAppContainer_function_007006CC.md) (function, `0x007006CC`)
- `0x00AB9DA8` → [SeCaptureSidAndAttributesArray](../9C/SeCaptureSidAndAttributesArray_function_009C9D70.md) (function, `0x009C9D70`)
- `0x00AB9DCA` → [SeCaptureHandles](../../text/60/SeCaptureHandles_function_00609FEC.md) (function, `0x00609FEC`)
- `0x00AB9DDA` → [RtlIsPackageSid](../A5/RtlIsPackageSid_function_00A5E73C.md) (function, `0x00A5E73C`)
- `0x00AB9E1B` → [RtlIsCapabilitySid](../A5/RtlIsCapabilitySid_function_00A5ED84.md) (function, `0x00A5ED84`)
- `0x00AB9E3C` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)
- `0x00AB9E62` → [SepCapabilitiesHasAppSiloBaseSID](../../text/40/SepCapabilitiesHasAppSiloBaseSID_function_004005B0.md) (function, `0x004005B0`)
- `0x00AB9E84` → [SepIsAppSiloCapability](../../text/48/SepIsAppSiloCapability_function_0048E54C.md) (function, `0x0048E54C`)
- `0x00AB9EA2` → [RtlGetAppContainerSidType](../A7/RtlGetAppContainerSidType_function_00A72160.md) (function, `0x00A72160`)
- `0x00AB9ED1` → [SepCheckCapabilities](../AA/SepCheckCapabilities_function_00AA4A10.md) (function, `0x00AA4A10`)
- `0x00AB9EF1` → [Feature_871661881__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_871661881__private_IsEnabledDeviceUsageNoInline_function_004F4D24.md) (function, `0x004F4D24`)
- `0x00AB9F0E` → [RtlQueryElevationFlags](../A6/RtlQueryElevationFlags_function_00A60CB0.md) (function, `0x00A60CB0`)
- `0x00AB9F41` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AB9F49` → [SepLocateTokenIntegrity](../../text/41/SepLocateTokenIntegrity_function_0041BF10.md) (function, `0x0041BF10`)
- `0x00AB9F5D` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (function, `0x00468F10`)
- `0x00AB9F74` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x00AB9FA0` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x00AB9FC5` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AB9FCD` → [SepLocateTokenIntegrity](../../text/41/SepLocateTokenIntegrity_function_0041BF10.md) (function, `0x0041BF10`)
- `0x00AB9FD8` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (function, `0x00468F10`)
- `0x00AB9FEB` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x00ABA001` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00ABA006` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00ABA013` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00ABA01F` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00ABA024` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00ABA05D` → [SepDuplicateToken](../8B/SepDuplicateToken_function_008B87EC.md) (function, `0x008B87EC`)
- `0x00ABA081` → [SeSetMandatoryPolicyToken](../A5/SeSetMandatoryPolicyToken_function_00A5EDCC.md) (function, `0x00A5EDCC`)
- `0x00ABA0AD` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00ABA0C1` → [SepLocateTokenIntegrity](../../text/41/SepLocateTokenIntegrity_function_0041BF10.md) (function, `0x0041BF10`)
- `0x00ABA0DA` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x00ABA10A` → [Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline](../../text/4C/Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline_function_004C78E8.md) (function, `0x004C78E8`)
- `0x00ABA15D` → [SepSetTokenCapabilities](../9C/SepSetTokenCapabilities_function_009C9AF4.md) (function, `0x009C9AF4`)
- `0x00ABA174` → [SepSetTokenLowboxNumber](../A6/SepSetTokenLowboxNumber_function_00A64D6C.md) (function, `0x00A64D6C`)
- `0x00ABA1A8` → [SepSetTokenCachedHandles](../9A/SepSetTokenCachedHandles_function_009A939C.md) (function, `0x009A939C`)
- `0x00ABA1BF` → [SepSetTokenPackage](../A2/SepSetTokenPackage_function_00A20CB8.md) (function, `0x00A20CB8`)
- `0x00ABA1D6` → [SepAppendAceToTokenDefaultDacl](../../text/40/SepAppendAceToTokenDefaultDacl_function_004002F8.md) (function, `0x004002F8`)
- `0x00ABA207` → [SepSidInTokenSidHash](../../text/3C/SepSidInTokenSidHash_function_003C85E0.md) (function, `0x003C85E0`)
- `0x00ABA254` → [SepSidInTokenSidHash](../../text/3C/SepSidInTokenSidHash_function_003C85E0.md) (function, `0x003C85E0`)
- `0x00ABA2A4` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00ABA2A9` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00ABA2DC` → [ObInsertObjectEx](../8B/ObInsertObjectEx_function_008B97A0.md) (function, `0x008B97A0`)
- `0x00ABA2FA` → [SepAppendAceToTokenObjectAcl](../8B/SepAppendAceToTokenObjectAcl_function_008B6430.md) (function, `0x008B6430`)
- `0x00ABA30A` → [SepFinalizeTokenAcls](../8B/SepFinalizeTokenAcls_function_008B63F4.md) (function, `0x008B63F4`)
- `0x00ABA314` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00ABA369` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00ABA36E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00ABA381` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00ABA396` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x00ABA3A8` → [SeReleaseLuidAndAttributesArray](../9C/SeReleaseLuidAndAttributesArray_function_009C7C40.md) (function, `0x009C7C40`)
- `0x00ABA3C0` → [SeReleaseSid](../A2/SeReleaseSid_function_00A2EF50.md) (function, `0x00A2EF50`)
- `0x00ABA3D2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00ABA3E6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00AB9C93` → RVA `0x00FD8020` (`PAGEDATA`; read)
- `0x00ABA1FE` → RVA `0x00F05780` (`.data`; read)
- `0x00ABA210` → RVA `0x00FD9AD8` (`PAGEDATA`; read/write)
- `0x00ABA24B` → RVA `0x00F05790` (`.data`; read)
- `0x00ABA276` → RVA `0x00012D08` (`.rdata`; read)
- `0x00ABA280` → RVA `0x00E0EBF0` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **36**
  - `0x00AB98AD` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (`PAGE` → `.text`)
  - `0x00AB9A82` → [SeCaptureHandles](../../text/60/SeCaptureHandles_function_00609FEC.md) (`PAGE` → `.text`)
  - `0x00AB9B22` → [SepCreateAppContainerToken](../../text/4F/SepCreateAppContainerToken_function_004F43AC.md) (`PAGE` → `.text`)
  - `0x00AB9B69` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AB9DCA` → [SeCaptureHandles](../../text/60/SeCaptureHandles_function_00609FEC.md) (`PAGE` → `.text`)
  - `0x00AB9E3C` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (`PAGE` → `.text`)
  - `0x00AB9E62` → [SepCapabilitiesHasAppSiloBaseSID](../../text/40/SepCapabilitiesHasAppSiloBaseSID_function_004005B0.md) (`PAGE` → `.text`)
  - `0x00AB9E84` → [SepIsAppSiloCapability](../../text/48/SepIsAppSiloCapability_function_0048E54C.md) (`PAGE` → `.text`)
  - `0x00AB9EF1` → [Feature_871661881__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_871661881__private_IsEnabledDeviceUsageNoInline_function_004F4D24.md) (`PAGE` → `.text`)
  - `0x00AB9F41` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AB9F49` → [SepLocateTokenIntegrity](../../text/41/SepLocateTokenIntegrity_function_0041BF10.md) (`PAGE` → `.text`)
  - `0x00AB9F5D` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (`PAGE` → `.text`)
  - `0x00AB9F74` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x00AB9FC5` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AB9FCD` → [SepLocateTokenIntegrity](../../text/41/SepLocateTokenIntegrity_function_0041BF10.md) (`PAGE` → `.text`)
  - `0x00AB9FD8` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (`PAGE` → `.text`)
  - `0x00AB9FEB` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x00ABA001` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00ABA006` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00ABA01F` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00ABA024` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00ABA0AD` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00ABA0C1` → [SepLocateTokenIntegrity](../../text/41/SepLocateTokenIntegrity_function_0041BF10.md) (`PAGE` → `.text`)
  - `0x00ABA0DA` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x00ABA10A` → [Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline](../../text/4C/Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline_function_004C78E8.md) (`PAGE` → `.text`)
  - `0x00ABA1D6` → [SepAppendAceToTokenDefaultDacl](../../text/40/SepAppendAceToTokenDefaultDacl_function_004002F8.md) (`PAGE` → `.text`)
  - `0x00ABA207` → [SepSidInTokenSidHash](../../text/3C/SepSidInTokenSidHash_function_003C85E0.md) (`PAGE` → `.text`)
  - `0x00ABA254` → [SepSidInTokenSidHash](../../text/3C/SepSidInTokenSidHash_function_003C85E0.md) (`PAGE` → `.text`)
  - `0x00ABA2A4` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00ABA2A9` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00ABA314` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00ABA369` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00ABA36E` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00ABA381` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00ABA3D2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00ABA3E6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB9880  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00AB9885  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00AB988A  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00AB988F  53                              push rbx
00AB9890  56                              push rsi
00AB9891  57                              push rdi
00AB9892  41 54                           push r12
00AB9894  41 55                           push r13
00AB9896  41 56                           push r14
00AB9898  41 57                           push r15
00AB989A  48 81 EC 50 01 00 00            sub rsp, 0x150
00AB98A1  4D 8B E9                        mov r13, r9
00AB98A4  45 8B F0                        mov r14d, r8d
00AB98A7  4C 8B E2                        mov r12, rdx
00AB98AA  4C 8B F9                        mov r15, rcx
00AB98AD  E8 D6 5E A3 FF                  call 0x1404ef788
00AB98B2  45 33 C9                        xor r9d, r9d
00AB98B5  0F 57 C0                        xorps xmm0, xmm0
00AB98B8  85 C0                           test eax, eax
00AB98BA  0F 84 B3 02 00 00               je 0x140ab9b73
00AB98C0  4C 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], r9
00AB98C8  44 89 8C 24 88 00 00 00         mov dword ptr [rsp + 0x88], r9d
00AB98D0  4C 89 8C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r9
00AB98D8  4C 89 8C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r9
00AB98E0  0F 11 84 24 C8 00 00 00         movups xmmword ptr [rsp + 0xc8], xmm0
00AB98E8  0F 11 84 24 D8 00 00 00         movups xmmword ptr [rsp + 0xd8], xmm0
00AB98F0  0F 11 84 24 E8 00 00 00         movups xmmword ptr [rsp + 0xe8], xmm0
00AB98F8  0F 11 84 24 F8 00 00 00         movups xmmword ptr [rsp + 0xf8], xmm0
00AB9900  0F 11 84 24 08 01 00 00         movups xmmword ptr [rsp + 0x108], xmm0
00AB9908  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AB9911  40 8A B0 32 02 00 00            mov sil, byte ptr [rax + 0x232]
00AB9918  40 84 F6                        test sil, sil
00AB991B  74 5B                           je 0x140ab9978
00AB991D  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
00AB9927  48 8B CA                        mov rcx, rdx
00AB992A  4C 3B FA                        cmp r15, rdx
00AB992D  49 0F 42 CF                     cmovb rcx, r15
00AB9931  48 8B 01                        mov rax, qword ptr [rcx]
00AB9934  48 89 01                        mov qword ptr [rcx], rax
00AB9937  8B 84 24 C8 01 00 00            mov eax, dword ptr [rsp + 0x1c8]
00AB993E  48 8D 0C C5 00 00 00 00         lea rcx, [rax*8]
00AB9946  48 85 C9                        test rcx, rcx
00AB9949  74 26                           je 0x140ab9971
00AB994B  F6 84 24 D0 01 00 00 07         test byte ptr [rsp + 0x1d0], 7
00AB9953  74 05                           je 0x140ab995a
00AB9955  E8 76 06 DE FF                  call 0x140899fd0
00AB995A  48 8B 84 24 D0 01 00 00         mov rax, qword ptr [rsp + 0x1d0]
00AB9962  48 03 C8                        add rcx, rax
00AB9965  48 3B CA                        cmp rcx, rdx
00AB9968  77 05                           ja 0x140ab996f
00AB996A  48 3B C8                        cmp rcx, rax
00AB996D  73 02                           jae 0x140ab9971
00AB996F  8A 02                           mov al, byte ptr [rdx]
00AB9971  EB 05                           jmp 0x140ab9978
00AB9973  E9 88 0A 00 00                  jmp 0x140aba400
00AB9978  4D 85 E4                        test r12, r12
00AB997B  75 0A                           jne 0x140ab9987
00AB997D  B8 08 00 00 C0                  mov eax, 0xc0000008
00AB9982  E9 79 0A 00 00                  jmp 0x140aba400
00AB9987  48 8B 8C 24 B0 01 00 00         mov rcx, qword ptr [rsp + 0x1b0]
00AB998F  48 85 C9                        test rcx, rcx
00AB9992  0F 84 BF 02 00 00               je 0x140ab9c57
00AB9998  44 39 8C 24 C8 01 00 00         cmp dword ptr [rsp + 0x1c8], r9d
00AB99A0  75 18                           jne 0x140ab99ba
00AB99A2  4C 39 8C 24 D0 01 00 00         cmp qword ptr [rsp + 0x1d0], r9
00AB99AA  0F 85 D9 02 00 00               jne 0x140ab9c89
00AB99B0  44 39 8C 24 C8 01 00 00         cmp dword ptr [rsp + 0x1c8], r9d
00AB99B8  74 0E                           je 0x140ab99c8
00AB99BA  4C 39 8C 24 D0 01 00 00         cmp qword ptr [rsp + 0x1d0], r9
00AB99C2  0F 84 C1 02 00 00               je 0x140ab9c89
00AB99C8  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
00AB99D0  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AB99D5  BF 01 00 00 00                  mov edi, 1
00AB99DA  40 88 7C 24 28                  mov byte ptr [rsp + 0x28], dil
00AB99DF  40 8A D6                        mov dl, sil
00AB99E2  E8 ED DC E6 FF                  call 0x1409276d4
00AB99E7  8B D8                           mov ebx, eax
00AB99E9  85 C0                           test eax, eax
00AB99EB  0F 88 38 01 00 00               js 0x140ab9b29
00AB99F1  44 8B B4 24 B8 01 00 00         mov r14d, dword ptr [rsp + 0x1b8]
00AB99F9  45 85 F6                        test r14d, r14d
00AB99FC  75 10                           jne 0x140ab9a0e
00AB99FE  48 83 BC 24 C0 01 00 00 00      cmp qword ptr [rsp + 0x1c0], 0
00AB9A07  75 10                           jne 0x140ab9a19
00AB9A09  45 85 F6                        test r14d, r14d
00AB9A0C  74 15                           je 0x140ab9a23
00AB9A0E  48 83 BC 24 C0 01 00 00 00      cmp qword ptr [rsp + 0x1c0], 0
00AB9A17  75 0A                           jne 0x140ab9a23
00AB9A19  BB 30 00 00 C0                  mov ebx, 0xc0000030
00AB9A1E  E9 06 01 00 00                  jmp 0x140ab9b29
00AB9A23  48 8B 8C 24 C0 01 00 00         mov rcx, qword ptr [rsp + 0x1c0]
00AB9A2B  48 85 C9                        test rcx, rcx
00AB9A2E  74 2F                           je 0x140ab9a5f
00AB9A30  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AB9A38  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00AB9A3D  48 8D 84 24 98 00 00 00         lea rax, [rsp + 0x98]
00AB9A45  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AB9A4A  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
00AB9A4F  45 33 C9                        xor r9d, r9d
00AB9A52  44 8A C6                        mov r8b, sil
00AB9A55  41 8B D6                        mov edx, r14d
00AB9A58  E8 13 03 F1 FF                  call 0x1409c9d70
00AB9A5D  8B D8                           mov ebx, eax
00AB9A5F  85 DB                           test ebx, ebx
00AB9A61  0F 88 C2 00 00 00               js 0x140ab9b29
00AB9A67  4C 8D 84 24 A8 00 00 00         lea r8, [rsp + 0xa8]
00AB9A6F  48 8B 94 24 D0 01 00 00         mov rdx, qword ptr [rsp + 0x1d0]
00AB9A77  44 8B BC 24 C8 01 00 00         mov r15d, dword ptr [rsp + 0x1c8]
00AB9A7F  41 8B CF                        mov ecx, r15d
00AB9A82  E8 65 05 B5 FF                  call 0x140609fec
00AB9A87  8B D8                           mov ebx, eax
00AB9A89  85 C0                           test eax, eax
00AB9A8B  0F 88 98 00 00 00               js 0x140ab9b29
00AB9A91  48 8D 84 24 C8 00 00 00         lea rax, [rsp + 0xc8]
00AB9A99  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
00AB9AA1  C7 84 24 C8 00 00 00 30 00 00 00  mov dword ptr [rsp + 0xc8], 0x30
00AB9AAC  09 BC 24 CC 00 00 00            or dword ptr [rsp + 0xcc], edi
00AB9AB3  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
00AB9ABB  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
00AB9AC3  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00AB9ACB  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
00AB9AD3  44 89 B4 24 E8 00 00 00         mov dword ptr [rsp + 0xe8], r14d
00AB9ADB  4C 89 A4 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r12
00AB9AE3  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
00AB9AEB  48 89 84 24 08 01 00 00         mov qword ptr [rsp + 0x108], rax
00AB9AF3  44 89 BC 24 10 01 00 00         mov dword ptr [rsp + 0x110], r15d
00AB9AFB  48 8D 84 24 F8 00 00 00         lea rax, [rsp + 0xf8]
00AB9B03  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AB9B08  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
00AB9B0D  4D 8B CD                        mov r9, r13
00AB9B10  44 8B 84 24 A0 01 00 00         mov r8d, dword ptr [rsp + 0x1a0]
00AB9B18  33 D2                           xor edx, edx
00AB9B1A  48 8B 8C 24 90 01 00 00         mov rcx, qword ptr [rsp + 0x190]
00AB9B22  E8 85 A8 A3 FF                  call 0x1404f43ac
00AB9B27  8B D8                           mov ebx, eax
00AB9B29  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00AB9B31  48 85 C9                        test rcx, rcx
00AB9B34  74 08                           je 0x140ab9b3e
00AB9B36  40 8A D6                        mov dl, sil
00AB9B39  E8 02 E1 F0 FF                  call 0x1409c7c40
00AB9B3E  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
00AB9B46  48 85 C9                        test rcx, rcx
00AB9B49  74 0B                           je 0x140ab9b56
00AB9B4B  44 8A C7                        mov r8b, dil
00AB9B4E  40 8A D6                        mov dl, sil
00AB9B51  E8 FA 53 F7 FF                  call 0x140a2ef50
00AB9B56  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
00AB9B5E  48 85 C9                        test rcx, rcx
00AB9B61  0F 84 97 08 00 00               je 0x140aba3fe
00AB9B67  33 D2                           xor edx, edx
00AB9B69  E8 02 8D 0C 00                  call 0x140b82870
00AB9B6E  E9 8B 08 00 00                  jmp 0x140aba3fe
00AB9B73  4C 89 4C 24 68                  mov qword ptr [rsp + 0x68], r9
00AB9B78  44 89 8C 24 8C 00 00 00         mov dword ptr [rsp + 0x8c], r9d
00AB9B80  4C 89 8C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r9
00AB9B88  4C 89 4C 24 70                  mov qword ptr [rsp + 0x70], r9
00AB9B8D  4C 89 8C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r9
00AB9B95  4C 89 8C 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], r9
00AB9B9D  4C 89 4C 24 58                  mov qword ptr [rsp + 0x58], r9
00AB9BA2  BF 01 00 00 00                  mov edi, 1
00AB9BA7  89 BC 24 90 00 00 00            mov dword ptr [rsp + 0x90], edi
00AB9BAE  44 88 4C 24 51                  mov byte ptr [rsp + 0x51], r9b
00AB9BB3  41 8A F1                        mov sil, r9b
00AB9BB6  44 88 4C 24 50                  mov byte ptr [rsp + 0x50], r9b
00AB9BBB  44 89 8C 24 80 00 00 00         mov dword ptr [rsp + 0x80], r9d
00AB9BC3  44 88 4C 24 60                  mov byte ptr [rsp + 0x60], r9b
00AB9BC8  33 C0                           xor eax, eax
00AB9BCA  0F 11 84 24 18 01 00 00         movups xmmword ptr [rsp + 0x118], xmm0
00AB9BD2  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
00AB9BDA  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AB9BE3  44 8A A8 32 02 00 00            mov r13b, byte ptr [rax + 0x232]
00AB9BEA  45 84 ED                        test r13b, r13b
00AB9BED  74 5B                           je 0x140ab9c4a
00AB9BEF  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
00AB9BF9  48 8B CA                        mov rcx, rdx
00AB9BFC  4C 3B FA                        cmp r15, rdx
00AB9BFF  49 0F 42 CF                     cmovb rcx, r15
00AB9C03  48 8B 01                        mov rax, qword ptr [rcx]
00AB9C06  48 89 01                        mov qword ptr [rcx], rax
00AB9C09  8B 84 24 C8 01 00 00            mov eax, dword ptr [rsp + 0x1c8]
00AB9C10  48 8D 0C C5 00 00 00 00         lea rcx, [rax*8]
00AB9C18  48 85 C9                        test rcx, rcx
00AB9C1B  74 26                           je 0x140ab9c43
00AB9C1D  F6 84 24 D0 01 00 00 07         test byte ptr [rsp + 0x1d0], 7
00AB9C25  74 05                           je 0x140ab9c2c
00AB9C27  E8 A4 03 DE FF                  call 0x140899fd0
00AB9C2C  48 8B 84 24 D0 01 00 00         mov rax, qword ptr [rsp + 0x1d0]
00AB9C34  48 03 C8                        add rcx, rax
00AB9C37  48 3B CA                        cmp rcx, rdx
00AB9C3A  77 05                           ja 0x140ab9c41
00AB9C3C  48 3B C8                        cmp rcx, rax
00AB9C3F  73 02                           jae 0x140ab9c43
00AB9C41  8A 02                           mov al, byte ptr [rdx]
00AB9C43  EB 05                           jmp 0x140ab9c4a
00AB9C45  E9 B6 07 00 00                  jmp 0x140aba400
00AB9C4A  48 8B 9C 24 B0 01 00 00         mov rbx, qword ptr [rsp + 0x1b0]
00AB9C52  48 85 DB                        test rbx, rbx
00AB9C55  75 0A                           jne 0x140ab9c61
00AB9C57  B8 0D 00 00 C0                  mov eax, 0xc000000d
00AB9C5C  E9 9F 07 00 00                  jmp 0x140aba400
00AB9C61  44 39 8C 24 C8 01 00 00         cmp dword ptr [rsp + 0x1c8], r9d
00AB9C69  75 14                           jne 0x140ab9c7f
00AB9C6B  4C 39 8C 24 D0 01 00 00         cmp qword ptr [rsp + 0x1d0], r9
00AB9C73  75 14                           jne 0x140ab9c89
00AB9C75  44 39 8C 24 C8 01 00 00         cmp dword ptr [rsp + 0x1c8], r9d
00AB9C7D  74 14                           je 0x140ab9c93
00AB9C7F  4C 39 8C 24 D0 01 00 00         cmp qword ptr [rsp + 0x1d0], r9
00AB9C87  75 0A                           jne 0x140ab9c93
00AB9C89  B8 30 00 00 C0                  mov eax, 0xc0000030
00AB9C8E  E9 6D 07 00 00                  jmp 0x140aba400
00AB9C93  4C 8B 05 86 E3 51 00            mov r8, qword ptr [rip + 0x51e386]
00AB9C9A  4C 89 4C 24 78                  mov qword ptr [rsp + 0x78], r9
00AB9C9F  48 8D 84 24 C0 00 00 00         lea rax, [rsp + 0xc0]
00AB9CA7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AB9CAC  48 8D 44 24 78                  lea rax, [rsp + 0x78]
00AB9CB1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AB9CB6  45 8A CD                        mov r9b, r13b
00AB9CB9  BA 02 00 00 00                  mov edx, 2
00AB9CBE  49 8B CC                        mov rcx, r12
00AB9CC1  E8 EA F0 DA FF                  call 0x140868db0
00AB9CC6  45 33 E4                        xor r12d, r12d
00AB9CC9  85 C0                           test eax, eax
00AB9CCB  0F 88 2F 07 00 00               js 0x140aba400
00AB9CD1  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00AB9CD6  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AB9CDB  40 88 7C 24 28                  mov byte ptr [rsp + 0x28], dil
00AB9CE0  41 8A D5                        mov dl, r13b
00AB9CE3  48 8B CB                        mov rcx, rbx
00AB9CE6  E8 E9 D9 E6 FF                  call 0x1409276d4
00AB9CEB  8B D8                           mov ebx, eax
00AB9CED  85 C0                           test eax, eax
00AB9CEF  0F 88 36 06 00 00               js 0x140aba32b
00AB9CF5  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00AB9CFA  E8 CD 69 C4 FF                  call 0x1407006cc
00AB9CFF  8B D8                           mov ebx, eax
00AB9D01  85 C0                           test eax, eax
00AB9D03  0F 88 22 06 00 00               js 0x140aba32b
00AB9D09  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
00AB9D0E  39 BE C0 00 00 00               cmp dword ptr [rsi + 0xc0], edi
00AB9D14  74 16                           je 0x140ab9d2c
00AB9D16  83 BE C4 00 00 00 02            cmp dword ptr [rsi + 0xc4], 2
00AB9D1D  7D 0D                           jge 0x140ab9d2c
00AB9D1F  BB A5 00 00 C0                  mov ebx, 0xc00000a5
00AB9D24  41 8A F4                        mov sil, r12b
00AB9D27  E9 FF 05 00 00                  jmp 0x140aba32b
00AB9D2C  44 8B BC 24 C4 00 00 00         mov r15d, dword ptr [rsp + 0xc4]
00AB9D34  45 85 F6                        test r14d, r14d
00AB9D37  45 0F 45 FE                     cmovne r15d, r14d
00AB9D3B  44 89 BC 24 94 00 00 00         mov dword ptr [rsp + 0x94], r15d
00AB9D43  44 8B B4 24 B8 01 00 00         mov r14d, dword ptr [rsp + 0x1b8]
00AB9D4B  45 85 F6                        test r14d, r14d
00AB9D4E  75 0F                           jne 0x140ab9d5f
00AB9D50  4C 39 A4 24 C0 01 00 00         cmp qword ptr [rsp + 0x1c0], r12
00AB9D58  75 0F                           jne 0x140ab9d69
00AB9D5A  45 85 F6                        test r14d, r14d
00AB9D5D  74 17                           je 0x140ab9d76
00AB9D5F  4C 39 A4 24 C0 01 00 00         cmp qword ptr [rsp + 0x1c0], r12
00AB9D67  75 0D                           jne 0x140ab9d76
00AB9D69  BB 30 00 00 C0                  mov ebx, 0xc0000030
00AB9D6E  41 8A F4                        mov sil, r12b
00AB9D71  E9 AD 05 00 00                  jmp 0x140aba323
00AB9D76  48 8B 8C 24 C0 01 00 00         mov rcx, qword ptr [rsp + 0x1c0]
00AB9D7E  48 85 C9                        test rcx, rcx
00AB9D81  74 2C                           je 0x140ab9daf
00AB9D83  48 8D 84 24 8C 00 00 00         lea rax, [rsp + 0x8c]
00AB9D8B  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00AB9D90  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00AB9D95  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AB9D9A  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00AB9D9F  45 33 C9                        xor r9d, r9d
00AB9DA2  45 8A C5                        mov r8b, r13b
00AB9DA5  41 8B D6                        mov edx, r14d
00AB9DA8  E8 C3 FF F0 FF                  call 0x1409c9d70
00AB9DAD  8B D8                           mov ebx, eax
00AB9DAF  85 DB                           test ebx, ebx
00AB9DB1  78 BB                           js 0x140ab9d6e
00AB9DB3  4C 8D 84 24 B0 00 00 00         lea r8, [rsp + 0xb0]
00AB9DBB  48 8B 94 24 D0 01 00 00         mov rdx, qword ptr [rsp + 0x1d0]
00AB9DC3  8B 8C 24 C8 01 00 00            mov ecx, dword ptr [rsp + 0x1c8]
00AB9DCA  E8 1D 02 B5 FF                  call 0x140609fec
00AB9DCF  8B D8                           mov ebx, eax
00AB9DD1  85 C0                           test eax, eax
00AB9DD3  78 99                           js 0x140ab9d6e
00AB9DD5  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00AB9DDA  E8 5D 49 FA FF                  call 0x140a5e73c
00AB9DDF  84 C0                           test al, al
00AB9DE1  75 07                           jne 0x140ab9dea
00AB9DE3  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AB9DE8  EB 84                           jmp 0x140ab9d6e
00AB9DEA  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00AB9DEF  8A 48 01                        mov cl, byte ptr [rax + 1]
00AB9DF2  80 E9 08                        sub cl, 8
00AB9DF5  F6 C1 FB                        test cl, 0xfb
00AB9DF8  74 0A                           je 0x140ab9e04
00AB9DFA  BB 02 A2 00 C0                  mov ebx, 0xc000a202
00AB9DFF  E9 6A FF FF FF                  jmp 0x140ab9d6e
00AB9E04  41 8B DC                        mov ebx, r12d
00AB9E07  41 3B DE                        cmp ebx, r14d
00AB9E0A  73 4E                           jae 0x140ab9e5a
00AB9E0C  44 8B FB                        mov r15d, ebx
00AB9E0F  4D 03 FF                        add r15, r15
00AB9E12  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
00AB9E17  4B 8B 0C FC                     mov rcx, qword ptr [r12 + r15*8]
00AB9E1B  E8 64 4F FA FF                  call 0x140a5ed84
00AB9E20  84 C0                           test al, al
00AB9E22  74 29                           je 0x140ab9e4d
00AB9E24  33 F6                           xor esi, esi
00AB9E26  3B F3                           cmp esi, ebx
00AB9E28  73 1F                           jae 0x140ab9e49
00AB9E2A  8B C6                           mov eax, esi
00AB9E2C  48 03 C0                        add rax, rax
00AB9E2F  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
00AB9E34  48 8B 14 C2                     mov rdx, qword ptr [rdx + rax*8]
00AB9E38  4B 8B 0C FC                     mov rcx, qword ptr [r12 + r15*8]
00AB9E3C  E8 8F 6C 94 FF                  call 0x140400ad0
00AB9E41  84 C0                           test al, al
00AB9E43  75 08                           jne 0x140ab9e4d
00AB9E45  03 F7                           add esi, edi
00AB9E47  EB DD                           jmp 0x140ab9e26
00AB9E49  03 DF                           add ebx, edi
00AB9E4B  EB BA                           jmp 0x140ab9e07
00AB9E4D  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AB9E52  45 33 E4                        xor r12d, r12d
00AB9E55  E9 C4 04 00 00                  jmp 0x140aba31e
00AB9E5A  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
00AB9E5F  41 8B CE                        mov ecx, r14d
00AB9E62  E8 49 67 94 FF                  call 0x1404005b0
00AB9E67  45 33 E4                        xor r12d, r12d
00AB9E6A  84 C0                           test al, al
00AB9E6C  75 27                           jne 0x140ab9e95
00AB9E6E  41 8B DC                        mov ebx, r12d
00AB9E71  41 3B DE                        cmp ebx, r14d
00AB9E74  73 1F                           jae 0x140ab9e95
00AB9E76  8B C3                           mov eax, ebx
00AB9E78  48 03 C0                        add rax, rax
00AB9E7B  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00AB9E80  48 8B 0C C1                     mov rcx, qword ptr [rcx + rax*8]
00AB9E84  E8 C3 46 9D FF                  call 0x14048e54c
00AB9E89  84 C0                           test al, al
00AB9E8B  0F 85 52 FF FF FF               jne 0x140ab9de3
00AB9E91  03 DF                           add ebx, edi
00AB9E93  EB DC                           jmp 0x140ab9e71
00AB9E95  48 8D 94 24 80 00 00 00         lea rdx, [rsp + 0x80]
00AB9E9D  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00AB9EA2  E8 B9 82 FB FF                  call 0x140a72160
00AB9EA7  8B D8                           mov ebx, eax
00AB9EA9  85 C0                           test eax, eax
00AB9EAB  0F 88 BD FE FF FF               js 0x140ab9d6e
00AB9EB1  39 BC 24 80 00 00 00            cmp dword ptr [rsp + 0x80], edi
00AB9EB8  75 2F                           jne 0x140ab9ee9
00AB9EBA  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00AB9EBF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AB9EC4  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00AB9EC9  41 8B D6                        mov edx, r14d
00AB9ECC  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00AB9ED1  E8 3A AB FE FF                  call 0x140aa4a10
00AB9ED6  8B D8                           mov ebx, eax
00AB9ED8  44 38 64 24 60                  cmp byte ptr [rsp + 0x60], r12b
00AB9EDD  75 0A                           jne 0x140ab9ee9
00AB9EDF  BB 22 00 00 C0                  mov ebx, 0xc0000022
00AB9EE4  E9 85 FE FF FF                  jmp 0x140ab9d6e
00AB9EE9  85 DB                           test ebx, ebx
00AB9EEB  0F 88 7D FE FF FF               js 0x140ab9d6e
00AB9EF1  E8 2E AE A3 FF                  call 0x1404f4d24
00AB9EF6  85 C0                           test eax, eax
00AB9EF8  0F 84 33 01 00 00               je 0x140aba031
00AB9EFE  44 89 A4 24 84 00 00 00         mov dword ptr [rsp + 0x84], r12d
00AB9F06  48 8D 8C 24 84 00 00 00         lea rcx, [rsp + 0x84]
00AB9F0E  E8 9D 6D FA FF                  call 0x140a60cb0
00AB9F13  8B 84 24 84 00 00 00            mov eax, dword ptr [rsp + 0x84]
00AB9F1A  24 18                           and al, 0x18
00AB9F1C  3C 10                           cmp al, 0x10
00AB9F1E  0F 85 0D 01 00 00               jne 0x140aba031
00AB9F24  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AB9F2D  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AB9F34  90                              nop
00AB9F35  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
00AB9F3A  40 8A D7                        mov dl, dil
00AB9F3D  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AB9F41  E8 7A 7C 75 FF                  call 0x140211bc0
00AB9F46  48 8B CE                        mov rcx, rsi
00AB9F49  E8 C2 1F 96 FF                  call 0x14041bf10
00AB9F4E  48 85 C0                        test rax, rax
00AB9F51  0F 84 C4 00 00 00               je 0x140aba01b
00AB9F57  4C 8B 38                        mov r15, qword ptr [rax]
00AB9F5A  49 8B CF                        mov rcx, r15
00AB9F5D  E8 AE EF 9A FF                  call 0x140468f10
00AB9F62  0F B6 08                        movzx ecx, byte ptr [rax]
00AB9F65  84 C9                           test cl, cl
00AB9F67  0F 84 AE 00 00 00               je 0x140aba01b
00AB9F6D  8B D1                           mov edx, ecx
00AB9F6F  2B D7                           sub edx, edi
00AB9F71  49 8B CF                        mov rcx, r15
00AB9F74  E8 97 CD 99 FF                  call 0x140456d10
00AB9F79  81 38 00 30 00 00               cmp dword ptr [rax], 0x3000
00AB9F7F  0F 82 96 00 00 00               jb 0x140aba01b
00AB9F85  0F 57 C0                        xorps xmm0, xmm0
00AB9F88  0F 11 84 24 30 01 00 00         movups xmmword ptr [rsp + 0x130], xmm0
00AB9F90  0F 11 84 24 40 01 00 00         movups xmmword ptr [rsp + 0x140], xmm0
00AB9F98  48 8D 8C 24 30 01 00 00         lea rcx, [rsp + 0x130]
00AB9FA0  E8 7B 18 DB FF                  call 0x14086b820
00AB9FA5  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AB9FAE  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AB9FB5  90                              nop
00AB9FB6  4C 8B BC 24 40 01 00 00         mov r15, qword ptr [rsp + 0x140]
00AB9FBE  40 8A D7                        mov dl, dil
00AB9FC1  49 8B 4F 30                     mov rcx, qword ptr [r15 + 0x30]
00AB9FC5  E8 F6 7B 75 FF                  call 0x140211bc0
00AB9FCA  49 8B CF                        mov rcx, r15
00AB9FCD  E8 3E 1F 96 FF                  call 0x14041bf10
00AB9FD2  4C 8B 20                        mov r12, qword ptr [rax]
00AB9FD5  49 8B CC                        mov rcx, r12
00AB9FD8  E8 33 EF 9A FF                  call 0x140468f10
00AB9FDD  0F B6 08                        movzx ecx, byte ptr [rax]
00AB9FE0  84 C9                           test cl, cl
00AB9FE2  74 14                           je 0x140ab9ff8
00AB9FE4  8B D1                           mov edx, ecx
00AB9FE6  2B D7                           sub edx, edi
00AB9FE8  49 8B CC                        mov rcx, r12
00AB9FEB  E8 20 CD 99 FF                  call 0x140456d10
00AB9FF0  81 38 00 30 00 00               cmp dword ptr [rax], 0x3000
00AB9FF6  73 05                           jae 0x140ab9ffd
00AB9FF8  BB 22 00 00 C0                  mov ebx, 0xc0000022
00AB9FFD  49 8B 4F 30                     mov rcx, qword ptr [r15 + 0x30]
00ABA001  E8 0A 5A 7A FF                  call 0x14025fa10
00ABA006  E8 A5 38 7A FF                  call 0x14025d8b0
00ABA00B  48 8D 8C 24 30 01 00 00         lea rcx, [rsp + 0x130]
00ABA013  E8 F8 16 DB FF                  call 0x14086b710
00ABA018  45 33 E4                        xor r12d, r12d
00ABA01B  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00ABA01F  E8 EC 59 7A FF                  call 0x14025fa10
00ABA024  E8 87 38 7A FF                  call 0x14025d8b0
00ABA029  85 DB                           test ebx, ebx
00ABA02B  0F 88 ED 02 00 00               js 0x140aba31e
00ABA031  48 8D 44 24 58                  lea rax, [rsp + 0x58]
00ABA036  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00ABA03B  44 88 64 24 30                  mov byte ptr [rsp + 0x30], r12b
00ABA040  44 88 6C 24 28                  mov byte ptr [rsp + 0x28], r13b
00ABA045  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00ABA04A  44 8B CF                        mov r9d, edi
00ABA04D  45 33 C0                        xor r8d, r8d
00ABA050  48 8B 94 24 A8 01 00 00         mov rdx, qword ptr [rsp + 0x1a8]
00ABA058  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00ABA05D  E8 8A E7 DF FF                  call 0x1408b87ec
00ABA062  8B D8                           mov ebx, eax
00ABA064  85 C0                           test eax, eax
00ABA066  0F 88 B2 02 00 00               js 0x140aba31e
00ABA06C  40 8A F7                        mov sil, dil
00ABA06F  40 88 7C 24 50                  mov byte ptr [rsp + 0x50], dil
00ABA074  48 8D 94 24 90 00 00 00         lea rdx, [rsp + 0x90]
00ABA07C  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00ABA081  E8 46 4D FA FF                  call 0x140a5edcc
00ABA086  8B D8                           mov ebx, eax
00ABA088  85 C0                           test eax, eax
00ABA08A  0F 88 93 02 00 00               js 0x140aba323
00ABA090  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00ABA099  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00ABA0A0  90                              nop
00ABA0A1  40 8A D7                        mov dl, dil
00ABA0A4  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00ABA0A9  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
00ABA0AD  E8 6E AD 75 FF                  call 0x140214e20
00ABA0B2  F0 44 09 24 24                  lock or dword ptr [rsp], r12d
00ABA0B7  40 88 7C 24 51                  mov byte ptr [rsp + 0x51], dil
00ABA0BC  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00ABA0C1  E8 4A 1E 96 FF                  call 0x14041bf10
00ABA0C6  48 85 C0                        test rax, rax
00ABA0C9  74 70                           je 0x140aba13b
00ABA0CB  48 8B 08                        mov rcx, qword ptr [rax]
00ABA0CE  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
00ABA0D2  84 C0                           test al, al
00ABA0D4  74 0F                           je 0x140aba0e5
00ABA0D6  8B D0                           mov edx, eax
00ABA0D8  2B D7                           sub edx, edi
00ABA0DA  E8 31 CC 99 FF                  call 0x140456d10
00ABA0DF  C7 00 00 10 00 00               mov dword ptr [rax], 0x1000
00ABA0E5  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00ABA0EA  48 B9 00 00 80 00 02 00 00 00   movabs rcx, 0x200800000
00ABA0F4  48 21 48 48                     and qword ptr [rax + 0x48], rcx
00ABA0F8  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00ABA0FD  48 21 48 50                     and qword ptr [rax + 0x50], rcx
00ABA101  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00ABA106  48 21 48 40                     and qword ptr [rax + 0x40], rcx
00ABA10A  E8 D9 D7 A0 FF                  call 0x1404c78e8
00ABA10F  85 C0                           test eax, eax
00ABA111  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00ABA116  74 0C                           je 0x140aba124
00ABA118  81 A0 C8 00 00 00 FF CF FF FF   and dword ptr [rax + 0xc8], 0xffffcfff
00ABA122  EB 08                           jmp 0x140aba12c
00ABA124  0F BA B0 C8 00 00 00 0D         btr dword ptr [rax + 0xc8], 0xd
00ABA12C  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00ABA131  0F BA A8 C8 00 00 00 0E         bts dword ptr [rax + 0xc8], 0xe
00ABA139  EB 05                           jmp 0x140aba140
00ABA13B  BB 46 04 00 C0                  mov ebx, 0xc0000446
00ABA140  85 DB                           test ebx, ebx
00ABA142  0F 88 DB 01 00 00               js 0x140aba323
00ABA148  45 8B CE                        mov r9d, r14d
00ABA14B  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00ABA150  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00ABA155  48 8B D6                        mov rdx, rsi
00ABA158  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00ABA15D  E8 92 F9 F0 FF                  call 0x1409c9af4
00ABA162  8B D8                           mov ebx, eax
00ABA164  85 C0                           test eax, eax
00ABA166  0F 88 B2 01 00 00               js 0x140aba31e
00ABA16C  48 8B D6                        mov rdx, rsi
00ABA16F  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00ABA174  E8 F3 AB FA FF                  call 0x140a64d6c
00ABA179  8B D8                           mov ebx, eax
00ABA17B  85 C0                           test eax, eax
00ABA17D  0F 88 9B 01 00 00               js 0x140aba31e
00ABA183  48 89 B4 24 20 01 00 00         mov qword ptr [rsp + 0x120], rsi
00ABA18B  4C 8B 8C 24 B0 00 00 00         mov r9, qword ptr [rsp + 0xb0]
00ABA193  44 8B 84 24 C8 01 00 00         mov r8d, dword ptr [rsp + 0x1c8]
00ABA19B  48 8D 94 24 18 01 00 00         lea rdx, [rsp + 0x118]
00ABA1A3  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00ABA1A8  E8 EF F1 EE FF                  call 0x1409a939c
00ABA1AD  8B D8                           mov ebx, eax
00ABA1AF  85 C0                           test eax, eax
00ABA1B1  0F 88 67 01 00 00               js 0x140aba31e
00ABA1B7  48 8B D6                        mov rdx, rsi
00ABA1BA  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00ABA1BF  E8 F4 6A F6 FF                  call 0x140a20cb8
00ABA1C4  8B D8                           mov ebx, eax
00ABA1C6  85 C0                           test eax, eax
00ABA1C8  0F 88 50 01 00 00               js 0x140aba31e
00ABA1CE  48 8B D6                        mov rdx, rsi
00ABA1D1  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00ABA1D6  E8 1D 61 94 FF                  call 0x1404002f8
00ABA1DB  8B D8                           mov ebx, eax
00ABA1DD  85 C0                           test eax, eax
00ABA1DF  0F 88 39 01 00 00               js 0x140aba31e
00ABA1E5  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
00ABA1EA  48 8D 8B 28 03 00 00            lea rcx, [rbx + 0x328]
00ABA1F1  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
00ABA1F6  40 88 7C 24 20                  mov byte ptr [rsp + 0x20], dil
00ABA1FB  45 33 C9                        xor r9d, r9d
00ABA1FE  4C 8B 05 7B B5 44 00            mov r8, qword ptr [rip + 0x44b57b]
00ABA205  33 D2                           xor edx, edx
00ABA207  E8 D4 E3 90 FF                  call 0x1403c85e0
00ABA20C  84 C0                           test al, al
00ABA20E  74 18                           je 0x140aba228
00ABA210  F0 01 3D C1 F8 51 00            lock add dword ptr [rip + 0x51f8c1], edi
00ABA217  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00ABA21C  81 88 C8 00 00 00 00 00 00 03   or dword ptr [rax + 0xc8], 0x3000000
00ABA226  EB 49                           jmp 0x140aba271
00ABA228  81 A3 C8 00 00 00 FF FF FF FC   and dword ptr [rbx + 0xc8], 0xfcffffff
00ABA232  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00ABA237  48 81 C1 28 03 00 00            add rcx, 0x328
00ABA23E  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
00ABA243  40 88 7C 24 20                  mov byte ptr [rsp + 0x20], dil
00ABA248  45 33 C9                        xor r9d, r9d
00ABA24B  4C 8B 05 3E B5 44 00            mov r8, qword ptr [rip + 0x44b53e]
00ABA252  33 D2                           xor edx, edx
00ABA254  E8 87 E3 90 FF                  call 0x1403c85e0
00ABA259  84 C0                           test al, al
00ABA25B  74 14                           je 0x140aba271
00ABA25D  F0 01 3D 74 F8 51 00            lock add dword ptr [rip + 0x51f874], edi
00ABA264  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00ABA269  0F BA A8 C8 00 00 00 18         bts dword ptr [rax + 0xc8], 0x18
00ABA271  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00ABA276  48 8B 0D 8B 8A 55 FF            mov rcx, qword ptr [rip - 0xaa7575]
00ABA27D  48 8B C1                        mov rax, rcx
00ABA280  F0 48 0F C1 05 67 49 35 00      lock xadd qword ptr [rip + 0x354967], rax
00ABA289  48 03 C1                        add rax, rcx
00ABA28C  89 42 38                        mov dword ptr [rdx + 0x38], eax
00ABA28F  48 C1 E8 20                     shr rax, 0x20
00ABA293  89 42 3C                        mov dword ptr [rdx + 0x3c], eax
00ABA296  F0 44 09 24 24                  lock or dword ptr [rsp], r12d
00ABA29B  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00ABA2A0  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
00ABA2A4  E8 67 57 7A FF                  call 0x14025fa10
00ABA2A9  E8 02 36 7A FF                  call 0x14025d8b0
00ABA2AE  44 88 64 24 51                  mov byte ptr [rsp + 0x51], r12b
00ABA2B3  48 8D 84 24 B8 00 00 00         lea rax, [rsp + 0xb8]
00ABA2BB  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00ABA2C0  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
00ABA2C5  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00ABA2CA  44 8B CF                        mov r9d, edi
00ABA2CD  44 8B 84 24 94 00 00 00         mov r8d, dword ptr [rsp + 0x94]
00ABA2D5  33 D2                           xor edx, edx
00ABA2D7  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00ABA2DC  E8 BF F4 DF FF                  call 0x1408b97a0
00ABA2E1  8B D8                           mov ebx, eax
00ABA2E3  85 C0                           test eax, eax
00ABA2E5  0F 88 83 FA FF FF               js 0x140ab9d6e
00ABA2EB  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
00ABA2F0  BA FF 01 0F 00                  mov edx, 0xf01ff
00ABA2F5  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00ABA2FA  E8 31 C1 DF FF                  call 0x1408b6430
00ABA2FF  8B D8                           mov ebx, eax
00ABA301  85 C0                           test eax, eax
00ABA303  78 19                           js 0x140aba31e
00ABA305  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00ABA30A  E8 E5 C0 DF FF                  call 0x1408b63f4
00ABA30F  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00ABA314  E8 37 F0 83 FF                  call 0x1402f9350
00ABA319  E9 50 FA FF FF                  jmp 0x140ab9d6e
00ABA31E  40 8A 74 24 50                  mov sil, byte ptr [rsp + 0x50]
00ABA323  4C 8B BC 24 90 01 00 00         mov r15, qword ptr [rsp + 0x190]
00ABA32B  44 38 64 24 51                  cmp byte ptr [rsp + 0x51], r12b
00ABA330  74 41                           je 0x140aba373
00ABA332  85 DB                           test ebx, ebx
00ABA334  78 25                           js 0x140aba35b
00ABA336  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
00ABA33B  48 8B 0D C6 89 55 FF            mov rcx, qword ptr [rip - 0xaa763a]
00ABA342  48 8B C1                        mov rax, rcx
00ABA345  F0 48 0F C1 05 A2 48 35 00      lock xadd qword ptr [rip + 0x3548a2], rax
00ABA34E  48 03 C1                        add rax, rcx
00ABA351  89 42 38                        mov dword ptr [rdx + 0x38], eax
00ABA354  48 C1 E8 20                     shr rax, 0x20
00ABA358  89 42 3C                        mov dword ptr [rdx + 0x3c], eax
00ABA35B  F0 44 09 24 24                  lock or dword ptr [rsp], r12d
00ABA360  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00ABA365  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
00ABA369  E8 A2 56 7A FF                  call 0x14025fa10
00ABA36E  E8 3D 35 7A FF                  call 0x14025d8b0
00ABA373  85 DB                           test ebx, ebx
00ABA375  79 24                           jns 0x140aba39b
00ABA377  40 84 F6                        test sil, sil
00ABA37A  74 0A                           je 0x140aba386
00ABA37C  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00ABA381  E8 CA EF 83 FF                  call 0x1402f9350
00ABA386  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00ABA38E  48 85 C9                        test rcx, rcx
00ABA391  74 08                           je 0x140aba39b
00ABA393  41 8A D5                        mov dl, r13b
00ABA396  E8 D5 74 DE FF                  call 0x1408a1870
00ABA39B  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00ABA3A0  48 85 C9                        test rcx, rcx
00ABA3A3  74 08                           je 0x140aba3ad
00ABA3A5  41 8A D5                        mov dl, r13b
00ABA3A8  E8 93 D8 F0 FF                  call 0x1409c7c40
00ABA3AD  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00ABA3B2  48 85 F6                        test rsi, rsi
00ABA3B5  74 0E                           je 0x140aba3c5
00ABA3B7  44 8A C7                        mov r8b, dil
00ABA3BA  41 8A D5                        mov dl, r13b
00ABA3BD  48 8B CE                        mov rcx, rsi
00ABA3C0  E8 8B 4B F7 FF                  call 0x140a2ef50
00ABA3C5  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
00ABA3CA  48 85 F6                        test rsi, rsi
00ABA3CD  74 08                           je 0x140aba3d7
00ABA3CF  48 8B CE                        mov rcx, rsi
00ABA3D2  E8 79 EF 83 FF                  call 0x1402f9350
00ABA3D7  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00ABA3DF  48 85 C9                        test rcx, rcx
00ABA3E2  74 07                           je 0x140aba3eb
00ABA3E4  33 D2                           xor edx, edx
00ABA3E6  E8 85 84 0C 00                  call 0x140b82870
00ABA3EB  85 DB                           test ebx, ebx
00ABA3ED  78 0F                           js 0x140aba3fe
00ABA3EF  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
00ABA3F7  49 89 07                        mov qword ptr [r15], rax
00ABA3FA  EB 02                           jmp 0x140aba3fe
00ABA3FC  EB 02                           jmp 0x140aba400
00ABA3FE  8B C3                           mov eax, ebx
00ABA400  48 81 C4 50 01 00 00            add rsp, 0x150
00ABA407  41 5F                           pop r15
00ABA409  41 5E                           pop r14
00ABA40B  41 5D                           pop r13
00ABA40D  41 5C                           pop r12
00ABA40F  5F                              pop rdi
00ABA410  5E                              pop rsi
00ABA411  5B                              pop rbx
00ABA412  C3                              ret
00ABA413  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtCreateLowBoxToken(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, unsigned int a6, __int64 a7, unsigned int a8, unsigned __int8 a9)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m104;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int8 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int8 v_stack_m137;
    unsigned __int8 v_stack_m138;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int8 v_stack_m160;
    unsigned int v_stack_m168;
    unsigned int v_stack_m188;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned int v_stack_mF8;
    unsigned int v_stack_mFC;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (336);
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    a4 = 0;
    if ((unsigned int)(result) == 0) goto loc_00AB9B73;
    v_stack_mF0 = 0;
    v_stack_m100 = 0;
    v_stack_mE0 = 0;
    v_stack_mE8 = 0;
    v_stack_mC0 = v_xmm0;
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AB9978;
    if (a1 < a2) { a2 = a1; }
    *(unsigned __int64 *)(a2) = *(unsigned __int64 *)(a2);
    if ((unsigned int)(a8) * 8 == 0) goto loc_00AB9971;
    result = (unsigned int)(a8);
    if (((a9) & (7)) != 0) {
        result = ExRaiseDatatypeMisalignment((unsigned int)(a8) * 8, a2, a3, a4);
    }
    a1 = ((unsigned int)(a8) * 8) + (a9);
    if (a1 > a2) goto loc_00AB996F;
    result = a9;
    if (a1 < a9) {
        result = *(unsigned __int8 *)(a2);
    }
    goto loc_00AB9978;
loc_00AB9978:
    if (a2 != 0) goto loc_00AB9987;
    goto loc_00ABA400;
loc_00AB9987:
    if (a5 == 0) goto loc_00AB9C57;
    if (a8 != 0) goto loc_00AB99BA;
    if (a9 != 0) goto loc_00AB9C89;
    if (a8 == 0) goto loc_00AB99C8;
loc_00AB99BA:
    if (a9 == 0) goto loc_00AB9C89;
loc_00AB99C8:
    v_stack_m158 = v_stack_mE8;
    v_stack_m160 = 1;
    result = SeCaptureSid(a5, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a3, a4);
    if (sign_flag) goto loc_00AB9B29;
    if ((unsigned int)((unsigned int)(a6)) != 0) goto loc_00AB9A0E;
    if (a7 != 0) goto loc_00AB9A19;
    if ((unsigned int)((unsigned int)(a6)) == 0) goto loc_00AB9A23;
loc_00AB9A0E:
    if (a7 != 0) goto loc_00AB9A23;
loc_00AB9A19:
    goto loc_00AB9B29;
loc_00AB9A23:
    v_rbx = (unsigned int)(0xC0000030ULL);
    if (a7 != 0) {
        result = v_stack_m100;
        v_stack_m148 = result;
        result = v_stack_mF0;
        v_stack_m150 = result;
        a4 = 0;
        a3 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        a2 = (unsigned int)((unsigned int)(a6));
        result = SeCaptureSidAndAttributesArray(a7, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    if (sign_flag) goto loc_00AB9B29;
    result = SeCaptureHandles((unsigned int)((unsigned int)((unsigned int)(a8))), a9, v_stack_mE0, a4);
    v_rbx = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        result = v_stack_mC0;
        v_stack_m88 = result;
        v_stack_mC0 = 48;
        result = v_stack_mE8;
        v_stack_mB0 = result;
        result = v_stack_mF0;
        v_stack_mA8 = result;
        v_stack_mA0 = (unsigned int)((unsigned int)(a6));
        v_stack_mB8 = a2;
        result = v_stack_mE0;
        v_stack_m80 = result;
        v_stack_m78 = (unsigned int)((unsigned int)(a8));
        result = v_stack_m90;
        v_stack_m160 = result;
        v_stack_m168 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        a4 = 0;
        a3 = v_stack_p18;
        a2 = 0;
        a1 = v_stack_p8;
        result = SepCreateAppContainerToken(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    if (v_stack_mF0 != 0) {
        a2 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        result = SeReleaseLuidAndAttributesArray(v_stack_mF0, a2, a3, a4);
    }
    if (v_stack_mE8 != 0) {
        a3 = 1;
        a2 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        result = SeReleaseSid(v_stack_mE8, a2, a3, a4);
    }
    if (v_stack_mE0 == 0) goto loc_00ABA3FE;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_mE0, a2, a3, a4);
    goto loc_00ABA3FE;
loc_00AB9B73:
    v_stack_m120 = a4;
    v_stack_mFC = (unsigned int)(a4);
    v_stack_mD8 = a4;
    v_stack_m118 = a4;
    v_stack_mC8 = a4;
    v_stack_mD0 = a4;
    v_stack_m130 = a4;
    v_stack_mF8 = 1;
    v_stack_m137 = (unsigned __int8)(a4);
    v_stack_m138 = (unsigned __int8)(a4);
    v_stack_m108 = (unsigned int)(a4);
    v_stack_m128 = (unsigned __int8)(a4);
    result = 0;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AB9C4A;
    a1 = 0;
    if (((unsigned int)(a8)) < 0) { a1 = (unsigned int)(a8); }
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(a1);
    if ((unsigned int)(a8) * 8 == 0) goto loc_00AB9C43;
    result = (unsigned int)(a8);
    if (((a9) & (7)) != 0) {
        result = ExRaiseDatatypeMisalignment((unsigned int)(a8) * 8, a2, a3, a4);
    }
    a1 = ((unsigned int)(a8) * 8) + (a9);
    if (a1 > 0) goto loc_00AB9C41;
    result = a9;
    if (a1 < a9) {
        result = *(unsigned __int8 *)(a2);
    }
    goto loc_00AB9C4A;
loc_00AB9C4A:
    if (a5 != 0) goto loc_00AB9C61;
loc_00AB9C57:
    goto loc_00ABA400;
loc_00AB9C61:
    if (a8 != ((unsigned int)(a4))) goto loc_00AB9C7F;
    if (a9 != a4) goto loc_00AB9C89;
    if (a8 == ((unsigned int)(a4))) goto loc_00AB9C93;
loc_00AB9C7F:
    if (a9 != a4) goto loc_00AB9C93;
loc_00AB9C89:
    goto loc_00ABA400;
loc_00AB9C93:
    v_stack_m110 = a4;
    v_stack_m160 = v_stack_mC8;
    v_stack_m168 = v_stack_m110;
    result = ObReferenceObjectByHandle(0, 2, *(unsigned __int64 *)(v_rip + 5366662), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_r12 = 0;
    if (sign_flag) goto loc_00ABA400;
    v_stack_m158 = v_stack_m118;
    v_stack_m160 = 1;
    result = SeCaptureSid(a5, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), *(unsigned __int64 *)(v_rip + 5366662), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (sign_flag) goto loc_00ABA32B;
    result = SepCheckCreateAppContainer(v_stack_m118, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), *(unsigned __int64 *)(v_rip + 5366662), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (sign_flag) goto loc_00ABA32B;
    if ((*(unsigned int *)(v_stack_m110 + 192)) == 1) goto loc_00AB9D2C;
    if ((*(unsigned int *)(v_stack_m110 + 196)) >= 2) goto loc_00AB9D2C;
    goto loc_00ABA32B;
loc_00AB9D2C:
    v_r15 = (unsigned int)(v_stack_mC4);
    if ((unsigned int)((unsigned int)(a6)) != 0) { v_r15 = (unsigned int)((unsigned int)(a6)); }
    v_stack_mF4 = (unsigned int)(v_r15);
    if ((unsigned int)((unsigned int)(a6)) != 0) goto loc_00AB9D5F;
    if (a7 != 0) goto loc_00AB9D69;
    if ((unsigned int)((unsigned int)(a6)) == 0) goto loc_00AB9D76;
loc_00AB9D5F:
    if (a7 != 0) goto loc_00AB9D76;
loc_00AB9D69:
loc_00AB9D6E:
    goto loc_00ABA323;
loc_00AB9D76:
    v_rbx = (unsigned int)(0xC0000030ULL);
    if (a7 != 0) {
        result = v_stack_mFC;
        v_stack_m148 = result;
        result = v_stack_m120;
        v_stack_m150 = result;
        v_stack_m168 = 0;
        a4 = 0;
        a3 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        a2 = (unsigned int)((unsigned int)(a6));
        result = SeCaptureSidAndAttributesArray(a7, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    if (sign_flag) goto loc_00AB9D6E;
    result = SeCaptureHandles((unsigned int)(a8), a9, v_stack_mD8, a4);
    if (sign_flag) goto loc_00AB9D6E;
    result = RtlIsPackageSid(v_stack_m118, a9, v_stack_mD8, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00AB9DEA;
loc_00AB9DE3:
    goto loc_00AB9D6E;
loc_00AB9DEA:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_stack_m118 + 1)) - (8));
    if ((((unsigned __int8)(a1)) & (251)) == 0) goto loc_00AB9E04;
    goto loc_00AB9D6E;
loc_00AB9E04:
loc_00AB9E07:
    if (0 >= ((unsigned int)((unsigned int)(a6)))) goto loc_00AB9E5A;
    v_r15 = (0) + (0);
    result = RtlIsCapabilitySid(*(unsigned __int64 *)(v_stack_m120 + v_r15 * 8), a9, v_stack_mD8, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AB9E4D;
    v_rsi = 0;
loc_00AB9E26:
    if (0 >= 0) goto loc_00AB9E49;
    result = (0) + (0);
    result = RtlEqualSid(*(unsigned __int64 *)(v_stack_m120 + v_r15 * 8), *(unsigned __int64 *)(v_stack_m120 + result * 8), v_stack_mD8, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00AB9E4D;
    v_rsi = (unsigned int)((v_rsi) + (1));
    goto loc_00AB9E26;
loc_00AB9E49:
    v_rbx = (unsigned int)((0) + (1));
    goto loc_00AB9E07;
loc_00AB9E4D:
    v_r12 = 0;
    goto loc_00ABA31E;
loc_00AB9E5A:
    result = SepCapabilitiesHasAppSiloBaseSID((unsigned int)((unsigned int)((unsigned int)(a6))), v_stack_m120, v_stack_mD8, a4);
    v_r12 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00AB9E95;
loc_00AB9E71:
    if (0 >= ((unsigned int)((unsigned int)(a6)))) goto loc_00AB9E95;
    result = (0) + (0);
    result = SepIsAppSiloCapability(*(unsigned __int64 *)(v_stack_m120 + result * 8), v_stack_m120, v_stack_mD8, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00AB9DE3;
    v_rbx = (unsigned int)((0) + (1));
    goto loc_00AB9E71;
loc_00AB9E95:
    result = RtlGetAppContainerSidType(v_stack_m118, v_stack_m108, v_stack_mD8, a4);
    if (sign_flag) goto loc_00AB9D6E;
    if (v_stack_m108 != 1) goto loc_00AB9EE9;
    v_stack_m168 = v_stack_m128;
    result = SepCheckCapabilities(v_stack_m110, (unsigned int)((unsigned int)((unsigned int)(a6))), v_stack_m120, a4);
    if (v_stack_m128 != 0) goto loc_00AB9EE9;
    goto loc_00AB9D6E;
loc_00AB9EE9:
    if (sign_flag) goto loc_00AB9D6E;
    result = Feature_871661881__private_IsEnabledDeviceUsageNoInline(v_stack_m110, (unsigned int)((unsigned int)((unsigned int)(a6))), v_stack_m120, a4);
    if ((unsigned int)(result) == 0) goto loc_00ABA031;
    v_stack_m104 = 0;
    result = RtlQueryElevationFlags(v_stack_m104, (unsigned int)((unsigned int)((unsigned int)(a6))), v_stack_m120, a4);
    result = (unsigned __int8)(((unsigned int)(v_stack_m104)) & (24));
    if (((unsigned __int8)(result)) != 16) goto loc_00ABA031;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m110 + 48), 1, v_stack_m120, a4);
    result = SepLocateTokenIntegrity(v_stack_m110, 1, v_stack_m120, a4);
    if (result == 0) goto loc_00ABA01B;
    result = RtlSubAuthorityCountSid(*(unsigned __int64 *)(result), 1, v_stack_m120, a4);
    if ((unsigned __int8)(*(unsigned __int8 *)(result)) == 0) goto loc_00ABA01B;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(result)))) - (1));
    result = RtlSubAuthoritySid(*(unsigned __int64 *)(result), a2, v_stack_m120, a4);
    if ((*(unsigned int *)(result)) < 0x3000ULL) goto loc_00ABA01B;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = SeCaptureSubjectContext(v_stack_m58, a2, v_stack_m120, a4);
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m48 + 48), 1, v_stack_m120, a4);
    result = SepLocateTokenIntegrity(v_stack_m48, 1, v_stack_m120, a4);
    result = RtlSubAuthorityCountSid(*(unsigned __int64 *)(result), 1, v_stack_m120, a4);
    if ((unsigned __int8)(*(unsigned __int8 *)(result)) == 0) goto loc_00AB9FF8;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(result)))) - (1));
    result = RtlSubAuthoritySid(*(unsigned __int64 *)(result), a2, v_stack_m120, a4);
    v_rbx = (unsigned int)(0xC0000022ULL);
    if ((*(unsigned int *)(result)) < 0x3000ULL) {
        v_rbx = 0xC0000022ULL;
    }
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m48 + 48), a2, v_stack_m120, a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m48 + 48), a2, v_stack_m120, a4);
    result = SeReleaseSubjectContext(v_stack_m58, a2, v_stack_m120, a4);
    v_r12 = 0;
loc_00ABA01B:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m110 + 48), a2, v_stack_m120, a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m110 + 48), a2, v_stack_m120, a4);
    if (sign_flag) goto loc_00ABA31E;
loc_00ABA031:
    v_stack_m150 = v_stack_m130;
    v_stack_m158 = 0;
    v_stack_m160 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m168 = 0;
    a3 = 0;
    result = SepDuplicateToken(v_stack_m110, v_stack_p20, a3, 1);
    if (sign_flag) goto loc_00ABA31E;
    v_stack_m138 = 1;
    result = SeSetMandatoryPolicyToken(v_stack_m130, v_stack_mF8, a3, 1);
    if (sign_flag) goto loc_00ABA323;
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_stack_m130 + 48), 1, a3, 1);
    v_stack_m137 = 1;
    result = SepLocateTokenIntegrity(v_stack_m130, 1, a3, 1);
    if (result == 0) goto loc_00ABA13B;
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1);
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) != 0) {
        a2 = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1));
        a2 = (unsigned int)((a2) - (1));
        result = RtlSubAuthoritySid(*(unsigned __int64 *)(result), a2, a3, 1);
        *(unsigned int *)(result) = 0x1000ULL;
    }
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(result), a2, a3, 1);
    if ((unsigned int)(result) == 0) goto loc_00ABA124;
    goto loc_00ABA12C;
loc_00ABA124:
loc_00ABA12C:
    goto loc_00ABA140;
loc_00ABA13B:
loc_00ABA140:
    if (sign_flag) goto loc_00ABA323;
    result = SepSetTokenCapabilities(v_stack_m130, v_stack_m118, v_stack_m120, (unsigned int)((unsigned int)((unsigned int)(a6))));
    if (sign_flag) goto loc_00ABA31E;
    result = SepSetTokenLowboxNumber(v_stack_m130, v_stack_m118, v_stack_m120, (unsigned int)((unsigned int)((unsigned int)(a6))));
    if (sign_flag) goto loc_00ABA31E;
    v_stack_m68 = v_stack_m118;
    result = SepSetTokenCachedHandles(v_stack_m130, v_stack_m70, (unsigned int)(a8), v_stack_mD8);
    if (sign_flag) goto loc_00ABA31E;
    result = SepSetTokenPackage(v_stack_m130, v_stack_m118, (unsigned int)(a8), v_stack_mD8);
    if (sign_flag) goto loc_00ABA31E;
    result = SepAppendAceToTokenDefaultDacl(v_stack_m130, v_stack_m118, (unsigned int)(a8), v_stack_mD8);
    if (sign_flag) goto loc_00ABA31E;
    v_stack_m160 = 0;
    v_stack_m168 = 1;
    a4 = 0;
    a2 = 0;
    result = SepSidInTokenSidHash(v_stack_m130 + 808, a2, *(unsigned __int64 *)(v_rip + 4502907), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00ABA228;
    goto loc_00ABA271;
loc_00ABA228:
    a1 = (v_stack_m130) + (808);
    v_stack_m160 = 0;
    v_stack_m168 = 1;
    a4 = 0;
    a2 = 0;
    result = SepSidInTokenSidHash(a1, a2, *(unsigned __int64 *)(v_rip + 4502846), a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m130;
    }
    result = (*(unsigned __int64 *)(v_rip - 11171189)) + (*(unsigned __int64 *)(v_rip - 11171189));
    *(unsigned int *)(v_stack_m130 + 56) = (unsigned int)(result);
    result = (result) >> (32);
    *(unsigned int *)(v_stack_m130 + 60) = (unsigned int)(result);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m130 + 48), v_stack_m130, *(unsigned __int64 *)(v_rip + 4502846), a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m130 + 48), v_stack_m130, *(unsigned __int64 *)(v_rip + 4502846), a4);
    v_stack_m137 = 0;
    v_stack_m158 = v_stack_mD0;
    v_stack_m160 = 0;
    v_stack_m168 = 0;
    a2 = 0;
    result = ObInsertObjectEx(v_stack_m130, a2, (unsigned int)(v_stack_mF4), 1);
    if (sign_flag) goto loc_00AB9D6E;
    result = SepAppendAceToTokenObjectAcl(v_stack_m130, (unsigned int)(0xF01FFULL), v_stack_m118, 1);
    if (sign_flag) goto loc_00ABA31E;
    result = SepFinalizeTokenAcls(v_stack_m130, (unsigned int)(0xF01FFULL), v_stack_m118, 1);
    result = ObfDereferenceObject(v_stack_m130, (unsigned int)(0xF01FFULL), v_stack_m118, 1);
    goto loc_00AB9D6E;
loc_00ABA31E:
loc_00ABA323:
loc_00ABA32B:
    if (v_stack_m137 == 0) goto loc_00ABA373;
    if (!(sign_flag)) {
        a2 = v_stack_m130;
        a1 = *(unsigned __int64 *)(v_rip - 11171386);
        result = a1;
        result = (result) + (a1);
        *(unsigned int *)(a2 + 56) = (unsigned int)(result);
        result = (result) >> (32);
        *(unsigned int *)(a2 + 60) = (unsigned int)(result);
    }
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m130 + 48), a2, v_stack_m118, 1);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m130 + 48), a2, v_stack_m118, 1);
loc_00ABA373:
    if (!sign_flag) goto loc_00ABA39B;
    if ((unsigned __int8)(v_stack_m138) != 0) {
        a1 = v_stack_m130;
        result = ObfDereferenceObject(a1, a2, v_stack_m118, 1);
    }
    if (v_stack_mD0 != 0) {
        a2 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        result = ObCloseHandle(v_stack_mD0, a2, v_stack_m118, 1);
    }
    if (v_stack_m120 != 0) {
        a2 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        result = SeReleaseLuidAndAttributesArray(v_stack_m120, a2, v_stack_m118, 1);
    }
    if (v_stack_m118 != 0) {
        a3 = 1;
        a2 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        a1 = v_stack_m118;
        result = SeReleaseSid(a1, a2, a3, 1);
    }
    if (v_stack_m110 != 0) {
        a1 = v_stack_m110;
        result = ObfDereferenceObject(a1, a2, a3, 1);
    }
    if (v_stack_mD8 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_mD8, a2, a3, 1);
    }
    if (sign_flag) goto loc_00ABA3FE;
    *(unsigned __int64 *)(v_stack_p8) = v_stack_mD0;
    goto loc_00ABA3FE;
loc_00ABA3FE:
loc_00ABA400:
    v_rsp = (v_rsp) + (336);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t NtCreateLowBoxToken(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, int64_t Arg7, uint32_t Arg8, uint8_t Arg9)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m104;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint8_t v_stack_m128;
    uint64_t v_stack_m130;
    uint8_t v_stack_m137;
    uint8_t v_stack_m138;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint8_t v_stack_m160;
    uint32_t v_stack_m168;
    uint32_t v_stack_m188;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint32_t v_stack_mF8;
    uint32_t v_stack_mFC;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (336);
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    Arg4 = 0;
    if ((uint32_t)(result) == 0) goto loc_00AB9B73;
    v_stack_mF0 = 0;
    v_stack_m100 = 0;
    v_stack_mE0 = 0;
    v_stack_mE8 = 0;
    v_stack_mC0 = v_xmm0;
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = v_xmm0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AB9978;
    if (Arg1 < Arg2) { Arg2 = Arg1; }
    *(uint64_t *)(Arg2) = *(uint64_t *)(Arg2);
    if ((uint32_t)(Arg8) * 8 == 0) goto loc_00AB9971;
    result = (uint32_t)(Arg8);
    if (((Arg9) & (7)) != 0) {
        result = ExRaiseDatatypeMisalignment((uint32_t)(Arg8) * 8, Arg2, Arg3, Arg4);
    }
    Arg1 = ((uint32_t)(Arg8) * 8) + (Arg9);
    if (Arg1 > Arg2) goto loc_00AB996F;
    result = Arg9;
    if (Arg1 < Arg9) {
        result = *(uint8_t *)(Arg2);
    }
    goto loc_00AB9978;
loc_00AB9978:
    if (Arg2 != 0) goto loc_00AB9987;
    goto loc_00ABA400;
loc_00AB9987:
    if (Arg5 == 0) goto loc_00AB9C57;
    if (Arg8 != 0) goto loc_00AB99BA;
    if (Arg9 != 0) goto loc_00AB9C89;
    if (Arg8 == 0) goto loc_00AB99C8;
loc_00AB99BA:
    if (Arg9 == 0) goto loc_00AB9C89;
loc_00AB99C8:
    v_stack_m158 = v_stack_mE8;
    v_stack_m160 = 1;
    result = SeCaptureSid(Arg5, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg3, Arg4);
    if (sign_flag) goto loc_00AB9B29;
    if ((uint32_t)((uint32_t)(Arg6)) != 0) goto loc_00AB9A0E;
    if (Arg7 != 0) goto loc_00AB9A19;
    if ((uint32_t)((uint32_t)(Arg6)) == 0) goto loc_00AB9A23;
loc_00AB9A0E:
    if (Arg7 != 0) goto loc_00AB9A23;
loc_00AB9A19:
    goto loc_00AB9B29;
loc_00AB9A23:
    local_rbx = (uint32_t)(0xC0000030ULL);
    if (Arg7 != 0) {
        result = v_stack_m100;
        v_stack_m148 = result;
        result = v_stack_mF0;
        v_stack_m150 = result;
        Arg4 = 0;
        Arg3 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        Arg2 = (uint32_t)((uint32_t)(Arg6));
        result = SeCaptureSidAndAttributesArray(Arg7, Arg2, Arg3, Arg4);
        local_rbx = (uint32_t)(result);
    }
    if (sign_flag) goto loc_00AB9B29;
    result = SeCaptureHandles((uint32_t)((uint32_t)((uint32_t)(Arg8))), Arg9, v_stack_mE0, Arg4);
    local_rbx = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        result = v_stack_mC0;
        v_stack_m88 = result;
        v_stack_mC0 = 48;
        result = v_stack_mE8;
        v_stack_mB0 = result;
        result = v_stack_mF0;
        v_stack_mA8 = result;
        v_stack_mA0 = (uint32_t)((uint32_t)(Arg6));
        v_stack_mB8 = Arg2;
        result = v_stack_mE0;
        v_stack_m80 = result;
        v_stack_m78 = (uint32_t)((uint32_t)(Arg8));
        result = v_stack_m90;
        v_stack_m160 = result;
        v_stack_m168 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        Arg4 = 0;
        Arg3 = v_stack_p18;
        Arg2 = 0;
        Arg1 = v_stack_p8;
        result = SepCreateAppContainerToken(Arg1, Arg2, Arg3, Arg4);
        local_rbx = (uint32_t)(result);
    }
    if (v_stack_mF0 != 0) {
        Arg2 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        result = SeReleaseLuidAndAttributesArray(v_stack_mF0, Arg2, Arg3, Arg4);
    }
    if (v_stack_mE8 != 0) {
        Arg3 = 1;
        Arg2 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        result = SeReleaseSid(v_stack_mE8, Arg2, Arg3, Arg4);
    }
    if (v_stack_mE0 == 0) goto loc_00ABA3FE;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_mE0, Arg2, Arg3, Arg4);
    goto loc_00ABA3FE;
loc_00AB9B73:
    v_stack_m120 = Arg4;
    v_stack_mFC = (uint32_t)(Arg4);
    v_stack_mD8 = Arg4;
    v_stack_m118 = Arg4;
    v_stack_mC8 = Arg4;
    v_stack_mD0 = Arg4;
    v_stack_m130 = Arg4;
    v_stack_mF8 = 1;
    v_stack_m137 = (uint8_t)(Arg4);
    v_stack_m138 = (uint8_t)(Arg4);
    v_stack_m108 = (uint32_t)(Arg4);
    v_stack_m128 = (uint8_t)(Arg4);
    result = 0;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = 0;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AB9C4A;
    Arg1 = 0;
    if (((uint32_t)(Arg8)) < 0) { Arg1 = (uint32_t)(Arg8); }
    *(uint64_t *)(Arg1) = *(uint64_t *)(Arg1);
    if ((uint32_t)(Arg8) * 8 == 0) goto loc_00AB9C43;
    result = (uint32_t)(Arg8);
    if (((Arg9) & (7)) != 0) {
        result = ExRaiseDatatypeMisalignment((uint32_t)(Arg8) * 8, Arg2, Arg3, Arg4);
    }
    Arg1 = ((uint32_t)(Arg8) * 8) + (Arg9);
    if (Arg1 > 0) goto loc_00AB9C41;
    result = Arg9;
    if (Arg1 < Arg9) {
        result = *(uint8_t *)(Arg2);
    }
    goto loc_00AB9C4A;
loc_00AB9C4A:
    if (Arg5 != 0) goto loc_00AB9C61;
loc_00AB9C57:
    goto loc_00ABA400;
loc_00AB9C61:
    if (Arg8 != ((uint32_t)(Arg4))) goto loc_00AB9C7F;
    if (Arg9 != Arg4) goto loc_00AB9C89;
    if (Arg8 == ((uint32_t)(Arg4))) goto loc_00AB9C93;
loc_00AB9C7F:
    if (Arg9 != Arg4) goto loc_00AB9C93;
loc_00AB9C89:
    goto loc_00ABA400;
loc_00AB9C93:
    v_stack_m110 = Arg4;
    v_stack_m160 = v_stack_mC8;
    v_stack_m168 = v_stack_m110;
    result = ObReferenceObjectByHandle(0, 2, *(uint64_t *)(v_rip + 0x51E386), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    local_r12 = 0;
    if (sign_flag) goto loc_00ABA400;
    v_stack_m158 = v_stack_m118;
    v_stack_m160 = 1;
    result = SeCaptureSid(Arg5, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), *(uint64_t *)(v_rip + 0x51E386), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (sign_flag) goto loc_00ABA32B;
    result = SepCheckCreateAppContainer(v_stack_m118, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), *(uint64_t *)(v_rip + 0x51E386), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (sign_flag) goto loc_00ABA32B;
    if ((*(uint32_t *)(v_stack_m110 + 0xC0)) == 1) goto loc_00AB9D2C;
    if ((*(uint32_t *)(v_stack_m110 + 0xC4)) >= 2) goto loc_00AB9D2C;
    goto loc_00ABA32B;
loc_00AB9D2C:
    local_r15 = (uint32_t)(v_stack_mC4);
    if ((uint32_t)((uint32_t)(Arg6)) != 0) { local_r15 = (uint32_t)((uint32_t)(Arg6)); }
    v_stack_mF4 = (uint32_t)(local_r15);
    if ((uint32_t)((uint32_t)(Arg6)) != 0) goto loc_00AB9D5F;
    if (Arg7 != 0) goto loc_00AB9D69;
    if ((uint32_t)((uint32_t)(Arg6)) == 0) goto loc_00AB9D76;
loc_00AB9D5F:
    if (Arg7 != 0) goto loc_00AB9D76;
loc_00AB9D69:
loc_00AB9D6E:
    goto loc_00ABA323;
loc_00AB9D76:
    local_rbx = (uint32_t)(0xC0000030ULL);
    if (Arg7 != 0) {
        result = v_stack_mFC;
        v_stack_m148 = result;
        result = v_stack_m120;
        v_stack_m150 = result;
        v_stack_m168 = 0;
        Arg4 = 0;
        Arg3 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        Arg2 = (uint32_t)((uint32_t)(Arg6));
        result = SeCaptureSidAndAttributesArray(Arg7, Arg2, Arg3, Arg4);
        local_rbx = (uint32_t)(result);
    }
    if (sign_flag) goto loc_00AB9D6E;
    result = SeCaptureHandles((uint32_t)(Arg8), Arg9, v_stack_mD8, Arg4);
    if (sign_flag) goto loc_00AB9D6E;
    result = RtlIsPackageSid(v_stack_m118, Arg9, v_stack_mD8, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00AB9DEA;
loc_00AB9DE3:
    goto loc_00AB9D6E;
loc_00AB9DEA:
    Arg1 = (uint8_t)((*(uint8_t *)(v_stack_m118 + 0x1)) - (8));
    if ((((uint8_t)(Arg1)) & (251)) == 0) goto loc_00AB9E04;
    goto loc_00AB9D6E;
loc_00AB9E04:
loc_00AB9E07:
    if (0 >= ((uint32_t)((uint32_t)(Arg6)))) goto loc_00AB9E5A;
    local_r15 = (0) + (0);
    result = RtlIsCapabilitySid(*(uint64_t *)(v_stack_m120 + local_r15 * 8), Arg9, v_stack_mD8, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00AB9E4D;
    local_rsi = 0;
loc_00AB9E26:
    if (0 >= 0) goto loc_00AB9E49;
    result = (0) + (0);
    result = RtlEqualSid(*(uint64_t *)(v_stack_m120 + local_r15 * 8), *(uint64_t *)(v_stack_m120 + result * 8), v_stack_mD8, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00AB9E4D;
    local_rsi = (uint32_t)((local_rsi) + (1));
    goto loc_00AB9E26;
loc_00AB9E49:
    local_rbx = (uint32_t)((0) + (1));
    goto loc_00AB9E07;
loc_00AB9E4D:
    local_r12 = 0;
    goto loc_00ABA31E;
loc_00AB9E5A:
    result = SepCapabilitiesHasAppSiloBaseSID((uint32_t)((uint32_t)((uint32_t)(Arg6))), v_stack_m120, v_stack_mD8, Arg4);
    local_r12 = 0;
    if ((uint8_t)(result) != 0) goto loc_00AB9E95;
loc_00AB9E71:
    if (0 >= ((uint32_t)((uint32_t)(Arg6)))) goto loc_00AB9E95;
    result = (0) + (0);
    result = SepIsAppSiloCapability(*(uint64_t *)(v_stack_m120 + result * 8), v_stack_m120, v_stack_mD8, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00AB9DE3;
    local_rbx = (uint32_t)((0) + (1));
    goto loc_00AB9E71;
loc_00AB9E95:
    result = RtlGetAppContainerSidType(v_stack_m118, v_stack_m108, v_stack_mD8, Arg4);
    if (sign_flag) goto loc_00AB9D6E;
    if (v_stack_m108 != 1) goto loc_00AB9EE9;
    v_stack_m168 = v_stack_m128;
    result = SepCheckCapabilities(v_stack_m110, (uint32_t)((uint32_t)((uint32_t)(Arg6))), v_stack_m120, Arg4);
    if (v_stack_m128 != 0) goto loc_00AB9EE9;
    goto loc_00AB9D6E;
loc_00AB9EE9:
    if (sign_flag) goto loc_00AB9D6E;
    result = Feature_871661881__private_IsEnabledDeviceUsageNoInline(v_stack_m110, (uint32_t)((uint32_t)((uint32_t)(Arg6))), v_stack_m120, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00ABA031;
    v_stack_m104 = 0;
    result = RtlQueryElevationFlags(v_stack_m104, (uint32_t)((uint32_t)((uint32_t)(Arg6))), v_stack_m120, Arg4);
    result = (uint8_t)(((uint32_t)(v_stack_m104)) & (24));
    if (((uint8_t)(result)) != 16) goto loc_00ABA031;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m110 + 0x30), 1, v_stack_m120, Arg4);
    result = SepLocateTokenIntegrity(v_stack_m110, 1, v_stack_m120, Arg4);
    if (result == 0) goto loc_00ABA01B;
    result = RtlSubAuthorityCountSid(*(uint64_t *)(result), 1, v_stack_m120, Arg4);
    if ((uint8_t)(*(uint8_t *)(result)) == 0) goto loc_00ABA01B;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(result)))) - (1));
    result = RtlSubAuthoritySid(*(uint64_t *)(result), Arg2, v_stack_m120, Arg4);
    if ((*(uint32_t *)(result)) < 0x3000ULL) goto loc_00ABA01B;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = SeCaptureSubjectContext(v_stack_m58, Arg2, v_stack_m120, Arg4);
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m48 + 0x30), 1, v_stack_m120, Arg4);
    result = SepLocateTokenIntegrity(v_stack_m48, 1, v_stack_m120, Arg4);
    result = RtlSubAuthorityCountSid(*(uint64_t *)(result), 1, v_stack_m120, Arg4);
    if ((uint8_t)(*(uint8_t *)(result)) == 0) goto loc_00AB9FF8;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(result)))) - (1));
    result = RtlSubAuthoritySid(*(uint64_t *)(result), Arg2, v_stack_m120, Arg4);
    local_rbx = (uint32_t)(0xC0000022ULL);
    if ((*(uint32_t *)(result)) < 0x3000ULL) {
        local_rbx = 0xC0000022ULL;
    }
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m48 + 0x30), Arg2, v_stack_m120, Arg4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m48 + 0x30), Arg2, v_stack_m120, Arg4);
    result = SeReleaseSubjectContext(v_stack_m58, Arg2, v_stack_m120, Arg4);
    local_r12 = 0;
loc_00ABA01B:
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m110 + 0x30), Arg2, v_stack_m120, Arg4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m110 + 0x30), Arg2, v_stack_m120, Arg4);
    if (sign_flag) goto loc_00ABA31E;
loc_00ABA031:
    v_stack_m150 = v_stack_m130;
    v_stack_m158 = 0;
    v_stack_m160 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m168 = 0;
    Arg3 = 0;
    result = SepDuplicateToken(v_stack_m110, v_stack_p20, Arg3, 1);
    if (sign_flag) goto loc_00ABA31E;
    v_stack_m138 = 1;
    result = SeSetMandatoryPolicyToken(v_stack_m130, v_stack_mF8, Arg3, 1);
    if (sign_flag) goto loc_00ABA323;
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_stack_m130 + 0x30), 1, Arg3, 1);
    v_stack_m137 = 1;
    result = SepLocateTokenIntegrity(v_stack_m130, 1, Arg3, 1);
    if (result == 0) goto loc_00ABA13B;
    result = *(uint8_t *)(*(uint64_t *)(result) + 0x1);
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1)) != 0) {
        Arg2 = (uint32_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1));
        Arg2 = (uint32_t)((Arg2) - (1));
        result = RtlSubAuthoritySid(*(uint64_t *)(result), Arg2, Arg3, 1);
        *(uint32_t *)(result) = 0x1000ULL;
    }
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(result), Arg2, Arg3, 1);
    if ((uint32_t)(result) == 0) goto loc_00ABA124;
    goto loc_00ABA12C;
loc_00ABA124:
loc_00ABA12C:
    goto loc_00ABA140;
loc_00ABA13B:
loc_00ABA140:
    if (sign_flag) goto loc_00ABA323;
    result = SepSetTokenCapabilities(v_stack_m130, v_stack_m118, v_stack_m120, (uint32_t)((uint32_t)((uint32_t)(Arg6))));
    if (sign_flag) goto loc_00ABA31E;
    result = SepSetTokenLowboxNumber(v_stack_m130, v_stack_m118, v_stack_m120, (uint32_t)((uint32_t)((uint32_t)(Arg6))));
    if (sign_flag) goto loc_00ABA31E;
    v_stack_m68 = v_stack_m118;
    result = SepSetTokenCachedHandles(v_stack_m130, v_stack_m70, (uint32_t)(Arg8), v_stack_mD8);
    if (sign_flag) goto loc_00ABA31E;
    result = SepSetTokenPackage(v_stack_m130, v_stack_m118, (uint32_t)(Arg8), v_stack_mD8);
    if (sign_flag) goto loc_00ABA31E;
    result = SepAppendAceToTokenDefaultDacl(v_stack_m130, v_stack_m118, (uint32_t)(Arg8), v_stack_mD8);
    if (sign_flag) goto loc_00ABA31E;
    v_stack_m160 = 0;
    v_stack_m168 = 1;
    Arg4 = 0;
    Arg2 = 0;
    result = SepSidInTokenSidHash(v_stack_m130 + 808, Arg2, *(uint64_t *)(v_rip + 0x44B57B), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00ABA228;
    goto loc_00ABA271;
loc_00ABA228:
    Arg1 = (v_stack_m130) + (808);
    v_stack_m160 = 0;
    v_stack_m168 = 1;
    Arg4 = 0;
    Arg2 = 0;
    result = SepSidInTokenSidHash(Arg1, Arg2, *(uint64_t *)(v_rip + 0x44B53E), Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m130;
    }
    result = (*(uint64_t *)(v_rip - 0xAA7575)) + (*(uint64_t *)(v_rip - 0xAA7575));
    *(uint32_t *)(v_stack_m130 + 0x38) = (uint32_t)(result);
    result = (result) >> (32);
    *(uint32_t *)(v_stack_m130 + 0x3C) = (uint32_t)(result);
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m130 + 0x30), v_stack_m130, *(uint64_t *)(v_rip + 0x44B53E), Arg4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m130 + 0x30), v_stack_m130, *(uint64_t *)(v_rip + 0x44B53E), Arg4);
    v_stack_m137 = 0;
    v_stack_m158 = v_stack_mD0;
    v_stack_m160 = 0;
    v_stack_m168 = 0;
    Arg2 = 0;
    result = ObInsertObjectEx(v_stack_m130, Arg2, (uint32_t)(v_stack_mF4), 1);
    if (sign_flag) goto loc_00AB9D6E;
    result = SepAppendAceToTokenObjectAcl(v_stack_m130, (uint32_t)(0xF01FFULL), v_stack_m118, 1);
    if (sign_flag) goto loc_00ABA31E;
    result = SepFinalizeTokenAcls(v_stack_m130, (uint32_t)(0xF01FFULL), v_stack_m118, 1);
    result = ObfDereferenceObject(v_stack_m130, (uint32_t)(0xF01FFULL), v_stack_m118, 1);
    goto loc_00AB9D6E;
loc_00ABA31E:
loc_00ABA323:
loc_00ABA32B:
    if (v_stack_m137 == 0) goto loc_00ABA373;
    if (!(sign_flag)) {
        Arg2 = v_stack_m130;
        Arg1 = *(uint64_t *)(v_rip - 0xAA763A);
        result = Arg1;
        result = (result) + (Arg1);
        *(uint32_t *)(Arg2 + 0x38) = (uint32_t)(result);
        result = (result) >> (32);
        *(uint32_t *)(Arg2 + 0x3C) = (uint32_t)(result);
    }
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m130 + 0x30), Arg2, v_stack_m118, 1);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m130 + 0x30), Arg2, v_stack_m118, 1);
loc_00ABA373:
    if (!sign_flag) goto loc_00ABA39B;
    if ((uint8_t)(v_stack_m138) != 0) {
        Arg1 = v_stack_m130;
        result = ObfDereferenceObject(Arg1, Arg2, v_stack_m118, 1);
    }
    if (v_stack_mD0 != 0) {
        Arg2 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        result = ObCloseHandle(v_stack_mD0, Arg2, v_stack_m118, 1);
    }
    if (v_stack_m120 != 0) {
        Arg2 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        result = SeReleaseLuidAndAttributesArray(v_stack_m120, Arg2, v_stack_m118, 1);
    }
    if (v_stack_m118 != 0) {
        Arg3 = 1;
        Arg2 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        Arg1 = v_stack_m118;
        result = SeReleaseSid(Arg1, Arg2, Arg3, 1);
    }
    if (v_stack_m110 != 0) {
        Arg1 = v_stack_m110;
        result = ObfDereferenceObject(Arg1, Arg2, Arg3, 1);
    }
    if (v_stack_mD8 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_mD8, Arg2, Arg3, 1);
    }
    if (sign_flag) goto loc_00ABA3FE;
    *(uint64_t *)(v_stack_p8) = v_stack_mD0;
    goto loc_00ABA3FE;
loc_00ABA3FE:
loc_00ABA400:
    local_rsp = (local_rsp) + (336);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB9880&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
