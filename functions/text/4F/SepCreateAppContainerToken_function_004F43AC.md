# SepCreateAppContainerToken

- RVA: `0x004F43AC`–`0x004F4D1C` (길이 `2,416` bytes)
- VA: `0x00000001404F43AC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BBF70`
- 디코드: `593`개 명령, `2,416/2,416` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **59**; 고유 호출 대상: **35**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x004F449B` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x004F44DF` → [PsReferenceEffectiveToken](../../page/9A/PsReferenceEffectiveToken_function_009A2B40.md) (function, `0x009A2B40`)
- `0x004F44EA` → [SepCheckCreateAppContainer](../../page/70/SepCheckCreateAppContainer_function_007006CC.md) (function, `0x007006CC`)
- `0x004F452A` → [RtlIsPackageSid](../../page/A5/RtlIsPackageSid_function_00A5E73C.md) (function, `0x00A5E73C`)
- `0x004F4563` → [RtlIsCapabilitySid](../../page/A5/RtlIsCapabilitySid_function_00A5ED84.md) (function, `0x00A5ED84`)
- `0x004F4581` → [RtlEqualSid](../40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)
- `0x004F45EA` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x004F45EF` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x004F4607` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x004F461D` → [ObCloseHandle](../../page/8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x004F4645` → [SepCapabilitiesHasAppSiloBaseSID](../40/SepCapabilitiesHasAppSiloBaseSID_function_004005B0.md) (function, `0x004005B0`)
- `0x004F465E` → [SepIsAppSiloCapability](../48/SepIsAppSiloCapability_function_0048E54C.md) (function, `0x0048E54C`)
- `0x004F4677` → [RtlGetAppContainerSidType](../../page/A7/RtlGetAppContainerSidType_function_00A72160.md) (function, `0x00A72160`)
- `0x004F469F` → [SepCheckCapabilities](../../page/AA/SepCheckCapabilities_function_00AA4A10.md) (function, `0x00AA4A10`)
- `0x004F46BF` → [Feature_871661881__private_IsEnabledDeviceUsageNoInline](Feature_871661881__private_IsEnabledDeviceUsageNoInline_function_004F4D24.md) (function, `0x004F4D24`)
- `0x004F46D6` → [RtlQueryElevationFlags](../../page/A6/RtlQueryElevationFlags_function_00A60CB0.md) (function, `0x00A60CB0`)
- `0x004F4700` → [ExAcquireResourceSharedLite](../21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x004F4708` → [SepLocateTokenIntegrity](../41/SepLocateTokenIntegrity_function_0041BF10.md) (function, `0x0041BF10`)
- `0x004F4750` → [SeCaptureSubjectContext](../../page/86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x004F4774` → [ExAcquireResourceSharedLite](../21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x004F477C` → [SepLocateTokenIntegrity](../41/SepLocateTokenIntegrity_function_0041BF10.md) (function, `0x0041BF10`)
- `0x004F47A1` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x004F47A6` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x004F47B3` → [SeReleaseSubjectContext](../../page/86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x004F47BC` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x004F47C1` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x004F47FC` → [SepDuplicateToken](../../page/8B/SepDuplicateToken_function_008B87EC.md) (function, `0x008B87EC`)
- `0x004F481D` → [SeSetMandatoryPolicyToken](../../page/A5/SeSetMandatoryPolicyToken_function_00A5EDCC.md) (function, `0x00A5EDCC`)
- `0x004F4848` → [ExAcquireResourceExclusiveLite](../21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x004F485C` → [SepLocateTokenIntegrity](../41/SepLocateTokenIntegrity_function_0041BF10.md) (function, `0x0041BF10`)
- `0x004F48A9` → [SeCaptureSubjectContext](../../page/86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x004F48B3` → [SeLockSubjectContext](../../page/8C/SeLockSubjectContext_function_008C64C0.md) (function, `0x008C64C0`)
- `0x004F48CF` → [ExAcquireResourceSharedLite](../21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x004F48D7` → [SepLocateTokenIntegrity](../41/SepLocateTokenIntegrity_function_0041BF10.md) (function, `0x0041BF10`)
- `0x004F4904` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x004F4909` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x004F4913` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x004F491D` → [SeReleaseSubjectContext](../../page/86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x004F492B` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x004F4930` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x004F493D` → [SepLocateTokenIntegrity](../41/SepLocateTokenIntegrity_function_0041BF10.md) (function, `0x0041BF10`)
- `0x004F4988` → [SepLocateTokenIntegrity](../41/SepLocateTokenIntegrity_function_0041BF10.md) (function, `0x0041BF10`)
- `0x004F4A19` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x004F4A23` → [SeReleaseSubjectContext](../../page/86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x004F4A75` → [Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline](../4C/Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline_function_004C78E8.md) (function, `0x004C78E8`)
- `0x004F4ACC` → [SepSetTokenCapabilities](../../page/9C/SepSetTokenCapabilities_function_009C9AF4.md) (function, `0x009C9AF4`)
- `0x004F4AE3` → [SepSetTokenLowboxNumber](../../page/A6/SepSetTokenLowboxNumber_function_00A64D6C.md) (function, `0x00A64D6C`)
- `0x004F4B17` → [SepSetTokenCachedHandles](../../page/9A/SepSetTokenCachedHandles_function_009A939C.md) (function, `0x009A939C`)
- `0x004F4B2E` → [SepSetTokenPackage](../../page/A2/SepSetTokenPackage_function_00A20CB8.md) (function, `0x00A20CB8`)
- `0x004F4B45` → [SepAppendAceToTokenDefaultDacl](../40/SepAppendAceToTokenDefaultDacl_function_004002F8.md) (function, `0x004002F8`)
- `0x004F4B76` → [SepSidInTokenSidHash](../3C/SepSidInTokenSidHash_function_003C85E0.md) (function, `0x003C85E0`)
- `0x004F4BC3` → [SepSidInTokenSidHash](../3C/SepSidInTokenSidHash_function_003C85E0.md) (function, `0x003C85E0`)
- `0x004F4C13` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x004F4C18` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x004F4C50` → [ObInsertObject](../../page/8B/ObInsertObject_function_008B9100.md) (function, `0x008B9100`)
- `0x004F4C78` → [SepAppendAceToTokenObjectAcl](../../page/8B/SepAppendAceToTokenObjectAcl_function_008B6430.md) (function, `0x008B6430`)
- `0x004F4C88` → [SepFinalizeTokenAcls](../../page/8B/SepFinalizeTokenAcls_function_008B63F4.md) (function, `0x008B63F4`)
- `0x004F4C97` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x004F4CF7` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- [SeSubProcessToken](../../page/AA/SeSubProcessToken_function_00AAD570.md) at `0x00AAD8B7`
- [NtCreateLowBoxToken](../../page/AB/NtCreateLowBoxToken_function_00AB9880.md) at `0x00AB9B22`

### Static image references
- `0x004F4465` → RVA `0x00FD8020` (`PAGEDATA`; read)
- `0x004F45BC` → RVA `0x00012D08` (`.rdata`; read)
- `0x004F45C6` → RVA `0x00E0EBF0` (`.data`; read/write)
- `0x004F4B6D` → RVA `0x00F05780` (`.data`; read)
- `0x004F4B7F` → RVA `0x00FD9AD8` (`PAGEDATA`; read/write)
- `0x004F4BBA` → RVA `0x00F05790` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **26**
  - `0x004F449B` → [ObReferenceObjectByHandle](../../page/86/ObReferenceObjectByHandle_function_00868DB0.md) (`.text` → `PAGE`)
  - `0x004F44DF` → [PsReferenceEffectiveToken](../../page/9A/PsReferenceEffectiveToken_function_009A2B40.md) (`.text` → `PAGE`)
  - `0x004F44EA` → [SepCheckCreateAppContainer](../../page/70/SepCheckCreateAppContainer_function_007006CC.md) (`.text` → `PAGE`)
  - `0x004F452A` → [RtlIsPackageSid](../../page/A5/RtlIsPackageSid_function_00A5E73C.md) (`.text` → `PAGE`)
  - `0x004F4563` → [RtlIsCapabilitySid](../../page/A5/RtlIsCapabilitySid_function_00A5ED84.md) (`.text` → `PAGE`)
  - `0x004F461D` → [ObCloseHandle](../../page/8A/ObCloseHandle_function_008A1870.md) (`.text` → `PAGE`)
  - `0x004F4677` → [RtlGetAppContainerSidType](../../page/A7/RtlGetAppContainerSidType_function_00A72160.md) (`.text` → `PAGE`)
  - `0x004F469F` → [SepCheckCapabilities](../../page/AA/SepCheckCapabilities_function_00AA4A10.md) (`.text` → `PAGE`)
  - `0x004F46D6` → [RtlQueryElevationFlags](../../page/A6/RtlQueryElevationFlags_function_00A60CB0.md) (`.text` → `PAGE`)
  - `0x004F4750` → [SeCaptureSubjectContext](../../page/86/SeCaptureSubjectContext_function_0086B820.md) (`.text` → `PAGE`)
  - `0x004F47B3` → [SeReleaseSubjectContext](../../page/86/SeReleaseSubjectContext_function_0086B710.md) (`.text` → `PAGE`)
  - `0x004F47FC` → [SepDuplicateToken](../../page/8B/SepDuplicateToken_function_008B87EC.md) (`.text` → `PAGE`)
  - `0x004F481D` → [SeSetMandatoryPolicyToken](../../page/A5/SeSetMandatoryPolicyToken_function_00A5EDCC.md) (`.text` → `PAGE`)
  - `0x004F48A9` → [SeCaptureSubjectContext](../../page/86/SeCaptureSubjectContext_function_0086B820.md) (`.text` → `PAGE`)
  - `0x004F48B3` → [SeLockSubjectContext](../../page/8C/SeLockSubjectContext_function_008C64C0.md) (`.text` → `PAGE`)
  - `0x004F4913` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (`.text` → `PAGE`)
  - `0x004F491D` → [SeReleaseSubjectContext](../../page/86/SeReleaseSubjectContext_function_0086B710.md) (`.text` → `PAGE`)
  - `0x004F4A19` → [SeUnlockSubjectContext](../../page/8C/SeUnlockSubjectContext_function_008C6520.md) (`.text` → `PAGE`)
  - `0x004F4A23` → [SeReleaseSubjectContext](../../page/86/SeReleaseSubjectContext_function_0086B710.md) (`.text` → `PAGE`)
  - `0x004F4ACC` → [SepSetTokenCapabilities](../../page/9C/SepSetTokenCapabilities_function_009C9AF4.md) (`.text` → `PAGE`)
  - `0x004F4AE3` → [SepSetTokenLowboxNumber](../../page/A6/SepSetTokenLowboxNumber_function_00A64D6C.md) (`.text` → `PAGE`)
  - `0x004F4B17` → [SepSetTokenCachedHandles](../../page/9A/SepSetTokenCachedHandles_function_009A939C.md) (`.text` → `PAGE`)
  - `0x004F4B2E` → [SepSetTokenPackage](../../page/A2/SepSetTokenPackage_function_00A20CB8.md) (`.text` → `PAGE`)
  - `0x004F4C50` → [ObInsertObject](../../page/8B/ObInsertObject_function_008B9100.md) (`.text` → `PAGE`)
  - `0x004F4C78` → [SepAppendAceToTokenObjectAcl](../../page/8B/SepAppendAceToTokenObjectAcl_function_008B6430.md) (`.text` → `PAGE`)
  - `0x004F4C88` → [SepFinalizeTokenAcls](../../page/8B/SepFinalizeTokenAcls_function_008B63F4.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F43AC  4C 8B DC                        mov r11, rsp
004F43AF  49 89 5B 18                     mov qword ptr [r11 + 0x18], rbx
004F43B3  49 89 73 20                     mov qword ptr [r11 + 0x20], rsi
004F43B7  49 89 53 10                     mov qword ptr [r11 + 0x10], rdx
004F43BB  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
004F43BF  57                              push rdi
004F43C0  41 54                           push r12
004F43C2  41 55                           push r13
004F43C4  41 56                           push r14
004F43C6  41 57                           push r15
004F43C8  48 81 EC E0 00 00 00            sub rsp, 0xe0
004F43CF  4D 8B E1                        mov r12, r9
004F43D2  41 8B F8                        mov edi, r8d
004F43D5  48 8B F2                        mov rsi, rdx
004F43D8  48 8B D1                        mov rdx, rcx
004F43DB  33 DB                           xor ebx, ebx
004F43DD  89 5C 24 58                     mov dword ptr [rsp + 0x58], ebx
004F43E1  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
004F43E6  0F 57 C0                        xorps xmm0, xmm0
004F43E9  33 C0                           xor eax, eax
004F43EB  41 0F 11 43 A0                  movups xmmword ptr [r11 - 0x60], xmm0
004F43F0  49 89 43 B0                     mov qword ptr [r11 - 0x50], rax
004F43F4  88 5C 24 50                     mov byte ptr [rsp + 0x50], bl
004F43F8  88 5C 24 40                     mov byte ptr [rsp + 0x40], bl
004F43FC  49 89 5B 90                     mov qword ptr [r11 - 0x70], rbx
004F4400  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
004F4405  C7 44 24 60 01 00 00 00         mov dword ptr [rsp + 0x60], 1
004F440D  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
004F4412  0F 11 84 24 80 00 00 00         movups xmmword ptr [rsp + 0x80], xmm0
004F441A  88 5C 24 41                     mov byte ptr [rsp + 0x41], bl
004F441E  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
004F4426  48 8B 40 08                     mov rax, qword ptr [rax + 8]
004F442A  4C 8B 70 10                     mov r14, qword ptr [rax + 0x10]
004F442E  4C 8B 68 18                     mov r13, qword ptr [rax + 0x18]
004F4432  8B 48 20                        mov ecx, dword ptr [rax + 0x20]
004F4435  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
004F4439  48 85 D2                        test rdx, rdx
004F443C  75 0A                           jne 0x1404f4448
004F443E  48 85 F6                        test rsi, rsi
004F4441  74 0F                           je 0x1404f4452
004F4443  48 85 D2                        test rdx, rdx
004F4446  74 05                           je 0x1404f444d
004F4448  48 85 F6                        test rsi, rsi
004F444B  75 05                           jne 0x1404f4452
004F444D  4D 85 F6                        test r14, r14
004F4450  75 0A                           jne 0x1404f445c
004F4452  B8 0D 00 00 C0                  mov eax, 0xc000000d
004F4457  E9 A2 08 00 00                  jmp 0x1404f4cfe
004F445C  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
004F4460  48 85 C9                        test rcx, rcx
004F4463  74 4D                           je 0x1404f44b2
004F4465  4C 8B 05 B4 3B AE 00            mov r8, qword ptr [rip + 0xae3bb4]
004F446C  48 89 9C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rbx
004F4474  48 8D 84 24 98 00 00 00         lea rax, [rsp + 0x98]
004F447C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004F4481  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
004F4489  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004F448E  44 8A 8C 24 30 01 00 00         mov r9b, byte ptr [rsp + 0x130]
004F4496  BA 02 00 00 00                  mov edx, 2
004F449B  E8 10 49 37 00                  call 0x140868db0
004F44A0  4C 8B BC 24 90 00 00 00         mov r15, qword ptr [rsp + 0x90]
004F44A8  85 C0                           test eax, eax
004F44AA  0F 88 4E 08 00 00               js 0x1404f4cfe
004F44B0  EB 35                           jmp 0x1404f44e7
004F44B2  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
004F44BB  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
004F44C0  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
004F44C8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004F44CD  4C 8D 4C 24 51                  lea r9, [rsp + 0x51]
004F44D2  4C 8D 84 24 A4 00 00 00         lea r8, [rsp + 0xa4]
004F44DA  BA 53 68 72 74                  mov edx, 0x74726853
004F44DF  E8 5C E6 4A 00                  call 0x1409a2b40
004F44E4  4C 8B F8                        mov r15, rax
004F44E7  49 8B CE                        mov rcx, r14
004F44EA  E8 DD C1 20 00                  call 0x1407006cc
004F44EF  8B D8                           mov ebx, eax
004F44F1  85 C0                           test eax, eax
004F44F3  0F 88 A6 00 00 00               js 0x1404f459f
004F44F9  41 83 BF C0 00 00 00 01         cmp dword ptr [r15 + 0xc0], 1
004F4501  74 14                           je 0x1404f4517
004F4503  41 83 BF C4 00 00 00 02         cmp dword ptr [r15 + 0xc4], 2
004F450B  7D 0A                           jge 0x1404f4517
004F450D  BB A5 00 00 C0                  mov ebx, 0xc00000a5
004F4512  E9 88 00 00 00                  jmp 0x1404f459f
004F4517  8B 84 24 9C 00 00 00            mov eax, dword ptr [rsp + 0x9c]
004F451E  85 FF                           test edi, edi
004F4520  0F 45 C7                        cmovne eax, edi
004F4523  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
004F4527  49 8B CE                        mov rcx, r14
004F452A  E8 0D A2 56 00                  call 0x140a5e73c
004F452F  84 C0                           test al, al
004F4531  75 07                           jne 0x1404f453a
004F4533  BB 0D 00 00 C0                  mov ebx, 0xc000000d
004F4538  EB 65                           jmp 0x1404f459f
004F453A  41 8A 46 01                     mov al, byte ptr [r14 + 1]
004F453E  2C 08                           sub al, 8
004F4540  A8 FB                           test al, 0xfb
004F4542  74 07                           je 0x1404f454b
004F4544  BB 02 A2 00 C0                  mov ebx, 0xc000a202
004F4549  EB 54                           jmp 0x1404f459f
004F454B  33 DB                           xor ebx, ebx
004F454D  8B 74 24 54                     mov esi, dword ptr [rsp + 0x54]
004F4551  3B DE                           cmp ebx, esi
004F4553  0F 83 E7 00 00 00               jae 0x1404f4640
004F4559  8B F3                           mov esi, ebx
004F455B  48 03 F6                        add rsi, rsi
004F455E  49 8B 4C F5 00                  mov rcx, qword ptr [r13 + rsi*8]
004F4563  E8 1C A8 56 00                  call 0x140a5ed84
004F4568  84 C0                           test al, al
004F456A  74 26                           je 0x1404f4592
004F456C  33 FF                           xor edi, edi
004F456E  3B FB                           cmp edi, ebx
004F4570  73 1C                           jae 0x1404f458e
004F4572  8B D7                           mov edx, edi
004F4574  48 03 D2                        add rdx, rdx
004F4577  49 8B 54 D5 00                  mov rdx, qword ptr [r13 + rdx*8]
004F457C  49 8B 4C F5 00                  mov rcx, qword ptr [r13 + rsi*8]
004F4581  E8 4A C5 F0 FF                  call 0x140400ad0
004F4586  84 C0                           test al, al
004F4588  75 08                           jne 0x1404f4592
004F458A  FF C7                           inc edi
004F458C  EB E0                           jmp 0x1404f456e
004F458E  FF C3                           inc ebx
004F4590  EB BB                           jmp 0x1404f454d
004F4592  BB 0D 00 00 C0                  mov ebx, 0xc000000d
004F4597  48 8B B4 24 18 01 00 00         mov rsi, qword ptr [rsp + 0x118]
004F459F  48 8B BC 24 10 01 00 00         mov rdi, qword ptr [rsp + 0x110]
004F45A7  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
004F45AC  80 7C 24 41 00                  cmp byte ptr [rsp + 0x41], 0
004F45B1  74 41                           je 0x1404f45f4
004F45B3  85 DB                           test ebx, ebx
004F45B5  78 25                           js 0x1404f45dc
004F45B7  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
004F45BC  48 8B 0D 45 E7 B1 FF            mov rcx, qword ptr [rip - 0x4e18bb]
004F45C3  48 8B C1                        mov rax, rcx
004F45C6  F0 48 0F C1 05 21 A6 91 00      lock xadd qword ptr [rip + 0x91a621], rax
004F45CF  48 03 C1                        add rax, rcx
004F45D2  89 42 38                        mov dword ptr [rdx + 0x38], eax
004F45D5  48 C1 E8 20                     shr rax, 0x20
004F45D9  89 42 3C                        mov dword ptr [rdx + 0x3c], eax
004F45DC  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
004F45E1  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
004F45E6  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
004F45EA  E8 21 B4 D6 FF                  call 0x14025fa10
004F45EF  E8 BC 92 D6 FF                  call 0x14025d8b0
004F45F4  85 DB                           test ebx, ebx
004F45F6  79 32                           jns 0x1404f462a
004F45F8  45 84 F6                        test r14b, r14b
004F45FB  74 0F                           je 0x1404f460c
004F45FD  BA 44 66 6C 74                  mov edx, 0x746c6644
004F4602  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
004F4607  E8 D4 32 E0 FF                  call 0x1402f78e0
004F460C  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
004F4611  48 85 C9                        test rcx, rcx
004F4614  74 0C                           je 0x1404f4622
004F4616  8A 94 24 30 01 00 00            mov dl, byte ptr [rsp + 0x130]
004F461D  E8 4E D2 3A 00                  call 0x1408a1870
004F4622  85 DB                           test ebx, ebx
004F4624  0F 88 C0 06 00 00               js 0x1404f4cea
004F462A  48 85 FF                        test rdi, rdi
004F462D  0F 84 A6 06 00 00               je 0x1404f4cd9
004F4633  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
004F4638  48 89 07                        mov qword ptr [rdi], rax
004F463B  E9 A6 06 00 00                  jmp 0x1404f4ce6
004F4640  49 8B D5                        mov rdx, r13
004F4643  8B CE                           mov ecx, esi
004F4645  E8 66 BF F0 FF                  call 0x1404005b0
004F464A  84 C0                           test al, al
004F464C  75 21                           jne 0x1404f466f
004F464E  33 DB                           xor ebx, ebx
004F4650  3B DE                           cmp ebx, esi
004F4652  73 1B                           jae 0x1404f466f
004F4654  8B CB                           mov ecx, ebx
004F4656  48 03 C9                        add rcx, rcx
004F4659  49 8B 4C CD 00                  mov rcx, qword ptr [r13 + rcx*8]
004F465E  E8 E9 9E F9 FF                  call 0x14048e54c
004F4663  84 C0                           test al, al
004F4665  0F 85 27 FF FF FF               jne 0x1404f4592
004F466B  FF C3                           inc ebx
004F466D  EB E1                           jmp 0x1404f4650
004F466F  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
004F4674  49 8B CE                        mov rcx, r14
004F4677  E8 E4 DA 57 00                  call 0x140a72160
004F467C  8B D8                           mov ebx, eax
004F467E  85 C0                           test eax, eax
004F4680  0F 88 11 FF FF FF               js 0x1404f4597
004F4686  83 7C 24 58 01                  cmp dword ptr [rsp + 0x58], 1
004F468B  75 2A                           jne 0x1404f46b7
004F468D  48 8D 44 24 50                  lea rax, [rsp + 0x50]
004F4692  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004F4697  4D 8B C5                        mov r8, r13
004F469A  8B D6                           mov edx, esi
004F469C  49 8B CF                        mov rcx, r15
004F469F  E8 6C 03 5B 00                  call 0x140aa4a10
004F46A4  8B D8                           mov ebx, eax
004F46A6  80 7C 24 50 00                  cmp byte ptr [rsp + 0x50], 0
004F46AB  75 0A                           jne 0x1404f46b7
004F46AD  BB 22 00 00 C0                  mov ebx, 0xc0000022
004F46B2  E9 E0 FE FF FF                  jmp 0x1404f4597
004F46B7  85 DB                           test ebx, ebx
004F46B9  0F 88 D8 FE FF FF               js 0x1404f4597
004F46BF  E8 60 06 00 00                  call 0x1404f4d24
004F46C4  85 C0                           test eax, eax
004F46C6  0F 84 02 01 00 00               je 0x1404f47ce
004F46CC  83 64 24 5C 00                  and dword ptr [rsp + 0x5c], 0
004F46D1  48 8D 4C 24 5C                  lea rcx, [rsp + 0x5c]
004F46D6  E8 D5 C5 56 00                  call 0x140a60cb0
004F46DB  8B 44 24 5C                     mov eax, dword ptr [rsp + 0x5c]
004F46DF  24 18                           and al, 0x18
004F46E1  3C 10                           cmp al, 0x10
004F46E3  0F 85 E5 00 00 00               jne 0x1404f47ce
004F46E9  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004F46F2  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
004F46F9  90                              nop
004F46FA  B2 01                           mov dl, 1
004F46FC  49 8B 4F 30                     mov rcx, qword ptr [r15 + 0x30]
004F4700  E8 BB D4 D1 FF                  call 0x140211bc0
004F4705  49 8B CF                        mov rcx, r15
004F4708  E8 03 78 F2 FF                  call 0x14041bf10
004F470D  48 85 C0                        test rax, rax
004F4710  0F 84 A2 00 00 00               je 0x1404f47b8
004F4716  48 8B 08                        mov rcx, qword ptr [rax]
004F4719  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
004F471D  84 C0                           test al, al
004F471F  0F 84 93 00 00 00               je 0x1404f47b8
004F4725  FF C8                           dec eax
004F4727  81 7C 81 08 00 30 00 00         cmp dword ptr [rcx + rax*4 + 8], 0x3000
004F472F  0F 82 83 00 00 00               jb 0x1404f47b8
004F4735  0F 57 C0                        xorps xmm0, xmm0
004F4738  0F 11 84 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm0
004F4740  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
004F4748  48 8D 8C 24 C0 00 00 00         lea rcx, [rsp + 0xc0]
004F4750  E8 CB 70 37 00                  call 0x14086b820
004F4755  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004F475E  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
004F4765  90                              nop
004F4766  48 8B BC 24 D0 00 00 00         mov rdi, qword ptr [rsp + 0xd0]
004F476E  B2 01                           mov dl, 1
004F4770  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
004F4774  E8 47 D4 D1 FF                  call 0x140211bc0
004F4779  48 8B CF                        mov rcx, rdi
004F477C  E8 8F 77 F2 FF                  call 0x14041bf10
004F4781  48 8B 08                        mov rcx, qword ptr [rax]
004F4784  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
004F4788  84 C0                           test al, al
004F478A  74 0C                           je 0x1404f4798
004F478C  FF C8                           dec eax
004F478E  81 7C 81 08 00 30 00 00         cmp dword ptr [rcx + rax*4 + 8], 0x3000
004F4796  73 05                           jae 0x1404f479d
004F4798  BB 22 00 00 C0                  mov ebx, 0xc0000022
004F479D  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
004F47A1  E8 6A B2 D6 FF                  call 0x14025fa10
004F47A6  E8 05 91 D6 FF                  call 0x14025d8b0
004F47AB  48 8D 8C 24 C0 00 00 00         lea rcx, [rsp + 0xc0]
004F47B3  E8 58 6F 37 00                  call 0x14086b710
004F47B8  49 8B 4F 30                     mov rcx, qword ptr [r15 + 0x30]
004F47BC  E8 4F B2 D6 FF                  call 0x14025fa10
004F47C1  E8 EA 90 D6 FF                  call 0x14025d8b0
004F47C6  85 DB                           test ebx, ebx
004F47C8  0F 88 C9 FD FF FF               js 0x1404f4597
004F47CE  48 8D 44 24 48                  lea rax, [rsp + 0x48]
004F47D3  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
004F47D8  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
004F47DD  8A 84 24 30 01 00 00            mov al, byte ptr [rsp + 0x130]
004F47E4  88 44 24 28                     mov byte ptr [rsp + 0x28], al
004F47E8  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
004F47ED  41 B9 01 00 00 00               mov r9d, 1
004F47F3  45 33 C0                        xor r8d, r8d
004F47F6  49 8B D4                        mov rdx, r12
004F47F9  49 8B CF                        mov rcx, r15
004F47FC  E8 EB 3F 3C 00                  call 0x1408b87ec
004F4801  8B D8                           mov ebx, eax
004F4803  45 33 E4                        xor r12d, r12d
004F4806  85 C0                           test eax, eax
004F4808  0F 88 89 FD FF FF               js 0x1404f4597
004F480E  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
004F4813  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
004F4818  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
004F481D  E8 AA A5 56 00                  call 0x140a5edcc
004F4822  8B D8                           mov ebx, eax
004F4824  85 C0                           test eax, eax
004F4826  0F 88 6B FD FF FF               js 0x1404f4597
004F482C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004F4835  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
004F483C  90                              nop
004F483D  B2 01                           mov dl, 1
004F483F  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
004F4844  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
004F4848  E8 D3 05 D2 FF                  call 0x140214e20
004F484D  F0 44 09 24 24                  lock or dword ptr [rsp], r12d
004F4852  C6 44 24 41 01                  mov byte ptr [rsp + 0x41], 1
004F4857  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
004F485C  E8 AF 76 F2 FF                  call 0x14041bf10
004F4861  48 8B F8                        mov rdi, rax
004F4864  48 85 C0                        test rax, rax
004F4867  0F 84 44 02 00 00               je 0x1404f4ab1
004F486D  4C 8B 00                        mov r8, qword ptr [rax]
004F4870  45 0F B6 48 01                  movzx r9d, byte ptr [r8 + 1]
004F4875  45 84 C9                        test r9b, r9b
004F4878  0F 84 AE 01 00 00               je 0x1404f4a2c
004F487E  48 8B B4 24 38 01 00 00         mov rsi, qword ptr [rsp + 0x138]
004F4886  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
004F488A  8B 51 04                        mov edx, dword ptr [rcx + 4]
004F488D  F6 C2 01                        test dl, 1
004F4890  74 12                           je 0x1404f48a4
004F4892  41 8D 49 FF                     lea ecx, [r9 - 1]
004F4896  41 C7 44 88 08 00 10 00 00      mov dword ptr [r8 + rcx*4 + 8], 0x1000
004F489F  E9 84 01 00 00                  jmp 0x1404f4a28
004F48A4  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
004F48A9  E8 72 6F 37 00                  call 0x14086b820
004F48AE  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
004F48B3  E8 08 1C 3D 00                  call 0x1408c64c0
004F48B8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004F48C1  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
004F48C8  90                              nop
004F48C9  B2 01                           mov dl, 1
004F48CB  49 8B 4F 30                     mov rcx, qword ptr [r15 + 0x30]
004F48CF  E8 EC D2 D1 FF                  call 0x140211bc0
004F48D4  49 8B CF                        mov rcx, r15
004F48D7  E8 34 76 F2 FF                  call 0x14041bf10
004F48DC  48 85 C0                        test rax, rax
004F48DF  74 46                           je 0x1404f4927
004F48E1  48 8B 08                        mov rcx, qword ptr [rax]
004F48E4  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
004F48E8  84 C0                           test al, al
004F48EA  75 05                           jne 0x1404f48f1
004F48EC  41 8B CC                        mov ecx, r12d
004F48EF  EB 06                           jmp 0x1404f48f7
004F48F1  FF C8                           dec eax
004F48F3  8B 4C 81 08                     mov ecx, dword ptr [rcx + rax*4 + 8]
004F48F7  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
004F48FB  39 48 28                        cmp dword ptr [rax + 0x28], ecx
004F48FE  76 27                           jbe 0x1404f4927
004F4900  49 8B 4F 30                     mov rcx, qword ptr [r15 + 0x30]
004F4904  E8 07 B1 D6 FF                  call 0x14025fa10
004F4909  E8 A2 8F D6 FF                  call 0x14025d8b0
004F490E  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
004F4913  E8 08 1C 3D 00                  call 0x1408c6520
004F4918  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
004F491D  E8 EE 6D 37 00                  call 0x14086b710
004F4922  E9 86 FD FF FF                  jmp 0x1404f46ad
004F4927  49 8B 4F 30                     mov rcx, qword ptr [r15 + 0x30]
004F492B  E8 E0 B0 D6 FF                  call 0x14025fa10
004F4930  E8 7B 8F D6 FF                  call 0x14025d8b0
004F4935  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
004F493D  E8 CE 75 F2 FF                  call 0x14041bf10
004F4942  48 85 C0                        test rax, rax
004F4945  0F 84 B8 00 00 00               je 0x1404f4a03
004F494B  48 8B 08                        mov rcx, qword ptr [rax]
004F494E  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
004F4952  84 C0                           test al, al
004F4954  75 05                           jne 0x1404f495b
004F4956  41 8B CC                        mov ecx, r12d
004F4959  EB 06                           jmp 0x1404f4961
004F495B  FF C8                           dec eax
004F495D  8B 4C 81 08                     mov ecx, dword ptr [rcx + rax*4 + 8]
004F4961  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
004F4965  8B 50 28                        mov edx, dword ptr [rax + 0x28]
004F4968  3B CA                           cmp ecx, edx
004F496A  72 A2                           jb 0x1404f490e
004F496C  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
004F4971  48 85 C9                        test rcx, rcx
004F4974  74 7E                           je 0x1404f49f4
004F4976  83 B9 C0 00 00 00 02            cmp dword ptr [rcx + 0xc0], 2
004F497D  75 09                           jne 0x1404f4988
004F497F  83 B9 C4 00 00 00 02            cmp dword ptr [rcx + 0xc4], 2
004F4986  7C 86                           jl 0x1404f490e
004F4988  E8 83 75 F2 FF                  call 0x14041bf10
004F498D  4C 8B 08                        mov r9, qword ptr [rax]
004F4990  45 0F B6 41 01                  movzx r8d, byte ptr [r9 + 1]
004F4995  45 8B D0                        mov r10d, r8d
004F4998  45 84 C0                        test r8b, r8b
004F499B  75 05                           jne 0x1404f49a2
004F499D  41 8B C4                        mov eax, r12d
004F49A0  EB 09                           jmp 0x1404f49ab
004F49A2  41 8D 40 FF                     lea eax, [r8 - 1]
004F49A6  41 8B 44 81 08                  mov eax, dword ptr [r9 + rax*4 + 8]
004F49AB  3B C2                           cmp eax, edx
004F49AD  73 15                           jae 0x1404f49c4
004F49AF  45 84 C0                        test r8b, r8b
004F49B2  75 05                           jne 0x1404f49b9
004F49B4  41 8B C4                        mov eax, r12d
004F49B7  EB 0D                           jmp 0x1404f49c6
004F49B9  41 8D 42 FF                     lea eax, [r10 - 1]
004F49BD  41 8B 44 81 08                  mov eax, dword ptr [r9 + rax*4 + 8]
004F49C2  EB 02                           jmp 0x1404f49c6
004F49C4  8B C2                           mov eax, edx
004F49C6  3B D0                           cmp edx, eax
004F49C8  72 2A                           jb 0x1404f49f4
004F49CA  45 84 C0                        test r8b, r8b
004F49CD  75 05                           jne 0x1404f49d4
004F49CF  41 8B C4                        mov eax, r12d
004F49D2  EB 09                           jmp 0x1404f49dd
004F49D4  41 8D 42 FF                     lea eax, [r10 - 1]
004F49D8  41 8B 44 81 08                  mov eax, dword ptr [r9 + rax*4 + 8]
004F49DD  3B C2                           cmp eax, edx
004F49DF  73 13                           jae 0x1404f49f4
004F49E1  45 84 C0                        test r8b, r8b
004F49E4  75 05                           jne 0x1404f49eb
004F49E6  41 8B D4                        mov edx, r12d
004F49E9  EB 09                           jmp 0x1404f49f4
004F49EB  41 8D 40 FF                     lea eax, [r8 - 1]
004F49EF  41 8B 54 81 08                  mov edx, dword ptr [r9 + rax*4 + 8]
004F49F4  48 8B 0F                        mov rcx, qword ptr [rdi]
004F49F7  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
004F49FB  FF C8                           dec eax
004F49FD  89 54 81 08                     mov dword ptr [rcx + rax*4 + 8], edx
004F4A01  EB 11                           jmp 0x1404f4a14
004F4A03  48 8B 17                        mov rdx, qword ptr [rdi]
004F4A06  0F B6 42 01                     movzx eax, byte ptr [rdx + 1]
004F4A0A  FF C8                           dec eax
004F4A0C  C7 44 82 08 00 10 00 00         mov dword ptr [rdx + rax*4 + 8], 0x1000
004F4A14  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
004F4A19  E8 02 1B 3D 00                  call 0x1408c6520
004F4A1E  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
004F4A23  E8 E8 6C 37 00                  call 0x14086b710
004F4A28  8B 74 24 54                     mov esi, dword ptr [rsp + 0x54]
004F4A2C  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
004F4A31  48 B9 00 00 80 00 02 00 00 00   movabs rcx, 0x200800000
004F4A3B  48 21 48 48                     and qword ptr [rax + 0x48], rcx
004F4A3F  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
004F4A44  48 21 48 50                     and qword ptr [rax + 0x50], rcx
004F4A48  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
004F4A4D  48 21 48 40                     and qword ptr [rax + 0x40], rcx
004F4A51  48 8B 0F                        mov rcx, qword ptr [rdi]
004F4A54  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
004F4A58  84 C0                           test al, al
004F4A5A  74 0C                           je 0x1404f4a68
004F4A5C  FF C8                           dec eax
004F4A5E  81 7C 81 08 00 20 00 00         cmp dword ptr [rcx + rax*4 + 8], 0x2000
004F4A66  73 0D                           jae 0x1404f4a75
004F4A68  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
004F4A6D  0F BA B0 C8 00 00 00 0D         btr dword ptr [rax + 0xc8], 0xd
004F4A75  E8 6E 2E FD FF                  call 0x1404c78e8
004F4A7A  85 C0                           test eax, eax
004F4A7C  74 24                           je 0x1404f4aa2
004F4A7E  48 8B 0F                        mov rcx, qword ptr [rdi]
004F4A81  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
004F4A85  84 C0                           test al, al
004F4A87  74 0C                           je 0x1404f4a95
004F4A89  FF C8                           dec eax
004F4A8B  81 7C 81 08 00 30 00 00         cmp dword ptr [rcx + rax*4 + 8], 0x3000
004F4A93  73 0D                           jae 0x1404f4aa2
004F4A95  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
004F4A9A  0F BA B0 C8 00 00 00 0C         btr dword ptr [rax + 0xc8], 0xc
004F4AA2  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
004F4AA7  0F BA A8 C8 00 00 00 0E         bts dword ptr [rax + 0xc8], 0xe
004F4AAF  EB 05                           jmp 0x1404f4ab6
004F4AB1  BB 46 04 00 C0                  mov ebx, 0xc0000446
004F4AB6  85 DB                           test ebx, ebx
004F4AB8  0F 88 D9 FA FF FF               js 0x1404f4597
004F4ABE  44 8B CE                        mov r9d, esi
004F4AC1  4D 8B C5                        mov r8, r13
004F4AC4  49 8B D6                        mov rdx, r14
004F4AC7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
004F4ACC  E8 23 50 4D 00                  call 0x1409c9af4
004F4AD1  8B D8                           mov ebx, eax
004F4AD3  85 C0                           test eax, eax
004F4AD5  0F 88 E9 01 00 00               js 0x1404f4cc4
004F4ADB  49 8B D6                        mov rdx, r14
004F4ADE  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
004F4AE3  E8 84 02 57 00                  call 0x140a64d6c
004F4AE8  8B D8                           mov ebx, eax
004F4AEA  85 C0                           test eax, eax
004F4AEC  0F 88 D2 01 00 00               js 0x1404f4cc4
004F4AF2  4C 89 B4 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r14
004F4AFA  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
004F4B02  4C 8B 48 10                     mov r9, qword ptr [rax + 0x10]
004F4B06  44 8B 40 18                     mov r8d, dword ptr [rax + 0x18]
004F4B0A  48 8D 94 24 A8 00 00 00         lea rdx, [rsp + 0xa8]
004F4B12  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
004F4B17  E8 80 48 4B 00                  call 0x1409a939c
004F4B1C  8B D8                           mov ebx, eax
004F4B1E  85 C0                           test eax, eax
004F4B20  0F 88 9E 01 00 00               js 0x1404f4cc4
004F4B26  49 8B D6                        mov rdx, r14
004F4B29  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
004F4B2E  E8 85 C1 52 00                  call 0x140a20cb8
004F4B33  8B D8                           mov ebx, eax
004F4B35  85 C0                           test eax, eax
004F4B37  0F 88 87 01 00 00               js 0x1404f4cc4
004F4B3D  49 8B D6                        mov rdx, r14
004F4B40  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
004F4B45  E8 AE B7 F0 FF                  call 0x1404002f8
004F4B4A  8B D8                           mov ebx, eax
004F4B4C  85 C0                           test eax, eax
004F4B4E  0F 88 70 01 00 00               js 0x1404f4cc4
004F4B54  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
004F4B59  48 8D 8F 28 03 00 00            lea rcx, [rdi + 0x328]
004F4B60  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
004F4B65  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
004F4B6A  45 33 C9                        xor r9d, r9d
004F4B6D  4C 8B 05 0C 0C A1 00            mov r8, qword ptr [rip + 0xa10c0c]
004F4B74  33 D2                           xor edx, edx
004F4B76  E8 65 3A ED FF                  call 0x1403c85e0
004F4B7B  84 C0                           test al, al
004F4B7D  74 18                           je 0x1404f4b97
004F4B7F  F0 FF 05 52 4F AE 00            lock inc dword ptr [rip + 0xae4f52]
004F4B86  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
004F4B8B  81 88 C8 00 00 00 00 00 00 03   or dword ptr [rax + 0xc8], 0x3000000
004F4B95  EB 49                           jmp 0x1404f4be0
004F4B97  81 A7 C8 00 00 00 FF FF FF FC   and dword ptr [rdi + 0xc8], 0xfcffffff
004F4BA1  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
004F4BA6  48 81 C1 28 03 00 00            add rcx, 0x328
004F4BAD  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
004F4BB2  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
004F4BB7  45 33 C9                        xor r9d, r9d
004F4BBA  4C 8B 05 CF 0B A1 00            mov r8, qword ptr [rip + 0xa10bcf]
004F4BC1  33 D2                           xor edx, edx
004F4BC3  E8 18 3A ED FF                  call 0x1403c85e0
004F4BC8  84 C0                           test al, al
004F4BCA  74 14                           je 0x1404f4be0
004F4BCC  F0 FF 05 05 4F AE 00            lock inc dword ptr [rip + 0xae4f05]
004F4BD3  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
004F4BD8  0F BA A8 C8 00 00 00 18         bts dword ptr [rax + 0xc8], 0x18
004F4BE0  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
004F4BE5  48 8B 0D 1C E1 B1 FF            mov rcx, qword ptr [rip - 0x4e1ee4]
004F4BEC  48 8B C1                        mov rax, rcx
004F4BEF  F0 48 0F C1 05 F8 9F 91 00      lock xadd qword ptr [rip + 0x919ff8], rax
004F4BF8  48 03 C1                        add rax, rcx
004F4BFB  89 42 38                        mov dword ptr [rdx + 0x38], eax
004F4BFE  48 C1 E8 20                     shr rax, 0x20
004F4C02  89 42 3C                        mov dword ptr [rdx + 0x3c], eax
004F4C05  F0 44 09 24 24                  lock or dword ptr [rsp], r12d
004F4C0A  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
004F4C0F  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
004F4C13  E8 F8 AD D6 FF                  call 0x14025fa10
004F4C18  E8 93 8C D6 FF                  call 0x14025d8b0
004F4C1D  44 88 64 24 41                  mov byte ptr [rsp + 0x41], r12b
004F4C22  48 8B BC 24 10 01 00 00         mov rdi, qword ptr [rsp + 0x110]
004F4C2A  48 85 FF                        test rdi, rdi
004F4C2D  74 72                           je 0x1404f4ca1
004F4C2F  48 8D 44 24 68                  lea rax, [rsp + 0x68]
004F4C34  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004F4C39  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
004F4C3E  41 B9 01 00 00 00               mov r9d, 1
004F4C44  44 8B 44 24 64                  mov r8d, dword ptr [rsp + 0x64]
004F4C49  33 D2                           xor edx, edx
004F4C4B  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
004F4C50  E8 AB 44 3C 00                  call 0x1408b9100
004F4C55  8B D8                           mov ebx, eax
004F4C57  85 C0                           test eax, eax
004F4C59  79 10                           jns 0x1404f4c6b
004F4C5B  45 8A F4                        mov r14b, r12b
004F4C5E  48 8B B4 24 18 01 00 00         mov rsi, qword ptr [rsp + 0x118]
004F4C66  E9 41 F9 FF FF                  jmp 0x1404f45ac
004F4C6B  4D 8B C6                        mov r8, r14
004F4C6E  BA FF 01 0F 00                  mov edx, 0xf01ff
004F4C73  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
004F4C78  E8 B3 17 3C 00                  call 0x1408b6430
004F4C7D  8B D8                           mov ebx, eax
004F4C7F  85 C0                           test eax, eax
004F4C81  78 49                           js 0x1404f4ccc
004F4C83  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
004F4C88  E8 67 17 3C 00                  call 0x1408b63f4
004F4C8D  BA 44 66 6C 74                  mov edx, 0x746c6644
004F4C92  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
004F4C97  E8 44 2C E0 FF                  call 0x1402f78e0
004F4C9C  45 8A F4                        mov r14b, r12b
004F4C9F  EB 05                           jmp 0x1404f4ca6
004F4CA1  44 8A 74 24 40                  mov r14b, byte ptr [rsp + 0x40]
004F4CA6  48 8B B4 24 18 01 00 00         mov rsi, qword ptr [rsp + 0x118]
004F4CAE  48 85 F6                        test rsi, rsi
004F4CB1  0F 84 F5 F8 FF FF               je 0x1404f45ac
004F4CB7  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
004F4CBC  48 89 06                        mov qword ptr [rsi], rax
004F4CBF  E9 E8 F8 FF FF                  jmp 0x1404f45ac
004F4CC4  48 8B BC 24 10 01 00 00         mov rdi, qword ptr [rsp + 0x110]
004F4CCC  48 8B B4 24 18 01 00 00         mov rsi, qword ptr [rsp + 0x118]
004F4CD4  E9 CE F8 FF FF                  jmp 0x1404f45a7
004F4CD9  48 85 F6                        test rsi, rsi
004F4CDC  74 08                           je 0x1404f4ce6
004F4CDE  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
004F4CE3  48 89 06                        mov qword ptr [rsi], rax
004F4CE6  EB 02                           jmp 0x1404f4cea
004F4CE8  EB 14                           jmp 0x1404f4cfe
004F4CEA  4D 85 FF                        test r15, r15
004F4CED  74 0D                           je 0x1404f4cfc
004F4CEF  BA 44 66 6C 74                  mov edx, 0x746c6644
004F4CF4  49 8B CF                        mov rcx, r15
004F4CF7  E8 E4 2B E0 FF                  call 0x1402f78e0
004F4CFC  8B C3                           mov eax, ebx
004F4CFE  4C 8D 9C 24 E0 00 00 00         lea r11, [rsp + 0xe0]
004F4D06  49 8B 5B 40                     mov rbx, qword ptr [r11 + 0x40]
004F4D0A  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
004F4D0E  49 8B E3                        mov rsp, r11
004F4D11  41 5F                           pop r15
004F4D13  41 5E                           pop r14
004F4D15  41 5D                           pop r13
004F4D17  41 5C                           pop r12
004F4D19  5F                              pop rdi
004F4D1A  C3                              ret
004F4D1B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepCreateAppContainerToken(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned __int8 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m64;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned __int64 v_stack_mB7;
    unsigned __int8 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int8 v_stack_mC7;
    unsigned __int8 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int8 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (224);
    v_rbx = 0;
    v_stack_mB0 = 0;
    v_stack_mA0 = 0;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 96) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 80) = 0;
    v_stack_mB8 = 0;
    v_stack_mC8 = 0;
    *(unsigned __int64 *)(v_rsp - 112) = 0;
    v_stack_mC0 = 0;
    v_stack_mA8 = 1;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    v_stack_mC7 = 0;
    v_stack_mB4 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a6 + 8) + 32)));
    if (a1 != 0) goto loc_004F4448;
    if (a2 == 0) goto loc_004F4452;
    if (a1 == 0) goto loc_004F444D;
loc_004F4448:
    if (a2 != 0) goto loc_004F4452;
loc_004F444D:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 16) != 0) goto loc_004F445C;
loc_004F4452:
    goto loc_004F4CFE;
loc_004F445C:
    if (*(unsigned __int64 *)((unsigned int)(0xC000000DULL) + 8) == 0) goto loc_004F44B2;
    v_stack_m78 = 0;
    v_stack_mE0 = v_stack_m70;
    v_stack_mE8 = v_stack_m78;
    result = ObReferenceObjectByHandle(*(unsigned __int64 *)((unsigned int)(0xC000000DULL) + 8), 2, *(unsigned __int64 *)(v_rip + 11418548), a5);
    if (sign_flag) goto loc_004F4CFE;
    goto loc_004F44E7;
loc_004F44B2:
    v_stack_mE0 = 0;
    v_stack_mE8 = v_stack_m68;
    result = PsReferenceEffectiveToken(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(0x74726853ULL), v_stack_m64, v_stack_mB7);
loc_004F44E7:
    result = SepCheckCreateAppContainer(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 16), (unsigned int)(0x74726853ULL), v_stack_m64, v_stack_mB7);
    if (sign_flag) goto loc_004F459F;
    if ((*(unsigned int *)(result + 192)) == 1) goto loc_004F4517;
    if ((*(unsigned int *)(result + 196)) >= 2) goto loc_004F4517;
    goto loc_004F459F;
loc_004F4517:
    result = (unsigned int)(v_stack_m6C);
    if ((unsigned int)((unsigned int)(a3)) != 0) { result = (unsigned int)((unsigned int)(a3)); }
    v_stack_mA4 = (unsigned int)(result);
    result = RtlIsPackageSid(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 16), (unsigned int)(0x74726853ULL), v_stack_m64, v_stack_mB7);
    if ((unsigned __int8)(result) != 0) goto loc_004F453A;
    goto loc_004F459F;
loc_004F453A:
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 16) + 1)) - (8));
    if ((((unsigned __int8)(result)) & (251)) == 0) goto loc_004F454B;
    goto loc_004F459F;
loc_004F454B:
    v_rbx = 0;
loc_004F454D:
    if (0 >= ((unsigned int)((unsigned int)(v_stack_mB4)))) goto loc_004F4640;
    v_rsi = (0) + (0);
    result = RtlIsCapabilitySid(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24) + v_rsi * 8), (unsigned int)(0x74726853ULL), v_stack_m64, v_stack_mB7);
    if ((unsigned __int8)(result) == 0) goto loc_004F4592;
    v_rdi = 0;
loc_004F456E:
    if (0 >= 0) goto loc_004F458E;
    a2 = (0) + (0);
    result = RtlEqualSid(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24) + v_rsi * 8), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24) + a2 * 8), v_stack_m64, v_stack_mB7);
    if ((unsigned __int8)(result) != 0) goto loc_004F4592;
    v_rdi = (unsigned int)((v_rdi) + 1);
    goto loc_004F456E;
loc_004F458E:
    v_rbx = (unsigned int)((v_rbx) + 1);
    goto loc_004F454D;
loc_004F4592:
loc_004F4597:
loc_004F459F:
loc_004F45A7:
loc_004F45AC:
    if (v_stack_mC7 == 0) goto loc_004F45F4;
    if (!(sign_flag)) {
        a2 = v_stack_mC0;
        a1 = *(unsigned __int64 *)(v_rip - 5118139);
        result = a1;
        result = (result) + (a1);
        *(unsigned int *)(a2 + 56) = (unsigned int)(result);
        result = (result) >> (32);
        *(unsigned int *)(a2 + 60) = (unsigned int)(result);
    }
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_mC0 + 48), a2, v_stack_m64, v_stack_mB7);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_mC0 + 48), a2, v_stack_m64, v_stack_mB7);
loc_004F45F4:
    if (!sign_flag) goto loc_004F462A;
    if ((unsigned __int8)(v_stack_mC8) != 0) {
        a2 = 0x746C6644ULL;
        a1 = v_stack_mC0;
        result = ObfDereferenceObjectWithTag(a1, a2, v_stack_m64, v_stack_mB7);
    }
    if (v_stack_mA0 != 0) {
        a2 = a5;
        result = ObCloseHandle(v_stack_mA0, a2, v_stack_m64, v_stack_mB7);
    }
    if (sign_flag) goto loc_004F4CEA;
loc_004F462A:
    if (v_stack_p8 == 0) goto loc_004F4CD9;
    *(unsigned __int64 *)(v_stack_p8) = v_stack_mA0;
    goto loc_004F4CE6;
loc_004F4640:
    result = SepCapabilitiesHasAppSiloBaseSID((unsigned int)((unsigned int)(v_stack_p10)), *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24), v_stack_m64, v_stack_mB7);
    if ((unsigned __int8)(result) != 0) goto loc_004F466F;
    v_rbx = 0;
loc_004F4650:
    if (0 >= ((unsigned int)(v_stack_p10))) goto loc_004F466F;
    a1 = (0) + (0);
    result = SepIsAppSiloCapability(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24) + a1 * 8), *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24), v_stack_m64, v_stack_mB7);
    if ((unsigned __int8)(result) != 0) goto loc_004F4592;
    v_rbx = (unsigned int)((v_rbx) + 1);
    goto loc_004F4650;
loc_004F466F:
    result = RtlGetAppContainerSidType(v_stack_mC8, v_stack_mB0, v_stack_m64, v_stack_mB7);
    if (sign_flag) goto loc_004F4597;
    if (v_stack_mB0 != 1) goto loc_004F46B7;
    v_stack_mE8 = v_stack_mB8;
    result = SepCheckCapabilities(result, (unsigned int)((unsigned int)(v_stack_p10)), *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24), v_stack_mB7);
    if (v_stack_mB8 != 0) goto loc_004F46B7;
loc_004F46AD:
    goto loc_004F4597;
loc_004F46B7:
    if (sign_flag) goto loc_004F4597;
    result = Feature_871661881__private_IsEnabledDeviceUsageNoInline(result, (unsigned int)((unsigned int)(v_stack_p10)), *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24), v_stack_mB7);
    if ((unsigned int)(result) == 0) goto loc_004F47CE;
    result = RtlQueryElevationFlags(v_stack_mAC, (unsigned int)((unsigned int)(v_stack_p10)), *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24), v_stack_mB7);
    result = (unsigned __int8)(((unsigned int)(v_stack_mAC)) & (24));
    if (((unsigned __int8)(result)) != 16) goto loc_004F47CE;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(result + 48), 1, *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24), v_stack_mB7);
    result = SepLocateTokenIntegrity(result, 1, *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24), v_stack_mB7);
    if (result == 0) goto loc_004F47B8;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) == 0) goto loc_004F47B8;
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) - 1);
    if ((*(unsigned int *)(*(unsigned __int64 *)(result) + result * 4 + 8)) < 0x3000ULL) goto loc_004F47B8;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = SeCaptureSubjectContext(v_stack_m48, 1, *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24), v_stack_mB7);
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m38 + 48), 1, *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24), v_stack_mB7);
    result = SepLocateTokenIntegrity(v_stack_m38, 1, *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24), v_stack_mB7);
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) == 0) goto loc_004F4798;
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) - 1);
    v_rbx = (unsigned int)(0xC0000022ULL);
    if ((*(unsigned int *)(*(unsigned __int64 *)(result) + result * 4 + 8)) < 0x3000ULL) {
        v_rbx = 0xC0000022ULL;
    }
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m38 + 48), 1, *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24), v_stack_mB7);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m38 + 48), 1, *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24), v_stack_mB7);
    result = SeReleaseSubjectContext(v_stack_m48, 1, *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24), v_stack_mB7);
loc_004F47B8:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(result + 48), 1, *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24), v_stack_mB7);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(result + 48), 1, *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24), v_stack_mB7);
    if (sign_flag) goto loc_004F4597;
loc_004F47CE:
    v_stack_mD0 = v_stack_mC0;
    v_stack_mD8 = 0;
    v_stack_mE0 = a5;
    a3 = 0;
    result = SepDuplicateToken(result, a4, a3, 1);
    v_r12 = 0;
    if (sign_flag) goto loc_004F4597;
    v_stack_mC8 = 1;
    result = SeSetMandatoryPolicyToken(v_stack_mC0, v_stack_mA8, a3, 1);
    if (sign_flag) goto loc_004F4597;
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_stack_mC0 + 48), 1, a3, 1);
    v_stack_mC7 = 1;
    result = SepLocateTokenIntegrity(v_stack_mC0, 1, a3, 1);
    if (result == 0) goto loc_004F4AB1;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) == 0) goto loc_004F4A2C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a6 + 8) + 4)))) & (1)) == 0) goto loc_004F48A4;
    *(unsigned int *)(*(unsigned __int64 *)(result) + *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1) - 1 * 4 + 8) = 0x1000ULL;
    goto loc_004F4A28;
loc_004F48A4:
    result = SeCaptureSubjectContext(v_stack_m98, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a6 + 8) + 4)), *(unsigned __int64 *)(result), *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1));
    result = SeLockSubjectContext(v_stack_m98, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a6 + 8) + 4)), *(unsigned __int64 *)(result), *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1));
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(result + 48), 1, *(unsigned __int64 *)(result), *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1));
    result = SepLocateTokenIntegrity(result, 1, *(unsigned __int64 *)(result), *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1));
    if (result == 0) goto loc_004F4927;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) != 0) goto loc_004F48F1;
    goto loc_004F48F7;
loc_004F48F1:
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) - 1);
loc_004F48F7:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a6 + 8) + 40)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(0 + result * 4 + 8))))) goto loc_004F4927;
    result = ExReleaseResourceLite(*(unsigned __int64 *)(result + 48), 1, *(unsigned __int64 *)(result), *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1));
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(result + 48), 1, *(unsigned __int64 *)(result), *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1));
loc_004F490E:
    result = SeUnlockSubjectContext(v_stack_m98, 1, *(unsigned __int64 *)(result), *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1));
    result = SeReleaseSubjectContext(v_stack_m98, 1, *(unsigned __int64 *)(result), *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1));
    goto loc_004F46AD;
loc_004F4927:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(result + 48), 1, *(unsigned __int64 *)(result), *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1));
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(result + 48), 1, *(unsigned __int64 *)(result), *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1));
    result = SepLocateTokenIntegrity(v_stack_m88, 1, *(unsigned __int64 *)(result), *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1));
    if (result == 0) goto loc_004F4A03;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) != 0) goto loc_004F495B;
    goto loc_004F4961;
loc_004F495B:
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) - 1);
loc_004F4961:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(0 + result * 4 + 8)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a6 + 8) + 40))))) goto loc_004F490E;
    if (v_stack_m98 == 0) goto loc_004F49F4;
    if ((*(unsigned int *)(v_stack_m98 + 192)) != 2) goto loc_004F4988;
    if ((*(unsigned int *)(v_stack_m98 + 196)) < 2) goto loc_004F490E;
loc_004F4988:
    result = SepLocateTokenIntegrity(v_stack_m98, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a6 + 8) + 40)), *(unsigned __int64 *)(result), *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) != 0) goto loc_004F49A2;
    goto loc_004F49AB;
loc_004F49A2:
loc_004F49AB:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result) + *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1) - 1 * 4 + 8)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a6 + 8) + 40))))) goto loc_004F49C4;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) != 0) goto loc_004F49B9;
    goto loc_004F49C6;
loc_004F49B9:
    goto loc_004F49C6;
loc_004F49C4:
loc_004F49C6:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a6 + 8) + 40)))) < ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a6 + 8) + 40))))))) goto loc_004F49F4;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) != 0) goto loc_004F49D4;
    goto loc_004F49DD;
loc_004F49D4:
loc_004F49DD:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result) + (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1))) - 1 * 4 + 8)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a6 + 8) + 40))))) goto loc_004F49F4;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) != 0) goto loc_004F49EB;
    goto loc_004F49F4;
loc_004F49EB:
loc_004F49F4:
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) - 1);
    *(unsigned int *)(*(unsigned __int64 *)(result) + result * 4 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result) + *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1) - 1 * 4 + 8)));
    goto loc_004F4A14;
loc_004F4A03:
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) - 1);
    *(unsigned int *)(*(unsigned __int64 *)(result) + result * 4 + 8) = 0x1000ULL;
loc_004F4A14:
    result = SeUnlockSubjectContext(v_stack_m98, *(unsigned __int64 *)(result), *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1), *(unsigned __int64 *)(result));
    result = SeReleaseSubjectContext(v_stack_m98, *(unsigned __int64 *)(result), *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1), *(unsigned __int64 *)(result));
loc_004F4A28:
loc_004F4A2C:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) == 0) goto loc_004F4A68;
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) - 1);
    if ((*(unsigned int *)(*(unsigned __int64 *)(result) + result * 4 + 8)) < 0x2000ULL) {
        result = v_stack_mC0;
    }
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(result), *(unsigned __int64 *)(result), *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1), *(unsigned __int64 *)(result));
    if ((unsigned int)(result) == 0) goto loc_004F4AA2;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) == 0) goto loc_004F4A95;
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) - 1);
    if ((*(unsigned int *)(*(unsigned __int64 *)(result) + result * 4 + 8)) < 0x3000ULL) {
        result = v_stack_mC0;
    }
    goto loc_004F4AB6;
loc_004F4AB1:
loc_004F4AB6:
    if (sign_flag) goto loc_004F4597;
    result = SepSetTokenCapabilities(v_stack_mC0, v_stack_mC8, *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24), (unsigned int)((unsigned int)((unsigned int)(v_stack_mB4))));
    if (sign_flag) goto loc_004F4CC4;
    result = SepSetTokenLowboxNumber(v_stack_mC0, v_stack_mC8, *(unsigned __int64 *)(*(unsigned __int64 *)(a6 + 8) + 24), (unsigned int)((unsigned int)((unsigned int)(v_stack_mB4))));
    if (sign_flag) goto loc_004F4CC4;
    v_stack_m58 = v_stack_mC8;
    result = SepSetTokenCachedHandles(v_stack_mC0, v_stack_m60, (unsigned int)(*(unsigned int *)(a6 + 24)), *(unsigned __int64 *)(a6 + 16));
    if (sign_flag) goto loc_004F4CC4;
    result = SepSetTokenPackage(v_stack_mC0, v_stack_mC8, (unsigned int)(*(unsigned int *)(a6 + 24)), *(unsigned __int64 *)(a6 + 16));
    if (sign_flag) goto loc_004F4CC4;
    result = SepAppendAceToTokenDefaultDacl(v_stack_mC0, v_stack_mC8, (unsigned int)(*(unsigned int *)(a6 + 24)), *(unsigned __int64 *)(a6 + 16));
    if (sign_flag) goto loc_004F4CC4;
    v_stack_mE0 = 0;
    v_stack_mE8 = 1;
    a4 = 0;
    a2 = 0;
    result = SepSidInTokenSidHash(v_stack_mC0 + 808, a2, *(unsigned __int64 *)(v_rip + 10554380), a4);
    if ((unsigned __int8)(result) == 0) goto loc_004F4B97;
    goto loc_004F4BE0;
loc_004F4B97:
    a1 = (v_stack_mC0) + (808);
    v_stack_mE0 = 0;
    v_stack_mE8 = 1;
    a4 = 0;
    a2 = 0;
    result = SepSidInTokenSidHash(a1, a2, *(unsigned __int64 *)(v_rip + 10554319), a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_mC0;
    }
    result = (*(unsigned __int64 *)(v_rip - 5119716)) + (*(unsigned __int64 *)(v_rip - 5119716));
    *(unsigned int *)(v_stack_mC0 + 56) = (unsigned int)(result);
    result = (result) >> (32);
    *(unsigned int *)(v_stack_mC0 + 60) = (unsigned int)(result);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_mC0 + 48), v_stack_mC0, *(unsigned __int64 *)(v_rip + 10554319), a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_mC0 + 48), v_stack_mC0, *(unsigned __int64 *)(v_rip + 10554319), a4);
    v_stack_mC7 = 0;
    if (v_stack_p8 == 0) goto loc_004F4CA1;
    v_stack_mE0 = v_stack_mA0;
    v_stack_mE8 = 0;
    a2 = 0;
    result = ObInsertObject(v_stack_mC0, a2, (unsigned int)(v_stack_mA4), 1);
    if (!sign_flag) goto loc_004F4C6B;
    goto loc_004F45AC;
loc_004F4C6B:
    result = SepAppendAceToTokenObjectAcl(v_stack_mC0, (unsigned int)(0xF01FFULL), 0, 1);
    if (sign_flag) goto loc_004F4CCC;
    result = SepFinalizeTokenAcls(v_stack_mC0, (unsigned int)(0xF01FFULL), 0, 1);
    result = ObfDereferenceObjectWithTag(v_stack_mC0, (unsigned int)(0x746C6644ULL), 0, 1);
    goto loc_004F4CA6;
loc_004F4CA1:
loc_004F4CA6:
    if (v_stack_p10 == 0) goto loc_004F45AC;
    *(unsigned __int64 *)(v_stack_p10) = v_stack_mC0;
    goto loc_004F45AC;
loc_004F4CC4:
loc_004F4CCC:
    goto loc_004F45A7;
loc_004F4CD9:
    result = v_stack_mC0;
    if (v_stack_p10 != 0) {
        result = v_stack_mC0;
        *(unsigned __int64 *)(v_stack_p10) = result;
    }
    goto loc_004F4CEA;
loc_004F4CEA:
    if (result != 0) {
        a2 = 0x746C6644ULL;
        a1 = result;
        result = ObfDereferenceObjectWithTag(a1, a2, 0, 1);
    }
loc_004F4CFE:
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t SepCreateAppContainerToken(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint8_t Arg5, void *Arg6)
{
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m108;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m64;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint64_t v_stack_mB7;
    uint8_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint8_t v_stack_mC7;
    uint8_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint8_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (224);
    local_rbx = 0;
    v_stack_mB0 = 0;
    v_stack_mA0 = 0;
    result = 0;
    *(uint64_t *)(local_rsp - 0x60) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x50) = 0;
    v_stack_mB8 = 0;
    v_stack_mC8 = 0;
    *(uint64_t *)(local_rsp - 0x70) = 0;
    v_stack_mC0 = 0;
    v_stack_mA8 = 1;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    v_stack_mC7 = 0;
    v_stack_mB4 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg6 + 0x8) + 0x20)));
    if (Arg1 != 0) goto loc_004F4448;
    if (Arg2 == 0) goto loc_004F4452;
    if (Arg1 == 0) goto loc_004F444D;
loc_004F4448:
    if (Arg2 != 0) goto loc_004F4452;
loc_004F444D:
    if (*(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x10) != 0) goto loc_004F445C;
loc_004F4452:
    goto loc_004F4CFE;
loc_004F445C:
    if (*(uint64_t *)((uint32_t)(0xC000000DULL) + 0x8) == 0) goto loc_004F44B2;
    v_stack_m78 = 0;
    v_stack_mE0 = v_stack_m70;
    v_stack_mE8 = v_stack_m78;
    result = ObReferenceObjectByHandle(*(uint64_t *)((uint32_t)(0xC000000DULL) + 0x8), 2, *(uint64_t *)(v_rip + 0xAE3BB4), Arg5);
    if (sign_flag) goto loc_004F4CFE;
    goto loc_004F44E7;
loc_004F44B2:
    v_stack_mE0 = 0;
    v_stack_mE8 = v_stack_m68;
    result = PsReferenceEffectiveToken(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(0x74726853ULL), v_stack_m64, v_stack_mB7);
loc_004F44E7:
    result = SepCheckCreateAppContainer(*(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x10), (uint32_t)(0x74726853ULL), v_stack_m64, v_stack_mB7);
    if (sign_flag) goto loc_004F459F;
    if ((*(uint32_t *)(result + 0xC0)) == 1) goto loc_004F4517;
    if ((*(uint32_t *)(result + 0xC4)) >= 2) goto loc_004F4517;
    goto loc_004F459F;
loc_004F4517:
    result = (uint32_t)(v_stack_m6C);
    if ((uint32_t)((uint32_t)(Arg3)) != 0) { result = (uint32_t)((uint32_t)(Arg3)); }
    v_stack_mA4 = (uint32_t)(result);
    result = RtlIsPackageSid(*(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x10), (uint32_t)(0x74726853ULL), v_stack_m64, v_stack_mB7);
    if ((uint8_t)(result) != 0) goto loc_004F453A;
    goto loc_004F459F;
loc_004F453A:
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x10) + 0x1)) - (8));
    if ((((uint8_t)(result)) & (251)) == 0) goto loc_004F454B;
    goto loc_004F459F;
loc_004F454B:
    local_rbx = 0;
loc_004F454D:
    if (0 >= ((uint32_t)((uint32_t)(v_stack_mB4)))) goto loc_004F4640;
    local_rsi = (0) + (0);
    result = RtlIsCapabilitySid(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18) + local_rsi * 8), (uint32_t)(0x74726853ULL), v_stack_m64, v_stack_mB7);
    if ((uint8_t)(result) == 0) goto loc_004F4592;
    local_rdi = 0;
loc_004F456E:
    if (0 >= 0) goto loc_004F458E;
    Arg2 = (0) + (0);
    result = RtlEqualSid(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18) + local_rsi * 8), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18) + Arg2 * 8), v_stack_m64, v_stack_mB7);
    if ((uint8_t)(result) != 0) goto loc_004F4592;
    local_rdi = (uint32_t)((local_rdi) + 1);
    goto loc_004F456E;
loc_004F458E:
    local_rbx = (uint32_t)((local_rbx) + 1);
    goto loc_004F454D;
loc_004F4592:
loc_004F4597:
loc_004F459F:
loc_004F45A7:
loc_004F45AC:
    if (v_stack_mC7 == 0) goto loc_004F45F4;
    if (!(sign_flag)) {
        Arg2 = v_stack_mC0;
        Arg1 = *(uint64_t *)(v_rip - 0x4E18BB);
        result = Arg1;
        result = (result) + (Arg1);
        *(uint32_t *)(Arg2 + 0x38) = (uint32_t)(result);
        result = (result) >> (32);
        *(uint32_t *)(Arg2 + 0x3C) = (uint32_t)(result);
    }
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_mC0 + 0x30), Arg2, v_stack_m64, v_stack_mB7);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_mC0 + 0x30), Arg2, v_stack_m64, v_stack_mB7);
loc_004F45F4:
    if (!sign_flag) goto loc_004F462A;
    if ((uint8_t)(v_stack_mC8) != 0) {
        Arg2 = 0x746C6644ULL;
        Arg1 = v_stack_mC0;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, v_stack_m64, v_stack_mB7);
    }
    if (v_stack_mA0 != 0) {
        Arg2 = Arg5;
        result = ObCloseHandle(v_stack_mA0, Arg2, v_stack_m64, v_stack_mB7);
    }
    if (sign_flag) goto loc_004F4CEA;
loc_004F462A:
    if (v_stack_p8 == 0) goto loc_004F4CD9;
    *(uint64_t *)(v_stack_p8) = v_stack_mA0;
    goto loc_004F4CE6;
loc_004F4640:
    result = SepCapabilitiesHasAppSiloBaseSID((uint32_t)((uint32_t)(v_stack_p10)), *(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18), v_stack_m64, v_stack_mB7);
    if ((uint8_t)(result) != 0) goto loc_004F466F;
    local_rbx = 0;
loc_004F4650:
    if (0 >= ((uint32_t)(v_stack_p10))) goto loc_004F466F;
    Arg1 = (0) + (0);
    result = SepIsAppSiloCapability(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18) + Arg1 * 8), *(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18), v_stack_m64, v_stack_mB7);
    if ((uint8_t)(result) != 0) goto loc_004F4592;
    local_rbx = (uint32_t)((local_rbx) + 1);
    goto loc_004F4650;
loc_004F466F:
    result = RtlGetAppContainerSidType(v_stack_mC8, v_stack_mB0, v_stack_m64, v_stack_mB7);
    if (sign_flag) goto loc_004F4597;
    if (v_stack_mB0 != 1) goto loc_004F46B7;
    v_stack_mE8 = v_stack_mB8;
    result = SepCheckCapabilities(result, (uint32_t)((uint32_t)(v_stack_p10)), *(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18), v_stack_mB7);
    if (v_stack_mB8 != 0) goto loc_004F46B7;
loc_004F46AD:
    goto loc_004F4597;
loc_004F46B7:
    if (sign_flag) goto loc_004F4597;
    result = Feature_871661881__private_IsEnabledDeviceUsageNoInline(result, (uint32_t)((uint32_t)(v_stack_p10)), *(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18), v_stack_mB7);
    if ((uint32_t)(result) == 0) goto loc_004F47CE;
    result = RtlQueryElevationFlags(v_stack_mAC, (uint32_t)((uint32_t)(v_stack_p10)), *(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18), v_stack_mB7);
    result = (uint8_t)(((uint32_t)(v_stack_mAC)) & (24));
    if (((uint8_t)(result)) != 16) goto loc_004F47CE;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(result + 0x30), 1, *(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18), v_stack_mB7);
    result = SepLocateTokenIntegrity(result, 1, *(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18), v_stack_mB7);
    if (result == 0) goto loc_004F47B8;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1)) == 0) goto loc_004F47B8;
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(result) + 0x1)) - 1);
    if ((*(uint32_t *)(*(uint64_t *)(result) + result * 4 + 0x8)) < 0x3000ULL) goto loc_004F47B8;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = SeCaptureSubjectContext(v_stack_m48, 1, *(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18), v_stack_mB7);
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m38 + 0x30), 1, *(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18), v_stack_mB7);
    result = SepLocateTokenIntegrity(v_stack_m38, 1, *(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18), v_stack_mB7);
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1)) == 0) goto loc_004F4798;
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(result) + 0x1)) - 1);
    local_rbx = (uint32_t)(0xC0000022ULL);
    if ((*(uint32_t *)(*(uint64_t *)(result) + result * 4 + 0x8)) < 0x3000ULL) {
        local_rbx = 0xC0000022ULL;
    }
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m38 + 0x30), 1, *(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18), v_stack_mB7);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m38 + 0x30), 1, *(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18), v_stack_mB7);
    result = SeReleaseSubjectContext(v_stack_m48, 1, *(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18), v_stack_mB7);
loc_004F47B8:
    result = ExReleaseResourceLite(*(uint64_t *)(result + 0x30), 1, *(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18), v_stack_mB7);
    result = KeLeaveCriticalRegion(*(uint64_t *)(result + 0x30), 1, *(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18), v_stack_mB7);
    if (sign_flag) goto loc_004F4597;
loc_004F47CE:
    v_stack_mD0 = v_stack_mC0;
    v_stack_mD8 = 0;
    v_stack_mE0 = Arg5;
    Arg3 = 0;
    result = SepDuplicateToken(result, Arg4, Arg3, 1);
    local_r12 = 0;
    if (sign_flag) goto loc_004F4597;
    v_stack_mC8 = 1;
    result = SeSetMandatoryPolicyToken(v_stack_mC0, v_stack_mA8, Arg3, 1);
    if (sign_flag) goto loc_004F4597;
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_stack_mC0 + 0x30), 1, Arg3, 1);
    v_stack_mC7 = 1;
    result = SepLocateTokenIntegrity(v_stack_mC0, 1, Arg3, 1);
    if (result == 0) goto loc_004F4AB1;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1)) == 0) goto loc_004F4A2C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg6 + 0x8) + 0x4)))) & (1)) == 0) goto loc_004F48A4;
    *(uint32_t *)(*(uint64_t *)(result) + *(uint8_t *)(*(uint64_t *)(result) + 0x1) - 0x1 * 4 + 0x8) = 0x1000ULL;
    goto loc_004F4A28;
loc_004F48A4:
    result = SeCaptureSubjectContext(v_stack_m98, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg6 + 0x8) + 0x4)), *(uint64_t *)(result), *(uint8_t *)(*(uint64_t *)(result) + 0x1));
    result = SeLockSubjectContext(v_stack_m98, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg6 + 0x8) + 0x4)), *(uint64_t *)(result), *(uint8_t *)(*(uint64_t *)(result) + 0x1));
    result = ExAcquireResourceSharedLite(*(uint64_t *)(result + 0x30), 1, *(uint64_t *)(result), *(uint8_t *)(*(uint64_t *)(result) + 0x1));
    result = SepLocateTokenIntegrity(result, 1, *(uint64_t *)(result), *(uint8_t *)(*(uint64_t *)(result) + 0x1));
    if (result == 0) goto loc_004F4927;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1)) != 0) goto loc_004F48F1;
    goto loc_004F48F7;
loc_004F48F1:
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(result) + 0x1)) - 1);
loc_004F48F7:
    if ((*(uint32_t *)(*(uint64_t *)(arg6 + 0x8) + 0x28)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(0 + result * 4 + 0x8))))) goto loc_004F4927;
    result = ExReleaseResourceLite(*(uint64_t *)(result + 0x30), 1, *(uint64_t *)(result), *(uint8_t *)(*(uint64_t *)(result) + 0x1));
    result = KeLeaveCriticalRegion(*(uint64_t *)(result + 0x30), 1, *(uint64_t *)(result), *(uint8_t *)(*(uint64_t *)(result) + 0x1));
loc_004F490E:
    result = SeUnlockSubjectContext(v_stack_m98, 1, *(uint64_t *)(result), *(uint8_t *)(*(uint64_t *)(result) + 0x1));
    result = SeReleaseSubjectContext(v_stack_m98, 1, *(uint64_t *)(result), *(uint8_t *)(*(uint64_t *)(result) + 0x1));
    goto loc_004F46AD;
loc_004F4927:
    result = ExReleaseResourceLite(*(uint64_t *)(result + 0x30), 1, *(uint64_t *)(result), *(uint8_t *)(*(uint64_t *)(result) + 0x1));
    result = KeLeaveCriticalRegion(*(uint64_t *)(result + 0x30), 1, *(uint64_t *)(result), *(uint8_t *)(*(uint64_t *)(result) + 0x1));
    result = SepLocateTokenIntegrity(v_stack_m88, 1, *(uint64_t *)(result), *(uint8_t *)(*(uint64_t *)(result) + 0x1));
    if (result == 0) goto loc_004F4A03;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1)) != 0) goto loc_004F495B;
    goto loc_004F4961;
loc_004F495B:
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(result) + 0x1)) - 1);
loc_004F4961:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(0 + result * 4 + 0x8)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg6 + 0x8) + 0x28))))) goto loc_004F490E;
    if (v_stack_m98 == 0) goto loc_004F49F4;
    if ((*(uint32_t *)(v_stack_m98 + 0xC0)) != 2) goto loc_004F4988;
    if ((*(uint32_t *)(v_stack_m98 + 0xC4)) < 2) goto loc_004F490E;
loc_004F4988:
    result = SepLocateTokenIntegrity(v_stack_m98, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg6 + 0x8) + 0x28)), *(uint64_t *)(result), *(uint8_t *)(*(uint64_t *)(result) + 0x1));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1)) != 0) goto loc_004F49A2;
    goto loc_004F49AB;
loc_004F49A2:
loc_004F49AB:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result) + *(uint8_t *)(*(uint64_t *)(result) + 0x1) - 0x1 * 4 + 0x8)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg6 + 0x8) + 0x28))))) goto loc_004F49C4;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1)) != 0) goto loc_004F49B9;
    goto loc_004F49C6;
loc_004F49B9:
    goto loc_004F49C6;
loc_004F49C4:
loc_004F49C6:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg6 + 0x8) + 0x28)))) < ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg6 + 0x8) + 0x28))))))) goto loc_004F49F4;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1)) != 0) goto loc_004F49D4;
    goto loc_004F49DD;
loc_004F49D4:
loc_004F49DD:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result) + (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1))) - 0x1 * 4 + 0x8)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg6 + 0x8) + 0x28))))) goto loc_004F49F4;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1)) != 0) goto loc_004F49EB;
    goto loc_004F49F4;
loc_004F49EB:
loc_004F49F4:
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(result) + 0x1)) - 1);
    *(uint32_t *)(*(uint64_t *)(result) + result * 4 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result) + *(uint8_t *)(*(uint64_t *)(result) + 0x1) - 0x1 * 4 + 0x8)));
    goto loc_004F4A14;
loc_004F4A03:
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(result) + 0x1)) - 1);
    *(uint32_t *)(*(uint64_t *)(result) + result * 4 + 0x8) = 0x1000ULL;
loc_004F4A14:
    result = SeUnlockSubjectContext(v_stack_m98, *(uint64_t *)(result), *(uint8_t *)(*(uint64_t *)(result) + 0x1), *(uint64_t *)(result));
    result = SeReleaseSubjectContext(v_stack_m98, *(uint64_t *)(result), *(uint8_t *)(*(uint64_t *)(result) + 0x1), *(uint64_t *)(result));
loc_004F4A28:
loc_004F4A2C:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1)) == 0) goto loc_004F4A68;
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(result) + 0x1)) - 1);
    if ((*(uint32_t *)(*(uint64_t *)(result) + result * 4 + 0x8)) < 0x2000ULL) {
        result = v_stack_mC0;
    }
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(result), *(uint64_t *)(result), *(uint8_t *)(*(uint64_t *)(result) + 0x1), *(uint64_t *)(result));
    if ((uint32_t)(result) == 0) goto loc_004F4AA2;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1)) == 0) goto loc_004F4A95;
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(result) + 0x1)) - 1);
    if ((*(uint32_t *)(*(uint64_t *)(result) + result * 4 + 0x8)) < 0x3000ULL) {
        result = v_stack_mC0;
    }
    goto loc_004F4AB6;
loc_004F4AB1:
loc_004F4AB6:
    if (sign_flag) goto loc_004F4597;
    result = SepSetTokenCapabilities(v_stack_mC0, v_stack_mC8, *(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18), (uint32_t)((uint32_t)((uint32_t)(v_stack_mB4))));
    if (sign_flag) goto loc_004F4CC4;
    result = SepSetTokenLowboxNumber(v_stack_mC0, v_stack_mC8, *(uint64_t *)(*(uint64_t *)(arg6 + 0x8) + 0x18), (uint32_t)((uint32_t)((uint32_t)(v_stack_mB4))));
    if (sign_flag) goto loc_004F4CC4;
    v_stack_m58 = v_stack_mC8;
    result = SepSetTokenCachedHandles(v_stack_mC0, v_stack_m60, (uint32_t)(*(uint32_t *)(arg6 + 0x18)), *(uint64_t *)(arg6 + 0x10));
    if (sign_flag) goto loc_004F4CC4;
    result = SepSetTokenPackage(v_stack_mC0, v_stack_mC8, (uint32_t)(*(uint32_t *)(arg6 + 0x18)), *(uint64_t *)(arg6 + 0x10));
    if (sign_flag) goto loc_004F4CC4;
    result = SepAppendAceToTokenDefaultDacl(v_stack_mC0, v_stack_mC8, (uint32_t)(*(uint32_t *)(arg6 + 0x18)), *(uint64_t *)(arg6 + 0x10));
    if (sign_flag) goto loc_004F4CC4;
    v_stack_mE0 = 0;
    v_stack_mE8 = 1;
    Arg4 = 0;
    Arg2 = 0;
    result = SepSidInTokenSidHash(v_stack_mC0 + 808, Arg2, *(uint64_t *)(v_rip + 0xA10C0C), Arg4);
    if ((uint8_t)(result) == 0) goto loc_004F4B97;
    goto loc_004F4BE0;
loc_004F4B97:
    Arg1 = (v_stack_mC0) + (808);
    v_stack_mE0 = 0;
    v_stack_mE8 = 1;
    Arg4 = 0;
    Arg2 = 0;
    result = SepSidInTokenSidHash(Arg1, Arg2, *(uint64_t *)(v_rip + 0xA10BCF), Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_mC0;
    }
    result = (*(uint64_t *)(v_rip - 0x4E1EE4)) + (*(uint64_t *)(v_rip - 0x4E1EE4));
    *(uint32_t *)(v_stack_mC0 + 0x38) = (uint32_t)(result);
    result = (result) >> (32);
    *(uint32_t *)(v_stack_mC0 + 0x3C) = (uint32_t)(result);
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_mC0 + 0x30), v_stack_mC0, *(uint64_t *)(v_rip + 0xA10BCF), Arg4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_mC0 + 0x30), v_stack_mC0, *(uint64_t *)(v_rip + 0xA10BCF), Arg4);
    v_stack_mC7 = 0;
    if (v_stack_p8 == 0) goto loc_004F4CA1;
    v_stack_mE0 = v_stack_mA0;
    v_stack_mE8 = 0;
    Arg2 = 0;
    result = ObInsertObject(v_stack_mC0, Arg2, (uint32_t)(v_stack_mA4), 1);
    if (!sign_flag) goto loc_004F4C6B;
    goto loc_004F45AC;
loc_004F4C6B:
    result = SepAppendAceToTokenObjectAcl(v_stack_mC0, (uint32_t)(0xF01FFULL), 0, 1);
    if (sign_flag) goto loc_004F4CCC;
    result = SepFinalizeTokenAcls(v_stack_mC0, (uint32_t)(0xF01FFULL), 0, 1);
    result = ObfDereferenceObjectWithTag(v_stack_mC0, (uint32_t)(0x746C6644ULL), 0, 1);
    goto loc_004F4CA6;
loc_004F4CA1:
loc_004F4CA6:
    if (v_stack_p10 == 0) goto loc_004F45AC;
    *(uint64_t *)(v_stack_p10) = v_stack_mC0;
    goto loc_004F45AC;
loc_004F4CC4:
loc_004F4CCC:
    goto loc_004F45A7;
loc_004F4CD9:
    result = v_stack_mC0;
    if (v_stack_p10 != 0) {
        result = v_stack_mC0;
        *(uint64_t *)(v_stack_p10) = result;
    }
    goto loc_004F4CEA;
loc_004F4CEA:
    if (result != 0) {
        Arg2 = 0x746C6644ULL;
        Arg1 = result;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, 0, 1);
    }
loc_004F4CFE:
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x8` | `64` | `R` |
| `Arg6` | `+ 0x10` | `64` | `R` |
| `Arg6` | `+ 0x18` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F43AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
