# SepCommonAccessCheckEx

- RVA: `0x0047602C`–`0x0047735B` (길이 `4,911` bytes)
- VA: `0x000000014047602C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000ACC3C`
- 디코드: `1,308`개 명령, `4,911/4,911` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **69**; 고유 호출 대상: **32**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x004760D3` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004760E4` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004760F5` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004761D8` → [AuthzBasepSetAccessReasons](../42/AuthzBasepSetAccessReasons_function_0042F980.md) (function, `0x0042F980`)
- `0x004762B2` → [SeLockSubjectContext](../../page/8C/SeLockSubjectContext_function_008C64C0.md) (function, `0x008C64C0`)
- `0x004762D8` → [SepTrustLevelCheck](../3E/SepTrustLevelCheck_function_003ED7E0.md) (function, `0x003ED7E0`)
- `0x00476342` → [SepLocateTokenTrustLevel](../3E/SepLocateTokenTrustLevel_function_003EDA40.md) (function, `0x003EDA40`)
- `0x0047636C` → [SeLogAccessFailure](../44/SeLogAccessFailure_function_00448550.md) (function, `0x00448550`)
- `0x0047637A` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x00476397` → [AuthzBasepSetAccessReasons](../42/AuthzBasepSetAccessReasons_function_0042F980.md) (function, `0x0042F980`)
- `0x004763D2` → [SepFilterCheck](../30/SepFilterCheck_function_00301B60.md) (function, `0x00301B60`)
- `0x00476441` → [SeLogAccessFailure](../44/SeLogAccessFailure_function_00448550.md) (function, `0x00448550`)
- `0x00476451` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x004764F6` → [SepMandatoryIntegrityCheck](../25/SepMandatoryIntegrityCheck_function_0025F4E0.md) (function, `0x0025F4E0`)
- `0x0047651A` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x0047652C` → [SepMandatoryToDiscretionary](../41/SepMandatoryToDiscretionary_function_0041BF40.md) (function, `0x0041BF40`)
- `0x00476561` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x004765A9` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x004765DA` → [SepMandatoryAccessCheck](../60/SepMandatoryAccessCheck_function_00608480.md) (function, `0x00608480`)
- `0x004765FB` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x00476669` → [SepGetScopedPolicySid](../3A/SepGetScopedPolicySid_function_003A59AC.md) (function, `0x003A59AC`)
- `0x0047667D` → [SepRmReferenceFindCap](../3A/SepRmReferenceFindCap_function_003A58EC.md) (function, `0x003A58EC`)
- `0x004766C8` → [SepTokenIsOwner](../3E/SepTokenIsOwner_function_003E5D60.md) (function, `0x003E5D60`)
- `0x00476727` → [RtlpOwnerAcesPresent](../3F/RtlpOwnerAcesPresent_function_003FB2F0.md) (function, `0x003FB2F0`)
- `0x00476775` → [AuthzBasepSetAccessReasons](../42/AuthzBasepSetAccessReasons_function_0042F980.md) (function, `0x0042F980`)
- `0x00476798` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x004767D1` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x004768C7` → [SepAccessCheckEx](../3C/SepAccessCheckEx_function_003CF7B0.md) (function, `0x003CF7B0`)
- `0x0047699C` → [SepAdtAuditThisEventWithContext](../../page/87/SepAdtAuditThisEventWithContext_function_00870AC0.md) (function, `0x00870AC0`)
- `0x004769C0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004769D7` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x004769DF` → [SepRmDereferenceCap](../4B/SepRmDereferenceCap_function_004B1E9C.md) (function, `0x004B1E9C`)
- `0x004769F9` → [SepFreeResourceInfo](../30/SepFreeResourceInfo_function_003019F0.md) (function, `0x003019F0`)
- `0x00476A10` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00476A6B` → [AuthzBasepInitializeResourceClaimsFromSacl](../30/AuthzBasepInitializeResourceClaimsFromSacl_function_00302E84.md) (function, `0x00302E84`)
- `0x00476AFD` → [AuthzBasepEvaluateAceCondition](../2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (function, `0x002FEBD0`)
- `0x00476BA1` → [AuthzBasepEvaluateAceCondition](../2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (function, `0x002FEBD0`)
- `0x00476BD6` → [SepBuildCapeSecurityDescriptor](../4D/SepBuildCapeSecurityDescriptor_function_004D9E38.md) (function, `0x004D9E38`)
- `0x00476CC5` → [SepAccessCheckEx](../3C/SepAccessCheckEx_function_003CF7B0.md) (function, `0x003CF7B0`)
- `0x00476D37` → [AuthzBasepSetAccessReasons](../42/AuthzBasepSetAccessReasons_function_0042F980.md) (function, `0x0042F980`)
- `0x00476D6D` → [SepBuildCapeSecurityDescriptor](../4D/SepBuildCapeSecurityDescriptor_function_004D9E38.md) (function, `0x004D9E38`)
- `0x00476E59` → [SepAccessCheckEx](../3C/SepAccessCheckEx_function_003CF7B0.md) (function, `0x003CF7B0`)
- `0x00476F0C` → [AuthzBasepSetAccessReasons](../42/AuthzBasepSetAccessReasons_function_0042F980.md) (function, `0x0042F980`)
- `0x00476F3B` → [AuthzBasepSetAccessReasons](../42/AuthzBasepSetAccessReasons_function_0042F980.md) (function, `0x0042F980`)
- `0x00476F5A` → [AuthzBasepMergeAccessReasons](../69/AuthzBasepMergeAccessReasons_function_0069D67C.md) (function, `0x0069D67C`)
- `0x00476F8C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00476FBD` → [AuthzBasepMergeAccessReasons](../69/AuthzBasepMergeAccessReasons_function_0069D67C.md) (function, `0x0069D67C`)
- `0x00476FD3` → [AuthzBasepMergeAccessReasons](../69/AuthzBasepMergeAccessReasons_function_0069D67C.md) (function, `0x0069D67C`)
- `0x00477041` → [SepConstrainByMandatory](../43/SepConstrainByMandatory_function_0043FC70.md) (function, `0x0043FC70`)
- `0x0047708A` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x00477092` → [SepRmDereferenceCap](../4B/SepRmDereferenceCap_function_004B1E9C.md) (function, `0x004B1E9C`)
- `0x004770B3` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x004770BC` → [SepRmDereferenceCap](../4B/SepRmDereferenceCap_function_004B1E9C.md) (function, `0x004B1E9C`)
- `0x004770D3` → [SepFreeResourceInfo](../30/SepFreeResourceInfo_function_003019F0.md) (function, `0x003019F0`)
- `0x004770E6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00477170` → [AuthzBasepSetAccessReasons](../42/AuthzBasepSetAccessReasons_function_0042F980.md) (function, `0x0042F980`)
- `0x004771A7` → [SepConstrainByConstraintMask](../43/SepConstrainByConstraintMask_function_0043FDE0.md) (function, `0x0043FDE0`)
- `0x004771C7` → [AuthzBasepSetAccessReasons](../42/AuthzBasepSetAccessReasons_function_0042F980.md) (function, `0x0042F980`)
- `0x004771F4` → [SepConstrainByConstraintMask](../43/SepConstrainByConstraintMask_function_0043FDE0.md) (function, `0x0043FDE0`)
- `0x00477214` → [AuthzBasepSetAccessReasons](../42/AuthzBasepSetAccessReasons_function_0042F980.md) (function, `0x0042F980`)
- `0x00477219` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x00477284` → [SepLocateTokenTrustLevel](../3E/SepLocateTokenTrustLevel_function_003EDA40.md) (function, `0x003EDA40`)
- `0x004772AF` → [SeLogAccessFailure](../44/SeLogAccessFailure_function_00448550.md) (function, `0x00448550`)
- `0x004772DC` → [SepLpacCausedAccessFailure](../46/SepLpacCausedAccessFailure_function_00462484.md) (function, `0x00462484`)
- `0x004772E5` → [SepLogLpacAccessFailure](../41/SepLogLpacAccessFailure_function_0041E8A0.md) (function, `0x0041E8A0`)
- `0x004772F4` → [SepRmDereferenceCap](../4B/SepRmDereferenceCap_function_004B1E9C.md) (function, `0x004B1E9C`)
- `0x00477302` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x0047730B` → [SepFreeResourceInfo](../30/SepFreeResourceInfo_function_003019F0.md) (function, `0x003019F0`)
- `0x0047733A` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [SeSrpAccessCheck](SeSrpAccessCheck_function_00475FD0.md) at `0x00475FEB`
- [SeAccessCheckEx](SeAccessCheckEx_function_00476000.md) at `0x0047601B`

### Static image references
- `0x0047604B` → RVA `0x00E0A740` (`.data`; read)
- `0x00476494` → RVA `0x00E0CCB0` (`.data`; read)
- `0x0047661C` → RVA `0x00F04AC5` (`.data`; read)
- `0x00476691` → RVA `0x00FD80F0` (`PAGEDATA`; read)
- `0x00476936` → RVA `0x00FD9B00` (`PAGEDATA`; read)
- `0x0047693E` → RVA `0x00FD9B04` (`PAGEDATA`; read)
- `0x0047694F` → RVA `0x00FD9B38` (`PAGEDATA`; read)
- `0x00476957` → RVA `0x00FD9B3C` (`PAGEDATA`; read)
- `0x00476961` → RVA `0x00FD9B28` (`PAGEDATA`; read)
- `0x00476969` → RVA `0x00FD9B2C` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **15**
  - `0x004762B2` → [SeLockSubjectContext](../../page/8C/SeLockSubjectContext_function_008C64C0.md) (`.text` → `PAGE`)
  - `0x0047637A` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (`.text` → `PAGE`)
  - `0x00476451` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (`.text` → `PAGE`)
  - `0x0047651A` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (`.text` → `PAGE`)
  - `0x00476561` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (`.text` → `PAGE`)
  - `0x004765FB` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (`.text` → `PAGE`)
  - `0x004767D1` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (`.text` → `PAGE`)
  - `0x0047699C` → [SepAdtAuditThisEventWithContext](../../page/87/SepAdtAuditThisEventWithContext_function_00870AC0.md) (`.text` → `PAGE`)
  - `0x004769C0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x004769D7` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (`.text` → `PAGE`)
  - `0x00476F8C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x0047708A` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (`.text` → `PAGE`)
  - `0x004770B3` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (`.text` → `PAGE`)
  - `0x004770E6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00477302` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0047602C  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00476031  55                              push rbp
00476032  56                              push rsi
00476033  57                              push rdi
00476034  41 54                           push r12
00476036  41 55                           push r13
00476038  41 56                           push r14
0047603A  41 57                           push r15
0047603C  48 8D AC 24 A0 FD FF FF         lea rbp, [rsp - 0x260]
00476044  48 81 EC 90 03 00 00            sub rsp, 0x390
0047604B  48 8B 05 EE 46 99 00            mov rax, qword ptr [rip + 0x9946ee]
00476052  48 33 C4                        xor rax, rsp
00476055  48 89 85 50 02 00 00            mov qword ptr [rbp + 0x250], rax
0047605C  0F 57 C0                        xorps xmm0, xmm0
0047605F  48 89 4D 20                     mov qword ptr [rbp + 0x20], rcx
00476063  0F 57 C9                        xorps xmm1, xmm1
00476066  4C 89 45 18                     mov qword ptr [rbp + 0x18], r8
0047606A  4C 8B E1                        mov r12, rcx
0047606D  88 55 80                        mov byte ptr [rbp - 0x80], dl
00476070  33 C9                           xor ecx, ecx
00476072  33 C0                           xor eax, eax
00476074  88 4D 83                        mov byte ptr [rbp - 0x7d], cl
00476077  4D 8B F8                        mov r15, r8
0047607A  88 4D 89                        mov byte ptr [rbp - 0x77], cl
0047607D  8A DA                           mov bl, dl
0047607F  48 89 8D 8C 00 00 00            mov qword ptr [rbp + 0x8c], rcx
00476086  BF 80 00 00 00                  mov edi, 0x80
0047608B  48 89 4D D8                     mov qword ptr [rbp - 0x28], rcx
0047608F  44 8B C7                        mov r8d, edi
00476092  89 4D C8                        mov dword ptr [rbp - 0x38], ecx
00476095  33 D2                           xor edx, edx
00476097  89 4D F8                        mov dword ptr [rbp - 8], ecx
0047609A  4D 8B F1                        mov r14, r9
0047609D  48 89 4D B0                     mov qword ptr [rbp - 0x50], rcx
004760A1  88 4D 81                        mov byte ptr [rbp - 0x7f], cl
004760A4  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
004760A8  89 4D B8                        mov dword ptr [rbp - 0x48], ecx
004760AB  48 8D 8D D0 00 00 00            lea rcx, [rbp + 0xd0]
004760B2  0F 11 45 08                     movups xmmword ptr [rbp + 8], xmm0
004760B6  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
004760BA  F3 0F 7F 4D 7C                  movdqu xmmword ptr [rbp + 0x7c], xmm1
004760BF  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
004760C3  0F 11 45 28                     movups xmmword ptr [rbp + 0x28], xmm0
004760C7  0F 11 45 38                     movups xmmword ptr [rbp + 0x38], xmm0
004760CB  0F 11 4D 50                     movups xmmword ptr [rbp + 0x50], xmm1
004760CF  0F 11 4D 60                     movups xmmword ptr [rbp + 0x60], xmm1
004760D3  E8 68 0B 25 00                  call 0x1406c6c40
004760D8  44 8B C7                        mov r8d, edi
004760DB  48 8D 8D 50 01 00 00            lea rcx, [rbp + 0x150]
004760E2  33 D2                           xor edx, edx
004760E4  E8 57 0B 25 00                  call 0x1406c6c40
004760E9  44 8B C7                        mov r8d, edi
004760EC  48 8D 8D D0 01 00 00            lea rcx, [rbp + 0x1d0]
004760F3  33 D2                           xor edx, edx
004760F5  E8 46 0B 25 00                  call 0x1406c6c40
004760FA  33 FF                           xor edi, edi
004760FC  83 C8 FF                        or eax, 0xffffffff
004760FF  40 88 7D 86                     mov byte ptr [rbp - 0x7a], dil
00476103  40 88 7D 87                     mov byte ptr [rbp - 0x79], dil
00476107  89 7D CC                        mov dword ptr [rbp - 0x34], edi
0047610A  89 45 D0                        mov dword ptr [rbp - 0x30], eax
0047610D  89 45 00                        mov dword ptr [rbp], eax
00476110  4D 85 F6                        test r14, r14
00476113  0F 84 15 12 00 00               je 0x14047732e
00476119  41 83 3E 28                     cmp dword ptr [r14], 0x28
0047611D  0F 85 0B 12 00 00               jne 0x14047732e
00476123  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
00476127  48 85 C9                        test rcx, rcx
0047612A  0F 84 FE 11 00 00               je 0x14047732e
00476130  4D 85 E4                        test r12, r12
00476133  0F 84 EF 11 00 00               je 0x140477328
00476139  4D 85 FF                        test r15, r15
0047613C  0F 84 E6 11 00 00               je 0x140477328
00476142  41 83 3F 38                     cmp dword ptr [r15], 0x38
00476146  0F 85 DC 11 00 00               jne 0x140477328
0047614C  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00476150  48 85 D2                        test rdx, rdx
00476153  0F 84 CF 11 00 00               je 0x140477328
00476159  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
0047615D  48 85 C0                        test rax, rax
00476160  74 16                           je 0x140476178
00476162  83 38 10                        cmp dword ptr [rax], 0x10
00476165  0F 85 BD 11 00 00               jne 0x140477328
0047616B  F7 40 04 F8 FF FF FF            test dword ptr [rax + 4], 0xfffffff8
00476172  0F 85 B0 11 00 00               jne 0x140477328
00476178  48 8B 85 C0 02 00 00            mov rax, qword ptr [rbp + 0x2c0]
0047617F  48 85 C0                        test rax, rax
00476182  74 09                           je 0x14047618d
00476184  83 38 60                        cmp dword ptr [rax], 0x60
00476187  0F 85 9B 11 00 00               jne 0x140477328
0047618D  89 3A                           mov dword ptr [rdx], edi
0047618F  B9 22 00 00 C0                  mov ecx, 0xc0000022
00476194  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00476198  89 08                           mov dword ptr [rax], ecx
0047619A  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
0047619E  89 7D A0                        mov dword ptr [rbp - 0x60], edi
004761A1  89 4D E8                        mov dword ptr [rbp - 0x18], ecx
004761A4  48 85 C0                        test rax, rax
004761A7  74 03                           je 0x1404761ac
004761A9  48 89 38                        mov qword ptr [rax], rdi
004761AC  41 8B 77 14                     mov esi, dword ptr [r15 + 0x14]
004761B0  41 BB FF FF FF FD               mov r11d, 0xfdffffff
004761B6  4D 8B 4E 18                     mov r9, qword ptr [r14 + 0x18]
004761BA  F7 D6                           not esi
004761BC  41 23 77 10                     and esi, dword ptr [r15 + 0x10]
004761C0  41 BD 01 00 00 00               mov r13d, 1
004761C6  41 23 F3                        and esi, r11d
004761C9  44 88 6C 24 20                  mov byte ptr [rsp + 0x20], r13b
004761CE  8B CE                           mov ecx, esi
004761D0  89 75 BC                        mov dword ptr [rbp - 0x44], esi
004761D3  45 33 C0                        xor r8d, r8d
004761D6  33 D2                           xor edx, edx
004761D8  E8 A3 97 FB FF                  call 0x14042f980
004761DD  40 38 BD C8 02 00 00            cmp byte ptr [rbp + 0x2c8], dil
004761E4  75 44                           jne 0x14047622a
004761E6  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
004761EA  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
004761EE  0F BA E0 19                     bt eax, 0x19
004761F2  73 22                           jae 0x140476216
004761F4  49 8B 47 20                     mov rax, qword ptr [r15 + 0x20]
004761F8  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
004761FB  89 01                           mov dword ptr [rcx], eax
004761FD  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
00476201  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
00476205  41 23 C3                        and eax, r11d
00476208  09 01                           or dword ptr [rcx], eax
0047620A  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
0047620E  41 8B 47 14                     mov eax, dword ptr [r15 + 0x14]
00476212  09 01                           or dword ptr [rcx], eax
00476214  EB 06                           jmp 0x14047621c
00476216  41 0B 47 14                     or eax, dword ptr [r15 + 0x14]
0047621A  89 01                           mov dword ptr [rcx], eax
0047621C  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
00476220  89 39                           mov dword ptr [rcx], edi
00476222  41 8A C5                        mov al, r13b
00476225  E9 06 11 00 00                  jmp 0x140477330
0047622A  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
0047622E  48 85 C0                        test rax, rax
00476231  74 31                           je 0x140476264
00476233  48 39 78 08                     cmp qword ptr [rax + 8], rdi
00476237  74 2B                           je 0x140476264
00476239  49 39 3C 24                     cmp qword ptr [r12], rdi
0047623D  74 17                           je 0x140476256
0047623F  41 83 7C 24 08 02               cmp dword ptr [r12 + 8], 2
00476245  7D 0F                           jge 0x140476256
00476247  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0047624B  C7 00 A5 00 00 C0               mov dword ptr [rax], 0xc00000a5
00476251  E9 D8 10 00 00                  jmp 0x14047732e
00476256  41 39 7F 10                     cmp dword ptr [r15 + 0x10], edi
0047625A  75 31                           jne 0x14047628d
0047625C  41 8B 4F 14                     mov ecx, dword ptr [r15 + 0x14]
00476260  85 C9                           test ecx, ecx
00476262  75 0F                           jne 0x140476273
00476264  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00476268  C7 00 22 00 00 C0               mov dword ptr [rax], 0xc0000022
0047626E  E9 BB 10 00 00                  jmp 0x14047732e
00476273  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00476277  89 08                           mov dword ptr [rax], ecx
00476279  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0047627D  89 38                           mov dword ptr [rax], edi
0047627F  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
00476283  48 85 C0                        test rax, rax
00476286  74 9A                           je 0x140476222
00476288  48 89 38                        mov qword ptr [rax], rdi
0047628B  EB 95                           jmp 0x140476222
0047628D  41 8B 46 04                     mov eax, dword ptr [r14 + 4]
00476291  41 3B C5                        cmp eax, r13d
00476294  74 15                           je 0x1404762ab
00476296  41 3B 47 28                     cmp eax, dword ptr [r15 + 0x28]
0047629A  74 0F                           je 0x1404762ab
0047629C  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
004762A0  C7 00 0D 00 00 C0               mov dword ptr [rax], 0xc000000d
004762A6  E9 83 10 00 00                  jmp 0x14047732e
004762AB  84 DB                           test bl, bl
004762AD  75 08                           jne 0x1404762b7
004762AF  49 8B CC                        mov rcx, r12
004762B2  E8 09 02 45 00                  call 0x1408c64c0
004762B7  49 8B 57 08                     mov rdx, qword ptr [r15 + 8]
004762BB  48 8D 45 D0                     lea rax, [rbp - 0x30]
004762BF  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
004762C4  45 33 C9                        xor r9d, r9d
004762C7  40 88 7C 24 28                  mov byte ptr [rsp + 0x28], dil
004762CC  4D 8B C4                        mov r8, r12
004762CF  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
004762D4  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
004762D8  E8 03 75 F7 FF                  call 0x1403ed7e0
004762DD  49 8B 56 10                     mov rdx, qword ptr [r14 + 0x10]
004762E1  89 02                           mov dword ptr [rdx], eax
004762E3  49 8B 56 10                     mov rdx, qword ptr [r14 + 0x10]
004762E7  39 3A                           cmp dword ptr [rdx], edi
004762E9  7D 07                           jge 0x1404762f2
004762EB  84 DB                           test bl, bl
004762ED  E9 1F 02 00 00                  jmp 0x140476511
004762F2  41 8B 4F 10                     mov ecx, dword ptr [r15 + 0x10]
004762F6  41 BA 22 00 00 C0               mov r10d, 0xc0000022
004762FC  8B 5D D0                        mov ebx, dword ptr [rbp - 0x30]
004762FF  0F BA F1 19                     btr ecx, 0x19
00476303  8B C1                           mov eax, ecx
00476305  23 C3                           and eax, ebx
00476307  2B C1                           sub eax, ecx
00476309  F7 D8                           neg eax
0047630B  1B C0                           sbb eax, eax
0047630D  45 33 C9                        xor r9d, r9d
00476310  41 23 C2                        and eax, r10d
00476313  89 02                           mov dword ptr [rdx], eax
00476315  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00476319  49 8B 3C 24                     mov rdi, qword ptr [r12]
0047631D  48 89 7D F0                     mov qword ptr [rbp - 0x10], rdi
00476321  44 39 08                        cmp dword ptr [rax], r9d
00476324  7D 7B                           jge 0x1404763a1
00476326  4C 8B EF                        mov r13, rdi
00476329  48 85 FF                        test rdi, rdi
0047632C  75 05                           jne 0x140476333
0047632E  4D 8B 6C 24 10                  mov r13, qword ptr [r12 + 0x10]
00476333  41 8B 77 14                     mov esi, dword ptr [r15 + 0x14]
00476337  49 8B CC                        mov rcx, r12
0047633A  41 0B 77 10                     or esi, dword ptr [r15 + 0x10]
0047633E  49 8B 7F 08                     mov rdi, qword ptr [r15 + 8]
00476342  E8 F9 76 F7 FF                  call 0x1403eda40
00476347  45 33 FF                        xor r15d, r15d
0047634A  4C 8B C8                        mov r9, rax
0047634D  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00476351  45 33 C0                        xor r8d, r8d
00476354  44 88 7C 24 38                  mov byte ptr [rsp + 0x38], r15b
00476359  33 D2                           xor edx, edx
0047635B  44 88 7C 24 30                  mov byte ptr [rsp + 0x30], r15b
00476360  49 8B CD                        mov rcx, r13
00476363  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
00476367  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0047636C  E8 DF 21 FD FF                  call 0x140448550
00476371  44 38 7D 80                     cmp byte ptr [rbp - 0x80], r15b
00476375  75 08                           jne 0x14047637f
00476377  49 8B CC                        mov rcx, r12
0047637A  E8 A1 01 45 00                  call 0x1408c6520
0047637F  F7 D3                           not ebx
00476381  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
00476386  23 5D BC                        and ebx, dword ptr [rbp - 0x44]
00476389  BA 00 00 90 00                  mov edx, 0x900000
0047638E  8B CB                           mov ecx, ebx
00476390  4D 8B 4E 18                     mov r9, qword ptr [r14 + 0x18]
00476394  45 33 C0                        xor r8d, r8d
00476397  E8 E4 95 FB FF                  call 0x14042f980
0047639C  E9 8D 0F 00 00                  jmp 0x14047732e
004763A1  48 85 FF                        test rdi, rdi
004763A4  75 09                           jne 0x1404763af
004763A6  49 8B 7C 24 10                  mov rdi, qword ptr [r12 + 0x10]
004763AB  48 89 7D F0                     mov qword ptr [rbp - 0x10], rdi
004763AF  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
004763B3  8B 41 04                        mov eax, dword ptr [rcx + 4]
004763B6  A8 04                           test al, 4
004763B8  0F 85 A9 00 00 00               jne 0x140476467
004763BE  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
004763C2  48 8D 45 00                     lea rax, [rbp]
004763C6  4C 8B C7                        mov r8, rdi
004763C9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004763CE  48 8D 55 90                     lea rdx, [rbp - 0x70]
004763D2  E8 89 B7 E8 FF                  call 0x140301b60
004763D7  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
004763DB  45 33 C9                        xor r9d, r9d
004763DE  89 01                           mov dword ptr [rcx], eax
004763E0  49 8B 56 10                     mov rdx, qword ptr [r14 + 0x10]
004763E4  44 39 0A                        cmp dword ptr [rdx], r9d
004763E7  0F 8C DE 00 00 00               jl 0x1404764cb
004763ED  41 8B 4F 10                     mov ecx, dword ptr [r15 + 0x10]
004763F1  41 BA 22 00 00 C0               mov r10d, 0xc0000022
004763F7  8B 5D 00                        mov ebx, dword ptr [rbp]
004763FA  0F BA F1 19                     btr ecx, 0x19
004763FE  8B C1                           mov eax, ecx
00476400  23 C3                           and eax, ebx
00476402  2B C1                           sub eax, ecx
00476404  F7 D8                           neg eax
00476406  1B C0                           sbb eax, eax
00476408  41 23 C2                        and eax, r10d
0047640B  89 02                           mov dword ptr [rdx], eax
0047640D  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00476411  44 39 08                        cmp dword ptr [rax], r9d
00476414  7D 51                           jge 0x140476467
00476416  41 8B 57 14                     mov edx, dword ptr [r15 + 0x14]
0047641A  45 33 C0                        xor r8d, r8d
0047641D  41 0B 57 10                     or edx, dword ptr [r15 + 0x10]
00476421  48 8B CF                        mov rcx, rdi
00476424  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
00476428  44 88 4C 24 38                  mov byte ptr [rsp + 0x38], r9b
0047642D  44 88 4C 24 30                  mov byte ptr [rsp + 0x30], r9b
00476432  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
00476436  33 D2                           xor edx, edx
00476438  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0047643C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00476441  E8 0A 21 FD FF                  call 0x140448550
00476446  33 FF                           xor edi, edi
00476448  40 38 7D 80                     cmp byte ptr [rbp - 0x80], dil
0047644C  75 08                           jne 0x140476456
0047644E  49 8B CC                        mov rcx, r12
00476451  E8 CA 00 45 00                  call 0x1408c6520
00476456  23 DE                           and ebx, esi
00476458  40 88 7C 24 20                  mov byte ptr [rsp + 0x20], dil
0047645D  BA 00 00 A0 00                  mov edx, 0xa00000
00476462  E9 27 FF FF FF                  jmp 0x14047638e
00476467  49 8B 57 08                     mov rdx, qword ptr [r15 + 8]
0047646B  8B 42 04                        mov eax, dword ptr [rdx + 4]
0047646E  8A D8                           mov bl, al
00476470  41 22 DD                        and bl, r13b
00476473  88 5D 84                        mov byte ptr [rbp - 0x7c], bl
00476476  A8 02                           test al, 2
00476478  74 14                           je 0x14047648e
0047647A  F7 87 C8 00 00 00 00 20 00 00   test dword ptr [rdi + 0xc8], 0x2000
00476484  45 8A C5                        mov r8b, r13b
00476487  74 08                           je 0x140476491
00476489  41 8A CD                        mov cl, r13b
0047648C  EB 06                           jmp 0x140476494
0047648E  45 8A C1                        mov r8b, r9b
00476491  41 8A C9                        mov cl, r9b
00476494  44 38 0D 15 68 99 00            cmp byte ptr [rip + 0x996815], r9b
0047649B  88 4D 85                        mov byte ptr [rbp - 0x7b], cl
0047649E  75 31                           jne 0x1404764d1
004764A0  8B 87 C8 00 00 00               mov eax, dword ptr [rdi + 0xc8]
004764A6  A8 20                           test al, 0x20
004764A8  75 27                           jne 0x1404764d1
004764AA  48 8B 87 D8 00 00 00            mov rax, qword ptr [rdi + 0xd8]
004764B1  48 85 C0                        test rax, rax
004764B4  74 1B                           je 0x1404764d1
004764B6  8B 40 28                        mov eax, dword ptr [rax + 0x28]
004764B9  A8 20                           test al, 0x20
004764BB  74 14                           je 0x1404764d1
004764BD  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
004764C1  44 89 08                        mov dword ptr [rax], r9d
004764C4  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
004764C8  44 89 10                        mov dword ptr [rax], r10d
004764CB  44 38 4D 80                     cmp byte ptr [rbp - 0x80], r9b
004764CF  EB 40                           jmp 0x140476511
004764D1  44 88 4D AC                     mov byte ptr [rbp - 0x54], r9b
004764D5  84 C9                           test cl, cl
004764D7  0F 85 CC 00 00 00               jne 0x1404765a9
004764DD  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
004764E1  48 8D 45 08                     lea rax, [rbp + 8]
004764E5  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
004764E9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004764EE  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
004764F3  4C 8B CF                        mov r9, rdi
004764F6  E8 E5 8F DE FF                  call 0x14025f4e0
004764FB  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
004764FF  45 33 D2                        xor r10d, r10d
00476502  89 01                           mov dword ptr [rcx], eax
00476504  4D 8B 4E 10                     mov r9, qword ptr [r14 + 0x10]
00476508  45 39 11                        cmp dword ptr [r9], r10d
0047650B  7D 17                           jge 0x140476524
0047650D  44 38 55 80                     cmp byte ptr [rbp - 0x80], r10b
00476511  0F 85 17 0E 00 00               jne 0x14047732e
00476517  49 8B CC                        mov rcx, r12
0047651A  E8 01 00 45 00                  call 0x1408c6520
0047651F  E9 0A 0E 00 00                  jmp 0x14047732e
00476524  41 8B 57 10                     mov edx, dword ptr [r15 + 0x10]
00476528  48 8D 4D 08                     lea rcx, [rbp + 8]
0047652C  E8 0F 5A FA FF                  call 0x14041bf40
00476531  41 89 01                        mov dword ptr [r9], eax
00476534  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00476538  44 39 10                        cmp dword ptr [rax], r10d
0047653B  7D 42                           jge 0x14047657f
0047653D  F7 87 C8 00 00 00 00 40 00 00   test dword ptr [rdi + 0xc8], 0x4000
00476547  74 0F                           je 0x140476558
00476549  81 7D 14 00 20 00 00            cmp dword ptr [rbp + 0x14], 0x2000
00476550  77 06                           ja 0x140476558
00476552  44 88 6D AC                     mov byte ptr [rbp - 0x54], r13b
00476556  EB 51                           jmp 0x1404765a9
00476558  44 38 55 80                     cmp byte ptr [rbp - 0x80], r10b
0047655C  75 0B                           jne 0x140476569
0047655E  49 8B CC                        mov rcx, r12
00476561  E8 BA FF 44 00                  call 0x1408c6520
00476566  45 33 D2                        xor r10d, r10d
00476569  8B 4D 08                        mov ecx, dword ptr [rbp + 8]
0047656C  BA 00 00 30 00                  mov edx, 0x300000
00476571  F7 D1                           not ecx
00476573  44 88 54 24 20                  mov byte ptr [rsp + 0x20], r10b
00476578  23 CE                           and ecx, esi
0047657A  E9 11 FE FF FF                  jmp 0x140476390
0047657F  41 F7 47 10 00 00 00 02         test dword ptr [r15 + 0x10], 0x2000000
00476587  74 20                           je 0x1404765a9
00476589  F7 87 C8 00 00 00 00 40 00 00   test dword ptr [rdi + 0xc8], 0x4000
00476593  74 14                           je 0x1404765a9
00476595  8B 45 AC                        mov eax, dword ptr [rbp - 0x54]
00476598  81 7D 14 00 20 00 00            cmp dword ptr [rbp + 0x14], 0x2000
0047659F  0F B6 C0                        movzx eax, al
004765A2  41 0F 46 C5                     cmovbe eax, r13d
004765A6  89 45 AC                        mov dword ptr [rbp - 0x54], eax
004765A9  E8 BA 73 15 00                  call 0x1405cd968
004765AE  45 33 C0                        xor r8d, r8d
004765B1  85 C0                           test eax, eax
004765B3  74 67                           je 0x14047661c
004765B5  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
004765B9  48 8D 45 CC                     lea rax, [rbp - 0x34]
004765BD  8A 5D 80                        mov bl, byte ptr [rbp - 0x80]
004765C0  49 8B D4                        mov rdx, r12
004765C3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004765C8  84 DB                           test bl, bl
004765CA  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
004765CE  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
004765D2  41 0F 94 C1                     sete r9b
004765D6  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
004765DA  E8 A1 1E 19 00                  call 0x140608480
004765DF  45 33 C0                        xor r8d, r8d
004765E2  85 C0                           test eax, eax
004765E4  78 0E                           js 0x1404765f4
004765E6  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
004765EA  23 45 CC                        and eax, dword ptr [rbp - 0x34]
004765ED  A9 FF FF FF FD                  test eax, 0xfdffffff
004765F2  74 25                           je 0x140476619
004765F4  84 DB                           test bl, bl
004765F6  75 0B                           jne 0x140476603
004765F8  49 8B CC                        mov rcx, r12
004765FB  E8 20 FF 44 00                  call 0x1408c6520
00476600  45 33 C0                        xor r8d, r8d
00476603  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00476607  44 89 00                        mov dword ptr [rax], r8d
0047660A  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0047660E  C7 00 C0 01 00 C0               mov dword ptr [rax], 0xc00001c0
00476614  E9 15 0D 00 00                  jmp 0x14047732e
00476619  8A 5D 84                        mov bl, byte ptr [rbp - 0x7c]
0047661C  8A 05 A3 E4 A8 00               mov al, byte ptr [rip + 0xa8e4a3]
00476622  84 C0                           test al, al
00476624  74 29                           je 0x14047664f
00476626  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
0047662A  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0047662E  0F B7 51 02                     movzx edx, word ptr [rcx + 2]
00476632  F6 C2 10                        test dl, 0x10
00476635  74 18                           je 0x14047664f
00476637  44 0F 20 C0                     mov rax, cr8
0047663B  3C 02                           cmp al, 2
0047663D  73 10                           jae 0x14047664f
0047663F  66 85 D2                        test dx, dx
00476642  79 15                           jns 0x140476659
00476644  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
00476647  85 C0                           test eax, eax
00476649  75 09                           jne 0x140476654
0047664B  4C 89 45 D8                     mov qword ptr [rbp - 0x28], r8
0047664F  8A 4D 81                        mov cl, byte ptr [rbp - 0x7f]
00476652  EB 4E                           jmp 0x1404766a2
00476654  48 03 C1                        add rax, rcx
00476657  EB 04                           jmp 0x14047665d
00476659  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
0047665D  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00476661  48 85 C0                        test rax, rax
00476664  74 E9                           je 0x14047664f
00476666  48 8B C8                        mov rcx, rax
00476669  E8 3E F3 F2 FF                  call 0x1403a59ac
0047666E  45 33 C0                        xor r8d, r8d
00476671  48 85 C0                        test rax, rax
00476674  74 29                           je 0x14047669f
00476676  48 8D 55 B0                     lea rdx, [rbp - 0x50]
0047667A  48 8B C8                        mov rcx, rax
0047667D  E8 6A F2 F2 FF                  call 0x1403a58ec
00476682  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
00476686  45 33 C0                        xor r8d, r8d
00476689  85 C0                           test eax, eax
0047668B  41 8A CD                        mov cl, r13b
0047668E  88 4D 81                        mov byte ptr [rbp - 0x7f], cl
00476691  48 0F 48 15 57 1A B6 00         cmovs rdx, qword ptr [rip + 0xb61a57]
00476699  48 89 55 B0                     mov qword ptr [rbp - 0x50], rdx
0047669D  EB 03                           jmp 0x1404766a2
0047669F  41 8A C8                        mov cl, r8b
004766A2  84 DB                           test bl, bl
004766A4  74 17                           je 0x1404766bd
004766A6  41 F7 47 10 00 00 06 02         test dword ptr [r15 + 0x10], 0x2060000
004766AE  75 0D                           jne 0x1404766bd
004766B0  84 C9                           test cl, cl
004766B2  75 09                           jne 0x1404766bd
004766B4  45 8A D8                        mov r11b, r8b
004766B7  44 88 45 82                     mov byte ptr [rbp - 0x7e], r8b
004766BB  EB 19                           jmp 0x1404766d6
004766BD  49 8B 57 08                     mov rdx, qword ptr [r15 + 8]
004766C1  48 8B CF                        mov rcx, rdi
004766C4  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
004766C8  E8 93 F6 F6 FF                  call 0x1403e5d60
004766CD  44 8A D8                        mov r11b, al
004766D0  88 45 82                        mov byte ptr [rbp - 0x7e], al
004766D3  45 33 C0                        xor r8d, r8d
004766D6  41 8B 5F 10                     mov ebx, dword ptr [r15 + 0x10]
004766DA  BA 00 00 06 00                  mov edx, 0x60000
004766DF  45 84 DB                        test r11b, r11b
004766E2  0F 84 AC 00 00 00               je 0x140476794
004766E8  F7 C3 00 00 06 02               test ebx, 0x2060000
004766EE  0F 84 A0 00 00 00               je 0x140476794
004766F4  44 38 45 84                     cmp byte ptr [rbp - 0x7c], r8b
004766F8  75 42                           jne 0x14047673c
004766FA  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
004766FE  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00476702  0F B7 41 02                     movzx eax, word ptr [rcx + 2]
00476706  A8 04                           test al, 4
00476708  75 05                           jne 0x14047670f
0047670A  49 8B D0                        mov rdx, r8
0047670D  EB 16                           jmp 0x140476725
0047670F  66 85 C0                        test ax, ax
00476712  79 0D                           jns 0x140476721
00476714  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
00476717  85 C0                           test eax, eax
00476719  74 EF                           je 0x14047670a
0047671B  48 8D 14 01                     lea rdx, [rcx + rax]
0047671F  EB 04                           jmp 0x140476725
00476721  48 8B 51 20                     mov rdx, qword ptr [rcx + 0x20]
00476725  33 C9                           xor ecx, ecx
00476727  E8 C4 4B F8 FF                  call 0x1403fb2f0
0047672C  45 33 C0                        xor r8d, r8d
0047672F  84 C0                           test al, al
00476731  75 61                           jne 0x140476794
00476733  44 8A 5D 82                     mov r11b, byte ptr [rbp - 0x7e]
00476737  BA 00 00 06 00                  mov edx, 0x60000
0047673C  41 8B 47 14                     mov eax, dword ptr [r15 + 0x14]
00476740  8B CB                           mov ecx, ebx
00476742  81 E1 00 00 00 02               and ecx, 0x2000000
00476748  74 06                           je 0x140476750
0047674A  8B DA                           mov ebx, edx
0047674C  0B C2                           or eax, edx
0047674E  EB 04                           jmp 0x140476754
00476750  23 DA                           and ebx, edx
00476752  0B C3                           or eax, ebx
00476754  41 89 47 14                     mov dword ptr [r15 + 0x14], eax
00476758  85 C9                           test ecx, ecx
0047675A  74 04                           je 0x140476760
0047675C  8B F2                           mov esi, edx
0047675E  EB 02                           jmp 0x140476762
00476760  23 F2                           and esi, edx
00476762  4D 8B 4E 18                     mov r9, qword ptr [r14 + 0x18]
00476766  BA 00 00 40 00                  mov edx, 0x400000
0047676B  44 88 44 24 20                  mov byte ptr [rsp + 0x20], r8b
00476770  8B CE                           mov ecx, esi
00476772  45 33 C0                        xor r8d, r8d
00476775  E8 06 92 FB FF                  call 0x14042f980
0047677A  41 81 67 10 FF FF F9 FF         and dword ptr [r15 + 0x10], 0xfff9ffff
00476782  8A 45 81                        mov al, byte ptr [rbp - 0x7f]
00476785  F6 D8                           neg al
00476787  1A C9                           sbb cl, cl
00476789  41 22 CB                        and cl, r11b
0047678C  40 8A F1                        mov sil, cl
0047678F  88 4D 82                        mov byte ptr [rbp - 0x7e], cl
00476792  EB 04                           jmp 0x140476798
00476794  40 8A 75 82                     mov sil, byte ptr [rbp - 0x7e]
00476798  E8 EB 8F 07 00                  call 0x1404ef788
0047679D  41 8B 4F 10                     mov ecx, dword ptr [r15 + 0x10]
004767A1  45 33 C0                        xor r8d, r8d
004767A4  85 C0                           test eax, eax
004767A6  74 4B                           je 0x1404767f3
004767A8  85 C9                           test ecx, ecx
004767AA  75 43                           jne 0x1404767ef
004767AC  44 38 45 81                     cmp byte ptr [rbp - 0x7f], r8b
004767B0  75 3D                           jne 0x1404767ef
004767B2  8B 87 C8 00 00 00               mov eax, dword ptr [rdi + 0xc8]
004767B8  25 00 60 00 00                  and eax, 0x6000
004767BD  3D 00 20 00 00                  cmp eax, 0x2000
004767C2  74 04                           je 0x1404767c8
004767C4  85 DB                           test ebx, ebx
004767C6  75 27                           jne 0x1404767ef
004767C8  44 38 45 80                     cmp byte ptr [rbp - 0x80], r8b
004767CC  75 0B                           jne 0x1404767d9
004767CE  49 8B CC                        mov rcx, r12
004767D1  E8 4A FD 44 00                  call 0x1408c6520
004767D6  45 33 C0                        xor r8d, r8d
004767D9  41 8B 47 14                     mov eax, dword ptr [r15 + 0x14]
004767DD  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
004767E1  89 01                           mov dword ptr [rcx], eax
004767E3  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
004767E7  44 89 00                        mov dword ptr [rax], r8d
004767EA  E9 33 FA FF FF                  jmp 0x140476222
004767EF  8B D1                           mov edx, ecx
004767F1  EB 1C                           jmp 0x14047680f
004767F3  8B D1                           mov edx, ecx
004767F5  85 C9                           test ecx, ecx
004767F7  75 16                           jne 0x14047680f
004767F9  44 38 45 81                     cmp byte ptr [rbp - 0x7f], r8b
004767FD  75 10                           jne 0x14047680f
004767FF  F7 87 C8 00 00 00 00 20 00 00   test dword ptr [rdi + 0xc8], 0x2000
00476809  75 BD                           jne 0x1404767c8
0047680B  85 DB                           test ebx, ebx
0047680D  74 B9                           je 0x1404767c8
0047680F  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
00476813  48 8D 45 83                     lea rax, [rbp - 0x7d]
00476817  4D 8B 0C 24                     mov r9, qword ptr [r12]
0047681B  0F 57 C0                        xorps xmm0, xmm0
0047681E  4C 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r8
00476826  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
0047682E  48 8D 45 90                     lea rax, [rbp - 0x70]
00476832  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0047683A  48 8D 45 78                     lea rax, [rbp + 0x78]
0047683E  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00476846  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
0047684A  4C 89 85 8C 00 00 00            mov qword ptr [rbp + 0x8c], r8
00476851  44 8A 85 D0 02 00 00            mov r8b, byte ptr [rbp + 0x2d0]
00476858  44 88 84 24 80 00 00 00         mov byte ptr [rsp + 0x80], r8b
00476860  4D 8B 44 24 10                  mov r8, qword ptr [r12 + 0x10]
00476865  40 88 74 24 78                  mov byte ptr [rsp + 0x78], sil
0047686A  33 F6                           xor esi, esi
0047686C  40 88 74 24 70                  mov byte ptr [rsp + 0x70], sil
00476871  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00476876  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0047687A  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0047687F  49 8B 46 20                     mov rax, qword ptr [r14 + 0x20]
00476883  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00476888  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0047688C  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00476891  8A 85 C8 02 00 00               mov al, byte ptr [rbp + 0x2c8]
00476897  88 44 24 48                     mov byte ptr [rsp + 0x48], al
0047689B  41 8B 47 14                     mov eax, dword ptr [r15 + 0x14]
0047689F  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
004768A3  49 8B 47 20                     mov rax, qword ptr [r15 + 0x20]
004768A7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
004768AC  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
004768B0  F3 0F 7F 45 7C                  movdqu xmmword ptr [rbp + 0x7c], xmm0
004768B5  89 5D 78                        mov dword ptr [rbp + 0x78], ebx
004768B8  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
004768BC  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
004768C1  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
004768C5  33 D2                           xor edx, edx
004768C7  E8 E4 8E F5 FF                  call 0x1403cf7b0
004768CC  8A 0D F3 E1 A8 00               mov cl, byte ptr [rip + 0xa8e1f3]
004768D2  88 45 88                        mov byte ptr [rbp - 0x78], al
004768D5  84 C9                           test cl, cl
004768D7  0F 84 FB 06 00 00               je 0x140476fd8
004768DD  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
004768E1  8B 01                           mov eax, dword ptr [rcx]
004768E3  89 45 BC                        mov dword ptr [rbp - 0x44], eax
004768E6  85 C0                           test eax, eax
004768E8  0F 88 EA 06 00 00               js 0x140476fd8
004768EE  40 38 75 81                     cmp byte ptr [rbp - 0x7f], sil
004768F2  0F 84 E0 06 00 00               je 0x140476fd8
004768F8  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
004768FC  8B DE                           mov ebx, esi
004768FE  40 88 75 8C                     mov byte ptr [rbp - 0x74], sil
00476902  44 8B CE                        mov r9d, esi
00476905  89 75 9C                        mov dword ptr [rbp - 0x64], esi
00476908  8B 01                           mov eax, dword ptr [rcx]
0047690A  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
0047690E  89 45 C0                        mov dword ptr [rbp - 0x40], eax
00476911  89 45 A8                        mov dword ptr [rbp - 0x58], eax
00476914  48 85 C9                        test rcx, rcx
00476917  74 6C                           je 0x140476985
00476919  48 8B 09                        mov rcx, qword ptr [rcx]
0047691C  48 85 C9                        test rcx, rcx
0047691F  74 64                           je 0x140476985
00476921  8B 01                           mov eax, dword ptr [rcx]
00476923  85 C0                           test eax, eax
00476925  74 5E                           je 0x140476985
00476927  48 83 C1 0C                     add rcx, 0xc
0047692B  44 8B C0                        mov r8d, eax
0047692E  39 71 04                        cmp dword ptr [rcx + 4], esi
00476931  7D 45                           jge 0x140476978
00476933  8B 51 FC                        mov edx, dword ptr [rcx - 4]
00476936  3B 15 C4 31 B6 00               cmp edx, dword ptr [rip + 0xb631c4]
0047693C  75 11                           jne 0x14047694f
0047693E  8B 05 C0 31 B6 00               mov eax, dword ptr [rip + 0xb631c0]
00476944  39 01                           cmp dword ptr [rcx], eax
00476946  75 07                           jne 0x14047694f
00476948  41 0F BA E9 18                  bts r9d, 0x18
0047694D  EB 29                           jmp 0x140476978
0047694F  3B 15 E3 31 B6 00               cmp edx, dword ptr [rip + 0xb631e3]
00476955  75 0A                           jne 0x140476961
00476957  8B 05 DF 31 B6 00               mov eax, dword ptr [rip + 0xb631df]
0047695D  39 01                           cmp dword ptr [rcx], eax
0047695F  74 12                           je 0x140476973
00476961  3B 15 C1 31 B6 00               cmp edx, dword ptr [rip + 0xb631c1]
00476967  75 0F                           jne 0x140476978
00476969  8B 05 BD 31 B6 00               mov eax, dword ptr [rip + 0xb631bd]
0047696F  39 01                           cmp dword ptr [rcx], eax
00476971  75 05                           jne 0x140476978
00476973  41 0F BA E9 13                  bts r9d, 0x13
00476978  48 83 C1 0C                     add rcx, 0xc
0047697C  4D 2B C5                        sub r8, r13
0047697F  75 AD                           jne 0x14047692e
00476981  44 89 4D 9C                     mov dword ptr [rbp - 0x64], r9d
00476985  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00476989  4D 8B CC                        mov r9, r12
0047698C  45 8A C5                        mov r8b, r13b
0047698F  41 8A D5                        mov dl, r13b
00476992  8B 08                           mov ecx, dword ptr [rax]
00476994  89 4D C4                        mov dword ptr [rbp - 0x3c], ecx
00476997  B9 82 00 00 00                  mov ecx, 0x82
0047699C  E8 1F A1 3F 00                  call 0x140870ac0
004769A1  48 8B 75 B0                     mov rsi, qword ptr [rbp - 0x50]
004769A5  8A D0                           mov dl, al
004769A7  88 45 84                        mov byte ptr [rbp - 0x7c], al
004769AA  84 C0                           test al, al
004769AC  74 6A                           je 0x140476a18
004769AE  8B 56 3C                        mov edx, dword ptr [rsi + 0x3c]
004769B1  B9 40 00 00 00                  mov ecx, 0x40
004769B6  48 C1 E2 03                     shl rdx, 3
004769BA  41 B8 53 65 53 41               mov r8d, 0x41536553
004769C0  E8 2B B7 70 00                  call 0x140b820f0
004769C5  48 8B D8                        mov rbx, rax
004769C8  33 C0                           xor eax, eax
004769CA  48 85 DB                        test rbx, rbx
004769CD  75 34                           jne 0x140476a03
004769CF  38 45 80                        cmp byte ptr [rbp - 0x80], al
004769D2  75 08                           jne 0x1404769dc
004769D4  49 8B CC                        mov rcx, r12
004769D7  E8 44 FB 44 00                  call 0x1408c6520
004769DC  48 8B CE                        mov rcx, rsi
004769DF  E8 B8 B4 03 00                  call 0x1404b1e9c
004769E4  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
004769E8  83 20 00                        and dword ptr [rax], 0
004769EB  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
004769EF  C7 00 17 00 00 C0               mov dword ptr [rax], 0xc0000017
004769F5  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
004769F9  E8 F2 AF E8 FF                  call 0x1403019f0
004769FE  E9 2B 09 00 00                  jmp 0x14047732e
00476A03  44 8B 46 3C                     mov r8d, dword ptr [rsi + 0x3c]
00476A07  33 D2                           xor edx, edx
00476A09  49 C1 E0 03                     shl r8, 3
00476A0D  48 8B CB                        mov rcx, rbx
00476A10  E8 2B 02 25 00                  call 0x1406c6c40
00476A15  8A 55 84                        mov dl, byte ptr [rbp - 0x7c]
00476A18  8B 4E 3C                        mov ecx, dword ptr [rsi + 0x3c]
00476A1B  45 33 D2                        xor r10d, r10d
00476A1E  41 8B C2                        mov eax, r10d
00476A21  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
00476A24  89 4D 98                        mov dword ptr [rbp - 0x68], ecx
00476A27  85 C9                           test ecx, ecx
00476A29  0F 84 6A 04 00 00               je 0x140476e99
00476A2F  0F 57 C0                        xorps xmm0, xmm0
00476A32  0F 11 85 98 00 00 00            movups xmmword ptr [rbp + 0x98], xmm0
00476A39  0F 11 85 A8 00 00 00            movups xmmword ptr [rbp + 0xa8], xmm0
00476A40  0F 11 85 B8 00 00 00            movups xmmword ptr [rbp + 0xb8], xmm0
00476A47  4C 8B 44 C6 40                  mov r8, qword ptr [rsi + rax*8 + 0x40]
00476A4C  4C 89 45 E0                     mov qword ptr [rbp - 0x20], r8
00476A50  4D 39 50 18                     cmp qword ptr [r8 + 0x18], r10
00476A54  0F 84 6C 01 00 00               je 0x140476bc6
00476A5A  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
00476A5E  48 85 C9                        test rcx, rcx
00476A61  75 27                           jne 0x140476a8a
00476A63  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00476A67  48 8D 55 90                     lea rdx, [rbp - 0x70]
00476A6B  E8 14 C4 E8 FF                  call 0x140302e84
00476A70  8B 4D 8C                        mov ecx, dword ptr [rbp - 0x74]
00476A73  45 33 D2                        xor r10d, r10d
00476A76  4C 8B 45 E0                     mov r8, qword ptr [rbp - 0x20]
00476A7A  85 C0                           test eax, eax
00476A7C  0F B6 C9                        movzx ecx, cl
00476A7F  41 0F 48 CD                     cmovs ecx, r13d
00476A83  89 4D 8C                        mov dword ptr [rbp - 0x74], ecx
00476A86  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
00476A8A  48 8B 87 48 04 00 00            mov rax, qword ptr [rdi + 0x448]
00476A91  48 85 C0                        test rax, rax
00476A94  74 1E                           je 0x140476ab4
00476A96  4C 8B 88 40 02 00 00            mov r9, qword ptr [rax + 0x240]
00476A9D  48 8B 90 50 02 00 00            mov rdx, qword ptr [rax + 0x250]
00476AA4  4C 8B 90 48 02 00 00            mov r10, qword ptr [rax + 0x248]
00476AAB  4C 8B 98 58 02 00 00            mov r11, qword ptr [rax + 0x258]
00476AB2  EB 09                           jmp 0x140476abd
00476AB4  4D 8B CA                        mov r9, r10
00476AB7  49 8B D2                        mov rdx, r10
00476ABA  45 33 DB                        xor r11d, r11d
00476ABD  48 8D 45 B8                     lea rax, [rbp - 0x48]
00476AC1  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00476AC6  41 8B 40 10                     mov eax, dword ptr [r8 + 0x10]
00476ACA  C6 44 24 50 00                  mov byte ptr [rsp + 0x50], 0
00476ACF  44 88 6C 24 48                  mov byte ptr [rsp + 0x48], r13b
00476AD4  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00476AD8  49 8B 40 18                     mov rax, qword ptr [r8 + 0x18]
00476ADC  4C 8B C1                        mov r8, rcx
00476ADF  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00476AE4  48 8B CF                        mov rcx, rdi
00476AE7  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
00476AEC  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
00476AF1  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00476AF6  48 8B 97 08 03 00 00            mov rdx, qword ptr [rdi + 0x308]
00476AFD  E8 CE 80 E8 FF                  call 0x1402febd0
00476B02  8B 4D B8                        mov ecx, dword ptr [rbp - 0x48]
00476B05  89 45 98                        mov dword ptr [rbp - 0x68], eax
00476B08  41 3B CD                        cmp ecx, r13d
00476B0B  0F 84 B5 00 00 00               je 0x140476bc6
00476B11  45 33 D2                        xor r10d, r10d
00476B14  85 C0                           test eax, eax
00476B16  0F 88 65 05 00 00               js 0x140477081
00476B1C  8B 87 C8 00 00 00               mov eax, dword ptr [rdi + 0xc8]
00476B22  A8 10                           test al, 0x10
00476B24  0F 84 8D 00 00 00               je 0x140476bb7
00476B2A  48 8B 87 48 04 00 00            mov rax, qword ptr [rdi + 0x448]
00476B31  48 85 C0                        test rax, rax
00476B34  74 1E                           je 0x140476b54
00476B36  4C 8B 88 40 02 00 00            mov r9, qword ptr [rax + 0x240]
00476B3D  48 8B 90 50 02 00 00            mov rdx, qword ptr [rax + 0x250]
00476B44  4C 8B 80 48 02 00 00            mov r8, qword ptr [rax + 0x248]
00476B4B  4C 8B 90 58 02 00 00            mov r10, qword ptr [rax + 0x258]
00476B52  EB 09                           jmp 0x140476b5d
00476B54  4D 8B CA                        mov r9, r10
00476B57  49 8B D2                        mov rdx, r10
00476B5A  4D 8B C2                        mov r8, r10
00476B5D  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00476B61  48 8D 45 B8                     lea rax, [rbp - 0x48]
00476B65  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00476B6A  44 88 6C 24 50                  mov byte ptr [rsp + 0x50], r13b
00476B6F  44 88 6C 24 48                  mov byte ptr [rsp + 0x48], r13b
00476B74  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
00476B77  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00476B7B  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
00476B7F  48 8B CF                        mov rcx, rdi
00476B82  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00476B87  4C 89 54 24 30                  mov qword ptr [rsp + 0x30], r10
00476B8C  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
00476B91  4C 8B 45 90                     mov r8, qword ptr [rbp - 0x70]
00476B95  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00476B9A  48 8B 97 08 03 00 00            mov rdx, qword ptr [rdi + 0x308]
00476BA1  E8 2A 80 E8 FF                  call 0x1402febd0
00476BA6  45 33 D2                        xor r10d, r10d
00476BA9  89 45 98                        mov dword ptr [rbp - 0x68], eax
00476BAC  85 C0                           test eax, eax
00476BAE  0F 88 CD 04 00 00               js 0x140477081
00476BB4  8B 4D B8                        mov ecx, dword ptr [rbp - 0x48]
00476BB7  44 38 55 8C                     cmp byte ptr [rbp - 0x74], r10b
00476BBB  75 09                           jne 0x140476bc6
00476BBD  41 3B CD                        cmp ecx, r13d
00476BC0  0F 85 B9 02 00 00               jne 0x140476e7f
00476BC6  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
00476BCA  48 8D 4D 28                     lea rcx, [rbp + 0x28]
00476BCE  4C 8B 45 D8                     mov r8, qword ptr [rbp - 0x28]
00476BD2  48 8B 52 20                     mov rdx, qword ptr [rdx + 0x20]
00476BD6  E8 5D 32 06 00                  call 0x1404d9e38
00476BDB  33 D2                           xor edx, edx
00476BDD  8B F0                           mov esi, eax
00476BDF  85 C0                           test eax, eax
00476BE1  0F 88 09 05 00 00               js 0x1404770f0
00476BE7  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00476BEB  41 8B 4F 10                     mov ecx, dword ptr [r15 + 0x10]
00476BEF  8B 40 30                        mov eax, dword ptr [rax + 0x30]
00476BF2  41 84 C5                        test r13b, al
00476BF5  74 0E                           je 0x140476c05
00476BF7  0F BA E1 19                     bt ecx, 0x19
00476BFB  72 04                           jb 0x140476c01
00476BFD  41 0B 4F 14                     or ecx, dword ptr [r15 + 0x14]
00476C01  8B F2                           mov esi, edx
00476C03  EB 04                           jmp 0x140476c09
00476C05  41 8B 77 14                     mov esi, dword ptr [r15 + 0x14]
00476C09  4D 8B 0C 24                     mov r9, qword ptr [r12]
00476C0D  48 8D 45 83                     lea rax, [rbp - 0x7d]
00476C11  4D 8B 44 24 10                  mov r8, qword ptr [r12 + 0x10]
00476C16  0F 57 C0                        xorps xmm0, xmm0
00476C19  48 89 94 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rdx
00476C21  0F BA E9 19                     bts ecx, 0x19
00476C25  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
00476C2D  48 8D 45 90                     lea rax, [rbp - 0x70]
00476C31  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00476C39  48 8D 45 78                     lea rax, [rbp + 0x78]
00476C3D  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00476C45  8A 85 D0 02 00 00               mov al, byte ptr [rbp + 0x2d0]
00476C4B  88 84 24 80 00 00 00            mov byte ptr [rsp + 0x80], al
00476C52  8A 45 82                        mov al, byte ptr [rbp - 0x7e]
00476C55  88 44 24 78                     mov byte ptr [rsp + 0x78], al
00476C59  48 8D 85 D0 01 00 00            lea rax, [rbp + 0x1d0]
00476C60  88 54 24 70                     mov byte ptr [rsp + 0x70], dl
00476C64  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00476C69  48 8D 45 E8                     lea rax, [rbp - 0x18]
00476C6D  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00476C72  48 8D 45 A0                     lea rax, [rbp - 0x60]
00476C76  48 89 54 24 58                  mov qword ptr [rsp + 0x58], rdx
00476C7B  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00476C80  8A 85 C8 02 00 00               mov al, byte ptr [rbp + 0x2c8]
00476C86  88 44 24 48                     mov byte ptr [rsp + 0x48], al
00476C8A  49 8B 47 20                     mov rax, qword ptr [r15 + 0x20]
00476C8E  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
00476C92  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00476C97  48 8D 85 98 00 00 00            lea rax, [rbp + 0x98]
00476C9E  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
00476CA3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00476CA8  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00476CAC  48 8D 4D 28                     lea rcx, [rbp + 0x28]
00476CB0  0F 11 85 98 00 00 00            movups xmmword ptr [rbp + 0x98], xmm0
00476CB7  0F 11 85 A8 00 00 00            movups xmmword ptr [rbp + 0xa8], xmm0
00476CBE  0F 11 85 B8 00 00 00            movups xmmword ptr [rbp + 0xb8], xmm0
00476CC5  E8 E6 8A F5 FF                  call 0x1403cf7b0
00476CCA  44 8B 9D B4 00 00 00            mov r11d, dword ptr [rbp + 0xb4]
00476CD1  45 33 D2                        xor r10d, r10d
00476CD4  44 8B 4D 9C                     mov r9d, dword ptr [rbp - 0x64]
00476CD8  45 0B D9                        or r11d, r9d
00476CDB  88 45 88                        mov byte ptr [rbp - 0x78], al
00476CDE  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00476CE2  0B 30                           or esi, dword ptr [rax]
00476CE4  23 75 A0                        and esi, dword ptr [rbp - 0x60]
00476CE7  89 75 A0                        mov dword ptr [rbp - 0x60], esi
00476CEA  44 38 55 82                     cmp byte ptr [rbp - 0x7e], r10b
00476CEE  74 0A                           je 0x140476cfa
00476CF0  8B C6                           mov eax, esi
00476CF2  25 00 00 06 00                  and eax, 0x60000
00476CF7  44 0B D8                        or r11d, eax
00476CFA  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
00476D00  B9 22 00 00 C0                  mov ecx, 0xc0000022
00476D05  44 8B 45 A4                     mov r8d, dword ptr [rbp - 0x5c]
00476D09  F7 D0                           not eax
00476D0B  44 23 D8                        and r11d, eax
00476D0E  8B 45 E8                        mov eax, dword ptr [rbp - 0x18]
00476D11  21 75 C0                        and dword ptr [rbp - 0x40], esi
00476D14  8B 75 C4                        mov esi, dword ptr [rbp - 0x3c]
00476D17  0F 44 C1                        cmove eax, ecx
00476D1A  41 8B CB                        mov ecx, r11d
00476D1D  33 CE                           xor ecx, esi
00476D1F  89 45 BC                        mov dword ptr [rbp - 0x44], eax
00476D22  23 CE                           and ecx, esi
00476D24  74 23                           je 0x140476d49
00476D26  4C 8D 8D D0 00 00 00            lea r9, [rbp + 0xd0]
00476D2D  44 88 54 24 20                  mov byte ptr [rsp + 0x20], r10b
00476D32  BA 00 00 05 00                  mov edx, 0x50000
00476D37  E8 44 8C FB FF                  call 0x14042f980
00476D3C  44 8B 4D 9C                     mov r9d, dword ptr [rbp - 0x64]
00476D40  41 23 F3                        and esi, r11d
00476D43  89 75 C4                        mov dword ptr [rbp - 0x3c], esi
00476D46  45 33 D2                        xor r10d, r10d
00476D49  8A 55 84                        mov dl, byte ptr [rbp - 0x7c]
00476D4C  84 D2                           test dl, dl
00476D4E  0F 84 24 03 00 00               je 0x140477078
00476D54  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00476D58  48 8B 50 28                     mov rdx, qword ptr [rax + 0x28]
00476D5C  48 85 D2                        test rdx, rdx
00476D5F  0F 84 F0 02 00 00               je 0x140477055
00476D65  4C 8B 45 D8                     mov r8, qword ptr [rbp - 0x28]
00476D69  48 8D 4D 50                     lea rcx, [rbp + 0x50]
00476D6D  E8 C6 30 06 00                  call 0x1404d9e38
00476D72  45 33 C9                        xor r9d, r9d
00476D75  8B F0                           mov esi, eax
00476D77  85 C0                           test eax, eax
00476D79  0F 88 2B 03 00 00               js 0x1404770aa
00476D7F  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00476D83  41 8B 4F 10                     mov ecx, dword ptr [r15 + 0x10]
00476D87  F7 40 30 00 01 00 00            test dword ptr [rax + 0x30], 0x100
00476D8E  74 0F                           je 0x140476d9f
00476D90  0F BA E1 19                     bt ecx, 0x19
00476D94  72 04                           jb 0x140476d9a
00476D96  41 0B 4F 14                     or ecx, dword ptr [r15 + 0x14]
00476D9A  41 8B C1                        mov eax, r9d
00476D9D  EB 04                           jmp 0x140476da3
00476D9F  41 8B 47 14                     mov eax, dword ptr [r15 + 0x14]
00476DA3  44 8A 85 D0 02 00 00            mov r8b, byte ptr [rbp + 0x2d0]
00476DAA  48 8D 55 89                     lea rdx, [rbp - 0x77]
00476DAE  4C 89 8C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r9
00476DB6  0F 57 C0                        xorps xmm0, xmm0
00476DB9  48 89 94 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdx
00476DC1  48 8D 55 90                     lea rdx, [rbp - 0x70]
00476DC5  48 89 94 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdx
00476DCD  48 8D 55 78                     lea rdx, [rbp + 0x78]
00476DD1  48 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdx
00476DD9  8A 55 82                        mov dl, byte ptr [rbp - 0x7e]
00476DDC  44 88 84 24 80 00 00 00         mov byte ptr [rsp + 0x80], r8b
00476DE4  4D 8B 44 24 10                  mov r8, qword ptr [r12 + 0x10]
00476DE9  88 54 24 78                     mov byte ptr [rsp + 0x78], dl
00476DED  48 8D 95 D0 01 00 00            lea rdx, [rbp + 0x1d0]
00476DF4  44 88 4C 24 70                  mov byte ptr [rsp + 0x70], r9b
00476DF9  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
00476DFE  48 8D 55 F8                     lea rdx, [rbp - 8]
00476E02  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
00476E07  48 8D 55 C8                     lea rdx, [rbp - 0x38]
00476E0B  4C 89 4C 24 58                  mov qword ptr [rsp + 0x58], r9
00476E10  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
00476E15  8A 95 C8 02 00 00               mov dl, byte ptr [rbp + 0x2c8]
00476E1B  88 54 24 48                     mov byte ptr [rsp + 0x48], dl
00476E1F  33 D2                           xor edx, edx
00476E21  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00476E25  49 8B 47 20                     mov rax, qword ptr [r15 + 0x20]
00476E29  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00476E2E  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
00476E33  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
00476E38  4D 8B 0C 24                     mov r9, qword ptr [r12]
00476E3C  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00476E40  48 8D 4D 50                     lea rcx, [rbp + 0x50]
00476E44  0F 11 85 98 00 00 00            movups xmmword ptr [rbp + 0x98], xmm0
00476E4B  0F 11 85 A8 00 00 00            movups xmmword ptr [rbp + 0xa8], xmm0
00476E52  0F 11 85 B8 00 00 00            movups xmmword ptr [rbp + 0xb8], xmm0
00476E59  E8 52 89 F5 FF                  call 0x1403cf7b0
00476E5E  8B 4D A4                        mov ecx, dword ptr [rbp - 0x5c]
00476E61  8B 55 A8                        mov edx, dword ptr [rbp - 0x58]
00476E64  8B 45 9C                        mov eax, dword ptr [rbp - 0x64]
00476E67  48 8B 75 B0                     mov rsi, qword ptr [rbp - 0x50]
00476E6B  44 88 6C CB 04                  mov byte ptr [rbx + rcx*8 + 4], r13b
00476E70  0B 45 C8                        or eax, dword ptr [rbp - 0x38]
00476E73  89 04 CB                        mov dword ptr [rbx + rcx*8], eax
00476E76  23 55 C8                        and edx, dword ptr [rbp - 0x38]
00476E79  89 55 A8                        mov dword ptr [rbp - 0x58], edx
00476E7C  45 33 D2                        xor r10d, r10d
00476E7F  8A 55 84                        mov dl, byte ptr [rbp - 0x7c]
00476E82  8B 45 A4                        mov eax, dword ptr [rbp - 0x5c]
00476E85  8B 4E 3C                        mov ecx, dword ptr [rsi + 0x3c]
00476E88  41 03 C5                        add eax, r13d
00476E8B  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
00476E8E  89 4D 98                        mov dword ptr [rbp - 0x68], ecx
00476E91  3B C1                           cmp eax, ecx
00476E93  0F 82 96 FB FF FF               jb 0x140476a2f
00476E99  33 F6                           xor esi, esi
00476E9B  84 D2                           test dl, dl
00476E9D  0F 84 DF 00 00 00               je 0x140476f82
00476EA3  8B 55 A8                        mov edx, dword ptr [rbp - 0x58]
00476EA6  44 8B 45 C0                     mov r8d, dword ptr [rbp - 0x40]
00476EAA  41 3B D0                        cmp edx, r8d
00476EAD  0F 84 CF 00 00 00               je 0x140476f82
00476EB3  8B F2                           mov esi, edx
00476EB5  41 33 F0                        xor esi, r8d
00476EB8  8B C6                           mov eax, esi
00476EBA  23 F2                           and esi, edx
00476EBC  41 23 C0                        and eax, r8d
00476EBF  33 D2                           xor edx, edx
00476EC1  89 45 8C                        mov dword ptr [rbp - 0x74], eax
00476EC4  85 C9                           test ecx, ecx
00476EC6  0F 84 B4 00 00 00               je 0x140476f80
00476ECC  4C 8B E3                        mov r12, rbx
00476ECF  8B FA                           mov edi, edx
00476ED1  45 33 FF                        xor r15d, r15d
00476ED4  85 F6                           test esi, esi
00476ED6  75 08                           jne 0x140476ee0
00476ED8  85 C0                           test eax, eax
00476EDA  0F 84 94 00 00 00               je 0x140476f74
00476EE0  45 38 7C 24 04                  cmp byte ptr [r12 + 4], r15b
00476EE5  74 7E                           je 0x140476f65
00476EE7  45 8B 1C 24                     mov r11d, dword ptr [r12]
00476EEB  41 8B CB                        mov ecx, r11d
00476EEE  33 C8                           xor ecx, eax
00476EF0  23 C8                           and ecx, eax
00476EF2  74 20                           je 0x140476f14
00476EF4  44 8B C7                        mov r8d, edi
00476EF7  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
00476EFC  41 C1 E0 18                     shl r8d, 0x18
00476F00  4C 8D 8D 50 01 00 00            lea r9, [rbp + 0x150]
00476F07  BA 00 00 00 80                  mov edx, 0x80000000
00476F0C  E8 6F 8A FB FF                  call 0x14042f980
00476F11  8B 45 8C                        mov eax, dword ptr [rbp - 0x74]
00476F14  F7 D1                           not ecx
00476F16  23 C1                           and eax, ecx
00476F18  89 45 8C                        mov dword ptr [rbp - 0x74], eax
00476F1B  44 23 DE                        and r11d, esi
00476F1E  74 20                           je 0x140476f40
00476F20  44 8B C7                        mov r8d, edi
00476F23  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
00476F28  41 C1 E0 18                     shl r8d, 0x18
00476F2C  4C 8D 8D 50 01 00 00            lea r9, [rbp + 0x150]
00476F33  BA 00 00 00 80                  mov edx, 0x80000000
00476F38  41 8B CB                        mov ecx, r11d
00476F3B  E8 40 8A FB FF                  call 0x14042f980
00476F40  41 F7 D3                        not r11d
00476F43  48 8D 95 50 01 00 00            lea rdx, [rbp + 0x150]
00476F4A  41 23 F3                        and esi, r11d
00476F4D  48 8D 8D D0 00 00 00            lea rcx, [rbp + 0xd0]
00476F54  41 B8 00 00 00 FF               mov r8d, 0xff000000
00476F5A  E8 1D 67 22 00                  call 0x14069d67c
00476F5F  8B 45 8C                        mov eax, dword ptr [rbp - 0x74]
00476F62  8B 4D 98                        mov ecx, dword ptr [rbp - 0x68]
00476F65  41 03 FD                        add edi, r13d
00476F68  49 83 C4 08                     add r12, 8
00476F6C  3B F9                           cmp edi, ecx
00476F6E  0F 82 60 FF FF FF               jb 0x140476ed4
00476F74  4C 8B 7D 18                     mov r15, qword ptr [rbp + 0x18]
00476F78  4C 8B 65 20                     mov r12, qword ptr [rbp + 0x20]
00476F7C  48 8B 7D F0                     mov rdi, qword ptr [rbp - 0x10]
00476F80  33 F6                           xor esi, esi
00476F82  48 85 DB                        test rbx, rbx
00476F85  74 0A                           je 0x140476f91
00476F87  33 D2                           xor edx, edx
00476F89  48 8B CB                        mov rcx, rbx
00476F8C  E8 DF B8 70 00                  call 0x140b82870
00476F91  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00476F95  8B 4D BC                        mov ecx, dword ptr [rbp - 0x44]
00476F98  89 08                           mov dword ptr [rax], ecx
00476F9A  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00476F9E  8B 4D C0                        mov ecx, dword ptr [rbp - 0x40]
00476FA1  21 08                           and dword ptr [rax], ecx
00476FA3  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00476FA7  39 30                           cmp dword ptr [rax], esi
00476FA9  7D 04                           jge 0x140476faf
00476FAB  40 88 75 83                     mov byte ptr [rbp - 0x7d], sil
00476FAF  49 8B 4E 18                     mov rcx, qword ptr [r14 + 0x18]
00476FB3  48 8D 95 D0 00 00 00            lea rdx, [rbp + 0xd0]
00476FBA  45 33 C0                        xor r8d, r8d
00476FBD  E8 BA 66 22 00                  call 0x14069d67c
00476FC2  49 8B 4E 18                     mov rcx, qword ptr [r14 + 0x18]
00476FC6  48 8D 95 D0 00 00 00            lea rdx, [rbp + 0xd0]
00476FCD  41 B8 00 00 00 FF               mov r8d, 0xff000000
00476FD3  E8 A4 66 22 00                  call 0x14069d67c
00476FD8  40 38 75 85                     cmp byte ptr [rbp - 0x7b], sil
00476FDC  0F 85 13 01 00 00               jne 0x1404770f5
00476FE2  41 8B 57 10                     mov edx, dword ptr [r15 + 0x10]
00476FE6  0F BA E2 19                     bt edx, 0x19
00476FEA  0F 83 05 01 00 00               jae 0x1404770f5
00476FF0  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00476FF4  41 8B 18                        mov ebx, dword ptr [r8]
00476FF7  40 38 75 AC                     cmp byte ptr [rbp - 0x54], sil
00476FFB  74 2F                           je 0x14047702c
00476FFD  40 38 B5 8E 00 00 00            cmp byte ptr [rbp + 0x8e], sil
00477004  0F 85 6B 01 00 00               jne 0x140477175
0047700A  40 38 B5 8D 00 00 00            cmp byte ptr [rbp + 0x8d], sil
00477011  0F 85 5E 01 00 00               jne 0x140477175
00477017  8B 87 C8 00 00 00               mov eax, dword ptr [rdi + 0xc8]
0047701D  B9 00 00 00 03                  mov ecx, 0x3000000
00477022  23 C1                           and eax, ecx
00477024  3B C1                           cmp eax, ecx
00477026  0F 84 49 01 00 00               je 0x140477175
0047702C  4D 8B 4E 10                     mov r9, qword ptr [r14 + 0x10]
00477030  48 8D 45 83                     lea rax, [rbp - 0x7d]
00477034  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
00477038  48 8D 4D 08                     lea rcx, [rbp + 8]
0047703C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00477041  E8 2A 8C FC FF                  call 0x14043fc70
00477046  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
0047704A  8B 0A                           mov ecx, dword ptr [rdx]
0047704C  F7 D1                           not ecx
0047704E  23 CB                           and ecx, ebx
00477050  E9 0A 01 00 00                  jmp 0x14047715f
00477055  48 8B 75 B0                     mov rsi, qword ptr [rbp - 0x50]
00477059  41 8B C1                        mov eax, r9d
0047705C  41 8B C8                        mov ecx, r8d
0047705F  44 88 6C CB 04                  mov byte ptr [rbx + rcx*8 + 4], r13b
00477064  0B 45 A0                        or eax, dword ptr [rbp - 0x60]
00477067  89 04 CB                        mov dword ptr [rbx + rcx*8], eax
0047706A  8B 45 A8                        mov eax, dword ptr [rbp - 0x58]
0047706D  23 45 A0                        and eax, dword ptr [rbp - 0x60]
00477070  89 45 A8                        mov dword ptr [rbp - 0x58], eax
00477073  E9 07 FE FF FF                  jmp 0x140476e7f
00477078  48 8B 75 B0                     mov rsi, qword ptr [rbp - 0x50]
0047707C  E9 01 FE FF FF                  jmp 0x140476e82
00477081  44 38 55 80                     cmp byte ptr [rbp - 0x80], r10b
00477085  75 08                           jne 0x14047708f
00477087  49 8B CC                        mov rcx, r12
0047708A  E8 91 F4 44 00                  call 0x1408c6520
0047708F  48 8B CE                        mov rcx, rsi
00477092  E8 05 AE 03 00                  call 0x1404b1e9c
00477097  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
0047709B  33 FF                           xor edi, edi
0047709D  8B 4D 98                        mov ecx, dword ptr [rbp - 0x68]
004770A0  89 38                           mov dword ptr [rax], edi
004770A2  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
004770A6  89 08                           mov dword ptr [rax], ecx
004770A8  EB 25                           jmp 0x1404770cf
004770AA  44 38 4D 80                     cmp byte ptr [rbp - 0x80], r9b
004770AE  75 08                           jne 0x1404770b8
004770B0  49 8B CC                        mov rcx, r12
004770B3  E8 68 F4 44 00                  call 0x1408c6520
004770B8  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
004770BC  E8 DB AD 03 00                  call 0x1404b1e9c
004770C1  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
004770C5  33 FF                           xor edi, edi
004770C7  89 38                           mov dword ptr [rax], edi
004770C9  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
004770CD  89 30                           mov dword ptr [rax], esi
004770CF  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
004770D3  E8 18 A9 E8 FF                  call 0x1403019f0
004770D8  48 85 DB                        test rbx, rbx
004770DB  0F 84 4D 02 00 00               je 0x14047732e
004770E1  33 D2                           xor edx, edx
004770E3  48 8B CB                        mov rcx, rbx
004770E6  E8 85 B7 70 00                  call 0x140b82870
004770EB  E9 3E 02 00 00                  jmp 0x14047732e
004770F0  38 55 80                        cmp byte ptr [rbp - 0x80], dl
004770F3  EB B9                           jmp 0x1404770ae
004770F5  40 38 75 AC                     cmp byte ptr [rbp - 0x54], sil
004770F9  74 7A                           je 0x140477175
004770FB  40 38 B5 8E 00 00 00            cmp byte ptr [rbp + 0x8e], sil
00477102  75 71                           jne 0x140477175
00477104  40 38 B5 8D 00 00 00            cmp byte ptr [rbp + 0x8d], sil
0047710B  75 68                           jne 0x140477175
0047710D  8B 87 C8 00 00 00               mov eax, dword ptr [rdi + 0xc8]
00477113  B9 00 00 00 03                  mov ecx, 0x3000000
00477118  23 C1                           and eax, ecx
0047711A  3B C1                           cmp eax, ecx
0047711C  75 25                           jne 0x140477143
0047711E  39 B5 84 00 00 00               cmp dword ptr [rbp + 0x84], esi
00477124  75 1D                           jne 0x140477143
00477126  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0047712A  44 88 AD 8F 00 00 00            mov byte ptr [rbp + 0x8f], r13b
00477131  89 30                           mov dword ptr [rax], esi
00477133  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
00477137  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
0047713B  89 01                           mov dword ptr [rcx], eax
0047713D  44 88 6D 83                     mov byte ptr [rbp - 0x7d], r13b
00477141  EB 32                           jmp 0x140477175
00477143  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
00477147  C7 00 22 00 00 C0               mov dword ptr [rax], 0xc0000022
0047714D  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00477151  89 30                           mov dword ptr [rax], esi
00477153  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00477157  40 88 75 83                     mov byte ptr [rbp - 0x7d], sil
0047715B  8B 08                           mov ecx, dword ptr [rax]
0047715D  F7 D1                           not ecx
0047715F  4D 8B 4E 18                     mov r9, qword ptr [r14 + 0x18]
00477163  45 33 C0                        xor r8d, r8d
00477166  BA 00 00 30 00                  mov edx, 0x300000
0047716B  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
00477170  E8 0B 88 FB FF                  call 0x14042f980
00477175  41 8B 57 10                     mov edx, dword ptr [r15 + 0x10]
00477179  0F BA E2 19                     bt edx, 0x19
0047717D  0F 83 AA 00 00 00               jae 0x14047722d
00477183  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
00477187  48 8D 45 86                     lea rax, [rbp - 0x7a]
0047718B  4D 8B 4E 10                     mov r9, qword ptr [r14 + 0x10]
0047718F  8B 4D D0                        mov ecx, dword ptr [rbp - 0x30]
00477192  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00477197  48 8D 45 83                     lea rax, [rbp - 0x7d]
0047719B  41 8B 18                        mov ebx, dword ptr [r8]
0047719E  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
004771A2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004771A7  E8 34 8C FC FF                  call 0x14043fde0
004771AC  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
004771B0  45 33 C0                        xor r8d, r8d
004771B3  4D 8B 4E 18                     mov r9, qword ptr [r14 + 0x18]
004771B7  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
004771BC  8B 0A                           mov ecx, dword ptr [rdx]
004771BE  BA 00 00 90 00                  mov edx, 0x900000
004771C3  F7 D1                           not ecx
004771C5  23 CB                           and ecx, ebx
004771C7  E8 B4 87 FB FF                  call 0x14042f980
004771CC  4D 8B 46 08                     mov r8, qword ptr [r14 + 8]
004771D0  48 8D 45 87                     lea rax, [rbp - 0x79]
004771D4  4D 8B 4E 10                     mov r9, qword ptr [r14 + 0x10]
004771D8  8B 4D 00                        mov ecx, dword ptr [rbp]
004771DB  41 8B 57 10                     mov edx, dword ptr [r15 + 0x10]
004771DF  41 8B 18                        mov ebx, dword ptr [r8]
004771E2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
004771E7  48 8D 45 83                     lea rax, [rbp - 0x7d]
004771EB  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
004771EF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004771F4  E8 E7 8B FC FF                  call 0x14043fde0
004771F9  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
004771FD  45 33 C0                        xor r8d, r8d
00477200  4D 8B 4E 18                     mov r9, qword ptr [r14 + 0x18]
00477204  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
00477209  8B 0A                           mov ecx, dword ptr [rdx]
0047720B  BA 00 00 A0 00                  mov edx, 0xa00000
00477210  F7 D1                           not ecx
00477212  23 CB                           and ecx, ebx
00477214  E8 67 87 FB FF                  call 0x14042f980
00477219  E8 4A 67 15 00                  call 0x1405cd968
0047721E  85 C0                           test eax, eax
00477220  74 0B                           je 0x14047722d
00477222  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
00477226  8B 45 CC                        mov eax, dword ptr [rbp - 0x34]
00477229  F7 D0                           not eax
0047722B  21 01                           and dword ptr [rcx], eax
0047722D  48 85 FF                        test rdi, rdi
00477230  0F 84 B4 00 00 00               je 0x1404772ea
00477236  40 38 75 86                     cmp byte ptr [rbp - 0x7a], sil
0047723A  75 2D                           jne 0x140477269
0047723C  40 38 75 87                     cmp byte ptr [rbp - 0x79], sil
00477240  75 27                           jne 0x140477269
00477242  8B 8D 84 00 00 00               mov ecx, dword ptr [rbp + 0x84]
00477248  85 C9                           test ecx, ecx
0047724A  75 70                           jne 0x1404772bc
0047724C  F7 87 C8 00 00 00 00 40 00 00   test dword ptr [rdi + 0xc8], 0x4000
00477256  74 64                           je 0x1404772bc
00477258  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0047725C  39 30                           cmp dword ptr [rax], esi
0047725E  7C 09                           jl 0x140477269
00477260  40 38 B5 8F 00 00 00            cmp byte ptr [rbp + 0x8f], sil
00477267  74 53                           je 0x1404772bc
00477269  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0047726D  49 8B CC                        mov rcx, r12
00477270  41 8B 7F 14                     mov edi, dword ptr [r15 + 0x14]
00477274  41 0B 7F 10                     or edi, dword ptr [r15 + 0x10]
00477278  49 8B 5F 08                     mov rbx, qword ptr [r15 + 8]
0047727C  8B 30                           mov esi, dword ptr [rax]
0047727E  C1 EE 1F                        shr esi, 0x1f
00477281  41 32 F5                        xor sil, r13b
00477284  E8 B7 67 F7 FF                  call 0x1403eda40
00477289  C6 44 24 38 00                  mov byte ptr [rsp + 0x38], 0
0047728E  4C 8B C8                        mov r9, rax
00477291  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00477295  45 33 C0                        xor r8d, r8d
00477298  40 88 74 24 30                  mov byte ptr [rsp + 0x30], sil
0047729D  33 D2                           xor edx, edx
0047729F  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
004772A3  48 8B 7D F0                     mov rdi, qword ptr [rbp - 0x10]
004772A7  48 8B CF                        mov rcx, rdi
004772AA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004772AF  E8 9C 12 FD FF                  call 0x140448550
004772B4  8B 8D 84 00 00 00               mov ecx, dword ptr [rbp + 0x84]
004772BA  33 F6                           xor esi, esi
004772BC  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
004772C0  39 30                           cmp dword ptr [rax], esi
004772C2  7D 26                           jge 0x1404772ea
004772C4  85 C9                           test ecx, ecx
004772C6  75 22                           jne 0x1404772ea
004772C8  F7 87 C8 00 00 00 00 40 00 00   test dword ptr [rdi + 0xc8], 0x4000
004772D2  74 16                           je 0x1404772ea
004772D4  41 8B 57 10                     mov edx, dword ptr [r15 + 0x10]
004772D8  48 8D 4D 78                     lea rcx, [rbp + 0x78]
004772DC  E8 A3 B1 FE FF                  call 0x140462484
004772E1  84 C0                           test al, al
004772E3  74 05                           je 0x1404772ea
004772E5  E8 B6 75 FA FF                  call 0x14041e8a0
004772EA  40 38 75 81                     cmp byte ptr [rbp - 0x7f], sil
004772EE  74 09                           je 0x1404772f9
004772F0  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
004772F4  E8 A3 AB 03 00                  call 0x1404b1e9c
004772F9  40 38 75 80                     cmp byte ptr [rbp - 0x80], sil
004772FD  75 08                           jne 0x140477307
004772FF  49 8B CC                        mov rcx, r12
00477302  E8 19 F2 44 00                  call 0x1408c6520
00477307  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0047730B  E8 E0 A6 E8 FF                  call 0x1403019f0
00477310  40 38 75 88                     cmp byte ptr [rbp - 0x78], sil
00477314  74 0A                           je 0x140477320
00477316  40 38 75 83                     cmp byte ptr [rbp - 0x7d], sil
0047731A  0F 85 02 EF FF FF               jne 0x140476222
00477320  44 8A EE                        mov r13b, sil
00477323  E9 FA EE FF FF                  jmp 0x140476222
00477328  C7 01 0D 00 00 C0               mov dword ptr [rcx], 0xc000000d
0047732E  32 C0                           xor al, al
00477330  48 8B 8D 50 02 00 00            mov rcx, qword ptr [rbp + 0x250]
00477337  48 33 CC                        xor rcx, rsp
0047733A  E8 01 53 23 00                  call 0x1406ac640
0047733F  48 8B 9C 24 D8 03 00 00         mov rbx, qword ptr [rsp + 0x3d8]
00477347  48 81 C4 90 03 00 00            add rsp, 0x390
0047734E  41 5F                           pop r15
00477350  41 5E                           pop r14
00477352  41 5D                           pop r13
00477354  41 5C                           pop r12
00477356  5F                              pop rdi
00477357  5E                              pop rsi
00477358  5D                              pop rbp
00477359  C3                              ret
0047735A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepCommonAccessCheckEx(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, unsigned __int8 a6, unsigned __int8 a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1E0;
    unsigned int v_stack_m1E4;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m200;
    unsigned __int8 v_stack_m209;
    unsigned __int8 v_stack_m20A;
    unsigned __int8 v_stack_m20B;
    unsigned __int64 v_stack_m20C;
    unsigned int v_stack_m214;
    unsigned __int64 v_stack_m21C;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned int v_stack_m284;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned int v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned int v_stack_m2B0;
    unsigned __int64 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned int v_stack_m2C8;
    unsigned int v_stack_m2CC;
    unsigned int v_stack_m2D0;
    unsigned int v_stack_m2D4;
    unsigned int v_stack_m2D8;
    unsigned int v_stack_m2DC;
    unsigned int v_stack_m2E0;
    unsigned __int64 v_stack_m2E8;
    unsigned __int8 v_stack_m2EC;
    unsigned int v_stack_m2F0;
    unsigned int v_stack_m2F4;
    unsigned int v_stack_m2F8;
    unsigned int v_stack_m2FC;
    unsigned int v_stack_m300;
    unsigned __int64 v_stack_m308;
    unsigned __int8 v_stack_m30C;
    unsigned __int8 v_stack_m30F;
    unsigned __int8 v_stack_m310;
    unsigned __int8 v_stack_m311;
    unsigned __int8 v_stack_m312;
    unsigned __int8 v_stack_m313;
    unsigned __int8 v_stack_m314;
    unsigned __int8 v_stack_m315;
    unsigned __int8 v_stack_m316;
    unsigned __int8 v_stack_m317;
    unsigned __int8 v_stack_m318;
    unsigned __int64 v_stack_m328;
    unsigned __int64 v_stack_m330;
    unsigned __int64 v_stack_m338;
    unsigned __int64 v_stack_m340;
    unsigned __int8 v_stack_m348;
    unsigned __int8 v_stack_m350;
    unsigned __int8 v_stack_m358;
    unsigned __int64 v_stack_m360;
    unsigned __int64 v_stack_m368;
    unsigned __int64 v_stack_m370;
    unsigned __int64 v_stack_m378;
    unsigned __int8 v_stack_m380;
    unsigned int v_stack_m388;
    unsigned __int8 v_stack_m390;
    unsigned __int64 v_stack_m398;
    unsigned __int8 v_stack_m3A0;
    unsigned __int8 v_stack_m3A8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (912);
    result = (*(unsigned __int64 *)(v_rip + 10045166)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m278 = a1;
    v_stack_m280 = a3;
    v_stack_m318 = (unsigned __int8)(a2);
    a1 = 0;
    result = 0;
    v_stack_m315 = 0;
    v_stack_m30F = 0;
    v_stack_m20C = 0;
    v_stack_m2C0 = 0;
    v_stack_m2D0 = 0;
    a2 = 0;
    v_stack_m2A0 = 0;
    v_stack_m2E8 = 0;
    v_stack_m317 = 0;
    v_stack_m308 = 0;
    v_stack_m2E0 = 0;
    v_stack_m290 = v_xmm0;
    v_stack_m250 = 0;
    v_stack_m21C = v_xmm1;
    v_stack_m228 = 0;
    v_stack_m270 = v_xmm0;
    v_stack_m260 = v_xmm0;
    v_stack_m248 = v_xmm1;
    v_stack_m238 = v_xmm1;
    result = memset(v_stack_m1C8, a2, 128, a4);
    a2 = 0;
    result = memset(v_stack_m148, a2, 128, a4);
    a2 = 0;
    result = memset(v_stack_mC8, a2, 128, a4);
    v_rdi = 0;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    v_stack_m312 = 0;
    v_stack_m311 = 0;
    v_stack_m2CC = 0;
    v_stack_m2C8 = (unsigned int)(result);
    v_stack_m298 = (unsigned int)(result);
    if (a4 == 0) goto loc_0047732E;
    if ((*(unsigned int *)(a4)) != 40) goto loc_0047732E;
    if (*(unsigned __int64 *)(a4 + 16) == 0) goto loc_0047732E;
    if (0 == 0) goto loc_00477328;
    if (a3 == 0) goto loc_00477328;
    if ((*(unsigned int *)(a3)) != 56) goto loc_00477328;
    if (*(unsigned __int64 *)(a4 + 8) == 0) goto loc_00477328;
    if (*(unsigned __int64 *)(a3 + 8) == 0) goto loc_00476178;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a3 + 8))) != 16) goto loc_00477328;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a3 + 8) + 4)) & (0xFFFFFFF8ULL)) != 0) goto loc_00477328;
loc_00476178:
    if (a5 == 0) goto loc_0047618D;
    if ((*(unsigned int *)(a5)) != 96) goto loc_00477328;
loc_0047618D:
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 8)) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = (unsigned int)((unsigned int)(0xC0000022ULL));
    v_stack_m2F8 = 0;
    v_stack_m2B0 = (unsigned int)((unsigned int)(0xC0000022ULL));
    if (*(unsigned __int64 *)(a4 + 32) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 32)) = 0;
    }
    v_rsi = (unsigned int)(~((unsigned int)(*(unsigned int *)(a3 + 20))));
    v_rsi = (unsigned int)((v_rsi) & (*(unsigned int *)(a3 + 16)));
    v_rsi = (unsigned int)((v_rsi) & ((unsigned int)((unsigned int)(0xFDFFFFFFULL))));
    v_stack_m3A8 = 1;
    v_stack_m2DC = (unsigned int)(v_rsi);
    a3 = 0;
    a2 = 0;
    result = AuthzBasepSetAccessReasons((unsigned int)((unsigned int)(v_rsi)), a2, a3, *(unsigned __int64 *)(a4 + 24));
    if (a6 != 0) goto loc_0047622A;
    if (a6 >= 0) goto loc_00476216;
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 8)) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3 + 32) + 12)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 16))) & ((unsigned int)((unsigned int)(0xFDFFFFFFULL))));
    goto loc_0047621C;
loc_00476216:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 20))) | (*(unsigned int *)(a3 + 20)));
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 8)) = (unsigned int)(result);
loc_0047621C:
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = 0;
loc_00476222:
    goto loc_00477330;
loc_0047622A:
    if (*(unsigned __int64 *)(a3 + 8) == 0) goto loc_00476264;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 8) + 8)) == 0) goto loc_00476264;
    if ((*(unsigned __int64 *)(a1)) == 0) goto loc_00476256;
    if ((*(unsigned int *)(a1 + 8)) >= 2) goto loc_00476256;
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = 0xC00000A5ULL;
    goto loc_0047732E;
loc_00476256:
    if ((*(unsigned int *)(a3 + 16)) != 0) goto loc_0047628D;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 20))) != 0) goto loc_00476273;
loc_00476264:
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = 0xC0000022ULL;
    goto loc_0047732E;
loc_00476273:
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 8)) = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 20)));
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = 0;
    if (*(unsigned __int64 *)(a4 + 32) == 0) goto loc_00476222;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 32)) = 0;
    goto loc_00476222;
loc_0047628D:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)))) == 1) goto loc_004762AB;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)))) == (*(unsigned int *)(a3 + 40))) goto loc_004762AB;
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = 0xC000000DULL;
    goto loc_0047732E;
loc_004762AB:
    result = *(unsigned __int64 *)(a4 + 16);
    if ((unsigned __int8)((unsigned __int8)(a2)) == 0) {
        a1 = 0;
        result = SeLockSubjectContext(a1, a2, a3, *(unsigned __int64 *)(a4 + 24));
    }
    v_stack_m398 = v_stack_m2C8;
    a4 = 0;
    v_stack_m3A0 = 0;
    v_stack_m3A8 = 0;
    result = SepTrustLevelCheck(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 8) + 8), a1, a4);
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = (unsigned int)(result);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a4 + 16))) >= 0) goto loc_004762F2;
    goto loc_00476511;
loc_004762F2:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 16))))) & ((unsigned int)((unsigned int)(v_stack_m2C8))));
    result = (unsigned int)((result) - ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 16)))));
    result = (unsigned int)(-(result));
    a4 = 0;
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000022ULL))));
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = (unsigned int)(result);
    v_stack_m2A8 = *(unsigned __int64 *)(a1);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a4 + 16))) >= 0) goto loc_004763A1;
    v_r13 = *(unsigned __int64 *)(a1);
    if (*(unsigned __int64 *)(a1) == 0) {
        v_r13 = *(unsigned __int64 *)(a1 + 16);
    }
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 20))) | (*(unsigned int *)(a3 + 16)));
    result = SepLocateTokenTrustLevel(a1, *(unsigned __int64 *)(a4 + 16), a1, a4);
    v_r15 = 0;
    a3 = 0;
    v_stack_m390 = 0;
    a2 = 0;
    v_stack_m398 = 0;
    v_stack_m3A0 = (unsigned int)(v_rsi);
    v_stack_m3A8 = *(unsigned __int64 *)(*(unsigned __int64 *)(a3 + 8) + 8);
    result = SeLogAccessFailure(v_r13, a2, a3, result);
    if (v_stack_m318 == 0) {
        a1 = a1;
        result = SeUnlockSubjectContext(a1, a2, a3, result);
    }
    v_rbx = (unsigned int)(~((unsigned int)(v_stack_m2C8)));
    v_stack_m3A8 = 0;
    v_rbx = (unsigned int)((v_rbx) & (v_stack_m2DC));
loc_0047638E:
loc_00476390:
    a3 = 0;
    result = AuthzBasepSetAccessReasons((unsigned int)((unsigned int)(v_rbx)), (unsigned int)(0x900000ULL), a3, *(unsigned __int64 *)(a4 + 24));
    goto loc_0047732E;
loc_004763A1:
    v_rdi = *(unsigned __int64 *)(a3 + 8);
    if (*(unsigned __int64 *)(a3 + 8) == 0) {
        v_rdi = *(unsigned __int64 *)(a1 + 16);
        v_stack_m2A8 = v_rdi;
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r15 + 8) + 4)))) & (4)) != 0) goto loc_00476467;
    v_stack_m3A8 = v_stack_m298;
    result = SepFilterCheck(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8) + 8), v_stack_m308, v_rdi, *(unsigned __int64 *)(a4 + 24));
    a4 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = (unsigned int)(result);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a4 + 16))) < 0) goto loc_004764CB;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 16))))) & ((unsigned int)((unsigned int)(v_stack_m298))));
    result = (unsigned int)((result) - ((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 16)))));
    result = (unsigned int)(-(result));
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC0000022ULL))));
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = (unsigned int)(result);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a4 + 16))) >= 0) goto loc_00476467;
    a3 = 0;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 20))) | (*(unsigned int *)(v_r15 + 16)));
    v_stack_m390 = 0;
    v_stack_m398 = 0;
    v_stack_m3A0 = a2;
    a2 = 0;
    v_stack_m3A8 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8) + 8);
    result = SeLogAccessFailure(v_rdi, a2, a3, a4);
    v_rdi = 0;
    if (v_stack_m318 == 0) {
        a1 = a1;
        result = SeUnlockSubjectContext(a1, a2, a3, a4);
    }
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m298)) & ((unsigned int)(v_rsi)));
    v_stack_m3A8 = 0;
    goto loc_0047638E;
loc_00476467:
    v_rbx = (unsigned __int8)(((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r15 + 8) + 4)))) & ((unsigned __int8)(v_r13)));
    v_stack_m314 = (unsigned __int8)(v_rbx);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_r15 + 8) + 4)))) & (2)) == 0) goto loc_0047648E;
    if (((*(unsigned int *)(v_rdi + 200)) & (0x2000ULL)) == 0) goto loc_00476491;
    goto loc_00476494;
loc_0047648E:
loc_00476491:
loc_00476494:
    v_stack_m313 = 0;
    if ((*(unsigned __int8 *)(v_rip + 10053653)) != 0) goto loc_004764D1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 200)))) & (32)) != 0) goto loc_004764D1;
    if (*(unsigned __int64 *)(v_rdi + 216) == 0) goto loc_004764D1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi + 216) + 40)))) & (32)) == 0) goto loc_004764D1;
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 8)) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = (unsigned int)((unsigned int)(0xC0000022ULL));
loc_004764CB:
    goto loc_00476511;
loc_004764D1:
    v_stack_m2EC = 0;
    if (0 != 0) goto loc_004765A9;
    v_stack_m3A0 = v_stack_m290;
    v_stack_m3A8 = 0;
    result = SepMandatoryIntegrityCheck(*(unsigned __int64 *)(v_r15 + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8) + 8), 0, 0);
    v_r10 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = (unsigned int)(result);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a4 + 16))) >= 0) goto loc_00476524;
loc_00476511:
    if (v_stack_m318 != 0) goto loc_0047732E;
    result = SeUnlockSubjectContext(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8) + 8), 0, *(unsigned __int64 *)(a4 + 16));
    goto loc_0047732E;
loc_00476524:
    result = SepMandatoryToDiscretionary(v_stack_m290, (unsigned int)(*(unsigned int *)(v_r15 + 16)), 0, *(unsigned __int64 *)(a4 + 16));
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = (unsigned int)(result);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a4 + 16))) >= 0) goto loc_0047657F;
    if (((*(unsigned int *)(v_rdi + 200)) & (0x4000ULL)) == 0) goto loc_00476558;
    if (v_stack_m284 > 0x2000ULL) goto loc_00476558;
    v_stack_m2EC = (unsigned __int8)(v_r13);
    goto loc_004765A9;
loc_00476558:
    result = *(unsigned __int64 *)(a4 + 16);
    if (v_stack_m318 == 0) {
        a1 = a1;
        result = SeUnlockSubjectContext(a1, (unsigned int)(*(unsigned int *)(v_r15 + 16)), 0, *(unsigned __int64 *)(a4 + 16));
        v_r10 = 0;
    }
    a1 = (unsigned int)(~((unsigned int)(v_stack_m290)));
    v_stack_m3A8 = 0;
    a1 = (unsigned int)((a1) & ((unsigned int)(v_rsi)));
    goto loc_00476390;
loc_0047657F:
    if (((*(unsigned int *)(v_r15 + 16)) & (0x2000000ULL)) == 0) goto loc_004765A9;
    if (((*(unsigned int *)(v_rdi + 200)) & (0x4000ULL)) != 0) {
        result = v_stack_m2EC;
        result = (unsigned __int8)(result);
        if (v_stack_m284 <= 0x2000ULL) { result = (unsigned int)(v_r13); }
        v_stack_m2EC = (unsigned int)(result);
    }
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(a1, (unsigned int)(0x300000ULL), 0, *(unsigned __int64 *)(a4 + 16));
    a3 = 0;
    if ((unsigned int)(result) == 0) goto loc_0047661C;
    v_stack_m3A0 = v_stack_m2CC;
    a4 = ((unsigned __int8)(v_stack_m318) == 0) ? 1 : 0;
    v_stack_m3A8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 16)));
    result = SepMandatoryAccessCheck(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8) + 8), a1, a3, a4);
    a3 = 0;
    if (sign_flag) goto loc_004765F4;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 16))) & (v_stack_m2CC));
    if ((((unsigned int)(result)) & (0xFDFFFFFFULL)) == 0) goto loc_00476619;
loc_004765F4:
    if ((unsigned __int8)(v_stack_m318) == 0) {
        a1 = a1;
        result = SeUnlockSubjectContext(a1, a1, a3, a4);
        a3 = 0;
    }
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 8)) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = 0xC00001C0ULL;
    goto loc_0047732E;
loc_00476619:
loc_0047661C:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11068579)) == 0) goto loc_0047664F;
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8) + 8) + 2))) & (16)) == 0) goto loc_0047664F;
    if (((unsigned __int8)(v_cr8)) >= 2) goto loc_0047664F;
    if (!sign_flag) goto loc_00476659;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8) + 8) + 12))) != 0) goto loc_00476654;
    v_stack_m2C0 = 0;
loc_0047664F:
    goto loc_004766A2;
loc_00476654:
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8) + 8) + 12))) + (v_stack_m317);
    goto loc_0047665D;
loc_00476659:
loc_0047665D:
    v_stack_m2C0 = *(unsigned __int64 *)(v_stack_m317 + 24);
    if (*(unsigned __int64 *)(v_stack_m317 + 24) == 0) goto loc_0047664F;
    result = SepGetScopedPolicySid(*(unsigned __int64 *)(v_stack_m317 + 24), *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8) + 8) + 2), a3, a4);
    a3 = 0;
    if (result == 0) goto loc_0047669F;
    result = SepRmReferenceFindCap(result, v_stack_m2E8, a3, a4);
    a3 = 0;
    v_stack_m317 = (unsigned __int8)((unsigned __int8)(v_r13));
    a2 = v_stack_m2E8;
    if (sign_flag) { a2 = *(unsigned __int64 *)(v_rip + 11934295); }
    v_stack_m2E8 = a2;
    goto loc_004766A2;
loc_0047669F:
loc_004766A2:
    if ((unsigned __int8)(v_stack_m314) == 0) goto loc_004766BD;
    if (((*(unsigned int *)(v_r15 + 16)) & (0x2060000ULL)) != 0) goto loc_004766BD;
    if (0 != 0) goto loc_004766BD;
    v_stack_m316 = 0;
    goto loc_004766D6;
loc_004766BD:
    result = SepTokenIsOwner(0, *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8) + 8), a3, a4);
    v_stack_m316 = (unsigned __int8)(result);
    a3 = 0;
loc_004766D6:
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_00476794;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 16)))) & (0x2060000ULL)) == 0) goto loc_00476794;
    if (v_stack_m314 != 0) goto loc_0047673C;
    if ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8) + 8) + 2))) & (4)) != 0) goto loc_0047670F;
loc_0047670A:
    goto loc_00476725;
loc_0047670F:
    if (!sign_flag) goto loc_00476721;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8) + 8) + 16))) == 0) goto loc_0047670A;
    goto loc_00476725;
loc_00476721:
loc_00476725:
    a1 = 0;
    result = RtlpOwnerAcesPresent(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8) + 8) + 32), a3, a4);
    a3 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00476794;
loc_0047673C:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 16))))) & (0x2000000ULL));
    if (condition_is_equal) goto loc_00476750;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 20))) | ((unsigned int)((unsigned int)(0x60000ULL))));
    goto loc_00476754;
loc_00476750:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x60000ULL)))) & ((unsigned int)((unsigned int)(0x60000ULL))));
    result = (unsigned int)((result) | ((unsigned int)(v_rbx)));
loc_00476754:
    *(unsigned int *)(v_r15 + 20) = (unsigned int)(result);
    if ((unsigned int)(a1) == 0) goto loc_00476760;
    goto loc_00476762;
loc_00476760:
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x60000ULL)))) & ((unsigned int)((unsigned int)(0x60000ULL))));
loc_00476762:
    v_stack_m3A8 = 0;
    a3 = 0;
    result = AuthzBasepSetAccessReasons((unsigned int)((unsigned int)(v_rsi)), (unsigned int)(0x400000ULL), a3, *(unsigned __int64 *)(a4 + 24));
    result = (unsigned __int8)(-(v_stack_m317));
    a1 = (unsigned __int8)(((unsigned int)((unsigned int)(v_rsi))) & ((unsigned __int8)(v_stack_m316)));
    v_stack_m316 = (unsigned __int8)(a1);
    goto loc_00476798;
loc_00476794:
loc_00476798:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(a1, (unsigned int)(0x400000ULL), a3, *(unsigned __int64 *)(a4 + 24));
    a3 = 0;
    if ((unsigned int)(result) == 0) goto loc_004767F3;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 16))) != 0) goto loc_004767EF;
    if (v_stack_m317 != 0) goto loc_004767EF;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 200))) & (0x6000ULL));
    if (((unsigned int)(result)) == 0x2000ULL) goto loc_004767C8;
    if ((unsigned int)(v_rbx) != 0) goto loc_004767EF;
loc_004767C8:
    if (v_stack_m318 == 0) {
        a1 = a1;
        result = SeUnlockSubjectContext(a1, (unsigned int)(0x400000ULL), a3, *(unsigned __int64 *)(a4 + 24));
        a3 = 0;
    }
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 8)) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 20)));
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = 0;
    goto loc_00476222;
loc_004767EF:
    goto loc_0047680F;
loc_004767F3:
    if ((unsigned int)(*(unsigned __int64 *)(a4 + 8)) != 0) goto loc_0047680F;
    if (v_stack_m317 != 0) goto loc_0047680F;
    if (((*(unsigned int *)(v_rdi + 200)) & (0x2000ULL)) != 0) goto loc_004767C8;
    if ((unsigned int)(v_rbx) == 0) goto loc_004767C8;
loc_0047680F:
    v_stack_m328 = 0;
    v_stack_m330 = v_stack_m315;
    v_stack_m338 = v_stack_m308;
    v_stack_m340 = v_stack_m220;
    v_stack_m20C = 0;
    v_stack_m348 = a7;
    v_stack_m350 = (unsigned __int8)(v_stack_m316);
    v_rsi = 0;
    v_stack_m358 = 0;
    v_stack_m360 = *(unsigned __int64 *)(a4 + 24);
    v_stack_m368 = *(unsigned __int64 *)(a4 + 16);
    v_stack_m370 = *(unsigned __int64 *)(a4 + 32);
    v_stack_m378 = *(unsigned __int64 *)(a4 + 8);
    v_stack_m380 = a6;
    v_stack_m388 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 20)));
    v_stack_m390 = *(unsigned __int64 *)(v_r15 + 32);
    v_stack_m398 = 0;
    v_stack_m21C = v_xmm0;
    v_stack_m220 = (unsigned int)(v_rbx);
    v_stack_m3A0 = 0;
    v_stack_m3A8 = (unsigned int)((unsigned int)((unsigned int)(*(unsigned __int64 *)(a4 + 8))));
    a2 = 0;
    result = SepAccessCheckEx(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8) + 8), a2, *(unsigned __int64 *)(a1 + 16), *(unsigned __int64 *)(a1));
    v_stack_m310 = (unsigned __int8)(result);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11067891)) == 0) goto loc_00476FD8;
    v_stack_m2DC = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 16))));
    if (sign_flag) goto loc_00476FD8;
    if (v_stack_m317 == 0) goto loc_00476FD8;
    v_stack_m30C = 0;
    v_stack_m2FC = 0;
    v_stack_m2D8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8))));
    v_stack_m2F0 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8))));
    if (*(unsigned __int64 *)(a4 + 32) == 0) goto loc_00476985;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 32)) == 0) goto loc_00476985;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 32))))) == 0) goto loc_00476985;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 32))) + (12);
loc_0047692E:
    if ((*(unsigned int *)(a1 + 4)) >= 0) goto loc_00476978;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 - 4)))) != (*(unsigned int *)(v_rip + 11940292))) goto loc_0047694F;
    if ((*(unsigned int *)(a1)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11940288))))) goto loc_0047694F;
    goto loc_00476978;
loc_0047694F:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 - 4)))) != (*(unsigned int *)(v_rip + 11940323))) goto loc_00476961;
    if ((*(unsigned int *)(a1)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11940319))))) goto loc_00476973;
loc_00476961:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 - 4)))) != (*(unsigned int *)(v_rip + 11940289))) goto loc_00476978;
    if ((*(unsigned int *)(a1)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11940285))))) {
    }
    a1 = (a1) + (12);
    a3 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 32))))))) - (v_r13);
    if (condition_is_not_equal) goto loc_0047692E;
    v_stack_m2FC = 0;
loc_00476985:
    v_stack_m2D4 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8))));
    result = SepAdtAuditThisEventWithContext(130, (unsigned __int8)(v_r13), (unsigned __int8)(v_r13), a1);
    v_stack_m314 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_00476A18;
    a2 = ((unsigned int)(*(unsigned int *)(v_stack_m2E8 + 60))) << (3);
    result = ExAllocatePool2(64, a2, (unsigned int)(0x41536553ULL), a1);
    result = 0;
    if (0 != 0) goto loc_00476A03;
    if (v_stack_m318 == 0) {
        a1 = a1;
        result = SeUnlockSubjectContext(a1, a2, (unsigned int)(0x41536553ULL), a1);
    }
    result = SepRmDereferenceCap(v_stack_m2E8, a2, (unsigned int)(0x41536553ULL), a1);
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = 0xC0000017ULL;
    result = SepFreeResourceInfo(v_stack_m308, a2, (unsigned int)(0x41536553ULL), a1);
    goto loc_0047732E;
loc_00476A03:
    a2 = 0;
    a3 = ((unsigned int)(*(unsigned int *)(v_stack_m2E8 + 60))) << (3);
    result = memset(result, a2, a3, a1);
loc_00476A18:
    v_r10 = 0;
    v_stack_m2F4 = 0;
    v_stack_m300 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m2E8 + 60)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m2E8 + 60))) == 0) goto loc_00476E99;
loc_00476A2F:
    v_stack_m200 = v_xmm0;
    v_stack_m1F0 = v_xmm0;
    v_stack_m1E0 = v_xmm0;
    v_stack_m2B8 = *(unsigned __int64 *)(v_stack_m2E8 + 0 * 8 + 64);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2E8 + 0 * 8 + 64) + 24)) == 0) goto loc_00476BC6;
    result = 0;
    if (v_stack_m308 == 0) {
        a1 = v_stack_m2C0;
        a2 = v_stack_m308;
        result = AuthzBasepInitializeResourceClaimsFromSacl(a1, a2, *(unsigned __int64 *)(v_stack_m2E8 + 0 * 8 + 64), a1);
        a1 = v_stack_m30C;
        v_r10 = 0;
        a3 = v_stack_m2B8;
        a1 = (unsigned __int8)(a1);
        if (sign_flag) { a1 = (unsigned int)(v_r13); }
        v_stack_m30C = (unsigned int)(a1);
        a1 = v_stack_m308;
    }
    if (*(unsigned __int64 *)(v_rdi + 1096) == 0) goto loc_00476AB4;
    goto loc_00476ABD;
loc_00476AB4:
    v_r11 = 0;
loc_00476ABD:
    v_stack_m370 = v_stack_m2E0;
    v_stack_m378 = 0;
    v_stack_m380 = (unsigned __int8)(v_r13);
    v_stack_m388 = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 16)));
    v_stack_m390 = *(unsigned __int64 *)(a3 + 24);
    v_stack_m398 = 0;
    v_stack_m3A0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 1096) + 584);
    v_stack_m3A8 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 1096) + 584);
    result = AuthzBasepEvaluateAceCondition(0, *(unsigned __int64 *)(v_rdi + 776), a1, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 1096) + 584));
    v_stack_m300 = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(v_stack_m2E0))) == ((unsigned int)(v_r13))) goto loc_00476BC6;
    v_r10 = 0;
    if (sign_flag) goto loc_00477081;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 200)))) & (16)) == 0) goto loc_00476BB7;
    if (*(unsigned __int64 *)(v_rdi + 1096) == 0) goto loc_00476B54;
    goto loc_00476B5D;
loc_00476B54:
loc_00476B5D:
    v_stack_m370 = v_stack_m2E0;
    v_stack_m378 = (unsigned __int8)(v_r13);
    v_stack_m380 = (unsigned __int8)(v_r13);
    v_stack_m388 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m2B8 + 16)));
    v_stack_m390 = *(unsigned __int64 *)(v_stack_m2B8 + 24);
    v_stack_m398 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 1096) + 600);
    v_stack_m3A0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 1096) + 600);
    v_stack_m3A8 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 1096) + 600);
    result = AuthzBasepEvaluateAceCondition(0, *(unsigned __int64 *)(v_rdi + 776), v_stack_m308, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 1096) + 600));
    v_r10 = 0;
    v_stack_m300 = (unsigned int)(result);
    if (sign_flag) goto loc_00477081;
loc_00476BB7:
    if (v_stack_m30C != 0) goto loc_00476BC6;
    if (((unsigned int)((unsigned int)(v_stack_m2E0))) != ((unsigned int)(v_r13))) goto loc_00476E7F;
loc_00476BC6:
    result = SepBuildCapeSecurityDescriptor(v_stack_m270, *(unsigned __int64 *)(v_stack_m2B8 + 32), v_stack_m2C0, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 1096) + 600));
    a2 = 0;
    if (sign_flag) goto loc_004770F0;
    if ((((unsigned __int8)(v_r13)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m2B8 + 48))))) == 0) goto loc_00476C05;
    if (!(condition_is_below)) {
        a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 16))) | (*(unsigned int *)(v_r15 + 20)));
    }
    goto loc_00476C09;
loc_00476C05:
loc_00476C09:
    v_stack_m328 = 0;
    v_stack_m330 = v_stack_m315;
    v_stack_m338 = v_stack_m308;
    v_stack_m340 = v_stack_m220;
    v_stack_m348 = a7;
    v_stack_m350 = (unsigned __int8)(v_stack_m316);
    v_stack_m358 = 0;
    v_stack_m360 = v_stack_mC8;
    v_stack_m368 = v_stack_m2B0;
    v_stack_m370 = 0;
    v_stack_m378 = v_stack_m2F8;
    v_stack_m380 = a6;
    v_stack_m388 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 20)));
    v_stack_m390 = *(unsigned __int64 *)(v_r15 + 32);
    v_stack_m398 = (unsigned int)(v_r13);
    v_stack_m3A0 = v_stack_m200;
    v_stack_m3A8 = (unsigned int)(a1);
    v_stack_m200 = v_xmm0;
    v_stack_m1F0 = v_xmm0;
    v_stack_m1E0 = v_xmm0;
    result = SepAccessCheckEx(v_stack_m270, a2, *(unsigned __int64 *)(a1 + 16), *(unsigned __int64 *)(a1));
    v_r10 = 0;
    v_r11 = (unsigned int)(((unsigned int)(v_stack_m1E4)) | ((unsigned int)((unsigned int)(v_stack_m2FC))));
    v_stack_m310 = (unsigned __int8)(result);
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 20))) | (*(unsigned int *)(*(unsigned __int64 *)(a4 + 8))));
    v_rsi = (unsigned int)((v_rsi) & (v_stack_m2F8));
    v_stack_m2F8 = (unsigned int)(v_rsi);
    result = *(unsigned __int64 *)(a4 + 8);
    if (v_stack_m316 != 0) {
        result = (unsigned int)(v_rsi);
        result = (unsigned int)((result) & (0x60000ULL));
        v_r11 = (unsigned int)((v_r11) | ((unsigned int)(result)));
    }
    result = (unsigned int)(~((unsigned int)(v_stack_m1E0)));
    v_r11 = (unsigned int)((v_r11) & ((unsigned int)(result)));
    result = (unsigned int)(v_stack_m2B0);
    if (condition_is_equal) { result = (unsigned int)((unsigned int)(0xC0000022ULL)); }
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r11))) ^ ((unsigned int)((unsigned int)(v_stack_m2D4))));
    v_stack_m2DC = (unsigned int)(result);
    a1 = (unsigned int)((a1) & ((unsigned int)((unsigned int)(v_stack_m2D4))));
    v_rsi = (unsigned int)(v_stack_m2D4);
    if (!(condition_is_equal)) {
        a4 = v_stack_m1C8;
        v_stack_m3A8 = 0;
        a2 = 0x50000ULL;
        result = AuthzBasepSetAccessReasons(a1, a2, (unsigned int)(v_stack_m2F4), a4);
        a4 = v_stack_m2FC;
        v_rsi = (unsigned int)(((unsigned int)(v_stack_m2D4)) & ((unsigned int)(v_r11)));
        v_stack_m2D4 = (unsigned int)(v_rsi);
        v_r10 = 0;
    }
    if ((unsigned __int8)(v_stack_m314) == 0) goto loc_00477078;
    if (*(unsigned __int64 *)(v_stack_m2B8 + 40) == 0) goto loc_00477055;
    result = SepBuildCapeSecurityDescriptor(v_stack_m248, *(unsigned __int64 *)(v_stack_m2B8 + 40), v_stack_m2C0, a4);
    a4 = 0;
    if (sign_flag) goto loc_004770AA;
    if (((*(unsigned int *)(v_stack_m2B8 + 48)) & (256)) == 0) goto loc_00476D9F;
    if (!(condition_is_below)) {
        a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 16))) | (*(unsigned int *)(v_r15 + 20)));
    }
    goto loc_00476DA3;
loc_00476D9F:
loc_00476DA3:
    v_stack_m328 = 0;
    v_stack_m330 = v_stack_m30F;
    v_stack_m338 = v_stack_m308;
    v_stack_m340 = v_stack_m220;
    v_stack_m348 = a7;
    v_stack_m350 = (unsigned __int8)(v_stack_m316);
    v_stack_m358 = 0;
    v_stack_m360 = v_stack_mC8;
    v_stack_m368 = v_stack_m2A0;
    v_stack_m370 = 0;
    v_stack_m378 = v_stack_m2D0;
    v_stack_m380 = a6;
    a2 = 0;
    v_stack_m388 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 20)));
    v_stack_m390 = *(unsigned __int64 *)(v_r15 + 32);
    v_stack_m398 = 0;
    v_stack_m3A0 = 0;
    v_stack_m3A8 = (unsigned int)(a1);
    v_stack_m200 = v_xmm0;
    v_stack_m1F0 = v_xmm0;
    v_stack_m1E0 = v_xmm0;
    result = SepAccessCheckEx(v_stack_m248, a2, *(unsigned __int64 *)(a1 + 16), *(unsigned __int64 *)(a1));
    *(unsigned __int8 *)(result + (unsigned int)(v_stack_m2F4) * 8 + 4) = (unsigned __int8)(v_r13);
    result = (unsigned int)(((unsigned int)(v_stack_m2FC)) | (v_stack_m2D0));
    *(unsigned int *)(result + (unsigned int)(v_stack_m2F4) * 8) = (unsigned int)(result);
    a2 = (unsigned int)(((unsigned int)(v_stack_m2F0)) & (v_stack_m2D0));
    v_stack_m2F0 = a2;
    v_r10 = 0;
loc_00476E7F:
loc_00476E82:
    result = (unsigned int)(((unsigned int)(v_stack_m2F4)) + ((unsigned int)(v_r13)));
    v_stack_m2F4 = (unsigned int)(result);
    v_stack_m300 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m2E8 + 60)));
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m2E8 + 60))))) goto loc_00476A2F;
loc_00476E99:
    v_rsi = 0;
    if ((unsigned __int8)(v_stack_m314) == 0) goto loc_00476F82;
    if (((unsigned int)((unsigned int)(v_stack_m2F0))) == ((unsigned int)((unsigned int)(v_stack_m2D8)))) goto loc_00476F82;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m2F0)))) ^ ((unsigned int)((unsigned int)(v_stack_m2D8))));
    v_rsi = (unsigned int)((v_rsi) & ((unsigned int)((unsigned int)(v_stack_m2F0))));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & ((unsigned int)((unsigned int)(v_stack_m2D8))));
    a2 = 0;
    v_stack_m30C = (unsigned int)(result);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m2E8 + 60))) == 0) goto loc_00476F80;
    v_r15 = 0;
loc_00476ED4:
    if ((unsigned int)(v_rsi) != 0) goto loc_00476EE0;
    if ((unsigned int)(result) == 0) goto loc_00476F74;
loc_00476EE0:
    if ((*(unsigned __int8 *)(result + 4)) == 0) goto loc_00476F65;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result))))) ^ ((unsigned int)(result)));
    a1 = (unsigned int)((a1) & ((unsigned int)(result)));
    if (!(condition_is_equal)) {
        a3 = 0;
        v_stack_m3A8 = 0;
        a3 = (unsigned int)((a3) << (24));
        a4 = v_stack_m148;
        a2 = 0x80000000ULL;
        result = AuthzBasepSetAccessReasons(a1, a2, a3, a4);
        result = v_stack_m30C;
    }
    a1 = (unsigned int)(~(a1));
    result = (unsigned int)((result) & ((unsigned int)(a1)));
    v_stack_m30C = (unsigned int)(result);
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(result))) & ((unsigned int)(v_rsi)));
    if (!(condition_is_equal)) {
        a3 = 0;
        v_stack_m3A8 = 0;
        a3 = (unsigned int)((a3) << (24));
        a4 = v_stack_m148;
        a2 = 0x80000000ULL;
        a1 = (unsigned int)(v_r11);
        result = AuthzBasepSetAccessReasons(a1, a2, a3, a4);
    }
    v_r11 = (unsigned int)(~(v_r11));
    v_rsi = (unsigned int)((v_rsi) & ((unsigned int)(v_r11)));
    result = AuthzBasepMergeAccessReasons(v_stack_m1C8, v_stack_m148, (unsigned int)(0xFF000000ULL), a4);
loc_00476F65:
    v_rdi = (unsigned int)((0) + ((unsigned int)(v_r13)));
    v_r12 = (result) + (8);
    if (((unsigned int)(v_rdi)) < ((unsigned int)((unsigned int)(v_stack_m300)))) goto loc_00476ED4;
loc_00476F74:
loc_00476F80:
    v_rsi = 0;
loc_00476F82:
    result = (unsigned int)(v_stack_m30C);
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0xFF000000ULL), a4);
    }
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = (unsigned int)((unsigned int)(v_stack_m2DC));
    if ((*(unsigned int *)(*(unsigned __int64 *)(a4 + 16))) < 0) {
        v_stack_m315 = 0;
    }
    a3 = 0;
    result = AuthzBasepMergeAccessReasons(*(unsigned __int64 *)(a4 + 24), v_stack_m1C8, a3, a4);
    result = AuthzBasepMergeAccessReasons(*(unsigned __int64 *)(a4 + 24), v_stack_m1C8, (unsigned int)(0xFF000000ULL), a4);
loc_00476FD8:
    if (v_stack_m313 != 0) goto loc_004770F5;
    if (v_stack_m313 >= 0) goto loc_004770F5;
    if (v_stack_m2EC == 0) goto loc_0047702C;
    if (v_stack_m20A != 0) goto loc_00477175;
    if (v_stack_m20B != 0) goto loc_00477175;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m2A8 + 200))) & ((unsigned int)((unsigned int)(0x3000000ULL))));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0x3000000ULL)))) goto loc_00477175;
loc_0047702C:
    v_stack_m3A0 = 0;
    v_stack_m3A8 = v_stack_m315;
    result = SepConstrainByMandatory(v_stack_m290, (unsigned int)(*(unsigned int *)(v_stack_m280 + 16)), *(unsigned __int64 *)(a4 + 8), *(unsigned __int64 *)(a4 + 16));
    a1 = (unsigned int)(~((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))));
    a1 = (unsigned int)((a1) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8))))));
    goto loc_0047715F;
loc_00477055:
    *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8))) + (unsigned int)((unsigned int)(*(unsigned __int64 *)(a4 + 8))) * 8 + 4) = (unsigned __int8)(v_r13);
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(a4 + 16)))) | (v_stack_m2F8));
    *(unsigned int *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8))) + (unsigned int)((unsigned int)(*(unsigned __int64 *)(a4 + 8))) * 8) = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)(v_stack_m2F0)) & (v_stack_m2F8));
    v_stack_m2F0 = (unsigned int)(result);
    goto loc_00476E7F;
loc_00477078:
    goto loc_00476E82;
loc_00477081:
    if (v_stack_m318 == 0) {
        a1 = v_stack_m278;
        result = SeUnlockSubjectContext(a1, *(unsigned __int64 *)(a4 + 8), *(unsigned __int64 *)(a4 + 8), *(unsigned __int64 *)(a4 + 16));
    }
    result = SepRmDereferenceCap(v_stack_m2E8, *(unsigned __int64 *)(a4 + 8), *(unsigned __int64 *)(a4 + 8), *(unsigned __int64 *)(a4 + 16));
    v_rdi = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 8)) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = (unsigned int)((unsigned int)(v_stack_m300));
    goto loc_004770CF;
loc_004770AA:
loc_004770AE:
    result = *(unsigned __int64 *)(a4 + 16);
    if (v_stack_m318 == ((unsigned __int8)(*(unsigned __int64 *)(a4 + 16)))) {
        a1 = v_stack_m278;
        result = SeUnlockSubjectContext(a1, *(unsigned __int64 *)(a4 + 8), *(unsigned __int64 *)(a4 + 8), *(unsigned __int64 *)(a4 + 16));
    }
    result = SepRmDereferenceCap(v_stack_m2E8, *(unsigned __int64 *)(a4 + 8), *(unsigned __int64 *)(a4 + 8), *(unsigned __int64 *)(a4 + 16));
    v_rdi = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 8)) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = (unsigned int)(v_stack_m2E8);
loc_004770CF:
    result = SepFreeResourceInfo(v_stack_m308, *(unsigned __int64 *)(a4 + 8), *(unsigned __int64 *)(a4 + 8), *(unsigned __int64 *)(a4 + 16));
    if ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8))) == 0) goto loc_0047732E;
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8))), a2, *(unsigned __int64 *)(a4 + 8), *(unsigned __int64 *)(a4 + 16));
    goto loc_0047732E;
loc_004770F0:
    goto loc_004770AE;
loc_004770F5:
    if (v_stack_m2EC == ((unsigned __int8)(v_stack_m2E8))) goto loc_00477175;
    if (v_stack_m20A != ((unsigned __int8)(v_stack_m2E8))) goto loc_00477175;
    if (v_stack_m20B != ((unsigned __int8)(v_stack_m2E8))) goto loc_00477175;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 200))) & ((unsigned int)((unsigned int)(0x3000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x3000000ULL)))) goto loc_00477143;
    if (v_stack_m214 != ((unsigned int)(v_stack_m2E8))) goto loc_00477143;
    v_stack_m209 = (unsigned __int8)(v_r13);
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = (unsigned int)(v_stack_m2E8);
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 8)) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m280 + 16)));
    v_stack_m315 = (unsigned __int8)(v_r13);
    goto loc_00477175;
loc_00477143:
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 16)) = 0xC0000022ULL;
    *(unsigned int *)(*(unsigned __int64 *)(a4 + 8)) = (unsigned int)(v_stack_m2E8);
    v_stack_m315 = (unsigned __int8)(v_stack_m2E8);
    a1 = (unsigned int)(~((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))));
loc_0047715F:
    a3 = 0;
    v_stack_m3A8 = (unsigned __int8)(v_stack_m2E8);
    result = AuthzBasepSetAccessReasons(a1, (unsigned int)(0x300000ULL), a3, *(unsigned __int64 *)(a4 + 24));
loc_00477175:
    if (condition_is_above_or_equal) goto loc_0047722D;
    v_stack_m398 = v_stack_m312;
    v_stack_m3A0 = (unsigned int)(v_stack_m2E8);
    v_stack_m3A8 = v_stack_m315;
    result = SepConstrainByConstraintMask((unsigned int)(v_stack_m2C8), (unsigned int)(*(unsigned int *)(v_stack_m280 + 16)), *(unsigned __int64 *)(a4 + 8), *(unsigned __int64 *)(a4 + 16));
    a3 = 0;
    v_stack_m3A8 = (unsigned __int8)(v_stack_m2E8);
    a1 = (unsigned int)(~((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))));
    a1 = (unsigned int)((a1) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8))))));
    result = AuthzBasepSetAccessReasons(a1, (unsigned int)(0x900000ULL), a3, *(unsigned __int64 *)(a4 + 24));
    v_stack_m398 = v_stack_m311;
    v_stack_m3A0 = (unsigned int)(v_stack_m2E8);
    v_stack_m3A8 = v_stack_m315;
    result = SepConstrainByConstraintMask((unsigned int)(v_stack_m298), (unsigned int)(*(unsigned int *)(v_stack_m280 + 16)), *(unsigned __int64 *)(a4 + 8), *(unsigned __int64 *)(a4 + 16));
    a3 = 0;
    v_stack_m3A8 = (unsigned __int8)(v_stack_m2E8);
    a1 = (unsigned int)(~((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)))));
    a1 = (unsigned int)((a1) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8))))));
    result = AuthzBasepSetAccessReasons(a1, (unsigned int)(0xA00000ULL), a3, *(unsigned __int64 *)(a4 + 24));
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(a1, (unsigned int)(0xA00000ULL), a3, *(unsigned __int64 *)(a4 + 24));
    if ((unsigned int)(result) != 0) {
        a1 = *(unsigned __int64 *)(a4 + 8);
        result = v_stack_m2CC;
        result = (unsigned int)(~(result));
    }
    if (0 == 0) goto loc_004772EA;
    if (v_stack_m312 != ((unsigned __int8)(v_stack_m2E8))) goto loc_00477269;
    if (v_stack_m311 != ((unsigned __int8)(v_stack_m2E8))) goto loc_00477269;
    if ((unsigned int)((unsigned int)(v_stack_m214)) != 0) goto loc_004772BC;
    if (((*(unsigned int *)(v_rdi + 200)) & (0x4000ULL)) == 0) goto loc_004772BC;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a4 + 16))) < ((unsigned int)(v_stack_m2E8))) goto loc_00477269;
    result = *(unsigned __int64 *)(a4 + 16);
    v_rbx = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8)));
    v_rsi = v_stack_m2E8;
    if (v_stack_m209 != ((unsigned __int8)(v_stack_m2E8))) {
        result = *(unsigned __int64 *)(a4 + 16);
        a1 = v_stack_m278;
        v_rdi = *(unsigned int *)(v_stack_m280 + 20);
        v_rdi = (unsigned int)((v_rdi) | (*(unsigned int *)(v_stack_m280 + 16)));
        v_rbx = *(unsigned __int64 *)(v_stack_m280 + 8);
        v_rsi = *(unsigned int *)(result);
        v_rsi = (unsigned int)((v_rsi) >> (31));
        v_rsi = (unsigned __int8)((v_rsi) ^ ((unsigned __int8)(v_r13)));
        result = SepLocateTokenTrustLevel(a1, (unsigned int)(0xA00000ULL), a3, *(unsigned __int64 *)(a4 + 24));
        v_stack_m390 = 0;
        a4 = result;
        result = *(unsigned __int64 *)(v_rbx + 8);
        a3 = 0;
        v_stack_m398 = (unsigned __int8)(v_rsi);
        a2 = 0;
        v_stack_m3A0 = (unsigned int)(v_rdi);
        v_rdi = v_stack_m2A8;
        a1 = v_rdi;
        v_stack_m3A8 = result;
        result = SeLogAccessFailure(a1, a2, a3, a4);
        a1 = v_stack_m214;
        v_rsi = 0;
    }
    if ((*(unsigned int *)(*(unsigned __int64 *)(a4 + 16))) >= 0) goto loc_004772EA;
    if ((unsigned int)(a1) != 0) goto loc_004772EA;
    if (((*(unsigned int *)(v_rdi + 200)) & (0x4000ULL)) == 0) goto loc_004772EA;
    result = SepLpacCausedAccessFailure(v_stack_m220, (unsigned int)(*(unsigned int *)(v_stack_m280 + 16)), a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = SepLogLpacAccessFailure(v_stack_m220, (unsigned int)(*(unsigned int *)(v_stack_m280 + 16)), a3, a4);
    }
    if (v_stack_m317 != 0) {
        a1 = v_stack_m2E8;
        result = SepRmDereferenceCap(a1, (unsigned int)(*(unsigned int *)(v_stack_m280 + 16)), a3, a4);
    }
    if (v_stack_m318 == 0) {
        a1 = v_stack_m278;
        result = SeUnlockSubjectContext(a1, (unsigned int)(*(unsigned int *)(v_stack_m280 + 16)), a3, a4);
    }
    result = SepFreeResourceInfo(v_stack_m308, (unsigned int)(*(unsigned int *)(v_stack_m280 + 16)), a3, a4);
    if (v_stack_m310 == 0) goto loc_00477320;
    if (v_stack_m315 != 0) goto loc_00476222;
loc_00477320:
    goto loc_00476222;
loc_00477328:
    *(unsigned int *)(v_stack_m308) = 0xC000000DULL;
loc_0047732E:
    result = 0;
loc_00477330:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(*(unsigned int *)(v_stack_m280 + 16)), a3, a4);
    v_rsp = (v_rsp) + (912);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SepCommonAccessCheckEx(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint8_t Arg6, uint8_t Arg7)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m148;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1E0;
    uint32_t v_stack_m1E4;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m200;
    uint8_t v_stack_m209;
    uint8_t v_stack_m20A;
    uint8_t v_stack_m20B;
    uint64_t v_stack_m20C;
    uint32_t v_stack_m214;
    uint64_t v_stack_m21C;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint64_t v_stack_m238;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m260;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m280;
    uint32_t v_stack_m284;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint32_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint32_t v_stack_m2B0;
    uint64_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint32_t v_stack_m2C8;
    uint32_t v_stack_m2CC;
    uint32_t v_stack_m2D0;
    uint32_t v_stack_m2D4;
    uint32_t v_stack_m2D8;
    uint32_t v_stack_m2DC;
    uint32_t v_stack_m2E0;
    uint64_t v_stack_m2E8;
    uint8_t v_stack_m2EC;
    uint32_t v_stack_m2F0;
    uint32_t v_stack_m2F4;
    uint32_t v_stack_m2F8;
    uint32_t v_stack_m2FC;
    uint32_t v_stack_m300;
    uint64_t v_stack_m308;
    uint8_t v_stack_m30C;
    uint8_t v_stack_m30F;
    uint8_t v_stack_m310;
    uint8_t v_stack_m311;
    uint8_t v_stack_m312;
    uint8_t v_stack_m313;
    uint8_t v_stack_m314;
    uint8_t v_stack_m315;
    uint8_t v_stack_m316;
    uint8_t v_stack_m317;
    uint8_t v_stack_m318;
    uint64_t v_stack_m328;
    uint64_t v_stack_m330;
    uint64_t v_stack_m338;
    uint64_t v_stack_m340;
    uint8_t v_stack_m348;
    uint8_t v_stack_m350;
    uint8_t v_stack_m358;
    uint64_t v_stack_m360;
    uint64_t v_stack_m368;
    uint64_t v_stack_m370;
    uint64_t v_stack_m378;
    uint8_t v_stack_m380;
    uint32_t v_stack_m388;
    uint8_t v_stack_m390;
    uint64_t v_stack_m398;
    uint8_t v_stack_m3A0;
    uint8_t v_stack_m3A8;
    uint64_t v_stack_m48;
    uint64_t v_stack_mC8;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (912);
    result = (*(uint64_t *)(v_rip + 0x9946EE)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m278 = Arg1;
    v_stack_m280 = Arg3;
    v_stack_m318 = (uint8_t)(Arg2);
    Arg1 = 0;
    result = 0;
    v_stack_m315 = 0;
    v_stack_m30F = 0;
    v_stack_m20C = 0;
    v_stack_m2C0 = 0;
    v_stack_m2D0 = 0;
    Arg2 = 0;
    v_stack_m2A0 = 0;
    v_stack_m2E8 = 0;
    v_stack_m317 = 0;
    v_stack_m308 = 0;
    v_stack_m2E0 = 0;
    v_stack_m290 = v_xmm0;
    v_stack_m250 = 0;
    v_stack_m21C = v_xmm1;
    v_stack_m228 = 0;
    v_stack_m270 = v_xmm0;
    v_stack_m260 = v_xmm0;
    v_stack_m248 = v_xmm1;
    v_stack_m238 = v_xmm1;
    result = memset(v_stack_m1C8, Arg2, 128, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m148, Arg2, 128, Arg4);
    Arg2 = 0;
    result = memset(v_stack_mC8, Arg2, 128, Arg4);
    local_rdi = 0;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    v_stack_m312 = 0;
    v_stack_m311 = 0;
    v_stack_m2CC = 0;
    v_stack_m2C8 = (uint32_t)(result);
    v_stack_m298 = (uint32_t)(result);
    if (Arg4 == 0) goto loc_0047732E;
    if ((*(uint32_t *)(Arg4)) != 40) goto loc_0047732E;
    if (*(uint64_t *)(Arg4 + 0x10) == 0) goto loc_0047732E;
    if (0 == 0) goto loc_00477328;
    if (Arg3 == 0) goto loc_00477328;
    if ((*(uint32_t *)(Arg3)) != 56) goto loc_00477328;
    if (*(uint64_t *)(Arg4 + 0x8) == 0) goto loc_00477328;
    if (*(uint64_t *)(Arg3 + 0x8) == 0) goto loc_00476178;
    if ((*(uint32_t *)(*(uint64_t *)(Arg3 + 0x8))) != 16) goto loc_00477328;
    if (((*(uint32_t *)(*(uint64_t *)(Arg3 + 0x8) + 0x4)) & (0xFFFFFFF8ULL)) != 0) goto loc_00477328;
loc_00476178:
    if (Arg5 == 0) goto loc_0047618D;
    if ((*(uint32_t *)(Arg5)) != 96) goto loc_00477328;
loc_0047618D:
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)) = 0;
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = (uint32_t)((uint32_t)(0xC0000022ULL));
    v_stack_m2F8 = 0;
    v_stack_m2B0 = (uint32_t)((uint32_t)(0xC0000022ULL));
    if (*(uint64_t *)(Arg4 + 0x20) != 0) {
        *(uint64_t *)(*(uint64_t *)(Arg4 + 0x20)) = 0;
    }
    local_rsi = (uint32_t)(~((uint32_t)(*(uint32_t *)(Arg3 + 0x14))));
    local_rsi = (uint32_t)((local_rsi) & (*(uint32_t *)(Arg3 + 0x10)));
    local_rsi = (uint32_t)((local_rsi) & ((uint32_t)((uint32_t)(0xFDFFFFFFULL))));
    v_stack_m3A8 = 1;
    v_stack_m2DC = (uint32_t)(local_rsi);
    Arg3 = 0;
    Arg2 = 0;
    result = AuthzBasepSetAccessReasons((uint32_t)((uint32_t)(local_rsi)), Arg2, Arg3, *(uint64_t *)(Arg4 + 0x18));
    if (Arg6 != 0) goto loc_0047622A;
    if (Arg6 >= 0) goto loc_00476216;
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3 + 0x20) + 0xC)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3 + 0x10))) & ((uint32_t)((uint32_t)(0xFDFFFFFFULL))));
    goto loc_0047621C;
loc_00476216:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3 + 0x14))) | (*(uint32_t *)(Arg3 + 0x14)));
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)) = (uint32_t)(result);
loc_0047621C:
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = 0;
loc_00476222:
    goto loc_00477330;
loc_0047622A:
    if (*(uint64_t *)(Arg3 + 0x8) == 0) goto loc_00476264;
    if ((*(uint64_t *)(*(uint64_t *)(Arg3 + 0x8) + 0x8)) == 0) goto loc_00476264;
    if ((*(uint64_t *)(Arg1)) == 0) goto loc_00476256;
    if ((*(uint32_t *)(Arg1 + 0x8)) >= 2) goto loc_00476256;
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = 0xC00000A5ULL;
    goto loc_0047732E;
loc_00476256:
    if ((*(uint32_t *)(Arg3 + 0x10)) != 0) goto loc_0047628D;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x14))) != 0) goto loc_00476273;
loc_00476264:
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = 0xC0000022ULL;
    goto loc_0047732E;
loc_00476273:
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x14)));
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = 0;
    if (*(uint64_t *)(Arg4 + 0x20) == 0) goto loc_00476222;
    *(uint64_t *)(*(uint64_t *)(Arg4 + 0x20)) = 0;
    goto loc_00476222;
loc_0047628D:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)))) == 1) goto loc_004762AB;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x4)))) == (*(uint32_t *)(Arg3 + 0x28))) goto loc_004762AB;
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = 0xC000000DULL;
    goto loc_0047732E;
loc_004762AB:
    result = *(uint64_t *)(Arg4 + 0x10);
    if ((uint8_t)((uint8_t)(Arg2)) == 0) {
        Arg1 = 0;
        result = SeLockSubjectContext(Arg1, Arg2, Arg3, *(uint64_t *)(Arg4 + 0x18));
    }
    v_stack_m398 = v_stack_m2C8;
    Arg4 = 0;
    v_stack_m3A0 = 0;
    v_stack_m3A8 = 0;
    result = SepTrustLevelCheck(Arg1, *(uint64_t *)(*(uint64_t *)(Arg3 + 0x8) + 0x8), Arg1, Arg4);
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = (uint32_t)(result);
    if ((*(uint32_t *)(*(uint64_t *)(Arg4 + 0x10))) >= 0) goto loc_004762F2;
    goto loc_00476511;
loc_004762F2:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x10))))) & ((uint32_t)((uint32_t)(v_stack_m2C8))));
    result = (uint32_t)((result) - ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x10)))));
    result = (uint32_t)(-(result));
    Arg4 = 0;
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000022ULL))));
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = (uint32_t)(result);
    v_stack_m2A8 = *(uint64_t *)(Arg1);
    if ((*(uint32_t *)(*(uint64_t *)(Arg4 + 0x10))) >= 0) goto loc_004763A1;
    local_r13 = *(uint64_t *)(Arg1);
    if (*(uint64_t *)(Arg1) == 0) {
        local_r13 = *(uint64_t *)(Arg1 + 0x10);
    }
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3 + 0x14))) | (*(uint32_t *)(Arg3 + 0x10)));
    result = SepLocateTokenTrustLevel(Arg1, *(uint64_t *)(Arg4 + 0x10), Arg1, Arg4);
    local_r15 = 0;
    Arg3 = 0;
    v_stack_m390 = 0;
    Arg2 = 0;
    v_stack_m398 = 0;
    v_stack_m3A0 = (uint32_t)(local_rsi);
    v_stack_m3A8 = *(uint64_t *)(*(uint64_t *)(Arg3 + 0x8) + 0x8);
    result = SeLogAccessFailure(local_r13, Arg2, Arg3, result);
    if (v_stack_m318 == 0) {
        Arg1 = Arg1;
        result = SeUnlockSubjectContext(Arg1, Arg2, Arg3, result);
    }
    local_rbx = (uint32_t)(~((uint32_t)(v_stack_m2C8)));
    v_stack_m3A8 = 0;
    local_rbx = (uint32_t)((local_rbx) & (v_stack_m2DC));
loc_0047638E:
loc_00476390:
    Arg3 = 0;
    result = AuthzBasepSetAccessReasons((uint32_t)((uint32_t)(local_rbx)), (uint32_t)(0x900000ULL), Arg3, *(uint64_t *)(Arg4 + 0x18));
    goto loc_0047732E;
loc_004763A1:
    local_rdi = *(uint64_t *)(Arg3 + 0x8);
    if (*(uint64_t *)(Arg3 + 0x8) == 0) {
        local_rdi = *(uint64_t *)(Arg1 + 0x10);
        v_stack_m2A8 = local_rdi;
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x4)))) & (4)) != 0) goto loc_00476467;
    v_stack_m3A8 = v_stack_m298;
    result = SepFilterCheck(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x8), v_stack_m308, local_rdi, *(uint64_t *)(Arg4 + 0x18));
    Arg4 = 0;
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = (uint32_t)(result);
    if ((*(uint32_t *)(*(uint64_t *)(Arg4 + 0x10))) < 0) goto loc_004764CB;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x10))))) & ((uint32_t)((uint32_t)(v_stack_m298))));
    result = (uint32_t)((result) - ((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x10)))));
    result = (uint32_t)(-(result));
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC0000022ULL))));
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = (uint32_t)(result);
    if ((*(uint32_t *)(*(uint64_t *)(Arg4 + 0x10))) >= 0) goto loc_00476467;
    Arg3 = 0;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x14))) | (*(uint32_t *)(local_r15 + 0x10)));
    v_stack_m390 = 0;
    v_stack_m398 = 0;
    v_stack_m3A0 = Arg2;
    Arg2 = 0;
    v_stack_m3A8 = *(uint64_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x8);
    result = SeLogAccessFailure(local_rdi, Arg2, Arg3, Arg4);
    local_rdi = 0;
    if (v_stack_m318 == 0) {
        Arg1 = Arg1;
        result = SeUnlockSubjectContext(Arg1, Arg2, Arg3, Arg4);
    }
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m298)) & ((uint32_t)(local_rsi)));
    v_stack_m3A8 = 0;
    goto loc_0047638E;
loc_00476467:
    local_rbx = (uint8_t)(((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x4)))) & ((uint8_t)(local_r13)));
    v_stack_m314 = (uint8_t)(local_rbx);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x4)))) & (2)) == 0) goto loc_0047648E;
    if (((*(uint32_t *)(local_rdi + 0xC8)) & (0x2000ULL)) == 0) goto loc_00476491;
    goto loc_00476494;
loc_0047648E:
loc_00476491:
loc_00476494:
    v_stack_m313 = 0;
    if ((*(uint8_t *)(v_rip + 0x996815)) != 0) goto loc_004764D1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0xC8)))) & (32)) != 0) goto loc_004764D1;
    if (*(uint64_t *)(local_rdi + 0xD8) == 0) goto loc_004764D1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi + 0xD8) + 0x28)))) & (32)) == 0) goto loc_004764D1;
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)) = 0;
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = (uint32_t)((uint32_t)(0xC0000022ULL));
loc_004764CB:
    goto loc_00476511;
loc_004764D1:
    v_stack_m2EC = 0;
    if (0 != 0) goto loc_004765A9;
    v_stack_m3A0 = v_stack_m290;
    v_stack_m3A8 = 0;
    result = SepMandatoryIntegrityCheck(*(uint64_t *)(local_r15 + 0x20), *(uint64_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x8), 0, 0);
    local_r10 = 0;
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = (uint32_t)(result);
    if ((*(uint32_t *)(*(uint64_t *)(Arg4 + 0x10))) >= 0) goto loc_00476524;
loc_00476511:
    if (v_stack_m318 != 0) goto loc_0047732E;
    result = SeUnlockSubjectContext(Arg1, *(uint64_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x8), 0, *(uint64_t *)(Arg4 + 0x10));
    goto loc_0047732E;
loc_00476524:
    result = SepMandatoryToDiscretionary(v_stack_m290, (uint32_t)(*(uint32_t *)(local_r15 + 0x10)), 0, *(uint64_t *)(Arg4 + 0x10));
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = (uint32_t)(result);
    if ((*(uint32_t *)(*(uint64_t *)(Arg4 + 0x10))) >= 0) goto loc_0047657F;
    if (((*(uint32_t *)(local_rdi + 0xC8)) & (0x4000ULL)) == 0) goto loc_00476558;
    if (v_stack_m284 > 0x2000ULL) goto loc_00476558;
    v_stack_m2EC = (uint8_t)(local_r13);
    goto loc_004765A9;
loc_00476558:
    result = *(uint64_t *)(Arg4 + 0x10);
    if (v_stack_m318 == 0) {
        Arg1 = Arg1;
        result = SeUnlockSubjectContext(Arg1, (uint32_t)(*(uint32_t *)(local_r15 + 0x10)), 0, *(uint64_t *)(Arg4 + 0x10));
        local_r10 = 0;
    }
    Arg1 = (uint32_t)(~((uint32_t)(v_stack_m290)));
    v_stack_m3A8 = 0;
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)(local_rsi)));
    goto loc_00476390;
loc_0047657F:
    if (((*(uint32_t *)(local_r15 + 0x10)) & (0x2000000ULL)) == 0) goto loc_004765A9;
    if (((*(uint32_t *)(local_rdi + 0xC8)) & (0x4000ULL)) != 0) {
        result = v_stack_m2EC;
        result = (uint8_t)(result);
        if (v_stack_m284 <= 0x2000ULL) { result = (uint32_t)(local_r13); }
        v_stack_m2EC = (uint32_t)(result);
    }
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(Arg1, (uint32_t)(0x300000ULL), 0, *(uint64_t *)(Arg4 + 0x10));
    Arg3 = 0;
    if ((uint32_t)(result) == 0) goto loc_0047661C;
    v_stack_m3A0 = v_stack_m2CC;
    Arg4 = ((uint8_t)(v_stack_m318) == 0) ? 1 : 0;
    v_stack_m3A8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x10)));
    result = SepMandatoryAccessCheck(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x8), Arg1, Arg3, Arg4);
    Arg3 = 0;
    if (sign_flag) goto loc_004765F4;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x10))) & (v_stack_m2CC));
    if ((((uint32_t)(result)) & (0xFDFFFFFFULL)) == 0) goto loc_00476619;
loc_004765F4:
    if ((uint8_t)(v_stack_m318) == 0) {
        Arg1 = Arg1;
        result = SeUnlockSubjectContext(Arg1, Arg1, Arg3, Arg4);
        Arg3 = 0;
    }
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)) = 0;
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = 0xC00001C0ULL;
    goto loc_0047732E;
loc_00476619:
loc_0047661C:
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xA8E4A3)) == 0) goto loc_0047664F;
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x8) + 0x2))) & (16)) == 0) goto loc_0047664F;
    if (((uint8_t)(v_cr8)) >= 2) goto loc_0047664F;
    if (!sign_flag) goto loc_00476659;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x8) + 0xC))) != 0) goto loc_00476654;
    v_stack_m2C0 = 0;
loc_0047664F:
    goto loc_004766A2;
loc_00476654:
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x8) + 0xC))) + (v_stack_m317);
    goto loc_0047665D;
loc_00476659:
loc_0047665D:
    v_stack_m2C0 = *(uint64_t *)(v_stack_m317 + 0x18);
    if (*(uint64_t *)(v_stack_m317 + 0x18) == 0) goto loc_0047664F;
    result = SepGetScopedPolicySid(*(uint64_t *)(v_stack_m317 + 0x18), *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x8) + 0x2), Arg3, Arg4);
    Arg3 = 0;
    if (result == 0) goto loc_0047669F;
    result = SepRmReferenceFindCap(result, v_stack_m2E8, Arg3, Arg4);
    Arg3 = 0;
    v_stack_m317 = (uint8_t)((uint8_t)(local_r13));
    Arg2 = v_stack_m2E8;
    if (sign_flag) { Arg2 = *(uint64_t *)(v_rip + 0xB61A57); }
    v_stack_m2E8 = Arg2;
    goto loc_004766A2;
loc_0047669F:
loc_004766A2:
    if ((uint8_t)(v_stack_m314) == 0) goto loc_004766BD;
    if (((*(uint32_t *)(local_r15 + 0x10)) & (0x2060000ULL)) != 0) goto loc_004766BD;
    if (0 != 0) goto loc_004766BD;
    v_stack_m316 = 0;
    goto loc_004766D6;
loc_004766BD:
    result = SepTokenIsOwner(0, *(uint64_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x8), Arg3, Arg4);
    v_stack_m316 = (uint8_t)(result);
    Arg3 = 0;
loc_004766D6:
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_00476794;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x10)))) & (0x2060000ULL)) == 0) goto loc_00476794;
    if (v_stack_m314 != 0) goto loc_0047673C;
    if ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x8) + 0x2))) & (4)) != 0) goto loc_0047670F;
loc_0047670A:
    goto loc_00476725;
loc_0047670F:
    if (!sign_flag) goto loc_00476721;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x8) + 0x10))) == 0) goto loc_0047670A;
    goto loc_00476725;
loc_00476721:
loc_00476725:
    Arg1 = 0;
    result = RtlpOwnerAcesPresent(Arg1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x8) + 0x20), Arg3, Arg4);
    Arg3 = 0;
    if ((uint8_t)(result) != 0) goto loc_00476794;
loc_0047673C:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x10))))) & (0x2000000ULL));
    if (condition_is_equal) goto loc_00476750;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x14))) | ((uint32_t)((uint32_t)(0x60000ULL))));
    goto loc_00476754;
loc_00476750:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x60000ULL)))) & ((uint32_t)((uint32_t)(0x60000ULL))));
    result = (uint32_t)((result) | ((uint32_t)(local_rbx)));
loc_00476754:
    *(uint32_t *)(local_r15 + 0x14) = (uint32_t)(result);
    if ((uint32_t)(Arg1) == 0) goto loc_00476760;
    goto loc_00476762;
loc_00476760:
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x60000ULL)))) & ((uint32_t)((uint32_t)(0x60000ULL))));
loc_00476762:
    v_stack_m3A8 = 0;
    Arg3 = 0;
    result = AuthzBasepSetAccessReasons((uint32_t)((uint32_t)(local_rsi)), (uint32_t)(0x400000ULL), Arg3, *(uint64_t *)(Arg4 + 0x18));
    result = (uint8_t)(-(v_stack_m317));
    Arg1 = (uint8_t)(((uint32_t)((uint32_t)(local_rsi))) & ((uint8_t)(v_stack_m316)));
    v_stack_m316 = (uint8_t)(Arg1);
    goto loc_00476798;
loc_00476794:
loc_00476798:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(Arg1, (uint32_t)(0x400000ULL), Arg3, *(uint64_t *)(Arg4 + 0x18));
    Arg3 = 0;
    if ((uint32_t)(result) == 0) goto loc_004767F3;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x10))) != 0) goto loc_004767EF;
    if (v_stack_m317 != 0) goto loc_004767EF;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0xC8))) & (0x6000ULL));
    if (((uint32_t)(result)) == 0x2000ULL) goto loc_004767C8;
    if ((uint32_t)(local_rbx) != 0) goto loc_004767EF;
loc_004767C8:
    if (v_stack_m318 == 0) {
        Arg1 = Arg1;
        result = SeUnlockSubjectContext(Arg1, (uint32_t)(0x400000ULL), Arg3, *(uint64_t *)(Arg4 + 0x18));
        Arg3 = 0;
    }
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x14)));
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = 0;
    goto loc_00476222;
loc_004767EF:
    goto loc_0047680F;
loc_004767F3:
    if ((uint32_t)(*(uint64_t *)(Arg4 + 0x8)) != 0) goto loc_0047680F;
    if (v_stack_m317 != 0) goto loc_0047680F;
    if (((*(uint32_t *)(local_rdi + 0xC8)) & (0x2000ULL)) != 0) goto loc_004767C8;
    if ((uint32_t)(local_rbx) == 0) goto loc_004767C8;
loc_0047680F:
    v_stack_m328 = 0;
    v_stack_m330 = v_stack_m315;
    v_stack_m338 = v_stack_m308;
    v_stack_m340 = v_stack_m220;
    v_stack_m20C = 0;
    v_stack_m348 = Arg7;
    v_stack_m350 = (uint8_t)(v_stack_m316);
    local_rsi = 0;
    v_stack_m358 = 0;
    v_stack_m360 = *(uint64_t *)(Arg4 + 0x18);
    v_stack_m368 = *(uint64_t *)(Arg4 + 0x10);
    v_stack_m370 = *(uint64_t *)(Arg4 + 0x20);
    v_stack_m378 = *(uint64_t *)(Arg4 + 0x8);
    v_stack_m380 = Arg6;
    v_stack_m388 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x14)));
    v_stack_m390 = *(uint64_t *)(local_r15 + 0x20);
    v_stack_m398 = 0;
    v_stack_m21C = v_xmm0;
    v_stack_m220 = (uint32_t)(local_rbx);
    v_stack_m3A0 = 0;
    v_stack_m3A8 = (uint32_t)((uint32_t)((uint32_t)(*(uint64_t *)(Arg4 + 0x8))));
    Arg2 = 0;
    result = SepAccessCheckEx(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x8) + 0x8), Arg2, *(uint64_t *)(Arg1 + 0x10), *(uint64_t *)(Arg1));
    v_stack_m310 = (uint8_t)(result);
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xA8E1F3)) == 0) goto loc_00476FD8;
    v_stack_m2DC = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x10))));
    if (sign_flag) goto loc_00476FD8;
    if (v_stack_m317 == 0) goto loc_00476FD8;
    v_stack_m30C = 0;
    v_stack_m2FC = 0;
    v_stack_m2D8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8))));
    v_stack_m2F0 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8))));
    if (*(uint64_t *)(Arg4 + 0x20) == 0) goto loc_00476985;
    if (*(uint64_t *)(*(uint64_t *)(Arg4 + 0x20)) == 0) goto loc_00476985;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg4 + 0x20))))) == 0) goto loc_00476985;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(Arg4 + 0x20))) + (12);
loc_0047692E:
    if ((*(uint32_t *)(Arg1 + 0x4)) >= 0) goto loc_00476978;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 - 0x4)))) != (*(uint32_t *)(v_rip + 0xB631C4))) goto loc_0047694F;
    if ((*(uint32_t *)(Arg1)) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB631C0))))) goto loc_0047694F;
    goto loc_00476978;
loc_0047694F:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 - 0x4)))) != (*(uint32_t *)(v_rip + 0xB631E3))) goto loc_00476961;
    if ((*(uint32_t *)(Arg1)) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB631DF))))) goto loc_00476973;
loc_00476961:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 - 0x4)))) != (*(uint32_t *)(v_rip + 0xB631C1))) goto loc_00476978;
    if ((*(uint32_t *)(Arg1)) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB631BD))))) {
    }
    Arg1 = (Arg1) + (12);
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg4 + 0x20))))))) - (local_r13);
    if (condition_is_not_equal) goto loc_0047692E;
    v_stack_m2FC = 0;
loc_00476985:
    v_stack_m2D4 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8))));
    result = SepAdtAuditThisEventWithContext(130, (uint8_t)(local_r13), (uint8_t)(local_r13), Arg1);
    v_stack_m314 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_00476A18;
    Arg2 = ((uint32_t)(*(uint32_t *)(v_stack_m2E8 + 0x3C))) << (3);
    result = ExAllocatePool2(64, Arg2, (uint32_t)(0x41536553ULL), Arg1);
    result = 0;
    if (0 != 0) goto loc_00476A03;
    if (v_stack_m318 == 0) {
        Arg1 = Arg1;
        result = SeUnlockSubjectContext(Arg1, Arg2, (uint32_t)(0x41536553ULL), Arg1);
    }
    result = SepRmDereferenceCap(v_stack_m2E8, Arg2, (uint32_t)(0x41536553ULL), Arg1);
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = 0xC0000017ULL;
    result = SepFreeResourceInfo(v_stack_m308, Arg2, (uint32_t)(0x41536553ULL), Arg1);
    goto loc_0047732E;
loc_00476A03:
    Arg2 = 0;
    Arg3 = ((uint32_t)(*(uint32_t *)(v_stack_m2E8 + 0x3C))) << (3);
    result = memset(result, Arg2, Arg3, Arg1);
loc_00476A18:
    local_r10 = 0;
    v_stack_m2F4 = 0;
    v_stack_m300 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m2E8 + 0x3C)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m2E8 + 0x3C))) == 0) goto loc_00476E99;
loc_00476A2F:
    v_stack_m200 = v_xmm0;
    v_stack_m1F0 = v_xmm0;
    v_stack_m1E0 = v_xmm0;
    v_stack_m2B8 = *(uint64_t *)(v_stack_m2E8 + 0x0 * 8 + 0x40);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m2E8 + 0x0 * 8 + 0x40) + 0x18)) == 0) goto loc_00476BC6;
    result = 0;
    if (v_stack_m308 == 0) {
        Arg1 = v_stack_m2C0;
        Arg2 = v_stack_m308;
        result = AuthzBasepInitializeResourceClaimsFromSacl(Arg1, Arg2, *(uint64_t *)(v_stack_m2E8 + 0x0 * 8 + 0x40), Arg1);
        Arg1 = v_stack_m30C;
        local_r10 = 0;
        Arg3 = v_stack_m2B8;
        Arg1 = (uint8_t)(Arg1);
        if (sign_flag) { Arg1 = (uint32_t)(local_r13); }
        v_stack_m30C = (uint32_t)(Arg1);
        Arg1 = v_stack_m308;
    }
    if (*(uint64_t *)(local_rdi + 0x448) == 0) goto loc_00476AB4;
    goto loc_00476ABD;
loc_00476AB4:
    local_r11 = 0;
loc_00476ABD:
    v_stack_m370 = v_stack_m2E0;
    v_stack_m378 = 0;
    v_stack_m380 = (uint8_t)(local_r13);
    v_stack_m388 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x10)));
    v_stack_m390 = *(uint64_t *)(Arg3 + 0x18);
    v_stack_m398 = 0;
    v_stack_m3A0 = *(uint64_t *)(*(uint64_t *)(local_rdi + 0x448) + 0x248);
    v_stack_m3A8 = *(uint64_t *)(*(uint64_t *)(local_rdi + 0x448) + 0x248);
    result = AuthzBasepEvaluateAceCondition(0, *(uint64_t *)(local_rdi + 0x308), Arg1, *(uint64_t *)(*(uint64_t *)(local_rdi + 0x448) + 0x248));
    v_stack_m300 = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(v_stack_m2E0))) == ((uint32_t)(local_r13))) goto loc_00476BC6;
    local_r10 = 0;
    if (sign_flag) goto loc_00477081;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0xC8)))) & (16)) == 0) goto loc_00476BB7;
    if (*(uint64_t *)(local_rdi + 0x448) == 0) goto loc_00476B54;
    goto loc_00476B5D;
loc_00476B54:
loc_00476B5D:
    v_stack_m370 = v_stack_m2E0;
    v_stack_m378 = (uint8_t)(local_r13);
    v_stack_m380 = (uint8_t)(local_r13);
    v_stack_m388 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m2B8 + 0x10)));
    v_stack_m390 = *(uint64_t *)(v_stack_m2B8 + 0x18);
    v_stack_m398 = *(uint64_t *)(*(uint64_t *)(local_rdi + 0x448) + 0x258);
    v_stack_m3A0 = *(uint64_t *)(*(uint64_t *)(local_rdi + 0x448) + 0x258);
    v_stack_m3A8 = *(uint64_t *)(*(uint64_t *)(local_rdi + 0x448) + 0x258);
    result = AuthzBasepEvaluateAceCondition(0, *(uint64_t *)(local_rdi + 0x308), v_stack_m308, *(uint64_t *)(*(uint64_t *)(local_rdi + 0x448) + 0x258));
    local_r10 = 0;
    v_stack_m300 = (uint32_t)(result);
    if (sign_flag) goto loc_00477081;
loc_00476BB7:
    if (v_stack_m30C != 0) goto loc_00476BC6;
    if (((uint32_t)((uint32_t)(v_stack_m2E0))) != ((uint32_t)(local_r13))) goto loc_00476E7F;
loc_00476BC6:
    result = SepBuildCapeSecurityDescriptor(v_stack_m270, *(uint64_t *)(v_stack_m2B8 + 0x20), v_stack_m2C0, *(uint64_t *)(*(uint64_t *)(local_rdi + 0x448) + 0x258));
    Arg2 = 0;
    if (sign_flag) goto loc_004770F0;
    if ((((uint8_t)(local_r13)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m2B8 + 0x30))))) == 0) goto loc_00476C05;
    if (!(condition_is_below)) {
        Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x10))) | (*(uint32_t *)(local_r15 + 0x14)));
    }
    goto loc_00476C09;
loc_00476C05:
loc_00476C09:
    v_stack_m328 = 0;
    v_stack_m330 = v_stack_m315;
    v_stack_m338 = v_stack_m308;
    v_stack_m340 = v_stack_m220;
    v_stack_m348 = Arg7;
    v_stack_m350 = (uint8_t)(v_stack_m316);
    v_stack_m358 = 0;
    v_stack_m360 = v_stack_mC8;
    v_stack_m368 = v_stack_m2B0;
    v_stack_m370 = 0;
    v_stack_m378 = v_stack_m2F8;
    v_stack_m380 = Arg6;
    v_stack_m388 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x14)));
    v_stack_m390 = *(uint64_t *)(local_r15 + 0x20);
    v_stack_m398 = (uint32_t)(local_r13);
    v_stack_m3A0 = v_stack_m200;
    v_stack_m3A8 = (uint32_t)(Arg1);
    v_stack_m200 = v_xmm0;
    v_stack_m1F0 = v_xmm0;
    v_stack_m1E0 = v_xmm0;
    result = SepAccessCheckEx(v_stack_m270, Arg2, *(uint64_t *)(Arg1 + 0x10), *(uint64_t *)(Arg1));
    local_r10 = 0;
    local_r11 = (uint32_t)(((uint32_t)(v_stack_m1E4)) | ((uint32_t)((uint32_t)(v_stack_m2FC))));
    v_stack_m310 = (uint8_t)(result);
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x14))) | (*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8))));
    local_rsi = (uint32_t)((local_rsi) & (v_stack_m2F8));
    v_stack_m2F8 = (uint32_t)(local_rsi);
    result = *(uint64_t *)(Arg4 + 0x8);
    if (v_stack_m316 != 0) {
        result = (uint32_t)(local_rsi);
        result = (uint32_t)((result) & (0x60000ULL));
        local_r11 = (uint32_t)((local_r11) | ((uint32_t)(result)));
    }
    result = (uint32_t)(~((uint32_t)(v_stack_m1E0)));
    local_r11 = (uint32_t)((local_r11) & ((uint32_t)(result)));
    result = (uint32_t)(v_stack_m2B0);
    if (condition_is_equal) { result = (uint32_t)((uint32_t)(0xC0000022ULL)); }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r11))) ^ ((uint32_t)((uint32_t)(v_stack_m2D4))));
    v_stack_m2DC = (uint32_t)(result);
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)((uint32_t)(v_stack_m2D4))));
    local_rsi = (uint32_t)(v_stack_m2D4);
    if (!(condition_is_equal)) {
        Arg4 = v_stack_m1C8;
        v_stack_m3A8 = 0;
        Arg2 = 0x50000ULL;
        result = AuthzBasepSetAccessReasons(Arg1, Arg2, (uint32_t)(v_stack_m2F4), Arg4);
        Arg4 = v_stack_m2FC;
        local_rsi = (uint32_t)(((uint32_t)(v_stack_m2D4)) & ((uint32_t)(local_r11)));
        v_stack_m2D4 = (uint32_t)(local_rsi);
        local_r10 = 0;
    }
    if ((uint8_t)(v_stack_m314) == 0) goto loc_00477078;
    if (*(uint64_t *)(v_stack_m2B8 + 0x28) == 0) goto loc_00477055;
    result = SepBuildCapeSecurityDescriptor(v_stack_m248, *(uint64_t *)(v_stack_m2B8 + 0x28), v_stack_m2C0, Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_004770AA;
    if (((*(uint32_t *)(v_stack_m2B8 + 0x30)) & (256)) == 0) goto loc_00476D9F;
    if (!(condition_is_below)) {
        Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x10))) | (*(uint32_t *)(local_r15 + 0x14)));
    }
    goto loc_00476DA3;
loc_00476D9F:
loc_00476DA3:
    v_stack_m328 = 0;
    v_stack_m330 = v_stack_m30F;
    v_stack_m338 = v_stack_m308;
    v_stack_m340 = v_stack_m220;
    v_stack_m348 = Arg7;
    v_stack_m350 = (uint8_t)(v_stack_m316);
    v_stack_m358 = 0;
    v_stack_m360 = v_stack_mC8;
    v_stack_m368 = v_stack_m2A0;
    v_stack_m370 = 0;
    v_stack_m378 = v_stack_m2D0;
    v_stack_m380 = Arg6;
    Arg2 = 0;
    v_stack_m388 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x14)));
    v_stack_m390 = *(uint64_t *)(local_r15 + 0x20);
    v_stack_m398 = 0;
    v_stack_m3A0 = 0;
    v_stack_m3A8 = (uint32_t)(Arg1);
    v_stack_m200 = v_xmm0;
    v_stack_m1F0 = v_xmm0;
    v_stack_m1E0 = v_xmm0;
    result = SepAccessCheckEx(v_stack_m248, Arg2, *(uint64_t *)(Arg1 + 0x10), *(uint64_t *)(Arg1));
    *(uint8_t *)(result + (uint32_t)(v_stack_m2F4) * 8 + 0x4) = (uint8_t)(local_r13);
    result = (uint32_t)(((uint32_t)(v_stack_m2FC)) | (v_stack_m2D0));
    *(uint32_t *)(result + (uint32_t)(v_stack_m2F4) * 8) = (uint32_t)(result);
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m2F0)) & (v_stack_m2D0));
    v_stack_m2F0 = Arg2;
    local_r10 = 0;
loc_00476E7F:
loc_00476E82:
    result = (uint32_t)(((uint32_t)(v_stack_m2F4)) + ((uint32_t)(local_r13)));
    v_stack_m2F4 = (uint32_t)(result);
    v_stack_m300 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m2E8 + 0x3C)));
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m2E8 + 0x3C))))) goto loc_00476A2F;
loc_00476E99:
    local_rsi = 0;
    if ((uint8_t)(v_stack_m314) == 0) goto loc_00476F82;
    if (((uint32_t)((uint32_t)(v_stack_m2F0))) == ((uint32_t)((uint32_t)(v_stack_m2D8)))) goto loc_00476F82;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m2F0)))) ^ ((uint32_t)((uint32_t)(v_stack_m2D8))));
    local_rsi = (uint32_t)((local_rsi) & ((uint32_t)((uint32_t)(v_stack_m2F0))));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & ((uint32_t)((uint32_t)(v_stack_m2D8))));
    Arg2 = 0;
    v_stack_m30C = (uint32_t)(result);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m2E8 + 0x3C))) == 0) goto loc_00476F80;
    local_r15 = 0;
loc_00476ED4:
    if ((uint32_t)(local_rsi) != 0) goto loc_00476EE0;
    if ((uint32_t)(result) == 0) goto loc_00476F74;
loc_00476EE0:
    if ((*(uint8_t *)(result + 0x4)) == 0) goto loc_00476F65;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result))))) ^ ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
    if (!(condition_is_equal)) {
        Arg3 = 0;
        v_stack_m3A8 = 0;
        Arg3 = (uint32_t)((Arg3) << (24));
        Arg4 = v_stack_m148;
        Arg2 = 0x80000000ULL;
        result = AuthzBasepSetAccessReasons(Arg1, Arg2, Arg3, Arg4);
        result = v_stack_m30C;
    }
    Arg1 = (uint32_t)(~(Arg1));
    result = (uint32_t)((result) & ((uint32_t)(Arg1)));
    v_stack_m30C = (uint32_t)(result);
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(result))) & ((uint32_t)(local_rsi)));
    if (!(condition_is_equal)) {
        Arg3 = 0;
        v_stack_m3A8 = 0;
        Arg3 = (uint32_t)((Arg3) << (24));
        Arg4 = v_stack_m148;
        Arg2 = 0x80000000ULL;
        Arg1 = (uint32_t)(local_r11);
        result = AuthzBasepSetAccessReasons(Arg1, Arg2, Arg3, Arg4);
    }
    local_r11 = (uint32_t)(~(local_r11));
    local_rsi = (uint32_t)((local_rsi) & ((uint32_t)(local_r11)));
    result = AuthzBasepMergeAccessReasons(v_stack_m1C8, v_stack_m148, (uint32_t)(0xFF000000ULL), Arg4);
loc_00476F65:
    local_rdi = (uint32_t)((0) + ((uint32_t)(local_r13)));
    local_r12 = (result) + (8);
    if (((uint32_t)(local_rdi)) < ((uint32_t)((uint32_t)(v_stack_m300)))) goto loc_00476ED4;
loc_00476F74:
loc_00476F80:
    local_rsi = 0;
loc_00476F82:
    result = (uint32_t)(v_stack_m30C);
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0xFF000000ULL), Arg4);
    }
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = (uint32_t)((uint32_t)(v_stack_m2DC));
    if ((*(uint32_t *)(*(uint64_t *)(Arg4 + 0x10))) < 0) {
        v_stack_m315 = 0;
    }
    Arg3 = 0;
    result = AuthzBasepMergeAccessReasons(*(uint64_t *)(Arg4 + 0x18), v_stack_m1C8, Arg3, Arg4);
    result = AuthzBasepMergeAccessReasons(*(uint64_t *)(Arg4 + 0x18), v_stack_m1C8, (uint32_t)(0xFF000000ULL), Arg4);
loc_00476FD8:
    if (v_stack_m313 != 0) goto loc_004770F5;
    if (v_stack_m313 >= 0) goto loc_004770F5;
    if (v_stack_m2EC == 0) goto loc_0047702C;
    if (v_stack_m20A != 0) goto loc_00477175;
    if (v_stack_m20B != 0) goto loc_00477175;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m2A8 + 0xC8))) & ((uint32_t)((uint32_t)(0x3000000ULL))));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0x3000000ULL)))) goto loc_00477175;
loc_0047702C:
    v_stack_m3A0 = 0;
    v_stack_m3A8 = v_stack_m315;
    result = SepConstrainByMandatory(v_stack_m290, (uint32_t)(*(uint32_t *)(v_stack_m280 + 0x10)), *(uint64_t *)(Arg4 + 0x8), *(uint64_t *)(Arg4 + 0x10));
    Arg1 = (uint32_t)(~((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8))))));
    goto loc_0047715F;
loc_00477055:
    *(uint8_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8))) + (uint32_t)((uint32_t)(*(uint64_t *)(Arg4 + 0x8))) * 8 + 0x4) = (uint8_t)(local_r13);
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(Arg4 + 0x10)))) | (v_stack_m2F8));
    *(uint32_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8))) + (uint32_t)((uint32_t)(*(uint64_t *)(Arg4 + 0x8))) * 8) = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)(v_stack_m2F0)) & (v_stack_m2F8));
    v_stack_m2F0 = (uint32_t)(result);
    goto loc_00476E7F;
loc_00477078:
    goto loc_00476E82;
loc_00477081:
    if (v_stack_m318 == 0) {
        Arg1 = v_stack_m278;
        result = SeUnlockSubjectContext(Arg1, *(uint64_t *)(Arg4 + 0x8), *(uint64_t *)(Arg4 + 0x8), *(uint64_t *)(Arg4 + 0x10));
    }
    result = SepRmDereferenceCap(v_stack_m2E8, *(uint64_t *)(Arg4 + 0x8), *(uint64_t *)(Arg4 + 0x8), *(uint64_t *)(Arg4 + 0x10));
    local_rdi = 0;
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)) = 0;
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = (uint32_t)((uint32_t)(v_stack_m300));
    goto loc_004770CF;
loc_004770AA:
loc_004770AE:
    result = *(uint64_t *)(Arg4 + 0x10);
    if (v_stack_m318 == ((uint8_t)(*(uint64_t *)(Arg4 + 0x10)))) {
        Arg1 = v_stack_m278;
        result = SeUnlockSubjectContext(Arg1, *(uint64_t *)(Arg4 + 0x8), *(uint64_t *)(Arg4 + 0x8), *(uint64_t *)(Arg4 + 0x10));
    }
    result = SepRmDereferenceCap(v_stack_m2E8, *(uint64_t *)(Arg4 + 0x8), *(uint64_t *)(Arg4 + 0x8), *(uint64_t *)(Arg4 + 0x10));
    local_rdi = 0;
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)) = 0;
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = (uint32_t)(v_stack_m2E8);
loc_004770CF:
    result = SepFreeResourceInfo(v_stack_m308, *(uint64_t *)(Arg4 + 0x8), *(uint64_t *)(Arg4 + 0x8), *(uint64_t *)(Arg4 + 0x10));
    if ((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8))) == 0) goto loc_0047732E;
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8))), Arg2, *(uint64_t *)(Arg4 + 0x8), *(uint64_t *)(Arg4 + 0x10));
    goto loc_0047732E;
loc_004770F0:
    goto loc_004770AE;
loc_004770F5:
    if (v_stack_m2EC == ((uint8_t)(v_stack_m2E8))) goto loc_00477175;
    if (v_stack_m20A != ((uint8_t)(v_stack_m2E8))) goto loc_00477175;
    if (v_stack_m20B != ((uint8_t)(v_stack_m2E8))) goto loc_00477175;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0xC8))) & ((uint32_t)((uint32_t)(0x3000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x3000000ULL)))) goto loc_00477143;
    if (v_stack_m214 != ((uint32_t)(v_stack_m2E8))) goto loc_00477143;
    v_stack_m209 = (uint8_t)(local_r13);
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = (uint32_t)(v_stack_m2E8);
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m280 + 0x10)));
    v_stack_m315 = (uint8_t)(local_r13);
    goto loc_00477175;
loc_00477143:
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x10)) = 0xC0000022ULL;
    *(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)) = (uint32_t)(v_stack_m2E8);
    v_stack_m315 = (uint8_t)(v_stack_m2E8);
    Arg1 = (uint32_t)(~((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))));
loc_0047715F:
    Arg3 = 0;
    v_stack_m3A8 = (uint8_t)(v_stack_m2E8);
    result = AuthzBasepSetAccessReasons(Arg1, (uint32_t)(0x300000ULL), Arg3, *(uint64_t *)(Arg4 + 0x18));
loc_00477175:
    if (condition_is_above_or_equal) goto loc_0047722D;
    v_stack_m398 = v_stack_m312;
    v_stack_m3A0 = (uint32_t)(v_stack_m2E8);
    v_stack_m3A8 = v_stack_m315;
    result = SepConstrainByConstraintMask((uint32_t)(v_stack_m2C8), (uint32_t)(*(uint32_t *)(v_stack_m280 + 0x10)), *(uint64_t *)(Arg4 + 0x8), *(uint64_t *)(Arg4 + 0x10));
    Arg3 = 0;
    v_stack_m3A8 = (uint8_t)(v_stack_m2E8);
    Arg1 = (uint32_t)(~((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8))))));
    result = AuthzBasepSetAccessReasons(Arg1, (uint32_t)(0x900000ULL), Arg3, *(uint64_t *)(Arg4 + 0x18));
    v_stack_m398 = v_stack_m311;
    v_stack_m3A0 = (uint32_t)(v_stack_m2E8);
    v_stack_m3A8 = v_stack_m315;
    result = SepConstrainByConstraintMask((uint32_t)(v_stack_m298), (uint32_t)(*(uint32_t *)(v_stack_m280 + 0x10)), *(uint64_t *)(Arg4 + 0x8), *(uint64_t *)(Arg4 + 0x10));
    Arg3 = 0;
    v_stack_m3A8 = (uint8_t)(v_stack_m2E8);
    Arg1 = (uint32_t)(~((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)))));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8))))));
    result = AuthzBasepSetAccessReasons(Arg1, (uint32_t)(0xA00000ULL), Arg3, *(uint64_t *)(Arg4 + 0x18));
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(Arg1, (uint32_t)(0xA00000ULL), Arg3, *(uint64_t *)(Arg4 + 0x18));
    if ((uint32_t)(result) != 0) {
        Arg1 = *(uint64_t *)(Arg4 + 0x8);
        result = v_stack_m2CC;
        result = (uint32_t)(~(result));
    }
    if (0 == 0) goto loc_004772EA;
    if (v_stack_m312 != ((uint8_t)(v_stack_m2E8))) goto loc_00477269;
    if (v_stack_m311 != ((uint8_t)(v_stack_m2E8))) goto loc_00477269;
    if ((uint32_t)((uint32_t)(v_stack_m214)) != 0) goto loc_004772BC;
    if (((*(uint32_t *)(local_rdi + 0xC8)) & (0x4000ULL)) == 0) goto loc_004772BC;
    if ((*(uint32_t *)(*(uint64_t *)(Arg4 + 0x10))) < ((uint32_t)(v_stack_m2E8))) goto loc_00477269;
    result = *(uint64_t *)(Arg4 + 0x10);
    local_rbx = (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x8)));
    local_rsi = v_stack_m2E8;
    if (v_stack_m209 != ((uint8_t)(v_stack_m2E8))) {
        result = *(uint64_t *)(Arg4 + 0x10);
        Arg1 = v_stack_m278;
        local_rdi = *(uint32_t *)(v_stack_m280 + 0x14);
        local_rdi = (uint32_t)((local_rdi) | (*(uint32_t *)(v_stack_m280 + 0x10)));
        local_rbx = *(uint64_t *)(v_stack_m280 + 0x8);
        local_rsi = *(uint32_t *)(result);
        local_rsi = (uint32_t)((local_rsi) >> (31));
        local_rsi = (uint8_t)((local_rsi) ^ ((uint8_t)(local_r13)));
        result = SepLocateTokenTrustLevel(Arg1, (uint32_t)(0xA00000ULL), Arg3, *(uint64_t *)(Arg4 + 0x18));
        v_stack_m390 = 0;
        Arg4 = result;
        result = *(uint64_t *)(local_rbx + 0x8);
        Arg3 = 0;
        v_stack_m398 = (uint8_t)(local_rsi);
        Arg2 = 0;
        v_stack_m3A0 = (uint32_t)(local_rdi);
        local_rdi = v_stack_m2A8;
        Arg1 = local_rdi;
        v_stack_m3A8 = result;
        result = SeLogAccessFailure(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_m214;
        local_rsi = 0;
    }
    if ((*(uint32_t *)(*(uint64_t *)(Arg4 + 0x10))) >= 0) goto loc_004772EA;
    if ((uint32_t)(Arg1) != 0) goto loc_004772EA;
    if (((*(uint32_t *)(local_rdi + 0xC8)) & (0x4000ULL)) == 0) goto loc_004772EA;
    result = SepLpacCausedAccessFailure(v_stack_m220, (uint32_t)(*(uint32_t *)(v_stack_m280 + 0x10)), Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = SepLogLpacAccessFailure(v_stack_m220, (uint32_t)(*(uint32_t *)(v_stack_m280 + 0x10)), Arg3, Arg4);
    }
    if (v_stack_m317 != 0) {
        Arg1 = v_stack_m2E8;
        result = SepRmDereferenceCap(Arg1, (uint32_t)(*(uint32_t *)(v_stack_m280 + 0x10)), Arg3, Arg4);
    }
    if (v_stack_m318 == 0) {
        Arg1 = v_stack_m278;
        result = SeUnlockSubjectContext(Arg1, (uint32_t)(*(uint32_t *)(v_stack_m280 + 0x10)), Arg3, Arg4);
    }
    result = SepFreeResourceInfo(v_stack_m308, (uint32_t)(*(uint32_t *)(v_stack_m280 + 0x10)), Arg3, Arg4);
    if (v_stack_m310 == 0) goto loc_00477320;
    if (v_stack_m315 != 0) goto loc_00476222;
loc_00477320:
    goto loc_00476222;
loc_00477328:
    *(uint32_t *)(v_stack_m308) = 0xC000000DULL;
loc_0047732E:
    result = 0;
loc_00477330:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(*(uint32_t *)(v_stack_m280 + 0x10)), Arg3, Arg4);
    local_rsp = (local_rsp) + (912);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0047602C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
