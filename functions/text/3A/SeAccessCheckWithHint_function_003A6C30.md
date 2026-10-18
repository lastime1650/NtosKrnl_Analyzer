# SeAccessCheckWithHint

- RVA: `0x003A6C30`–`0x003A779E` (길이 `2,926` bytes)
- VA: `0x00000001403A6C30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00089B78`
- 디코드: `792`개 명령, `2,926/2,926` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **38**; 고유 호출 대상: **26**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x003A6D86` → [SeLockSubjectContext](../../page/8C/SeLockSubjectContext_function_008C64C0.md) (function, `0x008C64C0`)
- `0x003A6DA7` → [SepTrustLevelCheck](../3E/SepTrustLevelCheck_function_003ED7E0.md) (function, `0x003ED7E0`)
- `0x003A6E06` → [SepFilterCheck](../30/SepFilterCheck_function_00301B60.md) (function, `0x00301B60`)
- `0x003A6EDE` → [SepMandatoryIntegrityCheck](../25/SepMandatoryIntegrityCheck_function_0025F4E0.md) (function, `0x0025F4E0`)
- `0x003A6EF4` → [SepMandatoryToDiscretionary](../41/SepMandatoryToDiscretionary_function_0041BF40.md) (function, `0x0041BF40`)
- `0x003A6F49` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x003A6F73` → [SepMandatoryAccessCheck](../60/SepMandatoryAccessCheck_function_00608480.md) (function, `0x00608480`)
- `0x003A6F93` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x003A6FF0` → [SepGetScopedPolicySid](SepGetScopedPolicySid_function_003A59AC.md) (function, `0x003A59AC`)
- `0x003A7001` → [SepRmReferenceFindCap](SepRmReferenceFindCap_function_003A58EC.md) (function, `0x003A58EC`)
- `0x003A7063` → [SepTokenIsOwner](../3E/SepTokenIsOwner_function_003E5D60.md) (function, `0x003E5D60`)
- `0x003A70AA` → [RtlpOwnerAcesPresent](../3F/RtlpOwnerAcesPresent_function_003FB2F0.md) (function, `0x003FB2F0`)
- `0x003A70F0` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x003A713A` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x003A71EA` → [SepAccessCheck](../3D/SepAccessCheck_function_003D0E54.md) (function, `0x003D0E54`)
- `0x003A7264` → [AuthzBasepInitializeResourceClaimsFromSacl](../30/AuthzBasepInitializeResourceClaimsFromSacl_function_00302E84.md) (function, `0x00302E84`)
- `0x003A72F5` → [AuthzBasepEvaluateAceCondition](../2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (function, `0x002FEBD0`)
- `0x003A739C` → [AuthzBasepEvaluateAceCondition](../2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (function, `0x002FEBD0`)
- `0x003A73D1` → [SepBuildCapeSecurityDescriptor](../4D/SepBuildCapeSecurityDescriptor_function_004D9E38.md) (function, `0x004D9E38`)
- `0x003A7487` → [SepAccessCheck](../3D/SepAccessCheck_function_003D0E54.md) (function, `0x003D0E54`)
- `0x003A74E0` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x003A74E9` → [SepRmDereferenceCap](../4B/SepRmDereferenceCap_function_004B1E9C.md) (function, `0x004B1E9C`)
- `0x003A74FB` → [SepFreeResourceInfo](../30/SepFreeResourceInfo_function_003019F0.md) (function, `0x003019F0`)
- `0x003A756C` → [SepConstrainByMandatory](../43/SepConstrainByMandatory_function_0043FC70.md) (function, `0x0043FC70`)
- `0x003A75EC` → [SepConstrainByConstraintMask](../43/SepConstrainByConstraintMask_function_0043FDE0.md) (function, `0x0043FDE0`)
- `0x003A7613` → [SepConstrainByConstraintMask](../43/SepConstrainByConstraintMask_function_0043FDE0.md) (function, `0x0043FDE0`)
- `0x003A7618` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x003A7677` → [SepLocateTokenTrustLevel](../3E/SepLocateTokenTrustLevel_function_003EDA40.md) (function, `0x003EDA40`)
- `0x003A76A2` → [SeLogAccessFailure](../44/SeLogAccessFailure_function_00448550.md) (function, `0x00448550`)
- `0x003A76C7` → [SepLpacCausedAccessFailure](../46/SepLpacCausedAccessFailure_function_00462484.md) (function, `0x00462484`)
- `0x003A76D0` → [SepLogLpacAccessFailure](../41/SepLogLpacAccessFailure_function_0041E8A0.md) (function, `0x0041E8A0`)
- `0x003A76E2` → [SepRmDereferenceCap](../4B/SepRmDereferenceCap_function_004B1E9C.md) (function, `0x004B1E9C`)
- `0x003A76EF` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x003A76F8` → [SepFreeResourceInfo](../30/SepFreeResourceInfo_function_003019F0.md) (function, `0x003019F0`)
- `0x003A773A` → [SepLocateTokenTrustLevel](../3E/SepLocateTokenTrustLevel_function_003EDA40.md) (function, `0x003EDA40`)
- `0x003A775D` → [SeLogAccessFailure](../44/SeLogAccessFailure_function_00448550.md) (function, `0x00448550`)
- `0x003A776A` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x003A777D` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [ExCpuSetResourceManagerAccessCheck](ExCpuSetResourceManagerAccessCheck_function_003A5444.md) at `0x003A54EC`
- [RtlCheckTokenCapability](RtlCheckTokenCapability_function_003A5520.md) at `0x003A5772`
- [RtlCheckTokenMembershipEx](RtlCheckTokenMembershipEx_function_003A5A30.md) at `0x003A5C09`
- [SeAccessCheckFromState](SeAccessCheckFromState_function_003A6650.md) at `0x003A6758`
- [SeAccessCheckFromStateEx](SeAccessCheckFromStateEx_function_003A6B20.md) at `0x003A6BA9`
- [SeAccessCheck](SeAccessCheck_function_003A6BC0.md) at `0x003A6C1D`
- [sub_006EF3AA](../6E/Unknown_function_006EF3AA.md) at `0x006EF4A3`
- [PspCheckCpuPartitionCreateAccess](../../page/78/PspCheckCpuPartitionCreateAccess_function_00784130.md) at `0x00784200`
- [ExCheckFullProcessInformationAccess](../../page/95/ExCheckFullProcessInformationAccess_function_0095D93C.md) at `0x0095D9E4`
- [ObpVerifyAccessToBoundaryEntry](../../page/A5/ObpVerifyAccessToBoundaryEntry_function_00A5E500.md) at `0x00A5E690`
- [ExpCheckWakeTimerAccess](../../page/AB/ExpCheckWakeTimerAccess_function_00AB15FC.md) at `0x00AB1691`

### Static image references
- `0x003A6C4C` → RVA `0x00E0A740` (`.data`; read)
- `0x003A6E85` → RVA `0x00E0CCB0` (`.data`; read)
- `0x003A6FAA` → RVA `0x00F04AC5` (`.data`; read)
- `0x003A7015` → RVA `0x00FD80F0` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x003A6D86` → [SeLockSubjectContext](../../page/8C/SeLockSubjectContext_function_008C64C0.md) (`.text` → `PAGE`)
  - `0x003A6F93` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (`.text` → `PAGE`)
  - `0x003A713A` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (`.text` → `PAGE`)
  - `0x003A74E0` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (`.text` → `PAGE`)
  - `0x003A76EF` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (`.text` → `PAGE`)
  - `0x003A776A` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003A6C30  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
003A6C35  55                              push rbp
003A6C36  56                              push rsi
003A6C37  57                              push rdi
003A6C38  41 54                           push r12
003A6C3A  41 55                           push r13
003A6C3C  41 56                           push r14
003A6C3E  41 57                           push r15
003A6C40  48 8D 6C 24 A0                  lea rbp, [rsp - 0x60]
003A6C45  48 81 EC 80 01 00 00            sub rsp, 0x180
003A6C4C  48 8B 05 ED 3A A6 00            mov rax, qword ptr [rip + 0xa63aed]
003A6C53  48 33 C4                        xor rax, rsp
003A6C56  48 89 45 58                     mov qword ptr [rbp + 0x58], rax
003A6C5A  48 8B 9D E8 00 00 00            mov rbx, qword ptr [rbp + 0xe8]
003A6C61  45 33 E4                        xor r12d, r12d
003A6C64  4C 8B BD F0 00 00 00            mov r15, qword ptr [rbp + 0xf0]
003A6C6B  0F 57 C0                        xorps xmm0, xmm0
003A6C6E  8B B5 C0 00 00 00               mov esi, dword ptr [rbp + 0xc0]
003A6C74  4D 8B F0                        mov r14, r8
003A6C77  45 33 C0                        xor r8d, r8d
003A6C7A  48 89 4D 98                     mov qword ptr [rbp - 0x68], rcx
003A6C7E  8B C2                           mov eax, edx
003A6C80  4C 89 45 30                     mov qword ptr [rbp + 0x30], r8
003A6C84  41 83 C8 FF                     or r8d, 0xffffffff
003A6C88  89 55 8C                        mov dword ptr [rbp - 0x74], edx
003A6C8B  48 8B 95 D8 00 00 00            mov rdx, qword ptr [rbp + 0xd8]
003A6C92  83 E0 08                        and eax, 8
003A6C95  48 8B F9                        mov rdi, rcx
003A6C98  44 89 23                        mov dword ptr [rbx], r12d
003A6C9B  48 8B 8D D0 00 00 00            mov rcx, qword ptr [rbp + 0xd0]
003A6CA2  45 8A E9                        mov r13b, r9b
003A6CA5  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
003A6CA9  41 B9 22 00 00 C0               mov r9d, 0xc0000022
003A6CAF  48 89 55 E8                     mov qword ptr [rbp - 0x18], rdx
003A6CB3  0F 57 C9                        xorps xmm1, xmm1
003A6CB6  44 88 65 81                     mov byte ptr [rbp - 0x7f], r12b
003A6CBA  4C 89 65 4C                     mov qword ptr [rbp + 0x4c], r12
003A6CBE  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
003A6CC2  4C 89 65 B0                     mov qword ptr [rbp - 0x50], r12
003A6CC6  44 88 65 80                     mov byte ptr [rbp - 0x80], r12b
003A6CCA  44 89 65 84                     mov dword ptr [rbp - 0x7c], r12d
003A6CCE  4C 89 65 A0                     mov qword ptr [rbp - 0x60], r12
003A6CD2  44 89 65 A8                     mov dword ptr [rbp - 0x58], r12d
003A6CD6  44 88 65 89                     mov byte ptr [rbp - 0x77], r12b
003A6CDA  44 88 65 8A                     mov byte ptr [rbp - 0x76], r12b
003A6CDE  44 89 65 C8                     mov dword ptr [rbp - 0x38], r12d
003A6CE2  45 89 0F                        mov dword ptr [r15], r9d
003A6CE5  44 89 65 C0                     mov dword ptr [rbp - 0x40], r12d
003A6CE9  44 89 4D D0                     mov dword ptr [rbp - 0x30], r9d
003A6CED  44 89 45 C4                     mov dword ptr [rbp - 0x3c], r8d
003A6CF1  44 89 45 F0                     mov dword ptr [rbp - 0x10], r8d
003A6CF5  89 45 CC                        mov dword ptr [rbp - 0x34], eax
003A6CF8  0F 11 45 00                     movups xmmword ptr [rbp], xmm0
003A6CFC  F3 0F 7F 4D 3C                  movdqu xmmword ptr [rbp + 0x3c], xmm1
003A6D01  0F 11 45 10                     movups xmmword ptr [rbp + 0x10], xmm0
003A6D05  0F 11 45 20                     movups xmmword ptr [rbp + 0x20], xmm0
003A6D09  48 85 C9                        test rcx, rcx
003A6D0C  74 03                           je 0x1403a6d11
003A6D0E  4C 89 21                        mov qword ptr [rcx], r12
003A6D11  44 38 A5 E0 00 00 00            cmp byte ptr [rbp + 0xe0], r12b
003A6D18  75 22                           jne 0x1403a6d3c
003A6D1A  0F BA E6 19                     bt esi, 0x19
003A6D1E  73 07                           jae 0x1403a6d27
003A6D20  0F BA F6 19                     btr esi, 0x19
003A6D24  0B 72 0C                        or esi, dword ptr [rdx + 0xc]
003A6D27  0B B5 C8 00 00 00               or esi, dword ptr [rbp + 0xc8]
003A6D2D  89 33                           mov dword ptr [rbx], esi
003A6D2F  45 89 27                        mov dword ptr [r15], r12d
003A6D32  B8 01 00 00 00                  mov eax, 1
003A6D37  E9 3A 0A 00 00                  jmp 0x1403a7776
003A6D3C  48 85 FF                        test rdi, rdi
003A6D3F  0F 84 2C 0A 00 00               je 0x1403a7771
003A6D45  4D 39 26                        cmp qword ptr [r14], r12
003A6D48  74 13                           je 0x1403a6d5d
003A6D4A  41 83 7E 08 02                  cmp dword ptr [r14 + 8], 2
003A6D4F  7D 0C                           jge 0x1403a6d5d
003A6D51  41 C7 07 A5 00 00 C0            mov dword ptr [r15], 0xc00000a5
003A6D58  E9 17 0A 00 00                  jmp 0x1403a7774
003A6D5D  85 F6                           test esi, esi
003A6D5F  75 1D                           jne 0x1403a6d7e
003A6D61  8B 85 C8 00 00 00               mov eax, dword ptr [rbp + 0xc8]
003A6D67  85 C0                           test eax, eax
003A6D69  0F 84 02 0A 00 00               je 0x1403a7771
003A6D6F  89 03                           mov dword ptr [rbx], eax
003A6D71  45 89 27                        mov dword ptr [r15], r12d
003A6D74  48 85 C9                        test rcx, rcx
003A6D77  74 B9                           je 0x1403a6d32
003A6D79  4C 89 21                        mov qword ptr [rcx], r12
003A6D7C  EB B4                           jmp 0x1403a6d32
003A6D7E  45 84 ED                        test r13b, r13b
003A6D81  75 08                           jne 0x1403a6d8b
003A6D83  49 8B CE                        mov rcx, r14
003A6D86  E8 35 F7 51 00                  call 0x1408c64c0
003A6D8B  48 8D 45 C4                     lea rax, [rbp - 0x3c]
003A6D8F  45 33 C9                        xor r9d, r9d
003A6D92  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
003A6D97  4D 8B C6                        mov r8, r14
003A6D9A  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
003A6D9F  48 8B D7                        mov rdx, rdi
003A6DA2  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
003A6DA7  E8 34 6A 04 00                  call 0x1403ed7e0
003A6DAC  41 89 07                        mov dword ptr [r15], eax
003A6DAF  85 C0                           test eax, eax
003A6DB1  0F 88 AB 09 00 00               js 0x1403a7762
003A6DB7  8B CE                           mov ecx, esi
003A6DB9  41 BC FF FF FF FD               mov r12d, 0xfdffffff
003A6DBF  41 23 CC                        and ecx, r12d
003A6DC2  8B C1                           mov eax, ecx
003A6DC4  23 45 C4                        and eax, dword ptr [rbp - 0x3c]
003A6DC7  3B C1                           cmp eax, ecx
003A6DC9  0F 85 46 09 00 00               jne 0x1403a7715
003A6DCF  33 D2                           xor edx, edx
003A6DD1  41 89 17                        mov dword ptr [r15], edx
003A6DD4  49 8B 3E                        mov rdi, qword ptr [r14]
003A6DD7  48 89 7D F8                     mov qword ptr [rbp - 8], rdi
003A6DDB  48 85 FF                        test rdi, rdi
003A6DDE  75 08                           jne 0x1403a6de8
003A6DE0  49 8B 7E 10                     mov rdi, qword ptr [r14 + 0x10]
003A6DE4  48 89 7D F8                     mov qword ptr [rbp - 8], rdi
003A6DE8  8B 45 8C                        mov eax, dword ptr [rbp - 0x74]
003A6DEB  A8 04                           test al, 4
003A6DED  75 3D                           jne 0x1403a6e2c
003A6DEF  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
003A6DF3  48 8D 45 F0                     lea rax, [rbp - 0x10]
003A6DF7  45 33 C9                        xor r9d, r9d
003A6DFA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003A6DFF  4C 8B C7                        mov r8, rdi
003A6E02  48 8D 55 A0                     lea rdx, [rbp - 0x60]
003A6E06  E8 55 AD F5 FF                  call 0x140301b60
003A6E0B  33 D2                           xor edx, edx
003A6E0D  41 89 07                        mov dword ptr [r15], eax
003A6E10  85 C0                           test eax, eax
003A6E12  0F 88 4A 09 00 00               js 0x1403a7762
003A6E18  8B CE                           mov ecx, esi
003A6E1A  41 23 CC                        and ecx, r12d
003A6E1D  8B C1                           mov eax, ecx
003A6E1F  23 45 F0                        and eax, dword ptr [rbp - 0x10]
003A6E22  3B C1                           cmp eax, ecx
003A6E24  75 24                           jne 0x1403a6e4a
003A6E26  8B 45 8C                        mov eax, dword ptr [rbp - 0x74]
003A6E29  41 89 17                        mov dword ptr [r15], edx
003A6E2C  41 BC 01 00 00 00               mov r12d, 1
003A6E32  A8 02                           test al, 2
003A6E34  74 4A                           je 0x1403a6e80
003A6E36  F7 87 C8 00 00 00 00 20 00 00   test dword ptr [rdi + 0xc8], 0x2000
003A6E40  45 8A C4                        mov r8b, r12b
003A6E43  74 3E                           je 0x1403a6e83
003A6E45  41 8A CC                        mov cl, r12b
003A6E48  EB 3B                           jmp 0x1403a6e85
003A6E4A  41 C7 07 22 00 00 C0            mov dword ptr [r15], 0xc0000022
003A6E51  39 55 CC                        cmp dword ptr [rbp - 0x34], edx
003A6E54  0F 85 08 09 00 00               jne 0x1403a7762
003A6E5A  0B B5 C8 00 00 00               or esi, dword ptr [rbp + 0xc8]
003A6E60  48 8B CF                        mov rcx, rdi
003A6E63  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
003A6E67  45 33 C9                        xor r9d, r9d
003A6E6A  88 54 24 38                     mov byte ptr [rsp + 0x38], dl
003A6E6E  88 54 24 30                     mov byte ptr [rsp + 0x30], dl
003A6E72  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
003A6E76  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003A6E7B  E9 DA 08 00 00                  jmp 0x1403a775a
003A6E80  44 8A C2                        mov r8b, dl
003A6E83  8A CA                           mov cl, dl
003A6E85  38 15 25 5E A6 00               cmp byte ptr [rip + 0xa65e25], dl
003A6E8B  88 4D 88                        mov byte ptr [rbp - 0x78], cl
003A6E8E  88 55 90                        mov byte ptr [rbp - 0x70], dl
003A6E91  75 2B                           jne 0x1403a6ebe
003A6E93  8B 87 C8 00 00 00               mov eax, dword ptr [rdi + 0xc8]
003A6E99  A8 20                           test al, 0x20
003A6E9B  75 21                           jne 0x1403a6ebe
003A6E9D  48 8B 87 D8 00 00 00            mov rax, qword ptr [rdi + 0xd8]
003A6EA4  48 85 C0                        test rax, rax
003A6EA7  74 15                           je 0x1403a6ebe
003A6EA9  8B 40 28                        mov eax, dword ptr [rax + 0x28]
003A6EAC  A8 20                           test al, 0x20
003A6EAE  74 0E                           je 0x1403a6ebe
003A6EB0  89 13                           mov dword ptr [rbx], edx
003A6EB2  41 C7 07 22 00 00 C0            mov dword ptr [r15], 0xc0000022
003A6EB9  E9 A4 08 00 00                  jmp 0x1403a7762
003A6EBE  84 C9                           test cl, cl
003A6EC0  0F 85 83 00 00 00               jne 0x1403a6f49
003A6EC6  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
003A6ECA  48 8D 45 00                     lea rax, [rbp]
003A6ECE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003A6ED3  4C 8B CF                        mov r9, rdi
003A6ED6  88 54 24 20                     mov byte ptr [rsp + 0x20], dl
003A6EDA  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
003A6EDE  E8 FD 85 EB FF                  call 0x14025f4e0
003A6EE3  41 89 07                        mov dword ptr [r15], eax
003A6EE6  85 C0                           test eax, eax
003A6EE8  0F 88 74 08 00 00               js 0x1403a7762
003A6EEE  8B D6                           mov edx, esi
003A6EF0  48 8D 4D 00                     lea rcx, [rbp]
003A6EF4  E8 47 50 07 00                  call 0x14041bf40
003A6EF9  41 89 07                        mov dword ptr [r15], eax
003A6EFC  85 C0                           test eax, eax
003A6EFE  79 23                           jns 0x1403a6f23
003A6F00  F7 87 C8 00 00 00 00 40 00 00   test dword ptr [rdi + 0xc8], 0x4000
003A6F0A  0F 84 52 08 00 00               je 0x1403a7762
003A6F10  81 7D 0C 00 20 00 00            cmp dword ptr [rbp + 0xc], 0x2000
003A6F17  0F 87 45 08 00 00               ja 0x1403a7762
003A6F1D  44 88 65 90                     mov byte ptr [rbp - 0x70], r12b
003A6F21  EB 26                           jmp 0x1403a6f49
003A6F23  0F BA E6 19                     bt esi, 0x19
003A6F27  73 20                           jae 0x1403a6f49
003A6F29  F7 87 C8 00 00 00 00 40 00 00   test dword ptr [rdi + 0xc8], 0x4000
003A6F33  74 14                           je 0x1403a6f49
003A6F35  8B 45 90                        mov eax, dword ptr [rbp - 0x70]
003A6F38  81 7D 0C 00 20 00 00            cmp dword ptr [rbp + 0xc], 0x2000
003A6F3F  0F B6 C0                        movzx eax, al
003A6F42  41 0F 46 C4                     cmovbe eax, r12d
003A6F46  89 45 90                        mov dword ptr [rbp - 0x70], eax
003A6F49  E8 1A 6A 22 00                  call 0x1405cd968
003A6F4E  45 33 DB                        xor r11d, r11d
003A6F51  85 C0                           test eax, eax
003A6F53  74 55                           je 0x1403a6faa
003A6F55  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
003A6F59  48 8D 45 C8                     lea rax, [rbp - 0x38]
003A6F5D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003A6F62  45 84 ED                        test r13b, r13b
003A6F65  49 8B D6                        mov rdx, r14
003A6F68  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
003A6F6C  41 0F 94 C1                     sete r9b
003A6F70  45 33 C0                        xor r8d, r8d
003A6F73  E8 08 15 26 00                  call 0x140608480
003A6F78  45 33 DB                        xor r11d, r11d
003A6F7B  85 C0                           test eax, eax
003A6F7D  78 0C                           js 0x1403a6f8b
003A6F7F  8B 45 C8                        mov eax, dword ptr [rbp - 0x38]
003A6F82  23 C6                           and eax, esi
003A6F84  A9 FF FF FF FD                  test eax, 0xfdffffff
003A6F89  74 1F                           je 0x1403a6faa
003A6F8B  45 84 ED                        test r13b, r13b
003A6F8E  75 0B                           jne 0x1403a6f9b
003A6F90  49 8B CE                        mov rcx, r14
003A6F93  E8 88 F5 51 00                  call 0x1408c6520
003A6F98  45 33 DB                        xor r11d, r11d
003A6F9B  44 89 1B                        mov dword ptr [rbx], r11d
003A6F9E  41 C7 07 C0 01 00 C0            mov dword ptr [r15], 0xc00001c0
003A6FA5  E9 CA 07 00 00                  jmp 0x1403a7774
003A6FAA  8A 05 15 DB B5 00               mov al, byte ptr [rip + 0xb5db15]
003A6FB0  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
003A6FB4  84 C0                           test al, al
003A6FB6  74 73                           je 0x1403a702b
003A6FB8  0F B7 4A 02                     movzx ecx, word ptr [rdx + 2]
003A6FBC  F6 C1 10                        test cl, 0x10
003A6FBF  74 6A                           je 0x1403a702b
003A6FC1  44 0F 20 C0                     mov rax, cr8
003A6FC5  3C 02                           cmp al, 2
003A6FC7  73 62                           jae 0x1403a702b
003A6FC9  66 85 C9                        test cx, cx
003A6FCC  79 12                           jns 0x1403a6fe0
003A6FCE  8B 42 0C                        mov eax, dword ptr [rdx + 0xc]
003A6FD1  85 C0                           test eax, eax
003A6FD3  75 06                           jne 0x1403a6fdb
003A6FD5  4C 89 5D E0                     mov qword ptr [rbp - 0x20], r11
003A6FD9  EB 50                           jmp 0x1403a702b
003A6FDB  48 03 C2                        add rax, rdx
003A6FDE  EB 04                           jmp 0x1403a6fe4
003A6FE0  48 8B 42 18                     mov rax, qword ptr [rdx + 0x18]
003A6FE4  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
003A6FE8  48 85 C0                        test rax, rax
003A6FEB  74 3E                           je 0x1403a702b
003A6FED  48 8B C8                        mov rcx, rax
003A6FF0  E8 B7 E9 FF FF                  call 0x1403a59ac
003A6FF5  48 85 C0                        test rax, rax
003A6FF8  74 2D                           je 0x1403a7027
003A6FFA  48 8D 55 B0                     lea rdx, [rbp - 0x50]
003A6FFE  48 8B C8                        mov rcx, rax
003A7001  E8 E6 E8 FF FF                  call 0x1403a58ec
003A7006  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
003A700A  45 33 DB                        xor r11d, r11d
003A700D  85 C0                           test eax, eax
003A700F  41 8A CC                        mov cl, r12b
003A7012  88 4D 80                        mov byte ptr [rbp - 0x80], cl
003A7015  48 0F 48 15 D3 10 C3 00         cmovs rdx, qword ptr [rip + 0xc310d3]
003A701D  48 89 55 B0                     mov qword ptr [rbp - 0x50], rdx
003A7021  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
003A7025  EB 07                           jmp 0x1403a702e
003A7027  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
003A702B  8A 4D 80                        mov cl, byte ptr [rbp - 0x80]
003A702E  8B C6                           mov eax, esi
003A7030  44 84 65 8C                     test byte ptr [rbp - 0x74], r12b
003A7034  74 1E                           je 0x1403a7054
003A7036  25 00 00 06 02                  and eax, 0x2060000
003A703B  44 88 65 82                     mov byte ptr [rbp - 0x7e], r12b
003A703F  89 45 8C                        mov dword ptr [rbp - 0x74], eax
003A7042  75 1C                           jne 0x1403a7060
003A7044  89 45 8C                        mov dword ptr [rbp - 0x74], eax
003A7047  84 C9                           test cl, cl
003A7049  75 15                           jne 0x1403a7060
003A704B  44 88 5D 83                     mov byte ptr [rbp - 0x7d], r11b
003A704F  E9 9C 00 00 00                  jmp 0x1403a70f0
003A7054  25 00 00 06 02                  and eax, 0x2060000
003A7059  44 88 5D 82                     mov byte ptr [rbp - 0x7e], r11b
003A705D  89 45 8C                        mov dword ptr [rbp - 0x74], eax
003A7060  48 8B CF                        mov rcx, rdi
003A7063  E8 F8 EC 03 00                  call 0x1403e5d60
003A7068  45 33 C9                        xor r9d, r9d
003A706B  88 45 83                        mov byte ptr [rbp - 0x7d], al
003A706E  84 C0                           test al, al
003A7070  74 7E                           je 0x1403a70f0
003A7072  44 39 4D 8C                     cmp dword ptr [rbp - 0x74], r9d
003A7076  74 78                           je 0x1403a70f0
003A7078  44 38 4D 82                     cmp byte ptr [rbp - 0x7e], r9b
003A707C  75 38                           jne 0x1403a70b6
003A707E  4C 8B 45 98                     mov r8, qword ptr [rbp - 0x68]
003A7082  41 0F B7 48 02                  movzx ecx, word ptr [r8 + 2]
003A7087  F6 C1 04                        test cl, 4
003A708A  75 05                           jne 0x1403a7091
003A708C  49 8B D1                        mov rdx, r9
003A708F  EB 17                           jmp 0x1403a70a8
003A7091  66 85 C9                        test cx, cx
003A7094  79 0E                           jns 0x1403a70a4
003A7096  41 8B 40 10                     mov eax, dword ptr [r8 + 0x10]
003A709A  85 C0                           test eax, eax
003A709C  74 EE                           je 0x1403a708c
003A709E  49 8D 14 00                     lea rdx, [r8 + rax]
003A70A2  EB 04                           jmp 0x1403a70a8
003A70A4  49 8B 50 20                     mov rdx, qword ptr [r8 + 0x20]
003A70A8  33 C9                           xor ecx, ecx
003A70AA  E8 41 42 05 00                  call 0x1403fb2f0
003A70AF  45 33 C9                        xor r9d, r9d
003A70B2  84 C0                           test al, al
003A70B4  75 3A                           jne 0x1403a70f0
003A70B6  8B C6                           mov eax, esi
003A70B8  BA 00 00 06 00                  mov edx, 0x60000
003A70BD  23 C2                           and eax, edx
003A70BF  0F BA E6 19                     bt esi, 0x19
003A70C3  0F 43 D0                        cmovae edx, eax
003A70C6  81 E6 FF FF F9 FF               and esi, 0xfff9ffff
003A70CC  8B C2                           mov eax, edx
003A70CE  89 55 84                        mov dword ptr [rbp - 0x7c], edx
003A70D1  0B 85 C8 00 00 00               or eax, dword ptr [rbp + 0xc8]
003A70D7  89 85 C8 00 00 00               mov dword ptr [rbp + 0xc8], eax
003A70DD  44 38 4D 80                     cmp byte ptr [rbp - 0x80], r9b
003A70E1  75 0D                           jne 0x1403a70f0
003A70E3  44 88 4D 83                     mov byte ptr [rbp - 0x7d], r9b
003A70E7  89 85 C8 00 00 00               mov dword ptr [rbp + 0xc8], eax
003A70ED  89 55 84                        mov dword ptr [rbp - 0x7c], edx
003A70F0  E8 93 86 14 00                  call 0x1404ef788
003A70F5  33 D2                           xor edx, edx
003A70F7  85 F6                           test esi, esi
003A70F9  75 61                           jne 0x1403a715c
003A70FB  38 55 80                        cmp byte ptr [rbp - 0x80], dl
003A70FE  75 5C                           jne 0x1403a715c
003A7100  8B 8F C8 00 00 00               mov ecx, dword ptr [rdi + 0xc8]
003A7106  41 B8 00 60 00 00               mov r8d, 0x6000
003A710C  85 C0                           test eax, eax
003A710E  74 44                           je 0x1403a7154
003A7110  8B C1                           mov eax, ecx
003A7112  41 23 C0                        and eax, r8d
003A7115  3D 00 20 00 00                  cmp eax, 0x2000
003A711A  74 16                           je 0x1403a7132
003A711C  8B 45 84                        mov eax, dword ptr [rbp - 0x7c]
003A711F  85 C0                           test eax, eax
003A7121  74 0F                           je 0x1403a7132
003A7123  41 23 C8                        and ecx, r8d
003A7126  81 F9 00 20 00 00               cmp ecx, 0x2000
003A712C  74 04                           je 0x1403a7132
003A712E  85 C0                           test eax, eax
003A7130  75 2D                           jne 0x1403a715f
003A7132  45 84 ED                        test r13b, r13b
003A7135  75 0A                           jne 0x1403a7141
003A7137  49 8B CE                        mov rcx, r14
003A713A  E8 E1 F3 51 00                  call 0x1408c6520
003A713F  33 D2                           xor edx, edx
003A7141  8B 85 C8 00 00 00               mov eax, dword ptr [rbp + 0xc8]
003A7147  89 03                           mov dword ptr [rbx], eax
003A7149  41 89 17                        mov dword ptr [r15], edx
003A714C  41 8A C4                        mov al, r12b
003A714F  E9 22 06 00 00                  jmp 0x1403a7776
003A7154  0F BA E1 0D                     bt ecx, 0xd
003A7158  72 D8                           jb 0x1403a7132
003A715A  EB C0                           jmp 0x1403a711c
003A715C  8B 45 84                        mov eax, dword ptr [rbp - 0x7c]
003A715F  4D 8B 0E                        mov r9, qword ptr [r14]
003A7162  0F 57 C0                        xorps xmm0, xmm0
003A7165  4D 8B 46 10                     mov r8, qword ptr [r14 + 0x10]
003A7169  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
003A716D  48 89 94 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdx
003A7175  89 45 38                        mov dword ptr [rbp + 0x38], eax
003A7178  48 8D 45 81                     lea rax, [rbp - 0x7f]
003A717C  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
003A7184  48 8D 45 A0                     lea rax, [rbp - 0x60]
003A7188  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
003A7190  48 8D 45 38                     lea rax, [rbp + 0x38]
003A7194  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
003A7199  8A 45 83                        mov al, byte ptr [rbp - 0x7d]
003A719C  88 44 24 70                     mov byte ptr [rsp + 0x70], al
003A71A0  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
003A71A4  88 54 24 68                     mov byte ptr [rsp + 0x68], dl
003A71A8  4C 89 7C 24 60                  mov qword ptr [rsp + 0x60], r15
003A71AD  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
003A71B2  8A 85 E0 00 00 00               mov al, byte ptr [rbp + 0xe0]
003A71B8  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
003A71BD  88 44 24 48                     mov byte ptr [rsp + 0x48], al
003A71C1  8B 85 C8 00 00 00               mov eax, dword ptr [rbp + 0xc8]
003A71C7  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
003A71CB  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
003A71CF  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
003A71D4  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
003A71D8  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
003A71DD  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
003A71E1  F3 0F 7F 45 3C                  movdqu xmmword ptr [rbp + 0x3c], xmm0
003A71E6  48 89 55 4C                     mov qword ptr [rbp + 0x4c], rdx
003A71EA  E8 65 9C 02 00                  call 0x1403d0e54
003A71EF  8A 0D D0 D8 B5 00               mov cl, byte ptr [rip + 0xb5d8d0]
003A71F5  45 33 DB                        xor r11d, r11d
003A71F8  88 45 8B                        mov byte ptr [rbp - 0x75], al
003A71FB  84 C9                           test cl, cl
003A71FD  0F 84 18 03 00 00               je 0x1403a751b
003A7203  41 8B 07                        mov eax, dword ptr [r15]
003A7206  89 45 D4                        mov dword ptr [rbp - 0x2c], eax
003A7209  85 C0                           test eax, eax
003A720B  0F 88 0A 03 00 00               js 0x1403a751b
003A7211  44 38 5D 80                     cmp byte ptr [rbp - 0x80], r11b
003A7215  0F 84 00 03 00 00               je 0x1403a751b
003A721B  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
003A721F  45 8B C3                        mov r8d, r11d
003A7222  8B 13                           mov edx, dword ptr [rbx]
003A7224  44 88 5D 82                     mov byte ptr [rbp - 0x7e], r11b
003A7228  89 55 84                        mov dword ptr [rbp - 0x7c], edx
003A722B  44 88 5D 8C                     mov byte ptr [rbp - 0x74], r11b
003A722F  44 89 5D D8                     mov dword ptr [rbp - 0x28], r11d
003A7233  44 39 59 3C                     cmp dword ptr [rcx + 0x3c], r11d
003A7237  0F 86 D0 02 00 00               jbe 0x1403a750d
003A723D  41 8B C0                        mov eax, r8d
003A7240  48 8B 4C C1 40                  mov rcx, qword ptr [rcx + rax*8 + 0x40]
003A7245  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
003A7249  4C 39 59 18                     cmp qword ptr [rcx + 0x18], r11
003A724D  0F 84 72 01 00 00               je 0x1403a73c5
003A7253  4C 8B 45 A0                     mov r8, qword ptr [rbp - 0x60]
003A7257  4D 85 C0                        test r8, r8
003A725A  75 2A                           jne 0x1403a7286
003A725C  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
003A7260  48 8D 55 A0                     lea rdx, [rbp - 0x60]
003A7264  E8 1B BC F5 FF                  call 0x140302e84
003A7269  44 8B 4D 8C                     mov r9d, dword ptr [rbp - 0x74]
003A726D  45 33 DB                        xor r11d, r11d
003A7270  4C 8B 45 A0                     mov r8, qword ptr [rbp - 0x60]
003A7274  85 C0                           test eax, eax
003A7276  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
003A727A  45 0F B6 C9                     movzx r9d, r9b
003A727E  45 0F 48 CC                     cmovs r9d, r12d
003A7282  44 89 4D 8C                     mov dword ptr [rbp - 0x74], r9d
003A7286  48 8B 87 48 04 00 00            mov rax, qword ptr [rdi + 0x448]
003A728D  48 85 C0                        test rax, rax
003A7290  74 1E                           je 0x1403a72b0
003A7292  4C 8B 88 40 02 00 00            mov r9, qword ptr [rax + 0x240]
003A7299  48 8B 90 50 02 00 00            mov rdx, qword ptr [rax + 0x250]
003A72A0  4C 8B 90 48 02 00 00            mov r10, qword ptr [rax + 0x248]
003A72A7  4C 8B 98 58 02 00 00            mov r11, qword ptr [rax + 0x258]
003A72AE  EB 09                           jmp 0x1403a72b9
003A72B0  4D 8B CB                        mov r9, r11
003A72B3  49 8B D3                        mov rdx, r11
003A72B6  4D 8B D3                        mov r10, r11
003A72B9  48 8D 45 A8                     lea rax, [rbp - 0x58]
003A72BD  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
003A72C2  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
003A72C5  C6 44 24 50 00                  mov byte ptr [rsp + 0x50], 0
003A72CA  44 88 64 24 48                  mov byte ptr [rsp + 0x48], r12b
003A72CF  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
003A72D3  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
003A72D7  48 8B CF                        mov rcx, rdi
003A72DA  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
003A72DF  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
003A72E4  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
003A72E9  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
003A72EE  48 8B 97 08 03 00 00            mov rdx, qword ptr [rdi + 0x308]
003A72F5  E8 D6 78 F5 FF                  call 0x1402febd0
003A72FA  8B 4D A8                        mov ecx, dword ptr [rbp - 0x58]
003A72FD  89 45 94                        mov dword ptr [rbp - 0x6c], eax
003A7300  41 3B CC                        cmp ecx, r12d
003A7303  0F 84 B8 00 00 00               je 0x1403a73c1
003A7309  45 33 DB                        xor r11d, r11d
003A730C  85 C0                           test eax, eax
003A730E  0F 88 C4 01 00 00               js 0x1403a74d8
003A7314  8B 87 C8 00 00 00               mov eax, dword ptr [rdi + 0xc8]
003A731A  A8 10                           test al, 0x10
003A731C  0F 84 90 00 00 00               je 0x1403a73b2
003A7322  48 8B 87 48 04 00 00            mov rax, qword ptr [rdi + 0x448]
003A7329  48 85 C0                        test rax, rax
003A732C  74 1E                           je 0x1403a734c
003A732E  4C 8B 88 40 02 00 00            mov r9, qword ptr [rax + 0x240]
003A7335  48 8B 90 50 02 00 00            mov rdx, qword ptr [rax + 0x250]
003A733C  4C 8B 80 48 02 00 00            mov r8, qword ptr [rax + 0x248]
003A7343  4C 8B 90 58 02 00 00            mov r10, qword ptr [rax + 0x258]
003A734A  EB 0C                           jmp 0x1403a7358
003A734C  4D 8B CB                        mov r9, r11
003A734F  49 8B D3                        mov rdx, r11
003A7352  4D 8B C3                        mov r8, r11
003A7355  4D 8B D3                        mov r10, r11
003A7358  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
003A735C  48 8D 45 A8                     lea rax, [rbp - 0x58]
003A7360  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
003A7365  44 88 64 24 50                  mov byte ptr [rsp + 0x50], r12b
003A736A  44 88 64 24 48                  mov byte ptr [rsp + 0x48], r12b
003A736F  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
003A7372  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
003A7376  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
003A737A  48 8B CF                        mov rcx, rdi
003A737D  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
003A7382  4C 89 54 24 30                  mov qword ptr [rsp + 0x30], r10
003A7387  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
003A738C  4C 8B 45 A0                     mov r8, qword ptr [rbp - 0x60]
003A7390  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
003A7395  48 8B 97 08 03 00 00            mov rdx, qword ptr [rdi + 0x308]
003A739C  E8 2F 78 F5 FF                  call 0x1402febd0
003A73A1  45 33 DB                        xor r11d, r11d
003A73A4  89 45 94                        mov dword ptr [rbp - 0x6c], eax
003A73A7  85 C0                           test eax, eax
003A73A9  0F 88 29 01 00 00               js 0x1403a74d8
003A73AF  8B 4D A8                        mov ecx, dword ptr [rbp - 0x58]
003A73B2  44 38 5D 8C                     cmp byte ptr [rbp - 0x74], r11b
003A73B6  75 09                           jne 0x1403a73c1
003A73B8  41 3B CC                        cmp ecx, r12d
003A73BB  0F 85 F9 00 00 00               jne 0x1403a74ba
003A73C1  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
003A73C5  48 8B 51 20                     mov rdx, qword ptr [rcx + 0x20]
003A73C9  48 8D 4D 10                     lea rcx, [rbp + 0x10]
003A73CD  4C 8B 45 E0                     mov r8, qword ptr [rbp - 0x20]
003A73D1  E8 62 2A 13 00                  call 0x1404d9e38
003A73D6  45 33 C0                        xor r8d, r8d
003A73D9  89 45 94                        mov dword ptr [rbp - 0x6c], eax
003A73DC  85 C0                           test eax, eax
003A73DE  0F 88 F4 00 00 00               js 0x1403a74d8
003A73E4  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
003A73E8  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
003A73EB  41 84 C4                        test r12b, al
003A73EE  8B C6                           mov eax, esi
003A73F0  74 11                           je 0x1403a7403
003A73F2  0F BA E6 19                     bt esi, 0x19
003A73F6  72 06                           jb 0x1403a73fe
003A73F8  0B 85 C8 00 00 00               or eax, dword ptr [rbp + 0xc8]
003A73FE  41 8B C8                        mov ecx, r8d
003A7401  EB 06                           jmp 0x1403a7409
003A7403  8B 8D C8 00 00 00               mov ecx, dword ptr [rbp + 0xc8]
003A7409  4D 8B 0E                        mov r9, qword ptr [r14]
003A740C  48 8D 55 81                     lea rdx, [rbp - 0x7f]
003A7410  4C 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], r8
003A7418  48 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdx
003A7420  48 8D 55 A0                     lea rdx, [rbp - 0x60]
003A7424  48 89 94 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdx
003A742C  48 8D 55 38                     lea rdx, [rbp + 0x38]
003A7430  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
003A7435  8A 55 83                        mov dl, byte ptr [rbp - 0x7d]
003A7438  88 54 24 70                     mov byte ptr [rsp + 0x70], dl
003A743C  48 8D 55 D0                     lea rdx, [rbp - 0x30]
003A7440  44 88 44 24 68                  mov byte ptr [rsp + 0x68], r8b
003A7445  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
003A744A  48 8D 55 C0                     lea rdx, [rbp - 0x40]
003A744E  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
003A7453  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
003A7458  8A 95 E0 00 00 00               mov dl, byte ptr [rbp + 0xe0]
003A745E  88 54 24 48                     mov byte ptr [rsp + 0x48], dl
003A7462  33 D2                           xor edx, edx
003A7464  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
003A7468  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
003A746C  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
003A7471  48 8D 4D 10                     lea rcx, [rbp + 0x10]
003A7475  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
003A747A  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
003A747F  4D 8B 46 10                     mov r8, qword ptr [r14 + 0x10]
003A7483  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
003A7487  E8 C8 99 02 00                  call 0x1403d0e54
003A748C  45 33 DB                        xor r11d, r11d
003A748F  88 45 8B                        mov byte ptr [rbp - 0x75], al
003A7492  44 38 5D 82                     cmp byte ptr [rbp - 0x7e], r11b
003A7496  75 05                           jne 0x1403a749d
003A7498  8B 45 C0                        mov eax, dword ptr [rbp - 0x40]
003A749B  EB 06                           jmp 0x1403a74a3
003A749D  8B 45 84                        mov eax, dword ptr [rbp - 0x7c]
003A74A0  23 45 C0                        and eax, dword ptr [rbp - 0x40]
003A74A3  89 45 84                        mov dword ptr [rbp - 0x7c], eax
003A74A6  85 C0                           test eax, eax
003A74A8  74 5B                           je 0x1403a7505
003A74AA  8B 45 D0                        mov eax, dword ptr [rbp - 0x30]
003A74AD  89 45 D4                        mov dword ptr [rbp - 0x2c], eax
003A74B0  44 88 65 82                     mov byte ptr [rbp - 0x7e], r12b
003A74B4  85 C0                           test eax, eax
003A74B6  78 52                           js 0x1403a750a
003A74B8  EB 03                           jmp 0x1403a74bd
003A74BA  8B 45 D4                        mov eax, dword ptr [rbp - 0x2c]
003A74BD  44 8B 45 D8                     mov r8d, dword ptr [rbp - 0x28]
003A74C1  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
003A74C5  45 03 C4                        add r8d, r12d
003A74C8  44 89 45 D8                     mov dword ptr [rbp - 0x28], r8d
003A74CC  44 3B 41 3C                     cmp r8d, dword ptr [rcx + 0x3c]
003A74D0  0F 82 67 FD FF FF               jb 0x1403a723d
003A74D6  EB 32                           jmp 0x1403a750a
003A74D8  45 84 ED                        test r13b, r13b
003A74DB  75 08                           jne 0x1403a74e5
003A74DD  49 8B CE                        mov rcx, r14
003A74E0  E8 3B F0 51 00                  call 0x1408c6520
003A74E5  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
003A74E9  E8 AE A9 10 00                  call 0x1404b1e9c
003A74EE  8B 45 94                        mov eax, dword ptr [rbp - 0x6c]
003A74F1  83 23 00                        and dword ptr [rbx], 0
003A74F4  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
003A74F8  41 89 07                        mov dword ptr [r15], eax
003A74FB  E8 F0 A4 F5 FF                  call 0x1403019f0
003A7500  E9 6F 02 00 00                  jmp 0x1403a7774
003A7505  B8 22 00 00 C0                  mov eax, 0xc0000022
003A750A  8B 55 84                        mov edx, dword ptr [rbp - 0x7c]
003A750D  41 89 07                        mov dword ptr [r15], eax
003A7510  21 13                           and dword ptr [rbx], edx
003A7512  45 39 1F                        cmp dword ptr [r15], r11d
003A7515  7D 04                           jge 0x1403a751b
003A7517  44 88 5D 81                     mov byte ptr [rbp - 0x7f], r11b
003A751B  44 38 5D 88                     cmp byte ptr [rbp - 0x78], r11b
003A751F  75 55                           jne 0x1403a7576
003A7521  0F BA E6 19                     bt esi, 0x19
003A7525  73 4F                           jae 0x1403a7576
003A7527  44 38 5D 90                     cmp byte ptr [rbp - 0x70], r11b
003A752B  74 25                           je 0x1403a7552
003A752D  44 38 5D 4E                     cmp byte ptr [rbp + 0x4e], r11b
003A7531  0F 85 93 00 00 00               jne 0x1403a75ca
003A7537  44 38 5D 4D                     cmp byte ptr [rbp + 0x4d], r11b
003A753B  0F 85 89 00 00 00               jne 0x1403a75ca
003A7541  8B 87 C8 00 00 00               mov eax, dword ptr [rdi + 0xc8]
003A7547  B9 00 00 00 03                  mov ecx, 0x3000000
003A754C  23 C1                           and eax, ecx
003A754E  3B C1                           cmp eax, ecx
003A7550  74 78                           je 0x1403a75ca
003A7552  48 8D 45 81                     lea rax, [rbp - 0x7f]
003A7556  44 89 5C 24 28                  mov dword ptr [rsp + 0x28], r11d
003A755B  4D 8B CF                        mov r9, r15
003A755E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003A7563  4C 8B C3                        mov r8, rbx
003A7566  48 8D 4D 00                     lea rcx, [rbp]
003A756A  8B D6                           mov edx, esi
003A756C  E8 FF 86 09 00                  call 0x14043fc70
003A7571  45 33 DB                        xor r11d, r11d
003A7574  EB 54                           jmp 0x1403a75ca
003A7576  44 38 5D 90                     cmp byte ptr [rbp - 0x70], r11b
003A757A  74 48                           je 0x1403a75c4
003A757C  44 38 5D 4E                     cmp byte ptr [rbp + 0x4e], r11b
003A7580  75 42                           jne 0x1403a75c4
003A7582  44 38 5D 4D                     cmp byte ptr [rbp + 0x4d], r11b
003A7586  75 3C                           jne 0x1403a75c4
003A7588  8B 87 C8 00 00 00               mov eax, dword ptr [rdi + 0xc8]
003A758E  B9 00 00 00 03                  mov ecx, 0x3000000
003A7593  23 C1                           and eax, ecx
003A7595  3B C1                           cmp eax, ecx
003A7597  75 1D                           jne 0x1403a75b6
003A7599  44 39 5D 44                     cmp dword ptr [rbp + 0x44], r11d
003A759D  75 17                           jne 0x1403a75b6
003A759F  8B C6                           mov eax, esi
003A75A1  45 89 1F                        mov dword ptr [r15], r11d
003A75A4  0B 85 C8 00 00 00               or eax, dword ptr [rbp + 0xc8]
003A75AA  89 03                           mov dword ptr [rbx], eax
003A75AC  44 88 65 4F                     mov byte ptr [rbp + 0x4f], r12b
003A75B0  44 88 65 81                     mov byte ptr [rbp - 0x7f], r12b
003A75B4  EB 0E                           jmp 0x1403a75c4
003A75B6  41 C7 07 22 00 00 C0            mov dword ptr [r15], 0xc0000022
003A75BD  44 89 1B                        mov dword ptr [rbx], r11d
003A75C0  44 88 5D 81                     mov byte ptr [rbp - 0x7f], r11b
003A75C4  0F BA E6 19                     bt esi, 0x19
003A75C8  73 61                           jae 0x1403a762b
003A75CA  8B 4D C4                        mov ecx, dword ptr [rbp - 0x3c]
003A75CD  48 8D 45 89                     lea rax, [rbp - 0x77]
003A75D1  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
003A75D6  4D 8B CF                        mov r9, r15
003A75D9  48 8D 45 81                     lea rax, [rbp - 0x7f]
003A75DD  44 89 5C 24 28                  mov dword ptr [rsp + 0x28], r11d
003A75E2  4C 8B C3                        mov r8, rbx
003A75E5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003A75EA  8B D6                           mov edx, esi
003A75EC  E8 EF 87 09 00                  call 0x14043fde0
003A75F1  8B 4D F0                        mov ecx, dword ptr [rbp - 0x10]
003A75F4  48 8D 55 8A                     lea rdx, [rbp - 0x76]
003A75F8  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
003A75FD  48 8D 45 81                     lea rax, [rbp - 0x7f]
003A7601  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
003A7606  8B D6                           mov edx, esi
003A7608  4D 8B CF                        mov r9, r15
003A760B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003A7610  4C 8B C3                        mov r8, rbx
003A7613  E8 C8 87 09 00                  call 0x14043fde0
003A7618  E8 4B 63 22 00                  call 0x1405cd968
003A761D  45 33 DB                        xor r11d, r11d
003A7620  85 C0                           test eax, eax
003A7622  74 07                           je 0x1403a762b
003A7624  8B 45 C8                        mov eax, dword ptr [rbp - 0x38]
003A7627  F7 D0                           not eax
003A7629  21 03                           and dword ptr [rbx], eax
003A762B  48 85 FF                        test rdi, rdi
003A762E  0F 84 A4 00 00 00               je 0x1403a76d8
003A7634  44 38 5D 89                     cmp byte ptr [rbp - 0x77], r11b
003A7638  75 23                           jne 0x1403a765d
003A763A  44 38 5D 8A                     cmp byte ptr [rbp - 0x76], r11b
003A763E  75 1D                           jne 0x1403a765d
003A7640  44 39 5D 44                     cmp dword ptr [rbp + 0x44], r11d
003A7644  75 64                           jne 0x1403a76aa
003A7646  F7 87 C8 00 00 00 00 40 00 00   test dword ptr [rdi + 0xc8], 0x4000
003A7650  74 58                           je 0x1403a76aa
003A7652  45 39 1F                        cmp dword ptr [r15], r11d
003A7655  7C 06                           jl 0x1403a765d
003A7657  44 38 5D 4F                     cmp byte ptr [rbp + 0x4f], r11b
003A765B  74 4D                           je 0x1403a76aa
003A765D  44 39 5D CC                     cmp dword ptr [rbp - 0x34], r11d
003A7661  75 47                           jne 0x1403a76aa
003A7663  41 8B 3F                        mov edi, dword ptr [r15]
003A7666  8B DE                           mov ebx, esi
003A7668  0B 9D C8 00 00 00               or ebx, dword ptr [rbp + 0xc8]
003A766E  49 8B CE                        mov rcx, r14
003A7671  C1 EF 1F                        shr edi, 0x1f
003A7674  41 32 FC                        xor dil, r12b
003A7677  E8 C4 63 04 00                  call 0x1403eda40
003A767C  C6 44 24 38 00                  mov byte ptr [rsp + 0x38], 0
003A7681  4C 8B C8                        mov r9, rax
003A7684  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
003A7688  45 33 C0                        xor r8d, r8d
003A768B  40 88 7C 24 30                  mov byte ptr [rsp + 0x30], dil
003A7690  33 D2                           xor edx, edx
003A7692  48 8B 7D F8                     mov rdi, qword ptr [rbp - 8]
003A7696  48 8B CF                        mov rcx, rdi
003A7699  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
003A769D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003A76A2  E8 A9 0E 0A 00                  call 0x140448550
003A76A7  45 33 DB                        xor r11d, r11d
003A76AA  45 39 1F                        cmp dword ptr [r15], r11d
003A76AD  7D 29                           jge 0x1403a76d8
003A76AF  44 39 5D 44                     cmp dword ptr [rbp + 0x44], r11d
003A76B3  75 23                           jne 0x1403a76d8
003A76B5  F7 87 C8 00 00 00 00 40 00 00   test dword ptr [rdi + 0xc8], 0x4000
003A76BF  74 17                           je 0x1403a76d8
003A76C1  8B D6                           mov edx, esi
003A76C3  48 8D 4D 38                     lea rcx, [rbp + 0x38]
003A76C7  E8 B8 AD 0B 00                  call 0x140462484
003A76CC  84 C0                           test al, al
003A76CE  74 08                           je 0x1403a76d8
003A76D0  E8 CB 71 07 00                  call 0x14041e8a0
003A76D5  45 33 DB                        xor r11d, r11d
003A76D8  44 38 5D 80                     cmp byte ptr [rbp - 0x80], r11b
003A76DC  74 09                           je 0x1403a76e7
003A76DE  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
003A76E2  E8 B5 A7 10 00                  call 0x1404b1e9c
003A76E7  45 84 ED                        test r13b, r13b
003A76EA  75 08                           jne 0x1403a76f4
003A76EC  49 8B CE                        mov rcx, r14
003A76EF  E8 2C EE 51 00                  call 0x1408c6520
003A76F4  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
003A76F8  E8 F3 A2 F5 FF                  call 0x1403019f0
003A76FD  80 7D 8B 00                     cmp byte ptr [rbp - 0x75], 0
003A7701  74 0A                           je 0x1403a770d
003A7703  80 7D 81 00                     cmp byte ptr [rbp - 0x7f], 0
003A7707  0F 85 3F FA FF FF               jne 0x1403a714c
003A770D  45 32 E4                        xor r12b, r12b
003A7710  E9 37 FA FF FF                  jmp 0x1403a714c
003A7715  41 C7 07 22 00 00 C0            mov dword ptr [r15], 0xc0000022
003A771C  45 33 FF                        xor r15d, r15d
003A771F  44 39 7D CC                     cmp dword ptr [rbp - 0x34], r15d
003A7723  75 3D                           jne 0x1403a7762
003A7725  49 8B 1E                        mov rbx, qword ptr [r14]
003A7728  48 85 DB                        test rbx, rbx
003A772B  75 04                           jne 0x1403a7731
003A772D  49 8B 5E 10                     mov rbx, qword ptr [r14 + 0x10]
003A7731  0B B5 C8 00 00 00               or esi, dword ptr [rbp + 0xc8]
003A7737  49 8B CE                        mov rcx, r14
003A773A  E8 01 63 04 00                  call 0x1403eda40
003A773F  44 88 7C 24 38                  mov byte ptr [rsp + 0x38], r15b
003A7744  4C 8B C8                        mov r9, rax
003A7747  44 88 7C 24 30                  mov byte ptr [rsp + 0x30], r15b
003A774C  33 D2                           xor edx, edx
003A774E  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
003A7752  48 8B CB                        mov rcx, rbx
003A7755  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
003A775A  45 33 C0                        xor r8d, r8d
003A775D  E8 EE 0D 0A 00                  call 0x140448550
003A7762  45 84 ED                        test r13b, r13b
003A7765  75 0D                           jne 0x1403a7774
003A7767  49 8B CE                        mov rcx, r14
003A776A  E8 B1 ED 51 00                  call 0x1408c6520
003A776F  EB 03                           jmp 0x1403a7774
003A7771  45 89 0F                        mov dword ptr [r15], r9d
003A7774  32 C0                           xor al, al
003A7776  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
003A777A  48 33 CC                        xor rcx, rsp
003A777D  E8 BE 4E 30 00                  call 0x1406ac640
003A7782  48 8B 9C 24 C8 01 00 00         mov rbx, qword ptr [rsp + 0x1c8]
003A778A  48 81 C4 80 01 00 00            add rsp, 0x180
003A7791  41 5F                           pop r15
003A7793  41 5E                           pop r14
003A7795  41 5D                           pop r13
003A7797  41 5C                           pop r12
003A7799  5F                              pop rdi
003A779A  5E                              pop rsi
003A779B  5D                              pop rbp
003A779C  C3                              ret
003A779D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeAccessCheckWithHint(__int64 a1, int a2, __int64 a3, unsigned __int8 a4, unsigned int a5, unsigned int a6, __int64 a7, __int64 a8, unsigned __int8 a9, __int64 a10, __int64 a11)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m104;
    unsigned __int8 v_stack_m108;
    unsigned int v_stack_m10C;
    unsigned __int8 v_stack_m10D;
    unsigned __int8 v_stack_m10E;
    unsigned __int8 v_stack_m10F;
    unsigned __int8 v_stack_m110;
    unsigned int v_stack_m114;
    unsigned __int8 v_stack_m115;
    unsigned __int8 v_stack_m116;
    unsigned __int8 v_stack_m117;
    unsigned __int8 v_stack_m118;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int8 v_stack_m148;
    unsigned __int8 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int8 v_stack_m170;
    unsigned int v_stack_m178;
    unsigned __int8 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int8 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m40;
    unsigned __int8 v_stack_m49;
    unsigned __int8 v_stack_m4A;
    unsigned __int8 v_stack_m4B;
    unsigned __int64 v_stack_m4C;
    unsigned int v_stack_m54;
    unsigned __int64 v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p30;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (384);
    result = (*(unsigned __int64 *)(v_rip + 10894061)) ^ (v_rsp);
    v_stack_m40 = result;
    v_r12 = 0;
    a3 = 0;
    v_stack_m100 = a1;
    v_stack_m68 = 0;
    a3 = (unsigned int)((a3) | (0xFFFFFFFFULL));
    v_stack_m10C = a2;
    result = (unsigned int)(((unsigned int)(a2)) & (8));
    *(unsigned int *)(a10) = 0;
    v_stack_mE0 = a7;
    v_stack_mB0 = a8;
    v_stack_m117 = 0;
    v_stack_m4C = 0;
    v_stack_mB8 = 0;
    v_stack_mE8 = 0;
    v_stack_m118 = 0;
    v_stack_m114 = 0;
    v_stack_mF8 = 0;
    v_stack_mF0 = 0;
    v_stack_m10F = 0;
    v_stack_m10E = 0;
    v_stack_mD0 = 0;
    *(unsigned int *)(a11) = (unsigned int)((unsigned int)(0xC0000022ULL));
    v_stack_mD8 = 0;
    v_stack_mC8 = (unsigned int)((unsigned int)(0xC0000022ULL));
    v_stack_mD4 = (unsigned int)(a3);
    v_stack_mA8 = (unsigned int)(a3);
    v_stack_mCC = (unsigned int)(result);
    v_stack_m98 = v_xmm0;
    v_stack_m5C = v_xmm1;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm0;
    if (a7 != 0) {
        *(unsigned __int64 *)(a7) = 0;
    }
    if (a9 != 0) goto loc_003A6D3C;
    v_rsi = (unsigned int)(a5);
    if (a9 < 0) {
        v_rsi = (unsigned int)(((unsigned int)(a5)) | (*(unsigned int *)(a8 + 12)));
    }
    v_rsi = (unsigned int)((v_rsi) | (a6));
    *(unsigned int *)(a10) = (unsigned int)(v_rsi);
    *(unsigned int *)(a11) = 0;
loc_003A6D32:
    goto loc_003A7776;
loc_003A6D3C:
    if (a1 == 0) goto loc_003A7771;
    if ((*(unsigned __int64 *)(a3)) == 0) goto loc_003A6D5D;
    if ((*(unsigned int *)(a3 + 8)) >= 2) goto loc_003A6D5D;
    *(unsigned int *)(a11) = 0xC00000A5ULL;
    goto loc_003A7774;
loc_003A6D5D:
    if ((unsigned int)(v_rsi) != 0) goto loc_003A6D7E;
    if ((unsigned int)((unsigned int)(a6)) == 0) goto loc_003A7771;
    *(unsigned int *)(a10) = (unsigned int)((unsigned int)(a6));
    *(unsigned int *)(a11) = 0;
    if (a7 == 0) goto loc_003A6D32;
    *(unsigned __int64 *)(a7) = 0;
    goto loc_003A6D32;
loc_003A6D7E:
    result = (unsigned int)(a6);
    if (a4 == 0) {
        a1 = a3;
        result = SeLockSubjectContext(a1, a8, a3, (unsigned int)(0xC0000022ULL));
    }
    a4 = 0;
    v_stack_m188 = v_stack_mD4;
    v_stack_m190 = 0;
    v_stack_m198 = 0;
    result = SepTrustLevelCheck(a1, a1, a3, a4);
    *(unsigned int *)(a11) = (unsigned int)(result);
    if (sign_flag) goto loc_003A7762;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & ((unsigned int)((unsigned int)(0xFDFFFFFFULL))));
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (v_stack_mD4));
    if (((unsigned int)(result)) != ((unsigned int)(a1))) goto loc_003A7715;
    a2 = 0;
    *(unsigned int *)(a11) = 0;
    v_stack_mA0 = *(unsigned __int64 *)(a3);
    v_rdi = *(unsigned __int64 *)(a3);
    if (*(unsigned __int64 *)(a3) == 0) {
        v_rdi = *(unsigned __int64 *)(a3 + 16);
        v_stack_mA0 = v_rdi;
    }
    if ((((unsigned __int8)((unsigned int)(v_stack_m10C))) & (4)) != 0) goto loc_003A6E2C;
    a4 = 0;
    v_stack_m198 = v_stack_mA8;
    result = SepFilterCheck(v_stack_m100, v_stack_mF8, v_rdi, a4);
    a2 = 0;
    *(unsigned int *)(a11) = (unsigned int)(result);
    if (sign_flag) goto loc_003A7762;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & ((unsigned int)((unsigned int)(0xFDFFFFFFULL))));
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (v_stack_mA8));
    if (((unsigned int)(result)) != ((unsigned int)(a1))) goto loc_003A6E4A;
    *(unsigned int *)(a11) = 0;
loc_003A6E2C:
    if ((((unsigned __int8)((unsigned int)(v_stack_m10C))) & (2)) == 0) goto loc_003A6E80;
    if (((*(unsigned int *)(v_rdi + 200)) & (0x2000ULL)) == 0) goto loc_003A6E83;
    goto loc_003A6E85;
loc_003A6E4A:
    *(unsigned int *)(a11) = 0xC0000022ULL;
    if (v_stack_mCC != 0) goto loc_003A7762;
    v_rsi = (unsigned int)((v_rsi) | (a6));
    a4 = 0;
    v_stack_m180 = 0;
    v_stack_m188 = 0;
    v_stack_m190 = (unsigned int)(v_rsi);
    v_stack_m198 = v_stack_m100;
    goto loc_003A775A;
loc_003A6E80:
loc_003A6E83:
loc_003A6E85:
    v_stack_m110 = 0;
    v_stack_m108 = 0;
    if ((*(unsigned __int8 *)(v_rip + 10903077)) != 0) goto loc_003A6EBE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 200)))) & (32)) != 0) goto loc_003A6EBE;
    if (*(unsigned __int64 *)(v_rdi + 216) == 0) goto loc_003A6EBE;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi + 216) + 40)))) & (32)) == 0) goto loc_003A6EBE;
    *(unsigned int *)(a10) = 0;
    *(unsigned int *)(a11) = 0xC0000022ULL;
    goto loc_003A7762;
loc_003A6EBE:
    if (0 != 0) goto loc_003A6F49;
    v_stack_m190 = v_stack_m98;
    v_stack_m198 = 0;
    result = SepMandatoryIntegrityCheck(v_stack_mB0, v_stack_m100, 0, v_rdi);
    *(unsigned int *)(a11) = (unsigned int)(result);
    if (sign_flag) goto loc_003A7762;
    result = SepMandatoryToDiscretionary(v_stack_m98, (unsigned int)((unsigned int)(v_rsi)), 0, v_rdi);
    *(unsigned int *)(a11) = (unsigned int)(result);
    if (!sign_flag) goto loc_003A6F23;
    if (((*(unsigned int *)(v_rdi + 200)) & (0x4000ULL)) == 0) goto loc_003A7762;
    if (v_stack_m8C > 0x2000ULL) goto loc_003A7762;
    v_stack_m108 = 1;
    goto loc_003A6F49;
loc_003A6F23:
    if (v_stack_m8C >= 0x2000ULL) goto loc_003A6F49;
    if (((*(unsigned int *)(v_rdi + 200)) & (0x4000ULL)) != 0) {
        result = v_stack_m108;
        result = (unsigned __int8)(result);
        if (v_stack_m8C <= 0x2000ULL) { result = 1; }
        v_stack_m108 = (unsigned int)(result);
    }
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(v_stack_m98, (unsigned int)((unsigned int)(v_rsi)), 0, v_rdi);
    v_r11 = 0;
    if ((unsigned int)(result) == 0) goto loc_003A6FAA;
    v_stack_m190 = v_stack_mD0;
    v_stack_m198 = (unsigned int)(v_rsi);
    a4 = (0 == 0) ? 1 : 0;
    a3 = 0;
    result = SepMandatoryAccessCheck(v_stack_m100, a3, a3, a4);
    v_r11 = 0;
    if (sign_flag) goto loc_003A6F8B;
    result = (unsigned int)(((unsigned int)(v_stack_mD0)) & ((unsigned int)(v_rsi)));
    if ((((unsigned int)(result)) & (0xFDFFFFFFULL)) == 0) goto loc_003A6FAA;
loc_003A6F8B:
    if (a4 == 0) {
        a1 = 0;
        result = SeUnlockSubjectContext(a1, a3, a3, a4);
        v_r11 = 0;
    }
    *(unsigned int *)(a10) = 0;
    *(unsigned int *)(a11) = 0xC00001C0ULL;
    goto loc_003A7774;
loc_003A6FAA:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11918101)) == 0) goto loc_003A702B;
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_m100 + 2))) & (16)) == 0) goto loc_003A702B;
    if (((unsigned __int8)(v_cr8)) >= 2) goto loc_003A702B;
    if (!sign_flag) goto loc_003A6FE0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m100 + 12))) != 0) goto loc_003A6FDB;
    v_stack_mB8 = 0;
    goto loc_003A702B;
loc_003A6FDB:
    result = ((unsigned int)(*(unsigned int *)(v_stack_m100 + 12))) + (v_stack_m100);
    goto loc_003A6FE4;
loc_003A6FE0:
loc_003A6FE4:
    v_stack_mB8 = *(unsigned __int64 *)(v_stack_m100 + 24);
    if (*(unsigned __int64 *)(v_stack_m100 + 24) == 0) goto loc_003A702B;
    result = SepGetScopedPolicySid(*(unsigned __int64 *)(v_stack_m100 + 24), v_stack_m100, a3, a4);
    if (result == 0) goto loc_003A7027;
    result = SepRmReferenceFindCap(result, v_stack_mE8, a3, a4);
    v_r11 = 0;
    v_stack_m118 = 1;
    a2 = v_stack_mE8;
    if (sign_flag) { a2 = *(unsigned __int64 *)(v_rip + 12783827); }
    v_stack_mE8 = a2;
    goto loc_003A702E;
loc_003A7027:
loc_003A702B:
loc_003A702E:
    if (((v_stack_m10C) & (1)) == 0) goto loc_003A7054;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & (0x2060000ULL));
    v_stack_m116 = 1;
    v_stack_m10C = (unsigned int)(result);
    if (condition_is_not_equal) goto loc_003A7060;
    v_stack_m10C = (unsigned int)(result);
    if ((unsigned __int8)(v_stack_m118) != 0) goto loc_003A7060;
    v_stack_m115 = 0;
    goto loc_003A70F0;
loc_003A7054:
    result = (unsigned int)((result) & (0x2060000ULL));
    v_stack_m116 = 0;
    v_stack_m10C = (unsigned int)(result);
loc_003A7060:
    result = SepTokenIsOwner(v_rdi, v_stack_m100, a3, a4);
    a4 = 0;
    v_stack_m115 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_003A70F0;
    if (v_stack_m10C == 0) goto loc_003A70F0;
    if (v_stack_m116 != 0) goto loc_003A70B6;
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_m100 + 2))) & (4)) != 0) goto loc_003A7091;
loc_003A708C:
    goto loc_003A70A8;
loc_003A7091:
    if (!sign_flag) goto loc_003A70A4;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m100 + 16))) == 0) goto loc_003A708C;
    goto loc_003A70A8;
loc_003A70A4:
loc_003A70A8:
    a1 = 0;
    result = RtlpOwnerAcesPresent(a1, *(unsigned __int64 *)(v_stack_m100 + 32), v_stack_m100, a4);
    a4 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_003A70F0;
loc_003A70B6:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & ((unsigned int)((unsigned int)(0x60000ULL))));
    a2 = (unsigned int)(0x60000ULL);
    if (condition_is_above_or_equal) { a2 = (unsigned int)(result); }
    v_rsi = (unsigned int)((v_rsi) & (0xFFF9FFFFULL));
    v_stack_m114 = a2;
    result = (unsigned int)(((unsigned int)(a2)) | (a6));
    v_stack_p30 = (unsigned int)(result);
    if (v_stack_m118 == 0) {
        v_stack_m115 = 0;
        v_stack_p30 = (unsigned int)(result);
        v_stack_m114 = a2;
    }
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(a1, a2, v_stack_m100, a4);
    a2 = 0;
    if ((unsigned int)(v_rsi) != 0) goto loc_003A715C;
    if (v_stack_m118 != 0) goto loc_003A715C;
    if ((unsigned int)(result) == 0) goto loc_003A7154;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 200))))) & ((unsigned int)((unsigned int)(0x6000ULL))));
    if (((unsigned int)(result)) == 0x2000ULL) goto loc_003A7132;
loc_003A711C:
    if ((unsigned int)((unsigned int)(v_stack_m114)) == 0) goto loc_003A7132;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 200))) & ((unsigned int)((unsigned int)(0x6000ULL))));
    if (((unsigned int)(a1)) == 0x2000ULL) goto loc_003A7132;
    if ((unsigned int)((unsigned int)(v_stack_m114)) != 0) goto loc_003A715F;
loc_003A7132:
    result = (unsigned int)(v_stack_m114);
    if (0 == 0) {
        a1 = 0;
        result = SeUnlockSubjectContext(a1, a2, (unsigned int)(0x6000ULL), a4);
        a2 = 0;
    }
    *(unsigned int *)(a10) = (unsigned int)((unsigned int)(a6));
    *(unsigned int *)(a11) = 0;
loc_003A714C:
    goto loc_003A7776;
loc_003A7154:
    if (condition_is_below) goto loc_003A7132;
    goto loc_003A711C;
loc_003A715C:
loc_003A715F:
    v_stack_m128 = 0;
    v_stack_m60 = (unsigned int)((unsigned int)(v_stack_m114));
    v_stack_m130 = v_stack_m117;
    v_stack_m138 = v_stack_mF8;
    v_stack_m140 = v_stack_m60;
    v_stack_m148 = (unsigned __int8)(v_stack_m115);
    v_stack_m150 = 0;
    v_stack_m158 = a11;
    v_stack_m160 = v_stack_mE0;
    v_stack_m168 = a10;
    v_stack_m170 = a9;
    v_stack_m178 = (unsigned int)((unsigned int)(a6));
    v_stack_m180 = v_stack_mB0;
    v_stack_m188 = 0;
    v_stack_m190 = 0;
    v_stack_m198 = (unsigned int)(v_rsi);
    v_stack_m5C = v_xmm0;
    v_stack_m4C = 0;
    result = SepAccessCheck(v_stack_m100, a2, *(unsigned __int64 *)(a3 + 16), *(unsigned __int64 *)(a3));
    v_r11 = 0;
    v_stack_m10D = (unsigned __int8)(result);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11917520)) == 0) goto loc_003A751B;
    v_stack_mC4 = (unsigned int)((unsigned int)(*(unsigned int *)(a11)));
    if (sign_flag) goto loc_003A751B;
    if (v_stack_m118 == 0) goto loc_003A751B;
    v_stack_m116 = 0;
    v_stack_m114 = (unsigned int)((unsigned int)(*(unsigned int *)(a10)));
    v_stack_m10C = 0;
    v_stack_mC0 = 0;
    if ((*(unsigned int *)(v_stack_mE8 + 60)) <= 0) goto loc_003A750D;
loc_003A723D:
    v_stack_mE0 = *(unsigned __int64 *)(v_stack_mE8 + 0 * 8 + 64);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE8 + 0 * 8 + 64) + 24)) == 0) goto loc_003A73C5;
    result = 0;
    if (v_stack_mF8 == 0) {
        a1 = v_stack_mB8;
        a2 = v_stack_mF8;
        result = AuthzBasepInitializeResourceClaimsFromSacl(a1, a2, v_stack_mF8, *(unsigned __int64 *)(a3));
        a4 = v_stack_m10C;
        v_r11 = 0;
        a3 = v_stack_mF8;
        a1 = v_stack_mE0;
        a4 = a4;
        if (sign_flag) { a4 = 1; }
        v_stack_m10C = a4;
    }
    if (*(unsigned __int64 *)(v_rdi + 1096) == 0) goto loc_003A72B0;
    goto loc_003A72B9;
loc_003A72B0:
loc_003A72B9:
    v_stack_m160 = v_stack_mF0;
    v_stack_m168 = 0;
    v_stack_m170 = 1;
    v_stack_m178 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)));
    v_stack_m180 = *(unsigned __int64 *)(a1 + 24);
    v_stack_m188 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 1096) + 600);
    v_stack_m190 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 1096) + 600);
    v_stack_m198 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 1096) + 600);
    result = AuthzBasepEvaluateAceCondition(v_rdi, *(unsigned __int64 *)(v_rdi + 776), a3, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 1096) + 600));
    v_stack_m104 = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(v_stack_mF0))) == 1) goto loc_003A73C1;
    v_r11 = 0;
    if (sign_flag) goto loc_003A74D8;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 200)))) & (16)) == 0) goto loc_003A73B2;
    if (*(unsigned __int64 *)(v_rdi + 1096) == 0) goto loc_003A734C;
    goto loc_003A7358;
loc_003A734C:
loc_003A7358:
    v_stack_m160 = v_stack_mF0;
    v_stack_m168 = 1;
    v_stack_m170 = 1;
    v_stack_m178 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mE0 + 16)));
    v_stack_m180 = *(unsigned __int64 *)(v_stack_mE0 + 24);
    v_stack_m188 = 0;
    v_stack_m190 = 0;
    v_stack_m198 = 0;
    result = AuthzBasepEvaluateAceCondition(v_rdi, *(unsigned __int64 *)(v_rdi + 776), v_stack_mF8, 0);
    v_r11 = 0;
    v_stack_m104 = (unsigned int)(result);
    if (sign_flag) goto loc_003A74D8;
loc_003A73B2:
    if (v_stack_m10C != 0) goto loc_003A73C1;
    if (((unsigned int)((unsigned int)(v_stack_mF0))) != 1) goto loc_003A74BA;
loc_003A73C1:
loc_003A73C5:
    result = SepBuildCapeSecurityDescriptor(v_stack_m88, *(unsigned __int64 *)(v_stack_mE0 + 32), v_stack_mB8, 0);
    a3 = 0;
    v_stack_m104 = (unsigned int)(result);
    if (sign_flag) goto loc_003A74D8;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mE0 + 48))))) == 0) goto loc_003A7403;
    result = (unsigned int)((unsigned int)(v_rsi));
    if (!(condition_is_below)) {
        result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) | (a6));
    }
    goto loc_003A7409;
loc_003A7403:
loc_003A7409:
    v_stack_m128 = 0;
    v_stack_m130 = v_stack_m117;
    v_stack_m138 = v_stack_mF8;
    v_stack_m140 = v_stack_m60;
    v_stack_m148 = (unsigned __int8)(v_stack_m115);
    v_stack_m150 = 0;
    v_stack_m158 = v_stack_mC8;
    v_stack_m160 = 0;
    v_stack_m168 = v_stack_mD8;
    v_stack_m170 = a9;
    a2 = 0;
    v_stack_m178 = (unsigned int)((unsigned int)(a6));
    v_stack_m180 = v_stack_mB0;
    v_stack_m188 = 0;
    v_stack_m190 = 0;
    v_stack_m198 = (unsigned int)(result);
    result = SepAccessCheck(v_stack_m88, a2, *(unsigned __int64 *)(a3 + 16), *(unsigned __int64 *)(a3));
    v_r11 = 0;
    v_stack_m10D = (unsigned __int8)(result);
    if (v_stack_m116 != 0) goto loc_003A749D;
    goto loc_003A74A3;
loc_003A749D:
    result = (unsigned int)(((unsigned int)(v_stack_m114)) & (v_stack_mD8));
loc_003A74A3:
    v_stack_m114 = (unsigned int)(result);
    if ((unsigned int)(result) == 0) goto loc_003A7505;
    v_stack_mC4 = (unsigned int)((unsigned int)(v_stack_mC8));
    v_stack_m116 = 1;
    if (sign_flag) goto loc_003A750A;
    goto loc_003A74BD;
loc_003A74BA:
loc_003A74BD:
    a3 = (unsigned int)(((unsigned int)(v_stack_mC0)) + (1));
    v_stack_mC0 = (unsigned int)(a3);
    if (((unsigned int)(a3)) < (*(unsigned int *)(v_stack_mE8 + 60))) goto loc_003A723D;
    goto loc_003A750A;
loc_003A74D8:
    result = (unsigned int)(v_stack_mC4);
    if (a4 == 0) {
        a1 = a3;
        result = SeUnlockSubjectContext(a1, a2, a3, *(unsigned __int64 *)(a3));
    }
    result = SepRmDereferenceCap(v_stack_mE8, a2, a3, *(unsigned __int64 *)(a3));
    *(unsigned int *)(a11) = (unsigned int)((unsigned int)(v_stack_m104));
    result = SepFreeResourceInfo(v_stack_mF8, a2, a3, *(unsigned __int64 *)(a3));
    goto loc_003A7774;
loc_003A7505:
loc_003A750A:
loc_003A750D:
    *(unsigned int *)(a11) = (unsigned int)((unsigned int)(0xC0000022ULL));
    if ((*(unsigned int *)(a11)) < 0) {
        v_stack_m117 = 0;
    }
    if (v_stack_m110 != 0) goto loc_003A7576;
    if (v_stack_m110 >= 0) goto loc_003A7576;
    if (v_stack_m108 == 0) goto loc_003A7552;
    if (v_stack_m4A != 0) goto loc_003A75CA;
    if (v_stack_m4B != 0) goto loc_003A75CA;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 200))) & ((unsigned int)((unsigned int)(0x3000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x3000000ULL)))) goto loc_003A75CA;
loc_003A7552:
    v_stack_m190 = 0;
    v_stack_m198 = v_stack_m117;
    result = SepConstrainByMandatory(v_stack_m98, (unsigned int)((unsigned int)(v_rsi)), a10, a11);
    v_r11 = 0;
    goto loc_003A75CA;
loc_003A7576:
    if (v_stack_m108 == 0) goto loc_003A75C4;
    if (v_stack_m4A != 0) goto loc_003A75C4;
    if (v_stack_m4B != 0) goto loc_003A75C4;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 200))) & ((unsigned int)((unsigned int)(0x3000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x3000000ULL)))) goto loc_003A75B6;
    if (v_stack_m54 != 0) goto loc_003A75B6;
    *(unsigned int *)(a11) = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) | (a6));
    *(unsigned int *)(a10) = (unsigned int)(result);
    v_stack_m49 = 1;
    v_stack_m117 = 1;
    goto loc_003A75C4;
loc_003A75B6:
    *(unsigned int *)(a11) = 0xC0000022ULL;
    *(unsigned int *)(a10) = 0;
    v_stack_m117 = 0;
loc_003A75C4:
    if (condition_is_above_or_equal) goto loc_003A762B;
loc_003A75CA:
    v_stack_m188 = v_stack_m10F;
    v_stack_m190 = 0;
    v_stack_m198 = v_stack_m117;
    result = SepConstrainByConstraintMask((unsigned int)(v_stack_mD4), (unsigned int)((unsigned int)(v_rsi)), a10, a11);
    v_stack_m188 = v_stack_m10E;
    v_stack_m198 = v_stack_m117;
    result = SepConstrainByConstraintMask((unsigned int)(v_stack_mA8), (unsigned int)((unsigned int)(v_rsi)), a10, a11);
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline((unsigned int)(v_stack_mA8), (unsigned int)((unsigned int)(v_rsi)), a10, a11);
    v_r11 = 0;
    if ((unsigned int)(result) != 0) {
        result = v_stack_mD0;
        result = (unsigned int)(~(result));
    }
    if (v_rdi == 0) goto loc_003A76D8;
    if (v_stack_m10F != 0) goto loc_003A765D;
    if (v_stack_m10E != 0) goto loc_003A765D;
    if (v_stack_m54 != 0) goto loc_003A76AA;
    if (((*(unsigned int *)(v_rdi + 200)) & (0x4000ULL)) == 0) goto loc_003A76AA;
    if ((*(unsigned int *)(a11)) < 0) goto loc_003A765D;
    if (v_stack_m49 == 0) goto loc_003A76AA;
loc_003A765D:
    v_rbx = a10;
    if (v_stack_mCC == 0) {
        v_rdi = *(unsigned int *)(a11);
        v_rbx = (unsigned int)(v_rsi);
        v_rbx = (unsigned int)((v_rbx) | (a6));
        a1 = a3;
        v_rdi = (unsigned int)((v_rdi) >> (31));
        v_rdi = (unsigned __int8)((v_rdi) ^ (1));
        result = SepLocateTokenTrustLevel(a1, (unsigned int)((unsigned int)(v_rsi)), a10, a11);
        v_stack_m180 = 0;
        a4 = result;
        result = v_stack_m100;
        a3 = 0;
        v_stack_m188 = (unsigned __int8)(v_rdi);
        a2 = 0;
        v_rdi = v_stack_mA0;
        a1 = v_rdi;
        v_stack_m190 = (unsigned int)(v_rbx);
        v_stack_m198 = result;
        result = SeLogAccessFailure(a1, a2, a3, a4);
        v_r11 = 0;
    }
    if ((*(unsigned int *)(a11)) >= 0) goto loc_003A76D8;
    if (v_stack_m54 != 0) goto loc_003A76D8;
    if (((*(unsigned int *)(v_rdi + 200)) & (0x4000ULL)) == 0) goto loc_003A76D8;
    result = SepLpacCausedAccessFailure(v_stack_m60, (unsigned int)((unsigned int)(v_rsi)), a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = SepLogLpacAccessFailure(v_stack_m60, (unsigned int)((unsigned int)(v_rsi)), a3, a4);
        v_r11 = 0;
    }
    if (v_stack_m118 != 0) {
        a1 = v_stack_mE8;
        result = SepRmDereferenceCap(a1, (unsigned int)((unsigned int)(v_rsi)), a3, a4);
    }
    if (a4 == 0) {
        a1 = 0;
        result = SeUnlockSubjectContext(a1, (unsigned int)((unsigned int)(v_rsi)), a3, a4);
    }
    result = SepFreeResourceInfo(v_stack_mF8, (unsigned int)((unsigned int)(v_rsi)), a3, a4);
    if (v_stack_m10D == 0) goto loc_003A770D;
    if (v_stack_m117 != 0) goto loc_003A714C;
loc_003A770D:
    v_r12 = 0;
    goto loc_003A714C;
loc_003A7715:
    *(unsigned int *)(a11) = 0xC0000022ULL;
    v_r15 = 0;
    if (v_stack_mCC != 0) goto loc_003A7762;
    v_rbx = *(unsigned __int64 *)(a3);
    if (*(unsigned __int64 *)(a3) == 0) {
        v_rbx = *(unsigned __int64 *)(a3 + 16);
    }
    v_rsi = (unsigned int)((v_rsi) | (a6));
    result = SepLocateTokenTrustLevel(0, (unsigned int)((unsigned int)(v_rsi)), a3, a4);
    v_stack_m180 = 0;
    v_stack_m188 = 0;
    a2 = 0;
    v_stack_m190 = (unsigned int)(v_rsi);
    v_stack_m198 = v_rdi;
loc_003A775A:
    a3 = 0;
    result = SeLogAccessFailure(v_rbx, a2, a3, result);
loc_003A7762:
    if (a4 != 0) goto loc_003A7774;
    result = SeUnlockSubjectContext(0, a2, a3, result);
    goto loc_003A7774;
loc_003A7771:
    *(unsigned int *)(v_r15) = (unsigned int)(result);
loc_003A7774:
    result = 0;
loc_003A7776:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, result);
    v_rsp = (v_rsp) + (384);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SeAccessCheckWithHint(int64_t Arg1, int32_t Arg2, void *Arg3, uint8_t Arg4, uint32_t Arg5, uint32_t Arg6, int64_t Arg7, void *Arg8, uint8_t Arg9, void *Arg10, void *Arg11)
{
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg8 = (uint8_t *)Arg8;
    uint8_t *arg10 = (uint8_t *)Arg10;
    uint8_t *arg11 = (uint8_t *)Arg11;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m104;
    uint8_t v_stack_m108;
    uint32_t v_stack_m10C;
    uint8_t v_stack_m10D;
    uint8_t v_stack_m10E;
    uint8_t v_stack_m10F;
    uint8_t v_stack_m110;
    uint32_t v_stack_m114;
    uint8_t v_stack_m115;
    uint8_t v_stack_m116;
    uint8_t v_stack_m117;
    uint8_t v_stack_m118;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint8_t v_stack_m148;
    uint8_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint8_t v_stack_m170;
    uint32_t v_stack_m178;
    uint8_t v_stack_m180;
    uint64_t v_stack_m188;
    uint8_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m40;
    uint8_t v_stack_m49;
    uint8_t v_stack_m4A;
    uint8_t v_stack_m4B;
    uint64_t v_stack_m4C;
    uint32_t v_stack_m54;
    uint64_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint32_t v_stack_p30;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (384);
    result = (*(uint64_t *)(v_rip + 0xA63AED)) ^ (local_rsp);
    v_stack_m40 = result;
    local_r12 = 0;
    Arg3 = 0;
    v_stack_m100 = Arg1;
    v_stack_m68 = 0;
    Arg3 = (uint32_t)((Arg3) | (0xFFFFFFFFULL));
    v_stack_m10C = Arg2;
    result = (uint32_t)(((uint32_t)(Arg2)) & (8));
    *(uint32_t *)(arg10) = 0;
    v_stack_mE0 = Arg7;
    v_stack_mB0 = Arg8;
    v_stack_m117 = 0;
    v_stack_m4C = 0;
    v_stack_mB8 = 0;
    v_stack_mE8 = 0;
    v_stack_m118 = 0;
    v_stack_m114 = 0;
    v_stack_mF8 = 0;
    v_stack_mF0 = 0;
    v_stack_m10F = 0;
    v_stack_m10E = 0;
    v_stack_mD0 = 0;
    *(uint32_t *)(arg11) = (uint32_t)((uint32_t)(0xC0000022ULL));
    v_stack_mD8 = 0;
    v_stack_mC8 = (uint32_t)((uint32_t)(0xC0000022ULL));
    v_stack_mD4 = (uint32_t)(Arg3);
    v_stack_mA8 = (uint32_t)(Arg3);
    v_stack_mCC = (uint32_t)(result);
    v_stack_m98 = v_xmm0;
    v_stack_m5C = v_xmm1;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm0;
    if (Arg7 != 0) {
        *(uint64_t *)(Arg7) = 0;
    }
    if (Arg9 != 0) goto loc_003A6D3C;
    local_rsi = (uint32_t)(Arg5);
    if (Arg9 < 0) {
        local_rsi = (uint32_t)(((uint32_t)(Arg5)) | (*(uint32_t *)(arg8 + 0xC)));
    }
    local_rsi = (uint32_t)((local_rsi) | (Arg6));
    *(uint32_t *)(arg10) = (uint32_t)(local_rsi);
    *(uint32_t *)(arg11) = 0;
loc_003A6D32:
    goto loc_003A7776;
loc_003A6D3C:
    if (Arg1 == 0) goto loc_003A7771;
    if ((*(uint64_t *)(arg3)) == 0) goto loc_003A6D5D;
    if ((*(uint32_t *)(arg3 + 0x8)) >= 2) goto loc_003A6D5D;
    *(uint32_t *)(arg11) = 0xC00000A5ULL;
    goto loc_003A7774;
loc_003A6D5D:
    if ((uint32_t)(local_rsi) != 0) goto loc_003A6D7E;
    if ((uint32_t)((uint32_t)(Arg6)) == 0) goto loc_003A7771;
    *(uint32_t *)(arg10) = (uint32_t)((uint32_t)(Arg6));
    *(uint32_t *)(arg11) = 0;
    if (Arg7 == 0) goto loc_003A6D32;
    *(uint64_t *)(Arg7) = 0;
    goto loc_003A6D32;
loc_003A6D7E:
    result = (uint32_t)(Arg6);
    if (Arg4 == 0) {
        Arg1 = Arg3;
        result = SeLockSubjectContext(Arg1, Arg8, Arg3, (uint32_t)(0xC0000022ULL));
    }
    Arg4 = 0;
    v_stack_m188 = v_stack_mD4;
    v_stack_m190 = 0;
    v_stack_m198 = 0;
    result = SepTrustLevelCheck(Arg1, Arg1, Arg3, Arg4);
    *(uint32_t *)(arg11) = (uint32_t)(result);
    if (sign_flag) goto loc_003A7762;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & ((uint32_t)((uint32_t)(0xFDFFFFFFULL))));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (v_stack_mD4));
    if (((uint32_t)(result)) != ((uint32_t)(Arg1))) goto loc_003A7715;
    Arg2 = 0;
    *(uint32_t *)(arg11) = 0;
    v_stack_mA0 = *(uint64_t *)(arg3);
    local_rdi = *(uint64_t *)(arg3);
    if (*(uint64_t *)(arg3) == 0) {
        local_rdi = *(uint64_t *)(arg3 + 0x10);
        v_stack_mA0 = local_rdi;
    }
    if ((((uint8_t)((uint32_t)(v_stack_m10C))) & (4)) != 0) goto loc_003A6E2C;
    Arg4 = 0;
    v_stack_m198 = v_stack_mA8;
    result = SepFilterCheck(v_stack_m100, v_stack_mF8, local_rdi, Arg4);
    Arg2 = 0;
    *(uint32_t *)(arg11) = (uint32_t)(result);
    if (sign_flag) goto loc_003A7762;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & ((uint32_t)((uint32_t)(0xFDFFFFFFULL))));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (v_stack_mA8));
    if (((uint32_t)(result)) != ((uint32_t)(Arg1))) goto loc_003A6E4A;
    *(uint32_t *)(arg11) = 0;
loc_003A6E2C:
    if ((((uint8_t)((uint32_t)(v_stack_m10C))) & (2)) == 0) goto loc_003A6E80;
    if (((*(uint32_t *)(local_rdi + 0xC8)) & (0x2000ULL)) == 0) goto loc_003A6E83;
    goto loc_003A6E85;
loc_003A6E4A:
    *(uint32_t *)(arg11) = 0xC0000022ULL;
    if (v_stack_mCC != 0) goto loc_003A7762;
    local_rsi = (uint32_t)((local_rsi) | (Arg6));
    Arg4 = 0;
    v_stack_m180 = 0;
    v_stack_m188 = 0;
    v_stack_m190 = (uint32_t)(local_rsi);
    v_stack_m198 = v_stack_m100;
    goto loc_003A775A;
loc_003A6E80:
loc_003A6E83:
loc_003A6E85:
    v_stack_m110 = 0;
    v_stack_m108 = 0;
    if ((*(uint8_t *)(v_rip + 0xA65E25)) != 0) goto loc_003A6EBE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0xC8)))) & (32)) != 0) goto loc_003A6EBE;
    if (*(uint64_t *)(local_rdi + 0xD8) == 0) goto loc_003A6EBE;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi + 0xD8) + 0x28)))) & (32)) == 0) goto loc_003A6EBE;
    *(uint32_t *)(arg10) = 0;
    *(uint32_t *)(arg11) = 0xC0000022ULL;
    goto loc_003A7762;
loc_003A6EBE:
    if (0 != 0) goto loc_003A6F49;
    v_stack_m190 = v_stack_m98;
    v_stack_m198 = 0;
    result = SepMandatoryIntegrityCheck(v_stack_mB0, v_stack_m100, 0, local_rdi);
    *(uint32_t *)(arg11) = (uint32_t)(result);
    if (sign_flag) goto loc_003A7762;
    result = SepMandatoryToDiscretionary(v_stack_m98, (uint32_t)((uint32_t)(local_rsi)), 0, local_rdi);
    *(uint32_t *)(arg11) = (uint32_t)(result);
    if (!sign_flag) goto loc_003A6F23;
    if (((*(uint32_t *)(local_rdi + 0xC8)) & (0x4000ULL)) == 0) goto loc_003A7762;
    if (v_stack_m8C > 0x2000ULL) goto loc_003A7762;
    v_stack_m108 = 1;
    goto loc_003A6F49;
loc_003A6F23:
    if (v_stack_m8C >= 0x2000ULL) goto loc_003A6F49;
    if (((*(uint32_t *)(local_rdi + 0xC8)) & (0x4000ULL)) != 0) {
        result = v_stack_m108;
        result = (uint8_t)(result);
        if (v_stack_m8C <= 0x2000ULL) { result = 1; }
        v_stack_m108 = (uint32_t)(result);
    }
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(v_stack_m98, (uint32_t)((uint32_t)(local_rsi)), 0, local_rdi);
    local_r11 = 0;
    if ((uint32_t)(result) == 0) goto loc_003A6FAA;
    v_stack_m190 = v_stack_mD0;
    v_stack_m198 = (uint32_t)(local_rsi);
    Arg4 = (0 == 0) ? 1 : 0;
    Arg3 = 0;
    result = SepMandatoryAccessCheck(v_stack_m100, Arg3, Arg3, Arg4);
    local_r11 = 0;
    if (sign_flag) goto loc_003A6F8B;
    result = (uint32_t)(((uint32_t)(v_stack_mD0)) & ((uint32_t)(local_rsi)));
    if ((((uint32_t)(result)) & (0xFDFFFFFFULL)) == 0) goto loc_003A6FAA;
loc_003A6F8B:
    if (Arg4 == 0) {
        Arg1 = 0;
        result = SeUnlockSubjectContext(Arg1, Arg3, Arg3, Arg4);
        local_r11 = 0;
    }
    *(uint32_t *)(arg10) = 0;
    *(uint32_t *)(arg11) = 0xC00001C0ULL;
    goto loc_003A7774;
loc_003A6FAA:
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xB5DB15)) == 0) goto loc_003A702B;
    if ((((uint8_t)(*(uint16_t *)(v_stack_m100 + 0x2))) & (16)) == 0) goto loc_003A702B;
    if (((uint8_t)(v_cr8)) >= 2) goto loc_003A702B;
    if (!sign_flag) goto loc_003A6FE0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m100 + 0xC))) != 0) goto loc_003A6FDB;
    v_stack_mB8 = 0;
    goto loc_003A702B;
loc_003A6FDB:
    result = ((uint32_t)(*(uint32_t *)(v_stack_m100 + 0xC))) + (v_stack_m100);
    goto loc_003A6FE4;
loc_003A6FE0:
loc_003A6FE4:
    v_stack_mB8 = *(uint64_t *)(v_stack_m100 + 0x18);
    if (*(uint64_t *)(v_stack_m100 + 0x18) == 0) goto loc_003A702B;
    result = SepGetScopedPolicySid(*(uint64_t *)(v_stack_m100 + 0x18), v_stack_m100, Arg3, Arg4);
    if (result == 0) goto loc_003A7027;
    result = SepRmReferenceFindCap(result, v_stack_mE8, Arg3, Arg4);
    local_r11 = 0;
    v_stack_m118 = 1;
    Arg2 = v_stack_mE8;
    if (sign_flag) { Arg2 = *(uint64_t *)(v_rip + 0xC310D3); }
    v_stack_mE8 = Arg2;
    goto loc_003A702E;
loc_003A7027:
loc_003A702B:
loc_003A702E:
    if (((v_stack_m10C) & (1)) == 0) goto loc_003A7054;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & (0x2060000ULL));
    v_stack_m116 = 1;
    v_stack_m10C = (uint32_t)(result);
    if (condition_is_not_equal) goto loc_003A7060;
    v_stack_m10C = (uint32_t)(result);
    if ((uint8_t)(v_stack_m118) != 0) goto loc_003A7060;
    v_stack_m115 = 0;
    goto loc_003A70F0;
loc_003A7054:
    result = (uint32_t)((result) & (0x2060000ULL));
    v_stack_m116 = 0;
    v_stack_m10C = (uint32_t)(result);
loc_003A7060:
    result = SepTokenIsOwner(local_rdi, v_stack_m100, Arg3, Arg4);
    Arg4 = 0;
    v_stack_m115 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_003A70F0;
    if (v_stack_m10C == 0) goto loc_003A70F0;
    if (v_stack_m116 != 0) goto loc_003A70B6;
    if ((((uint8_t)(*(uint16_t *)(v_stack_m100 + 0x2))) & (4)) != 0) goto loc_003A7091;
loc_003A708C:
    goto loc_003A70A8;
loc_003A7091:
    if (!sign_flag) goto loc_003A70A4;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m100 + 0x10))) == 0) goto loc_003A708C;
    goto loc_003A70A8;
loc_003A70A4:
loc_003A70A8:
    Arg1 = 0;
    result = RtlpOwnerAcesPresent(Arg1, *(uint64_t *)(v_stack_m100 + 0x20), v_stack_m100, Arg4);
    Arg4 = 0;
    if ((uint8_t)(result) != 0) goto loc_003A70F0;
loc_003A70B6:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & ((uint32_t)((uint32_t)(0x60000ULL))));
    Arg2 = (uint32_t)(0x60000ULL);
    if (condition_is_above_or_equal) { Arg2 = (uint32_t)(result); }
    local_rsi = (uint32_t)((local_rsi) & (0xFFF9FFFFULL));
    v_stack_m114 = Arg2;
    result = (uint32_t)(((uint32_t)(Arg2)) | (Arg6));
    v_stack_p30 = (uint32_t)(result);
    if (v_stack_m118 == 0) {
        v_stack_m115 = 0;
        v_stack_p30 = (uint32_t)(result);
        v_stack_m114 = Arg2;
    }
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, v_stack_m100, Arg4);
    Arg2 = 0;
    if ((uint32_t)(local_rsi) != 0) goto loc_003A715C;
    if (v_stack_m118 != 0) goto loc_003A715C;
    if ((uint32_t)(result) == 0) goto loc_003A7154;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0xC8))))) & ((uint32_t)((uint32_t)(0x6000ULL))));
    if (((uint32_t)(result)) == 0x2000ULL) goto loc_003A7132;
loc_003A711C:
    if ((uint32_t)((uint32_t)(v_stack_m114)) == 0) goto loc_003A7132;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0xC8))) & ((uint32_t)((uint32_t)(0x6000ULL))));
    if (((uint32_t)(Arg1)) == 0x2000ULL) goto loc_003A7132;
    if ((uint32_t)((uint32_t)(v_stack_m114)) != 0) goto loc_003A715F;
loc_003A7132:
    result = (uint32_t)(v_stack_m114);
    if (0 == 0) {
        Arg1 = 0;
        result = SeUnlockSubjectContext(Arg1, Arg2, (uint32_t)(0x6000ULL), Arg4);
        Arg2 = 0;
    }
    *(uint32_t *)(arg10) = (uint32_t)((uint32_t)(Arg6));
    *(uint32_t *)(arg11) = 0;
loc_003A714C:
    goto loc_003A7776;
loc_003A7154:
    if (condition_is_below) goto loc_003A7132;
    goto loc_003A711C;
loc_003A715C:
loc_003A715F:
    v_stack_m128 = 0;
    v_stack_m60 = (uint32_t)((uint32_t)(v_stack_m114));
    v_stack_m130 = v_stack_m117;
    v_stack_m138 = v_stack_mF8;
    v_stack_m140 = v_stack_m60;
    v_stack_m148 = (uint8_t)(v_stack_m115);
    v_stack_m150 = 0;
    v_stack_m158 = Arg11;
    v_stack_m160 = v_stack_mE0;
    v_stack_m168 = Arg10;
    v_stack_m170 = Arg9;
    v_stack_m178 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m180 = v_stack_mB0;
    v_stack_m188 = 0;
    v_stack_m190 = 0;
    v_stack_m198 = (uint32_t)(local_rsi);
    v_stack_m5C = v_xmm0;
    v_stack_m4C = 0;
    result = SepAccessCheck(v_stack_m100, Arg2, *(uint64_t *)(arg3 + 0x10), *(uint64_t *)(arg3));
    local_r11 = 0;
    v_stack_m10D = (uint8_t)(result);
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xB5D8D0)) == 0) goto loc_003A751B;
    v_stack_mC4 = (uint32_t)((uint32_t)(*(uint32_t *)(arg11)));
    if (sign_flag) goto loc_003A751B;
    if (v_stack_m118 == 0) goto loc_003A751B;
    v_stack_m116 = 0;
    v_stack_m114 = (uint32_t)((uint32_t)(*(uint32_t *)(arg10)));
    v_stack_m10C = 0;
    v_stack_mC0 = 0;
    if ((*(uint32_t *)(v_stack_mE8 + 0x3C)) <= 0) goto loc_003A750D;
loc_003A723D:
    v_stack_mE0 = *(uint64_t *)(v_stack_mE8 + 0x0 * 8 + 0x40);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mE8 + 0x0 * 8 + 0x40) + 0x18)) == 0) goto loc_003A73C5;
    result = 0;
    if (v_stack_mF8 == 0) {
        Arg1 = v_stack_mB8;
        Arg2 = v_stack_mF8;
        result = AuthzBasepInitializeResourceClaimsFromSacl(Arg1, Arg2, v_stack_mF8, *(uint64_t *)(arg3));
        Arg4 = v_stack_m10C;
        local_r11 = 0;
        Arg3 = v_stack_mF8;
        Arg1 = v_stack_mE0;
        Arg4 = Arg4;
        if (sign_flag) { Arg4 = 1; }
        v_stack_m10C = Arg4;
    }
    if (*(uint64_t *)(local_rdi + 0x448) == 0) goto loc_003A72B0;
    goto loc_003A72B9;
loc_003A72B0:
loc_003A72B9:
    v_stack_m160 = v_stack_mF0;
    v_stack_m168 = 0;
    v_stack_m170 = 1;
    v_stack_m178 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x10)));
    v_stack_m180 = *(uint64_t *)(Arg1 + 0x18);
    v_stack_m188 = *(uint64_t *)(*(uint64_t *)(local_rdi + 0x448) + 0x258);
    v_stack_m190 = *(uint64_t *)(*(uint64_t *)(local_rdi + 0x448) + 0x258);
    v_stack_m198 = *(uint64_t *)(*(uint64_t *)(local_rdi + 0x448) + 0x258);
    result = AuthzBasepEvaluateAceCondition(local_rdi, *(uint64_t *)(local_rdi + 0x308), Arg3, *(uint64_t *)(*(uint64_t *)(local_rdi + 0x448) + 0x258));
    v_stack_m104 = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(v_stack_mF0))) == 1) goto loc_003A73C1;
    local_r11 = 0;
    if (sign_flag) goto loc_003A74D8;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0xC8)))) & (16)) == 0) goto loc_003A73B2;
    if (*(uint64_t *)(local_rdi + 0x448) == 0) goto loc_003A734C;
    goto loc_003A7358;
loc_003A734C:
loc_003A7358:
    v_stack_m160 = v_stack_mF0;
    v_stack_m168 = 1;
    v_stack_m170 = 1;
    v_stack_m178 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mE0 + 0x10)));
    v_stack_m180 = *(uint64_t *)(v_stack_mE0 + 0x18);
    v_stack_m188 = 0;
    v_stack_m190 = 0;
    v_stack_m198 = 0;
    result = AuthzBasepEvaluateAceCondition(local_rdi, *(uint64_t *)(local_rdi + 0x308), v_stack_mF8, 0);
    local_r11 = 0;
    v_stack_m104 = (uint32_t)(result);
    if (sign_flag) goto loc_003A74D8;
loc_003A73B2:
    if (v_stack_m10C != 0) goto loc_003A73C1;
    if (((uint32_t)((uint32_t)(v_stack_mF0))) != 1) goto loc_003A74BA;
loc_003A73C1:
loc_003A73C5:
    result = SepBuildCapeSecurityDescriptor(v_stack_m88, *(uint64_t *)(v_stack_mE0 + 0x20), v_stack_mB8, 0);
    Arg3 = 0;
    v_stack_m104 = (uint32_t)(result);
    if (sign_flag) goto loc_003A74D8;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mE0 + 0x30))))) == 0) goto loc_003A7403;
    result = (uint32_t)((uint32_t)(local_rsi));
    if (!(condition_is_below)) {
        result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) | (Arg6));
    }
    goto loc_003A7409;
loc_003A7403:
loc_003A7409:
    v_stack_m128 = 0;
    v_stack_m130 = v_stack_m117;
    v_stack_m138 = v_stack_mF8;
    v_stack_m140 = v_stack_m60;
    v_stack_m148 = (uint8_t)(v_stack_m115);
    v_stack_m150 = 0;
    v_stack_m158 = v_stack_mC8;
    v_stack_m160 = 0;
    v_stack_m168 = v_stack_mD8;
    v_stack_m170 = Arg9;
    Arg2 = 0;
    v_stack_m178 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m180 = v_stack_mB0;
    v_stack_m188 = 0;
    v_stack_m190 = 0;
    v_stack_m198 = (uint32_t)(result);
    result = SepAccessCheck(v_stack_m88, Arg2, *(uint64_t *)(arg3 + 0x10), *(uint64_t *)(arg3));
    local_r11 = 0;
    v_stack_m10D = (uint8_t)(result);
    if (v_stack_m116 != 0) goto loc_003A749D;
    goto loc_003A74A3;
loc_003A749D:
    result = (uint32_t)(((uint32_t)(v_stack_m114)) & (v_stack_mD8));
loc_003A74A3:
    v_stack_m114 = (uint32_t)(result);
    if ((uint32_t)(result) == 0) goto loc_003A7505;
    v_stack_mC4 = (uint32_t)((uint32_t)(v_stack_mC8));
    v_stack_m116 = 1;
    if (sign_flag) goto loc_003A750A;
    goto loc_003A74BD;
loc_003A74BA:
loc_003A74BD:
    Arg3 = (uint32_t)(((uint32_t)(v_stack_mC0)) + (1));
    v_stack_mC0 = (uint32_t)(Arg3);
    if (((uint32_t)(Arg3)) < (*(uint32_t *)(v_stack_mE8 + 0x3C))) goto loc_003A723D;
    goto loc_003A750A;
loc_003A74D8:
    result = (uint32_t)(v_stack_mC4);
    if (Arg4 == 0) {
        Arg1 = Arg3;
        result = SeUnlockSubjectContext(Arg1, Arg2, Arg3, *(uint64_t *)(arg3));
    }
    result = SepRmDereferenceCap(v_stack_mE8, Arg2, Arg3, *(uint64_t *)(arg3));
    *(uint32_t *)(arg11) = (uint32_t)((uint32_t)(v_stack_m104));
    result = SepFreeResourceInfo(v_stack_mF8, Arg2, Arg3, *(uint64_t *)(arg3));
    goto loc_003A7774;
loc_003A7505:
loc_003A750A:
loc_003A750D:
    *(uint32_t *)(arg11) = (uint32_t)((uint32_t)(0xC0000022ULL));
    if ((*(uint32_t *)(arg11)) < 0) {
        v_stack_m117 = 0;
    }
    if (v_stack_m110 != 0) goto loc_003A7576;
    if (v_stack_m110 >= 0) goto loc_003A7576;
    if (v_stack_m108 == 0) goto loc_003A7552;
    if (v_stack_m4A != 0) goto loc_003A75CA;
    if (v_stack_m4B != 0) goto loc_003A75CA;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0xC8))) & ((uint32_t)((uint32_t)(0x3000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x3000000ULL)))) goto loc_003A75CA;
loc_003A7552:
    v_stack_m190 = 0;
    v_stack_m198 = v_stack_m117;
    result = SepConstrainByMandatory(v_stack_m98, (uint32_t)((uint32_t)(local_rsi)), Arg10, Arg11);
    local_r11 = 0;
    goto loc_003A75CA;
loc_003A7576:
    if (v_stack_m108 == 0) goto loc_003A75C4;
    if (v_stack_m4A != 0) goto loc_003A75C4;
    if (v_stack_m4B != 0) goto loc_003A75C4;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0xC8))) & ((uint32_t)((uint32_t)(0x3000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x3000000ULL)))) goto loc_003A75B6;
    if (v_stack_m54 != 0) goto loc_003A75B6;
    *(uint32_t *)(arg11) = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) | (Arg6));
    *(uint32_t *)(arg10) = (uint32_t)(result);
    v_stack_m49 = 1;
    v_stack_m117 = 1;
    goto loc_003A75C4;
loc_003A75B6:
    *(uint32_t *)(arg11) = 0xC0000022ULL;
    *(uint32_t *)(arg10) = 0;
    v_stack_m117 = 0;
loc_003A75C4:
    if (condition_is_above_or_equal) goto loc_003A762B;
loc_003A75CA:
    v_stack_m188 = v_stack_m10F;
    v_stack_m190 = 0;
    v_stack_m198 = v_stack_m117;
    result = SepConstrainByConstraintMask((uint32_t)(v_stack_mD4), (uint32_t)((uint32_t)(local_rsi)), Arg10, Arg11);
    v_stack_m188 = v_stack_m10E;
    v_stack_m198 = v_stack_m117;
    result = SepConstrainByConstraintMask((uint32_t)(v_stack_mA8), (uint32_t)((uint32_t)(local_rsi)), Arg10, Arg11);
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline((uint32_t)(v_stack_mA8), (uint32_t)((uint32_t)(local_rsi)), Arg10, Arg11);
    local_r11 = 0;
    if ((uint32_t)(result) != 0) {
        result = v_stack_mD0;
        result = (uint32_t)(~(result));
    }
    if (local_rdi == 0) goto loc_003A76D8;
    if (v_stack_m10F != 0) goto loc_003A765D;
    if (v_stack_m10E != 0) goto loc_003A765D;
    if (v_stack_m54 != 0) goto loc_003A76AA;
    if (((*(uint32_t *)(local_rdi + 0xC8)) & (0x4000ULL)) == 0) goto loc_003A76AA;
    if ((*(uint32_t *)(arg11)) < 0) goto loc_003A765D;
    if (v_stack_m49 == 0) goto loc_003A76AA;
loc_003A765D:
    local_rbx = Arg10;
    if (v_stack_mCC == 0) {
        local_rdi = *(uint32_t *)(arg11);
        local_rbx = (uint32_t)(local_rsi);
        local_rbx = (uint32_t)((local_rbx) | (Arg6));
        Arg1 = Arg3;
        local_rdi = (uint32_t)((local_rdi) >> (31));
        local_rdi = (uint8_t)((local_rdi) ^ (1));
        result = SepLocateTokenTrustLevel(Arg1, (uint32_t)((uint32_t)(local_rsi)), Arg10, Arg11);
        v_stack_m180 = 0;
        Arg4 = result;
        result = v_stack_m100;
        Arg3 = 0;
        v_stack_m188 = (uint8_t)(local_rdi);
        Arg2 = 0;
        local_rdi = v_stack_mA0;
        Arg1 = local_rdi;
        v_stack_m190 = (uint32_t)(local_rbx);
        v_stack_m198 = result;
        result = SeLogAccessFailure(Arg1, Arg2, Arg3, Arg4);
        local_r11 = 0;
    }
    if ((*(uint32_t *)(arg11)) >= 0) goto loc_003A76D8;
    if (v_stack_m54 != 0) goto loc_003A76D8;
    if (((*(uint32_t *)(local_rdi + 0xC8)) & (0x4000ULL)) == 0) goto loc_003A76D8;
    result = SepLpacCausedAccessFailure(v_stack_m60, (uint32_t)((uint32_t)(local_rsi)), Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = SepLogLpacAccessFailure(v_stack_m60, (uint32_t)((uint32_t)(local_rsi)), Arg3, Arg4);
        local_r11 = 0;
    }
    if (v_stack_m118 != 0) {
        Arg1 = v_stack_mE8;
        result = SepRmDereferenceCap(Arg1, (uint32_t)((uint32_t)(local_rsi)), Arg3, Arg4);
    }
    if (Arg4 == 0) {
        Arg1 = 0;
        result = SeUnlockSubjectContext(Arg1, (uint32_t)((uint32_t)(local_rsi)), Arg3, Arg4);
    }
    result = SepFreeResourceInfo(v_stack_mF8, (uint32_t)((uint32_t)(local_rsi)), Arg3, Arg4);
    if (v_stack_m10D == 0) goto loc_003A770D;
    if (v_stack_m117 != 0) goto loc_003A714C;
loc_003A770D:
    local_r12 = 0;
    goto loc_003A714C;
loc_003A7715:
    *(uint32_t *)(arg11) = 0xC0000022ULL;
    local_r15 = 0;
    if (v_stack_mCC != 0) goto loc_003A7762;
    local_rbx = *(uint64_t *)(arg3);
    if (*(uint64_t *)(arg3) == 0) {
        local_rbx = *(uint64_t *)(arg3 + 0x10);
    }
    local_rsi = (uint32_t)((local_rsi) | (Arg6));
    result = SepLocateTokenTrustLevel(0, (uint32_t)((uint32_t)(local_rsi)), Arg3, Arg4);
    v_stack_m180 = 0;
    v_stack_m188 = 0;
    Arg2 = 0;
    v_stack_m190 = (uint32_t)(local_rsi);
    v_stack_m198 = local_rdi;
loc_003A775A:
    Arg3 = 0;
    result = SeLogAccessFailure(local_rbx, Arg2, Arg3, result);
loc_003A7762:
    if (Arg4 != 0) goto loc_003A7774;
    result = SeUnlockSubjectContext(0, Arg2, Arg3, result);
    goto loc_003A7774;
loc_003A7771:
    *(uint32_t *)(local_r15) = (uint32_t)(result);
loc_003A7774:
    result = 0;
loc_003A7776:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, result);
    local_rsp = (local_rsp) + (384);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x8` | `32` | `R` |
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg8` | `+ 0xC` | `32` | `R` |
| `Arg10` | `+ 0x0` | `32` | `R` |
| `Arg10` | `+ 0x0` | `32` | `R/W` |
| `Arg10` | `+ 0x0` | `32` | `W` |
| `Arg11` | `+ 0x0` | `32` | `R` |
| `Arg11` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003A6C30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
