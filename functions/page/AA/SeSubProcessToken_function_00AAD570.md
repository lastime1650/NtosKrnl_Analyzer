# SeSubProcessToken

- RVA: `0x00AAD570`–`0x00AADE4D` (길이 `2,269` bytes)
- VA: `0x0000000140AAD570`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BC10C`
- 디코드: `579`개 명령, `2,269/2,269` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **51**; 고유 호출 대상: **41**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00AAD609` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AAD61D` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AAD687` → [SeTokenGetNoChildProcessRestricted](../../text/45/SeTokenGetNoChildProcessRestricted_function_004584DC.md) (function, `0x004584DC`)
- `0x00AAD6E2` → [PsReferenceEffectiveToken](../9A/PsReferenceEffectiveToken_function_009A2B40.md) (function, `0x009A2B40`)
- `0x00AAD6FB` → [SeTokenIsNoChildProcessRestrictionEnforced](../../text/60/SeTokenIsNoChildProcessRestrictionEnforced_function_00609A38.md) (function, `0x00609A38`)
- `0x00AAD72D` → [ObFastDereferenceObject](../../text/3E/ObFastDereferenceObject_function_003ED5F0.md) (function, `0x003ED5F0`)
- `0x00AAD741` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AAD7B4` → [EtwTimLogProhibitChildProcessCreation](../A4/EtwTimLogProhibitChildProcessCreation_function_00A43694.md) (function, `0x00A43694`)
- `0x00AAD7CE` → [Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline](../../text/4C/Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline_function_004C78E8.md) (function, `0x004C78E8`)
- `0x00AAD7E0` → [RtlQueryElevationFlags](../A6/RtlQueryElevationFlags_function_00A60CB0.md) (function, `0x00A60CB0`)
- `0x00AAD81E` → [SepLocateTokenIntegrity](../../text/41/SepLocateTokenIntegrity_function_0041BF10.md) (function, `0x0041BF10`)
- `0x00AAD82E` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (function, `0x00468F10`)
- `0x00AAD845` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x00AAD868` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x00AAD8B7` → [SepCreateAppContainerToken](../../text/4F/SepCreateAppContainerToken_function_004F43AC.md) (function, `0x004F43AC`)
- `0x00AAD8C6` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x00AAD8FF` → [SepDereferenceLowBoxNumberEntry](../A5/SepDereferenceLowBoxNumberEntry_function_00A55DBC.md) (function, `0x00A55DBC`)
- `0x00AAD91F` → [SepSetTokenLowboxNumberEntry](../../text/60/SepSetTokenLowboxNumberEntry_function_0060B594.md) (function, `0x0060B594`)
- `0x00AAD966` → [SepSetTokenAntiTamperEntry](../../text/60/SepSetTokenAntiTamperEntry_function_0060B28C.md) (function, `0x0060B28C`)
- `0x00AAD978` → [SepDereferenceAntiTamperEntry](../7A/SepDereferenceAntiTamperEntry_function_007A2E50.md) (function, `0x007A2E50`)
- `0x00AAD9AC` → [SepDuplicateToken](../8B/SepDuplicateToken_function_008B87EC.md) (function, `0x008B87EC`)
- `0x00AAD9D2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AAD9EF` → [SepDeleteAccessState](../../text/3F/SepDeleteAccessState_function_003FFF20.md) (function, `0x003FFF20`)
- `0x00AADA13` → [SepDereferenceLowBoxNumberEntry](../A5/SepDereferenceLowBoxNumberEntry_function_00A55DBC.md) (function, `0x00A55DBC`)
- `0x00AADA38` → [SepSetTokenSessionById](../A0/SepSetTokenSessionById_function_00A0DAE4.md) (function, `0x00A0DAE4`)
- `0x00AADA51` → [SepSetTokenLowboxNumber](../A6/SepSetTokenLowboxNumber_function_00A64D6C.md) (function, `0x00A64D6C`)
- `0x00AADA73` → [SepSetTokenSessionById](../A0/SepSetTokenSessionById_function_00A0DAE4.md) (function, `0x00A0DAE4`)
- `0x00AADAC8` → [SepSetTokenBnoIsolation](../../text/49/SepSetTokenBnoIsolation_function_0049002C.md) (function, `0x0049002C`)
- `0x00AADB05` → [SepDesktopAppxSubProcessToken](../../text/45/SepDesktopAppxSubProcessToken_function_0045BD90.md) (function, `0x0045BD90`)
- `0x00AADB2B` → [SepMandatorySubProcessToken](../../text/4C/SepMandatorySubProcessToken_function_004C0B88.md) (function, `0x004C0B88`)
- `0x00AADB3D` → [Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline](../../text/4C/Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline_function_004C78E8.md) (function, `0x004C78E8`)
- `0x00AADB57` → [SepLocateTokenIntegrity](../../text/41/SepLocateTokenIntegrity_function_0041BF10.md) (function, `0x0041BF10`)
- `0x00AADB6A` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (function, `0x00468F10`)
- `0x00AADB81` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x00AADB92` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x00AADBC6` → [SepSetTrustLevelForProcessToken](../../text/40/SepSetTrustLevelForProcessToken_function_00400604.md) (function, `0x00400604`)
- `0x00AADBE7` → [SepSetProcessUniqueAttribute](../A4/SepSetProcessUniqueAttribute_function_00A424C8.md) (function, `0x00A424C8`)
- `0x00AADC16` → [SepSetTokenAllApplicationPackagesPolicy](../../text/60/SepSetTokenAllApplicationPackagesPolicy_function_00609A90.md) (function, `0x00609A90`)
- `0x00AADC40` → [SepAddTokenOriginClaim](../AF/SepAddTokenOriginClaim_function_00AF2130.md) (function, `0x00AF2130`)
- `0x00AADC45` → [Feature_AgentId2__private_IsEnabledDeviceUsageNoInline](../../text/60/Feature_AgentId2__private_IsEnabledDeviceUsageNoInline_function_006066CC.md) (function, `0x006066CC`)
- `0x00AADC61` → [SepGetAgentIdFromOriginClaim](../7A/SepGetAgentIdFromOriginClaim_function_007A10C0.md) (function, `0x007A10C0`)
- `0x00AADC9D` → [SepAddAgentIdClaimToToken](../7A/SepAddAgentIdClaimToToken_function_007A0B30.md) (function, `0x007A0B30`)
- `0x00AADCD9` → [SepSetTokenBnoIsolation](../../text/49/SepSetTokenBnoIsolation_function_0049002C.md) (function, `0x0049002C`)
- `0x00AADD40` → [SepCreateAccessStateFromSubjectContext](../../text/3E/SepCreateAccessStateFromSubjectContext_function_003EBF40.md) (function, `0x003EBF40`)
- `0x00AADD58` → [SeCreateAccessState](../8C/SeCreateAccessState_function_008C6AC0.md) (function, `0x008C6AC0`)
- `0x00AADD7E` → [ObInsertObjectEx](../8B/ObInsertObjectEx_function_008B97A0.md) (function, `0x008B97A0`)
- `0x00AADD93` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x00AADDB7` → [SepAppendAceToTokenObjectAcl](../8B/SepAppendAceToTokenObjectAcl_function_008B6430.md) (function, `0x008B6430`)
- `0x00AADDCB` → [SepFinalizeTokenAcls](../8B/SepFinalizeTokenAcls_function_008B63F4.md) (function, `0x008B63F4`)
- `0x00AADE1B` → [SeDeleteAccessState](../8C/SeDeleteAccessState_function_008C5F70.md) (function, `0x008C5F70`)
- `0x00AADE2C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PspInitializeProcessSecurity](PspInitializeProcessSecurity_function_00AAD368.md) at `0x00AAD45F`

### Static image references
- `0x00AAD58F` → RVA `0x00E0A740` (`.data`; read)
- `0x00AADBD5` → RVA `0x00E67E20` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **32**
  - `0x00AAD609` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AAD61D` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AAD687` → [SeTokenGetNoChildProcessRestricted](../../text/45/SeTokenGetNoChildProcessRestricted_function_004584DC.md) (`PAGE` → `.text`)
  - `0x00AAD6FB` → [SeTokenIsNoChildProcessRestrictionEnforced](../../text/60/SeTokenIsNoChildProcessRestrictionEnforced_function_00609A38.md) (`PAGE` → `.text`)
  - `0x00AAD72D` → [ObFastDereferenceObject](../../text/3E/ObFastDereferenceObject_function_003ED5F0.md) (`PAGE` → `.text`)
  - `0x00AAD741` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AAD7CE` → [Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline](../../text/4C/Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline_function_004C78E8.md) (`PAGE` → `.text`)
  - `0x00AAD81E` → [SepLocateTokenIntegrity](../../text/41/SepLocateTokenIntegrity_function_0041BF10.md) (`PAGE` → `.text`)
  - `0x00AAD82E` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (`PAGE` → `.text`)
  - `0x00AAD845` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x00AAD868` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (`PAGE` → `.text`)
  - `0x00AAD8B7` → [SepCreateAppContainerToken](../../text/4F/SepCreateAppContainerToken_function_004F43AC.md) (`PAGE` → `.text`)
  - `0x00AAD8C6` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (`PAGE` → `.text`)
  - `0x00AAD91F` → [SepSetTokenLowboxNumberEntry](../../text/60/SepSetTokenLowboxNumberEntry_function_0060B594.md) (`PAGE` → `.text`)
  - `0x00AAD966` → [SepSetTokenAntiTamperEntry](../../text/60/SepSetTokenAntiTamperEntry_function_0060B28C.md) (`PAGE` → `.text`)
  - `0x00AAD9D2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AAD9EF` → [SepDeleteAccessState](../../text/3F/SepDeleteAccessState_function_003FFF20.md) (`PAGE` → `.text`)
  - `0x00AADAC8` → [SepSetTokenBnoIsolation](../../text/49/SepSetTokenBnoIsolation_function_0049002C.md) (`PAGE` → `.text`)
  - `0x00AADB05` → [SepDesktopAppxSubProcessToken](../../text/45/SepDesktopAppxSubProcessToken_function_0045BD90.md) (`PAGE` → `.text`)
  - `0x00AADB2B` → [SepMandatorySubProcessToken](../../text/4C/SepMandatorySubProcessToken_function_004C0B88.md) (`PAGE` → `.text`)
  - `0x00AADB3D` → [Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline](../../text/4C/Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline_function_004C78E8.md) (`PAGE` → `.text`)
  - `0x00AADB57` → [SepLocateTokenIntegrity](../../text/41/SepLocateTokenIntegrity_function_0041BF10.md) (`PAGE` → `.text`)
  - `0x00AADB6A` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (`PAGE` → `.text`)
  - `0x00AADB81` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x00AADB92` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x00AADBC6` → [SepSetTrustLevelForProcessToken](../../text/40/SepSetTrustLevelForProcessToken_function_00400604.md) (`PAGE` → `.text`)
  - `0x00AADC16` → [SepSetTokenAllApplicationPackagesPolicy](../../text/60/SepSetTokenAllApplicationPackagesPolicy_function_00609A90.md) (`PAGE` → `.text`)
  - `0x00AADC45` → [Feature_AgentId2__private_IsEnabledDeviceUsageNoInline](../../text/60/Feature_AgentId2__private_IsEnabledDeviceUsageNoInline_function_006066CC.md) (`PAGE` → `.text`)
  - `0x00AADCD9` → [SepSetTokenBnoIsolation](../../text/49/SepSetTokenBnoIsolation_function_0049002C.md) (`PAGE` → `.text`)
  - `0x00AADD40` → [SepCreateAccessStateFromSubjectContext](../../text/3E/SepCreateAccessStateFromSubjectContext_function_003EBF40.md) (`PAGE` → `.text`)
  - `0x00AADD93` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (`PAGE` → `.text`)
  - `0x00AADE2C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AAD570  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00AAD575  55                              push rbp
00AAD576  56                              push rsi
00AAD577  57                              push rdi
00AAD578  41 54                           push r12
00AAD57A  41 55                           push r13
00AAD57C  41 56                           push r14
00AAD57E  41 57                           push r15
00AAD580  48 8D AC 24 50 FE FF FF         lea rbp, [rsp - 0x1b0]
00AAD588  48 81 EC B0 02 00 00            sub rsp, 0x2b0
00AAD58F  48 8B 05 AA D1 35 00            mov rax, qword ptr [rip + 0x35d1aa]
00AAD596  48 33 C4                        xor rax, rsp
00AAD599  48 89 85 A0 01 00 00            mov qword ptr [rbp + 0x1a0], rax
00AAD5A0  48 8B 85 28 02 00 00            mov rax, qword ptr [rbp + 0x228]
00AAD5A7  0F 57 C0                        xorps xmm0, xmm0
00AAD5AA  48 8B BD 40 02 00 00            mov rdi, qword ptr [rbp + 0x240]
00AAD5B1  41 8B D9                        mov ebx, r9d
00AAD5B4  4C 8B BD 18 02 00 00            mov r15, qword ptr [rbp + 0x218]
00AAD5BB  49 8B F0                        mov rsi, r8
00AAD5BE  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00AAD5C3  4C 8B F2                        mov r14, rdx
00AAD5C6  48 8B 85 38 02 00 00            mov rax, qword ptr [rbp + 0x238]
00AAD5CD  4C 8B E9                        mov r13, rcx
00AAD5D0  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00AAD5D4  48 8D 4D 20                     lea rcx, [rbp + 0x20]
00AAD5D8  33 C0                           xor eax, eax
00AAD5DA  4C 89 45 88                     mov qword ptr [rbp - 0x78], r8
00AAD5DE  45 33 E4                        xor r12d, r12d
00AAD5E1  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00AAD5E5  33 D2                           xor edx, edx
00AAD5E7  89 45 C0                        mov dword ptr [rbp - 0x40], eax
00AAD5EA  41 B8 A0 00 00 00               mov r8d, 0xa0
00AAD5F0  89 5C 24 58                     mov dword ptr [rsp + 0x58], ebx
00AAD5F4  48 89 7D 90                     mov qword ptr [rbp - 0x70], rdi
00AAD5F8  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
00AAD5FD  0F 11 45 98                     movups xmmword ptr [rbp - 0x68], xmm0
00AAD601  44 89 65 04                     mov dword ptr [rbp + 4], r12d
00AAD605  0F 11 45 A8                     movups xmmword ptr [rbp - 0x58], xmm0
00AAD609  E8 32 96 C1 FF                  call 0x1406c6c40
00AAD60E  33 D2                           xor edx, edx
00AAD610  48 8D 8D C0 00 00 00            lea rcx, [rbp + 0xc0]
00AAD617  41 B8 E0 00 00 00               mov r8d, 0xe0
00AAD61D  E8 1E 96 C1 FF                  call 0x1406c6c40
00AAD622  4C 89 26                        mov qword ptr [rsi], r12
00AAD625  4C 8D 4C 24 51                  lea r9, [rsp + 0x51]
00AAD62A  33 C0                           xor eax, eax
00AAD62C  66 44 89 27                     mov word ptr [rdi], r12w
00AAD630  0F 57 C0                        xorps xmm0, xmm0
00AAD633  44 88 67 02                     mov byte ptr [rdi + 2], r12b
00AAD637  33 FF                           xor edi, edi
00AAD639  44 88 64 24 50                  mov byte ptr [rsp + 0x50], r12b
00AAD63E  4C 8D 44 24 52                  lea r8, [rsp + 0x52]
00AAD643  40 88 7C 24 41                  mov byte ptr [rsp + 0x41], dil
00AAD648  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
00AAD64D  40 88 7C 24 54                  mov byte ptr [rsp + 0x54], dil
00AAD652  49 8B CE                        mov rcx, r14
00AAD655  40 88 7C 24 55                  mov byte ptr [rsp + 0x55], dil
00AAD65A  40 88 7C 24 40                  mov byte ptr [rsp + 0x40], dil
00AAD65F  48 89 7C 24 68                  mov qword ptr [rsp + 0x68], rdi
00AAD664  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
00AAD669  40 88 7C 24 53                  mov byte ptr [rsp + 0x53], dil
00AAD66E  44 88 64 24 52                  mov byte ptr [rsp + 0x52], r12b
00AAD673  44 88 64 24 51                  mov byte ptr [rsp + 0x51], r12b
00AAD678  0F 11 45 C8                     movups xmmword ptr [rbp - 0x38], xmm0
00AAD67C  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00AAD680  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
00AAD684  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00AAD687  E8 50 AE 9A FF                  call 0x1404584dc
00AAD68C  40 8A 74 24 50                  mov sil, byte ptr [rsp + 0x50]
00AAD691  40 84 F6                        test sil, sil
00AAD694  75 0B                           jne 0x140aad6a1
00AAD696  40 38 7C 24 51                  cmp byte ptr [rsp + 0x51], dil
00AAD69B  0F 84 2D 01 00 00               je 0x140aad7ce
00AAD6A1  41 8B 07                        mov eax, dword ptr [r15]
00AAD6A4  BF 9D 04 00 C0                  mov edi, 0xc000049d
00AAD6A9  A8 02                           test al, 2
00AAD6AB  0F 84 9A 00 00 00               je 0x140aad74b
00AAD6B1  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00AAD6BA  48 8D 44 24 5C                  lea rax, [rsp + 0x5c]
00AAD6BF  33 F6                           xor esi, esi
00AAD6C1  4C 8D 4C 24 51                  lea r9, [rsp + 0x51]
00AAD6C6  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00AAD6CB  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00AAD6D0  BA 53 68 72 74                  mov edx, 0x74726853
00AAD6D5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AAD6DA  89 74 24 60                     mov dword ptr [rsp + 0x60], esi
00AAD6DE  89 74 24 5C                     mov dword ptr [rsp + 0x5c], esi
00AAD6E2  E8 59 54 EF FF                  call 0x1409a2b40
00AAD6E7  83 7C 24 60 02                  cmp dword ptr [rsp + 0x60], 2
00AAD6EC  48 8B D8                        mov rbx, rax
00AAD6EF  75 07                           jne 0x140aad6f8
00AAD6F1  83 7C 24 5C 02                  cmp dword ptr [rsp + 0x5c], 2
00AAD6F6  7C 3C                           jl 0x140aad734
00AAD6F8  48 8B CB                        mov rcx, rbx
00AAD6FB  E8 38 C3 B5 FF                  call 0x140609a38
00AAD700  F6 D8                           neg al
00AAD702  1B C9                           sbb ecx, ecx
00AAD704  23 F9                           and edi, ecx
00AAD706  83 7C 24 60 01                  cmp dword ptr [rsp + 0x60], 1
00AAD70B  75 27                           jne 0x140aad734
00AAD70D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AAD716  41 B8 53 68 72 74               mov r8d, 0x74726853
00AAD71C  48 8B D3                        mov rdx, rbx
00AAD71F  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00AAD726  48 81 C1 48 02 00 00            add rcx, 0x248
00AAD72D  E8 BE FE 93 FF                  call 0x1403ed5f0
00AAD732  EB 12                           jmp 0x140aad746
00AAD734  48 85 DB                        test rbx, rbx
00AAD737  74 0D                           je 0x140aad746
00AAD739  BA 53 68 72 74                  mov edx, 0x74726853
00AAD73E  48 8B CB                        mov rcx, rbx
00AAD741  E8 9A A1 84 FF                  call 0x1402f78e0
00AAD746  40 8A 74 24 50                  mov sil, byte ptr [rsp + 0x50]
00AAD74B  41 8B 85 FC 05 00 00            mov eax, dword ptr [r13 + 0x5fc]
00AAD752  33 DB                           xor ebx, ebx
00AAD754  41 83 7F 08 01                  cmp dword ptr [r15 + 8], 1
00AAD759  0F 45 DF                        cmovne ebx, edi
00AAD75C  33 FF                           xor edi, edi
00AAD75E  A8 01                           test al, 1
00AAD760  74 09                           je 0x140aad76b
00AAD762  49 39 BD 40 06 00 00            cmp qword ptr [r13 + 0x640], rdi
00AAD769  74 5F                           je 0x140aad7ca
00AAD76B  85 DB                           test ebx, ebx
00AAD76D  79 5B                           jns 0x140aad7ca
00AAD76F  40 38 7C 24 52                  cmp byte ptr [rsp + 0x52], dil
00AAD774  74 06                           je 0x140aad77c
00AAD776  41 39 7F 0C                     cmp dword ptr [r15 + 0xc], edi
00AAD77A  75 4E                           jne 0x140aad7ca
00AAD77C  49 8B 57 18                     mov rdx, qword ptr [r15 + 0x18]
00AAD780  48 8B C2                        mov rax, rdx
00AAD783  48 F7 D8                        neg rax
00AAD786  4D 1B C9                        sbb r9, r9
00AAD789  48 8D 4A 70                     lea rcx, [rdx + 0x70]
00AAD78D  4C 23 C9                        and r9, rcx
00AAD790  48 8D 42 60                     lea rax, [rdx + 0x60]
00AAD794  48 F7 DA                        neg rdx
00AAD797  49 8B 57 10                     mov rdx, qword ptr [r15 + 0x10]
00AAD79B  48 1B FF                        sbb rdi, rdi
00AAD79E  48 23 F8                        and rdi, rax
00AAD7A1  40 8A C6                        mov al, sil
00AAD7A4  F6 D8                           neg al
00AAD7A6  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
00AAD7AB  4C 8B C7                        mov r8, rdi
00AAD7AE  1B C9                           sbb ecx, ecx
00AAD7B0  F7 D9                           neg ecx
00AAD7B2  FF C1                           inc ecx
00AAD7B4  E8 DB 5E F9 FF                  call 0x140a43694
00AAD7B9  33 FF                           xor edi, edi
00AAD7BB  40 84 F6                        test sil, sil
00AAD7BE  74 0A                           je 0x140aad7ca
00AAD7C0  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00AAD7C5  E9 FB 01 00 00                  jmp 0x140aad9c5
00AAD7CA  8B 5C 24 58                     mov ebx, dword ptr [rsp + 0x58]
00AAD7CE  E8 15 A1 A1 FF                  call 0x1404c78e8
00AAD7D3  85 C0                           test eax, eax
00AAD7D5  74 76                           je 0x140aad84d
00AAD7D7  48 8D 4C 24 5C                  lea rcx, [rsp + 0x5c]
00AAD7DC  89 7C 24 5C                     mov dword ptr [rsp + 0x5c], edi
00AAD7E0  E8 CB 34 FB FF                  call 0x140a60cb0
00AAD7E5  8B 44 24 5C                     mov eax, dword ptr [rsp + 0x5c]
00AAD7E9  24 18                           and al, 0x18
00AAD7EB  3C 10                           cmp al, 0x10
00AAD7ED  75 5E                           jne 0x140aad84d
00AAD7EF  49 8B 86 D8 00 00 00            mov rax, qword ptr [r14 + 0xd8]
00AAD7F6  8B 48 28                        mov ecx, dword ptr [rax + 0x28]
00AAD7F9  F6 C1 04                        test cl, 4
00AAD7FC  74 4F                           je 0x140aad84d
00AAD7FE  41 8B 86 C8 00 00 00            mov eax, dword ptr [r14 + 0xc8]
00AAD805  0F BA E0 1B                     bt eax, 0x1b
00AAD809  73 42                           jae 0x140aad84d
00AAD80B  0F BA E0 0C                     bt eax, 0xc
00AAD80F  73 3C                           jae 0x140aad84d
00AAD811  F6 C3 02                        test bl, 2
00AAD814  74 37                           je 0x140aad84d
00AAD816  49 8B CE                        mov rcx, r14
00AAD819  C6 44 24 53 01                  mov byte ptr [rsp + 0x53], 1
00AAD81E  E8 ED E6 96 FF                  call 0x14041bf10
00AAD823  48 85 C0                        test rax, rax
00AAD826  74 25                           je 0x140aad84d
00AAD828  48 8B 18                        mov rbx, qword ptr [rax]
00AAD82B  48 8B CB                        mov rcx, rbx
00AAD82E  E8 DD B6 9B FF                  call 0x140468f10
00AAD833  0F B6 08                        movzx ecx, byte ptr [rax]
00AAD836  84 C9                           test cl, cl
00AAD838  75 05                           jne 0x140aad83f
00AAD83A  44 8B E7                        mov r12d, edi
00AAD83D  EB 0E                           jmp 0x140aad84d
00AAD83F  8D 51 FF                        lea edx, [rcx - 1]
00AAD842  48 8B CB                        mov rcx, rbx
00AAD845  E8 C6 94 9A FF                  call 0x140456d10
00AAD84A  44 8B 20                        mov r12d, dword ptr [rax]
00AAD84D  BB 30 00 00 00                  mov ebx, 0x30
00AAD852  48 89 7D A0                     mov qword ptr [rbp - 0x60], rdi
00AAD856  0F 57 C0                        xorps xmm0, xmm0
00AAD859  89 5D 98                        mov dword ptr [rbp - 0x68], ebx
00AAD85C  F3 0F 7F 45 B8                  movdqu xmmword ptr [rbp - 0x48], xmm0
00AAD861  89 7D B0                        mov dword ptr [rbp - 0x50], edi
00AAD864  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
00AAD868  E8 1B 1F A4 FF                  call 0x1404ef788
00AAD86D  85 C0                           test eax, eax
00AAD86F  0F 84 0F 01 00 00               je 0x140aad984
00AAD875  49 8B 47 20                     mov rax, qword ptr [r15 + 0x20]
00AAD879  48 85 C0                        test rax, rax
00AAD87C  0F 84 02 01 00 00               je 0x140aad984
00AAD882  0F 57 C0                        xorps xmm0, xmm0
00AAD885  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AAD88A  4C 8D 4D C8                     lea r9, [rbp - 0x38]
00AAD88E  89 5D C8                        mov dword ptr [rbp - 0x38], ebx
00AAD891  41 B8 FF 01 0F 00               mov r8d, 0xf01ff
00AAD897  48 89 7D D0                     mov qword ptr [rbp - 0x30], rdi
00AAD89B  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00AAD8A0  C7 45 E0 00 06 00 00            mov dword ptr [rbp - 0x20], 0x600
00AAD8A7  33 C9                           xor ecx, ecx
00AAD8A9  48 89 7D D8                     mov qword ptr [rbp - 0x28], rdi
00AAD8AD  F3 0F 7F 45 E8                  movdqu xmmword ptr [rbp - 0x18], xmm0
00AAD8B2  40 88 7C 24 20                  mov byte ptr [rsp + 0x20], dil
00AAD8B7  E8 F0 6A A4 FF                  call 0x1404f43ac
00AAD8BC  8B D8                           mov ebx, eax
00AAD8BE  85 C0                           test eax, eax
00AAD8C0  0F 88 FA 00 00 00               js 0x140aad9c0
00AAD8C6  E8 9D 00 B2 FF                  call 0x1405cd968
00AAD8CB  8B BD 10 02 00 00               mov edi, dword ptr [rbp + 0x210]
00AAD8D1  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AAD8D6  85 C0                           test eax, eax
00AAD8D8  0F 84 1B 01 00 00               je 0x140aad9f9
00AAD8DE  44 8B 41 78                     mov r8d, dword ptr [rcx + 0x78]
00AAD8E2  44 3B C7                        cmp r8d, edi
00AAD8E5  0F 84 7A 01 00 00               je 0x140aada65
00AAD8EB  0F BA A1 C8 00 00 00 0E         bt dword ptr [rcx + 0xc8], 0xe
00AAD8F3  73 3E                           jae 0x140aad933
00AAD8F5  48 8B 91 38 04 00 00            mov rdx, qword ptr [rcx + 0x438]
00AAD8FC  41 8B C8                        mov ecx, r8d
00AAD8FF  E8 B8 84 FA FF                  call 0x140a55dbc
00AAD904  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00AAD909  8B D7                           mov edx, edi
00AAD90B  48 83 A0 38 04 00 00 00         and qword ptr [rax + 0x438], 0
00AAD913  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AAD918  4C 8B 81 10 03 00 00            mov r8, qword ptr [rcx + 0x310]
00AAD91F  E8 70 DC B5 FF                  call 0x14060b594
00AAD924  8B D8                           mov ebx, eax
00AAD926  85 C0                           test eax, eax
00AAD928  0F 88 92 00 00 00               js 0x140aad9c0
00AAD92E  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AAD933  48 8B B1 B8 05 00 00            mov rsi, qword ptr [rcx + 0x5b8]
00AAD93A  48 85 F6                        test rsi, rsi
00AAD93D  0F 84 22 01 00 00               je 0x140aada65
00AAD943  48 83 A1 B8 05 00 00 00         and qword ptr [rcx + 0x5b8], 0
00AAD94B  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AAD950  4C 8B 81 98 04 00 00            mov r8, qword ptr [rcx + 0x498]
00AAD957  4D 85 C0                        test r8, r8
00AAD95A  74 16                           je 0x140aad972
00AAD95C  4C 8B 4E 30                     mov r9, qword ptr [rsi + 0x30]
00AAD960  8B D7                           mov edx, edi
00AAD962  4D 8B 40 10                     mov r8, qword ptr [r8 + 0x10]
00AAD966  E8 21 D9 B5 FF                  call 0x14060b28c
00AAD96B  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AAD970  8B D8                           mov ebx, eax
00AAD972  8B 49 78                        mov ecx, dword ptr [rcx + 0x78]
00AAD975  48 8B D6                        mov rdx, rsi
00AAD978  E8 D3 54 CF FF                  call 0x1407a2e50
00AAD97D  85 DB                           test ebx, ebx
00AAD97F  E9 D6 00 00 00                  jmp 0x140aada5a
00AAD984  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00AAD989  41 B9 01 00 00 00               mov r9d, 1
00AAD98F  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AAD994  48 8D 55 98                     lea rdx, [rbp - 0x68]
00AAD998  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
00AAD99D  45 33 C0                        xor r8d, r8d
00AAD9A0  40 88 7C 24 28                  mov byte ptr [rsp + 0x28], dil
00AAD9A5  49 8B CE                        mov rcx, r14
00AAD9A8  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00AAD9AC  E8 3B AE E0 FF                  call 0x1408b87ec
00AAD9B1  8B D8                           mov ebx, eax
00AAD9B3  85 C0                           test eax, eax
00AAD9B5  0F 89 0B FF FF FF               jns 0x140aad8c6
00AAD9BB  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
00AAD9C0  40 8A 7C 24 40                  mov dil, byte ptr [rsp + 0x40]
00AAD9C5  45 33 F6                        xor r14d, r14d
00AAD9C8  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AAD9CD  48 85 C9                        test rcx, rcx
00AAD9D0  74 05                           je 0x140aad9d7
00AAD9D2  E8 79 B9 84 FF                  call 0x1402f9350
00AAD9D7  40 84 FF                        test dil, dil
00AAD9DA  0F 84 40 04 00 00               je 0x140aade20
00AAD9E0  48 8D 4D 20                     lea rcx, [rbp + 0x20]
00AAD9E4  44 38 74 24 41                  cmp byte ptr [rsp + 0x41], r14b
00AAD9E9  0F 84 2C 04 00 00               je 0x140aade1b
00AAD9EF  E8 2C 25 95 FF                  call 0x1403fff20
00AAD9F4  E9 27 04 00 00                  jmp 0x140aade20
00AAD9F9  0F BA A1 C8 00 00 00 0E         bt dword ptr [rcx + 0xc8], 0xe
00AADA01  73 62                           jae 0x140aada65
00AADA03  8B 41 78                        mov eax, dword ptr [rcx + 0x78]
00AADA06  3B C7                           cmp eax, edi
00AADA08  74 5B                           je 0x140aada65
00AADA0A  48 8B 91 38 04 00 00            mov rdx, qword ptr [rcx + 0x438]
00AADA11  8B C8                           mov ecx, eax
00AADA13  E8 A4 83 FA FF                  call 0x140a55dbc
00AADA18  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00AADA1D  45 33 C9                        xor r9d, r9d
00AADA20  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00AADA26  45 33 C0                        xor r8d, r8d
00AADA29  8B D7                           mov edx, edi
00AADA2B  48 83 A0 38 04 00 00 00         and qword ptr [rax + 0x438], 0
00AADA33  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AADA38  E8 A7 00 F6 FF                  call 0x140a0dae4
00AADA3D  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00AADA42  89 78 78                        mov dword ptr [rax + 0x78], edi
00AADA45  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AADA4A  48 8B 91 10 03 00 00            mov rdx, qword ptr [rcx + 0x310]
00AADA51  E8 16 73 FB FF                  call 0x140a64d6c
00AADA56  8B D8                           mov ebx, eax
00AADA58  85 C0                           test eax, eax
00AADA5A  0F 88 60 FF FF FF               js 0x140aad9c0
00AADA60  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AADA65  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00AADA6B  45 33 C9                        xor r9d, r9d
00AADA6E  45 33 C0                        xor r8d, r8d
00AADA71  8B D7                           mov edx, edi
00AADA73  E8 6C 00 F6 FF                  call 0x140a0dae4
00AADA78  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00AADA7D  89 78 78                        mov dword ptr [rax + 0x78], edi
00AADA80  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00AADA85  0F BA B0 C8 00 00 00 15         btr dword ptr [rax + 0xc8], 0x15
00AADA8D  41 8B 07                        mov eax, dword ptr [r15]
00AADA90  A8 01                           test al, 1
00AADA92  74 21                           je 0x140aadab5
00AADA94  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00AADA99  0F BA A8 C8 00 00 00 13         bts dword ptr [rax + 0xc8], 0x13
00AADAA1  41 8B 07                        mov eax, dword ptr [r15]
00AADAA4  A8 04                           test al, 4
00AADAA6  74 0D                           je 0x140aadab5
00AADAA8  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00AADAAD  0F BA A8 C8 00 00 00 14         bts dword ptr [rax + 0xc8], 0x14
00AADAB5  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AADABA  45 33 C9                        xor r9d, r9d
00AADABD  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00AADAC3  45 33 C0                        xor r8d, r8d
00AADAC6  33 D2                           xor edx, edx
00AADAC8  E8 5F 25 9E FF                  call 0x14049002c
00AADACD  8B D8                           mov ebx, eax
00AADACF  85 C0                           test eax, eax
00AADAD1  0F 88 E9 FE FF FF               js 0x140aad9c0
00AADAD7  8B 74 24 58                     mov esi, dword ptr [rsp + 0x58]
00AADADB  48 8D 44 24 55                  lea rax, [rsp + 0x55]
00AADAE0  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AADAE5  45 33 C0                        xor r8d, r8d
00AADAE8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AADAED  49 8B D5                        mov rdx, r13
00AADAF0  48 8D 44 24 54                  lea rax, [rsp + 0x54]
00AADAF5  83 E6 02                        and esi, 2
00AADAF8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AADAFD  41 8B 47 04                     mov eax, dword ptr [r15 + 4]
00AADB01  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00AADB05  E8 86 E2 9A FF                  call 0x14045bd90
00AADB0A  8B D8                           mov ebx, eax
00AADB0C  85 C0                           test eax, eax
00AADB0E  0F 88 AC FE FF FF               js 0x140aad9c0
00AADB14  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00AADB19  4C 8D 4C 24 68                  lea r9, [rsp + 0x68]
00AADB1E  8B C6                           mov eax, esi
00AADB20  4D 8B C5                        mov r8, r13
00AADB23  F7 D8                           neg eax
00AADB25  48 1B C9                        sbb rcx, rcx
00AADB28  49 23 CE                        and rcx, r14
00AADB2B  E8 58 30 A1 FF                  call 0x1404c0b88
00AADB30  45 33 F6                        xor r14d, r14d
00AADB33  8B D8                           mov ebx, eax
00AADB35  85 C0                           test eax, eax
00AADB37  0F 88 D6 02 00 00               js 0x140aade13
00AADB3D  E8 A6 9D A1 FF                  call 0x1404c78e8
00AADB42  85 C0                           test eax, eax
00AADB44  74 6E                           je 0x140aadbb4
00AADB46  44 38 74 24 53                  cmp byte ptr [rsp + 0x53], r14b
00AADB4B  74 67                           je 0x140aadbb4
00AADB4D  45 85 E4                        test r12d, r12d
00AADB50  74 62                           je 0x140aadbb4
00AADB52  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AADB57  E8 B4 E3 96 FF                  call 0x14041bf10
00AADB5C  48 8B D8                        mov rbx, rax
00AADB5F  48 85 C0                        test rax, rax
00AADB62  74 50                           je 0x140aadbb4
00AADB64  48 8B 38                        mov rdi, qword ptr [rax]
00AADB67  48 8B CF                        mov rcx, rdi
00AADB6A  E8 A1 B3 9B FF                  call 0x140468f10
00AADB6F  0F B6 08                        movzx ecx, byte ptr [rax]
00AADB72  84 C9                           test cl, cl
00AADB74  75 05                           jne 0x140aadb7b
00AADB76  41 8B C6                        mov eax, r14d
00AADB79  EB 0D                           jmp 0x140aadb88
00AADB7B  8D 51 FF                        lea edx, [rcx - 1]
00AADB7E  48 8B CF                        mov rcx, rdi
00AADB81  E8 8A 91 9A FF                  call 0x140456d10
00AADB86  8B 00                           mov eax, dword ptr [rax]
00AADB88  41 3B C4                        cmp eax, r12d
00AADB8B  73 27                           jae 0x140aadbb4
00AADB8D  33 D2                           xor edx, edx
00AADB8F  48 8B CF                        mov rcx, rdi
00AADB92  E8 79 91 9A FF                  call 0x140456d10
00AADB97  B9 00 20 00 00                  mov ecx, 0x2000
00AADB9C  44 89 20                        mov dword ptr [rax], r12d
00AADB9F  48 8B 3B                        mov rdi, qword ptr [rbx]
00AADBA2  44 3B E1                        cmp r12d, ecx
00AADBA5  72 12                           jb 0x140aadbb9
00AADBA7  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00AADBAC  09 88 C8 00 00 00               or dword ptr [rax + 0xc8], ecx
00AADBB2  EB 05                           jmp 0x140aadbb9
00AADBB4  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00AADBB9  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AADBBE  4C 8D 44 24 41                  lea r8, [rsp + 0x41]
00AADBC3  49 8B D5                        mov rdx, r13
00AADBC6  E8 39 2A 95 FF                  call 0x140400604
00AADBCB  8B D8                           mov ebx, eax
00AADBCD  85 C0                           test eax, eax
00AADBCF  0F 88 3E 02 00 00               js 0x140aade13
00AADBD5  8B 05 45 A2 3B 00               mov eax, dword ptr [rip + 0x3ba245]
00AADBDB  83 E0 03                        and eax, 3
00AADBDE  3C 03                           cmp al, 3
00AADBE0  75 14                           jne 0x140aadbf6
00AADBE2  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AADBE7  E8 DC 48 F9 FF                  call 0x140a424c8
00AADBEC  8B D8                           mov ebx, eax
00AADBEE  85 C0                           test eax, eax
00AADBF0  0F 88 1D 02 00 00               js 0x140aade13
00AADBF6  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
00AADBFB  41 F7 80 C8 00 00 00 00 40 00 00  test dword ptr [r8 + 0xc8], 0x4000
00AADC06  74 22                           je 0x140aadc2a
00AADC08  8B 95 20 02 00 00               mov edx, dword ptr [rbp + 0x220]
00AADC0E  F6 C2 01                        test dl, 1
00AADC11  74 17                           je 0x140aadc2a
00AADC13  49 8B C8                        mov rcx, r8
00AADC16  E8 75 BE B5 FF                  call 0x140609a90
00AADC1B  8B D8                           mov ebx, eax
00AADC1D  85 C0                           test eax, eax
00AADC1F  0F 88 EE 01 00 00               js 0x140aade13
00AADC25  4C 8B 44 24 48                  mov r8, qword ptr [rsp + 0x48]
00AADC2A  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00AADC2F  48 85 DB                        test rbx, rbx
00AADC32  74 11                           je 0x140aadc45
00AADC34  8B 95 30 02 00 00               mov edx, dword ptr [rbp + 0x230]
00AADC3A  45 33 C9                        xor r9d, r9d
00AADC3D  48 8B CB                        mov rcx, rbx
00AADC40  E8 EB 44 04 00                  call 0x140af2130
00AADC45  E8 82 8A B5 FF                  call 0x1406066cc
00AADC4A  85 C0                           test eax, eax
00AADC4C  74 6A                           je 0x140aadcb8
00AADC4E  8B 95 30 02 00 00               mov edx, dword ptr [rbp + 0x230]
00AADC54  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
00AADC59  48 8B CB                        mov rcx, rbx
00AADC5C  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
00AADC61  E8 5A 34 CF FF                  call 0x1407a10c0
00AADC66  84 C0                           test al, al
00AADC68  74 4E                           je 0x140aadcb8
00AADC6A  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AADC6F  8B 81 90 04 00 00               mov eax, dword ptr [rcx + 0x490]
00AADC75  A8 02                           test al, 2
00AADC77  75 44                           jne 0x140aadcbd
00AADC79  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
00AADC7E  48 85 D2                        test rdx, rdx
00AADC81  74 0D                           je 0x140aadc90
00AADC83  66 44 39 32                     cmp word ptr [rdx], r14w
00AADC87  76 07                           jbe 0x140aadc90
00AADC89  48 85 D2                        test rdx, rdx
00AADC8C  74 2F                           je 0x140aadcbd
00AADC8E  EB 0D                           jmp 0x140aadc9d
00AADC90  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00AADC95  48 85 C0                        test rax, rax
00AADC98  74 23                           je 0x140aadcbd
00AADC9A  48 8B D0                        mov rdx, rax
00AADC9D  E8 8E 2E CF FF                  call 0x1407a0b30
00AADCA2  8B D8                           mov ebx, eax
00AADCA4  85 C0                           test eax, eax
00AADCA6  0F 88 67 01 00 00               js 0x140aade13
00AADCAC  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00AADCB1  83 88 90 04 00 00 02            or dword ptr [rax + 0x490], 2
00AADCB8  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AADCBD  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
00AADCC1  48 85 D2                        test rdx, rdx
00AADCC4  74 27                           je 0x140aadced
00AADCC6  48 8B 42 18                     mov rax, qword ptr [rdx + 0x18]
00AADCCA  4C 8B C2                        mov r8, rdx
00AADCCD  44 8B 4A 10                     mov r9d, dword ptr [rdx + 0x10]
00AADCD1  8A 52 20                        mov dl, byte ptr [rdx + 0x20]
00AADCD4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AADCD9  E8 4E 23 9E FF                  call 0x14049002c
00AADCDE  8B D8                           mov ebx, eax
00AADCE0  85 C0                           test eax, eax
00AADCE2  0F 88 2B 01 00 00               js 0x140aade13
00AADCE8  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AADCED  85 F6                           test esi, esi
00AADCEF  74 05                           je 0x140aadcf6
00AADCF1  48 85 FF                        test rdi, rdi
00AADCF4  74 05                           je 0x140aadcfb
00AADCF6  C6 44 24 41 01                  mov byte ptr [rsp + 0x41], 1
00AADCFB  44 38 74 24 41                  cmp byte ptr [rsp + 0x41], r14b
00AADD00  74 45                           je 0x140aadd47
00AADD02  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AADD0B  4C 8D 85 C0 00 00 00            lea r8, [rbp + 0xc0]
00AADD12  48 89 4D 08                     mov qword ptr [rbp + 8], rcx
00AADD16  48 8D 55 20                     lea rdx, [rbp + 0x20]
00AADD1A  45 33 C9                        xor r9d, r9d
00AADD1D  4C 89 75 F8                     mov qword ptr [rbp - 8], r14
00AADD21  44 89 75 00                     mov dword ptr [rbp], r14d
00AADD25  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00AADD2C  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00AADD31  48 8B 81 D0 01 00 00            mov rax, qword ptr [rcx + 0x1d0]
00AADD38  48 8D 4D F8                     lea rcx, [rbp - 8]
00AADD3C  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00AADD40  E8 FB E1 93 FF                  call 0x1403ebf40
00AADD45  EB 16                           jmp 0x140aadd5d
00AADD47  45 33 C9                        xor r9d, r9d
00AADD4A  48 8D 95 C0 00 00 00            lea rdx, [rbp + 0xc0]
00AADD51  45 33 C0                        xor r8d, r8d
00AADD54  48 8D 4D 20                     lea rcx, [rbp + 0x20]
00AADD58  E8 63 8D E1 FF                  call 0x1408c6ac0
00AADD5D  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AADD62  48 8D 55 20                     lea rdx, [rbp + 0x20]
00AADD66  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AADD6B  45 33 C9                        xor r9d, r9d
00AADD6E  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00AADD73  45 33 C0                        xor r8d, r8d
00AADD76  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
00AADD7B  40 B7 01                        mov dil, 1
00AADD7E  E8 1D BA E0 FF                  call 0x1408b97a0
00AADD83  8B D8                           mov ebx, eax
00AADD85  85 C0                           test eax, eax
00AADD87  79 0A                           jns 0x140aadd93
00AADD89  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
00AADD8E  E9 35 FC FF FF                  jmp 0x140aad9c8
00AADD93  E8 F0 19 A4 FF                  call 0x1404ef788
00AADD98  85 C0                           test eax, eax
00AADD9A  74 2A                           je 0x140aaddc6
00AADD9C  4D 8B 47 20                     mov r8, qword ptr [r15 + 0x20]
00AADDA0  4D 85 C0                        test r8, r8
00AADDA3  74 21                           je 0x140aaddc6
00AADDA5  4D 8B 40 08                     mov r8, qword ptr [r8 + 8]
00AADDA9  BA FF 01 0F 00                  mov edx, 0xf01ff
00AADDAE  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AADDB3  4D 8B 40 10                     mov r8, qword ptr [r8 + 0x10]
00AADDB7  E8 74 86 E0 FF                  call 0x1408b6430
00AADDBC  8B D8                           mov ebx, eax
00AADDBE  85 C0                           test eax, eax
00AADDC0  0F 88 02 FC FF FF               js 0x140aad9c8
00AADDC6  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AADDCB  E8 24 86 E0 FF                  call 0x1408b63f4
00AADDD0  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00AADDD5  8B 4C 24 58                     mov ecx, dword ptr [rsp + 0x58]
00AADDD9  40 22 CF                        and cl, dil
00AADDDC  88 88 CC 00 00 00               mov byte ptr [rax + 0xcc], cl
00AADDE2  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
00AADDE6  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00AADDEB  48 89 01                        mov qword ptr [rcx], rax
00AADDEE  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
00AADDF2  8A 44 24 41                     mov al, byte ptr [rsp + 0x41]
00AADDF6  88 01                           mov byte ptr [rcx], al
00AADDF8  8A 44 24 54                     mov al, byte ptr [rsp + 0x54]
00AADDFC  88 41 01                        mov byte ptr [rcx + 1], al
00AADDFF  8A 44 24 55                     mov al, byte ptr [rsp + 0x55]
00AADE03  88 41 02                        mov byte ptr [rcx + 2], al
00AADE06  85 DB                           test ebx, ebx
00AADE08  0F 89 D2 FB FF FF               jns 0x140aad9e0
00AADE0E  E9 B5 FB FF FF                  jmp 0x140aad9c8
00AADE13  41 8A FE                        mov dil, r14b
00AADE16  E9 AD FB FF FF                  jmp 0x140aad9c8
00AADE1B  E8 50 81 E1 FF                  call 0x1408c5f70
00AADE20  8B C3                           mov eax, ebx
00AADE22  48 8B 8D A0 01 00 00            mov rcx, qword ptr [rbp + 0x1a0]
00AADE29  48 33 CC                        xor rcx, rsp
00AADE2C  E8 0F E8 BF FF                  call 0x1406ac640
00AADE31  48 8B 9C 24 08 03 00 00         mov rbx, qword ptr [rsp + 0x308]
00AADE39  48 81 C4 B0 02 00 00            add rsp, 0x2b0
00AADE40  41 5F                           pop r15
00AADE42  41 5E                           pop r14
00AADE44  41 5D                           pop r13
00AADE46  41 5C                           pop r12
00AADE48  5F                              pop rdi
00AADE49  5E                              pop rsi
00AADE4A  5D                              pop rbp
00AADE4B  C3                              ret
00AADE4C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeSubProcessToken(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5, __int64 a6, unsigned int a7, __int64 a8, unsigned int a9, __int64 a10, __int64 a11)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned int v_stack_m1E4;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned int v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned int v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned int v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned int v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m28C;
    unsigned int v_stack_m290;
    unsigned __int8 v_stack_m293;
    unsigned __int8 v_stack_m294;
    unsigned __int8 v_stack_m295;
    unsigned __int64 v_stack_m296;
    unsigned __int64 v_stack_m297;
    unsigned __int8 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int8 v_stack_m2A7;
    unsigned __int8 v_stack_m2A8;
    unsigned __int64 v_stack_m2B0;
    unsigned __int8 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (688);
    result = (*(unsigned __int64 *)(v_rip + 3527082)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m270 = a8;
    v_stack_m268 = a10;
    result = 0;
    v_stack_m260 = a3;
    v_r12 = 0;
    v_stack_m230 = 0;
    a2 = 0;
    v_stack_m228 = 0;
    v_stack_m290 = (unsigned int)((unsigned int)(a4));
    v_stack_m258 = a11;
    v_stack_m2A0 = 0;
    v_stack_m250 = v_xmm0;
    v_stack_m1E4 = 0;
    v_stack_m240 = v_xmm0;
    result = memset(v_stack_m1C8, a2, 160, a4);
    a2 = 0;
    result = memset(v_stack_m128, a2, 224, a4);
    *(unsigned __int64 *)(a3) = 0;
    result = 0;
    *(unsigned __int16 *)(a11) = 0;
    *(unsigned __int8 *)(a11 + 2) = 0;
    v_rdi = 0;
    v_stack_m298 = 0;
    v_stack_m2A7 = 0;
    v_stack_m294 = 0;
    v_stack_m293 = 0;
    v_stack_m2A8 = 0;
    v_stack_m280 = 0;
    v_stack_m278 = 0;
    v_stack_m295 = 0;
    v_stack_m296 = 0;
    v_stack_m297 = 0;
    v_stack_m220 = v_xmm0;
    v_stack_m200 = 0;
    v_stack_m210 = v_xmm0;
    v_stack_m1F8 = 0;
    result = SeTokenGetNoChildProcessRestricted(0, v_stack_m298, v_stack_m296, v_stack_m297);
    if ((unsigned __int8)(v_stack_m298) != 0) goto loc_00AAD6A1;
    if (v_stack_m297 == 0) goto loc_00AAD7CE;
loc_00AAD6A1:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a6)))) & (2)) == 0) goto loc_00AAD74B;
    v_rsi = 0;
    v_stack_m2C0 = 0;
    v_stack_m2C8 = v_stack_m28C;
    v_stack_m288 = 0;
    v_stack_m28C = 0;
    result = PsReferenceEffectiveToken(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(0x74726853ULL), v_stack_m288, v_stack_m297);
    if (v_stack_m288 != 2) goto loc_00AAD6F8;
    if (v_stack_m28C < 2) goto loc_00AAD734;
loc_00AAD6F8:
    result = SeTokenIsNoChildProcessRestrictionEnforced(result, (unsigned int)(0x74726853ULL), v_stack_m288, v_stack_m297);
    result = (unsigned __int8)(-(result));
    v_rdi = (unsigned int)(((unsigned int)(0xC000049DULL)) & ((unsigned int)(result)));
    if (v_stack_m288 != 1) goto loc_00AAD734;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (584);
    result = ObFastDereferenceObject(a1, result, (unsigned int)(0x74726853ULL), v_stack_m297);
    goto loc_00AAD746;
loc_00AAD734:
    if (result != 0) {
        a2 = 0x74726853ULL;
        a1 = result;
        result = ObfDereferenceObjectWithTag(a1, a2, (unsigned int)(0x74726853ULL), v_stack_m297);
    }
loc_00AAD74B:
    v_rbx = 0;
    if ((*(unsigned int *)(a6 + 8)) != 1) { v_rbx = (unsigned int)(v_rdi); }
    v_rdi = 0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 1532)))) & (1)) == 0) goto loc_00AAD76B;
    if ((*(unsigned __int64 *)(a1 + 1600)) == 0) goto loc_00AAD7CA;
loc_00AAD76B:
    if (!sign_flag) goto loc_00AAD7CA;
    if (v_stack_m296 == 0) goto loc_00AAD77C;
    if ((*(unsigned int *)(a6 + 12)) != 0) goto loc_00AAD7CA;
loc_00AAD77C:
    result = -(*(unsigned __int64 *)(a6 + 24));
    a4 = (v_stack_m297) & (*(unsigned __int64 *)(a6 + 24) + 112);
    a2 = -(*(unsigned __int64 *)(a6 + 24));
    v_rdi = (v_rdi) & (*(unsigned __int64 *)(a6 + 24) + 96);
    result = (unsigned __int8)(-((unsigned __int8)(v_stack_m298)));
    v_stack_m278 = v_rdi;
    a1 = (unsigned int)(-(*(unsigned __int64 *)(a6 + 24) + 112));
    a1 = (unsigned int)((a1) + 1);
    result = EtwTimLogProhibitChildProcessCreation(a1, *(unsigned __int64 *)(a6 + 16), v_rdi, a4);
    v_rdi = 0;
    if ((unsigned __int8)(v_stack_m298) == 0) goto loc_00AAD7CA;
    v_stack_m2A0 = 0;
    goto loc_00AAD9C5;
loc_00AAD7CA:
loc_00AAD7CE:
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(a1, *(unsigned __int64 *)(a6 + 16), v_rdi, a4);
    if ((unsigned int)(result) == 0) goto loc_00AAD84D;
    v_stack_m28C = 0;
    result = RtlQueryElevationFlags(v_stack_m28C, *(unsigned __int64 *)(a6 + 16), v_rdi, a4);
    result = (unsigned __int8)(((unsigned int)(v_stack_m28C)) & (24));
    if (((unsigned __int8)(result)) != 16) goto loc_00AAD84D;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 216) + 40)))) & (4)) == 0) goto loc_00AAD84D;
    if (condition_is_above_or_equal) goto loc_00AAD84D;
    if (condition_is_above_or_equal) goto loc_00AAD84D;
    if ((((unsigned __int8)((unsigned int)(v_stack_m290))) & (2)) == 0) goto loc_00AAD84D;
    v_stack_m295 = 1;
    result = SepLocateTokenIntegrity(a2, *(unsigned __int64 *)(a6 + 16), v_rdi, a4);
    if (result == 0) goto loc_00AAD84D;
    result = RtlSubAuthorityCountSid(*(unsigned __int64 *)(result), *(unsigned __int64 *)(a6 + 16), v_rdi, a4);
    if ((unsigned __int8)(*(unsigned __int8 *)(result)) != 0) goto loc_00AAD83F;
    goto loc_00AAD84D;
loc_00AAD83F:
    result = RtlSubAuthoritySid(*(unsigned __int64 *)(result), *(unsigned __int8 *)(result) - 1, v_rdi, a4);
loc_00AAD84D:
    v_stack_m248 = 0;
    v_stack_m250 = 48;
    v_stack_m230 = v_xmm0;
    v_stack_m238 = 0;
    v_stack_m240 = 0;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(result), *(unsigned __int8 *)(result) - 1, v_rdi, a4);
    if ((unsigned int)(result) == 0) goto loc_00AAD984;
    if (*(unsigned __int64 *)(a6 + 32) == 0) goto loc_00AAD984;
    v_stack_m2C0 = *(unsigned __int64 *)(a6 + 32);
    v_stack_m220 = 48;
    v_stack_m218 = 0;
    v_stack_m208 = 0x600ULL;
    a1 = 0;
    v_stack_m210 = 0;
    v_stack_m200 = v_xmm0;
    v_stack_m2C8 = 0;
    result = SepCreateAppContainerToken(a1, v_stack_m2A0, (unsigned int)(0xF01FFULL), v_stack_m220);
    if (sign_flag) goto loc_00AAD9C0;
loc_00AAD8C6:
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(a1, v_stack_m2A0, (unsigned int)(0xF01FFULL), v_stack_m220);
    if ((unsigned int)(result) == 0) goto loc_00AAD9F9;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m2A0 + 120)))) == ((unsigned int)((unsigned int)(a5)))) goto loc_00AADA65;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m2A0 + 120)))) >= ((unsigned int)((unsigned int)(a5)))) goto loc_00AAD933;
    result = SepDereferenceLowBoxNumberEntry((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m2A0 + 120)))), *(unsigned __int64 *)(v_stack_m2A0 + 1080), (unsigned int)(*(unsigned int *)(v_stack_m2A0 + 120)), v_stack_m220);
    result = SepSetTokenLowboxNumberEntry(v_stack_m2A0, (unsigned int)((unsigned int)((unsigned int)(a5))), *(unsigned __int64 *)(v_stack_m2A0 + 784), v_stack_m220);
    if (sign_flag) goto loc_00AAD9C0;
loc_00AAD933:
    if (*(unsigned __int64 *)(v_stack_m2A0 + 1464) == 0) goto loc_00AADA65;
    v_rbx = (unsigned int)((unsigned int)(result));
    if (*(unsigned __int64 *)(v_stack_m2A0 + 1176) != 0) {
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2A0 + 1464) + 48);
        a2 = (unsigned int)((unsigned int)(a5));
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2A0 + 1176) + 16);
        result = SepSetTokenAntiTamperEntry(v_stack_m2A0, a2, a3, a4);
        a1 = v_stack_m2A0;
        v_rbx = (unsigned int)(result);
    }
    result = SepDereferenceAntiTamperEntry((unsigned int)(*(unsigned int *)(a1 + 120)), *(unsigned __int64 *)(v_stack_m2A0 + 1464), a3, a4);
    goto loc_00AADA5A;
loc_00AAD984:
    v_stack_m2B0 = v_stack_m2A0;
    v_stack_m2B8 = 1;
    a3 = 0;
    v_stack_m2C0 = (unsigned __int8)((unsigned int)(a5));
    v_stack_m2C8 = (unsigned int)((unsigned int)(a5));
    result = SepDuplicateToken(a2, v_stack_m250, a3, 1);
    if (!sign_flag) goto loc_00AAD8C6;
    v_stack_m2A0 = (unsigned int)(a5);
loc_00AAD9C0:
loc_00AAD9C5:
    v_r14 = 0;
loc_00AAD9C8:
    if (v_stack_m2A0 != 0) {
        result = ObfDereferenceObject(v_stack_m2A0, v_stack_m250, a3, 1);
    }
    if ((unsigned __int8)(v_stack_m2A8) == 0) goto loc_00AADE20;
loc_00AAD9E0:
    if (v_stack_m2A7 == 0) goto loc_00AADE1B;
    result = SepDeleteAccessState(v_stack_m1C8, v_stack_m250, a3, 1);
    goto loc_00AADE20;
loc_00AAD9F9:
    if (v_stack_m2A7 >= 0) goto loc_00AADA65;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1C8 + 120)))) == ((unsigned int)(v_stack_m2A8))) goto loc_00AADA65;
    result = SepDereferenceLowBoxNumberEntry((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1C8 + 120)))), *(unsigned __int64 *)(v_stack_m1C8 + 1080), a3, 1);
    a4 = 0;
    a3 = 0;
    result = SepSetTokenSessionById(v_stack_m2A0, (unsigned int)((unsigned int)(v_stack_m2A8)), a3, a4);
    *(unsigned int *)(v_stack_m2A0 + 120) = (unsigned int)(v_stack_m2A8);
    result = SepSetTokenLowboxNumber(v_stack_m2A0, *(unsigned __int64 *)(v_stack_m2A0 + 784), a3, a4);
loc_00AADA5A:
    if (sign_flag) goto loc_00AAD9C0;
loc_00AADA65:
    a4 = 0;
    a3 = 0;
    result = SepSetTokenSessionById(v_stack_m2A0, (unsigned int)((unsigned int)(v_stack_m2A8)), a3, a4);
    *(unsigned int *)(v_stack_m2A0 + 120) = (unsigned int)(v_stack_m2A8);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a6)))) & (1)) == 0) goto loc_00AADAB5;
    result = (unsigned int)(*(unsigned int *)(a6));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a6)))) & (4)) != 0) {
        result = v_stack_m2A0;
    }
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = SepSetTokenBnoIsolation(v_stack_m2A0, a2, a3, a4);
    if (sign_flag) goto loc_00AAD9C0;
    a3 = 0;
    v_stack_m2B8 = v_stack_m293;
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m290)) & (2));
    v_stack_m2C0 = v_stack_m294;
    v_stack_m2C8 = (unsigned int)((unsigned int)(*(unsigned int *)(a6 + 4)));
    result = SepDesktopAppxSubProcessToken(v_stack_m2A0, a1, a3, a4);
    if (sign_flag) goto loc_00AAD9C0;
    result = (unsigned int)(-((unsigned int)((unsigned int)(v_rsi))));
    a1 = (v_stack_m2A0) & (0);
    result = SepMandatorySubProcessToken(a1, v_stack_m2A0, a1, v_stack_m280);
    v_r14 = 0;
    if (sign_flag) goto loc_00AADE13;
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(a1, v_stack_m2A0, a1, v_stack_m280);
    if ((unsigned int)(result) == 0) goto loc_00AADBB4;
    if (v_stack_m295 == 0) goto loc_00AADBB4;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result))) == 0) goto loc_00AADBB4;
    result = SepLocateTokenIntegrity(v_stack_m2A0, v_stack_m2A0, a1, v_stack_m280);
    if (result == 0) goto loc_00AADBB4;
    result = RtlSubAuthorityCountSid(*(unsigned __int64 *)(result), v_stack_m2A0, a1, v_stack_m280);
    if ((unsigned __int8)(*(unsigned __int8 *)(result)) != 0) goto loc_00AADB7B;
    goto loc_00AADB88;
loc_00AADB7B:
    result = RtlSubAuthoritySid(*(unsigned __int64 *)(result), *(unsigned __int8 *)(result) - 1, a1, v_stack_m280);
loc_00AADB88:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(result))))) goto loc_00AADBB4;
    a2 = 0;
    result = RtlSubAuthoritySid(*(unsigned __int64 *)(result), a2, a1, v_stack_m280);
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result)))) < ((unsigned int)((unsigned int)(0x2000ULL)))) goto loc_00AADBB9;
    goto loc_00AADBB9;
loc_00AADBB4:
loc_00AADBB9:
    result = SepSetTrustLevelForProcessToken(v_stack_m2A0, a1, v_stack_m2A7, v_stack_m280);
    if (sign_flag) goto loc_00AADE13;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3908165))) & (3));
    if (((unsigned __int8)(result)) != 3) goto loc_00AADBF6;
    result = SepSetProcessUniqueAttribute(v_stack_m2A0, a1, v_stack_m2A7, v_stack_m280);
    if (sign_flag) goto loc_00AADE13;
loc_00AADBF6:
    if (((*(unsigned int *)(v_stack_m2A0 + 200)) & (0x4000ULL)) == 0) goto loc_00AADC2A;
    if ((((unsigned __int8)((unsigned int)(a7))) & (1)) == 0) goto loc_00AADC2A;
    result = SepSetTokenAllApplicationPackagesPolicy(v_stack_m2A0, (unsigned int)(a7), v_stack_m2A0, v_stack_m280);
    if (sign_flag) goto loc_00AADE13;
loc_00AADC2A:
    if (v_stack_m270 != 0) {
        a2 = a9;
        a4 = 0;
        a1 = v_stack_m270;
        result = SepAddTokenOriginClaim(a1, a2, v_stack_m2A0, a4);
    }
    result = Feature_AgentId2__private_IsEnabledDeviceUsageNoInline(a1, a2, v_stack_m2A0, a4);
    if ((unsigned int)(result) == 0) goto loc_00AADCB8;
    v_stack_m280 = 0;
    result = SepGetAgentIdFromOriginClaim(v_stack_m270, (unsigned int)(a9), v_stack_m280, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AADCB8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m2A0 + 1168)))) & (2)) != 0) goto loc_00AADCBD;
    if (v_stack_m280 == 0) goto loc_00AADC90;
    if ((*(unsigned __int16 *)(v_stack_m280)) <= 0) goto loc_00AADC90;
    if (v_stack_m280 == 0) goto loc_00AADCBD;
    goto loc_00AADC9D;
loc_00AADC90:
    if (v_stack_m278 == 0) goto loc_00AADCBD;
loc_00AADC9D:
    result = SepAddAgentIdClaimToToken(v_stack_m2A0, v_stack_m278, v_stack_m280, a4);
    if (sign_flag) goto loc_00AADE13;
loc_00AADCB8:
loc_00AADCBD:
    if (v_stack_m268 == 0) goto loc_00AADCED;
    v_stack_m2C8 = *(unsigned __int64 *)(v_stack_m268 + 24);
    result = SepSetTokenBnoIsolation(v_stack_m2A0, *(unsigned __int8 *)(v_stack_m268 + 32), v_stack_m268, (unsigned int)(*(unsigned int *)(v_stack_m268 + 16)));
    if (sign_flag) goto loc_00AADE13;
loc_00AADCED:
    if ((unsigned int)(v_rsi) == 0) goto loc_00AADCF6;
    if (v_stack_m280 != 0) {
        v_stack_m2A7 = 1;
    }
    if (v_stack_m2A7 == 0) goto loc_00AADD47;
    v_stack_m1E0 = v_stack_m2A0;
    a4 = 0;
    v_stack_m1F0 = 0;
    v_stack_m1E8 = 0;
    v_stack_m2C8 = 0;
    v_stack_m1D8 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 464);
    result = SepCreateAccessStateFromSubjectContext(v_stack_m1F0, v_stack_m1C8, v_stack_m128, a4);
    goto loc_00AADD5D;
loc_00AADD47:
    a4 = 0;
    a3 = 0;
    result = SeCreateAccessState(v_stack_m1C8, v_stack_m128, a3, a4);
loc_00AADD5D:
    v_stack_m2B8 = 0;
    a4 = 0;
    v_stack_m2C0 = 0;
    a3 = 0;
    v_stack_m2C8 = 0;
    result = ObInsertObjectEx(v_stack_m2A0, v_stack_m1C8, a3, a4);
    if (!sign_flag) goto loc_00AADD93;
    v_stack_m2A0 = 0;
    goto loc_00AAD9C8;
loc_00AADD93:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(v_stack_m2A0, v_stack_m1C8, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00AADDC6;
    if (*(unsigned __int64 *)(a6 + 32) == 0) goto loc_00AADDC6;
    result = SepAppendAceToTokenObjectAcl(v_stack_m2A0, (unsigned int)(0xF01FFULL), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 32) + 8) + 16), a4);
    if (sign_flag) goto loc_00AAD9C8;
loc_00AADDC6:
    result = SepFinalizeTokenAcls(v_stack_m2A0, (unsigned int)(0xF01FFULL), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 32) + 8) + 16), a4);
    a1 = (unsigned __int8)(((unsigned int)(v_stack_m290)) & (1));
    *(unsigned __int8 *)(v_stack_m2A0 + 204) = (unsigned __int8)(a1);
    *(unsigned __int64 *)(v_stack_m260) = v_stack_m2A0;
    *(unsigned __int8 *)(v_stack_m258) = (unsigned __int8)(v_stack_m2A7);
    *(unsigned __int8 *)(v_stack_m258 + 1) = (unsigned __int8)(v_stack_m294);
    *(unsigned __int8 *)(v_stack_m258 + 2) = (unsigned __int8)(v_stack_m293);
    if (!sign_flag) goto loc_00AAD9E0;
    goto loc_00AAD9C8;
loc_00AADE13:
    goto loc_00AAD9C8;
loc_00AADE1B:
    result = SeDeleteAccessState(v_stack_m258, (unsigned int)(0xF01FFULL), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 32) + 8) + 16), a4);
loc_00AADE20:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(0xF01FFULL), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 32) + 8) + 16), a4);
    v_rsp = (v_rsp) + (688);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SeSubProcessToken(void *Arg1, void *Arg2, void *Arg3, int32_t Arg4, uint32_t Arg5, void *Arg6, uint32_t Arg7, int64_t Arg8, uint32_t Arg9, int64_t Arg10, void *Arg11)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg11 = (uint8_t *)Arg11;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m128;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint32_t v_stack_m1E4;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint32_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint32_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint32_t v_stack_m228;
    uint64_t v_stack_m230;
    uint32_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m280;
    uint64_t v_stack_m288;
    uint64_t v_stack_m28C;
    uint32_t v_stack_m290;
    uint8_t v_stack_m293;
    uint8_t v_stack_m294;
    uint8_t v_stack_m295;
    uint64_t v_stack_m296;
    uint64_t v_stack_m297;
    uint8_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint8_t v_stack_m2A7;
    uint8_t v_stack_m2A8;
    uint64_t v_stack_m2B0;
    uint8_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m48;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (688);
    result = (*(uint64_t *)(v_rip + 0x35D1AA)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m270 = Arg8;
    v_stack_m268 = Arg10;
    result = 0;
    v_stack_m260 = Arg3;
    local_r12 = 0;
    v_stack_m230 = 0;
    Arg2 = 0;
    v_stack_m228 = 0;
    v_stack_m290 = (uint32_t)((uint32_t)(Arg4));
    v_stack_m258 = Arg11;
    v_stack_m2A0 = 0;
    v_stack_m250 = v_xmm0;
    v_stack_m1E4 = 0;
    v_stack_m240 = v_xmm0;
    result = memset(v_stack_m1C8, Arg2, 160, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m128, Arg2, 224, Arg4);
    *(uint64_t *)(arg3) = 0;
    result = 0;
    *(uint16_t *)(arg11) = 0;
    *(uint8_t *)(arg11 + 0x2) = 0;
    local_rdi = 0;
    v_stack_m298 = 0;
    v_stack_m2A7 = 0;
    v_stack_m294 = 0;
    v_stack_m293 = 0;
    v_stack_m2A8 = 0;
    v_stack_m280 = 0;
    v_stack_m278 = 0;
    v_stack_m295 = 0;
    v_stack_m296 = 0;
    v_stack_m297 = 0;
    v_stack_m220 = v_xmm0;
    v_stack_m200 = 0;
    v_stack_m210 = v_xmm0;
    v_stack_m1F8 = 0;
    result = SeTokenGetNoChildProcessRestricted(0, v_stack_m298, v_stack_m296, v_stack_m297);
    if ((uint8_t)(v_stack_m298) != 0) goto loc_00AAD6A1;
    if (v_stack_m297 == 0) goto loc_00AAD7CE;
loc_00AAD6A1:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg6)))) & (2)) == 0) goto loc_00AAD74B;
    local_rsi = 0;
    v_stack_m2C0 = 0;
    v_stack_m2C8 = v_stack_m28C;
    v_stack_m288 = 0;
    v_stack_m28C = 0;
    result = PsReferenceEffectiveToken(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(0x74726853ULL), v_stack_m288, v_stack_m297);
    if (v_stack_m288 != 2) goto loc_00AAD6F8;
    if (v_stack_m28C < 2) goto loc_00AAD734;
loc_00AAD6F8:
    result = SeTokenIsNoChildProcessRestrictionEnforced(result, (uint32_t)(0x74726853ULL), v_stack_m288, v_stack_m297);
    result = (uint8_t)(-(result));
    local_rdi = (uint32_t)(((uint32_t)(0xC000049DULL)) & ((uint32_t)(result)));
    if (v_stack_m288 != 1) goto loc_00AAD734;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (584);
    result = ObFastDereferenceObject(Arg1, result, (uint32_t)(0x74726853ULL), v_stack_m297);
    goto loc_00AAD746;
loc_00AAD734:
    if (result != 0) {
        Arg2 = 0x74726853ULL;
        Arg1 = result;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, (uint32_t)(0x74726853ULL), v_stack_m297);
    }
loc_00AAD74B:
    local_rbx = 0;
    if ((*(uint32_t *)(arg6 + 0x8)) != 1) { local_rbx = (uint32_t)(local_rdi); }
    local_rdi = 0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x5FC)))) & (1)) == 0) goto loc_00AAD76B;
    if ((*(uint64_t *)(arg1 + 0x640)) == 0) goto loc_00AAD7CA;
loc_00AAD76B:
    if (!sign_flag) goto loc_00AAD7CA;
    if (v_stack_m296 == 0) goto loc_00AAD77C;
    if ((*(uint32_t *)(arg6 + 0xC)) != 0) goto loc_00AAD7CA;
loc_00AAD77C:
    result = -(*(uint64_t *)(arg6 + 0x18));
    Arg4 = (v_stack_m297) & (*(uint64_t *)(arg6 + 0x18) + 112);
    Arg2 = -(*(uint64_t *)(arg6 + 0x18));
    local_rdi = (local_rdi) & (*(uint64_t *)(arg6 + 0x18) + 96);
    result = (uint8_t)(-((uint8_t)(v_stack_m298)));
    v_stack_m278 = local_rdi;
    Arg1 = (uint32_t)(-(*(uint64_t *)(arg6 + 0x18) + 112));
    Arg1 = (uint32_t)((Arg1) + 1);
    result = EtwTimLogProhibitChildProcessCreation(Arg1, *(uint64_t *)(arg6 + 0x10), local_rdi, Arg4);
    local_rdi = 0;
    if ((uint8_t)(v_stack_m298) == 0) goto loc_00AAD7CA;
    v_stack_m2A0 = 0;
    goto loc_00AAD9C5;
loc_00AAD7CA:
loc_00AAD7CE:
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(Arg1, *(uint64_t *)(arg6 + 0x10), local_rdi, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00AAD84D;
    v_stack_m28C = 0;
    result = RtlQueryElevationFlags(v_stack_m28C, *(uint64_t *)(arg6 + 0x10), local_rdi, Arg4);
    result = (uint8_t)(((uint32_t)(v_stack_m28C)) & (24));
    if (((uint8_t)(result)) != 16) goto loc_00AAD84D;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0xD8) + 0x28)))) & (4)) == 0) goto loc_00AAD84D;
    if (condition_is_above_or_equal) goto loc_00AAD84D;
    if (condition_is_above_or_equal) goto loc_00AAD84D;
    if ((((uint8_t)((uint32_t)(v_stack_m290))) & (2)) == 0) goto loc_00AAD84D;
    v_stack_m295 = 1;
    result = SepLocateTokenIntegrity(Arg2, *(uint64_t *)(arg6 + 0x10), local_rdi, Arg4);
    if (result == 0) goto loc_00AAD84D;
    result = RtlSubAuthorityCountSid(*(uint64_t *)(result), *(uint64_t *)(arg6 + 0x10), local_rdi, Arg4);
    if ((uint8_t)(*(uint8_t *)(result)) != 0) goto loc_00AAD83F;
    goto loc_00AAD84D;
loc_00AAD83F:
    result = RtlSubAuthoritySid(*(uint64_t *)(result), *(uint8_t *)(result) - 1, local_rdi, Arg4);
loc_00AAD84D:
    v_stack_m248 = 0;
    v_stack_m250 = 48;
    v_stack_m230 = v_xmm0;
    v_stack_m238 = 0;
    v_stack_m240 = 0;
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(result), *(uint8_t *)(result) - 1, local_rdi, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00AAD984;
    if (*(uint64_t *)(arg6 + 0x20) == 0) goto loc_00AAD984;
    v_stack_m2C0 = *(uint64_t *)(arg6 + 0x20);
    v_stack_m220 = 48;
    v_stack_m218 = 0;
    v_stack_m208 = 0x600ULL;
    Arg1 = 0;
    v_stack_m210 = 0;
    v_stack_m200 = v_xmm0;
    v_stack_m2C8 = 0;
    result = SepCreateAppContainerToken(Arg1, v_stack_m2A0, (uint32_t)(0xF01FFULL), v_stack_m220);
    if (sign_flag) goto loc_00AAD9C0;
loc_00AAD8C6:
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(Arg1, v_stack_m2A0, (uint32_t)(0xF01FFULL), v_stack_m220);
    if ((uint32_t)(result) == 0) goto loc_00AAD9F9;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m2A0 + 0x78)))) == ((uint32_t)((uint32_t)(Arg5)))) goto loc_00AADA65;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m2A0 + 0x78)))) >= ((uint32_t)((uint32_t)(Arg5)))) goto loc_00AAD933;
    result = SepDereferenceLowBoxNumberEntry((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m2A0 + 0x78)))), *(uint64_t *)(v_stack_m2A0 + 0x438), (uint32_t)(*(uint32_t *)(v_stack_m2A0 + 0x78)), v_stack_m220);
    result = SepSetTokenLowboxNumberEntry(v_stack_m2A0, (uint32_t)((uint32_t)((uint32_t)(Arg5))), *(uint64_t *)(v_stack_m2A0 + 0x310), v_stack_m220);
    if (sign_flag) goto loc_00AAD9C0;
loc_00AAD933:
    if (*(uint64_t *)(v_stack_m2A0 + 0x5B8) == 0) goto loc_00AADA65;
    local_rbx = (uint32_t)((uint32_t)(result));
    if (*(uint64_t *)(v_stack_m2A0 + 0x498) != 0) {
        Arg4 = *(uint64_t *)(*(uint64_t *)(v_stack_m2A0 + 0x5B8) + 0x30);
        Arg2 = (uint32_t)((uint32_t)(Arg5));
        Arg3 = *(uint64_t *)(*(uint64_t *)(v_stack_m2A0 + 0x498) + 0x10);
        result = SepSetTokenAntiTamperEntry(v_stack_m2A0, Arg2, Arg3, Arg4);
        Arg1 = v_stack_m2A0;
        local_rbx = (uint32_t)(result);
    }
    result = SepDereferenceAntiTamperEntry((uint32_t)(*(uint32_t *)(arg1 + 0x78)), *(uint64_t *)(v_stack_m2A0 + 0x5B8), Arg3, Arg4);
    goto loc_00AADA5A;
loc_00AAD984:
    v_stack_m2B0 = v_stack_m2A0;
    v_stack_m2B8 = 1;
    Arg3 = 0;
    v_stack_m2C0 = (uint8_t)((uint32_t)(Arg5));
    v_stack_m2C8 = (uint32_t)((uint32_t)(Arg5));
    result = SepDuplicateToken(Arg2, v_stack_m250, Arg3, 1);
    if (!sign_flag) goto loc_00AAD8C6;
    v_stack_m2A0 = (uint32_t)(Arg5);
loc_00AAD9C0:
loc_00AAD9C5:
    local_r14 = 0;
loc_00AAD9C8:
    if (v_stack_m2A0 != 0) {
        result = ObfDereferenceObject(v_stack_m2A0, v_stack_m250, Arg3, 1);
    }
    if ((uint8_t)(v_stack_m2A8) == 0) goto loc_00AADE20;
loc_00AAD9E0:
    if (v_stack_m2A7 == 0) goto loc_00AADE1B;
    result = SepDeleteAccessState(v_stack_m1C8, v_stack_m250, Arg3, 1);
    goto loc_00AADE20;
loc_00AAD9F9:
    if (v_stack_m2A7 >= 0) goto loc_00AADA65;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1C8 + 0x78)))) == ((uint32_t)(v_stack_m2A8))) goto loc_00AADA65;
    result = SepDereferenceLowBoxNumberEntry((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1C8 + 0x78)))), *(uint64_t *)(v_stack_m1C8 + 0x438), Arg3, 1);
    Arg4 = 0;
    Arg3 = 0;
    result = SepSetTokenSessionById(v_stack_m2A0, (uint32_t)((uint32_t)(v_stack_m2A8)), Arg3, Arg4);
    *(uint32_t *)(v_stack_m2A0 + 0x78) = (uint32_t)(v_stack_m2A8);
    result = SepSetTokenLowboxNumber(v_stack_m2A0, *(uint64_t *)(v_stack_m2A0 + 0x310), Arg3, Arg4);
loc_00AADA5A:
    if (sign_flag) goto loc_00AAD9C0;
loc_00AADA65:
    Arg4 = 0;
    Arg3 = 0;
    result = SepSetTokenSessionById(v_stack_m2A0, (uint32_t)((uint32_t)(v_stack_m2A8)), Arg3, Arg4);
    *(uint32_t *)(v_stack_m2A0 + 0x78) = (uint32_t)(v_stack_m2A8);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg6)))) & (1)) == 0) goto loc_00AADAB5;
    result = (uint32_t)(*(uint32_t *)(arg6));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg6)))) & (4)) != 0) {
        result = v_stack_m2A0;
    }
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = SepSetTokenBnoIsolation(v_stack_m2A0, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00AAD9C0;
    Arg3 = 0;
    v_stack_m2B8 = v_stack_m293;
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m290)) & (2));
    v_stack_m2C0 = v_stack_m294;
    v_stack_m2C8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg6 + 0x4)));
    result = SepDesktopAppxSubProcessToken(v_stack_m2A0, Arg1, Arg3, Arg4);
    if (sign_flag) goto loc_00AAD9C0;
    result = (uint32_t)(-((uint32_t)((uint32_t)(local_rsi))));
    Arg1 = (v_stack_m2A0) & (0);
    result = SepMandatorySubProcessToken(Arg1, v_stack_m2A0, Arg1, v_stack_m280);
    local_r14 = 0;
    if (sign_flag) goto loc_00AADE13;
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(Arg1, v_stack_m2A0, Arg1, v_stack_m280);
    if ((uint32_t)(result) == 0) goto loc_00AADBB4;
    if (v_stack_m295 == 0) goto loc_00AADBB4;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result))) == 0) goto loc_00AADBB4;
    result = SepLocateTokenIntegrity(v_stack_m2A0, v_stack_m2A0, Arg1, v_stack_m280);
    if (result == 0) goto loc_00AADBB4;
    result = RtlSubAuthorityCountSid(*(uint64_t *)(result), v_stack_m2A0, Arg1, v_stack_m280);
    if ((uint8_t)(*(uint8_t *)(result)) != 0) goto loc_00AADB7B;
    goto loc_00AADB88;
loc_00AADB7B:
    result = RtlSubAuthoritySid(*(uint64_t *)(result), *(uint8_t *)(result) - 1, Arg1, v_stack_m280);
loc_00AADB88:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(result))))) goto loc_00AADBB4;
    Arg2 = 0;
    result = RtlSubAuthoritySid(*(uint64_t *)(result), Arg2, Arg1, v_stack_m280);
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result)))) < ((uint32_t)((uint32_t)(0x2000ULL)))) goto loc_00AADBB9;
    goto loc_00AADBB9;
loc_00AADBB4:
loc_00AADBB9:
    result = SepSetTrustLevelForProcessToken(v_stack_m2A0, Arg1, v_stack_m2A7, v_stack_m280);
    if (sign_flag) goto loc_00AADE13;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x3BA245))) & (3));
    if (((uint8_t)(result)) != 3) goto loc_00AADBF6;
    result = SepSetProcessUniqueAttribute(v_stack_m2A0, Arg1, v_stack_m2A7, v_stack_m280);
    if (sign_flag) goto loc_00AADE13;
loc_00AADBF6:
    if (((*(uint32_t *)(v_stack_m2A0 + 0xC8)) & (0x4000ULL)) == 0) goto loc_00AADC2A;
    if ((((uint8_t)((uint32_t)(Arg7))) & (1)) == 0) goto loc_00AADC2A;
    result = SepSetTokenAllApplicationPackagesPolicy(v_stack_m2A0, (uint32_t)(Arg7), v_stack_m2A0, v_stack_m280);
    if (sign_flag) goto loc_00AADE13;
loc_00AADC2A:
    if (v_stack_m270 != 0) {
        Arg2 = Arg9;
        Arg4 = 0;
        Arg1 = v_stack_m270;
        result = SepAddTokenOriginClaim(Arg1, Arg2, v_stack_m2A0, Arg4);
    }
    result = Feature_AgentId2__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, v_stack_m2A0, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00AADCB8;
    v_stack_m280 = 0;
    result = SepGetAgentIdFromOriginClaim(v_stack_m270, (uint32_t)(Arg9), v_stack_m280, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00AADCB8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m2A0 + 0x490)))) & (2)) != 0) goto loc_00AADCBD;
    if (v_stack_m280 == 0) goto loc_00AADC90;
    if ((*(uint16_t *)(v_stack_m280)) <= 0) goto loc_00AADC90;
    if (v_stack_m280 == 0) goto loc_00AADCBD;
    goto loc_00AADC9D;
loc_00AADC90:
    if (v_stack_m278 == 0) goto loc_00AADCBD;
loc_00AADC9D:
    result = SepAddAgentIdClaimToToken(v_stack_m2A0, v_stack_m278, v_stack_m280, Arg4);
    if (sign_flag) goto loc_00AADE13;
loc_00AADCB8:
loc_00AADCBD:
    if (v_stack_m268 == 0) goto loc_00AADCED;
    v_stack_m2C8 = *(uint64_t *)(v_stack_m268 + 0x18);
    result = SepSetTokenBnoIsolation(v_stack_m2A0, *(uint8_t *)(v_stack_m268 + 0x20), v_stack_m268, (uint32_t)(*(uint32_t *)(v_stack_m268 + 0x10)));
    if (sign_flag) goto loc_00AADE13;
loc_00AADCED:
    if ((uint32_t)(local_rsi) == 0) goto loc_00AADCF6;
    if (v_stack_m280 != 0) {
        v_stack_m2A7 = 1;
    }
    if (v_stack_m2A7 == 0) goto loc_00AADD47;
    v_stack_m1E0 = v_stack_m2A0;
    Arg4 = 0;
    v_stack_m1F0 = 0;
    v_stack_m1E8 = 0;
    v_stack_m2C8 = 0;
    v_stack_m1D8 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1D0);
    result = SepCreateAccessStateFromSubjectContext(v_stack_m1F0, v_stack_m1C8, v_stack_m128, Arg4);
    goto loc_00AADD5D;
loc_00AADD47:
    Arg4 = 0;
    Arg3 = 0;
    result = SeCreateAccessState(v_stack_m1C8, v_stack_m128, Arg3, Arg4);
loc_00AADD5D:
    v_stack_m2B8 = 0;
    Arg4 = 0;
    v_stack_m2C0 = 0;
    Arg3 = 0;
    v_stack_m2C8 = 0;
    result = ObInsertObjectEx(v_stack_m2A0, v_stack_m1C8, Arg3, Arg4);
    if (!sign_flag) goto loc_00AADD93;
    v_stack_m2A0 = 0;
    goto loc_00AAD9C8;
loc_00AADD93:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(v_stack_m2A0, v_stack_m1C8, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00AADDC6;
    if (*(uint64_t *)(arg6 + 0x20) == 0) goto loc_00AADDC6;
    result = SepAppendAceToTokenObjectAcl(v_stack_m2A0, (uint32_t)(0xF01FFULL), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + 0x20) + 0x8) + 0x10), Arg4);
    if (sign_flag) goto loc_00AAD9C8;
loc_00AADDC6:
    result = SepFinalizeTokenAcls(v_stack_m2A0, (uint32_t)(0xF01FFULL), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + 0x20) + 0x8) + 0x10), Arg4);
    Arg1 = (uint8_t)(((uint32_t)(v_stack_m290)) & (1));
    *(uint8_t *)(v_stack_m2A0 + 0xCC) = (uint8_t)(Arg1);
    *(uint64_t *)(v_stack_m260) = v_stack_m2A0;
    *(uint8_t *)(v_stack_m258) = (uint8_t)(v_stack_m2A7);
    *(uint8_t *)(v_stack_m258 + 0x1) = (uint8_t)(v_stack_m294);
    *(uint8_t *)(v_stack_m258 + 0x2) = (uint8_t)(v_stack_m293);
    if (!sign_flag) goto loc_00AAD9E0;
    goto loc_00AAD9C8;
loc_00AADE13:
    goto loc_00AAD9C8;
loc_00AADE1B:
    result = SeDeleteAccessState(v_stack_m258, (uint32_t)(0xF01FFULL), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + 0x20) + 0x8) + 0x10), Arg4);
loc_00AADE20:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(0xF01FFULL), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + 0x20) + 0x8) + 0x10), Arg4);
    local_rsp = (local_rsp) + (688);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x5FC` | `32` | `R` |
| `Arg1` | `+ 0x640` | `64` | `R` |
| `Arg2` | `+ 0xC8` | `32` | `R` |
| `Arg2` | `+ 0xD8` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg6` | `+ 0x0` | `32` | `R` |
| `Arg6` | `+ 0x4` | `32` | `R` |
| `Arg6` | `+ 0x8` | `32` | `R` |
| `Arg6` | `+ 0xC` | `32` | `R` |
| `Arg6` | `+ 0x10` | `64` | `R` |
| `Arg6` | `+ 0x18` | `64` | `R` |
| `Arg6` | `+ 0x20` | `64` | `R` |
| `Arg11` | `+ 0x0` | `16` | `W` |
| `Arg11` | `+ 0x2` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AAD570&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
