# SepFilterToken

- RVA: `0x009C6B80`–`0x009C7882` (길이 `3,330` bytes)
- VA: `0x00000001409C6B80`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A07E8`
- 디코드: `768`개 명령, `3,330/3,330` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **67**; 고유 호출 대상: **41**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x009C6C1E` → [RtlIsPackageSid](../A5/RtlIsPackageSid_function_00A5E73C.md) (function, `0x00A5E73C`)
- `0x009C6C2E` → [RtlIsCapabilitySid](../A5/RtlIsCapabilitySid_function_00A5ED84.md) (function, `0x00A5ED84`)
- `0x009C6C59` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009C6C9A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009C6CC1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009C6CD3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009C6CE6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009C6DB6` → [ObCreateObjectEx](../89/ObCreateObjectEx_function_0089B1E0.md) (function, `0x0089B1E0`)
- `0x009C6DC6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009C6DD0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009C6DEA` → [ExInitializeResourceLite](../../text/41/ExInitializeResourceLite_function_0041F9A0.md) (function, `0x0041F9A0`)
- `0x009C6EDA` → [RtlWalkFrameChain](../../text/2F/RtlWalkFrameChain_function_002F85E0.md) (function, `0x002F85E0`)
- `0x009C6F01` → [RtlWalkFrameChain](../../text/2F/RtlWalkFrameChain_function_002F85E0.md) (function, `0x002F85E0`)
- `0x009C6F1D` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x009C6F50` → [SepSetTokenSessionById](../A0/SepSetTokenSessionById_function_00A0DAE4.md) (function, `0x00A0DAE4`)
- `0x009C6F5B` → [Feature_2045735225__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_2045735225__private_IsEnabledDeviceUsageNoInline_function_004F0968.md) (function, `0x004F0968`)
- `0x009C6FCA` → [Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline_function_004F2D58.md) (function, `0x004F2D58`)
- `0x009C6FE1` → [Feature_AgentId2__private_IsEnabledDeviceUsageNoInline](../../text/60/Feature_AgentId2__private_IsEnabledDeviceUsageNoInline_function_006066CC.md) (function, `0x006066CC`)
- `0x009C7016` → [SepModifyTokenPolicyCounter](../79/SepModifyTokenPolicyCounter_function_0079D1E0.md) (function, `0x0079D1E0`)
- `0x009C7054` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009C707B` → [SepDuplicateLogonSessionReference](../../text/44/SepDuplicateLogonSessionReference_function_004463B0.md) (function, `0x004463B0`)
- `0x009C708A` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x009C708F` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x009C7097` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009C70A1` → [Feature_2045735225__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_2045735225__private_IsEnabledDeviceUsageNoInline_function_004F0968.md) (function, `0x004F0968`)
- `0x009C70CE` → [SepReferenceLogonSession](../A3/SepReferenceLogonSession_function_00A3B74C.md) (function, `0x00A3B74C`)
- `0x009C70E5` → [SepRefDerefLuidToIndexEntryIfNecessary](../9F/SepRefDerefLuidToIndexEntryIfNecessary_function_009FEFD8.md) (function, `0x009FEFD8`)
- `0x009C710E` → [AuthzBasepDuplicateSecurityAttributes](../../text/30/AuthzBasepDuplicateSecurityAttributes_function_003023C0.md) (function, `0x003023C0`)
- `0x009C712C` → [SepDuplicateTokenClaims](../A7/SepDuplicateTokenClaims_function_00A762C8.md) (function, `0x00A762C8`)
- `0x009C71FA` → [SepAddTokenLogonSession](../7A/SepAddTokenLogonSession_function_007A14E0.md) (function, `0x007A14E0`)
- `0x009C721A` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (function, `0x0020FF80`)
- `0x009C722A` → [SeIsSystemContext](../../text/60/SeIsSystemContext_function_006095B8.md) (function, `0x006095B8`)
- `0x009C7249` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009C72AA` → [SepDuplicateTokenUserAndGroups](../9F/SepDuplicateTokenUserAndGroups_function_009FDFD4.md) (function, `0x009FDFD4`)
- `0x009C72F2` → [RtlCopySidAndAttributesArray](../9A/RtlCopySidAndAttributesArray_function_009A8BE0.md) (function, `0x009A8BE0`)
- `0x009C733A` → [SepSidInSidAndAttributes](../9D/SepSidInSidAndAttributes_function_009D4A94.md) (function, `0x009D4A94`)
- `0x009C7377` → [RtlCopySidAndAttributesArray](../9A/RtlCopySidAndAttributesArray_function_009A8BE0.md) (function, `0x009A8BE0`)
- `0x009C73F0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009C74DF` → [SepDuplicateToken](../8B/SepDuplicateToken_function_008B87EC.md) (function, `0x008B87EC`)
- `0x009C74ED` → [SepStopReferencingLogonSession](../A8/SepStopReferencingLogonSession_function_00A8E35C.md) (function, `0x00A8E35C`)
- `0x009C74FB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009C7518` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009C752F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009C7587` → [SepSetTokenCapabilities](SepSetTokenCapabilities_function_009C9AF4.md) (function, `0x009C9AF4`)
- `0x009C75A5` → [SepSetTokenPackage](../A2/SepSetTokenPackage_function_00A20CB8.md) (function, `0x00A20CB8`)
- `0x009C7668` → [SepSetTokenTrust](../9E/SepSetTokenTrust_function_009E79B0.md) (function, `0x009E79B0`)
- `0x009C7678` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x009C7685` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x009C768A` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x009C76C3` → [SepRemoveDisabledGroupsAndPrivileges](../9D/SepRemoveDisabledGroupsAndPrivileges_function_009D48B4.md) (function, `0x009D48B4`)
- `0x009C76D9` → [RtlSidHashInitialize](../../text/41/RtlSidHashInitialize_function_00416EA0.md) (function, `0x00416EA0`)
- `0x009C76F2` → [RtlSidHashInitialize](../../text/41/RtlSidHashInitialize_function_00416EA0.md) (function, `0x00416EA0`)
- `0x009C76FB` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x009C7712` → [RtlIsSandboxedToken](../8B/RtlIsSandboxedToken_function_008B3AB0.md) (function, `0x008B3AB0`)
- `0x009C7721` → [RtlIsSandboxedToken](../8B/RtlIsSandboxedToken_function_008B3AB0.md) (function, `0x008B3AB0`)
- `0x009C7745` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x009C775A` → [SepNewTokenAsRestrictedAsProcessToken](../A2/SepNewTokenAsRestrictedAsProcessToken_function_00A20A98.md) (function, `0x00A20A98`)
- `0x009C7766` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x009C776B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x009C777F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009C7788` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x009C7799` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x009C77B7` → [RtlSidHashInitialize](../../text/41/RtlSidHashInitialize_function_00416EA0.md) (function, `0x00416EA0`)
- `0x009C782E` → [DbgPrint](../../text/35/DbgPrint_function_00358CB0.md) (function, `0x00358CB0`)
- `0x009C7859` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009C7863` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009C7876` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [SeFilterToken](../79/SeFilterToken_function_0079CD00.md) at `0x0079CDC7`
- [NtFilterToken](NtFilterToken_function_009C7890.md) at `0x009C7B57`

### Static image references
- `0x009C6C87` → RVA `0x00FD8010` (`PAGEDATA`; read)
- `0x009C6D75` → RVA `0x00FD8020` (`PAGEDATA`; read)
- `0x009C6DEF` → RVA `0x00012D08` (`.rdata`; read)
- `0x009C6DF9` → RVA `0x00E0EBF0` (`.data`; read/write)
- `0x009C6F84` → RVA `0x00FD9AD8` (`PAGEDATA`; read/write)
- `0x009C7296` → RVA `0x00E67BF0` (`.data`; read)
- `0x009C77C5` → RVA `0x00E67BA4` (`.data`; read)
- `0x009C77DE` → RVA `0x00E67B98` (`.data`; read)
- `0x009C77F3` → RVA `0x00E67BA8` (`.data`; read/write)
- `0x009C781C` → RVA `0x00E67BA0` (`.data`; read)
- `0x009C7827` → RVA `0x00B05DD0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **42**
  - `0x009C6C59` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009C6C9A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009C6CC1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009C6CD3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009C6CE6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009C6DC6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009C6DD0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009C6DEA` → [ExInitializeResourceLite](../../text/41/ExInitializeResourceLite_function_0041F9A0.md) (`PAGE` → `.text`)
  - `0x009C6EDA` → [RtlWalkFrameChain](../../text/2F/RtlWalkFrameChain_function_002F85E0.md) (`PAGE` → `.text`)
  - `0x009C6F01` → [RtlWalkFrameChain](../../text/2F/RtlWalkFrameChain_function_002F85E0.md) (`PAGE` → `.text`)
  - `0x009C6F1D` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x009C6F5B` → [Feature_2045735225__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_2045735225__private_IsEnabledDeviceUsageNoInline_function_004F0968.md) (`PAGE` → `.text`)
  - `0x009C6FCA` → [Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline_function_004F2D58.md) (`PAGE` → `.text`)
  - `0x009C6FE1` → [Feature_AgentId2__private_IsEnabledDeviceUsageNoInline](../../text/60/Feature_AgentId2__private_IsEnabledDeviceUsageNoInline_function_006066CC.md) (`PAGE` → `.text`)
  - `0x009C7054` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009C707B` → [SepDuplicateLogonSessionReference](../../text/44/SepDuplicateLogonSessionReference_function_004463B0.md) (`PAGE` → `.text`)
  - `0x009C708A` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x009C708F` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x009C7097` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009C70A1` → [Feature_2045735225__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_2045735225__private_IsEnabledDeviceUsageNoInline_function_004F0968.md) (`PAGE` → `.text`)
  - `0x009C710E` → [AuthzBasepDuplicateSecurityAttributes](../../text/30/AuthzBasepDuplicateSecurityAttributes_function_003023C0.md) (`PAGE` → `.text`)
  - `0x009C721A` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (`PAGE` → `.text`)
  - `0x009C722A` → [SeIsSystemContext](../../text/60/SeIsSystemContext_function_006095B8.md) (`PAGE` → `.text`)
  - `0x009C7249` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009C73F0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009C74FB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009C7518` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009C752F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009C7678` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x009C7685` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x009C768A` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x009C76D9` → [RtlSidHashInitialize](../../text/41/RtlSidHashInitialize_function_00416EA0.md) (`PAGE` → `.text`)
  - `0x009C76F2` → [RtlSidHashInitialize](../../text/41/RtlSidHashInitialize_function_00416EA0.md) (`PAGE` → `.text`)
  - `0x009C7745` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x009C7766` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x009C776B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x009C777F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009C77B7` → [RtlSidHashInitialize](../../text/41/RtlSidHashInitialize_function_00416EA0.md) (`PAGE` → `.text`)
  - `0x009C782E` → [DbgPrint](../../text/35/DbgPrint_function_00358CB0.md) (`PAGE` → `.text`)
  - `0x009C7859` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009C7863` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009C7876` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009C6B80  48 8B C4                        mov rax, rsp
009C6B83  48 89 58 08                     mov qword ptr [rax + 8], rbx
009C6B87  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
009C6B8B  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
009C6B8F  88 50 10                        mov byte ptr [rax + 0x10], dl
009C6B92  55                              push rbp
009C6B93  56                              push rsi
009C6B94  57                              push rdi
009C6B95  41 54                           push r12
009C6B97  41 55                           push r13
009C6B99  41 56                           push r14
009C6B9B  41 57                           push r15
009C6B9D  48 8D 68 A8                     lea rbp, [rax - 0x58]
009C6BA1  48 81 EC 20 01 00 00            sub rsp, 0x120
009C6BA8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009C6BB1  45 33 ED                        xor r13d, r13d
009C6BB4  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
009C6BB9  0F 57 C0                        xorps xmm0, xmm0
009C6BBC  44 89 6D D4                     mov dword ptr [rbp - 0x2c], r13d
009C6BC0  0F 57 C9                        xorps xmm1, xmm1
009C6BC3  44 89 6D EC                     mov dword ptr [rbp - 0x14], r13d
009C6BC7  48 8B F1                        mov rsi, rcx
009C6BCA  8A 80 32 02 00 00               mov al, byte ptr [rax + 0x232]
009C6BD0  41 8B FD                        mov edi, r13d
009C6BD3  88 44 24 60                     mov byte ptr [rsp + 0x60], al
009C6BD7  44 88 6C 24 50                  mov byte ptr [rsp + 0x50], r13b
009C6BDC  44 88 6C 24 51                  mov byte ptr [rsp + 0x51], r13b
009C6BE1  0F 11 45 80                     movups xmmword ptr [rbp - 0x80], xmm0
009C6BE5  0F 11 45 90                     movups xmmword ptr [rbp - 0x70], xmm0
009C6BE9  0F 11 4D 00                     movups xmmword ptr [rbp], xmm1
009C6BED  0F 11 4D 10                     movups xmmword ptr [rbp + 0x10], xmm1
009C6BF1  41 F6 C0 08                     test r8b, 8
009C6BF5  74 0E                           je 0x1409c6c05
009C6BF7  8B 81 C8 00 00 00               mov eax, dword ptr [rcx + 0xc8]
009C6BFD  A8 58                           test al, 0x58
009C6BFF  0F 85 A7 00 00 00               jne 0x1409c6cac
009C6C05  44 8B A5 98 00 00 00            mov r12d, dword ptr [rbp + 0x98]
009C6C0C  45 8B F5                        mov r14d, r13d
009C6C0F  45 85 E4                        test r12d, r12d
009C6C12  74 2F                           je 0x1409c6c43
009C6C14  48 8B 9D A0 00 00 00            mov rbx, qword ptr [rbp + 0xa0]
009C6C1B  48 8B 0B                        mov rcx, qword ptr [rbx]
009C6C1E  E8 19 7B 09 00                  call 0x140a5e73c
009C6C23  84 C0                           test al, al
009C6C25  0F 85 81 00 00 00               jne 0x1409c6cac
009C6C2B  48 8B 0B                        mov rcx, qword ptr [rbx]
009C6C2E  E8 51 81 09 00                  call 0x140a5ed84
009C6C33  84 C0                           test al, al
009C6C35  75 75                           jne 0x1409c6cac
009C6C37  41 FF C6                        inc r14d
009C6C3A  48 83 C3 10                     add rbx, 0x10
009C6C3E  45 3B F4                        cmp r14d, r12d
009C6C41  72 D8                           jb 0x1409c6c1b
009C6C43  BB 53 65 41 74                  mov ebx, 0x74416553
009C6C48  41 BF 00 01 00 00               mov r15d, 0x100
009C6C4E  44 8B C3                        mov r8d, ebx
009C6C51  41 8B CF                        mov ecx, r15d
009C6C54  BA 30 00 00 00                  mov edx, 0x30
009C6C59  E8 92 B4 1B 00                  call 0x140b820f0
009C6C5E  4C 8B F0                        mov r14, rax
009C6C61  48 85 C0                        test rax, rax
009C6C64  0F 84 81 00 00 00               je 0x1409c6ceb
009C6C6A  48 8D 48 08                     lea rcx, [rax + 8]
009C6C6E  44 89 28                        mov dword ptr [rax], r13d
009C6C71  48 89 49 08                     mov qword ptr [rcx + 8], rcx
009C6C75  48 89 09                        mov qword ptr [rcx], rcx
009C6C78  48 8D 48 20                     lea rcx, [rax + 0x20]
009C6C7C  48 89 49 08                     mov qword ptr [rcx + 8], rcx
009C6C80  48 89 09                        mov qword ptr [rcx], rcx
009C6C83  44 89 68 18                     mov dword ptr [rax + 0x18], r13d
009C6C87  44 39 2D 82 13 61 00            cmp dword ptr [rip + 0x611382], r13d
009C6C8E  74 23                           je 0x1409c6cb3
009C6C90  44 8B C3                        mov r8d, ebx
009C6C93  41 8D 57 20                     lea edx, [r15 + 0x20]
009C6C97  41 8B CF                        mov ecx, r15d
009C6C9A  E8 51 B4 1B 00                  call 0x140b820f0
009C6C9F  48 8B F8                        mov rdi, rax
009C6CA2  48 85 C0                        test rax, rax
009C6CA5  75 0C                           jne 0x1409c6cb3
009C6CA7  49 8B CE                        mov rcx, r14
009C6CAA  EB 38                           jmp 0x1409c6ce4
009C6CAC  B8 0D 00 00 C0                  mov eax, 0xc000000d
009C6CB1  EB 3D                           jmp 0x1409c6cf0
009C6CB3  BA 68 00 00 00                  mov edx, 0x68
009C6CB8  41 B8 53 65 54 6C               mov r8d, 0x6c546553
009C6CBE  8D 4A D8                        lea ecx, [rdx - 0x28]
009C6CC1  E8 2A B4 1B 00                  call 0x140b820f0
009C6CC6  4C 8B F8                        mov r15, rax
009C6CC9  48 85 C0                        test rax, rax
009C6CCC  75 3E                           jne 0x1409c6d0c
009C6CCE  33 D2                           xor edx, edx
009C6CD0  49 8B CE                        mov rcx, r14
009C6CD3  E8 98 BB 1B 00                  call 0x140b82870
009C6CD8  44 39 2D 31 13 61 00            cmp dword ptr [rip + 0x611331], r13d
009C6CDF  74 0A                           je 0x1409c6ceb
009C6CE1  48 8B CF                        mov rcx, rdi
009C6CE4  33 D2                           xor edx, edx
009C6CE6  E8 85 BB 1B 00                  call 0x140b82870
009C6CEB  B8 9A 00 00 C0                  mov eax, 0xc000009a
009C6CF0  48 8B 9C 24 60 01 00 00         mov rbx, qword ptr [rsp + 0x160]
009C6CF8  48 81 C4 20 01 00 00            add rsp, 0x120
009C6CFF  41 5F                           pop r15
009C6D01  41 5E                           pop r14
009C6D03  41 5D                           pop r13
009C6D05  41 5C                           pop r12
009C6D07  5F                              pop rdi
009C6D08  5E                              pop rsi
009C6D09  5D                              pop rbp
009C6D0A  C3                              ret
009C6D0B  CC                              int3
009C6D0C  8B 8E 84 00 00 00               mov ecx, dword ptr [rsi + 0x84]
009C6D12  8B 95 A8 00 00 00               mov edx, dword ptr [rbp + 0xa8]
009C6D18  03 D1                           add edx, ecx
009C6D1A  3B D1                           cmp edx, ecx
009C6D1C  0F 82 28 0B 00 00               jb 0x1409c784a
009C6D22  8D 42 04                        lea eax, [rdx + 4]
009C6D25  41 83 C8 FF                     or r8d, 0xffffffff
009C6D29  3B C2                           cmp eax, edx
009C6D2B  45 8B E8                        mov r13d, r8d
009C6D2E  B9 95 00 00 C0                  mov ecx, 0xc0000095
009C6D33  44 0F 43 E8                     cmovae r13d, eax
009C6D37  1B DB                           sbb ebx, ebx
009C6D39  23 D9                           and ebx, ecx
009C6D3B  44 89 6C 24 64                  mov dword ptr [rsp + 0x64], r13d
009C6D40  3B C2                           cmp eax, edx
009C6D42  0F 82 09 0B 00 00               jb 0x1409c7851
009C6D48  41 8D 85 C0 05 00 00            lea eax, [r13 + 0x5c0]
009C6D4F  BA C0 05 00 00                  mov edx, 0x5c0
009C6D54  3B C2                           cmp eax, edx
009C6D56  44 0F 43 C0                     cmovae r8d, eax
009C6D5A  1B DB                           sbb ebx, ebx
009C6D5C  23 D9                           and ebx, ecx
009C6D5E  3B C2                           cmp eax, edx
009C6D60  0F 82 EB 0A 00 00               jb 0x1409c7851
009C6D66  8B 86 88 00 00 00               mov eax, dword ptr [rsi + 0x88]
009C6D6C  33 C9                           xor ecx, ecx
009C6D6E  44 8A 4D 68                     mov r9b, byte ptr [rbp + 0x68]
009C6D72  0F 57 C0                        xorps xmm0, xmm0
009C6D75  48 8B 15 A4 12 61 00            mov rdx, qword ptr [rip + 0x6112a4]
009C6D7C  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
009C6D81  48 89 4D D8                     mov qword ptr [rbp - 0x28], rcx
009C6D85  89 4D E8                        mov dword ptr [rbp - 0x18], ecx
009C6D88  48 89 4D E0                     mov qword ptr [rbp - 0x20], rcx
009C6D8C  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
009C6D91  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
009C6D96  41 8A C9                        mov cl, r9b
009C6D99  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
009C6D9E  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009C6DA2  44 89 44 24 28                  mov dword ptr [rsp + 0x28], r8d
009C6DA7  45 33 C0                        xor r8d, r8d
009C6DAA  C7 45 D0 30 00 00 00            mov dword ptr [rbp - 0x30], 0x30
009C6DB1  F3 0F 7F 45 F0                  movdqu xmmword ptr [rbp - 0x10], xmm0
009C6DB6  E8 25 44 ED FF                  call 0x14089b1e0
009C6DBB  8B D8                           mov ebx, eax
009C6DBD  49 8B CF                        mov rcx, r15
009C6DC0  85 C0                           test eax, eax
009C6DC2  79 1D                           jns 0x1409c6de1
009C6DC4  33 D2                           xor edx, edx
009C6DC6  E8 A5 BA 1B 00                  call 0x140b82870
009C6DCB  33 D2                           xor edx, edx
009C6DCD  49 8B CE                        mov rcx, r14
009C6DD0  E8 9B BA 1B 00                  call 0x140b82870
009C6DD5  83 3D 34 12 61 00 00            cmp dword ptr [rip + 0x611234], 0
009C6DDC  E9 8E 0A 00 00                  jmp 0x1409c786f
009C6DE1  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
009C6DE6  4C 89 7B 30                     mov qword ptr [rbx + 0x30], r15
009C6DEA  E8 B1 8B A5 FF                  call 0x14041f9a0
009C6DEF  48 8B 0D 12 BF 64 FF            mov rcx, qword ptr [rip - 0x9b40ee]
009C6DF6  48 8B C1                        mov rax, rcx
009C6DF9  F0 48 0F C1 05 EE 7D 44 00      lock xadd qword ptr [rip + 0x447dee], rax
009C6E02  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
009C6E07  48 03 C1                        add rax, rcx
009C6E0A  48 8B 0D F7 BE 64 FF            mov rcx, qword ptr [rip - 0x9b4109]
009C6E11  89 43 38                        mov dword ptr [rbx + 0x38], eax
009C6E14  48 C1 E8 20                     shr rax, 0x20
009C6E18  89 43 3C                        mov dword ptr [rbx + 0x3c], eax
009C6E1B  48 8B C1                        mov rax, rcx
009C6E1E  F0 48 0F C1 05 C9 7D 44 00      lock xadd qword ptr [rip + 0x447dc9], rax
009C6E27  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
009C6E2C  48 03 C1                        add rax, rcx
009C6E2F  89 42 10                        mov dword ptr [rdx + 0x10], eax
009C6E32  45 33 FF                        xor r15d, r15d
009C6E35  48 C1 E8 20                     shr rax, 0x20
009C6E39  89 42 14                        mov dword ptr [rdx + 0x14], eax
009C6E3C  44 88 BB CC 00 00 00            mov byte ptr [rbx + 0xcc], r15b
009C6E43  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
009C6E47  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
009C6E4B  0F 10 06                        movups xmm0, xmmword ptr [rsi]
009C6E4E  F3 0F 7F 03                     movdqu xmmword ptr [rbx], xmm0
009C6E52  44 89 BB 8C 00 00 00            mov dword ptr [rbx + 0x8c], r15d
009C6E59  44 89 BB 80 00 00 00            mov dword ptr [rbx + 0x80], r15d
009C6E60  44 89 AB 84 00 00 00            mov dword ptr [rbx + 0x84], r13d
009C6E67  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
009C6E6B  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
009C6E6F  8B 86 C0 00 00 00               mov eax, dword ptr [rsi + 0xc0]
009C6E75  89 83 C0 00 00 00               mov dword ptr [rbx + 0xc0], eax
009C6E7B  8B 86 C4 00 00 00               mov eax, dword ptr [rsi + 0xc4]
009C6E81  89 83 C4 00 00 00               mov dword ptr [rbx + 0xc4], eax
009C6E87  48 8B 46 28                     mov rax, qword ptr [rsi + 0x28]
009C6E8B  48 89 43 28                     mov qword ptr [rbx + 0x28], rax
009C6E8F  48 8B 86 E0 00 00 00            mov rax, qword ptr [rsi + 0xe0]
009C6E96  48 89 83 E0 00 00 00            mov qword ptr [rbx + 0xe0], rax
009C6E9D  4C 89 BB 60 04 00 00            mov qword ptr [rbx + 0x460], r15
009C6EA4  4C 89 BB 68 04 00 00            mov qword ptr [rbx + 0x468], r15
009C6EAB  4C 89 BB 48 04 00 00            mov qword ptr [rbx + 0x448], r15
009C6EB2  48 89 BB 78 04 00 00            mov qword ptr [rbx + 0x478], rdi
009C6EB9  44 89 7B 78                     mov dword ptr [rbx + 0x78], r15d
009C6EBD  4C 89 BB 88 04 00 00            mov qword ptr [rbx + 0x488], r15
009C6EC4  44 39 3D 45 11 61 00            cmp dword ptr [rip + 0x611145], r15d
009C6ECB  74 39                           je 0x1409c6f06
009C6ECD  48 8D 4F 28                     lea rcx, [rdi + 0x28]
009C6ED1  45 33 C0                        xor r8d, r8d
009C6ED4  41 8D 7F 1E                     lea edi, [r15 + 0x1e]
009C6ED8  8B D7                           mov edx, edi
009C6EDA  E8 01 17 93 FF                  call 0x1402f85e0
009C6EDF  44 0F 20 C1                     mov rcx, cr8
009C6EE3  80 F9 02                        cmp cl, 2
009C6EE6  73 1E                           jae 0x1409c6f06
009C6EE8  2B F8                           sub edi, eax
009C6EEA  8B C8                           mov ecx, eax
009C6EEC  48 8B 83 78 04 00 00            mov rax, qword ptr [rbx + 0x478]
009C6EF3  45 8D 47 01                     lea r8d, [r15 + 1]
009C6EF7  48 83 C0 28                     add rax, 0x28
009C6EFB  8B D7                           mov edx, edi
009C6EFD  48 8D 0C C8                     lea rcx, [rax + rcx*8]
009C6F01  E8 DA 16 93 FF                  call 0x1402f85e0
009C6F06  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009C6F0F  B2 01                           mov dl, 1
009C6F11  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
009C6F18  90                              nop
009C6F19  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
009C6F1D  E8 9E AC 84 FF                  call 0x140211bc0
009C6F22  8B 86 88 00 00 00               mov eax, dword ptr [rsi + 0x88]
009C6F28  45 33 C9                        xor r9d, r9d
009C6F2B  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009C6F30  45 33 C0                        xor r8d, r8d
009C6F33  48 8B CF                        mov rcx, rdi
009C6F36  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
009C6F3B  89 87 88 00 00 00               mov dword ptr [rdi + 0x88], eax
009C6F41  8B 86 90 00 00 00               mov eax, dword ptr [rsi + 0x90]
009C6F47  89 87 90 00 00 00               mov dword ptr [rdi + 0x90], eax
009C6F4D  8B 56 78                        mov edx, dword ptr [rsi + 0x78]
009C6F50  E8 8F 6B 04 00                  call 0x140a0dae4
009C6F55  8B 46 78                        mov eax, dword ptr [rsi + 0x78]
009C6F58  89 43 78                        mov dword ptr [rbx + 0x78], eax
009C6F5B  E8 08 9A B2 FF                  call 0x1404f0968
009C6F60  8B 8E C8 00 00 00               mov ecx, dword ptr [rsi + 0xc8]
009C6F66  85 C0                           test eax, eax
009C6F68  74 08                           je 0x1409c6f72
009C6F6A  81 E1 D7 FB FF EF               and ecx, 0xeffffbd7
009C6F70  EB 06                           jmp 0x1409c6f78
009C6F72  81 E1 D7 FB FF FF               and ecx, 0xfffffbd7
009C6F78  89 8F C8 00 00 00               mov dword ptr [rdi + 0xc8], ecx
009C6F7E  0F BA E1 18                     bt ecx, 0x18
009C6F82  73 0C                           jae 0x1409c6f90
009C6F84  F0 FF 05 4D 2B 61 00            lock inc dword ptr [rip + 0x612b4d]
009C6F8B  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009C6F90  0F 10 46 58                     movups xmm0, xmmword ptr [rsi + 0x58]
009C6F94  0F 11 47 58                     movups xmmword ptr [rdi + 0x58], xmm0
009C6F98  0F 10 4E 68                     movups xmm1, xmmword ptr [rsi + 0x68]
009C6F9C  0F 11 4F 68                     movups xmmword ptr [rdi + 0x68], xmm1
009C6FA0  8B 86 D0 00 00 00               mov eax, dword ptr [rsi + 0xd0]
009C6FA6  89 87 D0 00 00 00               mov dword ptr [rdi + 0xd0], eax
009C6FAC  8B 86 D4 00 00 00               mov eax, dword ptr [rsi + 0xd4]
009C6FB2  89 87 D4 00 00 00               mov dword ptr [rdi + 0xd4], eax
009C6FB8  0F 10 46 40                     movups xmm0, xmmword ptr [rsi + 0x40]
009C6FBC  0F 11 47 40                     movups xmmword ptr [rdi + 0x40], xmm0
009C6FC0  F2 0F 10 4E 50                  movsd xmm1, qword ptr [rsi + 0x50]
009C6FC5  F2 0F 11 4F 50                  movsd qword ptr [rdi + 0x50], xmm1
009C6FCA  E8 89 BD B2 FF                  call 0x1404f2d58
009C6FCF  85 C0                           test eax, eax
009C6FD1  74 0E                           je 0x1409c6fe1
009C6FD3  48 8B 86 90 04 00 00            mov rax, qword ptr [rsi + 0x490]
009C6FDA  48 89 87 90 04 00 00            mov qword ptr [rdi + 0x490], rax
009C6FE1  E8 E6 F6 C3 FF                  call 0x1406066cc
009C6FE6  85 C0                           test eax, eax
009C6FE8  74 19                           je 0x1409c7003
009C6FEA  8B 87 90 04 00 00               mov eax, dword ptr [rdi + 0x490]
009C6FF0  8B D0                           mov edx, eax
009C6FF2  33 96 90 04 00 00               xor edx, dword ptr [rsi + 0x490]
009C6FF8  83 E2 02                        and edx, 2
009C6FFB  33 D0                           xor edx, eax
009C6FFD  89 97 90 04 00 00               mov dword ptr [rdi + 0x490], edx
009C7003  4C 89 B7 08 03 00 00            mov qword ptr [rdi + 0x308], r14
009C700A  80 7F 77 02                     cmp byte ptr [rdi + 0x77], 2
009C700E  75 0B                           jne 0x1409c701b
009C7010  B2 01                           mov dl, 1
009C7012  48 8D 4F 58                     lea rcx, [rdi + 0x58]
009C7016  E8 C5 61 DD FF                  call 0x14079d1e0
009C701B  4C 89 BF 38 04 00 00            mov qword ptr [rdi + 0x438], r15
009C7022  48 8D 8F 28 03 00 00            lea rcx, [rdi + 0x328]
009C7029  4C 89 BF 40 04 00 00            mov qword ptr [rdi + 0x440], r15
009C7030  33 D2                           xor edx, edx
009C7032  4C 89 BF 80 04 00 00            mov qword ptr [rdi + 0x480], r15
009C7039  41 B8 10 01 00 00               mov r8d, 0x110
009C703F  4C 89 BF 18 03 00 00            mov qword ptr [rdi + 0x318], r15
009C7046  4C 89 BF 10 03 00 00            mov qword ptr [rdi + 0x310], r15
009C704D  44 89 BF 20 03 00 00            mov dword ptr [rdi + 0x320], r15d
009C7054  E8 E7 FB CF FF                  call 0x1406c6c40
009C7059  4C 89 BF B0 00 00 00            mov qword ptr [rdi + 0xb0], r15
009C7060  48 8B D6                        mov rdx, rsi
009C7063  4C 89 BF 50 04 00 00            mov qword ptr [rdi + 0x450], r15
009C706A  48 8B CF                        mov rcx, rdi
009C706D  4C 89 BF 58 04 00 00            mov qword ptr [rdi + 0x458], r15
009C7074  4C 89 BF 70 04 00 00            mov qword ptr [rdi + 0x470], r15
009C707B  E8 30 F3 A7 FF                  call 0x1404463b0
009C7080  8B D8                           mov ebx, eax
009C7082  85 C0                           test eax, eax
009C7084  79 1B                           jns 0x1409c70a1
009C7086  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
009C708A  E8 81 89 89 FF                  call 0x14025fa10
009C708F  E8 1C 68 89 FF                  call 0x14025d8b0
009C7094  48 8B CF                        mov rcx, rdi
009C7097  E8 B4 22 93 FF                  call 0x1402f9350
009C709C  E9 DA 07 00 00                  jmp 0x1409c787b
009C70A1  E8 C2 98 B2 FF                  call 0x1404f0968
009C70A6  85 C0                           test eax, eax
009C70A8  74 36                           je 0x1409c70e0
009C70AA  41 BE 00 00 00 10               mov r14d, 0x10000000
009C70B0  44 85 B6 C8 00 00 00            test dword ptr [rsi + 0xc8], r14d
009C70B7  74 27                           je 0x1409c70e0
009C70B9  48 8B 8F D8 00 00 00            mov rcx, qword ptr [rdi + 0xd8]
009C70C0  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
009C70C5  48 83 C1 10                     add rcx, 0x10
009C70C9  4C 89 7C 24 78                  mov qword ptr [rsp + 0x78], r15
009C70CE  E8 79 46 07 00                  call 0x140a3b74c
009C70D3  8B D8                           mov ebx, eax
009C70D5  85 C0                           test eax, eax
009C70D7  78 AD                           js 0x1409c7086
009C70D9  44 09 B7 C8 00 00 00            or dword ptr [rdi + 0xc8], r14d
009C70E0  33 D2                           xor edx, edx
009C70E2  48 8B CE                        mov rcx, rsi
009C70E5  E8 EE 7E 03 00                  call 0x1409fefd8
009C70EA  48 8B 96 70 04 00 00            mov rdx, qword ptr [rsi + 0x470]
009C70F1  48 89 97 70 04 00 00            mov qword ptr [rdi + 0x470], rdx
009C70F8  48 8B 8E 08 03 00 00            mov rcx, qword ptr [rsi + 0x308]
009C70FF  44 39 39                        cmp dword ptr [rcx], r15d
009C7102  74 19                           je 0x1409c711d
009C7104  48 8B 97 08 03 00 00            mov rdx, qword ptr [rdi + 0x308]
009C710B  45 33 C0                        xor r8d, r8d
009C710E  E8 AD B2 93 FF                  call 0x1403023c0
009C7113  8B D8                           mov ebx, eax
009C7115  85 C0                           test eax, eax
009C7117  0F 88 69 FF FF FF               js 0x1409c7086
009C711D  4C 39 BE 48 04 00 00            cmp qword ptr [rsi + 0x448], r15
009C7124  74 15                           je 0x1409c713b
009C7126  48 8B D7                        mov rdx, rdi
009C7129  48 8B CE                        mov rcx, rsi
009C712C  E8 97 F1 0A 00                  call 0x140a762c8
009C7131  8B D8                           mov ebx, eax
009C7133  85 C0                           test eax, eax
009C7135  0F 88 4B FF FF FF               js 0x1409c7086
009C713B  44 39 3D CE 0E 61 00            cmp dword ptr [rip + 0x610ece], r15d
009C7142  0F 84 B7 00 00 00               je 0x1409c71ff
009C7148  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
009C7151  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
009C7156  48 8B 88 78 04 00 00            mov rcx, qword ptr [rax + 0x478]
009C715D  48 8B 82 08 05 00 00            mov rax, qword ptr [rdx + 0x508]
009C7164  48 89 01                        mov qword ptr [rcx], rax
009C7167  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009C7170  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
009C7175  48 8B 80 10 05 00 00            mov rax, qword ptr [rax + 0x510]
009C717C  48 8B 8A 78 04 00 00            mov rcx, qword ptr [rdx + 0x478]
009C7183  48 89 41 08                     mov qword ptr [rcx + 8], rax
009C7187  48 8B 82 78 04 00 00            mov rax, qword ptr [rdx + 0x478]
009C718E  C7 40 20 0F 00 00 00            mov dword ptr [rax + 0x20], 0xf
009C7195  48 8B 82 78 04 00 00            mov rax, qword ptr [rdx + 0x478]
009C719C  44 89 B8 18 01 00 00            mov dword ptr [rax + 0x118], r15d
009C71A3  48 8B 82 78 04 00 00            mov rax, qword ptr [rdx + 0x478]
009C71AA  44 89 B8 1C 01 00 00            mov dword ptr [rax + 0x11c], r15d
009C71B1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009C71BA  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009C71BF  48 8B 90 B8 00 00 00            mov rdx, qword ptr [rax + 0xb8]
009C71C6  48 8B 8F 78 04 00 00            mov rcx, qword ptr [rdi + 0x478]
009C71CD  F2 0F 10 82 38 03 00 00         movsd xmm0, qword ptr [rdx + 0x338]
009C71D5  F2 0F 11 41 10                  movsd qword ptr [rcx + 0x10], xmm0
009C71DA  8B 82 40 03 00 00               mov eax, dword ptr [rdx + 0x340]
009C71E0  89 41 18                        mov dword ptr [rcx + 0x18], eax
009C71E3  0F B7 82 44 03 00 00            movzx eax, word ptr [rdx + 0x344]
009C71EA  66 89 41 1C                     mov word ptr [rcx + 0x1c], ax
009C71EE  8A 82 46 03 00 00               mov al, byte ptr [rdx + 0x346]
009C71F4  88 41 1E                        mov byte ptr [rcx + 0x1e], al
009C71F7  48 8B CF                        mov rcx, rdi
009C71FA  E8 E1 A2 DD FF                  call 0x1407a14e0
009C71FF  F6 45 70 02                     test byte ptr [rbp + 0x70], 2
009C7203  74 49                           je 0x1409c724e
009C7205  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009C720E  BA 44 66 6C 74                  mov edx, 0x746c6644
009C7213  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
009C721A  E8 61 8D 84 FF                  call 0x14020ff80
009C721F  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
009C7224  48 8B C8                        mov rcx, rax
009C7227  48 8B D8                        mov rbx, rax
009C722A  E8 89 23 C4 FF                  call 0x1406095b8
009C722F  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009C7234  85 C0                           test eax, eax
009C7236  78 0E                           js 0x1409c7246
009C7238  44 38 7C 24 50                  cmp byte ptr [rsp + 0x50], r15b
009C723D  74 07                           je 0x1409c7246
009C723F  83 8F C8 00 00 00 40            or dword ptr [rdi + 0xc8], 0x40
009C7246  48 8B CB                        mov rcx, rbx
009C7249  E8 02 21 93 FF                  call 0x1402f9350
009C724E  4C 8D B7 C0 05 00 00            lea r14, [rdi + 0x5c0]
009C7255  41 8B C6                        mov eax, r14d
009C7258  83 E0 07                        and eax, 7
009C725B  74 14                           je 0x1409c7271
009C725D  B9 08 00 00 00                  mov ecx, 8
009C7262  2B C8                           sub ecx, eax
009C7264  8B C1                           mov eax, ecx
009C7266  4C 03 F0                        add r14, rax
009C7269  44 2B E9                        sub r13d, ecx
009C726C  44 89 6C 24 64                  mov dword ptr [rsp + 0x64], r13d
009C7271  8B 86 80 00 00 00               mov eax, dword ptr [rsi + 0x80]
009C7277  45 8B FC                        mov r15d, r12d
009C727A  41 3B C4                        cmp eax, r12d
009C727D  44 0F 47 F8                     cmova r15d, eax
009C7281  45 33 ED                        xor r13d, r13d
009C7284  44 03 7E 7C                     add r15d, dword ptr [rsi + 0x7c]
009C7288  49 C1 E7 04                     shl r15, 4
009C728C  4D 03 FE                        add r15, r14
009C728F  4C 89 B7 98 00 00 00            mov qword ptr [rdi + 0x98], r14
009C7296  44 38 2D 53 09 4A 00            cmp byte ptr [rip + 0x4a0953], r13b
009C729D  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
009C72A2  74 1D                           je 0x1409c72c1
009C72A4  48 8B D7                        mov rdx, rdi
009C72A7  48 8B CE                        mov rcx, rsi
009C72AA  E8 25 6D 03 00                  call 0x1409fdfd4
009C72AF  8B D8                           mov ebx, eax
009C72B1  85 C0                           test eax, eax
009C72B3  79 49                           jns 0x1409c72fe
009C72B5  4C 89 AF 98 00 00 00            mov qword ptr [rdi + 0x98], r13
009C72BC  E9 C5 FD FF FF                  jmp 0x1409c7086
009C72C1  8B 46 7C                        mov eax, dword ptr [rsi + 0x7c]
009C72C4  4D 8B CE                        mov r9, r14
009C72C7  44 8B 44 24 64                  mov r8d, dword ptr [rsp + 0x64]
009C72CC  89 47 7C                        mov dword ptr [rdi + 0x7c], eax
009C72CF  48 8D 44 24 64                  lea rax, [rsp + 0x64]
009C72D4  48 8B 96 98 00 00 00            mov rdx, qword ptr [rsi + 0x98]
009C72DB  8B 4E 7C                        mov ecx, dword ptr [rsi + 0x7c]
009C72DE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009C72E3  48 8D 44 24 70                  lea rax, [rsp + 0x70]
009C72E8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009C72ED  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
009C72F2  E8 E9 18 FE FF                  call 0x1409a8be0
009C72F7  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
009C72FC  8B D8                           mov ebx, eax
009C72FE  8B 46 7C                        mov eax, dword ptr [rsi + 0x7c]
009C7301  45 8B E5                        mov r12d, r13d
009C7304  C1 E0 04                        shl eax, 4
009C7307  4C 03 F0                        add r14, rax
009C730A  4C 89 B7 A0 00 00 00            mov qword ptr [rdi + 0xa0], r14
009C7311  44 39 AD 98 00 00 00            cmp dword ptr [rbp + 0x98], r13d
009C7318  0F 86 9B 00 00 00               jbe 0x1409c73b9
009C731E  4C 8B AD A0 00 00 00            mov r13, qword ptr [rbp + 0xa0]
009C7325  8B 96 80 00 00 00               mov edx, dword ptr [rsi + 0x80]
009C732B  85 D2                           test edx, edx
009C732D  74 14                           je 0x1409c7343
009C732F  4D 8B 4D 00                     mov r9, qword ptr [r13]
009C7333  48 8B 8E A0 00 00 00            mov rcx, qword ptr [rsi + 0xa0]
009C733A  E8 55 D7 00 00                  call 0x1409d4a94
009C733F  84 C0                           test al, al
009C7341  74 62                           je 0x1409c73a5
009C7343  44 8B 44 24 64                  mov r8d, dword ptr [rsp + 0x64]
009C7348  48 8D 44 24 64                  lea rax, [rsp + 0x64]
009C734D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009C7352  4D 8B CE                        mov r9, r14
009C7355  48 8D 44 24 70                  lea rax, [rsp + 0x70]
009C735A  41 8B D4                        mov edx, r12d
009C735D  48 C1 E2 04                     shl rdx, 4
009C7361  B9 01 00 00 00                  mov ecx, 1
009C7366  48 03 95 A0 00 00 00            add rdx, qword ptr [rbp + 0xa0]
009C736D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009C7372  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
009C7377  E8 64 18 FE FF                  call 0x1409a8be0
009C737C  8B 8F 80 00 00 00               mov ecx, dword ptr [rdi + 0x80]
009C7382  8B D8                           mov ebx, eax
009C7384  48 8B 87 A0 00 00 00            mov rax, qword ptr [rdi + 0xa0]
009C738B  48 03 C9                        add rcx, rcx
009C738E  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
009C7393  49 83 C6 10                     add r14, 0x10
009C7397  C7 44 C8 08 07 00 00 00         mov dword ptr [rax + rcx*8 + 8], 7
009C739F  FF 87 80 00 00 00               inc dword ptr [rdi + 0x80]
009C73A5  41 FF C4                        inc r12d
009C73A8  49 83 C5 10                     add r13, 0x10
009C73AC  44 3B A5 98 00 00 00            cmp r12d, dword ptr [rbp + 0x98]
009C73B3  0F 82 6C FF FF FF               jb 0x1409c7325
009C73B9  48 8B 86 A8 00 00 00            mov rax, qword ptr [rsi + 0xa8]
009C73C0  45 33 E4                        xor r12d, r12d
009C73C3  0F B6 50 01                     movzx edx, byte ptr [rax + 1]
009C73C7  48 8B 86 B8 00 00 00            mov rax, qword ptr [rsi + 0xb8]
009C73CE  44 8D 34 95 08 00 00 00         lea r14d, [rdx*4 + 8]
009C73D6  48 85 C0                        test rax, rax
009C73D9  74 07                           je 0x1409c73e2
009C73DB  0F B7 40 02                     movzx eax, word ptr [rax + 2]
009C73DF  44 03 F0                        add r14d, eax
009C73E2  41 8B D6                        mov edx, r14d
009C73E5  B9 00 01 00 00                  mov ecx, 0x100
009C73EA  41 B8 53 65 54 64               mov r8d, 0x64546553
009C73F0  E8 FB AC 1B 00                  call 0x140b820f0
009C73F5  48 89 87 B0 00 00 00            mov qword ptr [rdi + 0xb0], rax
009C73FC  4C 8B F8                        mov r15, rax
009C73FF  48 85 C0                        test rax, rax
009C7402  75 0A                           jne 0x1409c740e
009C7404  BB 9A 00 00 C0                  mov ebx, 0xc000009a
009C7409  E9 78 FC FF FF                  jmp 0x1409c7086
009C740E  44 39 A6 80 00 00 00            cmp dword ptr [rsi + 0x80], r12d
009C7415  74 13                           je 0x1409c742a
009C7417  44 39 A7 80 00 00 00            cmp dword ptr [rdi + 0x80], r12d
009C741E  75 0A                           jne 0x1409c742a
009C7420  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009C7425  E9 5C FC FF FF                  jmp 0x1409c7086
009C742A  41 8A C4                        mov al, r12b
009C742D  44 39 A7 80 00 00 00            cmp dword ptr [rdi + 0x80], r12d
009C7434  76 0E                           jbe 0x1409c7444
009C7436  81 8F C8 00 00 00 10 08 00 00   or dword ptr [rdi + 0xc8], 0x810
009C7440  B0 01                           mov al, 1
009C7442  EB 07                           jmp 0x1409c744b
009C7444  4C 89 A7 A0 00 00 00            mov qword ptr [rdi + 0xa0], r12
009C744B  44 8B 6D 70                     mov r13d, dword ptr [rbp + 0x70]
009C744F  41 F6 C5 08                     test r13b, 8
009C7453  74 09                           je 0x1409c745e
009C7455  83 8F C8 00 00 00 18            or dword ptr [rdi + 0xc8], 0x18
009C745C  B0 01                           mov al, 1
009C745E  84 C0                           test al, al
009C7460  0F 84 BC 00 00 00               je 0x1409c7522
009C7466  33 C0                           xor eax, eax
009C7468  4C 89 64 24 68                  mov qword ptr [rsp + 0x68], r12
009C746D  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
009C7471  0F 57 C0                        xorps xmm0, xmm0
009C7474  89 45 C8                        mov dword ptr [rbp - 0x38], eax
009C7477  48 8B 86 D8 00 00 00            mov rax, qword ptr [rsi + 0xd8]
009C747E  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
009C7482  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
009C7486  4C 39 60 38                     cmp qword ptr [rax + 0x38], r12
009C748A  0F 85 92 00 00 00               jne 0x1409c7522
009C7490  8B 86 C8 00 00 00               mov eax, dword ptr [rsi + 0xc8]
009C7496  A8 18                           test al, 0x18
009C7498  0F 85 84 00 00 00               jne 0x1409c7522
009C749E  48 8D 44 24 68                  lea rax, [rsp + 0x68]
009C74A3  C7 45 A0 30 00 00 00            mov dword ptr [rbp - 0x60], 0x30
009C74AA  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009C74AF  48 8D 55 A0                     lea rdx, [rbp - 0x60]
009C74B3  44 88 64 24 30                  mov byte ptr [rsp + 0x30], r12b
009C74B8  41 B9 01 00 00 00               mov r9d, 1
009C74BE  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
009C74C3  45 33 C0                        xor r8d, r8d
009C74C6  48 8B CE                        mov rcx, rsi
009C74C9  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
009C74CE  4C 89 65 A8                     mov qword ptr [rbp - 0x58], r12
009C74D2  44 89 65 B8                     mov dword ptr [rbp - 0x48], r12d
009C74D6  4C 89 65 B0                     mov qword ptr [rbp - 0x50], r12
009C74DA  F3 0F 7F 45 C0                  movdqu xmmword ptr [rbp - 0x40], xmm0
009C74DF  E8 08 13 EF FF                  call 0x1408b87ec
009C74E4  85 C0                           test eax, eax
009C74E6  78 3A                           js 0x1409c7522
009C74E8  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
009C74ED  E8 6A 6E 0C 00                  call 0x140a8e35c
009C74F2  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
009C74F7  85 C0                           test eax, eax
009C74F9  79 07                           jns 0x1409c7502
009C74FB  E8 50 1E 93 FF                  call 0x1402f9350
009C7500  EB 20                           jmp 0x1409c7522
009C7502  48 8B 96 D8 00 00 00            mov rdx, qword ptr [rsi + 0xd8]
009C7509  33 C0                           xor eax, eax
009C750B  F0 48 0F B1 4A 38               lock cmpxchg qword ptr [rdx + 0x38], rcx
009C7511  74 0A                           je 0x1409c751d
009C7513  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
009C7518  E8 33 1E 93 FF                  call 0x1402f9350
009C751D  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009C7522  48 8B 96 B0 00 00 00            mov rdx, qword ptr [rsi + 0xb0]
009C7529  49 8B CF                        mov rcx, r15
009C752C  45 8B C6                        mov r8d, r14d
009C752F  E8 0C F3 CF FF                  call 0x1406c6840
009C7534  4C 39 A6 B8 00 00 00            cmp qword ptr [rsi + 0xb8], r12
009C753B  74 18                           je 0x1409c7555
009C753D  8B 86 B8 00 00 00               mov eax, dword ptr [rsi + 0xb8]
009C7543  2B 86 B0 00 00 00               sub eax, dword ptr [rsi + 0xb0]
009C7549  49 03 C7                        add rax, r15
009C754C  48 89 87 B8 00 00 00            mov qword ptr [rdi + 0xb8], rax
009C7553  EB 07                           jmp 0x1409c755c
009C7555  4C 89 A7 B8 00 00 00            mov qword ptr [rdi + 0xb8], r12
009C755C  44 8B A6 A8 00 00 00            mov r12d, dword ptr [rsi + 0xa8]
009C7563  44 2B A6 B0 00 00 00            sub r12d, dword ptr [rsi + 0xb0]
009C756A  44 8B 8E 20 03 00 00            mov r9d, dword ptr [rsi + 0x320]
009C7571  45 85 C9                        test r9d, r9d
009C7574  74 18                           je 0x1409c758e
009C7576  4C 8B 86 18 03 00 00            mov r8, qword ptr [rsi + 0x318]
009C757D  48 8B CF                        mov rcx, rdi
009C7580  48 8B 96 10 03 00 00            mov rdx, qword ptr [rsi + 0x310]
009C7587  E8 68 25 00 00                  call 0x1409c9af4
009C758C  8B D8                           mov ebx, eax
009C758E  85 DB                           test ebx, ebx
009C7590  0F 88 F0 FA FF FF               js 0x1409c7086
009C7596  48 8B 96 10 03 00 00            mov rdx, qword ptr [rsi + 0x310]
009C759D  48 85 D2                        test rdx, rdx
009C75A0  74 13                           je 0x1409c75b5
009C75A2  48 8B CF                        mov rcx, rdi
009C75A5  E8 0E 97 05 00                  call 0x140a20cb8
009C75AA  85 C0                           test eax, eax
009C75AC  79 07                           jns 0x1409c75b5
009C75AE  8B D8                           mov ebx, eax
009C75B0  E9 D1 FA FF FF                  jmp 0x1409c7086
009C75B5  48 8B 8E 38 04 00 00            mov rcx, qword ptr [rsi + 0x438]
009C75BC  41 B9 0E 00 00 00               mov r9d, 0xe
009C75C2  45 8D 41 F3                     lea r8d, [r9 - 0xd]
009C75C6  48 85 C9                        test rcx, rcx
009C75C9  74 29                           je 0x1409c75f4
009C75CB  41 8B C0                        mov eax, r8d
009C75CE  F0 48 0F C1 41 18               lock xadd qword ptr [rcx + 0x18], rax
009C75D4  49 03 C0                        add rax, r8
009C75D7  49 3B C0                        cmp rax, r8
009C75DA  7F 05                           jg 0x1409c75e1
009C75DC  41 8B C9                        mov ecx, r9d
009C75DF  CD 29                           int 0x29
009C75E1  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009C75E6  48 8B 86 38 04 00 00            mov rax, qword ptr [rsi + 0x438]
009C75ED  48 89 87 38 04 00 00            mov qword ptr [rdi + 0x438], rax
009C75F4  48 8B 8E 40 04 00 00            mov rcx, qword ptr [rsi + 0x440]
009C75FB  48 85 C9                        test rcx, rcx
009C75FE  74 29                           je 0x1409c7629
009C7600  49 8B C0                        mov rax, r8
009C7603  F0 48 0F C1 41 18               lock xadd qword ptr [rcx + 0x18], rax
009C7609  49 03 C0                        add rax, r8
009C760C  49 3B C0                        cmp rax, r8
009C760F  7F 05                           jg 0x1409c7616
009C7611  49 8B C9                        mov rcx, r9
009C7614  CD 29                           int 0x29
009C7616  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009C761B  48 8B 86 40 04 00 00            mov rax, qword ptr [rsi + 0x440]
009C7622  48 89 87 40 04 00 00            mov qword ptr [rdi + 0x440], rax
009C7629  48 8B 96 80 04 00 00            mov rdx, qword ptr [rsi + 0x480]
009C7630  48 85 D2                        test rdx, rdx
009C7633  74 29                           je 0x1409c765e
009C7635  49 8B C0                        mov rax, r8
009C7638  F0 48 0F C1 42 18               lock xadd qword ptr [rdx + 0x18], rax
009C763E  49 03 C0                        add rax, r8
009C7641  49 3B C0                        cmp rax, r8
009C7644  7F 05                           jg 0x1409c764b
009C7646  49 8B C9                        mov rcx, r9
009C7649  CD 29                           int 0x29
009C764B  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009C7650  48 8B 86 80 04 00 00            mov rax, qword ptr [rsi + 0x480]
009C7657  48 89 87 80 04 00 00            mov qword ptr [rdi + 0x480], rax
009C765E  48 8B 96 50 04 00 00            mov rdx, qword ptr [rsi + 0x450]
009C7665  48 8B CF                        mov rcx, rdi
009C7668  E8 43 03 02 00                  call 0x1409e79b0
009C766D  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
009C7671  44 8B F0                        mov r14d, eax
009C7674  85 C0                           test eax, eax
009C7676  79 0D                           jns 0x1409c7685
009C7678  E8 93 83 89 FF                  call 0x14025fa10
009C767D  41 8B DE                        mov ebx, r14d
009C7680  E9 0A FA FF FF                  jmp 0x1409c708f
009C7685  E8 86 83 89 FF                  call 0x14025fa10
009C768A  E8 21 62 89 FF                  call 0x14025d8b0
009C768F  4C 8B 8D 80 00 00 00            mov r9, qword ptr [rbp + 0x80]
009C7696  41 8B D5                        mov edx, r13d
009C7699  44 8B 45 78                     mov r8d, dword ptr [rbp + 0x78]
009C769D  48 8B CF                        mov rcx, rdi
009C76A0  41 8B C4                        mov eax, r12d
009C76A3  49 03 C7                        add rax, r15
009C76A6  48 89 87 A8 00 00 00            mov qword ptr [rdi + 0xa8], rax
009C76AD  48 8B 85 90 00 00 00            mov rax, qword ptr [rbp + 0x90]
009C76B4  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009C76B9  8B 85 88 00 00 00               mov eax, dword ptr [rbp + 0x88]
009C76BF  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009C76C3  E8 EC D1 00 00                  call 0x1409d48b4
009C76C8  8B 57 7C                        mov edx, dword ptr [rdi + 0x7c]
009C76CB  4C 8D 87 E8 00 00 00            lea r8, [rdi + 0xe8]
009C76D2  48 8B 8F 98 00 00 00            mov rcx, qword ptr [rdi + 0x98]
009C76D9  E8 C2 F7 A4 FF                  call 0x140416ea0
009C76DE  8B 97 80 00 00 00               mov edx, dword ptr [rdi + 0x80]
009C76E4  4C 8D 87 F8 01 00 00            lea r8, [rdi + 0x1f8]
009C76EB  48 8B 8F A0 00 00 00            mov rcx, qword ptr [rdi + 0xa0]
009C76F2  E8 A9 F7 A4 FF                  call 0x140416ea0
009C76F7  48 8D 4D 80                     lea rcx, [rbp - 0x80]
009C76FB  E8 20 41 EA FF                  call 0x14086b820
009C7700  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
009C7704  48 8D 4D 80                     lea rcx, [rbp - 0x80]
009C7708  8A 5C 24 60                     mov bl, byte ptr [rsp + 0x60]
009C770C  8A D3                           mov dl, bl
009C770E  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
009C7712  E8 99 C3 EE FF                  call 0x1408b3ab0
009C7717  84 C0                           test al, al
009C7719  74 7A                           je 0x1409c7795
009C771B  8A D3                           mov dl, bl
009C771D  48 8D 4D 00                     lea rcx, [rbp]
009C7721  E8 8A C3 EE FF                  call 0x1408b3ab0
009C7726  84 C0                           test al, al
009C7728  74 6B                           je 0x1409c7795
009C772A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009C7733  B2 01                           mov dl, 1
009C7735  48 8B 5D 90                     mov rbx, qword ptr [rbp - 0x70]
009C7739  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
009C7740  90                              nop
009C7741  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
009C7745  E8 76 A4 84 FF                  call 0x140211bc0
009C774A  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009C774F  4C 8D 44 24 51                  lea r8, [rsp + 0x51]
009C7754  48 8B CF                        mov rcx, rdi
009C7757  48 8B D3                        mov rdx, rbx
009C775A  E8 39 93 05 00                  call 0x140a20a98
009C775F  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
009C7763  44 8B F0                        mov r14d, eax
009C7766  E8 A5 82 89 FF                  call 0x14025fa10
009C776B  E8 40 61 89 FF                  call 0x14025d8b0
009C7770  45 85 F6                        test r14d, r14d
009C7773  78 07                           js 0x1409c777c
009C7775  80 7C 24 51 00                  cmp byte ptr [rsp + 0x51], 0
009C777A  75 19                           jne 0x1409c7795
009C777C  48 8B CF                        mov rcx, rdi
009C777F  E8 CC 1B 93 FF                  call 0x1402f9350
009C7784  48 8D 4D 80                     lea rcx, [rbp - 0x80]
009C7788  E8 83 3F EA FF                  call 0x14086b710
009C778D  41 8B C6                        mov eax, r14d
009C7790  E9 5B F5 FF FF                  jmp 0x1409c6cf0
009C7795  48 8D 4D 80                     lea rcx, [rbp - 0x80]
009C7799  E8 72 3F EA FF                  call 0x14086b710
009C779E  48 8B 8F 18 03 00 00            mov rcx, qword ptr [rdi + 0x318]
009C77A5  48 85 C9                        test rcx, rcx
009C77A8  74 12                           je 0x1409c77bc
009C77AA  8B 97 20 03 00 00               mov edx, dword ptr [rdi + 0x320]
009C77B0  4C 8D 87 28 03 00 00            lea r8, [rdi + 0x328]
009C77B7  E8 E4 F6 A4 FF                  call 0x140416ea0
009C77BC  83 3D 4D 08 61 00 00            cmp dword ptr [rip + 0x61084d], 0
009C77C3  74 76                           je 0x1409c783b
009C77C5  83 3D D8 03 4A 00 0F            cmp dword ptr [rip + 0x4a03d8], 0xf
009C77CC  75 6D                           jne 0x1409c783b
009C77CE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009C77D7  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
009C77DE  48 8B 05 B3 03 4A 00            mov rax, qword ptr [rip + 0x4a03b3]
009C77E5  48 39 81 D0 01 00 00            cmp qword ptr [rcx + 0x1d0], rax
009C77EC  75 48                           jne 0x1409c7836
009C77EE  B9 01 00 00 00                  mov ecx, 1
009C77F3  F0 0F C1 0D AD 03 4A 00         lock xadd dword ptr [rip + 0x4a03ad], ecx
009C77FB  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009C7800  FF C1                           inc ecx
009C7802  48 8B 87 78 04 00 00            mov rax, qword ptr [rdi + 0x478]
009C7809  89 88 18 01 00 00               mov dword ptr [rax + 0x118], ecx
009C780F  48 8B 87 78 04 00 00            mov rax, qword ptr [rdi + 0x478]
009C7816  8B 90 18 01 00 00               mov edx, dword ptr [rax + 0x118]
009C781C  3B 15 7E 03 4A 00               cmp edx, dword ptr [rip + 0x4a037e]
009C7822  7C 17                           jl 0x1409c783b
009C7824  4C 8B C7                        mov r8, rdi
009C7827  48 8D 0D A2 E5 13 00            lea rcx, [rip + 0x13e5a2]
009C782E  E8 7D 14 99 FF                  call 0x140358cb0
009C7833  CC                              int3
009C7834  EB 05                           jmp 0x1409c783b
009C7836  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009C783B  48 8B 85 B0 00 00 00            mov rax, qword ptr [rbp + 0xb0]
009C7842  48 89 38                        mov qword ptr [rax], rdi
009C7845  E9 43 FF FF FF                  jmp 0x1409c778d
009C784A  BB 95 00 00 C0                  mov ebx, 0xc0000095
009C784F  EB 03                           jmp 0x1409c7854
009C7851  45 33 ED                        xor r13d, r13d
009C7854  33 D2                           xor edx, edx
009C7856  49 8B CF                        mov rcx, r15
009C7859  E8 12 B0 1B 00                  call 0x140b82870
009C785E  33 D2                           xor edx, edx
009C7860  49 8B CE                        mov rcx, r14
009C7863  E8 08 B0 1B 00                  call 0x140b82870
009C7868  44 39 2D A1 07 61 00            cmp dword ptr [rip + 0x6107a1], r13d
009C786F  74 0A                           je 0x1409c787b
009C7871  33 D2                           xor edx, edx
009C7873  48 8B CF                        mov rcx, rdi
009C7876  E8 F5 AF 1B 00                  call 0x140b82870
009C787B  8B C3                           mov eax, ebx
009C787D  E9 6E F4 FF FF                  jmp 0x1409c6cf0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepFilterToken(__int64 a1, unsigned __int8 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int8 v_stack_m107;
    unsigned __int8 v_stack_m108;
    unsigned __int8 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned int v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p51;
    unsigned __int64 v_stack_p58;
    unsigned __int8 v_stack_p60;
    unsigned int v_stack_p64;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int8 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (288);
    v_r13 = 0;
    v_stack_m100 = 0;
    *(unsigned int *)(v_rsp - 88 - 44) = 0;
    *(unsigned int *)(v_rsp - 88 - 20) = 0;
    v_stack_mF8 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m108 = 0;
    v_stack_m107 = 0;
    *(unsigned __int64 *)(v_rsp - 88 - 128) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 88 - 112) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 88) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 88 + 16) = v_xmm1;
    if ((((unsigned __int8)(a3)) & (8)) == 0) goto loc_009C6C05;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 200)))) & (88)) != 0) goto loc_009C6CAC;
loc_009C6C05:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 + 152))) == 0) goto loc_009C6C43;
loc_009C6C1B:
    result = RtlIsPackageSid(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 88 + 160)), a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_009C6CAC;
    result = RtlIsCapabilitySid(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 88 + 160)), a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_009C6CAC;
    v_r14 = (unsigned int)((0) + 1);
    v_rbx = (*(unsigned __int64 *)(v_rsp - 88 + 160)) + (16);
    if (((unsigned int)(v_r14)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 + 152))))) goto loc_009C6C1B;
loc_009C6C43:
    result = ExAllocatePool2(256, 48, (unsigned int)((unsigned int)((unsigned int)(0x74416553ULL))), a4);
    if (result == 0) goto loc_009C6CEB;
    *(unsigned int *)(result) = 0;
    *(unsigned __int64 *)(result + 8 + 8) = result + 8;
    *(unsigned __int64 *)(result + 8) = result + 8;
    *(unsigned __int64 *)(result + 32 + 8) = result + 32;
    *(unsigned __int64 *)(result + 32) = result + 32;
    *(unsigned int *)(result + 24) = 0;
    if ((*(unsigned int *)(v_rip + 6361986)) == 0) goto loc_009C6CB3;
    result = ExAllocatePool2(256, 256 + 32, (unsigned int)((unsigned int)((unsigned int)(0x74416553ULL))), a4);
    if (result != 0) goto loc_009C6CB3;
    goto loc_009C6CE4;
loc_009C6CAC:
    goto loc_009C6CF0;
loc_009C6CB3:
    result = ExAllocatePool2(104 - 40, 104, (unsigned int)(0x6C546553ULL), a4);
    if (result != 0) goto loc_009C6D0C;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x6C546553ULL), a4);
    if ((*(unsigned int *)(v_rip + 6361905)) == 0) goto loc_009C6CEB;
loc_009C6CE4:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x6C546553ULL), a4);
loc_009C6CEB:
loc_009C6CF0:
    v_rsp = (v_rsp) + (288);
    return (unsigned int)(0xC000009AULL);
loc_009C6D0C:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 88 + 168))) + ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 132)))));
    if (a2 < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 132))))) goto loc_009C784A;
    a3 = (unsigned int)(((unsigned int)(0x6C546553ULL)) | (0xFFFFFFFFULL));
    v_r13 = (unsigned int)(a3);
    if (((unsigned int)(a2 + 4)) >= a2) { v_r13 = (unsigned int)(a2 + 4); }
    v_rbx = (unsigned int)((v_stack_p8) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    v_stack_p64 = (unsigned int)(v_r13);
    if (((unsigned int)(a2 + 4)) < a2) goto loc_009C7851;
    if (((unsigned int)(v_r13 + 1472)) >= ((unsigned int)((unsigned int)(0x5C0ULL)))) { a3 = (unsigned int)(v_r13 + 1472); }
    v_rbx = (unsigned int)((v_rbx) & ((unsigned int)((unsigned int)(0xC0000095ULL))));
    if (((unsigned int)(v_r13 + 1472)) < ((unsigned int)((unsigned int)(0x5C0ULL)))) goto loc_009C7851;
    a1 = 0;
    v_stack_p48 = 0;
    *(unsigned __int64 *)(v_rsp - 88 - 40) = 0;
    *(unsigned int *)(v_rsp - 88 - 24) = 0;
    *(unsigned __int64 *)(v_rsp - 88 - 32) = 0;
    v_stack_p40 = v_stack_p58;
    v_stack_p38 = a3;
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 136)));
    v_stack_p28 = a3;
    a3 = 0;
    *(unsigned int *)(v_rsp - 88 - 48) = 48;
    *(unsigned __int64 *)(v_rsp - 88 - 16) = v_xmm0;
    result = ObCreateObjectEx((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 88 + 104)), *(unsigned __int64 *)(v_rip + 6361764), a3, *(unsigned __int8 *)(v_rsp - 88 + 104));
    if (!sign_flag) goto loc_009C6DE1;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, *(unsigned __int8 *)(v_rsp - 88 + 104));
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, *(unsigned __int8 *)(v_rsp - 88 + 104));
    goto loc_009C786F;
loc_009C6DE1:
    *(unsigned __int64 *)(v_stack_p58 + 48) = result;
    result = ExInitializeResourceLite(result, a2, a3, *(unsigned __int8 *)(v_rsp - 88 + 104));
    result = (*(unsigned __int64 *)(v_rip - 10174702)) + (*(unsigned __int64 *)(v_rip - 10174702));
    *(unsigned int *)(v_stack_p58 + 56) = (unsigned int)(result);
    result = (result) >> (32);
    *(unsigned int *)(v_stack_p58 + 60) = (unsigned int)(result);
    result = (*(unsigned __int64 *)(v_rip - 10174729)) + (*(unsigned __int64 *)(v_rip - 10174729));
    *(unsigned int *)(v_stack_p58 + 16) = (unsigned int)(result);
    v_r15 = 0;
    result = (result) >> (32);
    *(unsigned int *)(v_stack_p58 + 20) = (unsigned int)(result);
    *(unsigned __int8 *)(v_stack_p58 + 204) = 0;
    *(unsigned __int64 *)(v_stack_p58 + 24) = *(unsigned __int64 *)(a1 + 24);
    *(unsigned __int64 *)(v_stack_p58) = v_xmm0;
    *(unsigned int *)(v_stack_p58 + 140) = 0;
    *(unsigned int *)(v_stack_p58 + 128) = 0;
    *(unsigned int *)(v_stack_p58 + 132) = (unsigned int)(v_r13);
    *(unsigned __int64 *)(v_stack_p58 + 32) = *(unsigned __int64 *)(a1 + 16);
    *(unsigned int *)(v_stack_p58 + 192) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 192)));
    *(unsigned int *)(v_stack_p58 + 196) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 196)));
    *(unsigned __int64 *)(v_stack_p58 + 40) = *(unsigned __int64 *)(a1 + 40);
    *(unsigned __int64 *)(v_stack_p58 + 224) = *(unsigned __int64 *)(a1 + 224);
    *(unsigned __int64 *)(v_stack_p58 + 1120) = 0;
    *(unsigned __int64 *)(v_stack_p58 + 1128) = 0;
    *(unsigned __int64 *)(v_stack_p58 + 1096) = 0;
    *(unsigned __int64 *)(v_stack_p58 + 1144) = result;
    *(unsigned int *)(v_stack_p58 + 120) = 0;
    *(unsigned __int64 *)(v_stack_p58 + 1160) = 0;
    if ((*(unsigned int *)(v_rip + 6361413)) == 0) goto loc_009C6F06;
    a3 = 0;
    result = RtlWalkFrameChain(result + 40, (unsigned int)((unsigned int)(v_r15 + 30)), a3, *(unsigned __int8 *)(v_rsp - 88 + 104));
    v_rdi = v_r15 + 30;
    if (((unsigned __int8)(v_cr8)) < 2) {
        v_rdi = (unsigned int)((v_r15 + 30) - ((unsigned int)(result)));
        a1 = (unsigned int)(result);
        result = *(unsigned __int64 *)(v_stack_p58 + 1144);
        a3 = v_r15 + 1;
        result = (result) + (40);
        a2 = (unsigned int)(v_rdi);
        a1 = result + a1 * 8;
        result = RtlWalkFrameChain(a1, a2, a3, *(unsigned __int8 *)(v_rsp - 88 + 104));
    }
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(a1 + 48), 1, a3, *(unsigned __int8 *)(v_rsp - 88 + 104));
    a4 = 0;
    a3 = 0;
    v_stack_p20 = 0;
    *(unsigned int *)(v_stack_p58 + 136) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 136)));
    *(unsigned int *)(v_stack_p58 + 144) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 144)));
    result = SepSetTokenSessionById(v_stack_p58, (unsigned int)(*(unsigned int *)(a1 + 120)), a3, a4);
    *(unsigned int *)(v_stack_p58 + 120) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 120)));
    result = Feature_2045735225__private_IsEnabledDeviceUsageNoInline(v_stack_p58, (unsigned int)(*(unsigned int *)(a1 + 120)), a3, a4);
    if ((unsigned int)(result) == 0) goto loc_009C6F72;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 200))) & (0xEFFFFBD7ULL));
    goto loc_009C6F78;
loc_009C6F72:
    a1 = (unsigned int)((a1) & (0xFFFFFBD7ULL));
loc_009C6F78:
    *(unsigned int *)(v_stack_p58 + 200) = (unsigned int)(a1);
    v_rdi = v_stack_p58;
    if (!(condition_is_above_or_equal)) {
        v_rdi = v_stack_p58;
    }
    *(unsigned __int64 *)(v_rdi + 88) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 104) = v_xmm1;
    *(unsigned int *)(v_rdi + 208) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 208)));
    *(unsigned int *)(v_rdi + 212) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 212)));
    *(unsigned __int64 *)(v_rdi + 64) = v_xmm0;
    *(unsigned __int64 *)(v_rdi + 80) = v_xmm1;
    result = Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline(a1, (unsigned int)(*(unsigned int *)(a1 + 120)), a3, a4);
    if ((unsigned int)(result) != 0) {
        result = *(unsigned __int64 *)(a1 + 1168);
        *(unsigned __int64 *)(v_rdi + 1168) = result;
    }
    result = Feature_AgentId2__private_IsEnabledDeviceUsageNoInline(a1, (unsigned int)(*(unsigned int *)(a1 + 120)), a3, a4);
    if ((unsigned int)(result) != 0) {
        result = *(unsigned int *)(v_rdi + 1168);
        a2 = (unsigned int)(result);
        a2 = (unsigned int)((a2) ^ (*(unsigned int *)(a1 + 1168)));
        a2 = (unsigned int)((a2) & (2));
        a2 = (unsigned int)((a2) ^ ((unsigned int)(result)));
        *(unsigned int *)(v_rdi + 1168) = a2;
    }
    *(unsigned __int64 *)(v_rdi + 776) = result;
    if ((*(unsigned __int8 *)(v_rdi + 119)) == 2) {
        a2 = 1;
        a1 = v_rdi + 88;
        result = SepModifyTokenPolicyCounter(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(v_rdi + 1080) = 0;
    *(unsigned __int64 *)(v_rdi + 1088) = 0;
    a2 = 0;
    *(unsigned __int64 *)(v_rdi + 1152) = 0;
    *(unsigned __int64 *)(v_rdi + 792) = 0;
    *(unsigned __int64 *)(v_rdi + 784) = 0;
    *(unsigned int *)(v_rdi + 800) = 0;
    result = memset(v_rdi + 808, a2, 272, a4);
    *(unsigned __int64 *)(v_rdi + 176) = 0;
    *(unsigned __int64 *)(v_rdi + 1104) = 0;
    *(unsigned __int64 *)(v_rdi + 1112) = 0;
    *(unsigned __int64 *)(v_rdi + 1136) = 0;
    result = SepDuplicateLogonSessionReference(v_rdi, a1, 272, a4);
    if (!sign_flag) goto loc_009C70A1;
loc_009C7086:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(a1 + 48), a1, 272, a4);
loc_009C708F:
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(a1 + 48), a1, 272, a4);
    result = ObfDereferenceObject(v_rdi, a1, 272, a4);
    goto loc_009C787B;
loc_009C70A1:
    result = Feature_2045735225__private_IsEnabledDeviceUsageNoInline(v_rdi, a1, 272, a4);
    if ((unsigned int)(result) == 0) goto loc_009C70E0;
    if (((*(unsigned int *)(a1 + 200)) & ((unsigned int)((unsigned int)(0x10000000ULL)))) == 0) goto loc_009C70E0;
    a1 = (*(unsigned __int64 *)(v_rdi + 216)) + (16);
    v_stack_p78 = 0;
    result = SepReferenceLogonSession(a1, v_stack_p78, 272, a4);
    if (sign_flag) goto loc_009C7086;
loc_009C70E0:
    a2 = 0;
    result = SepRefDerefLuidToIndexEntryIfNecessary(a1, a2, 272, a4);
    *(unsigned __int64 *)(v_rdi + 1136) = *(unsigned __int64 *)(a1 + 1136);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 776))) == 0) goto loc_009C711D;
    a3 = 0;
    result = AuthzBasepDuplicateSecurityAttributes(*(unsigned __int64 *)(a1 + 776), *(unsigned __int64 *)(v_rdi + 776), a3, a4);
    if (sign_flag) goto loc_009C7086;
loc_009C711D:
    if ((*(unsigned __int64 *)(a1 + 1096)) == 0) goto loc_009C713B;
    result = SepDuplicateTokenClaims(a1, v_rdi, a3, a4);
    if (sign_flag) goto loc_009C7086;
loc_009C713B:
    if ((*(unsigned int *)(v_rip + 6360782)) != 0) {
        a2 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = v_stack_p58;
        a1 = *(unsigned __int64 *)(result + 1144);
        result = *(unsigned __int64 *)(a2 + 1288);
        *(unsigned __int64 *)(a1) = result;
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = v_stack_p58;
        result = *(unsigned __int64 *)(result + 1296);
        a1 = *(unsigned __int64 *)(a2 + 1144);
        *(unsigned __int64 *)(a1 + 8) = result;
        result = *(unsigned __int64 *)(a2 + 1144);
        *(unsigned int *)(result + 32) = 15;
        result = *(unsigned __int64 *)(a2 + 1144);
        *(unsigned int *)(result + 280) = 0;
        result = *(unsigned __int64 *)(a2 + 1144);
        *(unsigned int *)(result + 284) = 0;
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        v_rdi = v_stack_p58;
        a2 = *(unsigned __int64 *)(result + 184);
        a1 = *(unsigned __int64 *)(v_rdi + 1144);
        *(unsigned __int64 *)(a1 + 16) = v_xmm0;
        result = *(unsigned int *)(a2 + 832);
        *(unsigned int *)(a1 + 24) = (unsigned int)(result);
        result = *(unsigned __int16 *)(a2 + 836);
        *(unsigned __int16 *)(a1 + 28) = (unsigned __int16)(result);
        result = *(unsigned __int8 *)(a2 + 838);
        *(unsigned __int8 *)(a1 + 30) = (unsigned __int8)(result);
        a1 = v_rdi;
        result = SepAddTokenLogonSession(a1, a2, a3, a4);
    }
    if (((*(unsigned __int8 *)(v_rsp - 88 + 112)) & (2)) == 0) goto loc_009C724E;
    result = PsReferencePrimaryTokenWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), (unsigned int)(0x746C6644ULL), a3, a4);
    result = SeIsSystemContext(result, v_stack_p50, a3, a4);
    if (sign_flag) goto loc_009C7246;
    if (v_stack_p50 != 0) {
    }
    result = ObfDereferenceObject(result, v_stack_p50, a3, a4);
loc_009C724E:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p58 + 1472))) & (7));
    v_r14 = v_stack_p58 + 1472;
    if (!(condition_is_equal)) {
        a1 = 8;
        a1 = (unsigned int)((a1) - ((unsigned int)(result)));
        result = (unsigned int)(a1);
        v_r14 = (v_stack_p58 + 1472) + (result);
        v_r13 = (unsigned int)((v_r13) - ((unsigned int)(a1)));
        v_stack_p64 = (unsigned int)(v_r13);
    }
    v_r15 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 + 152))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 128)))) > ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 + 152))))) { v_r15 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 128))); }
    v_r13 = 0;
    v_r15 = (unsigned int)((v_r15) + (*(unsigned int *)(a1 + 124)));
    v_r15 = (v_r15) << (4);
    v_r15 = (v_r15) + (v_r14);
    *(unsigned __int64 *)(v_stack_p58 + 152) = v_r14;
    v_stack_p70 = v_r15;
    if ((*(unsigned __int8 *)(v_rip + 4852051)) == 0) goto loc_009C72C1;
    result = SepDuplicateTokenUserAndGroups(a1, v_stack_p58, a3, a4);
    if (!sign_flag) goto loc_009C72FE;
    *(unsigned __int64 *)(v_stack_p58 + 152) = 0;
    goto loc_009C7086;
loc_009C72C1:
    *(unsigned int *)(v_stack_p58 + 124) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124)));
    v_stack_p30 = v_stack_p64;
    v_stack_p28 = v_stack_p70;
    v_stack_p20 = v_r15;
    result = RtlCopySidAndAttributesArray((unsigned int)(*(unsigned int *)(a1 + 124)), *(unsigned __int64 *)(a1 + 152), (unsigned int)(v_stack_p64), v_r14);
loc_009C72FE:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 124))) << (4));
    v_r14 = (v_r14) + (result);
    *(unsigned __int64 *)(v_stack_p58 + 160) = v_r14;
    if ((*(unsigned int *)(v_rsp - 88 + 152)) <= 0) goto loc_009C73B9;
loc_009C7325:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 128))) == 0) goto loc_009C7343;
    result = SepSidInSidAndAttributes(*(unsigned __int64 *)(a1 + 160), (unsigned int)(*(unsigned int *)(a1 + 128)), (unsigned int)(v_stack_p64), *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 88 + 160)));
    v_rbx = (unsigned int)((unsigned int)(result));
    v_r15 = v_stack_p70;
    if ((unsigned __int8)(result) != 0) {
        a3 = v_stack_p64;
        result = v_stack_p64;
        v_stack_p30 = result;
        a4 = v_r14;
        result = v_stack_p70;
        a2 = 0;
        a2 = (a2) << (4);
        a1 = 1;
        a2 = (a2) + (*(unsigned __int64 *)(v_rsp - 88 + 160));
        v_stack_p28 = result;
        v_stack_p20 = v_stack_p70;
        result = RtlCopySidAndAttributesArray(a1, a2, a3, a4);
        a1 = *(unsigned int *)(v_stack_p58 + 128);
        v_rbx = (unsigned int)(result);
        result = *(unsigned __int64 *)(v_stack_p58 + 160);
        a1 = (a1) + (a1);
        v_r15 = v_stack_p70;
        v_r14 = (v_r14) + (16);
        *(unsigned int *)(result + a1 * 8 + 8) = 7;
    }
    v_r12 = (unsigned int)((0) + 1);
    v_r13 = (*(unsigned __int64 *)(v_rsp - 88 + 160)) + (16);
    if (((unsigned int)(v_r12)) < (*(unsigned int *)(v_rsp - 88 + 152))) goto loc_009C7325;
loc_009C73B9:
    v_r12 = 0;
    result = *(unsigned __int64 *)(a1 + 184);
    v_r14 = *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 168) + 1) * 4 + 8;
    if (*(unsigned __int64 *)(a1 + 184) != 0) {
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 184) + 2);
        v_r14 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 168) + 1) * 4 + 8) + ((unsigned int)(result)));
    }
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_r14)), (unsigned int)(0x64546553ULL), a4);
    *(unsigned __int64 *)(v_stack_p58 + 176) = result;
    if (result != 0) goto loc_009C740E;
    goto loc_009C7086;
loc_009C740E:
    if ((*(unsigned int *)(a1 + 128)) == 0) goto loc_009C742A;
    if ((*(unsigned int *)(v_stack_p58 + 128)) != 0) goto loc_009C742A;
    goto loc_009C7086;
loc_009C742A:
    if ((*(unsigned int *)(v_stack_p58 + 128)) <= 0) goto loc_009C7444;
    goto loc_009C744B;
loc_009C7444:
    *(unsigned __int64 *)(v_stack_p58 + 160) = 0;
loc_009C744B:
    result = 1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 88 + 112)))) & (8)) != 0) {
        result = 1;
    }
    if ((unsigned __int8)(result) == 0) goto loc_009C7522;
    result = 0;
    v_stack_p68 = 0;
    *(unsigned __int64 *)(v_rsp - 88 - 64) = 0;
    *(unsigned int *)(v_rsp - 88 - 56) = 0;
    *(unsigned __int64 *)(v_rsp - 88 - 96) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 88 - 80) = v_xmm0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 216) + 56)) != 0) goto loc_009C7522;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 200)))) & (24)) != 0) goto loc_009C7522;
    *(unsigned int *)(v_rsp - 88 - 96) = 48;
    v_stack_p38 = v_stack_p68;
    v_stack_p30 = 0;
    v_stack_p28 = 0;
    a3 = 0;
    v_stack_p20 = 0;
    *(unsigned __int64 *)(v_rsp - 88 - 88) = 0;
    *(unsigned int *)(v_rsp - 88 - 72) = 0;
    *(unsigned __int64 *)(v_rsp - 88 - 80) = 0;
    *(unsigned __int64 *)(v_rsp - 88 - 64) = v_xmm0;
    result = SepDuplicateToken(a1, v_rsp - 88 - 96, a3, 1);
    if (sign_flag) goto loc_009C7522;
    result = SepStopReferencingLogonSession(v_stack_p68, v_rsp - 88 - 96, a3, 1);
    if (!sign_flag) goto loc_009C7502;
    result = ObfDereferenceObject(v_stack_p68, v_rsp - 88 - 96, a3, 1);
    goto loc_009C7522;
loc_009C7502:
    result = 0;
    if (!(condition_is_equal)) {
        a1 = v_stack_p68;
        result = ObfDereferenceObject(a1, *(unsigned __int64 *)(a1 + 216), a3, 1);
    }
loc_009C7522:
    result = memcpy(result, *(unsigned __int64 *)(a1 + 176), (unsigned int)((unsigned int)(v_r14)), 1);
    if ((*(unsigned __int64 *)(a1 + 184)) == 0) goto loc_009C7555;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 184))) - (*(unsigned int *)(a1 + 176)));
    result = (result) + (result);
    *(unsigned __int64 *)(v_stack_p58 + 184) = result;
    goto loc_009C755C;
loc_009C7555:
    *(unsigned __int64 *)(v_stack_p58 + 184) = 0;
loc_009C755C:
    v_r12 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 168))) - (*(unsigned int *)(a1 + 176)));
    v_rbx = (unsigned int)(0xC000000DULL);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 800))) != 0) {
        a3 = *(unsigned __int64 *)(a1 + 792);
        a1 = v_stack_p58;
        a2 = *(unsigned __int64 *)(a1 + 784);
        result = SepSetTokenCapabilities(a1, a2, a3, (unsigned int)(*(unsigned int *)(a1 + 800)));
        v_rbx = (unsigned int)(result);
    }
    if (sign_flag) goto loc_009C7086;
    if (*(unsigned __int64 *)(a1 + 784) == 0) goto loc_009C75B5;
    result = SepSetTokenPackage(v_stack_p58, *(unsigned __int64 *)(a1 + 784), a3, (unsigned int)(*(unsigned int *)(a1 + 800)));
    if (!sign_flag) goto loc_009C75B5;
    goto loc_009C7086;
loc_009C75B5:
    if (*(unsigned __int64 *)(a1 + 1080) == 0) goto loc_009C75F4;
    result = ((unsigned int)((unsigned int)(14 - 13))) + (14 - 13);
    if (result <= (14 - 13)) {
        a1 = 14;
    }
    *(unsigned __int64 *)(v_stack_p58 + 1080) = *(unsigned __int64 *)(a1 + 1080);
loc_009C75F4:
    if (*(unsigned __int64 *)(a1 + 1088) == 0) goto loc_009C7629;
    result = (14 - 13) + (14 - 13);
    if (result <= (14 - 13)) {
        a1 = 14;
    }
    *(unsigned __int64 *)(v_stack_p58 + 1088) = *(unsigned __int64 *)(a1 + 1088);
loc_009C7629:
    if (*(unsigned __int64 *)(a1 + 1152) == 0) goto loc_009C765E;
    result = (14 - 13) + (14 - 13);
    if (result <= (14 - 13)) {
        a1 = 14;
    }
    *(unsigned __int64 *)(v_stack_p58 + 1152) = *(unsigned __int64 *)(a1 + 1152);
loc_009C765E:
    result = SepSetTokenTrust(v_stack_p58, *(unsigned __int64 *)(a1 + 1104), 14 - 13, 14);
    if (!sign_flag) goto loc_009C7685;
    result = ExReleaseResourceLite(*(unsigned __int64 *)(a1 + 48), *(unsigned __int64 *)(a1 + 1104), 14 - 13, 14);
    goto loc_009C708F;
loc_009C7685:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(a1 + 48), *(unsigned __int64 *)(a1 + 1104), 14 - 13, 14);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(a1 + 48), *(unsigned __int64 *)(a1 + 1104), 14 - 13, 14);
    result = ((unsigned int)((unsigned int)(v_r12))) + (result);
    *(unsigned __int64 *)(v_stack_p58 + 168) = result;
    v_stack_p28 = *(unsigned __int64 *)(v_rsp - 88 + 144);
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 + 136)));
    result = SepRemoveDisabledGroupsAndPrivileges(v_stack_p58, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 88 + 112)))), (unsigned int)(*(unsigned int *)(v_rsp - 88 + 120)), *(unsigned __int64 *)(v_rsp - 88 + 128));
    result = RtlSidHashInitialize(*(unsigned __int64 *)(v_stack_p58 + 152), (unsigned int)(*(unsigned int *)(v_stack_p58 + 124)), v_stack_p58 + 232, *(unsigned __int64 *)(v_rsp - 88 + 128));
    result = RtlSidHashInitialize(*(unsigned __int64 *)(v_stack_p58 + 160), (unsigned int)(*(unsigned int *)(v_stack_p58 + 128)), v_stack_p58 + 504, *(unsigned __int64 *)(v_rsp - 88 + 128));
    result = SeCaptureSubjectContext(v_rsp - 88 - 128, (unsigned int)(*(unsigned int *)(v_stack_p58 + 128)), v_stack_p58 + 504, *(unsigned __int64 *)(v_rsp - 88 + 128));
    *(unsigned __int64 *)(v_rsp - 88 + 16) = *(unsigned __int64 *)(v_rsp - 88 - 112);
    result = RtlIsSandboxedToken(v_rsp - 88 - 128, (unsigned __int8)(v_stack_p60), v_stack_p58 + 504, *(unsigned __int64 *)(v_rsp - 88 + 128));
    if ((unsigned __int8)(result) == 0) goto loc_009C7795;
    result = RtlIsSandboxedToken(v_rsp - 88, (unsigned __int8)(v_stack_p60), v_stack_p58 + 504, *(unsigned __int64 *)(v_rsp - 88 + 128));
    if ((unsigned __int8)(result) == 0) goto loc_009C7795;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 88 - 112) + 48), 1, v_stack_p58 + 504, *(unsigned __int64 *)(v_rsp - 88 + 128));
    result = SepNewTokenAsRestrictedAsProcessToken(v_stack_p58, *(unsigned __int64 *)(v_rsp - 88 - 112), v_stack_p51, *(unsigned __int64 *)(v_rsp - 88 + 128));
    result = ExReleaseResourceLite(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 88 - 112) + 48), *(unsigned __int64 *)(v_rsp - 88 - 112), v_stack_p51, *(unsigned __int64 *)(v_rsp - 88 + 128));
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 88 - 112) + 48), *(unsigned __int64 *)(v_rsp - 88 - 112), v_stack_p51, *(unsigned __int64 *)(v_rsp - 88 + 128));
    if (sign_flag) goto loc_009C777C;
    if (v_stack_p51 != 0) goto loc_009C7795;
loc_009C777C:
    result = ObfDereferenceObject(v_stack_p58, *(unsigned __int64 *)(v_rsp - 88 - 112), v_stack_p51, *(unsigned __int64 *)(v_rsp - 88 + 128));
    result = SeReleaseSubjectContext(v_rsp - 88 - 128, *(unsigned __int64 *)(v_rsp - 88 - 112), v_stack_p51, *(unsigned __int64 *)(v_rsp - 88 + 128));
loc_009C778D:
    goto loc_009C6CF0;
loc_009C7795:
    result = SeReleaseSubjectContext(v_rsp - 88 - 128, *(unsigned __int64 *)(v_rsp - 88 - 112), v_stack_p51, *(unsigned __int64 *)(v_rsp - 88 + 128));
    if (*(unsigned __int64 *)(v_stack_p58 + 792) != 0) {
        a2 = *(unsigned int *)(v_stack_p58 + 800);
        a3 = v_stack_p58 + 808;
        result = RtlSidHashInitialize(*(unsigned __int64 *)(v_stack_p58 + 792), a2, a3, *(unsigned __int64 *)(v_rsp - 88 + 128));
    }
    if ((*(unsigned int *)(v_rip + 6359117)) == 0) goto loc_009C783B;
    if ((*(unsigned int *)(v_rip + 4850648)) != 15) goto loc_009C783B;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 464)) != (*(unsigned __int64 *)(v_rip + 4850611))) goto loc_009C7836;
    a1 = (unsigned int)((1) + 1);
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p58 + 1144) + 280) = (unsigned int)(a1);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p58 + 1144) + 280)))) < (*(unsigned int *)(v_rip + 4850558))) goto loc_009C783B;
    result = DbgPrint(v_rip + 1303970, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p58 + 1144) + 280)), v_stack_p58, *(unsigned __int64 *)(v_rsp - 88 + 128));
    goto loc_009C783B;
loc_009C7836:
loc_009C783B:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 88 + 176)) = v_stack_p58;
    goto loc_009C778D;
loc_009C784A:
    goto loc_009C7854;
loc_009C7851:
    v_r13 = 0;
loc_009C7854:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, v_stack_p58, *(unsigned __int64 *)(v_rsp - 88 + 128));
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)((unsigned int)(result)), a2, v_stack_p58, *(unsigned __int64 *)(v_rsp - 88 + 128));
loc_009C786F:
    if ((*(unsigned int *)(v_rip + 6358945)) != 0) {
        a2 = 0;
        a1 = v_stack_p58;
        result = ExFreePoolWithTag(a1, a2, v_stack_p58, *(unsigned __int64 *)(v_rsp - 88 + 128));
    }
    goto loc_009C6CF0;
}
```

## 5. (Beta) C Style

```c
int64_t SepFilterToken(void *Arg1, uint8_t Arg2, int32_t Arg3, int32_t Arg4)
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
    uint64_t v_stack_m100;
    uint8_t v_stack_m107;
    uint8_t v_stack_m108;
    uint8_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint32_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p51;
    uint64_t v_stack_p58;
    uint8_t v_stack_p60;
    uint32_t v_stack_p64;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint8_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (288);
    local_r13 = 0;
    v_stack_m100 = 0;
    *(uint32_t *)(local_rsp - 0x58 - 0x2C) = 0;
    *(uint32_t *)(local_rsp - 0x58 - 0x14) = 0;
    v_stack_mF8 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m108 = 0;
    v_stack_m107 = 0;
    *(uint64_t *)(local_rsp - 0x58 - 0x80) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x58 - 0x70) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x58) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x58 + 0x10) = v_xmm1;
    if ((((uint8_t)(Arg3)) & (8)) == 0) goto loc_009C6C05;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC8)))) & (88)) != 0) goto loc_009C6CAC;
loc_009C6C05:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x98))) == 0) goto loc_009C6C43;
loc_009C6C1B:
    result = RtlIsPackageSid(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x58 + 0xA0)), Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_009C6CAC;
    result = RtlIsCapabilitySid(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x58 + 0xA0)), Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_009C6CAC;
    local_r14 = (uint32_t)((0) + 1);
    local_rbx = (*(uint64_t *)(local_rsp - 0x58 + 0xA0)) + (16);
    if (((uint32_t)(local_r14)) < ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x98))))) goto loc_009C6C1B;
loc_009C6C43:
    result = ExAllocatePool2(256, 48, (uint32_t)((uint32_t)((uint32_t)(0x74416553ULL))), Arg4);
    if (result == 0) goto loc_009C6CEB;
    *(uint32_t *)(result) = 0;
    *(uint64_t *)(result + 0x8 + 0x8) = result + 8;
    *(uint64_t *)(result + 0x8) = result + 8;
    *(uint64_t *)(result + 0x20 + 0x8) = result + 32;
    *(uint64_t *)(result + 0x20) = result + 32;
    *(uint32_t *)(result + 0x18) = 0;
    if ((*(uint32_t *)(v_rip + 0x611382)) == 0) goto loc_009C6CB3;
    result = ExAllocatePool2(256, 256 + 32, (uint32_t)((uint32_t)((uint32_t)(0x74416553ULL))), Arg4);
    if (result != 0) goto loc_009C6CB3;
    goto loc_009C6CE4;
loc_009C6CAC:
    goto loc_009C6CF0;
loc_009C6CB3:
    result = ExAllocatePool2(104 - 40, 104, (uint32_t)(0x6C546553ULL), Arg4);
    if (result != 0) goto loc_009C6D0C;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x6C546553ULL), Arg4);
    if ((*(uint32_t *)(v_rip + 0x611331)) == 0) goto loc_009C6CEB;
loc_009C6CE4:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x6C546553ULL), Arg4);
loc_009C6CEB:
loc_009C6CF0:
    local_rsp = (local_rsp) + (288);
    return (uint32_t)(0xC000009AULL);
loc_009C6D0C:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0xA8))) + ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x84)))));
    if (Arg2 < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x84))))) goto loc_009C784A;
    Arg3 = (uint32_t)(((uint32_t)(0x6C546553ULL)) | (0xFFFFFFFFULL));
    local_r13 = (uint32_t)(Arg3);
    if (((uint32_t)(Arg2 + 4)) >= Arg2) { local_r13 = (uint32_t)(Arg2 + 4); }
    local_rbx = (uint32_t)((v_stack_p8) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    v_stack_p64 = (uint32_t)(local_r13);
    if (((uint32_t)(Arg2 + 4)) < Arg2) goto loc_009C7851;
    if (((uint32_t)(local_r13 + 1472)) >= ((uint32_t)((uint32_t)(0x5C0ULL)))) { Arg3 = (uint32_t)(local_r13 + 1472); }
    local_rbx = (uint32_t)((local_rbx) & ((uint32_t)((uint32_t)(0xC0000095ULL))));
    if (((uint32_t)(local_r13 + 1472)) < ((uint32_t)((uint32_t)(0x5C0ULL)))) goto loc_009C7851;
    Arg1 = 0;
    v_stack_p48 = 0;
    *(uint64_t *)(local_rsp - 0x58 - 0x28) = 0;
    *(uint32_t *)(local_rsp - 0x58 - 0x18) = 0;
    *(uint64_t *)(local_rsp - 0x58 - 0x20) = 0;
    v_stack_p40 = v_stack_p58;
    v_stack_p38 = Arg3;
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x88)));
    v_stack_p28 = Arg3;
    Arg3 = 0;
    *(uint32_t *)(local_rsp - 0x58 - 0x30) = 48;
    *(uint64_t *)(local_rsp - 0x58 - 0x10) = v_xmm0;
    result = ObCreateObjectEx((uint8_t)(*(uint8_t *)(local_rsp - 0x58 + 0x68)), *(uint64_t *)(v_rip + 0x6112A4), Arg3, *(uint8_t *)(local_rsp - 0x58 + 0x68));
    if (!sign_flag) goto loc_009C6DE1;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, *(uint8_t *)(local_rsp - 0x58 + 0x68));
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, Arg3, *(uint8_t *)(local_rsp - 0x58 + 0x68));
    goto loc_009C786F;
loc_009C6DE1:
    *(uint64_t *)(v_stack_p58 + 0x30) = result;
    result = ExInitializeResourceLite(result, Arg2, Arg3, *(uint8_t *)(local_rsp - 0x58 + 0x68));
    result = (*(uint64_t *)(v_rip - 0x9B40EE)) + (*(uint64_t *)(v_rip - 0x9B40EE));
    *(uint32_t *)(v_stack_p58 + 0x38) = (uint32_t)(result);
    result = (result) >> (32);
    *(uint32_t *)(v_stack_p58 + 0x3C) = (uint32_t)(result);
    result = (*(uint64_t *)(v_rip - 0x9B4109)) + (*(uint64_t *)(v_rip - 0x9B4109));
    *(uint32_t *)(v_stack_p58 + 0x10) = (uint32_t)(result);
    local_r15 = 0;
    result = (result) >> (32);
    *(uint32_t *)(v_stack_p58 + 0x14) = (uint32_t)(result);
    *(uint8_t *)(v_stack_p58 + 0xCC) = 0;
    *(uint64_t *)(v_stack_p58 + 0x18) = *(uint64_t *)(arg1 + 0x18);
    *(uint64_t *)(v_stack_p58) = v_xmm0;
    *(uint32_t *)(v_stack_p58 + 0x8C) = 0;
    *(uint32_t *)(v_stack_p58 + 0x80) = 0;
    *(uint32_t *)(v_stack_p58 + 0x84) = (uint32_t)(local_r13);
    *(uint64_t *)(v_stack_p58 + 0x20) = *(uint64_t *)(arg1 + 0x10);
    *(uint32_t *)(v_stack_p58 + 0xC0) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC0)));
    *(uint32_t *)(v_stack_p58 + 0xC4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC4)));
    *(uint64_t *)(v_stack_p58 + 0x28) = *(uint64_t *)(arg1 + 0x28);
    *(uint64_t *)(v_stack_p58 + 0xE0) = *(uint64_t *)(arg1 + 0xE0);
    *(uint64_t *)(v_stack_p58 + 0x460) = 0;
    *(uint64_t *)(v_stack_p58 + 0x468) = 0;
    *(uint64_t *)(v_stack_p58 + 0x448) = 0;
    *(uint64_t *)(v_stack_p58 + 0x478) = result;
    *(uint32_t *)(v_stack_p58 + 0x78) = 0;
    *(uint64_t *)(v_stack_p58 + 0x488) = 0;
    if ((*(uint32_t *)(v_rip + 0x611145)) == 0) goto loc_009C6F06;
    Arg3 = 0;
    result = RtlWalkFrameChain(result + 40, (uint32_t)((uint32_t)(local_r15 + 30)), Arg3, *(uint8_t *)(local_rsp - 0x58 + 0x68));
    local_rdi = local_r15 + 30;
    if (((uint8_t)(v_cr8)) < 2) {
        local_rdi = (uint32_t)((local_r15 + 30) - ((uint32_t)(result)));
        Arg1 = (uint32_t)(result);
        result = *(uint64_t *)(v_stack_p58 + 0x478);
        Arg3 = local_r15 + 1;
        result = (result) + (40);
        Arg2 = (uint32_t)(local_rdi);
        Arg1 = result + Arg1 * 8;
        result = RtlWalkFrameChain(Arg1, Arg2, Arg3, *(uint8_t *)(local_rsp - 0x58 + 0x68));
    }
    result = ExAcquireResourceSharedLite(*(uint64_t *)(arg1 + 0x30), 1, Arg3, *(uint8_t *)(local_rsp - 0x58 + 0x68));
    Arg4 = 0;
    Arg3 = 0;
    v_stack_p20 = 0;
    *(uint32_t *)(v_stack_p58 + 0x88) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x88)));
    *(uint32_t *)(v_stack_p58 + 0x90) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x90)));
    result = SepSetTokenSessionById(v_stack_p58, (uint32_t)(*(uint32_t *)(arg1 + 0x78)), Arg3, Arg4);
    *(uint32_t *)(v_stack_p58 + 0x78) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x78)));
    result = Feature_2045735225__private_IsEnabledDeviceUsageNoInline(v_stack_p58, (uint32_t)(*(uint32_t *)(arg1 + 0x78)), Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_009C6F72;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xC8))) & (0xEFFFFBD7ULL));
    goto loc_009C6F78;
loc_009C6F72:
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFBD7ULL));
loc_009C6F78:
    *(uint32_t *)(v_stack_p58 + 0xC8) = (uint32_t)(Arg1);
    local_rdi = v_stack_p58;
    if (!(condition_is_above_or_equal)) {
        local_rdi = v_stack_p58;
    }
    *(uint64_t *)(local_rdi + 0x58) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x68) = v_xmm1;
    *(uint32_t *)(local_rdi + 0xD0) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xD0)));
    *(uint32_t *)(local_rdi + 0xD4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xD4)));
    *(uint64_t *)(local_rdi + 0x40) = v_xmm0;
    *(uint64_t *)(local_rdi + 0x50) = v_xmm1;
    result = Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline(Arg1, (uint32_t)(*(uint32_t *)(arg1 + 0x78)), Arg3, Arg4);
    if ((uint32_t)(result) != 0) {
        result = *(uint64_t *)(arg1 + 0x490);
        *(uint64_t *)(local_rdi + 0x490) = result;
    }
    result = Feature_AgentId2__private_IsEnabledDeviceUsageNoInline(Arg1, (uint32_t)(*(uint32_t *)(arg1 + 0x78)), Arg3, Arg4);
    if ((uint32_t)(result) != 0) {
        result = *(uint32_t *)(local_rdi + 0x490);
        Arg2 = (uint32_t)(result);
        Arg2 = (uint32_t)((Arg2) ^ (*(uint32_t *)(arg1 + 0x490)));
        Arg2 = (uint32_t)((Arg2) & (2));
        Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(result)));
        *(uint32_t *)(local_rdi + 0x490) = Arg2;
    }
    *(uint64_t *)(local_rdi + 0x308) = result;
    if ((*(uint8_t *)(local_rdi + 0x77)) == 2) {
        Arg2 = 1;
        Arg1 = local_rdi + 88;
        result = SepModifyTokenPolicyCounter(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint64_t *)(local_rdi + 0x438) = 0;
    *(uint64_t *)(local_rdi + 0x440) = 0;
    Arg2 = 0;
    *(uint64_t *)(local_rdi + 0x480) = 0;
    *(uint64_t *)(local_rdi + 0x318) = 0;
    *(uint64_t *)(local_rdi + 0x310) = 0;
    *(uint32_t *)(local_rdi + 0x320) = 0;
    result = memset(local_rdi + 808, Arg2, 272, Arg4);
    *(uint64_t *)(local_rdi + 0xB0) = 0;
    *(uint64_t *)(local_rdi + 0x450) = 0;
    *(uint64_t *)(local_rdi + 0x458) = 0;
    *(uint64_t *)(local_rdi + 0x470) = 0;
    result = SepDuplicateLogonSessionReference(local_rdi, Arg1, 272, Arg4);
    if (!sign_flag) goto loc_009C70A1;
loc_009C7086:
    result = ExReleaseResourceLite(*(uint64_t *)(arg1 + 0x30), Arg1, 272, Arg4);
loc_009C708F:
    result = KeLeaveCriticalRegion(*(uint64_t *)(arg1 + 0x30), Arg1, 272, Arg4);
    result = ObfDereferenceObject(local_rdi, Arg1, 272, Arg4);
    goto loc_009C787B;
loc_009C70A1:
    result = Feature_2045735225__private_IsEnabledDeviceUsageNoInline(local_rdi, Arg1, 272, Arg4);
    if ((uint32_t)(result) == 0) goto loc_009C70E0;
    if (((*(uint32_t *)(arg1 + 0xC8)) & ((uint32_t)((uint32_t)(0x10000000ULL)))) == 0) goto loc_009C70E0;
    Arg1 = (*(uint64_t *)(local_rdi + 0xD8)) + (16);
    v_stack_p78 = 0;
    result = SepReferenceLogonSession(Arg1, v_stack_p78, 272, Arg4);
    if (sign_flag) goto loc_009C7086;
loc_009C70E0:
    Arg2 = 0;
    result = SepRefDerefLuidToIndexEntryIfNecessary(Arg1, Arg2, 272, Arg4);
    *(uint64_t *)(local_rdi + 0x470) = *(uint64_t *)(arg1 + 0x470);
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x308))) == 0) goto loc_009C711D;
    Arg3 = 0;
    result = AuthzBasepDuplicateSecurityAttributes(*(uint64_t *)(arg1 + 0x308), *(uint64_t *)(local_rdi + 0x308), Arg3, Arg4);
    if (sign_flag) goto loc_009C7086;
loc_009C711D:
    if ((*(uint64_t *)(arg1 + 0x448)) == 0) goto loc_009C713B;
    result = SepDuplicateTokenClaims(Arg1, local_rdi, Arg3, Arg4);
    if (sign_flag) goto loc_009C7086;
loc_009C713B:
    if ((*(uint32_t *)(v_rip + 0x610ECE)) != 0) {
        Arg2 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = v_stack_p58;
        Arg1 = *(uint64_t *)(result + 0x478);
        result = *(uint64_t *)(Arg2 + 0x508);
        *(uint64_t *)(arg1) = result;
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg2 = v_stack_p58;
        result = *(uint64_t *)(result + 0x510);
        Arg1 = *(uint64_t *)(Arg2 + 0x478);
        *(uint64_t *)(arg1 + 0x8) = result;
        result = *(uint64_t *)(Arg2 + 0x478);
        *(uint32_t *)(result + 0x20) = 15;
        result = *(uint64_t *)(Arg2 + 0x478);
        *(uint32_t *)(result + 0x118) = 0;
        result = *(uint64_t *)(Arg2 + 0x478);
        *(uint32_t *)(result + 0x11C) = 0;
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        local_rdi = v_stack_p58;
        Arg2 = *(uint64_t *)(result + 0xB8);
        Arg1 = *(uint64_t *)(local_rdi + 0x478);
        *(uint64_t *)(arg1 + 0x10) = v_xmm0;
        result = *(uint32_t *)(Arg2 + 0x340);
        *(uint32_t *)(arg1 + 0x18) = (uint32_t)(result);
        result = *(uint16_t *)(Arg2 + 0x344);
        *(uint16_t *)(arg1 + 0x1C) = (uint16_t)(result);
        result = *(uint8_t *)(Arg2 + 0x346);
        *(uint8_t *)(arg1 + 0x1E) = (uint8_t)(result);
        Arg1 = local_rdi;
        result = SepAddTokenLogonSession(Arg1, Arg2, Arg3, Arg4);
    }
    if (((*(uint8_t *)(local_rsp - 0x58 + 0x70)) & (2)) == 0) goto loc_009C724E;
    result = PsReferencePrimaryTokenWithTag(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), (uint32_t)(0x746C6644ULL), Arg3, Arg4);
    result = SeIsSystemContext(result, v_stack_p50, Arg3, Arg4);
    if (sign_flag) goto loc_009C7246;
    if (v_stack_p50 != 0) {
    }
    result = ObfDereferenceObject(result, v_stack_p50, Arg3, Arg4);
loc_009C724E:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p58 + 1472))) & (7));
    local_r14 = v_stack_p58 + 1472;
    if (!(condition_is_equal)) {
        Arg1 = 8;
        Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result)));
        result = (uint32_t)(Arg1);
        local_r14 = (v_stack_p58 + 1472) + (result);
        local_r13 = (uint32_t)((local_r13) - ((uint32_t)(Arg1)));
        v_stack_p64 = (uint32_t)(local_r13);
    }
    local_r15 = (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x98))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x80)))) > ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x98))))) { local_r15 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x80))); }
    local_r13 = 0;
    local_r15 = (uint32_t)((local_r15) + (*(uint32_t *)(arg1 + 0x7C)));
    local_r15 = (local_r15) << (4);
    local_r15 = (local_r15) + (local_r14);
    *(uint64_t *)(v_stack_p58 + 0x98) = local_r14;
    v_stack_p70 = local_r15;
    if ((*(uint8_t *)(v_rip + 0x4A0953)) == 0) goto loc_009C72C1;
    result = SepDuplicateTokenUserAndGroups(Arg1, v_stack_p58, Arg3, Arg4);
    if (!sign_flag) goto loc_009C72FE;
    *(uint64_t *)(v_stack_p58 + 0x98) = 0;
    goto loc_009C7086;
loc_009C72C1:
    *(uint32_t *)(v_stack_p58 + 0x7C) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C)));
    v_stack_p30 = v_stack_p64;
    v_stack_p28 = v_stack_p70;
    v_stack_p20 = local_r15;
    result = RtlCopySidAndAttributesArray((uint32_t)(*(uint32_t *)(arg1 + 0x7C)), *(uint64_t *)(arg1 + 0x98), (uint32_t)(v_stack_p64), local_r14);
loc_009C72FE:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x7C))) << (4));
    local_r14 = (local_r14) + (result);
    *(uint64_t *)(v_stack_p58 + 0xA0) = local_r14;
    if ((*(uint32_t *)(local_rsp - 0x58 + 0x98)) <= 0) goto loc_009C73B9;
loc_009C7325:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x80))) == 0) goto loc_009C7343;
    result = SepSidInSidAndAttributes(*(uint64_t *)(arg1 + 0xA0), (uint32_t)(*(uint32_t *)(arg1 + 0x80)), (uint32_t)(v_stack_p64), *(uint64_t *)(*(uint64_t *)(local_rsp - 0x58 + 0xA0)));
    local_rbx = (uint32_t)((uint32_t)(result));
    local_r15 = v_stack_p70;
    if ((uint8_t)(result) != 0) {
        Arg3 = v_stack_p64;
        result = v_stack_p64;
        v_stack_p30 = result;
        Arg4 = local_r14;
        result = v_stack_p70;
        Arg2 = 0;
        Arg2 = (Arg2) << (4);
        Arg1 = 1;
        Arg2 = (Arg2) + (*(uint64_t *)(local_rsp - 0x58 + 0xA0));
        v_stack_p28 = result;
        v_stack_p20 = v_stack_p70;
        result = RtlCopySidAndAttributesArray(Arg1, Arg2, Arg3, Arg4);
        Arg1 = *(uint32_t *)(v_stack_p58 + 0x80);
        local_rbx = (uint32_t)(result);
        result = *(uint64_t *)(v_stack_p58 + 0xA0);
        Arg1 = (Arg1) + (Arg1);
        local_r15 = v_stack_p70;
        local_r14 = (local_r14) + (16);
        *(uint32_t *)(result + arg1 * 8 + 0x8) = 7;
    }
    local_r12 = (uint32_t)((0) + 1);
    local_r13 = (*(uint64_t *)(local_rsp - 0x58 + 0xA0)) + (16);
    if (((uint32_t)(local_r12)) < (*(uint32_t *)(local_rsp - 0x58 + 0x98))) goto loc_009C7325;
loc_009C73B9:
    local_r12 = 0;
    result = *(uint64_t *)(arg1 + 0xB8);
    local_r14 = *(uint8_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x1) * 4 + 8;
    if (*(uint64_t *)(arg1 + 0xB8) != 0) {
        result = *(uint16_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x2);
        local_r14 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x1) * 4 + 8) + ((uint32_t)(result)));
    }
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(local_r14)), (uint32_t)(0x64546553ULL), Arg4);
    *(uint64_t *)(v_stack_p58 + 0xB0) = result;
    if (result != 0) goto loc_009C740E;
    goto loc_009C7086;
loc_009C740E:
    if ((*(uint32_t *)(arg1 + 0x80)) == 0) goto loc_009C742A;
    if ((*(uint32_t *)(v_stack_p58 + 0x80)) != 0) goto loc_009C742A;
    goto loc_009C7086;
loc_009C742A:
    if ((*(uint32_t *)(v_stack_p58 + 0x80)) <= 0) goto loc_009C7444;
    goto loc_009C744B;
loc_009C7444:
    *(uint64_t *)(v_stack_p58 + 0xA0) = 0;
loc_009C744B:
    result = 1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x70)))) & (8)) != 0) {
        result = 1;
    }
    if ((uint8_t)(result) == 0) goto loc_009C7522;
    result = 0;
    v_stack_p68 = 0;
    *(uint64_t *)(local_rsp - 0x58 - 0x40) = 0;
    *(uint32_t *)(local_rsp - 0x58 - 0x38) = 0;
    *(uint64_t *)(local_rsp - 0x58 - 0x60) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x58 - 0x50) = v_xmm0;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0xD8) + 0x38)) != 0) goto loc_009C7522;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC8)))) & (24)) != 0) goto loc_009C7522;
    *(uint32_t *)(local_rsp - 0x58 - 0x60) = 48;
    v_stack_p38 = v_stack_p68;
    v_stack_p30 = 0;
    v_stack_p28 = 0;
    Arg3 = 0;
    v_stack_p20 = 0;
    *(uint64_t *)(local_rsp - 0x58 - 0x58) = 0;
    *(uint32_t *)(local_rsp - 0x58 - 0x48) = 0;
    *(uint64_t *)(local_rsp - 0x58 - 0x50) = 0;
    *(uint64_t *)(local_rsp - 0x58 - 0x40) = v_xmm0;
    result = SepDuplicateToken(Arg1, local_rsp - 88 - 96, Arg3, 1);
    if (sign_flag) goto loc_009C7522;
    result = SepStopReferencingLogonSession(v_stack_p68, local_rsp - 88 - 96, Arg3, 1);
    if (!sign_flag) goto loc_009C7502;
    result = ObfDereferenceObject(v_stack_p68, local_rsp - 88 - 96, Arg3, 1);
    goto loc_009C7522;
loc_009C7502:
    result = 0;
    if (!(condition_is_equal)) {
        Arg1 = v_stack_p68;
        result = ObfDereferenceObject(Arg1, *(uint64_t *)(arg1 + 0xD8), Arg3, 1);
    }
loc_009C7522:
    result = memcpy(result, *(uint64_t *)(arg1 + 0xB0), (uint32_t)((uint32_t)(local_r14)), 1);
    if ((*(uint64_t *)(arg1 + 0xB8)) == 0) goto loc_009C7555;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xB8))) - (*(uint32_t *)(arg1 + 0xB0)));
    result = (result) + (result);
    *(uint64_t *)(v_stack_p58 + 0xB8) = result;
    goto loc_009C755C;
loc_009C7555:
    *(uint64_t *)(v_stack_p58 + 0xB8) = 0;
loc_009C755C:
    local_r12 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xA8))) - (*(uint32_t *)(arg1 + 0xB0)));
    local_rbx = (uint32_t)(0xC000000DULL);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x320))) != 0) {
        Arg3 = *(uint64_t *)(arg1 + 0x318);
        Arg1 = v_stack_p58;
        Arg2 = *(uint64_t *)(arg1 + 0x310);
        result = SepSetTokenCapabilities(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0x320)));
        local_rbx = (uint32_t)(result);
    }
    if (sign_flag) goto loc_009C7086;
    if (*(uint64_t *)(arg1 + 0x310) == 0) goto loc_009C75B5;
    result = SepSetTokenPackage(v_stack_p58, *(uint64_t *)(arg1 + 0x310), Arg3, (uint32_t)(*(uint32_t *)(arg1 + 0x320)));
    if (!sign_flag) goto loc_009C75B5;
    goto loc_009C7086;
loc_009C75B5:
    if (*(uint64_t *)(arg1 + 0x438) == 0) goto loc_009C75F4;
    result = ((uint32_t)((uint32_t)(14 - 13))) + (14 - 13);
    if (result <= (14 - 13)) {
        Arg1 = 14;
    }
    *(uint64_t *)(v_stack_p58 + 0x438) = *(uint64_t *)(arg1 + 0x438);
loc_009C75F4:
    if (*(uint64_t *)(arg1 + 0x440) == 0) goto loc_009C7629;
    result = (14 - 13) + (14 - 13);
    if (result <= (14 - 13)) {
        Arg1 = 14;
    }
    *(uint64_t *)(v_stack_p58 + 0x440) = *(uint64_t *)(arg1 + 0x440);
loc_009C7629:
    if (*(uint64_t *)(arg1 + 0x480) == 0) goto loc_009C765E;
    result = (14 - 13) + (14 - 13);
    if (result <= (14 - 13)) {
        Arg1 = 14;
    }
    *(uint64_t *)(v_stack_p58 + 0x480) = *(uint64_t *)(arg1 + 0x480);
loc_009C765E:
    result = SepSetTokenTrust(v_stack_p58, *(uint64_t *)(arg1 + 0x450), 14 - 13, 14);
    if (!sign_flag) goto loc_009C7685;
    result = ExReleaseResourceLite(*(uint64_t *)(arg1 + 0x30), *(uint64_t *)(arg1 + 0x450), 14 - 13, 14);
    goto loc_009C708F;
loc_009C7685:
    result = ExReleaseResourceLite(*(uint64_t *)(arg1 + 0x30), *(uint64_t *)(arg1 + 0x450), 14 - 13, 14);
    result = KeLeaveCriticalRegion(*(uint64_t *)(arg1 + 0x30), *(uint64_t *)(arg1 + 0x450), 14 - 13, 14);
    result = ((uint32_t)((uint32_t)(local_r12))) + (result);
    *(uint64_t *)(v_stack_p58 + 0xA8) = result;
    v_stack_p28 = *(uint64_t *)(local_rsp - 0x58 + 0x90);
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x88)));
    result = SepRemoveDisabledGroupsAndPrivileges(v_stack_p58, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x70)))), (uint32_t)(*(uint32_t *)(local_rsp - 0x58 + 0x78)), *(uint64_t *)(local_rsp - 0x58 + 0x80));
    result = RtlSidHashInitialize(*(uint64_t *)(v_stack_p58 + 0x98), (uint32_t)(*(uint32_t *)(v_stack_p58 + 0x7C)), v_stack_p58 + 232, *(uint64_t *)(local_rsp - 0x58 + 0x80));
    result = RtlSidHashInitialize(*(uint64_t *)(v_stack_p58 + 0xA0), (uint32_t)(*(uint32_t *)(v_stack_p58 + 0x80)), v_stack_p58 + 504, *(uint64_t *)(local_rsp - 0x58 + 0x80));
    result = SeCaptureSubjectContext(local_rsp - 88 - 128, (uint32_t)(*(uint32_t *)(v_stack_p58 + 0x80)), v_stack_p58 + 504, *(uint64_t *)(local_rsp - 0x58 + 0x80));
    *(uint64_t *)(local_rsp - 0x58 + 0x10) = *(uint64_t *)(local_rsp - 0x58 - 0x70);
    result = RtlIsSandboxedToken(local_rsp - 88 - 128, (uint8_t)(v_stack_p60), v_stack_p58 + 504, *(uint64_t *)(local_rsp - 0x58 + 0x80));
    if ((uint8_t)(result) == 0) goto loc_009C7795;
    result = RtlIsSandboxedToken(local_rsp - 88, (uint8_t)(v_stack_p60), v_stack_p58 + 504, *(uint64_t *)(local_rsp - 0x58 + 0x80));
    if ((uint8_t)(result) == 0) goto loc_009C7795;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x58 - 0x70) + 0x30), 1, v_stack_p58 + 504, *(uint64_t *)(local_rsp - 0x58 + 0x80));
    result = SepNewTokenAsRestrictedAsProcessToken(v_stack_p58, *(uint64_t *)(local_rsp - 0x58 - 0x70), v_stack_p51, *(uint64_t *)(local_rsp - 0x58 + 0x80));
    result = ExReleaseResourceLite(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x58 - 0x70) + 0x30), *(uint64_t *)(local_rsp - 0x58 - 0x70), v_stack_p51, *(uint64_t *)(local_rsp - 0x58 + 0x80));
    result = KeLeaveCriticalRegion(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x58 - 0x70) + 0x30), *(uint64_t *)(local_rsp - 0x58 - 0x70), v_stack_p51, *(uint64_t *)(local_rsp - 0x58 + 0x80));
    if (sign_flag) goto loc_009C777C;
    if (v_stack_p51 != 0) goto loc_009C7795;
loc_009C777C:
    result = ObfDereferenceObject(v_stack_p58, *(uint64_t *)(local_rsp - 0x58 - 0x70), v_stack_p51, *(uint64_t *)(local_rsp - 0x58 + 0x80));
    result = SeReleaseSubjectContext(local_rsp - 88 - 128, *(uint64_t *)(local_rsp - 0x58 - 0x70), v_stack_p51, *(uint64_t *)(local_rsp - 0x58 + 0x80));
loc_009C778D:
    goto loc_009C6CF0;
loc_009C7795:
    result = SeReleaseSubjectContext(local_rsp - 88 - 128, *(uint64_t *)(local_rsp - 0x58 - 0x70), v_stack_p51, *(uint64_t *)(local_rsp - 0x58 + 0x80));
    if (*(uint64_t *)(v_stack_p58 + 0x318) != 0) {
        Arg2 = *(uint32_t *)(v_stack_p58 + 0x320);
        Arg3 = v_stack_p58 + 808;
        result = RtlSidHashInitialize(*(uint64_t *)(v_stack_p58 + 0x318), Arg2, Arg3, *(uint64_t *)(local_rsp - 0x58 + 0x80));
    }
    if ((*(uint32_t *)(v_rip + 0x61084D)) == 0) goto loc_009C783B;
    if ((*(uint32_t *)(v_rip + 0x4A03D8)) != 15) goto loc_009C783B;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1D0)) != (*(uint64_t *)(v_rip + 0x4A03B3))) goto loc_009C7836;
    Arg1 = (uint32_t)((1) + 1);
    *(uint32_t *)(*(uint64_t *)(v_stack_p58 + 0x478) + 0x118) = (uint32_t)(Arg1);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p58 + 0x478) + 0x118)))) < (*(uint32_t *)(v_rip + 0x4A037E))) goto loc_009C783B;
    result = DbgPrint(v_rip + 1303970, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p58 + 0x478) + 0x118)), v_stack_p58, *(uint64_t *)(local_rsp - 0x58 + 0x80));
    goto loc_009C783B;
loc_009C7836:
loc_009C783B:
    *(uint64_t *)(*(uint64_t *)(local_rsp - 0x58 + 0xB0)) = v_stack_p58;
    goto loc_009C778D;
loc_009C784A:
    goto loc_009C7854;
loc_009C7851:
    local_r13 = 0;
loc_009C7854:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, v_stack_p58, *(uint64_t *)(local_rsp - 0x58 + 0x80));
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)((uint32_t)(result)), Arg2, v_stack_p58, *(uint64_t *)(local_rsp - 0x58 + 0x80));
loc_009C786F:
    if ((*(uint32_t *)(v_rip + 0x6107A1)) != 0) {
        Arg2 = 0;
        Arg1 = v_stack_p58;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_p58, *(uint64_t *)(local_rsp - 0x58 + 0x80));
    }
    goto loc_009C6CF0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x40` | `128` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x58` | `128` | `R` |
| `Arg1` | `+ 0x68` | `128` | `R` |
| `Arg1` | `+ 0x78` | `32` | `R` |
| `Arg1` | `+ 0x7C` | `32` | `R` |
| `Arg1` | `+ 0x80` | `32` | `R` |
| `Arg1` | `+ 0x84` | `32` | `R` |
| `Arg1` | `+ 0x88` | `32` | `R` |
| `Arg1` | `+ 0x90` | `32` | `R` |
| `Arg1` | `+ 0x98` | `64` | `R` |
| `Arg1` | `+ 0xA0` | `64` | `R` |
| `Arg1` | `+ 0xA8` | `32` | `R` |
| `Arg1` | `+ 0xA8` | `64` | `R` |
| `Arg1` | `+ 0xB0` | `32` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `32` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `32` | `R` |
| `Arg1` | `+ 0xC4` | `32` | `R` |
| `Arg1` | `+ 0xC8` | `32` | `R` |
| `Arg1` | `+ 0xD0` | `32` | `R` |
| `Arg1` | `+ 0xD4` | `32` | `R` |
| `Arg1` | `+ 0xD8` | `64` | `R` |
| `Arg1` | `+ 0xE0` | `64` | `R` |
| `Arg1` | `+ 0x308` | `64` | `R` |
| `Arg1` | `+ 0x310` | `64` | `R` |

추가 오프셋 10개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009C6B80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
