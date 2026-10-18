# SepDuplicateToken

- RVA: `0x008B87EC`–`0x008B90F8` (길이 `2,316` bytes)
- VA: `0x00000001408B87EC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082C2C`
- 디코드: `532`개 명령, `2,316/2,316` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **46**; 고유 호출 대상: **29**
- 직접 호출자로 확인된 함수: **18**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x008B884C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B888D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B88AD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B88BF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B88D2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B8944` → [ObCreateObjectEx](../89/ObCreateObjectEx_function_0089B1E0.md) (function, `0x0089B1E0`)
- `0x008B8955` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B895F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B8972` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B89C4` → [ExInitializeResourceLite](../../text/41/ExInitializeResourceLite_function_0041F9A0.md) (function, `0x0041F9A0`)
- `0x008B8A3E` → [RtlWalkFrameChain](../../text/2F/RtlWalkFrameChain_function_002F85E0.md) (function, `0x002F85E0`)
- `0x008B8A65` → [RtlWalkFrameChain](../../text/2F/RtlWalkFrameChain_function_002F85E0.md) (function, `0x002F85E0`)
- `0x008B8A81` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B8AC2` → [Feature_2045735225__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_2045735225__private_IsEnabledDeviceUsageNoInline_function_004F0968.md) (function, `0x004F0968`)
- `0x008B8B07` → [SepSetTokenSessionById](../A0/SepSetTokenSessionById_function_00A0DAE4.md) (function, `0x00A0DAE4`)
- `0x008B8B4D` → [Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline_function_004F2D58.md) (function, `0x004F2D58`)
- `0x008B8B64` → [Feature_AgentId2__private_IsEnabledDeviceUsageNoInline](../../text/60/Feature_AgentId2__private_IsEnabledDeviceUsageNoInline_function_006066CC.md) (function, `0x006066CC`)
- `0x008B8BC9` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008B8BF6` → [SepModifyTokenPolicyCounter](../79/SepModifyTokenPolicyCounter_function_0079D1E0.md) (function, `0x0079D1E0`)
- `0x008B8C01` → [SepDuplicateLogonSessionReference](../../text/44/SepDuplicateLogonSessionReference_function_004463B0.md) (function, `0x004463B0`)
- `0x008B8C10` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008B8C15` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008B8C1D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008B8C29` → [Feature_2045735225__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_2045735225__private_IsEnabledDeviceUsageNoInline_function_004F0968.md) (function, `0x004F0968`)
- `0x008B8C54` → [SepReferenceLogonSession](../A3/SepReferenceLogonSession_function_00A3B74C.md) (function, `0x00A3B74C`)
- `0x008B8C6B` → [SepRefDerefLuidToIndexEntryIfNecessary](../9F/SepRefDerefLuidToIndexEntryIfNecessary_function_009FEFD8.md) (function, `0x009FEFD8`)
- `0x008B8C95` → [AuthzBasepDuplicateSecurityAttributes](../../text/30/AuthzBasepDuplicateSecurityAttributes_function_003023C0.md) (function, `0x003023C0`)
- `0x008B8CB9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008B8CE8` → [SepDuplicateTokenUserAndGroups](../9F/SepDuplicateTokenUserAndGroups_function_009FDFD4.md) (function, `0x009FDFD4`)
- `0x008B8D8E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B8DB9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008B8E10` → [SepSetTokenCapabilities](../9C/SepSetTokenCapabilities_function_009C9AF4.md) (function, `0x009C9AF4`)
- `0x008B8E2E` → [SepSetTokenPackage](../A2/SepSetTokenPackage_function_00A20CB8.md) (function, `0x00A20CB8`)
- `0x008B8EF0` → [SepDuplicateTokenClaims](../A7/SepDuplicateTokenClaims_function_00A762C8.md) (function, `0x00A762C8`)
- `0x008B8F0A` → [SepSetTokenTrust](../9E/SepSetTokenTrust_function_009E79B0.md) (function, `0x009E79B0`)
- `0x008B8F1D` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008B8F22` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008B8FE3` → [SepAddTokenLogonSession](../7A/SepAddTokenLogonSession_function_007A14E0.md) (function, `0x007A14E0`)
- `0x008B8FF1` → [SepMakeTokenEffectiveOnly](../A1/SepMakeTokenEffectiveOnly_function_00A17C18.md) (function, `0x00A17C18`)
- `0x008B9007` → [RtlSidHashInitialize](../../text/41/RtlSidHashInitialize_function_00416EA0.md) (function, `0x00416EA0`)
- `0x008B9020` → [RtlSidHashInitialize](../../text/41/RtlSidHashInitialize_function_00416EA0.md) (function, `0x00416EA0`)
- `0x008B903A` → [RtlSidHashInitialize](../../text/41/RtlSidHashInitialize_function_00416EA0.md) (function, `0x00416EA0`)
- `0x008B90AF` → [DbgPrint](../../text/35/DbgPrint_function_00358CB0.md) (function, `0x00358CB0`)
- `0x008B90CC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B90D6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B90E9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [SepGetAnonymousToken](../../text/30/SepGetAnonymousToken_function_00301830.md) at `0x003018A2`
- [SepLinkLogonSessions](../../text/4A/SepLinkLogonSessions_function_004AAE78.md) at `0x004AAFA7`
- [SepLinkLogonSessions](../../text/4A/SepLinkLogonSessions_function_004AAE78.md) at `0x004AB02B`
- [SepCreateAppContainerToken](../../text/4F/SepCreateAppContainerToken_function_004F43AC.md) at `0x004F47FC`
- [SepOneWayLinkLogonSessions](../../text/60/SepOneWayLinkLogonSessions_function_006068D8.md) at `0x00606A1B`
- [SepOneWayLinkLogonSessions](../../text/60/SepOneWayLinkLogonSessions_function_006068D8.md) at `0x00606A68`
- [SeDuplicateTokenWithPredictedClaims](../6F/SeDuplicateTokenWithPredictedClaims_function_006FD084.md) at `0x006FD175`
- [sub_00891DF4](../89/Unknown_function_00891DF4.md) at `0x00891E15`
- [NtDuplicateToken](NtDuplicateToken_function_008B6DF0.md) at `0x008B6FB9`
- [NtOpenThreadTokenEx](NtOpenThreadTokenEx_function_008B7840.md) at `0x008B7BCF`
- [PsImpersonateClient](../8C/PsImpersonateClient_function_008CBE10.md) at `0x008CC10B`
- [PsImpersonateClient](../8C/PsImpersonateClient_function_008CBE10.md) at `0x008CC23B`
- [SepFilterToken](../9C/SepFilterToken_function_009C6B80.md) at `0x009C74DF`
- [SeCopyClientToken](../9E/SeCopyClientToken_function_009EC5A8.md) at `0x009EC60B`
- [NtImpersonateAnonymousToken](../A3/NtImpersonateAnonymousToken_function_00A3A150.md) at `0x00A3A3EE`
- [SeGetLinkedToken](../A3/SeGetLinkedToken_function_00A3B640.md) at `0x00A3B72D`
- [SeGetLogonSessionToken](../A6/SeGetLogonSessionToken_function_00A6E4B0.md) at `0x00A6E574`
- [SeSubProcessToken](../AA/SeSubProcessToken_function_00AAD570.md) at `0x00AAD9AC`
- [NtCreateLowBoxToken](../AB/NtCreateLowBoxToken_function_00AB9880.md) at `0x00ABA05D`
- [SeDuplicateTokenAndAddOriginClaim](../AC/SeDuplicateTokenAndAddOriginClaim_function_00AC6DF4.md) at `0x00AC6E6A`
- [NtQueryInformationToken](../AE/NtQueryInformationToken_function_00AECDD0.md) at `0x00AED6E9`
- [NtQueryInformationToken](../AE/NtQueryInformationToken_function_00AECDD0.md) at `0x00AEE9AD`

### Static image references
- `0x008B8876` → RVA `0x00FD8010` (`PAGEDATA`; read)
- `0x008B8923` → RVA `0x00FD8020` (`PAGEDATA`; read)
- `0x008B897F` → RVA `0x00012D08` (`.rdata`; read)
- `0x008B898D` → RVA `0x00E0EBF0` (`.data`; read/write)
- `0x008B8AEB` → RVA `0x00FD9AD8` (`PAGEDATA`; read/write)
- `0x008B8CC8` → RVA `0x00E67BF0` (`.data`; read)
- `0x008B9048` → RVA `0x00E67BA4` (`.data`; read)
- `0x008B9061` → RVA `0x00E67B98` (`.data`; read)
- `0x008B9074` → RVA `0x00E67BA8` (`.data`; read/write)
- `0x008B909D` → RVA `0x00E67BA0` (`.data`; read)
- `0x008B90A8` → RVA `0x00B05DD0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **34**
  - `0x008B884C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B888D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B88AD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B88BF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B88D2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B8955` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B895F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B8972` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B89C4` → [ExInitializeResourceLite](../../text/41/ExInitializeResourceLite_function_0041F9A0.md) (`PAGE` → `.text`)
  - `0x008B8A3E` → [RtlWalkFrameChain](../../text/2F/RtlWalkFrameChain_function_002F85E0.md) (`PAGE` → `.text`)
  - `0x008B8A65` → [RtlWalkFrameChain](../../text/2F/RtlWalkFrameChain_function_002F85E0.md) (`PAGE` → `.text`)
  - `0x008B8A81` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B8AC2` → [Feature_2045735225__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_2045735225__private_IsEnabledDeviceUsageNoInline_function_004F0968.md) (`PAGE` → `.text`)
  - `0x008B8B4D` → [Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline_function_004F2D58.md) (`PAGE` → `.text`)
  - `0x008B8B64` → [Feature_AgentId2__private_IsEnabledDeviceUsageNoInline](../../text/60/Feature_AgentId2__private_IsEnabledDeviceUsageNoInline_function_006066CC.md) (`PAGE` → `.text`)
  - `0x008B8BC9` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008B8C01` → [SepDuplicateLogonSessionReference](../../text/44/SepDuplicateLogonSessionReference_function_004463B0.md) (`PAGE` → `.text`)
  - `0x008B8C10` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008B8C15` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008B8C1D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008B8C29` → [Feature_2045735225__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_2045735225__private_IsEnabledDeviceUsageNoInline_function_004F0968.md) (`PAGE` → `.text`)
  - `0x008B8C95` → [AuthzBasepDuplicateSecurityAttributes](../../text/30/AuthzBasepDuplicateSecurityAttributes_function_003023C0.md) (`PAGE` → `.text`)
  - `0x008B8CB9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008B8D8E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B8DB9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008B8F1D` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008B8F22` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008B9007` → [RtlSidHashInitialize](../../text/41/RtlSidHashInitialize_function_00416EA0.md) (`PAGE` → `.text`)
  - `0x008B9020` → [RtlSidHashInitialize](../../text/41/RtlSidHashInitialize_function_00416EA0.md) (`PAGE` → `.text`)
  - `0x008B903A` → [RtlSidHashInitialize](../../text/41/RtlSidHashInitialize_function_00416EA0.md) (`PAGE` → `.text`)
  - `0x008B90AF` → [DbgPrint](../../text/35/DbgPrint_function_00358CB0.md) (`PAGE` → `.text`)
  - `0x008B90CC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B90D6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B90E9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008B87EC  48 8B C4                        mov rax, rsp
008B87EF  48 89 58 08                     mov qword ptr [rax + 8], rbx
008B87F3  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
008B87F7  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
008B87FB  44 88 40 18                     mov byte ptr [rax + 0x18], r8b
008B87FF  55                              push rbp
008B8800  41 54                           push r12
008B8802  41 55                           push r13
008B8804  41 56                           push r14
008B8806  41 57                           push r15
008B8808  48 8B EC                        mov rbp, rsp
008B880B  48 83 EC 60                     sub rsp, 0x60
008B880F  44 8B 65 50                     mov r12d, dword ptr [rbp + 0x50]
008B8813  45 33 FF                        xor r15d, r15d
008B8816  4C 89 7D F0                     mov qword ptr [rbp - 0x10], r15
008B881A  45 8B E9                        mov r13d, r9d
008B881D  4C 8B F2                        mov r14, rdx
008B8820  48 8B F9                        mov rdi, rcx
008B8823  41 8B DF                        mov ebx, r15d
008B8826  41 83 F9 02                     cmp r9d, 2
008B882A  75 10                           jne 0x1408b883c
008B882C  41 83 FC 03                     cmp r12d, 3
008B8830  76 0A                           jbe 0x1408b883c
008B8832  B8 A5 00 00 C0                  mov eax, 0xc00000a5
008B8837  E9 A0 00 00 00                  jmp 0x1408b88dc
008B883C  BA 30 00 00 00                  mov edx, 0x30
008B8841  B9 00 01 00 00                  mov ecx, 0x100
008B8846  41 B8 53 65 41 74               mov r8d, 0x74416553
008B884C  E8 9F 98 2C 00                  call 0x140b820f0
008B8851  48 8B F0                        mov rsi, rax
008B8854  48 85 C0                        test rax, rax
008B8857  74 7E                           je 0x1408b88d7
008B8859  44 89 38                        mov dword ptr [rax], r15d
008B885C  48 83 C0 08                     add rax, 8
008B8860  44 89 7E 18                     mov dword ptr [rsi + 0x18], r15d
008B8864  48 89 40 08                     mov qword ptr [rax + 8], rax
008B8868  48 89 00                        mov qword ptr [rax], rax
008B886B  48 8D 46 20                     lea rax, [rsi + 0x20]
008B886F  48 89 40 08                     mov qword ptr [rax + 8], rax
008B8873  48 89 00                        mov qword ptr [rax], rax
008B8876  44 39 3D 93 F7 71 00            cmp dword ptr [rip + 0x71f793], r15d
008B887D  74 20                           je 0x1408b889f
008B887F  BA 20 01 00 00                  mov edx, 0x120
008B8884  41 B8 53 65 41 74               mov r8d, 0x74416553
008B888A  8D 4A E0                        lea ecx, [rdx - 0x20]
008B888D  E8 5E 98 2C 00                  call 0x140b820f0
008B8892  48 8B D8                        mov rbx, rax
008B8895  48 85 C0                        test rax, rax
008B8898  75 05                           jne 0x1408b889f
008B889A  48 8B CE                        mov rcx, rsi
008B889D  EB 31                           jmp 0x1408b88d0
008B889F  BA 68 00 00 00                  mov edx, 0x68
008B88A4  41 B8 53 65 54 6C               mov r8d, 0x6c546553
008B88AA  8D 4A D8                        lea ecx, [rdx - 0x28]
008B88AD  E8 3E 98 2C 00                  call 0x140b820f0
008B88B2  4C 8B F8                        mov r15, rax
008B88B5  48 85 C0                        test rax, rax
008B88B8  75 41                           jne 0x1408b88fb
008B88BA  33 D2                           xor edx, edx
008B88BC  48 8B CE                        mov rcx, rsi
008B88BF  E8 AC 9F 2C 00                  call 0x140b82870
008B88C4  44 39 3D 45 F7 71 00            cmp dword ptr [rip + 0x71f745], r15d
008B88CB  74 0A                           je 0x1408b88d7
008B88CD  48 8B CB                        mov rcx, rbx
008B88D0  33 D2                           xor edx, edx
008B88D2  E8 99 9F 2C 00                  call 0x140b82870
008B88D7  B8 9A 00 00 C0                  mov eax, 0xc000009a
008B88DC  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
008B88E1  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
008B88E5  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
008B88E9  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
008B88ED  49 8B E3                        mov rsp, r11
008B88F0  41 5F                           pop r15
008B88F2  41 5E                           pop r14
008B88F4  41 5D                           pop r13
008B88F6  41 5C                           pop r12
008B88F8  5D                              pop rbp
008B88F9  C3                              ret
008B88FA  CC                              int3
008B88FB  8B 8F 84 00 00 00               mov ecx, dword ptr [rdi + 0x84]
008B8901  81 C1 C0 05 00 00               add ecx, 0x5c0
008B8907  81 F9 C0 05 00 00               cmp ecx, 0x5c0
008B890D  0F 82 B4 07 00 00               jb 0x1408b90c7
008B8913  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
008B8919  4C 8D 45 F0                     lea r8, [rbp - 0x10]
008B891D  8B 87 88 00 00 00               mov eax, dword ptr [rdi + 0x88]
008B8923  48 8B 15 F6 F6 71 00            mov rdx, qword ptr [rip + 0x71f6f6]
008B892A  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
008B892F  4D 8B C6                        mov r8, r14
008B8932  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
008B8936  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008B893A  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
008B893E  8A 4D 58                        mov cl, byte ptr [rbp + 0x58]
008B8941  44 8A C9                        mov r9b, cl
008B8944  E8 97 28 FE FF                  call 0x14089b1e0
008B8949  44 8B F0                        mov r14d, eax
008B894C  85 C0                           test eax, eax
008B894E  79 2F                           jns 0x1408b897f
008B8950  33 D2                           xor edx, edx
008B8952  48 8B CE                        mov rcx, rsi
008B8955  E8 16 9F 2C 00                  call 0x140b82870
008B895A  33 D2                           xor edx, edx
008B895C  49 8B CF                        mov rcx, r15
008B895F  E8 0C 9F 2C 00                  call 0x140b82870
008B8964  83 3D A5 F6 71 00 00            cmp dword ptr [rip + 0x71f6a5], 0
008B896B  74 0A                           je 0x1408b8977
008B896D  33 D2                           xor edx, edx
008B896F  48 8B CB                        mov rcx, rbx
008B8972  E8 F9 9E 2C 00                  call 0x140b82870
008B8977  41 8B C6                        mov eax, r14d
008B897A  E9 5D FF FF FF                  jmp 0x1408b88dc
008B897F  48 8B 0D 82 A3 75 FF            mov rcx, qword ptr [rip - 0x8a5c7e]
008B8986  48 8B 55 F0                     mov rdx, qword ptr [rbp - 0x10]
008B898A  48 8B C1                        mov rax, rcx
008B898D  F0 48 0F C1 05 5A 62 55 00      lock xadd qword ptr [rip + 0x55625a], rax
008B8996  4C 8B 75 F0                     mov r14, qword ptr [rbp - 0x10]
008B899A  48 03 C1                        add rax, rcx
008B899D  89 42 10                        mov dword ptr [rdx + 0x10], eax
008B89A0  49 8B CF                        mov rcx, r15
008B89A3  48 C1 E8 20                     shr rax, 0x20
008B89A7  89 42 14                        mov dword ptr [rdx + 0x14], eax
008B89AA  41 C6 86 CC 00 00 00 00         mov byte ptr [r14 + 0xcc], 0
008B89B2  45 89 AE C0 00 00 00            mov dword ptr [r14 + 0xc0], r13d
008B89B9  45 89 A6 C4 00 00 00            mov dword ptr [r14 + 0xc4], r12d
008B89C0  4D 89 7E 30                     mov qword ptr [r14 + 0x30], r15
008B89C4  E8 D7 6F B6 FF                  call 0x14041f9a0
008B89C9  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
008B89CD  45 33 ED                        xor r13d, r13d
008B89D0  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
008B89D4  0F 10 07                        movups xmm0, xmmword ptr [rdi]
008B89D7  F3 41 0F 7F 06                  movdqu xmmword ptr [r14], xmm0
008B89DC  45 89 AE 8C 00 00 00            mov dword ptr [r14 + 0x8c], r13d
008B89E3  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
008B89E7  49 89 46 20                     mov qword ptr [r14 + 0x20], rax
008B89EB  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
008B89EF  49 89 46 28                     mov qword ptr [r14 + 0x28], rax
008B89F3  48 8B 87 E0 00 00 00            mov rax, qword ptr [rdi + 0xe0]
008B89FA  49 89 86 E0 00 00 00            mov qword ptr [r14 + 0xe0], rax
008B8A01  4D 89 AE 60 04 00 00            mov qword ptr [r14 + 0x460], r13
008B8A08  4D 89 AE 68 04 00 00            mov qword ptr [r14 + 0x468], r13
008B8A0F  4D 89 AE 48 04 00 00            mov qword ptr [r14 + 0x448], r13
008B8A16  49 89 9E 78 04 00 00            mov qword ptr [r14 + 0x478], rbx
008B8A1D  45 89 6E 78                     mov dword ptr [r14 + 0x78], r13d
008B8A21  4D 89 AE 88 04 00 00            mov qword ptr [r14 + 0x488], r13
008B8A28  44 39 2D E1 F5 71 00            cmp dword ptr [rip + 0x71f5e1], r13d
008B8A2F  74 39                           je 0x1408b8a6a
008B8A31  48 8D 4B 28                     lea rcx, [rbx + 0x28]
008B8A35  45 33 C0                        xor r8d, r8d
008B8A38  41 8D 5D 1E                     lea ebx, [r13 + 0x1e]
008B8A3C  8B D3                           mov edx, ebx
008B8A3E  E8 9D FB A3 FF                  call 0x1402f85e0
008B8A43  44 0F 20 C1                     mov rcx, cr8
008B8A47  80 F9 02                        cmp cl, 2
008B8A4A  73 1E                           jae 0x1408b8a6a
008B8A4C  2B D8                           sub ebx, eax
008B8A4E  8B C8                           mov ecx, eax
008B8A50  49 8B 86 78 04 00 00            mov rax, qword ptr [r14 + 0x478]
008B8A57  45 8D 45 01                     lea r8d, [r13 + 1]
008B8A5B  48 83 C0 28                     add rax, 0x28
008B8A5F  8B D3                           mov edx, ebx
008B8A61  48 8D 0C C8                     lea rcx, [rax + rcx*8]
008B8A65  E8 76 FB A3 FF                  call 0x1402f85e0
008B8A6A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B8A73  B2 01                           mov dl, 1
008B8A75  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B8A7C  90                              nop
008B8A7D  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B8A81  E8 3A 91 95 FF                  call 0x140211bc0
008B8A86  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
008B8A8A  48 8B 5D F0                     mov rbx, qword ptr [rbp - 0x10]
008B8A8E  48 89 43 38                     mov qword ptr [rbx + 0x38], rax
008B8A92  8B 87 88 00 00 00               mov eax, dword ptr [rdi + 0x88]
008B8A98  89 83 88 00 00 00               mov dword ptr [rbx + 0x88], eax
008B8A9E  8B 87 90 00 00 00               mov eax, dword ptr [rdi + 0x90]
008B8AA4  89 83 90 00 00 00               mov dword ptr [rbx + 0x90], eax
008B8AAA  8B 87 80 00 00 00               mov eax, dword ptr [rdi + 0x80]
008B8AB0  89 83 80 00 00 00               mov dword ptr [rbx + 0x80], eax
008B8AB6  8B 87 84 00 00 00               mov eax, dword ptr [rdi + 0x84]
008B8ABC  89 83 84 00 00 00               mov dword ptr [rbx + 0x84], eax
008B8AC2  E8 A1 7E C3 FF                  call 0x1404f0968
008B8AC7  8B 8F C8 00 00 00               mov ecx, dword ptr [rdi + 0xc8]
008B8ACD  85 C0                           test eax, eax
008B8ACF  74 08                           je 0x1408b8ad9
008B8AD1  81 E1 DF FB FF EF               and ecx, 0xeffffbdf
008B8AD7  EB 06                           jmp 0x1408b8adf
008B8AD9  81 E1 DF FB FF FF               and ecx, 0xfffffbdf
008B8ADF  89 8B C8 00 00 00               mov dword ptr [rbx + 0xc8], ecx
008B8AE5  0F BA E1 18                     bt ecx, 0x18
008B8AE9  73 0B                           jae 0x1408b8af6
008B8AEB  F0 FF 05 E6 0F 72 00            lock inc dword ptr [rip + 0x720fe6]
008B8AF2  48 8B 5D F0                     mov rbx, qword ptr [rbp - 0x10]
008B8AF6  8B 57 78                        mov edx, dword ptr [rdi + 0x78]
008B8AF9  45 33 C9                        xor r9d, r9d
008B8AFC  45 33 C0                        xor r8d, r8d
008B8AFF  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
008B8B04  48 8B CB                        mov rcx, rbx
008B8B07  E8 D8 4F 15 00                  call 0x140a0dae4
008B8B0C  8B 47 78                        mov eax, dword ptr [rdi + 0x78]
008B8B0F  41 89 46 78                     mov dword ptr [r14 + 0x78], eax
008B8B13  0F 10 47 58                     movups xmm0, xmmword ptr [rdi + 0x58]
008B8B17  0F 11 43 58                     movups xmmword ptr [rbx + 0x58], xmm0
008B8B1B  0F 10 4F 68                     movups xmm1, xmmword ptr [rdi + 0x68]
008B8B1F  0F 11 4B 68                     movups xmmword ptr [rbx + 0x68], xmm1
008B8B23  8B 87 D0 00 00 00               mov eax, dword ptr [rdi + 0xd0]
008B8B29  89 83 D0 00 00 00               mov dword ptr [rbx + 0xd0], eax
008B8B2F  8B 87 D4 00 00 00               mov eax, dword ptr [rdi + 0xd4]
008B8B35  89 83 D4 00 00 00               mov dword ptr [rbx + 0xd4], eax
008B8B3B  0F 10 47 40                     movups xmm0, xmmword ptr [rdi + 0x40]
008B8B3F  0F 11 43 40                     movups xmmword ptr [rbx + 0x40], xmm0
008B8B43  F2 0F 10 4F 50                  movsd xmm1, qword ptr [rdi + 0x50]
008B8B48  F2 0F 11 4B 50                  movsd qword ptr [rbx + 0x50], xmm1
008B8B4D  E8 06 A2 C3 FF                  call 0x1404f2d58
008B8B52  85 C0                           test eax, eax
008B8B54  74 0E                           je 0x1408b8b64
008B8B56  48 8B 87 90 04 00 00            mov rax, qword ptr [rdi + 0x490]
008B8B5D  48 89 83 90 04 00 00            mov qword ptr [rbx + 0x490], rax
008B8B64  E8 63 DB D4 FF                  call 0x1406066cc
008B8B69  85 C0                           test eax, eax
008B8B6B  74 19                           je 0x1408b8b86
008B8B6D  8B 83 90 04 00 00               mov eax, dword ptr [rbx + 0x490]
008B8B73  8B C8                           mov ecx, eax
008B8B75  33 8F 90 04 00 00               xor ecx, dword ptr [rdi + 0x490]
008B8B7B  83 E1 02                        and ecx, 2
008B8B7E  33 C8                           xor ecx, eax
008B8B80  89 8B 90 04 00 00               mov dword ptr [rbx + 0x490], ecx
008B8B86  48 89 B3 08 03 00 00            mov qword ptr [rbx + 0x308], rsi
008B8B8D  4C 8D A3 28 03 00 00            lea r12, [rbx + 0x328]
008B8B94  4C 89 AB 38 04 00 00            mov qword ptr [rbx + 0x438], r13
008B8B9B  33 D2                           xor edx, edx
008B8B9D  4C 89 AB 40 04 00 00            mov qword ptr [rbx + 0x440], r13
008B8BA4  41 B8 10 01 00 00               mov r8d, 0x110
008B8BAA  4C 89 AB 80 04 00 00            mov qword ptr [rbx + 0x480], r13
008B8BB1  49 8B CC                        mov rcx, r12
008B8BB4  4C 89 AB 18 03 00 00            mov qword ptr [rbx + 0x318], r13
008B8BBB  4C 89 AB 10 03 00 00            mov qword ptr [rbx + 0x310], r13
008B8BC2  44 89 AB 20 03 00 00            mov dword ptr [rbx + 0x320], r13d
008B8BC9  E8 72 E0 E0 FF                  call 0x1406c6c40
008B8BCE  4C 89 AB B0 00 00 00            mov qword ptr [rbx + 0xb0], r13
008B8BD5  4C 89 AB 50 04 00 00            mov qword ptr [rbx + 0x450], r13
008B8BDC  4C 89 AB 58 04 00 00            mov qword ptr [rbx + 0x458], r13
008B8BE3  4C 89 AB 70 04 00 00            mov qword ptr [rbx + 0x470], r13
008B8BEA  80 7B 77 02                     cmp byte ptr [rbx + 0x77], 2
008B8BEE  75 0B                           jne 0x1408b8bfb
008B8BF0  B2 01                           mov dl, 1
008B8BF2  48 8D 4B 58                     lea rcx, [rbx + 0x58]
008B8BF6  E8 E5 45 EE FF                  call 0x14079d1e0
008B8BFB  48 8B D7                        mov rdx, rdi
008B8BFE  48 8B CB                        mov rcx, rbx
008B8C01  E8 AA D7 B8 FF                  call 0x1404463b0
008B8C06  8B F0                           mov esi, eax
008B8C08  85 C0                           test eax, eax
008B8C0A  79 1D                           jns 0x1408b8c29
008B8C0C  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B8C10  E8 FB 6D 9A FF                  call 0x14025fa10
008B8C15  E8 96 4C 9A FF                  call 0x14025d8b0
008B8C1A  48 8B CB                        mov rcx, rbx
008B8C1D  E8 2E 07 A4 FF                  call 0x1402f9350
008B8C22  8B C6                           mov eax, esi
008B8C24  E9 B3 FC FF FF                  jmp 0x1408b88dc
008B8C29  E8 3A 7D C3 FF                  call 0x1404f0968
008B8C2E  85 C0                           test eax, eax
008B8C30  74 34                           je 0x1408b8c66
008B8C32  41 BE 00 00 00 10               mov r14d, 0x10000000
008B8C38  44 85 B7 C8 00 00 00            test dword ptr [rdi + 0xc8], r14d
008B8C3F  74 25                           je 0x1408b8c66
008B8C41  48 8B 8B D8 00 00 00            mov rcx, qword ptr [rbx + 0xd8]
008B8C48  48 8D 55 F8                     lea rdx, [rbp - 8]
008B8C4C  48 83 C1 10                     add rcx, 0x10
008B8C50  4C 89 6D F8                     mov qword ptr [rbp - 8], r13
008B8C54  E8 F3 2A 18 00                  call 0x140a3b74c
008B8C59  8B F0                           mov esi, eax
008B8C5B  85 C0                           test eax, eax
008B8C5D  78 AD                           js 0x1408b8c0c
008B8C5F  44 09 B3 C8 00 00 00            or dword ptr [rbx + 0xc8], r14d
008B8C66  33 D2                           xor edx, edx
008B8C68  48 8B CF                        mov rcx, rdi
008B8C6B  E8 68 63 14 00                  call 0x1409fefd8
008B8C70  48 8B 97 70 04 00 00            mov rdx, qword ptr [rdi + 0x470]
008B8C77  48 89 93 70 04 00 00            mov qword ptr [rbx + 0x470], rdx
008B8C7E  48 8B 8F 08 03 00 00            mov rcx, qword ptr [rdi + 0x308]
008B8C85  44 39 29                        cmp dword ptr [rcx], r13d
008B8C88  74 1A                           je 0x1408b8ca4
008B8C8A  44 8A 45 60                     mov r8b, byte ptr [rbp + 0x60]
008B8C8E  48 8B 93 08 03 00 00            mov rdx, qword ptr [rbx + 0x308]
008B8C95  E8 26 97 A4 FF                  call 0x1403023c0
008B8C9A  8B F0                           mov esi, eax
008B8C9C  85 C0                           test eax, eax
008B8C9E  0F 88 68 FF FF FF               js 0x1408b8c0c
008B8CA4  44 8B 87 84 00 00 00            mov r8d, dword ptr [rdi + 0x84]
008B8CAB  48 8D 97 C0 05 00 00            lea rdx, [rdi + 0x5c0]
008B8CB2  48 8D 8B C0 05 00 00            lea rcx, [rbx + 0x5c0]
008B8CB9  E8 82 DB E0 FF                  call 0x1406c6840
008B8CBE  4C 8B F3                        mov r14, rbx
008B8CC1  41 83 CF FF                     or r15d, 0xffffffff
008B8CC5  4C 2B F7                        sub r14, rdi
008B8CC8  44 38 2D 21 EF 5A 00            cmp byte ptr [rip + 0x5aef21], r13b
008B8CCF  74 2E                           je 0x1408b8cff
008B8CD1  48 8B 8F 98 00 00 00            mov rcx, qword ptr [rdi + 0x98]
008B8CD8  48 8B D3                        mov rdx, rbx
008B8CDB  49 03 CE                        add rcx, r14
008B8CDE  48 89 8B 98 00 00 00            mov qword ptr [rbx + 0x98], rcx
008B8CE5  48 8B CF                        mov rcx, rdi
008B8CE8  E8 E7 52 14 00                  call 0x1409fdfd4
008B8CED  8B F0                           mov esi, eax
008B8CEF  85 C0                           test eax, eax
008B8CF1  79 36                           jns 0x1408b8d29
008B8CF3  4C 89 AB 98 00 00 00            mov qword ptr [rbx + 0x98], r13
008B8CFA  E9 0D FF FF FF                  jmp 0x1408b8c0c
008B8CFF  8B 47 7C                        mov eax, dword ptr [rdi + 0x7c]
008B8D02  89 43 7C                        mov dword ptr [rbx + 0x7c], eax
008B8D05  48 8B 8F 98 00 00 00            mov rcx, qword ptr [rdi + 0x98]
008B8D0C  49 03 CE                        add rcx, r14
008B8D0F  48 89 8B 98 00 00 00            mov qword ptr [rbx + 0x98], rcx
008B8D16  8B 43 7C                        mov eax, dword ptr [rbx + 0x7c]
008B8D19  85 C0                           test eax, eax
008B8D1B  74 0C                           je 0x1408b8d29
008B8D1D  4C 01 31                        add qword ptr [rcx], r14
008B8D20  48 8D 49 10                     lea rcx, [rcx + 0x10]
008B8D24  41 03 C7                        add eax, r15d
008B8D27  75 F4                           jne 0x1408b8d1d
008B8D29  48 8B 87 A0 00 00 00            mov rax, qword ptr [rdi + 0xa0]
008B8D30  48 89 83 A0 00 00 00            mov qword ptr [rbx + 0xa0], rax
008B8D37  48 85 C0                        test rax, rax
008B8D3A  74 20                           je 0x1408b8d5c
008B8D3C  49 03 C6                        add rax, r14
008B8D3F  48 89 83 A0 00 00 00            mov qword ptr [rbx + 0xa0], rax
008B8D46  8B 8B 80 00 00 00               mov ecx, dword ptr [rbx + 0x80]
008B8D4C  85 C9                           test ecx, ecx
008B8D4E  74 0C                           je 0x1408b8d5c
008B8D50  4C 01 30                        add qword ptr [rax], r14
008B8D53  48 8D 40 10                     lea rax, [rax + 0x10]
008B8D57  41 03 CF                        add ecx, r15d
008B8D5A  75 F4                           jne 0x1408b8d50
008B8D5C  48 8B 87 A8 00 00 00            mov rax, qword ptr [rdi + 0xa8]
008B8D63  0F B6 50 01                     movzx edx, byte ptr [rax + 1]
008B8D67  48 8B 87 B8 00 00 00            mov rax, qword ptr [rdi + 0xb8]
008B8D6E  8D 14 95 08 00 00 00            lea edx, [rdx*4 + 8]
008B8D75  48 85 C0                        test rax, rax
008B8D78  74 06                           je 0x1408b8d80
008B8D7A  0F B7 40 02                     movzx eax, word ptr [rax + 2]
008B8D7E  03 D0                           add edx, eax
008B8D80  B9 00 01 00 00                  mov ecx, 0x100
008B8D85  44 8B FA                        mov r15d, edx
008B8D88  41 B8 53 65 54 64               mov r8d, 0x64546553
008B8D8E  E8 5D 93 2C 00                  call 0x140b820f0
008B8D93  48 89 83 B0 00 00 00            mov qword ptr [rbx + 0xb0], rax
008B8D9A  4C 8B F0                        mov r14, rax
008B8D9D  48 85 C0                        test rax, rax
008B8DA0  75 0A                           jne 0x1408b8dac
008B8DA2  BE 9A 00 00 C0                  mov esi, 0xc000009a
008B8DA7  E9 60 FE FF FF                  jmp 0x1408b8c0c
008B8DAC  48 8B 97 B0 00 00 00            mov rdx, qword ptr [rdi + 0xb0]
008B8DB3  4D 8B C7                        mov r8, r15
008B8DB6  49 8B CE                        mov rcx, r14
008B8DB9  E8 82 DA E0 FF                  call 0x1406c6840
008B8DBE  48 8B 87 B8 00 00 00            mov rax, qword ptr [rdi + 0xb8]
008B8DC5  4C 2B B7 B0 00 00 00            sub r14, qword ptr [rdi + 0xb0]
008B8DCC  48 89 83 B8 00 00 00            mov qword ptr [rbx + 0xb8], rax
008B8DD3  48 85 C0                        test rax, rax
008B8DD6  74 0A                           je 0x1408b8de2
008B8DD8  49 03 C6                        add rax, r14
008B8DDB  48 89 83 B8 00 00 00            mov qword ptr [rbx + 0xb8], rax
008B8DE2  48 8B 8F A8 00 00 00            mov rcx, qword ptr [rdi + 0xa8]
008B8DE9  49 03 CE                        add rcx, r14
008B8DEC  48 89 8B A8 00 00 00            mov qword ptr [rbx + 0xa8], rcx
008B8DF3  44 8B 8F 20 03 00 00            mov r9d, dword ptr [rdi + 0x320]
008B8DFA  45 85 C9                        test r9d, r9d
008B8DFD  74 18                           je 0x1408b8e17
008B8DFF  4C 8B 87 18 03 00 00            mov r8, qword ptr [rdi + 0x318]
008B8E06  48 8B CB                        mov rcx, rbx
008B8E09  48 8B 97 10 03 00 00            mov rdx, qword ptr [rdi + 0x310]
008B8E10  E8 DF 0C 11 00                  call 0x1409c9af4
008B8E15  8B F0                           mov esi, eax
008B8E17  85 F6                           test esi, esi
008B8E19  0F 88 ED FD FF FF               js 0x1408b8c0c
008B8E1F  48 8B 97 10 03 00 00            mov rdx, qword ptr [rdi + 0x310]
008B8E26  48 85 D2                        test rdx, rdx
008B8E29  74 10                           je 0x1408b8e3b
008B8E2B  48 8B CB                        mov rcx, rbx
008B8E2E  E8 85 7E 16 00                  call 0x140a20cb8
008B8E33  85 C0                           test eax, eax
008B8E35  0F 88 BE 00 00 00               js 0x1408b8ef9
008B8E3B  48 8B 8F 38 04 00 00            mov rcx, qword ptr [rdi + 0x438]
008B8E42  41 B8 0E 00 00 00               mov r8d, 0xe
008B8E48  45 8D 70 F3                     lea r14d, [r8 - 0xd]
008B8E4C  48 85 C9                        test rcx, rcx
008B8E4F  74 28                           je 0x1408b8e79
008B8E51  41 8B C6                        mov eax, r14d
008B8E54  F0 48 0F C1 41 18               lock xadd qword ptr [rcx + 0x18], rax
008B8E5A  49 03 C6                        add rax, r14
008B8E5D  49 3B C6                        cmp rax, r14
008B8E60  7F 05                           jg 0x1408b8e67
008B8E62  41 8B C8                        mov ecx, r8d
008B8E65  CD 29                           int 0x29
008B8E67  48 8B 5D F0                     mov rbx, qword ptr [rbp - 0x10]
008B8E6B  48 8B 87 38 04 00 00            mov rax, qword ptr [rdi + 0x438]
008B8E72  48 89 83 38 04 00 00            mov qword ptr [rbx + 0x438], rax
008B8E79  48 8B 8F 40 04 00 00            mov rcx, qword ptr [rdi + 0x440]
008B8E80  48 85 C9                        test rcx, rcx
008B8E83  74 28                           je 0x1408b8ead
008B8E85  49 8B C6                        mov rax, r14
008B8E88  F0 48 0F C1 41 18               lock xadd qword ptr [rcx + 0x18], rax
008B8E8E  49 03 C6                        add rax, r14
008B8E91  49 3B C6                        cmp rax, r14
008B8E94  7F 05                           jg 0x1408b8e9b
008B8E96  49 8B C8                        mov rcx, r8
008B8E99  CD 29                           int 0x29
008B8E9B  48 8B 5D F0                     mov rbx, qword ptr [rbp - 0x10]
008B8E9F  48 8B 87 40 04 00 00            mov rax, qword ptr [rdi + 0x440]
008B8EA6  48 89 83 40 04 00 00            mov qword ptr [rbx + 0x440], rax
008B8EAD  48 8B 97 80 04 00 00            mov rdx, qword ptr [rdi + 0x480]
008B8EB4  48 85 D2                        test rdx, rdx
008B8EB7  74 28                           je 0x1408b8ee1
008B8EB9  49 8B C6                        mov rax, r14
008B8EBC  F0 48 0F C1 42 18               lock xadd qword ptr [rdx + 0x18], rax
008B8EC2  49 03 C6                        add rax, r14
008B8EC5  49 3B C6                        cmp rax, r14
008B8EC8  7F 05                           jg 0x1408b8ecf
008B8ECA  49 8B C8                        mov rcx, r8
008B8ECD  CD 29                           int 0x29
008B8ECF  48 8B 5D F0                     mov rbx, qword ptr [rbp - 0x10]
008B8ED3  48 8B 87 80 04 00 00            mov rax, qword ptr [rdi + 0x480]
008B8EDA  48 89 83 80 04 00 00            mov qword ptr [rbx + 0x480], rax
008B8EE1  4C 39 AF 48 04 00 00            cmp qword ptr [rdi + 0x448], r13
008B8EE8  74 16                           je 0x1408b8f00
008B8EEA  48 8B D3                        mov rdx, rbx
008B8EED  48 8B CF                        mov rcx, rdi
008B8EF0  E8 D3 D3 1B 00                  call 0x140a762c8
008B8EF5  85 C0                           test eax, eax
008B8EF7  79 07                           jns 0x1408b8f00
008B8EF9  8B F0                           mov esi, eax
008B8EFB  E9 0C FD FF FF                  jmp 0x1408b8c0c
008B8F00  48 8B 97 50 04 00 00            mov rdx, qword ptr [rdi + 0x450]
008B8F07  48 8B CB                        mov rcx, rbx
008B8F0A  E8 A1 EA 12 00                  call 0x1409e79b0
008B8F0F  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B8F13  8B F0                           mov esi, eax
008B8F15  85 C0                           test eax, eax
008B8F17  0F 88 F3 FC FF FF               js 0x1408b8c10
008B8F1D  E8 EE 6A 9A FF                  call 0x14025fa10
008B8F22  E8 89 49 9A FF                  call 0x14025d8b0
008B8F27  44 39 2D E2 F0 71 00            cmp dword ptr [rip + 0x71f0e2], r13d
008B8F2E  0F 84 B4 00 00 00               je 0x1408b8fe8
008B8F34  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
008B8F3D  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
008B8F41  48 8B 88 78 04 00 00            mov rcx, qword ptr [rax + 0x478]
008B8F48  48 8B 82 08 05 00 00            mov rax, qword ptr [rdx + 0x508]
008B8F4F  48 89 01                        mov qword ptr [rcx], rax
008B8F52  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B8F5B  48 8B 55 F0                     mov rdx, qword ptr [rbp - 0x10]
008B8F5F  48 8B 80 10 05 00 00            mov rax, qword ptr [rax + 0x510]
008B8F66  48 8B 8A 78 04 00 00            mov rcx, qword ptr [rdx + 0x478]
008B8F6D  48 89 41 08                     mov qword ptr [rcx + 8], rax
008B8F71  48 8B 82 78 04 00 00            mov rax, qword ptr [rdx + 0x478]
008B8F78  C7 40 20 0D 00 00 00            mov dword ptr [rax + 0x20], 0xd
008B8F7F  48 8B 82 78 04 00 00            mov rax, qword ptr [rdx + 0x478]
008B8F86  44 89 A8 18 01 00 00            mov dword ptr [rax + 0x118], r13d
008B8F8D  48 8B 82 78 04 00 00            mov rax, qword ptr [rdx + 0x478]
008B8F94  44 89 A8 1C 01 00 00            mov dword ptr [rax + 0x11c], r13d
008B8F9B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B8FA4  48 8B 5D F0                     mov rbx, qword ptr [rbp - 0x10]
008B8FA8  48 8B 90 B8 00 00 00            mov rdx, qword ptr [rax + 0xb8]
008B8FAF  48 8B 8B 78 04 00 00            mov rcx, qword ptr [rbx + 0x478]
008B8FB6  F2 0F 10 82 38 03 00 00         movsd xmm0, qword ptr [rdx + 0x338]
008B8FBE  F2 0F 11 41 10                  movsd qword ptr [rcx + 0x10], xmm0
008B8FC3  8B 82 40 03 00 00               mov eax, dword ptr [rdx + 0x340]
008B8FC9  89 41 18                        mov dword ptr [rcx + 0x18], eax
008B8FCC  0F B7 82 44 03 00 00            movzx eax, word ptr [rdx + 0x344]
008B8FD3  66 89 41 1C                     mov word ptr [rcx + 0x1c], ax
008B8FD7  8A 82 46 03 00 00               mov al, byte ptr [rdx + 0x346]
008B8FDD  88 41 1E                        mov byte ptr [rcx + 0x1e], al
008B8FE0  48 8B CB                        mov rcx, rbx
008B8FE3  E8 F8 84 EE FF                  call 0x1407a14e0
008B8FE8  44 38 6D 40                     cmp byte ptr [rbp + 0x40], r13b
008B8FEC  74 08                           je 0x1408b8ff6
008B8FEE  48 8B CB                        mov rcx, rbx
008B8FF1  E8 22 EC 15 00                  call 0x140a17c18
008B8FF6  8B 53 7C                        mov edx, dword ptr [rbx + 0x7c]
008B8FF9  4C 8D 83 E8 00 00 00            lea r8, [rbx + 0xe8]
008B9000  48 8B 8B 98 00 00 00            mov rcx, qword ptr [rbx + 0x98]
008B9007  E8 94 DE B5 FF                  call 0x140416ea0
008B900C  8B 93 80 00 00 00               mov edx, dword ptr [rbx + 0x80]
008B9012  4C 8D 83 F8 01 00 00            lea r8, [rbx + 0x1f8]
008B9019  48 8B 8B A0 00 00 00            mov rcx, qword ptr [rbx + 0xa0]
008B9020  E8 7B DE B5 FF                  call 0x140416ea0
008B9025  48 8B 8B 18 03 00 00            mov rcx, qword ptr [rbx + 0x318]
008B902C  48 85 C9                        test rcx, rcx
008B902F  74 0E                           je 0x1408b903f
008B9031  8B 93 20 03 00 00               mov edx, dword ptr [rbx + 0x320]
008B9037  4D 8B C4                        mov r8, r12
008B903A  E8 61 DE B5 FF                  call 0x140416ea0
008B903F  44 39 2D CA EF 71 00            cmp dword ptr [rip + 0x71efca], r13d
008B9046  74 73                           je 0x1408b90bb
008B9048  83 3D 55 EB 5A 00 0D            cmp dword ptr [rip + 0x5aeb55], 0xd
008B904F  75 6A                           jne 0x1408b90bb
008B9051  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B905A  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
008B9061  48 8B 05 30 EB 5A 00            mov rax, qword ptr [rip + 0x5aeb30]
008B9068  48 39 81 D0 01 00 00            cmp qword ptr [rcx + 0x1d0], rax
008B906F  75 46                           jne 0x1408b90b7
008B9071  41 8B CE                        mov ecx, r14d
008B9074  F0 0F C1 0D 2C EB 5A 00         lock xadd dword ptr [rip + 0x5aeb2c], ecx
008B907C  48 8B 5D F0                     mov rbx, qword ptr [rbp - 0x10]
008B9080  41 03 CE                        add ecx, r14d
008B9083  48 8B 83 78 04 00 00            mov rax, qword ptr [rbx + 0x478]
008B908A  89 88 18 01 00 00               mov dword ptr [rax + 0x118], ecx
008B9090  48 8B 83 78 04 00 00            mov rax, qword ptr [rbx + 0x478]
008B9097  8B 90 18 01 00 00               mov edx, dword ptr [rax + 0x118]
008B909D  3B 15 FD EA 5A 00               cmp edx, dword ptr [rip + 0x5aeafd]
008B90A3  7C 16                           jl 0x1408b90bb
008B90A5  4C 8B C3                        mov r8, rbx
008B90A8  48 8D 0D 21 CD 24 00            lea rcx, [rip + 0x24cd21]
008B90AF  E8 FC FB A9 FF                  call 0x140358cb0
008B90B4  CC                              int3
008B90B5  EB 04                           jmp 0x1408b90bb
008B90B7  48 8B 5D F0                     mov rbx, qword ptr [rbp - 0x10]
008B90BB  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
008B90BF  48 89 18                        mov qword ptr [rax], rbx
008B90C2  E9 5B FB FF FF                  jmp 0x1408b8c22
008B90C7  33 D2                           xor edx, edx
008B90C9  48 8B CE                        mov rcx, rsi
008B90CC  E8 9F 97 2C 00                  call 0x140b82870
008B90D1  33 D2                           xor edx, edx
008B90D3  49 8B CF                        mov rcx, r15
008B90D6  E8 95 97 2C 00                  call 0x140b82870
008B90DB  83 3D 2E EF 71 00 00            cmp dword ptr [rip + 0x71ef2e], 0
008B90E2  74 0A                           je 0x1408b90ee
008B90E4  33 D2                           xor edx, edx
008B90E6  48 8B CB                        mov rcx, rbx
008B90E9  E8 82 97 2C 00                  call 0x140b82870
008B90EE  B8 95 00 00 C0                  mov eax, 0xc0000095
008B90F3  E9 E4 F7 FF FF                  jmp 0x1408b88dc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepDuplicateToken(__int64 a1, __int64 a2, unsigned __int8 a3, int a4, unsigned int a5, unsigned __int8 a6, unsigned __int8 a7, __int64 a8)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int8 v_stack_p18;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int8 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (96);
    v_r15 = 0;
    v_stack_m38 = 0;
    if (a4 != 2) goto loc_008B883C;
    if (((unsigned int)((unsigned int)(a5))) <= 3) goto loc_008B883C;
    goto loc_008B88DC;
loc_008B883C:
    result = ExAllocatePool2(256, 48, (unsigned int)(0x74416553ULL), a4);
    if (result == 0) goto loc_008B88D7;
    *(unsigned int *)(result) = 0;
    result = (result) + (8);
    *(unsigned int *)(result + 24) = 0;
    *(unsigned __int64 *)(result + 8) = result;
    *(unsigned __int64 *)(result) = result;
    *(unsigned __int64 *)(result + 32 + 8) = result + 32;
    *(unsigned __int64 *)(result + 32) = result + 32;
    if ((*(unsigned int *)(v_rip + 7468947)) == 0) goto loc_008B889F;
    result = ExAllocatePool2(288 - 32, 288, (unsigned int)(0x74416553ULL), a4);
    if (result != 0) goto loc_008B889F;
    goto loc_008B88D0;
loc_008B889F:
    result = ExAllocatePool2(104 - 40, 104, (unsigned int)(0x6C546553ULL), a4);
    if (result != 0) goto loc_008B88FB;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x6C546553ULL), a4);
    if ((*(unsigned int *)(v_rip + 7468869)) == ((unsigned int)(result))) goto loc_008B88D7;
loc_008B88D0:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(0x6C546553ULL), a4);
loc_008B88D7:
loc_008B88DC:
    return (unsigned int)(0xC000009AULL);
loc_008B88FB:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 132))) + (0x5C0ULL));
    if (((unsigned int)(a1)) < 0x5C0ULL) goto loc_008B90C7;
    v_stack_m20 = v_stack_m38;
    v_stack_m28 = (unsigned int)(a1);
    v_stack_m30 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 136)));
    v_stack_m38 = (unsigned int)(a1);
    result = ObCreateObjectEx(a6, *(unsigned __int64 *)(v_rip + 7468790), 0, a6);
    if (!sign_flag) goto loc_008B897F;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m28 + 56), a2, 0, a6);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, 0, a6);
    if ((*(unsigned int *)(v_rip + 7468709)) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_stack_m28 + 48);
        result = ExFreePoolWithTag(a1, a2, 0, a6);
    }
    goto loc_008B88DC;
loc_008B897F:
    result = (*(unsigned __int64 *)(v_rip - 9067646)) + (*(unsigned __int64 *)(v_rip - 9067646));
    *(unsigned int *)(v_stack_m38 + 16) = (unsigned int)(result);
    result = (result) >> (32);
    *(unsigned int *)(v_stack_m38 + 20) = (unsigned int)(result);
    *(unsigned __int8 *)(v_stack_m38 + 204) = 0;
    *(unsigned int *)(v_stack_m38 + 192) = (unsigned int)((unsigned int)(a4));
    *(unsigned int *)(v_stack_m38 + 196) = (unsigned int)((unsigned int)(a5));
    *(unsigned __int64 *)(v_stack_m38 + 48) = result;
    result = ExInitializeResourceLite(result, v_stack_m38, 0, a6);
    v_r13 = 0;
    *(unsigned __int64 *)(v_stack_m38 + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 24);
    *(unsigned __int64 *)(v_stack_m38) = v_xmm0;
    *(unsigned int *)(v_stack_m38 + 140) = 0;
    *(unsigned __int64 *)(v_stack_m38 + 32) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 32);
    *(unsigned __int64 *)(v_stack_m38 + 40) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 40);
    *(unsigned __int64 *)(v_stack_m38 + 224) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 224);
    *(unsigned __int64 *)(v_stack_m38 + 1120) = 0;
    *(unsigned __int64 *)(v_stack_m38 + 1128) = 0;
    *(unsigned __int64 *)(v_stack_m38 + 1096) = 0;
    *(unsigned __int64 *)(v_stack_m38 + 1144) = *(unsigned __int64 *)(v_stack_m28 + 48);
    *(unsigned int *)(v_stack_m38 + 120) = 0;
    *(unsigned __int64 *)(v_stack_m38 + 1160) = 0;
    if ((*(unsigned int *)(v_rip + 7468513)) == 0) goto loc_008B8A6A;
    a3 = 0;
    result = RtlWalkFrameChain(*(unsigned __int64 *)(v_stack_m28 + 48) + 40, (unsigned int)((unsigned int)(v_r13 + 30)), a3, a6);
    v_rbx = v_r13 + 30;
    if (((unsigned __int8)(v_cr8)) < 2) {
        v_rbx = (unsigned int)((v_r13 + 30) - ((unsigned int)(result)));
        a1 = (unsigned int)(result);
        result = *(unsigned __int64 *)(v_stack_m38 + 1144);
        a3 = v_r13 + 1;
        result = (result) + (40);
        a2 = (unsigned int)(v_rbx);
        a1 = result + a1 * 8;
        result = RtlWalkFrameChain(a1, a2, a3, a6);
    }
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 48), 1, a3, a6);
    *(unsigned __int64 *)(v_stack_m38 + 56) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 56);
    *(unsigned int *)(v_stack_m38 + 136) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 136)));
    *(unsigned int *)(v_stack_m38 + 144) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 144)));
    *(unsigned int *)(v_stack_m38 + 128) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 128)));
    *(unsigned int *)(v_stack_m38 + 132) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 132)));
    result = Feature_2045735225__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 48), 1, a3, a6);
    if ((unsigned int)(result) == 0) goto loc_008B8AD9;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 200))) & (0xEFFFFBDFULL));
    goto loc_008B8ADF;
loc_008B8AD9:
    a1 = (unsigned int)((a1) & (0xFFFFFBDFULL));
loc_008B8ADF:
    *(unsigned int *)(v_stack_m38 + 200) = (unsigned int)(a1);
    v_rbx = v_stack_m38;
    if (!(condition_is_above_or_equal)) {
        v_rbx = v_stack_m38;
    }
    a4 = 0;
    a3 = 0;
    v_stack_m40 = 0;
    result = SepSetTokenSessionById(v_rbx, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 120)), a3, a4);
    *(unsigned int *)(v_stack_m38 + 120) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 120)));
    *(unsigned __int64 *)(v_rbx + 88) = v_xmm0;
    *(unsigned __int64 *)(v_rbx + 104) = v_xmm1;
    *(unsigned int *)(v_rbx + 208) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 208)));
    *(unsigned int *)(v_rbx + 212) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 212)));
    *(unsigned __int64 *)(v_rbx + 64) = v_xmm0;
    *(unsigned __int64 *)(v_rbx + 80) = v_xmm1;
    result = Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline(v_rbx, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 120)), a3, a4);
    if ((unsigned int)(result) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 1168);
        *(unsigned __int64 *)(v_rbx + 1168) = result;
    }
    result = Feature_AgentId2__private_IsEnabledDeviceUsageNoInline(v_rbx, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 120)), a3, a4);
    if ((unsigned int)(result) != 0) {
        result = *(unsigned int *)(v_rbx + 1168);
        a1 = (unsigned int)(result);
        a1 = (unsigned int)((a1) ^ (*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 1168)));
        a1 = (unsigned int)((a1) & (2));
        a1 = (unsigned int)((a1) ^ ((unsigned int)(result)));
        *(unsigned int *)(v_rbx + 1168) = (unsigned int)(a1);
    }
    *(unsigned __int64 *)(v_rbx + 776) = *(unsigned __int64 *)(v_stack_m28 + 56);
    *(unsigned __int64 *)(v_rbx + 1080) = 0;
    a2 = 0;
    *(unsigned __int64 *)(v_rbx + 1088) = 0;
    *(unsigned __int64 *)(v_rbx + 1152) = 0;
    *(unsigned __int64 *)(v_rbx + 792) = 0;
    *(unsigned __int64 *)(v_rbx + 784) = 0;
    *(unsigned int *)(v_rbx + 800) = 0;
    result = memset(v_rbx + 808, a2, 272, a4);
    *(unsigned __int64 *)(v_rbx + 176) = 0;
    *(unsigned __int64 *)(v_rbx + 1104) = 0;
    *(unsigned __int64 *)(v_rbx + 1112) = 0;
    *(unsigned __int64 *)(v_rbx + 1136) = 0;
    if ((*(unsigned __int8 *)(v_rbx + 119)) == 2) {
        a2 = 1;
        a1 = v_rbx + 88;
        result = SepModifyTokenPolicyCounter(a1, a2, 272, a4);
    }
    result = SepDuplicateLogonSessionReference(v_rbx, *(unsigned __int64 *)(v_stack_m28 + 72), 272, a4);
    if (!sign_flag) goto loc_008B8C29;
loc_008B8C0C:
loc_008B8C10:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 48), *(unsigned __int64 *)(v_stack_m28 + 72), 272, a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 48), *(unsigned __int64 *)(v_stack_m28 + 72), 272, a4);
    result = ObfDereferenceObject(v_rbx, *(unsigned __int64 *)(v_stack_m28 + 72), 272, a4);
loc_008B8C22:
    goto loc_008B88DC;
loc_008B8C29:
    result = Feature_2045735225__private_IsEnabledDeviceUsageNoInline(v_rbx, *(unsigned __int64 *)(v_stack_m28 + 72), 272, a4);
    if ((unsigned int)(result) == 0) goto loc_008B8C66;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 200)) & ((unsigned int)((unsigned int)(0x10000000ULL)))) == 0) goto loc_008B8C66;
    a1 = (*(unsigned __int64 *)(v_rbx + 216)) + (16);
    v_stack_m30 = 0;
    result = SepReferenceLogonSession(a1, v_stack_m30, 272, a4);
    if (sign_flag) goto loc_008B8C0C;
loc_008B8C66:
    a2 = 0;
    result = SepRefDerefLuidToIndexEntryIfNecessary(*(unsigned __int64 *)(v_stack_m28 + 72), a2, 272, a4);
    *(unsigned __int64 *)(v_rbx + 1136) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 1136);
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 776))) == 0) goto loc_008B8CA4;
    result = AuthzBasepDuplicateSecurityAttributes(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 776), *(unsigned __int64 *)(v_rbx + 776), a7, a4);
    if (sign_flag) goto loc_008B8C0C;
loc_008B8CA4:
    result = memcpy(v_rbx + 1472, *(unsigned __int64 *)(v_stack_m28 + 72) + 1472, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 132)), a4);
    v_r15 = (unsigned int)((result) | (0xFFFFFFFFULL));
    v_r14 = (v_rbx) - (*(unsigned __int64 *)(v_stack_m28 + 72));
    if ((*(unsigned __int8 *)(v_rip + 5959457)) == 0) goto loc_008B8CFF;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 152)) + (v_r14);
    *(unsigned __int64 *)(v_rbx + 152) = a1;
    result = SepDuplicateTokenUserAndGroups(*(unsigned __int64 *)(v_stack_m28 + 72), v_rbx, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 132)), a4);
    if (!sign_flag) goto loc_008B8D29;
    *(unsigned __int64 *)(v_rbx + 152) = 0;
    goto loc_008B8C0C;
loc_008B8CFF:
    *(unsigned int *)(v_rbx + 124) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 124)));
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 152)) + (v_r14);
    *(unsigned __int64 *)(v_rbx + 152) = a1;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 124))) == 0) goto loc_008B8D29;
loc_008B8D1D:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 124))) + ((unsigned int)(v_r15)));
    if (condition_is_not_equal) goto loc_008B8D1D;
loc_008B8D29:
    *(unsigned __int64 *)(v_rbx + 160) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 160);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 160) == 0) goto loc_008B8D5C;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 160)) + (v_r14);
    *(unsigned __int64 *)(v_rbx + 160) = result;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 128))) == 0) goto loc_008B8D5C;
loc_008B8D50:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 128))) + ((unsigned int)(v_r15)));
    if (condition_is_not_equal) goto loc_008B8D50;
loc_008B8D5C:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 184);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 184) != 0) {
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 184) + 2);
        a2 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 168) + 1) * 4 + 8) + ((unsigned int)(result)));
    }
    result = ExAllocatePool2(256, a2, (unsigned int)(0x64546553ULL), a4);
    *(unsigned __int64 *)(v_rbx + 176) = result;
    if (result != 0) goto loc_008B8DAC;
    goto loc_008B8C0C;
loc_008B8DAC:
    result = memcpy(result, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 176), (unsigned int)((unsigned int)(a2)), a4);
    v_r14 = (result) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 176));
    *(unsigned __int64 *)(v_rbx + 184) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 184);
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 184);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 184) != 0) {
        result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 184)) + (v_r14);
        *(unsigned __int64 *)(v_rbx + 184) = result;
    }
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 168)) + (v_r14);
    *(unsigned __int64 *)(v_rbx + 168) = a1;
    v_rsi = (unsigned int)(0xC000009AULL);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 800))) != 0) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 792);
        a1 = v_rbx;
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 784);
        result = SepSetTokenCapabilities(a1, a2, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 800)));
        v_rsi = (unsigned int)(result);
    }
    if (sign_flag) goto loc_008B8C0C;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 784) == 0) goto loc_008B8E3B;
    result = SepSetTokenPackage(v_rbx, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 784), a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 800)));
    if (sign_flag) goto loc_008B8EF9;
loc_008B8E3B:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 1080) == 0) goto loc_008B8E79;
    result = ((unsigned int)((unsigned int)(14 - 13))) + (14 - 13);
    if (result <= (14 - 13)) {
        a1 = 14;
    }
    *(unsigned __int64 *)(v_stack_m38 + 1080) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 1080);
loc_008B8E79:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 1088) == 0) goto loc_008B8EAD;
    result = (14 - 13) + (14 - 13);
    if (result <= (14 - 13)) {
        a1 = 14;
    }
    *(unsigned __int64 *)(v_stack_m38 + 1088) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 1088);
loc_008B8EAD:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 1152) == 0) goto loc_008B8EE1;
    result = (14 - 13) + (14 - 13);
    if (result <= (14 - 13)) {
        a1 = 14;
    }
    *(unsigned __int64 *)(v_stack_m38 + 1152) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 1152);
loc_008B8EE1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 1096)) == 0) goto loc_008B8F00;
    result = SepDuplicateTokenClaims(*(unsigned __int64 *)(v_stack_m28 + 72), v_stack_m38, 14, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 800)));
    if (!sign_flag) goto loc_008B8F00;
loc_008B8EF9:
    goto loc_008B8C0C;
loc_008B8F00:
    result = SepSetTokenTrust(v_stack_m38, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 1104), 14, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 800)));
    if (sign_flag) goto loc_008B8C10;
    result = ExReleaseResourceLite(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 1104), 14, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 800)));
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 1104), 14, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 800)));
    v_rbx = v_stack_m38;
    if ((*(unsigned int *)(v_rip + 7467234)) != 0) {
        a2 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = v_stack_m38;
        a1 = *(unsigned __int64 *)(result + 1144);
        result = *(unsigned __int64 *)(a2 + 1288);
        *(unsigned __int64 *)(a1) = result;
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = v_stack_m38;
        result = *(unsigned __int64 *)(result + 1296);
        a1 = *(unsigned __int64 *)(a2 + 1144);
        *(unsigned __int64 *)(a1 + 8) = result;
        result = *(unsigned __int64 *)(a2 + 1144);
        *(unsigned int *)(result + 32) = 13;
        result = *(unsigned __int64 *)(a2 + 1144);
        *(unsigned int *)(result + 280) = 0;
        result = *(unsigned __int64 *)(a2 + 1144);
        *(unsigned int *)(result + 284) = 0;
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        v_rbx = v_stack_m38;
        a2 = *(unsigned __int64 *)(result + 184);
        a1 = *(unsigned __int64 *)(v_rbx + 1144);
        *(unsigned __int64 *)(a1 + 16) = v_xmm0;
        result = *(unsigned int *)(a2 + 832);
        *(unsigned int *)(a1 + 24) = (unsigned int)(result);
        result = *(unsigned __int16 *)(a2 + 836);
        *(unsigned __int16 *)(a1 + 28) = (unsigned __int16)(result);
        result = *(unsigned __int8 *)(a2 + 838);
        *(unsigned __int8 *)(a1 + 30) = (unsigned __int8)(result);
        a1 = v_rbx;
        result = SepAddTokenLogonSession(a1, a2, 14, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 800)));
    }
    if (v_stack_p18 != 0) {
        a1 = v_rbx;
        result = SepMakeTokenEffectiveOnly(a1, a2, 14, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 800)));
    }
    result = RtlSidHashInitialize(*(unsigned __int64 *)(v_rbx + 152), (unsigned int)(*(unsigned int *)(v_rbx + 124)), v_rbx + 232, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 800)));
    result = RtlSidHashInitialize(*(unsigned __int64 *)(v_rbx + 160), (unsigned int)(*(unsigned int *)(v_rbx + 128)), v_rbx + 504, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 800)));
    if (*(unsigned __int64 *)(v_rbx + 792) != 0) {
        a2 = *(unsigned int *)(v_rbx + 800);
        a3 = v_rbx + 808;
        result = RtlSidHashInitialize(*(unsigned __int64 *)(v_rbx + 792), a2, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 800)));
    }
    if ((*(unsigned int *)(v_rip + 7466954)) == 0) goto loc_008B90BB;
    if ((*(unsigned int *)(v_rip + 5958485)) != 13) goto loc_008B90BB;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 464)) != (*(unsigned __int64 *)(v_rip + 5958448))) goto loc_008B90B7;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(14 - 13))) + ((unsigned int)(14 - 13)));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m38 + 1144) + 280) = (unsigned int)(a1);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m38 + 1144) + 280)))) < (*(unsigned int *)(v_rip + 5958397))) goto loc_008B90BB;
    result = DbgPrint(v_rip + 2411809, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m38 + 1144) + 280)), v_stack_m38, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 800)));
    goto loc_008B90BB;
loc_008B90B7:
loc_008B90BB:
    *(unsigned __int64 *)(a8) = v_stack_m38;
    goto loc_008B8C22;
loc_008B90C7:
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)((unsigned int)(result)), a2, v_stack_m38, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 800)));
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)((unsigned int)(a2)), a2, v_stack_m38, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 800)));
    if ((*(unsigned int *)(v_rip + 7466798)) != 0) {
        a2 = 0;
        a1 = v_stack_m38;
        result = ExFreePoolWithTag(a1, a2, v_stack_m38, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 800)));
    }
    goto loc_008B88DC;
}
```

## 5. (Beta) C Style

```c
int64_t SepDuplicateToken(void *Arg1, int64_t Arg2, uint8_t Arg3, int32_t Arg4, uint32_t Arg5, uint8_t Arg6, uint8_t Arg7, void *Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint8_t v_stack_p18;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint8_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (96);
    local_r15 = 0;
    v_stack_m38 = 0;
    if (Arg4 != 2) goto loc_008B883C;
    if (((uint32_t)((uint32_t)(Arg5))) <= 3) goto loc_008B883C;
    goto loc_008B88DC;
loc_008B883C:
    result = ExAllocatePool2(256, 48, (uint32_t)(0x74416553ULL), Arg4);
    if (result == 0) goto loc_008B88D7;
    *(uint32_t *)(result) = 0;
    result = (result) + (8);
    *(uint32_t *)(result + 0x18) = 0;
    *(uint64_t *)(result + 0x8) = result;
    *(uint64_t *)(result) = result;
    *(uint64_t *)(result + 0x20 + 0x8) = result + 32;
    *(uint64_t *)(result + 0x20) = result + 32;
    if ((*(uint32_t *)(v_rip + 0x71F793)) == 0) goto loc_008B889F;
    result = ExAllocatePool2(288 - 32, 288, (uint32_t)(0x74416553ULL), Arg4);
    if (result != 0) goto loc_008B889F;
    goto loc_008B88D0;
loc_008B889F:
    result = ExAllocatePool2(104 - 40, 104, (uint32_t)(0x6C546553ULL), Arg4);
    if (result != 0) goto loc_008B88FB;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x6C546553ULL), Arg4);
    if ((*(uint32_t *)(v_rip + 0x71F745)) == ((uint32_t)(result))) goto loc_008B88D7;
loc_008B88D0:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(0x6C546553ULL), Arg4);
loc_008B88D7:
loc_008B88DC:
    return (uint32_t)(0xC000009AULL);
loc_008B88FB:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x84))) + (0x5C0ULL));
    if (((uint32_t)(Arg1)) < 0x5C0ULL) goto loc_008B90C7;
    v_stack_m20 = v_stack_m38;
    v_stack_m28 = (uint32_t)(Arg1);
    v_stack_m30 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x88)));
    v_stack_m38 = (uint32_t)(Arg1);
    result = ObCreateObjectEx(Arg6, *(uint64_t *)(v_rip + 0x71F6F6), 0, Arg6);
    if (!sign_flag) goto loc_008B897F;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m28 + 0x38), Arg2, 0, Arg6);
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, 0, Arg6);
    if ((*(uint32_t *)(v_rip + 0x71F6A5)) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(v_stack_m28 + 0x30);
        result = ExFreePoolWithTag(Arg1, Arg2, 0, Arg6);
    }
    goto loc_008B88DC;
loc_008B897F:
    result = (*(uint64_t *)(v_rip - 0x8A5C7E)) + (*(uint64_t *)(v_rip - 0x8A5C7E));
    *(uint32_t *)(v_stack_m38 + 0x10) = (uint32_t)(result);
    result = (result) >> (32);
    *(uint32_t *)(v_stack_m38 + 0x14) = (uint32_t)(result);
    *(uint8_t *)(v_stack_m38 + 0xCC) = 0;
    *(uint32_t *)(v_stack_m38 + 0xC0) = (uint32_t)((uint32_t)(Arg4));
    *(uint32_t *)(v_stack_m38 + 0xC4) = (uint32_t)((uint32_t)(Arg5));
    *(uint64_t *)(v_stack_m38 + 0x30) = result;
    result = ExInitializeResourceLite(result, v_stack_m38, 0, Arg6);
    local_r13 = 0;
    *(uint64_t *)(v_stack_m38 + 0x18) = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x18);
    *(uint64_t *)(v_stack_m38) = v_xmm0;
    *(uint32_t *)(v_stack_m38 + 0x8C) = 0;
    *(uint64_t *)(v_stack_m38 + 0x20) = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x20);
    *(uint64_t *)(v_stack_m38 + 0x28) = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x28);
    *(uint64_t *)(v_stack_m38 + 0xE0) = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xE0);
    *(uint64_t *)(v_stack_m38 + 0x460) = 0;
    *(uint64_t *)(v_stack_m38 + 0x468) = 0;
    *(uint64_t *)(v_stack_m38 + 0x448) = 0;
    *(uint64_t *)(v_stack_m38 + 0x478) = *(uint64_t *)(v_stack_m28 + 0x30);
    *(uint32_t *)(v_stack_m38 + 0x78) = 0;
    *(uint64_t *)(v_stack_m38 + 0x488) = 0;
    if ((*(uint32_t *)(v_rip + 0x71F5E1)) == 0) goto loc_008B8A6A;
    Arg3 = 0;
    result = RtlWalkFrameChain(*(uint64_t *)(v_stack_m28 + 0x30) + 40, (uint32_t)((uint32_t)(local_r13 + 30)), Arg3, Arg6);
    local_rbx = local_r13 + 30;
    if (((uint8_t)(v_cr8)) < 2) {
        local_rbx = (uint32_t)((local_r13 + 30) - ((uint32_t)(result)));
        Arg1 = (uint32_t)(result);
        result = *(uint64_t *)(v_stack_m38 + 0x478);
        Arg3 = local_r13 + 1;
        result = (result) + (40);
        Arg2 = (uint32_t)(local_rbx);
        Arg1 = result + Arg1 * 8;
        result = RtlWalkFrameChain(Arg1, Arg2, Arg3, Arg6);
    }
    result = ExAcquireResourceSharedLite(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x30), 1, Arg3, Arg6);
    *(uint64_t *)(v_stack_m38 + 0x38) = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x38);
    *(uint32_t *)(v_stack_m38 + 0x88) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x88)));
    *(uint32_t *)(v_stack_m38 + 0x90) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x90)));
    *(uint32_t *)(v_stack_m38 + 0x80) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x80)));
    *(uint32_t *)(v_stack_m38 + 0x84) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x84)));
    result = Feature_2045735225__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x30), 1, Arg3, Arg6);
    if ((uint32_t)(result) == 0) goto loc_008B8AD9;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xC8))) & (0xEFFFFBDFULL));
    goto loc_008B8ADF;
loc_008B8AD9:
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFBDFULL));
loc_008B8ADF:
    *(uint32_t *)(v_stack_m38 + 0xC8) = (uint32_t)(Arg1);
    local_rbx = v_stack_m38;
    if (!(condition_is_above_or_equal)) {
        local_rbx = v_stack_m38;
    }
    Arg4 = 0;
    Arg3 = 0;
    v_stack_m40 = 0;
    result = SepSetTokenSessionById(local_rbx, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x78)), Arg3, Arg4);
    *(uint32_t *)(v_stack_m38 + 0x78) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x78)));
    *(uint64_t *)(local_rbx + 0x58) = v_xmm0;
    *(uint64_t *)(local_rbx + 0x68) = v_xmm1;
    *(uint32_t *)(local_rbx + 0xD0) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xD0)));
    *(uint32_t *)(local_rbx + 0xD4) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xD4)));
    *(uint64_t *)(local_rbx + 0x40) = v_xmm0;
    *(uint64_t *)(local_rbx + 0x50) = v_xmm1;
    result = Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline(local_rbx, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x78)), Arg3, Arg4);
    if ((uint32_t)(result) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x490);
        *(uint64_t *)(local_rbx + 0x490) = result;
    }
    result = Feature_AgentId2__private_IsEnabledDeviceUsageNoInline(local_rbx, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x78)), Arg3, Arg4);
    if ((uint32_t)(result) != 0) {
        result = *(uint32_t *)(local_rbx + 0x490);
        Arg1 = (uint32_t)(result);
        Arg1 = (uint32_t)((Arg1) ^ (*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x490)));
        Arg1 = (uint32_t)((Arg1) & (2));
        Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(result)));
        *(uint32_t *)(local_rbx + 0x490) = (uint32_t)(Arg1);
    }
    *(uint64_t *)(local_rbx + 0x308) = *(uint64_t *)(v_stack_m28 + 0x38);
    *(uint64_t *)(local_rbx + 0x438) = 0;
    Arg2 = 0;
    *(uint64_t *)(local_rbx + 0x440) = 0;
    *(uint64_t *)(local_rbx + 0x480) = 0;
    *(uint64_t *)(local_rbx + 0x318) = 0;
    *(uint64_t *)(local_rbx + 0x310) = 0;
    *(uint32_t *)(local_rbx + 0x320) = 0;
    result = memset(local_rbx + 808, Arg2, 272, Arg4);
    *(uint64_t *)(local_rbx + 0xB0) = 0;
    *(uint64_t *)(local_rbx + 0x450) = 0;
    *(uint64_t *)(local_rbx + 0x458) = 0;
    *(uint64_t *)(local_rbx + 0x470) = 0;
    if ((*(uint8_t *)(local_rbx + 0x77)) == 2) {
        Arg2 = 1;
        Arg1 = local_rbx + 88;
        result = SepModifyTokenPolicyCounter(Arg1, Arg2, 272, Arg4);
    }
    result = SepDuplicateLogonSessionReference(local_rbx, *(uint64_t *)(v_stack_m28 + 0x48), 272, Arg4);
    if (!sign_flag) goto loc_008B8C29;
loc_008B8C0C:
loc_008B8C10:
    result = ExReleaseResourceLite(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x30), *(uint64_t *)(v_stack_m28 + 0x48), 272, Arg4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x30), *(uint64_t *)(v_stack_m28 + 0x48), 272, Arg4);
    result = ObfDereferenceObject(local_rbx, *(uint64_t *)(v_stack_m28 + 0x48), 272, Arg4);
loc_008B8C22:
    goto loc_008B88DC;
loc_008B8C29:
    result = Feature_2045735225__private_IsEnabledDeviceUsageNoInline(local_rbx, *(uint64_t *)(v_stack_m28 + 0x48), 272, Arg4);
    if ((uint32_t)(result) == 0) goto loc_008B8C66;
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xC8)) & ((uint32_t)((uint32_t)(0x10000000ULL)))) == 0) goto loc_008B8C66;
    Arg1 = (*(uint64_t *)(local_rbx + 0xD8)) + (16);
    v_stack_m30 = 0;
    result = SepReferenceLogonSession(Arg1, v_stack_m30, 272, Arg4);
    if (sign_flag) goto loc_008B8C0C;
loc_008B8C66:
    Arg2 = 0;
    result = SepRefDerefLuidToIndexEntryIfNecessary(*(uint64_t *)(v_stack_m28 + 0x48), Arg2, 272, Arg4);
    *(uint64_t *)(local_rbx + 0x470) = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x470);
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x308))) == 0) goto loc_008B8CA4;
    result = AuthzBasepDuplicateSecurityAttributes(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x308), *(uint64_t *)(local_rbx + 0x308), Arg7, Arg4);
    if (sign_flag) goto loc_008B8C0C;
loc_008B8CA4:
    result = memcpy(local_rbx + 1472, *(uint64_t *)(v_stack_m28 + 0x48) + 1472, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x84)), Arg4);
    local_r15 = (uint32_t)((result) | (0xFFFFFFFFULL));
    local_r14 = (local_rbx) - (*(uint64_t *)(v_stack_m28 + 0x48));
    if ((*(uint8_t *)(v_rip + 0x5AEF21)) == 0) goto loc_008B8CFF;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x98)) + (local_r14);
    *(void **)(local_rbx + 0x98) = Arg1;
    result = SepDuplicateTokenUserAndGroups(*(uint64_t *)(v_stack_m28 + 0x48), local_rbx, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x84)), Arg4);
    if (!sign_flag) goto loc_008B8D29;
    *(uint64_t *)(local_rbx + 0x98) = 0;
    goto loc_008B8C0C;
loc_008B8CFF:
    *(uint32_t *)(local_rbx + 0x7C) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x7C)));
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x98)) + (local_r14);
    *(void **)(local_rbx + 0x98) = Arg1;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x7C))) == 0) goto loc_008B8D29;
loc_008B8D1D:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x7C))) + ((uint32_t)(local_r15)));
    if (condition_is_not_equal) goto loc_008B8D1D;
loc_008B8D29:
    *(uint64_t *)(local_rbx + 0xA0) = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xA0);
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xA0) == 0) goto loc_008B8D5C;
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xA0)) + (local_r14);
    *(uint64_t *)(local_rbx + 0xA0) = result;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x80))) == 0) goto loc_008B8D5C;
loc_008B8D50:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x80))) + ((uint32_t)(local_r15)));
    if (condition_is_not_equal) goto loc_008B8D50;
loc_008B8D5C:
    result = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xB8);
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xB8) != 0) {
        result = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xB8) + 0x2);
        Arg2 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xA8) + 0x1) * 4 + 8) + ((uint32_t)(result)));
    }
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x64546553ULL), Arg4);
    *(uint64_t *)(local_rbx + 0xB0) = result;
    if (result != 0) goto loc_008B8DAC;
    goto loc_008B8C0C;
loc_008B8DAC:
    result = memcpy(result, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xB0), (uint32_t)((uint32_t)(Arg2)), Arg4);
    local_r14 = (result) - (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xB0));
    *(uint64_t *)(local_rbx + 0xB8) = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xB8);
    result = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xB8);
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xB8) != 0) {
        result = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xB8)) + (local_r14);
        *(uint64_t *)(local_rbx + 0xB8) = result;
    }
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xA8)) + (local_r14);
    *(void **)(local_rbx + 0xA8) = Arg1;
    local_rsi = (uint32_t)(0xC000009AULL);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x320))) != 0) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x318);
        Arg1 = local_rbx;
        Arg2 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x310);
        result = SepSetTokenCapabilities(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x320)));
        local_rsi = (uint32_t)(result);
    }
    if (sign_flag) goto loc_008B8C0C;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x310) == 0) goto loc_008B8E3B;
    result = SepSetTokenPackage(local_rbx, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x310), Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x320)));
    if (sign_flag) goto loc_008B8EF9;
loc_008B8E3B:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x438) == 0) goto loc_008B8E79;
    result = ((uint32_t)((uint32_t)(14 - 13))) + (14 - 13);
    if (result <= (14 - 13)) {
        Arg1 = 14;
    }
    *(uint64_t *)(v_stack_m38 + 0x438) = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x438);
loc_008B8E79:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x440) == 0) goto loc_008B8EAD;
    result = (14 - 13) + (14 - 13);
    if (result <= (14 - 13)) {
        Arg1 = 14;
    }
    *(uint64_t *)(v_stack_m38 + 0x440) = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x440);
loc_008B8EAD:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x480) == 0) goto loc_008B8EE1;
    result = (14 - 13) + (14 - 13);
    if (result <= (14 - 13)) {
        Arg1 = 14;
    }
    *(uint64_t *)(v_stack_m38 + 0x480) = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x480);
loc_008B8EE1:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x448)) == 0) goto loc_008B8F00;
    result = SepDuplicateTokenClaims(*(uint64_t *)(v_stack_m28 + 0x48), v_stack_m38, 14, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x320)));
    if (!sign_flag) goto loc_008B8F00;
loc_008B8EF9:
    goto loc_008B8C0C;
loc_008B8F00:
    result = SepSetTokenTrust(v_stack_m38, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x450), 14, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x320)));
    if (sign_flag) goto loc_008B8C10;
    result = ExReleaseResourceLite(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x30), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x450), 14, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x320)));
    result = KeLeaveCriticalRegion(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x30), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x450), 14, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x320)));
    local_rbx = v_stack_m38;
    if ((*(uint32_t *)(v_rip + 0x71F0E2)) != 0) {
        Arg2 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = v_stack_m38;
        Arg1 = *(uint64_t *)(result + 0x478);
        result = *(uint64_t *)(Arg2 + 0x508);
        *(uint64_t *)(arg1) = result;
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg2 = v_stack_m38;
        result = *(uint64_t *)(result + 0x510);
        Arg1 = *(uint64_t *)(Arg2 + 0x478);
        *(uint64_t *)(arg1 + 0x8) = result;
        result = *(uint64_t *)(Arg2 + 0x478);
        *(uint32_t *)(result + 0x20) = 13;
        result = *(uint64_t *)(Arg2 + 0x478);
        *(uint32_t *)(result + 0x118) = 0;
        result = *(uint64_t *)(Arg2 + 0x478);
        *(uint32_t *)(result + 0x11C) = 0;
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        local_rbx = v_stack_m38;
        Arg2 = *(uint64_t *)(result + 0xB8);
        Arg1 = *(uint64_t *)(local_rbx + 0x478);
        *(uint64_t *)(arg1 + 0x10) = v_xmm0;
        result = *(uint32_t *)(Arg2 + 0x340);
        *(uint32_t *)(arg1 + 0x18) = (uint32_t)(result);
        result = *(uint16_t *)(Arg2 + 0x344);
        *(uint16_t *)(arg1 + 0x1C) = (uint16_t)(result);
        result = *(uint8_t *)(Arg2 + 0x346);
        *(uint8_t *)(arg1 + 0x1E) = (uint8_t)(result);
        Arg1 = local_rbx;
        result = SepAddTokenLogonSession(Arg1, Arg2, 14, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x320)));
    }
    if (v_stack_p18 != 0) {
        Arg1 = local_rbx;
        result = SepMakeTokenEffectiveOnly(Arg1, Arg2, 14, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x320)));
    }
    result = RtlSidHashInitialize(*(uint64_t *)(local_rbx + 0x98), (uint32_t)(*(uint32_t *)(local_rbx + 0x7C)), local_rbx + 232, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x320)));
    result = RtlSidHashInitialize(*(uint64_t *)(local_rbx + 0xA0), (uint32_t)(*(uint32_t *)(local_rbx + 0x80)), local_rbx + 504, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x320)));
    if (*(uint64_t *)(local_rbx + 0x318) != 0) {
        Arg2 = *(uint32_t *)(local_rbx + 0x320);
        Arg3 = local_rbx + 808;
        result = RtlSidHashInitialize(*(uint64_t *)(local_rbx + 0x318), Arg2, Arg3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x320)));
    }
    if ((*(uint32_t *)(v_rip + 0x71EFCA)) == 0) goto loc_008B90BB;
    if ((*(uint32_t *)(v_rip + 0x5AEB55)) != 13) goto loc_008B90BB;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1D0)) != (*(uint64_t *)(v_rip + 0x5AEB30))) goto loc_008B90B7;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(14 - 13))) + ((uint32_t)(14 - 13)));
    *(uint32_t *)(*(uint64_t *)(v_stack_m38 + 0x478) + 0x118) = (uint32_t)(Arg1);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m38 + 0x478) + 0x118)))) < (*(uint32_t *)(v_rip + 0x5AEAFD))) goto loc_008B90BB;
    result = DbgPrint(v_rip + 2411809, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m38 + 0x478) + 0x118)), v_stack_m38, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x320)));
    goto loc_008B90BB;
loc_008B90B7:
loc_008B90BB:
    *(uint64_t *)(arg8) = v_stack_m38;
    goto loc_008B8C22;
loc_008B90C7:
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)((uint32_t)(result)), Arg2, v_stack_m38, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x320)));
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)((uint32_t)(Arg2)), Arg2, v_stack_m38, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x320)));
    if ((*(uint32_t *)(v_rip + 0x71EF2E)) != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m38;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m38, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x320)));
    }
    goto loc_008B88DC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
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
| `Arg1` | `+ 0xA8` | `64` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg1` | `+ 0xC8` | `32` | `R` |
| `Arg1` | `+ 0xD0` | `32` | `R` |
| `Arg1` | `+ 0xD4` | `32` | `R` |
| `Arg1` | `+ 0xE0` | `64` | `R` |
| `Arg1` | `+ 0x308` | `64` | `R` |
| `Arg1` | `+ 0x310` | `64` | `R` |
| `Arg1` | `+ 0x318` | `64` | `R` |
| `Arg1` | `+ 0x320` | `32` | `R` |
| `Arg1` | `+ 0x438` | `64` | `R` |
| `Arg1` | `+ 0x440` | `64` | `R` |
| `Arg1` | `+ 0x448` | `64` | `R` |

추가 오프셋 7개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008B87EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
