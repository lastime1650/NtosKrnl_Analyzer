# CmpCloneHwProfile

- RVA: `0x007E303C`–`0x007E383A` (길이 `2,046` bytes)
- VA: `0x00000001407E303C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BC10C`
- 디코드: `497`개 명령, `2,046/2,046` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **61**; 고유 호출 대상: **31**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x007E30EA` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (function, `0x0042A7F0`)
- `0x007E30F3` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x007E311D` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (function, `0x00504B20`)
- `0x007E312D` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E3160` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x007E316E` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007E3197` → [ZwQuerySecurityObject](../../text/6A/ZwQuerySecurityObject_function_006AFDF0.md) (function, `0x006AFDF0`)
- `0x007E31B2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007E31D9` → [ZwQuerySecurityObject](../../text/6A/ZwQuerySecurityObject_function_006AFDF0.md) (function, `0x006AFDF0`)
- `0x007E31E7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007E323A` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (function, `0x006AD470`)
- `0x007E324B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007E327D` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (function, `0x00504B20`)
- `0x007E328E` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E32DC` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (function, `0x006AD470`)
- `0x007E32FD` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E332E` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x007E335F` → [ZwQueryKey](../../text/6A/ZwQueryKey_function_006AD390.md) (function, `0x006AD390`)
- `0x007E33A8` → [ZwEnumerateKey](../../text/6A/ZwEnumerateKey_function_006AD710.md) (function, `0x006AD710`)
- `0x007E33C5` → [wtoi](../../text/50/wtoi_function_005003E0.md) (function, `0x005003E0`)
- `0x007E33D6` → [wtoi](../../text/50/wtoi_function_005003E0.md) (function, `0x005003E0`)
- `0x007E3432` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x007E3447` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E3472` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (function, `0x006AD3B0`)
- `0x007E349E` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007E34CD` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E34F5` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x007E350B` → [CmpCreateHwProfileFriendlyName](CmpCreateHwProfileFriendlyName_function_007E3840.md) (function, `0x007E3840`)
- `0x007E3520` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E354D` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x007E3556` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x007E3574` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E3597` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x007E35AD` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E35D0` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x007E35D9` → [ExUuidCreate](../91/ExUuidCreate_function_00917500.md) (function, `0x00917500`)
- `0x007E35ED` → [RtlStringFromGUIDEx](../91/RtlStringFromGUIDEx_function_00915450.md) (function, `0x00915450`)
- `0x007E3602` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x007E3628` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x007E3631` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x007E365A` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x007E368F` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x007E369E` → [CmpLockRegistryExclusive](../84/CmpLockRegistryExclusive_function_0084F9B4.md) (function, `0x0084F9B4`)
- `0x007E36D0` → [CmpCopySyncTree](../7F/CmpCopySyncTree_function_007F21A0.md) (function, `0x007F21A0`)
- `0x007E370B` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007E3712` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007E373B` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007E3742` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007E3765` → [CmpRebuildKcbCache](../87/CmpRebuildKcbCache_function_00874DF8.md) (function, `0x00874DF8`)
- `0x007E377F` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007E3786` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007E37AB` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007E37B2` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007E37C4` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x007E37C9` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007E37D1` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007E37E0` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007E37EE` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007E37FF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007E3808` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)
- `0x007E3819` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [CmSetAcpiHwProfile](CmSetAcpiHwProfile_function_007E2584.md) at `0x007E29D7`
- [CmpCreateHardwareProfiles](../../init/C5/CmpCreateHardwareProfiles_function_00C56EF4.md) at `0x00C573C7`

### Static image references
- `0x007E305B` → RVA `0x00E0A740` (`.data`; read)
- `0x007E3107` → RVA `0x00B09280` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E326A` → RVA `0x00B093F0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E32F1` → RVA `0x00B09130` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E343B` → RVA `0x00B09340` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E3514` → RVA `0x00B09360` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E3563` → RVA `0x00B09320` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E359C` → RVA `0x00B093E0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E35F6` → RVA `0x00B093B0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007E3636` → RVA `0x00FC6AC0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **43**
  - `0x007E30EA` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (`PAGE` → `.text`)
  - `0x007E30F3` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`PAGE` → `.text`)
  - `0x007E311D` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (`PAGE` → `.text`)
  - `0x007E312D` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E3160` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x007E316E` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007E3197` → [ZwQuerySecurityObject](../../text/6A/ZwQuerySecurityObject_function_006AFDF0.md) (`PAGE` → `.text`)
  - `0x007E31B2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007E31D9` → [ZwQuerySecurityObject](../../text/6A/ZwQuerySecurityObject_function_006AFDF0.md) (`PAGE` → `.text`)
  - `0x007E31E7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007E323A` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (`PAGE` → `.text`)
  - `0x007E324B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007E327D` → [swprintf_s](../../text/50/swprintf_s_function_00504B20.md) (`PAGE` → `.text`)
  - `0x007E328E` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E32DC` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (`PAGE` → `.text`)
  - `0x007E32FD` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E332E` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x007E335F` → [ZwQueryKey](../../text/6A/ZwQueryKey_function_006AD390.md) (`PAGE` → `.text`)
  - `0x007E33A8` → [ZwEnumerateKey](../../text/6A/ZwEnumerateKey_function_006AD710.md) (`PAGE` → `.text`)
  - `0x007E33C5` → [wtoi](../../text/50/wtoi_function_005003E0.md) (`PAGE` → `.text`)
  - `0x007E33D6` → [wtoi](../../text/50/wtoi_function_005003E0.md) (`PAGE` → `.text`)
  - `0x007E3432` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x007E3447` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E3472` → [ZwQueryValueKey](../../text/6A/ZwQueryValueKey_function_006AD3B0.md) (`PAGE` → `.text`)
  - `0x007E349E` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007E34CD` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E34F5` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`PAGE` → `.text`)
  - `0x007E3520` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E354D` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`PAGE` → `.text`)
  - `0x007E3574` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E3597` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`PAGE` → `.text`)
  - `0x007E35AD` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E35D0` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`PAGE` → `.text`)
  - `0x007E3602` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x007E3628` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`PAGE` → `.text`)
  - `0x007E37C4` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x007E37C9` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007E37D1` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007E37E0` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007E37EE` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007E37FF` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007E3808` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
  - `0x007E3819` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007E303C  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
007E3041  55                              push rbp
007E3042  56                              push rsi
007E3043  57                              push rdi
007E3044  41 54                           push r12
007E3046  41 55                           push r13
007E3048  41 56                           push r14
007E304A  41 57                           push r15
007E304C  48 8D AC 24 50 FE FF FF         lea rbp, [rsp - 0x1b0]
007E3054  48 81 EC B0 02 00 00            sub rsp, 0x2b0
007E305B  48 8B 05 DE 76 62 00            mov rax, qword ptr [rip + 0x6276de]
007E3062  48 33 C4                        xor rax, rsp
007E3065  48 89 85 A0 01 00 00            mov qword ptr [rbp + 0x1a0], rax
007E306C  4C 8B BD 18 02 00 00            mov r15, qword ptr [rbp + 0x218]
007E3073  33 DB                           xor ebx, ebx
007E3075  48 8B B5 20 02 00 00            mov rsi, qword ptr [rbp + 0x220]
007E307C  0F 57 C0                        xorps xmm0, xmm0
007E307F  0F 57 C9                        xorps xmm1, xmm1
007E3082  4C 89 44 24 48                  mov qword ptr [rsp + 0x48], r8
007E3087  33 C0                           xor eax, eax
007E3089  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
007E308D  49 89 1F                        mov qword ptr [r15], rbx
007E3090  4C 8B E9                        mov r13, rcx
007E3093  48 8D 4D E8                     lea rcx, [rbp - 0x18]
007E3097  44 89 0E                        mov dword ptr [rsi], r9d
007E309A  4D 8B E0                        mov r12, r8
007E309D  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
007E30A1  4C 8B F2                        mov r14, rdx
007E30A4  89 45 C0                        mov dword ptr [rbp - 0x40], eax
007E30A7  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
007E30AB  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
007E30B0  0F 11 4C 24 50                  movups xmmword ptr [rsp + 0x50], xmm1
007E30B5  89 5C 24 70                     mov dword ptr [rsp + 0x70], ebx
007E30B9  0F 11 45 80                     movups xmmword ptr [rbp - 0x80], xmm0
007E30BD  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
007E30C1  0F 11 4D C8                     movups xmmword ptr [rbp - 0x38], xmm1
007E30C5  89 5C 24 74                     mov dword ptr [rsp + 0x74], ebx
007E30C9  0F 11 45 98                     movups xmmword ptr [rbp - 0x68], xmm0
007E30CD  48 89 5D 90                     mov qword ptr [rbp - 0x70], rbx
007E30D1  0F 11 45 A8                     movups xmmword ptr [rbp - 0x58], xmm0
007E30D5  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
007E30DA  0F 11 45 10                     movups xmmword ptr [rbp + 0x10], xmm0
007E30DE  48 89 45 08                     mov qword ptr [rbp + 8], rax
007E30E2  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
007E30E6  0F 11 4D F8                     movups xmmword ptr [rbp - 8], xmm1
007E30EA  E8 01 77 C4 FF                  call 0x14042a7f0
007E30EF  48 8D 4D F8                     lea rcx, [rbp - 8]
007E30F3  E8 78 8D C1 FF                  call 0x1403fbe70
007E30F8  44 8B 0E                        mov r9d, dword ptr [rsi]
007E30FB  41 81 F9 C8 00 00 00            cmp r9d, 0xc8
007E3102  73 7C                           jae 0x1407e3180
007E3104  41 FF C1                        inc r9d
007E3107  4C 8D 05 72 61 32 00            lea r8, [rip + 0x326172]
007E310E  BA 40 00 00 00                  mov edx, 0x40
007E3113  44 89 0E                        mov dword ptr [rsi], r9d
007E3116  48 8D 8D 20 01 00 00            lea rcx, [rbp + 0x120]
007E311D  E8 FE 19 D2 FF                  call 0x140504b20
007E3122  48 8D 95 20 01 00 00            lea rdx, [rbp + 0x120]
007E3129  48 8D 4D D8                     lea rcx, [rbp - 0x28]
007E312D  E8 4E 76 C4 FF                  call 0x14042a780
007E3132  48 8D 45 D8                     lea rax, [rbp - 0x28]
007E3136  C7 45 98 30 00 00 00            mov dword ptr [rbp - 0x68], 0x30
007E313D  0F 57 C0                        xorps xmm0, xmm0
007E3140  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
007E3144  4C 8D 45 98                     lea r8, [rbp - 0x68]
007E3148  4C 89 75 A0                     mov qword ptr [rbp - 0x60], r14
007E314C  BA 1F 00 02 00                  mov edx, 0x2001f
007E3151  C7 45 B0 40 02 00 00            mov dword ptr [rbp - 0x50], 0x240
007E3158  49 8B CF                        mov rcx, r15
007E315B  F3 0F 7F 45 B8                  movdqu xmmword ptr [rbp - 0x48], xmm0
007E3160  E8 AB A1 EC FF                  call 0x1406ad310
007E3165  8B D8                           mov ebx, eax
007E3167  85 C0                           test eax, eax
007E3169  78 0A                           js 0x1407e3175
007E316B  49 8B 0F                        mov rcx, qword ptr [r15]
007E316E  E8 3D A1 EC FF                  call 0x1406ad2b0
007E3173  EB 83                           jmp 0x1407e30f8
007E3175  3D 34 00 00 C0                  cmp eax, 0xc0000034
007E317A  0F 85 4E 06 00 00               jne 0x1407e37ce
007E3180  45 33 C9                        xor r9d, r9d
007E3183  48 8D 44 24 60                  lea rax, [rsp + 0x60]
007E3188  45 33 C0                        xor r8d, r8d
007E318B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E3190  49 8B CC                        mov rcx, r12
007E3193  41 8D 51 04                     lea edx, [r9 + 4]
007E3197  E8 54 CC EC FF                  call 0x1406afdf0
007E319C  3D 23 00 00 C0                  cmp eax, 0xc0000023
007E31A1  75 4D                           jne 0x1407e31f0
007E31A3  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
007E31A7  B9 00 01 00 00                  mov ecx, 0x100
007E31AC  41 B8 43 4D 20 20               mov r8d, 0x20204d43
007E31B2  E8 39 EF 39 00                  call 0x140b820f0
007E31B7  33 DB                           xor ebx, ebx
007E31B9  48 8B F8                        mov rdi, rax
007E31BC  48 85 C0                        test rax, rax
007E31BF  74 31                           je 0x1407e31f2
007E31C1  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
007E31C6  48 8D 44 24 60                  lea rax, [rsp + 0x60]
007E31CB  4C 8B C7                        mov r8, rdi
007E31CE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E31D3  8D 53 04                        lea edx, [rbx + 4]
007E31D6  49 8B CC                        mov rcx, r12
007E31D9  E8 12 CC EC FF                  call 0x1406afdf0
007E31DE  85 C0                           test eax, eax
007E31E0  79 10                           jns 0x1407e31f2
007E31E2  33 D2                           xor edx, edx
007E31E4  48 8B CF                        mov rcx, rdi
007E31E7  E8 84 F6 39 00                  call 0x140b82870
007E31EC  8B FB                           mov edi, ebx
007E31EE  EB 02                           jmp 0x1407e31f2
007E31F0  33 FF                           xor edi, edi
007E31F2  48 8D 45 D8                     lea rax, [rbp - 0x28]
007E31F6  4C 89 75 A0                     mov qword ptr [rbp - 0x60], r14
007E31FA  45 33 F6                        xor r14d, r14d
007E31FD  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
007E3201  48 8D 44 24 70                  lea rax, [rsp + 0x70]
007E3206  C7 45 98 30 00 00 00            mov dword ptr [rbp - 0x68], 0x30
007E320D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007E3212  4C 8D 45 98                     lea r8, [rbp - 0x68]
007E3216  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
007E321B  45 33 C9                        xor r9d, r9d
007E321E  BA 1F 00 02 00                  mov edx, 0x2001f
007E3223  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
007E3228  49 8B CF                        mov rcx, r15
007E322B  C7 45 B0 40 02 00 00            mov dword ptr [rbp - 0x50], 0x240
007E3232  48 89 7D B8                     mov qword ptr [rbp - 0x48], rdi
007E3236  4C 89 75 C0                     mov qword ptr [rbp - 0x40], r14
007E323A  E8 31 A2 EC FF                  call 0x1406ad470
007E323F  8B D8                           mov ebx, eax
007E3241  48 85 FF                        test rdi, rdi
007E3244  74 0A                           je 0x1407e3250
007E3246  33 D2                           xor edx, edx
007E3248  48 8B CF                        mov rcx, rdi
007E324B  E8 20 F6 39 00                  call 0x140b82870
007E3250  85 DB                           test ebx, ebx
007E3252  0F 88 76 05 00 00               js 0x1407e37ce
007E3258  83 7C 24 70 01                  cmp dword ptr [rsp + 0x70], 1
007E325D  74 08                           je 0x1407e3267
007E325F  41 8B DE                        mov ebx, r14d
007E3262  E9 67 05 00 00                  jmp 0x1407e37ce
007E3267  44 8B 0E                        mov r9d, dword ptr [rsi]
007E326A  4C 8D 05 7F 61 32 00            lea r8, [rip + 0x32617f]
007E3271  BA 40 00 00 00                  mov edx, 0x40
007E3276  48 8D 8D 20 01 00 00            lea rcx, [rbp + 0x120]
007E327D  E8 9E 18 D2 FF                  call 0x140504b20
007E3282  48 8D 95 20 01 00 00            lea rdx, [rbp + 0x120]
007E3289  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007E328E  E8 ED 74 C4 FF                  call 0x14042a780
007E3293  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007E3298  4C 89 6D A0                     mov qword ptr [rbp - 0x60], r13
007E329C  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
007E32A0  4C 8D 45 98                     lea r8, [rbp - 0x68]
007E32A4  48 8D 44 24 70                  lea rax, [rsp + 0x70]
007E32A9  C7 45 B0 40 02 00 00            mov dword ptr [rbp - 0x50], 0x240
007E32B0  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007E32B5  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
007E32BA  0F 57 C0                        xorps xmm0, xmm0
007E32BD  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
007E32C2  BF 30 00 00 00                  mov edi, 0x30
007E32C7  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
007E32CC  45 33 C9                        xor r9d, r9d
007E32CF  89 7D 98                        mov dword ptr [rbp - 0x68], edi
007E32D2  BA 1F 00 02 00                  mov edx, 0x2001f
007E32D7  F3 0F 7F 45 B8                  movdqu xmmword ptr [rbp - 0x48], xmm0
007E32DC  E8 8F A1 EC FF                  call 0x1406ad470
007E32E1  8B D8                           mov ebx, eax
007E32E3  85 C0                           test eax, eax
007E32E5  79 0A                           jns 0x1407e32f1
007E32E7  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
007E32EC  E9 DD 04 00 00                  jmp 0x1407e37ce
007E32F1  48 8D 15 38 5E 32 00            lea rdx, [rip + 0x325e38]
007E32F8  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007E32FD  E8 7E 74 C4 FF                  call 0x14042a780
007E3302  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007E3307  89 7D 98                        mov dword ptr [rbp - 0x68], edi
007E330A  0F 57 C0                        xorps xmm0, xmm0
007E330D  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
007E3311  4C 8D 45 98                     lea r8, [rbp - 0x68]
007E3315  4C 89 6D A0                     mov qword ptr [rbp - 0x60], r13
007E3319  BA 19 00 02 00                  mov edx, 0x20019
007E331E  C7 45 B0 40 02 00 00            mov dword ptr [rbp - 0x50], 0x240
007E3325  48 8D 4D 90                     lea rcx, [rbp - 0x70]
007E3329  F3 0F 7F 45 B8                  movdqu xmmword ptr [rbp - 0x48], xmm0
007E332E  E8 DD 9F EC FF                  call 0x1406ad310
007E3333  8B D8                           mov ebx, eax
007E3335  85 C0                           test eax, eax
007E3337  79 09                           jns 0x1407e3342
007E3339  4C 89 75 90                     mov qword ptr [rbp - 0x70], r14
007E333D  E9 8C 04 00 00                  jmp 0x1407e37ce
007E3342  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
007E3346  48 8D 44 24 74                  lea rax, [rsp + 0x74]
007E334B  41 B9 00 01 00 00               mov r9d, 0x100
007E3351  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E3356  4C 8D 45 20                     lea r8, [rbp + 0x20]
007E335A  BA 02 00 00 00                  mov edx, 2
007E335F  E8 2C A0 EC FF                  call 0x1406ad390
007E3364  8B D8                           mov ebx, eax
007E3366  85 C0                           test eax, eax
007E3368  0F 88 60 04 00 00               js 0x1407e37ce
007E336E  8B 7D 34                        mov edi, dword ptr [rbp + 0x34]
007E3371  83 C8 FF                        or eax, 0xffffffff
007E3374  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
007E3378  41 8B DE                        mov ebx, r14d
007E337B  85 FF                           test edi, edi
007E337D  0F 84 38 01 00 00               je 0x1407e34bb
007E3383  41 BC 02 00 00 00               mov r12d, 2
007E3389  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
007E338D  48 8D 44 24 74                  lea rax, [rsp + 0x74]
007E3392  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007E3397  4C 8D 4D 20                     lea r9, [rbp + 0x20]
007E339B  45 33 C0                        xor r8d, r8d
007E339E  C7 44 24 20 FE 00 00 00         mov dword ptr [rsp + 0x20], 0xfe
007E33A6  8B D3                           mov edx, ebx
007E33A8  E8 63 A3 EC FF                  call 0x1406ad710
007E33AD  85 C0                           test eax, eax
007E33AF  0F 88 FD 00 00 00               js 0x1407e34b2
007E33B5  8B 45 2C                        mov eax, dword ptr [rbp + 0x2c]
007E33B8  48 8D 4D 30                     lea rcx, [rbp + 0x30]
007E33BC  48 D1 E8                        shr rax, 1
007E33BF  66 44 89 74 45 30               mov word ptr [rbp + rax*2 + 0x30], r14w
007E33C5  E8 16 D0 D1 FF                  call 0x1405003e0
007E33CA  85 C0                           test eax, eax
007E33CC  0F 84 D6 00 00 00               je 0x1407e34a8
007E33D2  48 8D 4D 30                     lea rcx, [rbp + 0x30]
007E33D6  E8 05 D0 D1 FF                  call 0x1405003e0
007E33DB  3B 06                           cmp eax, dword ptr [rsi]
007E33DD  0F 84 C5 00 00 00               je 0x1407e34a8
007E33E3  8B 45 2C                        mov eax, dword ptr [rbp + 0x2c]
007E33E6  4C 8D 45 98                     lea r8, [rbp - 0x68]
007E33EA  66 89 44 24 50                  mov word ptr [rsp + 0x50], ax
007E33EF  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
007E33F4  66 41 03 C4                     add ax, r12w
007E33F8  C7 45 98 30 00 00 00            mov dword ptr [rbp - 0x68], 0x30
007E33FF  66 89 44 24 52                  mov word ptr [rsp + 0x52], ax
007E3404  0F 57 C0                        xorps xmm0, xmm0
007E3407  48 8D 45 30                     lea rax, [rbp + 0x30]
007E340B  C7 45 B0 40 02 00 00            mov dword ptr [rbp - 0x50], 0x240
007E3412  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
007E3417  BA 19 00 02 00                  mov edx, 0x20019
007E341C  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
007E3420  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
007E3424  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007E3429  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
007E342D  F3 0F 7F 45 B8                  movdqu xmmword ptr [rbp - 0x48], xmm0
007E3432  E8 D9 9E EC FF                  call 0x1406ad310
007E3437  85 C0                           test eax, eax
007E3439  78 68                           js 0x1407e34a3
007E343B  48 8D 15 FE 5E 32 00            lea rdx, [rip + 0x325efe]
007E3442  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007E3447  E8 34 73 C4 FF                  call 0x14042a780
007E344C  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
007E3451  48 8D 44 24 74                  lea rax, [rsp + 0x74]
007E3456  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007E345B  4C 8D 4D 20                     lea r9, [rbp + 0x20]
007E345F  41 B8 01 00 00 00               mov r8d, 1
007E3465  C7 44 24 20 00 01 00 00         mov dword ptr [rsp + 0x20], 0x100
007E346D  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
007E3472  E8 39 9F EC FF                  call 0x1406ad3b0
007E3477  85 C0                           test eax, eax
007E3479  78 1E                           js 0x1407e3499
007E347B  83 7D 24 04                     cmp dword ptr [rbp + 0x24], 4
007E347F  75 18                           jne 0x1407e3499
007E3481  8B 45 28                        mov eax, dword ptr [rbp + 0x28]
007E3484  8B 4C 05 20                     mov ecx, dword ptr [rbp + rax + 0x20]
007E3488  3B 4C 24 40                     cmp ecx, dword ptr [rsp + 0x40]
007E348C  77 07                           ja 0x1407e3495
007E348E  83 7C 24 40 FF                  cmp dword ptr [rsp + 0x40], -1
007E3493  75 04                           jne 0x1407e3499
007E3495  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
007E3499  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
007E349E  E8 0D 9E EC FF                  call 0x1406ad2b0
007E34A3  4C 89 74 24 78                  mov qword ptr [rsp + 0x78], r14
007E34A8  FF C3                           inc ebx
007E34AA  3B DF                           cmp ebx, edi
007E34AC  0F 82 D7 FE FF FF               jb 0x1407e3389
007E34B2  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
007E34B6  4C 8B 64 24 48                  mov r12, qword ptr [rsp + 0x48]
007E34BB  FF C0                           inc eax
007E34BD  48 8D 15 7C 5E 32 00            lea rdx, [rip + 0x325e7c]
007E34C4  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007E34C9  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
007E34CD  E8 AE 72 C4 FF                  call 0x14042a780
007E34D2  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
007E34D7  48 8D 44 24 40                  lea rax, [rsp + 0x40]
007E34DC  BB 04 00 00 00                  mov ebx, 4
007E34E1  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
007E34E6  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
007E34EA  44 8B CB                        mov r9d, ebx
007E34ED  45 33 C0                        xor r8d, r8d
007E34F0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E34F5  E8 D6 A7 EC FF                  call 0x1406adcd0
007E34FA  0F B7 95 10 02 00 00            movzx edx, word ptr [rbp + 0x210]
007E3501  4C 8D 4D 80                     lea r9, [rbp - 0x80]
007E3505  44 8B 06                        mov r8d, dword ptr [rsi]
007E3508  49 8B CD                        mov rcx, r13
007E350B  E8 30 03 00 00                  call 0x1407e3840
007E3510  85 C0                           test eax, eax
007E3512  78 49                           js 0x1407e355d
007E3514  48 8D 15 45 5E 32 00            lea rdx, [rip + 0x325e45]
007E351B  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007E3520  E8 5B 72 C4 FF                  call 0x14042a780
007E3525  0F B7 45 80                     movzx eax, word ptr [rbp - 0x80]
007E3529  44 8D 6B FD                     lea r13d, [rbx - 3]
007E352D  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
007E3532  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
007E3537  83 C0 02                        add eax, 2
007E353A  45 8B CD                        mov r9d, r13d
007E353D  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
007E3541  45 33 C0                        xor r8d, r8d
007E3544  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
007E3548  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E354D  E8 7E A7 EC FF                  call 0x1406adcd0
007E3552  48 8D 4D 80                     lea rcx, [rbp - 0x80]
007E3556  E8 A5 D2 1D 00                  call 0x1409c0800
007E355B  EB 06                           jmp 0x1407e3563
007E355D  41 BD 01 00 00 00               mov r13d, 1
007E3563  48 8D 15 B6 5D 32 00            lea rdx, [rip + 0x325db6]
007E356A  44 89 74 24 40                  mov dword ptr [rsp + 0x40], r14d
007E356F  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007E3574  E8 07 72 C4 FF                  call 0x14042a780
007E3579  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
007E357E  48 8D 44 24 40                  lea rax, [rsp + 0x40]
007E3583  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
007E3587  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
007E358C  44 8B CB                        mov r9d, ebx
007E358F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E3594  45 33 C0                        xor r8d, r8d
007E3597  E8 34 A7 EC FF                  call 0x1406adcd0
007E359C  48 8D 15 3D 5E 32 00            lea rdx, [rip + 0x325e3d]
007E35A3  44 89 6C 24 40                  mov dword ptr [rsp + 0x40], r13d
007E35A8  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007E35AD  E8 CE 71 C4 FF                  call 0x14042a780
007E35B2  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
007E35B7  48 8D 44 24 40                  lea rax, [rsp + 0x40]
007E35BC  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
007E35C0  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
007E35C5  44 8B CB                        mov r9d, ebx
007E35C8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E35CD  45 33 C0                        xor r8d, r8d
007E35D0  E8 FB A6 EC FF                  call 0x1406adcd0
007E35D5  48 8D 4D 10                     lea rcx, [rbp + 0x10]
007E35D9  E8 22 3F 13 00                  call 0x140917500
007E35DE  85 C0                           test eax, eax
007E35E0  78 54                           js 0x1407e3636
007E35E2  45 8A C5                        mov r8b, r13b
007E35E5  48 8D 55 C8                     lea rdx, [rbp - 0x38]
007E35E9  48 8D 4D 10                     lea rcx, [rbp + 0x10]
007E35ED  E8 5E 1E 13 00                  call 0x140915450
007E35F2  85 C0                           test eax, eax
007E35F4  78 40                           js 0x1407e3636
007E35F6  48 8D 15 B3 5D 32 00            lea rdx, [rip + 0x325db3]
007E35FD  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007E3602  E8 79 71 C4 FF                  call 0x14042a780
007E3607  0F B7 45 CA                     movzx eax, word ptr [rbp - 0x36]
007E360B  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
007E3610  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
007E3615  45 8B CD                        mov r9d, r13d
007E3618  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
007E361C  45 33 C0                        xor r8d, r8d
007E361F  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
007E3623  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E3628  E8 A3 A6 EC FF                  call 0x1406adcd0
007E362D  48 8D 4D C8                     lea rcx, [rbp - 0x38]
007E3631  E8 CA D1 1D 00                  call 0x1409c0800
007E3636  4C 8B 05 83 34 7E 00            mov r8, qword ptr [rip + 0x7e3483]
007E363D  48 8D 45 80                     lea rax, [rbp - 0x80]
007E3641  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
007E3646  45 33 C9                        xor r9d, r9d
007E3649  BA 19 00 02 00                  mov edx, 0x20019
007E364E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E3653  49 8B CC                        mov rcx, r12
007E3656  4C 89 75 80                     mov qword ptr [rbp - 0x80], r14
007E365A  E8 51 57 08 00                  call 0x140868db0
007E365F  8B D8                           mov ebx, eax
007E3661  85 C0                           test eax, eax
007E3663  0F 88 65 01 00 00               js 0x1407e37ce
007E3669  4C 8B 05 50 34 7E 00            mov r8, qword ptr [rip + 0x7e3450]
007E3670  48 8D 44 24 48                  lea rax, [rsp + 0x48]
007E3675  49 8B 0F                        mov rcx, qword ptr [r15]
007E3678  45 33 C9                        xor r9d, r9d
007E367B  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
007E3680  BA 06 00 02 00                  mov edx, 0x20006
007E3685  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007E368A  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
007E368F  E8 1C 57 08 00                  call 0x140868db0
007E3694  8B D8                           mov ebx, eax
007E3696  85 C0                           test eax, eax
007E3698  0F 88 30 01 00 00               js 0x1407e37ce
007E369E  E8 11 C3 06 00                  call 0x14084f9b4
007E36A3  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
007E36A8  48 8B 75 80                     mov rsi, qword ptr [rbp - 0x80]
007E36AC  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
007E36B1  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
007E36B9  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
007E36BD  44 8B 48 28                     mov r9d, dword ptr [rax + 0x28]
007E36C1  4C 8B 40 20                     mov r8, qword ptr [rax + 0x20]
007E36C5  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
007E36C9  8B 50 28                        mov edx, dword ptr [rax + 0x28]
007E36CC  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
007E36D0  E8 CB EA 00 00                  call 0x1407f21a0
007E36D5  8B D8                           mov ebx, eax
007E36D7  85 C0                           test eax, eax
007E36D9  0F 88 DF 00 00 00               js 0x1407e37be
007E36DF  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
007E36E3  4C 8D 44 24 48                  lea r8, [rsp + 0x48]
007E36E8  83 C9 FF                        or ecx, 0xffffffff
007E36EB  44 89 74 24 4C                  mov dword ptr [rsp + 0x4c], r14d
007E36F0  89 4C 24 48                     mov dword ptr [rsp + 0x48], ecx
007E36F4  89 4D 80                        mov dword ptr [rbp - 0x80], ecx
007E36F7  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
007E36FB  8B 50 28                        mov edx, dword ptr [rax + 0x28]
007E36FE  44 89 75 84                     mov dword ptr [rbp - 0x7c], r14d
007E3702  44 84 A9 8C 00 00 00            test byte ptr [rcx + 0x8c], r13b
007E3709  74 07                           je 0x1407e3712
007E370B  E8 50 15 07 00                  call 0x140854c60
007E3710  EB 05                           jmp 0x1407e3717
007E3712  E8 99 15 07 00                  call 0x140854cb0
007E3717  48 8B D8                        mov rbx, rax
007E371A  48 85 C0                        test rax, rax
007E371D  0F 84 96 00 00 00               je 0x1407e37b9
007E3723  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
007E3727  4C 8D 45 80                     lea r8, [rbp - 0x80]
007E372B  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
007E372F  8B 50 28                        mov edx, dword ptr [rax + 0x28]
007E3732  44 84 A9 8C 00 00 00            test byte ptr [rcx + 0x8c], r13b
007E3739  74 07                           je 0x1407e3742
007E373B  E8 20 15 07 00                  call 0x140854c60
007E3740  EB 05                           jmp 0x1407e3747
007E3742  E8 69 15 07 00                  call 0x140854cb0
007E3747  48 8B C8                        mov rcx, rax
007E374A  48 85 C0                        test rax, rax
007E374D  74 41                           je 0x1407e3790
007E374F  0F B7 43 34                     movzx eax, word ptr [rbx + 0x34]
007E3753  48 8D 55 E8                     lea rdx, [rbp - 0x18]
007E3757  66 89 41 34                     mov word ptr [rcx + 0x34], ax
007E375B  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
007E375E  89 41 38                        mov dword ptr [rcx + 0x38], eax
007E3761  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
007E3765  E8 8E 16 09 00                  call 0x140874df8
007E376A  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
007E376E  48 8D 55 80                     lea rdx, [rbp - 0x80]
007E3772  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
007E3776  44 84 A9 8C 00 00 00            test byte ptr [rcx + 0x8c], r13b
007E377D  74 07                           je 0x1407e3786
007E377F  E8 9C 94 07 00                  call 0x14085cc20
007E3784  EB 05                           jmp 0x1407e378b
007E3786  E8 B5 27 07 00                  call 0x140855f40
007E378B  41 8B DE                        mov ebx, r14d
007E378E  EB 05                           jmp 0x1407e3795
007E3790  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007E3795  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
007E3799  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
007E379E  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
007E37A2  44 84 A9 8C 00 00 00            test byte ptr [rcx + 0x8c], r13b
007E37A9  74 07                           je 0x1407e37b2
007E37AB  E8 70 94 07 00                  call 0x14085cc20
007E37B0  EB 0C                           jmp 0x1407e37be
007E37B2  E8 89 27 07 00                  call 0x140855f40
007E37B7  EB 05                           jmp 0x1407e37be
007E37B9  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007E37BE  33 D2                           xor edx, edx
007E37C0  48 8D 4D E8                     lea rcx, [rbp - 0x18]
007E37C4  E8 D7 81 C3 FF                  call 0x14041b9a0
007E37C9  E8 B6 62 3E 00                  call 0x140bc9a84
007E37CE  49 8B CC                        mov rcx, r12
007E37D1  E8 DA 9A EC FF                  call 0x1406ad2b0
007E37D6  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
007E37DB  48 85 C9                        test rcx, rcx
007E37DE  74 05                           je 0x1407e37e5
007E37E0  E8 CB 9A EC FF                  call 0x1406ad2b0
007E37E5  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
007E37E9  48 85 C9                        test rcx, rcx
007E37EC  74 05                           je 0x1407e37f3
007E37EE  E8 BD 9A EC FF                  call 0x1406ad2b0
007E37F3  85 DB                           test ebx, ebx
007E37F5  79 0D                           jns 0x1407e3804
007E37F7  49 8B 0F                        mov rcx, qword ptr [r15]
007E37FA  48 85 C9                        test rcx, rcx
007E37FD  74 05                           je 0x1407e3804
007E37FF  E8 AC 9A EC FF                  call 0x1406ad2b0
007E3804  48 8D 4D F8                     lea rcx, [rbp - 8]
007E3808  E8 43 C5 C3 FF                  call 0x14041fd50
007E380D  8B C3                           mov eax, ebx
007E380F  48 8B 8D A0 01 00 00            mov rcx, qword ptr [rbp + 0x1a0]
007E3816  48 33 CC                        xor rcx, rsp
007E3819  E8 22 8E EC FF                  call 0x1406ac640
007E381E  48 8B 9C 24 08 03 00 00         mov rbx, qword ptr [rsp + 0x308]
007E3826  48 81 C4 B0 02 00 00            add rsp, 0x2b0
007E382D  41 5F                           pop r15
007E382F  41 5E                           pop r14
007E3831  41 5D                           pop r13
007E3833  41 5C                           pop r12
007E3835  5F                              pop rdi
007E3836  5E                              pop rsi
007E3837  5D                              pop rbp
007E3838  C3                              ret
007E3839  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpCloneHwProfile(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned __int16 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m1B4;
    unsigned __int64 v_stack_m1B8;
    unsigned int v_stack_m1BC;
    unsigned int v_stack_m1C0;
    unsigned int v_stack_m1C4;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int16 v_stack_m21E;
    unsigned __int64 v_stack_m220;
    unsigned int v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned int v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned int v_stack_m264;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned int v_stack_m274;
    unsigned int v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned int v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int16 v_stack_m296;
    unsigned __int64 v_stack_m298;
    unsigned int v_stack_m29C;
    unsigned __int64 v_stack_m2A0;
    unsigned int v_stack_m2A8;
    unsigned __int64 v_stack_m2B8;
    unsigned int v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (688);
    result = (*(unsigned __int64 *)(v_rip + 6452958)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rbx = 0;
    v_stack_m2A0 = a3;
    result = 0;
    v_stack_m288 = 0;
    *(unsigned __int64 *)(a6) = 0;
    *(unsigned int *)(a7) = a4;
    v_stack_m230 = 0;
    v_stack_m228 = 0;
    v_stack_m210 = v_xmm0;
    v_stack_m280 = 0;
    v_stack_m298 = v_xmm1;
    v_stack_m278 = 0;
    v_stack_m268 = v_xmm0;
    v_stack_m2A8 = 0;
    v_stack_m220 = v_xmm1;
    v_stack_m274 = 0;
    v_stack_m250 = v_xmm0;
    v_stack_m258 = 0;
    v_stack_m240 = v_xmm0;
    v_stack_m270 = 0;
    v_stack_m1D8 = v_xmm0;
    v_stack_m1E0 = 0;
    v_stack_m200 = v_xmm0;
    v_stack_m1F0 = v_xmm1;
    result = CmpInitializeDelayDerefContext(v_stack_m200, a2, a3, a4);
    result = CmpInitializeThreadInfo(v_stack_m1F0, a2, a3, a4);
loc_007E30F8:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a7)))) >= 200) goto loc_007E3180;
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a7))) + 1);
    *(unsigned int *)(a7) = a4;
    result = swprintf_s(v_stack_mC8, 64, v_rip + 3301746, a4);
    result = RtlInitUnicodeString(v_stack_m210, v_stack_mC8, v_rip + 3301746, a4);
    v_stack_m250 = 48;
    v_stack_m240 = v_stack_m210;
    v_stack_m248 = a2;
    v_stack_m238 = 576;
    v_stack_m230 = v_xmm0;
    result = ZwOpenKey(a6, (unsigned int)(0x2001FULL), v_stack_m250, a4);
    if (sign_flag) goto loc_007E3175;
    result = ZwClose(*(unsigned __int64 *)(a6), (unsigned int)(0x2001FULL), v_stack_m250, a4);
    goto loc_007E30F8;
loc_007E3175:
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_007E37CE;
loc_007E3180:
    a4 = 0;
    a3 = 0;
    v_stack_m2C8 = v_stack_m288;
    result = ZwQuerySecurityObject(0, a4 + 4, a3, a4);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_007E31F0;
    result = ExAllocatePool2(256, (unsigned int)(v_stack_m288), (unsigned int)(0x20204D43ULL), a4);
    v_rbx = 0;
    if (result == 0) goto loc_007E31F2;
    v_stack_m2C8 = v_stack_m288;
    result = ZwQuerySecurityObject(0, v_rbx + 4, result, (unsigned int)(v_stack_m288));
    if (!sign_flag) goto loc_007E31F2;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, result, (unsigned int)(v_stack_m288));
    goto loc_007E31F2;
loc_007E31F0:
    v_rdi = 0;
loc_007E31F2:
    v_stack_m248 = 0;
    v_r14 = 0;
    v_stack_m240 = v_stack_m210;
    v_stack_m250 = 48;
    v_stack_m2B8 = v_stack_m278;
    v_stack_m2C0 = 0;
    a4 = 0;
    v_stack_m2C8 = 0;
    v_stack_m238 = 576;
    v_stack_m230 = 0;
    v_stack_m228 = 0;
    result = ZwCreateKey(a6, (unsigned int)(0x2001FULL), v_stack_m250, a4);
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, v_stack_m250, a4);
    }
    if (sign_flag) goto loc_007E37CE;
    if (v_stack_m278 == 1) goto loc_007E3267;
    goto loc_007E37CE;
loc_007E3267:
    result = swprintf_s(v_stack_mC8, 64, v_rip + 3301759, (unsigned int)(*(unsigned int *)(a7)));
    result = RtlInitUnicodeString(v_stack_m298, v_stack_mC8, v_rip + 3301759, (unsigned int)(*(unsigned int *)(a7)));
    v_stack_m248 = a1;
    v_stack_m240 = v_stack_m298;
    v_stack_m238 = 576;
    v_stack_m2B8 = v_stack_m278;
    v_stack_m2C0 = 0;
    v_stack_m2C8 = 0;
    a4 = 0;
    v_stack_m250 = 48;
    v_stack_m230 = v_xmm0;
    result = ZwCreateKey(v_stack_m280, (unsigned int)(0x2001FULL), v_stack_m250, a4);
    if (!sign_flag) goto loc_007E32F1;
    v_stack_m280 = 0;
    goto loc_007E37CE;
loc_007E32F1:
    result = RtlInitUnicodeString(v_stack_m298, v_rip + 3300920, v_stack_m250, a4);
    v_stack_m250 = 48;
    v_stack_m240 = v_stack_m298;
    v_stack_m248 = a1;
    v_stack_m238 = 576;
    v_stack_m230 = v_xmm0;
    result = ZwOpenKey(v_stack_m258, (unsigned int)(0x20019ULL), v_stack_m250, a4);
    if (!sign_flag) goto loc_007E3342;
    v_stack_m258 = 0;
    goto loc_007E37CE;
loc_007E3342:
    v_stack_m2C8 = v_stack_m274;
    result = ZwQueryKey(v_stack_m258, 2, v_stack_m1C8, 256);
    if (sign_flag) goto loc_007E37CE;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    v_stack_m2A8 = (unsigned int)(result);
    if ((unsigned int)((unsigned int)(v_stack_m1B4)) == 0) goto loc_007E34BB;
loc_007E3389:
    v_stack_m2C0 = v_stack_m274;
    a3 = 0;
    v_stack_m2C8 = 254;
    result = ZwEnumerateKey(v_stack_m258, 0, a3, v_stack_m1C8);
    if (sign_flag) goto loc_007E34B2;
    result = ((unsigned int)(v_stack_m1BC)) >> (1);
    *(unsigned __int16 *)(v_stack_m1E8 + result * 2 + 48) = 0;
    result = wtoi(v_stack_m1B8, 0, a3, v_stack_m1C8);
    if ((unsigned int)(result) == 0) goto loc_007E34A8;
    result = wtoi(v_stack_m1B8, 0, a3, v_stack_m1C8);
    if (((unsigned int)(result)) == (*(unsigned int *)(a7))) goto loc_007E34A8;
    v_stack_m298 = (unsigned __int16)((unsigned int)(v_stack_m1BC));
    result = (unsigned __int16)(((unsigned int)(v_stack_m1BC)) + (2));
    v_stack_m250 = 48;
    v_stack_m296 = (unsigned __int16)(result);
    v_stack_m238 = 576;
    v_stack_m290 = v_stack_m1B8;
    v_stack_m248 = v_stack_m258;
    v_stack_m240 = v_stack_m298;
    v_stack_m230 = v_xmm0;
    result = ZwOpenKey(v_stack_m270, (unsigned int)(0x20019ULL), v_stack_m250, v_stack_m1C8);
    if (sign_flag) goto loc_007E34A3;
    result = RtlInitUnicodeString(v_stack_m298, v_rip + 3301118, v_stack_m250, v_stack_m1C8);
    v_stack_m2C0 = v_stack_m274;
    v_stack_m2C8 = 256;
    result = ZwQueryValueKey(v_stack_m270, v_stack_m298, 1, v_stack_m1C8);
    if (sign_flag) goto loc_007E3499;
    if (v_stack_m1C4 != 4) goto loc_007E3499;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1E8 + (unsigned int)(v_stack_m1C0) * 1 + 32)))) > v_stack_m2A8) goto loc_007E3495;
    if (v_stack_m2A8 == -1) {
        v_stack_m2A8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1E8 + (unsigned int)(v_stack_m1C0) * 1 + 32)));
    }
    result = ZwClose(v_stack_m270, v_stack_m298, 1, v_stack_m1C8);
loc_007E34A3:
    v_stack_m270 = 0;
loc_007E34A8:
    v_rbx = (unsigned int)((0) + 1);
    if (((unsigned int)(v_rbx)) < ((unsigned int)((unsigned int)(v_stack_m1B4)))) goto loc_007E3389;
loc_007E34B2:
loc_007E34BB:
    result = (unsigned int)(((unsigned int)(v_stack_m2A8)) + 1);
    v_stack_m2A8 = (unsigned int)(result);
    result = RtlInitUnicodeString(v_stack_m298, v_rip + 3300988, 1, v_stack_m1C8);
    v_stack_m2C0 = 4;
    a3 = 0;
    v_stack_m2C8 = v_stack_m2A8;
    result = ZwSetValueKey(v_stack_m280, v_stack_m298, a3, 4);
    result = CmpCreateHwProfileFriendlyName(a1, a5, (unsigned int)(*(unsigned int *)(a7)), v_stack_m268);
    if (sign_flag) goto loc_007E355D;
    result = RtlInitUnicodeString(v_stack_m298, v_rip + 3300933, (unsigned int)(*(unsigned int *)(a7)), v_stack_m268);
    result = (unsigned int)((v_stack_m268) + (2));
    v_stack_m2C0 = (unsigned int)(result);
    a3 = 0;
    v_stack_m2C8 = v_stack_m260;
    result = ZwSetValueKey(v_stack_m280, v_stack_m298, a3, (unsigned int)((unsigned int)(4 - 3)));
    result = RtlFreeAnsiString(v_stack_m268, v_stack_m298, a3, (unsigned int)((unsigned int)(4 - 3)));
    goto loc_007E3563;
loc_007E355D:
loc_007E3563:
    v_stack_m2A8 = 0;
    result = RtlInitUnicodeString(v_stack_m298, v_rip + 3300790, a3, (unsigned int)((unsigned int)(4 - 3)));
    v_stack_m2C0 = 4;
    v_stack_m2C8 = v_stack_m2A8;
    a3 = 0;
    result = ZwSetValueKey(v_stack_m280, v_stack_m298, a3, 4);
    v_stack_m2A8 = 1;
    result = RtlInitUnicodeString(v_stack_m298, v_rip + 3300925, a3, 4);
    v_stack_m2C0 = 4;
    v_stack_m2C8 = v_stack_m2A8;
    a3 = 0;
    result = ZwSetValueKey(v_stack_m280, v_stack_m298, a3, 4);
    result = ExUuidCreate(v_stack_m1D8, v_stack_m298, a3, 4);
    if (sign_flag) goto loc_007E3636;
    result = RtlStringFromGUIDEx(v_stack_m1D8, v_stack_m220, 1, 4);
    if (!(sign_flag)) {
        a2 = v_rip + 3300787;
        a1 = v_stack_m298;
        result = RtlInitUnicodeString(a1, a2, 1, 4);
        result = v_stack_m21E;
        a2 = v_stack_m298;
        a1 = v_stack_m280;
        a4 = 1;
        v_stack_m2C0 = (unsigned int)(result);
        a3 = 0;
        result = v_stack_m218;
        v_stack_m2C8 = result;
        result = ZwSetValueKey(a1, a2, a3, a4);
        a1 = v_stack_m220;
        result = RtlFreeAnsiString(a1, a2, a3, a4);
    }
    v_stack_m2C0 = 0;
    a4 = 0;
    v_stack_m2C8 = v_stack_m268;
    v_stack_m268 = 0;
    result = ObReferenceObjectByHandle(v_stack_m2A0, (unsigned int)(0x20019ULL), *(unsigned __int64 *)(v_rip + 8270979), a4);
    if (sign_flag) goto loc_007E37CE;
    a4 = 0;
    v_stack_m2C0 = 0;
    v_stack_m2C8 = v_stack_m2A0;
    v_stack_m2A0 = 0;
    result = ObReferenceObjectByHandle(*(unsigned __int64 *)(a6), (unsigned int)(0x20006ULL), *(unsigned __int64 *)(v_rip + 8270928), a4);
    if (sign_flag) goto loc_007E37CE;
    result = CmpLockRegistryExclusive(*(unsigned __int64 *)(a6), (unsigned int)(0x20006ULL), *(unsigned __int64 *)(v_rip + 8270928), a4);
    v_stack_m2C0 = 0;
    v_stack_m2C8 = 2;
    result = CmpCopySyncTree(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m268 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m268 + 8) + 40)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 40)));
    if (sign_flag) goto loc_007E37BE;
    a1 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m268 + 8) + 32)) | (0xFFFFFFFFULL));
    v_stack_m29C = 0;
    v_stack_m2A0 = (unsigned int)(a1);
    v_stack_m268 = (unsigned int)(a1);
    v_stack_m264 = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m268 + 8) + 32) + 140)) & (1)) == 0) goto loc_007E3712;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m268 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m268 + 8) + 40)), v_stack_m2A0, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 40)));
    goto loc_007E3717;
loc_007E3712:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m268 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m268 + 8) + 40)), v_stack_m2A0, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 40)));
loc_007E3717:
    if (result == 0) goto loc_007E37B9;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 32) + 140)) & (1)) == 0) goto loc_007E3742;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 40)), v_stack_m268, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 40)));
    goto loc_007E3747;
loc_007E3742:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 40)), v_stack_m268, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 40)));
loc_007E3747:
    if (result == 0) goto loc_007E3790;
    *(unsigned __int16 *)(result + 52) = (unsigned __int16)(*(unsigned __int16 *)(result + 52));
    *(unsigned int *)(result + 56) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 56)));
    result = CmpRebuildKcbCache(*(unsigned __int64 *)(v_stack_m2A0 + 8), v_stack_m200, v_stack_m268, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 40)));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 32) + 140)) & (1)) == 0) goto loc_007E3786;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 32), v_stack_m268, v_stack_m268, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 40)));
    goto loc_007E378B;
loc_007E3786:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 32), v_stack_m268, v_stack_m268, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 40)));
loc_007E378B:
    goto loc_007E3795;
loc_007E3790:
loc_007E3795:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m268 + 8) + 32) + 140)) & (1)) == 0) goto loc_007E37B2;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m268 + 8) + 32), v_stack_m2A0, v_stack_m268, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 40)));
    goto loc_007E37BE;
loc_007E37B2:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m268 + 8) + 32), v_stack_m2A0, v_stack_m268, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 40)));
    goto loc_007E37BE;
loc_007E37B9:
loc_007E37BE:
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m200, a2, v_stack_m268, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 40)));
    result = CmpUnlockRegistry(v_stack_m200, a2, v_stack_m268, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 40)));
loc_007E37CE:
    result = ZwClose(v_stack_m2A0, a2, v_stack_m268, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 40)));
    if (v_stack_m280 != 0) {
        result = ZwClose(v_stack_m280, a2, v_stack_m268, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 40)));
    }
    if (v_stack_m258 != 0) {
        result = ZwClose(v_stack_m258, a2, v_stack_m268, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 40)));
    }
    if (!sign_flag) goto loc_007E3804;
    if (*(unsigned __int64 *)(a6) != 0) {
        result = ZwClose(*(unsigned __int64 *)(a6), a2, v_stack_m268, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 40)));
    }
    result = CmCleanupThreadInfo(v_stack_m1F0, a2, v_stack_m268, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 40)));
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m268, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2A0 + 8) + 40)));
    v_rsp = (v_rsp) + (688);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpCloneHwProfile(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint16_t Arg5, void *Arg6, void *Arg7)
{
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m1B4;
    uint64_t v_stack_m1B8;
    uint32_t v_stack_m1BC;
    uint32_t v_stack_m1C0;
    uint32_t v_stack_m1C4;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m200;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint16_t v_stack_m21E;
    uint64_t v_stack_m220;
    uint32_t v_stack_m228;
    uint64_t v_stack_m230;
    uint32_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint32_t v_stack_m264;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint32_t v_stack_m274;
    uint32_t v_stack_m278;
    uint64_t v_stack_m280;
    uint32_t v_stack_m288;
    uint64_t v_stack_m290;
    uint16_t v_stack_m296;
    uint64_t v_stack_m298;
    uint32_t v_stack_m29C;
    uint64_t v_stack_m2A0;
    uint32_t v_stack_m2A8;
    uint64_t v_stack_m2B8;
    uint32_t v_stack_m2C0;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m48;
    uint64_t v_stack_mC8;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (688);
    result = (*(uint64_t *)(v_rip + 0x6276DE)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rbx = 0;
    v_stack_m2A0 = Arg3;
    result = 0;
    v_stack_m288 = 0;
    *(uint64_t *)(arg6) = 0;
    *(uint32_t *)(arg7) = Arg4;
    v_stack_m230 = 0;
    v_stack_m228 = 0;
    v_stack_m210 = v_xmm0;
    v_stack_m280 = 0;
    v_stack_m298 = v_xmm1;
    v_stack_m278 = 0;
    v_stack_m268 = v_xmm0;
    v_stack_m2A8 = 0;
    v_stack_m220 = v_xmm1;
    v_stack_m274 = 0;
    v_stack_m250 = v_xmm0;
    v_stack_m258 = 0;
    v_stack_m240 = v_xmm0;
    v_stack_m270 = 0;
    v_stack_m1D8 = v_xmm0;
    v_stack_m1E0 = 0;
    v_stack_m200 = v_xmm0;
    v_stack_m1F0 = v_xmm1;
    result = CmpInitializeDelayDerefContext(v_stack_m200, Arg2, Arg3, Arg4);
    result = CmpInitializeThreadInfo(v_stack_m1F0, Arg2, Arg3, Arg4);
loc_007E30F8:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg7)))) >= 200) goto loc_007E3180;
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg7))) + 1);
    *(uint32_t *)(arg7) = Arg4;
    result = swprintf_s(v_stack_mC8, 64, v_rip + 3301746, Arg4);
    result = RtlInitUnicodeString(v_stack_m210, v_stack_mC8, v_rip + 3301746, Arg4);
    v_stack_m250 = 48;
    v_stack_m240 = v_stack_m210;
    v_stack_m248 = Arg2;
    v_stack_m238 = 576;
    v_stack_m230 = v_xmm0;
    result = ZwOpenKey(Arg6, (uint32_t)(0x2001FULL), v_stack_m250, Arg4);
    if (sign_flag) goto loc_007E3175;
    result = ZwClose(*(uint64_t *)(arg6), (uint32_t)(0x2001FULL), v_stack_m250, Arg4);
    goto loc_007E30F8;
loc_007E3175:
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_007E37CE;
loc_007E3180:
    Arg4 = 0;
    Arg3 = 0;
    v_stack_m2C8 = v_stack_m288;
    result = ZwQuerySecurityObject(0, Arg4 + 4, Arg3, Arg4);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_007E31F0;
    result = ExAllocatePool2(256, (uint32_t)(v_stack_m288), (uint32_t)(0x20204D43ULL), Arg4);
    local_rbx = 0;
    if (result == 0) goto loc_007E31F2;
    v_stack_m2C8 = v_stack_m288;
    result = ZwQuerySecurityObject(0, local_rbx + 4, result, (uint32_t)(v_stack_m288));
    if (!sign_flag) goto loc_007E31F2;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, result, (uint32_t)(v_stack_m288));
    goto loc_007E31F2;
loc_007E31F0:
    local_rdi = 0;
loc_007E31F2:
    v_stack_m248 = 0;
    local_r14 = 0;
    v_stack_m240 = v_stack_m210;
    v_stack_m250 = 48;
    v_stack_m2B8 = v_stack_m278;
    v_stack_m2C0 = 0;
    Arg4 = 0;
    v_stack_m2C8 = 0;
    v_stack_m238 = 576;
    v_stack_m230 = 0;
    v_stack_m228 = 0;
    result = ZwCreateKey(Arg6, (uint32_t)(0x2001FULL), v_stack_m250, Arg4);
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m250, Arg4);
    }
    if (sign_flag) goto loc_007E37CE;
    if (v_stack_m278 == 1) goto loc_007E3267;
    goto loc_007E37CE;
loc_007E3267:
    result = swprintf_s(v_stack_mC8, 64, v_rip + 3301759, (uint32_t)(*(uint32_t *)(arg7)));
    result = RtlInitUnicodeString(v_stack_m298, v_stack_mC8, v_rip + 3301759, (uint32_t)(*(uint32_t *)(arg7)));
    v_stack_m248 = Arg1;
    v_stack_m240 = v_stack_m298;
    v_stack_m238 = 576;
    v_stack_m2B8 = v_stack_m278;
    v_stack_m2C0 = 0;
    v_stack_m2C8 = 0;
    Arg4 = 0;
    v_stack_m250 = 48;
    v_stack_m230 = v_xmm0;
    result = ZwCreateKey(v_stack_m280, (uint32_t)(0x2001FULL), v_stack_m250, Arg4);
    if (!sign_flag) goto loc_007E32F1;
    v_stack_m280 = 0;
    goto loc_007E37CE;
loc_007E32F1:
    result = RtlInitUnicodeString(v_stack_m298, v_rip + 3300920, v_stack_m250, Arg4);
    v_stack_m250 = 48;
    v_stack_m240 = v_stack_m298;
    v_stack_m248 = Arg1;
    v_stack_m238 = 576;
    v_stack_m230 = v_xmm0;
    result = ZwOpenKey(v_stack_m258, (uint32_t)(0x20019ULL), v_stack_m250, Arg4);
    if (!sign_flag) goto loc_007E3342;
    v_stack_m258 = 0;
    goto loc_007E37CE;
loc_007E3342:
    v_stack_m2C8 = v_stack_m274;
    result = ZwQueryKey(v_stack_m258, 2, v_stack_m1C8, 256);
    if (sign_flag) goto loc_007E37CE;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    v_stack_m2A8 = (uint32_t)(result);
    if ((uint32_t)((uint32_t)(v_stack_m1B4)) == 0) goto loc_007E34BB;
loc_007E3389:
    v_stack_m2C0 = v_stack_m274;
    Arg3 = 0;
    v_stack_m2C8 = 254;
    result = ZwEnumerateKey(v_stack_m258, 0, Arg3, v_stack_m1C8);
    if (sign_flag) goto loc_007E34B2;
    result = ((uint32_t)(v_stack_m1BC)) >> (1);
    *(uint16_t *)(v_stack_m1E8 + result * 2 + 0x30) = 0;
    result = wtoi(v_stack_m1B8, 0, Arg3, v_stack_m1C8);
    if ((uint32_t)(result) == 0) goto loc_007E34A8;
    result = wtoi(v_stack_m1B8, 0, Arg3, v_stack_m1C8);
    if (((uint32_t)(result)) == (*(uint32_t *)(arg7))) goto loc_007E34A8;
    v_stack_m298 = (uint16_t)((uint32_t)(v_stack_m1BC));
    result = (uint16_t)(((uint32_t)(v_stack_m1BC)) + (2));
    v_stack_m250 = 48;
    v_stack_m296 = (uint16_t)(result);
    v_stack_m238 = 576;
    v_stack_m290 = v_stack_m1B8;
    v_stack_m248 = v_stack_m258;
    v_stack_m240 = v_stack_m298;
    v_stack_m230 = v_xmm0;
    result = ZwOpenKey(v_stack_m270, (uint32_t)(0x20019ULL), v_stack_m250, v_stack_m1C8);
    if (sign_flag) goto loc_007E34A3;
    result = RtlInitUnicodeString(v_stack_m298, v_rip + 3301118, v_stack_m250, v_stack_m1C8);
    v_stack_m2C0 = v_stack_m274;
    v_stack_m2C8 = 256;
    result = ZwQueryValueKey(v_stack_m270, v_stack_m298, 1, v_stack_m1C8);
    if (sign_flag) goto loc_007E3499;
    if (v_stack_m1C4 != 4) goto loc_007E3499;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1E8 + (uint32_t)(v_stack_m1C0) * 1 + 0x20)))) > v_stack_m2A8) goto loc_007E3495;
    if (v_stack_m2A8 == -1) {
        v_stack_m2A8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1E8 + (uint32_t)(v_stack_m1C0) * 1 + 0x20)));
    }
    result = ZwClose(v_stack_m270, v_stack_m298, 1, v_stack_m1C8);
loc_007E34A3:
    v_stack_m270 = 0;
loc_007E34A8:
    local_rbx = (uint32_t)((0) + 1);
    if (((uint32_t)(local_rbx)) < ((uint32_t)((uint32_t)(v_stack_m1B4)))) goto loc_007E3389;
loc_007E34B2:
loc_007E34BB:
    result = (uint32_t)(((uint32_t)(v_stack_m2A8)) + 1);
    v_stack_m2A8 = (uint32_t)(result);
    result = RtlInitUnicodeString(v_stack_m298, v_rip + 3300988, 1, v_stack_m1C8);
    v_stack_m2C0 = 4;
    Arg3 = 0;
    v_stack_m2C8 = v_stack_m2A8;
    result = ZwSetValueKey(v_stack_m280, v_stack_m298, Arg3, 4);
    result = CmpCreateHwProfileFriendlyName(Arg1, Arg5, (uint32_t)(*(uint32_t *)(arg7)), v_stack_m268);
    if (sign_flag) goto loc_007E355D;
    result = RtlInitUnicodeString(v_stack_m298, v_rip + 3300933, (uint32_t)(*(uint32_t *)(arg7)), v_stack_m268);
    result = (uint32_t)((v_stack_m268) + (2));
    v_stack_m2C0 = (uint32_t)(result);
    Arg3 = 0;
    v_stack_m2C8 = v_stack_m260;
    result = ZwSetValueKey(v_stack_m280, v_stack_m298, Arg3, (uint32_t)((uint32_t)(4 - 3)));
    result = RtlFreeAnsiString(v_stack_m268, v_stack_m298, Arg3, (uint32_t)((uint32_t)(4 - 3)));
    goto loc_007E3563;
loc_007E355D:
loc_007E3563:
    v_stack_m2A8 = 0;
    result = RtlInitUnicodeString(v_stack_m298, v_rip + 3300790, Arg3, (uint32_t)((uint32_t)(4 - 3)));
    v_stack_m2C0 = 4;
    v_stack_m2C8 = v_stack_m2A8;
    Arg3 = 0;
    result = ZwSetValueKey(v_stack_m280, v_stack_m298, Arg3, 4);
    v_stack_m2A8 = 1;
    result = RtlInitUnicodeString(v_stack_m298, v_rip + 3300925, Arg3, 4);
    v_stack_m2C0 = 4;
    v_stack_m2C8 = v_stack_m2A8;
    Arg3 = 0;
    result = ZwSetValueKey(v_stack_m280, v_stack_m298, Arg3, 4);
    result = ExUuidCreate(v_stack_m1D8, v_stack_m298, Arg3, 4);
    if (sign_flag) goto loc_007E3636;
    result = RtlStringFromGUIDEx(v_stack_m1D8, v_stack_m220, 1, 4);
    if (!(sign_flag)) {
        Arg2 = v_rip + 3300787;
        Arg1 = v_stack_m298;
        result = RtlInitUnicodeString(Arg1, Arg2, 1, 4);
        result = v_stack_m21E;
        Arg2 = v_stack_m298;
        Arg1 = v_stack_m280;
        Arg4 = 1;
        v_stack_m2C0 = (uint32_t)(result);
        Arg3 = 0;
        result = v_stack_m218;
        v_stack_m2C8 = result;
        result = ZwSetValueKey(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_m220;
        result = RtlFreeAnsiString(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m2C0 = 0;
    Arg4 = 0;
    v_stack_m2C8 = v_stack_m268;
    v_stack_m268 = 0;
    result = ObReferenceObjectByHandle(v_stack_m2A0, (uint32_t)(0x20019ULL), *(uint64_t *)(v_rip + 0x7E3483), Arg4);
    if (sign_flag) goto loc_007E37CE;
    Arg4 = 0;
    v_stack_m2C0 = 0;
    v_stack_m2C8 = v_stack_m2A0;
    v_stack_m2A0 = 0;
    result = ObReferenceObjectByHandle(*(uint64_t *)(arg6), (uint32_t)(0x20006ULL), *(uint64_t *)(v_rip + 0x7E3450), Arg4);
    if (sign_flag) goto loc_007E37CE;
    result = CmpLockRegistryExclusive(*(uint64_t *)(arg6), (uint32_t)(0x20006ULL), *(uint64_t *)(v_rip + 0x7E3450), Arg4);
    v_stack_m2C0 = 0;
    v_stack_m2C8 = 2;
    result = CmpCopySyncTree(*(uint64_t *)(*(uint64_t *)(v_stack_m268 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m268 + 0x8) + 0x28)), *(uint64_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x28)));
    if (sign_flag) goto loc_007E37BE;
    Arg1 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(v_stack_m268 + 0x8) + 0x20)) | (0xFFFFFFFFULL));
    v_stack_m29C = 0;
    v_stack_m2A0 = (uint32_t)(Arg1);
    v_stack_m268 = (uint32_t)(Arg1);
    v_stack_m264 = 0;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m268 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007E3712;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(v_stack_m268 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m268 + 0x8) + 0x28)), v_stack_m2A0, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x28)));
    goto loc_007E3717;
loc_007E3712:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(v_stack_m268 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m268 + 0x8) + 0x28)), v_stack_m2A0, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x28)));
loc_007E3717:
    if (result == 0) goto loc_007E37B9;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007E3742;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x28)), v_stack_m268, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x28)));
    goto loc_007E3747;
loc_007E3742:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x28)), v_stack_m268, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x28)));
loc_007E3747:
    if (result == 0) goto loc_007E3790;
    *(uint16_t *)(result + 0x34) = (uint16_t)(*(uint16_t *)(result + 0x34));
    *(uint32_t *)(result + 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x38)));
    result = CmpRebuildKcbCache(*(uint64_t *)(v_stack_m2A0 + 0x8), v_stack_m200, v_stack_m268, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x28)));
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007E3786;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x20), v_stack_m268, v_stack_m268, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x28)));
    goto loc_007E378B;
loc_007E3786:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x20), v_stack_m268, v_stack_m268, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x28)));
loc_007E378B:
    goto loc_007E3795;
loc_007E3790:
loc_007E3795:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m268 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007E37B2;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(v_stack_m268 + 0x8) + 0x20), v_stack_m2A0, v_stack_m268, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x28)));
    goto loc_007E37BE;
loc_007E37B2:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(v_stack_m268 + 0x8) + 0x20), v_stack_m2A0, v_stack_m268, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x28)));
    goto loc_007E37BE;
loc_007E37B9:
loc_007E37BE:
    Arg2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m200, Arg2, v_stack_m268, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x28)));
    result = CmpUnlockRegistry(v_stack_m200, Arg2, v_stack_m268, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x28)));
loc_007E37CE:
    result = ZwClose(v_stack_m2A0, Arg2, v_stack_m268, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x28)));
    if (v_stack_m280 != 0) {
        result = ZwClose(v_stack_m280, Arg2, v_stack_m268, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x28)));
    }
    if (v_stack_m258 != 0) {
        result = ZwClose(v_stack_m258, Arg2, v_stack_m268, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x28)));
    }
    if (!sign_flag) goto loc_007E3804;
    if (*(uint64_t *)(arg6) != 0) {
        result = ZwClose(*(uint64_t *)(arg6), Arg2, v_stack_m268, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x28)));
    }
    result = CmCleanupThreadInfo(v_stack_m1F0, Arg2, v_stack_m268, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x28)));
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m268, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2A0 + 0x8) + 0x28)));
    local_rsp = (local_rsp) + (688);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `64` | `R` |
| `Arg6` | `+ 0x0` | `64` | `W` |
| `Arg7` | `+ 0x0` | `32` | `R` |
| `Arg7` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007E303C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
